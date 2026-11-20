# Fabrique la pièce unique des changements du brouillon 2 au candidat. Bibliothèque standard ; ne lit que les brouillons,
# le candidat, les scripts des couples (sans les exécuter) et les différentiels.
import sys, json, re, hashlib, subprocess, os
S = sys.argv[1]; SORTIE = sys.argv[2]; FIN = sys.argv[3]
sys.path.insert(0, S)
from annotations import A
import couples as C
P = "prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/"
B = "prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon%d.md"
CAND = S + "/lecture-sondes-bbis-par-lentilles-v2-candidat.md"
def h(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def run(*a): return subprocess.run(a, capture_output=True).stdout
L = []
w = L.append
THEMES = [
 ("2→3", "égalité de score au vingtième rang : score décroissant, puis identifiant de jeton croissant ; portée : direction lue, directions nulles, témoins, toute lentille ; compte des égalités écrit dans les tables", "hunk 2 (ligne (b))", []),
 ("2→3", "concentration : chaque direction nulle jugée sur les M − 1 autres ; comparaison en simple précision, une égalité compte contre la direction lue ; arrêt si variance nulle ou moins de trois directions", "hunk 2 (ligne (a) 1)", []),
 ("2→3", "part au-dessus du nul : quantile 0,99 des M − 1 autres pour une direction nulle ; quantile par interpolation linéaire", "hunk 2 (ligne (a) 2)", []),
 ("2→3", "calibration : témoins jugés comme la direction lue, directions nulles sans elles-mêmes ; loi du compte dite « de référence », approchée ; bornes dites égales à celles d'un programme nommé (classé « règle » dans le doute pour cette dernière part)", "hunk 3 (lignes (a) 3 et (a) 4)", []),
 ("3→4", "libellé du premier palier reconnu avec ou sans « ; reprise sur sauvegarde notée » ; tout autre ajout : arrêt", "", ["K12", "K18", "K20", "K27c"]),
 ("3→4", "seconde course incomplète (ou fiche qui ne dit pas l'achèvement) traitée comme l'ajustement seul : aucune lecture sans la ligne du mot de Lazar", "", ["K12", "K18", "K19", "K24b", "K26", "K27b", "K29", "K31a", "K31c"]),
 ("3→4", "audit dû dès que le programme rend un déclencheur, donc aussi au deuxième palier ; la fiche porte la liste des déclencheurs", "", ["K18", "K19", "K27b"]),
 ("3→4", "une phrase permise par cas (six formes), dans les mots de la version 8 du critère d'identité ; préfixe par lentille retiré", "", ["K18", "K26"]),
 ("3→4", "premier palier en cas mixte : le verdict d'ensemble et les conditions communes ne se transportent pas tels quels ; ligne de verdict d'ensemble pour une seule lentille", "", ["K13", "K26b", "K26c", "K28"]),
 ("3→4", "règle de départage étendue : référence « plongements seuls » et témoin de couche, signe −, listes de dix, pôles à cosinus égal (indice de neurone croissant, puis signe +) ; comptes d'égalités écrits", "", ["K21a", "K21c", "K22"]),
 ("3→4", "ligne de l'addendum de concentration au registre propre : unique, de l'empreinte citée, antérieure à toute clé de la v2 ; sinon rien de la seconde passe ne part", "", ["K24a", "K27a", "K29", "K30a"]),
 ("3→4", "module des statistiques neuf pour la seconde passe ; la reproduction porte la phrase « code de lecture différent […] » (classé « règle » dans le doute)", "", ["K25", "K30a"]),
 ("4→5", "phrase du verdict au déclencheur (vi) : champ de la fiche, place et forme contrôlées, recopiée après la phrase permise, arrêt sur forme inconnue ou champ incohérent", "", ["L23", "L29", "L34"]),
 ("4→5", "première passe lancée et non achevée : la seconde ne la remplace pas ; aucune phrase de la lentille publique ni de la lentille des logits avant le nœud de la v1 ; phrase de tête ; ligne d'arrêt", "", ["L25", "L27", "L32", "L34"]),
 ("4→5", "fiche muette sur l'achèvement de la seconde course : non lue sous un motif propre, sans voie par le mot de Lazar ; quatrième valeur de la ligne « Course du réajustement »", "", ["L20", "L28", "L33"]),
 ("4→5", "une lentille au premier palier, l'autre au deuxième : deux lignes de verdict d'ensemble, chacune nommant sa lentille, réserves par lentille", "", ["L31"]),
 ("4→5", "étiquettes du programme de comparaison : la version du critère n'en est pas tirée", "", ["L23"]),
 ("4→5", "nœuds N12 et N17 laissés ouverts : règle écrite pour chaque option ; option lue dans la pièce de `GO-LENTILLES-BBIS-V2` ; pièce muette : le défaut ; clé conditionnelle de l'addendum de recopie ; arrêt sur une autre forme (règles conditionnelles, retirées au brouillon 6)", "", ["L21", "L22", "L33", "L34", "L35", "L38", "L39"]),
 ("5→6", "nœud N12 tranché, option (a) : règles des options (b) et (c) retirées ; le mot de Lazar postérieur à l'avertissement ouvre ou non la lecture et ne choisit aucune branche", "", ["P10", "P16", "P29"]),
 ("5→6", "nœud N17 tranché, option (a) aux deux paliers : condition de l'addendum de recopie, sa clé, son motif « Non lue » et son cas d'arrêt retirés", "", ["P11", "P17", "P22", "P30"]),
 ("5→6", "issue des deux nœuds fixée avant le scellement : la pièce de `GO-LENTILLES-BBIS-V2` la recopie avec l'identifiant et l'heure de la ligne d'accord ; le code n'y lit aucune option ; arrêt nommé (autre issue, ligne d'accord non antérieure au scellement, autre forme) ; pièce muette : aucun arrêt, phrase de tête fixée", "", ["P20", "P22"]),
 ("5→6", "phrase du déclencheur (vi) : formes admises élargies (« séries … inchangées » ; deux faits joints par « et »)", "", ["P12", "P19"]),
 ("5→6", "première passe encore en cours au montage : pas de nœud de la v1, phrases de la première passe si elle s'achève ; ligne des tables sans ligne des entrées : arrêt", "", ["P15", "P18"]),
 ("6→candidat", "ligne d'accord des nœuds N12 et N17 nommée (GO-2026-11-20-18) avec l'heure que la pièce de `GO-LENTILLES-BBIS-V2` recopie (2026-11-20T05:34:13Z, ligne R-4104) : marqueur porté, classé « règle » dans le doute parce que l'arrêt sur la ligne d'accord compare cette heure à celle du scellement ; le rapport de vérification dit que l'arrêt et l'essai « s'appliquent tels quels »", "couple R1, hunk 2", []),
]
res = {}; ctl = {}
for n, m in ((3, 4), (4, 5), (5, 6)):
    a, b, r, egal = C.etape(n, m); assert egal
    H0 = C.hunks(n, m, "-U0"); H3 = C.hunks(n, m, "-U3")
    for d in r:
        d["h0"] = [i for i, (s1, l1, s2, l2) in enumerate(H0, 1) if not (d["l_arr_fin"] < s2 or d["l_arr"] > (s2 + l2 - 1 if l2 else s2 + 1))]
        d["h3"] = [i for i, (s1, l1, s2, l2) in enumerate(H3, 1) if not (d["l_arr_fin"] < s2 or d["l_arr"] > s2 + l2 - 1)]
        assert d["h0"] and d["h3"], d["id"]
    orph = [i for i in range(1, len(H0) + 1) if not any(i in d["h0"] for d in r)]
    assert not orph
    k = "%d-%d" % (n, m); res[k] = r
    assert set(A[k]) == set(d["id"] for d in r), k
    versé = P + "diff-brouillon%d-vers-brouillon%d-v1.txt" % (n, m)
    ctl[k] = dict(nb=len(r), h0=len(H0), h3=len(H3),
                  normal=(run("diff", B % n, B % m) == open(versé, "rb").read()),
                  unifie=(run("diff", "-u", B % n, B % m) == open(versé, "rb").read()))
    assert ctl[k]["normal"] and not ctl[k]["unifie"]
# couverture des thèmes
for etp, k in (("3→4", "3-4"), ("4→5", "4-5"), ("5→6", "5-6")):
    Rs = set(i for i, v in A[k].items() if v[0] == "R")
    T = set(x for t in THEMES if t[0] == etp for x in t[3])
    assert Rs == T, (etp, Rs ^ T)
d6 = run("diff", "-U0", "--label", "brouillon6", "--label", "candidat", B % 6, CAND)
assert d6 == open(S + "/differentiel-brouillon6-candidat.diff", "rb").read()
d23 = run("diff", "-u", "--label", B % 2, "--label", B % 3, B % 2, B % 3)
assert d23 == open(P + "diff-brouillon2-vers-brouillon3-v1.txt", "rb").read()
E = {p: h(p) for p in [B % i for i in range(2, 7)] + [CAND, S + "/differentiel-brouillon6-candidat.diff", S + "/applique.py"]
     + [P + f for f in sorted(os.listdir(P)) if re.match(r"(couples|diff|sortie-couples)-brouillon.*\.(py|txt)$", f)]}
N = "docs/notes/neuron-lens-v1/"
AUTRES = [N + "verification-corrections-texte-lecture-lentilles-v2-brouillon6-v1.md",
          N + "verification-corrections-texte-lecture-lentilles-v2-brouillon5-v1.md",
          N + "contre-lecture-texte-lecture-lentilles-v2-brouillon4-v1.md",
          "docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-redacteur-differences-brouillon2-version-v1.md",
          N + "mot-lazar-redacteur-differences-brouillon2-version-2026-11-20-v1.md"]
for p in AUTRES: E[p] = h(p)
def e(p): return "`%s`" % E[p]
SC = "docs/notes/neuron-lens-v1/scellement-texte-lecture-v2/"
w("# Changements du brouillon 2 à la version du préenregistrement « lecture des sondes de l'étape B bis par lentilles, v2 » — pièce unique, v1")
w("")
w("Cette pièce liste chaque changement fait au texte de lecture, version 2, depuis son brouillon 2 jusqu'au **candidat** de la session")
w("principale, étape par étape : brouillon 2 → 3, 3 → 4, 4 → 5, 5 → 6, 6 → candidat. Elle décrit ; elle ne juge aucun changement sur le fond.")
w("Elle est faite pour être citée à la place du marqueur `DIFFERENCES_DU_BROUILLON_2_A_LA_VERSION` (nom écrit ici sans chevrons) du texte,")
w("« Ce que l'auteur savait », point 4.")
w("")
w("## En-tête")
w("")
w("- **Auteur** : rédacteur neuf de cette pièce, sous-agent de la session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`), modèle")
w("  **Claude Fable 5.2** (`claude-fable-5-2`), sur le mandat")
w("  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-redacteur-differences-brouillon2-version-v1.md`")
w("  (%s, recalculée avant lecture ; section « Texte du mandat » suivie), parti sur le mot de Lazar « a » que consigne la note" % e(AUTRES[3]))
w("  `%s` (%s ; note non ouverte, empreinte seule)." % (AUTRES[4], e(AUTRES[4])))
w("  Il n'a écrit ni la v1, ni aucun brouillon de la v2, ni aucune contre-lecture ou vérification. Aucun commit, aucun push, aucune")
w("  machine, aucune dépense, aucun modèle chargé ; aucun fichier existant modifié ; réseau : `git fetch origin main` seul.")
w("- **Heures (UTC, `date -u`)** : 2026-11-20 ; début à 07:56:24 ; différentiel du brouillon 2 au brouillon 3 versé et scellé à 08:00:03 ;")
w("  cette pièce écrite à %s. Branche des lentilles `claude/brave-galileo-jhp684` à `%s` ;" % (FIN, sys.argv[4]))
w("  branche principale récupérée à `%s`." % sys.argv[5])
w("- **Pièces lues** : la section « Texte du mandat » ; `CLAUDE.md` ; les blocs de tête « Brouillon 4 », « Brouillon 5 » et « Brouillon 6 »")
w("  (brouillon 4, lignes 3 à 108 ; brouillon 5, lignes 3 à 158 ; brouillon 6, lignes 3 à 162), en entier ; le bloc « Brouillon 3 » par le")
w("  différentiel du brouillon 2 au brouillon 3, lu en entier ; les trois scripts des couples, lus par programme (leur liste `COUPLES`")
w("  est extraite sans que le script soit exécuté) ; de chaque couple, ce qu'il retire et ce qu'il met, coupé à 1 800 caractères pour")
w("  l'étape 3 → 4 et à 650 caractères pour les étapes 4 → 5 et 5 → 6 (les couples longs n'ont donc pas été lus jusqu'au bout : leur")
w("  nature est dite d'après leur début, leur lieu et les tables des blocs de tête) ; le début et la fin de la sortie du script des")
w("  couples du brouillon 3 au brouillon 4 ; le candidat, par son différentiel au brouillon 6 et par une recherche du nom du marqueur ;")
w("  le script `applique.py` (60 premières lignes) ; du rapport de vérification des corrections du brouillon 6, ses titres et ses")
w("  sections R1 et R2 (lignes 114 à 147) ; du relevé des marqueurs de la session principale (`%smarqueurs-v1.md`, branche" % SC)
w("  principale), le seul § 7, qui porte sur ce marqueur. **Non lus** : les brouillons hors des passages ci-dessus ; la contre-lecture")
w("  du brouillon 4 et la vérification des corrections du brouillon 5 (empreintes seules) ; les mandats des rédacteurs ; le critère")
w("  d'identité, le devis, l'addendum de concentration.")
w("- **Expositions, déclarées** (R4) : (1) *mots du verdict de la tranche de nos lentilles*, vus dans les brouillons et non dans le verdict,")
w("  qui n'a pas été ouvert : la phrase citée sur la lecture contre ablation par fenêtre (couche 15), les libellés « autre » et")
w("  « intermédiaire » de deux mesures ; tout porte sur nos lentilles, rien sur les sondes. (2) *Chiffres sur données synthétiques* que")
w("  citent les brouillons (part des témoins à p ≤ 0,05, fréquence d'une égalité au vingtième rang, banc à petite taille). (3) *Registres* :")
w("  aucun registre ouvert ; vus seulement les identifiants, heures et objets de lignes que les brouillons, le candidat et le rapport de")
w("  vérification citent, et la description, dans le bloc « Brouillon 6 », de six débuts de lignes d'autres chaînes (sans mesure ni issue).")
w("- **Jamais ouverts** : aucun fichier de la liste « Jamais ouverts » de la v1 ; aucune sortie, aucun score, aucune table, aucune lecture,")
w("  aucun verdict de l'apprentissage des sondes sur la tâche ; aucune table ni sortie de la lecture par la lentille publique ; aucune")
w("  branche `donnees/*` ou `calcul/*` ; rien sous `diag/`, `runs/` ou `docs/verdicts/` ; aucun fichier « consigne-privee » ou")
w("  « conception-ii-b » ; rien de `brouillons/ii-b-saboteur-budget-v1/` ; le verdict de la tranche de nos lentilles (`3a9b947e…`).")
w("- **Refus d'outil** : aucun refus d'outil, de permission ni de classifieur.")
w("")
w("## Ce que « la version » désigne ici")
w("")
w("Le candidat de la session principale : `%slecture-sondes-bbis-par-lentilles-v2-candidat.md` sur la branche principale" % SC)
w("(%s ; 3 000 lignes). Il porte encore neuf marqueurs entre doubles chevrons, dont celui que cette pièce sert. **Les textes mis" % e(CAND))
w("à la place de ces marqueurs après le candidat ne sont pas listés ici** : ils n'existaient pas à l'écriture de cette pièce.")
w("")
w("## Contrôles par programme")
w("")
w("| objet | commande rejouée | résultat |")
w("|---|---|---|")
w("| brouillon 2 → 3 | `diff -u --label <brouillon 2> --label <brouillon 3>` (les étiquettes sont les deux chemins ; sans elles l'en-tête porterait les dates des fichiers) | versé : `%sdiff-brouillon2-vers-brouillon3-v1.txt`, %s ; **3 hunks** |" % (P, e(P + "diff-brouillon2-vers-brouillon3-v1.txt")))
for k, (n, m) in (("3-4", (3, 4)), ("4-5", (4, 5)), ("5-6", (5, 6))):
    w("| brouillon %d → %d | `diff` (format normal) et `diff -u` | la pièce versée est au **format normal** de `diff`, non au format unifié : le `diff` normal recalculé lui est **égal à l'octet** ; le `diff -u` recalculé en diffère **par la forme seule** (%d hunks à trois lignes de contexte pour les mêmes %d blocs) ; **écart de forme, dit** |" % (n, m, ctl[k]["h3"], ctl[k]["h0"]))
w("| brouillon 6 → candidat | `diff -U0 --label brouillon6 --label candidat` et `diff -u` | la pièce versée est un différentiel unifié **sans ligne de contexte** : recalculé ainsi, il lui est **égal à l'octet** (2 hunks) ; le `diff -u` à trois lignes de contexte en diffère par le contexte et l'en-tête seuls (2 hunks, mêmes lignes changées) ; **écart de forme, dit** |")
w("| couples des étapes 3 → 4, 4 → 5, 5 → 6 | listes `COUPLES` extraites des scripts sans les exécuter, appliquées au brouillon de départ | chaque texte « avant » trouvé une fois ; **le brouillon d'arrivée est reconstruit à l'octet** aux trois étapes ; chaque bloc du différentiel versé tombe dans un couple, chaque couple touche au moins un bloc : **aucun bloc sans couple, aucun couple sans bloc** |")
w("| compagnons | `controle_ia.scellement verifier` sur les cinq brouillons et les dix pièces de fabrication | tous `OK` |")
w("")
w("Dans les tables ci-dessous, « bloc n » est le n-ième bloc du différentiel versé de l'étape (format normal), qui est aussi le n-ième")
w("hunk du `diff -U0` recalculé ; « hunk n » est le n-ième hunk du `diff -u` recalculé (trois lignes de contexte). Les lignes sont")
w("celles du **brouillon d'arrivée**. Classe : **R** change une règle de lecture (seuil, statistique, libellé, phrase gelée, arrêt,")
w("condition de lecture) ; **E** est un essai du code qui accompagne une règle (« Code neuf », R5) ; **M** ne change que des mots, une")
w("citation, un marqueur ou l'histoire du texte. **Dans le doute, le changement est classé R** et le doute est écrit. Quand les")
w("brouillons 5 et 6 classent eux-mêmes un changement (« règle », « lettre », « forme »), leur mot est repris ou l'écart est dit.")
w("")
# ---- étape 2 -> 3
w("## Étape 1 — du brouillon 2 au brouillon 3")
w("")
w("- Pièces : brouillon 2 `%s` (%s) ; brouillon 3 `%s` (%s) ; différentiel, fait pour cette pièce :" % (B % 2, e(B % 2), B % 3, e(B % 3)))
w("  `%sdiff-brouillon2-vers-brouillon3-v1.txt` (%s). Aucune pièce de fabrication n'existait pour cette étape." % (P, e(P + "diff-brouillon2-vers-brouillon3-v1.txt")))
w("- Raison de l'étape, d'après le bloc « Brouillon 3 — différences avec le brouillon 2 » : (a) la statistique de la valeur p, chaque")
w("  direction nulle jugée sans elle-même (option 2, mot de Lazar GO-2026-11-19-47, donné pour le texte de la v1 ; mots repris de")
w("  l'addendum de concentration, EC-1 à EC-3) ; (b) la règle de départage à score égal au vingtième rang (contre-lecture de l'addendum")
w("  de concentration, § 10).")
w("")
w("| n° | lieu (brouillon 3) | classe | nature | ce qui change | raison | hunk |")
w("|---|---|---|---|---|---|---|")
E23 = [
 ("tête, lignes 3 à 54", "M", "histoire", "bloc « Brouillon 3 — différences avec le brouillon 2 » ajouté (ce qu'est le fichier, auteur, (a), (b), occurrences laissées, restes ouverts)", "forme : le bloc se décrit lui-même (« et ce bloc »)", "hunk 1 (`@@ -1,5 +1,57 @@`)"),
 ("« Métrique », point 6, puce des vingt premiers jetons, lignes 994 à 1003", "R", "règle (liste ; compte écrit)", "égalité de score : score décroissant puis identifiant de jeton croissant ; portée ; la règle « ne penche vers aucun libellé » ; compte des listes à égalité écrit dans les tables", "(b) du bloc ; contre-lecture de l'addendum de concentration, § 10", "hunk 2 (`@@ -939,11 +991,35 @@`)"),
 ("« Métrique », point 6, concentration, lignes 1004 à 1015", "R", "règle (statistique ; arrêt)", "C(u_j) calculé sur les M − 1 autres directions nulles ; formules exactes ; comparaison en simple précision ; arrêt sur variance nulle ou moins de trois directions", "(a) 1 du bloc ; GO-2026-11-19-47 ; addendum de concentration, EC-1", "hunk 2"),
 ("« Métrique », point 6, part au-dessus du nul, lignes 1017 à 1022", "R", "règle (statistique)", "P(u_j) contre le quantile 0,99 des M − 1 autres ; quantile par interpolation linéaire, écrit", "(a) 2 du bloc ; GO-2026-11-19-47 ; addendum de concentration, EC-2", "hunk 2"),
 ("« Plan d'analyse », point 6, calibration, lignes 1243 à 1245", "R", "règle (statistique)", "témoins jugés comme la direction lue, directions nulles jugées sans elles-mêmes", "(a) 3 du bloc ; addendum de concentration, EC-3", "hunk 3 (`@@ -1164,13 +1240,17 @@`)"),
 ("« Plan d'analyse », point 6, calibration, lignes 1249 à 1253", "R", "mots (« loi exacte » devient « loi de référence », approchée) et bornes dites égales à celles du programme `bornes_calibration_statistique_corrigee_v2.py` — classé R dans le doute", "la loi bêta-binomiale dite loi de référence, approchée ; bornes inchangées, dites égales à celles d'un programme nommé", "(a) 4 du bloc ; addendum de concentration, EC-3 et § 7", "hunk 3"),
]
# contrôle des lignes annoncées : toutes doivent être des lignes ajoutées du différentiel
plus = set(); cur = None
for l in d23.decode("utf-8").splitlines():
    mm = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)", l)
    if mm: cur = int(mm.group(1)); continue
    if cur is None: continue
    if l.startswith("+"): plus.add(cur); cur += 1
    elif l.startswith(" "): cur += 1
