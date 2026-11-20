# Notice — module des autres moniteurs et de la lecture commune du bras A, version 9 — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `reponses-sans-interne-demandes-v8-v2.md`, même dossier.

Écrit par le développeur habilité neuf côté moniteurs, le 20 novembre 2026, sur commande de la mère sous GO-2026-11-20-21 (mandat v2, `8c60bfe7…`). Classe B : à contre-lire par un autre modèle. Sources de la commande : partie 3 de mes réponses internes (`reponses-developpeur-habilite-demandes-v8-v1.md`, `0cd329f1…`) et lecture habilitée de ces réponses (`lecture-habilitee-reponses-v8-v1.md`, `0f1c410e5548f04d9a674beee50e1b9fb4fd523e99efdc4ad8823ed3c27ccb43`). Aucun résultat lu, aucun poids chargé, aucune dépense. Ni commit ni poussée. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| module, version 9 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v9.py` | `08a8f5c532e350045b0ab8a640525f6f839f47a2a9dc48dad6655b1dec9b13d2` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v9.py` | `b0d505933a7514ff6bc4e2078435280a898134c7725fb2516c93fb208c8cefda` |
| épreuve par retrait : script | `docs/notes/bras-a-moniteurs-v1/epreuve-par-retrait-autres-moniteurs-v9-v1/passage_mutations_v9.py` | `ee7445b2d8e2c306c8cdec6d20b8fb3f78332d27dce4cd159d27a1c9ffb4feed` |
| épreuve par retrait : relevé | `…/epreuve-par-retrait-autres-moniteurs-v9-v1/mutations-v9-resultats.md` | `195dc56cd0610b9242748f2aa0e4271152b5a02256fc5fbb44a3480d91546f23` |
| épreuve de forme : script | `scripts/bras_a_v2_habilite_epreuve_de_forme_v9_v1.py` | `2962dac91c6e2e68a91db44e2fe757028ee542421f58ea3cea074bad0df0e6ef` |
| épreuve de forme : sorties | `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v9-v1/` | partie 4 |

Essais : `PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_autres_moniteurs_v9.py` ; dernière ligne : `74 passed in 652.47s (0:10:52)`.

## 2. Ce qui change depuis la version 8

**Aucun calcul d'aire, de score, de borne ni de valeur p ne change** (attestation de la demande 24 b, par comparaison ligne à ligne des deux fichiers) : `_aire`, `_borne_haute`, `_permuter`, l'ajustement et la notation, les graines et l'ordre des tirages sont inchangés. Un seul déplacement : l'aire observée est calculée **avant** la boucle des permutations au lieu d'après ; elle ne consomme aucun tirage et ne dépend pas des permutations, sa valeur est la même ; seule change la forme d'une lecture dont l'aire observée n'est pas calculable (comptes de permutations nuls, cas B, au lieu de N permutations perdues sur N).

