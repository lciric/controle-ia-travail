# Puissance de la garde appariée δ dans la fiche — v8 : sujet et comparateurs dispersés ensemble, remèdes chiffrés, neuvième comparateur — rapport v8

Lignée conv-audit, 30/10/2026, 01:51 UTC (heure lue par le constructeur du rapport). **Répond à la question de Lazar** : « quand le sujet et les comparateurs sont dispersés ensemble, la garde ne tient plus à 288
unités : comment faire alors ? », et, sur son feu vert relayé (23 h 35, heure de Paris), ajoute le **neuvième comparateur** (la recette HELIOS). **Complète la v7** (`rapport-puissance-garde-delta-v7.md`,
gardée, R12) et répond à la contre-lecture GD7 (`contre-lecture-garde-delta-v7.md`, constats GD7-01 à GD7-10, § 8). **Exploratoire, processeur seul, sans dépense, non préenregistré, non opposable ;
lois synthétiques seulement ; aucune lecture de `donnees/`. Non relu par une autre main (R2) : contre-lecture à demander (§ 10).** Les recommandations du § 6 sont des propositions : fixer une taille
ou un paramètre du programme est un nœud de décision de Lazar.

Fichiers (dossier `simulation-puissance-garde-delta-v8/`, chacun avec son empreinte compagnon `.sha256`) : le script `simulation-puissance-garde-delta-v8.py` (`4c7c93a9…`, fabriqué depuis la v7 `027954d8…`),
**46 passages principaux** et **6 passages de complément** (incertitude de graine), chacun avec sa sortie, son journal et son manifeste écrits par le script ; `tableaux-v8.md` (tous les tableaux détaillés, produits
par `tableaux-v8.py` depuis les sorties), `resume-v8.md` (les tableaux résumés de ce rapport, produits par `resume-v8.py` : **les tableaux ci-dessous en sont insérés par programme, rien n'est recopié à la
main**), les vérifications, et le manifeste d'ensemble `manifeste-puissance-garde-delta-v8-v2.json` (`a7dd020a…`), assemblé par `assembler-manifeste-v8.py` depuis les manifestes par passage (le manifeste `manifeste-puissance-garde-delta-v8.json` d'une première assemblée, scellé avant
la correction du texte de ce rapport, est gardé et remplacé : R12). Empreintes de
l'ensemble : § 12. Python 3.13.18, numpy 2.5.3, scipy 1.18.1 (utilisé seulement pour la table des quantiles de la copule, § 3.1), une seule version pour tous les passages ; graine maîtresse 20261029 (1, 2 et 3 pour
les compléments), dérivation `SeedSequence([graine, sha256(étiquette)])` (R9).

**Vocabulaire.** « Fiche » : minimum des 8 gardes (honnêtes) et des 8 contrastes (sabotés) d'un mode ; « seuil 40 » : lecture (A), deux modes, la fiche est retenue par la règle e-BH (Benjamini-Hochberg sur les
richesses des paris) à budget α_c/2, α_c = 0,05 ; « seuil 160 » : référence stricte 8/α_c, mesurée par l'atteinte du seuil par le minimum des 16 processus (borne basse de la retenue à m = 8, non simulée) ;
ρ : corrélation intra-unité (variance de la probabilité d'unité divisée par p(1 − p)), identique côté honnête (p = τ = 0,01) et côté saboté (p = 0,40) ; ρ_A pour le sujet, ρ_B pour les comparateurs ; K_h, K_s :
exécutions honnêtes et sabotées par unité ; « biais δ/4 » : décalage de 0,0125 de l'espérance du sujet honnête ; « **pire** » : au pire des quatre cellules K_h ∈ {10 ; 5} × biais ∈ {0 ; δ/4} (minimum d'une
puissance, maximum d'un n80 ou d'un n90) ; n80 (n90) : unités (honnêtes = sabotées) pour une puissance de 0,8 (0,9), par dichotomie à pas de 1/32 de l'intervalle (8 unités vers 256 à 512) ; « SUPPOSÉ » : scénario,
non estimation. **Les nombres à trois décimales des tableaux (puissances, gains, écarts-types, écarts relatifs) sont tronqués vers le bas (GD7-07) : une puissance affichée est un minorant ; les pourcentages du texte sont arrondis.** Je n'emploie pas « tient » sans seuil
(GD7-06) : je donne la puissance minimale, n80 et n90 ; la référence de la v7 était une fiche ≥ 0,986 à 288 unités. Paramètres communs : k = 8 comparateurs (9 au § 5), τ = 0,01, δ = 0,05, écart de
contraste 0,10, K_s = 10 (20 au § 3.3), 2 000 répétitions (erreur type ≤ 0,011), lecture (A) m = 2, α_c = 0,05, lois en échelle bêta.

## 0. Verdict

1. **À 288 unités, la fiche perd toute marge dès que le sujet et les comparateurs ont la même dispersion d'unité de 0,17** (bêta, au pire des quatre cellules) : **0,847 au seuil 40** (au-dessus de 0,8, mais n80 = 280) et
   **0,509 au seuil 160** (sous 0,8), contre 0,999 et 0,935 sans dispersion ; à ρ = 0,10 : 0,970 et 0,768 ; à ρ = 0,25 : 0,583 et 0,250 (sous 0,8 aux deux seuils). La perte vient d'abord des contrastes (variances de r_A et de r_B qui s'ajoutent), puis de la garde au seuil 160 (§ 1, table GC).
2. **Le remède qui se chiffre et se lit est « plus d'unités », réglé sur ρ mesuré au pilote** : n_h = 288 jusqu'à ρ_B = 0,10 au seuil 40, **304 à 0,17** (384 au seuil 160), **384 à 0,25** (496 au seuil 160) ; sans mesure,
   **400 unités** (fiche ≥ 0,980 au seuil 40 et ≥ 0,905 au seuil 160 à ρ = 0,17), soit **+112 unités (+39 %), +15 120 épisodes à K_h = 5** (+20 160 à K_h = 10) (§ 2, 6).
