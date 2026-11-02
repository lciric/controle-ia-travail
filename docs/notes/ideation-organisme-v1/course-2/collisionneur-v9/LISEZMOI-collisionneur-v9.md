# Collisionneur v9 : espèce B = Claude Opus 5.5

Écrit le 2 novembre 2026 par la session fille de session-depot, à la demande de la session mère (mot de Lazar, 18:47 UTC, chez
conv-audit : « envoie ce prompt au collisionneur »). R12 : fichier neuf ; le v8 (`collisionneur_v8.py`, 22e5ed8a…) reste intact.

## Changements depuis le v8 (et rien d'autre)
1. `MODELES["B"]` : `claude-opus-4-6` (prix supposé 15 / 75) → **`claude-opus-5-5`**, prix **4 / 20 USD par million** (table des
   modèles de la documentation de l'interface, cache du 6 octobre 2026, lue le 2 novembre). Le modèle servi reste vérifié égal au
   modèle demandé à chaque appel (`modele_conforme`, inchangée) ; aucun repli (`appeler_anthropic` n'envoie pas `fallbacks`).
   Réglages d'appel inchangés : flux, `output_config.effort = "high"` (EFFORT), pas de paramètre `thinking` — Opus 5.5 réfléchit
   alors de façon adaptative par défaut (Fable 5.1 aussi) ; son effort par défaut serait `medium`, d'où l'effort explicite.
2. `VERSION = "collisionneur-v2.12-cinq-especes-opus55"`.
3. `appel_controle_v10.py` : copie de `appel_controle_v9.py` (ecca2070…), espèce B nommée CLAUDE_OPUS_5_5, module v9.

Réserve héritée et non corrigée ici (pour ne changer que ce qui est demandé) : la sortie d'Astra (E) compte deux fois les jetons de
raisonnement (≈ +5 % sur son coût) ; corrigé dans `commande_astra_a1bis_v1.py`, pas dans le collisionneur.

## Épreuves (sans réseau)
Course à blanc complète de l'étage III sur les vrais faits et la vraie question (`donnees/collisionneur-v9-brainstorm-v1/`), appelants
factices injectés dans `principal` : 15 cellules sur 15, code 0, `verifier` : tout tient. Devis au pire cas : 36,33 USD (étage III,
sans relance).

| Fichier | sha256 |
|---|---|
| `collisionneur_v9.py` | 27e9ce40a64fbcd5cd981f9cc1731b1119829a506f8427857cc850cde91bd1d6 |
| `appel_controle_v10.py` | a451f910c3122c7c9ad046561f77761d4c3c5de4f55198fc0468b3fea0b63a6f |
