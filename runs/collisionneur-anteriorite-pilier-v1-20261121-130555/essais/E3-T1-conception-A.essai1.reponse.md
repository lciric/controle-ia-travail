# Proposition A — Tour III.1 : quand et sur quelle étendue lire l'antériorité

## 0. État des pièces

- Les blocs FAITS et QUESTION sont présents et ne paraissent pas coupés. Je n'ai pas recalculé les empreintes sha256.
- Le bloc FAITS ne porte aucune étiquette de statut. Je cite ses éléments comme « FAITS (statut non fourni) », sans les promouvoir en VÉRIFIÉ. Ce qui vient de moi est marqué HYPOTHÈSE ou « proposition ».
- L'option (c), « pour tout le pilier », fixe une étendue mais pas un moment. Je la lis comme « lecture large de tout le pilier avant les pilotes ». C'est une interprétation, à confirmer.

## A. Ce que la question suppose sans que ce soit établi (livrable a)

| # | Présupposé | Statut |
|---|---|---|
| P1 | Les trois options sont exclusives. Or elles croisent deux axes : (b) fixe un moment, (c) une étendue, (a) les deux. | HYPOTHÈSE de la question, que je conteste |
| P2 | Les cinq zones, nommées dans le vocabulaire du programme, sont celles d'où viennent les collisions. | HYPOTHÈSE, non mesurée (duel 2) |
| P3 | « Lu et empreinté » vaut « antériorité connue ». Une empreinte atteste quels octets ont été ouverts, pas que l'énoncé pertinent a été repéré ou compris. | HYPOTHÈSE, non mesurée (duel 3) |
| P4 | « Première revendication de nouveauté » est un événement net. Or inscrire une cible dans une liste d'un pilier « mathématiques nouvelles » est déjà une revendication implicite. | HYPOTHÈSE |
| P5 | Une collision est binaire. En pratique elle est graduée : énoncé identique, cas particulier, corollaire non écrit, folklore, contre-exemple connu, travail concurrent. | HYPOTHÈSE (proposition d'échelle en §1) |
| P6 | Le gel de la veille peut être levé. Les FAITS disent qu'il résulte d'une décision du directeur. Les options (a) et (c) exigent une dérogation, qui ne relève ni de moi ni d'un agent. | FAITS (statut non fourni) pour le gel ; la levée est une décision humaine ouverte |
| P7 | Une collision coûte plus qu'une lecture. Les FAITS donnent les deux coûts en mots (« coûte cher », « coûte de l'effort et retarde »), sans chiffre. | Je ne sais pas ; le duel 1 pose le seuil |
| P8 | La nouveauté est la propriété à protéger. Pour un programme défensif, un théorème déjà connu qui répond au besoin de contrôle est un gain à coût nul : la lecture peut trouver la réponse, pas seulement la collision. | HYPOTHÈSE (la mienne) |
| P9 | Le juge de nouveauté et le lecteur humain « prévus » fonctionnent. | FAITS (statut non fourni) pour « prévus » ; aucune mesure transmise |
| P10 | Une liste de cibles candidates existe déjà. | Je ne sais pas |

## 1. Ce qu'un expert ferait, et qu'on ne demande pas

**Séparer les trois formes de cible.** La collision n'y a ni la même nature ni le même détecteur (proposition).

- *Objet à score exact.* La collision est un score déjà atteint. Le contrôle est d'abord un calcul : faire passer les procédures classiques dans le même évaluateur. La lecture sert surtout à savoir quelles procédures classiques inclure.
- *Énoncé à démontrer ou réfuter.* C'est le seul régime où la lecture d'articles est le détecteur principal, et où le vocabulaire trompe. La collision peut aussi être un contre-exemple connu, puisque la réfutation compte.
- *Lemme de bibliothèque.* La nouveauté est relative à la bibliothèque, pas aux mathématiques. Lire des articles n'y apprend presque rien. Il faut interroger la bibliothèque, ses demandes de fusion ouvertes et ses mainteneurs.

**Arrêter la lecture sur un critère de cible, pas de zone.** Un expert ne s'arrête pas quand la zone est couverte, ce qui n'arrive jamais. Il s'arrête quand il sait nommer le plus proche voisin connu de la cible et écrire l'écart en une phrase. Exemple de forme : « connu sous indépendance avec telle constante ; cible : dépendance arbitraire, même constante ». Sans voisin nommé, pas de scellement. L'écart écrit est ce qui devient réfutable.

**Sonder les cas particuliers.** On spécialise la cible (indépendance, deux tests, cas gaussien) et on cherche ce cas dans la littérature, puis on remonte les citations de type « généralisation de ». Si le cas particulier contredit une borne connue, la cible est fausse avant toute dépense.

