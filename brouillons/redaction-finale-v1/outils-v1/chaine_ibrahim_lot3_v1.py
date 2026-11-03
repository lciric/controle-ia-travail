"""Ibrahim Q1, seconde course (source 3) : paquet sans provenance, consigne du lecteur A suite, lot 3 et ensemble v2
(tour, matin, première course, seconde course), consignes des moissonneurs et du groupeur aveugle, puis moisson fusionnée et consigne du classeur.
Usage : chaine_ibrahim_lot3_v1.py paquet DOSSIER_GENERATION_1 | lecteur | prep TAILLE_PART | classeur
Graines : SeedSequence (numpy), entier tiré d'un sha256 (paquet : 'source-3-permutation-v1|' + sha256(fiches.json) ; lot 3 : 16 premiers hexadécimaux du sha256 de la v3 du lecteur)."""
import hashlib, json, sys, os, glob, shutil
import numpy as np
R = '/home/claude/controle-ia-travail/'; P = R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/'
S = '/home/claude/scratch/soir-rapport/ibrahim-q1/'; E1 = '/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/'
E = '/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble-v2/'; C = '/home/claude/coffre-soir/'
PIECE = R + 'brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md'
QNOM = "la question 1 de Lujain Ibrahim"
QTEXTE = "Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading."
NOYAU = ('type', 'enonce', 'mecanisme', 'mesure_qui_tue', 'prediction', 'echec_le_plus_probable', 'cout')
NA = "\n**N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le. Toute commande : `timeout 60 nice -n 10 …`.\n"
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def liste(x): return x if isinstance(x, list) else next(v for v in x.values() if isinstance(v, list))
def noyau(f):
    x = {k: f.get(k, '') for k in NOYAU}; x['prediction'] = f.get('resultat_attendu', '') or f.get('prediction', ''); return x
def ecrire(p, t): assert not os.path.exists(p), p; open(p, 'w').write(t); return sha(p)
SRC3 = S + 'source-3/source-3-course-ibrahim-v1.json'; V2 = S + 'lecteur-A/fiches-normalisees-v2.json'; V3 = S + 'lecteur-A/fiches-normalisees-v3.json'
mode = sys.argv[1]
if mode == 'paquet':
    gen = sys.argv[2]; fp = os.path.join(gen, 'fiches.json'); fu = os.path.join(gen, 'fusions-inachevees.json')
    F = json.load(open(fp)) if os.path.exists(fp) else {}
    U = json.load(open(fu)).get('fusions', []) if os.path.exists(fu) else []
    brut = [('fiches.json', k, v.get('contenu'), v.get('meta')) for k, v in sorted(F.items())]
    brut += [('fusions-inachevees.json', str(i), (x.get('contenu') if isinstance(x, dict) and 'contenu' in x else x), (x.get('meta') if isinstance(x, dict) else None)) for i, x in enumerate(U)]
    absents = [(f, k) for f, k, c, _ in brut if c is None]; brut = [b for b in brut if b[2] is not None]
    e = int(hashlib.sha256(('source-3-permutation-v1|' + (sha(fp) if os.path.exists(fp) else 'vide')).encode()).hexdigest(), 16)
    perm = np.random.default_rng(np.random.SeedSequence(e)).permutation(len(brut)) if brut else []
    items, cle = [], {}
    for j, i in enumerate(perm, 1):
        f, k, c, m = brut[int(i)]; ident = f'S3-{j:02d}'; items.append({'item': ident, 'contenu': c}); cle[ident] = {'fichier': f, 'id': k, 'meta': m}
    out = {'source': 3, 'description': "Seconde course d'idéation de l'organisme sur la question servie : fiches de toutes les passes de tous les proposeurs et fusions inachevées du bisociateur ; sans provenance, sans sortie des juges, sans le coffre de la course.",
           'nombre': len(items), 'non_fourni': ([] if os.path.exists(fp) else ['fiches.json absent']) + [f'{f} n° {k} : contenu absent (fusion non écrite)' for f, k in absents], 'items': items}
    os.makedirs(os.path.dirname(SRC3), exist_ok=True); assert not os.path.exists(SRC3)
    json.dump(out, open(SRC3, 'w'), ensure_ascii=False, indent=1)
    cp = C + 'cle-source-3-ibrahim-q1-v1.json'; assert not os.path.exists(cp); json.dump({'cle': cle}, open(cp, 'w'), ensure_ascii=False, indent=1)
    man = {'graine_entropie': str(e), 'regle': "int(sha256('source-3-permutation-v1|' + sha256(fiches.json)), 16) → SeedSequence → default_rng → permutation", 'numpy': np.__version__,
           'entrees': {p: sha(p) for p in (fp, fu) if os.path.exists(p)}, 'sortie': sha(SRC3), 'cle': sha(cp)}
    json.dump(man, open(os.path.join(os.path.dirname(SRC3), 'manifeste-preparation-source-3-v1.json'), 'w'), ensure_ascii=False, indent=1)
    print(SRC3, man['sortie'], len(items), 'éléments ; non fourni', len(out['non_fourni']), '; clé', man['cle'])
