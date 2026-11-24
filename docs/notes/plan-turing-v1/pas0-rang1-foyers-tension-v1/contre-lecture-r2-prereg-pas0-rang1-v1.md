# Rapport de contre-lecture méthodologique indépendante — Préenregistrement de l'extraction rétrodictive des foyers de tension et d'épicycles (2024 vers 2025–2026, brouillon 1)

- **Sous-agent contre-lecteur neuf (règle de contre-lecture indépendante, `R2`)** : conversation `8ce0b993687504c727f5781919798801` (lecture seule stricte, aucun fichier ouvert dans les répertoires interdits ni dans `docs/sources/pdf/`)
- **Brouillon relu** : `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/pas0-rang1-foyers-tension/prereg-pas0-rang1-retrodiction-foyers-tension-2024-vers-2025-2026-v1-brouillon1.md`
- **Empreinte cryptographique sur 256 bits vérifiée du brouillon relu** : `28dc3ab6949ff312e2156ae869128d0b8723793c98107bb74054d8c9f87dfd62`
- **Autres pièces de référence lues explicitement et vérifiées par empreinte** :
  - `/home/antigravity/lciric/controle-ia-travail/docs/notes/protocole-x-boucle-organisme-controle-v1/reponse-approfondie-carbon-boucle-organisme-controle-v1.md` (`f744320dcd7c2a8c08ebb95375c4bd86322c5fd0a2bcdc43af7f3ef28f3e02a1`)
  - `/home/antigravity/lciric/controle-ia-travail/src/controle_ia/prereg.py`
  - `/home/antigravity/lciric/controle-ia-travail/CLAUDE.md` (`dcd1e7ceddf4d15cc90dc19cafded1775b38fb94b7148e267469377e5a5dd94f`), `/home/antigravity/lciric/controle-ia-travail/prereg/gabarit-preregistrement-v1.md` et entrées citées dans `/home/antigravity/lciric/controle-ia-travail/docs/notes/idee-interessante-v1/lot-8/registre-idees-session-2026-11-23-v1.md` (`e7bf754c9402dda105c67dde7ca58994c78beabe0f59fbd638b3f2c983f01d5a`)

## Verdict synthétique de contre-lecture

**REFUSÉ EN L'ÉTAT AVANT SCELLEMENT — 13 critiques (dont 7 bloquantes)** doivent être corrigées dans une version révisée avant tout scellement et toute ouverture des textes extraits. Le cadrage général est solide, mais le brouillon 1 comporte des collisions lexicales avérées qui feraient sauter ou biaiser la garde d'orthogonalité, une expression régulière défectueuse sur les preuves numérotées, un recollage de césures qui détruit les mots composés à trait d'union, un témoin nul « doit mourir » mathématiquement condamné à échouer à tort sous des effectifs sains, des cas de division par zéro ou d'indétermination totale de la cible binaire, l'absence de formules pour les variables dyadiques du test de Mantel, et plusieurs sigles anglais nus dans la prose française.

---

## Volet I — Disjonction des vocabulaires, expressions régulières et contamination thématique

### Critique 1 (Bloquante) — Violations directes de la disjonction mutuelle entre `L_axes`, `L_tension` et `L_reform` par inclusions exactes de sous-chaînes, et incomplétude de la garde d'arrêt n° 2

Contrairement à l'engagement de la ligne 40 (« trois vocabulaires d'expressions régulières mutuellement disjoints deux à deux »), des inclusions exactes de sous-chaînes subsistent :
1. **Inclusion exacte à bornes de mots entre `L_axes` et `L_tension` (sens 1)** : le motif `unlearning` (`AXE_09`, ligne 74) est une sous-chaîne exacte (même avec bornes de mots `\b`) du motif `superficial unlearning` ($S_4$, ligne 91). La chaîne témoin `"superficial unlearning"` de $\mathcal{L}_{\text{tension}}$ active donc nécessairement $\mathcal{L}_{\text{axes}}$ (`AXE_09`), ce qui déclenchera immédiatement l'arrêt de la garde n° 2 (ligne 155) tout en gonflant mécaniquement $S_4$ sur le sous-domaine du désapprentissage.
2. **Inclusion exacte à bornes de mots entre `L_tension` et `L_axes` (sens 2)** : le motif `post-hoc` ($S_1$, ligne 88) est une sous-chaîne exacte (même avec bornes de mots `\b`, car le trait d'union et l'espace sont des séparateurs non alphanumériques) de `post-hoc rationalization` (`AXE_13`, ligne 78). De même, la variante sans trait d'union `post hoc` ($S_1$) chevauche toute graphie `"post hoc rationalization"`. Toute mention du concept thématique de `AXE_13` incrémente mécaniquement le score de tension $S_1$.
3. **Inclusions sans bornes de mots entre `L_axes` / `L_tension` et `L_reform`** : si les motifs ne sont pas tous encadrés par des bornes de mots strictes `\b...\b`, alors `rmu` (`AXE_09`, ligne 74) est sous-chaîne de `game-theoretic formulation`, `unified formulation`, `reformulation` et `reformulating` ($\mathcal{L}_{\text{reform}}$, lignes 101–102), et `entangles` ($S_5$, ligne 92) est sous-chaîne de `disentangles` ($F_3$, ligne 102).
4. **Trou logique dans la garde d'arrêt n° 2 (ligne 155)** : la formulation actuelle (« détecte qu'une chaîne témoin de $\mathcal{L}_{\text{tension}}$ active $\mathcal{L}_{\text{reform}}$ (ou inversement), ou active $\mathcal{L}_{\text{axes}}$ ») omet **trois des six directions ordonnées** : $\mathcal{L}_{\text{axes}} \to \mathcal{L}_{\text{tension}}$ (qui aurait laissé passer `post-hoc` $\subset$ `post-hoc rationalization` !), $\mathcal{L}_{\text{axes}} \to \mathcal{L}_{\text{reform}}$ et $\mathcal{L}_{\text{reform}} \to \mathcal{L}_{\text{axes}}$.

