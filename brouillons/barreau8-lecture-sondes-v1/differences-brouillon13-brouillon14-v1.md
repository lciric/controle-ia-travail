# Différences entre le brouillon 13 et le brouillon 14 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 13 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon13.md`, empreinte `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4`.
- Sources, empreintes vérifiées, lues en entier : contre-lecture du brouillon 13 (Opus 5.5, contre-lecteur neuf), `brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon13-v1.md`, `a723e7d91b8d4cf2c485598e24e49123359725f932b7b81b27e4e935a137575d` ; contre-lecture des deux codes et troisième essai d'intégration, `docs/notes/barreau8-cote-moniteurs-sorties-v1/contre-lecture-codes-passe-v5-lecture-v4-integration-v1.md`, `c08e1ffb168454f44fb6f277423fe8e3d264ef24f2aa91d6e301cb5aa91cd1d4`. **Ni le code ni ses essais n'ont été lus.**
- Brouillon 14 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 entre 2026-11-19T04:49Z et 2026-11-19T04:51Z (`date -u` ; mêmes heures que la ligne de date du brouillon 14), par programme, à partir du brouillon 13 : remplacements contrôlés (chaque texte cherché doit paraître exactement une fois, sinon rien n'est écrit). Le programme vérifie que les chaînes de la procédure de remplissage restent uniques, qu'il reste exactement deux marqueurs, que la ligne 76 (F-3) est identique à celle du brouillon 13, que le bloc « Noms et champs, liste fermée » est identique au caractère près, et que la citation du passage (b-2) est le texte exact de la phrase citée.
- Ni hypothèse, ni prédiction, ni métrique, ni seuil, ni niveau, ni état, ni ligne de la table des issues ne changent.

## Une ligne par point

| n° | objet | état | où, dans le brouillon 14 |
|---|---|---|---|
| R-1 | le retour à l'option sans scores par jeton couvre la fin de phrase ajoutée au cas sain | mot pour mot | bloc de décision des scores par jeton, passage (b-5) |
| R-2 | copier, déposer, transmettre les fichiers de scores et en calculer l'empreinte n'est pas les ouvrir | mot pour mot | « Passe », « Qui fait quoi » |
| O-6 | le passage (b-2) citait une phrase sans ses marques de gras | corrigé comme (b-5) | passage (b-2) : la citation abrégée par des points de suspension est remplacée par la phrase entière, marques de gras comprises. Contrôlé par programme : la phrase paraît exactement deux fois dans le brouillon 14, une fois à sa place (« Métrique », score d'action) et une fois citée entre guillemets |
| T-1 | finitude : les neuf noms cherchés dans l'index de chacun des trois fichiers | mot pour mot | règle mécanique des sondes lues, phrase de la finitude (« sur toute entrée de l'index qui porte… » devient « sur toute entrée qui porte…, dans l'index de chacun des trois fichiers de sondes et de planchers, ») |
| T-2 | l'égalité des deux chemins n'éprouve pas le champ `rang` | mot pour mot, **avec un ajout à la garde r5** | essai A0, chapeau, après la phrase de l'égalité. La phrase dit que « la garde de réception r5 exige » que `rang` soit le rang de l'action dans l'ordre du fichier ; r5 ne l'écrivait pas (seule la liste des champs de l'index le définissait) : une demi-phrase est ajoutée à r5 pour que T-2 soit vraie du texte. C'est ce que le code fait déjà d'après le rapport |
| T-3 | après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués | mot pour mot | essai A0, chapeau, après la phrase de l'égalité |
| T-4 | nom des couches 7 ou 23 « qui paraît plus d'une fois dans l'index de son fichier » | mot pour mot à la règle mécanique ; **les trois autres endroits alignés** | règle mécanique ; plan, point 3 ; garde P1 (« ou y paraît plus d'une fois » devient « ou paraît plus d'une fois dans l'index de son fichier ») ; liste d'arrêt, ligne 8 |
| C | les deux champs `run_id` reçoivent la même valeur | écrit en une parenthèse, comme fait transmis par la session mère, non vérifiable par le côté des moniteurs ; la règle est inchangée | condition de départ D-12 |

**Cohérence vérifiée**
- T-3 contre la règle d'échec et le rejeu unique : la règle d'échec dit déjà qu'une inégalité fait échouer l'essai sans rejeu ; le rejeu ne s'ouvre que si (i) ou (iii) rend une sonde au-dessus, ce qui ne peut arriver quand ils ne sont pas joués. Aucune contradiction.
- T-1 et T-4 contre les quatre endroits de la règle des sondes lues : la finitude porte sur les trois index, le nom en double sur l'index du fichier de la sonde ; les quatre endroits disent maintenant la même chose pour le nom en double, et restent généraux pour la finitude (« un vecteur ou un biais d'une sonde ou d'une direction »).
- **Conséquence de T-2 et T-3 sur le retour (b-5)** (ajout du rédacteur) : le retour retirait la phrase de l'égalité « jusqu'à "jamais un score." » ; les deux phrases neuves, qui la suivent, seraient restées sans objet. Le passage (b-5) dit maintenant qu'elles sont retirées aussi.

## Autres changements (demandés)

- En-tête : titre et statut « brouillon 14 » ; ligne de date ; contre-lecteur du brouillon 13 ; les deux rapports cités avec leur empreinte ; le code de la passe est dit en version 5, celui de la lecture en « version 4 ou suivante », la ligne de registre de chaque code faisant foi.
- Section « Contre-lecture » : la phrase de renvoi de l'entrée « 3 octies » devient « cette différence est contre-lue par l'entrée 3 nonies » ; entrée « Contre-lecture 3 nonies » ajoutée (empreintes du brouillon 13 et du rapport).

## À réaligner dans le code (tiré du rapport seul)

- **Code de la lecture** : chercher les neuf noms aussi dans l'index du fichier des planchers pour le contrôle de finitude (remarque C-1 du rapport, T-1).
- **Code de la passe** : rien.

## Marqueurs restants

Deux, et deux seulement : F-3 (entropie racine des graines, ligne 76, inchangée au caractère près) et l'entrée « Contre-lecture 4 (finale, texte rempli) ». Sortie exacte du validateur sur le brouillon 14 : `['section vide ou à remplir : Contre-lecture']`.
