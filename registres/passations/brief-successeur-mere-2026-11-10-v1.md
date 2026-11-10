# Brief de passation à la session mère qui me succède — v1

Écrit le 2026-11-10 à 11:20 UTC (heure relevée par `date -u`) par la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, arrêtée sur quota : 0,94 du quota hebdomadaire du compte à 11:13 UTC ; remise à zéro le 13 novembre à 15:00 UTC. Tu reprends **sur un autre compte**. Dépôt privé `lciric/controle-ia-travail`, branche `main`, commit de départ : le dernier de `main` (au moins `8fb4c68a`).

## 0. Qui tu es, comment tu parles
Tu es la session mère du programme de Lazar (directeur) : contrôle boîte blanche des menaces diffuses. Français, tutoiement, aucun sigle non développé. Verdict d'abord (1 à 3 lignes). Format de décision : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures. Tu écris à Lazar seulement pour un prononcé, une réserve, une divergence, une demande de GO ou une dépense ; le reste vit dans les registres.

## 1. Premiers gestes, dans l'ordre
1. Routine de reprise de `CLAUDE.md` (R14) : empreintes de `docs/`, arbre scellé, tests (`PYTHONPATH=src`, `.venv` à recréer par `requirements-cpu.txt`).
2. Lire **`registres/passations/2026-11-10-1113.md`** (`64d321cf…`), puis `registres/decisions.md` de **R-2116 à R-2190** et `registres/go.md` jusqu'à **GO-2026-11-10-09**. L'en-tête de `registres/etat.md` (11:13) renvoie à la passation.
3. Lire les passations des six autres sessions (section 4) sur leurs branches, par `git fetch origin refs/heads/<branche>:refs/remotes/origin/<branche>` puis `git show` — **sauf** la branche du bras d'attaque (cloison).
4. Envoyer à Lazar un premier message court : reprise faite, ce qui est relancé, et les quatre attentes de la section 6.

