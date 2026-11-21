# Proposition B : Tour III.3, réponse aux critiques

**Pièces.** Les blocs FAITS, QUESTION, ma conception III.1 et les critiques A, C, D et E sont présents. Chacun va jusqu'à sa ligne de fin, sans coupure visible. Je n'ai pas vérifié les empreintes sha256. La critique D n'a pas d'en-tête d'intégrité, ce qui ne bloque rien.

**Statuts.** Je garde ma convention du tour III.1 : les énoncés de FAITS sont cités comme **RAPPORTÉ**, et mes propositions sont des **HYPOTHÈSES**. Mes calculs sont des identités sous un modèle que je pose ; ce modèle est une HYPOTHÈSE, et ses entrées numériques sont illustratives. C et E étiquettent **[VÉRIFIÉ]** certaines de leurs dérivations. Je ne change pas leurs étiquettes, mais je ne les reprends pas à mon compte.

---

## (a) Réponse à chaque critique visant B

| # | Critique (source) | Verdict | Raison ou test |
|---|---|---|---|
| K1 | E1 confond le type de collision et l'accès au texte. Les collisions de traduction vivent hors arXiv ou derrière un mur payant (A ; formalisé par E). | **Transformée en test** | J'enregistre l'indicateur d'accès pour chaque appât. J'ajoute une cellule où le texte intégral est fourni à l'agent. Voir E1′. |
| K2 | E1 mesure la mémoire, pas la recherche, car les appâts publiés sont dans les corpus d'entraînement (A). | **Transformée en test** | J'ajoute un bras « livre fermé ». Je ne connais pas les dates de coupure des modèles, donc je ne promets pas d'appâts postérieurs à la coupure. |
| K3 | L'étiquette « quasi-jumeau non trouvé » est fragile. Une vraie collision inconnue de l'étalon y compte comme fausse alerte, avec un biais η(r − f) qui croît avec le rappel (A, C, D, E). | **Transformée** | J'adopte la définition locale de D, que A reprend : le négatif signifie « *ce parent* ne règle pas *ce jumeau* », jamais « neuf ». Le fait que le parent n'implique pas le jumeau est établi par un contre-exemple. Sans contre-exemple, le jumeau est exclu du banc. Une alerte qui pointe vers un *autre* document est adjugée à part, et reclassée en positif si l'implication est confirmée. |
| K4 | Le même expert rédige les déguisements, choisit les quasi-jumeaux et décide de leur statut, ce qui crée un indice de surface. Le lexique qui sert à construire les appâts alimente aussi les reformulations de l'agent (D, C, E). | **Acceptée et testée** | Rédacteurs séparés. L'agent ne reçoit aucun lexique issu des rédacteurs. Contrôle : un classifieur de surface ne doit pas séparer les appâts des jumeaux mieux que le hasard. **Rejet partiel** de la formule de C selon laquelle le rappel « ne reflète que » le recouvrement lexical : c'est une cause possible, que le bras sans lexique permet de mesurer. |
| K5 | Le seuil de 30 points n'est pas jugeable avec 5 à 10 appâts par type (A, C). | **Acceptée** | J'ai refait les calculs. L'écart-type de la différence vaut au plus √(1/(2n)), soit environ 0,22 pour n = 10. Le calcul de C donne environ 0,238. Entrées illustratives dans les deux cas. Je remplace le duel sur l'écart par un test unilatéral contre un plancher absolu (E1′). |
| K6 | Une borne sur l'écart relatif valide un instrument uniformément faible (E, D : si r_L = r_T = f). | **Acceptée** | Trois exigences remplacent l'écart : un plancher absolu, la discrimination r − f, et une performance au-dessus de la ligne de base mécanique. |
| K7 | E1 n'identifie ni la répartition des types P(type \| collision) ni le rappel sous P_dépl (D ; constat transversal de A). | **Acceptée, avec correction de mon tour III.1** | J'avais écrit qu'E1 réfutait l'hypothèse (i), « les collisions chères sont surtout non littérales ». C'est faux : la composition du banc est choisie par son constructeur. Seul l'audit E5 touche cette hypothèse. |
| K8 | Un résultat publié et réécrit n'est pas du folklore (D). | **Acceptée** | La strate « folklore » est retirée d'E1. Le folklore reste non mesuré par banc. |
| K9 | Une citation textuellement exacte peut soutenir l'énoncé inverse. Le contrôle par sous-chaîne est satisfait par construction (D, E). | **Acceptée et testée** | La présence du passage devient une condition nécessaire, plus suffisante. J'ajoute des appâts dont la citation est exacte mais où l'implication échoue (problème ouvert, hypothèse i.i.d.). |
| K10 | E2 est positif ou nul par construction : l'ordre est fixe, l'effort se cumule, et la cartographie peut hériter des synonymes de l'examen ciblé (A, C, D, E). | **Transformée** | Bras parallèles, à l'aveugle, sans partage de traces. J'ajoute un second examen ciblé indépendant, à budget égal. Test sur paires discordantes. Cartographie placebo. Voir E2′. |
| K11 | La règle « au moins une collision » est déclenchée par les seules fausses alertes : 1 − (1 − ε)^K tend vers 1 (A, C, E). | **Acceptée** | Toute collision comptée est adjugée par une implication vérifiée, par quelqu'un qui n'a construit ni la cible ni le bras. |
| K12 | Une liste déjà proposée mesure des retraits, pas les bonnes cibles qu'une cartographie aurait fait proposer (D). | **Acceptée comme limite non réparée** | Je ne sais pas mesurer la valeur de la cartographie pour *choisir* à cette échelle. J'en tire une conséquence : la cartographie n'est plus obligatoire dans ma recommandation. |
| K13 | La H_B d'E3 fusionne « présent ou en PR » et « fermé automatiquement » (A). | **Acceptée** | E3′ a trois issues séparées. |
| K14 | « Non fermé » décrit le budget de temps t, pas le lemme (A). | **Acceptée** | Je rapporte une courbe de fermeture en fonction de t. |
| K15 | Les « lemmes renommés » d'E3 sont un contrôle positif (A, D, E). | **Acceptée** | Renommés en positifs. Vrais négatifs : des énoncés faux et des énoncés réfutés par un contre-modèle. |
| K16 | Un lemme présent sur un type isomorphe ne se ferme pas, et il est déclaré neuf à tort (C). | **Acceptée** | J'ajoute des positifs difficiles sur des types isomorphes. Leur rappel est rapporté à part. |
| K17 | Le rappel sur les PR publiques ne couvre pas les travaux en cours non publics (D). | **Acceptée comme limite** | Le verdict E3′ est daté et porte sur les dépôts publics seulement. |
| K18 | E4 est presque vrai par construction (pile sélectionnée parce que voisine), et son négatif hors pilier est trop lointain (A, D, E). | **Transformée** | H_A devient « règle une cible candidate ». Les négatifs sont appariés par thème. Voir E4′. |
| K19 | L'accord entre relecteurs n'estime pas r. Avec un relecteur par zone, la covariance n'est pas estimable. Le κ est instable quand p est faible (A, D, E). | **Rejet partiel et correction** | Rejet : je n'utilisais l'accord que comme condition nécessaire (« s'il est faible, l'étalon est en cause »). Correction acceptée : mon §4 disait « un par zone » et mon tableau (c) disait « deux », c'est incohérent. Je retiens deux relecteurs de communautés différentes. Pour chacun, je mesure la sensibilité sur des positifs semés et la spécificité sur des négatifs semés, sans κ comme critère. |
| K20 | Le juge est évalué sur les appâts qui ont servi à le régler (A). | **Acceptée** | Des familles entières de résultats sont réservées au test (procédé de D). |
| K21 | Le relecteur est évalué sur des appâts qu'il a lui-même construits (C). | **Acceptée** | Le relecteur évalué n'est jamais un constructeur du banc. |

