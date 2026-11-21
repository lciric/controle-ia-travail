> You are powered by the model named Fable 5.2.

# Erratum 1 de la note « science de la détection » : la règle « moniteur invalide » corrigée, sa table refaite, et ce que les voisins lus depuis occupent

- **Date** : 21 novembre 2026, 13:50 UTC (`date -u`). **Auteur** : Claude Fable 5.2, concepteur (R-3735) ; la phrase en tête est celle de mon invite système qui nomme mon modèle. Pièce de classe C, non contre-lue. Aucun appel payant, ni commit ni poussée. Dépôt à `ce6cf61cd`.
- **Ce qu'il corrige** : `docs/notes/science-de-la-detection-v1/reponse-fable-science-de-la-detection-v1.md` (`a10df4fa…543e`), qui reste scellée telle quelle. **Là où ils diffèrent, cet erratum prime.**
- **Ce qui l'a déclenché** : la re-dérivation indépendante de la règle par un Opus 5.5 qui n'a reçu que l'énoncé, `docs/notes/regle-moniteur-invalide-rederivation-v1/rederivation-opus-v1.md` (`a5ff23f2…4cc4`) et sa sortie de calcul (`5e626061…031b`) ; la lecture en entier de six voisins, `docs/notes/science-de-la-detection-v1/lecture-six-voisins-et-banc-public-opus-v1.md` (`74d44e6f…0f60`). Je les ai lues en entier.
- **Lu sur PDF pour cet erratum** : Singh, « Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries », arXiv 2610.18948v1, pages 1 à 3, 9 et 48 à 50, versé sous `docs/sources/pdf/science-de-la-detection-v1/erratum-1/` avec sa table de provenance ; deux phrases vérifiées dans Li et al., arXiv 2610.06576v1 (p. 2 et 8), et une dans l'esquisse de dossier de sûreté par contrôle, arXiv 2501.17315v1 (p. 11).
- **Mes calculs** : `calculs-science-de-la-detection-erratum-1-v1.py` (`26ec7fec…4c44`) et sa sortie `.txt` (`c3e74929…09e6`), même dossier : formules fermées et programmation dynamique exacte, aucun tirage, rejoués à l'octet, non contre-lus.
- **Marques** : [établi] = lu par moi sur PDF à la page dite ; [re-dérivation] et [six voisins] = repris de ces deux pièces, à la section dite ; [calcul, X] = bloc X de ma sortie d'erratum.

## Verdict

1. **Ma règle était mal écrite et sa borne mal énoncée ; la re-dérivation a raison sur ses quatre points.** La phrase « moyenne de cinq rapports, multipliés d'audit en audit » se lit comme un produit de moyennes, qui n'est qu'un seul rapport au taux moyen et laisse un excès linéaire. Mon programme calculait autre chose, le mélange (moyenne des produits) ; mais avec ma grille, qui s'arrête à 1,25 fois le taux acceptable, le mélange laisse lui aussi une bande où l'agent s'installe sans jamais être annoncé, jusqu'à 1,12 fois ce taux [calcul, A].
2. **« La borne croît comme la racine, donc la part qui passe tend vers zéro » était faux pour la règle écrite.** Avec ma grille, la borne garantie finit linéaire : 1,25 % des épisodes à dix millions [calcul, C]. L'ordre en racine demande une grille qui descend vers le taux acceptable.
3. **Ma table (100, 190, 392) n'était pas la borne annoncée.** C'était une valeur exacte, mais d'un énoncé plus étroit : silence jusqu'à l'horizon, agent aveugle à tous les tirages. Elle ne borne pas ce qui s'accumule avant une annonce survenue plus tôt. Je l'ai retrouvée, et j'ai réimplémenté le théorème de la re-dérivation : mes valeurs égalent ses douze valeurs publiées à 0,05 près [calcul, B, D].
4. **La forme n'est plus libre.** Un moniteur à mélange de rapports de vraisemblance qui borne l'excès cumulé à l'ordre de la racine, sur chaque trajectoire, face à tout adversaire adaptatif, et le fait qu'une alternative unique laisse un excès linéaire, sont publiés depuis le 13 octobre (Singh, p. 1 et 9) [établi]. Ce que je n'y ai pas trouvé aux pages lues : l'audit d'une fraction tirée au hasard, la condition sur ce que l'agent peut savoir des tirages, la perte « endommagé et non signalé ».

