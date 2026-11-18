"""Contre-lecture de la grille brouillon 2 : fuites restantes dans les copies neutres de la moitié développement.
Usage : python fuites_copies_neutres_dev_v1.py W   (W contient copies-dev/, sortie du script preparer_copies_neutres_v1.py sur la moitié développement).
Lit seulement le manifeste v2 et les copies neutres de développement. Écrit W/fuites.json (décomptes, aucun extrait de texte)."""
import json, re, os, sys, collections, statistics
W=sys.argv[1]
man=json.load(open('/home/user/controle-ia-travail/docs/notes/billets-v1/manifeste-corpus-v2.json'))
dev={b['identifiant']:b for b in man['billets'] if b['moitie']=='developpement'}
table=json.load(open(f'{W}/copies-dev/cles/table-de-correspondance.json'))['neutre_vers_site']
inv={v:k for k,v in table.items()}
BORNE="⟦FIN DE L'EN-TÊTE — 250 MOTS⟧"
res=[]
pat_score=re.compile(r"\b(karma|upvot\w*|curated|curation|frontpage|front page|LessWrong Review|Best of LessWrong|20\d\d Review|strong[- ]upvote|most[- ]upvoted)\b",re.I)
pat_html=re.compile(r"<(img|a|iframe|figure|table|div|span|sup|details)\b",re.I)
tot=collections.Counter()
rows=[]
for i,b in sorted(dev.items()):
    t=open(f'{W}/copies-dev/codeurs/billets/{inv[i]}.md',encoding='utf-8').read()
    titre,corps=t.split('\n\n',1)
    tete,_,reste=corps.partition(BORNE)
    toks=re.findall(r"\S+",tete)
    # marqueurs : jetons appartenant à [IMAGE ...], [lien : ...], [AUTEUR], [ÉLÉMENT INTERACTIF]
    sans=re.sub(r"\[IMAGE \d+[^\]]*\]"," ",tete); n_img_tete=len(re.findall(r"\[IMAGE \d+",tete))
    sans2=re.sub(r"\[lien : [^\]]*\]"," ",sans); n_lien_tete=len(re.findall(r"\[lien : ",tete))
    sans3=sans2.replace("[AUTEUR]"," ").replace("[ÉLÉMENT INTERACTIF]"," ")
    vrais=len(re.findall(r"\S+",sans3))
    # jetons de syntaxe pure (#, ---, ===, *, >, |)
    synt=sum(1 for x in re.findall(r"\S+",sans3) if re.fullmatch(r"[#=\-*>|_:]+",x))
    noms=[b['auteur'],*(b['coauteurs'] or [])]
    # fragments de noms restants
    frag=set()
    for n in noms:
        for part in re.split(r"[\s_.\-]+",n):
            if len(part)>=4 and re.search(r"\b"+re.escape(part)+r"\b",t):
                frag.add(part)
    colle=re.findall(r"\w\[AUTEUR\]|\[AUTEUR\]\w",t)
    sc=[m.group(0) for m in pat_score.finditer(t)]
    html=collections.Counter(m.group(1).lower() for m in pat_html.finditer(t))
    http=len(re.findall(r"https?://",t)); 
    ids=len(re.findall(r"lesswrong\.com/posts|alignmentforum\.org/posts",t))
    rows.append(dict(id=i,neutre=inv[i],classe=b['classe'],annee=b['annee'],mots_site=b['nombre_de_mots_site'],
        mots_copie=len(re.findall(r"\S+",corps)),tete_jetons=len(toks),tete_vrais=vrais,tete_synt=synt,img_tete=n_img_tete,liens_tete=n_lien_tete,
        auteurs_masques=t.count('[AUTEUR]'),fragments=sorted(frag),colle=colle[:3],score=sc[:6],html=dict(html),http=http,ids=ids,
        n_img=len(re.findall(r"\[IMAGE \d+",t)), n_noms=len(noms), noms_courts=[n for n in noms if len(n)<5]))
