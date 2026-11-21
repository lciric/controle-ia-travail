> You are powered by the model named Fable 5.2.

# Un troisième billet à partir des conceptions du 21 novembre : oui ; trois candidats, un recommandé, son plan — propositions du concepteur (v1)

- **Date** : 21 novembre 2026, de 18:10 à 18:41 UTC (`date -u`). **Auteur** : Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), agent neuf lancé par l'orchestration de la session mère ; la phrase en tête est celle de mon invite système qui nomme mon modèle. Pièce de travail (classe C), **non contre-lue**. Aucun appel payant, aucune machine, **aucune recherche en ligne**, ni commit ni poussée. Dépôt à `f64d95ac9` au relevé des empreintes (18:22 UTC), `2b04bc736` à la fin : la branche a avancé pendant mon travail, par d'autres mains.
- **Ta question**, mot pour mot : « à partir des conceptions d'aujourd'hui peut-on imaginer concevoir un 3e billet ? ». Traitée par ta « demande approfondie ».
- **Lu au dépôt**, empreintes égales aux compagnons (annexe) : le gabarit des billets v2 ; l'état des deux billets ; la note d'entretien v4 et ses errata 1 et 2, en entier ; la décision sur le retrait de la marge asymétrique (N-077), en entier ; la décision sur l'assurance par l'audit et la référence honnête (N-076), § 1, 2 et 11, et ses errata 1 et 2 ; la décision sur le plancher et les deux regards (N-075), version 3, § 2 et 7, et son erratum 3 v2, § 4 ; **les douze conceptions du jour dans leur v2** : le verdict de chacune, et les sections dites en annexe ; la lecture du collisionneur sur l'adjudant, en entier ; le verdict de chacune des douze vérifications de corrections ; de la note « percée » du matin, le seul § 7.1 ; le résumé de la politique du site ; la consigne commune de méthode ; cinq lignes du registre des accords, par leur identifiant.
- **Relu par moi sur pièce empreintée, à la page** : seize PDF et une copie de page web (annexe). Toute citation et tout chiffre de l'état de l'art marqués [lu] en viennent.
- **Mes calculs** : `calculs-troisieme-billet-v1.py` (`f36f3990574bead1fcf2d65c632834c23f83d85ea839bbc1b952031434ce2c96`) et sa sortie `calculs-troisieme-billet-v1.txt` (`6841f5efc2cb3f3a98831eebb9c3e22ee363fc432a4d3372201c53693dbdc989`), même dossier, scellés ; lois normales exactes et tirages à graines écrites (R9) ; rejoués deux fois, sorties identiques à l'octet ; **non contre-lus**. Aucune donnée du programme n'y entre : toutes les entrées sont des suppositions d'illustration.
- **Non ouvert** : les brouillons des deux billets et leurs fiches de faits ; tout résultat, verdict ou score ; `registres/decisions.md`, `registres/etat.md` ; tout dossier ou branche cloisonnés ; l'annexe réservée de la note du protocole X sur le dommage, et la famille de menaces qu'elle garde, que je ne nomme pas ici ; le § 7.2 (côté menace) de la note « percée ».
- **Marques** : [lu] = relu par moi ce jour sur pièce empreintée, à la page dite (rang dans le fichier) ; [repris] = dit par une note du dépôt avec sa page, non rouvert par moi ; [calcul, X] = bloc X de ma sortie ; [calcul de la note …] = bloc d'une sortie scellée du dépôt, non rejoué par moi ; [jugement] = estimation de ma part ; [non vérifié] = ni pièce ni page, aucun chiffre n'en est tiré. « Non trouvé » veut dire « non trouvé dans les pièces lues », jamais « libre » (règle contre les faux trous, R8).

## Verdict

**En trois lignes.** Oui. Trois billets tiennent sans aucun résultat du programme, sans course et sans pièce cloisonnée : (A) la référence honnête, (B) « tirer au sort n'est pas reconnaître », (C) l'hypothèse retirée avant d'être mesurée. Je recommande **A**, confiance 0,65 : il tient en une formule, une figure et un script, il répond par un nombre à la phrase que le papier de l'entretien cite contre la surveillance, et son calcul est fait et rejoué. Prêt pour ta plume en trois jours si rien ne le tue ; en ligne avant le 1er décembre : un peu moins d'une chance sur deux [jugement].

1. **Ce qui peut tuer A** : l'antériorité. Rien n'y est neuf en mathématiques, et son voisin le plus proche est cosigné par un auteur du papier de l'entretien (Wen et al., p. 6 [lu]). Il se présente comme un pont chiffré, jamais comme un résultat ; une recherche sur le forum et parmi les travaux citants passe avant toute écriture.
2. **Ce qui le bloque aujourd'hui** : les billets hors du chantier de l'entretien sont gelés (consignes permanentes, « Allègement de la procédure » ; GO-2026-11-19-28). L'ouvrir est ton mot.
3. **Fait en plus de la demande** : un prototype du calcul et de son contrôle par tirages (§ 2.1), pour que « ce qui manque » soit mesuré et non estimé.
4. **À signaler** : une précision pour l'entretien, hors de ta question : le « 98,8 % » de la note d'entretien v4 est une aire sous la courbe, non un taux de détection (relevé de méthode, trouvaille 5). Dans mon propre tirage, une case est sortie à 3,5 erreurs types ; je l'ai auditée, c'est un écart de tirage (§ 2.1, règle de symétrie R4).
5. **Décisions pour toi** : quatre, toutes des nœuds (§ 7).

---

## 1. Tes quatre points, et la reformulation