for lieu, *_ in E23:
    a_, b_ = map(int, re.search(r"lignes (\d+) à (\d+)", lieu).groups())
    assert all(x in plus for x in range(a_, b_ + 1)), lieu
assert plus == set(range(3, 55)) | set(range(994, 1016)) | set(range(1017, 1023)) | set(range(1243, 1246)) | set(range(1249, 1254)), sorted(plus)
for i, t in enumerate(E23, 1):
    w("| %d | %s | %s | %s | %s | %s | %s |" % ((i,) + t))
w("")
w("**Chaque hunk est-il expliqué par le bloc « Brouillon 3 » ?** Oui pour les trois : le hunk 1 est le bloc lui-même ; le hunk 2 porte")
w("(b), (a) 1 et (a) 2 ; le hunk 3 porte (a) 3 et (a) 4. **Aucun hunk non expliqué.** Deux détails vus dans des hunks expliqués, que le")
w("bloc ne nomme pas mot pour mot, listés sans jugement : dans (b), la phrase « le nombre de listes dont le vingtième et le")
w("vingt-et-unième score sont égaux est écrit dans les tables » ; dans (a) 4, la mention que les bornes sont « égales à celles du")
w("programme `bornes_calibration_statistique_corrigee_v2.py` » (le bloc dit « bornes inchangées »).")
w("")
LEG = {
 "3-4": ("Étape 2 — du brouillon 3 au brouillon 4", 3, 4,
   "Raison de l'étape : les douze tâches du mandat du rédacteur du brouillon 4 (colonne « raison » : « tâche n »). 1 : alignement sur le critère d'identité version 8 (lieux (a) à (l) ; écarts E1 à E6 de la table du bloc « Brouillon 4 ») ; 2 : écart sur la couche 15 (rapport du lecteur désigné) ; 3 : marqueur de la vérification du bloc séparable ; 4 : autres marqueurs ; 5 : phrase « elle ne penche vers aucun libellé » ; 6 : règle de départage étendue aux listes de dix ; 7 : option « permutation fixe », nœud N18 ; 8 : essais de « Code neuf » ; 9 : table « Changements de la v1 à la v2 » ; 10 : citation de l'addendum de concentration ; 11 : portée du mot GO-2026-11-19-47 pour la version 2 ; 12 : garde d'égalité de la v1 (GO-2026-11-19-78, R-3929).",
   lambda t: "mandat du rédacteur du brouillon 4, " + ("forme" if t.startswith("forme") else "tâche " + t)),
 "4-5": ("Étape 3 — du brouillon 4 au brouillon 5", 4, 5,
   "Raison de l'étape : les corrections de la contre-lecture du brouillon 4 (`docs/notes/neuron-lens-v1/contre-lecture-texte-lecture-lentilles-v2-brouillon4-v1.md`, %s : quatre bloquantes, B1 à B4, dix non bloquantes, N1 à N10) et les tâches du mandat du rédacteur du brouillon 5 (« mandat, tâche n »)." % e(AUTRES[2]),
   lambda t: ("forme" if t == "forme" else "contre-lecture du brouillon 4 et mandat du rédacteur du brouillon 5 : " + t)),
 "5-6": ("Étape 4 — du brouillon 5 au brouillon 6", 5, 6,
   "Raison de l'étape : les nœuds N12 et N17 tranchés par Lazar le 2026-11-20 (option (a) chacun ; mot « go reco », note `cd02b0fb…` ; ligne d'accord GO-2026-11-20-18, citée au candidat) — « tâche 1 » ; la correction bloquante C1 et les six non bloquantes M1 à M6 de la vérification des corrections du brouillon 5 (`docs/notes/neuron-lens-v1/verification-corrections-texte-lecture-lentilles-v2-brouillon5-v1.md`, %s) ; « tâche 4 » : tables des changements ; « tâche 5 » : contrôle des lignes de la v1." % e(AUTRES[1]),
   lambda t: ("forme" if t == "forme" else "vérification des corrections du brouillon 5 et mandat du rédacteur du brouillon 6 : " + t)),
}
comptes = {"2→3": {"R": 5, "E": 0, "M": 1}}
for k in ("3-4", "4-5", "5-6"):
    titre, n, m, raison, fr = LEG[k]
    w("## " + titre); w("")
    f1 = P + "couples-brouillon%d-vers-brouillon%d-v1.py" % (n, m); f2 = P + "sortie-couples-brouillon%d-vers-brouillon%d-v1.txt" % (n, m); f3 = P + "diff-brouillon%d-vers-brouillon%d-v1.txt" % (n, m)
    w("- Pièces : brouillon %d `%s` (%s) ; brouillon %d `%s` (%s) ; script des couples `%s` (%s) ; sa sortie `%s` (%s) ; différentiel `%s` (%s)." % (n, B % n, e(B % n), m, B % m, e(B % m), f1, e(f1), f2, e(f2), f3, e(f3)))
    w("- " + raison)
    w("- %d couples ; %d blocs au différentiel versé ; %d hunks au `diff -u` recalculé." % (ctl[k]["nb"], ctl[k]["h0"], ctl[k]["h3"]))
    w("")
    w("| couple | lieu (script des couples) | lignes (brouillon %d) | classe | nature | ce qui change | raison | bloc ; hunk |" % m)
    w("|---|---|---|---|---|---|---|---|")
    cc = {"R": 0, "E": 0, "M": 0}
    for d in res[k]:
        cl, nat, quoi, comp = A[k][d["id"]]; cc[cl] += 1
        meta = d["meta"]; tache = str(meta[0]); lieu = str(meta[1]).replace("|", "\\|")
        lg = "%d" % d["l_arr"] if d["l_arr"] == d["l_arr_fin"] else "%d à %d" % (d["l_arr"], d["l_arr_fin"])
        rs = fr(tache) + (" ; " + comp if comp else "")
        hh = "bloc%s %s ; hunk%s %s" % ("s" if len(d["h0"]) > 1 else "", ", ".join(map(str, d["h0"])), "s" if len(d["h3"]) > 1 else "", ", ".join(map(str, d["h3"])))
        w("| %s | %s | %s | %s | %s | %s | %s | %s |" % (d["id"], lieu, lg, cl, nat, quoi.replace("|", "\\|"), rs, hh))
    comptes["%d→%d" % (n, m)] = cc
    w("")
    if k == "4-5":
        w("Classement propre du brouillon 5 (sa table « Changements du brouillon 4 au brouillon 5 », seize lignes) : « règle » pour ses")
        w("lignes 3, 4, 6, 8, 12 et 13 (13 : « règle, conditionnelle ») ; « lettre » pour 1, 2, 5, 7, 9, 10, 11, 14, 15 ; « forme » pour 16.")
        w("Le classement ci-dessus s'y accorde, couple par couple, à ceci près : L05 (ligne E7 d'une table du bloc « Brouillon 4 ») est classé")
        w("M ici parce que le couple n'écrit qu'une ligne d'histoire, la règle étant portée par L23, L29 et L34 ; L36 et L37 sont classés E.")
        w("")
    if k == "5-6":
        w("Classement propre du brouillon 6 (sa table « Changements du brouillon 5 au brouillon 6 », dix lignes) : « règle » pour ses lignes")
        w("2, 3, 4 et 5 ; « lettre » pour 1, 6, 7, 8 et 9 ; « forme » pour 10. **Écart de classement, dit** : sa ligne 1 (nœud N12 tranché)")
        w("est dite « lettre (la règle écrite est celle retenue ; deux règles conditionnelles retirées) » ; les couples P10, P16 et P29, qui")
        w("retirent ces deux règles conditionnelles, sont classés R ici, dans le doute. P23 à P26 sont classés E.")
        w("")
