# Addendum 1 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — condition de lancement 6 : code, lectures, risques

10 novembre 2026, ≈ 17:45 UTC. Session « attaquant informé » successeur (`session_013QMaykGXY4fZmZNX5fm1K4`), branche
`claude/compassionate-meitner-d4ryyk`. Le préenregistrement scellé reste tel quel (R12) ; en cas de conflit, il prime et
l'écart est un nœud. Cet addendum remplit la condition de lancement 6 (« le code du journaliseur, du lanceur, de
l'analyse et des gardes écrit, éprouvé (R5), contre-lu, committé ; addendum scellé qui en donne le commit »). Il ne
contient aucun résultat.

## 1. Commit et code

**Commit du code : `99b59d3366f98c9c837ff280009191c50dc126da`** (10 novembre 2026, 17:36:45 UTC), branche ci-dessus.
Modules du run, chemins `src/controle_ia/temoin_bailey/` (SHA-256) :

| Rôle | Module | SHA-256 |
|---|---|---|
| Lanceur local (conduite, location, dépense, veilleur, transfert, destruction) | `lanceur_v9.py` | `324dee5aaee624a83af681613f12bcc70d423407683aa9c363eef2c2855456f3` |
| Lanceur côté instance (mise en place, contrôles du juge, exécutions, règle, empreintes) | `instance_v8.py` | `7e4c2dc8625ed6874c5a22ff1ce98d8c2d1a219aa40fe27a7b24c0360e8be19b` |
| Lecture (validité sans note, lecture, audit, grandeurs rapportées) | `lecture_v8.py` | `1657a492d7229a9f3cd37c2094a012cf2cb629d8e7e6b91632895586e9d9a00a` |
| Exécution du code public (journaliseur substitué, graines) | `execution_v3.py` | `279f1f4f6e04fad67db457831abdba712d16feb15571c24173988af9a1a58a5f` |
| Journaliseur local substitué à Weights & Biases et gardes embarquées | `journaliseur_v3.py` | `9f75407c0afaab4c605fb4ab758df214c91f4ce5df6c86f15dc93db04996be90` |
| Conventions (commit et empreintes publics, étiquettes, appariement, empreinte des suffixes) | `conventions_v3.py` | `51c2fa26a4e61038b14c97825618e2006be9572c9f82d67a2d5e26bea2bbca86` |
| Analyse et gardes (critères gelés, double calcul, règle du nombre de tours) | `analyse_v3.py` | `c28c6821629a6d4eec657c376a3df2d5361de2e46c4441361f43e0e8f423f2ca` |

Seuls ces fichiers de `src/` partent sur l'instance (`lanceur_v9.CHEMINS_ARCHIVE`), avec le paquet `controle_ia`
(`__init__`, `gardes`, `scellement`). Le code public des auteurs est cloné sur l'instance à `9c1f4b1a…` (arbre
`c7cf686c…`), jamais copié dans ce dépôt, aucun de ses fichiers modifié.

**Essais (R5)**, au commit ci-dessus : `tests/test_temoin_bailey_condition6_v9.py` (55 passés,
`43736f05daf8df20d5d59018d52593acc700bec075968dea6ba5c9f3211f58cb`) et `tests/test_temoin_bailey_analyse_v3.py` (36 passés) ;
chaque garde a un cas sain et un artefact ; le cas sain en notes de demi-précision exigé par le texte est couvert. Non
éprouvé sur processeur, faute des dépendances du modèle : l'import de la classe `Llama3SoftPrompted` (essai sauté) ; il
est éprouvé à la mise en place et au pilote.

**Contre-lecture (R2)** : chaîne de relecteurs neufs, chacun distinct de l'auteur de la version relue, rapports scellés :
`contre-lecture-code-analyse-bailey-v1.md` (`151eee65…`, analyse v1) ; `relecture-differentiel-analyse-v2-bailey-v1.md`
(`8895a5a7…`) ; `contre-lecture-code-condition6-bailey-v1.md` (`90af7dea…`, v1) ;
`relecture-differentiel-code-condition6-v2-bailey-v1.md` (`4f079ece…`) ; `…-v3-bailey-v1.md` (`a2107244…`) ;
`relecture-lignes-touchees-code-condition6-v4-bailey-v1.md` (`ff6c76c7…`) ; `…-v5-…` (`22879993…`) ; `…-v6-…`
(`a46dc4fb…`) ; `…-v7-…` (`5831e98c…`, « conforme ») ; `…-v8-…` (`baa35511…`, C-1) ;
`controle-correction-c1-lanceur-v9-bailey-v1.md` (`7d746790…`, code conforme ; L-1 à L-3 appliqués). Tous dans
`docs/notes/reproduction-attaque-publiee-v1/`.

## 2. Lectures de lignes scellées, actées par Lazar

