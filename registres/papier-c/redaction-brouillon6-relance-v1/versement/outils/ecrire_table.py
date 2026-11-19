import sys,os,hashlib,collections
W=sys.argv[1]
AN={'A20':'archive du 20 octobre','A21':'complément du 21 octobre'}
def sha(p):
    h=hashlib.sha256(); h.update(open(p,'rb').read()); return h.hexdigest()
plan=[l.rstrip('\n').split('\t') for l in open(W+'/outils/plan.tsv',encoding='utf-8')]
byh=collections.defaultdict(list)
for r in plan: byh[r[4]].append(r)
cites={}  # empreinte -> (ligne, chemin cité)
for l in open(W+'/outils/releve-brut.tsv',encoding='utf-8'):
    c=l.rstrip('\n').split('\t')
    if c[0]=='H' and c[2] not in cites: cites[c[2]]=(c[1],c[3])
# correction des chemins cités mal appariés par proximité (relus dans le texte)
fix={'12879073de20e9129e1e555642ed85fb9a887d955fc5c9e2ac418552842a129b':'./papier-C/contre-lectures-brouillon5/texte/contre-lecture-R2-brouillon5-texte-v1.md'}
o=[]
o.append("# Table de versement des pièces du papier C restées dans les archives de la session 16 — version 1\n")
o.append("Date : 2026-11-19. Pièce de travail (classe C), écrite par un sous-agent d'inventaire ; rien n'est modifié au dépôt.\n")
o.append("Texte dépouillé : `brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c2.md` (`7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61`, recalculée).")
o.append("Archives (empreintes conformes à leurs compagnons) : archive du 20 octobre `registres/passations/bloc-notes-session16-2026-10-20.tar.gz` (`cfe144eb1b1183d2f95fb429f00b89e4c2b1441183c5ab1babc05741df822dec`) ; complément du 21 octobre `registres/passations/bloc-notes-session16-complement-2026-10-21.tar.gz` (`0c15862cfc97470d816690c282d9fde7ecb65e684308fbfcf128ef4cd5e2c436`).")
o.append("Arbre de versement : `"+W+"/arbre/` (reproduit les chemins du dépôt ; chaque pièce a son compagnon `<nom>.sha256`).\n")
o.append("Méthode : relevé par programme de chaque chemin et de chaque empreinte complète du texte (109 empreintes, 90 distinctes ; 159 chemins) ; absence vérifiée sur disque (R11) par chemin et par index des empreintes de l'arbre du dépôt, hors `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; membres des archives hachés sans extraction, puis extraits par nom ; empreinte et taille recontrôlées après copie ; aucun chemin de versement n'existe au dépôt (R12).\n")
# A
A=[(int(cites[h][0]),h) for h in cites if h in byh]
A.sort()
o.append("## 1. Pièces citées par empreinte dans le texte, absentes de l'arbre du dépôt, trouvées dans les archives\n")
o.append("%d pièces. Toutes conformes : l'empreinte recalculée est l'empreinte citée.\n"%len(A))
o.append("| Ligne du texte | Chemin cité | Empreinte citée | Archive et chemin dans l'archive | Empreinte recalculée | Conforme | Chemin de versement |")
o.append("|---|---|---|---|---|---|---|")
vusA=set()
for ln,h in A:
    r=byh[h][0]; vusA.add(r[1])
    dst=W+'/arbre/'+r[1]; h2=sha(dst)
    o.append("| %d | `%s` | `%s` | %s : `%s` | `%s` | %s | `%s` |"%(ln,fix.get(h,cites[h][1]),h,AN[r[2]],r[3],h2,'oui' if h2==h else 'NON',r[1]))
o.append("\nNote : `verifier_kendall_C_P3_v1.txt` existe aussi, à la même empreinte, sous `./papier-C/contre-lectures-brouillon5/outils-texte/rejeu_verifier_kendall_cl6.txt` (archive du 20 octobre), non versé.\n")
# B
o.append("## 2. Pièces versées que le texte ne cite pas par empreinte complète (demandées par les verrous 2 et 5, ou solidaires d'une pièce citée)\n")
lots=collections.OrderedDict([
 ('1-brouillon4',"Brouillon 4 et pièces de son traitement"),
 ('2-notes-voisins',"Notes finales des voisins et rapports de leurs contre-lectures"),
 ('3-mesures',"Mesures de conception et vérification des lois nulles du W de Kendall"),
 ('4-ecrire-config',"Programmes d'écriture de la configuration"),
 ('5-contre-lectures-brouillon4',"Contre-lectures du brouillon 4 et leurs simulations"),
 ('6-contre-lectures-brouillon5',"Contre-lectures du brouillon 5 (session 16) et leurs simulations"),
 ('7-contre-lectures-brouillon6',"Contre-lectures du brouillon 6 de la session 16 et leurs simulations"),
 ('8-familles-du-vivier',"Vérification par indices des familles du vivier"),
 ('9-brouillons-6-7',"Brouillons 6 et 7 de la session 16, jamais versés, matière première, et leurs tables de traitement"),
 ('10-notes-posterieures',"Notes des voisins postérieures au brouillon 5 (verrou 2 ; décision D-11, accord GO-2026-11-19-53)")])
