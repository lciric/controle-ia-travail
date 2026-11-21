"""Outil de rédaction du brouillon 5 : lit le brouillon 4 (empreinte vérifiée), applique une liste de retouches dont chaque
ancre doit se trouver le nombre de fois dit (une, sauf mention), et écrit le brouillon 5 comme un fichier entier. Écrit aussi
la table de traitement de la vérification du brouillon 4 (la même que l'annexe A0 du brouillon 5).
Appel : python3 assembler-brouillon5-v1.py brouillon4.md brouillon5.md table-de-traitement.md
"""
import hashlib
import sys

src, dst, dst_table = sys.argv[1:4]
t = open(src, encoding="utf-8").read()
assert hashlib.sha256(t.encode("utf-8")).hexdigest() == "1a11b635bf285b3e2ea3779da9226ba14cdde06fffe67907aeab95606a74a10f"
N_RETOUCHES = 0


def r(ancre, neuf, n=1):
    global t, N_RETOUCHES
    assert t.count(ancre) == n, (t.count(ancre), ancre[:80])
    t = t.replace(ancre, neuf)
    N_RETOUCHES += 1


def section(debut, fin, neuf):
    global t, N_RETOUCHES
    assert t.count(debut) == 1 and t.count(fin) == 1, (t.count(debut), t.count(fin), debut[:60])
    i, j = t.index(debut), t.index(fin)
    assert i < j
    t = t[:i] + neuf + t[j:]
    N_RETOUCHES += 1


# ------------------------------------------------------------------ en-tête
r("# Conception de l'organisme retenu du saboteur à budget — v5, brouillon 4",
  "# Conception de l'organisme retenu du saboteur à budget — v5, brouillon 5")
r("Les brouillons 1 (`85ab3a38…`), 2 (`a5dc6b36…`) et 3 (`cb39c12b…`) et les textes d'avant restent intacts",
  "Les brouillons 1 (`85ab3a38…`), 2 (`a5dc6b36…`), 3 (`cb39c12b…`) et 4 (`1a11b635…`) et les textes d'avant restent intacts")
r("- **Statut** : brouillon 4, pièce décisive (classe A), pour le scellement une fois les sept nœuds tranchés et les corrections vérifiées par le vérificateur du brouillon 3 (`07b5ed3a…` : scellable après corrections ; aucun bloquant, cinq majeurs, douze mineurs, tous traités en annexe A).",
  "- **Statut** : brouillon 5, pièce décisive (classe A), pour le scellement une fois les sept nœuds tranchés. Vérification du brouillon 3 (`07b5ed3a…` : cinq majeurs, douze mineurs) traitée au brouillon 4 (annexe A) ; vérification du brouillon 4 (`d00a7a67…` : scellable après corrections ; aucun bloquant, un majeur, cinq mineurs) traitée ici (annexe A0).")
r("pour ce brouillon 4, un rédacteur neuf (Claude Fable 5.2)", "pour les brouillons 4 et 5, un rédacteur neuf (Claude Fable 5.2)")
r("la table des nœuds, 5.2 bis, 10.4 ter, la section 17, l'annexe A, l'annexe C et les retouches listées au fichier des différences.",
  "la table des nœuds, 5.2 bis, 10.4 ter, la section 17, les annexes A0, A et C et les retouches listées aux deux fichiers des différences.")

# ------------------------------------------------------------------ table des nœuds
r("(c) règle sur les épisodes acceptés, avant la distillation, niveau 1/40 | **(a)**, confiance moyenne |",
  "(c) règle sur les épisodes acceptés, avant la distillation, niveau 1/40 — **dimensionnée en partie** : puissance à 1/40 citée pour 96 épisodes seulement (×2 vu 98,8 % des fois), non pour 48 | **(a)**, confiance moyenne |")
r("(b) ôter la marge de moitié pour [N] seul ; (c) relever le plafond de tours (devis) |",
  "(b) ôter la marge de moitié pour [N] seul — **dimensionnée en partie** : conditions et erreurs jouées, sauf l'aboutissement des courses parties ; (c) relever le plafond de tours (reporte le scellement d'un devis, non d'un passage) |")
