# Protocole de la boucle extérieure du pilote 4 — v1

**Statut.** Version 1. Écrite le 26 octobre 2026 par un sous-agent neuf de la lignée conv-audit, sur le brief v2
(`LISEZMOI-brief-v2.md`, `bb472681…`) et le brief v1 (`brief-boucle-exterieure-v1.md`, `54fe31f1…`). Écriture achevée le
2026-10-26 à 03:58:24 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Écrite avant tout score : l'auteur n'a lu
aucun score ni aucun fait de course. Pièce de travail d'un pilote de conception : ni préenregistrement ni scellement au
sens de R1 ; relecture gardée, donc à contre-lire par un agent neuf avant le premier usage. Elle ne modifie ni le texte du
pilote 4 (`pilote4-gemini-organisme-v4.md`, `782b858c…`) ni ses règles. Rien de cette pièce n'est servi à un organisme.
Les heures des mots de Lazar sont celles de Paris ; les autres sont en UTC.

**But.** Lazar, 26 octobre, 02:17 : « go » sur la boucle extérieure. À la fin de chaque course du pilote 4, des agents
neufs lisent la sortie du script de lecture et un relevé mécanique. Ils statuent fiche par fiche, selon le registre
(`registre-hypotheses-conception-pilote4-v2.md`). Ils proposent la ronde suivante. Toute relance est une course nouvelle,
sur le mot direct de Lazar dans la session de session-depot (dépense). La boucle intérieure (primitive d'expérience dans
le noyau, R-471) n'est pas dans ce protocole.

## 0. Mots employés

- **Course** : un objet qui tourne sous le noyau, en un ou plusieurs segments, du lancement à la fermeture.
- **Ronde de la boucle** (numéro k = 1, 2 ou 3) : une course d'un objet, sa lecture et sa proposition de correction. La
  ronde 1 d'un objet est sa course du pilote 4. À ne pas confondre avec une **ronde de conception**, interne à une course.
- **Dossier de course** : ce que session-depot pousse à la fin d'une course (liste fermée, `EMPREINTES-pilote-v1.txt`,
  archive `ferme.tar.gz`, extrait mécanique, journaux, `LANCEMENT.md`…). Aucun agent ne l'ouvre.
- **Dossier de lecture** : le dossier que conv-audit assemble pour les agents d'une ronde, à partir de pièces nommées
  seulement (§ 3). C'est la seule chose qu'un agent voit, avec son brief et son dossier de sortie.
- **(A)**, **(B)**, **(C)** : la sortie du script de lecture, le relevé mécanique, le code de l'objet à son commit
  (registre, § 0.1).
- **Facteur** : un seul levier de conception de l'organisme, nommé (§ 6).
- **Journal des essais** : le journal de la boucle (§ 5).

## 1. Quand la boucle démarre (conditions cumulées)

1. **La course est finie.** Sa liste fermée est poussée avec son fichier d'empreintes, et la recherche des clés est faite.
   Jamais pendant une course. Jamais entre deux segments : une course arrêtée par `STOP`, qui attend son segment K+1,
   n'est pas finie.
