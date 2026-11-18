# Contre-lecture du relevé d'idées des courses de l'organisme et du tour du collisionneur sur la question 2 du mentor Kirchner (3 novembre) — v1

- **Écrit** le 18 novembre 2026 par un contre-lecteur neuf (Claude Opus 5.5, règle R2), qui n'a pas écrit la note. Consigne calculée par le script de la mère, sous l'autonomie GO-2026-11-18-05 et le « go » de Lazar aux quatre lectures sans dépense de l'inventaire (R-3168, R-3170). Inventaire : `docs/notes/inventaire-collisionneurs-organismes-v1/inventaire-v1.md` (`b49dc2462382…`, empreinte recalculée), sections A (rangées 58 et 74), B (point 4), C et E (nœud 3).
- **Note contre-lue** : `docs/notes/quatre-lectures-inventaire-v1/mentors-kirchner-q2-v1.md`, `8a077899a49954de7f4c622b790292bab87036258544bd3a2eb9c0d983030d63` (recalculée ; égale au compagnon). Non modifiée.
- **Cadre tenu** : lecture seule ; aucune dépense, aucun appel de modèle, aucune clé lue ni affichée, aucun commit, aucune poussée, aucun `git fetch`. Seules les sources extraites par la mère ont été ouvertes. Rien sous `diag/` ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis. Les trois fiches d'Argon exclues n'ont pas été rouvertes, pas même leur titre : l'outil de sécurité a refusé cette lecture, et ce refus a été respecté. Leur taille a été mesurée sur leurs bornes de lignes, sans lire leur contenu.
- **Sources rouvertes** (sous `/tmp/claude-0/-home-user-controle-ia-travail/8282ab93-0983-5813-b791-a7a522157dcd/scratchpad/quatre-lectures/extrait/<branche>/`) :
  - branche `donnees/course-kirchner-q2-v1-run`, commit `e7f288c` (première course) ;
  - branche `donnees/course-kirchner-q2-v1-run-seconde`, commit `5d8a9e8` (seconde course) ;
  - branches `donnees/collisionneur-v9-kirchner-q2-v1` (`16ec2e5`, le kit), `-run` (`9652f23`, le tour) et `-suite` (`19e1814`, la suite) du collisionneur.
  - Au dépôt : `registres/depenses.md` lignes 335-346 ; `registres/decisions.md` (R-1124, R-1126, R-1127, R-1139, R-1155, R-1451).
- **Nommage** (celui de la note) : Fable = Claude Fable 5.1 ; Opus = Claude Opus 5.5 ; Argon = Gemini 4 Argon ; Astra = GPT-6 Astra ; Kimi = Kimi K3.1 Pro. Lettres du collisionneur : A Fable, B Opus, C Argon, D Kimi, E Astra.

## Verdict

**À corriger.** La note est fidèle sur le fond. Ses citations tirées au hasard sont justes, ses comptes et ses montants concordent avec les sources, et elle n'oublie aucune fiche lisible. Elle a toutefois dix défauts précis (liste ci-dessous) :
- quatre erreurs ou imprécisions de fait ;
- deux inférences du rédacteur présentées sans marque ;
- un oubli dans le tableau des exclusions ;
- trois passages qui décrivent l'objet ou le thème de pièces exclues (cloisonnement).

Toutes ces corrections sont de fait ou purement soustractives : elles ne demandent aucun jugement nouveau sur le fond. J'ai donc écrit la version 2 : `docs/notes/quatre-lectures-inventaire-v1/mentors-kirchner-q2-v2.md`. Réserve sur ce point : les trois retraits de cloisonnement ne sont pas, au sens strict, des « corrections de fait ». Si la mère lit la règle à la lettre, elle peut écarter la v2 et faire appliquer ces trois retraits par le rédacteur. Une réserve séparée, sur le partage « classe W2 », est laissée à la mère (§ 4).

## 1. Citations rouvertes (plus de quinze, tirées dans tout le texte)

Chaque ligne indique la citation de la note, ce que dit la source, et le résultat. Abréviations : « F » = fichier `fiches.json` de la seconde course (`5d8a9e8`, chemin `donnees/course-kirchner-q2-v1-run-seconde/run-20261103-1221-seconde/course/generation-1/fiches.json`, empreinte `7c9067537d81…`) ; « coll: » = `donnees/collisionneur-v9-kirchner-q2-v1-suite/run-kirchner-q2-e3-v1/cellules/` (`19e1814`).

