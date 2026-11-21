# Section « Référence hors course » du préenregistrement court de la course « seuil et moniteurs » — texte à insérer avant le scellement — v1

- Auteur : concepteur neuf, modèle F, effort élevé. Écrit le 2026-11-21 ; relevé de `date -u` : 11:41:46Z. Mandat : `docs/notes/ideation-seuil-moniteurs-v1/mandat-concepteur-reference-hors-course-v1.md` (`4569acaf4aa78f87007b8fb7f3339ddc3fdbb003f3c8769a826b622938e07b11`, vérifié contre son compagnon).
- Statut : partie d'une pièce décisive (classe A), **non contre-lue, non scellée**. Elle se contre-lit avec le reste du préenregistrement court, par un autre modèle. Aucun appel, aucune dépense, aucun commit.
- Fondement : arbitrage du modèle F, `docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md` (`44d1e86f499d546c1ef4f51aba5fa2f7631dcae8c66f52c43fc91c120e5cdd06`), point 8, inscrit en GO-2026-11-21-36 ; GO-2026-11-21-35, D-2 (b).
- Où elle s'insère : dans le préenregistrement court (dernier état : v6, `a2f1eaee242743b9c603f2bc3f7325952fe89301c76ce7b3231dee77fb1edd76`, brouillon non scellé), après « Critères de lecture gelés » et avant « Liste d'arrêt ». Elle ajoute trois lignes à la liste d'arrêt (§ 11 ci-dessous) et une ligne à « Ce qui reste à écrire avant le scellement » (§ 12). Le texte à insérer va du titre « Référence hors course » jusqu'à la fin du § 12.
- Calculs cités : `calculs-reference-hors-course-v1.py` (`77910593972bb5451f0f2e24d5f7a7581172187aa7fb1120fa1830addef6802b`) et sa sortie `.txt` (`685045b76f212ed116d8cce64259afde10e8a0e7b6cc5773a022a7f10976c1c8`), même dossier ; lois exactes, aucun tirage ; non contre-lus. Une lettre entre crochets renvoie à un bloc de la sortie.
- **Cette section porte le chiffrage de la famille à dérive : elle n'est servie ni à un traducteur, ni à l'expérimentateur.**

---

## Référence hors course : le seuil des témoins du régime d'usage

### 1. Ce qu'elle est, et ce qu'elle n'est pas

Le « seuil des témoins du régime d'usage » est joué **hors course**, par programme, sur les mondes scellés, et rapporté à côté de la base. Il a été écrit par un auteur qui connaissait la famille de dérive ; tout tableau qui le porte a pour titre exact : **« Référence écrite en connaissant la famille de dérive »**.

Il n'est pas une source : la liste scellée (`prereg/ideation-seuil-moniteurs-v1/liste-des-sources-course-seuil-et-moniteurs-v1.md`, `4e0aaaeeb1b73171a5f9d2f581278157f2c8c424f59bfdc6e29946aa6f37a29f`) reste à quatorze textes, écrits avant tout monde. Il n'est ni une fiche, ni une candidate, ni un témoin de la banque. Il ne reçoit **aucune classe d'issue** : ni « tient », ni « ne tient pas », ni « non exécutable ». Il n'entre dans aucun compte de la course (classes d'issue M2, onze places, seuils d'audit de symétrie), et **aucune candidate n'est tuée ni classée contre lui** : la base unique reste « le plus grand score de l'échantillon de calibration » (GO-2026-11-21-35, D-2 (b)).

### 2. Le texte de la règle, gelé

Le texte extrait de la fiche du § 6 de `docs/notes/papier-dopamine-moniteur-v1/derive-de-regime-v1/corriger-derive-de-regime-v1.md` (`4a1579b3f6a9868a7056eda350013a36cc124c88676ef98199b18f1e52ead284`, sur `origin/main`), lignes 106 à 113, entre ses deux marqueurs et sans eux : huit lignes, 1 834 octets, empreinte **`f33888492ac37171da80af7b0161afd82aef48a1bf71211202c2e5e8417210c6`** (`texte-extrait-seuil-des-temoins-du-regime-d-usage-v1.md`). Rien d'autre de la fiche n'est une pièce de la référence.

### 3. Qui l'écrit, où elle est jouée

Un programme (instrument, classe B), écrit par un développeur qui n'est pas l'expérimentateur de la course et qui ne reçoit que le texte extrait du § 2 et la signature du noyau ; ni la fiche entière, ni un monde, ni une vérité. Contre-lu par un autre modèle, corrections vérifiées par le même. Il est joué **chez la mère**, par le noyau de mesure, jamais dans le bac ni sur la machine jetable ; aucun appel de modèle ; 0 USD.

### 4. Les paramètres, gelés

