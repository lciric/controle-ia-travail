# Pièce 5 — Esquisse de devis de l'exécution des épreuves de l'oracle, cycle 1 du scellement 2 — v1

- **En clair : aucun contenu de mode.** Rangée au coffre avec les autres pièces du monteur ; peut en sortir telle
  quelle si la mère le décide. Ce n'est pas un devis : aucun prix n'est relevé, aucune dépense n'est engagée. Un devis
  chiffré, contre-lu, porté à Lazar, précède tout lancement.
- Écrite le 2026-11-21 par le monteur de l'oracle du cycle 1 (`session_01Qi7Gr4BDyW322Ljw2o29ZT`).
- Les volumes sont des ordres de grandeur. Les prix sont des lettres. Les comptes de tâches et de directions sont faits
  par programme sur les fichiers du banc (`taches-entrainement.json`, `8d20a698d76baa8a…` ;
  `taches-evaluation.json`, `76cdeace861d2fff…`).

## 1. Postes

| n° | poste | volume | unité de coût | qui |
|---|---|---|---|---|
| 0 | code de l'oracle, tests, contrôle côté agent, altérations par programme | — | processeur, sans dépense | monteur |
| 1 | épisodes honnêtes réservés sur les 32 tâches d'épreuve | 64, plus au plus 32 en complément | heures de carte : 64 × `N` × `T` actions du modèle de l'agent (`a` par épisode) | lanceur du banc |
| 2 | énoncés neutres de la référence | 96 appels (un par tâche), environ 1 500 jetons d'entrée et 600 de sortie chacun | `p_e`, `p_s` du modèle de la main neuve | main neuve |
| 3 | épreuve de neutralité | 96 appels, environ 600 jetons d'entrée et 100 de sortie | idem, modèle d'un lecteur | lecteur neuf |
| 4 | lectures par les deux lecteurs : plans intacts et plans des épreuves 1 à 5 et 7 | environ 64 + 32 + 60 + 32 + 32 + 32 + 32 = 284 plans par lecteur, soit 568 appels ; environ 4 500 jetons d'entrée et 800 de sortie par appel | `p_e¹`, `p_s¹`, `p_e²`, `p_s²` | lecteurs |
| 5 | épreuve d'aveuglement | environ 2 × 2 × 124 = 496 appels courts, environ 4 000 jetons d'entrée et 30 de sortie | idem | lecteurs |
| 6 | ancre | environ 20 plans, 20 appels de la taille du poste 4 | modèle de l'agent de l'ancre | agent neuf |
| 7 | dose flagrante et niveau « tous » | — | processeur, sans dépense | autre main |
| 8 | contrôle côté moniteurs | une question | sans dépense | concepteur de moniteurs |

## 2. Totaux en jetons, ordres de grandeur

- Lecteurs (postes 3 à 5) : environ 568 × 4 500 + 496 × 4 000 + 96 × 600 ≈ 4,6 millions de jetons d'entrée, et
  568 × 800 + 496 × 30 + 96 × 100 ≈ 0,48 million de jetons de sortie, répartis à peu près par moitié entre les deux
  lecteurs.
- Main neuve (poste 2) : environ 0,15 million d'entrée et 0,06 million de sortie.
- Ancre (poste 6) : environ 0,09 million d'entrée et 0,02 million de sortie.
- Relances (au plus une par appel) : marge de 10 % sur chaque poste.
- Coût des lectures ≈ 1,1 × Σ (jetons d'entrée × `p_e` + jetons de sortie × `p_s`) par modèle ; coût du poste 1 =
  heures de carte × prix horaire `g`.

## 3. Ordre, chacun sur son mot de Lazar

1. Poste 0 (déjà fait, sous contre-lecture), puis épreuve 8 et contrôle côté agent : processeur seul.
2. Poste 8, question seule.
3. Postes 2 et 3 (énoncés neutres et leur neutralité). Arrêt si l'épreuve de neutralité échoue.
4. Poste 1, puis lecture des plans intacts (part du poste 4) : nul et préconditions. Arrêt si une précondition échoue.
5. Altérations (postes 0 et 7), puis le reste du poste 4, poste 5, poste 6. Arrêt à la première épreuve échouée.

## 4. Réserves

- Aucun prix vérifié ; aucun chiffre opposable hors des comptes de tâches et de directions.
- Les jetons par appel sont estimés depuis la longueur des énoncés et du format des propositions ; ils se remplacent
  par une mesure sur dix épisodes honnêtes existants avant le devis.
- Les modèles des lecteurs ne sont pas encore choisis (pièce 2, section 7).
