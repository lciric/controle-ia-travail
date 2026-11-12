# Serveur de la course v67, session du poste local (GO-2026-11-12-06) — v1-bis

Fiche complète du serveur créé sous la consigne `consigne-poste-local-course-v67-v4.md` (`7349680b…`, mandat, point 3).
**Pourquoi « bis »** : la fiche `poste-local-serveur-v1.md`, poussée au commit `2744efaed` dans les 11 s qui ont suivi la création, est
**vide (0 octet)** : une erreur de substitution du gabarit de l'interpréteur de commandes a vidé le fichier avant son scellement
(l'identifiant figure dans le message de ce commit) ; elle n'est pas réécrite (R12). Heures relevées par `date -u`.

| point | valeur |
|---|---|
| identifiant | **175834755** |
| nom | `organisme-v67-course` |
| type, image, lieu | cpx32, debian-13, hel1 |
| création (API) | 2026-11-12T14:01:34Z |
| fiche bis écrite à | 2026-11-12T14:02:25Z |
| prix horaire | 0.0577200000000000 EUR TTC (API `server_types`, hel1) ; IPv4 primaire 0.0009600000000000 EUR/h TTC (API `pricing`) |
| GO | GO-2026-11-12-06 (commande de création citant `GO_ID=GO-2026-11-12-06` ; étiquette `go=GO-2026-11-12-06`) |
| clé SSH Hetzner | 132525071 (`organisme-v67-course-cle`, partie privée dans le bac à sable du poste, jamais versée) |

Destruction : `DELETE https://api.hetzner.cloud/v1/servers/175834755` (et `DELETE /v1/ssh_keys/132525071`).
