# Le juge et la sélection des cartes écartées (Astra, Carbon) — note de conception — v1

- **Statut : note de conception, brouillon 1, à contre-lire.** Écrite par un rédacteur neuf (modèle F), sur mandat de la mère (GO-2026-11-19-65, R-3845, numéros donnés par le mandat ; je ne les ai pas trouvés sur `main` au commit `2e4194cb`), le 2026-11-19 vers 13:45Z (`date -u`). Pièce de travail. Processeur seul, aucune dépense, aucun appel de modèle. **Ce texte propose ; la mère soumet à Lazar.**
- **Demande de Lazar, verbatim** : « il faut que le juge puisse selectionner les cartes du type d'astra qui ont ete ecartees , idem celles de carbon » ; « peut etre mettre un consortium de juges qui votent, un de chaque modele ? » ; « ou bine plus de juges astra pour reequilibrer le biais negatif de notre juge envers astra ? ».
- **Lu**, sur `main` (commit `2e4194cb`), empreintes recalculées : les pièces du tableau du § 2 ; les décisions N-045 v2 (`c7b05e39…`), N-053 (`2204256d…`), N-058 (`854f2724…`) ; les lignes GO-2026-11-19-60, -61, -63 de `registres/go.md` et R-3831 à R-3843 de `registres/decisions.md`. Sur la branche : l'ordre de passage v3 (`b19f550b…`).
- **Non lus** : aucune carte, aucun verdict de juge, le classement, le coffre. Tous les comptes cités viennent de pièces déjà versées.

## 1. Verdict

Les cartes d'Astra et de Carbon n'ont pas été écartées par un juge : elles l'ont été par la règle de choix (cinq questions déjà posées, coût pesé), écrite avant l'ouverture des cartes et appliquée sans l'espèce.
Aucune mesure ne montre un juge défavorable à Astra ; le seul compte disponible va dans l'autre sens (20 cartes d'Astra sur 20 « notables » chez les deux juges) et il est confondu avec l'absence de citation.
Je recommande donc de changer la règle de sélection (voies par type de carte, coût rapporté, quotas par strate, droit de défense) et de mesurer le collège à cinq lignées comme un bras de la ligne 3, sur devis, avant de lui confier quoi que ce soit.

## 2. Faits établis sur les pièces

Dossier `docs/notes/organisme-auto-conception-v1/course-v2/` sauf mention.

| pièce | sha256 | ce qu'elle établit |
|---|---|---|
| `criteres-choix-cartes-v9-v1.md` | `8881dbb2f63bdfedba34c971e5fb7081fc244ab5c3555307482589b84d837326` | § 0 : ni le verdict des juges ni l'espèce ne sont des critères ; § 2 : le critère C2 ne note que cinq questions du programme (0 si aucun lien) ; le critère C3 note le coût (0 au-delà de 75 dollars ou de plusieurs générations) ; § 3 : plancher C2 ≥ 1 et total ≥ 7 |
| `proposition-cartes-a-eprouver-v9-v1.md` | `a2cd45adf7c49a909ad14be378b75b3233eae198b7f51cc416450f4cd878d856` | cartes lues sans le champ de l'espèce ; 34 cartes sous le plancher, « presque toutes par le coût […] joint à un lien de biais ou nul avec les cinq questions » (§ 2) ; écart 2 : les instruments tombent « par construction de mes cinq questions » (§ 6) |
| `contre-lecture-proposition-cartes-v9-v1.md` | `a923cb57702a055d7c0460c990e5ecff5dd6125c1f0c0460cedba67de606fc43` | critères commis avant la proposition, cartes lues sans l'espèce (§ 7) ; conclusion « À refaire pour le classement et la décision » ; plusieurs notes de C2 sont des jugements discutables (interprète de référence : 9 et non 8 ; écart 2 requalifié en jugement, mineure 3) |
| `especes-et-originalite-cartes-v9-v1.md` | `2af9e67fce5b8edb3a3cc197347ab35f08e5f1731f5dcc3b3ef11c1fc6c44beb` | part des cartes dans les neuf premières lignes retenues : Astra 3 sur 20, Carbon 11 sur 16, Opus 13 sur 22, Argon 8 sur 21, Fable 5 sur 15 ; 13 des 18 cartes « originales » sont d'Astra ; raison donnée : une question neuve vaut zéro à C2 par construction ; aucune exclusion ne les touche. Une seule lecture, sans contre-lecture ; le masque d'espèce « n'a pas tenu », le style d'Astra se reconnaît (limites 2 et 4) |
| `cartes-reexaminees-cout-non-limitant-v9-v1.md` | `de7ed04d06903c507ace3a16130fccf9f22d88e6e16143c3f8f3e0530837d063` | quatre des cinq cartes de Carbon alors non gardées (`f91a7a590c8fe`, `f0a8378953d43`, `f17603c39bc32`, `ff76aee57bba1`) sont la porteuse et trois bras de la ligne 2.1, qui demande de vrais proposeurs sur quatre générations au moins (de l'ordre de 1 300 dollars pour l'étape à deux bras) : c'est le coût qui les tenait dehors ; la cinquième (`f7cc0003c4b2c`) est une variante d'une ligne déjà gardée |
| `lecture-course-v9-v1.md` | `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb` | deux juges seulement, de lignées Opus et Argon ; quatre items sur cinq presque à plafond ; tout « notable » du juge Opus l'est du juge Argon ; coût des juges 9,27 dollars pour 94 cartes |
| `lecture-course-v9-v1-erratum-1.md` et sa sortie `…-verif-probabilites-v1-sortie.txt` | `9a77160097458889d4ec7771c05e50d97632b7772466c6023f2e444e0a72b9d3` ; `3cea377a66ec93e7eb1fc694a652d7c880c0b104e5a87ffe97c4d3d03b135ee4` | « notable » mesure en bonne part l'absence de citation (sans marque de citation : 33 notables sur 39 ; avec : 34 sur 55) ; aucune carte d'Astra ne cite ; cartes d'Astra les plus courtes ; aucun juge n'est de la lignée d'Astra |
| `../epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` (branche) | `b19f550b525fe5696321167bd43a35fa5ece180fd2f97dad5dfc6e970a8c0f67` | rang 3 : votes effectifs des juges croisés, étage sur processeur puis étage payant d'environ 25 dollars (deux juges réels, une centaine de témoins), sans dépendance au branchement |

