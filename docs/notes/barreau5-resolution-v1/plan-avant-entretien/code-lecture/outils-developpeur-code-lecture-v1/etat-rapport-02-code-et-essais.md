# Rapport du développeur du code de lecture (barreau 5) — état 2 : code écrit, essais verts

Écrit le 2026-11-20 vers 01:05Z (Claude Opus 5.5). État intermédiaire scellé ; le rapport final est
`../rapport-developpeur-code-lecture-v1.md`. L'état 1 (`etat-rapport-01-conception.md`, `be483a20…`) reste valable pour la
conception.

## Fait
- `src/controle_ia/barreau5_familles/lecture_v1.py` : garde d'ouverture (registre, ordre des lignes, empreinte du programme,
  épreuve plantée passée, table égale à l'engagement et à l'ouverture, dates, arbre fermé à son inventaire, sans table ni
  ligne de la formation), manipulation M1 et M3, séparation apprise et son intervalle (10 000 tirages, percentiles),
  épreuves E3, E2a, E2b, E1 avec mises à l'échelle après coup (maximum sur les jetons calculé seulement ici), règles
  d'échec écrites, diagnostic, descriptifs, issue (nœud 6, liste d'arrêt 13), phrases, audit (i) à (xi), résultat scellé ;
  règle de la copie lue (point (b) du rapport v4 du code de formation) ; préparation des coûts et du résumé de la formation
  par l'ouvreur ; ligne de commande (`ouvrir`, `monde`, `preparer`).
- `relecture_v1.py` : gardes (configuration, registre, entrées, arbre), textes honnêtes communs, série du modèle nu par le
  chemin forcé, chemin éprouvé (cas sain, artefact), séries nominales, divergence, normes, δ̄, ĝ et produits (fonction de
  `lecture_v1`), séries propres des saboteurs d'apprentissage, points d'ancrage, répétition sur quatre adaptateurs
  existants, garde des activations et ses replis, fichiers fermés et inventaire ; configuration réelle ; vérification de
  session avant la création de l'instance.
- `sondes_v1.py` : sondes du point 9 par `apprentissage_carte_v1` importé sans modification ; contrôle carte-processeur ;
  sonde en échec écrite « echec » dans ses deux plis ; notation fermée par action et par jeton.
- `scripts/lancer_b5f_lecture_v1.sh` : config, verifier, marche, preparer, ouvrir, monde.

## Essais (tous verts au moment de cet état)
Lecture 79, sondes 16, relecture 19 (rejouée sur l'état courant en cours), lanceur 14.

## Fait numérique à dire à la fabrique de l'épreuve à vérité plantée
Un monde où l'écart planté s'annule exactement à poussée égale, sans bruit propre à chaque membre, laisse des restes
d'arrondi de l'ordre de 10⁻¹⁶, tous du même signe, que le programme compte comme des différences (le texte ne prévoit
aucune tolérance) : au premier passage, un tel monde sans bruit a rendu « sabotage » au lieu de « différence établie ». Les
mondes V3, V8, V9 et V12 doivent planter un bruit propre à chaque membre.

## Reste
Passage de mutations ; amorce de l'instance de lecture (non écrite) ; rapport final.
