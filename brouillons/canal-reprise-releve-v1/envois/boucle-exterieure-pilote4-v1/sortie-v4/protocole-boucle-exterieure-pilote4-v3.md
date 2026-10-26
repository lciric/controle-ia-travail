# Protocole de la boucle extérieure du pilote 4 — v3

**Statut.** Version 3. Écrite le 26 octobre 2026 par l'auteur de la v2 (sous-agent de la lignée conv-audit), relancé par
conv-audit, sur le brief v4 (`LISEZMOI-brief-v4.md`, `dc5b823b…`) et trois messages de conv-audit reçus pendant
l'écriture (deux précisions à D5 ; une correction de D4). Écriture achevée le 2026-10-26 à 06:16:37 UTC (heure lue sur `date -u` dans la
commande qui écrit cette ligne). Elle remplace la v2 (`protocole-boucle-exterieure-pilote4-v2.md`, `0c71a74b…`), gardée
telle quelle (R12), après la vérification de la v3 des pièces (`rapport-verification-boucle-exterieure-v3.md`,
`1a7873e2…` : CLB3-01 à CLB3-08) et les décisions D1 à D7 de conv-audit. Écrite avant tout score : l'auteur n'a lu aucun
score ; les faits mécaniques de la course M qu'il a lus sont déclarés au registre v4 (§ Écrit avant tout score), et il
n'en a rien tiré. Pièce de travail d'un pilote de conception : ni préenregistrement ni scellement au sens de R1 ;
relecture gardée : vérifiée par le vérificateur de la v3 avant le premier usage. Elle ne modifie ni le texte v4 du pilote
(`782b858c…`), ni le texte v5 (`1943f39a…`, qui prime), ni leurs règles. Rien de cette pièce n'est servi à un organisme.
Les heures des mots de Lazar sont celles de Paris ; les autres sont en UTC.

**But.** Lazar, 26 octobre, 02:17 : « go » sur la boucle extérieure. À la fin de chaque course du pilote 4, des agents
neufs lisent la part `test` de la sortie du script de lecture et le relevé mécanique ; ils statuent fiche par fiche selon
le registre (`registre-hypotheses-conception-pilote4-v4.md`). À chaque ronde de la boucle, un correcteur propose au plus
une correction de l'objet, un facteur, selon la règle de préséance (§ 4). À la fin du compteur de rondes, `test_final` est
lu une seule fois. Les points à trancher par Lazar sont posés au format de décision dans
`points-boucle-exterieure-pilote4-pour-lazar-v1.md` (`ac105262…`), que ce protocole cite sans les reposer (§ 16). Toute
relance est une course nouvelle, sur le mot direct de Lazar dans la session de session-depot (dépense). La boucle
intérieure (R-471) n'est pas dans ce protocole.

## 0. Mots employés

- **Objet** : la v6.2.1 (commit `7ea3270`, arbre `4f13647a…`, 26 fichiers). Un seul objet dans ce pilote.
- **Course** : un objet qui tourne sous le noyau, en un ou plusieurs segments, du lancement à la fermeture. Ce pilote en a
  deux : la **course M** (`pilote4-gemini-v6-2-v1`, question M, dossier réel `pilote4-gemini-v6-2-v1-tentative2`) et la
  **course S** (`pilote4-gemini-v6-2-s-v1`, question S, dossier réel `pilote4-gemini-v6-2-s-v1`, sans suffixe de
  tentative, R-497). Identité complète : § 9.
- **Nom de course** (`<course>`) : le nom que le texte du pilote donne à la course. **Nom de dossier** (`<dossier>`) : le
  nom exact du dossier que session-depot a poussé pour la course qui a tourné (il peut porter un suffixe `-tentativeK`
  après un refus avant le manifeste, P4v3 l. 357–358). Les fichiers de lecture sont nommés par `<dossier>`.
- **Ronde de la boucle** (k = 1, 2 ou 3), pour l'objet : des courses, leurs lectures et au plus une correction. **La
  ronde 1 est le pilote 4** : la course M, puis la course S (M seule si S ne part pas) ; sa correction suit la **règle de
  préséance** (§ 4). Les rondes 2 et 3 sont des relances de l'objet corrigé, une course chacune. À ne pas confondre avec
  une **ronde de conception**, interne à une course.
- **Compteur** : le nombre de rondes, fixé d'avance à trois (§ 7). **Plafond** : la dépense totale des relances, fixée par
  Lazar (§ 7). **Plateau** : l'issue écrite d'avance pour une boucle qui s'arrête sans correction motivée (§ 7).
- **Dossier de course** : ce que session-depot pousse à la fin d'une course (liste fermée, `EMPREINTES-pilote-v1.txt`,
  archive `ferme.tar.gz`, extrait mécanique, journaux, `LANCEMENT.md`, manifeste…). Aucun agent ne l'ouvre.
- **Dossier de lecture** : le dossier que conv-audit assemble pour les agents d'une course, à partir de pièces nommées
  (§ 3). **Dossier de lecture finale** : le même, pour la lecture de `test_final` à la fin du compteur (§ 3 et § 13).
- **(A-test)**, **(A-final)**, **(B)**, **(C)** : la part `test` de la sortie du script de lecture ; sa part `test_final` ;
  le relevé mécanique ; le code de l'objet à son commit (registre, § 0.1).
- **Facteur** : un seul levier de conception de l'organisme, nommé par la **carte des facteurs** (§ 6).
- **Zones interdites** : les parties du code de l'objet que le correcteur ne touche pas (§ 14).
- **Journal des essais** : le journal de la boucle, tenu par conv-audit (§ 5). Il n'est pas dans le dossier de lecture.
- **Liste d'audit** : la liste, tenue par conv-audit, des dossiers d'audit et de leurs verdicts attendus (§ 12).

## 1. Quand la boucle démarre (conditions cumulées)

1. **La course est finie.** Sa liste fermée est poussée avec son fichier d'empreintes, et la recherche des clés est faite.
   Jamais pendant une course. Jamais entre deux segments : une course arrêtée par `STOP`, qui attend son segment K+1,
   n'est pas finie (garde G1).
2. **Le relevé (B) existe** pour cette course, produit par le script de `specification-releve-mecanique-B-v2.md`,
   empreinté, ses essais R5 consignés au journal. **Sans lui, rien n'est lu** (CLB-02). Ce script refuse d'écrire un
   relevé à identité incomplète (spécification v2, § 4.2 ; D5) : sans relevé, la course n'est pas lue.
3. **La lecture est ouverte.** Tant que Lazar n'a pas tranché la question des graines de plus (posée à 02:05 ; tour du
   collisionneur R-491 entre les deux courses), ou dit de lire, personne ne lit un score du pilote 4. Session-depot pousse
   la sortie du script et le relevé sans les afficher. La boucle ne démarre que lorsque conv-audit transmet la décision de
   Lazar qui ouvre la lecture, écrite dans le dossier de lecture : `ouverture-lecture-<dossier>-v1.txt`, qui cite une
   **référence vérifiable** (ligne du registre des décisions ou message du canal, avec son empreinte), contrôlée par
   conv-audit avant l'assemblage (garde G2 ; CLB-08 d) ; heure lue sur `date -u` dans la commande qui l'écrit.
4. **Rien de la boucle ne se lit sous la retenue, fiches mécaniques comprises.** Plusieurs faits mécaniques portent un
   bit sur les scores de `test` (registre, § 0.8). Ce que session-depot lit pendant et entre les segments, et ses portes de
   santé (porte « course M précédente », déclencheurs mécaniques du critère 1), restent tels que les textes v4 et v5 les
   règlent : ce n'est pas la boucle.
5. **Ce qui s'ouvre à la fin d'une course** : (A-test) et (B) de cette course (N-050). **Jamais (A-final)** avant la fin
   du compteur (§ 13).
6. **Si la décision ouvre la lecture par un texte nouveau** (par exemple des graines de plus, ces deux courses comptant
   comme premières graines), ce texte est poussé avant toute lecture de leurs scores. S'il change la règle de lecture, le
   registre et les briefs reçoivent une version nouvelle avant la première lecture.
