# Vérification des corrections — fiche des quatre décisions sur l'orchestrateur v68, version 2 — v1

- Auteur : le même contre-lecteur, modèle O (règle de l'allègement), qui a écrit la contre-lecture de la v1 (`contre-lecture-fiche-quatre-decisions-orchestrateur-v68-v1.md`, `af90dae48d9e35770f00d1ee66becd26986caea13d76ea2f930cb5d83ec8e247`, versée à l'octet). Je n'ai écrit ni la fiche v2, ni son rapport, ni son mandat. 2026-11-19, vers 23:43Z à 23:55Z (`date -u` : 23:47:08Z).
- Lecture seule. `git fetch origin lot/compte-organisme-v1 main` ; branche à `a0a3e68d3` (arbre propre) ; `main` à `ef8008682`. Aucun lancement de l'orchestrateur, aucun appel à un fournisseur, aucune dépense, aucune écriture dans le dépôt, aucun interpréteur appelé avec du code en ligne, aucune commande sur le dossier d'archives interdit. Aucun refus d'outil.

## Verdict

**Prête après corrections** (dix corrections à texte exact, § 5). Les dix-neuf corrections et les trois au rapport sont appliquées, et les trois écarts déclarés sont acceptables. La recommandation (b) à 0,6 de la décision 4 tient, mais sa troisième raison est fausse. Le premier constat neuf du rédacteur est une vraie divergence entre deux mots de Lazar, et la fiche doit la lui porter comme question, au verdict et dans la phrase de la décision 2. Les constats 2 et 3 (R-3209, point 3 ; GO-94 à -96) doivent entrer dans la fiche, en une phrase chacun.

## 1. Pièces vérifiées

| pièce | empreinte | état |
|---|---|---|
| fiche v2 | `2b8e3815ed35cb68514c00a323a3451ec2eae6c65b5193b377369da7b7faa099` | conforme au compagnon ; lue en entier |
| différentiel v1 → v2 | `412d004e914dd20f37906a7e104087aecacafe6ba274b73041df89f2d7ee2597` | conforme. Le corps est égal à l'octet à un `diff -u` refait par moi entre la v1 et la v2 du dépôt (seuls les chemins et les heures de l'en-tête diffèrent). Trente blocs, tous rapportés à une correction ou à un changement déclaré |
| remplacements (40) ; journal de l'outil | `aab710ce…` ; `4d22e4e6…` | conformes ; la cible du journal est la v1 `52741f65…` |
| rapport du rédacteur v2 | `29ccc99d49b2c403480db73a79ed901c28984a59505e0070b3677e472d440cfd` | conforme ; lu en entier |
| mandat v2 | `c8acd3323857e462d3bfc83bc50b94c3a4fd0a5cffd74b2d8236e85accdd7c06` | conforme ; lu en entier |
| `main` : `registres/go.md` | `7ec26e96…` à `7d0b0ba9` (la version du rédacteur) ; `3fa872ce…` à `ef8008682` | GO-85, -89, -93 à -96 lus en entier ; GO-96 a été ajouté après la lecture du rédacteur (commit `e692664bb`, 23:34Z) |
| `main` : `registres/decisions.md` | à `ef8008682` | R-3209 et R-3965 lus |
| `main` : état des faits des trois règles v2 | `a4c99910f716073a1b8b868f90e34a7c2e785489cfdc99aa4cd3a0e6bcfebca7` | § 0, § 5, § 7 (règle 2) lus |
| `main` : préenregistrement de la ligne 1 v5 | `523adfd7…` | titre : « étage sur processeur seul » ; juste |
| verdict de la course v67 | `d7902432…` | § 4.3 relu |

## 2. Les corrections, une à une

| n° | appliquée | remarque |
|---|---|---|
| 1 à 11 | à la lettre | — |
| 12 | (a) et (b) à la lettre ; recommandation revue en (b) | écart déclaré et légitime : mon texte de repli ne valait que si (a) restait |
| 13 à 17 | à la lettre | — |
| 18 | à la lettre, placée dans l'enjeu | écart déclaré : la phrase sur les relais est bien dans l'enjeu, et c'est ma correction qui la situait mal |
| 19 | « n'était pas dans les pièces du mandat de la v1 » | écart déclaré, exact (le mandat v2 nomme la pièce) |
| R1 à R3 | portées au rapport v2, le rapport v1 restant intact | conforme à R12 |

