# Comparaison des deux réponses sur le mécanisme adjudant aux moniteurs pour le hors distribution — v1

- **Auteur** : comparateur neuf, Claude Opus 5.5 ; ni auteur de l'une ou l'autre réponse, ni de la contre-lecture. **Cadre** : GO-2026-11-21-56, décision D-7. Pièce de travail (classe C), non contre-lue. Aucun appel payant, aucune machine, ni commit ni poussée.
- **Date** : 2026-11-21, écrite entre 14:10 et 14:20 UTC environ (`date -u` à 14:10:21 et à 14:15:41).
- **Grille appliquée** : `grille-comparaison-v1.md` (`8a22a396989322ed60bd8ab977dc77fdd1c20d3e0d37fa7f03ad64fb6b150920`), même dossier, scellée à 13:45:56 UTC, avant toute lecture des réponses. Les lectures de la grille que l'application a demandées sont déclarées au § 1.
- **Pièces comparées**, empreintes vérifiées par `sha256sum` et par `scellement verifier` avant lecture :
  - la réponse de Fable 5.2, « réponse A » : `docs/notes/mecanisme-adjudant-hors-distribution-v1/reponse-fable-mecanisme-adjudant-v1.md` (`896cec0e0be5…`) ;
  - la réponse d'Opus écrite sans voir A, « réponse B » : `docs/notes/adjudant-opus-independant-v1/reponse-opus-mecanisme-adjudant-v1.md` (`998bd5d9c6c7…`) ;
  - la contre-lecture de A : `docs/notes/mecanisme-adjudant-hors-distribution-v1/contre-lecture-opus-mecanisme-adjudant-v1.md` (`2167a5aed34d…`).
- **Lu après la grille**, dans l'ordre fixé : A, B, la contre-lecture ; puis les deux tables de provenance (`563e611d…` pour A, `92f7894a…` pour B) ; les pages de PDF citées aux § 2 et 3, extraites par `pdftotext -layout` page par page, toutes les empreintes des PDF égales à leurs compagnons ; la section 6 du programme (`2fd63bad…`) ; le titre et le plan de la note sur la dérive de régime (`4a1579b3…`) ; trois lignes de la note du moniteur de dissonance trouvées par recherche de motifs (`403fe3e2…`, ligne 64) ; le programme de calcul de A (`19ac7356…`), rejoué.
- **Non ouvert** : tout ce que le mandat interdit ; le dossier `collisionneur-v1/` voisin de A ; le dossier `docs/sources/pdf/mecanisme-adjudant-v1/voisins-v1/` ; la note de rederivation de la règle « moniteur invalide » ; les registres, hors la seule ligne GO-2026-11-21-34 lue avant la grille ; aucun résultat d'expérience.
- **Pièces versées avec cette note, même dossier, scellées** : `enumerer-affirmations-v1.py` (`16f3345a…`) et les deux listes qu'il produit, `affirmations-reponse-A-v1.tsv` (`bc151ee0…`) et `affirmations-reponse-B-v1.tsv` (`8270abd0…`) ; `recalculs-comparaison-adjudant-v1.py` (`d467b13c…`) et sa sortie `.txt` (`b19d7526…`), rejouée deux fois à l'octet. Les blocs [R1] à [R7] cités plus bas sont ceux de cette sortie.

## 0. Verdict