**Ce que ces critiques changent dans ma position (HYPOTHÈSE).** Mon banc, comme ceux des autres selon A, estime le rappel sous la loi des collisions déjà découvertes. Ces collisions sont publiées, nommées et probablement mémorisées. Je fais l'hypothèse que ce biais est *optimiste* : le rappel sur banc dépasserait le rappel en déploiement. Si c'est vrai, le banc n'est informatif que dans une direction. Un échec sur banc rend l'agent insuffisant ; un succès sur banc n'établit rien pour le déploiement. Je réécris E1 pour qu'il ne serve que dans cette direction. L'hypothèse de monotonie du biais n'est pas établie. Le bras « livre fermé » la met partiellement à l'épreuve : il mesure la part de mémoire, mais ne dit rien des cas hors banc.

---

## (b) Expériences corrigées

Seuils et effectifs sont **illustratifs** ; ils seraient fixés avec l'arbitre avant toute levée d'aveugle. « Pas de verdict » est une issue déclarée, pas un échec caché.

### E1′ : l'agent est-il insuffisant, même sur des cas faciles ?

- **H_A** : le rappel de l'agent sur les collisions non littérales, texte intégral fourni, livre ouvert, atteint au moins un plancher ρ. En même temps, r − f > 0 et l'agent bat la ligne de base mécanique.
- **H_B** : le rappel est inférieur à ρ, ou r − f ≤ 0, ou l'agent ne bat pas la ligne de base.
- **Cellule minimale** (si le banc est petit) : appâts de traduction et de généralisation, texte fourni, en deux bras, livre ouvert et livre fermé. Cette cellule isole la compétence de lecture des deux confusions K1 et K2. Si le budget le permet, j'ajoute la cellule « texte non fourni », qui mesure le coût de l'accès.
- **Banc** : appâts rédigés par un expert X. Quasi-jumeaux pour lesquels un contre-exemple établit que le parent n'implique pas le jumeau. Appâts de citation hors implication (K9). Familles réservées (K20). Reformulations de l'agent produites sans lexique venant de X (K4).
- **Contrôles** :
  - classifieur de surface au hasard ;
  - énoncés fabriqués, pour lesquels aucune alerte n'est attendue ;
  - alertes pointant vers un autre document, adjugées et rapportées à part (K3).
