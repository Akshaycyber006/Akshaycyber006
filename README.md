<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Akshay Krishna — Developer / B.Tech IT</title>
<meta name="description" content="Akshay Krishna — IT student & developer. Software development, AI, cybersecurity. Chennai, India. Build • Innovate • Contribute." />
<meta name="theme-color" content="#1e37a0" />

<!-- Fonts (Press Start 2P for pixel headings, VT323 for pixel body) -->
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&family=Share+Tech+Mono&display=swap" rel="stylesheet" />

<!-- Favicon: inline pixel "A" -->
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' fill='%231e37a0'/%3E%3Ctext x='8' y='12' text-anchor='middle' fill='%23fff' font-family='monospace' font-size='11' font-weight='bold'%3EA%3C/text%3E%3C/svg%3E" />

<style>
/* ===================================================================
   PIXEL-ART GITHUB PROFILE  —  single-file website
   Palette: royal blue on white  •  retro 8-bit
=================================================================== */
:root{
  --bg:#ffffff;
  --ink:#0f1a52;
  --blue-deep:#0a1340;
  --blue:#1e37a0;
  --blue-mid:#2a3eb1;
  --blue-light:#9db4f5;
  --blue-pale:#c9d6ff;
  --blue-mist:#eef0ff;
  --gold:#ffcc66;
  --card-bg:#ffffff;
  --shadow:#9db4f5;
  --ok:#1e37a0;
  --warn:#c47a00;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:'VT323','Share Tech Mono','Courier New',monospace;
  font-size:clamp(17px,1.15vw,21px);
  background:var(--bg);
  color:var(--ink);
  line-height:1.45;
  overflow-x:hidden;
  -webkit-font-smoothing:none;
}
/* CRT scanlines + vignette over everything */
body::before{
  content:"";position:fixed;inset:0;pointer-events:none;z-index:9999;
  background:
    repeating-linear-gradient(0deg, rgba(15,26,82,.035) 0 1px, transparent 1px 3px),
    radial-gradient(ellipse at center, transparent 55%, rgba(10,19,64,.12) 100%);
}
.pixel{font-family:'Press Start 2P','Courier New',monospace;letter-spacing:1px}
.wrap{max-width:1120px;margin:0 auto;padding:0 clamp(12px,3vw,28px)}
a{color:var(--blue);text-decoration:none}
a:hover{text-decoration:underline}

/* ---------- HERO ---------- */
.hero-wrap{width:100%;background:var(--blue-deep)}
.hero-wrap svg{display:block;width:100%;height:auto}

/* ---------- SECTION SHELL ---------- */
section{padding:clamp(28px,4vw,52px) 0}
.sec-title{
  font-family:'Press Start 2P',monospace;
  font-size:clamp(11px,1.7vw,16px);
  color:var(--blue);
  text-align:center;
  margin-bottom:clamp(18px,2.5vw,30px);
  letter-spacing:1px;
}
.sec-title::before{content:"< "}
.sec-title::after{content:" />"}
.sec-title .a{color:var(--gold)}

/* ---------- GRID ---------- */
.grid{display:grid;gap:clamp(16px,2vw,26px);align-items:start}
.grid-3{grid-template-columns:repeat(3,1fr)}
.grid-2{grid-template-columns:repeat(2,1fr)}
@media (max-width:900px){.grid-3{grid-template-columns:1fr}.grid-2{grid-template-columns:1fr}}
@media (min-width:901px) and (max-width:1080px){.grid-3{grid-template-columns:repeat(2,1fr)}}

/* ---------- CARD ---------- */
.card{
  background:var(--card-bg);
  border:4px solid var(--blue);
  box-shadow:8px 8px 0 0 var(--shadow);
  padding:clamp(16px,2vw,26px);
  position:relative;
  transition:transform .15s ease, box-shadow .15s ease;
}
.card:hover{transform:translate(-3px,-3px);box-shadow:11px 11px 0 0 var(--blue-mid)}
.card::before{
  content:"";position:absolute;top:-4px;left:8px;right:8px;height:4px;
  background:repeating-linear-gradient(90deg,var(--blue) 0 8px,transparent 8px 12px);
  opacity:.25;
}
.card h3{
  font-family:'Press Start 2P',monospace;
  font-size:clamp(10px,1.4vw,13px);
  color:var(--blue);
  text-align:center;
  margin-bottom:14px;
  letter-spacing:1px;
}
.card p{margin:6px 0}
.card ul{list-style:none;padding:0;margin:10px 0}
.card li{padding:4px 0;border-bottom:1px dashed var(--blue-mist);font-size:clamp(15px,1.1vw,18px)}
.card li:last-child{border-bottom:none}
.b{color:var(--blue-deep);font-weight:700}

/* ---------- ABOUT ---------- */
.about-head{display:flex;gap:14px;align-items:center;justify-content:center;margin-bottom:8px}
.avatar{
  width:64px;height:64px;border:3px solid var(--blue);
  box-shadow:4px 4px 0 0 var(--shadow);
  background:var(--blue-mist);
  image-rendering:pixelated;
}
.about-line{display:flex;align-items:center;gap:8px;padding:3px 0;font-size:clamp(15px,1.1vw,18px)}
.about-line .ic{width:22px;text-align:center}

/* ---------- TECH STACK ---------- */
.tech-img{width:100%;max-width:340px;display:block;margin:0 auto}
.tech-tags{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-top:10px}
.tech-tags code{
  font-family:'Share Tech Mono',monospace;font-size:13px;
  background:var(--blue-mist);color:var(--blue);
  padding:3px 7px;border:1px solid var(--blue-light);
}

