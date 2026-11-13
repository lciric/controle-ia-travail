# État de l'art vérifié sur sources primaires — niveau 3 — v1 (synthèse finale)

Date : 2026-11-13, 18:21 UTC (heure relevée par `date -u`). Écrite par un lecteur neuf (sous-agent, Claude Fable), qui n'a
écrit ni le programme, ni les décisions, ni aucun des rapports qu'il assemble. Mandat : mot de Lazar du 13 novembre
(`registres/decisions.md`, R-2555, point D). Journal des sources, des empreintes et des contrôles :
`etat-de-l-art-verifie-niveau3-v1-journal.md`, à côté de ce fichier.

**Ce que ce document est.** L'assemblage des vingt-sept rapports scellés du niveau 3 (quinze de la session sans réseau,
douze de la session à réseau ouvert), de la lecture de veille du 13 novembre et de sa contre-lecture. Il remplace, pour
la lecture, la synthèse provisoire 1 (`8adb561d…`) et son complément 1 (`a4176d46…`), qui restent archivés sans
modification. Il complète les niveaux 1 et 2 et ne les remplace pas.

**Ce que ce document n'est pas.** Je n'ai rouvert aucun PDF : chaque page citée ici est celle que donne le rapport
nommé, dont les citations ont été contrôlées par script par son auteur (zéro échec déclaré partout). Je n'ai contrôlé
que les rapports eux-mêmes, par leur empreinte et par lecture.

**Règles de lecture.**
- « Libre dans les pièces lues » veut dire « non trouvé dans les pièces lues », jamais « trou du champ » (R8).
- Aucun chiffre sans page et sans rapport (R7). Pour les billets (lots 2-A et 2-B), la « page » est le numéro de ligne
  du rendu texte du billet, noté « l. ».
- Tout ce qui vient d'un moteur de recherche (rapports D1, D2, D3) est une piste non opposable.
- **Ce document ne tranche aucune revendication.** Quatre collisions partielles sont en cours de décision (R-2555,
  point B (a)) : la décision est annoncée, ses textes ne sont pas encore écrits, contre-lus ni scellés dans
  `docs/decisions/`. Les verdicts ci-dessous décrivent ce que les pièces occupent ; ils ne disent pas ce que le
  programme revendique après décision.

**Renvois.** B1, B2, B3, C1 à C9, D1 à D3 : rapports sous `docs/etat-de-l-art/niveau3-v1/rapports/` (branche
`prep/etat-de-l-art-niveau3-v1`). S-1, S-2A, S-2B, S-3A, S-4A, S-5A, S-5B, S-7A, S-7B, S-7C, S-7D, S-12 : rapports des
lots de même numéro sous `docs/sources/lecture-pdf-niveau3/` (branche `prep/etat-de-l-art-niveau3-pieces-v1`). V1 :
`docs/notes/lecture-veille-2611.04556-influence-inter-agents-v1.md` ; V2 :
`docs/notes/contre-lecture-veille-2611.04556-v1.md`. Un nombre à dix chiffres avec un point (2610.12445) est un
identifiant de prépublication sur arXiv.

**Échelle des verdicts** (celle du mandat) : « occupé », « occupé en partie », « voisin », « libre dans les pièces
lues ». Quand un énoncé a un socle déjà cédé par le programme et une pièce encore tenue, les deux sont donnés.

---

## 1. Prononcés

1. **Aucun énoncé du programme n'est trouvé occupé en entier** dans les pièces lues. Ce résultat est celui que le
   programme préfère ; il est donc à lire avec la section 9 (ce qui n'a pas été lu) sous les yeux (R4).
2. **Quatre collisions partielles sont constatées sur source et sont en cours de décision** (R-2555) : l'organisme
   d'idéation (O2, O11) ; HC2 ; la statistique de population du papier B ; H9. Détail en section 7.
3. **Deux énoncés sont plus occupés que ne le disait la synthèse provisoire** : O2 (trois composantes sur quatre selon
   S-4A, contre deux et une « dans son principe » selon C7) et la forme de l'attaque de Goodhart O12 (occupée en partie
   par une pièce du 3 novembre 2026, S-4A). H1 a un précédent élargi (deux bancs, faux positifs égaux à 1 %, S-3A).
4. **Aucune bascule et aucune porte n'est déclenchée** par les pièces lues (section 6). L'histoire des versions de
   NARCBench, qui date l'annonce du séquentiel, n'a pas été lue (lot 10-A non rendu).
5. **Le texte envoyé au fonds contient des erreurs de fait** sur des travaux d'autrui : trois selon B1, deux et une
   formulation à restreindre selon C2 (section 8). Le socle de preuves demande quatre corrections (B3).
6. **Des contre-indices publiés existent contre plusieurs prédictions du programme** : H1 au seuil de 1 %, H2 (poids
   de l'accumulation), H9 (forme de la décroissance), HC1 (destination, stabilité de rang), HC4 (« le contexte seul n'y
   suffit pas », « gratuitement »), HC5 (paraphrase), HC6, critère de la porte G2. Ils sont listés sous chaque énoncé.
7. **Le complément 1 a été contrôlé contre les rapports 7-B, 7-C et 7-D** : ses verdicts et ses pages tiennent ; il
   omet des contre-indices et une de ses phrases sur H9 est trop favorable (section 10).

---

## 2. Papier A — le temps

### H1 — gain de la boîte blanche sur la boîte noire, sabotage diffus, tâches floues

- **Verdict : occupé en partie.** Le gain « en général » est déjà cédé par le programme. Il est maintenant publié sur
  du sabotage d'agent, étape par étape, à taux de faux positifs égal. **La mesure sur du diffus et du flou, à
  agrégation égale sur la trajectoire : libre dans les pièces lues.**
- **Pièces.**
  - 2610.12445 (FAR.AI ; version 1 du 8 octobre 2026 « Caught in the Act », version 4 du 20 octobre « Telling FIBS ») :
    sondes contre moniteurs boîte noire sur SHADE-Arena puis BashArena, par étape, à 1 %, 2 % et 5 % de faux positifs ;
    le diffus est écarté du banc (version 1 : p. 6, 19, C5 ; version 4 : p. 8, 26, 28, 34, S-3A).
  - 2512.07810, 2606.17478, 2610.04575, HELIOS (2604.01151 version 5) : chacun un morceau de la comparaison (C1).
  - 2610.17301 : comparaison à 10 % de fausses alertes sur un acte unique, tests préenregistrés ; n'occupe ni H1 ni H2
    (p. 3, 5-6, 8-9, S-7A).
  - Billet long de l'institut britannique de sécurité de l'intelligence artificielle, 10 juillet 2025 : sonde contre
    moniteur boîte noire sur une sous-performance d'agent, en aire sous la courbe seulement, 74 % contre 97 à 99 %
    (l. 193 et 195, S-2A) ; lecture dure du lecteur : « occupé en partie » pour cette seule composante.
  - Aucun billet lu ne compare à faux positifs égaux sur du diffus (S-2A, section 5).
- **Contre-indices publiés.**
  - À 1 % de fausses alarmes sur du désalignement agentique : boîte noire 0,571, sonde linéaire 0,000 (2606.17478,
    p. 30, C1).
  - Dans le voisin le plus favorable, la sonde ne bat pas le seul moniteur d'interface qui a un seuil à 1 % : 64,5
    contre 65,1 (2610.12445 version 4, p. 26, S-3A) ; seuil réglé dans l'échantillon, moniteurs privés du raisonnement
    (p. 8, S-3A) ; un moniteur refuse 2 638 des 5 014 étapes positives (version 1, p. 7, D1).
  - Sondes à 0,585–0,781 sur un modèle de 2 milliards de paramètres, 0,963–0,986 à partir de 27 milliards (2610.12445
    version 1, p. 8, C5) ; le programme travaille à 8 milliards.
  - Un classifieur de texte entraîné sur le même préfixe égale la sonde : 0,98 contre 0,96 (2610.40588, p. 9, S-7A) ;
    les comparaisons préenregistrées « tous négatifs » ne passent pas (2610.17301, p. 5, S-7A) ; un sac de mots atteint
    96,5 % là où la sonde publiée annonçait 95,1 % (2607.13346, p. 7, C8).
  - Sondes muettes sur le modèle qui sous-performe sur une tâche d'agent (2512.07810, p. 17-18, B3 et C1) : c'est de la
    sous-performance verrouillée par mot de passe, pas du sabotage ; contre-résultat partiel ; sondes moyennées sur les
    jetons.
  - Un seuil réglé pour 10 % réalise 18,67 % au test (2610.04575, p. 6, C1).
  - Opinion du cadre de référence : la surveillance « seems […] less promising » contre le diffus (2606.08892, p. 2,
    B3) ; c'est une prémisse des auteurs, maintenue dans la version 3 publiée (S-5B).
