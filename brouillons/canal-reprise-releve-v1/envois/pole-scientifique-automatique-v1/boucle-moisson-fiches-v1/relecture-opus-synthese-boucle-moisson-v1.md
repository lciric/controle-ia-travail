# Relecture neuve de la synthèse du collisionneur « boucle itérative moisson ↔ fiches ↔ bisociateur » (tour 1) — v1

## En-tête

- **Relecteur** : sous-agent neuf de la lignée conv-audit, modèle **Opus 5.5** (`claude-opus-5-5`), règle R-746 du registre de conv-audit (relecture neuve d'une synthèse de session-depot). Je n'ai écrit ni la question, ni les critères, ni les faits, ni aucune cellule, ni la synthèse, ni l'antériorité.
- **Famille** : je suis de la lignée Opus, comme l'espèce B de ce run (Opus 4.6), et du même fournisseur (Anthropic) que l'espèce A (Fable 5.1) et que le lecteur de la synthèse (Fable 5.1). Les deux voix hors Anthropic sont C (Argon, Google) et D (Kimi K3.1 Pro, Moonshot) ; je les ai relues avec ce risque en tête (voir RB-12).
- **Date UTC** (`date -u`, relevée après la lecture complète, avant l'écriture) : `Sun Nov 1 15:48:30 UTC 2026`.
- **Lecture seule** : aucun commit, aucun compagnon `.sha256`, aucun fichier existant modifié, rien lu sous `donnees/`, aucun `git fetch`, aucun appel de réseau ni de modèle. Les PDF ont été lus par extraction de texte locale (`pdftotext`), copies dans mon espace de travail.
- **Non lus** : les douze cellules du run, `faits-boucle-moisson-v1.md`, l'état et le journal du run (tous sous `donnees/`, non versés) ; l'état des lieux de Gu et Krenn (pièce 3, sur `main`, absent de cette branche) ; l'annexe du tour 2.

### Empreintes SHA-256 recalculées (toutes conformes à leur compagnon ou à l'abrégé donné)

| Fichier | Empreinte |
|---|---|
| question v1 `…/boucle-moisson-fiches-v1/question-collisionneur-boucle-moisson-fiches-v1.md` | `72b4f14980ce259b0f2836f7162bbfb33377227b0da05f511c19774c17d7ae76` |
| synthèse `…/scratchpad/sd-syntheses/synthese-boucle-moisson-v1.md` | `48a514de40b5baa95423e77e17e09a0be566312faa9e05f350296b03968bf856` |
| critères `…/scratchpad/sd-syntheses/criteres-lecture-boucle-moisson-v1.md` | `3d0dc1051492fa9c66d2f0f12e8ff8a2df8b17b63444297195bd6e0f55147cc5` |
| antériorité `…/boucle-moisson-fiches-v1/anteriorite-boucle-moisson-fiches-v1.md` | `a953879ab6a96073909400be138bfbef603a57351a275837323c7e7370b2c2a8` |
| dossier factuel `docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md` | `0751fc8cf4aa0a9eaccb23d80cb06220fa3db9805092bd1d854bc68fce7ae250` |
| SciMuse v4 `docs/sources/pdf/boucle-moisson-fiches-v1/arxiv-2405.17044v4.pdf` | `fcb49a059e17a25c351153a8022717aa594ddc279f6e276e204f1fbe9ce32af4` |
| HindSight `…/arxiv-2603.15164v2.pdf` | `86471129a50c9ad76b136971c977a4ccb6cf28113c4bca646fb7f5998ee78ad3` |
| MAGenIdeas `…/arxiv-2604.20548v1.pdf` | `4e998f5a5dad38427e5f465c27f725d29b1ae6b4991b5b297464ba7f6948f212` |
| MiroGraph `…/arxiv-2610.25281v1.pdf` | `4b32d77139a21965f6cd5fcab6085db5f2893cc82a6ad60f91c8ab8f5dc62d3c` |

### Conventions

Espèces : **A** = Fable 5.1 (Anthropic) ; **B** = Opus 4.6 (Anthropic) ; **C** = Argon (Google) ; **D** = Kimi K3.1 Pro (Moonshot). Sous-tours : T1 = avis propre, T2 = critique croisée, T3 = réponse aux critiques ; « A-T3 15 » = cellule de réponse de A, point 15, tel que la synthèse le cite. « l. N » sans autre précision = ligne du dossier factuel. « Q1 » à « Q7 » = volets de la question. Les étiquettes de divergence (« Q6-a »…) sont celles de la synthèse. Les codes internes sont développés à leur première apparition dans chaque section.

---

## Verdict en une phrase

**Tenue sous condition** : les positions par espèce et les citations que j'ai pu recouper sur le dossier factuel tiennent, et les dix recalculs de la synthèse sont exacts, mais **aucun des décomptes ne se reproduit** à partir du texte de la synthèse elle-même (accords, convergences, divergences résolues et maintenues, apports seuls), trois accords comptés comme indépendants sont soufflés par la question ou nés de la critique, et la liste servie au tour 2 **perd quatre divergences** et **range A du mauvais côté** sur « Gu-Krenn tel quel » — à corriger par erratum avant tout tour 2.

---

## Constats

### RB-01 — Décompte des accords : « 7 larges » annoncés, huit énumérés ; double compte probable — **majeure**

La ligne du décompte annonce « 11 accords, **7 larges** » puis énumère huit accords larges : (1) Q1 état minimal en champs fermés ; (2) Q1 « affiner » sans capteur = « reformuler » ; (3) Q2 dérivation et garde mécaniques ; (4) Q3 séparer les types de paires ; (5) Q4 uniforme avec arrêt ; (6) Q5 circularité ; (7) Q5 témoin « allocation de ressources » ; (8) Q7 course 2 d'abord ; plus trois accords à deux. 8 + 3 = 11 : le total ne tient que si les deux énoncés de Q1 comptent pour deux, alors que le volet Q1 les écrit comme **un seul** accord (« Large à quatre en T1 : état minimal en champs fermés, et sans capteur "affiner" = "reformuler" »). Soit 7 est faux, soit Q1 est compté deux fois.

Plus grave : la définition donnée par la synthèse (« même position en T1, au moins deux espèces ») n'est pas respectée pour deux accords :
- **Q3 « séparer les types de paires »** : en T1, seules C et D ; A rejoint en T3 (A-T3 15) et B par sa critique de D (B-T2 sur D (c) 2). C'est un accord à deux plus une convergence née de la critique ; A-T3 15 est compté **deux fois** (dans les onze accords et dans les vingt-sept convergences).
- **Q4 « uniforme avec arrêt par défaut »** : en T1, seule C le tient explicitement ; A le laisse entendre (« le bandit n'est pas un problème bien posé ») ; D ne le dit qu'en T3 (« l'uniforme avec arrêt demeure l'option par défaut », D-T3 7-9), après les critiques de A et C — cession que la synthèse range aussi parmi les convergences. Double compte.

Enfin, les volets nomment au moins dix-sept accords (Q3 « noyade sans stratification » C et D ; Q3 « nombres par puissance » A et D ; Q5 « condition de jugeabilité » ; Q6 « allocation de ressources reprise comme base » A, C, D ; Q6 « reproduction puis test hors échantillon » A et D ; etc.) ; la règle qui en retient onze n'est pas écrite.

### RB-02 — « 27 convergences nées de la critique » : non reproductible — **majeure**

La même ligne donne les cessions par espèce : A 15, B 17, C 11, D 12, soit **55**. Les paragraphes « Convergences nées de la critique » des volets en nomment **33** (Q1 : 8 ; Q2 : 7 ; Q3 : 8 ; Q4 : 3 ; Q5 : 5 ; Q6 : 0 ; Q7 : 2). Ni 55 ni 33 ne donnent 27, et aucun recalcul n'est montré (critère 15 : « recalcul montré en une ligne quand il y en a un »).

### RB-03 — « 9 divergences résolues, listées par volet » : trois seulement sont listées — **majeure**

Trois paragraphes portent l'intitulé « Divergence résolue » : Q1 (garde lexicale de C retirée), Q2 (« les résumés suffisent-ils ? »), Q3 (le « ≥ 7/8 » de C). Les six autres ne sont nommées nulle part.

### RB-04 — Divergences maintenues : sept dans le décompte et dans la liste du tour 2, onze dans les volets — **majeure**

Les volets nomment, en plus des sept de la liste : **Q3-c** (les nombres de paires : quatre bases différentes) ; **Q4-b** (C refuse tout bandit tant que la récompense n'est pas un test par calcul ; A et D le gardent comme hypothèse à éprouver en monde synthétique) ; **Q5-b** (ce que mesure la rétrodiction : terrain et règles de tirage pour A et B, moteurs pour C, métrique secondaire pour D) ; **Q7-b** (passe de moisson courte en génération 1 : C oui, B non, D seulement après essai réel du relais). Les quatre disparaissent du décompte et de la liste « Pour le tour 2 ». Deux d'entre elles sont portées par C seule ou d'abord (Q4-b, Q7-b) : leur abandon élimine des avis non réfutés.

S'y ajoute une divergence **non relevée** : le coût de la reproduction de Gu et Krenn sur leur propre graphe (voie dite « R-a ») : A, « ≈ 1 h par tâche, < 15 Go », puis « ≈ 10-40 dollars illustratif » ; D, « 32 Go, 50 Go, "100–600 €" illustratif ». Un facteur dix, côte à côte dans la table Q6, sans commentaire. Seule la pièce 3 (non lue ici) peut trancher.

### RB-05 — « 12 apports seuls (A 4, B 2, C 4, D 2) » : non reproductible — **moyenne**

Les paragraphes « Apports » marqués « seule » donnent environ A 8 (boucle déjà existante ; mesure « ancrage inversé » ; témoin « paires délibérément incompatibles » ; retour du bras hasard comme témoin ; « blocs couverts » ; trois fuites non nommées ; regroupement des succès au-delà de l'allocation de ressources ; « garder l'allocation de ressources »), B 1 (entropie comme garde), C 5 à 6, D 5 (récompense rétrodictive interdite ; canal « issue future » ; refus du « nombre d'expert » ; criblage uniforme puis bandit ; préalables à tout recodage). B est surcompté, D et A sous-comptés. Le sens du biais n'avantage pas A (lecteur de la même famille) ; c'est un défaut de tenue, pas de faveur.

### RB-06 — Accords vrais par construction ou soufflés, non marqués comme tels — **majeure**

- **Q1 « "affiner" sans capteur = "reformuler" »** est **la parenthèse de la question elle-même** (Q1 : « sans quoi "affiner" veut dire "reformuler" »). L'accord à quatre est un acquiescement à l'énoncé, compté comme accord indépendant large. Le critère 2 (et le critère 11, effet d'ordre) aurait dû le classer « vrai par construction ».
- **Q1 « état minimal en champs fermés »** est fortement soufflé par la demande (b) de la question (« objet versionné (affirmation, mécanisme, pièces, trous) ») et par le format de fiche déjà servi (§ 3.2, l. 120). L'accord est réel sur le détail (quels champs), pas sur le principe.
- **Q5 circularité** : la question demande « Quelle fuite rend le test circulaire (modèles entraînés après la coupure) » ; la synthèse dit « en partie vrai par construction ». C'est plus qu'en partie : la circularité est posée par la question ; l'apport des espèces est seulement la frontière (algorithmique valide, générative invalide).
- **Q5 témoin « allocation de ressources » manquant, « à quatre »** : la pièce 2 servie dit que la marche de Swanson perd contre l'allocation de ressources (−0,82 point) ; l'accord est soufflé par la pièce. Et la ligne de B dans la table Q5 ne mentionne pas l'allocation de ressources : « à quatre » n'est pas soutenu par ce que la synthèse cite (trois au plus ; voir « exige les cellules »).

### RB-07 — Q6 : accord et divergence contradictoires ; A mal rangé dans la liste du tour 2 — **moyenne** (elle touche la décision (ii))

Le volet Q6 écrit : « À quatre (vrai par construction : pièce 3) : … "tel quel" possible seulement dans leur domaine (R-a) ». Or C, selon la même table, veut « exécuter tel quel » leur code d'extraction, de traits et d'entraînement **sur notre corpus** (C-T1 Q6 ; C-T3 (c) 3) : l'accord « à quatre » contredit la divergence Q6-a écrite trois lignes plus bas ; le décompte, lui, dit « à deux (A, D) ». Par le critère 2, la partie « aucun poids, vocabulaire de physique » est un fait servi et ne compte pas comme accord.

La liste du tour 2 formule Q6-a ainsi : « relancer leur code sur notre corpus est-il "tel quel" (C) ou "recoder un substitut" (A, B, D) ? ». **A ne dit pas « recoder un substitut »** : sa ligne dit « la chaîne RAKE relancée sur `cs.LG, cs.AI, cs.CL, cs.CR, stat.ML` = tester leur méthode, pas leur modèle » et, en T3, « la relance de leur chaîne (leur méthode, pas leur modèle) vaut un devis ». Le vrai partage est à deux axes : **l'action** — relancer leur chaîne (A, C) ou coder un substitut (B, D) ; **le mot** — « tel quel » (C seul) ou non (A, B, D). La formulation de la synthèse fait apparaître C seule contre trois, ce qui est faux sur l'action.

### RB-08 — Q2 « dérivation mécanique à quatre » : soutenu pour C et D seulement — **moyenne**

Dans la table Q2, C (« aucune requête en texte libre ») et D (« dérivées mécaniquement de champs autorisés ») disent la dérivation mécanique. A veut que la dérivation « concepts, antériorités, trous » **batte** une base mécanique (titre verbatim, TF-IDF) : sa dérivation n'est donc pas posée comme mécanique. B : « requête des concepts et trous », sans dire par quoi. La **garde** mécanique, elle, est bien à quatre (A grep des identifiants, B « 10/10 piégées », C, D). L'accord « dérivation et garde » doit être scindé ; la moitié « dérivation » est inférée pour A et B.

### RB-09 — Fuite de recommandations par les faits plus large que relevée — **moyenne** (défaut de notre question, pas de la synthèse)

La question promettait « toute recommandation des auteurs est retirée ». La synthèse relève une fuite (C cite la bande d'éloignement [2 ; 4] de l'annexe du bras méta, l. 219). Le § 2 et le § 7 servis en portent deux autres : « **quotas recommandés** : 1 tour, 4 requêtes, 5 résultats » (l. 101) — A les a pris pour « décidés », ce que la synthèse compte comme inexactitude d'état, mais pas comme fuite — et « condition de reproduction préalable : relâchée (**recommandation R-635**) » pour Gu-Krenn (l. 213), qui touche directement Q6. Que des espèces s'y soient appuyées ne se vérifie que sur les cellules. C'est un défaut de la question écrite par conv-audit, à corriger pour le tour 2.

### RB-10 — Pièces non servies qui pèsent sur Q7 — **mineure** pour la synthèse, **à servir** au tour 2

La pièce 1 servie couvre les § 1, 2, 3, 7, 9 et 10 du dossier. Ni le § 4 (aiguilleur : défaut R-819 déclaré le 1er novembre, **porte du pré-pilote fermée d'avance**, course partant par l'option O8 (b) sur ton mot, l. 157-158) ni le § 11 (GO du pré-pilote jusqu'au 7 novembre, GO de la course 2 jusqu'au 14 novembre, issue la plus probable du pré-pilote « nœud sans départ » 0,63, l. 298-308) n'ont été servis. Les quatre espèces raisonnent sur « la course 2 attend un pré-pilote » sans savoir que la porte de ce pré-pilote est déjà déclarée fermée. Cela ne renverse pas leur avis, mais le « lien avec le pré-pilote » (critère 10) est lu sur une prémisse incomplète.

### RB-11 — Une inexactitude « sur les pièces » à requalifier ; une traçabilité incomplète — **mineure**

- C : « α = 0,05 par hypothèse testée, pièce 1 § 1.1, VÉRIFIÉ ». La ligne servie (§ 1.1, l. 23 du dossier) dit seulement « 5 % de fausses promotions garanties ». La synthèse a raison de refuser « VÉRIFIÉ » ; mais le § 6 du dossier (non servi) parle de « pari séquentiel, inégalité de Ville, garantie de 5 % de fausses promotions, règle de fausses découvertes entre hypothèses » (l. 192), ce qui rend « par hypothèse » plausible sur le fond. À requalifier : « VÉRIFIÉ non soutenu par la ligne citée », pas « inexact ».
- Plusieurs renvois à D n'ont pas de section (« D-T1 »), dont la citation de l'apport de D ; le critère 15 demande la section.

### RB-12 — Réserve de famille — **mineure** (observation, pas preuve)

Le lecteur est du modèle de A et le déclare. Je ne trouve **pas** de faveur à A : ses deux inexactitudes d'état sont relevées et exactes sur le dossier (« quotas décidés » contre « quotas recommandés », l. 101 ; « coupure 30 juin 2026 décidée » contre « SUPPOSÉ, à essayer avant le gel », l. 212), ses apports sont plutôt sous-comptés. En revanche, les pertes de la synthèse tombent surtout sur les voix hors Anthropic : C est montrée seule contre trois en Q6-a alors que A partage son action (RB-07) ; Q4-b et Q7-b, portées par C, disparaissent du tour 2 (RB-04) ; le refus du bandit par C est fondu dans un « large » où D n'arrive qu'en T3 (RB-01). Trois des quatre voix de la chaîne qui produit cette relecture sont d'Anthropic (A, B, le lecteur), plus moi. L'espèce B est servie en Opus 4.6, pas en Opus 5.5 comme le dit le dossier (§ 8, l. 231) : c'est conforme à la règle de repli de Lazar (R-787 de `main`, relayée en R-507 et R-593 du registre de conv-audit) et au précédent de la question 6 du collisionneur, mais la synthèse ne dit pas si Opus 4.6 était le modèle prévu ou un repli après refus.

### RB-13 — Recommandations glissées — **mineure**

Le critère 16 interdit toute recommandation du lecteur. Relevées : (1) en-tête : « le tour 2 pourra confier la contre-lecture de cette synthèse à un autre modèle » ; (2) note de méthode : « une contre-lecture par un autre modèle serait la plus utile sur la table Q6 et sur l'accord Q7 » (procédurales, sans effet sur le fond) ; (3) Q6-a : « elle décide ce que la décision de Lazar autorise sans nœud nouveau » — le lecteur interprète la portée de ta décision, ce qui n'est pas son rôle ; (4) Q3-a : « Les objets diffèrent (classement en course chez C ; banc d'évaluation chez D), aucune ne le dit » — début de réconciliation par le lecteur, qui tranche à moitié une divergence qu'il déclare pourtant maintenue ; (5) « Accords trop propres » 1 : la « question inverse » suggère une option (brancher la boucle dès le pré-pilote) ; acceptable comme symétrie (règle R4 : un accord trop propre déclenche le même audit), à garder comme question, pas comme piste.

### RB-14 — Ce qui tient — **constat positif**

- Tous les recalculs refaits : entropie (0,276 et 1,178 bit), √(0,5/28) = 0,134 et 0,62, 2 × 0,5/√84 = 0,109, combinatoire (8 128 ; 2,53 × 10⁷ ; 1,95 × 10¹⁰), π = 0,0208 et 0,982, k = 5 141, √(0,25/24) = 0,102 et Φ(−0,67) = 0,25, ± 20 points, 3 954 pages et 0,395 dollar, 0,337² = 0,114 : **exacts**.
- Chiffres du dossier recoupés : quotas (l. 101), ≈ 0,4 dollar par course (l. 105), 197 681 œuvres et 237 Mo (l. 107), 24 fusions et 8 par bras (l. 223), « aucune comparaison entre bras n'est lue » au pré-pilote (l. 224), 0,27 / 0,55 et bande [2 ; 4] à 0,49 et 0,84 (l. 219), accord de rang 0,12 et 17 idées sur 29 (l. 285), juges sur la cohérence seule (l. 191, 266) : **exacts**.
- Les positions T3 que le relayeur résume (Q1 à Q7, apports de A et de D) sont soutenues par les tables de la synthèse, avec les nuances ci-dessous.

### Les positions T3 résumées par le relayeur, une à une

| Point | Soutenu par ce que cite la synthèse ? | Vrai par construction, effet d'ordre ou d'énoncé |
|---|---|---|
| Q1 état minimal en champs fermés ; pertinence jugée à l'aveugle contre des cas dégradés ; qui juge : divergence | Oui pour A (version neutre et version dégradée), B (témoin « ajout au hasard »), D (classes plantées) ; **C le plus faible** : aveugle oui, « dégradés » seulement par sa calibration à paraphrases | « champs fermés » soufflé par la demande (b) ; « affiner = reformuler » est la phrase de la question (RB-06) |
| Q2 dérivation et garde mécaniques, à quatre | Garde : oui à quatre. Dérivation : C, D seulement (RB-08) | Garde déjà codée (l. 102) ; le critère 5 classe toute garde non mécanique « non opérationnelle » |
| Q3 ne jamais mélanger les types de paires ; nombres par puissance | Séparer : C, D en T1, A en T3, B par sa critique de D — convergence, pas accord indépendant (RB-01). Puissance : A et D ; B déclare sa puissance (0,25) ; C donne des nombres « illustratifs » | — |
| Q4 uniforme avec arrêt par défaut | C en T1, D en T3, A implicite, B silencieuse | **À contre-énoncé** : la question et la demande (d) favorisaient le bandit ; l'accord n'est pas un effet d'ordre |
| Q5 rétrodiction générative avec les modèles courants circulaire, 4/4 ; fermetures algorithmique et prospective | Oui ; prospective chez A, C, D (B non montrée) | Circularité posée par la question (RB-06) ; l'antériorité la confirme de façon indépendante (voir plus bas) |
| Q6 « tel quel » seulement dans le domaine de Gu-Krenn ; divergence sur le sens | Le « à quatre » est contredit par la ligne de C (RB-07) | Partie factuelle = pièce 3, vraie par construction |
| Q7 course 2 d'abord, boucle en génération 2 sous portes, tests de mort à activer, 4/4 | Oui, à quatre en T1 | **Effet d'énoncé** : la question donne à cette option la raison entre parenthèses et nomme « tests de mort » dans l'objectif ; la synthèse le dit |
| Apport de A : la boucle existe déjà (chaîne à deux passes, entre générations) ; la demande ajoute la moisson comme nœud ; trois fuites non nommées | « La boucle existe » : **vrai sur pièces** (le dossier marque trois boucles : passe « tableau », fusion qui repasse, génération suivante, l. 85, 86, 91). « Ajoute la moisson comme nœud » : **imprécis** — le nœud moisson existe déjà dans le schéma (l. 59, 82), codé en version 47 de l'orchestrateur, jamais servi (l. 105-106) ; ce que la demande ajoute, c'est la moisson **ciblée par embryon, relancée à chaque version**, et les œuvres moissonnées **dans le vivier d'appariement**. Trois fuites : plausibles sur le dossier (vérificateur d'antériorité avec recherche web, l. 49 ; héritage des fiches entre générations, l. 39 ; moisson en vrac jusqu'à la coupure du 30 juin 2026, l. 212), non contestées ; l'antériorité ne nomme pas la première | Une source ; aucune autre espèce ne l'a discuté |
| Apport de D : « le gain rétrodictif post-coupure ne doit jamais servir de récompense interne » | Cité « D-T1 » sans section : citation à vérifier sur la cellule | **Presque vrai par construction** : c'est l'interdit de sélectionner sur la mesure qui sert d'épreuve. Seul par la formulation, compatible en substance avec C (seule récompense admissible : un test par calcul) et A (récompense non observable). Rangé en Q1 alors qu'il porte sur Q4 et Q5 |

---

## Points qui exigent les cellules (chez session-depot)

1. Recompter accords, convergences, divergences résolues, divergences maintenues et apports seuls, avec la règle écrite (RB-01 à RB-05).
2. B en Q5 : nomme-t-elle l'allocation de ressources comme témoin manquant ? B en Q3 (T3) : sépare-t-elle les types de paires ?
3. A et B en Q2 : la dérivation des requêtes est-elle mécanique ou écrite par un modèle ?
4. Citations exactes, avec section : D-T1 sur la récompense rétrodictive ; A-T1 A11 et A12 ; C-T3 (c) 3 (« Exécuter tel quel (décision de Lazar) … »).
5. Journal et état du run : modèle servi pour B (Opus 4.6 prévu ou repli ?), 12,61 dollars.
6. Pièce 3 (état des lieux de Gu et Krenn) : ressources et coût de leur reproduction (A contre D, RB-04).
7. Usages par les espèces des deux recommandations servies par les faits (quotas ; R-635) (RB-09).

---

# Pour Lazar, en clair

## 1. Ce que conclut le collisionneur, question par question (aucun avis non réfuté retiré)

Espèces : A = Fable 5.1, B = Opus 4.6, C = Argon (Google), D = Kimi K3.1 Pro. « Allocation de ressources » = un score de lien entre deux concepts par leurs voisins communs, pondérés par l'inverse de leur nombre de liens ; c'est lui qui a battu la marche de Swanson dans notre rétrodiction.

**Q1 — Qu'est-ce qu'un embryon d'idée, quand y a-t-il progrès, quand s'arrêter.**
Commun : une nouvelle version ne compte comme progrès que si des **champs fermés** changent (une antériorité nouvelle vérifiée, une prédiction chiffrée modifiée, un trou fermé) ; un écart de texte ne suffit jamais ; la part de jugement doit être **mesurée à l'aveugle contre des versions dégradées ou plantées**. (Réserve : ta question disait déjà « sans quoi affiner veut dire reformuler ».)
- A : trois champs (prédiction chiffrée, antériorités vérifiées, trous fermés) ; arrêt après deux tours sans changement, sinon au budget seul ; épreuve : trois juges devant une version neutre et une version dégradée.
- B : un évaluateur aveugle champ par champ et un témoin « ajouts au hasard » ; garde contre la boucle qui tourne en rond par l'entropie des concepts (corrigée) ; **aucune règle d'arrêt**.
- C : une transition vaut si une référence non citée apparaît et qu'un lecteur aveugle au tour confirme qu'elle comble le trou ; plafond de deux tours ; arrêt si l'antériorité tue l'idée.
- D : objet gelé à chaque tour ; progrès seulement si un trou est fermé par une pièce vérifiée, une prédiction modifiée, une réfutation, ou une traduction en loi testable ; plafond de tours et d'euros ; vérité terrain par lecteurs sur PDF.
- **Divergence maintenue** : qui juge le progrès (les juges de la course, un évaluateur dédié, le lecteur du bisociateur, ou des lecteurs sur PDF).
- **Apports seuls** : A — l'organisme boucle déjà (seconde passe « tableau », fusion qui repasse, génération suivante) ; ce que tu demandes ajoute surtout une moisson ciblée par idée à chaque version ; C — la moisson comme **filtre de réfutation** plutôt que comme affinage ; B — l'entropie comme alarme de rond ; D — **le score de rétrodiction ne doit jamais servir à choisir ou à récompenser** les idées, sinon l'épreuve fuit dans la sélection.

**Q2 — Moisson ciblée sans fuite.**
Commun : **garde mécanique** qui refuse toute requête portant un texte d'épreuve ou un identifiant d'épisode, à **mesurer branchée sur le vrai relais**, jamais essayé à ce jour. C et D : requêtes tirées de champs fermés, jamais de texte libre (A et B ne le disent pas dans ce que cite la synthèse). C et D : les résumés suffisent pour **trouver**, pas pour **valider** un chiffre (il faut le PDF).
- A : requête tirée de la fiche amputée ; doit battre une base mécanique (titre tel quel, recherche par mots) ; mesure « ancrage inversé » : part des œuvres qui réfutent la fiche intégrées comme soutien (seuil 0,3).
- B : témoin « requêtes sur les antériorités déjà citées » ; mesure : œuvres **non citées** jugées pertinentes.
- C : étiquettes de concepts et identifiants ; liste noire stricte de termes ; déclencheur à deux détentes (résumé pour repérer, PDF pour les survivantes).
- D : trois canaux plafonnés ; univers de candidats figé et empreinté ; la douane refuse aussi toute « issue future ».
- **Apports seuls** : C, les deux détentes ; A, l'ancrage inversé ; D, le canal « issue future ». Repris par tous : la moisson croisée (servir à une fiche la moisson d'une autre) comme témoin.

**Q3 — Apparier fiches et articles.**
Commun (C et D d'emblée, A et B après critique) : **ne jamais classer ensemble des types de paires différents** ; sans séparation, les paires article–article (≈ 2 × 10¹⁰) noient les paires avec fiche (≈ 8 × 10³ fiche–fiche) (C, D). A et D : nombre de paires fixé par la puissance statistique, pas par le prix ni par un « expert ».
- A : seules les paires concept–concept ont une issue mesurable en rétrodiction ; les paires avec fiche relèvent d'une autre épreuve ; calculer **avant** si l'épreuve est jugeable (au moins 50 réussites attendues par méthode).
- B : 24 fiche–article contre 24 au hasard appariées ; puissance ≈ 0,25 déclarée : un « non concluant » voudra dire « trop petit », pas « inutile ».
- C : **interdire l'article–article pendant la course** ; quotas séparés (une fiche–fiche et une fiche–article par bras, illustratif) ; filtre anti-plagiat.
- D : l'article–article est la **seule épreuve primaire** des bras (en banc), les épreuves avec fiches reportées ; refus de tout nombre avant un pré-échantillon.
- **Divergences maintenues** : article–article interdit en course (C) ou seule épreuve d'évaluation (D, A) — peut-être deux usages compatibles, personne ne l'a dit ; coût de la moisson complémentaire (C : ≈ 0,40 dollar pour compléter nos 197 681 œuvres ; B : tout le corpus, volume inconnu) ; les nombres (quatre bases différentes).
- **Apports seuls** : C, interdiction et quotas séparés, anti-plagiat ; D, refus du « nombre d'expert » ; A, témoin « paires délibérément incompatibles » et retour du bras hasard comme témoin.

**Q4 — Répartir le budget entre embryons.**
Commun (A, C, D ; B silencieuse) : **allocation uniforme avec arrêt par défaut** ; un bandit (qui donne plus aux embryons qui « rapportent ») n'a aujourd'hui aucune récompense observable, puisque les juges ne notent que la cohérence. Personne ne défend le bandit — contre l'énoncé, qui le présentait en premier.
- A : éprouver le bandit d'abord dans des mondes simulés avec des « parasites » plantés (idées faciles à fusionner et stériles) ; réserver une part d'exploration.
- B : « gain de nouveauté » non défini ; ni choix ni pire cas.
- C : **refus du bandit** tant que la récompense n'est pas un test par calcul (sinon on récompense l'enflure verbale).
- D : criblage uniforme puis bandit avec plancher d'exploration, en simulation d'abord ; l'uniforme reste le défaut.
- **Divergences maintenues** : la récompense « trou fermé » va-t-elle contre la nouveauté (A, C : oui, comme une loi ; D : un risque, pas une loi) ; **C refuse tout bandit, A et D le gardent à éprouver** (cette seconde divergence a disparu de la liste de la synthèse).
- **Apports seuls** : D, criblage puis bandit ; A, compter les régions couvertes comme garde contre la concentration.

**Q5 — La rétrodiction (faire comme si on était avant une date de coupure).**
Commun (quatre) : avec des proposeurs entraînés après la coupure (Kimi, Argon, Opus), **la rétrodiction qui génère des idées est circulaire** (ta question le posait). Fermetures : rétrodiction **strictement algorithmique** (sans modèle de langage) pour juger la moisson et les règles d'appariement ; pour la boucle avec modèles, **test prospectif scellé** (on produit maintenant, on lit plus tard) (A, C, D). Témoin manquant : l'allocation de ressources (A, C, D ; B non établie).
- A : « apparu après la coupure » mesure une cooccurrence de mots, pas une découverte ; si l'épreuve n'est pas jugeable, déclarer la rétrodiction **non lançable sur ce champ**.
- B : vérifier d'abord que le terrain (arXiv en intelligence artificielle) porte un signal ; seuil relatif ; appariement sur le nombre de liens et l'âge des concepts ; aucun modèle de langage.
- C : valide pour des paires de concepts sans modèle, invalide pour la boucle complète.
- D : « apparaître après » pénalise une bonne idée inédite ; des poids ouverts ne prouvent pas une date de coupure ; le score rétrodictif doit prédire la survie aux tests de mort, sinon il reste secondaire.
- **Divergences maintenues** : un modèle à poids ouverts daté peut-il prouver l'absence de contamination (A oui ; D non sans corpus d'entraînement vérifiable ; C a retiré l'idée ; B l'évite) ; ce que la rétrodiction mesure au juste (cette seconde divergence a disparu de la liste de la synthèse).
- **Apports seuls** : A, trois fuites que la question ne nommait pas : le vérificateur d'antériorité **cherche sur le web** (il voit l'avenir), les fiches héritées d'une génération à l'autre, la moisson en vrac non coupée à la date ; C, la « recherche en un coup » comme témoin.

**Q6 — Ce qui existe, et que reprendre tel quel.**
Commun : Gu et Krenn n'ont publié aucun poids et leur vocabulaire est de physique (fait de la pièce 3) ; les huit autres systèmes restent « à vérifier » (l'antériorité ne leur avait pas été servie) ; l'allocation de ressources de notre rétrodiction est reprise comme base (A, C, D).
- A : « tel quel » seulement sur leur propre graphe ; relancer leur chaîne sur nos catégories arXiv, c'est tester **leur méthode, pas leur modèle** ; d'abord vérifier sur leur graphe que leur réseau bat l'allocation de ressources — sinon « garder Gu-Krenn » revient à « garder l'allocation de ressources ».
- B : « tel quel » est impossible pour notre domaine ; seule la méthode se transfère ; les autres systèmes ne sont pas traités.
- C : **exécuter tel quel** leur extraction de concepts, leurs 141 traits et leur entraînement sur notre corpus (« décision de Lazar appliquée »), sans fichiers sérialisés à risque ; liste fichier par fichier.
- D : reprendre leur code dans leur domaine, puis hors échantillon si les tolérances passent ; pour nous, **assumer un substitut** ; avant tout recodage : PDF, sortie exacte, licence, version du code, coupure, petit banc.
- **Divergence maintenue** : le sens de « tel quel ». Sur l'**action**, A et C relancent leur chaîne, B et D codent un substitut ; sur le **mot**, C seul l'appelle « tel quel ». Non relevé par la synthèse : coût de leur reproduction, A ≈ 10-40 dollars, D 100-600 euros (tous deux illustratifs).

**Q7 — L'ordre.**
Commun (quatre, avec la réserve que ta question soufflait cette option) : **course 2 d'abord ; boucle au plus tôt en génération 2, sous portes ; activer d'abord les tests de mort.**
- A : boucle seulement après un capteur de progrès éprouvé et l'épreuve des bras contre l'allocation de ressources ; confiance 0,6.
- B : course 2 **sans** moisson ; boucle en génération 2 seulement si ses expériences 1 (la moisson aide-t-elle ?) et 4 (le terrain a-t-il un signal ?) le justifient.
- C : une **passe de moisson courte** dès la génération 1 ; tests de mort entre générations 1 et 2 ; boucle à plusieurs tours seulement si elle bat le tirage en un coup ; calibration des tests de mort bloquante.
- D : la course 2 peut journaliser des embryons sans appeler ses sorties « validées » ; moisson seulement après essai réel du relais et de la douane ; première expérience : calibrer l'étage des tests de mort.
- **Divergences maintenues** : la première expérience (rétrodiction algorithmique pour A, B, C ; calibration des tests de mort pour D, en parallèle chez C) ; la passe de moisson en génération 1 (C oui, B non, D après essai du relais — disparue de la liste de la synthèse).

## 2. Ce que changent l'antériorité et SciMuse (à servir au tour 2)

Lu sur PDF par moi : SciMuse (p. 1, 5, 7, 8, 16), HindSight (p. 2 et 4), MAGenIdeas (p. 21-22), MiroGraph (p. 1 et 3). Tout le reste de l'antériorité est « à vérifier sur PDF » (règle R7 : aucun chiffre sans PDF empreinté et page lue).

**SciMuse (Gu et Krenn, version 4 du 24 septembre 2026), vérifié.** 110 chefs de groupe ont noté 4 451 idées (de 1 à 5). Trois conditions, même consigne au modèle : paire de concepts **choisie par leur réseau** (la méthode de Gu et Krenn adaptée, cible : au moins 10 citations en 3 ans, p. 5), paire **au hasard**, ou **aucune paire** (le modèle ne reçoit que les titres des deux chercheurs). Moyennes : 2,350 ± 0,034, 2,446 ± 0,035 et 2,414 ± 0,036 (p. 7) ; part des idées notées 4 ou 5 : 23,3 %, 25,2 % et 26,2 % (p. 7 ; effectifs 1 516, 1 480, 1 455, p. 16). Les auteurs parlent de « faible indication statistique (1,94 écart-type) » que leurs paires font **moins bien** que le hasard (p. 1, 7) ; mon recalcul donne 1,97, soit p bilatéral ≈ 0,05 : **à la limite**, pas établi. Et surtout : **aucune condition ne bat « aucune paire »** (p. 8 : « no evidence that supplying either random or high-citation-predicted concept pairs improves expert-rated interest over the titles-only GPT baseline ») ; plus un concept est relié dans le graphe, moins l'idée intéresse (pente −0,213, p. 8).
Ce que cela change : (1) la formule qui a circulé (« les paires à la Gu-Krenn font moins bien que le hasard », registre R-1045, et ta décision du 15:39 R-1049) **exagère** : disons « pas mieux que le hasard, peut-être un peu moins bien » ; ta décision de tester plusieurs bras en sort renforcée, pas affaiblie ; (2) il manque aux trois témoins de la boucle un témoin **« sans paire »** (aucune espèce ne l'a proposé tel quel) ; (3) le critère est l'**intérêt jugé**, pas la réalisation future ni la survie à un test : SciMuse ne dit rien de la rétrodiction ; (4) le bras Gu-Krenn optimise l'impact prédit en citations, qui va **contre** l'intérêt jugé sur plusieurs traits du graphe.

**Par question :**
- **Q1** : MAGenIdeas (vérifié, p. 21-22) montre la moisson qui cesse de nourrir l'idée (17,6 % → 3,3 % → 5 % des notions venues des articles moissonnés ; 11,8 % → 43,1 % → 78,3 % venues de la version précédente) — mais sur **un seul cas** présenté comme « représentatif » (51 à 60 notions) : une anecdote, pas une mesure ; l'antériorité la généralise trop. Nova (plus de gain après trois tours) et BioDisco (trois cycles au plus) soutiennent le plafond court de C (à vérifier). Callaghan et Müller-Hansen 2020 donnent une règle d'arrêt **statistique** (s'arrêter quand on peut rejeter « on a manqué l'antériorité » à un niveau donné), absente des quatre avis et utile contre l'absence de règle chez B.
- **Q2** : la moisson tirée des faiblesses d'une idée existe déjà (Co-scientist de Google) ; **aucun système lu ne filtre les requêtes de moisson elles-mêmes**, qui sortent vers OpenAlex et arXiv : faut-il une douane **avant** chaque moisson ? Aucune espèce ne l'a posé.
- **Q3** : bancs datés d'article–article en intelligence artificielle (PreScience, Alien Space — 16 068 articles sur les modèles de langage) : l'épreuve primaire de D peut s'y adosser au lieu d'être construite (à vérifier). Un vivier mêlant les trois types sous trois bras comparés : non trouvé — c'est une question, pas un trou (règle R8 : zone vierge = question).
- **Q4** : les bandits publiés qui marchent récompensent un **résultat d'expérience** ou une surprise mesurée sur des données (DeepScientist, AutoDiscovery), pas une nouveauté jugée — cela soutient C. HindSight (vérifié, p. 4) : la nouveauté jugée par un modèle est **négativement** corrélée à la réalisation (ρ = −0,291, p = 0,003) : une récompense « gain de nouveauté » jugée serait trompeuse ; c'est une pièce pour la divergence sur l'anticorrélation (pas la même grandeur que « trou fermé »).
- **Q5** : HindSight, le protocole publié le plus proche de ta demande (f), a **précisément la fuite** que les quatre craignent : coupure en juin 2023, modèle Llama-3.3-70B dont la connaissance va jusqu'en décembre 2023, présenté comme « marge de 6 mois » (vérifié, p. 2) — le modèle connaît les six premiers mois de la période à prédire. IdeaForecastBench recommande de **geler les prévisions avant de collecter la littérature cible** (le test prospectif de A, C, D ; à vérifier). MiroGraph **cache l'identité des concepts** aux agents (p. 3) — l'anonymisation que C a retirée sous la critique existe dans un travail publié (non validée pour autant). Dans le contrôle des IA, la littérature utile date de 2022-2026 : une coupure assez ancienne pour un modèle propre laisse peu à prédire, ce qui soutient la « condition de jugeabilité » de A.
- **Q6** : réponse que les espèces n'avaient pas : **aucun composant de la boucle n'est vierge** ; trois systèmes en font l'essentiel (BioDisco, Co-scientist, MOOSE-Chem) ; toute revendication devra porter sur un **résultat** (la boucle bat ses témoins à budget égal), pas sur l'architecture. **MiroGraph** (vérifié, p. 1 et 3) rejoue déjà Impact4Cast de Gu et Krenn **hors physique**, sur des graphes de concepts construits par modèle à partir de CIKM, KDD et SIGIR, code annoncé (`github.com/bdi-lab/MiroGraph`) ; dans leur table, Impact4Cast obtient 0,58 à 0,66 et MiroGraph 0,62 à 0,75 (score F1 moyen par classe) ; mais il appelle GPT-5.4 et GPT-4o-mini (dépense, envoi de données), licence du code non vérifiée, rien exécuté. C'est une troisième voie pour « Gu-Krenn tel quel », qu'aucune espèce n'a pesée.
- **Q7** : rien de direct ; l'écart idéation–exécution (Si, Hashimoto, Yang 2025 : les idées des modèles perdent plus que celles des humains une fois exécutées, à vérifier) soutient la priorité aux tests de mort. Fait du registre, hors antériorité : le pont fiche → loi (R-1044) conclut que presque aucune fiche n'est testable aujourd'hui sur une banque existante — « validé par l'expérience » dépend d'abord de ce pont et des épisodes neufs, pas de la boucle de moisson.

À servir aussi : les § 4 et 11 du dossier (porte du pré-pilote déjà fermée, échéances des GO) ; la liste des divergences corrigée (onze, plus le coût de la reproduction de Gu et Krenn) ; Q6-a reformulée sur ses deux axes (action et mot).

## 3. Cartes de décision

### (i) Construire la boucle avant la course 2, ou en génération 2

- **Décision** : quand construire la boucle itérative moisson ↔ fiches ↔ bisociateur.
- **Enjeu** : la course 2 a un GO jusqu'au 14 novembre (GO-2026-10-31-04, plafond 160 dollars pré-pilote compris) ; la boucle exige des pièces qui n'existent pas (relais de moisson réel jamais essayé, capteur de progrès non défini, récompense d'allocation non observable, rétrodiction circulaire avec nos modèles) ; ton objectif « validées par l'expérience » passe d'abord par les tests de mort et le pont fiche → loi.
- **Options** :
  - **(A) Boucle complète avant la course 2** — avantage : la génération 1 profite de la moisson ciblée ; inconvénient : retard probable au-delà du 14 novembre, aucune espèce ne la soutient, l'affinage plafonne vite selon l'antériorité.
  - **(B) Course 2 sans moisson, boucle en génération 2 sous portes** (B) — avantage : calendrier tenu, aucune fuite nouvelle ; inconvénient : contredit ton « il nous faut le moissonneur pour la course 2 » (R-469), génération 1 sans littérature fraîche.
  - **(C) Course 2 avec une seule passe de moisson** (déjà codée, version 47 de l'orchestrateur, ≈ 0,4 dollar par course annoncé), **après un essai réel du relais et de sa garde de fuite**, embryons journalisés ; boucle à plusieurs tours en génération 2 seulement si elle bat la passe unique (C, D) — avantage : honore R-469 et produit les données qui jugeront la boucle ; inconvénient : un essai du relais avant le départ (temps, petite dépense), garde jamais éprouvée en vrai.
- **Recommandation** : **(C)**, et **(B)** si l'essai du relais ne peut pas se faire avant le départ ; confiance **0,65**. Réserve : l'accord à quatre est soufflé par la question ; la question inverse (qu'est-ce qui interdirait de brancher la boucle dès le pré-pilote si le relais était essayé ?) n'a jamais été posée.
- **Défaut sous 48 heures** : (B). Passer à (C) demande ton mot et un devis d'essai du relais chez session-depot (nœud de dépense).

### (ii) « Gu-Krenn tel quel » : leur code relancé sur notre corpus, méthode seulement, ou substitut

- **Décision** : ce que veut dire « tel quel » pour le bras Gu-Krenn du bisociateur et pour le témoin Gu-Krenn de la rétrodiction.
- **Enjeu** : aucun poids publié ; leur vocabulaire (37 960 concepts d'optique et de physique quantique) ne couvre pas le contrôle des IA ; le code actuel (version 56) n'accepte que le substitut maison (« Gu-Krenn maison », seuil S31 jamais essayé) ; ta phrase du 1er novembre : « tel quel dès que c'est possible **sans recoder nous-mêmes** » ; SciMuse : leurs paires ne font pas mieux que le hasard ni qu'aucune paire, sur l'intérêt jugé.
- **Options** :
  - **(a) Relancer leur code sans en écrire** (extraction de concepts, 141 traits, réseau réentraîné) sur notre corpus — position de C (qui l'appelle « tel quel ») et, sur l'action, de A (« leur méthode, pas leur modèle ») — avantage : respecte « sans recoder nous-mêmes » si leurs scripts acceptent notre corpus par simple configuration ; teste leur méthode entière ; inconvénient : modèle nouveau, pas le leur ; leur extraction de mots-clés bruite le graphe (B) ; il faut des résumés (≈ 0,40 dollar d'interface selon C, illustratif) et une machine louée.
  - **(b) Substitut maison** (B, D) — avantage : déjà codé, peu coûteux ; inconvénient : seulement inspiré, jamais reproduit, seuil non essayé.
  - **(c) La chaîne de MiroGraph** (antériorité ; aucune espèce ne l'a pesée) — avantage : le portage hors physique est déjà fait, avec une garde de fuite ; inconvénient : appels à des modèles d'OpenAI (dépense, envoi de données), licence du code non vérifiée, rien exécuté.
  - Pour toutes : flanquer le bras de l'**allocation de ressources** (déjà codée) et d'un témoin **« sans paire »** (SciMuse).
- **Recommandation** : **(a)** si un essai sans dépense montre que leurs scripts tournent sur notre corpus **sans qu'on écrive de code** — c'est alors « tel quel » au sens de ta phrase, dont le critère est « écrit-on du code ? » ; sinon **(b)** ; **(c)** à lire (licence, code) avant toute dépense. Si l'allocation de ressources égale leur réseau, « garder Gu-Krenn » revient à garder l'allocation de ressources (A). Confiance **0,55**.
- **Nœud** : c'est le sens de ta propre décision, et la voie (a) ou (c) engage une dépense ; pas de défaut.

### (iii) Lancer le tour 2 (devis chez session-depot)

- **Décision** : lancer ou non le tour 2 du collisionneur sur la boucle (attaque des recommandations), sur devis.
- **Enjeu** : le tour 1 a coûté 12,61 dollars (douze cellules, chiffre de la synthèse, non vérifié ici) ; Q6 a été répondue sans l'antériorité ; deux accords à quatre (l'ordre, la circularité) sont soufflés par la question ; la liste du tour 2 de la synthèse perd quatre divergences et range mal A ; la décision (i) ne dépend pas du tour 2, la (ii) en partie.
- **Options** :
  - **(a) Tour 2 complet, quatre espèces** — avantage : tout est remis à l'épreuve avec l'antériorité ; inconvénient : dépense de l'ordre du tour 1 ou plus, délai.
  - **(b) Tour 2 ciblé** sur les onze divergences maintenues, les deux accords soufflés (ordre, circularité) et la voie MiroGraph, en servant l'antériorité vérifiée (SciMuse, HindSight, MiroGraph ; MAGenIdeas comme anecdote) et les § 4 et 11 du dossier, **après erratum de la synthèse** — avantage : moins cher, porte là où l'antériorité change le plus, conforme à ton choix pour les nœuds N12 et N13 (« à résoudre », tour 2 ciblé, R-1042) ; inconvénient : Q1 et Q2 restent sur le tour 1.
  - **(c) Pas de tour 2** — avantage : zéro dépense, tu tranches (i) maintenant ; inconvénient : « tel quel » et la fuite par les modèles restent sans contradicteur informé.
- **Recommandation** : **(b)**, sur devis, après erratum ; ne pas suspendre (i) en l'attendant ; confiance **0,6**.
- **Nœud** (dépense) : devis et ligne de GO chez session-depot, sur ton mot direct dans sa session.

## 4. Erratum à demander à session-depot (avant le tour 2)

1. Recompter, règle écrite : accords indépendants (T1 seulement), convergences, divergences résolues (en les nommant), maintenues, apports seuls (RB-01 à RB-05).
2. Marquer « vrai par construction » ou « soufflé » : Q1 « affiner = reformuler » ; Q5 circularité ; Q5 témoin allocation de ressources (RB-06).
3. Q6 : supprimer l'« accord à quatre » contradictoire ; reformuler Q6-a sur ses deux axes ; ranger A avec C sur l'action (RB-07).
4. Rétablir Q3-c, Q4-b, Q5-b, Q7-b dans la liste du tour 2 ; ajouter le coût de la reproduction de Gu et Krenn (RB-04).
5. Scinder l'accord Q2 en « garde » (à quatre) et « dérivation » (C, D) (RB-08).
6. Dire si B était servie en Opus 4.6 comme prévu ou par repli (RB-12).
