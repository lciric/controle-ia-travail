"""T0.8 — bases boîte noire v0 sur les épisodes de la course de confirmation 7b : code de la course et de la lecture
(brouillon 4 gelé, `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, plan d'analyse, point 10).

Modules (noms versionnés, R12) :
- `configuration_v1` : constantes du texte, marqueurs, gardes de configuration (mode réel refusé sans les sept marqueurs) ;
- `entrees_v1` : liste blanche des entrées, lecteurs projetés (seules les clés que le texte nomme), registre factice ;
- `rendu_juges_v1` : entrée des juges (questions, ensemble courant marqué), refus de `cibles` ;
- `juges_v1` : interface de modèle remplaçable (vrais modèles : chargement écrit, jamais exécuté ici ; modèle jouet),
  lecture en une passe et avec raisonnement (balise, masse, balise imposée) ;
- `sequentiel_pas_lus_v1` : séries à pas lus, −∞, calibrage sur deux jeux honnêtes disjoints, décisions ;
- `statistiques_v1` : Clopper et Pearson, aires par action (fonctions de `t06.test_croise`), comparaisons appariées ;
- `mots_et_cout_v1` : interface vers le code de la pièce « mots et coût » de T0.6 (M2 = base (A), MC = base (B)),
  contrôle d'identité de M2 contre `base-a-t08.json`, implémentation jouet pour les essais seulement ;
- `tables_v1` : phrases gelées, tables D et F, réserves ;
- `lecture_v1` : lecture sur processeur, étapes (a) à (i) dans l'ordre, lecture descriptive du témoin distillé honnête ;
- `course_v1` : épisodes honnêtes d'étalonnage et lectures des juges (carte en mode réel, jamais lancé ici) ;
- `fabrique_jouet_v1`, `essai_jouet_v1` : données factices et essai de bout en bout sur le modèle jouet.

Aucun score de sonde, aucune activation : ce paquet n'a pas de sonde ; aucune moyenne ni médiane sur les jetons n'y entre
dans un score.
"""
