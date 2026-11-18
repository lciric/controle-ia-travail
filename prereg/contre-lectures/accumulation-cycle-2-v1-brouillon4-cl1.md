# Contre-lecture 1 (règle R2) des brouillons 4 du second cycle de la lecture « accumuler les scores de sondes sur l'épisode » — v1

- **Contre-lecteur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Opus 5.5 (`claude-opus-5-5`), autre modèle que le rédacteur (Claude Fable 5.2). N'a écrit aucune pièce du second cycle ; ne sera ni analyste, ni développeur, ni lecteur, ni juge de ce cycle. **Déclaré** : même modèle (autre instance) que les contre-lecteurs et le vérificateur des tours précédents.
- **Écrit le** : 2026-11-18, à partir de 21:25 UTC (`date -u`).
- **Mandat** : tâche transmise par la session mère (contre-lire les brouillons 4 ; vérifier les points (1) à (8) ; écrire les couples qui portent `GO-2026-11-18-58`).
- **Pièces relues** (empreinte recalculée par `sha256sum`, égale à son compagnon `.sha256`, toutes) :

| pièce | empreinte |
|---|---|
| préenregistrement, brouillon 4, `prereg/accumulation-cycle-2-v1-brouillon4.md` | `92e9021f8efd6f1d6d3f7b2e6c82ae388d5e1c00765a93bcdfa250cf50905f60` |
| ordre exploratoire, brouillon 4, `docs/notes/reconception-accumulation-cycle-2-v1/ordre-exploratoire-temps-1-v1-brouillon4.md` | `feb63aa9c1ba10dd63c984dc2d0b6acc4be4f8f62476fee5f6e5029e5ca66fc1` |
| devis, brouillon 3, `…/devis-cycle-2-v1-brouillon3.md` | `e8c83fc14c4aed24a49603fa75db7343c08290b2ec5ca6be35560b36d565f734` |
| note des différences, `…/differences-brouillons-3-vers-4-v1.md` | `d38ec83a08b899d47cf69a4e2208bbffb2d6681bc41e1f9a05b38eccc4900ab9` |
| script de fabrication, `…/pieces-redaction-cycle-2-v1/brouillons4-faire-v1.py` | `7c8f1fcdc72ca9f1874098b29e1904beede1940067b1a8aa7a482fd752e3b739` |
| sources : préenregistrement brouillon 3 ; ordre brouillon 3 ; devis brouillon 2 | `b6ff8208…`, `af4cb7fb…`, `065057f0…` (égales aux empreintes que le script exige) |
| points à trancher, brouillon 3 | `1999a6ded7bfdcdc0f29bc1c940873903dc2a15c5c5a8b9f7ca795f0a15890ac` |
| vérification des brouillons 2, `prereg/contre-lectures/accumulation-cycle-2-v1-brouillon2-verif1.md` (lue **en entier**) | `624939fb4e39bd8ac889a544a43199c55b48e3b7fd49a587763f17201726cc0e` |
| sortie de calcul version 3, `…/pieces-redaction-cycle-2-v1/sortie-calculs-redaction-cycle-2-v3.txt` (§ 9, pour la remarque D-1) | compagnon vérifié : OK |
| brouillon de décision N-074, brouillon 2 (pour vérifier qu'il n'est pas touché) | `29b38fc41ac4585551abe64079a921523a2142096a2b2f1e4d909e2f483543d5`, égal à son compagnon et à la vérification des brouillons 2 |

Choix de Lazar lus : `registres/go.md`, les seules lignes `GO-2026-11-18-56` (point 2) et `GO-2026-11-18-58`.

---

## 1. Verdict

**Scellable après le nœud 3 et ces couples exacts** — dont un bloquant (B-1) qui exige une décision de Lazar, portée dans le texte par un marqueur de gabarit que le validateur refuse tant qu'il n'est pas rempli. Sans B-1, le texte laisserait la définition d'une « issue répliquée » s'écrire **après** la lecture de ce cycle : ce serait choisir une règle de revendication après avoir vu une issue.

En une phrase : la fabrication est exacte à l'octet ; chaque changement se rattache à un choix de Lazar, à la remarque D-1 ou à la tenue ; le nœud 3 reste ouvert sans pente ; rien de la vérification des brouillons 2 n'est perdu ; mais une conséquence du nœud 1 (b) est à corriger (B-1), une autre à resserrer (M-1, M-2), et `GO-2026-11-18-58` n'est pas encore porté (couples G-1 à G-6).

