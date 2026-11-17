import copy
import unittest
from unittest.mock import patch
from test_site_assets import build

class WeeklyFreshnessTest(unittest.TestCase):
    def test_foundations_do_not_appear_in_week_calendar(self):
        payload = build.build_payload()
        foundations = [p for p in payload['papers'] if p.get('collection') == 'foundation']
        self.assertGreaterEqual(len(foundations), 10)
        self.assertNotIn('security-foundations', {w['id'] for w in payload['weeks']})
        self.assertTrue(all(p['cached'] and len(p['details']['easycatch']) == 2 for p in foundations))

    def test_missing_window_event_fails_build(self):
        papers = copy.deepcopy(build.load_index())
        paper = next(p for p in papers if p['id'] == 'arxiv-2610-38438-rolefuzzer')
        paper.pop('discovery_events')
        with patch.object(build, 'load_index', return_value=papers):
            with self.assertRaisesRegex(ValueError, 'missing verified in-window'):
                build.build_payload()

    def test_old_date_cannot_fill_a_current_week(self):
        papers = copy.deepcopy(build.load_index())
        paper = next(p for p in papers if p['id'] == 'arxiv-2610-38438-rolefuzzer')
        paper['discovery_events'][0]['date'] = '2024-10-28'
        with patch.object(build, 'load_index', return_value=papers):
            with self.assertRaisesRegex(ValueError, 'missing verified in-window'):
                build.build_payload()

    def test_substantive_update_needs_concrete_change(self):
        papers = copy.deepcopy(build.load_index())
        paper = next(p for p in papers if p['id'] == 'arxiv-2611-10099-enmo-safety')
        paper['discovery_events'][0].pop('change')
        with patch.object(build, 'load_index', return_value=papers):
            with self.assertRaisesRegex(ValueError, 'substantive update needs'):
                build.build_payload()

    def test_future_issue_requires_a_declared_window(self):
        papers = copy.deepcopy(build.load_index())
        paper = next(p for p in papers if p['id'] == 'arxiv-2610-38438-rolefuzzer')
        paper['weekly_notes'] = ['weekly/2026/2026-W48.md']
        with patch.object(build, 'load_index', return_value=papers):
            with self.assertRaisesRegex(ValueError, 'declare 2026-W48'):
                build.build_payload()
