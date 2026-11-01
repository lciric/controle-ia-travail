# Spécification formelle de la statistique décisive et des règles de lecture — course de convergence des règles de défense et sa réplication — v1

Sous-agent neuf (Claude Opus 5.5), 1er novembre 2026, ≈ 21:30 UTC. Document destiné à un implémenteur neuf qui **ne voit pas le code** de la course : il doit pouvoir recoder, à partir de ce seul texte, la statistique décisive, les classes et les verdicts, et retrouver au bit près (écart ≤ 10⁻⁹) l'analyse scellée de la course originale. Aucun code ici ; seuls des objets mathématiques, des formats de fichiers et, pour le générateur pseudo-aléatoire, la référence à l'algorithme publié de numpy, assortie de vecteurs d'essai. En cas d'écart entre ce document et le préenregistrement de réplication une fois scellé, **le texte scellé fait foi** ; ce document en reprend les tables mot pour mot.

Vérification faite par l'auteur : une recodification écrite d'après cette spécification, sans importer le code de la course, rend l'analyse scellée `analyse-regles-defense.json` (`18b80112…`) avec un **écart maximal de 0,0** sur les moyennes, écarts-types et dix quantiles des 16 contrastes × 2 budgets (§ 12).

## 1. Objet et vocabulaire

- **Tâche** : un couple (budget, instance) ; budget codé c ∈ {1, 2} (c = 1 : δ = 1,4 ; c = 2 : δ = 1,6) ; instance i ∈ {0, 1, …, 99}.
- **Variante** k, avec son **rang** r(k) et son **nom** exact dans les fichiers :

| Variante | Surnom | Rang r(k) | Nom exact dans les fichiers |
|---|---|---|---|
| R0 | défense figée | 0 | `R0` |
| R1 | dernière attaque | 1 | `R1` |
| R2 | historique (référence de tous les contrastes) | 2 | `R2` |
| R3 | mélange d'équilibre | 3 | `R3` |
| R4 | régularisation vers le passé | 4 | `R4[moyenne,λ=0.3]` (λ = lettre grecque U+03BB) |

- **Mesure** M, avec son **code** j(M) et son champ :

| Mesure | Code j | Champ (par tâche et par variante) | Sens d'un contraste positif |
|---|---|---|---|
| V, détection finale | 0 | `V_iii_final` | la variante détecte mieux que R2 |
| (ii), détection sur les lois tenues à l'écart | 1 | `ii_final` | la variante détecte mieux |
| X, exploitabilité finale (= 1 − V) | 2 | `exploitabilite_finale` | la variante est plus exploitable |
| X̄, exploitabilité moyenne au fil des tours | 8 | `exploitabilite_moyenne_tours` | la variante est plus exploitable |

- **Contraste** (k, M) à budget c : différence appariée par instance « variante k moins R2 » sur la mesure M. Son **libellé** dans les fichiers d'analyse est la chaîne `<nom de k> - R2 (<champ de M>)`, par exemple `R3 - R2 (V_iii_final)`.

## 2. Constantes

| Symbole | Valeur | Rôle |
|---|---|---|
| n | 100 | instances par budget (garde : exactement 100) |
| B | 20 000 | nombre de rééchantillonnages |
| P | (0,003125 ; 0,00625 ; 0,0125 ; 0,025 ; 0,05 ; 0,95 ; 0,975 ; 0,9875 ; 0,99375 ; 0,996875) | niveaux de quantiles, dans cet ordre |
| m | 0,02 | marge d'effet d'intérêt (S1) |
| S5 | 0,02 | tolérance de non-régression sur (ii) |
| α | 0,01 | taux de fausses alertes visé |
| τ | 0,05 | seuil de taille de la réplication de HR1 |
| z* | 2,497705474412374 | quantile 0,99375 de la loi normale centrée réduite (déclencheur d'écart de réplication) |
| ε | 10⁻⁹ | tolérance de concordance entre deux implémentations |

Toutes les constantes décimales sont les nombres binaires64 (norme IEEE 754) les plus proches de leur écriture décimale. Les bornes d'intervalle sont des quantiles du § 5.6 :
- **B2** = [q(0,00625) ; q(0,99375)] ;
- **B8** = [q(0,003125) ; q(0,996875)] ;
- **E8** = [q(0,00625) ; q(0,99375)] (mêmes quantiles que B2 ; rôle différent : équivalence).

## 3. Entrées

Tous les fichiers sont en JSON, codés en UTF-8. **Lecture exacte** : chaque nombre décimal est lu comme le binaire64 qu'il représente (l'écriture est celle de Python, la plus courte qui se relit à l'identique) ; chaque entier est lu **exactement** (les racines de la réplication vont jusqu'à 2⁶⁴ − 1 : un lecteur qui convertit les entiers en binaire64 est faux).

