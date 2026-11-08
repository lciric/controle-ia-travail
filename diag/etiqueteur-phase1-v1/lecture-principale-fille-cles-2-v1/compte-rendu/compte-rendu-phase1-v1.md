# Compte rendu de la phase 1 de l'épreuve de l'étiqueteur — exécutante : la session mère (R-1756)

Ordre : docs/procedures/ordre-execution-phase1-epreuve-etiqueteur-v1.md (30f265a9a1c49a6af734c71a69cdc444989f9ec1c6e294525f43035a28705f18).

## Sections 1 et 2 (8 novembre 2026, 05:50:18Z à 05:52:34Z, date -u)
- 1.1 : variables-v1.sh 90b6bee859044fd9edbb7351c4efa61a3c11eae0898576525c4023136b7bb976.
- 1.2 : « commit du code conforme », « arbre propre ».
- 1.3 : douze « OK », code sha256sum=0 ; GO-2026-11-07-07 : 1 ligne ; entropie 17812956677980471985 ; python 3.13.18, numpy 2.4.6.
- 1.4 : 24, 6, 79, 12 passés, codes 0.
- 1.5 : GEMINI_API_KEY_2 présente, KIMI_API_KEY présente (par le nom seulement).
- 1.6 : port 8789 libre.
- 2.1 à 2.3 : codes 0 ; 2.4 : 396, 396, 20, 20, 80, 60 lignes ; « comptes conformes » ; entropie, commit 64e67cbd…, empreinte du script ceeef529… conformes ; empreintes-generation-v1.txt 73f5f61abeb29d5b62ed73a4abcada2ced3b948e7d00f7e9e6b8a9038cb8b914.
- CO-10 : 1.3 et 1.4 refaits (conformes) ; empreintes de 2.4 recalculées dans empreintes-generation-verification-v1.txt (fichier neuf, R12) : identiques.