**(1) Ce qu'un expert ferait ici, et que tu ne demandes pas.** L'expert est quelqu'un qui publie sur le forum où iront les billets et qui a siégé dans un jury de bourse.
- **Il demanderait d'abord à quoi sert le billet.** Devant un jury, un billet prouve trois choses : que tu sais finir un travail petit et juste, que tu connais les textes de ceux qui t'écoutent, que tu sais concéder. Il choisirait donc le sujet le plus proche du papier de l'entretien, et une thèse qui concède quelque chose de précis plutôt qu'une thèse qui défend le programme.
- **Il fixerait l'unité** : une thèse, une figure, un script, environ 1 300 mots. Pas un panorama.
- **Il tuerait chaque candidat avant d'écrire** : recherche sur le forum, billets et commentaires, et parmi les travaux qui citent les trois textes les plus proches ; la phrase qui ferait abandonner est écrite d'avance.
- **Il préférerait un billet où l'erreur coûte peu.** Un calcul sous suppositions écrites se réfute en le rejouant ; une phrase de nouveauté ne se réfute que par un lecteur fâché.
- **Il ne ferait dépendre le billet d'aucun résultat à venir** : c'est ce qui bloque le billet sur les sondes.
- **Il vérifierait ce que le billet laisse voir** : rien des modes de sabotage, de la famille tenue à l'écart, des procédés en quarantaine. Un billet sur la statistique du défenseur ne montre rien de tel.
- **Il lirait la politique du site avant de choisir la forme.** Pour un compte neuf, la règle est presque « aucun texte de modèle » ; mais le code n'est pas compté, ni « les faits ou arguments trouvés avec un modèle mais rédigés par l'humain », et une traduction mot à mot d'un texte écrit dans ta langue est permise (résumé de la politique, points 2, 6 et 8). **Un billet fait d'un calcul, d'une table et d'une figure, avec peu de prose, est la forme qui pèse le moins sur ta plume.**
- **Il accorderait le billet à ce que tu diras le 1er décembre** (note d'entretien v4 et ses errata), et à la copie publique du dépôt.
- **Il prévoirait un repli** : si la modération tarde, un texte fini et un script public que tu montres à l'entretien. Les montrer est aussi un geste de publication : ton mot.

**(2) Les données brutes de départ.** Pas les verdicts des douze notes, déjà analysés, mais :
- les textes premiers dont dépend « neuf ou pas neuf » : le billet théorique de Hebbar ; Wen et al., p. 6 ; le papier de l'entretien, p. 2 et 10 ; Singh, p. 9 ; Taylor et al., p. 18 ; Gan et al., p. 1, 8, 10, 37 ; le glossaire des garanties nucléaires, p. 113-114 ; « Blindfold », p. 12 ; Lucassen et Kaufman, p. 2 et 10 ; Kutasov et al., p. 5 ; « Ctrl-Z », p. 5 à 9. Tous relus aujourd'hui [lu] ;
- les scripts de calcul et leurs sorties, rejoués, et non les phrases qui les citent ;
- le forum lui-même pour l'antériorité, billets et commentaires : **non lu**, aucune recherche faite ;
- pour un exemple qui ne soit pas un jouet : des scores de moniteur par acte, sur des épisodes honnêtes d'un jeu public, pour mesurer de combien deux sources honnêtes diffèrent entre elles. Licences non vérifiées ; après le billet.

**(3) Les méthodes et les outils.** La formule fermée du test à deux échantillons ; des tirages à graines écrites pour la contrôler ; un test de rangs pour montrer qu'elle ne tient pas à la loi normale ; un monde à scores dépendants et un monde à référence décalée ; une figure à échelles logarithmiques ; un programme qui recalcule chaque nombre du texte depuis les sorties, comme celui de l'autre billet ; un registre des affirmations (R6) ; chaque chiffre de travaux voisins relu sur PDF empreinté, à la page (règle de provenance, R7) ; une lecture adverse par un autre modèle ; le collisionneur sur une question neutre, pour l'antériorité et les contre-arguments, jamais pour la vérité.

**(4) Ce qui vérifierait hors de toi et de moi.**
1. Le rejeu par n'importe qui : script public, graines écrites.
2. Une dérivation par un agent qui ne reçoit que l'énoncé. C'est encore un modèle.
3. Un statisticien du séquentiel, ou un chercheur du contrôle, avant la mise en ligne. Contact externe : nœud ; je rédige, tu envoies.
4. Les commentaires du forum. Les deux objections les plus fréquentes de l'étude des billets sont l'explication concurrente et l'antériorité (gabarit, § 1.4) : le plan les prévient.
5. Le jury, le 1er décembre.

**Ta demande, reformulée.**

> Parmi les idées écrites aujourd'hui, laquelle peut devenir en une semaine un billet court et vérifiable par un tiers (une thèse, une figure, un script), qui (1) ne s'appuie sur aucun résultat du programme, aucune course payante, aucune pièce cloisonnée ; (2) parle la langue des auteurs du papier de l'entretien et leur concède quelque chose de précis ; (3) survit à une recherche d'antériorité, ou la cite d'elle-même ; (4) ne peut pas être démenti de façon gênante par nos résultats à venir ; (5) ne dit rien que tu ne dirais pas le 1er décembre ? Ranger les candidats selon ces cinq critères, dire ce qui manque à chacun, en recommander un et en donner le plan selon le gabarit.

---

## 2. Les trois candidats

### 2.0 Vue d'ensemble

| | **A. La référence honnête** | **B. Tirer au sort n'est pas reconnaître** | **C. L'hypothèse retirée avant d'être mesurée** |
|---|---|---|---|
| Genre | une loi et ses nombres | une méthode empruntée à un autre métier | un retrait, et la règle de lecture qui en sort |
| Source du jour | décision sur la référence honnête (N-076), point 1 ; note du protocole X sur le contrôle diffus, verdict 3 | notes sur la couverture de l'oracle et sur les dommages plantés par un tiers ; décision sur le plancher (N-075), erratum 3 v2, § 4.1 | note du protocole X sur la marge asymétrique ; décision sur son retrait (N-077) |
| Ce qui manque | recherche d'antériorité ; script public et figure ; ta plume | lecture en entier de huit voisins ; relecture de cloisonnement ; ta plume | lecture en entier de six voisins ; relecture de cloisonnement ; ta plume |
| Expérience à faire | des tirages sur processeur, moins de deux minutes : prototype fait ici | aucune ; des lois exactes déjà calculées | aucune ; des lois exactes déjà calculées |
| Durée jusqu'à ta plume [jugement] | 3 jours | 5 à 6 jours | 3 à 4 jours |
| En ligne avant le 1er décembre [jugement] | 0,45 | 0,2 | 0,3 |
| Idée volée | faible | faible à moyen | faible |
| Faux trou du champ (R8) | moyen | moyen à élevé | faible |
| Contradiction avec un résultat à venir | faible à moyen | faible | moyen |
| Risque de cloisonnement | faible (la sortie par le jumeau, § 7, D-2) | moyen | moyen |
| Intérêt pour la bourse | fort | fort, ton délicat | moyen |

Les durées sont mes estimations, pas des devis. Les cinq critères de la reformulation, appliqués d'abord à deux objets de contrôle : ils rejettent le billet sur les sondes (critère 1 : il attend un résultat) et le billet « Reasons or watching? » (critère 2 : il ne porte pas sur le papier de l'entretien). Ils ne retiennent donc pas tout.

### 2.1 A — La référence honnête : « à quel point faut-il connaître l'honnête ? »

**Thèse en une phrase.** Accumuler beaucoup de petits indices contre un saboteur diffus n'incrimine que si la conduite de l'honnête est connue à mieux que le produit de la part d'actes sabotés par l'écart que le moniteur lit ; avec une référence honnête de m actes, la part d'actes sabotés qui reste cachée cesse de baisser dès que le nombre d'actes surveillés dépasse m, aussi longtemps qu'on surveille.

**Pourquoi ce sujet.** Le papier de l'entretien écarte la surveillance en une phrase : « monitoring and incrimination seem theoretically [Hebbar, 2025] and empirically […] less promising for mitigating diffuse threats » (version 3, p. 2 [lu]). Sa source théorique dit qu'un grand volume d'actes légèrement suspects n'incriminerait que « if we knew exactly how suspicious a benign model would look. But without that affordance, no amount of mildly suspicious actions is enough » (copie empreintée du billet [lu]). Le billet A dit combien vaut ce « exactly ». C'est déjà la phrase 2 et l'objection 2 de ta note d'entretien : l'écrire, c'est aussi préparer l'entretien.

