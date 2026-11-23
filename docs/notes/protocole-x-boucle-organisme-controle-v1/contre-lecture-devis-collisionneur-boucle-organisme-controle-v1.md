# Contre-lecture R2 du devis du collisionneur — Boucle « Organisme d'idéation ⇄ Contrôle de l'intelligence artificielle »

Pièce examinée : [devis-collisionneur-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/protocole-x-boucle-organisme-controle/devis-collisionneur-boucle-organisme-controle-v1.md).
Référentiels lus : [CLAUDE.md](file:///home/antigravity/lciric/controle-ia-travail/CLAUDE.md), [garde_google_v3.py](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/garde_google_v3.py), [collisionneur_v9_v8d.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py), [releve-journaux-v2.json](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json), [taux_pannes_v1.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/service-collisionneur-modes-v8-v1/calculs/taux_pannes_v1.py), [sortie-taux-pannes-v1.txt](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/service-collisionneur-modes-v8-v1/calculs/sortie-taux-pannes-v1.txt), [calcul_devis_v8_v3.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/service-collisionneur-modes-v8-v1/calculs-v3/calcul_devis_v8_v3.py) et `origin/idees/lot-8-chef-d-orchestre-v1:docs/notes/idee-interessante-v1/lot-8/decision-economie-protocole-x-v1.md`.
Scripts indépendants de recalcul conservés dans le brouillon : [verif_devis.py](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cl-protocole-x-boucle/verif_devis.py) et [verif_scenario22.py](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cl-protocole-x-boucle/verif_scenario22.py).

---

## 1. Verdict global

**Verdict : conforme sur l'arithmétique et les règles matérielles, sous réserve de deux précisions mineures et d'un blocage d'appariement et de neutralité.**

1. **Arithmétique et règles Google v3 / Carbon / Lot 8** : **validés à 100 %**. Chaque montant cellule par cellule, chaque sous-total, chaque pire cas (sans relance et avec deux relances sur Google), l'espérance de pannes, le scénario haut avec deux coupures de Carbon, la pointe avant envoi et les plafonds (`16` dollars américains par bras en Option A, `18` dollars américains par bras en Option B) sont exacts au centime près.
2. **Réserve technique majeure (voie abonnement hors moteur `v9-v8d`)** : le moteur [collisionneur_v9_v8d.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py) exige `--cle-anthropic` et facture Opus à l'interface (`4 / 20` dollars américains par million de jetons) ; il ne supporte pas directement l'exécution d'Opus via l'abonnement (`0,00 / 0,00` dollar). Le devis le signale en section 3 (« ou sa révision sous voie abonnement »), mais les deux commandes d'exécution prêtes à l'emploi de l'Option A supposent cet aménagement d'exécution (ou sinon le basculement sur l'Option B, ou une révision dédiée du script).
3. **Réserve d'exécution liée à l'étape 1 (test de neutralité)** : selon le rapport aveugle [test-neutralite-devinette-boucle-organisme-controle-v1.md](file:///home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/cl-protocole-x-boucle/test-neutralite-devinette-boucle-organisme-controle-v1.md), `question-neutre-collisionneur-boucle-organisme-controle-v1.md` obtient un score d'orientation de `0,68 >= 0,50`. L'autorisation financière peut être jugée sur ce devis (les écarts de taille après retouche seront inférieurs à `0,01` dollar américain), mais la course du bras principal ne doit partir qu'après retouche de la question neutre.

---

## 2. Vérification indépendante des tarifs, réglages et garde Google v3

| Paramètre vérifié | Devis v1 | Code de référence | Statut |
|---|---|---|---|
| Tailles des entrées (octets / caractères / mots) | Faits `4 979` / `749`, Question `2 887` / `440`, Témoin `2 598` / `394` | `faits` : `5 151` octets brute (`4 979` caractères normalisés), `749` mots ; `question` : `3 000` octets (`2 887` caractères normalisés), `440` mots ; `témoin` : `2 703` octets (`2 598` caractères normalisés), `394` mots | **Attention mineure** : le devis nomme « octets » les longueurs en caractères après normalisation (`lire_entree`), alors que la taille sur disque en UTF-8 avec accents est de `5 151`, `3 000` et `2 703` octets (sans impact sur les coûts, qui utilisent `len(lire_entree(...))`). |
| Tarifs (USD / million de jetons) | Opus `4,00 / 20,00` (ou `0 / 0` abo.), Carbon `4,00 / 20,00` (facturé `2 / 10` jusqu'au 30 nov.), Neon `3,00 / 15,00` | [collisionneur_v9_v8d.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py#L318-L332) : `opus=(4.0, 20.0)`, `carbon=(4.0, 20.0)`, `neon=(3.0, 15.0)` ; note pré-1er décembre exacte (lignes 234-235). | **Exact** |
| Carbon : réglages et règle `>= 16 000` jetons de texte | Mode `flux`, `thinkingLevel="high"`, `includeThoughts=True`, `maxOutputTokens=65 536`, `provision=49 152`, texte `16 384` ; jamais en lot non diffusé (`32 768 < 49 152 + 16 000`). | [collisionneur_v9_v8d.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py#L327-L329), [garde_google_v3.py](file:///home/antigravity/lciric/controle-ia-travail/src/controle_ia/garde_google_v3.py#L68-L151), [CLAUDE.md](file:///home/antigravity/lciric/controle-ia-travail/CLAUDE.md#L63-L67). Vérification Python : `65 536 - 49 152 = 16 384 >= 16 000` ; `non_diffuse` exige `65 152 > 32 768` (interdit). | **Exact** |
| Carbon : limite de mots (`ratio = 4,2`) | T1/T3 (`3 500` mots) : `ceil(3 500 × 4,2) = 14 700 < 16 384` ; T2 (`3 000` mots) : `12 600 < 16 384` ; `problemes = []`. | Vérifié via `garde_google_v3.verifier_reglages_google` : `problemes = []` aux tours 1, 2 et 3. | **Exact** |
| Neon : réglages et règle `>= 16 000` jetons de texte | Mode `flux`, `thinkingLevel="xhigh"`, `includeThoughts=True`, `maxOutputTokens=65 536`, `provision=32 768`, texte `32 768 >= 16 000`. | Vérifié via `garde_google_v3.verifier_reglages_google` et `collisionneur_v9_v8d.py` lignes 330-332 : `65 536 - 32 768 = 32 768 >= 16 000`. | **Exact** |
| Neon : limite de mots (`ratio = 5,1`) | T1/T3 (`3 500` mots) : `ceil(3 500 × 5,1) = 17 850 < 32 768` ; T2 (`3 000` mots) : `15 300 < 32 768` ; `problemes = []`. | Vérifié via `garde_google_v3.verifier_reglages_google` : `problemes = []` aux tours 1, 2 et 3. | **Exact** |
| Nombre de cellules | `3` espèces × `3` tours = `9` cellules par bras, soit `18` cellules appariées (`2` bras). | Tours `E3-T1` (3 cellules), `E3-T2` (3 cellules, 2 pièces injectées par cellule), `E3-T3` (3 cellules, 3 pièces injectées par cellule : propre conception + 2 critiques). | **Exact** |
| Règles d'économie du lot 8 | 3 espèces décorrélées (`opus`, `carbon`, `neon`) ; Argon retiré ; Fable réservé ; arrêt séquentiel Neon à `>= 2` unités propres fortes ; bras appariés. | Conforme à `decision-economie-protocole-x-v1.md` § 3 points 1 à 3, 5 et 7. | **Exact** |

---

## 3. Recalcul arithmétique complet (Option A, Option B, devis natif, avant 1er décembre)

### 3.1 Bras principal — Option A (`verif_devis.py`)

| Cellule | Entrée (devis / recalcul) | Médiane / 90e centile sortie | Attendu (devis / exact) | Haut (devis / exact) | Pire sans relance (devis / exact) | Pire avec relances (devis / exact) |
|---|---:|---:|---:|---:|---:|---:|
| `E3-T1-conception-A` (Opus abo.) | `4 573` / `4 573` | `20 722` / `28 181` | `0,00` / `0,0000` | `0,00` / `0,0000` | `0,00` / `0,0000` | `0,00` / `0,0000` |
| `E3-T1-conception-B` (Carbon) | `2 922` / `2 922` | `33 819` / `37 234` | `0,69` / `0,6881` | `0,76` / `0,7564` | `2,31` / `2,3110` | `6,93` / `6,9330` (2 rel.) |
| `E3-T1-conception-C` (Neon) | `2 968` / `2 968` | `34 709` / `41 581` | `0,53` / `0,5295` | `0,63` / `0,6326` | `1,49` / `1,4875` | `4,46` / `4,4625` (2 rel.) |
| `E3-T2-critique-croisee-A` (Opus abo.) | `34 939` / `34 939` | `20 871` / `25 616` | `0,00` / `0,0000` | `0,00` / `0,0000` | `0,00` / `0,0000` | `0,00` / `0,0000` |
| `E3-T2-critique-croisee-B` (Carbon) | `19 187` / `19 187` | `43 090` / `50 275` | `0,94` / `0,9385` | `1,10` / `1,0968` | `2,43` / `2,4255` | `7,28` / `7,2765` (2 rel.) |
| `E3-T2-critique-croisee-C` (Neon) | `18 960` / `18 960` | `42 520` / `46 942` | `0,69` / `0,6947` | `0,78` / `0,7815` | `1,59` / `1,5859` | `4,76` / `4,7576` (2 rel.) |
| `E3-T3-reponse-A` (Opus abo.) | `50 533` / `50 533` | `25 526` / `32 150` | `0,00` / `0,0000` | `0,00` / `0,0000` | `0,00` / `0,0000` | `0,00` / `0,0000` |
| `E3-T3-reponse-B` (Carbon) | `29 519` / `29 519` | `34 491` / `40 024` | `0,81` / `0,8079` | `0,95` / `0,9508` | `2,50` / `2,4963` | `7,49` / `7,4889` (2 rel.) |
| `E3-T3-reponse-C` (Neon) | `30 759` / `30 759` | `37 488` / `41 431` | `0,65` / `0,6546` | `0,73` / `0,7311` | `1,62` / `1,6189` | `4,86` / `4,8567` (2 rel.) |
| **Total Bras principal (Option A)** | — | — | **`4,31`** / **`4,3133`** | **`4,95`** / **`4,9491`** | **`11,93`** / **`11,9250`** | **`35,78`** / **`35,7751`** |

Note sur le nombre de relances : pour Carbon et Neon en mode `flux`, les plafonds sont égaux (`max = max_relance = 65 536`), donc `reglage_de_relance(m)[1]` est vrai et le moteur autorise jusqu'à `2` relances (relance identique, puis dernier recours au niveau inférieur), soit un facteur `3` sur le pire cas (`pire + 2 × pire_relance`). C'est exactement ce qui produit `35,78` dollars (`3 × 11,9250 = 35,7751`).

### 3.2 Totaux consolidés (espérance de pannes, scénario 22 novembre, Option A, Option B, devis natif)

| Grandeur vérifiée | Devis v1 | Recalcul Python exact | Écart |
|---|---:|---:|---|
| Option A — Espérance de pannes par bras (`7/56` Carbon, `1/26` Neon) | `1,09` | `1,0846` (principal) / `1,0844` (témoin) | `0,00` (arrondi au centime exact) |
| Option A — Attendu avec pannes (par bras / couple) | `5,40` / `10,80` | `5,3979` + `5,3959` = `10,7938` (`10,79` ou `2 × 5,40`) | `<= 0,01` (arrondi du doublé) |
| Option A — Scénario haut + 2 coupures Carbon (T1 et T2) | `9,69` / `19,38` | `9,6856` (principal) / `9,6829` (témoin) = `19,3685` | `0,01` sur le doublé |
| Option A — Pire sans relance (principal + témoin) | `11,93 + 11,92 = 23,85` | `11,9250 + 11,9226 = 23,8476` | **`0,00`** |
| Option A — Pire avec toutes relances (principal + témoin) | `35,78 + 35,77 = 71,55` | `35,7751 + 35,7677 = 71,5428` | **`0,00`** |
| Option A — Plafond recommandé (`pointe + 2 × 2,50`) | `16` / bras (`32` total) | `10,5734 + 2 × 2,4963 = 15,5660` → plafond entier `16` | **`0,00`** |
| Option B — Surcoût Opus (`4 / 20`) attendu / haut / pire | `1,70` (`0,43+0,56+0,71`) / `2,16` / `4,23` | `0,4327 + 0,5572 + 0,7127 = 1,7026` / `2,1594` / `4,2235` | **`0,00`** |
| Option B — Attendu hors pannes / avec pannes (bras / couple) | `6,02` / `7,26` (`14,52`) | `6,0159` / `7,2629` (témoin `7,2593`), couple `14,5222` | **`0,00`** |
| Option B — Haut / Haut + 2 coupures / Pire sans relance | `7,11` / `11,85` / `16,15` | `7,1085` / `11,8450` / `16,1486` | **`0,00`** |
| Option B — Plafond recommandé | `18` / bras (`36` total) | `12,7328 + 2 × 2,4963 = 17,7254` → plafond entier `18` | **`0,00`** |
| Devis natif `collisionneur_v9_v8d.py devis` (E3 seul, interface) | `15,84` + `15,83` = `31,68` (`4,09` Opus, `7,13` Carbon, `4,61` Neon) | Principal : `15,8362` (`4,09` Opus, `7,13` Carbon, `4,61` Neon) ; Témoin : `15,8324` ; Somme `31,6686` (`31,67`) | **`0,01`** sur la somme arrondie |
| Option A — Rappel facturation réelle avant 1er décembre (`Carbon 2/10`) | `6,5` à `8,0` dollars sur les 2 bras | Sans panne : `6,19` ; avec espérance de pannes : `7,46` ; avec 2 coupures en haut : `11,83` | Fourchette cohérente (`6,5` à `8,0` couvre `6,19` à `7,46`) |

---

## 4. Anomalies ou précisions à corriger / signaler avant GO

1. **Incohérence mineure sur la cellule porteuse de la pointe de dépense (ligne 70 du devis)** :
   - Le devis écrit « pointe de dépense + marge avant envoi : `10,57` dollars américains (`E3-T3-reponse-B`) » (et `12,73` en Option B).
   - Or, notre recalcul montre que `10,5734` dollars (et `12,7328` en Option B) est exactement la pointe atteinte au lancement de **`E3-T3-reponse-C` (Neon)** — la toute dernière cellule — lorsque `E3-T3-reponse-B` (Carbon) vient de réussir au 90e centile (`8,9545 + 1,6189 = 10,5734`). Au moment du lancement de `E3-T3-reponse-B`, la pointe est légèrement inférieure (`8,0037 + 2,4963 = 10,5000` en Option A et `10,1631 + 2,4963 = 12,6594` en Option B).
   - **Impact** : nul sur le plafond recommandé (`16` dollars en Option A et `18` dollars en Option B restent inchangés et exacts). Il convient simplement de corriger le nom de la cellule de pointe (`E3-T3-reponse-C` au lieu de `E3-T3-reponse-B`) si le devis est réédité.
2. **Désignation « octets » contre « caractères » en section 0** :
   - Les nombres `4 979`, `2 887` et `2 598` sont les nombres de caractères normalisés (`len(lire_entree(...))`), non les tailles exactes en octets sur disque (`5 151`, `3 000`, `2 703` octets en UTF-8). Sans effet sur les calculs.
3. **Voie d'exécution pour Opus par abonnement** :
   - Rappel explicite : [collisionneur_v9_v8d.py](file:///home/antigravity/lciric/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8d.py#L807-L808) refuse de démarrer `--opus` sans clé d'interface Anthropic (`--cle-anthropic`) et impute toujours les coûts à `4 / 20` dollars américains. L'Option A exige donc le lanceur adapté à la voie abonnement (ou une décision d'arbitre pour partir directement en Option B à `18` dollars américains par bras afin de préserver l'appariement strict sous le moteur `v9-v8d` sans écriture de nouveau code).
4. **Condition de neutralité issue de l'étape 1** :
   - Le devis peut être approuvé financièrement dès maintenant, mais l'exécution effective doit attendre la retouche de `question-neutre-collisionneur-boucle-organisme-controle-v1.md` (dont le score d'orientation est de `0,68 >= 0,50`).
