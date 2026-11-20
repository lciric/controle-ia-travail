# Contre-lecture habilitée du module des autres moniteurs et de la lecture commune, version 9 — pièce interne — v1

**Pièce habilitée, à ne pas transmettre à une session non habilitée.** Ce qui est transmissible est dans `contre-lecture-habilitee-autres-moniteurs-v9-sans-interne-v1.md`, même dossier.

Écrit par le lecteur habilité côté moniteurs du bras A (Claude Fable 5.2, accord de Lazar GO-2026-11-20-21), le 20 novembre 2026, à la demande de la session mère. Classe B. Copie `/home/user/bras-a-habilite`, tête `92842ac543a1ed16678746ba1d5dbc3d7b319280`. Mêmes règles qu'à ma lecture précédente (`lecture-habilitee-reponses-v8-v1.md`, `0f1c410e5548f04d9a674beee50e1b9fb4fd523e99efdc4ad8823ed3c27ccb43`).

## Verdict : **conforme après ces corrections**

Aucun calcul n'est faux et aucune fuite n'est trouvée. Les demandes 13, 1, 2, 3, 15, 16 et 31 sont levées ; la demande 17 l'est avec une réserve. Quatre corrections, toutes de forme, aucune ne touche un calcul (partie 6).

## 0. Pièces, et ce qui a été fait

