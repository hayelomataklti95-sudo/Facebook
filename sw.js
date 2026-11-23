const CACHE = 'lingua-pro-v1';

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(['./', './index.html'])));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(clients.claim());
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const u = new URL(req.url);
  const sameOrigin = u.origin === location.origin;
  const cdn = u.hostname === 'cdn.jsdelivr.net';
  if (!sameOrigin && !cdn) return; // model files are cached by WebLLM itself

  if (sameOrigin) {
    // network first, fall back to cache (so updates show up, offline still works)
    e.respondWith(
      fetch(req)
        .then(r => {
          if (r.ok) { const cp = r.clone(); caches.open(CACHE).then(c => c.put(req, cp)); }
          return r;
        })
        .catch(() => caches.match(req).then(h => h || caches.match('./index.html')))
    );
  } else {
    // CDN library: cache first
    e.respondWith(
      caches.match(req).then(hit => hit || fetch(req).then(r => {
        if (r.ok) { const cp = r.clone(); caches.open(CACHE).then(c => c.put(req, cp)); }
        return r;
      }))
    );
  }
});
