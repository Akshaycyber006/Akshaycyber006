<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Akshay Krishna — Pixel Developer Portfolio</title>
<style>
:root{--blue:#071b75;--blue2:#1238a5;--pale:#dce7ff;--white:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--blue);color:var(--blue);font-family:ui-monospace,Consolas,monospace}
main{max-width:1500px;margin:auto;padding:14px}
section{position:relative;margin:0 auto 12px;line-height:0}
.art{display:block;width:100%;height:auto;image-rendering:pixelated}
.hero{margin-bottom:10px}
.grid{display:grid;grid-template-columns:1fr 1fr 1.55fr;gap:10px}
.lower{display:grid;grid-template-columns:1fr 1fr 1.12fr;gap:10px}
.panel{position:relative;overflow:hidden}
.panel img{display:block;width:100%;height:100%;object-fit:fill;image-rendering:pixelated}
.feature{position:relative}
.qr-cover{position:absolute;right:5.4%;top:23%;width:20%;aspect-ratio:1;background:#fff;padding:5px;image-rendering:pixelated}
.qr-cover img{width:100%;height:100%;object-fit:contain;image-rendering:pixelated}
.qr-label{position:absolute;right:5%;top:77%;font-size:clamp(8px,1vw,14px);font-weight:bold;background:#fff;padding:2px 5px}
.contrib{position:relative;background:#fff;border:5px solid var(--blue);min-height:164px;overflow:hidden}
.contrib-head{height:37px;background:var(--blue);color:white;font-weight:bold;padding:7px 12px;font-size:clamp(12px,1.5vw,20px);line-height:22px}
.graph-wrap{padding:10px 12px 5px}
#heatmap{display:grid;grid-auto-flow:column;grid-template-rows:repeat(7,1fr);grid-auto-columns:1fr;gap:4px;height:75px}
.cell{background:#e8efff;border:1px solid #7c9ce8;opacity:.25;transform:scale(.8);transition:opacity .3s,transform .3s,background .3s}
.cell.active{opacity:1;transform:scale(1);background:var(--blue)}
.cell.level1{background:#a9bfff}.cell.level2{background:#6e8ee8}.cell.level3{background:#3158c5}.cell.level4{background:#071b75}
.graph-foot{text-align:center;font-weight:bold;font-size:12px;padding:3px}
.controls{display:flex;justify-content:center;gap:8px;align-items:center;color:white;flex-wrap:wrap;padding:8px}
button{background:white;color:var(--blue);border:2px solid white;padding:7px 12px;font: bold 12px ui-monospace,monospace;cursor:pointer}
button:hover{background:var(--pale)}
#status{font-size:11px}
.footer img{width:100%;display:block;image-rendering:pixelated}
@media(max-width:760px){main{padding:6px}.grid{grid-template-columns:1fr 1fr}.feature{grid-column:1/-1}.lower{grid-template-columns:1fr}.contrib{min-height:160px}.qr-cover{width:18%}}
</style>
</head>
<body>
<main>
  <section class="hero"><img class="art" src="assets/hero.png" alt="Pixel art developer desk hero"></section>
  <div class="grid">
    <section class="panel"><img src="assets/about.png" alt="About me panel"></section>
    <section class="panel"><img src="assets/tech-stack.png" alt="Tech stack panel"></section>
    <section class="panel feature">
      <img src="assets/featured-project.png" alt="QRVerse featured project panel">
      <a class="qr-cover" href="https://github.com/Akshaycyber006/QRVerse" target="_blank" rel="noopener" title="Open QRVerse repository"><img src="assets/qrverse-real-qr.png" alt="Real QR code linking to QRVerse repository"></a>
      <span class="qr-label">SCAN TO OPEN</span>
    </section>
  </div>
  <div class="lower">
    <section class="panel"><img src="assets/github-stats.png" alt="GitHub stats artwork"></section>
    <section class="contrib">
      <div class="contrib-head">▦ Contribution Activity — LIVE</div>
      <div class="graph-wrap"><div id="heatmap" aria-label="Animated GitHub contribution calendar"></div></div>
      <div class="graph-foot" id="count">Loading contribution history…</div>
    </section>
    <section class="panel"><img src="assets/connect.png" alt="Connect panel"></section>
  </div>
  <div class="controls">
    <button id="play">▶ PLAY</button><button id="pause">Ⅱ PAUSE</button><button id="replay">↻ REPLAY</button>
    <span id="status">Fetching public contribution history for @Akshaycyber006…</span>
  </div>
  <section class="footer"><img src="assets/footer.png" alt="Code today, lead tomorrow"></section>
</main>
<script>
const USER="Akshaycyber006";
const heat=document.getElementById("heatmap");
const count=document.getElementById("count");
const statusEl=document.getElementById("status");
let cells=[],timer=null,index=0;
function fallback(){
  // Visual fallback only; live history will replace this when the GitHub endpoint responds.
  const now=new Date();
  const start=new Date(now); start.setDate(now.getDate()-363);
  start.setDate(start.getDate()-start.getDay());
  const data=[];
  for(let i=0;i<371;i++) data.push({date:new Date(start.getTime()+i*86400000).toISOString().slice(0,10),count:0,level:0});
  return data;
}
function render(data){
  heat.innerHTML=""; cells=[];
  data.forEach((d,i)=>{
    const el=document.createElement("div");
    el.className="cell";
    el.title=`${d.date}: ${d.count} contributions`;
    el.dataset.level=String(d.level||0);
    heat.appendChild(el); cells.push(el);
  });
  count.textContent=`${data.reduce((s,d)=>s+(d.count||0),0)} contributions in displayed period`;
  index=0;
}
function stop(){if(timer){clearInterval(timer);timer=null;}}
function play(){
  stop();
  timer=setInterval(()=>{
    if(index>=cells.length){stop();statusEl.textContent="Animation complete — press REPLAY to watch again.";return;}
    const el=cells[index++];
    el.classList.add("active");
    const level=Number(el.dataset.level);
    if(level) el.classList.add("level"+level);
    statusEl.textContent=`Revealing contribution day ${index} / ${cells.length}`;
  },18);
}
async function load(){
  try{
    const r=await fetch("/api/contributions");
    if(!r.ok) throw new Error("Could not fetch GitHub contribution data");
    const data=await r.json();
    render(data.days);
    count.textContent=`${data.total} contributions in the last year`;
    statusEl.textContent=`Live public history loaded for @${USER}`;
  }catch(e){
    render(fallback());
    statusEl.textContent="Live data unavailable. Showing an empty calendar; check internet and try refresh.";
    count.textContent="Live contribution data not loaded";
  }
  play();
}
document.getElementById("play").onclick=play;
document.getElementById("pause").onclick=()=>{stop();statusEl.textContent="Animation paused.";};
document.getElementById("replay").onclick=()=>{cells.forEach(c=>c.className="cell");index=0;play();};
load();
</script>
</body>
</html>
