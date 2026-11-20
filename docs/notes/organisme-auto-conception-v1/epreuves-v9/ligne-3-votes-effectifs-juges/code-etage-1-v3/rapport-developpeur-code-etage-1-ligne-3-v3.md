# Rapport du développeur — code de l'étage 1 de la ligne 3, deux ajouts de l'additif 1 (code v3)

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel), sous le mandat `mandat-developpeur-code-etage-1-ligne-3-v4.md` (`1d29671b3ff68bfb7094f9e6368695802511349357b2eda3ba9627103b4b7847`, égal à son compagnon). Les fichiers n'existent que dans le bloc-notes (`…/developpeur-etage-1-ligne-3-v4/code-etage-1-v3/`). Rien n'est écrit dans le dépôt. Rien n'est committé. Le v2 n'est pas touché : ses quatre compagnons ont été revérifiés « OK » en fin de travail.

## Verdict

Les deux ajouts sont faits, tous deux **après les tirages, sur les tableaux déjà tirés**. Aucun tirage, aucune graine, aucune constante existante, aucune mesure existante ne change.

- **115 essais passés, 0 échoué.** Ce sont les 109 essais du v2, gardés, et 6 essais neufs. Deux lancements donnent le même résultat.
- **Sorties existantes égales à l'octet**, sur la racine des essais seule, pour deux configurations :
  - toutes les clés du v2 sont présentes en v3 ;
  - les seules clés neuves sont les ajouts déclarés ;
  - la seule feuille qui diffère est `/version`, par la règle R12 ;
  - une fois les ajouts retirés et `version` remise, le résultat v3 a l'empreinte exacte du résultat v2 ;
  - les dérivations de graines sont identiques.
- **Contrôle « trop beau » (R4), rejoué en entier, dans les deux modes : 93 défauts sur 93 vus.** Ce sont les 70 défauts du v2 et 23 défauts neufs.

## Pièces lues, empreintes recalculées

