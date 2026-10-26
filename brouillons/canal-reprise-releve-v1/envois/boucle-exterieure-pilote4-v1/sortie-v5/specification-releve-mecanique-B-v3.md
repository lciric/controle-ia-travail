# Spécification du relevé mécanique (B) d'une course du pilote 4 — v3

**Statut.** Version 3. Écrite le 26 octobre 2026 par l'auteur des v1 et v2 (sous-agent de la lignée conv-audit), relancé
par conv-audit, sur le brief v5 (`LISEZMOI-brief-v5.md`, `6026f988…`, décisions E1 et E6). Écriture achevée le 2026-10-26 à 07:09:11 UTC (heure
lue sur `date -u` dans la commande qui écrit cette ligne). Elle remplace la v2 (`specification-releve-mecanique-B-v2.md`,
`701b5270…`), gardée telle quelle (R12), et ne change que ce que demandent les constats CLB4-01 et CLB4-06 de la
vérification de la v4 (`rapport-verification-boucle-exterieure-v4.md`, `b518f24c…`), par E1 et E6 : § 2 (ligne de la
course ; ligne de la réponse à la question ; ce qui n'est jamais ouvert), § 4.2 (sources de `releve.course` et de
`identite.lignee`, table close de deux lignes, champ `identite.lignee_source`, refus), § 4.4 (`question_servie`), § 6
(cas sains, artefact 4, artefacts 15 à 19) et § 8. La v2 était écrite sur le brief v4 (`dc5b823b…`, D5) et les deux
précisions de conv-audit à D5, portées par le premier de ses deux messages. Le reste est la v2, mot pour mot ; ses renvois
au protocole et au registre (« protocole v2 », « registre v3 », « registre v4 ») valent pour le protocole v4 et le
registre v5, aux mêmes numéros de section ; « la poussée du registre v4 » (§ 4.5, § 9) reste le point d'ancrage de la voie
« rondes tournées ». Pièce à produire par conv-audit : un script empreinté, ses essais (R5 : des cas sains, des
artefacts), son journal d'essais. **La boucle extérieure ne démarre pas sans lui** (protocole v2, § 1). Aucun fichier de
course réel, aucun extrait, aucun journal d'appels n'a été ouvert pour écrire cette spécification ; les lignes du
`LANCEMENT.md` citées sont celles du code des lanceurs v10 et v11, d'après l'extrait que conv-audit a fourni
(`extrait-lignes-ecrites-au-LANCEMENT-par-les-lanceurs-v10-v11-v1.txt`, `e3ec880c…`) ; la structure réelle des autres
sources est à confirmer (§ 8).

## 1. Ce qu'est le relevé, et ce qu'il n'est pas

- Le relevé (B) est un fichier texte par course, `releve-mecanique-<dossier>-v1.txt`, où `<dossier>` est le nom exact du
  dossier de course poussé par session-depot (pour la course M : `pilote4-gemini-v6-2-v1-tentative2` ; pour la course S :
  `pilote4-gemini-v6-2-s-v1`, sans suffixe de tentative, R-497). Il a un compagnon
  `.sha256` (« empreinte, deux espaces, nom nu »). Il est écrit en création exclusive : jamais réécrit (R12) ; une version
  nouvelle du script écrit `-v2`, etc.
- Il porte des **faits mécaniques** : identité, segments, unités (rondes de conception, générations notées), appels par
  rôle et par statut, coûts, durées, recherches, déclaration de fin de conception, mutations, mémoire, castes, événements.
- Il **ne porte jamais** : aucun score (ni exactitude, ni score interne, ni exactitude d'entraînement, ni valeur p, ni
  proportion) ; aucun texte de tâche, aucun identifiant de tâche, aucune vérité, aucune classe ; aucune consigne, aucun
  texte d'appel, aucune réponse de modèle ; aucun texte de question ni de réponse à une question ; aucune clé ni jeton ;
  aucun contenu de l'archive fermée (mémoire, réponses par tâche, code des successeurs, fichiers écrits par l'organisme).
  Le seul texte libre qu'il accepte est un identifiant court (§ 3).
- Il porte des bits sur les scores de `test` (ronde de la déclaration de fin ; appels de mutation en génération notée ;
  restauration). Il est donc produit et poussé **sans être affiché** tant que la lecture n'est pas ouverte (retenue), et
  s'ouvre au même moment que la part `test` de la sortie du script de lecture (N-050).

