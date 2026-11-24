# Rapport de priorisation et d'impact pour l'organisme d'idéation — reclassement à la lumière de l'attelage du plan Turing — v2

- **Nature.** Pièce de travail (classe C). Réponse à la question de Lazar du 24 novembre : « faut-il corriger le rapport de priorisation pour l'organisme avec le plan Turing et son attelage ? »
- **Ce que cette v2 n'est pas.** Elle ne réécrit pas le rapport du 23 novembre (`docs/notes/idee-interessante-v1/lot-8/rapport-priorites-et-impact-organisme-2026-11-23-v1.md`, `88d80f76…`), qui reste tel quel : c'est la photographie du 23. Elle le reclasse.
- **Sources.** Note de Fable en effort maximal sur l'attelage (`docs/notes/attelage-plan-turing-v1/attelage-plan-turing-organisme-fable-max-v1.md`, `5aa73e46…`), citée « note, § x » ; inventaire des pistes du plan Turing (`docs/notes/inventaire-plan-turing-v1/inventaire-pistes-plan-turing-depuis-23-novembre-v1.md`, `65ce3c09…`) ; décisions du 22 novembre sur les puits étroits (`docs/notes/demandes-fable-api-2026-11-22-v1/synthese-protocole-x-puits-etroits-v2.md`, `6112172f…`, § 9) ; décisions de Lazar sur les nœuds de l'attelage (GO-2026-11-24-38) ; réponse à la question 5 du directeur du 24 et errata du même dossier (branche `idees/questions-directeur-2026-11-24-v1`, commit `ee6b868c7`, non fusionnée : `reponse-q5-carbon-fable-et-plan-turing-v1.md`, `0bdc9810…` ; erratum transversal sur κ et l'hypergraphe, `72afe693…` ; errata des questions 5 et 7).
- **Auteur.** Opus 5.5, sous-agent de la mère, 24 novembre 2026. Rien de neuf au-delà de ces pièces ; tout chiffre renvoie à elles.

## 0. Réponse

**Oui, il faut le corriger, par cette v2 et non par réécriture.** L'ordre du 23 plaçait en tête des épreuves sur corpus réels du *choix des lieux*, avant tout instrument ; l'attelage place d'abord l'instrument (cible, hasard, mondes plantés), puis la première mesure de l'organisme, et ne garde les épreuves sur corpus qu'en cinquième étape, réécrites. Sur sept expériences et cinq leviers du 23, **un seul meurt, la version rétrospective des détecteurs sémantiques**, et la lecture des neurones de récompense sort de l'attelage ; tous les autres sont **différés ou transformés** ; aucun ne reste au premier rang.

## 1. Ce que la méthode de classement du 23 avait de faux

Le rapport classait par `score = gain × facilité × portée × découverte / coût`, chaque terme noté de 1 à 5. La méthode est fausse, pas seulement mal réglée :

1. **Elle ne vise pas la question posée.** La question du directeur est : l'organisme cherche-t-il les puits étroits et profonds mieux que le hasard ? Aucune des sept expériences du 23 ne compare une recherche au hasard ; toutes éprouvent un *sélecteur de lieux* sur un corpus. Le score ne distinguait pas les trois fonctions que l'attelage sépare — choisir où chercher, faire naître l'idée, la reconnaître — qui n'ont ni le même hasard ni le même test (note, § 1.1, point 2).
2. **Elle ignore les dépendances.** Une épreuve sur le passé ne se lit qu'avec une mesure validée contre une vérité plantée ; le rapport mettait les mondes plantés après (« tout le reste … doit s'appuyer sur ce qui aura survécu à ces trois réfutations »). C'est l'inverse de « l'évaluateur d'abord », principe qui court d'octobre à novembre sans rupture (inventaire, § 3 ; note, § 1.1, point 4).
3. **Elle multiplie des rangs.** Un produit de notes ordinales de 1 à 5 n'a pas de sens arithmétique ; ici il sature : six expériences sur sept ont 5 en gain et 5 en portée, et six sur sept ont 1 en coût, de sorte que le dénominateur ne départage rien et que facilité et coût comptent deux fois la même chose.
4. **« Potentiel de découverte majeure » est un juge-modèle déguisé.** C'est une note d'avis, sans mesure, exactement ce que la définition de la cible exclut (note, § 3.1 : cible définie sans juge-modèle).
5. **Elle ne demande ni « ce qui tue » ni les faits de données.** La facilité 5 donnée à l'épreuve sur la base ouverte de relations biomédicales PubTator 3 n'a pas survécu à la lecture du fichier (§ 2 ci-dessous). L'attelage écrit pour chaque étape ce qu'elle tranche et ce qui la tue, et commence par les données brutes (note, § 1.2 et § 4.1).
6. **Elle se contredit.** Dans la partie 2, le levier classé premier a 187,5 et le deuxième 500 ; dans la partie 1, l'expérience classée sixième (500) passe après deux expériences à 400. L'ordre ne suit pas le score.
7. **Elle lit un accord comme une preuve.** Le « consensus remarquable » de cinq modèles n'est pas une validation extérieure : ces modèles partagent une culture, et la question oriente une part de l'accord (synthèse du 22, § 8, point 5).

