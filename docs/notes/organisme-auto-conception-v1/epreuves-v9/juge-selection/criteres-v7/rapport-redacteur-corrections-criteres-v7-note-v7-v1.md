# Rapport du rédacteur — corrections F1, T1, M1 : critères v7, note v7 — v1

- **Auteur : rédacteur neuf, modèle F.** Je n'ai écrit ni les critères v4, v5 ou v6, ni la note v4, v5 ou v6, ni leurs programmes, ni leur contre-lecture, ni leurs contrôles, ni aucune carte, ni aucun rejeu. Écrit le 2026-11-20 (`date -u` : 2026-11-20T03:12:40Z). Processeur seul, aucune dépense, aucun appel de modèle, aucun réseau. Rien n'est écrit dans le dépôt : tout est dans mon dossier ; la session verse et scelle.
- **Mandat** : `mandat-redacteur-corrections-criteres-v7-note-v7-v1.md` (`0c366493e5cfad0383d977ab980ce1f4282b85bdf14a5ffdf0e917ce55c8646c`, égal à son compagnon). Python 3.13.18. Contrôle appliqué : `controle-differentiel-criteres-v5-v6-v1.md` (`a9793588eb0ecab67bfadde09ee535a339d4283e5ec9d13fd6f0b25511312ef4`, recalculé, égal). Outil : `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, recalculé).
- **Verdict.** T1 et M1 sont appliquées par l'outil sur les v6 versées, sous des noms neufs ; F1 est appliquée à la fiche (§ 6) ; la seconde moitié de M1 et les trois compléments du contrôle sont dans la demande de configuration (§ 5). Aucun programme ne change. Aucune carte ouverte. Aucun refus d'outil, de classifieur ni de garde ; aucun JSON rejeté par l'outil. **Un écart déclaré** : là où le texte neuf de T1 nommait la pièce sœur « v6 », les v7 la nomment « v7 », comme le mandat le demande (§ 3, point 1).

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-juge-v7/`. Chaque fichier a son compagnon `.sha256` ; `sha256sum -c` passe sur les huit premiers (le neuvième est ce rapport).

| pièce | sha256 |
|---|---|
| `criteres-choix-cartes-v9-v7.md` | `6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f` |
| `note-conception-juge-selection-cartes-ecartees-v7.md` | `bbd71b7c998866ec249556fe7803015c54aac4081dffc4e5084588819bc98a26` |
| `remplacements-criteres-v6-vers-v7-v1.json` (6 remplacements) | `2eb7db630f2893f135e7a74976962087024bb466d23a3b72319462f5c33d26fe` |
| `remplacements-note-v6-vers-v7-v1.json` (5 remplacements) | `2800d82c428cdeaaa1bc7efa20b97a7356441b1ecfa00f7da45dbeb822901b36` |
| `criteres-choix-cartes-v9-v7.md.journal-remplacements-v1.json` | `8b7639f21316516252960c25159053f13e74a79855a36a0f071786358c5e74d8` |
| `note-conception-juge-selection-cartes-ecartees-v7.md.journal-remplacements-v1.json` | `1e303c222cc328483e808d7f04eeb79f3238d3613e7b0a2d67b545cef835446b` |
| `differentiel-criteres-v6-vers-v7-v1.diff` | `3eb46e8ec887c5dea7d508c947ce79ed38cda151f9b0fbbb7d87c7d0437468a2` |
| `differentiel-note-v6-vers-v7-v1.diff` | `bd1745ff016e16bd992c494cb8c0d0bc78734f917af073130236d5bdcab31f82` |
| `rapport-redacteur-corrections-criteres-v7-note-v7-v1.md` (ce rapport) | dans son compagnon |

**Cibles** : `criteres-choix-cartes-v9-v6.md` (`6ea6f70139ccb92a4317694420c5b19749f3d2aa067fc4907f98ef812b61ca0f`) et `note-conception-juge-selection-cartes-ecartees-v6.md` (`5bcae2d3473066d65a63a8fee6ababb655e31acc199de406f1ca9d04dc09a464`), recalculées, égales au mandat. L'outil exige que chaque texte ancien figure exactement une fois : tout le reste est la v6, à l'octet près. Chaque ancre a été comptée par `grep -c -F` sur sa cible avant l'appel : une fois chacune.

**Inchangés, non recopiés** : les trois programmes joints, leurs essais et leurs sorties.

## 2. Correction par correction