**La matrice juge × auteur existe déjà, pour deux juges** (sortie `3cea377a…`, comptes de « notable ») :

| | Argon (21) | Astra (20) | Carbon (16) | Fable (15) | Opus (22) |
|---|---|---|---|---|---|
| juge Opus | 12 | 20 | 13 | 11 | 11 |
| juge Argon | 19 | 20 | 16 | 13 | 15 |

Lecture, sans plus : aucun juge ne note Astra plus bas ; le juge Opus est le plus sévère pour sa propre lignée ; le juge Argon passe 19 des 21 cartes de la sienne. Rien de cela ne vaut mesure d'un biais, dans aucun sens : l'item qui trie sanctionne une citation sans « non vérifié », et les lignées citent inégalement.

**Ce qui n'est pas établi.** (1) Un biais d'un juge contre Astra comme modèle : non mesuré, et je ne l'affirme pas. (2) Un biais du rédacteur de la proposition (modèle F) contre le style d'Astra : non mesuré non plus ; il a lu sans l'espèce, mais le style se reconnaît. (3) Que la règle ait eu tort : seule l'épreuve le dira.

**État présent.** Les cartes d'Astra sont toutes gardées (20 sur 20) et les treize cartes restantes d'Astra, d'Opus, de Fable et de Carbon aussi (GO-2026-11-19-61) ; le coût n'élimine plus (GO-2026-11-19-60). La question porte donc sur la règle des courses à venir, et la course v9 sert de terrain de mesure.

## 3. Les voies comparées

Garde commune (N-058, N-053 point 5, exclusion X1 des critères) : un juge ou un collège peut **proposer** ce qui va à l'épreuve ; il ne décide ni de la composition des proposeurs ou des juges, ni de l'adoption d'un mécanisme, et il ne trie rien à l'intérieur de l'organisme. L'adoption se juge sur l'oracle du monde planté et le coût mesuré.

