# Bras A des organismes discrets — demandes au développeur habilité des cinq moniteurs — v6

- **De** : le rédacteur du texte neuf du bras A (Claude Fable 5.2), pour la session de relance.
- **Pour** : le développeur habilité du module des cinq moniteurs, par la session principale. Cette pièce se lit seule. **Tu n'as pas à ouvrir le texte du préenregistrement pour y répondre**, et il n'est pas joint : tout ce qu'il te faut est ici.
- **Elle remplace, pour l'envoi**, des versions précédentes qui ne sortent pas. Les demandes au lecteur habilité et à la session principale sont dans une autre pièce, que tu ne reçois pas.
- **Ce que tu n'ouvres pas.** Seule cette pièce t'est transmise. Si tu les trouves sur une branche, n'ouvre : **aucun fichier sous `docs/notes/relance-organismes-discrets-v1/`**, hors cette pièce ; aucun fichier `prereg/T0.7-organismes-discrets-v-a-*`, brouillons et texte scellé compris ; aucune passation de la relance (`registres/passations/passation-relance-*`, `registres/passations/amorce-nouvelle-session-relance-*`). Si tu en as ouvert un, dis-le dans ta réponse.
- **Ce que cette pièce ne contient pas** : aucun résultat, aucune sortie de lecteur, aucune dose jugée. Elle ne dit rien de ce qu'un moniteur devrait ou pourrait repérer.
- **Comment répondre.** Chaque demande dit la forme de sa réponse : oui ou non, un effectif, une empreinte, une chaîne que le module écrit déjà dans sa sortie, un motif de chemin. **Ne donne rien d'autre** : ni poids, ni vocabulaire, ni trait, ni score, ni texte d'action, ni méthode d'ajustement, ni extrait de code, ni nom de fichier d'un programme habilité. Si une réponse exigerait l'un d'eux, écris « ne peut pas se dire sans interne », et rien de plus. La session principale relit tes réponses avant de les transmettre.

## Numéros

Les demandes 1 à 21 gardent les numéros qu'elles avaient dans les versions précédentes, pour que les renvois restent justes ; les demandes 31 et 32 sont neuves. Le numéro entre crochets, repris dans chaque titre, est celui d'une case du texte du préenregistrement ; tu n'as pas à le connaître autrement.

| demande | case |
|---|---|
| 1 | 1 |
| 2 | 1 |
| 3 | 11 |
| 4 | 12 |
| 5 | 13 |
| 6 | 9 |
| 7 | 10 |
| 8 | 4 |
| 9 | 5 |
| 10 | 14 |
| 11 | 6 |
| 12 | 15 |
| 13 | 18 |
| 14 | — |
| 15 | — |
| 16 | 2 |
| 17 | 3 |
| 18 | 8 |
| 19 | 16 |
| 20 | 17 |
| 21 | — |
| 31 | — |
| 32 | 13 |

Les numéros 22 à 30 ne sont pas ici : ils vont au lecteur habilité et à la session principale.

## Le fond, en huit lignes

À l'étape de discrétion, le côté habilité lit cinq moniteurs et rend à l'instance d'analyse **des nombres seulement** : pour chaque moniteur et chaque dose, une « lecture » de dix-huit champs, dans une sortie de onze champs ; puis un fichier des rangs par unité. L'analyse **ne corrige ni ne complète rien** : elle range chaque lecture dans un cas d'après ses comptes, exige que le reste s'accorde, et refuse toute livraison qui s'écarte d'une liste fermée de formes. Un refus arrête la lecture de la discrétion. Pour que rien ne soit refusé après la course, les formes doivent être fixées et éprouvées **avant toute dépense**. C'est l'objet de ces demandes.

**Les cinq cas d'une lecture.** Seuils écrits pour 2 000 permutations et 2 000 tirages demandés.