v_=[r['tete_vrais'] for r in rows]
resume={"billets":len(rows),"adresses_http_restantes":sum(r['http'] for r in rows),"adresses_de_billets_du_site":sum(r['ids'] for r in rows),
 "mots_reels_avant_la_borne":{"min":min(v_),"mediane":statistics.median(v_),"max":max(v_)},
 "billets_avec_image_avant_la_borne":sum(r['img_tete']>0 for r in rows),"billets_avec_lien_avant_la_borne":sum(r['liens_tete']>0 for r in rows),
 "billets_avec_fragment_de_nom_d_auteur_restant":{c:sum(1 for r in rows if r['fragments'] and r['classe']==c) for c in ('bien-note','apparie-peu-note')},
 "billets_avec_marqueur_AUTEUR":{c:sum(1 for r in rows if r['auteurs_masques']>0 and r['classe']==c) for c in ('bien-note','apparie-peu-note')},
 "billets_par_classe":{c:sum(1 for r in rows if r['classe']==c) for c in ('bien-note','apparie-peu-note')},
 "billets_avec_mention_de_score_ou_de_curation":[r['id'] for r in rows if r['score']],
 "AUTEUR_colle_a_un_mot":sum(1 for r in rows if r['colle']),"balises_html_restantes":sum(len(r['html']) for r in rows)}
json.dump({"resume":resume,"par_billet":[{k:r[k] for k in ('id','classe','tete_vrais','img_tete','liens_tete','auteurs_masques','fragments','n_img','n_noms')} for r in rows]},open(f'{W}/fuites.json','w'),ensure_ascii=False,indent=1)
print('billets',len(rows))
print('http restants',sum(r['http'] for r in rows),'| adresses de billets du site',sum(r['ids'] for r in rows))
v=[r['tete_vrais'] for r in rows]
print('mots réels avant la borne : min',min(v),'médiane',statistics.median(v),'max',max(v))
for cl in ('bien-note','apparie-peu-note'):
    vv=[r['tete_vrais'] for r in rows if r['classe']==cl]
    print('  ',cl,'n',len(vv),'min',min(vv),'médiane',statistics.median(vv),'moyenne',round(statistics.mean(vv),1),'sous 200:',sum(x<200 for x in vv),'sous 150:',sum(x<150 for x in vv))
print('billets avec image avant la borne:',sum(r['img_tete']>0 for r in rows), '| avec lien avant la borne:',sum(r['liens_tete']>0 for r in rows))
print('--- les dix en-têtes les plus amputés')
for r in sorted(rows,key=lambda r:r['tete_vrais'])[:10]:
    print('  ',r['id'],r['classe'],'vrais',r['tete_vrais'],'liens',r['liens_tete'],'images',r['img_tete'],'synt',r['tete_synt'])
print('--- fragments de noms d auteurs restants')
nf=[r for r in rows if r['fragments']]
print(len(nf),'billets sur',len(rows))
for r in nf[:40]: print('  ',r['id'],r['classe'],r['fragments'])
print('--- [AUTEUR] collé à un mot'); 
for r in rows:
    if r['colle']: print('  ',r['id'],r['colle'])
print('--- noms courts',[ (r['id'],r['noms_courts']) for r in rows if r['noms_courts']])
print('--- mentions de score ou de curation dans le texte')
for r in rows:
    if r['score']: print('  ',r['id'],r['classe'],r['score'])
print('--- balises html restantes',collections.Counter(k for r in rows for k in r['html']))
print('--- billets sans aucun [AUTEUR]:',sum(r['auteurs_masques']==0 for r in rows),'; par classe',collections.Counter(r['classe'] for r in rows if r['auteurs_masques']==0))
print('--- [AUTEUR] présent par classe',collections.Counter(r['classe'] for r in rows if r['auteurs_masques']>0))
for cl in ('bien-note','apparie-peu-note'):
    vv=[r['mots_copie'] for r in rows if r['classe']==cl]; ii=[r['n_img'] for r in rows if r['classe']==cl]
    print(cl,'mots copie médiane',statistics.median(vv),'images médiane',statistics.median(ii),'moyenne images',round(statistics.mean(ii),1))