7. **Les gardes (§ 11) et l'audit (§ 12) ont été essayés** sur un cas sain et sur un artefact (R5) avant la première
   lecture ; **l'étalonnage à blanc des agents (§ 12.5) est passé** avant qu'un verdict d'élimination soit transmissible.
   Leurs issues sont consignées au journal des essais.
8. **Les pièces de la boucle ont été contre-lues** (relecture gardée) et poussées avec leurs empreintes. Le texte v4 les
   voulait poussées avant la fin de la première course (§ Décisions, 02:17) : la v2 des pièces a été committée avant la
   fin de la course M, la v3 après elle, avant toute lecture (brief v4, § 4, point 1). Cette v3 du protocole est poussée
   avant l'ouverture de la lecture ; son auteur n'a lu aucun score.
9. **Le paramètre « famille du contre-lecteur » est fixé** (§ 12.3) : par Lazar, ou par son défaut (a), même famille,
   48 heures après l'envoi du point (pièce des points pour Lazar, point 1 ; envoyé le 26 octobre vers 05:42 UTC, heure
   exacte au journal de conv-audit). D'ici sa réponse ou l'échéance, l'analyste et le correcteur peuvent travailler, mais
   aucune proposition ne sort d'une ronde.
10. **Le plafond des relances** (pièce des points, point 3) est posé à Lazar au premier devis de relance ; aucun défaut
    (dépense) ; sans plafond, chaque relance reste une dépense sur son mot, et le compteur borne le nombre.

## 2. Qui lit quoi

| qui | lit | ne lit jamais |
|---|---|---|
| session-depot | exécute le script de lecture v3 à la fin de chaque course, dans son conteneur (il lit le secret, sans jamais l'afficher) ; pousse ses fichiers (§ 3), avec leurs empreintes, sans les afficher ; la ligne d'état du script v3 ne compte que les signalements de `test` (« signalements de test : N » ; CLB3-07 b) ; exécute l'essai « séparation » du script sans en afficher la sortie (G8 bis) ; exécute le relevé (B) sur les courses réelles, sans l'afficher (brief v4, § 4, point 3) ; écrit en réserve dans ses textes qu'il a exécuté le script, sans en afficher la sortie (texte v4, point 4 bis ; R-473 ; D6) | ce que ses propres règles lui interdisent |
| conv-audit | transmet l'ouverture ; assemble le dossier de lecture en copiant des fichiers nommés et en vérifiant leurs empreintes, sans ouvrir aucun fichier `test_final` ; contrôle à l'assemblage le seul fichier `test` réel (G8 bis) et les noms des fichiers de lecture (G12) ; lance les agents ; tient le journal et la liste d'audit ; fait écrire la carte des facteurs et les zones interdites par un sous-agent neuf, depuis le code de la v6.2.1 ; transmet les propositions à Lazar ; après l'ouverture, peut lire (A-test) et (B) (texte v4, point 3) ; (A-final) à la fin du compteur seulement | le secret, l'archive fermée, les textes de tâches, les réponses aux questions |
| analyste (fin de course) | le dossier de lecture d'une course : manifeste, ouverture, (A-test), (B), registre, protocole | la liste interdite ; `objet/` ; tout ce qui vient de l'autre course |
| correcteur (ronde 1 : de M, puis de S seulement si aucune fiche de M ne motive ; § 4) | la seule pièce de verdicts de la course dont il est le correcteur, par son chemin et son empreinte ; la liste des fiches en désaccord de cette course ; registre ; protocole ; `mecanique/` de cette course ; (C), en copie de lecture ; carte des facteurs ; zones interdites ; pour le correcteur de S, la référence (nom et empreinte) de la pièce de correction de M, sans la lire | la liste interdite ; `lecture/` (CLB-12) ; toute pièce de l'autre course |
| contre-lecteur, partie A (fin de course) | le dossier de lecture seul, comme l'analyste | les pièces de l'analyste et du correcteur : leurs chemins ne lui sont donnés qu'après que conv-audit a reçu sa partie A et consigné son empreinte (CLB-13) |
| contre-lecteur, partie B (une par course) | sa partie A de la course ; la pièce de verdicts de la course ; s'il y en a, la pièce de correction de la course (et, pour une correction, la pièce de périmètre et le diff) ; (C) ; carte des facteurs ; zones interdites | la liste interdite ; `lecture/` ; toute pièce de l'autre course |
| analyste de la lecture finale (fin du compteur) | le dossier de lecture finale d'une course : manifeste, ouverture finale, (A-final) de cette course, (B), registre, protocole | la liste interdite ; (A-final) de l'autre course ; les pièces de verdicts de fin de course (il n'en a pas besoin) |
| agent d'audit | un dossier d'audit (§ 12), aux mêmes noms qu'un dossier réel | la liste interdite |
| Lazar | ce qu'il décide de lire | — |

**Liste interdite, pour tous les agents.** Les fichiers de banque (`banque-confrontation-v*.json`, `*-cle.json`,
`*-secret.json`). L'archive fermée `ferme.tar.gz` et tout ce qui en est tiré hors (A) et (B) (mémoire, réponses par
tâche, code des successeurs, fichiers écrits par l'organisme pendant la course). Les journaux d'appels bruts
(`journal-appels*.jsonl`), l'extrait mécanique brut (`extrait-mecanique*.json`), `LANCEMENT.md` et le manifeste de la
course : on n'en lit que le relevé (B). Les questions M et S et les réponses de l'organisme (`reponse-question*`).
`P3-consignes-v1.md`, `textes-actions-…`. Les dossiers `donnees/`, `runs/`, `diag/`, `pilotes/`. Les réponses du
collisionneur. Toute clé ou tout jeton. Tout score d'un autre pilote. Le journal des essais. Pendant la lecture d'une
course : la sortie, le relevé et les pièces de l'autre course. (A-final) avant la fin du compteur. Un fichier de lecture
dont le nom porte `-provisoire-`, ou d'une version du script inférieure à 3 (G12). Un dossier de tentative refusée (§ 9).

## 3. Le dossier de lecture et le dossier de lecture finale

Conv-audit les assemble. Chemins relatifs à `<dossier-de-lecture>/`. `<dossier>` est le nom exact du dossier de course
(§ 0 et § 9 : `pilote4-gemini-v6-2-v1-tentative2` pour M, `pilote4-gemini-v6-2-s-v1` pour S) ; les sorties du script et
du relevé gardent les noms que leurs auteurs leur donnent, **jamais renommées** (leurs compagnons portent le nom nu). Les
noms de fichiers ci-dessous suivent cette règle : ceux du script de lecture v3 sont ceux qu'il écrit (brief v4, D1) ; les
autres sont fixés ici. Ni la v1 ni la v2 du script ne s'exécutent sur les courses (message n° 79 de conv-audit à
session-depot).

**Dossier de lecture d'une course (fin de course)** :
- `MANIFESTE-DOSSIER-v1.txt` : chaque fichier du dossier avec son empreinte, au format « empreinte, deux espaces,
  nom ». Sa première ligne est une ligne de commentaire, que `sha256sum -c` ignore (essayé sur GNU coreutils 9.4, mode
  strict compris) : `# script de lecture : lire_pilote4_v<n>.py, sha256 <empreinte du script>, version <n>`. `<n>` (au
  moins 3) est la version du script (D1). Chaque agent vérifie le manifeste par `sha256sum -c` avant de lire, vérifie que
  son empreinte est celle que son brief lui donne (`<empreinte-manifeste>` ; CLB-16 f), et que la version des fichiers de
  lecture est celle de cette ligne.
- `ouverture-lecture-<dossier>-v1.txt` : la décision qui ouvre la lecture (§ 1.3), avec sa référence vérifiable.
- `lecture/` : (A-test) de cette course seulement : `lecture-<dossier>-test-v<n>.json` et `.md`, écrits par le script v3 à
  la fin de la course, avec leurs `.sha256`. Ni le mot `test_final`, ni test (iii), ni valeur p, ni mention d'essai
  (garde G8 bis, § 11) ; aucun fichier dont le nom porte `-provisoire-`, aucune version inférieure à 3 (garde G12).
- `mecanique/releve-mecanique-<dossier>-v1.txt`, avec son `.sha256` : le relevé (B) (spécification).
- `registre/`, `protocole/` : la version en vigueur du registre et de ce protocole, chacun avec son `.sha256`.
- `objet/` : copie de lecture du dossier `organisme/` au commit de l'objet, pour le correcteur et la partie B seulement ;
  `objet-EMPREINTE-ARBRE.txt` **à côté de `objet/`, pas dedans** (CLB-16 b) : l'empreinte d'arbre recalculée par
  conv-audit sur `objet/`, égale à celle qui est attendue (`4f13647a…`).
- `carte-facteurs-v<n>.md` et `zones-interdites-v<n>.md`, avec leurs `.sha256` (§ 6 et § 14), pour le correcteur et la
  partie B.
- **Pas de journal** (CLB-05 a, CLB-08 a) ; aucun fichier de l'autre course.

**Dossier de lecture finale d'une course (fin du compteur)** : `MANIFESTE-DOSSIER-FINAL-v1.txt` (même forme, même ligne
de version) ; `ouverture-lecture-finale-<dossier>-v1.txt` (la décision qui ouvre `test_final`, avec sa référence) ;
`lecture-finale/lecture-<dossier>-test-final-holm-quatre-v<n>.json` et `.md`, écrits par le script v3 à la fin de la
course S pour chacune des deux courses — ou, pour M si la course S ne court pas ou ne finit pas saine,
`lecture-<dossier de M>-test-final-holm-deux-v<n>` (option `--sans-seconde-course`) — : cette course seulement, aucune
valeur de l'autre course (ni compte, ni proportion, ni valeur p, ni libellé) ; jamais un fichier dont le nom porte
`-provisoire-` (G12) ; `mecanique/` ; `registre/` ; `protocole/`. Un dossier par course, un agent par dossier. Pour une
course de relance : le nom et la règle de sa sortie `test_final` sont fixés par son texte (§ 10).