| sévérité | couples |
|---|---|
| bloquant | B-1 |
| majeurs | M-1, M-2, M-3 ; portage de `GO-2026-11-18-58` : G-1 à G-5 |
| mineurs | m-1 à m-6 ; G-6 |

---

## 2. Rejeux

1. **Fabrication** : les trois sources copiées dans un dossier à moi (`…/scratchpad/rejeu/`, mêmes chemins relatifs), le script lancé par `python3 -B` depuis ce dossier. Sortie : préenregistrement 30 changements (lignes retirées 26, ajoutées 29, égales 265) ; ordre 10 (9, 24, 150) ; devis 25 (22, 40, 112) ; note écrite. `cmp` contre le dépôt : **les quatre fichiers identiques à l'octet** (les trois textes et la note des différences). Le script vérifie lui-même l'empreinte de chaque source, l'unicité de chaque motif et refuse d'écraser (R12).
2. **Validateur** (`controle_ia.prereg.problemes`) : brouillon 3 et brouillon 4 → **un seul problème chacun**, les **quatorze** mêmes marqueurs de gabarit (`<<ATTAQUE_SHA256>>`, `<<COMMIT_CODE_ACC2>>`, `<<EPREUVE_DEV_CHEMIN>>`, `<<EPREUVE_DEV_SHA256>>`, `<<N_TACHES>>`, `<<PUISSANCE_SIMULEE_SHA256>>`, `<<RAPPORT_ANALYSTE_SHA256>>`, `<<RECETTE_FAMILLE_CHEMIN>>`, `<<RECETTE_FAMILLE_SHA256>>`, `<<SONDES_GELEES_CHEMIN>>`, `<<SONDES_GELEES_SHA256>>`, `<<SONDE_PRINCIPALE_NOM>>`, `<<TACHES_CHEMIN>>`, `<<TACHES_SHA256>>`). **Le validateur ne voit pas** les deux marqueurs entre crochets `**[NŒUD 3 — OUVERT]**` (deux occurrences) et `**[RÉPLICATION — À ÉCRIRE]**` : il ne cherche que la forme `<<…>>`. D'où B-1 et m-1.
3. **Remarque D-1** : la sortie version 3, § 9, porte bien « 1,6 à 2,5 h de carte ; 1,7 à 3,3 USD » et le pire cas P2 « 324,7 … 474,4 USD » ; les citations du devis (« 325 à 474 », « 1,7 à 3,3 USD ») sont justes. Le devis garde à côté « environ 2 à 3 USD » : arrondi, sans gravité.

---

## 3. Point (1) : chaque changement rattaché, rien d'autre ne change

- **Journal du script, entrée par entrée** : préenregistrement — tenue 9 (version, date, mandat, statut, lectures de registre déclarées, décisions, renvois, points à trancher et note cités, état de contre-lecture) ; nœud 1 (b) 2 ; nœud 2 (a) 3 ; nœuds 4, 5 (a), 8 (a) 1 ; nœud 7 6 ; proposition 11, 6 ; proposition 12, 1 ; conséquences déclarées 3. Ordre — tenue 5 ; proposition 14 ; nœud 4 deux fois ; nœud 6 (b) ; conséquence du nœud 2 (a). Devis — tenue 5 ; nœuds 1, 2, 4, 5, 7, 8 ; propositions 11 et 13 ; vérification D-1. **Chacun se rattache à un choix de `GO-2026-11-18-56`, point 2, ou à D-1, ou à la tenue** ; vérifié contre le texte tranché des points à trancher, point par point (options retenues et leurs inconvénients écrits).
- **Rien d'autre** : le script ne touche que des motifs comptés ; le reste est égal à la source à l'octet (rejeu ci-dessus et `diff` mot à mot du préenregistrement).
- **Vérification des brouillons 2, rien de perdu** : P-1 (deux endroits), P-2, P-3, P-4, P-5, P-6 retrouvés tels quels dans le brouillon 4 ; O-1 (remplacé par sa forme confirmée « confirmé par Lazar : points à trancher, point 14 »), O-2 (deux endroits) dans l'ordre ; T-1, T-2, T-4 et la suite de P-6 dans les points à trancher, brouillon 3 ; T-3 porte la source de la date du 27 novembre ; D-1 dans le devis, brouillon 3. Les avis du § 3 du rapport (cohérence de la conséquence tirée du troisième bloquant ; invariance du jumeau à décalage commun ; concentré faible « rapporté ») sont dans le texte ; les « deux trous d'exécution » du § 6 sont fermés par P-3 et P-4/O-2.
- **Ce que `GO-2026-11-18-58` rend caduc dans des pièces scellées qu'on ne réécrit pas** : la note des différences, § 7, point 7 ; les points à trancher, point 14 et section C (« La règle qui commande tout ») ; la ligne « laissé à confirmer » de l'ordre, section 9. Les brouillons suivants le disent (G-5) ; ces pièces restent telles quelles (R12).

