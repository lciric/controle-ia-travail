# Course 1, tentative 2 — Kimi K3.1 Pro, troisième juge (lecture complémentaire) — v1

session-depot, 30 octobre 2026, 11:51 UTC. GO-2026-10-30-09 ; mot de Lazar : « demande à Kimi de juger les fiches de la course 1 ».

**Montage.** Kimi reçoit la consigne exacte d'Argon (`traces-argon-juge/consigne.md`, `6fd2277d…`, 851 581 octets) : mêmes 29 fiches, même anonymisation, mêmes 6 témoins v1.
- Chaîne d'envoi : `commande_kimi_v1.py`, puis le relais Kimi v3 (amont en flux, délai 1 800 s).
- Notes lues par les fonctions de la v52 (`extraire_bloc_json`, `valider_notes`) avec la clé d'anonymisation d'Argon (`lire_juge_kimi.py`).
- Le classement de la course n'est pas réécrit : c'est une lecture complémentaire.

**Appel.**
- De 11:37:30 à 11:50:16 UTC, 765 s ; statut 200 ; modèle servi `kimi-k3.1-pro` (conforme).
- 222 635 jetons d'entrée, 31 010 de sortie (plafond 32 768) ; **0,755 USD**.
- Premier essai (`juge-kimi-course-1-v1`, relais v2) : coupé à 300 s, 2,03 USD comptés au pire cas.

**Résultats** (`lecture-kimi-v1.json`). Total moyen par auteur, sur 15 :

| Juge | Fiches de Fable | Fiches d'Argon | Écart Argon − Fable |
|---|---|---|---|
| Kimi K3.1 Pro | 9,33 | 8,79 | −0,55 |
| Opus 5.5 | 10,73 | 10,00 | −0,73 |
| Argon | 11,93 | 13,14 | **+1,21** |

**Lecture.**
- Les deux juges sans fiche à eux, Kimi et Opus, notent tous deux Fable un peu au-dessus d'Argon.
- Argon seul note ses propres fiches au-dessus. L'**auto-préférence d'Argon** vaut environ 1,2 + 0,6 ≈ **1,8 point sur 15** par rapport aux deux juges neutres. C'est une différence de différences, à 14 et 15 fiches, sans intervalle de confiance.
- **Doublons** : Kimi signale exactement les 12 paires entre passes que les deux autres juges ont signalées, plus les témoins jumeaux.
- **Témoins** : Kimi déclare éligible le témoin p0-06, que les deux autres juges ont écarté (attendu : inéligible). Kimi échoue donc sur un témoin sur six.
- **Accord de rang** (Spearman sur les totaux des 29 fiches) : Kimi et Opus 0,30 ; Kimi et Argon 0,39 ; Opus et Argon −0,20.
- **Dix premières selon Kimi** : argon-p2-08 et fable-p1-01 (11), puis huit fiches à 10. Les deux premières du classement de la course y sont les deux premières.
