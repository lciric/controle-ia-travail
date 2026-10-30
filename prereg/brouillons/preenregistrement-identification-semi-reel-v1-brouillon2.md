# Préenregistrement — épreuve semi-réelle des méthodes d'identification des causes de la fertilité (gradation 1 de R-633) — v1 — BROUILLON 2 (non gelé, non scellé)

**Statut : brouillon 2, non scellé ; contre-lecture par un modèle différent à faire.**

Brouillon 2, écrit par un sous-agent neuf (Opus 5.5) le 30 octobre 2026 (relevé `date -u` : 23:27 UTC au début), **avant tout verdict du collisionneur sur la question 6**. Il intègre les corrections tirées des fiches de lecture vérifiées des neuf PDF (règle R7, page citée) et remplace, sans l'écraser, le brouillon 1 (`preenregistrement-identification-semi-reel-v1-brouillon1.md`, `d8ae28dc66888793886bc202ad47f7081c2033244b4bdfbce14cbbd664121516`, intact, règle R12). Suite : verdict du collisionneur → **brouillon 3** (section « À intégrer après le verdict du collisionneur sur la question 6 ») → contre-lecture par un modèle différent d'Opus (règle R2) → gel des seuils par Lazar (aucun défaut de 48 heures) → scellement par `sceller_prereg` **avant toute lecture des métadonnées moissonnées** (règle R1). Aucune méthode n'a été exécutée ; aucune donnée n'a été lue ; la moisson n'est pas disponible pour l'auteur. Les seules grandeurs calculées sont des probabilités binomiales exactes, une arithmétique de budget et de condition de rang, sans tirage aléatoire (script cité plus bas). Chaque seuil porte le marqueur littéral du validateur ; la section « À intégrer… » le porte aussi : tant qu'il en reste un, `sceller_prereg` refuse de sceller.

Conventions de renvoi : « fiche § k, p. X » = section k de `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` (`63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79`), page X **du fichier PDF** (le numéro imprimé, quand il diffère, suit « art. ») ; « (M) » = grandeur calculée par le script du brouillon 2 ; « SUPPOSÉ » = énoncé non vérifié sur PDF empreinté ; « LECTURE À CONFIRMER » = doute de l'auteur sur une lecture, à trancher avant le gel, jamais comblé par une invention.

## Résumé de dix lignes pour Lazar

1. **Ce que l'épreuve mesure (inchangé).** Vraies métadonnées d'OpenAlex ; on y **plante une cause connue** C (« contact » entre deux niches qui ajoute des œuvres-ponts deux ans plus tard) et l'on regarde si chaque méthode retrouve C au milieu du vrai bruit, sans jamais prétendre connaître les vraies causes.
2. **Pièges plantés (inchangés)** : facteur caché H, leurre L (collisionneur entre C et H), jumeau sans effet C⁰ ; **nouveau** : une condition où le contact **retire** des œuvres-ponts (R2⁻, signe négatif), parce qu'une vérité publiée (Borjas et Doran 2012) donne un signe négatif à l'afflux : l'épreuve ne doit plus présupposer « plus de contact, plus de fertilité ».
3. **Volet A** : témoins (popularité, prédicteur associatif, tri par variance **avec sélection par critère d'information bayésien comme dans Reisach 2021**, et nouveau tri par coefficient de détermination), prédiction causale invariante, PCMCI, **DirectLiNGAM** nommé (ICA-LiNGAM en descriptif). PCMCI et la prédiction invariante ne sont couverts par aucun des neuf PDF : tout énoncé sur elles est SUPPOSÉ, trois PDF sont à demander.
4. **Volet B réécrit** : le brouillon 1 sortait des hypothèses du théorème 1 de Khemakhem 2020 (fiche § 3, p. 5). Deux options soumises à Lazar : (1) garder ce volet comme **test de robustesse hors théorème** ; (2) **recommandée** : ajouter une variante qui respecte le théorème (cinq sources plantées, conditionnellement indépendantes, variable auxiliaire à au moins 22 valeurs, indicateurs continus) qui porte la décision, le volet hors théorème devenant descriptif.
5. **Graines** : deux graines d'entraînement étaient trop peu (Locatello 2019 en emploie 50, fiche § 2, p. 4) ; recommandation : 5 graines par méthode, médiane par monde (jamais la meilleure graine), plus une sous-étude à 50 graines sur 2 mondes ; coût (M, § 12) environ 107 heures de processeur pour l'option 2, d'où S15 relevé.
6. **Supervision écrite** : choisir le facteur latent par son coefficient sur la sortie est une supervision ; elle est désormais nommée, appliquée à l'identique aux deux réseaux, et faite sur une moitié des données tenues à l'écart, testée sur l'autre.
7. **CITRIS** sort de l'épreuve (cibles d'intervention exigées à chaque pas, fiche § 4, p. 3) : candidate de la gradation 3. **Schölkopf 2021** : cadre seulement.
8. **Gradation 2 (suites)** : pour chacune des quatre expériences naturelles, la « vérité » qu'elle fournit (signe, taille, délai, unité, page) et sa transposition aux œuvres-ponts, avec réserves.
9. **Ce qu'elle n'autorise pas (inchangé)** : aucune affirmation sur les vraies causes de la fertilité ; seulement l'entrée (ou non) de chaque méthode dans les gradations 2 et 3.
10. **Pour geler** : seuils S1 à S16 (numérotation stable) et nouveaux S17 à S21 ; sept décisions à soumettre (liste ci-dessous).

### Décisions à soumettre à Lazar (format : décision ; enjeu ; options ; recommandation et confiance)

Aucune ne prend de défaut à 48 heures : elles touchent un préenregistrement avant scellement et se gèlent avec les seuils.