**Les nombres, sous supposition** (un score par acte, honnête de loi normale, saboté décalé de μ écarts types, actes indépendants, test de niveau 1 %, puissance un demi) :
- *Le plancher.* La part cachée vaut z × √(1/n + 1/m) / μ. Avec m = 400 et μ = 0,5 : 27,5 % à mille actes surveillés, 23,7 % à dix mille, 23,3 % à cent mille et à un million. Avec une référence exacte : 14,7 %, 4,65 %, 1,47 %, 0,47 %. Au-delà de n = m, allonger la surveillance ne gagne plus que 29 % au mieux [calcul, A]. Mes valeurs sont celles du bloc A de la note « percée », retrouvées par un code réécrit ; j'avais lu la fonction d'origine : c'est un rejeu, non une dérivation indépendante.
- *Ce que vaut « exactly ».* La tolérance est la part sabotée fois μ. Pour un moniteur dont l'aire sous la courbe vaudrait 0,77, la meilleure valeur imprimée pour les auditeurs de Gan et al. (p. 1 [lu] ; leur unité est le dépôt de code, non l'acte : repère seulement), et 2 % d'actes sabotés : il faut connaître la moyenne honnête à 0,021 écart type près, soit au moins 12 393 actes honnêtes de référence, quelle que soit la durée de la surveillance ; 1 250 pour une aire de 0,99 ; 105 397 pour une aire de 0,60 ; 1,85 fois plus pour une puissance de 0,8 [calcul, B].
- *Un décalage ne se moyenne pas.* Une référence décalée de 0,05 écart type donne 23 % de fausses alertes à mille actes et 99,6 % à dix mille ; décalée de 0,01 : 9 % à dix mille, 80 % à cent mille [calcul, C]. Les deux premières valeurs sont celles de la note du protocole X sur le contrôle diffus.
- *Deux sorties, et leur prix.* Des témoins honnêtes vérifiés, entrelacés à taux p : la loi en racine revient, multipliée par √(1 + 1/p), soit 10 à 1 % de témoins [calcul, D]. Un nul refait à chaque acte, par le rang de l'acte parmi quelques tirages d'un jumeau de confiance : la loi en racine nue, 7,5 fois moins d'actes cachés qu'avec 1 % de témoins, au prix de quatre tirages par acte [calcul de la note « percée », bloc C]. Le jumeau n'existe qu'au banc.
- *Ce n'est pas un artefact de la loi normale.* Avec un test de rangs et une loi honnête à queues lourdes, 10 % d'actes sabotés : la détection passe de 0,10 à 0,17 puis 0,19 quand la surveillance est multipliée par dix puis par cent, la référence restant à 400 ; de 0,10 à 0,84 puis 1,00 quand la référence suit [calcul, E2]. La lecture attendue était écrite dans le script avant le tirage.
- *Contrôles.* Référence exacte : aucun plancher, la part cachée est divisée par dix quand la surveillance est multipliée par cent (0,1000) ; référence fixe : le même rapport vaut 0,98 [calcul, A]. Par tirages, à l'endroit où la formule annonce une puissance d'un demi : fausse alerte 0,0107, détection 0,5018 [calcul, E1]. Une case du test de rangs est sortie à 0,0155 de fausse alerte, 3,5 erreurs types au-dessus de 0,01 ; refaite avec dix fois plus de répétitions et trois graines neuves : 0,0098, 0,0103, 0,0095. Le test est bien réglé, la case est gardée telle quelle [calcul, E3 ; bloc ajouté après lecture de E2, dit dans le script].

**Ce qui n'est pas neuf.**
- La formule : c'est la variance d'un test à deux échantillons. De la statistique de première année.
- La loi en racine de la dissimulation : Ker (2006, 2007) ; Bash, Goeckel et Towsley [repris de N-076, non rouverts par moi].
- Son revers : elle suppose que le guetteur « has an accurate statistical characterization of the channel » ; s'il en est incertain et que son récepteur se limite à un test de seuil sur la puissance reçue, une puissance qui ne décroît pas passe inaperçue (Sobers et al., arXiv 1608.00698 v3, p. 1 [lu]) ; He et al. (arXiv 1612.09027 v1, p. 1 [lu, résumé]). Le « mur de rapport signal sur bruit » de la détection de spectre dit la même chose, je crois [non vérifié].
- L'ensemble aveugle d'un moniteur tolérant : « no betting scheme recovers what the tolerance obligation removes » (« The Price of Self-Calibration », arXiv 2609.23254 v1, p. 6 [lu]).
- La marge de la référence qui reste une exposition linéaire : « Registration slack (p0 − pclean)H and events preceding revocation remain sources of exposure » (Singh, arXiv 2610.18948 v1, p. 9 [lu]).
- Une référence de taille fixe tenue à part pour le risque d'origine : Podkopaev et Ramdas (arXiv 2110.06177 v4, p. 4-5 [repris]).
- **Le voisin le plus proche, dans le contrôle même** : Wen, Hebbar et al. donnent à l'équipe bleue une distribution de référence et écrivent : « these estimates are approximate due to finite sample size. As such, errors can accumulate over long time sequences to produce overconfident credences. We mitigate this by bootstrapping » ; en pratique la référence serait « a moderate number of harmless outputs » vérifiés à la main (arXiv 2411.17693 v1, p. 6 [lu]). Le phénomène est donc nommé, sans formule ni horizon, par un auteur du papier de l'entretien.
- Un cas observé : au jeu d'audit sur le sous-rendement, une référence de calibration trop étroite a fait soupçonner un modèle bénin, et « the effect disappears when using the larger and more diverse Alpaca chat distribution as a baseline » (Taylor et al., p. 18 [lu]).

**Ce qui serait neuf, sous réserve de la recherche.** Les nombres mis sur la condition, pour des moniteurs de qualité réaliste ; la règle d'horizon écrite comme une règle de compte rendu (« toute accumulation déclare la taille de sa référence, son horizon et ce qui garantit ses fausses alertes ») ; les trois sources de validité mises côte à côte avec leur prix. Non trouvé par les dix requêtes de la note « percée » [repris] ; **je n'ai fait aucune recherche**. Son auteur donnait 0,55 à « pont non déjà publié » : je garde ce chiffre, la page 6 de Wen et al. ne le fait pas monter [jugement].

**Ce qui manque.** Détail au § 6. En bref : la recherche d'antériorité ; un script public, sans chemin interne, avec le monde à scores dépendants et la figure ; la contre-lecture de la borne « pour tout test » (7,7 % à m = 400, dérivation à la main non contre-lue [calcul de la note « percée », bloc A bis]), ou son retrait ; l'inventaire, par étiquettes, des tailles de référence et des horizons de nos textes scellés ; ta plume.

**Risques.**
- *Idée volée : faible.* Rien à voler dans une formule de manuel ; publier est ce qui date le pont. La seule pièce sensible est la sortie par le jumeau, qui touche le pari apparié du programme : le billet n'en dit que le principe, ou rien (décision D-2).
- *Faux trou du champ : moyen.* La zone est « séduisante, à voisins de deux mois » (N-076, § 2). Le billet ne dit jamais « personne n'a chiffré » : il dit « nous n'avons pas trouvé, par telles requêtes ». La liste « Ne pas écrire » de N-076 (§ 11) s'applique : jamais « un résultat du programme », jamais un chiffre sans « sous supposition ».
- *Contradiction avec un résultat à venir : faible à moyen.* Le billet n'annonce rien sur nos organismes. Deux endroits à tenir : la mesure de la prévision (N-076, § 2) peut montrer que l'écart entre l'honnête et son jumeau cache déjà plus que le dommage, « la loi est alors juste et ne sert à rien » ; le billet doit le dire lui-même. Et nous publions une règle : il faut savoir, avant, si nos propres textes scellés la suivent.
- *Devant le jury.* Le risque est qu'il soit jugé élémentaire. Parade : court, un nombre dont ils peuvent se servir, le crédit rendu à leur page 6.

**Intérêt pour la bourse : fort.** Il prend la phrase qui fonde leur jugement, la concède et la chiffre ; il montre ce que tu fais d'une objection ; il laisse une pièce publique, rejouable, accordée à ta phrase 2. Je n'ai lu ni l'appel de la bourse ni la composition du jury : c'est mon premier pas non justifié (relevé de méthode).

### 2.2 B — « Tirer au sort n'est pas reconnaître »

**Thèse en une phrase.** Une garantie par audit tiré au hasard multiplie deux probabilités : celle de tirer l'épisode endommagé, que le défenseur fixe, et celle que l'oracle reconnaisse le dommage qu'il regarde, que personne ne mesure ; les garanties nucléaires les séparent depuis longtemps, et la seconde ne se connaît que par des dommages plantés par un tiers, comptés au pire des strates.