## 4. Point (2) : le nœud 3 reste ouvert, sans pente

- Le préenregistrement nomme le nœud dans son statut et dans ses décisions, et le tient « hors de ce texte » ; aucune phrase, aucun critère, aucune grandeur ne dépend de A ou de C ; la frontière, point 2, ferme toute pièce de la porte de fin de phase 1. L'ordre et le devis le nomment dans leur table, « aucun » changement. Le brouillon de décision N-074, brouillon 2, est inchangé (empreinte ci-dessus). **Aucune pente.**
- Seule tenue à prévoir : le marqueur `**[NŒUD 3 — OUVERT]**` (deux occurrences) échappe au validateur : couple m-1.

## 5. Point (3) : les six conséquences tirées par le rédacteur

| conséquence (note, § 6) | jugement |
|---|---|
| 1. réserve « non répliquée » | **juste** dans son principe ; **à corriger** sur deux points : ce qu'est une « issue positive » (B-1, à porter à Lazar) et ce que dit la réserve après une réplication lue (m-2) |
| 2. ce que la réplication laisse à écrire ; marqueur non écrit | **à corriger, bloquant (B-1)** : le texte place la définition d'une issue répliquée dans un préenregistrement « scellé avant que la seconde famille existe », donc possiblement **après** la lecture de ce cycle ; la recommandation retenue par Lazar disait « l'écrire avant la lecture de ce cycle » (points à trancher, point 1), et la note elle-même écrit « à écrire avant la lecture de ce cycle » (§ 7, point 5) : les deux textes se contredisent. Le marqueur entre crochets n'est pas vu par le validateur. **À porter à Lazar** : la définition touche la revendication. L'arithmétique « au plus K × 0,025² » est juste (borne de la réunion, nul commun, lectures indépendantes, même niveau ; elle rend « sous 2,5 % jusqu'à quarante cycles », comme le point 1) ; c'est une formule, non un chiffre lu : à verser au prochain script de calcul (m-6), sans bloquer |
| 3. mode connu de l'analyste | **juste**, mais **à préciser (M-2)** : le texte écrit aussi « même recette » ; ce qui est connu n'est donc pas « le mode seul », mais le mode et le fait que la recette reprend celle du développement ; ce qui reste fermé est le texte scellé de la recette, sa règle du tirage, son entropie et la liste |
| 4. absence du bras d'attaque devenue un écart | **juste** : le marqueur `<<ATTAQUE_SHA256>>` empêche déjà le scellement sans lui ; la réserve « sans bras d'attaque » reste une garde (R5). Même alignement à faire pour le dépôt daté, que le texte dit encore « facultatif » et « s'il est accordé » (m-3) |
| 5. branches de garde laissées en place (second témoin) | **à corriger (M-1)** : le second témoin est retenu par Lazar ; un repli « à défaut de second témoin » qui s'applique sans mot de Lazar est un repli d'un choix de Lazar sans nœud (R5 : aucun repli silencieux ; symétrie avec la conséquence 4). Garder les branches, mais sous un nœud |
| 6. tables des tours précédents laissées telles quelles | **juste** ; mais la ligne de la section 11 de l'ordre qui « confirme » la condition d'ouverture 3 avec le verdict de la validité de l'adaptateur est désormais fausse (G-5) |

## 6. Point (4) : échappatoires, seuils, règle R3

- **Aucun seuil numérique neuf, aucun seuil choisi après une lecture** dans les brouillons 4 : les plafonds (275 et 75 USD) sont des branches chiffrées avant tout choix ; niveaux, marge, critères de l'épreuve plantée, phrases gelées : inchangés.
- **Une seule règle laissée à écrire après lecture possible** : la définition d'une issue répliquée (B-1). Corrigée par B-1, R3 reste entière.
- **Nœud 6 (b)** (temps 1 sans sonde : cycle rapporté sans lecture) : il ne crée pas de voie vers une issue positive plus facile — il ne peut que supprimer une lecture, se clôt seulement « à une limite », est compté dans K et rapporté. Il permet en principe d'éviter une lecture qui s'annoncerait nulle au développement ; c'est une sélection sur le développement, permise, et visible par le compte des cycles. Rien à corriger ; le rapport de l'analyste dit déjà pourquoi aucune principale n'est gelée (section 7, point 2).
- **Repli « à défaut de second témoin »** : seule autre porte de sortie sans nœud ; M-1 la ferme.
- **`GO-2026-11-18-58`** desserre une condition d'ouverture par choix de Lazar ; les couples G-1 à G-5 le portent sans affaiblir le reste (exclusion de l'analyste gardée et étendue à la transmission de ses sorties ; lot E ouvert seulement sur empreintes recopiées).