- **D-1 — Volet B et théorème 1 de Khemakhem 2020.** Enjeu : le volet B du brouillon 1 viole les hypothèses (ii) à (iv) du théorème (fiche § 3, p. 5 ; corrigendum p. 9) ; tel quel, son verdict « oui sous hypothèse » serait faux par construction. Options : (1) **hors théorème seul**, réécrit comme test de robustesse (avantage : coût le plus bas, environ 87 heures avec 5 graines, M § 12 ; inconvénient : ne teste jamais l'iVAE là où son théorème s'applique, donc un échec ne dit rien de l'hypothèse) ; (2) **variante B-θ dans le théorème, qui décide, plus le volet hors théorème en descriptif à 30 mondes par condition** (avantage : sépare « échec en échantillon fini dans le théorème » de « fragilité hors théorème » ; inconvénient : indicateurs entièrement synthétiques dans B-θ, le réel n'entre que par la sortie et la variable auxiliaire ; environ 107 heures) ; (3) B-θ seul (avantage : coût moindre ; inconvénient : on perd la mesure de robustesse, qui est ce qui importe sur données réelles). **Recommandation : option 2, confiance 0,65.**
- **D-2 — Graines d'entraînement du volet B (S18) et budget (S15).** Enjeu : la stabilité entre deux graines est bruitée et une stabilité haute de M5 ne prouverait pas l'identification (fiche § 2, p. 5–6). Options : 3 graines (≈ 86 h, option 2) ; **5 graines + sous-étude à 50 graines sur 2 mondes (≈ 107 h)** ; 10 graines (≈ 161 h). Temps unitaires SUPPOSÉS. **Recommandation : 5 graines, S15 = 110 heures, confiance 0,6.**
- **D-3 — Condition à effet négatif R2⁻ (S20).** Enjeu : sans elle, l'épreuve ne plante que des effets positifs, ce qui présuppose la branche « plus de contact, plus de fertilité » que Borjas et Doran contredisent (fiche § 7, p. 28–29, art. 27–28). Options : (1) **condition de décision, ligne 7bis de la Table A** (avantage : une méthode qui ne détecte qu'un signe est attrapée ; inconvénient : 100 mondes de plus, la conjonction de recouvrement passe de 0,852 à 0,818 pour un recouvrement vrai de 0,85, M § 9) ; (2) condition descriptive (avantage : ne durcit pas la qualification ; inconvénient : un défaut de signe ne coûte rien) ; (3) rien. **Recommandation : option 1, confiance 0,7.**
- **D-4 — CITRIS.** Enjeu : exige des cibles d'intervention observées à chaque pas (fiche § 4, p. 3). Options : (1) **hors de la gradation 1, candidate de la gradation 3** ; (2) variante où C est donné comme cible connue (avantage : elle entre dans l'épreuve ; inconvénient : on lui donne l'information qui fait l'identification — quand et sur quoi l'on intervient — ce qu'aucune autre méthode du volet A ne reçoit ; ce serait un avantage à écrire comme tel, et l'hypothèse « sans effet instantané », fiche § 4, p. 2, est probablement violée par l'agrégation annuelle, SUPPOSÉ). **Recommandation : option 1, confiance 0,85.**
- **D-5 — Sélection supervisée du facteur à l'étape d'effet (S21).** Enjeu : le brouillon 1 testait l'effet sur le facteur choisi par la vérité (oracle), et classait les facteurs par leur coefficient sur la sortie (supervision non dite, fiche § 2, portée (b)). Options : (1) **sélection par la sortie sur une moitié des données tenues à l'écart, test sur l'autre moitié, « trouve » seulement si le facteur choisi est le bon** (avantage : praticable et honnête ; inconvénient : moins de puissance) ; (2) oracle (avantage : puissance ; inconvénient : ne correspond à aucun usage réel). **Recommandation : option 1, l'oracle en descriptif, confiance 0,75.**
- **D-6 — PDF manquants avant le gel.** Enjeu : PCMCI et la prédiction invariante portent quatre lignes de prédiction et deux seuils (S8) sans aucune vérification sur PDF. Options : (1) **obtenir Runge et collègues 2019, Peters, Bühlmann et Meinshausen 2016, Reisach et collègues 2023 (et Shimizu et collègues 2006 et 2011) et en faire des fiches vérifiées avant le gel** ; (2) geler avec les marques SUPPOSÉ (aucun chiffre de ces papiers n'est utilisé). **Recommandation : option 1, confiance 0,7** ; à défaut, option 2 sans changement de texte.
- **D-7 — Seuils S1 à S21** : à geler en une ligne datée de `registres/decisions.md` ; les trois choix vraiment ouverts du brouillon 1 (S3, S8, S9) restent ouverts.

### Nœuds ouverts avant scellement

1. **Verdict du collisionneur sur la question 6** (pièce n° 264) : attendu ; le brouillon 3 l'intègre (section dédiée, laissée vide ici).
2. **Manifeste de la moisson** (session-depot, n° 265) : cité par chemin et empreinte au scellement ; son contenu chiffré n'est pas lu avant. LECTURE À CONFIRMER : compter les valeurs distinctes de la variable auxiliaire de B-θ (environnements × années, S19) à partir de la **liste des environnements et des années** du manifeste est-il une lecture au sens de R1 ? L'auteur pense que non (c'est la règle de sélection, pas le contenu), mais la décision revient à Lazar ; à défaut, la vérification se fait à la validation de la base (booléen seulement, S13).
3. **Décisions D-1 à D-7.**
4. **PDF manquants** (D-6).
5. **Bibliothèques** (routine) : `tigramite` (PCMCI), `lingam` (DirectLiNGAM et ICA-LiNGAM), `scikit-learn` (témoins ; `LassoLarsIC` pour le critère d'information bayésien), `scipy` (appariement par affectation linéaire), torch ; versions figées au manifeste.

- Auteur : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), canal `canal/conv-audit-n04` ; n'a écrit ni le brouillon 1, ni les fiches de lecture, ni la réponse 6. **Ne peut pas être contre-lecteur** de ce texte ni de ses versions suivantes. Le brouillon 1 a été écrit par conv-audit (Opus 5.5) : un contre-lecteur Opus serait doublement non indépendant ; la contre-lecture se fait par un modèle différent.
- Date (UTC), relevé `date -u` : début 2026-10-30T23:27Z ; fin, voir l'empreinte compagnon (à écrire par l'orchestrateur, pas par l'auteur).
- Commit du code d'analyse : aucun code ; le code s'écrit **après** scellement (R9).
- Non lus : tout `donnees/` ; la moisson ; les neuf PDF eux-mêmes (seules leurs fiches vérifiées sont lues) ; aucune commande git, aucun réseau, aucune dépense.
- Documents qui font foi (empreintes SHA-256 calculées par l'auteur le 2026-10-30 vers 23:27 UTC ; « pièces » = chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-niches-v1/`) :
  - brouillon 1 `prereg/brouillons/preenregistrement-identification-semi-reel-v1-brouillon1.md` `d8ae28dc66888793886bc202ad47f7081c2033244b4bdfbce14cbbd664121516` (base, lu en entier), son script `…-brouillon1.py` `474a45d984d56f53482c8e36018bf58eca518762d52b94890ae5dcf62f150358` et sa sortie `…-brouillon1-sortie.txt` `eb3922a0736216f16f70d50ada1153c9399d84571a2d9bea479951b5f41942a9` (empreintes conformes aux compagnons `.sha256`) ;
  - fiches de lecture vérifiées `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` `63db77700da4bccf2911d3184afda33c4374b7138ed91f2692bd7f0a363d1d79` (conforme à son compagnon ; **source des corrections**) ; les empreintes des neuf PDF y figurent (fiche, tableau d'en-tête) ;
  - `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`, `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (lus) ;
  - pièces : `question-6-identification-collisionneur-v1.md` `14966d0d2ffdea9de94b924a6ad661b440eae1bb2db865b81fd0eb75e6d71b73` (non relue ; empreinte seulement), `reponse-conv-audit-question-6-v1.md` `afdb9f9dbf9ed8a837d20962eb815e4eea817454dc296440a743123769ef00bf` (survolée), `relecture-fable-reponse-6-v1.md` `bedb1f4c674ef70264e5c3bd19036f2ef6f18da9c098797d24c7be8b5da6c26e` (survolée ; RL6-01 à RL6-09), `reponse-fable-independante-questions-6-7-v1.md` `052a37e765afc6aaa8a14afcb3ac3803994046457b361542cff1dd3b067cd65e` (survolée, question 6 seulement) ;
  - `registres/decisions.md` (fichier vivant, `2f3eb9f0d0a007346dd3e4c51901b0628f351bae208ab7c14c2a120af42a126a` à la lecture) : R-631, R-633, R-641, R-650 ;
  - les documents cités par le brouillon 1 (questions 2 à 5, réponses 3 à 5, relecture 5, programme v2, préenregistrement modèle) gardent les empreintes que le brouillon 1 leur donne ; **non relus** pour ce brouillon ;
  - script `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon2.py` `eb9d429d3e02c0e843941efed87efa233b05b62f43f141aaee784038a59ba05d` et sortie `prereg/brouillons/calcul-regles-identification-semi-reel-v1-brouillon2.sortie.txt` `35aa0d02445387bdbf7ed24d6d20468574a17104dc281bd43b63381b7f053a51` (lancé par `python3 -I` ; paragraphes 1 à 8 identiques au bit près à la sortie du brouillon 1, vérifié par `diff` ; deux exécutions donnent la même empreinte).
- Références de littérature : les neuf papiers des fiches sont cités **par fiche et page** ; tous les autres sont **SUPPOSÉS** (liste et PDF manquants : section Hypothèse, « Références non couvertes »).

## Ce qui change par rapport au brouillon 1

| # | Changement | Fiche → page | Section du brouillon 2 |
|---|---|---|---|
| C1 | T2 : régression pénalisée en norme 1 sélectionnée par **critère d'information bayésien** (comme « sortnregress »), non par validation croisée | § 1, p. 7 (énoncé 5) | Hypothèse (table, T2) ; Plan § 5 |
| C2 | La standardisation n'efface pas l'artefact : mesure de la croissance des coefficients de détermination le long du sous-graphe planté, témoin T2b (tri par coefficient de détermination), seuil **S17**, déclencheur S14 (h) | § 1, p. 9 (énoncé 9) ; p. 8 (énoncé 6 : v = 1/2 après standardisation) | Métrique (artefacts) ; S17 ; Plan § 6 ; S14 |
| C3 | Variante de LiNGAM nommée : **DirectLiNGAM** (M3, décision) ; ICA-LiNGAM (M3b, descriptive) ; prédiction écrite pour ART(M3) | § 1, p. 6 (§ 3.4) et p. 2 | Hypothèse (table) ; Prédiction PA-M3, PA-M3b ; Plan § 5 |
| C4 | Conditions du théorème de Reisach (linéaire, sans confondeur caché) écrites : T2 reste un témoin, jamais une méthode candidate | § 1, p. 3 | Hypothèse (table, T2) |
| C5 | Graines d'entraînement : 5 par méthode, médiane par monde, sous-étude à 50 graines sur 2 mondes ; seuil **S18** ; S15 relevé | § 2, p. 4 (50 graines) ; p. 5–6 (graine plus influente que l'objectif) | S18 ; S15 ; Plan § 5, § 8 ; Métrique (volet B) |
| C6 | Classer le facteur par son coefficient sur la sortie est une **supervision** : écrite, identique pour M4 et M5, faite sur une moitié tenue à l'écart ; seuil **S21** | § 2, portée (b) ; p. 3 (« we only observe samples from P(x) ») | Métrique (volet B) ; S21 ; Table Bθ et B-hors |
| C7 | M5 reste le contre-exemple ; sa non-identification est le résultat attendu, l'instabilité entre graines est un constat empirique, pas le théorème | § 2, p. 3 (théorème 1) ; p. 5–6 | Hypothèse (table, M5) |
| C8 | **Volet B hors des hypothèses du théorème 1** : sources réelles dépendantes, non exponentielles conditionnelles ; comptes discrets ; variable auxiliaire à moins de nk + 1 = 11 valeurs possibles ; d = 6 ≠ n = 5. Réécrit en volet **B-hors** (robustesse) et nouvelle variante **B-θ** (dans le théorème) ; seuil **S19** ; décision D-1 | § 3, p. 5 (théorème 1, (i) à (iv)) ; p. 9 et p. 18 (corrigendum) ; p. 6 (proposition 1) ; p. 6–7 (simulation, d = n = 5, M = 40, L = 1 000) ; p. 15 (λ aléatoires) | Hypothèse (W5, W5θ, table M4) ; Prédiction volet B ; S6 (inchangé, rattaché à B-hors) ; S19 ; Tables Bθ et B-hors |
| C9 | Mesure de recouvrement alignée : en plus de r_Z (maximum sur les dimensions), coefficient de corrélation moyen après appariement par affectation linéaire (MCC) en B-θ | § 3, p. 7 | Métrique (volet B) |
| C10 | **CITRIS** : hors de la gradation 1 (cibles d'intervention exigées à chaque pas), candidate de la gradation 3 ; décision D-4 | § 4, p. 3 ; p. 2 ; p. 5 | Hypothèse (méthodes écartées) |
| C11 | **Schölkopf 2021** cité comme cadre seulement ; l'hypothèse des décalages parcimonieux qui fonde l'emploi des environnements de M1 est écrite **non testable** | § 5, p. 1 (art. 612) ; p. 8 (art. 619) ; p. 4–5 (art. 615–616) | Hypothèse (hypothèses non testables ; table M1) |
| C12 | **Hypothèse concurrente de signe** (Borjas et Doran 2012 : l'afflux réduit la production en place) ; prédiction de signe à deux branches ; condition plantée à effet négatif **R2⁻**, seuil **S20**, ligne 7bis de la Table A ; décision D-3 | § 7, p. 76 (art. 75), p. 28–29 (art. 27–28), p. 55–56 (art. 54–55) ; lecture transversale | Hypothèse ; Prédiction ; S20 ; Plan § 3, § 7 ; Table A |
| C13 | Gradation 2 : « vérité » de chacune des quatre expériences naturelles et transposition aux œuvres-ponts, réserves | § 6 à § 9 (pages dans la section) | Suites |
| C14 | PCMCI et prédiction invariante : aucun des neuf PDF ne les couvre ; tout énoncé marqué SUPPOSÉ ; PDF à demander ; décision D-6 | fiches, en-tête (liste des neuf PDF) ; § 1, portée (« R²-sortabilité » SUPPOSÉE) | Hypothèse (références non couvertes) |
| C15 | Section « À intégrer après le verdict du collisionneur sur la question 6 » (vide, points attendus) | — | section dédiée |
| C16 | Liste d'arrêt complétée : neuf gardes nouvelles, chacune testée sur un cas sain et sur un artefact (R5) | — | Liste d'arrêt |
| C17 | S7 et S15 : recommandations mises à jour (mondes de R2⁻, B-θ, B-hors ; budget) ; aucune valeur de S1 à S16 n'est retirée | M § 9, § 11, § 12 | Seuil |

Aucun seuil n'est retiré. Les tables de lecture gardent leurs numéros de ligne ; les lignes nouvelles portent un suffixe (« 7bis »).

## Hypothèse

**Énoncé d'ensemble (H-SR, inchangé).** L'identification d'une cause n'est pas une propriété de l'algorithme mais du couple « données + hypothèses » (position de la réponse 6). Sur une base réelle de métadonnées d'OpenAlex où l'on plante une cause connue de fertilité au milieu du vrai bruit, chaque méthode retrouve la cause plantée **si et seulement si** l'hypothèse dont dépend son résultat d'identifiabilité est satisfaite par la plantation, et elle se trompe (leurre, jumeau, signe) là où cette hypothèse est violée. Cadre conceptuel (et non preuve) : « l'identification exige des hypothèses ou des interventions » (fiche § 5, p. 4–5, art. 615–616 ; Schölkopf et collègues 2021 est un article de revue et de perspective, sans théorème propre, fiche § 5, p. 1, art. 612). Les théorèmes invoqués sont ceux de Locatello et collègues 2019 (fiche § 2, p. 3), Khemakhem et collègues 2020 (fiche § 3, p. 5–6) et Reisach et collègues 2021 (fiche § 1, p. 5) ; ceux de PCMCI, de LiNGAM et de la prédiction invariante sont SUPPOSÉS (aucun PDF vérifié). Renvoi : R-631, R-633 (gradation 1), R-650 (fiches) ; programme v2, E1.4.

**Objet mesuré (inchangé).** Pour une paire de niches (i, j) d'un même environnement et une année t, la fertilité est approchée par le nombre d'**œuvres-ponts** : œuvres publiées en t dont les références contiennent au moins une œuvre de i et au moins une œuvre de j (Plan § 2). C'est un indicateur, pas la fertilité au sens de la question 3.

### Hypothèse concurrente de signe (nouvelle ; deux branches)

Les quatre expériences naturelles lues (fiches § 6 à § 9) ne donnent pas un signe unique au « contact » :
- **Branche H-C⁺ (contact entre niches distinctes → plus de ponts).** Retirer un contact ou un nœud baisse la production ou les citations entre groupes : Campos et collègues 2018, annulation d'un congrès, −0,0241 sur la probabilité de collaborer (moyenne 0,1563), soit environ −16 % (fiche § 8, p. 12, art. 1006, tableau 4) ; Iaria et collègues 2018, coupure de 1914, −0,222 de part des références hors du camp, environ −85 % (fiche § 9, p. 23, art. 949, tableau IV) ; Azoulay et collègues, décès d'une « superstar », −0,086 (fiche § 6, p. 28, art. 26, tableau III, colonne 1b).
- **Branche H-C⁻ (afflux dans les mêmes niches → moins de production en place).** Borjas et Doran 2012 : après 1992, (après 1992) × corrélation d'exposition = −0,133 (0,036) article par an (fiche § 7, p. 76, art. 75, tableau III, panneau A), soit environ un tiers de la production de 1992–2008 (fiche § 7, p. 28–29, art. 27–28) ; baisse « comblée » par les émigrés, sans agrandissement du « gâteau » (fiche § 7, p. 55–56, art. 54–55).

Ces deux branches ne portent ni sur le même traitement (retrait d'un contact entre groupes distincts contre afflux de producteurs concurrents dans les mêmes champs) ni sur la même sortie (collaboration, citation entre groupes, production individuelle). **Prédiction de signe à deux branches**, écrite pour le préenregistrement de la gradation 2 (pas pour celui-ci, qui ne lit aucun signe réel) : l'effet d'une hausse de contact sur les œuvres-ponts d'une paire de niches est **positif** quand le contact relie des niches distinctes et complémentaires (H-C⁺), **négatif ou nul** quand il prend la forme d'un afflux de producteurs dans une même niche (H-C⁻). Réfutation de H-C⁺ : sur la transposition d'Iaria ou de Campos, la coupure du contact ne baisse pas les ponts (borne haute de l'effet ≥ 0). Réfutation de H-C⁻ : sur la transposition de Borjas et Doran, l'exposition à l'afflux **augmente** les ponts de la niche en place (borne basse > 0). Les deux réfutations sont possibles ; aucune branche ne peut être confirmée par construction.

**Conséquence pour la gradation 1** : le brouillon 1 ne plantait que des effets positifs ; une méthode qui ne détecte qu'un signe, ou un banc qui ne sait voir qu'une direction, passait. Le brouillon 2 ajoute la condition **R2⁻** (W1⁻) où le contact **retire** des œuvres-ponts (décision D-3, S20).

### Monde planté (écrit, connu, jamais lu par une méthode)

- (W1) **Cause plantée observée** C : pour une paire-année traitée, des œuvres-ponts synthétiques s'ajoutent ℓ années plus tard, en nombre tiré d'une loi de Poisson de moyenne β·σ_e ; effet invariant entre environnements par construction (sauf D1).
- (W1⁻, nouveau) **Cause plantée de signe négatif** (condition R2⁻) : un **fond planté** ajoute à chaque paire-année **non traitée** de la fenêtre, ℓ années plus tard, des œuvres-ponts de loi de Poisson de moyenne |β|·σ_e ; une paire-année traitée n'en reçoit pas. L'effet de C est donc −|β|·σ_e en espérance, exactement, sans retirer aucune œuvre réelle (les œuvres réelles ne sont jamais supprimées, garde de plomberie). En β = 0 la base est inchangée au bit près.
- (W2) **Facteur caché planté** H (inchangé).
- (W3) **Leurre** L, collisionneur entre C et H (inchangé).
- (W4) **Jumeau sans effet** C⁰ (inchangé).
- (W5) **Volet B-hors** (le volet B du brouillon 1, renommé) : cause latente Z continue ; les méthodes voient K = 8 indicateurs, mélange non linéaire de Z **et des covariables réelles** S, D, A, g(Y⁰) ; la loi de Z varie (Bv) ou non (Bc) avec u = (environnement × bloc de cinq ans). **Hors des hypothèses du théorème 1** (fiche § 3, p. 5, et portée) : (a) quatre des cinq sources sont réelles, dépendantes entre elles, non modélisées en famille exponentielle conditionnelle à u (hypothèse « toutes les latentes conditionnellement indépendantes sachant u » violée) ; (b) S et D sont des comptes (transformés en log), sources discrètes hors du cadre des densités, et le corrigendum retire toute revendication d'identifiabilité pour des observations discrètes (fiche § 3, p. 9 et p. 18) ; (c) avec n = 5 sources et k = 2 (moyenne et variance modulées), le théorème demande nk + 1 = 11 valeurs distinctes de u (fiche § 3, p. 5 ; M § 10) ; u = environnement × bloc de cinq ans en donne entre 3 et 15 selon la base (M § 10) ; (d) dimension apprise d = 6 ≠ n = 5. **Ce volet teste une robustesse hors théorème, pas le théorème.** Aucun résultat partiel du papier ne garantit Z seul quand les autres sources violent l'hypothèse (SUPPOSÉ : rien de tel dans le PDF, fiche § 3, portée (a)).
- (W5θ, nouveau) **Volet B-θ** (dans les hypothèses du théorème 1) : n = 5 sources latentes **toutes plantées**, z₁ à z₅, conditionnellement indépendantes sachant u ; z_i | u ~ normale de moyenne μ_i(u) et d'écart-type σ_i(u) (famille exponentielle, k = 2 : moyenne **et** variance modulées, ce qui évite le contre-cas de la proposition 1, où seule la moyenne varie et où la permutation n'est pas atteinte, fiche § 3, p. 6) ; μ_i(u) ~ uniforme(−2 ; 2), σ_i(u) ~ uniforme(0,5 ; 2), tirés **indépendamment pour chaque u** (condition (iv) presque sûre pour des paramètres aléatoires indépendants, fiche § 3, p. 15) ; u = (environnement × année après la période de référence), au moins 22 valeurs distinctes (S19 ; 2 × (nk + 1), marge parce que le résultat est asymptotique, fiche § 3, p. 6, théorème 4) ; indicateurs **continus** x = f(z) + ε, K = 5, f perceptron à deux couches cachées carrées 5 × 5 à poids orthogonaux et pente négative 0,2 de la fonction « leaky ReLU » (injective), ε normal d'écart-type 0,1 ; d = n = 5 (comme la simulation du papier, fiche § 3, p. 6–7 ; LECTURE À CONFIRMER : la fiche écrit « d = n = 5 » sans préciser si d désigne la dimension des observations ou la dimension apprise ; ici les deux valent 5). **Seule z₁ a un effet** : œuvres-ponts de loi de Poisson de moyenne β_Z·σ_e·2Φ(z̃₁) au retard ℓ (z̃₁ = z₁ centrée réduite dans le monde) ; z₂ à z₅ sont des latentes de nuisance sans effet. Bθc (contrôle) : μ_i et σ_i constants en u (la condition (iv) échoue : la matrice L est nulle). **Le réel n'entre dans B-θ que par la sortie** (Y⁰ réel, bruit réel des ponts, H planté) **et par la structure** (paires, environnements, années de u) ; c'est sa limite, écrite.
- Tout le reste est le **vrai bruit** ; aucune variable réelle n'est jamais notée « cause » ou « non-cause ».

### Hypothèses non testables, écrites (nouveau)

- **(NT1) Environnements de M1.** L'emploi des environnements (sous-domaine × bloc de cinq ans) par la prédiction invariante suppose que le passage d'un environnement à l'autre ne change que peu de mécanismes et ne touche pas directement la loi de la sortie sachant ses vraies causes. Schölkopf et collègues posent les « décalages parcimonieux de mécanismes » **comme hypothèse** (fiche § 5, p. 8, art. 619) et disent seulement que des changements de loi « peuvent aider » à identifier (fiche § 5, p. 10, art. 621). Sur la partie réelle de la base, cette hypothèse **n'est pas testable** par l'épreuve : la plantation la satisfait pour C (effet invariant par construction) ; le vrai bruit peut la violer (inflation des citations par décennie, normes par sous-domaine : relecture 6, point (b)2, SUPPOSÉ). L'épreuve mesure la conséquence (erreurs et abstentions de M1), jamais l'hypothèse. La condition D1 viole l'invariance de l'effet planté, pas celle du vrai bruit.
- **(NT2) Invariance de la prédiction invariante** (hypothèse propre de Peters, Bühlmann et Meinshausen 2016) : SUPPOSÉ, aucun PDF vérifié (D-6).
- **(NT3) Suffisance causale de PCMCI et de LiNGAM** : violée par construction sous H (c'est l'objet du piège) ; l'énoncé exact des hypothèses de ces méthodes est SUPPOSÉ (aucun PDF vérifié).
- **(NT4) B-θ** : les indicateurs sont synthétiques ; une réussite en B-θ ne dit rien de la satisfaction des hypothèses du théorème par de vrais indicateurs bibliographiques. B-hors en mesure la robustesse, sur un seul type de violation.
- **(NT5) Une seule réalisation du vrai bruit** (inchangé) : la variabilité estimée est celle de la plantation.

### Hypothèses rivales gelées, méthode par méthode

| Code | Méthode | Hypothèse d'identification | Satisfaite par la plantation ? | Rivale gelée |
|---|---|---|---|---|
| T0 | Popularité seule (inchangé) | aucune (prédiction pure) | sans objet | **HR-T0** : ne retrouve jamais C ; plancher et contrôle de plomberie |
| T1 | Prédicteur associatif (inchangé) | aucune (association) | sans objet | **HR-T1** : retrouve C, retient aussi L et, sous H, C⁰ |
| T2 | Tri par variance puis lasso **sélectionné par critère d'information bayésien** (« sortnregress », fiche § 1, p. 7, énoncé 5) | l'ordre causal suit l'ordre des variances ; résultat d'identifiabilité seulement si v = 1, en modèle linéaire à bruit additif acyclique, sans confondeur caché (fiche § 1, p. 3 et p. 5) | non (artefact connu ; hypothèses du théorème violées) | **HR-T2** : témoin ; réussit en échelle brute si l'ordre des variances suit l'ordre causal ; au hasard en échelle standardisée, où v = 1/2 (fiche § 1, p. 8, énoncé 6) |
| T2b | **Nouveau témoin** : tri par coefficient de détermination croissant (chaque variable régressée sur toutes les autres candidates), puis lasso sélectionné par critère d'information bayésien | l'ordre causal suit la croissance des coefficients de détermination, motif que la standardisation laisse (fiche § 1, p. 9, énoncé 9) | non (artefact) | **HR-T2b** : témoin ; réussit en échelles brute **et** standardisée si les corrélations croissent le long du sous-graphe planté. Défini ici de façon opératoire ; le critère publié de « R²-sortabilité » (Reisach et collègues 2023) est SUPPOSÉ (PDF manquant) |
| M1 | Prédiction causale invariante, version linéaire (Peters, Bühlmann et Meinshausen 2016 : **SUPPOSÉ**, aucun PDF vérifié) | invariance de la loi de la sortie sachant ses vraies causes entre environnements ; pas de facteur caché entre candidates et sortie (SUPPOSÉ) ; emploi des environnements sous NT1 (non testable) | partiellement : effet planté invariant, affectation de C variable entre environnements ; vrai bruit peut-être non invariant ; H viole l'hypothèse sous l'affectation H | **HR-M1** (inchangée) : n'inclut presque jamais L ni C⁰ ; retrouve C seulement si la partie réelle est assez invariante ; s'abstient sous confusion cachée |
| M2 | PCMCI (Runge et collègues 2019 : **SUPPOSÉ**, aucun PDF vérifié) | suffisance causale, stationnarité, fidélité, ordre temporel (SUPPOSÉ) | ordre temporel oui ; suffisance causale non (H) | **HR-M2** (inchangée) |
| M3 | **DirectLiNGAM** (Shimizu et collègues 2011 : SUPPOSÉ quant à la référence ; nommé dans Reisach, fiche § 1, p. 6) | linéarité, bruits non gaussiens indépendants, acyclicité, aucun facteur caché (SUPPOSÉ) ; **ne devrait pas dépendre de l'échelle** (critère invariant d'échelle, fiche § 1, p. 6, § 3.4 : attente des auteurs, LECTURE À CONFIRMER : propriété démontrée ou seulement attendue) | non-gaussianité oui ; linéarité non ; aucun facteur caché : non | **HR-M3** (inchangée) ; **ART(M3) prédit vrai** (invariance d'échelle) |
| M3b | ICA-LiNGAM (Shimizu et collègues 2006, SUPPOSÉ), **descriptive** | mêmes hypothèses ; **sensible au redimensionnement** (fiche § 1, p. 2) | idem | **HR-M3b** : résultats qui changent avec l'échelle (au-delà de 0,10) ; sert de témoin positif de la mesure d'échelle de S12 |
| M4 | iVAE (Khemakhem et collègues 2020) | théorème 1 (fiche § 3, p. 5) : (i) zéros de la fonction caractéristique du bruit de mesure nulle ; (ii) mélange injectif ; (iii) statistiques suffisantes dérivables, linéairement indépendantes ; (iv) nk + 1 valeurs distinctes de u avec matrice L inversible ; a priori conditionnellement factorisé de famille exponentielle (p. 3) ; observations continues (p. 9) ; résultat asymptotique (p. 6, théorème 4), à transformation linéaire près (∼A), à permutation et transformation élément par élément près sous les théorèmes 2 ou 3 (p. 6) | **B-θ : oui** (Bθv), **non** en Bθc (iv échoue) ; **B-hors : non** (voir W5) | **HR-M4θ** : en Bθv, retrouve z₁ (corrélation ≥ 0,70) dans la plupart des mondes, de façon stable entre graines ; en Bθc, pas mieux que M5. **HR-M4hors** : en B-hors, ne garde qu'une partie de cet avantage (robustesse partielle) |
| M5 | **Contre-exemple libre** : même autoencodeur, a priori normal standard, sans u | aucune : un a priori inconditionnel n'est pas identifiable (fiche § 3, p. 3 et p. 18–19) ; démêlage non supervisé impossible sans biais inductif sur le modèle et les données (fiche § 2, p. 3, théorème 1, observations indépendantes et a priori factorisé) ; analyse en composantes indépendantes non linéaire non identifiable (Hyvärinen et Pajunen 1999, rappelé fiche § 2, p. 2) | non | **HR-M5** : ne retrouve pas Z de façon stable. **Réserve** : l'instabilité entre graines est un constat empirique (fiche § 2, p. 5–6), pas un corollaire du théorème ; une stabilité haute de M5 ne prouverait pas l'identification |
| T3 | Composantes principales (inchangé) | ordre des variances | non | **HR-T3** (inchangée) |

**Méthodes écartées de la gradation 1.**
- **CITRIS** (Lippe et collègues 2022) : exige l'accès aux **cibles** d'intervention I^t à chaque pas (fiche § 4, p. 3, § 3.1) ; processus latent markovien d'ordre un, stationnaire, **sans effet instantané** (fiche § 4, p. 2) ; observation bijective (p. 3) ; ce qui est identifié est la « variable causale minimale » des facteurs intervenus, le reste va au groupe résiduel (p. 4–5). Sur OpenAlex aucune cible n'est observée : **inutilisable en observation pure**. Rangée en **gradation 3** (nos courses, où la cible est connue). Variante non retenue (D-4, option 2) : donner C comme cible observée ; ce serait donner à CITRIS l'information qui fait l'identification, avantage qu'aucune autre méthode du volet A ne reçoit, et l'agrégation annuelle viole probablement l'hypothèse sans effet instantané (SUPPOSÉ).
- Méthodes d'estimation sous identification acquise (forêts causales, apprentissage double) : hors de ce préenregistrement (inchangé).
- NOTEARS et méthodes fondées sur l'erreur quadratique moyenne : absentes ; si elles entraient, leur qualification serait conditionnée à l'échelle standardisée (fiche § 1, p. 8–9, § 4.3).

### Références non couvertes par les neuf PDF (SUPPOSÉES) et PDF à demander

Aucun des neuf PDF ne couvre PCMCI ni la prédiction invariante (fiches, en-tête). **Tout énoncé du présent texte sur M1 et M2 est SUPPOSÉ.** PDF à demander (D-6), par priorité :
1. Runge, Nowack, Kretschmer, Flaxman et Sejdinovic 2019, *Science Advances* (PCMCI) — hypothèses, niveaux, comportement sous confondeur caché ;
2. Peters, Bühlmann et Meinshausen 2016, *Journal of the Royal Statistical Society B* (prédiction causale invariante) — garantie de niveau, version approchée (tests de moyenne et de variance des résidus, invoqués à S8) ;
3. Reisach, Tami, Seiler et Weichwald 2023 (« R²-sortabilité ») — titre, auteurs et contenu SUPPOSÉS ; T2b est défini ici sans lui ;
4. Shimizu, Hoyer, Hyvärinen et Kerminen 2006 (ICA-LiNGAM) et Shimizu et collègues 2011 (DirectLiNGAM), *Journal of Machine Learning Research* (SUPPOSÉ) ;
5. secondaires : Hyvärinen et Morioka 2016 et 2017 (hypothèses distinctes, relecture 6, RL6-07) ; Perry, von Kügelgen et Schölkopf 2022 (décalages parcimonieux, relecture 6, RL6-06) ; Hill 2011, Dorie et collègues 2019, Neal et collègues 2020 (plantation sur données réelles, antériorité R8) ; Boudreau et collègues 2017 (rencontres randomisées).

### Ce que l'épreuve n'autorise pas (écrit d'avance)

- **Aucune affirmation sur les vraies causes de la fertilité**, ni sur le signe réel du contact (la prédiction à deux branches appartient à la gradation 2).
- Aucune généralisation hors de la base moissonnée ; aucun transport vers la science réelle : une méthode « qualifiée » l'est pour ces mécanismes plantés (additif positif au retard ℓ ; fond retiré en R2⁻).
- **B-θ** n'autorise rien sur des indicateurs réels ; **B-hors** ne réfute pas le théorème 1 (ses hypothèses n'y sont pas satisfaites).
- La qualification n'autorise que l'emploi de la méthode dans un préenregistrement distinct de la gradation 2 ou 3.
- Un échec n'est pas « la méthode est fausse » : c'est « la méthode n'identifie pas ce mécanisme dans ce bruit ».
- Antériorité (R8) : plantation d'effets connus dans des données réelles = pratique établie (références SUPPOSÉES ci-dessus) ; la méthode n'est pas revendiquée comme inédite.

## Prédiction chiffrée et signe attendu

Toutes les grandeurs sont des **paris de l'auteur, SUPPOSÉS, sans aucune donnée**. Le verdict ne lit que les seuils et les tables. Une prédiction de grandeur hors fourchette est rapportée comme « prédiction de grandeur réfutée », sans effet sur les tables. Notations du brouillon 1 inchangées (R, O, H : affectation ; indices 0 à 3 : taille ; recouvrement, erreurs C, L, C⁰, erreur d'intervention). **En R2⁻, « trouve » exige le signe négatif.**

### Volet A — cause observée

| # | Méthode | Recouvrement (R2, R3, O2, O3) | **Recouvrement R2⁻ (signe −)** | Erreur C (β = 0) | Erreur L | Erreur C⁰ | Signe, grandeur ; intervention | Critère de mort de la rivale | Confiance |
|---|---|---|---|---|---|---|---|---|---|
| PA-T0 | T0 | 0 | 0 | 0 | 0 | 0 | effet prédit nul ; erreur d'intervention = 1,00 | importance non nulle de C ou effet non nul : **erreur de plomberie** (arrêt) | 1,00 |
| PA-T1 | T1 | 0,85 à 1,00 (moyen, fort) ; 0,3 à 0,8 (faible) | comme R2 à 0,10 près | R0 : 0,02 à 0,10 ; O0 : 0,05 à 0,20 ; H0 : 0,4 à 0,9 | 0,3 à 0,9 | R ≤ 0,10 ; O 0,05 à 0,25 ; H 0,4 à 0,9 | signe juste ; biais (collisionneur, H) ; erreur d'intervention 0,2 à 0,6 | erreur L regroupée sous R ≤ 0,10 : HR-T1 morte, leurre non jugeable | 0,70 |
| PA-T2 | T2, brute (critère d'information bayésien) | 0,4 à 0,9 | 0,3 à 0,9 (le fond planté augmente la variance des non traitées : sens de l'artefact inconnu) | 0,05 à 0,30 | 0,3 à 0,9 | 0,05 à 0,5 | non lu | témoin ; **standardisée : ≤ 0,3** (v = 1/2, fiche § 1, p. 8) | 0,60 |
| PA-T2b | T2b, brute et standardisée | 0,2 à 0,8 | 0,2 à 0,8 | 0,05 à 0,30 | 0,2 à 0,8 | 0,05 à 0,5 | non lu | témoin ; **écart brute − standardisée ≤ 0,10** (le motif de corrélation survit à la standardisation, fiche § 1, p. 9) ; s'il chute de plus de 0,10, rapporté | 0,45 |
| PA-M1 | M1 | 0,2 à 0,8 | comme R2 à 0,10 près | ≤ 0,05 (R, O) ; ≤ 0,10 (H) | ≤ 0,05 | ≤ 0,05 (R, O) ; ≤ 0,10 (H) | quand C est retenu : signe juste, erreur d'intervention ≤ 0,3 (R, O) ; abstention 0,5 à 1,0 en H2, H3 | erreur L ou C⁰ au-delà de S9 : HR-M1 morte ; recouvrement sous S9 : « trop prudente » | 0,55 ; 0,30 (qualifiée) |
| PA-M2 | M2 | 0,85 à 1,00 au bon retard | comme R2 à 0,10 près | R0, O0 ≤ 0,05 ; H0 0,3 à 0,9 | 0,3 à 0,9 | R, O ≤ 0,10 ; H 0,3 à 0,9 | signe juste ; erreur d'intervention ≤ 0,3 (R, O) | erreur L regroupée sous R et O ≤ 0,10 : HR-M2 morte | 0,60 |
| PA-M3 | M3 (DirectLiNGAM) | 0,6 à 0,95 (R, O) | comme R2 à 0,15 près | R0 ≤ 0,10 ; H0 0,3 à 0,9 | 0,3 à 0,8 | H 0,3 à 0,8 | signe juste ; grandeur biaisée ; erreur d'intervention 0,2 à 0,6 | erreur L ≤ 0,10 (R, O) et recouvrement selon S9 : HR-M3 morte ; **|standardisé − brut| et |redimensionné − brut| ≤ 0,10 prédits** (ART(M3) vrai) ; au-delà : prédiction réfutée, artefact constaté | 0,55 ; 0,70 (invariance) |
| PA-M3b | M3b (ICA-LiNGAM), descriptive | 0,4 à 0,9 | — | — | — | — | — | **|redimensionné − brut| > 0,10 prédit** (fiche § 1, p. 2) ; sinon la mesure d'échelle de S12 est peu sensible (rapporté) | 0,50 |

**Prédiction de symétrie de signe (nouvelle, descriptive).** Pour T1, M1, M2, M3 : |recouvrement R2 − recouvrement R2⁻| ≤ 0,10 (confiance 0,6). Une asymétrie au-delà est rapportée ; la ligne 7bis de la Table A décide seulement si la règle de recouvrement n'est pas tenue en R2⁻.

### Volet B-θ — cause latente dans les hypothèses du théorème 1 (décision si D-1 = option 2 ou 3)

r̃ = médiane, sur les 5 graines d'entraînement, de la corrélation maximale avec z₁ (Métrique).

| # | Méthode | Part des mondes Bθv avec r̃ ≥ 0,70 | MCC médian (5 sources, Bθv) | Stabilité médiane | Effet (Bθv1, sélection supervisée S21) ; fausse détection (Bθv0) | Critère de mort de la rivale | Confiance |
|---|---|---|---|---|---|---|---|
| PB-M4θ | M4 | **0,75 à 0,95** ; Bθc : comme M5 (écart < 0,15) | 0,70 à 0,95 | 0,75 à 0,95 | trouve (bon facteur, signe aligné +, seuil 0,01) dans 0,6 à 0,95 des mondes ; fausse détection ≤ 0,10 | part sous S19, ou stabilité < 0,70 : HR-M4θ morte (« dans le théorème, sur ce volume fini et ce bruit réel, l'iVAE n'identifie pas ») | 0,60 |
| PB-M5θ | M5 | 0,1 à 0,5 | 0,2 à 0,5 | 0,3 à 0,6 | 0,2 à 0,7 | en Bθv, part ≥ S19, stabilité ≥ 0,70 et écart < 0,15 : **thèse « pas à lui seul » réfutée ici** (déclenche S14 (c)) | 0,60 |
| PB-Δθ | écart M4 − M5 de r̃ | **Bθv : +0,25 à +0,60 ; Bθc : −0,10 à +0,10** | — | — | — | Bθv : estimation < 0,15 ou borne basse ≤ 0 | 0,55 |

Ancrage (non opposable comme prédiction, contexte seulement) : dans la simulation du papier (M = 40 segments, L = 1 000 points, d = n = 5), l'iVAE dépasse 0,95 de coefficient de corrélation moyen et l'autoencodeur ordinaire échoue (fiche § 3, p. 6–7, figure 2). Nos fourchettes sont plus basses : volume par valeur de u plafonné par S8 (au plus 1 000 paires par environnement, donc par valeur de u), sortie réelle bruitée, graines médianes plutôt que meilleures.

### Volet B-hors — robustesse hors théorème (décision si D-1 = option 1 ; descriptif si option 2)

| # | Méthode | Part des mondes Bv avec r̃ ≥ 0,70 | Stabilité médiane | Effet (Bv1, S21) ; fausse détection (Bv0) | Captation de la popularité | Critère de mort | Confiance |
|---|---|---|---|---|---|---|---|
| PB-M4h | M4 | **0,3 à 0,8** (abaissé : hors théorème) ; Bc : comme M5 | 0,6 à 0,9 | 0,4 à 0,9 ; ≤ 0,10 | 0,3 à 0,7 | lecture « non robuste hors théorème » si part sous S11 ; ne réfute pas le théorème | 0,40 |
| PB-M5h | M5 | 0,1 à 0,5 | 0,3 à 0,6 | 0,3 à 0,8 | ≥ 0,6 | comme PB-M5θ | 0,60 |
| PB-T3 | T3 | 0,0 à 0,4 | 1,00 | sans objet | ≥ 0,7 | témoin de variance | 0,60 |
| PB-Δh | écart M4 − M5 | Bv : 0,00 à +0,40 ; Bc : −0,10 à +0,10 | — | — | — | Bv : estimation < 0,15 ou borne basse ≤ 0 : « avantage non robuste hors théorème » | 0,40 |

**Prédictions transversales (signe seul, descriptives ; inchangées, plus deux).** (i) Recouvrement croissant avec |β| ; (ii) erreurs C⁰ plus fortes dans le tiers supérieur de popularité sous O ; (iii) en D2, retour au nominal des erreurs L et C⁰ de T1, M2, M3 ; (iv) en D1, M1 s'abstient plus souvent ; **(v)** écart M4 − M5 plus grand en B-θ qu'en B-hors (le passage hors théorème coûte) ; **(vi)** sous-étude à 50 graines : la dispersion entre graines de r de M5 dépasse celle de M4 en Bθv1.

**Verdicts attendus (SUPPOSÉ).** Volet A : inchangés (T1, M2, M3 : « confondent le leurre », confiance 0,6 ; M1 : sans préférence nette). Bθ : « oui sous hypothèse » (Table Bθ, ligne 9), confiance 0,55. B-hors : « non robuste » ou « robuste partiellement », sans préférence. Si toutes les méthodes du volet A sont non qualifiées : « aucune méthode d'observation pure n'identifie ce mécanisme dans ce bruit ; les gradations 2 et 3 doivent apporter l'affectation », jamais « la fertilité n'a pas de cause identifiable ».

## Métrique

**Unité de réplication, ensemble d'ajustement, ensemble d'intervention, sortie, candidates du volet A, décisions par méthode, issues, taux, vérité contrefactuelle et intervention jamais vue : inchangés** par rapport au brouillon 1 (§ Métrique), avec les précisions suivantes.

- **T2** : d = cause si V précède la sortie dans l'ordre des variances et si son coefficient dans le lasso **sélectionné par critère d'information bayésien** est non nul (fiche § 1, p. 7) ; signe = signe du coefficient.
- **T2b** : idem, ordre par coefficient de détermination croissant (R² de chaque variable sur toutes les autres candidates, calculé dans l'échelle de la variante).
- **M3** = DirectLiNGAM ; **M3b** = ICA-LiNGAM, mêmes règles de décision, descriptive.
- **Issues en R2⁻** : « trouve » = d(C) = cause **et signe négatif** ; « se trompe sur C » inclut d(C) = cause avec signe positif. Vérité contrefactuelle : τ*_I < 0 ; e_I = |τ̂_I − τ*_I| / |τ*_I|.

**Artefacts (mesures, Plan § 6).**
- v_var = part des arêtes du sous-graphe planté **entre variables observées** (C → sortie ; C → L ; sous O, S → C et D → C) où la variance de la cause est strictement plus faible que celle de l'effet (égalité comptée 1/2 ; même convention que la triabilité par la variance, fiche § 1, p. 4, § 3.1), en échelles brute et standardisée.
- **v_R² (nouveau)** = même part, le critère étant le coefficient de détermination de chaque variable régressée sur toutes les autres candidates ; calculée en échelles brute **et standardisée** ; c'est la mesure du motif que la standardisation n'efface pas (fiche § 1, p. 9).
- Recouvrement en échelles brute, standardisée et redimensionnée ; par tiers de S, D, A.

**Volet B (B-θ et B-hors).** Sur 20 % des paires-années tenues à l'écart de l'entraînement (ensemble E), coupé en deux moitiés E₁ et E₂ par le rôle 15 :
- **Graines** : chaque méthode (M4, M5) est entraînée avec **5 graines** (S18). Pour chaque graine g : r_g = maximum sur k de |ρ_S(z₁, ẑ_k)| (Z en B-hors), sur E. **r̃ = médiane des r_g** : aucune sélection de la meilleure graine (la graine pèse plus que l'objectif, fiche § 2, p. 5–6).
- **MCC (B-θ, nouveau)** = moyenne sur les 5 sources des |ρ_S(z_i, ẑ_π(i))| après appariement π par affectation linéaire (maximisation de la somme des |ρ_S|), médiane sur les graines. Alignement sur la mesure du papier (coefficient de corrélation moyen après affectation linéaire, fiche § 3, p. 7). Le rang de Spearman est choisi parce que l'identification n'a lieu qu'à transformation élément par élément près (fiche § 3, p. 6, théorèmes 2 et 3). LECTURE À CONFIRMER : le type de corrélation employé par le papier (Pearson ou Spearman) n'est pas donné par la fiche. Ce choix n'est pas une invention de chiffre ; il est écrit comme choix.
- **Stabilité** = médiane, sur les 10 paires de graines (M § 13), de max_k' |ρ_S(ẑ^a_k*(a), ẑ^b_k')|, où k*(a) est la dimension de la graine a la plus corrélée avec la latente vraie (évaluation) et l'appariement avec la graine b se fait **sans la vérité**.
- **Captation de la popularité** (B-hors seulement) : inchangée.
- **Étape d'effet — sélection supervisée, écrite comme telle (S21).** Dans la pratique, on ne connaît pas la vérité : on choisit le facteur par sa relation à la sortie. C'est une **supervision par la sortie** (fiche § 2, portée (b)) ; le contraste M4 − M5 sur r̃ reste « variable auxiliaire contre rien » parce que r̃ n'emploie pas la sortie ; l'étape d'effet est supervisée **à l'identique** pour M4 et M5. Procédure, pour la graine médiane (celle dont r_g est la médiane ; en cas d'égalité, le plus petit indice) : sur E₁, régression de g(Y⁺) sur toutes les dimensions apprises et sur S, D, A, g(Y) ; k̂ = dimension au plus grand |coefficient| standardisé ; sur E₂, régression de g(Y⁺) sur ẑ_k̂ et S, D, A, g(Y), test bilatéral au seuil 0,01. **« Trouve l'effet »** = k̂ = k* **et** coefficient significatif **et** signe aligné positif (signe du coefficient × signe de ρ_S(ẑ_k̂, z₁)). En Bθv0 et Bv0 : « fausse détection » = coefficient significatif sur E₂, quel qu'en soit le signe. **Oracle (descriptif)** : même test sur ẑ_k*, sans sélection.
- Écart apparié M4 − M5 de r̃ par monde ; intervalle à 95 % par 2 000 rééchantillonnages des mondes.

**Mondes exclus (inchangé)**, plus : un monde B-θ est exclu si la base n'offre pas 22 valeurs distinctes de u (alors **tous** les mondes B-θ le sont : B-θ non exécutable, verdict « non concluant », Liste d'arrêt).

## Seuil

**Tous les seuils de ce préenregistrement sont des marqueurs de gel. Lazar les gèle en une ligne datée dans `registres/decisions.md` ; aucun défaut ne s'applique, ni à 48 heures ni autrement.** Pour chaque seuil : la valeur (marqueur), la recommandation de l'auteur, sa raison. Une recommandation n'est pas une valeur. **S1 à S16 : numérotation et recommandations du brouillon 1 conservées, sauf S7, S12 (précision), S14 (déclencheurs ajoutés) et S15, marqués « mis à jour ». S17 à S21 : nouveaux.**

**S1 — Niches et paires** (inchangé)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : niche = thème principal OpenAlex de l'œuvre, dans son environnement ; au moins 30 œuvres publiées avant la première année du panel ; paires non ordonnées internes à un environnement.
- Raison : celle du brouillon 1 (étiquette externe ; réserve de fuite temporelle du classifieur, SUPPOSÉ ; D3 mesure la sensibilité).

**S2 — Calendrier** (inchangé)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : panel = années complètes moins les deux dernières, au plus 20 ; référence = 5 premières années ; fenêtre = 6e année à la dernière moins τ_max ; ℓ = 2 ; τ_max = 3.
- Raison : celle du brouillon 1 (SUPPOSÉ). Repère publié, non transposé : l'effet d'un décès de « superstar » devient significatif trois à quatre ans après (fiche § 6, p. 17, art. 15) ; il porte sur un autre traitement et une autre sortie, d'où aucun changement de ℓ.

**S3 — Tailles d'effet et forme (choix vraiment ouvert)** (inchangé)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : β ∈ {0 ; 0,1 ; 0,2 ; 0,4} en écarts-types σ_e, effet additif ; β = 0 contrôle de plomberie. R2⁻ : voir S20.
- Raison : celle du brouillon 1 (M, § 8 : statistiques attendues 3,0 ; 6,0 ; 12,0).

**S4 — Affectation de C (et de C⁰)** (inchangé ; s'applique aussi à R2⁻, affectation au hasard)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : π_0 = 0,10 ; κ ∈ {0,5 ; 1 ; 1,5} cyclique par (environnement, bloc de cinq ans) ; γ_O = γ_H = 1,0.
- Raison : celle du brouillon 1.

**S5 — Facteur caché et leurre** (inchangé)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : H ~ normale standard par paire ; η = 0,4 ; logit P(L = 1) = −3 + 2,5·C + 1,0·H.
- Raison : celle du brouillon 1.

**S6 — Volet B-hors** (inchangé dans ses valeurs ; renommé : il ne régit plus que B-hors)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : K = 8 indicateurs, réseau aléatoire 16-16 sur (Z, S, D, A, g(Y⁰)) standardisés, bruit 0,1 ; Bv : μ_u ~ uniforme(−2 ; 2), σ_u ~ uniforme(0,5 ; 2) ; Bc : normale standard ; β_Z ∈ {0 ; 0,4} ; d = 6 ; u = environnement × bloc de cinq ans.
- Raison : conserver le volet du brouillon 1 comme mesure de robustesse ; **les violations du théorème sont voulues et écrites** (W5).

**S7 — Nombre de mondes** (mis à jour)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **100** par condition de décision du volet A (12 conditions) **et 100 pour R2⁻** ; **B-θ : 50** par condition (4 conditions, 200 mondes) ; **B-hors : 30** par condition si D-1 = option 2 (120 mondes), **50** si option 1 (200 mondes) ; **50** par condition descriptive (D1 à D4) ; variantes d'échelle sur les 30 premiers mondes de chaque condition du volet A, R2⁻ compris.
- Raison : M § 1 à § 3 (inchangé) ; à 30 mondes par condition, la règle d'identification regroupée (60 mondes) demande 44 réussites, tenue avec 0,680 pour une part vraie de 0,75 et 0,110 pour 0,65 (M § 11) : suffisant pour un descriptif, trop faible pour décider.

**S8 — Niveaux de décision et plafond (choix vraiment ouvert : le plafond)** (inchangé)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : au plus 1 000 paires par environnement ; α_M1 = 0,05 avec correction de Bonferroni (version approchée de la prédiction invariante : **SUPPOSÉ**, PDF manquant) ; environnements de M1 = sous-domaine × bloc de cinq ans (sous NT1) ; α_M2 = 0,01, sélection 0,05 (SUPPOSÉ) ; seuil d'effet total de M3 = 0,05.
- Raison : celle du brouillon 1. Effet en B-θ : le plafond fixe aussi au plus 1 000 points par valeur de u, ordre de grandeur des 1 000 points par segment de la simulation du papier (fiche § 3, p. 6–7).

**S9 — Règles de qualification du volet A (choix vraiment ouvert)** (inchangé ; s'applique à R2⁻ avec le signe négatif)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : recouvrement BB ≥ 0,70 (79 sur 100) ; erreur C BH ≤ 0,15 (8 sur 100) ; erreurs L et C⁰ BH ≤ 0,10 sur 400 (28 sur 400) ; intervention médiane ≤ 0,30, borne haute ≤ 0,40.
- Raison : M § 1 à § 3 ; avec R2⁻, conjonction de 5 règles tenue avec 0,818 pour un recouvrement vrai de 0,85 partout, 0,998 pour 0,90 (M § 9).

**S10 — Lecture sous confusion cachée** (inchangé)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : robuste = erreur relative médiane ≤ 0,50 en H2 et H3 ; prudente = abstention ≥ 0,50, règles d'erreur sous H tenues.
- Raison : celle du brouillon 1.

**S11 — Règles du volet B** (inchangé dans ses valeurs ; s'applique à B-hors, et à B-θ par renvoi de S19 ; r remplacé par r̃, effet mesuré selon S21)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : identification : part des mondes Bv (Bv0 et Bv1 regroupés) où r̃ ≥ 0,70, BB de Wilson ≥ 0,60 ; stabilité médiane ≥ 0,70 ; avantage : écart M4 − M5 ≥ 0,15 et BB > 0 ; contrôle : |écart| < 0,15 en Bc ; effet : « trouve l'effet » (S21) dans ≥ 90 % des mondes Bv1, fausse détection ≤ 10 % des mondes Bv0.
- Raison : M § 4, § 6 (100 mondes), § 11 (60 mondes). Réserve : avec la sélection supervisée sur demi-échantillon et l'exigence k̂ = k*, le seuil de 90 % est exigeant ; l'auteur le garde (numérotation et valeur stables) et le signale à Lazar.

**S12 — Artefacts** (inchangé dans ses trois règles ; précision ajoutée)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : invariance d'échelle |standardisé − brut| ≤ 0,10 et |redimensionné − brut| ≤ 0,10 sur 30 mondes ; domination par le tri par variance : T2 brut ≥ méthode − 0,05 **et** chute de la méthode > 0,10 en standardisé → « artefact d'ordre des variances » ; popularité (B-hors) : corrélation facteur apparié de M4 / première composante principale ≥ 0,9 → audit. **Précision** : T2 emploie le critère d'information bayésien ; la règle de domination ne couvre que l'artefact que la standardisation efface ; l'artefact qui lui survit relève de S17.
- Raison : Reisach et collègues 2021, désormais vérifié sur page : la variance croît le long de l'ordre causal dans les modèles simulés génériques (fiche § 1, p. 1) ; standardiser ramène v à 1/2 (p. 8) ; les méthodes fondées sur l'erreur quadratique moyenne chutent après standardisation (p. 8–9).

**S13 — Validation de la base** (inchangé, plus un booléen)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : celle du brouillon 1 (3 environnements, 15 niches, 100 paires, 12 années, références résolues ≥ 0,30, sortie non nulle ≥ 0,02, références vers le futur ≤ 0,01, doublons = 0), **plus** : nombre de valeurs distinctes de u de B-θ ≥ S19 (booléen seulement).
- Raison : celle du brouillon 1 ; condition de rang du théorème 1 (fiche § 3, p. 5).

**S14 — Audit de symétrie (R4)** (mis à jour : déclencheurs ajoutés)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : déclencheurs (a) à (g) du brouillon 1 (en (c) : M5 atteint la règle d'identification en Bv **ou en Bθv**), plus **(h)** T2b atteint la règle de recouvrement de S9 en échelle standardisée dans R2 et R3 (un tri trivial suffit : le banc est « facile à tromper ») ; **(i)** |recouvrement R2 − recouvrement R2⁻| > 0,30 pour une méthode candidate ; **(j)** M4 en Bθc atteint la règle d'identification (la condition (iv) n'y est pas remplie) ; **(k)** une graine de la sous-étude à 50 graines donne r ≥ 0,90 pour M5 en Bθv1 alors que r̃ de M5 < 0,50 (la sélection de graine aurait fabriqué une identification).
- Raison : un seul jeu de déclencheurs pour le trop propre et le trop mauvais (inchangé).

**S15 — Budget de processeur** (mis à jour)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **110 heures** de temps mural au plus (option 2 de D-1, 5 graines : ≈ 107 h, M § 12 ; option 1 : ≈ 87 h ; temps unitaires SUPPOSÉS), sans instance payante ; règle de réduction **avant** tout monde de décision si l'estimation sur les 20 mondes de validation dépasse le budget : (1) conditions descriptives D1 à D4 à 30 mondes ; (2) B-hors à 20 mondes par condition (si option 2) ; (3) variantes d'échelle à 15 mondes ; (4) graines de B-hors à 3 ; (5) sous-étude à 50 graines réduite à 1 monde ; **jamais** les conditions de décision du volet A, R2⁻, ni les 5 graines de B-θ.
- Raison : aucune dépense ; le coût est du temps de calendrier avant la porte G0 ; une réduction qui toucherait la décision changerait les caractéristiques opératoires.

**S16 — Ensemble d'intervention** (inchangé ; R2⁻ comme R)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : année t_I tirée ; I = décile inférieur de propension (O, H), 10 % au hasard (R, R2⁻) ; do(C = 1) contre do(C = 0).
- Raison : celle du brouillon 1.

**S17 — Motif de corrélation que la standardisation n'efface pas** (nouveau)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : mesurer v_R² en échelles brute et standardisée sur les 30 mondes de chaque condition du volet A ; exécuter le témoin T2b ; **mention « recouvrement égalé par le tri par coefficient de détermination »** pour toute méthode candidate dont le recouvrement standardisé en R2 et R3 ne dépasse pas celui de T2b de plus de 0,05 alors que v_R² médian standardisé ≥ 0,80 ; cette mention n'est pas une disqualification (aucune perturbation simple n'efface le motif) mais **déclenche S14 (h)** si T2b passe lui-même la règle de recouvrement.
- Raison : une chaîne simulée à forte triabilité laisse des coefficients de régression standardisés croissants qui orientent la chaîne au-dessus du hasard en échelles brute, standardisée et harmonisée (fiche § 1, p. 9, § 5.1) ; l'épreuve doit pouvoir le constater chez nous. Seuil 0,80 : choix de l'auteur, sans chiffre de littérature (le critère publié de 2023 est SUPPOSÉ).

**S18 — Graines d'entraînement du volet B** (nouveau ; décision D-2)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : **5 graines** par méthode (M4, M5) et par monde, dans B-θ et B-hors ; r̃ = médiane ; stabilité sur les 10 paires ; **sous-étude à 50 graines** sur 2 mondes (indice 0 de Bθv1 et de Bθc1), descriptive, avec S14 (k).
- Raison : 50 graines par configuration dans Locatello et collègues (fiche § 2, p. 4) ; la graine et les hyperparamètres comptent plus que l'objectif (p. 5–6 ; p. 6 : l'objectif seul explique 37 % de la variance des scores, objectif × régularisation 59 %, le reste la graine) ; deux graines (brouillon 1) donnaient une stabilité sur une seule paire. Coût (M § 12) : 3 graines ≈ 86 h, 5 ≈ 107 h, 10 ≈ 161 h (option 2).

**S19 — Variante B-θ** (nouveau ; décision D-1)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : n = 5 sources gaussiennes conditionnelles, k = 2 (moyenne et variance modulées), μ_i(u) ~ uniforme(−2 ; 2), σ_i(u) ~ uniforme(0,5 ; 2) tirés indépendamment par u et par monde ; **u = environnement × année après la période de référence, au moins 22 valeurs distinctes** ; K = d = 5 ; mélange injectif carré à poids orthogonaux, pente 0,2 ; bruit 0,1 ; observations continues ; β_Z ∈ {0 ; 0,4} sur z₁ seule ; Bθc : μ_i, σ_i constants en u ; règles de décision = celles de S11 appliquées à r̃(z₁) ; mention « identification complète » si MCC médian ≥ 0,70 en Bθv.
- Raison : hypothèses (i) à (iv) du théorème 1 (fiche § 3, p. 5), famille exponentielle conditionnelle (p. 3), observations continues (corrigendum, p. 9), k = 2 pour échapper à la proposition 1 (p. 6), λ aléatoires indépendants (p. 15). nk + 1 = 11 (M § 10) ; 22 = marge de 2, parce que le résultat est asymptotique (p. 6, théorème 4) et que le papier fait varier 10 à 50 segments (p. 7, figure 3a). u = environnement × année après la référence donne au moins 21 valeurs avec la base minimale de S13 (3 environnements, 12 ans) et 33 avec 16 ans (M § 10) : la base minimale ne suffit pas, d'où le booléen de S13.

**S20 — Condition à effet négatif R2⁻** (nouveau ; décision D-3)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : affectation au hasard (S4) ; fond planté de loi de Poisson de moyenne 0,2·σ_e au retard ℓ sur chaque paire-année non traitée ; effet de C = −0,2·σ_e ; 100 mondes ; condition **de décision** : règle de recouvrement de S9 avec signe négatif (ligne 7bis de la Table A) ; règle d'intervention de S9 en R2⁻ incluse dans INT_R.
- Raison : prédiction de signe à deux branches (Hypothèse ; Borjas et Doran, fiche § 7, p. 76 et p. 28–29) ; « moyen » (β = 0,2) parce que c'est la taille où la plupart des méthodes sont prédites détecter (M § 8) : un échec n'y viendra pas de la puissance. Caractéristique opératoire : une méthode à 0,85 partout et 0,75 en R2⁻ passe la conjonction avec 0,180 (M § 9) : la ligne 7bis attrape une détection asymétrique.

**S21 — Sélection supervisée du facteur à l'étape d'effet** (nouveau ; décision D-5)
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation : ensemble E tenu à l'écart (20 %) coupé en deux moitiés égales (rôle 15) ; sélection de k̂ sur E₁ (plus grand |coefficient| standardisé dans la régression de g(Y⁺) sur toutes les dimensions et sur S, D, A, g(Y)) ; test sur E₂ au seuil bilatéral 0,01 ; « trouve l'effet » exige k̂ = k* ; oracle en descriptif.
- Raison : classer le facteur par son coefficient sur la sortie est une supervision (fiche § 2, portée (b)) ; sélectionner et tester sur les mêmes données gonflerait la fausse détection en Bv0 ; l'exigence k̂ = k* évite de compter comme réussite un effet trouvé sur un mauvais facteur.

### Récapitulatif des seuils à geler

| Seuil | Objet | Recommandation en une ligne | État |
|---|---|---|---|
| S1 | niches, paires | thème principal, ≥ 30 œuvres avant le panel ; paires internes | inchangé |
| S2 | calendrier | panel sans les 2 dernières années (≤ 20) ; référence 5 ans ; ℓ = 2 ; τ_max = 3 | inchangé |
| S3 | tailles d'effet (ouvert) | β ∈ {0 ; 0,1 ; 0,2 ; 0,4}, additif | inchangé |
| S4 | affectation | π_0 = 0,10 ; κ ∈ {0,5 ; 1 ; 1,5} ; γ_O = γ_H = 1,0 | inchangé |
| S5 | facteur caché, leurre | η = 0,4 ; logit P(L) = −3 + 2,5 C + 1,0 H | inchangé |
| S6 | volet B-hors | K = 8, d = 6, réseau 16-16, Bv / Bc, β_Z ∈ {0 ; 0,4} | inchangé (renommé) |
| S7 | mondes | A 100 (+ R2⁻ 100) ; B-θ 50 ; B-hors 30 (ou 50) ; D 50 ; échelles 30 | mis à jour |
| S8 | niveaux, plafond (ouvert) | 1 000 paires par environnement ; α 0,05 / 0,01 ; effet total 0,05 | inchangé |
| S9 | qualification volet A (ouvert) | BB ≥ 0,70 ; BH ≤ 0,15 ; BH ≤ 0,10 (400) ; intervention ≤ 0,30 (≤ 0,40) | inchangé |
| S10 | confusion cachée | robuste ≤ 0,50 ; prudente ≥ 0,50 | inchangé |
| S11 | volet B | r̃ ≥ 0,70, BB ≥ 0,60 ; stabilité ≥ 0,70 ; écart ≥ 0,15 ; contrôle < 0,15 ; effet 90 % / 10 % | inchangé (r̃, S21) |
| S12 | artefacts | échelle ≤ 0,10 ; tri par variance − 0,05 ; composante principale 0,9 | inchangé (précisé) |
| S13 | base | celle du brouillon 1 + valeurs de u ≥ S19 | complété |
| S14 | audit R4 | (a) à (g) + (h) à (k) | mis à jour |
| S15 | budget | 110 heures, réduction écrite | mis à jour |
| S16 | intervention | décile inférieur de propension | inchangé |
| S17 | motif de corrélation | v_R² standardisé ≥ 0,80 et T2b à 0,05 près → mention ; S14 (h) | nouveau |
| S18 | graines | 5 par méthode, médiane ; sous-étude 50 graines sur 2 mondes | nouveau |
| S19 | B-θ | n = 5, k = 2, u ≥ 22 valeurs, K = d = 5, continu | nouveau |
| S20 | R2⁻ | fond 0,2·σ_e retiré par C ; 100 mondes ; décision | nouveau |
| S21 | sélection supervisée | demi-échantillons, seuil 0,01, k̂ = k* | nouveau |

Aucun seuil retiré.

## Plan d'analyse

### 1. Données (inchangé)

Moisson (session-depot, n° 265), manifeste cité par chemin et empreinte ; distinction lecture / non-lecture du brouillon 1 ; un environnement par sous-domaine moissonné.

### 2. Panel des paires de niches (inchangé)

Niches et paires (S1), années (S2), plafond (S8) ; sortie réelle Y⁰ ; covariables S, D, A, g(Y) calculées sur les seules données ≤ t et recalculées sur la base plantée ; σ_e et quantiles de propension écrits au manifeste, lus par personne avant le verdict.

### 3. Plantation du volet A (par monde)

Étapes 1 à 6 du brouillon 1, inchangées. **R2⁻ (nouveau)** : étape 3 remplacée par — pour chaque paire-année **non traitée** de la fenêtre, B = F⁻¹_Poisson(U ; 0,2·σ_e) œuvres en t + ℓ, U uniforme du rôle 5 par paire-année ; aucune œuvre pour une paire-année traitée. Contrefactuel : do(C = 0) ajoute le fond avec les mêmes U ; do(C = 1) le retire. Aucune œuvre réelle n'est jamais supprimée.

### 4. Plantation du volet B (par monde)

- **B-hors** : celle du volet B du brouillon 1 (S6 ; rôles 5, 7, 8).
- **B-θ** : u = (environnement × année après la référence) ; μ_i(u), σ_i(u) (rôle 13) ; z_i (rôle 13) ; mélange f (rôle 14) ; x = f(z) + ε ; œuvres-ponts de z₁ au retard ℓ (rôle 5) ; H présent comme au volet A ; pas de C, L, C⁰. u est transmis à M4 seulement.

### 5. Méthodes et hyperparamètres (fixés ici)

- T0, T1, M1, M2 : inchangés.
- **T2** : ordre par variance marginale croissante (échelle de la variante) ; lasso de chaque variable sur ses prédécesseurs **sélectionné par critère d'information bayésien** (`LassoLarsIC(criterion="bic")`, `scikit-learn`), comme « sortnregress » (fiche § 1, p. 7).
- **T2b** : idem, ordre par coefficient de détermination croissant.
- **M3** : **DirectLiNGAM** (`lingam.DirectLiNGAM`), élagage par défaut de la bibliothèque, version figée ; aucune connaissance a priori d'ordre.
- **M3b** (descriptive) : ICA-LiNGAM (`lingam.ICALiNGAM`, SUPPOSÉ quant au nom de classe), mêmes entrées.
- **M4** : iVAE ; B-hors : encodeur 8 → 64 → 64 → 2d, d = 6 (inchangé) ; **B-θ : encodeur 5 → 64 → 64 → 10, décodeur 5 → 64 → 64 → 5, d = 5** ; a priori normal factorisé dont moyenne et log-variance sortent d'un réseau à une couche de 32 unités sur l'encodage de u ; Adam, pas 10⁻³, lots de 256, 50 époques ; au plus 50 000 paires-années d'entraînement ; **5 graines** (S18).
- **M5** : identique, a priori normal standard, u absent ; 5 graines.
- T3 : inchangé.
- Variantes d'échelle (T2, T2b, M1, M2, M3, M3b, T1) : brute, standardisée, redimensionnée.
- Toute exception levée et consignée ; aucun repli silencieux ; un échec de convergence compte « ne trouve pas » et est rapporté. **Une graine qui échoue ne se remplace pas** : r̃ est la médiane des graines restantes, et plus d'une graine échouée sur 5 dans un monde exclut ce monde pour la méthode (rapporté).

### 6. Artefacts à traquer

Table du brouillon 1, inchangée, avec les modifications suivantes :

| Artefact | Mécanisme | Mesure | Conséquence |
|---|---|---|---|
| Ordre des variances (fiche § 1, p. 1, p. 4–5) | variance croissante le long de l'ordre causal | v_var brut et standardisé ; T2 (critère d'information bayésien) ; variantes d'échelle | S12 |
| **Motif de corrélation (fiche § 1, p. 9)** | la standardisation laisse des corrélations croissantes le long de la chaîne | **v_R² brut et standardisé ; T2b** | **S17 ; S14 (h)** |
| **Sensibilité à l'échelle selon la variante de LiNGAM (fiche § 1, p. 2 et p. 6)** | ICA-LiNGAM sensible, DirectLiNGAM non (attendu) | variantes d'échelle de M3 et M3b | ART(M3) ; M3b descriptif |
| **Sélection de graine (fiche § 2, p. 5–6)** | une bonne graine fabrique une identification | médiane sur 5 graines ; sous-étude à 50 graines | S18 ; S14 (k) |
| **Supervision cachée (fiche § 2, portée (b))** | choisir le facteur par la sortie | S21 (demi-échantillons, k̂ = k*) | Tables Bθ et B-hors |
| **Signe imposé** | banc qui ne plante qu'un signe | R2⁻ | S20 ; ligne 7bis ; S14 (i) |

Les autres lignes (échelle, degré et âge, effet Matthieu, survivants, fuite temporelle, œuvres synthétiques reconnaissables, popularité apprise) sont celles du brouillon 1.

### 7. Conditions

| Code (graine) | Volet | Affectation | β (ou β_Z) | Mondes | Rôle |
|---|---|---|---|---|---|
| R0 à R3 (1 à 4) | A | au hasard | 0 ; faible ; moyen ; fort | S7 | décision |
| O0 à O3 (5 à 8) | A | popularité observée | idem | S7 | décision |
| H0 à H3 (9 à 12) | A | facteur caché | idem | S7 | décision |
| **R2⁻ (21)** | A | au hasard | **−0,2 (fond retiré)** | S7 | **décision (S20)** |
| Bv0, Bv1 (13, 14) | B-hors | — (Z variable selon u) | 0 ; 0,4 | S7 | décision si D-1 = 1 ; descriptive si 2 |
| Bc0, Bc1 (15, 16) | B-hors | — (Z constant selon u) | 0 ; 0,4 | S7 | idem (contrôle) |
| **Bθv0, Bθv1 (22, 23)** | **B-θ** | — (lois variables selon u) | 0 ; 0,4 | S7 | **décision si D-1 = 2 ou 3** |
| **Bθc0, Bθc1 (24, 25)** | **B-θ** | — (lois constantes selon u) | 0 ; 0,4 | S7 | **idem (contrôle)** |
| **Sous-étude (26)** | B-θ | mondes d'indice 0 de 23 et 25, rejoués | — | 2 mondes × 50 graines | descriptive (S18) |
| D1 à D4 (17 à 20) | A | inchangées | inchangées | S7 | descriptives |

### 8. Graines (R9)

- Racines inchangées : RACINE = 20261110 ; RACINE_VALIDATION = 20261111.
- `numpy.random.SeedSequence(entropy=RACINE, spawn_key=(code_condition, indice_monde, code_rôle[, graine]))` (numpy ≥ 1.25) ; **graine d'entraînement g ∈ {0, …, 4}** en cinquième élément (brouillon 1 : 0 et 1) ; sous-étude : g ∈ {0, …, 49}, code de condition 26, plantation recopiée des clés des conditions 23 et 25 (même monde au bit près, garde).
- Codes de rôle du brouillon 1 inchangés (0 à 11, 20 + rang, 99) ; **nouveaux** : 13 sources et paramètres λ(u) de B-θ ; 14 mélange de B-θ ; 15 coupure E₁ / E₂ ; méthodes T2b = 29, M3b = 30 ; rééchantillonnage : contrastes 8 (R2⁻) et 9 (écart M4 − M5 en B-θ). Le fond de R2⁻ emploie le rôle 5 (nombres aléatoires communs avec le contrefactuel).
- Manifeste par run : inchangé, plus le nombre de valeurs distinctes de u (non imprimé), les versions de `scipy` et la liste des graines par méthode.

### 9. Comparaisons, multiplicité, puissance

Inchangé (conjonctions sans correction ; jugeabilités J_L, J_O, J_H), plus : R2⁻ entre dans la conjonction de recouvrement (M § 9) ; Table Bθ sur 100 mondes regroupés (M § 6) ; B-hors à 60 mondes regroupés si descriptif (M § 11). Coût : environ 1 900 mondes plus les entraînements du volet B (S15, M § 12).

### 10. Ordre d'exécution

Verdict du collisionneur sur la question 6 → **brouillon 3** → contre-lecture par un modèle différent d'Opus (R2) → corrections → décisions D-1 à D-7 et gel de S1 à S21 par Lazar (ligne datée) → (D-6 : fiches vérifiées des PDF manquants, si option 1) → remplacement des marqueurs et scellement → écriture du code → gardes R5 sur base jouet entièrement synthétique → réception de la moisson (empreinte, manifeste : pas une lecture) → validation de la base (S13, booléens seulement, dont le compte des valeurs de u) → validation de la plomberie sur 20 mondes de RACINE_VALIDATION (dont R2⁻ et B-θ ; estimation du temps → réduction de S15 si besoin) → manifeste scellé → **une seule invocation** des mondes de décision et descriptifs → lecture par un sous-agent neuf (R13) → verdict scellé → GO de Lazar.

## Suites : gradation 2 (expériences naturelles publiées comme vérité)

Pas une décision de ce préenregistrement : ce qu'une méthode qualifiée ici devra reproduire dans le préenregistrement distinct de la gradation 2. Chaque « vérité » est un **signe**, une **taille**, un **délai** et une **unité**, avec la page de la fiche ; la **transposition** aux œuvres-ponts entre niches est écrite d'avance ; les **réserves** viennent des fiches. Aucun de ces chiffres n'est une prédiction de l'épreuve semi-réelle.

| Expérience | Traitement | Vérité : signe ; taille ; délai ; unité (page) | Transposition vers nos œuvres-ponts | Réserves (fiche) |
|---|---|---|---|---|
| **Azoulay, Graff Zivin et Wang** (document de travail NBER 14577, révisé juillet 2009) | décès prématuré et inattendu de 112 « superstars » des sciences de la vie (fiche § 6, p. 2 ; p. 8, art. 6) | signe **négatif** ; −0,086 (0,025) avec témoins, soit 8,79 % de baisse (p. 28, art. 26, tableau III, colonne 1b) ; significatif **trois à quatre ans après** le décès, sans résorption (p. 17, art. 15) ; unité : **coauteur**, publications pondérées par le facteur d'impact de la revue (p. 15–16, art. 13–14) ; placebo précisément nul (p. 24, art. 22 ; p. 48) | retrait d'un **nœud** : œuvres-ponts entre les niches que la superstar reliait (paires de niches où elle publiait), avant et après le décès, témoins appariés ; prédiction transposée : signe négatif, délai ≥ 3 ans | **mort d'un nœud ≠ contact** entre deux niches ; sortie individuelle, non citation-pont ; coauteurs seulement (p. 22–23, art. 20–21) ; pages du document de travail, non de la version de revue (SUPPOSÉE parue en 2010) ; incohérence interne colonne 2b / 1b (p. 17, art. 15) ; le décès est retrouvable dans OpenAlex ? **SUPPOSÉ** (pas de champ de décès ; liste externe nécessaire) |
| **Borjas et Doran 2012** (NBER 17800) | afflux de mathématiciens soviétiques après 1992 ; exposition = recouvrement par champ d'avant 1990, 63 champs (fiche § 7, p. 24–25, art. 23–24) | signe **négatif** pour les mathématiciens américains en place ; (après 1992) × corrélation : −0,133 (0,036) article par an, −19,577 (1,576) citations (p. 76, art. 75, tableau III, A) ; ≈ 2,2 articles sur 1992–2008 contre 6,8, environ un tiers (p. 28–29, art. 27–28) ; délai : effets de long terme au moins aussi grands que de court terme (p. 29, art. 28) ; unité : **individu**, exposition au niveau du **champ** | afflux de producteurs dans une niche : œuvres-ponts des niches en place exposées (par recouvrement de leurs références avec celles des arrivants) ; branche **H-C⁻** de la prédiction de signe | **niveau du champ**, non de la paire de niches ; sortie individuelle ; tendances préalables **non strictement parallèles** (p. 29, art. 28, figure VIIa) ; incohérence de période de long terme (p. 30 contre p. 76) et cellule « −2378 » (vraisemblablement −0,2378, SUPPOSÉ) ; aucune preuve d'agrandissement du « gâteau » (p. 55–56) |
| **Campos, Leon et McQuillin 2018** (*The Economic Journal*) | congrès 2012 de l'Association américaine de science politique annulé moins de 48 heures avant ; témoin : congrès du Midwest (fiche § 8, p. 3–4, art. 997–998) | signe **négatif** de l'annulation (donc positif du contact) ; −0,0241 (0,0088) sur la probabilité de collaborer avec un autre participant, moyenne 0,1563, ≈ −16 % ; même thème −0,0247 (0,0069) ; autre institution −0,0219 (0,0083) ; même institution −0,0085, non significatif (p. 12, art. 1006, tableau 4) ; **délai : LECTURE À CONFIRMER** (la fiche ne donne pas l'horizon de mesure) ; unité : **auteur-congrès** et **dyade** | contact entre niches présentes au même congrès : œuvres-ponts entre les niches des participants de 2012 contre celles du témoin ; branche **H-C⁺** ; c'est la plus proche du contact C planté | **coécriture**, non citation-pont ; **taux de base dyadique 3 828 sur 86 068 533, soit 0,004 %** (p. 17, art. 1011, note 21 ; M § 14 : environ 2,2 millions de dyades pour attendre 100 collaborations) : la transposition exige une puissance écrite d'avance ; programmes de congrès absents d'OpenAlex (SUPPOSÉ) ; une seule discipline (limite dite, fiche § 8, sans page) ; égalité des coefficients entre sous-échantillons non rejetée (p. 18, art. 1012) ; tableau d'équilibre en annexe non lu (p. 9) |
| **Iaria, Schwarz et Waldinger 2018** (*Quarterly Journal of Economics*) | coupure de la science internationale après 1914 (fiche § 9, p. 3, art. 929) | signe **négatif** de la coupure (donc positif du contact) ; part des références hors du camp −0,222, ≈ −85 % de la part d'avant-guerre (p. 23, art. 949, tableau IV) ; similarité des titres −0,5 écart-type, retour vers 1930 (p. 4, art. 930 ; p. 35, art. 961) ; production : −1,727 (0,638) au seuil du 1 % supérieur (p. 40, art. 966, tableau VIII) ; **délai** : dès « après 1914 » ; LECTURE À CONFIRMER pour un retard annuel plus précis ; unité : **article citant** (parts de références), chercheur, camp × champ | coupure du contact entre deux groupes de niches : œuvres-ponts **entre** groupes, avant et après ; c'est la plus « native » d'un réseau de citations ; branche **H-C⁺** | période **1900–1930**, couverture dans OpenAlex **non vérifiée** (SUPPOSÉ) ; unité « camp », non « niche » ; citations = approximations des flux de connaissance (p. 19, art. 945) ; écart hors du camp / dans le camp non significatif à 5 % au seuil du 1 % (p. 43, art. 969) ; les citations vers la recherche d'avant-guerre ne baissent pas (p. 3, art. 929) |

Lecture commune : les quatre identifient par un **choc extérieur** plus des hypothèses écrites (non-anticipation, tendances parallèles, absence d'interférence), jamais par le réseau de citations seul (fiche, lecture transversale : Azoulay p. 10–11, Borjas p. 24 et 27, Campos p. 3–4, Iaria p. 36 et 38). Les signes ne sont pas monotones en « contact » (fiche, lecture transversale, dernier point) : d'où la prédiction à deux branches.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites ; la première ligne vraie décide.

**Booléens communs** (inchangés), avec : REC_R⁻(M) = règle de recouvrement de S9 tenue en R2⁻ **avec le signe négatif** ; INT_R(M) inclut R2⁻ ; ART(M) = aucun artefact d'échelle ni d'ordre des variances (S12) ; la mention de S17 est portée à côté du verdict, sans changer la ligne.

**Audit de symétrie (R4)** : déclencheurs S14 (a) à (k) ; contenu et issues inchangés.

### Table A — volet A (T1, M1, M2, M3)

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | non V0 | **non concluant** |
| 1 | AUDIT_EN_ATTENTE | **non concluant** (audit en attente) |
| 2 | ARTEFACT | **non concluant** ; version nouvelle |
| 3 | non ART(M) | **non qualifiée : artefact d'échelle ou d'ordre des variances** |
| 4 | règle d'erreur C non tenue en R0 | **non qualifiée : invente une cause sans effet** |
| 5 | règle d'erreur L non tenue sous R | **non qualifiée : confond le leurre** |
| 6 | règle d'erreur C⁰ non tenue sous R | **non qualifiée : confond le jumeau sans effet** |
| 7 | non REC_R(M) | **non qualifiée : ne retrouve pas la cause plantée, même au hasard** |
| **7bis** | **non REC_R⁻(M)** | **non qualifiée : ne retrouve pas une cause de signe négatif** (détection asymétrique ou signe imposé) |
| 8 | non INT_R(M) | **détection seulement** |
| 9 | non J_O | **qualifiée pour la gradation 3 seulement**, « confusion observée non jugeable » |
| 10 | non (REC_O ∧ ERR_O ∧ INT_O) | **qualifiée pour la gradation 3 seulement** |
| 11 | non J_H, ou non ERR_H(M) | **gradation 3, et gradation 2 sous confusion observée seulement** (mentions du brouillon 1) |
| 12 | ROB_H(M) | **qualifiée pour les gradations 2 et 3, robuste sous confusion cachée** |
| 13 | PRU_H(M) | **qualifiée pour les gradations 2 et 3, prudente** |
| 14 | tout autre cas | **gradation 3, et gradation 2 sous confusion observée seulement** |

Notes du brouillon 1 inchangées (leurre non jugeable ; T0 = arrêt de plomberie ; T2 sans verdict). **T2b et M3b** ne reçoivent pas de verdict : T2b sert à S17 et S14 (h), M3b à S12 (témoin positif d'échelle). Si D-3 = option 2, la ligne 7bis est retirée (marquée « retirée ») et R2⁻ devient descriptive.

### Table Bθ — « dans les hypothèses du théorème 1, l'apprentissage non supervisé identifie-t-il la cause latente à lui seul ? » (décision si D-1 = option 2 ou 3)

Booléens : IDVθ(M) = règle d'identification de S11 sur r̃(z₁) en Bθv ; STABθ(M) ; AUXθ = écart M4 − M5 en Bθv ≥ 0,15, BB > 0 ; AUXθc = |écart| < 0,15 en Bθc ; EFFθ(M4) = règle d'effet de S11 avec S21.

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | non V0, ou B-θ non exécutable (moins de 22 valeurs de u) | **non concluant** |
| 1 | AUDIT_EN_ATTENTE | **non concluant** |
| 2 | ARTEFACT | **non concluant** ; version nouvelle |
| 3 | IDVθ(M5) ∧ STABθ(M5) ∧ non AUXθ | **le réseau libre identifie aussi bien que l'iVAE : la thèse « pas à lui seul » est réfutée dans ce monde** (issue permise) |
| 4 | non IDVθ(M4) | **dans les hypothèses du théorème, sur ce volume fini et ce bruit réel de sortie, l'iVAE n'identifie pas** : échec en échantillon fini, **pas une réfutation du théorème** (asymptotique, fiche § 3, p. 6, théorème 4) ; non qualifiée |
| 5 | non STABθ(M4) | **identification sans stabilité entre graines** : non qualifiée |
| 6 | non AUXθc | **contrôle en défaut** : avantage de l'iVAE quand la condition (iv) n'est pas remplie ; l'avantage ne vient pas de l'hypothèse ; non qualifiée |
| 7 | non AUXθ | **identification sans avantage démontré de la variable auxiliaire** : indécis |
| 8 | non EFFθ(M4) | **latente identifiée, effet faux, inventé ou attribué au mauvais facteur** : non qualifiée pour l'étape d'effet |
| 9 | tout autre cas | **oui sous hypothèse** : l'iVAE identifie avec la variable auxiliaire, le réseau libre non ; l'identification vient de l'hypothèse écrite ; qualifiée pour l'étape de représentation **là où les hypothèses du théorème sont défendables** ; portée sur des indicateurs réels donnée par la Table B-hors |

Mentions (sans changer la ligne) : « identification complète » si MCC médian ≥ 0,70 ; résultat de la sous-étude à 50 graines.

### Table B-hors — robustesse hors théorème (décision si D-1 = option 1 ; descriptive, sans qualification, si option 2)

Booléens comme au brouillon 1 (IDV, STAB, AUX, AUXc, EFF), sur r̃ et avec S21.

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | non V0 | **non concluant** |
| 1 | AUDIT_EN_ATTENTE | **non concluant** |
| 2 | ARTEFACT | **non concluant** ; version nouvelle |
| 3 | IDV(M5) ∧ STAB(M5) ∧ non AUX | **le réseau libre fait aussi bien hors théorème : « pas à lui seul » réfuté dans ce monde** (la non-gaussianité ou la variance de Z ont suffi) |
| 4 | non IDV(M4) | **iVAE non robuste à ces violations** (sources réelles dépendantes, comptes, u trop pauvre) ; **ne réfute pas le théorème** |
| 5 | non STAB(M4) | **retrouve sans stabilité entre graines hors théorème** |
| 6 | non AUXc | **contrôle en défaut** |
| 7 | non AUX | **robustesse sans avantage démontré de la variable auxiliaire** |
| 8 | non EFF(M4) | **latente retrouvée, effet faux ou mal attribué** |
| 9 | tout autre cas | **robuste hors théorème dans ce monde** : avantage empirique de la variable auxiliaire malgré les violations écrites ; **ne prouve pas** que l'hypothèse en est la cause |

Lecture combinée (option 2) : Bθ ligne 9 et B-hors ligne 9 → « qualifiée, robuste hors théorème » ; Bθ ligne 9 et B-hors ligne 4 → « qualifiée sous hypothèse, fragile hors théorème : n'employer que là où les hypothèses sont défendables » ; Bθ ligne 4 → non qualifiée quelle que soit B-hors.

Aucune lecture avant scellement ; rien de ces tables ne change après lecture ; toute déviation est écrite comme telle (R1). Le verdict est scellé puis soumis à Lazar pour GO (R13).

## Liste d'arrêt

Toutes les lignes du brouillon 1 sont conservées (moisson sans manifeste ; lecture avant scellement ; base ratée ; plomberie ; fuite temporelle ; agrégat synthétique ; `except` qui rend une valeur par défaut ; valeur non numérique ; non-convergence > 5 % ; exclusions > 2 % ; nombre de mondes ; manifeste tardif ; racines ; versions ; budget dépassé pendant la décision ; appel de modèle, réseau ou dépense ; déclencheur S14 ; marqueur restant ; ligne de gel absente). **Ajouts :**

| Condition | Action |
|---|---|
| Œuvre réelle supprimée ou modifiée par une plantation (R2⁻ compris) | arrêt (plomberie) |
| Base de R2⁻ en β = 0 différente au bit près de la base réelle ; fond planté présent sur une paire-année traitée | arrêt |
| Moins de 22 valeurs distinctes de u (B-θ) à la validation de la base | B-θ non exécutée ; Table Bθ « non concluant » ; consigné ; **jamais** de repli silencieux vers une autre définition de u après lecture |
| Indicateur de B-θ à valeurs entières ou discrètes ; dimension apprise ≠ 5 en B-θ | arrêt (hypothèse du théorème violée par le code) |
| r̃ calculé autrement que par la médiane des graines ; graine échouée remplacée par une autre | arrêt (sélection de graine) |
| k̂ choisi sur des données d'entraînement ou sur E₂ ; test sur E₁ | arrêt (double emploi des données) |
| T2 ou T2b sélectionnés autrement que par critère d'information bayésien | arrêt |
| M3 exécuté avec une autre classe que DirectLiNGAM | arrêt |
| Sous-étude dont la plantation diffère au bit près du monde d'origine | arrêt de la sous-étude ; consigné |
| Verdict du collisionneur sur la question 6 non intégré (section dédiée encore marquée) | pas de scellement (contrôlé par le validateur : marqueur restant) |

**Gardes testées sur un cas sain et sur un artefact (R5)**, sur base jouet synthétique, avant toute lecture de la moisson. Les treize gardes du brouillon 1 sont conservées ; **nouvelles** :
- **fond de R2⁻** : base jouet où l'effet négatif se calcule à la main ; égalité avec le code et aucune œuvre réelle retirée (sain) ; plantation fautive qui supprime une œuvre réelle, ou qui met le fond sur une paire traitée : détectée (artefact) ;
- **signe en R2⁻** : base jouet linéaire à effet négatif fort : M1, M2, M3, T1 trouvent C avec signe négatif (sain) ; méthode artefact qui rend la valeur absolue de l'effet : comptée « se trompe sur C » (artefact) ;
- **condition de rang** : base jouet à 30 valeurs de u : booléen vrai (sain) ; base jouet à 10 valeurs : booléen faux, B-θ refusée, Table Bθ « non concluant » (artefact) ;
- **B-θ identifiable** : base jouet B-θ à grand volume (40 valeurs de u, 1 000 points chacune, comme la simulation du papier, fiche § 3, p. 6–7) : M4 atteint r ≥ 0,90 (sain) ; même base en Bθc (lois constantes) : M4 ne dépasse pas M5 de plus de 0,15 (artefact : le contrôle mord) ;
- **indicateurs continus** : B-θ à indicateurs réels continus accepté (sain) ; indicateur arrondi à l'entier : refusé (artefact) ;
- **médiane des graines** : 5 valeurs connues, médiane exacte (sain) ; fonction qui rend le maximum : refusée (artefact) ;
- **sélection supervisée** : base jouet où le bon facteur a l'effet, sélection sur E₁ et test sur E₂, « trouve » (sain) ; base jouet Bv0 (aucun effet), 200 répétitions : fausse détection ≤ 0,02 avec demi-échantillons (seuil 0,01), et le code qui sélectionne et teste sur les mêmes données est refusé par la garde (artefact) ;
- **critère de T2** : sur base jouet linéaire triable (v = 1), T2 avec critère d'information bayésien retrouve l'ordre (sain) ; appel avec validation croisée : refusé (artefact) ;
- **motif de corrélation** : chaîne jouet à corrélations croissantes : v_R² standardisé = 1 et T2b retrouve l'ordre en standardisé (sain) ; même chaîne à ordre permuté au hasard : v_R² proche de 0,5 (artefact).

## À intégrer après le verdict du collisionneur sur la question 6

À REMPLIR — brouillon 3. Section volontairement vide : elle porte le marqueur du validateur, de sorte que le scellement reste impossible tant que le verdict n'est pas intégré. Points attendus (liste de contrôle, non exhaustive) :
1. Méthodes ajoutées ou retirées par le verdict (et leur place dans les tables A, Bθ, B-hors) ; ligne du récapitulatif des changements.
2. Critères de mort chiffrés par voie (relecture 6, RL6-08) : correspondance avec S9, S11, S19, S20.
3. Épreuve d'intervention **hors support** avec **ligne de base non identifiante** (RL6-04) : vérifier que S16 (décile inférieur de propension) et T1 la réalisent, sinon la compléter.
4. Mondes qui **violent** chaque hypothèse une à une (RL6-05) : inventaire de ce que l'épreuve viole déjà (H, non-linéarité, B-hors, D1, R2⁻) et de ce qui manque (dépendance entre latentes en B-θ, bruit gaussien, décalage dense des environnements).
5. Séparation **latentes / graphe / effet** (RL6-01) : vérifier que chaque verdict nomme son niveau.
6. Hyvärinen et Morioka 2016 contre 2017 (RL6-07) ; décalages parcimonieux et Perry et collègues 2022 (RL6-06) : place éventuelle dans l'épreuve.
7. Protocole de détection de ce que le modèle apprend en pratique (RL6-09) : comparer à la captation de la popularité et à T3.
8. Toute divergence entre le verdict et ce brouillon : écrite, avec la décision de Lazar si elle touche une hypothèse ou un seuil.

## Contre-lecture

À REMPLIR — contre-lecture à faire par un sous-agent neuf **d'un modèle différent d'Opus** (Fable 5.1 de préférence, sinon Sonnet 5.5 avec réserve d'indépendance), non-auteur des brouillons 1 et 2, des fiches de lecture, de la question 6, des réponses 5 et 6 et des relectures 5 et 6 ; **sur le brouillon 3** de préférence (après le verdict du collisionneur). Fichiers à lui donner explicitement : ce brouillon (empreinte au moment de la relecture) ; le brouillon 1 (base) ; les deux scripts et leurs sorties (à rejouer au bit près avec `python3 -I`) ; `docs/sources/pdf/identification-causale-v1/fiches-de-lecture-verifiees-v1.md` **et les neuf PDF empreintés** (pour vérifier chaque page citée) ; `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/prereg.py` ; `question-6-identification-collisionneur-v1.md`, `reponse-conv-audit-question-6-v1.md`, `relecture-fable-reponse-6-v1.md`, `reponse-fable-independante-questions-6-7-v1.md` ; le verdict du collisionneur ; rien de `donnees/`, rien de la moisson. Points à attaquer en priorité : (1) B-θ respecte-t-elle vraiment les hypothèses (i) à (iv) du théorème 1 (fiche § 3, p. 5), et la marge de 22 valeurs est-elle justifiée ? (2) la sélection supervisée de S21 rend-elle la règle d'effet de S11 (90 %) inatteignable ? (3) R2⁻ est-elle une vraie épreuve de signe ou un doublon de R2 ? (4) T2b et S17 : la mention sans disqualification est-elle cohérente avec S12 ? (5) les transpositions de la section « Suites » sont-elles honnêtes (mort d'un nœud, niveau du champ, coécriture, période) ? (6) les six points du brouillon 1 restent ouverts (leurre collisionneur, plafond S8, indicateur, exhaustivité de la Table A, jugeabilités, une seule réalisation du vrai bruit). Entrée à écrire ensuite : « Contre-lecture 1 », identifiant du sous-agent, empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
