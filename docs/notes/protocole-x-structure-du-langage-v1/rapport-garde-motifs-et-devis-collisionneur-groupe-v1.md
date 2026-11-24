# Rapport de garde de motifs et devis du collisionneur groupé — Dossier 1 (Structure du langage), série de pistes sur la naissance des idées scientifiques fécondes et dossiers thématiques 1 à 6 (version 1)

Pièce de travail (classe A candidate à la contre-lecture, non scellée), produite sur processeur (dépense nulle) sous les mandats des 23 et 24 novembre 2026 (`GO-2026-11-23-36` et `GO-2026-11-24-03`). Langue : français intégral, zéro émoji, groupes nominaux scientifiques explicites, tous chiffres calculés mécaniquement par `calcul_devis_collisionneur_groupe_v1.py` (sortie brute archivée dans `sortie-calcul-devis-collisionneur-groupe-v1.txt`).

---

## 1. Résumé décisionnel

1. **Passage mécanique de la garde de motifs (`collisionneur_v9_v8d.motifs_trouves`, réponse au constat `R-5214`)** :
   - **Zéro alerte (`[]`)** sur les trois pièces d'entrée et la synthèse du **Dossier 1 — Structure du langage** (`faits-neutres-structure-du-langage-v1.md`, `question-neutre-collisionneur-structure-du-langage-v1.md`, `question-temoin-neutre-structure-du-langage-v1.md`, `synthese-structure-du-langage-v1.md`) ainsi que sur l'ensemble des six prompts assemblés du premier tour (`E3-T1`) pour les trois espèces (bras principal et bras témoin).
   - **Zéro alerte (`[]`)** sur les fichiers `collisionneur-v2` des dossiers **dommages plantés par un tiers** (`faits-dommages-plantes-tiers-v2.md`, `question-dommages-plantes-tiers-v2.md`) et **marge asymétrique** (`faits-marge-asymetrique-v2.md`, `question-marge-asymetrique-v2.md`), levant directement le constat de la décision `R-5214`, ainsi que sur le dossier complémentaire **programmation de poids** (`faits-programmation-de-poids-v2.md`, `question-programmation-de-poids-v2.md`) et sur tous leurs prompts assemblés du tour `E3-T1`.
   - **Témoin positif synthétique** : déclenche bien les trois catégories attendues (`chemin interne`, `identifiant d'accord`, `identifiant de registre`).
2. **Garde Google version 3 (`garde_google_v3.verifier_reglages_google`)** : conforme (`probs=[]`) pour **Carbon** (`flux`, niveau `"high"`, plafond `65 536`, provision `49 152`, texte disponible `16 384 >= 14 700` jetons) et **Neon** (`flux`, niveau `"xhigh"`, plafond `65 536`, provision `32 768`, texte disponible `32 768 >= 17 850` jetons) sur les trois tours de l'étage 3 (`E3-T1`, `E3-T2`, `E3-T3`).
3. **Devis immédiat en Option B sous `collisionneur_v9_v8d.py`** (trois espèces décorrélées **Opus 5.5 + Carbon + Neon**, étage 3 seul, bras principal + bras témoin strictement appariés, `--plafond-usd 18 --ligne-usd 18` par bras) :
   - **Dossier 1 seul — Structure du langage (1 couple apparié, 2 bras, 18 cellules)** : attendu avec espérance de pannes **`14,65` dollars américains** au tarif plein (**`11,29` dollars** avant le 1er décembre 2026), scénario haut avec deux coupures de Carbon `23,84` dollars (`16,26` dollars avant le 1er décembre), pire cas sans relance `32,43` dollars, **plafond cumulé recommandé `36` dollars** (`18` dollars par bras).
   - **Scénario G1 — Collisionneur groupé unifié (1 couple apparié couvrant la série de pistes sur la naissance des idées scientifiques fécondes et les dossiers thématiques 1 à 6, entrée groupée `12 000 + 4 500` caractères, 18 cellules)** : attendu avec pannes **`14,74` dollars** (**`11,36` dollars** avant le 1er décembre), pire cas sans relance `32,52` dollars, **plafond cumulé `36` dollars** (économie de **83,3 %** par rapport à 6 couples séparés).
   - **Scénario G2 — Collisionneur groupé en deux axes thématiques (2 couples appariés, 4 bras, 36 cellules — recommandé pour préserver la profondeur de réponse sous la limite de 3 500 mots)** :
     - Axe A : *Structure du langage, représentation des connaissances et pistes sur la naissance des idées scientifiques fécondes* ;
     - Axe B : *Verrous du contrôle boîte blanche et des garanties d'audit (dommages plantés par un tiers, marge asymétrique, programmation de poids et contrôles connexes)* ;
     - Attendu avec pannes **`29,47` dollars** (**`22,73` dollars** avant le 1er décembre), scénario haut avec deux coupures de Carbon par bras `47,88` dollars, pire cas sans relance `65,05` dollars, **plafond cumulé recommandé `72` dollars** (`18` dollars par bras, économie de **66,7 %** par rapport à 6 couples séparés).