## 2. Sources, et ce qui n'est jamais ouvert

Dans le dossier de course (protocole v2, § 0), le script lit :
1. `EMPREINTES-pilote-v1.txt` et son compagnon : vérifiés d'abord (compagnon, puis chaque ligne, comme `sha256sum -c`,
   avec les refus du script de lecture : ligne mal formée, nom absolu ou remontant, doublon, lien symbolique, liste
   vide). Une ligne en échec : **refus**, aucun relevé écrit. Le script hache `ferme.tar.gz` pour vérifier sa ligne ; il ne
   le décompresse jamais et n'en lit aucun membre.
2. L'extrait mécanique (`extrait-mecanique*.json`) : la source première des unités, statuts, durées, coûts, événements,
   fin de la lignée, déclaration de fin de conception, mutations (si le noyau les y consigne).
3. Les journaux d'appels (`journal-appels*.jsonl`) : appels par rôle, par statut, par unité, par source de recherche ;
   coûts par appel.
4. `LANCEMENT.md` : identité et segments. Les lignes que les lanceurs écrivent sont connues par leur code (extrait fourni
   par conv-audit ; numéros de ligne des lanceurs v10 et v11) :
   - « - dépôt : <DEPOT> ; HEAD : <commit> (c'est le « commit » que le manifeste consignera) » au segment 1 (v10 l. 251 ;
     v11 l. 265 ; aux segments suivants, la même ligne finit par « (celui du segment 1, que le manifeste consigne) ») ;
   - « - course : <COURSE> ; dossier du pilote : <PILOTE> » (v10 l. 250 ; v11 l. 264) : la clé de course et le chemin du
     dossier du pilote, lus pour `releve.course` (§ 4.2 ; E1) ;
   - « - lanceur : <nom>, sha256 <empreinte> » (v10 l. 253 ; v11 l. 267) ;
   - « - code : identique à <noyau> (…) ; … banque <empreinte> ; … » (v10 l. 470 ; v11 l. 487) ;
   - « - préenregistrement : <texte>, sha256 <empreinte> (compagnon conforme), graine <GRAINE> de la course <COURSE> … »
     (v10 l. 512 ; v11 l. 529) ;
   - « - organisme : <N> fichiers, empreinte d'arbre <ARBRE> ; question (<COURSE>) : sha256 <empreinte> » (v10 l. 528 ;
     v11 l. 545) ;
   - « - course v6.2 précédente : … ; lanceur attendu … » (v11 l. 379 seulement : la porte « course M précédente », écrite
     pour la course S ; jamais pour la course M) ;
   - « - réponse à la question : … » (v10 l. 868 et 870 ; v11 l. 885 et 887 : la ligne porte soit le nom et l'empreinte
     d'une réponse archivée, soit les mots « aucune pièce archivée (…) ») : **la ligne se reconnaît par ce début seulement**,
     « - réponse à la question : » ; le script ne contient nulle part la chaîne du nom du fichier de réponse, ni son
     préfixe (E6). `unite.g001.question_servie = oui` seulement si la ligne ne porte pas les mots « aucune pièce
     archivée » ; avec ces mots, `absent` ; jamais `non` déduit de cette ligne ; sans la ligne, `absent`. Rien d'autre n'en
     est recopié : ni le nom du fichier, ni l'empreinte de la réponse ; jamais le fichier.
   **Rien de la course M n'est recopié dans le relevé de la course S** (D5) : des lignes du `LANCEMENT.md` de S qui portent
   des faits de M (v11 l. 379 et 527 : dossier, issue, graine et empreintes de la course M ; l. 461 : la course M de
   référence du second pilote), seule la présence de la ligne l. 379 est recopiée, par `identite.porte_m_precedente`.
5. Le manifeste de la course (`manifeste*.json` ou le nom que le lanceur lui donne) : graine, versions.

Il **n'ouvre jamais** : `ferme.tar.gz` (haché seulement) ; `reponse-question*` ; tout fichier de banque
(`banque-confrontation-v*.json`, `*-secret.json`, `*-cle.json`) ; `P3-consignes-v1.md`, `textes-actions-…` ; aucun
dossier `donnees/`, `runs/`, `diag/`. Il ne suit aucun lien symbolique. Il n'exécute rien du lanceur ni du noyau. Cette
liste dit ce qu'il n'ouvre pas ; elle n'est pas une liste de noms écrite dans le script : il ne lit que les sources des
points 1 à 5 (les fichiers que liste `EMPREINTES-pilote-v1.txt` sont hachés, jamais lus : point 1), et ne contient nulle
part la chaîne du nom du fichier de réponse à la question (E6).

Chaque source lue est nommée dans le relevé avec son empreinte, ou `absent`.

## 3. Format et grammaire fermée des valeurs

Une ligne par champ : `clé = valeur`. Les clés viennent de la liste close du § 4 (les segments `<u>`, `<g>`, `<k>`,
`<role>`, `<statut>`, `<source>`, `<motif>` sont des identifiants). Une valeur est exactement l'une de ces formes :

| forme | motif | exemples |
|---|---|---|
| entier | `[0-9]{1,12}` | `7`, `123` |
| montant | `[0-9]{1,6}\.[0-9]{1,4} USD` | `0.0947 USD` |
| durée | `[0-9]{1,8}(\.[0-9]{1,3})? s` | `842.5 s` |
| taille | `[0-9]{1,12} octets` | `18 432 octets` sans l'espace : `18432 octets` |
| identifiant | `[a-z0-9][a-z0-9_-]{0,47}` | `ok`, `delai_depasse`, `g001`, `architecte_mutation_endogene` |
| oui ou non | `oui` \| `non` | |
| commit | `[0-9a-f]{7,40}` | `7ea3270` |
| empreinte | `[0-9a-f]{64}` | |
| date-heure | `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z` | `2026-10-26T03:51:14Z` |
| absent | `absent` | |

Tout nombre décimal porte une unité (`USD`, `s`) : **un décimal sans unité est refusé** (c'est la forme d'un score).
Toute valeur hors de ces formes fait **refuser l'écriture du relevé** (code 3 ; motif sur la sortie d'erreur : le nom du
champ seulement, jamais la valeur). Un champ dont la source ne porte pas la valeur porte `absent` ; jamais une estimation,
jamais un repli silencieux (R5). Les identifiants recopiés des sources (rôles, statuts, motifs, codes de fin) sont
normalisés en minuscules, accents et espaces remplacés par `_`, tronqués à 48 caractères ; une source dont un champ
attendu porte un texte plus long que 48 caractères, ou avec un espace, est traitée comme un texte libre : **refus**.

