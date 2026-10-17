import json, os, sys, time, urllib.request
D=os.path.join(os.path.dirname(__file__), "..", "tuto-sources") + "/"
K=open(os.path.expanduser('~/.config/krea/token')).read().strip()
REF="https://gen.krea.ai/images/180e3a77-bbea-4a02-9ca2-9cdb35272d7b.png"
STYLE=("Use the attached image only as STYLE reference (clean modern flat vector illustration, soft natural colors; rider: man in black full wetsuit, blue waist harness, white helmet; partner: woman in red short-sleeve wetsuit top; kite: white canopy, thick orange leading-edge tube, orange struts; twin-tip board yellow). Technically precise kitesurfing instruction illustration. ")
SIDE=("SIDE VIEW, camera level with the beach, perpendicular to the wind: the sea is on the LEFT edge of the image, the beach extends to the right, the wind blows from LEFT to RIGHT. ")
BACK=("View from slightly above and BEHIND the rider, who has his back to the viewer; the wind blows from behind the viewer into the scene; open sea all around, horizon high in the image. ")
END=" No flags, no text, no letters, no numbers, no arrows, no logos, no watermark."
JOBS={
 'etaler': STYLE+SIDE+"In the center, a DEFLATED kite is spread flat on the sand, upside down: its flat orange leading-edge tube lies along the LEFT side of the kite, facing the wind and the sea; the white canopy lies flat behind it to the right. A small inflation valve on the orange leading edge points straight UP to the sky. The rider kneels next to it smoothing the fabric. Four thin lines lead from the kite to the LEFT toward a bar near the water."+END,
 'gonfler': STYLE+SIDE+"In the center, the kite lies on the sand with its thick orange leading-edge tube on the LEFT side, facing the wind and the sea, the white canopy behind it to the right held down by two small piles of sand. The rider stands on the right of the kite, downwind, and pumps with a tall black hand pump; a hose goes from the pump to the valve on top of the orange leading edge, which is now round and inflated."+END,
 'securiser': STYLE+SIDE+"In the center, an inflated kite lies safely on the sand like a dome with its BACK (outer convex side, with the struts) facing the SKY; its thick orange leading-edge tube rests on the sand on the LEFT side, facing the wind and the sea; two piles of sand on the canopy hold it down. The partner kneels and puts sand on the canopy. The rider walks toward the kite from the left winding the lines onto the bar."+END,
 'porter': STYLE+SIDE+"The rider walks on the beach carrying a detached inflated kite with one hand, holding it LOW at waist height by the MIDDLE of its orange leading-edge tube. The orange leading edge is on the LEFT, facing the wind and the sea; the kite is tilted so that its BACK (outer convex side with the struts) faces DOWN toward the sand and the inside of the canopy faces up; the wingtips trail to the right, downwind, close to the sand. No lines attached."+END,
 'porter2': STYLE+SIDE+"The rider, empty-handed except for the kite, walks on the beach toward the right carrying a detached inflated kite with ONE hand held low at waist height, gripping the MIDDLE of the thick orange leading-edge tube. The kite is held almost horizontal like an upside-down umbrella: the orange leading edge is on the LEFT side facing the wind and the sea, the canopy's outer convex BACK faces DOWN toward the sand, the inside of the canopy faces the sky, and the two wingtips point to the right, downwind, close to the sand. No board, no lines attached."+END,
 'ws4b': STYLE+BACK+"The rider sits in the water, feet in the straps, board across in front of him, arms straight. His kite is diving from the top of the sky DOWN toward the LEFT: it is now at about 10 o'clock, low on the LEFT side of the sky, its nose pointing down-left. A soft dotted curved trail starts at the very top center of the sky (the zenith) and curves DOWN to the kite on the left, showing it came from above. Nothing on the right side of the sky."+END,
 'ws1': STYLE+BACK+"The rider floats on his back in the water, head out, holding the control bar at the center with one hand and reaching for the board with the other. His kite flies stable directly ABOVE him at the zenith (12 o'clock), its four lines going straight up."+END,
 'ws2': STYLE+BACK+"The rider sits in the water, feet in the footstraps of the twin-tip board, knees bent toward his chest, the board placed across in front of him, perpendicular to the wind, its edge just out of the water. Both hands on the control bar, ARMS STRAIGHT. The kite is stable directly ABOVE him at the zenith (12 o'clock)."+END,
 'ws3': STYLE+"Split image, two panels side by side, separated by a thin vertical gap, same rider in the water with feet in the board straps, side view, wind from the left. LEFT panel: the rider pulls the control bar tightly against his chest, ELBOWS BENT, body tense, being pulled over the board, splash. RIGHT panel: the rider keeps both ARMS FULLY STRAIGHT, the bar far away from his body, relaxed hands, the kite pulls him smoothly out of the water. Small red cross shape above the left panel, small green check mark shape above the right panel."+" No text, no letters, no numbers, no logos, no watermark.",
 'ws4': STYLE+BACK+"The rider sits in the water, feet in the straps, board across in front of him. His kite dives powerfully from the zenith down toward the LEFT side of the sky (10 o'clock position), leaving a soft dotted curved trail behind it showing its path from high in the center down to the left. Arms straight."+END,
 'ws5': STYLE+BACK+"The rider rises out of the water onto the twin-tip board, riding toward the LEFT. Front leg (left) straight, back leg slightly bent with weight on the back heel, arms straight, looking ahead to the left. The kite flies at about 10 o'clock on the left side of the sky, lines taut. Spray behind the board."+END,
 'ws6': STYLE+BACK+"The rider rides comfortably on the twin-tip board toward the LEFT, upright and balanced, arms relaxed and straight, the bar away from his body. The kite flies stable at about 11 o'clock, high on the left side of the sky. A clean wake behind the board."+END,
}
def call(url, data=None):
    req=urllib.request.Request(url, data=json.dumps(data).encode() if data else None, headers={'Authorization':'Bearer '+K,'Content-Type':'application/json'}, method='POST' if data else 'GET')
    return json.load(urllib.request.urlopen(req, timeout=60))
names = sys.argv[1:] or list(JOBS)
for n in names:
    if os.path.exists(D+'nb_'+n+'.png') and os.path.getsize(D+'nb_'+n+'.png')>0: continue
    for attempt in range(30):
        try:
            j=call('https://api.krea.ai/generate/image/google/nano-banana-pro', {"aspect_ratio":"16:9","resolution":"1K","image_urls":[REF],"prompt":JOBS[n]})['job_id']; break
        except Exception as e:
            time.sleep(6)
    else:
        print('submit fail',n); continue
    for _ in range(60):
        r=call('https://api.krea.ai/jobs/'+j)
        if r['status']=='completed':
            urllib.request.urlretrieve(r['result']['urls'][0], D+'nb_'+n+'.png'); print('ok',n, flush=True); break
        if r['status'] in ('failed','cancelled'):
            print('fail',n,r.get('error'), flush=True); break
        time.sleep(4)
