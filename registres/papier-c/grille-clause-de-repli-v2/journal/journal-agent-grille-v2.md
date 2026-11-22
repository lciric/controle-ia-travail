# Journal de l'agent de la grille de la clause de repli — rapport v2

Heures en temps universel, 2026-11-22. Machine : 4 cœurs ; calcul par `/usr/local/bin/python3` (python 3.13.18,
numpy 2.5.3, les versions des sorties de v1) ; scellement par `.venv` (`PYTHONPATH=src`).

| heure | action | durée |
|---|---|---|
| 20:22 | empreinte de la consigne vérifiée (`37ee2527…`) ; lecture de la consigne | — |
| 20:22 | empreintes vérifiées : texte c5 (`0747f357…`), erratum 1 (`78cc1127…`), liste finie (`0c62072c…`), rapport v1 (`8d1616fc…`) ; programmes, archive et 198 sorties de v1 conformes à leurs manifestes (`sha256sum -c`) | — |
| 20:22–20:24 | lecture : texte c5 (verrou 10, bloc de la stabilité de rang, précisions 3, 5, 8, 37), erratum 1, liste finie, rapport v1, programmes v1, archive (fonctions de rang et loi jointe), contre-lecture v1, `src/controle_ia/manifeste.py` | — |
| 20:24 | dossier créé ; programmes v1, archive et liste finie copiés (empreintes égales) | — |
| 20:24–20:27 | `grille_commun_v2.py`, `grille_ab_v2.py`, `grille_c_v2.py` (différences écrites en tête) ; `liste_et_garde_v2.py`, `essais_garde_v2.py`, `lancer_v2.sh`, `mesure_temps_v2.sh`, `manifeste_v2.py` | — |
| 20:26 | `python3 -B essais_garde_v2.py ../entrees/liste-finie-cases-grille-v1.md` : cas sain « saine », quatre artefacts « échec » (attendus) | < 1 s |
| 20:26 | `python3 -B liste_et_garde_v2.py inventaire-v1 …` : 86 reprises et 58 cases à jouer (C-P3a, C-P3b) ; 96 reprises et 48 à jouer (C-P3c) ; aucun écart à la colonne « jouée » de la liste | < 1 s |
| 20:27 | 182 sorties reprises copiées sous `sorties/reprises-v1/` ; empreintes égales au manifeste des sorties de v1 ; leurs `.err` vides | — |
| 20:27 | essai de fumée (2 essais, passe 8, sorties hors du dossier, aucun taux lu) ; `/usr/bin/time` absent, mesure réécrite avec l'horloge du shell | < 5 s |
| 20:28:11 | **empreintes figées et scellées** : `sha256sums-programmes-avant-lancement-v2.txt` (`a91545e5…`), archive (`1d203e8b…`), entrées (`c239c4ce…`) | — |
| 20:28:17 | manifeste de la mesure (`manifestes/manifeste-mesure-temps-v2.json`) ; `bash programmes/mesure_temps_v2.sh` (passe 9, graines distinctes de toute case ; seules les durées lues) | 9 s |
| 20:28:35 | contrôle des programmes contre le fichier figé (conformes) ; manifeste du lot (`manifestes/manifeste-lot-v2.json`, 106 cases) | — |
| 20:28:40 | `bash programmes/lancer_v2.sh lot` en arrière-plan (C-P3c puis C-P3a et C-P3b, 4 processus) | voir plus bas |
| 20:29:46 | `resume_v2.py` (mise en tables) écrit pendant le lot, essayé sur sorties synthétiques (cas sain ; refus sur une sortie retirée), **figé et scellé** (`sha256sums-programme-resume-v2.txt`) avant toute lecture d'un taux neuf | — |
| 20:28:42–20:35:23 | partie C-P3c du lot (48 cases, R = 8 000) | 6 min 41 s ; 1 528 s de processeur |
| 20:35:23–20:53:37 | partie C-P3a et C-P3b du lot (58 cases, R = 1 000, 1 000 tirages) | 18 min 14 s ; 4 234 s de processeur |
| 20:53:37 | fin du lot, code 0 ; 106 sorties, 106 `.err` vides ; aucune relance (`lancer_v2.sh relance` non employé) | — |
| 20:54 | programmes et programme de tables contrôlés contre leurs fichiers figés : conformes | — |
| 20:54 | `python3 -B programmes/liste_et_garde_v2.py verifier …` sur les sorties réelles : SAINE (144 / 144 / 108) | < 1 s |
| 20:54 | `python3 -B programmes/resume_v2.py …` : `tables-grille-v2.md`, `resume-grille-v2.json` ; première lecture des taux neufs | < 1 s |
| 20:55–20:56 | rapport v2 écrit ; deux affirmations vérifiées par programme et corrigées avant scellement (liste des cases E40 neuves ; marges de C-P3c) ; liste des empreintes des sorties ; scellement de tous les fichiers | — |

Durée d'horloge du lot : 25 minutes (20:28:42 à 20:53:37). Durée du travail : 20:22 à 20:56 UTC.
