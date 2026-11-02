# Faits servis — collisionneur « boucle itérative moisson ↔ fiches ↔ bisociateur » — v1

Assemblés par session-depot (instance 3, seconde session), 1er novembre 2026, selon la liste « Pièces servies » de la question v1 de conv-audit (`72b4f149…`). Règle 2 : les recommandations, confiances d'auteur et défauts sont retirés quand ils portent sur la question posée ; les étiquettes d'état du dossier factuel (DÉCIDÉ / PROPOSÉ / etc.) sont gardées comme faits. La pièce 5 (antériorité de la boucle) n'était pas rendue au lancement : non servie. Niveau méthode ; aucune pièce du bras d'attaque.

### Pièce 1 — dossier factuel de l'organisme, § 1, 2, 3, 7, 9, 10 (`docs/notes/ideation-organisme-v1/explication-organisme-v1/dossier-factuel-organisme-v1.md`, `0751fc8cf4aa…`, extraits)

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


### Pièce 2 — rétrodiction de Swanson (`retrodiction-swanson-v1.md`, `057ef8a5314f…`, entier)

# Rétrodiction sur arXiv : la marche « à la Swanson » relie-t-elle mieux les champs éloignés ? — v1

Exécution du brief `BRIEF-retrodiction-swanson-v1.md` (empreinte `3b83d113…c7c0e4`) selon le préenregistrement
`preenregistrement-retrodiction-v1.md` (empreinte `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb`,
scellé à 20:13:35 UTC, avant tout calcul). Sous-agent neuf de la lignée conv-audit, 26 octobre 2026.

## Décisions (figées par le brief, découpage principal : avant 2003-2010, après 2011-2016)

- **D1 — réfutée.** Précision à 10 000 : marche à la Swanson (S) **9,83 %** [9,22 ; 10,44] contre tirage stratifié (ST)
  **0,22 %** [0,14 ; 0,32] ; écart **+9,61 points** [+8,98 ; +10,23], sous le seuil de 12 points. La marche n'est pas
  retenue comme règle de tirage de la version 0.
- **D2 — pas de contribution.** Meilleure méthode classique = **allocation de ressources (RA) : 10,65 %**
  [10,08 ; 11,23]. Écart S − RA = **−0,82 point** [−1,43 ; −0,25] : S est *en dessous*, pas 2 points au-dessus ; les
  intervalles se recouvrent. Selon la règle, on adopte l'allocation de ressources **sous son nom**, sans revendication.
- Contrôles : permutations des issues réussies (toutes les méthodes au taux de base) ; placebo 2003-2006 / 2007-2010
  **stable** (même ordre des cinq méthodes à score, tau de Kendall = 1 sur les sept) ; essais d'absence de fuite
  temporelle réussis (cas sain, artefact pris, référence lente à 4e−15 près).

Les nombres (intervalles à 95 % par rééchantillonnage des paires, 1 000 tirages) viennent de
`resultats/issues-v1.json` et `resultats/synthese-v1.json` (empreintes dans la table des sources, fin du document).

## Résultats du découpage principal

1 000 000 de paires candidates, 2 752 positives : **taux de base 0,2752 %** [0,2651 ; 0,2857] (Wilson).

| méthode | précision à 1 000 (%) | précision à 10 000 (%) | précision moyenne (%) | aire sous la courbe de fonctionnement du récepteur |
|---|---|---|---|---|
| S, marche à la Swanson (moyenne des deux sens) | 19,20 [16,90 ; 21,80] | **9,83** [9,22 ; 10,44] | 9,05 [8,38 ; 10,01] | **0,9595** [0,9572 ; 0,9618] |
| AA, Adamic-Adar | 24,20 [21,50 ; 26,80] | 9,05 [8,52 ; 9,65] | 9,47 [8,59 ; 10,52] | 0,9419 [0,9384 ; 0,9455] |
| RA, allocation de ressources | **28,40** [25,70 ; 31,30] | **10,65** [10,08 ; 11,23] | **12,16** [11,14 ; 13,36] | 0,9574 [0,9547 ; 0,9602] |
| CN, voisins communs | 23,70 [21,10 ; 26,30] | 8,87 [8,33 ; 9,45] | 9,16 [8,29 ; 10,18] | 0,9396 [0,9361 ; 0,9432] |
| PA, attachement préférentiel | 11,40 [9,60 ; 13,40] | 5,62 [5,19 ; 6,07] | 3,79 [3,45 ; 4,25] | 0,8897 [0,8840 ; 0,8951] |
| ST, tirage stratifié | 0,30 [0,00 ; 0,60] | 0,22 [0,14 ; 0,32] | 0,27 [0,26 ; 0,29] | 0,4975 [0,4868 ; 0,5082] |
| U, tirage uniforme | 0,30 [0,00 ; 0,70] | 0,25 [0,16 ; 0,36] | 0,27 [0,26 ; 0,29] | 0,4964 [0,4861 ; 0,5073] |
| S(A→C), sens unique (secondaire) | 18,20 [15,90 ; 20,60] | 7,98 [7,46 ; 8,56] | 6,52 [5,94 ; 7,34] | 0,9176 [0,9133 ; 0,9220] |
| S(C→A), sens unique (secondaire) | 9,80 [7,90 ; 11,60] | 4,11 [3,69 ; 4,49] | 2,67 [2,37 ; 3,07] | 0,8768 [0,8720 ; 0,8816] |

Écarts de précision à 10 000, appariés (points ; dans les deux sens) : S − ST **+9,61** [+8,98 ; +10,23] ;
S − RA **−0,82** [−1,43 ; −0,25] ; S − AA +0,78 [+0,12 ; +1,42] ; S − CN +0,96 [+0,30 ; +1,59] ; S − PA +4,21
[+3,69 ; +4,76].

Lecture, sans changer les décisions :
- S bat Adamic-Adar, voisins communs et attachement préférentiel à 10 000, de moins d'un point face aux deux premiers ;
  elle perd contre l'allocation de ressources à 10 000, et plus nettement en tête de liste (précision à 1 000 :
  19,2 % contre 28,4 %, la plus faible des quatre méthodes de cooccurrence) et en précision moyenne (9,05 % contre 12,16 %).
- Seule mesure où S devance RA : l'aire sous la courbe (0,9595 contre 0,9574), intervalles qui se recouvrent. S
  ordonne un peu mieux le gros de la liste, moins bien la tête — or c'est la tête que mesure la décision.
- Le choix préenregistré de la moyenne des deux sens n'a pas desservi S : chacun des deux sens seuls fait pire
  (7,98 % et 4,11 %).
- L'avantage de toutes les méthodes sur ST ne tient pas au choix des strates : la précision qu'aurait la tête de liste
  de chaque méthode avec sa seule composition par strates est de 0,23 à 0,30 % (audit n° 2, non préenregistré).

