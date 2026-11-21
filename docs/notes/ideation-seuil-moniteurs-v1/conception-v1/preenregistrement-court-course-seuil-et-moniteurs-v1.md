# Préenregistrement court — course de l'organisme d'idéation « seuil et moniteurs », une génération et un étage de tests de mort — v1

- Auteur : rédacteur de la conception de la course seuil et moniteurs, modèle F.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 06:43:41Z, après la lecture des pièces et avant l'écriture.
- Statut : **brouillon, non contre-lu, non scellé.** Il ne peut pas être scellé en l'état : la section « Ce qui reste à écrire avant le scellement » liste ce qui lui manque. Aucune réponse d'aucun modèle n'est lue avant le scellement (règles R1 et R3).
- Commit du code d'analyse : **aucun à cette date.** Le programme de mesure, le comparateur, le tirage des cases et celui des candidates font partie de ce qui reste à écrire ; leur commit et leurs empreintes entrent au complément de valeurs, avant tout allumage.
- Documents qui font foi (chemin et empreinte) :

| pièce | chemin | empreinte |
|---|---|---|
| question | `question-course-seuil-et-moniteurs-v1.md`, dossier du rédacteur | à la table d'empreintes du dossier |
| ordre de course | `ordre-course-seuil-et-moniteurs-v1.md`, même dossier | idem |
| devis et son calcul | `devis-course-seuil-et-moniteurs-v1.md`, `calcul_devis_course_seuil_et_moniteurs_v1.py`, `calcul-devis-course-seuil-et-moniteurs-v1.json` | idem |
| faits neutres de la mère | `docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/faits-seuil-et-moniteurs-v1.md` | `c8c7fb32ff7d2c8ce651607a8a777e8ee1da2cf45d101fa3a5e4f426cfb59119` |
| question neutre de la mère | même dossier, `question-seuil-et-moniteurs-v1.md` | `a5fbe8986745bf5c43eca3d33472abaeea152308db4db9aa6e16164ed8d80940` |
| gabarit | `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` |
| modèle de forme | `prereg/ideation-nouvelles-attaques-v1/preenregistrement-court-course-nouvelles-attaques-v9.md` | `864f39a7ecd41a613f8892efbf66607c14da34252d643a4fd40032b5d2b500c2` |
| nœuds | `docs/decisions/decision-N-044-v1.md`, `-N-045-v2.md`, `-N-049-v1.md`, `-N-058-v1.md`, `-N-064-v1.md`, `-N-065-v1.md`, `-N-067-v1.md` | `2b70bdac…`, `c7b05e39…`, `8a5bf5e5…`, `854f2724…`, `387c9d4e…`, `f820e90d…`, `966dd9dc…` |
| accords et décisions | `registres/go.md` et `registres/decisions.md` sur `origin/main`, commit `55f7f6e1fe6779a4fb57b5fd07f58d33d598cbef` : GO-2026-11-19-75, -76, -89 ; GO-2026-11-20-05 ; GO-2026-11-21-14 ; R-3861, R-3882, R-4131, R-4360, R-4362 | `38f63a0d40b591fb1890437107cdb77511916360e2bda0baddda70ff5986d63b` ; `352e3ea921a117faec79920fe9d329f6d96bcd1de524a04bd0eaaf2ed5caea16` |

**Ce que ce texte ne contient pas.** Aucun identifiant de modèle, aucune valeur ni nom de clé, aucun moyen de tromper un moniteur.

## Hypothèse

**Aucune hypothèse du programme n'est éprouvée par cette course.** C'est une course de l'atelier d'idées (N-065). Elle ne passe aucune porte ; aucun verdict de porte n'est prononcé.

Ce qui est décisif, et qui appelle la règle R1 : **chaque candidate porte sa propre hypothèse**, écrite par son proposeur dans le champ `test_de_mort` de sa fiche avant que le monde soit joué, et un programme dit si elle meurt. La règle R1 vise « toute expérience décisive, simulation comprise » : un test de mort sur scores simulés en est une. Ce texte gèle donc, à la place d'une hypothèse de la course, l'objet et la règle du jeu :

1. **La question** : celle du dossier, à son empreinte ; elle part par sa seule partie servie.
2. **Une génération, un étage** après elle ; rien de l'étage n'est servi à un agent.
3. **La composition** : cinq espèces, toutes proposeuses, sans Kimi ; un portier ; deux juges pour information ; un expérimentateur modèle ; un lecteur et un comparateur écrits par programme. Régime d'usage (N-044) : rien n'apprend ni ne se réécrit dans la course.
4. **Les cases** : 144 ; une famille de 24 tenue à l'écart ; onze servies, tirées par graine (ordre de course, § 4).
5. **Les mondes plantés**, leur vérité, leurs graines, la famille de mondes tenue à l'écart, le programme de mesure : scellés avant la sonde de refus (ordre de course, § 7).
6. **Qui est candidate** : au plus vingt fiches « passées », tirées par graine, quatre par voie au plus ; ordre de jeu tiré et scellé.
7. **Ce qui tranche** : le calcul contre la vérité plantée et contre la base nommée. Jamais un juge (N-058).