## 7. Point (5) : cohérence préenregistrement, ordre, devis

- **Plafonds** : 275 USD (famille) et 75 USD (relecture complémentaire) identiques dans les trois textes ; extraction des tâches à devis dans le préenregistrement et le devis ; bras d'attaque et seconde famille « devis et ligne à part » dans les deux. **Cohérent.**
- **Ordre des opérations** : inchangé ; l'extraction à devis peut retarder `TACHES-ACC2`, ce que P-4 et O-2 couvrent déjà. Le bras d'attaque demande un devis et une ligne avant `ATTAQUE-ACC2`, donc avant le scellement : à prévoir au calendrier (section 9).
- **Relecture complémentaire** : le devis, section 6, compte 1 024 passes « seulement si la pièce du témoin distillé … a été créée » ; avec `GO-2026-11-18-58`, elles dépendent aussi de l'ouverture du lot E (G-6, mineur).
- **Gardes et essais R5** : la réserve neuve de G-3 doit être écrite par le code et éprouvée sur un cas où elle s'applique et un cas où elle ne s'applique pas (G-4) ; la réserve « non répliquée » de même (même couple).
- **Dépôt daté** : préenregistrement « s'il est accordé » et « (facultative) » contre « empreintes seules, geste de Lazar » ailleurs (m-3).

## 8. Point (6) : validateur rejoué

Voir § 2, point 2 : quatorze marqueurs, aucun autre problème ; deux marqueurs entre crochets non vus (B-1, m-1).

---

## 9. Couples exacts (avant → après)

