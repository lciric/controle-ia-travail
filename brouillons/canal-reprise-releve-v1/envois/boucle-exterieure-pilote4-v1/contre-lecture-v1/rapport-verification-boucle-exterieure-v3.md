# Vérification de la v3 de la boucle extérieure du pilote 4 (registre v3, protocole v2, briefs v2, spécification du relevé (B) v1)

## En-tête

- **Vérificateur** : le sous-agent (`claude-opus-5-5`) qui a contre-lu la v2 (rapport `2eb11e6a…`), relancé par conv-audit
  le 26 octobre 2026. Je n'ai écrit aucune des pièces vérifiées.
- **Heure** : rapport écrit le 2026-10-26 à 05:30:11 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Le début de
  la vérification n'est consigné par aucune commande d'écriture.
- **Pièces** : `/var/tmp/contre-lecture-boucle-exterieure-pilote4-v2/fournis/`, treize entrées sur treize conformes à
  `../EMPREINTES-fournis-v1.txt` (`1203fbc8…`), vérifiées avant lecture ; compagnons des cinq pièces de sortie justes.
  Registre v3 `a5abc176…` ; protocole v2 `0c71a74b…` ; briefs v2 `60553a1b…` ; spécification (B) v1 `3ed32fe8…` ;
  LISEZMOI v3 `218619cf…` ; brief v3 `82b9028d…` ; texte v5 du pilote `1943f39a…` (qui prime) ; LISEZMOI du script de
  lecture v2 `2f328fee…`.
- **Lu en entier** : les huit pièces. **Exécuté** : `sha256sum`, `sha256sum -c`, `ls`, `wc`, `grep`, `date -u`.
  **Non ouvert** : rien hors de ce dossier ; aucun fichier de course, aucun script, aucun score. Aucun `git`, aucun
  sous-agent, aucun réseau, aucune clé. Ce rapport ne contient aucun score, aucun critère ni aucune stratégie de
  classement des tâches.
- Numéros de lignes : ceux des fichiers nommés. « Registre », « protocole », « briefs », « spécification », « LISEZMOI »
  désignent les pièces v3 ; « script v2 », le LISEZMOI du script de lecture v2.

## Verdict

**Utilisable après corrections.**

Les dix-neuf constats sont traités dans les fichiers eux-mêmes, pas seulement dans la table. Aucun constat bloquant ;
cinq à corriger avant usage (CLB3-01 à CLB3-05), trois mineurs (CLB3-06 à CLB3-08). Ce qui reste : la lecture finale ne
correspond pas aux fichiers que le script v2 écrit ; les verdicts des courses M et S sont mis en regard pour décider
d'une correction ; HC-P4-01 a reçu, après la lecture de faits de la course M, une voie de lecture qui tranchera M ;
six points sur sept pour Lazar ne sont pas posés comme des décisions ; le relevé (B) n'a ni cas sain pour la course S
ni règle pour un champ d'identité « absent ».

## 1. Les constats CLB-01 à CLB-19, dans les fichiers