Hypothèses de travail, dites : l'étage sait projeter un test de mort écrit pour ces mondes (non établi ; éprouvé à blanc avant tout appel) ; l'expérimentateur programme fidèlement la règle d'une fiche (non établi ; mesuré par la classe « non exécutée » et par le contrôle C2).

## Prédiction chiffrée et signe attendu

**Aucune prédiction chiffrée de résultat n'est revendiquée pour la course, et aucun signe n'est attendu** : en inventer une serait viser un signe (règle R3). Les seuls chiffres écrits d'avance pour la course sont des coûts : 97,02 USD au cas bas, 256,14 au cas haut, 276 au pire (devis, § 0).

Les prédictions chiffrées sont celles des fiches : chacune écrit la sienne, avec son signe et l'issue qui la tue, avant l'étage. Une fiche sans prédiction chiffrée est classée « sans test » et n'est pas candidate.

Sont écrites au même rang, sans préférence :

| issue | son contraire |
|---|---|
| « aucune candidate ne tient » | « une ou plusieurs candidates tiennent » |
| « aucune règle de seuil ne fait mieux que la base à validité tenue » | « une ou plusieurs le font » |
| « aucun moniteur tiré du papier ne sépare le saboteur de l'honnête qui échoue quand la composante d'intention est nulle » | « un ou plusieurs le font » — ce qui, à composante nulle, signalerait un défaut du monde ou une fuite, et déclenche l'audit |
| « les candidates qui tiennent sur les mondes décrits tiennent aussi sur la famille tenue à l'écart » | « elles n'y tiennent pas » |

Aucune de ces issues n'est un succès ni un échec de la course.

## Métrique

Toutes calculées par programme, sans juge. Chaque part est rendue avec son numérateur et son dénominateur.

