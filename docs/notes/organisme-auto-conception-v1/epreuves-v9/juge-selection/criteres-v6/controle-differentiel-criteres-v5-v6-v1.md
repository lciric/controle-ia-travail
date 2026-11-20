# Contrôle du différentiel v5 → v6 des critères et de la note du juge de sélection — v1

- **Contre-lecteur, modèle O** : le même que pour `ee578a61…` et `86a9813a…`. Je n'ai écrit ni les pièces v6, ni aucune carte. Écrit le 2026-11-20 (`date -u` : 2026-11-20T03:05:59Z). Processeur seul, aucune dépense, aucun appel de modèle, aucun réseau. Rien n'est écrit dans le dépôt.
- Dossiers : V5 = `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v5/` ; V6 = `…/juge-selection/criteres-v6/`.

## Verdict

**Conforme après corrections.**

Ce qui tient :
- Les v6 sont exactement les v5 plus les remplacements déclarés : je les ai rejoués à l'octet.
- D1 à D7 sont portées à la lettre.
- Les deux horloges, l'annexe B à deux valeurs et le motif de D6 tiennent.

**La fiche du § 7 peut partir à Lazar ce matin**, après une seule retouche de format (F1 : la décision 5 a quatre options, alors que le format en veut deux ou trois). Ses défauts et ses horloges sont exacts.

Deux autres corrections doivent être faites **avant le scellement des pièces et l'écriture du manifeste**, mais pas avant la fiche :
- T1 — **tenue seulement** : les renvois « v5 » qui comptent ;
- M1 — **moyen** : là où s'écrit la ligne R-3890. Le manifeste refuse toute clé en plus.

S'y ajoutent trois compléments à la demande de configuration (§ 4).

## 1. Empreintes et rejeu

**Empreintes.** `sha256sum -c` passe sur chaque compagnon :
- le mandat `V5/mandat-redacteur-corrections-criteres-v6-note-v6-v1.md` (`15d2a548…`) ;
- les deux textes v6 (`6ea6f701…`, `5bcae2d3…`) et les deux fichiers de remplacements ;
- les deux journaux et les deux différentiels ;
- le rapport (`1630a39a…`).

**Outil.** J'ai rejoué `remplacer_texte_exact_v1.py` (`391db990…`, recalculé sur ma copie) sur des copies des v5 (`b22827fd…`, `6ec0aeeb…`) :
- critères : 6 remplacements, sortie **`6ea6f70139ccb92a4317694420c5b19749f3d2aa067fc4907f98ef812b61ca0f`** ;
- note : 10 remplacements, sortie **`5bcae2d3473066d65a63a8fee6ababb655e31acc199de406f1ca9d04dc09a464`**.

Les deux sont égales aux pièces versées. Rien d'autre ne change : l'outil exige une occurrence unique de chaque texte ancien. J'ai lu les deux différentiels ligne à ligne.

## 2. D1 à D7, à la lettre

J'ai comparé chaque texte neuf au § 7 de mon contrôle `86a9813a…` : D1, D2, D3, D4, D5 (i à iv), D6 et D7 sont mot pour mot. La tenue (titres, lignes « Version 6 », critères § 16, note § 10.4) ne change aucune règle. Aucun programme ne change.

## 3. Les écarts déclarés

**Renvois « v5 ».** Les uns sont historiques et doivent rester : les lignes « Version 5 », les critères § 15, la note § 10.3. Quatre renvois, en revanche, désignent la pièce en vigueur, et deux d'entre eux mènent à la v5 non corrigée :
- note, ligne 11, « Pièces jointes : `criteres-choix-cartes-v9-v5.md` » ;
- note, § 8, « Critères : … v5 » ;
- critères, § 13, ouverture, « dans la note v5 » ;
- critères, § 13, point 2, « note v5, § 9 ». Celui-ci vient de mon propre texte D2 ; l'erreur est à moi.

Un lecteur qui suit ces renvois tombe sur la note v5, dont la décision 2 porte encore « Défaut : (a) ». La ligne « Version 6 » dit de lire « v6 », mais c'est précisément le passage qui compte. Ces renvois **ne gênent pas la fiche** : le § 7 ne nomme que les pièces v6. Ils gênent **les pièces jointes**, qu'il faut corriger avant le scellement. Correction T1 : tenue seulement.

**D1 nomme deux horloges.** Cela tient. La lettre du 19, (c), échoit le 21 vers 14:41Z et reste en vigueur jusqu'à l'échéance de la fiche ; ensuite vient (a). Il n'y a ni trou ni chevauchement, puisque la fiche part le 20, avant le 21 vers 14:41Z. La fiche du § 7 sépare les deux horloges en deux lignes : c'est la lecture claire.

