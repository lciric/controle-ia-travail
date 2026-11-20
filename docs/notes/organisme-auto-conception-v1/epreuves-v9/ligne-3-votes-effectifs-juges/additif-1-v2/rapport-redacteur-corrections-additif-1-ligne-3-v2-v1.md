# Rapport du rédacteur — corrections 1 à 6 de l'additif 1 de la ligne 3 (additif v2) — v1

Pièce de travail (classe C). Écrite le 2026-11-20, sur le mandat `mandat-redacteur-corrections-additif-1-ligne-3-v2-v1.md` (`a47f8f044ce3779ace178aacfa78c4576191574ee2074e13c65fd09f164e03ed`, vérifiée par `env -C` et `sha256sum -c` de son compagnon : OK).

## Verdict

Les six corrections de la contre-lecture sont appliquées à la lettre, par l'outil contre-lu, sous des noms neufs. Quinze remplacements : neuf dans l'additif, six dans le rapport. Aucun critère gelé ne change. Un incident, déclaré plus bas : un premier JSON du rapport portait une ancre fausse ; l'outil a refusé sans rien écrire, je me suis arrêté, puis j'ai repris sur le mot de la session.

## Sources vérifiées (empreinte recalculée)

| pièce | sha256 |
|---|---|
| contre-lecture `contre-lecture-additif-1-ligne-3-v1.md` | `f12200ae427da3f3f70d549ac4dfef4feeb805b2279c7a24bf36e86f563d3955` |
| additif v1 | `27ecd5d5a8dba97352cf7ab18dee9ef0b9e3eaa5839122221640ee29be97c89d` |
| rapport du rédacteur v1 | `6c273e5e594035ab73ee8e56a3d18c6d07fefdb99a33e6f31849f841f3dac873` |
| outil `scripts/remplacer_texte_exact_v1.py` | `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6` |

Python 3.13.18.

## Pièces rendues (dans mon dossier, chacune avec son compagnon, compagnons vérifiés par `sha256sum -c`)

| pièce | sha256 |
|---|---|
| `additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md` | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` |
| `rapport-redacteur-additif-1-ligne-3-v2.md` | `492cde9452b013230a004b5d6e1bbcd300afd3e8ceeccc36232df681a4a46bcd` |
| `remplacements-additif-1-ligne-3-v1-vers-v2.json` | `74b629e14a065b3aebe521a6542cf7fef5531eb754414679bb2f7677be4d3f58` |
| `remplacements-rapport-redacteur-additif-1-ligne-3-v1-vers-v2-b.json` | `bee95353fb62cf632f49380ae46a2a00e08ce7a12a3dce29b381948ff1fed0d4` |
| `additif-1-preenregistrement-ligne-3-votes-effectifs-juges-v7-v2.md.journal-remplacements-v1.json` | `6c61ec89dfad816d55e1d7aad379213d792930ed2272b41f8d8aad6d033e14ad` |
| `rapport-redacteur-additif-1-ligne-3-v2.md.journal-remplacements-v1.json` | `a72e1f950db1743e38ed99a0e1528c2c0f603cc3ec7cf78f17395e05c071803e` |
| `differentiel-additif-1-ligne-3-v1-vers-v2.diff` | `5858efb7c9d3ee0b20b0d5a8249f5c53b81a306151570af486dfbaca7ee7fa99` |
| `differentiel-rapport-redacteur-additif-1-ligne-3-v1-vers-v2.diff` | `3bfc11946a3cd78cc96b8799b77e4bcc463c05ff4bf54cbf0c72ff6c829dfcf1` |
| `remplacements-rapport-redacteur-additif-1-ligne-3-v1-vers-v2.json` (JSON fautif, gardé, non réemployé) | `f21632cb3b92ae4c81c5a55795afc472bdcffaa01a16858a34eb657c1ff3a2a5` |

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/227b647d-2ece-5654-bf04-8493b3ed2f19/scratchpad/redacteur-additif-1-ligne-3-v2/`.

## Les quinze remplacements

**Additif (9).**
1. Titre : « — v1 » devient « — v2 ».
2. Ligne de version, ajoutée après « recalculée égale à son compagnon). » : empreintes de la v1 et de la contre-lecture, ce que la v2 porte, ce qui reste.
3. Correction 1 (règle C, point 1).
4. Correction 2 (règle B, « Pourquoi ρ′ = 0 »).
5. Correction 4, début du point 6 de la règle D (bras A).
6. Correction 4, fin du même point 6 (référence à zéro erreur).
7. Correction 5, phrase de P6 (règle du silence 2).
8. Correction 5, « le mot de P6 » au point 2 de « Ce que le code doit changer ».
9. Correction 6, côté additif (cinq comptes).

**Rapport (6).**
1. Titre : « — v1 » devient « — v2 ».
2. Ligne de version, ajoutée après « égale à son compagnon). ».
3. Tenue : au « Verdict », le nom de l'additif passe à `…-v7-v2.md` (accepté comme tenue par la session).
4. Point B : une phrase ajoutée, qui suit le jugement de la contre-lecture (question de conception, non un nœud ; raisonnement juste en moyenne, non démontré sur la loi entière ; option (b) presque gratuite en calcul, son vrai coût étant le code, les essais et leur vérification).
5. Correction 3 (nœud éventuel, inconvénient de l'option (b)).
6. Correction 6, côté rapport (cinq comptes).

Les textes anciens et neufs des corrections sont copiés de la contre-lecture. L'outil n'a rendu aucun avertissement. Les deux différentiels, relus en entier, ne montrent que ces quinze zones.

## Incident déclaré

Le premier JSON du rapport portait, pour la ligne de version, l'ancre « `f4ace`, égale à son compagnon). » : la fin d'une mauvaise empreinte (celle du mandat du contre-lecteur, citée dans la contre-lecture). La ligne 3 du rapport v1 finit par « `…fa894972`, égale à son compagnon). ». L'outil a refusé (code 2, « trouvé 0 fois dans la cible »), sans rien écrire. J'ai lu la règle « au premier refus d'un outil : arrête-toi » à la lettre, je me suis arrêté et je l'ai dit. La session a répondu que la règle vise un refus de permission ou de classifieur, non la validation propre de l'outil, et m'a fait reprendre : JSON neuf (`…-v2-b.json`), ancre corrigée, chacune des six ancres comptée une fois par `grep -c -F` sur le rapport v1 avant l'appel, puis l'outil : six remplacements, fait. Le JSON fautif reste dans mon dossier, avec son compagnon, non réemployé.

## Ce que je laisse tel quel, à dessein

- Dans l'additif v2, la phrase de statut « à contre-lire (règle R2), puis à sceller… » n'est pas touchée ; la ligne de version dit que la contre-lecture est faite.
- Dans le rapport v2, la section « Ce qui reste à faire » nomme encore la contre-lecture ; la ligne de version dit qu'elle est faite.
- Les empreintes citées dans les deux pièces pour le texte v7 et la tête de main sont celles de la v1, non relues par moi.

## Ce que je n'ai pas fait, refus et écarts

Aucun calcul de l'étage 1, aucun tirage, aucun essai. Aucune écriture dans le dépôt, aucun commit, aucune commande `git`. Rien sous `archives-reponses-modeles/` ni sous `/root/.claude/`. Aucun appel à un fournisseur, aucune dépense. Aucun refus de permission ni de classifieur. Seul écart : l'incident ci-dessus.

Rédacteur neuf, modèle F.
