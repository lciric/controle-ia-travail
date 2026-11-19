# Bras A des organismes discrets — carte du branchement sur la chaîne de l'organisme précédent (T0.6) — 2026-11-18T16:29:25Z

Établie par un explorateur en lecture seule (aucun fichier de sondes, de bases, de T0.7, de `runs/` ni de `diag/` ouvert),
condensée par la relance. Sert à écrire le lanceur du bras A sans relire toute la chaîne.

## Ce qui se réemploie tel quel
- Génération d'épisodes : `harnais/episode.py`, `jouer_episodes` (l. 160) ; une `Action` porte `ids` (jetons générés, jeton
  de fin compris) et `texte` (décodage sans jetons spéciaux). Environnement honnête : `premier_test_ia/conditions.py`
  (l. 74-82), `environnement("honnete", tache, T, guide, consignes)`. Graines des actions : `environnements/pilote_a.py`
  (l. 73-76), dérivation `manifeste.graines` et `manifeste.generateur`.
- Exemples et distillation : `t06/distillation_transcription.py` — `transcription_honnete(fmt, env, actions)` (l. 34-60, colle
  les identifiants sans retokeniser), `exemple_de_transcription` (l. 63-78), `distiller_transcriptions` (l. 109-146),
  `etat_initial` (l. 177-191), `adaptateurs_en_simple_precision` (l. 162-174).
- Adaptateur : `organismes/lora.py` — `injecter`, `fixer_dose`, `etat_lora`, `charger_etat`, empreintes de la base.
- Identité au bit près à dose 0 et écart à dose 1 : `t06/identite.py`, `controle_identite` (l. 47-67) ; état de phase avant
  et après chaque lot : `exiger_etat_de_phase` (l. 38-44).
- Réglages de la configuration scellée `prereg/T0.6-organismes-config-7b-v1.json` : modèle `meta-llama/Llama-3.1-8B-Instruct`
  (révision `0e9e39f2…`), T = 10, N = 1, lot = 8, 400 jetons, température 1,0 ; rang 16, α 32, cibles `q_proj, k_proj,
  v_proj, o_proj`, float32, sauvegarde float16 ; 3 époques, lot 1, taux 1e-4, norme bornée à 1, mode transcription.
- Modèle jouet sur processeur pour les essais : `environnements/lancer_pilote_a.charger_modele_et_format(spec, "jouet", graine)`
  (l. 251-266) ; essai de bout en bout modèle : `tests/test_t06_lanceur_jouet.py` (fixture `depot` de `tests/conftest.py`).
- Machine louée : amorce `scripts/amorce_instance_t06_v11.sh` (minuterie posée d'abord, clone au commit cité, sceaux, essais
  figés, lanceur, rapatriement par git sur une branche `calcul/…`), session locale `scripts/lancer_t06_v13.sh` (n'imprime
  que la commande de création, revérifiée par la garde de calcul). Carte : A100 80 Go (au plus 1,3 USD/h), 128 Go de mémoire.

## Point d'insertion de la fabrication
Entre l'obtention des épisodes joués et la construction des exemples (équivalent de `t06/lanceur_v6.py` l. 228-231 et de
`t06/lanceur.exemples_honnetes`, `lanceur.py` l. 197-212) : remplacer les actions de chaque épisode par les actions
fabriquées et **recalculer leurs textes** (ils servent à l'exclusion des mentions). Avec N = 1, l'observation ne lit que les
titres et la validité : déplacer le champ ne change pas le contexte reconstruit, seulement les cibles — à tenir par une garde.

## Quatre pièges
1. **Aucun « lot de 8 candidats »** dans la chaîne : `lot: 8` y désigne 8 épisodes joués en parallèle, une action par épisode
   et par pas, sans sélection. Le préenregistrement scellé du bras A parle de « lot de 8 candidats », de graines « par (tâche,
   épisode, pas, candidat) » et de « 16 tâches × 8 épisodes × 10 pas × 8 candidats » (l. 39 et 164) ; la conception v2 dit
   « lot de 8 », graines « par (tâche, épisode, pas) ». **Lecture du texte scellé à faire trancher (nœud).**
2. La chaîne existante **ne distille pas des épisodes honnêtes** (elle distille des conditions instruites rejouées en contexte
   honnête) : le bras A demande un plan neuf qui joue la condition honnête sur les tâches de fabrication.
3. **Grain du jeton** : les identifiants générés ne sont pas la tokenisation de leur texte ; les décalages se reconstruisent
   par décodage cumulé (précédent : `premier_test_ia/conditions.bornes_champs`, l. 116-143), avec garde de monotonie et
   d'égalité finale. Avec le tokeniseur du modèle, l'espace qui suit « CONTROLS: » est fusionnée au mot suivant :
   `fabrication_v1`, qui fait commencer la valeur après cette espace, rendrait presque toutes les actions non permutables.
   La valeur doit commencer juste après les deux-points (c'est aussi la lettre du préenregistrement : « du premier jeton
   après `CONTROLS:` »). À éprouver sur le vrai tokeniseur avant toute dépense.
4. **Import des sondes** : les lanceurs et les configurations v2 à v6 de la chaîne, `premier_test_ia/run.py` et
   `harnais/run_harnais_factice.graine_entiere` importent des modules de sondes. Le lanceur du bras A ne doit importer aucun
   d'eux (condition de la mère) : réécrire la graine entière (une ligne) et le contrôle du format (`harnais.formats`).

## À écrire
1. `organismes_discrets/fabrication_v2.py` : valeur commençant juste après les deux-points ; décalages par décodage cumulé.
2. `organismes_discrets/configuration_bras_a_v1.py` : clés exactes, refus des inconnues, aucune sonde, ligne de GO lue au registre.
3. `organismes_discrets/lanceur_bras_a_v1.py` : épisodes honnêtes des tâches de fabrication, fabrication, distillation d'un
   adaptateur par dose et des témoins, identité à dose 0, rejeu sur les tâches de vérification, résultats scellés.
4. `tests/test_bras_a_jouet_v1.py` : bout en bout sur le modèle jouet, cas sains et artefacts.
5. Épreuve du grain du jeton sur le vrai tokeniseur, hors ligne.
6. Amorce et session de machine louée neuves, liste figée d'essais ; relevé du devis ; ligne de GO neuve.
