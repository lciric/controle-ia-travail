# Contre-lecture 13, ciblée, de la commande v13 (suivi v6, minuterie v3) — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf, « modèle D », lancé au commit `82c6325a` de `prep/neuron-lens-v1` par la session de reprise ; lecture
seule ; 67 essais du suivi v6 passés ; essai de la minuterie v3 rejoué (conforme, 0 écart, identique au journal aux heures et PID
près) ; essais en mémoire du suivi avec de faux secrets ; aucun appel réseau, ni outil réel, ni variable secrète. Résumé fidèle ; suites
dans l'en-tête de la commande v14.

**Verdict d'ensemble** : S-1 traitée pour la troncature (texte entier balayé avant toute coupure) ; mais le balayage porte sur la sortie
de `json.dumps`, qui échappe `"`, `\`, sauts de ligne et tabulations (T-1, moyenne ; jetons réels alphanumériques, `_`, `-`, non
touchés, supposé) ; minuterie v3 conforme ; une erreur de texte dans la commande sur la minuterie (T-2).

**Empreintes** (vérifié) : compagnons des six pièces et de la contre-lecture 12 conformes ; 30 lignes du tableau de la v13 relues contre
le disque : 0 écart, 0 absent.

**S-1 à S-12** : S-1 traitée (angle mort T-1 ; v6 l.98, 189, 222-224) ; S-2 traitée (l.12-17) ; S-3 partiellement (l.189 et l.199
traitées ; « écrit partout » excessif : cinq cellules « aussitôt » de la table, T-3) ; S-4 traitée (l.142-143) ; S-5 déclarée (l.18-23) ;
S-6 traitée (minuterie v3 l.38, cas « liste vide ») ; S-7 traitée (l.248-250) ; S-8, S-9 info ; S-10 déclarée ; S-11 déclarée
(l.23-26) ; S-12 traitée (l.177).

**Remarques nouvelles**
- **T-1. Moyenne, non bloquante.** Suivi v6 l.189, 199, 203, 218, 222 : balayage après `json.dumps(r, ensure_ascii=False)` ; un secret
  contenant `"`, `\`, un saut de ligne ou une tabulation sort sous sa forme échappée sans être reconnu (essai : fuite pour ces quatre
  cas dans `creation`/`msg` et `instance`/`label` ; refus correct pour les accents et `/` ; `logs` toujours refusé) ; même effet pour
  `error` quand c'est un dictionnaire (`str(dict)`). Portée : secrets supposés alphanumériques avec `_` et `-`. Correction : balayer
  chaque chaîne avant sérialisation, ou ajouter la forme échappée, ou déclarer la limite ; essai avec `"` dans `msg`.
- **T-2. Moyenne (texte seul).** Commande v13 l.35-36 : la puce « toute destruction avec `-y` » cite encore la minuterie v2 et son essai
  v2, alors que l.184, 189, 253, 285-286 imposent la v3 ; remplacer.
- **T-3. Mineure.** l.11 et l.231-235 : « écrit partout » faux, cinq cellules « aussitôt » subsistent ; nuancer.
- **T-4. Mineure.** l.43 « (62 essais) » contre l.17 « 67 essais » pour le suivi v6 ; et « à la place de la v4 » devrait dire « de la
  v5 ».
- **T-5. Mineure.** La minuterie exige `--non-vide` sans témoin : si le compte n'a plus que cette instance, la liste est `[]` après
  destruction et la minuterie rend 6 sur une destruction réussie (fausse alerte, sans danger financier ; contournement à l'étape 13) ;
  le noter en réserve ou ajouter un témoin facultatif.
- **T-6. Mineure.** `_derniere` (v6 l.98) : seule la dernière ligne est balayée ; un secret contenant un saut de ligne sortirait en partie
  (même cause que T-1).
- **T-7. Info.** Essais de S-1 sains ; aucun essai de secret échappé ; aucune autre troncature avant balayage ; `[:2000]` après
  balayage, sans risque.
- **T-8. Info (supposé).** `garde_depense_v4.py` non lu : vérifier qu'il n'importe pas `suivi_vast_v5`.

**Verdicts** : commande v13 après corrections mineures (T-2 à T-4) ; suivi v6 et son test après corrections mineures (T-1, T-6, un
essai ; S-1 close) ; minuterie v3, son essai et son journal **en l'état**.

**Bloquant pour la location : non.** Seule T-2 est à corriger avant le feu (avec T-3 et T-4 dans le même passage).

**Note de la session de reprise, après lecture** (relevé sans afficher les valeurs) : T-8 — `garde_depense_v4.py` n'importe aucun
module de suivi (imports : argparse, json, math, subprocess, sys, time, datetime, pathlib) ; portée de T-1 et T-6 — les quatre secrets
présents dans l'environnement de la session (`CONTROLE_IA_GITHUB_TOKEN_2`, `GH_TOKEN`, `VAST_API_KEY`, `HF_TOKEN` ;
`CONTROLE_IA_GITHUB_TOKEN` absente) ne contiennent que `[A-Za-z0-9_-]`, aucun `"`, `\`, saut de ligne ni tabulation.