## 2.5 — Feu vert de dépôt (session mère, 2026-11-08T05:55:04Z)
- Dépôt chez le tiers : projet privé dr57c de l'Open Science Framework, fichier depot-epreuve-etiqueteur-phase1-v1.json, date de dépôt rendue par l'interface **2026-11-08T05:54:40.935302Z**, empreinte relue ab240b401de2f9a6edb69dfc14ac9dfdc828f50542dc8a543f5473d13ce8707a (conforme), identifiant 6af00ea0066c9d972ba9da79. Copie scellée : livrables/osf-depot-epreuve-etiqueteur-phase1-v1/ (commit 3b39d1e75).
- Empreintes déposées : texte scellé f73455b8… ; extrait des seuils et critères des deux phases 2f146f94… ; ordre 30f265a9… ; items 8efc13d3…, clé 191e5001…, items de formation 14d887a2…, clé de formation cf528ffa…, manifeste de génération e39ea53b…, relectures 5ed697c8…, tirage de la phase 2 07e359ba… — égales à empreintes-generation-v1.txt (vérifié par programme à la construction du dépôt).
- CO-07 (a) : prix public d'Argon relevé à 05:46:11Z (copie docs/sources/prix/page-prix-gemini-api-20261108T054611Z.html, ad2140dd…) : 2,00 USD par million d'entrée, 10,00 USD par million de sortie pensée comprise, jusqu'au 30 novembre 2026 ; sous 10 et 50 : pas d'arrêt.
- CO-07 (b) : GEMINI_API_KEY_2 ne sert à rien d'autre (mot du directeur, R-1754) ; KIMI_API_KEY : aucun autre appel engagé par la session mère ni par ses filles pendant la fenêtre de l'essai de format (aucun ordre en cours qui l'emploie).
- Feu vert de dépôt donné : l'essai de format (section 3) peut partir.

## Section 3 — essai de format (05:55:13Z à 06:05:34Z)
- 3.1 : relais 4488 ; état avant conforme (relais-kimi-v4, Kimi seul, plafond 300, réserve 0,4, 100 appels, 0 appel, prix 2 / 10 / 2, recherche inactive, variable de clé absente de son environnement, numéro conforme).
- 3.2 : lecture 4539, lancée détachée 05:55:23Z ; deux guets ; code de fin **0**.
- 3.4 : état du relais après : 20 appels, depense_usd 0,379924, 0 refus, 0 écart de modèle servi, 0 usage absent, 0 délai dépassé, réponses 200 : 20 ; relais 4488 arrêté (vérifié). Manifeste : code 0, aucun arrêt ; comptes A ok 20, B ok 20 (0 illisible, 0 arrêt) ; **feu_vert True**, motifs [] ; extrapolation 34,8598 USD ; plafond restant 298,8351 ; **depense_estimee_dollars 1.164904** ; tentatives interrompues 0 ; empreinte des réglages 303edae8… ; commit 64e67cbd… ; manifeste 3a3d868ebc15e995040c9c70807e801589bd02dda4bf7725865c1e22580222a2 ; empreintes au fichier empreintes-lecture-format-v1.txt.

## 3 bis — facture attendue (journal, nombres seulement)
- A, gemini-4-argon, appel direct, GEMINI_API_KEY_2 : 20 tentatives ; jetons d'entrée 60 883 ; jetons de sortie 3 523 (pensée comprise, dont pensée 1 723) ; coût estimé au barème scellé 0,78498 USD ; modèle servi différent : 0 ; fenêtre 05:55:23Z → 06:03:13Z.
- B, kimi-k3.1-pro, par le relais, KIMI_API_KEY : 20 tentatives ; jetons d'entrée 62 132 ; jetons de sortie 25 566 (raisonnement compris, dont 23 455) ; coût estimé 0,379924 USD (relais : 20 appels, 0,379924 USD) ; modèle servi différent : 0 ; fenêtre 05:55:23Z → 06:05:07Z.
- Comparaison par le directeur sur les consoles de facturation (Google, Moonshot), écrite ici par la session mère. (2026-11-08T06:05:55Z)

## 4.1 — Feu vert de la lecture principale (session mère, 2026-11-08T06:09:35Z)
- « feu vert de la lecture principale ».
- Empreinte de lecture-format/manifeste-lecture-phase1-v4.json : 3a3d868ebc15e995040c9c70807e801589bd02dda4bf7725865c1e22580222a2 (égale à celle de empreintes-lecture-format-v1.txt).
- depense_estimee_dollars de ce manifeste : 1.164904.
- Contrôle de la facture : **non fait, levé par le directeur** (GO-2026-11-08-03, verbatim « pas la peine on avance ») ; écart au texte scellé (point 6) consigné ; feu vert du script : True, motifs aucun.

## Passation (2026-11-08T06:10:57Z)
- 4.2 joué une fois (relais 7210, plafond 298,83, 2 280 appels, état avant conforme), puis **arrêté par son numéro sans aucun appel** (0 appel, 0 USD) : passation demandée par le directeur vers une nouvelle instance ; la lecture principale (4.3) n'a **jamais** été lancée ici. États du relais annulé copiés : relais-principale-annule-etat-avant-v1.json, relais-principale-annule-etat-apres-v1.json. Le dossier relais-principale n'est pas transmis : la nouvelle instance refait 4.2 dans un dossier neuf.

## Exécution par la fille clés 2 (session `session_016QhUrreBYxC9arQKTBEHAb`, 2026-11-08, heures par `date -u`)
- **Clés** (par le nom, 09:47:59Z) : GEMINI_API_KEY_2, KIMI_API_KEY, VAST_API_KEY, OSF_TOKEN, HF_TOKEN, CONTROLE_IA_GITHUB_TOKEN_2, GEMINI_API_KEY : présentes. Aucune valeur lue ni affichée.
- **Restauration** (09:52Z) : archive `201e1295…` OK ; `variables-v1.sh` `90b6bee8…` conforme ; arbre du code au commit `64e67cbd…`, conforme ; génération 7 « OK » ; essai de format 15 « OK » sur 16 (manque connu `relais-format/console-relais-kimi-v1.log`, R-1765) ; manifeste de l'essai `3a3d868e…` conforme.
- **Blocs 3, 5 et 6** : conformes (douze « OK », code 0 ; GO 1 ; entropie 17812956677980471985 ; deux « présente » ; port 8789 libre).
- **Bloc 4, écart** : `test_lire_items_phase1_v4` 1 échec, 78 passés (attendu 79). Essai `test_B5_cle_refusee_arrete_tous_les_appels`, assertion `(10 - 6) <= 2`, console `700f49cc…`. Arrêt, compte rendu court 01 (`3363ac34`). **Écart accepté et déclaré par la session mère, R-1776** (commit `465fb2a9…`). Diagnostic de la mère : 4 passages sur 5 du fichier à 79 passés ; B5 seul : 1 échec sur 40 tel quel, 0 sur 40 avec une latence simulée de 20 ms ; course entre l'écriture au journal et la pose de `arret_general` (l. 517-521 et 485) avec un fournisseur simulé sans latence ; garde de dépense non en cause. Essai non rejoué ici.
- **Feu vert 4.1** comparé aux fichiers restaurés : texte, empreinte `3a3d868e…` (= `empreintes-lecture-format-v1.txt`), `depense_estimee_dollars` 1.164904, `controle_format.feu_vert` True, `motifs` [] : identiques.
- **Mot du directeur dans la session exécutante** : « go feu vert » (vers 10:07Z), puis « go lecture principale de l’étiqueteur sous GO-2026-11-07-07 et GO-2026-11-08-03 ».
- **4.2, relais** (10:07:47Z) : dépense de l'essai 1.164904, plafond du relais 298.83 ; **relais lancé, numéro 248** ; état avant conforme (relais-kimi-v4, modèles permis [kimi-k3.1-pro], plafond_usd 298.83, réserve 0.4, max_appels 2280, appels 0, depense_usd 0.0, `variable_cle_encore_presente` False, numéro conforme).
- **4.3, lecture** : départ 10:07:58Z, **numéro 340**, un fil par lecteur.
- **4.4, surveillance** : 19 passages du guet et de `bloc-4-4`, tous « lecture en cours » jusqu'à la fin ; comptes rendus courts 02 à 06 sur `rapports/fille-cles-2-v1`. Lecteur A : premier « illisible » à 12:18Z (tentative 234) ; **lecture `principale` de A finie avec 7 « illisible » sur 396 (1,77 %), sous le seuil d'arrêt de 8** ; B : 0. Une sentinelle à 60 secondes (seuil 8, arrêt par numéro), testée sur un cas sain et un artefact (R5), a tourné de 13:05Z à 14:40:16Z sans se déclencher (`rapports/fille-cles-2-v1/sentinelle-illisibles-v1.sh`). Aucun arrêt de la section 4.4 atteint.
- **Enquête sur le format** demandée par la session mère (R-1809, R-1811 ; codes et longueurs seulement, aucun contenu ouvert, aucun appel) : les illisibles de A sont tous `sorte` « erreur », `fin_fournisseur` « AUCUN_CANDIDAT », motif « erreur : aucun candidat (OTHER) », soit `promptFeedback.blockReason` = OTHER (réponse 200, aucun candidat, pas de `promptTokenCount`) ; `jetons_entree` au journal = `ceil(len(consigne)/3)` (estimation prudente) ; `cout_estime` = `cout_reserve`, la réservation au pire cas (l. 505, 375-377), non facturée par le fournisseur ; B lit les mêmes items « ok » ; longueurs des consignes de rang 24 à 45 sur 341, pas les plus longues.
- **Fin** : code de fin 0 (14:40Z). Guet : « lecture finie, code 0 ». Console de lecture `0db81d2e…` (277 octets).
- **4.5** (14:40:32Z) : relais après : 463 appels, depense_usd 12.925556, engage 0.0, restant 285.904444, refus 0, refus_modele 0, ecarts_modele_servi 0, **usages_absents 7**, delais_depasses 0, appels_au_dessus_de_la_reserve 0, réponses par statut 200 : 456, 429 : 4, 502 : 3 ; **relais 248 arrêté**. Manifeste : code 0, arret None, lecteurs_arretes {} ; comptes A : ok 448, illisible 8 (7 principale + 1 relecture), arret 0, non_appele 0 ; B : ok 456, illisible 0 ; **depense_estimee_dollars 41.08914** (dépense de l'essai comprise), reserve_restante 0.0, tentatives interrompues 0 ; empreinte_reglages `303edae8…` ; relais_max_appels 2280 ; commit `64e67cbd…`. Empreintes : `empreintes-lecture-principale-v1.txt`.
- **Bloc 21** (14:40:34Z) : `reponses-phase1-A-v4.jsonl` `5d0e8296d1b9410d7771e5839188430273f0813fd4701c52699732bba3b99e2e` et `reponses-phase1-B-v4.jsonl` `b03fccb51b37d088080bda4fefc5cf860aef85c95ebe03595dc05a256454237a`, égales au manifeste ; A et B différentes ; A et B : principale 396, relecture 60, 0 ligne d'un autre lecteur : conforme (couple CO-16).
- **Processus** : lancés 248 (relais) et 340 (lecture) ; 340 fini de lui-même (code 0) ; 248 arrêté par son numéro ; les deux vérifiés morts (`kill -0`). Aucun autre processus laissé.
- **Dépense estimée** : 41.08914 USD au barème scellé, dont 1.164904 pour l'essai de format ; part de Kimi mesurée au relais 12.925556 ; les 8 illisibles de A comptent environ 7,04 USD de réservation au pire cas.
- **Écarts** : (1) bloc 4, R-1776 ; (2) la sentinelle s'est ajoutée au guet, sans toucher la lecture ; (3) aucune réponse, aucun item, aucune clé ouverts, sauf ce qui précède (champs chiffrés et codes des journaux, longueurs des consignes reconstruites, champs `statut`, `lecture`, `lecteur`, `motif`).
- L'analyse (section 5) n'est pas lancée : la mère la confie à un lecteur neuf.
