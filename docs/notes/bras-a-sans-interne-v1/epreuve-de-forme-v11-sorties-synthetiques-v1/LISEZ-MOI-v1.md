# Épreuve de forme de la lecture commune des cinq moniteurs, version 11 — sorties synthétiques — LISEZ-MOI v1

**Ce sont des cas synthétiques. Aucun score d'épisode réel n'est ici.** Tous les scores sont construits à la main par le programme de l'épreuve (tirages d'une loi fixée, seize tâches factices nommées « tache-forme-00 » à « tache-forme-15 », huit épisodes factices par tâche et par condition), sans moniteur, sans modèle, sans épisode de l'agent. Les empreintes que les fichiers citent sont celles du code et des fichiers factices de l'épreuve.

Versé le 2026-11-22 vers 21:50Z (`date -u`) par un lecteur habilité (Opus 5.5), à la demande de la mère, sur la branche `relance-bras-a/epreuve-forme-v11-sorties-synthetiques`, partie de `main`. Rien d'autre n'est versé sur cette branche.

## D'où viennent ces fichiers

- Programme : l'épreuve de forme de la version 10 (empreinte `41a377e6e455deeee767e712fa027214f0942737700f8d5fe0e76a63f185d130`), rejouée sur la version 11 du module de lecture commune, avec deux changements seulement : le module importé (version 11) et le préfixe d'un dossier temporaire (R-5032).
- Produits le 22 novembre entre 19:51Z et 19:54Z par le vérificateur habilité de la version 11, dans son bloc-notes ; recopiés ici à l'octet. Chaque compagnon d'empreinte a été vérifié avant la copie, et après.
- Six cas : un par ligne de la table des formes (cas A à E), plus l'artefact (le cas A avec une valeur p arrondie, que l'analyse doit refuser). Pour chaque cas A à E : un fichier de la lecture commune et un fichier des rangs par unité ; pour l'artefact : un fichier de la lecture commune.
- Les cinq fichiers des rangs par unité sont identiques, octet pour octet, à ceux versés pour la version 10. Les fichiers de la lecture commune diffèrent de ceux de la version 10 par l'empreinte du module, la version du programme de préparation cité, et ce qui dépend du tirage d'une table neuve à chaque passage (dates, empreintes et comptes) ; rien d'autre.

## Fichiers et empreintes (chacun avec son compagnon `.sha256` dans son dossier)

| fichier | octets | sha256 |
|---|---|---|
| `artefact-cas-a-valeur-p-arrondie/lecture-commune-moniteurs-bras-a.json` | 25599 | `dced25c34acc1fbd7834e88f192f5ef9c379572353521aa459fb7a8798b09bd1` |
| `cas-a/lecture-commune-moniteurs-bras-a.json` | 25614 | `350f9d6b386d94911afff41c52f3173be80e502c38027b3f24149127a435407a` |
| `cas-b/lecture-commune-moniteurs-bras-a.json` | 24346 | `4abb5ea361e9b4ac2ec15bd75c7ed7b71ad260e321a1d6b49540a5ed469bc4c8` |
| `cas-c/lecture-commune-moniteurs-bras-a.json` | 25250 | `35cdbef38edc67cb9eaaa0e5ad04001acaf60db30d200fdbc9e34b9a705d2564` |
| `cas-d/lecture-commune-moniteurs-bras-a.json` | 25863 | `d81ab885565b1c65f8345a9c8dd76929114a09b57cf17bb7113fb04caa39baa3` |
| `cas-e/lecture-commune-moniteurs-bras-a.json` | 25644 | `3fddd217143cd3e1ce88330c308c09b4241184dff83acae4e547be49964988ab` |
| `unites-cas-a/rangs-par-unite-moniteurs-bras-a.jsonl` | 1767200 | `07b6b6f0f2212b96f9c8280cc40cd51f2755f3277b050220fa07f4f752101aca` |
| `unites-cas-b/rangs-par-unite-moniteurs-bras-a.jsonl` | 1320504 | `ba10697740bd9abd457477482c4bbbac27bd3741126e1b9747462ab73c7840d8` |
| `unites-cas-c/rangs-par-unite-moniteurs-bras-a.jsonl` | 1767200 | `9f4fcbc3c3e7cf8efff5531008bed897968d64fc8bbedb851cd8bb7c158bd34e` |
| `unites-cas-d/rangs-par-unite-moniteurs-bras-a.jsonl` | 329240 | `cefcfd3ae2cbd2030f77c21f25d030950c9de7986bcaa2d3159823fbfc079081` |
| `unites-cas-e/rangs-par-unite-moniteurs-bras-a.jsonl` | 220056 | `d1ebda67ea99e7b53c0d74bccee30668ff8aaeddf2894bf2e8472eac6c33ee33` |
