# Carrousels kite : illustrations + annotations exactes superposées (vent, bord d'attaque, positions).
# Coordonnées en % de la largeur (x) et de la hauteur (y) de l'image.
import html, re
P='/Users/antoine/deauville-passerelle-ecluse/index.html'
H=56.25  # hauteur du viewBox pour une image 16:9 de largeur 100

def wind(x1,y1,x2,y2,label='vent'):
    return ('arrow',x1,y1,x2,y2,label)
def back(label='vent dans le dos'):
    return ('back',label)
def tag(text,tx,ty,px=None,py=None,kind=''):
    return ('tag',text,tx,ty,px,py,kind)

def overlay(items):
    svg=[]; tags=[]
    for it in items:
        if it[0]=='arrow':
            _,x1,y1,x2,y2,label=it
            # l'étiquette se place à la queue de la flèche, la flèche part juste après
            tx,ty=x1,y1
            if abs(x2-x1)<1: y1+=7; y2+=7
            elif abs(y2-y1)<1: x1+=9; x2+=9
            else: x1+=7; y1+=7; x2+=7; y2+=7
            y1*=H/100; y2*=H/100
            import math
            a=math.atan2(y2-y1,x2-x1); L=2.6
            p1=(x2-L*math.cos(a-.55),y2-L*math.sin(a-.55)); p2=(x2-L*math.cos(a+.55),y2-L*math.sin(a+.55))
            svg.append('<path class="an-wind-bg" d="M%.1f %.2fL%.1f %.2fM%.1f %.2fL%.1f %.2fL%.1f %.2f"/>'%(x1,y1,x2,y2,p1[0],p1[1],x2,y2,p2[0],p2[1]))
            svg.append('<path class="an-wind" d="M%.1f %.2fL%.1f %.2fM%.1f %.2fL%.1f %.2fL%.1f %.2f"/>'%(x1,y1,x2,y2,p1[0],p1[1],x2,y2,p2[0],p2[1]))
            tags.append('<span class="tag tag-wind" style="left:%.1f%%;top:%.1f%%">%s</span>'%(max(7,tx),max(6,ty),label))
        elif it[0]=='back':
            tags.append('<span class="tag tag-wind tag-back" style="left:3%%;top:5%%"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2.5"/><circle cx="12" cy="12" r="2.5" fill="currentColor"/></svg>%s</span>'%it[1])
        else:
            _,text,tx,ty,px,py,kind=it
            if px is not None:
                tx=min(78,max(22,tx)); ty=min(91,max(8,ty))
                svg.append('<path class="an-lead" d="M%.1f %.2fL%.1f %.2f"/><circle class="an-dot" cx="%.1f" cy="%.2f" r=".9"/>'%(tx,ty*H/100,px,py*H/100,px,py*H/100))
            tags.append('<span class="tag %s" style="left:%.1f%%;top:%.1f%%">%s</span>'%(kind,min(78,max(22,tx)),min(91,max(8,ty)),text))
    return '<svg class="ann" viewBox="0 0 100 %s" aria-hidden="true">%s</svg>%s'%(H,''.join(svg),''.join(tags))