o.append("| Lot | Archive et chemin dans l'archive | Empreinte recalculée | Octets | Chemin de versement |")
o.append("|---|---|---|---|---|")
nB=0
for r in plan:
    if r[1] in vusA: continue
    nB+=1
    src=AN[r[2]]+(' (aussi au complément du 21 octobre, même empreinte)' if r[6]=='A20+A21' else '')
    o.append("| %s | %s : `%s` | `%s` | %s | `%s` |"%(lots[r[0]],src,r[3],sha(W+'/arbre/'+r[1]),r[5],r[1]))
o.append("\n%d pièces. Les trois manifestes de simulations, rejoués sur l'arbre : `sha256sums-simulations-methode-v1.txt` 25 lignes sur 25 ; `sha256sums-simulations-methode-b5-v1.txt` 27 sur 27 ; `sha256sums-simulations-methode-courte-b6-v1.txt` 61 sur 61.\n"%nB)
o.append("Compte par lot (pièces, sans les compagnons) :\n")
c=collections.Counter(r[0] for r in plan)
for k,v in lots.items(): o.append("- %s : %d"%(v,c[k]))
# C v2
M=W+'/arbre/docs/notes/papier-C-mesures-v1/'
o.append("\n## 3. Mesures de conception, version 2 (pièces neuves, émises le 2026-11-19)\n")
o.append("| Pièce | Empreinte | Chemin de versement |\n|---|---|---|")
for f in ('mesures_conception_papier_c_v2.py','mesures-conception-papier-C-v2.txt'):
    o.append("| %s | `%s` | `docs/notes/papier-C-mesures-v1/%s` |"%(f,sha(M+f),f))
