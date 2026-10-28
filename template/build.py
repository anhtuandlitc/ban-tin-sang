import base64,sys,datetime
import os; d=os.path.dirname(os.path.abspath(__file__))+'/'
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
vi=b(d+'fonts/fraunces-vietnamese-600-normal.woff2')
la=b(d+'fonts/fraunces-latin-600-normal.woff2')
jobs=[
 ("Senior Technical Engineer (SRE, Ops, AI)","HSC · Chứng khoán","https://www.linkedin.com/jobs/view/4446040417/",86,[("Làm việc",20,30),("Tài chính",25,25),("Học mới",22,25),("Cân bằng",19,20)],True),
 ("Senior Platform / DevOps Engineer","GreenNode","https://www.linkedin.com/jobs/view/4482914311/",60,[("Làm việc",20,30),("Tài chính",5,25),("Học mới",25,25),("Cân bằng",10,20)],False),
 ("Application Production Support Engineer, Banking","Innotech Vietnam","https://www.linkedin.com/jobs/view/4482945342/",60,[("Làm việc",20,30),("Tài chính",22,25),("Học mới",8,25),("Cân bằng",10,20)],False),
 ("Senior Site Reliability Engineer","SmartDev","https://www.linkedin.com/jobs/view/4483532250/",59,[("Làm việc",20,30),("Tài chính",5,25),("Học mới",24,25),("Cân bằng",10,20)],False),
 ("Senior MLOps Engineer (AI/ML, AWS)","FPT Software Innovation","https://www.linkedin.com/jobs/view/4482918134/",59,[("Làm việc",20,30),("Tài chính",5,25),("Học mới",24,25),("Cân bằng",10,20)],False),
]
out=[]
for t,c,u,s,bars,hi in jobs:
    assert sum(x[1] for x in bars)==s,(t,s)
    bh=''.join(f'<div>{n} <span class="num">{v}</span><i><u style="width:{v/m*100:.0f}%"></u></i></div>' for n,v,m in bars)
    out.append(f'<article class="job{" hi" if hi else ""}"><div class="ring" style="--p:{s}"><span>{s}</span></div><div><b><a href="{u}" target="_blank" rel="noopener">{t}</a></b><div class="co">{c} · {"Cao" if s>=75 else "Trung bình"}</div><div class="bars">{bh}</div></div></article>')
h=open(d+'template.html',encoding='utf-8').read()
h=h.replace('{{FONT_VI}}',vi).replace('{{FONT_LATIN}}',la).replace('{{JOBS}}','\n'.join(out)).replace('{{TIME}}',sys.argv[1])
open(d+'../index.html','w',encoding='utf-8').write(h)
print(len(h))
