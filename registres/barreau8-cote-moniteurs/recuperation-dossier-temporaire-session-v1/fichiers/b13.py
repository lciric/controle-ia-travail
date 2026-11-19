import pathlib, sys, hashlib, subprocess
R = pathlib.Path('/home/user/controle-ia-travail')
D = R/'brouillons/barreau8-lecture-sondes-v1'
B12 = D/'prereg-lecture-sondes-barreau8-v1-brouillon12.md'
P = D/'prereg-lecture-sondes-barreau8-v1-brouillon13.md'
N = D/'differences-brouillon12-brouillon13-v1.md'
assert not P.exists() and not N.exists()
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
H12 = '467c2e8ba627554e454bba09dd640c3d10c5f25ed73cd7d25fcf7e491013bd5a'
assert sha(B12) == H12
CL12 = 'brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon12-v1.md'; HC12 = '715cef034f1a50f604bda49b204b9117502fc228b4b111f465097a17904e2f0d'
INT = 'docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-code-lecture-v3-integration-v1.md'; HINT = 'c07e50324925f0d4e47ec09e6342737b9de477f0bd8a83e7df69a44cef210228'
NV4 = 'docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v4.md'; HNV4 = '66f1e6c11aaed7f66d9a50191c4a066ed2a427107678180858d5626a764006db'
assert sha(R/CL12)==HC12 and sha(R/INT)==HINT and sha(R/NV4)==HNV4
t = B12.read_text(encoding='utf-8'); L0 = t.splitlines(); fautes = []
i0 = next(i for i,l in enumerate(L0) if l.startswith('**Noms et champs, liste fermée**')); i1 = next(i for i,l in enumerate(L0) if l.startswith('**Fichiers non lus avant**'))
BLOC = "\n".join(L0[i0:i1]); F3 = L0[75]
def r(a, b):
    global t
    c = t.count(a)
    if c != 1: fautes.append((c, a[:90])); return
    t = t.replace(a, b)
