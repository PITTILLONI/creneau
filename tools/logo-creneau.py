"""Construit le kit du logo Crén'eau (piste A, « La fenêtre »)."""
import math, sys, os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONT, OUT = sys.argv[1], sys.argv[2]
BLUE, GREEN, INK = '#0057ff', '#0a7d45', '#0a0f1a'
BLUE_D, GREEN_D = '#5b9dff', '#6fdba0'

def ring(cx, cy, ro, ri, half, dot_r, title='Crén\'eau'):
    a = math.radians(half)
    p = lambda r, s: (cx + r*math.cos(a), cy - s*r*math.sin(a))
    (x1,y1),(x2,y2),(x3,y3),(x4,y4) = p(ro,1), p(ro,-1), p(ri,-1), p(ri,1)
    f = lambda v: f'{v:.2f}'.rstrip('0').rstrip('.')
    c = (f'M{f(x1)} {f(y1)}A{ro} {ro} 0 1 0 {f(x2)} {f(y2)}'
         f'L{f(x3)} {f(y3)}A{ri} {ri} 0 1 1 {f(x4)} {f(y4)}Z')
    d = (cx + (ro+ri)/2, cy, dot_r)
    return c, d

# Symbole : anneau 96/58 (épaisseur 38), ouverture de 70°, point = épaisseur de l'anneau, posé sur la piste.
C, D = ring(128, 128, 96, 58, 35, 19)
# Petites tailles : anneau plus épais, ouverture et point plus grands.
Cs, Ds = ring(126, 128, 104, 56, 38, 24)

def sym(c, d, ring_col, dot_col, bg=None, rx=0, size=256, title="Crén'eau", scale=1):
    bgs = f'<rect width="{size}" height="{size}" rx="{rx}" fill="{bg}"/>' if bg else ''
    # Dans une tuile, le symbole occupe ~62 % et se décale un peu à droite (le C pèse à gauche).
    g = f'<g transform="translate({128-128*scale+5*(scale<1):g} {128-128*scale:g}) scale({scale})">' if scale!=1 else '<g>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}"><title>{title}</title>{bgs}{g}'
            f'<path fill="{ring_col}" d="{c}"/><circle fill="{dot_col}" cx="{d[0]:g}" cy="{d[1]:g}" r="{d[2]}"/></g></svg>')

# Mot « Crén’eau » en tracés, Geist 700.
f = TTFont(FONT)
f = instantiateVariableFont(f, {'wght': 700})
gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f['hmtx']
upm = f['head'].unitsPerEm
cap = f['OS/2'].sCapHeight
TEXT = 'Crén’eau'
CAP_PX = 112                      # hauteur des capitales dans la version horizontale
k = CAP_PX / cap
TRACK = -0.015 * upm              # léger resserrement pour un mot-logo
def word(x0, base):
    pen = SVGPathPen(gs)
    x = 0
    for ch in TEXT:
        g = cmap[ord(ch)]
        tp = TransformPen(pen, (k, 0, 0, -k, x0 + x*k, base))
        gs[g].draw(tp)
        x += hmtx[g][0] + TRACK
    return pen.getCommands(), (x - TRACK) * k

GAP = 52
wx = 32 + 192 + GAP                # le mot démarre après l'anneau (bord droit du point = 224)
wpath, wwidth = word(wx, 128 + CAP_PX/2)
W = math.ceil(wx + wwidth + 24)

def horiz(ring_col, dot_col, word_col, bg=None):
    bgs = f'<rect width="{W}" height="256" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 256"><title>Crén\'eau</title>{bgs}'
            f'<path fill="{ring_col}" d="{C}"/><circle fill="{dot_col}" cx="{D[0]:g}" cy="{D[1]:g}" r="{D[2]}"/>'
            f'<path fill="{word_col}" d="{wpath}"/></svg>')

# Version empilée : symbole au-dessus, mot centré dessous.
SH = 460
spath, swidth = word(0, 0)
sx = (max(256, swidth + 48) - swidth) / 2
SW = math.ceil(max(256, swidth + 48))
spath, _ = word(sx, 256 + 24 + CAP_PX + 8)
dx = (SW - 256) / 2
def stacked(ring_col, dot_col, word_col):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SW} {SH}"><title>Crén\'eau</title>'
            f'<g transform="translate({dx:g},0)"><path fill="{ring_col}" d="{C}"/><circle fill="{dot_col}" cx="{D[0]:g}" cy="{D[1]:g}" r="{D[2]}"/></g>'
            f'<path fill="{word_col}" d="{spath}"/></svg>')

files = {
  'creneau-symbole.svg': sym(C, D, BLUE, GREEN),
  'creneau-symbole-noir.svg': sym(C, D, '#000', '#000'),
  'creneau-symbole-blanc.svg': sym(C, D, '#fff', '#fff'),
  'creneau-symbole-sombre.svg': sym(C, D, BLUE_D, GREEN_D),
  'creneau-symbole-petit.svg': sym(Cs, Ds, BLUE, GREEN),
  'creneau-icone-app.svg': sym(Cs, Ds, '#fff', GREEN_D, bg=BLUE, rx=56, scale=0.66),
  'creneau-icone-carre.svg': sym(Cs, Ds, '#fff', GREEN_D, bg=BLUE, scale=0.66),
  'creneau-horizontal.svg': horiz(BLUE, GREEN, INK),
  'creneau-horizontal-noir.svg': horiz('#000', '#000', '#000'),
  'creneau-horizontal-blanc.svg': horiz('#fff', '#fff', '#fff'),
  'creneau-horizontal-sombre.svg': horiz(BLUE_D, GREEN_D, '#f5f7fb'),
  'creneau-empile.svg': stacked(BLUE, GREEN, INK),
}
for n, s in files.items():
    open(os.path.join(OUT, n), 'w').write(s + '\n')
print('ok', W, SW, round(wwidth))