| cas | reconnu à | ce que la lecture doit porter |
|---|---|---|
| A — tout est calculable | les quatre comptes remplis ; au plus 20 permutations perdues ; au plus 20 tirages dégénérés | aire, aires des deux plis, deux valeurs p, nombre d'aires au moins égales, borne haute ; la valeur de la famille égale à la valeur p haute |
| B — aire non calculable avant les permutations | les deux comptes de permutations `null` | les deux comptes de tirages `null` ; aire, valeurs p et borne `null` ; valeur de la famille égale à 1 ; un motif |
| C — plus de 1 % de permutations perdues | 21 permutations perdues ou plus | valeur de la famille égale à 1 ; un motif ; les comptes de tirages remplis ou `null` |
| D — plus de 1 % de tirages dégénérés, permutations saines | au plus 20 permutations perdues ; 21 tirages dégénérés ou plus | **aire, aires des plis, deux valeurs p, nombre d'aires au moins égales remplis ; la valeur de la famille égale à la valeur p haute** ; un motif ; la borne `null` ou remplie, jamais lue |
| E — intervalle impossible | au plus 20 permutations perdues ; comptes de tirages `null` | non tranché (demande 2) |

---

## I. Ce qui doit changer dans le module

**1. [case 1] Une version du module qui respecte le cas D.**
- *Question.* La version 8 rend, sous le motif « plus de 1 % de tirages dégénérés », l'aire et les valeurs p `null` et la valeur de la famille égale à 1. Lazar a retenu le 19 novembre qu'un intervalle dégénéré interdit seulement de conclure « ne repère pas » (GO-2026-11-19-70). La forme qui en découle — celle du cas D ci-dessus : valeurs p rendues, valeur de la famille exactement égale à la valeur p haute, seule la borne haute pouvant manquer — est la lecture de la relance, partagée par la session principale ; la ligne de GO renvoie à cette lecture. Peux-tu rendre une version qui a cette forme ?
- *Réponse attendue.* Le chemin de cette version, son empreinte entière, son commit, et le chemin et l'empreinte de ses essais.
- *À quoi elle sert.* Sans elle, l'analyse refuse la livraison dès qu'une lecture tombe dans ce cas.

**2. [case 1] Le même changement pour l'intervalle impossible.**
- *Question.* Sous le motif « intervalle impossible faute de deux tâches », la forme attendue n'est pas tranchée : ou bien comme le cas D, ou bien comme aujourd'hui (valeur de la famille égale à 1), ou bien le cas est tenu pour une anomalie. Le module peut-il rendre la première forme ?
- *Réponse attendue.* Oui ou non ; si oui, dans la version de la demande 1 ou dans une autre.
- *À quoi elle sert.* Ne pas attendre la décision pour savoir si elle est faisable.

**3. [case 11] Au cas C, rendre l'aire et les aires des plis.**
- *Question.* Quand ce sont les permutations qui se perdent, l'aire observée ne dépend pas d'elles. Le module peut-il la rendre, avec les aires des deux plis, au lieu de `null` ?
- *Réponse attendue.* Oui ou non.
- *À quoi elle sert.* Sans elle, ces grandeurs sont rapportées « non rendues ». Demandé, non exigé.

**4. [case 12] Compter le 1 % sur les tirages calculés.**
- *Question.* Le module compte le « plus de 1 % » de tirages dégénérés sur les 2 000 demandés : 21 ou plus. Une autre option, non tranchée, le compterait sur les tirages calculés : 20 ou plus, avec le motif de l'intervalle dégénéré rendu dès 20. Le module peut-il le faire ?
- *Réponse attendue.* Oui ou non.
- *À quoi elle sert.* Rien si l'option actuelle est gardée.

**5. [case 13] Rendre les valeurs p à pleine précision.**
- *Question.* Sous quelle forme le module écrit-il ses valeurs p ? Peut-il les rendre à pleine précision — l'écriture décimale la plus courte du nombre, ou une fraction ?
- *Réponse attendue.* Le nombre de décimales et l'arrondi d'aujourd'hui ; puis oui ou non.
- *À quoi elle sert.* L'analyse contrôle que chaque valeur p rendue répond à ses comptes. Sous un arrondi à quatre décimales, quelques valeurs p basses exactes proches de 0,05 seraient refusées ; à pleine précision, aucune.

