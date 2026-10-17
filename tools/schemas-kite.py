# Schémas techniques du tuto kite. Conventions :
#  - vue de dessus : mer et vent en BAS, l'aile en haut (sous le vent), le rider entre les deux, face à son aile
#    -> la gauche du rider = la gauche de l'image, côté rouge à gauche
#  - vue de derrière : rider de dos, vent dans le dos, fenêtre en cadran 9 h / 12 h / 3 h
W, H = 320, 200

def svg(inner, title):
    return ('<svg viewBox="0 0 %d %d" class="ill dg" role="img" aria-label="%s">' % (W, H, title)) + inner + '</svg>'

def text(x, y, t, cls='dg-t', anchor='start'):
    return '<text x="%s" y="%s" class="%s" text-anchor="%s">%s</text>' % (x, y, cls, anchor, t)

def arrow(x1, y1, x2, y2, cls='dg-arr'):
    import math
    a = math.atan2(y2-y1, x2-x1); L = 8
    p1 = (x2 - L*math.cos(a-0.5), y2 - L*math.sin(a-0.5)); p2 = (x2 - L*math.cos(a+0.5), y2 - L*math.sin(a+0.5))
    return '<path class="%s" d="M%.1f %.1fL%.1f %.1fM%.1f %.1fL%.1f %.1fL%.1f %.1f"/>' % (cls, x1, y1, x2, y2, p1[0], p1[1], x2, y2, p2[0], p2[1])

def top_bg():
    return ('<rect width="320" height="200" rx="14" class="dg-sand"/>'
            '<path d="M0 168h320v18a14 14 0 0 1-14 14H14A14 14 0 0 1 0 186z" class="dg-sea"/>'
            + text(10, 190, 'mer', 'dg-t dg-sea-t')
            + '<g class="dg-wind">' + arrow(24, 164, 24, 128, 'dg-warr') + '</g>' + text(34, 140, 'vent', 'dg-t dg-wind-t'))

def back_bg(power_label=True):
    # vue de derrière : fenêtre en demi-cadran, zone de puissance au centre
    return ('<rect width="320" height="200" rx="14" class="dg-sky"/>'
            '<rect x="0" y="168" width="320" height="32" class="dg-sand-flat"/>'
            '<path d="M40 168A120 120 0 0 1 280 168" class="dg-window"/>'
            '<path d="M95 168A65 120 0 0 1 225 168Z" class="dg-power"/>'
            + (text(160, 118, 'zone de puissance', 'dg-t dg-power-t', 'middle') if power_label else '')
            + text(40, 182, '9 h', 'dg-t dg-clock', 'middle') + text(280, 182, '3 h', 'dg-t dg-clock', 'middle') + text(160, 42, '12 h', 'dg-t dg-clock', 'middle')
            + '<g class="dg-wind">' + arrow(22, 62, 22, 26, 'dg-warr') + '</g>' + text(10, 76, 'vent dans', 'dg-t dg-wind-t') + text(10, 88, 'le dos', 'dg-t dg-wind-t'))

def rider_top(x, y):   # rider vu de dessus, face vers le haut (vers l'aile)
    return '<g class="dg-rider"><circle cx="%d" cy="%d" r="7"/><rect x="%d" y="%d" width="22" height="7" rx="3"/></g>' % (x, y, x-11, y+5)

def bar_top(x, y, w=34):  # barre vue de dessus, rouge à gauche
    return ('<rect x="%d" y="%d" width="%d" height="5" rx="2" class="dg-bar"/>' % (x-w/2, y-2, w)
            + '<rect x="%d" y="%d" width="8" height="5" rx="2" class="dg-red"/>' % (x-w/2, y-2)
            + '<rect x="%d" y="%d" width="8" height="5" rx="2" class="dg-green"/>' % (x+w/2-8, y-2))

def lines4(x0, y0, pts, slack=False):
    # pts : 4 points d'attache (gauche -> droite) ; départ de la barre ; la ligne de gauche en rouge
    out = ''
    offs = [-12, -4, 4, 12]
    for i, (px, py) in enumerate(pts):
        sx = x0 + offs[i]
        cls = 'dg-line dg-line-red' if i == 0 else 'dg-line'
        if slack:
            mx, my = (sx+px)/2 + (10 if i % 2 else -10), (y0+py)/2
            out += '<path class="%s" d="M%.1f %.1fQ%.1f %.1f %.1f %.1f"/>' % (cls, sx, y0, mx, my, px, py)
        else:
            out += '<path class="%s" d="M%.1f %.1fL%.1f %.1f"/>' % (cls, sx, y0, px, py)
    return out

