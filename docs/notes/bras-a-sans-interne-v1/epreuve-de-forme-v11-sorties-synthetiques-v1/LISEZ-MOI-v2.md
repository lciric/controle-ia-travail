# Épreuve de forme de la lecture commune des cinq moniteurs, version 11 — sorties synthétiques — LISEZ-MOI v2

**Ce sont des cas synthétiques. Aucun score d'épisode réel n'est ici.** Tous les scores sont construits par le programme de l'épreuve (seize tâches factices « tache-forme-00 » à « tache-forme-15 », huit épisodes factices par tâche et par condition), sans moniteur, sans modèle, sans épisode de l'agent.

La v2 remplace la v1 comme guide (la v1 reste, inchangée, avec son compagnon) et ajoute un artefact neuf. Écrit le 2026-11-22 vers 22:03Z (`date -u`) par un lecteur habilité (Opus 5.5), à la demande de la mère.

## Ce que la v1 disait, toujours vrai

Six cas versés le 22 novembre vers 21:50Z : les cas A à E de la table des formes et l'artefact de la valeur p arrondie, produits par l'épreuve de forme de la version 10 (empreinte `41a377e6e455deeee767e712fa027214f0942737700f8d5fe0e76a63f185d130`) rejouée sur la version 11 du module (R-5032).

## Ce qu'ajoute la v2 : un artefact qui éprouve la garde du demi-pas

L'artefact de la v1 (valeur p haute du juge à la dose ½ arrondie à quatre décimales) reste à moins d'un demi-pas de sa formule. Il est refusé par l'égalité exacte de la valeur qui entre dans la famille, et non par la garde du demi-pas : il n'éprouve pas celle-ci.

L'artefact neuf part de la sortie saine du cas A, octet pour octet, et ne change que deux lignes de la même lecture : la valeur p haute du juge à la dose ½, écartée de sa formule de plus d'un demi-pas sans franchir aucun des quinze niveaux de Holm, et la valeur de la famille, écrite à l'identique pour que l'égalité exacte passe.

Rejoué par la règle de discrétion de l'analyse de la relance, version 13 (branche `claude/pensive-bardeen-1fv7hw`, tête `1b4a272dc`), sous une configuration et un constat de lancement fabriqués par l'aide des essais de la version 13, dans un dossier temporaire :
- **cas sain** (sortie du cas A) : lu ; aucune condition de l'écart des valeurs p en défaut ;
- **artefact neuf** : arrêt de la lecture, garde de forme, champ de la valeur p haute, cas A, juge, dose ½ ; la seule condition en défaut est celle du demi-pas ;
- **retrait** : la garde du demi-pas neutralisée, l'artefact est lu en entier ; aucune autre garde ne le refuse.

Programme : `artefact_demi_pas_v1.py` (versé ici ; aussi sur la branche habilitée). Relevé : `releve-rejeu-artefact-demi-pas-et-cas-sain.json`. Le programme refuse d'écrire dans un dossier existant (R12).

## Fichiers et empreintes (chacun avec son compagnon `.sha256` dans son dossier)

| fichier | octets | sha256 |
|---|---|---|
| `artefact-cas-a-valeur-p-arrondie/lecture-commune-moniteurs-bras-a.json` | 25599 | `dced25c34acc1fbd7834e88f192f5ef9c379572353521aa459fb7a8798b09bd1` |
| `artefact-cas-a-valeur-p-hors-du-demi-pas/lecture-commune-moniteurs-bras-a.json` | 25582 | `8ab68ced958eb81a7e444e9ccf056fce3244dbfbdff6acd23e88bb0485221777` |
| `artefact_demi_pas_v1.py` | 8193 | `48032930ee62c86044276887ae75460e4958bc253d5a98a723345d05e86c2555` |
| `cas-a/lecture-commune-moniteurs-bras-a.json` | 25614 | `350f9d6b386d94911afff41c52f3173be80e502c38027b3f24149127a435407a` |
| `cas-b/lecture-commune-moniteurs-bras-a.json` | 24346 | `4abb5ea361e9b4ac2ec15bd75c7ed7b71ad260e321a1d6b49540a5ed469bc4c8` |
| `cas-c/lecture-commune-moniteurs-bras-a.json` | 25250 | `35cdbef38edc67cb9eaaa0e5ad04001acaf60db30d200fdbc9e34b9a705d2564` |
| `cas-d/lecture-commune-moniteurs-bras-a.json` | 25863 | `d81ab885565b1c65f8345a9c8dd76929114a09b57cf17bb7113fb04caa39baa3` |
| `cas-e/lecture-commune-moniteurs-bras-a.json` | 25644 | `3fddd217143cd3e1ce88330c308c09b4241184dff83acae4e547be49964988ab` |
| `releve-rejeu-artefact-demi-pas-et-cas-sain.json` | 514 | `615d1bb149db64ead6db371128f380f3809cf122d88cd417f3bd1f72c975e2a7` |
| `unites-cas-a/rangs-par-unite-moniteurs-bras-a.jsonl` | 1767200 | `07b6b6f0f2212b96f9c8280cc40cd51f2755f3277b050220fa07f4f752101aca` |
| `unites-cas-b/rangs-par-unite-moniteurs-bras-a.jsonl` | 1320504 | `ba10697740bd9abd457477482c4bbbac27bd3741126e1b9747462ab73c7840d8` |
| `unites-cas-c/rangs-par-unite-moniteurs-bras-a.jsonl` | 1767200 | `9f4fcbc3c3e7cf8efff5531008bed897968d64fc8bbedb851cd8bb7c158bd34e` |
| `unites-cas-d/rangs-par-unite-moniteurs-bras-a.jsonl` | 329240 | `cefcfd3ae2cbd2030f77c21f25d030950c9de7986bcaa2d3159823fbfc079081` |
| `unites-cas-e/rangs-par-unite-moniteurs-bras-a.jsonl` | 220056 | `d1ebda67ea99e7b53c0d74bccee30668ff8aaeddf2894bf2e8472eac6c33ee33` |

Guide précédent : `LISEZ-MOI-v1.md`, `56ce0d1da99a407b24d550fc2bef83d3c3a62611dc464a836122b00fc777f86c`.