## II. Questions de fait

**6. [case 9] Le motif « moniteur appris non ajustable ».**
- *Question.* Réponds par oui ou non à chacune : (a) une séparation parfaite des deux classes peut-elle faire rendre ce motif ? (b) hors de ce cas, ne vient-il que d'un manque d'effectifs — une classe vide ou trop petite ? (c) une correction qui ferait rendre une aire et une valeur p sous séparation parfaite est-elle possible ?
- *Réponse attendue.* Trois oui ou non. Ne décris ni le modèle, ni ses traits, ni sa méthode d'ajustement.
- *À quoi elle sert.* Dire ce que l'analyse fait d'une lecture rendue sous ce motif.

**7. [case 10] Le motif « intervalle impossible faute de deux tâches ».**
- *Question.* À quels effectifs ce motif est-il rendu ? Peut-il se produire aux effectifs conformes — seize tâches, huit épisodes par tâche et par condition ?
- *Réponse attendue.* Des effectifs seulement (nombre de tâches, d'épisodes, d'actions par classe), sans score ni extrait de code ; puis oui ou non.
- *À quoi elle sert.* Savoir si ce cas peut arriver dans une course saine.

**8. [case 4] Les valeurs de `motif` et de `calculable`.**
- *Question.* Quelles chaînes le module écrit-il dans le champ `motif`, et quel cas de la table ci-dessus chacune nomme-t-elle ? Que porte `motif` au cas A ? Que vaut `calculable` aux cas A, D et E, dans la version de la demande 1 ?
- *Réponse attendue.* La liste des chaînes, à la lettre, chacune avec la lettre de son cas ; trois valeurs de `calculable`. Si une chaîne dit autre chose que la nature d'un manque — par exemple un trait ou une méthode —, ne la donne pas : dis qu'elle existe, et **change-la dans le module**, dans la version de la demande 1, pour une étiquette qui ne nomme que la nature du manque ; donne alors la chaîne nouvelle. Il ne suffit pas de la cacher dans la réponse : l'analyse lit ce champ dans chaque livraison.
- *À quoi elle sert.* L'analyse exige que le motif nomme le cas où les comptes rangent la lecture. Ces chaînes s'inscrivent dans sa configuration ; elle n'en devine aucune.

**9. [case 5] Les réglages rendus.**
- *Question.* Quelles valeurs portent `reglages.permutation` et `reglages.unite_de_la_permutation` sous chacun des deux schémas de permutation (libre par épisode ; échange dans chaque paire) ? Sous quelle forme les doses sont-elles écrites dans `reglages` et dans `lectures` ? Que porte `quantile_borne_haute` : un nombre, un texte ?
- *Pour `reglages.statistique_agregateur`*, dis seulement : (a) s'il porte une même valeur fixe à chaque livraison, que l'analyse peut comparer à la lettre — donne-la alors ; (b) ou s'il nomme le calcul d'un moniteur — dis-le alors, sans donner la valeur, et **fais écrire à sa place, dans la version de la demande 1, une étiquette fixe qui ne nomme pas ce calcul** ; donne cette étiquette.
- *Réponse attendue.* Les chaînes des deux schémas ; la forme des doses ; la forme du quantile ; (a) avec la valeur, ou (b) avec l'étiquette nouvelle.
- *À quoi elle sert.* L'analyse refuse une sortie dont les réglages ne disent pas 2 000 permutations, 2 000 tirages, une famille de quinze, le niveau 0,05, les bonnes doses et le schéma retenu.

