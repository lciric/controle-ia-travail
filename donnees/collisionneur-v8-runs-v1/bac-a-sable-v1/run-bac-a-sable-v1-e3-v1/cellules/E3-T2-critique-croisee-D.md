Repère commun d’analyse : pour un signal \(S\), je note \(TD=P(S=1\mid D)\) et \(FA=P(S=1\mid H)\), où \(D\) et \(H\) sont les **lois cibles** des artefacts défectueux et honnêtes, non deux corpus fabriqués à part. Si \(P(S\mid D)=P(S\mid H)\), aucun seuil sur \(S\) ne discrimine. Zéro événement sur \(n\) cas indépendants ne donne pas une probabilité nulle, mais seulement la borne supérieure de Clopper–Pearson \(1-\gamma^{1/n}\). Enfin, un intervalle d’incertitude qui traverse le seuil gelé rend la décision « non tranchée », pas favorable à une hypothèse.

## Sur la proposition A

**(a) Défauts de méthode**

- **E1 établit la portabilité, pas la validité.** Un script constant, stable et scientifiquement faux est reproduit avec ses mêmes empreintes. Le second hôte change simultanément image, bibliothèques et environnement d’exécution : une divergence ne peut être attribuée au seul non-déterminisme. L’écart entre les exigences sur `RESULTAT:` et sur les fichiers laisse aussi indéfini ce que « reproduction exacte » signifie.
- **E2 ne mesure pas spécifiquement la circularité.** Les bras diffèrent par le matériau servi, mais aussi par les trajectoires adaptatives qu’il induit. L’augmentation de « survit » peut venir du renouvellement des fiches encore actives, sans amélioration à fiche constante. La conjonction survie/reproduction/canaris est un critère composite : une adaptation bénigne et une fraude peuvent produire des trajectoires différentes mais également une survie accrue seule.
- **E3 et E4 contiennent des détections vraies par construction.** Les contrôles de E3 reçoivent précisément des comportements susceptibles de toucher les canaris ; ceux de E4 sont choisis parce qu’ils dépendent de l’implémentation. Retirer un canari après échec sur le corpus honnête, puis réévaluer sur ce même corpus, constitue une fuite calibration–évaluation.
- **E4 conditionne en outre la redondance à la reproduction E1** : sa population estimée est seulement celle des artefacts déjà reproductibles. Le second bac varie avec l’image ou le noyau. Dans **E5**, « le journal explique une divergence » n’a ni étiquette ni estimateur reproductible. Le contrôle `print(RESULTAT:…)` ne teste qu’un journal minimal.

**(b) Lois sous lesquelles les critères perdent leur pouvoir**

- **E1.** Soit \(r_H=P(Y_1=Y_2\mid H)\). Si \(r_H\) est inférieur au seuil, ou si son estimateur a un intervalle couvrant ce seuil, le critère est non jugeable. Si, pour une fraude déterministe \(M\), la loi de \((Y_1,Y_2,\text{empreintes})\) est identique à celle des honnêtes, la puissance contre \(M\) est nulle. La sélection de la dernière exécution réussie modifie en outre la loi conditionnelle estimée.
- **E2.** Si l’information transmise par le canal vérifie \(I(M;V)=0\), ou si le coefficient de sélection exercé sur les générations est nul, la différence d’effet attendue est nulle sans que la circularité structurelle soit réfutée. Avec dépendance sérielle, la variance entre bras placebo ne représente pas la variance des trajectoires adaptatives ; elle sous-estime alors l’incertitude. Des taux proches des bornes rendent également le seuil en écarts-types normal inadéquat.
- **E3.** Zéro touche honnête ne démontre pas \(FA=0\). Si la loi des imports, bibliothèques ou dépendances change entre calibration et production, \(FA\) change sans modification du canari. Une sensibilité agrégée est dominée par les contrôles faciles ; sur la loi cible, les sondages peuvent avoir leur masse hors du support couvert.
- **E4.** Si une cause commune produit la même sortie fausse dans les deux bacs, l’accord est indépendant de la correction. Le désaccord ne discrimine plus lorsque \(P(\Delta\neq0\mid H)\simeq P(\Delta\neq0\mid D)\). Conditionner à E1 modifie ces deux lois et interdit l’extrapolation au corpus initial.
- **E5.** Sans probabilité estimée de couverture du journal, \(P(\text{événement observé}\mid\text{événement survenu})\), la détection est non identifiable. Les exécutions répétées d’un même script ne fournissent pas des unités indépendantes.

