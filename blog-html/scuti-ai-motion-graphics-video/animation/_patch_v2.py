# one-off patch: applies critic round-1 fixes (v1 -> v2) to scuti-intro.html
from pathlib import Path
f = Path(__file__).with_name("scuti-intro.html")
c = f.read_text(encoding="utf-8")
start = c.index("const services = [")
end = c.index("// place red dots")
NEW = r"""const services = [
  {ic:'AI', t:'Gen AI Consulting',    d:'Solve problems with Gen AI', x:110,  y:220},
  {ic:'OCR',t:'Generative AI OCR',    d:'Read any document format',   x:1310, y:220},
  {ic:'RAG',t:'Secure GAI (RAG)',     d:'Your knowledge, secured',    x:110,  y:540},
  {ic:'D',  t:'Dify Support',         d:'Adopt AI fast',              x:1310, y:540},
  {ic:'VN', t:'Software Outsourcing', d:'Vietnamese engineer teams',  x:710,  y:780},
];
const CW = 500, CH = 200;
const cardsWrap = document.getElementById('cards'), links = document.getElementById('links');
const cards = services.map(s => { const c=document.createElement('div'); c.className='card abs';
  c.style.left=s.x+'px'; c.style.top=s.y+'px';
  c.innerHTML=`<div class="ic">${s.ic}</div><h3>${s.t}</h3><p>${s.d}</p>`; cardsWrap.appendChild(c);
  const l=document.createElementNS('http://www.w3.org/2000/svg','line');
  l.setAttribute('x1',960); l.setAttribute('y1',540); l.setAttribute('x2',s.x+CW/2); l.setAttribute('y2',s.y+CH/2);
  links.appendChild(l); return c; });
const linkEls = [...links.querySelectorAll('line')];
const toCenterX = (i)=>960-CW/2-services[i].x, toCenterY = (i)=>540-CH/2-services[i].y;

// prepare line drawing
const netLines = [...document.querySelectorAll('#netLines line')];
netLines.forEach(l => { const L = Math.hypot(l.x2.baseVal.value-l.x1.baseVal.value, l.y2.baseVal.value-l.y1.baseVal.value);
  l.style.strokeDasharray = L; l.style.strokeDashoffset = L; l.dataset.len = L; });
const nodes = [...document.querySelectorAll('#netNodes circle')];
const trail = document.getElementById('dragonTrail'), scales = document.getElementById('dragonScales');
const TL = trail.getTotalLength(); trail.style.strokeDasharray = TL; trail.style.strokeDashoffset = TL;
scales.style.opacity = 0;

// ---------- master timeline ----------
gsap.set(['#kicker','#h2','#underline','#s3title','#stats','#src','#lockup','#tagline','#url'], {opacity:0});
gsap.set('#h1 .w', {yPercent:110});
gsap.set(nodes, {scale:0, transformOrigin:'50% 50%'});
gsap.set('#net', {scale:.8, rotation:-8, transformOrigin:'50% 50%'});
gsap.set(cards, {opacity:0, scale:.3});
gsap.set('.card > *', {opacity:0});
gsap.set(linkEls, {opacity:0});
gsap.set('#dragonHead', {opacity:0});
gsap.set('#logoText .ch', {yPercent:115});
gsap.set(['#dot1','#dot2'], {opacity:0});

const tl = gsap.timeline({paused:true});
const D = 18.0;
const S2 = 4.15, S3 = 6.05, S4 = 9.75, S5 = 12.55;   // shot starts (v2 retime after critic round 1)

// ambient drift for the whole duration (no frozen frames)
tl.to('#grid', {x:80, y:80, duration:D, ease:'none'}, 0);
parts.forEach((p,i)=> tl.to(p, {y:'-='+(60+ (i%7)*25), x:'+='+((i%5)-2)*30, opacity:.15+(i%4)*.15, duration:D, ease:'sine.inOut'}, 0));

// SHOT 1 (0 - 3.9): network builds, headline
tl.to(nodes[0], {scale:1, duration:.5, ease:'back.out(3)'}, 0.15)
  .to(netLines, {strokeDashoffset:0, duration:.7, ease:'power2.out', stagger:.07}, 0.45)
  .to(nodes.slice(1), {scale:1, duration:.45, ease:'back.out(3)', stagger:.12}, 0.6)
  .to('#net', {scale:1, rotation:0, duration:1.6, ease:'power3.out'}, 0.2)
  .fromTo('#kicker', {opacity:0, letterSpacing:'40px'}, {opacity:1, letterSpacing:'14px', duration:1.2, ease:'power3.out'}, 0.9)
  .to('#net', {x:-480, duration:0.9, ease:'expo.inOut'}, 1.3)
  .to('#h1 .w', {yPercent:0, duration:.7, ease:'power4.out', stagger:.09}, 1.95)
// exit: headline leaves fast, network flies at the camera (foreground = transition)
  .to(['#h1','#kicker'], {y:-80, opacity:0, duration:.35, ease:'power3.in'}, 3.4)
  .to('#net', {x:0, scale:14, rotation:25, opacity:0, duration:.75, ease:'power4.in'}, 3.45);

// SHOT 2 (S2 - S3): text arrives AFTER the fly-through lines have cleared
tl.set('#h2', {opacity:1}, S2)
  .from('#h2 .w', {scale:2.4, opacity:0, filter:'blur(18px)', duration:.55, ease:'expo.out', stagger:.11}, S2)
  .fromTo('#h2', {scale:1}, {scale:1.06, duration:1.9, ease:'none', immediateRender:false}, S2)
  .fromTo('#underline', {opacity:1, scaleX:0}, {scaleX:1, duration:.55, ease:'expo.out', immediateRender:false}, S2+.6)
  .fromTo('#net', {x:0, scale:.15, rotation:-40, opacity:0}, {scale:.35, rotation:0, opacity:.35, y:-300, duration:1.4, ease:'power2.out', immediateRender:false}, S2)
  .to('#h2 .w', {opacity:0, scaleY:.1, duration:.28, ease:'power3.in', stagger:.03}, S3-.3)
  .to('#underline', {scaleX:0, transformOrigin:'100% 50%', duration:.28, ease:'power3.in'}, S3-.25)
  .to('#net', {y:0, scale:.55, opacity:1, duration:.6, ease:'expo.inOut'}, S3-.35);

// SHOT 3 (S3 - S4): services fly out from the network as solid chips, content appears on landing
tl.fromTo('#s3title', {opacity:0, y:-40}, {opacity:1, y:0, duration:.5, ease:'power3.out', immediateRender:false}, S3)
  .to(linkEls, {opacity:1, duration:.35, stagger:.08}, S3+.05)
  .fromTo(cards, {x:toCenterX, y:toCenterY}, {x:0, y:0, opacity:1, scale:1, duration:.75, ease:'back.out(1.5)', stagger:.1, immediateRender:false}, S3+.1);
cards.forEach((c,i)=> tl.to(c.children, {opacity:1, duration:.3, stagger:.05}, S3+.1+i*.1+.55));
tl.to('#net', {rotation:24, duration:3.6, ease:'sine.inOut'}, S3)
  .to(cards, {boxShadow:'0 0 60px rgba(227,18,27,.55)', duration:.45, yoyo:true, repeat:1, stagger:.1}, S3+1.7)
// exit: all cards collapse together, matched cut on the network scaling up
  .to(cards, {x:toCenterX, y:toCenterY, scale:.2, opacity:0, duration:.4, ease:'power3.in'}, S4-.5)
  .to(linkEls, {opacity:0, duration:.25}, S4-.5)
  .to('#s3title', {opacity:0, y:-40, duration:.3, ease:'power3.in'}, S4-.5)
  .to('#net', {scale:2.6, opacity:.12, rotation:60, duration:.75, ease:'expo.inOut'}, S4-.4);

// SHOT 4 (S4 - S5): numbers from scuti.asia; the year is fixed (no counting)
const nums = [...document.querySelectorAll('.stat .num[data-to]')];
tl.set('#stats', {opacity:1}, S4)
  .fromTo('.stat', {y:120, opacity:0}, {y:0, opacity:1, duration:.55, ease:'power3.out', stagger:.08, immediateRender:false}, S4)
  .fromTo('.stat .bar', {scaleX:0}, {scaleX:1, duration:.7, ease:'expo.out', stagger:.08, immediateRender:false}, S4+.25)
  .to('#src', {opacity:1, duration:.4}, S4+.5)
  .to('#net', {rotation:110, duration:2.6, ease:'none'}, S4+.3);
gsap.set(nums, {innerHTML:(i,n)=>'0'+(n.dataset.suffix?'<small>+</small>':'')});
nums.forEach((n,i)=>{ const o={v:0}; const to=+n.dataset.to; const suf=n.dataset.suffix?'<small>+</small>':'';
  tl.fromTo(o, {v:0}, {v:to, duration:1.2, ease:'power2.out', immediateRender:false, onUpdate:()=>{ n.innerHTML=Math.round(o.v)+suf; }}, S4+.1+(i+1)*.08); });
tl.to('.stat', {y:80, opacity:0, duration:.35, ease:'power3.in', stagger:.05}, S5-.35)
  .to('#src', {opacity:0, duration:.25}, S5-.35)
// the carrier object stays on screen: it shrinks straight into its place in the logo lockup
  .to('#net', {scale:.6, opacity:1, x:-270, y:0, rotation:360, duration:.8, ease:'expo.inOut'}, S5-.3);

// SHOT 5 (S5 - D): dragon flight (overlaps the network move) then logo lockup
const headPos = {p:0};
const placeHead = () => { const pt = trail.getPointAtLength(TL*headPos.p), pt2 = trail.getPointAtLength(Math.max(0,TL*headPos.p-4));
  const ang = Math.atan2(pt.y-pt2.y, pt.x-pt2.x)*180/Math.PI;
  gsap.set('#dragonHead', {attr:{transform:`translate(${pt.x},${pt.y}) rotate(${ang}) scale(.8,${Math.abs(ang)>90?-.8:.8})`}}); };
tl.set('#dragonHead', {opacity:1}, S5)
  .to(headPos, {p:1, duration:1.5, ease:'power2.inOut', onUpdate:placeHead}, S5)
  .to(trail, {strokeDashoffset:0, duration:1.5, ease:'power2.inOut'}, S5)
  .to(scales, {opacity:.7, duration:.5}, S5+1.5)
  .to('#dragon', {y:-14, duration:1.3, yoyo:true, repeat:1, ease:'sine.inOut'}, S5+1.6)
  .set('#lockup', {opacity:1}, S5+1.45)
  .to('#logoText .ch', {yPercent:0, duration:.55, ease:'power4.out', stagger:.05}, S5+1.5)
  .fromTo(['#dot1','#dot2'], {opacity:0, y:-120}, {opacity:1, y:0, duration:.6, ease:'bounce.out', stagger:.1, immediateRender:false}, S5+2.3)
  .fromTo('#tagline', {opacity:0, x:-40}, {opacity:1, x:0, duration:.55, ease:'power3.out', immediateRender:false}, S5+2.45)
  .fromTo('#url', {opacity:0, letterSpacing:'20px'}, {opacity:1, letterSpacing:'6px', duration:.65, ease:'power3.out', immediateRender:false}, S5+2.7)
  .to('#lockup', {scale:1.035, transformOrigin:'40% 50%', duration:D-S5-1.8, ease:'sine.inOut'}, S5+1.8)
  .to('#grid', {scale:1.06, duration:D-S5-1.8, ease:'sine.inOut'}, S5+1.8)
  .to('#fade', {opacity:1, duration:.4, ease:'power1.in'}, D-0.4);

"""
c = c[:start] + NEW + c[end:]
# CSS / markup tweaks
rep = [
    ("#s3title { left:0; width:100%; top:70px;", "#s3title { left:0; width:100%; top:100px;"),
    (".card { width:430px; padding:26px 30px;", ".card { width:500px; padding:22px 30px;"),
    (".card h3 { font-size:36px;", ".card h3 { font-size:36px; white-space:nowrap;"),
    (".card p { font-size:22px;", ".card p { font-size:28px;"),
    ("#logoText { left:820px;", "#logoText { overflow:hidden; padding-top:6px; left:880px;"),
    ("#tagline { left:820px;", "#tagline { left:880px;"),
    ("#url { left:820px;", "#url { left:880px;"),
    ('<div class="num" data-to="2015" data-from="1990">2015</div>', '<div class="num">2015</div>'),
    (".card .ic { width:54px; height:54px;", ".card .ic { width:46px; height:46px; font-size:20px !important; border-radius:12px !important;"),
]
for a, b in rep:
    assert a in c, a
    c = c.replace(a, b)
f.write_text(c, encoding="utf-8")
print("patched")