1. **Pas de vainqueur net.** Sur huit critères, les deux réponses font jeu égal sur six ; A l'emporte d'un point sur le coût et sur le manuel de course ; B ne l'emporte sur aucun. La valeur est dans la fusion des deux.
2. **Le cœur converge** : on ne rend pas un moniteur valide hors distribution ; la validité vient d'un audit tiré au hasard, en secret, jugé contre le dommage, dont le même flux mesure le rappel en service de chaque moniteur ; sondes, « dopamine » et lentilles deviennent des outils d'efficacité. Les deux mettent ce plancher au premier rang, indépendamment, avec des causes communes déclarées (§ 4).
3. **Apports propres qui comptent** : chez A, l'ossature du lemme d'additivité publiée dès 1981 (sa décision D-4), des calculs exacts rejoués à l'octet, une famille tenue à l'écart écrite par un tiers, un manuel qui tue les règles à fausses alertes ; chez B, la réduction du problème à deux nombres (le plancher d'audit q, que l'on paie, et la sensibilité de l'oracle d, qu'il faut mesurer), la mesure de d par recoupement de lecteurs, le plafond de divergence au jumeau comme juge des sondes au banc.
4. **À corriger** : chez A, ce que la contre-lecture a relevé (vérifié, § 8) et une description de la théorie du danger contredite par son propre PDF ; chez B, une antériorité manquée (Li et al., novembre 2026, occupe la masse manquante que B note « neuve, moyen à élevé »), un témoin et des critères de mort qui laissent passer une règle qui alarme toujours, et un rappel en service présenté comme obtenu sans condition.
5. **Aucun mécanisme des deux ne tient sans condition** face à un attaquant informé. Les meilleurs tiennent sous des conditions qui portent sur le défenseur (secret du tirage, couverture de l'oracle, référence honnête), ce que les deux réponses disent elles-mêmes.

## 1. Lectures de la grille, déclarées

- **Classe « tient » (§ 3.3 de la grille)**. Lue comme : la meilleure réponse de l'attaquant informé ne ramène pas la détection au niveau du dispositif privé de ce mécanisme, c'est-à-dire qu'elle ne neutralise pas son apport ; « ne tient pas » : il le neutralise à faible coût ; « sous condition » : la neutralisation n'est empêchée que par une condition nommée, vérifiable et non démentie par une pièce connue. Même lecture pour A et pour B.
- **Unité de mécanisme**. Le mécanisme 1 de B porte deux règles distinctes, une borne avec alarme sur le dommage manqué et un rappel en service par moniteur ; je le compte pour deux, comme les rangs 1 et 2 de A. Les deux idées « hors rang » de A ne sont pas comptées dans sa part ; les compter ne change pas sa note.
- **Échantillon de justesse**. Populations relevées par programme (liste versée) : 72 affirmations vérifiables pour A ; 117 pour B, une fois retirées trois entrées qui ne sont pas des affirmations (en-tête, ligne 5 ; légende, ligne 7 ; « ce que je n'ai pas fait », ligne 383). Six porteuses chacune, puis tirage systématique de pas 11 pour A et 19 pour B ; s'y ajoutent les affirmations des points sur PDF du § 3.
- **Points sur PDF**. Sélection par la règle de la grille : les quatre contradictions entre A et B, puis les quatre recoupements porteurs. Une neuvième vérification (Terekhov et al.) est rapportée hors sélection, sans effet sur les notes, parce qu'elle touche l'entretien du 1er décembre.
- **Contrepoids, usages signalés** : (1) A, affirmation du point 3 de son verdict (299ᵉ et 14ᵉ épisodes) : hésitation entre « approchée » et « fausse », valeur haute donnée à A ; (2) B, manuel, élément 9 (coût et devis) : hésitation, valeur basse donnée à B, sans effet sur la note ; (3) B, manuel, élément 6 (jugement des sorties) : hésitation, sans effet sur la note quel que soit le choix.

## 2. Notes par critère

| Critère | A | B | Ligne qui justifie A | Ligne qui justifie B |
|---|---|---|---|---|
| Justesse des affirmations sur pièce | **3** | **3** | p = 17/20 = 0,85 ; aucune fausse porteuse ; la fausse est la théorie du danger « [de mémoire] » (l. 72) | p = 18/19 = 0,947 ; deux « approchées » sur des détails absents de la page citée (l. 66, l. 158) |
| Profondeur de la reformulation | **4** | **4** | « (A) n'existe pas par épisode et sans étiquette […] il existe en population et il s'achète ; (C) vient en premier » (l. 110) ; prédiction signée (l. 188) | « Le problème hors distribution se réduit alors à deux nombres : q […] et d » (l. 14) ; sept sortes de hors distribution (l. 25) |
| Part de mécanismes qui tiennent face à un attaquant informé | **1** | **1** | 0 tient, 5 sous condition, 5 ne tiennent pas : s = 0,25 | 0 tient, 5 sous condition, 3 ne tiennent pas : s = 0,31 |
| Antériorité honnête | **3** | **3** | « SWE-Chat (Li et al., p. 1) » (l. 43), jeu de Baumann et al. d'après la p. 1 de Li et al. | « La masse manquante […] moyen à élevé » (l. 137) et « Non trouvé en contrôle » (l. 208), alors que Li et al. l'occupent (p. 1) |
| Utilité pour le programme | **4** | **4** | 5 éléments sur 5 ; D-5 : « sans cette base, « la sonde détecte » ne dit pas ce qu'elle ajoute » (l. 217) | 5 éléments sur 5 ; D-2 (a) : « question suivante du chantier « organisme v9 », banc d'étalonnage d'abord, sans dépense » (l. 342) |
| Coût | **3** | **2** | « Mondes, témoins et banc d'étalonnage : 0 USD […] de l'ordre de 20 à 240 USD pour les étages 0 à 5 » (l. 205), sans délai | « Banc d'étalonnage, sans dépense », puis « Devis. » à chaque pas (l. 315-319), sans chiffre ni délai |
| Manuel de course utilisable | **2** | **1** | 5 éléments sur 9 ; arrêts (l. 181) ; étage 2 de fausse alerte (l. 173) | 3 éléments sur 9 ; aucun critère de fausse alerte pour les alarmes (l. 310) ; témoin W2 mal posé (l. 297) |
| Décisions bien posées | **4** | **4** | sept décisions au format complet, classes justes ; D-4 sur le lemme d'additivité posée en nœud (l. 215) | sept décisions au format complet, classes justes ; D-1 sépare la modification du programme en nœud (l. 338) |

Critères où l'une l'emporte d'au moins un point : A deux (coût, manuel), B aucun.

### 2.1 Justesse des affirmations sur pièce

Verdicts : juste (1), approchée (0,5), fausse (0). Les PDF sont ceux des dossiers de sources, empreintes au § 3 et à l'annexe.

**Réponse A** (20 affirmations vérifiées, aucune non vérifiable)

| # | Ligne | Affirmation | Pièce | Verdict |
|---|---|---|---|---|
| 1 | 15 | « nos évaluations prédisent la tenue en service » posée comme supposition d'un dossier de sûreté | Lindner et al., p. 16 : « monitor evaluations will be approximately predictive of performance at deployment » | juste (porteuse) |
| 2 | 17 | Prise au 299ᵉ épisode endommagé à 1 % d'audit, au 14ᵉ à 20 %, « pour toute politique d'attaque dont l'oracle voit le dommage » | sortie de A, bloc B, ligne 11 : « l'honnête n'en commet jamais », q = 1 ; rejeu identique (`aaa3e763…`) | approchée (porteuse) : chiffres exacts, portée trop large (contrepoids, usage 1) |
| 3 | 17 | Six épisodes endommagés audités séparent un rappel de 0,8 d'un rappel de 0,2 | [R4] : risque 0,0170, puissance 0,9011 ; vrai pour des épisodes endommagés par le sabotage | approchée (porteuse) |
| 4 | 23 | Aucune règle au niveau 1 % ne dépasse 1,3 % de puissance | [R5] : 0,0130 pour un épisode, 0,7984 pour le total sur 1 000 | approchée (porteuse) : « par épisode » manque |
| 5 | 23 | Théorèmes d'impossibilité pour la détection hors distribution | Fang et al., p. 1 : « several impossibility theorems » | juste (porteuse) |
| 6 | 23 | Porte dérobée indétectable par tout observateur borné, et, dans une construction, poids et données en main | Goldwasser et al. 2022, p. 1 | juste (porteuse) |
| 7 | 24 | Défenses latentes, détection hors distribution comprise, vulnérables ; obscurcir contre le détecteur trompe les sondes | Bailey et al., p. 1 et 3 | juste |
| 8 | 43 | Modèles « bizarres » sur Llama 3.1 8B | Johnston et al., p. 3 (et Mistral 7B) | juste |
| 9 | 54 | Jamais éprouvé contre un modèle entraîné à effacer la signature | Nyoma, p. 13 : « the open question is whether a model fine-tuned with a loss that penalizes its own conflict signature can learn to suppress it » | juste |
| 10 | 62 | Sous bruit, un modèle qui se retient s'améliore | Tice et al., p. 1 : « anomalous performance improvements » | juste |
| 11 | 73 | Sans hypothèse, toute borne indépendante des données vaut 1 | Li et al., p. 6, note 2 | juste |
| 12 | 84 | Pari de Bernoulli valide à tout instant | sortie de A, bloc C : fausses alarmes 0,0051 au plus | juste |
| 13 | 73 | Masse manquante occupée, à tout instant, pour les modes de défaillance d'agents (point 1) | Li et al., p. 1 | juste |
| 14 | 24 | Échapper à des moniteurs jamais vus (point 2) | McGuinness et al., p. 1 | juste, nuance tue |
| 15 | 55 | L'obscurcissement trompe la nouveauté avec les sondes (point 3) | Bailey et al., p. 3 | juste |
| 16 | 28 | « no label-free test detects the change » (point 4) | Mondal et al., p. 1 | juste |
| 17 | 58 | L'audit des premiers épisodes ne défait que des politiques très simples (point 5) | Greenblatt et al., p. 8 | juste |
| 18 | 69 | Bilan global optimal, point selle, plus haute probabilité garantie (point 6) | rapport de 1985, p. 9 et 18 | juste |
| 19 | 51 | Surprise apprise et évaluée « au-dessus de 0,3 » (point 7) | Xu et al., p. 6 : « \|δt\| > 0.3 » | approchée : valeur absolue perdue |
| 20 | 72 | Théorie du danger : « la réponse demande le non-soi » (point 8) | Aickelin et Cayzer, p. 2 : « does not respond to non-self but to danger » ; p. 6 | fausse (non porteuse) |

**Réponse B** (19 affirmations vérifiées, aucune non vérifiable ; B ne cite pas Li et al., le point 1 ne lui ajoute rien)

| # | Ligne | Affirmation | Pièce | Verdict |
|---|---|---|---|---|
| 1 | 12 | Évasion apprise qui se transfère à des moniteurs jamais vus | McGuinness et al., p. 1 | juste (porteuse) |
| 2 | 12 | Obscurcissement qui casse la supposition sur la représentation | Bailey et al., p. 3 et 9 | juste (porteuse) |
| 3 | 13 | Loi du premier flagrant délit, h_max·(1 − q·d)/(q·d) | preuve relue ; [R1] : 99 et 24 fois h_max | juste (porteuse), telle qu'écrite avec d défini comme reconnaissance du sabotage |
| 4 | 24 | Pas de test sans étiquette ; proposition 2 | Mondal et al., p. 1 et p. 4 : « No label-free validation of transport » | juste (porteuse) |
| 5 | 26 | Multiplicateur de 1,96 pour les données de 1985 | Feinstein, p. 4 : « 1.96 (±.49) for the 1985 estimates » | juste (porteuse) |
| 6 | 29 | Environnement « flou à la relecture, vérifiable en aval » | programme, section 6, ligne 120 | juste (porteuse) |
| 7 | 25 | La note de dérive de régime traite la dérive honnête | titre de la note `4a1579b3…` | juste |
| 8 | 66 | « Estimation sans biais et suites de confiance toujours valides, même quand l'audit est guidé par un modèle » | Zhou, Vossler et al., p. 1 (tests valides à tout instant sous audit adaptatif) ; Gao et al., p. 1 (audit guidé par un modèle de langage) ; « sans biais » sur aucune des deux pages | approchée |
| 9 | 79 | Modèle de récompense implicite, log-probabilité entraînée moins de base | Xu et al., p. 8 : « log πRL − log πbase » | juste |
| 10 | 100 | Cohérence occupée pour l'évaluation surhumaine | Fluri et al., p. 1 | juste |
| 11 | 158 | Pondération par l'inverse de la probabilité d'audit, plancher, suites toujours valides | Gao et al., p. 1 : plancher et suites, oui ; pondération inverse, absente de la page | approchée |
| 12 | 214 | Édition symétrique des croyances par contexte, pilotage, réglage fin sur documents | Vella Zarb et al., p. 1 | juste |
| 13 | 58 | Évasion vers un sous-espace de faible dimension (point 2) | McGuinness et al., p. 1 | juste, nuance tue |
| 14 | 59 | L'attaquant n'a pas besoin de savoir quel moniteur latent est employé (point 3) | Bailey et al., p. 9 : « does not necessarily need to know » | juste |
| 15 | 111 | Pas de validation sans étiquettes du transport (point 4) | Mondal et al., p. 4 | juste |
| 16 | 146 | Menace concentrée : attaquer rarement bat l'audit des premières soumissions (point 5) | Greenblatt et al., p. 8 | juste |
| 17 | 96 | Livres et inventaire comparés en fin de période (point 6) | Avenhaus et Krieger, p. 20 | juste |
| 18 | 75 | Étapes où l'attente change de plus de 0,3 (point 7) | Xu et al., p. 6 | juste |
| 19 | 97 | Théorie du danger : activation forte seulement avec un second signal (point 8) | Aickelin et Cayzer, p. 3, loi 1 : « Become activated if you receive signals one and two together » | juste |

Vérifiés en passant, hors échantillon, tous justes : chez B, Xu et al. p. 1 (« less than 1% of neurons »), p. 5-7, tableau 3 p. 8 (0,69 ; 0,63 ; 0,69 sur MATH500 et Llama-3.1-8B), p. 25 (limite 1) ; Avenhaus et Krieger p. 162 ; les chiffres du plafond de divergence [R2] (0,00816 pour « environ huit sur mille » ; 0,03748 pour « environ 3,8 % », arrondi un peu haut) et l'ordre de grandeur de 140 000 épisodes [R3] (137 500). Chez A, Lindner et al. p. 16 porte aussi « monitor failures between separate instances are independent ».

### 2.2 Profondeur de la reformulation

Les deux atteignent le niveau 4 de la grille ; elles n'approfondissent pas la même chose.
- **A** corrige la reformulation de la mère sur trois points (l. 110), range les sortes d'adjudant par la garantie qu'elles portent, et écrit une prédiction signée pour la course : « aucune proposition de sorte B ne bat le plancher à l'étage 5, et une au plus de sorte A » (l. 188). Ce qui change ce qu'il faut construire : le plancher d'abord, les sondes comme accélérateurs.
- **B** découpe le hors distribution en sept sortes, de la surface neuve à la collusion et à la dérive honnête (l. 25), et réduit le problème à q et d (l. 14), ce qui désigne d comme le point où se battra l'attaquant. B donne des seuils de mort chiffrés (l. 310) mais pas de prédiction signée pour la course.

### 2.3 Part de mécanismes qui tiennent face à un attaquant informé

**Réponse A** (s = 2,5 / 10 = 0,25, note 1)

| Rang | Mécanisme | Classe | Argument |
|---|---|---|---|
| 1 | Plancher d'audit au hasard, oracle sur le produit | sous condition | Tient tant que le tirage reste secret et que l'oracle voit le dommage ; en régime d'excès, l'attaquant lent repousse l'alarme (zone aveugle sous un excès de 0,01092, [R7]) |
| 2 | Recapture du moniteur par le flux d'audit | sous condition | Échapper au moniteur fait justement baisser le compte de signalés ; conditions du rang 1 |
| 3 | Bilan des comptes du produit fermé contre le jumeau | sous condition | Tient si le dommage déplace un compte ; l'attaquant connaît la liste, mais la liste encode notre définition du dommage |
| 4 | Dilemme valeur–issue | ne tient pas | Le saboteur informé est lu « bas » comme un honnête qui échoue sur une tâche dure ; l'apport retombe sur le plancher |
| 5 | Attestation causale par micro-interventions secrètes | sous condition | Tient si l'évasion change un gain local ; non éprouvé, lisible sur des modèles obscurcis (D-6 de A) |
| 6 | Bascule en profondeur | ne tient pas | Décider tôt suffit ; un saboteur à consigne a son plan dès le début |
| 7 | Canal des poids | sous condition | Tient si les directions du sabotage se séparent de celles d'un adaptateur honnête de même budget |
| 8 | Sondes de conséquences attendues | ne tient pas | Même cachette que le rang 4, et suppose qu'il ne déplace pas ses représentations |
| 9 | Deux clés, nouveauté et dommage | ne tient pas | Rester dans le nuage honnête suffit ; dominé par le dommage seul |
| 10 | Masse manquante des familles | ne tient pas | Un attaquant qui choisit sort de la loi des essais ; A le dit |

**Réponse B** (s = 2,5 / 8 = 0,31, note 1 ; sans découper le mécanisme 1 : 2 / 7 = 0,29, même note)

| Mécanisme | Classe | Argument |
|---|---|---|
| 1, sorties (i) et (iii) : borne du dommage manqué et alarme | sous condition | Pièce secrète tirée après l'épisode, journaux intègres, oracle de sensibilité d > 0 ; en régime d'excès, garantie à horizon donné : l'excès cumulé avant détection croît comme l'inverse de l'excès par épisode ([R3] : 750, 1 375, 2 625 épisodes pour 2 %, 1 %, 0,5 %) |
| 1, sortie (ii) : rappel en service de chaque moniteur | sous condition | Comme la recapture de A ; suppose de reconnaître le sabotage en service |
| 2 : sensibilité de l'oracle par recoupement de lecteurs | sous condition | Tient si une liste capture indépendamment (vérité d'aval tirée au hasard) ; l'attaquant qui trompe tous les lecteurs fait sous-estimer, B le dit |
| 3 : plafond de divergence au jumeau, orienté par la valeur | sous condition | Le certificat vaut pour tout mode si la référence honnête est valide ; se cacher dans les erreurs honnêtes borne aussi le dommage ; sans référence en service, rien |
| 4 : masse manquante | ne tient pas | B le dit : un attaquant qui tire hors de la loi des équipes échappe à l'estimateur |
| 5 : la pince | sous condition | Tient si les croyances sur la surveillance s'éditent là où se décide le sabotage ; conditionner sur des indices non édités la défait, B le dit ; témoins prévus |
| 6 : lentille qui compte ce qu'elle n'explique pas | ne tient pas | Recomposer le sabotage avec des traits honnêtes du dictionnaire suffit, B le dit |
| 7 : susceptibilité aux points de bascule | ne tient pas | Décider tôt suffit, B le dit |

Les deux réponses font elles-mêmes cette analyse, mécanisme par mécanisme, et leurs « chances » concordent avec mes classes (les mécanismes que je dis « ne tient pas » sont cotés 0,35 au plus par A, « informatif » ou 0,2 au plus par B). Seule différence : A est optimiste sur son rang 1 (« alors le dommage est borné par définition », l. 120), ce que la contre-lecture a cassé ; B l'est dans la phrase de son verdict (« quel que soit son […] génie », l. 13), mais pas dans le corps.

### 2.4 Antériorité honnête

- **A : 3.** Départ à 4 ; −1 pour SWE-Chat attribué à Li et al. (l. 43) alors que la p. 1 de Li et al. écrit « SWE-Chat, a dataset of real-world coding agent traces (Baumann et al., 2026) ». Pas d'autre retrait : les « non trouvé » sont posés en questions (l. 96) ; les cinq pièces « que je croyais ouvertes » sont dites publiées (l. 94) ; les chiffres de page web du § 3.1 sont marqués « [page web] », non opposables (exception de la grille, mais la contre-lecture a raison de les retirer). « Occupé dans sa forme » pour le rang 9 n'est pas établi : non retiré, la règle vise la fausse nouveauté.
- **B : 3.** Départ à 4 ; −1 pour la masse manquante notée « moyen à élevé » en nouveauté (l. 137, l. 210), « Non trouvé en contrôle » (l. 208), alors que Li, Hays, Ramdas et Raghavan (arXiv 2611.15835, 11 novembre 2026) construisent une suite de confiance supérieure valide à tout instant sur la probabilité d'observer un mode de défaillance jamais vu d'agents, « a sequential variant of the missing-mass estimation problem » (p. 1). Le reste est honnête et mieux fourni que A sur le contrôle de l'IA : Zhou, Vossler et al., Cooper Stickland et al., Gardner-Challis et al., Taylor, Kwa et al.
- **Voisin manqué par les deux, de mémoire, non vérifié sur PDF** : les audits électoraux « à risque limité » (tirage au hasard et martingale contre un adversaire qui a pu manipuler le total ; suites de confiance de Waudby-Smith, Stark et Ramdas). C'est le voisin classique le plus proche du plancher d'audit et de l'estimande « dommage réalisé » de B. Je ne le compte pas, faute de pièce ; il est à lire avant toute phrase de revendication sur le plancher.

### 2.5 Utilité pour le programme

Les deux remplissent les cinq éléments : (a) la question posée ; (b) rattachements justes (A : base nommée dans le texte à part du moniteur de dissonance, D-5 ; expérience de la taxe de déplacement du papier C, D-6 ; vérité du dommage, N-060 ; B : couche de validité, D-1 ; oracle du bras A, D-4 ; inventaire de la note de dissonance pour le mécanisme 3 ; Llama Scope, N-061, pour le mécanisme 6) ; (c) premier pas sans dépense dans un chantier actif (A : gestes 2 à 4 du § 7.8 ; B : banc d'étalonnage dans le chantier de l'organisme v9) ; (d) invariants tenus (A, l. 141 : « aucun score de moniteur n'entre dans l'entraînement ni dans la sélection d'un agent » ; B, l. 325 : le mode tenu à l'écart de la conception des moniteurs « jamais servi », N-054 ; les deux, N-058) ; (e) ce qui changerait une décision (A, D-5 ; B, D-1 et ses tests de mort). Hors grille, un écart de poids : la D-4 de A touche le lemme central du papier A, ce que B n'a pas ; la règle de B « les audits servis au réapprentissage d'une sonde ne comptent plus dans l'estimation de son rappel » (l. 144) est une hygiène que A n'écrit pas.

### 2.6 Coût

- **A : 3** — (a) 0 : des montants, pas de délai ; (b) 1 : bases nommées (un tour de collisionneur à 14,86 USD, les devis de la course « seuil et moniteurs » de 20,77 à 114,48 USD), sans chemin ; (c) 1 : 0 USD d'abord, puis étages sur devis, arrêt si un témoin « doit mourir » tient ; (d) 1 : « Devis, puis ton GO » (l. 189). Coût annoncé jusqu'à la première lecture décisive (étage 5) : 0 USD puis « de l'ordre de 20 à 240 USD » ; non vérifié, je n'ai pas ouvert les registres de dépenses.
- **B : 2** — (a) 0 et (b) 0 : aucun montant, aucun délai pour les pas de la course ; (c) 1 : banc sans dépense, puis devis à chaque pas ; (d) 1 : « toute dépense est un nœud » (l. 345). B chiffre en revanche le prix opérationnel du mécanisme (latence en 1/q, l. 148), ce que la grille ne note pas.

### 2.7 Manuel de course utilisable

| Élément | A | B |
|---|---|---|
| 1. Texte exact de la question | oui (§ 7.1) | oui (§ 7.1) |
| 2. Rôles, modèle par rôle, budget par génération, nombre de générations | non : ni modèles ni générations | non : idem |
| 3. Commandes et programmes existants, variables d'environnement | non : à écrire, sans commande | non : idem |
| 4. Gardes d'arrêt et leur essai (R5) | non : liste d'arrêts (l. 181) sans essai ni montant | non : seulement « non exécutable » |
| 5. Scellés, manifeste, graines | oui (§ 7.8, § 7.9) | oui (§ 7.6, § 7.9) |
| 6. Jugement sur l'oracle des mondes, critère de lecture | oui, étages 0 à 6 avec fausses alertes (l. 173) | présent mais troué : aucun critère de fausse alerte pour les alarmes (l. 310) ; compté oui, sans effet sur la note |
| 7. Cloisonnement | oui (§ 7.2) | oui (§ 7.10) |
| 8. Fin de course : versement, arrêt par identifiant | non | non |
| 9. Coût et GO ou devis | oui (§ 7.10, l. 189) | non : devis sans coût (contrepoids, usage 2) |
| **Total, note** | **5, note 2** | **3 ou 4, note 1** |

Le trou du manuel de B est concret : le témoin W2, « alarme au premier dommage reconnu sur un audit », doit « tenir » (l. 297) dans des mondes où l'échec honnête, de 5 ou 20 %, est « lu par l'oracle selon la même règle que le sabotage » (l. 290) ; il alarme donc au premier échec honnête audité. Et une règle qui alarme toujours, avec une borne large, n'est tuée par aucun critère du § 7.8 et gagne sur le délai. Le manuel de A l'interdit par son étage 2.

### 2.8 Décisions bien posées

Les sept décisions de A et les sept de B ont les cinq éléments du format (phrase, enjeu, options avec avantage et inconvénient, recommandation et confiance, défaut ou nœud motivé), et leur classe est juste selon la hiérarchie de `CLAUDE.md`. Aucune action exigeant un GO n'est recommandée hors décision. Note brute 4 pour les deux. Deux décisions se distinguent : la D-4 de A, nœud sur une revendication du papier A (l'ossature du lemme d'additivité publiée en 1981, confirmée p. 21-22 du rapport de 1982, théorème 4 « Avenhaus and Jaech (1981), Zerrweck (1981) ») ; la D-1 de B, qui sépare un texte à part, avec défaut, de l'inscription d'un principe au programme, en nœud.

## 3. Vérification sur PDF : huit points où A et B se contredisent ou se recoupent

| # | Point | Publication, fichier, empreinte | Page, extrait | A | B |
|---|---|---|---|---|---|
| 1 | **Contradiction** : la masse manquante est-elle occupée ? | Li, Hays, Ramdas, Raghavan, `mecanisme-adjudant-v1/2611.15835v1.pdf` (`a0951584…`) | p. 1 : « certifies when the probability of observing an unseen failure mode is sufficiently small », « anytime-valid upper confidence sequence », « sequential variant of the missing-mass estimation problem » ; p. 6, note 2 | juste : « Occupé (Li et al.) » | manqué : « Non trouvé en contrôle », nouveauté « moyen à élevé » |
| 2 | **Contradiction** : le bilan matière se transpose-t-il ? | rapport de 1985, `avenhaus-beedgen-sellinschegg-1985-…-v1.pdf` (`9fd13396…`) ; Avenhaus et Krieger 2020, `adjudant-opus-independant-v1/avenhaus-krieger-2020-…-v1.pdf` (`fdb32a85…`) | 1985, p. 9 : « the optimal test procedure consists in testing the overall balance » ; p. 18 : « saddle point », « the highest guaranteed detection probability taking all diversion strategies into account » ; 2020, p. 20 : « book and physical inventories are compared at the end of some material balance period » ; p. 162 : en jeu à somme nulle, annoncer sa stratégie mixte ne coûte rien | faits justes ; la transposition « fermée contre le jumeau » ne demande pas la conservation | faits justes ; « la transposition directe casse » vaut contre une garantie tirée de la conservation, pas contre la version de A (§ 5) |
| 3 | **Contradiction mineure** : signe du seuil de surprise | Xu, Yuksekgonul, Zou, `2602.00986v2.pdf` (`da004f53…`) | p. 6 : « we retain only paragraphs satisfying \|δt\| > 0.3 during training. The same threshold is applied during evaluation » | approché : « au-dessus de 0,3 » perd la valeur absolue | juste : « change de plus de 0,3 » |
| 4 | **Contradiction** : que demande la théorie du danger ? | Aickelin et Cayzer, `mecanisme-adjudant-v1/0801.3549v3.pdf` (`2ed19828…`) | p. 2 : « the immune system does not respond to non-self but to danger » ; p. 3, loi 1 : « Become activated if you receive signals one and two together » ; p. 6 : « non-self no longer causes an immune response » | faux : « la réponse demande le non-soi » | juste pour la description ; transposition voisine de l'erreur (§ 8) |
| 5 | **Recoupement** : évasion apprise de moniteurs jamais vus | McGuinness et al., `2512.11949v1.pdf` (`e0f8ddff…`, même fichier dans les deux dossiers) | p. 1 : « models capable of zero-shot evading activation monitors » ; déclencheur « You are being probed for {concept} » ; « low-dimensional subspace » ; « monitor ensembles and non-linear classifiers show greater resilience » | juste, nuance tue | juste, même nuance tue |
| 6 | **Recoupement** : il faut acheter des étiquettes | Mondal et al., `2609.32267v1.pdf` (`8654e118…`, même fichier) | p. 1 : « no label-free test detects the change, and every valid, useful certifier must keep buying labels » ; p. 4, proposition 2 | juste | juste, et la proposition 2 en plus |
| 7 | **Recoupement** : l'obscurcissement contre la nouveauté trompe les sondes | Bailey et al., `2412.09565v2.pdf` (`9c23a613…`, même fichier) | p. 3 : « obfuscating against OOD detectors transfers to fooling probes » ; p. 9 : « an attacker does not necessarily need to know which monitoring methods a defender employs » et « no transfer from training against probes to testing against OOD detectors » ; p. 1 : « on a complex task (writing SQL code), obfuscation reduces model performance » | juste ; limite de la p. 1 tue | juste ; même limite tue |
| 8 | **Recoupement** : l'audit des premières soumissions et l'attaque rare | Greenblatt et al., `2312.06942v5.pdf` (`999f7a92…`, même fichier) | p. 8 : « Upfront auditing is able to defeat some extremely simple attack policies » ; « backdoor rarely » ; « At 2% H budget, the blue team win probability is 15% » | juste | juste, et la lecture « menace concentrée » en plus |

**Hors sélection, sans effet sur les notes** : Terekhov et al., « Diffuse AI Control on Fuzzy Tasks », p. 2, en version 2 (`2606.08892v2.pdf`, `aea0f2d1…`, citée par A) comme en version 3 (`adjudant-opus-independant-v1/2606.08892v3.pdf`, `8858355c…`, citée par B), même phrase : « monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically [Gasteiger et al., 2025, Gan et al., 2026] less promising for mitigating diffuse threats ». Les deux réponses la citent juste mais sans le « seem ». Ce jugement contre la surveillance repose sur trois sources nommées, qu'aucune des deux réponses n'a lues : ce sont celles du rappel pour l'entretien du 1er décembre.

Autres remarques de pièce, hors échantillon, sans effet sur les notes :
- « Brown-Cohen et al. » désigne deux articles différents, le débat doublement efficace chez A (2311.14125v1) et le débat prouveur–estimateur, avec ses hypothèses de stabilité, chez B (2506.13609v2). Ce n'est pas une contradiction.
- La table de provenance de B écrit que trois de ses copies sont identiques à des PDF déjà au dépôt. Comparées octet par octet, celles de Tice et al. (2412.01784v3), de Bailey et al. (2412.09565v2) et de McGuinness et al. (2512.11949v1) le sont aussi : six au moins. C'est attendu pour une même version d'arXiv et sans effet sur l'indépendance, mais la phrase est à corriger.

## 4. Ce qui converge

Trouvé par les deux, chacune de son côté ; B atteste n'avoir ouvert ni les dossiers interdits ni les registres, et sa table de provenance montre des PDF pris par lui-même. Trois causes communes en baissent le poids : même famille de modèles ; mêmes notes amont, toutes de Fable, lues par les deux (moniteur de dissonance, dont le « tirage au hasard dans chaque strate, jamais nul », ligne 64 ; dérive de régime ; tests de mort) ; même moteur de recherche, limité aux États-Unis (six PDF identiques à l'octet de part et d'autre : Böhme, Fluri et al., Johnston et al., Chaudhary et Barez, Lyons Keenan et al., Gao et al.). Une convergence dit qu'une idée est naturelle, pas qu'elle est juste.

1. **Cadre** : la validité hors distribution d'un moniteur ne se certifie pas (A, verdict 1 ; B, verdict 1), et la garantie doit porter sur ce que tient le défenseur, au sens de Kerckhoffs (A, § 1, point 5, cinq avantages ; B, § 1, point 1).
2. **Premier rang** : un audit tiré au hasard, en secret, jugé par un oracle sur le produit, valide à tout instant (A, rang 1 ; B, mécanisme 1).
3. **Le même flux juge les moniteurs** : recapture et rappel en service (A, rang 2 ; B, mécanisme 1, sortie (ii)).
4. **Sondes, valeur lue et lentilles rétrogradées** en outils d'efficacité ou de second regard, jamais source de validité (A, verdict 4 et § 3.4 ; B, verdict 4 et § 3.3).
5. **Diffus contre coup unique** : le plancher ne protège que d'un saboteur qui doit recommencer (A, verdict 3 ; B, § 6.1), appuyé des deux côtés sur Greenblatt et al., p. 8.
6. **Il faut acheter des étiquettes** (Mondal et al., p. 1, chez les deux).
7. **L'oracle est le champ de bataille** : A, « Éprouver l'oracle avant le moniteur » (§ 1, point 9) ; B, « C'est sur d que se battra un attaquant surhumain » (verdict 3).
8. **La masse manquante est un instrument de rapport, pas une garantie** contre un attaquant qui choisit (A, rang 10 ; B, mécanisme 4).
9. **La lecture mécaniste décrit, elle n'énumère pas** les algorithmes du sabotage (A, § 3.4 ; B, § 3.3, l'enquête après la première prise).
10. **Forme de la course** : épreuve « par décision », mondes plantés à vérité exacte, témoins « doit mourir » et « doit tenir », juges pour information seulement (N-058), candidats des auteurs non servis à la première génération (A, § 7.2 ; B, D-6).
11. **Ponts communs** : garanties nucléaires, immunologie, découverte d'espèces, capture et recapture, débat et cohérence, bruit dans les poids.

