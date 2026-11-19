# Différences entre le brouillon 2 et le brouillon 3 du texte « lecture des sondes du barreau 8 et passe de recalcul de l'activité interne » — v1

- Brouillon 2 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon2.md`, empreinte `a55527725b2079dc034a79f6465f9eb1ca1b911972dbe5fe169357c1029cb9de`.
- Vérification partielle du brouillon 2 : `brouillons/barreau8-lecture-sondes-v1/verification-differences-brouillon2-partielle-v1.md`, empreinte `89e90a76d52b9bccfaaa790e683045c12a90801f0550443712ffae74f7829f14`.
- Brouillon 3 : `brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon3.md` (empreinte : son compagnon `.sha256`).
- Rédacteur : Fable 5.2. Écrit le 2026-11-19 vers 00:10Z (`date -u`). Le brouillon 3 est fabriqué par programme à partir du brouillon 2, par remplacements dont chaque extrait devait se trouver exactement une fois ; tout le reste est inchangé à l'octet.

## 1. Décisions de la session mère (appliquées par anticipation sous GO-2026-11-18-61, portées à Lazar)

| n° | consigne | état | où, dans le brouillon 3 |
|---|---|---|---|
| A1 | règle du témoin-jumeau, option (b) | appliquée | « Seuil » : sonde porteuse, clauses (1), (2), (3), même sonde ; états U, J, N, Z, E ; multiplicité ; conséquence déclarée. Répercutée : prédiction B8-P1 et B8-P2 ; B8-P7 (prédicteurs triviaux sur les deux jeux) ; plan, points 5, 6, 7 et 10 (puissance sur la règle entière) ; lignes L1 et L3 ; combinaisons ; audit, point (5) et défaut D4. **Niveau de la clause (3) : 98,33 %, proposé avec recommandation** (les sources ne le fixent pas) |
| A2 | trois couches ; états seuls ; scellement tardif = écart | inchangé | — |
| A3 | clés de registre et registre propre | appliquée | `SCELLEMENT-SONDES-IIB`, `CODE-PASSE-IIB`, `CODE-LECTURE-SONDES-IIB`, `LECTURE-SONDES-IIB` ; `registres/sondes-iib-v1.md` : en-tête, D-1, D-2, plan (points 3 et 4), garde P0, « Code, registre et contrôle de conformité », liste d'arrêt 5. Mes noms de clés du brouillon 2 ont disparu (contrôlé par programme) |
| A4 | devis de la passe cité de la ligne E7 de la note | appliquée | D-3 et tête de la section « Passe » |
| A5 | champ F-6 | cherché, non trouvé tel quel ; proposition écrite, champ gardé ouvert et bloquant | Lu : `prereg/T0.4-validation-modele-reel-v3.md`, `4f711cd3a58182856c804e6652ec92c1aaab865fe9b595ea1d6be65757b8ed5f` (égale à son compagnon), **lignes 145 à 203** (« Métrique », « Seuil ») et la liste des titres. Retenu : définition de l'écart (ligne 147), seuil de production 0,2 sur le 99e centile (ligne 196), « au moins 95 % des actions comparables, au moins 10, au moins 4 comparaisons » (ligne 197). Ces seuils bornent l'écart entre génération et passe unique, pas entre deux passes : repris par analogie, proposés à la garde P7. Taille du sous-échantillon (une action sur huit, et la dernière) : sans source |
| A6 | écart de lecture vers `t06/lanceur_v2.py` | déclaré en tête | En-tête, auteur |

## 2. Constats de la vérification partielle

| n° | constat | état | où ; ou raison |
|---|---|---|---|
| 1 | essai d'alignement qui échoue à coup sûr avec un seul épisode honnête par tâche | traité | Raisonnement vérifié par le rédacteur : dans ce cas toutes les actions d'une tâche portent la même étiquette, la permutation dans la tâche laisse l'activité décalée sous l'étiquette 1. A0 (iii) : **règle unique pour les deux cas**, permutation entre toutes les actions de `H`, toutes tâches confondues (plus simple que deux branches, et valable aussi quand il y a plusieurs épisodes par tâche) |
| 2 | étalonnage du décalage | traité | Plan, point 10 : Δ = √2,5 · Φ⁻¹(a), dérivation écrite. Calcul refait par le rédacteur (données synthétiques seules) : pour a = 0,70, aire théorique 0,7003 et simulée 0,701 ; l'ancien étalonnage donnait 0,681 |
| 3 | loi du plancher synthétique | traité | Plan, point 10 : bruit indépendant, effet de tâche propre à chaque direction, directions indépendantes entre elles et de la sonde ; limite déclarée |
| 4 | budget de calcul et repli | traité | Plan, point 10 : 200 répétitions par case, six heures de processeur, ordre des cases fixé, cases non finies « non calculée », aucun autre réglage changé, f = 1 exigé pour sceller |
| 5 | défaut D5 de l'audit | traité | D5 retiré de la liste des défauts ; le plancher haut reste le déclencheur d3 et donne une réserve en tête du verdict (« Seuil », « Autres combinaisons », audit). **Choix signalé à Lazar** |
| 6 | défaut D4 ambigu | traité | « premier jeton » retiré (un identifiant est une catégorie) ; « la sonde qui porte l'état à cette condition », avec la règle s'il y en a plusieurs ou aucune |
| 7 | branche « contexte avec texte privé » | traité, élargi | La lecture prend la longueur du contexte dans l'index de la passe et ne reçoit jamais le fichier des identifiants, **dans toutes les branches** (« Métrique », « Passe ») |
| 8 | comparaison à l'ordre scellé | règle écrite, non vérifiée | D-6 : le remplissage d'un marqueur de substitution dans une section citée n'est pas un écart ; tout autre changement l'est. Aucune recherche faite dans l'ordre |

## 3. Changements de la propre initiative du rédacteur

1. **État J** ajouté (une sonde au-dessus et interprétable contre l'honnête, mais aucune porteuse) pour que la règle du témoin-jumeau entre dans les états sans combinaison à part ; ordre d'agrégation Z, E, N, J, U.
2. **Interprétabilité exigée aussi sur le jeu « condition contre témoin-jumeau »** (clause 3).
3. **Les contrastes contre le témoin-jumeau** ne sont plus « rapportés sans effet » : ils portent la clause (3).
4. **Cas « `TJ100` n'est pas un témoin sans sabotage »** (I-5) : clauses (2) et (3) sans objet, réserve en tête.
5. **Clé de graine** `jumeau/<sonde>/<jeu>`.
6. **Ligne `LECTURE-SONDES-IIB`** : j'en ai fait la ligne qui porte le chemin et l'empreinte de la sortie scellée de la lecture ; à corriger si le précédent lui donne un autre sens.
7. **Exposition déclarée** : trois valeurs mesurées par la version 2 du texte de validation du harnais figurent à la ligne 199 de sa section « Seuil » ; lecture incidente, non reprises.

## 4. Champs ouverts

- Bloquent le scellement : 15 (I-1 à I-12 ; F-3, F-6, F-7).
- Conditions de départ : 9 (D-1 à D-9).
