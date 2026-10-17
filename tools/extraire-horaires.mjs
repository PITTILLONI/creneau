// Extrait les horaires des portes Morny et les marées du PDF officiel
// "Port de Deauville-Trouville — Horaires de manœuvres" (Ports du Calvados / SHOM)
// et signale les incohérences du document.
//
// Usage :
//   pdftotext -layout horaires-2026.pdf horaires.txt
//   node tools/extraire-horaires.mjs horaires.txt > data.json
//
// Sortie : { "MM-JJ": { c:[coefMatin,coefSoir], bm:[matin,soir], pm:[matin,soir], w:[[ouv,ferm]x3] } }
// Les heures sont en heure légale de Paris ("HH:MM"), null quand le PDF n'indique rien.

import fs from 'node:fs';

const txt = fs.readFileSync(process.argv[2], 'utf8');
const MONTHS = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre'];
const time = s => /^\d{2}[hH:]\d{2}$/.test(s) ? s.replace(/[hH]/, ':') : null;
const coef = s => /^\d+$/.test(s) ? s : null;

const data = {};
let month = -1, morny = true;
for (const line of txt.split('\n')) {
  const head = line.match(/^\s*(\S+) \d{4}/);
  if (head && MONTHS.includes(head[1])) {
    const i = MONTHS.indexOf(head[1]);
    if (i === 0 && month === 11) morny = false; // 2e moitié du PDF : portes Marinas, ignorée
    month = i;
    continue;
  }
  if (!morny) continue;
  const row = line.match(/^\s*(\d{1,2}) (lun|mar|mer|jeu|ven|sam|dim)\s+(.*)$/);
  if (!row) continue;
  const key = String(month + 1).padStart(2, '0') + '-' + row[1].padStart(2, '0');
  const t = row[3].trim().split(/\s+/);
  if (t.length !== 12) console.error(`! ${key} : ${t.length} colonnes au lieu de 12`);
  const g = t.slice(6).map(time);
  data[key] = {
    c: [coef(t[0]), coef(t[1])],
    bm: [time(t[2]), time(t[3])],
    pm: [time(t[4]), time(t[5])],
    w: [[g[0], g[1]], [g[2], g[3]], [g[4], g[5]]],
  };
}

// Contrôles : chaque ouverture qui passe minuit doit être refermée le lendemain,
// chaque fermeture en début de journée doit avoir une ouverture la veille.
let open = null;
for (const [key, d] of Object.entries(data)) {
  for (const [o, f] of d.w) {
    if (o && !f) { if (open) console.error(`! ${open} : ouverture jamais refermée`); open = key; }
    if (!o && f) { if (!open) console.error(`! ${key} : fermeture à ${f} sans ouverture correspondante dans le PDF`); open = null; }
  }
}
console.error(`${Object.keys(data).length} jours extraits`);
process.stdout.write(JSON.stringify(data));
