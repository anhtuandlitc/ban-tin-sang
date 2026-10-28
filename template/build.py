import base64,sys,datetime
import os; d=os.path.dirname(os.path.abspath(__file__))+'/'
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
vi=b(d+'fonts/fraunces-vietnamese-600-normal.woff2')
la=b(d+'fonts/fraunces-latin-600-normal.woff2')
jobs=[
 ("Senior Technical Engineer (SRE, Ops, AI)","HSC · Chứng khoán","https://www.linkedin.com/jobs/view/4446040417/",86,"Chứng khoán + SRE/AI, đúng hướng 50/50.",[("Làm việc",20,30),("Tài chính",25,25),("Học mới",22,25),("Cân bằng",19,20)],True),
 ("Senior Platform / DevOps Engineer","GreenNode","https://www.linkedin.com/jobs/view/4482914311/",60,"Học K8s, cloud nhiều; không nêu tài chính.",[("Làm việc",20,30),("Tài chính",5,25),("Học mới",25,25),("Cân bằng",10,20)],False),
 ("Application Production Support Engineer, Banking","Innotech Vietnam","https://www.linkedin.com/jobs/view/4482945342/",60,"Sát nghề cũ, ít thứ mới để học.",[("Làm việc",20,30),("Tài chính",22,25),("Học mới",8,25),("Cân bằng",10,20)],False),
 ("Senior Site Reliability Engineer","SmartDev","https://www.linkedin.com/jobs/view/4483532250/",59,"SRE thuần; không nêu tài chính.",[("Làm việc",20,30),("Tài chính",5,25),("Học mới",24,25),("Cân bằng",10,20)],False),
 ("Senior MLOps Engineer (AI/ML, AWS)","FPT Software Innovation","https://www.linkedin.com/jobs/view/4482918134/",59,"Vận hành hệ thống AI; không nêu tài chính.",[("Làm việc",20,30),("Tài chính",5,25),("Học mới",24,25),("Cân bằng",10,20)],False),
]
out=[]
for t,c,u,s_,cm,bars,hi in jobs:
    assert sum(x[1] for x in bars)==s_,(t,s_)
    bh=''.join(f'<div class="bar"><span>{n}</span><i><u style="width:{v/m*100:.0f}%"></u></i><em class="num">{v}</em></div>' for n,v,m in bars)
    lvl="Cao" if s_>=75 else "Trung bình"
    out.append(f'<article class="job{" hi" if hi else ""}"><div class="ring" style="--p:{s_}"><span>{s_}</span></div><div class="jb"><h4><a href="{u}" target="_blank" rel="noopener">{t}</a></h4><div class="co">{c} · {lvl}</div><p>{cm}</p><div class="bars">{bh}</div></div></article>')
h=open(d+'template.html',encoding='utf-8').read()
h=h.replace('{{FONT_VI}}',vi).replace('{{FONT_LATIN}}',la).replace('{{JOBS}}','\n'.join(out)).replace('{{TIME}}',sys.argv[1])
open(d+'../index.html','w',encoding='utf-8').write(h)
print(len(h))