**Parler à une personne avant de lire en masse.** Aucune recherche documentaire ne trouve le folklore, c'est-à-dire ce que les spécialistes savent sans l'avoir écrit. Une conversation courte avec un spécialiste a plus de chances de l'atteindre.

**Lire d'abord ce qui est déjà signalé.** Les travaux voisins de 2026 « croisés par hasard, sans être lus » (FAITS, statut non fourni) forment une liste finie et connue du programme. C'est la lecture la moins chère et la plus ciblée. Je n'en connais pas les titres.

**Traiter le modèle générateur comme un index contaminé.** Un résultat produit d'un jet par un modèle de langage peut être une restitution de son entraînement (HYPOTHÈSE). On peut lui demander « sous quel nom ceci est-il connu ? » : la sonde coûte peu, mais son taux de fausses alertes est inconnu, références fabriquées comprises.

**Dater.** La nouveauté est relative à une date. Entre scellement et revendication, des prépublications paraissent. Une relecture au moment de la revendication reste donc nécessaire quelle que soit l'option retenue. La question n'est pas (a) ou (b), mais « (b) suffit-elle ? ».

**Graduer et rapporter.** Je propose une échelle à six degrés : identique, cas particulier d'un résultat connu, corollaire non écrit, folklore, concurrent, neuf à date. Les FAITS disent que toutes les cibles sont rapportées. Une collision trouvée est donc un résultat à rapporter avec sa source.

## 2. Données brutes de départ

Sauf mention contraire, les listes sont ma proposition. Les références sont citées de mémoire, avec une attribution que je tiens pour correcte, à contrôler sur notice avant tout usage.

**Bases d'articles et graphe de citations**
- arXiv, sur les catégories de statistique, théorie de l'information, théorie des jeux, apprentissage, sécurité, et finance quantitative pour l'agrégation de risques.
- zbMATH Open et MathSciNet (ce dernier payant).
- OpenAlex, Semantic Scholar et Crossref pour le graphe de citations.

**Graines par zone**
- *Fusion.* Vovk et Wang (2020), « Combining p-values via averaging ». Vovk et Wang (2021), « E-values: Calibration, combination and applications ». Rüschendorf (1982), « Random variables with maximum sums », qui ouvre le vocabulaire voisin de l'agrégation de risques.
- *Séquentiel.* Ramdas, Grünwald, Vovk et Shafer (2023), « Game-theoretic statistics and safe anytime-valid inference ».
- *Frontières de détection.* Donoho et Jin (2004), « Higher criticism for detecting sparse heterogeneous mixtures ». Travaux d'Ingster : référence à vérifier.
- *Jeux d'inspection.* Avenhaus, von Stengel et Zamir (2002), « Inspection games ». Travaux appliquant ces jeux au contrôle d'IA : référence à vérifier.
- *Recherche de programmes.* Romera-Paredes et al. (2024), « Mathematical discoveries from program search with large language models ».

**Collisions naturelles passées.** Les commentaires de version et remerciements d'arXiv contiennent des formules du type « après dépôt, nous avons appris que », « indépendamment », « concurrent ». C'est la seule source que je connaisse qui dise d'où viennent réellement les collisions (elle sert au duel 2). Je ne sais pas combien de cas elle donnera.

**Bibliothèques formelles**
- Mathlib.
- La bibliothèque Lean de statistique des FAITS, dont le nom n'est pas transmis ; je ne l'invente pas.
- Leurs historiques git, demandes de fusion ouvertes et fils de discussion.
- L'Archive of Formal Proofs d'Isabelle, car une formalisation peut exister dans un autre assistant.

**Listes de problèmes ouverts.** Je connais les sessions de problèmes ouverts de conférences de théorie de l'apprentissage et les sections finales des monographies. Je ne connais pas de liste tenue à jour pour ces cinq zones. Deux réserves structurelles :
- « ouvert » sur une liste signifie « le mainteneur ne connaît pas de solution » ;
- une cible tirée d'une liste célèbre est neuve mais probablement hors de portée.

**Notices de bancs.** Je ne connais pas de table de records pour des règles de décision statistique. Si elle n'existe pas, la référence d'un « score exact » est construite par le programme. La collision se teste alors par calcul contre les procédures classiques, pas par lecture.

## 3. Méthodes, hypothèses et modes d'échec ; mesure minimale par instrument (livrable c)