**Correctif requis** : supprimer ou reformuler les motifs fautifs (retirer `superficial unlearning` de $S_4$, remplacer `post-hoc rationalization` dans `AXE_13` ou restreindre `post-hoc` dans $S_1$ à des syntagmes explicites comme `post-hoc patch` / `post-hoc heuristic` / `post-hoc fix`), encadrer tous les motifs par des bornes de mots explicites, et tester dans la garde n° 2 les **six paires ordonnées** de vocabulaires ainsi que toutes les concaténations chevauchantes d'un à deux mots entre vocabulaires.

---

### Critique 2 (Bloquante) — Collisions par syntagmes chevauchants et endogénéité thématique sévère de `L_tension` et `L_reform` vis-à-vis de certains sous-domaines

Même lorsque deux chaînes témoins prises isolément ne sont pas sous-chaînes l'une de l'autre, un unique syntagme anglais courant dans le corpus active simultanément deux vocabulaires sur les mêmes mots, ou injecte directement le sujet d'un axe dans le prédicteur ou la cible :
1. **Syntagmes chevauchants entre `L_axes` et `L_tension`** :
   - `vulnerable to adaptive` ($S_4$, ligne 91) + `adaptive attack` / `adaptive attacks` (`AXE_15`, ligne 80) fusionnent dans `"vulnerable to adaptive attack(s)"` : tout article d'équipes rouges et d'attaques adaptatives (`AXE_15`) motivant son sujet par cette locution canonique gonfle simultanément son appartenance à `AXE_15` et sa tension $S_4$.
   - `sensitive to prompt` ($S_1$, ligne 88) + `prompt injection` (`AXE_06`, ligne 71) fusionnent dans `"sensitive to prompt injection"` (vulnérabilité de sécurité confondue avec une sensibilité heuristique d'invite ; remplacer dans $S_1$ par `sensitive to prompt wording` / `sensitive to prompt formatting`).
   - `manually tuned` ($S_1$, ligne 88) + `tuned lens` (`AXE_03`, ligne 68) fusionnent potentiellement dans `"manually tuned lens"`.
   - Dans $S_4$ (ligne 91), cinq motifs incorporent directement les lexèmes définitoires de sous-domaines précis : `easily jailbroken` (flexion verbale de `jailbreak` dans `AXE_06` et `AXE_15`), `superficial alignment` (`AXE_07`, `AXE_10` : fusionne dans `"superficial alignment faking"`), `superficial safety` (`AXE_07`, `AXE_11`, `AXE_18` : fusionne dans `"superficial safety classifier"` et `"superficial safety alignment"`), `superficial refusal` (`AXE_06`, `AXE_07` : fusionne dans `"superficial refusal training"` et `"superficial refusal bypass"`), et `superficial unlearning` (`AXE_09`). Ces motifs violent la neutralité inter-axes du détecteur de tension : un article de circuits mécanistes (`AXE_03`) ou d'audit séquentiel (`AXE_16`) n'écrira jamais `"easily jailbroken"` ni `"superficial refusal"`. Il faut purger $S_4$ de tout nom de sous-domaine et ne garder que des marqueurs génériques de fragilité (`superficial fix`, `merely superficial`, `easily bypassed`, `easily circumvented`, `easily evaded`, `easily undone`, `easily reversed`, etc.).
   - Dans $S_2$ (ligne 89), `poor generalization`, `fails to generalize` et `out-of-distribution degradation` / `ood degradation` recoupent fortement le thème même de `AXE_17` (`domain generalization`, `domain shift`, `covariate shift`, ligne 82).
2. **Syntagmes chevauchants entre `L_axes` et `L_reform`** :
   - `invariant representation` et `canonical representation` ($F_3$, ligne 102) fusionnent avec `representation engineering` et `representation rerouting` (`AXE_04`, ligne 69) dans `"invariant representation engineering"`, et partagent la racine thématique centrale de `AXE_01` (`internal representations of truth`) et `AXE_04`.
   - `paradigm shift` ($F_3$, ligne 102) partage `shift` avec `domain shift` / `covariate shift` (`AXE_17`).
   - Colinéarité disciplinaire entre `AXE_16` (ligne 81 : `anytime-valid`, `e-value`, `test martingale`, `confidence sequence`) et $F_2$ (ligne 101 : `neyman-pearson`, `finite-sample guarantee`, `minimax`) : dans la littérature de test séquentiel et de prédiction conforme (`AXE_16`, `AXE_17`), `neyman-pearson` et `finite-sample guarantee` (souvent `"finite-sample anytime-valid guarantee"`) constituent le vocabulaire descriptif ordinaire dès $t \le 2024$ et non un marqueur de percée propre à `2025–2026`.
3. **Syntagmes chevauchants entre `L_tension` et `L_reform`** :
   - `we prove that no` ($F_2$, ligne 101) + `no guarantee` / `no guarantees` / `no consensus` / `no standard definition` ($S_3, S_4, S_5$, lignes 90–92) fusionnent dans `"we prove that no guarantee..."`, activant simultanément tension et reformulation sur la même proposition ! De plus, `no guarantee` ($S_4$) et `finite-sample guarantee` ($F_2$) partagent le substantif pivot `guarantee`.

**Correctif requis** : interdire tout partage de substantif ou d'adjectif technique thématique entre $\mathcal{L}_{\text{axes}}$ et $(\mathcal{L}_{\text{tension}}, \mathcal{L}_{\text{reform}})$, et vérifier par programme qu'aucune paire `(motif_A, motif_B)` issue de vocabulaires distincts ne possède un recouvrement suffixe-préfixe de jetons (`mots(A)[-k:] == mots(B)[:k]`).

---

### Critique 3 (Majeure) — Règles de comptage d'occurrences non spécifiées, doubles comptages internes/inter-axes et biais de couverture du filtre d'éligibilité

1. **Absence de règle formelle de correspondance et doubles comptages internes** : le texte ne précise pas si le comptage d'une liste de motifs s'effectue par somme des occurrences de chaque motif pris séparément ou par balayage sans chevauchement d'une unique expression régulière d'union triée par longueur décroissante. Or l'inventaire révèle **26 inclusions internes dans `L_axes`**, **8 inclusions internes dans `L_tension`**, **1 inclusion croisée entre $S_1$ et $S_4$** (`brittle hyperparameter` dans $S_1$ active aussi `brittle` dans $S_4$), et **3 inclusions internes dans `L_reform`** (`non-identifiability` active `\bidentifiability\b`).
2. **Quatre inclusions croisées entre axes distincts de `L_axes`** : `recursive reward modeling` (`AXE_12`) contient `reward model` et `reward modeling` (`AXE_05`) ; `automated jailbreak` (`AXE_15`) contient `jailbreak` (`AXE_06`) ; `undetectable backdoor` (`AXE_14`) contient `backdoor` (`AXE_08`).
3. **Défauts du filtre d'éligibilité (lignes 58–60)** : retirer `ai control` et `ai safety` de la liste *Modèles d'apprentissage* (ligne 58), encadrer tous les termes par `\b...\b`, et couvrir explicitement les marqueurs de `AXE_16` et `AXE_17` dans la ligne 59.

---

### Critique 4 (Bloquante) — Expression régulière défectueuse dans $F_1(d')$ et destruction des mots composés et syntagmes multi-mots par le prétraitement de `pdftotext`

1. **Bogue avéré sur les preuves dans $F_1(d')$ (ligne 100)** : corriger en `\bProof(?:\s+of\s+(?:Theorem|Proposition|Lemma|Corollary)(?:\s+[A-Z]?\d+(?:\.\d+)*)?)?\s*[.:]` évalué avec respect de la casse, et `\d+(?:\.\d+)*` pour les énoncés.
2. **Destruction des traits d'union légitimes et oubli des sauts de ligne simples (ligne 50)** : découper d'abord `corps_principal` sur le texte multi-lignes, puis normaliser les sauts de ligne en espaces et compiler tout trait d'union interne en `[- ]?`.

---

### Critique 5 (Majeure) — Ambiguïtés algébriques dans la pondération de $F_3(d')$ et dans le départage des ex-aequo d'assignation exclusive $k^*(d)$

Écrire l'équation explicite de $F_3(d')$ en fonction de $W(d')$, et fixer une règle déterministe de départage de $\arg\max_k$ non biaisée par l'indice $k$.

---

## Volet II — Rigueur statistique, cas limites dégénérés et définitions manquantes

### Critique 6 (Bloquante) — Témoin nul « doit mourir » condamné à échouer à tort sous support discret

Remplacer « taux de fausses découvertes » par « taux empirique d'erreur de première espèce », faire porter le contrôle sur $p_{\text{perm}}(\rho_S) \le 0,05$ avec une borne supérieure `<= 0,070` (sans borne inférieure incompatible avec un support discret ou des ex-aequo), et élargir l'intervalle de l'aire sous la courbe moyenne sous le nul à `[0,47 ; 0,53]`.

### Critique 7 (Bloquante) — Inflation du risque de première espèce par l'union « $p_{\text{perm}} \le 0,05$ ou $p_{\text{Fisher}} \le 0,05$ »

Retenir un unique test inferentiel primaire ($p_{\text{perm}}(\rho_S) \le 0,05$ avec formule $(1 + \#\{\rho_S^{(b)} \ge \rho_S^{\text{obs}}\}) / 10\,001$) et conserver le test exact de Fisher unilatéral supérieur (`greater`, sans correction de Yates) et le rapport de cotes empirique régularisé de Haldane-Anscombe à titre descriptif secondaire.

### Critique 8 (Bloquante) — Cas limites dégénérés ($\sigma_m = 0$, $\tau_j = 0$, amas à $Q_{0,75}(R)$, effondrement de $Z_k$ à la médiane et strate singleton)

Spécifier `ddof=0` et mise à `0,0` si écart type nul (avec garde si dégénérescence massive), imposer $F_1 + F_2 + F_3 > 0$ pour $\text{Percee}(d') = 1$, basculer vers $\ge \text{médiane}$ si un plateau annule $\sum \mathbb{I}[Y > \text{médiane}]$ (et `NON CONCLUANT` si $Y^{\text{taux}}$ est constant), et préciser le rééchantillonnage avec remise par percentiles `2,5 %`–`97,5 %`.

### Critique 9 (Bloquante) — Absence de formules mathématiques pour l'analyse dyadique et absence de contrôle des confondants dans le test de Mantel

Définir explicitement $X_{k\ell}$, $C_{k\ell}^{\le 2024}$, $Y_{k\ell}^{\text{pont}}$ et $Z_{k\ell}^{\text{pont}}$ dans la section Métrique, et faire porter la permutation des sommets sur la corrélation partielle des rangs dyadiques contrôlant $(\ln(V_k V_\ell), C_{k\ell}^{\le 2024})$.

### Critique 10 (Majeure) — Spécification de $\rho_{S,\text{partiel}}$, définition de $Y_k^{\text{taux}, \le 2024}$ et permutation au niveau des articles aval

Fixer la formule par moindres carrés ordinaires sur les rangs moyens pour $\rho_{S,\text{partiel}}$, définir explicitement $Y_k^{\text{taux}, \le 2024}$ sans fuite aval, et ajouter un test de permutation au niveau des articles aval $d'$ préservant la structure de recouvrement multi-axes.

---

## Volet III — Étanchéité temporelle, chantier `C3` et conformité R1/R2 et stylistique

### Critique 11 (Majeure) — Fuite temporelle potentielle dans l'extraction du millésime et les révisions post-2024

Prendre le maximum (et non le premier) des millésimes `1980`–`2026` dans l'en-tête hors mentions prospectives, exclure dès l'épreuve primaire les fichiers $t \le 2024$ portant une date de révision explicite en `2025` ou `2026` (hors identifiants `arXiv:\d{4}\.\d{4,5}`), et préciser le rang des fichiers sans suffixe `vK`.

### Critique 12 (Modérée) — Contrôle d'âge des concepts (`C3`), périmètre de centrage-réduction et règle `R6` sur le chiffre `912`

Intégrer $A_k = 2024 - \bar{t}_k^{\le 2024}$ aux seuils/contrôles, clarifier le périmètre des articles éligibles et de la garde n° 3, et retirer le chiffre non empreinté `912` au profit du renvoi au manifeste d'inventaire.

### Critique 13 (Majeure) — Conformité stylistique et structurelle à `src/controle_ia/prereg.py`

Remplacer tous les sigles et anglicismes nus ($\text{AUC}_{\text{ROC}} \to A(X, Z)$, $\text{FE}_{50\%} \to E_{50\%}$, `PDF`, `UTF-8`, `bootstrap`, `jackknife`), placer un groupe nominal explicite devant chaque identifiant entre parenthèses, mettre à jour le commit de tête du dépôt, et renseigner `- **Contre-lecture 1**` avec les deux empreintes hexadécimales à 64 caractères.