Taux de base par paire de champs (Wilson ; aucune strate ne touche « stat », qui n'a aucun terme candidat) :

| strate | paires candidates N_s | paires tirées | taux de base (%) |
|---|---|---|---|
| math – cs | 2 469 001 | 17 489 | 0,36 [0,28 ; 0,46] |
| math – physique | 112 832 560 | 799 241 | 0,17 [0,16 ; 0,18] |
| math – q-bio | 258 547 | 1 831 | 0,11 [0,03 ; 0,40] |
| math – q-fin | 6 834 | 49 | 0,00 [0,00 ; 7,27] |
| cs – physique | 23 113 888 | 163 726 | 0,76 [0,72 ; 0,80] |
| cs – q-bio | 52 064 | 369 | 0,00 [0,00 ; 1,03] |
| cs – q-fin | 1 436 | 10 | 0,00 [0,00 ; 27,75] |
| physique – q-bio | 2 374 883 | 16 822 | 0,47 [0,38 ; 0,58] |
| physique – q-fin | 65 247 | 462 | 0,00 [0,00 ; 0,82] |
| q-bio – q-fin | 150 | 1 | 0,00 [0,00 ; 79,35] |
| les cinq strates avec stat | 0 | 0 | — |

Strate « dominée par les termes passe-partout » (plus de la moitié de la masse de S par les 432 termes du 1 % le plus
fréquent) : **494 paires, une seule positive**. Précision à 1 000 et à 10 000 non définies (strate plus petite que k,
règle préenregistrée) ; la précision moyenne et l'aire y reposent sur une seule positive : aucune lecture possible.

## Contrôles

**(a) Issues permutées.** 20 permutations par découpage ; toutes les méthodes restent au taux de base (critère :
moins de 4 erreurs-types). Principal : précision à 10 000 moyenne de 0,27 à 0,29 % pour un taux de base de 0,2752 %,
écarts de −0,61 à +1,43 erreur-type ; aire de 0,4965 à 0,5014, écart le plus grand −2,81 erreurs-types (S). Placebo :
écarts tous sous 1,9 erreur-type. Comme les écarts d'aire au découpage principal penchaient tous du même côté (−1,85 à
−2,81 pour les méthodes à score), je les ai audités (non préenregistré) : 200 permutations de plus, autre graine →
aire à −0,18 à −1,21 erreur-type, écart-type observé 0,0050 à 0,0051 contre 0,0055 en théorie ; précision à 10 000 à
−1,4 à −2,3 erreurs-types, même signe pour toutes. Sous permutation, l'espérance est exactement le taux de base et 0,5 ;
ces écarts de même signe viennent de permutations communes et de têtes de liste qui se recouvrent (fluctuation
corrélée, moins de 0,01 point en valeur absolue), pas d'une fuite.

**(b) Placebo 2003-2006 / 2007-2010** (chaîne entière refaite : 180 284 documents d'avant, 248 918 d'après, 19 975 termes,
1 000 000 de paires, taux de base 0,528 % [0,514 ; 0,542]). Précision à 10 000 : RA 16,17 % [15,38 ; 16,83] > S 13,67 %
[13,03 ; 14,43] > AA 12,65 % > CN 12,29 % > PA 8,75 % > U 0,55 % ≈ ST 0,54 %. **Même ordre qu'au découpage principal :
« stable »**, tau de Kendall = 1,0. Écarts : S − RA −2,50 [−3,24 ; −1,57] ; S − ST **+13,13** [+12,47 ; +13,83].
Au placebo, la règle D1 aurait **retenu** S ; elle la réfute au découpage principal. Le préenregistrement fait décider
le seul découpage principal ; ce basculement est une réserve sur le seuil, traitée plus bas.

**(c) Absence de fuite temporelle.**
- Essai synthétique avec la chaîne même du calcul réel (`code/essais_v1.py`, `resultats/essais-v1.json`) : documents
  d'après mélangés, retirés, ou bourrés des paires candidates → vocabulaire, champs, candidats, paires tirées et scores
  identiques au bit près, issues changées ; un document d'avant modifié → tout change ; un calculateur volontairement
  fuyant est pris par la garde ; calcul à deux processus identique au calcul à un processus.
- Données réelles (`resultats/scores-bilan-v1.json`) : matrices d'avant limitées à 2003-2010 (2003-2006 au placebo) ;
  les fréquences d'avant de la matrice sont égales à celles de la passe d'extraction ; 1 000 paires recalculées par une
  implémentation lente sur les seuls documents d'avant (écart relatif maximal 4,0e−15, 3,3e−15 au placebo) ; degrés et
  normalisations r exacts sur 300 termes ; aucune des 2 000 000 de paires tirées ne cooccurre avant.
- Chronologie : scores écrits et empreintés à 20:30:32 et 20:32:31 UTC ; issues calculées à partir de 20:33:11 UTC.

## Description du corpus et du tirage

- 999 260 lignes, 999 213 articles (37 identifiants en double réduits). Avant : 429 202 ; après : 570 011.
- Vocabulaire : 43 162 termes (dont 27 583 bigrammes) de fréquence documentaire 50 à 21 460 ; 48,8 termes de vocabulaire
  par document d'avant ; 2 688 668 termes distincts avant (risque de conflit d'empreinte borné par 2e−7 ; aucun conflit
  touchant le vocabulaire).
- Part des documents d'avant : physique 73,9 %, math 19,4 %, cs 4,9 %, q-bio 1,1 %, stat 0,44 %, q-fin 0,30 %.
- Termes candidats (spécifiques, fréquence 50 à 3 000) : physique 33 078, math 3 497, cs 722, q-bio 75, q-fin 2, stat 0.
  141 174 610 paires candidates ; tirage proportionnel → 80 % de paires math – physique, 16 % cs – physique.
- Toutes les paires tirées ont au moins un voisin commun (K > 0).

## Ce que le test ne dit pas

- **Des termes ne sont pas des concepts.** Les unigrammes et bigrammes de titres et de résumés mêlent synonymes,
  polysémies et mots de discours. Les têtes de liste le montrent : celle de S ressemble à des ponts de physique
  mathématique (« toric variety — witten », « hopf — supergroups », « projective curves — calabi yau ») ; celle de RA
  est faite de mots courants (« ball — consistently », « users — shifts », « resp — thought », « proofs — vice »), qui
  cooccurrent pourtant plus souvent ensuite. L'issue mesurée est la **cooccurrence lexicale future**, pas une découverte
  féconde. Cette impression vient de 15 exemples et ne sert pas à racheter S.
- **arXiv n'est pas toute la littérature** : physique surreprésentée (74 % des documents d'avant), statistique et finance
  quantitative presque absentes avant 2011, pas de biomédecine (le terrain d'origine de Swanson).
- **« Champs éloignés » se réduit ici, pour l'essentiel, à math – physique et cs – physique**, deux champs reliés par la
  physique mathématique. Le test ne dit rien des champs vraiment lointains.
- **Le régime « termes passe-partout » n'est pas testé** : la strate est vide en pratique (494 paires sur 1 000 000, une
  positive). Le +17 points des mondes synthétiques n'est donc ni confirmé ni réfuté.
- Précision à 10 000 sur un échantillon d'un million = précision du premier centile de la population (≈ 1,4 million de
  paires sur 141 millions). Ce n'est pas la précision des 10 000 meilleures paires de la population entière.
- Une seule fenêtre (2011-2016), un seul seuil d'issue (3 documents), une seule graine par tâche, un seul corpus.
- La précision à 10 000 seule décide. S a la meilleure aire mais une tête plus faible.
- S et RA choisissent des têtes presque disjointes (2 378 paires communes sur 10 000), avec des taux de réussite voisins
  (983 et 1 065 positives). Leur combinaison est une **question ouverte**, à préenregistrer ; elle n'est pas testée ici
  et rien ne s'en revendique.

## Points du brief que je crois mal posés (dits à part ; décisions inchangées)

1. **Spécificité non normalisée par la taille des champs.** Avec 74 % des documents d'avant en physique, un mot réparti
   au hasard a 74 % de ses documents en physique : il devient « spécifique » de la physique (« consistently »,
   « thought », « apparently »…). La statistique n'a aucun terme spécifique. Une spécificité relative à la part du champ
   serait plus fidèle à l'idée de « champs éloignés ».
2. **La strate « passe-partout » est vide par construction.** Le vocabulaire exclut les termes de plus de 5 % des
   documents (les vrais termes passe-partout). De plus, P(C|B) = n(B,C)/r(B) donne peu de masse aux intermédiaires
   fréquents : par le 1 % le plus fréquent passent 22 % de la masse de S en médiane, 38 % au 99e centile. Le motif
   principal du test (le +17 points) ne peut donc pas être éprouvé avec ces définitions.
3. **Le seuil de D1 est absolu alors que ST vaut le taux de base.** Le verdict dépend du taux de base : 9,61 points à
   0,28 % (réfutée) et 13,13 points à 0,53 % (placebo, retenue), pour un même ordre des méthodes. En relatif, S
   multiplie le taux de base par 36 (principal) et 26 (placebo). Un seuil relatif, ou calé sur le taux de base, voyagerait
   mieux. L'allocation de ressources, adoptée par D2, ne passerait pas non plus la barre de D1 (+10,43 points).
4. **Le sens de la marche n'était pas fixé.** Le préenregistrement a tranché pour la moyenne des deux sens, qui
   l'emporte sur chaque sens seul ; aucune décision n'en dépend.
