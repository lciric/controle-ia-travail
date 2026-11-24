# Vérification finale du billet sur les sondes (version 2) — rapport complet

- **Vérificateur** : même lecteur adverse et relecteur de cloisonnement que pour la version 1 (`session_56e50cd5dfc8c1b81e95e915fef3928b`), mandaté en règle de contre-lecture `R2` par la session mère sous les décisions d'autorisation `GO-2026-11-23-17` (point 3), `GO-2026-11-23-32` (points `B3` sur le calendrier face à l'entretien et `B5` sur le cloisonnement avant la porte de transfert `G1`) et `GO-2026-11-23-33`.
- **Auteur contrôlé** : rédacteur habilité version 2 (`6b17adceee85b87aede4e9548f406294`), lot situé dans `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/billet-sondes-v2/`.
- **Empreintes vérifiées** :
  - `billet-texte-entier-en-v2.md` : `1624e7d66b21913e8e55d671ac13c30ecfbce994222906fe00ebc30379b0c371`
  - `registre-affirmations-v2.json` : `25f3f39490bef0450794714523e86be07cefa2a609f13d99385e4010f4a0b884`
  - `construire-registre-affirmations-v2.py` : `146847ea42da4977fe0c7332ca7991f72d80bc03f69f49d649e11b82ac15655f`
  - `verifier-billet-texte-entier-v2.py` : `1612ea6161071115e57e5fbe241776af57da1978f584ca9c02ef33aec6c6fcc8`
  - `verifier-billet-texte-entier-v2-sortie.txt` : `22b02a486e4e486358f372798f396e128e952ac3aadbdd2e66f5ad456becf9f9`
  - `suivi-corrections-v1-vers-v2-complet.md` : `3ec51650074bde533aa6dbcc96b39f31b6a6ba83e80f35d236643e51d86b2bc0`
  - `suivi-corrections-v1-vers-v2-sans-chiffres-mere.md` : `bf8e99acc72d6472e033ff78b7baa0d41cce09d337516888add40acd38978eab`
- **Intégrité du dépôt** : aucune modification, création ni suppression apportée par ce sous-agent dans `/home/antigravity/lciric/controle-ia-travail`.

---

## 1. Verdict de vérification finale

**`CONFORME POUR RÉÉCRITURE PAR LAZAR`**