| pièce | sha256 | contrôle |
|---|---|---|
| mandat v4 | `1d29671b…7847` | égale à son compagnon |
| additif 1 v2 | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` | égale au mandat |
| texte v7, `git show origin/main:…` (après `git fetch origin main`, redirigé vers le bloc-notes) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | égale |
| banc v2 | `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3` | égale |
| essais v2 | `d90eb6f3d8ad4772b274ba53e70e2c2e21b12ba5b094c2ac6646fde326200fe2` | égale |
| chronométrage v2 | `9bcea5306fd444afffbcc8a8a13565d7cba103d27be858e8f9c9161f66176e74` | égale |
| contrôle v2 | `1ead27755f433e4e88bbd6ff4b72605ce22ab24b4b7c96741f89245a1a6afd7f` | égale |
| rapport v2 | `995bd5f48494e9a241fcb5c7824c59105d0ddf0c0f8cc95702e942bdcf58903c` | égale |
| vérification du v2 | `09e462b9f42ccd7d11828c2f630a2cd6a6d205f2e1e15948c1a62b0664506186` | égale (« Conforme ») |

Environnement : Python 3.13.18.

Méthode de travail :
- Les quatre fichiers v3 qui dérivent du v2 sont produits par `scripts/remplacer_texte_exact_v1.py`. Il y a eu 10, 6, 11 et 6 remplacements, toutes ancres acceptées. Les fichiers JSON sont construits par un programme écrit en fichier (`brouillons/construire_remplacements_v3_v2.py`).
- Le programme de comparaison est un fichier neuf.

## Fichiers rendus (dossier `code-etage-1-v3/`, chacun avec son compagnon `.sha256`, vérifiés « OK »)

| fichier | sha256 |
|---|---|
| `banc_juges_scriptes_ligne_3_v3.py` | `09bfe0dbf237f00fa361515f6c870c9120a9a5a0ec9458ac131ddc5c81370ba0` |
| `essais_banc_juges_scriptes_ligne_3_v3.py` | `28ad0e8987790ec5a7bef61076606598604903e006f36c27a8a6e778dd0a3f77` |
| `chronometrer_banc_ligne_3_v3.py` | `8cb61afbdc6948197b756028d08df665725a2d3f99681c1e21c89b96eba5fa7e` |
| `controle_defauts_reintroduits_ligne_3_v3.py` | `b4078e715fdacc0ff6831d67921d315e28d8189c911ab000daa2fc33421bf654` |
| `comparer_sorties_v2_v3_ligne_3_v1.py` | `4209748a9c8ac261cd53a4dab54c3415af9ff8c73372684548b2c6341309ea7a` |
| `comparaison-sorties-v2-v3-ligne-3-v1.json` | `17ebe5557e8a1b81cb17cbc2b9922511a2363948ad7995c2a3ec8a2f5f5d44cd` |
| `rapport-defauts-reintroduits-ligne-3-v3.json` (mode « visé ») | `343f0f779a13753666cd8f118e20b755ee49f055a2eeb2b21d945ec6e00c9ce7` |
| `rapport-defauts-reintroduits-fichier-entier-ligne-3-v3.json` (mode « complet ») | `586e6f4561a918e0c4ea31917f6e07f8c086eb95f4943a6c3fe8c9be6f2d40fe` |
| journaux de l'outil, `<fichier v3>.journal-remplacements-v1.json` (banc ; chronométrage ; essais ; contrôle) | `5ef628f1…d172` ; `4d3355ac…347b` ; `2785e893…d4d717` ; `28240b8f…36dd7` |
| `rapport-developpeur-code-etage-1-ligne-3-v3.md` (ce rapport) | dans son compagnon |

## Différentiels v2 → v3 (`differentiels-v2-v3/`, `diff -u`, compagnon `differentiels-v2-v3.sha256`)

| différentiel | sha256 | lignes retirées du v2 |
|---|---|---|
| `banc-v2-v3.diff` | `d430702e374120c5eb1d55e32e9e0e7ff9df9db2b245bb04012348cc1d0e85ab` | 5, toutes des renommages en v3 : titre, ligne d'usage, `VERSION`, noms des deux fichiers de sortie |
| `essais-v2-v3.diff` | `a73d621b8678554672776944f2deb3bcc852e481d79b3cead430fbc31675583d` | 11, toutes des renommages en v3 : en-tête, chemins, nom du module, noms de sortie, chronométrage |
| `chronometrage-v2-v3.diff` | `94dbf457501734d6de1ca2a1fcfb31b04c628ecfcfc76610b1bbacc8eefe012c` | 5, toutes des renommages en v3 |
| `controle-v2-v3.diff` | `98c781fb95e7734795b10429ef8264e897abb8d09345ed8decc1c5d08a86d662` | 5 : quatre renommages, et la ligne de `DEFAUTS` qui reçoit `+ DEFAUTS_V3` |

Aucune ligne de calcul du v2 n'est retirée ni modifiée. Le banc v3 ne fait qu'ajouter du code.

## Ce que fait la version 3

### Ajout 1 — silence 1 (part (b) et cinq comptes)

- **Fonction neuve `silence_1_part_et_comptes(alarmes, change, effet, detecte)`.** Elle est appelée dans `cellule_alarme`, par bras, après le calcul du bloc existant. Ses entrées sont les tableaux déjà tirés : alarmes, mélange, détections. Elle ne fait aucun tirage.
- **La part (b)** est rendue sous la clé `part_des_suites_en_alarme_sur_changement_a_effet`. Elle vaut : suites « à effet » détectées / suites qui portent au moins une alarme à l'un des 11 tests. Le dénominateur compte toutes ces suites, qu'elles changent ou non, que l'alarme tombe avant ou après le changement.
  - Si le dénominateur est nul, la part vaut `null` (« indéfini »), comme la part (a) dans le v2. Elle ne vaut jamais 0.
  - La part (a), `part_des_detections_sur_changement_a_effet`, est inchangée.
- **Les cinq comptes** sont rendus dans `comptes_silence_1`, en entiers : `suites_a_effet_detectees`, `suites_qui_changent_detectees`, `suites_en_alarme`, `suites_sans_changement_en_alarme`, `suites`.
- **La mention obligatoire** accompagne la part (b), clé `mention_part_des_suites_en_alarme` : « dépend du mélange planté : une suite sur deux change, une sur quatre « à effet » ».
- **Choix déclaré (le plus étroit, sans effet sur les mesures).** J'ajoute par cellule d'alarme `comptes_du_melange_plante` : suites qui changent, « à effet », « sans effet », sans changement. Deux raisons :
  - l'aide P6 a besoin des dénominateurs, 1 000 et 500, pour comparer sur les comptes entiers ;
  - la mention de (b) renvoie à ce mélange.

  Ce n'est pas l'un des cinq comptes demandés. C'est une clé de plus, déclarée et vérifiée par la preuve d'égalité.

### Ajout 2 — silence 2 (aide « prédiction P6 », carte sans mot)

- **Fonction neuve `criteres_alarme_p6(cellules)`.** Sa sortie va dans `criteres_mecaniques["alarme_fcbf4a2dd1a57"]`. Elle est lue sur les cellules déjà calculées.
- **Champ `nature` : aide, jamais le verdict.** Le champ dit que l'agent neuf prononce (règle R13). Il dit aussi que les mots de P6 portent sur la prédiction, ne s'écrivent jamais pour la carte et ne disent rien de juges réels (réserve 11).
- **Champ `carte_fcbf4a2dd1a57`** : toujours « mesurée, sans mot : aucune règle de mot gelée ».
- **`prediction_P6.par_m`**, pour m = 10, 20 et 40, contient deux clauses.
  - *Clause « fausse alarme »* (bras B). Elle donne les suites sans changement en alarme et les suites sans changement. Elle est « atteinte » si 100 x > 8 N, en entiers : plus de 80 sur 1 000.
  - *Clause « détection »*. Elle donne les « à effet » détectées de B et de D et les suites « à effet ».
    - À m = 20 et 40, elle est lue : « atteinte » si B ≤ D.
    - À m = 10, elle est rapportée hors clause : `lue: false`, `atteinte: null`.
- **`prediction_P6.clauses_atteintes`** donne la liste des clauses atteintes, par exemple `fausse_alarme|m=10`.
- **`prediction_P6.mot`** prend l'une de trois valeurs :
  - « P6 réfutée » si une clause est atteinte dans l'une de ses cellules ;
  - « P6 non réfutée » sinon ;
  - « incomplet : cellules de P6 manquantes […], en double […] » si une cellule de m = 10, 20 ou 40 manque ou est en double. Ce n'est jamais un repli silencieux. C'est le cas des configurations d'essai à m = 10 seul.
- **`reste_de_P6_sans_clause`** dit que la fausse alarme « entre 0,05 et 0,08 » et la détection « sans effet » par C et D sont rapportées sans mot.
- **Constantes neuves** : `M_DE_P6 = (10, 20, 40)`, `M_DE_LA_CLAUSE_DETECTION_P6 = (20, 40)`, `BORNE_FAUSSE_ALARME_P6 = (8, 100)`, `MOT_CARTE_ALARME`, `MENTION_PART_B`. Aucune constante existante ne change : l'essai `test_constantes_du_texte_cas_sain` du v2 passe tel quel.

### Noms (R12)

- `VERSION = "banc-juges-scriptes-ligne-3-v3"`.
- Fichiers de sortie : `resultat-…-v3.json` et `manifeste-…-v3.json`.
- Manifeste du chronométrage en v3.
- Le chronométrage charge le banc v3. Rien d'autre n'y change.

## Essais neufs (sain et artefact pour chaque ajout, R5)

| essai | ajout | ce qu'il montre |
|---|---|---|
| `test_alarme_silence_1_part_b_et_comptes_cas_sain_generateur_factice` | 1, sain | Générateur factice, 8 suites. Sentinelle : (a) = 0,5, (b) = 0,2, comptes (1, 2, 5, 2, 8). Bras C : (b) = 0,0 avec (a) indéfinie. Bras A et D : (b) indéfinie. Mélange (4, 2, 2, 4). Les mesures existantes du même cas sont aussi vérifiées. Le cas est dessiné pour que chaque lecture fautive rende une autre valeur : (b) = (a) rend 0,5 ; dénominateur sans les suites sans changement, 1/3 ; numérateur comptant une alarme avant changement, 0,4 ; génération 2 oubliée, 0,25. |
| `test_alarme_silence_1_part_b_artefacts_generateur_factice` | 1, artefact | Aucune détection : une suite « à effet » est en alarme seulement avant son changement, une suite sans changement est en alarme. (a) est indéfinie. (b) = 0,0 : la suite « à effet » est au dénominateur seulement. Aucune alarme donne (b) indéfinie, jamais 0. La fonction seule est aussi jouée sur des tableaux écrits à la main. |
| `test_alarme_silence_1_comptes_coherents_sur_une_cellule_tiree` | 1 | Une cellule tirée sur la racine des essais (400 suites, m = 20). Les comptes sont des entiers, cohérents entre eux. Les parts existantes sont exactement égales aux rapports de comptes. Aucune valeur n'est épinglée. |
| `test_alarme_p6_aide_cas_sain` | 2, sain | Fausse alarme à 80 sur 1 000, la borne, non dépassée ; B > D d'une suite à m = 20 et 40 ; B < D à m = 10, hors clause ; bras C piégé. Résultat : « P6 non réfutée » et carte sans mot. |
| `test_alarme_p6_aide_artefacts` | 2, artefact | 81 sur 1 000 à m = 10 seul ; 80 sur 999 (comptes entiers) ; B = D à m = 20 ; B = D à m = 40 ; B < D à m = 40. Chacun donne « P6 réfutée », avec la seule clause attendue. Une cellule manquante ou en double donne « incomplet ». Dans tous les cas, la carte reste sans mot. |
| `test_v3_sorties_existantes_du_v2_egales_a_l_octet` | les deux | Le banc v2 est chargé par son empreinte. `executer_etage_1` v2 et v3 sont joués sur `CONFIGURATION_D_ESSAI` et sur la même configuration avec l'alarme à m = 10, 20 et 40 (400 suites). Le test vérifie : clés du v2 toutes présentes ; clés neuves égales aux ajouts déclarés ; v3 réduit égal à l'octet ; dérivations égales ; mot de l'aide dans les deux mots, ou « incomplet » à m = 10 seul. |

Lancement : `env -C …/code-etage-1-v3 TMPDIR=…/tmp PYTHONDONTWRITEBYTECODE=1 python3 -B -m pytest -q -p no:cacheprovider …/essais_banc_juges_scriptes_ligne_3_v3.py`. Résultat : **115 passés, 0 échoué**, en 9,5 s puis 9,8 s. Aucun essai n'a échoué en chemin.

## Preuve que les sorties existantes ne changent pas

`comparer_sorties_v2_v3_ligne_3_v1.py`, en mode « essais » (racine 2026111930), produit `comparaison-sorties-v2-v3-ligne-3-v1.json`. Le rapport ne contient que des empreintes, des chemins de clés et des booléens, aucune valeur mesurée.

| configuration | résultat v2 | v3 réduit | clés du v2 absentes | clés neuves (= déclarées) | feuilles différentes | dérivations |
|---|---|---|---|---|---|---|
| `essai` (celle des essais, alarme m = 10, 40 suites) | `b1c6f967…2680` | `b1c6f967…2680` | 0 | 14 (oui) | `/version` | égales |
| `essai_alarme_trois_m` (alarme m = 10, 20, 40, 400 suites) | (dans le JSON) | égal à l'octet | 0 | 40 (oui) | `/version` | égales |

Deux gardes complètent la preuve :
- la relecture du v2 rend ses octets, ce qui valide la méthode ;
- les journaux de graines des deux modules ne contiennent que {2026111930}.

Ces points sont rejoués dans l'essai `test_v3_sorties_existantes_du_v2_egales_a_l_octet`.

## Contrôle « trop beau » (R4), rejoué en entier

| famille | vus (visé) | vus (complet) |
|---|---|---|
| v1 | 27 / 27 | 27 / 27 |
| contre-lecture (`mutants_cl.py`) | 35 / 35 | 35 / 35 |
| c2 | 1 / 1 | 1 / 1 |
| v2 (branche 3) | 1 / 1 | 1 / 1 |
| graines (toujours visés) | 6 / 6 | 6 / 6 |
| **v3_silence_1** (S01–S10) | 10 / 10 | 10 / 10 |
| **v3_silence_2** (P01–P11) | 11 / 11 | 11 / 11 |
| **v3_egalite** (E01–E02) | 2 / 2 | 2 / 2 |

- Sur le banc sain : essais visés, 78 passés ; fichier entier, 115 passés, l'essai final compris.
- Défauts neufs du silence 1 :
  - S01 : (b) = (a) ;
  - S02 : dénominateur sans les suites sans changement ;
  - S03 : indéfini rendu 0 ;
  - S04 : numérateur compte les alarmes avant changement ;
  - S05 : suites sans changement en alarme comptées sur toutes les suites ;
  - S06 : génération 2 oubliée ;
  - S07 : nombre de suites faux ;
  - S08 : suites qui changent détectées mal comptées ;
  - S09 : mélange faux ;
  - S10 : ajout absent.
- Défauts neufs du silence 2 :
  - P01 : « plus de » lu « au moins » ;
  - P02 : borne 0,05 ;
  - P03 : ≤ lu < ;
  - P04 : détection lue aussi à m = 10 ;
  - P05 : détection lue à m = 40 seul ;
  - P06 : fausse alarme lue sur C ;
  - P07 : détection contre C ;
  - P08 : « toutes » au lieu de « une » ;
  - P09 : la carte reçoit le mot de P6 ;
  - P10 : cellule manquante non signalée ;
  - P11 : fausse alarme lue aux seuls m de la détection.
- Défauts neufs de l'égalité :
  - E01 : la part (a) existante remplacée par (b) ;
  - E02 : aide absente.

  Ces deux défauts sont joués contre le seul essai d'égalité, pour montrer qu'il a des dents. E01 y échoue sur l'égalité à l'octet, E02 sur la liste des clés neuves.
- J'ai lu les lignes d'échec de S04, S09, P03, P08, P10, P11, E01 et E02 : chacun échoue sur l'assertion qui le nomme.

## Graines

- Seule la racine 2026111930 a été dérivée : essais, deux modes du contrôle, programme de comparaison.
- Aucune racine de 2026111931 à 2026111937 n'a été dérivée.
- L'essai final `test_zz_final_aucune_graine_des_racines_decisives_derivee` passe aux deux lancements et dans le mode « complet » sur le banc sain.
- Le banc v2 chargé dans le processus des essais ne dérive que la racine des essais ; l'essai d'égalité l'affirme.
- Aucun calcul décisif, aucun chronométrage à pleine taille.
- **Je n'ai lu aucune valeur de l'aide P6 sur des cellules tirées.** Les essais n'affirment que l'appartenance du mot aux deux mots. Le programme de comparaison n'écrit aucune valeur. L'alarme y est jouée à 400 suites, non à la taille décisive.

## Défauts vus, réserves, incidents

- **Deux fautes dans mon premier constructeur de JSON, vues à la relecture avant tout lancement.** Le mutant P11 (alors écrit avec `and lue`) aurait échoué par une variable non encore définie, donc pour une mauvaise raison. Un appel `**{10: …}` aurait été refusé par Python. Je les ai corrigées par l'outil de remplacement : `construire_remplacements_v3_v1.py` → `…_v2.py`, 6 ancres acceptées. Le fautif est gardé dans `brouillons/`. Aucune ancre n'a été rejetée par l'outil.
- **Une option de `diff` refusée** (`--output`, absente de ce `diff`). J'ai relancé avec une redirection. Ce n'est pas un refus de permission.
- **Clé `comptes_du_melange_plante`** : ajout déclaré plus haut, hors des cinq comptes demandés.
- **« Indéfini » vaut `null`**, comme pour la part (a) du v2, et non la chaîne « indéfini ».
- **Les journaux de l'outil de remplacement** se trouvent à côté des fichiers v3, dans `code-etage-1-v3/`, parce que l'outil les écrit à côté de sa sortie.
- **Appels git du code hérité du v2.** Le manifeste appelle `git rev-parse` et `git status --porcelain` sur le dossier du code : c'est le code hérité du v2, joué par les essais du v2 comme du v3. Je n'ai lancé moi-même aucune commande de liste.

**Aucun refus de permission, de classifieur ou de garde.**

Développeur, modèle L′.
