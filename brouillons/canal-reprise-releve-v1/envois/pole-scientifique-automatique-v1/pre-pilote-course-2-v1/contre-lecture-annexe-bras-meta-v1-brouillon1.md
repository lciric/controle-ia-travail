# Contre-lecture de l'annexe des paramètres du bras méta, version 1, brouillon 1

**Auteur** : sous-agent Sonnet 5.5 neuf (modèle différent de l'auteur de l'annexe, Opus 5.5 ; R2). Je n'ai écrit aucune pièce lue ici. **Date** : 2026-10-31, 01:54 UTC. **Statut** : contre-lecture non scellée, sans compagnon ; je ne tranche rien.
**Interdits tenus** : rien lu sous `donnees/` ; aucun réseau ; aucun fichier existant modifié ; aucun `.sha256` écrit ; aucune clé lue. Mes essais ont tourné hors dépôt (`/tmp/cl/`, `python3 -I`, `PYTHONDONTWRITEBYTECODE`), sur des copies ; le compagnon de scellement a été neutralisé dans l'essai seulement (voir F).

**Pièces lues (empreintes à la lecture)** :
- annexe brouillon 1 : `3a2e8dc2f8d764674941498ab0da9a977e7cbbd1478d868428efb8d1ca3441a0` (compagnon conforme) ;
- préenregistrement brouillon 7 : `799b9ca9c4ec30d8ab2c782496643b64cdbfcd8ca09eb08b9b8694b0c8ece6f5` (lignes M9, S28, S29, S31, P14, R5 22a, 22b, 23, 24, A19 à A21) ;
- code v53 : `bisociateur_v53.py` `962eb8ce22d5af1bf59970e9ef9cab15620edef4d5e9746161bc302e97c2af02` ; `configuration_v53.py` `ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78` ; `course2_v53.py` (lignes 100-140, 325-400, 490) et `outils.py` (`extraire_bloc_json`) lus, empreintes non recalculées ici ;
- texte I `question-course-2-defense-fusion-v5.md` `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` ;
- synthèse v2 `23c2888ddd924b85a0bbd0009a17f64723399d69ffd17669f56c4fddf7d18a86` (décision 1 et défauts) ;
- réponses v2 : question 1 `0edee5d7…`, question 2 `adb640c6…`, question 3 `5f63dcb9…` (question 2 relue en détail, 1 et 3 consultées) ;
- Uzzi 2013 : `532970985650d07fe69c66d912dfae96d6f45522fcb72e92c88857f4fd101173` (compagnon conforme) ;
- décisions R-638, R-639, R-642, R-643, R-672 (`registres/decisions.md`) ;
- sortie v6 du calcul de puissance (pour un chiffre cité par l'annexe).

**Essais que j'ai joués moi-même** (scripts non versés, empreintes : `t1.py` `94afb2c3…`, `p14.py` `ad9e70fa…`) : (1) extraction du bloc, refus avec les deux champs à « À REMPLIR », acceptation avec un texte d'essai ; (2) profil des paires de niches ; (3) jeu d'essai de 10 fiches avec les fonctions réelles de v53 ; (4) poids −2, seuil textuel, nom libre de structure ; (5) rejeu du script P14 de l'annexe avec d'autres graines et trois lois a priori des niches ; (6) lecture des pages 469 et 471 d'Uzzi.

## Verdict

**Soumettable après corrections.** Le bloc lisible par le code est conforme et bloque comme annoncé ; les chiffres de l'annexe se rejouent ; les dix incompatibilités sont exactes. Mais trois défauts de fond doivent être traités ou assumés avant que Lazar approuve des valeurs : (1) la grille et les tables mettent dans le profil la paire n1–n2 que le programme lui-même fusionne, et n'y mettent jamais n5 ; (2) le pré-pilote n'éprouvera le profil que dans une minorité de lots (constat à remonter à Lazar, section C) ; (3) l'argument qui retire les jeux de données du compte vaut aussi pour des structures que le texte I impose à presque toutes les fiches. Aucun défaut ne rend la pièce dangereuse à soumettre : l'annexe se déclare brouillon et le bloc est refusé par le code tant que les champs ne sont pas remplis.

## A. Complétude par rapport au brouillon 7 — **tenu, avec deux réserves**

- S28 : kappa ≥ 0,40, Jaccard ≥ 0,30, marges constantes lues 1 ou 0 « dégénérée », conséquence « niches non lisibles », bras non retiré. Présents (section 1). Vérifié sur `kappa_niches` : la règle codée est bien celle écrite.
- S29 a à f : a grille (section 1), b communication (2), c structure forte (3), d bande (5), e forme et poids (6), f repli (6). Tous présents, avec raison, alternative et confiance, et le marqueur « À GELER par Lazar ». La table 11 les recapitule. Pas de valeur sans raison ni alternative, sauf : la liste des 20 structures (confiance 0,5, alternative limitée au seuil ; la liste elle-même n'a pas d'alternative) et la borne basse de la bande (voir CA1-07).
- Non-vacuité (garde 22a) : jeu d'essai de 10 fiches, résultat **rejoué par moi à l'identique** : 5 paires dans le profil, 36 hors profil, 4 refusées (même niche) ; argmax e01–e04 à 2,0 ; quatre autres paires à 1,5. Témoins hors profil conformes à ce que dit l'annexe. Mais : le jeu d'essai a été étiqueté par l'auteur de la table, après la table (il prouve que le code tourne, pas que la table est utile).
- P14 refaite : présente, script recopié en entier. **Rejeu avec mes graines** : 0 paire (6 fiches, accord 0,7, structure 0,3) zéro avec 0,594 ; 10 fiches zéro avec 0,255 ; aucune paire éligible 0,038 et 0,002. Les chiffres de l'annexe (0,59 ; 0,25 ; 0,039 ; 0,002) tiennent ; variantes [2 ; 4] (0,54 et 0,21) et c ≤ 2 (0,35 et 0,07) aussi. Réserve : le script et sa sortie ne sont pas versés (l'annexe le dit) ; la garde 22a exige « script rejoué, sortie nommée » : à verser avant scellement (CA1-12).
- Procédure de gel : section 9 complète (contre-lecture, brouillon 2, mot de Lazar, scellement, empreinte injectée, É0, A20). Rien de manquant. La table 11 demande bien un mot de Lazar par valeur, sans défaut à 48 heures.