| voie | ce qu'elle change | ce qu'elle risque | garde |
|---|---|---|---|
| **(i) Collège d'un juge par lignée** (cinq), chaque juge récusé pour les cartes de sa lignée, donc quatre voix par carte | plus de regards ; un juge Astra et un juge Carbon existent enfin | une majorité ramène vers le familier ; les erreurs sont corrélées (Opus et Fable sont de la même famille ; en v9 les notables d'un juge sont inclus dans ceux de l'autre) : cinq juges ne font pas cinq voix ; avec la consigne actuelle, le collège voterait surtout sur les citations ; coût des juges multiplié par deux et demi environ | sortie descriptive, ou liste proposée ; jamais un tri automatique (X1) ; l'avis pondéré reste descriptif (GO-2026-11-19-63) |
| **(ii) Davantage de juges Astra** | donne plus de poids à une lignée | corrige un biais non mesuré, dont le seul indice a le signe inverse ; un juge Astra sur des cartes d'Astra est le cas que N-053 veut éviter ; régler la composition des juges pour obtenir un résultat sur une espèce, c'est viser un signe (règle R3) et toucher la composition par une autre voie que l'oracle (N-058) | un seul juge Astra, comme bras mesuré de (i) ; pas de surpoids |
| **(iii) Juges descriptifs, règle de sélection changée** | trois voies d'entrée, chacune avec son plancher : *question du programme* (le critère C2 actuel), *question neuve* (la carte pose une question que le programme n'a pas, avec un oracle exécutable et deux issues qui changent une décision nommée), *instrument* (dit comment mesurer ou adopter) ; le coût est rapporté par étage et n'entre plus dans la note ; quotas par strate (voie × case du catalogue), jamais par espèce ; l'espèce est comptée après coup et un écart fort déclenche le même audit dans les deux sens (règle R4) | plus de lignes, donc plus de préenregistrements et de devis ; le rangement par voie est un jugement de lecteur (à faire par deux lecteurs de lignées différentes, désaccords rapportés) ; « question neuve » peut devenir un fourre-tout si l'oracle n'est pas exigé | la règle est écrite et scellée avant l'ouverture ; elle propose, Lazar choisit |
| **(iv) Droit de défense** (ajout) : un seul lecteur ou juge, hors de sa lignée, peut envoyer une carte sur la liste proposée, en écrivant la prédiction de l'oracle et la décision que l'épreuve changerait ; nombre de défenses borné par lecteur | protège la carte singulière qu'une majorité enterre ; chaque défense devient une prédiction vérifiable après l'épreuve | sans borne, tout passe ; un défenseur peut reconnaître le style de sa lignée | la défense propose ; son taux de réussite est rapporté, il ne sert pas à choisir les juges (N-058) |
| **(v) Lot tiré au sort** (ajout) : une part des cartes non proposées va à l'épreuve par tirage stratifié, graine consignée | aucun modèle n'y décide ; donne la base contre laquelle toute règle de sélection se compare | des épreuves dépensées sur des cartes faibles | bras témoin, coût rapporté |

Les voies (iii), (iv) et (v) se combinent ; (i) peut les servir comme instrument de mesure ; (ii) ne se défend que si une mesure montre le biais qu'elle veut corriger, et même alors le remède propre serait la récusation ou l'étalonnage, non le surpoids.

## 4. La mesure qui départage, gratuit d'abord

Chaque mesure se préenregistre et se scelle avant lecture (règle R1), contre-lecture par un modèle O ; les seuils se fixent au préenregistrement, pas ici.

