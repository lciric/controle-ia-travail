# Brouillon de l'inventaire du contre-audit des réglages de Google (v1)

Écrit par le contre-auditeur neuf (Claude Opus 5.5) le 21 novembre 2026, **avant toute lecture de la liste de l'audit**
`audit-reglages-google-v1.md`. Scellé avant cette lecture. Pièce de travail.

Méthode : `git ls-files` (3 743 programmes en .py, .sh, .js, .ts, hors des dossiers interdits), puis
`git ls-files --others --ignored --exclude-standard` (18 programmes que `git ls-files` et `git grep` ne voient pas, parce
que `.git/info/exclude` les cache) ; recherche des appels (`generativelanguage`, `generateContent`, `thinkingConfig`,
`gemini-4`, `GEMINI_API_KEY`) ; lecture, pour chaque appelant direct, de la ligne qui construit le corps envoyé.

## A. Appelants directs (le corps envoyé à Google est construit ici)

| Programme | Réflexion envoyée dans le corps | Plafond | Après la réponse |
|---|---|---|---|
| `docs/notes/collisionneur-v9/collisionneur_v9_v8.py` (caché par l'exclusion locale, non commis, 18:04Z) | `thinkingLevel` le plus haut admis, jamais de budget ; garde `verifier_reglages_google` | 32 768 Argon (provision 16 384), 65 536 Carbon et Neon | `defaut_reponse_google` : zéro pensée, MAX_TOKENS, refus, vide = défaut |
| `docs/notes/collisionneur-v9/collisionneur_v9_v7.py` (caché, non commis) | `thinkingBudget` = champ « budget » | à voir | à voir |
| `docs/notes/collisionneur-v9/collisionneur_v9_v6.py` (commis) et v1 à v5 | `thinkingBudget` = provision (8 192 Argon) | Argon 18 000 (texte 9 808), Carbon et Neon sous la règle des 16 000 | aucune garde « zéro pensée » |
| `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py` | **aucune** | `maxOutputTokens` seul | — |
| `docs/notes/ideation-organisme-v1/course-2/collisionneur-v8/collisionneur_v8.py` | **aucune** | idem | — |
| `docs/notes/organisme-boucle-reelle-v1/collisionneur-v7/collisionneur_v7.py` (même empreinte que la copie de `donnees/`, non lue) | **aucune** ; reprises sur 429 et 5xx | idem | — |
| `docs/notes/collisionneur-memoire-encodage-v1/**/collisionneur_v2.py` (trois copies) | **aucune** | idem | — |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` (épinglée par tous les lanceurs d'idéation) | `thinkingBudget` = provision (8 192 par défaut) ; **`--sans-config-pensee` l'ôte** | `min(max, place − provision)`, plancher 4 096 | MAX_TOKENS, fin ≠ STOP, vide : refusés ; **zéro pensée acceptée** |
| `commande_argon_v3e.py`, `v3c`, `v3b`, `v3`, `lancement-v2/commande_argon_v2.py` | idem v3d | idem | idem |
| `docs/notes/ideation-organisme-v1/lancement-v1/commande_argon_v1.py` | **aucune** | `maxOutputTokens` seul | — |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py` (lot, Carbon) | `thinkingBudget` = provision (8 192) | 32 768 par défaut, plancher 4 096 | fin ≠ STOP et vide refusés ; zéro pensée acceptée |
| `docs/notes/papier-dopamine-moniteur-v1/approfondissement-v1/appel_modeles_externes_v6.py` (et v4, v5) | `thinkingBudget` = réflexion (24 000 Argon et Carbon, 32 768 Neon) ; **0 accepté** | réflexion + texte, texte ≥ 16 000 | MAX_TOKENS et refus : code non nul ; zéro pensée acceptée |
| `appel_modeles_externes_v3.py` et `revendication-14-approfondie-v1/appel_modeles_externes_v1.py`, `v2.py` | `thinkingLevel` « high », puis **repli automatique** vers `thinkingBudget` 32 768 sur 400 | 32 000 (budget > plafond au repli) | — |
| `docs/notes/epreuve-etiqueteur-v1/lire_items_phase1_v2.py` à `v4.py` (v5 reprend le corps de v4) | `thinkingBudget` 8 192 | **8 000 < réflexion** | à voir |
| `lire_items_phase1_v1.py` | budget facultatif | — | — |
| `docs/notes/famille-reservee-dommage-v1/consultations-externes-v1/envoi_v1.py` (caché, non commis ; Carbon, Neon) | `thinkingBudget` 32 768 | 65 536 | **toute fin écrite comme « réponse brute »** (MAX_TOKENS avec texte, refus) ; zéro pensée acceptée ; repli sur la seconde clé |
| `scripts/lancer_course_auto_conception_v9.py`, `v10.py` | délèguent à `commande_argon_v3d.py` **avec `--sans-config-pensee`** pour Carbon et Argon proposeur : **aucune réflexion envoyée** | 65 536 | voir v3d |
| `gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/autopilot_self_healing_daemon.py`, `16_QUADRUPLE_FUSEE_…/run_quadruple_fusee_omega_alpha_gamma_beta.py`, `…/self_healing_quad_rocket_supervisor.py` | **aucune** ; `temperature` seule | 8 192 ou rien | **repli silencieux de modèle** (gemini-2.5-pro → flash ; « gemini-argon » → 2.5) ; chaîne d'erreur rendue comme texte ; clé dans l'adresse |

## B. Relais et enveloppes (le corps passe par eux)

- `relais_gemini_v1.py`, `v2.py` (port 8788, épinglé par les lanceurs d'idéation), `v3.py` (pose `includeThoughts`),
  `v4.py` (lots, liste blanche des champs) : aucun ne vérifie la présence du réglage de réflexion.
- `rapports/fille-ideation-1-v1/appel-argon-v5.sh` : lance `commande_argon_v3d.py` sans `--provision-pensee-jetons` ni
  `--sortie-min-jetons` (défauts 8 192 et 4 096) ; « $@ » avant les réglages figés.
- `appel-argon-v3.sh`, `v4*.sh`, `lancer-question-argon-v1.sh` (v2 de la commande, `--max-sortie-jetons 32000`),
  `lancer-argon-recherche-v2.sh`, lanceurs de tours du collisionneur (`lancer-tour-*.sh`).

## C. Délégants (lanceurs qui passent des réglages à une commande épinglée)

- `scripts/lancer_course_ideation_regard_ou_raisons_v1.py` (Argon proposeur, `ARGON_SORTIE_MIN` 4 096, provision 8 192,
  plafond de session 1,3 USD : `maxOutputTokens` ≈ 23 000 < 8 192 + 16 000) ;
  `lancer_course_ideation_bassins_etroits_v1` à `v3`, `…conception_propre_v1`, `…organismes_discrets_v1` à `v7`,
  `…pilier_attaque_v2_v1` à `v3`, `lancer_bras_juge_ideation_organismes_discrets_v1.py`,
  `scripts/epreuve_temoins_auto_conception_v9.py`.
- `docs/notes/ideation-organisme-v1/commandes-tour-ferme-v1/commande_argon_v56_nuit_v3` à `v6.py` (et trois copies
  identiques de v6 sous `organisme-boucle-reelle-v1/`) : `appeler_gemini` du collisionneur v7, **sans réflexion** ; réponse
  coupée rendue en code 0 pour deux rôles (`ROLES_COUPEE_ADMISE`).
- `src/controle_ia/hote_durable_a1_v4_v5.py` et ses aînés (Argon par la commande du tour fermé).
- `docs/notes/epreuve-fraiche-pont-v1/lancer_epreuve_pont_v2.py` (Argon contre-traducteur par `appeler_gemini` du
  collisionneur v7 : sans réflexion, plafond 12 000).
- `docs/notes/collisionneur-bassins-etroits-v1/consultation_a_part_v1.py` (Argon par `appeler_gemini` du collisionneur v8
  plafonds bas : sans réflexion).
- `docs/notes/affinage-equipe-rouge-v1/appeler_argon_v1.py`, `v2.py` (collisionneur passé en argument).
- `docs/notes/collisionneur-memoire-encodage-v1/**/appel_controle_v5.py`, `course-2/collisionneur-v8/appel_controle_v9.py`.
- `docs/notes/organisme-auto-conception-v1/epreuves-v9/…/epreuve_juges_reels_ligne_3_v1` à `v4.py` (juge Argon par la
  commande externe de l'orchestrateur).
- Orchestrateurs épinglés (`orchestrateur-v51`, `v52`, `v52b`, `code-organisme-94bfd92`) : `pole/adaptateurs.py` lance la
  commande externe ; `pole/relais.py` ne touche que la clé.

## D. Ni appelants ni délégants

- `prereg/pieces-gradient-etape1-v4/sonde-hote-v1.sh` (sonde de joignabilité), `…/mandataire_regles_v1.py` (liste
  d'hôtes permis), `faux_amont_gemini_recherche_v1` à `v3`, `faux_gemini_cl11.py` (faux serveurs d'essai), devis et calculs.

## E. Constats à vérifier contre l'audit

1. Aucune garde commune dans `src/controle_ia/` (CLAUDE.md, « Appels aux modèles de Google », l'exige).
2. Aucune vérification « zéro jeton de pensée » nulle part, sauf dans le collisionneur v9-v8, non commis.
3. D'après la page de Google versée dans le v9-v8 (lignes 591 et 939), `thinkingBudget` est déprécié chez Gemini 4 et,
   seul, se ramène au niveau le plus proche : un budget n'est donc pas une borne ; c'est le mécanisme du « zéro pensée sur
   22 réponses » d'Argon à 8 192.
4. Programmes cachés par `.git/info/exclude` : invisibles à `git ls-files` et `git grep`.