| correction | appliquée | où | remarque |
|---|---|---|---|
| **T1 (i)** | oui | critères, § 13, ouverture | nomme la note v7 et son fichier |
| **T1 (ii)** | oui | critères, § 13, point 2 | « note v7, § 9 » |
| **T1 (v)** | oui | critères, § 16, ligne « Laissé tel quel, et dit » | « ceux du § 13 nomment la note v7 » |
| **T1 (iii)** | oui | note, pièces jointes | `criteres-choix-cartes-v9-v7.md` |
| **T1 (iv)** | oui | note, § 8 | de même |
| **T1 (vi)** | oui | note, § 10.4, ligne « Laissé tel quel, et dit » | « les pièces jointes et le § 8 nomment `criteres-choix-cartes-v9-v7.md` » |
| **M1, critères** | oui, à la lettre | critères, annexe B | la ligne s'écrit dans la pièce qui scelle le manifeste |
| **M1, rapport § 6, point 4** | oui, à la lettre | ce rapport, § 5, point 4 | — |
| **F1** | oui | ce rapport, § 6, décision 5 | trois options, (a), (b), (d) ; phrase ajoutée à l'enjeu ; ligne « non posée » |

**Tenue.** Dans chaque texte : le titre (« v7 ») ; une ligne « Version 7 » en tête (qui, quand, mandat, pièce remplacée, contrôle appliqué, ce qui change, aucun programme changé). Aucun paragraphe de différentiel ajouté : le mandat borne la tenue aux titres, aux lignes de version et aux renvois ; la ligne « Version 7 » dit ce qui change, et les fichiers `.diff` le montrent.

**Différentiels** : critères, six lignes touchées (titre, ligne de version ajoutée, deux au § 13, une au § 16, une à l'annexe B) ; note, cinq (titre, ligne de version ajoutée, pièces jointes, § 8, § 10.4).

## 3. Écarts, réserves, ce que je n'ai pas fait

1. **Écart à la lettre de T1, voulu par le mandat.** Le contrôle écrivait les textes neufs avec « v6 », nom des pièces d'alors. Le mandat demande des pièces v7 et « les renvois aux pièces sœurs passés en v7 ». Dans les six textes neufs de T1, j'ai donc écrit « v7 » là où le contrôle écrivait « v6 » pour la pièce sœur ; tout autre mot est celui du contrôle. Sans cela, les critères v7 auraient renvoyé à la note v6, remplacée.
2. **Renvois historiques laissés.** Les lignes « Version 6 » et « Version 5 » des en-têtes, les critères § 15 et § 16 (« note v6, § 10.4 »), la note § 10.3 et § 10.4 (« critères v6, § 16 ») nomment les pièces de leur temps : je ne les ai pas touchés. La ligne « Version 6 » de chaque pièce dit encore de lire « v6 » ; la ligne « Version 7 », placée au-dessus, dit que la lettre en vigueur est celle des v7.
3. **La note v7 garde quatre options à la décision 5.** Le contrôle dit : « La note v6 garde ses quatre options jusqu'à sa version suivante. » La v7 est cette version suivante, mais F1 ne donne aucun texte pour la note, et le mandat interdit toute autre modification. Je n'ai donc pas retiré l'option (c) de la note ; sa ligne « Version 7 » dit que la fiche fait foi pour ce qui est posé. Si la mère veut la note à trois options, c'est une correction de plus, à donner avec son texte.
4. **Dans la fiche, la ligne « non posée » dit « note v7 »**, et non « note v6 » comme l'écrit F1 : la fiche ne nomme que les pièces v7, et c'est la note v7 qui porte l'option (c).
5. **`criteres_sha256` change.** Le contrôle écrivait `6ea6f701…` « si la v6 est scellée telle quelle ». Les critères en vigueur sont la v7 : `6af793a2…`, si elle est scellée telle quelle (§ 5, point 4).
6. **Non vérifié par moi** : la ligne R-3890 sur `main` (citée d'après le contrôle précédent, qui l'a vérifiée mot pour mot) ; le commit `a41b7b50` ; les étiquettes de lignée ; les seize clés dans le programme. Je n'ai ouvert ni les programmes, ni la statistique de famille, ni la configuration de la course (empreinte recalculée seulement : `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8`, égale à celle du contrôle).
7. **Non fait** : aucun contrôle de ce différentiel v6 → v7 (règle R2 : à un autre que moi, sur ordre de la mère) ; aucun essai relancé, aucun programme n'ayant changé.
8. **Jamais touché** : aucune carte, aucun fichier de cartes ni de sélections, le champ `meta`, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucun des fichiers, dossiers, branche ou ligne interdits. Aucune commande de liste, aucun heredoc, aucun code passé en ligne, une commande simple par appel, aucun `git show`.

## 4. Ce que j'ai lu

En entier : le mandat ; le contrôle ; les critères v6 ; la note v6 ; le rapport v6 ; l'outil ; le différentiel des critères v6 → v7.

## 5. Demande de configuration finale, pour la mère

Deux fichiers à écrire par la mère, **sans ouvrir une carte**, à sceller avec leur compagnon avant l'ouverture (critères v7, annexe C, geste 1), dans le dossier où sont versées les pièces v7. Puis le manifeste d'ouverture, et la pièce qui le scelle.

**Règle d'arrêt.** Si ni le code ni la consigne des proposeurs ne donnent la liste complète et ordonnée des noms des champs de `contenu`, **la mère s'arrête et revient vers la session**. Elle n'essaie pas une liste : le masque refuserait, et seul un nombre sortirait. Une liste fausse se corrige en relisant le code ou la consigne, **jamais en ouvrant une carte**.

**Règle des valeurs.** Là où aucune pièce que j'ai lue n'établit une valeur, j'écris « à lire dans… » : aucune valeur ci-dessous n'est devinée.

**1. Où lire les noms des champs de `contenu`** (complément 1 du contrôle).
- La configuration de la course est un fichier de **ce** dépôt, non du dépôt de l'organisme : `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json`, sha256 `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8` (recalculée par le contrôle et par moi ; non ouverte).
- Le code de l'organisme, au commit de la course v9, `a41b7b50` : `orchestrator/pole/course2_v54.py` (chemin tenu de la statistique de famille, § 0, d'après le contrôle) et `course2_v56.py` (la statistique n'en donne pas le dossier : **à lire dans le dépôt de l'organisme**, le dossier `orchestrator/pole/` étant une inférence du rédacteur de la v6). Le commit n'est pas un objet de ce dépôt local, d'après le rapport v6 : la mère le vérifie.
- Ces deux fichiers sont cités pour l'écriture de `meta` et de `fiches.json`. **Rien n'établit que les noms des champs de `contenu` s'y lisent** : ils peuvent venir de la consigne des proposeurs. Le chemin de cette consigne n'est donné par aucune pièce que j'ai lue : à lire dans la configuration de la course ci-dessus. Faute de liste complète et ordonnée : règle d'arrêt.