r("| 7 | Jouer pendant la course l'oracle que l'issue n'a pas nommé ? | (a) partout ; (b) à l'étalonnage et sur les épisodes acceptés du maître ; (c) non | **(b)**, confiance moyenne | le nombre d'oracles par tour et les actions d'oracle hors tours, dans le fichier d'entrées scellé : (a) 2 et 0 ; (b) 1 et 960 ; (c) 1 et 0 — donc le plafond de tours (10.2) |",
  "| 7 | Jouer après l'étalonnage l'oracle que l'issue n'a pas nommé ? | (a) partout : tous les épisodes du maître et l'évaluation ; (b) sur les seuls épisodes acceptés du maître, rien à l'évaluation — le niveau de l'élève n'est alors pas lu, et la promesse « rapporté à côté » est retirée partout ; (b') comme (b), plus l'évaluation (2 560 actions d'oracle de plus) — la promesse est tenue ; (c) non | **(b')**, confiance moyenne : la moins chère des options qui tiennent ce que 5.1 et 10.6 promettent sous l'issue [P] | le nombre d'oracles par tour et les actions d'oracle hors tours, dans le fichier d'entrées scellé : (a) 2 et 0 ; (b) 1 et 960 ; (b') 1 et 3 520 ; (c) 1 et 0 — donc le plafond de tours (10.2) ; sous (b) ou (c), les phrases « rapporté à côté » récrites comme dit en 17 |")

# ------------------------------------------------------------------ 5.1, 6, 15 : reprise ; niveau du maître
r("Toute reprise est une course neuve, sous devis neuf. **Aucune issue n'est laissée à une décision prise après l'étalonnage.**",
  "Toute reprise est une course neuve, sous devis neuf, **et l'issue de cet étalonnage est rapportée avec tout résultat de la reprise** ; il en va de même après une issue « ne part pas ». **Aucune issue n'est laissée à une décision prise après l'étalonnage.**")
r("toute reprise est une course neuve, sous devis neuf |",
  "toute reprise est une course neuve, sous devis neuf, et l'issue de cet étalonnage est rapportée avec tout résultat de la reprise |", n=2)
r("**sous [P], l'oracle [N] calculé sur les mêmes épisodes donne le niveau, en rapporté**.",
  "**sous [P], l'oracle [N] calculé sur les mêmes épisodes donne le niveau, en rapporté** — après l'étalonnage, sur les épisodes acceptés du maître (nœud 7, options (b) et (b') ; sur tous sous (a) ; sur aucun sous (c)).")

# ------------------------------------------------------------------ 10.2 et 12
r("actions hors tours 0. Le coût fixe porte alors l'évaluation à deux oracles.\n  - **Nœud 7, option (b)** (seulement sur les épisodes acceptés du maître) : nombre d'oracles par tour 1 ; actions hors tours 960 (96 épisodes acceptés au plus × 10).\n  - **Nœud 7, option (c)** : nombre d'oracles par tour 1 ; actions hors tours 0.",
  "actions hors tours 0. Le coût fixe porte alors l'évaluation à deux oracles.\n  - **Nœud 7, option (b)** (seulement sur les épisodes acceptés du maître, rien à l'évaluation) : nombre d'oracles par tour 1 ; actions hors tours 960 (96 épisodes acceptés au plus × 10). Le coût fixe porte l'évaluation à un seul oracle, celui que l'issue a nommé.\n  - **Nœud 7, option (b')** (les épisodes acceptés du maître et l'évaluation) : nombre d'oracles par tour 1 ; actions hors tours 3 520 (960 + les 2 560 actions d'évaluation de l'oracle non nommé). Le coût fixe porte l'évaluation à un seul oracle ; celle du second est comptée dans les actions hors tours, non dans le coût fixe. R_plafond = partie entière de (plafond − dépense passée − dépense de l'étalonnage − coût fixe − prix horaire × durée d'une action d'oracle × 3 520) / (prix horaire × 32 × (durée d'un épisode généré + 10 × durée d'une action d'oracle)).\n  - **Nœud 7, option (c)** : nombre d'oracles par tour 1 ; actions hors tours 0. Le coût fixe porte l'évaluation à un seul oracle.")
