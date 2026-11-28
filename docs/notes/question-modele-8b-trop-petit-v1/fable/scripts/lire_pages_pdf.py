import re,sys
def pages(path):
    return open(path,encoding='utf-8',errors='replace').read().split('\f')
def grep(path,pat,maxp=None,width=240):
    ps=pages(path)
    rx=re.compile(pat,re.I)
    for i,p in enumerate(ps,1):
        if maxp and i>maxp: break
        for line in p.split('\n'):
            if rx.search(line):
                print(i,'|',re.sub(r'\s+',' ',line.strip())[:width])
def show(path,nums):
    ps=pages(path)
    for n in nums:
        print('=== PAGE',n)
        print(re.sub(r'[ ]{2,}',' ',ps[n-1]))
if __name__=='__main__':
    if sys.argv[1]=='grep': grep(sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else None)
    else: show(sys.argv[2],[int(x) for x in sys.argv[3:]])