| objet | version 8 | version 9 | essais |
|---|---|---|---|
| cas D (plus de 1 % de tirages dégénérés) et E (intervalle impossible) | `calculable` faux, tout nul, famille 1 | `calculable` vrai ; aire, plis, deux valeurs p, aires au moins égales rendues ; famille = valeur p haute ; borne et quantile nuls ; motif écrit | `test_tirages_degeneres_de_la_borne_…`, `test_cas_e_naturel_une_tache_par_pli`, `test_motif_de_tirages_degeneres_illisible_arrete` |
| cas C | aire nulle | aire et aires des plis rendues | `test_plus_de_un_pour_cent_de_permutations_perdues_…` |
| motifs d'un moniteur appris non ajusté | `vocabulaire vide`, `pli k : tous les traits retirés (…)`, `pli k : non convergé (gradient maximal … > 0.0001 …)` | `pli k : moniteur appris non ajustable` ; `pli k : classe absente du pli d'apprentissage` gardé (effectifs) | `test_vocabulaire_vide_…`, `test_motifs_neutres_d_un_moniteur_appris` |
| garde de forme d'une lecture | clés seulement | clés ; motif en liste fermée (`MOTIFS`) ; cas rangé d'après les seuls comptes ; nombres rendus et nuls du cas ; aires dans [0, 1] ; valeurs p égales au quotient exact de leurs comptes ; famille ; nombres du motif égaux aux comptes | `test_motifs_en_liste_fermee_et_cas_des_comptes` |
| `piece_source` | chemin et empreinte de la pièce de la base | `{"sha256": empreinte de ce module, calculée sur son fichier à l'exécution, "production": {moniteur: empreintes des deux programmes}}` ; aucun chemin | `test_sortie_construite_et_ses_gardes`, essai de bout en bout |
| manifeste de production | six clés | sept : `programmes`, empreintes du module des deux moniteurs à modèle de langue (`8e941d24…`) et de la préparation des lectures (`6dfd2bfc…`), calculées sous la racine et égales aux empreintes inscrites (`PROGRAMMES_DE_PRODUCTION`) ; `ecrire_la_production(…, *, racine)` sans défaut | `test_programmes_de_production_au_manifeste` |
| champs de l'agrégateur | la statistique retenue manque (nul) | somme et maximum toujours, un nombre (ou nul) par dose | `test_autres_statistiques_de_l_agregateur_sans_etat` |
| `reglages.statistique_agregateur` | la statistique en clair | `statistique de l'agrégateur fixée par la configuration scellée du lanceur` | idem, bout en bout |
| sortie | rendue en mémoire | garde de toute la sortie (`exiger_sortie`), écriture et scellement sous `lecture-commune-moniteurs-bras-a.json` (`ecrire_la_sortie`), relecture identique exigée ; `lire_les_cinq(…, *, dossier_de_la_sortie)` sans défaut, dossier disjoint des dossiers du fichier par unité, de la table et des productions, vérifié avant tout calcul ; refus d'écraser avant tout calcul | `test_sortie_construite_et_ses_gardes`, `test_dossiers_disjoints`, `test_sortie_dans_un_dossier_non_disjoint_…`, `test_ecriture_de_la_sortie_a_pleine_precision` |

Valeur retenue pour `calculable` aux cas D et E : **vrai** (aire et valeurs p rendues ; seul l'intervalle manque). C'est mon choix, faute d'une valeur prescrite par la relance : à confirmer par la mère.

## 3. Épreuve par retrait

58 gardes et morceaux de code retirés un à un, essais ciblés joués après chaque retrait : **58 mordent sur 58**, aucune mutation non jouée (relevé ci-dessus). Couvert : toutes les gardes neuves ou changées de la version 9 ; le code de l'échange par paire (tirage d'une chance sur deux, inversion des deux étiquettes, regroupement par rang) et ses deux gardes (appel, trois épisodes de même rang, une étiquette de chaque sorte, épisode sans pair), l'appel de la garde par épisode et l'exigence de la permutation en clair (demande 24 a du lecteur). Le module est remis à l'identique après chaque retrait ; son empreinte a été vérifiée à la fin. Les gardes des versions 1 à 8 non touchées ne sont pas rejouées ici : leur épreuve reste celle de leurs notices.

## 4. Épreuve de forme (demande 17)

Sorties construites à la main, sans moniteur, sans épisode réel ; 2 000 permutations, 2 000 tirages, échange par paire, fichier par unité en rangs. Chaque sortie est assemblée et écrite par le module, donc passée par sa garde ; au cas C, 30 permutations perdues sur 2 000 sont **injectées** par le script (un moniteur lu sur des scores n'en perd aucune sous l'échange par paire). L'artefact est la sortie du cas A dont une valeur p haute est arrondie à quatre décimales ; la garde du module la refuse ; il est écrit hors du module.

| sortie | chemin, sous `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v9-v1/` | empreinte |
|---|---|---|
| cas A | `cas-a/lecture-commune-moniteurs-bras-a.json` | `009a34e4f44a8ff157af2c88ad75daca90199f0891ef2b488fb8db090bf36972` |
| cas B | `cas-b/lecture-commune-moniteurs-bras-a.json` | `529666dfb07921fc55c22af164a2e693d034f0e6bd001689cc6184a16cb1f99d` |
| cas C | `cas-c/lecture-commune-moniteurs-bras-a.json` | `0c7355e82c91c9f69fab2375737fd13a73d10311104f42078357a987576d02c9` |
| cas D | `cas-d/lecture-commune-moniteurs-bras-a.json` | `69b589366ba9aaac52a32e9cb213cdc44ad8ff89c93efb718830009758397554` |
| cas E | `cas-e/lecture-commune-moniteurs-bras-a.json` | `8c66905660c377ed66944f7ebde753087735834188157a8e39fd9fcbde214432` |
| artefact, valeur p arrondie | `artefact-cas-a-valeur-p-arrondie/lecture-commune-moniteurs-bras-a.json` | `7d5eb9c96d4c76ab3eda91428c92e4a62e299004e7678accbad484ee7b0b88c7` |

Chaque sortie porte, dans les deux champs de l'agrégateur, un seul nombre par dose, aux quatre doses (nombres construits). Les fichiers par unité de l'épreuve (`unites-cas-*/`) portent des rangs de scores construits.

## 5. Réserves, pour le contre-lecteur

- **Égalité de valeur.** La forme des deux champs de l'agrégateur ne dit plus la statistique retenue. Mais si la statistique retenue était la somme ou le maximum, l'un des deux champs serait égal, dose par dose, à l'aire décisive de l'agrégateur, et la dirait. Sous la moyenne, que la liste des nombres rendus suppose déjà (« aire de la somme et aire du maximum »), rien ne la dit. À trancher par la mère si la statistique peut être autre que la moyenne.
- **Empreintes des programmes de production.** Elles sont calculées sur les fichiers sous la racine, non sur les modules importés par le processus de production ; le lanceur doit importer ces modules du même arbre. Une version neuve de l'un d'eux demande une version neuve de ce module.
- **Garde statique des essais v8.** La présence de la version 9 fait échouer `test_garde_statique_du_paquet` du fichier d'essais v8 (sa liste ne la connaît pas) ; même situation qu'aux versions précédentes ; les autres essais v8 ne sont pas touchés.
- **Compagnon du module.** Le module est scellé (`.sha256` à côté de lui), ce que les versions précédentes du paquet n'avaient pas ; la garde statique ne lit que les `.py`.
- **Garde du chemin en clair.** Elle refuse toute sortie dont le texte contient `.py`, `src/` ou `scripts/` ; elle n'est pas une preuve qu'aucun autre nom de pièce habilitée n'y figure.
- **Pas fait** : le lanceur de l'étape de discrétion (demande 18) — l'ordre en six étapes n'est pas dans les pièces que j'ai ; le dossier du fichier des rangs (demande 19) reste celui que fixera sa configuration ; le module garantit seulement qu'il est disjoint de celui de la sortie. La correction de la note sur le lanceur du bras (garde d'équivalence, lecture habilitée, partie 5 point 4) n'est pas faite.
- Vérification par le contre-lecteur : à faire.
