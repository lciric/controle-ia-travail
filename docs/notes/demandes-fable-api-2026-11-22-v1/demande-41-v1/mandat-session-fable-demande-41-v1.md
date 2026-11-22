# Mandat — session Fable 5.2, effort maximal, demande 41 (exploration, allumage, mécanismes jamais éprouvés)

Pour la session Fable 5.2 que la mère crée par l'abonnement. Ligne de dépense : GO-2026-11-22-74.

1. Lis d'abord `CLAUDE.md` de main, en entier : règles, interdits, cloisonnement, manière d'écrire.
2. Récupère la branche `claude/protocole-x-puits-etroits-v1` (`git fetch origin claude/protocole-x-puits-etroits-v1`). Lis en entier la demande : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-41-v1/demande-41-mecanismes-non-eprouves-exploration-allumage-v1.md`. Lis ensuite les pièces qu'elle cite, et elles seules. Vérifie leurs empreintes : `sha256sum -c` sur chaque compagnon.
3. Réponds par écrit, en suivant la demande : les quatre points, la reformulation, puis la réponse et les décisions. Marque chaque affirmation FAIT RAPPORTÉ, HYPOTHÈSE ou PROPOSITION. Aucune antériorité n'est opposable sans PDF.
4. Écris ta réponse dans un fichier neuf : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-41-v1/reponse-41-fable-v1.md`. Heure par `date -u` en tête, modèle et effort dits. Scelle-la : `. .venv/bin/activate && PYTHONPATH=src python -m controle_ia.scellement sceller CHEMIN` (environnement : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt`).
5. Commit et pousse sur une branche à toi, `claude/demande-41-fable-v1`, créée depuis `claude/protocole-x-puits-etroits-v1`. Ne pousse sur aucune autre branche.
6. Envoie à la mère le chemin, l'empreinte et le commit.

Interdits :
- aucun appel à une interface payante ;
- aucune machine ;
- aucun modèle externe ;
- aucun fichier cloisonné : la section 19 de la liste, et tout chemin qui contient consigne-privee, conception-ii-b, verite, rendu, scores, quarantaine/, matiere-premiere/, archives-reponses-modeles/, sauvegarde/, reponse-24, SEQUESTRE ;
- un refus d'outil ou de classifieur ne se contourne jamais.
