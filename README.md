
<!DOCTYPE html>
<html>
<head>
<title>Akshay's Pixel Room</title>
<style>
*{box-sizing:border-box}
body{
 margin:0;background:#111827;
 display:grid;place-items:center;
 min-height:100vh;font-family:monospace;
}
.room{
 width:95%;max-width:1100px;height:500px;
 background:#1b2030;position:relative;
 overflow:hidden;border-radius:12px;
 border-bottom:12px solid #382820;
}
.window{
 position:absolute;left:5%;top:13%;
 width:23%;height:40%;
 background:#77c4f5;
 border:7px solid #101827;
 box-shadow:0 8px #69452f;
}
.window:before{
 content:"";position:absolute;left:50%;
 height:100%;width:7px;background:#101827;
}
.window:after{
 content:"";position:absolute;top:50%;
 height:7px;width:100%;background:#101827;
}
.sun{
 position:absolute;right:15%;top:15%;
 width:35px;height:35px;background:#ffdc55;
}
.clock{
 position:absolute;right:12%;top:10%;
 width:60px;height:60px;border-radius:50%;
 background:#f4e8ce;border:6px solid #101827;
}
.shelf{
 position:absolute;right:3%;top:44%;
 width:20%;height:12px;background:#69452f;
}
.book{
 position:absolute;bottom:12px;width:17px;
 height:50px;background:#3178bd;
}
.book:nth-child(2){left:30%;height:65px;background:#e74c35}
.book:nth-child(3){left:50%;background:#753e9c}
.book:nth-child(4){left:70%;height:60px;background:#e6d64f}

.desk{
 position:absolute;bottom:13%;left:3%;
 width:94%;height:15px;background:#69452f;
}
.monitor{
 position:absolute;left:36%;top:28%;
 width:29%;height:43%;
 background:#394354;padding:8px;
 box-shadow:0 8px #101827;
}
.screen{
 height:100%;background:#07182c;
 color:#65dc91;padding:12px;
 overflow:hidden;font-size:12px;
}
.screen h3{
 color:#ffe078;margin:0 0 12px;
 border-bottom:1px solid #52617b;
 padding-bottom:7px;
}
.project{display:none;animation:appear .7s}
.project.active{display:block}
.project h2{color:white;font-size:19px}
.project p{color:#b9cce0}
.project li{margin:7px 0}
@keyframes appear{
 from{opacity:0;transform:translateY(12px)}
 to{opacity:1;transform:translateY(0)}
}
.stand{
 position:absolute;left:48%;top:71%;
 width:25px;height:65px;background:#394354;
}
.plant{
 position:absolute;left:16%;bottom:13%;
 width:55px;height:50px;background:#985b37;
}
.plant:before{
 content:"";position:absolute;left:23px;bottom:45px;
 height:70px;width:8px;background:#26944e;
}
.plant:after{
 content:"";position:absolute;left:-5px;bottom:85px;
 width:65px;height:35px;
 background:#26944e;
 clip-path:polygon(0 40%,30% 40%,30% 0,60% 0,
 60% 35%,100% 35%,100% 65%,60% 65%,
 60% 100%,30% 100%,30% 65%,0 65%);
}
.poster{
 position:absolute;right:5%;top:12%;
 background:#f4e8ce;color:#071b75;
 padding:15px;font-weight:bold;
 transform:rotate(2deg);line-height:1.6;
}
.cat{
 position:absolute;right:13%;bottom:13%;
 width:90px;height:32px;background:#dda052;
 clip-path:polygon(0 50%,20% 40%,25% 0,
 40% 0,45% 40%,75% 40%,80% 0,
 95% 0,95% 40%,100% 50%,100% 100%,0 100%);
 animation:nap 3s infinite;
}
@keyframes nap{
 50%{transform:translateY(-4px)}
}
.floor{
 position:absolute;bottom:0;width:100%;height:13%;
 background:repeating-linear-gradient(
 #453027 0 8px,#35251e 8px 15px);
}
.caption{
 position:absolute;bottom:3%;left:3%;
 color:#b8c8df;font-size:11px;
}
@media(max-width:600px){
 .screen{padding:5px;font-size:8px}
 .project h2{font-size:12px}
 .project p{font-size:8px}
 .project li{margin:3px 0}
}
</style>
</head>
<body>

<div class="room">

 <div class="window"><div class="sun"></div></div>
 <div class="clock"></div>

 <div class="poster">
 DREAM<br>CODE<br>DEPLOY<br>♥
 </div>

 <div class="shelf">
  <div class="book"></div>
  <div class="book"></div>
  <div class="book"></div>
  <div class="book"></div>
 </div>

 <div class="plant"></div>

 <div class="monitor">
  <div class="screen">
   <h3>AKSHAY@GITHUB: ~/PROJECTS</h3>
   <div id="projects">
    <div class="project active">
     <h2>QRVerse</h2>
     <p>Smart QR & File Sharing</p>
     <ul>
      <li>QR Generation</li>
      <li>Offline File Bridge</li>
      <li>Supabase Integration</li>
     </ul>
    </div>
    <div class="project">
     <h2>CAMHealth</h2>
     <p>Camera Health Research</p>
     <ul>
      <li>Lens Degradation</li>
      <li>Image Quality</li>
      <li>Perception Risk</li>
     </ul>
    </div>
    <div class="project">
     <h2>Water Purification</h2>
     <p>Smart Tank System</p>
     <ul>
      <li>Multi-stage Filtration</li>
      <li>UV Treatment</li>
      <li>Overflow Sensor</li>
     </ul>
    </div>
    <div class="project">
     <h2>Code Similarity</h2>
     <p>ML-based Detection</p>
     <ul>
      <li>AST Comparison</li>
      <li>CFG Analysis</li>
      <li>Code Classification</li>
     </ul>
    </div>
   </div>
   <div style="color:#9cb6d2;font-size:9px">
    akshaycyber006@github_
   </div>
  </div>
 </div>

 <div class="stand"></div>
 <div class="desk"></div>
 <div class="cat"></div>
 <div class="floor"></div>

 <div class="caption">
 AKSHAY KRISHNA // BUILT WITH CURIOSITY
 </div>

</div>

<script>
const USER="Akshaycyber006";
let current=0;

function animateProjects(){
 const projects=document.querySelectorAll(".project");
 projects[current].classList.remove("active");
 current=(current+1)%projects.length;
 projects[current].classList.add("active");
}

setInterval(animateProjects,4000);

// Fetch real public GitHub repositories
async function loadGitHub(){
 try{
  const response=await fetch(
   `https://api.github.com/users/${USER}/repos?sort=updated&per_page=30`
  );

  if(!response.ok) throw new Error("GitHub unavailable");

  const repos=await response.json();
  const valid=repos.filter(r=>!r.fork).slice(0,4);
  const projects=document.querySelectorAll(".project");

  valid.forEach((repo,i)=>{
   if(!projects[i])return;

   projects[i].querySelector("h2").textContent=repo.name;
   projects[i].querySelector("p").textContent=
    repo.description||"GitHub Project";

   projects[i].querySelector("ul").innerHTML=`
    <li>Language: ${repo.language||"Multiple"}</li>
    <li>Stars: ${repo.stargazers_count}</li>
    <li>Forks: ${repo.forks_count}</li>
   `;
  });

 }catch(error){
  console.log("Using default projects",error);
 }
}

loadGitHub();
</script>

</body>
</html>