# ---- étape 6 -> candidat
w("## Étape 5 — du brouillon 6 au candidat")
w("")
w("- Pièces : brouillon 6 `%s` (%s) ; candidat `%slecture-sondes-bbis-par-lentilles-v2-candidat.md` (%s), différentiel" % (B % 6, e(B % 6), SC, e(CAND)))
w("  `%sdifferentiel-brouillon6-candidat.diff` (%s) et script `%sapplique.py` (%s), tous trois sur la branche" % (SC, e(S + "/differentiel-brouillon6-candidat.diff"), SC, e(S + "/applique.py")))
w("  principale ; rapport qui motive les deux couples : `%s` (%s), corrections R1 et R2." % (AUTRES[0], e(AUTRES[0])))
w("- 2 couples ; 2 hunks.")
w("")
w("| couple | lieu | lignes (candidat) | classe | nature | ce qui change | raison | hunk |")
w("|---|---|---|---|---|---|---|---|")
w("| R2 | bloc « Brouillon 5 », « Auteur » | 184 à 187 | M | citation | le mot « go reco » du départ du rédacteur du brouillon 5, dit « mot rapporté » au brouillon 6, est dit consigné depuis par la session principale : ligne GO-2026-11-20-17 de `registres/go.md`, inscrite par la ligne R-4104 | vérification des corrections du brouillon 6, R2 (recommandée) ; GO-2026-11-20-17 | hunk 1 (`@@ -184,3 +184,4 @@`) |")
w("| R1 | « Nœuds », alinéa « Ouverts au brouillon 2, tranchés par Lazar le 2026-11-20 » | 2707 | R (dans le doute) | marqueur porté | le marqueur de la ligne d'accord des nœuds N12 et N17 est remplacé par la ligne GO-2026-11-20-18 de `registres/go.md`, son objet, l'événement relu à la source, et l'heure d'inscription par la ligne R-4104 (2026-11-20T05:34:13Z), « heure que recopie la pièce de `GO-LENTILLES-BBIS-V2` » | vérification des corrections du brouillon 6, R1 (exigée) ; GO-2026-11-20-18 | hunk 2 (`@@ -2706 +2707 @@`) |")
w("")
w("Les numéros de lignes sont ceux du différentiel versé (sans ligne de contexte). Le marqueur")
w("`LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17` (nom écrit ici sans chevrons) n'a plus d'occurrence entre chevrons dans le candidat.")
w("")
comptes["6→candidat"] = {"R": 1, "E": 0, "M": 1}
w("## Compte des changements par étape")
w("")
w("Unité : pour l'étape 2 → 3, une ligne de la table ci-dessus ; pour les autres, un couple.")
w("")
w("| étape | changements | R (règle de lecture) | E (essais d'une règle) | M (mots, citations, marqueurs, histoire) | hunks du `diff -u` |")
w("|---|---|---|---|---|---|")
tot = {"R": 0, "E": 0, "M": 0}; HK = {"2→3": 3, "3→4": ctl["3-4"]["h3"], "4→5": ctl["4-5"]["h3"], "5→6": ctl["5-6"]["h3"], "6→candidat": 2}
for etp in ("2→3", "3→4", "4→5", "5→6", "6→candidat"):
    c = comptes[etp]
    for x in tot: tot[x] += c[x]
    w("| %s | %d | %d | %d | %d | %d |" % (etp, sum(c.values()), c["R"], c["E"], c["M"], HK[etp]))