Les « avant » sont copiés du brouillon 4 (ou de l'ordre, brouillon 4) et y figurent **une seule fois**, sauf mention ; vérifié par comptage.

### Bloquant

**B-1 — définition d'une issue répliquée, avant la lecture (préenregistrement, « Suite des cycles » ; et table des marqueurs). À porter à Lazar.**
- Avant : « Cette seconde lecture a son propre préenregistrement, contre-lu et scellé avant que la seconde famille existe, »
- Après : « Cette seconde lecture a son propre préenregistrement, contre-lu et scellé avant que la seconde famille existe (il fixe le mode, la recette et l'effectif de la seconde famille), »
- Avant : « **[RÉPLICATION — À ÉCRIRE]** : ce texte ne fixe pas ce qui compte comme une issue répliquée (le même état du cycle ; aux mêmes doses ou à une dose quelconque), ni le mode, la recette et l'effectif de la seconde famille ; le préenregistrement de la réplication les fixe, et tout choix qui toucherait la revendication est un nœud de Lazar. »
- Après : « **Règle de réplication, fixée avant le scellement de ce texte** (nœud de Lazar : elle touche la revendication ; points à trancher, point 1, recommandation retenue : « l'écrire avant la lecture de ce cycle ») : `<<REGLE_REPLICATION>>` — ce qui compte comme une **issue positive** de ce cycle (« accumuler, propre » seul, ou aussi « propre, sans gain d'accumulation établi ») et ce qui compte comme une **issue répliquée** (le même état ; aux mêmes doses ou à une dose quelconque des quatre ; au même niveau corrigé). Rien de cette règle ne peut être écrit ni changé après `LECTURE-ACC2`. »
- Table des marqueurs, après la ligne de `<<ATTAQUE_SHA256>>` (avant : « | `<<ATTAQUE_SHA256>>` | empreinte de l'issue scellée du bras d'attaque informé (lancé : choix de Lazar, points à trancher, point 7 (ii)) | session mère, avant le scellement | ») → après : cette même ligne, suivie de « | `<<REGLE_REPLICATION>>` | issue positive et issue répliquée (« Suite des cycles », règle de réplication) | Lazar (nœud), recopié par la session mère, avant le scellement | ».
- Recommandation du contre-lecteur, pour la décision de Lazar (confiance 0,55) : issue positive = « accumuler, propre » et aussi « propre, sans gain d'accumulation établi » (toute phrase qui affirme une propreté) ; issue répliquée = le même état, à au moins une dose des quatre, au même niveau corrigé, sans exiger les mêmes doses (la borne « au plus K × 0,025² » vaut alors telle quelle). Défaut : aucun (nœud).
- Conséquence : la note des différences, § 7, point 5, et le préenregistrement disent désormais la même chose.

### Majeurs

**M-1 — repli « sans second témoin » sous nœud (préenregistrement ; conséquence 5).**
- Avant : « à défaut de second témoin : moitiés par tâche des textes honnêtes lus sous l'état témoin (limite déclarée : les deux membres ne partagent plus leurs textes) »
- Après : « à défaut de second témoin — écart au choix de Lazar (points à trancher, point 11) : nœud ; ce qui suit ne vaut que sur son mot — : moitiés par tâche des textes honnêtes lus sous l'état témoin (limite déclarée : les deux membres ne partagent plus leurs textes) »
- Avant : « sans second témoin : « particularité de l'adaptateur non mesurée » est écrit à côté de toute issue « propre » ; »
- Après : « sans second témoin (écart au choix de Lazar, accepté par son mot : voir « Deux passages ») : « particularité de l'adaptateur non mesurée » est écrit à côté de toute issue « propre » ; »

**M-2 — ce que l'analyste connaît de la recette (préenregistrement et ordre ; conséquence 3).**
- Préenregistrement. Avant : « **hors son mode**, que Lazar a fixé : « coût déclaré gonflé », rejoué à neuf — même recette, adaptateurs réappris avec des graines neuves, tâches fraîches ; points à trancher, point 2, option (a)) »
- Après : « **hors son mode et le fait qu'elle reprend la recette du développement**, que Lazar a fixés : « coût déclaré gonflé », rejoué à neuf — même recette, adaptateurs réappris avec des graines neuves, tâches fraîches ; points à trancher, point 2, option (a) ; restent fermés le texte scellé de la recette, sa règle du tirage, son entropie et tout ce qu'elle précise au-delà) »
- Avant : « (connaître le mode, fixé par Lazar et écrit dans ce texte, n'est pas avoir lu la recette) »
- Après : « (connaître le mode et le fait que la recette reprend celle du développement, fixés par Lazar et écrits dans ce texte, n'est pas avoir lu la recette) »
- Ordre, section 5, point 1. Avant : « Seul le mode est connu de l'analyste, parce que Lazar l'a fixé et que le préenregistrement l'écrit : « coût déclaré gonflé », rejoué à neuf (points à trancher, point 2, option (a)). »
- Après : « Seuls sont connus de l'analyste le mode et le fait que la recette reprend celle du développement, parce que Lazar les a fixés et que le préenregistrement les écrit : « coût déclaré gonflé », rejoué à neuf (points à trancher, point 2, option (a)) ; le texte scellé de la recette, sa règle du tirage, son entropie et la liste restent fermés. »

**M-3 — la réserve neuve et la réserve « non répliquée » écrites par le code et éprouvées (préenregistrement, « Code neuf » ; R5).**
- Avant : « garde qui sépare les scores de sonde (aucune moyenne ni médiane sur les jetons) de la mesure d'intensité (moyenne sur les jetons d'une divergence) ; »
- Après : « garde qui sépare les scores de sonde (aucune moyenne ni médiane sur les jetons) de la mesure d'intensité (moyenne sur les jetons d'une divergence) ; écriture de chaque réserve à partir des lignes du registre propre (dont `OUVERTURE-TEMPS1-ACC2` pour la réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 », et la réserve « non répliquée » à côté de toute issue positive au sens de la règle de réplication), éprouvée sur un cas où elle s'applique et sur un cas où elle ne s'applique pas ; »

### Portage de `GO-2026-11-18-58` (point 7 du mandat)

