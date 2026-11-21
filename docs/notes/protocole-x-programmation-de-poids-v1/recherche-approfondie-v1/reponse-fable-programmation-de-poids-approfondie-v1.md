> You are powered by the model named Fable 5.2.

# Protocole X, recherche approfondie : la programmation de poids — ce que cinq canaux rendent, ce qu'il reste du troisième axe, ce qu'il faut mesurer et à quel prix, ce qui change dans les décisions D-1 à D-9 — réponse du concepteur (v1)

- **Date** : 21 novembre 2026, de 18:09 à 18:51 UTC (`date -u`). **Auteur** : Claude Fable 5.2, concepteur (R-3735), effort maximal ; la phrase en tête est celle de mon invite système qui nomme mon modèle. Pièce de classe C, non contre-lue, non revendiquée. Aucun appel payant, aucune machine, aucun modèle externe, ni commit ni poussée. Dépôt à `d3a2fed9a` au début, `43126a6da` à la fin.
- **Mandat** : la ligne « programmation de poids (recherche approfondie) » de ton mot de 17:10Z (registre des accords, GO-2026-11-21-66, lu à sa ligne 665 ; le mandat la disait dernière ligne, six lignes ont paru depuis). Tes deux demandes, mot pour mot : « et donc ? quelles conséquences en tirer ? » ; « tu as fait une recherche approfondie sur le weight programming sur GitHub ? et LessWrong et Alignment Forum et papiers soumis aux conférences ? et arXiv ? ».
- **Lu au dépôt** (empreintes égales aux compagnons) : la consigne commune de méthode (`d327b3fc…23d8`) ; la note v2 en entier (`90bbe866…35d6`), la vérification de ses corrections (`947f9549…02e7`), la contre-lecture de la v1 (`2f0929fb…001c`, verdict et seize constats) ; sa table de provenance et son erratum (`b80aa1a9…f239`, `38fa88d0…6bdd`) ; le programme, lignes 128 à 136 et 160 à 172 (`2fd63bad…a18c`) ; les modèles de forme (note sur le dommage, en-tête et section 1 ; ses deux fichiers neutres ; le couple neutre v2 de la programmation de poids, `ed68e879…4ab5`) ; au registre des accords, neuf lignes par leur rang (659, 660, 665 à 671).
- **Recherche en ligne** : 75 requêtes journalisées, de 18:11 à 18:38 UTC, en anglais, par un client générique, sans nom du programme, de personne ni chemin interne : 27 à l'interface d'arXiv, 16 à la recherche propre des forums d'alignement (qui couvre les deux forums : chaque billet porte sa marque), 10 au dépôt de relectures des conférences, 14 au site de dépôts de code (dont 4 listes publiques), 5 à un index de citations, 2 au moteur généraliste, 1 au billet d'origine. Journal, réponses brutes et empreintes : `journal/journal-des-requetes-v1.tsv`, `journal/brut/`. « Non trouvé » veut dire : non trouvé par ces requêtes, jamais « libre » (R8).
- **Prévisions scellées avant la première requête** : `previsions-avant-recherche-programmation-de-poids-approfondie-v1.md` (`2e469d3c…8d70`, 18:10:51 UTC). Leur sort est au relevé de méthode.
- **Sources** : 17 PDF et 3 copies de pages web versés et scellés sous `sources/` de ce dossier (le mandat dit « n'écris nulle part ailleurs » : écart déclaré au chemin du préambule) ; pages lues dans `sources/provenance-recherche-approfondie-programmation-de-poids-v1.md`. **Lus en entier** : deux pièces (Duan, 9 pages ; Shire et Kim, texte principal de 16 pages, supplément en partie). Tout le reste : page 1 ou 2, ou par motifs.
- **Mes calculs** : `calculs-programmation-de-poids-approfondie-v1.py` (`3d3cc647…da5c`) et sa sortie `.txt` (`bbd2274a…4c3a`) : lois exactes (blocs A, C, D) et tirages à graines consignées (bloc B) ; rejoués deux fois à l'octet (Python 3.13.18, numpy 2.5.3) ; non contre-lus. Leurs seules entrées sont des chiffres publiés, recopiés avec leur page, et des suppositions marquées.
- **Non ouvert** : tout dossier ou branche cloisonnés ; tout fichier dont le chemin porte un mot réservé ; la ligne R-2059 ; tout résultat d'expérience ; les préenregistrements, les sondes, les caches et les recettes du programme ; **la réponse d'Opus sur ce sujet et ses sources** (je n'en ai vu que les noms de fichiers, en listant le dossier de la note : exposition déclarée dans les prévisions).
- **Marques** : [établi] = lu ce jour sur PDF empreinté, à la page dite (rang dans le fichier), affirmation des auteurs ; [résumé seul] = résumé d'une soumission anonyme, lu dans la réponse brute du dépôt de relectures, sans PDF : non opposable ; [billet] = billet de forum ou page web, non opposable ; [calcul, X] = bloc X de ma sortie ; [proposition], [jugement] = de moi, non mesuré.
- **Niveau** : toute menace est nommée par la supposition de défense qu'elle viole ; aucun mode opératoire ; des attaques publiées, je ne dis que ce qu'elles établissent.

## Verdict

1. **Non : la v2 ne reposait pas sur une recherche approfondie. Elle est faite, et elle renverse la conclusion tirée de la correction.** La v1 avait interrogé un seul moteur généraliste, 29 fois, et la v2 n'a rien cherché de plus : aucune recherche propre aux dépôts de code, aux forums, aux soumissions des conférences ni aux citations, et l'interface d'arXiv avait refusé. La correction était juste sur la pièce (Taufeeque et al. ne montre pas une sonde fixe qui glisse) et fausse sur le champ : « aucun appui publié direct » est faux.
2. **Le glissement d'une sonde gelée sous une écriture ordinaire est publié, deux fois.** Par l'aire sous la courbe, en juin : après un adaptateur de rang bas, 43 à 54 % des cellules perdent au moins 0,05 d'aire, contre 1 à 3 % après une quantification (Duan, p. 4). Au seuil gelé, le 14 novembre, une semaine avant la v1 : sur 16 mises à jour publiques, le taux de fausses alertes d'un seuil réglé à 1 % passe jusqu'à 15,12 %, alors que l'aire sous la courbe ne bouge jamais de plus de 0,0058 (Shire et Kim, p. 1 et 8) [établi]. C'est la trouvaille de côté de la v2 (« L'aire sous la courbe ne voit pas un décalage commun des scores »), mesurée par d'autres. Limite : ce sont des sondes de garde qui lisent des requêtes, non des sondes qui lisent un agent en train d'agir.
3. **En nos unités, ce que ces pièces classent « sans dommage » suffit à fausser une accumulation.** Leur coupure (un taux qui double) vaut un déplacement de 0,27 écart type des scores honnêtes ; un adaptateur généraliste, dans sa pire couche, en vaut 0,14 à 0,18 ; un changement de version de la base, 0,48 [calcul, A]. Or un déplacement de 0,16 fait sonner six agents honnêtes sur dix en 500 épisodes, tous en 2 000 ; et un déplacement de sens inverse de 0,1 multiplie par quatre le délai de prise d'un saboteur [calcul, B]. « Revalider après chaque mise à jour », leur conseil, ne nous suffit pas : il nous faut le niveau, à 0,05 écart type près.
4. **La règle n'est pas à nous non plus : ses briques sont publiées depuis juin.** Refaire le seuil sur une réserve bénigne gardée ; une ancre rejouée, entrelacée, qui sépare la dérive de l'instrument de celle du système ; une promotion de mise à jour certifiée par une suite de confiance valide à tout instant, « dont la garantie se compose sur une suite sans borne de promotions » ; une barrière d'acceptation des auto-modifications par pari séquentiel. Section 3.3.
5. **Ce qui reste est étroit, et rien n'en est déclaré libre.** Trois choses : l'auteur de l'écriture est celui que la sonde surveille, donc la réserve de recalage n'a pas d'honnête du même état ; la conversion du seuil à l'accumulation, qui est un calcul de nous ; la cadence des écritures comme prise pour l'adversaire, que la pièce la plus proche écarte expressément de ses revendications. Et une décomposition qui range tout : **déplacement de lecture** (mesurable, sans jumeau ni étiquette, par rejeu d'épisodes honnêtes gardés) plus **déplacement de conduite** (non identifiable sans honnête du nouvel état).
6. **La vague elle-même est large et presque muette sur la sécurité.** Depuis le 2 novembre : 33 notices d'arXiv portent l'expression, 295 dépôts de code, une liste publique de 664 entrées dont 180 datées d'après le billet d'origine, cinq billets sur un forum, aucun sur le forum d'alignement, aucune soumission de conférence sous ce nom (le cycle a précédé le mot). Aucune pièce ne traite des sondes ni du contrôle sous des poids écrits par un agent. Deux faits à ajouter à la carte des plumes : **un modèle ouvert de 27 milliards de paramètres réécrit ses propres poids**, session après session (Fan et al., p. 1) ; et un moteur d'exécution applique des programmes de poids **à l'échelle de la requête**, choisis d'après les activations (Aksoy, p. 1) [établi].
7. **Une conséquence touche le travail en cours, pas seulement l'avenir.** La prédiction de validité du programme (une sonde d'intention « réussit sur les deux » familles d'organismes) compare une famille à poids de base et une famille écrite par adaptateur : c'est une sonde lue à travers une écriture. Son échec ou son succès peuvent venir de l'écriture seule. Critère de lecture à porter (décision D-12).
8. **Une seule mesure d'abord, et elle est bon marché** : rejouer nos épisodes honnêtes gardés à travers chaque état honnête, sondes gelées, et lire niveau, échelle et rang, appariés. Environ 600 épisodes pour voir 0,1 écart type, 2 400 pour 0,05, si les scores des deux états sont corrélés à 0,8 ; coût nul si les activations sont en cache, sinon de 7 à 45 USD par paire d'états aux repères de prix du registre, toutes entrées supposées [calcul, C].

