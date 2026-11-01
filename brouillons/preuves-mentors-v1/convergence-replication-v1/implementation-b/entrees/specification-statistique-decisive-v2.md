# Spécification formelle de la statistique décisive et des règles de lecture — course de convergence des règles de défense et sa réplication — v2

Version 2, écrite le 1er novembre 2026 (≈ 22:15 UTC) par un sous-agent de la session principale (Claude Opus 5.5), qui n'a écrit ni la v1 de ce texte, ni le code de la course (v2 ou v3), ni l'implémentation indépendante B, et qui n'a ouvert de B que son rapport de validation (`implementation-b/validation-b-v1.md`). La v1 (`specification-statistique-decisive-v1.md`, `2a1ad6d356ab60d44aebbf8d92ee9ba932bd24f925ae4fb86538545e0706e0e5`) reste archivée sans modification (R12).

Document destiné à un implémenteur qui **ne voit pas le code** de la course : il doit pouvoir recoder, à partir de ce seul texte, la statistique décisive, les contrôles, les classes et les verdicts, et retrouver au bit près (écart ≤ 10⁻⁹) l'analyse scellée de la course originale. Aucun code ici ; seulement des objets mathématiques, des formats de fichiers et, pour le générateur pseudo-aléatoire, la référence à l'algorithme publié de numpy avec des vecteurs d'essai. En cas d'écart entre ce document et le préenregistrement de réplication une fois scellé, **le texte scellé fait foi** ; ce document en reprend les tables mot pour mot.

## 0. Ce qui change par rapport à la v1, et ce que B doit changer

La v1 a été implémentée par B (implémentation indépendante, validée au bit sur la course originale : écart 0 sur 32 contrastes, classes et verdicts identiques). B a relevé quinze ambiguïtés ; la contre-lecture 1 du préenregistrement en a relevé une incohérence (CL-10). La v2 les tranche **en gardant la lecture de B chaque fois qu'elle est raisonnable**, pour ne pas invalider une implémentation validée. Aucune formule de la statistique (§ 5), aucune constante (§ 2), aucune classe (§ 8) ni aucun verdict (§ 9, § 10.1) ne change : les valeurs du § 12 restent exactes.

Colonne « B » : **non** = la lecture de B est retenue, rien à changer (à confirmer dans le rapport v2 de B) ; **oui** = B doit changer ; **à confirmer** = B dit dans son rapport v2 s'il le faisait déjà, et s'aligne sinon.

