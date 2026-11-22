import subprocess, sys, re
pdf=sys.argv[1]; pats=sys.argv[2:]
import pypdf
n=len(pypdf.PdfReader(pdf).pages)
for p in range(1,n+1):
    t=subprocess.run(['pdftotext','-f',str(p),'-l',str(p),pdf,'-'],capture_output=True,text=True).stdout
    t2=re.sub(r'\s+',' ',t.replace('-\n',''))
    for pat in pats:
        if re.search(pat,t2,flags=re.I):
            print(f'p.{p}: {pat}')
