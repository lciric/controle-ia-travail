# Préenregistrement court — course « seuil et moniteurs », option (b) : l'étage des tests de mort seul, sur les propositions déjà rendues — v3

- Auteur : rédacteur de la conception de la course seuil et moniteurs, modèle F.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:03:52Z.
- Version : la v3 remplace la v2 (`54a89d27f1cbd910120d73e6eb38535de412e84a7dfeaa262321b2a381362526`, brouillon non scellé, gardé intact) après la contre-lecture `662f751006d7f23c887ea5fb4088bc93dd32521f77362b77f51ee13c099b44bf` (« À corriger »), jeux portés tels quels : trois remplacements par l'outil contre-lu (`scripts/remplacer_texte_exact_v1.py`, `391db990734dd36f7c827b8b6c77dc0de1bda324f671b65748ccfe68c56a53d6`), sortie à l'empreinte de l'essai du contre-lecteur (`ee0bea7118efdf8dac4579d898b293613cf9a91b7a128236cf09c1abd86ae571`) ; puis trois remplacements pour les décisions de la mère de 07:24Z, et trois de tenue. Relevé de `date -u` : 07:26:18Z. Dans ce texte, hors de cette ligne et de la suivante, « ordre de course v2 », « ordre v2 », « devis v2 » et « rapport v2 » se lisent « v3 » ; le calcul du devis reste le programme v2 et sa sortie, inchangés ; les empreintes des pièces v3 sont à la table d'empreintes v3.
- Version antérieure : la v2 remplaçait la v1 (`8bab33820d9d7b44f4934534001238c9392f00bd74e09c99ff8246ff4718a92c`, brouillon non scellé, gardé intact) après GO-2026-11-21-16 (option (b)) et après la contre-lecture de la v1 (`18b630f702ae394dded262dda84b7f64d2bb84806202c558da06d7008240e2d4`, « À corriger »).
- Statut : **brouillon, non contre-lu, non scellé.** Il ne peut pas être scellé en l'état (section « Ce qui reste à écrire avant le scellement »). Aucune fiche, aucune issue n'est lue avant le scellement (règles R1 et R3).
- Commit du code d'analyse : **aucun à cette date.** Le programme de mise en fiches, le programme de mesure, le comparateur et le tirage restent à écrire ; leur commit et leurs empreintes entrent au complément de valeurs, avant tout allumage.
- Documents qui font foi (chemin et empreinte) :

| pièce | chemin | empreinte |
|---|---|---|
| ordre de course v2 | `ordre-course-seuil-et-moniteurs-v2.md`, dossier du rédacteur | à la table d'empreintes v2 |
| devis v2 et son calcul | `devis-course-seuil-et-moniteurs-v2.md`, `calcul_devis_course_seuil_et_moniteurs_v2.py`, `calcul-devis-course-seuil-et-moniteurs-v2.json` | idem |
| contre-lecture de la v1 | `docs/notes/ideation-seuil-moniteurs-v1/conception-v1/contre-lecture-v1/contre-lecture-conception-seuil-moniteurs-v1.md` | `18b630f702ae394dded262dda84b7f64d2bb84806202c558da06d7008240e2d4` |
| faits neutres de la mère | `docs/notes/papier-dopamine-moniteur-v1/collisionneur-seuil-et-moniteurs-v1/faits-seuil-et-moniteurs-v1.md` | `c8c7fb32ff7d2c8ce651607a8a777e8ee1da2cf45d101fa3a5e4f426cfb59119` |
| gabarit | `prereg/gabarit-preregistrement-v1.md` | `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` |
| nœud | `docs/decisions/decision-N-058-v1.md` | `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d` |
| accords et décisions | `registres/go.md` et `registres/decisions.md` sur `origin/main`, commit `332080c5f64d436627351cfbfc17a9603248454c` : GO-2026-11-19-75, -76 ; GO-2026-11-20-05, -10 ; GO-2026-11-21-13, -14, -15, -16 ; R-3882, R-4372, R-4374, R-4377, R-4386 | `ba9ba9eb9876e309d6719f009a0f158b10183b093abc5532fc38c94c518b69fa` ; `a1f662faa31c55252b1cde109c727fa2496b74d64d63e1e4457b7b4206e9042b` |
| textes sources | chez la mère ; **leurs chemins et leurs empreintes entrent ici avant le scellement** | à porter |

