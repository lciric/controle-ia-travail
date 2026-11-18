# Vérification 1 (règle R2) des brouillons 2 du second cycle de la lecture « accumuler les scores de sondes sur l'épisode » : différence avec les brouillons 1, contre les deux rapports de contre-lecture — v1

- **Vérificateur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur (Claude Fable 5.2) ; autre agent que les deux contre-lecteurs des brouillons 1. N'a écrit aucune pièce du second cycle ; ne sera ni analyste, ni développeur, ni lecteur, ni juge. **Déclaré** : même modèle que le contre-lecteur des textes (autre instance) ; le mandat n'exige qu'un autre modèle que le rédacteur.
- **Écrit le** : 2026-11-18, à partir de 19:32 UTC (`date -u`).
- **Mandat** : `docs/notes/reconception-accumulation-cycle-2-v1/mandat-verification-brouillons-2-cycle-2-v1.md`, `f018a763eb8a88d353f7362983fabcdf712c44a82ed38b2d3c00a843e77c1a8e` (vérifié par `controle_ia.scellement verifier` : OK ; `sha256sum` : égal), lu en entier.
- **Pièces** (empreintes recalculées, toutes égales au mandat ; compagnons vérifiés : OK) : préenregistrement brouillon 2 `bc68ba33…` et brouillon 1 `d24913f6…` ; ordre exploratoire brouillon 2 `21fe8ff4…` (et brouillon 1 `6f317917…`) ; devis brouillon 2 `065057f0…` (et brouillon 1 `ec6948d7…`) ; brouillon de décision N-074 brouillon 2 `29b38fc4…` ; points à trancher brouillon 2 `5fccf8c7…` (et brouillon 1 `4da79f0d…`) ; rapports `329a94f7…` et `75c9f7da…` ; verdict du premier cycle `c78e35b5…` ; scripts et sorties d'arithmétique v1 et v2 ; script de fabrication `accumulation-cycle-2-v1-brouillon2-faire-v1.py` (compagnon OK).

---

## 1. Verdicts

| pièce | verdict |
|---|---|
| Préenregistrement de la confirmation unique, brouillon 2 | **après ces couples exacts** (P-1 à P-6 ; deux majeurs, quatre mineurs) |
| Ordre exploratoire du temps 1, brouillon 2 | **après ces couples exacts** (O-1, O-2 ; mineurs) |
| Devis, brouillon 2 | **bon pour être soumis à Lazar** (une remarque mineure, non bloquante : D-1) |
| Brouillon de décision N-074, brouillon 2 | **bon pour être soumis à Lazar** |
| Points à trancher, brouillon 2 | **après ces couples exacts** (T-1 à T-4) |

En une phrase : la différence est fidèle aux deux rapports, fabriquée exactement comme déclaré, sans changement hors des remarques ; la conséquence que le rédacteur a tirée seul du troisième bloquant est **cohérente et sans échappatoire vers une issue positive**, mais sa règle est énoncée trop fort pour le compte du signal nul et sa réserve ne vise pas toutes les phrases qu'elle concerne ; l'ordre des opérations est exécutable, à deux précisions près.

---

## 2. Rejeux