**Fiches de la seconde course.** Proposeur relu dans `meta.proposeur`, bornes de lignes recalculées, champs hypothèse, première expérience et « changer d'avis » relus.
- Le rappel du moniteur sur tricheries plantées, avant et après le classement (Opus, `fa69db0f5e1a1`, F 629-652) : 600 méthodes, la moitié plantées, trois classes, même modèle en moniteur, quartile supérieur, baisse d'au moins 10 points « supposé », mécanisme de la délibération écrite. **Conforme.**
- Le classement sélectionne-t-il les angles morts (Astra, `f8506b9985d99`, F 508-531) : perte prédite d'au moins 10 points, « seuils supposés ». **Conforme.**
- La chute du rappel du moniteur du même modèle (Argon, `fe96087a6d947`) : 20 % supposé, classe W2 ou copie de format, décile supérieur, au moins 20 points, autre famille en comparaison. **Conforme sur le fond.** La borne de lignes est 774-797 et non 798 (correction 9).
- La saturation du classement au-delà de la médiane (Argon, `f15ac43332d34`, F 122-145) : annexe D.3 dans le champ « problème », banque de 288 épisodes, juge au nul v8 employé comme oracle après coup, +30 et −15 points. **Conforme.**
- Les ratés corrélés du filtre puis du moniteur (Opus, `f3a11681fbdd7`) : rapport prédit d'au moins 1,5, second étage d'une autre famille. **Conforme.**
- La fusion `f457b170a26d4` (filtre et audit du même modèle) : 6 400 lectures « calcul », cellule « tout même modèle » contre cellule où seul l'audit change de famille. **Conforme.**
- Grimper un banc de surveillabilité par sélection (Fable, `f9dc6da7bb4ba`) : meilleur de 16 échafaudages, rapport de transfert inférieur à 0,3, « une mesure corrélée n'est pas un levier » (pièce « nos résultats », § 7, dans le champ « problème »). **Conforme** ; la note marque bien ce point « non vérifié ».
- La surveillabilité perdue dans la course au classement (Fable, `f785f698c58ab`) : 0, 2 et 5 rivaux, 60 tâches de la banque P3, au moins 10 points. **Conforme.**
- La garde de capacité à 200 exemples (Fable, `f153de525939b`) : au moins 30 % contre au plus 5 %, réévaluation sur 2 000 exemples, volet sur l'organisme. **Conforme.**
- La garde de capacité bruitée et les moniteurs tenus à l'écart (Argon, `f50c7618cf132`) : tri de graines, baisse de séparabilité d'au moins 0,5. **Conforme.**
- Le forum et les faux négatifs (Astra, `f3f624640cb72`) : 80 groupes de 4, hausse de corrélation d'au moins 0,15 (champ « changer d'avis »). **Conforme.**
- La nulle de relance en tête du classement (Opus, `f1102c979a221`) : 30 loteries, au moins 30 %, e-valeurs. **Conforme.**
- La triche née de la sélection (Opus, `f093da138e4d3`) : 2 000 essais, au moins 15 points, règle des 30 tricheries puis 6 000 essais. **Conforme.**
- Le seuil calibré avant sélection (Astra, `f61a407b0b69e`) : plus de 10 % de fausses alertes, au moins 10 points de rappel (champ « changer d'avis »). **Conforme.**
- La relance chanceuse (Fable, `fd0681ac5bfa0`) : 50 relances, au moins 20 %, au plus 5 %, puissance de 80 %. **Conforme.**
- Également relues et conformes : `fa489015df210` (Astra), `f0263244aaf80` (Fable), `f2ef512adbbf0` (Argon), `f5718cde9c2d9` (Opus), `f6cb7fa0c0edb` (Argon), `f778420563500` (Opus), `fdc106610254a` (Opus), `f36fa17fdedf9` (Astra).
- **Bilan des fiches** : les 33 fiches ont toutes la case `niveau-methode` ; les proposeurs sont Fable 6, Opus 7, Astra 8, Argon 8, plus 4 fusions, comme le dit la note. Les 30 fiches non exclues figurent toutes au § 2.

**Fusions inachevées et pièces de la seconde course.**
- La fusion inachevée `f4d8599dd29de` (fichier des fusions inachevées, lignes 3-19) : interaction prédite d'au plus −8 points « supposé », parents `fa69db0f5e1a1` et `fdc106610254a`, bras « basique » (`kq2-cle-bras.json`). Catégorie « signe de l'interaction contradictoire » au journal d'aiguillage. **Conforme.**
- Le journal d'aiguillage de la seconde course : six retenues, à savoir trois propositions « claude », deux fusions « à corriger » et une fusion « concret » avec refus (`f09fb88cb9eff`). Celui de la première course : une seule retenue, `f6cb7fa0c0edb` (Argon), empreinte `a09cb18c…`. **Conforme.**
- Le manifeste de fin de la seconde course : `exclues_a4` vaut `f131f9c3ee017`, avec l'étiquette `["fusion"]` (lignes 873-879). La garde de Kimi (lignes 891-899) a 0 fiche vue et un taux de 0. **Conforme.**
- Les manifestes de lancement : consigne de l'aiguilleur v2 aux lignes 255-256 (`7514666e…`) et question aux lignes 287-288 (`291f91f8…`), dans les deux courses. `aiguilleur_v53.py` vaut `a856cdaa…` (manifeste de départ, ligne 225). **Conforme.**
- Le journal du relais Kimi de la seconde course : un appel de 880,8 s avec 27 750 jetons de sortie, statut 200. **Conforme.**

**Cellules du collisionneur.**
- Proposition A (Fable), T1, lignes 36-49 : facteur d'enrichissement, plants « sans dents », condition « même modèle » plus forte sur la classe P à la ligne 49. **Conforme.**
- Proposition A, T1, lignes 85-102 : la table d'instruments. La ligne 93 est le classement, la 96 Petri, la 98 le forum, la 102 la lecture d'ensemble. **Conforme.**
- Proposition A, T3 : ligne 22 (retrait de l'affirmation du plafond, acceptée), ligne 47 (violations suscitées, oracle mécanique), ligne 55 (bras de contagion E1-F), ligne 59 (le pilote « ne décide pas »), lignes 93-95 (amendement de la table), ligne 107 (retrait), ligne 112 (première expérience : le pilote de E1'). **Conforme.**
- Proposition B (Opus), T1 : ligne 30 (« bras naturel »), ligne 105 (effet de type Berkson), lignes 122-128 (1 000 classements, étage 2 par audit humain stratifié par rang), lignes 87-89 (contrôle négatif par permutation, contrôle positif par deux appels de même invite), lignes 213-233 (instruments 3, 4, 5 et 6). **Conforme.**
- Proposition B, T3 : lignes 74-94 (log-rapport de cotes, modèle de réponse à l'item, angle mort partagé construit, auto-indulgence), lignes 105-110 (quantiles 0,9 et 0,99, décomposition), ligne 124 (probabilités d'inclusion connues), lignes 143-147 (localisation d'un échec), lignes 178-181 (« apport conditionnel »), ligne 206 (première expérience : la fiche 1). **Conforme.**
- Proposition C (Argon), T3, lignes 32-46 : 120 courses de cinq agents, forum actif contre forum placebo, un agent sous consigne scellée qui suscite deux classes dont W2. Lignes 51-54 : trois partitions, classe externe « omission sélective de contraintes / recombinaison W2 ». Ligne 87 : C met C1 en premier. **Conforme.**
- Proposition D (Kimi) : T1 lignes 51-58 (trois sélections) et ligne 80 (plusieurs générations, batterie d'audit figée) ; T3 lignes 63-76 (aucun plancher de rappel, analyse secondaire du pipeline), ligne 88 (cellules « nouvelles classes », « nouvelles tâches », « horizon allongé »), lignes 113-121 (partage du modèle parmi « ce qui n'est pas établi » ; première expérience D1). **Conforme.**
- Proposition E (Astra) : T1 ligne 57 (candidats figés, sélection hors ligne), ligne 65 (la phrase citée sur la nouvelle session, exacte), ligne 99 (circularité), ligne 145 (« pas une baseline à battre ») ; T3 ligne 70 (micro-harnais construit avec des composants de l'organisme), ligne 98 (marge de 5 points), ligne 118 (seuils conditionnels), ligne 141 (rétrécissement aux comptes rendus), ligne 209 (première expérience). **Conforme.**

**Rapports, état et montants.**
- Rapport du tour, lignes 14-19 et 24-31 ; rapport de la suite, lignes 16-17, 21-23 et 29 ; `etat.md` (« Absences acceptées par l'arbitre : aucune », 10.34) ; vérification du tour (13 valides). Rapports des courses RA1 (lignes 13-21 et 33) et RA2 (lignes 19-22 et 33-35). Traces agrégées des deux courses ; registre des dépenses, lignes 336, 338, 342, 343 et 346. **Tous les montants concordent** : 13,228231 et 13,230489 ; 10,839252 et 10,84159 ; environ 24,07 ; 9,4956 + 0,603056 + 0,00279 ≈ 10,10 ; 0,8501 ; 10,3442 et environ 10,95.
- Inventaire, rangées 58 et 74 : 10,95 ; 13,23 + 10,84. **Concordent.**
- La question (kit `16ec2e5`, `question.md`) : lignes 7, 11-22, 24-35, 39 et 47 relues. Elle est égale à l'octet à `question-etage3.md` du tour (`cmp`). **Conforme.**
- Identifiants réemployés entre les deux courses : recalculés. Les 26 fichiers de verdicts de la première course (clés `ident` et `empreinte` seulement) comparés aux 33 fiches de la seconde donnent **23 identifiants communs, 23 empreintes différentes**. **Conforme.**

## 2. Avis, état de l'art (R7), zones vierges (R8)

- Les avis des espèces et des proposeurs sont attribués partout : espèce, lettre, fichier et ligne. Les chiffres des fiches sont dits supposés ou illustratifs. Les identifiants de travaux et les chiffres des pièces Kirchner et « nos résultats » sont déclarés **non vérifiés** en tête (ligne 5), puis au cas par cas (annexe D.3, § 7 de « nos résultats »). **Conforme à R7.**
- Les zones « peu couvertes » sont dites « questions, pas des trous du champ » (ligne 5), et le § 1 les cite entre guillemets comme demande de la question. **Conforme à R8.**
- **Deux inférences du rédacteur sont présentées sans marque** :
  - (a) § 4.1 : « Les deux fiches manquantes de Fable et la manquante d'Opus sont les trois propositions de Claude… ». Le journal d'aiguillage ne dit que « claude ». La répartition se déduit du quota de 8 fiches par proposeur (manifeste de départ, ligne 349). Le compte est juste, mais c'est une déduction (correction 4).
  - (b) § 3 : « la convergence dit au moins autant sur la question servie que sur les espèces » est une lecture du rédacteur, non une mesure (correction 5).
- « Très probable : toutes les fiches de Kimi refusées au format » est bien attribué à la fille et dit non vérifié (R-1155, relu au registre). **Conforme.**

## 3. Cloisonnement

- Aucun résultat sous embargo n'est cité. T0.3 et la banque P3 (non bis) sont nommés comme pièces des fiches ; ils ne sont pas sous embargo.
- Les sections exclues ne sont pas résumées dans le tableau des exclusions. Les tailles des fiches et sections exclues, mesurées sur leurs bornes de lignes (3 867, 3 525, 4 029, 7 187, 1 310, 1 642, 2 297, 2 815, 1 589 et 1 223 octets), concordent à un saut de ligne près.
- Les trois sections lues avant classement (fiche 4 de B aux deux tours ; E4' de A) sont déclarées. Je ne peux pas corriger cette lecture ; je le relève seulement.
- **Trois passages disent pourtant quelque chose de l'objet ou du thème de pièces exclues** :
  - la ligne 53 (« Réserve sur les exclusions voisines ») décrit l'objet des trois sections retirées ;
  - la ligne 127 (§ 2.5) donne le thème d'une fiche d'Argon exclue sur son seul titre ;
  - la ligne 137 (§ 2.6) donne le sujet de la fiche 4 de B.

  La règle demande « exclue : famille n », le chemin et la taille, rien de plus (corrections 8a à 8c).
- **Pièce exclue omise des exclusions** : chaque extrait porte un compagnon `.sha256` orphelin. Il nomme une pièce de la question-mère, qui relève de la famille 2 (inventaire § C) : exclue : famille 2, chemin `docs/notes/ideation-organisme-v1/question-mere-reponses/consigne-argon-question-mere-v3.txt.sha256`, 102 octets, cinq copies. Seule la ligne d'empreinte du compagnon a été vue ; la pièce elle-même est absente des extraits.

## 4. Oublis et réserve laissée à la mère

- **Fiches** : aucun oubli (30 lues, 3 exclues ; total 33). **Fusions inachevées** : 4 sur 4 (2 relevées, 2 non lues et déclarées). **Cellules** : 15 sur 15 (T2 par leur structure). **Espèces** : les cinq, Kimi par la seule lettre D, ce qui est déclaré.
- **Oubli de fait** :
  - l'orphelin d'empreinte n'est pas déclaré : « 0 écart » ne compte que les paires présentes (correction 1) ;
  - la ligne T2 du tableau des exclusions ne vise que la fiche 3 de C, alors que les sections « Sur la proposition B » des T2 visent aussi la fiche 4 de B, retirée (correction 7) ;
  - le § « ce que j'ai lu » affirme que les T2 ne contiennent « que » trois rubriques. Leurs préambules (T2-B lignes 1-20, T2-E lignes 1-15) et la « Note de clôture » de T2-A (ligne 131) n'ont pas été vus (correction 6).
- **Pièces non mentionnées** (sans conséquence) : `accords.json`, `memoire.json`, `kq2-paires-par-bras.json`, `kq2-cle-anonymisation.json`, `kq2-emplacement-sessions.json` de la seconde course ne figurent ni parmi les pièces lues ni parmi les non ouvertes.
- **Réserve sur le partage « classe W2 »** (jugement, non correction) : le rédacteur a retiré la fiche 4 de B comme voisine de la famille 2, mais il garde quatre idées qui prennent elles aussi pour pièces centrales le juge statistique de l'organisme et les classes qu'il ne couvre pas :
  - la fiche `f2ef512adbbf0` (Argon, F 146-169) ;
  - la fiche `f15ac43332d34` (Argon, F 122-145) ;
  - l'expérience C1 de C au T3 (agent sous consigne scellée) ;
  - l'expérience E4 de A au T1.

  Le partage n'est pas tenu de façon uniforme. Je n'en décris pas davantage le contenu. La mère tranche ; la v2 porte cette réserve dans ses limites, sans retirer ces entrées.

## 5. Corrections, une ligne chacune (toutes portées dans la v2)

1. Empreintes : « 0 écart » vaut sur les paires présentes. Chaque extrait porte un compagnon orphelin (`…/consigne-argon-question-mere-v3.txt.sha256`, 102 octets, famille 2), déjà connu au dépôt.
2. Première course : les 26 fichiers de verdicts ne sont pas tous « à deux juges ». 18 portent Astra et Opus, 8 le seul Opus.
3. Expérience E4 de A : la « copie renommée » est la classe C (couverte selon A), pas la classe W2 (`E3-T1-conception-A.md` ligne 77).
4. § 4.1 : la répartition « deux de Fable, une d'Opus » des trois propositions de Claude sans passeport est une déduction du quota ; à marquer comme telle.
5. § 3 : « la convergence dit au moins autant sur la question… » est une lecture du rédacteur, à marquer.
6. « Ce que j'ai lu » : les titres des T2 ne prouvent pas l'absence d'idée nouvelle (préambules et note de clôture non vus).
7. Tableau des exclusions : la ligne T2 s'étend aux sections visant la fiche 4 de B (et, par prudence, E4 de A).
8. Cloisonnement : trois retraits.
   - (a) La ligne 53 ne décrit plus l'objet des sections retirées.
   - (b) La ligne 127, qui donnait le thème d'une fiche exclue, est supprimée.
   - (c) À la ligne 137, la phrase sur la fiche de B « sur ce sujet » est supprimée.
9. Fiche `fe96087a6d947` : lignes 774-797, et non 798.
10. Limites : la réserve du contre-lecteur sur le partage « classe W2 » est ajoutée.
