# Passation — session fille du côté des moniteurs : texte candidat au scellement de l'additif 2 de format aux sondes du barreau 8

Session `session_01Qi7Gr3DCGJkFuLgghCz7Mh` ; branche `prep/additif-2-scellement-v1`, partie de la branche principale à `c4550d8d`, où la branche de livraison des brouillons 2 à 6 est fusionnée. **Rien n'est scellé : le texte candidat n'a pas de compagnon d'empreinte, et aucune ligne n'est inscrite au registre propre.** Demande de la session mère (message du 2026-11-24 à 10:16Z), après le mot de Lazar inscrit sous GO-2026-11-24-14 (vérifié au registre des accords de la branche principale).

## Fait

1. **Versement** des quatre pièces de la condition D-14 de l'additif 1 à leurs chemins, à 10:18:40Z ; `sha256sum -c` : quatre « OK ».
2. **Provenance du programme de comparaison de version 1** : « non attesté » (ligne R-5239 : écrit par un sous-agent du côté exposé ; aucune contre-lecture trouvée). Note : `docs/notes/rejeu-activations-saboteur-voie-a-v1/additif-2-scellement-v1/provenance-programme-comparaison-v1-et-versement-d14-v1.md` (`1bb83f9a…`).
3. **Texte candidat** : `prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md`, empreinte `d06fd7b4ab7ee609a28bc8e3ccaac2d3d968a1d7d8801ee5f2c58fc38da5662b` ; c'est le brouillon 6 (`3a3a4d16…`) avec ses quatre lieux remplis, par le programme `construire_texte_candidat_additif_2_v1.py` (`bf77a620…`) à partir de `champs-ad2-additif-2-v1.json`, même dossier.
4. **Deux contrôles**, sortie versée (`sortie-controles-texte-candidat-additif-2-v1.txt`) : `controle_ia.prereg.problemes` rend une liste vide ; la comparaison par programme avec le brouillon 6 ne trouve que quatre lignes changées (151 à 153 : cellules AD2-1 à AD2-3 ; 352 : entrée « Contre-lecture 2 »), aucun écart ailleurs.

## Réserves, pour la session mère, avant de sceller

- **Ce que Lazar avait vu.** Le champ AD2-3 porte, tel que la mère l'a dicté, qu'elle ne peut pas attester que Lazar n'a vu aucune autre sortie de la course lue (tableau des verdicts du 23 novembre, ligne « saboteur course 1 »). L'additif 1 voulait, dans ce cas, que le fait soit porté à Lazar et recopié en tête de tout verdict. Recommandation : lever ce doute auprès de Lazar avant le scellement, ou sceller avec la réserve écrite et la porter en tête du verdict.
- **Heures.** L'attestation de la mère est de 10:18:17Z ; le versement est de 10:18:40Z, fait ensuite par cette session, sur une branche et non sur la branche principale. Le champ AD2-3 le dit ainsi. Si la mère refait le versement ou veut une autre rédaction de ses cellules, elle rejoue le programme avec un fichier de champs neuf (nom nouveau) : les deux contrôles se rejouent d'eux-mêmes.
- **« Non attesté »** entraîne, après le scellement, la réécriture de la pièce de comparaison sous un nom nouveau par la version nouvelle du programme (règle M-4).
- Les lignes « qui a lu quoi » de cette session et de son vérificateur ne sont pas encore versées (texte proposé dans la note `versement-pieces-d14-et-lignes-qui-a-lu-quoi-v1.md`).
- `verifier-arbre` signalera sur cette branche le texte candidat sans compagnon : c'est voulu, jusqu'au scellement.
- En cherchant la provenance, cette session a lu les lignes R-5239 à R-5244 du registre des décisions ; aucune ne porte de sortie de la course lue. Elle n'a pas ouvert les lignes R-5201 et R-5212.

## Prochaine action

Session mère : vérifier, sceller (`controle_ia.prereg.sceller_prereg`), inscrire la ligne `SCELLEMENT-ADDITIF-2-SONDES-IIB`.

## Instances actives

Aucune. Aucune dépense.
