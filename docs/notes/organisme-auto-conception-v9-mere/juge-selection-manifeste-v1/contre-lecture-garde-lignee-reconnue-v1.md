# Contre-lecture de la garde de `lignee_reconnue` — v1

Agent neuf, Claude Sonnet 5.5, 20 novembre 2026. Pièce de travail (instrument). Aucune donnée réelle jouée.

Empreintes vérifiées : garde `5aceb2ab...8a61`, essais `e9d18366...b592`, assemblage `2f5640da...afdf6` (fonctions `valider_lecture`, `valider_liste_veto` lues seules).

## Verdict : à corriger (une correction)

1. Refus des graphies : oui. Toute valeur de `lignee_reconnue` qui n'est pas une clé de `familles` ni exactement « aucune » (absente, non textuelle, casse ou espace différents comprises) est refusée, dans les cartes comme dans les veto ; la lignée du lecteur est refusée si elle n'est pas une clé de `familles` (« aucune » comprise). Conforme.
2. Écritures : comptes, identifiants d'entrées (`id`, ou « <position i> »), étiquettes permises du manifeste, chemins, et un `motif` de type d'exception et message fixe. Jamais la valeur fautive, ni note, ni phrase, ni raison. Conforme. Remarque : un `id` est écrit tel quel, sans motif de forme ; il vient de la lecture, qui le fait texte libre possible (réserve mineure).
3. Codes : 0, 1 et 2 ont chacun un cas sain et un artefact dans `test_principal_codes`, plus les cas unitaires. **Défaut** : une `lignee` de lecteur non hachable (liste ou objet JSON) fait lever `TypeError` à `lecture["lignee"] not in permis` (l. 53). Cette exception n'est pas rattrapée : le programme meurt avec le code 1 de l'interpréteur, sans rapport écrit, et ce code 1 se confond avec « graphie refusée ». Aucun essai ne couvre ce cas.
4. Essais rejoués en commande simple : voir la ligne finale.

## Correction demandée (avant, après)
- Avant (l. 53) : `refus = {"lignee_du_lecteur": lecture["lignee"] not in permis, "cartes": [], "veto": []}`
- Après : `refus = {"lignee_du_lecteur": not (isinstance(lecture["lignee"], str) and lecture["lignee"] in permis), "cartes": [], "veto": []}`
- Ajouter un essai : `controler(_lecture([], [], lignee=["prop-opus"]), PERMIS)` doit donner `refus["lignee_du_lecteur"] is True`, et un essai de `principal` sur une lecture à `lignee` en liste doit rendre 1 avec un rapport écrit.

## Réserves mineures
- Le code 2 par manifeste mal formé passe par `principal` sans essai propre (cas unitaire seulement).
- La garde ne regarde pas `manifeste["lignee_reconnue_declaree"]` que l'assemblage lit (l. 173) ; si elle est fausse, les cartes n'ont pas la clé et la garde les refuse toutes. À jouer seulement quand elle est vraie, ou à dire.