**Une incohérence reste**, héritée de la v1 et que ma correction 6 aurait dû viser. À l'inconvénient de l'option (a) de la décision 2, la fiche écrit « les lignes à lecture (6, 7, 8, 9, 12, 20) », alors que le tableau corrigé de la décision 1 dit que la lecture de la v68 ne débloque pas le rang 6 (correction V4).

## 3. Le texte de la main du rédacteur

- **En-tête** : juste. Il serait plus exact d'écrire GO-55 à -95, puisque le rédacteur dit avoir lu GO-94 et -95.
- **Verdict, point 2 (4) et point 4** : justes. GO-89 et GO-81/-77 tranchent bien deux parts. GO-81 et GO-85 portent sur la ligne 1, dont le texte scellé est « étage sur processeur seul ».
- **Verdict, point 3, inchangé** : il ne dit plus qu'un côté. Après le paragraphe sur GO-89, il présente comme acquis que la lecture de l'héritage « n'autorise pas » ce que la v68 sert, alors qu'un mot plus récent de Lazar va dans l'autre sens (correction V1).
- **Décision 2, paragraphe sur GO-89** : les faits sont justes. GO-89 dit à la lettre « Rien du juge dans les courses qui comptent : vue sans verdict, comme le code depuis la v59 ». L'état des faits (§ 5 et § 7, règle 2) décrit cette vue : le proposeur suivant reçoit « les seules lois de l'archive (identifiant, loi) », et « ce qui passe toujours : un bit par loi (retenue ou non) ». La v67 l'a servie : « vue servie en génération 2 = […] {K1} ∪ les 11 retenues » (§ 4.3). Seule la phrase de conclusion, « aucun des deux ne le tranche », est trop faible (§ 4 ; correction V3).
- **Décision 2, confiance de (a) à 0,5** : cohérente avec ces faits.
- **Décision 4** : la phrase de décision est neutre et juste ; la recommandation est examinée au § 4. Le défaut, « c'est (b) de fait », fait de l'absence de réponse sur une dépense l'option recommandée. Rien n'est dépensé, puisque le devis reviendra à Lazar, mais la formule pousse (correction V10). Le titre de (b), « palier 1 de l'héritage », n'est pas harmonisé avec la recommandation, « premier étage payant à tests de mort » (correction V9).
- **Réserve 5** : juste à la date d'écriture. Elle est à mettre à jour après cette vérification (correction V11, facultative).

## 4. Questions posées

**La recommandation (b), confiance 0,6, de la décision 4 tient-elle ? Oui.** Ses deux premières raisons sont fondées. D'abord, la v67 a joué le vrai bac sur une machine louée, avec des scripts écrits par un modèle (§ 4.4). Ensuite, les lignes GO-10-11 et GO-12-06 louaient la machine sous la ligne de la course, avec l'essai à blanc `--bac reel` avant tout appel payant. Le contre-argument (le rapport du développeur place l'essai « avant tout GO d'étage ») est dit loyalement, et les conditions de retour à (a) aussi. **La troisième raison est fausse.** « Un essai loué aujourd'hui porterait sur la v68 » : l'essai du bac porte sur l'étage et la machine, et aucun des huit fichiers du paquet v68 ne touche l'étage (le paquet ne contient que configuration, budget de course, course 2, simulation, lanceur, essai à blanc, aides et essais). Remplacée par la correction V8, qui va dans le même sens. 0,6 est une confiance raisonnable.

**Constat neuf 1 : GO-89 et GO-76, une vraie divergence à porter à Lazar ? Oui, comme question, sans la trancher.**
- Ce qui diverge, à la lettre et sur le même cas : une vue qui ne sert que les survivantes, sans verdict. GO-89 prend pour règle des courses qui comptent « la vue sans verdict, comme le code depuis la v59 », c'est-à-dire les seules lois retenues : un tri par survie, que la course réelle v67 a servi. La lecture de la garde acceptée par GO-76, point 2 (devis v5, § 9, recommandation accordée par « go recos »), range « la sélection des survivants » du côté interdit.
- Ce qui peut les réconcilier, et que seul Lazar peut dire. Les portées diffèrent : GO-89 vise ce que les proposeurs voient **du juge**, alors que le bit « retenue » vient de l'étage, non d'une note de juge ; GO-76 vise le registre de l'héritage, et cette lecture est la justification d'un accord « à revoir au point 7 du palier 0b ». Aucune des deux ne nomme la lecture de la v68.
- Un fait aggrave : la vue du code depuis la v59 était déjà en service le 12 novembre (v67), avant GO-76. La lecture acceptée pour l'héritage contredisait donc déjà la pratique de l'organisme.
- Pourquoi la porter : c'est une « divergence non résolue » au sens de `CLAUDE.md`, sur le cœur de la décision 2 et du point 14 de l'ordre v3. Si GO-89 vaut, l'option (c) est conforme à la règle, et même un service dans les courses qui comptent le serait. Si la lecture de GO-76 vaut, (c) reste un écart. La fiche la dit aujourd'hui en lecture du rédacteur, au milieu de l'enjeu, avec un verdict qui ne montre que l'autre côté : il faut la monter au verdict et dans la phrase de décision (corrections V1 à V3, V5).

