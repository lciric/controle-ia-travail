# Conception des idées originales du relevé — plus petits essais, part processeur, devis par ligne — v1

**Statut.** Note de conception pour une **demande de GO** (R-2851 : « note de conception avec devis par ligne ; ce qui ne coûte
que du processeur se prépare ; aucune dépense avant un GO sur devis »). **Aucune dépense n'est autorisée par cette note** ;
aucune ligne de GO n'est inscrite ; chaque essai payant demandera en plus son propre préenregistrement scellé et contre-lu (R1,
R2). Rien ici n'est un résultat. Aucun nom de modèle : les proposeurs sont désignés par leur prix (section 1).

- Auteur : concepteur neuf (modèle A au sens de R-2851), sous-agent de la session mère ; je n'ai écrit ni le relevé, ni les
  fiches, ni aucune pièce citée.
- Date : 2026-11-15, rédaction de 08:40 à 08:46 environ (`date -u`).
- Relevé : `docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/releve-idees-reutilisables-v1.md`
  (`bd253b6c68f6baada0e61b5381f029b52838ca34aa092502e55253c662451c6c`), § 2.2 (b), § 3.1, § 3.2, § 4.1, § 4.3 et § 5 ; fiches de
  `runs/course-ideation-conception-propre-v1/20261113-235541-course-ideation-conception-propre-v1-g1/copies/sortie--fiches-validees.json`
  (`a9f9594e2dc3a7a553c54577202817758e3f7ef231445f1a48d500fc647389d5`) : opus-p1-03 (n° 7), opus-p1-04 (n° 8), argon-p1-04 (n° 3),
  argon-p2-04 (n° 17), opus-p1-02 (n° 6), argon-p2-05 (n° 18), argon-p1-05 (n° 4).

## 0. En bref

| idée | question tranchée | plus petit essai | attendu (USD) | pire (USD, plafonds du pilote) | nœuds |
|---|---|---|---|---|---|
| (i) placebo par monde jumeau | l'information d'une table de données pousse-t-elle vers la composante conditionnelle, ou sa seule présence ? | 1 génération, 20 mondes, 3 bras, 60 appels du proposeur le moins cher | 17,00 | 123,00 | dessin neuf (une donnée entre dans la vue) |
| (ii) proposeurs en série | voir les cartes brutes des pairs disperse-t-il ou regroupe-t-il les propositions ? | 1 génération, 20 mondes, 3 bras, 4 sessions par bras, 240 appels | 63,30 | 483,00 | dessin neuf (des cartes de pairs dans la vue) |
| (iii) deux passes | choisir les traits pas cher puis écrire la loi cher couvre-t-il plus par dollar ? le cher est-il nécessaire ? | 1 génération, 20 mondes, 4 bras, 120 appels | 63,30 | 243,00 | GO seulement |
| (iv) demi-générations | mettre l'archive à jour à mi-génération couvre-t-il plus, et plus profond, à dollars égaux ? | 2 générations, 20 mondes, 3 bras, 200 appels, test de mort mécanique | 30,30 | 243,00 | dessin neuf (calendrier) ; test de mort simplifié |
| (v) appel des chers sur le regroupement | ne payer la moitié chère que si la moitié bon marché ne rend que des copies épargne-t-il sans perte ? | rejeu sur processeur des traces de v67, puis 1 génération, 20 mondes, 80 appels, règle et placebo rejoués sur les mêmes appels | 73,30 | 183,00 | règle de composition à l'exécution (N-058) |
| **ensemble** | | | **247,20** (221,20 avec le témoin commun, section 4) | **1 275,00** (650,00 si le plafond de session du proposeur le moins cher passe à 0,75) | dépense : nœud, sans défaut |