---

## 2. Compte rendu complet de la garde de motifs (`R-5214`)

Chaque fichier a été lu par la fonction `lire_entree` de `collisionneur_v9_v8d.py` puis passé à `motifs_trouves`, complété par l'assemblage réel des trois prompts du premier tour (`E3-T1`) pour Opus 5.5 (`A`), Carbon (`B`) et Neon (`C`) :

| Dossier contrôlé | Fichier de faits (taille / motifs) | Fichier de question (taille / motifs) | Prompts assemblés `E3-T1` (`A`, `B`, `C`) | Statut |
|---|---|---|---|---|
| **Dossier 1 — Structure du langage (bras principal)** | `faits-neutres-structure-du-langage-v1.md` (`10 212` o, `9 917` car., `1 475` mots) — `[]` | `question-neutre-collisionneur-structure-du-langage-v1.md` (`3 184` o, `3 065` car., `457` mots) — `[]` | `[]`, `[]`, `[]` | **Sain** |
| **Dossier 1 — Structure du langage (bras témoin)** | `faits-neutres-structure-du-langage-v1.md` (`10 212` o, `9 917` car., `1 475` mots) — `[]` | `question-temoin-neutre-structure-du-langage-v1.md` (`3 026` o, `2 911` car., `419` mots) — `[]` | `[]`, `[]`, `[]` | **Sain** |
| **Dommages plantés par un tiers (`collisionneur-v2`, constat `R-5214`)** | `faits-dommages-plantes-tiers-v2.md` (`4 611` o, `4 470` car., `780` mots) — `[]` | `question-dommages-plantes-tiers-v2.md` (`3 055` o, `2 971` car., `530` mots) — `[]` | `[]`, `[]`, `[]` | **Sain** |
| **Marge asymétrique (`collisionneur-v2`, constat `R-5214`)** | `faits-marge-asymetrique-v2.md` (`8 823` o, `8 534` car., `1 473` mots) — `[]` | `question-marge-asymetrique-v2.md` (`3 777` o, `3 674` car., `651` mots) — `[]` | `[]`, `[]`, `[]` | **Sain** |
| **Programmation de poids (`collisionneur-v2`, contrôle complémentaire)** | `faits-programmation-de-poids-v2.md` (`6 776` o, `6 539` car., `1 052` mots) — `[]` | `question-programmation-de-poids-v2.md` (`2 889` o, `2 798` car., `467` mots) — `[]` | `[]`, `[]`, `[]` | **Sain** |
| **Synthèse Dossier 1 (contrôle de transparence)** | `synthese-structure-du-langage-v1.md` (`23 210` o, `22 517` car., `3 163` mots) — `[]` | — | — | **Sain** |
| **Témoin positif synthétique** | Chaîne de contrôle portant un accord, un numéro de registre et un chemin interne | — | Détection de 3 catégories (`chemin interne`, `identifiant d'accord`, `identifiant de registre`) | **Garde active** |

---

## 3. Paramètres de chiffrage et vérification de la garde Google version 3