**Annexe B à deux valeurs de `suppleantes`.** Cela tient : 6 est la valeur des critères, 4 celle du défaut du 19, et la phrase de D3 dit laquelle vaut et quand.

Mais D3, mon texte, dit « écrit au manifeste avec sa ligne ». Or `assemblage_selection_v4_v2.py` refuse tout manifeste dont les clés diffèrent des seize de `CLES_MANIFESTE`. La ligne R-3890 ne peut donc pas s'écrire dans le manifeste. Le défaut vient de la v4, et D3 l'a reconduit. Correction M1.

**D6, (a) à 0,5.** Le motif tient et ne vise aucun signe :
- (a) et (d) sont les seules options qui retirent la longueur ;
- aucun programme scellable ne sert (d) aujourd'hui ;
- la perte de D est mesurée, dans les deux sens ;
- le rejeu n'a aucune valeur de sélection.

L'argument contre « deux passes du masque v1 » est juste : la configuration serait écrite après une passe de programme sur les cartes.

**Commit `a41b7b50` et chemins cités** : comparés à mon contrôle.
- `orchestrator/pole/course2_v54.py` et le commit `a41b7b50` sont ceux de mon contrôle. Je les tenais de la statistique de famille, § 0.
- `orchestrator/pole/course2_v56.py` : la statistique n'écrit que `course2_v56.py`, sans dossier. Le dossier est une inférence du rédacteur.
- **La configuration n'est pas dans le dépôt de l'organisme**, contrairement à ce que laisse lire « au commit `a41b7b50` ». C'est un fichier de **ce** dépôt : `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json`, sha256 `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8`, recalculé, égal à la statistique. Je ne l'ai pas ouvert.
- Mon contrôle l'écrivait abrégé : l'ambiguïté vient de moi (§ 4, complément 1).

## 4. La demande de configuration (§ 6)

Elle est juste pour les deux fichiers : sept clés pour le masque, trois pour le lecteur, avec la contrainte d'inclusion. Elle **suffit à la mère pour écrire les deux fichiers sans ouvrir de carte**, avec ces trois compléments :

1. **Où lire les champs.** Il faut le chemin complet de la configuration, ci-dessus, dans ce dépôt.
   Les deux fichiers de l'orchestrateur sont cités par la statistique pour l'écriture de `meta` et de `fiches.json`. Rien n'établit que les noms des champs de `contenu` s'y lisent : ils peuvent venir de la consigne des proposeurs.
   Si ni le code ni la consigne ne donnent la liste complète et ordonnée, la mère s'arrête et revient vers la session. Elle n'essaie pas une liste : le masque refuserait, et seul un nombre sortirait.