**Méthode qui la remplace** : l'ordre du moins cher au plus cher de l'attelage, avec pour chaque étape ce qu'elle tranche, ce qui la tue et ce dont elle dépend (note, § 4.1) ; pour les sélecteurs, le test comme prévision contre un tirage au hasard et contre les bases simples (note, § 3.2).

## 2. Erreurs factuelles relevées depuis le 23

| Affirmation du 23 ou de la charte | Ce qu'on sait depuis | Renvoi |
|---|---|---|
| Épreuve « le pont suit-il la carte ? » sur PubTator 3 : « aucun blocage », démarrable « en 0 heure », 3 à 4 jours | le fichier des relations n'a **aucune date** ; huit types listés dans le fichier, douze dans l'article selon une réponse du 24, à trancher à la source ; le préenregistrement, rédigé par Carbon (écart d'auteur), est **non scellable** : six bloquants, onze majeurs (script d'épreuve plantée introuvable, fécondité fondée sur des auteurs absents, porte incompatible avec l'effet prédit, règles de réfutation contradictoires) | note, § 3.0 et § 3.4 ; contre-lecture `bd528999…` |
| Notes d'intérêt de Gu et Krenn : « réanalyse immédiate » dès la semaine 1 | l'identité des deux concepts de chaque paire n'est probablement pas publique : sans elle, le calcul par paire n'est pas faisable ; aucun préenregistrement | note, § 3.4 ; fiche de faisabilité `1736e5f0…` |
| Détecteurs de signaux dans la littérature d'alignement « testables d'abord rétrospectivement » sur l'archive arXiv coupée à 2024 | la version lexicale a tourné et est **réfutée** (aire 0,1667, corrélation de rang −0,6273, dominée par le volume ; l'ancienneté seule atteint 0,86 dans une partition) ; la version sémantique par modèle de langage ne peut pas se valider en rétrospectif, le modèle connaissant la suite | rapport `0a617ab1…` ; note, § 3.3 et § 3.8, point 6 |
| « Rétrodiction 7 sur 8 » de la cartographie des verrous (postérieure au rapport, citée par la charte comme validation) | ce n'est pas une rétrodiction : c'est un **rappel sur huit transitions choisies par l'auteur**, sans négatifs, sans taux de base, sans base concurrente ; elle contrôle le collecteur, non la capacité de la carte à prédire où naissent les percées ; la cartographie n'a pas été auditée | `temoins-externes-et-protocole-v1.md`, § 4 ; note, § 3.0, correction (a) |
| Sources LaTeX de l'archive arXiv « libres » | l'accès en masse est en compartiments payés par le demandeur (page vue le 24, à vérifier) : un échantillon stratifié article par article est gratuit, l'archive entière est une dépense | note, § 3.4 |
| Génération indépendante multi-familles « prouvée supérieure » au remue-méninges groupé | aucune référence vérifiée dans le rapport ; l'attelage la traite en hypothèse, mesurée par le comparateur « même effectif sans échange » ; confiance de Fable que la société d'agents ajoute quelque chose : 0,35 | note, § 3.5 et § 4.6 |
| Graphe causal biomédical daté : « neutralise le biais du survivant » | le plan de Carbon conditionne sur les paires nées (fécondité seule, paires nées en 2018) et ne teste pas la naissance : l'affirmation est une erreur partielle | question 5, § 3, ligne « Première expérience » ; erratum 1 de la question 5 |
| Compression croisée : « mesure exacte et infalsifiable » du gain inter-domaines | le gain de compression est exact pour un compresseur donné ; son lien avec la profondeur n'est pas validé : audit de réemploi d'abord, estimateur de profondeur ensuite. Bowers et al. (compresseur de bibliothèques Stitch) : de mémoire, à vérifier sur PDF | note, § 3.2, ligne 8 ; annexe |

## 3. Les sept expériences du 23, reclassées