**(c) Contrôles négatifs indispensables**

- Un **faux résultat stable et reproductible**, rejoué sur les deux hôtes : son accord ne doit jamais être compté comme validité.
- Des comparaisons appariées **même environnement/changement d’environnement**, pour séparer stochasticité et portabilité.
- Pour E2, un **canal placebo de même débit et même calendrier**, mais sans information de verdict, avec randomisation au niveau de la fiche ou du producteur.
- Pour E3/E4, des cas réservés de découverte bénigne, des sondes positives non calibrées sur les chemins exacts des canaris, et un **défaut commun aux deux bacs** que l’accord doit échouer à détecter.
- Pour E5, une perte de journal et une lecture supplémentaire connues, ainsi qu’un appariement dossier vierge/dossier prérempli.

## Sur la proposition B

**(a) Défauts de méthode**

- **L’expérience 1 confond faux positif statistique et tromperie du vérificateur.** Sous hypothèse nulle, un test correctement calibré produit encore des rejets. Exiger que les contrôles dont l’effet est planté à une puissance non démontrée passent tous favorise les procédures libérales et aggrave précisément le faux positif étudié.
- **L’expérience 2 confond environnement et étiquette.** Production et test peuvent différer par charge, date, image, données ou configuration. Un classifieur performant peut apprendre ces covariables sans démontrer une fuite attribuable au bac. Aucun partage des coupures apprentissage/évaluation par session ou environnement n’est spécifié.
- **Les expériences 3 et 4 utilisent des corpus non appariés.** Les scripts adversariaux sont construits avec des lectures dépendantes de la plateforme ; les honnêtes avec du calcul numérique. Leurs divergences respectives ne mesurent donc pas une propriété générale de la redondance ou des canaris.
- **L’instrument de hachage comporte une impasse structurelle.** Si l’empreinte attendue vient du producteur, modifier artefact et empreinte ensemble est indétectable par construction. Si elle est fixée extérieurement, le hachage vérifie l’intégrité, toujours pas la validité scientifique. Les substitutions plantées dans le journal testent surtout ce que le collecteur sait déjà voir.

**(b) Lois sous lesquelles les critères perdent leur pouvoir**

- **Expérience 1.** Pour un test valide de taille \(\alpha>0\), \(P(\text{au moins un rejet sous }H_0)>0\) et croît avec le nombre de fiches. Un seul faux positif ne falsifie donc pas la séparation structurelle. Après \(k\) choix adaptatifs, la probabilité de rejet dépend de la loi jointe des \(k\) analyses, non de \(\alpha\) seul. La borne après zéro événement suppose des unités indépendantes et une probabilité commune.
- **Expérience 2.** Si \(P(X\mid production)=P(X\mid test)\), la précision de Bayes est celle du hasard. Si les lois diffèrent seulement par une covariable \(Z\), la performance est prédictive de \(Z\), pas d’une fuite causale. Des observations groupées réduisent la taille effective ; les deux seuils de performance laissent en outre une zone où aucune hypothèse n’est falsifiée.
- **Expérience 3.** Un défaut commun déterministe donne une divergence nulle sur \(D\). Des divergences honnêtes et adversariales proches rendent le rapport de vraisemblance voisin de un ; les taux estimés sur deux corpus séparés ne suffisent pas à conclure.
- **Expérience 4.** Même avec une faible probabilité \(p\) d’accident honnête par exécution, la probabilité d’au moins une élimination sur \(m\) exécutions peut devenir élevée. La sensibilité chute si la loi cible du sondage se concentre hors des canaris couverts.
- **Instruments.** Avec référence de hachage contrôlée par la source, \(P(\text{acceptation}\mid\text{altération coordonnée})=1\). Pour le journal, une probabilité de perte non nulle borne directement la détection. Compter des « classes couvertes » n’estime aucune de ces probabilités.

