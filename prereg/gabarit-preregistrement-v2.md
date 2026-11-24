# Préenregistrement — À REMPLIR (identifiant, tâche, version)

<!-- Gabarit v2 (24 novembre 2026) : la v1 et ses sections restent ; ajout de la section « Règles de forme », issue de la proposition retenue 4 du collisionneur groupé sur la naissance des idées scientifiques fécondes (mandat GO-2026-11-24-46). -->

Gabarit conforme à R1 et R2. Copier sous `prereg/<tache>-<objet>-vN.md`, remplir chaque section,
faire contre-lire par un sous-agent neuf, puis sceller avec `controle_ia.prereg.sceller_prereg_v2` (contrôles v1 et
règles de forme) ; avant un run, `exiger_prereg_scelle_v2`.
Le validateur refuse toute section absente, vide, ou contenant le marqueur « À REMPLIR ».
La section « Règles de forme » est contrôlée par `controle_ia.prereg.problemes_forme` : chaque règle porte son
étiquette en gras, suivie soit de sa mise en œuvre, soit de « sans objet : » et d'une raison. Le contrôle est de forme :
il refuse les règles absentes, vides, en double ou bouche-trous, il ne juge pas le fond. « Non exécutable » se déclare
dans la règle « Effectif par analyse de puissance » ; il n'est pas vérifié par programme.
Pas de sous-liste sous une règle (elle serait lue comme une puce nouvelle et la règle jugée vide) ; rien sous la
dernière règle hors d'une puce.

- Auteur : À REMPLIR
- Date (UTC) : À REMPLIR
- Commit du code d'analyse : À REMPLIR
- Documents qui font foi (chemin + empreinte) : À REMPLIR

## Hypothèse

À REMPLIR — énoncé, renvoi au programme (section, identifiant d'hypothèse), hypothèses de travail.

## Prédiction chiffrée et signe attendu

À REMPLIR — pour chaque prédiction : signe attendu, ordre de grandeur ou forme de courbe, ce qui compterait comme réfutation.

## Métrique

À REMPLIR — définition exacte, unités, estimateur, intervalles (méthode et niveau).

## Seuil

À REMPLIR — seuils de décision et taux d'erreur visés, fixés avant toute lecture.

## Plan d'analyse

À REMPLIR — données, taille d'échantillon et justification, graines (R9), comparaisons, corrections pour comparaisons multiples, contrôles appariés.

## Règles de forme

À REMPLIR — une ligne par règle ; « sans objet : <raison> » permis.

- **Statistique et seuil uniques** : À REMPLIR — la statistique principale et son seuil, uniques ; toute autre est descriptive.
- **Hypothèses complémentaires** : À REMPLIR — deux hypothèses complémentaires sur le même dispositif, et l'issue qui départage.
- **Effectif par analyse de puissance** : À REMPLIR — effectif, puissance visée, effet minimal ; « non exécutable » déclaré d'avance si l'effectif est hors d'atteinte.
- **Nul de la statistique maximisée** : À REMPLIR — si la statistique est un maximum ou résulte d'une recherche : nul recalculé en refaisant la recherche sur chaque tirage nul.
- **Comparateur apparié** : À REMPLIR — comparateur de même capacité et même budget de requêtes ou de calcul.
- **Unité indépendante** : À REMPLIR — unité statistiquement indépendante explicite ; règle de trois si zéro événement.
- **Extracteurs figés avant la coupure** : À REMPLIR — extracteurs, taxonomies et vocabulaires figés avant la coupure temporelle ou avant la vérité plantée.
- **Amputation placebo** : À REMPLIR — pour toute redécouverte de primitive : amputation placebo et réécriture hétérogène.
- **Seuils sur générateurs disjoints** : À REMPLIR — seuils fixés sur des générateurs ou graines disjoints de ceux de l'épreuve.
- **Lot d'étalonnage distinct** : À REMPLIR — lot d'étalonnage distinct du lot jugé, et comment la séparation est garantie.

## Critères de lecture gelés

À REMPLIR — table : issue observée → verdict (confirmé, réfuté, non concluant) ; comment lire chaque combinaison ; ce qui déclenche l'audit de symétrie (R4).

## Liste d'arrêt

À REMPLIR — conditions qui arrêtent le run ou invalident la lecture (gardes, dépassements, anomalies), et action associée.

## Contre-lecture

À REMPLIR — sous-agent neuf (identifiant), empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