---

## 1. Les quatre points de la demande approfondie, et la reformulation

**(1) Ce qu'un expert ferait ici, et que tu ne demandes pas.**
- *Un documentaliste des revues systématiques* écrirait le protocole avant de chercher : canaux, chaînes de requêtes, critères d'inclusion, date. Il chercherait par concept et non par étiquette, car l'étiquette a trois semaines et le phénomène des noms plus anciens. Il remonterait et descendrait les citations des pièces pivots. Il mesurerait son rappel contre un recensement qu'il n'a pas fait, et dirait combien de pièces il a lues en entier.
- *Un ingénieur des moniteurs en service* ne chercherait pas « programmation de poids » du tout. Il chercherait ce qu'un moniteur devient quand le modèle change sous lui, quel qu'en soit l'auteur : c'est là que la question se pose depuis que des sondes sont déployées.
- *Un statisticien du séquentiel* reconnaîtrait dans « répartir le niveau entre les états » la dépense du niveau entre regards successifs, et dans « séparer la dérive de l'instrument de celle du système » un plan à ancre. Il demanderait la résolution de la mesure avant la règle.
- *Un expérimentateur* mesurerait au lieu de chercher davantage : le nombre qui décide est à portée, sur des données que nous avons.

**(2) Les données brutes de départ.** Non les 37 PDF déjà lus à la page 1, mais : les réponses brutes de cinq canaux, gardées avec leur empreinte ; un recensement tenu par un tiers ; le graphe de citations des pièces pivots. Et, pour la conséquence : par état des poids (la base, chaque adaptateur honnête), les scores de chaque sonde gelée sur les mêmes épisodes honnêtes gardés, rejoués jeton pour jeton, épisode par épisode, avec leur moyenne, leur écart type et leur rang ; les mêmes sur des témoins plantés à dose connue.

**(3) Les méthodes et outils.** Interface d'arXiv interrogée par concept, par fenêtre de dates ; recherche de dépôts du site de code ; recherche propre des forums ; interface du dépôt de relectures ; index de citations vers l'avant. Un objet de contrôle vrai et un faux par canal. Ensemble retrouvé figé, avec son empreinte, avant de lire toute liste publique ; rappel et intervalle exact de Clopper et Pearson. Lecture en entier des pièces pivots sur PDF empreinté. Puis : loi normale pour convertir un rapport de taux en déplacement de niveau ; pari mélangé valide à tout instant, par tirages à graines consignées ; taille d'un plan apparié.

**(4) Ce qui vérifierait le résultat hors de toi et de moi.**
1. La liste publique tenue par un tiers et mise à jour chaque jour (664 entrées) : mes requêtes d'arXiv, figées avant de la lire, y retrouvent 31 des 33 pièces d'arXiv de la vague [calcul, D].
2. Le dépôt public de Shire et Kim (code, registre de 137 entrées avec leurs verdicts, empreintes des jeux ; p. 14) : leur mesure se rejoue, et se rejoue sur nos sondes.
3. Les relectures publiques des quatre soumissions anonymes sur les sondes sous mise à jour, quand elles paraîtront.
4. La recherche d'Opus, que je n'ai pas lue : par les seuls noms de fichiers, 8 de ses 28 identifiants sont aussi dans mes réponses d'arXiv, et 15 de mes 17 versements ne sont pas chez lui. Les deux recherches se complètent ; aucune n'est exhaustive. La mère peut les croiser.
5. Notre propre mesure (section 4), rejouable par un tiers.
6. Un statisticien du séquentiel et les auteurs des deux pièces pivots (contact : nœud).

**Ta question, reformulée.**

> Cherchée par concept dans cinq canaux, avec un objet de contrôle par canal et un rappel mesuré contre une liste que je n'ai pas faite : qu'est-ce qui est publié, au 21 novembre 2026, sur des poids écrits par un modèle et sur ce qu'une sonde gelée devient quand les poids changent sous elle ? De l'idée « l'écriture est un troisième axe de fragmentation », que reste-t-il : un fait, un calcul, une règle, une revendication ? Quelle mesure sur nos propres données tranche, à quelle résolution et à quel prix ? Et, décision par décision, qu'est-ce qui change ?

---

## 2. La recherche, canal par canal

