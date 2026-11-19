import pathlib, sys, hashlib, subprocess
R = pathlib.Path('/home/user/controle-ia-travail')
D = R/'brouillons/barreau8-lecture-sondes-v1'
B13 = D/'prereg-lecture-sondes-barreau8-v1-brouillon13.md'
P = D/'prereg-lecture-sondes-barreau8-v1-brouillon14.md'
N = D/'differences-brouillon13-brouillon14-v1.md'
assert not P.exists() and not N.exists()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
H13 = '7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4'
assert sha(B13) == H13
CL13 = 'brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon13-v1.md'; HC13 = 'a723e7d91b8d4cf2c485598e24e49123359725f932b7b81b27e4e935a137575d'
INT = 'docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-codes-passe-v5-lecture-v4-integration-v1.md'; HINT = 'c08e1ffb168454f44fb6f277423fe8e3d264ef24f2aa91d6e301cb5aa91cd1d4'
assert sha(R/CL13)==HC13 and sha(R/INT)==HINT
t = B13.read_text(encoding='utf-8'); L0 = t.splitlines(); fautes = []
i0 = next(i for i,l in enumerate(L0) if l.startswith('**Noms et champs, liste fermée**')); i1 = next(i for i,l in enumerate(L0) if l.startswith('**Fichiers non lus avant**'))
BLOC = "\n".join(L0[i0:i1]); F3 = L0[75]
def r(a, b):
    global t
    c = t.count(a)
    if c != 1: fautes.append((c, a[:90])); return
    t = t.replace(a, b)