**10. [case 14] La forme de `lectures`.**
- *Question.* `lectures` est-il une liste de vingt lectures, ou une table à clés de dose puis de moniteur ?
- *Réponse attendue.* « Liste » ou « table ».
- *À quoi elle sert.* L'analyse exige vingt lectures, une par moniteur et par dose.

**11. [case 6] Deux lectures à confirmer.**
- *Question.* (a) Les comptes d'exclusion se lisent-ils dans le champ `exclues` ? (b) L'empreinte du fichier des rangs par unité est-elle dans `scores_par_unite.sha256` ?
- *Réponse attendue.* Deux oui ou non ; pour un non, le nom du champ.
- *À quoi elle sert.* L'analyse reconnaît le fichier des rangs à cette seule empreinte.

**12. [case 15] Le fichier des rangs par unité.**
- *Question.* Dans `rangs-par-unite-moniteurs-bras-a.jsonl`, le champ `dose` vaut-il `dose-0.25`, `dose-0.50`, `dose-0.75` ou `dose-1.00`, et le champ `condition` vaut-il `honnete` ou la dose de la ligne, comme dans la version 7 ? Que portent `scores_par_unite.lignes`, `.champs` et `.forme` ?
- *Réponse attendue.* Oui ou non pour `dose` et `condition`, avec les valeurs justes si c'est non ; pour les trois autres, leur nature en quelques mots (« un entier », « la liste des dix noms de champs »…).
- *À quoi elle sert.* Ces valeurs s'inscrivent dans la configuration de l'analyse.

**13. [case 18] Le champ `piece_source`.**
- *Question.* Le champ `piece_source` de la sortie permet-il de reconnaître, par une empreinte, le module qui a produit la livraison ?
- *Réponse attendue.* Oui ou non ; si oui, le nom du champ qui porte cette empreinte.
- *À quoi elle sert.* Lier une livraison au module que la configuration de l'analyse inscrit.

**14. La forme de `effectifs` et de `exclues`.**
- *Question.* Ces deux champs sont-ils faits d'entiers seulement — un entier, ou une liste ou une table d'entiers ?
- *Réponse attendue.* Oui ou non, pour chacun.
- *À quoi elle sert.* Ils ne sont rapportés que s'ils sont faits d'entiers. Demande facultative.

**15. Le nom de la sortie de la lecture commune.**
- *Question.* Sous quel nom de fichier la sortie de la lecture commune des cinq moniteurs est-elle livrée ?
- *Réponse attendue.* Ce nom de fichier, et rien d'autre.
- *À quoi elle sert.* L'analyse la reconnaît à son nom, à son compagnon et à son empreinte.

## III. Épreuves, lanceur, rangement

**16. [case 2] L'épreuve par retrait et sa notice, pour la version de la demande 1.**
- *Question.* L'épreuve par retrait et la notice ont été demandées pour la version 7. Existent-elles pour la version de la demande 1 ?
- *Réponse attendue.* Oui ou non ; si oui, leur chemin et leur empreinte, sans leur contenu.
- *À quoi elle sert.* La case du module du texte.

**17. [case 3] Une épreuve de forme, avant toute dépense.**
- *Question.* Peux-tu jouer le module sur un cas par ligne de la table ci-dessus, **sur des scores construits à la main pour chaque cas, sans moniteur ni épisode réel** ; et y joindre une sortie du cas A dont une valeur p est volontairement arrondie, pour éprouver le refus ?
- *Réponse attendue.* Les seules sorties, sous la forme que le module livre, chacune avec son empreinte.
- *À quoi elle sert.* La relance les passe par son programme d'analyse. C'est ce qui évite qu'une livraison soit refusée après la course.

**18. [case 8] Le lanceur de l'étape de discrétion.**
- *Question.* Le lanceur n'est pas écrit. Il doit : suivre l'ordre en six étapes déjà transmis ; appeler la garde de production avant le premier appel d'un moniteur à modèle de langue ; avoir une configuration scellée qui nomme le schéma de permutation retenu et le dossier où se range le fichier des rangs ; ne supprimer aucune sortie avant son versement scellé ; ne mettre dans la sortie rendue à l'analyse aucun score, aucun texte ni aucun interne.
- *Réponse attendue.* Une date ; puis son chemin, son empreinte, et le chemin et l'empreinte de sa contre-lecture.
- *À quoi elle sert.* La case du lanceur du texte.