Aucune méthode ne certifie une absence. « Qui ne laisse pas passer de collision » n'est pas atteignable. Ce qu'on peut livrer est un rappel mesuré sur des collisions connues, donc une borne.

| Méthode | Ce qu'elle suppose | Comment elle échoue |
|---|---|---|
| Mots-clés | Vocabulaire partagé | Synonymes entre communautés : e-valeur, martingale de test, pari ; fusion sous dépendance, agrégation de risques ; inspection, audit, patrouille |
| Graphe de citations, amont et aval des graines | La collision cite une graine | Communautés parallèles, prépublications récentes, folklore |
| Plongements sémantiques sur résumés | Le résultat figure dans le résumé | Lemme en annexe ; deux énoncés qui diffèrent d'un quantificateur sont voisins |
| Agent lecteur en texte intégral, avec empreintes | Lecture fidèle des hypothèses | « Rien trouvé » à tort, référence fabriquée, confusion d'hypothèses ; l'empreinte ne couvre que les octets |
| Mémoire du modèle | Couverture par l'entraînement | Fabrication assurée |
| Sonde par cas particuliers | Le cas particulier est publié | Cible sans cas particulier parlant |
| Recherche formelle d'énoncés (recherche de preuve automatique, par motif de type, sémantique) | Énoncé formalisé sous une forme proche | Définitions équivalentes non dépliées, niveau de généralité, autre assistant |
| Expert humain | Disponibilité, bonne spécialité | Spécialité étroite, coût, divulgation des cibles |

La recherche formelle est asymétrique. Une présence dans la bibliothèque est une certitude mécanique. Une absence ne dit presque rien sur la nouveauté mathématique, car la bibliothèque ne couvre qu'une part du vocabulaire (FAITS, statut non fourni).

**Banc de mesure commun (proposition) : retenue temporelle.** On fixe une date T, postérieure à la coupure d'entraînement du modèle et à l'instantané du corpus.
- *Positifs* : résultats publiés avant T, reformulés (notation, vocabulaire du contrôle, ordre des hypothèses).
- *Cas honnêtes appariés* : résultats de même zone et de même forme publiés après T, donc neufs à la date T.
- *Limite* : un résultat postérieur à T peut être une redécouverte non signalée. Toute alerte sur un cas honnête est donc arbitrée par un humain avant d'être comptée comme fausse.

| Instrument nommé | Détection | Fausses alertes | Vérification mécanique à battre |
|---|---|---|---|
| Agent lecteur avec empreintes, option (a) | Part des positifs reformulés signalés avec la bonne source | Part des cas post-T signalés à tort, après arbitrage | Mots-clés plus un saut de citation depuis les graines, à taux de fausses alertes égal |
| Relecteur du domaine | Mêmes positifs, à l'aveugle, temps borné | Mêmes cas post-T | L'agent seul. À coût supérieur, il doit attraper ce que l'agent manque (folklore, hors zone) |
| Mainteneurs de bibliothèque | Doublons plantés (lemmes existants reformulés) reconnus | Lemmes ajoutés après le commit T déclarés présents à tort | Recherche formelle seule sur le commit T |
| Recherche formelle d'énoncés | Doublons plantés retrouvés au commit T | Lemmes post-T déclarés présents | Recherche textuelle dans le dépôt |
| Juge de nouveauté (prévu, FAITS) | Même banc que l'agent | Idem | Idem ; non mesuré, son verdict reste OBSERVÉ-NON-AUDITÉ, pas une preuve |

Avec 30 positifs (effectif illustratif), l'intervalle à 95 % sur un rappel proche de 50 % est d'environ ±18 points. Le banc distingue donc « utile » de « inutile », pas 80 % de 90 %.

## 4. Ce qui, hors du programme, vérifierait qu'une cible est neuve

- **Auteurs du plus proche voisin.** On leur demande : « votre théorème implique-t-il ceci ? ». C'est la vérification la plus informative par unité d'effort (HYPOTHÈSE), parce qu'ils connaissent les corollaires non écrits. Elle divulgue la cible. Je ne sais pas ce que le programme accepte de divulguer.
- **Relecteur du domaine.** Seul instrument qui atteint le folklore. Son rappel se mesure sur le banc ci-dessus avant de s'y fier.
- **Mainteneurs.** Ils font autorité sur « absent de la bibliothèque et pas en cours », mais pas sur la nouveauté mathématique.
- **Recherche formelle.** Elle certifie une présence, jamais une absence.
- **Prépublication avec délai d'attente, puis relecture par les pairs.** Lent, et les pairs laissent passer des redécouvertes.