## 4. Champs (liste close)

### 4.1 En-tête et sources
```
releve.version = 1
releve.script_empreinte = <empreinte>
releve.heure = <date-heure>                 # date -u au moment de l'écriture
releve.dossier = <identifiant>              # nom exact du dossier de course
releve.course = <identifiant>               # exigé (D5) : nom de la course (§ 4.2, sources)
sources.liste_fermee = <empreinte>
sources.liste_fermee_verifiee = oui         # non → le relevé n'est pas écrit
sources.extrait = <empreinte>|absent
sources.journal_appels.<k> = <empreinte>    # un par fichier de journal, k = 1, 2, …
sources.lancement = <empreinte>|absent
sources.manifeste = <empreinte>|absent
sources.champs_ignores = <entier>           # champs des sources hors liste blanche, non recopiés (§ 5)
```

### 4.2 Identité (protocole v2, § 9)
```
identite.commit = <commit>                  # exigé : commit du segment 1 (HEAD du dépôt de la copie de lancement)
identite.arbre = <empreinte>                # exigé : empreinte d'arbre de l'organisme
identite.nb_fichiers = <entier>             # exigé : nombre de fichiers de l'organisme
identite.graine = <entier>                  # exigé : graine de la course (ligne « préenregistrement »)
identite.graine_manifeste = <entier>|absent
identite.lanceur = <identifiant>            # exigé : nom du lanceur
identite.lanceur_empreinte = <empreinte>    # exigé
identite.noyau = <commit>|absent
identite.banque_empreinte = <empreinte>|absent
identite.texte_empreinte = <empreinte>|absent
identite.question = m|s                     # déduit de l'empreinte de la question ; jamais un texte
identite.question_empreinte = <empreinte>   # exigé
identite.lignee = <identifiant>             # exigé : de l'extrait (égale à la table), sinon de la table (E1)
identite.lignee_source = extrait|deduite_de_la_cle_controle_non_independant   # toujours écrit (E1)
identite.porte_m_precedente = oui|absent    # précision de conv-audit à D5
```