## B. Grille des six niches — **à corriger**

**Fiches typiques du texte I.** Le champ « hypothèse » d'une fiche (affirmation centrale) se range ainsi :
- **Axe 2** (forme : loi, garantie, impossibilité) et **axe 5** (preuve dans Lean, bornes) : n5, sans ambiguïté. Axe 4 (préenregistrement d'universalité, exclusion d'une famille) : n6, sans ambiguïté.
- **Axe 1** (« battre HELIOS » : statistique qui lit une couche et un jeton, agrégée dans le temps, avec plancher apparié, matériau Mahalanobis, auto-encodeurs, e-valeurs) : **n1, n2 ou n3 selon le lecteur**. Les mots-indices de n2 (« plancher apparié », « couche », « sonde ») sont imposés par le texte à toute fiche de l'axe 1 ; ceux de n1 (« agrégation dans le temps », « e-valeur ») et de n3 (« Mahalanobis ») sont dans le matériau. L'affirmation centrale d'une fiche d'axe 1 est une statistique qui est à la fois lecture d'activations et agrégation séquentielle : l'annexe l'admet (section 1, réserve : « le programme lui-même fusionne n1 et n2 »).
- **Axe 3** (pré-mortem : l'hypothèse porteuse qui cède, classe de faille parmi circularité, puissance, juges, linéarité, stationnarité…) : aucune niche naturelle ; n6 par défaut, mais « additivité dans le temps » et « stationnarité de P_0 » tirent vers n1. Choix forcé, sans « autre ».
- **Axe 7** (hors pré-pilote) : angles sur tout le contrôle (élicitation et sous-performance, conscience d'évaluation, débat, organismes modèles, délégation multi-agents, sabotage de la recherche automatisée, argumentaires de sûreté, facteurs humains) : **aucune niche** ; forcés en n4 ou n6.

Environ 40 % des fiches d'un lot de défense à cinq axes (axes 1 et 3) sont donc ambiguës, et ce sont précisément celles qui peuplent les niches du profil (n1, n2, n3). Le filtre « deux lecteurs d'accord » écarte les fiches dont les lecteurs divergent ; il ne protège pas contre deux fiches voisines de l'axe 1 que les lecteurs rangent, chacun de façon stable, l'une en n1 et l'autre en n2 : on fabrique alors une paire « loin » (e = 3) et « à canal faible » (c = 1) à partir de deux fiches du même axe, de la même case.

**Trous et recouvrements.**
- Trous : huit des quatorze cases de l'esquisse du texte I n'ont pas de niche (voir ci-dessus). Acceptable pour les cinq axes du pré-pilote, pas pour « les mêmes niches dans la course 2, pour toutes les cases » (section 1, périmètre) : à restreindre aux axes 1 à 5 ou à prévoir une grille pour l'axe 7.
- Recouvrements : n1 et n5 (« délai de détection », « bornes de délai » ; l'axe 5 (f) demande l'apport face aux bornes de délai) ; n2 et n3 (Mahalanobis sur activations, matériau de l'axe 1) ; n4 et n6 (« équipe rouge », « budget d'audit », « collusion », « puissance ») ; n3 et n6 (« calibration »). Les niches mélangent des natures différentes : par méthode (n1, n2, n3), par type d'énoncé (n5 : tout énoncé prouvé, quel que soit l'objet), par situation (n4), par tâche (n6).

**Tables à la main.**
- Cohérence interne : les deux tables sont symétriques et complètes ; les clés triées passent `lire_annexe_meta` ; les comptes de l'annexe se vérifient (7 paires faibles sur 15 ; 13 sur 15 à c ≤ 2 ; 4, 6 et 10 paires dans le profil pour [2 ; 3], [2 ; 4] et c ≤ 2). L'inégalité triangulaire est tenue sur e. Pas de contradiction c élevé / e élevé gênante.
- **Contradictions avec le texte de l'annexe** : (i) n1–n2 a un canal faible (c = 1, e = 3) alors que la section 1 écrit que le programme fusionne n1 et n2 ; c'est pourtant la paire la plus probable du profil (CA1-01) ; (ii) l'alternative (b) de la grille dit que fusionner n1 et n5, n3 et n2 ferait perdre « la paire la plus nette (lecture des activations contre bornes) », mais cette paire (n2–n5, c = 0, e = 5) est **exclue** du profil par la bande : la paire la plus nette n'est pas dans le profil proposé (CA1-02) ; (iii) **n5 n'apparaît dans aucune des 4 paires du profil** ; toute fiche d'axe 2 ou 5 est structurellement exclue (CA1-03) ; (iv) les quatre paires du profil ont toutes c = 1 et e = 3 : la borne basse de la bande (2) ne joue jamais (CA1-07).

## C. Profil et P14 — **constat majeur à remonter à Lazar**

**Nombre de paires de niches dans le profil** : 4 sur 15 (n1–n2, n1–n4, n1–n6, n3–n4), vérifié par code. Avec c ≤ 1 seul : 7 ; la bande en retire 3 (n2–n5 : e = 5 ; n4–n5 et n5–n6 : e = 4).

**Rejeu de la prédiction (100 000 tirages, mes graines)** :

| Lot | Loi a priori | Médiane | Zéro dans le profil | Aucune paire éligible |
|---|---|---|---|---|
| 6 fiches | annexe (n1 0,30 … n6 0,05) | 0 | 0,59 | 0,04 |
| 6 fiches | « n6 fort » (n6 0,35, n5 0,20) | 0 | 0,67 | 0,04 |
| 6 fiches | « n2 fort » (n2 0,30) | 0 | 0,66 | 0,04 |
| 10 fiches | annexe | 1 | 0,25 | 0,002 |
| 10 fiches | « n6 fort » | 1 | 0,36 | 0,003 |
| 10 fiches | « n2 fort » | 1 | 0,34 | 0,002 |
| 15 fiches | annexe | 4 | 0,06 | 0,000 |

La loi a priori de l'annexe donne 5 % à n6, alors que ses propres mots-indices d'n6 (« famille tenue à l'écart », « transfert », « universalité », « préenregistrement ») décrivent les axes 3 et 4, soit environ 40 % des axes : cette loi paraît sous-estimer n6 (SUPPOSÉ des deux côtés). Conclusion robuste : la fraction de lots sans paire du profil est entre 0,6 et 0,7 à 6 fiches et entre 0,25 et 0,36 à 10 fiches.

**Le pré-pilote n'éprouve-t-il que le repli ?** À 6 fiches : oui, dans environ 6 lots sur 10 ; à 10 fiches : dans 1 lot sur 3 à 1 sur 4. Même quand une paire du profil existe, il y en a une (médiane 1) : le pré-pilote n'a qu'une paire méta, donc ne peut éprouver ni le classement par score (poids 0,5, égalités) ni le contraste profil / hors profil. Il éprouve la chaîne (lecture, paire, fusion, aiguilleur, juges), ce qui est le but affiché de M9 (descriptive pour l'effet, décisive pour la chaîne). Mais le bras est étiqueté « méta, profil trou à structure commune » ; une fusion issue du repli est « la paire à deux indicateurs sur trois » : le nom de bras ne dit plus la même chose. L'annexe le dit (« c'est attendu, déclaré ») ; ce n'est pas encore traité comme un constat pour Lazar : **il doit lui être écrit en tête de la demande d'approbation.**