Aucun de ces contrôles ne conclut « neuf ». Chacun abaisse une borne. Une revendication honnête s'écrit donc ainsi : « non trouvé au [date], par [méthodes], rappel mesuré [x] sur collisions plantées ».

## 5. Reformulation de la demande

La demande telle que posée est « quand lire, et combien ». Je propose à la place :

« Pour chaque forme de cible et chaque porte (scellement, dépense, revendication), quelle preuve minimale de non-collision exige-t-on, produite par quel instrument au rappel mesuré, pour que le coût attendu d'une collision passée reste inférieur au coût de la preuve ? Et qui autorise, sur quel périmètre, la dérogation au gel de la veille ? »

## 6. Recommandation : une option (d), lecture par cible à trois portes, calibrée par collisions plantées

Ni (a), ni (b) seule, ni (c).

**Contre (c).** Le pilier n'a pas de bord, donc « tout lire » n'a pas de critère d'arrêt. Cette option paie d'avance le retard des pilotes que les FAITS nomment, sans borne sur ce qu'elle manque.

**Contre (b) seule.** Elle accepte par construction la collision « après une dépense », que les FAITS disent coûteuse. Elle scelle aussi des énoncés sans voisin nommé, donc sans écart réfutable.

**Contre (a) telle quelle.** Elle délimite par zones alors que les collisions suivent les cibles (P2). Elle confond empreinte et lecture (P3). Elle applique la même lecture aux trois formes, alors que deux relèvent surtout de contrôles mécaniques. Elle ne dispense pas de (b).

**Contenu de (d)**

- **Porte 0, maintenant.** Borné, sous dérogation du directeur.
  - Lire les travaux de 2026 déjà croisés.
  - Lire une graine par zone.
  - Construire le banc à retenue temporelle.
  - Lancer les duels 1 et 4, les moins chers.
- **Porte 1, scellement.** Une fiche de collision par cible.
  - *Énoncé* : plus proche voisin nommé, écart en une phrase, cas particuliers sondés, synonymes dans au moins trois vocabulaires.
  - *Objet* : procédures classiques passées dans l'évaluateur.
  - *Lemme* : recherche formelle, plus demandes de fusion ouvertes.
  - Temps borné par fiche. Pas de fiche, pas de scellement. Les fiches sont rapportées avec la liste.
- **Porte 2, revendication.** C'est (b), conservée.
  - Relancer la recherche sur l'intervalle écoulé depuis le scellement.
  - Faire relire par un relecteur externe.
  - Écrire aux auteurs du voisin si la divulgation est permise.
  - Formuler la revendication avec date, méthodes et rappel mesuré.

**Ce que cela coûte.** Je ne sais pas le chiffrer. La structure du coût :
- un coût fixe : le banc et la lecture bornée de la porte 0 ;
- un coût par cible : la fiche ;
- un coût par revendication : le relecteur externe.

Le retard des pilotes est borné par la porte 0. Il n'est pas nul.

**Ce que cela suppose**
- Une liste de candidates existe ou peut être esquissée (P10).
- Le directeur accorde la dérogation (P6).
- La recherche par cible rappelle au moins autant que la lecture par zone (duel 2).
- Un spécialiste est disponible.

**Ce qui ferait changer la recommandation**
- *Duel 1, taux de collision sous le seuil de rentabilité* : (b) seule pour les objets et les lemmes, fiche maintenue pour les seuls énoncés.
- *Duel 2, sources majoritairement dans les zones* : la variante zonée de (a) devient défendable en étendue.
- *Duel 2, sources majoritairement concurrentes plutôt qu'antérieures* : aucune lecture préalable ne les évite, et l'effort se déplace vers la porte 2.
- *Duel 3, l'agent ne bat pas la recherche mécanique* : pas d'agent lecteur ; mécanique plus humain.
- *Duel 4, la recherche formelle suffit* : les lemmes sortent entièrement du périmètre de lecture.

## B. Expériences décisives (livrable b)

Tous les seuils sont illustratifs et à fixer par l'arbitre avant exécution.

**Duel 1. Quand : le taux de base justifie-t-il de lire avant de sceller ?**
- **H_A** : parmi des candidates rédigées sans lecture, le taux de collision p est au moins p*. **H_B** : p est inférieur à p*.
- **Seuil** : p* = coût d'une fiche ÷ coût d'une collision découverte après dépense (ma proposition). Je ne connais aucun des deux termes ; l'arbitre doit les poser.
- **Protocole** : n candidates tirées au hasard, examinées à l'aveugle par un spécialiste externe en temps borné.
- **Métrique** : intervalle de confiance exact sur p.
- **Contrôle négatif** : cas post-T mêlés au lot, qui doivent sortir « non trouvé ». S'y ajoutent des positifs plantés, pour vérifier que l'examinateur détecte ; sinon p est sous-estimé.
- **Issues** :
  - borne haute de l'intervalle sous p* : H_A falsifiée, la lecture avant scellement coûte plus qu'elle n'évite ;
  - borne basse au-dessus de p* : H_B falsifiée, (b) seule n'est pas tenable ;
  - intervalle à cheval sur p* : non conclusif, à dire tel quel.
