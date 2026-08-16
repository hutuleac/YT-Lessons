#!/usr/bin/env python3
"""Render lessons from notes.

    python3 build.py lessons/context-engineering.py   # one lesson + refresh index
    python3 build.py --all                            # every lesson + index

A note (notes/<id>.py) is the durable unit: one short video, one concept, its own diagrams.
A lesson (lessons/<id>.py) is a manifest naming notes in teaching order. A note can appear in
any number of lessons, so a single-note lesson published today can be absorbed into a larger
one later without touching the note.

DESIGN
Dark-first, light supported. Monospace display / serif body — the machine speaks in mono, the
teaching speaks in serif. Palette is a signal-degradation axis (teal signal, magenta
interference) rather than green-good/red-bad, because the subject is quality decaying across a
gradient. Signature element: a context rail down the left edge that fills with scroll progress
and crosses into the dumb zone near the end, so the page enacts the thing it explains.
System font stacks only, all CSS/SVG inline — the page is self-contained with no build step.
"""
import html
import importlib.util
import pathlib
import sys

# Notes and lessons are data files loaded by path, and a stale .pyc silently serves the previous
# version whenever an edit keeps the same byte size within the same second — you edit a note,
# rebuild, and the page doesn't change. Never write bytecode for them.
sys.dont_write_bytecode = True

ROOT = pathlib.Path(__file__).parent
NOTES = ROOT / "notes"
LESSONS = ROOT / "lessons"


def load(path, attr):
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.pop(0)
    return getattr(mod, attr)


def e(s):
    return html.escape(str(s), quote=False)


