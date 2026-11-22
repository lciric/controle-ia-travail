import subprocess,re,sys
def g(*a): return subprocess.run(['git',*a],capture_output=True,text=True).stdout
EXCL=re.compile(r'quarantaine|coffre|lot/compte-4-v1|matiere-premiere/modes-attaque|archives-reponses|bras-attaque-oracle|consigne-privee|conception-ii-b')
SENS=re.compile(r'verite|vérité|rendu|scores|consigne-privee|conception-ii-b|ii-b-saboteur-budget|archives-reponses|barreau5|t0-6|t0\.6|etape-b|p3-bis|resultat|quarantaine|coffre|bras-attaque-oracle|reponses-modeles',re.I)
VERSE=re.compile(r'fable|collisionneur|protocole|exploration|veille|biblio|memoire|mathematiques|lentilles|papier-c|essaim|conscience|adoring-mayer|idees|brainstorm|demande|passe-x',re.I)
refs=[l.split() for l in g('for-each-ref','--format=%(refname:short) %(objectname:short) %(committerdate:short)','refs/remotes/origin').splitlines()]
idx=[];verse=[]
for r,c,d in refs:
    if d<'2026-11-18' or EXCL.search(r) or r in('origin/main','origin/HEAD','origin'): continue
    add=[l.split('\t')[1] for l in g('diff','--name-status','--diff-filter=A',f'origin/main...{r}').splitlines() if '\t' in l]
    add=[f for f in add if (f.startswith('docs/') or f.startswith('registres/essaim') or f.startswith('registres/passations') or f.startswith('prereg/') or f.startswith('papiers/'))]
    if not add: continue
    sens=[f for f in add if SENS.search(f)]
    ok=[f for f in add if not SENS.search(f)]
    idx.append((r,c,d,len(add),len(sens),sorted({'/'.join(f.split('/')[:3]) for f in add})))
    if VERSE.search(r): verse+= [(r,f) for f in ok if not f.startswith('prereg/')]
with open(sys.argv[1],'w') as o:
    o.write("# Index des pistes, idées, hypothèses, échecs, remue-méninges et retours des modèles, par branche — v1\n\n")
    o.write("- Nature : classe C, écrit par programme par la mère sur l'ordre de Lazar (« dépose bien l'ensemble de TOUTES les idées … dans le dépôt et renvois dans la passation »). Noms et dossiers seulement ; aucun contenu lu.\n")
    o.write("- Périmètre : branches distantes poussées depuis le 18 novembre, fichiers AJOUTÉS par rapport à main sous docs/, prereg/, papiers/, registres/essaim, registres/passations. Branches exclues par nom : quarantaine, coffre, lot/compte-4-v1, matière première séquestrée des modes d'attaque, archives des réponses, oracle du bras d'attaque.\n")
    o.write("- Colonne « sensibles » : fichiers dont le nom porte un motif cloisonné (vérité, rendu, scores, barreau 5, T0.6, étape B, P3-bis, résultat…), jamais versés par la mère.\n\n")
    o.write("| branche | commit | date | fichiers ajoutés | dont sensibles | dossiers |\n|---|---|---|---|---|---|\n")
    for r,c,d,n,s,dirs in sorted(idx,key=lambda x:x[2],reverse=True):
        o.write(f"| {r[7:]} | {c} | {d} | {n} | {s} | {'<br>'.join(dirs[:12])}{' …' if len(dirs)>12 else ''} |\n")
with open(sys.argv[2],'w') as o:
    for r,f in verse: o.write(f"{r}\t{f}\n")
print(len(idx),len(verse))