r("option (b), 960 au plus (11 200 en tout) ; option (c), aucune (10 240).",
  "option (b), 960 au plus (11 200 en tout) ; option (b'), 3 520 au plus (13 760 en tout) ; option (c), aucune (10 240).")

# ------------------------------------------------------------------ 17
r("Sa puissance au niveau 1/40 sur 48 à 96 épisodes n'est pas citée dans ce texte (les chiffres cités à 1/40 sont ceux de 64 et de 128 épisodes : ×2 vu 93 % des fois sur 64).",
  "**Dimensionnée en partie** : au niveau 1/40, un gonflement de ×2 de tous les premiers coûts est vu 98,8 % des fois sur 96 épisodes (forme la moins favorable ; sortie du passage du contrôle du premier coût, ligne 292) et 93 % sur 64 ; pour 48 épisodes, la grille de ce passage ne contient pas le chiffre.")
r("un épisode à excès planté n'est pas accepté assez plus souvent que le bruit honnête (k_P contre k_H). » ;",
  "un épisode à excès planté n'est pas accepté assez plus souvent que le bruit honnête (k_P contre k_H). » ; sous l'issue [N], la phrase d'arrêt au tour de contrôle se lit « accepté a fois sur n, pour **k_P** sur 64 à l'instrument » ;")
r("- **(b) Ôter la marge de moitié pour [N] seulement.** **Rapporté** dans le passage",
  "- **(b) Ôter la marge de moitié pour [N] seulement.** **Dimensionnée en partie** : les conditions et les erreurs sont jouées, l'aboutissement des courses parties ne l'est pas. **Rapporté** dans le passage")
r("- **(c) Relever le plafond de tours** : affaire de devis ;", "- **(c) Relever le plafond de tours** : affaire de devis (la retenir reporte le scellement d'un devis, non d'un passage) ;")

