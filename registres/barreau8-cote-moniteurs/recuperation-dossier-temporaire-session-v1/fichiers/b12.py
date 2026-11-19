import pathlib, sys, hashlib, subprocess, re
R = pathlib.Path('/home/user/controle-ia-travail')
D = R/'brouillons/barreau8-lecture-sondes-v1'
B11 = D/'prereg-lecture-sondes-barreau8-v1-brouillon11.md'
P = D/'prereg-lecture-sondes-barreau8-v1-brouillon12.md'
N = D/'differences-brouillon11-brouillon12-v1.md'
assert not P.exists() and not N.exists()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
H11 = '32c6da0125e3280e5b15316947f768da5025499613e9be8c97c0f2fb6e08fdf7'
assert sha(B11) == H11
CL11 = 'brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon11-v1.md'; HC11 = '48480a70c25190696c01326641b6b7d5e323551bae5117df38089714f6cec823'
assert sha(R/CL11) == HC11
V6 = R/'docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md'
assert sha(V6) == '20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1'
note = V6.read_text(encoding='utf-8')
EMP = {}
for nom in ('config.json', 'generation_config.json', 'tokenizer.json', 'tokenizer_config.json'):
    m = re.findall(r'(?<![a-z_])`' + re.escape(nom) + r'` `([0-9a-f]{64})`', note)
    assert len(m) == 1, (nom, m); EMP[nom] = m[0]
t = B11.read_text(encoding='utf-8'); L0 = t.splitlines(); fautes = []
assert EMP['tokenizer_config.json'] in t   # déjà citée par la garde P3 (b) : même valeur
i0 = next(i for i,l in enumerate(L0) if l.startswith('**Noms et champs, liste fermée**')); i1 = next(i for i,l in enumerate(L0) if l.startswith('**Fichiers non lus avant**'))
BLOC = "\n".join(L0[i0:i1]); F3 = L0[75]
def r(a, b):
    global t
    c = t.count(a)
    if c != 1: fautes.append((c, a[:90])); return
    t = t.replace(a, b)
def ligne(prefixe, neuve):
    global t
    Ls = t.split("\n"); k = [i for i,l in enumerate(Ls) if l.startswith(prefixe)]
    if len(k) != 1: fautes.append(('ligne', len(k), prefixe)); return
    Ls[k[0]] = neuve; t = "\n".join(Ls)
