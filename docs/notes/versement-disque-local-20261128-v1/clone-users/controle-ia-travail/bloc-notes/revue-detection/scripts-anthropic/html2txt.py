import sys, html.parser
class P(html.parser.HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.skip=0
    def handle_starttag(s,t,a):
        if t in ('script','style','noscript'): s.skip+=1
        if t in ('p','h1','h2','h3','h4','li','figcaption','br','div','tr'): s.out.append('\n')
    def handle_endtag(s,t):
        if t in ('script','style','noscript') and s.skip: s.skip-=1
    def handle_data(s,d):
        if not s.skip: s.out.append(d)
p=P(); p.feed(open(sys.argv[1],encoding='utf-8').read())
import re
t=''.join(p.out); t=re.sub(r'\n\s*\n+','\n\n',t)
open(sys.argv[2],'w',encoding='utf-8').write(t)