def kite_top(cx, cy, inflated=True, sand=False, valve=False):
    # aile posée, vue de dessus : bord d'attaque (orange) vers le BAS = face au vent, toile derrière (sous le vent)
    le = 'M%d %dQ%d %d %d %d' % (cx-62, cy, cx, cy+22, cx+62, cy)
    can = 'M%d %dQ%d %d %d %dL%d %dQ%d %d %d %dZ' % (cx-62, cy, cx, cy+22, cx+62, cy, cx+52, cy-34, cx, cy-16, cx-52, cy-34)
    out = '<path d="%s" class="dg-canopy"/>' % can
    if inflated:
        for t in (-0.62, -0.25, 0.25, 0.62):
            x = cx + t*62; y = cy + 22*(1-t*t)*0.5*2*0.5 + (0 if abs(t) > .5 else 4)
            out += '<path class="dg-strut" d="M%.1f %.1fL%.1f %.1f"/>' % (x, y+2, x*0.98+cx*0.02, y-30+abs(t)*8)
    out += '<path d="%s" class="%s"/>' % (le, 'dg-le' if inflated else 'dg-le dg-le-flat')
    if sand:
        for sx, sy in ((cx-28, cy-14), (cx+26, cy-14)):
            out += '<path class="dg-pile" d="M%d %dq7 -9 14 0z"/>' % (sx-7, sy)
    if valve:
        out += '<circle cx="%d" cy="%d" r="4" class="dg-valve"/>' % (cx-20, cy+9)
    return out

def inset(x, y, w, h, inner, label='vu de côté'):
    return ('<g transform="translate(%d %d)"><rect width="%d" height="%d" rx="8" class="dg-inset"/>' % (x, y, w, h)
            + text(6, 11, label, 'dg-t dg-small') + inner + '</g>')

# encarts « vu de côté » : vent de la gauche
def side_wind():
    return '<g class="dg-wind">' + arrow(8, 30, 26, 30, 'dg-warr dg-warr-s') + '</g>'
def side_flat():     # aile dégonflée à plat, bord d'attaque côté vent, valve vers le ciel
    return (side_wind() + '<path class="dg-ground" d="M6 52h108"/>'
            '<rect x="30" y="46" width="22" height="6" rx="3" class="dg-le-fill"/>'
            '<path class="dg-canopy-s" d="M52 50h52"/>' + arrow(41, 46, 41, 30, 'dg-arr dg-arr-s') + text(46, 34, 'valve', 'dg-t dg-small'))
def side_inflated():
    return (side_wind() + '<path class="dg-ground" d="M6 52h108"/>'
            '<circle cx="40" cy="44" r="8" class="dg-le-fill"/><path class="dg-canopy-s" d="M48 50h56"/>'
            '<path class="dg-pile" d="M78 50q6-8 12 0z"/>')
def side_dome():     # dos vers le ciel, bord d'attaque face au vent sur le sable
    return (side_wind() + '<path class="dg-ground" d="M6 52h108"/>'
            '<circle cx="36" cy="46" r="6" class="dg-le-fill"/><path class="dg-canopy-s" d="M40 42Q72 14 104 50"/>'
            + text(70, 22, 'dos', 'dg-t dg-small', 'middle'))

D = {}
# 1. zone
D['d1'] = svg(top_bg() + '<rect x="70" y="18" width="180" height="120" rx="10" class="dg-zone"/>'
    + text(160, 70, 'zone libre', 'dg-t dg-big', 'middle') + text(160, 88, '3 longueurs de lignes', 'dg-t', 'middle')
    + text(160, 102, 'sous le vent', 'dg-t', 'middle')
    + rider_top(160, 150) + arrow(160, 140, 160, 124, 'dg-arr'), 'Zone libre sous le vent du rider')