Conformément à la décision d'économie (`decision-economie-protocole-x-v1.md`) et au devis vérifié de la boucle de rétroaction entre l'organisme d'idéation et le programme de contrôle :
- **Composition Option B (exécutable immédiatement sous `collisionneur_v9_v8d.py`)** :
  - **Opus 5.5 (`claude-opus-5-5`)** : clé d'interface Anthropic, tarif `4,00 / 20,00` dollars par million de jetons (entrée / sortie), effort `"high"`, plafond `64 000`, une relance maximale (`rel=1`), taux de panne historique `2/52 = 3,85 %`.
  - **Carbon (`gemini-4-carbon`)** : mode `flux`, tarif plein de prudence `4,00 / 20,00` dollars par million de jetons (facturation effective `2,00 / 10,00` jusqu'au 30 novembre 2026 inclus), niveau `"high"`, plafond `65 536`, provision `49 152` (`16 384` jetons de texte `>= 16 000`), deux relances maximales (`rel=2`), taux de panne historique `7/56 = 12,50 %`.
  - **Neon (`gemini-4-neon`)** : mode `flux`, tarif `3,00 / 15,00` dollars par million de jetons, niveau `"xhigh"`, plafond `65 536`, provision `32 768` (`32 768` jetons de texte `>= 16 000`), deux relances maximales (`rel=2`), taux de panne historique `1/26 = 3,85 %`.
- **Argon** est retiré par défaut ; **Fable 5.2** reste réservé aux pièces décisives et contre-lectures.
- **Base empirique** : `releve-journaux-v2.json` (médianes, 90es centiles et ratios caractères par jeton observés) et `taux_pannes_v1.py`, rapprochés du devis natif de `collisionneur_v9_v8d.py`.

---

## 4. Détail cellule par cellule — Dossier 1 (Structure du langage, Option B, tarif plein)

| Cellule | Espèce | Entrée attendue (jetons) | Sortie médiane / 90e centile (jetons) | Attendu (USD) | Haut p90 (USD) | Pire sans relance (USD) | Pire avec relances (USD) | Espérance panne (USD) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `E3-T1-conception-A` | Opus 5.5 | `6 783` | `20 722 / 28 181` | `0,4416` | `0,5908` | `1,3055` | `2,6110` | `0,0502` |
| `E3-T1-conception-B` | Carbon | `4 334` | `33 819 / 37 234` | `0,6937` | `0,7620` | `2,3193` | `6,9578` | `0,2899` |
| `E3-T1-conception-C` | Neon | `4 403` | `34 709 / 41 581` | `0,5338` | `0,6369` | `1,4937` | `4,4811` | `0,0574` |
| `E3-T2-critique-croisee-A` | Opus 5.5 | `37 224` | `20 871 / 25 616` | `0,5663` | `0,6984` | `1,4485` | `2,8969` | `0,0557` |
| `E3-T2-critique-croisee-B` | Carbon | `20 620` | `43 090 / 50 275` | `0,9443` | `1,1025` | `2,4338` | `7,3013` | `0,3042` |
| `E3-T2-critique-croisee-C` | Neon | `20 398` | `42 520 / 46 942` | `0,6990` | `0,7858` | `1,5921` | `4,7762` | `0,0612` |
| `E3-T3-reponse-A` | Opus 5.5 | `52 994` | `25 526 / 32 150` | `0,7225` | `0,8981` | `1,4944` | `2,9888` | `0,0575` |
| `E3-T3-reponse-B` | Carbon | `31 054` | `34 491 / 40 024` | `0,8140` | `0,9569` | `2,5046` | `7,5137` | `0,3131` |
| `E3-T3-reponse-C` | Neon | `32 330` | `37 488 / 41 431` | `0,6593` | `0,7358` | `1,6251` | `4,8753` | `0,0625` |
| **Total 1 bras (principal)** | **9 cellules** | — | — | **`6,0746`** | **`7,1672`** | **`16,2168`** | **`44,4020`** | **`1,2518`** |
| **Total couple apparié (principal + témoin)** | **18 cellules** | — | — | **`12,1474`** | **`14,3326`** | **`32,4315`** | **`88,7986`** | **`2,5034`** |

- **Devis natif `collisionneur_v9_v8d.py`** : `15,9037 + 15,9017 = 31,8054` dollars américains.
- **Pointe + marge avant envoi de la dernière cellule (`E3-T3-reponse-C`) dans le scénario haut à deux coupures de Carbon** : `12,8095` dollars (bras principal) et `12,8072` dollars (bras témoin). En ajoutant deux coupures supplémentaires de Carbon (`2 × 2,5046`), on obtient `17,82` dollars, justifiant exactement le **plafond entier de `18` dollars par bras** (`36` dollars le couple apparié).
- **Repères de vérification sur les dossiers `collisionneur-v2` existants (1 bras, Option B)** :
  - Dommages plantés par un tiers : natif `15,83` USD, attendu avec pannes `7,26` USD (`5,59` USD avant le 1er décembre), pire cas sans relance `16,14` USD, plafond `18` USD par bras.
  - Marge asymétrique : natif `15,89` USD, attendu avec pannes `7,32` USD (`5,64` USD avant le 1er décembre), pire cas sans relance `16,21` USD, plafond `18` USD par bras.
  - Programmation de poids : natif `15,86` USD, attendu avec pannes `7,28` USD (`5,61` USD avant le 1er décembre), pire cas sans relance `16,17` USD, plafond `18` USD par bras.

---

## 5. Comparaison des architectures du collisionneur groupé (pistes sur la naissance des idées scientifiques fécondes et dossiers thématiques 1 à 6)

En sensibilité sur une entrée groupée large (`12 000` caractères de faits + `4 500` caractères de question pour le bras principal et `4 200` caractères pour le bras témoin), le surcoût par rapport au Dossier 1 seul reste inférieur à `0,09` dollar par couple apparié (`14,74` contre `14,65` dollars attendus avec pannes), car le coût est dominé par les jetons de sortie et de réflexion. Le nombre de couples appariés est donc le seul véritable levier budgétaire :

| Architecture du collisionneur groupé (Option B, étage 3 seul) | Couples appariés (bras / cellules) | Attendu avec pannes, tarif plein (USD) | Attendu avec pannes, avant le 1er déc. (USD) | Haut + 2 coupures Carbon par bras (USD) | Pire cas sans relance (USD) | Plafond cumulé recommandé (USD) | Économie contre G3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **G1 — Un couple apparié unifié** | `1` (`2` bras / `18` cellules) | **`14,74`** | **`11,36`** | `23,94` | `32,52` | **`36`** (`18`/bras) | **-83,3 %** |
| **G2 — Deux couples appariés par grand axe (RECOMMANDÉ)** | `2` (`4` bras / `36` cellules) | **`29,47`** | **`22,73`** | `47,88` | `65,05` | **`72`** (`18`/bras) | **-66,7 %** |
| **G3 — Six couples séparés sans regroupement (référence)** | `6` (`12` bras / `108` cellules) | `87,90` | `67,75` | `143,03` | `194,59` | `216` (`18`/bras) | `0,0 %` |

### Recommandation opérationnelle

1. **Si la priorité est le lancement immédiat du Dossier 1 — Structure du langage (ou d'un seul couple groupé G1)** : plafond cumulé **`36` dollars américains** (`--plafond-usd 18 --ligne-usd 18` par bras), attendu effectif **`11,29` à `11,36` dollars** avant le 1er décembre 2026 (`14,65` à `14,74` dollars au tarif plein).
2. **Pour couvrir sans dilution l'ensemble de la série de pistes sur la naissance des idées scientifiques fécondes et des dossiers thématiques 1 à 6 (scénario G2 recommandé)** : scinder en **deux couples appariés** (Axe A : structure du langage, représentation des connaissances et naissance des idées fécondes ; Axe B : verrous du contrôle boîte blanche, dommages plantés par un tiers, marge asymétrique et programmation de poids), afin que chaque réponse de `3 500` mots conserve sa profondeur mathématique et expérimentale. Plafond cumulé **`72` dollars américains** (`18` dollars par bras), attendu effectif **`22,73` dollars** avant le 1er décembre 2026 (`29,47` dollars au tarif plein), soit un tiers du coût d'un lancement non groupé.
3. **Conditions préalables avant tout envoi payant** : contre-lecture indépendante de ce devis (classe A), test aveugle de devinette de neutralité sur les couples de questions (score inférieur à `0,50`), et confirmation explicite de l'accord de dépense sur le plafond retenu (`36` ou `72` dollars).