**2. Fichier A — `configuration-masque-style-cartes-v1.json`, pour `masque_style_cartes_v1.py`.** Sept clés, ni plus ni moins :

| clé | valeur |
|---|---|
| `champs` | la liste **ordonnée et complète** des noms des champs de `contenu` : à lire dans le code ou la consigne (point 1) ; ni `meta` ni `empreinte` ; les pièces en nomment deux, `ce_qui_la_refuterait` et `axe`, et en comptent dix d'après le rapport v6 — ce compte est à confirmer à la source, non à atteindre |
| `plafond` | `"mediane"` (option (a) de la décision 5, défaut pour le rejeu) |
| `formules` | au moins `"non vérifié"` ; toute autre formule imposée : à lire dans la consigne de la course |
| `intertitres` | les intertitres imposés par la consigne de la course, à lire dans cette consigne, ou une liste vide si elle n'en impose aucun |
| `seuil_formule_recitee` | `0.2` |
| `minimum_formule_recitee` | `3` |
| `hors_choix` | les identifiants du cas X6, les mêmes qu'au manifeste : à lire dans la liste que la mère tire par programme de la sortie de l'aiguilleur (critères v7, § 2, X6) ; aucune pièce lue n'en donne le chemin |

**3. Fichier B — `configuration-lecteur-par-programme-cartes-v1.json`, pour `lecteur_par_programme_cartes_v2.py`.** Trois clés :

| clé | valeur |
|---|---|
| `champ_refutation` | le nom du champ « ce qui la réfuterait » : `ce_qui_la_refuterait` d'après les pièces, à confirmer à la source du point 1 |
| `champs_voie` | le champ du titre, puis le champ du mécanisme : noms à lire à la source du point 1 |
| `hors_choix` | la même liste qu'en A |

Contrainte : tout champ nommé en B figure dans `champs` de A, sinon le lecteur refuse la forme masquée.