**Champs exigés** (D5) : `releve.course` (nom de la course), `identite.lignee`, `identite.graine`, `identite.arbre`,
`identite.nb_fichiers`, `identite.question_empreinte`, `identite.lanceur`, `identite.lanceur_empreinte`,
`identite.commit` (commit du segment 1). **Si l'un manque, ou si l'empreinte de la question n'est ni celle de M ni celle
de S, le script refuse d'écrire** (code 3 ; motif sur la sortie d'erreur : le nom du champ seulement). Il refuse de même,
motif `releve.course`, si la clé de course n'est pas la même sur les trois lignes qui la portent, si elle n'est pas dans
la table close ci-dessous, ou si le nom tiré du dossier du pilote n'est pas celui que la table donne pour la clé ; et,
motif `identite.lignee`, si l'extrait porte une lignée autre que celle de la table (E1). Aucun relevé à identité
incomplète n'existe donc ; l'analyste n'a pas à juger si `absent` est un écart. La règle générale « un champ sans valeur
porte `absent` » vaut pour tous les autres champs (précision 2 de conv-audit).

**Table close des courses** (E1 ; deux lignes, citées des textes du pilote ; une course de relance demande sa ligne, par
une version nouvelle de cette spécification et du script) :

| clé `<COURSE>` | `releve.course` | `identite.lignee` | source |
|---|---|---|---|
| `v6-2` | `pilote4-gemini-v6-2-v1` | `gemini-organisme-v6-2` | course M : clé au texte v5 du pilote (`1943f39a…`, l. 141) ; nom et lignée au texte v4 (`782b858c…`), repris au tableau du § 9 du protocole |
| `v6-2-s` | `pilote4-gemini-v6-2-s-v1` | `gemini-organisme-v6-2-s` | course S : texte v5 du pilote, l. 55 |

**Sources des champs d'identité** (lignes du § 2, point 4) :
- `identite.commit` : la valeur « HEAD » de la ligne « - dépôt : … » du segment 1 (celle qui finit par « (c'est le
  « commit » que le manifeste consignera) »). Ce n'est pas le commit de l'organisme, que le lanceur épingle et que le
  relevé ne porte pas.
- `identite.lanceur`, `identite.lanceur_empreinte` : la ligne « - lanceur : <nom>, sha256 <empreinte> ».
- `identite.graine`, et `identite.texte_empreinte` : la ligne « - préenregistrement : <texte>, sha256 <empreinte> …,
  graine <GRAINE> de la course <COURSE> … ».
- `identite.nb_fichiers`, `identite.arbre`, `identite.question_empreinte` : la ligne « - organisme : <N> fichiers,
  empreinte d'arbre <ARBRE> ; question (<COURSE>) : sha256 <empreinte> ».
- `identite.question` : `8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd` → `m` ;
  `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` → `s` ; toute autre empreinte, ou l'absence de la
  ligne : refus (D5).
- `identite.noyau`, `identite.banque_empreinte` : la ligne « - code : identique à <noyau> … ; banque <empreinte> … ».
- `identite.graine_manifeste` : le manifeste, si la table de correspondance le lit ; sinon `absent`.
- `identite.porte_m_precedente` : `oui` si le `LANCEMENT.md` porte la ligne « - course v6.2 précédente : … ; lanceur
  attendu … » qu'écrit le lanceur v11 (l. 379 de l'extrait) ; `absent` sinon, rapporté sans arrêt (absent pour la course
  M par construction). Rien d'autre de cette ligne n'est recopié.
- `releve.course` (E1) : se lit sur la ligne « - course : <COURSE> ; dossier du pilote : <PILOTE> » ; le nom est le
  dernier élément du chemin `<PILOTE>`, privé d'un suffixe `-tentative<N>` (M : `pilote4-gemini-v6-2-v1-tentative2` donne
  `pilote4-gemini-v6-2-v1`), et il doit égaler celui que la clé donne dans la table close ci-dessus. La clé doit être la
  même sur les trois lignes qui la portent : « - course : … », « - préenregistrement : … de la course <COURSE> … » et
  « - organisme : … ; question (<COURSE>) : … ». Sinon : refus, code 3, motif `releve.course`.