CSS = """
*,*::before,*::after{box-sizing:border-box}
:root{
  --void:#0B0E14; --surface:#121824; --surface-2:#1B2333; --line:#2A3446;
  --ink:#E7EAF0; --muted:#8A94A8;
  --signal:#5EEAD4; --interference:#E879A6; --sand:#F2D9A7;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  --measure:63ch;
}
@media (prefers-color-scheme:light){
  :root{
    --void:#F5F7FA; --surface:#FFFFFF; --surface-2:#EDF1F6; --line:#D3DBE6;
    --ink:#131A26; --muted:#5C6779;
    --signal:#0E9C8A; --interference:#C4437A; --sand:#8A6A22;
  }
}
html{-webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--void); color:var(--ink);
  font-family:var(--serif); font-size:19px; line-height:1.62;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:var(--measure); margin:0 auto; padding:0 22px}
.wide{max-width:860px; margin:0 auto; padding:0 22px}

/* ---- signature: the context rail ---- */
.rail{position:fixed; left:0; top:0; bottom:0; width:3px; background:var(--line); z-index:50}
.rail i{display:block; width:100%; height:0; background:var(--signal); transition:height .12s linear}
.rail.deep i{background:var(--interference)}
.rail b{
  position:absolute; left:12px; top:0; font:500 10px/1 var(--mono);
  letter-spacing:.14em; text-transform:uppercase; color:var(--muted);
  white-space:nowrap; transform:translateY(-50%); opacity:0; transition:opacity .2s
}
.rail.on b{opacity:1}
@media (max-width:820px){ .rail{display:none} }

/* ---- masthead ---- */
header{padding:16vh 0 9vh; border-bottom:1px solid var(--line)}
.eyebrow{
  font:500 11px/1 var(--mono); letter-spacing:.2em; text-transform:uppercase;
  color:var(--signal); margin:0 0 26px
}
h1{
  font-family:var(--mono); font-size:clamp(30px,5.6vw,52px); line-height:1.06;
  letter-spacing:-.035em; font-weight:600; margin:0 0 26px; text-wrap:balance
}
.standfirst{font-size:21px; color:var(--ink); margin:0 0 22px}
.audience{
  font-family:var(--sans); font-size:13px; color:var(--muted);
  border-left:2px solid var(--interference); padding-left:12px; margin:0
}

/* ---- concept sections ---- */
section{padding:8vh 0 2vh; border-bottom:1px solid var(--line)}
section:last-of-type{border-bottom:0}
.bridge{
  font-size:19px; color:var(--muted); font-style:italic;
  max-width:var(--measure); margin:0 auto -3vh; padding:6vh 22px 0
}
.chead{margin-bottom:34px}
.cnum{
  font:500 11px/1 var(--mono); letter-spacing:.18em; text-transform:uppercase;
  color:var(--muted); display:block; margin-bottom:12px
}
.cnum s{text-decoration:none; color:var(--interference)}
h2{
  font-family:var(--mono); font-size:clamp(23px,3.4vw,33px); line-height:1.14;
  letter-spacing:-.03em; font-weight:600; margin:0 0 16px
}
.oneline{font-size:20px; color:var(--ink); margin:0}
p{margin:0 0 20px}

/* ---- numbers ---- */
.figs{
  display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line);
  border-radius:6px; overflow:hidden; margin:34px auto; max-width:860px
}
.fig{background:var(--surface); padding:18px 16px}
.fig b{display:block; font:600 25px/1 var(--mono); letter-spacing:-.03em; color:var(--sand)}
.fig i{display:block; font:400 11px/1 var(--mono); color:var(--muted); margin:6px 0 9px; font-style:normal}
.fig span{font-family:var(--sans); font-size:12.5px; line-height:1.4; color:var(--muted)}

/* ---- diagrams ---- */
figure{margin:44px auto; max-width:860px; padding:0 22px}
.plate{background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:26px 24px 20px; overflow-x:auto}
/* Below ~470px the diagrams would shrink until their labels overflow their own boxes,
   so they scroll inside the plate instead of becoming illegible. */
.plate svg{display:block; width:100%; min-width:420px; max-width:560px; margin:0 auto; height:auto; overflow:visible}
.d-label{font:400 10px var(--mono); fill:var(--muted); letter-spacing:.08em}
.d-num{font:600 11px var(--mono); fill:var(--sand); letter-spacing:.04em}
.d-node{font:500 12px var(--mono); fill:var(--ink)}
.d-fix{font:600 12px var(--mono); fill:var(--signal)}
figcaption{margin-top:16px}
figcaption b{display:block; font-family:var(--mono); font-size:14px; font-weight:600; margin-bottom:6px}
figcaption span{font-family:var(--sans); font-size:13.5px; line-height:1.5; color:var(--muted)}

/* ---- analogy ---- */
.analogy{max-width:860px; margin:38px auto; padding:0 22px}
.analogy q{
  display:block; font-size:23px; line-height:1.4; quotes:none;
  border-left:2px solid var(--signal); padding-left:20px
}
.analogy p{font-family:var(--sans); font-size:14px; color:var(--muted); margin:14px 0 0 22px}

/* ---- practice ---- */
.do{max-width:860px; margin:40px auto 0; padding:24px; background:var(--surface-2); border-radius:8px}
.do h3{font:500 11px/1 var(--mono); letter-spacing:.2em; text-transform:uppercase; color:var(--signal); margin:0 0 16px}
.do ul{margin:0; padding:0; list-style:none}
.do li{font-family:var(--sans); font-size:15px; line-height:1.5; padding:0 0 0 22px; margin-bottom:12px; position:relative}
.do li:last-child{margin-bottom:0}
.do li::before{content:"\\2192"; position:absolute; left:0; color:var(--interference); font-family:var(--mono)}

/* ---- source ---- */
.src{max-width:860px; margin:26px auto 0; padding:0 22px}
.src a{
  font:400 12px var(--mono); color:var(--muted); text-decoration:none;
  border-bottom:1px solid var(--line)
}
.src a:hover{color:var(--signal); border-color:var(--signal)}

/* ---- closing ---- */
.close{padding:10vh 0 14vh}
.close h2{color:var(--signal)}
footer{border-top:1px solid var(--line); padding:34px 0; font:400 12px var(--mono); color:var(--muted)}
footer a{color:var(--muted)}

a:focus-visible,button:focus-visible{outline:2px solid var(--signal); outline-offset:3px}
@media (prefers-reduced-motion:reduce){*{transition:none!important; scroll-behavior:auto!important}}
"""

