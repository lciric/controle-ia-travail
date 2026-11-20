# Rapport de la seconde programmation du dénombrement exact et de la table des issues (barreau 5) — v2

Écrit le 20 novembre 2026 par le programmeur de la seconde programmation, Claude Fable 5.2 (`claude-fable-5-2`), sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`. Pièce d'instrument. Il complète le rapport v1 (`93bb0f5f…`), qui reste vrai hors de ce qui suit.

## En bref

- La contre-lecture (`contre-lecture-seconde-programmation-v1.md`, `35254454…`, vérifiée, lue en entier) rend « conforme après ces corrections ». Ses couples S1 à S11 et T1 à T10 sont tous appliqués, à la lettre, dans des fichiers neufs en v3.
- Preuve de la lettre : après les seuls couples, le module porte l'empreinte `820c3d5c…` et les essais `03ed2d9c…`, celles que la contre-lecture annonce (§ 7). Les retouches de version sont venues ensuite.
- 139 essais passent ; 86 mutations sur 86 sont attrapées, cas sain passé.
- Aucun couple n'est jugé faux. Une réserve sur S4, sans refus de l'appliquer (ci-dessous).
- Le couple P1 vise le premier programme : non appliqué par moi. Tant qu'il ne l'est pas, le motif « niveau non atteignable » reste en désaccord entre les deux programmes (E3 sous six familles).

## Table de traitement des couples

| couple | objet | état | où |
|---|---|---|---|
| S1 | motif ordinaire de NI : l'épreuve nommée seule | appliqué | `table_des_issues` |
| S2 | « 0 famille » | appliqué | `_familles` |
| S3 | un seul motif de force, « (E2a, E2b) » | appliqué | `table_des_issues` |
| S4 | motif de la sonde en échec : « sonde en échec : épreuves non calculables ([motif]) » | appliqué, avec réserve | `table_des_issues` |
| S5 | le comparateur passe le motif de l'instance | appliqué | `comparer` |
| S6 | signature, `refus_attendu` | appliqué | `comparer` |
| S7 | code 2 hors d'un refus planté : désaccord | appliqué | `comparer` |
| S8 | code 0 dans un monde à refus planté : désaccord | appliqué | `comparer` |
| S9 | `comparer_fichier` transmet le drapeau | appliqué | `comparer_fichier` |
| S10 | drapeau `--refus-attendu` | appliqué | `main` |
| S11 | drapeau transmis | appliqué | `main` |
| T1 à T10 | essais des couples | appliqués | essais v3 |
| P1 | motif « niveau non atteignable » du premier programme | non appliqué : hors de mon champ | — |

**Réserve sur S4.** Le point 9 du plan dit : « sonde en échec (perte non finie) : ses épreuves sont « non calculables », issue N avec ce motif ». La contre-lecture lit « ce motif » comme la cause et le mot réunis, avec une confiance de 0,7 ; ma lecture v2 gardait le seul mot entre guillemets. Les deux se défendent ; celle de la contre-lecture a pour elle de garder la cause, que la phrase NI et le jury ont à lire, et d'accorder les deux programmes. Je l'applique. La lettre exacte du motif (ordre des mots, parenthèse) reste celle du premier programme, non celle du texte : si la mère veut la fixer, c'est une ligne d'addendum.

## Ce qui a changé après les couples

Dans le module : l'en-tête (version 3, empreintes), l'usage de la ligne de commande (nom v3, drapeau), trois commentaires (motifs de D, sonde en échec, docstring de `comparer`, qui dit désormais `refus_attendu`). Aucun calcul.

Dans les essais : l'en-tête, l'import de la v3, les chemins temporaires, et cinq assertions de plus (drapeau avec un fichier ; code 2 avec un résultat dans un monde à refus planté), demandées par les mutations C08, C26 et C27.

## Outil de mutations

`mutations_seconde_programmation_v3.py`, 86 mutations. O05, M01 et M05 sont gardées, sur les « avant » du code corrigé. S'ajoutent : O05b, O16, M01b, M05b, M06, C13b, C24 à C29 pour les couples ; X1 à X3 pour les mutations de la contre-lecture (X4 y est M01b, X5 y est F06). Un premier passage à blanc, journal dans mon bloc-notes, a laissé passer C08 (code 2 avec un résultat écrit, que le couple S7 masquait) : une assertion a été ajoutée, et le passage final attrape tout.

## Ce qui reste à la mère

1. P1, ou son contraire, pour le motif « niveau non atteignable ».
2. Le juge de l'épreuve à vérité plantée doit passer `refus_attendu` (ou `--refus-attendu`) pour les mondes où un refus est planté, et lui seul le sait.
3. Dans le dossier des outils restent, non scellés et sans objet : `mutations_seconde_programmation_v1.py` et `journal-mutations-seconde-programmation-v1.json`.

## Tenue

Écriture par les seuls outils d'écriture et d'édition ; une commande à la fois ; aucun refus d'outil ; aucune donnée lue ; premier programme jamais joué ni lu ; aucun commit. Temporaires de `/dev/shm` effacés, vérifié.

## Fichiers et empreintes

| fichier | sha256 |
|---|---|
| `src/controle_ia/barreau5_familles/seconde_programmation_v3.py` | `aef13d08a45ea7362e9e4419ed657246779ca1e832966833629bfcfc06ed620b` |
| `tests/test_barreau5_familles_seconde_programmation_v3.py` | `b1e83ceed0b88bd8247c84ff18e9a293ac6f166844b548b21aeac9886136d7d3` |
| `outils-seconde-programmation-v1/mutations_seconde_programmation_v3.py` | `de72ef58c126cb88c0987804a06c05462a328de33949f6f1e43779bfa631687d` |
| `outils-seconde-programmation-v1/journal-mutations-seconde-programmation-v3.json` | `324b08e9d786865f675a78fbc991c71f3c9368b8d3b447532925fb08743e9500` |

Ce rapport est scellé par son compagnon `.sha256`.
