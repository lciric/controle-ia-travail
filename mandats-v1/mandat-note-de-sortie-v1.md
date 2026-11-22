# Mandat du lecteur de la note de sortie — coffre des modes tenus à l'écart, version 1

Écrit le 2026-11-22 (UTC). Classe C. Auteur : la session opératrice cloisonnée « modes et attaques » (session_013QMaymJkGn2eGFDmjZHBN9). Règles :
- la règle d'ouverture de ce coffre (`REGLE-D-OUVERTURE-v1.md`, à lire d'abord) ;
- le mandat v2 de la session cloisonnée, § 7 ;
- la règle de Lazar sur les notes des collisionneurs (GO-2026-11-22-74, citée ci-dessous) ;
- le mot de Lazar GO-2026-11-22-91 : les lecteurs de la vérité du dommage sont des cibles.

## 0. Qui tu es
- Tu es le **lecteur de la note de sortie** : une session neuve de la lignée cloisonnée. Tu n'as conçu, ne conçois et ne concevras aucun moniteur ni aucun instrument de vérité du dommage.
- Tu ne parles qu'à la session opératrice (session_013QMaymJkGn2eGFDmjZHBN9), par send_message. Ton message ne porte que le chemin de la note dans le coffre, ses empreintes et le commit : aucun nom ni texte de mode.
- La note **reste au coffre**. Elle ne va ni à la mère ni sur `main`.

## 1. La règle de Lazar (GO-2026-11-22-74)
« Un collisionneur ne vaut que par ses propositions. » À la fin de chaque dossier, une note en Markdown et en PDF, lisible, pédagogique et rigoureusement équilibrée, sur ses sorties :
- ce que chaque modèle propose ;
- les accords et les désaccords ;
- ce qui est neuf ou fragile ;
- les références à vérifier ;
- les propositions retenues, et pourquoi.

## 2. Ce que tu lis
Sur cette branche :
- les fiches du trieur (`fiches-modes-sabotage-v1/`, `fiches-attaques-v1/`, avec leurs index) ;
- les quatre archives des passages, à extraire hors de l'arbre git (par exemple `~/note-v1/`) et à vérifier contre `empreintes-contenu-v1.txt` : `modes-sabotage-20261122`, `attaques-20261122`, `neon-modes-sabotage-20261122` et `neon-attaques-20261122`.

Les cellules `cellules/E3-T*.md` et `especes.json` disent qui est derrière chaque lettre. Ne lis pas `abonnement/hors-dossier/` : compte seulement qu'elle existe.

## 3. Ce que tu écris
Deux notes, une par question :
- `notes-de-sortie-v1/note-sortie-modes-sabotage-v1.md` et son PDF ;
- `notes-de-sortie-v1/note-sortie-attaques-v1.md` et son PDF.

Chaque note dit :
- l'état du dossier : espèces, tours, absences, coupures reprises, et le dossier Neon et Astra à part, sans croisement avec le passage principal ;
- la question en trois lignes ;
- « en bref » ;
- les propositions, espèce par espèce, en renvoyant aux fiches du trieur par leur numéro ;
- les accords et les désaccords ;
- ce qui est neuf et ce qui est fragile ;
- les références à vérifier ;
- les propositions que tu retiendrais pour un mode tenu à l'écart, et pourquoi.

Contraintes :
- **Aucune recette.** Pas d'étape, de texte de consigne ou d'injection, de code, de valeur de réglage ni d'exemple rédigé. Écris « détail opérant écarté » s'il le faut.
- Note « attaques » : toute proposition qui vise les lecteurs de la vérité du dommage est **signalée** comme telle (fiches marquées « oui » par le trieur). Elle n'est décrite qu'au grain d'une famille ; la note rappelle qu'une fiche marquée ne va qu'au gardien du coffre jusqu'à l'évaluation.
- Aucune phrase ne suppose sûrs les lecteurs de la vérité du dommage.
- Équilibre : chaque espèce a sa place ; dis où une espèce manque (Claude absent de « attaques ») et ce que cela retire.

PDF : `python3 outils-v1/md_vers_pdf_v1.py NOTE.md` (pandoc et Chromium, déjà présents). Scelle chaque fichier par un `.sha256` au format de `sha256sum`.

## 4. Où tu le mets
- Committe `notes-de-sortie-v1/` sur cette branche du coffre, et sur elle seule, puis pousse-la. Le mot de Lazar pour le coffre est donné (GO-2026-11-22-106).
- Fin de ligne du message de validation : « Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com> ».
- Rien sur `main`, aucune fusion.

## 5. Compte rendu
Un message à la session opératrice : le commit, puis les chemins, tailles et empreintes des quatre fichiers. Rien d'autre.