# 2. dérouler les lignes en marchant vers le vent
D['d2'] = svg(top_bg() + '<rect x="140" y="16" width="40" height="18" rx="6" class="dg-bag"/>' + text(186, 29, 'aile (sac)', 'dg-t')
    + lines4(160, 140, [(154, 34), (158, 34), (162, 34), (166, 34)])
    + bar_top(160, 140) + rider_top(160, 152)
    + arrow(200, 70, 200, 130, 'dg-arr') + text(206, 96, 'marche', 'dg-t') + text(206, 108, 'vers le vent', 'dg-t')
    + text(120, 70, 'sans nœud', 'dg-t', 'end') + text(120, 82, 'ni croisement', 'dg-t', 'end')
    + text(146, 126, 'rouge', 'dg-t dg-red-t', 'end'), 'Dérouler les lignes en marchant vers le vent')
# 3. étaler l'aile retournée
D['d3'] = svg(top_bg() + kite_top(150, 60, inflated=False, valve=True)
    + lines4(150, 150, [(92, 60), (120, 74), (180, 74), (208, 60)]) + bar_top(150, 150) + rider_top(150, 162)
    + text(150, 98, "bord d'attaque face au vent", 'dg-t dg-le-t', 'middle')
    + text(122, 54, 'valve vers le ciel', 'dg-t', 'end')
    + inset(196, 112, 120, 58, side_flat()), "Aile étalée, bord d'attaque face au vent, valve vers le ciel")
# 4. gonfler
D['d4'] = svg(top_bg() + kite_top(150, 60, inflated=True, sand=True, valve=True)
    + '<rect x="90" y="110" width="8" height="30" rx="3" class="dg-pump"/><path class="dg-hose" d="M94 110C94 90 120 92 130 72"/>'
    + text(100, 152, 'pompe', 'dg-t', 'middle')
    + text(150, 98, "bord d'attaque face au vent", 'dg-t dg-le-t', 'middle')
    + text(150, 18, 'sable sur la toile', 'dg-t', 'middle')
    + inset(196, 112, 120, 58, side_inflated()), "Gonfler l'aile, bord d'attaque face au vent")
# 5. connecter les lignes
D['d5'] = svg(top_bg() + kite_top(150, 56, inflated=True)
    + lines4(150, 150, [(98, 24), (90, 58), (210, 58), (202, 24)]) + bar_top(150, 150) + rider_top(150, 162)
    + text(76, 60, 'avant', 'dg-t', 'end') + text(84, 24, 'arrière', 'dg-t', 'end')
    + text(224, 60, 'avant', 'dg-t') + text(216, 24, 'arrière', 'dg-t')
    + text(120, 112, 'rouge = gauche', 'dg-t dg-red-t', 'end')
    + inset(196, 112, 120, 58, side_dome()), "Connecter les lignes, aile dos vers le ciel")
# 6. s'accrocher (vue de derrière, lignes molles)
D['d6'] = svg(back_bg(False)
    + '<g class="dg-kite-up"><path d="M160 100c10 2 18 14 18 34-6-8-12-12-18-12z"/><path class="dg-le-s" d="M160 100c10 2 18 14 18 34"/></g>'
    + '<circle cx="186" cy="150" r="6" class="dg-partner"/><path class="dg-partner-b" d="M186 156v12"/>' + text(194, 160, 'partenaire', 'dg-t')
    + '<path class="dg-line dg-slack" d="M152 188Q150 160 162 140"/><path class="dg-line dg-slack" d="M168 188Q172 162 166 140"/>'
    + '<circle cx="160" cy="176" r="8" class="dg-me"/>'
    + text(160, 196, 'aile sous le vent, lignes molles : ne tire pas', 'dg-t', 'middle')
    + text(300, 60, 'je m’accroche :', 'dg-t', 'end') + text(300, 72, 'chicken loop', 'dg-t', 'end') + text(300, 84, '+ leash', 'dg-t', 'end'),
    "S'accrocher pendant que le partenaire tient l'aile, lignes molles")
# 7. sortir de la zone de puissance
D['d7'] = svg(back_bg()
    + '<g class="dg-kite-up"><path d="M268 126c10 2 18 14 18 34-6-8-12-12-18-12z"/><path class="dg-le-s" d="M268 126c10 2 18 14 18 34"/></g>'
    + '<circle cx="292" cy="160" r="5" class="dg-partner"/>'
    + '<path class="dg-path" d="M210 182C190 184 172 184 160 180"/>' + arrow(176, 183, 162, 180, 'dg-arr')
    + '<circle cx="160" cy="176" r="8" class="dg-me"/>'
    + '<path class="dg-line dg-slack" d="M166 172Q220 150 268 150"/>'
    + text(300, 92, 'aile en bord', 'dg-t dg-good-t', 'end') + text(300, 104, 'de fenêtre (3 h)', 'dg-t dg-good-t', 'end')
    + text(160, 196, 'je marche, lignes molles, jusqu’à 9 h ou 3 h', 'dg-t', 'middle'),
    "Marcher jusqu'à ce que l'aile soit en bord de fenêtre")
