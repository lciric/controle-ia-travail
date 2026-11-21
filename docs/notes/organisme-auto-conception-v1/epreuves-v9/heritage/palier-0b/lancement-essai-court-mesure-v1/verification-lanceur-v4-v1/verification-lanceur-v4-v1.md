# Vérification hostile du lanceur v4 de l'essai 3 — palier 0b — v1

**Verdict : Conforme, avec une réserve non bloquante.** La liste de référence est bien celle du commit `d7f949ac…18c3` (refaite par une voie à moi, égale à l'octet). Un lien symbolique, un fichier en trop ou caché, un fichier modifié avec la liste refaite sont tous refusés sur ma propre copie par `git archive` ; la commande reste égale à l'octet. Réserve : la voie « avec `.git` » reste plus faible et un `.git` ajouté à la copie la choisit : un lien et un fichier non suivis y passent (démontré). Ma réserve (a) de la v3 est donc levée pour la copie sans `.git`, qui est la forme prévue par le devis.

Pièces (sha256 relevés, égaux au rapport) : lanceur v4 `b989db6e…5865` ; départ v4 `64b2c0ce…5937` ; script de fabrication `857b5138…0533` ; liste de référence `ab90e73b…91b4` ; devis v5 `452e7bcf…47fb` ; vérificateur de commande v3 `ca93ea3a…051e` ; complément 1 v3 (pièce d'origine, `git show` redirigé) `56ed20f8…b867`. Diffs relus en entier : lanceur v3 → v4 (contrôles de la copie remplacés, rien d'autre), départ v3 → v4 (seul le nom du lanceur lancé). Le gardien v4 n'est pas touché. Dossier d'essai : sous-dossier neuf `v5/` de mon dossier.

## Les quatre questions

| # | Question | Rendu | Preuve |
|---|---|---|---|
| 1 | la liste de référence est-elle celle du commit ? | **Oui** | `ma-reference.py` : `git ls-tree -r -z` puis `git cat-file --batch` (lecture seule), sha256 en Python, tri par octets des chemins « ./… », format `sha256sum`. Résultat : 35 732 fichiers (35 567 en 100644, 165 en 100755), aucune entrée non régulière, aucun sous-module, aucun nom à barre oblique inverse ou saut de ligne, aucun des deux fichiers exclus dans l'arbre, `.gitattributes` = `* -text` et types binaires (aucun `export-ignore` ni `export-subst`). `cmp` avec la liste de l'auteur : égale à l'octet ; sha256 de ma liste `ab90e73b0c824544150f450819a38c7db76dd1cac505942fd66b5375f96591b4`, égal à `REFERENCE_ATTENDUE` du lanceur (l. 67). |
| 2 | lien, fichier en trop ou caché, fichier modifié avec liste refaite : refusés ? | **Oui, tous** (copie sans `.git`) | Ma copie par `git archive` du commit (35 734 fichiers avec les deux fichiers de la copie, ma liste dedans), `art.sh`, lanceur en `--verifier-seulement` aux valeurs d'emploi sans aucun remplacement : copie saine 0. Refusés 12 : lien vers un fichier, lien vers un dossier, lien brisé caché, fichier en trop, fichier caché profond (`.cache/a/b/.cache`), fichier caché à la racine, nom avec saut de ligne, lien dur ajouté, fichier modifié (liste intacte, puis **liste refaite** : refus car la liste n'est plus la référence), programme modifié (liste intacte, puis liste refaite), fichier supprimé (liste intacte, puis refaite), fichier remplacé par un lien de même contenu, tube nommé, liste altérée d'un octet, racine en lien ; commit en lien : 11 ; copie saine de nouveau 0. Tenue placée dans la racine : 12 (refus sûr). **Limites attendues, déclarées par l'auteur, confirmées** : un changement de mode (`chmod +x`), un `touch` aux mêmes octets, un dossier vide ajouté rendent 0. |
| 3 | commande égale à l'octet | **Oui** | Statique : `verifier-commande-v3.py` sur le lanceur v4 : « ÉGAL », ligne de 506 octets, `2966b8d8…9d7c` (= le lanceur v3). Dynamique : `cmd-test.sh` (mon script, valeur attendue calculée du seul complément) : lanceur v4 lancé en emploi sur ma copie, interprète factice : cwd, `PYTHONPATH` et arguments ÉGAUX. Artefact à moi : copie du lanceur v4 avec `-B` changé en `-b` : vérificateur « ÉCHEC », « première différence à l'octet 126 ». |
| 4 | la v4 casse-t-elle autre chose ? | **Non, une réserve** | (i) **Réserve démontrée** (`gitbypass.sh`) : copie de ma copie avec un `.git` (clone à moi, HEAD sur le commit, index lu de l'arbre) : la voie « avec `.git` » (inchangée, l. 124-136) s'applique : saine 0 ; fichier suivi modifié 12 ; **lien non suivi ajouté 0 ; fichier non suivi ajouté 0** (`--untracked-files=no`). Sans `.git` les deux sont refusés. Conseil : refuser une racine qui porte un `.git` quand on attend la forme copie, ou appliquer les contrôles de la copie dans les deux formes. (ii) Le code 13 n'est plus atteignable sur copie (un programme altéré rend 12, écart 2 de l'auteur) : voulu, sans effet sur la sûreté. (iii) Chaque contrôle lit environ 3,6 Go deux fois (4 s ici) ; dossier de tenue à part toujours exigé en `--verifier-seulement` (code 4 ensuite). (iv) Le départ v4 et le gardien : diff relu, rien d'autre. |