| constat | traité dans les fichiers | où | réserve |
|---|---|---|---|
| CLB-01 | oui | protocole l. 28–30, 107–110, 286–300 ; briefs l. 13–16 ; registre l. 207–211 ; spécification l. 12–13 | CLB3-05 (identité de S) |
| CLB-02 | oui : spécification, condition de démarrage, G11 | spécification ; protocole l. 52–53, 341 ; registre l. 58–62 | script, table de correspondance et essais encore à écrire ; CLB3-05 |
| CLB-03 | oui | registre l. 128–133, 182–186, 341–391 ; protocole l. 221–223 | CLB3-08 (b) |
| CLB-04 | oui | registre l. 79–83, 134–137, 446–456, 510–512 ; briefs l. 75–76, 84–86 | CLB3-06 (a) |
| CLB-05 | oui, dans les textes | protocole l. 44, 101–103, 128, 177–179, 425–431 ; briefs l. 63–64 | CLB3-01 (condition non remplie par le script v2) ; CLB3-02 |
| CLB-06 | oui | protocole l. 212–241, 334 ; briefs l. 169–171, 186–195 | CLB3-08 (d) |
| CLB-07 | oui | protocole l. 334 (G5 c et e), 366–370, 459–466 ; briefs l. 249–257 | — |
| CLB-08 | oui | protocole l. 331, 353–381 ; briefs l. 88–89 | la forge de (A-final) dépend de CLB3-01 |
| CLB-09 | oui | registre l. 525–528 ; protocole l. 435 | — |
| CLB-10 | oui, comme point pour Lazar | protocole l. 270–277, 494 | — |
| CLB-11 | oui | protocole l. 232–234, 278–280, 333 ; briefs l. 190–193 | — |
| CLB-12 | oui | protocole l. 88, 90 ; briefs l. 158–159, 237 | — |
| CLB-13 | oui | protocole l. 89, 145–147 ; briefs l. 11–12, 213–224 | — |
| CLB-14 | oui | registre l. 529–531 ; protocole l. 434–435 ; briefs l. 79, 128–130 | — |
| CLB-15 | oui (code retiré des entrées de l'analyste) | registre l. 63–66, 401–402 ; briefs l. 109–110 | — |
| CLB-16 | oui, (a) à (f) | protocole l. 96, 123–125, 335, 473–475 ; registre l. 187–188 ; briefs l. 18–19, 50–52 | CLB3-08 (c) |
| CLB-17 | oui | registre l. 597–635 | — |
| CLB-18 | oui | registre l. 42–43, 537–544 | — |
| CLB-19 | oui | protocole l. 205, 257–261, 309–310, 438 | — |

## 2. Ce que le script v2 rend vraiment

Fichier `test` : `lecture-<dossier>-test-v2.{json,md}` ; il porte ce que le registre attend (registre l. 68–74 ; script
v2 l. 23–27) : conforme, au nom près, que protocole et briefs écrivent `-v<n>`. Fichier `test_final` : non conforme
(CLB3-01). Libellés demandés au script : absents (CLB3-06).

## 3. `test_final` lu une seule fois, à la fin du compteur

Conforme dans les quatre textes : (A-final) n'est jamais servi avant la fin du compteur (protocole l. 64–65, 101–103,
420–444 ; registre l. 107–112, 224–233 ; briefs l. 68–69, 119–120) ; ce qui se décide à chaque course sans `test_final`
est écrit (protocole l. 441–444). Restent : le contrôle d'union de G8 bis à l'assemblage (CLB3-01 c), et deux traces
écrites ou affichées avant la fin du compteur (CLB3-07).

## 4. Courses M et S

Aucun score ni aucune différence entre M et S ; mais leurs verdicts sont mis en regard pour décider (CLB3-02).

## 5. Points pour Lazar

| point | enjeu | options | recommandation | défaut | dépense |
|---|---|---|---|---|---|
| famille du contre-lecteur (protocole l. 392–399, 492) | à peine dit | deux, sans avantage ni inconvénient | aucune | aucun | peut-être (« famille différente ») |
| graines de plus (l. 491) | posé ailleurs (texte v4, § Décisions, 02:05 : trois options, recommandation) | renvoi | renvoi | aucun | oui |
| plafond des relances (l. 79, 493) | non dit | aucune | aucune | aucun | oui |
| symétrie avant (b) (l. 270–277, 494) | dit (R3) | trois | (a), confiance moyenne | aucun | (c) : oui |
| correction après M sans attendre S (l. 168–170, 496) | non dit | implicites | aucune | « le correcteur attend », écrit « aucun défaut » (l. 170) | non |
| question servie par une relance (l. 495) | non dit | M ou S | aucune | aucun | oui |
| seuils 0,01 et 0,03 (registre l. 357–360 ; protocole l. 503) | dit | trois (registre l. 358–359) | aucune | non dit | oui (une ronde) |

Un seul point est posé comme une décision ; aucun défaut n'est donné à une dépense (CLB3-04).

## Constats

### CLB3-01 — à corriger avant usage — La lecture finale ne correspond pas aux fichiers que le script v2 écrit

- **Où** : registre l. 32–33, 49–55, 76–77, 107–112 ; protocole l. 117–120, 130–133, 338, 345–346, 425–431, 498 ;
  briefs l. 280, 284–285 ; script v2 l. 23–29, 118–135.
