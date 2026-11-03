"""Scheurer, course de l'organisme sans Claude (source 2) : consigne du lecteur A suite, puis lot 2 et ensemble (tour, matin, course) par
preparer_lot2_soir_v1.py, parts et consignes des moissonneurs, groupeur aveugle de l'ensemble, clé de l'ensemble ; puis moisson fusionnée et classeur.
Le paquet sans provenance se fait par paquet_course_soir_v2.py (graine : 'source-2-permutation-v1|' + sha256(fiches.json)).
Usage : chaine_scheurer_lot2_v1.py lecteur | prep TAILLE_PART | classeur"""
import hashlib, json, sys, os, glob, shutil, subprocess
R = '/home/claude/controle-ia-travail/'; P = R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/'
S = '/home/claude/scratch/soir-rapport/scheurer/'; E = '/home/claude/scratch/soir-rapport/scheurer-ensemble/'; C = '/home/claude/coffre-soir/'
PIECE = R + 'brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md'
QNOM = "la question de Jérémy Scheurer (tendance d'échelle d'un comportement désaligné)"
_c = open(P + 'soir-classeur-D-scheurer-v1.md').read(); _i = _c.find('## La question du mentor (texte exact)\n> ') + len('## La question du mentor (texte exact)\n> ')
QTEXTE = _c[_i:_c.find('\n', _i)]
NA = "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.\n"
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def liste(x): return x if isinstance(x, list) else next(v for v in x.values() if isinstance(v, list))
def ecrire(p, t): assert not os.path.exists(p), p; open(p, 'w').write(t); return sha(p)
SRC2 = S + 'source-2/source-2-course-scheurer-v1.json'; V1 = S + 'lecteur-A/fiches-normalisees-v1.json'; V2 = S + 'lecteur-A/fiches-normalisees-v2.json'
mode = sys.argv[1]
if mode == 'lecteur':
    A = S + 'lecteur-A/'; n1 = len(liste(json.load(open(V1)))); src = json.load(open(SRC2)); n2 = src['nombre']
    t = f"""Tu es le **lecteur A, suite** (normalisation et dédoublonnage) du rapport des idées sur {QNOM}, pour la candidature de Lazar Ciric à Pivotal. Un premier lecteur A a traité le tour d'un collisionneur et les fiches du matin ; tu prends sa suite pour la **course de l'organisme** (source 2) seule, avec ses règles et son format, sur ses fichiers. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 25 minutes**, et écris `fiches-normalisees-v2.json` dans les quinze premières minutes.

## Ton protocole (gelé avant toute sortie : lis-le d'abord)
- `{R}brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** sur la source 2.
- La consigne du premier lecteur A, pour le format exact des fiches et les règles : `{P}soir-lecteur-A-scheurer-v1.md`. Ce qui y est dit des cellules du tour, des espèces et des fiches du matin ne vaut pas pour la source 2.
- La question du mentor (texte exact, coupé comme dans la pièce) : « {QTEXTE} » ; pièce de référence pour le rattachement : `{PIECE}`.

## Ce qui existe déjà (le travail du premier lecteur A ; lis-le en entier avant la source 2)
Dossier `{A}` : `fiches-normalisees-v1.json` ({n1} fiches, sha256 `{sha(V1)}`), `refutees-v1.md` (`{sha(A + 'refutees-v1.md')[:8]}…`), `hors-sujet-v1.md` (`{sha(A + 'hors-sujet-v1.md')[:8]}…`). Tu ne modifies aucun de ces fichiers. N'ouvre pas `cle-provenances-v1.json`.

## Source 2 (préparée par le directeur, sans provenance)
`{SRC2}` (sha256 `{sha(SRC2)}`) : {n2} éléments `S2-01`, `S2-02`, …, chacun avec son `contenu` (titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût) : les fiches de toutes les passes de tous les proposeurs et les fusions du bisociateur de la course.{(' Non fourni : ' + '; '.join(src['non_fourni']) + '.') if src.get('non_fourni') else ''} Lis-les tous en entier.
- **Classement** : « S » si l'élément répond à la question (une proposition de recherche qui obtient une tendance d'échelle d'un comportement désaligné ou d'une capacité de contrôle, chiffrable en facteur par mois ou par an) ; sinon hors sujet.
- **Aucune objection croisée** dans cette source : `objections` et `reponses` restent vides, sauf pour une fiche fusionnée qui en avait déjà.
- **Dédoublonnage par structure**, contre les {n1} fiches existantes et entre éléments : même hypothèse et même mesure qui tue = une seule fiche. Une fusion avec une fiche existante garde le texte de la fiche existante ; un champ vide de celle-ci peut être rempli par le texte de l'élément, cité tel quel, et c'est dit dans `note_du_lecteur`.
- **Réfutée** seulement si une source citée contredit son énoncé central, ou si l'élément se contredit lui-même ; jamais par accord ou désaccord de modèles. `WebFetch` seulement pour vérifier une telle source.
- **Règle d'intégrité** : une fiche ne garde aucun mode d'emploi d'attaque ; si un élément en contient, garde l'idée de mesure et retire le détail opératoire, et dis-le dans `note_du_lecteur`.

## Ce que tu écris (versions neuves ; on n'écrase jamais)
1. `{A}fiches-normalisees-v2.json` : les {n1} fiches de la v1 (identiques, sauf les champs remplis par une fusion, dits dans `note_du_lecteur`) puis les fiches neuves, numérotées à la suite de la dernière de la v1, même format (mêmes clés), **aucune provenance**.
2. `refutees-v2.md` et `hors-sujet-v2.md` (même dossier) : ceux de la v1, plus ce que la source 2 ajoute.
3. La clé de la source 2 : `{A}cle-provenances-source-2-v1.json` : pour chaque fiche (neuve ou fusionnée) la liste de ses éléments `S2-xx`, et pour chaque élément son sort (fiche neuve, fusionné dans S-…, réfuté, hors sujet).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi. Ne lis rien sous `/home/claude/coffre-*`, ni les dossiers `pour-lazar/`, `classement-D/`, `moisson-C/`, `piste/`, `prep-v1/`, ni le dossier `scheurer-ensemble/`, ni les réponses de Lazar. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : nombre d'éléments lus ; fiches neuves et fusions ; réfutés ; hors sujet ; total des fiches de la v2 ; chemins et sha256 de tes fichiers ; tout doute sur un dédoublonnage, en une ligne chacun.
"""
    print('lecteur', ecrire(P + 'soir-lecteur-A-scheurer-source-2-v1.md', t))
