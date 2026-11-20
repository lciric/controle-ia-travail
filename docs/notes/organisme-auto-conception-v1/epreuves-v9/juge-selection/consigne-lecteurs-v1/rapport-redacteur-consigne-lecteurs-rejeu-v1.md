# Rapport du rédacteur — consigne des deux lecteurs du rejeu (critères v7) — v1

- Rédacteur neuf, modèle F. Écrit le 2026-11-20 (`date -u` au début de la rédaction : 2026-11-20T05:14:06Z). Processeur seul, aucune dépense, aucun appel de modèle. Rien n'est écrit dans le dépôt, aucun commit.
- Pièce rendue : `consigne-lecteurs-rejeu-criteres-v7-v1.md`, dans le même dossier que ce rapport ; son empreinte est à son compagnon `.sha256`.
- **Verdict** : la consigne est écrite, une seule pour les deux lecteurs. Elle tient la forme que le programme accepte, vérifiée ligne par ligne. Cinq points restent ouverts (§ 4), dont deux sont des choix de ma main que la lettre scellée ne fixe pas.

## 1. Sources, avec chemin et empreinte

Toutes les empreintes ont été recalculées par `sha256sum`.

| pièce | chemin | sha256 | ce que j'en ai lu |
|---|---|---|---|
| Mandat | `docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/criteres-v7/mandat-redacteur-consigne-lecteurs-rejeu-v1.md` | `567d212ee7bd0ce45145264555f6acb2935ec756105c5292ec864619127b07c0` (compagnon : OK) | en entier |
| Critères v7 scellés | `origin/main:prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md` (commit `0b265f658bdfd3dda8bc432a1f05f2f15766d2e6`), copié dans mon dossier | `6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f`, égale à celle du mandat | en entier (388 lignes) |
| Note v7 scellée | `origin/main:prereg/organisme-auto-conception-v9/juge-selection/note-conception-juge-selection-cartes-ecartees-v7.md`, copiée dans mon dossier | `bbd71b7c998866ec249556fe7803015c54aac4081dffc4e5084588819bc98a26`, égale à celle du mandat | les intertitres, puis le seul § 9 (lignes 257 à 358) : les cinq décisions et les huit confirmations |
| Table du manifeste | `…/juge-selection/criteres-v7/table-manifeste-rejeu-apres-go-2026-11-20-10-v1.md` | `a41a2c7c748b4adc54a25d31f373cc981f85f7f73bcad434e34cc5f7574667d5` | en entier ; sa réserve sur `lignee_reconnue` est aux lignes 84 et 85 |
| Réponses sur les familles | `…/juge-selection/criteres-v7/reponses-familles-et-champ-x6-v1.md` | `35cc9bcfed53d9d3f6cd30a2280dd535bcc58f52f0e6c749e999b43b16239fec` | en entier |
| Programme d'assemblage | `…/juge-selection/criteres-v5/assemblage_selection_v4_v2.py` | `2f5640daaeae042d16fb22486a5994a41f0eb26b6e9f190c7984a38bfa5afdf6` | lignes 30 à 359, 488 à 599, 1034 à 1109, 1190 à 1285 ; recherches de motifs sur ce seul fichier |
| Registre des GO | `origin/main:registres/go.md` (même commit), copié dans mon dossier | copie : `faa6bd5175a6639a944485b6ab6112b938dabb7e8cbd47fca22e5aa8a31f9a4b` | par recherche de motif, les seules lignes 540 et 541 : « O2 recos » et « Juge, critères v7 : en tête (1) et (3) ; décision 1 (a) ; 2 (a) ; 3 (b) au rejeu et (a) en course ; 4 (b) ; 5 (a) au rejeu ; huit confirmations telles qu'écrites. » |

**Non ouverts** : les deux notes de rejeu antérieures (`rejeu-a-blanc-criteres-v2-lecteur-f-v1.md`, `5d8d537a…` ; `rejeu-a-blanc-criteres-v2-lecteur-o-v1.md`, `209243b7…`). Le mandat les donne « pour mémoire » ; l'en-tête des critères dit qu'elles nomment des cartes. J'ai calculé leur empreinte et je ne les ai pas lues : la consigne n'en avait pas besoin. Non ouverts non plus : aucune carte, aucun fichier de cartes ni de sélection, rien sous `archives-reponses-modeles/`, le programme de masque, le lecteur par programme, les configurations de course.