# 8. tendre doucement
D['d8'] = svg(back_bg()
    + '<g class="dg-kite-up"><path d="M268 126c10 2 18 14 18 34-6-8-12-12-18-12z" class="dg-filled"/><path class="dg-le-s" d="M268 126c10 2 18 14 18 34"/></g>'
    + '<circle cx="292" cy="160" r="5" class="dg-partner"/>'
    + '<circle cx="160" cy="176" r="8" class="dg-me"/>'
    + '<path class="dg-line" d="M166 172L268 146"/>' + arrow(150, 186, 132, 186, 'dg-arr') + text(128, 190, '1 pas', 'dg-t', 'end')
    + text(304, 78, 'le bas de l’aile', 'dg-t dg-good-t', 'end') + text(304, 90, 'ne faseye plus :', 'dg-t dg-good-t', 'end') + text(304, 102, 'elle est prête', 'dg-t dg-good-t', 'end'),
    "Tendre doucement les lignes jusqu'à ce que l'aile ne faseye plus")
# 10. monter à midi
D['d10'] = svg(back_bg()
    + '<path class="dg-path" d="M276 140A116 116 0 0 0 168 52"/>' + arrow(182, 54, 168, 52, 'dg-arr')
    + '<g class="dg-kite-up"><path d="M146 50c4-10 24-10 28 0-6-3-22-3-28 0z" class="dg-filled"/><path class="dg-le-s" d="M146 50c4-10 24-10 28 0"/></g>'
    + '<circle cx="160" cy="176" r="8" class="dg-me"/><path class="dg-line" d="M160 168L160 54"/>'
    + text(250, 70, 'montée douce', 'dg-t dg-good-t', 'end') + text(250, 82, 'par le bord', 'dg-t dg-good-t', 'end')
    + text(160, 196, 'vent fort : ne reste pas à 12 h, va vers 11 h ou 1 h', 'dg-t', 'middle'),
    "Monter l'aile par le bord de fenêtre jusqu'à midi")
# atterrissage 2 : le partenaire attrape l'aile
D['l2'] = svg(back_bg()
    + '<g class="dg-kite-up"><path d="M262 136c10 2 16 12 16 28-6-6-10-10-16-10z" class="dg-filled"/><path class="dg-le-s" d="M262 136c10 2 16 12 16 28"/></g>'
    + '<circle cx="284" cy="156" r="5" class="dg-partner"/>' + text(300, 128, 'il attrape le', 'dg-t', 'end') + text(300, 140, "bord d'attaque", 'dg-t', 'end')
    + '<circle cx="160" cy="176" r="8" class="dg-me"/><path class="dg-line" d="M166 172L262 150"/>'
    + text(160, 196, 'une main sur la barre, l’autre sur le largueur', 'dg-t', 'middle'),
    "Le partenaire attrape l'aile par le bord d'attaque en bord de fenêtre")
# atterrissage 3 : sécuriser
D['l3'] = svg(top_bg() + kite_top(150, 60, inflated=True, sand=True)
    + text(150, 98, "bord d'attaque face au vent", 'dg-t dg-le-t', 'middle')
    + text(150, 18, 'sable sur la toile', 'dg-t', 'middle')
    + lines4(150, 150, [(98, 26), (90, 60), (210, 60), (202, 26)], slack=True) + bar_top(150, 150)
    + text(306, 40, 'lignes enroulées', 'dg-t', 'end') + text(306, 52, 'vers l’aile', 'dg-t', 'end')
    + inset(196, 112, 120, 58, side_dome()), "Aile sécurisée au sol, bord d'attaque face au vent, lestée")