5. **« Paires possibles de chaque strate » était ambigu.** Lu comme le nombre exact de paires candidates. Les paires
   cooccurrentes écartées font de 0 à 4,3 % des paires |T_f|·|T_g| selon la strate (2,5 % pour math – physique) :
   l'autre lecture aurait à peine changé l'allocation.

## Écarts au préenregistrement

Aucun sur les définitions, les seuils, les périodes, le vocabulaire ou les décisions. Ajouts **non préenregistrés**,
signalés comme tels, sans effet sur les décisions :
- `resultats/audit-v1.json` : 200 permutations de plus ; parts des groupes ; masse de S par le 1 % le plus fréquent ;
  recouvrement des têtes de liste ; fréquences des termes en tête.
- `resultats/audit-strates-v1.json` : composition par strates des 10 000 premiers de chaque méthode.

## Sources (chemins sous `sortie/`, empreintes SHA-256)

| fichier | empreinte |
|---|---|
| `preenregistrement-retrodiction-v1.md` | `7a4868aa48cfff5eb48937b0a1a99647fc9968c44c1fe8a7bb8047629b3c91eb` |
| `resultats/synthese-v1.json` (D1, D2, stabilité) | `345e9a4e955f4f41baa24e4983379b0e46d12893f0bd62ab9cf4ed14c50d1ce8` |
| `resultats/issues-v1.json` (mesures, intervalles, permutations, strates) | `dd16d06e6feb59d85f38503cf4eba47fd9b134a0c13059664dd8e69fdc76373e` |
| `resultats/scores-bilan-v1.json` (corpus, vocabulaire, strates, contrôle de référence) | `54463b67fd7c13368b80b34d7926eab1feceeca95f11e4833c912217f4c0c371` |
| `resultats/essais-v1.json` (essais automatiques) | `b9c5b7cafb6e9dca0c2237877df58d358621ef6cb08097af83d714f3a94deb28` |
| `resultats/audit-v1.json` (non préenregistré) | `7f19db8caf136581f16f7b74cbedf14d69140dda2867ad8baf531ca8a387ac26` |
| `resultats/audit-strates-v1.json` (non préenregistré) | `e0700fbaf621e753b5f3a4ed0c6e2470bfffa681b47bb6c5e80535f3c1b4aa8b` |
| `resultats/scores-principal-v1.npz` (scores par paire) | `0850c7e33011fc89e94dd3f4cfd83a8ed8ee47e0ef8871035b5a6814bab92b0d` |
| `resultats/issues-principal-v1.npz` (issues par paire) | `31fbb60da3739cdbd7e7076f22c96c7af486baa9989afb202e5f6e481b1077ab` |
| `resultats/vocabulaire-principal-v1.npz` | `06c065948f0235711492cf58694d9687e50e326f9df20abf7ce781e2f237bff4` |
| `resultats/scores-placebo-v1.npz` | `173684c34fd58162a45f35f65b58393d345b9ab6f2313d1fbb3ff187412c2b49` |
| `resultats/issues-placebo-v1.npz` | `700db17558fc94406f68acf097f17308e32a1ea7a98ac0550dcddd04ff52525e` |
| `resultats/vocabulaire-placebo-v1.npz` | `c73f0c98e588ceb60907b4bd213be08d644b7ff4378bfe6672b33c9663be824d` |

Code (`code/`, chaque fichier a son compagnon `.sha256`) : `termes_v1.py`, `corpus_v1.py`, `chaine_v1.py`,
`mesures_v1.py`, `essais_v1.py`, `lancer_v1.py` (étapes `essais`, `scores`, `issues`, `synthese`), `tables_rapport_v1.py`,
`audit_v1.py`, `audit_strates_v1.py`. Empreintes, versions (Python 3.13.17, numpy 2.3.4, scipy 1.16.3, duckdb 1.4.1),
graines (`SeedSequence(20261026)`, clés d'engendrement par tâche) et heures sont consignées dans chaque fichier JSON et
dans `manifeste-v1.json`. Journaux : `travail/journal-*-v1.txt`. Matrices d'après intermédiaires : `travail/apres-*-v1.npz`.

Horodatage : écrit le 2026-10-26 20:52:23 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne).


### Pièce 3 — état des lieux de Gu et Krenn (`docs/notes/gu-krenn-v1/etat-des-lieux-gu-krenn-v1.md`, `1c1618a2484b…`, entier) et décision de Lazar du 1er novembre

Décision de Lazar (1er novembre 2026, rapportée par conv-audit, n° 312) : « on garde Gu-Krenn tel quel dès que c'est possible sans recoder nous-mêmes, on s'inspire à fond quand il faut coder ».

# État des lieux — Gu et Krenn 2024 (« Impact4Cast »), avant reproduction et test hors échantillon — v1

Lignée « session-depot », 31 octobre 2026, 02:15–03:00 UTC. Demande : message n° 261 de conv-audit
(`origin/canal/conv-audit-n04:brouillons/canal-reprise-releve-v1/messages/conv-audit_2026-10-30_n261.md`), qui cite le
brief `brief-nouvelle-lignee-bisociateur-v1.md` de la même branche (empreinte vérifiée contre son `.sha256` :
`2cdf135fff340960…`, conforme).

**Ce que cette note n'est pas.** Aucun code de Gu et Krenn n'a été exécuté ; aucune donnée lourde n'a été
téléchargée ; aucune aire sous la courbe ni aucune autre métrique n'a été calculée, ni sur leurs données ni sur
OpenAlex (R1). Les seuls comptes produits sont des comptes de chaînes dans leur liste de concepts (§ 5), qui ne sont pas
une mesure de résultat. Aucune dépense ; aucune requête à l'interface payante d'OpenAlex ; aucune clé lue.

Source primaire : `docs/sources/pdf/bisociation-fertilite-v1/arxiv-2402.08640-gu-krenn-2024.pdf`, empreinte
`6b3d29db7cd6f7de…` (vérifiée, conforme), version arXiv **v4 du 11 juin 2025**, 18 pages. Pages citées selon la
numérotation imprimée du PDF. Version publiée : *Machine Learning: Science and Technology* 6(2), 025041 (2025) (selon le
LISEZMOI du dépôt de code ; non vérifiée sur la version publiée, que nous n'avons pas — R7 : les chiffres ci-dessous
sont ceux de la v4).

---

## 0. Ce que fait le papier (lecture du PDF)

**Tâche exacte.** Ce n'est pas une prédiction de liens au sens strict : c'est une **prédiction d'impact** de paires de
concepts encore jamais reliées. Pour une paire non reliée à la fin de l'année *y*, prédire si, dans les trois ans qui
suivent, elle sera reliée par des articles qui cumulent **au moins IR citations** (« impact range ») ; classification
binaire (p. 4, § « Forecasting impact… » ; légende de la fig. 4, p. 5). Une paire qui reste non reliée vaut 0 citation
(code : `prepare_unconnected_pair_solution.ipynb`, colonne `citation` mise à 0). Une variante « au-delà de la
prédiction de liens » conditionne sur les paires qui se relient effectivement, et classe 0–5 contre ≥ 100 citations
(fig. 4(d), p. 5).

**Graphe de concepts.**
- Sommets : **37 960 concepts** du domaine optique et physique quantique (p. 3 ; annexe B, p. 10), tirés d'une liste
  générale de **368 825 concepts** extraits par l'algorithme d'extraction automatique de mots-clés RAKE des titres et
  résumés de **2 444 442 prépublications** (arXiv, bioRxiv, medRxiv, chemRxiv ; coupure février 2023) ; seuils : 9
  articles pour les concepts de deux mots, 6 pour trois mots et plus ; filtres automatiques puis revue manuelle ;
  restriction au domaine par les 78 084 articles arXiv `physics.optics` et `quant-ph` (87 741 candidats, puis 37 960
  après filtrage et revue manuelle) (p. 2–3, p. 10).
- Arêtes : deux concepts sont reliés quand ils **apparaissent ensemble dans le titre ou le résumé** d'un article de
  revue d'OpenAlex (p. 3). Le code (`create_dynamic_edges/get_concept_pairs.py`) fait une **recherche de sous-chaîne
  brute** (`if concept in curr_article`) sur le titre et le résumé reconstitué, mis en minuscules, tirets remplacés par
  des espaces, **sans limite de mot** (l'exemple du papier, p. 10, attribue d'ailleurs « ring theory » à un article sur
  la « string theory »).