# The deck is the lesson at presenting detail. It reads the slide-shaped fields — `skeleton`,
# `numbers`, `analogy`, `practice`, `diagrams` — and never `mechanism`, whose paragraphs would
# turn a slide back into the page. It shares the palette and type tokens above and drops the
# page's reading measure: a slide uses the whole viewport.
DECK_CSS = """
html{scroll-snap-type:y mandatory; scroll-behavior:smooth}
body{font-family:var(--sans)}
.slide{
  min-height:100dvh; scroll-snap-align:start; scroll-snap-stop:always;
  display:flex; flex-direction:column; justify-content:center;
  padding:clamp(58px,7vh,96px) clamp(30px,5vw,86px); position:relative; overflow:hidden
}
.slide>*{max-width:none}

/* ---- slide chrome: the same bar on every slide, the way a deck master works ---- */
.tick{
  position:absolute; top:clamp(22px,3.4vh,40px); left:clamp(30px,5vw,86px);
  right:clamp(30px,5vw,86px); display:flex; justify-content:space-between; gap:20px;
  font:500 11px/1 var(--mono); letter-spacing:.18em; text-transform:uppercase; color:var(--muted)
}
.tick s{text-decoration:none; color:var(--signal)}
.foot{
  position:absolute; bottom:clamp(22px,3.4vh,40px); left:clamp(30px,5vw,86px);
  right:clamp(30px,5vw,86px); display:flex; justify-content:space-between; gap:20px;
  align-items:center; font:400 11px/1 var(--mono); color:var(--muted)
}
.foot em{font-style:normal; letter-spacing:.06em}
.bar{position:absolute; left:0; right:0; bottom:0; height:3px; background:var(--line)}
.bar i{display:block; height:100%; background:var(--signal)}

/* ---- kinds ---- */
.k-title, .k-section, .k-close{background:var(--surface)}
/* The divider is the one slide with room to spare, so it splits: number left, concept right. */
@media (min-width:1000px){
  .k-section{display:grid; grid-template-columns:minmax(200px,22%) 1fr;
             gap:clamp(30px,4vw,70px); align-items:center; align-content:center}
  .k-section .idx{grid-row:1 / span 3; align-self:start; margin:0}
  .k-section h2, .k-section .lead, .k-section .src{grid-column:2}
}
.k-section .idx{
  font:600 clamp(64px,13vw,180px)/0.82 var(--mono); letter-spacing:-.05em;
  color:var(--line); margin:0 0 clamp(14px,2vh,26px)
}
.slide h1{font-size:clamp(34px,6.4vw,84px); margin:0 0 clamp(18px,3vh,32px)}
.slide h2{font-size:clamp(28px,5vw,64px); margin:0 0 clamp(16px,2.6vh,28px)}
.k-bullets h2, .k-do h2, .k-figs h2{font-size:clamp(22px,3.2vw,40px); color:var(--muted)}
.slide .lead{
  font-family:var(--serif); font-size:clamp(19px,2.3vw,30px); line-height:1.42;
  color:var(--muted); margin:0; max-width:36ch
}
.k-close .lead{color:var(--ink); max-width:44ch}
.k-title .audience{margin-top:clamp(20px,3vh,36px); font-size:clamp(12px,1.2vw,15px)}

/* ---- bullets ---- */
.bul{list-style:none; margin:0; padding:0; display:grid; gap:clamp(14px,2.6vh,30px); counter-reset:b}
.bul li{
  font-size:clamp(21px,2.9vw,42px); line-height:1.22; padding-left:1.5em; position:relative;
  text-wrap:balance; counter-increment:b
}
.bul li::before{
  content:counter(b); position:absolute; left:0; top:.3em;
  font:500 .42em var(--mono); color:var(--signal); letter-spacing:.1em
}

/* ---- big numbers ---- */
.nums{display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:clamp(20px,3vw,44px)}
.nums div{border-top:2px solid var(--line); padding-top:clamp(12px,2vh,20px)}
.nums b{display:block; font:600 clamp(34px,5.4vw,68px)/1 var(--mono); letter-spacing:-.04em; color:var(--sand)}
.nums i{display:block; font:400 clamp(12px,1.2vw,15px) var(--mono); font-style:normal; color:var(--muted); margin:10px 0 8px}
.nums span{font-size:clamp(13px,1.3vw,17px); line-height:1.4; color:var(--muted)}

/* ---- quote ---- */
.k-quote q{
  display:block; quotes:none; font-family:var(--serif); font-size:clamp(28px,4.6vw,62px);
  line-height:1.22; border-left:3px solid var(--signal); padding-left:clamp(20px,2.6vw,40px);
  text-wrap:balance
}
.k-quote p{
  margin:clamp(18px,3vh,32px) 0 0 clamp(23px,2.9vw,43px); color:var(--muted);
  font-size:clamp(14px,1.5vw,20px); max-width:52ch
}

/* ---- what to do ---- */
.acts{list-style:none; margin:0; padding:0; display:grid; gap:clamp(14px,2.4vh,26px);
      grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr))}
.acts li{
  font-size:clamp(16px,1.8vw,24px); line-height:1.35; padding-left:1.5em; position:relative;
  background:var(--surface-2); border-radius:8px; padding:clamp(16px,2vh,24px) clamp(18px,2vw,26px)
              clamp(16px,2vh,24px) clamp(38px,3.4vw,52px)
}
.acts li::before{
  content:"\\2192"; position:absolute; left:clamp(16px,1.6vw,24px); top:clamp(16px,2vh,24px);
  color:var(--interference); font-family:var(--mono)
}

/* ---- diagrams ---- */
/* SVG text is sized in user units, so an unclamped slide plate renders 10px labels at 40px+.
   Twice the page's cap is the ceiling that stays proportionate on a projector. */
.slide figure{margin:0 auto; padding:0; max-width:1180px; width:100%}
.slide .plate{padding:clamp(20px,3vw,42px); width:100%}
.slide .plate svg{max-width:1040px}
.slide figcaption{margin:clamp(16px,2.4vh,26px) auto 0; text-align:center}
.slide figcaption b{font-size:clamp(15px,1.5vw,21px)}
.slide figcaption span{font-size:clamp(13px,1.2vw,17px)}

.slide .src{max-width:none; margin:clamp(22px,4vh,44px) 0 0; padding:0}
@media print{
  html{scroll-snap-type:none}
  .slide{min-height:auto; height:auto; page-break-after:always; break-after:page}
  .bar{display:none}
}
"""