- **Décision** :
  - Borne unilatérale supérieure du rappel sous ρ : H_A est falsifiée. Option (a) « par un agent » écartée comme protection.
  - Borne inférieure au-dessus de ρ, et r − f significativement positif : H_B est falsifiée. Cela établit seulement que l'agent n'échoue pas sur des cas faciles, rien sur le déploiement.
  - Sinon : pas de verdict.
- **Jugeabilité** (modèle binomial, HYPOTHÈSE). Avec 0 détection sur n, la borne unilatérale à 95 % vaut 1 − 0,05^(1/n). Elle vaut environ 0,26 pour n = 10 (illustratif). Un agent très mauvais peut donc être écarté avec un petit banc. Établir H_A demande un banc nettement plus grand. Je ne sais pas si ce banc est finançable.
- **Livre fermé.** Si ce bras atteint un rappel proche du bras ouvert, la détection vient de la mémoire. Dans ce cas, même la falsification de H_B ne dit rien des travaux de 2026.

### E2′ : la cartographie protège-t-elle mieux qu'une seconde recherche ciblée ?

- **H_A** : à budget égal, la cartographie (ii) détecte plus souvent que le second examen ciblé indépendant (i′) des collisions que l'autre manque, au-delà d'une marge δ fixée d'avance.
- **H_B** : l'asymétrie des paires discordantes (ii) contre (i′) ne dépasse pas δ.
- **Matériel** : deux zones à fort risque de traduction. La liste des candidates est enrichie de collisions *semées*, construites par un expert qui n'opère aucun bras. Les semées sont mêlées aux candidates réelles, sans marque.
- **Bras** : (i), (i′) et (ii), en parallèle, à l'aveugle, sans partage de traces (K10).
- **Comptage** : test sur paires discordantes (type McNemar). Seules les collisions adjugées par implication vérifiée sont comptées (K11).
- **Contrôles** : cartographie placebo d'une zone sans rapport, qui ne doit écarter aucune cible après adjudication. Cibles connues comme ouvertes par l'expert, qui ne doivent pas être écartées.
- **Décision** :
  - Intervalle de l'asymétrie au-dessus de δ : H_B est falsifiée. Cartographie justifiée *pour protéger* dans ces zones.
  - Intervalle sous δ, avec une marge d'équivalence fixée : H_A est falsifiée.
  - Sinon, pas de verdict. C'est l'issue probable avec peu de paires discordantes, et je le dis d'avance.
- **Limites** : les semées viennent encore d'une loi de banc (K7). La fonction *choisir* n'est pas mesurée (K12).

### E3′ : un lemme candidat est-il payant comme lemme ?

- **H_A** : absent des dépôts et des PR publiques à la date d, et non fermé au budget maximal t_max.
- **H_B**, avec trois issues rapportées séparément (K13) :
  - (H_B1) présent ou en PR : collision de bibliothèque ;
  - (H_B2) fermé à un budget t ≤ t_max : pas payant comme lemme ;
  - (H_B3) présent sur un type isomorphe, trouvé par la recherche formelle ou un mainteneur.
- **Instrument validé avant usage** :
  - Positifs : lemmes renommés, positifs sur type isomorphe (K16), PR connues. Rappel rapporté par classe.
  - Négatifs : énoncés faux, et énoncés réfutés par un contre-modèle (K15). Toute alerte sur ces négatifs falsifie la spécificité de l'instrument.
