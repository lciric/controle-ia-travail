# Brancher et concevoir les expérimentateurs et les tests de mort de l'organisme d'idéation — note de conception — v1

- **Pièce de travail (classe C), non contre-lue.** Concepteur : Claude Fable 5.2 (règle « Qui conçoit », R-3735 ; mandat de la mère, R-4372). Écrite le 21 novembre 2026, de 06:42Z à 07:39Z (`date -u`). Processeur seul : aucun appel payant, aucune machine louée, ni commit ni poussée. Elle propose ; les pièces décisives qu'elle appelle (additifs, critères, préenregistrements, devis) suivront la chaîne complète. **Lecture courte : § 0, puis § 6.**
- **Question de Lazar**, verbatim : « demande a fable effort max comment brancher et concevoir les experimentateurs et les tests de mort ». **Priorité dite pendant l'écriture** (vers 07:03Z, ligne GO-2026-11-21-16), verbatim : « je veux surtout les experimentateurs et les tetss de mort sur la course principale d'autoconception et d'laboration de nouvelles mathematiques pour l'attaque et la defense ». L'ordre des emplois (§ 4) la suit.
- **Question reçue du plan de l'organisme pour la course principale** (branche `lot/compte-organisme-v1`, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v1/plan-experimentateur-tests-de-mort-course-principale-v1.md`, `0bb27bc0a1f262daa41ad1f7746c34a2d423a90354e834d6f6874eee1f80d8e7` ; rapport `eaf8120adc10cda144f84bf85fc1a658834d73a11eacf0cf6fe97b2c08c50461`), § 2.1 et décision D2 : qu'est-ce qu'un test de mort éprouve sur une carte d'auto-conception ? **La réponse est au § 2.2.**
- **Bases lues** : arbre de travail, qui a avancé pendant l'écriture (commit `ab5b025d8` au dernier relevé) ; branche de l'organisme au commit `7c61066cf` ; harnais de l'arbitre formel, branche `prep/lean-outillage-d1a-v10`, commit `ae894d8d`. Le dépôt de l'orchestrateur n'est pas sur cette machine : son code est lu dans la copie empreintée versée sur `main`.
- **Marques** : [vérifié] = lu par moi sur le fichier, empreinte recalculée ; [rapporté] = dit par la pièce citée, non revérifié ; [proposition] = de moi, à geler ou à changer au texte scellé. **Calculs** : `calculs-conception-tests-de-mort-v1.py` (`301c0f52fc11c7a7bc9de2292b51f56b314277fda72402fc7c76b33323fdb857`) et sa sortie (`9b66cc78d0e3328fa8eaa731933fa38cd2ec6d58efde59361b6d9dabc3cc54a7`), même dossier : lois exactes, aucun tirage, rejoués deux fois à l'octet, non contre-lus. Une lettre entre crochets renvoie à un bloc de cette sortie.
- **Côté attaque : niveau de la méthode seulement.** Cette note n'écrit aucun mode, aucune lecture retournée d'un énoncé, aucun procédé.

## 0. Verdict

1. **Non, ce n'est pas branché en général.** Des tests de mort réels ont tourné une fois : 14 tests, à la course réelle v67, sur des lois promues par le juge, à forme imposée. Le régime général n'existe que sur le papier, pour le seul palier 1 de l'héritage (additif scellé, aucun code). À la course d'auto-conception, l'épreuve d'une carte s'écrit à la main, ligne par ligne. Au pilier mathématique, le harnais de l'arbitre formel est écrit et n'a jamais été relevé conforme sur machine.
2. **Conception.** Personne dans l'organisme n'écrit le critère de mort. L'expérimentateur *implémente* la proposition sous une interface scellée ; le noyau *mesure* contre une vérité plantée qu'aucun agent ne voit ; toute épreuve passe d'abord ses témoins plantés, et une épreuve qui laisse vivre un témoin faux est une épreuve morte ; un mort reste mort.
3. **Carte d'auto-conception** (question D2) : elle meurt ou tient par une **course appariée** de l'organisme, avec et sans son mécanisme, sur des mondes à lois plantées scellés d'avance. D'abord sur un banc à proposeurs écrits par programme, où la sévérité ne coûte que du processeur ; ensuite, pour les seules cartes qui tiennent, avec de vrais proposeurs, sur devis. **Carte mathématique** : un énoncé meurt par un contre-exemple exact ou tient par l'arbitre formel ; un mécanisme de preuve se juge sur un banc de preuves plantées.
4. **Branchement.** L'étage existant, sans un octet changé, sert à écrire et sceller l'implémentation, non à rendre le verdict ; un sommet d'étage écrit une fois ; la vérité plantée ne monte jamais sur la machine jetable. Premier pas à 0 USD dans les trois emplois : le banc d'étalonnage. Sept décisions pour toi (§ 6) : l'une rouvre une décision prise (les champs de fiche), une autre touche la lecture d'une règle gelée.

## 1. État des lieux vérifié

Code de l'orchestrateur : commit `a41b7b50` de son dépôt [rapporté] ; copie sur `main` au commit `94bfd92`, `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/`, dont les seize fichiers employés au palier 0a ont les mêmes empreintes [vérifié].