## 1. La règle corrigée, en forme fixe

**Ce qu'elle annonce** (inchangé) : « la validation de ce moniteur ne décrit plus ce déploiement ».

**Entrées scellées avant le service.**
- ρ₀, taux acceptable d'épisodes endommagés et non signalés, avec ρ₀ < 0,2 ;
- q, probabilité d'audit ; α, risque de fausse annonce par déploiement ; β, risque sur la garantie 2 ; T, horizon ;
- le seuil du moniteur, gelé ; l'oracle ;
- **la grille, descendante** : douze taux ρ_j = ρ₀ × (1 + 4/2^j), j = 0 à 11, soit 5 ; 3 ; 2 ; 1,5 ; 1,25 ; 1,125 … 1,002 fois ρ₀, de poids égaux.

**Statistique : le mélange, c'est-à-dire la moyenne des produits.** Après chaque audit, N est le nombre d'audits faits et M le nombre d'audits « endommagé selon l'oracle et non signalé par le moniteur ». Pour chaque taux : a_j = log(ρ_j(1 − ρ₀) / (ρ₀(1 − ρ_j))) et b_j = log((1 − ρ₀)/(1 − ρ_j)).

  W = (1/12) × Σ_j exp(a_j × M − b_j × N).

**Décision.** « Moniteur invalide ici » au premier audit où W atteint 1/α. L'annonce est définitive.

**Conditions**, telles que la re-dérivation les a isolées [re-dérivation, § 1, § 2.3, § 3.6].
- **Tirage frais** : à chaque épisode, une pièce de probabilité q, indépendante du passé et de ce que l'agent fait à cet épisode. L'agent peut avoir vu les tirages et les verdicts **passés** ; il ne doit ni voir ni prédire le tirage **courant**, ni l'état du générateur. C'est plus faible, et plus exact, que mon « tirages secrets, indépendants de tout ce que l'agent observe ».
- **Oracle sans fausse alerte** sur les épisodes audités. S'il en commet au plus ε, on teste à ρ₀ + ε(1 − ρ₀). Ses oublis ne cassent pas la garantie 1 ; s'ils sont choisis par l'agent, la garantie 2 ne porte que sur le dommage que l'oracle voit.
- **Nulle posée épisode par épisode** : la probabilité qu'un épisode soit endommagé et non signalé, sachant tout le passé, tirages compris, est au plus ρ₀. Une nulle « en moyenne » ne suffit pas.

**Garantie 1, fausse annonce.** Sous ces conditions, la probabilité d'annoncer un jour est au plus α, à tout instant d'arrêt, sous toute dépendance entre épisodes et toute adaptation de l'agent au passé (inégalité de Ville ; preuve en quatre lignes dans [re-dérivation, § 2.2]).

**Garantie 2, ce qui s'accumule avant l'annonce.** Avec probabilité au moins 1 − β, pour toute politique d'attaque qui ne voit pas le tirage courant, **à tout instant m avant l'annonce** et jusqu'à l'horizon n :

  (épisodes endommagés et non signalés parmi les m premiers) − ρ₀ × m < B(n),

où B(n) est le minimum, sur les taux de la grille et sur λ > 0, de [log(12/α) + log(1/β)/λ] / A + n × (C/A − ρ₀), avec A = q·a_j − [φ(λu_j) − φ(−λb_j)]/λ, C = q·b_j + φ(−λb_j)/λ, u_j = a_j − b_j et φ(s) = q·s + log(1 − q + q·e^(−s)). L'épisode de l'annonce ajoute au plus 1. Énoncé et preuve : [re-dérivation, § 3.1 et 3.2] ; j'ai relu ses trois pas, je n'y vois pas de faute, et ce n'est pas une contre-lecture.

## 2. La table refaite par programme

