# Rapport de l'auteur — lanceur v4 de l'essai 3 du palier 0b — v1

Cette pièce corrige la réserve (a) de la vérification du lanceur v3 et du gardien v4 (`verification-lanceur-v3-gardien-v4-v1/…`, « Conforme »), sur la demande de la mère transmise à 18:59Z.

- Le gardien v4 ne change pas (`ba39fe9b…46ed`), ni son script de départ.
- Dossier (L) : `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-lanceur-v3-gardien-v4/lanceur-v4/`.
- Je n'ai lancé que des factices, jamais le vrai programme : un interprète factice remplace l'interpréteur.
- Le dépôt `/home/user/controle-ia-travail` a été **lu seulement** : `git archive`, `git ls-tree`, `git cat-file`.
- Rien n'est écrit sous `/home/user/palier-0b-racine/` ni sous `/home/user/journaux-palier-0b-essai-court-v1/`.
- Aucun commit du programme, aucune dépense, aucun refus de permission.

## Fichiers et empreintes (compagnon `.sha256` à côté de chacun)
| Pièce | sha256 |
|---|---|
| `lancer-essai-3-v4.sh` | b989db6e2e17772b74ec8ac99a5ed2708bf305d212a5e6825ed210759b7b5865 |
| `demarrer-essai-3-v4.sh` (= v3, seul le nom du lanceur lancé change) | 64b2c0ce03e1e586547580cbed62f8e8c84bbd798c695a588202955809105937 |
| `fabriquer-liste-reference-v4.sh` | 857b5138c77c1b80672718c2235a6c687185d0cc5fd93eafa5216cd48d850533 |
| `reference/EMPREINTES-DE-REFERENCE-d7f949ac.txt` (**liste de référence**) | **ab90e73b0c824544150f450819a38c7db76dd1cac505942fd66b5375f96591b4**, **35 732 fichiers** (35 567 en mode 100644 et 165 en mode 100755 ; aucun lien, aucun sous-module dans l'arbre ; `.gitattributes` sans attribut d'exportation) |

**Vérificateur de commande.** Le vérificateur reste `verifier-commande-v3.py` (`ca93ea3a…051e`), dans le dossier parent. La ligne `env -C` du lanceur v4 est égale à l'octet à celle du v3.

**Copie prête.** `reference/arbre/` est l'arbre du commit extrait par `git archive`, plus `COMMIT-DE-LA-COPIE.txt` et `EMPREINTES-DE-LA-COPIE.txt`. C'est la copie telle qu'elle doit arriver au serveur. Après les essais, sa liste a bien l'empreinte `ab90e73b…`. Elle pèse 3,6 Go et peut être supprimée.

## Ce qui change (racine sans `.git` seulement ; diff v3 → v4 relu en entier)
1. **Aucun lien symbolique ni fichier spécial dans la copie.** Le lanceur cherche toute entrée qui n'est ni un dossier ni un fichier régulier (`find . ! -type f ! -type d`). Une racine qui serait elle-même un lien est aussi refusée. Code 12.
2. **Liste ancrée au commit.** `EMPREINTES-DE-LA-COPIE.txt` doit avoir l'empreinte `REFERENCE_ATTENDUE`, écrite en dur dans le lanceur (`ab90e73b…`). Code 12.
3. **Liste refaite sur la copie.** Le lanceur refait la liste par la même recette (`LC_ALL=C find … | sort -z | xargs -0 sha256sum`) et l'écrit dans `TENUE/empreintes-recalculees-de-la-copie.txt`. Elle doit avoir la même empreinte. Un fichier ajouté, caché, manquant ou modifié est donc refusé (code 12), et les lignes qui diffèrent sont écrites au journal. Ce contrôle remplace `sha256sum --check` et les comptes de la v3.
4. **Un 8e argument en vérification.** `--verifier-seulement TETE EMPREINTE REFERENCE` permet de faire les essais sur copies factices. En emploi, aucun remplacement n'est possible.
5. **Un nouveau cas de code 4.** Le départ est aussi refusé si `empreintes-recalculees-de-la-copie.txt` existe déjà dans le dossier de tenue.

La recette de fabrication de la liste de référence est écrite en tête du lanceur : `git archive` du commit, puis `tar -x`, puis la recette `LC_ALL=C`. Le script `fabriquer-liste-reference-v4.sh` la porte.