ECART = "après le scellement, aucun défaut n'échoit et tout changement est un écart au préenregistrement, nœud de Lazar"
DEBUT = '2026-11-19T03:36Z'
# ---------- en-tête
r("— v1 — brouillon 11", "— v1 — brouillon 12")
r("**Statut : brouillon 11, texte soumis au scellement", "**Statut : brouillon 12, texte soumis au scellement")
r("contre-lecteur du brouillon 10 : désigné par la conductrice (section", "contre-lecteur du brouillon 10 : désigné par la conductrice ; contre-lecteur du brouillon 11 : Opus 5.5 (section")
r("brouillon 11 écrit entre 2026-11-19T03:04Z et 2026-11-19T03:07Z (`date -u`).", "brouillon 11 écrit entre 2026-11-19T03:04Z et 2026-11-19T03:07Z ; brouillon 12 écrit entre " + DEBUT + " et HEURE_DE_FIN (`date -u`).")
r("comparée par programme à celle de la version 1 : identique ; c'est la ligne de registre du code qui fait foi sur la version) ;", "comparée par programme à celle de la version 1 : identique ; le code de la lecture est en version 2 ; c'est la ligne de registre de chaque code qui fait foi sur sa version) ; contre-lecture du brouillon 11, lue en entier (remarques, simulation sur données synthétiques et texte de remplacement de l'essai de la chaîne), `" + CL11 + "` — `" + HC11 + "` ;")
# ---------- N-1
r("le seul nombre qu'elle écrit est le repère r8, agrégat sur toutes les conditions confondues", "hors des comptes, des tailles et des empreintes qu'une cause de refus peut porter, le seul nombre qu'elle écrit est le repère r8, agrégat sur toutes les conditions confondues")
r("La commande de réception seule peut être jouée par la conductrice du côté des moniteurs ou par le lecteur des sondes, dès que la ligne `LIVRAISON-PASSE-IIB` est inscrite, sans attendre les autres conditions du plan, point 3 ; elle n'écrit que « tenue », ou le refus et sa cause, et le repère r8", "La commande de réception seule peut être jouée par la conductrice du côté des moniteurs ou par le lecteur des sondes, dès que les lignes `SCELLEMENT-SONDES-IIB`, `CODE-LECTURE-SONDES-IIB` et `LIVRAISON-PASSE-IIB` sont inscrites, sans attendre les autres conditions du plan, point 3 ; avant d'ouvrir quoi que ce soit de la livraison, elle exige, comme la lecture, ce texte scellé à l'empreinte de sa ligne et des modules chargés exactement ceux du bordereau du code de la lecture, aux mêmes empreintes (D-2), sinon elle refuse ; elle n'écrit que « tenue », ou le refus et sa cause, et le repère r8 ; aucune cause de refus ne porte un score d'action ou de jeton, ni un écart entre un score livré et un score recalculé")
r("`CODE-LECTURE-SONDES-IIB` : strictement postérieure à `SCELLEMENT-SONDES-IIB`, **avant toute lecture**.", "`CODE-LECTURE-SONDES-IIB` : strictement postérieure à `SCELLEMENT-SONDES-IIB`, **avant toute lecture et avant toute réception de la livraison**.")
# ---------- N-2
r("l'invite publiée de la recette de la question (6), `H1-classification` sous `docs/sources/invites-2606.08892-v1/`,", "l'invite publiée de la recette de la question (6), `H1-classification`, et l'index des invites publiées, avec leurs compagnons, sous `docs/sources/invites-2606.08892-v1/`,")
# ---------- N-3
r("ou si une sonde des couches 7 ou 23 est trouvée sous son nom mais non conforme**)", "ou si une sonde des couches 7 ou 23 est trouvée sous son nom mais non conforme, ou y paraît plus d'une fois, ou si un vecteur ou un biais d'une sonde ou d'une direction n'est pas fini**)")
r("ou si l'état d'une sonde à la réception diffère de celui de la trace de la passe.", "ou si l'état d'une sonde à la réception diffère de celui de la trace de la passe, ou si un vecteur ou un biais d'une sonde ou d'une direction n'est pas fini, ou si un nom de sonde des couches 7 ou 23 paraît plus d'une fois dans l'index.")
r("| 8 | fichier de sonde ou de plancher absent, d'empreinte différente ou sans compagnon conforme ; état d'une sonde à la réception différent de celui de la trace |", "| 8 | fichier de sonde ou de plancher absent, d'empreinte différente ou sans compagnon conforme ; état d'une sonde à la réception différent de celui de la trace ; vecteur ou biais non fini ; nom de sonde des couches 7 ou 23 en double dans l'index |")
# ---------- O-2
r("les quatre fichiers de configuration de la révision à leurs empreintes ;", "les quatre fichiers de configuration de la révision à leurs empreintes (note d'interface, version 6, question (1) : `config.json` `" + EMP['config.json'] + "` ; `generation_config.json` `" + EMP['generation_config.json'] + "` ; `tokenizer.json` `" + EMP['tokenizer.json'] + "` ; `tokenizer_config.json` `" + EMP['tokenizer_config.json'] + "`) ;")
# ---------- forme (A) de l'essai de la chaîne
r("(tâches étiquetées, jeton injecté, permutation)", "(actions étiquetées, jeton injecté, permutation)")
ligne("- (i) **Cas sain.**", "- (i) **Cas sain.** Il n'y a qu'un épisode `H` par tâche (I-8) : **dans chaque tâche, cinq des dix actions de cet épisode reçoivent l'étiquette 1 et les cinq autres l'étiquette 0** (déclaré « apparié dans la tâche » : comme dans les jeux de la lecture, chaque tâche porte les deux classes). Tirage : le générateur neuf de la graine `sain/<sonde>` tire, tâche par tâche dans l'ordre du tri des chaînes de Python des identifiants de tâche, une permutation des rangs de pas 0 à 9 (`permutation(10)`) ; les rangs des cinq premières positions de la permutation reçoivent l'étiquette 1. Les étiquettes sont tirées sur les dix actions, avant le retrait des actions sans jeton noté, qui sortent ensuite des deux classes. Le score d'action de la sonde est le maximum, recalculé par le code de la lecture, de ses scores par jeton livrés. Aucune sonde ne doit être au-dessus.")
ligne("- (iii) **Artefact d'alignement.**", "- (iii) **Artefact d'alignement.** Sur les données de (ii), les clés d'action des scores par jeton de la sonde sont permutées **entre toutes les actions de `H`, toutes tâches confondues** (une permutation tirée par la graine `alignement/<sonde>`), les étiquettes restant en place : les scores injectés quittent les actions étiquetées 1, dans la tâche comme entre tâches. La sonde ne doit plus être au-dessus.")
ligne("- **Limite déclarée de l'artefact positif (ii), règle inchangée.**", "- **Limite déclarée de l'essai.** Les étiquettes sont tirées au hasard dans chaque tâche : le rang du pas et la longueur du contexte sont équilibrés entre les deux classes en espérance seulement ; leur déséquilibre de tirage touche la sonde et les 800 directions de la même façon, et l'essai ne compare aucun prédicteur trivial. L'essai ne lit que `H` : un désalignement entre conditions n'est pas son objet. Quand l'artefact positif (ii) échoue, la sortie écrit pour chaque sonde l'aire de l'artefact et le quantile 0,95 du plancher sur le jeu de l'essai, sans autre effet ; un échec de (ii) n'ouvre aucun rejeu. Forme écartée, déclarée : l'étiquetage de tâches entières (brouillons 1 à 11), sous lequel des directions aléatoires séparent la moitié de tâches tirée quand l'activité dépend de la tâche (vu à tailles réduites par la contre-lecture du code de la lecture ; simulé par la contre-lecture du brouillon 11), et qui ne voit pas un décalage des scores à l'intérieur d'un épisode.")
# (b-5) : le retour à (a) garde la forme (A)
r("le chapeau, (i), (ii) et (iii) reprennent leur forme du brouillon 4 (essai sur les scores d'action), la phrase « Les actions sans jeton noté n'y entrent pas. » restant à la fin du chapeau ;", "**l'étiquetage reste celui de la forme (A) du présent texte**, et seuls changent les passages qui supposent les scores par jeton : au chapeau, « Il est défini sur les scores par jeton livrés des sondes (option (b)) : il éprouve la chaîne à partir de ces scores (agrégation par le maximum, étiquettes, clés, aire, plancher, intervalle) ; le produit scalaire, fait sur la carte, est éprouvé par » devient « Il est défini sur les scores d'action livrés : il éprouve la chaîne à partir de ces scores (étiquettes, clés, aire, plancher, intervalle) ; le produit scalaire et l'agrégation par le maximum, faits sur la carte, sont éprouvés par », et « jeton injecté » sort de la liste des tirages ; en (i), la phrase « Le score d'action de la sonde est le maximum, recalculé par le code de la lecture, de ses scores par jeton livrés. » est retirée ; (ii) devient « Mêmes étiquettes que (i). Le score d'action livré de la sonde est augmenté de 2 s pour chaque action étiquetée 1, s étant l'écart-type (de population, diviseur n) des scores d'action de la sonde sur `H` ; les scores des 800 directions du plancher ne sont pas touchés. La sonde doit être au-dessus. » ; en (iii), « des scores par jeton de la sonde » devient « des scores d'action de la sonde » ; tout le reste de l'essai, la phrase « Les actions sans jeton noté n'y entrent pas. » et la limite déclarée comprises, est inchangé ;")
# bloc de décision
r("**Le texte est scellé sous (b)** ; " + ECART + ".\n\n## Qui lit, qui juge", "**Le texte est scellé sous (b)** ; " + ECART + """.

**Décision appliquée par anticipation : la forme de l'essai de la chaîne de lecture** (accordée par la session mère si la simulation la confirmait, ce qu'elle fait ; Lazar peut la changer d'un mot avant le scellement).
- **Décision** : quelle forme d'étiquetage l'essai de la chaîne de lecture (cas sain, artefact positif, alignement) emploie sur les épisodes de `H`.
- **Enjeu** : un essai qui peut rendre toute la lecture « non concluante » (ligne L5) par le seul tirage de ses étiquettes, ou qui ne voit pas un désalignement à l'intérieur d'un épisode, n'éprouve pas la chaîne qui servira.
- **(A), scellée** : dans chaque tâche, cinq des dix actions de l'épisode de `H` reçoivent l'étiquette 1 (section « Critères de lecture gelés », essai A0). Avantage : la structure des jeux de la lecture (chaque tâche porte les deux classes) ; marge stable ; voit un décalage d'un pas dans l'épisode. Inconvénient : rang du pas et longueur du contexte équilibrés en espérance seulement (limite déclarée de l'essai).
- **(R), non retenue** : une moitié de tâches entières reçoit l'étiquette 1 (brouillons 1 à 11). Avantage : aucun changement. Inconvénient : des directions aléatoires séparent la moitié tirée quand l'activité dépend de la tâche ; un échec n'y distingue pas le tirage d'une chaîne cassée.
- **Raison** (données synthétiques seulement ; fréquences de la contre-lecture du brouillon 11, `""" + CL11 + "`, `" + HC11 + """`, « Point 6 », « Simulation ») : aux tailles de la course, aucune des deux formes n'échoue sur une chaîne saine tant que les directions sont indépendantes (0 échec sur 25 répétitions à chaque force de l'effet de tâche, sous les deux formes), mais la marge de la forme (R) s'effondre avec l'effet de tâche (plus petite borne basse de D de l'artefact : de 0,317 sans effet de tâche à 0,051 pour un effet de tâche de quatre fois l'écart-type du bruit) et un échec y paraît avec des directions corrélées (1 sur 25). La forme (A) garde une marge stable (plus petite borne basse entre 0,32 et 0,36 dans toutes les cases) et voit un décalage d'un pas dans l'épisode (vu 25 fois sur 25), que la forme (R) ne voit jamais (0 fois sur 25).
- **Recommandation** : (A), confiance 0,8 (celle du contre-lecteur du brouillon 11). **Le texte est scellé sous (A)** ; """ + ECART + """.

## Qui lit, qui juge""")
# ---------- six précisions du développeur de la lecture
r("ne figure pas ainsi dans le texte scellé**), une graine dérivée par clé", "ne figure pas ainsi dans le texte scellé** ; au scellement, la cellule « état et raison » de F-3 ne porte que l'entier, en décimal, sans séparateur ni autre mot), une graine dérivée par clé")
r("`repetabilite-passe`, `injection-adaptateurs`. Toutes consignées au manifeste.", "`repetabilite-passe`, `injection-adaptateurs`. Toutes consignées au manifeste : la lecture ne consigne à son manifeste que ses propres clés et celle de la recette de puissance ; les clés de la passe sont consignées par la passe.")
r("L'audit est écrit et scellé avant le verdict.", "L'audit est écrit et scellé avant le verdict. L'audit s'ouvre au moins une seconde après l'inscription de la ligne `LECTURE-SONDES-IIB`.")
r("désigne celles du bordereau que la ligne cite.", "désigne celles du bordereau que la ligne cite. Le bordereau du code est écrit par la même forme de lancement que la commande qu'il couvre (`python -m`). La lecture ne lit du bordereau du code de la passe que ses sept clés et ses modules (nom et empreinte ; le champ de chemin est une chaîne non vide, sans autre exigence) ; rapport, notice et devis de la passe sont contrôlés par la passe.")
r("sinon refus ; « un chemin privé lu » vaut « non » ;", "sinon refus ; des deux valeurs de la course portées par la trace (nom de la course, commit de lancement), la lecture contrôle le type seulement, et elles sont recopiées en tête de la sortie ; « un chemin privé lu » vaut « non » ;")
# ---------- contre-lecture
r("cette différence reste à contre-lire (entrée 4).", "cette différence est contre-lue par l'entrée 3 septies.")
r("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR", "- **Contre-lecture 3 septies** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 10 au brouillon 11. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon11.md`, empreinte `" + H11 + "`. Rapport : `" + CL11 + "`, empreinte `" + HC11 + "`. Conclusion : « PAS PRÊT » sur une liste fermée (N-1, bloquante ; N-2, à corriger ; N-3, mineure) ; les seize points sont dits portés, sans changement de fond ; avis sur la décision de plan : forme (A) de l'essai de la chaîne, confiance 0,8, sur simulation. Traitement : `brouillons/barreau8-lecture-sondes-v1/differences-brouillon11-brouillon12-v1.md` (empreinte dans son compagnon) ; cette différence reste à contre-lire (entrée 4).\n- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR")
h = subprocess.run(['date','-u','+%Y-%m-%dT%H:%MZ'],capture_output=True,text=True).stdout.strip()
r("HEURE_DE_FIN", h)
for c in ("À REMPLIR — À FIXER : tirée par la session mère au scellement", "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :", "versée avec l'empreinte du texte scellé."):
    if t.count(c) != 1: fautes.append(('unicité', t.count(c), c))
if t.count("À REMPLIR") != 2: fautes.append(('marqueurs', t.count("À REMPLIR")))
L1 = t.splitlines()
if L1[75] != F3: fautes.append(('F-3 changée',))
j0 = next(i for i,l in enumerate(L1) if l.startswith('**Noms et champs, liste fermée**')); j1 = next(i for i,l in enumerate(L1) if l.startswith('**Fichiers non lus avant**'))
if "\n".join(L1[j0:j1]) != BLOC: fautes.append(('bloc Noms et champs changé',))
for mot in ("non apparié", "moitié des 64 tâches"):
    if mot in t: fautes.append(('reste', mot))
if fautes:
    for f in fautes: print("FAUTE", f)
    sys.exit(1)
P.write_text(t if t.endswith("\n") else t + "\n", encoding='utf-8')
corps = pathlib.Path('/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/diff1112-corps.md').read_text(encoding='utf-8')
N.write_text(corps.replace('@@DEBUT@@', DEBUT).replace('@@FIN@@', h), encoding='utf-8')
print("ok", h, len(L1), EMP)