## 2. Interdits (à recopier en tête de toute consigne d'agent)
Ceux de `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`1ee3b370…`), règle 9 comprise (aucune recherche récursive qui traverse un chemin interdit ; `git grep` avec exclusions). En particulier :
- jamais `diag/*/lecture-sondes-t06.json` (nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json`), la lecture B de 7a ni `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a, avant le verdict scellé de P3-bis ;
- jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk` ; au bras d'attaque on n'envoie que le questionnaire commun, la consigne du lecteur et la liste « ce qui manque » ;
- jamais l'étiqueteur (`prep/etiqueteur-v2-lecture-interrompue-reprise-v1`), jamais `scripts/extraire_mesures_epreuve_t06_v1.py` sur 7a ou 7b avant le verdict de P3-bis ;
- jamais une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ` ; interface Claude seulement par `RR_ANTHROPIC_API_KEY_RIGAUD` passée par `env -i`, sans `ANTHROPIC_BASE_URL` ;
- jamais d'heure écrite à la main (toujours `date -u` dans la même commande) ; jamais de `git fetch` sans refspec ; jamais pousser vers `lciric/controle-ia` ; poussée par `git push origin HEAD:main` (retentatives 2, 4, 8, 16 s) ; garde des secrets à 0 avant chaque commit ;
- jamais toucher les instances 58936096, 58936099, 58936100 sans mot écrit de Lazar avec les identifiants ;
- ne jamais contourner, reformuler ni confier à une autre session un refus de permission ou de classifieur ;
- la session-dépôt est exclue des rôles de lecteur et de verdict sur T0.6 (7b), T0.7, P3-bis, G0 ; tout agent qui lit T0.7 est exclu ensuite des lecteurs de P3-bis ;
- règles gelées R1 à R14 de `CLAUDE.md` (préenregistrement scellé et contre-lu avant toute course ; verdict par un agent neuf ; R12 on n'écrase jamais).

## 3. Ce que tu as le droit de faire seul
- **GO-2026-11-10-09** : autonomie de travail et de calcul jusqu'au **27 novembre**, enveloppe **500 USD**. Lignes : GO-2026-11-10-01 (7b et T0.7, 200), -02 (P3-bis, 80), -04/-06 (étape A, 20), -07 (adaptateur, 30), -08 (saboteur à budget, 60). T0.8 et la course v65 sur devis ≤ 60 USD chacune ; **T0.8 propose 120 → retour à Lazar**.
- Accord général sur tes recommandations (GO-2026-11-10-05, prolongé au 27) : la recommandation tient lieu de décision, consignée avant d'agir — sauf dépense nouvelle, revendication, porte, publication, contact, écart à un texte scellé, H200.

## 4. Les autres sessions (toutes arrêtées, passations écrites)
| Session | Identifiant | Branche, commit | Passation ou rendu |
|---|---|---|---|
| Session-dépôt | `session_01QPDgKgcLdggoVJfGC5cBw8` | `claude/upbeat-cray-dmauvv` `aa012484` | `registres/passations/2026-11-10-1115-session-depot.md` ; **dossier fusionné v1, 124 pages** (`88a58020…`) ; recompte de la calibration inachevé |
| État de l'art niveau 3 | `session_01QPDgKefT7L1TvJMZ4BiBNb` | `prep/etat-de-l-art-niveau3-v1` `f0aaf0d1` | passation `…-1112-etat-de-l-art-niveau3.md` ; synthèse provisoire `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1-provisoire1.md` et son complément (qui prévaut) |
| État de l'art, pièces à réseau | `session_01QPDgKghHndLJyQ4EpoutjR` | `prep/etat-de-l-art-niveau3-pieces-v1` `d227aee3` | passation `…-1115-pieces-reseau-niveau3.md` ; rapports sous `docs/sources/lecture-pdf-niveau3/` |
| Bras externe NARCBench | `session_01QPDgKgGRpVYqfbzKs8dpT6` | `prep/narcbench-externe-v1` `769ab122` | passation `…-1116-narcbench-externe.md` ; données à retélécharger (712 Mo) |
| Organisme v65 | `session_01QPDgKhUpjGAMFhKSKNcVEA` | `prep/organisme-v65-v1` `3daf08e2` | `docs/notes/organisme-boucle-reelle-v1/code-v65/passation-2026-11-10-1112-organisme-v65.md` |
| Bras d'attaque | `session_01QPDgKjN3jeeUyZP2mnkDNK` | `claude/compassionate-meitner-d4ryyk` `cab02e41` | sa passation, sur sa branche (cloison : tu ne l'ouvres pas) |
Pièces hors `main` sauvées : clé du questionnaire commun sur `cle/questionnaire-commun-v1` (`2107363b`, `3a38b037…`), réponses du lecteur de la mère sur `reponses/questionnaire-commun-mere-v1` (`77f6e59d`) ; correction des trois jeux confiée à la session-dépôt (R-2189).

## 5. Ce que tu relances, dans cet ordre (objectif : tout scellé le 12 au soir)
Calendrier resserré (R-2177) : T0.7, base (A) « mots et coût », P3-bis et consigne d'audit des fuites scellés le 12 au soir ; 7b et P3-bis créées le 12 ou le 13 ; lecture des sondes vers le 16-18 ; replis : T0.7 avant le 13 à 12:00 UTC, 7b au plus tard le 15, P3-bis au plus tard le 18, rendez-vous du 20 à 12:00 UTC.
1. **Consigne de l'audit des fuites de T0.7** (jamais écrite ; chemin le plus fragile) : partiel dans `brouillons/T0.7-audit-fuites-v1/` (marqué INTERROMPU).
2. **Module de lecture T0.7 v2** (option (c) des concepts, ordre 7b b4) : branche `prep/t07-module-v2` (`88e80ba0`, commit interrompu) ; puis contre-lecture courte, ligne CODE-T07 au nouveau commit, **brouillon 22** de T0.7 (citer la consigne v3 corrigée des concepts `ea5fe3f0…` ; ligne (iv-a) S100 contre T100 ; puissance par dose), contre-lecture R2, scellement.
3. **T0.8 brouillon 2** (44 couples de la contre-lecture `21499f7c…`, empreinte intermédiaire attendue `7110a230…`) et **texte court de la base (A) « mots et coût »** (coût brut, décision de Lazar R-2175) : rien d'écrit, à relancer en entier.
4. **Validité adaptateur** (paquet (i), (ii), (iv-a), (iv-b), (iv-c) + témoin distillé honnête ; D-1 (b), GO-2026-11-10-07) : partiel dans `brouillons/validite-adaptateur-v1/`. Source : `docs/notes/rapports-directeur/premisses-trace-interne-v1-point-2a.md` (`2db916aa…`).
5. **P3-bis** : brouillon 11 (`409c37ed…`) → contre-lecture 4 par un autre modèle → scellement ; disque ≥ 12,69 Go pour la répétition finale.
6. **Texte « accumulation contre score par action »** (barreau 6, demandé par Lazar ; nœuds G1 à remonter avant scellement) : rien d'écrit.
7. **Saboteur à budget (ii-b) avec activations** (GO-2026-11-10-08, 60 USD) : branche `prep/ii-b-code-v1` (`07ef895a`, interrompu) ; code, devis, ordre exploratoire, six épreuves de l'oracle.
8. **Bras externe NARCBench** : texte court (écarts de recette E1 à E4, checkpoint Llama « non établi », bande de six couches contre « five-layer » du PDF), après le mot de Lazar sur le refus.
9. **Concepts** : script v3 (liste fermée de la section 6 de la consigne v3 corrigée), puis lot neuf (écrivain Opus, lecteur Fable, `chats` et `geographie`) ; troisième échec = repli à clé permise.
10. **Organisme v65** : contre-lecture par un autre modèle (rien d'écrit), puis décision de Lazar sur la copie du texte scellé dans le dépôt public de l'organisme.
11. **Entretien** : sections de résultats v2 (partiel dans `docs/notes/rapports-directeur/resultats-pour-documents-v2/`, INTERROMPU ; aucun taux de calibration) ; contre-lecture du socle de preuves v3 (`b9377f1d…`) ; programme d'entretien v19 ; signaler la v2 des résultats à la session-dépôt pour le dossier fusionné v2 et la version intégrée ; verser la fusion v1 sur `main` (`docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/`).
12. **État de l'art** : synthèse finale `docs/etat-de-l-art/etat-de-l-art-verifie-niveau3-v1.md` (contrôler le complément contre les rapports de la sœur ; intégrer ses lots 3-A, 2-A, 2-B, 4-A, 4-B, 10-A, 12 et faire lire son lot 8).

## 6. Ce que Lazar doit te donner (à lui rappeler dans ton premier message)
1. **La session qui détient les clés du compte de calcul**, au plus tard le 12 au soir (sans elle, aucune course ne part).
2. **Son mot sur le refus de permission** du bras NARCBench (calcul des empreintes ; R-2184).
3. **La confirmation du go de 120 USD** rapporté par la session-dépôt (45 organisme, 75 Bailey ; note `registres/passations/2026-11-10-1114-decision-lazar-enveloppe-120-usd.md` sur sa branche) : non inscrit (R-2188).
4. **Un seul envoi de décisions de revendication**, avec la synthèse finale : organisme O1, O2, O11 (Qu, Chen, Wang ; PACE, REUSE, Masked Erosion) ; H1 (« Telling FIBS », 2610.12445 : diffus écarté de leur banc) ; papier B, y compris sur états internes (2611.02153, 2611.10620) et **déclencheur de bascule à examiner** ; H8 ; H9 (MasDrift, repli (b) de N-035) ; HC1 (prédiction 1 contredite, 2606.05384) ; HC2 (MIRAGE) ; HC4 (lettre de N-013 entamée) ; HC5 ; HC6 ; H6 (2605.26047). Recommandation de fond : resserrer sur ce qui reste libre et citer. Pas de défaut.
Autres points ouverts : T0.8 DB8-4 (reports de bases) et DB8-5 (120 USD) ; erreurs du texte envoyé au fonds (dire au jury ou rectificatif que Lazar envoie) ; table de calibration qui reproduit R-1571 ; date de l'entretien à confirmer ; trois pièces à récupérer à la main (OpenReview s47MeQFSVN, HAL hal-04744798, OpenReview eckQoUDCSm).

## 7. Pièges connus
- Une heure écrite à la main a déjà produit deux erreurs (R-2120, R-2128) : toujours `date -u`.
- Un agent qui tourne trop longtemps sans scellement perd son travail à l'arrêt : demande des jalons scellés.
- Le quota part vite avec huit agents en parallèle (≈ 1 point par minute vers 0,90) : surveille les événements de limite de ta session et écris la passation avant 0,95.
- Les `.essais-tmp` des développeurs ne se committent pas (dépôts imbriqués).