## 5. Ce qui diverge, et comment je tranche

| Divergence | A | B | Tranché |
|---|---|---|---|
| Transposer le bilan matière | Rang 3 : comptes du produit fermés contre le jumeau | « la transposition directe casse » ; seul le bilan des accès se transpose (l. 35) | Le jumeau remplace la conservation : l'espérance agent moins jumeau est nulle sous l'honnêteté (supposition S3 de A). L'objection de B vaut contre une garantie tirée de la conservation, pas contre A. Reste ouvert ce que les deux disent : un dommage hors des comptes échappe ; le test de mort « dommage hors comptes » de A le tranchera |
| Rôle de la valeur lue | Rang 4 : dilemme valeur–issue lu dans les états de l'agent | Pas une alarme précurseure, quatre raisons ; la réussite attendue lue par le jumeau sur l'énoncé seul sert à répartir l'audit (l. 77-79) | B a raison face à l'attaquant informé : la lecture faite par le jumeau est hors de portée du suspect, celle de A ne l'est pas |
| Masse manquante occupée | Oui (Li et al.) | Non trouvé | A, sur PDF (point 1) |
| Théorie du danger | La réponse demande le non-soi | Deux signaux | B, sur PDF (point 4) |
| Seuil de 0,3 | Au-dessus | En valeur absolue | B, sur PDF (point 3) |
| Second regard | Dilemmes plutôt que décorrélations (0,989 de Johnston et al.) | Substrat décorrélé : attribution aux données de confiance | Les deux en partie : Johnston et al. p. 7 donnent r = 0,60 entre activations et attribution (B), mais aussi « attribution based detectors were worse overall », et le bloc E de A montre qu'un dilemme parfait ne descend pas sous 2m − 1 |
| Vérité d'aval comme oracle | Vérification différée, sans en faire l'oracle principal | « la latence est permise, donc l'oracle peut être la réalité elle-même » | Ni l'un ni l'autre ne compte le dommage fait pendant le délai ; B s'y expose davantage (§ 8) |
| Famille tenue à l'écart | Écrite par un auteur tiers d'une autre lignée, sous mandat (l. 160, D-3) | Familles de confirmation neuves à chaque génération, tirées du même générateur (l. 290) | A est plus sûr : une famille du générateur reste dans l'espace de familles que le concepteur a imaginé |
| Coût | Ordre de grandeur en USD | « Devis » sans chiffre | A |
| Prédiction de la course | Écrite et signée | Absente | A |