## Table des essais
| Lot | Cas | Résultat |
|---|---|---|
| Liste de référence | Refaite par une autre voie (`git ls-tree` et `git cat-file`, sans l'arbre extrait) : sain | **ÉGALE** à l'octet, `ab90e73b…` (`final-controle-reference-saine.txt`) |
| Liste de référence | Liste altérée d'un octet (artefact) | **DIFFÉRENTE**, code 1 (`final-controle-reference-alteree.txt`) |
| Refus en vérification (`final-refus.txt`) | **61 cas en tout, 61 tenus, 0 échec** | Détail dans les lignes ci-dessous |
| | A. Racine avec `.git` (refus v2 et v3 rejoués) : sain 0 ; non suivi seul 0 ; sorties existantes 10 ; tête fausse 11 ; tête d'emploi 11 ; racine absente 11 ; fichier suivi modifié 12 ; empreinte fausse 13 ; interpréteur absent, non exécutable ou dossier 14 | Tenus |
| | B. Copies factices, référence propre à chacune — refus v3 rejoués : copie saine 0 ; sorties existantes 10 ; interpréteur absent 14 ; sans commit, commit faux, abrégé, sur deux lignes, sans fin de ligne, en lien, `.git` parasite 11 ; liste absente ou vide 12 ; fichier modifié, manquant ou ajouté 12 | Tenus |
| | B. Copies factices — nouveautés v4 : liste altérée d'un octet 12 ; liste en lien 12 ; **fichier modifié avec liste refaite** 12 ; fichier manquant avec liste refaite 12 ; **fichier ajouté avec liste refaite** 12 ; fichier caché ajouté 12 ; programme altéré avec liste refaite 12 ; programme altéré avec référence assortie 13 ; **lien vers un fichier** 12 ; lien vers un dossier 12 ; lien brisé 12 ; fichier remplacé par un lien de même contenu 12 ; tube nommé 12 ; racine en lien 12 ; **référence altérée d'un octet** 12 ; référence d'emploi sur copie factice 12 ; fichier de recalcul déjà présent 4 | Tenus |
| | C. **Vraie copie**, valeurs d'emploi, aucun remplacement : saine 0 ; **lien ajouté** 12 ; **fichier ajouté** 12 ; **fichier modifié avec liste refaite** 12 ; **liste altérée d'un octet** 12 ; interpréteur absent 14 ; **lanceur dont la référence est altérée d'un octet** 12 ; saine de nouveau après retour 0 | Tenus |
| | D. Usages : 3, 6 et 9 arguments, 5e argument inconnu, chemins relatifs 2 ; code déjà présent 4 ; tenue absente 3 ; sorties jamais créées | Tenus |
| Emploi, vrai départ v4 détaché, vraie copie (`final-emploi-et-commande.txt`) | **9 cas, tous tenus** : sain 0, argv égal à l'attendu du complément ; sain à un chemin avec espace 0, argv égal ; sans commit 11 ; commit faux 11 ; interpréteur absent 14 ; sorties existantes 10 ; fichier modifié 12 ; lien ajouté 12 ; sain après retour 0 | L'interprète n'est appelé que dans les trois cas sains |
| Commande statique | `verifier-commande-v3.py` sur le lanceur v4 ; huit altérations rejouées de la v3 | Lanceur v4 : 0 ; chaque altération : 1 ; aucune altération nulle |

Le lot « emploi et commande » compte 18 essais en tout : 9 en emploi et 9 en commande statique, aucun échec.

## Écarts
1. **Le contrôle `sha256sum --check` de la v3 et les comptes sont retirés.** La liste refaite, égale à la référence, couvre tout ce qu'ils couvraient (fichiers modifiés et manquants), et en plus les fichiers ajoutés et l'ordre.
2. **Le code 13 change de rôle sur copie.** Un programme altéré avec la liste refaite rend désormais 12, et non plus 13 : la liste n'est plus celle de la référence. Le code 13 n'est plus atteignable sur copie que si la référence elle-même porte un programme autre. L'essai b8b le montre avec une référence factice assortie.
3. **Un fichier de plus dans le dossier de tenue.** Le lanceur y écrit `empreintes-recalculees-de-la-copie.txt`. Si le dossier de tenue était placé dans la racine, le contrôle échouerait (refus sûr).
4. **La recette de la liste change de la v3 à la v4.** Elle porte désormais `LC_ALL=C` pour le tri. Une liste faite par la recette de la v3, sans `LC_ALL`, peut différer selon la langue du système. Seule la recette v4 fait foi.
5. **Commit factice.** Un dépôt git jetable a reçu un commit factice dans `essais/a-refus-*/racine-git`. Il sert à la forme avec `.git`.

## Réserves
- **Le contrôle hache deux fois la copie.** La liste refaite représente 3,6 Go à lire à chaque départ et à chaque `--verifier-seulement`, soit environ 4 s ici.
- **Hypothèse sur la copie envoyée.** Elle doit sortir de `git archive` du commit. Une copie faite autrement, par exemple un arbre de travail extrait par git avec ses filtres, peut différer. Aucun filtre n'est déclaré dans le `.gitattributes` du commit, mais rien n'est éprouvé hors `git archive`.
- **Ce qui n'est pas vérifié.** Le mode des fichiers (exécutable ou non) et les dossiers vides ne sont pas vérifiés : git ne suit pas ces derniers.
- Le vrai programme n'est pas exécuté (premier pas non justifié inchangé).
