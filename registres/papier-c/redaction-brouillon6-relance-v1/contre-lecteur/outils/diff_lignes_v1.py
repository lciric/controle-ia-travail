# Contre-lecteur : différence par lignes (unified, sans contexte).
import sys,difflib
a=open(sys.argv[1],encoding='utf-8').read().split('\n'); b=open(sys.argv[2],encoding='utf-8').read().split('\n')
for l in difflib.unified_diff(a,b,'avant','apres',n=0,lineterm=''): print(l)
