# Contre-lecture du chantier 2 du papier D (découplage géométrique, `papiers/D/theorie/decouplage-geometrique-v2.tex`)

- **Contre-lecteur** : Opus neuf, effort élevé, qui n'a rien écrit des pièces. Mandaté par la fille 2 (`session_01Qi7Gr5…`) sur consigne de la mère, le 24 novembre 2026. Aucun fichier de la pièce n'a été modifié.
- **Pièces** : `contre-lecture-decouplage-geometrique-v1.md` (rapport) et `verif/` (scripts du contre-lecteur, versés tels quels).
- **Verdict : tient avec réserves.** Les deux preuves sont justes sous leurs hypothèses. L'expérience jouet se reproduit au bit près. Il y a quatre défauts majeurs et aucun bloquant.

**Rejeu par la fille 2 sur une copie** (Python 3.13, numpy 2.5.5, scipy 1.18.1, environnement du bloc-notes) :
```
python -I verif/v3_moniteur_et_signe.py <dossier contenant experience_jouet_decouplage_sonde_v1.py>
python -I verif/v4_contre_exemple_signe.py <même dossier>
python -I verif/v5_borne.py
```
`v1_selection.py` demande en second argument le JSON `resultats-decouplage-v1.json` ; il n'a pas été rejoué. `v2_jouet.py` n'a pas été rejoué non plus.

**Les deux contre-exemples majeurs sont reproduits :**
- **Défaut 1.** En ReLU, une sonde sur des neurones disjoints de ceux du filtre ne change pas (lignes identiques, aire sous la courbe de 0,6914 avant et après). Pourtant, parmi les tricheurs qui passent le filtre, l'audit en attrape 0,356 au lieu de 0,519. L'invariance de la fonction de score ne protège donc pas l'audit conditionnel aux survivants. C'est la même leçon que pour le régime statique : ce qui compte, c'est la dépendance, pas le placement. En linéaire, la même mesure monte de 0,096 à 0,134.
- **Défaut 2.** La surveillance de ‖Ww‖ ne suffit pas : ‖W(T)w‖ = 5,3e-16 alors que ‖W(T) restreint aux neurones de la sonde‖ = 3,056, avec une dérive de la sonde de 3,4e-3.
- **Borne de robustesse** (`v5_borne.py`) : elle est atteinte avec égalité dans le cas gaussien testé. Le facteur 1/2 est donc juste mais lâche.

**Prochaine étape** (non faite : le mandat ne portait que sur la contre-lecture) : porter les corrections dans une v3 de la section, en reformulant la conclusion du second théorème (invariance du score, et non préservation de l'audit parmi les survivants), en remplaçant le moniteur ‖Ww‖ par la norme de W restreinte aux neurones de la sonde, et en ajoutant les citations classiques à vérifier sur PDF.