- **Ce qui ne va pas** :
  - (a) **Noms.** Les trois textes attendent `lecture-<dossier>-test_final-v<n>` ; le script v2 écrit
    `lecture-<dossier>-test-final-<règle>-v2` (`provisoire`, `holm-deux` ou `holm-quatre`). Les fichiers ne se renomment
    pas (protocole l. 107–110) : le dossier de lecture finale ne s'assemble pas tel qu'il est écrit.
  - (b) **Contenu.** Avec deux courses, le script v2 écrit pour M un fichier `…-provisoire-v2` (seuil 0,0125 : le
    calendrier que N-050 et le registre, l. 107–112, ont retiré) et pour S un fichier `…-holm-quatre-v2` qui porte aussi
    les deux tests de M ; les verdicts définitifs de M ne sont que dans ce fichier de S. Aucun fichier n'est « une
    course, Holm sur quatre, aucune valeur de l'autre » : la condition du protocole (l. 425–431) n'est pas remplie, et
    l'analyste de S s'arrêterait à l'étape 1 de la section 4 (briefs l. 284–285). Risque inverse : le seul fichier
    `test_final` propre à M est le provisoire ; s'il est servi, l'analyste de M passe l'étape 1 et recopie des libellés
    au seuil 0,0125, non ceux de Holm sur quatre.
  - (c) **G8 bis** (protocole l. 338, 345–346) éprouve un partage `test` / `test_final` fait par un outil, avec « l'union
    égale la sortie d'origine » : le script v2 sépare lui-même ; à l'assemblage, sur une course réelle, ce contrôle
    d'union obligerait à ouvrir le fichier `test_final` réel avant la fin du compteur. Aucune garde n'éprouve le partage
    entre M et S du fichier `holm-quatre`.
  - (d) Le registre (l. 32–33, 49–55) et le protocole (l. 117–120, 430–431) décrivent encore le script v1 (« une seule
    sortie », « le fichier actuel porte les deux parts ») et son LISEZMOI comme la sortie réelle.
- **Correction** : écrire les noms du script v2 ; interdire le fichier `…-provisoire-v2` à la lecture finale. Pour deux
  courses, demander une version 3 du script, ou un outil de partage, qui écrive à la fin de S deux fichiers « une course,
  Holm sur quatre, aucune valeur de l'autre » (M compris), avec une garde nouvelle (cas sain synthétique : l'union des deux
  égale les lignes (iii) du fichier d'origine ; artefact : une valeur de l'autre course plantée, refusée), essayée,
  empreintée, exécutée par session-depot sans affichage ; sans elle, pas de lecture finale (le cas
  `--sans-seconde-course`, `…-holm-deux-v2`, est déjà par course). Réécrire G8 bis : sur données synthétiques, l'essai
  « séparation » du script v2 ; à l'assemblage, contrôler le seul fichier `test` réel (ni le mot `test_final`, ni (iii),
  ni valeur p, ni mention d'essai), sans jamais ouvrir le fichier `test_final` réel. Mettre à jour les mentions du script v1.

### CLB3-02 — à corriger avant usage — Les verdicts des courses M et S sont mis en regard pour décider

- **Où** : registre l. 164–166, 278, 283–284, 335, 388, 564–567 ; protocole l. 161–163, 200, 248 ; briefs l. 165–168,
  247–248 ; contre texte v5 l. 65, protocole l. 416–418, registre l. 580–582.
- **Ce qui ne va pas** : le correcteur, la partie B et le journal mettent en regard, fiche par fiche, les verdicts des
  deux courses, et la correction de la ronde 1 en dépend : « verdicts différents selon la course » ne motive rien ;
  « tenue dans une course au moins, sans verdict contraire dans l'autre » motive (HC-P4-01). C'est une comparaison des
  deux courses, même sans score ni attribution. Le texte v5, qui prime, l'interdit, verdicts des agents compris (l. 65) ;
  protocole et registre disent eux-mêmes que M et S « ne sont jamais comparées ». Une section par course dans la pièce de
  correction (G6) ne change pas que la décision est jointe. Remarque : la raison donnée (« questions différentes ») ne
  vaut pas avant la génération 1 ; la question n'est servie qu'à g001 (texte v5, l. 55) ; pour la conception et g000, M
  et S ne diffèrent que par la graine.
- **Correction** : soit soumettre l'exception à Lazar, au format de décision (mettre en regard des libellés mécaniques
  pour s'abstenir, jamais pour attribuer ; et, s'il le veut, les unités d'avant g001 comme une vraie paire « à blanc »
  sur les faits mécaniques) ; soit, d'ici là, une règle de préséance écrite d'avance qui ne met jamais en regard les deux
  courses (par exemple : la course M motive la correction de la ronde 1 ; la course S seulement si M ne motive rien ; les
  verdicts de S rapportés à part).

### CLB3-03 — à corriger avant usage — HC-P4-01 : une voie de lecture ajoutée après la lecture de faits de la course M, et plus faible que celle de la v2

