# Borne de P3 v2 — écart d'exécution déclaré (absent du JSON), v1

Écrit par la session conv-audit le 2 novembre 2026 vers 23:30 UTC, d'après le rapport du rédacteur du calcul (sous-agent ; le JSON `borne-p3-v2.json` porte `ecarts_au_plan` vide).

1. **Premier lancement tué par manque de mémoire** : script `9b3625fd…` (non conservé), tué dans un espace mémoire partagé avec d'autres calculs, **avant d'avoir écrit quoi que ce soit** ; le rédacteur déclare n'avoir rien lu de ce lancement.
2. **Modification du script, sans changement du plan** : le calcul des familles de sondes a été découpé par paquets de 4 (économie de mémoire) ; nombres identiques à l'ancienne version vérifiés sur 2 répétitions (écart 0) ; relance avec le script final `borne_p3_v2.py` (`fa1833fb1c2729851dcd311edc13c21ad0c2f02c37b779a40d7c9eb2a013807f`), durée 1 422 s (22:59 → 23:23 UTC), R = 1 000.
3. **Plan de lecture** `plan-de-lecture-p3-borne-v2.md` (`d50b0f1af8e620068763ed9944dd62d1303a3bceee2cdcac85d34b2cbcb5e65d`) : inchangé ; daté par le commit `e142421f` avant toute sortie du calcul (sorties commitées en `d0ba3b21`). Il n'a pas été contre-lu avant le calcul (correction a posteriori, non aveugle : il connaissait les chiffres de la vérification de la v1, ce qu'il déclare en tête).

Conséquence : aucune citation de la borne v2 hors du dossier de brouillons avant la vérification par un sous-agent neuf.