**Ce que ce texte ne contient pas.** Aucun identifiant de modèle, aucune valeur ni nom de clé, aucun moyen de tromper un moniteur. La question v1 du dossier n'est pas une pièce de ce texte : sous (b), rien n'est servi à un proposeur.

## Hypothèse

**Aucune hypothèse du programme n'est éprouvée par cette course**, et aucune n'y est tenue pour acquise. En particulier, que la sonde de réussite attendue lise l'échec plutôt que l'intention est une hypothèse du programme ; les mondes en plantent les deux branches et n'en tranchent aucune.

Ce qui est décisif, et qui appelle la règle R1 (« toute expérience décisive, simulation comprise ») : chaque candidate porte une garantie dite, et un programme dit, sur des scores simulés, si elle meurt. Ce texte gèle l'objet et la règle du jeu :

1. **Les textes sources** : ceux que GO-2026-11-21-16 nomme (collisionneur, trois consultations, moniteur de dissonance), à leurs empreintes ; ni plus, ni moins (ordre de course v2, § 1).
2. **La mise en fiches** : deux traducteurs de deux lignées, un texte par appel, forme fixe, union des deux extractions, vérification de l'extrait par programme, aucun chiffre ajouté, aucune fusion entre textes (ordre, § 3 et § 4).
3. **Le tirage** : onze candidates ; d'abord les trois points de GO-2026-11-21-15 que la mère retient (moniteur de dissonance ; budget d'audit réparti selon la valeur ; aiguillage en lecture rétrospective par texte à part), par leurs passages, liste scellée avant la mise en fiches ; puis par graine (ordre, § 5).
4. **L'étage** : un expérimentateur modèle, qui reçoit la fiche et non le texte ; deux sessions au plus ; un bac sur machine jetable ; un lecteur et un comparateur écrits par programme (ordre, § 6).
5. **Les mondes plantés**, leur vérité, leur table « monde → supposition cassée », leurs graines, le programme de mesure : scellés avant la mise en fiches (ordre, § 7).
6. **Ce qui tranche** : le calcul contre la vérité plantée et contre la base nommée. Aucun juge ne joue (N-058).

Hypothèses de travail, dites : l'étage sait jouer un programme écrit pour ces mondes (non établi ; éprouvé à blanc) ; les traducteurs rendent fidèlement les textes (non établi ; mesuré par les témoins, par T2 et T3) ; l'expérimentateur programme fidèlement une fiche (non établi ; mesuré par C2).

## Prédiction chiffrée et signe attendu

**Aucune prédiction chiffrée de résultat n'est revendiquée pour la course, et aucun signe n'est attendu** (règle R3). Les seuls chiffres écrits d'avance sont des coûts, et **ce sont des règles du rédacteur, non des mesures** : 20,77 USD au cas bas, 97,41 au cas haut, 114,48 au pire (devis v2, § 0).

La prédiction d'une candidate est sa garantie dite, lue dans le texte par la mise en fiches. Quand le texte écrit en plus son propre test, il est gardé mot pour mot dans le champ `prediction_dite_par_le_texte` et lu à part (mesure M6).

Sont écrites au même rang, sans préférence :