**Pourquoi ce sujet.** C'est l'objection 5 de ta note d'entretien, et la limite que les auteurs écrivent de leur propre vérité approchée : « Our ground truth proxy score was not validated quantitatively against human judges » (p. 10 [lu]). Ta décision sur le plancher porte déjà la règle : « Une strate non mesurée compte pour zéro » (N-075, erratum 3 v2, § 4.1).

**Les nombres, sous supposition** [calculs de la note sur la couverture de l'oracle, blocs A, B, E, G ; sorties non rejouées par moi, l'arithmétique de ces quatre lignes refaite à la main] :
- à 1 % d'audit, un saboteur est pris avec probabilité 0,95 au plus tard à son 299ᵉ épisode endommagé si l'oracle reconnaît toujours le dommage, au 1 497ᵉ s'il le reconnaît une fois sur cinq, au 5 990ᵉ une fois sur vingt, jamais s'il ne le voit pas ;
- zéro manque sur 59 dommages plantés d'une strate borne le taux de manque à 0,05, à 95 % ; écrire « au moins neuf sur dix dans chacune de dix strates », à 95 % simultanément, demande 510 plants tous retrouvés ;
- l'accord entre deux oracles annonce 2 % d'angle mort commun là où il vaut 41 %, quand la moitié des dommages est dure pour les deux ;
- un plan de tirage réglé pour 10 % de non-détection en laisse 32 % si l'identification vaut un demi.

**Ce qui n'est pas neuf.**
- Les deux probabilités et leur nom : « Detection probability combines selection probabilities and identification probabilities » ; la probabilité atteinte « is not necessarily as large as (1 – β), because it also depends on the identification probabilities » (glossaire des garanties de l'Agence internationale de l'énergie atomique, entrées 9.30 et 9.32, p. 113-114 [lu]).
- L'ajout dosé et le taux de récupération du chimiste ; l'imprévisibilité des procédures de l'auditeur ; le test par mutation [repris de la note sur la couverture, pages dites là].
- Des juges éprouvés sur des erreurs plantées (Doddapaneni et al. ; Fox et al. ; Zubeldia et al. [repris, p. 1]) ; des auditeurs éprouvés sur des sabotages de recherche plantés : meilleure aire sous la courbe 0,77, 0,68 pour des personnes après deux heures (Gan et al., p. 1 et 8 [lu]). **La mesure de l'identification d'un auditeur existe donc déjà.**
- Le terme manquant, nommé par les auteurs du plancher eux-mêmes : « missed labels would enter as a second additive term » ; « A violation concealed even from the auditor has no label and needs a prevention argument » (« Blindfold », p. 12 [lu] ; deux phrases distinctes de la page).

**Ce qui serait neuf, sous réserve.** L'import du nom et de la comptabilité : l'identification écrite dans chaque garantie d'audit, minimum sur les strates mesurées, zéro ailleurs ; la forme de la campagne (un tiers, une grille que l'oracle n'a pas inspirée, les deux sens, des plants vérifiés). Non trouvé par les 23 requêtes de la note sur la couverture [repris] ; huit voisins restent à lire en entier avant toute phrase (sa décision D-6). La note sur les dommages plantés conclut elle-même : « rien à revendiquer ».

**Ce qui manque.** La lecture en entier des huit voisins, « Blindfold » compris ; une relecture de cloisonnement, parce que le billet ne doit décrire ni la grille de notre oracle ni la famille réservée, et que la note recommande elle-même de garder l'oracle imprévisible ; un script public des quatre nombres ; ta plume. Aucune expérience. *Selon le gabarit* : le choix justifié contre une option écartée est le pire des strates contre la moyenne, parce que l'attaquant choisit sa strate ; l'autre cause contrôlée, un oracle qui dit toujours « endommagé » et obtient une identification de 1, d'où le taux de fausse reconnaissance sur des produits propres (note sur les dommages plantés, verdict 1).

**Risques.** *Idée volée : faible à moyen* (le squelette de la campagne invite d'autres à la faire avant nous ; rien n'y est revendiqué). *Faux trou : moyen à élevé* (Gan et al. et la page 12 de « Blindfold » occupent le cœur). *Contradiction : faible* (une identification basse de notre oracle, quand elle sera mesurée, va dans le sens du billet). *Ton* : il peut se lire comme une leçon faite à des auteurs dont la vérité n'est pas validée ; à écrire d'abord contre notre propre oracle.

**Intérêt pour la bourse : fort**, si le ton est tenu. C'est la suite naturelle de A, après l'entretien.

### 2.3 C — L'hypothèse retirée avant d'être mesurée

**Thèse en une phrase.** Contre un saboteur qui connaît l'intervention et y répond au mieux, ni le rééchantillonnage, ni la paraphrase, ni la remise à zéro du contexte ne gardent de marge, et une marge mesurée sur un saboteur de laboratoire lit d'abord la façon dont on l'a fabriqué : nous avons retiré l'hypothèse avant de la mesurer, et gardé la mesure avec ses nuls écrits d'avance.

**Les pièces** [lu, sauf mention].
- La table d'origine : 41,8 % de sûreté pour la surveillance seule, à 100 % d'utilité ; 72,7 % avec la cession à la voie de confiance, 83,2 % avec le rééchantillonnage, 87,1 % pour le meilleur protocole de rééchantillonnage, 92,6 % en y ajoutant un moniteur non fiable, à 95 % d'utilité (« Ctrl-Z », p. 5, 7, 8, 9). Le pas du rééchantillonnage pèse 10,5 points sur 50,8, un cinquième ; la cession, trois cinquièmes, dépense d'utilité comprise (arithmétique refaite par moi).
- Exécuter le tirage le moins suspect « would not increase safety at all against an optimally consistent attack policy » ; leur attaquant n'est cohérent d'un tirage à l'autre qu'« around 80% of the time » ; le rééchantillonnage garde un gain d'information, « up to +10.2 pp […] with 5 samples per step » (Lucassen et Kaufman, p. 10 et 2).
- La robustesse apparente « stemmed from being tailored to a specific attack policy » (Terekhov et al., « Adaptive Attacks… », p. 7).
- L'attaquant qui sait qu'il est rééchantillonné fait passer la sûreté de 89 % à 46 % ; celui qui simule le moniteur, à 17 % (Kutasov et al., p. 5).
- L'idée est publiée comme une classe de parades, sans mesure : affaiblir l'attaquant « in a selective way » (feuille de route de Google DeepMind, p. 29).

