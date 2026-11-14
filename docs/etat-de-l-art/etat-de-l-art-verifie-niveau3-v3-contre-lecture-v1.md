# Contre-lecture de la synthèse de l'état de l'art vérifié de niveau 3, version 3 — v1

- **Date et heures** (relevées par `date -u`) : commencée le 2026-11-14 à 01:31:52 UTC ; fin de rédaction : 2026-11-14 à 01:34:27 UTC.
- **Contre-lecteur : sous-agent, modèle B ; auteur de la synthèse : modèle A ; A ≠ B.** J'ai écrit la contre-lecture de la v2 (`bc5909fc…`) ; je n'ai écrit ni la v3, ni aucun rapport, ni aucune décision.
- **Objet** : contrôle court et ciblé — les constats A à R de ma contre-lecture de la v2 sont-ils appliqués, et les lignes « déclarable : oui » tiennent-elles ?

**Empreintes vérifiées (recalculées, égales à l'attendu).**
- `etat-de-l-art-verifie-niveau3-v3.md` : `aab1538aaed833f2f06073dbd9ba30a12cbb8584e7d71b40535bef9bde4b918b` (« la v3 », lignes numérotées comme dans le fichier).
- `etat-de-l-art-verifie-niveau3-v3-journal.md` : `a4c4ab34e8855ecf3222d59f6b1570dc67bf872acaaa53810f97c4b11cd76234`.
- `rapport-H1-2609.19101-v1.md` : `498a34939a2d3960cc204b78a655229f36ad66e50dafa2fd1037eeb7e0eb8c82` ; `contre-lecture-rapport-H1-2609.19101-v1.md` : `724857f51ef78bc8d8a18e614c87e97c9f67d0e8e33cf8f7fb6fa82586ce7a21` (« K-H1b » et sa contre-lecture).

**Étendue réelle de ma lecture** (contrôle ciblé, non une relecture entière).
- La v3 : en-tête, prononcé, règle de la colonne (l. 1 à 80) ; dans la table datée, les lignes de H1, H2, L, T (deux lignes), des deux énoncés de N-069, de H3, H5, H7, HC1, HC2, HC3, HC6, O2, O3, O11, O12 ; la section 2 bis en entier ; la section 3, H1 ; dans la section 12, les phrases de H1, H2, T, H6, statistique de population, HC1, HC2, HC6 et la phrase d'ensemble ; le reste par recherche de mots sur les points de chaque constat (sections 2.1, 6, 7, 10.2, 10.3). **Les sections 4, 5, 8, 9 et 11 n'ont pas été relues.**
- Le journal de la v3 : la seule ligne sur HC1 (l. 38).
- K-H1b et sa contre-lecture : plans, verdicts, avis sur la colonne « déclarable », voisins ; pas les fiches de chiffres.
- Rapports et contre-lectures du compte 2 : ce que j'en avais lu pour la v2, sans relecture.
- Aucun PDF ouvert. L'archive de la v3 n'a pas été ouverte : je n'ai pas recontrôlé ses extraits sur PDF.

Aucune commande git, aucun réseau, aucun appel de modèle, aucune suppression ; rien sous `registres/`, `diag/`, `runs/`, `donnees/`, rien de T0.7, de 7a ni de 7b. Aucun refus de permission, de crochet ou de classifieur ; aucune ouverture fautive. Mes 13 citations de fichiers sont contrôlées par programme : 13 justes, 0 échec.

---

## 0. Verdict

**Utilisable après corrections.** Les dix-huit constats A à R sont appliqués, et la règle réécrite est meilleure que celle que je proposais. Mais cette règle, appliquée avec la même rigueur qu'à H2 et à l'énoncé 2 de N-069, **retire deux des six « oui »** : HC1 et l'énoncé 1 de N-069. Corrections nécessaires : les constats S et T (deux lignes de la table, le point 7 du prononcé, deux mentions de la section 12).

**Lignes « déclarable : oui » : mon partage.**

| ligne | v3 | mon avis | motif |
|---|---|---|---|
| H3 | oui | **oui** | statué par la contre-lecture de la v1 ; aucune désignation « à lire d'abord » connue de moi ; exposition et pièces nommées |
| H5 | oui | **oui** | idem ; les deux pièces lues pour un autre énoncé sont nommées |
| H7 | oui | **oui** | idem ; exposition faible |
| T, composantes (c) à (f) | oui | **oui** | le premier groupe de la liste ordonnée de K-T ne vise que (a) et (b) ; Koning cité ; voisins de rang inférieur nommés |
| HC1 | oui | **non** | constat S |
| Statistique de population, énoncé 1 de N-069 | oui | **non** | constat T |

Je n'ai pas lu les rapports du niveau 3 (hors de ma liste) : pour H3, H5 et H7, je ne peux pas exclure qu'un de leurs lecteurs désigne une pièce « à lire d'abord » ; la v3 ne le vérifie pas non plus, et sa condition 4 nomme pourtant les lecteurs du niveau 3. Réserve, non constat.

---

## 1. Application des constats A à R

« Appliqué » : fait au bon endroit, vérifié dans le texte de la v3. « Appliqué autrement » : fait d'une autre manière que le texte proposé, acceptable.

| constat | état | où je l'ai vérifié dans la v3 | remarque |
|---|---|---|---|
| A — H1 déclarable sans confrontation de 2609.19101 | appliqué | l. 85 (table), l. 221-235 (section 3), l. 547 (section 10.2), phrase de H1 en section 12 | 2609.19101 confrontée par un rapport contre-lu ; H1 passe à « non » ; voir le point 4 ci-dessous |
| B — T déclarable pour (a) et (b) | appliqué | deux lignes de T dans la table ; phrase de T | « oui » pour (c) à (f) seulement ; la phrase retire (a) et (b) de ce qui est revendiqué |
| C — HC6 déclarable | appliqué | ligne HC6 ; l. 35 ; phrase de HC6 | « non », par les conditions 2 et 4 ; Khan et collègues nommé |
| D — HC2 déclarable hors de la règle | appliqué | ligne HC2 ; point 7 du prononcé ; phrase de HC2 | « non statué », renvoi exprès à N-068, sections 4, 6 et 8 |
| E — règle de la colonne, critère de mots | appliqué autrement | règle, l. 68-79 | cinq conditions qui jugent la fonction d'une désignation ; deux écarts à mon texte, acceptables (point 2 ci-dessous) ; son application à HC1 et à l'énoncé 1 est le défaut (S, T) |
| F — versions 3 et 5 de NARCBench | appliqué | l. 37, 86, 101, 495, 548, 590 | les formules fausses de la v2 ne figurent plus (recherche de mots) |
| G — phrase de H2 | appliqué | phrase de H2 | texte proposé repris ; H2 dit non déclarable |
| H — N-067 rapportée avec erreurs | appliqué | lignes O2, O3, O11, O12 ; l. 470 ; l. 485 | O11, O3, 2611.00643, clause de O2, forme de O12 : conformes à N-067 |
| I — voisins du lot 4-B | appliqué | ligne HC1, HC2, HC3 ; l. 599 | rattachés au papier C ; leur effet sur la ligne HC1 est sous-pesé (S) |
| J — phrases de T, H6, HC1, HC6 | appliqué | section 12 | textes proposés repris |
| K — H2 : nommer les voisins | appliqué autrement | ligne H2 ; point 7 | plus durement : H2 passe à « non » ; acceptable et cohérent avec T |
| L — pièces lues pour un autre énoncé | appliqué | colonne ajoutée en 10.2 (l. 545) ; lignes H2, H3, H5 | — |
| M — titre de la section 10.3 | appliqué | l. 584, l. 597 | — |
| N — compte par lot | appliqué | section 2 bis, ligne N ; section 10.2 | vérifié par la seule ligne de suite donnée et par recherche de mots, non recompté |
| O — extrait contrôlé contre un autre PDF | appliqué | l. 594 ; règle de lecture, l. 27 | nom d'atelier paraphrasé ; je n'ai pas rouvert le JSON de la v3 |
| P — M4 pour L et pour T | appliqué autrement | l. 167 | une seule décision « réserve maintenue », motif distinguant T (levé) et L : acceptable |
| Q — « non-compensation » | appliqué | l. 87, l. 261 | — |
| R — point 7 du prononcé | appliqué | l. 39-44 | à réaligner de nouveau après S et T |

---

## 2. Réponses aux quatre points

**1. Les six « oui ».** Quatre tiennent (H3, H5, H7, T pour (c) à (f)) ; deux ne tiennent pas sous la règle de la v3 elle-même (HC1 : constat S ; énoncé 1 de N-069 : constat T).

**2. La règle réécrite et ses deux écarts.** Acceptables tous les deux.
- *Pièces de la section 5 de la contre-lecture de la v1 comme exposition à nommer, non comme empêchement.* L'auteur a raison : ma condition (v) aurait retiré H3, H5 et H7, que la contre-lecture de la v1 tenait pour déclarables en connaissant ces pièces non lues, et elle demandait seulement que l'exposition soit dite. La v3 la dit, pièce par pièce.
- *H2 et énoncé 2 de N-069 en « non ».* Plus dur que mon avis, et plus cohérent : un voisin que le lecteur veut lire en premier contre une composante déclarée empêche, quel que soit le mot. Je m'y range. Mais la cohérence joue alors dans les deux sens (S, T).

**3. Constats A à R.** Tous appliqués ; trois autrement, de façon acceptable (E, K, P). Table ci-dessus.

**4. La ligne H1 et la phrase fausse de la v2.** La phrase est corrigée : la v3 écrit « aucune des trois ne compare sondes et moniteur de texte » pour les seules pièces de K-H1, puis présente 2609.19101 à part. La ligne H1 est fidèle à K-H1b et à sa contre-lecture : « occupé en partie » sur la partie déjà cédée, signe mixte, réserve sur la vérité terrain, et « non » — la contre-lecture de K-H1b écrit « Mon avis sur la colonne « déclarable » de H1 : non, pour l'instant. », avec trois lectures avant le passage à « oui », que la ligne nomme. Rien à reprendre. Je n'ai pas recoupé les chiffres de la figure 8.

---

## 3. Constats nouveaux

| constat | gravité | endroit dans la v3 | preuve | texte corrigé proposé |
|---|---|---|---|---|
| S — HC1 « oui » ne tient pas sous la condition 4 de la règle | bloquant | ligne HC1 de la table (section 1) ; point 7 du prononcé, l. 40 ; phrase de HC1, section 12 ; journal, l. 38 | (i) La composante déclarée de HC1 comprend « par régression sur plusieurs intensités » : un gain continu d'un juge selon l'intensité de l'attaque. `rapport-4B-partie1-v2.md`, section 6, dernier interdit : « Rien sur le gain continu de la corruptibilité d'un juge appris tant que Gao, Schulman et Hilton n'est pas lu sur PDF » ; section 7 : cette pièce « touche (d) et l'idée même du papier C ». C'est une désignation qui précède toute phrase, contre une composante déclarée — non une « remarque de portée sans rang », comme l'écrit le journal. La règle dit : « Une désignation qui vise l'énoncé entier, ou qui précède toute phrase publique, vaut pour toutes ses composantes ». (ii) La v3 écrit que les trois voisins de K-HC1 sont « désignés en priorité par K-HC1 contre le phénomène (cédé) ». K-HC1 ne le dit que pour un des trois (« à lire en priorité : juges sous biais, cœur du phénomène de HC1 ») ; pour les deux autres, sa colonne « intérêt pour HC1 » dit « à lire en priorité : lecture interne de la flagornerie » et « à lire en priorité : autorité dans un cadre d'évaluation » — le second est un évaluateur sous pression d'autorité, c'est-à-dire l'objet même de la pièce déclarée. (iii) K-HC1 rattache cette liste à la pièce revendiquée : « Ce n'est pas un trou du champ (R8) : l'exposition nommée par M7 n'est pas lue (section 6) » ; sa contre-lecture de même : « l'exposition nommée par M7 et les voisins du § 6 du rapport ne sont pas lus ». H2 est rangée « non » pour deux voisins « à lire en premier » dont un seul vise une condition de la conjonction : HC1, avec quatre désignations, ne peut pas être traité plus doucement. | Colonne « déclarable » de HC1 : « **non** en l'état (condition 4) : Gao, Schulman et Hilton, 2210.10760 (gain continu contre un juge appris ; K-4B1 : rien à en dire avant lecture sur PDF), Choi et collègues, 2601.04790 (autorité dans un cadre d'évaluation), Wang, Li, Yang, Zhang et Wang (AAAI 2026) et Wang Q. et collègues, 2504.09946, désignés « à lire en priorité » par K-HC1, ne sont pas lus ; oui sous les mentions, avec l'exposition de M7 nommée, dès qu'ils le sont sans occupation de la destination libre ni de la régression par intensité. » Réserves : remplacer « contre le phénomène (cédé) » par « en priorité, pour HC1 (un seul des trois est dit par K-HC1 viser le phénomène) ». Phrase de HC1, en tête : « HC1 n'est pas déclarable en l'état (quatre voisins à lire). » |
| T — Énoncé 1 de N-069 « oui » alors que la désignation de sa contre-lecture n'est pas restreinte à l'énoncé 2 | bloquant | ligne « Statistique de population, A_pop » ; point 7 du prononcé ; phrase « Statistique de population », section 12 | La v3 retire l'énoncé 2 parce que K-B désigne Bonjour, Aggarwal et Bhargava 2022 « pour la composante « statistique conjointe » de l'énoncé 2 ». Mais la condition 4 compte aussi les contre-lecteurs (« aucune pièce non lue n'est désignée, par un lecteur ou un contre-lecteur »), et `contre-lecture-rapport-papierB-v1.md`, section 4, écrit sans restriction : « Bonjour et collègues 2022 : à lire en priorité, parce que c'est une statistique conjointe entre agents, en boîte noire, antérieure aux agents à modèle de langage ». La co-élévation de l'énoncé 1 est elle-même une statistique conjointe entre agents. La ligne de l'énoncé 1 ne nomme même pas cette pièce. La phrase de la section 12 parle en outre des deux énoncés à la fois. Je ne dis pas que cette pièce, en boîte noire, peut occuper un énoncé sur scores de sondes ; je dis que le même argument vaudrait pour l'énoncé 2, et que la v3 ne peut pas le tenir pour l'un sans le tenir pour l'autre. | Colonne « déclarable » de l'énoncé 1 : « **non** en l'état (condition 4) : Bonjour, Aggarwal et Bhargava 2022, « à lire en priorité » selon la contre-lecture de K-B comme statistique conjointe entre agents, sans restriction à l'énoncé 2, n'est pas lu ; oui sous les mentions, avec l'exposition et les voisins nommés, dès qu'il l'est sans occupation. » Phrase de la section 12 : « non déclarable en l'état pour les deux énoncés (un voisin de priorité haute à lire) ». Une seule lecture lève à la fois les deux lignes. |
| U — Point 7 du prononcé à réaligner | mineur | section 0, l. 40-43 | Conséquence de S et T. | « **oui** […] : H3, H5 (la loi), H7, T pour ses composantes (c) à (f) » ; ajouter HC1 et l'énoncé 1 de N-069 à la liste des « non », chacun avec ce qui le lèverait. |
| V — Condition 4 : les désignations des lecteurs du niveau 3 ne sont pas vérifiées pour H3, H5, H7 | mineur | règle, condition 4 ; lignes H3, H5, H7 | La condition nomme les lecteurs du niveau 3 ; la v3 ne dit pas avoir cherché, dans la v1 ou sa contre-lecture, une désignation « à lire d'abord » contre ces trois énoncés. | Ajouter à chaque ligne : « aucune désignation « à lire d'abord » relevée dans la v1 ni dans sa contre-lecture (rapports du niveau 3 non rouverts) », ou la pièce s'il y en a une. |

---

## 4. Conditions

La v3 devient utilisable pour l'horodatage dès que S et T sont corrigés (U en découle ; V est une précision). Resteraient alors déclarables : **H3, H5, H7 et T pour (c) à (f)**. HC1 et l'énoncé 1 de N-069 se lèvent par des lectures courtes et nommées : quatre pièces pour HC1, une pour le papier B.

Réserve sur ma propre lecture (R4) : contrôle ciblé, non relecture ; les sections 4, 5, 8, 9 et 11 de la v3 n'ont pas été relues et peuvent porter un défaut que je n'ai pas vu.

Version 1 ; ne sera jamais réécrite (R12). Fichiers de travail : `fichiers-de-travail-contre-lecture-synthese-niveau3-v3.tar`.
