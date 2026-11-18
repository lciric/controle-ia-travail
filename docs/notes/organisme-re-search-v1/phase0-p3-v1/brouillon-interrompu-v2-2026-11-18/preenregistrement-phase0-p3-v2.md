# Préenregistrement — phase 0 de P3 (panorama de candidats offerts au questionneur, monté sur l'instrument de P1), organisme d'idéation, v2

**Ce texte est la version 2. Il remplace, sans l'écraser, le texte v1 scellé `preenregistrement-phase0-p3-v1.md` (sha256 d3fd6dedad90ac18009bfe3e45f98bf183dfbfab8c3bca2670b4482bdff58685, commit e0923a07), qui reste en place, et porte la contre-lecture du modèle J `contre-lecture-phase0-p3-v1.md` (sha256 f254324bf5bb1a4ee62eaa1dce5aacb904c7a05e9b7e1256d858782e0b38c016, commit 9cb52d00 ; verdict « non scellable » ; bloquants C-1 et C-2, majeurs C-3 à C-5, mineurs C-6 à C-8), avec son programme de contrôles (8ed6f6abeb9d245e5545f2d5d239b809fd3873cd887b76a81b771cd8834800c0) et sa sortie (ab140b09e4fffdb1eeff2e7c303b246a9662beea2bcee4172201c0a4a329b8f7), et la décision de la mère sur C-2 : option (a).** Les chiffres marqués [CL-A], [CL-C], [CL-E] sont lus dans les sections A, C et E de cette sortie.

Gabarit suivi : `prereg/gabarit-preregistrement-v1.md` (8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e), sections dans son ordre, plus les sections propres à cette tâche.