## Relevé de méthode

**Chaîne de raisonnement.**
1. Pièces lues, empreintes relevées, diffs v3 → v4 relus ; devis v5 et complément relus pour ce que la v4 doit tenir.
2. Question 1 : liste refaite par `ma-reference.py`, sans `git archive` ni `find` ni `sha256sum`, donc par une voie indépendante de la recette du lanceur ; `cmp` ; recherches de cas pièges dans l'arbre (modes, liens, noms spéciaux, attributs d'export).
3. Question 2 : ma copie par `git archive` ; 25 cas fabriqués par `art.sh` sur cette copie, mutation puis restauration ; liste refaite par la recette du lanceur pour les cas « liste refaite ».
4. Question 3 : vérificateur statique, essai dynamique à moi, lanceur altéré d'un octet.
5. Question 4 : lecture des diffs ; `gitbypass.sh` pour la voie « avec `.git` ».
6. Supposé : le comportement de `git archive` sur le serveur de destination (tar, locale) ; la copie réelle envoyée sera faite par la même recette.

**Objets de contrôle.**
- Liste de référence : vrai par construction (la liste de l'auteur doit égaler celle que mon autre voie produit) → égale ; faux (liste altérée d'un octet, essai de l'auteur relu, et le mien) → refusée par le lanceur.
- Contrôle de copie : faux par construction (lien, ajout, ajout caché, modification liste refaite, suppression, tube, racine en lien) → refus 12 chacun ; vrai (copie saine) → 0 trois fois. Cas où le mécanisme devait échouer et a échoué : `.git` ajouté avec lien ou fichier non suivi (0 au lieu de 12), mode et dossier vide (limites déclarées).
- Commande : faux (`-b`) → différent ; vrai → égal.

**Premier pas non justifié.** Pas 6 : conduite de `git archive`, `tar` et du tri sur le serveur (locale, version) ; ce qui le justifierait : refaire la liste sur le serveur par la recette écrite, avant le départ (le lanceur le fait) ; un écart ferait refuser 12 (refus sûr).

**Mode d'échec affecté.** Réponse : 1 oui (égalité à l'octet) ; 2 oui, tous refusés (l. 147-170) ; 3 oui (l. 199 inchangée) ; 4 non, réserve sur la voie `.git` (l. 124-136).

**Dérivation de l'énoncé seul.** Sans objet : je suis vérificateur.

**Trouvaille de côté.** (a) La recette de fabrication du lanceur v4 (`LC_ALL=C`) donne la même liste que ma voie par `ls-tree`/`cat-file` : le tri en octets des chemins suffit à reproduire `sort -z` en locale C. (b) Le commit `d7f949ac` n'est sur aucune branche locale du dépôt (un clone n'en reçoit pas les objets ; il faut un fichier d'objets partagés) : sans effet sur la copie, qui sort de `git archive`.

**Évaluateur et conseil.** Ce qui juge mon produit : la session, puis mes essais à vrai et faux construits. Mon verdict pourrait être bon sans le mériter : ma copie vient de la même commande `git archive` que celle de l'auteur ; mes mutations sont celles auxquelles je pense ; modes et dossiers vides non vérifiés par construction ; le vrai programme n'est pas lancé. Je n'ai pas rejoué les 61 cas de l'auteur. Aucune écriture hors de mon dossier ni dans le dépôt (lecture seule : `ls-tree`, `cat-file`, `archive`, `show` ; un clone partagé écrit dans mon dossier) ; aucun commit ; aucune dépense ; aucun processus lancé hors des essais de lanceur en `--verifier-seulement` ou avec interprète factice.
