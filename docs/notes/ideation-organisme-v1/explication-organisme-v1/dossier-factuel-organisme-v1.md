# Dossier factuel — l'organisme d'idéation (« pôle scientifique automatique ») — v1

Lecteur neuf (Opus) de la lignée conv-audit, 1er novembre 2026. Lecture seule : rien sous `donnees/`, aucune ref `donnees/*`, aucun appel de réseau ni de modèle ; le dossier `bras-attaque-v1/` n'a pas été ouvert (sa fonction est tirée du programme de conception v7). Tout est au niveau méthode.

## Conventions de renvoi (pour le rédacteur)

- **[P]** = `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/`
- **[N]** = `docs/notes/ideation-organisme-v1/`
- **[B10]** = [P]`pre-pilote-course-2-v1/preenregistrement-pre-pilote-course-2-brouillon10.md` (préenregistrement du pré-pilote, non gelé)
- **[TI]** = [P]`question-mere-course-v1/recoupement-v1/question-course-2-defense-fusion-v5.md` (« texte I » de la course 2, la question servie aux proposeurs)
- **[Dbr]** = `registres/decisions.md` de la branche `canal/conv-audit-n04` (registre de conv-audit) ; **[Dmain]** = `origin/main:registres/decisions.md` (registre de session-depot). « l. » = ligne du fichier.
- **Attention : les numéros R-xxx des deux registres se recouvrent et ne désignent pas la même décision.** Exemple : R-597 de [Dmain] (l. 823) = bras d'attaque arrêté par un classifieur ; R-597 de [Dbr] (l. 811) = contre-lecture 1 du pré-pilote. Toujours dire de quel registre vient un R-xxx.
- Étiquettes d'état : **DÉCIDÉ** (mot de Lazar consigné), **PROPOSÉ** (recommandation sans mot), **ESSAYÉ** (a tourné, avec résultat), **CODÉ NON ACTIVÉ**, **PAS CONSTRUIT**.
- Les deux sessions : **conv-audit** conçoit, écrit le code de l'orchestrateur, ne lit jamais `donnees/` ; **session-depot** tient les clés, lance les dépenses sous ligne de feu vert (« GO »), garde `donnees/` et le bras d'attaque scellé.

---

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

## 2. Le moissonneur

- **Ce qu'il récolte (DÉCIDÉ)** : option (A) — **arXiv et OpenAlex, métadonnées et résumés seulement, jamais de PDF brut** ; Semantic Scholar en option (B) non retenue ; **Brave exclu** ([Dbr] R-442 l. 656 ; « go » de Lazar R-466 l. 680). Quotas recommandés : 1 tour, 4 requêtes, 5 résultats ([Dbr] R-442). Statut `MOISSONNE` des fiches : non opposable (R7). Aucun courriel d'identité envoyé à OpenAlex (« on verra ça plus tard », R-469 l. 683).
- **Comment** : un **relais de moisson séparé**, dont le noyau est le seul client (aucune commande `moisson` donnée à l'agent) ; clés tenues par le relais ; **garde de fuite** (refus de toute requête qui porte un texte de test ou un identifiant d'épisode) ; provenance par empreinte ; cache rejouable ; tour de moisson court entre passe 1 et passe 2 ([P]`orchestrateur-pole-v7/conception-v7-v1.md` § 5, l. 78-86 ; [Dbr] R-437 l. 651, R-442 l. 656).
- **Ce qu'il produit** : des extraits servis comme données (jamais comme consigne) à tous les proposeurs, **jamais aux juges** ([Dbr] R-442).
- **Où il en est** :
  - **CODÉ** dans l'orchestrateur v47 avec relais factice, option `--moisson` par défaut « aucune », 444 essais sur 444 ([Dbr] R-492 l. 706). Coût annoncé ≈ 0,4 dollar par course ; « go » de dépense de Lazar ([Dbr] R-514 l. 728).
  - **Relais réel, épreuve courte, première moisson réelle par ce module : aucune trace trouvée** (ordre prévu : chez session-depot, sur GO séparé, R-466). Lazar : « il nous faut le moissonneur pour la course 2 » (R-469).
  - **Moisson en vrac distincte** : session-depot a moissonné OpenAlex pour la bisociation et l'épreuve d'identification — 197 681 œuvres en cinq sous-domaines, 237 Mo, `donnees/moisson-openalex-v1/` (non lu ici) ([Dmain] R-863 l. 1092). Elle doit servir de source au substitut de Gu et Krenn (S31) après un essai ([B10] l. 49, 704).
  - Le pré-pilote ne s'en sert que pour vérifier l'existence des références (« routine, sans dépense », [B10] l. 671).

---

## 3. Les proposeurs et les fiches

### 3.1 Qui propose
- **Course 1** : Fable 5.1 et Argon ; Opus 5.5 proposeur retiré après son refus de la tentative 1 (et la bascule non autorisée vers Opus 4.8, arrêtée) ([Dmain] R-764 l. 992, R-802 l. 1030).
- **Course 2** : Kimi K3.1 Pro remplace les proposeurs Claude « pour économiser » (DÉCIDÉ, [Dbr] R-567 l. 781) ; Argon reste proposeur (SUPPOSÉ par le devis v6 § 4.1, [N]`course-2/devis-course-2-et-pre-pilote-v6.md` l. 237). Plan : 4 sous-sessions, chacun 2 passes de 8 fiches, ≈ 128 fiches (devis v6 l. 237).
- **Pôle** : « proposeur maison » (Opus 5.5 et Fable 5.1) ou **proposeur mécanique** sans modèle, essayé d'abord par règle (N-045-v2) ; systèmes publiés candidats : AI Scientist v2, Agent Laboratory (boucle complète), Co-scientist, Robin (idéation) — tous **à vérifier sur PDF** ([P]`integration-proposeurs-ia-v1.md` § 3, § 8).

### 3.2 Format d'une fiche de course ([TI] l. 44)
3 000 à 8 000 caractères ; champs : axe ; hypothèse ; prédiction chiffrée et signée (métrique de la liste M, valeur, unité) ; livrables de l'axe ; données (liste D) ; coût (processeur, carte, dollars) ; antériorités (au plus cinq : titre, auteurs, année, élément qui leur manque, page ou « à vérifier ») ; **source d'avantage** (liste L) ou élément manquant à l'antériorité la plus proche ; **critère de mort** ; **vis-à-vis** (lien angle ↔ faille, compté, non noté) ; marque SUPPOSÉ. Règle : niveau méthode, aucune conduite d'agent, consigne ou séquence d'actions ([TI] l. 42).