elif mode == 'lecteur':
    A = S + 'lecteur-A/'; n2 = len(liste(json.load(open(V2)))); n3 = json.load(open(SRC3))['nombre']
    t = f"""Tu es le **lecteur A, suite** (normalisation et dédoublonnage) du rapport des idées sur {QNOM}, pour la candidature de Lazar Ciric à Pivotal. Deux lecteurs A ont déjà traité le tour d'un collisionneur, les fiches du matin et une première course de l'organisme ; tu prends leur suite pour la **seconde course de l'organisme** (source 3) seule, avec leurs règles et leur format, sur leurs fichiers. Tu n'as écrit aucune des idées ni aucun des textes. Français, sans sigle non développé ; toute heure vient de `date -u`. Échéance du dépôt ce soir : **vise 25 minutes**, et écris `fiches-normalisees-v3.json` dans les quinze premières minutes.

## Ton protocole (gelé avant toute sortie : lis-le d'abord)
- `{R}brouillons/ideation-mentors-soir-v1/protocole-rapport-mentors-soir-v1.md` (sha256 `fbbbb5208e62232aa8230f3f036260649d571a1c910773b4539977e70ca5b347`) : tu fais **l'étape A** sur la source 3.
- La consigne du premier lecteur A, pour le format exact des fiches et les règles : `{P}soir-lecteur-A-ibrahim-q1-v1.md`. Ce qui y est dit des cellules du tour, des espèces et des fiches du matin ne vaut pas pour la source 3.
- La question de la mentore (texte exact) : « {QTEXTE} » ; pièce de référence pour le rattachement : `{PIECE}`.

## Ce qui existe déjà (lis-le en entier avant la source 3)
Dossier `{A}` : `fiches-normalisees-v2.json` ({n2} fiches, sha256 `{sha(V2)}`), `refutees-v2.md` (`{sha(A + 'refutees-v2.md')[:8]}…`), `hors-sujet-v2.md` (`{sha(A + 'hors-sujet-v2.md')[:8]}…`). Tu ne modifies aucun de ces fichiers. N'ouvre aucun fichier `cle-provenances-*`.

## Source 3 (préparée par le directeur, sans provenance)
`{SRC3}` (sha256 `{sha(SRC3)}`) : {n3} éléments `S3-01`, `S3-02`, …, chacun avec son `contenu` (titre, axe, hypothèse, prédiction, épreuve, contrôle, test de mort, coût) : les fiches de toutes les passes de tous les proposeurs et les fusions du bisociateur de la seconde course. Lis-les tous en entier.
- **Classement** : « I » si l'élément répond à la question (une première expérience sur l'un des deux projets de la mentore : ce qu'on entraîne ou mesure, le résultat attendu, une chose qui rendrait le résultat trompeur) ; sinon hors sujet.
- **Aucune objection croisée** dans cette source : `objections` et `reponses` restent vides, sauf pour une fiche fusionnée qui en avait déjà.
- **Dédoublonnage par structure**, contre les {n2} fiches existantes et entre éléments : même hypothèse et même mesure qui tue = une seule fiche. Une fusion avec une fiche existante garde le texte de la fiche existante ; un champ vide de celle-ci peut être rempli par le texte de l'élément, cité tel quel, et c'est dit dans `note_du_lecteur`.
- **Réfutée** seulement si une source citée contredit son énoncé central, ou si l'élément se contredit lui-même ; jamais par accord ou désaccord de modèles. `WebFetch` seulement pour vérifier une telle source.

## Ce que tu écris (versions neuves ; on n'écrase jamais)
1. `{A}fiches-normalisees-v3.json` : les {n2} fiches de la v2 (identiques, sauf les champs remplis par une fusion, dits dans `note_du_lecteur`) puis les fiches neuves, numérotées à la suite de la dernière de la v2, même format (mêmes clés), **aucune provenance**.
2. `refutees-v3.md` et `hors-sujet-v3.md` (même dossier) : ceux de la v2, plus ce que la source 3 ajoute.
3. La clé de la source 3 : `{A}cle-provenances-source-3-v1.json` : pour chaque fiche (neuve ou fusionnée) la liste de ses éléments `S3-xx`, et pour chaque élément son sort (fiche neuve, fusionné dans I-…, réfuté, hors sujet).

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git` ; aucun appel de modèle autre que toi. Ne lis rien sous `/home/claude/coffre-*`, ni les dossiers `pour-lazar/`, `classement-D/`, `moisson-C/`, `piste/`, `prep-v1/`, ni les dossiers `ibrahim-q1-ensemble*`, ni les réponses de Lazar. Toute commande : `timeout 60 nice -n 10 …`. **N'attends aucune approbation** : si un outil en demande une, renonce à l'appel et note-le.

## Rendu
Réponse finale : nombre d'éléments lus ; fiches neuves et fusions ; réfutés ; hors sujet ; total des fiches de la v3 ; chemins et sha256 de tes fichiers ; tout doute sur un dédoublonnage, en une ligne chacun.
"""
    print('lecteur', ecrire(P + 'soir-lecteur-A-ibrahim-q1-source-3-v1.md', t))