| Rang du 23 | Expérience | Statut v2 | Place dans l'attelage et raison | Renvoi |
|---|---|---|---|---|
| 1 | « Le pont suit-il la carte ? » sur PubTator 3 (IDE-2026-11-23-027) | **transformé et différé** | idée saine, sélecteur gardé au premier rang (interaction de la surprise et de la serrure). Sa garde sur monde planté entre à l'étape 2 ; l'épreuve, réécrite par Fable avec une spline de distance et une permutation des signes, à l'étape 5, après les faits de données de l'étape 0 (source des dates et des auteurs, types réels, ordre des concepts) | note, § 3.2 ligne 1 ; § 3.7 ; § 4.1 |
| 2 | « Surface et structure » sur les notes de Gu et Krenn, bras A et C (IDE-2026-11-23-028) | **différé, scindé** | bras C (prédiction hors temps) à l'étape 5, sur le graphe de concepts daté ; bras A (réanalyse par paire) à l'étape 5 bis, suspendu à la publicité des identités de concepts | note, § 3.7 ; § 3.4 |
| 3 | Macros LaTeX et arbres d'équations avant les algèbres amassées (IDE-2026-11-23-032) | **différé, transformé** | « attendre » : énoncé d'un seul modèle ; un cas historique unique est une anecdote. D'abord un monde de signaux plantés, puis un ensemble à risque et un échantillon stratifié de sources LaTeX ; étape 5 bis, janvier | note, § 3.2 ligne 10 ; § 3.7 |
| 4 | Formes d'équations anonymisées, archive arXiv 2000-2014 vers 2015-2018 (IDE-2026-11-23-025) | **différé** | rangé avec la ligne précédente, à l'étape 5 bis, sur ensemble à risque et échantillon stratifié ; l'accès en masse est une dépense (nœud 8, plus tard) | note, § 3.7 ; § 3.4 |
| 5 | Graphe causal biomédical daté avec permutation des signes (STIMULATES contre INHIBITS ; IDE-2026-11-23-026) | **transformé ; source non placée** | son contrôle — la permutation des signes — entre dans le préenregistrement réécrit du rang 1 (« permutation des signes à côté de celle des types ») ; la réponse à la question 5 le dit aussi : fusion dans l'épreuve du pont (amendement A3). La note ne nomme pas la base SemMedDB, qui demande un compte (nœud du directeur) : à décider, PubTator 3 restant la source de premier rang | note, § 3.2 ligne 1 ; question 5, § 3 et § 8 |
| 6 | Scissions conceptuelles avant publication (IDE-2026-11-23-033) | **différé, transformé** | sélecteur « en attente » d'un préenregistrement ; l'événement doit être désigné par règle (scissions de descripteurs du vocabulaire d'indexation de PubMed, par année), non par cas choisis ; épreuve datée à l'étape 5 bis ; l'opérateur devient un bras de l'organisme attelé aux étapes 4 et 7 ; déjà plantable comme monde | note, § 3.2 ligne 9 ; § 3.7 |
| 7 | Extraction de relations typées sur Gu et Krenn (bras B) et lecture de neurones de récompense (IDE-2026-11-23-028, bras B et H10) | **hors de l'attelage v1** (neurones) ; **non placé** (bras B) | la lecture de neurones de récompense est hors de l'attelage ; le signal interne de surprise, hors de la v1. Le graphe de Gu et Krenn n'a pas de relations typées ; une extraction par un modèle postérieur à la date de gel est exclue d'une rétrodiction par la règle d'ingestion | note, § 3.2 ligne 16 ; § 3.4 ; § 3.7 |

## 4. Les cinq leviers et les recommandations du 23, reclassés

| Rang du 23 | Levier | Statut v2 | Place et raison | Renvoi |
|---|---|---|---|---|
| 1 | Cycle éveil-sommeil avec compression de bibliothèque sur plusieurs bassins | **différé** | audit de réemploi des compresseurs à l'étape 0 ; opérateur et mesure de profondeur à l'étape 7 ; sélecteur « en attente » | note, § 3.2 ligne 8 ; § 3.7 |
| 2 | Opérateur de scission et obstructions de faisceau | **différé, gardé comme bras** | bras à rendement mesuré, avec son bras hasard (étapes 4 et 7) ; épreuve datée à l'étape 5 bis | note, § 3.6 ; § 3.7 |
| 3 | Détecteurs sémantiques des cinq signaux sur la littérature d'alignement | **mort en rétrospectif ; prospectif seulement** | fuite du futur ; étape 9, pas avant février ; avant toute carte relationnelle des tensions, un monde de signaux plantés | note, § 3.2 ligne 14 ; § 3.3 ; § 3.8 |
| 4 | Hypergraphes, résolvantes de chemins, foncteurs partiels | **transformé** | raffinement de la serrure ; second monde du banc des correspondances plantées (une relation correspond à une chaîne de deux), étape 2. L'objet n'est ni l'hypergraphe de Carbon (qui n'écrit nulle part « hypergraphe ») ni celui de Fable : le dossier du 24 recommande un **hypergraphe fusionné**, orienté des prémisses vers la conclusion (question 7, § 5 ; erratum transversal, § 2) | note, § 3.3 ; § 3.7 |
| 5 | Protocole de vérité terrain sans fuite temporelle | **gardé, promu** | règle transversale dès l'étape 0, en trois régimes (long sans modèle de langage ; court après la coupure ; prospectif) ; la consigne d'ignorer ce qu'on sait ne vaut rien. Le petit modèle à coupure pré-1900 n'est pas placé par la note | note, § 3.3 ; § 3.7 |