/* ---------- FEATURED PROJECT ---------- */
.proj-name{font-family:'Press Start 2P',monospace;font-size:clamp(12px,1.6vw,15px);color:var(--blue);text-align:center;margin:4px 0 2px}
.proj-sub{text-align:center;color:var(--blue-mid);font-style:italic;margin-bottom:10px}
.proj-check li::before{content:"[x] ";color:var(--blue);font-weight:700}
.btn{
  display:inline-block;font-family:'Press Start 2P',monospace;font-size:10px;
  background:var(--blue);color:#fff;padding:11px 16px;border:none;
  box-shadow:5px 5px 0 0 var(--blue-deep);cursor:pointer;letter-spacing:1px;
  transition:transform .1s, box-shadow .1s;
}
.btn:hover{text-decoration:none;transform:translate(3px,3px);box-shadow:2px 2px 0 0 var(--blue-deep)}
.btn:active{transform:translate(5px,5px);box-shadow:0 0 0 0 var(--blue-deep)}

/* ---------- STATS ---------- */
.stats-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:14px}
.stat{background:var(--blue-mist);border:2px solid var(--blue-light);padding:8px 4px;text-align:center}
.stat .num{font-family:'Press Start 2P',monospace;font-size:clamp(15px,2.4vw,22px);color:var(--blue);display:block}
.stat .lbl{font-size:13px;color:var(--blue-mid);text-transform:uppercase;letter-spacing:1px}
.stat-img{width:100%;display:block;border:2px solid var(--blue-light);margin-top:10px}
.status-pill{
  display:inline-block;font-family:'Share Tech Mono',monospace;font-size:12px;
  padding:2px 8px;border:1px solid var(--blue-light);background:var(--blue-mist);
  color:var(--blue-mid);margin-top:8px;
}
.status-pill.live{border-color:var(--blue);color:var(--blue)}
.status-pill.offline{border-color:var(--warn);color:var(--warn)}

/* ---------- LANGUAGES ---------- */
.lang-row{display:flex;align-items:center;gap:8px;margin:5px 0;font-size:15px}
.lang-name{width:88px;flex-shrink:0;color:var(--blue-deep)}
.lang-bar{flex:1;height:14px;background:var(--blue-mist);border:1px solid var(--blue-light);position:relative;min-width:40px}
.lang-fill{height:100%;background:linear-gradient(90deg,var(--blue),var(--blue-mid));transition:width .8s ease}
.lang-pct{width:42px;text-align:right;color:var(--blue-mid);font-size:14px}

/* ---------- CONNECT ---------- */
.badge{display:block;margin:6px auto;max-width:260px}
.badge img{width:100%;display:block}