elif mode == 'prep':
    taille = int(sys.argv[2]); v2 = liste(json.load(open(V2))); v3 = liste(json.load(open(V3))); v3d = {f['id']: f for f in v3}
    premier_neuf = max(int(f['id'].split('-')[1]) for f in v2) + 1
    neuves = [f for f in v3 if int(f['id'].split('-')[1]) >= premier_neuf and f.get('statut') == 'gardée' and f.get('classement') not in ('hors sujet', ['hors sujet'])]
    ens1 = json.load(open(E1 + 'prep-v1/fiches-servies-v1.json')); debut = max(int(f['id'].split('-')[1]) for f in ens1) + 1
    graine = int(sha(V3)[:16], 16); perm = np.random.default_rng(np.random.SeedSequence(graine)).permutation(len(neuves))
    lot3, cle3 = [], {}
    for r, i in enumerate(perm, debut):
        f = neuves[i]; nid = f'IB-{r:02d}'; lot3.append(dict(id=nid, **noyau(f))); cle3[nid] = {'source': 'seconde-course', 'ident': f['id']}
    cp = C + 'cle-preparation-lot3-ibrahim-q1-v1.json'; assert not os.path.exists(cp)
    json.dump({'cle': cle3, 'regle': f'IB-{debut} et suivants = rang dans la permutation du lot 3', 'graine': str(graine), 'numpy': np.__version__}, open(cp, 'w'), ensure_ascii=False, indent=1)
    cle = dict(json.load(open(C + 'cle-preparation-ibrahim-q1-v1.json'))['cle']); cle.update(json.load(open(C + 'cle-preparation-lot2-ibrahim-q1-v1.json'))['cle'])
    ens, maj = [], []
    for f in ens1:
        k = cle[f['id']]
        if k['source'] in ('tour', 'tour-course'):
            g = dict(id=f['id'], **noyau(v3d[k['ident']])); ens.append(g)
            if g != f: maj.append(f['id'])
        else: ens.append(f)
    ens += lot3
    for d in ('prep-v1', 'moisson-C', 'classement-D', 'piste', 'lecteur-A'): os.makedirs(E + d, exist_ok=True)
    # clé de l'ensemble pour la règle de piste (comme l'ensemble v1) : toute fiche venue du lecteur A = « tour » (fiche lue dans la v3), le matin inchangé
    cle.update(cle3); ce = C + 'cle-preparation-ibrahim-q1-ensemble-v2.json'; assert not os.path.exists(ce)
    json.dump({'cle': {i: ({'source': 'matin', 'ident': k['ident']} if k['source'] == 'matin' else {'source': 'tour', 'ident': k['ident']}) for i, k in cle.items() if i in {f['id'] for f in ens}},
               'regle': "ensemble v2 : « tour » = fiche du lecteur A v3 (tour, première ou seconde course) ; « matin » = fiche du matin"}, open(ce, 'w'), ensure_ascii=False, indent=1)
    shutil.copy(V3, E + 'lecteur-A/fiches-normalisees-v1.json')
    pl = E + 'prep-v1/fiches-lot3-a-moissonner-v1.json'; json.dump(lot3, open(pl, 'w'), ensure_ascii=False, indent=1)
    fs = E + 'prep-v1/fiches-servies-v1.json'; json.dump(ens, open(fs, 'w'), ensure_ascii=False, indent=1)
    gi = E + 'piste/fiches-a-grouper-v1.json'; json.dump([{'id': f['id'], 'enonce': f['enonce'], 'mecanisme': f['mecanisme']} for f in ens], open(gi, 'w'), ensure_ascii=False, indent=1)
    parts = [lot3[k:k + taille] for k in range(0, len(lot3), taille)]
    tpl = open(P + 'soir-moissonneur-C-gabarit-v1.md').read(); assert sha(P + 'soir-moissonneur-C-gabarit-v1.md') == open(P + 'soir-moissonneur-C-gabarit-v1.md.sha256').read().split()[0]
    for k, p in enumerate(parts, 1):
        pp = E + f'prep-v1/fiches-lot3-moisson-part-{k}-v1.json'; json.dump(p, open(pp, 'w'), ensure_ascii=False, indent=1)
        t = (tpl.replace('<<QNOM>>', QNOM).replace('<<QTEXTE>>', QTEXTE).replace('<<ENTREE>>', pp).replace('<<H_ENTREE>>', sha(pp)).replace('<<N>>', str(len(p)))
             .replace('<<MENTOR_TRAVAUX>>', f"Ses travaux et ses deux projets sont décrits dans `{PIECE}`, section 1 (lecture permise). N'ouvre pas les autres parts ni leurs sorties.")
             .replace('<<SORTIE>>', E + f'moisson-C/moisson-lot3-part-{k}-v1.json')) + NA
        print('moissonneur', k, len(p), ecrire(P + f'soir-moissonneur-C-ibrahim-q1-lot3-part-{k}-v1.md', t))
    g = open(P + 'piste-ibrahim-q1-groupeur-aveugle-ensemble-v1.md').read()
    a = "`/home/claude/scratch/soir-rapport/ibrahim-q1/piste/fiches-a-grouper-ensemble-v1.json` (sha256 `e3afb86950d457411d1d989635ed63ebb5ea34b6264bc1b30a172ad1dc267c81`)"
    b = "## Ce que tu écris (fichiers neufs, dossier `/home/claude/scratch/soir-rapport/ibrahim-q1/piste/`)"
    c = "Ne lis rien d'autre que le fichier d'entrée (ni `groupes-v1.*`, groupement précédent d'une partie de ces fiches ; surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, ni `/home/claude/coffre-*`)."
    for x in (a, b, c): assert g.count(x) == 1, x[:40]
    g = (g.replace(a, f"`{gi}` (sha256 `{sha(gi)}`)").replace(b, f"## Ce que tu écris (fichiers neufs, dossier `{E}piste/`)")
         .replace("`groupes-ensemble-v1.json`", "`groupes-v1.json`").replace("`groupes-ensemble-v1.md`", "`groupes-v1.md`")
         .replace(c, "Ne lis rien d'autre que le fichier d'entrée (ni les dossiers `ibrahim-q1/` et `ibrahim-q1-ensemble/`, qui contiennent des groupements précédents d'une partie de ces fiches ; surtout pas `classement-D/`, `moisson-C/`, `prep-v1/`, `lecteur-A/`, `source-3/`, ni `/home/claude/coffre-*`).")) + NA
    print('groupeur', ecrire(P + 'piste-ibrahim-q1-groupeur-aveugle-ensemble-v2.md', g))
    print('lot3', len(lot3), 'premier neuf', premier_neuf, 'début', debut, '| ensemble', len(ens), sha(fs), '| mis à jour depuis la v3', maj, '| à grouper', sha(gi), '| clé', sha(cp), '| graine', graine)