**Constat neuf 2 : R-3209, point 3, est à porter.** C'est un mot de Lazar (« Le mot « survit » des tests de mort du bac à sable : oui, remplacé par un verdict précis […] ; à porter dans la conception de la course à plusieurs générations »). L'état des faits le relève encore contre le brouillon 6. La v68 et sa règle de sélection (« ne retient que « survit » ») l'emploient. La v68 ne le sert pas aux proposeurs (garde A4, aucune consigne ne contient « survit »), mais la version suivante et l'additif devront dire quelles classes sont retenues : c'est un élément de « ce qui manque ». Une phrase suffit (correction V6).

**Constat neuf 3 : GO-94, -95 et -96 sont à porter.** GO-94 met en conception une course de trois générations : « héritage récompensé, composition apprise, coût dans le signal ; code et budget figés après la conception » ; aucune dépense avant devis et accord. GO-95 la confie à ce compte. GO-96 (23:34Z, hors de la lecture du rédacteur) précise qu'elle sert le bras d'attaque et vise des attaques inédites. Une course à trois générations à héritage récompensé devra dire ce qui passe d'une génération à l'autre et par quel véhicule. Elle dépend donc des décisions 1 et 2 : sous (a), la v68 ne sert rien. Elle ne relève pas de la décision 3, qui ne vise que la course d'auto-conception, mais « la prochaine course » y devient ambigu. Lazar doit le voir avant de répondre (correction V7).

**Pousse-t-elle sans le dire ?** Non vers une dépense ni une revendication. La seule poussée est le défaut de la décision 4 (V10).

## 5. Corrections demandées (texte exact ; « remplacer A par B » : A est copié de la v2)

V1. **Verdict, point 3.** Remplacer « 3. Un point que tu dois connaître avant de trancher la décision 2 : la lecture de la garde que tu as acceptée pour l'héritage **n'autorise pas** ce que la v68 sait servir. Elle dit que la garde interdit « les verdicts de juge et la sélection des survivants » ; or le régime de lecture de la v68 sert justement les fiches qui ont survécu. » par « 3. Un point que tu dois connaître avant de trancher la décision 2 : **deux de tes mots divergent** sur le cas exact que la v68 sait servir, les seules fiches qui ont survécu, sans verdict. La lecture de la garde que tu as acceptée pour l'héritage (`GO-2026-11-19-76`, point 2 ; devis v5, § 9) range « la sélection des survivants » du côté interdit. La règle `GO-2026-11-19-89` prend pour modèle « la vue sans verdict, comme le code depuis la v59 », qui sert les seules lois retenues et que la course réelle v67 a servie. Aucune pièce ne dit lequel vaut pour la lecture de la v68 : c'est à toi de le dire (décision 2). »

V2. **Décision 2, phrase.** Remplacer « **Décision.** La génération suivante peut-elle lire quelque chose de l'étage des tests de mort, et cette décision suit-elle celle que tu as prise pour l'héritage ? » par « **Décision.** La génération suivante peut-elle lire quelque chose de l'étage des tests de mort, et, puisque ta lecture de la garde pour l'héritage et ta règle `GO-2026-11-19-89` divergent sur le service des seules survivantes, laquelle vaut pour la lecture de la v68 ? »

V3. **Décision 2, paragraphe sur GO-89, dernière phrase.** Remplacer « Lecture du rédacteur, non contre-lue : tes deux mots ne disent pas la même chose de ce cas, aucun des deux ne le tranche, et l'allumage de la lecture reste ton nœud (`GO-2026-11-19-67`). » par « Tes deux mots ne disent pas la même chose de ce cas (vérifié en contre-lecture sur les deux lignes, l'état des faits et le verdict de la v67). Leurs portées diffèrent : `GO-2026-11-19-89` vaut pour les courses qui comptent et vise ce qui vient du juge ; la lecture de `GO-2026-11-19-76` vaut pour le registre de l'héritage et est « à revoir ». Aucune ne nomme la lecture de la v68. La vue du code depuis la v59 était déjà celle de la course v67, le 12 novembre, avant `GO-2026-11-19-76`. L'allumage de la lecture reste ton nœud (`GO-2026-11-19-67`). »

