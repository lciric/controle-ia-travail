# Erratum — heures d'écriture fausses dans quatre en-têtes du 27 octobre — v1

Lignée conv-audit, écrit le 27 octobre 2026 à 13:00 UTC (heure lue sur `date -u` : 12:59:50 juste avant). **Mon erreur** :
dans quatre en-têtes, j'ai écrit une heure « lue sur `date -u` » sans l'avoir lue ; elle est fausse (postérieure au
commit qui porte le fichier, ou trop tardive). Les fichiers restent tels quels (R12) ; voici les heures sûres, bornées
par l'heure de leur commit (`git log`, UTC) :

| fichier | heure écrite dans l'en-tête | heure sûre |
|---|---|---|
| `orchestrateur-pole-v3/LISEZMOI-orchestrateur-pole-v3-v1.md` | 12:22 UTC | avant 12:21:48 UTC (commit `3851b0f`) |
| `demonstration-cycle-v3/lecture-demonstration-cycle-v3-v1.md` | 12:28 UTC | avant 12:25:19 UTC (commit `dded695`) |
| `orchestrateur-pole-v4/LISEZMOI-orchestrateur-pole-v4-v1.md` | 12:48 UTC | avant 12:44:12 UTC (commit `b357564`) |
| `orchestrateur-pole-v5/LISEZMOI-orchestrateur-pole-v5-v1.md` | 13:05 UTC | avant 12:58:14 UTC (commit `0f4f297`) |

Aucun chiffre ni aucun résultat n'en dépend. Désormais, chaque heure d'en-tête est lue sur `date -u` dans la commande qui
précède l'écriture.
