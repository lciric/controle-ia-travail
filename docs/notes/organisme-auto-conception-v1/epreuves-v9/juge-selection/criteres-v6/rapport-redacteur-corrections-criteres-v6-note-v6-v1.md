# Rapport du rédacteur — corrections D1 à D7 : critères v6, note v6 — v1

- **Auteur : rédacteur neuf, modèle F.** Je n'ai écrit ni les critères v4 ou v5, ni la note v4 ou v5, ni leurs programmes, ni leur contre-lecture, ni leur contrôle, ni aucune carte, ni aucun rejeu. Écrit le 2026-11-20 (`date -u` : 2026-11-20T03:01:21Z). Processeur seul, aucune dépense, aucun appel de modèle, aucun réseau. Rien n'est écrit dans le dépôt : tout est dans mon dossier ; la session verse et scelle.
- **Mandat** : `mandat-redacteur-corrections-criteres-v6-note-v6-v1.md` (`15d2a5481540a4f8e15e203e5caae66e4394bf0a360ad684c54037d21e75e64f`, égal à son compagnon). Python 3.13.18. Contrôle appliqué : `controle-differentiel-criteres-v4-v5-v1.md` (`86a9813aa3cc8ffebc7f7f839c2bfd72cbe37a7547bb2107bd166a419061d2d8`, recalculé, égal). Outil : `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, recalculé).
- **Verdict.** Les sept corrections D1 à D7 sont appliquées à la lettre, par l'outil, sur les v5 versées. Aucun programme ne change. Aucune carte ouverte. Aucun refus d'outil ni de classifieur. Un point non vérifié : le commit `a41b7b50` n'est pas un objet de ce dépôt local (§ 6, point 1).

## 1. Pièces rendues

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-juge-v6/`. Chaque fichier a son compagnon `.sha256`.

| pièce | sha256 |
|---|---|
| `criteres-choix-cartes-v9-v6.md` | `6ea6f70139ccb92a4317694420c5b19749f3d2aa067fc4907f98ef812b61ca0f` |
| `note-conception-juge-selection-cartes-ecartees-v6.md` | `5bcae2d3473066d65a63a8fee6ababb655e31acc199de406f1ca9d04dc09a464` |
| `remplacements-criteres-v5-vers-v6-v1.json` (6 remplacements) | `4c1205b528748e3cc9952dc8f38d9b24a49c1dba4f583fd39329bede9e56eb82` |
| `remplacements-note-v5-vers-v6-v1.json` (10 remplacements) | `df0aa7ce3552d25756ba92178feaf8a9de88acdeb58283419d4a4d8301e34378` |
| `criteres-choix-cartes-v9-v6.md.journal-remplacements-v1.json` | `09b752969d13356737b1672d4d282b4f3c7edbd5cd72abb2267a6e6baa8fc9b6` |
| `note-conception-juge-selection-cartes-ecartees-v6.md.journal-remplacements-v1.json` | `988a13dc9794b685c6096a877cbffbb3493ef20588b0e863c12de657974a0dea` |
| `differentiel-criteres-v5-vers-v6-v1.diff` | `4f436ce952ba672beefa93f082e5c0da26b4764971ff8a68bf2511990b02963e` |
| `differentiel-note-v5-vers-v6-v1.diff` | `5883ec59456c6bea0f8f0224294d02dcc96ce89f225dc5284fb649de9f96db43` |
| `rapport-redacteur-corrections-criteres-v6-note-v6-v1.md` (ce rapport) | dans son compagnon |

**Cibles** : `criteres-choix-cartes-v9-v5.md` (`b22827fd056fa56326372525f78562c2dc9206ffc6cda560ca99c96ed3748237`) et `note-conception-juge-selection-cartes-ecartees-v5.md` (`6ec0aeebcd9756094750449444e5f9dd9401fd4499ee6d4384579fa06f4aee5b`), recalculées, égales au mandat. L'outil exige que chaque texte ancien figure exactement une fois : tout le reste est la v5, à l'octet près.