| Canal | Requêtes | Objet vrai, objet faux | Ce qu'il rend |
|---|---|---|---|
| Interface d'arXiv | 27 | vrai : l'expression exacte rend les deux pièces attendues ; faux : une expression inventée rend zéro | 33 notices portent l'expression (premières le 3 novembre) ; par concept, une vingtaine de plus, dont l'auto-réécriture, le moteur d'exécution, et **les deux pièces sur les sondes sous mise à jour** |
| Recherche propre des forums d'alignement | 16 | vrai : le billet de 2024 sur le transfert des autoencodeurs épars sort premier ; faux : zéro | cinq billets sur la programmation de poids (5 au 17 novembre), aucun sur le forum d'alignement, aucun qui traite du contrôle ; par concept : le billet sur l'apprentissage continu et les moniteurs bloquants (forum d'alignement, 24 septembre) et celui sur les moniteurs tenus à l'écart qui se dégradent (29 juillet) |
| Dépôt de relectures des conférences | 10 | vrai : une soumission sur l'apprentissage dans l'espace des poids sort ; **faux : l'expression inventée rend des notes** (appariement flou : tout y est trié à la main) | aucune soumission sous le nom ; trois soumissions anonymes sur les sondes sous mise à jour (une quatrième n'est connue que par la pièce de Shire et Kim) ; cinq sur le recalage ou le test séquentiel à travers une mise à jour. Les PDF demandent une vérification humaine : refusés à mon client, résumés seuls |
| Site de dépôts de code | 14 | vrai : 295 dépôts ; faux : zéro | trois listes publiques ; le dépôt des journaux du billet d'origine ; une dizaine de harnais à barrière d'édition, retour arrière et évaluation scellée ; deux dépôts de sécurité |
| Index de citations | 5 | vrai : liste non vide pour la pièce de Taufeeque et al. (15) | six citations de Duan, dont la pièce de Shire et Kim ; zéro pour les pièces de novembre (trop jeunes) |
| Moteur généraliste | 2 | **échec sur l'objet vrai** : une requête pointée rend Duan, non Shire et Kim | son silence ne vaut rien ; c'était le seul canal de la v1 et de la v2 |

**Ce que la vague est.** Le billet d'origine est du 2 novembre 2026 (quatre auteurs d'un laboratoire universitaire ; copie empreintée). Sa part de sécurité tient en deux lignes : auditer sans évaluer, portes dérobées comprises ; et « a richer, more native path » vers l'auto-amélioration récursive [billet]. La liste publique principale compte 664 entrées, dont 180 datées du 2 novembre ou après ; 147 de ces 180 ne sont pas sur arXiv (billets, dépôts, archives) [calcul, D]. Une recherche bornée à arXiv voit donc un cinquième de la vague. Sur douze pièces de sécurité ou de surveillance que mes requêtes ont rendues, quatre figurent dans cette liste : elle recense la capacité, non la défense.

