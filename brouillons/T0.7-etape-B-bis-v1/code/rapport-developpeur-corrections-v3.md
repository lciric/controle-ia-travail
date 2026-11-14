# Rapport du développeur sur les corrections du code de l'étape B bis de T0.7 (modèle A), v3 — destruction vérifiée (R-2789)

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu sous `diag/`, `runs/`,
`donnees/` du dépôt de travail ; aucune machine, aucun appel réseau, aucune dépense ; aucun vrai outil `vastai` appelé (faux outil
seulement, dans des dossiers jetables).

- **Auteur** : « modèle A ». **Date (UTC, `date -u`)** : 2026-11-14, de 16:35 à 16:47.
- **Pourquoi une v3** : la demande (défaut trouvé ce jour sur une vraie instance, fille Neuron Lens, R-2789) est arrivée après le
  scellement et le commit de la note v2 (`ac062190`, `rapport-developpeur-corrections-v2.md` `d8a2e40b…`). La v2 n'est pas réécrite
  (R12) ; cette v3 la complète et, sur un seul point, la met à jour (§ 3).
- **Défaut** : avec l'outil `vastai` 1.11.0, `vastai destroy instance ID` demande une confirmation [y/N], abandonne sans entrée
  (« Aborted. ») et **rend le code 0** : l'instance reste.
- **Commits** (branche `prep/t07bbis-code-v1`, jamais poussée) : code `1db788846752e1b3b93e0747ebba2b28a175156a` ; cette note et
  la sortie des essais : commit suivant.

## 1. Fait, fichier par fichier

