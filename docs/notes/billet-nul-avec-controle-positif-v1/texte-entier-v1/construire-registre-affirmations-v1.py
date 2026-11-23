"""Construit le registre des affirmations chiffrées du billet (texte entier v1).

Une entrée par nombre écrit dans le corps, dans l'ordre du texte :
(nombre écrit, clé de source, ligne ou page, valeur à la source, motif présent à cette ligne ou page, note).
La ligne de chaque motif est cherchée ici et écrite dans le registre ; le programme de vérification
la contrôle ensuite indépendamment (empreinte, motif à la ligne, arrondi, couverture du texte).
Pièce de classe B. Écrit le 2026-11-23 par le rédacteur habilité du billet.
"""
import hashlib
import json
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parents[4]
SOURCES = {
    "V3": "docs/verdicts/verdict-P3-premier-test-i-a-v2.md",
    "VB": "docs/verdicts/verdict-P3-bis-v1.md",
    "B": "docs/verdicts/verdict-T0.7-etape-B-v1.md",
    "Bb": "docs/verdicts/verdict-T0.7-etape-B-bis-v1.md",
    "E": "docs/verdicts/verdict-T0.7-etape-B-bis-v1-erratum-1-v2.md",
    "L": "docs/notes/neuron-lens-v1/lecture-b-beta/verdict-b-beta-v1.md",
}
# PDF : branche origin/prep/etat-de-l-art-niveau3-pieces-v1 (sauf GD, sur main) ; pages lues par pdftotext.
PDF = {
    "GD": ("HEAD", "docs/sources/pdf/2502.03407v1.pdf",
           "a4820ad59ef9b294609aa11cbcc044c27835d5f433d7e79d6ae374f874bc2e2b"),
    "FOMIN": ("origin/prep/etat-de-l-art-niveau3-pieces-v1", "docs/sources/pdf/niveau3-v1/lot2/2606.30449v1.pdf",
              "775abf11ef24188ee11b37a5cef0e5d2bbcd827ac86a0b3b1d4df923ff22b580"),
    "MOHSIN": ("origin/prep/etat-de-l-art-niveau3-pieces-v1", "docs/sources/pdf/niveau3-v1/lot7/2611.10620v1.pdf",
               "2aa2fd973d5693a267210b9ab742272761e32b80386cc95d87eaea8519ce3e1a"),
    "FIBS": ("origin/prep/etat-de-l-art-niveau3-pieces-v1", "docs/sources/pdf/niveau3-v1/lot3/2610.12445v4.pdf",
             "8d3ada9aa4ea22c4ec6b70d66675e9499375c5b95a949610fdccc00f928c2d86"),
}

