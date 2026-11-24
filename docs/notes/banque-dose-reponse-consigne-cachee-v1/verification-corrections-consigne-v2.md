# Vérification des corrections de la contre-lecture de la consigne v2 (une passe, classe B)

Verdict global : **utilisable en l'état** (réserve non bloquante : l'essai de la réextraction est statique, voir CV2-1).

Contrôles faits : diff v1/v2 de la consigne (une insertion en 2b et la dernière phrase, rien d'autre) ; sceau de la v2 (`sha256sum` = 44da46b3…, égal au compagnon) ; diff des deux modules v2 ; comparaison par programme de la lecture recopiée avec `rejeu_contre_verification_banque_v1.lire` (identique, deux lignes blanches de différence) ; lancement de `tests/test_banque_dose_reponse_v2.py` : 7 réussis. Aucun module lancé en mode réel, aucun fichier interdit ouvert.

- CV2-1 (bloquante) : corrigée. `consigne_extracteur_v2` vérifie le sceau et arrête si la marque « 2b. Before going on, check the "research_questions" field » manque ; la préparation de la banque (ligne 536) et celle de la réextraction (ligne 88) passent par elle ; la réextraction vérifie en plus, dossier par dossier, que `consigne.txt` porte la marque (lignes 95-96). Essais : retour à la v1 rescellée sous le nom de la v2 (arrêt), préparation réelle d'une tentative dans un dépôt jetable (chaque dossier a la marque). Réserve non bloquante : l'essai de la réextraction (`test_reextraction_v2_lit_la_consigne_v2`) lit le texte source et ne prépare pas de dossier ; seule la garde par dossier couvre le comportement à l'exécution. Un essai de comportement (préparation d'un faux échantillon) serait un plus.
- CV2-2 (mineure) : corrigée. Les deux en-têtes citent `..._v1.py` ; l'affirmation « prend la consigne v2 » est maintenant vraie.
- CV2-3 (mineure) : corrigée. La question phrase par phrase est « reveals any item of the list above » avec les six éléments énumérés (figure ou tableau, contribution nommée, nom d'auteur compris) ; la liste elle-même est inchangée et identique à H9.
- CV2-4 (mineure) : corrigée. « Apart from the file names, the check in step 2b and the check in step 5 ».
- CV2-5 (mineure) : corrigée pour le champ (« Change only the "research_questions" field ») ; l'écart de lettre « avant l'écriture » est déclaré dans la note de traitement et sans effet sur l'état final. Acceptable.
- CV2-6 (suggestion) : retenue comme engagement de rapport (énoncés sous 200 caractères, longueur médiane, avant et après) à l'essai ; rien à vérifier dans le code à ce stade.
- CV2-7 (suggestion) : corrigée en (a) sceau présent et exact, (b) essais ajoutés (cas sain, diff limité à 2b et dernière phrase, trois artefacts, préparation réelle). Pour la lecture recopiée, pas d'essai d'équivalence propre, mais l'identité textuelle avec l'original est vérifiée ci-dessus ; (c) noté, inchangé.

Remarques nouvelles : une seule, de forme, sans gravité (suggestion) : dans `extraire_banque_dose_reponse_v2.py`, la fonction `consigne_extracteur_v2` est collée à `FICHIERS_PROCEDURE` sans ligne blanche.