| # | Point (relevé par B ou par la contre-lecture) | Décision v2 | Où | B |
|---|---|---|---|---|
| 1 | Contrôles T2, T3, T5, T6 « déclenchés » par budget ou globalement | Chaque contrôle est évalué **par budget** ; il est **déclenché** s'il l'est dans **au moins un budget** (lecture de B). Les états par budget sont écrits dans la sortie. | § 7 | non |
| 2 | Ligne 2 du verdict « HR1 répliquée ? » inatteignable | Constat exact : sa condition fait partie de T2, testé à la ligne 1. La ligne est **gardée** (correspondance mot pour mot avec la Table A originale) et **déclarée inatteignable** ; l'ordre des lignes est obligatoire ; aucun essai ne doit l'atteindre, un essai doit montrer qu'une entrée qui la remplit rend « non jugeable (santé) ». | § 10.1 | non |
| 3 | « Issue globale brute » : avant ou après les déclencheurs d'audit | **Les deux** sont rendues (lecture de B) : l'issue **brute** applique le § 10.4 aux verdicts bruts du § 10.1 ; l'issue **après déclencheurs** l'applique aux verdicts après l'effet du § 10.2. Avant l'audit, c'est l'issue après déclencheurs qui vaut ; après un audit « pas d'artefact », c'est l'issue brute, avec la mention « après audit ». | § 10.4 | non |
| 4 | « Frontière numérique » : quelles comparaisons comptent | Lecture de B, précisée : comptent **toutes les comparaisons atomiques à un seuil évaluées sur le chemin de décision** (chaque ligne examinée jusqu'à la première vraie comprise, chaque comparaison de chaque ligne examinée **sans court-circuit**, aux deux budgets) ; tolérance **inclusive** \|x − seuil\| ≤ 10⁻⁹ ; une classe, un contrôle ou un verdict **hérite** du drapeau de toute entrée marquée. Ne comptent pas les comparaisons portant sur des valeurs **brutes** lues dans E1 (identiques pour toute implémentation) ni les comptes entiers. | § 8 | à confirmer (court-circuit) |
| 5 | Champs de E2 non vérifiés | Liste fermée de vérifications de E2, chacune un **arrêt** (code 2) : empreinte, rattachement à E1, racines, préenregistrement, λ, référence, N, empreinte de configuration. | § 3 | oui |
| 6 | Nom du fichier compagnon d'empreinte | `<chemin du fichier>.sha256` (nom du fichier suivi de « .sha256 », dans le même dossier), **une seule ligne** : 64 chiffres hexadécimaux minuscules, deux espaces, **nom de base** du fichier, fin de ligne (format de `sha256sum`). Les deux parties sont vérifiées. | § 3 | à confirmer (nom de base) |
| 7 | Fichier de résultats original sans compagnon | Les pièces originales (E4) sont vérifiées par les **empreintes épinglées** du § 3, sans compagnon ; quand les résultats originaux servent de E1 dans les auto-essais du § 12, l'empreinte épinglée remplace le compagnon. | § 3, § 12 | non |
| 8 | « Plomberie fausse (V0) » et « discordance A/B » non calculables depuis les entrées | V0 n'est **pas** évaluée par B : c'est le lecteur (R13) qui l'évalue et applique la ligne 1 du § 10.4. La **discordance A/B est calculée par B** à partir de l'analyse de A (entrée E5, neuve). B rend ses deux issues « sous réserve de V0 », et écrit dans sa sortie la valeur de toute option de ligne de commande qui touche ces lignes. | § 3, § 10.4, § 11 | à confirmer (discordance calculée depuis E5) |
| 9 | Forme de E1 : « contient » | « **Au moins** » (lecture de B) : des clés supplémentaires sont permises (le code v3 ajoute `version`, `serialisation`, `loi_cible` et d'autres) ; l'objet `regles` contient **exactement** les cinq noms. | § 3 | non |
| 10 | « Arrêt, aucune sortie » contre l'auto-essai du § 12 | Lecture de B : **code 2**, aucune sortie, pour tout arrêt d'**entrée** (empreinte, format, garde d'entrée) ; **code 3**, sortie écrite avec `lecture_autorisee: false` et les motifs, pour un arrêt de **contrôle** (graines non neuves, discordance A/B de niveau arrêt) ; **code 0**, sortie écrite avec `lecture_autorisee: true`, sinon. | § 11 | à confirmer (discordance → 3) |
| 11 | T5 : première condition unilatérale, seconde bilatérale | **Gardé tel quel** et rendu explicite : (a) unilatérale (le renforcé détecte plus mal que le standard de plus de 0,01 : l'optimiseur standard est faible) ; (b) bilatérale (le contraste dépend de la force de l'attaquant, dans un sens ou dans l'autre). | § 7 | non |
| 12 | « À 10⁻¹² près » pour [0 ; 1] | −10⁻¹² ≤ x ≤ 1 + 10⁻¹², bornes **incluses**, calculées en binaire64. | § 5.2 | non |
| 13 | Champs documentés non utilisés | Chaque champ de E1 a un emploi écrit : calcul, garde (arrêt) ou présence seule. Gardes neuves : `delta` conforme à `code_delta` ; `config_sha256` identique sur toutes les tâches et égal à l'empreinte épinglée ; `lam` et `reference` conformes. `par_tour.exploitabilite` n'est plus exigé. | § 3 | oui (trois gardes) |
| 14 | L'analyse de A ne contient pas ses contrôles de santé | La concordance des contrôles de santé est exigée entre B et le **recalcul indépendant du lecteur** depuis E1 (états identiques, sinon arrêt). En plus, à titre d'**alerte**, le lecteur les recalcule depuis les champs de l'analyse de A (table de correspondance, § 11.3). | § 11 | non |
| 15 | « 1 − 10⁻⁹ » en flottant | Le seuil de T3 est le binaire64 `0x1.fffffff768fa1p-1`, qui est à la fois le binaire64 le plus proche de 0,999999999 et le résultat de 1 − 10⁻⁹ calculé en binaire64 ; comparaison « ≥ ». | § 7 | non |
| CL-10 | § 6 contre § 11 : contrastes dont la discordance arrête ; seuil et champs de « graines neuves » ; qui et quand | Arrêt pour discordance sur les **cinq** contrastes de concordance exigée (les trois décisifs, le secondaire et (R1, X̄)), les 11 autres en alerte. « Graines non neuves » : **plus de 2 tâches** égales au bit à l'original, pour une variante, sur **V, X̄ ou (ii)** (au lieu de plus de 10 sur V seul) ; calculé par B après la course, avant toute lecture, recompté par le lecteur ; cas sain et artefact au § 12. | § 6, § 10.3 | oui (§ 10.3) |
| — | Environnement (constat de ce rédacteur) | B v1 a été validée avec numpy 2.5.3 ; la course tourne avec numpy 2.4.6. B v2 est validée **et** lancée avec l'interpréteur du dépôt (`/home/claude/controle-ia-travail/.venv/bin/python`, numpy 2.4.6, Python 3.13.18). | § 13 | oui (environnement) |

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
| ε | 10⁻⁹ | tolérance de concordance entre deux implémentations ; largeur de la frontière numérique |
| s_pur | `0x1.fffffff768fa1p-1` | seuil de T3 (= binaire64 le plus proche de 1 − 10⁻⁹ ; point 15) |
| G | 2 | seuil du contrôle « graines neuves » (plus de G tâches égales au bit ; CL-10) |

Toutes les constantes décimales sont les nombres binaires64 (norme IEEE 754) les plus proches de leur écriture décimale. Les bornes d'intervalle sont des quantiles du § 5.6 :
- **B2** = [q(0,00625) ; q(0,99375)] ;
- **B8** = [q(0,003125) ; q(0,996875)] ;
- **E8** = [q(0,00625) ; q(0,99375)] (mêmes quantiles que B2 ; rôle différent : équivalence).

## 3. Entrées

Tous les fichiers sont en JSON, codés en UTF-8, sauf E3 (Markdown, lu en octets). **Lecture exacte** : chaque nombre décimal est lu comme le binaire64 qu'il représente (l'écriture est celle de Python, la plus courte qui se relit à l'identique) ; chaque entier est lu **exactement** (les racines de la réplication vont jusqu'à 2⁶⁴ − 1 : un lecteur qui convertit les entiers en binaire64 est faux). « Contient » veut dire « contient **au moins** » : des clés supplémentaires sont permises partout, sauf dans `regles` (point 9).

**Compagnon d'empreinte (point 6).** Le compagnon d'un fichier `F` est le fichier `F.sha256` (même dossier, nom de `F` suivi de « .sha256 »). Il contient une seule ligne non vide : l'empreinte SHA-256 de `F` en 64 chiffres hexadécimaux minuscules, **deux espaces**, le **nom de base** de `F` (sans dossier), puis une fin de ligne (format de `sha256sum`). Vérifier un compagnon = vérifier les deux parties et recalculer l'empreinte des octets de `F`.

**E1 — fichier de résultats** (`diag/<run>/resultats-regles-defense.json`, avec compagnon) : objet contenant `run_id` (chaîne), `manifeste_sha256` (chaîne) et `resultat` ; `resultat` contient `temps` et `resultats`, liste de 200 objets « tâche ». Chaque tâche contient `code_delta` (1 ou 2), `instance` (entier), `delta` (nombre), `racine`, `racine_tenue` (entiers), `config_sha256` (chaîne), et `regles`, objet dont les clés sont **exactement** les cinq noms du § 1, chacune associée à un objet « variante » qui contient : `V_iii_final`, `V_iii_standard`, `V_iii_renforce`, `ii_final`, `exploitabilite_finale`, `exploitabilite_moyenne_tours`, `fpr_final` (nombres) ; `lam`, `reference` ; `poids_finaux` (liste de nombres) ; `par_tour`, objet contenant `cos_consecutif` (liste de 8 nombres).

Emploi de chaque champ de E1 (point 13) — toute garde est un **arrêt d'entrée** (code 2) :

| Champ | Emploi |
|---|---|
| `code_delta`, `instance` | sélection et ordre (§ 5.1) ; gardes du § 5.1 |
| `delta` | garde : `delta` = 1.4 si `code_delta` = 1, = 1.6 si `code_delta` = 2 (égalité de binaires64) |
| `racine`, `racine_tenue` | garde : égales à (ρ, ρ_t) de la règle D (réplication, § 4) ou à (20266201, 20266202) (course originale) dans chaque tâche |
| `config_sha256` | garde : identique dans les 200 tâches et égal à `3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098` ; en réplication, égal aussi à `config.config_sha256` de E2 |
| `lam`, `reference` | garde : pour `R4[moyenne,λ=0.3]`, `lam` = 0.3 et `reference` = « moyenne » ; pour les quatre autres variantes, les deux sont `null` |
| `V_iii_final`, `ii_final`, `exploitabilite_finale`, `exploitabilite_moyenne_tours` | statistique (§ 5) ; T2 ; graines neuves (§ 10.3, V, (ii) et X̄) |
| `V_iii_standard`, `V_iii_renforce` | T5 ; garde de cohérence de V (§ 7) |
| `fpr_final` | T6 |
| `poids_finaux` | T3 (R3 seulement ; liste non vide exigée pour R3) |
| `par_tour.cos_consecutif` | T4 (R4 seulement ; exactement 8 nombres exigés pour R4) |
| `temps`, `par_tour` (autres clés), toute autre clé | non employés ; présence non exigée (sauf `par_tour.cos_consecutif`) |

**E2 — manifeste du run** (`runs/<run>/manifeste.json`, avec compagnon). Vérifications (point 5), chacune un **arrêt d'entrée** (code 2) :
1. compagnon conforme ; l'empreinte de E2 est égale à `manifeste_sha256` de E1, et `run_id` de E2 est égal à `run_id` de E1 ;
2. `config.racine` et `config.racine_tenue` (entiers exacts) égaux à (ρ, ρ_t) de la règle D appliquée à H (§ 4) ; `config.racine_chaine` et `config.racine_tenue_chaine`, s'ils sont présents, égaux à l'écriture décimale de ρ et ρ_t ;
3. `config.prereg_sha256` = `preenregistrement.sha256` = H (empreinte recalculée de E3) ;
4. `config.lambda` = 0.3 ; `config.reference` = « moyenne » ;
5. `config.config.n_instances` = 100 ; `config.config_sha256` = `3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098`.

**E3 — préenregistrement scellé** (avec compagnon) : ses octets exacts, pour recalculer H (§ 4). L'empreinte du compagnon doit être égale à H recalculé (sinon arrêt d'entrée).

**E4 — pièces de la course originale** (pour la validation et pour l'écart de réplication), vérifiées par leurs **empreintes épinglées**, sans compagnon (point 7) : résultats `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` (`d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b`) et analyse `…/analyse-regles-defense.json` (`18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42`). Dans l'analyse, sous `resultat`, les clés `"1"` et `"2"` (budgets) contiennent `contrastes_contre_R2`, objet indexé par libellé, chaque entrée portant `moyenne`, `ecart_type`, `n`, `quantiles` (clés `q0.003125`, `q0.00625`, `q0.0125`, `q0.025`, `q0.05`, `q0.95`, `q0.975`, `q0.9875`, `q0.99375`, `q0.996875`) et `zeros_exacts`.

**E5 — analyse de l'implémentation de référence A sur la réplication** (`diag/<run>/analyse-regles-defense.json`, avec compagnon ; neuve en v2, point 8) : même format que l'analyse de E4 ; `run_id` égal à celui de E1 et `manifeste_sha256` égal à l'empreinte de E2 (sinon arrêt d'entrée). Sert à la comparaison du § 11 ; B ne la lit qu'**après** avoir calculé et gardé en mémoire sa propre statistique.

Toute différence d'empreinte, tout champ exigé absent, tout format inattendu : **arrêt d'entrée, aucune sortie, code 2**.

## 4. Règle D — racines de la réplication dérivées de l'empreinte du texte scellé

1. H = empreinte SHA-256 des octets exacts du préenregistrement scellé, écrite en 64 chiffres hexadécimaux minuscules.
2. E = l'entier naturel dont H est l'écriture en base 16 (0 ≤ E < 2²⁵⁶).
3. S = la suite de graines `SeedSequence` de numpy (algorithme publié depuis numpy 1.17 ; version de la course 2.4.6) construite avec l'entropie E et **sans** clé de descendance.
4. (w₀, w₁) = les deux premiers mots de 64 bits non signés de l'état engendré par S (« generate_state » avec deux mots de type entier non signé 64 bits).
5. **Racine principale ρ = w₀ ; racine des lois tenues ρ_t = w₁.**
6. Gardes (chacune : arrêt d'entrée, aucun repli, aucune autre dérivation) : ρ ≠ ρ_t ; ni ρ ni ρ_t n'appartient à l'ensemble interdit F = {20261201, 20261202, 20266201, 20266202} ∪ [20261000 ; 20269999] ; ni ρ ni ρ_t n'est égal à un des six entiers des vecteurs d'essai ci-dessous.

Vecteurs d'essai (calculés avec numpy 2.4.6 ; **jamais employés comme racines**) :

| H | (ρ, ρ_t) |
|---|---|
| `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` (préenregistrement de la course originale) | (11786724493248295725, 9136419304016434890) |
| soixante-quatre « 0 » | (15793235383387715774, 12390638538380655177) |
| soixante-quatre « f » | (10168828190493638947, 4616211851522120706) |

Contrôle de cohérence : (ρ, ρ_t) recalculés par la règle D doivent être égaux aux entiers lus dans E2 et dans chacune des 200 tâches de E1 (§ 3) ; sinon arrêt d'entrée.

## 5. La statistique d'un contraste

Pour un budget c, une variante k ≠ R2 et une mesure M (code j), avec une racine de rééchantillonnage ρ (pour la réplication : ρ de la règle D ; pour la course originale : 20266201) :

**5.1 Sélection et ordre.** T_c = les tâches de E1 dont `code_delta` = c, **triées par `instance` croissante**. Gardes : |T_c| = n = 100 ; instances égales à 0, 1, …, 99 sans doublon ; chaque tâche contient exactement les cinq noms de variantes ; si le lecteur JSON conserve l'ordre des clés, cet ordre est R0, R1, R2, R3, R4 dans chaque tâche (sinon arrêt d'entrée). Le rang r(k) est celui du § 1, jamais déduit de l'ordre des clés. On note l = 0, …, n − 1 la position dans cet ordre (ici l = instance).

**5.2 Différences appariées.** d_l = x_l(k, M) − x_l(R2, M), soustraction binaire64, où x_l(k, M) est le champ de M de la variante k dans la tâche de position l. Gardes (arrêt d'entrée) : chaque x fini ; pour V, (ii), X et X̄, chaque x vérifie −10⁻¹² ≤ x ≤ 1 + 10⁻¹², **bornes incluses**, les bornes étant les binaires64 de 10⁻¹² et de 1 + 10⁻¹² (point 12).

**5.3 Estimateur et dispersion.**
- est = (1/n) Σ_{l=0}^{n−1} d_l ;
- s = √( (1/(n − 1)) Σ_l (d_l − est)² ) (écart-type de l'échantillon, dénominateur n − 1) ;
- zéros = nombre de l tels que d_l = 0 exactement (descriptif).

L'ordre de sommation est libre (les écarts d'arrondi, de l'ordre de 10⁻¹⁷, sont très sous ε).

**5.4 Générateur du rééchantillonnage.** code = 200 + 100 × j + r(k). G = le générateur de numpy « Generator » fondé sur le générateur de bits PCG64, initialisé par la suite de graines `SeedSequence` d'entropie ρ et de clé de descendance (c, code, 0, 0, 99) — cinq entiers dans cet ordre. Exemples de codes : R3 sur V → 203 ; R0 sur V → 200 ; R4 sur V → 204 ; R0 sur (ii) → 300 ; R1 sur X̄ → 1001.

**5.5 Indices et moyennes rééchantillonnées.** On tire de G, en **un seul appel**, une matrice I de B lignes et n colonnes d'entiers uniformes dans {0, 1, …, n − 1} (borne haute exclue, entiers signés 64 bits), remplie ligne par ligne : c'est exactement le résultat de la méthode « integers » de numpy appelée avec la borne basse 0, la borne haute n et la forme (B, n). Pour chaque ligne b : μ_b = (1/n) Σ_{l=0}^{n−1} d_{I[b,l]}.

Vecteurs d'essai du générateur (racine 20266201) : clé (1, 203, 0, 0, 99) : ligne 0, dix premiers indices = 80, 79, 39, 86, 45, 87, 54, 22, 58, 80 ; ligne B − 1, cinq derniers = 56, 63, 4, 66, 85. Clé (2, 200, 0, 0, 99) : ligne 0 = 73, 34, 66, 88, 64, 92, 23, 55, 84, 31 ; ligne B − 1, cinq derniers = 10, 38, 20, 60, 51. Une implémentation qui ne retrouve pas ces indices n'est pas conforme et ne doit pas être employée.

**5.6 Quantiles.** On trie les μ_b par ordre croissant : μ_(0) ≤ … ≤ μ_(B−1). Pour chaque p de P : h = (B − 1) × p ; f = partie entière de h ; t = h − f ; si f ≥ B − 1, q(p) = μ_(B−1) ; sinon **q(p) = μ_(f) + t × (μ_(f+1) − μ_(f))** (interpolation linéaire, « type 7 » de Hyndman et Fan, méthode par défaut de numpy). Toute écriture algébriquement équivalente est permise (les écarts restent sous ε).

**5.7 Sortie d'un contraste.** {moyenne : est ; ecart_type : s ; n : n ; quantiles : {q0.003125 : q(0,003125), …, q0.996875 : q(0,996875)} ; zeros_exacts : zéros}.

## 6. Contrastes à calculer

Pour c = 1 et c = 2, avec la même racine ρ :
- **décisifs** : (R3, V) pour HR1 ; (R0, V) pour HR0 ; (R4, V) pour HR3 ;
- **secondaire** : (R0, (ii)) ;
- **descriptifs** : (R1, X̄) pour HR2 ; (R1, V), (R3, X̄), (R4, X̄), (R0, X̄), (R1, (ii)), (R3, (ii)), (R4, (ii)), et les quatre contrastes sur X ;
- au total les 16 contrastes « 4 variantes × 4 mesures » : la comparaison avec l'implémentation de référence (§ 11) porte sur les 16 ; **l'arrêt pour discordance porte sur les cinq contrastes de concordance exigée du § 11 (les trois décisifs, le secondaire et (R1, X̄)) ; les 11 autres donnent une alerte** (CL-10).

## 7. Contrôles de santé (recalculés depuis E1, par budget c)

Notations : moy_c(k, champ) = moyenne sur les 100 tâches de T_c du champ de la variante k. **Chaque contrôle est évalué par budget ; il est déclenché s'il l'est dans au moins un budget** (point 1). La sortie donne, par budget, la valeur comparée et l'état.

- **T2 — trop beau, trop mauvais** (bloque toutes les lectures) : moy_c(k, V) ≥ 0,99 pour une variante ; ou moy_c(k, V) ≤ 2α = 0,02 pour les cinq variantes ; ou est de (R3, V) > 0,30 ; ou |est de (k, X̄)| > 0,30 pour une variante k ∈ {R0, R1, R3, R4}.
- **T3 — mélange dégénéré** (bloque HR1) : nombre de tâches de T_c où le plus grand élément de `poids_finaux` de R3 est ≥ s_pur (§ 2, point 15), strictement supérieur à 50.
- **T4 — régularisation dégénérée, S12** (bloque HR3 seulement) : pour chaque tâche, cos_moyen = (1/8) Σ des 8 valeurs de `par_tour.cos_consecutif` de R4 ; déclenché si le nombre de tâches où cos_moyen ≥ 0,999 est strictement supérieur à 50.
- **T5 — optimiseur** (bloque toutes les lectures ; point 11) : (a) **unilatérale** : moy_c(k, V_iii_standard) − moy_c(k, V_iii_renforce) > 0,01 pour une variante k (l'attaquant renforcé trouve nettement mieux que le standard : le standard est faible) ; ou (b) **bilatérale** : pour une variante k ∈ {R0, R1, R3, R4}, |a − b| > 0,01 avec a = moyenne des (V_iii_standard(k) − V_iii_standard(R2)) et b = moyenne des (V_iii_renforce(k) − V_iii_renforce(R2)) sur T_c (le contraste dépend de la force de l'attaquant, dans un sens ou dans l'autre).
- **T6 — dérive des fausses alertes** (bloque toutes les lectures) : |moy_c(k, fpr_final) − α| > 0,001 pour une variante.
- **Garde de cohérence de V** (arrêt d'entrée) : pour chaque tâche et variante, `V_iii_final` = min(`V_iii_standard`, `V_iii_renforce`) exactement.

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

**Frontière numérique** (point 4). Une comparaison atomique « x op seuil » (op ∈ {<, >, ≥, ≤}) est **à la frontière** si |x − seuil| ≤ ε (inclusif). Comptent toutes les comparaisons atomiques du **chemin de décision** : pour chaque table, contrôle, verdict ou déclencheur, chaque ligne examinée dans l'ordre jusqu'à la première ligne vraie comprise, et dans chaque ligne examinée **toutes** ses comparaisons atomiques (sans court-circuit, aux deux budgets quand la ligne porte sur les deux). Sont exclues : les comparaisons portant sur une valeur **brute** de E1, sans aucune opération arithmétique (identiques pour toute implémentation : la comparaison du plus grand poids de chaque tâche à s_pur, l'égalité au bit du § 10.3), et les comparaisons d'entiers (comptes de T3, T4, § 10.3). En revanche, cos_moyen (T4) est une moyenne calculée, dont le dernier bit peut dépendre de l'ordre de sommation : la comparaison de chaque cos_moyen à 0,999 **compte** (si une tâche est à la frontière, T4 est marqué). Une classe, une ligne, un état de contrôle ou un déclencheur dont une comparaison est à la frontière est **marqué** ; un verdict ou une issue **hérite** de la marque de toute classe, de tout contrôle ou de tout déclencheur qui y entre. Deux implémentations peuvent alors légitimement diverger sur un élément marqué ; la valeur retenue est celle calculée avec les nombres de l'implémentation de référence (A), et la lecture le signale.

## 9. Verdicts de la course originale (pour la validation sur E4 seulement)

Contrôles T2, T3, T5, T6 supposés non déclenchés (ils ne le sont pas dans la course originale, § 12) ; déclencheurs d'audit de la course originale **ignorés** (leur audit a conclu « pas d'artefact »).
- **HR1** (« le mélange bat l'historique ») : verdict de la Table A.
- **HR0** (« réentraîner vaut mieux que ne rien faire ») : classes de (R0, V) par la Table B : « confirmée » si « R2 > R0 » aux deux budgets ; sinon « réfutée » si « R0 > R2 », « R0 ≳ R2 » ou « ≈ » dans au moins un budget ; sinon « non tranchée ».
- **HR3** (« la régularisation ne nuit pas ») : si T4 dans au moins un budget → « sans verdict (R4 ≈ défense figée) » ; sinon « confirmée » si la classe de (R4, V) est « R4 > R2 », « R4 ≳ R2 » ou « ≈ » aux deux budgets ; sinon « réfutée » si « R2 > R4 » dans au moins un budget ; sinon « non tranchée ».
- **HR2** (« oublier coûte », descriptif ici) : classes de (R1, X̄) par la Table B′ : « confirmée » si « R2 > R1 » aux deux budgets ; sinon « réfutée » si « R1 > R2 », « R1 ≳ R2 » ou « ≈ » dans au moins un budget ; sinon « non tranchée ».

## 10. Règles de la réplication (copie des « Critères de lecture gelés » du préenregistrement de réplication)

**10.1 Verdicts bruts** (calculés sur E1 de la réplication, racine ρ de la règle D ; la première ligne vraie décide ; l'ordre est obligatoire).

*HR1 répliquée ?* — pour chaque budget c : est_c, bas_c = bas(B2), haut_c = haut(B2) de (R3, V) :
1. T2, T3, T5 ou T6 déclenché → « non jugeable (santé) » ;
2. il existe un budget c tel que moy_c(k, V) ≤ 2α pour chacune des cinq variantes k → « non jugeable (jeu dégénéré) » — **ligne inatteignable** (sa condition fait partie de T2, ligne 1), gardée pour correspondre mot pour mot à la Table A originale (point 2) ;
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
- **TR1 — écart de réplication, dans les deux sens** : |g_π| > z* × σ_π pour au moins un π (forme canonique : c'est cette comparaison qui est évaluée et soumise à la frontière ; elle équivaut à |z_π| > z*). Un résultat **plus beau** que l'original déclenche comme un résultat plus faible ;
- **TR2 — trop propre** : |g_π| < 0,001 pour les quatre π ;
- **TR3 — défense figée plus belle que l'original** : κ_c ∈ {« R0 > R2 », « R0 ≳ R2 »} dans au moins un budget ;
- **TR4 — non-réplication** : verdict brut de HR1 ou de HR0 commençant par « non répliquée ».
Effet : si au moins un de TR1 à TR4 est déclenché, les verdicts de HR1, HR0, HR3 et du secondaire (ii) deviennent « non jugeable (audit en attente) » jusqu'au rapport scellé de l'audit ; « pas d'artefact » → verdicts bruts rétablis (avec la mention « après audit ») ; « artefact trouvé » → « non jugeable (artefact) ».

**10.3 Contrôle « graines neuves »** (liste d'arrêt, pas un audit ; CL-10). Après la course et **avant toute lecture**, B calcule, pour chaque variante k et chacune des trois mesures V (`V_iii_final`), X̄ (`exploitabilite_moyenne_tours`) et (ii) (`ii_final`), le nombre de tâches (c, i) où la valeur de la réplication est **égale au bit** (égalité de binaires64) à celle de la course originale (E4) à la même tâche. Si un de ces quinze comptes est **strictement supérieur à G = 2** → **arrêt de contrôle « graines non neuves »** (code 3, § 11). Le lecteur (R13) recompte ; ses comptes doivent être égaux à ceux de B. Justification du seuil : dans la course originale, les coïncidences au bit entre deux tâches distinctes d'une même variante, d'un même budget et d'une même mesure donnent au plus 0,081 coïncidence attendue par hasard sur 200 tâches (V de R0 et de R2) ; la probabilité de plus de 2 est alors d'au plus 8,3 × 10⁻⁵ par compte (loi de Poisson). Cas sain et artefact : § 12.

**10.4 Issues globales** (première ligne vraie ; point 3 et point 8). Deux issues sont calculées par B :
- l'**issue brute** : la table ci-dessous appliquée aux **verdicts bruts** du § 10.1 (TR1 à TR4 ignorés) ;
- l'**issue après déclencheurs** : la même table appliquée aux verdicts **après l'effet du § 10.2**.
Avant tout audit, c'est l'issue après déclencheurs qui vaut ; après un audit « pas d'artefact », l'issue brute vaut, avec la mention « après audit » ; après un audit « artefact trouvé », l'issue est « non jugeable (artefact) ». La ligne 1 dépend de V0, que B ne peut pas évaluer : B l'applique avec les seules conditions qu'il calcule (arrêt, discordance A/B), écrit dans sa sortie « V0 : non évaluée par B », et le **lecteur** applique la ligne 1 complète.

1. plomberie fausse (V0 de la réplication), arrêt, ou discordance A/B (§ 11) → « non jugeable (plomberie) » ;
2. HR1 ou HR0 « non jugeable (audit en attente) » → « en attente d'audit » ;
3. HR1 ou HR0 « non jugeable (artefact) » → « non jugeable (artefact) » ;
4. HR1 « non répliquée (…) » → « échec de réplication du résultat positif » ;
5. HR1 « répliquée » ∧ HR0 « répliquée » → « réplication réussie » ;
6. HR1 « répliquée » ∧ HR0 « non répliquée (…) » → « réplication partielle : le mélange tient, l'équivalence de la défense figée ne tient pas » ;
7. HR1 « répliquée » ∧ HR0 « non jugeable (…) » → « réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise » ;
8. sinon → « non jugeable ».

## 11. Sorties, codes de sortie et comparaison avec l'implémentation de référence

**11.1 Codes de sortie et fichier de sortie** (point 10).
- **Code 2 — arrêt d'entrée** : empreinte ou compagnon non conforme, champ exigé absent, format inattendu, garde des § 3, § 4, § 5.1, § 5.2 ou de cohérence de V (§ 7) : **aucun fichier de sortie**, motif sur la sortie d'erreur.
- **Code 3 — arrêt de contrôle** : « graines non neuves » (§ 10.3) ou discordance A/B de niveau arrêt (§ 11.2) : la sortie est **écrite** (pour le diagnostic par un sous-agent neuf) avec `lecture_autorisee: false` et la liste des motifs ; personne d'autre que l'agent de diagnostic n'en lit autre chose que le code, `lecture_autorisee` et les motifs.
- **Code 0** : sortie écrite, `lecture_autorisee: true`.
- Le fichier de sortie est **neuf** (jamais écrasé ; un fichier existant au même chemin est un arrêt d'entrée), en JSON UTF-8, et contient : `lecture_autorisee` et `motifs_arret` ; l'empreinte H et (ρ, ρ_t) en **chaînes** décimales ; pour `"1"` et `"2"`, l'objet `contrastes_contre_R2` indexé par libellé (format du § 5.7) ; les classes des Tables A, B, B′, C, avec leurs marques de frontière ; par budget, les valeurs comparées des contrôles T2 à T6 et leur état, puis leur état global ; les verdicts bruts et après déclencheurs du § 10.1 ; g_π, σ_π, z_π et l'état de TR1 à TR4 ; les quinze comptes du § 10.3 ; les deux issues globales du § 10.4 avec la mention « V0 : non évaluée par B » ; le résultat de la comparaison A/B (§ 11.2) ; les empreintes de tous les fichiers lus ; les versions (Python, numpy) ; la valeur de toute option de ligne de commande employée. Les noms de clés sont libres, mais le rapport de B donne la **table de correspondance** « élément de ce paragraphe → clé JSON ».

**11.2 Implémentation de référence A et concordance exigée.** A = l'analyse écrite par le code de la course (E5, mêmes libellés et mêmes champs que l'analyse de E4). Les classes, lignes et verdicts « de A » sont ceux que le lecteur neuf (R13) calcule à partir des nombres de A en appliquant le texte scellé.
- pour les **cinq contrastes de concordance exigée** × 2 budgets — (R3, V), (R0, V), (R4, V), (R0, (ii)), (R1, X̄) : |moyenne_A − moyenne_B|, |écart-type_A − écart-type_B| et, pour chacun des dix niveaux, |q_A − q_B| **≤ ε = 10⁻⁹** ; de même |z_π(A) − z_π(B)| ≤ 10⁻⁹ (z_π(A) calculé avec les nombres de A) ;
- classes, lignes de table, verdicts bruts, déclencheurs **identiques** entre B et les valeurs calculées sur les nombres de A, sauf élément marqué « à la frontière » (§ 8) ;
- sinon : **arrêt de contrôle** (code 3), aucune lecture, consignation ; le diagnostic est confié à un sous-agent neuf ; toute correction d'une implémentation après lecture des résultats de la réplication est un écart au préenregistrement (nœud de décision pour Lazar) ;
- les **11 autres contrastes** : même tolérance, mais une discordance y est une **alerte** écrite dans la sortie, pas un arrêt.

**11.3 Contrôles de santé : concordance et recoupement** (point 14). L'analyse de A ne contient pas d'état de contrôle. La concordance exigée porte sur les **états** de T2 à T6 (par budget et globaux) calculés par B et ceux que le **lecteur recalcule lui-même depuis E1** : identiques, sinon arrêt (consigné par le lecteur). En plus, à titre d'**alerte**, le lecteur recalcule les contrôles depuis les champs de l'analyse de A, selon cette correspondance (sous `resultat`, budget `"c"`) :

| Contrôle | Champs de l'analyse de A |
|---|---|
| T2 | `variantes.<k>.V_iii_final` (moy_c(k, V)) ; `contrastes_contre_R2."R3 - R2 (V_iii_final)".moyenne` ; `contrastes_contre_R2."<k> - R2 (exploitabilite_moyenne_tours)".moyenne` |
| T3 | `variantes.R3.poids.part_pure` × 100 = nombre de tâches pures (A emploie le même seuil s_pur) |
| T4 | `variantes.<R4>.cos_consecutif_par_tache` (100 valeurs, une par tâche, dans l'ordre des instances) |
| T5 | (a) `variantes.<k>.standard_moins_renforce` (moyenne des différences standard − renforcé : égale à la différence des moyennes à l'arrondi près) ; (b) `contrastes_contre_R2."<k> - R2 (V standard seul / renforce seul)".ecart` (= a − b) |
| T6 | `variantes.<k>.fpr_moyen` |

## 12. Validation obligatoire avant tout emploi (sur la course originale et sur des branches synthétiques)

**12.1 Sur la course originale.** L'implémentation appliquée à E4 (résultats originaux), avec ρ = 20266201, doit rendre l'analyse originale à ε près pour les 16 contrastes × 2 budgets. Valeurs de contrôle (écriture décimale complète, telle que lue dans l'analyse scellée `18b80112…`) :

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

**12.2 Branches que la course originale n'exerce pas** (exigé en v2). Pour **chaque ligne** de chaque table et de chaque verdict — Tables A, B, B′, C ; verdicts « HR1 répliquée ? », « HR0 répliquée ? », « HR3 répliquée ? », « lois tenues » ; issues brute et après déclencheurs du § 10.4 ; contrôles T2 à T6 (chaque condition) ; TR1 à TR4 — un essai sur des entrées **synthétiques** dont la ligne attendue est connue d'avance (vecteurs de différences de moyenne et de dispersion choisies, ou résultats synthétiques complets), en particulier les classes « R0 > R2 », « R0 ≳ R2 », « R2 ≳ R0 », « R2 > R0 », « R4 > R2 », « R2 > R4 » et les lignes 2, 3, 5 et 6 de la Table C. La ligne 2 de « HR1 répliquée ? » est inatteignable : l'essai montre qu'une entrée qui remplit sa condition rend « non jugeable (santé) ». Chaque essai de frontière place une quantité à moins de ε d'un seuil et vérifie la marque et son héritage.

**12.3 Gardes de la réplication : cas sain et artefact** (règle R5), sur des variantes de la course originale prises comme E1 (empreinte épinglée à la place du compagnon, point 7), avec ρ = 20266201 imposé :
- (a) **artefact** — original contre lui-même : g_π = 0 pour les quatre π, **TR2 déclenché** ; les quinze comptes du § 10.3 égaux à 200 ; **arrêt de contrôle « graines non neuves »**, code 3, `lecture_autorisee: false` ;
- (b) **cas sain** — dans chaque tâche et chaque variante, `V_iii_final`, `V_iii_standard`, `V_iii_renforce`, `exploitabilite_moyenne_tours` et `ii_final` augmentés de 10⁻⁶ (V reste le minimum des deux), et les trois champs de V de R3 augmentés en plus de 0,01 : aucun compte du § 10.3 au-dessus de 0, ni TR1 ni TR2, aucun arrêt, code 0 ;
- (c) R3 décalé (trois champs de V) de +0,06 : **TR1 déclenché vers le haut** (z_π > 0) ;
- (d) R3 décalé de −0,03, borné à 0 : **TR1 déclenché vers le bas** (z_π < 0) ;
- (e) une seule variante dont **trois** tâches gardent leur valeur originale exacte de V (les autres décalées comme en (b)) : arrêt « graines non neuves » ; **deux** tâches : aucun arrêt (le seuil est « strictement plus de 2 »).

**12.4 Entiers de 64 bits.** Fichiers E1 et E2 synthétiques dont les racines dépassent 2⁶³ (par exemple 2⁶⁴ − 59) : lues exactement, comparées exactement, écrites en chaînes exactes dans la sortie ; un lecteur qui passerait par le binaire64 doit faire échouer l'essai. Règle D sur les trois vecteurs d'essai du § 4.

**12.5 Gardes d'entrée** : pour chaque garde d'entrée des § 3, § 4, § 5 et § 7, un cas sain et un artefact (fichier modifié d'un octet, compagnon au mauvais nom de base, champ manquant, `delta` incohérent, `config_sha256` différent dans une tâche, `lam` faux, racine d'une tâche décalée d'une unité, E2 rattaché à un autre E1, etc.) : code 2, aucune sortie.

## 13. Arrondis, affichage, environnement, ce qui n'est pas spécifié

- Aucun arrondi dans les calculs ; toutes les comparaisons aux seuils portent sur les binaires64 non arrondis. L'affichage dans les documents se fait à 4 décimales (6 pour les bornes proches d'un seuil), sans effet sur aucune classe.
- La méthode de calcul de la moyenne, de l'écart-type et du tri est libre ; le générateur (§ 5.4) et l'ordre de remplissage de I (§ 5.5) ne le sont pas.
- **Environnement** : la validation (§ 12) et l'emploi sur la réplication se font avec l'interpréteur du dépôt, `/home/claude/controle-ia-travail/.venv/bin/python` (Python 3.13.18, numpy 2.4.6, celui de la course) ; les versions sont écrites dans la sortie et dans le rapport.
- Hors de cette spécification : la production des valeurs par tâche (le jeu, l'attaquant, l'oracle, la finale) ; elles sont les entrées.