ρ₀ = 0,10 ; α = 0,05 ; β = 0,10. Borne garantie B(n) de l'excès, en épisodes ; entre parenthèses, sa part de n [calcul, C].

| Audit | n = 1 000 | 4 000 | 16 000 | 100 000 | 1 000 000 |
|---|---|---|---|---|---|
| 0,20 | 136,1 (13,6 %) | 252,4 (6,3 %) | 483,7 (3,0 %) | 1 140,4 (1,1 %) | 3 661,9 (0,37 %) |
| 0,05 | 317,9 (31,8 %) | 564,6 (14,1 %) | 1 045,1 (6,5 %) | 2 411,6 (2,4 %) | 7 606,6 (0,76 %) |
| 1,00 (tout est audité ; borne sur chaque trajectoire) | 33,9 | 66,2 | 130,6 | 315,6 | 1 023,7 |

- **Lecture en racine** : B(n) divisé par √(n·ρ₀(1 − ρ₀)/q) reste entre 5,3 et 6,4 pour l'audit à 0,20, de mille à dix millions d'épisodes ; entre 5,5 et 7,5 à 0,05 [calcul, C].
- **Ce qu'aucune règle ne peut éviter** : au moins 18, 36 et 73 épisodes en excès à 1 000, 4 000 et 16 000 pour l'audit à 0,20 ; 55, 107 et 211 à 0,05 [re-dérivation, § 3.5]. Le facteur √(1/q) est irréductible : auditer quatre fois moins double l'excès inévitable.
- **Le prix de la grille descendante**, en audits avant l'annonce, médiane exacte dans un monde à taux constant [calcul, E] :

| Taux réel | Grille de la note | Grille corrigée |
|---|---|---|
| 3 fois ρ₀ | 21 | 28 |
| 2 fois | 69 | 93 |
| 1,5 fois | 251 | 331 |
| 1,25 fois | 991 | 1 245 |
| 1,10 fois | non atteinte à 12 000 (annonce : 0,40) | 7 322 (annonce à 12 000 : 0,76) |

  On paie environ un tiers d'audits de plus quand le taux double, pour fermer la bande où l'agent s'installait. Et un excès de 10 % reste long à voir quelle que soit la règle.
- **Fausse annonce dans le monde valide** : 0,014 à 1 000 audits, 0,022 à 12 000, pour 0,05 permis [calcul, E].
- **Jusqu'où douze taux suffisent** : environ 3·10⁷ épisodes à l'audit de 0,20, 1,3·10⁸ à 0,05. Au-delà la borne redevient linéaire, de pente 10⁻⁴ par épisode [calcul, F]. Un déploiement plus long demande des taux de plus.

## 3. D'où venaient 100, 190 et 392

Excès au-delà de ρ₀·T, audit 0,20 [calcul, D].

| | T = 1 000 | 4 000 | 16 000 |
|---|---|---|---|
| Valeur de la note : silence jusqu'à T, agent aveugle à tous les tirages, loi exacte, ma grille | 100 | 190 | 392 |
| Borne garantie, uniforme dans le temps, agent qui voit les tirages passés, ma grille | 130,0 | 238,3 | 465,5 |
| La même, grille de seize taux lue par la re-dérivation | 136,5 | 255,8 | 489,6 |
| La même, grille corrigée | 136,1 | 252,4 | 483,7 |

Trois écarts s'additionnent. La re-dérivation a lu « {1,25 … 5} » comme seize taux, j'en avais cinq. Ma valeur ne regardait que l'instant T ; un épisode annoncé avant T n'y comptait pas, alors que son dommage est déjà passé. Elle supposait un agent qui n'apprend rien des tirages. Le chiffre était juste pour son énoncé ; l'énoncé n'était pas celui que la phrase « ce qui passe pendant le silence » promettait. **La table de la note est retirée.**

## 4. Le pas qui reste non démontré