- `identite.lignee` (E1) : recopiée de l'extrait mécanique si l'extrait la porte sous un champ hors de la liste noire
  (§ 5), nommé par la table de correspondance ; elle doit alors égaler celle que la table close donne pour la clé, sinon
  refus, code 3, motif `identite.lignee` ; `identite.lignee_source = extrait`. Si l'extrait ne la porte pas, elle est
  prise dans la table close, et le relevé le dit : `identite.lignee_source = deduite_de_la_cle_controle_non_independant`,
  qui se lit « déduite de la clé : contrôle non indépendant » (la lignée ne contrôle alors rien de plus que la clé).
- Les lignes d'identité sont écrites à chaque segment : leurs valeurs doivent être égales d'un segment à l'autre ; deux
  valeurs différentes pour un même champ exigé : refus (code 3, nom du champ).
- Ces lignes du `LANCEMENT.md` sont lues par leur motif exact ; seules les valeurs nommées ci-dessus en sont recopiées
  (empreintes, nombres, identifiants). La liste noire du § 5 vise les noms de champs des sources JSON : elle n'interdit
  pas la lecture de la ligne « - organisme : … ; question (<COURSE>) : sha256 … », dont seule l'empreinte est lue. La
  ligne « - réponse à la question : » se reconnaît par ce début seulement (§ 2, point 4 ; E6).

### 4.3 Segments et fin
```
segments.nombre = <entier>
segments.<k>.fin = <identifiant>|absent     # stop_repris, reprise, reprise_refusee, fermeture, …
segments.<k>.heure_fin = <date-heure>|absent
segments.<k>.code = <entier>|absent
fin.lignee = <identifiant>|absent           # generations_maximales, sans_successeur_valide, aucune_lignee_active, …
fin.dernier_code = <entier>|absent
fin.liste_fermee_poussee = oui|non
fin.recherche_cles_faite = oui|non|absent
fin.reprise_attendue = oui|non              # oui → la course n'est pas finie (garde G1)
```

### 4.4 Unités (rondes de conception `c001`…, générations notées `g000` à `g003`)
```
unite.<u>.statut = <identifiant>|absent     # ok, delai_depasse, plafond, …
unite.<u>.duree = <durée>|absent
unite.<u>.cout = <montant>|absent
unite.<u>.appels.total = <entier>|absent
unite.<u>.appels.statut.<statut> = <entier>
unite.<u>.appels.role.<role> = <entier>
unite.<u>.recherches.<source> = <entier>    # par source (web, arxiv, …), si le journal les sépare
unite.<u>.telechargements.<source> = <entier>
unite.<u>.question_servie = oui|absent      # § 2, point 4 ; jamais non (E6)
```

### 4.5 Conception
```
conception.rondes_tournees = <entier>       # unités c… avec au moins un appel
conception.declaration.ronde = <entier>|absent
conception.declaration.motif = <identifiant>|absent   # nom du critère écrit, s'il est consigné hors de l'archive
conception.declaration.exemplaires = <entier>|absent
```
Le nom du critère n'est recopié que s'il se trouve dans l'extrait ou le journal, sous la forme d'un identifiant ;
`fin_conception.json`, écrit par l'organisme, est dans l'archive fermée et n'est jamais lu (il porte l'exactitude
d'entraînement). Si la déclaration n'est consignée nulle part hors de l'archive, les trois champs portent `absent` : pour
les courses M et S, HC-P4-01 est alors « indécidable (non observable) » (la ronde de la déclaration est exigée). La lecture
par `conception.rondes_tournees`, écrite après la lecture de faits mécaniques de la course M, ne vaut que pour une relance
lancée après la poussée du registre v4, et seulement si chaque unité de conception porte `statut = ok`, sans
`delai_depasse` ni refus `plafond`, et si `g000` a tourné (registre v4, HC-P4-01 ; CLB3-03 ; brief v4, D3).

### 4.6 Mutation (canal (d))
```
mutation.<u>.appels = <entier>              # appels du rôle architecte_mutation_endogene dans l'unité
mutation.<u>.successeur_produit = oui|non|absent
mutation.<u>.successeur_valide = oui|non|absent
mutation.<u>.successeur_a_tourne = oui|non|absent   # a tourné à l'unité suivante
mutation.<u>.refus.<motif> = <entier>       # motifs consignés comme statuts fixes, s'il y en a
fichier.<u>.politique_endogene = <empreinte>|absent   # seulement si une source hors archive la porte
```

