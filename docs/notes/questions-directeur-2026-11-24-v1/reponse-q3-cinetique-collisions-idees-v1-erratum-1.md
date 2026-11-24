# Erratum 1 de la réponse à la question 3 : la cinétique chimique des collisions d'idées (v1)

- **Nature** : pièce de travail (classe C), erratum ; la pièce visée n'est pas modifiée.
- **Heure** : `2026-11-24T16:38:45Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièce visée** : `reponse-q3-cinetique-collisions-idees-v1.md` (`af126ebffbb931a959395b7b512f79cd7b35d7c0eeafd3bd0b3075a1af9083d1`).
- **Source des constats** : `contre-lecture-reponses-q1-q5-q7-q9-v1.md` (`9cefaa1fab6da2328bf99990f06ed03b4ec790c5e954e75c8209af07c68a786f`), section Q3.
- **Calcul refait** : `simulation-cinetique-barriere-v2.py` (`5167d7cbf18c9036880d709df5295bc7e073594b9b7f1db9ff8200378c7eaacb`), sortie `simulation-cinetique-barriere-v2-sortie.txt` (`dc98b08f5460a71c3a59dd9e267ffad0b0d2bfb7635cdcc11acdc3528c880cd6`), même dossier, processeur, 14 secondes, graine racine 20261124 par `numpy.random.SeedSequence` (arbre distinct de la v1). La v1 du script et sa sortie restent archivées. Tous les chiffres ci-dessous viennent de la sortie v2, parties A0, A1 et A2.

## Majeur : le terme du préfacteur qui dépend de la température est omis dans la simulation

**Texte fautif** (section 4, « Ordres de grandeur ») : « pour une barrière de 2,5 nats, 1 600 collisions donnent 2,63 ± 0,59, 6 400 donnent 2,53 ± 0,27 ; à 3,5 nats, 400 collisions ne donnent rien d'utilisable. » La section 3 (point 2) exige pourtant `ln k = ln A + m·ln T − E/T`, et la partie A de la v1 ajustait `ln A − E/T` sans le terme `m·ln T`.

**Ce que montre le calcul refait.**
- *Colinéarité* (A0) : la corrélation entre ln T et −1/T vaut 0,987 sur l'ancien plan (0,4 ; 0,7 ; 1,0 ; 1,3) et 0,962 sur un plan plus large, posé ici (0,25 ; 0,4 ; 0,7 ; 1,0 ; 1,4 ; 2,0).
- *Précision de E = 2,5 nats, ancien plan, vérité m = 0* (A1) : sans le terme, écart type asymptotique 0,56 à 1 600 collisions (Monte-Carlo 0,59), comme dans la v1 ; avec le terme, 2,96 à 1 600 (distribution à queue lourde : Monte-Carlo 9,85, écart type robuste 3,68), 1,48 à 6 400, 0,74 à 25 600. La contre-lecture avait trouvé 0,56 et 2,96 : confirmé. Pour la même précision, il faut environ (2,96/0,56)² ≈ 28 fois plus de collisions (calcul de l'auteur sur ces deux nombres).
- *Plan large, ajustement avec le terme* (A1) : écart type asymptotique 1,87 à 1 600, 0,93 à 6 400, 0,47 à 25 600 (vérité m = 0) ; 2,25, 1,12, 0,56 (vérité m = 1). La précision que la v1 annonçait à 1 600 collisions (0,59) demande donc environ 25 600 collisions sur le plan large, soit seize fois le budget.
- *Biais si le terme existe et qu'on l'omet* (A1, vérité m = 1, ajustement sans le terme) : E = 2,5 est lu 3,44 à 3,51 sur l'ancien plan, 3,80 à 3,85 sur le plan large, et ce biais ne baisse pas avec le budget (3,44 à 25 600). L'ajustement de la v1 n'est donc pas seulement optimiste : si m ≠ 0, il est faux.
- *Barrière de 3,5 nats, avec le terme* : écart type asymptotique 1,93 à 25 600 sur l'ancien plan, 1,04 (m = 0) et 1,14 (m = 1) sur le plan large. *Barrière de 1,5 nat* : 0,28 à 25 600 sur l'ancien plan, 0,16 et 0,22 sur le plan large.
- *Test du catalyseur contre le préfacteur* (A2, E₀ = 2,5, abaissement de 1 nat contre préfacteur multiplié par e, terme `m·ln T` commun aux deux bras) : le test survit, parce qu'il compare deux bras à la même température. Ancien plan : puissance 0,35 à 3 200 collisions et 0,94 à 12 800 (m = 0), 0,23 et 0,81 (m = 1) ; plan large : 0,55 et 0,99 (m = 0), 0,46 et 0,99 (m = 1) ; faux positifs entre 0,02 et 0,06. Les chiffres de la v1 (0,35 et 0,96) restent du bon ordre si m = 0.
- *Hypothèse qui porte ce dernier point, non calculée ici* : le catalyseur ne change pas la dépendance en température du préfacteur. S'il la change (terme présence × ln T), ce terme est colinéaire au terme présence × 1/T à 0,987 ou 0,962, et la séparation s'effondre.

**Correction.** Remplacer le paragraphe « Ordres de grandeur » par : « Avec la forme exigée en section 3 (`ln A + m·ln T − E/T`), une barrière de 2,5 nats se lit à ± 0,74 avec 25 600 collisions sur quatre températures de 0,4 à 1,3, à ± 0,47 sur six températures de 0,25 à 2,0 (plan posé) ; omettre le terme, s'il existe (m = 1), biaise la lecture d'environ un nat. Le test du catalyseur contre le préfacteur garde une puissance de 0,81 à 0,99 à 12 800 collisions si le catalyseur ne change pas m. » Dans le « plan croisé » de la même section, lire « six températures au moins » au lieu de « quatre températures ». En section 3, point 2, « au moins trois températures » laisse le modèle à trois paramètres exactement déterminé, sans degré de liberté pour en éprouver la forme : lire « au moins cinq ».

**Réserve sur le plan large.** La borne haute (T = 2,0) est posée. La section 4 elle-même relève que l'incohérence croît avec la température (réaction parasite [8]) : la température la plus haute utilisable se mesure sur le proposeur avant tout plan.

**Conséquence sur le verdict.** « Garder en partie » (confiance 0,6) est maintenu. La phrase « dans l'organisme, la température existe : la barrière s'y mesure, le catalyseur s'y sépare du préfacteur » se lit : « la barrière s'y mesure, mais avec environ seize à vingt-huit fois plus de collisions que la v1 ne le disait, sur une plage de températures plus large, et seulement si la forme du préfacteur est juste ; le catalyseur s'y sépare du préfacteur à budget voisin de celui de la v1, s'il ne change pas la dépendance du préfacteur en température ». La course de dose-réponse, non lancée, demande un devis refait sur ces budgets.

## Mineurs

1. **Forme `m·ln T`.** Texte : « le préfacteur dépend de T (normalisation du softmax, comme le facteur en T d'Eyring [2]), d'où la forme `ln k = ln A + m·ln T − E/T` ». La normalisation du softmax (log de la somme des exponentielles des logits divisés par T) n'a pas la forme d'une puissance de T. *Correction* : « forme empruntée à Eyring, posée, à éprouver ». Piste, non calculée : sur un proposeur ouvert dont on lit les probabilités, la normalisation de chaque pas se calcule à chaque température ; l'entrer comme décalage remplacerait la forme posée.
2. **Premier ordre de la voie catalytique** (section 2, prédiction 2). Texte : « le terme de Fable en est le premier ordre, exact seulement si `β_c = β` ». *Correction* : « exact seulement si `β_c = β` et si la voie catalytique porte aussi le facteur `e^{δP}` » ; la forme s'écrit alors `λ = p⁰·[e^{βZ+δP} + ψ·Σ_m c_m h_a(m) h_b(m)·e^{β_c Z + δP}]`.
3. **Symboles.** Le coefficient catalytique κ devient ψ, la constante de rencontre κ₀ devient k₀ (`k_D = k₀·n_a^{m_a}·n_b^{m_b}·C_ab`), pour que κ désigne seulement la part des conflits dans tout le dossier : voir `erratum-notations-kappa-et-hypergraphe-v1.md`.
4. **Renvoi de Tria et collègues** (section 5 et référence 18). Texte : « [18, éq. (1), p. 3] » et « PDF lu, éq. (1), p. 3 ». *Correction* : « p. 3, légende de la figure 1 » ; le numéro d'équation n'a pas été retrouvé.

Aucun de ces mineurs ne change le verdict.
