# Vérification des corrections : réponse du concepteur sur la programmation de poids, v2

- **Date** : Sat Nov 21 16:43:02 UTC 2026 (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur de la contre-lecture de la v1 (`contre-lecture-reponse-fable-programmation-de-poids-v1-opus-v1.md`, `2f0929fb142db252fab2de6d51541e92dd527a44ae1d45c229b51e2bf9ba001c`). La règle R-3735 veut que ce soit le même contre-lecteur qui vérifie les corrections. Pièce de classe C. Lecture seule hors du présent fichier ; ni commit ni poussée ; aucun appel payant ; aucune recherche en ligne.
- **Pièces vérifiées** (toutes égales à leur compagnon `.sha256`) :
  - `reponse-fable-programmation-de-poids-v2.md`, `90bbe8667dc914d72305eebc196962d163eaee139eafc121ef6af48dafde35d6` ;
  - `calculs-programmation-de-poids-v2.py`, `ef266dbf…3a14` ;
  - `calculs-programmation-de-poids-v2.txt`, `c261b0f4…81a7` ;
  - `collisionneur-v2/faits-programmation-de-poids-v2.md`, `ed68e879…4ab5` ;
  - `collisionneur-v2/question-programmation-de-poids-v2.md`, `ba8fcb67…9537` ;
  - `docs/sources/pdf/protocole-x-programmation-de-poids-v1/provenance-protocole-x-programmation-de-poids-v1-erratum-1.md`, `38fa88d0…6bdd`.
- **Rejeu** : une fois, par `/usr/local/bin/python3 -B` (Python 3.13.18, numpy 2.5.3), dans un dossier temporaire. La sortie est **égale à l'octet** au `.txt`.
- **Écarts entre la v1 et la v2 des calculs** : aux lignes de version près, la sortie v2 ne diffère que par deux ajouts, le sous-bloc C5 et le repère du bloc E avec sa table. Tous les nombres de la v1 sont inchangés.
- **Ce que vaut le sous-bloc C5** :
  - La fausse alerte de l'honnête est comptée directement sur les tirages de la v1, recoupés en fenêtres. Le seuil réparti vaut `ln(W/α)` avec `W = ⌈5000/T⌉`. Par la borne de Ville et une somme sur les fenêtres, la part reste au plus α : elle est rendue à 0,0045 au plus.
  - Le facteur du saboteur à niveau réparti suit la même espérance que le bloc C2.
  - Les objets de contrôle sont pertinents (facteur au moins égal à celui de C2 ; part prise au plus celle de l'accumulation continue). Je n'y vois pas d'erreur.
- **Écart de 12 % à 15 %** : il vient de la formule, qui part d'une proportion estimée sur 16 trajectoires. Le compte direct est le bon chiffre ; la note donne les deux et le dit.

## Verdict

**Conforme.** Les 16 constats sont portés juste. Aucun n'est mal porté et aucun ne manque. Il reste une imprécision mineure, sans correction exigée.

## Constat par constat

| N° | État | Vérification |
|---|---|---|
| 1 | porté juste | **Appui de Taufeeque et al. retiré :**<br>• Verdict 3 : « Le glissement lui-même n'est pas publié sous cette forme ».<br>• § 3.2 : sondes « apprises à neuf sur le modèle d'après », entraînement qui récompensait la conduite, citation « deception-specific », conclusion « pas d'appui publié direct ».<br>• Pas 7 : Pinto reste un appui, dit indirect ; Taufeeque et al. passent en « voisin » et en « contre-appui sur le rang ».<br>• Proposition 1.3 : probabilité ramenée de 0,6 à 0,5.<br>• D-9 : Taufeeque et al. ajoutés aux voisins à lire en entier.<br>• Erratum de provenance, ligne 62.<br>**Le troisième axe** reste un calcul, et sa pertinence pour nous est renvoyée à la mesure de D-3. **Fait 4 du couple v2 :** juste. Il donne les sondes réapprises, l'entraînement qui récompensait une conduite trompeuse, la sonde du domaine et les sondes de traits sans rapport qui tiennent. Le couple v1 est déclaré à ne plus servir. |
| 2 | porté juste | **Fausse alerte de l'honnête avec remise à zéro :**<br>• Verdict 3 : « 12 à 15 fois sur 100 … contre 0,7 en continu ».<br>• § 3.2 : 12, 11, 9, 5 et 1,8 sur 100, égaux à C5 (0,1238 ; 0,1144 ; 0,0874 ; 0,0463 ; 0,0179). Les deux voies de calcul sont dites, ainsi que la taille de l'échantillon.<br>**Facteurs à niveau réparti, égaux à C5 :**<br>• 6,2 et 24 pour un déplacement de 0,2 ; environ 200 à une période de 50, où 9 saboteurs sur 100 sont pris.<br>• 2,7 et 6,7 pour un déplacement de 0,1 ; « aucune » trajectoire ne sonne à une période de 50.<br>• Entre 1,2 et 1,4 à une période de 2 000.<br>• « De 1,2 à plus de 200 » : juste.<br>**Plan d'épreuve :** huit règles. La remise à zéro à niveau plein doit mourir sur le monde sans écriture ; la remise à zéro à niveau réparti doit tenir.<br>**Règle de cadence :** « 1,4 à 2,3 » à deux délais médians, vérifié (1,37 ; 1,76 ; 2,34 ; 2,05). |
| 3 | porté juste | Verdict 2, § 3.1, pas 4 et repère du bloc E :<br>• « en moyenne » rétabli ;<br>• l'audit sur l'issue est dit continuer sur ces épisodes ;<br>• le seuil d'un épisode sur 800 est juste, car 1/(0,2 × 4 000) = 1/800 ;<br>• « avec probabilité 0,95 » remplace « à coup presque sûr ». |
| 4 | porté juste | § 3.2 (b), la règle, la réserve, le verdict 3, le plan et le pas 9 : le jumeau doit être « du même état *et* honnête ». Pour une écriture nourrie des produits de l'agent, seule la voie du compte en régime de signature traverse. |
| 5 | porté juste | Le § 3.2 donne la grille, « au moins 1,4 » restreint aux déplacements de 0,1 à 0,3, « croît sans borne » et « entre une et deux fois le délai médian ». **Imprécision résiduelle, mineure :** le verdict 3 garde « au moins 1,4 dès que… » sans cette restriction ; la table des corrections la signale. |
| 6 | porté juste | « Entre 8 000 et 16 000 », avec 74 et 97 sur 100. |
| 7 | porté juste | Les deux réseaux sont nommés (23 et 117 millions de paramètres). |
| 8 | porté juste | « ce que les auteurs ne tiennent pas pour mieux que le hasard ». |
| 9 | porté juste | Verdict 7, § 4.1 point 2, section 5, pas 13 et D-4 portent :<br>• « supposé, recette non lue » ;<br>• les outils sont dits boîte blanche, non par différence ;<br>• les modèles sont dits entraînés à ne pas avouer ;<br>• l'appui est dit indirect. |
| 10 | porté juste | « que la décision N-076 retient, à faire ». |
| 11 | porté juste | « Après le sas ». |
| 12 | porté juste | Corrigé au § 3.2 (antériorité), au § 3.4 (citation retirée), au § 3.6, au monde E3 et au fait 2 du couple. Chaque fois, la menace est nommée par la supposition qu'elle viole. Aucun mode opératoire. |
| 13 | porté juste | Le titre et l'enjeu de D-2 nomment la ligne 76 du programme ; la section 5 renvoie à D-2. |
| 14 | porté juste | La comparaison au saboteur est mise hors du défaut, au § 4.1 point 1, à la proposition 2.1 et à D-3. |
| 15 | porté juste | La question finale du couple v2 ne pointe plus vers la réponse, et la limite de NeuroPots est retirée du fait 7. |
| 16 | porté juste | L'interpréteur est dit dans l'en-tête et dans le commentaire de rejeu du script. |

## Couple v2 : neutralité

**Neutre.** Les seuls changements sont les quatre phrases annoncées : faits 2, 4 et 7, question finale.

Une recherche de motifs ne trouve dans les deux fichiers aucun de ces éléments :
- noms de personne ou de modèle ;
- sigle ou identifiant du programme (GO, N-, R-, T0., G1) ;
- session ;
- chemin interne ;
- nom de famille de modèle ouvert.

La réponse n'y est pas glissée : ni les plumes, ni le troisième axe, ni le retournement, ni le verdict sur les leurres. Reste dû par la mère, comme la note le dit : la garde de motifs du collisionneur et la relecture de cloisonnement.
