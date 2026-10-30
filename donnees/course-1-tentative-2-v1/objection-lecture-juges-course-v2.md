# Objection de lecture — juges de la course 1, tentative 2 (juge externe Argon)

- Lecteur : sous-agent neuf Opus (attestation de lecture, session-depot), non humain.
- Lu le : 2026-10-30T08:35Z (heure universelle).
- Fichier lu : `sortie-course-v2/fiches-validees.json`, empreinte `a7068ba41ec4929edaedf28a5669a6f7d34773445dfad7295b6652085ce3b7f9`, conforme à son compagnon `.sha256`, et égale à l'empreinte fixée dans le lanceur.
- Lecture : les 29 fiches, en entier, tous champs.

## Verdict

**Aucune attestation n'est écrite.** Deux fiches tombent sous le critère (a) : elles nomment une personne privée, et pas comme auteur d'une publication. Le code sert les fiches sans les caviarder : la reconstruction doit être identique octet pour octet, et `caviarder` ne s'applique qu'aux sorties et aux erreurs. Ce nom partirait donc tel quel chez le fournisseur tiers.

| Fiche (identifiant) | Critère | Constat (sans reproduire le contenu) |
|---|---|---|
| `fable-p1-06` (fiche n° 11) | (a) | Le champ `cout.ordre_de_grandeur` cite nommément le directeur du programme comme destinataire d'un nœud de dépense. |
| `fable-p2-01` (fiche n° 22) | (a) | Le champ `demande_organisme.texte` cite nommément le directeur du programme comme destinataire d'un nœud de publication. |

## Les 27 autres fiches

Je n'ai relevé aucun manquement aux critères (a) à (f) dans les 27 autres fiches. On n'y trouve que des noms d'auteurs cités avec leurs publications. Elles ne contiennent ni secret, ni chemin, ni données. Elles évoquent la carte des hypothèses par son nom seulement, sans en donner le contenu. Elles ne décrivent les catégories d'évasion qu'à travers les bancs publiés.

## Pour lever l'objection (proposition, non appliquée)

Il faut décider du traitement de ces deux fiches. On peut les retirer du lot servi, ou faire caviarder le nom en amont. Dans les deux cas, l'empreinte des fiches validées et la consigne changent : il faut une nouvelle version et un nouveau lecteur. La décision revient au directeur. Je n'ai modifié aucun fichier de la course.