**E1 — fichier de résultats** (`diag/<run>/resultats-regles-defense.json`) : objet à trois clés `run_id`, `manifeste_sha256`, `resultat` ; `resultat` contient `temps` et `resultats`, liste de 200 objets « tâche ». Chaque tâche contient au moins : `code_delta` (1 ou 2), `instance` (entier), `delta` (1.4 ou 1.6), `racine`, `racine_tenue` (entiers), `config_sha256` (chaîne), et `regles`, objet dont les clés sont les cinq noms du § 1, chacune associée à un objet « variante » qui contient au moins : `V_iii_final`, `V_iii_standard`, `V_iii_renforce`, `ii_final`, `exploitabilite_finale`, `exploitabilite_moyenne_tours`, `fpr_final` (nombres) ; `lam` (0.3 pour R4, nul sinon) ; `reference` (« moyenne » pour R4, nul sinon) ; `poids_finaux` (liste de nombres) ; `par_tour`, objet contenant au moins `cos_consecutif` (liste de 8 nombres) et `exploitabilite` (liste de 8 nombres).

**E2 — manifeste du run** (`runs/<run>/manifeste.json`) : on y lit `config.racine` et `config.racine_tenue` (entiers exacts), `config.prereg_sha256`, `config.lambda`, `config.reference`, `config.config.n_instances`, `preenregistrement.sha256`.

**E3 — préenregistrement scellé** : le fichier lui-même (ses octets exacts), pour recalculer son empreinte SHA-256 (§ 4).

**E4 — pièces de la course originale** (pour la validation et pour l'écart de réplication) : résultats `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` (empreinte `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b`) et analyse `…/analyse-regles-defense.json` (`18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42`). Dans l'analyse, sous `resultat`, les clés `"1"` et `"2"` (budgets) contiennent `contrastes_contre_R2`, objet indexé par libellé, chaque entrée portant `moyenne`, `ecart_type`, `n`, `quantiles` (clés `q0.003125`, `q0.00625`, `q0.0125`, `q0.025`, `q0.05`, `q0.95`, `q0.975`, `q0.9875`, `q0.99375`, `q0.996875`) et `zeros_exacts`.

L'implémentation vérifie l'empreinte SHA-256 de chaque fichier lu contre la valeur attendue (pour E4, les deux empreintes ci-dessus ; pour E1, E2 et E3, leur fichier compagnon `<nom>.sha256`, posé à côté, dont le contenu est une ligne « empreinte en 64 chiffres hexadécimaux minuscules, deux espaces, nom du fichier ») ; toute différence : **arrêt, aucune sortie**. Pour E3, l'empreinte du compagnon doit en outre être égale à H recalculé (§ 4) et à `preenregistrement.sha256` du manifeste.

## 4. Règle D — racines de la réplication dérivées de l'empreinte du texte scellé

1. H = empreinte SHA-256 des octets exacts du préenregistrement scellé, écrite en 64 chiffres hexadécimaux minuscules.
2. E = l'entier naturel dont H est l'écriture en base 16 (0 ≤ E < 2²⁵⁶).
3. S = la suite de graines `SeedSequence` de numpy (algorithme publié depuis numpy 1.17 ; version de la course 2.4.6) construite avec l'entropie E et **sans** clé de descendance.
4. (w₀, w₁) = les deux premiers mots de 64 bits non signés de l'état engendré par S (« generate_state » avec deux mots de type entier non signé 64 bits).
5. **Racine principale ρ = w₀ ; racine des lois tenues ρ_t = w₁.**
6. Gardes (chacune : arrêt, aucun repli, aucune autre dérivation) : ρ ≠ ρ_t ; ni ρ ni ρ_t n'appartient à l'ensemble interdit F = {20261201, 20261202, 20266201, 20266202} ∪ [20261000 ; 20269999] (toutes les racines et plages déjà nommées par les arènes v1 à v4 et les règles de défense v1 et v2) ; ni ρ ni ρ_t n'est égal à un des six entiers des vecteurs d'essai ci-dessous.

Vecteurs d'essai (calculés par l'auteur avec numpy 2.4.6 ; **jamais employés comme racines**) :

