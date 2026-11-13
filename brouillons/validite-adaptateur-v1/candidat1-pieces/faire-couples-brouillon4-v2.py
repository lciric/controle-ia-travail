"""Version 2 (après le mot de la mère du 13 novembre, journal du compte 4, C4-0009 : erratum cité par son fichier, champs confirmés au commit C7, marqueur à la place du commit C7). Écrit les couples du brouillon 4 « validité de l'adaptateur » (R12 : refuse d'écraser).

Usage : python3 -I faire-couples-brouillon4-v1.py HEURE_UTC SORTIE_JSON
- reprend tels quels les couples mécaniques de la contre-lecture 2 (bloc JSON de sa section 3),
  après vérification de l'empreinte du rapport scellé ;
- ajoute les couples de l'auteur du brouillon 4 (session du compte 4, Claude Opus 5.5).
"""
import hashlib, json, re, sys
from pathlib import Path

RAPPORT = Path("prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2.md")
SHA_RAPPORT = "11f7242b9dbada3fdc9f6e2c0a707eef3f0d2b51783e425545d78ec43d2bccee"

def couples_lecteur():
    if hashlib.sha256(RAPPORT.read_bytes()).hexdigest() != SHA_RAPPORT:
        sys.exit("ARRÊT : empreinte du rapport de la contre-lecture 2 différente")
    t = RAPPORT.read_text(encoding="utf-8")
    sec = t.split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    bloc = re.search(r"```json\n(.*?)\n```", sec, re.S).group(1)
    return json.loads(bloc)

M = "(T0.7 brouillon 21, levé par la contre-lecture 1 ; "
MARQUES = [
    ("A4-M01", M + "l. 1024, 1246)", "(T0.7 scellé, l. 1183, 2785)"),
    ("A4-M02", M + "l. 1773, 2348-2351)", "(T0.7 scellé, l. 1915 ; module sur `main`, `lecture_v4.py` l. 628-633)"),
    ("A4-M03", M + "l. 1157-1165, 1231-1236)", "(T0.7 scellé, l. 1293-1313, 1361, 2801 ; `lecture_v4.py` l. 495-499)"),
    ("A4-M04", M + "l. 1309-1312)", "(T0.7 scellé, l. 1451-1453, 2789)"),
    ("A4-M05", M + "code `8ae9fc44`, `lecture_v2.py` l. 606-607)", "(T0.7 scellé, l. 2789 ; `lecture_v4.py` l. 217-218, 259-262)"),
    ("A4-M06", M + "plan, point 8, l. 1385-1395)", "(T0.7 scellé, l. 2073, 2794 ; `repli_recalcul_v1.py` l. 179-216)"),
    ("A4-M07", M + "l. 1926-1931, 2339-2344 ; code `8ae9fc44`, `lecture_v2.py` l. 734-754, 901-902)", "(T0.7 scellé, l. 2049-2051, 2790, 2793 ; `lecture_v2.py` l. 764-789 ; `lecture_v4.py` l. 506)"),
    ("A4-M08", M + "l. 1054-1055)", "(T0.7 scellé, l. 1206 ; `lecture_v4.py` l. 137-141, 245-262)"),
    ("A4-M09", M + "code `8ae9fc44`, `lecture_v2.py` l. 608-609, 942)", "(T0.7 scellé, l. 2791 ; `lecture_v4.py` l. 262, 544-553)"),
    ("A4-M10", M + "levée 4)", "(T0.7 scellé, l. 2801 ; `mahalanobis_v1.py` l. 84-98)"),
    ("A4-M11", M + "l. 1085-1086, 2181)", "(T0.7 scellé, l. 1226-1229, 2312 ; configuration v8 l. 60-63)"),
    ("A4-M12", M + "l. 1157-1165)", "(T0.7 scellé, l. 1293-1313 ; `lecture_v4.py` l. 495-499)"),
    ("A4-M13", M + "l. 2083-2084, 2339-2344 ; code `8ae9fc44`, `lecture_v2.py` l. 942)", "(T0.7 scellé, l. 2790-2791 ; `lecture_v4.py` l. 495-506, 544-553)"),
    ("A4-M14", M + "l. 1398, 2067)", "(T0.7 scellé, l. 1540, 2188, 2252)"),
    ("A4-M15", M + "l. 2345, 2375 ; code `8ae9fc44`, `lecture_v2.py` l. 1081-1082 ; `criteres_v1.py` l. 586-600)", "(T0.7 scellé, l. 2792, 2800 ; `lecture_v4.py` l. 669-685 ; `criteres_v1.py` l. 586-600)"),
    ("A4-M16", M + "l. 2077)", "(T0.7 scellé, l. 2198-2205)"),
    ("A4-M17", M + "l. 1759-1766, 1798)", "(T0.7 scellé, l. 1900-1910, 2800 ; `criteres_v1.py` l. 504-532, 586-600)"),
    ("A4-M18", M + "l. 1777-1794)", "(T0.7 scellé, l. 1919-1921, 1927, 1935-1936, 2803 ; `lectures_t07_v1.py` l. 423-463)"),
    ("A4-M19", M + "l. 1956-1957)", "(T0.7 scellé, l. 2076-2078, 2086)"),
    ("A4-M20", M + "l. 2177-2178, 2322)", "(T0.7 scellé, l. 2309, 2454, 2805 ; `registre_v1.py` l. 138-148)"),
    ("A4-M21", M + "l. 2077-2084)", "(T0.7 scellé, l. 2198-2205 ; `registre_v1.py` l. 47-53)"),
]