### 3.3 Les axes, en clair (texte I et suivants)
- **Axe 1 — battre HELIOS** (meilleures statistiques et agrégateurs ; partir d'une table des écarts) ([TI] l. 50-54).
- **Axe 2 — ce que le domaine retiendrait** (loi, garantie ou impossibilité ; résultat publié qui la rendrait inutile) (l. 56-57).
- **Axe 3 — failles du programme en pré-mortem** (« G1 a échoué : quelle hypothèse porteuse a cédé ? ») (l. 59-60).
- **Axe 4 — universalité sur les familles existantes** (livrable = un préenregistrement à sceller, exécuté par un tiers) (l. 62-64).
- **Axe 5 — statistiques par la théorie** (preuve Lean sans `sorry` ou simulation préenregistrée) (l. 66-67).
- **Axe 6 — volet attaque**, servi à part en **texte II**, deux bras « avec » et « sans pistes » (DÉCIDÉ, [Dbr] R-564, R-565 l. 778-779) ; non ouvert ici.
- **Axe 7 — angles d'approche non occupés sur tout le contrôle**, sous-session neuve, grille de cases « à arrêter par Lazar » ([TI] l. 69-70).
- **Axe 8 — robustesse adaptative** : PROPOSÉ, en analyse (attend la synthèse du collisionneur sur N10) ([Dbr] R-743, R-744 l. 958-959).
- **Texte III** : comment concevoir le bras d'attaque et mesurer l'universalité des défenses, au niveau méthode (DÉCIDÉ, [Dmain] R-824 l. 1052) ; non ouvert ici.
- Écart à signaler : « une course, sept axes » est la décision de conception de R-469 ([Dbr] l. 683) ; la course 1 a tourné sur la question antérieure de la « voie (β) » ([Dmain] R-759 l. 987), dont je n'ai pas relu les axes.

### 3.4 Les « fonds » (deux sens)
- **Dans le pré-pilote** : un **fond** = le squelette d'une fiche témoin (12 à 16 ancres + « couples de défaut » plantés), rendu en fiche par un seul metteur en forme ; 28 fonds ([B10] l. 688). **D-i (2) DÉCIDÉ** : 28 fonds uniques + 4 rendus appariés (deux fournisseurs pour le même fond) servant seulement à éprouver la mémoire, ≈ +0,55 dollar ([Dbr] R-719 l. 933).
- **Ailleurs** : « le fonds » = le dossier de financement (le paragraphe de tête du programme de conception est « commun au dossier du fonds », [P]`programme-conception-organisme-v7.md` l. 19).

### 3.5 Cloisons entre proposeurs ([TI] l. 48 ; [Dbr] R-598 l. 812, R-565 l. 779)
- Passe 2 nourrie des fiches de la passe 1 du même proposeur (correction des doublons de la course 1, § 5).
- **Tableau minimal** : seulement titres et résumés d'une ligne, **même texte et même bras** ; jamais entre textes I, II, III, ni entre les bras « avec / sans pistes » de l'axe 6 ; jamais la fiche entière ; une fiche aiguillée n'y entre pas (garde A18, [B10] l. 291).
- Passe de critique : sur les fiches anonymes de l'autre fournisseur, seulement marquer un champ faux ou ajouter une antériorité ; aucune fiche nouvelle ou réécrite ([TI] l. 48).
- Axe 7 en sous-session neuve, sans les axes 1 à 5 ([TI] l. 48).
- Notation croisée : un proposeur ne juge pas ses propres fiches (Argon note Kimi, Kimi note Argon) ([Dbr] R-572 l. 786 ; devis v6 l. 244).

---

## 4. L'aiguilleur

- **Ce qu'il trie** : chaque fiche (et chaque fusion), **avant tout juge**, en « niveau méthode » (classe d'attaque, mécanisme, conditions, défense) ou « trop concret ». Les classes du trop concret sont décrites par leur forme seulement : C1 séquence d'actions ordonnée ; C2 recette à étapes ; C3 consigne d'agent rédigée ; C4 mode nommé avec paramètres opérationnels ([B10] l. 690).
- **Pourquoi** : **R-339** ([Dbr] l. 552 ; programme v7 l. 55-58) — la sortie adversariale va au niveau méthode, « jamais la recette » ; **R-597 de [Dmain]** (l. 823 : le lanceur du bras d'attaque arrêté par un classifieur, aucune relance) ; **R-575 de [Dbr]** (l. 789 : tout détail d'attaque concret est **scellé dans le bras d'attaque chez session-depot**, conv-audit n'en lit rien) ; **R-819 de [Dmain]** (l. 1047 : aiguillage avant les juges).
- **Où vont les fiches** :
  - trop concret → scellé au bras d'attaque (schéma n° 208 : dossiers scellés, lecteur isolé, seuls comptes et classes vers la défense) ; la fiche ne va à aucun juge, ni au tableau, ni aux lectures d'étiquettes ; elle est **comptée** ([B10] l. 282, 690 ; garde A17 l. 112 du tableau d'arrêts) ;
  - niveau méthode → tableau minimal, mémoire, bisociateur, étage 1, juges.
- **Comment on l'étalonne** (mesure M4, [B10] l. 282) : entrée anonyme mêlée de 28 rendus de témoins, ≤ 10 fiches de Kimi, 6 fiches « difficiles » de niveau méthode à vocabulaire dense, et **12 fiches trop concrètes (3 par classe C1 à C4) écrites chez session-depot sous scellés**. Rappel minimal recommandé S10 = 0,90 (11 sur 12), fausses alertes S11 ≤ 0,10 sur 34 fiches de niveau méthode ([B10] l. 31-32). **Second lecteur** qui lit sans la sortie de l'aiguilleur, puis **adjudicateur** sur les seuls désaccords (pour la mesure M5 du débordement de Kimi, [B10] l. 284). Quatre instances distinctes : concepteur de la consigne, auteur des 12 concrets (qui ne lit pas la consigne), second lecteur, adjudicateur (l. 690).
- **Coût et exigences** : étape É4 « aiguilleur 56 lectures (3,2 dollars), second lecteur 10 (0,6), adjudicateur (0,05) », attendu 4,1, plafond de relais 5,5 ([B10] l. 463) ; exige que session-depot écrive les 12 concrets « selon ce que sa revue de sécurité permet » (dépendance **DEP5**, l. 700).
- **Qui** : session-depot (bras d'attaque) écrit les concrets et tient les lecteurs isolés ; conv-audit n'en lit rien ([B10] l. 690-692).
- **Pourquoi il bloque la porte** : la condition **C7** exige l'aiguilleur « étalonné » ; au défaut R-819 (« pas d'étalonnage »), C7 vaut 0 et la **porte du pré-pilote se ferme à coup sûr** ; la course 2 ne peut alors partir que par l'option **O8 (b)** (course avec aiguilleur non étalonné, réserve écrite partout, mot de Lazar) ([B10] l. 539, 577 ; fiche [P]`pre-pilote-course-2-v1/fiche-decisions-lazar-pre-pilote-2026-10-31-v1.md` § 2).
- **DÉCIDÉ le 1er novembre, 07:23 UTC** : « go recos » → **(b) défaut R-819 déclaré dès maintenant**, C7 à 0, porte du pré-pilote **fermée d'avance et déclarée telle** (DEP5 non confirmée) ([Dbr] R-1028 l. 992). Conséquence : l'aiguilleur ne sera jamais éprouvé avant la course ; la course part par O8 (b) sur mot de Lazar.

---

## 5. Mémoire anti-redite et contrôle des références

### 5.1 Mémoire de la course
- **Constat de la course 1** : 12 **paires** de doublons signalées par les deux juges, toutes entre passe 1 et passe 2 **du même proposeur** → **17 idées distinctes sur 29 fiches** ([Dmain] R-820 l. 1048 ; mêmes 12 paires chez Kimi, R-827). (L'énoncé « 12 fiches redondantes sur 29 » est équivalent : 29 − 17 = 12.)
- **Correction (DÉCIDÉE, codée v53)** : passe 2 nourrie des fiches de la passe 1, fusion mécanique des paires signalées par deux juges ; module `memoire` ([Dmain] R-820 ; [Dbr] R-670 l. 884).
- **Fonctionnement prévu (pré-pilote, M3)** : plongement figé nommé au scellement ; similarité = cosinus de deux fiches entières ; seuil t* fixé sur une partie de calibrage (fausses alertes ≤ S7 = 0,05 visé, 0,10 toléré), scellé avant la vérification ; positifs = 18 paraphrases plantées (lexicales, structurelles, conceptuelles) ; rappel minimal S8 = 0,80 ([B10] l. 274-280, 28-29).
- **Ce qu'elle n'éprouve pas** : une idée déjà publiée ailleurs (ce n'est pas un contrôle d'antériorité) ([B10] l. 274).
- **Double garde de l'axe 7** : (1) la **table de substitution** (l'angle doit différer de l'énoncé le plus proche des huit questions sur au moins deux colonnes : objet, population, métrique, comparateur), lue par Opus 5.5 ; (2) un programme de **bardeaux de mots** contre les huit questions ; « union » = signalé par l'un ou l'autre ; seuil S9 : rappel 0,75, fausses alertes 0,15 ([TI] l. 70 ; [B10] l. 279, 30).

### 5.2 Mémoire du pôle (ESSAYÉE en simulation)
- **Signature prédictive** (ce que l'hypothèse prédit) plutôt que texte : redites manquées 0 à 3,5 % contre 100 % pour le texte ; **hériter la preuve** vaut mieux que refuser ([P]`memoire-v1/lecture-essais-memoire-v1.md`, Verdict).
- Proposeur qui lit la mémoire : 24,0 vraies associations par course contre 12,8 (placebo) et 11,8 (sans mémoire) ; l'avantage disparaît dans un monde sans structure ([P]`memoire-v1/lecture-essais-memoire-piste3-v1.md`, Verdict).
- Démonstration du cycle v5 : 0 découverte en double sur 31 redites avec mémoire, 11 sur 40 sans ([P]`demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md`, Verdict point 3).
- Génération 0 : la « mémoire spectrale » de l'organisme de Gemini est aveugle aux textes réels (rappel 0,000) ([P]`generation-0/synthese-generation-0-v1.md`).

### 5.3 Contrôle des références (antériorité)
- **Vérificateur** : Claude avec recherche (DÉCIDÉ, [Dbr] R-573 l. 787).
- **Pré-pilote, M6** : 8 fiches, 40 références (22 réelles vérifiées sur PDF empreinté, 9 inventées, 9 altérées) ; seuils S13 ≥ 0,90 (inventées détectées), S14 ≥ 0,70 (altérées), S15 ≤ 0,10 (fausses alertes) ([B10] l. 286, 34).
- **M6b** (antériorité publiée **non citée**, 4 fiches, ≈ 1,4 dollar, réserve hors porte, rappel 3 sur 4) : **DÉCIDÉ D-g (b)** ([Dbr] R-718 l. 932 ; [B10] l. 287).
- **Après la course** : aucun angle de l'axe 7 n'entre dans une note sans **deux recherches d'antériorité sur PDF empreinté** (un sous-agent neuf, puis une recherche adverse par un modèle d'un autre fournisseur) ; « non trouvé » n'est jamais « vierge » (R8) ([TI] l. 154).

---

## 6. Les juges

- **Qui** : étage 1 = **analyseur programmé** (il décide K5 : format des antériorités, pages des chiffres d'HELIOS, données dans la liste D) ; étage 2 = **Kimi K3.1 Pro et Argon en notation croisée + Opus 5.5 troisième juge sur toutes les fiches** (arbitre des désaccords) ([TI] l. 46 ; [Dbr] R-577, R-578 l. 791-792).
- **Ce qu'ils notent** : grille **binaire** K1 à K5 contre les listes fermées : K1 livrables de l'axe présents ; K2 source d'avantage dans L avec coût de reproduction chiffré (pièce, page), ou antériorité la plus proche et élément absent nommés ; K3 prédiction chiffrée et signée (rappel à 1 % de fausses alertes par famille pour une détection) ; K4 critère de mort à seuil numérique, première expérience sur processeur ou données déjà payées ; K5 antériorités au format, chiffres d'HELIOS conformes. **« Notable » = K1 à K5 vrais.** Classement par axe : facultatifs passés, puis coût croissant ([TI] l. 46). Agrégation des trois juges : règle de la v53, à défaut « notable chez au moins deux des trois » ([B10] l. 309).
- **Étalonnage sur témoins (pré-pilote, M1)** : classes plantées P (notable), C (creuse mais conforme : notable sous la grille), N1 à N4 (chacune viole un item K1 à K4 entre deux champs nommés), G (défaut que seul l'étage 1 doit voir) ([B10] l. 673-683). Seuils recommandés : exactitude équilibrée S1 ≥ 0,80, rappel S2 ≥ 0,70, plancher S3 0,70, accord S4 (kappa de Fleiss ≥ 0,45) ([B10] l. 22-25). Prédiction : Opus 0,90, Argon 0,85, Kimi 0,80 ; porte des juges seule 0,38 ([B10] l. 242, 8).
- **Course 1** : 6 témoins tenus chez Opus et Argon ; accord de rang entre juges **0,12** ; témoins plus courts que toutes les fiches (épreuve plus faible qu'annoncé) ; Kimi échoue à un témoin ; **auto-préférence d'Argon ≈ 1,8 point sur 15** ([Dmain] R-811, R-827).
- **Ce qu'ils ne font pas** (à dire clairement) : l'étage 2 ne note que la **cohérence entre champs** ; **ni « décisif » ni « inédit » n'est noté** ([TI] l. 46) ; ils ne jugent pas la valeur scientifique (« la classe C le rend visible », [B10] l. 234 A4) ; ils n'exécutent rien ; ils ne vérifient pas l'antériorité ; ils ne testent pas la plausibilité (« très plausible » est porté par les tests de mort, « inédit » par l'antériorité sur PDF, [B10] l. 221) ; l'auto-préférence n'est plus mesurée (M2 retirée, [Dbr] R-634 l. 848).
- **À ne pas confondre** avec le **juge figé du pôle**, qui n'est pas un modèle de langage : pari séquentiel, inégalité de Ville, inférence universelle contre un nul composite, garantie de 5 % de fausses promotions, règle de fausses découvertes entre hypothèses, témoins plantés ([P]`programme-conception-organisme-v7.md` l. 23-29). Validé en simulation : 18 contrôles fatals à 0 ou 1 sur 1 000 ([P]`experience-1-juge/lecture-experience-1-v1.md` ; nul des filles v2 : 13 contrôles à 0 sur 1 000, [P]`nul-des-filles-v2/lecture-experience-2-v1.md`).

---

## 7. Le bisociateur et ses trois bras

- **Principe** : la *bisociation* (Koestler 1964, *The Act of Creation*, **SUPPOSÉ**, non vérifié sur PDF) = percevoir une situation dans deux « matrices » habituellement incompatibles ; la fertilité naîtrait de leur collision ([P]`bisociation-niches-v1/revue-biblio-fertilite-v1.md` l. 44). Dans le pôle, la recombinaison bisociative venait d'une proposition de Gemini, avec filtre de compatibilité des contraintes ([P]`conception-pole-scientifique-v1.md` l. 3-5, 29-32).
- **Statut** : **module exploratoire** ajouté à l'organisme et utilisé dans la course 2 avant tout verdict de ses tests ; sorties **étiquetées exploratoires** (dans le registre seulement), **jugées à l'aveugle** avec les autres, **comptées à part**, sans revendication (DÉCIDÉ, [Dbr] R-601 l. 815).
- **Chronologie des bras** (la plus récente prévaut) : R-634 un seul bras (basique), Gu-Krenn retiré → R-635/R-636 Gu-Krenn gardé → R-638/R-639 le basique remplacé par un bras nouveau appelé **« bras méta »** → R-642/R-643 **basique gardé pour comparaison** : **trois bras, une paire par session chacun** ; bras hasard retiré ([Dbr] l. 848-857).
- **Fusion** : Kimi écrit **une fiche par paire**, sous une consigne de fusion figée, identique pour les trois bras, sans nom de bras ni de règle, au niveau méthode, au format du texte I ; la fusion repasse par l'aiguilleur puis les trois juges, chaque appel isolé et anonyme ; clé des bras scellée jusqu'au verdict ([B10] l. 308).
- **Lectures d'étiquettes** : deux lecteurs neufs qui ne connaissent ni les règles ni les bras, trois lectures séparées par fiche (concepts, vocabulaire Gu-Krenn, niches et structures) ([B10] l. 295).

### 7.1 Bras basique — « loin en domaine, proche en concept » (R-601, R-642, R-643)
- Domaine = indicateur (axe, case) déclaré ; concept = étiquettes d'une liste fermée posées par deux lecteurs ; score = (1 − cos²domaine)^8,5 × (Jaccard des concepts + 0,05), forme du préenregistrement de bisociation v2 scellé ; dans une seule case la règle se réduit à « deux axes différents, concepts les plus partagés » ([B10] l. 297, D-e PROPOSÉ l. 51).
- Antériorité de la règle : non trouvée telle quelle ; voisin le plus proche Sourati et Evans 2023 (collision partielle) ([Dbr] R-589 l. 803).
- Épreuve sur mondes inventés (bisociation à deux espaces v2, scellée) : **verdict « non concluant »** (critère V5 faux), version 3 en brouillon ([Dbr] R-660 l. 874, R-701).

### 7.2 Bras Gu-Krenn (R-619, R-635, R-636 ; D-j)
- Source : Gu et Krenn 2024, « Impact4Cast », prédiction d'impact de paires de concepts **jamais reliées** dans un graphe de concepts (optique et physique quantique) ; le PDF **est versé sur `main`** ([main]`docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md` § 0). **Écart** : [B10] l. 75 dit « aucun PDF versé » ; la note de `main` (31 oct., 02:15-03:00 UTC) est plus récente.
- **Pourquoi un substitut** : leur vocabulaire de 37 960 concepts **ne couvre pas le contrôle des intelligences artificielles** (sabotage, sonde linéaire, conscience d'évaluation… absents ; « probe », « alignment » n'y ont qu'un sens de physique) (même note § 5). Le code v56 n'accepte que le mode « substitut » ([N]`orchestrateur-v56/LISEZMOI-orchestrateur-pole-v7-v56.md` table, CL20-10).
- **Substitut inspiré de Gu et Krenn** : note d'une paire de fiches = part des paires de concepts **jamais reliées** et **toutes deux actives** ; « reliées » = au moins une œuvre portant les deux concepts entre 2015 et la coupure du 30 juin 2026 ; « actif » = au moins 5 œuvres dans les trois ans avant la coupure ; vocabulaire = étiquettes portées par au moins 20 œuvres ; source = moisson OpenAlex (seuil **S31**, SUPPOSÉ, à essayer avant le gel) ([B10] l. 49, 298).
- Condition de reproduction préalable : relâchée (recommandation R-635), **renvoyée au collisionneur (D-j, nœud N3)** ([Dbr] R-719 l. 933).

### 7.3 Bras méta — « trou à structure commune », version 1 (R-638, R-639)
- Profil cherché : deux fiches de **niches différentes** qui **communiquent peu**, partagent une **structure forte** (objet mathématique, méthode, jeu de données, protocole), à un **éloignement non extrême** (cloche d'Uzzi, SUPPOSÉ) ; le **désaccord** entre affirmations centrales est lu à part, hors score ([B10] l. 299-304).
- **Six niches** (grille proposée) : détection séquentielle ; lecture des activations ; anomalies hors distribution ; moniteurs et protocoles ; bornes et théorie ; science de l'évaluation ([P]`pre-pilote-course-2-v1/annexe-bras-meta-v1-brouillon4.md` § 1). **20 structures** nommées en quatre types (§ 3). Canal (0 à 3) et éloignement (1 à 5) : tables écrites à la main, SUPPOSÉ (§ 2, § 5).
- **Paramètres à la main**, déclarés SUPPOSÉ, dans une **annexe séparée** contre-lue, approuvée par Lazar (S28, S29) ; « transition de phase » **suspendue** jusqu'à l'épreuve E2′ ([Dmain] R-878 l. 1107 ; [B10] l. 234).
- **Problème ouvert (nœud N4, constat CA1-05)** : à 6 fiches, un lot contient au moins une paire du profil avec ≈ 0,27 seulement (0,55 à 10 fiches) ; le pré-pilote éprouverait surtout le **repli** ; recommandation de l'annexe : bande d'éloignement [2 ; 4] (0,49 et 0,84), confiance 0,55 (annexe brouillon 4, résumé l. 26-29, § 0.3).
- État : brouillon 4 contre-lu « soumettable après corrections » ; brouillon 5 et erratum v2 à écrire ([Dbr] R-1030, R-1032 l. 994-996). DEP10 : Lazar doit dire si les synthèses du collisionneur (questions 4 à 7) tiennent lieu des « verdicts » exigés (annexe § 0.0).

### 7.4 Combien de fusions, et pourquoi une seule paire au pré-pilote
- **Course 2 : 24 fusions** = une paire par bras et par proposeur dans chaque sous-session (3 bras × 2 proposeurs × 4 sous-sessions), soit **8 par bras** (DÉCIDÉ, GO-2026-10-31-04 ; [B10] l. 41 ; devis v6 l. 239 ; « 12 par bras » est périmé, [Dbr] R-1025 l. 989).
- **Pré-pilote : k = 1 paire par bras (3 fusions)** ([B10] S23 l. 42). Raisons : objectif « **produire, pas mesurer** » (Lazar : « juste des idées originales mais très plausibles ») et économie ; le pré-pilote éprouve la **chaîne** (paire → fusion → aiguilleur → juges) et **aucune comparaison entre bras n'est lue** ([Dbr] R-632, R-634 l. 846-848 ; [B10] l. 293).
- Questions liées (fertilité, allumage) : l'**allumage** n'est pas un paramètre mais une grandeur à mesurer entre générations (une fusion qui en engendre d'autres) ; analogie des **ensembles autocatalytiques** (Kauffman ; Hordijk et Steel, SUPPOSÉ) ; question 7 posée au collisionneur ([Dbr] R-642, R-643).

---

## 8. Le collisionneur

- **Espèces** (version 4 et suivantes) : A **Fable 5.1**, B **Opus 5.5** (Anthropic), C **Gemini Argon** (Google), D **Kimi K3.1 Pro** (Moonshot, ajouté le 30 oct.) ([Dmain] R-826 l. 1054 ; question des nœuds v12 [P]`collisionneur-noeuds-31-octobre-v1/question-noeuds-decisionnels-collisionneur-v12.md`). Certaines questions ont été rendues sans Kimi (questions 6 et 7) ou sans Fable.
- **Tours** : **tour 1 — avis propre** (option, confiance, pire cas et garde, option manquante, pièce qui trancherait) ; **tour 2 — attaque des recommandations** des auteurs, servies dans un second envoi après le tour 1 (« tenue », « tenue sous condition », « renversée », « aucune option ne tient », « indécidable sans la pièce X ») (question v12, l. 25-27).
- **Lecture** : critères de lecture **scellés avant l'ouverture des cellules** ; **synthèse par un lecteur neuf** qui n'a pas écrit les critères ; décompte d'accords, convergences nées de la critique, divergences ; relecture indépendante possible ([Dmain] R-927, R-934, R-939 ; [Dbr] R-1023 l. 987).
- **À quoi il sert** :
  - **nœuds de décision** de Lazar (« demande au collisionneur pour tous les nœuds décisionnels » ; consigne permanente : proposer le collisionneur dès qu'une confiance est ≤ 0,6) ([Dbr] R-719 l. 933) ;
  - **conception** de l'organisme : choix du moteur (« voie hybride ancrée sur notre noyau », 9 cellules, 7,82 dollars) ([Dmain] R-525 l. 749) ; bisociation (questions 1 à 7 : chapelles, niches, fertilité, apprendre, causes, identification, allumage) ([P]`bisociation-niches-v1/`) ;
  - **idées** : oui, indirectement — ses avis ont produit ou orienté des préenregistrements (bisociation à deux espaces, épreuve d'identification « semi-réel », arène coévolutive) et l'analyse des protocelles (§ 10). Ce n'est pas un générateur de fiches de course.
- Coûts relevés : tour des nœuds v12 23,87 dollars ; tour 2 des protocelles 8,29 dollars ([Dmain] R-926, R-937).

---

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

## 10. Résultats déjà obtenus

- **Course 1, tentative 1** (29 oct.) : arrêtée à 10:48 UTC, refus d'Opus 5.5 proposeur puis bascule automatique vers Opus 4.8 sans GO ; aucune fiche validée ([Dmain] R-764 l. 992).
- **Course 1, tentative 2** (30 oct.) : **29 fiches validées** (3 en quarantaine), juge Fable refuse ; rejugées par Opus 5.5 et Argon : **27 éligibles sur 29**, 15 de Fable, 14 d'Argon, 5 et 5 dans les dix premières ; accord de rang 0,12 ; totaux serrés (12,0 à 12,5 sur 15 dans les dix premières) ; **17 idées distinctes** (12 paires de doublons) ; auto-préférence d'Argon ≈ 1,8 point ; coût ≈ 37 dollars ([Dmain] R-804, R-811, R-820, R-827). « Notable » n'existait pas encore (classement par totaux ; critères de la course 1 décrits comme « avantage décisif ou approche inédite », [P]`question-mere-course-v1/question-mere-course-ideation-v3.md` l. 42-46).
- **Ce qui est sorti de la course 1** : des corrections d'instruments (mémoire anti-redite, témoins de longueur comparable, relais Kimi v3, notation croisée, aiguillage) ; **aucune fiche de la course 1 n'est tracée comme devenue hypothèse ou expérience du programme** dans ce que j'ai lu ; les fiches sont sous `donnees/` et non lues par conv-audit (règle). Relancer la course 1 : déconseillé (R-737 l. 951).
- **Démonstrations du cycle v5** : seuil par fiche (vraies filles refusées à tort 31 → 4) ; marchepieds 282 contre 212 vraies filles dans le monde fécond, 236 contre 245 dans le monde plat ; mémoire 0 double sur 31 ; aucune fausse promue. **Mécanisme vérifié, pas une découverte** ([P]`demonstration-cycle-v5/lecture-demonstration-cycle-v5-v1.md`).
- **Génération 0** : 5 / 10 / 3 (ci-dessus) ; deux correctifs utiles retenus (normaliser les hachages ; diversité de domaine dans le tirage).
- **Protocelles** : analogies (allumage par branchement, parasites, fusions inachevées) ; tour 2 du collisionneur synthétisé ; une règle passée dans le code (fusions inachevées archivées à part, jamais réutilisées).
- **Idées de l'organisme ou de ses brainstorms devenues préenregistrements ou pilotes** (toutes exploratoires, aucune porte franchie) : bisociation à deux espaces v2 (scellée, validation non concluante, v3 en brouillon) ; épreuve d'identification « semi-réel » (brouillon 7, [Dbr] R-1033) ; reproduction et test hors échantillon de Gu-Krenn (préenregistrement v2 sur `main`) ; pilote synthétique « mélange d'équilibre » (arène coévolutive P-041, brouillon 4). Ces pistes viennent des questions de Lazar et du collisionneur, pas de fiches de course.
- **Aucune porte franchie** ; critères de G0 prouvés : 1 et 5 seulement (`registres/etat.md` l. 57).

---

## 11. Pré-pilote et course 2

### 11.1 Décidé
- **Pré-pilote : plafond 50 dollars, arrêt d'étape 45**, plafonds de relais du brouillon 5 souples pour les étapes protégées — **GO-2026-10-31-03, échéance 7 novembre** ([B10] l. 3, 36).
- **Course 2 : plafond total 160 dollars, pré-pilote compris, séquencé, trois bras, 24 fusions** — **GO-2026-10-31-04, échéance 14 novembre** ([B10] l. 3, 701 ; [Dmain] R-878).
- Course 2 = **génération 1** ; brainstorm en parallèle (option A) ; **machine jetable** sans secret pour les tests de mort ([Dbr] R-637, R-640).
- Objectif : **produire des idées inédites et très plausibles, pas mesurer l'organisme** ([Dbr] R-632, R-634).
- Juges, proposeurs, aiguillage avant juges, tableau minimal, notation croisée gardée, bisociateur à trois bras, antériorité chez Claude.
- D-g (b) M6b ; D-h (a) attendre l'annexe du bras méta ; D-i (2) ([Dbr] R-718, R-719).
- Aiguilleur : défaut R-819 déclaré, porte fermée d'avance ([Dbr] R-1028).
- Bac à sable de la course : machine jetable par liste blanche dans le code v56.

### 11.2 Ce que mesure le pré-pilote ([B10] l. 10, 221)
Obéissance des trois juges à leur grille sur témoins nets (M1) ; détection des redites **du lot** (M3) ; aiguillage du concret (M4) ; tenue au niveau méthode de Kimi proposeur (M5) ; références inventées ou altérées (M6) ; antériorité non citée sur 4 fiches (M6b, réserve) ; consommation (M7) ; cloisons du tableau (M8) ; chaîne de bisociation sur une paire par bras (M9). **N'éprouve pas** : « très plausible » (tests de mort), l'antériorité non citée hors M6b, aucun taux de fausse élimination d'une bonne idée. Issue la plus probable, aux valeurs prédites : **nœud sans départ (0,63)** ; porte ouverte d'emblée 0,17 ; **0 au défaut de l'aiguilleur** — désormais le cas décidé ([B10] l. 7).

### 11.3 Ce qui reste
- **Décisions de Lazar** : S1 à S31 sauf S17 ; L1 à L7 sauf L4 ; D-e, D-f ; D-j (au collisionneur) ; DEP4 (confidentialité : envoyer des fiches inventées chez Moonshot et Google) ; DEP10 (les synthèses du collisionneur valent-elles verdicts ?) ; mot sur O8 (b) pour faire partir la course ([B10] l. 57, 699-705 ; fiche des décisions § 1-3).
- **Pièces** : annexe du bras méta (brouillon 5, contre-lecture, approbation, scellement) ; essai de S31 sur la moisson ; liste scellée des sources de M6b (DEP2c) ; consigne figée des juges et de l'aiguilleur ; analyseur de l'étage 1 (**n'existe pas**, DEP3) ; commandes de porte de plafond des relais Kimi et Claude (**n'existent pas** : A15 refuse tout lancement réel) ; lecture du GO de 160 « séquencé » par le code (à trancher) ([N] LISEZMOI v56 § 6).
- **Contrôles** : contre-lecture 5 du préenregistrement par un modèle ni Opus ni Fable ; scellement ; contre-lecture CL21 du code v56 ; essais de bac réel sur la machine du run ; lancement avant le 7 novembre, sinon ligne de GO nouvelle.
- **Contexte** : le 31 octobre ≈ 18:30 UTC, pause à la demande du coordinateur du projet (le canal touchait aux bras d'attaque), levée par Lazar le 1er novembre ([Dbr] R-1021, R-1022 l. 985-986).
- Sujet **suspendu** : « s'inspirer de la recette d'Avalon pour l'auto-organisation de l'organisme » (non traité ici).

---

## 12. Glossaire (une ligne en clair ; surnom parlant proposé)

**Règles gelées du dépôt**
- R1 — préenregistrement scellé avant toute expérience décisive. *« Gel d'abord »*
- R2 — contre-lecture par un sous-agent neuf qui n'a pas écrit la pièce. *« Œil neuf »*
- R4 — un résultat trop propre déclenche le même audit qu'un mauvais. *« Trop beau = suspect »*
- R5 — toute garde testée sur un cas sain et sur un artefact. *« Garde éprouvée »*
- R7 — aucun chiffre de littérature sans PDF empreinté, page citée. *« Page à l'appui »*
- R8 — une zone vierge est une question, pas une découverte. *« Pas de faux trou »*
- R13 — verdict de porte prononcé par un lecteur neuf qui applique les critères gelés. *« Arbitre neuf »*

**Décisions R-xxx utiles** (registre précisé)
- R-339 [Dbr] — sorties adversariales au niveau méthode, jamais la recette. *« Méthode, pas recette »*
- R-597 [Dmain] — lanceur du bras d'attaque arrêté par un classifieur ; aucune relance. *« Bras d'attaque gelé »*
- R-575 [Dbr] — tout détail d'attaque concret est scellé chez session-depot. *« Coffre du concret »*
- R-819 [Dmain] — aiguillage avant les juges ; défaut « pas d'étalonnage » de l'aiguilleur. *« Aiguilleur non étalonné »*
- R-567 [Dbr] — Kimi remplace Claude comme proposeur en course 2. *« Kimi propose »*
- R-573 [Dbr] — antériorité vérifiée par Claude, jamais par Kimi. *« Claude vérifie les sources »*
- R-577, R-578 [Dbr] — juges Kimi et Argon croisés + Opus troisième. *« Jury croisé »*
- R-598 [Dbr] — tableau minimal partagé dans la même case. *« Tableau des titres »*
- R-601 [Dbr] — bisociation ajoutée comme module exploratoire, comptée à part. *« Fusion à l'essai »*
- R-632, R-634 [Dbr] — produire des idées, pas mesurer l'organisme ; une paire par bras. *« Produire d'abord »*
- R-635, R-636 [Dbr] — Gu-Krenn gardé comme bras. *« Garder Gu-Krenn »*
- R-638, R-639 [Dbr] — bras nouveau « trou à structure commune » nommé bras méta. *« Bras méta »*
- R-642, R-643 [Dbr] — bras basique gardé pour comparaison : trois bras. *« Trois bras »*
- R-640 [Dbr] — tests de mort sur machine louée jetable. *« Machine jetable »*
- R-477, R-636 [Dbr] — « les agents qui testent » : couche 3 non construite, tests de mort non activés. *« Testeurs en attente »*
- R-776 [Dmain] — tests de mort, puis carte graphique par fiche, puis IA scientifique externe en parallèle. *« Trois étages de test »*
- R-878 [Dmain] — GO pré-pilote 50 et course 160 ; « transition de phase » suspendue. *« Plafonds du 31 »*
- R-1028 [Dbr] — défaut de l'aiguilleur déclaré : porte fermée d'avance. *« Porte fermée exprès »*

**Seuils du pré-pilote S1 à S31** ([B10] l. 20-56) — *groupés*
- S1-S4 juges (exactitude, rappel, plancher, accord). *« Notes du jury »*
- S5 retiré (biais de source). S6 fidélité du rendu des témoins. *« Rendu fidèle »*
- S7-S9 mémoire et double garde de l'axe 7. *« Anti-redite »*
- S10-S11 aiguilleur (rappel, fausses alertes). *« Tri du concret »*
- S12 débordement de Kimi proposeur. *« Kimi reste en méthode »*
- S13-S15 antériorité (inventées, altérées, fausses alertes). *« Fausses références »*
- S16 écart de coût toléré ; S17 plafond 50 / arrêt 45 (gelé). *« Budget »*
- S18-S20 forme des témoins et effectifs. *« Témoins crédibles »*
- S21 longueur des titres et résumés du tableau. *« Une ligne »*
- S22 24 fusions (fixé par GO) ; S23 une paire par bras. *« Nombre de fusions »*
- S24 accord des lecteurs de concepts (bras basique). *« Concepts lus pareil »*
- S25-S27 règle Gu-Krenn (m paires, reproduction retirée, couverture). *« Réglages Gu-Krenn »*
- S28-S29 accord et paramètres du bras méta (annexe). *« Réglages méta »*
- S30 rappel de l'antériorité non citée (M6b). *« Source oubliée »*
- S31 paramètres du substitut de Gu et Krenn. *« Substitut Gu-Krenn »*

**Décisions D-e à D-j** ([B10] l. 51-56)
- D-e — lire « domaine » et « concept » (bras basique). *« Définir domaine »* (ouvert)
- D-f — modèles des rôles neufs (tiers metteur en forme, relecteur). *« Qui met en forme »* (ouvert)
- D-g — ajouter 4 fiches d'antériorité non citée : (b) décidé. *« Test de l'oubli »*
- D-h — attendre l'annexe du bras méta avant le gel : (a) décidé. *« Attendre le méta »*
- D-i — plan des fonds : (2) 28 + 4 rendus appariés, décidé. *« Fonds doublés »*
- D-j — Gu-Krenn sans reproduction préalable : au collisionneur. *« Gu-Krenn sans preuve »*

**Lectures L1 à L7** — règles d'interprétation de l'auteur à confirmer : L1 garder la passe « tableau » ; L2 garder la « table seule » de l'axe 7 ; L3 désaccord hors du score méta ; L4 sans objet ; L5 fusions retirées lues sur les paires ; L6 S27 lu comme réserve ; L7 brouillon 3 accepté sans contre-lecture. *« Lectures à valider »* (attention : ne pas confondre avec **L**, liste fermée des sources d'avantage).

**Conditions de porte C1 à C14** (le brief disait C1 à C13 : il y en a **14**, [B10] l. 533-546) : C1-C3 juges ; C4 étage 1 ; C5 forme des témoins ; C6 mémoire ; **C7 aiguilleur** ; C8 Kimi proposeur ; C9 antériorité ; C10 coût de la course sous 160 ; C11 tableau ; C12 bisociation ; C13 arrêts et mesures complets ; C14 audit de symétrie. *« Feux de départ »* (homonymes : C1-C4 = classes de fiches trop concrètes ; C = témoin creux ; C-17 = restriction du noyau).

**Mesures M1 à M9** : M1 juges ; M2 retirée ; M3 redites ; M4 aiguilleur ; M5 débordement de Kimi ; M6 antériorité (+ M6b) ; M7 consommation ; M8 tableau ; M9 bisociation. *« Instruments »* (homonyme : M = liste fermée des métriques).

**Options O0 à O15** — issues possibles si une condition échoue ; **O8** = si l'aiguilleur échoue : (a) nouvelle consigne et nouvel essai, ou (b) au défaut R-819, course avec aiguilleur non étalonné, réserve partout ([B10] l. 577). *« Départ sous réserve »*

**Dépendances** : **DEP4** — relais des modèles plafonnés et mot de Lazar sur la confidentialité (fiches chez Moonshot et Google). *« Relais et confidentialité »* ; **DEP5** — bras d'attaque : 12 concrets, second lecteur, adjudicateur, mot sur l'étalonnage. *« Concrets pour l'aiguilleur »* ; **DEP10** — annexe du bras méta scellée et approuvée. *« Annexe méta »* ; DEP3 — analyseur de l'étage 1 et programmes (absent). *« Analyseur manquant »* ; DEP11 — étage de tests de mort (pas au pré-pilote). *« Testeurs »*

**Arrêts A1 à A21** ([B10] l. 608-628) : **A1** — règle budgétaire : on ne lance pas une étape si cumul + plafond de l'étape + reste attendu dépasse 50, ou si le cumul atteint 45. *« Coupe-budget »* ; **A15** — décision ou ligne de GO manquante ou échue : aucun lancement. *« Pas de GO, pas de départ »* (homonyme : A1 à A7 = hypothèses de travail du même texte, l. 234).

**Étapes É0 à É9b** : **É0** — étape de départ sans dépense : gardes éprouvées, consignes et code empreintés, annexe méta vérifiée, mode de Gu-Krenn déclaré ([B10] l. 413). *« Contrôle avant décollage »* ; É1 rédaction ; É2 passe 1 de Kimi ; É3 rendus ; É4 aiguilleur ; É5 relecteur ; É6 juges ; É7 passe « tableau », étiquettes, fusions, table de l'axe 7 ; É8 paraphrases ; É9 antériorité ; É9b antériorité non citée.

**Autres termes**
- **Axes** — chapitres de la question servie (1 battre HELIOS ; 2 ce que le domaine retiendrait ; 3 failles ; 4 universalité ; 5 théorie ; 6 attaque à part ; 7 angles non occupés ; 8 robustesse adaptative proposé). *« Chapitres »*
- **K1 à K5** — items binaires de la grille des juges. *« Cases à cocher »*
- **Notable** — fiche dont K1 à K5 sont vrais ; dit la conformité, pas la valeur. *« Conforme »* (surnom plus honnête que « notable »)
- **Fonds** — squelette d'un témoin planté (pré-pilote) ; « le fonds » = financement. *« Squelette »*
- **Témoins** — fiches plantées à vérité connue (P, C, N1-N4, G). *« Fiches pièges »*
- **Niches** — six communautés de méthode du bras méta. *« Familles de méthode »*
- **Structures** — 20 objets, méthodes, jeux de données ou protocoles partagés. *« Outils communs »*
- **Fusion** — fiche écrite par Kimi à partir d'une paire choisie par un bras. *« Croisement »*
- **Bisociation** — rapprocher deux cadres éloignés pour faire naître une idée (Koestler, SUPPOSÉ). *« Collision d'idées »*
- **Bras méta / Gu-Krenn / basique** — trois règles de choix de paire. *« Trou commun » / « Jamais reliés » / « Loin mais proche »*
- **Substitut inspiré de Gu et Krenn** — leur idée de paires jamais reliées, sur notre moisson. *« Gu-Krenn maison »*
- **Aiguilleur** — trieur méthode / concret avant les juges. *« Douane »*
- **Tableau minimal** — titres et résumés d'une ligne partagés dans une case. *« Tableau noir »*
- **Tests de mort** — exécution automatique du critère de mort d'une fiche. *« Épreuve du feu »*
- **Collisionneur** — quatre modèles de trois fournisseurs, deux tours, synthèse par lecteur neuf. *« Conseil des quatre »*
- **Pôle / organisme** — l'ensemble ; **juge figé** — juge statistique du pôle. *« Balance »*
- **Protocelles** — papier de Lazar ; source d'analogies (allumage, parasites). *« Analogie cellulaire »*
- **Moissonneur** — récolte arXiv et OpenAlex. *« Cueilleur »*
- **GO** — feu vert de dépense écrit au registre sur le mot de Lazar. *« Feu vert »*
- **HELIOS** — système publié de référence à battre (axe 1). *« Le rival »*
- **G0, G1** — portes de phase du programme. *« Portes »*
- **Session-depot / conv-audit** — exécutant qui tient clés, données et bras d'attaque / concepteur-auditeur. *« Le dépôt » / « L'architecte »*
- **N1 à N13** (collisionneur) — nœuds de décision posés au collisionneur (N3 Gu-Krenn, N4 bras méta, N11 reconduction des bras…). *« Questions au conseil »* (homonyme : N1-N4 classes de témoins ; N-0xx décisions de fond du programme)
- Codes de constats (CP, VB, CA, CL suivis de numéros) — renvois aux points relevés par un contre-lecteur. *« Remarques du relecteur »*

---

## Trous et réserves

- Les fiches et classements de la course 1 sont sous `donnees/` : **non lus** ; aucune idée de la course 1 n'est tracée vers le programme.
- Première moisson réelle par le moissonneur : **aucune trace** ; seule la moisson en vrac de R-863 existe.
- Duel des proposeurs : aucune trace de lancement. Carte des « chapelles » : aucune trace (annexe § 0.0).
- Collisionneur : code et procédure non relus ; espèces décrites d'après [Dmain] R-826 et la question v12.
- Textes II, III, bras d'attaque : non ouverts (règle de sécurité).
- Sujet « Avalon » : suspendu, non traité.
- Contradictions relevées : PDF de Gu et Krenn (absent selon [B10], présent sur `main`) ; « 12 fusions par bras » périmé (8) ; C1 à C14 et non C13 ; numérotation R-xxx propre à chaque registre.