- Articles retenus : type `journal-article` avec titre, date et résumé (`_get_openalex_workdata.py`) ; 92 millions
  d'articles après filtrage (68 Go compressés), dont 21 165 421 forment au moins une arête (fig. 1, p. 2 ; p. 10).
- Graphe final : 37 960 sommets, **26 010 946 arêtes uniques**, 193 977 096 paires avec multiplicité (p. 11) ;
  instantané OpenAlex, coupure **avril 2023** (p. 3).
- Poids : chaque arête porte la date de l'article (jours depuis le 1er janvier 1990) et ses citations annuelles **2012 à
  2023** plus le total ; les arêtes multiples additionnent les citations (p. 3, p. 11).

**Partage temporel.** « Année *y* » = graphe des articles publiés jusqu'au 31 décembre de *y* (code : `day_2016 =
(date(2016,12,31) - day_origin)`).
- Entraînement : paires non reliées en **2016**, cible en **2019** (citations cumulées des années 2017, 2018 et 2019
  des articles qui créent l'arête). Environ **689 millions** de paires non reliées en 2016 ; toutes les positives
  (≥ IR) et autant de négatives tirées au hasard ; 85 % entraînement, 15 % « test » (p. 11).
- Évaluation : **10 millions** de paires non reliées en **2019**, tirées au hasard, cible en **2022** (citations 2020 à
  2022), réseau entraîné sur 2016→2019 seulement (p. 4 ; fig. 3, p. 4 ; p. 11).
- Banc d'essai (fig. 6, p. 7 ; p. 8–9) : intervalles d'entraînement de 2, 3 ou 4 ans et d'évaluation de 1 à 5 ans, fin
  d'évaluation fixée à 2022, sur **1 million** de paires ; seuils IR = 10 et 50 ; quatre modèles (réseau
  entièrement connecté, transformeur, forêt aléatoire, XGBoost). Variante sans réentraînement : entraîné 2014→2017,
  évalué de 2017 vers 2018 à 2022 (fig. 7, p. 8).

**Traits d'entrée.** 141 traits par paire : 41 de réseau (20 de sommet : voisins, nouveaux voisins, rangs, PageRank sur
*y*, *y*−1, *y*−2 ; 21 de paire : voisins communs, similarités géométrique, cosinus, Simpson, attachement
préférentiel, Sørensen–Dice, Jaccard) et 100 de citations (58 de sommet, 42 de paire) (p. 4 ; tableaux I et II,
p. 14–15). **Normalisation** (code `features_utils.py`) : traits de sommet divisés par leur maximum par ligne ; traits
de paire divisés par leur maximum **sur l'échantillon évalué** (`rescaling_col`) ou par un maximum du graphe entier
pré-calculé (`get_norm_features`) — le choix change la valeur des traits selon la composition de l'échantillon (voir
§ 4, piège 5).

**Modèle.** Réseau entièrement connecté, **quatre couches cachées de 600** (p. 4 ; annexe C, p. 11 ; code
`train_model_utils.ff_network`), perte quadratique sur sortie unique, Adam, taux 3 × 10⁻⁵, lots de 1000 équilibrés
(p. 11), arrêt précoce sur moyenne mobile de la perte de test. Le banc d'essai utilise **trois** couches cachées de 600
(≈ 800 000 paramètres), lots de 2048, taux 10⁻⁴, patience 500 (p. 8 ; `benchmark_code/loops_fcNN.py`).

**Métrique.** Aire sous la courbe caractéristique de fonctionnement du récepteur (taux de vrais positifs contre taux
de faux positifs), « probabilité qu'un exemple vrai tiré au hasard soit classé au-dessus d'un exemple faux tiré au
hasard » (p. 4), calculée sur le classement des sorties brutes du réseau (`sklearn.metrics.roc_auc_score`), pour
l'ensemble « test » (paires de 2016 hors entraînement) et l'ensemble d'évaluation (2019→2022), **horizon trois ans**
dans l'expérience principale.

**Valeurs publiées (R7, page citée, lues sur le PDF v4 empreinté).**

| Expérience | Valeur | Page |
|---|---|---|
| Résumé : « au-delà de 0,9 pour la plupart des expériences » | — | p. 1 |
| Fig. 4(a) : test 2016→2019 et évaluation 2019→2022, IR de 1 à 200 | « au-delà de 0,8, le plus souvent au-delà de 0,9 » (courbe seulement, pas de tableau) | p. 4–5 |
| Évaluation 2019→2022, IR = 10 | 0,94 | fig. 11, p. 12 |
| Évaluation 2019→2022, IR = 50 | 0,96 | fig. 11, p. 12 |
| Évaluation 2019→2022, IR = 100 | 0,95 (fig. 11) ; **0,948** (texte de l'annexe D) | p. 12 |
| Fig. 4(d), paires reliées conditionnées, {0–5, ≥ 100} : test / évaluation | **0,747 / 0,694** (texte : « au-delà de 0,7 » et « au-delà de 0,67 ») | p. 5 |
| Banc, IR = 10, entraînement 2016–2019, évaluation 2019–2022 : réseau / transformeur / forêt / XGBoost | **0,9455 / 0,9454 / 0,9431 / 0,9442** | fig. 6(a), p. 7 |
| Banc, IR = 50, même découpage | **0,9588 / 0,9532 / 0,9602 / 0,9561** | fig. 6(b), p. 7 |
| Banc, entraînement 2014→2017 sans réentraînement, réseau IR = 10, évaluation jusqu'à 2018 … 2022 | 0,9463 ; 0,9416 ; 0,9373 ; 0,9332 ; 0,9311 | fig. 7, p. 8 |
| Meilleur trait seul (Simpson, année *y*) | 0,8880 | fig. 12, p. 13 |
| Moyenne des citations sur les 10 millions de paires d'évaluation | 0,029 citation | légende fig. 4, p. 5 |

Les valeurs du banc ont été associées à leur panneau par les coordonnées du texte du PDF, puis vérifiées à l'œil sur
la page 7 rendue en image. Aucune incertitude n'est publiée (une seule course par cas, graine 42).

**Code et données annoncés (p. 9).** Code : `https://github.com/artificial-scientist-lab/Impact4Cast`. Données :
`https://doi.org/10.5281/zenodo.10692137` ; banc : `https://doi.org/10.5281/zenodo.14527306`.

---

## 1. Où sont le code et les données ; licences, tailles, dates

**Code** — cloné (`git clone --depth 1`, puis historique approfondi pour les dates) dans
`docs/notes/gu-krenn-v1/sources-amont-v1/Impact4Cast/` ; tête `d2af4f3d69e1e5272c168d3f950b56b31845a51f`
(2026-07-19, « Update README.md ») ; dernière modification de code : 2025-04-23 (`features_utils.py`) ; premier commit
2024-02-12 ; 125 commits. **Licence MIT.** 8,9 Mo, 49 fichiers suivis. Le dossier `.git` a été archivé dans
`Impact4Cast-git-d2af4f3-v1.tar` (`68d3fb3c58481d4d…`) puis retiré du dossier pour que chaque fichier puisse être
scellé (R6) ; la liste des fichiers avec leurs empreintes de blob git est dans `Impact4Cast-ls-files-d2af4f3-v1.txt`
(`c6e30125163b8d57…`), le journal dans `Impact4Cast-journal-d2af4f3-v1.txt` (`78a08cab8d1798ff…`).
Pas de fichier de dépendances (aucun `requirements.txt`). Code lu, jamais exécuté.

**Données** — métadonnées seules (interface Zenodo `/api/records/<id>`, puis répertoire central de chaque archive lu
par requêtes partielles, quelques kilo-octets chacune ; script `scripts-v1/liste_zip_distant_v1.py`
`82b1b06ffbe9639c…`). Fichiers dans `sources-amont-v1/zenodo-metadonnees-v1/`.