- **Phrase pour un jury.** « Le gain des sondes sur un moniteur de texte est publié pour du sabotage d'agent noté étape
  par étape, à 1 % de fausses alarmes ; le banc le plus proche écarte lui-même le sabotage étalé. Personne, dans ce que
  nous avons lu, ne le mesure quand aucune étape prise seule n'est étiquetable, et deux bancs publiés montrent qu'au
  seuil strict la sonde peut perdre. »

### H2 — accumulation additive toujours valide de scores de sondes de l'agent (énoncé de N-007)

- **Verdict : occupé en partie.** Chaque morceau a un titulaire ; **la conjonction (scores de sondes de l'agent,
  accumulation, garantie uniforme sur l'horizon calibrée sur épisodes honnêtes, sabotage par l'agent sous le seuil par
  action) est libre dans les pièces lues.**
- **Pièces.**
  - États internes accumulés, sans garantie, autre menace : SafeDream, 2604.16824, somme cumulée de Page sur un score
    tiré de l'état caché (p. 4-5, 7, C1). À ajouter aux motifs de N-007 (C1).
  - Garantie en boîte noire sur trajectoires d'agent : E-valuator, 2512.03109 (p. 1, B3 ; p. 4, 8, C2) ; CURA,
    2608.27808, somme cumulée, fausse alarme certifiée, calibrage sans exemple d'échec, variante valable à tout instant
    (p. 1, 3, 4, 16, C8) ; 2608.02464 (p. 4, 5, C8).
  - Somme cumulée de scores sous le seuil par événement, en boîte noire : 2606.20746 (p. 1, 4, 6-9, 13, S-5A) ;
    2606.04141, cumul d'un critique textuel à côté d'une sonde jamais cumulée (p. 4-7, S-5B).
  - Configuration de référence de l'énoncé (seuil par action à 1 % sur sondes de l'agent, maximum sur la trajectoire,
    aucun lissage) : billet de LessWrong du 30 octobre 2026 (l. 136, 252, S-2A). Billet rejeté par la modération du
    site et issu d'un travail de deux semaines (l. 43, 168, S-2A).
  - Annonces sans résultat : HELIOS version 5 (p. 3, 18, 19, 26, C1) ; 2610.17301 annonce des seuils conformes sur
    lectures internes (S-7A) ; l'institut britannique annonce une accumulation entre échantillons (billet, note 10,
    l. 407, S-2A).
- **Contre-indices publiés.**
  - Un seuil unique calibré égale un test séquentiel et alerte plus tôt (2607.02510, p. 1, 3, C5).
  - L'accumulation n'apporte qu'« about a quarter » du gain (2606.12476, p. 2, C8) ; elle amplifie une marge présente
    sous le seuil, elle n'en crée pas (2606.20746, p. 8-9, S-5A).
  - Rappel de 42,3 % seulement pour une fausse alarme réalisée de 0,066 (CURA, p. 1, C8) ; la fausse alarme réalisée
    triple sous un autre régime (p. 7, C8) ; la dérive lente échappe aux moniteurs par pas (2608.02464, p. 12, C8).
  - Un seuil par appel se compose : 59 % des épisodes bénins alarmés, et 29 % au lieu d'environ un sur vingt quand le
    seuil par épisode est transporté (2610.40588, p. 10, S-7A) ; de 26 à 43 % des trajectoires honnêtes sonnent avec un
    seuil par action à 1 % (billet du 30 octobre, l. 136, S-2A).
  - Le cumul sans modèle (maximum glissant, historique entier) dégrade la détection (2609.06966, p. 27, 38, 40, S-5B).
  - La seule somme cumulée publiée sur scores internes mesure 6,6 à 8,0 % de fausses alarmes (SafeDream, p. 5, 7, C1).
  - Le détecteur de rupture par e-valeurs garantit une durée moyenne avant fausse alarme, pas une probabilité sur
    l'épisode (2203.03532, p. 7, 8, C6) : à tenir au préenregistrement de G1.
- **Phrase pour un jury.** « La somme cumulée sur états internes existe sans garantie et contre une autre menace ; la
  garantie à tout instant existe en boîte noire. Leur réunion sur les sondes de l'agent, contre un sabotage tenu sous le
  seuil, n'est pas trouvée, et l'équipe de NARCBench l'annonce. Les mesures voisines disent que l'accumulation pèse peu
  quand le score par pas est faible : c'est le risque que nous mesurons. »

### L — lemme d'additivité (énoncé de N-004)

- **Verdict : occupé en partie.** Le cœur statistique est classique et maintenant porté sur PDF. **L'énoncé adverse à
  budget total borné (invariances exactes dans le temps et entre agents, borne fonction du seul budget, chiffrage) et sa
  mesure sur scores de sondes : libres dans les pièces lues.**
- **Pièces.** Borne supérieure par la divergence : 2608.02698 (p. 5, C2). Critère sous garantie toujours valide :
  2208.07610 (p. 2, 6, C2). Seuil sur épisodes honnêtes entiers : 2512.03109 (p. 4, 8, C2). Dommage cumulé avant
  détection : 2601.20022 (p. 4, 10, 11, C2). Borne de mélange : 2210.01948 (p. 13, C6) et 1810.08240 (p. 9, 10, 28, C8).
  Dichotomie somme contre maximum : 1007.1434 (p. 2-3, 6-7, 13, 17-18, C8). Prix de la garantie et coût du report,
  antécédent qualitatif : 2203.03532 (p. 8, C6). Voisins en boîte noire : 2605.11135 (p. 8, 9, 16, 17), 2606.20746
  (p. 1, 4, 6, 7, 9) (S-5A). Précédents conceptuels en billets (budget additif, nombre contre discrétion) : S-2A.
- **Contre-indices et réserves.** Aucune des deux sources classiques n'écrit « la puissance ne dépend que du budget
  total » ; le fait est porté sous forme quadratique à horizon fixe (1007.1434, p. 2, 6-7, C8). Les composantes libres
  sont élémentaires ; l'originalité « environ 0,4 » de N-004 est jugée un plafond par C2 et par C6.
- **Phrase pour un jury.** « Le cœur statistique est classique et nous le citons. Notre apport est l'énoncé adverse à
  budget total borné et sa mesure sur des activations ; il est modeste sur le plan mathématique. »

### T — théorème négatif (énoncé de N-003)

- **Verdict : occupé en partie.** **Les quatre pièces de N-003 (classes « multi-ensemble » et « marginales » et leurs
  signes, impossibilité par rebrassage sur un groupe, garanties des statistiques locales, écriture commune du temps et
  des agents) et la mesure sur activations : libres dans les pièces lues.**
- **Pièces.** Contraste marginale contre corrélation, un agent, boîte noire, avec un attaquant adaptatif à un
  paramètre : 2606.10456 (p. 1-4, 6-7, C2). Moitié négative entre agents : 2607.11751 (p. 3, 10, C2). Principe
  d'invariance, classique : 2208.07610 (p. 2, 8, C2). Parade publiée comme outil (test séquentiel d'indépendance entre
  deux flux) : 2212.07383 (p. 3, 7, 8, C6). Voisin fort, théorème d'existence en boîte noire par un autre mécanisme :
  2605.11135 (p. 7-10, S-5A).
- **Contre-indices et réserves.** L'attaquant adaptatif contre l'autocorrélation est déjà montré, dans une forme
  restreinte (2606.10456, p. 6-7, C2) ; l'unification temps et agents est une mise en forme qu'un statisticien peut dire
  connue (C2). Non lu : Koning, 2310.01153 (invariance de groupe par e-valeurs), à confronter à cette unification
  (lot 8, section 9).
- **Phrase pour un jury.** « Zhang et Gao l'ont posé avant nous pour un agent, en boîte noire. Ce qui nous sépare : la
  distinction entre préserver le multi-ensemble des scores et préserver la loi de chaque pas, l'écriture commune du
  temps et des agents, et la mesure sur activations. »

### H6 — marge asymétrique (énoncé après N-013 et N-015)

- **Verdict : libre dans les pièces lues sur PDF.** Une lecture dure sur billet reste à trancher : « occupé en partie
  pour le rééchantillonnage, en sabotage concentré » (S-2A).
- **Pièces.** Billet de Redwood Research du 29 mai 2026, résumé de 2605.26047 : gain de sécurité de 10,2 points sans
  coût d'utilité quand le rééchantillonnage sert d'information (l. 120, 122, S-2A) ; le gain passe par l'audit, non
  par une chute du succès de l'attaque ; cadre concentré. Le PDF 2605.26047 est au dépôt et n'a pas été relu contre H6.
  Voisins : 2609.03035 version 2 (p. 9, S-7B) ; 2606.08892 version 3 (p. 8, 10, 84, S-5B). Rien dans C5, C8, D1.
- **Phrase pour un jury.** « Non trouvé dans nos lectures sur PDF ; un résultat voisin sur le rééchantillonnage en
  sabotage concentré est à lire contre cette hypothèse. Non prioritaire. »

### Tr — transposition du jeton à l'action