def couples_auteur(h):
    c = []
    def a(i, ancien, nouveau): c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    a("A4-01", "honnête (iii) — v1 — brouillon 3", "honnête (iii) — v1 — brouillon 4")
    a("A4-02", "- Auteur : rédacteur neuf, sous-agent de la session mère (reprise du 2026-11-10",
      "- Auteur du **brouillon 4** : la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`), Claude Opus 5.5 (`claude-opus-5-5`), qui n'a écrit ni T0.6, ni T0.7, ni son module, ni P3-bis, ni la note 2a, ni les brouillons 1 à 3, ni leurs contre-lectures ; elle a lu T0.7 scellé en partie (exclue de tout rôle de lecteur ou d'hôte du verdict de P3-bis) ; le brouillon 4 est écrit par couples versés (`brouillons/validite-adaptateur-v1/candidat1-pieces/`), sur le brouillon 3 et la contre-lecture 2.\n- Auteur des brouillons 2 et 3 : rédacteur neuf, sous-agent de la session mère (reprise du 2026-11-10")
    a("A4-03", "; ce rédacteur ne l'a pas vérifié.",
      "; ce rédacteur ne l'a pas vérifié. **Brouillon 4** : ces marques sont remplacées par les renvois à T0.7 scellé et au module sur `main` que relève la contre-lecture 2 (CLVA2-09).")
    a("A4-04", "- Date (UTC) : écrit le 2026-11-10 à partir de 12:05 UTC",
      "- Date (UTC) : brouillon 4 écrit le 2026-11-13 à partir de " + h + " UTC (heure relevée par `date -u`) ; brouillon 3 écrit le 2026-11-10 à partir de 12:05 UTC")
    a("A4-05", "- Statut : **brouillon 3**, applique la contre-lecture 1 (CLVA-01 à CLVA-20)",
      "- Statut : **brouillon 4**, écrit sur le brouillon 3 (`defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd`) ; applique la contre-lecture 2 (CLVA2-01 à CLVA2-18 ; section « Contre-lecture ») : ses couples mécaniques tels qu'écrits ; **CLVA2-01 et CLVA2-10 selon la recommandation du lecteur (règle (a) de T0.7), en attente de la décision de la mère** ; **CLVA2-11 (pièce HD) selon l'option recommandée à Lazar par la session du compte 4, en attente de son mot (nœud)** ; non scellable comme préenregistrement avant ces deux réponses et la vérification courte prévue (section « Contre-lecture »). Le brouillon 3, lui, appliquait la contre-lecture 1 (CLVA-01 à CLVA-20)")
    a("A4-06", "La variante stricte est gardée pour mémoire en annexe A, « variante non retenue (R-2207) » : elle ne s'applique pas.",
      "**Brouillon 4 (CLVA2-11)** : la course 7b est finie le 12 novembre sans que la pièce HD ait été jouée ; **Q-1 est sans objet** : la pièce HD se joue après la fin de 7b, ce qui tient pour elle la lettre de la ligne (« course à part après la course 7b ») ; **Q-3 reste en vigueur** (pièce R sur une instance à part). La variante stricte est gardée pour mémoire en annexe A ; seule sa moitié « pièce R sur l'instance de l'étape A » reste « non retenue (R-2207) ».")
    a("A4-07", ": **non lus par ce rédacteur**, empreinte et commit cités par la contre-lecture 1 ; **réserve générale** : T0.7 n'est pas scellé, plusieurs champs ne sont fixés que par son code ; chaque levée est revérifiée sur T0.7 scellé et sur le commit de la ligne `CODE-T07` avant le scellement de ce texte, et le code de ce texte s'arrête (R11) si un champ manque ;",
      " : lus par la contre-lecture 2 (par sections et par motifs ; empreintes des huit modules neufs égales à celles de T0.7 scellé, l. 695) et, en partie, par l'auteur du brouillon 4 ; T0.7 scellé fixe lui-même les champs que lit ce texte (section « Concordance avec le texte de validité de l'adaptateur », l. 2783-2808) ; **erratum des 200 directions, cité, non corrigé** (note de la session mère, `docs/notes/g0-deux-semaines-v1/t07-module-v2/erratum-concordance-adaptateur-t07-scelle-v1.md`, `f593676248698b985f842f30f403e0036b1faa556335d1b1bcb7ed7a08080aea` : font foi les sections gelées et le code cité) : cette section écrit encore « forme (200, n_actions) » (l. 2789) et « lues dans le fichier léger de P3 (sondes figées) » (l. 2802), que dépassent T0.7 scellé lui-même (l. 1198 : 800 directions ; l. 1206 : plancher neuf des sondes figées) et le module (`lecture_v4.py` l. 176-178) : ce texte lit 800 directions et le plancher neuf ; **réserve générale levée par la contre-lecture 2, sauf** : les champs que fixe le seul code de T0.7 (rapport de la contre-lecture 2, § 4 : sous-clé `sondes.sha256` de `fichiers_sondes_neuves`, littéraux de `entrees.Q`, `resultat.planchers_figees`, `meta.planchers` de `planchers-figees-t07.npz`, `index.sondes[k].etat`, forme de `reserves_identifiees`) sont vérifiés par la contre-lecture 2 sur le code de `main`, puis confirmés par l'auteur du brouillon 4 sur le code au commit C7 de la ligne `CODE-T07` (`<<COMMIT_C7_T07>>`), égal à `main` sur les vingt-six modules, et sur le rapport v3 du développeur (`docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/rapport-code-plancher-v3-v3.md`, `be2c86e215a1a7a0e41f646e60acaa20a39f0b626c6cd1b0807066348305b159`) : pièce `brouillons/validite-adaptateur-v1/candidat1-pieces/confirmation-champs-t07-c7-v1.md`, `f91452ed3e34a83b7c1c33c0cd74219b9340a2bcfb9beea805e4509910b9f2e7` ; **réserve écrite : ils ne sont pas confirmés par le développeur de T0.7, non joignable** (sous-agents de sessions mères closes ; mot de la mère du 13 novembre) ; `reextraction_p3_v1.py`, qui écrit `planchers-figees-t07.npz`, change au commit C7 suivant (R-2593) : ses champs sont revérifiés au commit qui remplira le marqueur ; le code de ce texte s'arrête (R11) si un champ manque ;")
    a("A4-08", "  - contre-lecture 1, `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon2-cl1.md`",
      "  - contre-lecture 2, `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2.md`, `11f7242b9dbada3fdc9f6e2c0a707eef3f0d2b51783e425545d78ec43d2bccee`, et son script, `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2-calcul.py`, `26437692aacc32fb1522025e37cf0dd6b14059415167491d0de9bedbd057d945` ;\n  - contre-lecture 1, `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon2-cl1.md`")
    a("A4-09", "≥ 0,66 à 0,86 selon les effectifs", "≥ 0,67 à 0,88 selon les effectifs")
    a("A4-10", "tau ≥ ≈ 0,155 (dix lisibles par tâche)", "tau ≥ ≈ 0,165 (dix lisibles par tâche)")
    a("A4-11", "≈ 0,596 | idem |", "≈ 0,602 | idem |")
    a("A4-12", "≈ 0,596 | aucune (puissance) |", "≈ 0,602 | aucune (puissance) |")
    a("A4-13", "≈ 0,596 | aucune (puissance ; intensité rapportée) |", "≈ 0,602 | aucune (puissance ; intensité rapportée) |")
    a("A4-14", "mêmes étiquettes ; quantile 0,95 de leurs aires.",
      "mêmes étiquettes ; quantile 0,95 de leurs aires ; « au-dessus du plancher » se juge par la **règle (a) de T0.7** (section « Seuil » ; CLVA2-01).")
    a("A4-15", "pour chacune des 800 directions, quantile 0,95 ;",
      "pour chacune des 800 directions, quantile 0,95 ; **différence `Dτ`** = tau − quantile 0,95 des tau des 800 directions, tau et quantile recalculés sur les mêmes tâches tirées (analogue de la règle (a) de T0.7 ; non simulé par T0.7 : déclaré) ;")
    a("A4-16", "(aire minimale détectable supposée > 0,80)",
      "(aire minimale détectable supposée > 0,80 sous la règle du brouillon 3, > 0,82 sous la règle (a) ; seuil en σ inchangé)")
    a("A4-17", "VA-1, VA-3, VA-5b, VA-6 : borne basse **strictement supérieure** au quantile 0,95 du plancher ;",
      "VA-1, VA-3, VA-5b, VA-6 : **règle (a) de T0.7** (T0.7 scellé, l. 1258 ; CLVA2-01) : la borne basse de l'intervalle percentile, par blocs de tâches, de la **différence D = (aire de la ligne) − (quantile 0,95 des aires des 800 directions du plancher)**, aires de la ligne et des directions recalculées sur les mêmes tirages (2 000, niveau de la ligne), est **strictement positive** ; calculée par `plancher_v2.comparer_difference_au_plancher` au commit de `CODE-T07`, importée sans modification ; la règle du candidat 1 de T0.7 (borne basse de la ligne au-dessus du quantile), dont T0.7 scellé écrit que l'erreur réelle atteint 4 à 9 fois le nominal sous un plancher à signal commun (l. 2033, 2035), n'est pas employée ;")
    a("A4-18", "le quantile du plancher et l'état « au-dessus du plancher » sont écrits à côté (CLVA-05) ;",
      "le quantile du plancher et l'état « au-dessus du plancher » (règle (a)) sont écrits à côté (CLVA-05) ;")
    a("A4-19", "borne basse de l'intervalle du tau strictement supérieure **à la fois** à 0 et au quantile 0,95 des tau des 800 directions (CLVA-06) ;",
      "borne basse de l'intervalle du tau strictement supérieure à 0 **et** borne basse de l'intervalle de `Dτ` (section « Métrique ») strictement positive (CLVA-06 ; CLVA2-01 : analogue de la règle (a), non simulé par T0.7, déclaré) ;")
    a("A4-20", "aire, intervalle, quantile écrits.", "aire, intervalle, quantile, différence D (ou `Dτ`) et son intervalle écrits.")
    a("A4-21", "`[r]` accompagne toute phrase de VA-6) :",
      "`[r]` accompagne toute phrase de VA-6 ; **brouillon 4** : « au-dessus de son plancher [q] » et « plancher [q] » se lisent par la règle (a) et sont suivis de « (différence D [x] [bas ; haut]) », pour VA-2 de « (`Dτ` [x] [bas ; haut]) ») :")
    a("A4-22", "aire minimale détectable à 80 % = `0,5 + (1,645 + z + 0,842) σ` pour les lignes de soutien,",
      "aire minimale détectable à 80 % = `0,5 + (1,645 + 1,10 × (z + 0,842)) σ` pour les lignes de soutien sous la règle (a) (**brouillon 4**, CLVA2-10 : écart type de D pris à 1,10 fois celui de la sonde, rapport lu à l'audit de P3 que cite T0.7 scellé, l. 2030, supposé ; script `brouillons/validite-adaptateur-v1/candidat1-pieces/puissance-devis-brouillon4-v1.py`, sortie `sortie-puissance-devis-brouillon4-v1.txt`, mêmes valeurs que la contre-lecture 2, § 2 bis ; T0.7 scellé écrit que cette formule, qui tient le quantile du plancher pour fixe, sous-estime la perte, simulée à 0,16 à 0,35 par sonde, l. 2033 : valeurs optimistes ; brouillon 3 : `0,5 + (1,645 + z + 0,842) σ`),")
    a("A4-23", "| 0,857 ; 0,771 ; 0,698 ; 0,656 |", "| 0,881 ; 0,789 ; 0,711 ; 0,667 |")
    a("A4-24", "tau ≥ 0,155 / 0,180 / 0,254", "tau ≥ 0,165 / 0,192 / 0,271")
    a("A4-25", "0,596 (même ordre que T0.7, 0,600 à 0,635, rapport des prémisses § 2b)",
      "0,602 (T0.7 scellé, règle (a), 64 tâches, 98,75 % : 0,6408, 0,6058 et 0,5815 à 0,6658 selon la sonde, l. 2031)")
    a("A4-26", "vérifiée par ce rédacteur) ne la compte pas.",
      "vérifiée par ce rédacteur) ne la compte pas ; **brouillon 4** : 7b est finie ; l'étiquette ne gêne pas non plus la création de l'instance de l'étape A de T0.7 (T0.7 scellé, l. 2806 : étiquettes `t06…` et `t07…` seules).")
    a("A4-27", "**Ordre** (lecture large de `GO-2026-11-10-07`, R-2207) : création **après la création de 7b**, en parallèle de sa marche (la lettre de la liste d'arrêt de T0.6 — « une instance du programme déjà sur le compte : aucune création » — est ainsi tenue), et **après** `SCELLEMENT-VADAPT`, `CODE-VADAPT`, `GO-HD-VADAPT` ; détruite **avant la création de l'étape A** seulement si l'ordre en vigueur de l'étape A exige un inventaire vide (point ouvert de la mère) ; aucune décision (lancer, relancer, abandonner) prise sur une sortie de 7b, de T0.7 ou de P3-bis. Variante stricte : annexe A.",
      "**Ordre** (**brouillon 4**, CLVA2-11 ; **option recommandée à Lazar, en attente de son mot (nœud)** ; au brouillon 3 : création après la création de 7b, en parallèle de sa marche, lecture large de `GO-2026-11-10-07`, R-2207, Q-1 — sans objet depuis la fin de 7b le 12 novembre) : la pièce HD n'a pas été jouée pendant 7b ; elle se joue **après la fin de 7b**, ce qui tient la lettre de la ligne (« course à part après la course 7b »). Création strictement **après** `SCELLEMENT-VADAPT`, `CODE-VADAPT`, `GO-HD-VADAPT` et `VERDICT-P3BIS`. **Règle de lancement, mécanique, écrite avant `VERDICT-P3BIS`** : la pièce HD est créée **si et seulement si** E8 → `issue` vaut « vu » ; sinon elle n'est pas créée et ses lignes sont « non lues (G-1) », comme toutes les autres lignes sous G-1 (rien de ce qui serait lu n'est perdu). La condition remplie, la pièce HD est jouée quelle que soit toute autre sortie (7b, table A, T0.7, P3-bis) ; aucune autre décision (lancer, relancer, abandonner) n'est prise sur une sortie de 7b, de T0.7 ou de P3-bis. Les courses louées de ce texte se jouent l'une après l'autre, après relevé du crédit, par la session tenante que désigne la mère. Variante stricte : annexe A (seule sa moitié « pièce R sur l'instance de l'étape A » reste non retenue).")
    a("A4-28", "VA-6 et ses contrôles « non calculables (pièce HD absente) ».",
      "VA-6 et ses contrôles « non calculables (pièce HD absente) » ; **sans sorties poussées de l'étape A de T0.7** (`SCORES-T07`, `SONDES-T07`), **aucune pièce R** : VA-5, VA-6 et leurs contrôles « non calculables (pièce R non jouée) » (CLVA2-11).")
    a("A4-29", "(journal de T0.7, l. 1316) ; le développeur du module de T0.7 confirme avant `CODE-VADAPT` qu'aucune garde de T0.7 ne compte les ouvertures de `scores-actions-t07.npz` par un autre moyen.",
      "(journal de T0.7 ; T0.7 scellé, l. 1458, 2804) ; T0.7 scellé écrit qu'aucune de ses gardes ne compte les ouvertures de `scores-actions-t07.npz` (section « Concordance », point 7, l. 2804 ; vérifié par son rédacteur sur le code, à la place de la confirmation du développeur), et la contre-lecture 2 l'a revérifié sur le module de `main` (`lecture_v2.premiere_ouverture_a`, `registre_v1.journaliser_ouverture`, `lecture_v1.ouvrir_scores`) : aucune confirmation ne reste exigée sur ce point (CLVA-17).")
    a("A4-30", "recopiée au journal (`devis_puissance_vadapt_b3.py`).",
      "recopiée au journal (`devis_puissance_vadapt_b3.py`) ; **brouillon 4** (CLVA2-07, CLVA2-13) : `brouillons/validite-adaptateur-v1/candidat1-pieces/puissance-devis-brouillon4-v1.py`, sortie `sortie-puissance-devis-brouillon4-v1.txt`.")
    a("A4-31", "| ≈ 2 368 passes × 0,45 s | 0,30 + 0,05 |",
      "| ≈ 2 816 passes × 0,45 s (séries 1 856 ; recalcul de T0.7 sur les 576 épisodes de 7b, + 192 ; recherche de `c_d` à douze pas, 768) | 0,35 + 0,05 |")
    a("A4-32", "**1,85 à 2,75** | calcul 2,0 à 3,6 ; téléchargement ≤ 1 : **≈ 2,4 à 4,6** | 5,5 h × 1,40 = 7,7 + 1 ≈ **8,7**",
      "**1,90 à 2,80** | calcul 2,1 à 3,6 ; téléchargement ≤ 1 : **≈ 2,5 à 4,6** | 5,6 h × 1,40 = 7,8 + 1 ≈ **8,85**")
    a("A4-33", "**≈ 9,2 à 10,4 h** | **≈ 11,0 à 17,1** | **≈ 33,2** |", "**≈ 9,3 à 10,4 h** | **≈ 11,0 à 17,2** | **≈ 33,4** |")
    a("A4-34", "(CLVA-09 (b), forme de T0.7, l. 1966)", "(CLVA-09 (b), forme de T0.7 ; T0.7 scellé, l. 2086)")
    a("A4-35", "**Le pire cas entier ne tient pas sous 30 USD** (≈ 33,2) : **nœud N-VA-1** (journal, § 3).",
      "**Le pire cas entier ne tient pas sous 30 USD** (≈ 33,4 au brouillon 4, 33,2 au brouillon 3 ; le pire de R dépasse sa coupure de 0,35 USD) : **nœud N-VA-1** (journal du brouillon 3, § 3 ; ouvert à la connaissance de l'auteur du brouillon 4, qui n'a pas lu le registre).")
    a("A4-36", "texte contre-lu et scellé le 12 au soir (R-2177), donc avant `VERDICT-P3BIS` (plan, point 4) ; HD créée après la création de 7b (12 ou 13), ≈ 7,5 h ; R après la poussée de l'étape A et de HD (≈ 14 à 17) ; L après `VERDICT-P3BIS`, la table A et l'étape B de T0.7 (≈ 16 à 22).",
      "(**brouillon 4** ; celui du brouillon 3 — texte scellé le 12 au soir, R-2177 ; HD le 12 ou le 13 — est périmé) : l'étape A de T0.7 s'est arrêtée au contrôle avant l'ouverture, sans aucun score (messages de commit de `main`, R-2588, R-2589, relevés le 13 novembre) ; ce texte est scellé strictement avant `VERDICT-P3BIS` (plan, point 4) ; HD après `VERDICT-P3BIS`, si l'issue est « vu » (plan, point 2), ≈ 7,5 h ; R après la poussée vérifiée de l'étape A de T0.7 et de HD ; L après `VERDICT-P3BIS`, la table A et l'étape B de T0.7 ; tout avant l'échéance de `GO-2026-11-10-07` (2026-11-27), sinon retour à Lazar.")
    a("A4-37", "étiquette `vadapt-r-v1`.",
      "étiquette `vadapt-r-v1`. **Disque** (CLVA2-14) : seules les activations du recalcul de T0.7 sont gardées sur disque (≈ 31,5 Go, T0.7 scellé, l. 2086) ; les séries à état imposé sont notées au fil de la passe, sans garder leurs activations ; scores à 800 directions ≈ 476 Mo (contre-lecture 2, § 2 bis).")
    a("A4-38", "(la recherche mécanique de `c_d` n'en est pas une).",
      "(la recherche mécanique de `c_d` n'en est pas une, ni la règle de lancement de la pièce HD sur `issue` de P3-bis, écrite au plan, point 2, avant `VERDICT-P3BIS`).")
    a("A4-39", "création qui ferait refuser une création de 7b, de P3-bis ou de l'étape A",
      "création qui ferait refuser une création de P3-bis ou de l'étape A (7b est finie)")
    a("A4-40", "Gardée pour mémoire, **non appliquée** : Lazar a retenu",
      "**Brouillon 4 (CLVA2-11)** : la moitié « pièce HD après la fin de 7b » de cette variante décrit désormais le fait (plan, point 2) ; seule la moitié « pièce R sur l'instance de l'étape A » reste non retenue ; le reste de cette annexe est gardé pour mémoire, sans effet.\n\nGardée pour mémoire, **non appliquée** : Lazar a retenu")
    entree = (
        "- **Contre-lecture 2** — sous-agent neuf de la session du compte 4, Claude Fable 5.2 (`claude-fable-5-2`), autre modèle que le rédacteur du brouillon 3 et que l'auteur du brouillon 4 (Claude Opus 5.5 ; N-052) ; **même modèle que la contre-lecture 1 (réserve déclarée par le lecteur)** ; lecteur de T0.7 scellé (exclu de tout rôle de lecteur ou d'hôte du verdict de P3-bis). Différentielle (brouillon 2 → brouillon 3) et sur T0.7 scellé et le module de `main`. Consigne : `brouillons/validite-adaptateur-v1/consigne-contre-lecture-2-brouillon3-compte4-v1.md`, `aad64678c18711fe7bcfc37bb72461c08a09dc59502035c447a81751992393f2`. Brouillon relu : `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md`, `defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd`. Rapport : `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2.md`, `11f7242b9dbada3fdc9f6e2c0a707eef3f0d2b51783e425545d78ec43d2bccee` (égal à son compagnon). Verdict : « non scellable en l'état » ; cinq bloquants, six majeurs, sept mineurs ; différentiel du brouillon 2 au brouillon 3 propre. Traitement au brouillon 4 :\n\n"
        "| constat | traitement | où |\n|---|---|---|\n"
        "| CLVA2-01 (règle « au-dessus » abandonnée par T0.7) | **option (a) du lecteur appliquée, en attente de la décision de la mère** : règle (a) de T0.7 pour VA-1, VA-3, VA-5b, VA-6 et la mention « au-dessus du plancher » des lignes de réserve ; `Dτ` pour VA-2 (analogue non simulé, déclaré) | « Métrique » ; « Seuil » ; phrases (en-tête de la table) |\n"
        "| CLVA2-02 (plancher des sondes figées) | couples CLVA2-02a, CLVA2-02b | « Métrique », directions ; plan, point 1 |\n"
        "| CLVA2-03 (800 directions) | couples CLVA2-03a à CLVA2-03h ; passage de T0.7 scellé qui contredit les 800 directions (l. 2789, 2793, 2802) cité, non corrigé | partout ; en-tête |\n"
        "| CLVA2-04 (littéraux de Q) | couple | plan, point 5 |\n"
        "| CLVA2-05 (`mention_etendue`) | couple | « Métrique », non interprétable |\n"
        "| CLVA2-06 (sonde en échec) | couple | « Liste d'arrêt » |\n"
        "| CLVA2-07 (3 200 directions, notation par lots) | couples CLVA2-07a, CLVA2-07b | « Calcul et dépense » ; « Code neuf » |\n"
        "| CLVA2-08 (réserves sans clé de sonde) | couple | « Critères », ordre de chaque couple |\n"
        "| CLVA2-09 (renvois au brouillon 21) | couple d'en-tête ; les vingt et une marques avec numéros de ligne remplacées une à une par la table de correspondance du rapport (couples A4-M01 à A4-M21) ; réserve générale réécrite | en-tête ; partout |\n"
        "| CLVA2-10 (puissance) | option (a) appliquée, en attente de la décision de la mère : table refaite par le script de l'auteur, mêmes valeurs que le lecteur ; seuil `σ > 0,060` gardé, aire minimale écrite (> 0,82) | « Puissance » ; « Prédiction » ; « Métrique », effectifs |\n"
        "| CLVA2-11 (pièce HD non jouée en parallèle de 7b) | **option recommandée à Lazar appliquée, en attente de son mot (nœud)** : HD après `VERDICT-P3BIS`, créée si et seulement si l'issue est « vu », règle écrite avant le verdict ; repli « sans étape A, aucune pièce R » ; calendrier refait ; annexe A annotée | en-tête ; plan, points 2 et 3 ; « Calcul et dépense » ; « Liste d'arrêt » ; annexe A |\n"
        "| CLVA2-12 (garde d'équivalence existante) | couples CLVA2-12a, CLVA2-12b | « Métrique » ; « Code neuf » |\n"
        "| CLVA2-13 (passes et pire cas) | devis refait : 2 816 passes, R 1,90 à 2,80 h, pire 8,85 USD, ensemble pire 33,4 USD ; nœud N-VA-1 toujours ouvert | « Calcul et dépense » |\n"
        "| CLVA2-14 (disque) | écrit | « Code neuf » |\n"
        "| CLVA2-15 (graine de `preparer_sonde`) | couple | plan, point 7 |\n"
        "| CLVA2-16 (`jeux` partiel ou nul) | couple | plan, point 6 |\n"
        "| CLVA2-17 (`R11-arret`, `R12-invalide`) | sans correction exigée | — |\n"
        "| CLVA2-18 (section « Contre-lecture ») | cette entrée ; paragraphe de la contre-lecture suivante réécrit | « Contre-lecture » |\n"
        "| champs fixés par le seul code de T0.7 (rapport, § 4) | vérifiés par le lecteur sur `main`, confirmés par l'auteur au commit C7 (pièce `confirmation-champs-t07-c7-v1.md`) ; **non confirmés par le développeur de T0.7, non joignable** : réserve écrite (en-tête) ; commit C7 laissé en marqueur (R-2593) | en-tête |\n\n"
        "**Vérification courte, prévue avant le scellement** : un sous-agent neuf, autre modèle que l'auteur du brouillon 4 (Claude Opus 5.5), non lecteur de P3-bis, en différentiel du brouillon 3 au brouillon 4 (couples versés et script d'application), contre le rapport de la contre-lecture 2 et T0.7 scellé ; puis la décision de la mère sur CLVA2-01 et CLVA2-10, et le mot de Lazar sur CLVA2-11.\n\n"
        "Brouillon 3 — contre-lecture suivante prévue alors (faite : contre-lecture 2) : un sous-agent neuf, autre modèle que le rédacteur,")
    a("A4-41", "Contre-lecture suivante, prévue avant le scellement : un sous-agent neuf, autre modèle que le rédacteur,", entree)
    a("A4-42", "`b4cd9953d199dd8f220f5162e5868c5b00fd392d`, vingt-six modules",
      "`<<COMMIT_C7_T07>>` (marqueur laissé sur le mot de la mère : le commit C7, `b4cd9953` au 13 novembre, change pour un correctif du contrôle de cache qui ne touche que `reextraction_p3_v1.py`, R-2593 ; à remplir par le commit de la ligne `CODE-T07` en vigueur au scellement), vingt-six modules")
    for i, ancien, nouveau in MARQUES:
        c.append({"id": i, "ancien": ancien, "nouveau": nouveau})
    return c

def principal():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    h, sortie = sys.argv[1], Path(sys.argv[2])
    if not re.fullmatch(r"\d{2}:\d{2}", h):
        sys.exit("ARRÊT : heure au format HH:MM attendue")
    if sortie.exists():
        sys.exit(f"ARRÊT : {sortie} existe déjà (R12)")
    tout = couples_lecteur() + couples_auteur(h)
    sortie.write_text(json.dumps(tout, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(tout)} couples écrits dans {sortie} ; sha256 {hashlib.sha256(sortie.read_bytes()).hexdigest()}")

principal()