- **Ordre de grandeur** : avec n = 20 (illustratif) et zéro collision, la borne haute unilatérale à 95 % vaut environ 14 %.

**Duel 2. Étendue : les collisions viennent-elles des cinq zones ?**
- **H_A** : au moins 80 % (illustratif) des sources de collisions naturelles passées (§2) tombent dans les cinq zones telles que nommées. **H_B** : moins.
- **Métrique** : part de sources en zone, codée par deux annotateurs. Métrique secondaire : part de collisions concurrentes plutôt qu'antérieures.
- **Contrôle négatif** : le taux « en zone » des citations ordinaires des mêmes articles. Si les sources de collision ne sont pas plus hors zone que les citations ordinaires, le découpage n'est pas en cause.
- **Issues** :
  - H_A falsifiée : l'option (a) zonée laisse passer par construction ; il faut la recherche par cible ou l'humain ;
  - H_B falsifiée : (c) est inutile en étendue, et ma critique P2 tombe.
- **Risque** : rendement de la fouille inconnu. Trop peu de cas donne un résultat non conclusif.

**Duel 3. Instrument : l'agent lecteur ajoute-t-il quelque chose ?**
- **H_A** : sur le banc à retenue temporelle, à taux de fausses alertes égal, le rappel de l'agent dépasse d'au moins 15 points (illustratif) celui de « mots-clés plus un saut de citation ». **H_B** : non.
- **Contrôle négatif** : cas post-T, alertes arbitrées par un humain.
- **Issues** :
  - H_A falsifiée : « articles lus et empreintés par un agent » ne vaut pas son coût ; l'empreinte reste utile comme trace, pas comme preuve ;
  - H_B falsifiée : une porte purement mécanique est insuffisante pour les énoncés.

**Duel 4. Lemmes : la recherche formelle suffit-elle ?**
- **H_A** : au commit T de la bibliothèque, la recherche formelle retrouve au moins 90 % (illustratif) des doublons plantés. Ce sont des lemmes existants reformulés : ordre des lieurs, noms, niveau de généralité. **H_B** : moins.
- **Contrôle négatif** : lemmes ajoutés après T, testés contre T. Ils doivent sortir « absent » ; ceux qui sortent « présent » sont arbitrés, car ils peuvent être de vrais doublons fusionnés par erreur.
- **Issues** :
  - H_A falsifiée : mainteneurs requis dans la boucle pour la forme « lemme » ;
  - H_B falsifiée : aucune lecture d'articles ni agent pour les lemmes.
- **Avantage** : la vérité terrain vient de l'historique git, sans jugement humain sur les positifs.

## D. Ancrage matériel (livrable d)

- **Modèles.** Un modèle à poids ouverts capable d'appeler des outils, pour l'agent lecteur. Un modèle de plongement ouvert, pour la ligne de base sémantique. Contrainte ferme : coupure d'entraînement antérieure à T, faute de quoi le banc est contaminé. Je ne nomme pas de modèle précis : je ne sais pas lesquels satisfont cette contrainte à la date du programme.
- **Données.** Métadonnées arXiv, OpenAlex et zbMATH Open, en accès ouvert. Dépôts git des bibliothèques Lean. MathSciNet est payant et facultatif.
- **Calcul.** La recherche d'antériorité est limitée par les entrées-sorties et le temps humain, pas par les processeurs graphiques.
  - Duels 2 et 3 : une machine ordinaire, plus l'inférence du modèle sur quelques dizaines de cas.
  - Duel 4 : compilation de la bibliothèque à un commit donné, sur une machine ordinaire.
- **Coût** (illustratif en totalité). Le poste dominant est humain :
  - de l'ordre d'un à deux jours de spécialiste pour le duel 1 ;
  - quelques jours d'ingénierie pour le banc ;
  - arbitrage des alertes.
  
  Le coût en calcul est faible devant ces postes. Je n'ai aucun chiffre des FAITS pour l'étayer.
- **Hors de portée de ce plan.** Le folklore non écrit, les travaux concurrents non encore déposés, et toute garantie d'absence.

FIN-DE-CELLULE