## 4. Les rôles, et leur ordre

À chaque course et à chaque ronde, chaque rôle est tenu par un sous-agent neuf, lancé par conv-audit. Il n'a écrit aucune
des pièces qu'il lit et n'a lu aucun score de ce pilote avant sa tâche. Les briefs sont dans
`brief-agents-fin-de-course-v3.md`, à donner tels quels.

**Règle de préséance**, écrite avant toute lecture (brief v4, D2 ; elle remplace les choix 1, 3 et 4 de la v3 des
pièces) : « **la course M motive la correction de la ronde 1 ; la course S ne la motive que si aucune fiche de M n'en
motive ; les verdicts de S sont rapportés à part, jamais mis en regard de ceux de M.** » La correction se propose après la
lecture de M ; le correcteur n'attend la course S que si M ne motive rien. « Aucune fiche de M ne motive de correction »
est un fait sur M seule (registre, § 0.7) : dans la pièce de verdicts de M, aucune fiche hors désaccord ne porte une
branche qui propose une correction. La règle tient avant la génération 1, où M et S ne diffèrent que par la graine (la
question n'est servie qu'à g001), comme après, où la question diffère aussi. Aucune pièce (verdicts, parties A et B,
correction, journal) ne met côte à côte les verdicts des deux courses.

**À la fin de chaque course** (M, puis S) :
1. **Analyste.** Il vérifie l'ouverture, la fin de la course et l'identité de l'objet et de la course. Il donne un verdict
   par fiche de fin de course (registre, § 2, étape 2), avec le champ qui le fonde. Il liste les faits suspects (R4) et la
   liste d'instrumentation. Il rend `verdicts-<dossier>-v1.md`.
2. **Contre-lecteur, partie A**, à l'aveugle : il applique le registre au même dossier et rend
   `contre-lecture-<dossier>-partie-A-v1.md` ; conv-audit consigne son empreinte avant de lui donner quoi que ce soit
   d'autre. Conv-audit relève ensuite, sur ces deux pièces de la même course, les fiches dont les verdicts diffèrent
   (désaccords), sans rien en conclure.

**Correction de la ronde 1** (règle de préséance) :
3. **Correcteur de M**, après les étapes 1 et 2 sur M. Il lit la seule pièce de verdicts de M et la liste de ses
   désaccords. Il propose au plus une correction (un facteur), ou une demande d'instrumentation, ou l'arrêt, ou une
   question pour Lazar ; ou il écrit le fait « aucune fiche de la course M ne motive de correction ». Pour une
   correction : d'abord la **pièce de périmètre** (facteur, fichiers, fonctions, plages de lignes au commit), rendue et
   empreintée **avant** d'écrire le diff (CLB-06 b) ; puis le diff (`diff -ruN`, commande exacte au brief du correcteur ;
   § 6) ; les essais ; l'observation mécanique attendue à la course suivante, **avec son nombre** (§ 5) ; ce qu'elle ne
   dit pas. Il rend `correction-<dossier>-ronde-1-v1.md` et, pour une correction, `perimetre-<dossier>-ronde-1-v1.md` et
   `correction-<dossier>-ronde-1-v1.diff`.
4. **Correcteur de S**, seulement si la pièce du correcteur de M établit qu'aucune fiche de M ne motive de correction, et
   que la partie B de M l'a vérifié (étape 5) : un sous-agent neuf, après les étapes 1 et 2 sur S. Il lit la seule pièce
   de verdicts de S et la liste de ses désaccords ; il reçoit de conv-audit le fait sur M par la référence de la pièce de
   correction de M (nom et empreinte), sans la lire. Mêmes règles et mêmes rendus, au nom du dossier de S. Si M motive une
   correction, aucune correction n'est proposée sur S dans la ronde 1 : les verdicts de S sont rapportés à part.
   Aux rondes 2 et 3 (une course) : un correcteur, sur la pièce de verdicts de la course, après sa lecture.
5. **Contre-lecteur, partie B, une par course** (l'agent qui « casse exprès » ; sa famille est un paramètre, § 12.3). Il
   compare sa partie A à la pièce de verdicts de la même course, vérifie les champs cités et les interdits. S'il y a une
   pièce de correction de cette course, il l'attaque (un facteur, périmètre, zones interdites, contenu interdit,
   motivation, essais) ; si elle dit qu'aucune fiche de la course ne motive de correction, il le vérifie sur la pièce de
   verdicts. Il conclut « transmissible à Lazar », « transmissible après corrections » ou « non transmissible ». Il rend
   `contre-lecture-<dossier>-ronde-<k>-v1.md`. Aucune partie B ne cite l'autre course.
6. **Désaccords.** Une fiche sur laquelle l'analyste et le contre-lecteur diffèrent ne motive aucune correction dans la
   ronde. Le désaccord est consigné au journal, dans l'entrée de sa course, et soumis à conv-audit.
7. **Ensuite.** Conv-audit écrit les entrées du journal (une par course ; une par correction). Il ne transmet à Lazar
   qu'une correction « transmissible ». La proposition part avec son devis, l'observation mécanique attendue chiffrée, le
   nombre de tests (iii) que la boucle aura accumulés (§ 7), et les mots exacts que Lazar écrirait dans la session de
   session-depot. Une correction motivée par M n'attend pas la lecture de S.

**À la fin du compteur** (§ 13) : un **analyste de la lecture finale** par course, puis un contre-lecteur à l'aveugle par
course (partie A seulement), puis une entrée finale du journal par conv-audit.

## 5. Journal des essais, journal des lancements et des lectures

- Un journal pour la boucle, versionné (R12) : `journal-essais-boucle-pilote4-v<N>.md`. Chaque version reprend la
  précédente mot pour mot, ajoute ses entrées et cite l'empreinte de la précédente. Conv-audit l'écrit et le pousse sur le
  canal. **Il n'est donné à aucun agent.**
- **Tout essai est consigné, échecs compris** : gardes, audits, étalonnage à blanc, lectures refusées, pièces d'agents
  refusées, corrections refusées, essais en échec, hypothèses éliminées, relances refusées par Lazar.