LAUNCH=[
 ('decollage-01','Vérifier la zone',"Sous le vent, une zone dégagée d'au moins trois longueurs de lignes, sans personne ni obstacle. Jamais par vent de terre.",
   [wind(4,30,20,30), tag('zone libre sous le vent : 3 longueurs de lignes',58,80,55,50)]),
 ('decollage-02','Dérouler les lignes',"Pars de l'endroit où sera l'aile et déroule les lignes en marchant vers le vent : bien droites, sans nœud ni croisement, rouge à gauche.",
   [wind(92,8,92,30), tag('je marche vers le vent',74,40,52,30), tag('lignes sans nœud ni croisement',72,64,56,58), tag('aile dans son sac',24,66,34,82)]),
 ('decollage-03','Étaler l’aile',"Au bout des lignes, étale l'aile retournée : valve de gonflage vers le ciel, bord d'attaque face au vent.",
   [wind(6,10,24,10), tag('bord d’attaque face au vent',34,36,49,57,'tag-le'), tag('lignes vers la barre',24,90,12,74)]),
 ('decollage-04','Gonfler',"Gonfle le boudin principal puis les lattes, bord d'attaque toujours face au vent, et leste la toile avec du sable.",
   [wind(6,8,20,24), tag('bord d’attaque face au vent',16,92,24,66,'tag-le'), tag('pompe branchée sur la valve',72,92,64,72)]),
 ('decollage-05','Connecter les lignes',"Aile dos vers le ciel, bord d'attaque face au vent. Lignes avant au bord d'attaque, lignes arrière aux bouts d'aile, rouge à gauche.",
   [wind(36,10,54,10), tag('dos de l’aile vers le ciel',72,22,70,44), tag('bord d’attaque face au vent',58,92,52,72,'tag-le'), tag('barre au bord de l’eau',24,62,12,80)]),
 ('decollage-06','S’accrocher',"Ton partenaire tient l'aile pendant que tu t'accroches au harnais (chicken loop et leash). Ne tire pas sur les lignes. Teste ton largueur.",
   [wind(40,8,40,26), tag('chicken loop + leash au harnais',26,30,9,60), tag('lignes molles : ne tire pas',44,84,40,62), tag('partenaire',84,90,85,62)]),
 ('decollage-07','Sortir de la zone de puissance',"Lignes encore molles, marche jusqu'à ce que l'aile soit en bord de fenêtre, vers 9 h ou 3 h, perpendiculaire au vent.",
   [wind(40,8,40,26), tag('aile en bord de fenêtre (3 h)',64,36,77,44,'tag-good'), tag('je marche, lignes molles',30,92,20,80)]),
 ('decollage-08','Tendre doucement',"Tends doucement les lignes et reviens sur tes pas jusqu'à ce que le bas de l'aile arrête de faseyer : elle est prête à décoller.",
   [wind(30,8,30,26), tag('le bas de l’aile ne faseye plus',66,88,84,60,'tag-good'), tag('un pas en arrière',22,94,19,86)]),
 ('decollage-09','Le signal',"Pouce levé : ton partenaire lâche doucement l'aile, sans la pousser. Mains croisées au-dessus de la tête = « repose l'aile ».",
   [wind(52,8,52,26), tag('pouce levé = « lâche »',50,44,32,30), tag('il ouvre les mains',74,90,82,58)]),
 ('decollage-10','Monter à midi',"Accompagne une montée douce par le bord de fenêtre jusqu'à midi (12 h). Par vent fort, n'y reste pas : ramène l'aile vers 11 h ou 1 h.",
   [wind(12,10,12,28), tag('12 h : au-dessus de toi',76,14,56,12,'tag-good'), tag('montée par le bord',74,46,76,52)]),
]
LANDING=[
 ('atterrissage-1','Le signal',"Aile en bord de fenêtre et assez basse, tape sur ta tête : ton partenaire vient se placer près de l'aile.",
   [wind(40,8,40,26), tag('main sur la tête',36,34,21,46), tag('aile basse en bord de fenêtre',62,90,80,60,'tag-good')]),
 ('atterrissage-2','L’attraper',"Descends l'aile doucement vers lui, une main sur la barre, l'autre sur le largueur. Il l'attrape par le milieu du bord d'attaque, jamais par les lignes.",
   [wind(40,8,40,26), tag('il tient le bord d’attaque',66,88,83,55,'tag-le'), tag('main sur le largueur',22,90,15,64)]),
 ('atterrissage-3','Sécuriser',"Lâche la barre, rejoins l'aile, décroche chicken loop et leash. Aile dos vers le ciel, bord d'attaque face au vent, lestée de sable. Enroule les lignes vers l'aile.",
   [wind(30,8,48,8), tag('dos vers le ciel',74,22,62,42), tag('bord d’attaque face au vent',32,90,46,72,'tag-le'), tag('sable sur la toile',78,84,64,64)]),
 ('atterrissage-4','Porter son aile',"Tiens-la par le milieu du bord d'attaque, face au vent, le dos de l'aile vers le sable : le vent la plaque au lieu de la soulever. Garde-la basse.",
   [wind(58,8,76,8), tag('main au milieu du bord d’attaque',58,90,44,54,'tag-le'), tag('pointes sous le vent',78,74,86,58)]),
]
WATER=[
 ('waterstart-1','Flotter, aile à midi',"Sur le dos dans l'eau, aile stable au zénith (12 h). Une main au centre de la barre, l'autre ramène la planche vers toi.",
   [back(), tag('aile stable à 12 h',78,14,59,12,'tag-good'), tag('planche vers toi',76,88,80,80)]),
 ('waterstart-2','Chausser la planche',"Pieds dans les straps, genoux pliés vers la poitrine, planche en travers devant toi. Aile toujours à 12 h, sans bouger.",
   [back(), tag('aile toujours à 12 h',78,14,59,12,'tag-good'), tag('planche en travers, pieds dans les straps',26,78,38,84)]),
 ('waterstart-3','Ne t’agrippe pas à la barre',"<strong>Bras tendus, barre loin de toi, mains souples.</strong> Si tu tires la barre vers toi, l'aile prend toute sa puissance d'un coup et te fait passer par-dessus la planche. La traction vient de l'aile, pas de tes bras.",
   [tag('barre tirée, bras pliés',25,84,None,None,'tag-bad'), tag('bras tendus, barre loin',75,84,None,None,'tag-good')]),
 ('waterstart-4','Piquer l’aile',"Depuis 12 h, emmène l'aile un peu du côté opposé puis plonge-la franchement vers 10 h (ou 2 h) du côté où tu pars. C'est l'aile qui te sort de l'eau.",
   [back(), tag('plonge l’aile vers 10 h',26,80,22,62,'tag-good'), tag('depuis 12 h',58,10,48,6)]),
 ('waterstart-5','Se laisser lever',"Laisse la traction te mettre debout : jambe avant tendue, poids sur le talon arrière, regard devant. Se lever est le dernier geste, pas le premier.",
   [back(), tag('jambe avant tendue',34,76,53,82), tag('poids sur le talon arrière',78,80,61,88), tag('aile vers 10 h',34,40,16,40,'tag-good')]),
 ('waterstart-6','Stabiliser',"Remonte l'aile vers 11 h (ou 1 h) et garde-la stable. Tu ralentis : un sinus. Trop de puissance : éloigne la barre.",
   [back(), tag('aile stable vers 11 h',42,30,20,22,'tag-good'), tag('barre loin, bras détendus',78,70,64,58)]),
]

