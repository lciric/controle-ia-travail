# Devis du collisionneur — Boucle de rétroaction « Organisme d'idéation ⇄ Programme de contrôle de l'intelligence artificielle » (v1)

Pièce de classe A (non scellée, soumise à contre-lecture d'un autre modèle puis à l'accord de Lazar), rédigée par Carbon en effort élevé en remplacement temporaire de Fable autorisé par `GO-2026-11-23-33`, sous le mandat `GO-2026-11-23-34`. Langue : français, aucun acronyme non développé, aucun emoji.

---

## 0. Résumé décisionnel

- **Périmètre** : deux dossiers du collisionneur épistémique à l'**étage III seul** (conception III.1, critique croisée III.2, réponse III.3), strictement **appariés** conformément à la règle 7 de `decision-economie-protocole-x-v1.md` :
  1. **Bras principal** : `faits-neutres-boucle-organisme-controle-v1.md` (`4 979` octets, `749` mots) + `question-neutre-collisionneur-boucle-organisme-controle-v1.md` (`2 887` octets, `440` mots).
  2. **Bras témoin ultra-neutre** (point 16 du lot 8) : `faits-neutres-boucle-organisme-controle-v1.md` (`4 979` octets, `749` mots) + `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` (`2 598` octets, `394` mots).
