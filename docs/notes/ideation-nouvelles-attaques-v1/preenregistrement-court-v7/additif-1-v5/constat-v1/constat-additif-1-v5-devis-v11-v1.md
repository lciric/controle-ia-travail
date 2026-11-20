# Constat final — additif 1 v5 au préenregistrement court v9 et devis v11 — v1

Pièce de travail (classe C), 2026-11-20, relevé de `date -u` : 14:35:30Z. Contre-lecteur neuf, modèle O, le même que pour la contre-lecture et les vérifications 1 à 3. Mandat `799b14c6…`, en-tête compris. Processeur seul : aucun appel, aucune dépense, aucune écriture dans le dépôt, aucun commit, aucune publication. Rien ici ne porte de méthode d'attaque, de procédé, de nom ou d'énoncé de mode, de case nommée, de valeur de clé ni d'identifiant de modèle. Aucun refus de permission, de classifieur ni de garde.

## 0. Verdict

**Conforme, à sceller.**
- La première passe de chaque pièce est égale, par `cmp`, à mes fichiers d'essai.
- La seconde passe rejoue à l'octet l'additif v5 et le devis v11.
- La seconde passe ne touche que la tenue.

Une condition, portée par le traitement que la mère écrit au scellement, comme pour la v9 (R-4271) : la phrase « La v4 n'est pas vérifiée » de la section « Contre-lecture » de l'additif est remplacée par l'entrée de la vérification 3 et par ce constat. Le texte proposé est au § 3.

## 1. Pièces et contrôles

| pièce | empreinte | contrôle |
|---|---|---|
| étape 1 de l'additif (v4 + X1, X2) | `3682b3c2e6106d10a5df0fb379eef22aebaf06bfea78fed6edc724458c3054d4` | `cmp` égal à mon essai `essai-additif-1-v4-corrige.md` |
| étape 1 du devis (v10 + Y1) | `e869d1835bf6e3183330d6f56093b507bc7a10ebf27acadeca28004818b6b7b6` | `cmp` égal à mon essai `essai-devis-v10-corrige.md` |
| jeu de tenue de l'additif | `9d514d589290855be49dcc7af43868538c4027fe2bab0019caca6163f3baec24` | 9 remplacements rejoués sur mon essai ; sortie `472c2adf…`, égale à l'additif v5 (`cmp`) |
| jeu de tenue du devis | `1b8c98d083c73a6137d2f10575b7fed673e305a3926077627a32da0b57e1b0c8` | 3 remplacements rejoués sur mon essai ; sortie `205e08f2…`, égale au devis v11 (`cmp`) |
| additif 1 v5 | `472c2adf8c150b281cdaf1dc01165b50956b3053760c4b7fc4578c25bc4ad53c` | compagnon « OK » |
| devis v11 | `205e08f23ef9ced92a35340b8fad38765b08483a2129ee32550081d1bd043570` | compagnon « OK » |
| différentiels ; rapport | `104458a5…`, `5f1c5a6a…` ; `6bfa66ae95a9b116c49f3778ffa2296d28ba01f3df403b2601f959715b73108f` | recalculées ; compagnon du rapport « OK » |
| vérification 3, au chemin versé | `9e08297c…` | recalculée, égale à celle que la table et les phrases de version citent |

Le rapport dit, à son écart 1, que l'égalité aux essais reste à constater par `cmp` : c'est fait ici.

## 2. La seconde passe ne touche que la tenue

J'ai lu les deux jeux entrée par entrée.
- **Additif, 9 remplacements** :
  - le titre (v4 → v5) ;
  - la date (« Version 5 : 14:32:16Z ») ;
  - le statut ;
  - une phrase de version neuve ;
  - la table : ligne du devis v11, son chemin de versement, sa copie de travail et son empreinte ; ligne « cet additif, v5 » ; ligne neuve de la vérification 3, avec le chemin et l'empreinte justes.
