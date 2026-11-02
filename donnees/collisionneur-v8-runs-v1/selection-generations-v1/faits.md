# Faits servis — question « boucle de sélection génération à génération de l'organisme d'idéation » v1 — v1

Assemblés par un sous-agent neuf (assembleur), 1er novembre 2026, pour trois canaux (Argon seul, Kimi seul, collisionneur à quatre espèces). Dossier de travail hors git. Pièces tirées de `origin/canal/conv-audit-n04` (sauf mention `main`) ; empreintes recalculées par `sha256sum` sur le fichier entier, même quand un extrait seul est servi.

- **Question servie** : `question-selection-generations-v1.md` — `c899221888d14e2df0640ac1b405cef286ca3bd84b45bec998519ac53fccbfcd` (833 mots).
- **Règle 2** : 5 passages retirés, tous dans la pièce 7 (conception du pont, § h « Décisions pour toi ») : les cinq clauses « Recommandation : … ; confiance … ; défaut sous 48 heures : … » des décisions D-P1 à D-P5 sont remplacées par la marque ; la décision, l'enjeu et les options (avantage, inconvénient) restent. Gardés, comme faits et non comme avis sur la question : les « seuils recommandés » de l'étalonnage des juges du pré-pilote (pièce 1, § 6, chiffres de [B10]), les confiances « 0,4 à 0,5 » des analogies des protocelles (pièce 1, § 9.3), « relancer la course 1 : déconseillé (R-737) » (pièce 1, § 10, décision consignée), les probabilités d'originalité des hypothèses (pièce 10, calibrées au 14 septembre, partie du document qui fait foi), « originalité revue à environ 0,35 (mon estimation, non sourcée) » sur HC3 (pièce 11, ne porte pas sur la question), et les options (a), (b), (c) de N-035 dont (a) est « retenue » par Lazar (pièce 12).
- **Niveau méthode** : aucune pièce du bras d'attaque ; rien sur l'auto-organisation inspirée d'Avalon. Les pièces décrivent le pôle (juge figé, gel, témoins, mémoire, recombinaison), ses lancements et ses lectures, le pont fiche → loi (conception seulement, pas le code `pont_v1.py`), et les hypothèses du programme.

## Pièces

