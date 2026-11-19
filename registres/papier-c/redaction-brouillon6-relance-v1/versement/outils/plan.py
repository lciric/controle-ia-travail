import sys,re,collections
W=sys.argv[1]
idx=[l.rstrip('\n').split('\t') for l in open(W+'/outils/index-archives.tsv',encoding='utf-8')]
N='docs/notes/'; CL=N+'contre-lectures-papier-C-v1/'; AR=N+'papier-C-session16-archive-v1/'; ME=N+'papier-C-mesures-v1/'
BR=AR+'brouillons-session16-jamais-verses-matiere-premiere/'
NP=AR+'notes-voisins-posterieures-au-brouillon5/'
P='./papier-C/'
# (lot, archive préférée ou None, motif, destination: fonction du match)
R=[
 ('1-brouillon4',None,r'papier-C-preenregistrement-HC1-HC3-v1-brouillon4\.md$',lambda m,n:AR+'brouillon4/'+n.split('/')[-1]),
 ('1-brouillon4',None,r'traitement-contre-lectures-brouillon4-papier-C-v1\.md$',lambda m,n:AR+'brouillon4/'+n.split('/')[-1]),
 ('1-brouillon4',None,r'brouillon5/table-traitement-brouillon5-v1\.md$',lambda m,n:AR+'brouillon5/'+n.split('/')[-1]),
 ('2-notes-voisins',None,r'brouillon5/notes/(lecture-[^/]+\.md)$',lambda m,n:N+m.group(1)),
 ('2-notes-voisins',None,r'contre-lectures/(contre-lecture-note-[^/]+\.md)$',lambda m,n:CL+m.group(1)),
 ('3-mesures',None,r'mesures/(mesures[-_]conception[^/]+\.(txt|py))$',lambda m,n:ME+m.group(1)),
 ('3-mesures',None,r'brouillon5/outils/(verifier_kendall_C_P3_v1\.(txt|py))$',lambda m,n:ME+m.group(1)),
 ('4-ecrire-config',None,r'outils/(ecrire_config_v1\.py)$',lambda m,n:AR+'outils/'+m.group(1)),
 ('4-ecrire-config',None,r'brouillon5/outils/(ecrire_config_brouillon2_v1\.(py|journal\.txt))$',lambda m,n:AR+'outils/'+m.group(1)),
 ('5-contre-lectures-brouillon4',None,r'contre-lectures/(contre-lecture-R2-brouillon4-[^/]+\.md)$',lambda m,n:CL+m.group(1)),
 ('5-contre-lectures-brouillon4',None,r'contre-lectures/(simulations-methode/[^/]+)$',lambda m,n:CL+m.group(1)),
 ('5-contre-lectures-brouillon4',None,r'contre-lectures/(outils-panin/simulation_selection_gamma_v1\.(py|sortie\.txt))$',lambda m,n:CL+m.group(1)),
 ('6-contre-lectures-brouillon5',None,r'(contre-lectures-brouillon5/methode/.+)$',lambda m,n:CL+m.group(1)),
 ('6-contre-lectures-brouillon5',None,r'(contre-lectures-brouillon5/texte/(contre-lecture-R2-brouillon5-texte-v1\.md|sha256sums-texte-v1\.txt))$',lambda m,n:CL+m.group(1)),
 ('7-contre-lectures-brouillon6',None,r'(contre-lectures-brouillon6/methode-courte/.+)$',lambda m,n:CL+m.group(1)),
 ('7-contre-lectures-brouillon6',None,r'(contre-lectures-brouillon6/texte/contre-lecture-R2-brouillon6-texte-v1\.md)$',lambda m,n:CL+m.group(1)),
 ('8-familles-du-vivier',None,r'(verrou-famille1/verification-verrou-famille1-v1\.md)$',lambda m,n:CL+m.group(1)),
 ('9-brouillons-6-7',None,r'(brouillon6/(papier-C-preenregistrement-HC1-HC3-v1-brouillon6\.md|table-traitement-brouillon6-v1\.md))$',lambda m,n:BR+m.group(1)),
 ('9-brouillons-6-7',None,r'(brouillon7/(papier-C-preenregistrement-HC1-HC3-v1-brouillon7\.md|table-traitement-brouillon7-v1\.md|papier-C-config-v1-brouillon4\.json))$',lambda m,n:BR+m.group(1)),
 ('10-notes-posterieures','A20',r'contre-lectures-brouillon5/(voisins/(lecture-voisins-joswin-huqu-v1\.md|sha256sums-voisins-v1\.txt))$',lambda m,n:NP+m.group(1)),
 ('10-notes-posterieures','A21',r'contre-lectures-brouillon5/((voisins-panin|voisins-second-rang|voisins-cp02|voisins-cv2-03|voisins-restants)/(lecture-voisins-[^/]+\.md|sha256sums-[^/]+\.txt))$',lambda m,n:NP+m.group(1)),
 ('10-notes-posterieures','A21',r'contre-lectures-brouillon5/(contre-lecture-courte-voisins/(contre-lecture-courte-notes-voisins-v1\.md|sha256sums-[^/]+\.txt))$',lambda m,n:NP+m.group(1)),
]
plan=collections.OrderedDict(); pb=[]
for tag,h,s,n in idx:
    if n.endswith('.sha256') or not n.startswith(P): continue
    rel=n[len(P):]
    for lot,pref,pat,f in R:
        m=re.search('^'+pat if pat.startswith('(') else pat,rel) if False else re.match(r'(?:.*/)?'+pat if not pat.startswith('(') and '/' not in pat.split('$')[0] else pat, rel)
        if not m: m=re.fullmatch(pat.rstrip('$'),rel) 
        if not m: continue
        if pref and tag!=pref: break
        d=f(m,n)
        if d in plan:
            if plan[d][2]!=h: pb.append(('DIVERGENCE',d,plan[d][:4],(lot,tag,h,n)))
            else: plan[d][5].append(tag)   # même empreinte dans l'autre archive
        else: plan[d]=[lot,tag,h,n,s,[tag]]
        break
for d,v in plan.items(): print('\t'.join([v[0],d,v[1],v[3],v[2],v[4],'+'.join(v[5])]))
for p in pb: print('PB',p,file=sys.stderr)