V4. **Décision 2, option (a), inconvénient.** Remplacer « les lignes à lecture (6, 7, 8, 9, 12, 20) » par « les lignes à lecture (7, 8, 9, 12, 20) ».

V5. **Décision 2, option (c), avantage.** Remplacer « Avantage : les rangs 7 et 8 peuvent écrire leur préenregistrement et leur devis. » par « Avantage : les rangs 7 et 8 peuvent écrire leur préenregistrement et leur devis ; c'est la vue que `GO-2026-11-19-89` prend pour règle, ici sur monde planté seulement. »

V6. **« Ce qui manque encore ».** Après « Les trois premiers sont du travail sur processeur, sans dépense. », ajouter : « Ta décision R-3209, point 3 (18 novembre), demande de remplacer le mot « survit » des tests de mort par un verdict précis (« identique », « portable », « dépendant de la donnée », « confiné ») dans la conception de la course à plusieurs générations. La v68 l'emploie encore, et sa sélection ne retient que « survit » : la version suivante et l'additif devront dire quelles classes sont retenues (`registres/decisions.md` sur `main`, R-3209). »

V7. **Verdict, point 4.** Après « Tes mots sur la ligne 1 (`GO-2026-11-19-81`, `GO-2026-11-19-85`) portent sur son étage sur processeur, que la v68 ne bloque pas. », ajouter : « Une course de trois générations sur de nouvelles attaques est en conception, portée par ce compte (`GO-2026-11-19-94`, `-95`, `-96`, sur `main`) : héritage récompensé, code et budget figés après la conception, aucune dépense avant un devis et un accord à part. Sa conception devra dire ce qui passe d'une génération à l'autre et par quel véhicule : elle dépend des décisions 1 et 2 (sous l'option (a) de la décision 2, la v68 ne sert rien). Elle fixera ses propres champs de fiche ; la décision 3 ne vise que la course d'auto-conception. »

V8. **Décision 4, recommandation, troisième raison.** Remplacer « Et un essai loué aujourd'hui porterait sur la v68, qui ne jouera jamais en réel : la version suivante de l'orchestrateur devra rejouer cet essai avant son premier appel payant, ce qui est la première étape de (b). » par « Et l'essai du bac porte sur l'étage et la machine, que la v68 ne change pas (aucun des huit fichiers de son paquet ne touche l'étage) ; la course v67 l'a déjà fait sur une machine louée : un essai sous un devis à part n'apprendrait presque rien de plus que la première étape de (b). »

V9. **Décision 4, titre de l'option (b).** Remplacer « **(b) La machine dans le devis du palier 1 de l'héritage**, » par « **(b) La machine dans le devis du premier étage payant à tests de mort** (le palier 1 de l'héritage si c'est lui), ».

V10. **Décision 4, défaut.** Remplacer « Sans ton mot, aucun essai à part n'est loué ; la machine reviendrait alors dans le devis du premier étage payant, qui te sera soumis : c'est (b) de fait. » par « Sans ton mot, rien n'est loué ; la question reviendra avec le devis du premier étage payant à tests de mort. »

V11 (facultative). **Réserve 5.** Remplacer « La v1 a été contre-lue (`af90dae4…`) ; ne l'ont pas été : la recommandation revue de la décision 4, la confiance revue de la décision 2, le point 4 du verdict et le paragraphe de la décision 2 sur `GO-2026-11-19-89`. » par « La v1 a été contre-lue (`af90dae4…`). La recommandation revue de la décision 4, la confiance revue de la décision 2, le point 4 du verdict et le paragraphe de la décision 2 sur `GO-2026-11-19-89` ont été vérifiés par le même contre-lecteur (`verification-fiche-quatre-decisions-orchestrateur-v68-v2-v1.md`). »

Chacun des passages A ci-dessus est présent une seule fois dans la v2 (recherche exacte faite).

## 6. Ce que je n'ai pas pu établir

1. Le code de l'orchestrateur reste absent. Je ne peux dire ni que la vue de la v59 et la lecture de la v68 sont de même nature au code, ni quelle version de l'étage a tourné en v67.
2. L'intention de Lazar derrière « comme le code depuis la v59 » : je lis la lettre de la ligne, de l'état des faits et du verdict de la v67.
3. Le contenu de la question scellée et de l'ordre de course de GO-94 : non écrits, ou non lus par moi.
