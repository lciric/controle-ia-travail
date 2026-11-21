# Rapport du développeur — véhicule NA-1, lots 1 (tirage) et 2 (garde de motifs) — v2

- Développeur des lots 1 et 2 du véhicule NA-1, modèle O ; le même que pour la v1.
- Date (UTC) : 2026-11-21 ; runs finaux lancés à 08:45:32Z (`date -u`).
- La v2 remplace la v1 : `…/scratchpad/dev-vehicule-na-lots-1-2/rapport-developpeur-lots-1-et-2-na-v1.md`, `960845dbccc7ceee944b85d91adf65715e5553430341f0863bdd07347be21214`. Le dossier de la v1 reste en l'état, sans modification (table `310cc708…`).
- Objet : le verdict provisoire « À corriger » du vérificateur (modèle S), transmis par la coordination. Ses trois pièces ont été lues en entier, par leur chemin complet : `…/scratchpad/verif-vehicule-na-lots-1-2/mutations_verificateur.py`, `sondes_verificateur.py`, `journal-mutations-rejoue.json`. Neuf de ses 35 mutations survivaient : X-03, X-05, X-07, X-08, X-11, X-20, X-30, X-32 et X-33.
- Mêmes règles que pour la v1 : processeur seul ; aucun appel, aucune clé, aucune dépense ; aucune écriture dans un dépôt, aucun commit ; données factices seules. Aucun refus de permission, de classifieur ni de garde rencontré. Aucune commande de liste hors de mon dossier ; ni `git ls-tree`, ni `git show` d'un dossier, ni `git fetch` dans cette session v2.

## 1. Verdict

Les huit points demandés sont portés. **Essais : 92 passés, 0 échec** (lot 1 : 61 ; lot 2 : 31). **Mutations : 77, toutes tuées** : les 42 du développeur et les 35 du vérificateur. Le témoin non muté passe ; le témoin inerte survit, comme il le doit.

## 2. Correction par correction

| point | lieu, v1 → v2 | ce qui est fait | essai v2 | mutation tuée |
|---|---|---|---|---|
| X-03 | `tirage_na_v1.py:172` → `tirage_na_v2.py:176` | essai sur une légende dont le rang 0 de l'axe 1 vaut « menace factice zero » : refus nommé, au niveau de la légende puis du tirage | `test_na_v2_tirage.py:557` | X-03 |
| X-05 | `:296` → `:300` (`sortie`) | dans un tirage factice, deux cases servies reçoivent le même mot : au départ, `sortie` refuse avec la cause « identifiant en double » | `:567` | X-05 |
| X-07 | `:333` → `:337` | une ligne finie par « \n », puis une qui porte un « \r » : cause « fin de ligne » | `:579` | X-07 |
| X-08 | `:339` → `:343` | une ligne en « Case : » (C majuscule), puis en « case: » (sans espace) : cause « forme » | `:584` | X-08 |
| X-11 | `:370` → `:374` | générations 0, 4 et "1" (une chaîne) : arrêt n° 10, cause « génération hors de 1 à 3 » | `:590` | X-11 |
| X-20 | `:430` → `:434` | un manifeste existant, sans sortie : refus (R12), aucune sortie écrite, manifeste intact à l'octet | `:597` | X-20 |
| X-33 | `garde_motifs_na_v1.py:240` → `garde_motifs_na_v2.py:245` | une requête qui porte un motif de chaque famille. Dans le texte, la famille 2 vient d'abord, et le rang 3 de la famille 1 précède son rang 1. Constat rendu : famille 1, rang 1. Sans motif de la famille 1 : famille 2, plus petit rang | `test_na_v2_garde_motifs.py:271` | X-33 |
| X-30 | `:297` → `:293` à `:309` | la comparaison `verifier_avant_envoi(rg, rg.octets)`, qui comparait la copie à elle-même, est **retirée** de `envoyer_apres_garde`. Le code et ce rapport disent que la vraie égalité est au lot 4 (conception v4, § 2.3, pas 5) : la surcharge d'`appel` y appelle `verifier_avant_envoi` (`:284`) sur les octets qu'elle remet au noyau. La fonction reste exposée et éprouvée | `:293` | X-30 est sans objet ; l'adaptée X-30b, qui retire l'égalité de `verifier_avant_envoi`, est tuée |
| X-32 | `:274` → `:274` et `:275` | l'empreinte est prise sur la copie, au moment même de la copie ; le tampon de l'appelant est lu une seule fois. L'essai passe un tampon dont la seconde lecture rendrait d'autres octets | `:284` | X-32b, l'adaptée sur le texte v2 (seconde lecture du tampon de l'appelant) |

