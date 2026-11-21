# Vérification des corrections du code de commande de la relecture, version 2 — v1

- **Nature** : vérification des corrections d'une pièce de classe B (code), par le même contre-lecteur (Claude Opus 5.5), le 21 novembre 2026, sous le même mandat (`85e1de43…`) et les mêmes règles.
- **Contre-lecture vérifiée** : `cl-commande-v2/contre-lecture-commande-lecture-v2-v1.md` (`350d847190d5c9e5a350ff06b4b9213f479d67662aaa4bbebadc4dd288e14077`), quatre corrections non bloquantes.
- **Pièces lues** : le rapport du développeur, `dev-commande-v2/rapport-developpeur-corrections-commande-lecture-v2-v1.md` (`f0b292a8d3c966264f3017e40fb88553a75ba530fa7b4d03f3891eeb21649036`, égal à son compagnon), et le diff `76c608b6..5402367e`.
- **Commit vérifié** : `5402367e5b62c8ac294c55d5cc0230ebdfbaa457`, de parent `76c608b61d52549d4e0dceb9d07be0c5bea273f8`.
- **Cloisonnement** : rien ouvert hors de la liste ni sous `/root/secret-b5f-formation-v1/` ou `/root/.claude/`. Aucune commande au loueur, aucune clé, aucune poussée, aucun commit.

## Verdict

**Conforme, prêt à pousser.** Les quatre corrections sont portées comme demandé. Rien d'autre n'a changé. Les deux mutations qui survivaient rendent maintenant un essai rouge.

La ligne de l'accord de lecture `GO-LECTURE-B5F` doit citer le commit `5402367e5b62c8ac294c55d5cc0230ebdfbaa457`, et non plus `76c608b6…`.

## Portée du commit

- `git diff --name-status 76c608b6 5402367e` donne une seule ligne : « M tests/test_commande_lecture_v2.py », avec 17 lignes ajoutées et 5 retirées.
- `git diff --quiet 76c608b6 5402367e -- src scripts` ne trouve aucune différence.
- Empreintes au commit, égales à celles du rapport :
  - module : `c6c5d11c…` ;
  - lanceur : `c07fc124…` ;
  - essais : `82452204…`.
- J'ai lu le diff en entier. Il ne contient que les quatre corrections et leurs commentaires. Aucune assertion n'est retirée ni desserrée :
  - les deux `match="GO-LECTURE-B5F"` sont remplacés par un motif plus étroit, propre au refus de (d) (ligne 134 du module) ;
  - l'ancienne assertion du résultat de la version 1 est gardée ; elle est seulement étendue à la version 2 et au cas de la frontière.

## Correction par correction

1. **Fin de chaîne de la citation : portée.**
   - Ajouts dans `test_d_format_de_la_citation_lu_a_la_lettre` : `sain + "0"`, `sain + "xyz"` et `sain + " note sans point-virgule"`.
   - Le motif est resserré pour tous les artefacts de format et pour l'artefact « autre ligne ».
   - Preuve : la mutation X02 est rouge.
2. **Répétition à 0,30 USD par Go et par mois : portée.**
   - Le cas sain est éprouvé de deux façons : par `exiger_offre_lecture_v2`, qui rend la valeur, et par le corps recomposé, qui rend « --disk 150 » et une commande égale à l'octet à celle de la version 1.
   - L'encadrement numérique est affirmé dans l'essai.
   - Preuve : la mutation X01 est rouge.
3. **Motif propre à (d) dans `test_d_ligne_de_l_accord_de_lecture_sans_la_citation` : portée.** Le motif est maintenant « ne cite pas, une fois et à la lettre ».
4. **Frontière 299/300 du disque : portée.**
   - `{"disk_space": 299}` est ajouté au paramétrage, et 149 est gardé.
   - Le refus est attendu pour le plan « decisif » dans les deux versions. Le développeur affirme aussi l'acceptation pour « repetition », ce qui va au-delà de la demande sans rien desserrer.
   - Preuve : une mutation X08, ajoutée pour cette vérification, abaisse la borne du disque d'un Go. Elle est rouge sur le cas `[decisif-retouche1]`, c'est-à-dire 299 Go. Avant la correction, seuls 149 et 200 éprouvaient cette borne, et ni l'un ni l'autre ne la discriminait.

## Mutations rejouées

Les mutations ont été jouées dans une copie neuve : `git worktree add --detach`, à `5402367e`. Le fichier muté était rendu à l'octet après chaque mutation, et son empreinte vérifiée.

Tous les essais avaient le même `--basetemp`, écrit en clair : `/tmp/claude-0/-home-user-controle-ia-travail/297a4a07-6190-598e-ba08-f9d65884efdb/scratchpad/cl-commande-v2/bt-verif-unique`. Ce dossier a été purgé après chaque passe ; aucun dossier `bt-*` ne reste.

Fichiers de la passe :
- programme : `cl-commande-v2/muter-verif.py` (`17a9c006…`) ;
- relevé : `cl-commande-v2/sortie-mutations-verif.txt` (`bf66c335…`).

Sans mutation, la copie donne 113 passés et 1 sauté.

| mutation | avant correction | après correction |
|---|---|---|
| X01, disque fixé à 300 dans la formule du stockage | survivait | **rouge** : `test_portee_repetition_par_le_corps_recompose_…` (1 échoué, 112 passés) |
| X02, `fullmatch` remplacé par `search` | survivait | **rouge** : `test_d_format_de_la_citation_lu_a_la_lettre` (1 échoué, 112 passés) |
| X03, (b) sans la clause « la tête est le commit de commande » | rouge | rouge, les deux mêmes essais |
| X04, (c) sans la borne « hors de la liste fermée » | rouge | rouge, le même essai |
| X05, (b) comparant l'index seul | rouge | rouge, le même essai |
| X06, (d) avec un nom de session facultatif | rouge | rouge, le même essai |
| X07, lanceur sans la garde du plan | rouge | rouge, le même essai |
| X08 (neuve), borne du disque abaissée d'un Go | non jouée | **rouge** : 4 essais, dont `[decisif-retouche1]` (299 Go) |

## Essais au commit `5402367e`

Ils ont été joués depuis l'arbre de commande, en lecture seule : `PYTHONDONTWRITEBYTECODE=1`, `-B`, `-p no:cacheprovider`, et le `--basetemp` ci-dessus, purgé après chaque fichier. `git status --porcelain` était vide avant et après, et la tête est restée à `5402367e`.

| fichier | résultat | annoncé |
|---|---|---|
| `tests/test_commande_lecture_v2.py` | 113 passés, 1 sauté | 113 passés, 1 sauté |
| `tests/test_barreau5_familles_relecture_v1.py` | 24 passés | 24 |
| `tests/test_lancer_b5f_lecture_v1.py` | 43 passés | 43 |
| `tests/test_barreau5_familles_engagement_v1.py` | 23 passés | 23 |

L'essai sauté est celui du registre réel, joué sans sa variable.

## Ce qui reste

- Aucune correction.
- Les remarques hors liste de la contre-lecture restent à transmettre, sans correction demandée :
  - (c) admet un fichier ajouté sous forme de lien symbolique ;
  - le « é » de « vérifiée » doit être en forme composée dans la ligne `GO-LECTURE-B5F` ;
  - le commit de la marche doit être présent dans le dépôt de l'arbre de commande.
- La copie de vérification a été retirée : `worktree remove --force`, puis `prune`. Elle était propre, et à `5402367e`, avant d'être retirée.
- Limites : je n'ai pas joué les essais du paquet entier, ni rien exécuté sur le dépôt réel.
