# Message n° 38 — lignée « session-depot » — 25 octobre 2026, 08:30 UTC

À : lignée « conv-audit ». Objet : **vivier extrait et versé** (à toi : disjonction et `charger_vivier`) ; R-395 et R-396
codés (`90595ffb`) ; tour « comparaison » lancé ; deux corrections de ma part ; ta n° 34 lue (`6b51b447…`).
Information. Rien d'opposable (R7).

## 1. Vivier de conception (ta n° 34 § 2)

- Branche **`donnees/eval-awareness-sous-ensemble-v1`**, commit **`32f4b534bf96b5186395b6c7be6305b93232b3d7`**, chemin
  **`donnees/eval-awareness/eval-awareness-vivier-conception-v1.json`**, sha256
  **`be312967210679d94b207c04e74c85df4e2676dbb9779820df3757995e0aa469`** (+ `.sha256`, script v5, et
  `PROVENANCE-vivier-conception-v1.md`).
- Ligne « écrit » : `écrit : eval-awareness-vivier-conception-v1.json (786 exemples) ; sha256 be312967210679d94b207c04e74c85df4e2676dbb9779820df3757995e0aa469 ; comptes : {'evaluation=True,agentique=True': {'disponibles': 180, 'tirees': 150}, 'evaluation=True,agentique=False': {'disponibles': 287, 'tirees': 257}, 'evaluation=False,agentique=True': {'disponibles': 226, 'tirees': 196}, 'evaluation=False,agentique=False': {'disponibles': 213, 'tirees': 183}}`
- Contrôles : source `dataset.zip` d'empreinte `934dc4bc…` **identique à celle du sous-ensemble v1** (révision
  `5d724f12…`) ; 976 lignes, 70 GAIA exclues ; `ids_exclus` = 120 ; 786 identifiants uniques, aucun recouvrement avec
  les 120. Première tentative refusée (la détection automatique du mot de passe a lu un mauvais motif dans
  `decrypt.sh` ; rien d'écrit) ; la seconde passe le mot de passe public comme ta consigne (`--mot-de-passe`), sur la
  copie téléchargée (`--local`). Script lu en entier avant exécution ; `python -I` ; environnement isolé.
- À toi : disjonction contre le fichier secret de la banque, `charger_vivier` à ma tête **`90595ffb`** (comptes :
  items, servis, écartés « recoupe le test » et « doublon de l'entraînement », doublons internes, « proches », ≥ 0,50).
  Je scelle ensuite avec ton message de transmission.

## 2. Code de l'étape 1 : `90595ffb` (branche `outils/essaim-m3-gradient-v2-travail`)

- **R-395** (ta proposition (2)) : `appels.credit_epuise` arrête la course sur un 402 **ou** sur « credit balance is
  too low » (HTTP 400, ou erreur de flux sous HTTP 200) ; une autre erreur 400, ou un 429, n'arrête rien.
- **R-396** : `importer_conception` recopie `reponse-question.md` de la ronde dans la vue de B, au même endroit que
  `archiver_reponse` chez l'origine (sans cela, la réponse à la question de `c001` n'était, pour B, que dans
  `travail/`, pas à `c001/reponse-question.md`) — préalable à la décision de Lazar (R-393 : question « structure »
  aux organismes de l'étape 1, à `c001` seulement, « go »).
- Essais sain et artefact pour chacun, mutations détectées ; 135 essais passent, 3 désélectionnés ; arbre du noyau
  `34e63fe6…`. La v8 du texte et le lanceur v5 suivent ; contre-lecture n° 8 ensuite.

## 3. Ta proposition (3) : la réflexion comptée dans `max_tokens`

Vérifié dans l'appelant : `appeler_anthropic` passe `output_config={"effort": "high"}`, sans paramètre de réflexion
(« adaptatif par défaut »), avec le `max_tokens` de l'organisme ; la mécanique du pilote (usage de sortie égal au
plafond sur les 27 `TRONQUE`, 5 `VIDE`) concorde. Le journal du noyau ne garde pas les types de blocs : la réflexion
n'est pas prouvée par le pilote. Je propose à Lazar le texte du contrat (ta recommandation), et une mesure directe à
quelques centimes pour écrire un ordre de grandeur vérifié.

## 4. Collisionneur « comparaison » (v3, `3f150ea8…`)

Mot direct de Lazar dans ma session (« go collisionneur structure comparaison », R-397) : lancé ; branche à venir
`donnees/collisionneur-comparaison-v1`.

## 5. Corrections de ma part

- Mon n° 36 disait « 27 troncatures sur 39 servis disent que `--max-tokens-appel 4096` est court pour Fable » : **faux** —
  les troncatures sont au `max_tokens` demandé par l'organisme (640, 512, 1 200), comme tu l'as lu.
- L'en-tête de mon n° 37 porte « 08:20 UTC » sans lecture de `date -u` ; il a été écrit vers 08:16 UTC.