**Inchangés, non recopiés** : les trois programmes joints (`assemblage_selection_v4_v2.py`, `masque_style_cartes_v1.py`, `lecteur_par_programme_cartes_v2.py`), leurs essais et leurs sorties, tels que le rapport v5 (`296993591622e6b84a9a6b62d7ac8325064d3b4eb77b894786f825591564a979`) les liste.

## 2. Correction par correction

| correction | appliquée | où | remarque |
|---|---|---|---|
| **D1** — défaut de la décision 2 | oui, à la lettre | note, § 9, décision 2 | jusqu'à 48 heures après la pose de la fiche : (c), la lettre du 19 ; ensuite (a) |
| **D2** — défaut du veto | oui, à la lettre | critères, § 13, décision 2 | le texte dit « note v5, § 9 » : gardé à la lettre ; l'en-tête v6 dit de lire « note v6 » |
| **D3** — valeurs du manifeste | oui, à la lettre | critères, annexe B | `filtre_veto` « lignee », `plafond_veto` null, `suppleantes` 4 |
| **D4** — défaut de la décision 1 | oui, à la lettre | note, § 9, décision 1 | — |
| **D5** — source juste, option (d) | oui, les quatre points | note, § 9 : ouverture (i, iv), décision 3 (ii), confirmations (iii) | — |
| **D6** — recommandation de la décision 5 | oui, texte du contrôle | note, § 9, décision 5 | confiance 0,5 gardée, motivée au § 3 |
| **D7** — lecture de C4 | oui, à la lettre | critères, § 1 | aucun programme ne change |

**Tenue.** Dans chaque texte : le titre (« v6 ») ; une ligne « Version 6 » en tête (qui, quand, mandat, pièce remplacée, contrôle appliqué, aucun programme changé, comment lire les renvois aux pièces v5) ; un différentiel v5 → v6 (critères § 16, note § 10.4) avec une ligne « Laissé tel quel, et dit ». Le contrôle permettait l'un ou l'autre : j'ai choisi le différentiel propre, pour ne pas retoucher les § 15 et § 10.3.

## 3. La recommandation de la décision 5 (D6), motivée

J'ai gardé le texte et la confiance du contrôle : **(a) pour le rejeu, confiance 0,5**.
- (a) et (d) sont les deux seules options qui retirent la longueur, seul trait de surface fort que l'audit ait trouvé.
- (d) protège le champ que lit D. Mais aucun programme scellable ne la sert aujourd'hui : il faut un masque v2, contre-lu et scellé avant l'ouverture. La voie « deux passes du masque v1 » n'est pas essayée, et elle ferait écrire une configuration après une première passe sur les cartes.
- (a) peut rendre illisible l'écart par famille au rejeu (critères, § 1). La commande `gardes` mesure cette perte, par espèce ; elle ne la corrige pas.
- Entre un rejeu tout de suite, dont une lecture peut rester en suspens, et un rejeu après un cycle de programme, le choix est presque égal. D'où 0,5, et non le 0,6 écrit avant que (d) existe.
- Rien ici ne vise un résultat sur une espèce (règle R3) : le rejeu n'a aucune valeur de sélection, et la mesure est rapportée quel que soit son sens.

## 4. Écarts, réserves, ce que je n'ai pas fait

