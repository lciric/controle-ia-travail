# Contre-lecture finale du brouillon 4 — épreuve semi-réelle des méthodes d'identification — v1

- Auteur : sous-agent Sonnet 5.5 neuf (`claude-sonnet-5-5`), canal `canal/conv-audit-n04`. N'a écrit ni les brouillons 1 à 4, ni les fiches, ni l'erratum, ni le script de règles, ni la synthèse v2 de la question 6. **Réserve d'indépendance** : modèle différent d'Opus (exigence de R2 satisfaite), mais même modèle que l'auteur de la contre-lecture CS2 (brouillon 2) dont ce rapport vérifie le traitement, même dépôt, même chaîne de travail. Fable (auteur de l'erratum et de la synthèse v2) n'est pas intervenu ici.
- Date (UTC) : 2026-10-31, vers 10:45 (relevé `date -u` : 10:42 à la fin de la lecture).
- Règles appliquées : R2 (contre-lecture), R3, R4, R5, R7 (page citée), R1 (aucune lecture de données).
- Interdits respectés : rien lu sous `donnees/` (ni sur disque ni par git) ; aucune moisson ; aucun commit ; aucun `.sha256` écrit ; aucun fichier existant modifié ; seul fichier créé dans le dépôt : ce rapport. **Écarts à signaler** : (1) `git fetch -q origin` pour lire `main` (met à jour les références distantes de `.git`, aucun fichier de l'arbre) ; (2) en plus du script de règles et du validateur (`python3 -I`, dossier temporaire vide), j'ai exécuté trois petits scripts de contre-lecture hors dépôt (`/tmp/cl4work/`, reproduits en annexe, graines par `numpy.random.SeedSequence`), un `pdftotext` en lecture seule sur quatre PDF (Khemakhem p. 5–6, Azoulay p. 17 et 28, Iaria p. 23, Locatello p. 6) et une copie temporaire du brouillon pour tester le validateur (supprimée).
- Fichiers lus et empreintes (SHA-256, recalculées ; chaque compagnon `.sha256` concorde) :
  - brouillon 4 `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon4.md` `30f45ac5af140913bdd3fa34af3bdd2322850f6e052e5d856f5c1ce9e35081d3` (845 lignes, lu en entier) ;
  - script `…calcul-regles-identification-semi-reel-v1-brouillon4.py` `096e6890370715879dcd5a7bd8786339d190c407a7c2e1648f252247da05d4cf` (lu en entier) et sortie `…brouillon4.sortie.txt` `484bc4d27bcbd8b8daa0a89c9e5b16988c661fe0c82065eae00bd511290f6ea1` ;
  - brouillon 3 `1a229998…` (sortie `a668a8e1…` utilisée pour le `diff`), brouillon 2 `f61ae4c0…`, contre-lecture CS2 `a539dc13…` (lue pour le format et la continuité) ;
  - synthèse v2 de la question 6 (`git show origin/main:docs/notes/bisociation-litterature-reelle-v1/collisionneur-question-6-v1/synthese-question-6-v2.md`) `ff3b19e3fb21a24329cd403efdf57db22423ce8630386425e3ac07c1207f05cf` (lue en entier, empreinte conforme à celle du brouillon) ; synthèse v2 du lot bisociation `23c2888d…` (§ (iv) décision 1, lue) ; lignes R-878 et R-884 de `registres/decisions.md` de `origin/main` ;
  - fiches `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` `63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79` (§ 1 à § 9 lus) et erratum `fa7e1d96…` ; gabarit `8cad4371…` ; `src/controle_ia/prereg.py` `3b2e3ee5…`.
  - Les 27 empreintes de 64 caractères citées par le brouillon : 19 retrouvées exactement sur disque ou dans `main` (dont toutes celles de la lignée de calcul, des fiches, de l'erratum et des cinq PDF cités), 8 renvoient à des pièces absentes de ce poste (réponses 5 et 6, relecture 6, question et faits de la question 6, `decisions.md` vivant, v1 de la synthèse) : non vérifiées, non contredites.
- Non lus : `donnees/`, la moisson, les cellules du collisionneur, les PDF hors pages citées.

Échelle : **bloquant** = interdit le gel ; **majeur** = à corriger avant le gel (le texte ou la conception change) ; **moyen** = à corriger ou à écrire comme choix assumé ; **mineur** = à corriger en repassant sur le texte.

---

## Verdict

**Présentable après corrections.** Le brouillon 4 est sérieux, la lignée de calcul est exacte (rejeu octet pour octet, chiffres du texte conformes à la sortie, aucun chiffre de littérature faux) et les deux étages latentes / flèche sont tenus sans glissement résiduel. Mais quatre défauts de conception ne se corrigent pas par un simple remplacement de marqueurs : l'affectation « au hasard » ne l'est pas marginalement (κ), la rétrodiction inversée n'est pas « sans fuite » pour M2 ni pour les méthodes qui retiennent le leurre, la puissance de l'étape d'estimation est surestimée (et la règle S11 peut être inatteignable), et le plancher de validation S13 est incompatible avec la puissance supposée. Aucun bloquant. Les décisions DL-1 à DL-11 et D1 à D3 sont bien ouvertes (marqueurs), mais cinq d'entre elles sont déjà câblées dans le corps du texte.

**Compte : 0 bloquant, 4 majeurs, 9 moyens, 6 mineurs (19 constats).**

**Les trois plus importants** : CS4-01 (κ confond C avec l'environnement × bloc, y compris sous « R »), CS4-02 (la rétrodiction n'est pas un test sans fuite : collisionneur L, série renversée de M2), CS4-03 (puissance jointe de l'étape d'estimation : 0,16 à 0,88 par monde au mieux selon la base et l'effet de plan, contre 0,85 à 1,00 annoncé ; la règle S11 passe presque jamais si l'effet de plan vaut 2).

---

## A. Réponse aux neuf points demandés

| # | Point | Résultat |
|---|---|---|
| 1 | Fidélité de la synthèse v2 (latentes / causes ; estimer / identifier) | **Tenue pour l'essentiel.** Aucune table du volet B ne qualifie une flèche ; les titres de tables, les lignes 3 et 8 de la Table Bθ, la table Estimation-θ et la lecture combinée sont corrects ; les emprunts (Q6 § (a), (b), (c), (d), (e)) sont fidèles, y compris les divergences écrites (nk + 1 contre « 2k », hasard + 5 points, rang). Quatre glissements de détail : CS4-11. |
| 2 | Six garde-fous de R-878 | **Présents tous les six, appliqués inégalement.** GF2 et GF5 (volet B) et GF6 gouvernent des lignes de décision ; GF1, GF3, GF4 et GF5 (volet A) sont descriptifs ou formels ; GF2 a des défauts de conception (CS4-02) ; GF6 affirme plus qu'il ne fait (CS4-07, CS4-04). Voir CS4-08. |
| 3 | Chiffres de littérature (R7) contre les fiches | **Aucun chiffre faux.** Tous les chiffres des tables « Suites » et de l'Hypothèse se retrouvent dans les fiches § 1 à § 9 à la page citée, corrigés par l'erratum pour Iaria (−0,217 colonne 1 ; −0,222 colonne 3 ; −85 %) et Azoulay (−0,092 → 8,79 % ; −0,086 → 8,2 %). Vérifié en plus sur PDF : Iaria p. 23 (−0,217 (0,033), −0,222 (0,025)), Azoulay p. 28 (note : 1−exp(−0,092) = 8,79 %, colonne 1a) et p. 17 (8,2 %, « trois à quatre ans »), Khemakhem p. 5–6 (nk + 1 ; théorème 2, (2.i), (2.ii)), Locatello p. 6 (37 %, 59 %). Deux détails absents des fiches : CS4-19. |
| 4 | Rejeu du script ; chiffres = sortie ; budget | **Conforme.** Deux rejeux `python3 -I` depuis un dossier vide : sorties identiques entre elles et à `…sortie.txt` (`484bc4d2…`) ; `diff` des § 1 à § 20 contre la sortie du brouillon 3 : vide ; numpy 2.5.3. Budget recomputé à la main : mondes 1 300 + 250 + 200 + 120 = **1 870** ; calcul 6 835 min = **113,9 h** ; validation 2,17 h ; gardes 2,5 h ; total **118,6 h** ; tous les « (M § k) » du texte que j'ai recoupés (§ 1 à § 4, § 6, § 7, § 9, § 11, § 15 à § 17, § 19 à § 23, § 25) concordent. Les temps unitaires restent SUPPOSÉS (CS4-15). |
| 5 | Plan / seuils / lignes ; première espèce ; puissance ; moitiés disjointes | Table A et tables du volet B cohérentes entre elles et avec S9 à S11. **Défauts** : CS4-01, CS4-02, CS4-03, CS4-04, CS4-05, CS4-07. Perte de puissance estimée par simulation : CS4-03. |
| 6 | Correction « effets fixes de u » | **Juste dans son principe** : en B-θ le seul chemin de confusion d'une latente passe par u, les effets fixes le ferment, la version sans effets fixes en descriptif le montre. **Coût non compté** : les effets fixes retirent 46 % de la variance de l'effet (statistique × 0,74), M § 23 l'ignore (CS4-03). Estimateur de variance : CS4-05. |
| 7 | R3, R4, R5 | R3 : pas de signe visé, une formulation à reprendre (CS4-10). R4 : symétrie bonne pour le volet A et la Table Bθ, absente pour la table Estimation-θ (CS4-10). R5 : paires sain / artefact présentes et bien choisies pour 33 gardes, **absentes pour 9 lignes de la liste d'arrêt** malgré l'affirmation contraire (CS4-09). |
| 8 | DL-1 à DL-11, D1 à D3 | **Ouvertes** : 11 « État : À REMPLIR » (DL), 3 « À REMPLIR au gel » (D1 à D3), aucun défaut appliqué, recommandations identiques à celles du brouillon 3 sauf DL-2, DL-5, DL-7 (déclaré). Nuance : CS4-12. |
| 9 | Validateur `problemes` | **Conforme** : exactement 2 problèmes, « Seuil » et « Contre-lecture ». Effet de masquage vérifié sur copie : une fois ces deux sections remplies, le validateur ne signale plus qu'un seul problème, « marqueur À REMPLIR restant hors des sections exigées » (16 occurrences dans « Résumé », 1 dans « Ce qui change »), dont 3 phrases de prose qui bloqueraient encore le scellement après les décisions de Lazar : CS4-14. |

---

## B. Constats

### Majeurs

**CS4-01 — Majeur — L'affectation « au hasard » (R) ne l'est que conditionnellement à (environnement × bloc) : κ confond C avec la sortie, y compris sous R.**
- Lignes : S4 (l. 408) « π_0 = 0,10 …, multipliée par κ ∈ {0,5 ; 1 ; 1,5} attribué cycliquement aux couples (environnement, bloc de cinq ans) ; R : logit π = logit(π_0 κ) » ; Hypothèse (l. 208) « Sous affectation au hasard (R, R2⁻), régression et effet coïncident » ; Table A, lignes 4 à 6 (l. 685–687) ; S14 (m) (l. 458) « C n'a aucun lien avec le passé sous R, seule une fuite le permet » ; prédiction rétrodite (l. 305).
- Constat : sous R, la probabilité de traitement vaut 0,05 / 0,10 / 0,15 selon le couple (environnement, bloc). La sortie réelle Y⁰ a, elle, un niveau qui dépend de l'environnement et du bloc (la synthèse et le brouillon le supposent eux-mêmes : « inflation des citations par décennie, normes par sous-domaine », NT1). Donc C est corrélé à Y⁺ et à Y⁻ à travers (environnement × bloc), sans aucun effet et sans fuite. Les candidates (S, D, A, g(Y)) ne contiennent ni l'environnement ni le bloc ; ils n'en captent qu'une part, et pas de façon monotone puisque κ cycle. Ordre de grandeur (raisonnement, non calculé, dépend des données) : avec 3 niveaux de π d'écart-type ≈ 0,04 pour un écart-type de C de 0,3 (corrélation C–niveau ≈ 0,13), et si le niveau (environnement × bloc) explique 10 % de la variance de g(Y⁺), la corrélation induite peut atteindre ≈ 0,04, à comparer à la corrélation causale de C avec g(Y⁺) de 0,035 (β = 0,2) à 0,07 (β = 0,4) déduite de M § 8. La confusion est donc du même ordre que l'effet planté « fort ».
- Conséquences : (a) l'erreur C en R0 (ligne 4), l'erreur L et C⁰ sous R (lignes 5 et 6) peuvent être non nominales pour des raisons de conception, et disqualifier toutes les méthodes sans qu'aucune ne soit en défaut ; (b) la phrase « sous R, régression et effet coïncident » est vraie conditionnellement à κ, non marginalement ; (c) la prémisse de S14 (m) (« seule une fuite le permet ») est fausse pour la même raison (voir aussi CS4-02) ; (d) l'audit de randomisation de la validation (« équilibre de S, D, A entre C = 1 et C = 0 sous R », l. 651) ne contrôle pas l'équilibre en (environnement × bloc).
- Correction proposée : au choix, (i) ajouter l'indicateur de (environnement × bloc), ou la propension nominale π_0 κ, aux candidates de toutes les méthodes (c'est une grandeur observée de l'analyste ; M1 garde ses environnements) et l'écrire dans la liste des variables candidates (Métrique l. 342) ; (ii) ou imposer κ = 1 sous R et R2⁻ et ne garder κ que dans D1 (qui est précisément la condition « décalage de mécanisme ») ; dans les deux cas, ajouter à la validation un booléen « équilibre de (environnement × bloc) entre C = 1 et C = 0 sous R » et une garde R5 (sain : C indépendant de la sortie passée à (environnement × bloc) fixé ; artefact : κ corrélé au niveau de la sortie). Réécrire « au hasard » en « au hasard à (environnement × bloc) fixé » si (i).

**CS4-02 — Majeur — La rétrodiction inversée (GF2, S23, S14 (m)) n'est pas un test « sans fuite » : collisionneur L pour T1, M2 et M3, conditionnement sur le futur pour M2.**
- Lignes : GF2 (l. 199), Métrique (l. 363), Plan § 5 (l. 582), S14 (m) (l. 458), prédiction (l. 305), garde « rétrodiction » (l. 812).
- Constat 1 (M2). La variante rétrodite de M2 « renverse la série de chaque paire dans le temps ». PCMCI conditionne, pour tester le lien C → g(Y), sur les parents estimés de chaque variable, qui sont ses retards dans la série renversée, c'est-à-dire, en temps d'origine, des valeurs **postérieures**. Avec τ_max = 3 et un effet planté C_t → Y_{t+2}, le jeu de conditionnement de Y_{t'} contient Y_{t'+3}, enfant de C_{t'+1} et de Y_{t'} (persistance de la sortie réelle) : un collisionneur. Le conditionner ouvre un chemin C_{t'+1} ↔ Y_{t'} qui n'existe pas sans conditionnement. Corrélation partielle induite de l'ordre de ρ(C_{t'+1}, Y_{t'+3}) × ρ(Y_{t'}, Y_{t'+3}) ≈ 0,1 × 0,3 = 0,03 (ordres de grandeur supposés), au-dessus du seuil de détection 2,576/√27 000 ≈ 0,016 à α_M2 = 0,01. La variante ne mesure alors plus « l'effet de C sur le passé » mais un artefact de conditionnement, croissant avec β.
- Constat 2 (L). Le leurre est un collisionneur C → L ← H → sortie, et H agit aussi sur la sortie passée de la fenêtre. Les méthodes qui conditionnent sur L (T1 : toutes les candidates ; M3 ; M2 en tant que variable) obtiennent une association entre C et Y⁻ à L fixé, sans fuite (le sens est négatif : pour L = 1, C = 0 exige un H élevé). Sous R2, R3, le signe exigé est positif et la règle « trouve » la compte rarement ; **sous R2⁻, où le signe exigé est négatif, cette association de collisionneur est précisément du bon signe et peut être comptée « trouve en rétrodiction »**. La prédiction « ≤ 0,10 sous R2, R3 et R2⁻, confiance 0,8 » (l. 305) et la phrase de S14 (m) « seule une fuite le permet » sont donc des paris, non des certitudes ; avec CS4-01 ils forment trois mécanismes sans fuite du même effet.
- Conséquences : S14 (m) peut sonner pour M2, T1 ou M3 sans faute de code ; S23 peut retirer à tort REC_R⁻(M) ou REC_X(M) ; la garde R5 « rétrodiction » (l. 812, « base jouet sous affectation au hasard, C sans lien avec le passé ») est **muette** si la base jouet n'a ni effet planté vers l'avant, ni persistance de la sortie, ni leurre collisionneur : elle passera sur un cas qui ne contient pas le mécanisme fautif.
- Correction proposée : (i) pour M2, remplacer la série renversée par un **décalage vers le passé de la sortie** (Ỹ_t = Y_{t−τ_max−1}, avec ses propres retards antérieurs à t seulement) : tout ce que PCMCI conditionne est alors antérieur à C_t ; (ii) pour toutes les méthodes, écrire que la rétrodiction se calcule **avec les mêmes candidates, L comprise**, et donc que le « nominal » du recouvrement rétrodit est la valeur de la base jouet et non zéro ; (iii) enrichir la garde R5 : base jouet avec effet vers l'avant, persistance de la sortie, H, L ; sain : recouvrement rétrodit au niveau mesuré sur une version de la même base sans effet ; artefact : fuite d'une année postérieure ; (iv) réécrire S14 (m) : « recouvrement rétrodit sous R supérieur de plus de 0,10 à celui de la base jouet de la garde », au lieu de ≥ 0,20 absolu.

**CS4-03 — Majeur — Puissance de l'étape d'estimation (S11, S21, M § 23) : l'approximation est trop favorable de plusieurs façons ; la règle « au moins 37 sur 50 » peut être inatteignable.**
- Lignes : S21 (l. 494) « puissance 0,85 à 1,00 au seuil 0,01 » ; S11 (l. 443–444) ; PB-M4θ (l. 315) « trouve dans 0,5 à 0,95 des mondes » ; Table Estimation-θ (l. 723–728) ; script § 23.
- Constat : M § 23 calcule la puissance du **seul test sur E₂**, avec les hypothèses suivantes qui jouent toutes dans le même sens : (a) pas d'effets fixes de u, alors que S21 les exige : la part de variance de 2Φ(z̃₁) qui reste à l'intérieur d'une valeur de u vaut 0,54 en moyenne (p10 0,48, p90 0,61 ; annexe B), donc la statistique est multipliée par 0,74 ; (b) pas de sélection de k̂ : « trouve l'effet » exige k̂ = k* choisi sur E₁ (n ≈ 1 100 paires-années, un échantillon plus petit que E₂) **et** significativité sur E₂ ; (c) années « utilisables » P − 3 (réf. incluse) alors que u₁ (choisie sur toutes les bases sauf la plus petite, M § 15) n'existe qu'après la référence : P − 8 années, soit 5 au lieu de 10 pour P = 13, 8 au lieu de 13 pour P = 16, 12 au lieu de 17 pour P = 20 (voir CS4-13) ; (d) l'effet de plan est inconnu (1 ou 2 arbitraires) ; (e) l'iVAE est supposé retrouver z₁ parfaitement (borne haute).
- Simulation (annexe A ; `SeedSequence(20261031, spawn_key=(901,))`, 250 mondes par ligne, écart-type de Monte-Carlo ≈ 0,03 ; représentation parfaite ẑ = z, 3 environnements × 990 paires, E = 40 %, moitiés de niches et d'années, sortie = bruit de variance 3 + effets de z₁ à t − 1, t, t + 1) :

| Base (N = 45 niches / env.) | n(E₁) / n(E₂) | « trouve » (effet de plan 1) | « trouve » (effet de plan 2) | Règle S11 (≥ 37/50) tenue, plan 1 / plan 2 |
|---|---|---|---|---|
| P = 12, u₂ (hypothèse de M § 23) | 1 111 / 1 521 | 0,76 | 0,46 | 0,70 / 0,0001 |
| P = 13, u₁ | 555 / 911 | 0,47 | 0,16 | 0,0001 / 0,00 |
| P = 16, u₁ | 1 106 / 1 209 | 0,63 | 0,28 | 0,07 / 0,00 |
| P = 20, u₁ | 1 664 / 1 821 | 0,88 | 0,58 | 0,998 / 0,014 |

  (Probabilités de la règle déduites de la loi binomiale à 50 mondes avec la part vraie indiquée, cohérentes avec M § 16 : 0,18 pour 0,67 ; 0,987 pour 0,85.) Le comptage de paires-années de M § 23 est exact (1 521 contre 1 533 annoncés pour P = 12). Le contrôle de fausse détection (sans effet réel, mêmes réglages) donne 0,02 à l'effet de plan 1 : le niveau nominal est tenu.
- Conséquences : « puissance 0,85 à 1,00 » (S21) est une puissance du test seul sans effets fixes ni sélection ; la prédiction PB-M4θ « 0,5 à 0,95 » est large mais sa moitié haute ne tient que pour une base longue **et** un effet de plan proche de 1 ; sur une base ordinaire la ligne 2 de la Table Estimation-θ (« latente identifiée, effet non retrouvé ») tombera pour manque de puissance et sera lue comme « non qualifiée » sans que rien ne la distingue d'un échec du réseau.
- Correction proposée : (i) recalculer M § 23 avec effets fixes (facteur 0,74), la sélection de k̂ et les années réellement utilisables par définition de u, et publier la table ci-dessus ou son équivalent exact ; (ii) écrire un booléen de **puissance de l'étape** calculé à la validation de la base (statistique approchée sur E₂ avec effets fixes ≥ 3,5, par exemple) : s'il est faux, la table Estimation-θ se lit « non concluant (puissance) » et non « non qualifiée » ; (iii) soit relever E ou le nombre de mondes (ce qui se paie en temps, S15), soit rendre la table Estimation-θ descriptive (DL-5 option 1 bis) ; (iv) réécrire l'effet de plan comme paramètre mesuré sur les 5 mondes B-θ de validation (booléen seulement) ; (v) retirer « 0,85 à 1,00 » de S21.

**CS4-04 — Majeur — Le plancher de validation S13 est incompatible avec la puissance supposée par S3, S8 et M § 23 (GF6 non tenu).**
- Lignes : S13 (l. 453) « au moins 15 niches et 100 paires par environnement, 12 années » ; S1 (l. 393) ; S8 (l. 428) « au plus 1 000 paires par environnement » ; S3 raison (l. 404) « 30 000 paires-années » ; S21 raison (l. 494) ; script § 8 et § 23 (`PAIRES = 3000`).
- Constat : 1 000 paires par environnement exigent **au moins 45 niches** (45 × 44 / 2 = 990) ; 15 niches donnent 105 paires. M § 23 imprime pourtant des lignes « N = 15 niches par environnement » avec 3 000 paires, et S21 raison les cite pour « la base minimale (P = 12) » : 1 533–1 600 paires-années pour E₂. Avec 15 niches, 315 paires au total, E₂ ≈ 0,4 × 315 × 0,267 × 5 ≈ 170 paires-années et E₁ ≈ 100 : sous le seuil de 200, tous les mondes sont exclus pour l'étape (mon essai : l'appel `run("E", 15, 12, 1, 9, reps)`, à ajouter à la fin de l'annexe A, rend « aucun monde utilisable (E1 ou E2 < 200 paires-années) » ; EXCLθ). Pour le volet A, au plancher de S13 (300 paires, fenêtre de 4 ans pour P = 12 : 1 200 paires-années), la statistique de M § 8 vaut 2,4 pour β = 0,4 et 1,2 pour β = 0,2, contre 12,0 et 6,0 annoncés pour 30 000 paires-années : aucune méthode ne peut passer la règle de recouvrement (BB ≥ 0,70) aux conditions R2, R3 ; S14 (b) sonne, le run est dépensé pour un « non concluant ». Même avec 3 000 paires la fenêtre courte (P = 12 : 4 ans) donne 12 000 paires-années, statistique 3,8 pour β = 0,2 et 7,6 pour β = 0,4 (3,33/√n par construction de M § 8).
- Correction proposée : (i) remplacer le plancher de S13 par un plancher de **puissance** : paires-années de la fenêtre de plantation ≥ n_min (par exemple 20 000, tel que β = 0,2 donne une statistique ≥ 4,5 selon M § 8 corrigé) et nombre de niches ≥ 46 ou nombre de paires ≥ 1 000 par environnement ; booléen unique, imprimé comme les autres ; (ii) ajouter à M § 8 et M § 23 la dépendance explicite à la longueur de la fenêtre et au nombre de paires, avec une table par base type ; (iii) écrire dans « n'autorise pas » que sur une base au plancher l'épreuve est non concluante par construction.

### Moyens

**CS4-05 — Moyen — « Erreurs groupées à deux voies (les deux niches de la paire) » n'est pas un estimateur de données dyadiques.**
- Lignes : Métrique (l. 382), S21 (l. 493), Plan § 5 (l. 585), nœud ouvert 5 (f) (l. 114), garde (l. 811).
- Constat : une paire (i, j) appartient aux deux grappes de niche i et j ; l'estimateur à deux voies de `statsmodels` suppose deux partitions croisées (deux colonnes de groupes), pas deux appartenances à un même ensemble de grappes. Si l'on assigne i à la première voie et j à la seconde, la covariance entre (a, b) et (c, a) (même niche a, rangs différents dans le couple) est ignorée ; l'ordre « i < j » dans le couple est arbitraire. L'estimateur adapté est un estimateur dyadique (sommation des scores sur toutes les paires qui partagent une niche). (Références de mémoire, SUPPOSÉES, non opposables : Fafchamps et Gubert 2007 ; Cameron et Miller 2014 ; Aronow, Samii et Assenova 2015.) De plus, le nombre de grappes est modeste (≈ 22 niches par moitié et par environnement pour N = 45), et le biais de sous-estimation de l'erreur type à peu de grappes aggrave l'erreur de première espèce.
- Pourquoi c'est une affaire de préenregistrement et non de code : l'estimateur détermine le niveau de FAUXθ (S11, au plus 2 sur 50) et la garde R5 de M § 17 est calibrée sur « dimensions synthétiques sans entraînement » avec une structure de grappes de son choix ; elle ne valide pas l'estimateur du run.
- Correction proposée : écrire l'estimateur (dyadique, avec correction à peu de grappes) dans Plan § 5 ; garde R5 : base jouet à covariance dyadique connue (calcul à la main), estimateur dyadique égal ; estimateur à deux voies naïf : plus petit, refusé ; ajouter au budget de validation un contrôle de niveau de FAUXθ par permutation de z₁ entre niches.

**CS4-06 — Moyen — S22 compare l'exactitude du classifieur à 1/U : le niveau du hasard est la fréquence de la classe majoritaire, pas 1/U.**
- Lignes : Métrique (l. 373 (a)), S22 (l. 498), S14 (n) (l. 458), M § 24.
- Constat : les classes de u sont des couples (environnement × année) ; leur taille est proportionnelle au nombre de paires de l'environnement, qui varie de 100 (plancher) à 1 000 (plafond). Un classifieur sans information (Bθc) atteint la fréquence de la classe majoritaire. Exemple : 3 environnements à 1 000 / 200 / 100 paires et P = 13 (u₁, U = 24 classes, 8 années) : la plus grande classe pèse 1 000/1 300/8 = **0,096**, au-dessus du seuil 1/24 + 0,05 = **0,092** de P2 : P2 « fausse » dans Bθc sans aucun défaut de code, S14 (n) sonne, la Table Bθ est « non concluante » jusqu'à l'audit. En sens inverse, P1 en Bθv est exigé « ≥ hasard + 0,05 » alors que la barre devrait être la fréquence majoritaire + 0,05.
- Correction proposée : définir le hasard comme la fréquence de la plus grande classe de u dans la base de validation (calculée sans lire autre chose que des effectifs, booléen seulement), ou utiliser l'exactitude équilibrée ; adapter M § 24 et la garde (sain : classes équilibrées ; artefact : classes déséquilibrées avec classifieur constant).

**CS4-07 — Moyen — GF6 « toutes les règles de lecture ont leur caractéristique opératoire » est inexact ; la chaîne complète de la Table A n'est pas chiffrée.**
- Lignes : GF6 (l. 203) ; Plan § 9 (l. 644) ; S9 « intervention » (l. 433) ; S10 (l. 438) ; S12 (l. 448) ; S14 (a), (e) ; S17.
- Constat : sont sans caractéristique opératoire : la règle d'intervention (médiane ≤ 0,30, borne haute ≤ 0,40), S10 (ROB_H, PRU_H), S12 (invariance, domination, popularité), S17 (reconnu : « sans littérature »), S14 (a), (e). Deux exemples chiffrés (annexe C pour S12, M § 2, § 3 et § 9 pour la chaîne) : (i) **S12** compare des recouvrements sur 30 mondes, sur 13 conditions et 2 variantes (14 à 26 comparaisons par méthode), seuil 0,10 : une méthode dont 3 % des mondes basculent dans chaque sens entre échelles (élagage, seuils d'effet total « 0,05 standardisé » appliqués à une variante brute…) est déclassée « artefact d'échelle » (ligne 3, avant toutes les autres) avec une probabilité de **0,14 (14 comparaisons) à 0,25 (26)** ; à 5 %, 0,42 à 0,64 ; (ii) **la chaîne**: pour une méthode au recouvrement vrai 0,85 et aux erreurs vraies 0,05, la conjonction des lignes 4 à 7bis tient avec 0,818 (REC, M § 9) × 0,822 (erreur C, M § 2) × 0,829 (erreurs L et C⁰, M § 3) = **0,557**, avant INT, ART, J, S17, S23. Les règles sont calculées une à une, jamais ensemble ; le texte du dépôt dit pourtant (R4, GF6) que la puissance est préalable.
- Correction proposée : ajouter un § 26 au script : probabilité de passer les lignes 3 à 14 pour une méthode de référence nommée (recouvrement 0,90, erreurs 0,03, bascule d'échelle 0,02), et le taux de déclassement à tort de S12 ; réécrire GF6 en « les règles chiffrées sont : … ; non chiffrées : … » ; pour S12, réduire le nombre de comparaisons (par exemple décider sur les conditions R2, R3, O2, O3 seulement) ou élargir la tolérance à 0,15.

**CS4-08 — Moyen — GF1, GF3, GF4 et GF5 (volet A) sont appliqués de façon descriptive ou formelle ; la liste des six « obligatoires » est tenue en lettre, moins en effet.**
- Lignes : GF1 (l. 198), GF3 (l. 200), GF4 (l. 201), GF5 (l. 202) ; Résumé 6 (l. 16) ; Tables A et Bθ.
- Constat : (a) **GF1** « sans objet pour la vérité » est défendable (la vérité est une plantation) ; mais la covariable D (citations reçues) contient **mécaniquement** les œuvres-ponts réelles et plantées, qui citent i et j ; le chemin C → D est mesuré et la boucle C → D → C sous O est écrite, mais rien dans les tables de décision ne dépend de ce canal. (b) **GF3** : D_amp et D3 amputé sont descriptifs (30 mondes, O2 et O3, T1, M2, M3 seulement ; M1 absent) ; aucune ligne de la Table A ne lit D_amp. (c) **GF4** : T0 prédit « un effet nul, erreur d'intervention 1,00 exactement » ; une règle ≤ 0,30 bat donc T0 par construction pour toute méthode qui retrouve un effet de bon signe ; ce n'est pas un bras de comparaison qui contraint (le second plancher, T1, est une candidate, jamais un comparateur dans une règle). En volet B, au contraire, le test conditionnel à (S, D, A, g(Y)) est réel. (d) **GF5 (volet A)** : la disjonction par niche est descriptive.
- Ce n'est pas une faute (le brouillon l'écrit et en donne la raison pour GF1 et GF5 (b)), mais R-878 dit « obligatoires » : Lazar doit voir que trois sur six ne gouvernent aucune ligne.
- Correction proposée : une phrase dans le Résumé 6 (« gouvernent une ligne : GF2, GF5 volet B, GF6 ; descriptifs : GF1, GF3, GF5 volet A ; formel : GF4 volet A ») ; ajouter une décision DL-12 (D_amp décisionnel pour T1, M1, M2, M3 en O, ou statu quo) plutôt que de la laisser implicite ; pour GF4, ajouter une comparaison réelle (gain de la méthode sur T0 sur l'erreur d'intervention, plancher de 0,30 sur l'écart).

**CS4-09 — Moyen — Gardes R5 absentes pour 9 lignes de la liste d'arrêt, contre l'affirmation « chaque ligne … qui porte sur le code a sa garde ».**
- Lignes : liste d'arrêt (l. 758–789), affirmation (l. 791), gardes (l. 792–827).
- Constat : sans garde « sain / artefact » : « balayage statique : `except` autour d'un appel de méthode qui rend une valeur par défaut » (le cœur de R5, « aucun repli silencieux »), « valeur non numérique ou division par zéro », « échec de convergence > 5 % », « exclusion > 2 % », « nombre de mondes ≠ S7 / plusieurs invocations », « manifeste scellé après le premier fichier de résultats », « racine différente, numpy < 1.25 » (la garde « graines » ne teste que la réutilisation de clé), « version de bibliothèque ou empreinte du code différentes », « appel de modèle, instance payante », « préconditions de S22 imprimées autrement que par booléens ». La garde « B-θ identifiable » a pour artefact un contrôle négatif (assumé, l. 802).
- Correction proposée : une garde par ligne, ou une phrase qui sépare les lignes à garde testée des lignes contrôlées par le lecteur de la porte (R13), avec la liste des deux ensembles.

**CS4-10 — Moyen — R4/R3 : la table Estimation-θ n'a ni déclencheur d'audit ni ligne « puissance » ; la raison du changement de S11 est mal formulée.**
- Lignes : S14 (l. 458–459) ; Table Estimation-θ (l. 723–728) ; S11 raison (l. 444) « L'ancienne règle d'effet … contredisait la prédiction de l'auteur ».
- Constat : S14 couvre le « trop mauvais » de la Table Bθ ((l)) mais pas celui de l'étape d'estimation (ligne 2 : latente identifiée, effet non retrouvé) ni de B-hors ; pas de « trop propre » non plus (50 sur 50, 0 sur 50 exactement) pour cette table, alors que (e) le prévoit pour le volet A. Avec CS4-03, un échec de la ligne 2 est le résultat le plus probable sur une base ordinaire et il est lu comme « non qualifiée » sans audit. Côté R3 : changer une règle parce qu'elle « contredisait la prédiction de l'auteur » règle le seuil sur le pari plutôt que sur une alternative nommée ; ici ce n'est pas un signe visé (rien n'a été lu), mais la formulation doit être « puissance 0,89 contre une part vraie de 0,80 nommée » (M § 16), pas « cohérent avec ma prédiction ».
- Correction proposée : déclencheur S14 (o) « étape d'estimation : TROUVEθ faux alors que la Table Bθ est à la ligne 8, ou 0/50 et 50/50 exactement » ; ligne « non concluant (puissance) » (CS4-03 (ii)) ; reformuler la raison de S11.

**CS4-11 — Moyen — Fidélité à la synthèse v2 : quatre glissements de détail.**
- (a) **S16** (l. 469) : « C'est, dans ce banc, le dispositif que la synthèse v2 retient comme le seul qui sépare estimer d'identifier ». La synthèse (Q6 § Verdict, § (d)) le retient **pour les courses** ; la transposition au banc (affectation biaisée O et H, jugement contre le contrefactuel simulé sur I) est de l'auteur, comme le disent l'Hypothèse (l. 208) et le Résumé 2 (l. 12). S16 se contredit. Corriger : « transposition de l'auteur du dispositif des courses ».
- (b) **W4** (l. 232), Résumé 3 (l. 13), Q8 : « le jumeau C⁰ réalise l'intervention fantôme ». L'intervention fantôme de la synthèse est un traitement **inscrit au journal et non délivré** (« d = 7 inscrit au journal mais d = 0 envoyé ») : la même variable, sans effet. Dans le banc, c'est le monde β = 0 (R0, O0, H0 : C observé, aucun effet) qui la réalise ; C⁰ est un placebo apparié tiré indépendamment, ce qui est autre chose (il teste l'attribution d'un effet à une variable de même loi d'affectation). Corriger : « les mondes β = 0 réalisent l'intervention fantôme ; C⁰ est un placebo apparié ».
- (c) **H-SR-A** (l. 208) : « si et seulement si l'hypothèse dont dépend son résultat d'identifiabilité est satisfaite » ; la synthèse dit que l'identification est une propriété du couple classe × loi sous hypothèses, non l'équivalence ; T1 et T2 n'ont aucune hypothèse d'identification et « retrouvent » C sous R. Remplacer par « si l'hypothèse … est satisfaite, et seulement sous l'une des hypothèses écrites pour lui ».
- (d) **Intégration § 2** (l. 834) : « MCorr < 0,5 sur ≥ 50 % des sources » (espèce B) « ≈ notre règle d'identification de S11 » : l'une compte des sources, l'autre des mondes ; ce n'est pas la même chose et la règle de B n'est pas « moins exigeante » dans le même sens. Écrire « non comparables ».
- Table A, lignes 11 à 14 (« qualifiée pour la gradation 2 », seules lignes qui « qualifient pour identifier ») : l'identification est jugée sur **un** mécanisme additif, linéaire à un retard, sur **un** ensemble I ; le brouillon l'écrit pour les autres limites (n'autorise pas) mais pas pour celle-ci. Ajouter une ligne dans « Ce que l'épreuve n'autorise pas ».

**CS4-12 — Moyen — Décisions « ouvertes » au sens du marqueur, mais cinq sont déjà câblées dans le corps du texte ; le budget présuppose DL-3 et DL-11.**
- Lignes : DL-2 (l. 33–39), DL-4, DL-5 (l. 53–59), DL-6, DL-8 ; Métrique (l. 372, 382) ; S18 ; S19 (l. 484) ; S7 (l. 423) ; S15 (l. 463).
- Constat : DL-1, DL-3, DL-9, DL-10, DL-11 sont écrits **conditionnellement** dans les tables et les seuils (« si DL-9 = option 1 », etc.). Pour DL-2 (graines), DL-5 (coupe et effets fixes), DL-8 (échelle de u), et en pratique DL-4 et DL-6, le corps du texte (Métrique, S18, S19, S21, tables) applique la recommandation sans variante : choisir autrement exige une version nouvelle (R12), pas le remplacement d'un marqueur. De plus S7 (1 870 mondes) et S15 (118,6 h) présupposent DL-3 = option 1 (R2⁻ de décision, 100 mondes) et DL-11 = option 1 (D5, 50 mondes) sans le dire : « Total : 1 870 mondes (DL-1 option 2, DL-10 option 1) ».
- Aucune décision n'est prise par défaut ; la conformité est formelle. Correction proposée : une ligne par décision « si l'option choisie n'est pas la recommandation : sections à réécrire = … » ; table de budget par combinaison (DL-1 × DL-3 × DL-10 × DL-11) ; ou accepter explicitement que le gel porte sur la recommandation, sauf demande contraire de Lazar.

**CS4-13 — Moyen — B-θ : fenêtre de plantation et années de référence non écrites ; u₁ et M § 23 ne comptent pas les mêmes années.**
- Lignes : W5θ (l. 235), Plan § 4 (l. 565), S2 (l. 398) « référence = les 5 premières années (…; aucune plantation du volet A) », S19 (l. 484), Métrique (l. 372) « années utilisables (celles où Y⁺ est défini) ».
- Constat : en B-θ, les z sont tirés « par paire-année » et les œuvres-ponts de z₁ plantées « au retard ℓ », sans dire sur quelles années. Si l'on plante dans les années de référence, σ_e (calculé « avant toute plantation ») et les covariables de référence ne sont plus celles de S2 ; si l'on ne plante pas, u₂ (qui « inclut les années de référence ») n'a pas de sens pour ces années et u₁ n'a pas de u pour elles. M § 23 compte P − 3 années, ce qui suppose la plantation dès l'année 1 (cohérent avec u₂ seul, pas avec u₁ : CS4-03 (c)).
- Correction proposée : écrire « B-θ plante sur toutes les années de la fenêtre de plantation (6e année à P − τ_max) et sur elles seules » (ou l'inverse), adapter u₁, u₂, u₃ et M § 15 : u = (environnement × année de la fenêtre), compté en conséquence ; M § 23 en dépend (le nombre de valeurs de u₁ passe de 21 à 12 pour 3 environnements et P = 12 : la base minimale tombe alors à u₂ puis u₃).

### Mineurs

**CS4-14 — Mineur — Le marqueur littéral « À REMPLIR » figure dans trois phrases de prose qui bloqueront le scellement après les décisions de Lazar ; le validateur masque ce défaut aujourd'hui.**
- Lignes : 20 (« toutes ouvertes (« À REMPLIR ») »), 24 (« Chaque décision porte « État : À REMPLIR » »), 157 (« DL-1 à DL-9 portent « État : À REMPLIR » », qui oublie en outre DL-10 et DL-11).
- Constat (vérifié sur copie temporaire, supprimée) : `problemes` renvoie aujourd'hui exactement deux problèmes (Seuil, Contre-lecture), ce qui est le comportement attendu ; une fois ces deux sections remplies, il renvoie le seul « marqueur À REMPLIR restant hors des sections exigées ». Les occurrences légitimes (11 DL, D1 à D3, ligne « Contre-lecture 2 ») disparaîtront quand Lazar tranchera ; ces trois phrases non.
- Correction proposée : écrire « marqueur de gel » ou « marqueur littéral du validateur » dans ces trois phrases ; garder « À REMPLIR » seulement dans les champs « État » et « Valeur ». Au passage, le tableau « Ce qui change » est inutile dans la version scellée (l. 134–190, 161–190 « Historique »).

**CS4-15 — Mineur — Budget : temps unitaires non ancrés ; le calendrier jusqu'à G0 n'est pas chiffré.**
- Lignes : S15 (l. 463), Intégration § 8 (c) (l. 840), DL-2 (l. 39).
- Constat : 1,5 minute pour un monde du volet A (qui exécute T0, T1 avec validation croisée en 5 plis et permutations répétées 10 fois sur 8 variables, T2, M1 sur 128 sous-ensembles, M2/PCMCI en « jeux de données multiples », M3/DirectLiNGAM sur 8 variables et ≈ 27 000 lignes, plus le contrefactuel et la recomputation de S, D, A, g(Y)), et 1,0 minute pour une variante qui relance six méthodes, sont plausibles pour un ordre de grandeur mais ne sont ancrés sur rien. La tolérance de 1,26 à 1,58 est honnête ; la réduction minimale reste à 94,9 h, sans toucher aux conditions de décision. Il manque seulement une date : écriture du code, gardes, validation (20 mondes), contre-lecture du code, puis 6,25 jours de calcul continus avant fin novembre 2026 ; aujourd'hui, 31 octobre.
- Correction proposée : un tableau de calendrier de l'auteur du code (jours ouvrés), à soumettre à Lazar avec DL-2 ; c'est déjà dit en une phrase, le chiffrer.

**CS4-16 — Mineur — T2b : la prédiction PA-T2b (0,3 à 0,9) suppose |corr(C, Y⁺)| > |corr(X, C)|, ce que M § 8 contredit.**
- Lignes : PA-T2b (l. 297), Métrique T2b (l. 348), S17 (l. 473).
- Constat : sous O, corr(C, popularité) ≈ 0,24 à 0,34 (calcul direct : prévalence 0,07 à 0,19) et corr(X, C) ≈ 0,2 pour X = S ou D ; la corrélation causale de C avec g(Y⁺) vaut 0,035 (β = 0,2) à 0,07 (β = 0,4) (M § 8), plus un terme de confusion par la popularité (Matthieu, SUPPOSÉ). Si la confusion est faible, T2b oriente la chaîne de travers quel que soit β, o_ch ≈ 0, et S17 reste inerte. Sans conséquence sur les tables (direction prudente), mais la prédiction et la recommandation de DL-9 (« mesure le motif là où il peut exister ») sont fragiles.
- Correction proposée : abaisser la confiance de PA-T2b, ou écrire que S17 peut être inerte par construction.

**CS4-17 — Mineur — Vocabulaire du gabarit et définitions mortes.**
- Le gabarit demande une table « issue observée → verdict (confirmé, réfuté, non concluant) » ; les tables disent « qualifiée / non qualifiée / oui sous hypothèse ». Ajouter une colonne de correspondance (par exemple : non qualifiée = réfuté ; qualifiée = confirmé).
- `REC_H(M)` et `INT_H(M)` sont définis (l. 673) mais aucune ligne de la Table A ne les utilise (les lignes 11 à 14 emploient ERR_H, ROB_H, PRU_H). Les retirer ou les employer.

**CS4-18 — Mineur — Validations croisées de T0 et T1 non disjointes par niche et par période (GF5 (c)).**
- Lignes : Plan § 5 (l. 570–571), GF5 (c) (l. 202).
- Constat : « ajustement croisé en 5 plis », « validation croisée en 5 plis » sans dire comment les plis sont formés. S'ils coupent par ligne (paire-année), l'importance de variables persistantes (S, D, A, g(Y)) est gonflée par des niches communes entre plis ; l'importance de C (indépendant par paire-année) l'est peu, mais la sonde de bruit et la barre « 9 répétitions sur 10 » en dépendent.
- Correction proposée : plis par paire (au moins) et le dire.

**CS4-19 — Mineur — R7 : deux détails ne sont ni dans les fiches ni dans l'erratum.**
- Lignes : Hypothèse (l. 219) « −0,217 (0,033), colonne (1) du tableau IV » ; « 8,79 % de baisse selon la note du tableau III (colonne 1a) ».
- Constat : l'écart-type 0,033 et la colonne 1a viennent de la contre-lecture CS2 ; je les ai revérifiés sur PDF (Iaria p. 23 : « −0.217*** (0.033) » colonne (1), « −0.222*** (0.025) » colonne (3) ; Azoulay p. 28 : « (1−exp[−0.092])=8.79 % », colonnes (1a)/(1b) ; p. 17 : « 8.2 % », « column 2b » pour 1b). Ils sont exacts. Écrire « vérifié par CS2 et CS4 sur PDF » plutôt que de laisser croire qu'ils viennent de l'erratum. Reisach : « fiche § 1, p. 8, énoncé 6 » pour v = 1/2 : l'énoncé 6 est donné p. 7 (tableau 1) et p. 8 (figure 1) ; sans importance.

---

## C. Points à ne pas toucher (vérifiés, tenus)

- Lignée de calcul : rejeu, `diff`, budget, chiffres (point 4).
- Deux étages latentes / flèche : aucune table du volet B ne qualifie une flèche ; la lecture combinée et « n'autorise pas » le disent ; le score r̃ ne décide jamais d'une flèche.
- Correction « effets fixes de u » : juste dans son principe (point 6) ; la fausse détection nominale est tenue (0,02 à l'effet de plan 1 dans ma simulation à effet nul).
- Constante de variabilité nk + 1 maintenue contre « 2k, 2k + 1 » de la synthèse : lue sur Khemakhem p. 5 ; divergence écrite.
- Pas de nouveau chiffre de littérature par rapport au brouillon 3 ; erratum cité avec les fiches.
- DL-10 option 1 recommandée avec raisons ; D4 de R-884 hors texte.

---

## D. Traitement attendu

Pour chaque CS4-xx : accepté, refusé et pourquoi, dans l'entrée « Contre-lecture 2 » de la section Contre-lecture du brouillon suivant (brouillon 5, R12), avec l'identifiant `claude-sonnet-5-5`, l'empreinte du brouillon relu (`30f45ac5af140913bdd3fa34af3bdd2322850f6e052e5d856f5c1ce9e35081d3`) et l'empreinte de ce rapport (à écrire par l'orchestrateur). Les quatre majeurs demandent une version nouvelle, non une retouche ; une nouvelle contre-lecture des seuls passages modifiés (S4, S13, S21, S22, S23, M § 23 et garde de rétrodiction) suffirait ensuite.

---

## Annexe — scripts de contre-lecture (hors dépôt, `/tmp/cl4work/`, non versionnés ; code intégral ci-dessous)

Empreintes : `sim_estim2.py` `f6bbfad77ff78e51d3993a2795208e45187be9e0adb2c9596ee95ab9082b207e` ; `part_intra_u.py` `a3195d1627b8207dafecdded6b41a4c5529c704ec7c2a4129727f22bbacab5eb` ; `bascule_s12.py` `d3e52518a6676717daf2f2f71da45af987bf48634ed6e31e166e70bc802239d0`. Lancement : `python3 -I sim_estim2.py 250` (≈ 50 s) ; les deux autres sans argument. Les sorties imprimées sont reprises dans CS4-03 (annexes A et B) et CS4-07 (annexe C).

### Annexe A — `sim_estim2.py` (puissance jointe de l'étape d'estimation ; ẑ = z, borne haute)

```python
# Simulation de contre-lecture CS4 : puissance jointe de l'étape d'estimation (selection k sur E1, test sur E2, effets fixes de u)
# Hypotheses identiques à M §23 du script du brouillon 4 : sortie cumulée = bruit (var 3) + effets de z1 à t-1, t, t+1 ; z_i parfaitement retrouvées (borne haute).
import numpy as np, sys
from scipy.stats import norm
rng = np.random.default_rng(np.random.SeedSequence(20261031, spawn_key=(901,)))
def demean_by(g, X):
    # soustrait la moyenne par groupe (effets fixes)
    out = X.astype(float).copy()
    ug, inv = np.unique(g, return_inverse=True)
    cnt = np.bincount(inv)
    for j in range(X.shape[1]):
        s = np.bincount(inv, weights=X[:, j])
        out[:, j] -= (s/cnt)[inv]
    return out
def ols_t(y, Z, g, deff=1.0):
    Yd = demean_by(g, y[:, None]); Zd = demean_by(g, Z)
    XtX = Zd.T @ Zd
    beta = np.linalg.solve(XtX, Zd.T @ Yd[:, 0])
    res = Yd[:, 0] - Zd @ beta
    dof = len(y) - len(np.unique(g)) - Z.shape[1]
    s2 = (res @ res)/dof
    se = np.sqrt(np.diag(np.linalg.inv(XtX))*s2*deff)
    return beta, beta/se
def one_world(N, P, firstyear, lastyear, beta_z=0.4, fe=True, deffs=(1.0,2.0), nsel_dims=5, eff=True):
    E = 3
    npair = min(N*(N-1)//2, 1000)
    # paires : tirage de couples de niches distincts
    allpairs = [(i,j) for i in range(N) for j in range(i+1,N)]
    sel = rng.choice(len(allpairs), size=npair, replace=False)
    pairs = np.array([allpairs[s] for s in sel])
    years = np.arange(firstyear, lastyear+1)
    # u = env x annee
    # E : 40% des paires (par environnement, tirage)
    res = {d: dict(trouve=0, k_ok=0, sig=0, fd=0) for d in deffs}
    rows = []
    # construit structure
    env = np.repeat(np.arange(E), npair)
    # moitiés de niches par environnement
    halfA = {e: set(rng.permutation(N)[:N//2]) for e in range(E)}
    inE = rng.random(E*npair) < 0.40
    pi = np.tile(pairs, (E,1))
    pa = np.array([ (pi[k,0] in halfA[env[k]]) and (pi[k,1] in halfA[env[k]]) for k in range(E*npair)])
    pb = np.array([ (pi[k,0] not in halfA[env[k]]) and (pi[k,1] not in halfA[env[k]]) for k in range(E*npair)])
    nY = len(years); h1 = years[:nY//2]; h2 = years[nY//2:]
    # u params
    U = E*(lastyear+1)  # indices
    mu = rng.uniform(-2,2,size=(5,E,lastyear+2)); sg = rng.uniform(0.5,2,size=(5,E,lastyear+2))
    out = {}
    def make(sub_pairs_mask, yrs):
        idx = np.where(sub_pairs_mask)[0]
        e = np.repeat(env[idx], len(yrs)); yy = np.tile(yrs, len(idx))
        return idx, e, yy
    # tirage des z pour tout (paires E seulement, annees firstyear-1..lastyear+1 pour effets t-1,t,t+1)
    idxE = np.where(inE & (pa|pb))[0]
    yrs_all = np.arange(firstyear-1, lastyear+2)
    z = np.empty((len(idxE), len(yrs_all), 5))
    for a,k in enumerate(idxE):
        e = env[k]
        for b,yv in enumerate(yrs_all):
            z[a,b,:] = rng.normal(mu[:,e,yv], sg[:,e,yv])
    # centrage-reduction de z1 dans le monde (approx : sur l'echantillon)
    z1 = z[:,:,0]; z1t = (z1 - z1.mean())/z1.std()
    e1 = beta_z*2*norm.cdf(z1t) if eff else np.zeros_like(z1t)
    pos = {yv:i for i,yv in enumerate(yrs_all)}
    def build(maskpairs, yrs):
        Zs=[]; ys=[]; gs=[]
        for a,k in enumerate(idxE):
            if not maskpairs[k]: continue
            for yv in yrs:
                b = pos[yv]
                y = rng.normal(0, np.sqrt(3.0)) + e1[a,b-1]+e1[a,b]+e1[a,b+1]
                Zs.append(z[a,b,:]); ys.append(y); gs.append(env[k]*1000+yv)
        return np.array(ys), np.array(Zs), np.array(gs)
    y1,Z1,g1 = build(pa, h1); y2,Z2,g2 = build(pb, h2)
    out['n1']=len(y1); out['n2']=len(y2)
    if len(y1)<200 or len(y2)<200: return out
    for d in deffs:
        if fe:
            b1,t1 = ols_t(y1, Z1, g1, d)
            kh = int(np.argmax(np.abs(b1*Z1.std(axis=0))))
            b2,t2 = ols_t(y2, Z2[:,[kh]], g2, d)
        else:
            gz1=np.zeros_like(g1); gz2=np.zeros_like(g2)
            b1,t1 = ols_t(y1, Z1, gz1, d); kh=int(np.argmax(np.abs(b1*Z1.std(axis=0))))
            b2,t2 = ols_t(y2, Z2[:,[kh]], gz2, d)
        out[('k_ok',d)] = (kh==0)
        out[('sig',d)] = (abs(t2[0])>2.5758293)
        out[('trouve',d)] = (kh==0) and abs(t2[0])>2.5758293 and b2[0]>0
        out[('t2',d)] = t2[0] if kh==0 else np.nan
    return out
def run(label, N, P, first, last, reps, fe=True, eff=True):
    acc = {}; n1=[]; n2=[]; t2=[]
    for r in range(reps):
        o = one_world(N,P,first,last,fe=fe,eff=eff)
        if ('trouve',1.0) not in o: continue
        n1.append(o['n1']); n2.append(o['n2'])
        for d in (1.0,2.0):
            acc.setdefault(('trouve',d),[]).append(o[('trouve',d)])
            acc.setdefault(('k_ok',d),[]).append(o[('k_ok',d)])
            acc.setdefault(('sig',d),[]).append(o[('sig',d)])
    if not n1:
        print(f"{label} fe={fe} eff={eff}: aucun monde utilisable (E1 ou E2 < 200 paires-annees) ; n moyen non calcule"); return
    print(f"{label} fe={fe} eff={eff}: reps={len(n1)} n(E1)={np.mean(n1):.0f} n(E2)={np.mean(n2):.0f} | "
          + " | ".join(f"deff {int(d)}: k_ok {np.mean(acc[('k_ok',d)]):.2f} sig {np.mean(acc[('sig',d)]):.2f} trouve {np.mean(acc[('trouve',d)]):.2f}" for d in (1.0,2.0)))
    sys.stdout.flush()
reps = int(sys.argv[1]) if len(sys.argv)>1 else 40
# annees utilisables = celles ou Y+ est defini ; u2 (panel entier) : annees 1..P-3 ; u1 : annees 6..P-3
run("A: P=12, u2, annees 1..9 (hyp. du brouillon 4, N=45)", 45, 12, 1, 9, reps)
run("B: P=16, u1, annees 6..13", 45, 16, 6, 13, reps)
run("C: P=20, u1, annees 6..17", 45, 20, 6, 17, reps)
run("D: P=13, u1, annees 6..10", 45, 13, 6, 10, reps)
```

### Annexe B — `part_intra_u.py` (part de variance de l'effet restant à l'intérieur d'une valeur de u)

Sortie : `part intra-u : moyenne 0.54, p10 0.48, p90 0.61 ; facteur sur la statistique 0.74`.

```python
# Part de la variance de l'effet 2*Phi(z1 centre-reduit) qui reste a l'interieur d'une valeur de u (ce que les effets fixes de u laissent)
import numpy as np
from scipy.stats import norm
rng=np.random.default_rng(np.random.SeedSequence(7,spawn_key=(1,)))
U=36; n=2000; sh=[]
for r in range(200):
    mu=rng.uniform(-2,2,U); sg=rng.uniform(0.5,2,U)
    z=rng.normal(mu[:,None],sg[:,None],(U,n)); zt=(z-z.mean())/z.std(); e=2*norm.cdf(zt)
    sh.append(e.var(axis=1).mean()/e.var())
sh=np.array(sh); print("part intra-u : moyenne %.2f, p10 %.2f, p90 %.2f ; facteur sur la statistique %.2f"%(sh.mean(),np.quantile(sh,.1),np.quantile(sh,.9),np.sqrt(sh.mean())))
```

### Annexe C — `bascule_s12.py` (déclassement à tort par bruit de bascule, S12)

Sortie : q = 0,03 : 0,0110 par comparaison, 0,144 sur 14 comparaisons, 0,250 sur 26 ; q = 0,05 : 0,0385, 0,423, 0,640 ; q = 0,02 : 0,0034, 0,046, 0,084.

```python
# S12 : probabilite qu'une methode invariante a bruit de bascule pres soit declassee (|ecart| > 0,10 sur 30 mondes, i.e. au moins 4 mondes nets)
from math import comb
def pmf(x,n,p): return comb(n,x)*p**x*(1-p)**(n-x)
n=30
for q in (0.01,0.02,0.03,0.05):
    pD=sum(pmf(x,n,q)*pmf(y,n,q) for x in range(n+1) for y in range(n+1) if abs(x-y)>=4)
    print(f"q={q:.2f} par monde et par sens : par comparaison {pD:.4f} ; 14 comparaisons {1-(1-pD)**14:.3f} ; 26 comparaisons {1-(1-pD)**26:.3f}")
```

### Sortie de l'annexe A (250 mondes par ligne)

```
A: P=12, u2, annees 1..9 (hyp. du brouillon 4, N=45) fe=True eff=True: reps=250 n(E1)=1111 n(E2)=1521 | deff 1: k_ok 0.88 sig 0.76 trouve 0.76 | deff 2: k_ok 0.88 sig 0.46 trouve 0.46
B: P=16, u1, annees 6..13 fe=True eff=True: reps=250 n(E1)=1106 n(E2)=1209 | deff 1: k_ok 0.92 sig 0.63 trouve 0.63 | deff 2: k_ok 0.92 sig 0.28 trouve 0.28
C: P=20, u1, annees 6..17 fe=True eff=True: reps=250 n(E1)=1664 n(E2)=1821 | deff 1: k_ok 0.98 sig 0.88 trouve 0.88 | deff 2: k_ok 0.98 sig 0.58 trouve 0.58
D: P=13, u1, annees 6..10 fe=True eff=True: reps=250 n(E1)=555 n(E2)=911 | deff 1: k_ok 0.74 sig 0.47 trouve 0.47 | deff 2: k_ok 0.74 sig 0.16 trouve 0.16
```