| Dépôt Zenodo | Licence | Publié | Archive | Taille | Contenu (répertoire central) |
|---|---|---|---|---|---|
| 10692137 « Impact4Cast » | CC-BY-4.0 | 2024-02-27, jamais mis à jour | `data_concept_graph.zip` | 1,25 Go | `full_dynamic_graph.parquet` (666 Mo), `full_dynamic_concept.parquet` (593 Mo), `full_domain_concepts.txt` (812 ko, même taille que celui du dépôt de code) |
| | | | `data_for_features.zip` | 2,64 Go | matrices d'adjacence 2012–2022 (`.gz`, **pickle**), PageRank 2012–2022 (pickle), citations par concept et par paire 2014–2022 (parquet) |
| | | | `data_eval.zip` | 5,65 Go | `eval_data_pair_feature.parquet` (4,12 Go : les 141 traits des 10 millions de paires 2019), solutions (87 Mo), variante conditionnée (1,41 Go + 26 Mo) |
| 14527306 « Benchmark » | CC-BY-4.0 | 2024-12-19, jamais mis à jour | `benchmark_data_for_train.zip` | 10,66 Go | 30 fichiers `train_data_<a1>_<a2>_IR<10|50>.parquet`, 310–372 Mo chacun |
| | | | `benchmark_data_for_eval.zip` | 6,98 Go | 20 fichiers `eval_data_<a1>_2022_IR<10|50>.parquet`, 317–361 Mo chacun |
| | | | `frp_example.zip` | 136 Mo | `solution_output_{10,50,100}.npy` (160 Mo chacun, décompressés) : **sorties brutes de leur réseau et vérité** sur les 10 millions de paires d'évaluation |

Total : 9,53 Go (données) + 17,77 Go (banc). Aucune donnée n'a été téléchargée : quatre archives dépassent 2 Go, et
les deux petites (`data_concept_graph.zip`, `frp_example.zip`) ont aussi été laissées de côté (rien n'en avait besoin
pour cet état des lieux).
Les membres des archives du banc sont presque non compressés (taille compressée ≈ taille) : un fichier isolé
(≈ 350 Mo) peut probablement être extrait par requêtes partielles sans tirer l'archive entière (non essayé).

**Point de vigilance R1** : `frp_example.zip` contient sorties et vérité ; en tirer une aire sous la courbe serait
une lecture de résultat. Ce fichier ne doit être ouvert qu'après scellement du préenregistrement.

---

## 2. Dépendances, matériel, temps

**Dépendances** (relevées dans les `import`) : torch, numpy, pandas (+ pyarrow pour parquet), scipy, networkx,
scikit-learn, xgboost, matplotlib, joblib ; pour reconstruire : boto3, jsonlines, rake-nltk/nltk. Aucune version
épinglée.

**Matériel publié** (annexe C, p. 12) : graphe et traits préparés sur un Intel Xeon Gold 6130 avec **1 Tio de mémoire**
(« pas strictement nécessaire ») ; graphe du domaine ≈ 23,12 Go ; entraînement principal sur **une carte graphique**
Nvidia Quadro RTX 6000, ≈ **1,5 h par valeur d'IR** ; banc d'essai sur **processeur** (même Xeon), mémoire < 15 Go,
≈ **1 h par tâche** (sauf le transformeur, carte graphique, ≈ 3 h).

**Ce conteneur** : 4 cœurs, 15 Go de mémoire, 9,1 Go de disque libre, ni torch ni pyarrow. Il ne suffit pas pour
les données principales (9,5 Go compressés, la matrice des traits d'évaluation fait à elle seule ≈ 10 millions × 141
réels, soit ≈ 11 Go en double précision) ; le banc d'essai est à la limite (< 15 Go selon le papier).

**Estimations (non mesurées ; à remplacer par une mesure sur machine louée)** :
- *Inférence seule* : ≈ 1,2 million de paramètres (quatre couches de 600) → ≈ 2 × 10⁷ opérations par paire ; 10
  millions de paires ≈ 2 × 10¹³ opérations, soit de l'ordre de **5 à 40 minutes sur 4 cœurs**. Le coût réel est
  ailleurs : **calculer les 141 traits** (matrices creuses de voisinage, ~10⁷ paires) et **régénérer les paires non
  reliées** (689 millions de paires pour 2016, jointures pandas avec indicateur : plusieurs dizaines de Go de mémoire).
- *Entraînement* : banc ≈ 1 h par tâche sur processeur (publié). Expérience principale : 1,5 h par IR sur carte
  graphique ; sur processeur, estimation grossière ×5 à ×20, soit **8 à 30 h par valeur d'IR** (nombre d'itérations
  avant arrêt précoce inconnu).
- **Poids publiés : non** (§ 3) — l'inférence seule n'est pas possible sans réentraîner.

---

## 3. Modèle entraîné publié ? Non.

Aucun fichier de poids (`.pt`) ni dans le dépôt de code ni dans les six archives Zenodo (répertoires centraux lus). Le
code sauve les réseaux en local (`torch.save(model)` et `state_dict`, `train_model_utils.py` l. 141–142) sans les
publier. **Il faut réentraîner.** Par ailleurs :
- Les paires d'entraînement de l'expérience principale (`data_pair_solution/unconnected_<a>_pair_solution_connected_<b>_clean.parquet`)
  **ne sont pas publiées** ; le carnet `prepare_unconnected_pair_solution.ipynb` produit la version sans suffixe
  `_clean` : l'étape de « nettoyage » n'est pas dans le code publié (inconnue I-5).
- Seul le banc d'essai fournit des jeux d'entraînement et d'évaluation prêts (traits déjà calculés) : c'est la voie de
  reproduction la moins chère.
- Le script principal boucle sur IR = 1 à 40 seulement (`IR_end=40`, commentaire « IR_end=200 ») : IR = 50 et 100
  demandent un changement de paramètre.
- Le script `train_model_2022_run.py` (entraînement 2019→2022, « pour de vraies prédictions de 2025 ») existe : c'est
  exactement le modèle à figer pour le test hors échantillon (§ 4).

**Sécurité** : les matrices d'adjacence et PageRank de Zenodo sont des **pickles** ; `torch.load` sans
`weights_only` charge aussi un pickle. Charger un pickle non sûr exécute du code. Règle proposée : ne jamais les
charger ; les régénérer depuis `full_dynamic_graph.parquet` (le code sait le faire si le fichier est absent), et ne
charger nos propres poids qu'en `weights_only=True`.

**Trois voies de reproduction**, de la moins chère à la plus fidèle :
- **(R-a) Banc d'essai** : réseau et XGBoost sur `train_data_2016_2019_IR{10,50}` et `eval_data_2019_2022_IR{10,50}`
  (≈ 1,45 Go en tout si l'extraction partielle marche, 17,6 Go sinon). Cibles : fig. 6, p. 7 (0,9455 et 0,9442 pour
  IR = 10 ; 0,9588 et 0,9561 pour IR = 50). Reproduit l'entraînement sur leurs traits, pas la construction du graphe.
- **(R-b) Expérience principale** : graphe + traits + évaluation (9,5 Go), régénération des paires (machine à
  ≥ 64 Go de mémoire, à confirmer), entraînement IR = 10, 50, 100. Cibles : 0,94 / 0,96 / 0,95 (fig. 11, p. 12) et
  0,948 (p. 12). C'est la seule voie qui donne un modèle 2016→2019 et 2019→2022 sur leur graphe, donc la base du test
  hors échantillon.
- **(R-c) Contrôle de cohérence** : recalculer l'aire sous la courbe à partir de `frp_example` (leurs propres sorties).
  Ce n'est pas une reproduction ; à préenregistrer comme contrôle, jamais avant scellement.

Une machine louée est nécessaire pour (R-b), probablement pour (R-a) : **nœud de dépense, devis et GO de Lazar**.

---

## 4. Test hors échantillon à partir d'OpenAlex

### 4.1 La moisson de `donnees/moisson-openalex-v1` ne couvre pas leurs concepts

