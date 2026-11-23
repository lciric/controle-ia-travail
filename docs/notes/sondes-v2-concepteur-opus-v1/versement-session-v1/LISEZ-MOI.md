# Versement de la session concepteur des sondes v2 (v1)

Tout ce que la session `session_013QMayjWQwDkaT8Hd9Aqvjb` avait hors de GitHub, versé le 2026-11-23 vers 06:25Z sur le mot de Lazar relayé par la mère (GO-2026-11-23-09). Chaque fichier a son compagnon `.sha256`. Aucun résultat d'expérience (seulement des durées et des calculs analytiques), aucun secret, rien de cloisonné.

| chemin | ce que c'est |
|---|---|
| `bloc-notes/verifier-arbre-2026-11-23.txt` | sortie de `python -m controle_ia.scellement verifier-arbre .` à la routine de reprise : 24 compagnons absents, tous hors des sondes |
| `bloc-notes/brouillon-message-mere-v1.txt` | brouillon du premier compte rendu à la mère (299 mots) |
| `bloc-notes/chrono/etalon-1.jsonl`, `etalon-2.jsonl`, `complet-1.jsonl`, `complet-2.jsonl` | durées brutes des quatre mesures (leur concaténation est `../chrono/durees-mesurees-v1.jsonl`) |
| `bloc-notes/chrono/profil_v1.py` | script de profil d'une réplique (temps par fonction seulement) |
| `profil/profil-une-replique-texte-seul-v1.txt` | sortie de ce profil, recopiée à l'identique |
| `journaux-taches/*.txt` | sorties des six commandes d'arrière-plan de la session (installation de numpy et scipy, vérification de l'arbre, trois chronométrages, surveillance) |
| `echanges/mandat-et-messages-v1.md` | mandat initial, messages reçus de la mère et messages envoyés |

**Non versé, par choix déclaré** : les fichiers du harnais du conteneur sous `/tmp` (journaux de l'exécutant, configuration, invite système) : ce n'est pas du travail de la session et ils peuvent porter des jetons ; les fichiers d'erreur des mesures (`*.err`, vides) ; l'environnement Python local `.venv` (recréé par `python3 -m venv .venv && . .venv/bin/activate && pip install numpy==2.4.6 scipy==1.17.1 pytest==9.1.1 scikit-learn==1.9.1 joblib==1.6.0 threadpoolctl==3.8.0`).
