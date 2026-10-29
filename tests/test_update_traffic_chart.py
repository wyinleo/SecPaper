import datetime as dt
import io
import json
import sys
import unittest
import urllib.error
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import update_traffic_chart as traffic  # noqa: E402


class JsonResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()


def http_error(status: int, message: str) -> urllib.error.HTTPError:
    return urllib.error.HTTPError(
        "https://example.goatcounter.com/api/v0/stats/total",
        status,
        message,
        {},
        io.BytesIO(json.dumps({"error": message}).encode()),
    )


class FetchStatsTests(unittest.TestCase):
    def test_retries_transient_404_then_succeeds(self):
        responses = [http_error(404, "not found"), JsonResponse(b'{"stats":[]}')]
        delays = []

        def urlopen(_request, timeout):
            self.assertEqual(timeout, 30)
            response = responses.pop(0)
            if isinstance(response, Exception):
                raise response
            return response

        result = traffic.fetch_stats(
            "example",
            "token",
            dt.date(2026, 8, 13),
            urlopen=urlopen,
            sleep=delays.append,
        )

        self.assertEqual(result, {"stats": []})
        self.assertEqual(delays, [5])

    def test_recovers_after_four_connection_resets(self):
        attempts = 0
        delays = []

        def urlopen(_request, timeout):
            nonlocal attempts
            attempts += 1
            if attempts <= 4:
                raise urllib.error.URLError(ConnectionResetError(104, "Connection reset by peer"))
            return JsonResponse(b'{"stats":[{"day":"2026-10-15","daily":3}]}')

        result = traffic.fetch_stats(
            "example", "token", dt.date(2026, 10, 15),
            urlopen=urlopen, sleep=delays.append,
        )

        self.assertEqual(result["stats"][0]["daily"], 3)
        self.assertEqual(attempts, 5)
        self.assertEqual(delays, [5, 10, 20, 40])

    def test_does_not_retry_authentication_error(self):
        attempts = 0

        def urlopen(_request, timeout):
            nonlocal attempts
            attempts += 1
            raise http_error(401, "unauthorized")

        with self.assertRaisesRegex(SystemExit, "HTTP 401: unauthorized"):
            traffic.fetch_stats(
                "example",
                "token",
                dt.date(2026, 8, 13),
                urlopen=urlopen,
                sleep=lambda _delay: None,
            )

        self.assertEqual(attempts, 1)

    def test_stops_after_bounded_network_retries(self):
        attempts = 0
        delays = []

        def urlopen(_request, timeout):
            nonlocal attempts
            attempts += 1
            raise urllib.error.URLError("temporary DNS failure")

        with self.assertRaisesRegex(SystemExit, "temporary DNS failure"):
            traffic.fetch_stats(
                "example",
                "token",
                dt.date(2026, 8, 13),
                urlopen=urlopen,
                sleep=delays.append,
            )

        self.assertEqual(attempts, traffic.MAX_FETCH_ATTEMPTS)
        self.assertEqual(delays, [5, 10, 20, 40, 60])


class CumulativeTests(unittest.TestCase):
    def test_keeps_old_days_and_replaces_repeated_dates(self):
        history = {"2026-08-01": 10, "2026-09-29": 2}
        payload = {"stats": [{"day": "2026-09-29", "daily": 3}]}
        for _ in range(2):
            history.update({day.isoformat(): count for day, count in traffic.daily_series(
                payload, dt.date(2026, 9, 30), dt.date(2026, 9, 29))})
        series = traffic.cumulative_series(history)
        self.assertEqual([count for _, count in series], [10, 13, 13])
        svg = traffic.render_svg(series, dt.datetime.now(dt.timezone.utc))
        self.assertIn("累计 13 次访问", svg)

    def test_explicit_zero_is_preserved(self):
        series = traffic.daily_series({"stats": [{"day": "2026-09-30", "daily": 0, "hourly": [3]}]},
                                      dt.date(2026, 9, 30), dt.date(2026, 9, 30))
        self.assertEqual(series[0][1], 0)

    def test_missing_stats_does_not_erase_history(self):
        with self.assertRaises(KeyError):
            traffic.daily_series({}, dt.date(2026, 9, 30))


if __name__ == "__main__":
    unittest.main()


class SelfHostedTests(unittest.TestCase):
    def test_history_endpoint_does_not_send_goatcounter_credentials(self):
        def urlopen(request, timeout):
            self.assertEqual(request.full_url, "https://example.com/r/code/api/history")
            self.assertIsNone(request.get_header("Authorization"))
            return JsonResponse(b'{"stats":[{"day":"2026-10-29","daily":3}]}')
        payload = traffic.fetch_stats("", "", dt.date(2026, 10, 29),
            endpoint="https://example.com/r/code/api/history", urlopen=urlopen)
        self.assertEqual(traffic.daily_series(payload, dt.date(2026, 10, 29), dt.date(2026, 10, 29))[0][1], 3)