RAIL_JS = """
(function(){
  var r=document.getElementById('rail'),f=r.firstElementChild,t=r.lastElementChild;
  function u(){
    var h=document.documentElement,
        m=(h.scrollHeight-h.clientHeight)||1,
        p=Math.min(1,Math.max(0,(h.scrollTop||document.body.scrollTop)/m));
    f.style.height=(p*100)+'%';
    t.style.top=(4+p*92)+'%';
    t.textContent=p<0.72?'smart zone':'dumb zone';
    r.classList.toggle('deep',p>=0.72);
    r.classList.toggle('on',p>0.02);
  }
  addEventListener('scroll',u,{passive:true}); addEventListener('resize',u); u();
})();
"""


def render_note(n, idx, total, bridge):
    o = []
    if bridge:
        o.append(f'<p class="bridge">{e(bridge)}</p>')
    o.append(f'<section id="{e(n["id"])}">')

    # Structural device: the prerequisite chain, which is real data from the note.
    pre = n.get("prerequisites") or []
    chain = f' &middot; builds on <s>{e(", ".join(pre))}</s>' if pre else " &middot; start here"
    o.append('<div class="wrap"><div class="chead">')
    o.append(f'<span class="cnum">{idx} / {total}{chain}</span>')
    o.append(f'<h2>{e(n["concept"])}</h2>')
    o.append(f'<p class="oneline">{e(n["one_liner"])}</p>')
    o.append("</div></div>")

    o.append('<div class="wrap">')
    for p in n.get("mechanism", []):
        o.append(f"<p>{e(p)}</p>")
    o.append("</div>")

    figs = n.get("numbers") or []
    if figs:
        o.append('<div class="figs">')
        for f in figs:
            o.append(
                f'<div class="fig"><b>{e(f["value"])}</b>'
                f'<i>{e(f.get("unit",""))}</i><span>{e(f["label"])}</span></div>'
            )
        o.append("</div>")

    for d in n.get("diagrams") or []:
        o.append(
            f'<figure><div class="plate">{d["svg"]}</div>'
            f'<figcaption><b>{e(d["title"])}</b><span>{e(d["caption"])}</span></figcaption></figure>'
        )

    a = n.get("analogy")
    if a:
        o.append(f'<div class="analogy"><q>{e(a["text"])}</q><p>{e(a["note"])}</p></div>')

    if n.get("practice"):
        o.append('<div class="do"><h3>What to do</h3><ul>')
        for p in n["practice"]:
            o.append(f"<li>{e(p)}</li>")
        o.append("</ul></div>")

    s = n["source"]
    o.append(
        f'<div class="src"><a href="{e(s["url"])}" target="_blank" rel="noopener">'
        f'{e(s["channel"])} &middot; {e(s["title"])} &middot; {e(s["duration"])} &#8599;</a></div>'
    )
    o.append("</section>")
    return "\n".join(o)