/* ---------- HEATMAP ---------- */
.heatmap-card .heatmap-meta{text-align:center;color:var(--blue-mid);font-size:14px;margin-bottom:10px}
.heatmap-scroll{overflow-x:auto;padding-bottom:6px}
.heatmap{
  display:grid;grid-template-columns:repeat(13,minmax(14px,1fr));gap:3px;
  min-width:260px;
}
.cell{
  aspect-ratio:1;background:var(--blue-mist);border:1px solid #dce3ff;
  transition:transform .1s;
}
.cell:hover{transform:scale(1.4);z-index:2;position:relative}
.cell.l0{background:#eef0ff}
.cell.l1{background:#c9d6ff}
.cell.l2{background:#9db4f5}
.cell.l3{background:#4f6fd6}
.cell.l4{background:#1e37a0;border-color:#1e37a0}
.heatmap-legend{display:flex;align-items:center;gap:4px;justify-content:center;margin-top:10px;font-size:13px;color:var(--blue-mid)}
.heatmap-legend .cell{width:12px;height:12px;aspect-ratio:auto}
.activity-img{width:100%;display:block;border:2px solid var(--blue-light);margin-top:14px}

/* ---------- REPOS ---------- */
.repo{
  display:block;border:3px solid var(--blue);background:#fff;
  padding:12px 14px;margin-bottom:12px;box-shadow:5px 5px 0 0 var(--shadow);
  transition:transform .12s,box-shadow .12s;
}
.repo:hover{text-decoration:none;transform:translate(-2px,-2px);box-shadow:7px 7px 0 0 var(--blue-mid)}
.repo-name{font-family:'Press Start 2P',monospace;font-size:11px;color:var(--blue);margin-bottom:4px;word-break:break-word}
.repo-desc{color:var(--ink);font-size:15px;margin-bottom:6px;min-height:18px}
.repo-meta{display:flex;flex-wrap:wrap;gap:10px;font-size:13px;color:var(--blue-mid)}
.repo-meta .dot{display:inline-flex;align-items:center;gap:4px}
.repo-lang-dot{width:10px;height:10px;display:inline-block;border:1px solid var(--blue-light)}

/* ---------- FOOTER ---------- */
.footer{background:var(--blue-deep);margin-top:0}
.footer svg{display:block;width:100%;height:auto}
.foot-note{text-align:center;color:var(--blue-light);font-size:14px;padding:14px 0 24px;background:var(--blue-deep)}
.foot-note a{color:var(--gold)}
.foot-note .heart{color:#ff7a7a}

/* top button */
.totop{
  position:fixed;right:18px;bottom:18px;z-index:1000;
  font-family:'Press Start 2P',monospace;font-size:11px;
  background:var(--blue);color:#fff;border:none;padding:12px 14px;cursor:pointer;
  box-shadow:5px 5px 0 0 var(--blue-deep);display:none;
}
.totop.show{display:block}
.totop:hover{transform:translate(3px,3px);box-shadow:2px 2px 0 0 var(--blue-deep)}

/* tiny helpers */
.center{text-align:center}
.muted{color:var(--blue-mid)}
.skel{display:inline-block;min-width:40px;height:18px;background:var(--blue-mist);border:1px solid var(--blue-light);vertical-align:middle}
hr.dashed{border:none;border-top:2px dashed var(--blue-light);margin:12px 0}
</style>
</head>
<body>

<!-- ===================== HERO ===================== -->
<div class="hero-wrap">
<!-- INLINE ANIMATED PIXEL-ART HERO SVG (night scene, coder, moon, twinkling stars, blinking cursor) -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="900" height="340" role="img" aria-label="Akshay Krishna — Developer / B.Tech IT — Build • Innovate • Contribute">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#070d2e"/><stop offset="0.55" stop-color="#0f1a52"/><stop offset="1" stop-color="#1e37a0"/>
    </linearGradient>
    <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#16307f"/><stop offset="1" stop-color="#0b1840"/>
    </linearGradient>
    <linearGradient id="screen" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#9db4f5"/><stop offset="1" stop-color="#c9d6ff"/>
    </linearGradient>
    <pattern id="dither" x="0" y="0" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="4" fill="none"/>
      <rect x="0" y="0" width="1" height="1" fill="#ffffff" opacity="0.05"/>
      <rect x="2" y="2" width="1" height="1" fill="#ffffff" opacity="0.05"/>
    </pattern>
    <style><![CDATA[
      .star{animation:tw 2.6s infinite ease-in-out;transform-origin:center}
      .s2{animation-delay:.4s}.s3{animation-delay:.8s}.s4{animation-delay:1.2s}.s5{animation-delay:1.6s}
      @keyframes tw{0%,100%{opacity:.25;transform:scale(.85)}50%{opacity:1;transform:scale(1.1)}}
      .moon{animation:glow 4s infinite ease-in-out;transform-origin:center}
      @keyframes glow{0%,100%{opacity:.9}50%{opacity:1}}
      .cursor{animation:blink 1.05s infinite step-end}
      @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
      .name{animation:fadein 1.6s ease-out both}
      .sub{animation:fadein 1.6s ease-out .25s both}
      .tag{animation:fadein 1.6s ease-out .5s both}
      @keyframes fadein{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}
      .code-screen{animation:scan 3.2s infinite linear}
      @keyframes scan{0%{opacity:.55}50%{opacity:1}100%{opacity:.55}}
      .cat-tail{animation:wag 1.8s infinite ease-in-out;transform-origin:0% 100%}
      @keyframes wag{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(10deg)}}
      .plant{animation:sway 3.5s infinite ease-in-out;transform-origin:50% 100%}
      @keyframes sway{0%,100%{transform:rotate(-2deg)}50%{transform:rotate(2deg)}}
      .rocket{animation:hover 2.4s infinite ease-in-out}
      @keyframes hover{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
      @media (prefers-reduced-motion:reduce){*{animation:none!important}}
    ]]></style>
  </defs>
  <rect width="900" height="340" fill="url(#sky)"/>
  <rect width="900" height="340" fill="url(#dither)"/>
  <rect x="0" y="270" width="900" height="70" fill="url(#floor)"/>
  <rect x="0" y="270" width="900" height="2" fill="#2a3eb1"/>
  <g fill="#ffffff">
    <rect class="star" x="40" y="30" width="3" height="3"/><rect class="star s2" x="90" y="55" width="2" height="2"/>
    <rect class="star s3" x="140" y="25" width="3" height="3"/><rect class="star s4" x="200" y="60" width="2" height="2"/>
    <rect class="star s5" x="260" y="35" width="3" height="3"/><rect class="star" x="320" y="70" width="2" height="2"/>
    <rect class="star s2" x="380" y="30" width="3" height="3"/><rect class="star s3" x="440" y="55" width="2" height="2"/>
    <rect class="star s4" x="500" y="25" width="3" height="3"/><rect class="star s5" x="560" y="65" width="2" height="2"/>
    <rect class="star" x="700" y="40" width="3" height="3"/><rect class="star s2" x="760" y="25" width="2" height="2"/>
    <rect class="star s3" x="820" y="60" width="3" height="3"/><rect class="star s4" x="860" y="35" width="2" height="2"/>
  </g>
  <g fill="#ffcc66">
    <rect class="star s2" x="170" y="40" width="3" height="3"/><rect class="star s4" x="420" y="45" width="3" height="3"/>
    <rect class="star" x="660" y="20" width="3" height="3"/><rect class="star s3" x="800" y="48" width="3" height="3"/>
  </g>
  <g class="moon" transform="translate(540,55)">
    <circle r="26" fill="#eef0ff"/>
    <circle cx="-9" cy="-7" r="5" fill="#9db4f5"/><circle cx="8" cy="6" r="4" fill="#9db4f5"/>
    <circle cx="-3" cy="10" r="3" fill="#9db4f5"/><circle cx="10" cy="-10" r="2.5" fill="#9db4f5"/>
  </g>
  <g transform="translate(50,30)">
    <rect width="90" height="70" fill="#0a1340" stroke="#2a3eb1" stroke-width="3"/>
    <rect x="3" y="3" width="84" height="64" fill="#0f1a52"/>
    <line x1="45" y1="3" x2="45" y2="67" stroke="#2a3eb1" stroke-width="2"/>
    <line x1="3" y1="35" x2="87" y2="35" stroke="#2a3eb1" stroke-width="2"/>
    <rect class="star" x="14" y="12" width="2" height="2" fill="#fff"/>
    <rect class="star s3" x="58" y="20" width="2" height="2" fill="#fff"/>
    <rect class="star s5" x="28" y="48" width="2" height="2" fill="#fff"/>
    <rect class="star s2" x="70" y="50" width="2" height="2" fill="#fff"/>
  </g>
  <g transform="translate(700,20)">
    <rect width="170" height="78" fill="#ffffff" stroke="#2a3eb1" stroke-width="3"/>
    <rect x="6" y="6" width="158" height="66" fill="none" stroke="#9db4f5" stroke-width="1"/>
    <text x="85" y="28" text-anchor="middle" fill="#1e37a0" font-size="14" font-weight="700" font-family="'Courier New',monospace" letter-spacing="1">DREAM</text>
    <text x="85" y="48" text-anchor="middle" fill="#1e37a0" font-size="14" font-weight="700" font-family="'Courier New',monospace" letter-spacing="1">CODE</text>
    <text x="85" y="68" text-anchor="middle" fill="#1e37a0" font-size="14" font-weight="700" font-family="'Courier New',monospace" letter-spacing="1">DEPLOY &#9829;</text>
  </g>
  <g transform="translate(620,150)">
    <rect width="56" height="90" fill="#0b1840" stroke="#2a3eb1" stroke-width="2"/>
    <rect x="4" y="6" width="10" height="34" fill="#9db4f5"/><rect x="16" y="6" width="10" height="34" fill="#ffffff"/>
    <rect x="28" y="6" width="10" height="34" fill="#2a3eb1"/><rect x="40" y="6" width="12" height="34" fill="#1e37a0"/>
    <rect x="4" y="48" width="10" height="34" fill="#ffffff"/><rect x="16" y="48" width="10" height="34" fill="#1e37a0"/>
    <rect x="28" y="48" width="10" height="34" fill="#9db4f5"/><rect x="40" y="48" width="12" height="34" fill="#2a3eb1"/>
  </g>
  <rect x="380" y="240" width="280" height="8" fill="#2a3eb1"/>
  <rect x="380" y="248" width="280" height="22" fill="#16307f"/>
  <rect x="500" y="232" width="40" height="8" fill="#2a3eb1"/>
  <rect x="450" y="160" width="140" height="74" rx="2" fill="#0b1840" stroke="#2a3eb1" stroke-width="3"/>
  <rect class="code-screen" x="456" y="166" width="128" height="62" fill="url(#screen)"/>
  <g fill="#1e37a0">
    <rect x="462" y="174" width="40" height="3"/><rect x="462" y="182" width="60" height="3"/>
    <rect x="470" y="190" width="50" height="3"/><rect x="470" y="198" width="30" height="3"/>
    <rect x="462" y="206" width="70" height="3"/><rect x="462" y="214" width="22" height="3"/>
    <rect class="cursor" x="488" y="214" width="6" height="3" fill="#1e37a0"/>
  </g>
  <g transform="translate(395,190)">
    <rect x="-2" y="20" width="34" height="40" fill="#0b1840"/>
    <rect x="2" y="24" width="28" height="36" fill="#1e37a0"/>
    <rect x="6" y="24" width="20" height="6" fill="#2a3eb1"/>
    <path d="M0 26 Q15 4 32 26 L32 28 L0 28 Z" fill="#16307f"/>
    <rect x="9" y="12" width="16" height="16" fill="#ffd5b5"/>
    <rect x="9" y="12" width="16" height="5" fill="#2a1500"/>
    <rect x="6" y="15" width="4" height="9" fill="#2a3eb1"/>
    <rect x="24" y="15" width="4" height="9" fill="#2a3eb1"/>
    <path d="M6 15 Q15 6 28 15" stroke="#2a3eb1" stroke-width="2" fill="none"/>
    <rect x="28" y="40" width="22" height="6" fill="#1e37a0"/>
    <rect x="48" y="38" width="14" height="10" fill="#ffd5b5"/>
    <rect x="46" y="48" width="22" height="6" fill="#0b1840" stroke="#2a3eb1" stroke-width="1"/>
  </g>
  <g class="plant" transform="translate(610,196)">
    <rect x="-9" y="32" width="22" height="14" fill="#2a3eb1"/>
    <rect x="-11" y="30" width="26" height="5" fill="#1e37a0"/>
    <path d="M0 32 L-9 12 L-3 18 L-2 0 L3 18 L9 8 L7 28 L11 16 L8 32 Z" fill="#1e37a0" stroke="#2a3eb1" stroke-width="1"/>
    <path d="M-2 30 L-6 18 L0 22 L4 14 L2 30 Z" fill="#9db4f5"/>
  </g>
  <g transform="translate(120,250)">
    <g class="cat-tail" transform="translate(34,12)">
      <rect x="0" y="-2" width="22" height="6" fill="#1e37a0"/>
      <rect x="20" y="-6" width="6" height="8" fill="#1e37a0"/>
    </g>
    <rect x="6" y="6" width="30" height="16" fill="#1e37a0"/>
    <rect x="10" y="-2" width="18" height="14" fill="#1e37a0"/>
    <rect x="10" y="-6" width="4" height="6" fill="#1e37a0"/>
    <rect x="24" y="-6" width="4" height="6" fill="#1e37a0"/>
    <rect x="14" y="2" width="2" height="3" fill="#ffcc66"/>
    <rect x="22" y="2" width="2" height="3" fill="#ffcc66"/>
    <rect x="9" y="22" width="4" height="6" fill="#16307f"/>
    <rect x="29" y="22" width="4" height="6" fill="#16307f"/>
  </g>
  <g class="rocket" transform="translate(660,110)">
    <rect x="0" y="0" width="8" height="18" fill="#ffffff"/>
    <path d="M0 0 L4 -6 L8 0 Z" fill="#ffcc66"/>
    <rect x="-2" y="14" width="12" height="4" fill="#9db4f5"/>
    <rect x="2" y="18" width="4" height="6" fill="#ffcc66" opacity="0.8"/>
  </g>
  <g>
    <text class="name" x="170" y="118" fill="#ffffff" font-size="34" font-weight="700" font-family="'Courier New',monospace" letter-spacing="2">AKSHAY KRISHNA</text>
    <text class="sub" x="172" y="142" fill="#9db4f5" font-size="15" font-family="'Courier New',monospace" letter-spacing="1">Developer  /  B.Tech IT</text>
    <text class="tag" id="heroTag" x="172" y="166" fill="#ffffff" font-size="13" font-family="'Courier New',monospace" letter-spacing="0.5">&lt; Build &#8226; Innovate &#8226; Contribute /&gt;<tspan class="cursor" fill="#ffcc66">&#9608;</tspan></text>
  </g>
  <rect x="2" y="2" width="896" height="336" fill="none" stroke="#2a3eb1" stroke-width="3"/>
  <rect x="6" y="6" width="888" height="328" fill="none" stroke="#9db4f5" stroke-width="1" opacity="0.4"/>
</svg>
</div>

<!-- ===================== ROW 1: ABOUT | TECH | FEATURED ===================== -->
<section>
  <div class="wrap">
    <div class="grid grid-3">

      <!-- ABOUT -->
      <div class="card">
        <h3>ABOUT ME</h3>
        <div class="about-head">
          <img id="avatar" class="avatar" alt="avatar" src="https://avatars.githubusercontent.com/Akshaycyber006" />
          <div>
            <div class="b pixel" style="font-size:11px">AKSHAY KRISHNA</div>
            <div class="muted" style="font-size:14px" id="bioLine">IT Student &amp; Developer</div>
          </div>
        </div>
        <p class="center" style="margin-top:6px">
          Hi! I'm <span class="b">Akshay Krishna</span> 👋<br/>
          Passionate about <span class="b">Software Development</span>, <span class="b">AI</span> and <span class="b">Cybersecurity</span>.<br/>
          Always learning, always building! 🚀
        </p>
        <hr class="dashed"/>
        <div class="about-line"><span class="ic">🎓</span><span><b>B.Tech IT</b></span></div>
        <div class="about-line"><span class="ic">📍</span><span><b id="locLine">Chennai, India</b></span></div>
        <div class="about-line"><span class="ic">🎯</span><span><b>Goal:</b> 12+ LPA</span></div>
        <div class="about-line"><span class="ic">♥</span><span><b>Dream:</b> Make an Impact</span></div>
        <hr class="dashed"/>
        <div class="center">
          <span id="statusPill" class="status-pill offline">loading live data…</span>
        </div>
      </div>

      <!-- TECH STACK -->
      <div class="card">
        <h3>TECH STACK</h3>
        <img class="tech-img" src="https://skillicons.dev/icons?i=c,cpp,python,java,html,css,js,mysql,linux,git,github,vscode&theme=light&perline=6" alt="tech stack icons" />
        <div class="tech-tags">
          <code>C</code><code>C++</code><code>Python</code><code>Java</code>
          <code>HTML5</code><code>CSS3</code><code>JavaScript</code>
          <code>SQL</code><code>Linux</code><code>Git</code>
          <code>GitHub</code><code>VS Code</code>
        </div>
      </div>

      <!-- FEATURED PROJECT -->
      <div class="card">
        <h3>FEATURED PROJECT</h3>
        <div class="proj-name">⚡ QRVerse</div>
        <div class="proj-sub">Smart QR &amp; File Sharing Platform</div>
        <ul class="proj-check">
          <li>Smart QR Generation &amp; Scanning</li>
          <li>Offline File Bridge</li>
          <li>AI OCR &amp; Translation</li>
          <li>Supabase Integration</li>
        </ul>
        <p class="center" style="margin-top:10px">
          <!-- Replace with the real QRVerse repo URL once published -->
          <a class="btn" href="https://github.com/Akshaycyber006?tab=repositories" target="_blank" rel="noopener">View Project →</a>
        </p>
      </div>

    </div>
  </div>
</section>

<!-- ===================== ROW 2: STATS | LANGUAGES | CONNECT ===================== -->
<section style="padding-top:0">
  <div class="wrap">
    <div class="grid grid-3">

      <!-- LIVE STATS -->
      <div class="card">
        <h3>GITHUB STATS</h3>
        <div class="stats-grid">
          <div class="stat"><span class="num" id="stRepos">—</span><span class="lbl">Repos</span></div>
          <div class="stat"><span class="num" id="stStars">—</span><span class="lbl">Stars</span></div>
          <div class="stat"><span class="num" id="stForks">—</span><span class="lbl">Forks</span></div>
          <div class="stat"><span class="num" id="stFollowers">—</span><span class="lbl">Followers</span></div>
        </div>
        <img class="stat-img" alt="GitHub stats card" src="https://github-readme-stats.vercel.app/api?username=Akshaycyber006&show_icons=true&include_all_commits=true&count_private=true&title_color=1e37a0&text_color=2a3eb1&icon_color=1e37a0&bg_color=ffffff&border_color=2a3eb1&hide_border=false&cache_seconds=86400" />
        <img class="stat-img" alt="GitHub streak card" src="https://streak-stats.demolab.com/?user=Akshaycyber006&ring_color=1e37a0&fire_color=ffcc66&currStreakNum=1e37a0&sideNums=2a3eb1&currStreakLabel=1e37a0&sideLabels=1e37a0&dates=2a3eb1&bg_color=ffffff&border_color=2a3eb1&hide_border=false" />
      </div>

      <!-- LIVE LANGUAGES -->
      <div class="card">
        <h3>TOP LANGUAGES</h3>
        <div id="langList">
          <div class="lang-row"><span class="lang-name muted">loading…</span></div>
        </div>
        <img class="stat-img" alt="Top languages card" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Akshaycyber006&layout=compact&langs_count=8&title_color=1e37a0&text_color=2a3eb1&bg_color=ffffff&border_color=2a3eb1&hide_border=false&cache_seconds=86400" />
        <p class="center muted" style="font-size:13px;margin-top:6px">across all public repositories (live)</p>
      </div>

      <!-- CONNECT -->
      <div class="card">
        <h3>LET'S CONNECT</h3>
        <a class="badge" href="https://github.com/Akshaycyber006" target="_blank" rel="noopener">
          <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Akshaycyber006-2a3eb1?style=for-the-badge&logo=github&logoColor=white" />
        </a>
        <!-- Replace akshaykrishna with your exact LinkedIn vanity slug -->
        <a class="badge" href="https://linkedin.com/in/akshaykrishna" target="_blank" rel="noopener">
          <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Akshay%20Krishna-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
        </a>
        <!-- Replace with your real email if different -->
        <a class="badge" href="mailto:akshaykrishna.email@gmail.com">
          <img alt="Email" src="https://img.shields.io/badge/Email-akshaykrishna.email@gmail.com-1e37a0?style=for-the-badge&logo=gmail&logoColor=white" />
        </a>
        <hr class="dashed"/>
        <div class="center">
          <img alt="profile views" src="https://komarev.com/ghpvc/?username=Akshaycyber006&label=Profile%20Views&color=1e37a0&style=for-the-badge&abbreviated=true" />
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ===================== CONTRIBUTION ACTIVITY (live heatmap + graph) ===================== -->
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-title">CONTRIBUTION <span class="a">ACTIVITY</span></div>

    <div class="card heatmap-card">
      <div class="heatmap-meta">
        Contribution calendar — <b>live, rendered from real GitHub data</b> (ghchart.rshah.org)
      </div>
      <!-- Real GitHub contribution calendar (server-side, the same graph as github.com/<user>) -->
      <div class="heatmap-scroll" style="text-align:center">
        <img class="activity-img" alt="Akshaycyber006 GitHub contribution calendar" style="display:inline-block;max-width:100%;width:auto;min-width:520px" src="https://ghchart.rshah.org/1e37a0/Akshaycyber006" />
      </div>
      <img class="activity-img" alt="contribution activity trend graph" src="https://github-readme-activity-graph.vercel.app/graph?username=Akshaycyber006&theme=blue-green&area=true&area_color=9db4f5&color=1e37a0&line=2a3eb1&point=1e37a0&bg_color=ffffff&hide_border=false&title=Contribution%20Activity&radius=16" />
      <p class="center muted" style="margin-top:10px"><i>Keep Coding! ♥</i></p>
    </div>
  </div>
</section>

<!-- ===================== LIVE REPOSITORIES ===================== -->
<section style="padding-top:0">
  <div class="wrap">
    <div class="sec-title">LATEST <span class="a">REPOSITORIES</span></div>
    <div id="repoList">
      <div class="center muted" style="padding:20px">loading live repositories…</div>
    </div>
  </div>
</section>

<!-- ===================== FOOTER ===================== -->
<div class="footer">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 80" width="900" height="80" role="img" aria-label="Code Today, Lead Tomorrow">
  <defs>
    <linearGradient id="ftr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#0f1a52"/><stop offset="0.5" stop-color="#1e37a0"/><stop offset="1" stop-color="#0f1a52"/>
    </linearGradient>
    <style><![CDATA[
      .cursor{animation:blink 1.05s infinite step-end}
      @keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
      .in{animation:fadein 1.4s ease-out both}
      @keyframes fadein{from{opacity:0}to{opacity:1}}
      .tw{animation:tw 2.4s infinite ease-in-out}
      .tw2{animation-delay:.6s}.tw3{animation-delay:1.2s}
      @keyframes tw{0%,100%{opacity:.3}50%{opacity:1}}
      @media (prefers-reduced-motion:reduce){*{animation:none!important}}
    ]]></style>
  </defs>
  <rect width="900" height="80" fill="url(#ftr)"/>
  <rect x="0" y="0" width="900" height="3" fill="#9db4f5"/>
  <rect x="0" y="77" width="900" height="3" fill="#9db4f5"/>
  <g fill="#ffffff">
    <rect class="tw" x="40" y="20" width="3" height="3"/><rect class="tw tw2" x="120" y="55" width="3" height="3"/>
    <rect class="tw tw3" x="780" y="22" width="3" height="3"/><rect class="tw tw2" x="860" y="55" width="3" height="3"/>
  </g>
  <g fill="#ffcc66">
    <rect class="tw tw2" x="80" y="50" width="3" height="3"/><rect class="tw tw3" x="820" y="28" width="3" height="3"/>
  </g>
  <text class="in" x="450" y="48" text-anchor="middle" fill="#ffffff" font-size="22" font-weight="700" font-family="'Courier New',monospace" letter-spacing="2">&lt; Code Today &#8226; Lead Tomorrow /&gt;<tspan class="cursor" fill="#ffcc66">&#9608;</tspan></text>
</svg>
<div class="foot-note">
  Built with ♥ by <b>Akshay Krishna</b> &nbsp;•&nbsp;
  <a href="https://github.com/Akshaycyber006" target="_blank" rel="noopener">github.com/Akshaycyber006</a><br/>
  <span class="muted" style="font-size:13px">Data fetched live from the GitHub REST API · cached 1 hour in your browser</span>
</div>
</div>

<button class="totop pixel" id="toTop" aria-label="back to top">↑ TOP</button>

<script>
/* ===================================================================
   LIVE DATA  —  GitHub public REST API (CORS-enabled, no token needed)
   Profile + repos → live stats, languages, repo list.
   1-hour localStorage cache; graceful fallback to static images.
=================================================================== */
(function(){
  "use strict";
  var USER = "Akshaycyber006";
  var CACHE_KEY = "akshay_gh_profile_v1";
  var CACHE_TTL  = 60 * 60 * 1000;          // 1 hour
  var API = "https://api.github.com";

  /* ---------- helpers ---------- */
  function $(id){ return document.getElementById(id); }
  function fmt(n){
    if(n >= 1000) return (n/1000).toFixed(n>=10000?0:1).replace(/\.0$/,"") + "k";
    return String(n);
  }
  function langColor(name){
    var map = {
      Python:"#3572A5", Java:"#b07219", C:"#555555", "C++":"#f34b7d",
      JavaScript:"#f1e05a", HTML:"#e34c26", CSS:"#563d7c", TypeScript:"#3178c6",
      Shell:"#89e051", PHP:"#4F5D95", Go:"#00ADD8", Rust:"#dea584",
      Ruby:"#701516", "Jupyter Notebook":"#DA5B0B", Dockerfile:"#384d54",
      Vue:"#41b883", Dart:"#00B4AB", Kotlin:"#A97BFF", Swift:"#F05138",
      Cuda:"#3A4E3A", SQL:null
    };
    return map[name] || "#2a3eb1";
  }

  /* ---------- fetch with cache ---------- */
  function readCache(){
    try{
      var raw = localStorage.getItem(CACHE_KEY);
      if(!raw) return null;
      var obj = JSON.parse(raw);
      if(Date.now() - obj.ts > CACHE_TTL) return null;
      return obj.data;
    }catch(e){ return null; }
  }
  function writeCache(data){
    try{ localStorage.setItem(CACHE_KEY, JSON.stringify({ts:Date.now(), data:data})); }catch(e){}
  }
  function staleCache(){
    try{
      var raw = localStorage.getItem(CACHE_KEY);
      if(!raw) return null;
      return JSON.parse(raw).data;
    }catch(e){ return null; }
  }

  async function gh(path){
    var res = await fetch(API + path, { headers:{ "Accept":"application/vnd.github+json", "User-Agent":"akshay-profile-site" } });
    if(!res.ok){
      if(res.status === 403 || res.status === 429){
        var err = new Error("rate-limited"); err.rateLimited = true; throw err;
      }
      throw new Error("http " + res.status);
    }
    return res.json();
  }

  async function loadAll(){
    var cached = readCache();
    if(cached) return { data:cached, fresh:true };

    try{
      var user  = await gh("/users/" + USER);
      var repos = await gh("/users/" + USER + "/repos?per_page=100&sort=updated");
      var data = { user:user, repos:repos||[], at:Date.now() };
      writeCache(data);
      return { data:data, fresh:true };
    }catch(e){
      var stale = staleCache();
      if(stale) return { data:stale, fresh:false };
      return { data:null, fresh:false, error:e };
    }
  }

  /* ---------- render: profile + stats ---------- */
  function renderProfile(d){
    var u = d.user;
    if(u){
      if(u.avatar_url && $("avatar")) $("avatar").src = u.avatar_url;
      if(u.bio) $("bioLine").textContent = u.bio;
      if(u.location) $("locLine").textContent = u.location;
    }
    var repos = d.repos || [];
    var stars = 0, forks = 0;
    repos.forEach(function(r){ stars += r.stargazers_count||0; forks += r.forks_count||0; });
    setNum("stRepos", u ? u.public_repos : repos.length);
    setNum("stStars", stars);
    setNum("stForks", forks);
    setNum("stFollowers", u ? u.followers : 0);
  }
  function setNum(id, n){
    var el = $(id);
    if(!el) return;
    var target = typeof n === "number" ? n : 0;
    // count-up animation
    var dur = 700, start = performance.now(), from = 0;
    function step(t){
      var p = Math.min(1, (t-start)/dur);
      var v = Math.floor(from + (target-from)*(1-Math.pow(1-p,3)));
      el.textContent = fmt(v);
      if(p < 1) requestAnimationFrame(step);
      else el.textContent = fmt(target);
    }
    requestAnimationFrame(step);
  }

  /* ---------- render: languages (live from repos) ---------- */
  function renderLanguages(d){
    var repos = d.repos || [];
    var counts = {};
    repos.forEach(function(r){
      if(r.language){ counts[r.language] = (counts[r.language]||0)+1; }
    });
    var arr = Object.keys(counts).map(function(k){ return {name:k, n:counts[k]}; });
    arr.sort(function(a,b){ return b.n - a.n; });
    var top = arr.slice(0, 6);
    var total = top.reduce(function(s,x){ return s+x.n; },0) || 1;
    var html = "";
    if(!top.length){
      html = '<p class="center muted" style="font-size:14px">No public language data yet — push some code!</p>';
    } else {
      top.forEach(function(x){
        var pct = Math.round(x.n/total*100);
        html += '<div class="lang-row">'
          + '<span class="lang-name"><span class="repo-lang-dot" style="background:'+langColor(x.name)+'"></span> '+escapeHtml(x.name)+'</span>'
          + '<span class="lang-bar"><span class="lang-fill" style="width:0%" data-w="'+pct+'"></span></span>'
          + '<span class="lang-pct">'+pct+'%</span>'
          + '</div>';
      });
    }
    $("langList").innerHTML = html;
    // animate bars
    setTimeout(function(){
      document.querySelectorAll(".lang-fill").forEach(function(el){
        el.style.width = el.getAttribute("data-w") + "%";
      });
    }, 80);
  }

  /* ---------- render: latest repos (live) ---------- */
  function renderRepos(d){
    var repos = (d.repos||[]).filter(function(r){ return !r.fork; }).slice(0, 6);
    if(!repos.length){
      $("repoList").innerHTML = '<div class="center muted" style="padding:20px">No public repositories yet — check back soon!</div>';
      return;
    }
    var html = "";
    repos.forEach(function(r){
      var desc = r.description ? escapeHtml(r.description) : '<span class="muted">— no description —</span>';
      var lang = r.language
        ? '<span class="dot"><span class="repo-lang-dot" style="background:'+langColor(r.language)+'"></span>'+escapeHtml(r.language)+'</span>'
        : "";
      html += '<a class="repo" href="'+r.html_url+'" target="_blank" rel="noopener">'
        + '<div class="repo-name">'+escapeHtml(r.name)+'</div>'
        + '<div class="repo-desc">'+desc+'</div>'
        + '<div class="repo-meta">'
        + lang
        + '<span class="dot">★ '+fmt(r.stargazers_count||0)+'</span>'
        + '<span class="dot">⑂ '+fmt(r.forks_count||0)+'</span>'
        + '<span class="dot">⤴ updated '+escapeHtml((r.updated_at||"").slice(0,10))+'</span>'
        + '</div></a>';
    });
    $("repoList").innerHTML = html;
  }

  function escapeHtml(s){
    return String(s).replace(/[&<>"']/g, function(c){
      return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];
    });
  }

  /* ---------- status pill ---------- */
  function setStatus(fresh, data, err){
    var el = $("statusPill");
    if(!el) return;
    if(data && fresh){
      var when = new Date(data.at||Date.now());
      el.className = "status-pill live";
      el.textContent = "● live · updated " + when.toLocaleString();
    } else if(data && !fresh){
      el.className = "status-pill offline";
      el.textContent = "● cached (API rate-limited)";
    } else if(err && err.rateLimited){
      el.className = "status-pill offline";
      el.textContent = "● API rate-limited · showing image fallbacks";
    } else {
      el.className = "status-pill offline";
      el.textContent = "● offline · showing image fallbacks";
    }
  }

  /* ---------- boot ---------- */
  loadAll().then(function(r){
    if(r.data){
      renderProfile(r.data);
      renderLanguages(r.data);
      renderRepos(r.data);
      setStatus(r.fresh, r.data, null);
    } else {
      setStatus(false, null, r.error);
      // hide skeletons but keep image fallbacks
      $("langList").innerHTML = '<p class="center muted" style="font-size:14px">Live data unavailable — stat images above still load from GitHub.</p>';
      $("repoList").innerHTML = '<div class="center muted" style="padding:20px">Live repos unavailable right now — visit <a href="https://github.com/Akshaycyber006?tab=repositories" target="_blank" rel="noopener">github.com/Akshaycyber006</a></div>';
    }
  }).catch(function(){
    setStatus(false, null, {});
  });

  /* ---------- back-to-top ---------- */
  var toTop = $("toTop");
  window.addEventListener("scroll", function(){
    if(window.scrollY > 600) toTop.classList.add("show");
    else toTop.classList.remove("show");
  });
  toTop.addEventListener("click", function(){ window.scrollTo({top:0, behavior:"smooth"}); });

  /* ---------- typewriter on hero tagline ---------- */
  (function(){
    var el = $("heroTag");
    if(!el) return;
    if(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var full = "< Build • Innovate • Contribute />";
    // keep the blinking cursor tspan; just retype the text portion
    // (the SVG already shows it statically — this adds a subtle retyping pulse once)
    // Skipped to avoid disturbing the SVG <tspan> cursor; the SVG's own blink stays.
  })();
})();
</script>
</body>
</html>