**Aggravants que l'annexe ne chiffre pas** : (a) l'indépendance supposée entre « structure partagée » et « canal faible » est optimiste : deux niches qui communiquent peu partagent, par définition, moins de structures (le « trou à structure commune » est une conjonction rare) ; (b) `choisir_paires` retire des candidates les paires déjà prises par un bras antérieur (ordre tiré) : la seule paire du profil peut être prise par le bras basique ou le bras Gu-Krenn, et le bras méta tombe alors au repli, sans que P14 en tienne compte (CA1-09) ; (c) la proportion de fiches retenues (accord des deux lecteurs 0,7) est supposée uniforme, alors qu'elle est plus basse sur les axes 1 et 3, qui nourrissent le profil.

**Options pour Lazar** (avec l'effet mesuré par mon rejeu, accord 0,7, structure 0,3) :
1. **Accepter le repli comme mesure** et le dire dans le nom du résultat : « le pré-pilote éprouve la chaîne, non le profil » ; zéro coût ; la prédiction P14 est remplacée par celle de l'annexe. Avantage : honnête, rapide. Inconvénient : rien n'est appris sur la lisibilité du profil avant la course.
2. **Plus de fiches non aiguillées** : 15 fiches donnent une médiane de 4 paires du profil et zéro avec 0,06 ; mais le pré-pilote est borné à ≤ 10 fiches de passe 1 (M4/M5) et le coût monte (lectures d'étiquettes). Demande un devis.
3. **Élargir la bande à [2 ; 4]** : n'aide presque pas (zéro 0,54 à 6 fiches, 0,21 à 10) ; les deux paires ajoutées passent par n5 (n4–n5, n5–n6, e = 4) et n5 est rare dans la loi de l'annexe. **Retirer la bande** : zéro 0,47 et 0,14 ; contraire à R-638. **Élargir le canal à c ≤ 2** : zéro 0,35 et 0,07 mais « faible » cesse d'avoir un sens (10 paires sur 15).
4. **Revoir le seuil de structure** (par exemple compter une structure à nom « presque partagé ») : ce n'est pas un paramètre de l'annexe, c'est une modification du profil de R-638 : nœud de Lazar.

Ma lecture, sans trancher : l'option 1 est cohérente avec le brouillon 7 ; l'option 2 est la seule qui change la fréquence du profil sans toucher à R-638 ; l'option 3 ne sert pas.

## D. Fidélité à R-638 — **tenu avec un écart à trancher et une incohérence**

- Communication faible entre niches : tenu (propriété de la paire de niches, fixée avant toute fiche).
- Désaccord lu à part, hors score : tenu ; la lecture par paire après le scellement des paires est plus stricte que la garde de signature. Écart par rapport au brouillon 7 : M9 dit « rapporté pour chaque paire candidate » et un champ « affirmation centrale » recopié ; l'annexe lit au plus 5 paires et change l'entrée du lecteur (CA1-10).
- Éloignement non extrême selon Uzzi : tenu et bien marqué SUPPOSÉ (section E sur les pages).
- **Structure commune forte** : R-638 nomme « objet mathématique, méthode, jeu de données ». L'annexe retire le jeu de données du compte et l'avoue (« écart déclaré »). Mon avis de contre-lecteur : l'argument tient pour D1 (le texte I le fait servir à presque toutes les fiches), mais **le même argument vaut pour `om_somme_cumulee_temps_arret`, `om_martingale_e_processus` et `me_test_sequentiel_cusum`** : le glossaire impose « fausse alerte tenue à tout instant », l'axe 1 impose l'agrégation, l'axe 5 la borne de délai ; ces structures seront partagées par la plupart des fiches de n1, n2 et n5, et la probabilité de 0,3 de partager au moins une structure comptée est un chiffre posé, pas mesuré. L'annexe ne retire pas ces structures « quasi universelles » alors qu'elle dit le faire (section 3, raison) : l'incohérence est à corriger (CA1-04). La décision de compter ou non les jeux de données reste à Lazar, avec cette précision.
- « Forte » = au moins une structure partagée parmi 14 identifiants : très faible comme « forte » ; la confiance 0,55 est honnête.
- Ajouts non demandés par R-638 qui changent le profil : quatrième type « protocole » (lu, non compté) ; règle « deux lecteurs d'accord » (déjà dans le code) ; seuil c ≤ 1 ; union des structures des deux lecteurs (favorise les fiches à beaucoup d'étiquettes). Aucun ne contredit R-638 mais chacun est un choix à faire valider.

## E. Circularité et garde-fous — **tenu, avec deux réserves**

Les trois transpositions « oui » sont correctes : étiquette de pont indépendante (l'issue d'une fusion, lue par l'aiguilleur et les juges, n'utilise ni c, ni e, ni la niche ; la table c est écrite avant toute fiche et n'est jamais recalée) ; jeux disjoints (conception de l'annexe avant toute fiche, aucun ajustement entre générations sans annexe v2 scellée) ; puissance préalable (P14 refaite). Les trois « non » sont justifiés, avec journal : la rétrodiction inversée n'a pas d'équivalent sans issue datée ; le graphe amputé et le bras « popularité seule » (R-643 a retiré le bras hasard ; R-634 interdit la comparaison au pré-pilote) se réduisent à des journaux.

**Réserves.**
- **Fuite entre profil et jugement** : pas de fuite directe (les lecteurs ne voient pas les notes, les juges ne voient pas les étiquettes, la fusion est aveugle). Mais le score récompense par construction un trait qui facilite la note : **une paire à structure partagée (s ≥ 1, score croissant en s) est plus facile à fusionner de façon cohérente** ; les juges notent cohérence et plausibilité. Dans la course, une avance du bras méta sur le bras basique pourrait venir de ce lien mécanique et non d'un « trou » fertile. L'annexe ne le dit pas (elle traite le biais « fiches riches en étiquettes », pas celui-ci) : à ajouter aux garde-fous comme limite d'interprétation (CA1-08).
- **« Le bras basique sert de comparateur simple » (R-642)** n'est pas un bras « popularité seule » : le bras basique note par domaine et par concept (kappa), pas par popularité. La ligne du tableau section 7 le fait passer pour l'équivalent ; à reformuler (« aucun équivalent ; le journal des nombres de structures et de concepts tient lieu de contrôle descriptif »).
- Chiffre non retrouvé : « à 12 fusions, l'erreur-type d'une aire à 6 contre 6 est d'environ 0,2, sortie v6 ». Je ne le trouve pas dans `calcul-puissance-pre-pilote-course-2-v6.sortie.txt` (seules figurent les erreurs-types Hanley-McNeil de 0,09 et 0,12 pour P12). Mon calcul de Hanley-McNeil à aire 0,5 et 6 contre 6 donne environ 0,17 : de l'ordre annoncé, mais le renvoi est faux (R6, R7) (CA1-11).

Pages d'Uzzi vérifiées sur le PDF empreinté : p. 469, « top 5 % … through 8 years » ; p. 471, « peak impact occurred in the 85th to 95th percentile of median conventionality, an exceptionally high level » et légende de la figure 4 « after which the relationship reverses ». **Tenu.** Nuance non signalée : chez Uzzi, la nouveauté de queue est **toujours** favorable, à tout niveau de conventionnalité ; la « cloche » ne porte que sur la conventionnalité médiane. La transposition « bande qui exclut le plus lointain » est donc, comme l'annexe le dit, une forme et non un chiffre ; elle ne repose pas sur une cloche dans la distance, et rien chez Uzzi ne fonde l'exclusion du quasi identique (e = 1) (mineur, CA1-07).

## F. Bloc de configuration — **tenu**

Essai joué sur une copie hors dépôt, `verifier_scelle` neutralisé (aucun compagnon dans l'essai) :
- Le bloc extrait (dernier objet portant `parametres_bras_meta`) contient les 11 clés de `CLES_ANNEXE` (22 clés en tout ; les clés de plus sont ignorées).
- Avec « À REMPLIR » dans `contre_lecture` et `approbation_lazar` : refus « A20 : annexe sans contre_lecture déclarée ». Avec un texte d'essai : acceptation ; `garde_desaccord_hors_score` passe. **Les deux champs bloquent bien.**
- Types et règle de repli conformes : `structure_forte.nombre_min` entier, `types` liste ; `bande` liste à deux valeurs ordonnées ; `repli` dans `REPLIS_CONNUS` ; clés de communication et d'éloignement triées et présentes pour les 15 paires.
- Fragment de configuration : clés `bisociateur.meta.annexe.{chemin, sha256}` conformes à `configuration_v53` ; l'empreinte « À FOURNIR AU SCELLEMENT » est refusée comme annoncé (expression régulière à 64 caractères).

**Incompatibilités I-1 à I-10 :**
- I-1 **exacte** : `valider_niche` ne contrôle que le type ; `{"type": "me_test_sequentiel_cusum", "nom": "CUSUM"}` est accepté ; s exige l'égalité du couple.
- I-2 **exacte** : `course2_v53.py` écrit « non lu en v53 » pour le désaccord.
- I-3 : `kappa_niches` et `accord_jaccard` existent, aucun appel dans `course2_v53` ; exacte sur ce que j'ai lu.
- I-4 : le lecteur ne reçoit que `{niches, types_structure}` (identifiants) : exacte.
- I-5 : `la[0] != ma[0]` écarte la fiche : exacte.
- I-6 **exacte** : poids −2 accepté (score d'une paire du profil −3,0 ; le code la range alors « hors profil » car `s > 0` est faux) ; seuil textuel accepté par `lire_annexe_meta`, il lève un `TypeError` plus tard, au calcul.
- I-7 **exacte** : `choisir_paires` écrit « non produit (aucune paire notable) ».
- I-8 : exacte (`gagnant = next(...)`).
- I-9 : exacte (`"À REMPLIR" in p[k]` seulement ; « à remplir » en minuscules ou « TODO » passerait).
- I-10 : exacte.

**Incompatibilités manquantes** : **I-11** `choisir_paires` retire les paires déjà prises ; effet non chiffré dans P14 (CA1-09). **I-12** l'« artefact d'ordre » ajouté à la garde 24 (journal de désaccord horodaté avant le scellement des paires) n'a aucun support dans le code v53 (le désaccord n'est pas lu) : il dépend de la v54. **I-13** la lecture de désaccord par paire est une dépense nouvelle (appels payants) absente du devis et du script v6 ; l'estimation « ≈ 0,1 USD » vient d'un prorata dont la base est ambiguë (« 0,25 USD par lecture et par dix fiches ») et peut valoir jusqu'à 0,5 USD ; à intégrer à M7 et au plafond (CLAUDE.md : toute dépense sur devis).

## G. Ce qui empêche de soumettre l'annexe à Lazar

Rien n'est bloquant au sens strict. À faire avant la soumission, par ordre d'importance : traiter ou assumer CA1-01, CA1-02, CA1-03, CA1-04 (cohérence grille/tables/texte) ; écrire le constat P14 en tête de la demande à Lazar avec les options de la section C (CA1-05) ; verser le script P14 et la sortie ; corriger les renvois faux (CA1-11) ; vérifier DEP10 (verdicts des questions 4 à 7 scellés), que l'annexe elle-même déclare non vérifié (réserve R1 de l'annexe, que je n'ai pas levée).

## Constats

| N° | Gravité | Constat | Preuve | Correction demandée |
|---|---|---|---|---|
| CA1-01 | majeur | La paire n1–n2 est dans le profil (c = 1, e = 3) alors que l'annexe écrit elle-même que le programme fusionne n1 et n2 ; deux fiches voisines de l'axe 1 peuvent être rangées chacune de façon stable en n1 et n2 et fabriquer une paire « loin » par bruit d'étiquette. | Annexe section 1 réserve et tables ; texte I axe 1 ; `course2_v53._notes` (le filtre ne compare que les deux lecteurs d'une même fiche). | Soit fusionner n1 et n2 (grille à 5 niches), soit relever c(n1, n2) à 2 ou 3 et dire l'effet sur le profil ; soit écrire la limite et un contrôle (lot des fiches d'axe 1 rangées dans deux niches). |
| CA1-02 | moyen | L'alternative (b) de la grille appelle n2–n5 « la paire la plus nette » du profil ; cette paire (c = 0) est exclue par la bande (e = 5). | Annexe sections 1 et 5 (tables). | Corriger la phrase, ou assumer que la paire à canal nul est écartée comme extrême, ce qui est un résultat de lecture d'Uzzi à dire. |
| CA1-03 | majeur | n5 n'appartient à aucune paire du profil : toute fiche d'axe 2 ou 5 (environ 40 % des axes) est exclue du bras méta par construction. | Calcul : partenaires de n5 à c ≤ 1 : n2 (e = 5), n4 (e = 4), n6 (e = 4). | Dire la limite en tête de l'annexe ; décider si n5 doit avoir un partenaire (bande, table ou grille). |
| CA1-04 | moyen | L'argument « jeux de données universels, donc non comptés » vaut aussi pour les structures séquentielles imposées par le texte I ; l'annexe ne les retire pas. Écart à R-638 à trancher en l'état. | Texte I glossaire et axes 1 et 5 ; annexe section 3. | Retirer ou signaler ces structures, ou renoncer à l'argument ; mesurer la fréquence sur le jeu d'essai (non sur des fiches réelles). |
| CA1-05 | majeur | Le pré-pilote n'éprouve le profil que dans 40 % (6 fiches) à 65-75 % (10 fiches) des lots, et une seule paire du profil au mieux. Constat à remonter à Lazar avec options. | Rejeu : zéro 0,59 à 0,67 (6 fiches), 0,25 à 0,36 (10 fiches). | Placer en tête de la demande d'approbation ; options de la section C. |
| CA1-06 | moyen | La loi a priori des niches (n6 5 %, n4 10 %) contredit les mots-indices de n6 et la structure en cinq axes ; indépendance structure / canal optimiste. | Annexe section 6 ; texte I axes 3 et 4. | Justifier la loi ou donner la fourchette complète (mon rejeu : 0,67 et 0,36). |
| CA1-07 | mineur | La borne basse de la bande (2) ne sert à aucune paire du profil ; Uzzi ne fonde pas l'exclusion du quasi identique (la nouveauté de queue est toujours favorable ; la cloche ne porte que sur la conventionnalité médiane). | Quatre paires du profil toutes à e = 3 ; Uzzi p. 471. | Dire que la bande effective est e = 3 ; reformuler la phrase sur Uzzi. |
| CA1-08 | moyen | Biais de conception non listé : un score croissant en structures partagées sélectionne des paires faciles à fusionner de façon cohérente, ce que les juges notent. | Annexe section 7 (aucune ligne sur ce point) ; score `1 + 0,5 × s`. | Ajouter une limite d'interprétation pour toute comparaison méta / basique en course ; reformuler la ligne « popularité seule » (le bras basique n'en est pas un). |
| CA1-09 | moyen | `choisir_paires` retire les paires prises par un bras antérieur ; la seule paire du profil peut être prise, le méta tombe alors au repli. P14 ne le chiffre pas. | `bisociateur_v53.choisir_paires` (`prises`) ; ordre tiré. | Chiffrer dans le script v7 ; ajouter I-11. |
| CA1-10 | moyen | Le désaccord lu par paire après sélection (5 paires, anonyme, sur le champ « hypothèse ») diffère du brouillon 7 (chaque paire candidate, champ « affirmation centrale » recopié) ; I-12 (artefact d'ordre sans support de code) et I-13 (dépense) absents de la liste. | Brouillon 7 M9 ; annexe section 4 ; `course2_v53` ligne 491. | Écrire l'écart à M9 pour Lazar ; ajouter I-12, I-13 ; chiffrer la dépense. |
| CA1-11 | mineur | « Erreur-type 0,2 à 6 contre 6, sortie v6 » : renvoi non retrouvé dans la sortie v6 (HM calculé : ≈ 0,17). Autres références : « Shi-Evans, page en ligne », « Yegros-Yegros, Dunbar » restent à vérifier (R7) avant d'être utilisées dans un papier. | Sortie v6 ; calcul HM. | Corriger le renvoi ou retirer le chiffre. |
| CA1-12 | mineur | Script P14 et sortie non versés, garde 22a exige script rejoué et sortie nommée. | Annexe en-tête et section 6 ; mon rejeu confirme les chiffres. | Verser avec compagnon avant scellement. |
| CA1-13 | mineur | Le format d'une structure dans la lecture (`{"type", "nom"}`) n'est pas décrit dans l'annexe, qui montre `"structures": [...]` de chaînes ; les écarts de forme feraient rejeter la lecture par `valider_niche`. | Annexe section 1 (« règle de lecture ») ; `valider_niche`. | Écrire le format exact à recopier dans la consigne du lecteur. |
| CA1-14 | mineur | Couverture : huit cases de l'esquisse du texte I sans niche ; « mêmes niches pour toutes les cases » en course 2. | Texte I annexe 1 (grille des sous-domaines). | Limiter la portée aux axes 1 à 5 ou prévoir une grille d'axe 7. |
| CA1-15 | mineur | Le champ `contre_lecture` ne contrôle que la non-vacuité (I-9) : cette contre-lecture devra être citée avec son empreinte, pas seulement nommée. | Code `lire_annexe_meta`. | Prévu par la procédure (section 9, point 5) ; v54. |

*Fin. Aucune valeur n'a été gelée ni tranchée ; ce document ne vaut pas approbation.*
