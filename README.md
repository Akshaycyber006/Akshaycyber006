
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Akshay Krishna — Developer / B.Tech IT</title>
<meta name="description" content="Akshay Krishna — IT student & developer. Software development, AI, cybersecurity. Chennai, India.">
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap" rel="stylesheet">
<style>
:root{--ink:#0f1a52;--deep:#0a1340;--blue:#1e37a0;--mid:#2a3eb1;--light:#9db4f5;--mist:#eef0ff;--gold:#ffcc66}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'VT323','Courier New',monospace;font-size:clamp(17px,1.2vw,21px);background:#fff;color:var(--ink);line-height:1.4}
a{color:var(--blue);text-decoration:none}
.px{font-family:'Press Start 2P',monospace}
.wrap{max-width:1120px;margin:0 auto;padding:0 clamp(12px,3vw,28px)}

/* ================= PIXEL ROOM ================= */
.stage{background:#111827;padding:clamp(10px,2vw,24px) 0}
.room{container-type:inline-size;position:relative;width:min(96%,1100px);margin:0 auto;aspect-ratio:11/5;
 background:#1b2030;overflow:hidden;border-radius:12px;border-bottom:1.2cqw solid #382820;font-family:monospace}
.room>*{position:absolute}
.window{left:4%;top:12%;width:22%;height:42%;background:#77c4f5;border:.7cqw solid #101827;box-shadow:0 .7cqw #69452f}
.window::before,.window::after{content:"";position:absolute;background:#101827}
.window::before{left:50%;top:0;width:.7cqw;height:100%}
.window::after{top:50%;left:0;height:.7cqw;width:100%}
.sun{right:15%;top:15%;width:18%;height:20%;background:#ffdc55}
.clock{left:48%;top:5%;width:5.4cqw;height:5.4cqw;border-radius:50%;background:#f4e8ce;border:.6cqw solid #101827}
.poster{left:30%;top:10%;background:#f4e8ce;color:#071b75;padding:1.2cqw 1.5cqw;font-weight:bold;font-size:1.3cqw;transform:rotate(-2deg);line-height:1.5}
.shelf{right:4%;top:36%;width:20%;height:1.1cqw;background:#69452f}
.book{bottom:1.1cqw;width:1.7cqw;height:5cqw;background:#3178bd;position:absolute}
.book:nth-child(1){left:12%}.book:nth-child(2){left:32%;height:6.4cqw;background:#e74c35}
.book:nth-child(3){left:52%;background:#753e9c}.book:nth-child(4){left:72%;height:5.8cqw;background:#e6d64f}
.monitor{left:33%;top:24%;width:34%;height:47%;background:#394354;padding:.8cqw;box-shadow:0 .8cqw #101827}
.screen{height:100%;background:#07182c;color:#65dc91;padding:1.2cqw;overflow:hidden;font-size:max(9px,1.25cqw);display:flex;flex-direction:column}
.screen h3{color:#ffe078;font-size:max(8px,1.1cqw);border-bottom:1px solid #52617b;padding-bottom:.6cqw;margin-bottom:1cqw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#projects{flex:1;min-height:0;position:relative}
.project{position:absolute;inset:0;opacity:0;animation:show 16s infinite}
.project:nth-child(2){animation-delay:4s}.project:nth-child(3){animation-delay:8s}.project:nth-child(4){animation-delay:12s}
@keyframes show{0%{opacity:0;transform:translateY(8px)}2%,23%{opacity:1;transform:none}25%,100%{opacity:0}}
.project h2{color:#fff;font-size:max(11px,1.9cqw);margin-bottom:.4cqw;overflow-wrap:anywhere}
.project p{color:#b9cce0;margin-bottom:.6cqw}
.project li{margin:.5cqw 0;list-style:none}.project li::before{content:"> ";color:#ffe078}
.live{color:#9cb6d2;font-size:max(8px,.95cqw)}
.live::after{content:"_";animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.stand{left:48.5%;top:71%;width:3%;height:13%;background:#394354}
.desk{left:3%;bottom:13%;width:94%;height:3cqw;max-height:15px;background:#69452f}
.plant{left:12%;bottom:calc(13% + 3cqw);width:5cqw;height:4cqw;background:#985b37}
.plant::before{content:"";position:absolute;left:2cqw;bottom:100%;width:.8cqw;height:6cqw;background:#26944e}
.plant::after{content:"";position:absolute;left:-.5cqw;bottom:calc(100% + 4.5cqw);width:6cqw;height:3.5cqw;background:#26944e;
 clip-path:polygon(0 40%,30% 40%,30% 0,60% 0,60% 35%,100% 35%,100% 65%,60% 65%,60% 100%,30% 100%,30% 65%,0 65%)}
.cat{right:10%;bottom:calc(13% + 3cqw);width:8cqw;height:3cqw;background:#dda052;animation:nap 3s infinite;
 clip-path:polygon(0 50%,20% 40%,25% 0,40% 0,45% 40%,75% 40%,80% 0,95% 0,95% 40%,100% 50%,100% 100%,0 100%)}
@keyframes nap{50%{transform:translateY(-4px)}}
.floor{left:0;bottom:0;width:100%;height:13%;background:repeating-linear-gradient(#453027 0 8px,#35251e 8px 15px)}
.caption{left:3%;bottom:3%;color:#b8c8df;font-size:max(9px,1.1cqw)}
@media(max-width:640px){
 .room{aspect-ratio:4/5}
 .window{left:5%;top:5%;width:34%;height:22%}
 .poster{left:46%;top:6%;font-size:3cqw;padding:2.5cqw}
 .clock{left:auto;right:6%;top:30%;width:11cqw;height:11cqw}
 .shelf{right:5%;top:25%;width:36%;height:2cqw}.book{width:3.5cqw;height:10cqw}
 .book:nth-child(2){height:13cqw}.book:nth-child(4){height:11cqw}
 .monitor{left:5%;top:36%;width:90%;height:36%;padding:2cqw}
 .screen{padding:3cqw;font-size:max(11px,3.4cqw)}.screen h3{font-size:max(9px,2.6cqw)}
 .project h2{font-size:max(14px,5cqw)}.live{font-size:max(9px,2.4cqw)}
 .stand{top:72%;height:8%}.desk{height:3%}
 .plant{left:5%;width:9cqw;height:7cqw}.plant::before{left:3.6cqw;width:1.6cqw;height:10cqw}
 .plant::after{left:-1cqw;width:11cqw;height:6cqw;bottom:calc(100% + 7cqw)}
 .cat{width:16cqw;height:6cqw;right:6%}.caption{font-size:max(9px,2.6cqw)}
}

/* ================= PROFILE ================= */
section{padding:clamp(24px,4vw,48px) 0}
.sec-title{font-family:'Press Start 2P',monospace;font-size:clamp(11px,1.7vw,16px);color:var(--blue);text-align:center;margin-bottom:24px}
.sec-title::before{content:"< "}.sec-title::after{content:" />"}
.grid{display:grid;gap:clamp(16px,2vw,26px);align-items:start;grid-template-columns:repeat(3,1fr)}
@media(max-width:1080px){.grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:700px){.grid{grid-template-columns:1fr}}
.card{background:#fff;border:4px solid var(--blue);box-shadow:8px 8px 0 var(--light);padding:clamp(16px,2vw,24px);transition:transform .15s,box-shadow .15s}
.card:hover{transform:translate(-3px,-3px);box-shadow:11px 11px 0 var(--mid)}
.card h3{font-family:'Press Start 2P',monospace;font-size:clamp(10px,1.4vw,13px);color:var(--blue);text-align:center;margin-bottom:14px}
.card p{margin:6px 0}.center{text-align:center}.muted{color:var(--mid)}.b{font-weight:700;color:var(--deep)}
.about-head{display:flex;gap:14px;align-items:center;justify-content:center;margin-bottom:8px}
.avatar{width:64px;height:64px;border:3px solid var(--blue);box-shadow:4px 4px 0 var(--light);image-rendering:pixelated}
.line{padding:3px 0}
hr{border:none;border-top:2px dashed var(--light);margin:12px 0}
.tech img{width:100%;max-width:340px;display:block;margin:0 auto}
.tags{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-top:10px}
.tags code{font-size:15px;background:var(--mist);color:var(--blue);padding:2px 7px;border:1px solid var(--light)}
.proj-name{font-family:'Press Start 2P',monospace;font-size:clamp(12px,1.6vw,15px);color:var(--blue);text-align:center}
.card ul{list-style:none;margin:10px 0}.card li{padding:4px 0;border-bottom:1px dashed var(--mist)}.card li:last-child{border:0}
.chk li::before{content:"[x] ";color:var(--blue);font-weight:700}
.btn{display:inline-block;font-family:'Press Start 2P',monospace;font-size:10px;background:var(--blue);color:#fff;padding:11px 16px;box-shadow:5px 5px 0 var(--deep);transition:transform .1s,box-shadow .1s}
.btn:hover{transform:translate(3px,3px);box-shadow:2px 2px 0 var(--deep)}
.img{width:100%;display:block;margin-top:10px}
.badge{display:block;margin:6px auto;max-width:260px}.badge img{width:100%;display:block}
.pins{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;justify-items:center}
.pins img{max-width:100%}
.footer{background:var(--deep);color:var(--light);text-align:center;padding:26px 12px;font-size:16px}
.footer a{color:var(--gold)}.footer .px{color:#fff;font-size:clamp(10px,1.6vw,14px);margin-bottom:10px}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.project:first-child{opacity:1}}
</style>
</head>
<body>

<!-- ============ 1. PIXEL ROOM ============ -->
<div class="stage">
 <div class="room" role="img" aria-label="Pixel room with a monitor showing Akshay's projects">
  <div class="window"><div class="sun"></div></div>
  <div class="poster">DREAM<br>CODE<br>DEPLOY<br>♥</div>
  <div class="clock"></div>
  <div class="shelf"><div class="book"></div><div class="book"></div><div class="book"></div><div class="book"></div></div>
  <div class="plant"></div>
  <div class="monitor"><div class="screen">
   <h3>akshaycyber006@github: ~/projects</h3>
   <div id="projects">
    <div class="project"><h2>QRVerse</h2><p>Smart QR &amp; File Sharing</p>
     <ul><li>QR Generation</li><li>Offline File Bridge</li><li>Supabase Integration</li></ul></div>
    <div class="project"><h2>CAMHealth</h2><p>Camera Health Research</p>
     <ul><li>Lens Degradation</li><li>Image Quality</li><li>Perception Risk</li></ul></div>
    <div class="project"><h2>Water Purification</h2><p>Smart Tank System</p>
     <ul><li>Multi-stage Filtration</li><li>UV Treatment</li><li>Overflow Sensor</li></ul></div>
    <div class="project"><h2>Code Similarity</h2><p>ML-based Detection</p>
     <ul><li>AST Comparison</li><li>CFG Analysis</li><li>Code Classification</li></ul></div>
   </div>
   <div class="live">akshaycyber006@github</div>
  </div></div>
  <div class="stand"></div><div class="desk"></div><div class="cat"></div><div class="floor"></div>
  <div class="caption">AKSHAY KRISHNA // BUILT WITH CURIOSITY</div>
 </div>
</div>

<!-- ============ 2. ABOUT / TECH / FEATURED ============ -->
<section><div class="wrap"><div class="grid">
 <div class="card">
  <h3>ABOUT ME</h3>
  <div class="about-head">
   <img class="avatar" alt="avatar" src="https://avatars.githubusercontent.com/Akshaycyber006">
   <div><div class="b px" style="font-size:11px">AKSHAY KRISHNA</div><div class="muted">IT Student &amp; Developer</div></div>
  </div>
  <p class="center">Hi! I'm <span class="b">Akshay Krishna</span> 👋<br>Passionate about <span class="b">Software Development</span>, <span class="b">AI</span> and <span class="b">Cybersecurity</span>.<br>Always learning, always building! 🚀</p>
  <hr>
  <div class="line">🎓 <b>B.Tech IT</b></div>
  <div class="line">📍 <b>Chennai, India</b></div>
  <div class="line">🎯 <b>Goal:</b> 12+ LPA</div>
  <div class="line">♥ <b>Dream:</b> Make an Impact</div>
 </div>

 <div class="card tech">
  <h3>TECH STACK</h3>
  <img src="https://skillicons.dev/icons?i=c,cpp,python,java,html,css,js,mysql,linux,git,github,vscode&theme=light&perline=6" alt="tech stack icons">
  <div class="tags"><code>C</code><code>C++</code><code>Python</code><code>Java</code><code>HTML5</code><code>CSS3</code><code>JavaScript</code><code>SQL</code><code>Linux</code><code>Git</code><code>GitHub</code><code>VS Code</code></div>
 </div>

 <div class="card">
  <h3>FEATURED PROJECT</h3>
  <div class="proj-name">⚡ QRVerse</div>
  <p class="center muted"><i>Smart QR &amp; File Sharing Platform</i></p>
  <ul class="chk"><li>Smart QR Generation &amp; Scanning</li><li>Offline File Bridge</li><li>AI OCR &amp; Translation</li><li>Supabase Integration</li></ul>
  <p class="center" style="margin-top:10px"><a class="btn" href="https://github.com/Akshaycyber006/QRVerse" target="_blank" rel="noopener">View Project →</a></p>
 </div>
</div></div></section>

<!-- ============ 3. LIVE STATS / LANGUAGES / CONNECT ============ -->
<section style="padding-top:0"><div class="wrap"><div class="grid">
 <div class="card">
  <h3>GITHUB STATS</h3>
  <img class="img" style="margin-top:0" alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username=Akshaycyber006&show_icons=true&include_all_commits=true&count_private=true&title_color=1e37a0&text_color=2a3eb1&icon_color=1e37a0&bg_color=ffffff&border_color=2a3eb1">
  <img class="img" alt="GitHub streak" src="https://streak-stats.demolab.com/?user=Akshaycyber006&ring_color=1e37a0&fire_color=ffcc66&currStreakNum=1e37a0&sideNums=2a3eb1&currStreakLabel=1e37a0&sideLabels=1e37a0&dates=2a3eb1&bg_color=ffffff&border_color=2a3eb1">
 </div>
 <div class="card">
  <h3>TOP LANGUAGES</h3>
  <img class="img" style="margin-top:0" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Akshaycyber006&layout=compact&langs_count=8&title_color=1e37a0&text_color=2a3eb1&bg_color=ffffff&border_color=2a3eb1">
  <p class="center muted" style="font-size:15px">across public repositories (live)</p>
 </div>
 <div class="card">
  <h3>LET'S CONNECT</h3>
  <a class="badge" href="https://github.com/Akshaycyber006" target="_blank" rel="noopener"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-Akshaycyber006-2a3eb1?style=for-the-badge&logo=github&logoColor=white"></a>
  <a class="badge" href="https://www.linkedin.com/in/akshaykrishna-s-a95370315" target="_blank" rel="noopener"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Akshay%20Krishna-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
  <a class="badge" href="mailto:akshaykrishna1225@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-akshaykrishna1225@gmail.com-1e37a0?style=for-the-badge&logo=gmail&logoColor=white"></a>
  <hr>
  <div class="center"><img alt="profile views" src="https://komarev.com/ghpvc/?username=Akshaycyber006&label=Profile%20Views&color=1e37a0&style=for-the-badge&abbreviated=true"></div>
 </div>
</div></div></section>

<!-- ============ 4. CONTRIBUTIONS ============ -->
<section style="padding-top:0"><div class="wrap">
 <div class="sec-title">CONTRIBUTION ACTIVITY</div>
 <div class="card center" style="overflow-x:auto">
  <img alt="GitHub contribution calendar" style="min-width:520px;max-width:100%" src="https://ghchart.rshah.org/1e37a0/Akshaycyber006">
  <p class="muted" style="margin-top:8px"><i>Keep Coding! ♥</i></p>
 </div>
</div></section>

<!-- ============ 5. REPOSITORIES (live pin cards) ============ -->
<section style="padding-top:0"><div class="wrap">
 <div class="sec-title">REPOSITORIES</div>
 <div class="pins">
  <a href="https://github.com/Akshaycyber006/QRVerse"><img alt="QRVerse" src="https://github-readme-stats.vercel.app/api/pin/?username=Akshaycyber006&repo=QRVerse&title_color=1e37a0&text_color=2a3eb1&icon_color=1e37a0&bg_color=ffffff&border_color=2a3eb1"></a>
  <a href="https://github.com/Akshaycyber006/sql-learning-journey"><img alt="sql-learning-journey" src="https://github-readme-stats.vercel.app/api/pin/?username=Akshaycyber006&repo=sql-learning-journey&title_color=1e37a0&text_color=2a3eb1&icon_color=1e37a0&bg_color=ffffff&border_color=2a3eb1"></a>
  <a href="https://github.com/Akshaycyber006/Ink-Escape-Notebook-Adventure"><img alt="Ink-Escape-Notebook-Adventure" src="https://github-readme-stats.vercel.app/api/pin/?username=Akshaycyber006&repo=Ink-Escape-Notebook-Adventure&title_color=1e37a0&text_color=2a3eb1&icon_color=1e37a0&bg_color=ffffff&border_color=2a3eb1"></a>
 </div>
</div></section>

<div class="footer">
 <div class="px">&lt; Code Today • Lead Tomorrow /&gt;</div>
 Built with ♥ by <b>Akshay Krishna</b> • <a href="https://github.com/Akshaycyber006" target="_blank" rel="noopener">github.com/Akshaycyber006</a>
</div>

</body>
</html>
