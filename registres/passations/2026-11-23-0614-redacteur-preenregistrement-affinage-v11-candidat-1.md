# Passation — rédacteur Opus du préenregistrement v11 de la course d'affinage : texte scellable (candidat 1), non scellé

- Écrite le 2026-11-23T06:14:50Z (`date -u +%FT%TZ`), sur la branche `prep/preenregistrement-affinage-v11-opus-v1`. Elle suit, sans les réécrire, les passations de 05:55, 06:01 et 06:04 (`registres/passations/2026-11-23-0604-redacteur-preenregistrement-affinage-v11-brouillon-8.md`, `e0339e4117a5dd19582863d35bcbf930f75ed645fe67d2b036bf481f0a16045e`), dont tout le reste vaut.
- Même rédacteur (Opus 5.5 en effort maximal, GO-2026-11-22-145). Aucun appel à un modèle externe, aucune dépense, aucune instance lancée.

## Fait

Commit `236731b52`, sous `docs/notes/organisme-affinage-mentors-v1/` :

| pièce | chemin | sha256 | état |
|---|---|---|---|
| **texte scellable du préenregistrement v11, candidat 1** (295 lignes) | `course-v11/preenregistrement-course-affinage-mentors-v11-candidat-1.md` | `8ce185b6c677f458c2d9770ca04bdc70bf3eefc3fdae8d6b9eeb7b740212f3f0` | **non scellé** (aucun compagnon), sur la consigne de la session de l'organisme : « ne le scelle pas avant mon feu » |
| programme d'assemblage du candidat 1 | `course-v11/assembler-preenregistrement-v11-candidat-1.py` | `1d8a72c1cbdb547225e32a242a1a3a93c29ec3395e48c26af48ebd488695d50d` | scellé (outil) |

Rejeu, à l'octet près : `python3 -I course-v11/assembler-preenregistrement-v11-candidat-1.py course-v11/preenregistrement-course-affinage-mentors-v11-brouillon-8.md <sortie> 2026-11-23T06:14:16Z`.

Ce qu'est le candidat 1 : le brouillon 8 sans sa ligne d'état ni sa dernière section ; ses quatorze emplacements remplis des empreintes des pièces du lanceur v11d (branche `prep/lanceur-affinage-v11c-interrompu-v1`, commit `708549da5`), chacune vérifiée à son compagnon et au message de la session de l'organisme ; lanceur de la course nommé v11e (`scripts/lancer_course_affinage_mentors_v11e.py`), le v11d à deux lignes près (VERSION et `PREREG_SHA256`, vide dans le v11d, posée à l'empreinte de ce texte), forme retenue par la session de l'organisme (message daté 06:12Z, étage 1) ; commande `GO_ID=GO-2026-11-22-80 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v11e.py` ; limite de l'essai à blanc écrite (essai de bout en bout sur un dépôt d'essai, avec un faux orchestrateur ; essai réel `--a-blanc` sur la machine de départ, avec l'orchestrateur épinglé).

Contrôles : 17 sections identiques à la v10, 9 changées, une neuve (différentiel v10 → v11) ; aucun emplacement restant ; les douze empreintes de pièces présentes ; commande v11e quatre fois, aucune commande v11d ; seul nombre neuf, 330 (essais réussis du v11d, rapport v11d, § 3) ; renvois « devis v11, § n » retrouvés dans le devis v11f. Faits vérifiés pour l'écrire : `PREREG_SHA256 = ""` dans le v11d (l. 477) et refus nommé (l. 979) ; le lanceur relit sa propre empreinte et exige que la contre-lecture la cite (l. 1019, 2591) ; la configuration v11d diffère de la v11c par les notes `changements_v11.carbon` et `.argon` (commande en flux v2), le retrait de `relais_persistants_v4.plafond_relais_claude_usd` et une note `note_v11d` ; le lanceur v10 épinglait l'empreinte de son texte (`7fc71712…`).

## Échanges avec la session de l'organisme

- Reçu à 06:07Z (« 06:52Z ») : empreintes v11d ; « écris le texte scellable, mais ne le scelle pas avant mon feu » ; limite de l'essai à blanc à écrire.
- Envoyé à 06:09Z : le v11d ne peut pas partir tel quel (épingle vide) ; proposition du v11e, le v11d à deux lignes près (confiance 0,8).
- Reçu à 06:10Z (« 06:12Z ») : v11e retenu (étage 1) ; « écris le texte scellable sous cette forme » ; après le scellement, le développeur produit le v11e et ses essais ; la contre-lecture vérifie la différence de deux lignes.
- Envoyé après la poussée de cette passation : chemin et empreinte du candidat 1 ; demande du feu explicite.

## Reste

- Au feu de la session de l'organisme : copier le candidat 1 à l'octet sous `course-v11/preenregistrement-course-affinage-mentors-v11.md` (empreinte inchangée, `8ce185b6…`), le sceller, committer, pousser. Puis, par d'autres : le v11e et ses essais (épingle `8ce185b6…`), les commandes exactes, la contre-lecture (Opus neuf, libellé « Opus 5.5, contre-lecteur neuf »), la mesure préalable d'Argon dès le scellement (R-5140), l'essai à blanc réel sur la machine de départ.
- Si le feu demande un changement du texte : un candidat 2, sous un nom neuf (R12).

## Réserves

- Le candidat 1 n'a pas de compagnon `.sha256` : sur la consigne de la session de l'organisme (pas de scellement avant son feu) ; son empreinte est donnée ici et au commit.
- Le texte nomme un lanceur v11e qui n'existe pas encore : sa forme (le v11d à deux lignes près) est fixée par le texte et retenue par la session de l'organisme ; la contre-lecture doit la vérifier.
- La vérification du lanceur v11d par le même contre-lecteur est en cours : son issue peut demander un lanceur suivant, donc un candidat suivant.
- Essais du dépôt : non relancés (aucun fichier de `src/` ni de `tests/` changé par cette session).

## Prochaine action

Sur le feu explicite de la session de l'organisme : sceller le texte sous son nom final (copie à l'octet du candidat 1). Sinon, rien.

## Instances actives

Aucune lancée par cette session ; aucune touchée. Dernier relevé en lecture seule à 06:00Z (passation de 06:01).