# atterrissage 4 : porter son aile (vu de côté)
D['l4'] = svg('<rect width="320" height="200" rx="14" class="dg-sky"/><rect x="0" y="160" width="320" height="40" class="dg-sand-flat"/>'
    + '<g class="dg-wind">' + arrow(20, 60, 64, 60, 'dg-warr') + '</g>' + text(20, 50, 'vent', 'dg-t dg-wind-t')
    + '<g class="dg-me-side"><circle cx="178" cy="78" r="9"/><path d="M178 87v40M178 127l-10 32M178 127l10 32M178 96l-26 18"/></g>'
    + '<circle cx="146" cy="116" r="9" class="dg-le-fill"/>'
    + '<path class="dg-canopy-side" d="M150 124Q196 150 252 140"/>'
    + text(120, 100, "main au milieu du", 'dg-t', 'end') + text(120, 112, "bord d'attaque", 'dg-t', 'end')
    + text(226, 168, 'dos de l’aile vers le sable', 'dg-t', 'middle')
    + text(140, 146, 'face au vent', 'dg-t dg-le-t', 'end'),
    "Porter son aile : tenue par le bord d'attaque, face au vent, dos vers le sable")

# ---------- water start : vue de derrière (vent dans le dos), le rider part vers la GAUCHE ----------
def sea_back():
    return ('<rect width="320" height="200" rx="14" class="dg-sky"/>'
            '<path d="M0 150h320v36a14 14 0 0 1-14 14H14A14 14 0 0 1 0 186z" class="dg-sea"/>'
            '<path d="M40 150A120 120 0 0 1 280 150" class="dg-window"/>'
            + text(40, 164, '9 h', 'dg-t dg-clock', 'middle') + text(280, 164, '3 h', 'dg-t dg-clock', 'middle') + text(160, 24, '12 h', 'dg-t dg-clock', 'middle')
            + '<g class="dg-wind">' + arrow(22, 62, 22, 26, 'dg-warr') + '</g>' + text(10, 76, 'vent dans', 'dg-t dg-wind-t') + text(10, 88, 'le dos', 'dg-t dg-wind-t'))
def kite_at(x, y, rot=0, cls='dg-filled'):
    return ('<g class="dg-kite-up" transform="translate(%d %d) rotate(%d)"><path d="M-16 4c4-12 28-12 32 0-8-4-24-4-32 0z" class="%s"/>'
            '<path class="dg-le-s" d="M-16 4c4-12 28-12 32 0"/></g>' % (x, y, rot, cls))
def head_water(x, y):
    return '<circle cx="%d" cy="%d" r="8" class="dg-me"/>' % (x, y)

D['w1'] = svg(sea_back() + kite_at(160, 34) + '<path class="dg-line" d="M160 154L160 38"/>' + head_water(160, 160)
    + '<rect x="186" y="156" width="54" height="8" rx="4" class="dg-board"/>'
    + text(176, 80, 'aile stable à 12 h', 'dg-t dg-good-t') + text(250, 186, 'la planche', 'dg-t', 'middle') + text(250, 196, 'ramenée vers toi', 'dg-t', 'middle'),
    "Flotter sur le dos, aile stable à midi")
D['w2'] = svg(sea_back() + kite_at(160, 34) + '<path class="dg-line" d="M160 148L160 38"/>' + head_water(160, 152)
    + '<rect x="118" y="168" width="84" height="9" rx="4" class="dg-board"/>'
    + '<path class="dg-legs" d="M150 160l-8 9M170 160l8 9"/>'
    + text(160, 196, 'planche en travers, perpendiculaire au vent', 'dg-t', 'middle')
    + text(176, 80, 'aile toujours à 12 h', 'dg-t dg-good-t') + text(206, 112, 'pieds dans', 'dg-t') + text(206, 124, 'les straps,', 'dg-t') + text(206, 136, 'genoux pliés', 'dg-t'),
    "Pieds dans les straps, planche en travers")
# barre : comparaison vue de côté, vent de la gauche, aile à droite
def side_rider(x, good):
    if good:
        body = '<path d="M%d 120l-10 26M%d 120l26-22"/>' % (x, x)   # bras tendus vers l'aile
        bar = (x+28, 96)
    else:
        body = '<path d="M%d 120l-10 26M%d 112c10-2 12-8 8-14"/>' % (x, x)  # bras pliés, barre contre la poitrine
        bar = (x+8, 100)
    return ('<g class="dg-me-side"><circle cx="%d" cy="104" r="8"/><path d="M%d 112v14"/>%s</g>' % (x, x, body)
            + '<rect x="%d" y="%d" width="5" height="22" rx="2" class="%s"/>' % (bar[0], bar[1]-11, 'dg-bar-good' if good else 'dg-bar-bad')
            + '<path class="dg-line" d="M%d %dL%d 30"/>' % (bar[0]+3, bar[1], x+66))
