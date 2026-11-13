# Protocole de veille concurrentielle par pièce — v2

- **Écrit** le 13 novembre 2026, commencé à 19:30:30 UTC, achevé à 19:47:34 UTC (heures relevées par `date -u`).
- **Rédacteur** : le même sous-agent que la v1 (Claude Opus 5.5), lancé par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`.
- **Remplace, pour l'exécution, la v1** (`protocole-veille-concurrentielle-v1.md`, `37e335d61cdee751…`), archivée intacte (R12).
- **Corrige la v1 selon sa contre-lecture** (`contre-lecture-protocole-veille-v1.md`, `f76596ca8062e20b…`, R-2574 : « utilisable
  après corrections », 3 bloquants, 13 majeurs, 14 mineurs, 25 couples) **et selon les décisions de Lazar** prises depuis
  (R-2570, R-2571, R-2573). Le sort de chaque couple et de chaque constat (appliqué, ou écarté avec sa raison) est dans
  `journal-corrections-protocole-veille-v2.md`, à côté de ce fichier.
- **Statut** : écrit et scellé **avant toute requête réseau**. Pour l'écrire : aucune requête, aucune dépense, aucune écriture
  git, aucune lecture des chemins interdits (section 10). La mère fait une **vérification courte** de cette v2 (R-2574) avant la
  première requête.
- **Annexes versées et scellées avec elle** : `annexe-a-signatures-retro-v1.py` (règle mécanique des signatures du rétro-test),
  ses sorties `annexe-a-signatures-retro-v1.json` et `annexe-a2-signatures-organisme-v1.json`.

## 0. Cadre

### 0.1 Règles de lecture
1. « Libre » veut dire « non trouvé dans les pièces lues », jamais « trou du champ » (R8). Une zone libre séduisante est vérifiée
   plus durement.
2. Aucun chiffre sur un travail d'autrui sans PDF empreinté et page (R7) ; pour un billet ou une page de site, ligne du rendu texte
   archivé et empreinté (« l. »). Un résumé d'interface, un contexte de citation, une sortie de modèle sont des **pistes**.
3. Les chiffres de ce protocole qui ne viennent pas d'un fichier du dépôt sont marqués **« a priori »** (choisis sans donnée,
   avant toute requête) ou **« hypothèse de volume »** (remplacée par un décompte gratuit avant de passer à l'étape suivante).
4. Le protocole s'applique **deux fois, avec les mêmes règles** : le **rétro-test** (date de coupe t0 = 2026-10-01T00:00:00Z,
   section 8), puis la **veille vivante** (t0 = heure de lancement de la phase 2). Le rétro-test est mené et ses prédictions
   scellées **avant** toute lecture d'un élément du corpus vivant daté après le 30 septembre 2026.
5. **Un seul passage du rétro-test** (section 8.5). Aucun paramètre n'est réglé après la lecture d'un de ses résultats. Un échec
   est rapporté comme tel ; aucune reprise n'est faite pour le faire réussir (R3).
6. Ce protocole ne tranche aucune revendication : une pièce trouvée occupée est un nœud porté à Lazar.

### 0.2 Ce que le protocole produit, au bout de la phase 4
Par pièce : l'équipe la mieux placée, ce qui lui manque, sa fourchette de sortie et sa probabilité, avec leur incertitude ; notre
délai réel jusqu'au premier résultat publiable ; le regret attendu ; une décision parmi **accélérer, tenir, mettre en sommeil,
abandonner**, avec sa stabilité ; le plus petit résultat qui resterait à nous ; l'ordre des travaux et ce qui se mène en
parallèle. Puis des prédictions datées, scellées, relues huit semaines plus tard (section 9). Si le rétro-test échoue, le
classement et les probabilités sont rendus avec la mention **« non validé »** (section 8.5).

### 0.3 Décisions de Lazar qui fixent cette version
- **R-2570** (« 1 (a), 2 (b), 3 non : go ») : **lecteurs = sous-agents Claude** d'autres modèles que le rédacteur, **aucun envoi
  à un autre fournisseur, aucune dépense** ; **pas de collisionneur** ; le réseau de la session est ouvert ; constats de la mère :
  OpenReview exige une **vérification humaine** (« ChallengeRequiredError » : aucun contournement), l'**interface de GitHub**
  répond 403 même avec un jeton, `git ls-remote` d'un dépôt public répond.
- **R-2571 et R-2573** : décisions N-067 à N-070 **retenues** (`docs/decisions/decision-N-067-v1.md` à `-070-v1.md`) ; les pièces
  de la veille vivante s'y prennent ; HC4 se lit pour des sondes entraînées qui lisent l'intention ou l'action de l'agent
  auteur, à taux de faux positifs fixé (N-068, point 8a) ; statuts les plus durs de O9, O10, O13, O19 (N-067, point 5a).
- **Message de la mère** (après R-2574) : exigences B1, M1, B3, M3, M4, M6, M2, M5, M7, B2 et autres, reprises ici.

### 0.4 Fichiers lus pour écrire cette version (empreintes contrôlées le 13 novembre 2026 contre leurs compagnons)
| fichier | empreinte | usage |
|---|---|---|
| `protocole-veille-concurrentielle-v1.md` ; `contre-lecture-protocole-veille-v1.md` (ce dossier) | `37e335d6…` ; `f76596ca…` | version corrigée ; corrections |
| `docs/programme-controle-ia-v2.md` ; `docs/etat-de-l-art-controle-ia-v1.md` | `2fd63bad…` ; `a7d6846d…` (empreintes de lancement) | **seules sources des signatures du rétro-test** ; ancrages |
| `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` ; sa contre-lecture | `e30a013d…` ; `f1580ddc…` | liste de référence ; pièces à lire |
| `docs/decisions/decision-N-067-v1.md` … `-070-v1.md` (retenues) | `966dd9dc…`, `ba6b2db3…`, `6e0d9d40…`, `7c4ce221…` | pièces vivantes ; dates de la liste |
| `docs/decisions/decision-N-013-v1.md` ; `…N-007-N-008-v1.md` ; `…N-003-N-004-v1.md` ; `…N-064-v1.md` ; `…N-065-v1.md` | `157d388e…` ; `ab7dc9bb…` ; (lu pour sa date) ; `387c9d4e…` ; `f820e90d…` | énoncés vivants ; dates des premières décisions |
| `docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md` | `08a3738a…` | table O1 à O20 (l. 257 à 276), résultat « à part » |
| `registres/decisions.md` (registre vivant) : R-2551 (l. 2510, « Veille, article signalé par Lazar »), R-2562 (l. 2521, « Mots directs de Lazar … ; ce pourrait être »), R-2563 (l. 2522, « go les deux demandes »), R-2567 (l. 2526, « Contre-lecture de la synthèse finale »), R-2570 (l. 2529, « 1 (a), 2 (b), 3 non »), R-2571 (l. 2530), R-2573 (l. 2532, « Décisions N-067 à N-070 RETENUES »), R-2574 (l. 2533) | non scellé | mandat, décisions, dates |
| `CLAUDE.md` | non scellé | délai de G0 (N-027) |
Aucun fichier de `registres/` autre que `registres/decisions.md` n'a été ouvert ni listé pour écrire cette version.

---

## 1. Pièces à couvrir, découpées en éléments (point a)

### 1.1 Les sept axes et leur vocabulaire fermé
Le vocabulaire ne sort pas de la session (section 4.4) : les lecteurs sont des sous-agents Claude.

| axe | codes |
|---|---|
| **OS — objet surveillé** | OS1 agent qui agit ; OS2 agent **auteur** d'un contenu destiné au moniteur ; OS3 agent **victime** (agit sous un contenu écrit par un tiers) ; OS4 modèle **lecteur** d'un contenu ; OS5 moniteur ou juge génératif ; OS6 plusieurs copies d'un même modèle ; OS7 plusieurs agents de modèles différents ; OS8 chaîne de délégation ; OS9 juge **statistique** de recherche automatisée ; OS10 juge **génératif** de recherche automatisée ; OS11 proposeur d'hypothèses ; OS0 autre |
| **TA — type d'accès** | TA1 boîte noire, actions et sorties ; TA2 boîte noire avec raisonnement visible ; TA3 boîte blanche en lecture (activations, sondes, états cachés, lentilles) ; TA4 boîte blanche en écriture ; TA5 statistique calculée hors des agents par un code de confiance ; TA6 intervention non spécifique (paraphrase, rééchantillonnage, remise à zéro) ; TA0 sans objet |
| **AC — accumulation** | AC1 par action ou par étape ; AC2 maximum ou pic sur la trajectoire ; AC3 moyenne ; AC4 somme cumulée ou processus e additif ; AC5 autocorrélation ou dépendance temporelle ; AC6 coupe transversale entre agents ; AC7 statistique conjointe temps × agents ; AC8 agrégation sur les jetons d'une seule sortie ; AC0 verdict unique |
| **GA — garantie et mesure** | GA1 aucune ; GA2 seuil réglé sur données, fausses alarmes mesurées ; GA3 garantie conforme ou de type « probablement approximativement correcte » ; GA4 garantie toujours valide ; GA5 durée moyenne avant fausse alarme ; GA6 contrôle des comparaisons multiples ; GA7 engagement scellé par empreinte avant les données ; GA8 nul formé des lois connues ; GA9 borne ou théorème ; **GA10 quantité d'information mesurée (fuite, information mutuelle)** (ajout de la v2, pour H7) |
| **ME — menace** | ME1 sabotage diffus : aucune action prise seule n'est étiquetable ; ME2 sabotage d'agent étiquetable par étape ; ME3 sous-performance volontaire ; ME4 collusion ou coordination ; ME5 attaque par le contenu sur un moniteur ; ME6 injection par un tiers ; ME7 évasion de sonde par consigne ou contexte ; ME8 évasion par écriture dans les activations ou les poids, ou par optimisation ou entraînement ; ME9 proposeur qui optimise contre un juge ; ME10 perte d'une contrainte à la délégation ; ME11 adversaire adaptatif qui répartit un budget ou préserve les marginales ; ME0 aucune |
| **CA — cadre** | CA1 évaluation de contrôle ; CA2 banc d'agents à outils ; CA3 tâches floues à vérité différée ; CA4 pipeline de code à plusieurs rôles ; CA5 recherche automatisée ; CA6 conversation sans outil ; CA7 théorie ou simulation seule ; CA8 garde ou classifieur de production |
| **EC — échelle** | champs chiffrés, chacun avec sa page : plus grand modèle à poids ouverts lu (milliards) ; modèles d'interface ; **valeurs** du nombre d'agents comparées ; **valeurs** de l'horizon comparées ; **nombre de moniteurs** comparés ; nombre d'épisodes |

### 1.2 Règle d'appariement d'un article à une pièce
- Une signature est une **table** (annexes A et B), seule lue par le script : par axe, une ou plusieurs **entrées** ; une entrée
  est un ensemble de codes admis (« \| ») ; les entrées d'un même axe sont exigées **ensemble** (« et »).
- Score d'un axe = part de ses entrées dont au moins un code est présent chez le lecteur. `c` = moyenne des scores des axes
  exigés. Axe d'échelle : une entrée « variable » est présente si l'article compare au moins deux valeurs ; une entrée « ≥ 7
  milliards » si le plus grand modèle ouvert lu atteint ce nombre.
- **Code discriminant** d'une pièce : la première entrée, dans l'ordre des axes ME, TA, AC, GA, OS, CA (règle mécanique).
- Un couple (article, pièce) passe au **jugement par pièce** (section 4.3) si `c ≥ 0,5` chez **l'un ou l'autre** lecteur, **ou**
  si le code discriminant est présent chez l'un d'eux.
- **Mesure de ce que la porte écarte** : 60 articles de l'étage 2 sans aucun couple retenu, tirés au hasard (graine, section
  12.2), sont jugés contre **toutes** les pièces de leur famille la plus proche (famille de leur plus grand `c`). Rendu : part
  jugée au moins « voisin », au moins « occupe en partie ». **Au-delà de 5 % d'« occupe en partie »**, la porte devient
  `c ≥ 0,34` par un addendum scellé, écrit et appliqué avant tout calcul du modèle de la section 5, rapporté comme écart (règle
  fixée ici, non discrétionnaire).
- Chaque lecteur rend en outre une phrase libre « contribution principale » par article, que reçoit le juge de l'échantillon.
- Le jugement par pièce, qui seul fait foi, emploie l'échelle de la synthèse : **occupe**, **occupe en partie** (axes couverts,
  page par page), **voisin**, **ne touche pas**.

### 1.3 Pièces de la veille vivante
Prises dans les décisions retenues N-067 à N-070 et, pour les autres, dans le programme v2 et les décisions N-003 à N-013 ;
**26 pièces**, signatures en table à l'annexe B (au moins trois axes chacune). Si une décision plus récente change un énoncé
avant la phase 2, l'écart est consigné avant toute requête ; s'il change une signature, c'est une v3 de ce protocole.

### 1.4 Pièces du rétro-test : signatures mécaniques, écrites à partir des seuls documents de lancement (B1)
- **Sources** : le seul programme v2 (empreinte de lancement `2fd63bad…`), aux lignes fixées par le script de l'annexe A
  (H1 l. 93, H2 l. 94, L l. 55-56, T l. 62, H6 l. 97, Tr l. 98, H8 l. 99, HC1 à HC6 l. 102 à 108, H3 l. 111, H4′ l. 112, H5 l. 113,
  H7 l. 114, statistique de population l. 208, statistique spatio-temporelle l. 211 et colonne B de la l. 43).
- **Aucune décision n'est datée d'avant le 1er octobre** : les plus anciennes (N-003 à N-008) portent le 4 octobre 2026. Le
  programme v2 et l'état de l'art v1 portent aussi le 4 octobre ; ils sont la version du 14 septembre révisée, et la mère les
  nomme comme sources permises. **Limite déclarée** : trois jours séparent t0 de ces documents ; aucune pièce de la liste de
  référence n'a de première version connue entre le 1er et le 4 octobre (section 8.3).
- **Règle mécanique** (annexe A, script `annexe-a-signatures-retro-v1.py`) : (1) on retire le titre en gras et la parenthèse de
  poids ; (2) on coupe le texte à la première phrase qui contient « Revendicable : », « est déjà décrit » ou « sont publiées » :
  ce qui suit est le **texte « cédé »** du programme, remis tel quel aux juges ; (3) sur le reste, un lexique figé de termes
  français (plus long d'abord) donne les entrées de la signature ; (4) une pièce à **un seul axe** ou moins **sort du
  rétro-test** ; à deux axes, elle reste, marquée « signature pauvre », et passe par son code discriminant.
- **Garde** : le script refuse toute signature, tout texte exigé ou tout texte « cédé » qui contient un identifiant `2609.*`,
  `2610.*` ou `2611.*` ; **testée** sur le cas sain (code 0) et sur un artefact qui ajoute « arXiv 2610.12445 » à la ligne de H1
  (code 1, « garde : identifiant postérieur ») le 13 novembre 2026, dans le bloc-notes de la session.
- **Ce qui a été écrit en connaissant la liste, et déclaré** : le lexique et l'affectation des lignes sont du rédacteur, qui
  connaît la liste de référence ; aucune entrée ne nomme un article ni une équipe. **Un seul changement a suivi le premier
  passage du script** : la règle de coupe prenait « existe » et « établi » pour des marques et coupait à tort H6 (« Il
  existe ») et Tr (« établie au niveau token ») ; les marques ont été réduites aux trois expressions ci-dessus ; le lexique n'a
  pas été touché.
- **Résultat** : **19 pièces au rétro-test principal** ; **A-H6 en sort** (un seul axe dérivable : TA6). Huit pièces y sont à
  deux axes (« signature pauvre ») : A-Tr, A-H8, B-POP, B-H7, C-HC1, C-HC2, C-HC2b, C-HC6. **B-H9 en sort** : H9 est née le
  22 octobre (N-035). **L'organisme en sort** : né le 9 novembre (N-064) ; résultat « à part » en section 8.3.2 (M1).

### 1.5 Valeurs
V vaut 1 pour une pièce revendiquée, 0,3 pour une mesure descriptive, 0,2 pour un instrument non revendiqué (**a priori**).
Lazar peut les remplacer avant la phase 4 ; la section 7.5 rapporte la sensibilité des décisions à V.

---

## 2. Sources brutes et requêtes exactes (point b)

### 2.0 Règles communes
1. **Journal** : chaque requête écrit une ligne dans `brut/journal-requetes-v1.jsonl` (heure UTC, méthode, adresse complète sans
   secret, code de retour, taille, empreinte du corps reçu, chemin du corps archivé) ; scellé à la fin de chaque phase.
2. **Hôtes permis**, et eux seuls (garde testée, R5) : `export.arxiv.org`, `arxiv.org`, `oaipmh.arxiv.org` (variante 2.1
   seulement), `api.semanticscholar.org`, `api.openalex.org`, `www.lesswrong.com`, `www.alignmentforum.org` ; **sur un mot
   de la mère, un premier essai unique chacun (refusé : flux « non observé »)** : `neurips.cc`, `huggingface.co`, `www.aisi.gov.uk`, `far.ai`,
   `redwoodresearch.substack.com`, `www.apolloresearch.ai`, `metr.org`, `alignment.anthropic.com` ; `github.com` **par `git`
   seulement** (section 2.7). **Aucun hôte d'un fournisseur de modèles** : la garde refuse toute requête vers une interface de
   modèle de langue (B2).
3. **En-tête** : agent utilisateur neutre `veille-bibliographique/1.0` ; aucun nom, aucune adresse électronique, aucune donnée
   du programme ; pas de paramètre `mailto`. Risque écrit : les requêtes par auteur et par identifiant disent quelles équipes
   et quelles pièces nous suivons ; information publique, risque faible, accepté.
4. **Cadence** : une seule connexion ; **une requête toutes les 3 secondes, partout** (PDF compris, pris sur
   `export.arxiv.org`). Sur un 429 ou un 503 : attente de 30, 60, 120 puis 240 secondes, puis échec consigné.
5. **Refus** (M13) : un refus (403, vérification humaine) d'un hôte permis arrête **ce flux** : il est consigné **tel quel**,
   rapporté à la mère, le flux est dit « non observé », les autres continuent. Un refus d'un **contrôle de permissions ou d'un
   classifieur** arrête **la phase** (liste d'arrêt). Aucune reformulation, aucun contournement, aucun mandataire.
6. **Dates** : la date d'un article est celle de sa **première version** (`published`) ; les versions suivantes sont datées à
   part (`updated`, page `export.arxiv.org/abs/<identifiant>`).

### 2.1 Interface d'arXiv (métadonnées)
Catégories **principales** : cs.LG, cs.AI, cs.CL, cs.CR, cs.MA, stat.ML. Catégories **complémentaires** (même tri que les
principales, décompte rendu à part, M8) : stat.ME, math.ST, cs.SE, cs.GT, cs.CY, cs.HC, econ.EM, q-fin.ST. Pour chaque
catégorie `C` et chaque tranche de dix jours `[D1, D2]` du 1er septembre 2026 à la date de lancement :
```
https://export.arxiv.org/api/query?search_query=cat:C+AND+submittedDate:[D10000+TO+D22359]&sortBy=submittedDate&sortOrder=ascending&start=S&max_results=500
```
(`D1`, `D2` en `AAAAMMJJ`, suivis sans espace de `0000` et `2359` ; exemple :
`…cat:cs.LG+AND+submittedDate:[202609010000+TO+202609102359]…` ; `S` = 0, 500, 1000, … jusqu'à atteindre `totalResults` ; une
page vide avant ce total est redemandée **une fois**, puis l'écart est consigné.) Contrôle : `published` tombe dans la tranche.
**Veille vivante seulement** (M8) : mêmes requêtes avec `lastUpdatedDate` à la place de `submittedDate`, du 1er octobre à la
date de lancement : un article plus ancien révisé dans cette période passe le préfiltre et l'étage 1 comme les autres, et son
étage 2 lit la dernière version en disant ce que la révision ajoute.
**Variante unique**, si `submittedDate` est refusé ou rend zéro sur une tranche que la liste (2.2) annonce pleine : moissonnage
`https://export.arxiv.org/oai2?verb=ListRecords&set=cs&metadataPrefix=arXiv&from=D1&until=D2` (puis `set=stat`) ; une
redirection n'est suivie que vers `oaipmh.arxiv.org` ; `from` et `until` y filtrent la date de **modification** : on garde
les seuls articles dont la première version tombe dans la tranche ; sinon la variante est dite « non disponible ».
**Par identifiant** : `https://export.arxiv.org/api/query?id_list=ID1,ID2,…&max_results=200`.

