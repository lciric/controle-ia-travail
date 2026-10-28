# Spécification du relevé mécanique (B) d'une course du pilote 4 — v1

**Statut.** Version 1. Écrite le 26 octobre 2026 par un sous-agent neuf de la lignée conv-audit, sur le brief v3
(`82b9028d…`), en réponse au constat CLB-02 de la contre-lecture (le relevé n'existait pas, et toute la boucle en
dépend). Écriture achevée le 2026-10-26 à 04:51:15 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Pièce à
produire par conv-audit : un script empreinté, ses essais (R5 : un cas sain, des artefacts), son journal d'essais.
**La boucle extérieure ne démarre pas sans lui** (protocole v2, § 1). Aucun fichier de course réel, aucun extrait, aucun
journal d'appels n'a été ouvert pour écrire cette spécification : la structure réelle des sources est à confirmer (§ 8).

## 1. Ce qu'est le relevé, et ce qu'il n'est pas

- Le relevé (B) est un fichier texte par course, `releve-mecanique-<dossier>-v1.txt`, où `<dossier>` est le nom exact du
  dossier de course poussé par session-depot (pour la course M : `pilote4-gemini-v6-2-v1-tentative2`). Il a un compagnon
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
4. `LANCEMENT.md` : identité (commit, arbre, nombre de fichiers, lanceur, noyau, banque, texte, question), segments, graine
   du manifeste s'il la recopie.
5. Le manifeste de la course (`manifeste*.json` ou le nom que le lanceur lui donne) : graine, versions.

Il **n'ouvre jamais** : `ferme.tar.gz` (haché seulement) ; `reponse-question*` ; tout fichier de banque
(`banque-confrontation-v*.json`, `*-secret.json`, `*-cle.json`) ; `P3-consignes-v1.md`, `textes-actions-…` ; aucun
dossier `donnees/`, `runs/`, `diag/`. Il ne suit aucun lien symbolique. Il n'exécute rien du lanceur ni du noyau.

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
releve.course = <identifiant>|absent        # nom du texte (LANCEMENT.md ou manifeste)
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
identite.commit = <commit>|absent
identite.arbre = <empreinte>|absent
identite.nb_fichiers = <entier>|absent
identite.graine_manifeste = <entier>|absent
identite.lanceur = <identifiant>|absent
identite.lanceur_empreinte = <empreinte>|absent
identite.noyau = <commit>|absent
identite.banque_empreinte = <empreinte>|absent
identite.texte_empreinte = <empreinte>|absent
identite.question = <identifiant>|absent    # m ou s (nom court), jamais un texte
identite.question_empreinte = <empreinte>|absent
identite.lignee = <identifiant>|absent
```

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
unite.<u>.question_servie = oui|non|absent
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
d'entraînement). Si la déclaration n'est consignée nulle part hors de l'archive, les trois champs portent `absent` et la
fiche HC-P4-01 se lit par `rondes_tournees` seul (registre v3).

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

**Cas sain** : les pièces des quatre cas sains de la série v13 (`simulation-lanceur-v10/` : v6.2.1 continue ; v5.3
continue ; v6.2.1 en deux et en trois segments ; `LANCEMENT.md`, extraits, journaux d'appels de simulation, jamais
`ferme.tar.gz`). Attendu : un relevé écrit par cas ; les comptes égaux à ceux du relevé de la série v13
(`releve-serie-v13-v1.txt`, `e99c1a48…` : c001 7 appels dont 1 de mutation ; g000 123 ; g001 129 ; g002 123 ; g003 124 dont
1 de mutation ; tous `ok` ; segments en deux et trois : mêmes nombres, 7 appels et 0,0947 USD puis 130 appels et
1,9544 USD relus, sans double compte) ; deux exécutions donnent deux relevés identiques (hors `releve.heure`) ; la sortie
standard porte une ligne (`relevé écrit : <fichier> <empreinte>`), sans aucun motif `[0-9][.,][0-9]`.

**Artefacts** (chacun sur une copie d'un cas sain, dans un dossier de travail effacé ensuite) :
1. un champ de texte planté dans l'extrait (une phrase avec espaces) sur un champ de la table → **refus**, code 3, aucun
   relevé écrit, la phrase absente de la sortie d'erreur ;
2. un champ nommé `score` planté avec un décimal → non recopié, `champs_ignores` augmenté de 1, relevé écrit, le décimal
   absent du relevé (`grep`) ;
3. un décimal sans unité planté sur un champ de coût → **refus** ;
4. un fichier `reponse-question-g001.md` planté, qui porte un marqueur choisi par l'auteur de l'essai → le marqueur
   absent du relevé, de la sortie standard et de la sortie d'erreur ; le fichier jamais ouvert (instantané des accès si
   l'outil le permet, sinon par construction : aucun motif de nom `reponse-question` dans le script) ;
5. l'extrait retiré → relevé écrit, `sources.extrait = absent`, tous les champs qui en viennent `absent`, aucune
   estimation ;
6. une ligne de `EMPREINTES-pilote-v1.txt` falsifiée → **refus** ;
7. `fin.reprise_attendue = oui` (cas simulé arrêté par `STOP` entre deux segments) → relevé écrit, et la garde G1 de
   l'assemblage le refuse ;
8. un relevé déjà présent sous le même nom → **refus** (R12) ;
9. une copie altérée du script (une ligne) → détectée par `sha256sum -c` de son compagnon avant toute exécution (R4) ;
10. un lien symbolique parmi les fichiers du dossier de course → **refus**.

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

## 9. Champ → fiche (registre v3)

| champ | fiches |
|---|---|
| `identite.*` | contrôle d'identité (§ 2, étape 1) |
| `fin.*`, `segments.*` | fin de course (garde G1) ; HC-P4-07 |
| `conception.rondes_tournees`, `conception.declaration.*`, `unite.c….appels.role.calibrateur_interne` | HC-P4-01 |
| `mutation.<u>.*`, `fichier.<u>.politique_endogene` | HC-P4-03 ; fait rapporté de HC-P4-04 |
| `memoire.<g>.*` | HC-P4-05 |
| `castes.<g>.*`, `unite.g….appels.role.*` | HC-P4-06 |
| `unite.<u>.duree`, `unite.<u>.cout`, `unite.<u>.statut`, `evenements.*`, `course.*` | HC-P4-07 |
| `unite.<u>.appels.statut.*` | HC-P4-08 |
| `unite.<u>.appels.role.*`, `unite.<u>.recherches.*`, `unite.<u>.telechargements.*` | HC-P4-09 |
| `unite.<u>.question_servie`, `identite.question*` | § 0.9 du registre (ce que la question S change) |
