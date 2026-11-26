<!DOCTYPE html>
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

/* ===== ROOM (all sizes in % / cqw so nothing drifts) ===== */
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
#projects{flex:1;min-height:0}
.project{display:none;animation:appear .7s}.project.active{display:block}
.project h2{color:#fff;font-size:max(11px,1.9cqw);margin-bottom:.4cqw;overflow-wrap:anywhere}
.project p{color:#b9cce0;margin-bottom:.6cqw;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.project li{margin:.5cqw 0;list-style:none}.project li::before{content:"> ";color:#ffe078}
.live{color:#9cb6d2;font-size:max(8px,.95cqw)}
@keyframes appear{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
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

/* ===== PROFILE ===== */
section{padding:clamp(24px,4vw,48px) 0}
.sec-title{font-family:'Press Start 2P',monospace;font-size:clamp(11px,1.7vw,16px);color:var(--blue);text-align:center;margin-bottom:24px}
.sec-title::before{content:"< "}.sec-title::after{content:" />"}
.grid{display:grid;gap:clamp(16px,2vw,26px);align-items:start;grid-template-columns:repeat(3,1fr)}
@media(max-width:1080px){.grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:700px){.grid{grid-template-columns:1fr}}
.card{background:#fff;border:4px solid var(--blue);box-shadow:8px 8px 0 var(--light);padding:clamp(16px,2vw,24px)}
.card h3{font-family:'Press Start 2P',monospace;font-size:clamp(10px,1.4vw,13px);color:var(--blue);text-align:center;margin-bottom:14px}
.card p{margin:6px 0}.center{text-align:center}.muted{color:var(--mid)}.b{font-weight:700;color:var(--deep)}
.about-head{display:flex;gap:14px;align-items:center;justify-content:center;margin-bottom:8px}
.avatar{width:64px;height:64px;border:3px solid var(--blue);box-shadow:4px 4px 0 var(--light);image-rendering:pixelated;background:var(--mist)}
.line{padding:3px 0}
hr{border:none;border-top:2px dashed var(--light);margin:12px 0}
.pill{display:inline-block;font-size:14px;padding:2px 8px;border:1px solid var(--blue);background:var(--mist);color:var(--blue)}
.pill.off{border-color:#c47a00;color:#c47a00}
.tech img{width:100%;max-width:340px;display:block;margin:0 auto}
.tags{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-top:10px}
.tags code{font-size:15px;background:var(--mist);color:var(--blue);padding:2px 7px;border:1px solid var(--light)}
.proj-name{font-family:'Press Start 2P',monospace;font-size:clamp(12px,1.6vw,15px);color:var(--blue);text-align:center}
.card ul{list-style:none;margin:10px 0}.card li{padding:4px 0;border-bottom:1px dashed var(--mist)}.card li:last-child{border:0}
.chk li::before{content:"[x] ";color:var(--blue);font-weight:700}
.btn{display:inline-block;font-family:'Press Start 2P',monospace;font-size:10px;background:var(--blue);color:#fff;padding:11px 16px;box-shadow:5px 5px 0 var(--deep)}
.btn:hover{transform:translate(3px,3px);box-shadow:2px 2px 0 var(--deep)}
.stats{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:12px}
.stat{background:var(--mist);border:2px solid var(--light);padding:8px 4px;text-align:center}
.stat b{font-family:'Press Start 2P',monospace;font-size:clamp(15px,2.2vw,20px);color:var(--blue);display:block}
.stat span{font-size:14px;color:var(--mid)}
.img{width:100%;display:block;border:2px solid var(--light);margin-top:10px}
.lang{display:flex;align-items:center;gap:8px;margin:6px 0;font-size:17px}
.lang .n{width:100px;flex-shrink:0}
.lang .bar{flex:1;height:14px;background:var(--mist);border:1px solid var(--light)}
.lang .bar i{display:block;height:100%;width:0;background:var(--blue);transition:width .8s}
.lang .p{width:42px;text-align:right;color:var(--mid)}
.dot{width:10px;height:10px;display:inline-block;border:1px solid var(--light)}
.badge{display:block;margin:6px auto;max-width:260px}.badge img{width:100%;display:block}
.repo{display:block;border:3px solid var(--blue);padding:12px 14px;margin-bottom:12px;box-shadow:5px 5px 0 var(--light)}
.repo:hover{transform:translate(-2px,-2px);box-shadow:7px 7px 0 var(--mid)}
.repo-name{font-family:'Press Start 2P',monospace;font-size:11px;color:var(--blue);margin-bottom:6px;overflow-wrap:anywhere}
.repo-meta{display:flex;flex-wrap:wrap;gap:12px;font-size:15px;color:var(--mid)}
.footer{background:var(--deep);color:var(--light);text-align:center;padding:26px 12px;font-size:16px}
.footer a{color:var(--gold)}.footer .px{color:#fff;font-size:clamp(10px,1.6vw,14px);margin-bottom:10px}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>

<!-- ===== 1. PIXEL ROOM (top) ===== -->
<div class="stage">
 <div class="room" role="img" aria-label="Pixel room with a monitor showing Akshay's GitHub projects">
  <div class="window"><div class="sun"></div></div>
  <div class="poster">DREAM<br>CODE<br>DEPLOY<br>♥</div>
  <div class="clock"></div>
  <div class="shelf"><div class="book"></div><div class="book"></div><div class="book"></div><div class="book"></div></div>
  <div class="plant"></div>
  <div class="monitor"><div class="screen">
   <h3>akshaycyber006@github: ~/projects</h3>
   <div id="projects">
    <div class="project active"><h2>QRVerse</h2><p>Smart QR &amp; File Sharing Platform</p>
     <ul><li>QR Generation</li><li>Offline File Bridge</li><li>Supabase Integration</li></ul></div>
   </div>
   <div class="live" id="roomLive">akshaycyber006@github_</div>
  </div></div>
  <div class="stand"></div><div class="desk"></div><div class="cat"></div><div class="floor"></div>
  <div class="caption">AKSHAY KRISHNA // BUILT WITH CURIOSITY</div>
 </div>
</div>

<!-- ===== 2. ABOUT / TECH / FEATURED ===== -->
<section><div class="wrap"><div class="grid">
 <div class="card">
  <h3>ABOUT ME</h3>
  <div class="about-head">
   <img id="avatar" class="avatar" alt="avatar" src="https://avatars.githubusercontent.com/Akshaycyber006">
   <div><div class="b px" style="font-size:11px">AKSHAY KRISHNA</div><div class="muted" id="bioLine">IT Student &amp; Developer</div></div>
  </div>
  <p class="center">Hi! I'm <span class="b">Akshay Krishna</span> 👋<br>Passionate about <span class="b">Software Development</span>, <span class="b">AI</span> and <span class="b">Cybersecurity</span>.<br>Always learning, always building! 🚀</p>
  <hr>
  <div class="line">🎓 <b>B.Tech IT</b></div>
  <div class="line">📍 <b id="locLine">Chennai, India</b></div>
  <div class="line">🎯 <b>Goal:</b> 12+ LPA</div>
  <div class="line">♥ <b>Dream:</b> Make an Impact</div>
  <hr>
  <div class="center"><span id="statusPill" class="pill off">loading live data…</span></div>
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

<!-- ===== 3. STATS / LANGUAGES / CONNECT ===== -->
<section style="padding-top:0"><div class="wrap"><div class="grid">
 <div class="card">
  <h3>GITHUB STATS</h3>
  <div class="stats">
   <div class="stat"><b id="stRepos">—</b><span>Repos</span></div>
   <div class="stat"><b id="stStars">—</b><span>Stars</span></div>
   <div class="stat"><b id="stForks">—</b><span>Forks</span></div>
   <div class="stat"><b id="stFollowers">—</b><span>Followers</span></div>
  </div>
  <img class="img" alt="GitHub streak" src="https://streak-stats.demolab.com/?user=Akshaycyber006&ring_color=1e37a0&fire_color=ffcc66&currStreakNum=1e37a0&sideNums=2a3eb1&currStreakLabel=1e37a0&sideLabels=1e37a0&dates=2a3eb1&bg_color=ffffff&border_color=2a3eb1">
 </div>
 <div class="card">
  <h3>TOP LANGUAGES</h3>
  <div id="langList"><p class="center muted">loading…</p></div>
  <p class="center muted" style="font-size:15px;margin-top:8px">across public repositories (live)</p>
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

<!-- ===== 4. CONTRIBUTIONS ===== -->
<section style="padding-top:0"><div class="wrap">
 <div class="sec-title">CONTRIBUTION ACTIVITY</div>
 <div class="card center" style="overflow-x:auto">
  <img alt="GitHub contribution calendar" style="min-width:520px;max-width:100%" src="https://ghchart.rshah.org/1e37a0/Akshaycyber006">
  <p class="muted" style="margin-top:8px"><i>Keep Coding! ♥</i></p>
 </div>
</div></section>

<!-- ===== 5. REPOS ===== -->
<section style="padding-top:0"><div class="wrap">
 <div class="sec-title">LATEST REPOSITORIES</div>
 <div id="repoList"><p class="center muted">loading live repositories…</p></div>
</div></section>

<div class="footer">
 <div class="px">&lt; Code Today • Lead Tomorrow /&gt;</div>
 Built with ♥ by <b>Akshay Krishna</b> • <a href="https://github.com/Akshaycyber006" target="_blank" rel="noopener">github.com/Akshaycyber006</a><br>
 Data fetched live from the GitHub API · refreshes every 5 minutes
</div>

<script>
(function(){
"use strict";
var USER="Akshaycyber006",KEY="akshay_gh_v2",TTL=5*60*1000,API="https://api.github.com";
var $=function(i){return document.getElementById(i)};
var esc=function(s){return String(s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})};
var fmt=function(n){return n>=1000?(n/1000).toFixed(1).replace(".0","")+"k":String(n)};
var COL={Python:"#3572A5",Java:"#b07219",C:"#555",
"C++":"#f34b7d",JavaScript:"#f1e05a",HTML:"#e34c26",CSS:"#563d7c",TypeScript:"#3178c6",Shell:"#89e051","Jupyter Notebook":"#DA5B0B"};
var col=function(n){return COL[n]||"#2a3eb1"};

function cache(fresh){try{var o=JSON.parse(localStorage.getItem(KEY));if(!o)return null;if(fresh&&Date.now()-o.ts>TTL)return null;return o.data}catch(e){return null}}
async function gh(p){var r=await fetch(API+p,{headers:{Accept:"application/vnd.github+json"}});if(!r.ok)throw new Error(r.status);return r.json()}
async function load(force){
 var c=!force&&cache(true);if(c)return{data:c,fresh:true};
 try{
  var u=await gh("/users/"+USER),r=await gh("/users/"+USER+"/repos?per_page=100&sort=updated");
  var d={user:u,repos:r,at:Date.now()};
  try{localStorage.setItem(KEY,JSON.stringify({ts:Date.now(),data:d}))}catch(e){}
  return{data:d,fresh:true};
 }catch(e){var s=cache(false);return s?{data:s,fresh:false}:{data:null}}
}

/* count-up number */
function num(id,n){var el=$(id),t=+n||0,s=performance.now();
 (function st(x){var p=Math.min(1,(x-s)/700);el.textContent=fmt(Math.floor(t*(1-Math.pow(1-p,3))));if(p<1)requestAnimationFrame(st);else el.textContent=fmt(t)})(s)}

/* ---- monitor in the room: real repos ---- */
var cur=0,timer=null;
function renderRoom(d){
 var repos=(d.repos||[]).filter(function(r){return !r.fork});
 repos.sort(function(a,b){return (b.name==="QRVerse")-(a.name==="QRVerse")}); // QRVerse first
 repos=repos.slice(0,5);if(!repos.length)return;
 $("projects").innerHTML=repos.map(function(r,i){
  return '<div class="project'+(i?'':' active')+'"><h2>'+esc(r.name)+'</h2><p>'+esc(r.description||"GitHub project")+'</p><ul><li>Language: '+esc(r.language||"Multiple")+'</li><li>Stars: '+r.stargazers_count+'</li><li>Forks: '+r.forks_count+'</li></ul></div>'}).join("");
 $("roomLive").textContent="akshaycyber006@github_ ● live";
 cur=0;clearInterval(timer);
 timer=setInterval(function(){var p=document.querySelectorAll(".project");if(p.length<2)return;
  p[cur].classList.remove("active");cur=(cur+1)%p.length;p[cur].classList.add("active")},4000);
}

function renderProfile(d){
 var u=d.user||{},repos=d.repos||[],st=0,fk=0;
 if(u.avatar_url)$("avatar").src=u.avatar_url;
 if(u.bio)$("bioLine").textContent=u.bio;
 if(u.location)$("locLine").textContent=u.location;
 repos.forEach(function(r){st+=r.stargazers_count||0;fk+=r.forks_count||0});
 num("stRepos",u.public_repos!=null?u.public_repos:repos.length);num("stStars",st);num("stForks",fk);num("stFollowers",u.followers);
}
function renderLangs(d){
 var c={};(d.repos||[]).forEach(function(r){if(r.language)c[r.language]=(c[r.language]||0)+1});
 var a=Object.keys(c).map(function(k){return{n:k,v:c[k]}}).sort(function(x,y){return y.v-x.v}).slice(0,6);
 var tot=a.reduce(function(s,x){return s+x.v},0)||1;
 $("langList").innerHTML=a.length?a.map(function(x){var p=Math.round(x.v/tot*100);
  return '<div class="lang"><span class="n"><span class="dot" style="background:'+col(x.n)+'"></span> '+esc(x.n)+'</span><span class="bar"><i data-w="'+p+'"></i></span><span class="p">'+p+'%</span></div>'}).join(""):'<p class="center muted">No language data yet.</p>';
 setTimeout(function(){document.querySelectorAll(".bar i").forEach(function(e){e.style.width=e.dataset.w+"%"})},80);
}
function renderRepos(d){
 var r=(d.repos||[]).filter(function(x){return !x.fork}).slice(0,6);
 $("repoList").innerHTML=r.length?r.map(function(x){
  return '<a class="repo" href="'+x.html_url+'" target="_blank" rel="noopener"><div class="repo-name">'+esc(x.name)+'</div><div>'+(x.description?esc(x.description):'<span class="muted">— no description —</span>')+'</div><div class="repo-meta">'+
  (x.language?'<span><span class="dot" style="background:'+col(x.language)+'"></span> '+esc(x.language)+'</span>':'')+'<span>★ '+x.stargazers_count+'</span><span>⑂ '+x.forks_count+'</span><span>updated '+esc((x.updated_at||"").slice(0,10))+'</span></div></a>'}).join(""):'<p class="center muted">No public repositories yet.</p>';
}
function status(r){
 var el=$("statusPill");
 if(r.data&&r.fresh){el.className="pill";el.textContent="● live · "+new Date(r.data.at).toLocaleTimeString()}
 else if(r.data){el.className="pill off";el.textContent="● cached (API limit reached)"}
 else{el.className="pill off";el.textContent="● offline · live data unavailable"}
}
function boot(force){
 load(force).then(function(r){
  status(r);
  if(r.data){renderRoom(r.data);renderProfile(r.data);renderLangs(r.data);renderRepos(r.data)}
  else{$("langList").innerHTML='<p class="center muted">Live data unavailable right now.</p>';
   $("repoList").innerHTML='<p class="center muted">See <a href="https://github.com/Akshaycyber006?tab=repositories">github.com/Akshaycyber006</a></p>'}
 });
}
boot(false);
setInterval(function(){boot(true)},TTL); // real-time refresh
})();
</script>
</body>
</html>
