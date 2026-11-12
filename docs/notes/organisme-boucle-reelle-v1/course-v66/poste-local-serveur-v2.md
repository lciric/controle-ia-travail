# Serveur de la course v66, session du poste local (GO-2026-11-10-11) — v1

Écrit dans la minute qui suit la création, pour que la session mère puisse détruire le serveur par son identifiant si la
session du poste s'interrompt (consigne `consigne-poste-local-course-v66-v3.md`, mandat, point 3). Heures relevées par `date -u`.

| point | valeur |
|---|---|
| identifiant | **175792062** |
| nom | `organisme-v66-course` |
| type, image, lieu | cpx32, debian-13, hel1 |
| création (API) | 2026-11-12T07:53:06Z |
| écrit à | 2026-11-12T07:53:06Z |
| prix horaire | 0.0577200000000000 EUR TTC (API `server_types`) |
| GO | GO-2026-11-10-11 (commande de création citant `GO_ID=GO-2026-11-10-11` ; étiquette `go`) |
| clé SSH Hetzner | 132513543 (`organisme-v66-course-cle`, partie privée dans le bac à sable du poste, jamais versée) |

Destruction : `DELETE https://api.hetzner.cloud/v1/servers/175792062` (et `DELETE /v1/ssh_keys/132513543`).
