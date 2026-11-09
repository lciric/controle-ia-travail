# Consigne : audit de l'écart DT-4 de la course 7a (décision (b) de Lazar, R-2048) — v1

Session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, 2026-11-09 vers 22:00 UTC (`date -u`). Destinataire : un sous-agent **neuf** (auditeur), qui n'a écrit ni lu aucune pièce de T0.6, T0.7, P3-bis ni de 7a avant cette tâche. Après cet audit, l'auditeur n'a aucun rôle sur T0.6, T0.7, P3-bis ni G0.

Dépôt : `/home/user/controle-ia-travail` (clone de `lciric/controle-ia-travail`, `main` local à `6886b61e`). `PYTHONPATH=src`. Python : `python3` (bibliothèque standard suffit).

## Interdits (recopiés de `interdits-communs-v1.md`, même dossier)

1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) : `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` ; la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` ; tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3` ; `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` ; les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. Secrets : jamais une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
3. Aucun appel de modèle ni d'interface externe, aucune location, aucun `vastai`, aucune dépense.
4. Git : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; autres commits par `git show <commit>:<chemin>` seulement. Rien écrit hors des chemins de sortie ci-dessous.
5. Pas de suite complète des essais.
6. Refus d'un contrôle de permissions ou d'un classifieur : s'arrêter sur ce point, le rapporter tel quel.
7. Heures relevées par `date -u`.

## Question (R-2048)

Rien de la lecture B de 7a ni de `lecture-sondes-t06.json` de 7a a-t-il atteint `main`, un rédacteur ou un contre-lecteur ? L'écart lui-même est décrit, **en catégories et sans valeur**, par `registres/decisions.md` R-2040 et R-2041 : le lecteur exploratoire de 7a a vu des valeurs du fichier des sondes ; sa lecture B ne porte aucune aire, aucun score ni rang, mais quatre éléments tirés de ce fichier.

## Limite imposée (à déclarer en tête du rapport)

Par le brief de Lazar du 9 novembre (21:5x UTC), personne n'ouvre `lecture-sondes-t06.json` ni la branche de quarantaine avant le verdict scellé de P3-bis. L'audit est donc **structurel et par catégories** : il ne compare aucune valeur du fichier des sondes au texte de `main`. Le rapport dit ce que cette limite laisse ouvert et ce qu'il faudrait pour le fermer (comparaison mécanique aveugle, qui demanderait un mot de Lazar).

## Ce qu'il faut faire

Écrire d'abord un script, puis le rapport.

**Script** `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1/verifier_ecart_dt4_v1.py` (sortie JSON `…/audit-ecart-dt4-7a-v1/sortie-verifier-ecart-dt4-v1.json`). Il n'imprime et n'écrit **que** des comptes, des chemins, des numéros de ligne, des identifiants de commit et des catégories ; jamais le texte d'une ligne. Il prend en argument la plage de commits et une liste de fichiers, pour que la mère le rejoue plus tard sur d'autres pièces (complément : contre-lecture 3 de la r3 et dossier (ii-b), à venir). Contrôles :