- **Verdict : libre dans les pièces lues ; voisins.**
- **Pièces.** Agrégations au niveau de l'action sans attaquant adaptatif : 2610.17301, 2610.40588, 2610.39377 (S-7A) ;
  2610.12445 (p. 3, C5) ; billets (maximum par action puis par trajectoire, l. 136, 252, S-2A).
- **Non lu.** « What the Monitor Saw » (atelier de NeurIPS 2026 ; activations du moniteur, mise en commun et
  combinaison des preuves) : PDF refusé par le site (section 9).
- **Phrase pour un jury.** « Angle mort que nous avons nommé ; une pièce voisine n'a pas pu être obtenue. »

### H8 — la validité du construit prédit la robustesse

- **Verdict : occupé en partie** pour le socle (ce que lit la sonde décide où elle échoue ; lien construit → tenue du
  seuil hors distribution, publié). **La prédiction de la robustesse adverse par un construit mesuré d'abord, sur l'axe
  intention contre conscience d'évaluation : libre dans les pièces lues.**
- **Pièces.** 2611.10620 : la sonde lit la consigne, pas la décision (aire sous la courbe par agent de 1,00 à 0,61,
  p. 15) ; la sonde « consigne » alarme 21 % et 28 % des contrôles quand la sonde « décision » garde son seuil (p. 19)
  (S-7B). 2610.17301 : construit identifié, échec sous injection prédit puis observé, sur un cas (p. 37, S-7A).
  2609.10739 (p. 1, 4) et 2607.13346 (p. 1, 4, 7) (C8). 2610.12445 (p. 10, C5 et S-3A), 2606.30449, 2610.37679,
  2610.18408, 2606.12618 (S-3A). Billets : S-2A.
- **Contre-indices.** Une sonde parfaite en validation peut s'inverser sous tromperie : aire de 0,006 (2609.10739, p. 1,
  C8).
- **Phrase pour un jury.** « Que les sondes lisent la consigne ou la situation plutôt que l'intention est décrit par
  plusieurs équipes, et le lien avec la tenue hors distribution est publié. Prédire la robustesse face à un adversaire
  à partir du construit mesuré ne l'est pas dans nos lectures. »

---

## 3. Papier B — l'essaim

### Statistique de population (co-élévation des états internes entre copies ; statistique spatio-temporelle)

- **Verdict : occupé en partie — collision en cours de décision (R-2555).** La coupe transversale entre agents est
  occupée. La forme « temps × agents » sur scores de sondes est posée. **Une statistique conjointe à garantie toujours
  valide, sur horizon long, démontrée supérieure au séquentiel par agent et à la coupe à fausses alarmes égales, sous
  adversaire : libre dans les pièces lues.**
- **Pièces.**
  - Coupe transversale : HELIOS, 2604.01151 version 5 (C1 ; registre R-622) ; billet de NARCBench du 3 avril 2026
    (l. 96, 100, 112, S-2B).
  - États internes, paire, cumul sur les tours : 2611.02153 (J-PACT), score relationnel sur représentations internes
    d'instances d'un même modèle, moyenné sur les tours, sans sonde, quatre agents, sans garantie (p. 2, 3, 4, 6, 7, 9,
    S-7B).
  - Grille temps × agents sur scores de sondes : 2611.10620, trois cumuls temporels croisés avec quatre règles entre
    agents, alarme en ligne à seuil conforme ; aucun résultat imprimé pour la moyenne cumulée ni pour la somme cumulée
    (p. 11-12, 14, 21, S-7B).
  - Squelette en boîte noire : 2601.05427, un processus par agent à garantie toujours valide, combinés à un temps
    d'arrêt commun (p. 4-6, 31, 34-36) ; 2605.11135, statistique de population suivie par carte de contrôle (p. 2-4, 10,
    18) (S-5A).
- **Contre-indices publiés.**
  - Critère de la porte G2 : à sonde égale, le maximum par agent fait aussi bien que les statistiques de groupe —
    rappel à 1 % de fausses alarmes de 0,86 pour le pic, 0,85 et 0,76 pour les deux balayages (2611.10620, tableau 3,
    p. 14, S-7B).
  - Le score de paire reste sous les sondes supervisées agrégées par agent : 0,921 contre 0,993 (2611.02153, p. 7,
    S-7B).
  - Rappel de 0,38 à 1 % de fausses alarmes sur le transfert (HELIOS version 5, p. 18, C1 et B3).
  - À 8 milliards de paramètres, un billet du 26 juillet 2026 ne trouve qu'un signal mince sur NARCBench-Core, et un
    classifieur sur les mots de la consigne sépare les conditions (S-2B, section 5.3) : à lire avant le devis de la ligne
    NARCBench de N-061.
  - Sans le modèle, quatre traits de surface atteignent 0,883 d'aire sous la courbe (2611.10620, p. 16, S-7B).
- **Phrase pour un jury.** « Deux prépublications de novembre 2026 posent un score sur les états internes d'agents à
  modèle partagé, cumulé sur les tours. Aucune ne donne un test toujours valide ni un résultat pour la somme cumulée, et
  la seule comparaison à sonde égale ne trouve aucun gain de la statistique de groupe sur le maximum. Ce qui reste est
  étroit, et son signe n'est pas acquis. »

### H3 — courbe de sécurité selon le nombre d'agents, à budget constant

- **Verdict : occupé en partie.** Boîte noire : occupé (cédé par le programme). Boîte blanche : occupé en partie.
  **Les deux courbes comparées à budget total constant : libres dans les pièces lues.**
- **Pièces.** Boîte noire : FakeLab, 2607.07368 version 2 (p. 8, 14, 55, S-3A) ; 2610.24052, 87 % de détection pour un
  agent seul contre 7 % par agent pour une équipe (p. 1, 5, 18, S-7B) ; 2609.19587 (p. 7, 8, C5 ; billet, l. 204, 206,
  S-2B) ; 2605.11135, en simulation (p. 18, 19, S-5A). Boîte blanche : HELIOS version 5, deux points, 0,88 à 4 agents
  et 0,737 au mieux à 8 agents (p. 27, 30, C1) ; rappel par taille de coalition de 2 à 7 (2611.10620, p. 21, S-7B).
- **Contre-indice.** La seule série boîte blanche publiée se dégrade quand le nombre d'agents double (HELIOS, ci-dessus).
- **Phrase pour un jury.** « La dégradation avec le nombre d'agents est publiée en boîte noire, et HELIOS montre que la
  boîte blanche se dégrade aussi de 4 à 8 agents. Les deux courbes à budget constant ne sont pas trouvées. »

### H4′ — diversification contre coordination

- **Verdict : libre dans les pièces lues ; voisins. Peu cherché** (D3).
- **Pièces.** Équipes mixtes de deux familles (2609.03035 version 2, S-7B, chiffres non opposables) ; limite reconnue de
  J-PACT sans espace commun entre modèles différents (2611.02153, p. 3, S-7B) ; revue sans expérience (2601.00360, p. 12,
  15) et cadre d'analyse (2608.26626, p. 32) (C9). Piste non lue : Keppo et collègues 2025 (C9).

### H5 — nombre × diversité des moniteurs

- **Verdict : occupé en partie.** **La loi sur un panel de sondes, par matrice de transfert d'attaque : libre dans les
  pièces lues.**
- **Pièces.** Sur 24 juges, la décorrélation ne prédit pas le gain d'un ensemble (2608.16190, p. 1, 9, C5). Matrice de
  co-défaillance entre sondes, hors attaque (2604.13386, p. 3, 5, C9). Une sonde contre dix sous pression
  d'optimisation (2510.21531, p. 1, 7, 9, C9). Transfert entre trois architectures de moniteurs (2609.36490, p. 8, B1).
- **Contre-indices.** Gain de la diversité « minimal » sous pression, une seule graine (2510.21531, p. 1, 9, C9) ; cinq
  sondes de même type tombent ensemble (2602.00750, p. 1, C9) ; la famille de modèles n'ajoute rien, c'est la diversité
  des entrées qui compte (2610.29178, S-7C).
- **Phrase pour un jury.** « Le résultat existe sur des juges et il est contraire à l'intuition ; sur un panel de
  sondes, l'instrument existe hors attaque, pas la loi. »

### H7 — riposte et fuite d'information

- **Verdict : occupé en partie** (mécanisme, comparaison de politiques de retour, niveaux d'information comparés sur
  sondes). **La mesure de la fuite, la pente d'adaptation et la prédiction de l'une par l'autre : libres dans les pièces
  lues.**
- **Pièces.** Billet de Hopman, Lemoine et Tracy, 27 mai 2025 : mécanisme et trois politiques de retour comparées
  (l. 60, 251, S-2B) ; antérieur de seize mois à 2609.36490 (p. 1, B1), que N-013 cite pour le mécanisme. 2609.03035
  (version 1 : p. 6, 9, C5 ; version 2 : S-7B). 2610.26935 (p. 1, C5). STACK, 2506.24068 (p. 5, 10, 24, C9). 2610.24052
  (p. 9, 23, S-7B).