| H | (ρ, ρ_t) |
|---|---|
| `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` (préenregistrement de la course originale) | (11786724493248295725, 9136419304016434890) |
| soixante-quatre « 0 » | (15793235383387715774, 12390638538380655177) |
| soixante-quatre « f » | (10168828190493638947, 4616211851522120706) |

Contrôle de cohérence : (ρ, ρ_t) recalculés par la règle D doivent être égaux aux entiers lus dans E2 (`config.racine`, `config.racine_tenue`), et égaux aux champs `racine` et `racine_tenue` de chacune des 200 tâches de E1 ; sinon arrêt.

## 5. La statistique d'un contraste

Pour un budget c, une variante k ≠ R2 et une mesure M (code j), avec une racine de rééchantillonnage ρ (pour la réplication : ρ de la règle D ; pour la course originale : 20266201) :

**5.1 Sélection et ordre.** T_c = les tâches de E1 dont `code_delta` = c, **triées par `instance` croissante**. Gardes : |T_c| = n = 100 ; instances égales à 0, 1, …, 99 sans doublon ; chaque tâche contient exactement les cinq noms de variantes (sinon arrêt) ; si le lecteur JSON conserve l'ordre des clés, cet ordre est R0, R1, R2, R3, R4 dans chaque tâche (sinon arrêt). Le rang r(k) est celui du § 1, jamais déduit de l'ordre des clés. On note l = 0, …, n − 1 la position dans cet ordre (ici l = instance).

**5.2 Différences appariées.** d_l = x_l(k, M) − x_l(R2, M), soustraction binaire64, où x_l(k, M) est le champ de M de la variante k dans la tâche de position l. Gardes : chaque x fini ; pour V, (ii), X et X̄, chaque x dans [0 ; 1] à 10⁻¹² près.