def build_deck(L, notes):
    """The lesson as slides: one kind of slide per slide-shaped field of the note.

    `mechanism` is deliberately absent — its paragraphs are what make a page a page.
    """
    slides = []  # (label, kind, inner html)
    slides.append((
        L["subject"], "title",
        f'<h1>{e(L["title"])}</h1><p class="lead">{e(L["standfirst"])}</p>'
        f'<p class="audience">{e(L["audience"])}</p>',
    ))

    for i, nid in enumerate(L["notes"], 1):
        n = notes[nid]
        if not n.get("skeleton"):
            raise SystemExit(f"notes/{nid}.py: empty 'skeleton' — the deck has nothing to show")
        label = n["concept"]
        s = n["source"]

        # Divider: the number carries the position so the concept slide doesn't have to.
        slides.append((
            label, "section",
            f'<p class="idx">{i:02d}</p><h2>{e(n["concept"])}</h2>'
            f'<p class="lead">{e(n["one_liner"])}</p>'
            f'<div class="src"><a href="{e(s["url"])}" target="_blank" rel="noopener">'
            f'{e(s["channel"])} &middot; {e(s["title"])} &middot; {e(s["duration"])} &#8599;</a></div>',
        ))
        slides.append((
            label, "bullets",
            f'<h2>{e(n["concept"])}</h2><ol class="bul">'
            + "".join(f"<li>{e(x)}</li>" for x in n["skeleton"])
            + "</ol>",
        ))
        for d in n.get("diagrams") or []:
            slides.append((
                label, "figs",
                f'<figure><div class="plate">{d["svg"]}</div>'
                f'<figcaption><b>{e(d["title"])}</b><span>{e(d["caption"])}</span>'
                f"</figcaption></figure>",
            ))
        if n.get("numbers"):
            slides.append((
                label, "nums",
                '<h2>By the numbers</h2><div class="nums">'
                + "".join(
                    f'<div><b>{e(f["value"])}</b><i>{e(f.get("unit",""))}</i>'
                    f'<span>{e(f["label"])}</span></div>'
                    for f in n["numbers"]
                )
                + "</div>",
            ))
        a = n.get("analogy")
        if a:
            slides.append((label, "quote", f'<q>{e(a["text"])}</q><p>{e(a["note"])}</p>'))
        if n.get("practice"):
            slides.append((
                label, "do",
                '<h2>What to do</h2><ul class="acts">'
                + "".join(f"<li>{e(x)}</li>" for x in n["practice"])
                + "</ul>",
            ))

    c = L.get("closing")
    if c:
        slides.append((
            "In one move", "close",
            f'<h2>{e(c["title"])}</h2><p class="lead">{e(c["body"])}</p>',
        ))

    total = len(slides)
    body = []
    for i, (label, kind, inner) in enumerate(slides, 1):
        body.append(
            f'<section class="slide k-{kind}">'
            f'<div class="tick"><span>{e(label)}</span><s>{i} / {total}</s></div>'
            f"{inner}"
            f'<div class="foot"><em>{e(L["subject"])}</em><em>{e(L["title"])}</em></div>'
            f'<div class="bar"><i style="width:{i / total * 100:.1f}%"></i></div></section>'
        )

    doc = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{e(L['title'])} &mdash; deck</title>\n"
        f"<style>{CSS}{DECK_CSS}</style>\n</head>\n<body>\n"
        + "\n".join(body)
        + "\n</body>\n</html>\n"
    )
    out = ROOT / f"{L['id']}-deck.html"
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out.name}  ({total} slides)")


def check_note(nid, n):
    """Catch the errors that would otherwise render silently to the reader."""
    if n["id"] != nid:
        raise SystemExit(f"notes/{nid}.py: declares id '{n['id']}' — must match its filename")
    for field in ("prerequisites", "related"):
        for ref in n.get(field) or []:
            if not (NOTES / f"{ref}.py").exists():
                raise SystemExit(
                    f"notes/{nid}.py: {field} names '{ref}', which is not a note. "
                    f"Typo, or write that note first."
                )