1. **Fabrication du brouillon 2** : le brouillon 1 copié dans un dossier à moi (`/tmp/verif-acc2-b2/prereg/`), le script lancé par `python -I` depuis ce dossier : « 60 changements » ; sortie `bc68ba33edece126c7d4b43dede5c6fda31fdb3d4885ef58b9cacb2ab8f48d65`, **identique à l'octet** au brouillon 2 du dépôt (`cmp` sans écart). Le script vérifie lui-même l'empreinte du brouillon 1 et l'unicité de chaque motif remplacé.
2. **Arithmétique v2** : `calculs-redaction-cycle-2-v2.py` rejoué par `python -I` dans le même dossier : sortie **identique à l'octet** à `sortie-calculs-redaction-cycle-2-v2.txt`.
3. **Validateur** (`controle_ia.prereg.problemes`) : brouillon 1 → deux problèmes (contre-lecture sans empreintes ; douze marqueurs) ; brouillon 2 → **un seul problème : quatorze marqueurs de gabarit**, exactement ceux de sa table finale (`<<ATTAQUE_SHA256>>`, `<<COMMIT_CODE_ACC2>>`, `<<EPREUVE_DEV_CHEMIN>>`, `<<EPREUVE_DEV_SHA256>>`, `<<N_TACHES>>`, `<<PUISSANCE_SIMULEE_SHA256>>`, `<<RAPPORT_ANALYSTE_SHA256>>`, `<<RECETTE_FAMILLE_CHEMIN>>`, `<<RECETTE_FAMILLE_SHA256>>`, `<<SONDES_GELEES_CHEMIN>>`, `<<SONDES_GELEES_SHA256>>`, `<<SONDE_PRINCIPALE_NOM>>`, `<<TACHES_CHEMIN>>`, `<<TACHES_SHA256>>`) ; la section « Contre-lecture » porte maintenant ses deux empreintes.
4. **Chiffres recopiés** : chaque nombre du devis (sections 1, 4, 5, 6, 7, 9), de la décision (section 4, « Pourquoi 300 épisodes ») et des points à trancher (points 1, 4, 5, 8 ; sections C et D) recoupé contre la sortie v2 : égaux aux arrondis près, sauf D-1. Les deux phrases de la décision sur le premier cycle (section 1) recoupées sur le verdict, § 3.4 à § 3.7 : **justes**.

---

## 3. Premier point du mandat : la conséquence tirée seule du troisième bloquant

**Ce qui a changé entre les brouillons, à l'épreuve de la famille** (le brouillon 1 fermait la lecture sur tout échec ; le brouillon 2 distingue) :

| signal | brouillon 1 (tout échec fermant) | brouillon 2 |
|---|---|---|
| propre et dense, à 0,70 | jamais « gain non propre », « rien de propre » ni « le maximum bat » ; reconnu dans quatre tirages sur cinq | **fermant** : aucun « le maximum bat » ; **non fermant** : moins de quatre sur cinq → l'issue nulle n'est pas prononcée, réserve écrite |
| jumeau à décalage commun | état ni « accumuler, propre » ni « propre » | **fermant** : état identique, tirage par tirage, au même tirage sans décalage (invariance) |
| jumeau à différence quelconque | au plus 5 sur 100 | au plus 9 sur 100, **non fermant** : réserve « sonde alignée » (remarque M3 du rapport des textes, non une conséquence du rédacteur) |
| concentré, faible amplitude | jamais « accumuler, propre » | **rapporté** |
| concentré, forte amplitude | « le maximum bat » exigé | **fermant** : aucun « accumuler, propre » ; part de « le maximum bat » écrite |
| nul | au plus 9 et 9 sur 200 | inchangé, **fermant** |