Les **23 constats** du rapport adverse sur la version 1 (**3 bloquants**, **11 majeurs**, **9 mineurs**) sont **tous résolus**. Aucune nouvelle erreur factuelle ni aucune fuite hors de la règle de cloisonnement `B5` (décision d'autorisation `GO-2026-11-23-32`) n'a été introduite. Six remarques mineures et sans gravité bloquante ni majeure (dont quatre de polissage éditorial lors de la réécriture manuelle par Lazar et deux de resserrement mécanique optionnel du registre ou du vérificateur) sont consignées à la section 4 pour mémoire.

---

## 2. Rejeu mécanique indépendant et audit du vérificateur version 2

### 2.1 Rejeu exact sous `PYTHONDONTWRITEBYTECODE=1`
Exécution directe le 2026-11-23 de :
```text
PYTHONDONTWRITEBYTECODE=1 /home/antigravity/lciric/controle-ia-travail/.venv/bin/python .../verifier-billet-texte-entier-v2.py
```
- **Code de sortie** : `0` ; résultat affiché : `RÉSULTAT : CONFORME`.
- **Comparaison octet pour octet** avec `verifier-billet-texte-entier-v2-sortie.txt` (`diff -u`) : **identique** (différence vide).
- **Sources vérifiées** : les 7 sources texte du dépôt (`V3`, `VB`, `B`, `Bb`, `E`, `L`, `P3`) concordent toutes en empreinte avec le registre et leur compagnon `.sha256` ; les 4 articles externes au format portable (`GD`, `FOMIN`, `MOHSIN`, `FIBS`) sont lus localement et concordent en empreinte à la fois avec le registre et avec leurs compagnons `.sha256`.
- **Couverture** : `321` jetons dans le corps contre `321` entrées au registre ; correspondance exacte section par section : `True`.
- **Comptes de mots mesurés** : `raw wc -w = 3527`, `hors balises LLM = 3437`, `TL;DR = 224` (`<= 250` : `True`, et les 250 premiers mots sans balises incluent déjà le titre et tout le résumé en tête couvrant les quatre expériences).
- **Autotest intégré (10 cas contraires)** : `10/10` refusés (`True`), couvrant notamment nombre faussé, ligne déplacée, troncature au premier mot d'une citation au format portable (`With ` → `Wit `), troncature au dernier mot (`trivial` → `trivia`), altération au milieu (`nearly `), mauvaise page (`35`), cardinal en toutes lettres faussé (`three`), emprunt croisé de section (`Step B` pointé sur `Bb`), qualificatif `lower_bound` appliqué à une estimation ponctuelle, et fuite `B5` (`transfer arm`).

### 2.2 Perturbations et audits complémentaires menés par le lecteur adverse
1. **Extraction exhaustive des jetons et nombres en lettres** : vérification indépendante de tout chiffre ou cardinal résiduel dans le corps après application de `EXCLUSIONS_DOC` et `RE_TOKEN` — seuls les identifiants `B1`, `B3` et `v2` restent hors jetons numériques, chacun explicitement documenté.
2. **Arrondis et tolérances** : vérification des `321` entrées contre l'arrondi standard (`round`) et l'arrondi à mi-chemin vers le haut (`ROUND_DIFF` vide hors notation scientifique exacte `10^{-4}`). Les notations scientifiques (`1.6 \times 10^{-22}`, `10^{-4}`) passent respectivement l'écart relatif (`< 0.02`, ici `0.62%` sur `1.59015668e-22`) et l'écart exact (`<= 1e-12`).
3. **Perturbations supplémentaires** :
   - Injection hors citation d'interdiction de `does not separate` → **refusée** (`True`).
   - Injection de `G1` (`before G1`) → **refusée** (`True`).
   - Altération du coefficient scientifique (`1.6` → `1.5`) → **refusée** (`True`).
   - *Point de vigilance mineur (remarque P-4)* : le test de présence de l'étiquette `"R15"` en ligne 335 du vérificateur cherche la sous-chaîne littérale `"R15"` dans tout le corps ; comme `"R15"` figure aussi en ligne 76 dans le résumé descriptif, la suppression de `"R15"` à la ligne 74 seule n'est pas arrêtée par ce seul contrôle tant qu'une occurrence demeure ailleurs dans le texte.

---

## 3. Contrôle point par point de la résolution des 23 constats de la version 1

### A. Rejeu mécanique et fidélité chiffrée (7 constats : 1 bloquant, 3 majeurs, 3 mineurs)

| Constat | Gravité | Vérification sur la version 2 | Verdict |
|---|---|---|---|
| **V-1** | **Bloquant** | Ligne 90 de `billet-texte-entier-en-v2.md` : les intervalles complets accompagnent désormais chaque estimation ponctuelle (`0.0184` [`−0.0189`, `0.0541`] à `0.25`, `−0.0290` [`−0.0726`, `0.0090`] à `0.5`, `0.0025` [`−0.0029`, `0.0082`] à `0.75`, `−0.0102` [`−0.0209`, `−0.0019`] à `1`), avec les 6 bornes enregistrées aux entrées `#230–231`, `#234–235`, `#238–239`. `verifier-billet-texte-entier-v2.py` contrôle `qualificatif_coherent` et rejette un mauvais qualificatif (autotest 9). | **Résolu** |
| **V-2** | **Majeur** | `charger_pdf()` lit localement les 4 documents au format portable en vérifiant à la fois `sha256` et `.sha256` compagnon ; `pat_pdf` impose `(?<!\w)…(?!\w)` ; `est_page` impose `p. <page>` / `page <page>` et `1 <= page <= n_pages` ; l'autotest vérifie séparément début, fin, milieu et numéro de page (`3` à `6`, tous `True`). | **Résolu** |
| **V-3** | **Majeur** | `SOURCES_PAR_SECTION` cloisonne strictement chaque section (`step_b` autorise `B` uniquement ; `p3bis` autorise `VB` et `B`) ; les doses de `Step B` (`#136–139`, `#148–150`, `#155`, `#174`, `#177–180`, `#188–190`, `#194`) pointent toutes vers `B` (`S25`–`S100`, `T100`), jamais vers `Bb`. Toutes les entrées hors PDF ont `lignes_portant_le_motif == 1` (`0` motif ambigu). Autotest `8` vérifié. | **Résolu** |
| **V-4** | **Majeur** | `EXCLUSIONS_DOC` documente explicitement toutes les chaînes non numériques exclues (`arXiv:...`, modèle, `log10`, code de run, étiquettes de protocoles/doses/réserves, condensats, pilotes contrôlés à part, `8B`). Les cardinaux/multiplicateurs en lettres (`two`, `threefold`, `Three`, `five`, `Two`, `three`, `Four`, `ten`, `one`, `four`) et les notations scientifiques sont extraits et vérifiés (`321/321` entrées, autotest `7` `True`). | **Résolu** |
| **V-5** | **Mineur** | Découpe depuis le titre inclus jusqu'à `## Hors billet` ; affichage séparé de `raw wc -w = 3527`, `hors balises LLM = 3437`, et contrôle automatique `TL;DR = 224 <= 250 : True`. L'étendue globale reste assumée en atelier tant que les réserves complètes sont maintenues dans le corps avant la réécriture manuelle de Lazar. | **Résolu** |
| **V-6** | **Mineur** | Précision homogénéisée à 4 décimales sur les grandeurs comparables : `0.7565` [`0.4410`, `1.0757`] et `0.0594` dans `P3-bis` (ligne 57, conformes à `VB` l. 224 et 351), `0.2872` et `0.1114` dans la note des lentilles (ligne 116, conformes à `L` l. 24 et 26). | **Résolu** |
| **V-7** | **Mineur** | Ligne 106 : `Hollinsworth et al. (arXiv:2610.12445v4, p. 1) report "98.7% AUROC in SHADE-Arena"` sépare explicitement la page `1` de `"becomes nearly trivial" (p. 34)`, avec contrôle contextuel `p. <page>` et appariement séquentiel dans la section. | **Résolu** |

### B. Cloisonnement `B5` selon la décision d'autorisation `GO-2026-11-23-32` (2 constats : 0 bloquant, 0 majeur, 2 mineurs)

| Constat | Gravité | Vérification sur la version 2 | Verdict |
|---|---|---|---|
| **B5-1** | **Mineur** | Suppression de l'annonce du saboteur discret en attente et retrait des marqueurs vides `<<SABOTEUR_DISCRET>>` et `<<LENTILLES_BBIS>>`, conformément à l'option `B3 (b)` consignée en note hors billet (ligne 137). Contrôle lexical de `verifier-v2` vérifiant l'absence de tout marqueur `<<...>>`. | **Résolu** |
| **B5-2** | **Mineur** | Ajout en fin de `TL;DR` (ligne 16) de l'unique phrase permise par la section `B.5` (`GO-2026-11-23-32`) : `"A further sabotage mode held back from probe design is not covered here."` — aucune nature, aucun chiffre, aucune mention du bras de transfert ni de la porte `G1`. Vérifié mot à mot et par contrôle lexical (`transfer[- ]arm`, `G1` absents, autotest `10` `True`). | **Résolu** |

### C. Règle `GO-2026-11-23-17` point 3, gabarit version 2 et réserves dans le corps (9 constats : 2 bloquants, 5 majeurs, 2 mineurs)

| Constat | Gravité | Vérification sur la version 2 | Verdict |
|---|---|---|---|
| **M-1** | **Bloquant** | Ligne 73 : `"and at dose 1, no probe is above its floor when separating the fine-tuned saboteur from that control adapter (not detected at this power)"` — respecte la règle gelée (« jamais ne sépare pas ») et nomme le rang `at dose 1`. Règle appliquée en plus dans `verifier-v2` (`does not separate` interdit hors citation d'interdiction de la ligne 9). | **Résolu** |
| **M-2** | **Bloquant** | Ligne 74 : `"and the semantic floor of unrelated concept directions was not read — so no above-floor probe (including concealment at 0.9017) can be said to separate better than an unrelated concept direction at the same layer (R15 attaches to every validity claim)."` — la portée retirée aux conclusions et le rattachement à toute phrase de validité sont fidèlement rendus d'après `B` l. 165. | **Résolu** |
| **M-3** | **Majeur** | Ligne 75 : `"the high-stakes permutation placebo fired (probe lower bound 0.4720 does not exceed the 0.95 quantile 0.5336 over 200 permutations; the label-leak audit named no leak)"` — la borne basse de la sonde (`0.4720`) est nommée explicitement contre le quantile (`0.5336`, `B` l. 114 et 574). | **Résolu** |
| **M-4** | **Majeur** | Lignes 55–57 : rétablissement complet de `PB-7` (`T vs. H on the deception probe is 0.5475, not above its floor`), de la réserve gelée déclenchée `PB-4` et de sa portée laissée ouverte (`0.7565 [0.4410, 1.0757]`, `53 tasks, 7 excluded`, `left open by the verdict`), de la borne marginale du moniteur (`≤ 1/61`), des deux probabilités (`P ≈ 1.6 \times 10^{-22}`, `P = 0.0594`), de la remarque sur la présence de texte planté, et de `blind only through that closure` sur les 3 pièces d'ouverture. | **Résolu** |
| **M-5** | **Majeur** | (1) Ligne 92 : mention explicite à `0.5` de `separates at equal tokens (0.8247) without being established to exceed the adapter alone`, détail à `0.75` et `1` des `2` lecteurs non battus (`words-and-cost baseline` et `honest reader`) ; (2) transfert inverse précisé `at dose 1` et `holds above its floor and null` ; (3) ajout de `temoin` (`lower bound 0.3319`) en ligne 72 et des bornes complètes `0.6456 and 0.6125 using the lower-bound distance` en ligne 43 ; (4) liste complète des réserves de procédure et de stabilité de `Step B-bis` en lignes 97–98 (`P-S25` pli `0` `≤ 10^{-4}` à `3` et `300` époques sans référence croisée hors déterminisme sur carte, changement d'entropie, code/fichiers de lancement et lecture hors manifeste, plafond de prix hors manifeste, image par nom, amorce de `41,436` caractères non éprouvée, registre non limité aux ajouts, règle d'ordre après coup, `1` correction sans revue tierce). | **Résolu** |
| **M-6** | **Majeur** | Gabarit version 2 appliqué dans l'ensemble du texte : résumé en tête et thèse dans les `241` premiers mots sans balises (`224` mots pour le seul résumé en tête) ; deux choix justifiés nommés contre option écartée (lignes 26 et 86) ; lexique en clair dans *Setup* (lignes 28–33) ; explicitations honnêtes entre crochets pour ce qui manque aux verdicts scellés (`Step B task count`, paramétrisation exacte des doses et modèle de base du saboteur réglé finement laissés à Lazar en lignes 24, 29, 114) ; empreintes SHA-256 des `6` verdicts et lien conditionnel à la ligne 128. | **Résolu** |
| **M-7** | **Majeur** | (1) Dans *Step B* (lignes 67–71), la phrase unique d'issue (`without object at this run... criterion 3 of governance gate G0`) est séparée nettement du paragraphe descriptif hors critère (`Outside the gate criterion...`), avec mention que la portée de `T7-P1` sous `R1`, `R3` et `R15` reste ouverte à l'auteur (`B` l. 227) ; (2) dans *Limits* (ligne 116), la note sur les lentilles est explicitement encadrée comme outil préparatoire non utilisé dans les résultats ci-dessus, et le marqueur vide `<<LENTILLES_BBIS>>` est retiré. | **Résolu** |
| **M-8** | **Mineur** | Ligne 43 : rappel explicite de $\log_{10}(3) \approx 0.4771$ face à `1.3211`, des 5 formes du champ de coût et des trois causes (`unit, proposal scale, or inflation`). Ligne 51 : mention exacte `ending the system message and placed before every action` (conforme au texte scellé de `P3-bis` l. 1158). | **Résolu** |
| **M-9** | **Mineur** | Corps intégralement encadré par `` `[LLM content block — start]` `` / `` `[LLM content block — end]` `` (`GO-2026-11-18-50`), avec consigne explicite de réécriture manuelle intégrale par Lazar en tête (ligne 1) et en notes hors billet (ligne 139). | **Résolu** |

### D. Attaques d'un lecteur sceptique (5 constats : 0 bloquant, 3 majeurs, 2 mineurs)

| Constat | Gravité | Vérification sur la version 2 | Verdict |
|---|---|---|---|
| **S-1** | **Majeur** | Justification en ligne 24 de la couche `15` et du maximum sur les jetons (verrouillés dans le plan `P3` avant toute course ; limite d'effacement d'un signal localisé nommée). Identification des trois lecteurs boîte noire (lignes 33 et 65) et reconnaissance franche en *Related work* et *Limits* (lignes 106 et 114) qu'un classifieur linéaire bon marché détecte déjà le sabotage dès les doses moyennes (`0.5` et plus). | **Résolu** |
| **S-2** | **Majeur** | Lignes 88–90, 96–97 et 126 : inversion à la dose `1` (`−0.0102 [−0.0209, −0.0019]`) et disqualification du bras plafond (`I5`) exposées de face ; absence de témoin d'adaptateur aux doses `0.25` à `0.75` signalée dans les limites et les questions ouvertes ; statut **provisoire** des aires jusqu'à `0.9994` affirmé explicitement tant que l'audit de symétrie `R4` reste inachevé. | **Résolu** |
| **S-3** | **Majeur** | Bloc *Plain definitions of terms used below* ajouté en *Setup* (lignes 28–33), titres descriptifs parallèles aux sigles, explication de la règle de départage de la sonde de dissimulation (`520` exemples, `118` validation, `5` sondes ex aequo à `1.0` départagées famille-puis-couche) et du critère `3` de la porte `G0`. | **Résolu** |
| **S-4** | **Mineur** | Ligne 55 : `0.7702` (coût visible seul) juxtaposé à `0.8012` avec l'aveu explicite que `the margin over declared cost is narrow`, suivi immédiatement de la réserve gelée déclenchée `PB-4` et de son impact ouvert sur `A` vs `T`. | **Résolu** |
| **S-5** | **Mineur** | Énumération des `5` formes du champ de coût (ligne 43), effectifs `520`/`118` et règle de départage (ligne 65), `6` préfixes de condensats SHA-256 vérifiables et condition de blocage avant mise en ligne du lien public jusqu'à mise à jour de la page publique `P3` avec `R-2299` (ligne 128). | **Résolu** |

---

## 4. Points de vigilance mineurs relevés sur la version 2 (sans gravité bloquante ni majeure)

Aucun de ces points n'invalide les faits, les chiffres, les réserves ni le cloisonnement `B5` ; ils sont signalés pour que Lazar puisse les lisser à sa main ou que le vérificateur puisse être resserré s'il sert sur d'autres versions :

1. **Règle d'au-dessus du plancher dans *Setup* (ligne 26) contre *Initial test (P3)* (ligne 43)** : la ligne 26 définit le critère « au-dessus » pour le lecteur général par l'intervalle de $D = \text{area} - \text{floor } 0.95 \text{ quantile}$ (`> 0`), sans mentionner que `P3` lui-même employait la borne basse de l'intervalle de la sonde comparée au quantile (`probe lower bound > floor 0.95 quantile`), ce qui est pourtant rappelé en ligne 43 au sujet des réserves `R-2299`. *Retouche conseillée lors de la réécriture* : préciser en ligne 26 que `P3` comparait directement la borne basse de la sonde au quantile avant le passage à l'intervalle apparié de $D$ à partir de `P3-bis`.
2. **Mot `temoin` et classement sous *Contrary reading (`R1`)* (ligne 72)** : `temoin` apparaît en français sans accent et sans définition dans l'article anglais, sous la puce *Contrary reading (`R1`)*, alors que dans le verdict de l'étape B (lignes 128 et 603), `temoin` était une condition témoin prédite **au-dessus** (comme l'organisme instruit) et non une prédiction contraire (seule `S100` était prédite « non au-dessus »). *Retouche conseillée* : clarifier en français/anglais que le jeu témoin positif (`temoin`) était lui aussi positif comme attendu, à la différence de `S100` qui déclenche `R1`.
3. **Renvoi de source de l'entrée `#186` dans `registre-affirmations-v2.json` (`over 200 permutations`)** : l'entrée `#186` (dans la phrase sur le placebo `T7-P19` en ligne 75) pointe vers `B` ligne 71 (`n_permutations 200` de l'épreuve `T0.6`), alors que la ligne exacte du placebo `enjeux-lineaire-c15` en annexe D (`B` ligne 574) porte elle aussi `permutations 200`. Les deux grandeurs valent `200`, donc le chiffre dans le billet est exact, mais pointer vers la ligne 574 avec le motif complet d'`enjeux-lineaire-c15 (i-a)` est plus fidèle.
4. **Resserrement optionnel de `verifier-billet-texte-entier-v2.py` sur deux détails** :
   - ligne 287 : `if q == "upper_bound": return ("]" in ctx or "`" in ctx)` laisse passer tout jeton entre accents graves même sans `"]"` ; exiger `"]" in ctx` ferme ce repli ;
   - ligne 335 : exiger `R15` (ou d'autres étiquettes) dans la section exacte concernée (`step_b`) plutôt que dans l'ensemble du corps, car une autre occurrence en ligne descriptrice masque une suppression locale ;
   - les deux expressions `a further sabotage mode` ou le sigle `ENC` en ligne 33 (alors que `ENC` n'est plus employé plus loin dans le texte) peuvent être nettoyés lors de la réécriture manuelle par Lazar, qui réduira aussi la longueur totale (`3 437` mots hors balises aujourd'hui) et tranchera les deux crochets laissés ouverts (`Step B` effectif de tâches et modèle de base du saboteur réglé finement) ainsi que la suite à donner aux sigles `P3`, `P3-bis`, `Step B`, `Step B-bis` (`CLAUDE.md` ligne 112).

---

## 5. Limites de cette vérification finale

- Les trois remarques de contenu réservées à Lazar hors scellés (nom du modèle de base du saboteur réglé finement, suite de l'audit de symétrie `R4` de l'étape B bis s'il est exécuté avant publication, mise à jour préalable de la page publique de `P3` avec `R-2299` avant tout lien, et réécriture intégrale à la main pour LessWrong) restent des conditions préalables à toute publication effective.
- Comme pour la v1, aucun fichier brut (`diag/`, `runs/`, `coffre/`, `essai/iib-explo-*`, `donnees/barreau5-*`, bras A, saboteur à budget ou mode tenu à l'écart) n'a été ouvert.

---

## 6. Mise à jour de la ligne `qui a lu quoi`

```text
| (n°) | session_56e50cd5dfc8c1b81e95e915fef3928b (lecteur adverse et relecteur de cloisonnement du billet sur les sondes v1 puis vérification finale v2 en règle R2, fille de ff6e9350-ef6c-4238-b52d-64a517f4205f) | compte Antigravity | modèle du sous-agent (hérité) | lu en v1 : pièces permises consignées en lecture v1 ; lu en plus en vérification finale v2 : lot scratch/billet-sondes-v2/{billet-texte-entier-en-v2.md (1624e7d6…), registre-affirmations-v2.json (25f3f394…), construire-registre-affirmations-v2.py (146847ea…), verifier-billet-texte-entier-v2.py (1612ea61…), verifier-billet-texte-entier-v2-sortie.txt (22b02a48…), suivi-corrections-v1-vers-v2-complet.md (3ec51650…), suivi-corrections-v1-vers-v2-sans-chiffres-mere.md (bf8e99ac…)} ; extraits de vérification dans prereg/P3-premier-test-i-a-v1.md (l. 123, 291, 318), prereg/P3-bis-temoin-positif-v1.md (l. 1211-1260), docs/notes/billets-v1/gabarit-billets-v2.md (en entier) et lignes de verdicts déjà ouverts en v1 (V3, VB, B, Bb, E, L). Non lu : coffre/*, essai/iib-explo-*, donnees/barreau5-*, bras A, saboteur à budget, bras d'attaque, mode tenu à l'écart, diag/*, runs/*. Aucune modification au dépôt | lecteur adverse et relecteur de cloisonnement v1 et vérificateur final v2 | mandats GO-2026-11-23-17 (point 3), GO-2026-11-23-32 (B3, B5), GO-2026-11-23-33, règle R2 | **exclu à vie** de toute conception ou réglage d'instrument, de sonde, de saboteur, d'organisme ou de moniteur, et de tout rôle devant rester aveugle aux verdicts lus de P3, P3-bis, étape B, étape B bis et tranche B-bêta des lentilles |
```