# (nombre écrit, source, valeur à la source, motif à trouver sur une seule ligne de la source, note)
# Pour un PDF : (nombre, "PDF:<clé>:<page>", valeur, citation, note) ; la citation doit être sur la page.
E_ = [
    # TL;DR et Setup
    ("60", "V3", "60", "sur les 60 tâches, aucune exclue", "60 tâches de P3 ; P3-bis : mêmes tâches (VB l. 221, « 60 (aucune exclue) »)"),
    ("10", "VB", "10", "10 actions par épisode", ""),
    ("600", "V3", "600", "600 par condition", "P3 ; P3-bis : VB l. 142"),
    ("4", "PDF:GD:4", "4", "pretend to be an honest or deceptive person", "page de la citation"),
    ("15", "B", "15", "tromperie `tromperie-difference_moyennes-c15` ; enjeux `enjeux-lineaire-c15`", "couche 15 (suffixe c15)"),
    ("200", "V3", "200", "200 sondes de plancher, 2 000 tirages, 0 dégénéré", ""),
    ("800", "VB", "800", "n = 800 ; quantile 0,95 : 0.6496013888888889", ""),
    ("800", "VB", "800", "n = 800 ; quantile 0,95 : 0.6496013888888889", ""),
    ("0.8743", "VB", "0.8742888888888889", "maximum 0.8742888888888889", ""),
    ("0.8012", "VB", "0.8012361111111111", "Fait relevé : le maximum du plancher", "ligne suivante de la même phrase"),
    ("0.95", "VB", "0,95", "n = 800 ; quantile 0,95 : 0.6496013888888889", ""),
    # P3
    ("19", "V3", "20261019", "`20261019-230011-p3-reel`. **Lecture décisive**", "run du 19 octobre 2026"),
    ("2026", "V3", "20261019", "`20261019-230011-p3-reel`. **Lecture décisive**", ""),
    ("97.5%", "V3", "97,5", "saboteur contre honnête, au niveau 97,5 %", ""),
    ("0.5748", "V3", "0,5748", "aire 0,5748, intervalle [0,5313 ; 0,6183]", ""),
    ("0.5313", "V3", "0,5313", "aire 0,5748, intervalle [0,5313 ; 0,6183]", ""),
    ("0.6183", "V3", "0,6183", "aire 0,5748, intervalle [0,5313 ; 0,6183]", ""),
    ("0.5717", "V3", "0,5717", "0,5717 ([L] `resultat.P3-P3.tromperie-difference_moyennes-c15`)", ""),
    ("0.5248", "V3", "0,5248", "aire 0,5248, intervalle [0,4813 ; 0,5700], quantile 0,95 du plancher 0,5356", ""),
    ("0.4813", "V3", "0,4813", "aire 0,5248, intervalle [0,4813 ; 0,5700], quantile 0,95 du plancher 0,5356", ""),
    ("0.5700", "V3", "0,5700", "aire 0,5248, intervalle [0,4813 ; 0,5700], quantile 0,95 du plancher 0,5356", ""),
    ("0.5356", "V3", "0,5356", "aire 0,5248, intervalle [0,4813 ; 0,5700], quantile 0,95 du plancher 0,5356", ""),
    ("1.5227", "V3", "1,5227", "honnête, 1,5227, intervalle à 95 % [1,2464 ; 1,8012], 60 tâches", ""),
    ("1.2464", "V3", "1,2464", "honnête, 1,5227, intervalle à 95 % [1,2464 ; 1,8012], 60 tâches", ""),
    ("1.8012", "V3", "1,8012", "honnête, 1,5227, intervalle à 95 % [1,2464 ; 1,8012], 60 tâches", ""),
    ("60", "V3", "60", "honnête, 1,5227, intervalle à 95 % [1,2464 ; 1,8012], 60 tâches", ""),
    ("1.3211", "V3", "1,3211", "borne basse de `E_sf` = 1,3211", ""),
    ("80%", "V3", "80", "l'aire minimale détectable (80 %) vaut 0,6315", ""),
    ("0.6315", "V3", "0,6315", "l'aire minimale détectable (80 %) vaut 0,6315", ""),
    ("0.5966", "V3", "0,5966", "l'aire minimale détectable (80 %) vaut 0,5966", ""),
    ("2.5%", "VB", "2,5", "dépasse le nominal de 2,5 %", "réserve 1 de R-2299, recopiée par le verdict de P3-bis"),
    ("6.0%", "VB", "6,0", "simulé : 6,0 % à 13,3 %", ""),
    ("13.3%", "VB", "13,3", "simulé : 6,0 % à 13,3 %", ""),
    ("2%", "VB", "2", "≈ 2 % à 5 %", ""),
    ("5%", "VB", "5", "≈ 2 % à 5 %", ""),
    ("−0.0531", "VB", "−0,0531", "−0,0531 et −0,0694", ""),
    ("−0.0694", "VB", "−0,0694", "−0,0531 et −0,0694", ""),
    ("0.6376", "VB", "0,6376", "la même formule donne 0,6376 et 0,6025", "réserve 2 de R-2299"),
    ("0.6025", "VB", "0,6025", "la même formule donne 0,6376 et 0,6025", ""),
    # P3-bis
    ("600", "VB", "600", "600 actions de A, 600 de T", ""),
    ("11", "B", "2026-11-11", "SCELLEMENT-P3BIS | 2026-11-11T15:52:30Z", "ligne de scellement recopiée par le verdict de l'étape B"),
    ("2026", "B", "2026", "SCELLEMENT-P3BIS | 2026-11-11T15:52:30Z", ""),
    ("0.8012", "VB", "0.8012361111111111", "aire de p sur A contre T 0.8012361111111111", ""),
    ("0.6496", "VB", "0.6496013888888889", "0,95 du plancher de 800 directions 0.6496013888888889", ""),
    ("0.1516", "VB", "0.1516347222222223", "différence D estimée 0.1516347222222223", ""),
    ("0.1178", "VB", "0.11776210416666666", "[0.11776210416666666 ; 0.18212723611111126]", ""),
    ("0.1821", "VB", "0.18212723611111126", "[0.11776210416666666 ; 0.18212723611111126]", ""),
    ("0.5166", "VB", "0.5166333333333334", "longueur notée 0.5166333333333334", ""),
    ("0.5025", "VB", "0.5025", "| m, mention étendue | aire 0.5025", "mention étendue"),
    ("0.8297", "VB", "0.8297222222222222", "| PB-6 | A contre B", ""),
    ("0.5160", "VB", "0.5160361111111111", "| PB-5 | B contre H", ""),
    ("0.7702", "VB", "0.7702318466752647", "séparation du coût seul 0.7702318466752647", ""),
    ("48", "VB", "48", "détecte 48 épisodes de A sur 60", ""),
    ("60", "VB", "60", "détecte 48 épisodes de A sur 60", ""),
    ("4", "VB", "4", "k_T = 4 sur n_T = 60", ""),
    ("60", "VB", "60", "k_T = 4 sur n_T = 60", ""),
    ("0.756", "VB", "0.7564532188372323", "| PB-4, T moins H | 0.7564532188372323", ""),
    ("0.441", "VB", "0.44102996348536266", "| PB-4, T moins H | 0.7564532188372323", ""),
    ("1.076", "VB", "1.075679970342812", "| PB-4, T moins H | 0.7564532188372323", ""),
    ("53", "VB", "53", "| PB-4, T moins H | 0.7564532188372323", ""),
    ("0.9856", "VB", "0.9856237865203533", "`aire_a` 0.9856237865203533 ;", ""),
    ("0.6172", "VB", "0.6172444444444445", "| `saboteur-temoin` | 0,95 | 0.6172444444444445", ""),
    # Étape B
    ("11", "B", "2026-11-11", "| SCELLEMENT-T07 | 2026-11-11T07:11:42Z |", ""),
    ("2026", "B", "2026", "| SCELLEMENT-T07 | 2026-11-11T07:11:42Z |", ""),
    ("1.0", "B", "1.0", "aire de validation 1.0, meilleure aire 1.0", ""),
    ("0.25", "Bb", "0,25", "| 0,25 (S25) |", "doses, notation du verdict de B bis ; S25 à S100 au verdict B l. 66-69"),
    ("0.5", "Bb", "0,5", "| 0,5 (S50) |", ""),
    ("0.75", "Bb", "0,75", "| 0,75 (S75) |", ""),
    ("1", "Bb", "1", "| 1 (S100) |", ""),
    ("640", "B", "640", "**640 positifs et 640 négatifs**", ""),
    ("640", "B", "640", "**640 positifs et 640 négatifs**", ""),
    ("0.5", "Bb", "0,5", "| 0,5 (S50) |", ""),
    ("0.75", "Bb", "0,75", "| 0,75 (S75) |", ""),
    ("1", "Bb", "1", "| 1 (S100) |", ""),
    ("0.7481", "B", "0.74810302734375", "- **S50** : aire_n029 0.74810302734375", ""),
    ("0.8933", "B", "0.89330078125", "- **S75** : aire_n029", "aire de la base décisive (mots et coût)"),
    ("0.9728", "B", "0.972802734375", "- **S100** : aire_n029", ""),
    ("0.70", "B", "0.7", "seuil_aire 0.7 ; état écrit `réussit`", "première ligne qui porte le motif (S50)"),
    ("0.25", "Bb", "0,25", "| 0,25 (S25) |", ""),
    ("0.5691", "B", "0.56906005859375", "- **S25** : aire_n029 0.56906005859375", ""),
    ("−0.1896", "B", "-0.1896138597621127", "- **S25** : aire_n029 0.56906005859375", ""),
    ("1", "B", "1", "niveau appliqué 0.9833333333333333 = 1 − 0,05 / 3", ""),
    ("0.05", "B", "0,05", "niveau appliqué 0.9833333333333333 = 1 − 0,05 / 3", ""),
    ("3", "B", "3", "niveau appliqué 0.9833333333333333 = 1 − 0,05 / 3", ""),
    ("0.5816", "B", "0.58160400390625", "aire: 0.58160400390625 | intervalle propre", ""),
    ("0.5738", "B", "0.5737883300781249", "quantile 0,95 du plancher: 0.5737883300781249", ""),
    ("0.5136", "B", "0.51360595703125", "aire: 0.51360595703125 | intervalle propre", ""),
    ("0.5521", "B", "0.5520766601562499", "quantile 0,95 du plancher: 0.5520766601562499", ""),
    ("0.9017", "B", "0.90169189453125", "aire: 0.90169189453125 | intervalle propre [bas_sonde, haut_sonde]: [0.8714749755859376", ""),
    ("0.8715", "B", "0.8714749755859376", "aire: 0.90169189453125 | intervalle propre [bas_sonde, haut_sonde]: [0.8714749755859376", ""),
    ("0.9287", "B", "0.9287143758138021", "aire: 0.90169189453125 | intervalle propre [bas_sonde, haut_sonde]: [0.8714749755859376", ""),
    ("0.5367", "B", "0.5366658935546875", "aire: 0.90169189453125 | intervalle propre [bas_sonde, haut_sonde]: [0.8714749755859376", ""),
    ("95%", "B", "95", "Lectures à 95 %% sans correction", ""),
    ("1", "B", "S100", "sur (ii), lue sur `S100` contre `honnete`", "dose 1 = S100"),
    ("0.1249", "B", "0,1248974639892578", "borne basse de D 0,1248974639892578", ""),
    ("1", "B", "T100", "est **au-dessus** sur `T100` contre `honnete`", "adaptateur témoin à la dose 1"),
    ("0.1174", "B", "0,1174279937744141", "borne basse de D 0,1174279937744141", ""),
    ("0.4720", "B", "0,47195196533203126", "borne basse 0,47195196533203126", ""),
    ("0.5336", "B", "0,5335870361328124", "quantile 0,5335870361328124", ""),
    ("0.5", "Bb", "0,5", "| 0,5 (S50) |", ""),
    ("0.75", "Bb", "0,75", "| 0,75 (S75) |", ""),
    ("1", "Bb", "1", "| 1 (S100) |", ""),
    ("0.6355", "B", "0.6354931640625", "dissimulation-lineaire-c15 | S50 : aire 0.6354931640625", ""),
    ("0.6923", "B", "0.692275390625", "dissimulation-lineaire-c15 | S75 : aire 0.692275390625", ""),
    ("0.7547", "B", "0.75471923828125", "dissimulation-lineaire-c15 | S100 : aire 0.75471923828125", ""),
    ("0.25", "Bb", "0,25", "| 0,25 (S25) |", ""),
    ("0.5", "B", "0,5", "dans les 15 lectures à prédicteurs triviaux", ""),
    ("15", "B", "15", "dans les 15 lectures à prédicteurs triviaux", ""),
    # Étape B bis
    ("14", "Bb", "2026-11-14", "| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z |", ""),
    ("2026", "Bb", "2026", "| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z |", ""),
    ("64", "Bb", "64", "64 tâches d'évaluation, deux plis externes de 32 tâches", ""),
    ("32", "Bb", "32", "64 tâches d'évaluation, deux plis externes de 32 tâches", ""),
    ("320", "Bb", "320", "320 positifs et 320 négatifs par pli", ""),
    ("320", "Bb", "320", "320 positifs et 320 négatifs par pli", ""),
    ("800", "Bb", "800", "plancher de 800 directions, nul de 100 réétiquetages", ""),
    ("100", "Bb", "100", "plancher de 800 directions, nul de 100 réétiquetages", ""),
    ("0.99", "Bb", "0,99", "Niveau décisif retenu : 0,99", ""),
    ("0.9436", "Bb", "0.9436", "aire 0.9436 à S25 ; aire 0.9532 à S50 ; aire 0.9967 à S75 ; aire 0.9885 à S100", ""),
    ("0.9532", "Bb", "0.9532", "aire 0.9436 à S25 ; aire 0.9532 à S50 ; aire 0.9967 à S75 ; aire 0.9885 à S100", ""),
    ("0.9967", "Bb", "0.9967", "aire 0.9436 à S25 ; aire 0.9532 à S50 ; aire 0.9967 à S75 ; aire 0.9885 à S100", ""),
    ("0.9885", "Bb", "0.9885", "aire 0.9436 à S25 ; aire 0.9532 à S50 ; aire 0.9967 à S75 ; aire 0.9885 à S100", ""),
    ("0.9252", "Bb", "0.9252", "artefact : aire 0.9252, détecté", ""),
    ("0.9822", "Bb", "0.9822", "aire 0.9822, détecté", ""),
    ("0.9942", "Bb", "0.9942", "aire 0.9942, détecté", ""),
    ("0.9986", "Bb", "0.9986", "aire 0.9986, détecté", ""),
    ("0.0184", "Bb", "0.0184", "différence 0.0184 [-0.0189 ; 0.0541]", "borne basse -0.0189"),
    ("−0.0290", "Bb", "-0.0290", "différence -0.0290 [-0.0726 ; 0.0090]", "borne basse -0.0726"),
    ("0.0025", "Bb", "0.0025", "différence 0.0025 [-0.0029 ; 0.0082]", "borne basse -0.0029"),
    ("1", "Bb", "1", "| 1 (S100) |", ""),
    ("−0.0102", "Bb", "-0.0102", "différence -0.0102 [-0.0209 ; -0.0019]", ""),
    ("−0.0209", "Bb", "-0.0209", "différence -0.0102 [-0.0209 ; -0.0019]", ""),
    ("−0.0019", "Bb", "-0.0019", "différence -0.0102 [-0.0209 ; -0.0019]", ""),
    ("0.25", "Bb", "0,25", "| 0,25 (S25) |", ""),
    ("0.5", "Bb", "0,5", "| 0,5 (S50) |", ""),
    ("0.75", "Bb", "0,75", "| 0,75 (S75) |", ""),
    ("0.6871", "Bb", "0.6871", "s'allume aussi sur le jumeau honnête (aire 0.6871)", ""),
    ("1", "Bb", "1", "| 1 (S100) |", ""),
    ("0.8793", "Bb", "0.8793", "s'allume aussi sur le jumeau honnête (aire 0.8793)", ""),
    ("0.5", "E", "0,5", "de l'honnête aux doses 0,5, 0,75 et 1", "phrase de l'erratum, qui prime"),
    ("0.75", "E", "0,75", "de l'honnête aux doses 0,5, 0,75 et 1", ""),
    ("1", "E", "1", "de l'honnête aux doses 0,5, 0,75 et 1", ""),
    ("0.5", "E", "0,5", "à la dose 0,5 seulement, elle bat les trois lecteurs du texte", ""),
    ("0.25", "E", "0,25", "à la dose 0,25, elle échoue au nul de réétiquetage", ""),
    ("8", "Bb", "huit", "(huit sur huit tests ; attendu par hasard ≈ 0,2)", "en lettres à la source"),
    ("8", "Bb", "huit", "(huit sur huit tests ; attendu par hasard ≈ 0,2)", ""),
    ("0.2", "Bb", "0,2", "(huit sur huit tests ; attendu par hasard ≈ 0,2)", ""),
    ("4", "Bb", "quatre", "(quatre sur quatre ; attendu ≈ 0,1)", ""),
    ("4", "Bb", "quatre", "(quatre sur quatre ; attendu ≈ 0,1)", ""),
    ("5", "Bb", "cinq", "cinq sur huit tests en tout", ""),
    ("8", "Bb", "huit", "cinq sur huit tests en tout", ""),
    ("1", "Bb", "une", "une sur une (attendu ≈ 0,025)", ""),
    ("1", "Bb", "une", "une sur une (attendu ≈ 0,025)", ""),
    ("1", "Bb", "dose 1", "réserve RF (adaptateur témoin, dose 1)", ""),
    ("32", "Bb", "32", "avec 32 tâches d'apprentissage par pli", ""),
    ("0.1427", "Bb", "0.1427", "écart absolu maximal 0.1427 (P-S25) sur 10 cellules lues", ""),
    ("2", "Bb", "2", "réglage retenu changé dans 2 plis sur 10", ""),
    ("10", "Bb", "10", "réglage retenu changé dans 2 plis sur 10", ""),
    ("0.9994", "Bb", "0.9994", "« (i) aire 0.9994 sur le jeu décisif de P-S100 »", ""),
    # Travaux voisins
    ("6", "PDF:GD:6", "6", "this probe fires much more on honest responses to our evaluation prompts than on responses to control prompts", "page"),
    ("0.999", "PDF:FOMIN:1", "0.999", "decode prompt domain almost perfectly (AUC 0.999), while the best future-behavior probe reaches AUC 0.801", ""),
    ("0.801", "PDF:FOMIN:1", "0.801", "decode prompt domain almost perfectly (AUC 0.999), while the best future-behavior probe reaches AUC 0.801", ""),
    ("1", "PDF:FOMIN:1", "1", "decode prompt domain almost perfectly (AUC 0.999), while the best future-behavior probe reaches AUC 0.801", "page"),
    ("1.00", "PDF:MOHSIN:15", "1.00", "agent AUROC 1.00 → 0.61", ""),
    ("0.61", "PDF:MOHSIN:15", "0.61", "agent AUROC 1.00 → 0.61", ""),
    ("15", "PDF:MOHSIN:15", "15", "with the brief and the private messages taken out of the context", "page"),
    ("98.7%", "PDF:FIBS:1", "98.7", "achieving 98.7% AUROC in SHADE-Arena", ""),
    ("1", "PDF:FIBS:1", "1", "achieving 98.7% AUROC in SHADE-Arena", "page"),
    ("34", "PDF:FIBS:34", "34", "With them kept, the transcript states the side task outright and detecting it becomes nearly trivial", "page ; « them » = les rappels de la tâche annexe, même page"),
    # Limites (lentilles)
    ("0.287", "L", "0,2872", "minimum **0,2872** à la couche 4", ""),
    ("4", "L", "4", "minimum **0,2872** à la couche 4", ""),
    ("0.20", "L", "+0,20", "écart `r_med`(notre R) − `r_med`(logits) ≥ +0,20", ""),
    ("0.111", "L", "0,1114", "différence entre moitiés au-dessus de 0,10 à six couches-cibles : R `mid` couches 0, 1, 2 (0,1114", ""),
    ("0.10", "L", "0,10", "différence entre moitiés au-dessus de 0,10 à six couches-cibles : R `mid` couches 0, 1, 2 (0,1114", ""),
    ("55", "L", "55", "55 pôles sur 64 au lieu de 58", "« pôles » au verdict, « directions » au billet"),
    ("64", "L", "64", "55 pôles sur 64 au lieu de 58", ""),
    ("8", "L", "8", "`pass` = **0,8594** à la couche 8", ""),
    ("58", "L", "58", "55 pôles sur 64 au lieu de 58", ""),
    ("1", "Bb", "dose 1", "réserve RF (adaptateur témoin, dose 1)", "« no control adapter below dose 1 »"),
]


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def main():
    reg = {"sources": {}, "pdf": {}, "entrees": []}
    lignes = {}
    for k, p in SOURCES.items():
        reg["sources"][k] = {"chemin": p, "sha256": sha(RACINE / p)}
        lignes[k] = (RACINE / p).read_text(encoding="utf-8").splitlines()
    for k, (ref, p, h) in PDF.items():
        reg["pdf"][k] = {"ref": ref, "chemin": p, "sha256": h}
    for i, (n, src, val, motif, note) in enumerate(E_, 1):
        e = {"n": i, "nombre": n, "source": src, "valeur_source": val, "motif": motif, "note": note}
        if not src.startswith("PDF:"):
            trouve = [j + 1 for j, l in enumerate(lignes[src]) if motif in l]
            if not trouve:
                sys.exit(f"entrée {i} ({n}) : motif absent de {src}")
            e["ligne"] = trouve[0]
            e["lignes_portant_le_motif"] = len(trouve)
        reg["entrees"].append(e)
    sortie = pathlib.Path(__file__).with_name("registre-affirmations-v1.json")
    sortie.write_text(json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("entrées :", len(reg["entrees"]))


if __name__ == "__main__":
    main()