**Avis.**
1. **Cohérent dans son principe.** Puisqu'un échec perd la famille (bloquant B3), fermer la lecture sur un événement qu'une chaîne juste produit par malchance ferait perdre des familles sans raison. Chaque garde reste attachée à l'issue qu'elle protège : les gardes contre une **fausse issue positive** (signal nul, concentré fort contre « accumuler, propre », invariance du décalage commun) restent fermantes ; la garde contre une **fausse issue nulle** (signal propre et dense non reconnu) retire l'issue nulle au lieu de fermer. **Aucune échappatoire vers une issue positive (R3)** : aucun chemin ne rend « accumuler, propre » plus facile à obtenir qu'au brouillon 1, hors du jumeau à différence quelconque, dont le passage en réserve vient de la remarque M3 elle-même.
2. **Le jumeau à décalage commun en invariance : juste et plus fort.** Le décalage étant planté au niveau des scores, identique pour les deux membres, il translate tous les scores d'une direction d'une même constante ; les aires de Mann-Whitney, donc tous les états, sont invariantes en arithmétique exacte. Le critère du brouillon 1 (« ni accumuler, propre, ni propre ») pouvait échouer par malchance si le tirage de base l'était ; l'invariance ne le peut pas et détecte toute erreur de chaîne. Seul risque résiduel : un arrondi en virgule flottante qui crée des ex aequo ; l'épreuve du développement, jouée par le même code avec ce jumeau, le révélerait avant le scellement. Aucun couple exigé.
3. **Le concentré à faible amplitude « rapporté » : juste, et corrige une erreur du brouillon 1.** Pour un décalage faible sur deux actions sur dix, la somme peut légitimement battre le maximum, et le décalage est le long de la sonde : « accumuler, propre » y serait une réponse correcte. Le critère du brouillon 1 pouvait fermer la lecture sur une chaîne juste.
4. **Le concentré à forte amplitude** : « aucun accumuler, propre » reste fermant (pour un décalage de trois écarts types sur deux actions, le maximum domine nettement : ce n'est pas un événement de malchance) ; ne plus exiger « le maximum bat » relâche le contrôle que la chaîne sait produire la réfutation, mais cet échec est une affaire de puissance. Acceptable ; la part est écrite.
5. **Défaut 1 (majeur) : la règle est énoncée trop fort pour le signal nul.** Le texte écrit que « seuls » sont fermants les critères « qu'une chaîne juste ne peut pas manquer par malchance », et range parmi eux le compte du signal nul. Or sa propre arithmétique (§ 3 bis) dit qu'une chaîne juste au niveau annoncé manque ce critère par malchance environ trois fois sur cent par côté si les tirages étaient indépendants, davantage puisqu'ils ne le sont pas (M2). **Garder ce critère fermant est juste** (c'est la garde contre les fausses issues décisives ; le rendre non fermant affaiblirait une garde du brouillon 1, R5) ; mais la phrase doit dire le risque accepté de perdre une famille. Couples P-1 et T-1.
6. **Défaut 2 (majeur, symétrie R4) : la réserve « la chaîne ne reconnaît pas un signal propre planté » ne vise que l'issue nulle.** Si la chaîne ne reconnaît pas un signal propre et dense, elle ne sait pas davantage établir la non-propreté : la phrase « gain non propre » (« pas au-dessus du plancher ») perd alors son sens, comme l'issue nulle. Le texte retire l'issue nulle, mais laisse « gain non propre » sans la réserve (la liste des réserves dit « écrites à côté de la phrase qu'elles visent », sans dire laquelle). Couple P-2.
7. **Garde du brouillon 1 affaiblie sans compensation (R5)** : aucune, sous P-1 et P-2. Le signal propre et dense à 0,70 n'est plus fermant sur les états « gain non propre » et « rien de propre » ; ces états ne sont pas des erreurs de chaîne certaines (ils arrivent si la sonde est alignée sur les directions de forte variance), et leur effet est couvert par le retrait de l'issue nulle et par P-2.

---

## 4. Deuxième point : chaque remarque est-elle traitée ?

**Rapport des textes** (trois bloquants, huit majeurs, treize mineurs, avis sur les douze points) : **tous traités**, dans le préenregistrement ou dans l'ordre exploratoire, chacun à l'endroit que dit la table de traitement ; vérifié dans le texte, remarque par remarque. Les avis de la section 7 sont repris dans les points à trancher, et les recommandations du contre-lecteur y sont nommées comme telles.

**Rapport du devis et de la décision** : C1 à C10 et la réponse sur la copie des activations, traités dans le devis ; D1 à D9 et les mots de Lazar, traités dans la décision ; l'avis B.4 porté côte à côte, non tranché.