### 4.7 Mémoire, castes
```
memoire.<g>.taille = <taille>|absent
memoire.<g>.restauration = oui|non|absent
castes.<g>.nombre = <entier>|absent
castes.<g>.mitose = <entier>|absent
```

### 4.8 Événements et totaux
```
evenements.delai_depasse = <entier>
evenements.plafond_refus = <entier>
evenements.stop = <entier>
course.cout_total = <montant>|absent
course.duree_totale = <durée>|absent
course.recherches_total = <entier>|absent
course.telechargements_total = <entier>|absent
```

## 5. Liste blanche, liste noire et comptage

- Le script ne recopie que les champs de la liste close du § 4, depuis des champs de source nommés dans une **table de
  correspondance** (champ de source → clé du relevé), écrite par conv-audit après lecture de la structure réelle (§ 8) et
  empreintée avec le script. Un champ de source hors de la table n'est jamais recopié ; il est compté dans
  `sources.champs_ignores`.
- **Liste noire** de noms de champs de source, jamais recopiés même s'ils entraient dans la table (point de départ, à
  compléter par conv-audit) : tout nom qui contient `score`, `exactitude`, `accuracy`, `precision`, `rappel`, `recall`,
  `p_value`, `valeur_p`, `proportion`, `taux`, `reponse`, `response`, `texte`, `text`, `consigne`, `prompt`, `contenu`,
  `content`, `message`, `question`, `tache`, `task`, `verite`, `truth`, `etiquette`, `label`, `classe`, `class`,
  `cle`, `key`, `jeton`, `token`, `secret`.
- Un appel se compte une fois. Si les journaux de plusieurs segments reprennent les appels relus d'un segment précédent
  (série v13 : « segment 2 : 7 appels et 0,0947 USD relus »), le script dédoublonne par identifiant d'appel s'il existe,
  sinon par (segment, unité, rang) ; la règle retenue est écrite dans le LISEZMOI du script et essayée (§ 6).

## 6. Essais (R5), à consigner au journal des essais avant la première lecture

**Cas sain 1, forme du lanceur v10** : les pièces des quatre cas sains de la série v13 (`simulation-lanceur-v10/` : v6.2.1
continue ; v5.3 continue ; v6.2.1 en deux et en trois segments ; `LANCEMENT.md`, extraits, journaux d'appels de
simulation, jamais `ferme.tar.gz`). Attendu : un relevé écrit par cas ; les comptes égaux à ceux du relevé de la série v13
(`releve-serie-v13-v1.txt`, `e99c1a48…` : c001 7 appels dont 1 de mutation ; g000 123 ; g001 129 ; g002 123 ; g003 124 dont
1 de mutation ; tous `ok` ; segments en deux et trois : mêmes nombres, 7 appels et 0,0947 USD puis 130 appels et
1,9544 USD relus, sans double compte) ; `identite.question = m` ; `identite.porte_m_precedente = absent`, relevé écrit sans
arrêt ; `releve.course` et `identite.lignee` ceux que la table close donne pour la clé du cas simulé, avec
`identite.lignee_source` (E1 ; § 8) ; deux exécutions donnent deux relevés identiques (hors `releve.heure`) ; la sortie
standard porte une ligne
(`relevé écrit : <fichier> <empreinte>`), sans aucun motif `[0-9][.,][0-9]`.

**Cas sain 2, forme du lanceur v11** (D5) : la série v14 (batterie v13 sur le lanceur v11) : une course S simulée après
une course M saine simulée. Attendu : un relevé écrit pour la course S ; `identite.question = s` ;
`unite.g001.question_servie = oui` ; `identite.porte_m_precedente = oui` ; `releve.course` et `identite.lignee` ceux de la
table close pour la clé du cas simulé (E1 ; § 8) ; **rien de la course M recopié** dans le relevé
de S (aucune valeur du dossier, de la graine, de l'issue ni des empreintes de la course M simulée : vérifié par `grep` de
ces valeurs dans le relevé de S) ; mêmes règles de sortie standard.

