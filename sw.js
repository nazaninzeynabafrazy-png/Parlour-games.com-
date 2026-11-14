// Offline cache for The Parlour. Bump VERSION when you upload a new build.
const VERSION = 'parlour-v76';
const FILES = ['./', 'index.html', 'three.min.js', 'manifest.webmanifest',
  'fonts/Inter-Regular.woff2', 'fonts/Inter-SemiBold.woff2', 'fonts/Fraunces-600.woff2',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(VERSION).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const u = new URL(e.request.url);
  const isPage = e.request.mode === 'navigate' || /(\/|index\.html)$/.test(u.pathname);
  if (isPage) {
    // Pages: ask the network first so players always get the newest game; fall back to the saved copy when offline.
    e.respondWith(fetch(e.request, {cache: 'no-cache'}).then(res => {
      const copy = res.clone(); caches.open(VERSION).then(c => c.put('index.html', copy)); return res;
    }).catch(() => caches.match('index.html').then(h => h || caches.match('./'))));
    return;
  }
  e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(hit => hit || fetch(e.request)));
});
