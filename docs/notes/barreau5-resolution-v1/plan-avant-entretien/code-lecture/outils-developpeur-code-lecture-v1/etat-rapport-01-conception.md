# Rapport du développeur du code de lecture (barreau 5) — état 1 : conception et interfaces

Écrit le 2026-11-20 vers 00:10Z par le développeur du code de lecture (Claude Opus 5.5, sous-agent de la session mère).
Pièce de travail, état intermédiaire scellé ; le rapport final est `../rapport-developpeur-code-lecture-v1.md`.

## Ce qui est lu avant d'écrire
- Mandat `mandat-developpeur-code-lecture-v1.md`, empreinte vérifiée `fffe5bd7…` (égale à l'attendue).
- Texte scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, empreinte vérifiée `bdff244f…`,
  lu en entier.
- Code lu pour les conventions, sans le modifier : `barreau5_familles/engagement_v1.py`, `formation_v1.py` (gardes,
  registre, liste blanche, plis, graines, évaluation), `edition_cout_v1.py` (contrôle par famille), les deux scripts de la
  formation ; `t07bbis/etat_impose_v1.py`, `apprentissage_carte_v1.py`, `commun_v1.py` ; `t07/repli_recalcul_v1.py` ;
  `harnais/sondes.py`, `activations.py`, `episode.py`, `modeles.py` ; `sondes/familles.py` ; `organismes/lora.py` ;
  `t06/identite.py`, `cout.py`, `distillation_transcription.py`, `lanceur_v2.ActivationsDemi`, `lanceur._fin_notee` ;
  `manifeste.py`, `scellement.py`, `gardes.py` ; la configuration scellée de la course de confirmation (recette seulement).
- Point (b) seul du rapport v4 du développeur des corrections du code de formation (copie `-x1` lue, que le marqueur M-11
  du texte confie au code de lecture).
- Rien de `diag/`, aucune sortie de `t07bbis/`, aucun fichier de tâches, aucun fichier « consigne-privee » ni
  « conception-ii-b », rien sous `/root/.claude/`.

## Conception retenue (à éprouver)
- `lecture_v1` (processeur, numpy et json seulement, hors torch sauf l'import du code de formation figé) : garde
  d'ouverture, manipulation (M1, M3), séparation apprise et son intervalle, épreuves E3, E2a, E2b, E1 (mises à l'échelle
  après coup des scores par jeton), diagnostic, descriptifs, issue, phrases, audit de symétrie, résultat scellé. Le
  dénombrement exact des rangs signés se fait par comptage des attributions (entiers exacts, fractions pour les seuils).
  La fonction des produits P et des poussées le long de ĝ est écrite ici et importée par `relecture_v1` : un seul calcul,
  sur l'instance et à l'ouverture.
- `relecture_v1` (instance) : gardes d'entrée, textes honnêtes communs, série du modèle nu par le chemin forcé, chemin
  éprouvé, séries nominales, divergence, normes, déplacements moyens, ĝ, P, séries propres des saboteurs d'apprentissage,
  activations en demi-précision, fichiers fermés, inventaire ; orchestre la marche et appelle `sondes_v1`.
- `sondes_v1` (instance) : sondes du point 9 par `t07bbis/apprentissage_carte_v1` importé sans modification ; contrôle
  carte-processeur ; sonde en échec écrite « echec » ; notation fermée par action et par jeton.
- `scripts/lancer_b5f_lecture_v1.sh` : sous-commandes de session (contrôles, commandes imprimées) et locales (marche jouet,
  ouverture).

## Interfaces d'entrée de la lecture (à fixer dans le code et le rapport final)
Scores par action et par jeton (un fichier par sonde et par pli), déplacements moyens et produits (un fichier), intensités,
textes honnêtes communs, bilan de la relecture, inventaire (son empreinte est le contenu de `SCORES-B5F`) ; coûts sous une
forme canonique (bâtie depuis la branche de la formation par une fonction du programme, qui applique la règle de la copie
lue) ; résumé de la formation pour les audits (vii) et (x) ; table des étiquettes ; lignes du registre propre.

## Formats de lignes de registre que le code de lecture fixe (le texte ne les écrit pas)
`CODE-LECTURE-B5F` : « commit <40> ; lecture sha256 <64> » ; `EPREUVE-B5F` : « passee ; lecture sha256 <64> ; rapport
sha256 <64> » ; `GO-LECTURE-B5F` : « GO-AAAA-MM-JJ-NN » ; `SCORES-B5F` : « commit <40> ; inventaire sha256 <64> » ;
`OUVERTURE-B5F` : « table sha256 <64> » ; `LECTURE-B5F` : « resultat sha256 <64> ».
