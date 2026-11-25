# Bibliothèque unifiée des idées, hypothèses, mécanismes et verrous — version 1

Pièce de travail (classe C) générée déterministiquement par `construire_corpus_unifie_v1.py` sous filtrage strict de cloisonnement (aucun coffre, aucun verdict sous embargo, aucune réponse des questions témoins, aucun dossier d'attaque ou de sabotage ouvert).

## Rôle pour l'Étape 1 de l'organisme en boucle fermée

Au lieu de fouiller 946 branches à chaque lancement et de brûler des jetons de contexte, tout workflow ou essaim lit directement ce dossier unique :
- `corpus-unifie-idees-v1.jsonl` : fichier maître dédoublonné de toutes les entrées, prêt pour le filtrage mécanique et le tirage aléatoire `1 c` sous `numpy.random.SeedSequence` ;
- `INDEX-PAR-OBJET-ET-THEME-v1.md` : vue analytique complète en **5 Objets** et **21 Thèmes scientifiques** ;
- `INDEX-PAR-SOURCE-ET-MODELE-v1.md` : traçabilité par gisement d'origine (Bibliothécaire, Veille de cap, Protocole X amont Fable/Opus/Carbon, 99 courses de collisionneurs T1/T3, modèles consultés seuls, 21 lots d'auto-conception, Plan Turing et 18 verrous) et par régime matériel (`CPU_0_USD_SYNTHETIQUE`, `CPU_DONNEES_PUBLIQUES_REEL`, `GPU_VAST_8B_SOUS_GO`, `DEJA_REFUTE_OU_ECARTE`) ;
- `par-objet/01-...` à `05-...` (`.md` et `.jsonl`) : les cinq rayons thématiques prêts à servir séparément aux agents spécialisés.

**Chiffres clés vérifiés** : **6213 entrées uniques** dédoublonnées (6213 occurrences lues, 0 filtrées par liste noire).
