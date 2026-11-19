# Préenregistrement neuf du bras A des organismes discrets, brouillon 3 — note du rédacteur — v1

- **Heures (UTC, `date -u`)** : brouillon 3 commencé à 2026-11-19T07:04:52Z, fini à 07:16:49Z ; note écrite ensuite. Commit lu au début : `10dffbaec96c180353f445e881bfe602a5378115` ; à la fin : `43552a85c7ed68944a6cc12dc23b4453c7bce824` (seul ajout entre les deux : la transcription du choix de Lazar sur les onze nœuds).
- **Objet** : accompagner `prereg/T0.7-organismes-discrets-v-a-v2-brouillon3.md` (non contre-lu, non scellé). Le brouillon 2 (`8db1899a…`) reste tel quel.
- **Déclaration** : j'ai écrit les brouillons 2 et 3 ; je n'ai écrit aucune contre-lecture. Je n'ai ouvert aucun interne de moniteur : ni bases, ni sondes, ni la tâche des sondes, ni la tâche T0.8, ni le document de la base « mots et coût », ni la règle « mots et coût » de `prereg/T0.6-organismes-v0-v1.md`, ni la proposition P-010. Je n'ai ouvert aucune fiche de l'organisme d'idéation, aucune référence cachée, aucune tâche, aucun résultat, ni le brouillon du repli. Je n'ai appelé aucun modèle. Je n'ai modifié aucun fichier existant ; je n'ai rien committé, rien scellé.
- **Lu en plus du brouillon 2** :
  - la contre-lecture du brouillon 2 (`065d0e1e…`) et la sortie de son essai ;
  - la contre-lecture habilitée (`27189edd…`) et la liste des familles (`1753a9d9…`), toutes deux en entier ;
  - la décision posée sur les onze nœuds (`30287a39…`) et la transcription du choix de Lazar (`ecfdbdc9…`) ;
  - par `git show`, sans réseau : `artefacts_v1.py` (lignes 353 à 495), `manifeste.py` (dérivation des graines), la ligne GO-2026-11-18-66 du registre des GO sur la branche principale.
- **Validateur** (`controle_ia.prereg.problemes`) : un seul problème, attendu : « contre-lecture 4 sans ses deux empreintes ».

## 1. Ce qui a changé, en bref