- **Où** : registre l. 16–21, 267–275, 278–284, 568–569 ; spécification l. 135–143 ; LISEZMOI l. 89 (choix 10) et
  l. 134–138 (écart 1).
- **Ce qui ne va pas** : la v2 exigeait la ronde de la déclaration (sinon « non observable ») ; la v3 lit « 1 ou 2 rondes
  tournées → tenue » quand la déclaration manque, et la spécification dit qu'elle manquera vraisemblablement (elle est
  dans l'archive fermée, l. 140–143). Aucun constat ni fait nouveau ne demandait cette voie : CLB-02 demandait que (B)
  existe. L'auteur l'a écrite après avoir lu que la conception de M s'est close après une ronde (écart 1, déclaré) ; c'est
  elle qui tranchera M, vers « tenue », branche « correction candidate ». De plus, `rondes_tournees` (« unités c… avec au
  moins un appel ») ne dit pas pourquoi la conception s'est arrêtée : une ronde finie par un délai, un plafond ou une
  erreur compterait aussi. Le LISEZMOI demandait de vérifier que les changements de HC-P4-01, 07 et 08 ne tiennent qu'à
  la contre-lecture et aux faits nouveaux : c'est vrai pour 07 et 08, pas pour 01.
- **Correction** : marquer cette voie « écrite après la lecture de faits mécaniques de la course M » et ne pas l'appliquer
  à M (registre § 2, point 7) : pour M, la règle de la v2. Pour toute course, exiger en plus que chaque unité de
  conception porte `statut = ok`, sans `delai_depasse` ni refus `plafond`, et que g000 ait tourné ; sinon « non
  observable ».

### CLB3-04 — à corriger avant usage — Un seul des sept points pour Lazar est posé comme une décision

- **Où** : LISEZMOI l. 122–130 ; protocole l. 79, 168–170, 392–399, 491–503 ; registre l. 357–360.
- **Ce qui ne va pas** : voir le tableau du point 5. Seule la symétrie avant (b) a enjeu, options, recommandation et
  confiance. Famille du contre-lecteur, plafond, correction après M, question d'une relance, seuils : ni recommandation,
  ni avantages et inconvénients ; enjeu absent ou à peine dit. Le § 4 écrit « Aucun défaut » puis en donne un (l. 170).
- **Correction** : poser chacun au format de décision (décision en une phrase ; enjeu ; deux ou trois options, avantage et
  inconvénient ; recommandation et confiance ; défaut sous 48 heures, aucun pour une dépense). Dépenses, donc sans défaut :
  plafond, question servie par une relance, seuils (une ronde), famille « différente » si elle passe par session-depot.
  Correction après M : ce n'est pas une dépense ; écrire le défaut comme un défaut (le correcteur attend). Graines : citer
  la décision déjà posée.

### CLB3-05 — à corriger avant usage — Relevé (B) : aucun cas sain pour la course S, et aucune règle pour un champ d'identité « absent »

- **Où** : spécification l. 102, 191–197 ; briefs l. 114–116 ; protocole l. 286–294.
- **Ce qui ne va pas** : (a) le cas sain n'emploie que la série v13 (lanceur v10 ; v6.2.1 et v5.3) ; la course S tourne
  sous le lanceur v11, dont le `LANCEMENT.md` porte la question par course et la porte « course M précédente » (texte v5,
  l. 60) : forme jamais essayée. (b) `identite.question` (« m » ou « s ») vient du `LANCEMENT.md` ; celui du lanceur v10
  ne la porte peut-être pas (non vérifié) ; l'analyste s'arrête à « un écart » sans savoir si `absent` en est un : la
  lecture de M peut s'arrêter là.
- **Correction** : ajouter un cas sain de la série v14 (course S : `identite.question = s`, `unite.g001.question_servie =
  oui`, rien de la course M recopié) ; dire quels champs d'identité sont exigés (commit, arbre, nombre de fichiers, graine)
  et lesquels peuvent porter `absent`, rapportés sans arrêt. À faire aussi : remplir la ligne S du tableau d'identité
  (protocole l. 289) d'après le texte v5 à ses graines (graine 6967892196853497016 ; lanceur v11 `21854b79…`).

### CLB3-06 — mineur — Champs que le script v2 n'écrit pas, et deux libellés à aligner

- **Où** : registre l. 79–83, 134–137, 446–456, 510–512 ; protocole l. 498 ; briefs l. 124–127, 286–290 ; script v2
  l. 23–27, 73, 93–94.
