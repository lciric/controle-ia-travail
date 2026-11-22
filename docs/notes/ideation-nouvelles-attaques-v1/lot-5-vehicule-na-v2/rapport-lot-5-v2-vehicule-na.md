# Rapport du développeur — véhicule NA-1, lot 5 v2 (registre des tentatives d'appel, repli) — v1

Développeur du lot 5 v2 du véhicule NA-1, modèle O (reprise après le refus de classifieur d'un premier développeur). Écrit le
2026-11-22. Aucun appel de modèle, aucun réseau, aucune dépense, aucune clé ; données factices seules ; rien d'écrit dans un
dépôt. Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/e2c3ce0b-40f3-55d3-a6bf-333c05f6ccd1/scratchpad/vehicule-na-lot-5-v2/`.

## 1. Verdict

`registre_na_v2.py` porte l'interface (`interface-lots-5-6-7-repli-v1.md`) **et son erratum 1**
(`erratum-1-interface-lots-5-6-7-repli-v1.md`, ajouté à ma liste en cours de travail par la session qui m'a lancé). Il refuse
une ligne incomplète ou une valeur hors des listes fermées. Il dit en clair quand on lui donne l'ancien format. Il distingue
les lignes `tentative` et `fiche` (`type_ligne`). Sur les seules lignes `fiche`, il rend le registre servi et la garde du
coffre **égaux à l'octet** à ceux du v1. Résultats : **115 essais passent ; 54 mutations sur 54 sont tuées** ; le témoin non
muté passe ; le témoin inerte survit. **Réserve majeure** : ces essais ont tourné sur un banc où les lots 1 à 3 sont
remplacés par des doublures (§ 4). Il reste à les rejouer sur une application réelle.

## 2. Livrables

| fichier | rôle |
|---|---|
| `paquet/orchestrator/pole/registre_na_v2.py` | le module (459 lignes) |
| `paquet/orchestrator/essais/aides_na_lot5_v2.py` | aides d'essai, factices |
| `paquet/orchestrator/essais/test_na_lot5_v2_registre.py` | 115 essais |
| `paquet/orchestrator/essais/mutations_na_lot5_v2.py` | 54 mutations, un témoin inerte |
| `jouer_banc_lot_5_v2.py` | monte le banc, vérifie les modules v1 contre le manifeste v1, joue les essais |
| `banc-doublures/orchestrator/pole/*.py` | quatre doublures d'essai déclarées (§ 4) |
| `journal-essais-na-lot-5-v2.txt`, `journal-mutations-na-lot-5-v2.json` | journaux |
| `table-empreintes-dossier-na-lot-5-v2.txt` | table d'empreintes ; un compagnon `.sha256` par fichier livré |

Le lecteur et le contrat n'ont **pas de v2** : le registre ne leur demande rien de neuf. `verifier_registre_servi_na_v1`
reste inchangé, puisque le registre servi est le même à l'octet. Le dossier `copie/` est une copie non modifiée de
l'orchestrateur de base ; `banc/` est le banc des essais.

## 3. Ce que le code porte (numéros de ligne de `registre_na_v2.py`)

- **Une ligne** : `type_ligne`, les champs du v1 et ceux de l'interface, **tous présents**, à `null` quand ils sont sans
  objet (`CHAMPS_LIGNE`, `verifier_ligne`, l. 192). Il y a **une ligne `tentative` par tentative**, et elle seule porte
  l'appel et le coût. Elle est suivie de ses lignes `fiche`, qui recopient ses champs et portent les champs de fiche ; leur
  accord avec la tentative est vérifié (l. 301).
- **Listes fermées** :
  - `type_ligne`, `espece` (les dix rôles), `classe_issue` (les quatre classes d'appel de la V9, plus la classe de repli),
    `classe`, `rang_repli` ∈ {0, 1, 2} ;
  - `case` : parmi les cases servies données, ou `null` ; `modele_demande` : parmi les identifiants par rôle donnés
    (`contexte_de`, l. 135).
- **Trois fins de chaîne** (`_clore`, l. 274 ; erratum, points 1 à 3) :
  - *servie* : les refus qui précèdent portent la classe de repli ;
  - *sans réponse* : `modele_servi` à `null`, `sans_reponse`, « réponse illisible » ;
  - *trois refus* : « refus du modèle », sans fiche (arrêt n° 1).
  Un rôle autre qu'un proposeur, servi par repli, garde la classe de son rôle.
- **`categorie_refus` est la seule à prendre `null` quand elle manque** (l. 377) ; elle n'est jamais devinée (mutation
  M2-12).
- **Chaîne écrite en un seul appel**, vérifiée entière avant toute écriture (`ajouter_chaine`). Chaque artefact refusé
  laisse le fichier intact.
- **Comptes** : `lignes_fiche` (l. 420) sert à tout compte de fiches, y compris la garde du coffre ; `lignes_tentative`
  (l. 425) sert aux appels et aux coûts.
- **Filiation** : `null` si la fiche dit « aucune », la chaîne telle quelle sinon (l. 116). Seule une fiche passée la porte ;
  M1 bis, au lot 7, en juge la validité.
- **Ancien format** : `RegistreAncienFormat` (l. 88) couvre une ligne du v1 ou une ligne sans `type_ligne`, un registre v1
  relu (l. 400), des lignes v1 données aux comptes (l. 412) et l'appel `ajouter_fiche`. L'écriture directe d'une ligne est
  refusée.
- **Registre servi et garde du coffre** : calculés par le code du v1 sur les lignes `fiche` ramenées à sa forme. Rien de
  l'espèce, du modèle, du coût ni du type n'entre au registre servi. Les fiches servies par repli y entrent, et entrent aussi
  dans la garde (P8 ; mutation M2-43).

## 4. Banc à doublures : réserve et rejeu exigé

La copie de `/home/user/lciric/ideation-organism/orchestrator/` ne porte pas les lots 1 à 3 : le script d'application du
v1 refuse, faute de `identifiants_na_v1.py`. Les paquets du lot 2 v5 et du lot 3 v3 ne sont pas dans ma liste, et **je ne
les ai pas cherchés**. Il me faudrait les dossiers de ces paquets, qui posent `orchestrator/pole/identifiants_na_v1.py`
(`38d9860b…`), `tirage_na_v4.py` (`55d6587e…`), `requete_na_v3.py` (`60d40f76…`), `journal_na_v3.py` (`c5a66c05…`) et les
autres dépendances du manifeste du lot 5 v1.

Les quatre doublures sont déclarées en tête comme telles. Elles ne portent que les noms publics lus, et leur encodage comme
leur permutation **ne sont pas ceux des lots 1 et 2**. Les cinq modules du lot 5 v1, eux, sont les vrais, vérifiés contre
leur manifeste.

**Rejeu à faire par le vérificateur**, sur une copie où les lots 2 v5, 3 v3 et 5 v1 sont posés :
1. `python -B jouer_banc_lot_5_v2.py BASE BANC JOURNAL.txt`, sans `--doublures`. Chaque dépendance est alors vérifiée à son
   empreinte, et le banc refuse sinon (j'ai joué cet artefact sur la base sans lots : refus obtenu).
2. Puis `essais/mutations_na_lot5_v2.py`, dans le banc.

## 5. Essais, mutations, différentiel

- **R5** : chaque garde a son artefact et au moins un cas sain. Les cas sains d'écriture sont 11, dont les trois fins de
  chaîne, le rôle non proposeur servi par repli et deux chaînes successives ; les relectures et le contexte ont aussi leurs
  cas sains.
- **Mutations** : 54 ; chacune retire une garde par un texte exact unique ; toutes sont tuées. R4 : le résultat est propre.
  Aucune mutation n'a été ajustée pour être tuée. Sur la première version (avant l'erratum), 45 mutations sur 45 avaient été
  tuées ; ce premier journal est remplacé, non livré.
- **Différentiel avec le v1**, à mêmes fiches dans les deux registres :
  - les lignes `fiche` sont égales à la forme v1, champ à champ ;
  - le registre servi est égal à l'octet (générations 2 et 3 ; comptes permutés ou non ; avec ou sans repli), et
    `verifier_registre_servi_na_v1` l'accepte ;
  - les lignes `tentative` (trois refus, sans réponse et portier compris) ne changent rien ;
  - la garde du coffre est égale aux générations 1 à 3.
- **Défaut du v1 que corrige la v2** (erratum, point 4) : un essai montre que le code du v1, appliqué à toutes les lignes v2,
  compterait les lignes `tentative` et diluerait la garde (pas d'arrêt), alors que la v2 arrête.
- **Différentiel d'interface** :

  | v1 | v2 |
  |---|---|
  | `RegistreTentatives(dossier, nom)` | `RegistreTentativesV2(…, *, generation, cases_servies, modeles_demandes)` |
  | `ajouter_fiche(issue)` | `ajouter_chaine(tentatives, fiches)` |
  | `lire_registre_tentatives` | `lire_registre_tentatives_v2(…)` |
  | `fabriquer_registre_servi`, `garde_du_coffre` | les mêmes fonctions, avec le suffixe `_v2` |
  | — | `lignes_fiche`, `lignes_tentative`, `chaines_de` (neuves) |

  Le v1 n'est pas touché.

## 6. Ce que la lettre ne fixe pas (remarques ; interface et erratum non changés)

1. **Trois refus** : l'erratum donne la classe « refus du modèle » à la **dernière** tentative. J'ai donné la même classe
   aux deux premières, puisque la classe de repli serait fausse. C'est ma lecture, à confirmer.
2. **Refus suivi d'une tentative sans réponse** : le refus garde la classe « servi par repli », alors qu'il n'y a pas eu de
   service. L'erratum ne dit rien de ce cas. À trancher.
3. **La « classe refus » de la V9** est lue comme « refus du modèle ». La « classe de défaut de l'appel sans réponse » est lue
   comme « réponse illisible » (V9, l. 99).
4. **Coût d'une tentative sans réponse** : l'erratum fixe « la réserve entière », mais le registre ne la connaît pas. Il
   vérifie la forme du coût, non sa valeur ; c'est au lot 6 v4 de l'écrire juste.
5. **Conception v5, § 2.6** : elle dit « rien du coût, rien de l'espèce » pour le registre des tentatives ; l'interface
   l'écarte. Le registre servi n'en porte toujours rien. Écart à déclarer à l'additif.
6. Un **proposeur sans case** est refusé, puisque sa requête est assemblée par case. La valeur `null` de `case` est admise
   pour les autres rôles.
7. **« Jamais un nom de modèle en clair »** : le code ne détecte pas un nom de modèle. Il s'appuie sur la liste fermée des
   identifiants par rôle que donne la configuration. `modele_servi` reste dans le dossier de sortie.
8. Les **fiches servies par repli** entrent au registre servi (V9, l. 63, lecture scellée P8). Proposition à confirmer par
   la mère.

## 7. Règles de lecture tenues

J'ai lu, chacun par son chemin complet, les fichiers de la liste fermée et l'erratum ajouté, par tranches de moins de
150 lignes. Je n'ai listé que mon dossier de sortie. Je n'ai ouvert aucun fichier de l'orchestrateur ni lu le dossier
`resultats/` ; rien sous `/root/.claude/`. Aucun refus d'outil ni de classifieur.
