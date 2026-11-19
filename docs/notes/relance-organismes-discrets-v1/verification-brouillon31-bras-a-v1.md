# Vérification du brouillon 31 du texte neuf du bras A des organismes discrets — v1

- **Vérificateur** : Claude Opus 5.5 (`claude-opus-5-5`), contre-lecteur des brouillons 21 à 30. Je juge ; je ne corrige rien.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon31.md` (`6fd71ee2c775…`). Note : `fea0c8821dbe…`.
- **Méthode** :
  - comparaison des brouillons 30 et 31 phrase par phrase, faite par programme ;
  - lecture des blocs touchés et de leur contexte : conventions, ligne 199 ; 6.9, lignes 743 et 760 ; 8.4, lignes 1011 et 1019 ; 13.1, ligne 1325 ; 13.2, ligne 1335.
  - Aucun code ouvert, ni les pièces de demandes, dont j'ai seulement pris les empreintes.

## Verdict : **engageable**

- Les deux points de ma vérification du brouillon 30 sont tenus (C-1, M-1).
- La règle « un seul nombre par dose » ne touche aucune règle de jugement.
- **Aucune règle de jugement ne change.**
- L'intégrité tient, et l'incident déclaré n'a rien laissé de faux.
- Une remarque mineure, sans effet sur l'engagement (M-1).

## 1. L'incident du compagnon : vérifié par programme

- Le compagnon actuel `prereg/…-brouillon31.md.sha256` porte `6fd71ee2c7756d07418155e7775ceba67ece71b438fb415838964652983a9768`. C'est l'empreinte recalculée du fichier, et `verifier` répond « OK ».
- Le brouillon 31 **diffère** du brouillon 30 : la comparaison octet par octet les dit différents. L'empreinte du brouillon 30, `0b51d1dd…`, n'est pas celle du 31. La différence est faite des 24 remplacements déclarés.
- Le compagnon a été écrit 8 secondes après le texte (horodatages du système de fichiers), ce qui s'accorde avec le récit de la note.
- Aucun fichier suivi par git n'est modifié dans l'arbre de travail. Les brouillons 20 à 30 répondent tous à leur compagnon.
- **L'incident n'a laissé aucune trace fausse.**

## 2. Les points demandés

| point | état | endroit |
|---|---|---|
| ma vérification du brouillon 30, C-1 : révocation entrée pendant une panne | **tenu** | Conventions, ligne 199 : seule l'étape (n), après le fichier scellé de l'étape (m), relève de la lecture déjà partie. Une révocation entrée pendant une panne sans résultat est entrée **avant** la lecture. Avant le rejeu, le programme du constat est rejoué à titre de contrôle : il n'écrit aucun fichier, laisse intact le constat d'origine (R12) et rend sa sortie au manifeste. Contrôle malsain : le rejeu ne part pas. 6.9, ligne 760, le redit. 8.4, ligne 1019 : un cas sain et trois artefacts (rejeu parti sur un contrôle qui voit une ligne neuve, rejeu sans contrôle, contrôle qui écrit un fichier). La contradiction avec le brouillon 26 est levée. |
| ma vérification du brouillon 30, M-1 : faux constats malsains | **tenu** | Conventions, ligne 199, et 13.2, ligne 1335 : consigne de tenue du registre. Entre la ligne de GO d'une reprise et la fin de la lecture, aucune ligne ne la nomme, sauf pour la révoquer. La ligne d'inscription ne nomme que l'empreinte. Un arrêt du constat est rapporté avec la ligne qui l'a causé, et la ligne de GO neuve la cite et dit si la livraison était déjà produite. La consigne est portée à la session principale (demande 29). C'est une consigne, non une garde : sans elle, la règle reste et seul le coût revient (réserve 2 de la note). |
| « un seul nombre par dose » pour la somme et le maximum de l'agrégateur | **juste** | 6.9, ligne 743 : par dose, un nombre de 0 à 1 est rapporté. Toute table, liste ou texte à sa place est « non rapportée », et rien de son contenu n'est rapporté. 8.4, ligne 1011 : cas sain. La raison relève du cloisonnement : une table pourrait porter des nombres de 0 à 1 qui ne sont pas des lectures, une part, un poids ou un seuil, donc un interne possible. Le filtre « de 0 à 1 » ne les arrêtait pas. |

## 3. Règles de jugement

- **Aucune ne change.** Par programme, sont identiques au brouillon 30 :
  - la section 12 ;
  - les sections 7.1 à 7.8 ;
  - la section 10 ;
  - et aussi l'hypothèse au seuil, les sections 6.1 à 6.8, 9 et 11.
- Les fiches 9 à 12 parties à Lazar restent mot pour mot dans le texte.
- **Le contrôle avant le rejeu** est une garde de lancement. Rien n'est lu, aucune issue n'est fixée, et le remède reste un mot de Lazar. Il rend le texte cohérent avec sa propre règle : une révocation entrée avant la lecture l'empêche de partir.
- **« Un seul nombre par dose »** porte sur des grandeurs rapportées sans état ni verdict (GO-2026-11-19-48). L'aire de la moyenne, qui fait l'état de l'agrégateur, reste sous la table des formes. C'est donc une règle de rapport et de cloisonnement, non de jugement.

## 4. Mineur

- **M-1. GO-2026-11-19-48 veut la somme et le maximum « calculés et rapportés ».** Si le module rend autre chose qu'un nombre par dose, ils seront « non rapportés ». Le texte le demande au module (demande 31). Il faudrait que l'épreuve de forme, avant toute dépense, vérifie que cette demande est tenue, pour que le mot de Lazar soit respecté dans les faits et pas seulement dans le texte. Une ligne en 13.1, à la demande 3 (épreuve de forme), suffirait.

## 5. Intégrité (vérifiée par programme)

| contrôle | résultat |
|---|---|
| brouillons 20 à 30 intacts | compagnons vérifiés |
| brouillon 31 | compagnon juste (`6fd71ee2…`) ; différent du brouillon 30 |
| section 12 ; 7.1 à 7.8 ; section 10 | **identiques au brouillon 30** ; fiches 9 à 12 mot pour mot dans le texte |
| hypothèse au seuil ; 6.1 à 6.8 ; sections 9 et 11 | identiques au brouillon 30 |
| citations à la lettre | brouillon 20 : 935 sur 935 retrouvées ; brouillon 30 : 1 200 sur 1 200 retrouvées |
| titres | 53 ; seul le titre de niveau 1 change |
| consignes figées (3.2 et 3.3) | sections égales octet pour octet à celles du brouillon 20 ; `98a9bd34d280…`, `ecf590eae0c0…` |
| validateur `problemes()` | deux problèmes, les attendus |
| marque des cases | huit lignes (1312, 1313, 1315, 1316, 1318, 1323, 1324, 1325), toutes en 13.1 |
| table d'en-tête, lignes neuves | empreintes égales : brouillon 30, sa note, ma vérification, vérification de cloisonnement des demandes en version 5, pièce du développeur en version 6 (`4937274b…`). La pièce du lecteur en version 6 a son compagnon et cite le brouillon 31 par son empreinte entière, comme la note le dit. Le texte ne porte pas son empreinte, pour éviter une boucle, et c'est correct. **Aucune empreinte de fichier cloisonné prise.** |

## 6. Ce qui sépare encore le texte du scellement

1. **Mots de Lazar**, chacun reporté ensuite au texte en retirant les rédactions écartées :
   - point 21 (fiche 12) ;
   - point 19 (fiche 10) ;
   - point 18 (fiche 9, défaut (a) le 21 novembre vers 14:30Z) ;
   - point 20 (fiche 11), seulement si la séparation parfaite peut déclencher le motif ;
   - point 17, le schéma de permutation ;
   - les lecteurs et la sortie maximale du lecteur Carbon ;
   - l'écart à R9 ;
   - la lecture du juge, après son chiffrage.
2. **Pièces de la session principale**, d'après les demandes en version 6, qui doivent d'abord passer leur relecture de cloisonnement (réserve 4 de la note) :
   - la version du module qui respecte la table des formes ;
   - l'épreuve par retrait et l'épreuve de forme ;
   - les chaînes du module ;
   - les causes des motifs ;
   - la pleine précision ;
   - un seul nombre par dose pour l'agrégateur ;
   - la forme de `lectures` ;
   - `piece_source` ;
   - les chemins de la garde statique ;
   - le lanceur ;
   - le renvoi de la base ;
   - le code des moniteurs à modèle de langue ;
   - les formes d'inscription et de révocation au registre, et la consigne de tenue (demande 29).
3. **Session de relance** :
   - le code de l'analyse en version 9, aligné sur le brouillon 31, contre-lu par un autre modèle, puis son commit ;
   - l'entier racine des graines, après le mot sur R9.
4. **Contre-lecture 10**, sur le texte aux cases remplies, par un agent Opus 5.5 neuf (ce ne peut être moi). Puis la vérification habilitée, qui reprend les quatorze lignes héritées de la table d'en-tête. Puis un validateur sans aucun problème, et le scellement.

## 7. Fichiers ouverts

- Le brouillon 31 : par différence ; les lignes citées en tête.
- Les brouillons 20 et 30, par programme.
- La note du brouillon 31.
- Le fichier des fiches du brouillon 23, par programme.
- `src/controle_ia/prereg.py` (`problemes()`).
- Pour leur seule empreinte ou une recherche de chaîne : les pièces de demandes en version 6, la vérification de cloisonnement des demandes en version 5, la note du brouillon 30.
- Rien d'autre : aucun code, aucun interne de moniteur, aucune clé, aucun appel de modèle ni appel réseau, aucun sous-agent. Un seul fichier écrit, celui-ci, scellé ; rien committé.
