# Vérification de la v4 du script de lecture contre le bruit du pilote 4 — rapport

Vérificateur : le relecteur des v1 à v3 (rapport sur la v3 : `rapport-relecture-script-lecture-v3.md`, `fcd43854…`),
relancé par conv-audit pour une vérification ciblée ; il n'a écrit ni le script ni ses essais. 26 octobre 2026 ;
vérification commencée à 08:34:18 UTC ; cet en-tête est écrit à 08:47:10 UTC (heures lues sur `date -u`, la seconde dans
la commande même qui écrit ce fichier). Demande : (1) la v4 ne diffère de la v3 que par la correction de RSL3-01, les
chaînes de version et la documentation ; (2) les cas de fausse alerte de RSL3-01 ne refusent plus, sous 3.11, 3.12 et
3.13, et les plantations d'une valeur propre à l'autre course sont toujours refusées ; (3) RSL3-02 au LISEZMOI ; (4) les
commandes du § 5 passent telles qu'écrites, noms de sortie en `-v4`.

## Verdict

**utilisable tel quel.** (1) La v4 ne diffère de la v3 que par la correction de RSL3-01 (celle que proposait la
relecture, telle qu'écrite), les chaînes de version et la documentation. (2) Les cas de fausse alerte ne refusent plus,
sous 3.11.17, 3.12.3 et 3.13.17 ; les plantations d'une valeur propre à l'autre course sont toutes refusées. (3) RSL3-02
(a), (b) et (c) sont traités au LISEZMOI. (4) Les commandes du § 5 passent telles qu'écrites et écrivent des noms en `-v4`.

## 1. Pièces

Copie `/var/tmp/relecture-script-lecture-pilote4-v3/copie-v4/`, égale à l'octet à `/var/tmp/lecture-pilote4-v4/`,
compagnons vérifiés :

| fichier | sha256 |
|---|---|
| `lire_pilote4_v4.py` | `a2d09ef6706fdf7f2f2b8a081a7a8f35e173c33e73e6da2c32f10af98e05ea9a` |
| `essais_lire_pilote4_v4.py` | `ea95b6a6517feeaf99bdf844c77b08a6ce3b6950cdfc3d54bc927471940da232` |
| `essais-lire-pilote4-v4.log` | `7a9b798b795ef57487616f787730571a563fc1810e33ca3151b0dd03c9787c0e` |
| `LISEZMOI-script-lecture-v4.md` | `1225ac433768a0d742e425591908f66c2f19d14bd7feaa56d3897feb8b3f67b9` |

## 2. La v4 contre la v3 (point 1)

`diff -u` et arbres syntaxiques sans les chaînes de documentation (`journaux/comparaison-v3-v4-v1.txt`). Fonctions qui
diffèrent : `verifier_separation`, par la correction seule (deux lignes qui forment l'ensemble des écritures — JSON, quatre
décimales, six chiffres significatifs — de chaque nombre du document du fichier, score du noyau compris, plus les fractions
exactes de ses valeurs p ; dans la boucle, `if jt in ecritures_x or jt in TEXTES_FIXES: continue` avant la recherche, ce
qui garde l'exclusion des textes fixes de la v3) ; et, par les seules chaînes de version, `document` et `md_entete`
(titres « — v4 »), `mode_test` et `mode_test_final` (noms en `-v4`), `principal` (aide) et la constante `VERSION`. Changés
aussi, sans effet sur le code : la chaîne de documentation du module (paragraphe de la v4, noms en `-v4`) et celles de
`holm` et de `verifier_separation`. Toutes les autres fonctions et constantes, calculs compris, sont identiques.

## 3. Fausses alertes et plantations (point 2)

| essai | 3.11.17 | 3.12.3 | 3.13.17 | v3, pour mémoire |
|---|---|---|---|---|
| sur archives : score du noyau de M (g2, conscience d'évaluation) mis à 0,33332, écrit 0,3333, une proportion de S | écrite | écrite | écrite | refus |
| dans le processus, série A (sans divergence) | 0 refus sur 500 | 0 sur 500 | 0 sur 500 | 0 sur 2 000 |
| série B (score du noyau tiré au hasard) | 0 sur 500 | 0 sur 500 | 0 sur 500 | 2 sur 2 000 |
| série C (score choisi sur une proportion de l'autre course) | 0 sur 198 | 0 sur 198 | 0 sur 198 | 185 sur 194 |
| série D (score des mêmes réponses moins une) | 0 sur 1 000 | 0 sur 1 000 | 0 sur 1 000 | 129 sur 2 000 |
| garde de la v4 telle quelle (outil de la correction proposée, enveloppe retirée) : divergences D et C | 0 sur 500 et 0 sur 500 | idem | idem | — |
| même outil : écritures propres à l'autre course plantées (proportion à quatre décimales au Markdown, en nombre JSON ; valeur p en fraction) | 2 977 refusées sur 2 977 | idem | idem | — |
| sur archives, dans le processus du script : proportion de S au Markdown, en JSON, valeur p de S en fraction ; entier de S | — | — | refus, refus, refus ; écrit (non cherché, déclaré) | idem |

Recherche propre aux outils de la vérification : dans les séries C et D, une écriture d'une proportion de l'autre course
paraît dans le fichier d'une course, toujours comme écriture d'un nombre de ce fichier, son score du noyau divergent
(149 fichiers en C, 59 en D) ; aucune autre écriture de l'autre course (0, sous les trois interpréteurs ;
`journaux/verification-v4-garde-series-c-d-py*-v1.log`). Les premiers passages (`verification-v4-garde-en-processus-py*-v1.log`,
code 1, « aucune fuite trouvée : False ») comptaient ces coïncidences parmi les fuites : leur recherche ne mettait pas à
part les écritures des nombres du fichier ; ce n'en sont pas. Les autres cas de la relecture de la v3, rejoués sur la v4
(noms en `-v4`), restent conformes : 7 sains sur 7, 15 artefacts sur 15 sous 3.11.17 et 3.12.3, 18 sur 18 sous 3.13.17
avec les injections (séparation entre parts et entre courses, série tirée au hasard, options, noms, écriture sans liens
durs, interruption) ; aucun cache dans les copies ni dans le noyau.

## 4. RSL3-02 au LISEZMOI v4 (point 3)

(a) Après un code 4 ou 130 : § 5, l. 160–163 (SORTIE à ne pas tenir pour non écrite, à ne pas réutiliser ; provisoire
resté nommé sur la sortie d'erreur). (b) Fenêtre de deux instructions : § 6, l. 165–171, pour les provisoires cachés et,
sans liens durs, pour les définitifs, avec le message trompeur ; les lignes citées (1143–1144, 1156–1157, 1356) sont
justes dans la v4 ; code inchangé, comme demandé. (c) `R` relatif : § 5, l. 98–100, et le commentaire de la ligne `R=`.
Conformes. Le LISEZMOI traite aussi O1 et O2 (§ 4) et récrit le § 3.2 de la v3 (§ 3).

## 5. Commandes du § 5 (point 4)

Les six blocs, extraits du LISEZMOI v4 par le harnais, lancés tels qu'écrits depuis la racine d'une copie de lancement
inventée (`R` relatif), `python3` remplacé par l'interpréteur essayé, `<…>` par les dossiers inventés, la ligne `unset`
par la définition de la variable d'essai (banque inventée) : `lire_pilote4_v4.py: OK`, essai-banque conforme, quatre
« code 0 » ; dossiers `lecture-test-M-v4`, `lecture-test-S-v4`, `lecture-test-final-holm-quatre-v4`,
`lecture-test-final-holm-deux-v4`, portant `lecture-pilote4-gemini-v6-2-v1-tentative2-test-v4`,
`lecture-pilote4-gemini-v6-2-s-v1-test-v4`, les deux `…-test-final-holm-quatre-v4` et
`lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-holm-deux-v4` (JSON, Markdown, compagnons) ; fichiers d'état d'une
ligne sans nombre décimal ; fichiers d'erreur sans autre ligne que celle de l'essai ; copie inchangée ; sous les trois
interpréteurs. Le cas garde le libellé hérité du harnais de la v3 (« commandes du LISEZMOI v3 § 5 ») ; il lance bien le
§ 5 du LISEZMOI v4.

## 6. Hors du champ ; interdits ; pièces

Hors du champ de cette vérification : une relecture complète ; la batterie de l'auteur n'est pas rejouée (son journal,
lu : 19 sains sur 19 et 65 artefacts sur 65, quatre fois ; 51 mutations sur 51, dont M51, la garde de la v3). Interdits
tenus : aucune donnée de la banque, aucune archive ni pièce d'un pilote réel, aucun dossier `donnees/`, `runs/`, `diag/`,
`pilotes/` réel ; aucun `git`, réseau, sous-agent ni clé ; données inventées ; Python avec `-I` ; heures lues sur `date -u`.
Écrit sous `/var/tmp/relecture-script-lecture-pilote4-v3/` seulement (`copie-v4/`, `outils/`, `journaux/`, ce rapport, le
journal, la liste d'empreintes) ; l'environnement d'outils a gardé sous `/tmp/claude-0/…/tasks/` la sortie d'une commande
d'attente lancée en arrière-plan (une heure).

Pièces, sous `/var/tmp/relecture-script-lecture-pilote4-v3/` : ce rapport et son compagnon ; `journal-verification-v4.log`
(`a0a965606ffaffd7d205f582cda3ec35ed103fac371ef53ff38b2682bb316cda`, recopie des journaux de la vérification) et son
compagnon ; `EMPREINTES-verification-v4.txt` (`10fca64ecaa60a9215534cd033de27529aa5f4e7f98b05b6a13a210bad3fddf4`) et son
compagnon ; outils `artefacts_verification_v4.py` (`927ac9e5…`, le harnais de la relecture de la v3 aux noms de la v4),
`garde_en_processus_v4.py` (`5715d7e1…`), `garde_en_processus_v4c.py` (`6bf29c4e…`), `verification_v4_plantations.py`
(`742902f5…`). Dossiers de travail effacés.
