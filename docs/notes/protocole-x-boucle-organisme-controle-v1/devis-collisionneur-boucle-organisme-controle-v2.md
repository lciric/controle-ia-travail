# Devis du collisionneur — Boucle de rétroaction « Organisme d'idéation ⇄ Programme de contrôle de l'intelligence artificielle » (v2)

Pièce de classe A (non scellée, révisée après test aveugle de neutralité et contre-lecture de rang deux), rédigée par Carbon en effort élevé en remplacement temporaire de Fable autorisé par l'accord du 23 novembre 2026 numéro 33, sous le mandat numéro 34 du même jour. Langue : français, aucun acronyme non développé, aucun emoji.

---

## 0. Résumé décisionnel

- **Périmètre et fichiers recalculés (versions deux prêtes après retouche de neutralité)** : deux dossiers du collisionneur épistémique à l'**étage trois seul** (conception, critique croisée et réponse finale), strictement **appariés** conformément à la règle 7 de la décision d'économie du lot huit :
  1. **Bras principal** : `faits-neutres-boucle-organisme-controle-v2.md` (`4 946` octets sur disque en codage Unicode à huit bits, `4 780` caractères normalisés mesurés par la fonction de lecture d'entrée, `717` mots) et `question-neutre-collisionneur-boucle-organisme-controle-v2.md` (`2 853` octets sur disque, `2 758` caractères normalisés, `410` mots).
  2. **Bras témoin ultra-neutre** (déjà admis à `0,18` au test aveugle de devinette) : `faits-neutres-boucle-organisme-controle-v2.md` (`4 946` octets, `4 780` caractères normalisés, `717` mots) et `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md` (`2 703` octets sur disque, `2 598` caractères normalisés, `394` mots).
- **Garde de motifs vérifiée** : la fonction `motifs_trouves` du moteur `collisionneur_v9_v8d.py` rend la liste vide `[]` (zéro alerte) sur `faits-neutres-boucle-organisme-controle-v2.md`, `question-neutre-collisionneur-boucle-organisme-controle-v2.md`, `question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md`, `sous-question-organisme-boucle-controle-v2.md`, ainsi que sur tous les prompts assemblés du premier tour pour les trois espèces ; un témoin positif synthétique déclenche bien deux catégories attendues.
- **Composition recommandée selon la règle d'économie du lot huit** : **trois espèces décorrélées par famille** — **Opus 5.5** (`claude-opus-5-5`, Anthropic), **Carbon** (`gemini-4-carbon`, Google, en flux continu) et **Neon** (`gemini-4-neon`, Google, en flux continu). Argon est retiré par défaut ; Fable 5.2 reste réservé aux pièces décisives et contre-lectures.
- **Choix opérationnel immédiat entre l'Option A et l'Option B** :
  - Comme l'abonnement Claude atteint son quota épuisé aujourd'hui et que le moteur `collisionneur_v9_v8d.py` (lignes 807 et 808) exige `--cle-anthropic` et facture Opus au tarif d'interface (`4,00` dollars en entrée et `20,00` dollars en sortie par million de jetons), **les deux options complètes sont présentées à parité** :
  - **Option A (Opus par la voie abonnement à `0,00 / 0,00` + Carbon et Neon sur l'interface Google, lorsque le quota d'abonnement est disponible et via le lanceur adapté à la voie abonnement)** :
    - **Attendu avec espérance de pannes** : `5,40` dollars par bras (`5,3957` sur le bras principal, `5,3946` sur le bras témoin), soit **`10,79` dollars américains au total** (`8,62` dollars hors pannes).
    - **Scénario haut avec deux coupures de Carbon (type 22 novembre)** : `9,68` dollars par bras (`9,6825` et `9,6810`), soit **`19,36` dollars américains au total**.
    - **Pire cas sans relance (formule stricte de la garde)** : `11,92 + 11,92` = **`23,84` dollars américains**.
    - **Pire cas absolu avec toutes relances** : `35,77 + 35,76` = **`71,53` dollars américains** (hors d'atteinte grâce au plafond de dépense).
    - **Plafond et ligne recommandés par bras** : **`16` dollars par bras**, soit **`32` dollars américains au total** pour le couple apparié.
  - **Option B (Opus sur clé d'interface de programmation Anthropic à `4,00 / 20,00` + Carbon et Neon sur interface Google — immédiatement exécutable sous `collisionneur_v9_v8d.py` sans attente de quota d'abonnement ni écriture de nouveau code)** :
    - **Attendu avec espérance de pannes** : `7,26` dollars par bras (`7,2588` sur le bras principal, `7,2568` sur le bras témoin), soit **`14,52` dollars américains au total** (`12,02` dollars hors pannes).
    - **Scénario haut avec deux coupures de Carbon (type 22 novembre)** : `11,84` dollars par bras (`11,8402` et `11,8378`), soit **`23,68` dollars américains au total**.
    - **Pire cas sans relance (formule stricte de la garde)** : `16,14 + 16,14` = **`32,29` dollars américains**.
    - **Pire cas absolu avec toutes relances** : `44,21 + 44,21` = **`88,42` dollars américains**.
    - **Plafond et ligne recommandés par bras** : **`18` dollars par bras**, soit **`36` dollars américains au total** pour le couple apparié.

---

## 1. Espèces retenues, réglages et vérification de la garde Google version trois

Conformément à la décision d'économie du lot huit (section 3) :
1. **Décorrélation par famille avant multiplication d'une même famille** : Carbon et Neon (Google, deux profils distincts : Neon est la voix Google produisant le plus de références propres selon les mesures du lot huit, avec `14` à `29` références propres contre `6` à `8` pour Carbon) associés à Opus 5.5 (Anthropic). Argon est retiré par défaut.
2. **Règle d'arrêt séquentielle de Neon** : ce dossier relevant d'une exploration ouverte et de conception stratégique, Neon est activé ; si l'audit post-course ne lui attribue pas au moins deux unités propres fortes, son maintien sera réévalué sur les dossiers suivants.
3. **Vérification exacte de la garde commune `garde_google_v3.py`** (`collisionneur_v9_v8d.py` lignes 327 à 332 et 1947 à 1960 ; `garde_google_v3.py` lignes 68 à 151) :
   - **Carbon (`gemini-4-carbon`)** : mode `flux` (limite `65 536` ; jamais en lot non diffusé car la limite y est `32 768`, inférieure à `49 152 + 16 000 = 65 152`), niveau de réflexion explicite `"high"`, inclusion des pensées activée, plafond de sortie `65 536`, provision de réflexion `49 152`, laissant **`16 384` jetons de texte** (`>= 16 000` exigés par les règles permanentes). Vérification de limite de mots (ratio de prudence `4,2` jetons par mot selon `garde_google_v3.py`) :
     - Tours un et trois (`3 500` mots maximum) : plafond entier de `3 500 × 4,2` = `14 700` jetons `< 16 384` (conforme, `verifier_reglages_google` rend `[]`).
     - Tour deux (`3 000` mots maximum) : `3 000 × 4,2` = `12 600` jetons `< 16 384` (conforme, `verifier_reglages_google` rend `[]`).
   - **Neon (`gemini-4-neon`)** : mode `flux`, niveau de réflexion explicite `"xhigh"`, inclusion des pensées activée, plafond de sortie `65 536`, provision de réflexion `32 768`, laissant **`32 768` jetons de texte** (`>= 16 000`). Vérification de limite de mots (ratio de prudence `5,1` jetons par mot selon `garde_google_v3.py`) :
     - Tours un et trois (`3 500` mots maximum) : plafond entier de `3 500 × 5,1` = `17 850` jetons `< 32 768` (conforme, `verifier_reglages_google` rend `[]`).
     - Tour deux (`3 000` mots maximum) : `3 000 × 5,1` = `15 300` jetons `< 32 768` (conforme, `verifier_reglages_google` rend `[]`).
   - **Opus 5.5 (`claude-opus-5-5`)** : effort `"high"`, plafond de sortie `64 000` jetons sous `collisionneur_v9_v8d.py` (ou `128 000` via la voie abonnement).

**Tarifs appliqués (table `collisionneur_v9_v8d.py` lignes 224 à 244 et 318 à 332, dollars américains par million de jetons en entrée / sortie avec réflexion) :**
- Opus 5.5 : `0,00 / 0,00` en Option A (voie abonnement) ; `4,00 / 20,00` en Option B (clé d'interface de programmation Anthropic).
- Carbon : compté au barème haut **`4,00 / 20,00`** par prudence (facturé `2,00 / 10,00` jusqu'au 30 novembre 2026 inclus, soit une facture Google effective environ deux fois plus faible avant le 1er décembre 2026).
- Neon : **`3,00 / 15,00`**.

---

## 2. Chiffrage cellule par cellule — Bras principal et Bras témoin ultra-neutre

Base de projection empirique : médianes, 90es centiles, ratios caractères par jeton et taux de pannes issus de `releve-journaux-v2.json` et `taux_pannes_v1.py` (taux de panne observés : Carbon `7/56 = 12,5 %`, Neon `1/26 = 3,85 %`, Opus `2/52 = 3,85 %`). Calcul exécuté exactement selon la logique de `calcul_devis_v8_v3.py` et vérifié face à la fonction `devis` native de `collisionneur_v9_v8d.py`.

### 2.1 Bras principal en Option A et Option B (`question-neutre-collisionneur-boucle-organisme-controle-v2.md`)

En Option A, les cellules Opus (`A`) coûtent `0,00` dollar (abonnement). En Option B, elles suivent le barème d'interface Anthropic (`4,00 / 20,00` dollars par million de jetons), indiqué entre parenthèses dans la ligne de chaque cellule Opus :

| Cellule | Espèce | Entrée attendue (jetons) | Sortie médiane / 90e centile (jetons) | Attendu Option A / Option B (dollars) | Haut Option A / Option B (dollars) | Pire sans relance Option A / Option B (dollars) | Pire avec relances Option A / Option B (dollars) |
|---|---|---:|---:|---:|---:|---:|---:|
| `E3-T1-conception-A` | Opus 5.5 | `4 431` | `20 722 / 28 181` | `0,00` / `0,43` | `0,00` / `0,58` | `0,00` / `1,30` | `0,00` / `2,59` |
| `E3-T1-conception-B` | Carbon | `2 831` | `33 819 / 37 234` | `0,69` / `0,69` | `0,76` / `0,76` | `2,31` / `2,31` | `6,93` / `6,93` |
| `E3-T1-conception-C` | Neon | `2 877` | `34 709 / 41 581` | `0,53` / `0,53` | `0,63` / `0,63` | `1,49` / `1,49` | `4,46` / `4,46` |
| `E3-T2-critique-croisee-A` | Opus 5.5 | `34 793` | `20 871 / 25 616` | `0,00` / `0,56` | `0,00` / `0,69` | `0,00` / `1,44` | `0,00` / `2,88` |
| `E3-T2-critique-croisee-B` | Carbon | `19 095` | `43 090 / 50 275` | `0,94` / `0,94` | `1,10` / `1,10` | `2,43` / `2,43` | `7,27` / `7,27` |
| `E3-T2-critique-croisee-C` | Neon | `18 868` | `42 520 / 46 942` | `0,69` / `0,69` | `0,78` / `0,78` | `1,59` / `1,59` | `4,76` / `4,76` |
| `E3-T3-reponse-A` | Opus 5.5 | `50 375` | `25 526 / 32 150` | `0,00` / `0,71` | `0,00` / `0,89` | `0,00` / `1,49` | `0,00` / `2,97` |
| `E3-T3-reponse-B` | Carbon | `29 421` | `34 491 / 40 024` | `0,81` / `0,81` | `0,95` / `0,95` | `2,50` / `2,50` | `7,49` / `7,49` |
| `E3-T3-reponse-C` | Neon | `30 658` | `37 488 / 41 431` | `0,65` / `0,65` | `0,73` / `0,73` | `1,62` / `1,62` | `4,86` / `4,86` |
| **Total Bras principal** | **9 cellules** | — | — | **`4,31` / `6,01`** | **`4,95` / `7,10`** | **`11,92` / `16,14`** | **`35,77` / `44,21`** |

Précision sur les relances et sur la pointe de dépense en cours d'exécution :
- En mode `flux`, Carbon et Neon ont des plafonds identiques (`65 536` en essai initial comme en relance), si bien que le moteur autorise jusqu'à `2` relances par cellule Google (relance identique puis dernier recours), d'où le facteur `3` sur le pire cas (`11,9223 × 3 = 35,7668` dollars américains en Option A), tandis qu'Opus en Option B n'a qu'une seule relance (`4,2220 × 2 = 8,4440` dollars, portant le pire cas avec toutes relances à `35,7668 + 8,4440 = 44,2107` dollars).
- Dans le scénario haut avec deux coupures de Carbon (`E3-T1-conception-B` et `E3-T2-critique-croisee-B`), la **pointe de dépense plus marge exigée avant envoi** est atteinte exactement au lancement de la toute dernière cellule **`E3-T3-reponse-C` (Neon)** : `8,9518 + 1,6185 = 10,5703` dollars (`10,57` dollars américains) en Option A, et `11,1094 + 1,6185 = 12,7279` dollars (`12,73` dollars américains) en Option B. L'ajout de deux coupures supplémentaires de Carbon à `2,4958` dollars l'une donne respectivement `15,56` dollars (plafond entier **`16` dollars**) en Option A et `17,72` dollars (plafond entier **`18` dollars**) en Option B.

### 2.2 Comparaison consolidée des deux bras appariés (Option A et Option B)

| Grandeur (dollars américains) | Option A Principal / Témoin | Option A Total (2 bras) | Option B Principal / Témoin | Option B Total (2 bras) |
|---|---:|---:|---:|---:|
| Attendu hors pannes | `4,3113 / 4,3104` | **`8,62`** | `6,0121 / 6,0103` | **`12,02`** |
| Espérance de pannes | `1,0843 / 1,0842` | **`2,17`** | `1,2467 / 1,2466` | **`2,49`** |
| **Attendu avec espérance de pannes** | **`5,3957 / 5,3946`** | **`10,79`** | **`7,2588 / 7,2568`** | **`14,52`** |
| Haut hors pannes (90e centile) | `4,9471 / 4,9461` | **`9,89`** | `7,1047 / 7,1029` | **`14,21`** |
| Haut avec 2 coupures de Carbon | `9,6825 / 9,6810` | **`19,36`** | `11,8402 / 11,8378` | **`23,68`** |
| Pointe + marge avant envoi (`E3-T3-reponse-C`) | `10,5703 / 10,5687` | — | `12,7279 / 12,7255` | — |
| Pire cas sans relance (garde) | `11,9223 / 11,9209` | **`23,84`** | `16,1442 / 16,1421` | **`32,29`** |
| Pire cas absolu avec toutes relances | `35,7668 / 35,7627` | **`71,53`** | `44,2107 / 44,2050` | **`88,42`** |
| **Plafond et ligne recommandés** | **`16,00 / 16,00`** | **`32,00`** | **`18,00 / 18,00`** | **`36,00`** |

### 2.3 Rapprochement avec la commande `devis` native et facturation avant le 1er décembre 2026

- **Devis natif de `collisionneur_v9_v8d.py` (borne large à `7` caractères par mot sur pièces complètes à `3 500` mots, au tarif d'interface `4 / 20` pour Opus et Carbon, `3 / 15` pour Neon)** :
  - Bras principal : **`15,83` dollars américains** (`15,8319` exacts : `4,09` Opus, `7,13` Carbon, `4,61` Neon).
  - Bras témoin ultra-neutre : **`15,83` dollars américains** (`15,8298` exacts : `4,09` Opus, `7,13` Carbon, `4,61` Neon).
  - Somme des deux bras : **`31,66` dollars américains** (`31,6616` exacts).
- **Facturation Google effective avant le 1er décembre 2026 (`Carbon` facturé `2,00 / 10,00` au lieu de `4,00 / 20,00`)** :
  - En Option A, le coût attendu passe à **`6,19` dollars hors pannes** et **`7,45` dollars avec espérance de pannes** sur les deux bras (`11,83` dollars dans le scénario haut à deux coupures de Carbon).
  - En Option B (exécution immédiate sur clé d'interface Anthropic sans attendre la réinitialisation du quota d'abonnement), le coût attendu passe à **`9,59` dollars hors pannes** et **`11,18` dollars avec espérance de pannes** sur les deux bras (`16,14` dollars dans le scénario haut à deux coupures de Carbon).
  - Par règle de prudence, les plafonds autorisés restent exprimés au tarif plein (`32` dollars en Option A, `36` dollars en Option B).

---

## 3. Conditions d'appariement, d'arrêt et discipline d'exécution

1. **Appariement strict (règle 7 de la décision d'économie du lot huit)** :
   - Les deux bras doivent impérativement partager la même voie d'exécution, les mêmes trois espèces (`opus`, `carbon`, `neon`), le même périmètre (`etage3` seul), les mêmes réglages de réflexion (`high` pour Carbon, `xhigh` pour Neon, `high` pour Opus) et le même plafond (`--plafond-usd 18 --ligne-usd 18` chacun en Option B immédiate sous `collisionneur_v9_v8d.py`, ou `--plafond-usd 16 --ligne-usd 16` chacun en Option A dès disponibilité du quota d'abonnement et du lanceur adapté). Il est interdit de panacher voie abonnement et voie interface entre les deux bras.
2. **Garanties d'exécution** :
   - Ne lancer la course qu'après validation de neutralité des fichiers en version deux par le lecteur aveugle de devinette (score inférieur à `0,50`) et autorisation explicite du directeur du programme ;
   - Aucune modification du dépôt avant accord ;
   - Aucune relance silencieuse : toute coupure technique entre au registre comme faux échec ;
   - Rejet automatique si `motifs_trouves` rend un motif non vide, si `garde_google_v3` échoue, si l'écart de jetons totaux est positif ou si zéro jeton de pensée est rendu.
3. **Note de fin de dossier attendue (règles permanentes lignes 69 et 70)** : une synthèse équilibrée en Markdown et en document portable comparant les sorties du bras principal et du bras témoin ultra-neutre (test d'effet d'orientation et audit de la règle d'arrêt séquentielle de Neon) sera rédigée à l'issue des deux courses avant toute réutilisation dans l'organisme.