Lu : requête déclarée v2 et les fiches `.moisson.json` (comptes et filtres, aucun contenu d'œuvre). Les cinq
sous-domaines (contrôle et alignement des intelligences artificielles, vérification formelle, sécurité des systèmes,
statistique séquentielle, neurosciences computationnelles) sont **disjoints** de l'optique et de la physique quantique,
et le `select=` garde `id, doi, title, publication_date, authorships, referenced_works, concepts, topics,
primary_location, type` : **ni résumé (`abstract_inverted_index`), ni `counts_by_year`, ni `cited_by_count`**. Or leur
graphe exige le résumé (repérage des concepts) et les citations annuelles (étiquettes). Non réutilisable.

### 4.2 Découpage proposé (à sceller avant toute lecture)

Leur graphe s'arrête en avril 2023 ; nous sommes le 31 octobre 2026. Une fenêtre de trois ans complète après leur
coupure n'existe que jusqu'à fin 2025.
- **Test principal, même tâche, même horizon** : traits à *y* = **2022** (fin décembre 2022) calculés sur **leur**
  graphe publié (les fichiers 2022 sont dans `data_for_features`) ; modèle figé = `train_model_2022_run.py`
  (2019→2022), entraîné par nous à l'identique ; étiquettes = arêtes nouvelles créées par les articles publiés du
  **1er janvier 2023 au 31 décembre 2025**, citations 2023 + 2024 + 2025, seuils IR = 10, 50, 100. Aucune information
  postérieure à 2022 n'entre dans les traits ni dans l'entraînement : c'est un vrai hors échantillon.
- **Test secondaire, « liens apparus de 2024 à 2026 »** (formulation du message n° 261) : graphe prolongé jusqu'à fin
  2023 par notre moisson, traits à *y* = 2023, étiquette = **apparition** de l'arête entre le 1er janvier 2024 et la date
  de moisson (fenêtre incomplète, ≈ 2 ans 10 mois). Leur modèle n'a pas été entraîné pour la prédiction de liens pure :
  le rapporter comme transfert de tâche, avec IR = 1 (au moins une citation) comme point le plus proche.

### 4.3 Requête OpenAlex (déclarée, non lancée)

Mêmes règles que leur code : articles de revue, titre et résumé présents, date de publication.
```
filter=from_publication_date:2023-01-01,to_publication_date:2025-12-31,has_abstract:true,type_crossref:journal-article
select=id,title,abstract_inverted_index,publication_date,cited_by_count,counts_by_year,type,type_crossref
per-page=200, sort=publication_date:asc, curseur
```
(le champ exact du type est une inconnue, I-2 : leur code filtre `type == 'journal-article'` sur l'ancien instantané ;
le type d'OpenAlex est devenu « article » et l'ancien vocabulaire survit dans `type_crossref`.) Puis traitement
**identique** au leur : `get_single_article_string` (minuscules, remplacements), recherche de sous-chaîne des 37 960
concepts, paires, horodatage en jours depuis 1990, citations annuelles.

**Volume et coût** : inconnus (I-1). Ordre de grandeur : leur filtre gardait 92 millions d'articles jusqu'en avril 2023 ;
trois années récentes en font vraisemblablement plus de 10 millions → plus de 50 000 pages de filtre, soit plus de 5 USD
au tarif déclaré dans `requete-declaree-v1.md` (0,0001 USD par page de filtre ; allocation gratuite de 1 USD par jour),
c'est-à-dire **plus d'une semaine d'allocation gratuite**, et des dizaines de Go de texte brut (le disque libre ici est
de 9 Go). Alternative sans crédit : l'**instantané public** d'OpenAlex (CC0, accès anonyme) — manifeste du 14 octobre
2026 lu : 464 765 485 œuvres, 1 898 fichiers parquet, **744 Go** (675 Go en lignes JSON compressées), partitionnés par
date de mise à jour, pas par date de publication ; le format parquet permet de ne tirer que les colonnes utiles, mais la
colonne des résumés reste le gros du volume. Les deux voies supposent une machine louée : nœud de dépense.

### 4.4 Témoins appariés sur le degré et l'âge

Pour chaque paire positive (*u*, *v*) (reliée dans la fenêtre, ≥ IR) : tirer *k* paires négatives (non reliées jusqu'à
la fin de la fenêtre) dans la même case de
(i) degré de chaque extrémité à *y*, ordonné (degré bas, degré haut), en classes de quantiles (ou classes log2) fixées
avant lecture ;
(ii) âge de chaque concept à *y* = *y* − année de sa première arête dans le graphe (tiré de `full_dynamic_graph`),
en classes fixées.
Graines par `numpy.random.SeedSequence` (R9). Rapporter : l'aire sous la courbe sur l'échantillon aléatoire « à leur
manière » (10 millions de paires) **et** sur l'échantillon apparié ; et les mêmes pour des bases simples figées
(attachement préférentiel, similarité cosinus seule, Simpson seule, degré seul). Le test apparié mesure ce que le modèle
sait au-delà de « les concepts populaires et anciens se relient davantage ».

### 4.5 Pièges à fixer dans le préenregistrement