**Recommandation** (section 6) : après le pilote MR-2, un premier GO sur (v) puis (iii) (question QO1 « la frontière est-elle
nécessaire ? », le bon marché d'abord, N-045 point 4), ≈ 137 USD attendus (≈ 121 avec le témoin commun) ; confiance 0,55.

## 1. Sources des prix (chaque prix vient d'une pièce du dépôt)

| prix | valeur | source (chemin, empreinte) | nature |
|---|---|---|---|
| un appel de proposeur sur un monde planté riche (au plus 6 cartes), quatre postes | **Pr-1** 0,25 attendu / 2,00 plafond de session ; **Pr-2** 0,80 / 2,00 ; **Pr-3** 1,00 / 2,00 ; **Pr-4** 1,60 / 3,00 | devis du pilote MR-2, `docs/notes/organisme-multi-generations-v1/pilote-v1/sorties/devis-pilote-v2.json` (`dba76367488ca0b7c66fbf66f03e44357cf5ad02d99b267d522ab2489542c350`), champs « central_proposeur » et « plafond_session », produit par `…/pilote-v1/outils/devis_pilote_v2.py` (`fa475e7a…`) | **estimé** (« tout estimé sauf les plafonds », préenregistrement du pilote, brouillon 4, `04ada9fa…`, section « Devis ») |
| machine du pilote | 0,30 attendu / 3,00 plafond | même fichier, poste « machine » | estimé / plafond |
| barèmes par million de jetons (entrée / sortie) | 4 / 20 et 10 / 50 (proposeurs par le relais du noyau) ; 8,3 / 41,5 (proposeur externe, « supposé ») ; 2 / 10 (page du fournisseur lue le 30 octobre) | devis de la course « conception propre », `docs/notes/organisme-conception-propre-v1/devis-v1.md` (`ce679a533a90a2a7b2feea1f0269429161ecc3467fd06f32ba83e611ed90bf2b`), § 1 | relevé ou supposé, comme dit |
| barème d'un proposeur externe, page officielle relevée le 14 novembre | 10 / 50 (standard), 5 / 25 (palier différé) | fichier de prix v2 du dossier `docs/notes/organisme-conception-propre-v1/` (nom de la forme `prix-<proposeur>-v2.md`, le seul « prix-…-v2 » du dossier ; `bf211a074868f49175bd59089a3082ec78da0d545850145ca27743b260ac78df`) | relevé |
| mesuré : course réelle v67 (monde jouet, deux proposeurs) | relais A : 30 appels, 1,13813 USD ; relais B : 16 appels, 0,85618 USD ; machine 3 h 18 : ≈ 0,27 USD | `registres/depenses.md`, lignes du 2026-11-12 sous GO-2026-11-12-06 | mesuré (les appels de proposeur n'y sont pas séparés des autres rôles) |
| mesuré : deux appels de proposeur à v67 | 31 891 et 38 343 jetons de sortie (au barème 2 / 10 : ≈ 0,32 et 0,38 USD de sortie) | verdict de v67, `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` (`d79024328157aafc5c801b5b0a4a621a5c009f367d88b96bbbfaeaeef3753459`), § 4.1 | mesuré ; **compte de ce fournisseur suspendu faute de solde le 14 novembre** (`registres/depenses.md`, ligne R-2645) |
| sondes des quatre relais du pilote | 0,079 et 0,099 USD par sonde complète | `registres/depenses.md`, lignes R-2731 et R-2769 | mesuré (appels de contrôle seulement) |
| carte graphique pour un instrument local | 0,3956 à 0,4489 USD par heure (RTX 4090) ; 1,04 à 1,25 USD par heure (A100) | `registres/depenses.md`, lignes du 14 et du 15 novembre (R-2789, R-2836, R-2840, R-2862) | mesuré |

**Réserve.** Les prix par appel sont **estimés** ; le pilote MR-2 (non joué à ce jour : il attend la vérification de sa procédure
v7, R-2849) les mesurera. Recommandation : jouer ces essais **après** le pilote et refaire chaque devis sur ses coûts mesurés ;
le pilote dit aussi si de vrais proposeurs trouvent une composante conditionnelle **avant** sa condition (faits du
collisionneur, `d19b5400…`, § 4 : hypothèse non mesurée), ce dont dépendent (i) et (iv).

## 2. Cadre commun des essais payants

- **Mondes** : famille MR-2 du pilote (monde riche à composantes conditionnelles, générateur `docs/notes/organisme-multi-generations-v1/outils-v4/monde_riche_v4.py`,
  `4b1658477811fb87360dda44a65b0af96e87ae1d2ca4a32bdabbd3ce6cc19eb8`, et le code du pilote), **écrits par programme à graine
  scellée** (R-2461) ; 20 mondes neufs par essai, jamais servis ailleurs.
- **Archive de départ** {K1} et **une génération** (sauf (iv)), comme le bras A du pilote ; **gardien mécanique seul** ; mesure
  **par l'oracle sur les cartes brutes** (programme du pilote `…/pilote-v1/outils/mesure_pilote_v4.py`,
  `676d5f37f21cf5d512f92d2029991fa8795a77076c285ea9bd83c43841748365`, et `…/outils-v1/complements_synthese_v1.py`, fonction
  `couverture`, `89eb7ba8…`), lue une seule fois. **Aucun juge, aucun test de mort** sauf en (iv) : la composition se juge sur
  l'oracle et le coût seuls (N-058).
- **Taille** : 20 mondes par bras donnent une puissance d'environ 0,80 pour voir passer de 0,05 à 0,40 la part des mondes où
  une carte porte la composante visée (test exact de Fisher unilatéral à 5 % ; mon compte, 3 000 simulations : 0,80 à 20 mondes,
  0,55 à 12, 0,89 à 24 ; annexe A). Ce sont des **cribles pour un grand effet** : un résultat nul ne dit rien d'un petit effet.
- **Égalité de coût** : chaque bras est arrêté avant tout appel qui dépasserait le coût mesuré du témoin quand la fiche le
  demande ; les cartes refusées au gardien comptent (recoupement, `eecd98fa…`, § 10).
- **Contrôles** repris du relevé (§ 5) : monde jumeau, cartes d'un autre monde de même longueur, même découpage sans le
  mécanisme, mondes sans la structure visée.

## 3. Les cinq idées

### (i) Placebo par monde jumeau (opus-p1-03 ; relevé § 2.2 (b) et § 5)

**Ce que c'est.** Le placebo d'une table calculée sur des données du monde (fréquences des issues dans les quatre cases de
chaque croisement de deux traits coupés à la médiane, sur 2 000 épisodes publics tirés une fois, disjoints des tirages du juge) :
la même table, calculée sur le **monde jumeau** — le même monde **sans ses composantes conditionnelles**, dont les marges par
trait sont les mêmes à la tolérance près (une conditionnelle est nulle en moyenne sur l'autre trait, faits § 4) — servie aux
proposeurs, dont les cartes sont mesurées **sur le vrai monde**. Pour une table purement syntaxique de l'archive (§ 2.2 (a)), le
jumeau ne s'applique pas (la table ne dépend d'aucune issue) : son placebo est une table de même format tirée au hasard
(recoupement, § 10).

**Question tranchée.** Le gain d'une table croisée vient-il de son **information** sur la composante cachée, ou de sa seule
présence, de sa forme et de sa longueur (une poussée générique vers `si_sinon`) ?

**Plus petit essai.** 20 mondes MR-2 portant au moins une conditionnelle dont la condition n'est pas dans {K1} ; trois bras :
sans table, table vraie, table du jumeau ; un appel de Pr-1 par bras et par monde (6 cartes). Mesure : part des mondes où une
carte brute porte la conditionnelle (oracle) ; part des cartes de forme `si_sinon` ; copies de l'archive. Lecture : **effet
d'information** si « table vraie » dépasse « jumeau » (Fisher, 5 %) et que « jumeau » ne dépasse pas « sans table » ; **effet de
forme** si « jumeau » dépasse « sans table » ; sinon rien. Confirmation facultative avec Pr-2 sur les mêmes mondes.

**Processeur seul, sans GO.** Générateur du jumeau (retrait des conditionnelles : `compiler_v4(spec, sans=…)` du générateur v4) ;
contrôle écrit d'égalité des marges par trait (test du khi-deux sur 2 000 épisodes, tolérance fixée avant) ; constructeur de la
table (coupure à la médiane, paires dans l'ordre des noms de traits, troncature à un budget fixe de jetons) ; mesure de la
longueur servie ; essai à blanc avec des proposeurs scriptés (`proposeurs_references_v59`).

**Devis par ligne.**

| ligne | appels | prix unitaire (attendu / plafond) | attendu | pire | source |
|---|---|---|---|---|---|
| Pr-1, 3 bras × 20 mondes | 60 | 0,25 / 2,00 | 15,00 | 120,00 | devis du pilote |
| entrée de la table (≈ 5 000 jetons sur 40 appels) | — | 8,3 USD par million | 1,70 | compris dans le plafond de session | devis « conception propre », § 1 |
| machine | — | 0,30 / 3,00 | 0,30 | 3,00 | devis du pilote |
| **total** | | | **17,00** | **123,00** | |
| facultatif : confirmation Pr-2, mêmes 60 appels | 60 | 0,80 / 2,00 (+ entrée ≤ 10 USD par million) | 50,00 | 120,00 | devis du pilote ; devis « conception propre » |

**Décisions.** N-058 : la table et ses bras se jugent sur l'oracle et le coût ; aucun juge. N-044 : famille de conception (MR-2) ;
l'universalité d'une vue adoptée se mesurera sur des familles jamais vues. N-045 (3) : l'essai mesure aussi si le proposeur le
moins cher profite de la table. **Nœud** : une donnée nouvelle (des issues d'épisodes publics) entre dans la vue ; elle n'est ni
verdict, ni oracle, ni loi plantée, mais c'est un **dessin neuf** (relevé § 2.2 ; synthèse § 7) ; et une table qui pousse vers
`si_sinon` pousse vers la classe que le nul v8 ne couvre pas : toute course à juge qui suivrait dépend du nœud R-1779 (préenregistrement
de l'idée 1.1 de ce dossier).

### (ii) Proposeurs en série (opus-p1-04 ; relevé § 3.2)

**Question tranchée.** Servir à chaque proposeur, en session neuve, les cartes **brutes** déjà rendues par les précédents de la
génération (sans verdict, avec la phrase factuelle du regroupement) **disperse**-t-il les propositions sur davantage de
composantes, ou les **regroupe**-t-il (grégarisme) ?

**Plus petit essai.** 20 mondes ; trois bras de quatre sessions : parallèle (quatre sessions indépendantes) ; série (ordre tiré à
graine scellée, la session de rang k voit les cartes des rangs 1 à k − 1) ; série placebo (même nombre de cartes, de même
longueur, **tirées d'un autre monde** de la famille). Version bon marché : les quatre places tenues par des sessions neuves de
Pr-1 (sépare le mécanisme de la composition). Mesure : nombre de composantes plantées distinctes touchées par les cartes brutes
d'un monde (oracle) ; nombre de groupes prédictifs (regroupement public) ; part de quasi-doublons. Lecture appariée par monde
(rangs signés de Wilcoxon) : **dispersion** si série > parallèle et placebo ≈ parallèle ; **grégarisme** si série < parallèle ;
**effet de contexte** si placebo ≈ série.

**Processeur seul.** Harnais en série (sessions neuves, ordre scellé, extraction des cartes des réponses brutes scellées) ;
réserve de cartes d'un autre monde de même longueur ; regroupement (`complements_synthese_v1.grouper_stratifie`) ; mesure ; essai
à blanc avec proposeurs scriptés.

**Devis par ligne.**

| ligne | appels | prix unitaire | attendu | pire | source |
|---|---|---|---|---|---|
| Pr-1, 3 bras × 4 sessions × 20 mondes | 240 | 0,25 / 2,00 | 60,00 | 480,00 | devis du pilote |
| entrée supplémentaire des rangs 2 à 4 (≈ 3 000 jetons sur 120 appels) | — | 8,3 USD par million | 3,00 | compris | devis « conception propre » |
| machine | — | 0,30 / 3,00 | 0,30 | 3,00 | devis du pilote |
| **total** | | | **63,30** | **483,00** (183,00 si le plafond de session de Pr-1 passe à 0,75) | |

**Décisions.** N-045 (1) : « l'ordre et la forme des échanges » sont une variable de composition à apprendre ; l'essai en donne
la première mesure. N-058 : ordre tiré au hasard, jamais choisi sur un résultat ; série contre parallèle jugés sur l'oracle et le
coût. Co-Scientist (C1 du catalogue, `ddfb2522…`) occupe les échanges à tournoi et à débat : ici, aucun classement, aucun juge à
modèle. **Nœud** : des cartes de pairs entrent dans la vue : dessin neuf.

### (iii) Deux passes : traits choisis pas cher, loi écrite cher (argon-p1-04, argon-p2-04 ; relevé § 3.1)

**Question tranchée.** Une passe bon marché qui propose vingt ensembles de 1 à 3 traits, réduits par un **programme
déterministe sans juge** (retrait des ensembles de l'archive, puis six ensembles choisis par une règle gloutonne de distance de
Jaccard), suivie d'une passe chère qui écrit une carte par ensemble, couvre-t-elle davantage de composantes **par dollar**
qu'un appel cher seul ? Et la passe chère est-elle nécessaire (QO1) ?

**Plus petit essai.** 20 mondes ; quatre bras : (1) standard : un appel de Pr-2 ; (2) deux passes : un appel de Pr-1 (20
ensembles), le filtre, un appel de Pr-2 sur les six ensembles ; (3) ensembles au hasard : six ensembles tirés par le programme sous
le même filtre, puis Pr-2 (sépare le choix du modèle bon marché de la seule mise en forme) ; (4) tout bon marché : Pr-1 écrit les
six cartes de ses propres ensembles (ablation de la frontière). Mesure : composantes couvertes par les cartes brutes (oracle),
par dollar ; mesure d'exécution (la carte k emploie-t-elle les traits de l'ensemble k ?) ; part des cartes bâties sur des traits
de pur bruit (piège nommé par la fiche). Variante d'instrument local pour la passe 1 : une carte graphique louée 1 à 2 heures
(≈ 0,40 à 0,90 USD), plus la mise en place.

**Processeur seul.** Filtre de Jaccard et ses essais (égalités rompues par l'ordre des noms) ; extraction des ensembles de traits
de l'archive ; gabarit de la passe 1 ; mesure d'exécution ; essai à blanc.

**Devis par ligne.**

| ligne | appels | prix unitaire | attendu | pire | source |
|---|---|---|---|---|---|
| Pr-2, bras 1 à 3 × 20 mondes | 60 | 0,80 / 2,00 | 48,00 | 120,00 | devis du pilote |
| Pr-1, bras 2 (20) et bras 4 (40) | 60 | 0,25 / 2,00 | 15,00 | 120,00 | devis du pilote |
| machine | — | 0,30 / 3,00 | 0,30 | 3,00 | devis du pilote |
| **total** | | | **63,30** | **243,00** (168,00 au plafond de 0,75 pour Pr-1) | |

**Décisions.** N-045 (1) et (3) : un rôle passe au bon marché ; le bras 4 mesure ce que perd le rôle sans la frontière ; (7)
espaces de conception égaux : le bras 3 sépare l'effet du format de celui du choix. N-058 : jugé sur l'oracle et le coût. N-044 :
famille de conception. **Nœud** : la dépense seulement.

### (iv) Demi-générations (opus-p1-02 ; relevé § 4.1)

**Question tranchée.** Une génération de six cartes devenue deux demi-générations de trois, avec la chaîne entre les deux
(gardien, juge, test de mort, sélection, archive), couvre-t-elle davantage de composantes, et de chaînes de profondeur 2, **à
dollars égaux** ? Le placebo sépare la mise à jour du simple découpage.

**Plus petit essai.** 20 mondes MR-2 portant une chaîne de profondeur 2 ; deux générations ; Pr-1 seul ; trois bras : (1) standard
(un appel de six cartes par génération) ; (2) demi-générations (deux appels de trois, chaîne entre les deux) ; (3) placebo (deux
appels de trois **sans** mise à jour entre eux). Bras 2 et 3 plafonnés au coût mesuré du bras 1, monde par monde. Chaîne : juge sur
processeur sous le nul de production, et **test de mort mécanique** (la statistique gelée calculée par l'orchestrateur sur des
épisodes frais, sans expérimentateur ni vérificateur) : simplification déclarée, qui retire le poste le plus cher de la chaîne
réelle (borne par test de l'expérimentateur de 0,80 à 3,40 USD selon le modèle, conception du monde riche v3, `386d48ba…`, § 6.2). Mesure : composantes couvertes par les
retenues, profondeur atteinte, copies et fausses retenues (oracle), dollars.

**Processeur seul.** Chaîne à demi-générations sous des noms neufs, test de mort mécanique, garde d'égalité de dollars ; essai à
blanc complet avec proposeurs scriptés (mode à blanc de `a_blanc_v59`, `606aa8b4…`, de la copie du code `94bfd92`).

**Devis par ligne.**

| ligne | appels | prix unitaire | attendu | pire | source |
|---|---|---|---|---|---|
| Pr-1, bras 1 : 2 générations × 20 mondes | 40 | 0,25 / 2,00 | 10,00 | 80,00 | devis du pilote |
| Pr-1, bras 2 : 2 × 2 × 20, plafonné au bras 1 | 80 | au plus le coût mesuré du bras 1 | 10,00 | 80,00 | règle d'égalité de la fiche |
| Pr-1, bras 3 : idem | 80 | idem | 10,00 | 80,00 | idem |
| machine | — | 0,30 / 3,00 | 0,30 | 3,00 | devis du pilote |
| **total** | | | **30,30** | **243,00** (93,00 au plafond de 0,75) | |

**Décisions.** N-058 : le nombre de demi-générations est fixé d'avance, jamais piloté par les promotions ; les promotions du juge
alimentent l'archive comme dans toute course (sélection de cartes, non d'agents) ; la comparaison des dessins se juge sur l'oracle
et le coût. N-045 (5) : l'essai raccourcit le délai de l'héritage d'une génération ; aucun signal d'apprentissage n'est servi.
Dépendances : l'hypothèse « une conditionnelle se trouve après sa condition » (faits § 4) ; le nul du juge (une demi-génération
produit des variantes que le nul doit refuser comme copies : nœud R-1779, idée 1.1 de ce dossier). **Nœuds** : calendrier neuf
(dessin neuf) ; test de mort mécanique au lieu de la chaîne scellée de la boucle réelle (écart, à dire au préenregistrement).

### (v) Appeler les proposeurs chers sur le regroupement des doublons, sans le juge (argon-p2-05, point 1 ; relevé § 4.3)

**Question tranchée.** N'appeler la moitié chère des proposeurs (Pr-3, Pr-4) que si plus de 80 % des cartes valides de la moitié
bon marché (Pr-1, Pr-2) sont déjà dans le nul de l'archive **au sens du regroupement** (distance au nul sous ε sur un jeu public
d'instances **sans issue**), épargne-t-il des dollars **sans perte de couverture** ? C'est aussi une mesure de la nécessité de la
frontière (N-045, point 3).

**Ce qui est écarté.** Les points 2 et 3 de la fiche (arrêter une course stérile ; ouvrir des générations tant que l'archive
grandit) pilotent le dessin par les promotions du juge : exclus (N-058 ; faits § 4 : la diversité ne pilote pas le nombre de
générations ; N-053, point 5). La partie d'argon-p1-05 sur l'arrêt de course l'est pour la même raison.

**Processeur seul, d'abord.** Regroupement « carte contre archive » (adaptation de `grouper_stratifie` : distance au nul engendré
par chaque loi d'archive, ε = 0,01 nat, lecture par strates à 0,04, conception v3, `386d48ba…`, § 3.1), essais ; **rejeu sur les
23 cartes réelles de v67** et leurs archives : quelle décision la règle aurait prise, quelle part du budget elle aurait épargnée
(sans rien dire de la couverture).

**Plus petit essai payant.** Une génération, 20 mondes, **les quatre proposeurs appelés partout** (une seule course) ; la règle et
un placebo (moitié chère retirée au hasard, à la même fréquence que sous la règle) sont **rejoués sur les mêmes appels** : les
appels étant des sessions neuves indépendantes, « ne pas appeler » revient à retirer les cartes de la moitié chère. On obtient,
pour une génération, le contrefactuel exact : couverture avec et sans, dollars épargnés. L'effet sur plusieurs générations (les
dollars épargnés réinvestis) demande des courses séparées, à décider sur ce résultat.

**Devis par ligne.**

| ligne | appels | prix unitaire | attendu | pire | source |
|---|---|---|---|---|---|
| Pr-1, 20 mondes | 20 | 0,25 / 2,00 | 5,00 | 40,00 | devis du pilote |
| Pr-2, 20 mondes | 20 | 0,80 / 2,00 | 16,00 | 40,00 | devis du pilote |
| Pr-3, 20 mondes | 20 | 1,00 / 2,00 | 20,00 | 40,00 | devis du pilote |
| Pr-4, 20 mondes | 20 | 1,60 / 3,00 | 32,00 | 60,00 | devis du pilote |
| machine | — | 0,30 / 3,00 | 0,30 | 3,00 | devis du pilote |
| **total** | | | **73,30** | **183,00** (158,00 au plafond de 0,75 pour Pr-1) | |

**Décisions.** N-058 : la règle décide à l'exécution d'une partie de la composition sur un critère qui n'est **ni** le verdict du
juge **ni** l'oracle (un calcul public sans issue) ; son évaluation contre « tout appeler » se fait sur l'oracle et le coût :
compatible avec la raison de N-058, mais c'est un critère de composition à l'exécution que N-058 ne prévoit pas : **nœud**.
N-045 (1) : règle écrite à la main, base de comparaison pour une composition apprise plus tard ; (3) mesure de la nécessité de la
frontière ; (4) le bon marché d'abord. N-044 (2) : règle de budget interne à une course, non une re-conception.

## 4. Récapitulatif et témoin commun

| idée | attendu | pire aux plafonds du pilote | pire au plafond de 0,75 pour Pr-1 |
|---|---|---|---|
| (i) | 17,00 | 123,00 | 48,00 |
| (ii) | 63,30 | 483,00 | 183,00 |
| (iii) | 63,30 | 243,00 | 168,00 |
| (iv) | 30,30 | 243,00 | 93,00 |
| (v) | 73,30 | 183,00 | 158,00 |
| **ensemble** | **247,20** | **1 275,00** | **650,00** |

**Témoin commun** (si les essais partagent les mêmes 20 mondes, la même archive {K1} et la même génération 1) : les appels de la
course (v) servent de bras « sans table » à (i) (20 appels de Pr-1), de bras standard à (iii) (20 appels de Pr-2) et de première
génération du bras standard à (iv) (20 appels de Pr-1) : **26,00 USD attendus et 120,00 au pire épargnés** (ensemble : 221,20
attendus). Prix : les conclusions des essais deviennent dépendantes (mêmes mondes, même témoin) ; à dire dans chaque texte.
**Plafond de 0,75** : abaisser le plafond de session de Pr-1 réduit le pire, mais un appel coupé à son plafond est un échec
(données perdues) ; le pilote dira si 0,75 suffit ; décision de la mère après le pilote.

## 5. Ce qui se prépare sur processeur seul (sans GO, sans dépense)

1. Générateur du monde jumeau et contrôle des marges ; constructeur de la table ((i)).
2. Harnais des sessions en série, réserve de cartes d'un autre monde ((ii)).
3. Filtre de Jaccard, extraction des ensembles de l'archive, mesure d'exécution ((iii)).
4. Chaîne à demi-générations avec test de mort mécanique et garde d'égalité de dollars ((iv)).
5. Regroupement « carte contre archive » et **rejeu de la règle sur les traces de v67** ((v)) : c'est le seul de ces travaux qui
   produise une mesure (budget épargné) sans aucune dépense ; il se préenregistre comme un essai.
6. Pour tous : essais (R5, cas sain et artefact), banc de mutations, essai à blanc avec proposeurs scriptés, devis recalculés par
   programme, préenregistrement contre-lu et scellé. Outils réutilisés : `monde_riche_v4.py` (`4b165847…`),
   `complements_synthese_v1.py` (`89eb7ba8…`), `monde_riche_outils_v1.py` (`1825b956…`), `mesure_pilote_v4.py` (`676d5f37…`),
   la copie du code de l'organisme `94bfd92` (liste `0153e02d…`).

## 6. Demande de décision (format des consignes du dépôt)

**Décision** : quel essai payant autoriser en premier, après le pilote MR-2. **Enjeu** : 247 USD attendus pour les cinq, 1 275 au
pire aux plafonds actuels ; tous sont des cribles d'un grand effet sur 20 mondes ; trois demandent en plus un mot sur un dessin
neuf. **Options.**
- **(a)** (v) puis (iii) : avantage, ils répondent à QO1 (la frontière est-elle nécessaire, et pour quel rôle ?) et appliquent
  « le bon marché d'abord » (N-045, points 3 et 4) ; (v) fournit en plus le témoin commun ; ≈ 137 USD attendus (avec le témoin
  commun : ≈ 121), 426 au pire (386 avec le témoin commun) ; inconvénient, (v) demande un mot sur une règle de composition à
  l'exécution.
- **(b)** (i) et (iv) : avantage, les deux moins chers (≈ 47 attendus, 366 au pire), tous deux sur un seul proposeur ;
  inconvénient, deux dessins neufs à accepter d'abord, et tous deux dépendent du résultat du pilote sur les conditionnelles.
- **(c)** les cinq : avantage, un seul tour de préparation ; inconvénient, la dépense la plus haute avant tout signal.

**Recommandation** : (a), confiance 0,55. **Défaut** : aucun — une dépense est un nœud sans défaut.

**Lignes de GO proposées, mot pour mot, non inscrites** (plafond = pire cas ; à inscrire par Lazar seulement) :

```
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | Organisme d'idéation, essai (v) « appel des proposeurs chers sur le regroupement » : une génération, 20 mondes MR-2 neufs à graine scellée, quatre proposeurs appelés une fois par monde (plafonds de session 2, 2, 2 et 3 USD), aucun juge, aucun test de mort ; règle et placebo rejoués sur les mêmes appels ; conditions toutes exigées : pilote MR-2 joué et ses coûts mesurés, préenregistrement de l'essai contre-lu et scellé, code et regroupement contre-lus, mondes vérifiés et leurs empreintes inscrites, mot de Lazar sur la règle de composition à l'exécution ; plafond de chaque relais égal à sa part ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 183 USD | 2026-11-30 | Lazar | R-2851 ; cette note |
| GO-AAAA-MM-JJ-NN | AAAA-MM-JJ | calcul | Organisme d'idéation, essai (iii) « deux passes » : une génération, 20 mondes (les mêmes que (v) si le témoin commun est retenu), bras 2 à 4 (et bras 1 si (v) n'est pas joué), proposeurs Pr-2 et Pr-1 de la section 1 (plafonds de session 2 USD) ; mêmes conditions que la ligne (v), sauf le mot sur la règle | 243 USD (203 avec le témoin commun) | 2026-11-30 | Lazar | R-2851 ; cette note |
```

## 7. Nœuds pour Lazar, en une ligne chacun

1. **Dépense** : chaque essai payant, sur devis refait après le pilote ; aucun défaut.
2. **(i)** : une donnée d'épisodes publics dans la vue des proposeurs (dessin neuf).
3. **(ii)** : les cartes brutes des pairs dans la vue (dessin neuf).
4. **(iv)** : calendrier en demi-générations et test de mort mécanique (écart à la chaîne scellée de la boucle réelle).
5. **(v)** : un critère de composition à l'exécution qui n'est ni le juge ni l'oracle (lecture de N-058).
6. Décision de la mère, non de Lazar : plafond de session du proposeur le moins cher (2,00 ou 0,75) ; témoin commun.

## Annexe A — compte de puissance des cribles (processeur seul, sans aucune donnée de course)

Commande exécutée le 15 novembre vers 08:33 UTC (`.venv/bin/python -I -c`, scipy 1.17.1, numpy 2.4.6), recopiée en entier :

```python
from scipy.stats import fisher_exact
import numpy as np
rng=np.random.default_rng(1)
for n in (12,20,24,30):
  for pt,pb in ((0.05,0.4),(0.05,0.3),(0.1,0.4)):
    ok=0
    for _ in range(3000):
        a=rng.binomial(n,pt); b=rng.binomial(n,pb)
        if fisher_exact([[b,n-b],[a,n-a]],alternative='greater')[1]<=0.05: ok+=1
    print('mondes',n,'temoin',pt,'bras',pb,'puissance',round(ok/3000,3))
```

Sortie :

```
mondes 12 temoin 0.05 bras 0.4 puissance 0.55
mondes 12 temoin 0.05 bras 0.3 puissance 0.327
mondes 12 temoin 0.1 bras 0.4 puissance 0.38
mondes 20 temoin 0.05 bras 0.4 puissance 0.804
mondes 20 temoin 0.05 bras 0.3 puissance 0.543
mondes 20 temoin 0.1 bras 0.4 puissance 0.631
mondes 24 temoin 0.05 bras 0.4 puissance 0.886
mondes 24 temoin 0.05 bras 0.3 puissance 0.644
mondes 24 temoin 0.1 bras 0.4 puissance 0.708
mondes 30 temoin 0.05 bras 0.4 puissance 0.937
mondes 30 temoin 0.05 bras 0.3 puissance 0.752
mondes 30 temoin 0.1 bras 0.4 puissance 0.818
```

Lecture : à 20 mondes, un passage de 0,05 à 0,30 n'est vu qu'une fois sur deux ; le préenregistrement de chaque essai refera ce
compte sur ses propres taux de référence (ceux que mesurera le pilote MR-2) et pourra porter le nombre de mondes à 24 ou 30, avec
le devis à l'avenant (≈ + 20 % à + 50 %).

## Citations obligatoires (N-064, N-067)

POPPER (Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b370…`) ; Dwork et al., arXiv 1506.02629 (`dcfbb9aa…`) ; Blum et Hardt, « The Ladder », arXiv 1502.04585 (`957ef473…`) ;
Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ; `351f49d8…`), voisin de la boucle générer-classer-faire évoluer et
des échanges entre agents de l'idée (ii) ; et la liste de `docs/decisions/decision-N-067-v1.md`, section 6, dont CADS (Chen et al.,
arXiv 2610.24597 : contribution incrémentale des proposeurs, cité par N-067 pour N-058, p. 7 ; PDF sur une autre branche, non lu par
moi). Voisins nommés par les fiches, non lus sur PDF par moi : Fork-and-Flush (C5 du catalogue, `ddfb2522…`) et « Scaling Discovery
Requires Forgetting » (C6) pour (ii) et (iv). Aucune revendication n'est faite ici.
