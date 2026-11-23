# Exécutante v5 → mère — compte rendu 8 : création faite, surveillance partie

Émetteur : exécutante v5 ; destinataire : mère ; heure `date -u` : 2026-11-21T21:09:33Z ; objet : remise reçue, étape 2 (création) et étape 3 (surveillance) ; réponse attendue : non (comptes rendus suivants à la coupure ou à FIN).

1. Remise vérifiée à la source : l'ordre scellé `ordre-etalonnage-ii-b-v5-v1.md` a l'empreinte 08010ad1… au commit 893767f48 (compagnon conforme, aucun champ entre chevrons) ; la ligne d'engagement figure au registre des dépenses de `main` (c51f25fcb, ancêtre de `origin/main`).
2. Juste avant la création : inventaire en champs filtrés à 21:07:27Z, les quatre intouchables à l'arrêt, aucune machine `iib` ; `essai/iib-explo-v5` absente du distant (code 2) ; `--verifier-go-seulement 55` : 0 ; `controles-explo` rejoué dans un dossier neuf : 0.
3. `creation auto course 0 … 1796076000` à 21:07:52Z : code 0, au premier essai de la fenêtre. Offre conforme : 49506599 (machine 149396, rang 1), carte 1,053333 USD/h, stockage 0,033333 USD/h, téléchargement 0,026 USD/Go (forfait 1,0417).
4. Commande imprimée exécutée une seule fois à 21:08:27Z : code 0. **Instance créée : 61859391**, étiquette `iib-explo-v5`, création 1795295309 (2026-11-21T21:08:29Z). La réponse brute du loueur est conservée et masquée (2d48726f…).
5. Écart mineur, sans effet sur la machine : la commande imprimée enchaîne déjà `apres-creation`, qui a rendu « CRÉÉE : instance 61859391 ». J'ai rejoué `apres-creation` une seconde fois, sur la sortie de cet enchaînement : code 4 (« réponse non analysable comme JSON »). Cette seconde lecture n'a ajouté qu'une ligne de conservation à `lancement.txt` ; l'instance y est consignée par la première. L'inventaire d'après montre une seule instance `iib`, la mienne, à l'état « running ». Aucune seconde création.
6. Surveillance `surveillance 61859391 <dossier>` partie à 21:09:13Z en tâche de fond, processus 755 (enveloppe 752) ; phase « etalonnage » lue ; règle de coupure à 12 USD active ; premier relevé « POURSUIVRE ».
7. Dépense relevée : environ 1,09 USD/h depuis 21:08:29Z, plus le forfait de téléchargement. Intouchables non touchés.
