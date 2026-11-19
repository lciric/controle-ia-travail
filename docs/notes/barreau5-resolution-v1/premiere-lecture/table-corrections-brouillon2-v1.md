# Table des corrections du brouillon 2 — texte neuf « validité de l'adaptateur pour les sondes apprises sur la tâche » et son devis — v1

Écrite le 19 novembre 2026 par le rédacteur du brouillon 2 (sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`, Claude Fable 5.2), sous le mandat `docs/notes/barreau5-resolution-v1/premiere-lecture/mandat-redacteur-corrections-brouillon2-v1.md` (`217ea246d7ab30275cd1fd9c6e3ed1eee2f5194219dea4ffd6a55fdfba3e1545`). Pièce de travail, pour le vérificateur (agent neuf, Claude Opus 5.5). Rien lancé sur carte, rien dépensé, rien commis ; aucun score ouvert ; aucun refus d'outil.

## Verdict en trois lignes

- Les 29 remarques de la contre-lecture (3 bloquantes, 10 majeures, 16 mineures) portent 44 couples « avant, après » : 41 dans le texte, 3 dans le devis. **Les 44 sont appliqués à la lettre, par programme.** Aucun n'est écarté.
- Aucune remarque ne demandait une rédaction libre. Ce que j'ai écrit moi-même est sous « hors correction » : 9 changements d'en-tête et d'état (texte), 5 (devis), et **8 changements qu'une correction rend nécessaires** (6 dans le texte, 2 dans le devis), tous marqués « à trancher par le vérificateur ».
- Une correction est jugée fausse sur un point : M4.1 (miroir exact de la tendance entre M+ et M−). Elle est appliquée à la lettre, suivie d'une phrase qui la borne (HT12). Onze points relevés ne sont pas changés (dernière section).

## Pièces (chemin, empreinte)

| pièce | sha256 |
|---|---|
| brouillon 1 du texte, `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md` | `c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43` |
| **brouillon 2 du texte**, `prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md` | `b346d5bd432a798cafd454d2dbec8fda52c98a43ef6108877d0ea04f5947d5d1` |
| brouillon 1 du devis, `docs/notes/barreau5-resolution-v1/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon1.md` | `d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d` |
| **brouillon 2 du devis**, `…/premiere-lecture/devis-relecture-meme-chemin-v1-brouillon2.md` | `35eb699660fed749870505fdd660ca6d94d3ad739edcc81b9034a2311943fb90` |
| contre-lecture, `…/premiere-lecture/contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md` | `13bde37898a0…` (compagnon `.sha256`, vérifié « OK ») |
| outil des remarques de la contre-lecture, `…/contre-lecture-outils-v1/remarques-contre-lecture-v1.py` | `a37fc7da85d25ade2792038d7c5f14e6b92553f9f3c1fc1c69a63ea8a9855dca` |
| outil d'application, `…/premiere-lecture/outils-brouillon2-v1/appliquer-corrections-brouillon2-v1.py` | `2a88a1baf2650fe462abad2093adc7a2001fb27f44a30133fd9d26f951876d71` |
| son relevé, `…/outils-brouillon2-v1/releve-application-brouillon2-v1.json` | `f411272df5d7548296c79aae54cde2c936e40a39d92135d71d650ade09468f02` |
| nœuds pour Lazar, `…/premiere-lecture/noeuds-restants-v2.md` | `8778c2138a1c0c2646ab60007e7f26934ded791611b51bf0e17ee6ae52134f82` |

## Comment vérifier sans rien deviner

1. **L'application à la lettre.** L'outil d'application ne recopie aucun texte de correction : il charge la liste des couples dans l'outil scellé de la contre-lecture (empreinte contrôlée), exige que chaque « avant » paraisse une seule fois, remplace, puis contrôle que chaque « après » est entier dans le brouillon 2 et que l'« avant » n'y est plus. Relevé : 44 corrections, `apres_tous_presents` vrai, `avant_tous_partis` vrai.
2. **Rejouer à blanc** (n'écrit que le relevé donné) : `cd /home/user/controle-ia-travail && python3 -B docs/notes/barreau5-resolution-v1/premiere-lecture/outils-brouillon2-v1/appliquer-corrections-brouillon2-v1.py . /tmp/releve.json --a-blanc`. Les deux empreintes affichées doivent être celles du tableau ci-dessus.
3. **La différence entre les brouillons** : `git diff --no-index --word-diff prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md` ; de même pour le devis. Tout ce qui diffère est soit un « après » de la contre-lecture, soit un changement HT ou HD de cette table ; les textes exacts des changements HT et HD sont dans l'outil d'application (listes `HORS_TEXTE` et `HORS_DEVIS`).
4. Les numéros de ligne ci-dessous sont ceux des brouillons 2.

## Une ligne par correction

Mode : « à la lettre » = le couple exact de la contre-lecture, appliqué tel quel.

| repère | classe | objet | mode | où, dans le brouillon 2 |
|---|---|---|---|---|
| B1.1 | bloquante | phrase gelée « contraire », première lecture | appliquée à la lettre | texte, l. 291, « Ce que dira chaque issue au jury », table de l'interaction |
| B1.2 | bloquante | « Réfutation » : ce que dit une interaction contraire | appliquée à la lettre | texte, l. 116, « Prédiction chiffrée et signe attendu » |
| B2.1 | bloquante | grille D : dose non relue, relecture non jouée, accordée ou réduite après l'ouverture | appliquée à la lettre | texte, l. 262, « Critères de lecture gelés », D |
| B2.2 | bloquante | choix de la phrase du dossier borné par l'issue finale de la grille D | appliquée à la lettre | texte, l. 276, « Ce que dira chaque issue au jury » |
| B2.3 | bloquante | l'état final est fixé par la grille D seule | appliquée à la lettre | texte, l. 184, « Seuil », règle de famille |
| B2.4 | bloquante | devis : « non relue (coupure) » | appliquée à la lettre | devis, l. 87, « Coupure, garde de projection, ordre de sacrifice » |
| B3.1 | bloquante | phrase « au niveau du texte seul », première lecture | appliquée à la lettre | texte, l. 289, « Ce que dira chaque issue au jury » |
| B3.2 | bloquante | phrase « au niveau du texte seul », deux lectures | appliquée à la lettre | texte, l. 289, même ligne de table |
| M1.1 | majeure | bande de la prévision élargie ; l'étiquette n'entre dans aucune phrase | appliquée à la lettre | texte, l. 140, « Métrique », point 3 |
| M2.1 | majeure | tendance jugée de même dans les deux sens, avec test par changement de signe | appliquée à la lettre | texte, l. 179, « Seuil » |
| M2.2 | majeure | plancher de l'honnête ; test par changement de signe de la tendance | appliquée à la lettre | texte, l. 148 et 149, « Métrique », point 4 |
| M2.3 | majeure | clé de graine `vsat/signes-tau/…` | appliquée à la lettre | texte, l. 195, « Plan d'analyse », point 7 |
| M3.1 | majeure | paires à coût égal retirées du tau | appliquée à la lettre | texte, l. 146, « Métrique », point 4 |
| M3.2 | majeure | monde PX, « ex aequo » | appliquée à la lettre | texte, l. 230 et 231, table des mondes |
| M3.3 | majeure | règle E1 étendue à PX | appliquée à la lettre | texte, l. 237, « Épreuve », E1 |
| M4.1 | majeure | règle E2 : miroir exact à la place de l'écart de 0,05 | appliquée à la lettre ; **jugée fausse sur un point**, bornée par la phrase HT12 qui la suit, à trancher par le vérificateur | texte, l. 238, « Épreuve », E2 |
| M5.1 | majeure | phrase « positive », première lecture | appliquée à la lettre | texte, l. 290, « Ce que dira chaque issue au jury » |
| M5.2 | majeure | phrase « positive », deux lectures : rappel de la ligne scellée | appliquée à la lettre | texte, l. 290, même ligne de table |
| M5.3 | majeure | phrase d'ensemble « interaction positive à adaptateur fixé… » | appliquée à la lettre | texte, l. 260, « Critères de lecture gelés », C |
| M6.1 | majeure | 0,9675 cité avec les lecteurs du seul texte (phrase d'ensemble) | appliquée à la lettre | texte, l. 304, « Ce que dira chaque issue au jury » |
| M6.2 | majeure | de même, section E, point 3 | appliquée à la lettre | texte, l. 267, « Critères de lecture gelés », E |
| M7.1 | majeure | devis : garde de projection par série | appliquée à la lettre | devis, l. 80 |
| M7.2 | majeure | devis : pire cas du bloc A s'il porte toute la notation | appliquée à la lettre | devis, l. 79 |
| M8.1 | majeure | garde d'identité des sondes relues | appliquée à la lettre | texte, l. 165, « Métrique », point 7 |
| M9.1 | majeure | motifs de l'exclusion de la sonde de l'organisme à consigne cachée | appliquée à la lettre | texte, l. 43, « 0. Objet, portée, frontière » |
| M10.1 | majeure | référence nulle de la tendance, distincte | appliquée à la lettre | texte, l. 91, « Hypothèse » |
| m1.1 | mineure | ordre des états de ligne de l'interaction | appliquée à la lettre | texte, l. 178, « Seuil » |
| m2.1 | mineure | dérivation des graines par clé | appliquée à la lettre | texte, l. 195, « Plan d'analyse », point 7 |
| m2.2 | mineure | le second programme régénère les tirages | appliquée à la lettre | texte, l. 241, « Épreuve », E5 |
| m3.1 | mineure | jumelle, niveau du contraste | appliquée à la lettre | texte, l. 181, « Seuil » |
| m3.2 | mineure | jumelle, tendance à la seconde lecture | appliquée à la lettre | texte, l. 180, « Seuil » |
| m4.1 | mineure | « au moins aussi grande » : estimation ponctuelle | appliquée à la lettre | texte, l. 179, « Seuil » |
| m5.1 | mineure | fausses lectures au pire taux simulé | appliquée à la lettre | texte, l. 335, « Puissance » |
| m6.1 | mineure | plus petite interaction détectable sous bruit asymétrique | appliquée à la lettre | texte, l. 331, « Puissance » |
| m7.1 | mineure | déclencheur (iii) de l'audit de symétrie | appliquée à la lettre | texte, l. 185, « Seuil » |
| m8.1 | mineure | phrase T+ : l'état diffère entre les deux termes | appliquée à la lettre | texte, l. 299, « Ce que dira chaque issue au jury » |
| m9.1 | mineure | phrase « rien de fait » | appliquée à la lettre | texte, l. 282, « Ce que dira chaque issue au jury » |
| m10.1 | mineure | exposition : deux lignes de table ajoutées | appliquée à la lettre | texte, l. 81 à 83, « Ce que les auteurs savaient » |
| m11.1 | mineure | épreuve : mode « seconde lecture », effectifs | appliquée à la lettre | texte, l. 234, « Épreuve » |
| m12.1 | mineure | calendrier : durée de l'épreuve | appliquée à la lettre | texte, l. 385, « Calendrier (UTC) » |
| m13.1 | mineure | extraction des poids des jumelles | appliquée à la lettre | texte, l. 197, « Plan d'analyse », point 9 |
| m14.1 | mineure | interaction ajustée sur un tirage | appliquée à la lettre | texte, l. 141, « Métrique », point 3 |
| m15.1 | mineure | intervalle de l'interaction réduite par état | appliquée à la lettre | texte, l. 142, « Métrique », point 3 |
| m16.1 | mineure | liste d'arrêt : second programme absent | appliquée à la lettre | texte, l. 314, « Liste d'arrêt » |

**Contrôle des nombres insérés par M6, M9 et m10.** Ils viennent de la note 02 du socle (`docs/notes/barreau5-resolution-v1/comprendre/02-etape-b-bis.md`, `93987ca3…`, citée en en-tête du texte). Je les ai cherchés un par un par filtre : tous y sont (0,9808 et 0,9790, l. 290 et 419 ; 0,9809, l. 118 et 296 ; 0,6233 à 0,9074, l. 117 ; bornes basses positives aux doses 0,25 et 1, l. 213 et 216 ; planchers, l. 245 ; aires par pli du texte égal, l. 399). Les nombres de M1.1, m5.1, m6.1 et M7.2 sont ceux des sorties scellées de la contre-lecture ; ceux de M1.1 et de M7.2 ont été relus dans `sortie-arithmetique-contre-lecture-v1.json` (blocs A, A2 et D) : égaux. Je n'ai pas rejoué la simulation de la contre-lecture (m6.1, ≈ 0,39).

## Hors correction

### a. En-tête et état (rien de conçu)

| repère | où | changement | raison |
|---|---|---|---|
| HT1 | texte, l. 1 | titre : « brouillon 2 » | nom neuf (R12) |
| HT2 | texte, l. 3 | une phrase : qui applique les corrections ; les « je » restent ceux du rédacteur du brouillon 1 | dire qui a écrit quoi |
| HT3 | texte, l. 4 | date du brouillon 2 | gabarit |
| HT4 | texte, l. 5 | mandat écrit du brouillon 2, chemin et empreinte | R6 |
| HT5 | texte, l. 6 | statut : contre-lu, corrections appliquées, vérification à faire | état réel |
| HT6 | texte, l. 16 et 17 | le devis cité devient son brouillon 2 (empreinte) ; la contre-lecture et ses deux sorties citées reçoivent chemin et empreinte | R6 : M1.1 et m6.1 citent ces sorties par leur seul nom |
| HT7 | texte, l. 55 | paragraphe « Rédacteur du brouillon 2 » : ce que j'ai lu et pas ouvert | exposition déclarée (R1) |
| HT8 | texte, l. 389, « Contre-lecture » | état réel de la contre-lecture ; écart déclaré (vérificateur neuf) ; le marqueur `<<CONTRE_LECTURE_1>>` reste, pour la session mère | la section disait « non contre-lu » |
| HT9 | texte, l. 378, « Calendrier » | « vérification par le même contre-lecteur » devient « par un agent neuf du même modèle (écart déclaré) » | état réel |
| HD1 à HD5 | devis, l. 1 à 6 | titre, auteur et date, statut, texte servi (brouillon 2), source des nombres de M7 (sortie de l'arithmétique de la contre-lecture, bloc D ; l'outil du devis n'est pas refait) | noms neufs, état réel, R6 |

Heure : les en-têtes des deux brouillons 2 disent « de 15:25 à 15:55 environ » ; l'écriture a fini plus tôt, vers 15:40 (`date -u` : 15:33:48Z au scellement des nœuds). Les cinq marqueurs du brouillon 1 restent, inchangés : ils reviennent à la session mère. Le validateur `controle_ia.prereg` rend sur le brouillon 2 les deux mêmes refus que sur le brouillon 1 (marqueurs ; entrée de contre-lecture au format).

### b. Changements qu'une correction rend nécessaires — écrits par le rédacteur, **à trancher par le vérificateur**

Chacun est une phrase ajoutée à côté d'un « après », jamais dedans : les « après » de la contre-lecture restent entiers.

| repère | où | ce qui est ajouté ou changé | pourquoi la correction l'exige |
|---|---|---|---|
| HT10 | texte, l. 278, « Ce que dira chaque issue au jury », paragraphe neuf « Deux crochets, leur source et leur place » | (1) le crochet « [état scellé à d ; différence [bas ; haut]] » est rempli par quatre constantes recopiées de la table « Aires déjà lues » du texte (doses 0,25 à 0,75 : non établie ; dose 1 : contraire ; différences et bornes de la ligne à 99 %) ; (2) la marque de la grille D s'écrit à la fin de la phrase « première lecture seule », entre crochets | B1.1, M5.1 et M5.2 créent ce crochet ; B2.1 dit que la marque « entre dans la phrase ». Le code n'a pas le droit d'ouvrir `lecture-bbis.json`, et la règle E5 exige des phrases identiques entre deux programmes : il faut une source et une place écrites. **À vérifier** : l'état par dose (« non établie » aux doses 0,25 à 0,75) est ma lecture de la dernière cellule de la table (« non établie ; contraire à la dose 1 ») et des intervalles, qui contiennent zéro ; je n'ai pas ouvert le verdict |
| HT11 | texte, l. 146, « Métrique », point 4 | une tâche dont P_t est nul dans un groupe est exclue et comptée, y compris pour le test par changement de signe | M3.1 retire les paires à coût égal de P_t ; M2.2 divise par P_t dans toute tâche à deux actions utiles : division par zéro possible quand tous les coûts d'une tâche sont égaux (monde PX : coûts de l'honnête arrondis) |
| HT12 | texte, l. 238, « Épreuve », E2 | l'état miroir de la tendance n'est exigé qu'entre MA et MA− ; celui de l'interaction, dans les deux paires | **M4.1 jugée fausse sur ce point.** Entre M+ et M−, le miroir change le signe des scores. Δτ et T_τ changent bien de signe, mais la condition de plancher non : « au-dessus » exige τ_S − Q_τ > 0 (quantile 0,95 des tau des directions, groupe du saboteur) ; après changement de signe, « contraire » exige (−τ_H) − (−quantile 0,05 des tau des directions de l'honnête) > 0, autre groupe et autre quantile. Un code juste pourrait donc ne pas rendre l'état miroir dans un jeu de M+ où la tendance sort par hasard de zéro, et l'épreuve s'arrêterait à tort (« 100 % des jeux »). Entre MA et MA−, les groupes sont échangés, plancher compris : le miroir est exact pour la tendance et, les quatre cases étant échangées, pour l'interaction. Autre rédaction possible : retirer « et pour la tendance » pour la paire M+, M− |
| HT13 | texte, l. 341, « Fautes trouvées », point 1 | l'accord de la jumelle se juge « sur le signe de son propre intervalle et sur son test par changement de signe, sans plancher (section « Seuil ») » | M2.1 et m3.2 changent la règle dans « Seuil » ; ce point la redisait dans son ancienne forme (même défaut que m1 : deux sections, deux règles) |
| HT14 | texte, l. 184, « Seuil », règle de famille | niveau corrigé de famille : « pour l'interaction et pour la tendance, valeur p du changement de signe sous 0,00625 » | M2.1 donne une valeur p à la tendance ; sans ce mot, deux programmes peuvent juger différemment la qualification « tient au niveau corrigé » (E5) |
| HT15 | texte, l. 38, « 0. Objet » | « La seconde lecture fait foi pour tout ce qu'elle recalcule, dans les cas que fixe la grille D des critères de lecture, et sous ses marques. » | B2.1 : une relecture accordée ou réduite après l'ouverture ne remplace rien ; B2.3 a fait le même renvoi dans « Seuil » ; la section 0 gardait la règle sans condition |
| HD6 | devis, l. 10, « En une ligne » | le pire cas ne garde les quatre doses (≈ 8,0 USD) que si 70 % de la notation revient au bloc A ; s'il la porte toute (≈ 8,4 USD), la garde par série sacrifie la dose 0,75, puis la 0,25 | M7.2 : la phrase d'ouverture du devis disait le contraire, sans condition |
| HD7 | devis, l. 74, « Montants » | « ≈ 8,4 (4,96 heures) s'il la porte toute » ajouté au pire cas du bloc A | M7.2 ; nombres de la sortie de l'arithmétique de la contre-lecture, bloc D (8,42 ; 4,96) |

## Corrections non appliquées

Aucune.

## Relevé, non changé — au vérificateur de dire s'il faut un couple de plus

1. **Symétrie de la phrase d'ensemble (R4).** M5.3 ajoute à la phrase des doses positives « (au niveau corrigé de famille : [tenue aux doses .. | non tenue]) » ; la phrase miroir « interaction contraire aux doses [D−] » (texte, l. 260) ne la reçoit pas. Couple possible : « interaction contraire aux doses [D−] » → « interaction contraire aux doses [D−] (au niveau corrigé de famille : [tenue aux doses .. | non tenue]) ».
2. **Garde d'identité (M8) hors de « Métrique ».** La contre-lecture dit (question 9) qu'elle manque à la liste d'arrêt, mais ne donne que M8.1. Elle n'est ni dans « 8. Non calculable » (l. 172), ni dans la liste d'arrêt (ligne « Relecture : … », l. 317), ni dans les épreuves du « Code neuf ». Le texte de M8.1 se suffit (« non calculable (identité) », « éprouvée sur un cas sain et sur un artefact ») ; je n'ai rien ajouté.
3. **Phrase T−.** Depuis M2.1, « contraire » exige que le tau de l'honnête dépasse son plancher ; la phrase T+ cite le tau du saboteur et son plancher, la phrase T− (l. 301) ne cite ni le tau de l'honnête ni le sien.
4. **Puissance de la tendance.** La section « Puissance » (l. 333) ne chiffre que l'intervalle seul et la condition de plancher du saboteur. La règle à trois conditions de M2.1, dans les deux sens, n'y est pas simulée par le rédacteur ; m5.1 en tient compte pour la famille seulement. L'épreuve (E1 : mondes M0, MN, PX) la mesure avant toute ouverture.
5. **Nom de l'issue « au niveau du texte seul ».** B3 retire l'équivalence des deux phrases ; le nom reste dans la grille A (ligne KT), dans la table des mondes (M0T) et dans « Quand toutes les doses sont non établies, au niveau du texte seul ou contraires ». Un nom d'issue n'est pas une phrase au jury ; laissé.
6. **Table « Prédiction chiffrée » et « Puissance ».** Elles gardent les deux voies de la prévision sans la bande élargie de M1.1, qui ne change que « Métrique », point 3.
7. **m11.1, mode « seconde lecture » de l'épreuve.** Le texte ne dit pas comment un monde fournit les fichiers relus ni quelle marque exacte est attendue pour la coupure simulée (« non relue (coupure) », d'après B2.1). Laissé au tireur, sous la règle E5 (addendum si ambiguïté).
8. **« Hypothèse », puce suivante.** « Les deux écarts à cette référence » reste au singulier alors que M10.1 sépare deux références nulles.
9. **Plan, point 3, et liste d'arrêt.** Ils disent qu'une relecture accordée après la première lecture est « écrite en réserve par le second verdict » ; B2.1 dit en plus que toutes les issues restent alors celles de la première lecture. Compatible, non redit. C'est en revanche un fait à porter à Lazar (nœuds v2, point 3).
10. **Devis, M7.1.** La phrase corrigée finit par « les scores des blocs faits sont scellés et poussés » : il faudrait lire « des séries faites ». Laissé à la lettre.
11. **Devis, M7.2.** « ce qui est le cas attendu » qualifie le fait que le bloc A porte toute la notation, non le pire cas de prix et de débit. Laissé à la lettre ; HD6 reprend les mêmes mots.

## Devis et nœuds

- **Devis** : brouillon 2 écrit (3 corrections à la lettre, HD1 à HD7). Aucun montant du brouillon 1 ne change ; s'ajoutent le pire cas du bloc A quand il porte toute la notation (≈ 8,42 USD, 0,29 au-delà de la coupure moins un quart d'heure) et la garde de projection par série.
- **Nœuds pour Lazar** : `noeuds-restants-v2.md` écrit. Le nœud de la dépense change (accord à donner avant l'ouverture des scores, sinon la seconde lecture ne remplace rien ; au pire cas, deux doses du bloc A sacrifiées sous la coupure de 8,5 USD) ; deux points d'information s'ajoutent (choix de la phrase du dossier borné dose par dose ; date de la première lecture non garantie tant que la durée de l'épreuve n'est pas mesurée).