def slide(i,n,img,title,text,ann):
    return ('        <figure class="slide" aria-label="Étape %d sur %d">\n          <div class="ill-wrap"><img class="ill-img" src="tuto/%s.webp" alt="%s" loading="lazy" decoding="async">%s</div>\n          <figcaption><b>%d · %s.</b> %s</figcaption>\n        </figure>\n'
            % (i,n,img,html.escape(title),overlay(ann),i,title,text))
def slides(lst):
    return ''.join(slide(i+1,len(lst),*st) for i,st in enumerate(lst))

s=open(P).read()
for cid,lst in (('launch',LAUNCH),('landing',LANDING),('waterstart',WATER)):
    a=s.index('id="%s"'%cid); a=s.index('<div class="slides">',a)+len('<div class="slides">\n')
    b=s.index('        </div>\n        <div class="car-nav">',a)
    s=s[:a]+slides(lst)+s[b:]
CSS="""
  /* annotations superposées aux illustrations */
  .ill-wrap{position:relative;border-radius:14px;overflow:hidden;}
  .ill-wrap .ill-img{border-radius:0;}
  .ann{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;}
  .an-wind-bg{fill:none;stroke:#fff;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}
  .an-wind{fill:none;stroke:#0b5ed7;stroke-width:1.2;stroke-linecap:round;stroke-linejoin:round;}
  .an-lead{stroke:#0d1f26;stroke-width:.35;}
  .an-dot{fill:#0d1f26;stroke:#fff;stroke-width:.35;}
  .tag{position:absolute;transform:translate(-50%,-50%);background:rgba(255,255,255,.94);color:#0d1f26;
    font-size:.66rem;font-weight:700;line-height:1.15;padding:3px 8px;border-radius:10px;white-space:normal;
    width:max-content;max-width:44%;text-align:center;box-shadow:0 0 0 1px rgba(13,31,38,.12);pointer-events:none;}
  .tag-wind{background:#0b5ed7;color:#fff;box-shadow:none;}
  .tag-back{transform:none;display:flex;align-items:center;gap:4px;max-width:none;white-space:nowrap;}
  .tag-back svg{width:12px;height:12px;}
  .tag-le{background:#f07c1b;color:#fff;box-shadow:none;}
  .tag-good{background:#16784a;color:#fff;box-shadow:none;}
  .tag-bad{background:#c0281f;color:#fff;box-shadow:none;}
  @media (min-width:480px){ .tag{font-size:.78rem;padding:4px 9px;} }
"""
s=s.replace("  /* carrousel de décollage */", CSS+"\n  /* carrousel de décollage */",1)
open(P,'w').write(s)
print('ok', s.count('class="ill-wrap"'), s.count('class="ill dg"'))