### 2.2 Listes d'arXiv (complétude)
Pour chaque catégorie principale `C` et chaque mois `M` ∈ {2026-09, 2026-10, 2026-11} :
`https://arxiv.org/list/C/M?skip=K&show=2000` (`K` = 0, 2000, … jusqu'à épuisement). Total annoncé et identifiants relevés ;
tout identifiant absent de 2.1 est pris par `id_list` ; écart rendu par catégorie et par mois.

### 2.3 Semantic Scholar : citations en aval
**Deux jeux d'ancrages, et les seuils du rétro-test se jugent sans ce flux** (M9) ; le résultat « avec citations » est rendu à
côté, pour chaque jeu.
1. **Jeu de contrôle mécanique**, sans choix : les identifiants d'arXiv cités **au moins deux fois** dans l'ensemble des deux
   documents de lancement (programme v2 et état de l'art v1, comptés par `grep` le 13 novembre 2026), de première version au plus
   tard le 30 septembre 2026, dont `citationCount`, relevé par la première requête, ne dépasse pas 500 (règle fixée, à
   rendre avec les comptes relevés) : 2005.07821, 2208.07610, 2502.03407, 2504.10374, 2506.10805, 2506.14261, 2511.00554,
   2512.03109, 2601.20022, 2604.01151, 2605.15377, 2605.18549, 2605.27690, 2605.27958, 2605.31593, 2606.07054, 2606.07612,
   2606.08892, 2606.10456, 2606.14037, 2607.02514, 2607.07368, 2607.08066, 2608.16190, 2609.03035 (25 identifiants).
2. **Les quinze ancrages choisis**, justifiés par les seuls documents de lancement :

| n° | identifiant | pièce, équipe (telles qu'écrites dans l'état de l'art v1) | pièces couvertes | justification (documents de lancement seulement) |
|---|---|---|---|---|
| 1 | 2512.07810 | Taylor et al. (institut britannique / FAR.AI) | A-H1, A-H8 | équipe nommée par la bascule (programme, § 13) |
| 2 | 2606.08892 | Terekhov et al., « Diffuse AI Control on Fuzzy Tasks » | A-H1, A-H2, A-H6 | base de l'environnement (a) (programme, l. 122) |
| 3 | 2606.10456 | « The Distributed Detectability Band » | A-T, A-L, A-H2 | « antériorité à vérifier en priorité » (programme, l. 66) ; veille (§ 16) |
| 4 | 2512.03109 | E-valuator (Sadhuka et al.) | A-H2, A-L | base séquentielle en boîte noire (programme, § 8.3) |
| 5 | 2609.03035 | Das, Ponde, More, Gupta | A-H8, C-HC2b, B-H7, B-H4′ | la plus citée de l'état de l'art v1 (cinq fois) |
| 6 | 2604.01151 | NARCBench (Rose, Cullen, Kaplowitz, Schroeder de Witt) | B-POP, B-ST, B-H3 | équipe nommée par la bascule ; veille (§ 16) |
| 7 | 2607.07368 | Makins, Angelini, Shams, Phuong | B-H3 | effet de fragmentation ; base de l'environnement (b) |
| 8 | 2608.02698 | Ghanem et Keele | B-POP, A-L | collusion au niveau de la population (état de l'art v1) |
| 9 | 2607.08066 | moniteurs de contrôle déplacés | C-HC1, C-HC5, C-HC6 | porte GC (programme, l. 201) ; veille (§ 16) |
| 10 | 2605.15377 | Koran et al. | C-HC5, B-H5 | ensembles de moniteurs (état de l'art v1) |
| 11 | 2605.27958 | Kumar, « Pressure-Testing Deception Probes » | C-HC2, C-HC2b, A-H8 | sondes sous pression (état de l'art v1) |
| 12 | 2506.14261 | Gupta et Jenner | C-HC4, A-Tr | évasion par apprentissage sur les poids ; choix des agrégations (programme, § 0) |
| 13 | 2606.14037 | Kim et al., plan factoriel à trois intensités | C-HC1, C-HC6 | dose-réponse (état de l'art v1) |
| 14 | 2603.12277 | « Prompt Injection as Role Confusion » | C-HC3 | sondes de rôle contre l'injection (état de l'art v1) |
| 15 | 2502.09858 | POPPER (Huang, Jin, Li, Li, Candès, Leskovec) | organisme | **hors du rétro-test principal** : l'organisme est né le 9 novembre ; N-064 demande la lecture de ses citants |

**Ancrages vivants** (veille vivante seulement) : les collisions de la section 8.3 et 2608.07556, 2609.27051. **En veille
vivante**, le flux des citations emploie l'union des trois listes.
Requêtes, pour chaque ancrage `ID` :
```
https://api.semanticscholar.org/graph/v1/paper/arXiv:ID?fields=paperId,title,authors,publicationDate,externalIds,citationCount
https://api.semanticscholar.org/graph/v1/paper/arXiv:ID/citations?fields=paperId,externalIds,title,abstract,authors,publicationDate,venue,contexts,intents&offset=O&limit=1000
```
Par auteur `A` d'un article retenu à l'étage 2 (section 5) :
`https://api.semanticscholar.org/graph/v1/author/A/papers?fields=title,abstract,publicationDate,externalIds,venue,authors&limit=1000`.
Le contexte de citation oriente la lecture, il ne prouve rien. **Limite** : Semantic Scholar indexe aujourd'hui des citations
qu'il n'avait pas au 1er octobre ; le résultat « avec citations » du rétro-test en est plus complet qu'il ne l'aurait été.

### 2.4 OpenAlex
`https://api.openalex.org/works/doi:10.48550/arXiv.ID`, puis `https://api.openalex.org/works?filter=cites:W&per-page=200&cursor=*`.
Écart de couverture avec Semantic Scholar rendu ; affiliations quand le PDF ne les imprime pas (au rétro-test, seules les
affiliations imprimées dans une version antérieure au 1er octobre comptent).

### 2.5 Soumissions d'ICLR 2027
OpenReview exige une vérification humaine (R-2570) : **aucun contournement**. On fait :
1. **Mandataire arXiv** : `search_query=co:%22ICLR+2027%22`, puis `abs:%22ICLR+2027%22`, paginés ; on garde les six catégories
   principales. Limite : une soumission anonyme absente d'arXiv est invisible.
2. Un **export fait par Lazar depuis son poste** peut être versé plus tard dans `brut/manuel/`, avec empreinte et date ; il entre
   alors en veille vivante seulement, comme **écart déclaré**.
3. Rétro-test : ce flux n'y entre pas.

### 2.6 Acceptés de NeurIPS 2026 (veille vivante seulement, M7)
Dans cet ordre, une requête chacun, on s'arrête au premier qui rend la liste : (1) `https://neurips.cc/virtual/2026/papers.html?filter=titles`
(sur un mot de la mère) ; (2) Semantic Scholar :
`https://api.semanticscholar.org/graph/v1/paper/search/bulk?query=monitor|probe|collusion|sabotage|judge|agent&venue=NeurIPS,Neural Information Processing Systems&year=2026&fields=paperId,externalIds,title,abstract,authors,publicationDate,venue`
(on suit `token` ; zéro résultat est consigné comme tel) ; (3) `co:%22NeurIPS+2026%22`. Les ateliers passent par OpenReview :
non observés.

### 2.7 Dépôts de code rivaux (interface de GitHub refusée)
1. **Sans requête** : adresses `github.com`, `gitlab.com`, `huggingface.co` extraites des champs `comment` et `summary` et du
   texte des PDF de l'étage 2 → indicateur « code annoncé ».
2. **Par `git`, sans l'interface** (R-2570) : pour chaque adresse de dépôt public ainsi relevée, et pour ControlArena (adresse à
   relever dans sa documentation ou l'article qui le présente ; sinon non observé) :
   `git ls-remote --heads --tags <adresse>` ; puis, dans un dossier neuf et vide hors du dépôt, `git init --bare` et
   `git fetch --depth=200 <adresse> +refs/heads/<branche>:refs/heads/<branche>` (refspec explicite, branche par défaut annoncée
   par `ls-remote`) ; on lit seulement `git log --format='%H %cI' <branche>` et les étiquettes. **Rien n'est extrait ni exécuté** ;
   un refus est consigné, le flux est « non observé ».
3. **Hugging Face**, sur un mot de la mère : `https://huggingface.co/api/datasets?search=collusion&limit=100`, puis `sabotage`,
   `monitor`, `probe`, `deception`, `control`.
4. Usage : la cadence des dépôts (validations, étiquettes) est **rapportée**, non employée dans le modèle (effet non mesuré).

### 2.8 Phrases « travaux futurs », avec leur page
Pour chaque article de l'étage 2 : PDF de la dernière version au plus tard le 30 septembre 2026 (rétro-test) ou de la dernière
version (veille vivante), par `https://export.arxiv.org/pdf/IDvK` ; empreinte consignée ; texte page par page
(`pdftotext -layout -f P -l P`). Expressions figées : `future work`, `in future`, `we plan to`, `we leave`, `left for future`,
`next step`, `we intend`, `remains open`, `open question`, `we hope to`, `follow-up`, `ongoing work`, `forthcoming`,
`companion paper`, `will release`, `we will`, et toute phrase des sections dont le titre contient `Limitation`, `Future`,
`Conclusion` ou `Discussion`. Chaque phrase garde sa page.

### 2.9 Billets et sites d'équipes (veille vivante seulement)
- LessWrong et Alignment Forum : `POST https://www.lesswrong.com/graphql` avec
  `{"query":"{ posts(input:{terms:{view:\"new\", after:\"2026-09-01\", before:\"DATE_LANCEMENT\", limit:1000}}) { results { _id title postedAt pageUrl htmlBody user { displayName } } } }"}`,
  puis la même sur `https://www.alignmentforum.org/graphql` ; variante unique : `https://www.alignmentforum.org/feed.xml`.
- Sites des équipes nommées par le programme (§ 13, § 16), sur un mot de la mère : une requête sur la racine de chaque hôte de
  la section 2.0 ; on suit au plus cinq liens du même hôte dont le chemin contient `research`, `blog`, `publications`, `papers`
  ou `posts` ; on garde les entrées datées du 1er septembre au lancement ; sinon « non observé ».
- Ces sources ne se reconstruisent pas au 30 septembre : **aucune n'entre au rétro-test** (m12). Limite écrite dans chaque
  rendu : « équipes qui publient hors d'arXiv et hors de ces sites : non vues ».

### 2.10 Semences forcées et occupants connus (veille vivante seulement)
- **Semences forcées**, versées à l'étage 2 sans passer l'étage 1 : SSRN 6569258 (O-O4 ; par son titre sur Semantic Scholar,
  PDF pris à la main) ; 2504.10374 (A-H6) ; 2607.00415 (C-HC1) ; 2601.04603 (C-HC5) ; 2608.11247 (C-HC6) ; 2609.03035 v2
  (C-HC2, B-POP) ; 2609.00731, 2606.06769, 2607.26642, 2608.20290 (O-O4) ; 2607.06807, 2510.04303 (B-ST) ; 2602.01425 (A-H8) ;
  2607.05545, 2605.03255 (C-HC1) ; et, demandées par la contre-lecture de la synthèse (`f1580ddc…`, section 6) : 1906.08938,
  2605.16140, math/0410072 (A-L) ; 2310.01153, 2102.00630, 1906.09256 (A-T) ; 2605.26047 (A-H6) ; 2603.04069, 2609.19101 (A-Tr) ;
  2610.27577 (A-H8) ; 2610.37849 (C-HC2b) ; 2110.00115, 2103.08402, 2610.07627, 2610.00314 (O-O4) ; les pièces du lot 4-B
  (O-R1), quand leur liste est versée.
- **Occupants connus** : toute pièce d'arXiv citée par la synthèse de niveau 3 entre à l'étage 2 du corpus vivant, marquée
  « connue », pour que l'équipe la mieux placée soit calculée avec elle.
- **Rien de cette section n'entre au rétro-test.**

---

## 3. Tri à deux étages, avec décomptes (point c)

### 3.1 Dédoublonnage et préfiltre lexical (gratuits)
- Dédoublonnage par identifiant d'arXiv, puis de Semantic Scholar, puis par titre normalisé.
- **Garde de date** (M7) : au rétro-test, tout article dont la **première version** (`published`) est postérieure au
  30 septembre 2026 fait **échouer** la construction du corpus (pas de filtrage silencieux) ; pour tout article révisé après
  le 30 septembre, titre et résumé sont pris sur `export.arxiv.org/abs/<identifiant>v<K>` (dernière version antérieure au
  1er octobre) et le champ `comment` est vidé. Pour une citation de Semantic Scholar : date d'arXiv, sinon `publicationDate` ;
  sans date, exclue. Garde testée sur un corpus sain et sur un corpus piégé (R5).
- **Préfiltre** sur titre et résumé, insensible à la casse ; passe si (au moins un terme de L1 **et** un de L2) **ou** un de L3.
  Listes **inchangées depuis la v1** (`protocole-veille-concurrentielle-v1.md`, section 3.1) ; elles ont été écrites par un
  rédacteur qui connaissait la synthèse : leur rappel est donc **mesuré hors de toute liste connue** (section 3.4).
- **Témoins du préfiltre**, avant l'étage 1 : les quinze ancrages, le jeu mécanique et les pièces citées par la synthèse dont la
  première version date d'avant le 1er septembre 2026 ; exigence : rappel ≥ 0,95 ; sinon **un seul** addendum scellé ajoute des
  termes tirés des seuls témoins manqués, avant l'étage 1, rapporté comme écart. Les pièces de la strate 2 (section 8.3) n'y
  entrent jamais.

### 3.2 Étage 1 — titre et résumé
Deux lecteurs (section 4), chacun seul, auteurs, affiliations et dates masqués, dans un ordre tiré au hasard (graine). Critère
remis tel quel, inchangé depuis la v1 (section 3.2 de la v1) : retenir si l'objet, la surveillance ou la menace, ou un résultat
théorique applicable à des agents, sont plausibles ; exclusions listées ; **dans le doute, retenir**. **Retenu si l'un des
deux lecteurs retient.**

### 3.3 Étage 2 — texte
- PDF de la version fixée (2.8) ; corps et pages d'annexe contenant un terme de L1, L2 ou L3, plafonné à 30 000 jetons
  (troncature consignée) ; en-tête d'auteurs, affiliations, remerciements et tampon d'arXiv masqués ; **les marques de page sont
  gardées** après masque et troncature ; masque et marques testés sur dix PDF tirés au hasard (graine) avant usage (m11).
- Chaque lecteur rend : codes des sept axes, une page par code ; une à cinq phrases de résultat avec page ; phrases « travaux
  futurs » codées ; champs d'échelle ; « code annoncé » ; phrase « contribution principale ».
- Porte vers le jugement par pièce : section 1.2.
- **Article retenu à l'étage 2** : au moins « voisin » sur une pièce chez au moins un juge. **Article compté** sur une pièce :
  verdict de consensus ou d'arbitrage « occupe », ou « occupe en partie » avec **au moins la moitié des axes exigés** listés
  comme couverts.

### 3.4 Mesures du rappel hors de nos listes (M5)
1. **Échantillon aveugle des écartés** : 300 articles de septembre écartés par le préfiltre, tirés au hasard (graine), passent
   l'étage 1 mêlés au lot, sans marque ; ceux qu'un lecteur retient vont à l'étage 2. Rendu : part retenue, avec son intervalle
   de Wilson à 95 %. **Au-delà de 2 % (plus de 6 sur 300) jugés au moins « voisin » à l'étage 2, le préfiltre est dit
   insuffisant** (critère C1c).
2. **Attribution** : pour chaque pièce de la strate 2, les termes qui l'ont fait passer ; C1a est rendu une seconde fois sans
   L3 et sans les termes propres à l'organisme et à H9 (`AI scientist`, `hypothesis generation`, `automated hypothesis`,
   `hypothesis validation`, `Goodhart`, `falsification`, `delegation chain`, `constraint drift`, `handoff*`, `delegat*`,
   `subagent*`, `sub-agent*`, `NARCBench`).
3. **Strate 3, mécanique** (liste que nous n'avons pas faite) : après le scellement des prédictions du rétro-test, un sous-agent
   neuf relève dans les bibliographies des PDF des quatre collisions de la strate 1 (section 8.3) tous les identifiants
   d'arXiv `2609.*` des catégories principales ; ceux que les juges, lisant à neuf, tiennent au moins « voisin » d'une pièce du
   rétro-test forment la strate 3 ; on mesure leur passage au préfiltre, à l'étage 1, à l'étage 2 (critère C1b).

### 3.5 Décomptes rendus à chaque étage (gabarit fixé)
Gabarit de la v1 (section 3.4), plus trois lignes : catégories complémentaires ; échantillon aveugle ; échantillon de 60 de la
section 1.2. Deux tableaux : rétro-test et veille vivante ; écarts listes contre interface, refus et troncatures à côté.

---

## 4. Grille de codage et double lecture aveugle (point d)

### 4.1 Les lecteurs : sous-agents Claude seulement (R-2570)
- **Codage par article** (étages 1 et 2) : lecteurs **A et B**, deux modèles différents entre eux et différents du rédacteur
  (Claude Opus 5.5). **Jugement par pièce** : juges **J1 et J2**, deux modèles différents entre eux et du rédacteur ; jamais
  la même instance qu'un lecteur. **Arbitre** : un sous-agent Claude d'un modèle distinct de J1, J2 et du rédacteur ; il tranche
  tout désaccord et refait les lectures d'un lecteur contaminé ; le « juge » des sections 1.2, 3.4 et 7.3 est J1 ou J2.
  Défaut, modèles déjà employés par le dépôt : A = Claude Fable 5.2, B = Claude Fable 5.1, J1 = Claude Fable 5.1,
  J2 = Claude Opus 4.6, arbitre = Claude Fable 5.2 ; toute substitution est consignée.
- **Limite déclarée** : tous les lecteurs sont de la même lignée que le rédacteur ; aucune lecture d'une autre lignée.
- Aucun lecteur n'a écrit ce protocole ni ne le reçoit ; chacun reçoit seulement sa consigne et son lot. Température : non réglée
  par l'outil de lancement des sous-agents ; consignée comme telle. **Un second passage d'un lecteur sur un même lot ne remplace
  jamais le premier** ; les deux sont gardés.

### 4.2 Consignes du codage par article
Vocabulaire de la section 1.1, tel quel ; une page par code, sinon code nul ; « absent » permis ; aucune inférence au-delà du
texte ; sortie JSON fixée. Lots de 25 articles par appel à l'étage 1, un article par appel à l'étage 2.

### 4.3 Consignes du jugement par pièce
Échelle « occupe / occupe en partie / voisin / ne touche pas », axes couverts et pages ; la pièce est donnée par sa signature, sa
forme de résultat et son texte « cédé » (annexe A au rétro-test : le texte du programme seulement ; annexe B en veille vivante).
« Occupe » exige tous les axes exigés et la forme du résultat. Le juge dit aussi si une phrase « travaux futurs » annonce un axe
manquant, avec sa page. **Un appel par article et par juge**, couvrant tous ses couples.

### 4.4 Aveuglement, confidentialité, isolement des juges (B2, M7)
- Lecteurs et juges ignorent auteurs, affiliations, dates, l'avis de l'autre, l'existence du rétro-test et la liste de
  référence.
- **Rien ne sort de la session** : ni nos énoncés, ni le vocabulaire des axes, ni les textes ; aucun appel à un autre
  fournisseur ; aucun collisionneur (R-2570). Garde des hôtes : section 2.0.
- **Isolement** : lecteurs, juges, arbitre et sous-agents de comparaison sont lancés **hors du dépôt** (dossier de travail neuf
  ne contenant que leur consigne et leur lot) et, si l'outil le permet, **sans outil de lecture de fichiers** ; sinon avec
  l'interdiction écrite d'ouvrir tout autre fichier, et **audit de leurs appels d'outil** : toute lecture hors du lot annule leur
  lecture, refaite par l'arbitre, et le rapport le dit.
- **Fin de connaissance** : celle de chaque modèle employé est consignée telle que le fournisseur la déclare (Claude Opus 5.5 :
  juin 2026, selon la consigne système de la session du rédacteur ; les autres à relever). Un modèle dont la fin de
  connaissance est postérieure au 30 septembre 2026 ne lit pas le rétro-test. **Sonde de connaissance par titre**, hors de
  tout lot, sur A, B, J1, J2 et l'arbitre : les titres des quatre collisions de la strate 1 et quatre titres inventés (tirés de
  modèles fixes, graine) ; un modèle qui décrit correctement le résultat d'une collision est **contaminé** pour le rétro-test.

### 4.5 Accord mesuré et règle de désaccord
- Étage 1 : kappa de Cohen sur « retenu », pourcentage d'accord, **accord positif**, nombre de retenus par un seul lecteur.
- Étage 2 : kappa de Cohen et accord positif par code, regroupés par axe ; kappa pondéré (quadratique) sur l'échelle à quatre
  niveaux du jugement par pièce.
- **Seuil** : kappa ≥ 0,6 par axe et pour le jugement par pièce ; en dessous, « accord faible » marqué partout. Chaque désaccord
  de jugement par pièce et chaque désaccord de code qui change `c` d'au moins 0,25 va à l'arbitre ; accords avant et après
  arbitrage rapportés.
- **Témoins des lecteurs** : 20 positifs tirés au hasard (graine) dans le jeu des témoins du préfiltre et 20 négatifs tirés au
  hasard parmi les écartés de septembre (hors échantillon aveugle) ; exigence : au moins 18 positifs retenus et **au plus 5
  négatifs retenus** sur 20, pour chaque lecteur ; sinon une révision de consigne (addendum scellé), un second essai ; nouvel
  échec : lecteur remplacé par l'arbitre, et dit.

---

## 5. Modèle de fourchette de sortie par équipe, refait pour ne pas saturer (point e ; B3)

Tout est calculé par script à partir du corpus d'avant t0. Les constantes sont **a priori**, fixées ici, jamais ajustées.

### 5.1 Fenêtre et événement
- **S** = nombre de semaines **réellement collectées** avant t0 (du 1er septembre à t0 ; 4,29 au rétro-test).
- **Événement** sur une pièce p : un article **compté** sur p (section 3.3), à sa première version (en veille vivante, aussi à une
  révision qui le fait compter, marquée).
- `k_p` = nombre d'articles comptés sur p dans la fenêtre ; famille F(p) ∈ {A, B, C, organisme} ; `k̄_F` = moyenne des `k_p`
  sur les pièces de F.

### 5.2 Bases naïves
- **Base constante** : `f_W` = part des pièces avec `k_p ≥ 1` ; taux commun `h_0 = −ln(1 − f_W) / S` (plancher : `f_W` vaut au
  moins 1/(2 × nombre de pièces)).
- **Base de volume** : `h_vol(p) = (k_p + k̄_F + 0,1) / (2 S)` (moitié pièce, moitié famille ; 0,1 a priori).

### 5.3 Équipes
Deux articles sont de la même équipe s'ils partagent le **dernier auteur**, ou **au moins deux auteurs et un indice de Jaccard
d'au moins 1/3** ; équipes = composantes reliées ; **une équipe de plus de quinze auteurs distincts est scindée par dernier
auteur** ; la taille de chaque équipe citée est rendue. Identité d'un auteur : identifiant de Semantic Scholar, sinon nom
normalisé. Nom : dernier auteur et affiliation la plus fréquente imprimée avant t0. **Équipes candidates** de la famille F :
celles d'un article de la fenêtre jugé au moins « voisin » sur une pièce de F.

### 5.4 Position et ce qui manque
`c(T,p)` = maximum, sur les articles de T, de : 1 si « occupe » ; part des axes exigés couverts si « occupe en partie » ; 0,1 si
« voisin » ; 0 sinon. **Ce qui lui manque** : axes exigés non couverts, et la forme de résultat si elle n'est pas faite.

### 5.5 Taux d'une équipe, borné par la base de volume
- `λ_T = (n_T + 1) / 104` (n_T = premières versions de T dans les 365 jours avant t0, Semantic Scholar, dates ≤ t0) ;
  `π_T = (m_T + 1) / (n_T + 2)` (m_T = celles qui passent le préfiltre sur titre et résumé).
- **Part des équipes nouvelles** de F : `ν_F = (u_F + 1) / (K_F + 2)`, K_F = articles comptés de la fenêtre sur F, u_F = ceux
  dont aucun auteur n'a d'article passant le préfiltre dans les 365 jours précédents (histoires de Semantic Scholar, non le seul
  corpus d'un mois).
- **Poids** `w(T,p) = λ_T π_T (1 + 4 c(T,p)) / Σ_{T′} λ_T′ π_T′ (1 + 4 c(T′,p))`, somme sur les équipes candidates de F : les
  poids somment à 1.
- **Annonce** `a(T,p)` = 2 si une phrase « travaux futurs » de T, page citée, jugée par J1 et J2 (ou l'arbitre), annonce au moins
  un axe manquant de p ; 1 sinon.
- **Taux** : `h(T,p) = h_vol(p) × (1 − ν_F) × w(T,p) × a(T,p)` ; équipes nouvelles, non nommées : `h_nouv(p) = h_vol(p) × ν_F`.
- **Taux de la pièce** : `h_mod(p) = h_vol(p) × [ν_F + (1 − ν_F) Σ_T w(T,p) a(T,p)]`, donc **entre `h_vol(p)` et `2 h_vol(p)`** :
  aucune saturation au-delà du double de la base de volume ; le modèle d'équipe n'ajoute à la base que la répartition entre
  équipes et l'effet des annonces.

### 5.6 Fourchettes, probabilités, incertitude
- Temps de sortie : loi exponentielle de taux h (Weibull de forme 1,5 en sensibilité, section 7.5). Quantiles 10, 50, 90 %, et
  probabilités sur des fenêtres **au plus égales à S** : rétro-test, H seul (5,71 semaines, section 8.1, **extrapolation de
  1,33 fois S, déclarée**) ; veille vivante, 4 et 8 semaines (13 semaines si S ≥ 13).
- **Incertitude** : rééchantillonnage des articles de la fenêtre (2 000 tirages, graine) ; intervalle de 80 % pour chaque
  probabilité de pièce et d'équipe.
- **Équipe la mieux placée** : plus grande probabilité à 8 semaines (au rétro-test, sur H), égalité départagée par c.
- « Sortie » : première version publique d'un article ou d'un billet, non l'acceptation dans une conférence.

---

## 6. Notre délai réel jusqu'au premier résultat publiable

- **Premier résultat publiable** : le plus petit résultat qui resterait à nous (7.3), préenregistré, contre-lu, mesuré, analysé,
  jugé, rédigé en texte d'atelier prêt pour arXiv.
- **Plan restant** : étapes et durées prévues lues dans le programme v2 (§ 10, § 14), le brief v2, `registres/etat.md`,
  `registres/go.md`, `prereg/` et les devis ; chaque étape typée par voie (7.6), dont une voie **« décision de Lazar »** (GO,
  portes, nœuds), dont la durée est mesurée sur les 20 derniers couples « demande → mot de Lazar » identifiables au registre
  des décisions (liste rendue) (m14). Aucune lecture des chemins interdits.
- **Glissement mesuré** : pour chaque jalon daté de nouveau ou atteint qui a une date prévue écrite, `durée réelle / durée
  prévue`. Premier point : phase 0 prévue du 5 octobre au 1er novembre 2026 (programme, l. 178) ; porte G0 « au plus tard fin
  novembre » (N-027, `CLAUDE.md`), **point censuré** (porte non franchie), qui ne vaut que borne basse. Avec moins de cinq
  jalons, le rapport le dit, emploie la plage des points, et **toute décision autre que « tenir » est dite fragile** (7.5).
- **Délai** : `T_n = durée restante prévue × glissement` (log-normale de médiane et d'écart interquartile ceux des rapports).
  Rendu par pièce : quantiles 10, 50, 90 % de T_n et `P(T_n < T_r)`.

---

## 7. Regret attendu, décision par pièce, ordre des travaux (point f ; M11)

### 7.1 Utilité
Pour une pièce p, un tirage ω (`T_r` tiré du taux retenu à la section 8.5, `T_n` de la section 6), et une décision d :
- **tenir** : `U = V × [1(T_n < T_r) + s × 1(T_n ≥ T_r)]` ;
- **accélérer** : même forme avec `0,6 × T_n`, moins `0,4 × W_p × ρ` ;
- **mettre en sommeil** : même forme avec `T_n + 8 semaines`, plus `8 × (W_p / T_n) × ρ_v` ;
- **abandonner** : `U = W_p × ρ_v`.
Où **W** = semaines de travail restantes ; **W_p** = la part de W qui ne sert aucune autre pièce gardée (une étape commune n'est
rendue que si toutes ses pièces sont abandonnées) ; **ρ = Σ V × q / Σ W**, avec `q = E[1(T_n < T_r) + s × 1(T_n ≥ T_r)]` sous
« tenir » (valeur d'une semaine de capacité **au même risque de rival** que les pièces gardées) ; **ρ_v** = ρ si une autre pièce
gardée a une étape prête sur la même voie dans les 8 semaines, sinon 0 (capacité non absorbable) ;
`s = max(0,1 ; 1 − e)`, `e = c* + (1 − c*) × 0,5`, × 1,5 si l'équipe la mieux placée annonce un axe manquant, plafonné à 1. Les
constantes 0,6 ; 0,4 ; 8 ; 0,5 ; 0,1 sont **a priori** et toutes perturbées (7.5).

### 7.2 Regret attendu et classement
`R(d) = E_ω[max_d′ U(d′, ω) − U(d, ω)]`, 20 000 tirages par pièce. Minimiser `R(d)` revient à maximiser l'utilité attendue
(`E[max]` ne dépend pas de d) : le mot « regret » n'ajoute que l'échelle du classement. **Classement par `R(tenir)`**
décroissant. **Décision** : la d qui minimise R(d), sous les décisions permises (annexe B) et la contrainte de capacité (la somme
des `0,4 × W_p` des pièces à accélérer ne dépasse pas la capacité rendue par les sommeils et abandons) ; si elle mord, on
accélère par ordre de `(R(tenir) − R(accélérer)) / (0,4 × W_p)` décroissant.

### 7.3 Le plus petit résultat qui resterait à nous
Le plus petit ensemble d'axes exigés, avec une forme de résultat mesurable, qui n'est couvert par aucun article compté et n'est
annoncé par aucune équipe (phrase à page citée) ; parmi les candidats, celui de plus court délai. Proposé par le script, vérifié
par J1.

### 7.4 Ce que la décision doit à la validation
Si le rétro-test échoue (8.5), le classement et les probabilités sont rendus **« non validés »**, toutes les décisions sont
**fragiles**, donc rendues « tenir » avec la décision calculée à côté.

### 7.5 Sensibilité
200 perturbations (graine) : V × exp(N(0 ; 0,5²)) ; facteur d'accélération uniforme sur [0,4 ; 0,8] ; coût de l'accélération
uniforme sur [0,2 ; 0,8] × W_p × ρ ; durée du sommeil uniforme sur [4 ; 13] semaines ; glissement × uniforme sur [0,75 ; 1,5] ;
le 0,1 de la base de volume × uniforme sur [0,5 ; 2] ; `ν_F` × uniforme sur [0,5 ; 2] (borné à 1) ; le 4 des poids uniforme sur
[1 ; 8] ; le 2 de l'annonce uniforme sur [1 ; 3] ; le 0,5 de `s` uniforme sur [0,25 ; 0,75] et son plancher sur [0 ; 0,3] ; loi
du temps de sortie tirée entre exponentielle et Weibull de forme 1,5. Une décision est **stable** si elle reste la même dans au
moins 80 % des perturbations, sinon **fragile** ; **une décision fragile est rendue « tenir »**, la décision calculée à côté.
Rang de chaque pièce rendu avec son intervalle de 80 %.

### 7.6 Ordre des travaux et parallélisme
Cinq voies : (1) calcul sur processeur graphique, sous GO ; (2) appels de modèles payants, sous GO ; (3) processeur et écriture ;
(4) lecture et veille ; (5) décision de Lazar. Graphe des dépendances tiré du programme (G0 avant G1 ; G1 et GC avant les
papiers A et C ; G2 avant la phase 3) et des registres. Ordonnancement par liste : à chaque pas, l'étape prête qui réduit le plus
le regret par semaine de capacité va à la première voie libre de son type ; une étape à la fois par voie, par défaut. Rendu :
ordre, prochaine étape, voie, dépendances, ce qui court en parallèle.

### 7.7 Forme du rendu (phase 4)
Une ligne par pièce, dans l'ordre de `R(tenir)` : pièce ; équipe la mieux placée et sa taille ; ce qui lui manque ; fourchette
(10, 50, 90 %) et probabilité, avec intervalle de 80 % ; part « équipes nouvelles » ; notre délai (10, 50, 90 %) ;
`P(T_n < T_r)` ; `R(tenir)` ; décision calculée, stabilité, décision rendue ; plus petit résultat à nous ; prochaine étape, voie,
parallèle ; mention « validé » ou « non validé ». Les décisions qui touchent une revendication sont portées à Lazar.

---

## 8. Rétro-test au 1er octobre 2026 (point g)

### 8.0 Hypothèse et prédictions du rédacteur, avant toute requête (m1)
**Hypothèse** : la chaîne, nourrie du seul corpus d'avant le 1er octobre, (i) retrouve les pièces de septembre que nous savons
proches de nos énoncés et ce qui leur ressemble hors de nos listes, (ii) donne aux pièces touchées entre le 1er octobre et le
9 novembre des probabilités plus hautes et de bon niveau, (iii) nomme parmi ses trois premières l'équipe qui a publié.
**Prédictions du rédacteur** (probabilité que chaque critère passe) : C1a 0,5 ; C1b 0,5 ; C1c 0,7 ; C2 0,25 ; C3 0,1 ;
**réussite d'ensemble, environ 0,04**. Le rédacteur attend un **échec**, surtout sur C3 (les quatre équipes publiantes sont
peu ou pas visibles dans un corpus de septembre sans citations), puis sur C2 (19 pièces, faible puissance). Ce protocole ne vise
pas un signe positif (R3) : un échec rendu tel quel est un résultat.

### 8.1 Ce qu'on refait
Toute la chaîne, sections 2 à 5, avec t0 = 2026-10-01T00:00:00Z : interface et listes d'arXiv du 1er au 30 septembre (catégories
principales et complémentaires, même tri) ; citations en aval **rapportées à part** (seuils sans elles) ; PDF de la
dernière version antérieure au 1er octobre ; histoires d'auteurs et affiliations antérieures à t0 ; **19 pièces de l'annexe
A** ; aucune semence, aucun occupant connu, aucun ancrage vivant, aucun billet, aucun site, ni NeurIPS ni ICLR.
**Horizon jugé : H = du 1er octobre au 9 novembre 2026** (dernier jour cherché, R-2567 ; 40 jours, 5,71 semaines).

### 8.2 Gardes contre la fuite d'information
1. Garde de date (3.1), testée.
2. Isolement des lecteurs et des juges, fin de connaissance et sonde par titre (4.4).
3. Aucun geste discrétionnaire de l'opérateur entre la collecte et le scellement des prédictions ; tout geste à la main est
   consigné.
4. Les prédictions du rétro-test (probabilités par pièce et par équipe, avec intervalles) sont **scellées avant** la comparaison,
   faite par un **sous-agent neuf** qui n'a ni conduit la collecte ni écrit les prédictions.
5. Limite résiduelle : le rédacteur et l'opérateur connaissent la liste ; d'où les règles mécaniques, le script, et les
   critères à base de comparaison.

### 8.3 Liste de référence, figée avant toute requête, avec dates et sources (M2)
Une pièce de la liste est une **collision** si la synthèse de niveau 3 (`e30a013d…`) ou R-2551 à R-2553 la donnent comme
occupant, au moins en partie, un élément d'une pièce que rien de daté d'avant le 1er octobre n'occupait déjà. **Règle de
numérotation d'arXiv** : un identifiant `AAMM.NNNNN` est attribué au mois de dépôt de la première version ; elle sert de source
au mois quand le jour n'est pas écrit au dépôt.

#### 8.3.1 Rétro-test principal (papiers A, B, C)
**Strate 1 — collisions dans H (jugent l'annonce).**

| n° | identifiant | première version | source de la date | équipe connue | pièces de l'annexe A touchées |
|---|---|---|---|---|---|
| 1 | 2610.12445 | 8 octobre 2026 | synthèse `e30a013d…`, l. 68 (« version 1 du 8 octobre 2026 ») | FAR.AI (même ligne) | A-H1 |
| 2 | 2611.10620 | 7 novembre 2026 | `decision-N-069-v1.md` (`6e0d9d40…`), l. 90 | Mohsin, Rahman (même ligne) | B-POP, B-ST, A-H8, B-H3 |
| 3 | 2611.02153 | 1er novembre 2026 | `decision-N-069-v1.md`, l. 89 | Molinari, Bettineschi (même ligne) | B-POP, B-ST |
| 4 | 2610.29178 | octobre 2026 | identifiant (jour non écrit au dépôt) | non écrite au dépôt | C-HC5 |

**Pièces touchées dans H : A-H1, A-H8, B-POP, B-ST, B-H3, C-HC5 — 6 sur 19.** Les 13 autres sont « non touchées dans H », au sens
« non trouvées » (R8) ; la seconde lecture (8.7) complète cette issue une fois.
**Blocs** pour les permutations et rééchantillonnages : {B-POP, B-ST, A-H8, B-H3} (articles 2 et 3) ; chaque autre pièce seule.

**Strate 2 — pièces de septembre 2026 (jugent la détection).**

| n° | identifiant | première version | source de la date | pièces de l'annexe A |
|---|---|---|---|---|
| 1 | 2609.19587 | septembre 2026 | identifiant ; « 27 septembre 2026 (PDF) » selon C5, synthèse l. 675 | C-HC3 |
| 2 | 2609.36490 | septembre 2026 | identifiant | B-H5, C-HC4 |
| 3 | 2609.10739 | septembre 2026 | identifiant | A-H8 |

**Vérification datée, une fois** : la première requête de la phase 2 relève par `id_list` la date de première version et les
auteurs de ces sept articles ; un sous-agent neuf complète les tableaux et les scelle (`retro-test/liste-reference-datee-v1.md`)
avant la collecte. **Règles écrites d'avance** : une première version antérieure au 1er septembre fait passer l'article en
strate 2b (information) ; antérieure au 1er octobre, en strate 2 ; postérieure au 9 novembre, hors liste ; une date qui
contredit sa source du dépôt est rapportée et c'est la date d'arXiv qui vaut. Les seuils s'appliquent alors **en proportion**,
arrondie à l'entier supérieur.
**Retirés de la liste de la v1, avec raison** : 2609.17560 (absent de la synthèse, M2) ; toutes les pièces de l'organisme
(section 8.3.2) ; les billets (m12) ; 2609.03035 v2 (venu de la contre-lecture des décisions, non de la synthèse).
**Écartés, jamais comptés** (comme en v1) : 2610.04575 ; 2610.17301 ; 2610.24052 ; 2610.26935 ; 2610.37679, 2611.11172,
2610.18408 ; CADS 2610.24597, Hegazy et al. 2610.06432, 2611.04420, N×N v5 ; versions postérieures de NARCBench, MasDrift, Sun.

#### 8.3.2 Résultat « à part » : l'organisme (M1, information seulement)
Pièces : **toutes** les lignes O1 à O20 de la table d'origine (`note-anteriorite-co-scientist-v1.md`, l. 257 à 276) et le rôle 1
(N-065, l. 15 à 17), **sans tri**, signatures par le même script, avec un supplément de lexique propre à l'organisme (annexe
A.2) ; **7 pièces gardées** (O2, O11, O12, O13, O19, O20, rôle 1), les 14 autres à un axe ou moins. Collisions dans H :
2611.04556 (3 novembre 2026 ; R-2551, `registres/decisions.md` l. 2510) → rôle 1 ; 2611.01449 (CONFIRM ; novembre 2026 par
l'identifiant ; version 2 du 3 novembre, `decision-N-067-v1.md` l. 104) → O2, O12 ; 2611.06607 (4 novembre 2026, l. 108) → O2 ;
2610.38392 (28 octobre 2026, l. 103) → seulement O3, sorti : **sans objet** ; 2611.00643 (novembre 2026 par l'identifiant, jour non
écrit au dépôt ; hors liste s'il est postérieur au 9 novembre, règle de 8.3.1) → O12, rôle 1. Touchées : O2, O12, rôle 1 (3 sur 7). Strate 2 :
2609.27051 (22 septembre 2026, l. 100) → O2, O11 ; 2609.33180 (septembre 2026 par l'identifiant ; version 2 du 29 septembre,
l. 102) → O19, O12 ; 2609.02246 (2 septembre 2026, l. 110) : ses pièces (O1, O10, O17) sont sorties, **sans objet**. Ancrage
POPPER permis ici. Mêmes critères, sans seuil : rendus pour information.

### 8.4 Critères, bases de comparaison et seuils (rétro-test principal ; M3, M4, B3)
Chaque critère a sa base ; aucun ne se passe par construction.
- **C1 — détection.** (a) Les **3** pièces de la strate 2 passent le préfiltre **et** sont retenues à l'étage 1, **et les 3** sont
  jugées au moins « occupe en partie » sur une de leurs pièces (proportion de la v1, 5 sur 7, arrondie à l'entier supérieur) ; rendu aussi sans L3 ni termes propres (3.4).
  (b) **Rappel sur la strate 3** (liste que nous n'avons pas faite) à l'étage 1 **≥ 0,80**, et supérieur d'au moins 0,5 à la
  **base « tri au hasard à volume égal »** (part du corpus de septembre retenue à l'étage 1) ; intervalle de Wilson à 95 %
  rendu ; une strate 3 de moins de 10 articles rend C1b « sans puissance », qui ne passe pas. (c) **Échantillon aveugle des
  écartés** : au plus 6 sur 300 jugés au moins « voisin ». **C1 = (a) et (b) et (c).**
- **C2 — annonce par pièce, en niveaux et en rangs.** Sur les 19 pièces, avec les probabilités du modèle pour H : (a)
  **calibrage d'ensemble** : la moyenne des probabilités est comprise entre la moitié et le double de la fréquence observée
  (6/19 → entre 0,158 et 0,632) ; (b) **score de Brier inférieur à celui de la base constante** (5.2, sans usage de l'issue) ;
  (c) aire sous la courbe avec **valeur de permutation par blocs** (10 000 permutations, graine) **inférieure à 0,10**.
  Rendus à côté : Brier et aire de la **base de volume**, écarts au modèle avec leurs intervalles de 90 % par rééchantillonnage
  des blocs. **C2 = (a) et (b) et (c).**
- **C3 — annonce par équipe.** Pour **au moins 2** des 4 collisions de la strate 1, une équipe qui partage au moins un auteur avec
  l'article figure parmi les **trois premières** équipes (probabilité sur H) de l'une des pièces qu'il touche, **sans** le flux
  des citations, **et** ce nombre est **strictement supérieur** à celui de la base « trois équipes de plus grand `λ_T π_T` » **et**
  à l'espérance sous tirage au hasard de trois équipes candidates (1 000 tirages, graine).
- **Réussite = C1 et C2 et C3.** Rendus sans seuil : tout « avec citations » (pour les quinze ancrages et pour le jeu
  mécanique) ; pièces à au moins trois axes seules ; Brier par pièce ; diagramme de fiabilité.
- **Taux retenu pour les décisions (section 7)** : celui des trois — modèle d'équipe, base de volume, base constante — qui a le
  plus petit score de Brier au rétro-test ; à égalité, le plus simple. Si le modèle ne bat pas la base de volume, le rapport dit
  que le modèle d'équipe n'apporte rien de mesuré.

### 8.5 Un seul passage ; conséquences écrites d'avance (M6)
- Le rétro-test est joué **une fois**. Aucune v3 ni aucun second rétro-test ne vaut validation : leurs pièces de référence
  auraient servi à corriger.
- **Réussite** : la veille vivante emploie le taux retenu (8.4) ; classement et probabilités sont dits « validés au
  rétro-test, sur 19 pièces, puissance faible ».
- **Échec, quel que soit le critère** : l'échec est rapporté tel quel, critère par critère ; la veille vivante est menée et rendue
  avec le même calcul, **classement et probabilités dits « non validés »**, toutes les décisions fragiles donc rendues « tenir »
  (7.4) ; seules les prédictions datées (section 9) jugeront le dispositif hors échantillon. Si C1 échoue, le rendu dit en tête
  que le corpus ou le tri ne voient pas ce qui existe ; nœud porté à Lazar.
- **Base de volume sans pouvoir** (aire inférieure à 0,60 et Brier pas meilleur que la base constante) : dit en tête du rendu.

### 8.6 Audit de symétrie (R4)
Chacun déclenche **le même audit** (dates, versions des résumés, sonde de connaissance, appels d'outil des sous-agents, gestes de
l'opérateur) avant toute acceptation ou tout rejet : aire ≥ 0,95 ; **ou** les 4 collisions annoncées en C3 ; **ou** aire ≤ 0,30 ;
**ou** aucune pièce de la strate 2 retrouvée ; **ou** calibrage hors d'un facteur 4 dans un sens ou dans l'autre.

### 8.7 Seconde lecture de l'issue, une fois
Après la veille vivante, les articles du 1er octobre au 9 novembre qu'elle compte sur une pièce vivante sont rejugés, par des
juges neufs ignorant les prédictions, contre les 19 pièces de l'annexe A ; les pièces ainsi touchées complètent l'issue « touchée
dans H ». Les critères C2 et C3 sont recalculés **sur les prédictions déjà scellées**. Le verdict qui vaut est celui de l'issue
complétée ; les deux verdicts sont rendus. C'est un complément de l'issue, fixé d'avance, non une reprise : aucune autre lecture
ne suit.

---

## 9. Prédictions datées (point h)

- **Forme** : identifiant `PV-AAAAMMJJ-NNN` ; date d'émission UTC ; pièce ; axes visés ; équipe (nom, auteurs, taille) ou
  « équipes nouvelles » ; fenêtre `[émission ; émission + 56 jours]` ; probabilité à deux décimales et son intervalle de 80 % ;
  composantes du taux (5.5) ; taux retenu (8.4) ; mention « validé » ou « non validé ».
- **Quelles prédictions** : toutes les pièces au niveau « au moins une équipe » ; tous les couples (équipe, pièce) de
  probabilité ≥ 0,05 à 8 semaines.
- **Appariement** : réalisée si un article ou un billet dont la première version tombe dans la fenêtre, d'au moins un auteur
  de l'équipe (ou de toute équipe pour une prédiction de pièce), est **compté** sur la pièce par deux juges aveugles (3.3).
- **Scellement** : `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller` ; jamais réécrit (R12).
- **Relecture à émission + 56 jours** par un sous-agent neuf : mêmes requêtes, limitées à la fenêtre ; jugement aveugle ; score
  de Brier contre la base constante et la base de volume émises le même jour ; score logarithmique (probabilités bornées à 0,01
  et 0,99) ; fiabilité par classes (0–0,1 ; 0,1–0,3 ; 0,3–0,6 ; 0,6–1) ; part des équipes nommées réalisées. Scellée, rapportée
  à Lazar avec les décisions qu'elle change. C'est la seule validation hors échantillon du dispositif.

---

## 10. Ce qui ne se fait pas (point i)

1. **Aucun chiffre sans page** (R7).
2. **Aucune lecture de nos chemins interdits**, ni recherche récursive qui les traverse, ni liste de dossier qui affiche leurs
   noms ; les scripts refusent d'ouvrir un chemin qui y correspond (garde testée, R5) : `diag/*/lecture-sondes-t06.json` ; la
   lecture B de 7a ; `donnees/lecture-b-7a-quarantaine-v1` ; `donnees/mesure-unanime-v15-sortie-v1` ; `essai/t06-explo-v3` ;
   tout `diag/` et `runs/` de 7a ou 7b ; l'étiqueteur ; `scripts/extraire_mesures_epreuve_t06_v1.py` ; la branche
   `calcul/p3bis-reel-v2` ; `donnees/bras-attaque*` ; `donnees/mode-tenu-a-l-ecart*` ; `docs/notes/bras-attaque/` ;
   `registres/index-bras-attaque*` ; `anteriorite-bras-informe*` ; la branche `claude/compassionate-meitner-d4ryyk`. Les fichiers
   ouverts sont nommés un par un.
3. **Aucun appel payant, aucun envoi à un autre fournisseur, aucun collisionneur** (R-2570) ; le devis des appels payants est
   **nul** ; tout appel payant futur serait un nœud à part, avec son devis.
4. Aucune valeur de clé lue ni affichée.
5. **Aucun contact** avec une équipe rivale ; aucune publication ; rien de ce travail ne sort du dépôt.
6. **Aucun contournement** d'un refus (OpenReview, interface de GitHub, classifieur, permission) ; aucun code rival exécuté.
7. Le protocole ne tranche aucune revendication.
8. Aucune requête, aucune dépense, aucune écriture git n'ont servi à écrire cette version.

---

## 11. Capacité de la session (en place du devis ; M12)

Aucune dépense en USD. Le coût est la capacité des sous-agents de la session (R-2550 rappelle qu'elle peut s'épuiser).
**Hypothèses de volume**, remplacées par les décomptes gratuits avant chaque étage : après préfiltre, de 1 500 à 15 000 articles
(la contre-lecture juge la borne basse de la v1 trop basse) ; à l'étage 2, de 100 à 600 ; témoins, échantillons (300, 60) et
second essai compris.
| poste | jetons de sous-agents (ordre de grandeur) |
|---|---|
| étage 1 : N1 × 430 × 2 lecteurs | 1,3 à 12,9 millions |
| étage 2, codage : N2 × 20 500 × 2 lecteurs | 4,1 à 24,6 millions |
| jugement par pièce : un appel par article et par juge, texte et pièces | 4 à 30 millions |
| arbitrage (environ un quart), sondes, échantillons | 2 à 15 millions |
| **total, rétro-test et veille vivante** (codages de septembre réemployés, sauf articles révisés) | **environ 10 à 80 millions** |
**Arrêts** : plus de 15 000 articles après préfiltre, ou plus de 600 à l'étage 2, ou plus de 3 000 couples (article, pièce) à
juger : arrêt et rapport à la mère avant de continuer ; au-delà de 3 000 couples, si elle décide de poursuivre, les couples
sont jugés par `c` décroissant et la coupure est rapportée.

---

## 12. Phases, livrables, graines, gardes, liste d'arrêt

### 12.1 Phases
| phase | contenu | livrables (sous `docs/notes/veille-concurrentielle-v1/`) |
|---|---|---|
| 1 | v2 scellée ; vérification courte de la mère | `protocole-veille-concurrentielle-v2.md`, `journal-corrections-protocole-veille-v2.md`, annexes A et A.2 |
| 2 | vérification datée de la liste (8.3) ; collecte (2) ; préfiltre, témoins, décomptes | `retro-test/liste-reference-datee-v1.md`, `brut/journal-requetes-v1.jsonl`, `corpus/corpus-retro-2026-10-01-v1.jsonl`, `corpus/corpus-vivant-AAAAMMJJ-v1.jsonl`, `decomptes-v1.md` |
| 3 | rétro-test : étages 1 et 2, jugement, accord, modèle, prédictions **scellées**, comparaison par un sous-agent neuf | `codage/…-v1.jsonl`, `codage/accord-v1.md`, `retro-test/predictions-retro-v1.md`, `retro-test/resultat-retro-test-v1.md` |
| 4 | veille vivante ; seconde lecture (8.7) ; délai réel ; regret ; décisions ; ordre | `retro-test/seconde-lecture-v1.md`, `equipes/…-v1.json`, `decisions/regret-et-decisions-v1.md` |
| 5 | prédictions datées, scellées | `predictions/predictions-datees-v1.md` |
| 6 | relecture à émission + 56 jours | `predictions/relecture-predictions-v1.md` |
À la fin de la phase 5, les livrables sont réunis dans un zip versionné `livrables/veille-concurrentielle-v1.zip` avec son
empreinte (R12). Scripts sous `scripts/veille_*_v1.py`, essais sous `tests/` ; manifeste de calcul par phase (R9) ; compagnons
`.sha256` (R6) ; commits et poussée par la session mère.

### 12.2 Graines (R9 ; m3)
`SeedSequence(entropie = int(16 premiers caractères hexadécimaux de l'empreinte de cette v2 scellée, base 16))`, puis
`.spawn(12)` ; l'enfant de rang i sert à l'usage i ; dans un usage, `.spawn(n)` dans l'ordre des pièces des annexes, puis des
identifiants croissants :
0 témoins négatifs des lecteurs ; 1 échantillon aveugle de 300 ; 2 échantillon de 60 ; 3 ordre des articles dans les lots de
l'étage 1 ; 4 choix des 20 témoins positifs ; 5 titres inventés de la sonde ; 6 dix PDF du test du masque ; 7 permutations ;
8 rééchantillonnages ; 9 tirages du regret ; 10 perturbations ; 11 tirages d'équipes de la base de C3.

### 12.3 Gardes, chacune testée sur un cas sain et sur un artefact (R5)
Date du rétro-test (3.1) ; identifiants postérieurs dans les signatures (annexe A, déjà testée) ; hôtes permis et hôtes de
modèles interdits (2.0) ; chemins interdits (10) ; masque et marques de page (3.3) ; plafonds de volume (11) ; appels d'outil
des sous-agents (4.4).

### 12.4 Liste d'arrêt (on s'arrête, on consigne, on rapporte tel quel)
Refus d'un contrôle de permissions ou d'un classifieur ; requête vers un hôte non permis ; garde de date déclenchée ; lecteur
contaminé sans remplaçant ; chemin interdit touché ; rappel des témoins < 0,95 après l'addendum ; un plafond de volume de la
section 11 franchi ; écart qui change une signature (1.3).

---

## 13. Ce qui reste ouvert
1. **Valeurs V** (1.5) : défaut appliqué si Lazar ne donne pas les siennes avant la phase 4.
2. **Export d'OpenReview par Lazar** (2.5) : facultatif, plus tard, veille vivante seulement, écart déclaré.
3. **Mot de la mère** pour l'essai unique des hôtes non vérifiés (`neurips.cc`, `huggingface.co`, sites d'équipes) ; à défaut,
   ces flux sont « non observés ».

---

## Annexe A — Signatures mécaniques du rétro-test (sortie de `annexe-a-signatures-retro-v1.py`)
Produites le 13 novembre 2026 par
`python3 -I annexe-a-signatures-retro-v1.py docs/programme-controle-ia-v2.md docs/notes/ideation-organisme-v1/anteriorite-co-scientist-v1/note-anteriorite-co-scientist-v1.md docs/decisions/decision-N-065-v1.md annexe-a2-signatures-organisme-v1.json > annexe-a-signatures-retro-v1.json`
(le script vérifie l'empreinte de lancement du programme et celles des deux autres fichiers). Le lexique est dans le script.

| pièce | lignes du programme v2 | axes | signature (« et » : entrées exigées ensemble ; « \| » : codes admis pour une entrée) | code discriminant | texte « cédé » du programme | statut |
|---|---|---|---|---|---|---|
| A-H1 | 93 | 4 | ME : ME1 ; TA : TA3 et TA1\|TA2 ; GA : GA2\|GA3\|GA4 ; CA : CA3 | ME : ME1 | Revendicable : la mesure spécifique diffus/flou ; le gain blanc-sur-noir en général est établi. | garde |
| A-H2 | 94 | 5 | ME : ME1 ; TA : TA3 ; AC : AC4 ; GA : GA4 ; EC : horizon variable (au moins deux valeurs) | ME : ME1 | Revendicable : l'application aux sondes internes ; le squelette séquentiel boîte noire existe. | garde |
| A-L | 55, 56 | 5 | ME : ME11 et ME1\|ME2 ; TA : TA3 ; AC : AC4 ; GA : GA9 ; OS : OS6\|OS7 | ME : ME11 | — | garde |
| A-T | 62 | 4 | ME : ME11 ; AC : AC5 et AC4 et AC6\|AC7 et AC3 et AC2 ; GA : GA2\|GA3\|GA4 et GA9 ; OS : OS6\|OS7 | ME : ME11 | — | garde |
| A-H6 | 97 | 1 | TA : TA6 | TA : TA6 | — | sort du rétro-test |
| A-Tr | 98 | 2 | ME : ME8\|ME11 ; AC : AC4 et AC1 et AC8 et AC2 | ME : ME8\|ME11 | — | garde, signature pauvre |
| A-H8 | 99 | 2 | ME : ME7\|ME8 ; TA : TA3 | ME : ME7\|ME8 | Le glissement de construit sous pression est déjà décrit ; la prédiction ne l'est pas. | garde, signature pauvre |
| B-POP | 208 | 2 | ME : ME1\|ME4 ; AC : AC6\|AC7 et AC2\|AC4 | ME : ME1\|ME4 | — | garde, signature pauvre |
| B-ST | 211, 43 (colonne B) | 4 | ME : ME4 ; TA : TA3 ; AC : AC7 et AC4 et AC6 ; OS : OS6 et OS1 | ME : ME4 | — | garde |
| B-H3 | 111 | 3 | ME : ME11 ; TA : TA3 et TA1\|TA2 ; EC : nombre d'agents variable (au moins deux valeurs) | ME : ME11 | Les courbes boîte noire sont publiées. | garde |
| B-H4' | 112 | 3 | ME : ME4 ; TA : TA3 ; OS : OS6\|OS7 | ME : ME4 | — | garde |
| B-H5 | 113 | 3 | ME : ME7\|ME8 ; TA : TA3 ; EC : nombre de moniteurs variable (au moins deux valeurs) | ME : ME7\|ME8 | — | garde |
| B-H7 | 114 | 2 | ME : ME11 ; CA : CA1 | ME : ME11 | — | garde, signature pauvre |
| C-HC1 | 102 | 2 | ME : ME5 ; OS : OS5 | ME : ME5 | — | garde, signature pauvre |
| C-HC2 | 103 | 2 | ME : ME5\|ME7 ; TA : TA1\|TA2 et TA3 | ME : ME5\|ME7 | — | garde, signature pauvre |
| C-HC2b | 104 | 2 | ME : ME5 ; TA : TA3 | ME : ME5 | — | garde, signature pauvre |
| C-HC3 | 105 | 4 | ME : ME5 ; TA : TA3 ; OS : OS5 ; CA : CA1 | ME : ME5 | — | garde |
| C-HC4 | 106 | 3 | ME : ME5 ; TA : TA4 et TA3 ; OS : OS5 | ME : ME5 | — | garde |
| C-HC5 | 107 | 3 | ME : ME5 ; TA : TA6 ; OS : OS5\|OS7 | ME : ME5 | — | garde |
| C-HC6 | 108 | 2 | ME : ME5\|ME8 et ME5 ; CA : CA1\|CA8 | ME : ME5\|ME8 | — | garde, signature pauvre |

## Annexe A.2 — Organisme, résultat « à part » (même script, supplément de lexique)

| pièce | source | axes | signature | statut |
|---|---|---|---|---|
| O1 | note l. 257 | 1 | CA : CA5 | hors du résultat à part |
| O2 | note l. 258 | 3 | TA : TA5 ; GA : GA4 ; OS : OS9 | garde |
| O3 | note l. 259 | 1 | GA : GA7 | hors du résultat à part |
| O4 | note l. 260 | 1 | GA : GA8 | hors du résultat à part |
| O5 | note l. 261 | 0 | — | hors du résultat à part |
| O6 | note l. 262 | 0 | — | hors du résultat à part |
| O7 | note l. 263 | 1 | OS : OS7 et OS5 | hors du résultat à part |
| O8 | note l. 264 | 1 | OS : OS7 et OS11 | hors du résultat à part |
| O9 | note l. 265 | 1 | OS : OS6\|OS7 et OS5 | hors du résultat à part |
| O10 | note l. 266 | 1 | GA : GA2 | hors du résultat à part |
| O11 | note l. 267 | 2 | ME : ME9 ; GA : GA7 | garde, signature pauvre |
| O12 | note l. 268 | 2 | ME : ME9 ; OS : OS11 et OS5 | garde, signature pauvre |
| O13 | note l. 269 | 2 | TA : TA5 ; GA : GA7 | garde, signature pauvre |
| O14 | note l. 270 | 0 | — | hors du résultat à part |
| O15 | note l. 271 | 0 | — | hors du résultat à part |
| O16 | note l. 272 | 1 | CA : CA5 | hors du résultat à part |
| O17 | note l. 273 | 1 | GA : GA7 | hors du résultat à part |
| O18 | note l. 274 | 1 | OS : OS10 | hors du résultat à part |
| O19 | note l. 275 | 2 | GA : GA9 ; OS : OS5 | garde, signature pauvre |
| O20 | note l. 276 | 2 | GA : GA2 ; OS : OS5 | garde, signature pauvre |
| rôle 1 | N-065 l. 15-17 | 3 | ME : ME9 ; OS : OS9 et OS10 ; CA : CA5 | garde |

## Annexe B — Signatures de la veille vivante
« et » : entrées exigées ensemble ; « \| » : codes admis pour une entrée ; le code discriminant est la première entrée dans
l'ordre ME, TA, AC, GA, OS, CA. La colonne « échelle » donne les entrées de l'axe EC (« — » : aucune). « Cédé » : ce que les décisions retenues donnent comme publié (ne compte pas).

| pièce | source | signature | échelle | forme du résultat | cédé | V ; décisions permises |
|---|---|---|---|---|---|---|
| A-H1 | programme l. 93 ; synthèse § 2 | ME : ME1 ; TA : TA3 et TA1\|TA2 ; AC : AC2\|AC4 ; GA : GA2 ; CA : CA3 | modèle ouvert lu ≥ 7 milliards | comparaison à fausses alarmes égales et à agrégation égale, sur la trajectoire | gain en général ; gain par étape sur sabotage étiquetable (2610.12445) | 1 ; toutes |
| A-H2 | N-007, l. 28 | ME : ME1 ; TA : TA3 ; AC : AC4 ; GA : GA4 ; OS : OS1 | horizon variable | rappel qui croît avec l'horizon, seuil calibré sans exemple de sabotage | squelette séquentiel en boîte noire ; somme cumulée sur états internes sans garantie | 1 ; toutes |
| A-L | N-003-N-004 ; programme l. 55-56 | ME : ME11 ; TA : TA3 ; AC : AC4 ; GA : GA4 et GA9 | agents ou horizon variables | énoncé adverse à budget total borné et sa mesure sur sondes | cœur statistique classique | 1 ; toutes |
| A-T | N-003-N-004 ; programme l. 62 | ME : ME11 ; TA : TA3 ; AC : AC5 et AC7 ; GA : GA9 | — | théorème (classes « multi-ensemble » et « marginales », rebrassage) et mesure sur activations | contraste en boîte noire pour un agent | 1 ; toutes |
| A-H6 | N-013, l. 78 ; N-015 | ME : ME1\|ME2 ; TA : TA6 ; OS : OS1 ; CA : CA1 | — | succès d'attaque contre utilité honnête selon l'intensité | bruit sur les poids | 1 ; toutes |
| A-Tr | programme l. 98 | ME : ME8 ; TA : TA3 ; AC : AC2\|AC8 et AC4 ; CA : CA1\|CA2 | — | tenue de la robustesse au niveau de l'action et de la trajectoire | — | 1 ; toutes |
| A-H8 | programme l. 99 | ME : ME7\|ME8 ; TA : TA3 ; OS : OS1 | — | prédiction de la robustesse adverse par un construit mesuré d'abord | le socle (ce que lit la sonde décide où elle échoue) | 1 ; toutes |
| B-POP | N-069, § 4, point 1 | ME : ME4 et ME1 ; TA : TA3 ; AC : AC6\|AC7 ; GA : GA2 ; OS : OS6 et OS1 ; CA : CA4 | au moins trois agents ; taille de coalition variable | co-élévation à sonde égale contre le pic, l'agrégation par agent et l'écart entre agents, avec contrôles de construit | score de paire (J-PACT) ; balayages (2611.10620) ; coupe transversale | 1 ; toutes |
| B-ST | N-069, § 4, point 2 | ME : ME11 et ME8 ; TA : TA3 ; AC : AC7 et AC4 et AC6 ; GA : GA4 ; OS : OS6 ; CA : CA4\|CA1 | horizon variable | démonstration de supériorité, à fausses alarmes égales, sous un adversaire entraîné contre elle | squelette en boîte noire ; forme de la grille | 1 ; toutes |
| B-H3 | programme l. 111 | ME : ME4\|ME1 ; TA : TA3 et TA1\|TA2 ; OS : OS6\|OS7 | nombre d'agents variable | deux courbes sécurité(N) à budget total constant | courbes en boîte noire | 1 ; toutes |
| B-H4′ | programme l. 112 | ME : ME4 ; TA : TA3 ; OS : OS6 | — | compromis décorrélation contre coordination, chiffré | — | 1 ; toutes |
| B-H5 | N-013, l. 84 ; R-2567 | ME : ME7\|ME8 ; TA : TA3 | nombre de moniteurs variable | loi de la sécurité selon le nombre de moniteurs, par la diversité effective | matrice de transfert hors et sous attaque ; résultat sur des juges | 1 ; toutes |
| B-H7 | N-013, l. 85 | ME : ME11 ; GA : GA10 ; CA : CA1 | — | prédiction de la pente d'adaptation par la fuite ; politiques de riposte | mécanisme ; comparaison de politiques | 1 ; toutes |
| B-H9 | N-070, § 4 | ME : ME10 ; OS : OS8 ; CA : CA4 | chaînes linéaires de longueur contrôlée | taux conditionnel par rang, force graduée ; moniteur à chaque passation × profondeur | profil de la première perte par rang (MasDrift, tableau 18, p. 23) | 0,3 ; tenir, sommeil, abandon |
| C-HC1 | N-013, l. 20 ; N-005 | ME : ME5 ; TA : TA1\|TA2 ; OS : OS5 ; CA : CA1 | — | destination libre testée contre la cible et la moyenne du corpus, par famille, par régression ; opposition juge contre sonde | forme à destination imposée ; phénomène | 1 ; toutes |
| C-HC2 | N-068, § 4 | ME : ME5\|ME7 ; TA : TA3 et TA1\|TA2 ; AC : AC2 ; OS : OS2 ; CA : CA1 | — | g continu en fonction de l'intensité, plan apparié, comparé au g des juges | absence d'évasion à seuil sur agent victime (MIRAGE) ; plan apparié ; comparaison sous simple avertissement | 1 ; toutes |
| C-HC2b | N-013 ; N-068, point 8b | ME : ME5 ; TA : TA3 ; OS : OS2 | — | le score monte quand l'agent tente de manipuler, contrôlé contre le style | — | 1 ; toutes |
| C-HC3 | N-013, l. 38-40 | ME : ME5 ; TA : TA3 ; OS : OS5 ; CA : CA1 | — | détection chiffrée des ordres en bande ; g résiduel sur juges, nul sur sondes de l'agent auteur | — | 1 ; toutes |
| C-HC4 | N-013, l. 48 ; N-068, point 8a | ME : ME7\|ME8 ; TA : TA3 et TA4 ; OS : OS5 et OS2 ; CA : CA1 | — | coût juge contre sonde par régime d'accès, sondes entraînées lisant l'intention ou l'action de l'agent auteur, faux positifs fixés | déplacement par le contexte seul de sondes de propriété de l'entrée et de lectures non supervisées | 1 ; toutes |
| C-HC5 | N-013, § 4 | ME : ME5 ; TA : TA3 et TA6 ; OS : OS5 et OS1\|OS2 ; CA : CA1 | — | cellules juge ↔ sonde ; quorum de juges et de sondes lisant l'agent ; paraphrase de confiance | matrice entre juges ; quorum avec moteur de règles (2610.29178) | 1 ; toutes |
| C-HC6 | programme l. 108 | ME : ME5\|ME8 ; OS : OS5 ; CA : CA1 | — | prédiction par moniteur de l'effondrement sous attaque optimisée, à partir du g bénin | niveau de l'item (2608.12645) | 1 ; toutes |
| O-O4 | N-067, § 4, points 1-2 | TA : TA5 ; GA : GA8 ; OS : OS9 ; CA : CA5 | — | promotion seulement si la prédiction scellée bat l'archive | TA5, GA4, GA6, GA7 en soi | 1 ; toutes |
| O-O12 | N-067, § 4, point 3 | ME : ME9 ; OS : OS9 et OS11 ; CA : CA5 | — | bras avec et sans verdicts, consigne de tromper, description exacte du juge, mondes tout faux | verdicts servis, mondes négatifs, zéro promotion (CONFIRM) | 1 ; toutes |
| O-R1 | N-065, rôle 1 ; N-067, point 5b | ME : ME9 ; OS : OS9 et OS10 ; CA : CA5 | — | gain continu comparé des deux juges sous la même attaque | la prémisse du bras « juge génératif » (2611.04556 ; 2611.00643) | 1 ; toutes |
| O-O8 | synthèse § 5 ; N-058 | GA : GA2 ; OS : OS11 et OS7 ; CA : CA5 | — | valeur de la diversité des fournisseurs, jugée sur l'oracle du monde planté | — | 1 ; toutes |
| O-INS | N-067, § 4, points 4, 6, 7 | GA : GA7 ; OS : OS9 ; CA : CA5 | — | instruments non revendiqués : tirages semés par l'empreinte ; mémoire sans verdict ; mutations du code du juge ; banc de mutations du scellement | — | 0,2 ; tenir, sommeil, abandon |