- Aucune valeur numérique de `test_final` n'y est écrite : une cellule se cite par ses coordonnées et son libellé.
- **Entrée de lancement, avant chaque relance** (fait nouveau 4 ; synthèse « agents sur le noyau », § 3) : identité de
  l'objet corrigé (commit, arbre, nombre de fichiers), noyau, banque, texte de la relance et son empreinte, graine, devis,
  question servie, et **l'attente chiffrée** : la ou les fiches visées par la correction et l'observation mécanique
  attendue avec son nombre (par exemple « HC-P4-03 : au moins un successeur valide ayant tourné, nombre attendu ≥ 1 » ;
  « HC-P4-01 : `conception.declaration.ronde` ≥ 3 »). Pour `test_final` : « aucune attente au-delà des nulles HC-P4-11 et
  12 ». **Une entrée de lancement sans nombre fait refuser la relance** (garde G9).
- **Compteur des lectures** : chaque entrée dit qui a lu quoi (A-test, B, A-final, par course), quand, et le nombre
  cumulé de lectures humaines et d'agents de chaque part ; `test_final` : une lecture, à la fin.
- **Une entrée par course, une entrée par correction** (règle de préséance, § 4). Une entrée ne cite les verdicts que
  d'une course et ne renvoie pas ligne à ligne à une entrée de l'autre course. L'entrée d'une correction motivée par S
  porte la seule ligne « condition de préséance » : la référence de la pièce de correction de M qui établit qu'aucune
  fiche de M ne motive, sans aucune fiche ni aucun verdict de M.
- Format d'une entrée de fin de course ou de correction :

```
### Entrée <numéro> — <dossier>, ronde <k> — <date et heure lues sur date -u>
- objet : arbre <…>, <n> fichiers ; graine <…> ; question <m|s>
- lecture : ouverte par <référence vérifiable> ; course finie (liste fermée <empreinte>) ; relevé (B) <empreinte>
- pièces lues : <noms et empreintes>
- fiches testées : <liste>
- verdicts (cette course seulement) : <fiche : verdict de l'analyste / verdict de la partie A ; champ cité>
- désaccords : <liste, ou « aucun »>
- correction proposée : <facteur ; empreinte du périmètre ; empreinte du diff ; attente chiffrée>, ou « aucune fiche de cette course ne motive de correction », ou « aucune : la course M motive la correction de la ronde 1 » (S)
- condition de préséance (correction motivée par S seulement) : <nom et empreinte de la pièce de correction de M>
- ce qui a échoué : <liste, ou « rien »>
- audit des agents : <dossiers d'audit donnés ; accords et désaccords avec la liste d'audit> ; étalonnage à blanc : <passé le … / non passé>
- paramètres : famille du contre-lecteur = <valeur fixée par Lazar, ou défaut (a) à l'échéance> ; plafond = <valeur ou « non fixé »> ; compteur = <k sur 3>
- tests (iii) accumulés par la boucle : <4 pour le pilote 4, + 2 par relance>
- lectures : <qui a lu quoi, quand ; cumul>
- décision de Lazar : <relance, arrêt, autre ; référence>, ou « en attente »
- dépense : <ligne de dépense>, ou « aucune »
- écarts déclarés : <liste, ou « aucun »>
```

## 6. Un facteur à la fois

- Entre deux rondes de l'objet, un seul facteur change. Un facteur est une entrée de la **carte des facteurs**
  (`carte-facteurs-v<n>.md`), écrite d'avance pour conv-audit par un sous-agent neuf, depuis le code de la v6.2.1 et la
  liste ci-dessous, qui donne pour chaque facteur : fichiers, fonctions, plages de lignes au commit ; et dit quels
  paramètres comptent ensemble pour un facteur, avec la raison. Liste de départ, tirée du registre : nombre minimal de
  rondes avant la déclaration de fin ; nombre de tâches d'entraînement du score interne ; les deux seuils du critère de fin
  (0,78 et 0,65 : proposés comme un seul facteur, une seule règle de déclaration ; la carte tranche, un facteur ou deux ;
  conv-audit ne confirme rien d'avance ; CLB-06 c) ; un élément du contrat de l'architecte ; la mutation en génération
  notée ; le retour arrière ; une borne interne par tâche ; le chemin de formulation de la moisson ; un défaut de code
  nommé. Les seuils 0,01 (stagnation) et 0,03 (retour arrière) sont des points de conception a priori (registre, § 0.5 ;
  pièce des points pour Lazar, point 7 : défaut, garder) : tout changement attend le mot de Lazar, hors d'une correction de
  la boucle motivée par un verdict, et compte pour une ronde.
- La graine change à chaque course (texte nouveau, entropie nouvelle, R9). Ce n'est pas un facteur : c'est du bruit. La
  dérive des modèles appelés aussi. La question servie (M ou S) est fixée par le texte de la relance ; elle n'est pas un
  facteur de conception et n'est jamais comparée.
- **Comment on le garantit** :
  1. Le correcteur rend la **pièce de périmètre** (facteur de la carte ; fichiers, fonctions, plages de lignes), et
     conv-audit en consigne l'empreinte, **avant** que le diff soit écrit (CLB-06 b).
  2. Le diff (`diff -ruN`, unifié, fichiers nouveaux compris) se calcule dans le dossier de sortie du correcteur, entre
     `objet-origine/` (copie fidèle de `objet/`, vérifiée identique par `diff -r`) et `copie-organisme/` (la copie
     modifiée) ; la commande exacte, chemins complets par variables nommées, est au brief du correcteur (section 2) ; les
     en-têtes de fichiers du diff portent les préfixes `objet-origine/` (ancien) et `copie-organisme/` (nouveau), les
     seuls que G5 accepte (D7 ; CLB3-08 d). Le diff ne touche que ce
     périmètre, plus une liste close de fichiers d'accompagnement : `manifeste.json` (champs de version et de description
     seulement) ; un `CORRECTIONS-v<N>.md` nouveau, qui **ne décrit que le changement de code (quoi, où)**, sans fait de
     course, sans fiche, sans verdict, sans score (CLB-11) ; un `tests/test_corrections_v<N>.py` nouveau ; un essai hérité
     adapté, seulement si la correction l'exige, déclaré avec sa raison.
  3. Un script de contrôle (garde G5) compare chaque bloc du diff, fichiers nouveaux compris, à la carte des facteurs et
     à la pièce de périmètre ; refuse tout bloc hors du périmètre, tout périmètre qui couvre deux facteurs de la carte,
     tout bloc dans une zone interdite (§ 14), et tout contenu interdit détectable par motifs (§ 14).
  4. Le contre-lecteur lit le diff entier et confirme qu'il n'y a qu'un facteur et aucun contenu interdit.
  5. Conv-audit commite la correction (les agents n'ont pas `git`), recalcule l'arbre et vérifie que l'écart entre le
     commit précédent et le nouveau est le diff transmis, fichiers nouveaux compris. Le lanceur dérivé épingle ce commit
     (§ 9).

## 7. Règle d'arrêt, compteur, plafond, plateau

La boucle s'arrête pour l'objet à la première de ces conditions :
1. **Compteur : trois rondes** (k = 3 : le pilote 4 et au plus deux relances), avant la confirmation sur la banque v6.
2. **Plus aucune fiche ne motive de correction** (à la ronde 1 : ni dans M, ni ensuite dans S, selon la règle de
   préséance) : chaque fiche est éliminée, ou indécidable (par ce pilote, dans le bruit, ou non observable), ou tenue sans
   correction attachée, ou en désaccord. C'est l'issue **« plateau »**, écrite d'avance comme une réponse de la boucle, pas
   comme un échec à corriger par une ronde de plus.
3. **Plafond** : la dépense totale des relances dépasse le plafond fixé par Lazar (pièce des points pour Lazar, point 3 ;
   aucun défaut, dépense ; posé au premier devis de relance), ou le plafond d'un GO.
4. **Une ligne de la liste d'arrêt** du texte en vigueur (texte v4, v5, ou texte de la relance) : défaut, course hors de
   la liste close, fait suspect (R4).
5. **Le mot de Lazar.**

Une demande d'instrumentation n'est pas une relance : elle change le relevé ou le script (versions nouvelles), pas
l'organisme. **Multiplicité d'une ronde à l'autre** (CLB-19) : chaque relance a sa propre famille de deux tests (iii),
corrigée par Holm dans son texte ; sur trois rondes, jusqu'à huit tests (iii) s'enchaînent par les décisions de la boucle,
sans contrôle d'ensemble. Ce fait est écrit dans chaque texte de relance, dans chaque transmission à Lazar et dans
l'entrée finale du journal. À la fin du compteur, la lecture de `test_final` (§ 13) décrit ; elle ne relance pas.

## 8. Exploration et confirmation

- Tout ce que la boucle conclut sur la banque v3 est exploratoire et non opposable (R7). Les pièces de verdicts sont à
  part, exploratoires, poussées sur le canal, hors du rapport de lecture et hors des critères gelés. Elles restent tenues
  par l'interdit de comparer les deux courses, verdicts compris (texte v4, point 3 ; texte v5, table ; P4C7-02 ; règle de
  préséance, § 4).