**Ce qui n'est pas neuf** : tout ce qui précède. **Ce qui serait neuf, sous réserve** : l'argument de validité (une marge mesurée sur un organisme construit lit son mode d'induction ; marqué « supposé » par la note elle-même, N-077, § 2) ; les trois pièges de la lecture « il existe une intensité où… », dont une fausse annonce trois fois sur dix sur quinze cellules [calcul de la note sur la marge, bloc D1] ; et le cas lui-même, un retrait documenté.

**Ce qui manque.** La lecture en entier de six voisins (décision D-5 de la note) ; une relecture de cloisonnement, parce que le billet parle des modes d'induction de nos organismes ; le silence sur les deux hypothèses candidates non inscrites ; ta plume. Aucune expérience. *Selon le gabarit* : le choix justifié est la marge lue à utilité égale contre une base nommée, plutôt que la meilleure de quinze cellules ; l'autre cause contrôlée, un score qui baisse à la relance sans que rien n'ait changé (note sur la marge, verdict 7).

**Risques.** *Idée volée : faible.* *Faux trou : faible* (c'est un retrait) ; le risque inverse est de mal lire la table d'un autre, relue ici aux quatre pages. *Contradiction : moyen* : la mesure gardée peut trouver une marge positive sur l'organisme à consigne, et la note dit que les sources penchent de ce côté ; le billet doit l'annoncer et dire d'avance comment il la lira.

**Intérêt pour la bourse : moyen.** Il montre le jugement et rejoint un résultat d'un auteur du papier de l'entretien ; mais il raconte notre programme plus qu'il ne sert le lecteur.

---

## 3. Ce que j'écarte, et pourquoi

| Conception du jour | Pourquoi pas un billet maintenant |
|---|---|
| La part sue du dommage (protocole X sur le contrôle diffus, § 9) | C'est ta proposition de recherche pour la bourse elle-même. Elle dépend de ton mot sur la voie (ses décisions D-1, D-3, D-7), et la note d'entretien demande de ne la dire que « proposée, pas décidée ». La publier avant l'entretien l'expose sans la servir |
| Le second regard après la publication du plancher | Sa propre conclusion : une constante, pas un régime ; six textes en trois mois sur la couche statistique. Un billet y dirait surtout ce qui est pris |
| La taxe de l'obscurcissement (note sur l'étau, décision D-4) | Une table de voisins dont plusieurs chiffres sont lus à l'œil sur des figures, non opposables (R7) ; plusieurs voisins non vérifiés, que la note liste ; trop près du billet sur les sondes et du bras d'attaque |
| Le banc à lois plantées | « Un banc seul n'est pas un résultat » (sa § 9) ; des semaines de construction ; aucune phrase de nouveauté avant le collisionneur |
| La programmation de poids | Des faits de novembre, publiés une seule fois, sans réplication ; et un appui sur la recette de nos organismes, que la note dit supposée et non lue |
| La boucle audit, recapture, réapprentissage | Une règle interne ; « rien à revendiquer » ; un nœud ouvert |
| L'adjudant, et la lecture du collisionneur | Le fond (borner sans reconnaître) est porté par le plancher, publié. Le premier geste commun aux cinq modèles, compter les tâches qui admettent une propriété vérifiable fixée d'avance, est accordé (GO-2026-11-21-69) : **ce compte ferait un billet, quand il existera** |
| Le pont complet avec les garanties nucléaires (théorème de 1981 sur le détournement étalé, N-075, § 7) | Le meilleur sujet de fond après A et B, et sans risque de faux trou puisqu'il rend une antériorité. Mais tu dois avoir lu toi-même l'article et les deux rapports pour t'en porter garant : pas avant l'entretien |
| La sélection d'attaque, les représentations choisies, la diversité effective (protocole X sur l'attaquant) | Côté menace, ou hypothèse candidate non inscrite : hors d'un texte public aujourd'hui |

---

## 4. Recommandation

**Le billet A, seul, maintenant ; le billet B ensuite, après l'entretien, comme sa suite.** Confiance 0,65 que A soit le bon choix des trois. Les deux ont la même forme : une garantie vaut ce que vaut ce qu'elle suppose connu, la conduite de l'honnête pour A, la vue de l'oracle pour B. Le glossaire nucléaire les relie d'une phrase, à l'entrée de la probabilité d'identification : elle se calcule d'ordinaire « by assuming that the measurements are normally distributed with a known standard deviation » (entrée 9.29, p. 113 [lu]). Deux billets sur ce que les garanties de contrôle supposent : c'est un fil que tu peux tenir devant le jury.

Ce qui me ferait changer d'avis :
- la recherche d'antériorité trouve, pour l'incrimination en contrôle, la règle d'horizon ou la tolérance avec ses nombres : A devient une note de lecture de quelques lignes, et C passe devant ;
- tu ne veux rien concéder en public avant l'entretien : alors aucun des trois, et A reste ta phrase 2 ;
- tu préfères un billet qui raconte le programme : C.

Mes probabilités [jugement]. A prêt pour ta plume le 25 novembre si tu dis « go » le 22 : 0,7. En ligne avant le 1er décembre : 0,45 ; cela tient à ta plume, à ton mot, à la modération, et à l'ordre avec « Reasons or watching? ». Remarqué par un auteur du papier : 0,25. Jugé élémentaire par un lecteur du métier : 0,5, et ce n'est pas un échec s'il est juste et court.

---

## 5. Plan du billet A, en sections, selon le gabarit

Titre de travail : « How exactly must we know what honest looks like? A horizon rule for accumulating weak evidence ». Environ 1 300 mots (la colonne de droite en fait 1 310), en anglais, une figure, deux tables, un lien vers le script. Le gabarit dit la pratique majoritaire des billets bien notés ; il ne promet rien (son § « Ce que ce gabarit est »).

| N° | Section | Contenu | Mots |
|---|---|---|---|
| 0 | **Summary**, bloc étiqueté en tête | Quatre résultats chiffrés, « under stated assumptions », et une ligne de ce qui n'est pas revendiqué | 180 |
| 1 | The condition | La phrase du billet théorique ; la phrase du papier qui la cite (p. 2) ; ce que Wen et al. avaient déjà vu (p. 6) ; le cas du jeu d'audit (Taylor et al., p. 18) | 130 |
| 2 | Setup | Le monde simulé : lois, μ, m, n, niveau, puissance ; nombre de répétitions et graines. **Le choix justifié contre une option écartée, nommée** : un test à horizon fixe sur la moyenne plutôt qu'un pari valide à tout instant, parce que la formule se vérifie à la main et que le plancher ne dépend pas du test (section 6) | 130 |
| 3 | Result 1 — the plateau | La formule ; **la figure** : nombre d'actes sabotés cachés selon le nombre d'actes surveillés, échelles logarithmiques ; pente un demi pour la référence exacte, pente un au-delà de n = m pour la référence fixe, pente un demi décalée d'un facteur dix pour 1 % de témoins | 170 |
| 4 | Result 2 — what "exactly" costs | La tolérance ; la table des tailles de référence par qualité du moniteur et part sabotée | 120 |
| 5 | Result 3 — an offset does not average out | La table des fausses alertes selon le décalage et l'horizon | 90 |
| 6 | Is this an artifact? | Trois autres causes possibles, chacune contrôlée par une expérience : la loi normale et la moyenne (test de rangs, queues lourdes) ; l'indépendance (monde à scores dépendants : à faire) ; l'horizon fixe (citation du résultat sur les moniteurs tolérants) | 130 |
| 7 | Two ways out, and their price | Les témoins entrelacés et leur facteur ; le nul par acte, en une phrase de principe ; l'audit de l'issue, qui n'a pas besoin d'une référence de scores mais d'un oracle | 100 |
| 8 | What is not new | La liste du § 2.1, avec les références | 90 |
| 9 | **Limitations**, section titrée | Indépendance à l'unité choisie ; un dommage qui déplace ce qui est lu ; rien de mesuré sur un modèle ; pas de jumeau en service ; une opérationnalisation parmi d'autres de « incriminer » | 90 |
| 10 | Open questions | Quelle est la taille de la référence dans les évaluations de contrôle publiées ? Le plancher se voit-il dans des scores de moniteur publics ? Quelle référence survit à un affinage bénin ? | 50 |
| 11 | Code, and how this was made | Lien vers le script et ses graines ; ce qu'un modèle a fait (calculs, vérifications) et ce que tu as écrit | 30 |

**Rattachement aux consignes du gabarit v2.**