| fichier | fait |
|---|---|
| `scripts/lancer_bbis_v1.sh` | `detruire ID` (ancienne l. 64) imprime `GO_ID=GO-2026-11-14-09 vastai destroy instance ID -y` (**`-y`**), puis la ligne de vérification à jouer ; refuse un identifiant non numérique ou d'une autre session. Sous-commande **neuve** `verifier-destruction ID TEMOIN [LISTE.json]` : lecture seule ; sans fichier, lit `vastai show instances --raw` (outil `VASTAI_BBIS` ou `vastai`), garde la liste lue dans un dossier `mktemp -d` dont le chemin est imprimé ; lecture en échec → « absence non prouvée », code 2 ; sinon `registre_bbis_v1 absence`. Le message de refus de `depense` annonce `detruire` puis `verifier-destruction`. |
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | `exiger_identifiant_a_detruire` (numérique ; jamais une instance d'une autre session : 58936096, 58936099, 58936100, 60480302, 60599797, liste `INSTANCES_D_AUTRES_SESSIONS`, mot de la mère ; elles restent permises comme témoins) ; `exiger_absence(liste, ID, TEMOIN)` : la destruction n'est **jamais jugée par un code de sortie** ; prouvée seulement si la liste est lue sans erreur (liste d'objets portant `id`, ou `{"instances": […]}`), si le témoin (≠ ID) y est présent et si ID en est absent ; sinon `GardeArret` « absence non prouvée » avec le motif (liste illisible, témoin absent, instance toujours listée). Sous-commandes `identifiant ID` et `absence ID TEMOIN LISTE.json`. Message de `garde_depense` : « commande avec -y, puis absence de l'identifiant vérifiée dans la liste des instances ». Docstring du module mis à jour. |
| `scripts/amorce_bbis_v1.sh` | **Minuterie** (destruction de l'instance par elle-même, `DELETE /instances/$CONTAINER_ID/` par l'API, sans l'outil `vastai`) : elle ne rendait la main qu'au premier code HTTP 2xx, ce qui jugeait la destruction par un code. Elle ne juge plus aucun code : **tant que le processus vit, l'instance n'est pas détruite**, la demande est refaite toutes les 60 s ; après cinq demandes, l'état « stopped » est demandé une fois (la carte cesse d'être facturée) ; le journal dit que seule l'absence de l'identifiant dans la liste, lue par la session, prouve la destruction. `fin_instance` écrit que la session détruit avec `-y` et vérifie l'absence (`verifier-destruction`). `MIN_ESSAIS` 84 → **86**. Aucune commande `vastai destroy` dans l'amorce (rien d'autre à corriger). |
| `tests/test_t07bbis_chaine_instance_v1.py` | deux essais neufs (§ 2). |
| `tests/test_t07bbis_registre_v1.py` | `detruire` : première ligne exacte avec `-y`, seconde ligne = vérification. |

Aucun autre endroit du code de B bis n'écrit ni ne joue une destruction (recherche par motifs `destroy`, `detruire`, `DELETE`,
`destruction` sur les dossiers exacts `scripts/*bbis*`, `src/controle_ia/t07bbis/`, `tests/*t07bbis*`). La lecture, la table
conjointe et la marche n'en contiennent pas. Le jeton et sa manipulation ne changent pas.

## 2. Essais ajoutés

- `test_destruction_avec_y_et_absence_prouvee_contre_un_faux_outil` — **faux outil** `vastai` (script bash dans un dossier
  jetable, état dans un fichier) qui reproduit le défaut : `destroy instance ID` **sans** `-y` affiche la question, lit une entrée
  vide, écrit « Aborted. » et **rend 0** sans rien détruire ; avec `-y`, retire ID ; `show instances --raw` rend la liste, ou une
  faute choisie (texte illisible, code 1).
  - sain : la ligne imprimée par `detruire`, jouée telle quelle (préfixe `GO_ID` compris, entrée vide), détruit ;
    `verifier-destruction 123456 60480302` → « DESTRUCTION PROUVEE », code 0 ;
  - **le cas du jour** : la même ligne sans `-y` → « Aborted. », **code 0** ; `verifier-destruction` → « absence non prouvée :
    instance 123456 toujours dans la liste », **code 2** : la chaîne le détecte ;
  - artefacts : témoin absent de la liste ; liste illisible ; lecture en échec (code 1) ; témoin égal à l'instance détruite ; liste
    par fichier sans `id` → code 2 ; liste par fichier de forme `{"instances": […]}` → acceptée ; `detruire` d'une des cinq
    instances d'autres sessions → refus, aucune commande imprimée ; `depense` en refus annonce `-y` et `verifier-destruction`.
- `test_minuterie_refait_la_destruction_tant_que_l_instance_vit` — extrait `minuterie` de l'amorce joué par bash, `curl` remplacé
  par un faux qui rend toujours 200 sans rien détruire : sept `DELETE` (jamais de retour au premier 200), un seul `PUT stopped`
  après le cinquième, journal « code jamais jugé » et « toujours vivante après 5 demandes ».

Comptes : arbre complet **108 passés** ; extraction partielle de l'instance simulée au commit `1db78884` (même procédure, motifs
inchangés) **86 passés, 22 sautés** ; `MIN_ESSAIS = 86` ; `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v3.txt`.
La liste des 90 fichiers cités par la fiche (`fichiers-fiche-code-bbis-v1.txt`, `8e3d0799…`) est recalculée à ce commit :
**inchangée**.

## 3. Mise à jour des commandes de la note v2 (§ 3, geste 0)

Le code éprouvé est maintenant celui du commit `1db788846752e1b3b93e0747ebba2b28a175156a` : dans le geste 0, la comparaison devient
`git diff --quiet 1db788846752e1b3b93e0747ebba2b28a175156a HEAD -- $(cat "$L")`, et les essais attendus sur l'arbre complet sont
**108 passés**. Le reste des gestes 1 à 5 et l'ordre (§ 4 de la v2) sont inchangés. Destruction de l'instance de B bis, par la
mère : `bash scripts/lancer_bbis_v1.sh detruire ID` (jouer la ligne `GO_ID=… vastai destroy instance ID -y` imprimée), puis
`bash scripts/lancer_bbis_v1.sh verifier-destruction ID TEMOIN` avec une instance témoin présente ; code 2 (« absence non
prouvée ») → arrêt, compte rendu, destruction et vérification refaites.

## 4. Réserves

- La forme de la liste rendue par `vastai show instances --raw` (liste d'objets portant `id`) est celle du faux outil et de la
  forme courante de l'outil ; la répétition à blanc doit la confirmer sur l'outil réel (sinon « liste illisible », jamais un faux
  « prouvée »).
- La minuterie ne peut pas prouver sa propre destruction (elle meurt avec elle) ; la preuve est toujours celle de la session.
- La liste des instances d'autres sessions est figée au mot du 2026-11-14 ; une instance d'une autre session créée plus tard n'y
  est pas (la destruction reste par l'identifiant donné, R10).

## 5. Empreintes (SHA-256, commit `1db78884`)

| fichier | empreinte |
|---|---|
| `scripts/amorce_bbis_v1.sh` | `f6ceeed69ed6697470127e7d4fef38f245ebca08c07d2e1670093675d6333d5f` |
| `scripts/lancer_bbis_v1.sh` | `9bc5232166f2c9dc6d46935c189ea9bef36789a831816f873f2595b0b817c9db` |
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | `6be2a2cc84650178a202bc8fdb8a052b82116cbc5fc2dc1656571608c46b0236` |
| `tests/test_t07bbis_chaine_instance_v1.py` | `7542f481be62c460201845823b03d85a3393a6266e7810f277f8394c01e072ed` |
| `tests/test_t07bbis_registre_v1.py` | `2b32fe13f53382fcfef2ac4bcf1273a724177c6658a6d3773cdf50cc33157e85` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v3.txt` | `6285781ba5a7769df1a9e30c93425b6f20b550926968b8b61bada7f14e52c28a` |

Ménage : les quatre dossiers `/tmp/tmp.*` laissés par un premier passage de l'essai neuf (avant que l'essai pose `TMPDIR` sur son
propre dossier), qui ne contenaient que les listes du faux outil, ont été retirés par leurs chemins exacts.