elif mode == 'prep':
    taille = int(sys.argv[2]); v1 = liste(json.load(open(V1))); premier_neuf = max(int(f['id'].split('-')[1]) for f in v1) + 1
    serv1 = json.load(open(S + 'prep-v1/fiches-servies-v1.json')); debut = max(int(f['id'].split('-')[1]) for f in serv1) + 1
    cle1_p = C + 'cle-preparation-scheurer-v1.json'; cle2_p = C + 'cle-preparation-lot2-scheurer-v1.json'
    for x in (S + 'prep-v1/fiches-lot2-a-moissonner-v1.json', S + 'prep-v1/fiches-ensemble-v1.json', S + 'piste/fiches-a-grouper-ensemble-v1.json', cle2_p): assert not os.path.exists(x), x
    out = subprocess.run(['nice', '-n', '10', 'python3', '-I', '/home/claude/scratch/soir-rapport/scripts/preparer_lot2_soir_v1.py', V2, 'SC', str(premier_neuf), str(debut), S.rstrip('/'), cle1_p, cle2_p],
                         capture_output=True, text=True, timeout=60); print(out.stdout.strip(), out.stderr.strip()); assert out.returncode == 0
    for d in ('prep-v1', 'moisson-C', 'classement-D', 'piste', 'lecteur-A'): os.makedirs(E + d, exist_ok=True)
    fs = E + 'prep-v1/fiches-servies-v1.json'; shutil.copy(S + 'prep-v1/fiches-ensemble-v1.json', fs)
    gi = E + 'piste/fiches-a-grouper-v1.json'; shutil.copy(S + 'piste/fiches-a-grouper-ensemble-v1.json', gi)
    shutil.copy(V2, E + 'lecteur-A/fiches-normalisees-v1.json')
    cle = dict(json.load(open(cle1_p))['cle']); cle.update(json.load(open(cle2_p))['cle']); ids = {f['id'] for f in json.load(open(fs))}
    ce = C + 'cle-preparation-scheurer-ensemble-v1.json'; assert not os.path.exists(ce)
    json.dump({'cle': {i: ({'source': 'matin', 'ident': k['ident']} if k['source'] == 'matin' else {'source': 'tour', 'ident': k['ident']}) for i, k in cle.items() if i in ids},
               'regle': "ensemble : « tour » = fiche du lecteur A v2 (tour ou course) ; « matin » = fiche du matin"}, open(ce, 'w'), ensure_ascii=False, indent=1)
    lot2 = json.load(open(S + 'prep-v1/fiches-lot2-a-moissonner-v1.json')); parts = [lot2[k:k + taille] for k in range(0, len(lot2), taille)]
    gab = P + 'soir-moissonneur-C-gabarit-v1.md'; assert sha(gab) == open(gab + '.sha256').read().split()[0]; tpl = open(gab).read()
    for k, p in enumerate(parts, 1):
        pp = E + f'prep-v1/fiches-lot2-moisson-part-{k}-v1.json'; json.dump(p, open(pp, 'w'), ensure_ascii=False, indent=1)
        t = (tpl.replace('<<QNOM>>', QNOM).replace('<<QTEXTE>>', QTEXTE).replace('<<ENTREE>>', pp).replace('<<H_ENTREE>>', sha(pp)).replace('<<N>>', str(len(p)))
             .replace('<<MENTOR_TRAVAUX>>', f"Ses travaux sont décrits dans `{PIECE}`, section 1 (lecture permise). N'ouvre pas les autres parts ni leurs sorties.")
             .replace('<<SORTIE>>', E + f'moisson-C/moisson-lot2-part-{k}-v1.json')) + NA
        print('moissonneur', k, len(p), ecrire(P + f'soir-moissonneur-C-scheurer-lot2-part-{k}-v1.md', t))
    g = open(P + 'piste-scheurer-groupeur-aveugle-v1.md').read()
    a = "`/home/claude/scratch/soir-rapport/scheurer/piste/fiches-a-grouper-v1.json` (sha256 `9bae335ec593d5e0cd7a8431dfdf7ef3cd7ce1ca68caa6b7c15cd50788c3ef1b`)"
    b = "dossier `/home/claude/scratch/soir-rapport/scheurer/piste/`"
    for x in (a, b): assert g.count(x) == 1, x[:40]
    g = g.replace(a, f"`{gi}` (sha256 `{sha(gi)}`)").replace(b, f"dossier `{E}piste/`")
    g += NA + "Ne lis rien dans le dossier `/home/claude/scratch/soir-rapport/scheurer/` (il contient un groupement précédent d'une partie de ces fiches), ni `source-2/`, ni `/home/claude/coffre-*`.\n"
    print('groupeur', ecrire(P + 'piste-scheurer-groupeur-aveugle-ensemble-v1.md', g))
    print('ensemble', len(ids), sha(fs), '| à grouper', sha(gi), '| clé ensemble', sha(ce), '| premier neuf', premier_neuf, 'début', debut)