| Consigne ou objection (gabarit) | Où, dans le plan |
|---|---|
| 1. Énoncer le résultat principal dans les 250 premiers mots | section 0 |
| 2. Ouvrir sur un résumé des résultats, bloc étiqueté ou liste | section 0 |
| 3. Justifier au moins un choix du dispositif contre une option écartée, nommée | section 2 |
| 4. Nommer le modèle, les données et l'effectif de l'expérience principale | section 2 : ici, les lois simulées, leurs paramètres, le nombre de répétitions et les graines ; dire en toutes lettres qu'aucun modèle n'est mesuré |
| 5. Nommer une autre cause possible et la contrôler par une expérience (sous réserve) | section 6 |
| 6. Inviter les lecteurs à poursuivre (sous réserve) | section 10 |
| 7. Donner un lien vers le code (sous réserve) | section 11 |
| Convention du genre : énoncer les limites, de préférence dans une section titrée | section 9 |
| Objection à prévenir : explication concurrente du résultat | section 6 |
| Objection à prévenir : antériorité, travaux voisins | sections 1 et 8 |

**Le résumé en tête, en faits** (la prose est la tienne) : (1) avec une référence honnête de m actes, la part d'actes sabotés qui reste cachée ne descend pas sous z / (μ √m), quel que soit le temps de surveillance : 23 % pour m = 400 et un demi écart type d'écart ; (2) « exactly » veut dire : à mieux que la part sabotée fois l'écart lu ; 12 393 actes honnêtes de référence pour 2 % d'actes sabotés et un moniteur d'aire 0,77 ; (3) un décalage de 0,05 écart type entre l'honnête et sa référence donne 23 % de fausses alertes à mille actes et 99,6 % à dix mille ; (4) deux sorties : des témoins vérifiés au fil de l'eau, qui coûtent un facteur dix à 1 % ; un nul refait à chaque acte, qui demande un modèle de confiance ; (5) rien de neuf en mathématiques : une formule de manuel, appliquée à une phrase.