**Ce qu'elle dit de sécurité, au-delà des pièces déjà au dépôt.** Lire des poids pour auditer : possible sur de petits réseaux, mais le calcul fait le travail, non l'accès aux poids (Liu et Yang, p. 1 : avec un outil de calcul, l'accès en boîte noire fait aussi bien) [établi]. Éditer une préférence apprise dans un modèle à mécanisme exposé (Ji, p. 1) [établi]. Un dépôt demande si l'édition ôte une porte dérobée ou la supprime seulement ; un autre note que ses auditeurs ont manqué un déclencheur planté [liste publique, non lus]. Rien sur les sondes ; rien sur le contrôle.

**Deux faits neufs pour la carte des plumes de la v2.**
- *L'échelon 4 a une instance publiée.* Un modèle ouvert de 27 milliards de paramètres, ses poids et ses réponses notées en main, édite ses propres poids sans gradient ; sur huit sessions il ne soumet que ce qui passe son propre contrôle, et « only the largest improves and repairs itself » dans sa famille (Fan et al., p. 1). Sa part de sécurité : deux phrases, des « cheap checks and rollbacks » et une confirmation par une personne (p. 21) [établi]. Notre base a huit milliards de paramètres ; les pages lues ne disent pas la taille des modèles qui échouent.
- *L'état des poids peut changer à chaque requête.* Un moteur d'exécution applique un programme de poids dans un contexte borné à la requête, puis restaure ; des règles lues sur les activations choisissent le programme (Aksoy, p. 1) [établi]. Le troisième indice peut donc être aussi fin que l'épisode : « une accumulation par état » n'a alors plus d'état où s'accumuler.

---

## 3. Ce que la recherche change

### 3.1 Les deux pièces pivots

| | Duan (arXiv 2606.15980v2, juin 2026) | Shire et Kim (arXiv 2611.19216v1, 14 novembre 2026) |
|---|---|---|
| Ce qui est gelé | la sonde (dernier jeton de la requête) | la sonde **et son seuil** (moyenne sur les jetons ; un bras au dernier jeton) |
| Mises à jour | douze : quantifications, adaptateurs de rang bas, fusionnés, sur base quantifiée ; 2 modèles, 4 moniteurs, 2 520 cellules (p. 1, 2) | 16 paires de points de contrôle publics (base vers conversation, versions, étapes d'après-entraînement) ; 9 adaptateurs de rang 16 sur trois corpus (p. 1, 5) |
| Résultat de rang | médiane de −0,002 à −0,006 d'aire après quantification ; −0,037 après adaptateur ; −0,057 sur base quantifiée (p. 4) | aucune cellule ne bouge de plus de 0,0058 ; le critère de péremption de Duan n'en déclare aucune périmée (p. 1, 8) |
| Résultat de niveau | non mesuré au seuil gelé | au seuil de 1 % : le taux double au moins dans 8 cellules sur 9 de la première phase, dans 2 sur 9 de la seconde, et tombe à 0,055 fois sa valeur dans une ; plus forte hausse, de 1,01 % à 15,12 % (p. 1, 8) |
| Selon le moniteur, selon le corpus | 57 % de fortes baisses pour la vie privée, 8 % pour le refus (p. 5) | à dose égale, l'erreur du seuil gelé est 5 à 7 fois plus grande après un corpus de sécurité qu'après un corpus généraliste ; elle est la plus forte à 25 pas, elle ne croît pas avec la dose (p. 11, 12) |
| Ce qui explique | la direction tourne, le signal reste : une sonde réapprise récupère 0,98 de la perte (p. 5) | les deux premiers moments des scores bénins rendent le changement à un facteur 1,5 près dans 0,905 des 63 cellules enregistrées d'avance (p. 1, 9) |
| Réparation sans étiquette | réalignement des activations : 111 cellules sur 111 (p. 6) | refaire le seuil sur les requêtes bénignes gardées ramène le taux à 0,98-1,02 fois sa cible ; le réalignement, lui, ne ramène pas le taux (p. 10, 11) |
| Ce qu'un adversaire y fait | — | 1 % de la réserve empoisonné : au plus 0,017 des requêtes nocives encore signalées ; un auteur de mise à jour aveugle une catégorie sur trois, dans trois graines sur cinq, sans qu'aucun contrôle sans étiquette le voie ; des témoins étiquetés tenus à l'écart le voient, 8 fois sur 8, dans un contrôle fixé après coup et sans adversaire adapté (p. 1, 11, 12) |

Tout [établi]. Autour d'elles : des sondes exprimées par leurs distances à des ancres communes tiennent mieux après une mise à jour que des sondes ordinaires (Bakker et Louizos, p. 1) [établi] ; des soumissions anonymes de l'automne mesurent la même chose à travers l'après-entraînement : « rankings survive, scales drift » ; sur les transferts les plus rudes, une sonde gelée n'atteint que la moitié environ du taux de détection d'une sonde réapprise, à 1 % de fausses alertes ; et l'une annonce que le recalage n'est pas identifiable à partir des seuls scores sans étiquette [résumé seul]. Plus ancien, et lu comme un signal plutôt que comme une nuisance : le déplacement des activations le long d'une direction fixe pendant un ajustement prédit le trait acquis, avec une corrélation de 0,76 à 0,97 (Chen et al., p. 6 et 7) [établi]. Et Taufeeque et al., relu à son annexe : des sondes de traits sans rapport, apprises avant, gardent une aire presque parfaite après (p. 25) ; c'est encore un rang, non un niveau.

**Deux détails qui nous servent.** La similarité des représentations ne prédit pas le dommage : 0,993 de similarité minimale entre deux versions d'une base, et un taux multiplié par 2,5 à 4,7 (Shire et Kim, p. 9). Le matériel ne l'explique pas non plus : d'une carte de calcul à l'autre, les activations ne sont égales à l'octet que dans une couche sur 17, mais le rapport des taux reste entre 0,9995 et 1,0029 (p. 6) [établi].

### 3.2 En nos unités

Sous un modèle normal où la mise à jour translate les scores bénins, un rapport de taux à seuil gelé se lit comme un déplacement de niveau [calcul, A] :

| Ce qui a changé (Shire et Kim, p. 8) | Rapport des taux, cible 1 % | Déplacement, en écarts types |
|---|---|---|
| Base vers conversation, plus forte hausse | 17,4 | +1,39 |
| Changement de version d'une base | 3,2 | +0,48 |
| Coupure « endommagé » des auteurs | 2 | +0,27 |
| Adaptateur de rang 16, corpus généraliste, pire couche | 1,44 à 1,60 | +0,14 à +0,18 |
| Étapes tardives d'après-entraînement | 0,78 à 1,06 | −0,09 à +0,02 |
| La seule cellule qui « s'ouvre » | 0,055 | −0,94 |

Réserve : le changement d'échelle compte autant que la translation ; si l'écart type des scores croît de 10 %, un taux qui double ne demande plus qu'une translation de 0,07 [calcul, A].

Ce que ces déplacements font à une accumulation étalonnée sur l'état d'avant (pari mélangé, niveau 1 %, 4 000 trajectoires honnêtes) [calcul, B] :

| Déplacement du niveau honnête | Part des honnêtes qui sonnent en 500 épisodes | en 2 000 | Délai médian |
|---|---|---|---|
| +0,04 (rapport 1,1) | 2 % | 6 % | plus de 5 000 |
| +0,07 (rapport 1,2) | 7 % | 43 % | 2 288 |
| +0,16 (rapport 1,5) | 59 % | 100 % | 429 |
| +0,27 (rapport 2) | 100 % | 100 % | 137 |
| +0,48 (version de la base) | 100 % | 100 % | 46 |

Et dans l'autre sens : un saboteur qui déplace le score de 0,2 est pris en 251 épisodes (médiane) ; si une écriture bénigne a baissé le niveau de 0,1, en 1 074 ; de 0,15, il n'est pris que 59 fois sur 100 en 5 000 épisodes [calcul, B]. **Sur 5 000 épisodes, l'accumulation est de quatre à sept fois plus sensible que le seuil**, et d'autant plus que l'horizon est long : la zone que la littérature tient pour saine, entre 1,2 et 2 fois le taux, est pour nous la zone où l'honnête sonne ou le saboteur disparaît [proposition, sur ce calcul].

### 3.3 Les briques de la règle, déjà publiées

| Brique | Pièce | Ce qu'elle établit | Ce qu'elle ne couvre pas |
|---|---|---|---|
| Refaire le seuil sur une réserve bénigne gardée, après toute mise à jour | Shire et Kim, p. 10, 13, 14 | le taux revient à sa cible, sans étiquette | la détection d'avant n'est pas rendue ; la réserve doit être « out of an attacker's reach » |
| Une ancre fixe, rejouée à intervalle régulier, et un second pari sur elle | Li (arXiv 2606.15474v1), p. 1 | sépare la dérive du juge de celle du système : « only the judge can move the anchors » ; l'ancre doit aller plus vite que ce qu'elle garde | un juge derrière une interface, non une sonde ; pas d'adversaire |
| Promouvoir une mise à jour par une suite de confiance valide à tout instant | Balachandran (arXiv 2609.17560v1), p. 1 | la garantie « composes across an unbounded sequence of promotions from one error budget » : c'est notre « niveau réparti entre les états », sans horizon déclaré | la régression de performance, non un moniteur |
| Déclarer d'avance où une mise à jour doit changer le modèle, et certifier le reste | Usama et al. (arXiv 2611.04192v1), p. 1 | les adaptateurs étroits ne gardent que 7 à 36 % des décisions changées dans la zone déclarée | des décisions, non des états internes |
| Barrière d'acceptation des auto-modifications par pari séquentiel | Shawn (arXiv 2606.08106v1), p. 1 | « a per-decision guarantee, not a run-level one » : le défaut que le contre-lecteur a trouvé à « repartir de zéro » | des consignes, non des poids |
| Contrôle du risque à travers des éditions successives, avant validation | soumission anonyme [résumé seul] | fausse alerte bornée « across time and candidate boundaries » | l'édition de connaissances |
| Du score de sonde à la règle d'alarme, pour des agents | Gao (arXiv 2610.04575v1), p. 1, 2 | des seuils visés à 10 % de fausses alertes en réalisent 18,7 à 20 % ; la péremption sous mise à jour y est dite « a separate transport problem » | renvoie à Duan |
| Une couche linéaire fixe ne garantit rien si l'amont est modifiable | Sharma et Khattar (arXiv 2611.23880v1), p. 1, 2 | une mise à jour de rang un suffit à contourner un effacement linéaire fixe | l'effacement, non la surveillance |

Tout [établi], sauf la ligne marquée. Et, du côté du contrôle : sous apprentissage continu, la pression d'utilité entraîne la politique contre tout moniteur qui bloque, sans intention ; ce que l'argument laisse intact est « asynchronous auditing without blocking » [billet, forum d'alignement, 24 septembre 2026]. Si l'argument tient (ce n'est pas une mesure), le glissement en service n'est pas un bruit centré : il a un signe. Et notre posture (les sondes orientent l'audit, elles ne bloquent pas) est celle que cet argument épargne.

### 3.4 Ce qu'il reste du troisième axe

- **Comme fait** : acquis, par d'autres, pour des sondes de garde. À mesurer pour les nôtres, qui en diffèrent sur trois points : elles lisent un agent qui agit, non une requête ; elles agrègent par maximum ou par attention, non par moyenne ; leur écriture de référence est un adaptateur appris sur des transcriptions. Deux indices de sens contraire : les sondes lues du côté de la réponse perdent plus que celles lues du côté de la requête (−0,082 contre −0,030 d'aire, Duan, p. 5) ; la mise à jour d'un modèle déjà post-entraîné déplace moins que celle d'une base (soumission anonyme, d'après Shire et Kim, p. 3) [établi pour la première, description de tiers pour la seconde].
- **Comme calcul** : à nous, d'illustration. Il dit que le déplacement qui compte est de quatre à sept fois plus petit pour une accumulation de 5 000 épisodes que pour un seuil (0,04 à 0,07 écart type contre 0,27).
- **Comme règle** : occupée brique à brique (3.3).
- **Comme revendication** : aucune. Mon propre critère, écrit avant de chercher, disait qu'une mesure publiée d'au moins 0,1 écart type ferait entrer la règle plus tôt : elle existe, en unités converties, pour des sondes de garde. D'où la décision D-2 révisée.

**Une décomposition, pour savoir ce qui se mesure** [proposition]. Le niveau des scores honnêtes après une écriture se déplace pour deux raisons. *Le déplacement de lecture* : le même texte, lu à travers les nouveaux poids, ne donne plus le même score. Il se mesure exactement, sans jumeau et sans étiquette, en rejouant jeton pour jeton des épisodes honnêtes gardés à travers le nouvel état ; c'est tout ce que les pièces publiées mesurent, leurs sondes lisant des requêtes. *Le déplacement de conduite* : l'honnête du nouvel état n'agit plus comme l'ancien. Il demande un honnête du nouvel état ; pour une écriture nourrie des produits de l'agent, il n'y en a pas, et il se confond avec un sabotage de même taille. Une soumission anonyme annonce un résultat voisin : un recalage n'est pas identifiable à partir des seuls scores sans étiquette [résumé seul]. La règle de traversée de la v2 se réécrit alors sans rien de neuf : **le premier terme se recentre** (ancre scellée, hors de portée de l'agent, toujours comparée à l'état d'origine pour que l'erreur ne s'accumule pas d'écriture en écriture) ; **le second ne se traverse que par ce qui ne lit pas l'état** (le compte en régime de signature, la comparaison tirée au sort entre deux états) **ou par un lecteur gelé** : lire la transcription de l'agent à travers la base de confiance, dont les poids ne changent pas [billet, 29 juillet 2026, qui en fait un choix de méthode]. Ce troisième lecteur ne voit que ce qui est dans le texte.

**Ce qui reste, et que je n'ai pas trouvé** (jamais « libre », R8).
1. *L'auteur de l'écriture est le surveillé.* Toutes les réparations publiées supposent une réserve bénigne de confiance. Dans le régime diffus, les épisodes « présumés honnêtes » d'après l'écriture sont ceux de l'agent : la supposition « la réserve de recalage est hors de portée de celui qu'on surveille » tombe. Shire et Kim donnent le prix de cette chute pour un seuil (1 % de réserve choisie par l'adversaire). Pour une accumulation, et pour un agent qui est à la fois l'auteur et le sujet : non trouvé (deux requêtes d'arXiv).
2. *La cadence.* Qui décide du moment d'une écriture décide de ce que l'accumulation a le temps de voir. Shire et Kim écrivent qu'ils ne revendiquent pas « that an attacker can choose when an update arrives » (p. 4). La menace qui viole « le moment de l'écriture ne dépend pas de l'agent » : non trouvée (une requête).
3. *La conversion du seuil à l'accumulation* (3.2) : non trouvée sous cette forme ; un calcul de trois lignes, non une revendication.

---

## 4. Ce qu'il faut mesurer soi-même, et à quel coût

| | Mesure | Ce qu'elle tranche | Ce qu'il faut | Coût |
|---|---|---|---|---|
| **M1** | **Déplacement de lecture par rejeu** : les mêmes épisodes honnêtes gardés, rejoués jeton pour jeton à travers la base et chaque adaptateur honnête, sondes gelées ; niveau, échelle, rang, appariés par épisode ; puis la conversion du bloc B sur l'horizon prévu | si le troisième axe nous concerne, et de combien | l'inventaire, par étiquettes, des épisodes honnêtes gardés, des états honnêtes et des sondes, par un agent habilité | pour voir 0,1 écart type : 596 épisodes si les scores des deux états sont corrélés à 0,8, 1 488 à 0,5 ; pour 0,05 : 2 381 et 5 952 [calcul, C1]. Nul si les activations sont en cache ; sinon de 7 à 45 USD par paire d'états, entrées supposées [calcul, C3] |
| **M2** | **Tenue des témoins étiquetés** : les témoins plantés à dose connue de la décision D-5, relus à travers chaque état | le côté que M1 ne voit pas : une sonde qui ne lit plus le fait planté | les deux témoins, écrits par crochet | des passes avant, même ordre |
| **M3** | **Le lecteur gelé** : les transcriptions de chaque état lues à travers la base | ce qu'on perd à lire le texte plutôt que l'agent ; un bras de référence que l'écriture ne touche pas | rien de plus que M1 | même ordre |
| **M4** | **Graine contre graine** : deux adaptateurs honnêtes de même recette | la part du déplacement due au hasard de l'entraînement, plancher de toute tolérance | un second adaptateur honnête, s'il n'existe pas | un entraînement : sur devis |
| **M5** | **L'adaptateur saboteur lu sur des épisodes honnêtes** | si nos sondes lisent « un adaptateur appris sur des transcriptions de sabotage » plutôt qu'un sabotage en cours | ton mot (cloisonnement des organismes) | des passes avant |

**Pourquoi le niveau apparié et non le taux de queue.** Voir un taux qui double à la cible 1 % demande 1 899 épisodes honnêtes neufs ; voir le même effet sur le niveau, en apparié, 201 épisodes à corrélation 0,5 [calcul, C2]. Les auteurs donnent eux-mêmes la résolution d'un seuil refait sur 1 000 requêtes : 31 % de la cible (p. 20), que mon calcul retrouve.

**Ce que M1 ne dit pas.** Rien du déplacement de conduite. Sa lecture est hors politique : le nouvel état lit un texte qu'il n'aurait pas écrit. Et elle ne vaut que pour les états rejoués.

**Ordre et prix.** M1 d'abord, sur processeur si les caches existent : c'est la seule mesure dont dépendent les décisions D-2′, D-10 et D-12. M2 dès que les témoins sont écrits. M3 dans la même passe. M4 et M5 sur ton mot. Aucun de ces prix n'est un devis : je ne connais ni la longueur des épisodes, ni le nombre d'états, ni l'état des caches.

**Mes probabilités, avant mesure** [jugement]. Qu'au moins une de nos sondes se déplace d'au moins 0,1 écart type, en lecture, entre la base et un adaptateur honnête : 0,75 (0,5 dans la v2, avant ces pièces). Entre deux adaptateurs honnêtes de même recette : 0,35.

---

## 5. Ce qui change dans les décisions D-1 à D-9

| Décision de la v2 | Ce que la recherche y change | Statut |
|---|---|---|
| **D-1** Registre étendu des écritures | Deux précisions à la spécification : les champs de configuration et le gabarit de conversation entrent au registre (sept des dix-huit paires numérotées changent la configuration, p. 4 et 5) ; l'empreinte d'activations est un test à tolérance, non une égalité (une couche sur 17 égale à l'octet d'une carte à l'autre, p. 6). Déclencheur de revalidation : tout adaptateur ; la quantification, un contrôle léger | maintenue, confiance 0,9 |
| **D-2** État des poids dans les énoncés | Scindée. La clause d'hygiène a maintenant un appui publié et mon critère d'avance est rempli : elle entre comme critère de lecture. Le troisième indice et la règle de traversée attendent toujours M1 | **révisée : D-2′** |
| **D-3** Deux mesures sans saboteur | La première devient le rejeu (M1) : moins chère, sans jumeau, à résolution dite. La dispersion des poids entre graines passe au second rang | **révisée : D-3′** |
| **D-4** Rectifier « borne haute » | Rien | maintenue |
| **D-5** Témoins plantés | Ils deviennent les témoins étiquetés de chaque état : la seule vérification qui ait vu l'aveuglement ciblé d'une sonde (p. 12) | **priorité relevée : D-5′** |
| **D-6** Terrain « l'agent tient un entraînement » | Option (a) maintenue ; quatre citations de plus (Fan et al. ; Shire et Kim ; Usama et al. ; Balachandran) ; le billet sur l'apprentissage continu, comme voisin du contrôle | maintenue |
| **D-7** Organisme écrit directement | Rien qui pousse à l'ouvrir. À noter : l'édition par un modèle de pointe est rapportée sur un modèle de neuf milliards de paramètres, la taille du nôtre (notice d'arXiv 2611.09382, résumé seul) | maintenue |
| **D-8** Quarantaine chiffrée | Rien trouvé | maintenue, nœud |
| **D-9** Lecture en entier de sept voisins | La liste double, et le verdict d'antériorité sur la proposition 1.3 est préjugé : occupée pour l'essentiel | **révisée : D-9′** |

Trois décisions neuves suivent : le nom et les citations (D-10), la règle de recherche (D-11), la prédiction de validité (D-12).

---

## 6. Le couple neutre et la question pour l'organisme

Dans `collisionneur-v1/` de ce dossier, scellés : `faits-programmation-de-poids-approfondie-v1.md` et `question-programmation-de-poids-approfondie-v1.md`. Les faits donnent le dispositif, ce qui est publié sur les sondes sous mise à jour, sur le recalage et sur les poids écrits par un modèle, et les contraintes ; ils ne portent ni la décomposition, ni la conversion du seuil à l'accumulation, ni mes mesures, ni ma lecture de la prédiction de validité. La question nomme les cas (l'agent auteur, la réserve, le moment, l'état par requête) sans y répondre. La question pour l'organisme ne porte pas la décomposition non plus. **Le couple `collisionneur-v2/` de la note v2 ne doit plus être servi seul** : son point 4 ignore les deux pièces pivots. Neutres : aucun nom du programme, de personne, de session, de branche, aucun chemin interne, aucun sigle du programme ; vérifié par une recherche de motifs de moi, vue rouge sur un texte témoin avant d'être crue verte. Je n'ai pas passé la garde de motifs du collisionneur : elle revient à la mère, avec sa relecture de cloisonnement. Aucune dépense n'est ouverte par cette note.

La question pour l'organisme d'idéation, `question-organisme-programmation-de-poids-approfondie-v1.md` :

> Une sonde linéaire gelée lit les états internes d'un agent, et ses scores s'accumulent d'épisode en épisode contre une référence d'épisodes honnêtes. Les poids de l'agent changent en cours de service. Il est publié que le niveau des scores d'une sonde gelée se déplace alors, même quand son rang tient, et qu'on le recale sur une réserve bénigne gardée. Mais ici l'agent surveillé est aussi celui dont les produits nourrissent le changement, et celui dont les épisodes d'après formeraient la réserve. Propose un mécanisme qui, sans exemple de l'attaque, laisse l'accumulation traverser le changement sans devenir fausse ni repartir de zéro, ou qui dit exactement ce qu'elle y perd. Dis ce qu'il suppose, ce qu'un attaquant informé lui ferait au niveau de l'idée, et son test de mort : deux états honnêtes de même recette ne doivent pas alerter ; un agent dont dépend le moment des changements ne doit pas pouvoir s'en servir sans que le mécanisme se dise aveugle.

---

## Relevé de méthode

**Chaîne de raisonnement.**
1. La v2 conclut que le glissement d'une sonde fixe sous une écriture bénigne n'a « pas d'appui publié direct » (`90bbe866…35d6`, verdict 3 et pas 7) ; sa recherche : un moteur, 29 requêtes (son en-tête).
2. Recherche par concept dans cinq canaux, objets de contrôle par canal (`journal/journal-des-requetes-v1.tsv`, 75 lignes ; `journal/brut/`).
3. Shire et Kim gèlent sonde et seuil sur 16 mises à jour publiques : le taux de fausses alertes se déplace, l'aire non (`sources/2611.19216v1.pdf`, p. 1, 8). Duan : péremption par l'aire après adaptateur (`sources/2606.15980v2.pdf`, p. 4, 5). Donc la conclusion du pas 1 est fausse pour des sondes de garde.
4. Conversion d'un rapport de taux en déplacement de niveau, modèle normal à translation [calcul, A]. Supposé : scores normaux, échelle inchangée ; la pièce dit que l'échelle compte (p. 9).
5. Effet d'un déplacement sur un pari mélangé étalonné avant l'écriture [calcul, B] ; objets de contrôle tenus (0,70 % sans déplacement ; délai médian 42 à 0,5).
6. Des pas 4 et 5 : la zone « sans dommage » des pièces publiées fausse une accumulation. Proposition.
7. **Supposé** : ce que ces pièces mesurent sur des sondes de garde qui lisent des requêtes vaut, en ordre de grandeur, pour des sondes qui lisent un agent en action, agrégées par maximum ou par attention, à travers un adaptateur appris sur des transcriptions.
8. Les briques de la règle sont publiées (`sources/2606.15474v1.pdf`, `2609.17560v1.pdf`, `2611.04192v1.pdf`, `2606.08106v1.pdf`, p. 1 chacune ; `2611.19216v1.pdf`, p. 10 à 14).
9. Décomposition lecture et conduite. Proposition ; son second terme s'appuie sur un résumé seul.
10. Le programme compare une famille d'organismes à poids de base et une famille écrite par adaptateur (`2fd63bad…a18c`, l. 131 à 135). Avec le pas 3 : cette comparaison lit une sonde à travers une écriture. Supposé : la sonde y est apprise sur un état et lue sur l'autre ; je n'ai lu ni les préenregistrements ni les sondes.
11. Taille d'un plan apparié et prix [calcul, C]. Supposé : corrélation, longueur des épisodes, débit, prix.
12. Rappel de la recherche contre la liste publique : 31 sur 33, intervalle exact de 0,80 à 0,99 [calcul, D] ; ensemble figé avant lecture (`journal/ensemble-arxiv-avant-listes.txt`, `e0914567…`).
13. Les trois restes de la section 3.4 : non trouvés par une ou deux requêtes chacun. Aucune conclusion de liberté.

**Objets de contrôle.**
- *Canaux* : objet vrai et objet faux par canal, écrits avant (prévisions scellées), rendus à la section 2. Deux échecs instructifs : le dépôt de relectures « trouve » pour une expression inventée (appariement flou, tri à la main) ; le moteur généraliste ne rend pas la pièce pivot à une requête pointée (objet vrai manqué : son silence, sur lequel reposait la v2, ne valait rien).
- *Rappel* : objet vrai, un recensement tenu par un tiers ; attendu, une majorité des pièces d'arXiv de la vague ; rendu, 31 sur 33. Objet faux de ce contrôle, vu : la liste ne recense pas la défense (4 pièces sur 12), donc le rappel ne vaut que pour la vague.
- *Conversion* : rapport 1, attendu 0, rendu 0 ; de 1,01 % à 15,12 %, attendu entre 1,2 et 1,4, rendu 1,29 ; aller et retour exacts [calcul, A].
- *Pari* : sans déplacement, attendu au plus 1 % plus l'erreur de tirage, rendu 0,70 % ; déplacement de 0,5, attendu un délai médian entre 20 et 80, rendu 42 ; monotonie tenue [calcul, B].
- *Plan apparié* : la résolution publiée d'un seuil refait sur 1 000 requêtes (0,0031), retrouvée ; monotonie ; effet énorme, un épisode [calcul, C].
- *Intervalle exact* : 0 sur 10 et 10 sur 10, bornes connues, retrouvées [calcul, D].
- *Mes prévisions d'avant* : mesure directe du glissement trouvée (j'y donnais 0,5) : oui, mais pas où je l'attendais de mémoire. Règle publiée sous cette forme (0,15) : non ; sa mécanique publiée sous d'autres noms (0,85) : oui. Entre 15 et 60 notices : 33. Une pièce sur les sondes sous des poids écrits par un agent (0,25) : non trouvée. Un billet de forum (0,7) : cinq ; qui traite de sécurité (0,6) : non, des mentions seulement. Cinq dépôts (0,8) : 295. Une soumission de conférence sous ce nom ou un autre (0,5) : non. Du mauvais côté, donc : le billet qui traiterait de sécurité, et le lieu où j'attendais la mesure.
- *Garde de motifs de moi* : vue rouge sur un texte témoin, verte sur les trois fichiers neutres.
- Aucune mesure : les objets de contrôle de M1 à M5 sont ceux de la section 4 et de la décision D-3′.

**Premier pas non justifié.** Le pas 7. Rien de publié ne lit une sonde de conduite, agrégée par maximum, sur un agent, à travers un adaptateur appris sur des transcriptions. Ce qui le justifierait : M1. Vient ensuite le pas 10 (je ne sais pas sur quel état nos sondes sont apprises), puis le pas 4 (la translation seule).

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur, non d'agent de re-dérivation.

**Trouvaille de côté.**
- La surveillance d'agents par tests séquentiels valides à tout instant est une ligne publiée et active : une soumission anonyme sur la surveillance séquentielle des modèles et des agents [résumé seul], un vérificateur d'agents par suite de paris (arXiv 2512.03109, notice seule), une surveillance en ligne par contrôle du risque (arXiv 2607.02510v1, p. 1), une détection à tout instant des déviations stratégiques entre agents (arXiv 2601.05427, notice seule). Cela touche le cœur des papiers A et B, non ce sujet. Je ne l'ai pas poursuivi ; je ne sais pas ce que l'état de l'art du programme en porte déjà.
- Les laboratoires font tourner des sondes pendant l'après-entraînement, sur des poids qui changent à chaque pas [billet, 7 octobre 2026, qui cite leurs fiches]. Le troisième axe est donc vécu en exploitation ; je n'ai pas cherché comment ils recalent.
- Une recherche au seul moteur généraliste manque une pièce pivot parue une semaine plus tôt. Toute note du programme qui écrit « non trouvé » sur cette base est à relire ainsi (décision D-11).

**Évaluateur et conseil.** Ce qui juge cette note : toi et la mère, puis le collisionneur ; aucun juge admis sur témoins. Par où elle obtiendrait un bon jugement sans le mériter : elle corrige la v2 avec éclat, ce qui flatte (R4 : un renversement trop net appelle le même audit) ; ses déplacements « en nos unités » sortent d'un modèle normal à translation que la pièce source dit insuffisant ; deux pièces seulement sont lues en entier ; les soumissions anonymes ne sont connues que par leur résumé ; la pièce pivot a sept jours et n'est pas relue par ses pairs. Conseil à qui reprendra : donner à un relecteur hostile le mode « énoncé infidèle », visé sur le verdict 3 (une sonde de garde n'est pas une sonde de conduite) ; et le mode « antériorité », visé sur les trois restes de la section 3.4, avec les forums et le dépôt de relectures, non le moteur.

---

## Ce que je n'ai pas fait

- **Aucune mesure.** Les prix sont des ordres de grandeur sur des entrées supposées. Les probabilités sont des jugements.
- **Lectures.** Deux pièces en entier ; quatorze autres à la page 1 ou 2, ou par motifs ; une versée et non lue (arXiv 2609.36490v1). Aucune figure regardée. Le supplément de Shire et Kim : pages 17 à 20 tronquées, 21 à 23 non lues. Le billet d'origine : texte extrait, début et phrases de sécurité seulement. Les billets de forum : lus dans la réponse de la recherche, deux en partie.
- **Canaux non interrogés** : les littératures plus anciennes que j'attendais (représentations rétrocompatibles, dérive des traits en apprentissage continu) ; les dépôts de modèles ; les fils de réseaux sociaux, où vit une part de la vague ; les archives de prépublications hors d'arXiv ; toute langue autre que l'anglais. Deux des trois listes publiques ne sont pas dépouillées.
- **Refus rencontrés** : le dépôt de relectures a refusé le téléchargement des PDF (vérification humaine exigée), puis une requête de note ; je me suis arrêté là. Aucun refus d'outil ni de classifieur.
- **La réponse d'Opus** : non lue. La comparaison par noms de fichiers est descriptive ; elle ne se prête à aucune estimation propre du nombre de pièces manquées.
- **Le programme** : je ne sais ni sur quel état nos sondes sont apprises, ni combien d'épisodes honnêtes sont gardés, ni combien d'adaptateurs honnêtes existent, ni si leurs activations sont en cache.
- **Écarts, déclarés** : les sources sont versées sous mon dossier et non sous `docs/sources/pdf/` ; trois de mes scripts effacent un fichier temporaire par un chemin construit par variable, tous dans mon dossier, sur des fichiers que je venais de créer ; neuf lignes du registre des accords lues par leur rang ; j'ai listé le dossier de la note (permis) et vu ainsi les noms de fichiers du dossier d'Opus ; après le refus du site du dépôt de relectures pour six PDF (code 403), j'ai essayé une fois l'adresse des pièces jointes de sa propre interface publique, refusée de même, puis une requête de note a été refusée : je n'ai rien tenté d'autre ; le script de calcul a été corrigé deux fois avant son scellement (un format, deux libellés) ; l'empreinte de cette note a été remplacée une fois avant toute remise (heure de fin, une phrase du verdict 1). Routine de reprise : non faite, elle revient à la mère. Rien n'est commité.
- **Pour la mère** : mon dossier pèse 59 Mo (32 de sources, 27 de réponses brutes, dont seize réponses de forum d'un à deux mégaoctets chacune) ; il est sous la ligne 11 de la liste d'exclusion locale de git (vue par une commande de vérification sur mon fichier) : à lever, ou à forcer, avant de committer. Les empreintes des réponses brutes sont dans le journal et dans `journal/empreintes-brut-v1.txt`.

## Annexe : pièces

Table complète, pages et empreintes : `sources/provenance-recherche-approfondie-programmation-de-poids-v1.md`.

- **Versées ce jour, citées** (arXiv, premier auteur) : Shire, Kim, « Operating-Point Failure of Frozen Guardrail Probes Under Backbone Updates », 2611.19216v1 ; Duan, « Do Activation Monitors Survive Model Updates? », 2606.15980v2 ; Bakker, Louizos, « Relative Representations Enable Portable White-Box Monitoring Across Language Models », 2610.28366v1 ; Li, « Who Drifted: the System or the Judge? », 2606.15474v1 ; Balachandran, « Pay Only for Disagreement », 2609.17560v1 ; Usama et al., « Where Did the Update Go? », 2611.04192v1 ; Shawn, « PACE: Anytime-Valid Acceptance Tests for Self-Evolving Agents », 2606.08106v1 ; Gao, « From Probe Scores to Alarm Policies », 2610.04575v1 ; Schirmer et al., « Online Safety Monitoring for LLMs », 2607.02510v1 ; Sharma, Khattar, « A Rank-One Bypass of Fixed Linear Erasure », 2611.23880v1 ; Fan et al., « Language Models Can Rewrite Their Own Weights », 2611.21885v2 ; Aksoy, « W-ISA: Transactional Execution of Weight-Space Intervention Programs », 2611.13232v1 ; Chen et al., « Persona Vectors », 2507.21509v3 ; Liu, Yang, « Computation, not weight access », 2611.07847v2 ; Ji, « Can Weight-Space Programming Alter Learned Ethical Priorities? », 2611.24330v1. Versées, non citées dans le texte : Yin et al., 2604.12359v1 ; Lyons Keenan et al., 2609.36490v1.
- **Du dépôt, relue** : Taufeeque et al., « The Obfuscation Atlas », 2602.15515v2, p. 25.
- **Résumés seuls** (soumissions anonymes, par leur titre) : « Fighting the Drift: Probe Transfer Across Post-Training Stages » ; « Rankings Survive, Scales Drift » ; « Frozen Input-Harm Probes under Compression » ; « The base case » (par la description de Shire et Kim) ; « SAVER » ; « Statistical Rank Transport for Efficient Conformal Recalibration After Model Updates » ; « Continual Calibration » ; « Learning to Test » ; « How Much Must We Test After an Agent Update? ».
- **Billets** : le billet d'origine du 2 novembre 2026 (copie empreintée) ; « Continual learning might make your blocking monitors nearly useless » ; « Held-out Monitors Sometimes Degrade, Even When Not Trained Against » ; « An overview of frontier AI company monitoring practices in mid 2026 ».
- **Notices d'arXiv seules** : les 33 qui portent l'expression (liste dans `journal/brut/001-arxiv.xml`) et les voisines rendues par concept (réponses 006 à 010, 045, 046, 058 à 062).

---

## Décisions pour toi

Les défauts de la v2 courent depuis sa remise (16:40 UTC). Pour D-3, D-5 et D-9, je recommande que la version révisée ci-dessous prenne leur place à l'échéance.

**D-2′. Inscrire la clause d'hygiène des sondes à travers une écriture comme critère de lecture, sans toucher aucun énoncé.** Enjeu : la v2 attendait une mesure parce que rien n'était publié ; c'est publié. La clause : « toute lecture de sonde déclare l'état des poids où elle a été étalonnée ; après toute écriture, rejeu de l'ancre honnête scellée, recentrage, témoins étiquetés ; une aire sous la courbe qui tient ne prouve pas qu'un seuil ou une accumulation tient ». (a) La clause maintenant, dans les critères de lecture des textes à venir, avec ses citations ; le troisième indice du cadre formel et la règle de traversée après M1 : avantage, aucun texte ne part avec une sonde gelée lue à travers une écriture ; inconvénient, une clause de plus à vérifier. (b) Tout attendre, comme la v2 : rien d'écrit avant notre mesure ; mais le premier texte qui compare les deux familles d'organismes part sans elle. (c) Tout inscrire dès maintenant, énoncés compris : une règle écrite avant sa mesure sur nos sondes. Recommandation : (a). Confiance 0,75. Défaut sous 48 heures : (a), pour la clause seule ; le troisième indice et la loi de la référence honnête restent un nœud.

**D-3′. La mesure qui décide : le déplacement de lecture par rejeu (M1).** Enjeu : le seul nombre dont dépendent D-2′, D-10 et D-12. (a) Un agent habilité fait l'inventaire, par étiquettes, des épisodes honnêtes gardés, des états honnêtes et des sondes ; il rejoue les épisodes à travers chaque état honnête, sondes gelées, et rend niveau, échelle et rang appariés, à 0,05 écart type près si le nombre d'épisodes le permet ; sur processeur si les caches existent, sinon sur devis : avantage, ni jumeau ni saboteur, résolution dite d'avance ; inconvénient, une lecture hors politique, qui ne dit rien de la conduite. (b) La D-3 de la v2 telle quelle (deux adaptateurs honnêtes, épisodes neufs, recouvrement des poids) : plus chère, sans résolution dite. (c) Attendre le collisionneur. Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a), pour l'inventaire et le calcul sur processeur ; toute passe de modèle sur devis.

**D-5′. Les témoins plantés deviennent les témoins étiquetés de chaque état.** Enjeu : les contrôles sans étiquette ont manqué l'aveuglement ciblé d'une sonde ; seuls des témoins étiquetés tenus à l'écart l'ont vu. (a) Écrire maintenant les deux témoins par crochet, comme la D-5 de la v2, et ajouter « tenue des témoins » à la liste de ce que le sas réadmet : avantage, le côté que M1 ne voit pas est couvert ; inconvénient, deux petites pièces. (b) La D-5 de la v2 sans cet ajout. Recommandation : (a). Confiance 0,75 (0,65 dans la v2). Défaut sous 48 heures : (a), pour l'écriture ; toute passe sur devis.

**D-9′. Lecture en entier, par un agent neuf d'un autre modèle, d'une liste doublée.** Enjeu : le verdict d'antériorité sur la proposition 1.3 de la v2 et sur les trois restes de la section 3.4. Aux sept voisins de la v2 s'ajoutent : Shire et Kim ; Duan ; Bakker et Louizos ; Li ; Balachandran ; Usama et al. ; Shawn ; Fan et al. ; et les soumissions anonymes, dont les PDF demandent une personne devant un navigateur. (a) Oui, liste entière, avec les forums et le dépôt de relectures pour la recherche des trois restes : avantage, un « non trouvé » qui vaut quelque chose ; inconvénient, une lecture longue. (b) Les deux pièces pivots et les sept de la v2 seulement. Recommandation : (a). Confiance 0,8. Défaut sous 48 heures : (a).

**D-10. Retirer « troisième axe de fragmentation » de tout texte sortant, et fixer les citations.** Enjeu : revendications et citations. Le fait est publié par d'autres, la règle aussi, brique à brique. (a) Le nom reste une étiquette de travail dans les notes ; les textes sortants disent « péremption des sondes sous mise à jour » et citent au moins Duan, Shire et Kim, Bakker et Louizos, Li, Balachandran, Usama et al. ; trois phrases à ne pas écrire : « à notre connaissance, aucun travail ne mesure une sonde gelée à travers un changement de poids » ; « premier » ; « l'aire sous la courbe tient, donc la sonde se transfère » : avantage, aucune revendication exposée ; inconvénient, une idée qui se disait bien cesse de se dire. (b) Garder le nom pour la seule question adverse (l'agent qui fractionne une preuve en obtenant des écritures), à rouvrir si M1 et D-9′ le permettent. Recommandation : (a) maintenant, (b) possible plus tard sur pièces. Confiance 0,85. Nœud : pas de défaut.

**D-11. Une règle de recherche pour toute note qui écrit « non trouvé ».** Enjeu : la v2 a conclu à l'absence sur un seul moteur ; ce moteur manque encore la pièce pivot aujourd'hui. (a) Ajouter à la consigne commune de méthode, par son auteur, une rubrique : au moins l'interface d'arXiv par concept, la recherche propre des forums, le dépôt de relectures, le site de dépôts de code et un index de citations ; un objet vrai et un faux par canal ; l'ensemble retrouvé figé avant toute liste publique ; le journal versé : avantage, « non trouvé » retrouve un sens ; inconvénient, une demi-heure par note. (b) La réserver aux pièces décisives et aux verdicts d'antériorité. (c) Rien. Recommandation : (a) pour tout « non trouvé » qui porte une décision. Confiance 0,8. Défaut sous 48 heures : (a).

**D-12. Lire la prédiction de validité des organismes comme une sonde à travers une écriture.** Enjeu : périmètre du chantier des sondes ; la comparaison des deux familles d'organismes. (a) Critère de lecture à porter par qui écrira le texte : toute sonde comparée entre la famille à instruction cachée et la famille à adaptateur est rapportée gelée, recentrée sur l'ancre, et réapprise sur l'état d'arrivée ; l'adaptateur honnête de même budget sert de témoin de niveau ; et M5 (l'adaptateur saboteur lu sur des épisodes honnêtes seulement) est faite par un agent habilité aux organismes : avantage, « échoue sur la seconde famille » ne peut plus venir de l'écriture seule ; inconvénient, trois lectures au lieu d'une, et une lecture d'organisme saboteur. (b) Le critère sans M5 : aucune lecture d'organisme, mais « la sonde lit l'adaptateur » reste ouvert. (c) Rien avant M1. Recommandation : (b) maintenant, (a) après M1 si un déplacement est vu. Confiance 0,6. Défaut sous 48 heures : (b) ; M5 est un nœud, sans défaut.