1. **Chemins** : pour chaque commit de `9b7721c7..6886b61e` (13 commits ; liste par `git log --format=%H 9b7721c7..6886b61e`), fichiers ajoutés, modifiés, supprimés (`git diff --name-status`) ; aucun chemin ne doit correspondre à `lecture-sondes*`, à `diag/20261109-070232-t06-reel/`, à `runs/20261109-070232-t06-reel/`, ni à un nom de la lecture B (cherchez les noms et empreintes de B **dans les registres et messages de commit de `main` seulement** : R-2040, R-2041, `e712f61a`, `39f17d33` ; s'ils n'y sont pas, le dire) ; si des empreintes de B figurent sur `main`, vérifier qu'aucun fichier de l'arbre de `6886b61e` n'a ces empreintes.
2. **Commit de quarantaine** : aucun commit de la plage ne commence par `e6c06113` ; `git log --format=%H 9b7721c7..6886b61e` suffit (créé après `9b7721c7`, il apparaîtrait dans la plage s'il était atteignable depuis `main`). Ne pas récupérer ce commit.
3. **Catégories** (sur les lignes **ajoutées** de chaque commit de la plage, puis sur le texte entier des pièces nommées au point 4) : C1 aires, bornes ou `pli0` des jeux de contrôle, décisif ou de validité de 7a ; C2 états « au-dessus / non au-dessus » de ces jeux ou des lectures T6-3 à T6-9 de 7a ; C3 « audit des sondes » déclenché ou non pour 7a ; C4 identité, famille ou couche de la sonde décisive **comme résultat de 7a** ; C5 durées par couple ou essais de Mahalanobis de 7a ; C6 tables B et C « suspendues » ; C7 courbe, T6-6, `verdict_p3bis` de 7a. Motifs larges (par exemple `aire|AUC|pli0|au-dessus|T6-[3-9]|audit des sondes|sonde décisive|famille|couche|Mahalanobis|tables? B|verdict_p3bis|lecture-sondes`), puis classement de chaque occurrence par vous, à la lecture du contexte : (i) description de l'écart en catégories (permis, forme de R-2041) ; (ii) texte de conception antérieur à 7a ou indépendant de ses résultats (le montrer : même texte avant `9b7721c7`, ou dans la révision 2 de T0.6 au commit `8cb539f9`) ; (iii) transfert possible d'un résultat de sonde de 7a → constat. Le script écrit la liste (chemin, ligne, catégorie, classement) ; le rapport ne cite **aucun nombre** d'une occurrence classée (iii).
4. **Pièces nommées** (texte entier) : `brouillons/T0.6-organismes-v0-v1-candidat12-r3.md` (`c24e268e…`) ; son journal `…-candidat12-r3-journal-v1.md` (`0728c7ed…`) ; différence révision 2 (`git show 8cb539f9:brouillons/T0.6-organismes-v0-v1-candidat12-r2.md`, `0d6bf1c4…`) → révision 3, limitée aux catégories ; `docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A-exploratoire-non-opposable-v1.md` (`3c84c419…`) et `…/garde-equivalence-20261109-070232-t06-reel-exploratoire-non-opposable-r522.json` (sortie de l'extracteur) ; `registres/decisions.md` R-2037 à R-2051 ; l'en-tête de `registres/etat.md` ; `registres/passations/2026-11-09-2117.md` ; `docs/procedures/brief-reprise-nouvelle-mere-2026-11-09-v1.md` ; les consignes de cette série (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-09-2200-v1/`) : elles ne doivent contenir aucune valeur ni élément de B, et nommer les fichiers interdits.

**Points de jugement, au rapport** :

5. **Lecture A** : écrite par le même lecteur que B (R-2040, R-2041) ? Avant ou après qu'il voie le fichier des sondes (heures de son en-tête, commits `a4d504a8`, `39f17d33`, `e712f61a`, textes de R-2039 à R-2041) ? Contient-elle un élément C1 à C7 ? L'extracteur des mesures (`extraire_mesures_epreuve_t06_v1.py`, `9a67b7b9…`, au commit `1609a4bf`, lisible par `git show 1609a4bf:<chemin>` ; trouver le chemin par `git ls-tree -r --name-only 1609a4bf | grep extraire_mesures`) lit-il le fichier des sondes ? (R-2040 : liste blanche, il ne lit jamais les aires : le vérifier sur le code.) Si l'ordre ne peut pas être établi, réserve écrite.
6. **Rédacteur de la r3** : d'après son journal et R-2046, qu'a-t-il reçu ? (Lecture A, grandeurs de coût du compte rendu de 7a, champ `graines[*].entropie` du manifeste de 7a.) Rien de B, rien du fichier des sondes ? Le différentiel r2 → r3 contient-il un élément C1 à C7 de 7a ?
7. **Session mère sortante** : son attestation (passation `2026-11-09-2117.md` § 2.1 : consignes sans valeur ni élément de B, fichiers interdits ; aucune valeur vue) est consignée comme **attestation**, non vérifiable au-delà de ce que le dépôt montre.
8. **Contre-lecteurs** : la contre-lecture 2 (`docs/notes/g0-deux-semaines-v1/contre-lecture-t06-course-v2/contre-lecture-t06-course-v2-v1.md`) est-elle antérieure à 7a (heure, commit) ? La contre-lecture 3 de la r3 et le dossier (ii-b) n'existent pas encore : ils seront couverts par un complément (le script rejoué), avant le scellement de la r3.

## Sorties

- Rapport `docs/notes/g0-deux-semaines-v1/e3-ter-v1/audit-ecart-dt4-7a-v1.md` : en tête, la limite imposée ; puis verdict en une ligne (« aucune trace trouvée » / « trace trouvée » / « indéterminé »), constats numérotés, réserves, ce qui reste ouvert, liste des pièces lues avec leurs empreintes vérifiées, déclaration des interdits tenus.
- Script et sortie JSON ci-dessus.
- Compagnons `.sha256` de chacun (format `empreinte  nom_de_fichier`, comme les compagnons du dépôt ; `PYTHONPATH=src python3 -m controle_ia.scellement sceller FICHIER` les écrit).
- Ne rien committer. Rendre à la mère : chemins, empreintes, verdict en une ligne, réserves.
