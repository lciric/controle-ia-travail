# Rapport du rédacteur — additif 3 de la ligne 3, portée à 200 témoins — version 2 — v1

Pièce de travail (classe C), 2026-11-20. Rédacteur, modèle F, le même que pour la version 1. Rien écrit dans le dépôt, aucun commit, aucun lancement du banc, aucune graine dérivée, aucun appel de modèle, aucune dépense, aucune mesure de l'étage 1 ouverte, aucun refus d'outil.

## Verdict

La version 2 est écrite : `additif-3-preenregistrement-ligne-3-portee-200-v2.md`, `bea75ff2b970f9cb344c241bccc63335289b27a97868b7543f5a6dd69a896b94`. Elle porte à la lettre les corrections 1 à 3 de la contre-lecture, et rien d'autre que la tenue de version. À contrôler sur le différentiel, puis à sceller par la mère.

## Ce qui a été fait

- Contre-lecture `contre-lecture-additif-3-portee-200-v1.md` : `f264cf9e8c8fca02a308e6831963ab55672f77017e522c653fa2ac2c08b57082`, égale à son compagnon (`sha256sum -c`), lue en entier.
- Outil `scripts/remplacer_texte_exact_v1.py` : `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`.
- Cinq ancres comptées par `grep -c -F -e` dans la version 1 (`9e189f1a…`) avant l'appel : chacune rend 1.
- Un seul appel de l'outil : « FAIT : 5 remplacement(s) ».

| n° | lieu | nature |
|---|---|---|
| 1 | titre | tenue : « v1 » devient « v2 » |
| 2 | ligne de statut | tenue : « version 2 », « Contre-lue (règle R2) ; à sceller par la mère, après contrôle du différentiel », et la phrase de version, de ma main |
| 3 | § 0, deuxième puce | correction 1, texte neuf du contre-lecteur, mot pour mot |
| 4 | § 4.2, ligne « l. 241, l. 305 (5) et (7) » | correction 2, mot pour mot |
| 5 | § 6, audit de symétrie | correction 3, mot pour mot |

Le différentiel montre cinq lignes changées, et aucune autre. Aucun chiffre de la mesure, aucune graine, aucune règle de lecture, aucun montant ne bouge. Les quatre nœuds de Lazar et le point de procédure pour la mère sont inchangés : je n'ai repris aucune des recommandations ni des remarques non exigées du contre-lecteur.

## Réserves

- La phrase de version et les mots du statut sont de ma main : à contrôler.
- La section « Pièces lues » de l'additif n'est pas complétée (la contre-lecture et l'outil sont nommés ici et à la ligne de statut) : la tenue permise ne couvrait que le titre, la ligne de version et le statut.
- La contre-lecture porte un calcul approché de la puissance à 200 fait par le contre-lecteur. Je l'ai lu ; je n'ai changé ni la prédiction ni sa confiance.

## Pièces et empreintes

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-3-ligne-3/`. Chaque pièce a son compagnon `.sha256`.

| pièce | sha256 |
|---|---|
| `additif-3-preenregistrement-ligne-3-portee-200-v2.md` | `bea75ff2b970f9cb344c241bccc63335289b27a97868b7543f5a6dd69a896b94` |
| `additif-3-preenregistrement-ligne-3-portee-200-v2.md.journal-remplacements-v1.json` | `e76d9fbc5add9ee459c0354d3be9ba54d8e1257026ca5a3000c0d9a1c30590b8` |
| `remplacements-additif-3-v1-v2.json` | `78d3c674c88c2b3de0c8d0ac06ef7d5e51a8d220ca68c058779f307c9fba0084` |
| `differentiel-additif-3-portee-200-v1-v2.diff` | `2da6bdd61c52d89dde9df7fd34bf954d83bfbebde979a589a517449e0e5b6308` |
| `additif-3-preenregistrement-ligne-3-portee-200-v1.md` (inchangée) | `9e189f1af673e07460e96fe17537727f445ee3e415c53cb24429787e9a898915` |

Rédacteur, modèle F.