**4. Manifeste d'ouverture du rejeu : les seize clés** (complément 2 du contrôle ; critères v7, annexe B). Toute clé absente ou en plus est un refus. Les noms sont ceux de l'annexe B ; ils sont à comparer à `CLES_MANIFESTE` dans `assemblage_selection_v4_v2.py`, que je n'ai pas ouvert.

| clé | valeur pour le rejeu |
|---|---|
| `identifiant_course` | la chaîne choisie par la mère ; à défaut, le nom du dossier d'archive de la course v9 : à lire sur ce dossier, aucune pièce lue ne le nomme |
| `usage` | `"rejeu"` |
| `ligne_accord` | vide pour un rejeu ; la forme du vide (chaîne vide ou null) : à lire dans `assemblage_selection_v4_v2.py` |
| `criteres_sha256` | l'empreinte des critères scellés : `6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f` si la v7 est scellée telle quelle ; sinon celle du fichier réellement scellé |
| `cartes_attendues` | 94 moins le nombre de cartes du cas X6 ; ce nombre : à lire dans la liste `hors_choix` |
| `hors_choix` | les identifiants du cas X6, la même liste qu'en A et en B |
| `nombre_vise` | `9`, à défaut de charge connue |
| `veto_par_titulaire` | `"selon_titulaires"` |
| `suppleantes` | `4` (défaut posé le 19) |
| `filtre_veto` | `"lignee"` (défaut posé le 19) |
| `plafond_veto` | `null` (défaut posé le 19) |
| `regime_items` | `"tous"` |
| `seuil_accord` | `0.75` |
| `lignee_reconnue_declaree` | faux |
| `emploie_lectures_v2` | faux |
| `familles` | la table lignée → famille ; ses clés : point 5 ; les lignées Opus et Fable dans la même famille, chaque autre dans la sienne ; les noms des familles : à lire dans `assemblage_selection_v4_v2.py` ou ses essais, aucune pièce lue ne les fixe |

Les valeurs du veto valent tant que l'option neuve n'a ni réponse ni défaut échu. Chaque valeur qui n'est pas celle des critères est justifiée par sa ligne, ici R-3890, dans la pièce qui scelle le manifeste ; le manifeste lui-même n'a que ses seize clés.

**5. Étiquettes de lignée** (complément 3 du contrôle). Les clés de `familles` doivent être les étiquettes mêmes de la table des espèces que la mère tire de `meta` par programme. D'après la statistique de famille (`bb2fa4a8…`, citée par le contrôle ; non ouverte par moi), ce sont `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra` et `prop-carbon` : à confirmer dans la statistique de famille, sans ouvrir une carte. Le champ `lignee` de chaque lecture et de chaque liste de juge doit porter l'une de ces clés, sans quoi le programme refuse. **À écrire dans la consigne des deux lecteurs** : le lecteur de la lignée Opus écrit l'étiquette de cette lignée, celui de la lignée Fable la sienne, lettre pour lettre.

**6. Gestes qui en dépendent.** Le lecteur par programme est joué deux fois avec la configuration B : `--forme fiches` sur le fichier des cartes, `--forme masque` sur la sortie du masque. La sortie masquée va à `assembler` (`--lecteur-programme`). Les deux vont à `gardes` (`--lecteur-programme-non-masque`, `--lecteur-programme-masque`), sans quoi la baisse de D sous le masque est « NON RAPPORTÉE ».

## 6. Fiche des décisions pour Lazar, prête à poser