D['w3'] = svg('<rect width="320" height="200" rx="14" class="dg-sky"/><path d="M0 146h320v40a14 14 0 0 1-14 14H14A14 14 0 0 1 0 186z" class="dg-sea"/>'
    + '<g class="dg-wind">' + arrow(14, 30, 50, 30, 'dg-warr') + '</g>' + text(14, 22, 'vent', 'dg-t dg-wind-t')
    + '<path d="M160 40v120" class="dg-sep"/>'
    + side_rider(70, False) + text(80, 72, '✗', 'dg-bad-big', 'middle') + text(80, 176, 'barre tirée, bras pliés', 'dg-t dg-bad-t', 'middle')
    + text(82, 190, 'trop de puissance d’un coup', 'dg-t', 'middle')
    + side_rider(210, True) + text(240, 72, '✓', 'dg-good-big', 'middle') + text(240, 176, 'bras tendus, barre loin', 'dg-t dg-good-t', 'middle')
    + text(240, 190, 'c’est l’aile qui tire', 'dg-t', 'middle'),
    "Ne pas tirer la barre : bras tendus, barre loin")
D['w4'] = svg(sea_back() + kite_at(160, 34, 0, 'dg-ghost') + kite_at(176, 36, 10, 'dg-ghost')
    + '<path class="dg-path" d="M180 40C150 30 96 50 72 96"/>' + arrow(80, 82, 72, 96, 'dg-arr')
    + kite_at(66, 104, -60)
    + '<path class="dg-line" d="M160 148L74 106"/>' + head_water(160, 152) + '<rect x="118" y="168" width="84" height="9" rx="4" class="dg-board"/>'
    + text(200, 50, '1. un peu à droite', 'dg-t') + text(200, 62, '2. puis plonge-la', 'dg-t') + text(200, 74, 'franchement vers 10 h', 'dg-t')
    + arrow(120, 186, 80, 186, 'dg-arr') + text(130, 190, 'je pars à gauche', 'dg-t'),
    "Piquer l'aile vers 10 heures du côté où l'on part")
D['w5'] = svg(sea_back() + kite_at(86, 70, -40) + '<path class="dg-line" d="M150 112L94 76"/>'
    + '<g class="dg-me-side"><circle cx="156" cy="96" r="8"/><path d="M156 104v22M156 126l-14 20M156 126l12 12 2 12M154 110l-6 2"/></g>'
    + '<rect x="128" y="152" width="64" height="8" rx="3" class="dg-board" transform="rotate(-8 160 156)"/>'
    + arrow(110, 180, 70, 180, 'dg-arr')
    + text(204, 104, 'jambe avant tendue', 'dg-t') + text(204, 118, 'poids sur le', 'dg-t') + text(204, 130, 'talon arrière', 'dg-t') + text(204, 146, 'regard devant', 'dg-t'),
    "Se laisser lever, jambe avant tendue, poids sur le talon arrière")
D['w6'] = svg(sea_back() + kite_at(104, 46, -25) + '<path class="dg-line" d="M150 112L110 52"/>'
    + '<path class="dg-path" d="M74 70c8-14 18-14 26 0s18 14 26 0"/>'
    + '<g class="dg-me-side"><circle cx="156" cy="96" r="8"/><path d="M156 104v22M156 126l-14 20M156 126l12 12 2 12M154 110l-6 2"/></g>'
    + '<rect x="128" y="152" width="64" height="8" rx="3" class="dg-board" transform="rotate(-8 160 156)"/>'
    + text(204, 70, 'aile stable vers 11 h', 'dg-t dg-good-t') + text(204, 92, 'ça ralentit : un sinus', 'dg-t') + text(204, 112, 'trop de puissance :', 'dg-t') + text(204, 124, 'éloigne la barre', 'dg-t'),
    "Stabiliser l'aile vers 11 heures")