**Ce que j'ai vu qui touche aux cartes, dit d'avance** : par le § 9 de la note v7, des comptes agrégés du rejeu v2 (11 sur 16 contre 1 sur 46 ; quatre cartes de veto de la famille des lecteurs ; « les cartes d'Astra sont les plus courtes »). Aucun identifiant, aucun texte de carte.

## 2. Ce que j'ai vérifié dans le programme (fichier et ligne)

Fichier : `assemblage_selection_v4_v2.py` (`2f5640da…`).

**En tête de la lecture.**
- l. 160-161 : les clés de tête sont exactement `lecteur`, `lignee`, `independance`, `cartes`, `veto`.
- l. 162, avec l. 1205-1206 : `lecteur` doit valoir `"F"` pour le fichier passé par `--lecture-f`, `"O"` pour `--lecture-o`.
- l. 164 : `lignee` doit être une clé de la table `familles` du manifeste. D'où `prop-fable` et `prop-opus`, lettre pour lettre (table du manifeste, ligne 40 et lignes 44 à 48).
- l. 166, avec l. 154-155 : `independance` est une chaîne non vide ; son texte n'est pas contrôlé.
- l. 168 : `cartes` est une liste non vide.

**Par carte.**
- l. 171-174 : douze clés, plus `lignee_reconnue` quand le manifeste porte `lignee_reconnue_declaree` à vrai ; l. 183-185 : toute clé en trop ou manquante est un refus. D'où « treize clés, exactement ».
- l. 48 et l. 178-179 : `meta`, `espece`, `proposeur`, `contenu` interdites.
- l. 186-187 : aucune carte en double.
- l. 41 et l. 188-196 : `exclusion` vaut `null` ou un objet `cas` (X1 à X5) et `phrase` ; `separable`, booléen, exigé pour X1 et refusé ailleurs.
- l. 197-203 : `voie` parmi I, N, P ; `sous_strate` parmi les sept en voie P, `null` ailleurs.
- l. 204-207 : `question` `null` ou texte ; voie N sans question et Q non nul : refus.
- l. 208-210 : `E`, `Q`, `D` entiers 0, 1 ou 2, booléen refusé.
- l. 211-213 : `raisons` à trois clés non vides.
- l. 42-46 et l. 214-220 : dix-huit items ; valeurs `oui`, `non`, `indecidable`, `ajoutable` ; « ajoutable » refusée hors de T3, B2, B3, B4, S1, S3, S4.
- l. 221-223 : `phrases` aux mêmes dix-huit clés, non vides.
- l. 224-225 : `groupe_fusion` `null` ou texte.
- l. 552-557 : les deux lectures portent les mêmes cartes, aucune carte hors du choix, et exactement `cartes_attendues`.

**`lignee_reconnue` — le point que le mandat met en gras.**
- l. 226-227 : pour une carte, le programme contrôle **seulement qu'un texte non vide est présent**. Aucune liste de valeurs permises.
- l. 238-241 : de même pour chaque entrée de veto.
- l. 1067-1081 : la commande `gardes` calcule `familles.get(lignee_reconnue) == familles[lignée du lecteur]` (l. 1071). Une valeur absente de la table — `aucune`, mais aussi toute faute de graphie — rend `None` et tombe dans « ne croit pas » (l. 1079), sans refus ni message. La réserve de la table du manifeste (lignes 84 et 85) est donc exacte ; la consigne l'impose au § 4 et la fait relire au § 10.
- l. 1071 encore : seule la **famille** de la lignée reconnue est comparée. `prop-opus` et `prop-fable` y pèsent de même. Les trois autres étiquettes et `aucune` aussi, entre elles. La distinction des cinq étiquettes n'est lue par aucun calcul de ce programme ; elle reste dans la lecture déposée.
- l. 532-534 : la `lignee_reconnue` d'une entrée de veto est seulement recopiée dans la sortie ; aucun calcul ne la lit, et rien ne la compare à celle de la même carte dans `cartes`.

**Veto.**
- l. 233-245 : une liste ; chaque entrée a exactement `id`, `prediction`, `decision`, `lignee_reconnue`, non vides ; aucune carte deux fois. Une liste vide passe.
- l. 574-579 : sous `selon_titulaires` et trois titulaires au plus, V = 3 ; une liste de plus de V + `suppleantes` entrées est refusée : 3 + 6 = 9 sous la décision 2 (a).
- l. 580-582 : chaque identifiant est une carte lue.
- l. 500-523 : parcours dans l'ordre déposé ; retrait par famille du titulaire (l. 512-513) ; « sans objet » pour une carte écartée ou rendue (l. 514-515) ou déjà visée (l. 516-517) ; suppléante non appelée au-delà de V (l. 518-519).
- l. 525-534 et l. 585 : plafond au nombre visé, servi par tour de rôle.

**Régime.** l. 47 et l. 250-255 : sous `ajoutables_oui`, « ajoutable » vaut 1 ; sinon 0.

## 3. Ce que la consigne dit, en regard du mandat

| demande du mandat | où, dans la consigne |
|---|---|
| ce que les lecteurs reçoivent, jamais l'espèce ni `meta` | § 1 |
| ce qu'ils rendent, au format de l'annexe A et sous la forme du programme | § 2, § 3, gabarit au § 3.4 |
| le veto et sa liste (décision 2 (a)) | § 7 |
| les questions « ajoutables » (décision 4 (b)) | § 5 |
| la lignée reconnue, carte par carte (décision 3 (b)) | § 4, rappelée aux § 3.3, § 7 et § 10 |
| le champ `lignee` de chaque lecteur, lettre pour lettre | § 3.1 |
| ce que le lecteur ne fait jamais | § 8 |
| aucun identifiant de modèle | tenu : les lignées sont nommées par leurs étiquettes ; « modèle F » ne figure que dans la signature que le mandat impose |

**La phrase sur `lignee_reconnue`** (consigne, § 4, mot pour mot) : « Le champ `lignee_reconnue` porte, pour chaque carte et pour chaque entrée de ta liste de veto, exactement l'une de ces six chaînes, lettre pour lettre, en minuscules, sans espace, sans guillemet ni ponctuation ajoutés : `prop-opus`, `prop-fable`, `prop-argon`, `prop-astra`, `prop-carbon`, ou `aucune`. »

## 4. Ce qui reste ouvert

1. **Aucun contrôle par programme de `lignee_reconnue`.** La consigne impose les six chaînes, mais une faute passerait encore en silence (l. 226 et l. 1071). Un contrôle de la mère sur chaque lecture déposée, avant `assembler` — chaque valeur est une clé de `familles` ou `aucune` — fermerait le cas. Il demanderait un petit programme neuf, hors des trois programmes scellés : à décider par la mère. Sans lui, la seule garde est la relecture du lecteur (consigne, § 10).
2. **Choix de ma main, que la lettre ne fixe pas : la famille reconnue sans la lignée.** Les critères (§ 1) disent « la lignée ou la famille » ; le mandat n'ouvre que cinq étiquettes de lignée et « aucune ». Pour le lecteur qui croit reconnaître la famille Opus-Fable sans dire laquelle, la consigne demande l'étiquette la plus probable des deux (§ 4), parce que le programme ne compare que la famille (l. 1071). L'autre lecture possible est « aucune », qui ferait compter ce cas comme « ne croit pas ». À confirmer par la mère ou le contre-lecteur.
3. **Choix de ma main : où s'écrit la limite sur la famille des lecteurs.** Les critères (§ 1) la veulent « en tête de chaque lecture » ; l'annexe A et le programme (l. 160) ne laissent aucune clé pour elle. La consigne la met en première ligne d'une **note de dépôt** à côté du fichier (§ 9), et garde `independance` pour la seule déclaration du § 1. La note de dépôt elle-même n'est prévue par aucune pièce scellée : je l'ai ajoutée pour que les écarts aient un lieu hors du JSON. À confirmer.
4. **Deux règles de tenue ajoutées, sans appui dans le programme** : la `lignee_reconnue` d'une entrée de veto recopie celle de la même carte (rien ne le contrôle, l. 532-534) ; le lecteur ne compose pas son veto d'après la lignée qu'il croit reconnaître (les critères disent seulement « désigne sans voir l'espèce », § 8). Elles vont dans le sens de la lettre ; elles ne sont pas la lettre.
5. **Ce que la mère doit fournir au lancement, et que la consigne laisse en blanc** : le chemin et l'empreinte du fichier des cartes masquées ; le nombre de cartes attendues (94 si la liste hors du choix est vide ; table du manifeste, réserve 1) ; le nom du fichier de lecture. Les étiquettes `prop-…` sont celles que les réponses sur les familles disent avoir lues dans la configuration de la course v9 (lignes 323 à 354) : je ne l'ai pas rouverte. **Si le manifeste scellé porte d'autres clés dans `familles`, les § 3.1 et § 4 de la consigne sont à refaire avant toute lecture.**

À savoir aussi, sans que ce soit à moi d'en décider : l'amorçage que la décision 3 (b) accepte (note v7, § 9) reste entier. La consigne demande d'écrire la lignée avant de noter et de ne pas y revenir ; elle ne peut pas empêcher qu'elle pèse.

## 5. Gestes, incidents, écarts

- Commandes : une vérification du compagnon du mandat ; un `git fetch origin main` ; trois `git show` redirigés vers mon dossier (critères, note, `go.md`) ; des `sha256sum` sur des fichiers nommés ; un `git rev-parse origin/main` ; un `date -u` ; la création de mon dossier. Une commande simple par appel, aucune commande de liste, aucun joker.
- **Incident, sans refus** : une recherche de motifs trop large sur le seul fichier du programme a rendu une sortie que l'outil a rangée de lui-même sous `/root/.claude/`. Je n'ai pas ouvert ce fichier ; j'ai relu le programme par plages de lignes à la place.
- **Aucun refus** de permission, de classifieur ni de garde.
- La consigne n'a pas été contre-lue (règle R2) : elle l'attend, par un autre modèle.

*rédacteur neuf, modèle F*
