# Erratum 3 à `interface-lots-5-6-7-repli-v1.md` — identifiant de tentative, formats d'attestation et d'étiquettes

Écrit le 2026-11-22 vers 11:15Z par la session de l'organisme. La mère l'a accordé à 11:09Z comme une décision de routine (code et interface). Il complète les errata 1 et 2, sans les modifier.

## 1. Identifiant de tentative
- **Champ** : `id_tentative`, chaîne fermée, de la forme `T` + génération sur 2 chiffres + `-` + numéro de chaîne sur 4 chiffres + `-` + rang de repli sur 1 chiffre.
  - Expression : `^T[0-9]{2}-[0-9]{4}-[0-2]$`.
  - Exemple : `T01-0007-1`.
- **Unicité** : dans une course, chaque identifiant est unique.
- **Numérotation** : le numéro de chaîne croît de 1 à chaque chaîne d'une même génération, en commençant à 0001. Les tentatives d'une même chaîne partagent le numéro et diffèrent par le rang.
- **Lignes de tentative** : chaque ligne `type_ligne` = `tentative` porte son `id_tentative`.
- **Lignes de fiche** : chaque ligne `type_ligne` = `fiche` porte l'`id_tentative` de la tentative qui l'a servie.
- **Rattachement** : une fiche se rattache à sa tentative **par cet identifiant seul**. L'ancien rattachement du lot 7 v1 (génération, case, espèce, rang) devient un contrôle de cohérence. Un désaccord entre les deux est un refus, pas un choix.
- **Porteurs** :
  - le lot 5 (registre) écrit le champ et refuse une ligne sans lui, ou hors de sa forme ;
  - le lot 6 (course) le produit ;
  - le lot 7 (mesures) le lit.

## 2. Format de l'attestation de relecture (adopté)
Il est adopté tel que le lot 7 v1 le lit : `lire_attestation` dans `lot-7-vehicule-na-v1/paquet/orchestrator/pole/mesures_na_v1.py` (`428ebefc…`), l. 245 à 255.
- JSON scellé, à deux clés exactement :
  - `format` = `attestation-relecture-na-v1` ;
  - `etiquettes` : un objet { identifiant de fiche → étiquette }.
- Étiquettes en liste fermée : `gardée`, `au coffre`.
- **Contrôles par programme**, au calcul des mesures (arrêt n° 15) :
  - forme exacte ;
  - étiquettes dans la liste ;
  - chaque fiche passée du registre a exactement une étiquette, et aucune clé n'est étrangère au registre.

## 3. Format des étiquettes d'antériorité (adopté)
Il est adopté tel que le lot 7 v1 le lit : `lire_anteriorite`, même fichier, l. 258 à 278.
- JSON scellé.
- Clés exactement :
  - `format` = `etiquettes-anteriorite-na-v1` ;
  - `branche` ∈ {`avec`, `sans`} ;
  - `etiquettes` : { identifiant de fiche → étiquette } ;
  - `temoins` : { identifiant de témoin → issue } ;
  - et, en branche `avec` seulement, `classes` (valeurs ∈ {`recette`, `réalisation`, `variante`, `mode candidat`}) et `desaccords` (entier positif ou nul).
- Étiquettes : `antériorité trouvée`, `antériorité partielle`, `non tranchée`, `aucune antériorité trouvée`, ou `non lue` (au-delà de la borne de lecture de 60 fiches).
- Issues de témoin : les étiquettes ci-dessus, les classes ci-dessus, `passée` ou `manqué`.
- **Contrôles par programme** :
  - forme exacte ;
  - listes fermées ;
  - au plus 60 fiches lues ;
  - chaque fiche passée a une étiquette ;
  - les témoins sont ceux du jeu scellé.

## 4. À faire par les lots
- **Lot 5 v4 ou lot 6 v5** : porter `id_tentative` au registre.
- **Lot 7 v2** : rattacher par `id_tentative` et ajouter le contrôle des clés de l'attestation contre le registre (§ 2), s'il ne le fait pas déjà.
