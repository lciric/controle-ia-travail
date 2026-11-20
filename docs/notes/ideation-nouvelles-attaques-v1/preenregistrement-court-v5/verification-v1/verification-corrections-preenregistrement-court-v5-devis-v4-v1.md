# Vérification des corrections — préenregistrement court v5 et devis v4 de la course « nouvelles attaques » — v1

- Contre-lecteur neuf, modèle O : le même qui a écrit la contre-lecture de la v4 et du devis v3 (`539c4854ad36e5d9b615c43bb2f7b7359c27661abc6f2a0abc6195812c1e150f`). Je n'ai écrit ni la v5 ni le devis v4. Règle R2 ; pièce de travail au service de pièces décisives. Écrit le 2026-11-20 ; relevé de `date -u` : 10:37:20Z, avant l'écriture.
- Demande : message de la session de l'organisme, sur le versement du commit `109205e3a77f9198626188ad3ddcf86abe2c5623` (HEAD de mon conteneur). Mêmes interdits que mon mandat (`01f9e057…`).
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucun lancement, aucune écriture dans le dépôt, aucun commit. **Aucun refus de permission, de classifieur ni de garde.**

## Verdict

**À corriger**, sur trois points de lettre du préenregistrement v5 (C1 à C3), et un blanc à écrire par la mère (C4). Le devis v4 est **conforme**. K1 à K9 et le texte de la contre-lecture 4 sont portés mot pour mot. Rien d'autre que la tenue n'a changé. Aucune correction ne touche un total, un seuil, un arrêt ni une décision.

## 1. Empreintes (égales au compagnon)

Dossier P5 = `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v5/`.

| pièce | empreinte |
|---|---|
| P5/`preenregistrement-court-course-nouvelles-attaques-v5.md` | `b2bb980af931fef450cdcb3aee59c0134e8fc0fbf6cce62415bc99c70dcf6993` |
| P5/`devis-course-nouvelles-attaques-v4.md` | `620de3692d3454f08d32832ca471551bb9a8439f80122b716b13474d9a6d363e` |
| P5/`remplacements-preenregistrement-court-v4-v5-v1.json` ; P5/`remplacements-devis-v3-v4-v1.json` | `55418553…` ; `25d7dbde…` |
| les deux journaux de l'outil | OK |
| P5/`differentiel-preenregistrement-court-v4-v5-v1.diff` ; P5/`differentiel-devis-v3-v4-v1.diff` | `04c601b1…` ; `46a3e42f…` |
| P5/`sortie-validateur-preenregistrement-court-v5-v1.txt` | `97feea71…` |
| P5/`rapport-redacteur-preenregistrement-court-v5-devis-v4-v1.md` | `74680af5…` |
| mandat du rédacteur de la v5 (dossier v4) | `2a813c54…` |
| ma contre-lecture et mes deux jeux, versés au sous-dossier `preenregistrement-court-v4/contre-lecture-v1/` | `539c4854…` ; `14b429fe…` ; `11977cde…` |

Les noms des différentiels, de la sortie du validateur et du rapport sont tirés des journaux de l'outil et du rapport du rédacteur, sans commande de liste.

## 2. Rejeu et comparaison