**Les dix écarts déclarés (points à trancher, section E) : fidèles à l'intention des remarques**, avec deux précisions :
1. **Entropie du tirage par l'empreinte du texte de la règle** : fidèle (c'est la convention de la règle de sélection d'origine, que cite le rapport du devis). Mais le préenregistrement garde deux voies (« par l'empreinte de ce texte de règle, … ou par une graine écrite dans la recette »), alors que la section E n'en dit qu'une ; et quiconque écrit un texte dont l'empreinte fixe le tirage peut, en principe, retoucher le texte jusqu'à un tirage voulu : son auteur doit être exclu comme l'extracteur. Couple P-6 (mineur).
2. **32 premières tâches à la distillation** : fidèle et meilleur que la proposition du rapport (l'ensemble de distillation ne dépend plus de l'effectif).
3. **Règle d'effectif** : fidèle ; « la plus petite amplitude » lève l'ambiguïté d'un écart non monotone en l'amplitude ; les deux sorties renvoyées à Lazar sont de vrais nœuds.
4. **Issue du bras d'attaque avant le code** si elle ajoute un signal : fidèle au rapport (« strictement avant le scellement ») et cohérent avec l'ordre corrigé par le deuxième bloquant. Ce que devient l'épreuve du développement pour ce signal n'est pas écrit : couple P-5 (mineur).
5. **Traces de la course arrêtée non données à l'analyste** : fidèle (le rapport demandait de le dire) ; mais l'ordre exploratoire laisse « la session mère » en décider autrement, alors que les points à trancher (point 14) le donnent à Lazar et que la session mère ne fixe aucun choix d'analyse : couple O-1.
6. **Condition d'ouverture du temps 1** (deux verdicts, plus la table conjointe et le verdict de la validité de l'adaptateur) : fidèle à la prudence du rapport (mineur 8) et à la note de conception ; laissée à Lazar au point 14, avec un défaut. Mais le calendrier des points à trancher (section C) ne retient que les deux verdicts : couple T-2.
7. **Débit de génération** : fidèle. Le rapport du devis écrit « 65 à 84 » pour 400 tâches et un témoin tout en ne demandant de changer que le haut ; le rédacteur suit la phrase (bas à 62), et retrouve les pires cas du rapport. J'approuve.
8. **Disque** : fidèle (deux calculs côte à côte, deux branches, prix du stockage à vérifier) ; le surcoût de la branche « couche par couche » est un ajout, chiffré hors de la sortie scellée (D-1).
9. **Mode sans témoin possible** : fidèle à D9 ; le rédacteur ajoute la lecture plus dure (« mode non recevable ») et laisse le choix à Lazar, dans la décision (section 2) et au point 3 des points à trancher. Sous la lecture douce, la porte rapporte le mode avec la mention : ce n'est pas une échappatoire cachée.
10. **Option recommandée pour la porte** : les deux avis côte à côte, avec les mêmes confiances ; rien n'est tranché à la place de Lazar.

---

## 5. Troisième point : aucun changement hors des remarques

Les soixante entrées du journal du script se rattachent toutes à une remarque nommée (B1 à B3, M1 à M8, mineurs 1 à 6 et 12, avis sur le point 5 de la section 7) ou sont de tenue déclarée : version, date, mandat, renvois renumérotés aux points à trancher, pièces nouvelles citées, exposition des contre-lecteurs, ponctuation, mots de Lazar transmis (repris de la contre-lecture de la décision). Trois détails nouveaux, couverts par la conséquence déclarée de B3 et sans effet sur une issue : vingt tirages pour le jumeau à décalage commun et pour chaque amplitude du signal concentré ; la phrase « L'épreuve du développement n'entre pas dans cette règle ». Rien d'autre n'a changé : le reste est égal au brouillon 1 à l'octet (vérifié par `diff`). Validateur : seuls les quatorze marqueurs prévus restent.

---

## 6. Quatrième point : le code avant le scellement, ordre exécutable ?

**Oui, sans cercle** : ordre exploratoire scellé → recette (règle et entropie de la famille) → ouverture → temps 1 (candidates, épreuve du développement sur elles, simulation, effectif) → liste des tâches (pour 632 au plus, indépendante de l'effectif) → sondes gelées → sortie de l'épreuve du développement de la principale → issue du bras d'attaque (avant le code s'il ajoute un signal) → code contre-lu qui rejoue l'épreuve sur ses entrées scellées, entropie du code → scellement, commit cité → dépôt daté → feu vert de dépense → création de la famille → validité → épreuve de la famille → lecture. Chaque entropie naît avant ce qu'elle tire ; aucun marqueur n'attend une donnée qui viendrait après le scellement ; le gabarit est suivi.