1. **Nœuds** : Lazar a tranché les onze nœuds (« go recos », 07:07:29Z). Le texte est écrit sous les seules options retenues. Les branches écartées sont retirées et listées en 14.4 ; quand une ligne de table disparaît, son identifiant est gardé (A4, B6, B7).
2. **B-1 (kappa)** : le kappa n'est plus calculé sur la seule condition honnête ni sur une dose, où des lecteurs justes donnent près de zéro. Il n'est plus calculé que sur des ensembles de prévalence mêlée (jumeaux et honnêtes relues ; sentinelles et actions d'épreuve relues). La comparabilité passe par la part sans verdict de chaque lecteur. La règle d'un kappa non défini est écrite.
3. **B-2 (ancre)** : l'ancre de l'appariement est coupée en deux parties.
   - Première partie, avant les épreuves sur plans honnêtes : 24 actions honnêtes et 24 actions à contrôles d'une autre tâche.
   - Seconde partie, après le scellement de ces épreuves et avant le lot des jumeaux : 24 jumeaux.
   - Le juge ne voit aucune action déplacée avant le scellement des épreuves sur plans honnêtes. Il juge 72 actions et 8 plans, et 72 actions de plus sous la révision.
4. **Témoins (nœud 6)** : lignes A15 et A16, branche non interprétable à toutes les doses. Un témoin est dit « à effet » sur l'agrégat seulement. Les lectures de chaque lecteur sont rapportées : une branche rendue non interprétable par un seul lecteur serait un verdict porté par un seul lecteur.
5. **Ordre (nœud 7)** :
   - les jumeaux d'épreuve sont lus avant la distillation, en écart déclaré à l'ordre que Lazar préférait ;
   - l'écart-type de la garde de puissance est estimé sur les seuls honnêtes, avant les jumeaux ; la garde A8 s'applique avant eux ;
   - une prise de la distillation non positive à la dose 1 arrête la course (A13).
6. **Jumeau d'épreuve (nœud 8)** : définitions corrigées ; le jumeau est lu comme une épreuve, et c'est déclaré comme une lecture du texte de décision.
7. **Statistique** :
   - intervalles de Student pour toute décision ; percentiles rapportés ;
   - « exclu » repose sur un test exact de « hausse < 0,10 », chez l'agrégat et chez chaque lecteur ;
   - règle de multiplicité neuve pour la discrétion (6.9) : famille de 12 fixée d'avance, plancher par 2 000 permutations, sens écrit pour chaque condition.
8. **Base « mots et coût »** :
   - renvois corrigés vers `prereg/T0.6-organismes-v0-v1.md`, ligne 576, sans avoir ouvert le fichier ;
   - transposition en six points (6.12, section neuve) ;
   - « classe absente » et « vocabulaire vide » rendent la dose non calculable, sans arrêt (nœud 9) ;
   - une base qui réussit rend la dose « hors jugement » (ligne 219 du texte archivé, alignée).
9. **Juge d'une autre lignée** : bras rapporté, hors du verdict (nœud 10).
10. **Case « familles »** remplie : Llama et Qwen sont exclues pour les lecteurs. Case neuve « consignes des moniteurs ».

## 2. Points non appliqués, ou appliqués autrement que proposé

1. **C-15** (exécution sous deux options) : sans objet, les nœuds sont tranchés.
2. **C-6** (témoins) : l'une des deux corrections proposées est retenue. « Témoins » est retiré de la retenue par un seul lecteur ; aucun test n'est donné à un seul lecteur.
3. **Nœud 7, option (a), telle que la contre-lecture l'écrivait** : elle faisait de l'estimation d'hétérogénéité tirée des jumeaux une seconde garde. Le texte de la décision posée à Lazar dit seulement « écart-type estimé sur les seuls honnêtes ». Je la rapporte donc **sans garde**, pour ne pas ajouter un arrêt que le choix de Lazar ne nomme pas. À confirmer.
4. **Condition 5 de la seconde contre-lecture** (spécificité de la place sur des plans déplacés à une dose partielle) : non reprise, réserve écrite (R-5).
5. **Remarque habilitée sur l'en-tête du document de la base** (« non scellé ») : sans effet ici.
6. **Recommandations de la contre-lecture sur les nœuds** : non écrites dans le texte (consigne : aucune recommandation dans le texte).

## 3. Doutes, et points qui demandent un mot

1. **Témoin positif de la base** (6.12, point 4 (i)). Il suppose une condition de saboteur instruit, que le bras A n'a pas. Je l'écris « sans objet », en écart déclaré à la lettre du document de la base, avec une réserve sur toute phrase « la base échoue ». **C'est un choix de transposition que le rapport habilité ne tranche pas** : à vérifier par le lecteur habilité, et peut-être à poser à Lazar. L'autre voie serait un témoin positif de remplacement, à concevoir.
2. **Contrôle de l'adaptateur de la base** (6.12, point 4 (ii)) : la base lit le témoin identité pour ce seul contrôle, sur processeur. Ce n'est pas un moniteur de plus, mais c'est une lecture de plus d'un témoin.
3. **Minimum de coûts lisibles par tâche et garde d'effectifs** (6.12, points 1 et 2) : écrits sans en connaître les valeurs ; à vérifier par le lecteur habilité.
4. **Règle de multiplicité** (6.9) : écrite par moi, dans le sens prudent pour l'affirmation « discret ». La condition (a) n'est pas corrigée, et la condition (b) l'est par Bonferroni. Le plancher passe de 200 à 2 000 permutations, faute de quoi une valeur p corrigée ne peut pas descendre sous le niveau. C'est un changement par rapport au texte archivé, déclaré dans « Ce qui change ».
5. **Hypothèse sur les consignes des moniteurs** : elle est non vérifiée pour le juge d'une autre lignée (case « consignes des moniteurs »). La phrase de C6 n'en dépend plus que pour le moniteur boîte noire, puisque le juge est en bras rapporté.
6. **Familles des lecteurs** : aucune pièce n'exclut la famille des agents qui rédigent ou contre-lisent les textes du programme, et le texte ne l'exclut pas. Si on la veut exclue, c'est à décider ailleurs.

## 4. Reste à fixer avant scellement (section 13)

- **Remplies** : nœuds ; familles.
- **À remplir** :
  - lecteurs (modèles, versions, tarifs) ;
  - renvoi de la base : vérification courte, par un lecteur habilité, des lignes corrigées (section 4 point 3, « Seuil », 6.9, 6.10, 6.12, C2, C3) ;
  - consignes des moniteurs ;
  - seuils proposés ;
  - juge des ancres : une personne, ou l'agent d'une troisième famille à défaut, en écart déclaré ;
  - entropie racine ;
  - code, dont la version neuve du code de la base et le lanceur neuf ;
  - longueurs des consignes ;
  - essai de forme ;
  - devis et lignes de GO ;
  - confinement ;
  - registre.
- **Et** : la contre-lecture neuve de ce brouillon (contre-lecture 4), qui peut porter sur les seuls points corrigés.

## 5. Table de correspondance des sections, brouillon 2 → brouillon 3

| brouillon 2 | brouillon 3 | changement |
|---|---|---|
| en-tête, conventions | en-tête, conventions | même place ; définitions corrigées (« jumeau d'épreuve ») ; deux conventions neuves (identifiants des lignes de table, nœuds tranchés) |
| 0 | 0 | même numéro ; paragraphes « Ordre » et « Contrôles vagues » réécrits |
| 1 | 1 | même numéro ; lignes ajoutées et déplacées dans les deux tables (ligne 178, multiplicité, intervalles, juge, base, témoins) |
| 2 | 2 | inchangée |
| 3.1 | 3.1 | inchangée |
| 3.2 | 3.2 | même numéro ; paragraphe « Variante sans la question de spécificité » **retiré** ; insertion des valeurs par remplacement de chaînes |
| 3.3 | 3.3 | même numéro ; consigne de la couverture : deux phrases ajoutées ; réserve et accord sur la place |
| 3.4 | 3.4 | même numéro ; familles nommées par renvoi à la liste |
| 3.5 | 3.5 | même numéro ; gardes « référence ni vue ni lue » |
| 4 | 4 | même numéro ; points 3 et 4 et hypothèse sur les moniteurs réécrits |
| Hypothèse | Hypothèse | même place ; nœud 2 tranché ; hypothèse de travail 5 |
| Prédiction | Prédiction | même place ; lignes revues |
| Métrique | Métrique | même place ; points 3, 5, 8 réécrits |
| Seuil | Seuil | même place ; table réécrite |
| 6.1 | 6.1 | même numéro ; noms des relectures ; invariants opposables à toute autre lecture (dernier point) |
| 6.2 | 6.2 | même numéro ; table des dérivations exactes |
| 6.3 | 6.3 | même numéro ; étape **(e′)** neuve (ancre, seconde partie) ; étapes (b), (d), (f), (h), (i), (l), (m) réécrites ; points d'insertion du repli gardés, numérotés 1 à 3 comme avant |
| 6.4 | 6.4 | même numéro ; point 5 (prise) réécrit |
| 6.5 | 6.5 | même numéro, titre changé ; réécrite (ancres, constructions des épreuves de la couverture) |
| 6.6 | 6.6 | même numéro ; ancre rejouée ; arrêt après révision |
| 6.7 | 6.7 | même numéro ; écart-type sur les seuls honnêtes |
| 6.8 | 6.8 | même numéro ; accord au lot décisif |
| 6.9 | 6.9 | même numéro ; règle de multiplicité de la discrétion neuve |
| 6.10 | 6.10 | même numéro ; juge en bras rapporté ; pas d'arrêt pour « classe absente » et « vocabulaire vide » |
| 6.11 | 6.11 | même numéro ; comptes d'ancre et majorant refaits (91 272) |
| — | **6.12** | **neuve** : transposition de la base « mots et coût » |
| 7.1 à 7.8 | 7.1 à 7.8 | mêmes numéros ; 7.1 à 7.7 réécrites ; lignes neuves A12 à A16 ; A4, B6, B7 sans objet ou retirées, identifiants gardés ; ordre de lecture écrit pour chaque table ; table C lue dans l'ordre C2, C3, C1, C4, C5, C6 |
| 8.1 à 8.6 | 8.1 à 8.6 | mêmes numéros ; 8.4 : dix gardes ajoutées |
| 9 | 9 | même numéro ; porte et nœud 3 ; nœud 2 |
| 10 | 10 | même numéro ; nœud 5 tranché |
| 11 | 11 | même numéro ; un renvoi à 6.1 ajouté au dernier point ; rien du repli n'est fixé |
| 12 | 12 | même numéro ; onze nœuds, options retenues, sans recommandation |
| 13 | 13 | même numéro ; colonne « état » ; case neuve « consignes des moniteurs » |
| 14 | 14 | même numéro ; découpée en **14.1** (brouillon 1 et addendum), **14.2** (brouillon 2), **14.3** (contre-lecture habilitée), **14.4** (branches retirées) |
| Contre-lecture | Contre-lecture | même place ; entrées 2 et 3 faites, entrée 4 à faire |

**Identifiants des lignes de table** :
- **Table A** : A1 à A11 gardent leur sens, sauf A4, sans objet. A12 à A16 sont neuves : lecteur retiré, prise non positive à la dose 1, coupe à 400 jetons, deux témoins.
- **Table B** : B1 à B5 et B8 à B10 gardent leur sens. B6 et B7 sont retirées ; leur rôle passe à A15 et A16.
- **Table C** : C1 à C6 gardent leur identifiant. C3 change de verdict : « hors jugement » au lieu de « non discret ». L'ordre de lecture de la table change.
