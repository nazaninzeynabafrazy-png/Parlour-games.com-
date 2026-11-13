import os
s=open('ads.html',encoding='utf-8').read()
# one source of truth: the no-ads copy is ads.html with the single ADS.enabled flag switched off
_on="  enabled: true,               // true = ads, gems"; assert s.count(_on)==1
s2=s.replace(_on,"  enabled: false,              // true = ads, gems")
open('ads2.html','w',encoding='utf-8').write(s2)
O=open('head_lines.txt',encoding='utf-8').read().split('\n')
def w(p,t):
    if os.path.exists(p): os.remove(p)
    open(p,'w',encoding='utf-8').write(t)
w('out/parlour-online.html','\n'.join(O+s2.split('\n')[19:]))
n=open('new.html',encoding='utf-8').read().split('\n'); body=s.split('\n')[19:]
while body[-1].strip()=='': body.pop()
idx='\n'.join(n[:16]+body[:-2]+[n[16513],'</body>','</html>'])+'\n'
REG_OLD='<script>if("serviceWorker" in navigator && location.protocol.indexOf("http")===0){window.addEventListener("load",function(){navigator.serviceWorker.register("sw.js").catch(function(){});});}</script>'
REG_NEW=r'''<script>if("serviceWorker" in navigator && location.protocol.indexOf("http")===0){window.addEventListener("load",function(){
function ask(){if(document.getElementById("updBar"))return;var L=(document.documentElement.lang||"en").slice(0,2),T={en:["A new version is ready.","Reload"],fa:"\u0646\u0633\u062e\u0647\u0654 \u062c\u062f\u06cc\u062f \u0622\u0645\u0627\u062f\u0647 \u0627\u0633\u062a.|\u0628\u0627\u0631\u06af\u0630\u0627\u0631\u06cc".split("|")},t=T[L]||T.en;var d=document.createElement("div");d.id="updBar";d.setAttribute("role","status");d.style.cssText="position:fixed;left:8px;right:8px;bottom:8px;z-index:99999;background:#1c3a2c;color:#fff;border:1px solid #d9b765;border-radius:10px;padding:10px 12px;display:flex;gap:10px;align-items:center;justify-content:space-between;font:15px system-ui,sans-serif";d.innerHTML="<span></span><button style=\"background:#d9b765;color:#10281f;border:0;border-radius:8px;padding:8px 14px;font-weight:700\"></button>";d.firstChild.textContent=t[0];d.lastChild.textContent=t[1];d.lastChild.onclick=function(){location.reload()};document.body.appendChild(d)}
navigator.serviceWorker.register("sw.js").then(function(reg){
if(reg.waiting&&navigator.serviceWorker.controller)ask();
reg.addEventListener("updatefound",function(){var nw=reg.installing;if(nw)nw.addEventListener("statechange",function(){if(nw.state==="installed"&&navigator.serviceWorker.controller)ask()})});
reg.update().catch(function(){});setInterval(function(){reg.update().catch(function(){})},1800000)}).catch(function(){});});}</script>'''
assert idx.count(REG_OLD)==1
idx=idx.replace(REG_OLD,REG_NEW)
w('out/index.html',idx); w('out/parlour-offline.html',s); w('out/parlour-offline-noads.html',s2); w('webpkg/index.html',idx)
w('out/parlour-online-gems.html','\n'.join(O+s.split('\n')[19:]))