**Deux trous d'exécution** :
- **la liste des tâches doit précéder le gel, mais son extraction est le poste le plus long** ; si elle n'est pas scellée à la fin du temps 1 (sept jours au plus), la ligne de clôture ne peut pas s'écrire, et rien ne dit ce qui se passe : couples P-4 et O-2 (majeur pour l'exécution, sans effet sur une issue) ;
- **un échec imputé à la sonde après le gel** (au rejeu par le code, après une correction de la chaîne) n'a pas de chemin : le texte permet seulement de « geler une autre sonde avant `SONDES-ACC2` », ligne déjà écrite et jamais réécrite : couple P-3 (mineur).

---

## 7. Cinquième point : les points à trancher

- **Format** : chaque nœud porte décision, enjeu, options avec avantage et inconvénient (quelques options sans avantage écrit, au point 2 (c) et au point 7 : sans gravité), recommandation et confiance, défaut ; mots clairs, les identifiants ne viennent qu'en appui. **Les deux avis côte à côte** là où ils diffèrent (point 3) ; là où un contre-lecteur ne choisit pas, c'est dit (points 4, 5, 8). Rien n'est tranché à la place de Lazar ; huit nœuds sans défaut, six propositions à défaut.
- **Calendrier** : le 22 novembre est sourcé (texte scellé de l'apprentissage des sondes sur la tâche, section « Calendrier », R-2716 : verdict au plus tard le dimanche 22 novembre ; le 22 novembre 2026 est bien un dimanche) ; durées recoupées sur le devis et la sortie v2. **Le 27 novembre n'apparaît dans aucun texte que j'ai pu lire** (mandats, note de conception, brouillons 1, rapports, `CLAUDE.md`) : sa source n'est pas écrite (couple T-3). La « règle qui commande tout » omet deux des quatre conditions d'ouverture que garde l'ordre exploratoire (couple T-2). La durée « deux jours » du code du premier cycle (citée de l'en-tête de son texte scellé) : non vérifiée par moi.
- Point 14 : une phrase dit que les épisodes naturels ne sont décrits qu'aux doses où le texte ne sépare pas ; le préenregistrement les **rapporte** partout et ne les **juge** qu'à ces doses (couple T-4, mineur).

---

## 8. Couples exacts (avant → après)

**Préenregistrement** (`prereg/accumulation-cycle-2-v1-brouillon2.md`)

**P-1 (majeur ; section « Épreuve », paragraphe « Deux passages », dernière phrase).**
- Avant : « **Un critère est dit « fermant » quand son échec à l'épreuve de la famille ferme la lecture** ; seuls le sont ceux qu'une chaîne juste ne peut pas manquer par malchance. »
- Après : « **Un critère est dit « fermant » quand son échec à l'épreuve de la famille ferme la lecture** ; le sont ceux qu'une chaîne juste ne manque pas par malchance ((α) en « le maximum bat », invariance de (α′), (β) forte en « accumuler, propre »), et le compte de (γ), gardé fermant parce qu'il protège contre les fausses issues décisives : une chaîne juste au niveau annoncé le manque par malchance avec une probabilité d'environ 0,03 par côté si les tirages étaient indépendants (arithmétique, version 2, § 3 bis), davantage s'ils ne le sont pas ; ce risque de perdre la famille est accepté et déclaré. »
- Même correction dans la table de traitement, ligne B3. Avant : « seuls restent « fermants » les critères qu'une chaîne juste ne peut pas manquer par malchance ((α) en « le maximum bat », invariance de (α′), (β) forte en « accumuler, propre », compte de (γ)) » → Après : « restent « fermants » les critères qu'une chaîne juste ne manque pas par malchance ((α) en « le maximum bat », invariance de (α′), (β) forte en « accumuler, propre »), et le compte de (γ), qu'elle ne manque que rarement (environ 0,03 par côté, tirages indépendants supposés), gardé fermant parce qu'il protège contre les fausses issues décisives ».

**P-2 (majeur ; « Critères de lecture gelés », réserves, dernière ligne).**
- Avant : « - **réserve « la chaîne ne reconnaît pas un signal propre planté »** : écrite si le signal (α) est reconnu dans moins de quatre tirages sur cinq à l'épreuve de la famille ; l'issue nulle n'est alors pas prononcée. »
- Après : « - **réserve « la chaîne ne reconnaît pas un signal propre planté »** : écrite, avec la part observée, à côté de **toute** phrase du cycle si le signal (α) est reconnu dans moins de quatre tirages sur cinq à l'épreuve de la famille ; l'issue nulle n'est alors pas prononcée, et une issue « gain non propre » ou « non concluant » se lit « propreté non établie par une chaîne qui ne reconnaît pas un signal propre planté », jamais « le signal n'est pas propre ». »

**P-3 (mineur ; « Épreuve », alinéa « Échec de (D) »).**
- Avant : « s'il est imputé à la sonde ((α) sous un tirage sur deux, (α″)), l'analyste peut geler une autre sonde avant `SONDES-ACC2`. »
- Après : « s'il est imputé à la sonde ((α) sous un tirage sur deux, (α″)), l'analyste peut geler une autre sonde avant `SONDES-ACC2` ; si l'épreuve de la principale gelée échoue pour ce motif après `SONDES-ACC2` (au rejeu par le code, après une correction de la chaîne), le scellement est impossible et c'est un nœud de Lazar : rouvrir le temps 1 sous une ligne neuve, l'épreuve rejouée sur des tirages neufs, ou clore le cycle sans lecture, compté et rapporté. »

**P-4 (majeur pour l'exécution ; « Plan d'analyse », point 2).**
- Avant : « **Deux lignes se placent à part** : la liste des tâches (`TACHES-ACC2`), après `RECETTE-FAMILLE-ACC2` et strictement avant `SONDES-ACC2` ; »
- Après : « **Deux lignes se placent à part** : la liste des tâches (`TACHES-ACC2`), après `RECETTE-FAMILLE-ACC2` et strictement avant `SONDES-ACC2` — si elle manque quand l'analyste a fini, ses sorties sont scellées à leur écriture, plus rien n'y change, et la ligne `SONDES-ACC2` attend `TACHES-ACC2` ; »

**P-5 (mineur ; « Validation hors de la session », bras d'attaque).**
- Avant : « ce signal entre à l'épreuve plantée par un brouillon neuf de ce texte, contre-lu ; »
- Après : « ce signal entre aux deux passages de l'épreuve plantée par un brouillon neuf de ce texte, contre-lu, qui écrit son critère et dit s'il est fermant ; l'épreuve du développement est rejouée pour lui avant `CODE-ACC2`, sa sortie versée à côté de la première ; »

**P-6 (mineur ; « Plan d'analyse », point 3).**
- Avant : « dans un texte neuf scellé et contre-lu avant le tirage, identifiants déjà employés par le programme exclus »
- Après : « dans un texte neuf, écrit par une instance qui n'est ni l'analyste ni un auteur de ce texte, scellé et contre-lu avant le tirage, identifiants déjà employés par le programme exclus »
- Et dans les points à trancher, section E, point 1 : avant « l'entropie du tirage vient de l'empreinte du texte de la règle, comme pour le premier tirage » → après « l'entropie du tirage vient de l'empreinte du texte de la règle, comme pour le premier tirage, ou d'une graine écrite dans la recette ».

**Ordre exploratoire** (`…/ordre-exploratoire-temps-1-v1-brouillon2.md`)

**O-1 (mineur ; section 2, lot D).**
- Avant : « (défaut prudent du rédacteur : elles ne sont pas des sorties que cite le registre ; la session mère peut en décider autrement, par écrit) »
- Après : « (défaut prudent du rédacteur : elles ne sont pas des sorties que cite le registre ; Lazar peut en décider autrement, points à trancher, point 14 ; la session mère ne fixe aucun choix d'analyse) »

**O-2 (avec P-4 ; section 8, point 2).**
- Avant : « 2. **Limite de temps** : sept jours après `OUVERTURE-TEMPS1-ACC2`. »
- Après : « 2. **Limite de temps** : sept jours après `OUVERTURE-TEMPS1-ACC2` (elle porte sur le travail de l'analyste ; si la ligne `TACHES-ACC2` manque à cette échéance, ses sorties sont scellées à leur écriture et la ligne `SONDES-ACC2` attend la liste). »
- Et, section 6, premier tiret : avant « l'instance qui conçoit la famille neuve, celle qui extrait ses tâches, et toute instance qui a lu sa recette ou sa liste ; » → après « l'instance qui conçoit la famille neuve, celle qui écrit la règle du tirage de ses tâches, celle qui les extrait, et toute instance qui a lu sa recette ou sa liste ; » (avec P-6).

**Points à trancher** (`…/points-a-trancher-cycle-2-v1-brouillon2.md`)

**T-1 (avec P-1 ; point 11 (ii)).**
- Avant : « J'en ai tiré une conséquence que personne n'a encore relue : seuls les critères qu'une chaîne juste ne peut pas manquer par malchance ferment la lecture ; les autres posent une réserve. »
- Après : « J'en ai tiré une conséquence, relue par un vérificateur neuf : ferment la lecture les critères qu'une chaîne juste ne manque pas par malchance, et le compte du signal nul, qu'elle ne manque que rarement (de l'ordre de trois chances sur cent par côté) et qui garde contre les fausses réussites ; les autres posent une réserve. »

**T-2 (section C, premier paragraphe).**
- Avant : « **La règle qui commande tout** : le temps 1 ne s'ouvre qu'après les deux verdicts scellés — la lecture des sondes (étape B) et l'apprentissage des sondes sur la tâche (étape B bis). »
- Après : « **La règle qui commande tout** : le temps 1 ne s'ouvre qu'après les deux verdicts scellés — la lecture des sondes (étape B) et l'apprentissage des sondes sur la tâche (étape B bis) — et, tant que tu ne réponds pas autrement au point 14, après leur table conjointe et le verdict de la validité de l'adaptateur, dont je ne connais pas l'échéance. »

**T-3 (« En deux lignes »).**
- Avant : « La section C dit ce qui peut exister avant le 27 novembre : »
- Après : « La section C dit ce qui peut exister avant le 27 novembre (échéance dont la session mère écrit ici la source — message ou ligne de registre — : aucun texte lu ne la porte) : »

**T-4 (mineur ; point 14).**
- Avant : « - Les épisodes naturels sont décrits, jamais décisifs, et seulement aux doses où ni le lecteur « mots et coût » ni un lecteur lexical ne sépare. »
- Après : « - Les épisodes naturels sont rapportés à toutes les doses, jamais décisifs, et jugés seulement aux doses où ni le lecteur « mots et coût » ni un lecteur lexical ne sépare. »

**Devis** — remarque non bloquante, **D-1** : section 6, branche de disque (ii), « deux relectures de plus, soit environ 2 à 3 USD et 1,6 à 2,5 h de carte de plus » ne figure pas dans la sortie scellée v2 (je le retrouve : deux fois 0,344 h de passe × 2,3 à 3,7, au prix de 1,0889 à 1,30 USD, soit 1,6 à 2,5 h et 1,7 à 3,3 USD) ; de même « plus de 300 » pour le pire cas avec relance (déduit de la sortie v1, au débit plus favorable). R6 voudrait qu'ils renvoient à une sortie scellée : à ajouter au script à sa prochaine version, sans bloquer la soumission.

---

## 9. Ce que j'ai fait, et lectures hors mandat

- **Lu** : le mandat ; les deux rapports, entiers ; les brouillons 2 du préenregistrement, de l'ordre, du devis, de la décision et des points, entiers ; les différences avec les brouillons 1 du préenregistrement, de l'ordre et du devis (`diff`) ; le script de fabrication (début, fin et fonctions) ; les sorties v2 ; le verdict du premier cycle, lignes 1 à 175 (§ 1 à § 3.7) ; `src/controle_ia/prereg.py`, lignes 1 à 70.
- **Rejoué** : le script de fabrication, l'arithmétique v2 et le validateur, dans `/tmp/verif-acc2-b2/` (supprimé à la fin).
- **Hors mandat, déclaré** : (1) `ls` non récursif du dossier du second cycle et de son sous-dossier de pièces, et de `prereg/`, `prereg/contre-lectures/`, `docs/decisions/` filtrés par motif (noms seulement) ; (2) une recherche de dates (`grep` sur des fichiers nommés, non récursive) dans les mandats, la note de conception, les brouillons, les rapports, `CLAUDE.md`, le verdict et le texte scellé de l'apprentissage des sondes sur la tâche (`prereg/T0.7-etape-B-bis-v1.md`), dont trois lignes ont été affichées (dépense, devis, titre du calendrier) ; (3) une recherche de mots dans les dix premières lignes du texte scellé du sixième barreau, pour vérifier une durée (non trouvée) ; (4) `git status --short` (aucune sortie). Rien ouvert sous `diag/`, `runs/`, `donnees/` ; aucun autre verdict ; aucune branche `calcul/` ou `donnees/` ; aucun registre ; aucun texte sur des organismes discrets.
- Ni commit, ni poussée ; aucun fichier existant modifié ; aucune dépense, aucun modèle chargé, aucun téléchargement. Aucun chiffre de résultat du premier cycle n'est repris dans ce rapport.