DEBUT = '2026-11-19T04:49Z'
T2 = "L'égalité des deux chemins n'éprouve pas le champ `rang` lui-même : la garde de réception r5 exige qu'il soit le rang de l'action dans l'ordre du fichier."
T3 = "Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués."
PHRASE_B2 = "**Pour les neuf sondes, les scores par jeton sont livrés aussi : la garde de réception r7 recalcule leur maximum et leur moyenne sur toutes les actions.**"
assert t.count(PHRASE_B2) == 1
# ---------- en-tête
r("— v1 — brouillon 13", "— v1 — brouillon 14")
r("**Statut : brouillon 13, texte soumis au scellement", "**Statut : brouillon 14, texte soumis au scellement")
r("contre-lecteur du brouillon 12 : Opus 5.5 (section", "contre-lecteur du brouillon 12 : Opus 5.5 ; contre-lecteur du brouillon 13 : Opus 5.5 (section")
r("brouillon 13 écrit entre 2026-11-19T04:24Z et 2026-11-19T04:26Z (`date -u`).", "brouillon 13 écrit entre 2026-11-19T04:24Z et 2026-11-19T04:26Z ; brouillon 14 écrit entre " + DEBUT + " et HEURE_DE_FIN (`date -u`).")
r("sont passés depuis en version 4, sans changement", "sont passés depuis en version 5, sans changement")
r("le code de la lecture est en version 3 ; c'est la ligne de registre de chaque code qui fait foi sur sa version) ;", "le code de la lecture est en version 4 ou suivante ; c'est la ligne de registre de chaque code qui fait foi sur sa version) ; contre-lecture du brouillon 13, lue en entier, `" + CL13 + "` — `" + HC13 + "` ; contre-lecture des deux codes (passe version 5, lecture version 4) et troisième essai d'intégration, lue en entier, `" + INT + "` — `" + HINT + "` ;")
# ---------- R-1, R-2 (mot pour mot)
r("est retiré de la règle d'échec ; tout le reste de l'essai", "est retiré de la règle d'échec ; en (i), « l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b) » devient « l'essai n'échoue que par (a) ou (b) » ; tout le reste de l'essai")
r("n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi.", "n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi ; les copier, les déposer, les transmettre et en calculer l'empreinte, sans en décoder le contenu, n'est pas les ouvrir au sens de cette phrase (comme une pièce dont seules l'existence et l'empreinte sont contrôlées n'est pas ouverte : plan, point 3).")
# ---------- O-6 : citation de (b-2) rendue exacte
r("la phrase « Pour les neuf sondes, les scores par jeton sont livrés aussi … sur toutes les actions. » est retirée ;", "la phrase « " + PHRASE_B2 + " » est retirée ;")
# ---------- T-1, T-4
r("sur toute entrée de l'index qui porte le nom de l'une des neuf sondes nommées, et sur toute direction candidate", "sur toute entrée qui porte le nom de l'une des neuf sondes nommées, dans l'index de chacun des trois fichiers de sondes et de planchers, et sur toute direction candidate")
r("et un nom de sonde des couches 7 ou 23 qui paraît plus d'une fois dans l'index, ne rendent pas", "et un nom de sonde des couches 7 ou 23 qui paraît plus d'une fois dans l'index de son fichier, ne rendent pas")
r("ou si un nom de sonde des couches 7 ou 23 paraît plus d'une fois dans l'index. Elle refuse aussi", "ou si un nom de sonde des couches 7 ou 23 paraît plus d'une fois dans l'index de son fichier. Elle refuse aussi")
r("est trouvée sous son nom mais non conforme, ou y paraît plus d'une fois, ou si", "est trouvée sous son nom mais non conforme, ou paraît plus d'une fois dans l'index de son fichier, ou si")
r("nom de sonde des couches 7 ou 23 en double dans l'index |", "nom de sonde des couches 7 ou 23 en double dans l'index de son fichier |")
# ---------- T-3, T-2 (après la phrase de l'égalité), et leur retrait au retour (b-5)
r("et la sortie écrit la sonde et le nombre d'actions inégales, jamais un score. Pour chaque essai,", "et la sortie écrit la sonde et le nombre d'actions inégales, jamais un score. " + T3 + " " + T2 + " Pour chaque essai,")
r("devient « l'essai n'échoue que par (a) ou (b) » ; tout le reste de l'essai", "devient « l'essai n'échoue que par (a) ou (b) » ; les deux phrases qui suivent celle de l'égalité, « " + T3 + " » et « " + T2 + " », sont retirées ; tout le reste de l'essai")
# r5 : l'exigence que T-2 nomme
r("- (r5) cohérence : 2 560 actions ; 64 tâches ;", "- (r5) cohérence : 2 560 actions, le champ `rang` de chaque ligne de l'index étant le rang de cette ligne dans le fichier, à partir de 0 ; 64 tâches ;")
# ---------- C : fait transmis sur les deux champs run_id
r("à l'ouverture de la lecture, qui refuse de tourner s'ils diffèrent (plan, point 3) ; elle est recopiée", "à l'ouverture de la lecture, qui refuse de tourner s'ils diffèrent (plan, point 3 ; fait transmis par la session mère, d'après le côté exposé, non vérifiable par le côté des moniteurs, et qui ne change rien à la règle : les deux champs `run_id` — celui de l'extrait du côté exposé qui accompagne la note d'interface, D-13, d'où la trace de la passe tire le nom de la course, et celui de l'extrait des états — reçoivent la même valeur, celle du manifeste de la course ; le côté exposé les compare par programme avant tout versement) ; elle est recopiée")
# ---------- contre-lecture
r("cette différence reste à contre-lire (entrée 4).", "cette différence est contre-lue par l'entrée 3 nonies.")
r("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR", "- **Contre-lecture 3 nonies** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 12 au brouillon 13. Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md`, empreinte `" + H13 + "`. Rapport : `" + CL13 + "`, empreinte `" + HC13 + "`. Conclusion : « PAS PRÊT » sur deux remplacements (R-1, à corriger ; R-2, mineure) ; tout le reste de la différence est dit porté exactement, sans changement de fond. Traitement : `brouillons/barreau8-lecture-sondes-v1/differences-brouillon13-brouillon14-v1.md` (empreinte dans son compagnon) ; cette différence reste à contre-lire (entrée 4).\n- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR")
h = subprocess.run(['date','-u','+%Y-%m-%dT%H:%MZ'],capture_output=True,text=True).stdout.strip()
r("HEURE_DE_FIN", h)
for c in ("À REMPLIR — À FIXER : tirée par la session mère au scellement", "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :", "versée avec l'empreinte du texte scellé."):
    if t.count(c) != 1: fautes.append(('unicité', t.count(c), c))
if t.count("À REMPLIR") != 2: fautes.append(('marqueurs', t.count("À REMPLIR")))
L1 = t.splitlines()
if L1[75] != F3: fautes.append(('F-3 changée',))
j0 = next(i for i,l in enumerate(L1) if l.startswith('**Noms et champs, liste fermée**')); j1 = next(i for i,l in enumerate(L1) if l.startswith('**Fichiers non lus avant**'))
if "\n".join(L1[j0:j1]) != BLOC: fautes.append(('bloc Noms et champs changé',))
# O-6 : la citation de (b-2) est le texte exact de la phrase citée (une fois à sa place, une fois citée)
if t.count(PHRASE_B2) != 2 or t.count("« " + PHRASE_B2 + " »") != 1: fautes.append(('citation b-2', t.count(PHRASE_B2)))
for ph in (T2, T3):
    if t.count(ph) != 2: fautes.append(('T-2/T-3', t.count(ph)))
if fautes:
    for f in fautes: print("FAUTE", f)
    sys.exit(1)
P.write_text(t, encoding='utf-8')
corps = pathlib.Path('/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/diff1314-corps.md').read_text(encoding='utf-8')
N.write_text(corps.replace('@@DEBUT@@', DEBUT).replace('@@FIN@@', h), encoding='utf-8')
print("ok", h, len(L1))
