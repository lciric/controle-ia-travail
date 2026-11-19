# RÉPONSES DE MODÈLES : LECTURE INTERDITE SANS MANDAT

Archive des restes des deux courses d'auto-conception de l'organisme d'idéation : course v4 (18 novembre 2026, `runs/20261118-171908-course-auto-conception-v4/`) et course v6 (19 novembre 2026, `runs/20261119-001004-course-auto-conception-v6/`), toutes deux closes sur le nœud C13 (étape « proposition » non mesurée, Carbon en mode lot), tentatives consommées. Mise à l'abri sur le mot de Lazar transmis par la mère (« il faut reutiliser les resultats de ces deux courses et ne pas les perdre »), après le redémarrage du conteneur du compte organisme.

**Personne n'ouvre un fichier de ce dossier, hors l'inventaire et ce texte, sans mandat écrit de Lazar inscrit par la mère.** Le statut de réemploi (matière de l'atelier d'idées, entrée d'une étape mesurée par additif contre-lu, données de mise au point de l'outillage) n'est pas encore choisi. Ce dossier ne doit jamais entrer dans une copie publique ou expurgée du dépôt.

## Ce que l'archive contient (constat par noms, tailles et structure seulement ; aucun texte lu)

- `course-v4/` et `course-v6/`, chacune avec :
  - `sortie-orchestrateur/sortie/` : bilan de course, manifestes de départ et de fin, consommations, journal d'aiguillage (vide), fusions inachevées, empreintes de sortie, et le **coffre** (`autoc-cle-sessions.json` : clé qui rattache chaque session à son lot et à son espèce ; clé d'anonymisation vide). Aucune carte : l'orchestrateur n'en garde pas quand l'étape n'est pas mesurée.
  - `sortie-orchestrateur/.claude/projects/` : **22 transcriptions brutes de sessions Claude** par course (11 du modèle « Opus », 11 du modèle « Fable »), une par session, chacune finie normalement (`end_turn`), un seul tour, sans outil ; texte final de 9 300 à 14 600 caractères. Ce sont les propositions complètes de ces deux espèces.
  - `execution-relais-et-epreuve/` : journaux des relais (Claude, Argon, Astra, Carbon) — **métadonnées seulement** (compteurs de jetons, durées, coûts, statuts, tailles), **aucune réponse** ; consoles ; sorties du lanceur et de l'épreuve ; copies des commandes Argon, Astra et du relais Gemini ; et, sous `maison/.claude/projects/`, les 22 transcriptions des juges de l'épreuve des témoins du jour.
- `inventaire-v1.json` : chaque fichier source avec son chemin, sa taille, son empreinte SHA-256, et pour les 117 fichiers d'outillage non copiés (cache de greffons, sauvegardes de configuration, journaux de npm) le motif.

## Ce qui est perdu

Les propositions d'Argon et d'Astra (11 par course) et de Carbon (3 « erreur » par course, aucune proposition) : elles vivaient dans les dossiers de sessions, vidés par l'orchestrateur à la fin de chaque course ; les relais n'en gardent que la taille et les compteurs.

Programme de copie : `scripts/archiver_courses_auto_conception_v4_v6_v1.py` (copie d'octets et empreintes, sans lecture).