elif mode == 'classeur':
    fs = E + 'prep-v1/fiches-servies-v1.json'; m1 = liste(json.load(open(E1 + 'moisson-C/moisson-fusionnee-v1.json'))); m3 = []
    for p in sorted(glob.glob(E + 'moisson-C/moisson-lot3-part-*-v1.json')): m3 += liste(json.load(open(p)))
    mf = E + 'moisson-C/moisson-fusionnee-v1.json'; assert not os.path.exists(mf); json.dump(m1 + m3, open(mf, 'w'), ensure_ascii=False, indent=1)
    ids = {f['id'] for f in json.load(open(fs))}; idm = {e['id'] for e in m1 + m3}
    print('moisson', len(m1), '+', len(m3), '; fiches sans moisson', sorted(ids - idm), '; moisson sans fiche', sorted(idm - ids), sha(mf))
    t = open(P + 'soir-classeur-D-ibrahim-q1-ensemble-v1.md').read()
    a1 = "`/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/prep-v1/fiches-servies-v1.json` (sha256 `b77b8c5fa07069de944171bdd07ace2c509a117ebd3d83f1c199685c3c94a9e1`)"
    a2 = "`/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/moisson-C/moisson-fusionnee-v1.json` (sha256 `21021ef70d0c4e398111dacd1fed514a6cd08f8cbc6f84a306491d8e57ec04ac`)"
    a3 = "`/home/claude/scratch/soir-rapport/ibrahim-q1-ensemble/classement-D/`"
    for x in (a1, a2, a3): assert t.count(x) == 1, x[:60]
    t = (t.replace(a1, f"`{fs}` (sha256 `{sha(fs)}`)").replace(a2, f"`{mf}` (sha256 `{sha(mf)}`)").replace(a3, f"`{E}classement-D/`")
         .replace("tour, fiches du matin et course ;", "tour, fiches du matin et deux courses ;"))
    t += NA + "numpy 2.5.3 est installé. Écris `notes-v1.json` dans les dix premières minutes. Ne lis rien dans les dossiers `ibrahim-q1/` et `ibrahim-q1-ensemble/` (classements précédents).\n"
    print('classeur', ecrire(P + 'soir-classeur-D-ibrahim-q1-ensemble-v2.md', t))