**À ne pas écrire** (N-076, § 11 ; note d'entretien v4, § 4) : « un résultat du programme » ; « personne n'a chiffré » ; un chiffre sans « under stated assumptions » ; « le rappel croît avec l'horizon » sans la taille de la référence ; « donc la surveillance marche », ou « donc elle ne marche pas » ; toute phrase sur nos organismes, nos sondes ou notre banc.

---

## 6. Ce qui manque au billet A : qui, combien de temps

| N° | Ce qui manque | Qui | Durée [jugement] | Bloquant |
|---|---|---|---|---|
| 1 | Ton mot : ouvrir ce billet, ce qui lève pour lui le gel des billets hors chantier, ou le rattache au chantier de l'entretien | toi | une minute | oui |
| 2 | **Recherche d'antériorité**, avant toute écriture : le forum (billets et commentaires), les travaux qui citent le billet théorique, Wen et al. et le papier de l'entretien, la détection sous bruit mal connu. Requêtes sans nom du programme. Critère de mort écrit d'avance : un texte qui donne, pour l'incrimination en contrôle, la règle d'horizon ou la tolérance avec ses nombres | un lecteur neuf d'un autre modèle | 2 à 3 h | oui |
| 3 | Le script public : mon prototype, sans chemin interne, plus le monde à scores dépendants, le décalage en rangs, la figure. Instrument (classe B) : contre-lecture par un autre modèle, puis vérification des corrections | le concepteur, puis le contre-lecteur | une demi-journée, puis 3 h | oui |
| 4 | La borne « pour tout test » : dérivation par un agent qui ne reçoit que l'énoncé ; sinon elle sort du billet | un agent neuf | 1 à 2 h | non |
| 5 | L'inventaire, par étiquettes seulement, des tailles de référence et des horizons de nos textes scellés qui accumulent (premier pas de N-076) | un lecteur autorisé, désigné par la mère | 1 à 2 h | oui, avant la mise en ligne |
| 6 | La fiche de faits : chaque nombre, son bloc, son empreinte ; chaque citation, son fichier, sa page | le concepteur | 2 h | oui |
| 7 | Le texte : toi, en français ou en anglais, d'après la fiche ; ou la session en blocs déclarés puis ta reformulation (GO-2026-11-18-50). Pour un compte neuf, la première voie est la plus sûre | toi | une demi-journée | oui |
| 8 | Lecture adverse du texte entier : chaque nombre recalculé par programme, chaque citation à sa page, la liste « à ne pas écrire » | un autre modèle ; un programme | 2 h | oui |
| 9 | Relecture de cloisonnement : courte, le billet ne porte ni résultat ni saboteur | la mère | un quart d'heure | oui |
| 10 | Ton accord exprès au moment de publier ; ton compte ; la modération, de durée inconnue | toi ; le site | non chiffrée | oui |
| 11 | Un lecteur humain du métier (contact externe : je rédige, tu envoies) ; un exemple sur des scores publics | toi ; plus tard | — | non |

**Calendrier possible**, si tu dis « go » le 22 : antériorité et script les 22 et 23 ; fiche de faits le 24 ; ta plume les 24 et 25 ; lecture adverse le 26 ; fenêtre de mise en ligne du 27 au 29. Aucune dépense de calcul : tout tient sur processeur, en minutes.

---

## 7. Décisions pour toi

Quatre nœuds, sans défaut sous 48 heures : chacun touche une publication, un gel ou un contact.

**D-1. Ouvrir un troisième billet, et lequel.**
*Enjeu* : une pièce publique avant l'entretien qui ne dépende d'aucun résultat ; deux à trois jours de travail de session, une demi-journée de toi, et un billet de plus hors du chantier de l'entretien.
- (a) Le billet A, maintenant. *Avantage* : calcul fait, forme légère pour ta plume, accord avec ta phrase 2. *Inconvénient* : peut être jugé élémentaire ; l'antériorité peut le réduire à une note.
- (b) A maintenant, B après l'entretien. *Avantage* : un fil en deux billets. *Inconvénient* : B demande cinq à six jours et une relecture de cloisonnement.
- (c) Aucun : tout l'effort sur l'entretien et sur « Reasons or watching? ». *Avantage* : rien ne se disperse. *Inconvénient* : rien de public sur ce programme le 1er décembre.

*Recommandation* : (a), en gardant (b) pour après ; confiance 0,65.

**D-2. Ce que le billet dit de la suite du programme.**
*Enjeu* : la sortie par le jumeau touche le pari apparié, et la prévision de N-076 n'est pas encore scellée.
- (a) Le billet dit la loi et les deux sorties en principe, rien sur nos organismes ni sur notre statistique. *Avantage* : aucun texte scellé touché, rien à démentir. *Inconvénient* : moins d'enjeu pour le lecteur.
- (b) Il annonce aussi la prévision, comme engagement public, une fois le texte de classe A scellé. *Avantage* : une prévision datée. *Inconvénient* : un délai de plus, et un résultat à venir qui peut la démentir.

*Recommandation* : (a) pour ce billet ; (b) pour un billet ultérieur, avec la mesure ; confiance 0,7.

**D-3. L'ordre et la date.**
- (a) Après « Reasons or watching? », avant le 1er décembre. *Avantage* : le compte n'est plus neuf, la pièce existe à l'entretien. *Inconvénient* : serré ; je ne sais pas ce que la modération fait d'un deuxième billet.
- (b) Texte fini et script public, montrés à l'entretien sans mise en ligne sur le forum. *Avantage* : aucun aléa de modération. *Inconvénient* : pas de lecteurs.
- (c) Après l'entretien. *Avantage* : le temps d'un lecteur humain. *Inconvénient* : ne sert pas la candidature.

*Recommandation* : (a) si la lecture adverse est close le 27 au soir, sinon (b) ; confiance 0,6.

**D-4. Un lecteur humain avant la mise en ligne.**
- (a) Oui, un statisticien ou un chercheur du contrôle que tu connais. *Avantage* : la seule vérification qui ne soit pas un modèle. *Inconvénient* : un à deux jours.
- (b) Non, le forum fera ce travail. *Avantage* : la date. *Inconvénient* : une erreur se paie en public.

*Recommandation* : (a) si un nom te vient tout de suite, sans retarder au-delà du 28 ; confiance 0,5.

---

## Relevé de méthode

**Chaîne de raisonnement.**
1. Les deux billets existants ne peuvent pas porter la candidature seuls : l'un attend un résultat, l'autre est d'un autre projet (état des deux billets, `fe8f75fd…`, verdict).
2. Un billet qui ne dépend d'aucun résultat doit porter sur une idée qui se vérifie par calcul ou par lecture : je ne retiens que des conceptions dont les nombres sont des lois exactes ou des citations.
3. Onze des douze conceptions du jour sont vérifiées « conforme » par leur contre-lecteur ; celle sur l'adjudant est rendue « à corriger, sur un point », et son auteur a porté ce point par un erratum, que je n'ai pas vu vérifié (verdicts des douze vérifications, relus ce jour).
4. Parmi elles, trois ont une thèse qui tient en une phrase, des nombres déjà calculés, et aucun besoin d'une pièce cloisonnée : la référence honnête (N-076, `49b664c1…`, § 2), l'identification de l'oracle (note sur la couverture, `d95d8554…`, verdict), le retrait de la marge (N-077, `41643fc5…`).
5. Le papier de l'entretien fonde son jugement contre la surveillance sur une phrase et trois appuis (p. 2 [lu]) ; sa source théorique pose la condition « exactly » ([lu]) : A répond à cette phrase, B à la limite de la page 10, C à aucune.
6. Les nombres de A se retrouvent par un code réécrit (bloc A : mêmes valeurs que la sortie `d43e62bc…`) et par tirages (bloc E1) ; ils ne tiennent pas à la loi normale (bloc E2).
7. Le voisin le plus proche de A nomme le phénomène sans le chiffrer (Wen et al., p. 6 [lu]) : A n'est pas neuf dans son objet, peut l'être dans ses nombres et sa règle. Je n'ai fait aucune recherche : la probabilité de 0,55 de la note d'origine est reprise, non refaite.
8. La politique du site ne compte ni le code ni les faits trouvés avec un modèle et rédigés par l'humain (résumé, `89f9a9ca…`, point 2) : un billet de calcul est la forme la moins lourde pour un compte neuf.
9. **Supposé** : un billet court et concédant, publié avant le 1er décembre, sert la candidature. Je n'ai lu ni l'appel de la bourse ni la composition du jury.
10. Des pas 4 à 9 : A d'abord, B ensuite, C en repli.

**Objets de contrôle.** Pour le calcul : un objet où la conclusion doit être fausse, la référence exacte, où aucun plancher ne doit paraître (rapport attendu 0,1000, rendu 0,1000) ; un objet où elle doit être vraie, la référence fixe (rapport attendu proche de 1, rendu 0,98) ; et la puissance d'un demi à l'endroit prédit (rendu 0,5018). Pour mes critères de choix : ils doivent rejeter le billet sur les sondes et « Reasons or watching? », et ils les rejettent (§ 2.0). Limite : ce second contrôle est fait par moi, après avoir lu pourquoi ces billets sont bloqués.

**Premier pas non justifié.** Le pas 9. Ce qui le justifierait : l'appel de la bourse, ses critères, et le nom de ceux qui t'entendront le 1er décembre.

**Mode d'échec affecté.** Sans objet : cette pièce n'est pas une relecture.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas un agent de re-dérivation. Mon bloc A retrouve celui de la note « percée », mais j'avais lu les trente premières lignes de son script, fonction du plancher comprise : c'est un rejeu par un code réécrit.

**Trouvaille de côté.**
1. L'annexe d'incrimination de Gan et al. tient en un alinéa et juge l'incrimination objet par objet : il faudrait une note si haute « that no honest codebase would ever receive such a high credence » (p. 37 [lu ; p. 36-37 seules]). L'accumulation sur beaucoup d'objets n'y est pas évaluée, à ces deux pages. Je n'ai pas rouvert le troisième appui du papier (Gasteiger et al.). À vérifier par une lecture entière avant de le dire.
2. Les candidats A et B se rejoignent dans une entrée du glossaire nucléaire (9.29, p. 113 [lu]) : l'identification y est calculée sous un écart type connu.
3. Dans mon tirage, une case nulle à 3,5 erreurs types ; auditée, c'est le hasard (bloc E3).
4. Le résumé de la politique du site permet la traduction mot à mot d'un texte que tu écris en français (point 8) : une voie pour tout billet à venir.
5. **Pour l'entretien.** La note d'entretien v4 écrit deux fois « 98,8 % » sans unité (§ 4, phrases sur les sondes ; § 5, objection 3). Le papier dit : « Our probes achieve 98.8% AUC in SHADE-Arena » (Hollinsworth et al., p. 1 [lu]). C'est une aire sous la courbe, non un taux de détection : à dire ainsi. Je n'ai pas touché à la note.

**Évaluateur et conseil.** Ce qui juge cette pièce : toi ; puis, pour le billet, la recherche d'antériorité, le contre-lecteur du script, la lecture adverse, le forum. Par où elle pourrait être bien jugée sans le mériter : je recommande le candidat dont j'ai pu refaire le calcul aujourd'hui, et qui est déjà une décision du programme ; c'est la lecture qui nous arrange. Audit fait : j'ai rouvert le voisin le plus proche, et il affaiblit la nouveauté ; j'ai laissé la probabilité où son auteur l'avait mise. Conseil à qui écrira : la difficulté n'est pas le calcul, c'est de ne rien dire de plus que lui.

## Ce que je n'ai pas fait

- **Aucune recherche en ligne, aucune lecture du forum.** Toute phrase « non trouvé » de cette note est reprise d'une note du jour, avec son nombre de requêtes.
- Les douze conceptions ne sont pas lues en entier : leur verdict, et les sections dites en annexe. Leurs calculs ne sont pas rejoués, sauf le bloc A de la note « percée », refait.
- Les deux billets existants, leurs brouillons et leurs fiches ne sont pas ouverts : je ne sais pas si l'un d'eux porte déjà une phrase sur la référence honnête.
- Aucun résultat du programme n'est lu. Je ne connais ni les tailles de référence ni les horizons de nos textes scellés.
- Ni l'appel de la bourse ni la composition du jury ne sont lus.
- Les PDF sont relus aux pages citées, non en entier. Ker, Bash et al., Podkopaev et Ramdas, et tous les voisins marqués [repris] ne sont pas rouverts.
- Le script et cette note ne sont pas contre-lus. Les durées et les probabilités sont des jugements.
- Ni la routine de reprise ni une passation : cette pièce est une étape d'une orchestration de la mère.

## Annexe : pièces lues, pages relues, empreintes

**Pièces du dépôt** (empreinte égale au compagnon `.sha256`, recalculée ce jour ; huit premiers signes).

| Pièce | Empreinte | Lu |
|---|---|---|
| `docs/notes/billets-v1/gabarit-billets-v2.md` | `5eee79b3` | en entier |
| `docs/notes/billets-v1/etat-des-deux-billets-2026-11-21-v1.md` | `fe8f75fd` | en entier |
| `docs/notes/veille-organismes-ideation-v2/note-entretien-controle-diffus-v4.md` ; errata 1 et 2 | `cd593d8f` ; `5e7b4c7b` ; `ad6debe3` | en entier |
| `docs/decisions/decision-N-077-retrait-marge-asymetrique-mesure-gardee-v1.md` | `41643fc5` | en entier |
| `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` ; errata 1 et 2 | `49b664c1` ; `34a59c49` ; `c2943188` | § 1, 2, 11 ; errata en entier |
| `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` ; erratum 3 v2 | `5aed4bab` ; `fbe3298e` | § 2 et 7 ; § 4 |
| `docs/notes/couverture-de-l-oracle-v1/reponse-fable-couverture-oracle-v2.md` | `d95d8554` | en-tête, verdict, § 1, 2, 3.1, 3.3, 3.7, 3.8, 4, 5 |
| `docs/notes/protocole-x-dommage-v1/reponse-fable-protocole-x-dommage-v2.md` | `c2838803` | en-tête, table des constats, verdict ; annexe réservée non ouverte |
| `docs/notes/protocole-x-attaquant-v1/reponse-fable-protocole-x-attaquant-v2.md` | `3180e43b` | en-tête, table des constats, verdict |
| `docs/notes/percee-apres-blindfold-v1/reponse-fable-percee-apres-blindfold-v2.md` | `b91e9d8e` | en-tête, verdict, § 1 à 6 |
| `docs/notes/pince-hors-distribution-v1/etau-d4-v1/reponse-fable-etau-d4-v2.md` | `838f2b8e` | en-tête, verdict, § 1 à 4 |
| `docs/notes/mecanisme-adjudant-hors-distribution-v1/reponse-fable-mecanisme-adjudant-v2.md` ; erratum 1 | `4f8fbeaf` ; `2062a4e4` | verdict ; erratum en entier |
| `docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-collisionneur-adjudant-opus-v1.md` | `c04a448a` | en entier |
| `docs/notes/banc-lois-plantees-c2-v1/conception-fable-banc-lois-plantees-v2.md` | `62c519c0` | verdict, § 9 |
| `docs/notes/protocole-x-marge-asymetrique-v1/reponse-fable-marge-asymetrique-v2.md` | `6c7e1c2f` | verdict, § 2 ; lignes des calculs C1 et D par motifs |
| `docs/notes/protocole-x-boucle-audit-recapture-v1/reponse-fable-boucle-audit-recapture-v2.md` | `3bc8585c` | verdict |
| `docs/notes/protocole-x-controle-diffus-v1/reponse-fable-controle-diffus-v2.md` | `dbe929e7` | verdict, § 9 |
| `docs/notes/protocole-x-programmation-de-poids-v1/reponse-fable-programmation-de-poids-v2.md` | `90bbe866` | verdict |
| `docs/notes/protocole-x-dommages-plantes-tiers-v1/reponse-fable-dommages-plantes-tiers-v2.md` | `1ec3cdf8` | verdict |
| `docs/notes/percee-controle-securite-v1/reponse-fable-percee-v1.md` ; son script ; sa sortie | `35599f4c` ; `9c2663e0` ; `d43e62bc` | § 7.1 seul ; trente premières lignes ; blocs A à C |
| `docs/sources/lesswrong-politique-ia-v1/resume-politique-v1.md` | `89f9a9ca` | en entier |
| `docs/procedures/consigne-commune-methode-de-recherche-v1.md` | `d327b3fc` | parties 1 et 2 |
| `registres/go.md` (sans compagnon) | `ed26d425` | cinq lignes par leur identifiant : GO-2026-11-18-50, -66 ; GO-2026-11-19-28 ; GO-2026-11-21-63, -69 ; deux lignes voisines affichées par la recherche, lues sans y chercher rien |

**Sources relues à la page ce jour** (texte tiré par `pdftotext`, page par page ; rang de la page dans le fichier ; empreinte égale au compagnon).

| Source | Fichier | Empreinte | Pages |
|---|---|---|---|
| Hebbar, billet théorique sur les menaces diffuses, copie de page web | `docs/notes/veille-organismes-ideation-v2/pdf/web-hebbar-2025-how-can-we-solve-diffuse-threats.html` | `6831b0ab` | texte entier, par motifs ; commentaires absents de la copie |
| Terekhov et al., « Diffuse AI Control on Fuzzy Tasks », version 3 | `docs/notes/veille-organismes-ideation-v2/pdf/arxiv-2606.08892.pdf` | `8858355c` | 2, 3, 10 |
| Wen et al., arXiv 2411.17693 v1 | `docs/sources/pdf/2411.17693v1.pdf` | `13a93a48` | 6 |
| Taylor et al., arXiv 2512.07810 v1 | `docs/sources/pdf/2512.07810v1.pdf` | `77e64bcd` | 3, 4, 18 |
| Gan et al., arXiv 2604.16286 v2 | `docs/sources/pdf/2604.16286v2.pdf` | `833a48e6` | 1, 8, 10, 36, 37 |
| Singh, arXiv 2610.18948 v1 | `docs/sources/pdf/science-de-la-detection-v1/erratum-1/2610.18948v1.pdf` | `53557a25` | 9 |
| « The Price of Self-Calibration », arXiv 2609.23254 v1 | `docs/sources/pdf/percee-controle-securite-v1/2609.23254v1.pdf` | `1d212b4a` | 6 |
| Sobers et al., arXiv 1608.00698 v3 | `docs/sources/pdf/percee-controle-securite-v1/1608.00698v3.pdf` | `4dcdbde7` | 1 |
| He et al., arXiv 1612.09027 v1 | `docs/sources/pdf/percee-controle-securite-v1/1612.09027v1.pdf` | `93e70341` | 1, résumé |
| Glossaire des garanties, Agence internationale de l'énergie atomique, édition 2022 | `docs/sources/pdf/couverture-de-l-oracle-v1/iaea-2022-safeguards-glossary-invs-3-rev-1-v1.pdf` | `a1875740` | 113, 114 |
| Zhu, Zuo et Sun, « Blindfold », arXiv 2610.37055 v1 | `docs/sources/pdf/attaquant-informe-v1/2610.37055v1.pdf` | `5250fa11` | 12 |
| Lucassen et Kaufman, arXiv 2605.26047 v2 | `docs/sources/pdf/2605.26047v2.pdf` | `947724f4` | 2, 10 |
| Terekhov et al., « Adaptive Attacks… », arXiv 2510.09462 v2 | `docs/sources/pdf/2510.09462v2.pdf` | `96c16e33` | 7 |
| Kutasov et al., arXiv 2511.02997 v1 | `docs/sources/pdf/2511.02997v1.pdf` | `1dcffc49` | 5 |
| Feuille de route de Google DeepMind, arXiv 2607.13087 v1 | `docs/sources/pdf/2607.13087v1.pdf` | `291a0cd7` | 29 (rang où se lit « in a selective way » ; la page 18, que les notes citent aussi pour cette idée, ne porte pas ces mots) |
| Bhatt et al., « Ctrl-Z », arXiv 2504.10374 v1 | `docs/sources/pdf/2504.10374v1.pdf` | `5f802d67` | 5, 7, 8, 9 |
| Hollinsworth et al., « Caught in the Act », arXiv 2610.12445 v1 | `docs/sources/pdf/2610.12445v1.pdf` | `7e141758` | 1, une phrase |

**Fichiers de ce dossier** : cette note ; `calculs-troisieme-billet-v1.py` ; `calculs-troisieme-billet-v1.txt` ; un compagnon `.sha256` pour chacun.