| n° | pièce | chemin d'origine | sha256 recalculée (fichier entier) | mots (fichier entier) | servi |
|---|---|---|---|---|---|
| 1 | dossier factuel de l'organisme, § 1, § 6, § 9, § 10 | `docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md` | `0751fc8cf4aa0a9eaccb23d80cb06220fa3db9805092bd1d854bc68fce7ae250` | 9,741 | extraits l. 18–97, 185–193, 242–280, 282–292 |
| 2 | conception du pôle : intégration des proposeurs, § 1 (la boucle) et § 2 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/integration-proposeurs-ia-v1.md` | `974b2dbe17b76975f8e9198f5852a36513f8a428b44874740e31395b34124184` | 2,976 | extrait l. 40–98 (l. 42–98 citées, plus le titre de section) |
| 3 | programme de conception de l'organisme v7, § 0 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/programme-conception-organisme-v7.md` | `b7cd2f56bf99357caf51493ca0ed966753711926c91c094f971197b29c7192fd` | 4,278 | extrait l. 19–41 (l. 23–33 citées, paragraphe entier) ; aucun compagnon `.sha256` sur la branche (R11 : fichier présent, empreinte lue ce jour) |
| 4 | lecture du lancement réel « (a) bis » | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/premier-lancement-reel/lecture-lancement-reel-a-bis-v1.md` | `cc475e042c15870e526ce322997dcec801652a9cfd79f3020d00f2bca538d9e4` | 778 | entière |
| 5 | lecture de la couche 1 v7, v2 (banque réelle, « pas de dents ») | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/demonstration-couche1-v7/lecture-couche1-v7-v2.md` | `e2946dd65c573fa00ce8eac90bf1640269b1a800efe6531adb2a9cce108d2c9e` | 546 | entière |
| 6 | lecture des démonstrations du cycle v5 | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md` | `60345b906006b7cfd0381354a2d19ead86a0e659f8d03a7a39b636f5cda440b4` | 1,130 | entière |
| 7 | pont fiche de course → fiche-loi, conception v1 (rendu avant le lancement) | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pont-fiche-loi-v1/conception-pont-fiche-loi-v1.md` | `5161e199e15dacc728d4b2e7b1769f700e0a293c05fb26d402dfe40d25c4a974` | 6,545 | entière, règle 2 appliquée au § h ; le code `pont_v1.py` et ses essais ne sont pas servis |
| 8 | pont, LISEZMOI v1 (état, essais, pièces lues) | `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/pont-fiche-loi-v1/LISEZMOI-pont-v1.md` | `7b1c131db760014798af159047849163bedc03b706f2f684dd0962ac4d6bd17a` | 883 | entier |
| 9 | programme v2 (`main`), section 5 « Hypothèses » : H1 à H8, HC1 à HC6, H3 à H7 (H9 vient de N-035) | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` | 4,587 | extrait l. 88–115 ; le document fait 4 411 mots, seule cette section est servie |
| 10 | décision N-013 (`main`) : revendications précisées après le niveau 2 de l'état de l'art | `docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` | 1,389 | entière |
| 11 | décision N-035 (`main`) : H9, survie des contraintes de sécurité à la délégation | `docs/decisions/decision-N-035-v1.md` | `55df073d6918405949f3543308f0de7f90293baeefc5a4525e5f49697b2517e6` | 680 | entière |

**Pièces listées mais absentes ou non servies** : aucune absente. Le dossier `pont-fiche-loi-v1/` contient aussi `pont_v1.py` et `essais/test_pont_v1.py` (code) : non servis, la question demande la conception seulement. Les sources que citent les pièces (brouillons B10, TI, registres [Dbr], [Dmain], lectures de génération 0, de la couche 1 bis, etc.) ne sont pas des pièces listées et ne sont pas servies.

---

### Pièce 1 — dossier factuel de l'organisme — § 1 vue d'ensemble (`dossier-factuel-organisme-v1.md`, `0751fc8cf4aa…`, extrait l. 18–97)

## 1. Vue d'ensemble

### 1.1 Deux étages qu'il ne faut pas confondre

1. **La course d'idéation** (courses 1 et 2) : des modèles de langage lisent un dossier fermé et écrivent des **fiches d'idées** (hypothèse, prédiction chiffrée, antériorités, critère de mort, première expérience) ; un aiguilleur, une mémoire, une vérification de références et des juges-modèles les trient ; un bisociateur fusionne des paires. **Ici tout est jugement ou contrôle de forme**, sauf l'étage de tests de mort, codé mais jamais activé ([TI] l. 44-48 ; [B10] l. 221).
2. **Le pôle de test d'hypothèses** (« boucle automatique », orchestrateur v7) : une hypothèse est écrite comme une **loi prédictive chiffrée** sur des épisodes ; elle est **gelée** (empreinte) avant l'expérience ; un **agent expérimentateur** écrit et exécute du code dans un bac à sable ; un **vérificateur d'une autre famille** rejoue ; un **juge figé statistique** (pas un modèle de langage) ne promeut que ce qui bat des prédicteurs aveugles sur des épisodes produits après le gel, avec 5 % de fausses promotions garanties. **Ici une hypothèse est réellement testée par calcul** ([P]`conception-pole-scientifique-v1.md` § 1 ; [P]`integration-proposeurs-ia-v1.md` § 1 ; [P]`programme-conception-organisme-v7.md` l. 23-33).

Le pont entre les deux (traduire une fiche d'idée en loi prédictive testable, « prise idéation ») est **conçu, pas construit** ([P]`integration-proposeurs-ia-v1.md` § 2, l. 95-98).

### 1.2 Parcours d'une idée dans la course 2 (état prévu au 1er novembre)

1. **Question servie** : texte I (axes 1 à 5 et 7) ; texte II (axe 6, deux bras) et texte III servis à part ([TI] ; [Dbr] R-565 l. 779, R-824 de [Dmain] l. 1052). Pièces fermées : 23 papiers, listes L, M, D, F ([TI] l. 76).
2. **Moisson** (option) : métadonnées et résumés d'arXiv et d'OpenAlex servis aux proposeurs entre les passes — codé (v47), jamais servi en course (§ 2).
3. **Passe 1** : Kimi K3.1 Pro (Moonshot) et Argon (Google, Gemini) écrivent chacun au plus deux fiches par axe ([TI] l. 48 ; [Dbr] R-567 l. 781 ; devis v6 § 4.1, Argon proposeur « SUPPOSÉ »).
4. **Garde de forme programmée**, puis **aiguilleur** (avant tout juge) : « niveau méthode » → continue ; « trop concret » → scellé au bras d'attaque, compté ([Dbr] R-575 l. 789 ; [B10] l. 282).
5. **Tableau minimal** : chaque proposeur reçoit titres et résumés d'une ligne des fiches de sa case, puis **passe « tableau »** (seconde passe) ([Dbr] R-598 l. 812).
6. **Mémoire anti-redite** et **double garde de l'axe 7** : repèrent les paraphrases ([B10] M3 l. 274-280).
7. **Bisociateur** : trois bras choisissent chacun une paire de fiches ; Kimi écrit la **fusion** ; la fusion repasse par l'aiguilleur puis les juges ([B10] M9 l. 293-310).
8. **Étage 1** (analyseur programmé, contrôle du format, des pages citées d'HELIOS, des données) puis **étage 2** : trois juges-modèles (Kimi et Argon croisés, Opus 5.5 sur tout) → « notable » ou « non notable » ; classement par axe ([TI] l. 46).
9. **Vérification d'antériorité** par Claude avec recherche, puis sur PDF empreinté (R7) ([Dbr] R-573 l. 787 ; [TI] annexe 3 l. 150-156).
10. **Tests de mort** (machine louée jetable, bac à sable, script exécuté par le noyau, seuil gelé lu mécaniquement) sur les fiches les mieux classées — **codé, jamais activé** ([Dbr] R-636 l. 850, R-640 l. 854).
11. **Génération suivante** : fiches scellées anonymes de g servies à g + 1 avec verdict, classement et étiquette d'héritage (neuve / affine X / réfute X) ([TI] l. 72-73).
12. **Sortie vers le programme** : une fiche survivante devient, hors de la course, un **préenregistrement scellé** (R1), contre-lu (R2), exécuté sur GO, jugé par un lecteur neuf (R13), soumis à Lazar. Aucune fiche de course n'a encore fait ce chemin (§ 10).

### 1.3 Qui fait quoi (modèles et fournisseurs)

| Rôle | Course 1 (30 oct.) | Course 2 (prévue) | Source |
|---|---|---|---|
| Proposeurs | Fable 5.1 (Anthropic) + Argon (Google) ; Opus 5.5 retiré après refus | Kimi K3.1 Pro (Moonshot) + Argon | [Dmain] R-802 l. 1030 ; [Dbr] R-567 l. 781 |
| Juges | Opus 5.5 + Argon (Fable a refusé de juger) ; Kimi en 3e juge après coup | Kimi + Argon en notation croisée ; Opus 5.5 troisième juge sur tout | [Dmain] R-804, R-811, R-827 ; [Dbr] R-577, R-578 l. 791-792 |
| Aiguilleur, second lecteur, adjudicateur | absent | instances isolées du bras d'attaque, chez session-depot | [B10] l. 690 |
| Antériorité | — | Claude (Opus ou Fable) avec recherche, jamais Kimi | [Dbr] R-573 l. 787 |
| Fusions | — | Kimi | [B10] l. 308 |
| Rédacteur de témoins, metteur en forme tiers | Sonnet (témoins v1) | Sonnet 5.5 ; relecteur Fable 5.1 (proposé, D-f) | [B10] l. 52, 671 |
| Collisionneur | — | Fable 5.1, Opus 5.5, Argon, Kimi | [Dmain] R-826 l. 1054 |
| Pôle : expérimentateur / vérificateur | Opus 5.5 / Fable 5.1 (lancements réels du 27 oct.) | — | [P]`premier-lancement-reel/lecture-lancement-reel-a-v1.md` § 1 |

### 1.4 Schéma à dessiner (nœuds, arêtes étiquetées, boucles)

**Nœuds de la course** :
- Q « Question servie (textes I, II, III) + dossier fermé »
- MO « Moissonneur (arXiv, OpenAlex) » [codé, pas en service]
- PR « Proposeurs : Kimi, Argon »
- GF « Garde de forme programmée »
- AI « Aiguilleur (+ second lecteur, adjudicateur) »
- BA « Bras d'attaque scellé (session-depot) »
- TB « Tableau minimal »
- ME « Mémoire anti-redite + double garde axe 7 »
- BI « Bisociateur : bras méta, bras Gu-Krenn, bras basique »
- FU « Fusion écrite par Kimi »
- E1 « Étage 1 : analyseur programmé »
- J « Juges : Kimi ⇄ Argon croisés, Opus 5.5 »
- T « Témoins plantés (anonymes) »
- AN « Vérification d'antériorité (Claude + PDF) »
- TM « Tests de mort (bac à sable, machine jetable) » [codé, jamais activé]
- CG « Tests sur carte graphique par fiche + IA scientifique externe » [décidés, pas construits]
- G+1 « Génération suivante »
- PRE « Préenregistrement scellé + contre-lecture »
- EXP « Expérience du programme (pôle : expérimentateur, vérificateur, juge figé) »
- V « Verdict par lecteur neuf → porte → GO de Lazar »
- CO « Collisionneur (4 espèces) » — conseille Lazar, hors flux
- L « Lazar »

**Arêtes** :
- Q → PR : « question + pièces » ; MO → PR : « métadonnées et résumés (entre passes) »
- PR → GF : « fiches passe 1 » ; GF → AI : « fiches de forme valide »
- AI → BA : « trop concret : scellé, compté » ; AI → TB, ME, BI, E1 : « niveau méthode »
- TB → PR : « titres + résumés d'une ligne (même texte, même bras) » → **boucle** PR → passe « tableau » → GF
- BI → FU : « une paire par bras » ; FU → AI : « la fusion repasse » (**boucle**)
- ME → J : « paires signalées » (fusion mécanique des doublons)
- T → E1, J : « témoins glissés anonymes »
- E1 → J : « conforme / signalé » ; J → AN : « notables, classement »
- AN → TM : « fiches les mieux classées » ; TM → G+1 : « résultats exploratoires, jamais aux juges de la même course »
- J, AN → G+1 : « fiches scellées anonymes + verdicts + classement » → G+1 → PR (**boucle entre générations**)
- AN, TM → PRE : « fiche survivante » ; PRE → CG ou EXP : « exécution sur GO » ; EXP → V ; V → L : « soumis pour GO »
- L → Q, CO : « décisions, questions » ; CO → L : « avis sur nœuds »

**Nœuds du pôle (boucle de test, second schéma)** : fiche-loi → gel (empreinte) → expérimentateur (partie de développement, bac à sable) → affinage → gel de la fiche affinée → juge figé (partie d'épreuve jamais vue, nul informé, témoins) → sélection (aptitude = sévérité du test survécu) → recombinaison bisociative des survivantes (la fille doit prédire plus que ses parents) → mémoire (refuse les redites, hérite la preuve) → génération suivante ; vérificateur d'une autre famille entre expérimentateur et juge ; archive complète des éliminées ([P]`integration-proposeurs-ia-v1.md` l. 42-71).

---

### Pièce 1 (suite) — dossier factuel — § 6 les juges (`dossier-factuel-organisme-v1.md`, `0751fc8cf4aa…`, extrait l. 185–193)

## 6. Les juges

- **Qui** : étage 1 = **analyseur programmé** (il décide K5 : format des antériorités, pages des chiffres d'HELIOS, données dans la liste D) ; étage 2 = **Kimi K3.1 Pro et Argon en notation croisée + Opus 5.5 troisième juge sur toutes les fiches** (arbitre des désaccords) ([TI] l. 46 ; [Dbr] R-577, R-578 l. 791-792).
- **Ce qu'ils notent** : grille **binaire** K1 à K5 contre les listes fermées : K1 livrables de l'axe présents ; K2 source d'avantage dans L avec coût de reproduction chiffré (pièce, page), ou antériorité la plus proche et élément absent nommés ; K3 prédiction chiffrée et signée (rappel à 1 % de fausses alertes par famille pour une détection) ; K4 critère de mort à seuil numérique, première expérience sur processeur ou données déjà payées ; K5 antériorités au format, chiffres d'HELIOS conformes. **« Notable » = K1 à K5 vrais.** Classement par axe : facultatifs passés, puis coût croissant ([TI] l. 46). Agrégation des trois juges : règle de la v53, à défaut « notable chez au moins deux des trois » ([B10] l. 309).
- **Étalonnage sur témoins (pré-pilote, M1)** : classes plantées P (notable), C (creuse mais conforme : notable sous la grille), N1 à N4 (chacune viole un item K1 à K4 entre deux champs nommés), G (défaut que seul l'étage 1 doit voir) ([B10] l. 673-683). Seuils recommandés : exactitude équilibrée S1 ≥ 0,80, rappel S2 ≥ 0,70, plancher S3 0,70, accord S4 (kappa de Fleiss ≥ 0,45) ([B10] l. 22-25). Prédiction : Opus 0,90, Argon 0,85, Kimi 0,80 ; porte des juges seule 0,38 ([B10] l. 242, 8).
- **Course 1** : 6 témoins tenus chez Opus et Argon ; accord de rang entre juges **0,12** ; témoins plus courts que toutes les fiches (épreuve plus faible qu'annoncé) ; Kimi échoue à un témoin ; **auto-préférence d'Argon ≈ 1,8 point sur 15** ([Dmain] R-811, R-827).
- **Ce qu'ils ne font pas** (à dire clairement) : l'étage 2 ne note que la **cohérence entre champs** ; **ni « décisif » ni « inédit » n'est noté** ([TI] l. 46) ; ils ne jugent pas la valeur scientifique (« la classe C le rend visible », [B10] l. 234 A4) ; ils n'exécutent rien ; ils ne vérifient pas l'antériorité ; ils ne testent pas la plausibilité (« très plausible » est porté par les tests de mort, « inédit » par l'antériorité sur PDF, [B10] l. 221) ; l'auto-préférence n'est plus mesurée (M2 retirée, [Dbr] R-634 l. 848).
- **À ne pas confondre** avec le **juge figé du pôle**, qui n'est pas un modèle de langage : pari séquentiel, inégalité de Ville, inférence universelle contre un nul composite, garantie de 5 % de fausses promotions, règle de fausses découvertes entre hypothèses, témoins plantés ([P]`programme-conception-organisme-v7.md` l. 23-29). Validé en simulation : 18 contrôles fatals à 0 ou 1 sur 1 000 ([P]`experience-1-juge/lecture-experience-1-v1.md` ; nul des filles v2 : 13 contrôles à 0 sur 1 000, [P]`nul-des-filles-v2/lecture-experience-2-v1.md`).

### Pièce 1 (suite) — dossier factuel — § 9 des idées aux hypothèses testées (`dossier-factuel-organisme-v1.md`, `0751fc8cf4aa…`, extrait l. 242–280)

## 9. Des idées aux hypothèses testées — et la question de Lazar

### 9.1 La chaîne réglementaire (règles gelées, `CLAUDE.md`)
R7 (aucun chiffre sans PDF empreinté, page citée) → **tests de mort** → **antériorité** → **R1** préenregistrement scellé (hypothèse, prédiction chiffrée et signe, métrique, seuil, plan, critères gelés, liste d'arrêt) → **R2** contre-lecture par un sous-agent neuf → exécution sur GO (dépense) → **R13** verdict par un sous-agent neuf qui applique les critères gelés → **porte** → GO de Lazar.

### 9.2 Les tests de mort, en clair
- **Ce que c'est** : pour une fiche, le noyau écrit et scelle un **préenregistrement court** (hypothèse, prédiction, seuil gelé, données) ; un **agent expérimentateur** demande au noyau d'exécuter un script ; **le noyau l'exécute** dans un bac à sable (`bwrap` : sans réseau, système en lecture seule, un seul dossier inscriptible), 3 exécutions de 120 s au plus ; le noyau **lit mécaniquement** la ligne `RESULTAT:` et applique le seuil gelé ; un **lecteur neuf** rend « survit / éliminée / non concluant » ; un désaccord avec la lecture mécanique vaut « non concluant » ; résultats **exploratoires**, jamais servis aux juges de la même course, servis en matériau à la génération suivante ([N]`orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v48.md` l. 30-44).
- **État** : CODÉ (v48), bac à sable jugé non sûr par deux contre-lectures (CL13, CL14 : voie vers le superutilisateur de l'hôte), durci en v50 ([Dbr] R-524 l. 738, R-533 l. 747) ; machine louée **jetable sans secret** DÉCIDÉE (R-640 l. 854) ; placé « entre générations » en v53 ([N]`orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v53.md` l. 26) ; **jamais activé** : course 1 lancée « sans l'étage » ([Dmain] R-802), « pas activés » ([Dbr] R-636 l. 850) ; hors du pré-pilote (DEP11, [B10] l. 706) ; essais de bac réel non joués ici ([N]`orchestrateur-v56/LISEZMOI…-v56.md` § 3).

### 9.3 Protocelles
- Papier de Lazar, « Protection of an RNA replicase by protocells has a ceiling and a price » (v0.19.2, PDF dans `docs/sources/pdf/`) ; lu par conv-audit comme **source d'analogies à éprouver** pour l'organisme : « ce qui se reproduit, c'est la paire » (une fiche seule est stérile sous la fusion) → critère d'allumage par **processus de branchement** (rayon spectral de la matrice des descendants) ; « parasites » = fiches faciles à fusionner qui n'engendrent rien ; fusion inachevée jetée, jamais archivée ([P]`papier-protocelles-idees-v1/idees-conv-audit-papier-protocelles-v1.md` § 1-5). Confiances 0,4 à 0,5.
- Collisionneur sur les protocelles : tour 2 fini, synthèse : 27 accords, 5 divergences résolues sur 6, seule la prédiction P10 retenue par les trois ([Dmain] R-939 l. 1168). La règle « fusions inachevées jamais réutilisées » est codée en v56 ([N] LISEZMOI v56, CL20-05 et § 5 point 4).

### 9.4 Réponse à : « je croyais que les modèles allaient appeler des agents pour tester les hypothèses et les idées plutôt que de s'en fier à des jugements »

Lazar a déjà posé la même question le 29 octobre ; réponse consignée : « l'exécution par l'idéateur est la couche 3 prévue et non construite » ([Dbr] R-477 l. 691) ; et le 30 octobre : « les tests de mort par agents existent dans l'orchestrateur mais ne sont pas activés » ([Dbr] R-636 l. 850). État au 1er novembre :

**A. Ce qui teste réellement par calcul, et a tourné**
1. **Génération 0 du pôle** (26 oct.) : 18 affirmations du rapport de méta-conception de Gemini testées par calcul indépendant par deux sous-agents expérimentateurs sur processeur : **5 survivent, 10 éliminées, 3 indécises**, 0 dollar ([P]`generation-0/synthese-generation-0-v1.md`). Non vérifiées par un agent d'une autre famille.
2. **Lancements réels du cycle du pôle** (27 oct.) : agents expérimentateurs (Opus 5.5) qui écrivent et exécutent du code en bac à sable, vérificateurs (Fable 5.1) qui rejouent, juge figé : (a) 140 appels, 6,24 dollars, génération 1 perdue par un défaut de plomberie ; (a bis) 136 appels, 5,89 dollars, 2 témoins vrais promus, 2 faux éliminés, 11 rejeux confirmés sur 11. **Réserve : monde tautologique** — prouve la plomberie, pas une découverte ([P]`premier-lancement-reel/lecture-lancement-reel-a-v1.md`, `…-a-bis-v1.md`).
3. **Couche 1 sur banque réelle** (épisodes du modèle de 8 milliards notés par deux juges) : rien promu, **« pas de dents »** (0 témoin vrai promu sur 20) ([P]`demonstration-couche1-v7/lecture-couche1-v7-v2.md` ; `demonstration-couche1-proposeur-v7/…-v1.md`). Le programme v7 écrit pourtant « la boucle a tourné de bout en bout sur données réelles » (l. 30) : vrai pour la plomberie, pas pour un résultat.
4. **Simulations et rétrodictions** (sous-agents, processeur) : juge v1 et nul des filles v2 validés ; démonstration du cycle v5 ; essais de la mémoire ; « Boucle d'or » ; rétrodiction de Swanson sur arXiv (D1 réfutée : la marche de Swanson ne bat pas l'allocation de ressources, −0,82 point) ([P]`retrodiction-swanson/retrodiction-swanson-v1.md`) ; bisociation à deux espaces (non concluant) ; pilote synthétique « mélange d'équilibre » (brouillon 4, essai : Q1 réfutée, racine d'essai sans lecture de décision) ([Dbr] R-1031 l. 995).

**B. Ce qui n'est que jugement**
- Toute la **notation de la course** (courses 1 et 2) : juges-modèles sur la cohérence entre champs ; ni valeur, ni nouveauté, ni plausibilité notées ([TI] l. 46).
- Le **collisionneur** : avis et critique croisée, sans exécution.
- La **vérification d'antériorité** : recherche et lecture, pas une expérience.
- Les « idées » des protocelles et des brainstorms : analogies à éprouver.

**C. Prévu mais pas construit (ou codé non activé)**
- **Étage de tests de mort** dans la course : codé (v48 à v56), jamais activé ; machine jetable décidée ; essais de bac réel non joués.
- **Tests sur carte graphique par fiche** (sondes sur le modèle à poids ouverts) : DÉCIDÉ (« a puis b et c en parallèle »), un devis et un GO par fiche — rien lancé ([Dmain] R-776 l. 1004).
- **IA scientifique externe** (The Agentic Scientist v3, Sakana, voulue par Lazar) : revue de sûreté **sur pièces seulement** (code non lu), « aucun lancement avant la lecture du code et un essai à blanc » ([P]`ia-scientifique-externe-v3/revue-surete-v3-v1.md` § 1 point 10 ; [Dbr] R-555, R-557) ; comparaison (b) contre (c) par règle écrite avant lecture : à faire.
- **Traduction fiche d'idée → loi prédictive** testable par le pôle (« prise idéation ») : conçue, non construite ([P]`integration-proposeurs-ia-v1.md` § 2).
- **Couche 3** (épisodes ou moniteurs neufs produits à la demande) et **couche 2** (banque avec sabotage) : au plan, non exécutées ([P]`programme-conception-organisme-v6.md` § 4).
- **Duel des proposeurs** (proposeur de la littérature contre le nôtre, même juge, plafond 100 dollars) : devis écrits ; aucune trace de lancement trouvée ([P]`demonstration-proposeurs-v7/devis-duel-proposeurs-v2.md` ; [Dmain] R-595).
- **Adversaire scellé** (voie d) : conçu au niveau méthode, exige une revue de sécurité externe avant toute exécution ; rien lancé ([P]`programme-conception-organisme-v7.md` § 3 bis).

---

### Pièce 1 (suite) — dossier factuel — § 10 résultats déjà obtenus (`dossier-factuel-organisme-v1.md`, `0751fc8cf4aa…`, extrait l. 282–292)

## 10. Résultats déjà obtenus

- **Course 1, tentative 1** (29 oct.) : arrêtée à 10:48 UTC, refus d'Opus 5.5 proposeur puis bascule automatique vers Opus 4.8 sans GO ; aucune fiche validée ([Dmain] R-764 l. 992).
- **Course 1, tentative 2** (30 oct.) : **29 fiches validées** (3 en quarantaine), juge Fable refuse ; rejugées par Opus 5.5 et Argon : **27 éligibles sur 29**, 15 de Fable, 14 d'Argon, 5 et 5 dans les dix premières ; accord de rang 0,12 ; totaux serrés (12,0 à 12,5 sur 15 dans les dix premières) ; **17 idées distinctes** (12 paires de doublons) ; auto-préférence d'Argon ≈ 1,8 point ; coût ≈ 37 dollars ([Dmain] R-804, R-811, R-820, R-827). « Notable » n'existait pas encore (classement par totaux ; critères de la course 1 décrits comme « avantage décisif ou approche inédite », [P]`question-mere-course-v1/question-mere-course-ideation-v3.md` l. 42-46).
- **Ce qui est sorti de la course 1** : des corrections d'instruments (mémoire anti-redite, témoins de longueur comparable, relais Kimi v3, notation croisée, aiguillage) ; **aucune fiche de la course 1 n'est tracée comme devenue hypothèse ou expérience du programme** dans ce que j'ai lu ; les fiches sont sous `donnees/` et non lues par conv-audit (règle). Relancer la course 1 : déconseillé (R-737 l. 951).
- **Démonstrations du cycle v5** : seuil par fiche (vraies filles refusées à tort 31 → 4) ; marchepieds 282 contre 212 vraies filles dans le monde fécond, 236 contre 245 dans le monde plat ; mémoire 0 double sur 31 ; aucune fausse promue. **Mécanisme vérifié, pas une découverte** ([P]`demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md`).
- **Génération 0** : 5 / 10 / 3 (ci-dessus) ; deux correctifs utiles retenus (normaliser les hachages ; diversité de domaine dans le tirage).
- **Protocelles** : analogies (allumage par branchement, parasites, fusions inachevées) ; tour 2 du collisionneur synthétisé ; une règle passée dans le code (fusions inachevées archivées à part, jamais réutilisées).
- **Idées de l'organisme ou de ses brainstorms devenues préenregistrements ou pilotes** (toutes exploratoires, aucune porte franchie) : bisociation à deux espaces v2 (scellée, validation non concluante, v3 en brouillon) ; épreuve d'identification « semi-réel » (brouillon 7, [Dbr] R-1033) ; reproduction et test hors échantillon de Gu-Krenn (préenregistrement v2 sur `main`) ; pilote synthétique « mélange d'équilibre » (arène coévolutive P-041, brouillon 4). Ces pistes viennent des questions de Lazar et du collisionneur, pas de fiches de course.
- **Aucune porte franchie** ; critères de G0 prouvés : 1 et 5 seulement (`registres/etat.md` l. 57).

### Pièce 2 — intégration des proposeurs dans l'organisme — § 1 la boucle, § 2 les prises (`integration-proposeurs-ia-v1.md`, `974b2dbe17b7…`, extrait l. 40–98)

## 1. La boucle, colonne du dispositif

La vie d'une fiche, de la proposition à la promotion ou à l'élimination :

1. **Proposition.** Un proposeur formule une fiche : énoncé en une phrase, **loi prédictive signée et chiffrée** des issues
   sachant les traits des instances, sur un espace d'instances déclaré, métrique, nul, seuil qui peut échouer, coût borné,
   parents (pour la recombinaison), domaines, opérateurs, contraintes de validité.
2. **Gel du test.** La fiche est empreintée **avant** l'expérience (R1). C'est la seule formalité gardée, automatique. Un
   test choisi après coup ne réfute rien : c'est ce gel qui rend l'élimination signifiante.
3. **Test sur la partie de développement.** L'expérimentateur écrit son code, le lance sur la **partie de développement**
   de la banque (traits et issues visibles), lit les traits, rend verdict, nombres, artefacts.
4. **Affinage épisode par épisode** *(première échelle, à l'intérieur d'une génération)*. L'expérimentateur **itère** sur
   la partie de développement : il resserre la loi prédictive, l'espace d'instances déclaré, le nul, à mesure qu'il voit
   les épisodes. Chaque lot d'épisodes aiguise la fiche. **Le signal d'affinage est la seule partie de développement** —
   jamais le verdict du juge figé sur l'épreuve (N-053). C'est ici que vivent la recherche arborescente d'un système de la
   littérature (investigation, réglage, ablations) et la liberté d'explorer.
5. **Gel de la fiche affinée.** La fiche resserrée est empreintée. Fin de la liberté : ce qui est jugé est ce qui est gelé.
6. **Jugement sur la partie d'épreuve.** Un **juge figé, hors des agents**, ne lit que des issues produites **après le
   gel**, sur des unités d'**épreuve** que la fiche n'a **jamais vues**, contre un nul informé et un nul d'archive, avec
   une garantie de fausses promotions démontrée (inférence universelle, inégalité de Ville), et des **témoins plantés** à
   vérité connue (vrais et faux). L'ordre d'épreuve est tiré en secret après le gel.
7. **Sélection.** Réfutée → éliminée et archivée ; survivante → **aptitude = sévérité du test survécu** (−log de la
   probabilité de survie sous le nul), **jamais** le signe ni l'ampleur du résultat (R3) ; indécise → un test plus
   puissant, ou retirée après deux essais.
8. **Affinage génération par génération** *(seconde échelle, d'une génération à l'autre)*. Les **survivantes** ensemencent
   la génération suivante : **recombinaison bisociative** (tirage éloignement de domaine × similarité d'opérateur sur arbre
   syntaxique canonisé, pont par un opérateur commun, filtre mécanique de compatibilité des contraintes, fusion) ; la fiche
   fille doit **prédire plus que ses parents** (contenu empirique accru), sinon elle n'entre pas dans la population. La
   **mémoire à empreinte prédictive** refuse les redites et **hérite la preuve**. Les **tâches sont fraîches à chaque
   génération** (N-049 : tirage dans un vivier, pas un jeu figé). L'**héritage sur K ≥ 3 générations est récompensé**
   (N-045-v2).
9. **Archive complète**, éliminées comprises : contre le biais du survivant, et pour mesurer le pôle lui-même (témoins).

**Les deux échelles d'affinage, nommées clairement :**

| échelle | où | sur quoi | signal d'affinage |
|---|---|---|---|
| **épisode par épisode** | à l'intérieur d'une génération | partie de développement (traits et issues visibles) | le développement seul — jamais le juge figé |
| **génération par génération** | d'une génération à la suivante | population des survivantes | sévérité du test survécu + recombinaison + héritage de la mémoire |

**Le pare-feu qui rend l'affinage légitime (et non un apprentissage à plaire au juge)** : la séparation développement /
épreuve ; le juge figé hors des agents ; **aucun score de moniteur ni de juge dans l'entraînement ou la sélection de
l'agent** (N-053, invariant). C'est exactement ce qui nous sépare des systèmes publiés (section 7 de v6/v7 : la différence
n'est pas *qui exécute* — nos agents exécutent — c'est *qui juge*).

## 2. Les prises (corrigées par la consigne « tester et affiner »)

La consigne de 12:18 fait de la « proposition seule » un **cas dégénéré** : un proposeur digne de ce nom tient la boucle
complète. Deux prises subsistent, selon ce que le système publié sait faire :

- **Prise « boucle complète »** (proposer + tester + affiner). Pour les systèmes qui lancent leurs propres expériences.
  Ils se branchent au **rôle expérimentateur** : ils explorent et affinent sur le **développement**, puis **gèlent** des
  fiches que **notre** juge figé évalue sur l'**épreuve**. On ne retire que leur **relecteur modèle** (ils jugeaient leur
  propre résultat) et on leur impose **le gel avant l'épreuve**. Ils tournent en **conteneur sans clés ni réseau**
  (avertissement de leur propre README : agents à pleins droits, clés montées — écarté).
- **Prise « idéation »** (proposer + classer seulement). Pour les systèmes dont les expériences sont faites par des
  humains. Ils proposent et classent des idées (tournois) ; **nos** expérimentateurs tiennent la boucle test-et-affinage
  sur leurs idées. Le point de passage est la **traduction de la fiche** (idée en texte libre → loi prédictive sur un
  espace d'instances déclaré) ; on mesure ce qu'on perd à la traduction, et qu'une idée traduite est encore l'idée proposée.

### Pièce 3 — programme de conception de l'organisme v7 — § 0 (`programme-conception-organisme-v7.md`, `b7cd2f56bf99…`, extrait l. 19–41)

## 0. En tête : ce qu'est devenu le programme (paragraphe commun au dossier du fonds)

*(Inchangé par rapport à la v6 ; la décision D1 reste en proposition.)*

Le programme est désormais conduit par une **boucle automatique de test d'hypothèses**. Des agents proposent des hypothèses
sous forme de paris précis — une loi prédictive sur les issues d'épisodes concrets — et un **juge figé, tenu hors des
agents**, ne promeut que ce qui bat une bibliothèque de prédicteurs aveugles sur des issues produites après le gel de
l'hypothèse, avec une garantie de 5 % de fausses promotions validée (pari séquentiel, inégalité de Ville, inférence
universelle contre un nul composite), une règle de fausses découvertes entre hypothèses, des témoins plantés à vérité
connue, et une mémoire qui refuse les redécouvertes et transmet la preuve d'une génération à l'autre. Le juge, le nul des
hypothèses recombinées et la mémoire ont été validés en simulation avec des contrôles fatals à 0 sur 1 000 ; la boucle a
tourné de bout en bout sur données réelles cette semaine (120 épisodes d'un modèle de 8 milliards de paramètres notés par
deux juges). Son but : rendre le programme *rapide et tolérant à l'échec* — beaucoup d'hypothèses testées à bas coût, un
échec qui ne coûte presque rien, et aucun résultat que la machine puisse se raconter. Les prochaines étapes la pointent
sur les deux questions du programme, sur de vrais épisodes de sabotage, puis sur la **mesure et la prédiction de ce que nos
moniteurs manquent** : une carte des hypothèses que chaque moniteur fait sur l'agent (ce qu'il suppose indépendant, borné,
visible), les lemmes qui disent quelle classe d'écart à ces hypothèses le rend aveugle, et des témoins — modes de sabotage
documentés réimplémentés, mode conçu à l'écart par une personne et scellé (N-054) — qui mesurent si la prédiction se
vérifie ; **la machine ne conçoit aucune recette de contournement** (position tenue le 28 octobre, R-597 de session-depot :
le lanceur du bras d'attaque a été arrêté par un classifieur de sécurité ; aucune relance ni reformulation). Un chemin
mesuré, pas une promesse. *(Proposition de réécriture de la dernière phrase de la v5, qui parlait de « recherche automatique
des modes de sabotage » ; la v5 recommandait déjà de la réécrire ; l'en-tête étant commun au dossier du fonds, la décision
est de Lazar.)*

### Pièce 4 — lecture du lancement réel « (a) bis » (`lecture-lancement-reel-a-bis-v1.md`, `cc475e042c15…`, entière)

# Course de contrôle « (a) bis » (moteur réel, v7 version 5) — lecture dans les deux sens — v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 15:47 UTC (heure lue sur `date -u` : 15:47:21).
Source : branche `donnees/pole-lancement-reel-a-bis-v1`, commit `8533de8`, versée par session-depot (GO-2026-10-27-10,
orchestrateur v7 version 5 au commit `5ac9cb6`, empreintes `81bd0204…`, sans modification). Empreintes de la sortie
vérifiées : `EMPREINTES-v1.txt` (`d73c8cc3…`), aucun écart. Fichiers lus : `course/bilan.json` (`3467f21b…`),
`course/manifeste.json` (`1c2e75ab…`), `course/journal/generation-00.json` (`659a34ea…`) et `-01.json` (`8edc1e5f…`),
`RELAIS.jsonl` (`4407a2bf…`), les réponses des vérificateurs (`traces-verification/`), les leçons
(`traces-synthese/lecons.json`), les dossiers des agents. Lecture L1 à L6 fixée avant la course (message n° 112, point 3).

## Verdict

1. **Les six lectures fixées tiennent.** Aucune erreur de l'orchestrateur ; les deux témoins vrais jugés et promus, les
   deux témoins faux jugés et éliminés (« dents ») ; aucune vérification bloquée par la garde ; bac à sable actif ; aucun
   appel au-dessus de la réserve du relais. 136 appels, 5,89 USD, de 15:37:35 à 15:42:20 UTC.
2. **La condition (i) de la porte P3 est remplie** : la plomberie réelle passe sans incident. Restent (ii) des dents sur
   la banque v3 en simulation et (iii) mon devis.
3. **Réserve (R4)** : le résultat est propre parce que le monde est tautologique — la loi d'un témoin vrai est la loi du
   monde (log W de 74 et 84). Cela montre que la machine laisse passer un vrai, pas que le juge trouve un effet difficile.
   Deux témoins vrais seulement, même monde que (a).

## Les lectures fixées

| lecture | attendu | observé |
|---|---|---|
| L1 erreurs de l'orchestrateur | aucune | **0** (8 fiches à lancer en génération 0, dont une renvoyée hors budget ; 4 en génération 1) |
| L2 témoins vrais jugés, `etat_dents` | au moins un | **2 jugés, 2 promus** (S-V1 : log W 73,9 ; S-V4 : 84,2) ; « dents » |
| L3 témoins faux promus | aucun | **0** sur 2 jugés (S-F4, S-F1) |
| L4 vérifications bloquées par la garde | au plus une | **0** : aucune réponse de vérificateur ne parle de refus, de garde ou de blocage ; 11 rejeux confirmés sur 11 |
| L5 bac à sable | actif | **actif** (manifeste et bilan : « bwrap et socat présents ; bwrap s'exécute, réseau isolé ») |
| L6 relais | dépassements comptés | **0** appel au-dessus de la réserve de 0,40 (le plus cher : 0,245) ; Opus 5.5 79 appels, 2,09 USD ; Fable 5.1 57 appels, 3,80 USD |

## Dans l'autre sens : l'audit d'un résultat propre (R4)

- **Rien de l'orchestrateur dans les dossiers des agents** : aucun `reponse.txt`, `consigne.txt` ni `lecons.json` dans un
  dossier `experience/` ; les traces sont dans les dossiers voisins `traces-…`.
- **Issues conformes aux dépôts du noyau** : 11 fiches sur 11. Graines du noyau écrites après les évaluations (deux
  générations).
- **Vérifications** : chaque vérificateur dit avoir rejoué le code et reproduit exactement les tirages déclarés
  (empreintes d'ordre recalculées) ; aucun verdict de « confirmation par lecture ».
- **Règle e-BH** : m = 7 puis 4 ; les e-valeurs retenues sont arrêtées juste au-dessus de log(m/α) (5,03 à 5,14 pour un seuil
  de 4,94 ; 4,78 et 5,49 pour 4,38) : c'est la construction (arrêt au premier franchissement), pas une coïncidence.
- **Leçons de la mémoire** : elles parlent maintenant de science (« une intuition plausible ne suffit pas : il faut un
  effet assez fort… »), plus de fichiers.
- **Une fiche « hors budget »** en génération 0 (G0-F08) : le plafond de génération (7,5 USD, la moitié de 15) réserve le
  pire cas par fiche (1,00 + 0,50) ; la huitième n'a pas trouvé de place, elle a été rejouée en génération 1 et promue.
  Pas un défaut (le plafond tient) ; une inefficacité à connaître pour dimensionner (prévoir 1,5 USD de réservation par
  fiche et par vague).
- **La fille de la génération 1** (G0-F05 × G0-F07) est passée par la garde de redite cette fois et a été éliminée (log W
  −135 sous le nul des filles v2) ; deux filles de fin de course n'ont pas été jouées (nombre de générations atteint).

## Suite

- P3 : (ii) se jouera sur la banque v3 (couche 1 bis), en simulation, après la correction du défaut de témoins que
  signale le collisionneur (témoins vrais et nul informé ajustés sur les mêmes 40 épisodes : voir mon message n° 113).
- Le premier monde non tautologique avec de vrais agents reste la couche 1 (banque réelle) : devis après (ii).

### Pièce 5 — lecture de la couche 1 v7, v2 (`lecture-couche1-v7-v2.md`, `e2946dd65c57…`, entière)

# Couche 1 en simulation d'agents — v2 de la démonstration (banque v2, règle e-BH, témoins sans agents, signal « pas de dents ») — lecture v2 (exploratoire)

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1), écrit à partir de 14:18 UTC (heure lue sur
`date -u` : 14:18:28). Sur les « go » de Lazar de 15:11 heure de Paris. Même plan et même lecture L1 à L4 que la v1
(`lecture-couche1-v7-v1.md`, `e21f8611…`, gardée) ; ce qui change : banque **v2** (trait redondant retiré : 78 fiches
monotones au lieu de 104, 5 témoins vrais, 13 faux), **règle de multiplicité e-BH** dans les bras « informe », « aveugle »
et « urne », un bras **« par-fiche »** (garantie par fiche seule, pour mesurer ce que la multiplicité retire), **témoins
jugés par le noyau sans agents** (cinq vrais et cinq faux servis par génération), **signal « pas de dents »** écrit par
le noyau. Exécution 14:15:02 à 14:15:19 UTC (16,7 s) ; résumé scellé `resultats-v2/demo-couche1-v7-v2.json`.

## Verdict

1. **Sous la règle de multiplicité, rien n'est promu** dans les trois bras (informé, aveugle, urne) : la seule fiche qui
   passait le seuil par fiche (richesse 21 sur 53 épisodes, bras « par-fiche ») ne passe pas m / (α·k) avec m = 88 fiches
   jugées. C'est le comportement voulu : une promotion isolée parmi 88 n'est pas une découverte.
2. **Pas de dents, confirmé sur cinq témoins vrais** (tous éliminés, dans les quatre bras) ; le noyau l'écrit dans le
   journal (`qualite_generation.sans_dents = true`) et étiquette la promue du bras « par-fiche » `sans_dents`. Aucun
   témoin faux promu (cinq servis par bras).
3. **Témoins sans agents** : vingt témoins jugés sans un seul appel d'agent ; sur une banque, la mesure du taux de
   fausses promotions et de la puissance ne coûte plus rien.

## Chiffres

| bras | fiches jugées | promues | témoins faux promus | témoins vrais promus | sans dents | arrêt |
|---|---|---|---|---|---|---|
| informé + e-BH | 88 | 0 | 0 / 5 | 0 / 5 | oui | plus aucune fiche ne survit |
| aveugle + e-BH | 88 | 0 | 0 / 5 | 0 / 5 | oui | idem |
| urne + e-BH | 88 | 0 | 0 / 5 | 0 / 5 | oui | idem |
| par-fiche (aveugle, sans multiplicité) | 88 | 1 (étiquetée sans dents) | 0 / 5 | 0 / 5 | oui | rien de nouveau à tester |

## Lecture

L1 **tenu** (0 faux promu sur 20) ; L2 **tenu** ({} ⊂ {}) ; L3 **non tenu** (0 sur 5) → pas de dents ; L4 **tenu**.

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : les trois corrections de 15:11 font ce qu'elles doivent ; la multiplicité retire la promotion isolée ; le
  signal « pas de dents » dispense la lecture humaine de le constater.
- **Ne dit pas** : rien sur les juges de T0.5 (banque trop petite : la couche 1 bis, 288 instances, GO de Lazar à
  15:16, est faite pour cela) ; rien sur le pari à fraction (levier de puissance à coder).

### Pièce 6 — lecture des démonstrations du cycle v5 (`lecture-demonstration-cycle-v5-v1.md`, `60345b906006…`, entière)

# Démonstrations du cycle v5 — seuil par fiche, marchepieds sur le vivier de 60, redites — lecture v1 (exploratoire, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026, servie par Fable 5.1 au moment de la lecture), écrit à partir de 13:36 UTC
(heure lue sur `date -u` : 13:36:00). Sans préenregistrement (R-546) ; plan et lecture fixés dans l'en-tête de
`../orchestrateur-pole-v5/demonstrations/demo_cycle_v5.py` (`a457a8e2…`), poussé avant les exécutions (commit `0f4f297`,
orchestrateur v5, 130 essais « OK », empreintes `142a7c1f…`). Exécutions lancées à 12:58 UTC, finies à 13:09 (A, 654 s),
13:17 (C, 463 s) et 13:25 UTC (B, 1 608 s) ; graines 1 à 20 ; résumés dans `resultats-v1/` (empreintes compagnons ; les
archives des courses restent dans le conteneur : elles se refont par le script, à graines égales).

## Verdict

1. **Le seuil de signature par fiche corrige la réserve de v4 (A)** : avec deux traits, les vraies filles neuves refusées
   à tort par la garde prédictive tombent de 31 et 39 (v4) à **4 et 5** ; avec quatre traits, 6 et 5 (inchangé). Les parts de
   vraies filles promues restent celles de v4 : 0,56 et **0,97** (2 traits, 120 et 500 tirages), 0,92 et **1,00** (4 traits).
   Aucune fille triviale promue (0 sur 181), aucune fausse découverte.
2. **Les marchepieds servent quand le vivier est assez grand (B)** : sur 60 fiches à quatre traits, six paires par
   génération, cinq générations, le tirage avec marchepieds promeut **282 vraies filles contre 212** (+33 %) dans le monde
   à lignées fécondes, et **236 contre 245** (−4 %, dans la bande des 10 %) dans le monde plat ; aucune fausse promue, aucun
   témoin vrai éliminé (200 témoins par bras). Les deux faces de la lecture tiennent : l'avantage apparaît là où il doit,
   et seulement là. C'est le mécanisme construit pour cela qui est vérifié, pas une découverte sur le monde.
3. **La mémoire empêche les découvertes en double (C)** : héritage, refus et « rien » : **0** double sur 31 redites
   proposées ; sans mémoire : **11** doubles sur 40. Aucune fausse parmi les redites, dans aucun bras (toujours sans dents
   pour C2).

## Chiffres (sommes sur 20 courses)

**A — puissance des filles** (tirage stratifié, `p_triviale` 0,4 ; v4 entre parenthèses)

| bras | vraies filles promues / testées | triviales promues | refusées par la garde | témoins vrais éliminés |
|---|---|---|---|---|
| 2 traits, 120 tirages | 14 / 25 (0,56) | 0 / 36 | **4** (31) | 10 / 52 |
| 2 traits, 500 tirages | 29 / 30 (0,97) | 0 / 48 | **5** (39) | 10 / 60 |
| 4 traits, 120 tirages | 22 / 24 (0,92) | 0 / 48 | 6 (6) | 0 / 57 |
| 4 traits, 500 tirages | **23 / 23 (1,00)** | 0 / 49 | 5 (5) | 0 / 57 |

Les témoins vrais éliminés à deux traits (10 sur 52 et 60) sont ceux des fiches sans parents à 120 tirages (le plan des
fiches de départ ne change pas avec `taille_plan_filles`) : même constat qu'en v4 (9 sur 49 et 55), lié à la pauvreté du
monde à deux traits, pas à la mémoire.

**B — marchepieds** (vivier de 60 fiches, 4 traits, 500 tirages, six paires par génération, cinq générations)

| monde | stratifié : vraies filles promues / testées | avec marchepieds | fausses promues | refusées par la garde |
|---|---|---|---|---|
| lignées fécondes | 212 / 215 | **282 / 287** | 0 | 9 ; 11 |
| plat | 245 / 246 | 236 / 241 | 0 | 7 ; 8 |

**C — redites** (2 traits, 120 tirages, `p_redite` 0,5, six générations)

| politique | redites proposées | refusées | testées | découvertes en double | fausses parmi les redites |
|---|---|---|---|---|---|
| héritage | 31 | 20 | 11 | **0** | 0 |
| refus | 31 | 31 | 0 | 0 | 0 |
| rien (garde des survivantes gardée) | 31 | 20 | 11 | 0 | 0 |
| sans mémoire | 40 | 0 | 40 | **11** | 0 |

## Lecture (fixée avant l'exécution)

- A1 aucune triviale promue : **tenu** ; A2 la part monte avec les tirages et les traits : **tenu** (0,56 → 0,97 ; 0,92 →
  1,00) ; A3 aucune fausse découverte : **tenu** ; mesure ajoutée (refusées par la garde à deux traits « de l'ordre de
  quelques unités ») : **tenu** (4 et 5).
- B1 marchepieds supérieurs dans le monde fécond : **tenu** (282 contre 212) ; B2 pas d'avantage dans le monde plat (au
  plus 10 % d'écart) : **tenu** (236 contre 245, −4 %) ; B3 aucune fausse découverte : **tenu**.
- C1 héritage et refus sans double, sans mémoire au moins un : **tenu** (0, 0, 11) ; C2 fausses parmi les redites,
  héritage au plus sans mémoire : **tenu** (0 et 0, sans dents : le monde de démonstration ne produit pas de redites
  d'idées fausses).

## Ce que cela dit, et ce que cela ne dit pas (R4)

- **Dit** : les trois réserves de v4 sont levées dans le monde simulé — le seuil par fiche tient la fausse fusion sans
  perdre de puissance ; les marchepieds exploitent les lignées fécondes quand il y a assez de paires parmi lesquelles
  choisir ; la mémoire évite le double comptage.
- **Trop beau ?** B tient exactement comme prévu parce que le monde fécond est construit pour cela (une fille d'une fille
  est vraie avec probabilité 0,85, sinon 0,35) et que les marchepieds choisissent précisément les paires qui ont une fille
  survivante : c'est une vérification de mécanisme, dont la valeur dépend de l'existence de lignées fécondes dans un
  monde réel, que rien ici ne mesure. Les parts à 1,00 (4 traits, 500 tirages) répètent v4 : puissance saturée dans un
  monde où les lois vraies sont exactement celles des fiches (vérité binaire ; limite relevée par la contre-lecture
  d'aptitude du 27 octobre, `../premier-lancement-reel/contre-lecture-aptitude-v1/`).
- **Ne dit pas** : que la loi de référence du seuil (softmax de force 1,5) convienne à de vraies fiches ; que les
  marchepieds servent sur un monde réel ; que la mémoire reconnaisse deux hypothèses de contrôle qui partagent le
  vocabulaire (garde textuelle) ou deux recettes d'attaque qui évadent pareil (signature sur la loi, pas sur la recette).
- **Suite** : v6 (premier lancement réel préparé sans dépense : monde tenu par le noyau, relais de clé réel, répétition
  générale, dépôt unique par engagement) ; v7 (monde du programme sur banque en cache, nul informé, rôle proposeur,
  moissonneur), selon la contre-lecture d'aptitude.

### Pièce 7 — pont fiche → loi, conception v1 (`conception-pont-fiche-loi-v1.md`, `5161e199e15d…`, entière, règle 2 appliquée au § h)

# Pont « fiche de course → fiche-loi du pôle » (prise idéation) — conception v1

Lignée conv-audit, rédacteur neuf (Opus), 1er novembre 2026 ; écrit à partir du relevé `date -u` de **09:45:13 UTC**.
Décision de Lazar consignée en **R-1037** (registre de la branche conv-audit, ligne 1001) : l'objectif de la course 2 devient
« produire des idées inédites, originales et qui survivent aux tests, expériences, tests de mort et pôle » ; « prévu mais pas
construit : fais-le ». Le pont était **conçu, pas construit** (`integration-proposeurs-ia-v1.md` § 2, l. 95-98 ; dossier
factuel § 1.1 et § 9.4 C). Régime exploratoire : rien n'est lancé, aucun appel de modèle, rien lu sous `donnees/`, dossier
`bras-attaque-v1/` non ouvert, niveau méthode seulement. Pièces lues et empreintes : `LISEZMOI-pont-v1.md`.

## Verdict

1. Le pont est **conçu et codé** (`pont_v1.py`, bibliothèque standard, appels de modèle injectés) : une fiche de course entre,
   il en sort **une fiche-loi au format du pôle** (loi par instance ou contraste apparié) ou **un renvoi motivé** par un code
   d'une liste fermée. 82 essais réussis, dont 5 contre le **vrai code de l'orchestrateur v56** (garde de forme du noyau,
   juge par pari, engagement apparié) ; 25 mutations sur 25 tuées.
2. Ce que le pont ne peut pas changer : **aujourd'hui, presque aucune fiche ne sera testable sur une banque existante**. Les
   seules banques d'épisodes du pôle sont celles de T0.5 (notes de juges sur des tâches de recherche, 13 moniteurs), leur
   épreuve est **entièrement lue** (couche 1 bis : « les 288 épisodes sont tous lus »), et la banque de scores avec sabotage
   (couche 2) n'existe pas. La plupart des fiches traduisibles sortiront en **« couche 3 »** : une loi gelée maintenant, qui
   attend ses épisodes. Je l'écris d'emblée pour qu'on ne lise pas ce constat comme un échec du pont.
3. Cinq décisions pour toi (section h) ; une seule est un nœud : le **premier essai** sur 10 fiches de la course 1
   (dépense ≈ 1 à 4 dollars, fiches tirées et servies par session-depot, jamais lues par conv-audit).

---

## (a) Les deux objets

### a.1 La fiche de course

Rangée par le noyau de la course comme `{"ident", "contenu", "empreinte", "meta"}` (`pole/fiches_v53.py`) ; **seul `contenu`
est servi** (vue anonyme) ; `meta` (case, fournisseur, passe, origine) ne sort jamais. Deux formats de contenu existent.

| course | champs du contenu | source |
|---|---|---|
| **2** (texte I, « question défense ») | axe ; hypothèse ; **prédiction chiffrée et signée** (métrique de la liste fermée M, valeur, unité de lecture) ; livrables de l'axe ; données (liste D) ; coût (processeur, carte, dollars) ; antériorités (≤ 5) ; source d'avantage (liste L) ou élément manquant ; **critère de mort** ; vis-à-vis (lien angle ↔ faille) ; marque SUPPOSÉ. 3 000 à 8 000 caractères. Noms exacts des clés JSON : injectés par la configuration (`champs_fiche`), non fixés dans le code | `question-course-2-defense-fusion-v5.md` l. 44 ; dossier factuel § 3.2 |
| **1** (gabarit d'idéation) | nom ; type (question, approche) ; énoncé ; **loi_predictive** {espace_instances, prediction, signe, metrique} — en **texte libre** ; perte_traduction ; questions_servies ; avantage ; originalité ; demande à l'organisme ; coût ; piège ; « cosmétique si » ; antériorité | `pole/ideation_v2.py` l. 401-419. **SUPPOSÉ** être le format de la course 1 (version de l'orchestrateur de la course 1 non vérifiée ici) |

Les deux formats portent déjà « une prédiction chiffrée » ; aucun ne porte une **loi exécutable** : la course 1 avait même un
champ « ce que l'idée perd en devenant loi prédictive », jamais exploité.

### a.2 La fiche-loi du pôle

Le pôle juge deux sortes d'engagement (orchestrateur v56).

**(i) Loi par instance** (`pole/fiche.py`, `pole/proposeur.py`, `pole/selection_pari.py`). Le proposeur rend
`{enonce, strategie, moniteur, loi_predictive, domaines, operateurs}` ; **la garde de forme du noyau**
(`proposeur.valider_proposition`) refuse tout champ hors gabarit, une stratégie hors catalogue, un moniteur inconnu de la
banque, un type de loi hors {softmax, par sous-population, si/sinon, mélange, fixe}, un poids hors |w| ≤ 4 (biais ≤ 8), une
dimension fausse, un énoncé de plus de 400 caractères ; puis le noyau **complète seul** la métrique (« richesse W contre la
bibliothèque »), le nul, le seuil 1/α, la sévérité α, le protocole, et l'espace d'instances (banque, moniteur, nombre
d'issues, dimension, sous-populations). La loi donne, pour chaque épisode, une probabilité de chacune des K issues d'un
moniteur sachant ses traits z et sa sous-population g.

**(ii) Contraste apparié** (`pole/pari_apparie.py`, `pole/engagement_apparie.py`, `pole/monde_banque_scores.py`). Pour les
affirmations globales du type « la statistique A bat le comparateur B » (forme de la porte G1) : contrastes v(t) = a₀ + Σ a_c·r_c(t)
sur des parts d'épisodes sabotés alertés par cellule (moniteur × condition), coefficients soumis à la **règle double**
(v ∈ [−1 ; 1]), point de fonctionnement τ, **garde** δ sur l'excès de fausses alertes, seuils calculés sur les honnêtes du
calibrage, lecture de la partie d'épreuve dans un ordre secret.

### a.3 Ce que le juge figé exige (« la balance », statistique, hors des agents)

| exigence | où dans le code v56 | ce que le pont doit fournir |
|---|---|---|
| prédiction chiffrée **sur des épisodes** | `selection_pari.proba` ; `pari_apparie.contraste` | une loi par instance ou un contraste, pas un énoncé |
| **partie de développement** (traits et issues visibles, pour l'affinage) | `MondeBanque.donnees_developpement` | rien : l'affinage est le travail de l'expérimentateur du pôle, après le pont |
| **partie d'épreuve jamais vue**, issues lues après le gel, ordre secret tiré par le noyau | `MondeBanque.reservoir`, `mesures` ; `ordre_execution` | aucune lecture de l'épreuve, ni par le traducteur ni par le pont (garde G3) |
| **nul informé** : prédicteur « connu » du moniteur, ajusté sur la partie de calibrage, plus les prédicteurs aveugles (marginale, uniforme, moyennes glissantes, urne) et l'archive des survivantes | `MondeBanque.membres_informes` ; `cycle.membres_de_l_archive` | une loi qui doit **prédire plus que le connu** : le pont la construit comme « connu + effet déclaré » |
| **témoins plantés** vrais et faux à chaque génération | `exemples/construire_banque_t05_v3.py` (vrais confirmés sur une moitié du développement ; faux par permutation dans la tâche) | rien de neuf côté pôle ; le pont a **ses propres témoins** (section g) |
| seuil m/α (règle de fausses découvertes e-BH entre fiches) | `pari_apparie.ebh_pondere`, cycle | m connu de l'orchestrateur ; le pont l'utilise pour la puissance |

### a.4 Ce que le pôle sait et ne sait pas faire aujourd'hui

- **Sait** : la plomberie réelle passe (lancement « (a) bis », 27 octobre : 2 témoins vrais promus, 2 faux éliminés, 11 rejeux
  sur 11, 5,89 dollars) — mais dans un monde **tautologique** (la loi du témoin vrai est la loi du monde) ; il a des dents
  dans un monde planté (8 sur 8 témoins vrais promus, 0 sur 8 faux, démonstration couche 1 proposeur) ; sur la banque de la
  couche 1 bis il promeut des témoins plantés jusqu'à la **force 0,5** (144 épisodes d'épreuve par fiche) ; la génération 0 a éliminé 10
  affirmations sur 18 par calcul, pour 0 dollar.
- **Ne sait pas encore** : rien promu sur les **13 moniteurs réels** de T0.5 (pas de dents à 120 épisodes : 0 témoin vrai sur
  20 ; à 288 épisodes, meilleure richesse 2,28 pour un seuil de 3,0) ; l'**épreuve de T0.5 est entièrement lue** et aucune
  épreuve disjointe n'existe ; la **banque de scores avec sabotage** (couche 2) et la **couche 3** (épisodes ou moniteurs neufs
  à la demande) ne sont pas construites ; l'avantage de l'exploration (E2) n'est pas démontré.
- Conséquence pour le pont : la sortie 1 sera rare tant qu'une épreuve fraîche n'existe pas. Ordre de grandeur, calculé
  par le module (approximation dite en d) : sur un moniteur à deux issues équilibrées et un trait centré réduit, une loi de
  log-rapport de cotes 0,6 par écart type demande environ **150 épisodes d'épreuve** (seuil 1/α, α = 0,05) et environ 300 si
  17 fiches sont jugées ensemble ; un effet de 0,3 en demande environ 560.

## (b) La traduction, champ par champ

### b.1 Le principe : « connu + effet », compilé par le programme

Le traducteur n'écrit **jamais une loi**. Il écrit une **spécification courte** (forme, cible, objets, sens, effet chiffré et
**cité**), et le programme la compile :

- **loi par instance** = prédicteur connu du moniteur (public dans le pôle, ajusté sur le calibrage, jamais sur l'épreuve)
  **plus** l'effet déclaré par la fiche, sur le trait et l'issue nommés. La fiche-loi affirme donc exactement **ce que la fiche
  ajoute au connu** ; une fiche qui ne fait que redire le connu ne bat pas son nul, par construction du juge.
- **contraste apparié** = coefficients {meilleure : +1, comparateur : −1}, τ et δ cités (constantes de la porte G1 permises :
  τ = 0,01, δ = 0,05), garde sur l'excès de fausses alertes de la meilleure.

Ce choix tient le traducteur **hors de toute donnée** (ni développement, ni épreuve, ni connu) et rend la traduction
vérifiable par un programme. L'affinage sur le développement reste au pôle (l'expérimentateur, avant le second gel).

### b.2 Table de correspondance

| champ de la fiche de course | ce que le pont en fait | champ de la fiche-loi |
|---|---|---|
| prédiction chiffrée et signée (course 2) ; `loi_predictive.prediction` et `.signe` (course 1) | **sens** et **effet** (valeur citée par son chemin, ou opération fermée sur des valeurs citées : différence, rapport, logarithme du rapport, différence de logits) | `loi_predictive` (poids ou biais ajoutés au connu) ; ou `contrastes` |
| métrique de M ; `loi_predictive.metrique` | **cible** : (banque, moniteur, issue visée) ou (banque de scores, cellules, τ) | `moniteur`, `espace_instances` ; ou `contrastes`, `tau` |
| données (D) ; `loi_predictive.espace_instances` | banque existante du catalogue, ou **objet à construire désigné par le chemin du champ qui le nomme** | `espace_instances.banque` ; sinon demande de couche 3 |
| hypothèse ; énoncé | rien directement : l'énoncé de la fiche-loi est **rendu par le programme** depuis la spécification (moins de texte libre, moins de canaux) | `enonce` (≤ 400 caractères) |
| critère de mort | **non traduit** : c'est l'objet des tests de mort ; le seuil du juge est 1/α (ou m/α), pas celui de la fiche — perte consignée | — |
| perte de traduction (course 1) | lue par le traducteur comme matériau | `perte_traduction` (écrite par le traducteur, toujours exigée) |
| axe, livrables, coût, antériorités, source d'avantage, vis-à-vis, SUPPOSÉ, piège, « cosmétique si », questions servies, originalité | **non traduits** : ils relèvent des juges de la course, de l'antériorité, du devis | — |
| — | ajoutés par le pont : `source` = « pont:<empreinte de la fiche> », `base` (« connu:<moniteur> »), empreinte de la spécification | `source`, `base`, `empreinte_specification` |
| — | complétés par le noyau, inchangés : métrique, nul, seuil, sévérité, protocole, coût borné | idem |

Règle de fer : **le traducteur n'invente aucun chiffre**. Chaque nombre de la spécification doit figurer dans le champ cité
de la fiche (virgule ou point, « 45 % » vaut aussi 0,45), ou être une constante nommée du programme, ou être recalculé par le
programme à partir de nombres cités. Une fiche, **une loi au plus** (choix pris seul pour la v1 ; la multiplicité e-BH
compterait chaque loi).

### b.3 Ce qui ne se traduit pas : les trois sorties

Le **programme** décide la sortie (jamais le traducteur seul) :

1. **« Loi testable sur la banque existante »** — la cible existe au catalogue (banque, moniteur ou cellules, traits), l'épreuve
   est fraîche (ou sa réutilisation déclarée, décision D-P4), l'affirmation n'a pas déjà été lue sur cette épreuve, et la
   puissance sous la vérité de la loi suffit. Sortie : une proposition qui passe la garde du noyau, prête pour une génération
   du pôle.
2. **« Loi testable seulement avec des épisodes neufs » (couche 3)** — la loi est bien définie, mais il manque : un moniteur ou
   une cellule (une statistique nouvelle à calculer sur des épisodes existants : étage sur carte graphique, devis et GO par
   fiche) ; une banque (population nouvelle) ; une épreuve fraîche ; ou des épisodes (effectif requis calculé). Sortie : la
   **spécification gelée maintenant** (empreinte), une **demande au niveau méthode** (ce qui manque, effectif requis, parties
   fixées par une instance tierce), et la loi compilée plus tard sur le calibrage de la banque future. **Jamais un mode de
   sabotage nouveau** : épisodes honnêtes, modes connus scellés tenus par session-depot (voie c), ou statistique nouvelle.
3. **« Non testable, renvoyée avec la raison »** — code fermé, en deux familles :

| code | surnom | famille | sens |
|---|---|---|---|
| N1 | « rien à mesurer » | fiche | méthode, outil ou protocole sans issue mesurable sur des épisodes |
| N2 | « pas de chiffre » | fiche | prédiction non chiffrée ou sans signe |
| N3 | « affaire de preuve » | fiche | preuve (Lean) ou simulation hors banque : renvoyée au pôle théorie |
| N4 | « mode nouveau » | fiche | exige des épisodes d'un mode adversarial nouveau : hors du pôle (adversaire scellé, revue externe) |
| N5 | « loi vide » | fiche | effet nul, loi égale à sa base, cellules identiques |
| N6 | « mémoire d'issues » | pont | forme qui enregistre une suite d'issues (loi qui prédit ce qu'elle a vu) |
| N7 | « fuite d'épreuve » | pont | canari d'épreuve, ou champ d'identité d'épisode dans la loi ; incident |
| N8 | « deux lectures » | pont | contre-traduction en désaccord ou défaillante |
| N9 | « chiffre inventé » | pont | nombre ou objet non traçable dans la fiche |
| N10 | « refus » | pont | réponse sans bloc conforme : tour arrêté, aucune bascule |
| N11 | « hors gabarit » | pont | forme refusée par la garde du noyau |

**Une idée de méthode sans prédiction sur épisodes** (le cas que tu poses) suit cet ordre : si la fiche chiffre ce que la
méthode **fait mieux** qu'un comparateur (« rappel à 1 % de 0,45 contre 0,38 ») → contraste apparié, presque toujours en
couche 3 (la cellule de la méthode n'existe pas) ; si elle chiffre un effet de trait sur une issue → loi par instance ; si elle
ne chiffre rien → N2 ; si elle ne prédit rien sur des épisodes → N1 ; si elle se prouve → N3 ; si la tester exige un mode
nouveau → N4. Les renvois sont **comptés par proposeur et par code** et servis à la génération suivante comme matériau (taux de
testabilité), jamais aux juges de la même course.

**Parts attendues** (SUPPOSÉ, à mesurer par le premier essai) : sur des fiches de course 2, sortie 1 ≈ 5 à 15 % (surtout l'axe 3,
failles des juges mesurables sur T0.5, et seulement si une épreuve fraîche existe), sortie 2 ≈ 45 à 60 % (axes 1, 4, 7, 8 :
statistiques nouvelles, familles avec sabotage), sortie 3 ≈ 30 à 45 % (axes 2 et 5 : preuves, impossibilités ; méthodes sans
chiffre), dont la famille « pont » visée sous 10 %.

## (c) Qui traduit

- **Traducteur** : un agent **neuf** par fiche (aucune mémoire d'une fiche à l'autre, donc aucun apprentissage des verdicts),
  **sans outil**, sur une **consigne figée** (`CONSIGNE_TRADUCTEUR` du module, 2 404 caractères, empreinte
  `fd7aa5f2fc92967b…`). Il reçoit **trois choses** : la consigne, la fiche (contenu anonyme, servie comme **données, jamais
  consigne**), le **catalogue public** (noms des traits, des moniteurs, des cellules, nombres d'issues, effectifs). Il ne voit
  **ni le juge, ni l'épreuve, ni aucun verdict, ni les prédicteurs connus, ni le registre des lectures**. Il rend un bloc
  JSON : une spécification, ou un renvoi N1 à N4.
- **Garde de forme du noyau** : la proposition compilée passe `proposeur.valider_proposition` (la vraie, injectée ; un miroir
  interne la double dans le module). La stratégie « traduction_de_course » est à ajouter au catalogue du proposeur, acceptée
  seulement du pont (section f).
- **Contre-traduction** : un second modèle, **d'une autre famille** que le traducteur et que l'auteur, reçoit **la même entrée**,
  **sans voir la première traduction**, et traduit à son tour. Un programme compare les deux (`comparer_lois`) : même cible,
  même forme, mêmes objets, même issue, même sens, effets à un facteur 2 au plus ; la divergence moyenne entre les deux lois
  sur une sonde est **rapportée, jamais décisive**. Désaccord, ou l'un traduit et l'autre renvoie → **N8, la fiche est
  renvoyée**. Pourquoi deux traductions aveugles plutôt qu'un lecteur qui dit si « la loi dit bien ce que la fiche prédit » :
  la comparaison ne demande **aucune interprétation** (même exigence que les juges de la course) et mesure l'ambiguïté de la
  fiche. Angle mort dit : deux traducteurs peuvent partager la même lecture fausse ; les témoins « aller-retour » du premier
  essai mesurent cela.
- **Affectation croisée** (trois familles, une par rôle) : auteur Google (Argon) → traducteur Opus 5.5, contre-traducteur
  Kimi ; auteur Moonshot (Kimi) → Opus 5.5, Argon ; auteur Anthropic (Fable, course 1) → Kimi, Argon. Une affectation qui
  répète une famille est refusée avant tout appel.
- **Refus** : un refus arrête le tour pour cette fiche (règle R-750 : une seule reformulation plus étroite permise, jamais la
  même rhabillée) ; N10, aucune bascule vers un autre modèle sans ton mot.
- **Quarantaine** : seules les fiches « niveau méthode » sorties de l'aiguilleur entrent ; une fiche « trop concrète » reste
  scellée au bras d'attaque et n'atteint jamais le pont (règle R-575 du registre conv-audit : le concret est scellé chez
  session-depot). Le traducteur ne décrit jamais un mode ; N4 renvoie hors du pôle.

## (d) Les gardes R5 (« garde éprouvée » : chacune essayée sur un cas sain et sur un artefact)

| garde | ce qu'elle attrape | cas sain (essai) | cas artefact (essai) |
|---|---|---|---|
| **G1 rétrodiction** (« loi qui prédit ce qu'elle a vu ») | l'affirmation (cible, moniteur, traits ; ou cellules) figure au registre des lectures de cette épreuve → sortie 2, épreuve fraîche, drapeau ; forme qui enregistre une suite d'issues (déterministe, calendrier, sans remise, moyenne glissante, dérive, transformée) → N6 ; épreuve déjà lue par d'autres fiches → sortie 2 (ou réutilisation déclarée, D-P4) | lecture d'un autre trait au registre : sortie 1 | même trait lu dans l'autre sens : sortie 2 ; contraste déjà lu ; forme « deterministe » : N6 sans second appel ; loi « calendrier » refusée par la garde de forme (N6) |
| **G2 loi vide** | effet nul ; loi égale à sa base sur la sonde (divergence ≤ 10⁻⁶ nat) ; cellules identiques | loi « connu + 0,8 » : divergence > seuil | effet 0,45 − 0,45 ; même cible sans loi numérique (objet à construire) ; loi égale au connu ; cellule A = cellule B : N5 |
| **G3 lecture de l'épreuve** | clé d'épreuve ou de juge dans le catalogue servi ou l'enveloppe ; métadonnée de fiche ; consigne altérée ; canari d'épreuve dans l'entrée → **arrêt avant tout appel** ; canari dans une réponse → N7 et incident ; trait d'identité d'épisode, condition sur un champ d'épisode → N7 | canari fourni, absent partout : sortie 1, deux appels | « issues » dans le catalogue, canari dans la fiche, « ident » dans la fiche : 0 appel ; canari dans la réponse du traducteur ou du contre-traducteur ; trait « identifiant » ; condition « identifiant » |
| **traçabilité** | nombre absent de la source, source absente, valeur mal recalculée, opération hors liste, constante du programme inconnue ou falsifiée, objet à construire sans source | « 0,8 » cité ; « 0,60 − 0,20 » recalculé | 0,9 inventé ; chemin inexistant ; 0,45 − 0,38 annoncé 0,1 ; « exponentielle » ; δ = 0,2 prétendu constante de G1 : N9 |
| **contre-traduction** | désaccord de cible, forme, objet, issue, sens, effet (> ×2), genre ; loi contre renvoi ; contre-traducteur défaillant | lois identiques ; effets 0,8 et 0,45 | sens inversé, autre trait, autre issue, autre moniteur, interaction au lieu de monotone, effet ÷ 4 : N8 |
| **affectation** | traducteur de la famille de l'auteur ; contre-traducteur d'une famille déjà présente ; famille inconnue | les trois affectations recommandées | cinq affectations fautives ; aucun appel |
| **refus et format** | pas de bloc, sortie hors liste, code réservé (N5) donné par le traducteur, sens hors liste, perte de traduction vide → N10, **pas de second appel** | bloc précédé d'un autre bloc JSON | cinq réponses fautives |
| **forme du noyau** | moniteur inconnu, stratégie autre, énoncé > 400, liste vide, poids > 4, dimension fausse, champ hors gabarit, loi brute écrite par le traducteur, issue hors moniteur, sous-population hors liste → N11 ; refus de la **vraie** garde injectée → N11 | proposition compilée acceptée (miroir et vraie garde v56) | onze artefacts ; refus de la garde injectée ; vraie garde v56 sans la stratégie au catalogue : N11 |
| **puissance** | effectif d'épreuve insuffisant sous la vérité de la loi → sortie 2 avec effectif requis | 2 000 épisodes, effet 0,8 : sortie 1 | 40 épisodes : sortie 2 ; contraste à écart 0,07 sur 600 unités : sortie 2 |

Banc de mutations (hors dépôt, dans un dossier temporaire) : **25 mutations, 25 tuées** — chaque garde neutralisée fait échouer
au moins un essai ; un premier passage avait laissé **une survivante** (« effet nul accepté » : le contrôle de divergence la
couvrait en profondeur), corrigée par un essai sur une cible sans loi numérique. Audit de propreté (R4, « trop beau =
suspect ») : 25 sur 25 ne prouve pas l'absence de garde manquante ; le banc ne dit rien des gardes que je n'ai pas pensées.

**Limites des gardes** : elles voient la forme et la provenance, jamais la vérité de la fiche ; le canari n'attrape qu'une
copie littérale, pas une fuite paraphrasée ; G1 ne vaut que si le registre des lectures est complet (à tenir par le noyau,
depuis la mémoire du pôle) ; la puissance est une **approximation** (lois par instance : divergence moyenne à la seule base,
**optimiste** ; contrastes : variance bornée par 1, **pessimiste**).

## (e) Coût et ordre de passage

- **Par fiche** : 2 appels (1 seul si le traducteur faillit, refuse ou fuit) ; entrée ≈ 4 000 à 6 000 jetons (fiche 3 000 à
  8 000 caractères, consigne 2 404, catalogue) ; sortie ≤ 1 000 jetons. Prix **SUPPOSÉ**, ordre de grandeur tiré des relevés du
  lancement (a) bis (appels d'agents, plus longs) : Opus 5.5 ≈ 0,026 dollar par appel (2,09 / 79), Fable 5.1 ≈ 0,067 (3,80 / 57) ;
  soit **≈ 0,05 à 0,15 dollar par fiche**, 1 à 3 minutes, parallélisable. Côté noyau : calcul sur processeur négligeable (82
  essais en moins d'une demi-seconde).
- **Pour la course 2** : seules les fiches passées par les juges et l'antériorité entrent ; à 30 à 60 fiches : **≈ 2 à 9
  dollars**, dans le plafond de 160 dollars s'il reste de la marge (sinon devis à part).
- **En aval, hors du pont** : une fiche en sortie 1 coûte un passage du pôle (≈ 0,5 dollar par fiche au lancement (a) bis :
  expérimentateur, vérificateur, juge) ; une sortie 2 coûte un devis (carte graphique par fiche, banque nouvelle).
- **Ordre** : après les juges de la course et la vérification d'antériorité (une antériorité « non trouvée » n'est jamais
  « vierge », règle R8 « pas de faux trou »), **en parallèle des tests de mort, cloisonnés** : aucun des deux ne voit le
  résultat de l'autre avant que les deux soient scellés, et la sélection des fiches à traduire ne dépend d'aucun verdict
  (règle N-053, « pare-feu » : aucun score de juge dans une sélection). Le noyau vérifie que la tranche exploratoire des tests
  de mort est **disjointe** de l'épreuve du pôle (par identifiants). Variantes : décision D-P3.

## (f) Ce qui change dans l'orchestrateur v56, et ce qui ne change pas

**Couche v57 neuve** (R12 : aucun fichier v56 modifié) :

| pièce | rôle | interface |
|---|---|---|
| `pole/pont_v1.py` | ce module | `traduire_fiche(fiche, *, catalogue, noyau, traduire, contre_traduire, affectation, canaris, alpha, m, marge, politique_epreuve, garde_forme_noyau) -> dict` ; `comparer_lois(a, b, sonde)` |
| `pole/proposeur_v57.py` | accepte la stratégie « traduction_de_course » **seulement** d'une proposition du pont (comme `references=True` pour les références) | `valider_proposition_v57(p, monde, alpha, ident, modele, pont=True)` |
| `pole/etage_pont_v57.py` | l'étage : lit le classement et les fiches validées (même format que `etage_entre_generations_v53.preparer_generation`), sert chaque fiche (vue servie + garde A4 des étiquettes de `fiches_v54`), appelle les rôles « traducteur » et « contre_traducteur » par les adaptateurs v56 (texte → texte), scelle `noyau/pont/<ident>/{entree.txt, reponse-traducteur.txt, reponse-contre-traducteur.txt, resultat.json}` et un manifeste | sorties : fiches (`Fiche`) pour une génération du pôle ; demandes de couche 3 pour session-depot ; renvois comptés pour la génération suivante |
| `pole/catalogue_public_v57.py` | catalogue servi (depuis `MondeBanque.description_publique` et `MondeBanqueScores.description_publique`) et état du noyau, **jamais servi** : connus (`predicteurs_connus_publics`), registre des lectures (mémoire du pôle : survivantes et éliminées par épreuve), épreuves fraîches (journal), sondes (traits du développement), canaris (dérivés des identifiants d'épreuve) | dictionnaires du module |
| `configuration_v57`, `budget` | rôles et plafonds d'étape « traduction », « contre_traduction » (plafond transmis et accusé comme en v56) ; `pont.modeles`, `pont.consigne_sha256`, `pont.politique_epreuve`, `pont.marge` | validés au départ, aucun défaut |
| `gardes_e0_v57.py` | lignes R5 du pont jouées à l'étape de départ | — |

**Inchangé** : le juge figé (`selection_pari`, `pari_apparie`, `engagement_apparie`, `nul_filles_v2`), les mondes sur banque,
la mémoire, la recombinaison, le cycle, les tests de mort, l'aiguilleur, les juges de la course, le bisociateur, les règles de
budget. Une fiche du pont porte `source = "pont:<empreinte>"` : `Fiche.famille_source()` la range dans la famille « pont »
pour la calibration, sans changement de code.

## (g) Préenregistrement court du premier essai (brouillon, à sceller après contre-lecture R2, « œil neuf »)

- **Question** : le pont classe-t-il des fiches réelles de façon stable et attrape-t-il ses témoins ? (Pas : « les lois
  traduites sont-elles vraies ? » — il faudrait une épreuve fraîche.)
- **Prise des 10 fiches sans que conv-audit les lise** : session-depot (qui tient `donnees/`) part des fiches **éligibles** de
  la course 1, tentative 2 (27 sur 29), **une par idée distincte** (17 idées distinctes sur 29 fiches, 12 paires de doublons ;
  R-811 et R-820 du registre de session-depot) ; tire 10 idées par `numpy.random.SeedSequence` (R9) dont l'entropie = empreinte de ce préenregistrement
  scellé **et** une valeur de session-depot engagée par son empreinte **avant** le scellement (personne ne choisit) ; 5 de Fable
  et 5 d'Argon si possible, sinon au prorata, déclaré ; copie le **contenu seul** (vue anonyme, garde A4) dans un dossier
  scellé. conv-audit ne lit ni les fiches, ni les réponses, ni les fiches-lois : il reçoit la lecture agrégée.
- **Témoins du pont (6)**, écrits par un metteur en forme tiers qui ne voit pas la consigne (Sonnet 5.5, comme pour D-f), mêlés
  anonymes : T1 et T2 « aller-retour » (fiches écrites depuis une spécification connue sur le catalogue réel) ; T3 « vide »
  (effet nul) ; T4 « méthode sans mesure » ; T5 « théorème » ; T6 « sans chiffre ». Vérité : T1, T2 → leur signature ; T3 → N5 ;
  T4 → N1 ; T5 → N3 ; T6 → N2 ou N9.
- **Catalogue** : descriptions publiques des banques T0.5 existantes, épreuves marquées « lues » (c'est le cas) ; politique
  « fraîche seulement ». Une fiche classée « banque existante, épreuve fraîche requise » est comptée à part (« sortie 1
  différée »).
- **Prédictions** (signées, chiffrées) sur les 10 fiches : sortie 1 différée **1** (intervalle 0 à 3) ; sortie 2 **4** (2 à 6) ;
  sortie 3 **5** (3 à 7), dont famille « pont » **≤ 2** ; accord des deux traductions parmi les fiches traduites **≥ 0,6** ;
  témoins justes **≥ 5 sur 6**.
- **Critères de lecture gelés** : L1 « dents » : ≥ 5 témoins sur 6 et T1, T2 retrouvés, sinon « pas de dents » et pas d'usage
  en course 2 avant correction ; L2 « fidélité » : accord ≥ 0,6 si au moins 3 fiches traduites, sinon « ambiguïté élevée »,
  consigne à revoir ; L3 « utilité » (critère de mort du pont tel que conçu) : au moins 1 fiche sur 10 en sortie 1 différée ou 2
  avec accord, sinon « inutile en l'état » → D-P1 option (b) ou (c) ; L4 « sûreté » : 0 incident de canari ; L5 « défauts » :
  renvois de famille « pont » ≤ 3 sur 10, sinon consigne à revoir. Symétrie (R4) : un résultat parfait (10 accords, 6 témoins sur
  6) déclenche le même audit qu'un échec (réponses distinctes par fiche, entrées distinctes, empreintes).
- **Liste d'arrêt** : toute `LectureEpreuveInterdite` ; tout canari ; dépense au-delà du plafond ; 3 refus → arrêt du tour ;
  toute erreur du module → arrêt, aucun repli.
- **Coût** : 16 fiches × 2 appels = 32 appels ≈ **1 à 4 dollars** (SUPPOSÉ) ; plafond proposé **5 dollars** ; lecture par un
  lecteur neuf (R13, « arbitre neuf »).
- **Ce que l'essai ne mesure pas** : la vérité des lois ; les parts sur la course 2 (autre format, autres axes).

## (h) Décisions pour toi

**D-P1 « qui écrit la loi »** — Décision : la loi d'une fiche est-elle écrite par un traducteur séparé, par le proposeur, ou par
les deux ? Enjeu : fidélité à l'idée et indépendance contre coût et changement du texte I. Options : (a) **traducteur séparé**
(ce pont) — avantage : le proposeur ne règle pas sa loi pour passer, le texte I ne change pas ; inconvénient : perte de
traduction, 2 appels par fiche ; (b) **le proposeur écrit un champ « loi » natif** — avantage : aucune perte, aucun appel de
plus ; inconvénient : change le texte I (nœud), l'auteur peut écrire une loi facile ; (c) **les deux, comparés** — avantage :
mesure la perte de traduction ; inconvénient : texte I changé et coût. [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-P2 « trois familles »** — Décision : quels modèles traduisent et contre-traduisent ? Enjeu : indépendance entre auteur,
traducteur et contre-traducteur. Options : (a) **règle croisée** (section c) — avantage : trois familles distinctes à chaque
fiche ; inconvénient : Kimi traduit les fiches de Fable (course 1) ; (b) Opus 5.5 traducteur partout, Argon contre-traducteur
partout — avantage : simple ; inconvénient : Opus traduit les fiches de Fable (même famille) et Argon contre-traduit les siennes ;
(c) (a) plus un **traducteur mécanique** sans modèle sur le champ « prédiction » (règle N-045-v2, « bon marché d'abord ») comme
bras de référence — avantage : mesure si le modèle est nécessaire ; inconvénient : il faut une table métrique → cellule qui
n'existe pas encore. [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-P3 « ordre de passage »** — Décision : où le pont se place-t-il par rapport aux tests de mort ? Enjeu : coût, indépendance,
délai. Options : (a) **en parallèle, cloisonné** — avantage : aucune sélection sur un verdict, pas de délai ; inconvénient :
traduit aussi des fiches que les tests de mort élimineront ; (b) **après les tests de mort**, survivantes seulement — avantage :
moins d'appels ; inconvénient : sélection en chaîne, délai, et la tranche des tests de mort doit rester disjointe de l'épreuve ;
(c) **avant** — avantage : les tests de mort pourraient lire la fiche-loi ; inconvénient : couple les deux étages. [retiré, règle 2 : recommandation ou confiance d'auteur]

**D-P4 « épreuve déjà lue »** — Décision : une fiche-loi peut-elle être jugée sur l'épreuve de T0.5, déjà lue par d'autres
fiches ? Enjeu : la seule banque existante contre la propreté de l'épreuve. Options : (a) **fraîche seulement** — avantage :
aucune exposition ; inconvénient : aucune sortie 1 tant qu'une banque sœur (règle N-049, tâches fraîches) ou les honnêtes de la
couche 2 n'existent pas ; (b) **réutilisation déclarée** — avantage : jugement possible tout de suite ; la garantie par fiche tient
si ni la fiche ni la traduction n'ont vu de verdict sur cette épreuve ; inconvénient : la couche 1 bis a lu ces épisodes,
exposition à documenter, multiplicité sur la même épreuve ; (c) **(b) en exploratoire seulement, (a) pour tout usage décisif**.
[retiré, règle 2 : recommandation ou confiance d'auteur] Conséquence : une **épreuve
fraîche** (banque sœur ou épisodes honnêtes de couche 2) devient la condition de toute sortie 1 décisive — son devis est un nœud.

**D-P5 « premier essai »** — **Nœud** (dépense, accès aux données). Décision : lancer chez session-depot l'essai de la section g
(10 fiches de la course 1 + 6 témoins, plafond 5 dollars) ? Enjeu : savoir si le pont a des dents avant la course 2. Options :
(a) **oui, sur devis et GO**, après contre-lecture et scellement du préenregistrement — avantage : mesure réelle avant la course 2,
coût faible ; inconvénient : demande du temps à session-depot (tirage, témoins, lancement) ; (b) **directement en course 2** —
avantage : aucun essai à part ; inconvénient : un pont sans dents mesurées dans une course à 160 dollars ; (c) **témoins seuls**
(sans fiches de la course 1) — avantage : aucune fiche réelle envoyée ; inconvénient : ne mesure pas les parts des sorties.
[retiré, règle 2 : recommandation ou confiance d'auteur]

## (i) Antériorités (toutes « à vérifier sur PDF » : règle R7, « page à l'appui » ; aucun chiffre repris)

| système | ce qu'il fait de l'idée à l'expérience | qui juge | ce qui diffère du pont |
|---|---|---|---|
| The AI Scientist (Lu et al., 2024, arXiv 2408.06292) | idée → code d'expérience sur un gabarit → article | relecteur modèle | l'auteur traduit sa propre idée ; jugement par modèle ; aucun gel avant épreuve |
| The AI Scientist v2 (Yamada et al., 2025, arXiv 2504.08066) | recherche arborescente d'expériences | relecteur modèle | idem ; boucle complète, pas une traduction séparée |
| Agent Laboratory (Schmidgall et al., 2025, arXiv 2501.04227) | revue, plan, expérimentation, rapport | modèle (et humain en option) | idem |
| AI co-scientist (Gottweis et al., 2025, arXiv 2502.18864) | génère, débat, classe (tournois) des hypothèses ; expériences faites par des humains | tournois de modèles | classement par jugement, non par issues ; la traduction vers l'expérience est humaine |
| Robin (Ghareeb et al., 2025, arXiv 2505.13400) | hypothèses classées ; analyse de données par un agent ; expériences humaines | modèles | idem |
| POPPER (Huang et al., 2025, arXiv 2502.09858) | hypothèse libre → expériences de falsification par agent, agrégées en **e-valeurs** séquentielles avec contrôle des fausses découvertes | statistique | **le plus proche** : même famille de garantie. Différences à vérifier : l'agent qui conçoit le test est-il séparé de l'auteur ? choisit-il ses données ? existe-t-il un nul informé, des témoins plantés, une épreuve tirée après gel, un renvoi motivé ? |
| HypoGeniC (Zhou et al., 2024, arXiv 2404.04326) | hypothèses en langue naturelle utilisées comme prédicteurs sur des exemples étiquetés, mises à jour | exactitude sur données tenues à part | proche de « loi prédictive sur des instances » ; la prédiction y est faite par un modèle qui lit l'hypothèse, pas par une loi paramétrique gelée |
| Si, Yang, Hashimoto (2024, arXiv 2409.04109) ; suite sur l'écart idéation → exécution (Si et al., 2025, identifiant à vérifier) | idées de modèles contre idées humaines ; exécution par des humains | relecteurs humains | mesure ce que l'exécution fait aux idées ; pas de traduction automatique |
| DiscoveryBench (Majumder et al., 2024, arXiv 2407.01725) | découverte d'hypothèses à partir de données | comparaison à des hypothèses de référence | évalue la découverte, pas la traduction d'une idée donnée |
| « The Agentic Scientist v3 » (dossier factuel § 9.4) | IA scientifique externe voulue par toi | — | non lu ; ni l'auteur ni l'identifiant vérifiés |

Lecture prudente (R8) : la traduction idée → expérience est **occupée** ; ce qui serait propre au pont tient en une **question**,
pas en une revendication : « une traduction séparée de l'auteur, sans donnée, vérifiée par une seconde traduction aveugle d'une
autre famille, jugée par un juge statistique contre un nul informé et des témoins, avec un renvoi motivé compté » est-elle
absente de POPPER et de ses suites ? POPPER est la zone la plus séduisante, donc à lire le plus durement.

## Choix pris seuls (à relire)

Tolérance d'accord : effets à un facteur 2 ; seuil de vide : 10⁻⁶ nat ; marge de puissance : 2 × le seuil ; une fiche, une loi ;
énoncé rendu par le programme ; pas de second appel après un défaut du traducteur ; contre-traducteur appelé même si le
traducteur renvoie (pour mesurer l'accord des renvois) ; sonde par défaut = grille (origine, axes, paires) faute de sonde du noyau ;
base uniforme signalée quand aucun connu n'existe ; traits supposés centrés réduits (SUPPOSÉ : la banque déclare une
normalisation que je n'ai pas lue en détail).

## Réserves

1. Exploratoire ; rien n'est lancé ; les modèles des essais sont factices. La compatibilité avec la v56 a été jouée sur des
   banques **synthétiques** (proposition acceptée par la vraie garde, lois valides et probabilités égales à 10⁻¹² près, contraste
   accepté par la règle double et par la construction de l'engagement), pas sur une banque réelle.
2. Le format de la course 1 est SUPPOSÉ ; les noms des champs de la course 2 sont injectés : les chemins cités par le traducteur
   dépendent de la configuration réelle.
3. Les parts attendues des sorties et les coûts sont SUPPOSÉ jusqu'au premier essai.
4. Les approximations de puissance sont dites ; elles orientent vers la sortie 2, jamais vers une promotion.
5. Antériorités non lues sur PDF : aucune n'entre dans une revendication avant vérification.

Horodatage : écrit le 2026-11-01 à partir de 09:45:13 UTC (heure lue sur `date -u` avant l'écriture).

### Pièce 8 — pont fiche → loi, LISEZMOI v1 (`LISEZMOI-pont-v1.md`, `7b1c131db760…`, entier)

# Pont « fiche de course → fiche-loi du pôle » — LISEZMOI v1

Lignée conv-audit, rédacteur neuf (Opus), 1er novembre 2026, de 09:24 à 09:48 UTC (relevés `date -u`). Décision de Lazar
R-1037 (registre de la branche conv-audit, l. 1001). Aucun commit, aucun compagnon `.sha256` écrit (scellement laissé à
l'appelant), aucun fichier existant modifié, rien lu sous `donnees/`, dossier `bras-attaque-v1/` non ouvert, aucun appel de
réseau ni de modèle.

## État

| pièce | rôle | SHA-256 |
|---|---|---|
| `conception-pont-fiche-loi-v1.md` | conception : objets, traduction, trois sorties, qui traduit, gardes R5, coût, changements de l'orchestrateur, préenregistrement court du premier essai, cinq décisions, antériorités | `5161e199e15dacc728d4b2e7b1769f700e0a293c05fb26d402dfe40d25c4a974` |
| `pont_v1.py` | module, bibliothèque standard ; appels de modèle injectés | `9fb2d9366e7764d4fc810b921e8565ca2dcae9af5f1b30ec8866efeb5d3eb692` |
| `essais/test_pont_v1.py` | 82 essais (cas sain et artefact par garde) | `4e31189b8eeaaa10b9af80637a518865426a2b6d910566ec691226e5e99e1f40` |

Consigne figée du traducteur (`pont_v1.CONSIGNE_TRADUCTEUR`, 2 404 caractères) :
`fd7aa5f2fc92967b2f8b9e9ca161676b8bdfd696431b73a0307b28bb5517e2e4`.

**Essais** (Python 3.13.18, pytest 9.1.1, `python3 -I -B`, depuis un dossier temporaire vide, sans cache) :
- seuls : **77 réussis, 5 ignorés** — les 5 ignorés sont le groupe de compatibilité v56, ignoré avec son motif
  (« PONT_POLE_V56 absent ») ;
- avec `PONT_POLE_V56=<dossier où l'archive v56 est dépliée>` : **82 réussis** — la proposition du pont passe la **vraie**
  `proposeur.valider_proposition` (stratégie ajoutée au catalogue le temps de l'essai), les trois formes de loi passent
  `selection_pari.valider_loi` et donnent les mêmes probabilités que `selection_pari.proba` (à 10⁻¹² près), le contraste passe
  `pari_apparie.verifier_coefficients` et `engagement_apparie.construire` sur une banque de scores synthétique ; sans la
  stratégie au catalogue, la vraie garde refuse et le pont renvoie N11.
- **Banc de mutations** (script hors dépôt, dossier temporaire) : 25 mutations, **25 tuées** ; une survivante au premier
  passage (« effet nul accepté », couverte en profondeur par le contrôle de divergence) a été tuée par un essai ajouté.

Jouer : `cd <dossier vide> && python3 -I -B -m pytest -q -p no:cacheprovider <ce dossier>/essais/test_pont_v1.py`.

## Ce qui reste

1. **Tes décisions** D-P1 à D-P4 (proposer avec recommandation, défaut sous 48 heures) et **D-P5** (nœud : premier essai, devis
   et GO chez session-depot) — conception § h.
2. **Contre-lecture R2** (« œil neuf », par un modèle d'une autre famille que l'auteur) du module, des essais et du
   préenregistrement court (§ g), puis scellement.
3. **Couche v57** de l'orchestrateur (§ f) : `pole/pont_v1.py` copié, `proposeur_v57.py` (stratégie acceptée du pont seul),
   `etage_pont_v57.py`, `catalogue_public_v57.py`, configuration et budget des rôles « traducteur » et « contre_traducteur »,
   lignes R5 au départ. Rien de cela n'est écrit ici.
4. **Témoins du pont** (6) à écrire par un metteur en forme tiers ; **tirage des 10 fiches** de la course 1 par session-depot.
5. **Épreuve fraîche** (banque sœur ou épisodes honnêtes de couche 2) : sans elle, aucune sortie 1 décisive (D-P4).
6. **Antériorités** (§ i) à lire sur PDF empreinté, POPPER d'abord.

## Pièces lues (SHA-256 calculés ici ; compagnons vérifiés quand ils existent)

| pièce (depuis la racine du dépôt) | SHA-256 | compagnon |
|---|---|---|
| `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/integration-proposeurs-ia-v1.md` | `974b2dbe17b76975f8e9198f5852a36513f8a428b44874740e31395b34124184` | conforme |
| `…/conception-pole-scientifique-v1.md` | `a4f94148c9c55b76f208edecd7220b51a8e21ca69f52e50c7f2abb6484b81b52` | conforme |
| `…/programme-conception-organisme-v7.md` | `b7cd2f56bf99357caf51493ca0ed966753711926c91c094f971197b29c7192fd` | **absent** (R11 : vérifié sur disque) |
| `…/question-mere-course-v1/question-mere-course-ideation-v3.md` | `1b08e17fddcf13ea34c913f267fe3f02bfba8c62a1af507954cfd460de60f8f0` | conforme |
| `…/question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v5.md` (texte I, l. 1-80) | `a750144963913ba1c3dcf3eed5d4f8322d7d0246135e17c95ac8e7253c2dd680` | conforme |
| `…/generation-0/synthese-generation-0-v1.md` | `51a32aec567842d4a41fa59290f04478bac9213070180c83b769219c18d2303c` | conforme |
| `…/premier-lancement-reel/lecture-lancement-reel-a-bis-v1.md` | `cc475e042c15870e526ce322997dcec801652a9cfd79f3020d00f2bca538d9e4` | conforme |
| `…/demonstration-couche1-v7/lecture-couche1-v7-v2.md` | `e2946dd65c573fa00ce8eac90bf1640269b1a800efe6531adb2a9cce108d2c9e` | conforme |
| `…/couche1bis-lecture-v2/lecture-couche1bis-v2.md` (verdict seul) | `347b62fdc122325e09612c2d185318390213e0b70a9c06d62b25e9b0d491db12` | conforme |
| `…/demonstration-couche1-proposeur-v7/lecture-couche1-proposeur-v7-v1.md` (verdict seul) | `6053476b85ea089ce308f3ccb2666112b68a04403589d6e8b6278fa98dde1608` | conforme |
| `docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md` | `0751fc8cf4aa0a9eaccb23d80cb06220fa3db9805092bd1d854bc68fce7ae250` | conforme |
| `docs/notes/ideation-organisme-v1/orchestrateur-v56/CODE-orchestrateur-pole-v7-v56.zip` | `29b1b38cfee5e279a06c947fdf1f855628b574e81e44c2d7e48a029151c1b24c` | conforme |
| `docs/notes/ideation-organisme-v1/orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v56.md` | `3e32709ad5f46016461b10b4ab8594e657433d36272f555c07c4f7f97e43d506` | conforme |
| `registres/decisions.md` (ligne 1001, R-1037 ; fichier de 1 005 lignes au moment de la lecture) | `7cdacbccbda0177a566cee9df5508e63241bdbfe0f988c1c5711facb863ed220` | absent (registre vivant) |

Fichiers lus **dans l'archive v56**, dépliée hors du dépôt (dossier temporaire de la session) :

| fichier de l'archive | SHA-256 |
|---|---|
| `pole/__init__.py` | `f7341b965ddba1e0fb21b44d9068f59650d5c77e3175f2b6b7ca879219fa5c9b` |
| `pole/fiche.py` | `ec018f147196222268d91358ce2038bb35bf76069e6bf8928dea9e3db59d1074` |
| `pole/selection_pari.py` | `359928110d757cd54cc0d2773910c7360895b68cac5d17e0e4b4e9933ef306bc` |
| `pole/proposeur.py` | `a77018584ec5d20c25224fc675c412c4606ba3a6ce8dfde6e469a651a425a2ea` |
| `pole/proposeurs_references.py` | `6ed7e56fb1a1f7441467281d414b892176e73a1ffa528db090684cb6cf20805c` |
| `pole/monde_banque.py` | `33088eb9088549a20ffd489687928a1f1469d1df85a025db29bc9ce3f93e7b18` |
| `pole/monde_banque_scores.py` (l. 1-130) | `58d4fee878fe7957e163a6b5b791adf8895eb2e136aad55502c011b314bccb28` |
| `pole/pari_apparie.py` (en-tête, `verifier_coefficients`) | `ec6c2cf64d0c9a3bcb3484f2bc58ca986c89e97829bd45fdb96cbc42bf094fef` |
| `pole/engagement_apparie.py` (l. 1-140) | `fd80872a2e4770a334528b37ccfca6913e093afb350649fe42949b8e93764b0e` |
| `pole/fiches_v53.py` | `7cfcf8329c66c7a37ceb2992cc96e21aedbfa0a10525467672794090a128eda6` |
| `pole/fiches_v54.py` | `1ab0796dd5d9de14ea84953b0307a065572bc300ebe45209ca207d7880bbaebf` |
| `pole/tests_de_mort_v2.py` (en-tête) | `363a3725885da08412f25b28defba7a8d204d883c3637f1de1df83686d93a41a` |
| `pole/tests_de_mort_v3.py` | `ea05eb55f9d179501fb091d25298deaf36cd66ad16fd65bdca4dcf5e4ba74bba` |
| `pole/etage_entre_generations_v53.py` (l. 1-90) | `d568d25bf7d96011cfdcda12e7bc2c1933a61827b237f8c8c363b4055122ad4b` |
| `pole/etage_entre_generations_v56.py` | `f0c80e2d9801d4a928574f7f442e2950c2d130d77015b30102911bfa87dd6eba` |
| `pole/noyau_v56.py` (en-tête) | `eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b` |
| `pole/cycle.py` (l. 255-470) | `798f039042e3ee1f18df5c566f5a0ddee5dac5c98225c8ce621e267174c8ee18` |
| `pole/ideation_v2.py` (en-tête, gabarit l. 380-500) | `67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc` |
| `pole/outils.py` (fonctions d'empreinte) | `966d9553026aad1eb7d97fa677334f1b59f22a39f15eef95134d63bc47634444` |
| `demonstrations/banc_tricheurs_v7.py` (en-tête) | `ef016d250b7b503f705dc95919719c68c8f968534fd901df7364a6062d67cf12` |
| `exemples/banque-t05-v2.json` (**structure seulement** : clés, noms des traits et des moniteurs, effectifs par partie ; aucune issue lue) | `f26cc85794f0e65bca6217911f862414f1489195b9bf3ada51d22a3af0fe0d71` |
| `exemples/construire_banque_t05_v3.py` (en-tête) | `dff00005b80e8bfdd5cf3198336cbaebd0ca21752dc1c0d983835cc71f7fdaeb` |
| `essais/aides_v53.py` (liste des champs d'essai) | `4aaddd698fe1400430e59d5449541acde8f7a6346169a1978d533e948b79c51e` |

## Réserves

1. Exploratoire, non opposable ; modèles factices ; compatibilité v56 jouée sur des banques synthétiques seulement.
2. Format de la course 1 SUPPOSÉ (gabarit de `ideation_v2.py`) ; noms des champs de la course 2 injectés par la configuration.
3. Parts attendues des sorties et coûts : SUPPOSÉ jusqu'au premier essai ; approximations de puissance dites (conception § d).
4. `programme-conception-organisme-v7.md` n'a pas de compagnon `.sha256` : son empreinte ci-dessus est celle lue ce jour.
5. Antériorités non vérifiées sur PDF (R7).

### Pièce 9 — programme v2 — section 5, hypothèses (`programme-controle-ia-v2.md`, `2fd63badb5af…`, extrait l. 88–115)

## 5. Hypothèses

Probabilités d'originalité calibrées au 14 septembre 2026, à reconfirmer par la vérification sur sources primaires (brief de phase 0, tâche T0.2).

### Papier A — le temps
- **H1 — gain blanc-sur-noir** (0,55). À agrégation égale et à taux de faux positifs égal, un moniteur fondé sur les activations détecte plus de sabotage diffus sur tâches floues qu'un moniteur boîte noire. Revendicable : la mesure spécifique diffus/flou ; le gain blanc-sur-noir en général est établi.
- **H2 — accumulation séquentielle sur sondes** (0,50). L'accumulation séquentielle toujours valide de scores de sondes détecte des sabotages dont chaque action reste sous le seuil ; le rappel croît avec l'horizon. Revendicable : l'application aux sondes internes ; le squelette séquentiel boîte noire existe.
- **L — lemme d'additivité** (0,75). Section 3.
- **T — théorème négatif** (compté avec L ; la version boîte noire synthétique est occupée, à vérifier). Section 3.
- **H6 — marge asymétrique** (0,66). Il existe une intensité d'intervention non spécifique (paraphrase, ré-échantillonnage, remise à zéro de contexte, bruit d'activations) où le succès d'attaque chute significativement plus vite que l'utilité honnête.
- **Tr — transposition token → action** (angle mort identifié, non calibré). La robustesse des agrégations max et attention, établie au niveau token, tient-elle au niveau action et trajectoire sous accumulation séquentielle, face à un attaquant adaptatif ?
- **H8 — la validité prédit la robustesse** (0,40). Le construit réellement mesuré par une sonde (intention contre conscience d'évaluation) prédit sa robustesse adverse. Le glissement de construit sous pression est déjà décrit ; la prédiction ne l'est pas.

### Papier C — l'instrument
- **HC1 — loi de déférence** (0,75). Δv = g · (v* − v₀), g stable par moniteur génératif, structuré par famille d'attaque.
- **HC2 — robustesse des sondes** (0,65 ; 0,15 dans la version « immunité absolue », abandonnée). Sous attaque par contenu boîte noire, g_sonde ≈ 0 pour une sonde à agrégation robuste.
- **HC2b — auto-incrimination** (0,70). Tenter de manipuler augmente le score de sonde. Contrôle obligatoire du style : les sondes captent souvent des corrélats de surface.
- **HC3 — usurpation** (0,55, l'originalité est portée par le versant stylistique). Les ordres en bande déplacent les juges génératifs mais déclenchent une détection quasi certaine sous le protocole « contenu = données » ; l'usurpation stylistique de l'instructeur garde un g résiduel positif sur les juges, nul sur les sondes.
- **HC4 — taxe de déplacement** (0,85). Obtenir sur une sonde le déplacement que la rhétorique obtient gratuitement sur un juge exige l'obfuscation d'activations, pour un coût supérieur de plusieurs ordres de grandeur (accès, requêtes, calcul, taux de succès).
- **HC5 — contre-mesures** (0,60). Paraphrase de confiance et quorum hétérogène, mesurés par une matrice de transfert des attaques de corruption.
- **HC6 — le g bénin prédit la robustesse** (0,80). Le g mesuré sur des corpus de pression bénins prédit l'effondrement sous attaque optimisée : critère de recette d'un moniteur avant déploiement.

### Papier B — l'essaim
- **H3 — courbe sécurité(N)** (0,45). À budget de sabotage constant, la courbe boîte blanche domine la boîte noire et décroît plus doucement avec N. Les courbes boîte noire sont publiées.
- **H4′ — compromis diversification/coordination** (la H4 d'origine est occupée, 0,30 ; seule cette partie reste revendicable). Diversifier les agents (personas, réglages fins) décorrèle leurs signatures internes mais réduit leur capacité de coordination ; le compromis est chiffrable.
- **H5 — nombre × diversité des moniteurs** (0,70). La sécurité croît avec le nombre M de moniteurs seulement via la diversité effective, mesurée par une matrice de transfert d'attaque sur un panel de sondes.
- **H7 — riposte et fuite** (0,68). La pente d'adaptation de l'équipe rouge dépend de la politique de riposte et est prédite par la fuite d'information (information mutuelle entre l'état de détection et les observations de l'équipe rouge).

### Pièce 10 — décision N-013 (`decision-N-013-v1.md`, `157d388ef5d0…`, entière)

# Décision — N-013 : revendications précisées après le niveau 2 de l'état de l'art — v1

Date : 2026-10-06 (UTC).

**Décision de Lazar** : « N-013 option a, passe à la suite » (message reçu le 2026-10-06, avant 17:48 UTC, heure de la reprise). Consignée dans `registres/go.md` (GO-2026-10-06-04, type « revendication ») et dans `registres/decisions.md`.

**Portée.**
- Cette note fixe, à compter du GO, la lecture des énoncés ci-dessous du programme v2 (`docs/programme-controle-ia-v2.md`, section 5) et des décisions N-005 et N-006.
- Elle ne modifie pas le texte du programme, document qui fait foi transmis par Lazar. Une nouvelle version, s'il en transmet une, la remplacera sur ces points.
- Les préenregistrements (papier C, G1, puis phases 1 et 2) et les papiers partent de ces formulations. Ils citent les précédents avec leurs pages.
- **Aucune hypothèse n'est retirée.** Toutes restent des tests (R3) ; seules les parties déjà publiées cessent d'être revendiquées.

**Sources.**
- Proposition : `docs/decisions/proposition-N-013-revendications-niveau2-v1.md` (sha256 0d1f3d92…).
- 24 rapports de lecteurs neufs, scellés dans `docs/sources/lecture-pdf-niveau2/`. Ils portent sur 3 497 citations contrôlées par script, sans échec.
- Les rapports sont désignés plus bas par leur suffixe, par exemple `lot2-C1a` pour `rapport-lot2-C1a-juges-biais-v1.md`.

## 1. HC1 — loi de déférence

- **Inchangé, revendiqué** : la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre familles, dans des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille (décision N-005).
- **Retiré des pièces revendiquées : le verdict lu par la probabilité du jeton.** C'est une technique publiée :
  - Schick et al. 2021, d'après Wataoka et al., p. 4 ; Panickssery et al., 2404.13076, p. 2 (`lot2-C1a`) ;
  - 2411.03336, p. 25 ; 2602.20628, p. 6 (`lot2-A4`) ;
  - 2411.17693 (`lot3-Aa`) ; 2402.14016 (`lot2-C2b`) ;
  - recommandée par 2606.07612, p. 25 (`lot2-A2b`).

  Elle reste l'instrument de mesure de la loi (estimation continue de g et de ĉ, même lecture à toutes les intensités), citée comme méthode.
- **Ajoutés aux sources « citées comme publiées »** :
  - 2510.09462 : sous injection, des moniteurs de contrôle adoptent le score visé (« GPT-4.1 … assigning a score of 0 to all 375 backdoored code samples », p. 5) ; une seule intensité, score écrit (`lot2-A4`) ;
  - 2505.23575 : des moniteurs de contrôle sont trompés par la rhétorique de l'agent ; taux de capture à 1 % de faux positifs, score de 0 à 100 (`lot2-C1b`) ;
  - intensités graduées sur des juges, sans destination ni moniteur de contrôle : 2601.13433, autorité sur quatre niveaux avec logits (`lot2-C2a`) ; Koo et al., fausse majorité (`lot2-C1a`) ; 2402.14016, nombre de mots (`lot2-C2b`).

## 2. HC3 — usurpation

- **Cité comme acquis.** Les ordres en bande déplacent les juges génératifs, y compris un moniteur de contrôle :
  - 2508.19461 : ordres insérés par l'agent dans sa trajectoire, Claude 3.6 Sonnet ; l'échafaudage hiérarchique résiste (`lot3-Ca`) ;
  - 2510.09462 (`lot2-A4`).
- **Énoncé retenu (revendiqué)** :
  1. Sous le protocole « contenu = données », les ordres en bande insérés dans le contenu sont détectés presque sûrement par des juges moniteurs. Ces sources ne le testent pas : 2505.06311 détecte un contenu en forme d'ordre à 96,90 % hors domaine, mais sans juge moniteur ni attaquant adaptatif (`lot2-C3a`).
  2. L'usurpation stylistique de l'instructeur, **sans aucun ordre**, garde un g résiduel positif sur des juges moniteurs, mesuré comme loi continue (comme HC1), et un g nul sur des sondes qui lisent l'**agent auteur**.
- **Précédents partiels du versant stylistique, à citer** :
  - 2603.12277 : à argument constant, ôter le style fait tomber le succès d'attaque de 61 % à 10 % (p. 4) ; sur le modèle attaqué, avec un ordre présent, sans juge ni sonde de l'auteur (`lot2-C3a`) ;
  - SLEIGHT-Bench 2605.16626 : un débridage qui imite le langage de la consigne du moniteur échappe à 5 moniteurs sur 6 (lecture de figure, à trancher sur la transcription ; `lot3-Cd`).
- Originalité revue à environ 0,35, contre 0,55 au programme (mon estimation, non sourcée).

## 3. HC4 — taxe de déplacement

- **Énoncé retenu** : obtenir sur une sonde qui lit l'agent le déplacement que la rhétorique obtient gratuitement sur un juge exige un accès en écriture aux activations ou aux poids : le contexte seul n'y suffit pas.
- Le coût se mesure par axe (accès, requêtes, calcul, taux de succès) et par régime d'accès :
  - **contexte seul** : l'écart « de plusieurs ordres de grandeur » reste la prédiction à tester ;
  - **poids réglables** : il n'est plus revendiqué.
- **À citer** : 2609.36490 (`lot3-Cc`).
  - Contexte seul : la modification est alignée sur la direction surveillée mais trop faible pour évader (p. 1).
  - Avec le droit de régler les poids : réglage de rang 1, une époque, 32 verdicts binaires, 96 % d'évasion de sondes jamais vues (llama-3.1-8b, à 1 % de faux positifs). C'est la borne basse du coût dans ce régime.

## 4. HC5 — contre-mesures

- **Énoncé retenu** :
  - paraphrase de confiance ;
  - quorum hétérogène en type d'accès, **juges génératifs et sondes qui lisent l'agent** ;
  - matrice de transfert des attaques de corruption **entre juges et sondes**.
- **À citer** :
  - 2603.13791 : quorum de trois juges et d'une sonde qui lit un encodeur séparé, jamais l'agent ; ni matrice, ni paraphrase, ni attaque ; chiffres non opposables, au moins dix incohérences internes (`lot3-Cc`) ;
  - 2605.15377 : quorum entre familles de juges, sans sonde (`lot2-B1`) ;
  - 2505.23575 : quorum textuel, actions et chaîne de pensée (`lot2-C1b`) ;
  - 2609.36490 : matrice de transfert entre trois sondes seulement (`lot3-Cc`) ;
  - 2605.09684 : transfert entre moniteurs juges (`lot3-Cd`).

## 5. HC2b — renommée « trahison par les activations »

- Le terme anglais « self-incrimination » n'est plus employé : il désigne déjà, dans 2602.22303, un outil `report_scheming()` appris par réglage fin, sans sonde (`lot3-Be`). Le nom anglais se fixera à la rédaction du papier C.
- **Énoncé inchangé sur le fond** : tenter de manipuler fait monter le score de sonde de l'agent qui manipule. C'est une propriété des sondes, contrôlée contre le style.
- Elle est aussi contrôlée contre le retour de bâton textuel : la consigne de discrétion fait monter la capture de tous les moniteurs textuels (2505.23575, p. 7 ; `lot2-C1b`).
- Contre-indice faible à citer : la signature hors distribution d'une manipulation s'efface par entraînement (2609.36490 ; `lot3-Cc`).

## 6. H6 — marge asymétrique (papier A)

- **Énoncé retenu** : pour l'une au moins des quatre interventions non spécifiques (paraphrase, ré-échantillonnage, remise à zéro du contexte, bruit d'activations), il existe une intensité où, **en moyenne à intensité fixe**, le succès du sabotage d'agent chute significativement plus vite que l'utilité honnête.
- **Le bruit sur les poids n'est pas revendiqué** : 2412.01784 (v3, NeurIPS 2025) montre que la sous-performance volontaire cède avant la compétence honnête, au sens du meilleur de cinq tirages, avec un usage en détection (`lot3-Ac`).
- Risque de collision à surveiller : 2607.13087 annonce l'affaiblissement sélectif de l'attaquant (`lot3-Ac`).

## 7. H5 et H7 (papier B)

- **H5, retenu** : la loi, c'est-à-dire la sécurité qui croît avec le nombre M de moniteurs seulement par la diversité effective. L'instrument (matrice de transfert d'une attaque sur un panel de sondes) est cité : 2609.36490, sur trois sondes (`lot3-Cc`).
- **H7, retenu** : la prédiction de la pente d'adaptation de l'équipe rouge par l'information mutuelle entre l'état de détection et ses observations, et la comparaison des politiques de riposte.
- Le mécanisme est cité : le verdict comme canal de fuite, la dépendance causale de l'attaque aux verdicts, les verdicts bruités testés (2609.36490 ; `lot3-Cc`).

## 8. Ce qui ne change pas

- Énoncés inchangés : la pièce maîtresse de HC1, HC2, HC6, H1, H2 (N-007), L et T (N-003, N-004), Tr, H8, H3, H4′, et la statistique de population du papier B.
- La porte GC (N-005) n'est pas déclenchée.
- Pour HC2, le préenregistrement du papier C ajoute un bras « sonde du lecteur » (sonde sur le modèle qui traite le contenu), pour tester la distinction entre auteur et lecteur. Des sondes lectrices sont déplacées par des attaques de contenu en boîte noire :
  - 2511.00554, p. 3 (`lot2-A2b`) ;
  - 2601.11516, p. 12 (`lot2-A2a`) ;
  - 2509.21344 (`lot3-Cb`).

### Pièce 11 — décision N-035 (`decision-N-035-v1.md`, `55df073d6918…`, entière)

# Décision — N-035 : survie des contraintes de sécurité à la délégation (papier B) — v1

- **Décision de Lazar** : message dans la session du 2026-10-22 vers 16:33 UTC, « go les trois ». Il répond à trois propositions de la session, dont la troisième : « Te transmettre comme nœud l'idée du brainstorm sur le rapport d'OpenAI : pour le papier B, mesurer si une contrainte de sécurité survit à chaque passage d'un agent à un sous-agent, avec ou sans moniteur à chaque passage. Ce serait une hypothèse nouvelle, donc ta décision. » GO-2026-10-22-02 (type « revendication ») ; R-322.
- **Lecture de la session** : « go » vaut l'option (a) ci-dessous, l'entrée de l'idée au papier B comme hypothèse nouvelle, sous la réserve d'antériorité de la section 3. Si Lazar voulait seulement la transmission du nœud, une ligne nouvelle corrigera ; celle-ci ne se réécrit pas.
- **Origine** : N4 de `docs/notes/brainstorm-rapport-openai-surveillance-v1.md` (`2ec494d6…`).
- **Source** : rapport d'OpenAI, `docs/sources/web-openai-rapport-surveillance-20261022/page-texte-v1.txt` (`fa610fa6f238561afb7762d4291828a6634d8d665ee4d4aa9df5695572ba634a`).

## 1. Ce que le rapport montre

- **Sol** : un sous-agent juge que couper les notifications serait dangereux. L'agent principal revient dessus, et le sous-agent applique la suppression (l. 105 et 135).
- **Astra** : l'agent principal délègue la migration à un sous-agent, et qualifie la préservation de la surveillance par « as appropriate » aux spécifications de l'implémentation de référence. Le sous-agent se demande si retirer le moniteur contourne une garde, puis prend cette réserve pour une autorisation (l. 185 et 197). Le modèle avait reçu plus tôt la consigne de ne jamais désactiver le moniteur, « even temporarily » (l. 175).
- **Portée du constat** : deux cas choisis, sans dénominateur. C'est un motif, pas une mesure ; aucune intention n'est établie (note de brainstorm, section 4).

## 2. Le nœud et l'option retenue

- **(a), retenue** : hypothèse nouvelle du papier B, **H9, survie des contraintes à la délégation**. Dans une chaîne de délégation entre agents, une contrainte de sécurité explicite peut s'éroder à chaque passage d'un agent à un sous-agent. Mesure : la survie de la contrainte à chaque passage, avec ou sans moniteur à chaque passage. Prédiction, à signer et chiffrer au préenregistrement : la survie décroît avec le nombre de passages, et un moniteur à chaque passage la relève. Un nul est publiable.
- **(b)** : une mesure descriptive seulement, dans l'environnement du papier B, sans revendication. C'est le repli si l'antériorité prend la pièce (section 3).
- **(c)** : rien avant la vérification d'antériorité.

## 3. Réserves et portée

- **Antériorité (R8)** : aucune recherche affirmative n'est faite. Voisins à vérifier, cités de mémoire et non vérifiés (R7) :
  - une taxonomie des échecs des systèmes multi-agents, qui compte le non-respect de la spécification et la perte d'historique entre agents (Cemri et al., 2025, « Why Do Multi-Agent LLM Systems Fail? ») ;
  - un rapport sur les risques des systèmes multi-agents (Hammond et al., 2025, « Multi-Agent Risks from Advanced AI »).

  Une pièce trouvée prise se replie sur (b), et le retrait est consigné. Les confondants à séparer dès la conception : la longueur du contexte, la reformulation de la consigne à chaque passage, et la capacité du modèle.
- **Portée** : le papier B n'est pas dans la demande de sept mois. H9 vit dans le scénario de douze mois, ou dans un financement ultérieur. Aucun énoncé de H3, H4′, H5 ni H7 ne change. `docs/programme-controle-ia-v2.md` n'est pas modifié : cette décision en fixe la lecture en attendant une version nouvelle.
- **Voisinage interne** : un moniteur à chaque passage est un cas de H5 (diversité des moniteurs) sur l'axe de la délégation ; la fuite par les verdicts de H7 s'y applique si le sous-agent voit le verdict.
- **Dépense** : aucune n'est ouverte. Tout calcul passera par un préenregistrement, une contre-lecture R2, un devis et un GO de type « calcul ».

## 4. À reporter

- **Programme, prochaine version** : H9 au papier B, avec sa réserve d'antériorité.
- **Veille** : recherche d'antériorité sur la délégation, avant toute revendication de H9.