**Recommandations et nœuds du 23.**
- *Génération indépendante avant confrontation* : **gardée comme conception** (proposeurs sans vue des autres), **non comme fait** ; mesurée (note, § 3.6 et § 3.5).
- *Collisionneur groupé du lot 8 et des dossiers 1 à 6* : **hors du chemin critique** ; aucune cellule valide sur dix-huit ; l'attelage n'en dépend pas (note, § 3.0).
- *Audit de réemploi des compresseurs de bibliothèques* : **gardé**, étape 0 (d).
- *Choix PubTator 3 contre SemMedDB* : PubTator 3 gardé, avec une source de dates à nommer et empreinter (instantanés d'iCite ou fichiers annuels de PubMed, à vérifier) (note, § 3.4).
- *« Préenregistrer immédiatement » les deux épreuves sans dépense* : **remplacé** : faits de données par Opus avant le 2 décembre, textes par Fable ensuite, selon l'économie de Fable.
- *Ne dégeler l'organisme qu'avec ses nouveaux opérateurs dotés d'un oracle* : **gardé dans l'esprit, transformé** : l'organisme entre en noyau minimal gelé, les opérateurs y sont des bras mesurés, et un seul socle sert l'attelage et la course d'auto-conception (nœud 3, a) (note, § 3.6 ; § 4.5).

## 5. Le nouvel ordre

1. **Étape 0, 25 novembre au 1er décembre, sans Fable, 0 dollar** : faits de données de PubTator 3 ; plomberie du banc ; audit du goulot ; lecture sur PDF des voisins ; audit de réemploi des compresseurs ; dépouillement du remue-méninges des 2 et 3 novembre.
2. **Étape 1, 2 au 4 décembre** : conception de l'instrument de la cible et des deux familles de mondes (mondes à puits, correspondances plantées), Fable en effort maximal ; scellement jusqu'au 7.
3. **Étape 2, 7 au 11 décembre, 0 dollar** : code et validation de l'instrument, courbe du hasard et de l'énumérateur, banc des correspondances plantées (où entre le levier 4), garde plantée du pont ; familles tenues à l'écart écrites par une instance aveugle d'Opus (nœud 4, b).
4. **Étapes 3 et 4, 9 au 19 décembre au plus tôt** : préenregistrement et devis, puis première course payante contre le meilleur modèle seul.
5. **Étape 5, texte du 9 au 12 décembre, courses du 14 au 23** : sélecteurs en rétrodiction longue — l'épreuve du pont réécrite (expériences 1 et 5 du 23), le bras C de Gu et Krenn.
6. **Étape 6, dès le 7 décembre** : registre prospectif scellé interne (nœud 5, a).
7. **Étape 5 bis, janvier** : scissions datées, macros et formes d'équations sur ensemble à risque, couche des problèmes pondérés, bras A de Gu et Krenn si les identités sont publiques.
8. **Étape 7, janvier** : opérateurs (scission, compression), cinétique en température, verrous ouverts ; cibles de preuve seulement là (nœud 6).
9. **Étapes 8 et 9** : transfert vers une épreuve réelle ; détecteurs sémantiques en prospectif, pas avant février.

## 6. Ce que le rapport du 23 avait de juste

L'interdit de juger l'organisme sur un juge-modèle (N-058) ; la priorité au processeur sans dépense ; le choix de PubTator 3 contre une base à compte ; l'audit de réemploi avant tout code d'opérateur ; la règle d'étanchéité temporelle, qui devient transversale. Ses idées survivent presque toutes ; c'est leur ordre et la manière de les classer qui tombent.

---

Fin de rédaction : 2026-11-24 (heure en pied du message de remise).
