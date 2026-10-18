// Service worker minimal de Crén'eau.
// - Rend l'app « installable » sur Android (bouton « Installer » de Chrome).
// - Ne met RIEN en cache : les pages et les données viennent toujours du réseau,
//   ce qui préserve la mise à jour automatique (version.json).
// - Hors connexion, une page simple remplace l'erreur du navigateur.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => {
  if(e.request.mode !== 'navigate') return;   // le reste passe directement par le réseau
  e.respondWith(fetch(e.request).catch(() => new Response(
    '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    + '<title>Crén\'eau</title><body style="font-family:system-ui;background:#05070c;color:#e8ecf3;display:grid;place-items:center;min-height:90vh;text-align:center;padding:16px">'
    + '<p><b>Pas de connexion</b><br>Crén\'eau a besoin d\'Internet pour les prévisions.<br>Réessayez dès que le réseau revient.</p></body>',
    {headers: {'Content-Type': 'text/html; charset=utf-8'}})));
});