1. **Renvois aux pièces v5 laissés dans le texte.** Les critères v6 disent encore « note v5 » (§ 13, texte de D2 compris ; § 15) ; la note v6 dit encore `criteres-choix-cartes-v9-v5.md` (en-tête v5, § 8). Je ne les ai pas remplacés : le mandat borne la tenue aux titres et aux lignes de version. La ligne « Version 6 » de chaque pièce dit comment les lire.
2. **Une phrase de D1 se lit avec soin.** « Jusqu'à 48 heures après que cette fiche t'a été posée : (c) […] c'est elle qui échoit le 21 vers 14:41Z. » Deux horloges y sont nommées : celle du 19, pour la lettre de la v3 ; celle de la fiche, pour (a). C'est la lettre du contrôle ; la fiche du § 7 les sépare en deux lignes.
3. **L'annexe B porte deux valeurs de `suppleantes`** : 6 entre parenthèses (valeur des critères), 4 pour le défaut du 19 (D3). C'est voulu par D3 ; dit au § 16 des critères.
4. **Non vérifié** : la ligne R-3890 sur `main` (je la cite d'après le complément 1 et le contrôle, qui l'a vérifiée mot pour mot) ; le commit `a41b7b50` (§ 6).
5. **Non lu** : les programmes, leurs essais, les différentiels v4 → v5, la note v3, la statistique de famille scellée. Aucune correction n'y porte.
6. **Non fait** : aucun contrôle de ce différentiel v5 → v6 (règle R2 : à un autre que moi, sur ordre de la mère) ; aucun essai relancé, aucun programme n'ayant changé.
7. **Jamais touché** : aucune carte, aucun fichier de cartes ni de sélections, le champ `meta`, rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`, aucun des fichiers, dossiers, branche ou ligne interdits. Aucune commande de liste, aucun heredoc, aucun code passé en ligne, une commande simple par appel.

## 5. Ce que j'ai lu

En entier : le mandat ; le contrôle ; les critères v5 ; la note v5 ; le rapport v5 ; le complément 1 ; l'outil. Deux recherches par `grep` sur les deux fichiers v5 nommés, pour les espaces insécables (aucune).

## 6. Demande de configuration complète et finale, pour la mère

Deux fichiers à écrire par la mère, **sans ouvrir une carte**, à sceller avec leur compagnon avant l'ouverture (critères v6, annexe C, geste 1), dans le dossier où sont versées les pièces v6. Puis le manifeste d'ouverture.

**1. Où lire les noms des champs de `contenu`.** Dans le code qui écrit les cartes, au commit de la course v9, `a41b7b50` : `orchestrator/pole/course2_v54.py` et `orchestrator/pole/course2_v56.py`, et la configuration `course-v4/configuration-course-auto-conception-v5.json`. Je cite ces chemins d'après le contrôle (§ 5), qui les tient de la statistique de famille, § 0. **Non vérifié par moi** : `a41b7b50` n'est pas un objet du dépôt local (`git cat-file -e` : « invalid object name ») ; je n'ai lancé aucun `fetch`. La mère vérifie le commit et les chemins avant d'écrire. Un champ manquant ou en trop arrête le masque, et son message ne donne qu'un nombre : une liste fausse se corrige en relisant le code, **jamais en ouvrant une carte**.

**2. Fichier A — `configuration-masque-style-cartes-v1.json`, pour `masque_style_cartes_v1.py`.** Sept clés, ni plus ni moins :

| clé | valeur |
|---|---|
| `champs` | la liste **ordonnée et complète** des noms des champs de `contenu`, lus au code ; ni `meta` ni `empreinte` ; dix champs d'après les pièces, dont `ce_qui_la_refuterait` et `axe` |
| `plafond` | `"mediane"` (option (a) de la décision 5, défaut pour le rejeu) |
| `formules` | au moins `"non vérifié"` |
| `intertitres` | les intertitres imposés par la consigne de la course, ou une liste vide ; si la consigne impose « pourquoi cela compte », le mettre (audit, § 8, point 3, cité d'après le contrôle) |
| `seuil_formule_recitee` | `0.2` |
| `minimum_formule_recitee` | `3` |
| `hors_choix` | les identifiants du cas X6, les mêmes qu'au manifeste |

**3. Fichier B — `configuration-lecteur-par-programme-cartes-v1.json`, pour `lecteur_par_programme_cartes_v2.py`.** Trois clés :

| clé | valeur |
|---|---|
| `champ_refutation` | le nom du champ « ce qui la réfuterait » : `ce_qui_la_refuterait` d'après les pièces, à confirmer au code |
| `champs_voie` | le champ du titre, puis le champ du mécanisme, noms lus au code |
| `hors_choix` | la même liste qu'en A |

Contrainte : tout champ nommé en B figure dans `champs` de A, sinon le lecteur refuse la forme masquée.

**4. Manifeste d'ouverture du rejeu** (critères v6, annexe B). Valeurs du veto tant que l'option neuve n'a ni réponse ni défaut échu (D3) :

| clé | valeur |
|---|---|
| `filtre_veto` | `"lignee"` |
| `plafond_veto` | `null` |
| `suppleantes` | `4` |
| `veto_par_titulaire` | `"selon_titulaires"` |

Les autres clés gardent les valeurs des critères : `usage` « rejeu » ; `nombre_vise` 9 à défaut de charge connue ; `regime_items` « tous » ; `seuil_accord` 0,75 ; `lignee_reconnue_declaree` faux ; `emploie_lectures_v2` faux ; `familles` (Opus et Fable dans la même). Chaque valeur qui n'est pas celle des critères porte sa ligne : ici R-3890.

**5. Gestes qui en dépendent.** Le lecteur par programme est joué deux fois avec la configuration B : `--forme fiches` sur le fichier des cartes, `--forme masque` sur la sortie du masque. La sortie masquée va à `assembler` (`--lecteur-programme`). Les deux vont à `gardes` (`--lecteur-programme-non-masque`, `--lecteur-programme-masque`), sans quoi la baisse de D sous le masque est « NON RAPPORTÉE ».

## 7. Fiche des décisions pour Lazar, prête à poser

> **Juge de sélection, critères v6 — six décisions, dont une à trancher en tête.**
>
> **Verdict.** Les critères et la note sont corrigés (v6) ; rien n'est adopté, aucune carte n'est lue, aucune dépense. Le 21 vers 14:41Z échoient les défauts posés le 19 (R-3890) : le rejeu seul, sans adoption ; le veto à la lettre de la v3. Tout ce qui est neuf ci-dessous a son propre délai : 48 heures à compter de cette fiche.
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
> **Enjeu.** La longueur est le seul trait de surface fort de l'audit, et elle suit la famille. Mais la coupe retire la fin du champ « ce qui la réfuterait », où se lit le critère D : elle peut effacer le signal par perte de contenu.
>
> **Options.**
> - **(a) Masque complet, champs coupés à la médiane.** Avantage : retire le trait le plus fort, programme prêt. Inconvénient : du contenu est perdu ; l'écart par famille peut rester illisible.
> - **(b) Masque de forme, sans coupe.** Avantage : aucun contenu perdu. Inconvénient : la longueur reste visible.
> - **(c) Pas de masque.** Avantage : la carte telle qu'elle est. Inconvénient : c'est la condition où le signal est apparu.
> - **(d) Masque complet, sauf le champ « ce qui la réfuterait ».** Avantage : D se lit sur le champ entier. Inconvénient : demande un masque v2, contre-lu et scellé avant l'ouverture.
>
> **Recommandation.** (a) pour le rejeu, confiance 0,5. La perte de D sous le masque est mesurée par programme, par espèce ; c'est elle qui dira si (d) vaut ce travail pour la course suivante.
>
> **Défaut sous 48 heures.** (a), pour le rejeu seulement.
>
> ### Huit confirmations (critères v6, § 13)
>
> Veto tenu par les deux lecteurs (écart à « par juge ») ; carte « un modèle décide » non séparable rendue à toi ; question (c) en trois ; tour de rôle entre les trois voies ; seuil d'accord de 0,75 ; neuf lignes visées et trois tirées au sort ; seuils des gardes par espèce ; phrase récitée retirée à partir d'un cinquième des cartes. **Défaut de chacune, 48 heures à compter de cette fiche : tel qu'écrit, pour le rejeu seulement.** Les six premières t'ont été portées le 19 sans défaut écrit. Aucune ne s'applique à une course neuve sans ton mot.

## 8. Refus et incidents

Aucun refus d'outil, aucun refus de classifieur, aucune commande bloquée. Trois commandes ont rendu une erreur, sans effet : une recherche `grep` mal écrite (refaite) ; deux `git cat-file -e` sur `a41b7b50`, objet absent du dépôt local.

*rédacteur neuf, modèle F*