def build_lesson(path):
    L = load(path, "LESSON")
    notes = {}
    for i in L["notes"]:
        f = NOTES / f"{i}.py"
        if not f.exists():
            raise SystemExit(f"{path.name}: lists note '{i}', which does not exist")
        notes[i] = load(f, "NOTE")
        check_note(i, notes[i])

    # The concept graph is enforced, not decorative: a note may not appear before its prerequisite.
    seen = []
    for nid in L["notes"]:
        for p in notes[nid].get("prerequisites") or []:
            if p not in L["notes"]:
                # The heading renders "builds on <p>", so an absent prerequisite points the
                # reader at a concept this lesson never teaches.
                raise SystemExit(
                    f"{path.name}: '{nid}' builds on '{p}', which the lesson never covers — "
                    f"add '{p}' to 'notes' before it"
                )
            if p not in seen:
                raise SystemExit(
                    f"{path.name}: '{nid}' needs '{p}' first — reorder 'notes' in the lesson"
                )
        seen.append(nid)

    body = [
        '<div class="rail" id="rail"><i></i><b></b></div>',
        "<header><div class='wrap'>",
        f'<p class="eyebrow">{e(L["subject"])}</p>',
        f'<h1>{e(L["title"])}</h1>',
        f'<p class="standfirst">{e(L["standfirst"])}</p>',
        f'<p class="audience">{e(L["audience"])}</p>',
        "</div></header>",
    ]
    total = len(L["notes"])
    for i, nid in enumerate(L["notes"], 1):
        body.append(render_note(notes[nid], i, total, L.get("bridges", {}).get(nid)))

    c = L.get("closing")
    if c:
        body.append(
            f'<div class="close"><div class="wrap"><h2>{e(c["title"])}</h2>'
            f'<p>{e(c["body"])}</p></div></div>'
        )
    body.append(
        '<footer><div class="wrap">Built from short-form video. '
        '<a href="index.html">All lessons</a></div></footer>'
    )

    doc = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<title>{e(L['title'])}</title>\n"
        f'<meta name="description" content="{e(L["standfirst"])}">\n'
        f"<style>{CSS}</style>\n</head>\n<body>\n"
        + "\n".join(body)
        + f"\n<script>{RAIL_JS}</script>\n</body>\n</html>\n"
    )
    out = ROOT / f"{L['id']}.html"
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out.name}  ({total} notes)")
    build_deck(L, notes)
    return L


def build_index(all_lessons):
    cards = []
    for L in sorted(all_lessons, key=lambda x: x["id"]):
        cards.append(
            f'<li><a href="{e(L["id"])}.html"><span class="k">{e(L["subject"])}</span>'
            f'<b>{e(L["title"])}</b><i>{e(L["standfirst"])}</i>'
            f'<u>{len(L["notes"])} concepts</u></a>'
            f'<p class="dk"><a href="{e(L["id"])}-deck.html">Deck &#8599;</a></p></li>'
        )
    doc = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>Lessons</title>\n<style>"
        + CSS
        + """
        .ix{max-width:860px;margin:0 auto;padding:14vh 22px 12vh}
        .ix ul{list-style:none;margin:44px 0 0;padding:0}
        .ix li{border-top:1px solid var(--line)}
        .ix a{display:block;padding:30px 0;text-decoration:none;color:inherit}
        .ix a:hover b{color:var(--signal)}
        .k{font:500 11px/1 var(--mono);letter-spacing:.2em;text-transform:uppercase;color:var(--interference)}
        .ix b{display:block;font-family:var(--mono);font-size:26px;font-weight:600;
              letter-spacing:-.03em;margin:12px 0 10px}
        .ix i{display:block;font-style:normal;color:var(--muted);font-size:17px;max-width:60ch}
        .ix u{display:block;text-decoration:none;font:400 11px var(--mono);color:var(--muted);margin-top:14px}
        .dk{margin:0 0 30px}
        /* .ix a matches this link too and only it declares display/padding — restate both. */
        .dk a{display:inline;padding:0;font:400 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;
              color:var(--muted);text-decoration:none;border-bottom:1px solid var(--line)}
        .dk a:hover{color:var(--signal);border-color:var(--signal)}
        </style>\n</head>\n<body>\n<div class="ix">
        <p class="eyebrow">Lessons</p>
        <h1>Ideas worth more than 60 seconds</h1>
        <p class="standfirst">Short-form video, taken apart and put back together as something you
        can actually learn from.</p>
        <ul>"""
        + "".join(cards)
        + "</ul></div>\n</body>\n</html>\n"
    )
    (ROOT / "index.html").write_text(doc, encoding="utf-8")
    print(f"wrote index.html  ({len(cards)} lessons)")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--all" in sys.argv or not args:
        paths = sorted(LESSONS.glob("*.py"))
    else:
        paths = [pathlib.Path(a) for a in args]
    if not paths:
        raise SystemExit("no lessons found in lessons/")
    built = [build_lesson(p) for p in paths]
    # The index always reflects every lesson on disk, not just the one just built.
    build_index([load(p, "LESSON") for p in sorted(LESSONS.glob("*.py"))] if args else built)


if __name__ == "__main__":
    main()