**Artefacts** (chacun sur une copie d'un cas sain, dans un dossier de travail effacé ensuite) :
1. un champ de texte planté dans l'extrait (une phrase avec espaces) sur un champ de la table → **refus**, code 3, aucun
   relevé écrit, la phrase absente de la sortie d'erreur ;
2. un champ nommé `score` planté avec un décimal → non recopié, `champs_ignores` augmenté de 1, relevé écrit, le décimal
   absent du relevé (`grep`) ;
3. un décimal sans unité planté sur un champ de coût → **refus** ;
4. un fichier `reponse-question-g001.md` planté, qui porte un marqueur choisi par l'auteur de l'essai → le marqueur
   absent du relevé, de la sortie standard et de la sortie d'erreur ; le fichier jamais ouvert : instantané des accès si
   l'outil le permet ; sinon par construction, établie par un essai consigné : le script ne contient nulle part la
   chaîne du nom du fichier de réponse, ni son préfixe `reponse-question` (`grep` sur le script : aucune occurrence), et
   il reconnaît la ligne « - réponse à la question : » par ce début seulement (E6) ;
5. l'extrait retiré → relevé écrit, `sources.extrait = absent`, tous les champs qui en viennent `absent`, aucune
   estimation ;
6. une ligne de `EMPREINTES-pilote-v1.txt` falsifiée → **refus** ;
7. `fin.reprise_attendue = oui` (cas simulé arrêté par `STOP` entre deux segments) → relevé écrit, et la garde G1 de
   l'assemblage le refuse ;
8. un relevé déjà présent sous le même nom → **refus** (R12) ;
9. une copie altérée du script (une ligne) → détectée par `sha256sum -c` de son compagnon avant toute exécution (R4) ;
10. un lien symbolique parmi les fichiers du dossier de course → **refus** ;
11. une ligne d'identité exigée retirée du `LANCEMENT.md` (par exemple « - lanceur : … ») → **refus**, code 3, motif : le
    nom du champ seulement ; aucun relevé écrit (D5, précision 2) ;
12. l'empreinte de la question remplacée par une autre empreinte → **refus**, code 3, motif `identite.question` ;
13. une ligne d'identité exigée répétée au segment 2 avec une autre valeur → **refus**, code 3, nom du champ ;
14. la ligne « - course v6.2 précédente : … ; lanceur attendu … » retirée d'une course S simulée → relevé écrit,
    `identite.porte_m_precedente = absent`, sans arrêt ;
15. la clé de course changée sur une seule des trois lignes qui la portent → **refus**, code 3, motif `releve.course`
    (E1) ;
16. le dernier élément du chemin du dossier du pilote remplacé par un nom autre que celui de la table pour la clé →
    **refus**, code 3, motif `releve.course` ; cas sain associé : le bon nom suivi de `-tentative2` → relevé écrit,
    `releve.course` sans le suffixe (E1) ;
17. une clé hors de la table close, la même sur les trois lignes → **refus**, code 3, motif `releve.course` (E1) ;
18. si la table de correspondance nomme un champ de lignée dans l'extrait : une lignée autre que celle de la table plantée
    dans ce champ → **refus**, code 3, motif `identite.lignee` ; la lignée de la table → relevé écrit,
    `identite.lignee_source = extrait` ; le champ retiré → relevé écrit,
    `identite.lignee_source = deduite_de_la_cle_controle_non_independant` (E1) ;
19. la ligne « - réponse à la question : » qui porte « aucune pièce archivée (…) » → relevé écrit,
    `unite.g001.question_servie = absent`, jamais `non` ; la ligne retirée → `absent` (E6).

## 7. Exécution

- **Qui écrit le script et ses essais** : conv-audit (pièce de la boucle), à partir de `releve_appels_simulation_v3.py`
  (`1e9df693…`) ou de zéro ; bibliothèque standard seule ; `python3 -I`.
- **Qui l'exécute sur une course réelle** : recommandé, session-depot, dans son conteneur, à la fin de chaque course, après
  le script de lecture, sur `$PILOTE` ou sur la copie du dossier poussé, puis pousse le relevé et son compagnon sans les
  afficher (même discipline que la sortie du script de lecture). Sinon, conv-audit, sur la copie poussée du dossier de
  course, après vérification de la liste fermée, sans afficher le relevé. Point à fixer par conv-audit (protocole v2,
  § 16).
- **Sortie standard** : une ligne, nom et empreinte du relevé. Codes : 0, 2 (usage), 3 (refus), 4 (erreur interne : type
  et ligne seulement).
- **Dossier d'audit** (protocole v2, § 12) : le relevé d'un dossier d'audit a le même format ; il est forgé par conv-audit
  (identité de l'objet réel, coûts et durées plausibles, faits plantés) par un script de forge empreinté, listé dans la
  liste d'audit ; il passe la même grammaire.

## 8. Ce qui reste à confirmer sur la structure réelle, avant la première lecture

- Les noms et la forme des champs de l'extrait mécanique et du journal d'appels (rôle, statut, coût, durée, unité,
  identifiant d'appel, source de recherche) : à lire sur les pièces de simulation de la série v13 (pas sur une course
  réelle sous la retenue), puis à écrire dans la table de correspondance.
- Si le noyau consigne hors de l'archive : la déclaration de fin de conception (ronde, critère, exemplaires) ; la validité
  et l'exécution d'un successeur muté ; les motifs de refus de l'architecte ; la restauration et la taille de la mémoire ;
  le nombre de castes. Chaque champ non consigné porte `absent`, et la fiche correspondante est « indécidable (non
  observable) » ; la liste des champs absents est la demande d'instrumentation de la ronde (registre v3).
- Le nom du manifeste de la course et la clé de la graine.
- La règle de dédoublonnage des appels relus entre segments (§ 5).
- Le nom de l'unité qui sert la question (g001 d'après le brouillon v5), pour `unite.<u>.question_servie`.
- **Lignes des champs exigés, écrites en simulation** (E1) : l'auteur du script confirme sur les séries v13 et v14 que
  chaque ligne qui porte un champ exigé est écrite en simulation — dont la ligne « - course : … ; dossier du pilote : … »
  (v10 l. 250 ; v11 l. 264) et la ligne « - préenregistrement : … » (v10 l. 512 ; v11 l. 529), écrite dans un bloc dont
  la condition n'est pas dans l'extrait des lignes des lanceurs — et que les valeurs simulées passent les règles du
  § 4.2 (clé égale sur les trois lignes et présente dans la table close ; dernier élément du chemin égal au nom de la
  table, suffixe `-tentative<N>` retiré). Sinon, conv-audit dit comment essayer les cas sains. L'auteur du script dit
  aussi si l'extrait mécanique porte la lignée, et sous quel champ (table de correspondance) ; sinon, la lignée est
  déduite de la clé (§ 4.2).
- Que les cas sains des séries v13 et v14 portent bien, à la ligne « - organisme : … ; question (<COURSE>) : sha256 … »,
  les empreintes réelles des questions M et S ; sinon les cas sains seraient refusés par la règle de `identite.question`,
  et conv-audit dit comment les essayer.

## 9. Champ → fiche (registre v4)

| champ | fiches |
|---|---|
| `releve.course`, `identite.*` | contrôle d'identité (registre, § 2, étape 1 ; protocole, § 9) |
| `fin.*`, `segments.*` | fin de course (garde G1) ; HC-P4-07 |
| `conception.declaration.*`, `unite.c….appels.role.calibrateur_interne` | HC-P4-01 (courses M et S : la ronde de la déclaration est exigée) |
| `conception.rondes_tournees`, `unite.c….statut`, `evenements.*`, `unite.g000.*` | HC-P4-01, voie « rondes tournées » : relances lancées après la poussée du registre v4 seulement (D3) |
| `mutation.<u>.*`, `fichier.<u>.politique_endogene` | HC-P4-03 ; fait rapporté de HC-P4-04 |
| `memoire.<g>.*` | HC-P4-05 |
| `castes.<g>.*`, `unite.g….appels.role.*` | HC-P4-06 |
| `unite.<u>.duree`, `unite.<u>.cout`, `unite.<u>.statut`, `evenements.*`, `course.*` | HC-P4-07 |
| `unite.<u>.appels.statut.*` | HC-P4-08 |
| `unite.<u>.appels.role.*`, `unite.<u>.recherches.*`, `unite.<u>.telechargements.*` | HC-P4-09 |
| `unite.<u>.question_servie`, `identite.question*` | § 0.9 du registre (ce que la question S change) |