Contenu du choix : le temps 1 s'ouvre sur les seuls verdicts scellés de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis) ; leur table conjointe reste exigée si elle est prévue ; la validité de l'adaptateur vient ensuite, **en réserve écrite** dans le préenregistrement et l'ordre ; le lot de la validité de l'adaptateur (lot E de l'ordre) n'est ouvert que si ses lignes existent. Rien d'autre n'est desserré.

**G-1 (majeur ; préenregistrement, « Décisions qui fondent ce texte », fin de l'alinéa).**
- Avant : « n'est pas tranché ; il reste à Lazar. » (seule occurrence suivie d'un point : fin de l'alinéa « Décisions »)
- Après : « n'est pas tranché ; il reste à Lazar. **Ouverture du temps 1 sans le verdict de la validité de l'adaptateur** (mot direct de Lazar « ecommandation : option a, confiance 0,7. go », `GO-2026-11-18-58`, R-3440) : le temps 1 s'ouvre sur les seuls verdicts scellés de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis), et sur leur table conjointe si elle est prévue ; la validité de l'adaptateur vient ensuite, en réserve écrite (« Critères de lecture gelés », réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 ») ; le lot de la validité de l'adaptateur n'est ouvert à l'analyste que si ses lignes existent (ordre exploratoire, section 2, lot E). »
- Et, même alinéa, la déclaration de lecture : avant « les seules lignes GO-2026-11-18-55, -56 et -57 du registre des accords » → après « les seules lignes GO-2026-11-18-55, -56, -57 et -58 du registre des accords » (si le rédacteur du brouillon 5 lit la ligne -58 ; sinon « … et la ligne GO-2026-11-18-58 telle que la session mère la transmet »).

**G-2 (majeur ; préenregistrement, « Plan d'analyse », point 2).**
- Avant : « → ouverture du temps 1 (`OUVERTURE-TEMPS1-ACC2`) → »
- Après : « → ouverture du temps 1 (`OUVERTURE-TEMPS1-ACC2` ; conditions : ordre exploratoire, section 2 ; la ligne écrit si le verdict de la validité de l'adaptateur est scellé et quelles lignes du lot de la validité de l'adaptateur sont ouvertes, `GO-2026-11-18-58`) → »

**G-3 (majeur ; préenregistrement, « Critères de lecture gelés », réserves : insertion après la réserve « non répliquée »).**
- Avant : « « issue non répliquée : aucune revendication n'en est tirée » (« Suite des cycles », règle de réplication). »
- Après : cette même fin de ligne, suivie d'une ligne neuve : « - **réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 »** (choix de Lazar, `GO-2026-11-18-58`) : si la ligne `OUVERTURE-TEMPS1-ACC2` écrit que le verdict de la validité de l'adaptateur n'était pas scellé, écrite à côté de **toute** phrase du cycle : « sonde conçue avant le verdict de la validité de l'adaptateur ; lot de la validité de l'adaptateur [ouvert / fermé] au temps 1 ; témoin de l'apprentissage de la sonde principale : [témoin distillé honnête / adaptateur témoin du premier cycle / sans objet] », complétée par l'issue de ce verdict s'il est scellé avant `VERDICT-ACC2` (« verdict de la validité de l'adaptateur : [issue], scellé le [date] »), sinon par « verdict de la validité de l'adaptateur non scellé au verdict de ce cycle ». Si ce verdict, scellé avant `SCELLEMENT-ACC2`, met en cause le témoin distillé honnête ou la remise à l'échelle par la divergence que ce texte emploie (« Métrique », « Intensité »), c'est un nœud de Lazar avant le scellement (changement de la famille : plan, point 1). Elle ne change aucun état. »

**G-4 (majeur ; ordre exploratoire, section 2, condition d'ouverture 3).**
- Avant : « 3. **les verdicts de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis) sont scellés**, ainsi que leur **table conjointe** si elle est prévue (`CONJOINTE-BBIS`) et le verdict de la validité de l'adaptateur — ou la session mère a écrit que la lecture concernée n'aura pas lieu : l'analyste recevrait les fichiers des deux étapes, il ne doit pouvoir peser sur aucun de ces verdicts ; il est exclu de tout rôle dans ces verdicts et dans cette table ; leurs textes scellés gardent leur statut ; »
- Après : « 3. **les verdicts de la lecture des sondes (étape B) et de l'apprentissage des sondes sur la tâche (étape B bis) sont scellés**, ainsi que leur **table conjointe** si elle est prévue (`CONJOINTE-BBIS`) — ou la session mère a écrit que la lecture concernée n'aura pas lieu : l'analyste recevrait les fichiers des deux étapes, il ne doit pouvoir peser sur aucun de ces verdicts ; il est exclu de tout rôle dans ces verdicts et dans cette table ; leurs textes scellés gardent leur statut. **Le verdict de la validité de l'adaptateur n'est pas une condition d'ouverture** (choix de Lazar, `GO-2026-11-18-58`, R-3440) : la ligne `OUVERTURE-TEMPS1-ACC2` écrit s'il est scellé ; s'il ne l'est pas, la réserve « validité de l'adaptateur non jugée à l'ouverture du temps 1 » du préenregistrement s'applique ; l'analyste reste exclu de tout rôle dans ce verdict, et ni son rapport, ni ses sondes, ni ses autres sorties ne sont transmis à un lecteur ou à un juge de la validité de l'adaptateur avant que ce verdict soit scellé ; le lot E n'est ouvert que si ses lignes existent (lot E ci-dessus) ; »

**G-5 (majeur ; ordre exploratoire, section 2, lot E ; et section 11).**
- Avant : « **Lot E — la validité de l'adaptateur**, si ses lignes existent au registre propre `registres/validite-adaptateur-v1.md` : »
- Après : « **Lot E — la validité de l'adaptateur**, si ses lignes existent au registre propre `registres/validite-adaptateur-v1.md` — son verdict peut ne pas être scellé (choix de Lazar, `GO-2026-11-18-58` ; condition d'ouverture 3) — : »
- Avant : « , lecture et verdict : `<<EMPREINTES_LOT_VADAPT>>` (lignes `SCORES-RELECTURE-VADAPT`, `SORTIES-HD-VADAPT`, `LECTURE-VADAPT`). »
- Après : « , lecture et, s'il est scellé, verdict : `<<EMPREINTES_LOT_VADAPT>>` (lignes `SCORES-RELECTURE-VADAPT`, `SORTIES-HD-VADAPT`, `LECTURE-VADAPT`, et la ligne du verdict si elle existe) ; seules s'ouvrent les lignes dont la session mère a recopié l'empreinte (en-tête de cette section ; condition 4) ; une ligne absente laisse sa part du lot fermée, et la session mère écrit « lot E fermé » si aucune n'existe. »
- Section 11, ligne du point 14. Avant : « condition d'ouverture 3 confirmée telle qu'écrite (les deux verdicts, leur table conjointe si elle est prévue, le verdict de la validité de l'adaptateur) : la ligne « laissé à confirmer » de la section 9 est close par ce choix »
- Après : « condition d'ouverture 3 confirmée pour les deux verdicts et leur table conjointe si elle est prévue ; **le verdict de la validité de l'adaptateur en est retiré** par un choix ultérieur de Lazar (`GO-2026-11-18-58`, R-3440 : réserve écrite au préenregistrement et ici ; lot E ouvert seulement si ses lignes existent) : la ligne « laissé à confirmer » de la section 9 est close par ces deux choix »
- Et la table de la section 11 (ou celle du brouillon 5) reçoit une ligne pour `GO-2026-11-18-58` : section 2, condition 3 et lot E.

**G-6 (mineur ; devis, section 6).**
- Avant : « **Ces 1 024 passes n'existent que si la pièce du témoin distillé de la validité de l'adaptateur a été créée** »
- Après : « **Ces 1 024 passes n'existent que si la pièce du témoin distillé de la validité de l'adaptateur a été créée et que ses lignes sont ouvertes au temps 1** (lot E de l'ordre exploratoire ; son verdict peut ne pas être scellé : `GO-2026-11-18-58`) »

### Mineurs

**m-1 — marqueur du nœud 3 visible du validateur (préenregistrement, deux occurrences de la même chaîne : statut et décisions).**
- Avant (deux fois) : « **[NŒUD 3 — OUVERT]** : l'énoncé du contraste à témoin apparié de la porte de fin de phase 1 (formulation A ou formulation C du brouillon de décision N-074) n'est pas tranché ; il reste à Lazar »
- Après, une fois le nœud tranché : « **Nœud 3 tranché par Lazar** (`<ligne de GO>`) : formulation [A ou C] du brouillon de décision N-074, hors de ce texte »
- Tant qu'il ne l'est pas : remplacer `**[NŒUD 3 — OUVERT]**` par `<<NOEUD_3_PORTE_G1>>` (ajouté à la table des marqueurs : « Lazar, avant le scellement »), pour que le validateur refuse le scellement. Ce texte ne dépendant pas du nœud 3, Lazar peut aussi dire qu'il se scelle sans lui : la phrase devient alors « nœud 3 non tranché au scellement ; hors de ce texte ».

**m-2 — la réserve « non répliquée » après une réplication lue (préenregistrement).**
- Avant : « écrite à côté de toute issue « accumuler, propre » tant que la seconde lecture de la même sonde gelée sur une autre famille neuve n'est pas lue : « issue non répliquée : aucune revendication n'en est tirée » »
- Après : « écrite à côté de toute issue positive au sens de la règle de réplication tant que la seconde lecture de la même sonde gelée sur une autre famille neuve n'a pas rendu une issue répliquée : « issue non répliquée : aucune revendication n'en est tirée » ; si elle est lue sans la rendre : « réplication échouée : aucune revendication n'en est tirée » »

**m-3 — dépôt daté chez un tiers aligné sur le choix de Lazar (préenregistrement ; conséquence 4).**
- Avant : « dépôt daté chez un tiers, s'il est accordé (`DEPOT-TIERS-ACC2`) »
- Après : « dépôt daté chez un tiers, accordé (empreintes seules, geste de Lazar : points à trancher, point 7 (i)) (`DEPOT-TIERS-ACC2`) »
- Avant : « `DEPOT-TIERS-ACC2` (facultative) »
- Après : « `DEPOT-TIERS-ACC2` (geste de Lazar, accordé ; si elle manque, réserve « sans dépôt daté chez un tiers ») »

**m-4 — table de traitement du brouillon 5.** Ajouter, sous l'entrée « Brouillon 4 : pas encore contre-lu », l'entrée de cette contre-lecture (brouillon relu et son empreinte ; ce rapport et son empreinte ; traitement couple par couple) : le validateur exige au moins deux empreintes par entrée.

**m-5 — « à confirmer par la recette » (devis, section 8) :** juste ; l'instance qui conçoit la recette dit si le lecteur du dommage reste celui du développement. Aucun couple.

**m-6 — arithmétique de la réplication (R6).** Verser « 1 − (1 − 0,025)^K » et « K × 0,025² » (et « sous 0,025 jusqu'à K = 40 ») au prochain script de calcul scellé, et y renvoyer depuis « Suite des cycles ». Sans bloquer.

---

## 10. Point (8) : ce qui reste avant le scellement

1. **Décisions de Lazar** : le nœud 3 (ou son mot que le texte se scelle sans lui, m-1) ; **la règle de réplication** (B-1 : issue positive, issue répliquée).
2. **Brouillons 5** du préenregistrement et de l'ordre (et 4 du devis pour G-6), portant B-1, M-1 à M-3, G-1 à G-6, m-1 à m-4, par script et note des différences ; puis **une vérification courte par un agent neuf** d'un autre modèle que le rédacteur (R2).
3. **Faits à venir et textes à écrire** : l'offre de disque d'au moins 250 gigaoctets au prix du stockage ; la règle du tirage complémentaire et la procédure d'extraction portée à cette échelle (proposition 13), par des instances qui ne sont ni l'analyste ni un auteur ; le relevé des compteurs du premier tirage, puis le **devis de l'extraction** et sa ligne ; le **devis et la ligne du bras d'attaque** (avant `ATTAQUE-ACC2`, donc avant le scellement) ; la ligne de dépense de la relecture complémentaire.
4. **Chaîne d'ouverture** : scellement de l'ordre (marqueurs de sa section 2 recopiés par la session mère, lot E compris ou « fermé ») ; recette scellée et fermée ; verdicts scellés de l'étape B et de l'étape B bis (et leur table conjointe si elle est prévue) ; ligne `OUVERTURE-TEMPS1-ACC2` écrivant l'état du verdict de la validité de l'adaptateur.
5. **Temps 1 puis marqueurs** : les quatorze marqueurs de gabarit (et `<<REGLE_REPLICATION>>`), dont la sonde gelée, l'épreuve du développement, l'effectif, le code contre-lu qui rejoue l'épreuve, l'issue du bras d'attaque ; puis la contre-lecture finale du texte rempli.

---

## 11. Ce que j'ai fait, et lectures hors mandat

- **Lu** : les cinq pièces, entières (préenregistrement, ordre, note des différences ; devis par sa différence au brouillon 2 et ses sections 6 à 8 ; script entier) ; le rapport de vérification des brouillons 2, **en entier** ; les points à trancher, brouillon 3, sections A et B entières et des lignes repérées de la section C ; la sortie de calcul version 3, § 8 et § 9 et des lignes repérées ; `registres/go.md`, les seules lignes `GO-2026-11-18-56` et `GO-2026-11-18-58` (repérées par leur numéro) ; `src/controle_ia/prereg.py`, motifs du validateur.
- **Rejoué** : le script de fabrication et le validateur, dans mon dossier de travail temporaire ; aucune donnée lue.
- **Hors mandat, déclaré** : (1) liste non récursive des noms de `prereg/contre-lectures/`, du sous-dossier des pièces et de `docs/decisions/` filtrés par motif ; empreinte du brouillon de décision N-074, brouillon 2 (non lu) ; (2) `git status --short` (fichiers modifiés hors de ce cycle, non ouverts). Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; aucun résultat, score ni aire d'aucune étape.
- Ni commit, ni poussée, ni écriture sous `registres/` ; aucun fichier existant modifié ; aucune dépense.