- Auteur : modèle I (seul auteur du texte et du code de P3, v1 et v2).
- Date (UTC) : 2026-11-18 ; reprise pour la v2 commencée après réception de la contre-lecture ; ce texte écrit à partir de 2026-11-18T06:56:22Z (`date -u`, jamais écrit à la main).
- Statut : **rien n'est exécuté sur la configuration de ce texte**, ni de la v1 ; **rien n'est adopté dans l'organisme** ; aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau ; aucune hypothèse ni revendication du programme n'est changée. Le nombre d'appels de la phase 1 **n'est pas engagé** et ne porte aucun prix.
- Code (même dossier, R12, noms neufs) : `panorama_p3_v2.py`, `lanceur_phase0_p3_v2.py`, essais `test_phase0_p3_v2.py`. Les fichiers v1 restent en place et ne doivent plus être lancés. Versés ensemble sur la branche `lot/compte-organisme-v1` : ce texte scellé d'abord, son empreinte posée ensuite dans le lanceur v2, puis code et essais scellés.
- **Code de P1 réemployé par import, sans modification** (dossier `../phase0-p1-p2-v1/`) : `mondes_reponses_p1p2_v1.py` (2c80a833e311b2983fbe6a31d401ac80e3aa03e8d7ccbcb4c3e515d577ebab04), `questionneurs_p1_v2.py` (2870503014f301208258e0b4b2310c20b7d1713aadc9ac8d6911ed98f5cded3e), `lanceur_phase0_p1p2_v2.py` (da4312e74d64f0898be4c3259486e61d0ff7357ff9d160a34cca4d345368c47c), et par lui `mesure_forme_p2_v1.py` (b3da53aa5dd665c386b9e62a46deb92d94ae418369f147e220e99421fe32b932). Compagnons et empreintes vérifiés par le lanceur v2 avant tout calcul. Le banc de P1 est l'instrument rendu « discriminant » par `verdict-phase0-p1-p2-v2.md` (471a4a4172a9285cc3e4676623341de6fdb3d65fa47363e27768de9ff42184a1).
- Pièces lues : celles de la v1 (propositions 2b882f8d…, contre-lecture d'ensemble f81c778d…, lecture 21d00c6d…, dossier de P1), plus la contre-lecture de la v1 et ses deux pièces ci-dessus. Source lue seulement au lancement : course v67 (21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71), pour la garde de disjonction ; évaluateur de l'organisme (26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632), lecture seule.
- Conditions : conditions de la mère (R-3186), P3 ; décision de la mère sur C-2 (option (a)).
- Conventions : aucun nom de modèle de la famille du rédacteur ; proposeurs nommés argon et kimi.

## Bloc « effort et échantillonnage gelés »

**Empreinte du bloc « effort et échantillonnage gelés » : bbcc4c11c5f59dc359e01bca950fe242c4d453fe6700d72cb3c860dbdff815e7**

Configuration gelée (`CONFIG["p3"]`, JSON canonique, clés triées ; racine des graines 20261118 ; le texte « proposeurs réels » du bloc dit que leurs réglages, rendu du panorama et de l'historique compris, seront gelés au manifeste de la phase 1) :

```
{"K": 8, "appels": {"cartes_par_monde": 4, "proposeurs": 2}, "delta_equivalence": 0.05, "delta_position": 0.05,
 "deltas_sensibilite": [0.03, 0.04, 0.05, 0.0625, 0.075, 0.1],
 "echangeabilite": {"echantillon_voisines": 64, "marges": {"entropie_nat": 0.02, "part_voisines_distinctes": 0.03}},
 "factices_artefact_roles": ["plate", "centrale"],
 "factices_critere": ["hasard", "premier", "dernier", "plate", "centrale", "compatible", "contradicteur", "famille"],
 "factices_rapportes": ["reconnaisseur:0.15", "evitant:0.5"], "factices_taux_de_base": ["hasard", "plate", "centrale"],
 "limite_lois_sans_leurre": 16384, "mondes": 2048, "niveau": 0.975, "niveau_position": 0.995, "politique_refus": "arret",
 "predicats_principaux": 42, "predicats_structurels": 51, "puissance": 0.8, "puissance_repetitions": 400,
 "puissance_tirages": 2000, "questionneur_des_questions": "aleatoire", "rho_evitant": 0.5, "rho_min": 0.15,
 "seuil_signature_nat": 0.3, "sonde_questions": 2048, "sonde_score": 256, "sondes_factices": {"sonde": 256, "sonde_q": 1024},
 "t_questions": 4, "t_sensibilite": [0, 2, 4, 8], "taille_espace_H": 65536, "taux_de_base": 0.29, "tirages_bootstrap": 10000}
```

Le lanceur refuse de partir si cette empreinte n'est pas dans ce texte, si le nombre de mondes est sous la taille analytique, ou si la règle gelée simulée à cette taille ne rend pas chaque issue vraie avec la puissance gelée.

## Hors table : P3 lève des indécidables, l'écart est déclaré (constat P-1)

Inchangé depuis la v1. P3 répond aux lignes C2 et C4, restées indécidables : **essai hors table, écart déclaré**. Cette phase 0 ne porte que sur C2 (reconnaissance), et seulement sur la mesure ; C4 n'est ni éprouvé ni dimensionné. Toute phase payante reste la décision de Lazar.

## Hypothèse

**Option (a) de la mère, écrite.** Pour chaque monde planté, le questionneur pose d'abord **t = 4 questions fermées au monde** sur le banc de P1 (prédicats empiriques de P1, répondeur exact de P1, ordre de présentation tiré par graine) ; **ensuite** le panorama de K = 8 candidats lui est offert, et il rend une carte de reconnaissance (une position). « Sans aide » : au moment du choix, rien ne vient du répondeur sur les candidats — l'état ne porte que K, le panorama et l'historique des t questions avec leurs réponses Oui ou Non ; aucune confirmation d'un candidat, aucune position, aucun « Inconnu » (garde `exiger_etat_sans_aide`). Les t questions sont posées **avant** le panorama : l'historique est le même pour les bras C et B et pour les deux ordres, qui ne diffèrent donc que par le panorama.

**H-P3 (validité de l'instrument de reconnaissance).** Avec la paire (forme vraie, leurre de même couple) dont les rôles sont tirés à pile ou face, un plan des positions équilibré et deux ordres, l'écart D = taux de la cible dans C − taux de la cible (le leurre) dans B, lu par la règle gelée à trois issues, **retrouve des questionneurs factices de biais connu** : au niveau du hasard le bras « choix au hasard », « premier », « dernier », les deux préférences de contenu sans vérité (« plate », « centrale ») et l'artefact « famille » ; au-dessus le choix par compatibilité avec l'historique (« compatible ») ; en dessous son contraire (« contradicteur ») ; et le biais de position de « premier » et « dernier », son absence ailleurs. Aucun juge (N-058).

**Choix de t = 4, justifié avant toute exécution.**
1. C'est le premier point de carte intermédiaire gelé de l'instrument P1 (cartes à 0, 4, 8, 16), sur lequel le banc a été rendu « discriminant » : la reconnaissance se lit là où l'instrument a été éprouvé.
2. Quatre réponses Oui ou Non partagent l'espace en au plus 16 classes : sur 65 536 lois, l'historique laisse en moyenne des milliers de lois compatibles. La reconnaissance n'est donc pas décidée par la seule élimination du monde dans H ; mais un leurre de même couple, hypothèse distincte, a une chance réelle de contredire une réponse : la compatibilité avec l'historique donne un canal de reconnaissance non tautologique, qui manquait à la v1 (C-2).
3. À t = 0, l'option (a) retombe sur la v1 (aucune information, D nul par construction, C-2) ; à t = 16, la reconnaissance se confond avec la recherche que P1 mesure déjà. t = 4 est le plus petit point gelé de P1 qui ne soit pas nul.
4. Coût : t questions par monde et par proposeur s'ajoutent aux 4 cartes ; t = 4 double les appels, t = 8 les triplerait.
5. La sensibilité à t est rapportée sans décision : le factice « compatible » est aussi joué à t ∈ {0, 2, 4, 8} (préfixes d'une même suite de 8 questions aléatoires, le questionneur aléatoire de P1 ne dépendant pas des réponses).

Le questionneur qui pose les t questions en phase 0 est le questionneur **aléatoire** de P1 (borne intermédiaire de l'instrument, ni la meilleure ni la pire ; la bissection donnerait l'historique le plus informatif). En phase 1, chaque proposeur pose ses propres t questions.

## Prédiction chiffrée et signe attendu

| factice du critère | vérité du banc | issue attendue | valeurs exactes attendues | biais de position attendu (première / dernière) |
|---|---|---|---|---|
| hasard | aucune | au niveau | — | absent / absent |
| premier | aucune | au niveau | D = 0, intervalle de largeur nulle | détecté / absent |
| dernier | aucune | au niveau | D = 0, largeur nulle | absent / détecté |
| plate (entropie la plus haute, sa propre sonde) | aucune | au niveau | — | absent / absent |
| centrale (divergence moyenne la plus basse aux autres) | aucune | au niveau | — | absent / absent |
| compatible (moins de désaccords avec l'historique) | aucune | au-dessus | — | absent / absent |
| contradicteur (plus de désaccords) | aucune | en dessous | — | absent / absent |
| famille (artefact simulé : couple du monde) | couple du monde | au niveau | taux C = 1, D = 0, largeur nulle ; lecture sans leurre « au-dessus » | absent / absent |

Rapportés sans décision : reconnaisseur:0,15 et evitant:0,5, qui lisent la position vraie : leur conformité est une identité (C-2), ils ne servent qu'à la puissance empirique.

Confiance : ≈ 95 % pour premier, dernier, famille (construction) ; ≈ 90 % pour compatible et contradicteur (sur les petits mondes d'essai : D = +0,41 et −0,13 à 4 096 lois et 512 mondes, section « Ce qui a été vu ») ; **≈ 70 % pour plate et centrale** : avec les rôles tirés, leur écart attendu est nul, mais leur variance est élevée (taux de base jusqu'à 0,19 sur petits mondes) et l'équivalence à ±0,05 n'est rendue qu'avec la puissance de la taille ; ≈ 85 % pour le bras au hasard. Réfutation de H-P3 : un factice du critère non conforme.

## Métrique

- **Monde, paire, rôles (C-1)** : une loi a tirée sans remise dans H (code de P1 : 65 536 lois disjointes de la course v67) ; une loi b de même couple (type de racine, complexité), distincte de a (signature, 0,30 nat dans les deux sens), tirée par la graine de a ; puis **pile ou face** (graine « p3/roles/<i> ») : le monde est a ou b, l'autre est le leurre. Les mondes ne sont plus uniformes dans H (déclaré). Lois sans leurre : écartées, comptées ; **arrêt au-delà de 16 384** (le quart de H, C-7 i).
- **Remplisseurs (C-6)** : 7 lois de H d'un **autre couple (type de racine, complexité)** que le monde — elles peuvent avoir son type de racine —, distinctes (signature) du monde, du leurre et entre elles ; la garde le vérifie (C-7 iii).
- **Plan, ordres, panoramas** : inchangés depuis la v1 (blocs de 8 permutations par la graine « p3/plan » ; ordre 2 = miroir ; C et B ne diffèrent que par la cible).
- **Historique** : t = 4 questions du questionneur aléatoire de P1 (graines « p3/historique/<i>/questionneur » et « …/ordre »), réponses exactes du monde ; chaque entrée est (prédicat de la grammaire empirique de P1, Oui ou Non).
- **Factices sans vérité** : « plate » et « centrale » évaluent les lois présentées sur leur propre sonde (256 instances, graine « p3/factice-sonde/<nom>/sonde ») ; « compatible » et « contradicteur » évaluent les prédicats de l'historique sur leur propre sonde des questions (1 024 instances), compte les désaccords et tirent au hasard parmi les ex æquo (minimum ou maximum).
- **Écart D, intervalles, trois issues** : inchangés (moyenne par monde sur les deux ordres ; 10 000 rééchantillonnages des mondes ; niveau 0,975 ; δ = 0,05). **Grandeur rapportée (C-3)** avec une issue au-dessus ou en dessous : « sous la marge » si l'intervalle entier est sous δ en valeur absolue, « au-delà » si sa borne la plus proche de 0 dépasse δ, sinon « chevauche ».
- **Biais de position (C-7 v)** : part des choix à la première et à la dernière position (quatre cartes par monde), intervalle au niveau 0,995 ; « détecté » si la borne basse dépasse 1/K + 0,05 ; « absent » si la borne haute est sous 1/K + 0,05 (équivalence unilatérale : aucun excès qui compte) ; sinon « indéterminé ».
- **Taux de base observé** : le plus haut taux (C ou B) des factices sans reconnaissance hasard, plate et centrale ; comparé au taux gelé de la puissance (0,29).
- **Échangeabilité de la paire (C-1 c, rapportée)** : écarts monde − leurre appariés sur l'entropie moyenne (sonde de score) et sur la part des voisines distinctes de la famille (échantillon de 64, graine par loi), intervalle au niveau 0,975, marges gelées 0,02 nat et 0,03 ; rôles tirés et, pour comparaison, rôles non tirés.
- **Artefact C-1 (rapporté)** : plate et centrale rejoués sur les mêmes panoramas aux **rôles non tirés** (le monde est toujours a).
- **Longueur du panorama (C-4)** : caractères du JSON canonique des 8 lois du panorama C, minimum, médiane, maximum, mesurés sans dépense.
- Coût de la phase 0 : 0 USD.

## Seuil

- Règle à trois issues : lo > 0 → au-dessus ; hi < 0 → en dessous ; −0,05 < lo et hi < 0,05 → au niveau ; sinon non concluant (défaut de puissance, jamais une conclusion).
- Critère de validité : chaque factice du critère conforme à toutes ses attentes du tableau de prédiction ; conjonction.
- Taux de base : observé ≤ 0,29, sinon la taille est sous-dimensionnée.
- Gardes (refus écrits, arrêt de P3) : plan ; panoramas (dont distinction du leurre et des remplisseurs) ; état sans aide (clés exactes, t entrées, prédicats de la grammaire, réponses booléennes) ; vérité refusée aux questionneurs non déclarés ; carte hors panorama ; lois sans leurre sous la limite ; grammaire de P1 inchangée ; questionneur des questions préenregistré.
- Taux d'erreur : 0,025 bilatéral par intervalle de D (0,05 sur les deux proposeurs de la phase 1) ; 0,005 par intervalle de position ; puissance 0,80 par issue.

## Calcul de puissance (refait, C-3)

- **Taux de base** : non plus 1/8, mais **0,29**, arrondi au centième supérieur du plus haut taux observé par la contre-lecture pour une règle de choix sans reconnaissance (0,2877, « loi la plus plate », bras C, racine 1004 [CL-C] ; réunions : 0,2739 et 0,2762 pour la même règle, 0,2597 « seul de son type de racine » [CL-C]). La phase 0 vérifie que le taux observé à l'échelle ne le dépasse pas.
- **Ordres corrélés à 1** (cas exact de tout choix sur le contenu, corrélation 1,00 [CL-C]) : l'unité est le monde. **La variante optimiste à 544 mondes est retirée.**
- **Taille analytique** (approximation normale, z = 2,2414, indicatrices C et B indépendantes) : au niveau (p_C = p_B = 0,29) n ≥ 0,4118 · ((2,2414 + 1,2816)/0,05)² = **2 044,37** ; au-dessus (reconnaissance ρ = 0,15 : p_C = 0,3965) n ≥ 373,08 ; en dessous (évitement ρ = 0,5 : p_C = 0,145) n ≥ 149,13. Multiple de 8 : **2 048 mondes**.
- **Contrôle par simulation de la règle gelée elle-même** (`verifier_taille` : `trois_issues`, rééchantillonnage, `inverted_cdf`, 2 000 tirages, 400 répétitions, ordres recopiés, graines « p3/puissance/<issue>/2048 ») : à 2 048 mondes, au niveau rendu **0,81** (au-dessus 0,005 ; en dessous 0,0125 ; non concluant 0,1725) ; au-dessus 1,00 ; en dessous 1,00. La recherche gelée (`rechercher_taille` : partir de la taille analytique, monter par pas de 64 jusqu'à 0,80 pour chaque issue) s'arrête donc au premier pas : **taille retenue 2 048 mondes par proposeur**. Marge faible (0,81 contre 0,80, écart-type de l'estimation ≈ 0,02) : dite. Le lanceur refait ce contrôle, aux mêmes graines, avant tout calcul. Pour comparaison, la règle gelée à l'ancienne taille de 1 088 mondes et au taux 0,25 ne rendait « au niveau » que 0,372 [CL-E].
- **Sensibilité à δ** (taille analytique, multiple de 8, même taux de base) : δ = 0,03 → 5 680 ; 0,04 → 3 200 ; **0,05 → 2 048** ; 0,0625 → 1 312 ; 0,075 → 912 ; 0,1 → 512. La marge fixe à elle seule la taille : à rediscuter par Lazar avant la phase 1.
- Ce calcul ne porte que sur des tirages de Bernoulli aux taux gelés : aucune donnée de la configuration n'y entre.

## Nombre d'appels de la phase 1 (refait, C-4 ; non engagé, sans prix)

- Par proposeur et par monde : **t = 4 questions** (historique commun aux deux bras et aux deux ordres : une seule suite de questions, les quatre cartes partent du même historique) **+ 4 cartes** (C et B × deux ordres) = 8 appels.
- **2 048 mondes × 8 = 16 384 appels par proposeur ; 32 768 appels pour deux proposeurs.**
- **Aucun prix en USD** : aucune pièce lue ne donne le prix d'un appel de question ou de carte ; le coût d'un appel de proposeur de la course v67 (unité différente, constats P-6 et C-4) n'est plus utilisé. Prix à relever avant tout devis.
- Longueur de l'entrée d'un appel de carte : mesurée par la phase 0 (caractères du JSON canonique du panorama, minimum, médiane, maximum) ; sur les petits mondes d'essai, médiane ≈ 4 300 caractères (section « Ce qui a été vu »). L'historique ajoute 4 prédicats et leurs réponses.
- La phase 2 (C4) n'est pas dimensionnée.

## Plan d'analyse

1. Sondes ; lois de référence de la course v67 évaluées par l'évaluateur de l'organisme (empreinte vérifiée) ; espace H (code de P1) ; contrôle de la grammaire.
2. Couples de H ; 2 048 paires et leurs rôles (« p3/mondes », « p3/leurre/<loi> », « p3/roles/<i> ») ; plan et sa garde ; remplisseurs ; panoramas et leur garde ; panoramas aux rôles non tirés (artefact).
3. Historiques : 8 questions aléatoires de P1 par monde, préfixe de 4 pour la carte décisive ; réponses exactes du monde (et de a pour l'artefact).
4. Cartes : chaque factice du critère et rapporté × 2 048 × {C, B} × {1, 2} (« p3/carte/<questionneur>/<bras>/<ordre>/<i> ») ; artefact (« p3/carte-roles-non-tires/… ») ; compatible à t ∈ {0, 2, 4, 8} (« p3/carte-t<t>/… »).
5. Lectures : trois issues et grandeur, biais de position, conformité ; taux de base ; échangeabilité ; audit R4.
6. Puissance (analytique, sensibilité, simulation) et nombre d'appels écrits dans la sortie.
- Graines (R9) : `SeedSequence(20261118, spawn_key=(k,))`, k des 8 premiers octets du sha256 du nom de tâche ; liste au manifeste, avec configuration, bloc et empreintes, versions, empreintes de ce texte, de la contre-lecture, du code de P3 v2 et de P1, de l'évaluateur et de la source, commit et état de l'arbre.
- Comparaisons multiples : une conjonction décisive ; intervalles de D au niveau 0,975, de position au niveau 0,995 ; le reste rapporté.

## Critères de lecture gelés

| gardes | taux de base observé ≤ 0,29 | issues et valeurs exactes des factices | biais de position des factices | verdict |
|---|---|---|---|---|
| une au moins échoue (arrêt écrit) | — | — | — | **garde défaillante** : arrêt, audit du code, rien soumis |
| tiennent | non | — | — | **taille sous-dimensionnée** : puissance à refaire, rien soumis |
| tiennent | oui | une au moins non conforme | — | **instrument de reconnaissance non discriminant (issues)** : arrêt, rapporté, rien soumis |
| tiennent | oui | conformes | un au moins non conforme | **biais de position non retrouvé** : arrêt, rapporté, rien soumis |
| tiennent | oui | conformes | conformes | **instrument de reconnaissance discriminant** : le nombre d'appels de la phase 1 peut être soumis à Lazar, prix à relever (non engagé) |

- **Trois issues écrites d'avance pour la phase 1** (par proposeur, même règle, mêmes t, δ, niveau et taille) : **reconnaissance au-dessus du hasard** (après les mêmes 4 réponses, il choisit la forme vraie offerte plus souvent que son leurre apparié ; rapportée avec sa grandeur, « sous la marge » ne se lit pas comme une reconnaissance qui compte) ; **au niveau du hasard** (équivalence à ±0,05) ; **en dessous du hasard** ; « non concluant » n'est pas une issue. Avec l'option (a), les trois issues sont atteignables par un questionneur réel : il lit un historique du monde (les factices compatible et contradicteur le montrent).
- Audit de symétrie (R4), motifs écrits, sans changer le verdict : intervalle du bras au hasard de largeur nulle ; un factice du critère d'issue contraire à l'attente ; paire non équivalente (rôles tirés) sur l'entropie ou les voisines ; artefact des rôles non tirés non vu ; écart de compatible ou de contradicteur entier sous la marge.

## Liste d'arrêt

| condition | action |
|---|---|
| empreinte de ce texte ≠ attendue ; compagnon absent ou non conforme | refus de partir (code 2), rien écrit |
| empreinte du bloc gelé absente de ce texte | refus (code 2), rien écrit |
| mondes sous la taille analytique ; règle gelée simulée sous la puissance gelée | refus (code 2), rien écrit |
| contre-lecture de ce texte absente, non scellée ; verdict strict autre que « scellable » ; empreinte absente de la ligne « Texte contre-lu » ; empreinte citée avec une négation de la relecture (C-5) | refus (code 2), rien écrit |
| module de P3 v2 ou de P1 sans compagnon conforme ou d'empreinte inattendue ; évaluateur ou source v67 absent ou différent | refus (code 2), rien écrit |
| mode d'essai hors des petits mondes (plus de 4 096 lois ou de 512 mondes) ; dossier de sortie déjà présent | refus (code 2), rien écrit ; le lecteur R13 refuse toute sortie « essai » |
| plan non équilibré ; panorama non conforme ; remplisseurs introuvables ; plus de 16 384 lois sans leurre | arrêt de P3, motif écrit, « garde défaillante » |
| état de carte avec une aide ; vérité lue par un questionneur non déclaré ; carte hors panorama | arrêt de P3, motif écrit |
| grammaire de P1 différente ; questionneur des questions différent ; loi de référence hors gabarit | arrêt de P3, motif écrit |
| verdict autre que « instrument de reconnaissance discriminant » | rien soumis ; rapporté tel quel |
| refus de permission, de crochet ou de classifieur | arrêt, rapport tel quel |

## Conditions de la mère (R-3186) et décision sur C-2 : où chacune est satisfaite

| condition | où |
|---|---|
| positions réparties d'avance | `plan_positions`, `exiger_plan_equilibre` ; graine « p3/plan » |
| factices à biais de position connu, retrouvés | `Premier`, `Dernier`, `Hasard` ; `biais_de_position` (détection et absence par équivalence) |
| un questionneur qui reconnaît la vraie forme | `Compatible` (sans vérité du banc, par l'historique) ; `Reconnaisseur` simulé rapporté seulement |
| carte sans aide, option (a) | `historique_de`, `etat_de_carte`, `exiger_etat_sans_aide`, `jouer_carte` ; t = 4 justifié (section « Hypothèse ») |
| leurre apparié (même famille, même complexité) | couple (type de racine, complexité) ; rôles à pile ou face ; `Plate`, `Centrale` au critère ; échangeabilité rapportée |
| deux ordres et un bras « choix au hasard » | `jouer_reconnaissance` ; `Hasard` |
| trois issues écrites d'avance | `issue`, `grandeur`, `trois_issues` ; section « Critères » |
| puissance avant tout devis | `taille_analytique`, `verifier_taille`, `rechercher_taille`, `sensibilite_delta` ; garde `exiger_puissance` |
| devis refait sur cette taille | `appels_phase1` : nombre d'appels seulement, prix à relever |
| P3 hors table, écart déclaré | section « Hors table » ; clé `hors_table` |
| R1, R4, R5, R6, R9, R12, N-058 | texte scellé avant exécution ; audit R4 ; gardes sur cas sain et artefact ; compagnons ; graines et manifeste ; noms neufs ; vérité du monde planté |

## Ce que la phase 0 ne dit pas

- Rien sur les proposeurs réels ; l'énoncé de l'article n'est pas éprouvé ici.
- Rien sur la découverte : C contient la vérité par construction. Avec l'option (a), une reconnaissance au-dessus du hasard peut venir de la seule compatibilité avec l'historique (« compatible » le montre) : en phase 1, « reconnaître mieux que produire » demandera de comparer D à ce que le même proposeur tire des mêmes 4 réponses sans panorama (carte de P1 à 4 questions) ; cette comparaison n'est pas préenregistrée ici.
- Rien sur C4, sur la boucle de production (aucun panorama avec une loi vraie connue ou un témoin n'est servi dans la boucle), sur une composition de proposeurs (N-058), sur le rendu en texte du panorama et de l'historique.
- Le recouvrement à T = 16 sur l'instrument de P1, rapporté en v1, est retiré (voir différentiel).
- Aucune dépense, aucune machine, aucun accès réseau.

## Écarts à la proposition et choix déclarés

1. Métrique principale : carte de reconnaissance après t = 4 questions (option (a)), non le recouvrement à T = 16.
2. Positions réparties d'avance en blocs équilibrés.
3. K = 8 (non 20 à 42) : séparabilité de « en dessous » ; effet sur la comparabilité à l'article dit.
4. Couple (type de racine, complexité) comme « même famille, même complexité » ; remplisseurs d'un autre couple (C-6).
5. Rôles de la paire à pile ou face (C-1) : les mondes ne sont plus uniformes dans H.
6. Bonferroni sur deux proposeurs dès la phase 0.
7. Taux de base gelé à 0,29 (plus haut observé, arrondi), ordres corrélés à 1, règle gelée simulée (C-3).
8. Questions de l'historique posées par le questionneur aléatoire de P1 en phase 0 ; historique commun aux bras et aux ordres.
9. Échangeabilité de la paire et artefact des rôles non tirés **rapportés** avec motif d'audit, non décisifs (raison : à 2 048 mondes, la largeur de l'intervalle d'entropie ≈ 0,02 laisse une chance de l'ordre de 5 % de non-équivalence sous des rôles exactement échangeables ; et la taille de l'effet C-1 à 65 536 lois n'est pas connue).

## Ce qui a été vu avant scellement (déclaré, R1 et R4)

- Rien de la configuration : ni H à 65 536 lois, ni les 2 048 mondes, ni la course v67.
- La puissance : taille analytique, sensibilité à δ et simulation de la règle gelée aux graines gelées (« p3/puissance/<issue>/2048 », racine 20261118) — ce sont des tirages de Bernoulli aux taux gelés, sans donnée ; chiffres ci-dessus.
- Les sorties de la contre-lecture (citées).
- **Petits mondes d'essai** (aucun ne touche la configuration) : (i) essais v2 (racine 4242, 256 lois, 64 mondes, 27 rôles échangés sur 64, aucune loi écartée) : hasard non concluant (D = +0,0938) ; premier et dernier D = 0, biais retrouvé ; plate et centrale non concluant (D = −0,078) ; compatible au-dessus (D = +0,469 [0,320 ; 0,609]) ; contradicteur non concluant (D = −0,070 [−0,164 ; 0,008]) ; famille D = 0, taux C = 1 ; plusieurs absences de biais de position « indéterminées » à cette taille. (ii) Deux lancements d'essai du lanceur v2 en dossier temporaire de la session, hors dépôt, sur sources fabriquées : 1 024 lois et 256 mondes (racine 4242) ; 4 096 lois et 512 mondes (racine 1001) — à 4 096 lois : hasard au niveau (D = 0,000) ; plate et centrale non concluant (D = +0,018 et +0,033) ; compatible au-dessus (D = +0,413) ; contradicteur en dessous (D = −0,134) ; compatible selon t : D = +0,033, +0,149, +0,396, +0,612 à t = 0, 2, 4, 8 ; artefact des rôles non tirés **non vu** (plate +0,029, centrale +0,025, non concluant) ; échangeabilité de l'entropie non équivalente à cette taille (rôles tirés, intervalle [−0,014 ; 0,032]) ; taux de base observé 0,186 ; longueur du panorama 2 396 / 4 313 / 6 811 caractères. Ces essais ont conduit à trois choix faits avant scellement : biais de position « absent » par équivalence **unilatérale** (une part nulle, comme celle de « premier » en dernière position, n'est pas un biais) ; échangeabilité et artefact rapportés avec motif d'audit plutôt que gardes (écart 9) ; aucun seuil (t, δ, taux de base, niveaux) changé après eux.

## Lancement (après contre-lecture de ce texte et versement, jamais avant)

`cd /home/user/controle-ia-travail/docs/notes/organisme-re-search-v1/phase0-p3-v1 && python3 -B lanceur_phase0_p3_v2.py --sortie <dossier neuf> --contre-lecture <contre-lecture scellée de ce texte v2>`. La contre-lecture de la v1 ne permet pas de lancer la v2 (verdict « non scellable », et elle ne cite pas ce texte). Durée estimée : la construction de H (≈ 12 minutes, comme P1), le contrôle de puissance (≈ 80 secondes), les cartes (quelques minutes). Le lancement est une décision à part.

## Contre-lecture

- Contre-lecture de la v1 : modèle J, sous-agent neuf d'un autre modèle, `contre-lecture-phase0-p3-v1.md` (f254324bf5bb1a4ee62eaa1dce5aacb904c7a05e9b7e1256d858782e0b38c016), texte relu d3fd6dedad90ac18009bfe3e45f98bf183dfbfab8c3bca2670b4482bdff58685, verdict « non scellable ». Traitement de chaque constat :

| constat | traitement | où |
|---|---|---|
| C-1 (bloquant, leurre non échangeable) | **porté** : rôles à pile ou face ; plate et centrale au critère, attendues au niveau ; échangeabilité (entropie, voisines) rapportée avec marges gelées ; artefact des rôles non tirés rapporté, motif d'audit s'il n'est pas vu (porté partiellement : rapporté, non décisif, écart 9) | `tirer_paires`, `Plate`, `Centrale`, `echangeabilite` ; essais `test_paires_roles_a_pile_ou_face`, `test_factices_sur_petits_mondes` |
| C-2 (bloquant, sans aide = sans information) | **porté par la décision de la mère, option (a)** : carte après t = 4 questions de P1, puis panorama ; t justifié ; factices non tautologiques compatible et contradicteur au critère ; factices qui lisent la position vraie retirés du critère | `historique_de`, `exiger_etat_sans_aide`, `Compatible`, `Contradicteur` ; essais `test_etat_sans_aide_sain_et_artefacts`, `test_historique_vrai` |
| C-3 (puissance) | **porté** : taux de base 0,29 ; ordres corrélés à 1 ; variante à 544 retirée ; règle gelée simulée ; sensibilité à δ ; grandeur des issues | `taille_analytique`, `verifier_taille`, `rechercher_taille`, `sensibilite_delta`, `grandeur` ; garde `exiger_puissance` ; essais `test_puissance_analytique_valeurs_gelees`, `test_regle_gelee_simulee_ordres_correles` |
| C-4 (devis) | **porté** : nombre d'appels seulement, aucun USD ; longueur du panorama mesurée | `appels_phase1`, `longueur_panorama` ; essai `test_appels_et_longueur` |
| C-5 (garde de contre-lecture) | **porté** : verdict strict sur la ligne entière ; empreinte sur la ligne « Texte contre-lu » ; refus d'une empreinte citée avec une négation de la relecture | `lire_verdict_strict`, `exiger_contre_lecture` ; essai `test_garde_contre_lecture_stricte` |
| C-6 (famille dans le texte) | **porté** : couple (type de racine, complexité) écrit partout | métrique ; `choisir_remplisseurs` |
| C-7 (gardes qui ne peuvent pas se déclencher) | **porté** : (i) limite 16 384 et artefact ; (ii) contrôle d'état remplacé par `exiger_etat_sans_aide`, qui peut échouer (essai d'artefacts) ; (iii) remplisseurs distincts du leurre et entre eux ; (iv) artefacts : signature non distincte, remplisseurs introuvables, limite des lois écartées ; (v) absence de biais par équivalence unilatérale | essais `test_limite_des_lois_sans_leurre_saine_et_artefact`, `test_panorama_sain_et_artefacts`, `test_remplisseurs_introuvables_artefact`, `test_biais_de_position_regle_sur_tableaux` |
| C-8 (mode d'essai ; essai sur la configuration réelle) | **porté** : mode d'essai limité aux petits mondes (≤ 4 096 lois, ≤ 512 mondes) ; l'essai qui appelle le lanceur en mode réel remplace le déroulement et la puissance par une sentinelle | `exiger_petit_monde` ; essais `test_mode_essai_petits_mondes_seulement`, `test_vrai_preenregistrement_et_lancement_reel_refuse` |

- **Contre-lecture de ce texte v2 : à faire** par un sous-agent neuf (R2), avant tout lancement, sur ce texte, `panorama_p3_v2.py`, `lanceur_phase0_p3_v2.py`, `test_phase0_p3_v2.py`, le code de P1 réemployé et la contre-lecture de la v1. Le lanceur v2 n'accepte qu'un rapport scellé au verdict strict « scellable » portant l'empreinte de ce texte sur sa ligne « Texte contre-lu ». Le validateur `controle_ia.prereg` signalera que cette section ne porte pas encore l'empreinte du rapport de la v2 : elle n'existe qu'après ; ce texte est scellé par `controle_ia.scellement`.

## Différentiel v1 → v2

Texte :
1. En-tête : remplace la v1 (citée par empreinte), porte la contre-lecture et ses pièces (citées par empreinte), et la décision de la mère sur C-2.
2. Bloc gelé : nouvelle configuration, nouvelle empreinte. **Retirés** : `devis` (prix, reprises), `ordres`, `mondes_kl`, `factices_kl`, `questions_T`, `points_de_carte`, `rho` à 1 au critère. **Ajoutés** : `t_questions`, `t_sensibilite`, `questionneur_des_questions`, `taux_de_base`, `puissance_repetitions`, `puissance_tirages`, `deltas_sensibilite`, `delta_position`, `factices_artefact_roles`, `factices_taux_de_base`, `sondes_factices`, `echangeabilite`, `appels`. `mondes` 1 088 → 2 048 ; `limite_lois_sans_leurre` 65 536 → 16 384.
3. Hypothèse : option (a) écrite ; « sans aide » redéfini (aucun indice du répondeur sur les candidats au moment du choix) ; choix de t = 4 justifié. **Retiré** : la carte « avant toute question ».
4. Prédiction : nouveau tableau (plate, centrale, compatible, contradicteur au critère). **Retirés du critère** : reconnaisseur:1, evitant:1 (identités, C-2).
5. Métrique : paire et rôles à pile ou face ; couple (type, complexité) ; remplisseurs distincts du leurre et entre eux ; historique ; factices sans vérité ; grandeur ; position par équivalence unilatérale ; taux de base ; échangeabilité ; artefact ; longueur du panorama. **Retiré** : recouvrement à T = 16 sur l'instrument de P1 (raison : sous l'option (a), l'historique est fixé avant le panorama ; une continuation demanderait son propre dessin ; il n'était que rapporté).
6. Seuil et critères : ligne « taille sous-dimensionnée » ajoutée ; verdict favorable réécrit (nombre d'appels, prix à relever).
7. Calcul de puissance refait (taux de base 0,29, ordres corrélés, simulation de la règle gelée, sensibilité à δ). **Retirés** : taux de base 1/8, variante optimiste à 544 mondes, « contrôle » par l'intervalle normal.
8. Section « Devis refait » remplacée par « Nombre d'appels » : **retirés** tous les montants en USD (2 641,03 ; 3 834,39 ; 1 320,51 ; 1 917,20) et les prix unitaires de la course v67.
9. Liste d'arrêt : garde de puissance simulée ; garde de contre-lecture stricte ; mode d'essai limité ; limite des lois sans leurre.
10. Écarts : 5, 7, 8, 9 ajoutés ou réécrits ; « Ce qui a été vu » réécrit ; « Lancement » et « Contre-lecture » réécrits ; cette section ajoutée.

Code :
11. `panorama_p3_v2.py` (nouveau nom) : `tirer_paires` (rôles), `historique_de`, `etat_de_carte`, `exiger_etat_sans_aide`, `Plate`, `Centrale`, `Compatible`, `Contradicteur`, `desaccords`, `grandeur`, `biais_de_position` (équivalence), `ATTENTES_FACTICES` nouvelles, `echangeabilite`, `scenarios`, `taille_analytique`, `puissance_regle_gelee`, `verifier_taille`, `rechercher_taille`, `sensibilite_delta`, `appels_phase1`, `longueur_panorama` ; `exiger_panorama` étendu. **Retirés** : `tirer_mondes_avec_leurre`, `taille_necessaire`, `puissance_par_simulation`, `devis`, `compatible` et `cartes_avec_reconnaissance` (recouvrement).
12. `lanceur_phase0_p3_v2.py` (nouveau nom) : `lire_verdict_strict`, `exiger_contre_lecture` stricte, `exiger_puissance` (analytique et simulée), `exiger_petit_monde`, `verdict_p3` à quatre entrées, déroulement de l'option (a), lectures nouvelles, sorties `*-v2.*`. **Retirés** : `recouvrement_p1`, le devis en USD.
13. `test_phase0_p3_v2.py` (nouveau nom) : essais de la v1 adaptés ; nouveaux : rôles, limite des lois, remplisseurs introuvables, historique, état sans aide, règle de position, grandeur, puissance gelée et simulée, appels, contre-lecture stricte, mode d'essai, sentinelle.