2. **Manifeste : les seize clés**, puisque toute clé absente ou en plus est un refus. Le § 6 n'en nomme que onze. Il manque :
   - `identifiant_course` (à défaut, le nom du dossier d'archive de la course) ;
   - `ligne_accord` (vide pour un rejeu) ;
   - `criteres_sha256` (l'empreinte des critères scellés, `6ea6f701…` si la v6 est scellée telle quelle) ;
   - `cartes_attendues` (94, moins les cartes du cas X6) ;
   - `hors_choix`.
3. **Étiquettes de lignée.** Les clés de `familles` doivent être les étiquettes mêmes de la table des espèces que la mère tire de `meta`. D'après la statistique de famille, ce sont `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra` et `prop-carbon`. Le champ `lignee` de chaque lecture et de chaque liste de juge doit porter l'une de ces clés, sans quoi le programme refuse. Il faut l'écrire dans la consigne des deux lecteurs.

## 5. La fiche du § 7

**Juste.**
- En tête, le point R-4050, avec les options de la contre-lecture.
- « Le 21 vers 14:41Z échoient : le rejeu seul, sans adoption ; le veto à la lettre de la v3 » : exact, d'après R-3890.
- « Tout ce qui est neuf a son propre délai : 48 heures à compter de cette fiche » : exact. Cela vaut pour les décisions 1 (conditions neuves), 2 ((a)), 3, 4 et 5, et pour les huit confirmations.
- La décision 3 et les six premières confirmations sont dites « portées le 19 sans défaut écrit » : exact.
- La réserve sur R-3890 est écrite.

**Au format**, sauf un point : la décision 5 a **quatre** options, alors que le format de `CLAUDE.md` en veut « 2 ou 3 ». C'est la correction F1. L'option (d) vient de mon C4.

## 6. Corrections

**F1 — format — fiche, § 7, décision 5, avant l'envoi.**
- Ancien : la ligne « > - **(c) Pas de masque.** Avantage : la carte telle qu'elle est. Inconvénient : c'est la condition où le signal est apparu. ».
- Nouveau : rien à la place de cette ligne. À la fin de l'enjeu, ajouter : « Ne rien masquer reprendrait la condition du rejeu v2, où le signal est apparu : je ne le propose pas. »
- Les lettres (a), (b) et (d) restent, pour garder les renvois des critères et de la note.
- La note v6 garde ses quatre options jusqu'à sa version suivante. La fiche fait foi pour ce qui est posé, et cela se dit en une ligne sous la décision 5 : « Option (c) de la note v6, “pas de masque”, non posée. »

**T1 — tenue seulement — avant le scellement.** Par l'outil, sous des noms neufs (règle R12).
- (i) Critères, § 13. Ancien : « Elles sont au format de décision dans la note v5 (`note-conception-juge-selection-cartes-ecartees-v5.md`, § 9). » Nouveau : « Elles sont au format de décision dans la note v6 (`note-conception-juge-selection-cartes-ecartees-v6.md`, § 9). »
- (ii) Critères, § 13, point 2. Ancien : « qui ne devient défaut que 48 heures après que la mère l'a posée ; note v5, § 9). » Nouveau : « qui ne devient défaut que 48 heures après que la mère l'a posée ; note v6, § 9). »
- (iii) Note, ligne 11. Ancien : « - **Pièces jointes** : `criteres-choix-cartes-v9-v5.md`, les critères ». Nouveau : « - **Pièces jointes** : `criteres-choix-cartes-v9-v6.md`, les critères ».
- (iv) Note, § 8. Ancien : « « Critères » : `criteres-choix-cartes-v9-v5.md`. ». Nouveau : « « Critères » : `criteres-choix-cartes-v9-v6.md`. ».
- (v) Critères, § 16. Ancien : « les renvois à « la note v5 » et à son nom de fichier (§ 13, texte de D2 compris ; § 15) se lisent « la note v6 ». ». Nouveau : « les renvois à « la note v5 » du § 15, historiques, restent ; ceux du § 13 nomment la note v6. ».
- (vi) Note, § 10.4. Ancien : « les renvois à `criteres-choix-cartes-v9-v5.md` (en-tête, § 8) se lisent `criteres-choix-cartes-v9-v6.md`. ». Nouveau : « les renvois à `criteres-choix-cartes-v9-v5.md` de la ligne « Version 5 », historiques, restent ; les pièces jointes et le § 8 nomment `criteres-choix-cartes-v9-v6.md`. ».

J'ai vérifié que chacun de ces textes anciens figure une seule fois dans sa pièce.

**M1 — moyen — avant le manifeste.**
- Critères, annexe B. Ancien : « écrit au manifeste avec sa ligne (de `registres/go.md` ou de `registres/decisions.md`). » Nouveau : « écrit avec sa ligne (de `registres/go.md` ou de `registres/decisions.md`) dans la pièce qui scelle le manifeste — non dans le manifeste, que le programme refuse s'il porte une clé de plus que les seize de l'annexe. »
- Rapport, § 6, point 4. Ancien : « Chaque valeur qui n'est pas celle des critères porte sa ligne : ici R-3890. » Nouveau : « Chaque valeur qui n'est pas celle des critères est justifiée par sa ligne, ici R-3890, dans la pièce qui scelle le manifeste ; le manifeste lui-même n'a que ses seize clés. »

**Compléments à la demande (§ 4, points 1 à 3)** : à remettre à la mère avec le § 6 du rapport. Ils ne touchent aucun texte scellable.

## 7. Ce que j'ai lu, et incidents

- **Lu en entier** : le mandat du rédacteur v6 ; son rapport ; les deux différentiels ; les lignes des v6 citées ici.
- **Recalculé sans l'ouvrir** : l'empreinte de la configuration de la course v9.
- **Pas de nouveau** : ni programme, ni essai, puisque rien n'a changé. Mes essais et mes défauts glissés du contrôle précédent valent toujours pour les mêmes programmes.
- **Mes copies** : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/contre-lecture-juge-v4/controle-v6/`.
- **Jamais touché** : aucune carte, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucun fichier, branche ou ligne interdits.
- **Aucun refus** d'outil ni de classifieur. Une commande simple par appel, aucun `git show` dans ce contrôle, aucun heredoc, aucun code en ligne.

*contre-lecteur, modèle O*