elif mode == 'classeur':
    fs = E + 'prep-v1/fiches-servies-v1.json'; m1 = liste(json.load(open(S + 'moisson-C/moisson-fusionnee-v1.json'))); m2 = []
    for p in sorted(glob.glob(E + 'moisson-C/moisson-lot2-part-*-v1.json')): m2 += liste(json.load(open(p)))
    mf = E + 'moisson-C/moisson-fusionnee-v1.json'; assert not os.path.exists(mf); json.dump(m1 + m2, open(mf, 'w'), ensure_ascii=False, indent=1)
    ids = {f['id'] for f in json.load(open(fs))}; idm = {e['id'] for e in m1 + m2}
    print('moisson', len(m1), '+', len(m2), '; fiches sans moisson', sorted(ids - idm), '; moisson sans fiche', sorted(idm - ids), sha(mf))
    t = open(P + 'soir-classeur-D-scheurer-v1.md').read()
    a1 = "`/home/claude/scratch/soir-rapport/scheurer/prep-v1/fiches-servies-v1.json` (sha256 `e1545f707d97912fda9b9176da1dac8c556b80ea83422c160a528e0056655cda`)"
    a2 = "`/home/claude/scratch/soir-rapport/scheurer/moisson-C/moisson-fusionnee-v1.json` (sha256 `f0c302586c9fec12a3a7a709186c8b0af4308c9c618ac091fb82464da22064a0`)"
    a3 = "`/home/claude/scratch/soir-rapport/scheurer/classement-D/`"
    for x in (a1, a2, a3): assert t.count(x) == 1, x[:60]
    t = (t.replace(a1, f"`{fs}` (sha256 `{sha(fs)}`)").replace(a2, f"`{mf}` (sha256 `{sha(mf)}`)").replace(a3, f"`{E}classement-D/`")
         .replace("Tu es le **classeur neuf** (", "Tu es le **classeur neuf** (classement de l'ensemble : tour, fiches du matin et course ; un classement précédent d'une partie existe ailleurs, tu ne le lis pas) ("))
    t += NA + "numpy 2.5.3 est installé. Écris `notes-v1.json` dans les dix premières minutes. Ne lis rien dans le dossier `/home/claude/scratch/soir-rapport/scheurer/` (classement précédent).\n"
    print('classeur', ecrire(P + 'soir-classeur-D-scheurer-ensemble-v1.md', t))