1. **Matrice juge × auteur, démêlée de la citation — gratuit.** Un programme relit les champs des verdicts déjà scellés (aucune lecture de carte ni de note par un agent, comme pour l'erratum) : matrice par item, puis à l'intérieur des cartes avec et sans marque de citation. Question : chaque juge note-t-il mieux sa lignée, une fois la citation tenue fixe ? Lit : le programme ; un rédacteur neuf écrit le plan, un modèle O le contre-lit. Limite : deux juges, items à plafond, 94 cartes ; cela ne peut pas répondre pour un juge Astra ou Carbon, qui n'existe pas.
2. **Rejeu de la règle — gratuit.** Deux lecteurs neufs, de lignées différentes, rangent les 94 cartes sans espèce sous la règle (iii) scellée d'avance ; un programme compare, par voie puis par espèce (lue en dernier), ce que la règle v1 et la règle (iii) envoient à l'épreuve, et l'accord des deux lecteurs. Cela décrit les règles ; cela ne dit pas laquelle a raison.
3. **Validation après coup contre l'oracle — gratuit, différé.** Presque toutes les cartes de la v9 seront éprouvées (les quatre cartes d'Argon non gardées et les exclusions mises à part ; compte exact à établir par programme). Avant de lire la première issue, on scelle ce que chaque règle candidate (v1, (iii), (iv), tirage (v), vote du collège s'il existe) aurait proposé, puis on compte, par règle, les épreuves qui ont changé une décision de conception et leur coût. Limites : une vingtaine de lignes, une seule course, des lignes et non des cartes ; puissance faible, à dire d'avance.
4. **Votes effectifs du collège sur témoins plantés — payant, sur devis et ligne de GO neuve.** C'est la ligne 3 de l'ordre de passage ; le collège à cinq lignées en devient un bras. Témoins à faute connue, plantée par programme dans des cartes de chaque lignée. On mesure par juge les faux acceptés et les vrais rejetés, la corrélation des erreurs et le nombre de votes effectifs ; l'interaction juge × lignée d'origine à faute égale (c'est la seule mesure qui puisse dire « ce juge défavorise Astra ») ; et trois règles de vote : majorité, unanimité, défense par un seul. Ordre de grandeur, à chiffrer au devis : l'étage à deux juges est annoncé à environ 25 dollars ; à cinq juges, de l'ordre de 60 dollars.
5. **Faire juger les 94 cartes par les trois lignées manquantes — payant, non recommandé en l'état.** De l'ordre de 10 à 30 dollars (9,27 dollars réels pour deux juges, majorés de moitié), mais la consigne de la v9 mesurerait encore la citation. À ne proposer qu'après la mesure 4 et avec une consigne refaite.

**Lecture qui départage.** La voie (iii) se juge sur les mesures 2 et 3. Le collège (i) ne gagne une place de proposeur de liste que si la mesure 4 lui trouve plus de votes effectifs que deux juges et si la défense par un seul récupère des témoins vrais sans laisser passer plus de témoins faux. La voie (ii) ne s'ouvre que si la mesure 4 montre une interaction défavorable à Astra dont l'intervalle exclut zéro.

## 5. Ce que la note ne dit pas

- Que les cartes d'Astra ou de Carbon valent mieux ou moins bien que les autres : rien n'est éprouvé.
- Qu'un juge, ou le rédacteur de la proposition, est biaisé ou ne l'est pas : aucune mesure n'existe ; la matrice du § 2 est confondue.
- Que la règle v1 avait tort : elle a fait ce qu'elle disait, et ses écarts étaient écrits.
- Qu'un collège à cinq est meilleur que deux juges : c'est l'objet de la mesure 4.
- Aucun seuil, aucun devis, aucune modification d'une hypothèse ou d'une revendication. Les ordres de grandeur de coût ne sont pas des devis.
- La règle (iii) n'est qu'esquissée : son texte exact est à écrire et à sceller par qui concevra la prochaine sélection.

## 6. Décision pour Lazar

**Décision.** Comment faire entrer à l'épreuve les cartes du type de celles d'Astra et de Carbon : par la règle de sélection, par un collège de juges qui vote, ou par davantage de juges Astra ?

**Enjeu.** Ces cartes sont tombées sur deux critères de la règle (questions déjà posées, coût), pas sur un juge. Changer les juges ne corrige pas cette cause ; et un collège qui vote ce qui va à l'épreuve touche N-058 et l'exclusion « un modèle décide » s'il fait plus que proposer.

**Options.**
- **(a) Règle changée, juges descriptifs, collège mesuré d'abord.** Voies par type de carte, coût rapporté, quotas par strate, droit de défense et lot tiré au sort ; mesures 1 à 3 tout de suite, sans dépense ; le collège à cinq lignées entre comme bras de la ligne 3, sur devis. Avantage : traite la cause établie, respecte N-058, et la course v9 dira après coup quelle règle avait raison. Inconvénient : plus de lignes à préenregistrer ; le collège attend sa mesure.
- **(b) Collège de cinq juges qui vote dès la prochaine course**, avec récusation par lignée et défense par un seul ; sa liste reste une proposition. Avantage : réponse directe à ta deuxième idée, un juge Astra et un juge Carbon existent. Inconvénient : rien ne dit qu'il vote autre chose que la citation ; coût des juges plus que doublé ; votes effectifs inconnus.
- **(c) Davantage de juges Astra.** Avantage : simple. Inconvénient : corrige un biais qu'aucune mesure ne montre, dont le seul indice a le signe inverse ; revient à régler la composition pour un résultat.

**Recommandation.** (a), confiance 0,7. Si la mesure 4 trouve un juge défavorable à Astra, je reviens vers toi avec la récusation ou l'étalonnage, pas avec le surpoids.

**Défaut sous 48 heures.** La part sans dépense de (a) : mesures 1 et 2 préparées et contre-lues, règle (iii) écrite en brouillon. Rien de payant, et aucun changement de la règle en vigueur, sans ton mot.