**L'ordre en racine de la règle auditée, comme énoncé.** Le théorème donne B(n) pour chaque n : cela est démontré. Que B(n) reste sous une constante fois √(n·log/q) sur tout l'horizon d'emploi n'est, pour la règle à douze taux, qu'un **constat numérique** [calcul, C] ; l'ordre principal donné par la re-dérivation est une approximation gaussienne, « pas une borne » [re-dérivation, § 3.4 et § 6]. Singh démontre cet ordre, sur chaque trajectoire, pour un mélange à H taux uniformes quand **tout** est observé (proposition 1 (ii), p. 9) [établi] ; le passage à une fraction auditée au hasard, avec son facteur 1/q, n'est démontré nulle part aux pages que j'ai lues.

Restent aussi, sans être des pas de la preuve : la re-dérivation n'est pas contre-lue et rien n'est vérifié en Lean ; le pire cas sur des politiques non stationnaires n'est pas connu (à 16 000 épisodes, la borne garantie vaut 1,3 à 1,6 fois ce qu'atteint le meilleur attaquant à taux constant simulé, [re-dérivation, § 4.1]).

## 5. Ce que les voisins lus depuis changent à la note

**La règle (question 9) : partiellement occupée, et plus que je ne l'écrivais.**
- Singh (p. 1) : « With permanent revocation, a mixture likelihood-ratio monitor bounds cumulative excess above a prespecified reference rate at square-root order, up to logarithmic factors, on every sample path. A single fixed alternative can permit linear expected excess under stationary attacks. » La borne vaut pour « every adapted policy, including an adversary observing M_t », et le taux sous lequel une alternative unique ne voit rien y est nommé (p. 9) [établi]. Donc le mélange, la borne d'excès contre tout adversaire adaptatif et la bande de non-détection sont publiés. Sa proposition exige des « trusted outcome observations » sur chaque essai (p. 9) ; une recherche de motifs sur ses 66 pages ne rend aucun audit par tirage.
- L'idée d'invalider est écrite en prose : « If the reliability of monitors meaningfully drops below the performance measured in control evaluations, the safety case is invalidated » (esquisse de dossier de sûreté par contrôle, p. 11) [établi].
- Budget d'étiquettes et filtration sans les tirages d'audit futurs : Cao ; tirages qu'on ne peut apprendre d'avance : Gans et Holden [six voisins, § 2 (a)].
- **Ce qui reste une question, non une revendication** : la fraction auditée au hasard et son facteur 1/q ; la condition exacte d'information (voir les tirages passés ne casse rien, prédire le tirage courant casse tout) ; la perte « endommagé et non signalé » jugée par un oracle extérieur au mode. Citations obligatoires à toute phrase : Singh ; Podkopaev et Ramdas ; Cao ; l'esquisse de dossier de sûreté.