- Ce qui part en confirmation se scelle avant toute lecture d'un score de la banque v6 (Lazar, 01:56). Ses auteurs
  déclarent avoir lu les scores de conception (R-473). Banque v6 (lot 3) ; jamais la v3, ni la v5.
- **Symétrie avant le pilote décisif (b)** (CLB-10) : la v5.3 ne court pas dans ce pilote et ne reçoit aucune ronde de
  boucle ; la v6.2.1 en reçoit jusqu'à trois. (b) compare les deux objets. Le point est posé au format de décision dans la
  pièce des points pour Lazar (point 4 : (a) les deux objets tels que livrés, `7ea3270` et `4ecba58` ; (b) la v6.2.1
  corrigée contre la v5.3 livrée, l'inégalité d'effort déclarée par le texte de (b) avant son scellement ; (c) autant de
  rondes pour la v5.3, une dépense). Recommandation (a), confiance moyenne ; **défaut (a)**, 48 heures après son envoi à
  Lazar ; nécessaire avant l'écriture du texte de (b) (D4).
- Rien de la boucle n'est servi à un organisme ni à Gemini : ni le registre, ni les verdicts, ni les motifs des
  corrections. L'organisme de la ronde suivante ne reçoit que son code ; le `CORRECTIONS-v<N>.md` de son arbre ne décrit
  que le changement de code (§ 6 ; garde G4 : aucun fait de course, aucun nom de fiche, aucun score, aucun libellé).

## 9. Contrôle d'identité des courses et des dossiers

Avant tout verdict, l'analyste compare l'identité portée par le relevé (B) aux valeurs attendues (brief v4, D5) :

| champ du relevé (spécification v2, § 4.2) | course M | course S |
|---|---|---|
| `releve.course` (nom de la course) — exigé | `pilote4-gemini-v6-2-v1` | `pilote4-gemini-v6-2-s-v1` |
| `releve.dossier` (dossier réel) | `pilote4-gemini-v6-2-v1-tentative2` | `pilote4-gemini-v6-2-s-v1` (copie de lancement : `essaim-m3-refonte-v1/pilotes/pilote4-gemini-v6-2-s-v1`, sans suffixe de tentative, R-497) |
| `identite.lignee` — exigé | `gemini-organisme-v6-2` | `gemini-organisme-v6-2-s` |
| `identite.graine` — exigé | 2334107546136117589 | 6967892196853497016 |
| `identite.arbre`, `identite.nb_fichiers` (organisme) — exigés | `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, 26 | les mêmes |
| organisme, pour mémoire (non porté par le relevé : le lanceur l'épingle par son commit, son arbre et son nombre de fichiers) | v6.2.1, commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e` | le même |
| `identite.question_empreinte` — exigé ; `identite.question` | `8b1c751174b3d24dc0d861873a2758d3b780ab9a878e83e591835849db1a7acd` ; `m` | `a54da93ee892d920c31ba47327c2400e25ccf42ff06faa46d94bfc471a5a6289` (commit `4772b525081342a6a30ba8823733aa5770a888a8`) ; `s` |
| `identite.lanceur`, `identite.lanceur_empreinte` — exigés | `lancer_pilote4_gemini_v10.sh`, `0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952` | `lancer_pilote4_gemini_v11.sh`, `21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7` |
| `identite.commit` (commit du segment 1 : tête du dépôt de la copie de lancement) — exigé | la tête citée au message de départ de la course M | la tête citée au message de départ de la course S |
| `identite.porte_m_precedente` — facultatif | `absent` (par construction) | `oui` |
| `identite.texte_empreinte` — facultatif | texte v4, `782b858c537222245fd757c23ea6d75abae142df029eed3e53af36d8c78cfa95` | texte v5, `1943f39ada61db7d21e53b7e0c02c6e826b86e1467687eedbe56617877ab7f87` |
| `identite.noyau`, `identite.banque_empreinte`, `identite.graine_manifeste` — facultatifs | `8e5e2f7b` ; `157a2b45…` ; 2334107546136117589 | `8e5e2f7b` ; `157a2b45…` ; 6967892196853497016 |

**Règles** (brief v4, D5 et sa précision 2). Les champs exigés sont présents par construction : si l'un manque, ou si
l'empreinte de la question n'est ni celle de M ni celle de S, le script du relevé refuse d'écrire ; l'analyste n'a donc
jamais à juger si `absent` est un écart. Chaque champ d'identité qui porte une valeur est comparé à sa valeur attendue ;
un champ facultatif `absent` est rapporté, sans arrêt. Le commit du segment 1 n'a pas de valeur dans ce tableau : sa
valeur attendue est la tête citée au message de départ de la course, que conv-audit compare au relevé avant l'assemblage
du dossier (aucun assemblage en cas d'écart). Tout écart : aucune lecture ; fait suspect (R4) ; conv-audit et Lazar
informés.

**Choix du dossier** (CLB-01) : le dossier de course se choisit par cette identité (arbre, nombre de fichiers, graine,
lanceur, question, commit du segment 1), jamais par son nom ; **un dossier de tentative refusée** (refus avant le manifeste) **n'est
jamais lu**, ni par le script, ni par le relevé, ni par un agent. Pour un objet relancé : le lanceur dérivé épingle le
commit, l'arbre et le nombre de fichiers, comme le lanceur v10 le fait (essais `organisme-v6-2`, `nombre-v6-2`,
`seg-organisme-modifie`) ; le même contrôle s'applique, aux valeurs du texte de la relance.

## 10. Relance

- Une relance est une course nouvelle. Jamais une course de plus sous les textes v4 ou v5. Jamais la reprise d'une course
  fermée.
- Il lui faut :
  1. un texte, version nouvelle (R12), de pilote de conception (relecture gardée), qui nomme l'objet corrigé (commit, arbre,
     nombre de fichiers), le facteur, l'empreinte du périmètre et du diff, **la question servie** (M ou S : pièce des
     points pour Lazar, point 6 ; aucun défaut, dépense ; posée au GO de la relance), sa graine (entropie tirée pour lui,
     R9), ses bornes, son devis, sa famille de deux tests (iii), le nom et la règle de sa sortie `test_final` et la version
     du script de lecture qui la lit, le nombre de tests accumulés par la boucle (§ 7), et **l'attente chiffrée** de
     l'entrée de lancement (§ 5) ;
  2. un lanceur dérivé du v11 par remplacements exacts, sa batterie et sa série d'essais (R5), qui épingle l'objet nouveau ;
  3. une ligne de GO (extension ou nouvelle) qui porte l'arbre de l'objet, et une ligne de dépense ;
  4. le mot direct de Lazar dans la session de session-depot (dépense ; aucun défaut) ;
  5. le lancement par session-depot, une fois la clé des courses libre (aucune course ni aucun tour en cours).
- Nom versionné : un nom jamais employé, qui porte l'objet, la ronde et la question. La forme du texte d'une relance et
  celle des noms sont fixées au premier devis de relance, dans un texte nouveau, avant toute lecture de son `test` ; ce
  protocole ne les fixe pas maintenant (brief v4, § 4, point 10).
- Des graines de plus pour un même objet, ou un autre objet, ne sont pas des relances de la boucle : ce sont des décisions
  de Lazar (question pendante depuis 02:05). La boucle rapporte seulement ce qui reste indécidable.
- Refusée : une relance « pour voir si les scores bougent » (R3) ; une relance sans attente chiffrée (G9) ; une relance
  avant l'étalonnage à blanc (G10).

## 11. Gardes à essayer avant la première lecture (R5 : un cas sain et un artefact chacune)

