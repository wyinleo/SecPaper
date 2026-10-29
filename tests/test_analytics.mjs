import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const source = readFileSync(new URL('../site/analytics.js', import.meta.url), 'utf8');
function browser({ hidden = false, optout = false, host = 'wyinleo.github.io', dnt = false } = {}) {
    const calls = [], events = {}, timers = [], storage = new Map();
    if (optout) storage.set('skipgc', 't');
    const nodes = Object.fromEntries(['total', 'today', 'month'].map(k => ['visit-' + k, { textContent: '—', removeAttribute() {} }]));
    const document = { visibilityState: hidden ? 'hidden' : 'visible',
        currentScript: { getAttribute: () => 'aHR0cHM6Ly95YW1heXVraS5zcGFjZS9yLzdjNjJkOTUzYTBlZjQ5OGI=' },
        getElementById: id => nodes[id], querySelector: () => null,
        addEventListener: (event, callback) => { events[event] = callback; } };
    const window = { PAPERNOTE_ANALYTICS: { allowedHosts: ['wyinleo.github.io'], endpointCode: btoa('https://yamayuki.space/r/b84e19f620d34ac7') } }; window.top = window; window.self = window;
    vm.runInNewContext(source, { document, window, URL, atob, AbortController, navigator: { doNotTrack: dnt ? '1' : '0' }, setTimeout, clearTimeout,
        setInterval: (fn, delay) => { timers.push({ fn, delay }); },
        location: new URL('https://' + host + '/SecPaper/'),
        crypto: { randomUUID: () => 'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb' },
        localStorage: { getItem: k => storage.get(k) || null, setItem: (k, v) => storage.set(k, v) },
        fetch: async (url, options) => { calls.push({ url, options }); return { ok: true, json: async () => ({ total: 12, today: 2, month: 10 }) }; }
    });
    return { calls, events, timers, nodes, document };
}
const settle = () => new Promise(resolve => setImmediate(resolve));
test('one visit per page load; refresh timers only read statistics', async () => {
    const page = browser(); await settle();
    assert.equal(page.calls.length, 1);
    assert.equal(page.calls[0].options.method, 'POST');
    assert.equal(JSON.parse(page.calls[0].options.body).path, '/SecPaper/');
    assert.equal(page.nodes['visit-total'].textContent, '12');
    assert.equal(page.nodes['visit-today'].textContent, '2');
    assert.equal(page.nodes['visit-month'].textContent, '10');
    assert.equal(page.timers[0].delay, 300000);
    page.timers[0].fn(); page.events.visibilitychange(); await settle();
    assert.equal(page.calls.filter(c => c.options.method === 'POST').length, 1);
    assert.ok(page.calls.slice(1).every(c => c.url.endsWith('/api/stats')));
});
test('background tabs wait for visibility, opt-out reads only, local previews do nothing', async () => {
    const hidden = browser({ hidden: true }); await settle(); assert.equal(hidden.calls.length, 0);
    hidden.document.visibilityState = 'visible'; hidden.events.visibilitychange(); await settle();
    assert.equal(hidden.calls[0].options.method, 'POST');
    const optout = browser({ optout: true }); await settle();
    assert.ok(optout.calls.every(c => c.url.endsWith('/api/stats')));
    const local = browser({ host: 'localhost' }); await settle(); assert.equal(local.calls.length, 0);
});

test('Do Not Track prevents recording', async () => { const page = browser({ dnt: true }); await settle(); assert.equal(page.calls.length, 1); assert.ok(page.calls.every(c => !c.options.method)); });