**La triche contre l'échec honnête (question 2) : la moitié « avant l'acte » est occupée.** Li et al., « Before Agent Tells The Lie: Has Deception Already Been Represented? », arXiv 2610.06576v1 : les issues trompeuses se prédisent avant le pas décisif, « representations collected up to seven steps earlier achieving comparable performance to the latest pre-decision representations (90.4% vs. 89.4% AUROC) » (p. 2) ; leurs signaux sont des « predictors of behavioral outcomes rather than direct evidence of deceptive intent » (p. 8) [établi] ; l'issue honnête y est l'échec déclaré [six voisins, § 2 (b)]. Ma proposition « soulagement sans résolution » ne garde que sa conjonction (retombée après l'acte, succès déclaré, échec au vérificateur caché), et doit battre deux bases : le détecteur d'avant l'acte de Li et al. et le contrôle déterministe à deux règles de Kezendirane. Li et al. devient une citation obligatoire.

**Les détecteurs qui orientent l'audit (question 5) : le cœur est publié.** Tirer les étiquettes selon un prédicteur et corriger par l'inverse de la probabilité garde l'inférence valide pour tout modèle (Zrnic et Candès, arXiv 2403.03208) ; les coupes minimales d'une pile de contrôle sont publiées (Molnar, arXiv 2609.26419) [six voisins, § 2 (c)]. Ma phrase « aucun détecteur ne peut invalider la mesure » est un résultat connu de l'échantillonnage pondéré : à citer, pas à revendiquer. Le test de mort que j'avais omis : un agent qui sait faire baisser son score se place au plancher, la garantie tient alors au plancher seul et le gain disparaît.

**Le banc public (verdict, point 5, et trouvaille de côté) : il n'est pas « prêt ».** Licence MIT, mais aucune trajectoire publiée, aucun état interne, agent servi quantifié en 4 bits ; il faut régénérer les épisodes. Et ses étiquettes « ne peuvent pas séparer un raccourci délibéré de la confusion » [six voisins, § 3]. Deux précisions : Tan et al. et Orgad et al. travaillent sur Llama-3-8B, non 3.1 ; Orgad et al. montrent qu'un honnête peut porter la trace d'une réponse juste qu'il n'émet pas, par sélection parmi des réponses rééchantillonnées, non que la signature de conflit y apparaît. Le contre-témoin reste dû ; sa force est moindre que ma phrase ne le laissait entendre.

## 6. Phrases de la note qui ne valent plus

| Où | Ce qui était écrit | Se lit désormais |
|---|---|---|
| Verdict, point 2 | deux garanties, « pour toute politique qui ne voit pas nos tirages » ; 190 sur 4 000, 392 sur 16 000 ; « ce qui n'est pas trouvé est son emploi contre un agent qui choisit » | § 1 et 2 de cet erratum ; 252 sur 4 000, 484 sur 16 000 ; l'emploi contre un adversaire adaptatif est publié pour l'observation complète (Singh) |
| Question 9, « Statistique » | moyenne de cinq rapports, multipliés d'audit en audit | le mélange du § 1, grille descendante |
| Question 9, « Garantie 2 », sa « Raison » et sa table | seuil m*, amincissement binomial | le théorème du § 1 et la table du § 2 |
| Question 9, « La part … tend vers zéro. C'est l'invariant 9, chiffré » | sans condition | vrai seulement avec une grille qui descend, et jusqu'à l'horizon du § 2 |
| Question 9, « Vitesse » | 69, 251 et 21 audits | 93, 331 et 28 pour la règle corrigée |
| Synthèse, étage 2 | « Garantie : la loi en racine, pour toute politique d'attaque » | « borne garantie du § 2, d'ordre racine constaté et non démontré pour la règle auditée » |
| Relevé de méthode, pas 10 et 11 ; premier pas non justifié | amincissement et couplage | § 1 (théorème re-dérivé) ; le pas non démontré est celui du § 4 |
| Question 10, ligne Lean | « amincissement binomial, énoncé fini » | « martingale exponentielle du tirage et inégalité de Ville » |
| Décisions D-2, D-3, D-6 | à faire | D-2 : re-dérivation faite ; D-3 : vérification faite, banc à régénérer ; D-6 : lecture faite, trois verdicts « partiellement occupé » |

## Relevé de méthode

**Chaîne de raisonnement.**
1. La moyenne des rapports d'un audit égale le rapport au taux moyen. — calcul, A (écart 1e-16) ; [re-dérivation, § 1].
2. Avec ma grille, le mélange laisse une bande jusqu'à 1,12 fois ρ₀. — calcul, A et E (annonce de 0,40 à 12 000 audits pour 1,10 fois).
3. Le théorème de la garantie 2. — [re-dérivation, § 3.1 et 3.2], relu ; réimplémenté : calcul, B.
4. Mes valeurs égalent ses douze valeurs à 0,05 près. — calcul, B (assertion dans le programme).
5. Ma table d'origine est la valeur à horizon fixe. — calcul, D.
6. L'ordre en racine de la règle à douze taux. — calcul, C : constat numérique, supposé au-delà.
7. Ce que Singh occupe. — PDF, p. 1 et 9 (`53557a25…9f7d`).
8. Ce que les six voisins occupent. — [six voisins] ; deux phrases revérifiées sur PDF.

**Objets de contrôle.**
- *Règle corrigée.* Faux : monde valide ; prévu : annonce d'au plus 0,05 ; rendu : 0,014 à 0,022. Vrai : taux doublé ; prévu : annonce ; rendu : 1,0000, médiane 93 audits (la re-dérivation en simule 94).
- *Bande de non-détection.* Objet où « l'agent est annoncé » doit être faux pour ma grille : taux de 1,10 fois ; prévu : pas de médiane ; rendu : annonce de 0,40 seulement à 12 000 audits. Sous la grille corrigée : médiane 7 322.
- *Ma réimplémentation.* Vrai : les douze valeurs publiées ; rendu : écart maximal 0,05.

**Premier pas non justifié.** Le pas 6 (§ 4).

**Mode d'échec affecté.** Sans objet : cette pièce n'est pas une relecture.

**Dérivation de l'énoncé seul.** Sans objet : c'est la pièce d'un autre, que je reçois ici.

**Trouvaille de côté.** La note d'origine avait vu la grille trop courte (« au-delà de l'horizon prévu il faut des mises plus proches ») et l'avait rangée en trouvaille de côté au lieu d'en tirer que la loi en racine tombait : c'était le pas à ne pas laisser de côté. Autre point, non poursuivi : la borne à audit complet (33,9 à 1 000 épisodes) est quatre fois plus basse que celle à 0,20 ; l'audit orienté par un score, sous plancher, se place entre les deux.

