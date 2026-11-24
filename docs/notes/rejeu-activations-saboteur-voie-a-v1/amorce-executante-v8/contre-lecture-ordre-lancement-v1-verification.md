# Vérification des corrections de l'ordre de lancement du rejeu, voie (A) — v1
Même contre-lecteur (Opus 5.5), une seule boucle, 2026-11-24. Ordre vérifié à `97a57d5c…f6425` (commit 8c6ac595). Aucun fichier du dépôt modifié.

**Verdict : corrections vérifiées.**

1. Contrôle de la carte par torch : fermé. La préparation « carte-torch » vient après « bibliotheques », lancée par l'interpréteur de l'environnement, délai 300 s. Elle exige torch qui voit la carte, « A100 » dans le nom, plus de 79e9 octets ; sinon code 1. Sans torch : code 1, joué ici.
2. Note périmée : fermé. L'erratum 1 prime sur la note. Il corrige l'accord (-13), le point 5 et le point 3. Il renvoie l'empreinte à celle du compagnon au scellement : acceptable, puisque l'empreinte changera au remplissage de « A_FIXER ».
3. Préalables du commit de lancement : fermé. Ils sont listés dans l'erratum : les six fichiers de la course, la table neuve de M-4, la ligne CODE-PASSE-IIB, le bordereau qui nomme -13 et le contrôle de M-3 par la mère.
4. Jeton Hugging Face : fermé. Dans `Machine._executer`, seule la préparation « modele » reçoit `HF_TOKEN`. Le nouvel essai montre « bibliotheques » sans jeton, « modele » avec le jeton Hugging Face, et jamais le jeton GitHub.
5. Compagnon vide : fermé. Message clair « NON CONFORMES <nom> », code 1 ; les vrais fichiers donnent toujours code 0. Les deux cas sont joués ici.
6. Dossier `original/` : fermé. `ignore_patterns=['original/*']` est ajouté ; la révision et le cache sont inchangés.
7. Commentaire de `PLAFOND_USD` : fermé (il cite -13). `git add -f` est gardé : sans effet, accepté.
8. Ligne de commande et motif « iib » : porté à la mère et inscrit dans l'erratum. Ouvert jusqu'à la livraison du module, comme prévu.

La copie de l'ordre où « A_FIXER » est remplacé passe toujours `lire_ordre` (accord -13). 55 essais passent.