w("| **total** | **%d** | **%d** | **%d** | **%d** | **%d** |" % (sum(tot.values()), tot["R"], tot["E"], tot["M"], sum(HK.values())))
w("")
w("## Ce qui change une règle de lecture")
w("")
w("Une ligne par règle changée ; les couples classés R qui la portent (un couple peut porter plusieurs règles) ; les essais (classe E)")
w("sont nommés à part.")
w("")
w("| n° | étape | règle changée | couples ou hunk |")
w("|---|---|---|---|")
for i, (etp, txt, hk, cs) in enumerate(THEMES, 1):
    w("| %d | %s | %s | %s |" % (i, etp, txt, hk if hk else ", ".join(cs)))
w("")
w("Essais qui accompagnent ces règles (classe E) : K30b, K30c, K30d (brouillon 4) ; L36, L37 (brouillon 5) ; P23, P24, P25, P26")
w("(brouillon 6).")
w("")
w("La règle 18 (brouillon 5) est retirée par les règles 19 à 21 (brouillon 6) : au candidat, il ne reste des nœuds N12 et N17 que")
w("l'option (a) de chacun.")
w("")
w("## Ce qui ne change que des mots, des citations, des marqueurs ou l'histoire")
w("")
for etp, k in (("3 → 4", "3-4"), ("4 → 5", "4-5"), ("5 → 6", "5-6")):
    grp = {}
    for d in res[k]:
        cl, nat, *_ = A[k][d["id"]]
        if cl != "M": continue
        g = ("marqueurs" if "marqueur" in nat else "citations" if nat.startswith("citation") else "histoire (blocs, tables des changements, pieds, entrées de contre-lecture)" if nat.startswith("histoire") or nat.startswith("nœuds") else "mots")
        grp.setdefault(g, []).append(d["id"])
    w("- **Étape %s** : " % etp + " ; ".join("%s : %s" % (g, ", ".join(v)) for g, v in grp.items()) + ".")