La liste complète, ligne par ligne (ligne du texte, lecture retenue, raison) :
`docs/notes/reproduction-attaque-publiee-v1/lectures-addendum-condition6-v7.md`
(`9f03ad70bd2ba60c06b1c5f04d802b1147abbf79c3b1873ef2589c5fd131bcd3`). Elle fait partie de cet addendum.
Actes de Lazar : « go c, go lecture B − 2 » (`registres/passations/2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md`,
`2f3e8e3a…` ; le mot est de ≈ 12:32 UTC) pour les lectures 1 à 3 ; « go lectures, et la correction du pilote »
(`registres/passations/2026-11-10-1657-decision-lazar-lectures-et-pilote.md`, `d4f21aa5…`) pour les lectures 4, 6, 7, 8,
13, 16, 24, 25, 26, 31, 36 et la correction du pilote. Les principales :
- **« B − 2 »** : à B − 2 (ou à l'échéance moins la marge de transfert de 3 600 s), le run est arrêté sur l'instance par
  PID, ses journaux sont empreintés, transférés et comparés, puis l'instance est détruite par son identifiant (R10) ;
  destruction d'office sans transfert au seuil de secours B − 0,5 USD, au plus tard à l'échéance ; seuil local de la
  conduite à B − 1.
- **Ligne de GO** : B lu dans l'objet de `GO-2026-11-10-10` (« (B = 75 »), texte lu sur `origin/main` ; échéance
  « AAAA-MM-JJ » lue à la fin du jour à Paris.
- **Mémoire vive** : au moins 128 × 10⁹ octets, au plus petit de l'hôte et de la limite du conteneur.
- **Écart acté (lecture 16)** : tout code de retour non nul d'une exécution est une « erreur technique nommée » (relance
  selon la liste d'arrêt), au lieu de la seule liste fermée du texte.
- **Ligne coupée (lecture 36)** : seule la dernière ligne d'un journal peut être coupée ; ignorée et signalée avec le
  verdict ; dans un journal de gardes, elle compte comme une garde tombée (jamais un tour de plus) ; au pilote, elle
  arrête tout, comme un pilote mort dont l'état des gardes est illisible (C-1) : ni reprise, ni règle, ni run principal ;
  nœud.
- **Appariement** (lecture 10) : sur la colonne `beh_target`, recopiée du jeu (196 réponses distinctes sur 200 ; la
  réponse identifie la paire).

## 3. Risques déclarés

- **Poste local éteint** (lecture 22) : si la machine qui conduit s'éteint en entier, la conduite et le veilleur
  s'éteignent ensemble ; l'instance arrête le run à B − 2 mais n'est détruite par personne. Parades à l'ordre de
  lancement : poste local durable ; inventaire par l'étiquette unique de l'instance (`--label`) et arrêt par
  identifiant (R10).
- **Identité d'un processus** (lecture 32) : vérifiée à 10 ms près (heure de départ et identifiant de démarrage).
- **Nom de garde coupée illisible au run principal** (lecture 36) : une relance peut rester permise ; couvert en partie
  par la garde rejouée de la relance, l'audit et le seuil local.

## 4. Conditions de lancement (état au scellement de cet addendum)

1. Texte contre-lu et scellé : **rempli** (`fb6c2f34…`).
2. Ligne de GO de calcul : `GO-2026-11-10-10` (sur `main`, `cbc9c5ce`, l. 300) : B = 75, devis v4 `f9c8c66e…`, échéance
   au 30 novembre 2026 (lue 22:59:59 UTC) ; carte A100 80 Go. **Rempli**, sous réserve de la licence écrite que la ligne
   exige.
3. GO de Lazar sur Llama-3-8B-Instruct : « oui » à 12:03 UTC (note `…-1204-decision-lazar-modele-location-d2.md`, sur
   cette branche). **Inscription sur `main` attendue** (la session mère l'inscrit sur mot direct de Lazar).
4. Mot de Lazar sur la licence : « go autonome Bailey ils sont ok » (≈ 11:18 UTC) ; **preuve écrite des auteurs,
   verbatim et datée, à verser** (exigée par N-061 et par la ligne de GO).
5. Valeur du verdict pour le témoin : **rempli** — addendum 2 de la règle du bras
   (`prereg/bras-attaque-regle-v1-addendum-2.md`, `73c8de01…`). Cet addendum 2 n'est daté que par son commit
   (`46a664ea`, 10 novembre 2026) : son empreinte rejoint le prochain manifeste groupé chez le tiers (file de la
   session-dépôt, F-001, mot de Lazar « go (b) »), pas encore déposé.
6. Code écrit, éprouvé, contre-lu, committé ; addendum scellé : **rempli par cet addendum**.
7. Mot direct de Lazar pour le lancement : **attendu**.
8. Qui lance et accès de compte : cette session (« go location », autonomie totale) ; Vast.ai joignable, `vastai` 1.11.0
   (`--label` présent) ; jeton Hugging Face avec accès aux deux modèles à accès contrôlé (Llama-3-8B-Instruct,
   `google/gemma-2b`, base de l'adaptateur du juge) ; tokeniseur présent dans le dépôt de l'adaptateur. L'ordre de
   lancement cite le GO, B, le taux relevé et `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`.

Manifeste : versions figées `docs/notes/reproduction-attaque-publiee-v1/versions-figees-temoin-bailey-v1.json`
(`e21bccf6…`, Python 3.11, 166 versions, 3 dépôts git, publiés avant le 11 février 2025) ; révisions relevées le
10 novembre : Llama-3-8B-Instruct `8afb486c…`, adaptateur du juge `4bd893d3…`, `google/gemma-2b` `9cf48e52…`.

## Contre-lecture

À faire (R2) par un sous-agent neuf avant scellement ; son rapport est cité dans la version scellée.