- **Garde de motifs vérifiée** : le moteur `docs/notes/collisionneur-v9/collisionneur_v9_v8d.py` rend `[]` (zéro alerte) sur les trois fichiers et sur tous les prompts `E3-T1` construits ; un témoin positif synthétique (`R5`) rend quatre catégories attendues.
- **Composition recommandée selon la règle d'économie du lot 8 (`decision-economie-protocole-x-v1.md`)** : **trois espèces décorrélées par famille** — **Opus 5.5** (`claude-opus-5-5`, Anthropic, via l'abonnement ou en repli interface), **Carbon** (`gemini-4-carbon`, Google, en flux continu) et **Neon** (`gemini-4-neon`, Google, en flux continu). Argon est retiré par défaut (redondant avec Carbon et moins fiable) ; Fable 5.2 est préservé pour les pièces décisives et contre-lectures (quota rare jusqu'au 29 novembre 2026) ; Astra peut être ajouté en option 4 espèces si Lazar souhaite une troisième famille d'interface.
- **Coût consolidé des deux bras appariés (3 espèces × 3 tours = 9 cellules par bras, soit 18 cellules au total)** :
  - **Option recommandée (A — Opus via abonnement + Carbon et Neon via interface Google)** :
    - **Attendu avec espérance de pannes** : `5,40` dollars par bras × `2` = **`10,80` dollars américains** (`4,31` dollars hors pannes par bras).
    - **Scénario haut avec pannes (type 22 novembre : 2 coupures de Carbon aux tours 1 et 2)** : `9,69` dollars par bras × `2` = **`19,38` dollars américains**.
    - **Pire cas sans relance (formule stricte de la garde)** : `11,93 + 11,92` = **`23,85` dollars américains**.
    - **Pire cas absolu avec toutes relances** : `35,78 + 35,77` = **`71,55` dollars américains** (inatteignable grâce à la ligne).
    - **Plafond et ligne recommandés par bras** : **`16` dollars par bras**, soit **`32` dollars américains au total** pour le couple apparié (couvre le scénario haut, la pointe de marge `10,57` et deux coupures supplémentaires de Carbon à `2,50` dollars l'une).
  - **Option de repli (B — Opus sur clé d'interface Anthropic + Carbon + Neon)** :
    - **Attendu avec pannes** : `7,26` dollars par bras × `2` = **`14,52` dollars américains**.
    - **Plafond et ligne recommandés par bras** : **`18` dollars par bras**, soit **`36` dollars américains au total**.

---

## 1. Espèces retenues, réglages et vérification de la garde Google v3

Conformément à la règle d'économie du lot 8 (`origin/idees/lot-8-chef-d-orchestre-v1:docs/notes/idee-interessante-v1/lot-8/decision-economie-protocole-x-v1.md`, section 3) :
1. **Décorrélation par famille avant multiplication d'une même famille** : Carbon et Neon (Google, deux profils distincts : Neon est la voix Google produisant le plus de références propres selon les mesures du lot 8, avec `14` à `29` références propres contre `6` à `8` pour Carbon) + Opus 5.5 (Anthropic). Argon est retiré par défaut ; son ajout éventuel reste chiffrable sans modifier le bras principal.
2. **Règle d'arrêt séquentielle de Neon** (`decision-economie-protocole-x-v1.md`, § 3 point 3) : ce dossier étant une question d'exploration ouverte et de conception stratégique, Neon est activé ; si l'audit post-course ne lui attribue pas au moins deux unités propres fortes, son maintien sera revu sur les dossiers suivants.
3. **Vérification exacte de la garde commune `src/controle_ia/garde_google_v3.py`** (`collisionneur_v9_v8d.py` l. 327-332, l. 1947-1960 ; `garde_google_v3.py` l. 68-151) :
   - **Carbon (`gemini-4-carbon`)** : mode `flux` (`streamGenerateContent`, limite `65 536` ; jamais en lot non diffusé car la limite y est `32 768` < `49 152 + 16 000`), niveau de réflexion explicite `"high"` (plus haut admis), `includeThoughts = true`, `maxOutputTokens = 65 536`, `provision = 49 152`, laissant **`16 384` jetons de texte** (`>= 16 000` exigés par `CLAUDE.md` l. 64-67). Vérification de limite de mots (`ratio = 4,2` jetons/mot pour Carbon selon `garde_google_v3.py` l. 80) :
     - Tours 1 et 3 (`3 500` mots max) : `ceil(3 500 × 4,2) = 14 700` jetons `< 16 384` (conforme, `problemes = []`).
     - Tour 2 (`3 000` mots max) : `ceil(3 000 × 4,2) = 12 600` jetons `< 16 384` (conforme, `problemes = []`).
   - **Neon (`gemini-4-neon`)** : mode `flux`, niveau de réflexion explicite `"xhigh"` (plus haut admis), `includeThoughts = true`, `maxOutputTokens = 65 536`, `provision = 32 768`, laissant **`32 768` jetons de texte** (`>= 16 000`). Vérification de limite de mots (`ratio = 5,1` jetons/mot par prudence selon `garde_google_v3.py` l. 80) :
     - Tours 1 et 3 (`3 500` mots max) : `ceil(3 500 × 5,1) = 17 850` jetons `< 32 768` (conforme, `problemes = []`).
     - Tour 2 (`3 000` mots max) : `ceil(3 000 × 5,1) = 15 300` jetons `< 32 768` (conforme, `problemes = []`).
   - **Opus 5.5 (`claude-opus-5-5`)** : effort `"high"`, plafond de sortie `64 000` jetons (moteur `v9-v8d`) ou `128 000` (voie abonnement).

**Tarifs appliqués (table `collisionneur_v9_v8d.py` l. 224-244 et l. 318-332, dollars américains par million de jetons entrée / sortie réflexion comprise) :**
- Opus 5.5 (voie abonnement) : `0,00 / 0,00` (coût d'interface `4,00 / 20,00` compté dans l'option B de repli).
- Carbon : compté au barème haut **`4,00 / 20,00`** par prudence (facturé `2,00 / 10,00` jusqu'au 30 novembre 2026 inclus, soit une facture réelle Google attendue environ deux fois moindre si exécuté avant le 1er décembre 2026).
- Neon : **`3,00 / 15,00`**.

---

## 2. Chiffrage cellule par cellule — Bras principal et Bras témoin ultra-neutre

Base de projection empirique : médianes, 90es centiles, ratios caractères/jeton et taux de pannes issus de `docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json` et `taux_pannes_v1.py` (taux de panne observés : Carbon `7/56 = 12,5 %`, Neon `1/26 = 3,85 %`, Opus `2/52 = 3,85 %`). Calcul exécuté exactement par la logique de `calcul_devis_v8_v3.py` et par la commande `devis` native de `collisionneur_v9_v8d.py`.

### 2.1 Option recommandée A : Opus par l'abonnement + Carbon + Neon (`9` cellules par bras)

#### Bras principal (`question-neutre-collisionneur-boucle-organisme-controle-v1.md`)

| Cellule | Espèce | Entrée attendue (jetons) | Sortie médiane / p90 (jetons) | Attendu (dollars américains) | Haut (dollars américains) | Pire sans relance (dollars américains) | Pire avec relances (dollars américains) |
|---|---|---|---|---|---|---|---|
| `E3-T1-conception-A` | Opus (abonnement) | `4 573` | `20 722 / 28 180` | `0,00` | `0,00` | `0,00` | `0,00` |
| `E3-T1-conception-B` | Carbon | `2 922` | `33 819 / 37 233` | `0,69` | `0,76` | `2,31` | `6,93` |
| `E3-T1-conception-C` | Neon | `2 968` | `34 709 / 41 580` | `0,53` | `0,63` | `1,49` | `4,46` |
| `E3-T2-critique-croisee-A` | Opus (abonnement) | `34 939` | `20 871 / 25 616` | `0,00` | `0,00` | `0,00` | `0,00` |
| `E3-T2-critique-croisee-B` | Carbon | `19 187` | `43 090 / 50 275` | `0,94` | `1,10` | `2,43` | `7,28` |
| `E3-T2-critique-croisee-C` | Neon | `18 960` | `42 520 / 46 941` | `0,69` | `0,78` | `1,59` | `4,76` |
| `E3-T3-reponse-A` | Opus (abonnement) | `50 533` | `25 526 / 32 149` | `0,00` | `0,00` | `0,00` | `0,00` |
| `E3-T3-reponse-B` | Carbon | `29 519` | `34 491 / 40 023` | `0,81` | `0,95` | `2,50` | `7,49` |
| `E3-T3-reponse-C` | Neon | `30 759` | `37 488 / 41 430` | `0,65` | `0,73` | `1,62` | `4,86` |
| **Total Bras principal (Option A)** | **9 cellules** | — | — | **`4,31`** | **`4,95`** | **`11,93`** | **`35,78`** |

- Espérance de pannes (taux empiriques × pire cas) : `1,09` dollars américains → **Attendu avec pannes : `5,40` dollars américains**.
- Scénario haut avec 2 coupures de Carbon (`E3-T1` et `E3-T2`) : **`9,69` dollars américains**, pointe de dépense + marge avant envoi : **`10,57` dollars américains** (`E3-T3-reponse-B`).
- Plafond pour tolérer 2 coupures de Carbon supplémentaires (`10,57 + 2 × 2,50 = 15,57` dollars américains) : **`16` dollars américains**.

#### Bras témoin ultra-neutre (`question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md`)

Les comptes d'entrée ne diffèrent que de `80` à `139` jetons (`440` mots contre `394` mots). Les totaux par cellule (arrondis au centime) et agrégés sont quasi identiques :

| Métrique (Option A) | Bras principal | Bras témoin ultra-neutre | Total des deux bras appariés |
|---|---|---|---|
| Attendu hors pannes | `4,31` dollars américains | `4,31` dollars américains | **`8,62` dollars américains** |
| Attendu avec espérance de pannes | `5,40` dollars américains | `5,40` dollars américains | **`10,80` dollars américains** |
| Haut hors pannes | `4,95` dollars américains | `4,95` dollars américains | **`9,90` dollars américains** |
| Haut + 2 coupures de Carbon | `9,69` dollars américains | `9,69` dollars américains | **`19,38` dollars américains** |
| Pire cas sans relance (garde) | `11,93` dollars américains | `11,92` dollars américains | **`23,85` dollars américains** |
| Pire cas avec relances | `35,78` dollars américains | `35,77` dollars américains | **`71,55` dollars américains** |
| **Plafond et ligne recommandés** | **`16,00` dollars américains** | **`16,00` dollars américains** | **`32,00` dollars américains** |

### 2.2 Comparaison avec l'option B (tout via interface, sans abonnement pour Opus) et devis natif de la garde

- **Option B (Opus payé sur clé Anthropic à `4 / 20` dollars américains par million de jetons, Carbon `4 / 20`, Neon `3 / 15`)** :
  - Opus ajoute `0,43 + 0,56 + 0,71 = 1,70` dollars américains attendus hors pannes (`2,16` dollars américains en haut, `4,23` dollars américains pire cas sans relance) par bras.
  - Total par bras : **`6,02` dollars américains** attendu hors pannes (**`7,26` dollars américains** avec espérance de pannes), **`7,11` dollars américains** haut hors pannes, **`11,85` dollars américains** en scénario haut avec 2 coupures de Carbon (pointe `12,73` dollars américains), **`16,15` dollars américains** pire sans relance.
  - Pour les deux bras appariés : **`14,52` dollars américains** attendus avec pannes ; plafond recommandé **`18` dollars américains par bras** (`36` dollars américains au total).
- **Devis natif de la commande `devis` de `collisionneur_v9_v8d.py` (borne maximale large avec 7 car/mot sur pièces complètes à 3 500 mots)** :
  - Étage III seul, par bras (tout par interface) : **`15,84` dollars américains** au pire cas sans relance (dont `4,09` dollars américains Opus, `7,13` dollars américains Carbon, `4,61` dollars américains Neon) ; soit **`31,68` dollars américains** pour les deux bras (`15,84 + 15,83` exacts).
  - Rappel sur la facturation effective avant le 1er décembre 2026 : Carbon étant facturé `2 / 10` dollars américains au lieu de `4 / 20` dollars américains jusqu'au 30 novembre inclus, la dépense réelle attendue sous l'option A sur les deux bras sera d'environ **`6,5` à `8,0` dollars américains** (hors rejeu massif de pannes), tout en gardant les plafonds scellés à `16` dollars par bras au barème prudent `4 / 20`.

---

## 3. Conditions d'appariement, d'arrêt et commandes prêtes à l'exécution

1. **Appariement strict (règle 7 de `decision-economie-protocole-x-v1.md`)** :
   - Les deux bras tournent sous le même moteur (`collisionneur_v9_v8d.py` ou sa révision sous voie abonnement), les mêmes trois espèces (`opus`, `carbon`, `neon`), les mêmes tours (`etage3` seul), les mêmes réglages de réflexion (`high` pour Carbon, `xhigh` pour Neon, `high` pour Opus) et le même plafond `--ligne-usd 16 --plafond-usd 16` chacun.
   - Si le quota d'abonnement est contraint, basculer les **deux** bras sur l'option B (`--plafond-usd 18 --ligne-usd 18` chacun) plutôt que de mélanger les voies entre bras principal et bras témoin.
2. **Garanties d'exécution** :
   - Aucune modification du dépôt avant l'accord explicite de Lazar ;
   - Aucune relance silencieuse : toute coupure technique entre au registre comme faux échec ;
   - Rejet automatique si `motifs_trouves` non vide, si la garde Google v3 échoue, si l'écart de jetons totaux est positif ou si zéro jeton de pensée est rendu (`CODE_PENSEES = 10`).
3. **Note de fin de dossier attendue (`CLAUDE.md` l. 69-70)** : une synthèse équilibrée en Markdown et en document portable PDF comparant les sorties du bras principal et du bras témoin ultra-neutre (test d'effet d'orientation) sera rédigée à l'issue des deux courses avant toute réutilisation dans l'organisme.