- **Contre-indices.** Après une riposte connue, la réussite conjointe des deux objectifs tombe de 77 % à 12 %
  (2610.26935, p. 1, C5) : rendre de l'information n'aide pas toujours l'attaquant. Les chiffres de 2609.03035 ne sont
  pas opposables : les rappels à seuil fixe ont été remplacés de la version 1 à la version 2 sans explication (S-7B,
  section 3.2).
- **Phrase pour un jury.** « L'effet de l'information rendue à l'attaquant est mesuré, et parfois de signe contraire à
  notre prémisse ; sa prédiction par une mesure de fuite ne l'est pas. »

### H9 — survie d'une contrainte de sécurité à la délégation (N-035)

- **Verdict : occupé en partie, sur le cœur de l'énoncé — collision en cours de décision (R-2555 : repli (b) de
  N-035).** La réserve d'antériorité de N-035 est confirmée.
- **Par composante** (S-7D, section 7 ; S-12, section 4).
  - Le phénomène : occupé — MasDrift, 2608.07556 version 3 du 15 octobre 2026 (p. 1, 6, 7) ; Sun et collègues,
    2608.24569 version 2 ; Hammond, 2502.14143 (p. 24, C6) ; AgentCollabBench, 2605.08647 version 1 du 9 mai 2026 (S-12).
  - La mesure par passage : occupé en partie — premier relais fautif localisé (MasDrift, p. 6, 23) ; taux de perte
    conditionnel par relais sur chaînes linéaires, pour un identifiant témoin et non pour la force d'une contrainte
    (AgentCollabBench, tableau 23, p. 34, S-12).
  - La décroissance avec le nombre de passages : occupé en partie, avec contre-indice.
  - Un moniteur qui relève la survie : occupé en partie — deux défenses comparées à l'absence, dont une politique
    portée à chaque relais (MasDrift, p. 5, 6, 22, S-7D).
  - Les confondants : occupé en partie ; la longueur du contexte n'est séparée nulle part.
  - Aucune des sept pièces ne lit un état interne ; **l'énoncé de H9 ne le demande pas non plus** (S-7D).
- **Libre dans les pièces lues.** Un moniteur qui lit chaque passation, traité comme facteur croisé avec la profondeur ;
  le profil du taux de perte par rang de relais, sur chaînes de longueur contrôlée, pour la force d'une contrainte ;
  l'érosion sous un agent qui sabote ; la lecture interne du sous-agent (hors de l'énoncé actuel).
- **Contre-indices publiés.** 88,2 % des premières pertes sont au premier relais (MasDrift, p. 23) ; la perte « does
  not order by depth » (p. 6) ; ce sont les actions non autorisées qui montent avec la profondeur, de 2,7 % à 19,8 %
  (p. 2) ; corrélation perte–violation de −0,26 sur 40 cellules (p. 22) (S-7D). La politique portée à chaque relais
  supprime les violations mais bloque jusqu'à 54,5 % des appels requis (p. 6, S-7D). La décroissance est déjà la forme
  publiée pour l'information : de 96 % à moins de 60 % en huit récritures (Hammond, p. 24, C6). Les taux par relais
  d'AgentCollabBench (3 à 40 % selon le modèle, p. 34) restent compatibles avec un risque à chaque relais : les deux
  lectures ne sont pas départagées (S-12).
- **Réserves sur MasDrift** (S-7D) : une trajectoire par cellule, sans intervalle ; un tableau dont les effectifs ne se
  recoupent pas ; versions 1 non lues, donc date de première parution non établie au-delà des dates imprimées.
- **Phrase pour un jury.** « La perte d'une contrainte au passage entre agents est mesurée par d'autres depuis 2026, et
  elle se produit surtout au premier relais. Nous n'en revendiquons pas la mesure. Ce qui n'est pas trouvé : un moniteur
  qui lit chaque passation, croisé avec la profondeur, et le profil de la perte par rang de relais. »

---

## 4. Papier C — l'instrument

### HC1 — loi de déférence, et porte GC

- **Verdict : occupé en partie, plus qu'au niveau 2.** La forme à destination imposée et le phénomène sont occupés
  (déjà cités comme publiés). **La pièce revendiquée — destination libre testée contre la cible de l'attaquant et
  contre la moyenne du corpus, par famille, dans un moniteur de contrôle, et l'opposition juge contre sonde — est libre
  dans les pièces lues. La porte GC n'est pas déclenchée** (C3, C9, S-7C, V2).
- **Pièces.**
  - Forme à destination imposée : Panin, SSRN 7424179 (p. 2) ; loi linéaire ajustée en cadre adverse, « descriptive R2
    ranges from 0.851 to 0.982 » (2603.15809, p. 17 ; aussi p. 15) (C3).
  - Régressions sur des intensités, hors moniteur : 2602.13568 (p. 3-5, C3) ; 2608.25869 (p. 1, 6, 7, C5) ; courbes
    dose-réponse sur dix tours pour neuf juges, sans régression ni gain (2608.12645, p. 4, 6, 8, 9, S-7C).
  - Moniteurs de contrôle déplacés, en taux binaires : 2607.08066, lue en entier, aucune loi (p. 4, C3) ; 2611.04556,
    trois capacités, 18 paires de modèles, plus un score continu de dérive (p. 6, 31-32, V2) — citée comme publiée par
    décision (R-2554), sans changement d'énoncé.
  - Test binaire de la destination : 2606.05384 (p. 2, 5, C9).
  - Voisins : 2609.20211 (p. 4, 5), 2610.29178 (p. 11, 13), 2603.19262 (S-7C) ; 2507.08794 (p. 7, 9, 26, 31, S-5B) ;
    billets (S-2B), dont une sixième voie d'attaque, l'affaiblissement d'argument, absente des cinq familles.
- **Contre-indices publiés sur les prédictions.**
  - Prédiction 1 (destination = cible) : les juges se renversent (0,194) mais pas vers la cible nommée, écart signé de
    −0,018 ; deux juges d'une famille, verdict binaire (2606.05384, p. 2, C9). En réseau non adverse, la destination
    est le biais propre du modèle (2606.18276, p. 1, 8, C3).
  - Forme : poids du conseil presque binaire dans trois modèles sur cinq (Panin, p. 6, C3) ; réponse « à seuil », pente
    proche de zéro (2608.25869, p. 1, 6, C5) ; dose concave, en logarithme (2602.13568, p. 3, C3).
  - Prédiction 3 (stabilité de rang) : les rangs ne se transfèrent pas d'un corpus à l'autre (2608.12645, p. 9, S-7C) ;
    le rang des cibles s'inverse entre deux environnements pour un même attaquant (2611.04556, p. 58-59, 11, V2) ; le
    taux de bascule d'un même juge va de 0,0 % à 87,6 % selon la consigne (2507.08794, p. 9, 31, S-5B).
  - Gain instable jusqu'au signe, et proche de zéro sur les modèles forts (Panin, p. 7, 11, C3) ; déplacements négatifs
    sur un juge textuel (2611.04556, p. 58, V2).
- **Phrase pour un jury.** « Nous n'apportons ni la forme ni le phénomène. Nous apportons le test de la destination,
  par famille d'attaque, dans des moniteurs de contrôle, face à des sondes. Un test binaire voisin de notre prédiction
  centrale existe et il est négatif, sur deux juges ; nous rapportons donc la distribution et pas seulement la pente. »

### HC2 — robustesse des sondes au contenu

- **Verdict : occupé en partie — collision en cours de décision (R-2555).** **Reste libre dans les pièces lues : la
  sonde qui lit l'agent auteur et adversaire, le déplacement continu en fonction de l'intensité, la comparaison aux
  juges sous les mêmes attaques.**
- **Pièces.** MIRAGE, 2606.10304 version 1 : aucune évasion conjointe au seuil par défaut d'une sonde à maximum
  glissant lue pendant la génération d'un agent victime d'injection (p. 1-2, 4, 7, 12, 18-20, S-1). Karne, 2609.05797
  version 3 : voisin, contre-indice sur le versant « sonde du lecteur » (p. 1, 5, 6, 22, S-1). Trois articles sous
  injection lisent un agent victime, sans attaquant adapté (2610.37679, 2611.11172, 2610.18408, S-3A) ; le plan apparié
  existe déjà côté lecteur (2610.18408, p. 4, 12, S-3A). Aucun billet ne met une sonde sur un agent auteur d'un contenu
  destiné à déplacer son moniteur (S-2B, section 0.1).
- **Chiffres de MIRAGE non opposables** (S-1) : sur 120 essais, 6 produisent une exfiltration réussie (p. 20) ; « 0
  évasion sur 120 » vaut « 0 sur 6 » ; l'attaquant n'itère pas ; sans adversaire, 23 attaques conformes sur 54 échappent
  à la sonde (p. 21).