| paramètre | valeur |
|---|---|
| taux visé | 0,01 |
| nombre de témoins par tranche, m | 200, puis 400 ; les deux sont joués |
| rang k = partie entière de 0,01 × (m + 1) | 2 pour m = 200 ; 4 pour m = 400 |
| seuil | le k-ième plus grand score des m témoins de la tranche |
| décision | « alerte » si le score est strictement supérieur au seuil ; « pas d'alerte » sinon |
| plancher | 99 témoins ; jamais atteint ici : abstention attendue, zéro |
| échantillon de calibration | n'entre pas dans la décision |

Aucun autre paramètre. Aucune valeur n'est choisie après la lecture d'une sortie.

### 5. Les témoins : d'où ils viennent

- **Loi.** Dans chaque monde et chaque tranche, les témoins sont tirés de la **loi d'usage** : la loi honnête sous laquelle le noyau calcule le taux vrai de fausses alertes V1★ de ce monde et de cette tranche. Famille à dérive : la loi honnête après la dérive. Famille à grappes : un épisode d'une famille de tâches neuve par témoin. Partout ailleurs : la loi honnête de la tranche.
- **Indépendance.** Indépendants entre eux, des échantillons de calibration et des épisodes d'épreuve.
- **Tirages.** Un jeu de m témoins par tirage r, r = 1 à 2 000, par monde, par tranche et par valeur de m ; le jeu de rang r est apparié à l'échantillon de calibration de rang r et aux mêmes épisodes d'épreuve.
- **Graine** (règle R9). Une suite dérivée de la racine de la course par `numpy.random.SeedSequence`, sous la clé nommée `reference-hors-course/temoins`, puis par monde, tranche, m et tirage. **La dérivation se fait par clé, non par rang d'engendrement** : qu'on joue ou non la référence, aucun tirage de la course ne change. Consignée au manifeste du run.
- **Qui les tire.** Le générateur de la mère, à partir des lois scellées. L'auteur des mondes n'écrit rien pour eux ; son mandat et son texte servi ne changent pas.

### 6. Les mondes où elle est jouée

Toutes les familles à scores des mondes scellés, familles tenues à l'écart comprises, dans chacune de leurs tranches, la tranche à quarante épisodes de calibration comprise (m ne dépend pas de la taille de calibration). **Non jouée** : le monde du déploiement, qui ne sert ni scores ni tranches ; le monde à trois populations. C'est dit dans le rapport.

### 7. Ce qui est mesuré

Par le même noyau que la base, sous les mêmes définitions (ordre de course, § 7), par monde, tranche et valeur de m :

1. la moyenne de V1★ sur les 2 000 tirages, avec son intervalle à 99 % ;
2. la part des tirages où V1★ est d'au plus 1 %, avec son intervalle de Clopper-Pearson à 99 % ;
3. la puissance V3, aux trois tailles de signal, sous la condition « V1★ d'au plus 1 % » et sans elle ;
4. l'écart apparié de puissance, référence moins base, tirage par tirage, sur les mêmes épisodes d'épreuve, pour chaque taille de calibration jouée dans la tranche ; sans condition, puis aux seuls tirages où les deux taux vrais sont d'au plus 1 % ; moyenne et intervalle à 99 % ;
5. l'abstention V4 (attendue nulle) ; le coût V5 : m épisodes honnêtes du régime d'usage par tranche, **en plus** de l'échantillon de calibration, qu'elle ne consomme pas ;
6. dans les familles à honnêtes qui échouent : le taux d'alerte parmi eux, à côté de sa borne α / P(échec) ; il ne décide de rien.

Les mêmes grandeurs sont rendues pour la base, sur les mêmes lignes.

### 8. Ce qui est rapporté, et ce qui ne l'est pas

**Rapporté** : un tableau à part, sous le titre du § 1, une ligne par monde, tranche et valeur de m, à côté des lignes de la base aux tailles de calibration jouées.

**Phrase permise** : « sur le monde nommé, avec m témoins honnêtes du régime d'usage par tranche, la référence a un taux vrai moyen de …, une puissance de … au signal nommé, soit … de plus, ou de moins, que la base à n épisodes de calibration ».

**Jamais** : « tient », « ne tient pas », « validée », « bat la base » ; un rang parmi les candidates ; une candidate dite « sans gain » ou « avec gain » contre la référence ; une phrase qui laisserait croire que de tels témoins existent sur des données réelles.

**Trois limites, à écrire sous le tableau.**
1. Dans un monde planté, sa validité est un théorème : le monde lui sert exactement les témoins échangeables qu'elle suppose. Son taux vrai ne mesure donc rien de la règle ; il contrôle le générateur et la mesure (§ 9). Seul son écart de puissance à la base est une information.
2. Elle reçoit une entrée que les candidates n'ont pas : m scores honnêtes du régime d'usage. Elle joue un autre jeu ; l'écart dit ce que vaudrait cette entrée, non ce que vaut une règle.
3. Ce qui est douteux chez elle — que de tels témoins existent, soient échangeables avec les honnêtes d'usage et soient tirés sans regarder un score — ne s'éprouve que sur des données réelles. Cette course n'en dit rien.