DEBUT = '2026-11-19T04:24Z'
# ---------- en-tête
r("— v1 — brouillon 12", "— v1 — brouillon 13")
r("**Statut : brouillon 12, texte soumis au scellement", "**Statut : brouillon 13, texte soumis au scellement")
r("contre-lecteur du brouillon 11 : Opus 5.5 (section", "contre-lecteur du brouillon 11 : Opus 5.5 ; contre-lecteur du brouillon 12 : Opus 5.5 (section")
r("brouillon 12 écrit entre 2026-11-19T03:36Z et 2026-11-19T03:38Z (`date -u`).", "brouillon 12 écrit entre 2026-11-19T03:36Z et 2026-11-19T03:38Z ; brouillon 13 écrit entre " + DEBUT + " et HEURE_DE_FIN (`date -u`).")
r("sont passés depuis en version 3, sans changement", "sont passés depuis en version 4, sans changement")
r("le code de la lecture est en version 2 ; c'est la ligne de registre de chaque code qui fait foi sur sa version) ;", "le code de la lecture est en version 3 ; c'est la ligne de registre de chaque code qui fait foi sur sa version) ; contre-lecture du brouillon 12, lue en entier, `" + CL12 + "` — `" + HC12 + "` ; contre-lecture du code de la lecture version 3 et second essai d'intégration des deux codes, lue en entier, `" + INT + "` — `" + HINT + "` ; notice du code de la passe version 4, section « Différences qui restent » lue pour contrôle, `" + NV4 + "` — `" + HNV4 + "` ;")
# ---------- A. contre-lecture du brouillon 12, mot pour mot
# M-1 (a) (porte m-1)
r("Les actions sans jeton noté n'y entrent pas. Pour chaque essai, la graine entière de sa clé sert d'abord au tirage de l'essai (actions étiquetées, jeton injecté, permutation) par un générateur neuf, puis", "Les actions sans jeton noté n'y entrent pas. **Égalité des deux chemins, jouée avant (i)** : pour chaque sonde lue et chaque action de `H` d'au moins un jeton noté, le score d'action lu par la fonction même de la lecture décisive (tableau des scores par action livré, colonne de la sonde, case du maximum, ligne désignée par la clé de l'action) est égal, sans tolérance, au maximum des scores par jeton de la sonde que l'essai recalcule ; l'essai déduit lui-même les bornes de chaque action des seuls champs `rang` et `jetons_notes` de l'index (sommes cumulées dans l'ordre de `rang`), sans appeler la fonction de la lecture qui associe les scores aux clés, et ces mêmes bornes placent le jeton injecté en (ii) et les blocs permutés en (iii) ; une seule inégalité fait échouer A0, sans rejeu, et la sortie écrit la sonde et le nombre d'actions inégales, jamais un score. Pour chaque essai, la graine entière de sa clé sert d'abord au tirage de l'essai (actions étiquetées, jeton injecté, permutation) par un générateur neuf, `numpy.random.default_rng(graine)`, puis")
# M-1 (b)
r("**A0 échoue** si et seulement si (a) la même sonde", "**A0 échoue** si et seulement si l'égalité des deux chemins n'est pas tenue, ou si (a) la même sonde")
# M-1 (c)
r("; en (iii), « des scores par jeton de la sonde » devient « des scores d'action de la sonde » ; tout le reste de l'essai", "; en (iii), « des scores par jeton de la sonde » devient « des scores d'action de la sonde » ; la phrase « **Égalité des deux chemins, jouée avant (i)** : … jamais un score. » est retirée, et « l'égalité des deux chemins n'est pas tenue, ou si » est retiré de la règle d'échec ; tout le reste de l'essai")
# m-2
r("(une permutation tirée par la graine `alignement/<sonde>`)", "(une permutation, `permutation(n)` du générateur neuf de la graine `alignement/<sonde>`, n étant le nombre d'actions de `H` d'au moins un jeton noté, rangées dans l'ordre des clés : l'action de rang k reçoit les scores de l'action dont le rang est l'élément k de la permutation)")
# m-3
r("Cette garde tient lieu d'effectif minimal : aucun autre n'est écrit.", "Cette garde tient lieu d'effectif minimal : aucun autre n'est écrit. Les blocs d'un jeu sont les tâches qui y portent au moins une action notée : une tâche réduite à une seule classe reste un bloc ; une tâche sans aucune action notée sur ce jeu n'en est pas un.")
# m-4
r("leur déséquilibre de tirage touche la sonde et les 800 directions de la même façon, et l'essai ne compare aucun prédicteur trivial.", "leur déséquilibre de tirage touche chaque direction, sonde comprise, selon sa propre dépendance au rang et à la longueur, et le rééchantillonnage par tâches en porte la variabilité ; l'essai ne compare aucun prédicteur trivial.")
# m-5
r("au chapeau, « Il est défini sur les scores par jeton livrés des sondes (option (b)) :", "au chapeau, « **Il est défini sur les scores par jeton livrés des sondes** (option (b)) :")
r("devient « Il est défini sur les scores d'action livrés :", "devient « **Il est défini sur les scores d'action livrés** :")
# m-6
r("l'essai à blanc n'écrit ni trace de livraison ni bordereau.", "l'essai à blanc n'écrit ni trace de livraison ni bordereau. Du côté exposé, aucune personne ni aucun programme autre que le code de la passe n'ouvre les fichiers 1, 2 et 4 de la livraison ni n'en lit un score, avant comme après leur envoi.")
# O-1 (ajout à la demande de la conductrice)
r("elle n'est comparée à rien et n'entre dans aucune règle ; elle n'est recopiée qu'en tête de la sortie de la lecture et du verdict,", "elle n'entre dans aucune règle de lecture ; elle n'est comparée qu'au nom de la course porté par la trace de la passe, à l'ouverture de la lecture, qui refuse de tourner s'ils diffèrent (plan, point 3) ; elle est recopiée en tête de la sortie de la lecture et du verdict,")
r("des deux valeurs de la course portées par la trace (nom de la course, commit de lancement), la lecture contrôle le type seulement, et elles sont recopiées en tête de la sortie ;", "des deux valeurs de la course portées par la trace (nom de la course, commit de lancement), la garde de réception contrôle le type seulement, et elles sont recopiées en tête de la sortie ; à l'ouverture de la lecture, où la trace et l'extrait des états sont lus ensemble, le nom de la course de la trace doit être égal à `run_id` de l'extrait des états, sinon la lecture refuse de tourner (plan, point 3) ;")
r("ou si un nom de sonde des couches 7 ou 23 paraît plus d'une fois dans l'index.", "ou si un nom de sonde des couches 7 ou 23 paraît plus d'une fois dans l'index. Elle refuse aussi de tourner si le nom de la course porté par la trace de la passe diffère de `run_id` de l'extrait des états : les états et les scores doivent venir de la même course.")
r("ou valeur hors du vocabulaire de I-9 (D-12) |", "ou valeur hors du vocabulaire de I-9 (D-12) ; ou `run_id` de l'extrait différent du nom de la course porté par la trace de la passe |")
# ---------- B. phrases du second essai d'intégration
# tâche réduite à une classe (décision de la conductrice ; fondue avec m-3 et M-1)
r("avant le retrait des actions sans jeton noté, qui sortent ensuite des deux classes.", "avant le retrait des actions sans jeton noté, qui sortent ensuite des deux classes. Une tâche qui, après le retrait des actions sans jeton noté, ne porte plus qu'une classe garde ses actions restantes dans leur classe (elle reste un bloc : « Métrique », « Intervalle ») ; la sortie nomme cette tâche et la classe qui lui reste, sans autre effet ; l'essai n'échoue que par l'égalité des deux chemins non tenue, (a) ou (b).")
# réception seule : quatre lignes ; pas d'entropie
r("dès que les lignes `SCELLEMENT-SONDES-IIB`, `CODE-LECTURE-SONDES-IIB` et `LIVRAISON-PASSE-IIB` sont inscrites, sans attendre", "dès que les lignes `SCELLEMENT-SONDES-IIB`, `CODE-PASSE-IIB`, `CODE-LECTURE-SONDES-IIB` et `LIVRAISON-PASSE-IIB` sont inscrites (la garde r4 compare la trace au bordereau du code que cite la ligne `CODE-PASSE-IIB`), sans attendre")
r("ni un écart entre un score livré et un score recalculé", "ni un écart entre un score livré et un score recalculé. La commande de réception seule ne reçoit pas l'entropie et ne contrôle pas la cellule de F-3 ; la lecture et la recette de puissance la contrôlent")
# clé et nom de la sonde décisive ; direction de plus ; finitude
r("désignées comme dans la table. **Recherche des directions : une seule règle, pour la passe et pour la lecture.**", "désignées comme dans la table. La sonde décisive est l'entrée de l'index de rang k, dont le vecteur est sous la clé `s<k>_w` de la table ; elle porte le nom de la table, et ce nom ne paraît qu'une fois dans l'index ; sinon « sans objet ». **Recherche des directions : une seule règle, pour la passe et pour la lecture.**")
r("Sinon la sonde est « sans objet », des deux côtés. Un vecteur ou un biais non fini,", "Pour la tromperie et les enjeux élevés : une direction de plus est toute entrée de l'index dont le nom commence par `<préfixe>-plancher-` sans être l'un des noms `<préfixe>-plancher-0` à `<préfixe>-plancher-799` (numéros écrits sans zéro de tête), quelles que soient sa famille et sa couche. Sinon la sonde est « sans objet », des deux côtés. Un vecteur ou un biais non fini,")
r("comme une sonde non conforme.", "comme une sonde non conforme. La finitude du vecteur et du biais est contrôlée avant toute autre condition, sur toute entrée de l'index qui porte le nom de l'une des neuf sondes nommées, et sur toute direction candidate au plancher (tromperie, enjeux élevés : toute entrée dont le nom commence par `<préfixe>-plancher-` ; dissimulation : toute entrée de famille « plancher » du fichier des sondes neuves), que la sonde soit ensuite « lue » ou « sans objet » ; une valeur non finie arrête la passe (P1) et fait refuser la lecture.")
# ligne d'accord (lecture et passe)
PH = " La première cellule est l'identifiant seul, sans autre mot ni mise en forme (ni gras, ni accent grave, ni marque) ; une ligne dont la première cellule porte autre chose ne compte pas"
r("les autres lignes qui citent cet identifiant ne comptent pas | la lecture |", "les autres lignes qui citent cet identifiant ne comptent pas." + PH + " | la lecture |")
r("les autres lignes qui citent cet identifiant ne comptent pas | la passe ne part pas |", "les autres lignes qui citent cet identifiant ne comptent pas." + PH + " | la passe ne part pas |")
# ---------- contre-lecture
r("cette différence reste à contre-lire (entrée 4).", "cette différence est contre-lue par l'entrée 3 octies.")
r("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR", "- **Contre-lecture 3 octies** — sous-agent neuf, modèle Claude Opus 5.5, qui n'a écrit ni ce texte, ni aucune contre-lecture antérieure de ce texte, ni la note d'interface, ni aucune notice, ni aucun code ; contre-lecture de la différence du brouillon 11 au brouillon 12, avec une simulation propre de la forme (A) de l'essai de la chaîne (données synthétiques). Brouillon relu : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon12.md`, empreinte `" + H12 + "`. Rapport : `" + CL12 + "`, empreinte `" + HC12 + "`. Conclusion : « PAS PRÊT » sur une liste fermée (M-1, à corriger ; m-1 à m-6, mineures) ; tout ce que le brouillon 12 portait est dit porté exactement, sans changement de fond, et la forme (A) est confirmée. Traitement : `brouillons/barreau8-lecture-sondes-v1/differences-brouillon12-brouillon13-v1.md` (empreinte dans son compagnon) ; cette différence reste à contre-lire (entrée 4).\n- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR")
h = subprocess.run(['date','-u','+%Y-%m-%dT%H:%MZ'],capture_output=True,text=True).stdout.strip()
r("HEURE_DE_FIN", h)
for c in ("À REMPLIR — À FIXER : tirée par la session mère au scellement", "- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :", "versée avec l'empreinte du texte scellé."):
    if t.count(c) != 1: fautes.append(('unicité', t.count(c), c))
if t.count("À REMPLIR") != 2: fautes.append(('marqueurs', t.count("À REMPLIR")))
L1 = t.splitlines()
if L1[75] != F3: fautes.append(('F-3 changée',))
j0 = next(i for i,l in enumerate(L1) if l.startswith('**Noms et champs, liste fermée**')); j1 = next(i for i,l in enumerate(L1) if l.startswith('**Fichiers non lus avant**'))
if "\n".join(L1[j0:j1]) != BLOC: fautes.append(('bloc Noms et champs changé',))
if "comparée à rien" in t: fautes.append(('reste', 'comparée à rien'))
if fautes:
    for f in fautes: print("FAUTE", f)
    sys.exit(1)
P.write_text(t, encoding='utf-8')
corps = pathlib.Path('/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/diff1213-corps.md').read_text(encoding='utf-8')
N.write_text(corps.replace('@@DEBUT@@', DEBUT).replace('@@FIN@@', h), encoding='utf-8')
print("ok", h, len(L1))