- **Contre-indices publiés.** Une consigne en langage naturel fait tomber une sonde linéaire lue sur le modèle auteur à
  5–21 % de détection à 1 % de faux positifs, consigne donnée ouvertement, concepts anodins (2608.21664, p. 6, 7, C9).
  Un suffixe dans le contenu évade cinq sondes du lecteur à la fois, 93,91 % et 99,63 %, avec lecture des poids
  (2602.00750, p. 1, C9). Par la consigne seule, le rappel à seuil fixe passe de 0,87 à 0,71 puis 0,55, l'aire sous la
  courbe bougeant peu (2611.10620, p. 22, S-7B). Deux lectures internes trompées par une consigne système, succès de
  l'auditeur à 1 % et 1,8 % (2602.08877, p. 17, 18, S-7C ; hors du périmètre strict : pas de sonde de tromperie).
- **Phrase pour un jury.** « MIRAGE publie une absence d'évasion par le contenu sur une sonde lue pendant la génération,
  avec six essais utiles. Il reste : la sonde qui lit l'agent lui-même adversaire, le déplacement continu, la
  comparaison aux juges. Deux travaux montrent qu'une consigne peut déplacer une sonde ; notre prédiction peut échouer. »

### HC2b — trahison par les activations

- **Verdict : libre dans les pièces lues ; un voisin proche.**
- **Pièces.** Volet « Stego » de NARCBench : la dissimulation se lit dans les activations des agents auteurs (aire sous
  la courbe de 0,90 à 1,00) quand le juge qui lit la table ne distingue rien (billet, l. 124, S-2B) — dissimulation, non
  persuasion. MIRAGE, voisin faible de signe favorable ; Karne, contre-indice indirect sur sonde lectrice (p. 6, 7, S-1).
  Sous consigne de tromper, la lecture interne suit la consigne (2602.08877, p. 5, 6, S-7C). Contrôle du style : sosie
  inoffensif de 2610.18408 (p. 1, 4) et séparation exposition contre engagement de 2610.37679 (p. 1, 7) (S-3A).
- **Phrase pour un jury.** « Non trouvé pour un agent qui tente de persuader son moniteur ; le contrôle contre le style
  est d'autant plus nécessaire que les consignes des bancs voisins se séparent par leurs mots. »

### HC3 — usurpation

- **Verdict : occupé en partie.** Composante 1 (ordres en bande sous le protocole « contenu = données ») : la
  neutralisation est publiée, la détection chiffrée ne l'est pas. Composante 2 : l'influence sans ordre par la voix ou
  le registre est publiée. **L'usurpation du style de l'instructeur sur un juge moniteur, en loi continue, avec le nul
  sur les sondes de l'auteur : libre dans les pièces lues.**
- **Pièces.** 2609.19587 : 79 % d'injections réussies contre deux moniteurs de production (p. 1) ; l'encadrement et
  l'échappement de chaque tour les atténuent (p. 6, 7) (C5 ; billet, l. 164, 172, 180, S-2B). Panin : l'étiquette de
  voix change l'adoption de 0,33 à 0,69 (p. 8, C3). 2509.16533 (p. 7, C3). 2507.08794 : un contenu sans ordre déplace
  des juges jusqu'à 95,1 % (p. 4, 7, 15, S-5B). 2610.17301 : injection signée du nom de l'utilisateur (p. 37, S-7A).
- **Contre-indice.** Sous une consigne « le contenu est une donnée », des juges de 8 à 9 milliards de paramètres
  obéissent encore à des ordres en bande, 0,65 à 0,90 sur un modèle (2610.29178, p. 26, S-7C).
- **Phrase pour un jury.** « L'influence par le seul style est publiée sur des modèles qui répondent ; pas sur un juge
  moniteur qui imite son instructeur. Et séparer le contenu des consignes atténue l'injection sans que sa détection ait
  été mesurée. »

### HC4 — taxe de déplacement

- **Verdict : la comparaison de coût juge contre sonde dans un même cadre est libre dans les pièces lues ; la prémisse
  est entamée des deux côtés.** Le rapport C9 écrit « occupée en partie (points de coût épars) » ; le complément 1
  écrivait « pièce revendiquée libre, prémisse entamée » : même substance, deux mots (section 10).
- **Pièces et contre-indices.**
  - Contre « le contexte seul n'y suffit pas » (lettre de N-013) : 2608.21664 (p. 6, 7, C9) ; 2602.08877, cent
    évaluations au plus (p. 17, 18, S-7C) ; 2611.10620 (p. 22, S-7B) ; Karne, pour une sonde de propriété de l'entrée
    (p. 1, 6, S-1). Régime manquant à la grille de N-013 : lecture des poids sans écriture (2602.00750, p. 3, 4, C9).
  - Contre « gratuitement » côté juge : 507 heures de processeur graphique pour 71 % de succès contre des classifieurs
    durcis (STACK, p. 8, 9, 21, C9) ; environ 76 dollars de recherche sans effet sur un juge de pointe (2610.29178,
    p. 13, S-7C) ; effets de 1,5, 5,0 et 0,7 points seulement à la première réponse du surveillant (2611.04556, p. 63,
    V2).
  - À l'appui de l'axe « accès » : chez MIRAGE l'évasion n'apparaît qu'avec l'écriture dans les activations, 4 familles
    sur 9 (p. 19, S-1).
  - Les trois coûts cités par l'état de l'art v1 (l. 140) restent invérifiables au dépôt (B2).
- **Phrase pour un jury.** « La comparaison de coût avec un juge n'est pas publiée. Notre prémisse, elle, est contestée
  des deux côtés : une consigne suffit parfois à déplacer une sonde, et un juge durci n'est pas gratuit à déplacer. Nous
  l'écrivons par régime d'accès et à durcissement égal. »

### HC5 — contre-mesures

- **Verdict : occupé en partie, davantage qu'au complément.** La matrice de transfert entre juges, la structure de
  co-défaillance et un quorum à moniteur hors de la surface textuelle sont publiés. **Les cellules juge ↔ sonde lisant
  l'agent, et le quorum de juges et de sondes lisant l'agent : libres dans les pièces lues.**
- **Pièces.** 2610.29178 : matrice charge utile × famille de moniteur, par sens ; règle de quorum ; moteur de règles
  ajouté au quorum (p. 1, 12, 14-16, 35, S-7C). 2607.08066 : vérificateur d'une autre famille avant le moniteur (p. 3, 6,
  C3). Billet du 14 septembre 2026 : sonde et verdict d'un même moniteur non fiable combinés dans un jeu de contrôle ; la
  sonde lit le moniteur, pas l'agent (l. 102, 124, S-2B). STACK (p. 1, 9, C9).
- **Contre-indices.** Une réécriture ordinaire entre l'agent et le moniteur efface le statut « non vérifié » d'une
  autorisation : l'approbation d'actions risquées passe de 0,03 à 0,68 (2609.20211, p. 20, S-7C) — contre la paraphrase
  de confiance. Le meilleur moniteur seul n'est pas battu hors échantillon par un ensemble de juges (2608.16190, p. 1,
  C5).
- **Phrase pour un jury.** « Le transfert des attaques entre juges et le quorum avec un moniteur d'un autre type sont
  publiés. Le quorum de juges et de sondes qui lisent l'agent, et sa matrice, ne sont pas trouvés ; et une réécriture de
  confiance peut effacer l'indice qui protégeait le moniteur. »

### HC6 — le déplacement bénin prédit la robustesse

- **Verdict : occupé en partie, au niveau de l'item.** **La prédiction par moniteur de l'effondrement sous attaque
  optimisée par contenu, dans des moniteurs de contrôle : libre dans les pièces lues.**