- **Devis, 3 remplacements** : le titre (v10 → v11), une phrase de version neuve et le statut.

Aucun autre lieu n'est touché. Aucun chiffre, aucune règle, aucun renvoi n'est changé, hors la règle de lecture des versions du devis. Les deux phrases de version citent ma vérification 3 exactement : chemin, empreinte, verdict, et la phrase « une fois X1, X2 et Y1 portés tels quels […] : conforme, à sceller ».

## 3. Les écarts 2 et 3 du rédacteur

**Écart 2 — section « Contre-lecture » non touchée.** Elle dit encore « **La v4 n'est pas vérifiée.** … reste à vérifier par le même contre-lecteur », et n'a pas d'entrée « Vérification 3 ». Scellée telle quelle, elle affirmerait une chose fausse : la v4 est vérifiée. Le statut et la phrase de version disent l'état juste, mais la section le contredit. Je ne demande pas de version neuve. Chaque entrée de cette section dit « Le traitement est écrit par la mère au scellement », et la v9 a été scellée ainsi, son traitement écrit par la mère (R-4271). **C'est acceptable au scellement, à la condition que le traitement de la mère remplace cette phrase.** Texte proposé, à la place de la puce « **La v4 n'est pas vérifiée.** … puis scellement par la mère. » :

    - **Vérification 3** (l'additif 1 v4 et le devis v10, par le même contre-lecteur) : brouillons relus : l'additif v4, `8e3d77a368189304fab58ddd548c4e21c30f5f469c36661620006db1a7613215`, et le devis v10, `5737ec6ed4d32635b91d04c7aad0cae894615b18a0129b8906eb196337aa5b77`. Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v7/additif-1-v4/verification-v1/verification-additif-1-v4-devis-v10-v1.md`, `9e08297c2934deb2d97c702d82a6a55d6398c5d4ef21849d3071333b2fd3787a`, verdict « À corriger, de lettre seulement » : X1 et X2 sur l'additif, Y1 sur le devis ; les deux passes rejouées à l'octet ; aucun chiffre du calcul changé ; relevé « aucune recette » conforme.
    - **Constat final** (l'additif 1 v5 et le devis v11, par le même contre-lecteur) : première passe égale, par `cmp`, aux essais du vérificateur ; seconde passe, de tenue seule, rejouée à l'octet ; verdict « Conforme, à sceller ». Chemin et empreinte du constat : écrits par la mère avec ce traitement.

**Écart 3 — « devis v10 » dans le corps du devis v11.** Il y a deux lieux :
- la ligne 14, « (le devis v10, depuis la seconde vérification) » ;
- la ligne 452, « c'est ce devis v10 qui va à Lazar ».

La phrase de version de la v11 dit : « Là où ce texte dit que « ce devis v10 » va à Lazar, c'est ce devis v11 qui y va. » La ligne 452 est exactement couverte. La ligne 14 dit « le devis v10 », non « ce devis v10 », mais c'est le même renvoi, au même objet. Le titre, le statut et la phrase de version disent v11. Le précédent est le même que pour « devis v3 » lu « devis v6 » à la v9 scellée, et pour les versions 3 et 4 de l'additif. **Acceptable au scellement, sans correction.** Un point pour la mère : le devis va à Lazar, qui lira « devis v10 » à deux endroits. Quand elle lui demande sa ligne de calcul, elle nomme le devis v11 et son empreinte (`205e08f2…`), pour que l'accord ne puisse viser une autre version.

Écarts 4 et 5 (copie de travail à `…/additif-1-v5/` ; date prise au journal de la première passe) : justes, comme aux versions précédentes.

## 4. Fichiers

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-additif-1-v9/` : cette pièce et son compagnon `.sha256`. Les rejeux (`rejeu-additif-1-v5.md`, `rejeu-devis-v11.md` et leurs journaux) sont des essais, non des pièces.

— contre-lecteur neuf, modèle O