| pièce | où, empreinte | ce qu'elle fait | où elle s'arrête |
|---|---|---|---|
| étage des tests de mort, version 5 | `pole/tests_de_mort_v5.py` `da524871…`, sur la v4 `35912a3a…` et la v2 `363a3725…` [vérifié, lu en entier] | préenregistrement court scellé avant toute session (l. 450) ; l'expérimentateur, session de modèle sans outil, fait exécuter un script ; verdict calculé par le noyau sur le fichier brut scellé (l. 616-622) ; douze fiches au plus | en-tête, l. 42-43 : « un script qui fabrique ses lignes n'est pas détecté ici » ; en forme libre le proposeur écrit son propre seuil |
| bac à sable, exécuteur factice | `pole/tests_de_mort_v2.py`, l. 1250 et 2100 [vérifié] | `bwrap` : réseau isolé, identité dédiée, lecture seule, bornes, sonde avant usage | le factice n'est pas une barrière : refusé avec le moteur réel (v5, l. 279) |
| tour fermé | `pole/tour_ferme_v64.py` `35a8294e…` [vérifié, lu par parties] | forme imposée (l. 460) ; sept témoins par génération (l. 125, 492) ; recalcul hors du bac qui arrête la course (l. 806, 893) | n'éprouve que ce que le juge a promu, témoins compris (l. 974-982) |
| oracle existant | `pole/oracle_tour_ferme_v60.py` `514864b7…` [vérifié] | mesure après coup | n'étiquette « loi plantée retrouvée » qu'une loi promue par le juge (l. 137-141) |
| code v6 du palier 0b (commit `8262c442`) | `comparateur.py` `8758b015…`, `enveloppe.py` `2173613a…`, `executeur.py` `063df6e1…`, `organisme.py` `fb2f7b48…` [vérifié] | comparateur sans juge ; lots de douze dans l'ordre du scellement ; artefacts « script qui fabrique », « sens inversé », « tient à toute loi » | lancé ce matin (GO-2026-11-21-09) ; aucune sortie lue par moi |
| orchestrateur v68 | huit fichiers, `course2_v68.py` `c1aeab4c…` ; contre-lecture « conforme » `d2cfeac1…` ; sur `main` (commit `61987a3a9`) avec les lanceurs de course 9 `1b47c1cf…` et 10 `f4196ec5…` [vérifié : empreintes] | régime « tests de mort sans rien servir » ; plafond de course | moteur réel refusé par construction |
| orchestrateur v69, cadre de la v70 | `prereg/organisme-auto-conception-v9/orchestrateur-v69/`, additif `cb352811…`, cadre `b1822613…` [vérifié] | véhicule du palier 1 : sommet d'étage neuf, neuf conditions d'allumage, vingt gardes | **aucun code** ; lanceur de course 11 non écrit ; ni préenregistrement court, ni devis, ni ligne de calcul |
| course d'auto-conception v9 | texte scellé `0d51e0b3…`, configuration `3f662ee8…` (branche de l'organisme) ; ordre de passage des épreuves v3 `b19f550b…` ; banc à lois plantées de la ligne 1, `banc_ligne1_v1.py` `ccc97ea2…` [vérifié : empreintes, en-têtes] | une génération, « pas de tests de mort » ; dix champs par carte, dont `module_change`, `epreuve_monde_plante`, `ce_qui_la_refuterait` ; 22 rangs d'épreuve | chaque épreuve est écrite à la main ; quatorze rangs sur vingt-deux attendent le branchement pour leur étage réel (ordre v3, § 1.3) |
| arbitre formel | branche `prep/lean-outillage-d1a-v10` : `verificateur_noyau_v6.lean` `3ef23bfa…` (énoncé imprimé, axiomes, rejeu par le noyau), `gardes_lean_v4.py` `eb747831…`, `executeur_bac_v6.py` `d8694804…`, artefacts de tricheurs [vérifié : fichiers, empreintes] | hors machine : 39 cas conformes sur 39, 176 mutations tuées sur 176 [rapporté : `docs/notes/etat-chantier-lean-2026-11-21-v1.md`, `3d2b8d3e…`] | deux essais sur machine isolée, étape du noyau non conforme (0 sur 18) ; troisième essai : aucun rapport retrouvé (même note, l. 57) ; aucune banque, aucune cible scellée |

- **Seule exécution réelle** (verdict `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md`, `d7902432…`, § 4.4 ; `registres/depenses.md`, l. 428-430) : 14 tests, vrai bac sur machine louée (3 h 18 min, ≈ 0,27 USD), 28 appels d'expérimentateur (un script, puis « fin »), au plus 0,081 USD par test pour l'expérimentateur et 0,061 pour le lecteur (totaux des deux relais divisés par 14, appels de proposeur compris) ; recalcul hors du bac égal à l'octet, 14 sur 14.
- **Le palier 0a** (rapport `93d8a104…`) [rapporté]. *Prouvé* : l'étage, sans un octet changé, exécute des engagements sur une loi vraie plantée, trois fausses et l'anti-loi, à l'identique en factice et dans le vrai bac local ; la vraie tient, les fausses meurent ; le comparateur apparie par calcul seul. *Non prouvé* : un coût ; la conduite d'un expérimentateur modèle ; une forme libre ; plus de douze tentatives ; la machine louée. *Montré contre l'étage* : une anti-loi dont le script écrit un gain constant « survit » au noyau ; seul le recalcul du tour fermé l'arrête, et il n'existe que pour la forme imposée.
- **L'expérimentateur aujourd'hui** : un rôle de l'étage, qui écrit le script d'un engagement scellé ; à la forme imposée il n'a rien à décider. Lazar le garde comme modèle (GO-2026-11-19-75) ; il reçoit l'engagement seul aux étages payants (GO-2026-11-19-81). Le modèle qui le jouait à la v67, servi par le relais Kimi, est absent des courses récentes (`registres/etat.md`, « sans Kimi ») ; aucun n'est nommé à sa place. Le proposeur qui expérimente avant de proposer (note `7df9afc4…` ; synthèse du collisionneur `f3d7eea7…`) n'a pas reçu de décision que j'aie retrouvée.
- **Collision de numéros** : 68 à 71 et 74 nomment aussi le code d'une autre lignée du même orchestrateur (`docs/notes/organisme-multi-generations-v1/pilote-v1/`, noms de fichiers lus ; plan de l'organisme, D3). Tout nom neuf est à vérifier libre (règle R12).

## 2. Conception

### 2.1 Quatre règles, une définition

1. **Le critère de mort n'appartient à aucun agent.** Le concepteur l'écrit ; il est scellé avant la course, le même pour toutes les propositions d'une sorte.
2. **La proposition décide, le noyau mesure.** Le code d'un agent rend une décision (un seuil, une promotion, un prédicat), jamais une mesure ; le noyau la confronte à une vérité plantée. Le défaut montré au palier 0a disparaît par construction : un script ne fabrique pas une mesure qu'il ne fait pas.
3. **L'épreuve est elle-même éprouvée**, par des témoins plantés, avant toute proposition réelle.
4. **Les issues sont écrites par programme, et un mort reste mort.**

**Un test de mort** est un quadruplet scellé : une famille de mondes plantés à vérité calculable ; une interface, qui dit ce que la proposition reçoit et ce qu'elle rend ; une statistique que le noyau calcule contre la vérité ; un critère écrit d'avance, avec son niveau d'erreur.

### 2.2 Quatre formes d'épreuve, et la réponse à la question D2

