# Erratum 2 de la réponse à la question 4 : l'hypothèse d'émergence, transition des coauteurs et groupes en interaction (v1)

- **Nature** : pièce de travail (classe C), erratum ; la pièce visée et son erratum 1 ne sont pas modifiés. L'erratum 1 reste en vigueur, sauf là où le présent texte le complète ou le corrige.
- **Heure** : `2026-11-24T18:02:12Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièces visées** : `reponse-q4-emergence-transition-et-groupes-v1.md` (`249c611c35c9bbe3742ebe3908dbb6ea059d16213b8ec967e49b4596cc2f922a`) ; `reponse-q4-emergence-transition-et-groupes-v1-erratum-1.md` (`b359bf154fc338e6392bdd8f73c8c6bd0145e15f814e9c0bcd433be4a9c685cc`).
- **Source des constats** : `contre-lecture-questions-directeur-opus-max-v1.md` (`31eb1c07fe83084df51e840ebeaf867905503d6304c1853440341550019f5eed`), section 3.4 : Q4-M1, Q4-m1, Q4-m2, Q4-m3. Un mineur de plus, trouvé ici (graines).
- **Calcul refait** : `simulation-emergence-organisme-v3.py` (`7ac344e5eea634d1e65fa8414fa6ac4876a3a69bfe5014f894977cc9ca0265ce`), sortie `simulation-emergence-organisme-v3-sortie.txt` (`70ec1939d78f7a5a917ed3d10593b9ef8cab8dfdaaa19a2986d4000da38c3b54`), même dossier, processeur, environ 26 secondes, numpy 2.5.3, python 3.13.18, graine racine 20261124, clé `(5,)` par `numpy.random.SeedSequence`. Rejoué deux fois : sorties identiques octet pour octet (hors ligne d'en-tête datée). Script autonome ; il ne lit ni la v1 ni la v2. Tous les chiffres ci-dessous en viennent, sauf mention.

## Majeur (Q4-M1, accepté et aggravé) : la courbe de percolation dépend du modèle de transmission des deux moitiés et du nombre de tours

**Textes fautifs.** Pièce, section 4, contraste C3 : « si chaque saut transmet une moitié avec la probabilité f, le recouvrement des composites suit la percolation de liens […]. Prédiction sans paramètre libre, f tiré de E0 : […] 0,11, 0,35 et 0,66 aux doses 1, 2 et 4 ». Erratum 1 : « La courbe repose pourtant sur quatre hypothèses posées » (f indépendant du degré, sauts indépendants, même prise après relais, graphe connu), et « Avec la formule fautive de E0 […] environ 20 % trop bas : assez pour rejeter à tort la percolation ».

**Vérification.** Les v1 et v2 tirent une seule réalisation de percolation, commune aux deux moitiés : elles se rencontrent si et seulement si leurs détenteurs sont dans le même amas ouvert, sans limite de tours. La phrase de la pièce (« chaque saut transmet une moitié ») décrit au contraire des pertes propres à chaque moitié, et le protocole a un nombre fini de tours (4 dans le plan réduit, 5 dans le plan complet, à budget égal : sortie v3, partie C2). La v3 calcule, sur les mêmes graphes, quatre modèles de transmission en lecture « arête » (commune ; partielle, une arête sur deux recopie le masque de l'autre moitié ; indépendantes, chaque arête décide une fois par moitié ; renouvelées, un agent renvoie à chaque tour ce qu'il tient, tirage neuf à chaque transmission) et trois en lecture « relais ». Le contrôle redonne la v2 : 0,108, 0,355, 0,656 en lecture « arête » commune illimitée (v2 : 0,111, 0,353, 0,656), 0,125, 0,380, 0,659 en lecture « relais » (v2 : 0,129, 0,382, 0,660).

**Recouvrement attendu d'une composite, N = 16, h = 0,7, ε = 0,02 (sortie v3, C1).**

| Modèle de transmission, f = 0,8 | c = 1 | c = 2 | c = 4 | écart à c = 2 |
|---|---|---|---|---|
| Arête, commune, illimité (v1, v2) | 0,108 | 0,355 | 0,656 | référence |
| Arête, commune, 2 tours | 0,102 | 0,313 | 0,641 | −12 % |
| Arête, indépendantes, 4 tours | 0,136 | 0,424 | 0,680 | +20 % |
| Arête, indépendantes, 5 tours | 0,138 | 0,433 | 0,681 | +22 % |
| Arête, indépendantes, illimité | 0,139 | 0,439 | 0,682 | +24 % |
| Arête, renouvelées, 4 tours | 0,153 | 0,472 | 0,686 | +33 % |
| Arête, renouvelées, 5 tours | 0,155 | 0,477 | 0,686 | +35 % |
| Relais, commune, illimité (v2) | 0,125 | 0,380 | 0,659 | référence relais |
| Relais, indépendantes, 4 tours | 0,142 | 0,434 | 0,681 | +14 % |

- Les chiffres de la contre-lecture (0,138 à 0,141, 0,439 à 0,440, 0,681 sans limite ; 0,137, 0,425, 0,679 à 4 tours ; 0,122, 0,348, 0,655 à 2 tours) sont **confirmés** (0,139, 0,439, 0,682 ; 0,136, 0,424, 0,680 ; 0,120, 0,348, 0,656).
- **Aggravation** non vue par la contre-lecture : si les agents renvoient à chaque tour ce qu'ils tiennent, l'écart monte à +33 % à c = 2 (4 tours) ; à f = 0,6, il vaut +50 % (indépendantes) et +107 % (renouvelées) à c = 2, 4 tours. Le nombre de tours compte aussi dans le modèle commun : −12 % à 2 tours.
- **Nuance dans l'autre sens**, non vue par l'erratum 1 ni par la contre-lecture (sortie v3, C3) : au plan prévu (3 courses par dose, 4 composites chacune), un test d'adéquation de la courbe commune (rapport de vraisemblance, 4 degrés de liberté, seuil 0,05, h et f pris exacts) la rejette à tort dans 8 % des cas si les pertes sont indépendantes (4 tours), 12 % si elles sont renouvelées, et 11 % sous la formule fautive de E0, pour une taille de 5 %. À 10 courses par dose : 14 %, 30 % et 35 %. L'erreur de transmission est donc **du même ordre** que celle que l'erratum 1 a corrigée (constat de la contre-lecture confirmé), mais aucune des deux n'est, à 3 courses par dose, « assez pour rejeter à tort la percolation » au sens d'un rejet fréquent : elles faussent l'intervalle prédit, plus que la décision.
- **Ce qui survit** (sortie v3, C4) : le choix « percolation contre voisins directs » reste juste dans 98,5 à 100 % des cas à 3 courses par dose, quel que soit le modèle de transmission vrai. Le contraste principal de l'épreuve bon marché tient ; c'est sa lettre « sans paramètre » et son critère « sortent de l'intervalle prédit par f » qui tombent.

**Correction.**
- Section 4, C3 de la pièce, et liste des hypothèses de l'erratum 1 : ajouter deux hypothèses aux quatre. (5) **Corrélation des pertes entre les deux moitiés** (commune, partielle ou indépendante). (6) **Règle de renvoi et nombre de tours** (une transmission perdue est-elle retentée au tour suivant ? combien de tours à budget égal ?).
- Épreuve de relais E0 : en plus de r(L), mesurer la transmission **conjointe** des deux moitiés le long d'une même chaîne (taux « les deux arrivent » et « une seule »), d'où la part de pertes communes `π̂ = (P(les deux) − f²)/(f − f²)` ; et des chaînes à plusieurs tours, pour savoir si une transmission perdue est retentée. Coût de ces ajouts : non chiffré.
- Prédiction : simuler le **protocole réel** (tours, règle de relais et de renvoi, graphe tiré de chaque course) avec les grandeurs mesurées par E0 ; à défaut, rapporter la **bande** [commune, T tours ; renouvelées, T tours], soit, à f = 0,8 et 4 tours, 0,108 à 0,153, 0,354 à 0,472 et 0,656 à 0,686 aux doses 1, 2 et 4.
- Partout où la pièce ou l'erratum 1 écrivent « sans paramètre libre » ou « sans paramètre ajusté […] sous quatre hypothèses », lire « sans paramètre ajusté sur la courbe de dose, sous six hypothèses posées (erratum 2) ».
- Section 5, H8-a dans l'organisme : « si les composites suivent la courbe des voisins directs ou sortent de l'intervalle prédit par f » se lit « si les composites suivent la courbe des voisins directs, ou sortent de la bande calculée sous le modèle de transmission mesuré par E0 ».
- Erratum 1, phrase « environ 20 % trop bas : assez pour rejeter à tort la percolation », lire « environ 20 % trop bas : l'intervalle prédit aurait été faux ; à 3 courses par dose, un test d'adéquation l'aurait rejeté à tort dans environ 11 % des cas, 35 % à 10 courses (erratum 2, sortie v3, C3) ».

## Mineurs

1. **Test de complémentarité** (Q4-m1, accepté). Texte (section 4) : « séparés puis confrontés contre le meilleur des deux extrêmes ». Choisir le comparateur après lecture gonfle l'erreur de première espèce. *Correction* : test d'intersection et d'union (battre chacun des deux extrêmes au niveau α ; Berger 1982, *Technometrics* 24(4), 295-300, référence de la contre-lecture, conforme à ce que je sais, non revue ici).
2. **Taille décelable optimiste** (Q4-m2, accepté). La partie D de la v1 suppose t* connue exactement ; elle est estimée (pic de susceptibilité) et endogène. *Correction* : propager l'incertitude de t* (rééchantillonnage du pic) ; lire 12,1 % et 8,4 % comme des minorants de la taille décelable.
3. **Survente** (Q4-m3, accepté). Texte : « Percolation des composites (C3, H8-a dans l'organisme) ». Le recouvrement des composites est une conséquence du monde conçu (moitiés réparties entre agents) ; le confirmer éprouve la fidélité de relais et le protocole, non qu'une transition « fait naître » des idées dans la science. *Correction* : « épreuve de relais et de connectivité de l'organisme, outil de conception ; non une épreuve de l'hypothèse d'émergence H8-a ». Le verdict (« prédiction de percolation […] dans l'organisme ») et la section 5 se lisent ainsi.
4. **Graines de la v2** (trouvé ici, mineur). `simulation-emergence-organisme-v2.py` prend `SeedSequence(20261124, spawn_key=(3,))` en le disant « arbre distinct de la v1 » ; or la v1 fait `SeedSequence(20261124).spawn(4)`, dont le quatrième enfant a la clé `(3,)` : c'est la graine de la partie D de la v1, et les cellules `(3,0)` à `(3,2)` de la v2 recouvrent les trois premières cellules de la partie D (vérifié : mêmes états générés). Les calculs étant différents, aucun chiffre ne change ; mais les deux tâches partagent leurs flux, contre la règle R9 (graines dérivées par tâche). *Correction* : lire « arbre recouvrant la partie D de la v1 » ; la v3 prend la clé `(5,)`, qu'aucun script du dossier n'emploie.

## Conséquence sur le verdict

L'ordre des épreuves est maintenu (réplique sur OpenAlex ; épreuve de relais puis courbe de dose ; contraste séparés contre interaction), confiance 0,7. L'épreuve bon marché garde son contraste principal (percolation contre voisins directs, discriminé dans plus de 98 % des cas sous tous les modèles calculés) ; sa prédiction chiffrée devient une bande, ou une simulation du protocole réel sous un modèle de transmission mesuré par une E0 élargie. Elle reste une épreuve de l'organisme (relais, connectivité), non de H8-a. Le coût de l'épreuve de relais élargie n'est pas chiffré ici. Toute question neutre ou tout devis du collisionneur qui reprendrait « la courbe de percolation sans paramètre » doit porter ces réserves.
