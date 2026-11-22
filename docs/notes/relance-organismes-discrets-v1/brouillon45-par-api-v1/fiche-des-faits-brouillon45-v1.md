# Fiche des faits pour le brouillon 45 — état au 2026-11-22T13:20Z

Écrite par la session de relance du bras A, d'après ses pièces scellées. Toutes les empreintes sont des sha256 complètes ; recopie-les telles quelles, ou leurs huit premiers signes suivis de « … » comme le fait le brouillon 44.

## 1. Second lecteur : Mistral Large 4 (`mistral-large-4-0`), admis
- Vérification de la clé, point d'accès européen (ligne GO-2026-11-21-86), saine, 2026-11-21T21:31Z : dossier `runs/verification-cle-mistral-bras-a-v1/20261121-213114-verification-mistral-eu`.
- Essai d'admission (ligne GO-2026-11-21-83), joué de 21:32 à 21:54Z le 21 novembre : 24 lectures sur 24, 24 réponses de code 200, 24 de forme conforme ; rapport technique `runs/essais-admission-bras-a-v1/20261121-213224-file-mistral/rapport-technique.json` (74106c3e87f56c2208d3101c54d813116404e804bac49eb9cb7a2a3049a9b6ce).
- Règles d'admission appliquées : elles tiennent ; `docs/notes/relance-organismes-discrets-v1/essais-admission-bras-a-v1/application-des-regles-file-mistral-2026-11-21-v1.json` (985817789d195d75da32516e611fb74e36b24d7f684266bb010eec80b3f0218f).
- Configuration de la file : `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v7-mistral-2026-11-21-v4.json` (371d5b235d8108daeb3bd3c71d8d2d4757e08c7a23f53e3d508eaddbc98fc448).

## 2. Juge des deux ancres : `gemini-4-neon`, admis
- Vérification de la clé 1 (`GEMINI_API_KEY`, ligne GO-2026-11-22-60), saine, 2026-11-22T12:51 à 12:53Z ; de la clé 2 (`GEMINI_API_KEY_2`, ligne GO-2026-11-22-61), saine, 12:54 à 12:55Z ; nom servi `gemini-4-neon`, niveau de réflexion `XHIGH`, sonde de borne « comprise » sur chaque clé.
- Essai d'admission (ligne GO-2026-11-22-62), joué de 12:57:16 à 13:09:11Z le 22 novembre : 8 lectures sur 8, partagées par rang (4 par clé : rangs impairs sous `GEMINI_API_KEY`, rangs pairs sous `GEMINI_API_KEY_2`), 8 réponses de code 200, 8 de forme conforme, aucun défaut, aucun envoi coupé ; rapport technique `runs/essais-admission-bras-a-v1/20261122-125716-file-neon/rapport-technique.json` (7bb8cc956898661bf5be2c47c8c0fe508fed3614018a2c4aedf722f8145cabc8).
- Règles d'admission appliquées : elles tiennent, « le modèle est le juge des deux ancres » ; sortie facturée la plus haute observée 21 132 jetons, sortie maximale à la course 84 992 (règle 7) ; `…/essais-admission-bras-a-v1/application-des-regles-file-neon-2026-11-22-v1.json` (c593784bf1609778f560e81474cb69812ef1297bb210a433e8275827f0dc37f2).
- Configuration de la file : `…/essais-admission-bras-a-v1/configuration-essais-admission-bras-a-v12-google-2026-11-22-v4.json` (37a23ab2d69663e8af6db9c980a20c2de96d020ed464bad2bf1f7cf6b57812a7) ; programme `scripts/chef_essais_admission_bras_a_v12.py` (6aa04397997a52785ce4bd05e1b7a45c5886e1565f3e2927984b08373d9758b1), vérifié « engageable » (`docs/notes/relance-organismes-discrets-v1/verification-programme-essais-admission-livraison13-v1.md`, bd935fd880092660f4ec4cd2eca3312478b659e975d282bd0015bee67345d798).
- Fichier des règles : `…/essais-admission-bras-a-v1/regles-admission-bras-a-v1-brouillon44.md` (cd0e384c21516b95c0c01ba2275d79a034777c92aca257b5700052724cfb2865), qui cite les lignes 529 à 537 et l'empreinte du brouillon 44.
- Dépense comptée des trois lignes de Google : 1,21 USD.

## 3. Conditions d'envoi
- Pièce de constat de Mistral : `docs/notes/relance-organismes-discrets-v1/constat-comptes-mistral-bras-a-2026-11-21-v1.md` (4907d0924dfd7526bea1c25b51606bb3d0dca4c07e7509cbefd5e934ffef9536).
- Pièce de constat de Google : `docs/notes/relance-organismes-discrets-v1/constat-comptes-google-bras-a-2026-11-22-v1.md` (2234e0cb1210a4042f6edbbf5629ae8cddd563019ba148a047fb7ff676af4cf1) : mot du directeur inscrit à GO-2026-11-22-40, « la recharge automatique vient de s'activer pour 20 euros », et captures de facturation du 2026-11-21T16:24Z ; elle ne sert plus aucune ligne après le 2026-11-24T00:00Z (borne d'âge du fixage du change, 96 heures).
- Avenant 3 au devis, version 2 : `docs/notes/relance-organismes-discrets-v1/avenant-3-devis-essais-admission-seuils-de-credit-google-leves-v2.md` (4b331d9aed86b280ea720ac554911df168fe7564799957a29776a1cad4dbeaa0) : les seuils de crédit de Google sont levés (décision GO-2026-11-22-02, confirmée GO-2026-11-22-16) ; la recharge automatique couvre les lignes et n'est comptée dans aucun crédit ; un refus pour crédit épuisé est un défaut journalisé qui arrête la ligne.
- Exemption de la sonde de borne confirmée (GO-2026-11-22-03).

## 4. Côté habilité (chemin et empreinte seulement ; rien n'a été ouvert)
Relevé sur la branche du développeur habilité (tête 5e5c17d8d) :
- **Lanceur de l'étape de discrétion, version 2** : vérification habilitée, pièce sans interne `docs/notes/bras-a-moniteurs-v1/verification-habilitee-lanceur-discretion-v2-sans-interne-v1.md` (33efc50fc10c821627fb31bf51f9845bfdb1c577d202d5ae054da18e98872ae9), commit 5e5c17d8d, dont le message dit « corrections faites (C9 avec réserve) » ; la réserve n'est pas lue ici et reste à porter par le lecteur habilité. Le lanceur v2 lui-même est au commit 848c17649.
- **Contre-lecture du module des autres moniteurs, version 11 : n'existe pas** sur cette branche. Seule existe la vérification habilitée de la version 10, déjà citée au brouillon 44.
- **Confrontation de `mistral-large-4-0` et `gemini-4-neon` à la liste des familles des moniteurs : n'existe pas.**

## 5. Calendrier (décision du directeur, GO-2026-11-22-57)
Plan d'analyse scellé le 23 novembre ; gel le 29. Ce brouillon ne fixe aucun calendrier dans une règle ; il peut le dire au statut.