| forme | proposition | ce que l'expérimentateur écrit | ce que le noyau mesure | état |
|---|---|---|---|---|
| **sur données** | une loi prédictive dans la grammaire fermée | un script fixe : rien à décider | le gain de log-score sur la tranche d'épreuve, recalculé hors du bac | existe (tour fermé, v67, palier 0a) |
| **par décision** | une règle : seuil d'alerte, promotion, sélection, mémoire | une fonction « ce qui est servi → décisions » | la vérité de chaque décision : taux vrai de fausses alertes et puissance ; lois vraies et fausses plantées promues, à budget apparié | à écrire ; petite |
| **par arbitre** | un énoncé : conjecture, borne, impossibilité | un prédicat exécutable ; un fichier de preuve de l'énoncé et de sa négation | une violation exacte sur de petits mondes ; l'acceptation par le noyau du vérificateur de preuves | harnais écrit, jamais conforme sur machine |
| **par course réelle** | un mécanisme dont l'effet dépend de la conduite des modèles | le greffon, branché dans l'organisme réel | l'organisme joué avec et sans, vrais proposeurs, mondes plantés | attend l'orchestrateur v69, puis la lecture entre générations |

**Ce qu'un test de mort éprouve sur une carte d'auto-conception.** Une telle carte n'énonce pas une loi sur des données : elle affirme que l'organisme fait mieux avec son mécanisme. « Mieux » a une définition scellée (`docs/notes/organisme-auto-conception-v1/course-v2/definition-amelioration-considerable-v9-v1.md`, `4eae96bc…`) : plus de lois vraies plantées promues, ou moins de lois fausses, face à un bras témoin sans le mécanisme, à budget apparié, selon trois cas (validité, rendement, cumul). **Son test de mort est donc une course appariée de l'organisme, avec et sans le mécanisme, sur des mondes à lois plantées scellés d'avance ; la carte meurt si l'engagement tiré de cette définition n'est pas tenu.** Des trois lectures du plan (§ 2.1), c'est la troisième, rendue jouable par deux barreaux, le bon marché d'abord (N-045).

- *Barreau 1, la course de banc* [proposition]. L'organisme y est un banc écrit par nous : lignées de proposeurs écrites par programme, fonctions de jugement de l'orchestrateur, mondes à lois vraies et fausses plantées. Base : le banc de la ligne 1, qui journalise déjà les entrées exactes de chaque décision et nomme ses mécanismes (`mecanismes_code`, l. 563). Le mécanisme de la carte y entre comme un **greffon** : une fonction appelée une fois par génération, dans le bac, qui ne reçoit que ce que recevait le mécanisme remplacé, jamais la vérité. Bras, sur les mêmes graines (`numpy.random.SeedSequence`, dérivées par monde et par course) : sans ; avec ; placebo de même forme ; bases bon marché du point de greffe, en liste fermée. Le noyau compte les lois vraies et fausses promues et le coût. La carte meurt « invalide » si elle fait promouvoir plus de lois fausses que le niveau annoncé ; « sans gain » si son écart apparié au témoin, au placebo et à la base ne passe pas le seuil de son cas, sur des familles de mondes tenues à l'écart (unité : le monde ; test exact des rangs signés, plan de l'héritage `9085bbe9…`, § 3.3). Sinon elle « tient au banc » : ce n'est pas une adoption.
- *Barreau 2, la course réelle appariée*. Pour les cartes qui tiennent au banc, et pour celles dont l'effet dépend de ce que des modèles font de ce qu'on leur sert, que nul banc ne peut tuer : l'organisme réel avec et sans le greffon, mêmes mondes, mêmes graines, tests de mort réels dans la boucle. Sur devis.
- *Cas fréquent.* Sur les 94 cartes, 42 nomment les tests de mort et 34 les témoins plantés dans `module_change` (lecture descriptive `0306adf7…`, l. 99 ; une mention n'est pas un changement ; je n'ai ouvert aucune carte). Pour une carte qui change l'épreuve elle-même, la course est le banc d'étalonnage du § 2.3 : l'épreuve modifiée doit laisser vivre moins de témoins faux sans tuer plus de vrais, à coût égal.
- *Témoins du banc de course* [proposition] : un mécanisme utile par théorème face à un témoin dégradé exprès doit tenir ; un neutre (mêmes décisions, autre code) doit mourir « sans gain » ; un surajusté aux mondes décrits doit mourir sur les familles tenues à l'écart ; un nuisible (tout promouvoir) doit mourir « invalide ». L'ordre de passage v3 portait cet instrument comme un rang parmi vingt-deux (rang 14, « porte de version à témoins plantés » ; voisins : le rang 10, « jumeau permuté aux tests de mort », et le rang 21, « porte transactionnelle des auto-modifications ») : je propose d'en faire la porte commune ; leurs rédacteurs reçoivent cette note.

