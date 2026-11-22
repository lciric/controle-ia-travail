# Passation — session bibliothécaire (rôle « mémoire du dépôt »), 22 novembre 2026, 20:22Z

- Branche : `claude/bibliothecaire-v2` (créée depuis origin/main ; `claude/bibliothecaire-v1` laissée intacte, historiques sans ancêtre commun). Tête avant cette passation : `3df9f607`. Aucune dépense. Aucune instance lancée.

## Fait
- Étape 2 de l'avis de fusion (deux listes, deux partitions) : `docs/notes/memoire-conception-v1/fusion-etape-2-deux-listes-deux-partitions-v1.md` (`f859d691…`), acceptée par la mère ; D-1 (a), D-2 (a), D-3, D-4 accordées.
- Versement du contenu neuf du 22 novembre vers le journal des idées : candidats v2 (79 lignes, `7942a069…`) acceptés sous conditions, versés sur main par la mère (`cb50cb69`) ; import par le cycle de veille après mise en service et validation de l'extrait.
- Outils de l'étape 4, dans `fusion-outils-v1/` : listes de lecture v3, partition du journal v3, manifestes v2, recherche bornée v7 (identité par l'environnement posé par le lanceur, journal chaîné à chemin fixe, témoin, verrou), porte de périmètre v2 (journée jugée contre le fichier des sessions de la mère). Contre-lectures et vérifications par un autre modèle versées ; aucun défaut restant (vérification de la recherche v7). Essais : 124 (outils) et 15 (porte, dont 16 lectures parallèles), tous passés ; mutations confirmées.
- Mandat pour Fable des épreuves A (banc planté de l'extraction) et B (mécanisme des retours) : `mandat-fable-epreuves-memoire-du-depot-v1.md` (`3c068ae6…`) ; envoi par la mère selon le quota.

## Reste
- Épreuves A et B : conception par Fable, puis code et essais ici, contre-lus par un autre modèle.
- Index des pistes « dans la liste autorisée v3 » : non fait ; l'index est hors de la liste v3, lu par nom et § 6 seulement. Demander à la mère s'il entre dans la liste stricte.
- Verser sur main les fichiers postérieurs à `cb50cb69` (versions ultérieures des outils, mandat) : à demander à la mère.
- Tests du dépôt entier : la passe complète a été arrêtée deux fois par la limite de temps (600 s, puis la limite des tâches de fond) ; dernière passe arrêtée vers 72 % avec une erreur (E) non identifiée et aucun échec (F) avant ; la première passe en « arrêt au premier échec » s'était aussi arrêtée sur un échec non identifié. Relancer par morceaux (par dossier de tests).

## Réserves
- Ligne Claude-Session fausse (identifiant de la mère) dans le commit `abfe90b0` ; correction par réécriture refusée par le classifieur, ni rejouée ni contournée ; la mère : « ne la réécris pas ».
- Limite déclarée : un agent de même privilège peut poser lui-même les variables MEMOIRE_* ou réécrire journal et témoin de façon cohérente ; la porte ne le voit pas. Seul remède réel : périmètres de session fixés par la plateforme (signalé à la mère).
- Consigne de la mère en vigueur : n'ouvrir aucun extrait commun avant que le cycle suivant l'ait refait sans la fiche I-0317 (marquée mère) ; la relecture de ses vingt premières lignes revient à un agent neuf, pas à moi.
- Fichier des rôles nommant « bibliothecaire » : l'option `--agent` n'existe plus depuis la recherche v6 ; l'identité vient de MEMOIRE_AGENT, le rôle de MEMOIRE_ROLE (reponse → bras memo) ; un fichier au format v1 doit être refait au format v2 de la porte.
- Cloisonnement : aucun fichier interdit lu ; la trace du sous-agent de versement a été établie sur les seuls chemins de son journal d'outils (`ligne-qui-a-lu-quoi-agent-versement-v1.md`).

## Prochaine action
Relancer les tests par morceaux et nommer l'erreur ; puis la réponse de la mère sur l'index des pistes et le versement sur main.

## Instances actives
Aucune.