Changements de code, en plus des essais : `garde_motifs_na_v2.py` (X-30, X-32) ; `tirage_na_v2.py`, dont aucune règle ne change, seuls le nom de version et l'import de la garde v2 changent. `identifiants_na_v1.py` et `liste-motifs-essai-na-v1.json` sont repris à l'octet.

## 3. Mutations rejouées

Programme : `paquet/orchestrator/essais/mutations_na_v2.py` ; journal : `journal-mutations-na-lots-1-2-v2.json`.

- **Développeur : 42 sur 42 tuées**, visées sur les fichiers v2. Deux sont adaptées au texte v2 et portent le suffixe « b » :
  - L2-10b : la copie défensive retirée (la ligne porte un commentaire en v2) ;
  - L2-15b : l'envoi déplacé avant la ligne de journal (le texte v2 n'a plus la comparaison à soi-même).
- **Vérificateur : 35 sur 35 tuées**, jouées comme il le fait, sur les deux fichiers d'essais entiers ; 33 sont à sa lettre exacte, deux sont adaptées :
  - X-30b, parce que X-30 est sans objet (le contrôle qu'elle retirait n'existe plus) ;
  - X-32b, parce que la ligne visée par X-32 a changé.
  Les neuf qui survivaient sont tuées : X-03, X-05, X-07, X-08, X-11, X-20, X-30b, X-32b, X-33.
- **Témoin non muté** : les deux fichiers d'essais passent (code 0). **Témoin inerte** (un mot de docstring changé) : survit (code 0), comme attendu.
- Une ébauche de ce run avait adapté X-35 en « X-35b », cherchant l'échappement `−`. Le source porte le caractère du signe moins lui-même : l'ébauche a dit la mutation invalide. La version finale joue X-35 à la lettre du vérificateur, et elle est tuée. L'ébauche de journal, hors de mon dossier, est retirée.

## 4. Essais et application

`/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -v -p no:cacheprovider …/paquet/orchestrator/essais` donne 92 passés (journal `journal-essais-na-lots-1-2-v2.txt`). Les essais neufs :
- lot 1, 6 : X-03, X-05, X-07, X-08, X-11, X-20 ;
- lot 2, 3 : X-33, X-32, X-30.

Le paquet a ensuite été posé, par son programme, dans une copie neuve du dossier `orchestrator` du commit `a41b7b50…`, hors de mon dossier (`…/scratchpad/copie-orchestrateur-na-lots-1-2-v2/`) : 92 passés. Une seconde application sur la même copie est refusée (« cible déjà présente », R12). Le dépôt de l'orchestrateur est resté propre.

## 5. Ce que la lettre ne fixe pas (remarques ; rien n'est tranché dans le code)

Points renvoyés à l'additif par le vérificateur, cités ici sans décision :

