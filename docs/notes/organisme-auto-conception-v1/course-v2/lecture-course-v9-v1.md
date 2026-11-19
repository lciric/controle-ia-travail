# Lecture descriptive de la course d'auto-conception v9 de l'organisme d'idéation — v1

- Lecture confiée à la mère par le préenregistrement v2 de la course (« Plan d'analyse » : « lecture descriptive, par la mère, après la course ») ; écrite pour elle par un sous-agent (modèle Opus 5.5), le 2026-11-19, processeur seul, aucune dépense, aucun appel à un modèle extérieur. Ni verdict de porte, ni choix de carte, ni promotion.
- Texte qui gouverne : `docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md`, sha256 `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` ; le plafond d'arrêt est celui de l'additif v2i (`course-v4/additif-preenregistrement-course-auto-conception-v2i.md`, 150 USD, mot de Lazar) ; les additifs v2c à v2i ne changent pas la lecture.
- Pièces lues : branche `lot/compte-organisme-v1`, commit `8029ae7f9539a950936cef5b2b669285d4efb05a`, arbre séparé détaché (retiré après lecture). Racine A = `archives-reponses-modeles/auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie`. Chaque empreinte vérifiée avant lecture (liste dans la sortie des comptes) : manifeste de fin du lanceur `28bc36df…`, bilan `b88bfcb9…`, manifeste de fin de l'orchestrateur `d3548fed…`, cartes `fiches.json` `ba65c411…`, journal de l'aiguilleur `e2ba2a33…`, classement `fa6ee4a0…`, mémoire `f018b701…`, consommations `a8a58571…`, liste des empreintes de la sortie `522c83a9…` (les 94 fichiers de verdicts y sont conformes), matière v3 lue sur `main` `11f4b69b…`, programme d'épreuve des témoins v2 `19d03876…`. Les manifestes de départ et de fin du lanceur et de l'orchestrateur, le bilan et les cartes passent `controle_ia.scellement verifier`.
- Programme de comptes : `course-v2/comptes_lecture_course_v9_v1.py`, sha256 `54abe6878512e51c60eb85cb4bb0ae37db0dcde7b46bec9922c7afb751c3b41c`. Sorties : audit `course-v2/lecture-course-v9-v1-sortie-audit.json` (`85d8e8b849b493947a62096a70cbc02d6cbde1e32fd6e6b8f427d92148e0e262`), comptes `course-v2/lecture-course-v9-v1-sortie-comptes.json` (`a9c90c34e1d8be4afdf2d71fab51bea57e67e603368c23938e33ebd0adeb9926`), issue de l'audit écrite avant les comptes `course-v2/lecture-course-v9-v1-issue-audit.txt` (`6184a05a6dd2720446e9620674162de4e12acfe83bd5b3fa4b4d5afb6da56950`, 12:39:47Z). Tout chiffre ci-dessous vient de ces sorties ou des manifestes cités.
- Non lus : `conservation-reponses-v1/` et `.claude/projects/` (absents du commit), tout fichier « consigne-privee » ou « conception-ii-b », la branche `lot/compte-4-v1`, `docs/verdicts/`. Les deux clés du coffre (`autoc-cle-anonymisation.json`, `autoc-cle-sessions.json`) n'ont été ouvertes que pour leur structure (deux entrées chacune) : elles relient les identifiants servis aux juges et les sessions aux cartes, sans porter l'espèce ; l'espèce est lue au champ `meta.proposeur` des cartes.

## 1. Bonne fin (critères de lecture gelés, l. 73) — issue : **fin propre**

Établie sur les manifestes seuls, avant l'ouverture d'une carte.

| contrôle | valeur lue | tenu |
|---|---|---|
| code rendu | 0 (manifeste de fin du lanceur) ; bilan : aucun arrêt, aucun nœud, condition C13 satisfaite (technique et budget) | oui |
| proposition, aiguillage, juges | « jouee » (lanceur et orchestrateur) | oui |
| passe « tableau », fusions | « retiree » (projection au-dessus du plafond, par construction) ; étiquettes jouée à vide | oui |
| cumul | 72,502472 USD ≤ 150 (et sous l'ancien plafond de 90 du texte v2) ; dépassement 0 | oui |
| manifestes écrits et scellés | départ et fin du lanceur, départ et fin de l'orchestrateur, compagnons `.sha256` conformes | oui |
| lacunes écrites | `especes_absentes` du manifeste de départ du lanceur : l'espèce Kimi, « relais non déclaré » (non déclarée par la mère, R-3273) | oui |

Autres champs : aucun rôle arrêté, aucune exclusion par la garde des étiquettes, aucun soupçon ni refus pour crédit, aucune alerte après. Durée 09:41:46 → 12:31:30 UTC. Ligne de GO de la course : GO-2026-11-19-19, plafond 150 USD. Bonne fin ne dit rien de la qualité des cartes.

Rapporté, sans effet sur la bonne fin : l'étape de proposition a coûté 58,64 USD, au-dessus de son plafond de relais de 45 USD (`au_dela_du_plafond_de_relais` vrai au journal du budget), sous son plafond dur de 140 USD.

## 2. Audit de symétrie (règle R4) — issue : **une case « trop propre », aucune « trop sale » ; rien d'artefactuel sur les champs**

Fait par programme sur les champs seuls (classe de l'aiguilleur, items des juges, notable, redites), avant les comptes et avant toute lecture des cartes ; issue écrite à 12:39:47Z.

- **Lot de la génération** (96 cartes rendues) : ni trop propre (2 cartes retenues par l'aiguilleur ; 67 cartes sur 94 à items tous vrais chez les deux juges), ni trop sale (67 notables). Aucune redite.
- **Par case du catalogue** (lecture plus stricte, onze cases) : la case « famille originalité » (6 cartes : 2 Argon, 2 Astra, 2 Opus) est **trop propre** (toutes à passeport, tous items vrais chez les deux juges, aucune redite) ; aucune case trop sale.
- **Audit déclenché, mêmes contrôles qu'à l'inverse** : probabilité qu'une case de 6 cartes tirées sans remise parmi 94 (67 notables) soit entièrement notable 0,1226 ; espérance du nombre de cases entièrement notables sous répartition au hasard 0,617 sur 11 ; longueurs des notes des juges et des cartes de la case dans l'étendue des autres cases ; empreinte du verdict égale à celle de la carte 94 fois sur 94 ; aucune note vide ; « notable » d'un juge égal à « cinq items vrais » 94 fois sur 94 chez chaque juge ; classement « notable » égal à l'unanimité 94 fois sur 94.
- **Constat général de l'audit** : deux items sont à plafond chez chaque juge (juge Opus : `module_nomme`, `epreuve_plantee` ; juge Argon : `module_nomme`, `voisin_nomme`) ; l'item `reserves_tenues` porte l'essentiel du tri ; tout notable du juge Opus est notable du juge Argon. Cela rejoint la limite dite au texte : l'épreuve des témoins n'a éprouvé qu'un plancher de lecture de forme.
- **Issue** : la propreté de la case « originalité » est compatible avec le hasard de la répartition ; réserve R4 consignée ; aucune lecture de qualité n'en est tirée.

## 3. Comptes de la « Métrique »

**Cartes rendues** : 96 = 94 à passeport + 2 retenues. Cinq espèces actives (deux Claude : Opus et Fable ; Argon ; Astra ; Carbon), 11 appels chacune, 55 appels.

| espèce | appels | sans sortie exploitable | cartes à passeport | cartes par appel exploitable | notables (unanimité) |
|---|---|---|---|---|---|
| Opus (Claude) | 11 | 0 | 22 | 2,0 | 11 |
| Fable (Claude) | 11 | 3 (statut « ok », sortie inexploitable) | 15 | 1,875 | 11 |
| Argon | 11 | 0 | 21 | 1,909 | 12 |
| Astra | 11 | 1 (statut « ok », sortie inexploitable) | 20 | 2,0 | 20 |
| Carbon | 11 | 3 (statut « refus ») | 16 | 2,0 | 13 |

Plus forte part sans sortie : 3 sur 11 (27 %), sous le seuil d'arrêt de 34 %.

**Par case du catalogue** (cartes à passeport) : exploration 6 (Argon, Astra, Opus) ; originalité 6 (Argon, Astra, Opus) ; épreuve 10 ; jugement 10 ; mémoire 10 ; sélection 8 (sans Carbon) ; coût 10 ; auto-conception 8 (Argon 1, Fable 1) ; machines 10 ; hors machine 8 (sans Fable) ; autre et marges 8 (sans Astra). Les trous suivent les appels sans sortie. Les deux cartes retenues n'ont pas de case au journal ; par élimination (une seule carte d'Argon et une seule de Fable dans la case « auto-conception »), elles en viendraient probablement, ce qui reste une inférence.

**Refus au format** : 7 appels sans sortie exploitable (ci-dessus) ; 2 cartes retenues par l'aiguilleur (classe `a_corriger`), l'une de fournisseur Claude, « champ vide (epreuve_hors_ligne) », l'autre d'Argon, « deux propositions mêlées » ; contenu non copié au journal, non lu ici. Champs hors des dix demandés, sur 4 cartes à passeport : `_` (2), `cout_note` (1), `epreuve_hors_ligne` (1).

**Classes de l'aiguilleur** (96 appels) : niveau de la méthode (passeport) 94 ; à corriger (retenue) 2 ; concret 0 ; refus de l'aiguilleur 0.

**Exclusions par la garde des étiquettes d'espèces (garde A4, mot entier)** : 0 au manifeste de l'orchestrateur et du lanceur. Contre-contrôle : aucune carte à passeport ne contient en mot entier l'une des six étiquettes (dont « carbon »).

**Verdicts des items** (94 cartes, vrais sur 94) :

| item | juge Opus | juge Argon | accord des deux juges |
|---|---|---|---|
| `module_nomme` | 94 | 94 | 94 |
| `voisin_nomme` | 91 | 94 | 91 |
| `epreuve_plantee` | 94 | 93 | 93 |
| `aucun_modele_ne_decide` | 92 | 93 | 91 |
| `reserves_tenues` | 72 | 83 | 83 |
| notable (cinq vrais) | 67 | 83 | — |

Notables à l'unanimité : 67 (agrégation descriptive, ni promotion ni classement de valeur). `reserves_tenues` faux chez le juge Opus : Opus 10, Argon 7, Fable 3, Carbon 2 ; chez le juge Argon : Opus 7, Argon 2, Fable 2. Par case, notables : exploration 3/6, originalité 6/6, épreuve 9/10, jugement 7/10, mémoire 7/10, sélection 7/8, coût 8/10, auto-conception 5/8, machines 8/10, hors machine 5/8, autre et marges 2/8.

**Redites** (bardeaux de trois mots, seuil 0,5) : 0 ; 94 idées distinctes. Complément descriptif hors « Métrique » : deux titres identiques à la casse près portés par plusieurs cartes — « Votes effectifs du collège mesurés sur témoins plantés » trois fois (Fable, Opus deux fois, cases jugement et hors machine), « Verdict de mort sur (k) réimplémentations indépendantes » deux fois (Opus, Fable, cases épreuve et sélection) ; la mémoire ne les compte pas comme redites.

**Rôles arrêtés** : aucun (arrêts par échecs consécutifs, par part sans sortie, par version servie changée : vides).

**Coûts** (manifeste de fin du lanceur ; recalcul sur les consommations : 72,502472 USD, égal) :

| rôle | appels | réel (USD) | devis v1 (USD) | écart |
|---|---|---|---|---|
| proposeur Opus | 11 | 7,43 | 2,79 | +4,64 |
| proposeur Fable | 11 | 17,58 | 6,98 | +10,60 |
| proposeur Argon | 11 | 4,17 | 5,79 | −1,62 |
| proposeur Astra | 11 | 4,75 | 6,98 | −2,23 |
| proposeur Carbon | 11 | 24,72 | 5,79 | +18,93 |
| aiguilleur | 96 | 4,59 | 2,98 | +1,61 |
| juge Opus | 94 | 6,86 | 3,48 | +3,39 |
| juge Argon | 94 | 2,41 | 3,26 | −0,85 |
| **total** | | **72,50** | **39,62** | **+32,89** |

Par relais : Claude 36,46 ; Carbon 24,72 ; Argon 6,58 ; Astra 4,75. Par étape : proposition 58,64 ; aiguillage 4,59 ; juges 9,27. Attendu de la ligne de GO (devis v2i) ≈ 59,03 USD, haut 137,81. Reste des clés après la course : clé Claude « Minuit » ≈ 162,56 USD estimé (seuil 40) ; clé Gemini (Argon et Carbon) illisible, dépense comptée 31,30 ; clé OpenAI (Astra) illisible, dépense comptée 4,75 — à relever aux interfaces de facturation.

**Voisin du catalogue qui existe** (par `ID_CATALOGUE` et `controles_statiques` du programme d'épreuve v2, importés et non recopiés) :
- champ `plus_proche_voisin` seul (copie servie avec `ce_qui_distingue` vide) : **93 cartes sur 94 (98,9 %)** citent au moins un identifiant de regroupement qui existe dans la matière v3 ; 92 n'en citent que d'existants ; 1 n'en cite aucun (Astra) ; 1 cite un identifiant « absent » (Fable) ;
- fonction telle quelle (elle lit `plus_proche_voisin` et `ce_qui_distingue`) : mêmes nombres ;
- l'unique « absent », `et n° 3`, est un artefact de l'expression gelée sur « coût n° 4 et n° 3 » : l'expression prend « et » pour un nom de famille. La carte cite par ailleurs des identifiants existants.
- Ce compte ne dit pas que le voisin nommé est le bon ni que la différence dite est juste.

**Répartition par axe**, valeurs écrites telles quelles : robustesse 45 ; exploration 21 ; mémoire 16 ; épreuve contre le réel 7 ; originalité 5. Par espèce : Opus robustesse 11, mémoire 4, exploration 4, originalité 3 ; Argon robustesse 8, exploration 5, mémoire 4, épreuve contre le réel 3, originalité 1 ; Astra robustesse 9, exploration 9, épreuve contre le réel 1, originalité 1 ; Carbon robustesse 8, mémoire 4, exploration 2, épreuve contre le réel 2 ; Fable robustesse 9, mémoire 4, épreuve contre le réel 1, exploration 1. Les cinq valeurs sont écrites exactement ; aucune autre.

Complément hors « Métrique » : modules nommés dans le champ `module_change` (une mention n'est pas un changement) : noyau et budget 55, sélection entre générations 53, tests de mort 42, mémoire anti-redite 41, témoins plantés 34, proposeurs 31, juge statistique (pari) 20, coffre 17, bisociateur 16, dossier fermé 11, juges croisés 10, aiguilleur 6, moisson de nouveauté 3.

## 4. Lecture descriptive des cartes, comme matière de l'atelier d'idées

Chaque carte est l'avis d'un proposeur, jamais un fait. Les regroupements ci-dessous sont une lecture de la mère (par son sous-agent), non un calcul ; une carte peut relever de plusieurs. Les identifiants viennent en appui. Une convergence entre espèces n'est pas un signal de valeur : beaucoup de cartes répondent aux points ouverts que la partie commune servie nomme (lecture de la sélection par la génération suivante, multiplicité entre cartes, agrégation fixe des juges), ce qui suffit à expliquer des rencontres.

1. **Traduire une carte en code plus d'une fois avant de croire son verdict** (≈ 9 cartes, quatre espèces) : deux ou plusieurs traductions indépendantes, ou une spécification déclarative bornée exécutée par un interprète écrit hors des agents et comparée au script, avant tout « survit » aux tests de mort ; refus en cas de désaccord, sans juge. Argon `fa46f1f3bd417` ; Astra `fd81c25c080e8`, `f19c7995f9c6a`, `f319823a86ea7`, `ff6ddb6c537f6`, `ff3f04bf88c72` ; Fable `f2d60f571d0e2`, `f2033ad1cbe45` ; Opus `fe0ce53be28b3`. Le style d'Astra est presque toujours celui d'un langage fini ou décidable vérifié par programme.
2. **Jumeaux contrefactuels, permutations et pièges à raccourcis** (≈ 8) : un monde jumeau aux traits de surface permutés ou aux issues permutées, pour séparer la loi portée par les données d'un artefact du générateur, d'une fuite ou de l'a priori des modèles. Argon `fbac0bab50a65`, `fb484116eccc4` ; Carbon `f11f00774547f`, `fb2a799e80c91`, `fe887ca5cb62c`, `f7782e931911d` ; Opus `f562951db6c70` ; Fable `f7219bb36cfcb` (retour d'épreuve permuté vers la génération suivante).
3. **Mesurer les juges croisés sur les témoins plantés** (≈ 7) : votes effectifs du collège estimés sur les erreurs corrélées, sentinelle de dérive de version sur un panier d'ancrage, double rendu et abstention du juge instable ; trois cartes portent le même titre. Argon `fa38f9faa24e0` ; Carbon `fefca0bd94064` ; Fable `fb3a2cc87251c`, `fcfa3d98b90f8` ; Opus `fc37640a0181d`, `fcbf4a2dd1a57`, `f6f8c8b855234`.
4. **Compter la redite par ce que les lois prédisent, non par les mots** (≈ 6) : équivalence des prédictions sur des sondes ou un domaine fini, facettes structurelles ; c'est, en creux, une remarque sur la mesure des redites de cette course même. Astra `f89c771e3ac68`, `f6bb348e95955` ; Opus `fb6f958eb1bb6`, `f69c4a2a9c9e7`, `fd31770b6907d` ; Argon `f7b38afebd589`.
5. **L'héritage cause-t-il les découvertes ? Archive servie contre archive factice ou placebo** (≈ 5) : bras où la génération suivante reçoit la sélection réelle, une archive factice de même forme ou un placebo, lus à plusieurs points du budget. Opus `fdfac3afd4bae`, `f0d21fb62aff2`, `fed7a993d9671` ; Fable `f7a4918afe116`, `fc1f059e8873e`. C'est la question de N-073 § 1 ; plusieurs de ces cartes le disent elles-mêmes.
6. **Mémoire des échecs et réentrée des éliminées** (≈ 9) : banque d'échecs étalonnée, datée ou à péremption, admise par le seul verdict des tests de mort ; quota de réentrée tiré par programme pour les lois éliminées de peu. Argon `f1d7c5f2e47d7`, `f6caf922edbf1`, `fb9e8ae1b97b8`, `f5662015db5bf` ; Carbon `fa312929593cf`, `f20fbf8b6d797` ; Fable `f5373a31410ab`, `fc53dfee17677` ; Opus `f856659046065`.
7. **Contre l'effondrement vers le familier : bifurquer, vider, oublier** (≈ 12, toutes espèces sauf Astra) : un indice de concentration calculé par l'orchestrateur déclenche une bifurcation et un vidage du contexte servi, ou un réducteur programmé décide de ce qui est servi. Argon `f4a47f030c829`, `fcf27198b7462`, `fdafe4598caad`, `f38a6ed2f7434`, `f68f93bac44e8` ; Carbon `f91a7a590c8fe`, `ff76aee57bba1`, `f0a8378953d43`, `f17603c39bc32` ; Opus `f473bb6a03ca3` ; Fable `ff99ce570c638`, `f760c773d6f15`. C'est le regroupement le plus large, et le moins notable (plusieurs cartes reprennent « battre le meilleur de N à budget égal » comme critère, voir § 6).
8. **Portefeuilles et couverture plutôt que classement carte par carte** (≈ 7) : sélection des survivants ou des paires de fusion par couverture comportementale ou structurelle, quotas de queue, quotas de dépense par strate de coût. Argon `f4b85ff3c1033` ; Astra `fdcf828b0dc80`, `fe15813583b5c`, `f4cbf7e62ff7b`, `f327b86c669cc`, `f9c8c39740352` ; Opus `f772b4c18818b`.
9. **Multiplicité et effort compté dans la règle de promotion** (≈ 6) : seuil des e-valeurs chargé du nombre d'essais et de la dépense amont, contrôle des faux découverts sur le registre des essais, placebo de sélection. Argon `f1373c384a771` ; Carbon `f01d286e78e83`, `fb45c8739b3d2`, `f4250eb75fbba` ; Opus `f169420b8d1d8`, `f8c05bffe7cb1`.
10. **Portes sur l'auto-modification de l'organisme** (≈ 6) et **rejeu d'inertie** (3) : toute modification proposée par l'auto-conception passe une porte de version sur des mondes plantés tenus à l'écart, à coût apparié, transactionnelle ou séquentielle ; et un rejeu, mécanisme éteint, dit si une garde a jamais changé une décision. Argon `f98b6974fb1dd`, `f1c19731ccffb` ; Astra `fbae5b702558e` ; Carbon `f7cc0003c4b2c` ; Fable `f76714f1ddda4`, `ff60dbc7baa6f`, `f6e7646851ba5` ; Opus `fd688912a8667`, `fc36c3c3125ac`.
11. **Enrichir le nul du pari** (3) : nul complété par une énumération sans modèle, par les lois que les mêmes familles écrivent sans voir les données (« nul de rappel »), certificat de nouveauté relatif à une archive finie. Opus `fcc96538bff00`, `f51c0935052f6` ; Astra `fec2307cbabb1`. Ces cartes touchent la revendication resserrée du juge au nul formé (N-067, N-071) : à lire avec elles.
12. **Bisociateur à calcul apparié** (4) : témoin à calcul égal pour chaque bras de fusion, allocation des bras sur l'issue scellée seulement, appariement par conflit d'issues vérifiées, carrés factoriels de modifications. Fable `f0497de657ec8` ; Opus `f232221730a16` ; Argon `f71350282d0c0` ; Astra `f2e3582b5fa97`.
13. **Isolés** : masquer les explications servies (Astra `fcd56a5ce3c1c`) ; dose d'appels sans archive (Opus `f11193560f4d4`) ; ancrage structurel par facettes (Argon `f5ee3a75faea3`) ; coupe avant exécution par contraste de logits (Argon `fafa0062508c9`, que le juge Opus marque « un modèle décide ») ; choix des expériences qui séparent les hypothèses et portefeuilles d'épreuves (Astra `fd9bbc7b19deb`, `f19c4c823d67c`) ; certificats de portée (Astra `f1675a6c453a9`) ; compactage certifié de la mémoire (Astra `f14a90c4535dd`).

Aucune carte ne porte sur le saboteur à budget ni sur des moniteurs précis ; une seule emploie le mot « moniteur », pour dire qu'aucun score de moniteur n'est utilisé (`f38a6ed2f7434`).

**Ce que les juges ont marqué** (notes des 27 cartes non notables et des items faux) :
- `reserves_tenues`, presque toujours pour un travail publié cité sans « non vérifié ». Les travaux en cause sont souvent ceux que N-073 rend obligatoires : Wang et al., Zhang et al., Robeyns et al., Sutton et Barto, Schmidhuber et al., Ferreira, Liu, Zheng, arXiv 2611.04420, CADS. Une carte qui suit la lettre de N-073 sans marquer ces citations « non vérifié » est donc marquée fausse (`fed7a993d9671`, `f7a4918afe116`, `f0d21fb62aff2`, `f6f8c8b855234`, `fc37640a0181d`…). Une carte de Fable écrit « à lire sur source avant citation » au lieu de « non vérifié » ; le juge Argon la marque fausse.
- `reserves_tenues`, aussi, chez le juge Opus seul, pour sept cartes qui prennent « battre le meilleur de N tirages à budget égal » comme critère de réfutation propre, sans attribution (`f4a47f030c829`, `f4b85ff3c1033`, `f68f93bac44e8`, `fb9e8ae1b97b8`, `fdafe4598caad`, `f20fbf8b6d797`, `f7cc0003c4b2c`). Le juge Argon ne les marque pas pour ce motif.
- `voisin_nomme` faux (juge Opus, 3) : la différence est dite face à d'autres travaux que le voisin nommé.
- `aucun_modele_ne_decide` faux (3) : un modèle (score de logits, aiguilleur) trie ce qui va à l'épreuve.
- `epreuve_plantee` faux (juge Argon, 1) : temps processeur compté et non apparié.

## 5. Ce que la course ne dit pas

Elle ne dit pas qu'un mécanisme proposé est nouveau, vrai, faisable, utile ou meilleur qu'un autre. Elle ne dit pas qu'un mécanisme du catalogue marche (rien n'y est vérifié), ni qu'une zone est libre (règle R8). Elle ne dit rien sur une hypothèse ou une revendication du programme, ni sur la version suivante de l'organisme avant l'épreuve de ses mécanismes sur monde planté, sur devis. Le classement de l'orchestrateur et les 67 notables ne sont pas une promotion. Les juges n'ont éprouvé qu'un plancher de lecture de forme : quatre items sur cinq sont presque à plafond. L'item `reserves_tenues` ne juge que les six affirmations de la consigne du juge ; la lettre de N-073 § 2 et § 4 reste à lire par la mère sur les cartes. Une convergence entre espèces n'est pas un signal de valeur. Tout travail cité par une carte reste non vérifié (règle R7). « Inédit » ne vaut que comme déclaration du proposeur. Le compte des identifiants existants ne dit pas que le voisin est le bon.

## 6. Nœuds pour la mère et Lazar

1. **Choix des cartes à éprouver sur monde planté** : nœud de la mère et de Lazar, chaque épreuve sur devis (N-058 : oracle du monde planté et coût mesuré). Cette lecture ne propose aucun choix.
2. **Lettre de N-073 à vérifier sur les cartes avant tout réemploi** :
   - § 1, pour les cartes d'héritage servi contre factice (regroupement 5) : citations obligatoires et compléments 1 à 3 ;
   - § 4, pour les cartes qui invoquent la banque sœur, l'audit du générateur ou « Bad Genius » (`fb484116eccc4`, `f7cc0003c4b2c`, `f98b6974fb1dd`, `fcfa3d98b90f8`) ;
   - la règle « aucune porte séquentiel contre meilleur de N », pour les sept cartes qui prennent ce critère comme leur.
3. **L'item `reserves_tenues` contre les citations obligatoires de N-073** : la consigne du juge marque fausse une citation obligatoire sans « non vérifié ». Pour une course suivante : soit la consigne du proposeur dit que ces citations portent « non vérifié », soit le juge les accepte. Rien n'est à changer pour cette course.
4. **Mesure des redites** : zéro redite, alors que trois cartes ont le même titre et que plusieurs regroupements se recouvrent. Plusieurs cartes proposent elles-mêmes une redite par comportement. À garder en tête avant tout usage du compteur actuel.
5. **Coût** :
   - réel 72,50 USD, contre 39,62 au devis v1 et ≈ 59,03 attendus par la ligne de GO ;
   - écarts surtout chez Carbon (4,3 fois le devis) et chez Fable proposeur (2,5 fois) ;
   - proposition au-dessus de son plafond de relais de 45 USD, sous le plafond dur ;
   - à reprendre dans tout devis suivant ; soldes de Gemini et d'OpenAI à relever aux interfaces.
6. **Les deux cartes retenues** par l'aiguilleur (`f9a7c8311d714`, `f640bf1e40418`) ne sont ni jugées ni lues ici. Elles restent sous scellé ; les lire ou non est un choix de la mère.
7. **Réserve R4** sur la case « originalité », entièrement notable : consignée, compatible avec le hasard (probabilité 0,12) ; aucune suite proposée.