section("### Nœud 7 — Jouer pendant la course l'oracle que l'issue n'a pas nommé", "## 18. Ce que ce texte ne prouve pas", r"""### Nœud 7 — Jouer après l'étalonnage l'oracle que l'issue n'a pas nommé

Ce nœud change ce que le résultat peut dire : sous l'issue [P], seul l'oracle [N] lit un niveau. Le texte courant (5.1, table des revendications ; 10.6, lecture du dommage ; section 11) promet que le niveau de l'élève est « rapporté à côté » : il faut, pour le tenir, que [N] soit joué à l'évaluation.

- **(a) Oui, sur tous les épisodes du maître et à l'évaluation** : 6 400 actions d'oracle de plus à 12 tours ; donne le niveau sous l'issue [P], l'ajout par pas sous l'issue [N], et de quoi lire le nœud 3 (a) sur les quatre premiers tours. *Fichier d'entrées scellé* : nombre d'oracles par tour 2 ; actions d'oracle hors tours 0 ; le coût fixe porte l'évaluation à deux oracles. *Plafond de tours* : le plus bas des quatre. *Texte* : tel quel, sauf la section 6, point 4, où « sur les épisodes acceptés du maître » devient « sur tous les épisodes du maître ».
- **(b) Seulement sur les épisodes acceptés du maître ; rien à l'évaluation** : 960 actions d'oracle de plus au plus. *Fichier d'entrées scellé* : nombre d'oracles par tour 1 ; actions d'oracle hors tours 960 ; le coût fixe porte l'évaluation à un seul oracle, celui que l'issue a nommé. **Le niveau de l'élève n'est alors lu par rien, et la promesse est retirée partout.** *Texte* : (i) le rapporté du nœud 3 (a) ne porte que sur les épisodes acceptés ; les phrases de 10.6 qui citent « l'autre oracle » pendant la course disent « sur les épisodes acceptés » ; (ii) 5.1, table des revendications, issue [P], case « ce que la lecture du dommage peut dire » : « le niveau, lu par [N], est rapporté à côté sans phrase de résultat » devient « le niveau du maître, lu par [N] sur ses épisodes acceptés, est rapporté à côté ; celui de l'élève n'est pas lu » ; même table, issue [N], case « thèse non revendiquée, et dite » : « rapporté par [P] sur les mêmes épisodes » devient « rapporté par [P] à l'étalonnage et sur les épisodes acceptés du maître ; l'ajout par pas de l'élève n'est pas lu » ; (iii) 10.6, phrase [P] de la lecture du dommage positive : « le niveau, lu par l'autre oracle, est rapporté à côté » devient « le niveau de l'élève n'est pas lu (nœud 7, option (b)) » ; (iv) section 11, [P], dernière phrase : « Le niveau des deux, lu par [N] et contre le modèle de base, est rapporté. » devient « Le niveau des deux n'est pas lu : rien ne dit si l'élève et son témoin déclarent trop en niveau. » ; (v) section 18, une ligne de plus : « Sous l'issue [P], que l'élève déclare ou non des coûts trop hauts en niveau : rien ne le lit. »
- **(b') Comme (b), étendue à l'évaluation** : l'oracle non nommé joue sur les épisodes acceptés du maître et sur les épisodes d'évaluation ; 960 + 2 560 = 3 520 actions d'oracle de plus au plus (13 760 en tout à 12 tours). *Fichier d'entrées scellé* : nombre d'oracles par tour 1 ; actions d'oracle hors tours 3 520 ; le coût fixe porte l'évaluation à un seul oracle, celle du second étant comptée dans les actions hors tours. *Plafond de tours* : la formule de 10.2, écrite pour cette option ; à durées égales, il est inférieur ou égal à celui de (b), de ce que coûtent 2 560 actions d'oracle rapportées au coût d'un tour, et au moins égal à celui de (a) dès que la course compte trois tours (sous (a), l'oracle non nommé joue 320 actions par tour). *Texte* : **tel quel** — c'est l'option que le texte courant porte ; le rapporté du nœud 3 (a) ne porte que sur les épisodes acceptés, comme sous (b), point (i).
- **(c) Non** : *fichier d'entrées scellé* : 1 et 0 ; le coût fixe porte l'évaluation à un seul oracle. *Texte* : les points (ii) à (v) de l'option (b), où « sur ses épisodes acceptés » devient « à l'étalonnage seulement » : sous l'issue [P], ni le niveau du maître pendant la course ni celui de l'élève ne sont lus ; section 6, point 4, la mesure du niveau du maître est retirée après l'étalonnage.
- **Dans les quatre cas**, R_plafond se calcule par la formule de 10.2 avec ces deux entrées ; sa valeur dépend des durées mesurées à l'étalonnage et du plafond du devis, et ne peut donc pas être écrite ici en nombre de tours. Dans la simulation il vaut 24, par hypothèse, quelle que soit l'option.
- **Recommandation, et défaut : (b')** ; confiance moyenne. Raison : sous l'issue [P], la plus probable (80 % à 85 % des étalonnages simulés), la lecture du dommage et le témoin ne disent rien du niveau ; sans [N] à l'évaluation, un élève et son témoin pourraient tous deux déclarer dix fois trop sans que rien le lise. (b') tient cette lecture pour un coût fixe de 2 560 actions, sans toucher au coût d'un tour. (a) si le devis le porte ; (b) si le directeur accepte que le résultat ne dise rien du niveau de l'élève. Je ne tranche pas.

""")