| issue | son contraire |
|---|---|
| « aucune candidate ne tient » | « une ou plusieurs candidates tiennent » |
| « aucune règle de seuil ne fait mieux que la base à garantie tenue » | « une ou plusieurs le font » |
| « au réglage où la composante d'intention est nulle, aucun moniteur tiré du papier ne sépare le saboteur de l'honnête qui échoue » | « un ou plusieurs le font » — ce qui, à ce réglage, signale un défaut du monde ou une fuite, et déclenche l'audit |
| « au réglage où elle n'est pas nulle, aucun ne les sépare mieux que la base » | « un ou plusieurs le font » |
| « moins de onze fiches sont calculables telles quelles » | « onze ou plus le sont » |

Aucune de ces issues n'est un succès ni un échec de la course.

## Métrique

Toutes calculées par programme, sans juge. Chaque part est rendue avec son numérateur et son dénominateur.

**Mesures de l'étage**, par candidate, par monde et par taille d'échantillon (définitions à l'ordre de course v2, § 7) : V1★, taux **vrai** de fausses alertes sous la loi plantée, par tirage de calibration ; V1, taux observé, rapporté, qui ne tue jamais ; V2, tenue de la garantie dite ; V3, puissance ; V3Δ, écart apparié de puissance à la base ; V4, abstention ; V5, épisodes honnêtes consommés ; V6, pour un protocole d'audit. **L'unité de tout intervalle est le tirage de calibration** (R = 2 000), jamais les épisodes mis en commun. Niveau : 99 %. Pour une part de tirages : Clopper-Pearson. Pour une moyenne ou un écart apparié sur les tirages : méthode à geler avec les mondes.

**Mesures de la course** (descriptives ; aucune inférence au-delà de la course) :

| n° | mesure | définition |
|---|---|---|
| T1 | registre des fiches | par texte et par traducteur : fiches rendues, fiches refusées par le programme (et pourquoi), fiches par `etat` et par `sorte` |
| T2 | accord des traducteurs | part des propositions du registre trouvées par les deux ; parmi elles, part des « traductions disputées », par champ |
| T3 | témoins de la mise en fiches | issue de chaque proposition plantée, par traducteur |
| M2 | classes d'issue | compte des candidates « tient », « morte, invalide », « morte, sans gain », « non exécutée », par `sorte` et par texte source ; à part pour les propositions nommées par Lazar et pour les tirées ; à part pour les « traductions disputées » et pour les `retiree_par_son_auteur` |
| M3 | fragilités | pour chaque candidate, les mondes où elle ne déclare pas tenir et où sa garantie est violée ; rapportées, ne tuent pas |
| M4 | coût | par candidate pour l'expérimentateur ; par texte et par traducteur ; machine |
| M6 | le test dit par le texte | pour chaque candidate dont le champ `prediction_dite_par_le_texte` n'est pas « aucune » : la grandeur qu'il nomme est-elle l'une de V1★ à V6 ; si oui, sa valeur mesurée, et si l'issue que le texte disait le réfuter est observée. **Rapportée à part ; elle ne change aucune classe d'issue.** Si la grandeur n'est pas mesurable sur ces mondes : « hors des mondes », compté |
| C2 | contrôle de fidélité | pour trois candidates tirées par graine, un second programme de la fiche, écrit par un développeur qui n'a pas vu le premier ; les deux joués sur le monde A ; écart de V1★ rapporté |
| C3 | base invalide | les couples monde et tranche où la base elle-même viole 1 % selon le critère « invalide » appliqué à elle, calculés par programme (au moins la tranche de quarante épisodes de la famille D ; la famille F peut en donner) : rapportés à part, sans mort « sans gain » ; la mort « invalide » d'une candidate y garde son cours |

## Seuil

Aucun taux d'erreur n'est visé pour la course. Les seuils sont ceux des tests de mort et des gardes.

| seuil | valeur | source |
|---|---|---|
| mort, invalide, « en moyenne » | la borne basse de l'intervalle à 99 % de la moyenne de V1★ sur les R tirages dépasse 1 %, sur un monde où la fiche déclare tenir | ordre v2, § 7 ; contre-lecture, § 5, point 2 |
| mort, invalide, « avec une confiance dite » | la borne basse de l'intervalle de Clopper-Pearson à 99 % de la part des tirages où V1★ dépasse 1 % dépasse le risque dit | idem |
| mort, invalide, « à tout instant » | de même, sur la part des tirages où une suite honnête déclenche, contre le niveau dit | idem |
| mort, sans gain | la borne basse de l'intervalle à 99 % de la moyenne de V3Δ sur les tirages, au signal moyen, à n = 400, **ne dépasse pas zéro** | ordre v2, § 6 et § 7 ; contre-lecture, § 5, point 3 |
| garantie « aucune » | pas de mort « invalide » ; mort « sans gain » aux tirages où V1★ est d'au plus 1 % | valeur du rédacteur |
| où une fiche « déclare tenir » | calculé par programme : aucun de ses `suppositions_declarees` n'est cassé par le monde, selon la table scellée | ordre v2, § 7 |
| non exécutée | deux sessions sans programme qui passe la vérification de forme | valeur du rédacteur |
| recouvrement d'extraits | deux fiches d'un même texte portent la même proposition si leurs extraits se recouvrent pour plus de la moitié du plus court | valeur du rédacteur |
| ligne de calcul | **114,48 USD**, en trois plafonds d'arrêt : étage 84 ; mise en fiches 20,48 ; machine 10. **À accorder par Lazar ; rien ne court avant** | devis v2, § 0 et § 8 ; plafond indicatif 120, GO-2026-11-21-16 |
| plafond de session de l'expérimentateur | 3,00 USD ; deux sessions au plus par unité | devis v2, § 2 ; règle du rédacteur |
| audit de symétrie, étage | toutes les candidates jouées tiennent, ou toutes meurent ; ou plus de la moitié sont « non exécutées » | valeurs du rédacteur (règle R4) |
| audit de symétrie, mise en fiches | aucune fiche « incomplète » ni « non calculable » ; ou moins du quart des propositions trouvées par les deux traducteurs ; ou plus de la moitié de « traductions disputées » | valeurs du rédacteur |

## Plan d'analyse

**Données.** Les textes sources, à leurs empreintes ; le registre scellé des fiches ; les sorties de l'étage ; les mondes scellés. Aucun épisode du programme, aucun score d'un moniteur du programme (N-053, point 5).

**Tailles et leur raison.** Onze candidates et trois témoins : ce que 84 USD paient au pire, à 6,00 l'unité ; sous la règle de réservation, les quatorze unités partent au cas haut comme au pire (devis v2, § 3, calculé par programme). n ∈ {200, 400} par tranche : l'énoncé du problème. R = 2 000 tirages : avec le tirage pour unité et le taux vrai pour grandeur, le bruit d'épreuve n'entre plus dans la mort « invalide » ; la largeur des intervalles à ce R est **à calculer par le programme de mesure avant le scellement**, et R est relevé avant, jamais après, si elle ne sépare pas 1 % de 2 %.

**Graines** (règle R9). Une racine au complément de valeurs ; par `numpy.random.SeedSequence`, des suites dérivées et nommées : lequel des deux traducteurs est « premier », texte par texte ; mondes ; tirage des candidates ; ordre de jeu ; contrôle C2. Consignées au manifeste du run.

**Comparaisons.** Chaque candidate contre la vérité plantée et, appariée, contre la base. **Aucune comparaison entre candidates, entre textes ou entre auteurs n'est testée** : des comptes. Dans une candidate, une seule violation sur un monde où elle déclare tenir la tue ; le taux de mort par hasard du témoin valide est mesuré à l'épreuve des témoins et écrit au complément de valeurs.

**Contrôles appariés.** Candidate et base sur les mêmes tirages de calibration et les mêmes épisodes d'épreuve.

**Ordre des opérations, gelé.** (1) Scellement des mondes, de la table, de la liste des passages nommés et des graines. (2) Mise en fiches. (3) Vérification et appariement par programme. (4) **Scellement du registre des fiches.** (5) Tirage des candidates. (6) Essai du bac, témoins de l'étage. (7) Candidates. (8) Lecture des comptes, une fois, puis des fiches.

**Course arrêtée avant la fin.** Si la mise en fiches s'arrête à son plafond, les textes non traduits sont nommés et le tirage se fait sur le registre obtenu. Si l'étage s'arrête, les candidates jouées gardent leur classe ; les autres sont « non jouées ».

## Critères de lecture gelés

| issue observée | ce qu'on a le droit de dire |
|---|---|
| une candidate « tient » | « elle tient sur les mondes plantés nommés, à ces paramètres, dans la lecture qu'en a faite la mise en fiches » ; candidate à un préenregistrement du programme. **Jamais « validée ».** |
| « morte, invalide » | « sa garantie dite est violée sur le monde nommé, où elle déclarait tenir » |
| « morte, sans gain » | « sa garantie tient et elle ne fait pas mieux que la base nommée » |
| une candidate à « traduction disputée » meurt | la mort vaut pour la lecture jouée ; l'autre lecture est citée à côté ; **on ne dit pas que l'idée du texte est morte** |
| « non exécutée », « non jouée », « incomplète », « non calculable » | rien sur l'idée ; un compte, et ce qui manquait |
| M6 : le test dit par le texte est réfuté, la candidate tient | les deux, à part ; la classe ne change pas |
| aucune candidate ne tient | « aucune des candidates jouées ne tient sur ces mondes » ; cela ne dit pas que le problème est sans solution |
| comptes par texte source ou par auteur | des comptes ; **aucun classement d'espèce** |

**Ce qui déclenche l'audit de symétrie (règle R4)** : les seuils d'audit de la section « Seuil » ; un moniteur qui sépare le saboteur de l'honnête qui échoue au réglage où la composante d'intention est nulle ; un écart de C2 hors de l'intervalle ; une proposition nommée par Lazar qui serait la seule à tenir, ou la seule à mourir. Le même audit dans les deux sens : relecture du programme de mesure, du monde, de la fiche et du programme de l'expérimentateur, par un agent qui n'en a écrit aucun.

**Verdict.** Ni « confirmé », ni « réfuté », ni « non concluant » sur une hypothèse du programme. Les seuls verdicts sont les classes d'issue, candidate par candidate.

## Liste d'arrêt

Chaque garde s'éprouve sur un cas sain et sur un artefact avant la course (règle R5) ; aucun repli silencieux.

| n° | condition | action |
|---|---|---|
| 1 | refus d'un classifieur de sûreté | l'appel s'arrête, consigné tel quel, non relancé |
| 2 | un traducteur manque un témoin | il est écarté ; s'il n'en reste qu'un, rien ne part sans un mot de la mère |
| 3 | un témoin de l'étage manqué (témoins joués sur le monde A) | aucun étage ; aucune retouche sans version neuve |
| 4 | l'essai réel du bac échoue sur la machine jetable | aucun étage |
| 5 | un plafond d'arrêt atteint (étage, mise en fiches, machine) ; une unité dont le pire ne tient plus | arrêt avant l'appel |
| 6 | une clé dont le reste relu ne couvre pas sa part | départ refusé |
| 7 | motif interdit dans un texte à envoyer | rien n'est envoyé, rien n'est retiré du texte |
| 8 | empreinte d'un texte source, d'un monde, de la table ou du programme de mesure différente de l'empreinte scellée | départ refusé |
| 9 | la machine du bac n'est pas déclarée jetable, ou une clé y est présente | l'étage ne part pas |
| 10 | le programme d'un expérimentateur tente de lire autre chose que l'interface du monde | la candidate est « non exécutée », incident consigné ; trois incidents arrêtent l'étage |
| 11 | modèle servi différent du modèle demandé | arrêt |
| 12 | une fiche ou une issue est servie à un modèle autre que l'expérimentateur (la fiche seule) ; un texte source est servi à l'expérimentateur | la lecture est invalidée |
| 13 | une fiche porte un chiffre absent de son extrait et de son texte, ou un champ ajouté | la fiche est refusée par le programme ; comptée |
| 14 | **le tirage des candidates est demandé alors que le registre des fiches n'est pas scellé**, ou que son empreinte diffère de l'empreinte scellée | le tirage est refusé ; l'étage ne part pas |
| 15 | la liste des passages nommés par Lazar n'était pas scellée avant la mise en fiches | aucune proposition n'entre « nommée » : toutes passent par le tirage |

## Ce qui reste à écrire avant le scellement

1. La ligne de calcul, sur le devis v2 contre-lu.
2. Les deux notes de conception du modèle F (tests de mort ; moniteur de dissonance, rendue : R-4382), puis les mondes, leur table, le programme de mesure, le comparateur, la méthode de l'intervalle apparié ; contre-lus et scellés ; leurs empreintes ici.
3. Le programme de mise en fiches et sa consigne ; le véhicule de l'étage ; contre-lus ; leurs empreintes ici.
4. Les chemins et les empreintes des textes sources ; la liste des passages nommés.
5. Le complément de valeurs : racine des graines, lignées des deux traducteurs (l'un de la lignée de l'expérimentateur, l'autre d'une deuxième lignée, l'auteur des mondes de la troisième : décision de la mère, 07:24Z, D-M9) et leur plafond de sortie, provision de réflexion comprise, relais et parts par clé après un relevé du jour, offre du loueur, largeur des intervalles à R, taux de mort par hasard du témoin valide, valeur du signal moyen, de γ et de b, noms des classes d'issue alignés sur l'additif `cb352811…`.
6. Les témoins, écrits par la mère.
7. **Hors de ce texte** (décision de la mère, 07:24Z) : le premier test de mort de la note du moniteur de dissonance (R-4382, `403fe3e2827540569e45c82866eea98d91d977fad74d5c518f852c806e82fae2`), sur MATH500, et le monde à K actions du jumeau honnête. Ils ont leur propre texte scellé, leur devis et leur ligne. Ce préenregistrement ne les couvre pas et ne lit aucun de leurs résultats ; la course ne paie pas ce test, et ce test ne paie pas la course.

## Contre-lecture

**Faite pour la v2** : contre-lecteur neuf, modèle O ; brouillon relu `54a89d27f1cbd910120d73e6eb38535de412e84a7dfeaa262321b2a381362526` ; rapport `docs/notes/ideation-seuil-moniteurs-v1/conception-v2/contre-lecture-v1/contre-lecture-conception-seuil-moniteurs-v2-v1.md`, `662f751006d7f23c887ea5fb4088bc93dd32521f77362b77f51ee13c099b44bf`, verdict « À corriger » ; ses trois remplacements pour ce texte (K2-P1, K2-P2, K2-P3) sont acceptés et portés tels quels. **À faire pour la v3** : le contrôle de son différentiel, par le même contre-lecteur. Sous-agent neuf, d'un autre modèle que le rédacteur (règle R2). Fichiers à lui donner, par leur chemin complet : les pièces v2 du dossier et le calcul v2 ; la contre-lecture de la v1 et la table de correspondance du rapport v2 ; les faits neutres de la mère ; le gabarit ; les lignes GO-2026-11-21-13 à -16 ; R-4377. **Tant que cette section n'est pas remplie, ce texte n'est pas scellable.**

Traitement de la contre-lecture de la v1 (`18b630f7…`) : chaque correction est acceptée ; la table « correction → où elle est dans la v2, ou pourquoi elle est sans objet sous (b) » est au rapport v2, § 3.