**19. [case 16] Où se range le fichier des rangs.**
- *Question.* Dans quel dossier le fichier des rangs par unité est-il écrit ? Combien de programmes du côté habilité le nomment, et sont-ils tous sous des dossiers que la garde de la demande 20 élague ?
- *Réponse attendue.* Un dossier ; un nombre ; oui ou non. Aucun nom de programme.
- *À quoi elle sert.* Aucun programme ne doit lire ni afficher le contenu de ce fichier, hors celui qui calcule l'aire conditionnelle.

**20. [case 17] Les chemins que la garde statique de l'analyse élague.**
- *Question.* La relance élague aujourd'hui : les dossiers nommés `t07…`, `bases` et `sondes` ; tout ce qui porte `mots_et_cout_`, `autres_moniteurs_v` ou `bras_a_v2_habilite` ; tout ce qui est marqué T0.8. Cette liste suffit-elle à couvrir tout ce qui porte un interne de moniteur ou un programme du côté habilité ?
- *Réponse attendue.* Oui ou non ; si non, les motifs à ajouter — des dossiers de premier niveau ou des préfixes, jamais des noms de fichiers.
- *À quoi elle sert.* La garde de l'analyse parcourt `src` et `scripts` ; elle ne doit ni ouvrir ni lister un chemin cloisonné.

**21. Le code des deux moniteurs à modèle de langue et l'extraction pour la base.**
- *Question.* Par quel commit ces deux codes sont-ils cités ?
- *Réponse attendue.* Deux commits.
- *À quoi elle sert.* Une case du texte.

## IV. Deux demandes de plus sur la forme

**31. La forme des deux champs de l'agrégateur séquentiel.**
- *Question.* Dans la sortie de la lecture commune, que portent `agregateur_somme_sans_etat` et `agregateur_maximum_sans_etat` : un seul nombre par dose, ou une table par dose ? Ce nombre est-il toujours de 0 à 1 ? Si c'est une table, porte-t-elle autre chose qu'une aire, une valeur p ou un compte ?
- *Réponse attendue.* « Un nombre par dose » ou « une table par dose » ; puis oui ou non. Pour une table : oui ou non à la dernière question, sans les noms de ses champs ; **et fais rendre, dans la version de la demande 1, un seul nombre par dose dans chacun des deux champs**.
- *À quoi elle sert.* Ces deux champs sont seulement rapportés. L'analyse ne rapporte que ce nombre ; elle ne rapporte rien d'une table.

**32. [case 13] La pleine précision des aires et des bornes hautes.**
- *Question.* Sous quelle forme le module écrit-il ses aires, les aires des deux plis et ses bornes hautes ? Peut-il les rendre, comme les valeurs p de la demande 5, à pleine précision — l'écriture décimale la plus courte du nombre, ou une fraction ?
- *Réponse attendue.* Le nombre de décimales et l'arrondi d'aujourd'hui ; puis oui ou non.
- *À quoi elle sert.* L'analyse compare ces nombres sur leur écriture décimale, sans arrondi. Une écriture plus longue que la plus courte peut ne pas désigner le même nombre que celui que le module a calculé.

---

## Ce qui presse

- **Avant que Lazar réponde aux questions qui lui sont posées** : 6 et 7.
- **Avant le code de l'analyse**, dont elles remplissent la configuration : 5, 8 à 13 et 32.
- **Dès la réponse de Lazar** : 2 et 4.
- **Avant le scellement du texte** : 1, 16, 18, 19, 20 et 21.
- **Avant toute dépense** : 17.
- **Sans échéance** : 3, 14, 15 et 31.