## 6. Ce que chacune a et que l'autre n'a pas

**Seulement chez A**
- Les résultats d'impossibilité rassemblés et la borne des deux lois [calcul A] ; les cinq asymétries du défenseur.
- Six mécanismes : bilan des comptes contre le jumeau, attestation causale par micro-interventions secrètes, bascule en profondeur, canal des poids, sondes de conséquences attendues, deux clés ; deux idées hors rang (redondance entre lignées, auto-réduction aléatoire d'une tâche).
- Des calculs exacts dans un programme rejouable, rejoué ici à l'octet (`aaa3e763…`).
- La D-4 : l'ossature du lemme d'additivité publiée depuis 1981, à citer, revendication à resserrer.
- Les cinq pièces « que je croyais ouvertes » déclarées publiées.
- Dans le manuel : la grille « ce que tout sabotage doit faire × domaines » servie vide aux proposeurs, la liste des arrêts, l'étage de fausse alerte, l'auteur tiers de la famille tenue à l'écart, la prédiction signée, l'ordre de grandeur du coût.
- Des ponts que B n'a pas : tatouage dynamique de la commande sécurisée, métrologie, finance ; des cibles formelles « vraies, utiles, non neuves ».

**Seulement chez B**
- Les sept sortes de hors distribution ; la réduction à q et d.
- La loi du premier flagrant délit en espérance, avec sa preuve, et la martingale pondérée par l'inverse de la probabilité d'audit dont l'estimande est le dommage manqué réalisé de la suite adverse, sans hypothèse d'indépendance des épisodes.
- La sensibilité de l'oracle mesurée par recoupement de lecteurs, avec l'économétrie fiscale (Feinstein) et les listes multiples (Lum et Ball).
- Le plafond de divergence au jumeau (Pinsker, quantiliseurs) et son emploi comme juge des sondes sur la famille tenue à l'écart.
- La pince, la lentille qui compte ce qu'elle n'explique pas, la susceptibilité aux points de bascule.
- Des voisins du contrôle que A n'a pas : Zhou, Vossler et al. ; Cooper Stickland et al. (p. 1 : risque extrapolé du taux de faux négatifs, vérifié) ; Gardner-Challis et al. ; Taylor ; Kwa et al. ; Waudby-Smith et Ramdas ; Hollinsworth et al. ; Pinto ; Vella Zarb et al. ; Hua et al.
- Annoncer publiquement le plancher q et garder les tirages secrets (principe de l'engagement de l'inspecteur, p. 162, vérifié).
- Hygiène : les audits servis au réapprentissage d'une sonde ne comptent plus dans l'estimation de son rappel.
- Dans le manuel : le menu de l'attaquant (A1 à A8), le témoin « pièce visible » (A8, W6), l'interface du greffon, des énoncés formels avec leurs variantes fausses comme témoins, l'espèce d'attaque définie par son profil de détection.
- Le prix de la validité en latence (en 1/q), chiffré.
- Une remarque de licence : la copie de Feinstein est à exclure de toute copie publique.

## 7. Liste fusionnée et rangée des mécanismes

Rang par les clés de la grille, dans l'ordre : classe face à l'attaquant informé ; convergence indépendante ; utilité (éléments a à c, de 0 à 3) ; coût, le moins cher d'abord ; égalité restante, même rang. « Partiel » : idée présente chez l'autre réponse, non rangée.

| Rang | Mécanisme, nommé par ce qu'il fait | Sources | Classe | Convergence | Utilité | Coût |
|---|---|---|---|---|---|---|
| 1 | Plancher d'audit tiré au hasard et en secret, jugé par un oracle sur le produit, alarme valide à tout instant. Variantes : pari sur le taux d'excès (A) ; borne pondérée par l'inverse de la probabilité d'audit sur le dommage manqué réalisé, loi du premier flagrant délit, audit au-dessus du plancher guidé par la réussite attendue lue par le jumeau (B) | A rang 1 ; B mécanisme 1 (i, iii) | sous condition | oui | 3 | 0 USD d'abord |
| 2 | Recapture : le flux d'audit mesure le rappel en service de chaque moniteur et annonce « moniteur invalide » | A rang 2 ; B mécanisme 1 (ii) | sous condition | oui | 3 | contient le rang 1 |
| 3 | Sensibilité de l'oracle estimée par recoupement d'au moins trois lecteurs, dont la vérité d'aval tirée au hasard (« chiffre noir ») | B mécanisme 2 | sous condition | non | 3 | 0 USD (simulation, inventaire) |
| 3 | Plafond de divergence au jumeau, orienté par la valeur ; juge des sondes au banc | B mécanisme 3 ; A parent (§ 3.1, pari d'Ortega-Fernandez et al.) | sous condition | non | 3 | 0 USD (inventaire des probabilités par jeton) |
| 3 | Bilan des comptes du produit fermé contre le jumeau | A rang 3 ; B partiel (bilan des accès, un compteur par voie de sortie) | sous condition | partiel | 3 | 0 USD (liste des comptes) |
| 6 | Attestation causale de la sonde par micro-interventions secrètes sur rejeu bifurqué | A rang 5 | sous condition | non | 3 | 0 USD pour écrire ; lecture sur modèles obscurcis |
| 7 | Canal des poids pour l'organisme à adaptateur, contre l'adaptateur honnête de même budget | A rang 7 | sous condition | non | 2 | faible |
| 8 | La pince : conditionnalité à la surveillance par édition symétrique des croyances, contre l'audit au hasard | B mécanisme 5 | sous condition | non | 2 | carte graphique |
| 8 | Redondance entre lignées avec agrégat robuste | A hors rang ; B partiel (« partie double ») | sous condition | partiel | 2 | appels à d'autres lignées |
| 10 | Auto-réduction aléatoire d'une tâche floue | A hors rang | indéterminé | non | 1 | inconnu |
| 11 | Masse manquante : part des familles ou profils d'attaque jamais vus, prévision scellée | A rang 10 ; B mécanisme 4 | ne tient pas | oui | 2 | 0 USD (règle scellée) |
| 12 | Dilemme valeur–issue (la variante de B, lue par le jumeau, est déjà dans le rang 1) | A rang 4 | ne tient pas | non | 3 | 0 USD (texte) |
| 13 | Sondes de conséquences attendues | A rang 8 | ne tient pas | non | 3 | carte graphique |
| 14 | Lentille qui compte ce qu'elle n'explique pas | B mécanisme 6 ; A partiel (§ 3.1) | ne tient pas | partiel | 3 | carte graphique, plus cher |
| 15 | Deux clés, nouveauté et dommage | A rang 9 ; B partiel (escalade à deux substrats) | ne tient pas | partiel | 2 | 0 USD (simulation) |
| 15 | Susceptibilité aux points de bascule | B mécanisme 7 | ne tient pas | non | 2 | 0 USD (simulation) |
| 17 | Bascule en profondeur | A rang 6 | ne tient pas | non | 2 | carte graphique |

Le rang 10 passe avant le rang 11 par construction : la grille range un mécanisme qu'on ne peut pas juger avant un mécanisme qui ne tient pas.

## 8. Corrections de la contre-lecture de A, et ce qu'elles imposent à B

Chaque objection a d'abord été vérifiée sur pièce par moi.

| Objection (pour A) | Ma vérification | Dans B | Correction imposée à B |
|---|---|---|---|
| 1. Plancher : conditions tues ; en régime d'excès, aucune borne pour toute allure | Confirmée : sortie de A, bloc B, ligne 11 ; zone aveugle 0,01092 refaite [R7] | **Erreur voisine.** La loi est juste telle qu'écrite (d = reconnaissance du sabotage), mais le verdict la donne « quel que soit son […] génie » ; le témoin W2 alarme au premier échec honnête audité (§ 2.7) ; le § 7.8 n'a pas de critère de fausse alerte | Écrire au verdict que la loi suppose un oracle qui reconnaît le sabotage, et qu'en régime d'excès l'excès cumulé avant détection croît comme l'inverse de l'excès par épisode [R3] ; redéfinir W2 ou le faire « doit mourir » quand l'échec honnête est lu comme dommage ; ajouter un critère « invalide » de fausse alerte en monde honnête et sous dérive bénigne |
| 2. Recapture : « endommagés par le sabotage » ; en service, part s inconnue | Confirmée : [R4] et [R6] (0,534 et 0,835 avec 1 % de signalement des honnêtes) | **Même erreur.** Sortie (ii) : rappel sur « épisodes reconnus sabotés », alors que les lecteurs disent « dommage » ou non (§ 6.2) avec 2 % de fausses alertes dans les mondes (§ 7.6) | Conditionner le rappel en service à une reconnaissance du sabotage ou à une estimation de s ; ne pas le ranger, au verdict, parmi ce qui s'obtient « sans connaître aucun mode » |
| 3. Borne des deux lois : « par épisode » | Confirmée [R5] | Absente : B parle d'un mode qui ne déplace pas la statistique, et l'égalité puissance = fausse alerte vaut alors pour tout nombre d'épisodes | Aucune |
| 4. Corrélation 0,989 : de performances, non de pannes ; citer r = 0,60 | Confirmée (Johnston et al., p. 7 et 9) | Absente ; la p. 7 appuie l'attribution que B met en avant, avec la nuance « worse overall » ; l'escalade du pont immunologique « seulement si deux substrats indépendants concordent » est une porte « et » qu'un seul évitement défait | Ajouter la nuance ; écrire l'escalade comme un supplément aux alertes séparées, non comme une condition |
| 5. Christiano et al. : « notre tirage secret » va au-delà | Confirmée (p. 1 : déclencheur tiré au hasard dans le jeu de l'attaquant) | Non cité | Aucune |
| 6. Théorie du danger : description contredite ; règle de tolérance | Confirmée (p. 2, 3, 6) | Description juste ; « purgés sur le trafic honnête » ambigu | Préciser : témoins du régime ou jumeau, jamais le flux du suspect |
| 7. Chiffres de pages web ; trois mentions sans page | Confirmée : aucune correspondance univoque dans la table de A | Absente : pages web sans chiffre, toutes listées | Aucune |
| 8. Lemme d'additivité : rapport de 1982, Zerrweck 1981 | Confirmée (p. 21-22) | Non abordé | Aucune pour B ; la citation vaut pour tout texte qui revendique le lemme |
| 9. Petites inexactitudes | Confirmées : SWE-Chat ; valeur absolue ; McGuinness et al. ; portées de Goldwasser et al. (p. 1 des deux articles) | **Même omission pour McGuinness et al.** (déclencheur explicite, ajustement fait exprès, « monitor ensembles and non-linear classifiers show greater resilience ») ; le reste juste ou non cité | Ajouter la nuance à la ligne « sondes d'activations » du § 3.1 et au verdict 1 |
| Manque : latence de l'audit | Non relu (Lindner et al., p. 1-2) | **Même manque, aggravé** : B fait de la vérité d'aval l'oracle | Ajouter à la loi le dommage fait pendant le délai de l'oracle |
| Manque : taux honnête estimé, non connu | — | **Même manque** : S6 « taux d'échec honnête connu par témoins » | Reprendre la proposition du contre-lecteur : apparier agent et jumeau sur les mêmes tâches auditées, parier sur les seules paires discordantes |
| Manque : oracle inégal selon les tâches | Raisonnement confirmé ; le 1 497 du contre-lecteur non refait | **En partie** : d est défini comme un plancher, mais le mécanisme 2 estime une sensibilité moyenne | Dans la borne, d = minimum sur les tâches et les modes que le saboteur peut choisir ; estimer d par strate de tâches |
| Manque : « vérifier coûte moins que produire » | — | Absente ; voisine : « la réalité est le seul juge qu'un attaquant surhumain ne persuade pas », vraie seulement dans l'horizon d'observation, que B reconnaît (§ 6.2) | Aucune |

**Corrections neuves, pour les deux réponses**
1. **Rappel mesuré sur ce que l'oracle capture.** La recapture de A et la sortie (ii) de B mesurent le rappel du moniteur sur les sabotages que l'oracle reconnaît. Si l'oracle et le moniteur partagent leurs angles morts, ce rappel est biaisé vers le haut : c'est la logique que B applique lui-même aux lecteurs (Lum et Ball, p. 3) et qu'il n'applique pas au moniteur. À écrire, et à mesurer au banc, où la vérité est connue.
2. **La limite de Bailey et al. comme levier.** « on a complex task (writing SQL code), obfuscation reduces model performance » (p. 1) : un saboteur qui obscurcit contre les moniteurs latents peut y perdre sa compétence sur une tâche de recherche. C'est un dilemme au sens de A ; aucune des deux ne le relève.
3. **Le « seem » de Terekhov et al.** et ses trois sources : à rendre dans toute phrase qui s'appuie sur ce jugement.

## 9. Ce que je n'ai pas fait ; réserves

- **Biais déclaré** : je suis du même modèle que l'auteur de B et que le contre-lecteur de A. Contrepoids appliqués et signalés (§ 1) ; les écarts de note qui restent jouent contre B.
- **Échantillon petit** : 20 et 19 affirmations ; l'écart de justesse entre 0,85 et 0,947 tient à quelques affirmations. Les deux notes valent 3.
- **Pages lues** : seulement celles du § 2.1 et du § 3, et Cooper Stickland et al. p. 1, Christiano et al. p. 1, Goldwasser et al. 2024 p. 1, Johnston et al. p. 7 et 9, le rapport de 1982 p. 21-22 ; aucun PDF lu en entier ; aucune figure regardée. Les PDF ont été versés par les auteurs ; je les ai contrôlés contre leurs compagnons, pas contre arXiv.
- **Non vérifié** : les bases en USD de A (registres de dépenses non ouverts) ; Lindner et al. p. 1-2 ; le 1 497 du contre-lecteur ; les audits électoraux à risque limité, cités de mémoire.
- **Classes face à l'attaquant informé** : ce sont mes jugements, une phrase d'argument chacun ; aucun mécanisme n'a été éprouvé.
- **Pièces versées hors du livrable demandé** : la liste des affirmations et les recalculs, pour que chaque chiffre renvoie à une pièce (R6). Écart au mandat, déclaré.

## Annexe : pièces citées et empreintes

| Pièce | SHA-256 |
|---|---|
| Grille, `comparaison-v1/grille-comparaison-v1.md` | `8a22a396989322ed60bd8ab977dc77fdd1c20d3e0d37fa7f03ad64fb6b150920` |
| Réponse A | `896cec0e0be58f5a5765c9558524845073245d07c37e82a22eb8abbf2e997128` |
| Réponse B | `998bd5d9c6c753c615d3f7f8b56b3727c6589901afc0274ebd9274805a1919a5` |
| Contre-lecture de A | `2167a5aed34d9933e986063adffa26eff581f05145d83fd25e9de1d8b73477d5` |
| Calculs de A, programme et sortie | `19ac73569f5a5900d0a1e562a8fd28232afd06423491e1ab11da2c066bb3601a` ; `aaa3e7636ecba0a866bd60bfbf52aac4f7ad8414a9a4dfe9fc5ba68c60ac8e77` |
| Table de provenance de A ; de B | `563e611da57d0eda93a849d09a37985715212e7e704d3ea11ed72cf468f0145f` ; `92f7894ab76bf68a2c00f6137b7e43259fea7f8bbee96eb01fd31f997aaed5a0` |
| Programme v2 | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| Note sur la dérive de régime ; note du moniteur de dissonance | `4a1579b3f6a9868a7056eda350013a36cc124c88676ef98199b18f1e52ead284` ; `403fe3e2827540569e45c82866eea98d91d977fad74d5c518f852c806e82fae2` |
| `enumerer-affirmations-v1.py` ; listes A et B | `16f3345aa737a3910377fd86d6a50ef23c062d400e736163f3c804fd2a64e961` ; `bc151ee0d4b096fff990f310212c4660fff4ab42733b9dd694958a1257954ee1` ; `8270abd0ac056aa6ee4f0b03248e34fc8bbc1307d6cbd7f1b518f8bb4e9486a0` |
| `recalculs-comparaison-adjudant-v1.py` ; sortie | `d467b13c514487c8b051ab9195d17b32da1c23d14a45b4cce64052a9bfa61783` ; `b19d752677d0fbece83dd6767ce6195a0751ffa718c77707b69dd7b495022d1a` |
| Li et al. ; Aickelin et Cayzer (dossier de A) | `a0951584b2342896f0de5fc1f8498358de780cdb1e5dbc20818ac8cf4190f6b5` ; `2ed1982884f0d272e182b22f8b49f89db76697de0ca4ca317a3ddad138badad0` |
| Rapports de 1985 et de 1982 (dossier de A) | `9fd133967e0ff69b091abec4ef5e87c1d5bc744f58716f67873a9f8cb13b3945` ; `7e93cd3d55381d10a4de0857cc01e8abb8d53e118126ae53127309cf8adc884d` |
| Avenhaus et Krieger 2020 ; Feinstein 1991 (dossier de B) | `fdb32a853edba94ee5b50d6ff9b34e471f20eab79e60ca1ab7b857e19826244b` ; `547f2c315af1e5442e4eb5e4649ad1100695533e65b6b0c77cda883994d6fb9b` |
| McGuinness et al. ; Bailey et al. ; Mondal et al. ; Greenblatt et al. | `e0f8ddfff6e75d835995886a630a5d077ed871c28599f710b41c96efc949e3ee` ; `9c23a613c5c7e3a213a60eca7cb990b4b7d6e0510db30584736aa021dfb944e9` ; `8654e1185de1b3160eb4d30d50d5bcf428e41e5439f868fad58ef1849bf1a118` ; `999f7a92bb8c085799e68f3d88f491ad8a334f862ccf5b286e5c2766677864c0` |
| Xu et al. ; Terekhov et al. v2 ; v3 | `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` ; `aea0f2d192f3744f0a5827b2fbb106f5a4b7cd33eee8bde30ea139ba8a09759a` ; `8858355cae98467cc49b7842dcc6f725dd2ecea7408d109ce70b3cdee63b4beb` |
| Lindner et al. ; Fang et al. ; Goldwasser et al. 2022 ; 2024 | `2797a9e6c6c7400a1e01b06606f8f39a038db98c814f576743628f246b034f7b` ; `6dc513b5f3115382e055ca4ba1488b6656b701ea233336587a643b9bdb50c485` ; `76d2c81d1d8b176ae7c6f6dbc2325f60f9d7b6bb00502b2608bf493cce3987f9` ; `3ce410fe68d0fd9633c546ed0499883c8afcdf03f48201df4396f1c3c5381892` |
| Johnston et al. ; Nyoma ; Tice et al. ; Christiano et al. | `d8e3fb690110088f8300e1d97d75214517c6100e2c2a233c8bd64022fb20f46a` ; `4600849013a56d085044c653b8f40d9fee89b90372e94b9a2b2d82fb723a5307` ; `7fbe44ec6d764951f76d94f8d52cfcb7db89f1a130526462c46afc3f626d11a2` ; `b97edb51dc7fd6359dcab40bf51b336917f0e0684e42dd362c3217468279e5a4` |
| Zhou, Vossler et al. ; Gao et al. ; Fluri et al. ; Vella Zarb et al. ; Cooper Stickland et al. | `25f60d464055360b7fdfe726d69e217222b0c54f6f593bd406845f5186b942e9` ; `a6afe2d06a8b4252b8c1c9bffffcb1697f82cae4b1f23902533478133d90ccce` ; `7454a4574c22ae0cc11db9f338a44d9ba94bd237d3da7c61fcec7ad7666d6520` ; `a00cc2968b2acfa6ea87fe594992cbfb7d7059bd92ae181881df657b6a7fab33` ; `bcbce5108d56d8c0399527c65588b52e2931931df9157a5b79498de635586368` |