**L'étage ne refuse plus les fiches.** Le manque n'est pas une tranche de données de la course, c'est l'objet servi à l'étage. L'orchestrateur écrit lui-même la fiche de l'étage, comme le tour fermé le fait pour une loi (`carte_servie`, l. 484) : texte de test imposé (« écris le greffon conforme à l'interface ; fais-lui passer l'auto-essai ») ; tranche faite de l'interface et d'un petit journal factice du banc, les mêmes pour toutes les cartes ; bloc de statistique réduit à la complétude du fichier d'auto-essai (statistique « nombre », déjà dans la liste de l'étage). L'étage v5 sert alors, sans un octet changé, à écrire, exécuter et sceller le greffon (à confirmer sur le code ; champs exigés d'une fiche : rapport du palier 0a, § 3.1). Le verdict vient après : le noyau rejoue le greffon scellé, sans appel de modèle, sur tous les mondes et tous les bras.

**Ce que cela change aux champs de fiche** (GO-2026-11-20-05, point 3a : « inchangés »). *Pour les 94 cartes de la v9 : rien.* Un pont les met en forme fixe sans rien inventer : point de greffe (liste fermée) ; cas de la définition ; quantité, signe et taille de l'effet tels que la carte les dit, sinon « lu au plus prudent » (définition, § 3, condition 1). Chaque valeur porte l'extrait qui la fonde, vérifié à l'octet par programme, par deux traducteurs de deux lignées, comme la conception v2 de la course « seuil et moniteurs » le fait pour des textes libres (`…/ideation-seuil-moniteurs-v1/conception-v2/ordre-course-seuil-et-moniteurs-v2.md`, `1fbd04c3…`, § 3 et § 4). Une carte qui ne se met pas en forme est « hors gabarit » : comptée, ni morte ni tenue, elle reste à sa ligne d'épreuve. *Pour les courses suivantes : trois champs fermés de plus* — `point_de_greffe`, `engagement` (cas, quantité, signe, taille), `greffon` (texte borné, facultatif) — à côté des dix gardés. Cela rouvre 3a et demande un texte neuf de la course (D7 du plan). L'objection « un proposeur écrit le test que sa carte passe » (plan, D2, option (a)) tombe : il choisit un cas et une taille, jamais l'épreuve, et les seuils de la définition scellée font plancher.

**Ce que cela change au coût de l'expérimentateur, que rien ne mesure.**
1. Il se paie **une fois par carte** : le greffon scellé se rejoue sur autant de mondes, de graines et de bras qu'on veut, sans appel. La sévérité ne coûte que du processeur.
2. Les bornes du plan — de 0,06 à 0,90 USD par tentative, soit de 16,92 à 253,80 USD pour 282 tentatives (§ 5.3) — sont celles de l'étage pour un script de loi. Un greffon pèse plus. Entre le relevé de la v67 (0,08 USD, deux tours) et, ordre de grandeur sous hypothèse, le plafond de 4 USD par item que le brouillon de l'essai de l'arbitre formel donne à une formalisation (`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md`, `717259ed…`, non mesuré), il y a un facteur cinquante.
3. Donc mesurer d'abord sur les seuls mécanismes témoins — dépense bornée par leur nombre fois le plafond — avant tout devis pour 282 tentatives.
4. Le barreau 2 a un autre prix : cinq paires au moins pour un test exact unilatéral à 5 % (plan de l'héritage, § 3.3), soit dix générations de bras par carte, de l'ordre de 590 USD de propositions à cinq espèces et de 90 à deux (58,64 et 8,92 USD la génération d'un bras, devis de l'héritage v5, `30c87fa6…`, § 2).

**Carte « mathématiques nouvelles ».** *Un énoncé* meurt ou tient par arbitre. D'abord la recherche de contre-exemples sur de petits mondes plantés à vérité calculée exactement : l'expérimentateur écrit l'énoncé comme prédicat exécutable, le noyau énumère les instances par graine et vérifie toute violation en arithmétique exacte. Ensuite le vérificateur de preuves, sur la machine isolée : accepté, réfuté ou ouvert, et « ouvert » ne vaut jamais « faux ». Un énoncé ne « tient » qu'accepté sous les gardes, non vide et fidèle (accord du prédicat et de l'énoncé formel sur les petites instances). *Un mécanisme de preuve* (stratégie de formalisation, garde de fidélité, contrôle de nouveauté) meurt ou tient comme tout mécanisme, par une course appariée, sur un **banc de preuves plantées** : erreurs de classes fixées plantées par un tiers et jumelles saines (brouillon de l'essai, § 1.1), cibles fausses à contre-exemple scellé, énoncés connus plantés ; il doit détecter plus d'erreurs plantées sans alerter plus sur les jumelles saines, à plafond de coût par item égal.

### 2.3 Issues, témoins, épreuve morte

- **Issues** (noms de l'additif `cb352811…`, § 4.2 ; le mot « survit » n'en est plus une, R-3209) : « tient » ; « ne tient pas », avec son motif écrit par programme (« invalide » ou « sans gain ») ; « non exécutable ou indéterminée », qui n'est pas une mort ; statuts « non éprouvée (budget) », « hors gabarit » et, neuf, « non éprouvée (épreuve morte) ».
- **Trois sortes de témoins**, mêlés aux propositions sous identifiant opaque : *doit mourir* (faux grossier, probabilité exacte de mort connue) ; *doit tenir* (vrai par théorème) ; *de marge* (faux de peu : il mesure l'angle mort, il ne décide de rien).
- **Épreuve admise, épreuve morte.** Le banc d'étalonnage joue toute la banque par des implémentations écrites par programme, à 0 USD, et scelle une table d'admission. Un témoin « doit mourir » qui tient : épreuve morte, aucune issue lue ; c'est un arrêt rapporté, jamais un repli. Dans un étage payant, chaque lot de douze porte en plus des témoins passés par l'expérimentateur : ils mesurent sa fidélité.
- **« Tient » n'est pas « vrai ».** L'angle mort de l'épreuve se calcule et s'écrit (§ 4.3). La survie se durcit sans appel : criblage, puis confirmation sur des lots neufs que l'implémentation scellée n'a jamais vus.
- **Un mort reste mort.** Registre des tentatives en ajout seul, chaîné, scellé (plan de l'héritage, § 1). Une mort est écrite par une fonction dont les seules entrées sont l'engagement scellé, les décisions scellées, la vérité et le journal des coûts. Seule une épreuve neuve sous règle scellée rouvre un dossier, jamais un juge. Essai : permuter toutes les sorties de juges laisse les issues identiques à l'octet (plan de l'héritage, § 3.1).

### 2.4 Les expérimentateurs

| rôle | ce qu'il lit | ce qu'il écrit | ce qu'il ne voit jamais | modèle, budget |
|---|---|---|---|---|
| **expérimentateur d'épreuve** (existe ; gardé) | l'engagement scellé seul, à forme imposée ; l'interface ; les données de mise au point ; ses propres tours | un script, un greffon, un prédicat ou un fichier de preuve, exécuté dans le bac ; jamais un verdict | la vérité, les graines, les lots de la mesure, la justification et la prédiction du proposeur, toute sortie de juge, toute issue | une autre lignée que le lecteur témoin (`tour_ferme_v64.py`, l. 692) ; plafond par tentative gelé au devis |
| **traducteurs** (mise en forme fixe) | une carte ou un texte, seul | la fiche à champs fermés, extrait cité | les autres fiches, toute issue | deux lignées, dont aucune n'est l'expérimentateur |
| **expérimentateur d'exploration** (un proposeur qui expérimente ; non décidé) | la part servie aux proposeurs, jamais la tranche d'épreuve | des cartes au même gabarit | la même liste | le protocole de session de l'étage est déjà cette boucle minimale (v5, l. 456-601) ; plus tard |

Un modèle n'éprouve jamais une proposition qu'il a écrite. Second temps possible, sur devis : un expérimentateur *propose* une épreuve ; elle ne devient test de mort qu'après avoir tué des témoins faux cachés et épargné des témoins vrais.

### 2.5 Articulation

```
question scellée ─► proposeurs ─► cartes à champs fermés ─► gardien de forme
        juges : pour information, jamais un choix ni un repêchage
  lot de douze = tentatives dans l'ordre du scellement + témoins (identifiants opaques)
        │  machine jetable, sans clé ni vérité : l'expérimentateur écrit, le bac exécute et scelle
        ▼
  chez la mère : le noyau rejoue l'implémentation scellée sur les lots de mesure,
  mesure contre la vérité, écrit les issues ─► registre ─► oracle et coût (N-058)
```

- **Proposeurs** : la question, les gabarits, la part servie. Rien de l'étage tant que rien n'est servi (GO-2026-11-20-05, 1a) ; ensuite le registre des tentatives et leur issue, toutes, sans tri (2b ; cadre de la v70).
- **Juges** : pour information. Toute tentative est éprouvée ; si le budget manque, tirage par graine, jamais un rang de juge.
- **Oracle et composition** (N-058) : par espèce, tentatives qui tiennent sur la famille tenue à l'écart, vérités plantées retrouvées par égalité de comportement, coût. Le volet des témoins jugés reste hors de la mesure, écart déclaré comme pour l'héritage (GO-2026-11-19-76, point 3).
- **Héritage récompensé** (rapport du plan, § 3, point 5) : ce qui est rendu à l'organisme est l'issue par tentative et son coût, rien de plus fin, sur des mondes neufs par génération (N-049), la mesure finale lue une fois (N-050). Ce qu'une génération lègue se mesure par l'épreuve à trois bras de l'héritage ; d'ici sa lecture, rien n'est servi : j'appuie l'option (a) de la décision D4 du plan.

### 2.6 Ce qui empêche de tricher

| triche | garde | cas sain et artefact (règle R5) |
|---|---|---|
| une épreuve qui ne peut pas tuer | le critère n'est écrit par aucun agent ; admission par témoins | l'artefact « tient à toute loi » (code v6 du palier 0b) fait échouer l'admission |
| un script qui fabrique ses lignes | le noyau mesure ; le script ne rend que des décisions | décisions constantes : mort « sans gain » ou « invalide » |
| lire la vérité plantée | elle n'est pas sur la machine ; seuls les lots et l'interface y montent | inventaire du dossier de travail contre une liste blanche ; un leurre de clé glissé arrête l'étage |
| ajuster l'implémentation aux données vues | scellée sur les lots de mise au point, jugée sur des lots neufs | décisions inchangées quand les lots de mise au point changent |
| viser le critère de génération en génération | familles tenues à l'écart, mondes neufs par génération, issue seule rendue (ni valeur ni distance au seuil), confirmation lue une fois | le mécanisme témoin surajusté meurt sur la famille tenue à l'écart |
| un expérimentateur infidèle, qui corrige ou durcit en silence | témoins passés par lui ; seconde implémentation par un développeur pour quelques tentatives tirées par graine | un témoin faux « corrigé » qui tient annule le lot |
| regarder le futur dans un journal | appel par génération, ou rejeu sur journal tronqué | décisions égales sur le journal tronqué |
| repêchage par un juge | invariant du § 2.3 | permutation des sorties de juges : issues identiques à l'octet |

**Exigences tenues** : N-058 ; mondes, témoins, critères et table d'admission scellés avant toute course (R1) ; graines par `SeedSequence`, dérivées par tâche, racine gardée avec la vérité (R9) ; chaque garde sur un cas sain et un artefact, aucun repli (R5) ; versions dans les noms (R12).

## 3. Branchement

### 3.1 Les changements minimaux

Le sommet d'étage de la v69 est à écrire de toute façon pour le palier 1. La plus petite différence : l'écrire une fois, la forme d'épreuve en paramètre, la forme imposée du tour fermé restant la seule valeur admise en réel tant qu'un additif n'en nomme pas d'autre. Aucun fichier existant n'est modifié ; l'additif `cb352811…` reste tel quel ; chaque épreuve de plus a le sien.

1. **Sommet d'étage paramétré** : constructeur de la fiche servie et contrôle d'après-étage en paramètres ; plusieurs générations dès l'écriture (plan, D5).
2. **Rejeu du script scellé** : une boucle qui appelle l'exécuteur du bac sur des lots neufs, sans session de modèle. Seul code neuf du côté de la machine.
3. **Mesure hors machine** : la fonction d'écriture des issues, avec la vérité, chez la mère.
4. **Porte des lots** : composition par graine avec témoins, règle de l'épreuve morte, statuts.
5. **Registre** : la garde « un mort reste mort », l'égalité de comportement.
6. **Table des épreuves** dans le lanceur de course 11 : épreuve → gabarits, banque de mondes, table d'admission, additif, ligne d'accord. Étendre le régime, c'est y ajouter une ligne scellée, non un interrupteur.
7. **Par emploi** : le banc de course greffable et ses mécanismes témoins ; le banc de contre-exemples exacts ; les mondes à scores plantés.

### 3.2 Le bac à sable

Machine louée sous le devis du premier étage payant à tests de mort, essai du bac en première étape (GO-2026-11-20-05, 4b ; additif, § 5.3 et § 5.4). Trois lieux : **le bac** (script d'un modèle : aucun réseau, identité dédiée, dossier neuf) ; **la machine jetable** (orchestrateur de l'étage : aucune variable d'environnement hors liste blanche, `etage_entre_generations_v56.py` ; sortie réseau vers le seul relais ; ni clé ni vérité) ; **la mère** (relais et clés, vérité, mesure, registre). Durée de location bornée par du code (garde 20 de l'additif). Avant destruction par l'identifiant du serveur : inventaire et versement scellé (R-3661). Le banc d'étalonnage, dont les implémentations sont écrites par nous, se joue en local à 0 USD, comme au palier 0a.

### 3.3 Lots, calendrier, coût

Le plan de l'organisme porte les lots E0 à E9 de la course principale, leur calendrier (de l'ordre de 61 heures de sessions, premier allumage au plus tôt le 26 novembre) et le devis du bac. Cette note en révise deux et en ajoute cinq. Conception par Fable, code par Opus, vérification par un autre modèle ; chaque lot avec ses essais sur cas sain et artefact, et trois mutations au moins.

| lot | contenu | classe | heures, ordre de grandeur sous hypothèse |
|---|---|---|---|
| C1 | gabarits, banques de témoins, critères, admission : un texte par emploi | A | 3,5 à 39 par texte |
| C2 | mesure hors machine, porte des lots, registre | B | 2 à 3 |
| C3 | rejeu du script scellé ; paramètre du sommet d'étage (avec le lot E1 du plan) | B | 1 à 2 en plus de E1 |
| E2 révisé | pont à extrait cité, gabarit « mécanisme » | B | 3,75, comme au plan |
| E3 révisé | banc de course greffable, mondes à lois plantées, mécanismes témoins | B | 8 à 15, au lieu de 3,75 |
| M1 | banc de contre-exemples exacts et témoins des deux cibles de défense | B | 4 à 6 |
| S1 | mondes à scores plantés et témoins de la course « seuil et moniteurs » | B | compté par sa conception v2 |

Hypothèses : les lots de code sont comptés comme ceux du plan (de 1,25 à 5,5 heures par lot, § 4) ; E3 entre le banc de la ligne 1, écrit en une session (rapport `af2fc6d6…`), et le code du palier 0b (5 670 lignes, six versions). Repères mesurés : l'orchestrateur v68 écrit en 30 minutes et contre-lu en 12 (`ad42b722…`, `d2cfeac1…`) ; l'additif de la v69, quatre versions, 3 h 21 min de la première consignée au scellement (R-4060, R-4131) ; le texte du palier 0b, 39 heures du mot de Lazar au scellement (GO-2026-11-19-76 ; R-4347). **Les textes décisifs sont le chemin critique, pas le code.**

Coût, hors sessions : 0 USD pour tous ces lots et pour les trois bancs d'étalonnage. Ensuite : course principale, § 2.2 ; mathématiques, § 4.2 ; « seuil et moniteurs », devis de sa conception v2 (20,77, 97,41 et 114,48 USD, R-4399 ; plafond indicatif 120, GO-2026-11-21-16). Machine : de 0,07 à 0,28 USD par location relevée (`registres/depenses.md`, l. 415 à 428).

## 4. Emplois

### 4.1 Premier emploi : la course principale d'auto-conception

1. **Compter**, par un agent habilité à lire les cartes : combien changent l'épreuve, combien une règle de l'orchestrateur, combien la conduite de modèles, combien sont hors gabarit. Sans ce compte, aucun devis.
2. **Écrire et étalonner la porte**, à 0 USD : la surface de modification du banc (un point de greffe par étage du trajet d'une carte), les mécanismes témoins, la table d'admission.
3. **Mesurer l'expérimentateur** sur les seuls témoins, sur la machine jetable : premier chiffre réel du coût d'un greffon, première lecture de fidélité.
4. **Passer les cartes** mises en forme : une issue par carte, sur processeur ; puis devis du barreau 2 pour celles qui tiennent.
5. **Courses suivantes** : la carte porte son engagement ; l'étage joue entre les générations ; la génération suivante lit le registre. C'est ce qui donne une raison à une deuxième génération, que le texte de la v9 n'avait pas (« une génération suivante lirait un héritage jugé », `0d51e0b3…`, « Plan »).

Les épreuves déjà engagées (lignes 1 et 3, héritage) gardent leur texte scellé ; la porte commune vaut pour les cartes qui n'ont pas encore le leur.

### 4.2 Premier emploi : les mathématiques nouvelles, défense et attaque

**Ce qui existe déjà comme épreuve de l'épreuve.** Les artefacts du harnais de l'arbitre formel (preuve inachevée, axiome ajouté, énoncé vide, notation trompeuse, code exécuté à la compilation, réseau) sont un banc de tricheurs écrit. L'essai « preuve formelle contre suite bon marché » est le banc d'étalonnage des deux épreuves du pilier : erreurs plantées par un tiers, jumelles saines, clé de la banque « jamais sur la machine » (brouillon, verdict, point 4). La note du pilier nomme les quatre banques (`docs/notes/ideation-organisme-v1/pilier-generation-v1/note-conception-pilier-generation-v1.md`, `94532165…`, § 3.4).

**Deux mondes plantés pour la défense** [proposition ; formes seulement, à vérifier sur source avant scellement, règle R7].

| cible du pilier | petit monde, vérité calculable | témoin vrai | témoin faux, et ce qui le tue |
|---|---|---|---|
| agrégateur sous corrélation adverse | de deux à quatre moniteurs à alerte binaire, taux fixés, dépendance au choix de l'adversaire : le pire cas d'une règle d'agrégation est un programme linéaire, résolu en rationnels | « les deux alertent ensemble avec une probabilité d'au moins la somme des taux moins un » | « … d'au moins le produit des taux » : faux hors de l'indépendance ; contre-exemple exact à deux moniteurs |
| lemme d'impossibilité | paires de lois sur un petit alphabet, distance en variation totale exacte, puissance du meilleur test par énumération | « la puissance d'un test de niveau α ne dépasse pas α plus cette distance » | « … α plus la moitié de cette distance » : contre-exemple exact sur un alphabet à deux lettres |

Un chercheur de contre-exemples qui ne retrouve pas le contre-exemple scellé d'un témoin faux est une épreuve morte, pour cette taille de monde ; un arbitre qui accepte une cible fausse plantée aussi.

**Côté attaque, au niveau de la méthode.** L'objet éprouvé est le même énoncé nu qu'en défense : une impossibilité ou une borne. Il meurt par un contre-exemple exact, tient par l'arbitre formel, reste ouvert sinon. Un énoncé vrai mais vide se voit au témoin de non-vacuité ; que ses hypothèses soient atteignables ne se prouve pas, cela se mesure sur le banc scellé. La lecture retournée d'un énoncé reste en quarantaine, hors de toute session qui conçoit des moniteurs (`docs/notes/lean-mathematiques-nouvelles-attaque-v1/note-cadrage-v1.md`, `24566704…`, § 2.1 et § 2.2).

**Ce qui est rouvert, ce qui reste un nœud.** GO-2026-11-21-12 avait rouvert : le troisième essai de l'outillage ; l'écriture du préenregistrement du pilote de l'essai ; le pilier pour l'attaque, au niveau de l'idée. **GO-2026-11-21-18 (vers 07:06Z) lève, pour tout le pilier, la fermeture de la couche 4 de l'organisme (N12 (b)) et l'interdit de préparation (DP-1 (a))** : conception et préenregistrement sans dépense. Restent des nœuds : toute course, tout outillage, tout bac, sur devis et ligne à part (même ligne) ; le rattachement au papier C (DP-5 (c), revendication) ; le scellement d'une cible tant que la carte des hypothèses corrigée n'est pas sur `main` (note du pilier, § 1.2). Repères, sans devis : un essai de l'outillage ≈ 0,28 USD (`registres/depenses.md`, l. 422 et 427), 2 à 3 heures de terminal (R-4392) ; pilote de l'essai, plafond proposé 578 USD d'appels et 35 de machine (brouillon, verdict, point 1) ; pilote de génération, de 600 à 3 000 USD d'appels selon la note du pilier (verdict, point 4, hypothèses non vérifiées). Le plan d'avancée du pilier est écrit par un autre agent (R-4388) ; je ne l'ai pas lu.

### 4.3 Second emploi : la course « seuil et moniteurs »

Lazar a choisi l'étage seul sur les propositions déjà rendues (GO-2026-11-21-16). La conception v2 de la course (commit `7c61066c`, ordre `1fbd04c3…`) tient déjà les règles du § 2.1 : forme fixe par deux traducteurs, test le même pour toutes, mort lue sur le taux vrai avec le tirage de calibration pour unité, écart apparié à une base, témoins avant toute candidate. Elle attend cette note pour ses mondes. Ce que j'y ajoute : la vérité hors de la machine ; le programme de l'expérimentateur scellé puis rejoué sur des lots neufs ; les valeurs exactes de la vérité plantée, des témoins et de l'angle mort.

| monde | ce qui est planté | la vérité, exacte | témoins et leur sort attendu |
|---|---|---|---|
| **1, queue connue** | scores honnêtes indépendants, loi continue connue ; saboteur décalé, aire sous la courbe 0,69, 0,80 ou 0,95 | pour un seuil s, le taux vrai est 1 − F(s) ; le seuil pris au k-ième plus grand de n a un taux de loi bêta | *doit mourir* : « le 3ᵉ plus grand de 300, certifié à 95 % » (couverture vraie 0,578) [A] ; « ne jamais alerter » (puissance nulle) [C]. *Doit tenir* : « le plus grand de 299 » (0,9505) [A] ; le 3ᵉ de 300 sous l'engagement « en moyenne » (taux moyen 0,00997) [A bis]. *De marge* : « le 6ᵉ de 1 000 » (0,934 pour 0,95) [A] |
| **2, changement de régime** | la moyenne des scores honnêtes se décale entre l'étalonnage et le service | un décalage de 0,446 écart type triple un taux de 1 % ; la couverture du « plus grand de 299 » tombe de 0,9505 à 0,566 [D] | une règle qui déclare tenir sous dérive et ne s'abstient pas doit mourir ; la même, qui ne le déclare pas : fragilité rapportée, pas une mort |
| **3, grappes par famille** | score = effet de famille + bruit ; corrélation 0,2 [proposition] | couverture du « plus grand de 300 » : 0,951 pour 300 familles d'un épisode, 0,817 pour 3 familles de 100 [E] | « certifié à 95 % sur 3 familles » doit mourir ; à 30 familles de 10 (0,935), témoin de marge |
| **4, déploiement** | suite d'épisodes, taux d'alerte honnête 0,20, horizon 300 [propositions] | par programmation dynamique exacte [F] | *doit mourir* : le test répété sans correction (fausse alerte 0,077 par déploiement pour 0,01 annoncé). *Doit tenir* : le pari de Bernoulli au seuil 100 (0,0076), qui sonne à 0,888 contre un saboteur à 0,30 et sonne à tort à 0,272 si le taux honnête dérive à 0,25 |

**L'angle mort, dit d'avance.** Avec 400 tirages et un test exact au niveau 0,001 [propositions], un engagement « certifié à 95 % » meurt à 364 tirages conformes ou moins : le 3ᵉ de 300 est tué avec une probabilité de 1,0000 à quatre décimales, le plus grand de 299 cinq fois sur dix mille, le 6ᵉ de 1 000 quatre fois sur cent ; une couverture vraie au-dessus de 0,892 est tuée moins de neuf fois sur dix [B]. Aux valeurs que la conception propose (2 000 tirages, borne exacte à 99 %), cette limite monte à 0,930 [G]. Deux faits utiles au gel : à 200 épisodes, aucun seuil fini n'est certifiable à 95 % sans hypothèse de forme (le plus grand des 200 couvre à 0,866), et une candidate qui y « tiendrait » ainsi sans s'abstenir signale une mesure fausse ; le témoin valide de la conception (le plus grand score, garantie « en moyenne ») a une marge large contre une mort « invalide » par hasard : son taux moyen est la moitié de 1 % (0,00498 à 200 épisodes) [G].

La réponse de fond déjà rendue (`docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/reponse-fable-v1.md`, `add9a2d3…`) passe l'étage comme les autres : ses règles sont des candidates, non des témoins. Limite, à écrire dans tout texte : une règle qui tient ici tient sous des lois que nous avons choisies.

## 5. Vérification hors du programme

1. **Engagement avant, révélation après.** Empreintes de la banque de mondes, de la table des témoins, des critères et de la table d'admission déposées chez le tiers avant toute course, comme les manifestes déjà déposés (R-2397) ; clés et graines révélées après.
2. **Un banc rejouable sans nous** : générateur, mesure et témoins en un paquet à bibliothèque standard et `numpy` ; la table d'admission se recalcule.
3. **Des vérités que personne ne nous doit** : les lois exactes se refont à la main ; une preuve acceptée se rejoue par le noyau à la version épinglée ; un contre-exemple exact se vérifie en trois lignes.
4. **Des témoins publics** : les procédures publiées et leurs codes publics, que la réponse de fond nomme, entrent comme témoins vrais dans leur domaine déclaré ; si notre épreuve en tue une, l'un des deux a tort, et l'audit est le même dans les deux sens (règle R4).
5. **Des tricheurs écrits par un tiers**, contre l'interface publiée, au niveau de la méthode ; le tableau des morts est calculé par le noyau. Un contact est un nœud.
6. **Mutations publiées, registre entier** : chaque garde retirée fait échouer un essai ; morts et lots nuls sont au registre, un tiers recompte.
7. **Une donnée réelle où la vérité de la queue est bon marché** (réponse de fond, § 4, point 1) : ce que le monde planté ne dit pas, un grand lot public rééchantillonné le dit.

## 6. Décisions pour toi, risques, ce que je n'ai pas vérifié

Les décisions D1 et D3 à D7 du plan de l'organisme restent posées par lui. Je n'ajoute que ce que cette conception commande.

**N1 — Ce qu'un test de mort éprouve sur une carte d'auto-conception** (D2 du plan).
- Enjeu : c'est le blocage de fond ; sans réponse, l'étage refuse chaque fiche.
- (a) Course appariée à deux barreaux, banc puis course réelle, épreuve imposée, pont à extrait cité pour les 94 cartes. Avantage : éprouve le mécanisme lui-même, tue à bas prix, ne touche pas aux cartes scellées. Inconvénient : « tient au banc » ne vaut que sous des proposeurs écrits par programme ; un banc à écrire.
- (b) Course réelle seulement. Avantage : la seule épreuve qui réponde pour tous les mécanismes. Inconvénient : de l'ordre de 590 USD par carte à cinq espèces.
- (c) Engagement écrit par le proposeur, joué par l'étage tel quel. Avantage : aucun banc. Inconvénient : le proposeur écrit le test que sa carte passe.
- Recommandation : (a), confiance 0,7. Aucun défaut : c'est le nœud qui commande le reste.

**N2 — Les champs de fiche des courses suivantes** (rouvre GO-2026-11-20-05, 3a).
- Enjeu : sans engagement dans la carte, chaque carte passe par deux traducteurs.
- (a) Trois champs fermés de plus, dix gardés. Avantage : plus de pont. Inconvénient : consigne et texte neufs ; la comparaison champ pour champ avec la v9 est perdue.
- (b) Inchangés, pont pour toujours. Avantage : 3a tient. Inconvénient : des cartes hors gabarit en nombre inconnu.
- Recommandation : (a) pour la suite, (b) pour les 94 cartes ; confiance 0,65. Aucun défaut.

**N3 — Un seul texte scellé pour la porte commune.**
- Enjeu : la règle R1 veut un préenregistrement par expérience décisive ; à une file, vingt-deux textes écrits à la main tiennent jusqu'au 30 novembre au matin (ordre v3, § 1).
- (a) Un préenregistrement de la porte, contre-lu, et par carte un engagement en forme fixe scellé avant toute course. Avantage : l'échelle. Inconvénient : les bras propres à une carte disparaissent, sauf ceux de la liste fermée des bases.
- (b) Un texte par ligne, comme aujourd'hui. Avantage : épreuve sur mesure. Inconvénient : le rythme constaté.
- Recommandation : (a) pour les cartes sans texte scellé ; confiance 0,6. Aucun défaut : lecture d'une règle gelée.

**N4 — Le modèle et le plafond de l'expérimentateur d'épreuve.**
- Enjeu : celui de la v67 est absent ; changer de modèle demande ton mot ; le coût d'un greffon n'est pas mesuré.
- (a) Un modèle d'une autre lignée que le lecteur témoin, nommé par toi parmi les relais ouverts ; plafond fixé après la mesure sur les témoins. Avantage : part tôt. Inconvénient : pas de continuité avec la v67.
- (b) Attendre le retour du modèle de la v67. Avantage : continuité. Inconvénient : sans date.
- (c) Deux lignées sur toutes les tentatives. Avantage : fidélité mesurée partout. Inconvénient : coût double.
- Recommandation : (a), avec la seconde implémentation sur un tirage de tentatives ; confiance 0,6. Aucun défaut.

**N5 — La règle de l'épreuve morte.**
- Enjeu : ce que vaut une issue quand un témoin est mal classé.
- (a) Un témoin « doit mourir » qui tient annule l'épreuve ou le lot ; un témoin « doit tenir » qui meurt est compté et n'annule qu'au-delà d'une borne exacte gelée. Avantage : sévère là où l'erreur trompe. Inconvénient : des lots perdus.
- (b) Annulation dans les deux sens. Avantage : simple. Inconvénient : un expérimentateur maladroit annule tout.
- Recommandation : (a), confiance 0,65. Défaut sous 48 heures : (a).

**N6 — Où se calcule l'issue.**
- Enjeu : la lecture de la vérité plantée par du code écrit par un modèle.
- (a) Chez la mère : ni clé ni vérité sur la machine jetable. Avantage : lire la vérité est impossible par construction. Inconvénient : un lot annulé se rejoue à la session suivante.
- (b) Sur la machine, vérité hors du bac. Avantage : rejeu dans la même location. Inconvénient : la vérité cohabite avec ce code.
- Recommandation : (a), confiance 0,8. Défaut sous 48 heures : (a).

**N7 — L'ordre au pilier mathématique**, maintenant qu'il est rouvert.
- Enjeu : produire des énoncés avant de savoir les tuer, ou après.
- (a) Les épreuves d'abord : outillage, banc de contre-exemples exacts, banques de témoins, pilote de l'essai ; la génération ensuite. Avantage : aucune conjecture n'est acceptée par une chaîne non étalonnée. Inconvénient : rien de neuf avant plusieurs jours.
- (b) Génération tout de suite, épreuves en parallèle. Avantage : matière plus tôt. Inconvénient : des acceptations qu'il faudra rejouer.
- Recommandation : (a), confiance 0,75. Défaut sous 48 heures : (a) pour la conception ; toute dépense reste sur devis.

**Risques.**
1. Le banc à proposeurs écrits par programme n'est pas l'organisme : une carte peut y tenir et ne rien valoir, y mourir et valoir. D'où « tient au banc », et le barreau 2.
2. Les mondes sont choisis par nous. Parades : famille tenue à l'écart, témoins publics, donnée réelle.
3. Angle mort : une proposition fausse de peu survit ; il est chiffré, il n'est pas fermé.
4. Fidélité de l'expérimentateur et des traducteurs : mesurée par témoins ; des témoins trop classiques la surestiment, il en faut d'inédits, à comportement calculable.
5. Coût du greffon inconnu à un facteur cinquante près.
6. Le bac n'offre que la bibliothèque standard (« SUPPOSÉ » dans la consigne de l'étage) : les idées qui demandent de l'optimisation numérique seront plus souvent « non exécutables ». Biais à rapporter par gabarit.
7. Une fois les issues servies entre générations, la visée du critère devient réelle : mondes neufs, issue seule, confirmation lue une fois.

**Ce que je n'ai pas pu lire ou vérifier.**
- Le dépôt de l'orchestrateur (absent ici) ; les lanceurs réels du tour fermé, donc où tournaient relais et orchestrateur à la v67 ; le code du paquet v68 au-delà de ses empreintes ; `tests_de_mort_v2.py` et `tour_ferme_v64.py`, lus par parties.
- Aucune carte de la course v9 (dossier interdit) : la part des cartes par barreau est inconnue. Aucune sortie du palier 0b ni d'aucune épreuve en cours ; aucun résultat interdit par le mandat.
- Le banc de la ligne 1 au-delà de son en-tête et de la table de ses fonctions : qu'il se rende greffable sans réécriture n'est pas établi.
- Le coût d'un greffon ; la durée d'une exécution nue du bac ; `numpy` dans le bac de la machine louée ; la tenue de gros fichiers numériques par le chargeur de tranche et son filtre de secrets.
- La décision de Lazar sur le proposeur qui expérimente, après la synthèse du collisionneur : non retrouvée.
- Le plan d'avancée du pilier mathématique (R-4388) et la conception du moniteur de dissonance (R-4382) : non lus. La note de cadrage de l'attaque : lue ; elle ne porte aucun mode.
- Antériorité : rien n'est revendiqué, rien n'a été cherché. Témoins plantés, contrôles positifs et négatifs, mutations, surajustement adaptatif, falsification séquentielle par des agents sont publiés ; toute sortie reprend les citations obligatoires de N-064 et de N-067.
- Mes calculs ne sont pas contre-lus. Les valeurs marquées [proposition] ne viennent d'aucune mesure.
- Routine de reprise : les trois empreintes de lancement vérifiées, conformes ; ni la vérification de l'arbre, qui hacherait des dossiers interdits, ni les tests.
- Incident : une sortie de commande trop longue a été rangée d'office par l'outil sous `/root/.claude/` ; je ne l'ai pas ouverte.
