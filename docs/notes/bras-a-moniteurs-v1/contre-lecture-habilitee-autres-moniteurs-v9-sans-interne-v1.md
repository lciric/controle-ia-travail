# Contre-lecture habilitée du module des cinq moniteurs, version 9 — sans interne — v1

Écrit par le lecteur habilité côté moniteurs du bras A (Claude Fable 5.2, accord de Lazar GO-2026-11-20-21), le 20 novembre 2026. Aucun seuil, trait, vocabulaire, poids ni texte de consigne de moniteur ; rien sur ce que lit quel moniteur. Ce qui fonde chaque ligne est dans la pièce interne `docs/notes/bras-a-moniteurs-v1/contre-lecture-habilitee-autres-moniteurs-v9-v1.md`, qui ne sort pas. La session principale relit cette pièce avant de la transmettre.

**Objet.** Module `src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v9.py`, `08a8f5c532e350045b0ab8a640525f6f839f47a2a9dc48dad6655b1dec9b13d2`, commit `92842ac54` ; ses essais, `b0d505933a7514ff6bc4e2078435280a898134c7725fb2516c93fb208c8cefda`. Réponses du développeur sans interne, v2 : `1959a0be4d74c7039a6e72d04f53bb4f57ca71545050d0d70bd6f0e6e6b7b9f7`.

## Verdict : **conforme après ces corrections**

Aucun calcul n'est faux. Quatre corrections de forme sont demandées au développeur ; aucune ne touche un calcul de moniteur. La version qui fera foi sera donc la suivante, non la version 9.

## Demandes du développeur dites levées

| demande | réponse du contre-lecteur |
|---|---|
| 13 — la clé de provenance | **levée.** Le champ `piece_source.sha256` porte l'empreinte entière du module qui a produit la livraison, calculée sur son fichier à l'exécution. La sortie n'écrit plus aucun chemin de programme : sa garde le refuse, et les sorties de l'épreuve de forme n'en portent aucun. `piece_source.production` porte en plus les empreintes des deux programmes qui ont produit les scores des deux moniteurs à modèle de langue. |
| 1 — cas D | **levée**, conforme à la ligne D de la table des formes de 6.9 |
| 2 — cas E | **levée**, conforme à la ligne E, rédaction (a) |
| 3 — cas C | **levée** : l'aire et les aires des deux plis sont rendues |
| 15 — nom du fichier de sortie | **levée** : `lecture-commune-moniteurs-bras-a.json`, écrit et scellé par le module |
| 16 — épreuve par retrait et notice | **levée** : rejouée par le contre-lecteur, 58 retraits, 58 mordent ; elle couvre l'échange dans chaque paire et ses gardes |
| 17 — épreuve de forme | **levée avec une réserve** : à refaire sur la version corrigée (ci-dessous) |
| 31 — champs de l'agrégateur | **levée** : un nombre, ou `null`, par dose, aux quatre doses, dans les deux champs, toujours |

## Demande 24 (b) du lecteur habilité — attestation

De la version 8 à la version 9, **aucun calcul d'aire, de score, de borne ni de valeur p ne change** (comparaison ligne à ligne des deux fichiers). Ce qui change est la forme d'une lecture : aux cas D et E, la valeur de la famille est la valeur p haute et `calculable` vaut vrai ; au cas C, l'aire est rendue ; au cas B, les deux comptes de permutations sont toujours `null`. L'attestation entre la version 7 et la version qui fera foi reste à écrire, quand cette version existera.

## À inscrire au texte

- **`calculable`** : vrai aux cas A, D et E ; faux aux cas B et C. La table des formes ne fixait pas sa valeur aux cas D et E ; le module rend vrai, puisque l'aire et les valeurs p y sont rendues.
- **Liste fermée de `motif`** : celle de la pièce sans interne v2 du développeur, demande 8 ; toute autre chaîne arrête la lecture.

## Corrections demandées au développeur, dites sans interne

1. La garde de la sortie ne contrôle que les clés de premier niveau de `comptes_des_lectures` et de `preuve_d_ordre` : un texte libre pourrait y passer. Leur forme est à fermer.
2. Dans l'épreuve de forme, deux objets n'ont pas la forme d'une vraie livraison : `comptes_des_lectures` n'y porte qu'une partie de ses clés, et le fichier par unité de chaque cas ne porte les lignes que d'un moniteur sur cinq. **Les sorties de l'épreuve de forme de la version 9 ne doivent donc pas servir à éprouver les contrôles de l'analyse sur ces deux objets** ; l'épreuve est à refaire sur la version corrigée.
3. La garde de forme accepte, au cas A, une borne haute non finie ; elle doit exiger un nombre de 0 à 1.
4. Trois phrases de `nombres_rendus` ne disent plus ce que rend la version 9 ; elles sont à récrire.

## Sur la pièce sans interne v2 du développeur

Relue ligne à ligne contre le code : **aucune fuite**. Une retouche d'exactitude : la version 9 a maintenant un commit, `92842ac54`.

## Rejeu

Essais : `74 passed`. Épreuve par retrait : 58 sur 58. Sept retraits de plus par le contre-lecteur : cinq mordent ; deux ne mordent pas, l'un parce que la garde est doublée par une autre, l'autre faute d'un artefact (correction 3).

Cette pièce ne dépense rien et n'autorise rien.