- **Sortie** : courbe de fermeture sur trois budgets (K14) ; verdict daté, limité aux dépôts publics (K17).
- **Décision** : l'une des issues H_B falsifie H_A pour ce lemme. L'absence robuste, avec un instrument validé, falsifie H_B *pour les dépôts publics à la date d* seulement.

### E4′ : un travail de 2026 déjà croisé règle-t-il une cible candidate ?

- **H_A** : au moins un travail croisé implique, réfute ou rend corollaire une cible candidate. Le passage est cité, et l'implication est adjugée par un lecteur qui n'a pas construit la cible.
- **H_B** : aucun ne le fait.
- **Contrôles négatifs appariés par thème** (K18) :
  - un article de 2026 de la même zone, hors de la pile (procédé de A) ;
  - des voisins partageant le lexique sans recoupement logique (procédé de E) ;
  - une citation exacte avec une hypothèse incompatible (procédé de D).
  
  Aucun ne doit être adjugé comme collision.
- **Décision** :
  - H_A retenue : la cible est retirée ou reformulée avant dépense. H_B est falsifiée. Il est alors établi qu'au moins une dépense aurait été engagée sur une cible déjà réglée sous l'option (b).
  - Aucune collision : H_A est falsifiée *pour cette pile*.
- **Ce qu'E4′ ne dit pas** : la pile est sélectionnée, donc ce résultat ne renseigne pas le taux de collision des candidates (argument de D).

### E5 (nouvelle) : audit de référence sur un échantillon de candidates

Cette expérience répond à la critique K7 et au constat de A sur P_dépl.

- **Échantillon** : candidates tirées avec une probabilité connue, y compris les abandonnées et les non revendiquées (contrôle que D exige contre E, et que j'applique ici). Si la liste est petite, on les audite toutes.
- **Auditeurs** : deux, de communautés différentes, avec un protocole préenregistré.
- **H_A** : le taux de collision p est au moins égal à un seuil s fixé par le programme.
- **H_B** : p < s.
- **Décision** :
  - Si l'adjudication ne produit pas de faux positifs (HYPOTHÈSE), le taux adjugé minore p. Une borne inférieure au-dessus de s falsifie donc H_B, et l'option (b) ne protège pas la dépense.
  - Une borne supérieure sous s falsifie seulement la conjonction « p ≥ s *et* rappel de l'audit élevé ». Le rappel de l'audit est inconnu, et je ne le cache pas.
- **Sous-produit** : le type de chaque collision adjugée. C'est la seule donnée de mon dispositif qui touche l'hypothèse (i). Le biais va contre les collisions non littérales, plus difficiles à trouver : une majorité non littérale observée serait donc robuste ; une majorité littérale ne le serait pas.

---

## (c) Réponse à la question de l'arbitre

**Ce qui est établi**, à partir des faits RAPPORTÉS et sans aucune mesure :

1. Les cibles sont à budget égal et toutes rapportées (RAPPORTÉ). Si la dépense s'engage au scellement (HYPOTHÈSE), le budget d'une cible déjà réglée est perdu *avant* toute revendication. L'option (b) protège la revendication, pas la dépense. J'emprunte cet argument à la critique de A contre C et je l'applique à (b).
2. Une bibliothèque Lean publique couvre une part du vocabulaire (RAPPORTÉ). Pour la forme « lemme », un contrôle mécanique est donc possible avant la dépense. Sa fiabilité n'est pas mesurée.
3. Des travaux de 2026 voisins existent et n'ont pas été lus. La veille est gelée (RAPPORTÉ).

**Ce qui n'est pas établi** :

- le taux de collision des candidates ;
- le rappel de *tout* instrument, par type de collision, y compris le lecteur humain ;
- la répartition des types de collision ;
- les coûts relatifs d'une lecture et d'une collision ;
- l'état de la liste, scellée ou non ;
- l'étendue du gel, notamment s'il couvre la recherche dans les bibliothèques formelles ;
- la taille de la pile de 2026.

Je ne sais rien de tout cela. Il y a plus. D'après les critiques reçues, qui visent toutes les propositions et dont je ne vois pas de réfutation, aucune expérience pilote proposée n'estimera à court terme, avec puissance, ni ce taux ni le rappel en déploiement : événements rares, petites listes, bancs biaisés vers les cas faciles. Mon jugement (HYPOTHÈSE) est donc que le choix ne peut pas reposer sur une estimation. Il doit reposer sur des actions peu chères, qui protègent dans tous les scénarios plausibles, et sur des tests qui peuvent *écarter* une option.

**Recommandation : option (d) corr