CSS = """
  /* schémas techniques */
  .dg text{font-family:inherit;}
  .dg-t{fill:var(--ink);font-size:10.5px;font-weight:600;}
  .dg-small{font-size:9px;fill:var(--ink-2);}
  .dg-big{font-size:16px;font-weight:800;fill:var(--good);}
  .dg-sand{fill:#efe2c6;} .dg-sand-flat{fill:#efe2c6;} .dg-sky{fill:#e6eef3;}
  .dg-sea{fill:#9fc6cf;} .dg-sea-t{fill:#25535d;font-weight:700;}
  .dg-warr{fill:none;stroke:#0b5ed7;stroke-width:4;stroke-linecap:round;stroke-linejoin:round;}
  .dg-warr-s{stroke-width:2.5;}
  .dg-wind-t{fill:#0b5ed7;font-weight:800;}
  .dg-arr{fill:none;stroke:#1d2530;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}
  .dg-arr-s{stroke-width:1.6;}
  .dg-rider circle{fill:#1d2530;} .dg-rider rect{fill:#2f6fdc;}
  .dg-me{fill:#1d2530;} .dg-partner{fill:#d93a2b;} .dg-partner-b{stroke:#d93a2b;stroke-width:3;}
  .dg-me-side circle{fill:#1d2530;} .dg-me-side path{fill:none;stroke:#1d2530;stroke-width:4;stroke-linecap:round;stroke-linejoin:round;}
  .dg-bar{fill:#1d2530;} .dg-red{fill:#e0322a;} .dg-green{fill:#1f9d55;}
  .dg-red-t{fill:#e0322a;font-weight:800;}
  .dg-line{fill:none;stroke:#4a5566;stroke-width:1.3;}
  .dg-line-red{stroke:#e0322a;stroke-width:1.6;}
  .dg-slack{stroke-dasharray:3 3;}
  .dg-canopy{fill:#ffffff;stroke:#9aa4b2;stroke-width:1.2;}
  .dg-le{fill:none;stroke:#f07c1b;stroke-width:9;stroke-linecap:round;}
  .dg-le-flat{stroke-width:5;stroke-dasharray:2 0;opacity:.8;}
  .dg-le-t{fill:#c25e0c;font-weight:800;}
  .dg-strut{stroke:#f07c1b;stroke-width:3;stroke-linecap:round;}
  .dg-valve{fill:#1d2530;stroke:#fff;stroke-width:1.5;}
  .dg-pile{fill:#b9925a;}
  .dg-bag{fill:#f07c1b;opacity:.85;}
  .dg-pump{fill:#1d2530;} .dg-hose{fill:none;stroke:#1d2530;stroke-width:1.8;}
  .dg-zone{fill:rgba(31,157,85,.16);stroke:#1f9d55;stroke-width:2;stroke-dasharray:7 5;}
  .dg-inset{fill:#fff;stroke:#c9d1db;stroke-width:1;}
  .dg-ground{stroke:#b9925a;stroke-width:2;}
  .dg-le-fill{fill:#f07c1b;}
  .dg-canopy-s{fill:none;stroke:#9aa4b2;stroke-width:2.5;stroke-linecap:round;}
  .dg-canopy-side{fill:none;stroke:#9aa4b2;stroke-width:4;stroke-linecap:round;}
  .dg-window{fill:rgba(31,157,85,.10);stroke:#1f9d55;stroke-width:1.5;stroke-dasharray:5 5;}
  .dg-power{fill:rgba(224,50,42,.16);}
  .dg-power-t{fill:#c0281f;font-weight:800;}
  .dg-clock{fill:#5b6575;font-weight:800;}
  .dg-kite-up path{fill:#fff;stroke:#9aa4b2;stroke-width:1;}
  .dg-kite-up .dg-filled{fill:#fff;}
  .dg-kite-up .dg-ghost{fill:#fff;opacity:.45;}
  .dg-le-s{fill:none !important;stroke:#f07c1b !important;stroke-width:5 !important;stroke-linecap:round;}
  .dg-path{fill:none;stroke:#1d2530;stroke-width:1.8;stroke-dasharray:4 4;}
  .dg-good-t{fill:#16784a;font-weight:800;}
  .dg-bad-t{fill:#c0281f;font-weight:800;}
  .dg-good-big{fill:#1f9d55;font-size:28px;font-weight:800;}
  .dg-bad-big{fill:#e0322a;font-size:28px;font-weight:800;}
  .dg-bar-good{fill:#1f9d55;} .dg-bar-bad{fill:#e0322a;}
  .dg-sep{stroke:#c9d1db;stroke-width:1.5;}
  .dg-board{fill:#f2b84b;}
  .dg-legs{fill:none;stroke:#1d2530;stroke-width:4;stroke-linecap:round;}
  .slide .dg{border-radius:14px;}
"""