2. **La lecture est ouverte.** Tant que Lazar n'a pas tranché la question des graines de plus (posée à 02:05 ; trois tours
   du collisionneur demandés à 03:27 ; décision pendante), ou dit de lire, personne ne lit un score du pilote 4. Session-depot
   pousse la sortie du script sans l'afficher (texte v4, § Décisions, 03:27). La boucle ne démarre que lorsque conv-audit
   transmet la décision de Lazar qui ouvre la lecture. Conv-audit l'écrit dans le dossier de lecture :
   `ouverture-lecture-<course>-v1.txt` (les mots de Lazar ou leur référence ; heure lue sur `date -u` dans la commande qui
   l'écrit).
3. **Rien de la boucle ne se lit sous la retenue, fiches mécaniques comprises.** Plusieurs faits mécaniques portent un
   bit sur les scores de `test` : la ronde de la déclaration de fin (canal (b)), les appels de mutation en génération notée
   (canal (d)), le retour arrière et la taille de la mémoire (P4v3, § Plan, point 3). Ce que session-depot lit pendant et
   entre les segments, et ses portes de santé (porte « v6.2 précédente », déclencheurs mécaniques du critère 1), restent
   tels que le texte v4 les règle : ce n'est pas la boucle.
4. **Si la décision ouvre la lecture par un texte nouveau** (par exemple des graines de plus, ces deux courses comptant
   comme premières graines), ce texte est poussé avant toute lecture de leurs scores (texte v4, § Décisions, 02:05). S'il
   change la règle de lecture, le registre et les briefs reçoivent une version nouvelle avant la première lecture.
5. **Les gardes (§ 11) et l'audit (§ 12) ont été essayés** sur un cas sain et sur un artefact (R5) avant la première
   lecture. Leurs issues sont consignées au journal des essais (§ 5).
6. **Les pièces de la boucle ont été contre-lues** (relecture gardée) et poussées avec leurs empreintes. Le texte v4 les
   veut poussées avant la fin de la première course (§ Décisions, 02:17). Si elles le sont après, conv-audit l'écrit au
   journal.
7. **Le paramètre « famille du contre-lecteur » est fixé par Lazar** (§ 12.3). Sans lui, l'analyste et le correcteur
   peuvent travailler, mais aucune proposition ne sort de la ronde.

## 2. Qui lit quoi

| qui | lit | ne lit jamais |
|---|---|---|
| session-depot | exécute le script de lecture à la fin de chaque course, dans son conteneur (il lit le secret, sans jamais l'afficher) ; pousse la sortie avec son empreinte, sans l'afficher sous la retenue ; produit le relevé (B) ; écrit en réserve dans ses textes qu'il a lu ces scores en les exécutant (texte v4, point 4 bis ; R-473) | ce que ses propres règles lui interdisent |
| conv-audit | transmet l'ouverture ; assemble le dossier de lecture en copiant des fichiers nommés et en vérifiant leurs empreintes, sans les ouvrir ; lance les agents ; tient le journal ; transmet les propositions à Lazar ; après l'ouverture, peut lire la sortie (texte v4, point 3) | le secret, l'archive fermée, les textes de tâches |
| analyste | le dossier de lecture : (A), (B), ouverture, registre, protocole, journal | la liste interdite |
| correcteur | la pièce de l'analyste ; le dossier de lecture ; (C), en copie de lecture | la liste interdite |
| contre-lecteur | partie A : le dossier de lecture seul ; partie B : ensuite seulement, les pièces de l'analyste et du correcteur, et (C) | la liste interdite ; les pièces de l'analyste et du correcteur avant d'avoir empreinté sa partie A |
| agent d'audit | un dossier d'audit (§ 12), aux mêmes noms qu'un dossier réel | la liste interdite |
| Lazar | ce qu'il décide de lire | — |

**Liste interdite, pour tous les agents.** Les fichiers de banque (`banque-confrontation-v*.json`, `*-cle.json`,
`*-secret.json`). L'archive fermée `ferme.tar.gz` et tout ce qui en est tiré (mémoire, réponses par tâche, code des
successeurs, fichiers écrits par l'organisme pendant la course). Les journaux d'appels bruts (`journal-appels*.jsonl`),
l'extrait mécanique brut (`extrait-mecanique*.json`) et `LANCEMENT.md` : on n'en lit que le relevé (B). La réponse à la
question M (`reponse-question*`). `P3-consignes-v1.md`, `textes-actions-…`. Les dossiers `donnees/`, `runs/`, `diag/`,
`pilotes/`. Les réponses du collisionneur (branches `donnees/collisionneur-…`). Toute clé ou tout jeton. Tout score d'un
autre pilote. Pendant la lecture d'une course : la sortie de l'autre course.

## 3. Le dossier de lecture

Conv-audit l'assemble pour chaque ronde. Chemins relatifs à `<dossier-de-lecture>/`. Les noms marqués « proposé » sont à
confirmer avec session-depot.

- `MANIFESTE-DOSSIER-v1.txt` (proposé) : chaque fichier du dossier avec son empreinte, au format « empreinte, deux
  espaces, nom ». Chaque agent le vérifie par `sha256sum -c` avant de lire.
- `ouverture-lecture-<course>-v1.txt` (proposé) : la décision qui ouvre la lecture (§ 1.2).
- `lecture/lecture-<course>-v1.md` et `lecture/lecture-<course>-v1.json`, avec leurs `.sha256` : la sortie (A), pour cette
  course seulement. Après la lecture des deux courses, le dossier d'une course ne porte que le fichier de cette course.
- `mecanique/releve-mecanique-<course>-v1.txt` (proposé), avec son `.sha256` : le relevé (B). Champs demandés ; chacun
  porte « absent » s'il n'est pas disponible, jamais une estimation :
  1. identité : commit, empreinte d'arbre et nombre de fichiers de l'objet ; graine du manifeste ; nom et empreinte du
     lanceur ; noyau ; empreinte de la banque ; empreinte du texte ;
  2. segments : nombre ; fin de chacun (`STOP` et heure, reprise, reprise refusée, fermeture) ; dernier code ; fin de la
     lignée ; liste fermée poussée et recherche des clés faite ;
  3. par unité (rondes de conception c001…, générations notées g000 à g003) : statut, durée, coût ; appels par statut ;
     appels par rôle ; recherches et téléchargements par source ;
  4. déclaration de fin de conception : ronde, nom du critère écrit, nombre d'exemplaires ; ni score interne ni exactitude
     d'entraînement ;
  5. par unité : successeur muté produit, déclaré valide, ayant tourné à l'unité suivante ; motif de refus de chaque appel
     de mutation, s'il est consigné comme un statut fixe ;
  6. par unité : empreinte de chaque fichier de l'organisme (au moins `politique_endogene.py`), sans contenu ;
  7. par génération notée : taille de la mémoire, en octets ; événement de restauration, s'il y en a ;
  8. par génération notée : nombre de castes et événements de mitose, s'ils sont disponibles ;
  9. événements `DELAI_DEPASSE` et refus `PLAFOND`.
  Le relevé ne porte aucun texte de tâche, aucune consigne, aucune réponse de modèle, aucun score ; seul le nom du critère
  de fin est recopié tel quel. Il est produit par un script empreinté (à écrire, ou à dériver de
  `releve_appels_simulation_v3.py`, `1e9df693…`), essayé avant la première lecture sur les pièces de simulation de la
  série v13 (cas sain) et sur un artefact (un champ de texte planté doit être refusé).
- `objet/` : copie de lecture du dossier `organisme/` au commit de l'objet, et `objet/EMPREINTE-ARBRE.txt` (empreinte
  d'arbre recalculée par conv-audit, égale à celle qui est attendue). Pour le correcteur et le contre-lecteur.
- `registre/`, `protocole/`, `journal/` : la version en vigueur du registre, ce protocole, la dernière version du journal
  des essais, chacun avec son `.sha256`. Le journal porte les issues des gardes et de l'audit (§ 11 et 12), sans aucune
  valeur synthétique.

## 4. Les trois rôles, et leur ordre

Ordre : analyste, puis correcteur, puis contre-lecteur. À chaque ronde, chaque rôle est tenu par un sous-agent neuf, lancé
par conv-audit. Il n'a écrit aucune des pièces qu'il lit et n'a lu aucun score de ce pilote avant sa tâche. Les briefs sont
dans `brief-agents-fin-de-course-v1.md`, à donner tels quels.

1. **Analyste.** Il vérifie l'ouverture, la fin de la course et l'identité de l'objet. Il donne un verdict par fiche, avec
   le champ qui le fonde. Il liste les faits suspects (R4). Il vérifie les cellules (ii). Il marque les verdicts (iii)
   provisoires ou finals. Il rend `verdicts-<course>-ronde-<k>-v1.md`.
2. **Correcteur.** Il lit l'analyse. Il propose au plus une correction (un facteur), ou aucune, ou une demande
   d'instrumentation, ou l'arrêt. Pour une correction : le facteur ; les fiches et verdicts qui la motivent ; le périmètre
   déclaré ; le diff contre la copie de l'objet ; les essais de la correction ; l'observation mécanique attendue à la ronde
   suivante ; ce qu'elle ne dit pas. Il rend `correction-<course>-ronde-<k>-v1.md` et `.diff`.
3. **Contre-lecteur** (l'agent qui « casse exprès » ; sa famille de modèle est un paramètre, § 12.3). Partie A, à
   l'aveugle : il applique le registre au même dossier et empreinte ses verdicts avant d'ouvrir l'analyse. Partie B : il
   compare, attaque l'analyse et la correction (un facteur, périmètre, contenu interdit, motivation, essais). Il conclut
   « transmissible à Lazar », « transmissible après corrections » ou « non transmissible ». Il rend
   `contre-lecture-<course>-ronde-<k>-partie-A-v1.md` puis `contre-lecture-<course>-ronde-<k>-v1.md`.
4. **Désaccords.** Une fiche sur laquelle l'analyste et le contre-lecteur diffèrent ne motive aucune correction dans cette
   ronde. Le désaccord est consigné au journal et soumis à conv-audit.
5. **Ensuite.** Conv-audit écrit l'entrée du journal. Il ne transmet à Lazar qu'une ronde « transmissible ». La
   proposition part avec son devis et les mots exacts que Lazar écrirait dans la session de session-depot.

## 5. Journal des essais

- Un journal pour la boucle, versionné (R12) : `journal-essais-boucle-pilote4-v<N>.md`. Chaque version reprend la
  précédente mot pour mot, ajoute ses entrées et cite l'empreinte de la précédente. Conv-audit l'écrit et le pousse sur le
  canal.
- **Tout essai est consigné, échecs compris** : gardes, audits, lectures refusées, pièces d'agents refusées, corrections
  refusées, essais en échec, hypothèses éliminées, relances refusées par Lazar.
- Aucune valeur numérique de `test_final` n'y est écrite : une cellule se cite par ses coordonnées et son libellé.
- Format d'une entrée :

```
### Entrée <numéro> — <course> — ronde <k> — <date et heure lues sur date -u>
- objet : commit <…>, arbre <…>, <n> fichiers ; graine du manifeste <…>
- lecture : ouverte par <référence de la décision> ; course finie (liste fermée <empreinte>)
- pièces lues : <noms et empreintes>
- fiches testées : <liste>
- verdicts : <fiche : verdict de l'analyste / verdict du contre-lecteur ; champ cité>
- désaccords : <liste, ou « aucun »>
- correction proposée : <facteur ; périmètre ; empreinte du diff>, ou « aucune » (raison)
- ce qui a échoué : <liste, ou « rien »>
- audit des agents : <dossiers d'audit donnés ; accords et désaccords avec la vérité connue>
- paramètres : famille du contre-lecteur = <valeur fixée par Lazar>
- décision de Lazar : <relance, arrêt, autre ; référence>, ou « en attente »
- dépense : <ligne de dépense>, ou « aucune »
- écarts déclarés : <liste, ou « aucun »>
```

## 6. Un facteur à la fois

- Entre deux rondes d'un même objet, un seul facteur change. Un facteur est un levier nommé par la conséquence d'une fiche
  du registre, ou un défaut de code nommé. Exemples tirés du registre : nombre minimal de rondes avant la déclaration de
  fin ; nombre de tâches d'entraînement du score interne ; les deux seuils du critère de fin, comptés ensemble ; le
  décalage d'indice de la v5.3 ; un élément du contrat de l'architecte ; le seuil ou la fenêtre de stagnation ; la
  mutation en génération notée ; le seuil du retour arrière ; le retour arrière lui-même ; une borne interne par tâche ; le
  chemin de formulation de la moisson.
- La graine change à chaque course (texte nouveau, entropie nouvelle, R9). Ce n'est pas un facteur de conception : c'est du
  bruit. La dérive des modèles appelés aussi. C'est pourquoi une correction ne s'évalue jamais par une différence de score
  entre deux rondes (registre, § 0.6).
- **Comment on le garantit** :
  1. Le correcteur déclare, avant d'écrire le diff, le facteur et son périmètre : fichiers, fonctions, plages de lignes au
     commit de l'objet.
  2. Le diff (unifié, contre la copie de lecture) ne touche que ce périmètre, plus une liste close de fichiers
     d'accompagnement : `manifeste.json` (champs de version et de description seulement) ; un `CORRECTIONS-v<N>.md`
     nouveau ; un `tests/test_corrections_v<N>.py` nouveau ; un essai hérité adapté, seulement si la correction l'exige,
     déclaré avec sa raison. C'est la forme de la correction de la v6.2.1 par conv-audit (C-14 à C-17).
  3. Un script de contrôle du périmètre (garde G5) compare chaque bloc du diff au périmètre déclaré et refuse tout bloc
     hors de lui.
  4. Le contre-lecteur lit le diff et confirme qu'il n'y a qu'un facteur.
  5. Conv-audit commite la correction (les agents n'ont pas `git`), recalcule l'arbre et vérifie que l'écart entre le
     commit précédent et le nouveau est le diff transmis. Le lanceur dérivé épingle ce commit (§ 9).

## 7. Règle d'arrêt, par objet

La boucle s'arrête pour un objet à la première de ces conditions :
1. **Trois rondes** de la boucle (k = 3 : la course du pilote 4 et au plus deux relances), avant la confirmation sur la
   banque v6.
2. **Plus aucune fiche ne motive de correction** : chaque fiche est éliminée, ou indécidable (par ce pilote, dans le
   bruit, ou non observable), ou tenue sans correction attachée. C'est la lecture, par ce protocole, de « toutes éliminées
   ou indécidables sans graines de plus » (brief v1).
3. **Dépassement du plafond de Lazar** : un plafond pour les relances de la boucle, à fixer par Lazar (aucun n'est fixé à
   l'écriture de ce protocole), ou le plafond d'un GO.
4. **Une ligne de la liste d'arrêt** du texte en vigueur (texte v4, ou texte de la relance) : défaut, course hors de la
   liste close, fait suspect (R4).
5. **Le mot de Lazar.**

Une demande d'instrumentation n'est pas une relance : elle change le relevé ou le script (versions nouvelles), pas
l'organisme.

## 8. Exploration et confirmation

- Tout ce que la boucle conclut sur la banque v3 est exploratoire et non opposable (R7). Les pièces de verdicts sont à
  part, exploratoires, poussées sur le canal, hors du rapport de lecture et hors des critères gelés. Elles restent tenues
  par l'interdit de comparer les deux objets (texte v4, point 3 ; P4C7-02).
- Ce qui part en confirmation se scelle avant toute lecture d'un score de la banque v6 (Lazar, 01:56 : les expériences de
  confirmation gardent le scellement). Ses auteurs déclarent avoir lu les scores de conception (R-473). Banque v6 (lot 3) ;
  jamais la v3, ni la v5, qui partage ses textes avec la v3.
- Les hypothèses du pilote décisif (b) sont écrites sans aucun score (`hypotheses-pilote-decisif-b-v1.md`, `903c6b51…`,
  pour information). La boucle ne les change pas. Si la boucle produit des versions corrigées, le texte de (b) les nomme
  (commit, arbre) avant toute lecture d'un score de la banque v6, comme il le prévoit. Une correction qui retirerait à la
  v6.2.1 sa réécriture de la règle de récompense la ferait sortir de la question de (b) : le correcteur le dit s'il la
  propose.
- Rien de la boucle n'est servi à un organisme ni à Gemini : ni le registre, ni les verdicts, ni les motifs des
  corrections. L'organisme de la ronde suivante ne reçoit que son code. Le document de correction joint au code ne cite que
  des faits mécaniques : jamais un score, un libellé de (iii) ou une valeur de `test_final`.

## 9. Contrôle d'identité des objets

Avant tout verdict, l'analyste compare l'identité portée par le relevé (B) aux valeurs attendues :

| course | objet | commit | arbre | fichiers | graine du manifeste |
|---|---|---|---|---|---|
| `pilote4-gemini-v6-2-v1` | v6.2.1 | `7ea32705c5437d91ed071dd95fb3209bb0b0035e` | `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d` | 26 | 2334107546136117589 |
| `pilote4-gemini-v5-3-v1` | v5.3 | `4ecba58bcaa7dc3abe82c54fc38ee7285620bdf6` | `6251ab219e86286ec892a65e28cf9eebad5265fd6e32e350e68827897c811753` | 22 | 755578208180416146 |

Communs aux deux : lanceur `lancer_pilote4_gemini_v10.sh` (`0203f546…`) ; noyau `8e5e2f7b` ; banque `157a2b45…` ; texte
`782b858c…`. Tout écart : aucune lecture ; fait suspect (R4) ; conv-audit et Lazar informés. Pour un objet relancé : le
lanceur dérivé épingle le commit, l'arbre et le nombre de fichiers, comme le lanceur v10 le fait (essais
`organisme-v6-2`, `nombre-v6-2`, `seg-organisme-modifie`) ; le même contrôle s'applique, aux valeurs du texte de la
relance.

## 10. Relance

- Une relance est une course nouvelle. Jamais une course de plus sous le texte v4. Jamais la reprise d'une course fermée.
- Il lui faut :
  1. un texte, version nouvelle (R12), de pilote de conception (relecture gardée : contre-lecture par un agent neuf), qui
     nomme l'objet corrigé (commit, arbre, nombre de fichiers), le facteur et l'empreinte du diff, sa graine (entropie
     tirée pour lui, R9), ses bornes et son devis ;
  2. un lanceur dérivé du v10 par remplacements exacts, sa batterie et sa série d'essais (R5), qui épingle l'objet
     nouveau ;
  3. une ligne de GO (extension ou nouvelle) qui porte l'arbre de l'objet, et une ligne de dépense ;
  4. le mot direct de Lazar dans la session de session-depot (dépense ; aucun défaut) ;
  5. le lancement par session-depot.
- Nom versionné : un nom jamais employé, qui porte l'objet et la ronde ; sa forme est fixée par le texte de la relance.
- Une relance ne change ni le texte v4 ni ses règles. Le départ de la v5.3 sous le texte v4 n'en dépend pas.
- Des graines de plus pour un même objet, ou un autre objet, ne sont pas des relances de la boucle : ce sont des décisions
  de Lazar (la question des graines est pendante depuis 02:05). La boucle rapporte seulement ce qui reste indécidable.
- Refusée : une relance « pour voir si les scores bougent » (R3 ; registre, HC-P4-11).

## 11. Gardes à essayer avant la première lecture (R5 : un cas sain et un artefact chacune)

Chaque garde est un script ou un contrôle écrit, empreinté, essayé, consigné au journal des essais. Leurs auteurs sont à désigner
par conv-audit. Aucune ne lit un score réel : elles emploient des pièces de simulation (série v13) et des données
synthétiques, comme les essais du script de lecture. Elles peuvent donc tourner sous la retenue.

| garde | cas sain (accepté) | artefact (refusé ou détecté) |
|---|---|---|
| G1 — lecture pendant une course | course finie : liste fermée présente et vérifiée, recherche des clés consignée, aucune « reprise attendue » après le dernier segment | course simulée arrêtée par `STOP` entre deux segments (« reprise attendue : SEGMENT=K+1 »), ou sans liste fermée : assemblage refusé |
| G2 — lecture sous la retenue | `ouverture-lecture-<course>-v1.txt` présent, qui cite une décision | fichier absent ou vide : assemblage refusé ; l'agent refuse de commencer |
| G3 — faux dossier de course à scores marqueurs | dossier synthétique dont les valeurs sont des marqueurs choisis par son auteur, gardés dans une liste empreintée que les agents ne voient pas ; toute la ronde tourne dessus, et ses pièces restent des pièces d'essai, jamais transmises à Lazar ; aucun marqueur d'une cellule de `test_final` n'apparaît dans une pièce de la boucle, dans ce qui serait servi à un organisme ou sur la sortie standard du script | une pièce de la boucle, ou l'arbre d'un organisme, qui porte un marqueur : détecté |
| G4 — faux fichier de `test_final` servi par erreur à un organisme | l'arbre de l'organisme corrigé, inspecté : aucun nom interdit, aucun marqueur, aucune chaîne tirée de (A) : accepté | le même arbre avec un fichier `test_final` synthétique planté (ou un fichier qui porte un marqueur, ou la copie d'une pièce de lecture) : refusé avant toute relance ; l'épinglage de l'arbre par le lanceur garantit que ce qui tourne est ce qui a été inspecté |
| G5 — diff qui touche deux facteurs | diff dans le périmètre déclaré, plus la liste d'accompagnement : accepté | diff qui touche deux facteurs (par exemple le seuil de stagnation et le seuil du retour arrière) : refusé |
| G6 — comparaison entre les objets | pièce de verdicts d'une seule course | pièce qui cite les deux courses, une différence v6.2.1 − v5.3, ou une phrase qui les juxtapose : refusée par le contre-lecteur et par un contrôle de motifs (les deux noms de course dans une même pièce) |
| G7 — libellé (ii) « au-dessus » | sortie synthétique qui ne porte que « non distinct » : rien | sortie synthétique qui porte un « au-dessus » : l'analyste le rapporte comme signal de défaut (R4) |
| G8 — valeur de `test_final` recopiée | pièce de verdicts qui cite les cellules par coordonnées et libellés | pièce qui porte une valeur marqueur d'une cellule de `test_final` : refusée |

G1 et G2 tournent chez conv-audit avant l'assemblage, et chez chaque agent à son départ (briefs).

## 12. Audit des agents contre la confabulation

Source : synthèse du collisionneur « neuron explorer » v2, § Convergences, point 4 (« nuls indiscernables »).

### 12.1 Dossiers à vérité connue

- Avant la première lecture réelle, puis à chaque ronde de la boucle, un agent neuf reçoit un **dossier d'audit**, avec le
  même brief que l'analyste réel. Mêmes noms de fichiers, mêmes formats, mêmes effectifs : 36 et 24 tâches par part ;
  sous-ensembles de 8 et 14 tâches, classes 4 et 4, 10 et 4. Il est construit à partir d'une course simulée (faux appels,
  aucune clé ; par exemple les cas de la série v13) et d'une sortie de script calculée sur une banque synthétique (comme
  dans les essais du script).
- Ses verdicts attendus, fiche par fiche, sont écrits d'avance par conv-audit dans une **liste d'audit** empreintée, que
  les agents ne voient pas. Le dossier y plante des faits connus. Par exemple : une fin de conception à la ronde 3 ; un
  appel de mutation sans successeur valide ; une borne atteinte ; un champ absent du relevé (verdict attendu : « non
  observable ») ; une cellule (iii) au libellé connu.
- L'agent ne sait pas si son dossier est un dossier d'audit. Son brief dit seulement qu'il peut l'être.
- **Mesure** : le nombre de fiches dont le verdict égale la liste d'audit. Tout verdict qui cite un champ absent du
  dossier, ou une valeur différente de celle du dossier, compte comme une confabulation.
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
  signalée comme telle (son test ne porte pas sur son énoncé). Un verdict qui ne s'inverse pas sous la négation est un
  ancrage ou une confabulation.
- Ces fiches ne sont pas des hypothèses du registre. Elles ne reçoivent aucun verdict hors de l'audit.

### 12.3 L'agent qui « casse exprès » : un paramètre

- C'est le contre-lecteur, et tout agent d'audit chargé d'attaquer un verdict.
- Sa famille de modèle est un **paramètre** de ce protocole : « famille du contre-lecteur » = « même famille que
  l'analyste et le correcteur », ou « famille différente ». La valeur est une décision de Lazar, en attente (synthèse
  « neuron explorer », Décisions pour Lazar, point 2). Ce protocole ne fixe aucune valeur par défaut. La valeur est écrite
  dans chaque entrée du journal.
- Si la valeur est « famille différente », l'agent ne peut pas être un sous-agent de conv-audit de la même famille. Il
  passerait par un autre canal (par exemple l'outillage de session-depot), ce qui peut être une dépense (mot de Lazar).
  À vérifier.

### 12.4 Réplication

La partie A du contre-lecteur, faite à l'aveugle, est une réplication de l'analyse. Son accord avec l'analyste est
consigné à chaque ronde.

## 13. Lecture de (iii) entre les deux courses

- **Après la seule course de la v6.2.1** : verdicts provisoires au seuil 0,0125 (script). Un rejet provisoire est final,
  sous Holm sur quatre ou sur deux. Un non-rejet dont la valeur p brute dépasse 0,05 est final. Sinon : « en attente ». Un
  rejet provisoire peut motiver une correction ; un non-rejet en attente ne motive rien.
- **Après la course de la v5.3** : le script, sur les deux courses, rend Holm sur les quatre tests. Un analyste neuf redit
  les verdicts (iii) de la v6.2.1 à partir du seul fichier de la v6.2.1. Conv-audit le consigne dans une entrée nouvelle.
  Un changement est rapporté comme l'effet de la seule correction de multiplicité. Aucune pièce ne met les deux courses
  côte à côte.
- **Si la v5.3 ne part pas** : session-depot relance le script pour Holm sur deux tests ; même redite.
- Une course relancée appartient à la famille de tests de son propre texte. Elle n'est jamais mise en commun avec les
  quatre tests du texte v4.

## 14. Ce que le correcteur peut changer, et ce qu'il n'écrit jamais

**Il peut changer** (un facteur à la fois) :
- un défaut de code, nommé ;
- la structure de l'organisme (par exemple désactiver un mécanisme : la mutation en génération notée, le retour arrière) ;
- les bornes internes de l'organisme (appels par tâche, délais). Pas les bornes du GO (3 dollars et 900 s par ronde,
  30 dollars et 2 400 s par génération, 75 dollars par course, 60 recherches) : elles demandent un devis et le mot de
  Lazar ;
- la règle de récompense interne : sa forme, les bornes de ses paramètres, son gabarit, le contrat de l'architecte.
  Jamais un contenu qui lie une récompense à un trait du texte d'une tâche ou à une classe ;
- les castes, mais pas tant que HC-P4-06 est tenue sous un budget inchangé.

**Il n'écrit jamais, ni ne suggère** :
- un critère ou une stratégie de classement : toute règle, tout seuil, toute liste de mots, toute consigne de tâche, tout
  exemple, tout texte d'appel qui intervient dans le choix d'une classe pour une transcription ou une trace. Les
  constantes de mots-clés (C-16) en font partie : il n'y touche pas ;
- une connaissance d'une tâche de la banque : texte, identifiant, catégorie, classe, vérité, ou tout fait tiré de
  résultats par tâche ;
- une valeur de `test_final` (score, compte, valeur p, libellé), ni aucun score dans les fichiers de l'organisme ;
- le registre ou les verdicts, dans quoi que ce soit qui serait servi à un organisme.

Un défaut du chemin des réponses (format, analyse de la réponse du modèle, délai) peut être corrigé seulement si la
correction ne change pas la règle qui choisit une classe.

## 15. Ce que la boucle ne fait pas

Pas de boucle intérieure (R-471). Aucun changement du texte v4 ni de ses règles. Aucune comparaison entre les deux objets.
Rien sur la valeur d'un ajout de complexité. Aucune décision sur les graines. Rien de servi à un organisme hors de son
propre code. Aucun critère de classement, nulle part.

## 16. Paramètres et points ouverts

| paramètre ou point | qui tranche | état à l'écriture |
|---|---|---|
| ouverture de la lecture (retenue) | Lazar, transmis par conv-audit | en attente (graines, 02:05) |
| famille du contre-lecteur | Lazar | en attente ; aucune valeur par défaut |
| plafond des relances de la boucle | Lazar | non fixé |
| forme du relevé (B) et son script | conv-audit et session-depot | à écrire et à essayer (R5) |
| champs à ajouter à (A) : score de `test` rendu, nombre sans réponse par cellule, b et c, un fichier par course | conv-audit (version nouvelle du script) | à demander |
| opération (2) du registre (HC-P4-04 et 05) | conv-audit | à confirmer ou refuser |
| auteurs des gardes G1 à G8 et des dossiers d'audit | conv-audit | à désigner |
| forme du texte d'une relance et des noms | conv-audit | à fixer |
