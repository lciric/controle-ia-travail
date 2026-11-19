# Rapport de recopie — erratum 1 à l'addendum 1 scellé de la ligne 1, version 2 — v1

Pièce de travail (classe C). Auteur : agent de recopie, modèle L′, écart déclaré sur le précédent de R-3791. Date (temps universel, `date -u`) : 2026-11-19, vers 22:59. Rien lancé ; aucun appel à un fournisseur de modèles ; aucune dépense ; aucun réseau sauf `git fetch origin main` et `git show` ; aucune écriture dans le dépôt ; aucun commit, aucune poussée ; rien touché sous `archives-reponses-modeles/` ; aucun refus d'outil.

## Écart déclaré

Le mandat `mandat-redacteur-erratum-1-addendum-ligne-1-v2-v1.md` est écrit pour un rédacteur neuf (modèle F) ; un agent de recopie le remplace en recopie pure, en écart à la règle « qui conçoit » (R-3735), sur le précédent de R-3791, accordé par la mère vers 22:56Z. Le programme de remplacement demandé par le mandat est remplacé, sur instruction de la mère, par l'outil contre-lu du dépôt `scripts/remplacer_texte_exact_v1.py` (`391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`, conforme à son compagnon). L'en-tête porte « Auteur : agent de recopie, modèle L′, écart déclaré sur le précédent de R-3791 » au lieu de « rédacteur neuf, modèle F ».

## Entrées, empreintes vérifiées par programme

| pièce | sha256 |
|---|---|
| mandat v2 | `4d6fd1f7bbb7e2853502f2dbf454166231ae5be461fd88a82c0229201116e663` |
| erratum v1 (cible, non modifiée) | `a370cf6ac9285c0c933fff299d43d5098f8fcd1432fe57c1db0c38006d2884bb` |
| relecture | `48f14f5c068ad0784125c4af5425f3afe27e8946d1eaecd806904caa50f988c8` |
| `registres/decisions.md`, `origin/main`, commit `a2be44dbc66426cc7e25ce2e85e5894c04ed0643` (ligne R-3985) | `452a74bf3dd99621119ad587f90e021606c8fba2188add80ef2abf959a8cb268` |

## Remplacements faits (7, par l'outil, journal joint)

1. Titre : « — v1 » → « — v2 ».
2. Statut : « version 1 » → « version 2 ».
3. Auteur : ligne de l'agent de recopie (mandat v2 et relecture cités avec empreinte, version 1 intacte, R12) ; l'ancienne ligne devient « Auteur de la version 1 », inchangée par ailleurs.
4. Date : « version 1 écrite vers 22:32 ; version 2 écrite vers 22:58 ».
5. Table du § 1 : « mandat de cet erratum » → « mandat de la version 1 de cet erratum » ; trois lignes ajoutées (mandat v2, relecture, `registres/decisions.md` sur `main` pour R-3985).
6. Correction 1 de la relecture (§ 2), texte exact, avec le seul renvoi permis par la mère « (rectification R-3985) » inséré après « ce sont ces quatre cellules ».
7. Correction 2 de la relecture (fin du § 3), paragraphe exact ajouté après la phrase citée, séparé par une ligne vide.

Les textes des corrections 1 et 2 ont été contrôlés à l'octet contre la relecture par `verifier_textes_relecture_v1.py` (lancé par son chemin) : « CONCORDE ». L'outil a accepté les sept remplacements au premier passage (code 0).

## Sorties (bloc-notes)

| fichier | sha256 |
|---|---|
| `erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v2.md` | `f66c3ce8682ef1dd9ced3227378eb18041cff41bea76edfeb2c6373d56d1fcf3` |
| son compagnon `.sha256` | `ca9654a4de8635f57a28c243663bb2d9aef96a7f2bf3fdc9b113ad5f77288ab8` |
| journal de l'outil `.journal-remplacements-v1.json` | `b3595bd8a4996cc8a82436e85b5980d3133f5a1cd0469347230f9d6e1076e90a` |
| compagnon du journal | `0fb0d697efb2a52b6b8cba29b7cdeb1f60a0efefcd7f5f6140c9c74c564aaed3` |
| `differentiel-erratum-1-addendum-ligne-1-v1-v2.diff` | `a84e20f76938f607fe6b386773e20ca22a7140589833221a51dd1784c07375d7` |
| `remplacements-erratum-1-addendum-ligne-1-v2-v1.json` | `bd96a54dd1c65316a391980003b71bac140d3d49215b56105decf7cb0a85c0b9` |
| `verifier_textes_relecture_v1.py` | `3df413f77443db2ed9082486579836eac24526f69dd462432bdbebd43eb2591c` |

## Réserve laissée à la mère (rien changé, recopie pure)

Après la correction 2, le § 3 porte deux précisions de lecture. Deux phrases de la version 1, que la relecture ne corrige pas, deviennent inexactes à la lettre : le chapeau dit « porte une seule précision de lecture (§ 3) », et le titre du § 3 nomme seulement le § 9, point 5. Le mandat dit « rien d'autre ne change » : elles sont laissées telles quelles. C'est à la mère de dire si une tenue est due, sous un texte exact donné.