**(c) Contrôles négatifs indispensables**

- Pour l’expérience 1 : des scripts fixes sans agent adaptatif, des tests dont la taille sous \(H_0\) est connue, et des effets positifs de puissances variées, sans exigence de réussite systématique.
- Pour l’expérience 2 : **deux environnements identiques arbitrairement réétiquetés**, permutation des étiquettes, et évaluation sur sessions entièrement réservées.
- Pour la redondance : répétition du même moteur sur scripts stochastiques, défaut sémantique commun, et différences de plateforme bénignes.
- Pour les canaris et journaux : découverte légitime de ressources, exécutions honnêtes avec processus secondaires, journal volontairement tronqué et accès positif connu. Sans ceux-ci, détection et fausses alertes sont seulement des propriétés du banc fabriqué.

## Sur la proposition C

**(a) Défauts de méthode**

- **La contre-épreuve par permutation ne teste pas nécessairement la fraude.** Elle suppose que la permutation conserve le plan expérimental et produit la bonne loi nulle. La lecture `openat`/`read` mesure un accès, pas une dépendance causale du résultat aux données. Les politiques constantes sont détectées par invariance précisément parce qu’elles ont été construites constantes.
- **L’expérience 1 calibre et évalue sur des populations trop proches.** La liste blanche d’initialisation ne couvre pas nécessairement les imports réels. Les sondes positives connaissent les familles de chemins recherchées ; les canaris inaccessibles ou absents donnent aussi des fausses alertes nulles par construction.
- **L’expérience 3 annonce un blocage des sondes sans métrique correspondante.** Son contrôle `bwrap` contre `bwrap` suppose une variance intra-bac nulle au lieu de la mesurer. La tolérance numérique et l’accord de verdict ne sont pas interchangeables : un écart minuscule peut franchir le seuil gelé.
- **Le ratio de fichiers ouverts est diluable** par de nombreux accès bénins. Le critère d’injection dans `stdout` est largement vrai par construction lorsque R4 transforme déjà tout désaccord en « non concluant ».

**(b) Lois sous lesquelles les critères perdent leur pouvoir**

- **Permutation.** Si \(P(D^\pi)\) diffère de la loi nulle préservant le plan, le rejet d’un honnête mesure une rupture de distribution, non une fraude. Sous une loi nulle valide de taille \(\alpha\), exiger aucun franchissement sur tranche permutée est incompatible avec le fonctionnement du test ; plusieurs permutations augmentent encore la probabilité d’au moins un rejet.
- Si une politique exploite une information non permutée dont la loi de sortie coïncide avec celle des honnêtes sur le couple \((R(D),R(D^\pi))\), la double exécution a une puissance nulle. L’indicateur de lecture reste indépendant de l’usage causal des octets.
- **Canaris.** Zéro fausse alerte sur le petit corpus conserve une borne supérieure non nulle. Si la loi cible des sondages évite le support des canaris, la sensibilité cible est faible même lorsque la sensibilité du banc est élevée. Toute dérive de la loi des imports modifie \(FA\).
- **Redondance.** Soit \(M=|R-\tau|\), distance au seuil. Lorsque \(P(M<\epsilon)\) est élevé, de petites fluctuations produisent des verdicts discordants malgré une concordance numérique. Une erreur commune laisse au contraire l’accord élevé. Un ratio de durées totales est instable sous des lois de temps à queue lourde.
- Les exigences de détection parfaite ou de fausse alerte nulle sont non jugeables lorsque les intervalles associés aux comptes finis couvrent ces exigences.

**(c) Contrôles négatifs indispensables**