# ------------------------------------------------------------------ vérification, annexes
TABLE = r"""| remarque du vérificateur du brouillon 4 (`d00a7a67…`) | traitement | où |
|---|---|---|
| **R1** (majeur), sous l'option (b) du nœud 7, une phrase promet le niveau de l'élève « rapporté à côté » alors que l'oracle non nommé ne joue pas à l'évaluation | les deux variantes écrites, sans trancher : (b), qui retire la promesse partout (cinq retouches dites : 5.1 deux cases, 10.6, section 11, section 18) ; (b'), qui étend (b) à l'évaluation (2 560 actions de plus, 3 520 hors tours, plafond de tours et coût fixe en formule). Recommandation et défaut : (b') ; le texte courant est celui de (b'). Ligne de la table des nœuds refaite ; section 6, point 4, précisée (épisodes acceptés du maître) | table des nœuds ; 6 ; 10.2 ; 12 ; 17, nœud 7 |
| m-a, 4 (b) et 1 (c) offertes comme prêtes | marquées « dimensionnées en partie » dans la table et en 17 ; 1 (c) : ×2 vu 98,8 % des fois sur 96 épisodes au niveau 1/40 (contrôlé sur la sortie, ligne 292, forme « tel quel », la moins favorable des deux), rien pour 48 ; 4 (c) : reporte le scellement d'un devis | table des nœuds ; 17, nœuds 1 et 4 |
| m-b, une reprise est un chemin qui bifurque | « l'issue de cet étalonnage est rapportée avec tout résultat de la reprise », après « non calculable » comme après « ne part pas » | 5.1 ; 15 (deux lignes) |
| m-c, k_P dans la phrase d'arrêt du tour de contrôle sous 2 (b) | ajouté au point (iii) | 17, nœud 2 |
| m-d, ce que porte le coût fixe sous 7 (b) et 7 (c) | écrit : l'évaluation à un seul oracle ; sous (b'), celle du second est dans les actions hors tours | 10.2 ; 17, nœud 7 |
| m-e, copie de contrôle hors du dossier et copie supprimée | rien à corriger dans la pièce ; déclaré au journal v7, redit au journal v8 ; l'outil du brouillon 5 n'écrit aucune copie de contrôle hors du dossier et rien n'est supprimé | journaux |
| écart d'arrondi relevé au sondage (1,95 % écrit « 1,9 % », section 8) | **non retouché** : hors des restes listés, et le cadre du brouillon 5 est de ne toucher à rien d'autre ; signalé ici | — |
"""

r("## Vérification\n\nÀ faire par le vérificateur du brouillon 3",
  "## Vérification\n\nLe brouillon 4 a été vérifié (`d00a7a67…`) ; ses restes sont traités ici (annexe A0), avec le fichier des différences du brouillon 4 au brouillon 5 et l'outil `assembler-brouillon5-v1.py`. Le paragraphe qui suit est celui du brouillon 4, gardé.\n\nÀ faire par le vérificateur du brouillon 3")
r("## Annexe A — Vérification du brouillon 3 (`07b5ed3a…`) : table de traitement\n",
  "## Annexe A0 — Vérification du brouillon 4 (`d00a7a67…`) : table de traitement\n\n" + TABLE + "\n## Annexe A — Vérification du brouillon 3 (`07b5ed3a…`) : table de traitement\n")
r("**Pièces du brouillon 4**, dossier du second rédacteur ; un compagnon `.sha256` par fichier ; les empreintes entières sont dans les compagnons et dans le journal v7.",
  "**Pièces du brouillon 5**, dossier du second rédacteur ; un compagnon `.sha256` par fichier : `assembler-brouillon5-v1.py` (outil de rédaction, rendu : lit le brouillon 4, empreinte vérifiée à l'ouverture, applique des retouches à ancres comptées, écrit ce texte entier et la table de l'annexe A0 ; le relancer redonne ce texte à l'octet) ; `differences-brouillon4-brouillon5-organisme-retenu-v1.md` ; `table-de-traitement-verification-brouillon4-v1.md` ; `journal-redaction-organisme-retenu-v8.md`. Aucun passage de simulation neuf.\n\n**Pièces du brouillon 4**, dossier du second rédacteur ; un compagnon `.sha256` par fichier ; les empreintes entières sont dans les compagnons et dans le journal v7.")
r("écrit le brouillon 4 entier et la table de traitement. Le relancer redonne ce texte à l'octet",
  "écrit le brouillon 4 entier et la table de traitement. Le relancer redonne le brouillon 4 à l'octet (rejoué par le vérificateur)")
r("| brouillons 1, 2 et 3 et tout ce qui précède | gardés, intacts | — |", "| brouillons 1, 2, 3 et 4 et tout ce qui précède | gardés, intacts | — |")

open(dst, "w", encoding="utf-8").write(t)
open(dst_table, "w", encoding="utf-8").write(
    "EXPLORATOIRE, NON OPPOSABLE (R-522)\n\n# Table de traitement — vérification du brouillon 4 (`d00a7a67d007155b15a7e749a842b69decd9d2c0053c847b8cd16f565e1b3674`) traitée au brouillon 5\n\n"
    "Identique à l'annexe A0 du brouillon 5 (même outil, même texte). Les sections citées sont celles du brouillon 5.\n\n" + TABLE)
print("retouches appliquees :", N_RETOUCHES, "; taille :", len(t.encode("utf-8")), "octets")
