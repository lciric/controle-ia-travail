# Vérification des corrections de la seconde programmation (v3) et du couple P1 du premier programme (barreau 5) — v1

Écrite le 20 novembre 2026 par le contre-lecteur de la seconde programmation, Claude Opus 5.5 (`claude-opus-5-5`), sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`. Elle suit le même mandat (`8655a5a7…`) et vérifie ma contre-lecture `contre-lecture-seconde-programmation-v1.md` (`35254454…`). Pièce d'instrument (classe B). Aucune donnée, ni réseau, ni dépense, ni commit.

## Verdict

**Conforme.** Les couples S1 à S11, T1 à T10 et P1 sont appliqués à la lettre. Rien d'autre n'a changé qui touche un calcul. Sur les 20 000 mondes de mon croisement, les deux programmes corrigés ne présentent aucun désaccord.

Le juge de l'épreuve à vérité plantée ne passe pas `refus_attendu`, et pour cause : il n'appelle pas le comparateur (voir § 5). Ce n'est pas un défaut des deux programmes vérifiés ici.

## 1. Empreintes, toutes égales à celles qu'annonce la mère

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/seconde_programmation_v3.py` | `aef13d08a45ea7362e9e4419ed657246779ca1e832966833629bfcfc06ed620b` |
| `tests/test_barreau5_familles_seconde_programmation_v3.py` | `b1e83ceed0b88bd8247c84ff18e9a293ac6f166844b548b21aeac9886136d7d3` |
| `src/controle_ia/barreau5_familles/lecture_v1.py` | `ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f` |
| `tests/test_barreau5_familles_lecture_v1.py` | `6ed14bdbdb895cedb759ce149dfba99a3c439f28b31a570ee364030baae5e6d7` |
| `rapport-seconde-programmation-v2.md` | `5c573adc9c0bac4a20aba88a707ac89bd8a4372375217ab7689e054f1d8d428d` |
| `rapport-developpeur-code-lecture-v5.md` | `473d340da7d2ec31cb1fab9d0faba178b85c63751f8b197aa84a6dbc067ef430` |
| `src/controle_ia/barreau5_familles/juge_verite_plantee_v1.py` | `37e136b087f9c9e39e318c45b356c48dc9a4e4b9a1f601b5b78fec5bb7135e1c` |

Je n'ai pas vérifié les empreintes de l'outil de mutations v3 du programmeur ni de son journal, ni rejoué cet outil. Des deux rapports, je n'ai lu que les lignes de résultats et la réserve sur S4.

## 2. Les couples, à la lettre (questions 1 et 2)

**Premier programme.** `lecture_v1.py` a l'empreinte `ed0999df…`. C'est exactement l'empreinte de la copie que j'avais faite de `d877d2de…`, avec le seul couple P1, par `appliquer_couples_v1.py`. Le fichier est donc `d877d2de…` plus P1, octet pour octet : rien d'autre n'a changé.

**Seconde programmation : `diff` de la v2 (`29c71ef9…`) à la v3.** Le diff contient S1, S2, S3, S4, S5, S6, S7, S8, S9, S10 et S11, chacun tel que je l'ai écrit. S10 est placé après la ligne d'usage, comme dans le couple. S'y ajoutent, sans calcul :
- l'en-tête du module ;
- la ligne d'usage, qui porte le nom v3 et le drapeau `--refus-attendu` ;
- deux commentaires, sur S3 et sur S4 ;
- la docstring de `comparer`, qui dit maintenant le drapeau.

**Essais : `diff` de la v2 (`c0e1b3fc…`) à la v3.** Le diff contient T1 à T10, tels qu'écrits. S'y ajoutent :
- l'en-tête, le nom du module importé et les chemins de `/dev/shm`, passés en v3 ;
- trois artefacts de plus, sans changer de règle : un code 2 avec un résultat, dans un monde à refus planté ; `--refus-attendu` avec un fichier ; `comparer_fichier` avec et sans refus planté.

Le programmeur dit que l'état après les seuls couples portait les empreintes `820c3d5c…` et `03ed2d9c…`, celles que j'avais annoncées. Je ne peux pas refaire ce constat sur l'état intermédiaire, qui n'est pas versé ; le `diff` dit la même chose.

**Réserve du programmeur sur S4** (`rapport-seconde-programmation-v2.md`, ligne 31). La lettre exacte du motif reste celle du premier programme. Je suis d'accord : si la mère veut la fixer dans le texte, il faut une ligne d'addendum, et aucun des deux programmes n'a à changer.

## 3. Croisement sur les 20 000 mondes (question 3)

J'ai rejoué `croisement_v1.py` (`8274223b…`), même entropie, avec le premier programme du paquet (`ed0999df…`) et la seconde programmation v3 (`aef13d08…`) ; le journal `journal-croisement-v3-et-p1-v1.json` porte les deux empreintes.

**Accord exact sur les 20 000 mondes : zéro désaccord** (C 1 361, D 1 231, E 800, N 6 051, NI 10 449, S 108).

## 4. Essais et mutations (question 4)

- **Essais** de la seconde programmation v3 : 139 passés. Essais de `lecture_v1.py` : 102 passés. Le rapport v5 annonce 244 essais, mais sur les six fichiers d'essais de la lecture ; il compte lui-même 102 essais pour ce fichier.
- **Mes 5 mutations** (X1 à X5), rejouées sur la v3 par `mutations_contre_lecture_v2.py`. C'est mon outil v1, avec les seuls chemins changés pour la v3. Les cinq « avant » sont présents une fois chacun ; cas sain passé ; 5 mutations sur 5 attrapées (`journal-mutations-contre-lecture-v2.json`).
- **Temporaires.** Le dossier `/dev/shm/b5f-contre-lecture-mutations-v2` est effacé par l'outil, à son chemin écrit en toutes lettres.

## 5. Le juge et `refus_attendu` (question 5)

**Il ne le passe pas.** `juge_verite_plantee_v1.py` n'importe pas la seconde programmation et n'appelle pas `comparer`. Il ne lit que des rendus traduits, un par monde (`"refus": bool`, `motif_refus`, issue, `motifs_D`, …), et les juge contre les règles gelées.

L'accord exact du point 11 reste donc à jouer à part, par l'agent qui joue l'épreuve. Il doit passer à la seconde programmation `--refus-attendu` pour les mondes dont la vérité porte `attendu.refus` vrai, et seulement pour eux.

Lu en passant, sans doubler la contre-lecture de la fabrique, à transmettre à cette contre-lecture : le juge recopie `W_GELE = {…, 95: {7: 2, 6: None}}` (ligne 59). Pour six familles au niveau de 95 %, il ne donne aucune somme admise, alors que les deux programmes donnent w = 0, et ma contre-lecture aussi (§ 1). À six familles présentes dans une épreuve, le juge tiendrait pour incohérente une épreuve « séparé » à w = 0. Aucun monde écrit de V0 à V12 n'a six familles dans une épreuve, à ma lecture du point 11.

## Mes fichiers

Ajoutés dans `outils-contre-lecture-seconde-programmation-v1/` : `mutations_contre_lecture_v2.py`, `journal-mutations-contre-lecture-v2.json` et `journal-croisement-v3-et-p1-v1.json`. Leurs empreintes sont dans leurs compagnons `.sha256`.

Aucun refus d'outil, de classifieur ni de garde n'a eu lieu.