- Outil (`391db990…`) sur la v4 (`2dabdadf…`) avec le jeu du rédacteur : « FAIT : 9 remplacement(s) », sortie `b2bb980a…` ; `cmp` avec la v5 versée : égal. Sur le devis v3 (`bf7b4ba3…`) : « FAIT : 8 remplacement(s) », sortie `620de369…` ; `cmp` : égal.
- Différentiels refaits : ils ne diffèrent des versés que par la ligne 2 (chemin et heure).
- Programme `comparer_corrections_v5_v1.py` (à côté de ce rapport ; il n'écrit rien) : chacun de mes neuf objets K1 à K9 figure à l'identique dans le jeu du rédacteur ; le « neuf » de la contre-lecture 4 est égal au texte du § 8 de ma pièce ; huit remplacements hors K1 à K9 (quatre de tenue et la contre-lecture 4 au préenregistrement, trois de tenue au devis).
- Validateur rejoué sur la v5 : « problemes : aucun », égal à la sortie versée.

## 3. La tenue et les deux écarts déclarés

- **Ligne de date, relevé « Version 5 »** : conforme à l'usage de la v4, qui ajoutait de même son relevé. Écart sans suite.
- **« La v3 n'est pas contre-lue. » devenu « La v3 est contre-lue (ligne suivante). »** au devis : la phrase était devenue fausse ; la corriger dans la phrase de version est la tenue juste. Écart sans suite.
- **Renvoi « devis neuf » du statut de la v5** : c'est la lettre de GO-2026-11-20-33 (« le mot de Lazar sur le devis neuf »), et la parenthèse nomme le devis v4. Conforme.
- Titres, statuts et phrases de version : rien n'y tranche ce qui reste à Lazar. Le plafond reste en deux options (§ 9 du devis) et la sonde de l'espèce 6 reste à 0,01 USD avec la réserve de K9.

## 4. Les réserves du rapport du rédacteur

1. **Le validateur ne voit pas les blancs.** C'est vrai, et c'est de mon fait : j'ai écrit « (empreinte du rapport) » et « (à écrire par la mère) » sans le marqueur que le validateur reconnaît. Un « aucun » du validateur ne vaut donc pas ici « complet ». L'empreinte est connue et déjà citée par la phrase de version de la v5 : C3 l'écrit. Le traitement reste à la mère (C4). **Avant scellement**, `grep -c -F -e "(à écrire par la mère)"` et `grep -c -F -e "(empreinte du rapport)"` doivent rendre 0 sur le texte à sceller.
2. **Le chemin de mon rapport** dans la contre-lecture 4 n'a pas le sous-dossier `contre-lecture-v1/` où il est versé. L'erreur vient de mon texte. Elle est à corriger (C3), parce qu'un chiffre et une pièce citée renvoient à un chemin et une empreinte (R6).
3. **Les renvois croisés.**
   - *Dans la v5, une correction est nécessaire.* La v5 se scelle avec un tableau des pièces qui donne le chemin et l'empreinte du devis v3 (`bf7b4ba3…`). Or son point 11 fait dépendre la course du « mot de Lazar sur le devis v3 », alors que c'est le devis v4 (`620de369…`) qui va à Lazar. Un texte scellé ne doit pas laisser ce doute à la ligne d'activation. Une seule ligne suffit : la ligne du tableau définit « devis v3 » dans ce texte comme renvoyant au devis v4 (C1). Les sections citées (§ 0, 2, 3, 4, 6, 9) et leurs chiffres sont les mêmes dans les deux devis. La citation de GO-34, qui dit « le devis v3 », reste une citation à la lettre. C2 retire « même réserve », qui perdrait son antécédent.
   - *Dans le devis v4, aucune correction.* Les quatre renvois au « préenregistrement court v4 » (en-tête, § 4 deux fois, § 9) visent la section « Seuil » et les valeurs ouvertes. Ces parties existent à l'identique dans la v5, hors la ligne ouverte ajoutée par K3. La phrase de version du devis v4 dit que la v5 remplace la v4. Le devis n'est pas le texte scellé au sens de R1.
4. **« Devis neuf » dans le statut** : conforme (§ 3).
5. **Les 0,05 USD de la sonde** ne sont dans aucun texte : c'est voulu. C'est une option que la mère porte à Lazar avec le devis, pas une correction. Sans suite.
6. **Le calcul n'est pas rejoué** : juste, aucun chiffre calculé ne change. Les chiffres ajoutés par K5 à K9 viennent de mon programme indépendant (`9a992891…`) et de `wc -c` sur la question scellée.
7. Les points renvoyés à la mère par ma contre-lecture restent entiers : la relecture du solde de Rigaud et les lots de R-4170, l'ordre de course v3 à cinq espèces, R-4179.

## 5. Corrections, à texte exact, sur la v5 (`b2bb980a…`)

Chaque « Ancien » est compté une fois par `grep -c -F -e`. C1 à C3 sont dans `corrections-preenregistrement-court-v5-v1.json`, à côté de ce rapport, et ont été passées à l'outil sur une copie : « FAIT : 3 remplacement(s) », sortie `367a85b71ab96ecca11e496cf1e8c9f488191cc131cb5c3dd424eb442c35b278`. La version neuve est à écrire par la mère, sous un nom neuf (R12).

- **C1** (tableau des pièces). Ancien : « | devis v3, à six espèces (« devis v3 » dans ce texte ; « devis » seul renvoie au devis v2) | `NA/preenregistrement-court-v4/devis-course-nouvelles-attaques-v3.md`, au chemin où la mère le verse | `bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a` | » — Neuf : « | devis à six espèces, v4 (« devis v3 » dans ce texte, hors la citation de GO-2026-11-20-34, renvoie à ce devis v4, qui ne change du devis v3 que la lettre des corrections K5 à K9, sans total, seuil ni section changés ; « devis » seul renvoie au devis v2) | `NA/preenregistrement-court-v5/devis-course-nouvelles-attaques-v4.md` ; il remplace le devis v3, `NA/preenregistrement-court-v4/devis-course-nouvelles-attaques-v3.md`, `bf7b4ba3ede3ba73c8ee4e1a3548b6b0d52975df717b98ca4af44a6c503c142a` | `620de3692d3454f08d32832ca471551bb9a8439f80122b716b13474d9a6d363e` | »
- **C2** (même tableau). Ancien : « `NA/preenregistrement-court-v4/calcul-devis-course-nouvelles-attaques-v3.json`, même réserve ; » — Neuf : « `NA/preenregistrement-court-v4/calcul-devis-course-nouvelles-attaques-v3.json`, sortie que le devis v4 garde sans la rejouer ; »
- **C3** (contre-lecture 4 : chemin et empreinte). Ancien : « Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/contre-lecture-preenregistrement-court-v4-devis-v3-v1.md`, (empreinte du rapport), » — Neuf : « Rapport : `docs/notes/ideation-nouvelles-attaques-v1/preenregistrement-court-v4/contre-lecture-v1/contre-lecture-preenregistrement-court-v4-devis-v3-v1.md`, `539c4854ad36e5d9b615c43bb2f7b7359c27661abc6f2a0abc6195812c1e150f`, »
- **C4** (blanc de la mère, non écrit par moi). Ancien : « Traitement : (à écrire par la mère). » — Neuf : le traitement, écrit par la mère. Proposition de lettre, qu'elle reprend ou non : « Traitement : K1 à K9 acceptées, appliquées à texte exact dans la v5 et le devis v4 ; vérification par le même contre-lecteur : `verification-corrections-preenregistrement-court-v5-devis-v4-v1.md` (empreinte au compagnon), verdict « À corriger » ; C1 à C3 appliquées dans la v6. »

**Après C1 à C4** : je recommande que la mère rejoue l'outil sur la v5 avec ses quatre remplacements, contrôle les deux `grep -c` à 0 du point 4.1, rejoue le validateur, puis me fasse vérifier par `cmp`. Je n'attends pas d'autre correction.

## 6. Écarts

1. J'ai tiré les noms des pièces versées des journaux et du rapport du rédacteur, faute de commande de liste.
2. Mes essais (rejeu, différentiels, copie corrigée) sont dans mon sous-dossier `verification-v5/`. Rien n'est écrit ailleurs.

— contre-lecteur neuf, modèle O