Chaque garde est un script ou un contrôle écrit, empreinté, essayé, consigné au journal des essais. Leur auteur : un
sous-agent de conv-audit, après la vérification de cette v3 du protocole (brief v4, § 4, point 7). Aucune ne lit un
score réel : elles emploient des pièces de simulation (séries v13 et v14) et des données synthétiques, comme les essais du
script de lecture. Elles peuvent donc tourner sous la retenue.

| garde | cas sain (accepté) | artefact (refusé ou détecté) |
|---|---|---|
| G1 — lecture pendant une course | course finie : liste fermée présente et vérifiée, recherche des clés consignée, `fin.reprise_attendue = non` au relevé | course simulée arrêtée par `STOP` entre deux segments (`fin.reprise_attendue = oui`), ou sans liste fermée : assemblage refusé |
| G2 — lecture sous la retenue | `ouverture-lecture-<dossier>-v1.txt` présent, qui cite une référence vérifiable, contrôlée par conv-audit avant l'assemblage | fichier absent, vide ou sans référence : assemblage refusé ; l'agent refuse de commencer ; référence qui ne correspond à aucune ligne ni aucun message : assemblage refusé par conv-audit |
| G3 — faux dossier de course à scores marqueurs | dossier synthétique dont les valeurs sont des marqueurs choisis par son auteur, gardés dans une liste empreintée que les agents ne voient pas ; toute la ronde tourne dessus, et ses pièces restent des pièces d'essai, jamais transmises à Lazar ; aucun marqueur d'une cellule de `test_final` n'apparaît dans une pièce de la boucle, dans ce qui serait servi à un organisme ou sur la sortie standard du script | une pièce de la boucle, ou l'arbre d'un organisme, qui porte un marqueur : détecté |
| G4 — arbre de l'organisme corrigé | arbre inspecté : aucun nom interdit, aucun marqueur, aucune chaîne tirée de (A) ou de (B), `CORRECTIONS-v<N>.md` sans fait de course, sans nom de fiche (`HC-P4-`), sans libellé du point 4 bis, sans score : accepté | le même arbre avec un fichier `test_final` synthétique planté, ou un fichier qui porte un marqueur, ou la copie d'une pièce de lecture, ou un `CORRECTIONS-v<N>.md` qui cite une fiche ou un fait de course : refusé avant toute relance ; l'épinglage de l'arbre par le lanceur garantit que ce qui tourne est ce qui a été inspecté |
| G5 — périmètre, facteurs, zones | diff `-ruN` entre `objet-origine/` et `copie-organisme/` (§ 6), dans le périmètre déclaré (pièce empreintée avant le diff), un facteur de la carte, plus la liste d'accompagnement : accepté | (a) diff qui touche deux facteurs (par exemple le seuil de stagnation et le seuil du retour arrière) : refusé ; (b) périmètre déclaré qui couvre deux facteurs de la carte : refusé ; (c) bloc dans une zone interdite (§ 14) : refusé ; (d) fichier nouveau hors de la liste d'accompagnement : refusé ; (e) diff synthétique qui porte un contenu interdit de la liste du § 14 (choisi par l'auteur de l'essai, gardé hors des pièces de la boucle) : refusé par G5 (motifs) **et** par le contre-lecteur (lecture) ; l'essai du contre-lecteur se fait par un dossier d'audit qui porte cette correction (§ 12.1) ; (f) en-tête de fichier dont le chemin ne commence pas par `objet-origine/` (ancien) ou `copie-organisme/` (nouveau) : refusé (D7) |
| G6 — mise en regard des deux courses | pièce de verdicts, partie A, partie B, pièce de périmètre ou de correction qui ne porte que le nom (de course et de dossier) de sa course ; pièce de correction motivée par S dont la seule mention de M est la ligne « condition de préséance » (nom et empreinte de la pièce de correction de M, aucune fiche ni aucun verdict de M) | pièce qui porte le nom de l'autre course hors de cette ligne, une fiche ou un verdict de l'autre course, une différence M − S, ou une phrase qui met les deux courses en regard : refusée par le contre-lecteur et par un contrôle de motifs (noms de course et de dossier de l'autre course) ; ligne « condition de préséance » qui porte une fiche ou un verdict de M : refusée. Portée : pièces de verdicts, parties A et B, pièces de périmètre et de correction (CLB-16 e ; D2) ; le tableau d'identité du protocole n'y est pas soumis ; le journal, tenu par conv-audit, suit la même règle entrée par entrée (§ 5) |
| G7 — libellé (ii) « au-dessus » | sortie synthétique qui ne porte que « non distinct » : rien | sortie synthétique qui porte un « au-dessus », sur `test` ou sur `test_final` : l'analyste le rapporte comme signal de défaut (R4) |
| G8 — valeur de `test_final` recopiée | pièce qui cite les cellules de `test_final` par coordonnées et libellés | pièce qui porte une valeur marqueur d'une cellule de `test_final` (score, compte, valeur p, nombre sans réponse) : refusée |
| G8 bis — séparation des parts et des courses (réécrite : CLB3-01 c ; D1) | (a) **sur données synthétiques**, l'essai « séparation » du script v3, exécuté par session-depot sans en afficher la sortie : le fichier `test` ne porte ni le mot `test_final`, ni (iii), ni valeur p, ni valeur de `test_final` ; l'union des deux fichiers « holm-quatre » rend les lignes (iii) du calcul joint ; aucune valeur d'une course n'apparaît dans le fichier de l'autre ; (b) **à l'assemblage d'un dossier de course**, contrôle du seul fichier `test` réel : ni le mot `test_final`, ni (iii), ni valeur p, ni mention d'essai. Aucun fichier `test_final` réel n'est ouvert avant la fin du compteur | (a) une valeur de l'autre course plantée dans un fichier « holm-quatre » synthétique : refusée par l'essai ; une valeur de `test_final` ou une valeur p plantée dans un fichier `test` synthétique : refusée ; (b) un fichier `test` qui porte le mot `test_final`, une ligne (iii), une valeur p ou la mention d'essai : assemblage refusé |
| G9 — entrée de lancement sans attente chiffrée | entrée de lancement qui nomme la fiche visée, l'observation mécanique attendue et son nombre | entrée sans nombre, ou dont l'attente est un score : relance refusée |
| G10 — étalonnage à blanc des agents (§ 12.5) | un dossier d'audit nul (aucun changement planté) et une paire de dossiers d'audit « A contre A » (même course simulée, deux graines, deux jeux de coûts) : verdicts égaux à la liste d'audit, aucune comparaison, verdicts identiques sur la paire | un verdict d'élimination sur le dossier nul, ou un verdict qui diffère entre les deux dossiers de la paire sans qu'un fait planté le justifie, ou une phrase de comparaison : étalonnage non passé ; brief ou registre corrigés, étalonnage refait avec un agent neuf |
| G11 — relevé (B) | voir la spécification v2, § 6 : cas sains des séries v13 (lanceur v10) et v14 (course S simulée après une course M saine simulée, lanceur v11) | artefacts de la spécification v2, § 6, dont un champ d'identité exigé retiré et une empreinte de question autre : écriture refusée |
| G12 — sortie de lecture hors du script v3 (D1) | dossier dont les fichiers de lecture portent `-test-v<n>` (lecture finale : `-test-final-holm-quatre-v<n>` ou `-test-final-holm-deux-v<n>`), `<n>` au moins 3 et égal à la version écrite à la ligne de commentaire du manifeste : assemblé | un fichier dont le nom porte `-provisoire-` (sortie de la v2), un fichier de lecture de version inférieure à 3, ou une version autre que celle du manifeste, parmi les pièces à copier : assemblage refusé ; l'agent qui en trouverait un s'arrête |

G1 et G2 tournent chez conv-audit avant l'assemblage, et chez chaque agent à son départ (briefs). G5 et G4 tournent chez
conv-audit après la pièce de correction, avant la commission. G6 et G8 tournent chez conv-audit sur chaque pièce rendue,
et chez le contre-lecteur. G8 bis (a) tourne chez session-depot, sur données synthétiques, sans affichage ; G8 bis (b) et
G12 chez conv-audit à l'assemblage, et chez chaque agent à son départ (briefs). G9 et G10 tournent chez conv-audit.

## 12. Audit des agents contre la confabulation, et étalonnage à blanc

Sources : synthèse « neuron explorer » v2, § Convergences, point 4 ; synthèses « agents sur le noyau » (§ 3 : paires à
blanc) et « littérature des boucles » (§ 4 : étalonnage sur paires à blanc avant tout droit d'éliminer).

### 12.1 Dossiers à vérité connue : construction

- Avant la première lecture réelle, puis à chaque ronde de la boucle, un agent neuf reçoit un **dossier d'audit**, avec le
  même brief que l'analyste réel. Mêmes noms de fichiers (un `<dossier>` plausible), mêmes formats, mêmes effectifs : 36
  et 24 tâches par part ; sous-ensembles de 8 et 14 tâches, classes 4 et 4, 10 et 4.
- **Comment il est construit** (CLB-08) : (a) (A-test) et, pour la lecture finale, (A-final), calculés par le script de
  lecture v3 sur une banque synthétique et des courses simulées, sous la variable réservée aux essais, aux noms que le
  script v3 écrit (`-test-v<n>` ; `-test-final-holm-quatre-v<n>` par course, ou `-holm-deux-`) ; puis **forgés** par un
  script de forge empreinté (listé dans la liste d'audit) qui retire la mention « essai : empreintes de banque
  surchargées » et les empreintes de la banque synthétique, y met les empreintes réelles, et recalcule les compagnons ;
  (b) le relevé (B) forgé au même format que le vrai (spécification v2, § 7) : identité réelle de la course (tous les
  champs exigés du § 9), coûts et durées plausibles (de l'ordre du devis, illustratif, pas ceux du
  simulateur), faits plantés ; (c) une ouverture de même forme qu'une vraie, avec une référence plausible ; (d) un manifeste
  recalculé. Aucun journal dans le dossier (§ 3), donc rien qui dise à l'agent où il en est.
- Ses verdicts attendus, fiche par fiche, sont écrits d'avance par conv-audit dans la **liste d'audit** empreintée, que
  les agents ne voient pas. Le dossier y plante des faits connus. Par exemple : une fin de conception à la ronde 3 ; un
  appel de mutation sans successeur valide ; une borne atteinte ; un champ absent du relevé (verdict attendu : « non
  observable ») ; pour la lecture finale, une cellule (iii) au libellé connu ; pour le contre-lecteur, une correction qui
  porte un contenu interdit du § 14 (attendu : « non transmissible », le contenu nommé).
- L'agent ne sait pas si son dossier est un dossier d'audit. Son brief dit seulement qu'il peut l'être.
- **Mesure** : le nombre de fiches dont le verdict égale la liste d'audit. Tout verdict qui cite un champ absent du
  dossier, ou une valeur différente de celle du dossier, compte comme une confabulation. La mesure éprouve aussi la lecture
  du registre par conv-audit : un désaccord entre la liste d'audit et un agent qui cite le bon champ est examiné des deux
  côtés.
- **Règle** : aucune erreur tolérée sur les fiches que des faits mécaniques ou des libellés du script déterminent. À la
  première erreur, le brief ou le registre est corrigé (version nouvelle) et l'audit est refait avec un agent neuf, avant
  toute lecture réelle de la ronde.
- Les nombres synthétiques d'un dossier d'audit ne sortent jamais du rapport d'audit, qui ne donne que les accords et
  désaccords. La liste d'audit dit quels dossiers sont des audits. Aucun dossier d'audit n'est jamais poussé comme la
  lecture d'une course.

### 12.2 Fiches niées ou permutées

- Un agent neuf reçoit le dossier réel (après l'ouverture) ou un dossier d'audit, avec une version du registre où des
  fiches sont niées (par exemple HC-P4-01 niée : « la fin de conception est déclarée à la ronde 3 ou plus tard ») ou ont
  leur « test » échangé avec celui d'une autre fiche.
- Attendu : une fiche niée reçoit le verdict contraire (tenue ou éliminée) sur les mêmes champs ; une fiche chimère est
  signalée comme telle. Un verdict qui ne s'inverse pas sous la négation est un ancrage ou une confabulation.
- Ces fiches ne sont pas des hypothèses du registre. Elles ne reçoivent aucun verdict hors de l'audit.

### 12.3 L'agent qui « casse exprès » : un paramètre

- C'est le contre-lecteur, et tout agent d'audit chargé d'attaquer un verdict.
- Sa famille de modèle est un **paramètre** de ce protocole : « même famille que l'analyste et le correcteur », ou
  « famille différente ». La valeur est une décision de Lazar, posée au format de décision dans la pièce des points pour
  Lazar (point 1), envoyée le 26 octobre vers 05:42 UTC (heure exacte au journal de conv-audit). **Défaut : (a), même
  famille**, 48 heures après cet envoi (D4). D'ici sa réponse ou l'échéance, aucune proposition ne sort d'une ronde. La
  valeur est écrite dans chaque entrée du journal.
- Si la valeur est « famille différente », l'agent ne peut pas être un sous-agent de conv-audit de la même famille ; il
  passerait par un autre canal (par exemple l'outillage de session-depot), ce qui peut être une dépense (mot de Lazar).

### 12.4 Réplication

La partie A du contre-lecteur, faite à l'aveugle, est une réplication de l'analyse. Son accord avec l'analyste est
consigné à chaque course.

### 12.5 Étalonnage à blanc : « A contre A » avant tout droit d'éliminer

- Avant qu'un verdict d'élimination d'une course réelle soit transmissible, le brief de l'analyste est éprouvé (garde
  G10) sur : (a) un **dossier d'audit nul**, construit sur une course simulée sans aucun fait planté (mécanismes vivants,
  aucune borne atteinte, pour la lecture finale des réponses tirées d'une même loi aux générations 0 et 3) : attendu,
  aucune élimination hors de ce que la liste d'audit prévoit, « non rejetée (bruit) » sur (iii) ; (b) une **paire « A
  contre A »** : deux dossiers d'audit construits sur la même course simulée, sous deux graines et deux jeux de coûts
  plausibles, donnés à deux agents neufs : attendu, les mêmes verdicts, aucune phrase qui compare.
- Un étalonnage non passé corrige le brief ou le registre (version nouvelle) et se refait avec des agents neufs. Il est
  refait à chaque version nouvelle du brief ou du registre.
- Une paire « A contre A » réelle (le même objet, la même question, deux graines) n'existe pas dans ce pilote : c'est la
  question des graines, décision de Lazar. Avant la génération 1, les courses M et S ne diffèrent que par la graine ;
  après, par la question aussi. Ce protocole ne s'en sert pas comme d'une paire « à blanc » : elles ne sont jamais mises
  en regard (règle de préséance, § 4 ; Lazar peut reprendre la règle : pièce des points, point 5).

## 13. Lecture de `test_final`, une seule fois, à la fin du compteur

- **Quand** : après la dernière ronde de la boucle (arrêt par le compteur, le plateau, le plafond, la liste d'arrêt ou le
  mot de Lazar), et après la décision de Lazar qui ouvre cette lecture (ouverture finale, référence vérifiable). Jamais à
  la fin d'une course.
- **Ce que session-depot produit** : par le script de lecture v3 (écrit par son auteur, relu avant usage ; D1), à la fin
  de la course S, pour chacune des deux courses, `lecture-<dossier>-test-final-holm-quatre-v<n>.{json,md}` : une course,
  Holm sur les quatre tests (deux par course), la taille de la famille, les verdicts après Holm, le sens de chaque rejet et
  « aucune tâche sans réponse » par cellule, et **aucune valeur de l'autre course** (ni compte, ni proportion, ni valeur
  p, ni libellé) ; si la course S ne court pas ou ne finit pas saine, `lecture-<dossier de M>-test-final-holm-deux-v<n>`
  (option `--sans-seconde-course`). **Plus aucun fichier « provisoire »** (G12). La séparation entre courses est gardée
  par le script lui-même (son essai « séparation », G8 bis (a)), exécuté par session-depot sans affichage. Ces fichiers
  sont poussés sans être affichés jusqu'à la fin du compteur. Ni la v1 ni la v2 du script ne s'exécutent sur les courses
  (message n° 79) : sans le script v3, pas de lecture finale. Pour chaque relance : sa propre famille de deux tests, le nom
  et la règle de sa sortie fixés par son texte (§ 10).
- **Qui lit** : un analyste de la lecture finale par course, puis un contre-lecteur à l'aveugle par course (partie A).
  Fiches : HC-P4-11, HC-P4-12, HC-P4-08 sur `test_final` (par libellé), contrôle des cellules (ii) de `test_final`.
  Verdicts cités par coordonnées et libellés, jamais par valeur. Aucun calcul. Tout verdict (iii), rejet ou non-rejet,
  reçoit le même audit (R4). L'attribution d'un rejet à un mécanisme est « indécidable par ce pilote ».
- **Ce qui ne se calcule pas** : l'écart `test` − `test_final` (différence hors de la levée du point 4 bis) ; aucune
  différence entre courses ; aucune mise en commun des familles de tests de textes différents.
- **Ce qui suit** : une entrée finale du journal, avec le nombre total de tests (iii) accumulés (§ 7) et le compteur des
  lectures ; la transmission à Lazar. Aucune relance sous ce protocole après la lecture finale : une boucle nouvelle
  demande un texte nouveau et des tâches fraîches (N-049).
- **Ce qui se décide à chaque course, sans `test_final`** : les fiches mécaniques (HC-P4-01, 03, 05, 06, 07, 09), HC-P4-08
  sur `test`, le fait rapporté de HC-P4-04, les contrôles de cohérence ; et la correction de la ronde, selon la règle de
  préséance (§ 4 : après la lecture de M ; après celle de S seulement si aucune fiche de M ne motive). Les fiches
  tranchées par `test_final` (HC-P4-11, 12, HC-P4-08 sur `test_final`) le sont à la fin du compteur ; HC-P4-02 et
  HC-P4-10 restent indécidables à tout moment.

## 14. Ce que le correcteur peut changer, et ce qu'il n'écrit jamais

**Il peut changer** (un facteur de la carte à la fois) :
- un défaut de code, nommé ;
- la structure de l'organisme (par exemple désactiver un mécanisme : la mutation en génération notée, le retour arrière) ;
- les bornes internes de l'organisme (appels par tâche, délais). Pas les bornes du GO (3 dollars et 900 s par ronde,
  30 dollars et 2 400 s par génération, 75 dollars par course, 60 recherches) : elles demandent un devis et le mot de
  Lazar ;
- la règle de récompense interne : sa forme, les bornes de ses paramètres, son gabarit, le contrat de l'architecte.
  Jamais un contenu qui lie une récompense à un trait du texte d'une tâche ou à une classe. Une correction qui retirerait
  à la v6.2.1 sa réécriture de la règle la ferait sortir de la question de (b) : il le dit ;
- les castes, mais pas tant que HC-P4-06 est tenue sous un budget inchangé.

**Zones interdites** (CLB-07) : une liste close des parties du code de l'objet que le correcteur ne touche pas, écrite par
conv-audit depuis le code (`zones-interdites-v<n>.md` : fichiers, fonctions, plages de lignes), lue par G5. Point de
départ : les consignes des rôles qui répondent aux tâches ; l'analyse de la réponse du modèle qui fixe une classe ; les
constantes de mots-clés (C-16, `memoire_isvd.py` l. 81–82) et ce qui les lit ; l'exemple de format (`principal.py`
l. 794) ; tout texte d'appel servi à un modèle pour une tâche. Exception : un **« défaut du chemin des réponses »**
(format, analyse de la réponse, délai) peut être corrigé seulement si la correction ne change pas la règle qui choisit une
classe ; il est déclaré comme tel dans la pièce de périmètre et revu à part par le contre-lecteur, qui le dit dans son
verdict.

**Il n'écrit jamais, ni ne suggère** :
- un critère ou une stratégie de classement : toute règle, tout seuil, toute liste de mots, toute consigne de tâche, tout
  exemple, tout texte d'appel qui intervient dans le choix d'une classe pour une transcription ou une trace ;
- une connaissance d'une tâche de la banque : texte, identifiant (forme `t-0001`), catégorie, classe, vérité, ou tout fait
  tiré de résultats par tâche ;
- une valeur de `test_final` (score, compte, valeur p) ni aucun score dans les fichiers de l'organisme ; dans la pièce de
  correction, s'il devait citer une cellule de `test_final` (il n'en a pas pendant la boucle), la cellule et son libellé
  seulement (CLB-16 c) ;
- le registre, une fiche (`HC-P4-`), un verdict ou un fait de course, dans quoi que ce soit qui serait servi à un
  organisme (`CORRECTIONS-v<N>.md` compris) ;
- une mention du secret, de la clé, de l'archive, des réponses par tâche, des questions M ou S ou de leurs réponses.

## 15. Ce que la boucle ne fait pas

Pas de boucle intérieure (R-471). Aucun changement des textes v4 et v5 ni de leurs règles. Aucune comparaison entre les
deux courses, ni entre la v6.2.1 et la v5.3. Rien sur la valeur d'un ajout de complexité. Aucune décision sur les graines.
Rien de servi à un organisme hors de son propre code. Aucun critère de classement, nulle part. Aucune lecture de
`test_final` avant la fin du compteur. Aucun calcul de l'écart `test` − `test_final`.

## 16. Paramètres et points ouverts

Les points de Lazar sont posés au format de décision dans `points-boucle-exterieure-pilote4-pour-lazar-v1.md`
(`ac105262…`) ; ce protocole les cite sans les reposer (D4).

| paramètre ou point | qui tranche | état | défaut | moment |
|---|---|---|---|---|
| ouverture de la lecture (retenue) | Lazar, transmis par conv-audit | en attente : décision « graines » posée à part (pièce des points, point 2) | aucun (dépense) | avant toute lecture |
| famille du contre-lecteur (§ 12.3) | Lazar (pièce des points, point 1) | envoyé le 26 octobre vers 05:42 UTC | (a) même famille, 48 heures après l'envoi ; d'ici là, aucune proposition ne sort d'une ronde | avant la contre-lecture de la ronde 1 |
| plafond des relances (§ 7) | Lazar (point 3) | non fixé | aucun (dépense) | au premier devis de relance |
| symétrie d'effort avant (b) (§ 8) | Lazar (point 4) | à poser | (a) objets tels que livrés, 48 heures après l'envoi | avant l'écriture du texte de (b) |
| ordre des courses M et S pour la correction de la ronde 1 (§ 4) | conv-audit (règle de préséance, D2 ; point 5 : information ; Lazar peut la reprendre) | tranché, écrit avant toute lecture | — | — |
| question servie par une relance (§ 10) | Lazar (point 6) | à poser | aucun (dépense) | au GO de la relance |
| seuils 0,01 et 0,03 (§ 6 ; registre, § 0.5) | Lazar (point 7) | à poser | (a) garder ; tout changement attend son mot et compte pour une ronde | avant une ronde 2 |
| seuils 0,78 et 0,65 du critère de fin : un facteur ou deux | la carte des facteurs (conv-audit ne confirme rien d'avance) | en écriture | — | avant la première correction |
| carte des facteurs ; zones interdites | un sous-agent neuf de conv-audit, depuis le code de la v6.2.1 | en écriture | — | avant la première correction |
| relevé (B) : script, essais, table de correspondance | un sous-agent de conv-audit, sur la spécification v2 ; exécuté sur les courses réelles par session-depot, sans affichage (confirmé : brief v4, § 4, point 3) | en écriture | — | avant la première lecture (condition de démarrage) |
| script de lecture v3 (fichiers du § 3 et du § 13 ; libellés ; ligne d'état « signalements de test : N » ; essai « séparation ») | son auteur, relu avant usage ; exécuté par session-depot | demandé (D1) | — | avant la première lecture |
| gardes G1 à G12, dossiers d'audit, script de forge, étalonnage à blanc | un sous-agent de conv-audit, après la vérification de cette v3 (brief v4, § 4, point 7) | à écrire | — | avant la première lecture |
| forme du texte d'une relance et des noms (dont la sortie `test_final` d'une relance et la version du script qui la lit) | conv-audit, dans un texte nouveau | fixée au premier devis de relance, avant toute lecture du `test` de la relance (brief v4, § 4, point 10) | — | au premier devis de relance |