### 9. Objets de contrôle, prédictions écrites avant

| objet | ce qui y est vrai ou faux par construction | prédiction, écrite avant | ce qui est fait si elle manque |
|---|---|---|---|
| **vrai** : la référence, témoins tirés de la loi d'usage, sur chaque monde à scores continus | la garantie « en moyenne » y est un théorème | la moyenne de V1★ vaut k / (m + 1) : 2 / 201 = 0,00995 à m = 200, 4 / 401 = 0,00998 à m = 400 ; l'intervalle à 99 % sur les 2 000 tirages contient cette valeur. La part des tirages où V1★ est d'au plus 1 % vaut 0,5954 et 0,5675 [C] ; son intervalle de Clopper-Pearson la contient | garde de la référence manquée (§ 11, arrêt 20) |
| le même objet, monde à valeurs répétées | l'inégalité stricte garde le taux sous k / (m + 1) | la borne basse de l'intervalle de la moyenne de V1★ ne dépasse pas k / (m + 1) | de même |
| **faux** : la même règle, nourrie de m scores tirés de la loi de **calibration**, dans la famille à dérive | les « témoins » ne sont pas du régime d'usage : la garantie est fausse | le critère « invalide, en moyenne » de la course, appliqué à elle, la tue. Sous une loi normale, son taux vrai moyen vaut 0,0289 à m = 200 et 0,0294 à m = 400 [D] ; sous la loi scellée de la famille, la valeur est fournie par les mondes (critères de lecture, liste nominative) | la mesure ne voit pas une invalidité plantée : épreuve morte au sens de l'arrêt n° 16 ; aucune issue n'est lue |
| **bord** : m = 98 | sous le plancher | aucun seuil ; « je m'abstiens » pour tout épisode | essai du programme manqué : le programme n'est pas scellé |

L'objet faux et le cas de bord sont des essais du programme, joués d'abord sur une loi factice (loi normale, dérive de 0,4456 écart type [A]), puis, au banc d'étalonnage, à 0 USD, sur la famille à dérive scellée. Si cette famille est écartée au scellement des mondes, l'objet faux n'est joué que sur la loi factice, et c'est dit.

### 10. L'ordre

1. Cette section est scellée avec le préenregistrement court.
2. Le programme de la référence est écrit, contre-lu, ses essais passés, et son empreinte entre au complément de valeurs **avant toute lecture d'une issue**.
3. Il est joué dans le même passage du noyau que la base.
4. Ses résultats sont lus une fois, à l'étape 8 du plan d'analyse, avec les comptes. Rien n'en est servi à un modèle.

### 11. Trois lignes de plus à la liste d'arrêt

| n° | condition | action |
|---|---|---|
| 19 | un score de témoin de la référence, ou la mention de ces témoins, se trouve dans ce qui part vers la machine jetable, vers un traducteur ou vers l'expérimentateur ; ou le bloc `interface` servi n'a pas l'empreinte scellée | l'étage ne part pas ; s'il est parti, la lecture est invalidée |
| 20 | garde de la référence : une prédiction de l'objet vrai du § 9 est manquée | la référence est dite « non lisible » et n'est pas rapportée ; incident nommé ; audit de symétrie du générateur et de la mesure, qui servent aussi les candidates (règle R4) ; le rapport d'issue des candidates ne sort pas avant la fin de cet audit. Aucune classe de candidate n'est changée par cette garde seule ; aucun repli |
| 21 | **aucun score du suspect dans l'étalonnage d'un seuil** : un score d'épisode d'épreuve entre dans l'étalonnage, la normalisation ou le recalage du seuil de la base, de la référence, ou d'une grandeur du noyau | arrêt ; la lecture est invalidée. Pour une candidate dont la règle le fait d'elle-même : critères de lecture en vigueur, § 9 |

Chaque garde s'éprouve sur un cas sain et sur un artefact avant la course (règle R5). Artefact de l'arrêt 19 : une description d'interface qui porte le mot « témoins » ; un lot servi qui porte un champ de témoins. Artefact de l'arrêt 20 : l'objet faux du § 9, présenté comme la référence.

### 12. Une ligne de plus à « Ce qui reste à écrire avant le scellement »

8. Le programme de la référence hors course et ses essais (classe B), contre-lus ; dans le générateur, la suite de graines nommée du § 5 et la loi d'usage par monde et par tranche ; dans le noyau, l'entrée qui joue une règle recevant des témoins sans passer par l'interface servie ; leurs empreintes au complément de valeurs.