- Des permutations **préservant blocs, dépendances et taille d’échantillon**, validées par des tests honnêtes dont le comportement sous nulle est connu ; corpus réservé après tout réglage.
- Des scripts honnêtes avec imports réels, découverte bénigne et processus secondaires ; des sondes positives indépendantes des chemins utilisés pour placer les canaris.
- Pour la redondance : répétitions stochastiques du même moteur, valeurs honnêtes proches du seuil, différence bénigne de plateforme et résultat faux commun aux deux moteurs.
- Pour la permutation : politique constante, politique aléatoire indépendante des données et statistique réellement dépendante des données, tous évalués sans réutiliser le corpus de conception.

## Sur la proposition E

**(a) Défauts de méthode**

- **L’indépendance de l’oracle est affirmée avant d’être opérationnalisée.** Si les étiquettes, la spécification ou le recalcul partagent leurs erreurs, le corpus ferme reproduit cette erreur commune. Le premier duel devient presque tautologique lorsque le vérificateur externe est aussi la source de la propriété prétendument indépendante.
- **Le gain du recalcul est vrai par construction sur les défauts sémantiques** : empreintes et traces ne sont pas conçues pour les détecter. Mélanger défauts documentaires, fonctionnels et de collecte permet de faire varier le gain mesuré en changeant seulement les proportions du corpus.
- **L’appariement peut sur-apparier** et supprimer précisément les caractéristiques qui distinguent les charges réelles. Sauf pour les canaris, la séparation calibration/évaluation n’est pas explicitement imposée à tous les réglages.
- **Le duel d’apprentissage confond information retournée et occasions supplémentaires.** À nombre de propositions, requêtes ou temps de recherche différents, l’effet ne peut être attribué au contenu du retour.
- La restriction aux cas « valides » risque enfin d’écarter sélectivement les exécutions difficiles, même si les refus sont publiés à part.

**(b) Lois sous lesquelles les critères perdent leur pouvoir**

- Pour des familles de défauts \(d\), \(\widehat{TD}=\sum_d w_d\widehat{TD}_d\). Changer les poids \(w_d\) change le gain estimé sans changer l’instrument. Les intervalles doivent être appariés et tenir compte de la dépendance entre cas issus d’une même base.
- Si l’oracle a une probabilité d’erreur non nulle, ou si ses erreurs sont corrélées à celles du vérificateur, \(TD\) et \(FA\) ne sont pas identifiables comme taux de correction réelle.
- Si \(P(\text{valide}\mid D)\neq P(\text{valide}\mid H)\) et que la validité dépend de l’issue, les estimateurs conditionnés aux cas valides sont biaisés. Le dénominateur principal doit rester celui des cas randomisés.
- Pour l’apprentissage, l’effet mesuré est \(q_1(K_1)-q_0(K_0)\). Si \(K_1\neq K_0\), il mélange retour et opportunités. Si le producteur n’utilise pas le canal ou ne dispose d’aucune adaptation, l’effet nul ne dit rien sur une loi future plus adaptative.
- Pour la garde réseau, dès que \(P(\text{délai}\mid\text{sortie ouverte})>0\), « délai ⇒ fermée » produit de faux certificats. La matrice n’estime ce risque que sur les lois d’états qu’elle contient.
- À faible prévalence \(\pi\), même une petite \(FA\) peut rendre la valeur prédictive positive \(TD\pi/[TD\pi+FA(1-\pi)]\) trop faible pour un seuil éliminatoire.

**(c) Contrôles négatifs indispensables**

- Un **défaut commun à l’oracle et aux exécuteurs**, qui doit rester détecté comme limite et non transformé en réussite par accord ou recalcul.
- Une tranche réservée pour tous les duels, avec audit indépendant des étiquettes et dénombrement en intention de traiter des refus, pertes et dépassements.
- Pour l’apprentissage : canal placebo de même longueur, calendrier et nombre de requêtes, mais sans information utile, et mesures pré-feedback.
- Pour la redondance : faux résultat stable partagé par les deux moteurs ; pour les canaris : accès incidents réservés et sondage hors couverture.
- Pour la garde réseau : un état **ouvert mais silencieux jusqu’au délai**, attesté indépendamment, en plus de l’état réellement fermé. Sans lui, la correction proposée ne falsifie pas le mode d’échec central.

FIN-DE-CELLULE