1. **Dérive de la source** : OpenAlex est passé à « Walden » en novembre 2025 (`RELEASE_NOTES` du seau public :
   « switch to walden dataset », 463 millions d'œuvres avec les fiches « xpack »), avec retraits et récupérations de
   résumés (2025-01-29 : 350 000 résumés retirés ; 2026-06-25 : 1,4 million récupérés), reclassements de types
   (2024-07-30 : 4 millions d'« article » reclassés). Le taux de création d'arêtes peut changer pour des raisons de base,
   pas de science. Contrôle proposé : **pont** — reconstruire avec la moisson actuelle les arêtes 2020–2022 et comparer
   **les comptes** (arêtes, articles) à leur graphe publié, avec une tolérance déclarée d'avance.
2. **Citations révisées** : `counts_by_year` actuel ≠ celui de leur instantané de 2023 ; les étiquettes 2023–2025
   viennent forcément de l'actuel. À rapporter, pas à corriger.
3. **Fenêtre 2026 incomplète** : aucune étiquette à trois ans au-delà de fin 2025.
4. **Recherche de sous-chaîne sans limite de mot** : à reproduire telle quelle (fidélité), avec une variante
   « mot entier » seulement en analyse secondaire déclarée.
5. **Normalisation dépendante de l'échantillon** : `rescaling_col` divise par le maximum de l'ensemble évalué ;
   l'échantillon apparié aurait d'autres maxima. Figer : maxima calculés sur le graphe entier de l'année *y*
   (`get_norm_features`), identiques pour tous les ensembles.
6. **Variance d'une course à l'autre** : non publiée ; le critère « aire retrouvée » doit porter une tolérance fixée
   d'avance et un nombre de graines.

---

## 5. Couverture du vocabulaire du contrôle des intelligences artificielles

Simple recherche de chaînes dans `full_domain_concepts.txt` (37 960 concepts, `1544c30a5470af06…`), script
`scripts-v1/couverture_vocabulaire_v1.py` (`0113767ffc20cf2d…`), sortie complète
`couverture-vocabulaire-controle-v1.tsv` (`0f8dc65752ded4ac…`). Ce ne sont pas des mesures de résultat.

- **Absents (0 concept, ni exact ni comme mot)** : sabotage, e-value (« e value », « evalue »), safety, AI safety,
  misalignment, deception, honesty, interpretability, mechanistic, sparse autoencoder, residual stream, reward hacking,
  reward model, red team, jailbreak, backdoor, steganography, sandbagging, scheming, situational awareness, chain of
  thought, language model, large language model, attention, multi agent, out of distribution, sequential test,
  hypothesis test, betting, watermark, oversight, audit, evaluation awareness, sycophancy, hallucination, linear probe.
- **Présents comme concepts exacts** : neural network, machine learning, reinforcement learning, artificial
  intelligence, adversarial attack.
- **Présents seulement dans un autre sens (homonymes de physique)** : probe (20 : « weak probe beam », « x ray
  probe »…), monitoring (2 : « non invasive monitoring »…), steering (16 : « EPR steering », « beam steering »…),
  activation (12 : « activation energy »…), alignment (2 : « magnetic field alignment »…), control (65 : « quantum
  control »…), conformal (20 : « conformal field »…), martingale (2), calibration (4), agent (8 : dont « dishonest
  agent », « adversarial agent »), trojan (2 : « trojan horse attack »), collusion (1 : « collusion attack »).

**Conclusion** : la liste ne couvre pas le contrôle des intelligences artificielles ; les quelques mots communs
portent un sens de physique et créeraient de fausses arêtes. La liste générale de 368 825 concepts **n'est pas publiée**
(seule la liste du domaine l'est). **Extension proposée** : relancer leur chaîne (`create_concepts/` : RAKE, seuils 9 et
6, filtres) sur un corpus arXiv `cs.LG`, `cs.AI`, `cs.CL`, `cs.CR`, `stat.ML` — ce qui construit un **autre graphe** et
demande un **autre entraînement** : on testerait alors leur *méthode*, pas leur *modèle*. Le test hors échantillon de
leur modèle doit donc rester dans leur domaine (optique et quantique) ; le transfert au contrôle des intelligences
artificielles est une seconde expérience, à préenregistrer à part.

---

## 6. Ce que cela implique pour le critère de mort (message n° 261, point 3)

- « Aire publiée non retrouvée » doit nommer **quelle** aire (banc, fig. 6 p. 7 ; ou principale, fig. 11 p. 12), la
  tolérance et le nombre de graines. Proposition à discuter avec conv-audit : voie (R-a) d'abord (peu chère), voie
  (R-b) seulement si (R-a) passe.
- « Échec hors échantillon » doit nommer la métrique (aire sur l'échantillon apparié), le seuil et les bases à battre
  (attachement préférentiel, Simpson seule), fixés avant la moisson 2023–2025.

---

## 7. Inconnues

- **I-1** Volume d'OpenAlex 2023–2025 (articles de revue avec résumé) : nombre de pages, crédits, jours d'allocation
  gratuite, octets. Une requête de comptage (`group_by`) répondrait ; non lancée (interface à crédits).
- **I-2** Champ de type à filtrer dans OpenAlex actuel (`type:article` ou `type_crossref:journal-article`) et
  équivalence avec leur `journal-article` de 2023.
- **I-3** Ampleur de la dérive de résumés et d'arêtes entre leur instantané (2023) et Walden (2025–2026).
- **I-4** Écart entre leurs `counts_by_year` et ceux d'aujourd'hui pour les mêmes articles.
- **I-5** Étape de « nettoyage » qui produit les fichiers `_clean` d'entraînement : absente du code publié.
- **I-6** Temps réel d'entraînement sur processeur et nombre d'itérations avant l'arrêt précoce.
- **I-7** Mémoire de pointe pour régénérer les 689 millions de paires non reliées (machine à dimensionner).
- **I-8** Extraction d'un seul membre d'une archive du banc par requêtes partielles (probable, non essayée).
- **I-9** Variance d'une graine à l'autre de leurs aires (une seule course publiée, graine 42).
- **I-10** Valeurs de la fig. 4(a) pour les IR autres que 10, 50, 100 : courbe seulement, non tabulées.
- **I-11** Différences éventuelles entre l'arXiv v4 (notre PDF) et la version publiée dans *MLST* (non versée).
- **I-12** Coût et type de machine louée (mémoire ≥ 64 Go ? disque ≥ 100 Go ?) : devis à écrire.
- **I-13** Seuils du critère de mort (tolérance de reproduction, seuil hors échantillon, bases) : à fixer par
  préenregistrement contre-lu (R1, R2).

---

## 8. Fichiers de cette note

Tous sous `docs/notes/gu-krenn-v1/`, chacun avec son `.sha256` :
`sources-amont-v1/Impact4Cast/` (code cloné, lu, non exécuté) ; `sources-amont-v1/Impact4Cast-git-d2af4f3-v1.tar` ;
`…-ls-files-…`, `…-journal-…` ; `sources-amont-v1/zenodo-metadonnees-v1/` (deux fiches JSON, six listes TSV) ;
`sources-amont-v1/openalex-instantane-metadonnees-v1/` (LISEZMOI, notes de version, deux manifestes du 14 octobre
2026) ; `scripts-v1/` (deux scripts écrits ici) ; `couverture-vocabulaire-controle-v1.tsv` ; cette note.
Rien n'est commité (consigne de la demande).


### Pièce 4a — lecture des essais de la mémoire du pôle (`lecture-essais-memoire-v1.md`, `0cd614b16fc3…`, entier)

# Essais de la mémoire, pistes 1 et 2 — lecture (exploratoire, non opposable, lue dans les deux sens)

Lignée conv-audit (instance nouvelle), 27 octobre 2026, écrit à partir de 08:38 UTC (heure lue sur `date -u`). Plan
`plan-essais-memoire-v1.md` (`ac0354ad…`, poussé avant tout lancement, commit `8edfaf7`) ; script `essais_memoire_v1.py`
(commit `c949781`) ; résultats `resultats-v1/conforme/` (conforme au plan, graine 20261028, 2 min 5 s) et
`resultats-v1/variante-B/` (variante déclarée, voir piste 2). Deux essais de fumée avant (2 courses chacun, non retenus).

## Verdict

1. **Une signature prédictive bat de loin le texte** pour reconnaître une redite ; mais **la signature brute** (la piste
   de l'instance sortante) fait aussi bien que ma signature invariante, et mieux sur le mélange aveugle : mon idée
   d'invariance n'apporte rien ici. Je la retire au profit de la signature brute.
2. **Hériter de la preuve vaut mieux que refuser** : mêmes fausses découvertes (0,05 par course), plus de vraies
   (+ 0,06 au plan, + 0,50 quand la première tentative est trop sûre d'elle) ; ne rien faire augmente les fausses
   découvertes de 70 %.

## Piste 1 — redites manquées par famille, à 5 % de fausses fusions (moitié de mesure, 200 paires par famille)

| famille | texte (Jaccard) | signature brute | signature invariante |
|---|---|---|---|
| paraphrase, copie renommée, jargon rare, changement d'échelle | 1,000 chacune | 0,000 chacune | 0,000 chacune |
| biais par issue | 1,000 | 0,025 (5) | 0,000 (0) |
| mélange avec une loi aveugle | 1,000 | **0,035 (7)** | 0,125 (25) |
| fausses fusions réalisées (vraies différences) | 0,000 | 0,060 | 0,050 |
| variante quantitative fusionnée (logits × 2) | 0,000 | 1,000 | 1,000 |

- Le texte simulé est grossier (il ne dit que le sens des effets) : deux lois différentes ont souvent le même texte, si
  bien qu'à 5 % de fausses fusions son seuil monte à 1 et il ne fusionne plus rien. Ce chiffre dit qu'un texte peut être
  identique pour deux hypothèses différentes ; son ampleur est un artefact du générateur.
- Prédictions : tenues pour le texte (il manque tout) et pour la variante quantitative (fusionnée par les deux
  signatures) ; **non tenues** pour la signature brute (je prédisais qu'elle manquerait le mélange et le biais : elle
  n'en manque que 3,5 % et 2,5 %) ; la signature invariante tient sa prédiction (mélange ≤ 0,3) mais elle est **moins
  bonne** que la brute sur le mélange (intervalles de Wilson disjoints) et pas significativement meilleure sur le biais.
  Le critère « ce qui contredirait le brainstorm » du plan est rempli.

## Piste 2 — politiques face aux retentatives (200 courses de 40 hypothèses, environ 4 vraies par course)

| première tentative d'une vraie | politique | fausses par course | vraies par course | tests par course |
|---|---|---|---|---|
| trop faible (× 0,3, plan) | rien | 0,085 | 4,040 | 93,5 |
| | refus | 0,050 | 3,985 | 40,0 |
| | héritage | 0,050 | 4,040 | 93,5 |
| trop sûre d'elle (× 3, variante B) | rien | 0,085 | 3,975 | 94,1 |
| | refus | 0,050 | 3,310 | 40,0 |
| | héritage | 0,050 | 3,810 | 94,3 |

- Rien − refus, fausses : + 0,035 [+ 0,010 ; + 0,060] (les deux variantes) : réessayer jusqu'à la chance gonfle les
  fausses découvertes ; l'essai a des dents (R5).
- Héritage − refus, fausses : 0,000 [0 ; 0] ; vraies : + 0,055 [+ 0,025 ; + 0,090] au plan, + 0,500 [+ 0,400 ; + 0,605]
  en variante B. Prédictions tenues.
- Coût de l'héritage : quand la première tentative est très fausse sur l'effet (trop sûre d'elle), sa classe part de
  très bas ; « rien » retrouve 0,165 vraie de plus par course (+ 0,115 à + 0,220), au prix de fausses découvertes en plus.
- **Variante B, déclarée** : ajoutée après l'essai de fumée, qui montrait qu'à × 0,3 presque toutes les vraies passent dès
  la première tentative (la piste n'aurait pas eu de dents sur les vraies) ; seule l'option de la première tentative change.

## Ce que cela change pour la mémoire

- Identité d'une entrée : la **signature brute** sur une sonde fixe tenue hors de la vue des agents ; seuil réglé sur des
  paires de vraies différences ; la variante quantitative est fusionnée — c'est l'héritage qui lui laisse sa chance.
- Politique : **héritage de la preuve**, pas de refus. Reste à écrire : la classe d'une fille (avec ses parents), et la
  piste 3 (un proposeur qui lit la mémoire, contre mémoire placebo).
- Limites : lois softmax synthétiques, deux traits, textes simulés ; aucune mesure d'effet sur de vrais agents.


### Pièce 4b — lecture des essais de la mémoire, piste 3 (`lecture-essais-memoire-piste3-v1.md`, `27e4cdaca14f…`, entier)

# Essais de la mémoire, piste 3 — un proposeur qui lit la mémoire — lecture v1 (exploratoire, non opposable, lue dans les deux sens)

Lignée conv-audit (instance du 27 octobre 2026), écrit à partir de 11:26 UTC (heure lue sur `date -u`). Sans
préenregistrement (mot de Lazar, 12:02 heure de Paris) ; plan, lecture et prédictions dans l'en-tête du script
`essais_memoire_piste3_v1.py` (`c8353a5e…`), poussé avant le lancement (commit `b720bdc`). Graine
176238914913698272559241769767042812787 (`numpy.random.SeedSequence().entropy`) ; 60 courses par type de monde ;
exécution de 11:11:56 à 11:25:30 UTC ; résultats `resultats-piste3-v1/` (manifeste poussé avant le calcul, commit
`30c2b37`). Un essai de fumée avant (2 courses, graine 1, non retenu).

## Verdict

1. **Lire la mémoire double les découvertes quand le monde a une structure** : pour le même budget (200 tests), la
   mémoire complète trouve 24,0 vraies associations par course, contre 12,8 avec la mémoire placebo et 11,8 sans
   mémoire (+ 11,2 sur le placebo, intervalle [+ 9,8 ; + 12,5]). Ce qui aide, c'est le **contenu** de la mémoire : la
   même politique nourrie de la mémoire d'une autre course ne fait pas mieux que le hasard (+ 1,0 ; [− 0,2 ; + 2,2]).
2. **L'essai a des dents** : quand la même vérité est dispersée sans structure (monde permuté), l'avantage des
   marchepieds disparaît (+ 0,7 sur « redites seulement », [− 0,3 ; + 1,6]). Seul reste le gain d'éviter les redites
   (+ 2,9 sur « sans mémoire », [+ 2,1 ; + 3,7]) : sans mémoire, 40 tests sur 200 partent en redites.
3. **Le prix** : la lecture structurée concentre les découvertes. Dans le monde permuté, elle couvre moins de régions
   que « redites seulement » (8,6 blocs contre 9,9 ; − 1,3, [− 1,9 ; − 0,7]) ; il faut garder une part d'exploration.
   Les fausses découvertes restent rares pour tous (au plus 0,22 par course) : le registre avec héritage les tient.

## Chiffres (moyennes par course ; 36,5 vraies associations par monde sur 400)

| monde | proposeur | vraies | part trouvée | fausses | redites | blocs | puissance du 1er essai |
|---|---|---|---|---|---|---|---|
| groupé | sans mémoire | 11,8 | 0,32 | 0,07 | 39,8 | 6,7 | 0,80 |
| groupé | mémoire, redites seulement | 14,4 | 0,39 | 0,17 | 0,5 | 7,6 | 0,78 |
| groupé | **mémoire complète** | **24,0** | **0,66** | 0,08 | 0,7 | 7,5 | 0,88 |
| groupé | mémoire placebo | 12,8 | 0,35 | 0,10 | 35,8 | 6,9 | 0,79 |
| permuté | sans mémoire | 11,5 | 0,32 | 0,18 | 39,3 | 8,1 | 0,79 |
| permuté | mémoire, redites seulement | 14,4 | 0,39 | 0,22 | 0,6 | 9,9 | 0,79 |
| permuté | mémoire complète | 15,1 | 0,41 | 0,17 | 0,3 | 8,6 | 0,80 |
| permuté | mémoire placebo | 12,2 | 0,33 | 0,13 | 36,3 | 8,7 | 0,81 |

Différences appariées par course (vraies ; intervalle à 95 % par rééchantillonnage des courses) :

| différence | groupé | permuté |
|---|---|---|
| complète − placebo | + 11,2 [+ 9,8 ; + 12,5] | + 2,9 [+ 1,9 ; + 3,9] |
| complète − redites seulement | + 9,6 [+ 8,7 ; + 10,6] | + 0,7 [− 0,3 ; + 1,6] |
| redites seulement − sans mémoire | + 2,5 [+ 1,7 ; + 3,4] | + 2,9 [+ 2,1 ; + 3,7] |
| placebo − sans mémoire | + 1,0 [− 0,2 ; + 2,2] | + 0,7 [− 0,2 ; + 1,6] |

## Lecture et prédictions (fixées avant le lancement)

- Critères 1 (contenu), 2a (structure, monde groupé), 2b (disparition en monde permuté), 3 (placebo sans apport, deux
  mondes) : remplis ; 5 (trop beau, plus de 95 % trouvées) : non (0,66).
- Prédictions : toutes tenues (complète − placebo ≥ + 5 : + 11,2 ; complète − redites seulement ≥ + 3 : + 9,6 ; permuté,
  écart ≤ 1,5 en valeur absolue : 0,7 ; placebo − sans mémoire dans ± 1,5 : + 1,0 et + 0,7).
- **Pourquoi la mémoire complète gagne en monde groupé**, en deux parts : elle teste les voisines des promues (60 % de
  vraies près d'un foyer, contre 2 % ailleurs) et elle y suppose la force estimée de la promue (forces voisines dans un
  foyer) : sa puissance au premier essai monte à 0,88 contre 0,78. En monde permuté, les deux parts disparaissent
  (0,80) : c'est cohérent.
- **Audit de propreté (R4)** : toutes les prédictions tenues, mais elles suivaient l'essai de fumée (déclaré) ; rien de
  « trop beau » au sens du critère 5. La part de la puissance du premier essai est un mécanisme voulu, pas une fuite :
  la force estimée vient des tirages du test de la promue, jamais du monde.

## Ce que cela dit, et ce que cela ne dit pas

- **Dit** : avec un proposeur qui sait lire, la mémoire améliore les propositions **si et seulement si** les vraies
  associations se regroupent dans l'espace où le proposeur mesure la proximité. Éviter les redites rapporte toujours
  (+ 2,5 à + 2,9 vraies, 20 % du budget récupéré).
- **Ne dit pas** : que la vérité se regroupe dans le monde réel. C'est la condition à vérifier sur données réelles. La
  rétrodiction sur arXiv (2003-2016, `../retrodiction-swanson/`) permet de mesurer si les associations qui ont réussi
  se regroupent dans un espace de concepts : à faire avant de bâtir sur ce résultat.
- **Limites** : proposeur scripté (de vrais agents lisent mal, ou trop) ; voisinage connu exactement (dans la réalité,
  la proximité du proposeur est bruitée : l'essai suivant doit ajouter une part de « fausses voisines ») ; quatre foyers
  seulement ; 200 tests par course.
- **Pour la mémoire du pôle** : signature brute + héritage de la preuve (pistes 1 et 2) + archive lue par marchepieds
  autour des survivantes, avec une part d'exploration réservée (contre la concentration, point 3 du verdict).