- **Pièces.** 2608.12645 : mêmes items et juges sous pression scriptée bénigne et sous persuadeur adaptatif ; un
  prédicteur sans pression (force de la majorité d'un jury) (p. 6-8, 10, 12, S-7C).
- **Contre-indices.** Corrélation faible entre les deux, 0,33 à 0,40 (2608.12645, p. 7, S-7C) ; la qualité bénigne d'un juge
  ne classe pas sa robustesse, corrélation de rangs de −0,34 sur dix juges, calcul du lecteur (2507.08794, p. 7, 8,
  S-5B) ; « robustness to overt pressure offers little assurance against deception » (2611.04556, p. 10, V2) ; la
  co-défaillance sans attaque ne prédit pas la co-défaillance sous attaque (2610.29178, p. 15, S-7C).
- **Phrase pour un jury.** « La question est posée par d'autres au niveau de l'item, et la corrélation qu'ils trouvent
  est faible. Notre prédiction par moniteur n'est pas trouvée ; elle doit battre un prédicteur publié. »

---

## 5. Organisme d'idéation — O1 à O20 et rôles de N-065

**Collision en cours de décision (R-2555) : O2 et O11.** Trois rapports portent ces verdicts : C4 (première lecture),
C7 (contre-lecture de Qu, Chen, Wang et du dossier c8), S-4A (neuf articles de 2025 et 2026 sur la validation
statistique d'hypothèses d'agents). **S-4A n'a lu ni C4 ni C7, et réciproquement** : ses lignes « avant » partent de
N-064. Les colonnes ne sont donc pas réconciliées ; je donne le plus dur des verdicts en « verdict final » et les deux
lectures à côté. Clés : QU = Qu, Chen, Wang, 2609.27051 ; MASK = 2610.38392 ; REUSE = 2609.33180 ; PROCTOR =
2609.02246 ; PACE = 2606.08106 ; CONFIRM = 2611.01449 ; CADS = 2610.24597 ; N×N = 2608.06621 ; « Hard to Fool » =
2611.06607 ; Sargsyan = 2511.06701.

| | revendication (abrégée) | C4 puis C7 | S-4A | verdict final |
|---|---|---|---|---|
| O1 | qui produit ne tient pas la clé qui évalue | occupée dans son principe (QU p. 1, 2, 4, 11 ; priorité revendiquée p. 2) | occupée en partie (CADS p. 4, 17 ; Sargsyan p. 10 ; « Hard to Fool » p. 3) | **occupé en partie** (le principe est occupé) |
| O2 | statistique hors des agents, engagement scellé, nul des lois connues, multiplicité | deux composantes occupées, une dans son principe, une absente (QU p. 1, 2, 6, 8-11, 14, 22, 30) | trois composantes occupées, le nul absent ; réunies sans le nul dans CONFIRM (p. 3, 5-6, 14) | **occupé en partie** : seul le nul des lois connues et la conjonction complète ne sont pas trouvés |
| O3 | prédictions scellées avant les données ; tirages semés par l'empreinte | occupée dans son principe (QU p. 2, 10 ; MASK p. 4, 24) | occupée en partie pour le sceau (CONFIRM p. 3 ; « Hard to Fool » p. 3-4) | **occupé en partie** ; le tirage semé par l'empreinte : libre dans les pièces lues |
| O4 | battre un nul formé des lois connues | libre ; verdict « le plus fragile » | non trouvée ; quatre voisins (N×N p. 3 ; 2611.00643 p. 1, 6 ; 2610.11289 p. 2 ; Sargsyan p. 5) | **libre dans les pièces lues — verdict le plus fragile du document** |
| O5, O6, O15 | moisson non opposable ; douane de forme ; bisociateur | non réexaminées | non touchées | **non réexaminés au niveau 3** |
| O7 | juges croisés de plusieurs fournisseurs | voisine | — | **voisin** |
| O8 | proposeurs de plusieurs fournisseurs | libre (QU p. 2) | non trouvée ; contre-indice sur sa valeur | **libre dans les pièces lues** |
| O9 | mémoire sans verdicts | occupée dans son principe (REUSE p. 2 ; QU p. 12, 16) | voisine | **occupé en partie** (principe) ; la forme « aucun verdict » non trouvée |
| O10 | témoins plantés à chaque génération | occupée dans son principe (PROCTOR p. 2), confiance moyenne | voisine (CONFIRM p. 6) | **occupé en partie** (principe), confiance moyenne |
| O11 | banc de tricheurs, validation préenregistrée, mutations | occupée dans son principe sur les trois gestes (QU p. 13, 16, 29 ; PACE p. 6 ; MASK p. 2, 8) | occupée en partie, mutations comprises (2611.04420 p. 5-6 ; CADS p. 9, 23 ; Sargsyan p. 27-29) | **occupé en partie** ; la combinaison et l'ampleur non trouvées |
| O12 | attaque de Goodhart (proposeur modèle qui lit le juge, mondes tout faux) | principe occupé ; forme non trouvée (REUSE p. 32, en théorie) | **forme occupée en partie** (CONFIRM p. 9, 22 ; juge génératif : 2611.00643 p. 1, 10, 12) | **occupé en partie, forme comprise** ; la consigne de tromper, la lecture de la description du juge et le contraste des deux bras non trouvés |
| O13 | épreuves en bac à sable, verdict sur le fichier brut | voisine | occupée en partie (Sargsyan p. 9-11 ; CADS p. 5) | **occupé en partie** (S-4A seul) |
| O14, O16, O18 | sélection par les épreuves ; pont fiche → loi ; discrimination des juges | voisines | — | **voisin** |
| O17 | scellement avant lecture, aucun repli silencieux | occupée dans son principe (MASK p. 4, 24), confiance moyenne | occupée en partie (« Hard to Fool » p. 4) | **occupé en partie** |
| O19 | puissance du juge | occupée dans son principe (REUSE p. 6) | voisine (CONFIRM p. 5) | **occupé en partie** (principe) |
| O20 | juge éprouvé sur vérité plantée | occupée comme méthode (QU p. 14, 15, 22) | occupée dans son principe | **occupé** comme méthode ; restent les chiffres propres |

**Contre-indices publiés.** Sur la valeur des proposeurs modèles (O8) : un tirage au hasard fournit le candidat promu
dans 48 % et 46 % des paires (2611.04420, p. 8) ; un a priori fixe sans modèle domine les trois modèles (CADS, p. 11)
(S-4A). Sur la tenue d'un préenregistrement (R1) : un instrument faux « was locked in before any data were collected
and passed three confirmation stages » (2611.00643, p. 16, S-4A). Réserves sur QU : prépublication, cinq graines, code
sur demande, un « 0,000 » identique à trois décimales jugé trop propre (C4, C7).

**Décision N-058** (la composition des proposeurs se juge sur l'oracle et le coût) : principe occupé en partie et
appuyé, non contredit (CADS p. 7 ; 2611.04420 p. 2, 8 ; 2611.00643 p. 16 ; S-4A).

**Rôles de N-065.**
- **Rôle 1** (second terrain du papier C : corruptibilité de deux sortes de juges de la recherche automatisée) :
  **occupé en partie pour la prémisse du bras « juge génératif »**. Pièces : 2611.04556, environnement E3 — un
  relecteur génératif approuve un écart non documenté à un préenregistrement, effets de +10,39, +13,61 et +8,56 points
  (p. 19, 48, V2 ; un seul manuscrit) ; 2611.00643 — optimiser un harnais contre un juge modèle fait monter sa note en
  coupant la précision de 46 à 68 % (p. 1, 2, 12, S-4A). **La pièce propre (juge statistique, gain continu, même
  attaque sur les deux juges) : libre dans les pièces lues.** Décision déjà prise par Lazar sur 2611.04556 : citée
  comme précédent de la prémisse, énoncé inchangé (R-2554). 2611.00643 n'a fait l'objet d'aucune décision.
- **Rôle 2** (atelier d'idées) : pas une revendication d'antériorité ; sans objet.
- **Rôle 3** (proposeur trompeur comme famille de menaces diffuses) : à trancher par Lazar ; aucune recherche
  d'antériorité dédiée n'a été faite au niveau 3.

**Phrase pour un jury.** « Séparer qui propose de qui juge, calculer la statistique hors des agents, sceller le plan
par empreinte avant les données, contrôler la multiplicité, éprouver le juge sur vérité plantée : tout cela est publié
en 2025 et 2026, et nous le citons. Ce que nous n'avons pas trouvé ailleurs : un juge dont le nul est formé des lois
déjà connues, sur des hypothèses libres, et sa mesure sous un proposeur chargé de le tromper qui en lit la règle. Cette
dernière phrase vaut pour les pièces lues, pas pour le champ : la littérature de finance sur les facteurs redondants
n'a pas été lue. »

---

## 6. Bascules et portes

| bascule ou porte | état | raison |
|---|---|---|
| « Publication externe du cœur séquentiel sur sondes » (programme, section 13) | **non déclenchée** | HELIOS version 5 annonce le séquentiel quatre fois sans le faire (p. 3, 18, 19, 26, C1) ; l'institut britannique moyenne sur les jetons (2512.07810, C1) ; 2611.02153 et 2611.10620 ne viennent pas des deux équipes nommées et ne publient pas de test toujours valide (S-7B) ; 2611.04556 n'a aucune sonde, mais un auteur de NARCBench et l'institut britannique y signent (V2). **Réserve** : le lecteur de 7-B porte le déclencheur à l'examen de Lazar ; l'histoire des versions de NARCBench (lot 10-A) et les codes de HELIOS et d'Orbit n'ont pas été lus. |
| Porte GC (N-005) : une source couvre la pièce revendiquée de HC1 | **non déclenchée** | aucune des sources visées ni des pièces neuves ne couvre la destination libre testée contre les deux nuls, par famille, dans un moniteur de contrôle (C3, C9, S-7C, V2). |
| « g des sondes > 0 » → papier C sur la contamination de construit | **non déclenchée** (elle dépend d'une mesure du programme) | des contre-indices publiés la rendent plus probable (section 4, HC2). |
| Repli (b) de N-035 pour H9 | **condition remplie pour le cœur de l'énoncé** selon S-7D et S-12 | repli annoncé par R-2555, décision à écrire et sceller. |
| « G1 échoue », « 8 milliards trop faible », « élicitation rouge insuffisante », « pas de témoin de vérité différée » | sans objet | elles dépendent de mesures, non de l'état de l'art. |
| Porte G2 (statistique de population supérieure à l'agrégation par agent) | sans objet ici | un contre-indice publié à sonde égale (2611.10620, p. 14, S-7B) est à porter au préenregistrement. |
| Veille « toute suite de 2607.08066 » (programme, section 16) | **une suite constatée** | 2611.04556 dit prolonger ces auteurs (p. 17, V2). |

Texte de la bascule : il dit « Oxford/NYU » ; aucune affiliation à New York n'est trouvée dans la version 5 de HELIOS
(p. 1, C1) ; l'erreur reste à la ligne 239 du programme (B1, B2).

---

## 7. Les quatre collisions en cours de décision (R-2555, point B (a))

Annoncées comme tranchées « en bloc sur les recommandations » ; les décisions restent à écrire, contre-lire et sceller
avant tout usage. Je rapporte ce que les lecteurs ont constaté et proposé, sans rien trancher.

1. **Organisme, O2 et O11.** Constat : C4, C7 (R-2177, R-2184) et S-4A. Proposition des lecteurs : ne garder en propre
   que le nul des lois connues et la conjonction ; étendre les citations obligatoires. **Point non couvert par la
   lettre de R-2555** : S-4A demande aussi de requalifier la forme de O12 en « occupée en partie » (CONFIRM).
2. **HC2.** Constat : S-1 (R-2180). Reformulation proposée par le lecteur : la sonde qui lit l'agent auteur et
   adversaire, le déplacement continu en plan apparié, la comparaison aux juges. **Ajustement de S-3A, postérieur** : le
   plan apparié n'est pas en soi une pièce neuve (2610.18408, p. 4, 12).
3. **Statistique de population.** Constat : S-5A (R-2181) puis S-7B. Proposition : la statistique sur scores de sondes
   de copies d'un même modèle, comparée au séquentiel par agent et à la coupe, à garantie toujours valide ; J-PACT et les
   balayages de 2611.10620 deviennent des bases à battre. S-7B ajoute que le mot « cœur vierge » ne tient plus.
4. **H9.** Constat : S-7D et S-12. Repli (b) de N-035.

**Autres points que les lecteurs portent à Lazar et qu'aucune décision lue ne couvre** : lettre de N-013 pour HC4 (« le
contexte seul n'y suffit pas ») ; prédictions 1 et 3 de HC1 ; H6 et le rééchantillonnage ; SafeDream aux motifs de
N-007 ; HC5 (la partie « juges entre eux » de la matrice) ; 2611.00643 pour le rôle 1 ; O12 (ci-dessus) ; manière de
dire les erreurs du texte envoyé à l'entretien. Les trois contre-indices de 2611.04556 sont à porter aux
préenregistrements de HC1, HC4 et HC6 (R-2554).

---

## 8. Erreurs de fait et corrections

### Texte envoyé au fonds (B1, C2)

| ligne | ce qui est écrit | constat | rapport |
|---|---|---|---|
| l. 199-200, 261 | « quorums across judge families (2605.15377) » | **contredit par le PDF** : tous les moniteurs emploient un seul modèle (p. 4) ; les familles différentes ne sont pas essayées (p. 8). Le rapport C3 trouve la pièce occupée par une autre source, 2607.08066 (p. 1, 2, 6) : la référence serait fausse, non le retrait. | B1 ; C3 |
| l. 131-132 | « additive accumulation on black-box scores (E-valuator …) » | **faux** : E-valuator n'est pas une somme cumulée (2512.03109, p. 1). | B1 |
| l. 87 | « synthetic precursor (2606.10456) » | **divergence entre lecteurs** : contredit par l'imprimé selon B1 (« We validate the threat model on real traces », p. 8) ; exact selon C2 (l'attaque reste construite ; les traces sont des scores de moniteur). | B1 ; C2 |
| l. 87-88 | « its central statement does not hold for its own construction » | exact pour la somme et la moyenne, faux pour le maximum ; à restreindre. Calcul en forme close de C2 au niveau 0,05 : 0,074 au point phare, 0,254 à l'écart le plus grand. L'article imprime lui-même 0,048 pour la moyenne à 1 % (p. 6), non cité. | C2 ; B1 |
| l. 84-85 | « The statistical core is classical and cited » | aucune référence dans le texte selon B1 ; « fidèle » selon C2. Les sources sont maintenant portées sur PDF (C6, C8). | B1 ; C2 |
| l. 176 | « weight of advice » puis 2603.15809 | l'article emprunte un autre modèle (p. 1) ; l'identification est celle du programme. | B1 |
| l. 181-183 | Panin, « three of five models » | exact, mais le PDF n'a été versé que treize jours après l'envoi. | B1 |
| l. 276 | « The source paper's 18 prompts » | décompte du programme, non imprimé par l'article. | B1 |
| l. 264 | « No claimed statement has been found fully occupied » | littéralement exact ; n'est plus un tableau fidèle. | B1 |

Bilan de traçabilité (B1) : 101 affirmations sur des travaux d'autrui dans le programme v2 et le texte envoyé ; une seule
porte une page ; 78 tracées après ce passage, dont 4 contredites ou fausses telles qu'écrites ; 13 sans source désignée.

### Socle de preuves v2 (B3)

Dix-huit affirmations : 10 confirmées, 5 avec réserve, 3 corrigées. Quatre corrections avant l'entretien :
1. l. 73 : « less promising » n'est pas une conclusion de 2606.08892 mais une prémisse (p. 2).
2. l. 76, 457-458, 539 : 2512.07810 traite de sous-performance, non de sabotage ; pages 17 et 18 ; contre-résultat
   partiel ; aucun chiffre de sonde sur ces pages.
3. l. 68-69 : « échoue par construction » demande la condition de 2606.10456, proposition 1 (p. 3).
4. l. 74, 77 : nommer E-valuator (p. 1).

### État de l'art v1 et programme v2 (B1, B2, S-2A, S-2B, C6)

- État de l'art v1, l. 37 : à nuancer ; le billet long de l'institut britannique mesure, « The Case for White Box
  Control » ne soutient pas que le blanc bat le noir ; la date invérifiable selon B2 est maintenant lue : 10 juillet 2025
  (S-2A).
- l. 102 (billet de Gasteiger et collègues) : chiffres de nature « figure », à réécrire ; la fourchette vaut pour trois
  juges sur quatre (S-2B, section 0.3). l. 92 (Hopman) : exact sur le fond, deux détails inexacts, incomplet (S-2B).
- l. 99 : à corriger selon S-2B. l. 154 : contredite par le niveau 2 et jamais corrigée (B2). l. 132 et 140 : six
  chiffres invérifiables au dépôt (B2) ; le lot 11, qui les visait, a des pièces versées et aucun rapport de lecture.
- Programme v2 : l. 59, auteurs faux pour 2208.07610 (déjà corrigé par P-008, resté dans le texte) ; l. 239,
  « Oxford/NYU » ; neuf affirmations d'antériorité sans source (l. 16, 93, 99, 104, 112, 137, 145, 197, 239) (B1) ;
  section 3, « il faut un agrégateur d'autocorrélation ou de co-élévation » écrit sans citer les outils publiés (C6).
- Faits repris de pistes : « What the Monitor Saw » est une communication d'atelier de NeurIPS 2026 sans entrée sur
  arXiv ; le billet sur la « dilution » des sondes est « Trusted monitoring, but with deception probes » (provenance du
  lot 8) ; le fichier 2607.13346 s'intitule « PRISM », non « The Refusal Residue » (C8).

---

## 9. Ce qui reste non vérifié

1. **Lots dont les pièces sont versées et qu'aucun lecteur n'a lus** (aucun rapport sur la branche, tête `10016a61`) :
   - lot 8 (13 PDF), dont Koning 2310.01153, Ramdas et collègues 2102.00630, Vovk 1906.09256, 2609.15994, 2604.15384,
     2610.31593 ;
   - lot 10 (23 PDF) : histoire des versions de NARCBench (lot 10-A, qui date l'annonce du séquentiel), 2602.21262,
     2607.00415, et d'autres ;
   - lot 11 (13 PDF) : sources des chiffres invérifiables de l'état de l'art v1, classiques de détection séquentielle ;
   - lot 4 : 41 PDF versés, 9 lus (S-4A) ; lot 4-B (juges de la recherche automatisée) non rendu ;
   - lot 3 : 19 PDF versés, 7 lus (S-3A) ; lot 7 : 39 PDF versés, lus en partie (C8, C9, S-7A à S-7D).
2. **Lot 9 jamais rendu** : articles citant 2606.08892, 2512.07810 et 2606.10456 ; listes d'arXiv du 1er au 10
   novembre ; pages de Redwood Research, Apollo, FAR.AI, METR ; soumissions à ICLR 2027.
3. **Rien n'a été cherché entre le 10 et le 13 novembre**, hors l'article signalé par Lazar (2611.04556).
4. **Pièces inaccessibles aux sessions** : « What the Monitor Saw » et « When Monitors Fail, the Model Still Knows »
   (OpenReview, refus 403) ; Ramtin et collègues (dépôt HAL `hal-04744798`, à prendre à la main) ; SSRN ; ScienceDirect ;
   GitHub hors du dépôt du programme, donc les **codes de HELIOS, d'Orbit et de POPPER** (une statistique séquentielle
   codée sans être dans l'article échapperait) ; Harvey et Fischer 1997 (payant) ; l'affiche antérieure à 2607.08066
   (non attestée ; deux candidats : un article d'OpenReview résumé par un billet du 25 juillet 2025, S-2B, et un atelier
   d'ICML 2025 cité par 2611.04556, p. 15, V2).
5. **Billets non versés** (droits réservés) : les sources des lots 2-A et 2-B ne vivaient que dans le dossier temporaire
   de la session sœur ; elles ne sont plus contrôlables sans nouveau téléchargement.
6. **Articles connus par leur seul billet** : 2609.14796, 2610.20941, 2610.31593 ; PDF au dépôt non relus contre un
   énoncé : 2605.26047 (H6), 2607.06503 (cascade, H2), 2604.16286.
7. **Pistes nommées par les lecteurs et non lues** : pour O4, Martin, « Regularized e-processes », et la littérature de
   finance sur les facteurs redondants ; Gençay 2608.27734 (O11, O20) ; pour H2, 2602.11409, 2606.07624 (lu par S-5A
   seulement), 2607.02510 et 2606.06223 lus par C5 ; pour le papier B, 2607.06807, 2510.04303 ; pour H8, 2602.01425 ;
   pour HC1, 2607.05545, 2605.03255 ; pour HC5, Pandey et collègues ; pour H4′, Keppo et collègues ; pour H9, la
   référence 38 d'AgentCollabBench et les versions 1 de MasDrift et de Sun.
8. **Étendue de lecture** : plusieurs lecteurs n'ont lu ligne à ligne que le corps des pièces, annexes par mots-clés
   (C4, C7, C8, S-4A, S-5A) ; S-7A a lu 124 pages en six minutes et se tient pour une lecture rapide ; les preuves de
   2601.05427 ne sont pas vérifiées (S-5A) ; trois écarts de C7 (O10, O17, O19) reposent sur des pièces lues par
   passages.
9. **Recherche affirmative** : D1, D2, D3 sont des pistes de moteur ; une requête de D1 a été refusée par un
   classifieur de l'outil, ni relancée ni reformulée. Peu de requêtes pour H4′, H6, HC2b, HC4.
10. **Non réexaminés** : O5, O6, O15 ; rôle 3 de N-065.
11. **Par moi** : aucun PDF rouvert ; les archives de fichiers de travail (`.tar`) des lots n'ont pas été ouvertes.

---

## 10. Divergences entre lecteurs, dites telles quelles

1. **O2.** C4 : trois composantes sur quatre occupées par Qu, Chen, Wang. C7 : deux en entier, une dans son principe.
   S-4A, sur d'autres pièces : trois occupées, par empreinte cryptographique comprise. Le registre (R-2177) reprend
   « trois sur quatre ».
2. **Forme de O12.** C4 et C7 : non trouvée. S-4A : occupée en partie (CONFIRM, annexe C.6).
3. **O1, O3, O9, O10, O13, O17, O19.** Mots et statuts différents entre C7 et S-4A (table de la section 5) ; les deux
   lecteurs n'ont pas lu les mêmes pièces.
4. **« synthetic » pour 2606.10456.** B1 : contredit par l'imprimé. C2 : exact. La synthèse provisoire retenait une
   formulation intermédiaire.
5. **Nombre d'erreurs de fait du texte envoyé.** B1 : trois. Synthèse provisoire : deux et une formulation contestable.
6. **« quorums across judge families ».** B1 : pièce retirée sur une source qui ne l'occupe pas. C3 : pièce occupée par
   2607.08066.
7. **« The statistical core is classical and cited ».** B1 : sans répondant dans le texte. C2 : fidèle.
8. **H2, L, T : le mot.** C1, C2, C8, S-5B, S-2A : « occupé en partie ». S-5A : « non occupée », avec occupations
   partielles en boîte noire. S-7A : « libre ». Même substance : la conjonction n'est pas trouvée.
9. **H8.** S-7A : « voisin fort », lecture dure « occupée en partie », à trancher. S-7B : « occupée en partie ». S-3A :
   « voisins multiples, aucune occupation nouvelle ». C8 : socle occupé en partie, pièce revendiquée libre.
10. **H6.** Synthèse provisoire : libre. S-2A : occupée en partie pour le rééchantillonnage (lecture dure, sur billet).
    S-7B écrit « occupée en partie (bruit sur les poids) », état d'avant N-015.
11. **H3 et 2605.11135.** S-5A : « occupée en partie en boîte noire », lecture « voisin » défendable.
12. **Squelette statistique de 2601.05427.** S-5A : « occupée en partie », lecture « voisin fort, outil » défendable.
13. **HC4.** C9 : « occupée en partie (points de coût épars) ». Complément 1 : « pièce revendiquée libre, prémisse
    entamée ».
14. **H9.** C6 et C9, sur leurs lots : « libre » ou « repli non déclenché ». S-7D et S-12 : occupée en partie sur le
    cœur. Pas une contradiction : pièces différentes.
15. **Date de « Red-Teaming Auto Mode ».** C5 : 27 septembre 2026 (PDF 2609.19587). S-2B : 22 octobre 2026 (billet).
    Non réconcilié ; les deux peuvent être vrais.
16. **2611.04556, rôle 1 de N-065.** V1 (session mère) : « voisin ». V2 (lecteur neuf) : « occupé en partie pour la
    prémisse ». Tranché par Lazar (R-2554) : précédent à citer.
17. **2611.04556, autres points.** V2 juge trop forts dans V1 : « aucune intensité graduée », « aucune détection »,
    « HC6 annoncée comme suite », l'usage des données pour HC2b.
18. **Bascule.** C1 : non déclenchée. S-7B : non déclenchée au sens du texte, déclencheur « à examiner par Lazar ».

**Contrôle du complément 1 contre les rapports 7-B, 7-C et 7-D** (demandé par le mandat).
- Verdicts et pages : conformes pour 7-B (2611.02153, p. 4, 6-9 ; 2611.10620, p. 11-12, 15, 19, 21 ; 2610.24052, p. 5)
  et pour 7-C (2610.29178, p. 1, 12, 14-16, 35 ; 2608.12645, p. 6-10, 12 ; 2602.08877, p. 17, 18). Pour 7-D, les
  verdicts sont conformes ; les plages de pages du complément (MasDrift « p. 1-3, 5-8, 14, 18-19, 21-25 ») sont plus
  larges que les pages que je retrouve citées une à une dans le rapport (p. 1, 2, 5, 6, 7, 19, 21, 22, 23, 24).
- **Omis par le complément** : le contre-indice sur le critère de G2 (2611.10620, p. 14) ; le contre-indice partiel de
  2611.10620 sur HC4 (p. 22) ; le contre-indice de 2609.20211 sur la paraphrase de HC5 (p. 20) ; le contre-indice partiel
  de 2610.29178 sur HC3 (p. 26) ; le contre-indice indirect de 2602.08877 sur HC2 ; l'occupation « au sens faible »
  de HC1 (b) par 2608.12645.
- **Trop favorable** : « le bras “moniteur à chaque passage” n'existe que comme concept (2602.11865, p. 16) ». Le
  rapport 7-D donne la composante « un moniteur relève la survie » pour occupée en partie par MasDrift (politique portée
  à chaque relais, p. 5, 6).
- **Dépassé** : le « non trouvé » de 7-D sur la survie conditionnelle par relais, resserré par le lot 12 (p. 34).
- Les faits de la section 3 du complément (atelier, billet, identifiants) ne sont pas dans les rapports de lecture ; je
  les retrouve dans la note de provenance du lot 8 (`6ba353ea…`), sauf le résumé du livre blanc du SANS Institute, que
  je n'ai pas contrôlé.

---

## 11. Phrase d'ensemble pour un jury

« Nous avons fait lire sur source, par des lecteurs qui n'avaient pas écrit le programme, plus de cent cinquante pièces
contre chacun de nos énoncés. Aucun n'est trouvé occupé en entier ; presque tous le sont en partie, et quatre l'ont été
assez pour que nous resserrions ce que nous revendiquons. Nous disons nous-mêmes les résultats publiés qui vont contre
nos prédictions, les erreurs de notre texte envoyé, et ce que nous n'avons pas lu. »

Le nombre « plus de cent cinquante » est un ordre de grandeur tiré des comptes de pièces des rapports (journal,
section 3) ; il n'a pas été recompté pièce par pièce et ne doit pas être cité comme un chiffre exact.