w("- **Étape 2 → 3** : le bloc de tête (hunk 1). **Étape 6 → candidat** : R2 (citation).")
w("")
w("Marqueurs, d'une étape à l'autre (d'après les couples) : au brouillon 4, un porté (vérification du bloc séparable : K09b, K15) et deux")
w("ajoutés (K09c, K31d) ; au brouillon 5, ces deux-là portés (L07, L24, L39, L41) ; au brouillon 6, un ajouté (P04, P28) ; au candidat,")
w("celui-ci porté (R1). Le bloc séparable de « Hypothèse » est touché par K15 et K16 (brouillon 4) et par L18 et L19 (brouillon 5) :")
w("mots seuls, les brouillons disant qu'aucune valeur chiffrée n'y bouge ; il n'est touché ni au brouillon 3, ni au brouillon 6, ni au candidat.")
w("")
w("## Écarts trouvés")
w("")
w("1. **Aucun hunk non expliqué** du brouillon 2 au brouillon 3 (deux détails listés à l'étape 1).")
w("2. **Forme des différentiels versés** : ceux des étapes 3 → 4, 4 → 5 et 5 → 6 sont au format normal de `diff`, non au format unifié ;")
w("   celui du brouillon 6 au candidat est unifié sans ligne de contexte. Recalculés dans leur propre forme, les quatre sont **égaux à")
w("   l'octet** aux pièces versées ; contre un `diff -u` à trois lignes de contexte, ils diffèrent par la forme seule.")
w("3. **Aucun bloc de différentiel sans couple, aucun couple sans bloc**, aux étapes 3 → 4, 4 → 5 et 5 → 6 ; les deux hunks du candidat sont")
w("   les couples R1 et R2 du rapport de vérification.")
w("4. **Écart de classement** avec le brouillon 6 sur le nœud N12 (« lettre » chez lui, R ici, dans le doute) : dit à l'étape 4.")
w("5. **Limite de cette pièce** : les couples longs ont été lus coupés (voir « Pièces lues ») ; le lieu, les lignes et les hunks de")
w("   chaque couple viennent du programme, sa nature du début de son texte et des tables des brouillons.")
w("")
w("Pied : pièce fabriquée par programme dans le bloc-notes du rédacteur (les contrôles ci-dessus sont des assertions du programme : il")
w("n'écrit rien si l'une échoue), puis versée et scellée. Aucun refus d'outil, de permission ni de classifieur.")
open(SORTIE, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(json.dumps(comptes, ensure_ascii=False)); print(len(L), "lignes")
