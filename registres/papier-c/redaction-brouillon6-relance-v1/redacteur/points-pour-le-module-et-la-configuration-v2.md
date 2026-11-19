# Papier C — ce qui change pour le module et la configuration entre la version r1 et la version r2 — v2

Pour l'auteur du module (verrou 3) et de la configuration (verrou 4). Écrit par le rédacteur du préenregistrement
(Claude Fable 5.2), le 2026-11-19. La fiche v1 (`1505819ae0b3532f91e20d50f58d3e77ecb21860d189bdd5d022187b00c738bb`)
reste valable pour tout ce qui n'est pas dit ici. Texte de référence : version r2,
`papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r2.md`
(`1ab62e7d22163306a3251cd75f4001f7daac63ea72577d5ee200a3bcf86cfec3`). « Précision n » = Plan d'analyse, section 8.
Le texte fait foi : cette fiche est un index. Aucun code ici. Je n'ai ouvert ni le code du module, ni le harnais,
ni aucune consigne privée : là où je dis « lecture codée », c'est d'après `points-ouverts-module-v1.md`.

## 1. Là où le texte s'écarte de la lecture codée (à reprendre dans le module)

| Point | Lecture codée (d'après le relevé) | Ce que r2 écrit | Lieu |
|---|---|---|---|
| PO-01 | garde sur l'arbre au commit 7a54d43 | plus de commit : une ligne « Dépendance du papier C » par fichier de `src/controle_ia/` importé (fermeture des imports), calculée par programme au scellement ; arrêt si une empreinte diffère, si une ligne manque, ou si un fichier du module ou de l'adaptateur est sous `src/` ou `tests/` | liste d'arrêt 1 ; champs du scellement |
| PO-02 | identifiant d'accord accepté tel quel | règles de la garde de calcul du dépôt : ligne de type « calcul », donnée par Lazar, dans sa période, non révoquée ; identifiant nommé ou reçu par `GO_ID` selon D-18 (en attente) | Plan, section 1 ; liste d'arrêt 2 |
| PO-08 | tirages non finis écartés | écartés des quantiles et comptés ; dans une valeur p, comptés au numérateur (contre la conclusion testée) | précision 5 |
| PO-09 | témoin lexical : message système seul | transcription rebâtie par le harnais sous la condition honnête : la fin du message système et l'indication privée de chaque tour de l'utilisateur sont remplacées par leur pendant honnête ; scores sur les seuls jetons des tours de l'agent ; la fonction appelle le harnais, ne recopie aucun texte ; à éprouver sur un cas sain et sur un artefact | Métrique, point 14 ; liste d'arrêt 20 ; verrou 9 |
| PO-15 | borne par repère propre au module | règle de forme : après la clé du dernier champ présent, le paragraphe commence à la première ligne non vide qui suit une ligne vide ; même règle pour toutes les cellules ; champ de coût jusqu'à la clé suivante, la borne ou la fin | précision 9 |
| PO-22 | identifiabilité sur la loi calibrée | sur la loi nette calibrée **et** sur la loi nette sans calibrage ; Holm sur toutes les familles positives du juge | précision 14 |
| PO-26 | « non testable » remplace l'issue | interdit la confirmation (« non concluante », avec la mention) ; une réfutation reste une réfutation, avec la mention ; issue brute écrite à côté | précision 18 |
| PO-33 | recherche du texte entier | chaque ligne non vide d'au moins 40 caractères de chaque contenu, de chaque item et du gabarit | précision 27 |
| PO-34 | — | trois contrôles par programme : aucun champ de score dans un objet passé à la génération ; tous les épisodes d'une tâche générés avant toute lecture par un juge ; fichier des scores en ligne jamais ouvert en lecture par la génération | précision 26 |
| PO-36 | clé `conception` réemployée | clé neuve `papier-C/pilote/banc` ; `papier-C/pilote/lisibilite` réservée, ne tire rien ; `papier-C/pilote/raisonne` tire les 10 contenus | précision 32 ; Plan, section 4 |
| PO-37 | simulations lues dans l'archive | simulations S5 et S6 versées sous `docs/notes/contre-lectures-papier-C-v1/simulations-methode/` ; 1 000 tirages par essai ; issue du test de l'intervalle BCa écrite dans un fichier scellé | précision 33 |
| PO-41 | D₀ de la sonde lectrice sur les jetons de l'agent | sur la passe du juge Llama, borne de la précision 9 appliquée au contenu lu | précision 22 |
| PO-42 | `derivation.py` | `derivation_v1.py` | Plan, section 2 |
| PO-45 | certaines lignes calculées hors du module | toute ligne nommée au texte est calculée et écrite par le module scellé (liste à la précision 36) | précision 36 ; verrou 3 |

## 2. Lectures codées confirmées, écrites au texte

PO-03 (précision 1), PO-04 (2 : écart type de population sur toutes les paires — à vérifier contre le diviseur
codé), PO-05 (3), PO-07 (4), PO-10 (6), PO-12 (7), PO-13 (8), PO-16 (10), PO-18 (11), PO-20 (12), PO-21 (13),
PO-23 (15), PO-24 (16), PO-25 (17), PO-27 (19), PO-28 (28), PO-29 (29), PO-30 (30), PO-31 (31), PO-39 (20),
PO-40 (21), PO-44 (23), PO-46 (24), PO-06 (25). L'auteur du module compare chaque précision à son code, ligne par
ligne : je n'ai pas lu le code, et « confirmée » veut dire « conforme au relevé », pas « vérifiée ».

## 3. Configuration

- Champs remplis au scellement : aux cinq de r1 s'ajoutent `stabilite_rang.version` et le champ du rapport de la
  grille (D-9) ; le script de différences les admet, aucun autre.
- Bras « contrôlabilité » : selon D-19 (en attente). Version (a) : six champs vides au scellement, fixés par un
  addendum ; version (b) : tous remplis avant le scellement ; version (c) : parties (b1) et (b2) retirées. Ne rien
  coder de définitif avant la décision.
- Clé de graine neuve : `papier-C/pilote/banc`.
- Paragraphes de plaidoyer des niveaux 1 et 3 : à contre-lire (verrou 4) ; gardes lexicales selon la précision 31.
- Consignes : la branche « dicte l'ampleur » de la garde 9 se contrôle à la contre-lecture de la configuration ; à
  l'exécution, égalité octet pour octet avec la consigne contre-lue (précision 25).

## 4. Marqueurs et lignes du scellement

- Marqueur neuf : `<<LIGNES_DEPENDANCES_PAPIER_C>>`. `<<EMPREINTE_MESURES_V2>>` est rempli.
- Adaptateur réel : hors des lignes « Module du papier C » ; lignes « Lanceur du papier C » d'un addendum de
  lancement, avant le pilote (D-20, défaut sous 48 heures). Il ne porte aucune fonction de calcul d'une ligne.

## 5. Ce qui reste à écrire dans le module avant le scellement (verrou 3)

Mise à jour sur r2 ; lignes rapportées de la précision 36 ; addendum de dérivation en fichiers (`.md` et `.json`) ;
fonction de reconstruction du témoin lexical ; contrôle du format des fichiers du banc par un agent qui peut ouvrir
`donnees/` ; examen du taux de 0,0000 (trop propre, R4) ; mesure du taux de déclenchement de la réserve « loi
portée par le contraste d'intention » sous le nul (verrou 11, clause de la précision 34). Avant l'étape 2 : banc
de contrôlabilité (verrou 12), grandeurs du verdict de G0 dont la procédure du plancher (verrou 13, précision 35).

## 6. Non vérifié par moi

Le comportement du lecteur de champs sur un dernier champ de plusieurs lignes (précision 9) ; le diviseur codé de
σ̂ ; que le harnais permet bien de rebâtir une transcription sous une autre condition (dit par l'auteur du module).
