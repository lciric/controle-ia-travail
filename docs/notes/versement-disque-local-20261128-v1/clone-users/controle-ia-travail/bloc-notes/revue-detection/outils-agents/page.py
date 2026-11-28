import sys
D="/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/extraction/txt-agents/"
pid=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3]) if len(sys.argv)>3 else a
pages=open(D+pid+".txt",encoding="utf-8",errors="replace").read().split("\f")
for i in range(a,b+1):
    print(f"========== p.{i}")
    print(pages[i-1])