| pièce | chemin | empreinte recalculée |
|---|---|---|
| module, version 9 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v9.py` | `08a8f5c532e350045b0ab8a640525f6f839f47a2a9dc48dad6655b1dec9b13d2` |
| ses essais | `tests/test_bras_a_v2_habilite_autres_moniteurs_v9.py` | `b0d505933a7514ff6bc4e2078435280a898134c7725fb2516c93fb208c8cefda` |
| notice | `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-autres-moniteurs-v9-v1.md` | `fe28737d1d2465e7e1280c950a7ba70fafecf774f74ed8476e30d66542002cc4` |
| pièce sans interne v2 | `docs/notes/bras-a-moniteurs-v1/reponses-sans-interne-demandes-v8-v2.md` | `1959a0be4d74c7039a6e72d04f53bb4f57ca71545050d0d70bd6f0e6e6b7b9f7` |
| épreuve par retrait, script | `…/epreuve-par-retrait-autres-moniteurs-v9-v1/passage_mutations_v9.py` | `ee7445b2d8e2c306c8cdec6d20b8fb3f78332d27dce4cd159d27a1c9ffb4feed` |
| épreuve par retrait, relevé | `…/epreuve-par-retrait-autres-moniteurs-v9-v1/mutations-v9-resultats.md` | `195dc56cd0610b9242748f2aa0e4271152b5a02256fc5fbb44a3480d91546f23` |
| épreuve de forme, script | `scripts/bras_a_v2_habilite_epreuve_de_forme_v9_v1.py` | `2962dac91c6e2e68a91db44e2fe757028ee542421f58ea3cea074bad0df0e6ef` |
| épreuve de forme, six sorties | `docs/notes/bras-a-moniteurs-v1/epreuve-de-forme-v9-v1/` | les six empreintes de la notice, retrouvées |
| texte visé (table des formes de 6.9, par extraits) | brouillon 33 | `dc3bc0236e9103454c988fa24997c698306ef78a2328587430bed553a5020c4a` |

- **Lu** : la différence entière entre les versions 8 et 9 (`diff`, 449 lignes), les fonctions touchées de la version 9, les essais neufs, les deux scripts d'épreuve, la notice, la pièce sans interne v2, la table des formes du texte.
- **Rejoué** : les essais (`74 passed in 575.73s`) ; l'épreuve par retrait du développeur (58 retraits, **58 mordent**, aucun non joué) ; sept retraits de plus, de mon fait (partie 5) ; la garde statique des essais de la version 8. Module remis à l'identique après chaque passage, empreinte vérifiée ; copie propre à la fin.
- **Pas rejoué** : l'épreuve de forme (ses sorties portent la date de l'ouverture : leurs empreintes ne se retrouvent pas d'un jeu à l'autre). Ses sorties scellées ont été lues.
- Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `archives-reponses-modeles/`. Aucun poids chargé, aucun appel payant. Aucun refus d'outil pour une permission. Un écart : la première sortie du `diff`, trop longue, a été rangée par l'outil sous `/root/.claude/` ; je ne l'y ai pas lue, je l'ai refaite dans le bloc-notes. Ni commit ni poussée.

## 1. Les demandes dites levées

| demande | état | fondement (version 9) |
|---|---|---|
| 13, empreinte du module | **levée** | `empreinte_du_module` (lignes 1265 à 1267 : `hashlib.sha256(Path(__file__).read_bytes())`), posée dans `piece_source.sha256` par `assembler_la_sortie` ; l'essai compare à l'empreinte du fichier ; les six sorties de l'épreuve portent `08a8f5c5…`. `piece_source` n'a plus que `sha256` et `production` ; la garde refuse toute autre clé et tout texte de la sortie qui contient `.py`, `src/` ou `scripts/`. Recherche dans les cinq sorties de l'épreuve : zéro chemin. La pièce de la base reste liée : le module ne la charge qu'à l'empreinte qu'il inscrit. |
| 1, cas D | **levée** | `_conclure`, lignes 593 à 622 : aire, plis, deux valeurs p, aires au moins égales rendues ; famille égale à la valeur p haute ; borne et quantile nuls ; les deux comptes de tirages rendus ; motif écrit. Conforme à la ligne D de la table des formes du texte. |
| 2, cas E | **levée** | même chemin ; comptes de tirages nuls. Conforme à la ligne E, rédaction (a). |
| 3, cas C | **levée** | ligne 600 : aire et aires des plis rendues avant la levée du motif ; valeurs p nulles, famille 1. |
| 15, nom du fichier de sortie | **levée** | `FICHIER_SORTIE = "lecture-commune-moniteurs-bras-a.json"`, écrit et scellé par `ecrire_la_sortie`, dans un dossier disjoint des autres. |
| 16, épreuve par retrait et notice | **levée** | rejouée, 58 sur 58 ; elle couvre l'échange par paire et ses deux gardes, que la version 7 ne couvrait pas (ma demande 24 a). |
| 17, épreuve de forme | **levée avec une réserve** | une sortie par ligne de la table, passée par la garde du module ; un nombre par dose dans les deux champs de l'agrégateur. Réserve : deux objets de l'épreuve n'ont pas la forme d'une vraie livraison (correction 2). |
| 31, champs de l'agrégateur | **levée** | `autres_statistiques`, lignes 1060 à 1079 : somme et maximum toujours, un nombre ou nul par dose ; garde de forme dans `exiger_sortie`. |

## 2. La différence v8 → v9 change-t-elle un calcul ? **Non.**

Comparaison ligne à ligne.
- `_aire`, `_borne_haute`, `_permuter`, les deux gardes de la permutation, l'ajustement, la notation, les graines et leurs clés : **aucune ligne changée**.
- Les deux valeurs p et le compte des aires au moins égales : mêmes expressions, déplacées de la fin de `_conclure` à son milieu (lignes 602 à 608).
- L'aire observée est calculée avant la boucle des permutations (lignes 659 et 689) au lieu d'après. Elle ne consomme aucun tirage ; la boucle ne dépend pas d'elle. Sa valeur est la même. Seule conséquence : une lecture dont l'aire observée n'est pas calculable sort au cas B, comptes de permutations nuls, sans jouer les permutations. Mon retrait de plus le confirme : remettre l'aire après la boucle fait échouer l'essai.
- Les matrices des deux plis sont construites dans le même ordre ; seul le motif d'un défaut est neutralisé.
- La somme et le maximum de l'agrégateur sont calculés tous les deux, par la même fonction qu'avant.
- **Ce qui change dans les nombres rendus, et qui est commandé** : aux cas D et E, la valeur de la famille passe de 1 à la valeur p haute, et `calculable` de faux à vrai ; au cas C, l'aire est rendue. Ce sont des changements de forme d'une lecture, non d'un calcul.

L'attestation de la demande 24 (b) peut donc être écrite pour la paire (version 8, version 9) : aucun calcul d'aire, de score, de borne ni de valeur p ne change.

## 3. Les quatre réserves du développeur

1. **`calculable` vrai aux cas D et E : acceptable, à inscrire.** La table des formes du texte fixe `calculable` faux aux cas B et C et ne dit rien aux cas D et E ; elle demande que la valeur y soit inscrite, et dit que ce champ n'entre dans aucune règle de jugement. Vrai est le choix cohérent (aire et valeurs p rendues). À transmettre à la relance : vrai aux cas A, D et E ; faux aux cas B et C.
2. **Égalité de valeur de l'agrégateur : sans objet tant que la statistique est la moyenne.** Le texte, côté relance, écrit lui-même que la moyenne sert l'aire de l'agrégateur ; il n'y a donc rien à trahir. De plus, l'égalité ne prouve rien : quand aucun pas n'est sauté, la somme et la moyenne rangent les épisodes de la même façon, et l'aire de la somme égale l'aire décisive sous la moyenne aussi. Si la mère veut fermer le cas, une garde qui n'admet que la statistique du texte suffit ; je ne l'exige pas.
3. **Garde statique des essais de la version 8 : confirmé, sans gravité.** Rejouée : `1 failed, 1 passed` ; seul motif, « autres_moniteurs_v9.py charge un fichier par son chemin », la liste de la version 8 ne connaissant pas la version 9. Les essais de la version 9 portent leur propre liste et passent. À consigner, pour que la suite d'essais du dépôt ne soit pas lue comme une régression ; chaque version neuve refera cet échec dans le fichier d'essais de la précédente.
4. **Permutations perdues injectées au cas C : acceptable.** Le script remplace la fonction d'aire pour les trente premières permutations, dans le script seulement, et la remet ; le compte, le motif et la forme sortent du vrai chemin du module et passent sa garde ; l'injection est déclarée dans les deux pièces. Un moniteur lu sur des scores ne perd en effet aucune permutation sous l'échange par paire, chaque paire gardant une étiquette de chaque sorte.

Deux réserves de sa notice que la mère n'a pas listées, et que je confirme : les empreintes des programmes de production disent quels fichiers étaient sur le disque, non ce que le processus a importé ; la garde du chemin en clair ne prouve pas qu'aucun autre nom de pièce habilitée ne sort.

## 4. La pièce sans interne v2 : **aucune fuite**

Relue ligne à ligne contre le code. Elle ne porte ni seuil de méthode, ni trait, ni vocabulaire, ni poids, ni texte de consigne. La chaîne neuve `pli <k> : moniteur appris non ajustable` ne nomme aucune méthode ; les trois chaînes retirées n'y figurent plus. Les empreintes des deux programmes de production ne sont pas dans la pièce. Mes trois retouches d'exactitude de la v1 sont reprises ; le chiffrage corrigé est celui de ma lecture.

Aucun couple (avant, après) n'est exigé. **Deux retouches d'exactitude**, sans effet de cloisonnement :

| ligne | avant | après |
|---|---|---|
| demande 1 | « commit : pas encore (versement par la mère) » | « commit : `92842ac54` » |
| en-tête | « elle n'a pas encore de commit (la mère verse sur la branche) ni de vérification du contre-lecteur » | « commit `92842ac54` ; contre-lue : conforme après corrections de forme » |

## 5. Rejeu des essais et de l'épreuve par retrait

- Essais : `74 passed in 575.73s (0:09:35)`.
- Épreuve par retrait du développeur : 58 retraits, 58 mordent, aucun non joué ; le relevé rejoué est égal au sien, aux durées près.
- **Sept retraits de plus**, de mon fait (script hors du dépôt, bloc-notes de la session, `retraits_du_contre_lecteur_v9.py`) :

| retrait | essais joués | issue |
|---|---|---|
| appel de la garde de forme du cas dans la garde d'un résultat | `liste_fermee or cas_e or neutres` | mord |
| écriture de la sortie par la lecture commune | `bout_en_bout` | mord |
| famille égale à la valeur p haute | `tirages_degeneres_de_la_borne or cas_e or valeur_p_pour_la_famille` | mord |
| comptes de tirages rendus au cas D | `tirages_degeneres_de_la_borne` | mord |
| aire observée avant les permutations | `classe_absente_a_l_aire` | mord |
| garde de la sortie à l'assemblage | `sortie_construite or non_disjoint or programmes_de_production` | **ne mord pas** |
| écriture qui refuse un nombre non fini (`allow_nan=False`) | `sortie_construite or pleine_precision` | **ne mord pas** |

  Les deux qui ne mordent pas : la garde à l'assemblage est doublée par celle de l'écriture ; le refus d'un nombre non fini n'a pas d'artefact. Voir la correction 3.

## 6. Corrections demandées (aucune ne touche un calcul)

1. **Fermer la forme de deux champs de la sortie.** `exiger_sortie` ne contrôle de `comptes_des_lectures` et de `preuve_d_ordre` que les clés de premier niveau. Un texte libre y passe : l'essai du module le montre lui-même, qui n'obtient le refus d'un champ `note` ajouté que parce que sa valeur ressemble à un chemin. À faire : `comptes_des_lectures`, par moniteur et par condition, les cinq clés que rend `comptes_des_lectures` (lignes 1082 à 1098), des entiers, et les clés des deux tables prises dans les listes fermées des états de la balise et des jointures ; `preuve_d_ordre`, une date au format du journal et une empreinte de soixante-quatre signes ou nulle (la date vient d'une cellule du journal que rien ne valide, ligne `exiger_ouverture`). Un artefact par garde.
2. **Épreuve de forme : deux objets qui n'ont pas la forme d'une livraison.** (a) `comptes_des_lectures` y vaut `{"lectures": 0}` par condition, sans les quatre autres clés ; (b) le fichier par unité de chaque cas ne porte que les lignes d'un seul moniteur (192 lignes au cas D), alors que la sortie porte vingt lectures de cinq moniteurs. L'instance d'analyse éprouverait ses contrôles sur une forme que la course ne rendra pas. À refaire après la correction 1, avec les cinq moniteurs au fichier par unité, dont un à l'unité de l'épisode.
3. **Borne haute finie, et les deux gardes qui ne mordent pas.** Au cas A, la garde de forme accepte pour la borne haute tout flottant, un nombre non fini compris (ligne 1165) ; exiger un nombre de 0 à 1, avec son artefact. Garder une seule des deux gardes de la sortie, ou donner à chacune un artefact qui la distingue.
4. **Trois phrases de `nombres_rendus` qui ne disent plus la version 9** (elles sortent dans la livraison) : « le score » alors que la forme retenue rend un rang ; « rendus aussi quand le moniteur n'est pas calculable pour l'une de ces deux raisons » alors qu'au cas D il est dit calculable. À récrire.

**Remarques, sans correction exigée.**
- L'empreinte du module est calculée à l'assemblage, sur le fichier du disque, non à l'import. La calculer aussi à l'import et exiger l'égalité fermerait le cas d'un fichier changé pendant la lecture.
- La lecture commune écrit et scelle le fichier par unité avant la garde et l'écriture de la sortie (lignes 1378 à 1384) : si la garde refusait, le fichier par unité resterait seul, et un second jeu serait refusé. Sans effet sur l'analyse, qui prend l'empreinte du fichier dans la sortie scellée ; à dire dans la règle de reprise du lanceur.

## 7. Pour la mère

1. Commander la version 10 sur les corrections 1, 3 et 4, puis l'épreuve de forme refaite (correction 2) ; je vérifie les corrections.
2. Transmettre à la relance la pièce sans interne ci-jointe, et lui faire inscrire au texte la valeur de `calculable` aux cas D et E.
3. Consigner l'échec attendu de la garde statique des essais de la version 8.
4. Reporter le commit dans la pièce sans interne v2 du développeur (erratum).
