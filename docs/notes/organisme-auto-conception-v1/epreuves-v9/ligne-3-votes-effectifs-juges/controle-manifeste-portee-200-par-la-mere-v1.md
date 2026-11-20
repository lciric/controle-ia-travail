# Contrôle du manifeste de la mesure « portée à 200 » par la mère (additif 3, § 6, point 3) — v1

Fait par la mère (`session_01QPDgKgejkqwnuaJHJ31Ydo`) le 20 novembre 2026, sur le seul manifeste de la mesure et celui du chronométrage, **sans ouvrir le fichier de résultat**. Additif 3 v3 scellé (`71b7a876…`), additif 5 scellé (`581e97e5…`).

| point du § 6, 3 | attendu | manifeste | |
|---|---|---|---|
| `programme_sha256` | `79865552dd666ea6…` (additif 5) | `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7` | égal |
| empreinte du chronométrage | `6b9d2cbfd9bbf638…` (additif 5) | `programme_chronometrage_sha256` du manifeste de chronométrage : `6b9d2cbfd9bbf638d30c0d314531de510d85a4a2b28c8da40100ec8c7be51b90` | égal |
| `autorisation` | chemin absolu de l'additif 5 scellé et HEX | `/home/user/controle-ia-travail/prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md`, `581e97e5fb6d390378ce94f32f0057b55afa77ce1831d480f4b317c1c0eaa34c` | égal |
| configuration | la constante `CONFIGURATION_PORTEE_200` du code (n = 200, 2 000 répliques, 2 000 tirages de rééchantillonnage, écarts 0,05 / 0,10 / 0,15, lois 1 et 3, sept ρ, trois ρ′) | mêmes valeurs ; `configuration_sha256` `1652218c64f00a6f…`. Aucune empreinte attendue n'est écrite dans les additifs : la configuration est une constante du programme, fixée par `programme_sha256` | conforme, réserve de forme |
| racines | 2026112032 et 2026112033, elles seules | `racine_des_tirages` 2026112032, `racine_du_reechantillonnage` 2026112033 | égal |
| table des clés | table gelée, inchangée ; clés 2 et 12 | quatorze clés, `monde_de_puissance` 2, `reechantillonnage_monde_de_puissance` 12 | égal |
| dérivations | deux, de 210 enfants | clé 2 sur 2026112032, 210 enfants ; clé 12 sur 2026112033, 210 enfants | égal |
| `dossier_du_code_propre` | vrai | `True` | égal |
| empreinte du résultat | égale à son compagnon | `afcb453acbb7dd883f040ce6e4b11cd83d2f86facf17a976621249ab31d2d174`, compagnon « OK » (`sha256sum -c`) | égal |

Autres : texte qui fait foi `4e3680d9…` et additif `71b7a876…` cités ; commit du dépôt à l'exécution `995aa45f…`, qui descend de `cce6f234…` (vérifié) ; python3 3.13.18, numpy 2.5.3 ; exécution unique, 11:37:54Z à 11:41:50Z, code 0 ; chronométrage à 11:37:18Z, code 0.

**Conclusion : manifeste conforme ; la lecture du résultat est permise, par l'agent neuf qui prononce (§ 6, « Verdict »), après la faute du banc et l'audit de symétrie.** La mère n'ouvre pas le résultat.