> **Juge de sélection, critères v7 — six décisions, dont une à trancher en tête.**
>
> **Verdict.** Les critères et la note sont corrigés (v7) ; rien n'est adopté, aucune carte n'est lue, aucune dépense. Le 21 vers 14:41Z échoient les défauts posés le 19 (R-3890) : le rejeu seul, sans adoption ; le veto à la lettre de la v3. Tout ce qui est neuf ci-dessous a son propre délai : 48 heures à compter de cette fiche.
>
> **Réserve.** La ligne R-3890 tient lieu de fiche du 19 : aucune fiche n'a été retrouvée. Elle ne dit ni le retrait par lignée ni l'absence de plafond, repris de la note v3.
>
> ### En tête — la statistique de famille et les listes courtes du veto (R-4050)
>
> **Décision.** Veux-tu une pièce neuve qui rende à la statistique de famille scellée de la puissance sur les listes courtes du veto, avant toute lecture du rejeu ?
>
> **Enjeu.** Avec la correction de Holm sur douze tests, la statistique scellée ne peut presque rien signaler sur une liste de quatre à six cartes. La v4 y ajoutait deux tests à 0,025 ; la contre-lecture a montré que ce seuil était réglé d'après une valeur déjà vue. La mère a tranché (R-4050) : aucun test ajouté sans ton mot. Ils sont retirés, la limite est écrite.
>
> **Options.**
> - **(1) Garder la statistique scellée telle quelle.** Avantage : rien de scellé n'est touché, rien ne dépend d'une valeur vue. Inconvénient : elle reste presque aveugle au veto.
> - **(2) Une règle neuve, dans une pièce neuve**, motivée par les seuls effectifs, contre-lue et scellée avant toute lecture. Avantage : plus de puissance, sans désigner un test d'après les données. Inconvénient : une pièce, une contre-lecture, du délai ; son rédacteur aura vu la valeur.
> - **(3) Lecture descriptive seulement** : la p brute de chaque liste, déjà rapportée « comme indice ». Avantage : rien à changer. Inconvénient : un indice ne renvoie pas vers toi avant adoption.
>
> **Recommandation.** (1), avec (3) qui s'y ajoute sans rien écrire ; confiance 0,75.
>
> **Défaut sous 48 heures.** (1) et (3) : rien de neuf n'est écrit.
>
> ### Décision 1 — rejeu à blanc d'abord
>
> **Décision.** Rejouer les critères à blanc sur les 94 cartes de la v9 avant de les adopter pour la prochaine course ?
>
> **Enjeu.** Le rang se fait par seize questions écrites sans lecture de carte : elles peuvent ne pas ranger, ou ranger une manière d'écrire.
>
> **Options.**
> - **(a) Rejeu d'abord, sans dépense ; adoption seulement s'il range ; retour vers toi avant toute adoption si une garde se déclenche.** Avantage : on sait si la règle range avant de s'y fier. Inconvénient : deux lectures à faire ; la v9 n'est pas tenue à l'écart ; fausse alerte une fois sur cinq au plus.
> - **(b) Adopter tout de suite.** Avantage : rien à attendre. Inconvénient : un défaut se découvre sur une course payée.
> - **(c) Garder la v2 et assumer le tirage.** Avantage : simple. Inconvénient : l'erreur du critère D reste, et le veto choisit seul.
>
> **Recommandation.** (a), confiance 0,65.
>
> **Défaut.** Le rejeu seul, sans adoption : c'est le défaut posé le 19, qui échoit le 21 vers 14:41Z. Les conditions neuves de (a) (huit items gardés dans chaque voie) courent de cette fiche. Aucun usage sur une course neuve sans ton mot.
>
> ### Décision 2 — le veto : limite, plafond, retrait
>
> **Décision.** Combien de cartes de veto par titulaire, sous quel plafond, avec quel retrait par programme ?
>
> **Enjeu.** Le veto est devenu une entrée directe dans ce qui est proposé en premier. Sur le rejeu v2, les quatre cartes de veto d'espèce connue étaient de la famille des lecteurs.
>
> **Options.**
> - **(a) Trois cartes à trois titulaires au plus, deux au-delà ; plafond au nombre visé ; retrait des cartes de la famille du titulaire.** Avantage : la capture par une famille est fermée par construction. Inconvénient : tant que les deux lecteurs sont seuls titulaires, aucune carte d'Opus ni de Fable n'entre par veto.
> - **(b) Deux cartes toujours, même plafond, même retrait.** Avantage : le plus léger. Inconvénient : protège moins à deux titulaires.
> - **(c) La lettre de la v3 : trois puis deux, sans plafond, retrait par lignée.** Avantage : ton mot sans rien y ajouter. Inconvénient : c'est le cas que l'audit a vu.
>
> **Recommandation.** (a), confiance 0,6.
>
> **Défaut.** Le 21 vers 14:41Z : (c), posée le 19, pour le rejeu seulement. Puis, 48 heures après cette fiche et sans mot de toi : (a), pour le rejeu seulement.
>
> ### Décision 3 — la lignée que le lecteur croit reconnaître
>
> **Décision.** Chaque lecteur écrit-il, pour chaque carte et avant de la noter, la lignée qu'il croit reconnaître ?
>
> **Enjeu.** C'est la seule mesure sans dépense qui commence à séparer « reconnaissance du style » de « manière d'écrire » ; mais deviner l'auteur avant de noter peut créer l'effet.
>
> **Options.**
> - **(a) Non : seulement pour les cartes de veto.** Avantage : lecture non orientée. Inconvénient : les deux explications restent confondues.
> - **(b) Oui, pour chaque carte.** Avantage : note comparable à la lignée reconnue et à la lignée vraie. Inconvénient : amorçage possible ; une description, non une mesure.
>
> **Recommandation.** (b) pour le rejeu, (a) pour une course ; confiance 0,5.
>
> **Défaut sous 48 heures, à compter de cette fiche.** (a), non. Le 19, cette décision t'a été nommée sans défaut écrit ; « non » est l'état actuel.
>
> ### Décision 4 — les questions qu'un préenregistrement peut ajouter (neuve)
>
> **Décision.** Quand une carte ne dit pas une chose qu'un préenregistrement peut ajouter sans toucher au mécanisme, la question compte-t-elle « non » ou « oui » dans le rang ?
>
> **Enjeu.** Sept des seize questions sont de cette sorte ; une carte brève y reçoit zéro, et les cartes d'Astra sont les plus courtes. C'est une question de fond sur ce que la règle récompense.
>
> **Options.**
> - **(a) La lettre de la v3 : zéro.** Avantage : récompense la carte qui a pensé son épreuve. Inconvénient : peut ranger la prose plutôt que l'idée.
> - **(b) Compte oui.** Avantage : cohérent avec le critère E. Inconvénient : un jugement de plus du lecteur ; plus de places au tirage.
> - **(c) L'idée d'abord : huit questions sur l'idée rangent, les autres départagent.** Avantage : aucun jugement de plus. Inconvénient : rang moins fin.
>
> **Recommandation.** (b), confiance 0,55, à choisir avant le rejeu.
>
> **Défaut sous 48 heures.** (a), pour le rejeu seulement ; les trois régimes sont rapportés.
>
> ### Décision 5 — le masque de style (neuve)
>
> **Décision.** Les deux lecteurs lisent-ils les cartes mises en forme par programme, chaque champ coupé à la longueur médiane ?
>
> **Enjeu.** La longueur est le seul trait de surface fort de l'audit, et elle suit la famille. Mais la coupe retire la fin du champ « ce qui la réfuterait », où se lit le critère D : elle peut effacer le signal par perte de contenu. Ne rien masquer reprendrait la condition du rejeu v2, où le signal est apparu : je ne le propose pas.
>
> **Options.**
> - **(a) Masque complet, champs coupés à la médiane.** Avantage : retire le trait le plus fort, programme prêt. Inconvénient : du contenu est perdu ; l'écart par famille peut rester illisible.
> - **(b) Masque de forme, sans coupe.** Avantage : aucun contenu perdu. Inconvénient : la longueur reste visible.
> - **(d) Masque complet, sauf le champ « ce qui la réfuterait ».** Avantage : D se lit sur le champ entier. Inconvénient : demande un masque v2, contre-lu et scellé avant l'ouverture.
>
> Option (c) de la note v7, “pas de masque”, non posée.
>
> **Recommandation.** (a) pour le rejeu, confiance 0,5. La perte de D sous le masque est mesurée par programme, par espèce ; c'est elle qui dira si (d) vaut ce travail pour la course suivante.
>
> **Défaut sous 48 heures.** (a), pour le rejeu seulement.
>
> ### Huit confirmations (critères v7, § 13)
>
> Veto tenu par les deux lecteurs (écart à « par juge ») ; carte « un modèle décide » non séparable rendue à toi ; question (c) en trois ; tour de rôle entre les trois voies ; seuil d'accord de 0,75 ; neuf lignes visées et trois tirées au sort ; seuils des gardes par espèce ; phrase récitée retirée à partir d'un cinquième des cartes. **Défaut de chacune, 48 heures à compter de cette fiche : tel qu'écrit, pour le rejeu seulement.** Les six premières t'ont été portées le 19 sans défaut écrit. Aucune ne s'applique à une course neuve sans ton mot.

## 7. Refus et incidents

Aucun refus de permission, de classifieur ni de garde. Aucun JSON rejeté par l'outil : les deux appels ont réussi au premier essai (6 et 5 remplacements). Trois recherches `grep -c -F` ont rendu une erreur d'usage (motif commençant par un tiret, pris pour une option) ; refaites avec `-e`, sans effet sur aucune pièce.

*rédacteur neuf, modèle F*