3. **Les autres remèdes ne remplacent pas les unités** : la difficulté d'unité partagée aide beaucoup (0,847 → 0,973 à c = 0,5) mais c'est une propriété du monde, non un levier, et son niveau n'est pas lisible sur le
   sujet avant G1 (§ 3.1) ; les strates ne rapportent que si la covariable prédit un écart propre au sujet (+0,025 à +0,054 à 288, ≤ +0,006 à 400, nul si l'écart est commun) (§ 3.2) ; K_s = 20 aide modestement
   (−32 unités au n80, mais +67 % d'épisodes par unité à K_h = 5) (§ 3.3).
4. **Neuvième comparateur** : à écart de contraste 0,10 comme les huit autres, **il ne change pas les tailles prévues** (surcoût du n80 ≤ 16 unités au seuil 40, ≤ 8 au seuil 160, table de lecture inchangée à 16 unités près) ;
   à écart **0,05 (SUPPOSÉ, « comparateur fort »)**, **il les change fortement** : 0,865 à 288 sans dispersion, 0,542 en logit σ = 1,0, 0,312 à ρ = 0,17, et il faut +128 à +432 unités au seuil 40 (§ 5).

## 1. La question : où la fiche perd-elle, et combien d'unités la ramènent (remède 1)

La v7 (GD7-03) avait laissé ouverte la combinaison de la dispersion du sujet et de celle des comparateurs ; la v8 la rend simulable (`--combiner-dispersion-a-et-comparateurs`, `--effet-unite-beta` pour A,
`--rho-comparateurs` pour les B) et **retrouve les chiffres de la contre-lecture** (`verif-identite-gd7-v8-sortie.json` : 25 résultats, 307 champs, 0 différence ; ρ donné directement = ρ déduit de σ, § 11).

**Table R1 — puissance de la fiche selon la taille (K_s = 10, k = 8, au pire des quatre cellules) et n80, n90 (deux hypothèses sur le sujet : ρ_A = ρ_B, et ρ_A = 2 ρ_B)**

| ρ_A | ρ_B | seuil | 288 | 400 | 500 | 650 | n80 (pire) | n90 (pire) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 40 | 0,999 | 1,000 | 1,000 | 1,000 | 184 | 196 |
| 0 | 0 | 160 | 0,935 | 1,000 | 1,000 | 1,000 | 264 | 280 |
| 0,05 | 0,05 | 40 | 0,994 | 1,000 | 1,000 | 1,000 | 200 | 216 |
| 0,05 | 0,05 | 160 | 0,869 | 0,998 | 1,000 | 1,000 | 280 | 296 |
| 0,05 | 0,025 | 40 | 0,995 | 1,000 | 1,000 | 1,000 | 196 | 216 |
| 0,05 | 0,025 | 160 | 0,901 | 0,999 | 1,000 | 1,000 | 272 | 296 |
| 0,1 | 0,1 | 40 | 0,970 | 0,998 | 1,000 | 1,000 | 224 | 252 |
| 0,1 | 0,1 | 160 | 0,768 | 0,989 | 0,999 | 1,000 | 304 | 328 |
| 0,1 | 0,05 | 40 | 0,989 | 1,000 | 1,000 | 1,000 | 208 | 236 |
| 0,1 | 0,05 | 160 | 0,822 | 0,994 | 0,999 | 1,000 | 288 | 320 |
| 0,17 | 0,17 | 40 | 0,847 | 0,980 | 0,997 | 1,000 | 280 | 320 |
| 0,17 | 0,17 | 160 | 0,509 | 0,905 | 0,985 | 0,999 | 360 | 400 |
| 0,17 | 0,085 | 40 | 0,923 | 0,994 | 0,999 | 1,000 | 244 | 280 |
| 0,17 | 0,085 | 160 | 0,655 | 0,957 | 0,996 | 1,000 | 320 | 360 |
| 0,25 | 0,25 | 40 | 0,583 | 0,902 | 0,976 | 0,997 | 360 | 408 |
| 0,25 | 0,25 | 160 | 0,250 | 0,693 | 0,889 | 0,983 | 456 | 512 |

Lecture : sans dispersion du sujet (v7), la fiche valait ≥ 0,986 à 288 unités ; avec la même dispersion sur les deux, elle perd 0,15 (ρ = 0,17, seuil 40) et il faut **280 unités pour 0,8** (320 pour 0,9) au seuil 40 et
**360** (400) au seuil 160, contre 184 et 264 sans dispersion. À 400 unités elle remonte à ≥ 0,980 (seuil 40) et ≥ 0,905 (seuil 160) à ρ = 0,17 ; à 500 unités à ≥ 0,997 et ≥ 0,985. À ρ = 0,25 même 650 unités ne
donnent que 0,997 et 0,983. À ρ_A = 0,17, diviser ρ_B par 2 fait passer la fiche pire à 288 unités de 0,847 à 0,923 et le n80 de 280 à 244 (seuil 40) : la dispersion des comparateurs pèse, celle du sujet aussi.

**Où la fiche perd-elle (288 unités, K_s = 10, au pire des quatre cellules)** — le minimum de la fiche est le plus petit des deux ; au seuil 40 la garde est presque saturée sans dispersion (GD7-01), au seuil 160 elle ne l'est pas.

| ρ_A | ρ_B | minimum des 8 gardes, seuil 40 | minimum des 8 gardes, seuil 160 | minimum des 8 contrastes, seuil 40 | minimum des 8 contrastes, seuil 160 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0,995 | 0,935 | 1,000 | 0,999 |
| 0,05 | 0,05 | 0,989 | 0,880 | 0,997 | 0,986 |
| 0,05 | 0,025 | 0,987 | 0,904 | 0,998 | 0,994 |
| 0,1 | 0,1 | 0,974 | 0,845 | 0,971 | 0,910 |
| 0,1 | 0,05 | 0,977 | 0,845 | 0,990 | 0,964 |
| 0,17 | 0,17 | 0,942 | 0,751 | 0,849 | 0,686 |
| 0,17 | 0,085 | 0,939 | 0,755 | 0,946 | 0,859 |
| 0,25 | 0,25 | 0,888 | 0,672 | 0,620 | 0,395 |

À ρ = 0,17 : au seuil 40 le contraste (0,849) pèse plus que la garde (0,942, à K_h = 5 et biais δ/4) ; au seuil 160 les deux pèsent (garde 0,751, contraste 0,686). Le biais et K_h n'agissent que sur la garde.

**Table de lecture pour le pilote** (« ρ mesuré → n_h »). n_h = max(288 ; plus petit multiple de 16 au moins égal à 1,06 × n80 pire), enveloppe croissante en ρ_B (jamais de lecture vers le bas) ; la marge 1,06 reprend la
borne d'incertitude de graine de GD2-07, mesurée au § 7.

| ρ_B mesuré | hypothèse sur A | n80 seuil 40 (pire) | n80 seuil 160 (pire) | n_h seuil 40 | n_h seuil 160 |
| --- | --- | --- | --- | --- | --- |
| 0 | ρ_A = ρ_B | 184 | 264 | 288 | 288 |
| 0,05 | ρ_A = ρ_B | 200 | 280 | 288 | 304 |
| 0,1 | ρ_A = ρ_B | 224 | 304 | 288 | 336 |
| 0,17 | ρ_A = ρ_B | 280 | 360 | 304 | 384 |
| 0,25 | ρ_A = ρ_B | 360 | 456 | 384 | 496 |
| 0,025 | ρ_A = 2 ρ_B | 196 | 272 | 288 | 304 |
| 0,05 | ρ_A = 2 ρ_B | 208 | 288 | 288 | 320 |
| 0,085 | ρ_A = 2 ρ_B | 244 | 320 | 288 | 352 |

Règle : mesurer ρ_B au pilote **côté sabotage** (p ≈ 0,4), prendre la ligne **égale ou immédiatement supérieure à ρ̂ + 1,645 × écart-type de la lecture**, lire n_h ; lire les deux hypothèses sur le sujet et prendre
la plus grande (A n'est pas lu avant G1, P-9) ; au-delà de ρ_B = 0,25 la table ne dit rien. Précision de la lecture : estimateur par les moments, ρ̂ = (K·V/(p̄(1 − p̄)) − 1)/(K − 1) (V : variance empirique des scores
d'unité, K = 10) ; écart-type simulé (2 000 répétitions, `precision-rho-pilote-v8-sortie.json`) :

| ρ vrai | N unités du pilote | écart-type de ρ̂ côté sabotage (p = 0,4) | écart-type de ρ̂ côté honnête (p = 0,01) |
| --- | --- | --- | --- |
| 0,05 | 50 | 0,028 | 0,052 |
| 0,05 | 100 | 0,021 | 0,045 |
| 0,05 | 288 | 0,012 | 0,027 |
| 0,1 | 50 | 0,036 | 0,086 |
| 0,1 | 100 | 0,024 | 0,073 |
| 0,1 | 288 | 0,015 | 0,047 |
| 0,17 | 50 | 0,044 | 0,122 |
| 0,17 | 100 | 0,032 | 0,108 |
| 0,17 | 288 | 0,018 | 0,071 |
| 0,25 | 50 | 0,053 | 0,171 |
| 0,25 | 100 | 0,036 | 0,147 |
| 0,25 | 288 | 0,020 | 0,097 |

**Le côté honnête (p = 0,01) est inutilisable pour lire ρ** (écart-type 0,072 à ρ = 0,17 et 288 unités) ; le côté sabotage donne 0,018. La lecture suppose le **même ρ des deux côtés** (une seule κ), ce qui est la loi
simulée, non un fait (SUPPOSÉ).

Coût en épisodes (SUPPOSÉ : plan apparié, le sujet et chaque comparateur jouent tous les épisodes) : n × (K_h + K_s) × (k + 1) = 135 n à K_h = 5 et 180 n à K_h = 10. Soit : 288 unités, 38 880 (51 840) ; 304,
41 040 (54 720) ; 384, 51 840 (69 120) ; **400, 54 000 (72 000)** ; 496, 66 960 (89 280) épisodes à K_h = 5 (K_h = 10).

## 2. Remède 1 en une phrase

Plus d'unités est le seul remède dont l'effet est **garanti par la taille**, **lisible** au pilote (ρ_B côté sabotage) et **monotone** : fiche pire ≥ 0,980 à 400 unités pour tout ρ ≤ 0,17 (A = B) au seuil 40, ≥ 0,905 au
seuil 160. Son coût est linéaire en épisodes (135 par unité à K_h = 5).

## 3. Les trois autres remèdes

### 3.1 Remède 2 — difficulté d'unité partagée entre le sujet et les comparateurs (copule gaussienne, c ∈ {0 ; 0,5 ; 0,8})

Modèle : une difficulté d'unité commune u ; z_x = √c·u + √(1 − c)·e_x pour le sujet et pour chaque comparateur ; p_x = quantile bêta de Φ(z_x) (mêmes lois marginales qu'à c = 0, vérifié : table des quantiles à 10⁻⁹,
espérances et variances tenues, corrélations de Pearson retrouvées par quadrature à moins de 0,01, témoin c → 0 à moins de 2 erreurs types, `verif-copule-strates-v8-sortie.json`).

| ρ_A = ρ_B | c | Pearson(p_A, p_B) sabotés | fiche 288, seuil 40 (pire) | fiche 288, seuil 160 (pire) | fiche 400, seuil 160 (pire) | n80 seuil 40 (pire) | n80 seuil 160 (pire) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0,1 | 0 | 0,00 | 0,970 | 0,768 | 0,989 | 224 | 304 |
| 0,1 | 0,5 | 0,50 | 0,994 | 0,849 | 0,996 | 204 | 280 |
| 0,1 | 0,8 | 0,80 | 0,994 | 0,884 | 0,999 | 196 | 272 |
| 0,17 | 0 | 0,00 | 0,847 | 0,509 | 0,905 | 280 | 360 |
| 0,17 | 0,5 | 0,49 | 0,973 | 0,759 | 0,980 | 220 | 304 |
| 0,17 | 0,8 | 0,79 | 0,987 | 0,846 | 0,993 | 200 | 280 |

**Mesure de l'annulation** : à ρ = 0,17, la corrélation observée entre r_A et r_B est 0,33 (c = 0,5) et 0,53 (c = 0,8) (0,26 et 0,42 à ρ = 0,10) ; l'écart-type du contraste v = r_A − r_B passe de 0,352
(calcul exact sans corrélation : √(Σ p(1 − p)[1/K_s + ρ(1 − 1/K_s)]), non simulé) à **0,288 (−18 %) puis 0,241 (−32 %)** (simulé) ; celui de la garde g vaut 0,064 (c = 0,5) et 0,054 (c = 0,8) (valeurs tirées, `tableaux-v8.md` T4bis). Le
contraste annule donc la part de variance inter-unités commune au sujet et au comparateur (corrélation de Pearson des probabilités côté sabotage : 0,50 et 0,79), pas davantage ; côté honnête elle reste sous c
(0,27 et 0,63 à ρ = 0,17, à cause de la queue de la bêta de moyenne 0,01 : c'est la copule qui vaut c, non la corrélation).

Effet sur la fiche (pire, 288 unités, seuil 40) : 0,847 → **0,973** → **0,987** à ρ = 0,17 ; n80 280 → 220 → 200 ; seuil 160 : 0,509 → 0,759 → 0,846. **Le gain est réel mais n'est pas un levier** :
(i) c est une propriété du monde, non un réglage ; (ii) A n'est pas lu avant G1 (P-9), donc c entre sujet et comparateurs n'est pas mesurable au pilote ; on peut lire à sa place la **corrélation entre
comparateurs** (égale à c dans ce modèle, 0,50 et 0,80 mesurées à ρ = 0,17 côté sabotage : SUPPOSÉ que la difficulté qui lie les comparateurs lie aussi le sujet) ; (iii) la copule lie aussi les comparateurs entre
eux ; la corrélation de leurs contrastes reste à 0,51 pour c = 0,5 et 0,8 (attendue 0,51 à c = 0, par r_A partagé) : le minimum des huit n'en tire pas de bénéfice supplémentaire, le gain vient de l'annulation entre sujet et comparateur. **Dimensionner à c = 0** ; lire c au pilote comme un bonus éventuel.

### 3.2 Remède 3 — strates d'unités (blocage par une covariable de difficulté connue d'avance, étalonnage par strate)

Modèle : S ∈ {2, 3} strates de poids égaux, difficulté multiplicative θ_s = 1 + γ·d_s (d = −1, +1 ou −1, 0, +1) sur la probabilité d'unité, ρ total tenu à 0,17 (ρ intra-strate résolu par le script,
`verif-copule-strates-v8-sortie.json`) ; allocation par blocs (équilibrée à chaque répétition) ; étalonnage = soustraction du décalage analytique de strate sur g et sur v (**exact : borne haute de ce qu'une
covariable réelle donnerait**). Deux portées : « **commune** » (la covariable déplace A et les B de la même façon : le contraste apparié l'annule déjà) et « **sujet** » (elle déplace A seul : sensibilité
différenciée, SUPPOSÉ).

| portée | S | γ | fiche 288 brute | fiche 288 étalonnée | gain à 288 | gain à 400 |
| --- | --- | --- | --- | --- | --- | --- |
| sujet | 2 | 0.2 | 0,874 | 0,909 | +0,035 | +0,006 |
| sujet | 2 | 0.4 | 0,932 | 0,978 | +0,046 | +0,002 |
| sujet | 3 | 0.2 | 0,869 | 0,894 | +0,025 | +0,004 |
| sujet | 3 | 0.4 | 0,906 | 0,961 | +0,054 | +0,004 |
| commune | 2 | 0.4 | 0,990 | 0,989 | −0,001 | −0,000 |
| commune | 3 | 0.4 | 0,984 | 0,985 | +0,001 | +0,000 |

Passes avec n80 (S = 3, γ = 0,4, sensibilité différenciée, ρ = 0,17, K_s = 10, pire des quatre cellules) :

| passage | fiche 288 (pire) | fiche 400 (pire) | fiche 500 (pire) | fiche 650 (pire) | n80 seuil 40 (pire) | n80 seuil 160 (pire) |
| --- | --- | --- | --- | --- | --- | --- |
| sans strate (A et B, ρ = 0,17) | 0,847 | 0,980 | 0,997 | 1,000 | 280 | 360 |
| 3 strates, γ = 0,4, sensibilité différenciée, brut | 0,878 | 0,992 | 0,998 | 1,000 | 264 | 352 |
| 3 strates, γ = 0,4, sensibilité différenciée, étalonné | 0,934 | 0,996 | 1,000 | 1,000 | 248 | 328 |

**Résultat** : portée commune, gain nul (−0,001 et +0,001 ; erreur type de la moyenne de quatre différences ≈ 0,008) ; portée sujet, **+0,025 à +0,054** à 288 unités et **≤ +0,006** à 400 ; au mieux
(S = 3, γ = 0,4) le n80 passe de 280 à 248 (−32 unités, −11 %) au seuil 40 et de 360 à 328 au seuil 160. Le blocage seul (sans étalonnage) donne une partie du gain (allocation par blocs contre aléatoire, S = 3, γ = 0,4, brut, une cellule K_h = 10, biais 0 : 0,910 contre
0,873). Les strates ne remplacent pas les unités, et leur gain dépend d'une covariable qui prédit l'écart propre au sujet : à vérifier sur données, hors de cette simulation.

### 3.3 Remède 4 — K_s = 20 au lieu de 10

| ρ_A = ρ_B | K_s | fiche 288, seuil 40 (pire) | fiche 288, seuil 160 (pire) | n80 seuil 40 (pire) | n80 seuil 160 (pire) | épisodes au n80 seuil 40 (K_h = 5) | épisodes à 400 unités (K_h = 5) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0,05 | 10 | 0,994 | 0,869 | 200 | 280 | 27000 | 54000 |
| 0,05 | 20 | 0,994 | 0,885 | 192 | 272 | 43200 | 90000 |
| 0,1 | 10 | 0,970 | 0,768 | 224 | 304 | 30240 | 54000 |
| 0,1 | 20 | 0,983 | 0,827 | 208 | 288 | 46800 | 90000 |
| 0,17 | 10 | 0,847 | 0,509 | 280 | 360 | 37800 | 54000 |
| 0,17 | 20 | 0,934 | 0,626 | 248 | 328 | 55800 | 90000 |

(Épisodes : n × (5 + K_s) × 9, à K_h = 5.) K_s = 20 aide **modestement**, plus que je ne l'attendais (« peu ») : à ρ = 0,17, fiche 0,847 → 0,934 à 288 unités et n80 280 → 248 (−32 unités, −11 %) au seuil 40, mais
chaque unité coûte 25/15 = 1,67 fois plus d'épisodes à K_h = 5 : **le n80 coûte 55 800 épisodes contre 37 800**, et à 288 unités 64 800 épisodes donnent 0,934 là où 54 000 (400 unités, K_s = 10) donnent 0,980.
La raison : doubler K_s retire la part binomiale (1/K_s) de la variance des scores d'unité, non la part entre unités (ρ), qui domine à ρ = 0,17. À K_h = 20, K_s = 10 : fiche 0,882 (0,877 à K_h = 10), le contraste
reste le maillon (0,854, `tableaux-v8.md` T6ter). **Les unités achètent plus par épisode que K_s.**

## 4. Les trois remèdes lus ensemble

| remède | gain à 288 unités (ρ = 0,17, seuil 40) | gain sur n80 | coût | levier ? |
| --- | --- | --- | --- | --- |
| 1. plus d'unités | 0,847 → 0,980 (400) → 0,997 (500) | n_h = 304 à 384 | 135 épisodes par unité à K_h = 5 | oui, lu au pilote |
| 2. difficulté partagée | 0,847 → 0,973 (c = 0,5) → 0,987 (c = 0,8) | 280 → 220 → 200 | aucun | non (propriété du monde) |
| 3. strates (étalonnage exact) | +0,025 à +0,054 (sujet) ; 0 (commun) | −32 unités au mieux | covariable connue d'avance | partiel, hypothèse non vérifiée |
| 4. K_s = 20 | 0,847 → 0,934 | −32 unités | +67 % d'épisodes par unité (K_h = 5) | oui, mais moins rentable que les unités |

## 5. Effet d'un neuvième comparateur (recette HELIOS)

Le neuvième comparateur est tiré comme les huit autres (mêmes lois, mêmes dispersions) ; seul change l'**écart de contraste** de son r_B : r_B9 = r_B + 0,10 − E, avec E = 0,10 (comme les autres) ou **E = 0,05
(SUPPOSÉ : « comparateur fort », moitié moins séparé du sujet saboté)**. k = 9 passé aux cellules principales (K_s = 10, K_h ∈ {10 ; 5}, biais ∈ {0 ; δ/4}, tailles 288, 400, 500, 650, n80 aux deux seuils).
Dispersions : aucune, logit σ = 1,0, bêta de même variance, bêta combinée ρ ∈ {0,05 ; 0,10 ; 0,17} (le cas E = 0,10 à ρ = 0,10 et 0,17 est lu aussi). Pire des quatre cellules ; surcoût = n80 à neuf moins n80 à huit
(même loi, même cellule), au pire des quatre cellules.

| dispersion | k | écart du 9ᵉ | 288 | 400 | 500 | 650 | n80 seuil 40 (pire) | n80 seuil 160 (pire) | surcoût seuil 40 (unités, pire) | surcoût seuil 160 (unités, pire) | n_h seuil 40 | n_h seuil 160 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nulle | 8 | — | 0,999 | 1,000 | 1,000 | 1,000 | 184 | 264 | — | — | 288 | 288 |
| nulle | 9 | 0,05 | 0,865 | 0,961 | 0,989 | 0,997 | 264 | 344 | +128 | +176 | 288 | 368 |
| nulle | 9 | 0,10 | 0,999 | 1,000 | 1,000 | 1,000 | 184 | 264 | +2 | +4 | 288 | 288 |
| logit σ = 1,0 | 8 | — | 0,986 | 0,999 | 1,000 | 1,000 | 208 | 280 | — | — | 288 | 304 |
| logit σ = 1,0 | 9 | 0,05 | 0,542 | 0,725 | 0,838 | 0,917 | 472 | 624 | +288 | +388 | 512 | 672 |
| logit σ = 1,0 | 9 | 0,10 | 0,987 | 0,999 | 1,000 | 1,000 | 208 | 280 | +8 | +8 | 288 | 304 |
| bêta (σ de référence 1,0) | 8 | — | 0,988 | 0,999 | 1,000 | 1,000 | 212 | 280 | — | — | 288 | 304 |
| bêta (σ de référence 1,0) | 9 | 0,05 | 0,534 | 0,737 | 0,836 | 0,927 | 456 | 624 | +264 | +388 | 496 | 672 |
| bêta (σ de référence 1,0) | 9 | 0,10 | 0,989 | 0,999 | 1,000 | 1,000 | 212 | 288 | +4 | +8 | 288 | 320 |
| ρ_A = ρ_B = 0,05 | 8 | — | 0,994 | 1,000 | 1,000 | 1,000 | 200 | 280 | — | — | 288 | 304 |
| ρ_A = ρ_B = 0,05 | 9 | 0,05 | 0,672 | 0,833 | 0,924 | 0,973 | 368 | 504 | +212 | +308 | 400 | 544 |
| ρ_A = ρ_B = 0,05 | 9 | 0,10 | 0,994 | 0,999 | 1,000 | 1,000 | 200 | 280 | +4 | +8 | 288 | 304 |
| ρ_A = ρ_B = 0,10 | 8 | — | 0,970 | 0,998 | 1,000 | 1,000 | 224 | 304 | — | — | 288 | 336 |
| ρ_A = ρ_B = 0,10 | 9 | 0,05 | 0,484 | 0,702 | 0,804 | 0,896 | 504 | 688 | +316 | +428 | 544 | 736 |
| ρ_A = ρ_B = 0,10 | 9 | 0,10 | 0,972 | 0,998 | 1,000 | 1,000 | 228 | 304 | +4 | +4 | 288 | 336 |
| ρ_A = ρ_B = 0,17 | 8 | — | 0,847 | 0,980 | 0,997 | 1,000 | 280 | 360 | — | — | 304 | 384 |
| ρ_A = ρ_B = 0,17 | 9 | 0,05 | 0,312 | 0,483 | 0,631 | 0,782 | 688 | 912 | +432 | +568 | 736 | 976 |
| ρ_A = ρ_B = 0,17 | 9 | 0,10 | 0,810 | 0,978 | 0,995 | 1,000 | 280 | 360 | +16 | +8 | 304 | 384 |

**Réponse à la question (a), « l'ajout tient-il aux tailles prévues, ou à quel coût ? »** — « oui » veut dire ici : n80 et n_h inchangés à 16 unités près ; « non » : le coût est donné en unités.


- **À écart de contraste 0,10 (comme les huit autres) : oui.** Fiche pire à 288 unités, de huit à neuf comparateurs : 0,999 → 0,999 (sans dispersion), 0,986 → 0,987 (logit σ = 1,0), 0,970 → 0,972 (ρ = 0,10),
  0,847 → 0,810 (ρ = 0,17) ; surcoût du n80 ≤ 16 unités au seuil 40 (le 16 est à ρ = 0,17 ; ≤ 8 ailleurs, soit la résolution de la dichotomie) et ≤ 8 au seuil 160 ; la table de lecture n_h ne change pas (304 et 384 à
  ρ = 0,17), sauf +16 en bêta σ = 1,0 au seuil 160 (320 contre 304). Le coût en épisodes d'un comparateur de plus est de 10/9 à unités égales (150 par unité à K_h = 5).
- **À écart 0,05 (SUPPOSÉ) : non.** Fiche pire à 288 unités : 0,865 sans dispersion, 0,672 (ρ = 0,05), 0,542 (logit σ = 1,0), 0,484 (ρ = 0,10), 0,312 (ρ = 0,17) ; même 650 unités ne donnent que 0,917
  à 0,927 en σ = 1,0 et 0,782 à ρ = 0,17. Pour garder 0,8 il faut, **en plus** de la taille à huit comparateurs, **+128** (sans dispersion), **+212** (ρ = 0,05), **+288** (logit), **+316** (ρ = 0,10), **+432**
  (ρ = 0,17) unités au seuil 40 ; +176, +308, +388, +428, +568 au seuil 160 ; soit n_h = 288, 400, 512, 544, 736 au seuil 40 (368, 544, 672, 736, 976 au seuil 160), à coûter à 150 épisodes par unité (K_h = 5).
  Le maillon est le contraste du neuvième comparateur : à K_h = 5 et biais δ/4, minimum des neuf contrastes 0,848 sans dispersion, 0,530 en bêta σ = 1,0, 0,349 à ρ = 0,17, contre un minimum des neuf gardes de 0,996, 0,997 et
  0,930 (`tableaux-v8.md` T7bis) ; le n80 est multiplié par 1,4 (sans dispersion) à 2,5 (ρ = 0,17).
- **Ce que le pilote doit lire** : l'écart de contraste observé du neuvième comparateur (moyenne de r_A − r_B9 sur unités sabotées) ; s'il est proche de 0,10, ajouter le comparateur ; s'il est proche de 0,05, ou bien
  porter la taille à la valeur de la table ci-dessus, ou bien le traiter à part de la fiche (choix de revendication : nœud de décision de Lazar).

## 6. Recommandation chiffrée

1. **Remède à retenir : plus d'unités, réglées sur ρ_B lu au pilote côté sabotage** (table de lecture, § 1). Taille proposée **sans mesure : 400 unités** (K_s = 10, huit comparateurs), qui couvre le sujet et les
   comparateurs à ρ ≤ 0,17 avec une fiche pire ≥ 0,980 au seuil 40 et ≥ 0,905 au seuil 160 (n90 au seuil 160 : 400). **Coût : +112 unités par rapport à 288 (+39 %), +15 120 épisodes à K_h = 5, +20 160 à K_h = 10.**
   Si le pilote lit ρ_B ≤ 0,10 : n_h = 288 au seuil 40 (fiche pire ≥ 0,970), 336 au seuil 160 ; si ρ_B ≈ 0,25 : 384 (seuil 40) à 496 (seuil 160) unités, soit 51 840 à 66 960 épisodes à K_h = 5.
2. **Ne pas acheter K_s = 20 ni compter sur les strates ou sur la difficulté partagée pour dimensionner** : K_s = 20 coûte 1,67 fois plus d'épisodes par unité pour −32 unités de n80 ; les strates ne rapportent que
   dans un scénario non vérifié (+0,025 à +0,054 à 288, ≤ +0,006 à 400) ; la difficulté partagée est un bonus non mesurable avant G1 sur le sujet. Lire c entre comparateurs et la covariable de difficulté au pilote,
   sans en dépendre.
3. **Neuvième comparateur** : l'ajouter si son écart de contraste lu au pilote est ≈ 0,10 (aucun coût visible aux tailles de la table) ; sinon, à ≈ 0,05, ajouter +128 à +432 unités (seuil 40) ou le sortir de la
   fiche (décision de Lazar).
4. **À trancher par Lazar** : (i) la taille sans mesure (400 proposée) ; (ii) le seuil qui fait foi pour G1 (40, lecture (A), ou 160 plus strict : 304 contre 384 à ρ = 0,17) ; (iii) le sort du neuvième comparateur
   s'il est fort. Aucun de ces points ne change le programme sans son GO.

## 7. Incertitude de graine de n80 (GD2-07), mesurée

Même script, mêmes options que `meme-rho0.05` et `meme-rho0.17`, restreintes à K_h = 5, K_s = 10, biais δ/4, 288 unités ; quatre graines maîtresses (20261029, 1, 2, 3), n80 et n90 aux deux seuils :

| ρ_A = ρ_B | mesure | seuil | n80 ou n90 par graine (20261029 ; 1 ; 2 ; 3) | écart relatif maximal à la moyenne | étendue relative |
| --- | --- | --- | --- | --- | --- |
| 0,05 | n80 | 40 | 200 ; 200 ; 200 ; 200 | 0,000 | 0,000 |
| 0,05 | n90 | 40 | 216 ; 216 ; 220 ; 216 | 0,013 | 0,018 |
| 0,05 | n80 | 160 | 280 ; 280 ; 280 ; 272 | 0,021 | 0,028 |
| 0,05 | n90 | 160 | 296 ; 296 ; 296 ; 296 | 0,000 | 0,000 |
| 0,17 | n80 | 40 | 280 ; 280 ; 280 ; 280 | 0,000 | 0,000 |
| 0,17 | n90 | 40 | 320 ; 312 ; 320 ; 320 | 0,018 | 0,025 |
| 0,17 | n80 | 160 | 360 ; 360 ; 352 ; 360 | 0,016 | 0,022 |
| 0,17 | n90 | 160 | 400 ; 392 ; 408 ; 400 | 0,020 | 0,040 |

Écart relatif maximal à la moyenne : **2,2 %** ; étendue relative maximale : **4,0 %**. **Lecture prudente (R4, résultat suspect de propreté)** : sur trois lignes de huit, les quatre graines donnent le
même n80 ; la raison n'est pas une absence de bruit mais la **résolution de la dichotomie** (pas de 8 unités vers 256 à 512, soit 2,9 % à 280) ; la dispersion de graine mesurée est du même ordre que la
résolution, donc **non résolue en dessous de 8 unités**. La borne de 6 % de GD2-07 n'est pas contredite ; elle n'est pas démontrée non plus (quatre graines, deux lignes). La marge 1,06 de la table couvre l'écart
maximal (2,2 %) mais non la somme étendue maximale + résolution (4,0 % + 3,1 % = 7,1 %) ; l'arrondi de n_h au multiple de 16 supérieur ajoute 8 unités en moyenne (≈ 3 %).

## 8. Réponses aux constats GD7-01 à GD7-10

| constat | réponse en v8 |
| --- | --- |
| GD7-01 (« la garde ne perd pas » vaut au seuil 40) | Le seuil est nommé partout ; la garde est lue aux deux seuils (table GC) : à ρ = 0,17 elle vaut 0,942 (seuil 40) et 0,751 (seuil 160) au pire, elle **perd**. |
| GD7-02 (autre appariement de κ) | Inchangé (v7) ; non repassé ; la contre-lecture l'a passé (plus favorable). |
| GD7-03 (combinaison A et B, « grave ») | **Objet de la v8** : simulée par le script (`--combiner-dispersion-a-et-comparateurs`), chiffres de la contre-lecture retrouvés sans différence ; remèdes quantifiés. |
| GD7-04 (identité, chemin K_s ≠ K_h) | `verif-identite-v7-v8` couvre le produit cartésien K_h × K_s (K_s ∈ {10, 5, 3}, apparié `--K-sabotes`), 7 cas, 57 cellules, 4 447 champs, 0 différence, deux témoins négatifs décelés. |
| GD7-05 (« dépend de K_s, presque pas de K_h » : propriété du modèle) | Écrit comme tel : écart de contraste 0,10, τ = 0,01, seuil nommé ; K_h compte via la garde au seuil 160 (table GC) et via le biais. |
| GD7-06 (phrase trop forte) | § 9 : seuil nommé, tailles simulées nommées, minima donnés, lois énumérées (non un continuum), sujet A déclaré, deux seuils séparés. |
| GD7-07 (arrondi du minimum) | Puissances **tronquées** à 3 décimales (minorants) dans tous les tableaux de la v8. |
| GD7-08 (lois non essayées) | (a) corrélation entre comparateurs : essayée par la copule (§ 3.1) ; (b) lien honnêtes–sabotés : non simulé (tirés à part, corrélation mesurée nulle, |r| ≤ 0,003) ; effet attendu de second ordre (v6, T6) ; (c) ρ plus fort : ρ = 0,25 passé ; (d) biais au-delà de δ/4 : hors sujet ; (e) A et B combinés : fait. |
| GD7-09 (lectures hors dossier, git) | **Aucune commande git dans le script ni dans les lanceurs** : le commit est déclaré (`--commit-declare`, copié sans être lu), `platform.platform()` remplacé par `os.uname()` ; `verif-sans-git-v8-sortie.json` : analyse syntaxique (aucun `subprocess`, `os.system`…), piège à sous-processus (aucun appel au cours d'un passage sain avec `--sortie`, copule et import de scipy ; l'artefact est vu), commit déclaré retrouvé dans la sortie et le manifeste. |
| GD7-10 (chiffres de synthèse) | Repris tels quels (`chiffres-v7-repris-v8-sortie.json` recalcule GD7-01, 05, 07, 10 depuis les sorties de la v7). |

## 9. Phrase pour le brouillon 4 de G1 (compatible avec GD7-01 à GD7-10)

**Phrase proposée** (sans recommandation sur les valeurs, à trancher par Lazar) :

« Sous lois synthétiques non préenregistrées (simulation v8, 2 000 répétitions, graine 20261029), à τ = 0,01, δ = 0,05, huit comparateurs, écart de contraste 0,10, K_s = 10, lecture (A), K_h ∈ {10 ; 5} et biais ≤ δ/4,
**si le sujet et les comparateurs ont la même dispersion d'unité bêta de corrélation intra-unité ρ, la puissance de la fiche, au pire de ces quatre cellules, vaut à n = 288 unités au moins 0,994 (ρ = 0,05), 0,970
(ρ = 0,10) et 0,847 (ρ = 0,17) au seuil 40, et au moins 0,869, 0,768 et 0,509 au seuil de référence 160 ; à n = 400 unités au moins 0,980 (seuil 40) et 0,905 (seuil 160) à ρ = 0,17.** Sans dispersion du sujet, la fiche
valait au moins 0,986 à n = 288 (v7, seuil 40, K_s = 10). Seules les tailles 288, 400, 500 et 650 sont simulées et seules les valeurs de ρ 0 ; 0,05 ; 0,10 ; 0,17 ; 0,25 ; la taille minimale pour une puissance de 0,8
est de 280 unités à ρ = 0,17 (seuil 40 ; 360 au seuil 160), avec une incertitude de graine mesurée de 2,2 % au plus de la moyenne (quatre graines, résolution 8 unités). À n = 288, la fiche est sous 0,8 au seuil 160 dès ρ = 0,10 (0,768) et au seuil 40 dès ρ = 0,25 (0,583) ; la taille se lit au pilote dans la table de lecture (ρ mesuré côté sabotage → n_h, au plus 304 au seuil 40 et 384 au seuil 160 à ρ ≤ 0,17), 400 unités par défaut. Un neuvième comparateur d'écart de contraste
0,10 ne change pas ces tailles (surcoût du n80 ≤ 16 unités) ; à écart 0,05 (SUPPOSÉ) il demande +128 à +432 unités au seuil 40. »

Chiffres derrière la phrase : 0,994, 0,970, 0,847, 0,869, 0,768, 0,509 (`resume-v8.md`, table R1, lignes `meme-rho…`, 288 unités, minorants) ; 0,980 et 0,905 (400 unités, ρ = 0,17) ; 280 et 360 (n80 pire) ; 304 et
384 (table de lecture) ; 2,2 % (§ 7) ; ≥ 0,986 (v7, GD7-05, `chiffres-v7-repris-v8-sortie.json`, bloc `fiche_par_K_s`, `logit-0` à `beta-1.0` à K_s = 10 : le minimum de ces lignes est 0,986) ; +128 et +432 (table
du § 5, écart 0,05).

## 10. Doutes restants et réserves

1. **Lois synthétiques ; ρ, c, γ et l'écart 0,05 sont des scénarios**, pas des estimations (P-9 : f_A non lue avant G1). Le ρ commun aux deux côtés (une seule κ) et le même ρ pour A et les B sont des hypothèses de la
   loi, non des constats. Un sujet moins dispersé que les comparateurs (0 < ρ_A < ρ_B) n'est pas passé (attendu plus favorable que ρ_A = ρ_B ; ρ_A = 0 : v7).
2. **Remède 3 (strates) : interprétation à contre-lire.** La portée « commune » donne zéro par construction (le contraste apparié annule déjà la difficulté commune) ; la portée « sujet » est un scénario de
   sensibilité différenciée que rien ne prouve ; l'étalonnage est exact (borne haute). Les 15 passages de strates : 13 à 288 et 400 unités, 2 avec n80.
3. **Remède 2 (copule) : un seul facteur commun** au sujet et à tous les comparateurs ; c entre sujet et comparateurs n'est pas mesurable avant G1 (§ 3.1). La corrélation de Pearson des probabilités honnêtes est
   inférieure à c (queue de la bêta à p = 0,01).
4. **Résolution de n80** : 8 unités vers 256 à 512 (1/32), donc des écarts de n80 inférieurs ne sont pas résolus ; la borne de graine de 6 % n'est ni contredite ni démontrée (§ 7).
5. **Convention d'écrêtage** : la simulation écrête δ − g après l'étalonnage par strate, le juge fixe écrête g d'abord ; dans le périmètre des passages la part de valeurs hors de [−1 ; 1] est ≤ 7,8 × 10⁻⁵ et la
   différence de puissance entre les deux conventions est nulle dans les huit sous-cas vérifiés (`verif-ebh-pole-v8-sortie.json`, bloc `ecretage_etalonnage`) ; des écarts de l'étalonnage par strate n'apparaissent
   qu'à K_h < 5 (hors périmètre) et sont expliqués dans la vérification.
6. **Refus tardif laissant un journal** : un refus survenant après l'ouverture du journal (par exemple une amplitude de strates excessive avec `--sortie`) laisserait un journal sans sortie ; le script est scellé,
   non corrigé ; aucun des 52 passages n'a été concerné (tous ont écrit sortie, journal et manifeste).
7. **Seuil 160** : borne basse de la retenue e-BH à m = 8 (non simulée) ; lecture (A) m = 2 seulement ; deux modes, une génération, α_c entier (réserves 5 à 10 de la v6, inchangées).
8. **Coûts en épisodes** : plan apparié supposé (SUPPOSÉ) ; aucun montant en argent n'est avancé.
9. **Durée** : 46 passages principaux, 5,6 h cumulées de temps mural, et 6 compléments, 0,2 h (deux à trois passages à la fois sur deux processeurs) ; le plus long, `neuf-k9-g0.05-logit1.0`, a duré 1 449 s (24,2 minutes) sous deux à trois
   processus concurrents, sous les 25 minutes ; aucun passage n'a été interrompu ni réduit : 2 000 répétitions partout.
10. **scipy** est utilisé (table des quantiles de la copule, importé dans la fonction seulement) ; la v7 n'en dépendait pas.
11. **Un écart de conduite à signaler** : j'ai lancé une fois `git --version` par mégarde au début du travail (aucune interrogation du dépôt) ; ni le script ni les lanceurs n'en lancent.
12. **Non relu par une autre main (R2)** : à regarder en premier, `_tirage_combine`, `table_quantiles_beta` et `quantile_bete_de_z` (copule), les strates (`decalages_strates`, `_rho_interne`), la branche du neuvième
    comparateur dans `tirer`, l'interprétation du remède 3, et la règle de lecture de la table du pilote.

## 11. Vérifications (R5 : cas sain et artefact)

| vérification | résultat | empreinte de la sortie |
| --- | --- | --- |
| `verif-identite-v7-v8-sortie.json` | v7 contre v8 de bout en bout, 7 cas, 57 cellules, 4 447 champs communs, 0 différence ; deux témoins négatifs décelés (graine différente : 184 différences ; ρ = 0,17 contre σ = 1,0) | `a61f6ee7…` |
| `verif-identite-gd7-v8-sortie.json` | rejeu des figures de la contre-lecture GD7 : 25 résultats, 307 champs, 0 différence ; ρ direct = ρ déduit de σ ; témoin négatif | `0ca30f6a…` |
| `verif-copule-strates-v8-sortie.json` | table de quantiles, copule (Pearson par quadrature), témoin c → 0, strates (espérances, variances, ρ total), hypothèse nulle (contraste atteignant 40 : 0,0085 brut, 0,0125 étalonné, borne de Ville 0,025), témoin négatif (+ 0,08 : 0,875) | `eae902b4…` |
| `verif-ebh-pole-v8-sortie.json` | 96 cellules aléatoires (bêta, copule, strates, neuvième comparateur, K_s = 20) contre le pôle `pari_apparie.py` (`ec6c2cf6…`) : 0 différence d'atteinte ou de retenue ; écrêtage : § 10, point 5 | `778e245a…` |
| `verif-sans-git-v8-sortie.json` | GD7-09 : analyse syntaxique, piège à sous-processus, commit déclaré | `ae4ae9dd…` |
| `essais-entrees-v8-sortie.json` | 183 essais d'entrées, 183 conformes, 144 refus nommés, 0 erreur brute | `dd4fd546…` |
| artefacts de la garde (tableau T8) | frontière et tricheur sur les 608 cellules : frontière ≤ 0,0115 (borne de Ville 0,025 au seuil 40), ≤ 0,0035 (0,00625 au seuil 160), tricheur 0,000 | `tableaux-v8-sortie.json` |

La vérification de l'écrêtage a nécessité cinq exécutions : une plantée sur un écart étalonné hors de [−1 ; 1] refusé par le juge, trois non conformes au critère initial (cellules à K_h < 5, hors périmètre), la
cinquième conforme avec un critère scindé et le périmètre vérifié à part, sans toucher au script (sorties échouées conservées hors du dossier, dans l'espace de travail).

## 12. Empreintes

Chaque fichier a son empreinte compagnon `.sha256` (vérifiée par le constructeur). Les 52 passages (sortie, journal, manifeste) sont listés avec leurs empreintes dans `manifeste-puissance-garde-delta-v8-v2.json`. Remplacés avant toute transmission, gardés (R12) : `manifeste-puissance-garde-delta-v8.json`, `rapport-v8-gabarit.md`, `construire-rapport-v8.py`.

| fichier | sha256 |
| --- | --- |
| `simulation-puissance-garde-delta-v8.py` | `4c7c93a90e0be922e839f5826488edcc0745bde17f8a5de22f3a2a41bf75f1d1` |
| `lancer-passages-v8.sh` | `8ec7fd67660e71caad1b49bd8a0869db89f8f983a1345f0270dc33dd7b948774` |
| `lancer-complements-v8.sh` | `acf8d7539e424362a1e13acf49d5e358f25a45553893725d8ae172bf8b6b9f43` |
| `lancer-verifications-v8.sh` | `8455c9d063e26074537f8a5008ce047ce915e4c2261ae7ff1dce084149d239d0` |
| `tableaux-v8.py` | `13484491786b2ca640137570be6dc13144ca440cb444ad1d1786ee7865528391` |
| `tableaux-v8.md` | `047cbac24c0feb902edc79cd2f52c024a11b96f29092c87af17e6726188ce8ed` |
| `tableaux-v8-sortie.json` | `2c30a27e1534500e5d7e16318aecf938a09910f795ef466bbf99636beb6a4834` |
| `resume-v8.py` | `c3bee3d46f86fee34be947a30d5e04c559b632af0e9748a3130f629e77038e2b` |
| `resume-v8.md` | `94b4d997626111b27a50b17e387f01e42e04bdd520f7733892a33ea61953e183` |
| `resume-v8-sortie.json` | `aa9e4d0a969b44abf3782cc205066a060459fcd975e7e9e6c3e56f6e5be626b6` |
| `incertitude-graine-n80-v8.py` | `f3875ef46d0029e7c912bbd46a656c6e3d09e05a62f4222c1be67d141efc4556` |
| `incertitude-graine-n80-v8-sortie.json` | `17a78187bb7574b52af4c2067a969adc3c394d174cfcda8ef42aa45de8c1b1b3` |
| `precision-rho-pilote-v8.py` | `edd51cd7fea353f8944e35ecc4e3e8780a690577b917a99d2fe7f6d39c1b25e5` |
| `precision-rho-pilote-v8-sortie.json` | `7e9c93e006dad9be901db21d3c4798dfb318847aa728e209cb0afec1c18da4ef` |
| `chiffres-v7-repris-v8.py` | `51bed5b6bcbc4997f57688cce31d5929e9b19a3fae643704678b82d085d30e13` |
| `chiffres-v7-repris-v8-sortie.json` | `cb16cc01e62c821224c7d4d3463bd29bba9036510eeaecc462e351711aa9ea3f` |
| `verif-identite-v7-v8.py` | `1ae2bef2d7919822b7a5c42732ba24c2bd9bbe969d5a50ad7dc2109ab0d7e0b7` |
| `verif-identite-v7-v8-sortie.json` | `a61f6ee7f2bb209ca3e3edf0c2e0faaf0889d580073a90cf27244e8bea88b443` |
| `verif-identite-gd7-v8.py` | `83334f07d8d2abe2ccccd9567f3254d19f88821f8fd243b43c49fb379f51bb39` |
| `verif-identite-gd7-v8-sortie.json` | `0ca30f6aff89947abff594851148f66013217bed307996e157966170b3cf569e` |
| `verif-copule-strates-v8.py` | `9a1c05cb498428aea4a8d6aa713a51ccc55f577886497aa9cd29d95cc7ec1e82` |
| `verif-copule-strates-v8-sortie.json` | `eae902b43a56b6ef5fc1e4c29cd2535345b0c1ac9237bea60ab5c61de25691fd` |
| `verif-ebh-pole-v8.py` | `5128f10fbaa230366aaf819e504c3f9c013ad30fc628d91b3250188e5bcefc2a` |
| `verif-ebh-pole-v8-sortie.json` | `778e245a4572effa1a1bf3c5754200da1949e508831a13a3862f3c529978d025` |
| `verif-sans-git-v8.py` | `b0a1c86647510ccadf1064b34e07d86fbdea4d380fc0ec2373085987cbc48e0d` |
| `verif-sans-git-v8-sortie.json` | `ae4ae9dd0bcf8672099e4d9dc18073ab7e463e0d2c76c1fe4763fc5eb4025eaa` |
| `essais-entrees-v8.py` | `f4f55a37b58544460da51badc49eb7eb2521f515a213cfcf6d710466fe48a324` |
| `essais-entrees-v8-sortie.json` | `dd4fd546355e8d20a94da542b5065afd0c85eb46261b0ecaae6de6144f8756b7` |
| `assembler-manifeste-v8.py` | `a2e6711e41225d214cf2a8ea4b186708aa4ff5516ce809bb0fd5d37db903cd3d` |
| `manifeste-puissance-garde-delta-v8-v2.json` | `a7dd020a734a634aca2340b403158ae1384e67bb405ba142ae364683178a2d26` |
| `manifeste-puissance-garde-delta-v8.json` | `8642b5f69b79a72e70e2f1061778e973ce50d20f0b8bea0b8f05a0a4cb6c81c1` |
| `rapport-v8-gabarit-v2.md` | `1de91fbf995e6dec948de9607023e64b2e58fe8f36dd2b9e29e7ceab28441094` |
| `rapport-v8-gabarit.md` | `540b1684bb9f5e5bee3a810210ae5e9a1f9de8466733575e3761935ba8936f1f` |
| `construire-rapport-v8-v2.py` | `abf5d4a77372a3cc2f9b2f821e0879a6bfca2035ce494eae1e903405fc9ce943` |
| `construire-rapport-v8.py` | `d9ccf63ec65180691d331ef22e11efe126e9919f8e3d78ab266ec26bf0bb7380` |