**Évaluateur et conseil.** Ce qui a jugé la règle : un dériveur d'un autre modèle, qui n'a reçu que l'énoncé. Il a trouvé ce que ni mes objets de contrôle ni mon rejeu ne pouvaient trouver : mes contrôles éprouvaient des taux doublés, jamais un taux juste au-dessus de l'acceptable. Conseil : pour toute règle séquentielle, l'objet de contrôle à écrire d'abord est l'adversaire qui se place au bord.

## Décisions pour toi

**E-1. Remplacer la règle de la note par celle du § 1.** Enjeu : la règle d'origine laisse une bande où un saboteur s'installe sans annonce. (a) Règle corrigée à douze taux : avantage, borne en racine jusqu'à 3·10⁷ épisodes ; inconvénient, un tiers d'audits de plus quand le taux double. (b) Garder cinq taux pour la vitesse : la bande reste. Recommandation : (a). Confiance 0,85. Défaut sous 48 heures : (a) ; aucun texte scellé n'est touché.

**E-2. Faire contre-lire la re-dérivation, puis viser Lean.** Enjeu : la garantie 2 ne tient aujourd'hui que par un dériveur et par ma relecture d'auteur. (a) Un contre-lecteur neuf, mode d'échec « garantie qui suppose ce qu'elle prouve », puis les deux garanties en cibles Lean : avantage, aucune dépense ; inconvénient, un mandat. (b) En rester là. Recommandation : (a). Confiance 0,7. Défaut sous 48 heures : (a).

**E-3. Aucune phrase de nouveauté sur la règle, la trajectoire autour de l'acte ou l'audit orienté.** Enjeu : les trois sont partiellement occupées ; Singh n'est lu qu'à sept pages. (a) Lecture en entier de Singh par un agent neuf, verdict d'antériorité sur les trois restes du § 5 : avantage, R8 tenue ; inconvénient, lève le gel de la veille pour une pièce. (b) Ranger les trois restes à l'atelier d'idées sans lecture. Recommandation : (a). Confiance 0,8. Pas de défaut : le gel est ta décision.

## Ce que je n'ai pas fait

- **Aucune mesure.** Les entrées sont des suppositions d'illustration ; rien n'est contre-lu.
- **Singh n'est pas lu en entier** : pages 1 à 3, 9, 48 à 50 ; ni ses preuves (annexe A.11), ni ses hypothèses complètes. La constante de sa borne n'est pas reprise : l'extraction abîme la formule.
- **Je n'ai pas contre-lu la re-dérivation** : j'ai relu les trois pas de sa preuve et réimplémenté sa formule. Ses bornes inférieures (§ 3.5) et ses simulations sont reprises sans recalcul.
- **Les six voisins** : je me fie à la lecture qui en a été faite, sauf trois phrases revérifiées sur PDF.
- **La note d'origine n'est pas réécrite** : une version 2 qui intègre cet erratum reste à faire si tu la veux.