1. **La définition d'un « caractère invisible ».** La garde retire la catégorie Unicode « Cf ». Les sondes du vérificateur (`sondes_verificateur.py`, § 5) montrent que d'autres caractères restent dans le texte et y coupent un motif : le sélecteur de variation U+FE0F, le joint de graphèmes U+034F, le remplisseur U+3164 et le braille vide U+2800.
2. **Espace et tiret.** « Espaces et tirets ramenés à une seule forme » est lu comme deux formes : une espace, et le tiret « - ». Ainsi « graine-factice » ne mord pas sur « graine factice ».
3. **Le texte trouvé dans la ligne « non envoyé » du journal** : il est pris dans le texte normalisé, et il est écrit au journal, qui est en quarantaine (V9, l. 387).
4. Les points 2 à 5 et 7 du rapport v1, repris ici :
   - l'écriture d'un rang en mot de trois syllabes ;
   - l'ordre des onze cases d'une génération (ordre du tirage) ;
   - la lecture « cases servies » et le rang de la menace « sabotage » pour la clé 30 ;
   - la forme de la ligne de case, proposition du concepteur non fixée par l'additif ;
   - le format de la liste des motifs.

Les autres remarques du rapport v1 tiennent toujours : 1, l'encodage au lot 1 ; 8, le texte trouvé normalisé ; 9, le mot de case passe la garde seul ; 10, la clé 20 pour n ≤ 60 ; 11, le gabarit réel jamais passé au programme ; 12, la liste exigée par le programme du tirage ; 13, le programme d'application ne clone pas.

## 6. Interface pour les lots 3 et 5

Elle est celle de la v1 (rapport v1, § 7), aux noms de modules près : `tirage_na_v2`, `garde_motifs_na_v2`, `identifiants_na_v1`. Un seul changement : `envoyer_apres_garde` ne rejoue plus d'égalité. **Le lot 4 doit appeler `garde_motifs_na_v2.verifier_avant_envoi(requete_gardee, octets)`** sur les octets qu'il remet à `super().appel`. `RequeteGardee.sha256` est l'empreinte de la copie que la garde a lue.

## 7. Livré

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lots-1-2-v2/`. Chaque fichier a son compagnon `.sha256` ; la table d'empreintes du dossier est `table-empreintes-dossier-na-lots-1-2-v2.txt`.

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/identifiants_na_v1.py` (inchangé) | `38d9860b7535e24b5ba707560f9dd5c4a27acc6e5632e453308a3fd2b93909dd` |
| `paquet/orchestrator/pole/tirage_na_v2.py` | `69230783d5effb98dbad97a1e1fbea97a06ab8b769a9a2a3bfd7ce6f101357de` |
| `paquet/orchestrator/pole/garde_motifs_na_v2.py` | `1e4fe266c25aa6dc7b3fcf5441e293a38d91d9c7a1372ef8f4f846ed1b82e127` |
| `paquet/orchestrator/essais/aides_na_v2.py` | `1943d30e8c17726ffc9230dabf69dadb2f4c279fa4b0b45073b599c9acc6d0c6` |
| `paquet/orchestrator/essais/liste-motifs-essai-na-v1.json` (inchangé) | `41a50329f67c41d073115a75ae64981fd59a46b4663c269f42a32b4055c0508b` |
| `paquet/orchestrator/essais/test_na_v2_tirage.py` | `d8c2e5bbaa8820f2ccadee1d3f4fb2a7d7865786723e882c393937ad2e31386e` |
| `paquet/orchestrator/essais/test_na_v2_garde_motifs.py` | `75de933c677f08342ecd21599cf6c32f286fbc295062638bcab86180b8d8db24` |
| `paquet/orchestrator/essais/mutations_na_v2.py` | `882f05ac0e96196db3f2ca31c6b169fad2d40a49d42578460d665004c49bba3e` |
| `manifeste-paquet-vehicule-na-lots-1-2-v2.json`, `appliquer_paquet_vehicule_na_lots_1_2_v2.py`, `journal-essais-na-lots-1-2-v2.txt`, `journal-mutations-na-lots-1-2-v2.json` | voir la table d'empreintes |

— développeur des lots 1 et 2 du véhicule NA-1, modèle O
