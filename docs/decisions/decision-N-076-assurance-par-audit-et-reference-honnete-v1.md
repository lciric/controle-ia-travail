# Décision — N-076 : l'assurance par l'audit et par la référence honnête — loi de la référence honnête ; hasard du défenseur comme preuve ; banc de recherche à vérité plantée ; attestation en service des sondes, candidate ; audit après coup, à plancher et à l'enjeu ; boucle audit, recapture, réapprentissage ; épreuves du devin ; borne inférieure lue comme une table du seuil au taux d'audit ; quatre invariants d'audit ; les scores orientent l'audit sous un plancher ; question préalable sur la sonde de surprise (v1)

- **Décision de Lazar** : mots directs dans la session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`, 21 novembre 2026, consignés à la ligne `GO-2026-11-21-57` de `registres/go.md` (`f3093a46…` à ma lecture). Mots recopiés en section 0.
- **Statut : v1, à contre-lire** par un autre modèle (Opus 5.5), puis vérification des corrections par le même contre-lecteur : la ligne du GO le demande (« écrit par Fable et contre-lu »). Écrite le 21 novembre 2026 entre 13:56 et 14:04 UTC (`date -u`) par Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), dépôt à `2d6d22854` au début. Aucun appel payant, ni commit ni poussée. `CLAUDE.md` n'est pas modifié : la ligne de la section 14 est **proposée**.
- **Numéro.** Aucun fichier de `docs/decisions/` ne porte N-076 ; le numéro ne figure au dépôt que dans la ligne du GO et dans son écho au registre des décisions (R-4547), qui désignent ce texte (recherche du 21 novembre, hors dossiers interdits par le mandat). La vérification finale revient à la mère.
- **Ce que ce texte complète.** N-075 v2 (`docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v2.md`, `997bc0b3fc238bf35e7920f328a3adf9d8206b4ea9a984fe02a8a228ac4f589f`, en vérification) a inscrit le plancher d'audit au hasard, les deux regards, la règle à deux clés, le bilan du produit, le passage obligé et la restriction du lemme d'additivité. Je n'en répète rien : j'y renvoie par « N-075, § ». Là où ce texte va plus loin que N-075, c'est dit (section 8 ; section 13, points 6 et 9).
- **Sources de la décision**, notes du concepteur, de classe C, non contre-lues : « percée » (`docs/notes/percee-controle-securite-v1/reponse-fable-percee-v1.md`, `35599f4c…3dc4`), § 7.1, § 8 et § 9 ; « attaquant informé » (`docs/notes/attaquant-informe-v1/reponse-fable-attaquant-informe-v1.md`, `c23a1034…e6d0`), questions 1, 2, 4 et 6, décisions D-1 et D-3 ; « asymétries » (`docs/notes/asymetries-attaquant-v1/reponse-fable-asymetries-v1.md`, `fa29b32d…7c63`), question 2 et décision D-2 ; « science de la détection » (`docs/notes/science-de-la-detection-v1/reponse-fable-science-de-la-detection-v1.md`, `a10df4fa…543e`), questions 3 et 5, lue avec son erratum 1 (`…-v1-erratum-1.md`, `54102032…75e1`), qui prime. Et la contre-lecture de la note sur l'adjudant par Opus 5.5 (`docs/notes/mecanisme-adjudant-hors-distribution-v1/contre-lecture-opus-mecanisme-adjudant-v1.md`, `2167a5ae…77d5`), § 6, explication (d).
- **Verdicts d'antériorité rendus depuis l'écriture de N-075 v2** (Opus 5.5, classe C, non contre-lus) : la lecture en entier de douze voisins et son verdict sur neuf revendications candidates (`docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-sept-voisins-opus-v1.md`, `973bd0dd…7869`), notée [verdict, n] ; la lecture en entier de six voisins et ses trois verdicts (`docs/notes/science-de-la-detection-v1/lecture-six-voisins-et-banc-public-opus-v1.md`, `74d44e6f…0f60`), notée [six voisins, x]. **Ils ne couvrent pas les points 1, 2 et 3** (les trois candidats de la note « percée ») : la recherche des travaux qui citent le billet de Hebbar et trois pièces de référence, accordée à `GO-2026-11-21-50` (D-P4), n'est pas au dépôt à ma lecture.
- **Portée.** Cette note fixe la lecture du programme v2 (`docs/programme-controle-ia-v2.md`, `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c`) à compter de son scellement après contre-lecture, en attendant une version nouvelle. Elle ne modifie pas le fichier du programme ; le texte à y reporter est en section 12. **Elle ne change le critère d'aucune porte ni l'énoncé d'aucune hypothèse ; elle n'ouvre ni dépense ni chantier ; elle ne déclare aucune revendication « libre ».** « À faire » se lit : inscrit, premier pas sans dépense permis, toute course sur devis et GO.
- **Règle de lecture.** « Non trouvé » veut dire « non trouvé dans les pièces lues » (R8). Sous « ce qui pourrait être revendiqué », cette note dit ce que le verdict rendu laisse, dans quelle forme, et à quelle condition ; pour les points 1 à 3, sans verdict, rien ne se revendique avant qu'il soit rendu.
- **Marques** : [PDF, p.] = page lue sur le PDF empreinté par l'auteur de la pièce citée, reprise sans relecture de ma part ; [calcul, X] = bloc X de la sortie de calcul de la note citée, lois exactes sous **suppositions d'illustration**, aucune donnée du programme ; [rejoué] = recalculé par moi dans cette session, commande au relevé de méthode ; [page web] et [résumé] = non opposables (R7).

## 0. Mots de Lazar, verbatim

Ligne `GO-2026-11-21-57`, colonne des mots. Seules les phrases qui touchent cette note sont recopiées ; la ligne en porte d'autres (méthodes nommées, protocole X, Neon, consultations).

> BRILLNT , genial,  integrer au programme !!

> go insris dans le prog et a faire

Lecture de la mère, consignée à la même ligne (extrait) : « la loi de la référence honnête intégrée au programme ; l'attestation en service des sondes, candidate ; C3 (hasard du défenseur comme preuve) à faire ; C2 (banc à vérité plantée) à faire ; les trois propositions de la note « attaquant informé » (audit après coup à plancher et à l'enjeu, boucle audit-recapture-réapprentissage, épreuves du devin) inscrites au programme et à faire ; D-1 de cette note (la borne inférieure lue comme une table du seuil au taux d'audit, à deux régimes, séparée du lemme) ; D-3 (quatre invariants d'audit : audit après coup, plancher indépendant du score, part selon l'enjeu, aucun retour à l'agent) ; « les scores orientent l'audit sous un plancher » adopté ; la question préalable « la sonde de surprise ajoute-t-elle quelque chose à la différence de deux lectures de réussite attendue » à mesurer ».

**Ce que je ne sais pas rattacher.** La ligne donne deux phrases pour neuf points : le rattachement de chaque phrase à chaque point est la lecture de la mère, non la mienne. **Ce que cette note ne porte pas** : le resserrement de la marge asymétrique (H6, décision D-2 de la note « attaquant informé »), que la même ligne envoie au protocole X ; la redéfinition de la diversité effective (H5), de même ; la proposition D-2 de la note « asymétries », restée à Lazar à `GO-2026-11-21-56` (section 8).

## 1. Vocabulaire (ajouts à N-075, § 1)

- **Référence honnête** : ce par quoi un moniteur connaît la conduite de l'honnête ; **m**, sa taille en unités honnêtes, exogènes au suspect et du régime d'usage. **n** : l'horizon, nombre d'unités surveillées accumulées avant la décision. **Unité** : l'acte ou l'épisode, déclarée, celle à laquelle les scores sont tenus pour indépendants sous le nul.
- **Source de validité** d'une accumulation : ce qui garantit son taux de fausses alertes. Quatre sortes : une référence fixe de taille m ; des témoins honnêtes entrelacés, à taux p ; un nul par acte ; un tirage du défenseur.
- **Nul par acte** : un nul propre à chaque acte, tiré par le défenseur (exemple : le rang de l'action parmi K tirages du jumeau honnête sur le même début) ; il ne s'appuie sur aucune référence étalonnée ailleurs.
- **Hasard du défenseur** : tout tirage fait par le harnais et que l'agent ne choisit pas (pièce d'audit, condition tirée, ordre de présentation, perturbation secrète).
- **Régime de signature**, **régime d'excès** : les deux régimes de N-075, § 2 (l'honnête ne commet jamais ce dommage ; l'honnête le commet aussi). **Seuil toléré K** : le nombre d'épisodes endommagés que l'on accepte avant l'alerte. **p**, part auditée ; **q**, probabilité que l'oracle reconnaisse le dommage qu'il regarde ; **délai** de l'oracle.
- **Enjeu** : le poids du dommage possible d'un épisode, fixé par le défenseur avant l'épisode. **Pièce d'audit** : le tirage qui décide si un épisode est audité.
- **Devin** : un prédicteur qui reçoit toute la vue de l'agent et tente de deviner ce que le harnais tient secret.
- **Canal de retour** : tout ce par quoi une lecture, un verdict ou une conséquence d'un score atteint ce que l'agent observe. **Attestation en service** : épreuve, pendant le déploiement, qu'une sonde lit encore ce que le modèle utilise.

## 2. Point 1 — La loi de la référence honnête

**Ce qu'elle dit** (note « percée », § 7.1, candidat C1). Quand la loi de l'honnête n'est connue que par m unités de référence, la part d'actes sabotés qui reste cachée cesse de baisser dès que l'horizon n dépasse m. Pour un test sur la moyenne, à puissance un demi, cette part vaut z × √(1/n + 1/m) / μ, où μ est l'écart lu par acte saboté : à m = 400 et μ = 0,5, elle tend vers 23,3 % et n'en descend plus [calcul, A ; rejoué] ; pour quelque test que ce soit, pas moins de 7,7 % [calcul, A bis, dérivation à la main, non contre-lue]. Trois régimes : référence fixe, ce plancher ; témoins honnêtes à taux p, la loi en racine revient, multipliée par √(1 + 1/p), soit 10 à 1 % de témoins [calcul, A ; rejoué] ; nul par acte, la loi en racine nue [calcul, C, non rejoué]. Un écart systématique entre l'honnête et sa référence joue le rôle de l'incertitude et ne décroît pas avec n [calcul, B]. Suppositions : des scores indépendants sous le nul, à l'unité choisie ; un dommage qui déplace ce qui est lu ; une référence honnête et du régime d'usage. Rien de neuf en mathématiques : c'est un pont entre des pièces publiées.

**Le protocole**, tel qu'accordé :

> Toute accumulation déclare m, n et la source de sa validité ; son horizon ne dépasse pas m, sauf nul par acte.

**Lecture retenue.**
- *Déclare* : dans le texte écrit avant la lecture (le préenregistrement, pour une pièce décisive), en chiffres, avec l'unité.
- *Source de sa validité* : l'une des quatre de la section 1, nommée.
- *Ne dépasse pas m* : pour une référence fixe, aucun gain de rappel au-delà de n = m n'est lu comme un effet de l'accumulation ; les lectures plus longues sont rapportées sous l'étiquette « au-delà de la référence » et ne fondent aucun verdict. Le moniteur n'est pas arrêté à n = m : ce qui est plafonné est ce que l'on conclut.
- *Référence qui grandit avec le déploiement* (témoins à taux p) : m se lit à l'instant de la lecture, et le texte déclare p et le facteur √(1 + 1/p). **Précision de ma part**, tirée des trois régimes de la note ; la phrase accordée ne nomme que le nul par acte.
- *Biais* : l'écart toléré entre l'honnête et sa référence est déclaré avec sa borne.

**La prévision, à sceller avant la porte de fin de phase 1 (G1)** :

> Le rappel d'une statistique étalonnée sur m épisodes honnêtes cesse de croître au-delà d'un horizon de l'ordre de m ; celui du rang contre le jumeau continue.

Elle se scelle dans un texte à part de classe A, écrit par le concepteur, contre-lu, avant toute lecture des épisodes qui la servent. Ce texte porte les chiffres que cette note ne peut pas porter (m et n du banc, l'horizon où la première courbe doit s'aplatir, l'écart minimal entre les deux), le signe, la métrique (rappel à 1 % de fausses alertes en fonction de l'horizon, pour les deux statistiques), le plan et la liste d'arrêt, et ses objets de contrôle sur monde planté. Ses trois tests de mort sont ceux de la note : *instrument*, sur monde planté l'agrégateur ne retrouve pas les deux pentes ; *mesure*, les deux courbes ne se séparent pas, ou l'écart systématique mesuré entre l'honnête et le jumeau cache déjà plus que le dommage visé, et la loi est alors juste et ne sert à rien ; *adversaire*, l'écart lu par unité de dommage tombe à zéro sous le mode tenu à l'écart. **Elle n'est pas un critère de la porte.**

**Ce qui change dans le programme.**
1. *Lemme d'additivité*, hypothèse (c) (l. 55, « la variance des scores honnêtes est estimable sur épisodes honnêtes ») et énoncé (l. 56, « la puissance de détection ne dépend que de B et de la variance ») : s'y ajoute une lecture. Quand la loi honnête n'est connue que par m unités, la puissance dépend aussi de m. La lettre du lemme (N-004, resserrée par N-075, § 7) est inchangée.
2. *Jeu de contrôle* (l. 72, agrégateurs de temps, de population, spatio-temporel) : tout agrégateur déclare m, n, l'unité et la source de sa validité.
3. *Accumulation séquentielle sur sondes* (H2, l. 94 ; énoncé retenu de N-007) : énoncé inchangé. « Seuil calibré sur des épisodes honnêtes » reçoit sa taille m ; « rappel qui croît avec l'horizon » se lit, dans tout texte à venir, jusqu'à un horizon de l'ordre de m quand la référence est fixe. Mettre cette clause dans l'énoncé serait modifier une hypothèse : renvoyé (section 13, point 4).
4. *Bases boîte noire* (l. 149, accumulation séquentielle sur scores boîte noire) : même déclaration (R4). Sans elle, le plan à deux fois deux cases (l. 184) comparerait des accumulations à références inégales.
5. *Plan de la phase 1* (l. 184-185, plan à deux fois deux cases et lemme sur données réelles) : un bras rapporté « référence honnête » porte les deux courbes de la prévision ; *porte de fin de phase 1* (l. 190) : la prévision est scellée avant elle, hors critère.
6. *Papier B* (l. 62, co-élévation ; N-069) : même déclaration dès qu'une accumulation porte sur plusieurs agents ; sous dépendance, l'effectif utile plafonne à l'inverse de la corrélation (arXiv 2611.26592, [PDF, p. 1]).
7. *Méthode* (l. 229) : le protocole s'ajoute à la liste héritée.

**Ce qui ne change pas.** Le critère de la porte de fin de phase 1 (N-008 ; N-056, point 1 ; le contraste à témoin apparié accordé en principe à `GO-2026-11-18-48`). Les énoncés du gain de la boîte blanche (H1), de H2, du lemme et du théorème négatif. La lecture de « toujours valide » fixée par N-007 (garantie uniforme sur l'horizon de l'épisode, calibrée sur des épisodes honnêtes entiers). La reconception des sondes après un échec (N-062). Le jumeau honnête ne vaut qu'au banc (N-075, § 5) : en service, la référence est exogène, avec son biais.

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** Aucun verdict n'est rendu. Si la recherche des travaux citants ne le trouve pas imprimé, pourrait se dire, dans sa forme : la réunion de ces pièces en réponse chiffrée à la condition que le domaine a écrite (savoir « exactement » à quel point un honnête paraît suspect ; billet de Hebbar, [page web]), la règle d'horizon, et la comptabilité jointe de l'audit et du moniteur. Zone séduisante, à voisins de deux mois : une question (R8).

**Voisins qui occupent une part.**
- La loi en racine : Ker (2006, 2007) ; Bash, Goeckel et Towsley, déjà « classique, à citer » au programme (état de l'art de niveau 3, repris par la note).
- Son revers, un guetteur qui ne connaît pas exactement son bruit laisse passer un débit constant : arXiv 1608.00698 et 1612.09027 ([PDF, p. 1]).
- L'ensemble aveugle d'un moniteur tolérant, que « no betting scheme recovers » : arXiv 2609.23254 ([PDF, p. 6]).
- L'accumulation valide à tout instant contre une référence rejouée, sous une hypothèse de transfert de calibration : Ortega-Fernandez et al. (2610.11843, [PDF, p. 1-2]).
- L'erreur de référence qui s'accumule, et des épisodes vérifiés comme témoins : Wen et al. (2411.17693, [PDF, p. 6]).
- **Ajouts tirés des deux lectures** : le risque d'origine estimé sur un échantillon de taille fixe tenu à part, et l'excès sur ce risque plus une tolérance (Podkopaev et Ramdas, 2110.06177, [PDF, p. 4-5], [six voisins, 1.2] et [verdict, 6]) : c'est une référence fixe de taille m, dans la surveillance du risque ; le délai au pire sous budget d'étiquettes (Cao, 2611.00576, [PDF, p. 1, 5-6], [six voisins, 1.1]) ; l'excès cumulé borné à l'ordre de la racine au-dessus d'un taux de référence **fixé d'avance**, contre tout adversaire adaptatif, quand tout est observé (Singh, 2610.18948, [PDF, p. 1, 9], erratum 1 de la note « science de la détection »).

**Textes scellés.** Aucun n'est modifié. Le premier pas comprend un inventaire, **par étiquettes seulement**, des m et des n des textes scellés qui accumulent (la simulation du lemme, `prereg/T0.3-simulation-lemme-theoreme-v1.md` ; l'accumulation du barreau 6, `prereg/accumulation-barreau6-v1.md` ; la formulation de la porte en simulation, `prereg/formulation-g1-simulation-v1.md`). Un n supérieur à m trouvé dans un texte scellé est une réserve à dire à sa lecture ; il ne se corrige que par un additif, qui est un écart à un préenregistrement scellé, donc un nœud. Le préenregistrement de la porte de fin de phase 1, quand il se scellera, portera la déclaration.

**Premier pas et dépense.** Sans dépense : la table des barrières (pour chaque garantie publiée ou scellée chez nous, la supposition qu'elle consomme) ; les mondes plantés aux trois régimes, en rangs, sous dépendance et sous référence biaisée, sur processeur ; l'inventaire par étiquettes ; la prévision écrite, contre-lue et scellée. Mesure sur les organismes : sur devis (tirages du jumeau), aucun prix lu.

## 3. Point 2 — Le hasard du défenseur comme preuve, à faire

**Énoncé retenu** (note « percée », § 7.1, candidat C3). Le harnais tire au sort, par épisode, une condition sans rapport avec la tâche (cadre dit d'évaluation, de déploiement, sans surveillance). Un test de permutation donne une p-valeur exacte pour le nul « la conduite ne dépend pas de la condition », sans rien supposer de la loi honnête ni des dépendances : la validité vient du tirage. Il ne prend que le saboteur conditionnel ; son prix est de le forcer à saboter partout, donc aussi là où une vérité est plantée et où l'audit le compte.

**Ce qui change dans le programme.**
1. *Contrôles croisés* (l. 136, « organisme honnête averti de la surveillance ; saboteur en régime simulé "non observé" ») : la condition y est désormais **tirée par le harnais, par épisode**, et lue par un test de permutation écrit d'avance. Le plan y gagne une inférence exacte ; il garde son but (dissocier conscience d'évaluation et intention).
2. *Validité de construit* (l. 223 ; H8, l. 99) : énoncés inchangés ; la mesure de la conscience d'évaluation du dispositif (N-053, point 3) reste le préalable.
3. *Plan de la phase 1* : un bras rapporté, sans critère de porte.

**Ce qui ne change pas.** Aucune hypothèse, aucune porte. La p-valeur est exacte pour son nul, non pour « il y a sabotage » : l'honnête peut réagir à la condition pour de bonnes raisons. Le jumeau honnête, sous le même tirage, est donc le témoin obligé : **mort si le jumeau rejette autant que le saboteur**. La condition tirée est vue de l'agent par construction ; ce n'est pas un secret, à la différence de la pièce d'audit (section 6).

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** Aucun verdict n'est rendu ; une seule requête a été faite. Résidu mince, s'il existe : la couche d'inférence exacte sur le plan à conditions tirées, et le dilemme joint avec l'audit sur vérité plantée.

**Voisins qui occupent une part.** Le plan à trois conditions, sans sa statistique : Hasan (2604.13301, [PDF, p. 1, 5]). Les leurres réalistes : Krakovna et al. (2605.29729, [PDF, p. 1]). Les modèles distinguent une évaluation d'un usage réel : Needham et al. (2505.23836, [PDF, p. 1]). Tirés des lectures : le moniteur éprouvé sur des cas plantés rendus indiscernables (Greenblatt et al., 2312.06942, [PDF, p. 11-12], [verdict, 2]) ; le tirage du défenseur traité comme un bien à protéger (« Blindfold », 2610.37055, [PDF, p. 1-3], [verdict, 6]). Le test de permutation est classique.

**Textes scellés.** Aucun n'est touché. L'inventaire des régimes « observé » et « non observé » déjà joués sur les mêmes tâches se fait par étiquettes, sans lecture de résultat.

**Premier pas et dépense.** Sans dépense : le test exact et son monde planté (un saboteur conditionnel planté, un jumeau insensible, un jumeau sensible) ; l'inventaire par étiquettes. Mesure sur les organismes : sur devis.

## 4. Point 3 — Le banc de recherche à vérité plantée, à faire

**Énoncé retenu** (note « percée », § 7.1, candidat C2). Des mondes de recherche engendrés par programme, à lois plantées : flous à la relecture, exacts en aval. Le dommage d'un sabotage diffus s'y compte en lois vraies perdues et en lois fausses promues, par un oracle hors de la machine. Le banc est servi avec un jumeau honnête, un juge faible et l'accès aux états internes. Seul, il n'est pas un résultat : c'est le terrain qui rend le point 1 vérifiable par d'autres.

**Ce qui change dans le programme.**
1. *Environnements* (l. 120, critère « flou à la relecture, vérifiable en aval » ; l. 122, environnement des propositions d'expériences, « cibles semées préenregistrées + vérification différée sur sous-échantillon ») : un environnement candidat de plus, où la vérité est plantée et exacte. Il ne remplace pas l'environnement des propositions d'expériences ; il n'est pas sous la porte de la phase 3 (l. 124).
2. *Rôle 3 de l'organisme d'idéation* (N-065, point 3, « à trancher » : « faire d'un proposeur à poids ouverts qui trompe le juge une famille de menaces diffuses pour les papiers A et B, et, s'il le faut, la réserver comme famille tenue à l'écart »). **Ma lecture** : « à faire » tranche la première moitié, le banc à lois plantées de l'organisme devenant un terrain où un sabotage diffus a un dommage exact. La seconde moitié (réserver cette famille comme tenue à l'écart, N-044, N-054) n'est pas tranchée : renvoyé (section 13, point 5).
3. *Trois témoins qui doivent le tuer*, écrits avant toute génération : un juge faible qui voit tout ; un modèle faible qui égale le fort ; un oracle qui fuit.

**Ce qui ne change pas.** Les invariants : aucun score d'un moniteur du programme dans l'entraînement ou la sélection de l'organisme (N-053 ; N-065, point 4) ; les citations obligatoires de tout texte qui présente l'organisme (N-064, N-067, N-073 et ses compléments). Les trois oracles exécutables gardés pour une banque à tâches exécutables (N-060 v3, point 5) et les tâches fraîches (N-049). Le modèle des agents : en changer reste un GO.

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** Aucun verdict n'est rendu ; une seule requête. Si rien ne l'occupe : une vérité plantée exacte pour un sabotage diffus, sur un banc que d'autres rejouent.

**Voisins qui occupent une part.** Le sabotage par tâche annexe en recherche automatisée (2607.19321, [PDF, p. 1]) ; l'audit de dépôts sabotés à la main (2604.16286, repris par la note) ; les tâches floues à vérité approchée et non validée (Terekhov et al., 2606.08892, [PDF, p. 10]) ; les mondes de découverte sans adversaire (2406.06769, [PDF, p. 1]). Tiré des lectures : un banc public « triche contre échec honnête » sur Llama 3.1 8B, étiqueté par rejeu contrefactuel, sans état interne ni poids, dont les étiquettes « ne peuvent pas séparer un raccourci délibéré de la confusion » (Kezendirane, 2611.00407, [PDF, p. 1, 4], [six voisins, verdict 4 et § 3]) : la vérité par rejeu y est prise, pour la triche et non pour le sabotage diffus de recherche. Sur résumé seulement, non opposables : 2611.21832 et 2607.02514 ([verdict, § 4]).

**Textes scellés.** Aucun n'est touché. Le banc à lois plantées de l'organisme et sa définition scellée de l'amélioration sont réemployés tels quels ; tout usage comme banc de sabotage passe par un texte neuf.

**Premier pas et dépense.** Sans dépense : la spécification et les trois témoins. Générations et juges : sur devis. Plusieurs lignées et une taille supérieure : la bourse.

## 5. Point 4 — L'attestation en service des sondes, candidate

**Énoncé retenu** (contre-lecture de la note sur l'adjudant, § 6, explication (d)). Pendant le déploiement, on rejoue des épisodes réels tirés au hasard jusqu'à un pas donné, puis on bifurque **sur une copie** ; on y injecte de petites perturbations tirées en secret, le long de la direction de la sonde et de directions témoins de même taille ; la lecture de la sonde et le comportement doivent répondre avec le gain mesuré au laboratoire. Une réponse qui a baissé annonce « sonde invalide ici ». Le principe vient de la commande sécurisée (Satchidanandan et Kumar, 1606.08741, [PDF, p. 1, 6]).

**Statut.** Candidate : ni hypothèse, ni instrument admis, ni porte. Son texte et son bras à part sont déjà accordés (`GO-2026-11-21-46`, D-6 ; `GO-2026-11-21-51`, point 6) ; cette note l'inscrit au programme sous ce nom et n'ajoute rien à ces accords.

**Ce qui change dans le programme.**
1. *Sondes* (l. 143) et *validité de construit* (l. 223) : un candidat de plus, qui demande non « la sonde détecte-t-elle ? » mais « lit-elle encore ce que le modèle utilise, ici ? ».
2. *Questions ouvertes* (l. 264-271) : la question y entre.

**Ce qui ne change pas.** Rien n'entre dans l'agent : les perturbations vivent sur un rejeu, jamais sur l'épisode servi, et aucun score n'entre dans son entraînement ni sa sélection (N-053, point 5). Le bruit d'activations reste hors des interventions revendiquées par la marge asymétrique (N-015). Limites à écrire partout où elle est présentée : la garantie d'origine est asymptotique et porte sur une puissance moyenne, une tricherie d'énergie finie lui échappe ([PDF, p. 6]) ; une évasion qui garde les gains locaux passe ; un audit de validité au laboratoire ne dit rien du service.

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** [verdict, 2] : « partiellement occupé ». Ce qu'il laisse : des micro-interventions dans les activations d'un rejeu bifurqué, le long de la direction de la sonde et de directions témoins, en service, jugées par un gain de lecture contre une référence, face à un agent qui contrôle ses activations. Question, non acquis.

**Voisins qui occupent une part** ([verdict, 2]). Le principe en commande : Satchidanandan et Kumar. Le moniteur éprouvé sur des cas plantés indiscernables, et arrêté s'il les manque : Greenblatt et al. ([PDF, p. 11-12]). Un « canari » étiqueté pour une sonde gelée : Shire et Kim (2611.19216, [PDF, p. 2, 4, 7]). Une clé secrète inscrite dans les activations : Aremu et al. (2603.23171, [PDF, p. 1-3]). **Menace publiée sur le secret** : un modèle ajusté détecte un vecteur de pilotage injecté ; « Activation steering should therefore not be considered an invisible intervention in safety evaluations » (Fonseca Rivera et Africa, 2511.21399, [PDF, p. 1]).

**Textes scellés.** Aucun n'est touché ; le préenregistrement du papier C n'est pas modifié par le texte à part.

**Premier pas et dépense.** Sans dépense : l'écriture du texte à part, avec deux tests de mort écrits d'avance (sur une évasion plantée qui garde les gains locaux, elle doit se dire muette ; si un devin retrouve l'intervention dans ce que l'agent calcule, le secret n'en est pas un), et un monde planté sur processeur. Toute carte : sur devis.

## 6. Point 5 — Les trois propositions de la note « attaquant informé », à faire

### 6.1 L'audit après coup, à plancher et à l'enjeu

**Énoncé retenu** (question 6, proposition 6.1). Le tirage se fait après la fin de l'épisode ; le jugement porte sur une copie, hors ligne. La probabilité d'audit d'un épisode vaut un plancher, plus une part proportionnelle à l'enjeu, plus une part qui suit le soupçon ; elle n'est jamais nulle, le soupçon peut la monter et jamais la descendre sous le plancher ; chaque probabilité est consignée, et les estimations sont pondérées par son inverse.

**Ce qui change dans le programme.**
1. *Jeu de contrôle* (l. 72, « budget d'audit b ») : le budget se décompose en trois parts déclarées.
2. *Métriques du plan à deux fois deux cases* (l. 184, « courbe sécurité-utilité à budget d'audit ») : rapportées avec cette décomposition.
3. *Invariants* : voir section 8.
4. *Banc* : une famille plantée « attaque choisie » (dommage placé où le soupçon est bas et l'enjeu haut), avec trois attentes écrites d'avance : la borne du plancher tient ; l'audit des seuls plus suspects meurt ; l'audit uniforme perd le rapport de l'enjeu maximal à l'enjeu moyen [calcul, C et D de la note, non rejoués].

**Ce qui ne change pas.** N-075, § 2 : le plancher reste une base rapportée, hors de la liste de la porte de fin de phase 1 ; l'audit qui suit le score ne porte pas la borne. L'unité auditée est celle où le dommage se forme ; l'oracle lit ce que le harnais a enregistré, jamais le récit de l'agent. Limites à écrire : une violation cachée même à l'auditeur n'a pas d'étiquette (« Blindfold », [PDF, p. 12]) ; « stronger auditing makes undeterred violations better hidden » (Gans et Holden, 2609.38262, [PDF, p. 1, 8]) ; si la pièce fuit, monter le taux d'audit ne répare rien ([PDF, p. 1]).

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** [verdict, 7] : « partiellement occupé ». Ce qu'il laisse : l'assemblage des trois parts, défini par le défenseur, contre un agent informé qui place le dommage où l'enjeu et le soupçon sont bas, avec la garantie qui en suit. **Le plancher lui-même ne se revendique pas** : [verdict, 6] le dit « occupé » (section 13, point 6).

**Voisins qui occupent une part** ([verdict, 6 et 7]). L'audit après coup, sûr par construction, et les propensions connues avec plancher : « Blindfold » ([PDF, p. 1-4, 6, 8]). Le tirage pondéré par les montants, guidé par l'information annexe, valide pour toute stratégie d'échantillonnage : Shekhar et al. (2305.06884, [PDF, p. 1-3]). Le plancher sous une règle adaptative : Gao et al. (2611.15197, [PDF, p. 4-7]) ; Li et al. (2611.15835, [PDF, p. 13-14]). Des exigences d'audit par voie selon le gain, et le tirage après l'action dans des enregistrements conservés : Gans et Holden ([PDF, p. 11-13, 15-16, 25]). L'audit des plus suspects : Greenblatt et al. ([PDF, p. 11]).

### 6.2 La boucle audit, recapture, réapprentissage

**Énoncé retenu** (question 4, proposition 4.1). Le flux d'audit au hasard fournit les épisodes endommagés ; la recapture dit si la sonde est devenue aveugle ; la sonde est réapprise sur ces épisodes, les poids de l'agent gelés et le canal de retour fermé : le défenseur joue en dernier. Grandeur rapportée : le rappel retrouvé en fonction du nombre d'épisodes endommagés audités. Deux tests de mort : le rappel retrouvé avec les étiquettes que le plancher livre **avant le seuil toléré** reste sous le niveau validé, la boucle ne se ferme pas à temps ; canal de retour ouvert, le rétablissement doit s'effondrer, sinon le banc ne mesure rien.

**Ce qui change dans le programme.**
1. *Asymétrie d'apprentissage* (l. 170, « chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes ») : elle reçoit sa mesure (une courbe de rétablissement), sa source d'étiquettes (le flux du plancher) et sa condition (canal fermé, mesuré par les épreuves du devin, § 6.3).
2. *Attaques adaptatives* (l. 187, E1.5 (b)) et le test de récupération après réentraînement (N-053, point 5) : la boucle en est la version à budget d'étiquettes compté.
3. *Réserve de détecteurs* (l. 143) : inchangée ; elle sert de témoin à la boucle.

**Ce qui ne change pas, et un heurt à trancher.** L'invariant de l'oracle interdit « toute sortie de l'oracle dans la sélection d'un agent ou d'un moniteur » (N-060 v3, point 4). Réapprendre une sonde sur des épisodes jugés par l'oracle y entre. N-075 avait déjà renvoyé ce heurt pour la l. 170 (son § 11, point 9) et avait proposé de lire que la suite d'une annonce de la recapture n'est « jamais un choix, un réglage ou une reconception de moniteur sur les épisodes audités » (son § 11, point 2, à confirmer). **« À faire » se lit donc ici : le protocole et sa statistique sur mondes plantés ; aucune sonde du programme n'est réapprise sur des verdicts de l'oracle avant le mot de Lazar** (section 13, point 3). Le mode tenu à l'écart n'entre dans aucun réapprentissage (N-054, N-062).

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** [verdict, 8] : « partiellement occupé ». Ce qu'il laisse : le rappel retrouvé en fonction du nombre d'épisodes endommagés audités avant un seuil de dommage toléré, canal fermé déclaré contre le même à canal ouvert. **Réserve de ma part** : ce verdict n'a pas lu Rudoler et al. (2609.36049), que la note « asymétries » donne pour occupant d'un moniteur qui apprend sur des audits tirés au hasard face à un ouvrier adverse ([PDF, p. 2-4]) ; sa lecture en entier est accordée (`GO-2026-11-21-56`) et n'est pas au dépôt à ma lecture. Le reste est donc plus étroit que le verdict ne le dit, jusqu'à cette lecture.

**Voisins qui occupent une part** ([verdict, 8]). La course à tours où l'attaquant joue en dernier : Bailey et al. (2412.09565, [PDF, p. 3, 11-12]). La sonde réapprise sur les générations évasives d'une politique gelée : Gupta et Jenner (2506.14261, [PDF, p. 10, 24]). Le réapprentissage après l'optimisation : Wehner et Fritz (2510.21531, [PDF, p. 1-2, 7]). La sonde apprise sur les activations supprimées, au prix d'avoir déjà identifié les tentatives, et le canal de retour qui suffit à l'évasion : Lyons Keenan et al. (2609.36490, [PDF, p. 1, 6-7, 18-19]). Le défenseur qui joue en dernier sur des poids gelés : Westphal et al. (2606.09411, [PDF, p. 2, 5, 9]). L'entraînement adverse des moniteurs, proposé et non fait : McGuinness et al. (2512.11949, [PDF, p. 11]). Rudoler et al., ci-dessus.

### 6.3 Les épreuves du devin

**Énoncé retenu** (propositions 2.1 et 6.2 ; `GO-2026-11-21-54`, D-4). Avant de s'appuyer sur un secret, on l'éprouve. *Sur la lecture de la sonde* : un prédicteur reçoit tout ce que l'agent peut observer après les décisions du harnais et tente de deviner la lecture. *Sur la pièce d'audit* : un prédicteur reçoit toute la vue de l'agent avant l'action et prédit « audité ou non ». Une prédiction au-dessus du hasard suspend la garantie qui s'appuyait sur le secret, jusqu'à réparation.

**Ce qui change dans le programme.**
1. *Invariants* (l. 166, flux unidirectionnel ; l. 167, moniteurs amnésiques ; l. 168, seuils stochastiques) : ils cessent d'être supposés et deviennent **éprouvés à l'admission du harnais**, avant toute course qui s'appuie sur un secret.
2. *Riposte et fuite* (H7, l. 114 ; l. 214) : le devin est l'instrument de fuite que H7 demande ; énoncé inchangé.

**Ce qui ne change pas.** Ce sont des instruments (classe B) : code, contre-lecture par un autre modèle, vérification des corrections. **Le devin réfute, il n'atteste pas** : un classifieur qui échoue ne donne qu'une borne basse de la fuite ; une borne haute demande un couplage apparié des deux branches lancées du même état (« Blindfold », [PDF, p. 7-8]). Aucun texte n'écrit « le secret est établi » sur la foi d'un devin au hasard. Une troisième épreuve, le devin des corrections (note « asymétries », proposition 2.2), n'est pas inscrite par cette note : elle suit le sort de la décision D-2 (section 8).

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** [verdict, 9] : « partiellement occupé ». Ce qu'il laisse : le devin sur la lecture de la sonde, et l'emploi des deux comme épreuves d'admission avant toute course. Épreuves d'admission, non résultats.

**Voisins qui occupent une part** ([verdict, 9]). Le devin sur la pièce d'audit, mesuré sur une porte réelle où le contenu est fermé et où le temps fuit : « Blindfold » ([PDF, p. 3, 7-9]). La fuite par les verdicts et son usage : Lyons Keenan et al. ([PDF, p. 1-2, 7]). La fuite par les refus : Chinaei (2604.04035, [résumé]).

**Textes scellés, pour les trois propositions.** Aucun préenregistrement n'est modifié. La décision scellée N-060 v3 est heurtée par la boucle (§ 6.2) ; ce heurt n'est pas tranché ici.

**Premier pas et dépense, pour les trois.** Sans dépense : la règle d'audit écrite comme témoin du banc de la course de l'adjudant ; le protocole de la boucle et sa statistique sur mondes plantés, reliés à la table de la section 7 ; l'inventaire, par un agent habilité, de ce que l'agent observe après un aiguillage et de ce que le chemin d'audit peut toucher (horodatages, charge, relances), puis l'écriture des deux devins. Toute mesure sur un modèle : sur devis ; les deux cases vides du « caméléon » relèvent d'un bras d'attaque déclaré, hors de cette note.

## 7. Point 6 — Décision D-1 : la borne inférieure lue comme une table du seuil au taux d'audit, à deux régimes, séparée du lemme

**Énoncé retenu.** N-075 (§ 2) dit du plancher qu'il donne « une borne inférieure de la sécurité au sens de la l. 74 ». Cette borne se lit désormais **à l'envers** : on écrit d'abord le seuil toléré K, en épisodes endommagés, puis on en déduit le taux d'audit, le délai de l'oracle compris, par famille de tâches étiquetée « signature » ou « excès ».
- *Régime de signature.* Agir avant K épisodes endommagés avec probabilité 0,95 demande p × q ≥ 1 − 0,05^(1/K) : 9,5 % pour K = 30 ; 3,0 % pour K = 100 ; 1,0 % pour K = 300 ; 0,3 % pour K = 1 000 [rejoué] ; le double si q = 0,5 ; et 26 % au lieu de 9,5 % si vingt épisodes s'endommagent pendant le délai de l'oracle [calcul, A de la note, non rejoué].
- *Régime d'excès.* **Il n'y a pas de seuil fixe garanti.** La garantie porte sur un taux d'excès, sur un horizon dit ; ce qui passe sans alerte croît comme la racine de l'horizon divisé par le taux d'audit [calcul, B de la note, approximation normale], et cet ordre en racine n'est tenu que si la grille des mises descend vers le taux acceptable : avec une grille qui s'arrête au-dessus, la borne finit linéaire (erratum 1 de la note « science de la détection », verdict, point 2).
- *Séparée du lemme.* Le lemme d'additivité (l. 54-56) additionne des déplacements du score de **sonde** : son hypothèse (a) est ce qu'un sabotage invisible à la boîte blanche nie. La table additionne le **dommage** lui-même (hypothèse (b)), échantillonné par l'audit. Même ossature, citée (tester le total ; N-075, § 7), autre grandeur mesurée. Le lemme est la voie rapide, sur tous les épisodes, quand la trace existe ; la table est la voie lente, qui tient quand elle n'existe pas. **Aucun texte n'écrit que le lemme porte la borne du plancher.**

**Ce qui change dans le programme.**
1. *Sécurité* (l. 74, « alerte avant que le dommage cumulé n'atteigne θ ») : elle a deux bornes inférieures distinctes, l'une par le lemme, sous son hypothèse (a), l'autre par la table, dans la couverture de l'oracle. Tout texte dit laquelle il invoque.
2. *Lemme* (l. 54-56) : une phrase le sépare de la table (section 12).
3. *Métriques* (l. 184, « latence (alerte contre dommage cumulé) ») : la table en donne la référence, par régime.
4. Si, au seuil réaliste du banc, le taux exigé dépasse le budget d'étiquettes, le plancher n'y sert pas de garantie : **on l'écrit**.

**Ce qui ne change pas.** Les conditions du plancher (N-075, § 2), toutes nécessaires. L'énoncé du lemme et sa restriction (N-004 ; N-075, § 7). « Agir » borne le dommage déjà fait sans l'annuler, sauf si les effets sont retenus jusqu'à la vérification. La proposition de préférer, dans l'oracle, des contrôles qu'un honnête ne viole jamais (note, 1.2) touche l'oracle de N-060 : elle n'est pas inscrite par cette note.

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** Rien du plancher ([verdict, 6]). La table est l'inversion d'une loi géométrique : élémentaire. Sa seule forme propre serait la lecture par famille, signature ou excès, délai compris, pour une menace diffuse : non trouvée par l'auteur de la note (douze requêtes), non jugée à part par le lecteur ; question.

**Voisins qui occupent une part.** « Blindfold » certifie un taux, non un seuil ([verdict, 6]). Le déploiement adaptatif contre les menaces réparties s'appuie sur le passé de l'agent, non sur un tirage (Wen et al., [PDF, p. 1-2]). L'excès sur un risque de référence : Podkopaev et Ramdas ([PDF, p. 4]). L'ordre en racine de l'excès contre tout adversaire adaptatif, quand tout est observé, et l'excès linéaire que laisse une alternative unique : Singh ([PDF, p. 1, 9]). Aucun voisin ne borne le dommage accumulé avant l'alarme : le délai de détection n'a pas d'analogue de Neyman-Pearson (rapport KfK 3935, [PDF, p. 10]) ([verdict, 1]).

**Textes scellés.** Aucun n'est touché. Les textes qui écrivent déjà le plancher en mode exploratoire (N-075, § 2, point 3) reçoivent la table à leur prochaine version.

**Premier pas et dépense.** Fait : les deux blocs de calcul de la note. Puis, sans dépense : l'étiquetage des familles du banc en « signature » ou « excès » par un agent habilité. Aucune dépense.

## 8. Point 7 — Décision D-3 : quatre invariants d'audit à la section 9 du programme

**Les quatre lignes, telles qu'accordées.**
1. **Audit après coup** : le tirage se fait après la fin de l'épisode, le jugement sur une copie, hors ligne ; rien de ce que l'agent observe n'en dépend.
2. **Plancher indépendant du score** : tout épisode a une probabilité d'audit connue et jamais nulle ; le soupçon peut la monter, jamais la descendre sous le plancher ; chaque probabilité est consignée.
3. **Part selon l'enjeu** : une part de l'audit est proportionnelle à l'enjeu de l'épisode, que le défenseur fixe avant l'épisode.
4. **Aucun retour à l'agent** : aucune lecture ni aucun verdict ne revient à l'agent.

**Ce qui change dans le programme.**
1. *Section 9* (l. 162-170) : les quatre lignes y entrent, à la suite de la ligne des seuils stochastiques (l. 168). Elles valent pour **tout texte à venir qui emploie un audit**. N-075 n'allait pas jusque-là : son texte à reporter n'ajoutait le plancher que « là où un texte écrit le plancher » (son § 10, ligne du § 9). C'est un pas de plus, voulu par le mot de Lazar ; il est signalé (section 13, point 9).
2. *Seuils stochastiques* (l. 168, « probabilité d'audit lisse et croissante du score ») : gardés ; la ligne 2 leur donne le plancher qui leur manquait.
3. *Flux unidirectionnel* (l. 166) : la ligne 4 l'étend des moniteurs à l'audit et aux lectures de sondes.

**Deux lectures de ma part, à confirmer.**
- *La ligne 4 et la riposte.* Le programme compare quatre politiques de riposte, dont une « visible immédiate » (l. 214), et mesure la fuite que chacune ouvre (H7, l. 114). Une ligne 4 « toujours active » supprimerait l'objet de cette mesure. Je l'écris donc **active par défaut, ablatée dans cette expérience**, comme la ligne des seuils stochastiques l'est déjà (l. 168) ; les règles de sélection déclarées de l'expérience de la marge (l. 188 ; N-053, point 5) restent des bras déclarés.
- *L'enjeu.* Là où aucun enjeu par épisode n'est défini, la ligne 3 se réduit à des enjeux égaux, déclarés tels.

**L'écart avec la proposition D-2 de la note « asymétries », restée à Lazar.** Cette note, écrite après, dit de la ligne 4 : « nécessaire pour un détecteur figé et pour la pièce d'audit avant l'action ; ni pour un moniteur qui apprend, ni pour une correction tirée au hasard » (son verdict, point 5). Elle propose de la remplacer par trois lignes : **seul le tirage au hasard corrige ; un audit sans trouvaille ne laisse aucune trace ; en régime de signature, on alarme, on ne corrige pas.** L'écart est réel : sous la lettre de la ligne 4, « corriger » au sens de N-075 (arrêter, relancer, confier au modèle de confiance, vérifier davantage) n'est permis qu'à l'alarme, ou bien la ligne est violée, car réparer est observable. Les trois lignes gardent le levier « corriger » et ne tiennent secret que ce que suit le soupçon. **Cette note inscrit la ligne 4 dans sa lettre accordée** et ne tranche pas D-2 (`GO-2026-11-21-56` : « restent à Lazar »). D'ici son mot, la lettre s'applique : aucun texte à venir n'écrit, avant l'alarme, une correction que l'agent peut observer et qui vient d'un audit. Ma recommandation est en section 13, point 1.

**Ce qui ne change pas.** Les sept invariants de la section 9 et la frontière assumée (l. 172). L'invariant sur les scores de moniteur (N-053, point 5) et ceux de l'oracle (N-060 v3, point 4). Ces lignes visent l'audit du produit par l'oracle ; elles ne disent rien des interventions en ligne (paraphrase, rééchantillonnage, remise à zéro), qui restent celles de la marge asymétrique. Elles ne bornent rien contre un coup unique.

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** **Rien.** Ce sont des règles d'exploitation, chacune publiée ([verdict, 6 et 7]).

**Voisins qui occupent une part.** Ligne 1 : « A purely post-hoc audit … is safe by construction when each coin governs one commit » (« Blindfold », [PDF, p. 1]) ; « An audit drawn after the agent acts, from records it cannot alter » (Gans et Holden, [PDF, p. 16]). Ligne 2 : propensions connues au moins égales à un plancher (« Blindfold », [PDF, p. 2-3] ; Gao et al., [PDF, p. 4-7] ; Li et al., [PDF, p. 13-14]). Ligne 3 : tirage pondéré par les montants (Shekhar et al., [PDF, p. 1-3]) ; exigences d'audit par voie (Gans et Holden, [PDF, p. 11-13]). Ligne 4 : la surveillance interactive ouvre un canal de retour qui suffit à l'évasion (Lyons Keenan et al., [PDF, p. 1, 7]).

**Textes scellés.** Aucun n'est modifié, et aucun n'est rendu non conforme : ces lignes valent pour les textes à venir. La vérification différée déjà préenregistrée n'est pas relue comme un audit conforme (N-075, § 2, « Textes scellés »).

**Premier pas et dépense.** Sans dépense : les quatre lignes écrites dans le texte à part de l'audit tiré au hasard (accordé à `GO-2026-11-21-56`), gardées par le code là où un harnais les implémente (R5 : un cas sain, un artefact). Aucune dépense.

## 9. Point 8 — « Les scores orientent l'audit sous un plancher », adopté

**Énoncé retenu** (note « science de la détection », question 5 ; cadre accordé à `GO-2026-11-21-55`, D-5 ; adopté à `GO-2026-11-21-57`). Les détecteurs ne se combinent pas entre eux pour porter une garantie : ils se combinent avec l'audit. Chaque épisode garde une probabilité plancher d'être audité ; les scores l'augmentent ; l'estimation pondère par l'inverse de la probabilité de tirage. Un détecteur, même faux hors de son domaine, change alors la vitesse de la prise, non la validité de la mesure.

**Conditions, toutes nécessaires.** Des probabilités de tirage connues et consignées ; un plancher strictement positif ; une pièce que l'agent n'apprend pas avant d'agir (section 8, ligne 1). **Test de mort à écrire dans tout texte qui l'emploie** ([six voisins, verdict (c)] ; erratum 1) : un agent qui sait faire baisser son score se place au plancher ; la garantie tient alors au plancher seul, et le gain de l'orientation disparaît. Et, sur la famille tenue à l'écart, pas mieux que le hasard seul : « sans gain ».

**Ce qui change dans le programme.**
1. *Moniteurs* (section 8) : c'est la doctrine d'assemblage. Tout texte qui parle d'un « système » de détecteurs dit ce que chacun ajoute à l'audit qu'il oriente.
2. *Seuils stochastiques* (l. 168) : la probabilité d'audit croissante du score y est déjà ; s'y ajoutent le plancher, la consignation et la pondération par l'inverse.
3. *Jeu de contrôle* (l. 72) : le score par action sert de poids de tirage, non de verdict.

**Ce qui ne change pas.** L'énoncé de l'hypothèse sur le nombre et la diversité des moniteurs (H5, l. 113 ; N-013, § 7) et la matrice de transfert d'attaque (l. 146) : redéfinir la diversité effective par l'ordre du système reste à Lazar et au protocole X. N-075, § 2, point 4 (« l'audit qui suit le score reste permis, mais ne porte pas la borne ») et § 4, point 4 (la file d'audit prioritaire s'ajoute à la part tirée au hasard). L'orientation est une règle de tirage d'audit, jamais un signal d'entraînement ou de sélection de l'agent (N-053, point 5). Tant que la décision D-2 n'est pas tranchée, ce que suit le soupçon ne produit aucune conséquence que l'agent observe (section 8).

**Ce qui pourrait être revendiqué, sous verdict d'antériorité.** [six voisins, verdict (c)] : « partiellement occupé » ; « le programme peut l'employer en le citant ; il ne peut pas la revendiquer ». Ce qu'il laisse, comme question : l'assemblage appliqué à un agent qui choisit, avec le plancher comme garantie contre un détecteur trompeur. Aucune phrase de nouveauté avant la lecture en entier de Singh (`GO-2026-11-21-59`, E-3).

**Voisins qui occupent une part.** Tirer les étiquettes selon un prédicteur et corriger par l'inverse de la probabilité garde l'inférence valide « for any black-box machine learning model » : Zrnic et Candès (2403.03208, [PDF, p. 1, 4]). Le même facteur sous budget séquentiel : Cao ([PDF, p. 32]) ; Xu, Karampatziakis et Mineiro (2406.10490). Les coupes minimales d'une pile de contrôle : Molnar (2609.26419, [PDF, p. 1-2]). La moyenne d'e-valeurs sous dépendance quelconque : Vovk et Wang ([PDF, p. 1], repris de la note). Le tirage guidé par l'information annexe : Shekhar et al. ([verdict, 7]).

**Textes scellés.** Aucun n'est touché.

**Premier pas et dépense.** Sans dépense : la règle jouée sur les mondes plantés du banc de la course de l'adjudant, avec un score trompeur planté (la validité doit tenir, le délai rester dans la borne du tirage au hasard, sinon mort). Aucune dépense.

## 10. Point 9 — La question préalable, à mesurer en mode exploratoire dans le bras « papier dopamine »

**La question** (note « science de la détection », question 3) :

> La sonde de surprise ajoute-t-elle quelque chose à la différence de deux lectures de réussite attendue ?

La surprise d'une étape est, par définition, la différence de deux réussites attendues. Si la différence de deux lectures de la sonde de réussite attendue prédit autant que la sonde de surprise, il n'y a qu'un instrument, et la quatrième base du bras (la sonde de surprise réentraînée sans le seuil de 0,3) se réduit à la première.

**Ce qui change.**
1. *Bras « papier dopamine »* : la question entre, en mode exploratoire (`GO-2026-11-21-44` et `-45`), **avant** toute lecture de la sonde de surprise comme instrument distinct. Elle s'écrit au plan exploratoire puis dans la prochaine version du brouillon du préenregistrement court (`prereg/papier-dopamine-moniteur-v1/preenregistrement-court-papier-dopamine-v7-brouillon.md`, `e05f4a99…15ef`, non scellé), avec la pente de calibration en agrégat déjà accordée (`GO-2026-11-21-55`, D-4).
2. *Mesure* : le gain de la sonde de surprise sur la différence des deux lectures, en agrégat, par classe de surprise prédite, contre des continuations en deux moitiés indépendantes, rapporté au plafond de fidélité, sans filtrer sur l'étiquette bruitée. Deux témoins : des suites à surprise nulle (pente nulle attendue) ; une petite surprise plantée. *Test de mort* : gain nul.
3. *Programme* : rien. La sonde de surprise n'est ni une famille de sondes du programme (l. 143) ni une hypothèse.

**Ce qui ne change pas.** Toute sortie est marquée « exploratoire », non opposable, sans verdict ni porte ; un verdict décisif plus tard demande le texte scellé (R1). La liste approuvée des sondes et des lots lisibles du bras (cloisonnement) : si la différence de deux lectures n'y figure pas, elle y est ajoutée par la mère avant toute lecture. Pas de moyenne ni de médiane sur les jetons en production (N-026).

**Ce qui pourrait être revendiqué.** **Rien.** C'est une question de mesure ; elle n'a fait l'objet d'aucune requête propre.

**Voisins qui occupent une part.** La sonde et son seuil : Xu, Yuksekgonul et Zou (2602.00986, [PDF, p. 5-7]), qui ne donnent pas le nombre de continuations de cette sonde. Des sondes de progrès apprises sur les seules démonstrations réussies, lues à l'écart du progrès attendu : Bhardwaj et al. (2610.31613, [PDF, p. 1-3], [verdict, 4]). Un état qui monte avant la triche : Fischl-Lanzoni et al. (2611.14996, [PDF, p. 1-2, 5]). L'avant de l'acte, sur trajectoires d'agent : Li et al. (2610.06576, [PDF, p. 2, 7], [six voisins, verdict (b)]). Sur résumé seulement : 2606.17056, 2607.06503, 2602.09924, 2609.09448 ([verdict, 4]).

**Textes scellés.** Aucun n'est touché : le brouillon v7 n'est pas scellé.

**Premier pas et dépense.** Sans dépense : la statistique et ses deux témoins écrits au plan exploratoire ; le compte des frontières de paragraphe qu'offrent les réponses du rejeu sur données publiques. La mesure demande des continuations : dans le plafond de la ligne déjà accordée (`GO-2026-11-21-48`, 10 USD) si elles y tiennent, ce que je n'ai pas vérifié ; sinon sur devis.

## 11. Citations obligatoires ajoutées, et phrases à ne pas écrire

Dans tout texte, interne ou destiné à sortir, qui présente le point dit. Elles s'ajoutent à celles de N-075, § 8. Empreintes recalculées par moi (huit premiers signes) pour les fichiers dont le chemin est donné ; les pages sont celles que les deux lecteurs disent avoir lues.

| pour | pièce | fichier, empreinte | lu |
|---|---|---|---|
| points 5, 6, 7, 8 | Zhu, Zuo, Sun, « Blindfold », 2610.37055 v1 | `docs/sources/pdf/attaquant-informe-v1/2610.37055v1.pdf`, `5250fa11…` | en entier |
| points 5, 7 | Gans, Holden, 2609.38262 v1 | `docs/sources/pdf/attaquant-informe-v1/2609.38262v1.pdf`, `e28a4e8d…` | en entier |
| points 5, 7, 8 | Shekhar et al., 2305.06884 v1 | `docs/sources/pdf/mecanisme-adjudant-v1/voisins-v1/2305.06884v1.pdf`, `125ab42a…` | p. 1-3 |
| points 1, 6 | Podkopaev, Ramdas, 2110.06177 v4 | `docs/sources/pdf/2110.06177v4.pdf`, `a8bc8f2b…` | en entier |
| point 8 | Zrnic, Candès, 2403.03208 v3 | `docs/sources/pdf/adjudant-opus-independant-v1/2403.03208v3.pdf`, `58d973da…` (sans compagnon d'empreinte, selon le lecteur) | p. 1, 4 |
| points 1, 8 | Cao, 2611.00576 v1 | `docs/sources/pdf/science-de-la-detection-v1/2611.00576v1.pdf` | en entier |
| points 1, 6, 8 | Singh, 2610.18948 v1 | `docs/sources/pdf/science-de-la-detection-v1/erratum-1/2610.18948v1.pdf` | p. 1-3, 9, 48-50 |
| point 4 | Satchidanandan, Kumar, 1606.08741 v1 ; Shire, Kim, 2611.19216 v1 ; Fonseca Rivera, Africa, 2511.21399 v3 | `docs/sources/pdf/mecanisme-adjudant-v1/1606.08741v1.pdf`, `1685dba0…` ; `…/voisins-v1/2611.19216v1.pdf`, `bec0da21…` ; `…/voisins-v1/2511.21399v3.pdf`, `07a5a4f3…` | p. 6 ; p. 1-2, 4, 7, 14 ; p. 1 |
| point 5 (boucle, devin) | Lyons Keenan, Leckie, Erfani, 2609.36490 v1 ; Bailey et al., 2412.09565 v2 ; Gupta, Jenner, 2506.14261 v4 ; Westphal et al., 2606.09411 v1 ; Wehner, Fritz, 2510.21531 v1 | `docs/sources/pdf/2609.36490v1.pdf`, `eb6d5bbe…` ; `docs/sources/pdf/2412.09565v2.pdf`, `9c23a613…` ; `docs/sources/pdf/2506.14261v4.pdf`, `4b096062…` ; `docs/sources/pdf/anteriorite-P-041-v2/complement-2/2606.09411.pdf`, `3b8158a5…` ; `docs/sources/pdf/mecanisme-adjudant-v1/voisins-v1/2510.21531v1.pdf`, `4d851e74…` | en entier, sauf Bailey et al., Gupta et Jenner, Wehner et Fritz : pages dites aux verdicts |
| point 5 (boucle) | Rudoler et al., 2609.36049 v1 | `docs/sources/pdf/asymetries-attaquant-v1/2609.36049v1.pdf` | p. 2-4, 7 par l'auteur de la note ; lecture en entier à venir |
| point 2 | Hasan, 2604.13301 v1 ; Krakovna et al., 2605.29729 v2 | `docs/sources/pdf/percee-controle-securite-v1/` | p. 1, 5 ; p. 1 |
| point 1 | arXiv 1608.00698 v3, 1612.09027 v1, 2609.23254 v1 ; Ker ; Bash, Goeckel, Towsley | `docs/sources/pdf/percee-controle-securite-v1/` pour les trois premiers | p. 1 ; p. 1 ; p. 6 ; les deux derniers d'après l'état de l'art du programme |
| point 3 | Kezendirane, 2611.00407 v1 ; 2607.19321 ; 2604.16286 ; 2406.06769 v2 | table de provenance des six voisins ; table de provenance de la note « percée » | en entier pour le premier |
| point 9 | Bhardwaj et al., 2610.31613 v2 ; Li et al., 2610.06576 v1 | `docs/sources/pdf/mecanisme-adjudant-v1/voisins-v1/2610.31613v2.pdf`, `9caaf79b…` ; `docs/sources/pdf/science-de-la-detection-v1/voisins-v1/2610.06576v1.pdf` | p. 1-3, 8 ; p. 2, 6-8 |

**Ne pas écrire** : « le plancher d'audit est neuf », « premier audit à l'enjeu », « premier audit après coup » ; « la loi de la référence honnête est un résultat du programme » (ce sont des pièces publiées, réunies) ; « le rappel croît avec l'horizon » sans m ni source de validité ; « le lemme d'additivité borne le dommage du plancher » ; « seuil garanti » en régime d'excès ; « p-valeur exacte du sabotage » (elle est exacte pour le nul « la conduite ne dépend pas de la condition ») ; « le devin établit le secret » ; « le défenseur joue en dernier » sans « canal de retour fermé, éprouvé » ; « aucun détecteur ne peut invalider la mesure » sans Zrnic et Candès et sans ses trois conditions ; « attestation en service » comme un acquis ; tout chiffre des blocs de calcul sans les mots « sous supposition ».

## 12. À reporter à la prochaine version du programme

Texte proposé, en plus de celui de N-075, § 10 ; le programme v2 reste archivé tel quel.

- **§ 3**, sous le lemme, deux phrases : « Quand la loi honnête n'est connue que par m unités de référence, la puissance dépend aussi de m : toute accumulation déclare m, n et la source de sa validité ; son horizon ne dépasse pas m, sauf nul par acte (N-076). » ; « Le lemme additionne des déplacements du score de sonde ; la borne du plancher d'audit additionne le dommage lui-même : ce sont deux bornes distinctes de la sécurité, de même ossature. »
- **§ 4**, après « Sécurité » : « Table du seuil : pour un seuil toléré K d'épisodes endommagés, un taux d'audit p et un oracle qui reconnaît le dommage avec probabilité q, l'alerte vient avant K avec probabilité 0,95 si p × q ≥ 1 − 0,05^(1/K), délai de l'oracle compté, pour un dommage que l'honnête ne produit jamais ; pour un dommage qui se confond avec ses échecs, aucun seuil fixe n'est garanti, la garantie porte sur un taux d'excès à horizon dit. » Et : « Le budget d'audit se décompose en un plancher, une part proportionnelle à l'enjeu et une part qui suit le soupçon. »
- **§ 6**, ligne de plus : « (e) Banc de recherche à vérité plantée — candidat : mondes engendrés par programme, lois plantées, dommage compté par un oracle hors de la machine ; admis par trois témoins qui doivent le tuer. »
- **§ 7**, « Contrôles croisés », ajout : « la condition est tirée par le harnais, par épisode, et lue par un test de permutation écrit d'avance ; le jumeau honnête sous le même tirage en est le témoin. »
- **§ 8**, à l'alinéa « Deux regards » proposé par N-075 : « Les détecteurs orientent l'audit sous un plancher : ils en changent la vitesse, non la validité. » ; « Candidat : attestation en service d'une sonde par perturbations secrètes sur un rejeu. »
- **§ 9**, quatre lignes après les seuils stochastiques : « **Audit après coup** : tirage après la fin de l'épisode, jugement sur une copie, hors ligne. » ; « **Plancher indépendant du score** : probabilité d'audit connue, jamais nulle, consignée ; le soupçon la monte, jamais ne la descend sous le plancher. » ; « **Part selon l'enjeu**, fixé par le défenseur avant l'épisode. » ; « **Aucun retour à l'agent** : aucune lecture ni aucun verdict ne lui revient — actif par défaut, ablaté dans l'expérience de la riposte (E3.4) ; lettre en attente de la décision sur les corrections tirées au hasard. » Et, en tête de section : « Les secrets du harnais (lecture de sonde, pièce d'audit) sont éprouvés par un devin avant toute course qui s'y appuie. »
- **§ 9**, l. 170, ajout : « mesurée par le rappel retrouvé en fonction du nombre d'épisodes endommagés audités, canal de retour fermé ; sous réserve de l'invariant de l'oracle. »
- **§ 10**, phase 1 : « Bras rapporté "référence honnête" ; prévision scellée avant la porte : le rappel d'une statistique étalonnée sur m épisodes honnêtes cesse de croître au-delà d'un horizon de l'ordre de m ; celui du rang contre le jumeau continue. »
- **§ 15**, deux questions de plus : « l'attestation en service d'une sonde » ; « la sonde de surprise est-elle un second instrument ? ».

## 13. Points que cette note ne tranche pas, renvoyés à Lazar

1. **La ligne « aucun retour à l'agent », ou les trois lignes de la note « asymétries » (D-2).** Enjeu : sous la lettre accordée, corriger avant l'alarme est interdit ou viole l'invariant. (a) Les trois lignes (seul le tirage au hasard corrige ; un audit sans trouvaille ne laisse aucune trace ; en régime de signature, on alarme, on ne corrige pas) : avantage, le levier « corriger » reste entier et le seul vrai secret est gardé ; inconvénient, le soupçon ne corrige plus rien de visible. (b) La lettre accordée : avantage, plus simple à garder par le code ; inconvénient, elle retire la correction avant l'alarme. Recommandation : (a). Confiance 0,7. Nœud : pas de défaut ; d'ici là, la lettre accordée s'applique.
2. **La ligne « aucun retour » et l'expérience de la riposte.** Enjeu : « toujours active », elle supprime l'objet de l'hypothèse sur la riposte et la fuite (H7). (a) Active par défaut, ablatée dans cette expérience : avantage, le programme reste cohérent ; inconvénient, un invariant qui s'ablate. (b) Toujours active : la politique « visible immédiate » sort du plan, ce qui modifie une expérience. Recommandation : (a). Confiance 0,8. C'est ma lecture, non un mot de Lazar : à confirmer.
3. **La boucle de réapprentissage et l'invariant de l'oracle** (N-060 v3, point 4 ; N-075, § 11, points 2 et 9). Enjeu : réapprendre une sonde sur des verdicts de l'oracle est une sortie de l'oracle dans la sélection d'un moniteur. (a) Permettre le réapprentissage sous cloison : un flux d'épisodes propre à la boucle, jamais ceux qui servent à un verdict du même moniteur, jamais le mode tenu à l'écart, verdicts par épisode fermés aux concepteurs de moniteurs ; avantage, la boucle se mesure ; inconvénient, un invariant reçoit une exception écrite. (b) Garder l'invariant entier : la boucle ne vit que sur mondes plantés. Recommandation : (a), par un texte à part contre-lu. Confiance 0,6. Nœud : pas de défaut ; d'ici là, (b).
4. **Porter la règle d'horizon dans l'énoncé de H2.** Enjeu : « un rappel qui croît avec l'horizon » n'est vrai, sous référence fixe, que jusqu'à un horizon de l'ordre de m. (a) Ne pas toucher l'énoncé, déclarer m et n au préenregistrement de la porte, et décider après la lecture de la prévision scellée : avantage, aucune hypothèse modifiée sur un calcul d'illustration ; inconvénient, l'énoncé promet plus que la loi ne permet. (b) Ajouter la clause maintenant. Recommandation : (a). Confiance 0,7. Modification d'hypothèse : nœud, pas de défaut.
5. **Le rôle 3 de l'organisme (N-065), seconde moitié** : réserver la famille « qui trompe le juge » comme famille tenue à l'écart. Non tranché par « à faire ». Recommandation : attendre la spécification du banc et ses trois témoins. Confiance 0,6. Nœud.
6. **Le plancher est dit « occupé » par le lecteur des douze voisins** ([verdict, 6], par « Blindfold »). N-075, § 2, écrivait que son écriture comme borne chiffrée « pourrait être revendiquée, sous le verdict d'antériorité » : le verdict rendu répond non. Conséquence proposée : le plancher est une base nommée et citée, jamais une revendication ; à porter par erratum de N-075 ou à sa prochaine version. Le verdict n'est pas contre-lu. À confirmer.
7. **Où sceller la prévision du point 1.** (a) Texte à part de classe A, hors critère de la porte : avantage, elle peut mourir sans toucher la porte ; inconvénient, une pièce décisive de plus. (b) Dans le préenregistrement de la porte, comme prédiction rapportée. Recommandation : (a). Confiance 0,65. Défaut sous 48 heures : (a), l'écriture seule.
8. **L'ordre des premiers pas, et les trois chantiers actifs.** Cette note n'en ouvre aucun. Ordre proposé, tout à 0 USD : les deux devins (ils disent si nos secrets en sont) ; la table du seuil et l'étiquetage des familles ; les mondes plantés de la loi de la référence honnête et sa prévision ; la question préalable sur la sonde de surprise ; la spécification du banc à vérité plantée ; le test de permutation ; la boucle sur mondes plantés ; l'attestation, écriture seule. Savoir lesquels se rangent sous un chantier actif revient à Lazar. Confiance 0,55.
9. **Le plancher comme invariant de la section 9.** N-075 l'inscrivait « là où un texte écrit le plancher » ; D-3 en fait une ligne de la section 9. Ma lecture : il vaut pour tout texte à venir qui emploie un audit, et ne rend non conforme aucun texte scellé. À confirmer.

## 14. Ligne proposée pour `CLAUDE.md`

À ajouter à la fin de la liste « Décisions de Lazar », par la mère, après la vérification des corrections :

> N-076 (GO-2026-11-21-57) : loi de la référence honnête — toute accumulation déclare m, n et la source de sa validité, horizon au plus m sauf nul par acte, prévision scellée avant G1 ; hasard du défenseur comme preuve et banc à vérité plantée, à faire ; attestation en service, candidate ; audit après coup, à plancher et à l'enjeu, boucle audit-recapture-réapprentissage, épreuves du devin, à faire ; table du seuil au taux d'audit ; quatre invariants d'audit au § 9 ; les scores orientent l'audit ; rien revendiqué (`docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md`).

Longueur : 597 signes (plafond de 600, mesurée par programme). Elle perd, faute de place, « aucun critère de porte ni énoncé d'hypothèse changé », « la question préalable sur la sonde de surprise » et les points renvoyés à Lazar, qui restent dans la décision (en-tête ; sections 10 et 13).

## Relevé de méthode

Selon `docs/procedures/consigne-commune-methode-de-recherche-v1.md` (`d327b3fcbee59f37f833e83812a66ba8b28af72cdd5475772870612a2c9d23d8`).

**Chaîne de raisonnement.**
1. Lazar a accordé neuf points (`registres/go.md`, ligne `GO-2026-11-21-57`, recopiée en section 0).
2. Les neuf points viennent de quatre notes du concepteur et d'une contre-lecture (en-tête, « Sources »), dont j'ai vérifié les empreintes contre leurs compagnons.
3. Le programme porte une hypothèse (c) sur la variance honnête (l. 55), un rappel qui croît avec l'horizon (l. 94), un budget d'audit (l. 72), sept invariants (l. 164-170) et des contrôles croisés (l. 136) (`2fd63bad…`, lu en entier) : chaque point s'y loge sans changer un énoncé.
4. Référence fixe : la part cachée vaut z × √(1/n + 1/m) / μ et tend vers z / (μ √m). Rejoué : `python3 -c "import math;z=2.3263;print([round(z*math.sqrt(1/n+1/400)/0.5,4) for n in (100,10**4,10**6)])"` rend `[0.5202, 0.2372, 0.2327]`, égal au bloc A (`d43e62bc…`).
5. Témoins à taux p : facteur √(1 + 1/p), 10,05 à p = 0,01. Rejoué : `python3 -c "import math;print(round(math.sqrt(1+1/0.01),2))"`.
6. Table du seuil : `python3 -c "print([round(1-0.05**(1/K),4) for K in (30,100,300,1000)])"` rend `[0.095, 0.0295, 0.0099, 0.003]`.
7. Supposé : le plancher valable pour tout test (7,7 %), le nul par acte en racine nue, le délai de l'oracle (26 %), la racine du régime d'excès : repris des blocs de calcul des notes, non rejoués, non contre-lus.
8. Les verdicts d'antériorité (`973bd0dd…`, § 3 ; `74d44e6f…`, § 2) disent le plancher occupé et huit candidats partiellement occupés : d'où chaque rubrique « pourrait être revendiqué ».
9. Rudoler et al. n'est pas parmi les douze voisins lus (`973bd0dd…`, § 1 et 2) et la note « asymétries » le dit occupant (`fa29b32d…`, l. 51 et 68) : d'où la réserve du § 6.2.
10. L'invariant de l'oracle (`docs/decisions/decision-N-060-v3.md`, `2b448f69…`, point 4) interdit toute sortie de l'oracle dans la sélection d'un moniteur ; la boucle réapprend une sonde sur de telles sorties : d'où le heurt du § 6.2.
11. Le programme compare une riposte « visible immédiate » (l. 214) et ablate déjà un invariant dans cette expérience (l. 168) : d'où la lecture « active par défaut, ablatée » de la ligne 4.
12. La note « asymétries » précise la ligne 4 après coup (son verdict, point 5 ; D-2) et `GO-2026-11-21-56` laisse D-2 à Lazar : d'où l'écart signalé, non tranché.
13. Supposé : aucun texte scellé du dépôt n'écrit déjà un audit conforme aux quatre lignes, ni une accumulation dont l'horizon dépasse sa référence ; je n'ai ouvert aucun préenregistrement au-delà de l'en-tête et de quelques lignes de l'accumulation du barreau 6 et du brouillon v7 du bras « papier dopamine ».
14. Supposé : les pages citées [PDF, p.] disent ce que les notes et les deux lectures en rapportent ; je n'ai rouvert aucun PDF.

**Objets de contrôle.** Ce sont les contrôles d'arguments, non de mesures ; rien n'a été scellé avant. *La loi de la référence honnête* : objet où « la part cachée cesse de baisser » est fausse, la référence exacte : attendu, une part qui tombe comme l'inverse de la racine de n ; rendu par le bloc A : 46,53 % à n = 100, 0,47 % à n = 1 000 000 ; objet où elle est vraie, m = 400 fixe : attendu, un palier vers 23,3 % ; rendu et rejoué : 23,27 % à n = 1 000 000 (pas 4). *La table du seuil* : objet où « un taux d'audit suffit » est faux, le régime d'excès : attendu, aucun seuil fixe ; la note et son erratum le disent, non rejoué ; objet vrai, le régime de signature à K = 300 : attendu 1,0 %, rendu 0,99 % (pas 6). *Le devin* : objet où il doit réussir, un harnais où le soupçon règle des corrections visibles ; objet où il doit rester au hasard, un harnais où seul le plancher corrige (note « asymétries », 2.2) : **non exécuté**. *L'audit orienté* : objet où le gain doit disparaître, un agent qui abaisse son score jusqu'au plancher : **non exécuté**, écrit comme test de mort. *La ligne proposée pour `CLAUDE.md`* : attendu, 600 signes au plus ; rendu, 597 (un premier jet en faisait 624 et a été raccourci).

**Premier pas non justifié.** Le pas 13. Ce qui le justifierait : l'inventaire par étiquettes des textes scellés, par un agent habilité. Le pas 7 est le second : une contre-lecture des quatre blocs de calcul ; le pas 14, le troisième.

**Mode d'échec affecté.** Sans objet : pièce d'auteur, non de relecteur.

**Dérivation de l'énoncé seul.** Sans objet : pièce d'auteur, non d'agent de re-dérivation.

**Trouvaille de côté.** (1) Rudoler et al. manque à la lecture des douze voisins et resserre le reste de la boucle (pas 9). (2) La ligne « aucun retour à l'agent », lue « toujours active », retirerait son objet à l'expérience de la riposte (pas 11). (3) La phrase accordée du protocole ne nomme que le nul par acte, alors que la note a un troisième régime, les témoins à taux p, où l'horizon dépasse toujours m sans dommage : précisé en section 2, à contre-lire. (4) En relisant l'énoncé retenu de H2 dans N-007, j'ai vu en passant une ligne qui rapporte un chiffre de simulation ; je ne l'ai ni retenue ni reprise.

**Évaluateur et conseil.** Ce qui juge cette pièce : le contre-lecteur Opus 5.5, puis Lazar ; aucun juge admis sur témoins. Par où elle pourrait être bien jugée sans le mériter : elle ne revendique rien, ce qui se lit comme de la prudence, alors que ses appuis sont quatre notes non contre-lues, dont je suis l'auteur, et deux verdicts non contre-lus ; ses numéros de ligne du programme sont justes, ce qui ne dit rien de la justesse des lectures ; elle déplace les difficultés en section 13 au lieu de les résoudre. Conseil au contre-lecteur : les modes « énoncé infidèle » (la section 0 contre la ligne du GO ; chaque « inchangé » contre la décision citée ; la lecture du protocole contre sa phrase), « garantie qui suppose ce qu'elle prouve » (le secret de la pièce d'audit, le canal fermé, la référence exogène) et « antériorité » (les points 1 à 3, sans verdict ; Rudoler et al.).

## Ce que je n'ai pas fait

- Aucun PDF rouvert ; aucune recherche d'antériorité nouvelle ; aucun bloc de calcul des notes rejoué au-delà des trois commandes des pas 4 à 6.
- Aucun préenregistrement lu en entier, aucun verdict, aucun résultat d'expérience. « Aucun texte scellé touché » repose sur le fait que cette note ne change aucun critère ni aucun énoncé, et sur le pas 13.
- Non ouverts : les dossiers et branches interdits par le mandat ; la ligne R-2059 ; les réponses des collisionneurs ; la note sur la pince et la note sur l'adjudant, connues par N-075 ; N-004, N-013, N-015, N-044, N-049, N-054, N-062, N-064, N-067 et N-069, cités d'après `CLAUDE.md` ou d'après N-075 ; la re-dérivation de la règle « moniteur invalide », connue par l'erratum 1.
- Je n'ai pas vérifié que la différence de deux lectures de réussite attendue figure sur la liste approuvée des sondes et des lots lisibles, ni que les continuations de la question préalable tiennent dans la ligne de calcul accordée.
- `CLAUDE.md`, le programme, les registres et N-075 ne sont pas modifiés. Routine de reprise : les empreintes de lancement sont conformes (`sha256sum -c`) ; le reste revient à la mère.