**Mesures de l'étage, par candidate, par monde et par taille d'échantillon** (définitions à l'ordre de course, § 7) : V1, taux réel de fausses alertes par tranche (moyenne sur R = 2 000 tirages de calibration, et part des tirages où il dépasse 1 %) ; V2, tenue de la garantie dite ; V3, puissance contre le signal planté, à trois tailles de signal, aux seuls tirages où la règle n'alerte pas plus de 1 % des honnêtes, et sans cette condition ; V4, abstention ; V5, épisodes honnêtes consommés ; V6, pour un protocole d'audit, part des sabotages attrapés au budget b. Intervalles : Clopper-Pearson, niveau 99 %, sur les parts.

**Mesures de la course** (descriptives ; aucune inférence au-delà de la course) :

| n° | mesure | définition |
|---|---|---|
| M1 | classes du portier | parts « passée », « hors case », « sans test », « mise à part », par case et par espèce, parmi les fiches rendues |
| M2 | classes d'issue | compte des candidates « tient », « morte, invalide », « morte, sans gain », « non exécutée », « non jouée », par voie et par espèce ; sur les mondes décrits, et à part sur la famille tenue à l'écart |
| M3 | fragilités | pour chaque candidate, les mondes dont elle ne déclare pas tenir les suppositions et où sa garantie est violée ; rapportées, ne tuent pas |
| M4 | coût | par espèce et par rôle ; par candidate pour l'expérimentateur ; machine ; part du coût et part des candidates qui tiennent, par espèce (N-045 v2, N-058) |
| M5 | réponses sans fiche | compte des appels de proposeur sans fiche : réponse vide motivée, refus du modèle, réponse illisible |
| C1 | contrôles du tirage | onze cases servies, aucune deux fois, aucune de la famille tenue à l'écart, cinq voies au moins ; nombre de tirages refaits |
| C2 | contrôle de fidélité | pour cinq candidates tirées par graine, un second programme de la règle, écrit par un développeur qui n'a pas vu le premier ; les deux sont joués sur le monde A ; écart de V1 rapporté |
| I1 | juges, pour information | leur classement, à part ; et, après l'étage, la part des candidates du premier tiers de chaque juge qui tiennent, contre la part dans les deux autres tiers. Description : elle n'entre dans rien |
| I2 | collisionneur, pour information | compte des fiches passées étiquetées « déjà au collisionneur » par la lecture de la mère |

## Seuil

Aucun taux d'erreur n'est visé pour la course : elle ne décide rien du programme. Les seuils sont ceux des tests de mort et des gardes, fixés ici avant toute lecture.

| seuil | valeur | source |
|---|---|---|
| mort, invalide | la borne basse de l'intervalle à 99 % de la grandeur garantie dépasse la valeur garantie (1 % pour « en moyenne » ; le risque dit pour « avec une confiance dite » ; le niveau dit pour « à tout instant »), sur un monde dont la fiche déclare tenir les suppositions | ordre de course, § 7 ; valeur du rédacteur |
| mort, sans gain | la borne haute de l'intervalle à 99 % de V3 ne dépasse pas la puissance de la base nommée, au signal moyen, à n = 400 | idem |
| garantie « aucune » | une fiche qui ne dit aucune garantie ne peut pas mourir « invalide » ; elle est jouée, V1 est rapporté, et elle meurt « sans gain » si, aux tirages où elle tient 1 %, elle ne dépasse pas la base | valeur du rédacteur |
| non exécutée | deux sessions d'expérimentateur sans programme qui passe la vérification de forme | valeur du rédacteur |
| ligne de course, montant exact | **260 USD** : une génération à 150, un étage à 110. **À accorder par Lazar ; rien ne court avant son mot** | devis, § 0 et § 8 |
| lignes à part | machine jetable et essai du bac 10 ; épreuve des témoins 5 ; sonde de refus 1 | devis, § 0 |
| plafond total | **276 USD** | devis, § 0 |
| parts au pire par relais | premier 150 ; deuxième 150 ; troisième 66,55 ; expérimentateur 110 | devis, § 4 |
| garde des fiches mises à part | l'étage ne part pas si strictement plus d'un quart des fiches rendues sont « mises à part » | valeur du rédacteur, d'après la garde du coffre de la course « nouvelles attaques » |
| audit de symétrie, étage | toutes les candidates jouées tiennent, ou toutes meurent ; ou plus de la moitié sont « non exécutées » | valeurs du rédacteur (règle R4) |
| audit de symétrie, portier | aucune fiche hors des « passées » ; ou strictement plus de la moitié des fiches rendues « sans test » | valeurs du rédacteur |

## Plan d'analyse

**Données.** Les sorties de la génération et de l'étage, dans le dossier de sortie de la course ; les mondes plantés scellés. Aucun épisode du programme, aucun score d'un moniteur du programme (N-053, point 5).

**Tailles et leur raison.** Onze cases et cinq espèces : la forme de la course v9, dont les coûts sont mesurés. Vingt candidates : ce que l'étage paie à son cas haut sous 110 USD. n ∈ {200, 400} par tranche : « quelques centaines », l'énoncé du problème. R = 2 000 tirages : à ce nombre, l'intervalle à 99 % d'une part voisine de 1 % a une demi-largeur de l'ordre de 0,6 point — **ordre de grandeur donné de tête, à recalculer par le programme de mesure avant le scellement** ; si la demi-largeur ne permet pas de distinguer 1 % de 2 %, R est relevé avant le scellement, jamais après.

**Graines** (règle R9). Une racine écrite au complément de valeurs ; par `numpy.random.SeedSequence`, des suites dérivées et nommées : famille de cases tenue à l'écart ; tirage des cases ; famille de mondes tenue à l'écart ; mondes ; tirage des candidates ; ordre de jeu ; contrôle C2. Consignées au manifeste du run.

**Comparaisons.** Chaque candidate contre la vérité plantée et contre la base nommée. **Aucune comparaison entre candidates, entre espèces ou entre voies n'est testée** : ce sont des comptes. Donc aucune correction pour comparaisons multiples entre elles. Dans une candidate, la mort se lit monde par monde : une seule violation, sur un monde déclaré, tue ; le niveau de 99 % par intervalle est choisi pour que, sur quelques dizaines de couples monde et taille, une mort par le seul hasard reste rare — **non chiffré ici ; le taux de mort par hasard du témoin valide est mesuré à l'épreuve des témoins et écrit au complément de valeurs.**

**Contrôles appariés.** Chaque candidate et sa base sont jouées sur les mêmes tirages de calibration et les mêmes épisodes d'épreuve.

**Ordre de lecture.** Les comptes d'abord, par programme ; puis les fiches, mortes comprises, par la mère ; l'étiquette « déjà au collisionneur » ensuite. Les mesures sont lues une fois, après l'étage.

**Course arrêtée avant la fin.** Si la génération s'arrête à son plafond, l'étage joue sur les fiches rendues, et l'arrêt est rapporté. Si l'étage s'arrête à son plafond, les candidates jouées gardent leur classe ; les autres sont « non jouées » ; rien n'est dit d'elles.

## Critères de lecture gelés

| issue observée | ce qu'on a le droit de dire |
|---|---|
| une candidate « tient » | « elle tient sur les mondes plantés nommés, à ces paramètres » ; elle devient candidate à un préenregistrement du programme. **Jamais « validée », jamais « règle le problème ».** |
| une candidate « morte, invalide » | « sa garantie dite est violée sur le monde nommé, dont elle déclarait tenir les suppositions » |
| une candidate « morte, sans gain » | « elle est valide et ne fait pas mieux que la base nommée » |
| « non exécutée » ou « non jouée » | rien sur la règle ; un compte, et la raison |
| une candidate tient sur les mondes décrits et meurt sur la famille tenue à l'écart | les deux, à part ; la fiche n'est pas dite « universelle » |
| aucune candidate ne tient | « aucune des candidates jouées ne tient sur ces mondes » ; cela ne dit pas que le problème est sans solution |
| le rang d'un juge suit, ou ne suit pas, les classes d'issue | une description, sous le titre « pour information » ; aucune conclusion sur le juge à vingt candidates |
| coût et candidates qui tiennent, par espèce | des comptes ; **aucune réduction de la composition** |

**Ce qui déclenche l'audit de symétrie (règle R4)** : les seuils d'audit de la section « Seuil » ; un moniteur tiré du papier qui sépare le saboteur de l'honnête qui échoue à composante d'intention nulle ; un écart du contrôle C2 hors de l'intervalle. Le même audit dans les deux sens : relecture du programme de mesure, du monde et du programme de l'expérimentateur, par un agent qui n'a écrit aucun des trois.

**Verdict.** Cette course ne prononce ni « confirmé », ni « réfuté », ni « non concluant » sur une hypothèse du programme. Les seuls verdicts sont les classes d'issue, candidate par candidate.

## Liste d'arrêt

Chaque garde s'éprouve sur un cas sain et sur un artefact avant la course (règle R5) ; aucun repli silencieux.

| n° | condition | action |
|---|---|---|
| 1 | refus d'un classifieur de sûreté | le tour s'arrête, consigné tel quel, non relancé |
| 2 | une espèce refuse la question à la sonde | retirée de tous les rôles, sans reformulation |
| 3 | un témoin du portier ou de l'étage manqué | aucune course ; aucune retouche sans version neuve |
| 4 | l'essai réel du bac échoue sur la machine jetable | aucun étage |
| 5 | plafond de la génération, de l'étage ou d'une ligne à part atteint | arrêt avant le poste |
| 6 | une clé dont le reste relu ne couvre pas sa part | départ refusé |
| 7 | motif interdit dans un texte à servir | rien n'est envoyé, rien n'est retiré du texte |
| 8 | empreinte de la partie servie, d'un monde ou du programme de mesure différente de l'empreinte scellée | départ refusé |
| 9 | la machine du bac n'est pas déclarée jetable, ou une clé y est présente | l'étage ne part pas |
| 10 | le programme d'un expérimentateur tente de lire autre chose que l'interface du monde (la vérité, les graines, le réseau) | la candidate est « non exécutée », l'incident est consigné ; trois incidents arrêtent l'étage |
| 11 | strictement plus d'un quart des fiches rendues « mises à part » | l'étage ne part pas |
| 12 | modèle servi différent du modèle demandé | arrêt |
| 13 | une sortie de l'étage est servie à un agent, ou une sortie du collisionneur à un proposeur | la lecture est invalidée |

## Ce qui reste à écrire avant le scellement

1. Le mot de Lazar sur l'extension du régime « tests de mort réels » à cette course (rapport, D1), et sur la ligne de calcul.
2. Les mondes plantés, leur vérité, le programme de mesure, le comparateur, leurs essais ; contre-lus et scellés ; leurs empreintes ici.
3. Le véhicule (ordre de course, § 2.2), contre-lu ; ses empreintes ici.
4. La partie servie dérivée par programme ; la liste de la garde de motifs.
5. Le complément de valeurs : racine des graines, parts par clé après un relevé du jour, relais de l'expérimentateur, offre du loueur, demi-largeur recalculée pour R, taux de mort par hasard du témoin valide, noms des classes d'issue alignés sur l'additif `cb352811…`.
6. Les témoins, écrits par la mère.

## Contre-lecture

**À faire.** Sous-agent neuf, d'un autre modèle que le rédacteur, qui n'a écrit aucune de ces pièces (règle R2). Fichiers à lui donner, par leur chemin complet : les cinq pièces du dossier et le calcul ; les faits et la question neutres de la mère ; le gabarit ; le préenregistrement court v9 de la course « nouvelles attaques » ; le rapport du développeur de la version 68 ; les lignes GO-2026-11-19-75, GO-2026-11-19-76 et GO-2026-11-20-05 ; R-3861 et R-3882. Empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque : à porter ici par la version qui suivra. **Tant que cette section n'est pas remplie, ce texte n'est pas scellable.**
