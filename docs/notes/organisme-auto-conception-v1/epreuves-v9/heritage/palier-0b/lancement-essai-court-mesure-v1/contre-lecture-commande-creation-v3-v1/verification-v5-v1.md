# Seconde vérification : commande v5 — v1

Même contre-lecteur Opus. Rapport recopié tel quel.

Verdict : Conforme avec réserves. Les points 2, 3 et 4 sont corrigés, rien d'autre ne change que ce que la v5 déclare, et les trois commandes sont inchangées.

1. **Diff v4→v5.** Seules changent les lignes 1, 3, 22, 47 et 54, la section « Repli » et la section « Différence avec la v4 » : tout est déclaré. Les empreintes concordent : v5 `49420292…`, rapport sur la v4 recopié `57c4d494…`.
2. **La reprise passe les contrôles.**
   - `/home/user/essai-3-sortie-r1` est un chemin absolu, hors de tout dépôt git, et neuf : le `mkdir -m 700` puis le `stat` s'y appliquent.
   - Le fabricant ne refuse en 4 que sur les six fichiers de ce dossier, et l'outil ne refuse en 2 que sur des relevés existants. Un dossier neuf passe les deux.
   - Réserve : un échec 21 (délai dépassé ou coupure réseau) peut cacher un serveur bel et bien créé. Il faut lister les serveurs Hetzner avant toute reprise. Sinon, la machine fantôme pousse sur la branche, et la reprise est refusée en 8 par le contrôle de branche.
3. **Le repli est unique (ligne 54 et section « Repli »), avec une réserve.** Le fabricant écrit en dur `/home/user/controle-ia-travail/…` (le dossier des pièces, ligne 37, et l'interpréteur, ligne 109). Les commandes ne sont donc jouables sur le poste de Lazar que s'il a la même arborescence. Sinon, il faut une autre version de la commande. Il faut l'écrire.
4. **Le retrait est prévu dans tous les cas (ligne 47), y compris un refus du contrôle à blanc.** Le cas « la commande 1 échoue après avoir écrit `SORTIE` » est déjà couvert par le fabricant, qui retire lui-même les fichiers qu'il a créés (ligne 28). La règle est sans effet, mais sans danger.

## Suite donnée
Réserves des points 2 et 3 reprises dans `commande-creation-production-essai-3-v6.md` ; renvoyée au même contre-lecteur pour ces deux points seulement.