- **Ce qui ne va pas** : (a) les libellés « sens du rejet » et « aucune tâche sans réponse » par cellule de `test_final`
  ne sont pas dans le script v2 : HC-P4-08 sur `test_final` et le sens de HC-P4-11 et 12 exigent des champs absents ; ils
  sont « non observables » (le registre le prévoit), mais protocole et LISEZMOI disent encore « à demander ». (b) Le fichier
  `test` porte aussi des « faits mécaniques » (script v2 l. 26), que le registre ne nomme pas. (c) Pour la délégation sur
  `test`, le script écrit « impossible par construction (référence égale à 1) » (l. 73) ; l'analyste attend « non
  distinct » ou « impossible » (briefs l. 124–125). (d) La phrase (iv) du script dit encore « deux objets » (l. 93–94).
- **Correction** : écrire l'état réel (non observable avec le script v2 ; demande d'une version 3 si conv-audit la garde) ;
  dire que les faits mécaniques se citent depuis (B) seul ; écrire le libellé exact de (ii) ; aligner (iv) au prochain
  passage du script.

### CLB3-07 — mineur — Deux traces de `test_final` avant la fin du compteur

- **Où** : protocole l. 85 ; script v2 l. 40–41, 144–146.
- **Ce qui ne va pas** : (a) le protocole fait encore écrire à session-depot « qu'il a lu ces scores en les exécutant » ;
  depuis N-050, il exécute sans afficher. (b) La ligne d'état du script porte « signalements : N » à la fin de chaque
  course ; si N compte aussi les signalements de la part `test_final`, elle en dit un peu avant la fin du compteur (non
  vérifié : script non lu).
- **Correction** : (a) « qu'il a exécuté le script, sans en afficher la sortie » ; (b) le demander à l'auteur du script,
  sinon ne compter que les signalements de `test`.

### CLB3-08 — mineur — Petites incohérences

- (a) Registre l. 164 renvoie au « § 2, point 8 » pour la pièce de correction : c'est le point 6.
- (b) Registre l. 196 et briefs l. 162 comptent HC-P4-05 et HC-P4-06 parmi les fiches qui motivent une correction ; leurs
  conséquences n'en motivent aucune (registre l. 384–386 et 411–413).
- (c) Les étapes 1 et 2 de la partie commune (briefs l. 50–54) nomment `MANIFESTE-DOSSIER-v1.txt` et
  `ouverture-lecture-<dossier>-v1.txt` ; le dossier de lecture finale porte `MANIFESTE-DOSSIER-FINAL-v1.txt` et
  `ouverture-lecture-finale-<dossier>-v1.txt` (protocole l. 130–131) : dire que la section 4 les remplace.
- (d) Briefs l. 194 : « `diff -ruN objet/ copie-organisme/` (depuis le dossier qui contient les deux) » : `objet/` est
  dans le dossier de lecture, `copie-organisme/` dans le dossier de sortie ; aucun dossier ne contient les deux. Écrire la
  commande exacte et le préfixe de chemin que G5 attend.

## Ce que j'ai trouvé conforme, en plus du point 1

- Seule HC-P4-10 nomme la v5.3, déclarée « indécidable par ce pilote » ; chaque fiche dit ce que la question S y change ;
  aucune ne lit la question ni la réponse.
- La spécification de (B) : champs, grammaire fermée, liste noire, sources, ce qu'elle ne porte jamais, essais (un cas
  sain, dix artefacts), relevé poussé sans affichage sous la retenue.
- Les gardes demandées par le brief v3 : journal des lancements avec attente chiffrée (G9), compteur et issue « plateau »,
  étalonnage à blanc avant tout droit d'éliminer (G10), plafond laissé à Lazar ; aucune dépense par défaut.

## Ce que je n'ai pas pu vérifier

- Le script v2 lui-même (non fourni) : le contenu exact de ses fichiers, ce que compte « signalements : N ».
- Les pièces que la v3 cite sans qu'elles me soient fournies : LISEZMOI du script v1, brouillon v5, note N-049 et N-050,
  fiche de lecture, synthèses « agents sur le noyau » et « littérature des boucles ».
- La structure réelle de l'extrait mécanique et des `LANCEMENT.md` des lanceurs v10 et v11 : quels champs de (B) porteront
  `absent`.
- Si une conception peut s'arrêter avant la ronde 3 sans déclaration (code non lu).
- La poussée des pièces sur le canal et son heure.

## Écarts déclarés

Je déclare n'avoir fait aucun écart à ma consigne.