**5.3 Estimateur et dispersion.**
- est = (1/n) Σ_{l=0}^{n−1} d_l ;
- s = √( (1/(n − 1)) Σ_l (d_l − est)² ) (écart-type de l'échantillon, dénominateur n − 1) ;
- zéros = nombre de l tels que d_l = 0 exactement (descriptif).

L'ordre de sommation est libre (les écarts d'arrondi, de l'ordre de 10⁻¹⁷, sont très sous ε).

**5.4 Générateur du rééchantillonnage.** code = 200 + 100 × j + r(k). G = le générateur de numpy « Generator » fondé sur le générateur de bits PCG64, initialisé par la suite de graines `SeedSequence` d'entropie ρ et de clé de descendance (c, code, 0, 0, 99) — cinq entiers dans cet ordre. Exemples de codes : R3 sur V → 203 ; R0 sur V → 200 ; R4 sur V → 204 ; R0 sur (ii) → 300 ; R1 sur X̄ → 1001.

**5.5 Indices et moyennes rééchantillonnées.** On tire de G, en **un seul appel**, une matrice I de B lignes et n colonnes d'entiers uniformes dans {0, 1, …, n − 1} (borne haute exclue, entiers signés 64 bits), remplie ligne par ligne (I[0,0], I[0,1], …, I[0,n−1], I[1,0], …) : c'est exactement le résultat de la méthode « integers » de numpy appelée avec la borne basse 0, la borne haute n et la forme (B, n). Pour chaque ligne b : μ_b = (1/n) Σ_{l=0}^{n−1} d_{I[b,l]}.

Vecteurs d'essai du générateur (racine 20266201) : clé (1, 203, 0, 0, 99) : ligne 0, dix premiers indices = 80, 79, 39, 86, 45, 87, 54, 22, 58, 80 ; ligne B − 1, cinq derniers = 56, 63, 4, 66, 85. Clé (2, 200, 0, 0, 99) : ligne 0 = 73, 34, 66, 88, 64, 92, 23, 55, 84, 31 ; ligne B − 1, cinq derniers = 10, 38, 20, 60, 51. Une implémentation qui ne retrouve pas ces indices n'est pas conforme et ne doit pas être employée.

**5.6 Quantiles.** On trie les μ_b par ordre croissant : μ_(0) ≤ μ_(1) ≤ … ≤ μ_(B−1). Pour chaque p de P : h = (B − 1) × p ; f = partie entière de h ; t = h − f ; si f ≥ B − 1, q(p) = μ_(B−1) ; sinon **q(p) = μ_(f) + t × (μ_(f+1) − μ_(f))** (interpolation linéaire, « type 7 » de Hyndman et Fan, méthode par défaut de numpy). Toute écriture algébriquement équivalente est permise (les écarts restent sous ε).

**5.7 Sortie d'un contraste.** {moyenne : est ; ecart_type : s ; n : n ; quantiles : {q0.003125 : q(0,003125), …, q0.996875 : q(0,996875)} ; zeros_exacts : zéros}.

## 6. Contrastes à calculer

Pour c = 1 et c = 2, avec la même racine ρ :
- **décisifs** : (R3, V) pour HR1 ; (R0, V) pour HR0 ; (R4, V) pour HR3 ;
- **secondaire** : (R0, (ii)) ;
- **descriptifs** : (R1, X̄) pour HR2 ; (R1, V), (R3, X̄), (R4, X̄), (R0, X̄), (R1, (ii)), (R3, (ii)), (R4, (ii)), et les quatre contrastes sur X ;
- au total les 16 contrastes « 4 variantes × 4 mesures » : la comparaison avec l'implémentation de référence (§ 11) porte sur les 16 ; l'arrêt pour discordance ne porte que sur les décisifs et le secondaire.

## 7. Contrôles de santé (recalculés depuis E1, par budget c)

Notations : moy_c(k, champ) = moyenne sur les 100 tâches de T_c du champ de la variante k.

- **T2 — trop beau, trop mauvais** (bloque toutes les lectures) : moy_c(k, V) ≥ 0,99 pour une variante ; ou moy_c(k, V) ≤ 2α = 0,02 pour les cinq variantes ; ou est de (R3, V) > 0,30 ; ou |est de (k, X̄)| > 0,30 pour une variante k ∈ {R0, R1, R3, R4}.
- **T3 — mélange dégénéré** (bloque HR1) : nombre de tâches de T_c où le plus grand élément de `poids_finaux` de R3 est ≥ 1 − 10⁻⁹, strictement supérieur à 50.
- **T4 — régularisation dégénérée, S12** (bloque HR3 seulement) : pour chaque tâche, cos_moyen = (1/8) Σ des 8 valeurs de `par_tour.cos_consecutif` de R4 ; déclenché si le nombre de tâches où cos_moyen ≥ 0,999 est strictement supérieur à 50.
- **T5 — optimiseur** (bloque toutes les lectures) : moy_c(k, V_iii_standard) − moy_c(k, V_iii_renforce) > 0,01 pour une variante ; ou, pour une variante k ∈ {R0, R1, R3, R4}, |a − b| > 0,01 avec a = moyenne des (V_iii_standard(k) − V_iii_standard(R2)) et b = moyenne des (V_iii_renforce(k) − V_iii_renforce(R2)) sur T_c.
- **T6 — dérive des fausses alertes** (bloque toutes les lectures) : |moy_c(k, fpr_final) − α| > 0,001 pour une variante.
- **Garde de cohérence de V** (arrêt) : pour chaque tâche et variante, `V_iii_final` = min(`V_iii_standard`, `V_iii_renforce`) exactement.

## 8. Classes (règles gelées de la course originale ; la première condition vraie décide)

Pour un contraste de budget c : est, et les bornes B2, B8, E8 du § 2. « bas » et « haut » désignent les extrémités d'un intervalle. Les inégalités sont strictes sauf « ≥ » écrit.

**Table A — Δ(R3, R2) sur V (HR1, original)**, par budget, puis aux deux budgets :
1. il existe un budget c tel que moy_c(k, V) ≤ 2α pour chacune des cinq variantes k → « non concluant : jeu dégénéré » ;
2. est ≥ m ∧ bas(B2) > 0, aux deux budgets → « HR1 confirmée » ;
3. haut(B2) < 0 dans au moins un budget → « HR1 réfutée » ;
4. sinon → « HR1 non démontrée ».

**Table B — Δ(R_k, R2) sur V, k ∈ {R0, R1, R3, R4}** (signe + : R_k détecte mieux, donc est moins exploitable) :
1. bas(B8) > m → « R_k > R2 » ;
2. haut(B8) < −m → « R2 > R_k » ;
3. bas(E8) > −m ∧ haut(E8) < m → « ≈ » ;
4. bas(B8) > 0 → « R_k ≳ R2 » ;
5. haut(B8) < 0 → « R2 ≳ R_k » ;
6. sinon → « ? ».

**Table B′ — D̄(R_k, R2) sur X̄** (signe + : R_k plus exploitable) :
1. bas(B8) > m → « R2 > R_k » ;
2. haut(B8) < −m → « R_k > R2 » ;
3. bas(E8) > −m ∧ haut(E8) < m → « ≈ » ;
4. bas(B8) > 0 → « R2 ≳ R_k » ;
5. haut(B8) < 0 → « R_k ≳ R2 » ;
6. sinon → « ? ».

**Table C — Δ(R_k, R2) sur (ii), bornes B8, tolérance S5** (numéro de ligne) :
1. haut < −S5 → régression avérée au-delà de la tolérance ;
2. haut < 0 ∧ bas > −S5 → régression démontrée, sous la tolérance ;
3. haut < 0 → régression démontrée, ampleur non tranchée ;
4. bas > 0 → amélioration ;
5. bas > −S5 → sans régression à S5 près ;
6. sinon → imprécis.

**Frontière numérique** : si une quantité comparée à un seuil en est à moins de ε (|x − seuil| ≤ ε), la classe est marquée « à la frontière » ; deux implémentations peuvent alors légitimement diverger sur cette classe ; la classe retenue est celle calculée avec les nombres de l'implémentation de référence (A), et la lecture le signale.

## 9. Verdicts de la course originale (pour la validation sur E4 seulement)

Contrôles T2, T3, T5, T6 supposés non déclenchés (ils ne le sont pas dans la course originale, § 12) ; déclencheurs d'audit de la course originale **ignorés** (leur audit a conclu « pas d'artefact »).
- **HR1** (« le mélange bat l'historique ») : verdict de la Table A.
- **HR0** (« réentraîner vaut mieux que ne rien faire ») : classes de (R0, V) par la Table B : « confirmée » si « R2 > R0 » aux deux budgets ; sinon « réfutée » si « R0 > R2 », « R0 ≳ R2 » ou « ≈ » dans au moins un budget ; sinon « non tranchée ».
- **HR3** (« la régularisation ne nuit pas ») : si T4 dans au moins un budget → « sans verdict (R4 ≈ défense figée) » ; sinon « confirmée » si la classe de (R4, V) est « R4 > R2 », « R4 ≳ R2 » ou « ≈ » aux deux budgets ; sinon « réfutée » si « R2 > R4 » dans au moins un budget ; sinon « non tranchée ».
- **HR2** (« oublier coûte », descriptif ici) : classes de (R1, X̄) par la Table B′ : « confirmée » si « R2 > R1 » aux deux budgets ; sinon « réfutée » si « R1 > R2 », « R1 ≳ R2 » ou « ≈ » dans au moins un budget ; sinon « non tranchée ».

## 10. Règles de la réplication (copie des « Critères de lecture gelés » du préenregistrement de réplication)

**10.1 Verdicts bruts** (calculés sur E1 de la réplication, racine ρ de la règle D ; la première ligne vraie décide).

*HR1 répliquée ?* — pour chaque budget c : est_c, bas_c = bas(B2), haut_c = haut(B2) de (R3, V) :
1. T2, T3, T5 ou T6 déclenché → « non jugeable (santé) » ;
2. il existe un budget c tel que moy_c(k, V) ≤ 2α pour chacune des cinq variantes k → « non jugeable (jeu dégénéré) » ;
3. aux deux budgets : est_c ≥ τ ∧ bas_c > 0 → **« répliquée »** ;
4. dans au moins un budget : haut_c < 0 → **« non répliquée (signe inversé) »** ;
5. dans au moins un budget : haut_c < τ → **« non répliquée (effet démontré inférieur à 0,05) »** ;
6. sinon → **« non jugeable (imprécis) »**.

*HR0 répliquée ?* — pour chaque budget c : κ_c = classe de (R0, V) par la Table B :
1. T2, T5 ou T6 déclenché → « non jugeable (santé) » ;
2. dans au moins un budget : κ_c = « R2 > R0 » → **« non répliquée (le réentraînement l'emporte d'un effet d'intérêt) »** ;
3. dans au moins un budget : κ_c = « R2 ≳ R0 » → **« non répliquée (le réentraînement l'emporte, effet démontré non nul) »** ;
4. aux deux budgets : κ_c ∈ {« ≈ », « R0 ≳ R2 », « R0 > R2 »} → **« répliquée »** ;
5. sinon → **« non jugeable (imprécis) »**.

*HR3 répliquée ?* (secondaire) — κ′_c = classe de (R4, V) par la Table B :
1. T2, T5 ou T6 → « non jugeable (santé) » ;
2. T4 dans au moins un budget → « sans verdict (R4 ≈ défense figée) » ;
3. dans au moins un budget : κ′_c ∈ {« R2 > R4 », « R2 ≳ R4 »} → « non répliquée » ;
4. aux deux budgets : κ′_c ∈ {« R4 > R2 », « R4 ≳ R2 », « ≈ »} → « répliquée » ;
5. sinon → « non jugeable (imprécis) ».

*Lois tenues à l'écart, défense figée mieux que l'historique ?* (secondaire) — ℓ_c = ligne de la Table C pour (R0, (ii)) :
1. T2, T5 ou T6 → « non jugeable (santé) » ;
2. aux deux budgets : ℓ_c = 4 → « répliquée » ;
3. dans au moins un budget : ℓ_c ∈ {1, 2, 3} → « non répliquée (signe inversé) » ;
4. sinon → « non jugeable (imprécis) ».

*HR2* : classes de (R1, X̄) par la Table B′ et verdict du § 9 recopiés, **sans verdict de réplication**.

**10.2 Écart de réplication et déclencheurs d'audit symétriques (règle R4).** Pour chacun des quatre contrastes primaires π ∈ {(R3, V, c = 1), (R3, V, c = 2), (R0, V, c = 1), (R0, V, c = 2)} : est_rep, s_rep de la réplication ; est_or, s_or lus dans l'analyse originale (E4) ;
g_π = est_rep − est_or ; σ_π = √(s_rep²/100 + s_or²/100) ; z_π = g_π / σ_π.
- **TR1 — écart de réplication, dans les deux sens** : |g_π| > z* × σ_π pour au moins un π (un résultat **plus beau** que l'original déclenche comme un résultat plus faible) ;
- **TR2 — trop propre** : |g_π| < 0,001 pour les quatre π ;
- **TR3 — défense figée plus belle que l'original** : κ_c ∈ {« R0 > R2 », « R0 ≳ R2 »} dans au moins un budget ;
- **TR4 — non-réplication** : verdict brut de HR1 ou de HR0 commençant par « non répliquée ».
Effet : si au moins un de TR1 à TR4 est déclenché, les verdicts de HR1, HR0, HR3 et du secondaire (ii) deviennent « non jugeable (audit en attente) » jusqu'au rapport scellé de l'audit ; « pas d'artefact » → verdicts bruts rétablis (avec la mention « après audit ») ; « artefact trouvé » → « non jugeable (artefact) ».

**10.3 Contrôle « graines neuves »** (liste d'arrêt, pas un audit) : pour chaque variante k, compter les tâches (c, i) où `V_iii_final` de la réplication est **égal au bit** à celui de la course originale à la même tâche ; si un compte dépasse 10 (5 % des 200 tâches) → **arrêt** (« graines non neuves »).

**10.4 Issue globale** (première ligne vraie) :
1. plomberie fausse (V0 de la réplication), arrêt, ou discordance A/B (§ 11) → « non jugeable (plomberie) » ;
2. HR1 ou HR0 « non jugeable (audit en attente) » → « en attente d'audit » ;
3. HR1 ou HR0 « non jugeable (artefact) » → « non jugeable (artefact) » ;
4. HR1 « non répliquée (…) » → « échec de réplication du résultat positif » ;
5. HR1 « répliquée » ∧ HR0 « répliquée » → « réplication réussie » ;
6. HR1 « répliquée » ∧ HR0 « non répliquée (…) » → « réplication partielle : le mélange tient, l'équivalence de la défense figée ne tient pas » ;
7. HR1 « répliquée » ∧ HR0 « non jugeable (…) » → « réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise » ;
8. sinon → « non jugeable ».

## 11. Sorties et comparaison avec l'implémentation de référence

**Sortie de l'implémentation** : un fichier JSON neuf (jamais écrasé) contenant : l'empreinte H et (ρ, ρ_t) en **chaînes** décimales ; pour `"1"` et `"2"`, l'objet `contrastes_contre_R2` indexé par libellé (format du § 5.7) ; les classes des Tables A, B, B′, C ; les valeurs des contrôles T2 à T6 et leur état ; les verdicts bruts du § 10.1 ; g_π, σ_π, z_π et l'état de TR1 à TR4 ; les comptes du § 10.3 ; l'issue globale brute ; les empreintes de tous les fichiers lus.

**Implémentation de référence A** : l'analyse écrite par le code de la course (`diag/<run>/analyse-regles-defense.json`, mêmes libellés et mêmes champs) ; classes et verdicts de A = ceux que le lecteur neuf (R13) calcule à partir des nombres de A en appliquant le texte scellé.

**Concordance exigée** :
- pour les quatre contrastes décisifs et secondaire × 2 budgets — (R3, V), (R0, V), (R4, V), (R0, (ii)) — et pour le descriptif (R1, X̄) : |moyenne_A − moyenne_B|, |écart-type_A − écart-type_B| et, pour chacun des dix niveaux, |q_A − q_B| **≤ ε = 10⁻⁹** ; de même |z_π(A) − z_π(B)| ≤ 10⁻⁹ ;
- classes, lignes de table, états des contrôles et verdicts bruts **identiques**, sauf classe marquée « à la frontière » (§ 8) ;
- sinon : **arrêt**, aucune lecture, consignation ; le diagnostic est confié à un sous-agent neuf ; toute correction d'une implémentation après lecture des résultats de la réplication est un écart au préenregistrement (nœud de décision pour Lazar).
- Les 11 autres contrastes : même tolérance, mais une discordance y est une **alerte** consignée, pas un arrêt.

## 12. Vecteurs d'essai sur la course originale (validation obligatoire avant tout emploi)

L'implémentation appliquée à E4 (résultats originaux), avec ρ = 20266201, doit rendre l'analyse originale à ε près pour les 16 contrastes × 2 budgets. Valeurs de contrôle (écriture décimale complète, telle que lue dans l'analyse scellée `18b80112…`) :

| Budget | Contraste | moyenne | écart-type | q(0,003125) | q(0,00625) | q(0,99375) | q(0,996875) |
|---|---|---|---|---|---|---|---|
| 1 | R3 − R2, V | 0.10448042252007811 | 0.05656582805294246 | 0.08961294692052145 | 0.09061967064630756 | 0.11847919936691555 | 0.1195334438923409 |
| 1 | R0 − R2, V | 0.002372737273727372 | 0.0437743214432734 | −0.009994891676667669 | −0.00881441894189419 | 0.013423389213921407 | 0.014486709608460841 |
| 1 | R4 − R2, V | 0.0201960196019602 | 0.04239267589358395 | 0.010168702807780781 | 0.010856548154815484 | 0.031763698244824494 | 0.033126912691269106 |
| 1 | R0 − R2, (ii) | 0.05159014753688421 | 0.06098120554786593 | 0.03629339475493873 | 0.03746680951487873 | 0.06743716460365097 | 0.06881969804951228 |
| 1 | R1 − R2, X̄ | 0.026169991999199924 | 0.023547075573731077 | 0.020106790171204626 | 0.020531546123362335 | 0.032298407184468476 | 0.03288676562968797 |
| 2 | R3 − R2, V | 0.12355560350045353 | 0.042688591197885796 | 0.11167459572805016 | 0.1127024328599859 | 0.13408309749193276 | 0.13491261731301288 |
| 2 | R0 − R2, V | 0.003718371837183717 | 0.0383691164326799 | −0.00656942100460046 | −0.005623565481548155 | 0.013332498874887548 | 0.014550762888788865 |
| 2 | R4 − R2, V | 0.014203420342034203 | 0.03305933727569008 | 0.006422642264226423 | 0.006941184743474348 | 0.0231068294329433 | 0.023962247787278703 |
| 2 | R0 − R2, (ii) | 0.059960640160040005 | 0.06029064838824576 | 0.043867641754188544 | 0.045420316329082264 | 0.07563060796449118 | 0.0770858519317329 |
| 2 | R1 − R2, X̄ | 0.016226997699769964 | 0.018280298925448104 | 0.011546889454570441 | 0.011899875534428422 | 0.020956909753475347 | 0.021426363339458934 |

Classes et verdicts attendus sur la course originale :
- Table A : ligne « HR1 confirmée » (est ≥ 0,02 et bas(B2) > 0 aux deux budgets) ;
- Table B : R0 « ≈ » et « ≈ » ; R1 « R2 ≳ R1 » et « ? » ; R3 « R3 > R2 » et « R3 > R2 » ; R4 « R4 ≳ R2 » et « R4 ≳ R2 » ;
- Table B′ : R0 « ≈ » et « ≈ » ; R1 « R2 > R1 » et « R2 ≳ R1 » ; R3 « R3 > R2 » et « R3 > R2 » ; R4 « R4 ≳ R2 » et « R4 ≳ R2 » ;
- Table C : R0 ligne 4 et 4 ; R1 ligne 4 et 4 ; R3 ligne 1 et 1 ; R4 ligne 4 et 4 ;
- contrôles : T2 non ; T3 non (aucune tâche à poids pur) ; T4 non (5 et 2 tâches sur 100 à cos_moyen ≥ 0,999) ; T5 non (plus grand écart standard − renforcé 0,00039, plus grand écart de contraste 0,00043) ; T6 non (plus grand écart à α 0,00019) ;
- verdicts du § 9 : **HR1 confirmée ; HR0 réfutée ; HR3 confirmée ; HR2 non tranchée**.

Essai des gardes de la réplication (cas « artefact », R5) : appliquer le § 10 à la course originale **contre elle-même** (E1 = résultats originaux, E4 = résultats et analyse originaux, ρ = 20266201 imposé) doit rendre g_π = 0 pour les quatre π, donc **TR2 déclenché**, et les comptes du § 10.3 égaux à 200 pour chaque variante, donc **arrêt « graines non neuves »**. Cas sain : la règle D appliquée à l'empreinte du texte original rend (11786724493248295725, 9136419304016434890), différent de (20266201, 20266202).

## 13. Arrondis, affichage, ce qui n'est pas spécifié

- Aucun arrondi dans les calculs ; toutes les comparaisons aux seuils portent sur les binaires64 non arrondis. L'affichage dans les documents se fait à 4 décimales (6 pour les bornes proches d'un seuil), sans effet sur aucune classe.
- La méthode de calcul de la moyenne, de l'écart-type et du tri est libre ; le générateur (§ 5.4) et l'ordre de remplissage de I (§ 5.5) ne le sont pas.
- Hors de cette spécification : la production des valeurs par tâche (le jeu, l'attaquant, l'oracle, la finale) ; elles sont les entrées.