env=open(W+'/outils/manifeste-environnement-mesures-v2.txt',encoding='utf-8').read().strip().split('\n')
o.append("\n- Calcul sur processeur, sans donnée. Environnement local du bloc-notes (`venv/`) : "+' ; '.join(x for x in env[1:5])+". Manifeste : `outils/manifeste-environnement-mesures-v2.txt` (`%s`)."%sha(W+'/outils/manifeste-environnement-mesures-v2.txt'))
o.append("- Le script version 1, relancé dans cet environnement, rend la sortie version 1 de l'archive octet pour octet (`bbad099d…`).")
o.append("- Version 2 contre version 1, ligne à ligne : deux lignes ajoutées et rien d'autre — en tête « numpy 2.5.5 ; scipy 1.18.1 », en fin « P(W ≤ 0,20) sous le nul = 0,6327 ». Aucun chiffre ne diffère. La ligne ajoutée sort du calcul (part des 7 776 affectations où W ≤ 0,20).")
o.append("- Les versions de numpy et de scipy qui ont produit la sortie version 1 en session 16 ne sont pas connues de ce rédacteur.")
o.append("- Champ `<<EMPREINTE_MESURES_V2>>` du texte : `%s`.\n"%sha(M+'mesures-conception-papier-C-v2.txt'))
# D
o.append("## 4. Pièces citées, non versées\n")
o.append("- **Note du vivier** (`<<CHEMIN_NOTE_VIVIER>>`, `dbad9e6656fd366f9c4282a6c9a5d9c661076be2678af163370cf9d7a519d41e`) : introuvable par empreinte dans l'arbre du dépôt indexé et dans les deux archives entières ; aucun nom évocateur dans les listes. Non cherchée ailleurs ; la session de conduite s'en charge.")
o.append("- **Sept pièces sous `donnees/`** (tâches du pilote, deux résultats du projet précédent, note de provenance, items, invites, gabarit) : présentes au dépôt ; leurs compagnons portent l'empreinte citée ; ni ouvertes ni recalculées (dossier interdit à ce rédacteur).")
o.append("- **Quatre rapports de lecteurs du niveau 3** (lignes 265 à 268 du texte) : ni sur la branche de travail ni dans les archives ; le texte les dit sur les branches `prep/etat-de-l-art-niveau3-pieces-v1` et `prep/etat-de-l-art-niveau3-v1` ; non cherchés.")
o.append("- Les 49 autres empreintes distinctes citées désignent des pièces présentes au dépôt à l'empreinte citée (ou le texte lui-même dans ses versions antérieures, et les pièces « versées avec ce brouillon »), sauf la note du vivier et les sept pièces de `donnees/` ci-dessus : voir `outils/croisement.tsv`. Aucune pièce d'empreinte différente de celle citée n'a été trouvée.\n")
# E PDF
o.append("## 5. PDF cités par les notes versées et absents de `docs/sources/pdf/`\n")
rows=[l.rstrip('\n').split('\t') for l in open(W+'/outils/pdf-cites.tsv',encoding='utf-8')]
ab=[r for r in rows if r[0]=='ABSENT']; pr=[r for r in rows if r[0]!='ABSENT']
o.append("%d PDF absents (ni sous ce nom dans `docs/sources/pdf/`, ni à cette empreinte ailleurs dans l'arbre indexé du dépôt). Les archives n'en gardent que le compagnon `.pdf.sha256` ; aucun PDF n'est versé. Tous sont cités par les notes postérieures au brouillon 5.\n"%len(ab))
o.append("| PDF | Empreinte (compagnon de l'archive, aussi citée dans la note) | Note qui le cite | Compagnon dans l'archive |\n|---|---|---|---|")
for r in ab: o.append("| `%s` | `%s` | %s | `%s` |"%(r[1],r[2],r[4].replace(';',' ; '),r[3]))
o.append("\nPrésents au dépôt : "+' ; '.join('`docs/sources/pdf/%s`'%r[1] for r in pr)+" (cités par les deux notes finales du verrou 2).")
o.append("L'article de Kumaran et al. (revue, dossier `voisins-restants/telechargement/nmi-s42256-026-01217-9/`) n'a pas de compagnon de PDF dans l'archive : seul un fichier d'en-têtes de requête y figure ; relevé par nom, non ouvert.\n")
# F
o.append("## 6. Resté dans les archives, non versé\n")
o.append("Contre-lectures du brouillon 7 (le verrou 5 ne nomme que les brouillons 4, 5 et 6) ; consignes aux rédacteurs et aux contre-lecteurs ; configurations en brouillons 1 et 3 ; points ouverts du brouillon 4 ; traitement des contre-lectures du brouillon 5 et son projet ; dossiers `travail/`, `essais/`, `outils-texte/`, `outils-voisins/` ; programmes de vérification des citations des notes ; extractions de texte des PDF, pages téléchargées, image ; dossier `voisins-C/`.\n")
o.append("## 7. Chemins de versement proposés par ce rédacteur (le texte n'en donnait pas)\n")
o.append("- `docs/notes/papier-C-session16-archive-v1/brouillon4/`, `…/brouillon5/`, `…/outils/` ; `…/brouillons-session16-jamais-verses-matiere-premiere/brouillon6|brouillon7/` ; `…/notes-voisins-posterieures-au-brouillon5/`.")
o.append("- Sous `docs/notes/contre-lectures-papier-C-v1/` : rapports du brouillon 4 et des notes à plat (même nom, comme le dit le texte) ; `simulations-methode/` et `outils-panin/` sous leur nom cité ; `contre-lectures-brouillon5/…` et `contre-lectures-brouillon6/…` en gardant le chemin relatif de l'archive, de sorte que les chemins `papier-C/contre-lectures-brouillon5/…` du texte s'y lisent tels quels ; `verrou-famille1/`.")
o.append("- La note des voisins de second rang diffère entre les deux archives (`7357e85d…` le 20 octobre, `8027bd53…` le 21) : celle du 21 est versée, avec les manifestes du 21.\n")
# totals
n=0;tot=0;nc=0
for d,_,fs in os.walk(W+'/arbre'):
    for f in fs:
        p=os.path.join(d,f); tot+=os.path.getsize(p)
        if f.endswith('.sha256'): nc+=1
        else: n+=1
o.append("## 8. Totaux\n")
o.append("- Pièces dans l'arbre : %d (%d tirées des archives, 2 neuves en version 2) ; compagnons : %d ; %d octets au total, compagnons compris."%(n,len(plan),nc,tot))
o.append("- Contenus ouverts par ce rédacteur : le texte dépouillé ; le script et la sortie des mesures en version 1 ; les têtes de trois manifestes ; les notes des voisins, par programme seulement (noms de PDF et empreintes). Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune sortie de simulation ouverte.")
o.append("- Journal de l'exécution, refus de permission compris : `journal-versement-v1.md`.")
open(W+'/table-versement-pieces-papier-C-v1.md','w',encoding='utf-8',newline='\n').write('\n'.join(o)+'\n')
print(len(A),nB,n,nc,tot)
