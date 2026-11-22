# Proposition A · Tour III.3 : réponse aux critiques

## État des pièces

- Le bloc FAITS ne contient que l'énoncé de la question ; la « réponse 23 de Fable » et les « notes » annoncées en en-tête sont absentes, et je n'en infère rien.
- Ma conception T1 et les cinq critiques (B, C, D, E, F) sont présentes et se terminent chacune par FIN-DE-CELLULE. Je n'ai recalculé aucun sha256.
- Je ne réponds qu'aux sections « Sur la proposition A ».
- Statuts : ce que dit l'énoncé est RAPPORTÉ ; mes décisions, corrections et plans sont HYPOTHÈSE. Tous les chiffres sont illustratifs. Les références sont celles du T1, citées de mémoire.

## (a) Décision critique par critique

Trois décisions possibles : **acceptée**, **rejetée** (avec raison), **test** (transformée en test).

### Critiques de B

| Critique | Décision |
|---|---|
| a1. S_porte et S_scellé sont du même genre, donc E1-H_B s'obtient par construction sous fuite de genre | **Acceptée.** Ma phrase du T1 (« H_B réfute ma propre recommandation ») était fausse : E1 ne borne que l'usure au niveau des cas. E1 est retiré de l'ensemble réel et devient E1′. |
| a2. K est un temps d'arrêt, donc la régression de Δ sur K est confondue | **Acceptée.** K est imposé par tirage dans E1′. |
| a3 et R1. E2 confond canal et diversité et ne sépare pas α et β | **Test.** Je me sers de R1 comme HYPOTHÈSE d'architecture, et E2′ peut la réfuter. Le contraste Z_rejeu devient le cœur d'E2′. |
| a4. Bruit d'étiquette asymétrique sur le cas (a) d'E3 | **Acceptée.** E3′ ajoute une seconde vérification indépendante sur sous-échantillon. |
| a5. Le seuil « AUROC ≤ 0,6 » biaise (ii) contre le texte | **Acceptée.** Je n'avais pas prescrit de filtrer, mais un critère éliminatoire revient au même. Il devient un diagnostic rapporté, et (ii) se mesure sur la population non filtrée. |
| a6. La double différence d'E5 est aveugle à la fuite de genre | **Acceptée.** Voir E5′. |
| b. E1 : erreur-type d'environ 0,037, supérieure à la marge de ±3 points | **Acceptée.** Mes marges et mes effectifs étaient incohérents. Recalcul : ±3 points exigent environ 4 000 cas par moitié, et ±5 points à 25 % de discordance exigent environ 860 paires, pas 200. |
| b. E2 (corrélation des erreurs), E4 (Var f(X) ≤ m², σ_pub ≥ m), instrument 1 à 1 %, E5 | **Acceptées.** Le point à 1 % de fausses alertes sort du plan confirmatoire. Les autres deviennent des conditions de non-jugeabilité vérifiées avant ouverture. |
| c. Second genre, Z_rejeu, K randomisé | **Acceptées** et intégrées. |

### Critiques de C

| Critique | Décision |
|---|---|
| a1, b1. Fuite intra-genre, puissance nulle contre une fuite de genre pure | **Acceptée**, même objet que B-a1. Je reprends la décomposition de C (le terme β_genre s'élimine par soustraction) pour définir l'estimande U_genre d'E1′. |
| a2. E3 conditionne sur l'issue et confond avec la compétence | **Acceptée.** Voir E3′. |
| a3. Corrélation intra-canal plus forte entre T et T₂ | **Acceptée.** T₂ devient un bras descriptif, pas le comparateur décisif. |
| a4, b2. Le seuil transféré du développement ne garantit pas le même taux réel de fausses alertes sur Q | **Acceptée.** La métrique principale d'E2′ passe à taux de fausses alertes apparié sur les honnêtes de Q. |
| b3. TOST : région d'acceptation vide à n fini ; biais dû à l'erreur de mesure sur x | La première partie est **acceptée**. La seconde devient une condition de non-jugeabilité : σ_u est inconnu tant que la loi n'est pas nommée (P3). |
| b4. Double différence sous exposition endogène et changement de pente | **Acceptée.** Un placebo est ajouté à E5′. |
| c1. Lot d'un genre distinct | **Acceptée.** |
| c2. Permutation des activations par quantiles du score textuel, ou sonde sur modèle lecteur | **Scindée.** La permutation par quantiles est **rejetée** : la pièce de C (contre E) et celle de E (contre F) montrent qu'elle rejette à tort quand le score varie à l'intérieur d'une tranche. La sonde sur lecteur est **acceptée** sous la forme Z_rejeu (mêmes poids). |
| c3. Test d'homogénéité KS ou Anderson-Darling avant de lire un taux à seuil transféré | **Rejetée comme porte.** Un non-rejet n'établit pas l'homogénéité, et à grand effectif le test rejette pour des écarts sans conséquence. L'objectif est repris par l'appariement du taux de fausses alertes sur Q. |

### Critiques de D

| Critique | Décision |
|---|---|
| E1 : la croissance n'est pas identifiable sur un seul arrêt ; le bootstrap ne rejoue ni la sélection ni l'arrêt ; P(τ = ∞) > 0 | **Acceptée.** Dans E1′, l'unité de réplication est la campagne, et les campagnes sans franchissement sont comptées. |
| E2 : battre un second lecteur donné ne vaut que contre ce comparateur | **Acceptée.** Toute conclusion de (ii) sera formulée « relativement au détecteur texte nommé ». |
| E3 : le contraste diagonal ne détermine pas les effets propres | **Acceptée.** E3′ passe à un plan 2×2. |
| E4 : l'incertitude publiée n'est pas la marge d'écart négligeable ; le résidu moyen manque un écart conditionnel | **Acceptée.** m et σ_pub sont séparés, et le test se fait par tranche de x. |
| E5 : geler les poids ne gèle ni la loi, ni le seuil, ni l'affirmation | **Acceptée.** Le manifeste haché couvre ces objets, ce qui rejoint P2. |
| L'oracle qui lit les tests ayant défini les étiquettes ne vérifie que la cohérence du codage | **Acceptée.** Il est renommé « contrôle de cohérence ». La validité des étiquettes demande une vérification indépendante. |
| c. Boucle à retour fictif ; inducteur inerte ; résidus nuls simulés conditionnellement aux x couverts ; fausse date d'exposition | **Acceptées.** Je m'en sers telles quelles dans E1′, E3′, E4′ et E5′. |

### Critiques de E

| Critique | Décision |
|---|---|
| a1. Lire S_porte expose le genre unique avant ouverture | **Acceptée**, même objet que B-a1. E en tire en plus une conséquence pour mes réponses 1 et 2 : voir (c). |
| a2. Dérive de seuil ; effet d'encodeur (sonde sur un grand modèle contre un détecteur texte plus léger) | **Acceptée.** Z_rejeu, dans les mêmes poids, neutralise l'encodeur. |
| a3. Biais de collisionneur dans E3 | **Test.** Je reprends le contrôle de E : un prédicteur qui ne lit que l'énoncé initial. |
| a4. Compensation de signes dans E4 ; cécité au genre dans E5 | **Acceptées.** |
| b3. Résidus à queue lourde | **Acceptée sous condition.** Elle vaut si y n'est pas borné. Si y est un taux, la variance est finie. Cela dépend de P3. |
| c1 à c3. Duels sur l'égalité des taux de fausses alertes, la difficulté a priori, le genre tiers | **Acceptés** et intégrés avec leur forme H_A/H_B. |

### Critiques de F

| Critique | Décision |
|---|---|
| a1, a2 | **Acceptées**, mêmes objets que B-a1 et C-a4. |
| a3. « Même préfixe, même graine » est impossible sur un agent déterministe sans perturbation | **Acceptée.** « Même graine » est retiré. L'appariement devient : même tâche, même préfixe jusqu'au point de bifurcation, puis tirages distincts. |
| a4. E4 confond dérive du détecteur et écart à la loi | **Test**, conditionnel à P3 : si la grandeur y de la loi le permet, y est calculé deux fois, avec les étiquettes mécaniques et avec les sorties du détecteur. |
| a5. Fuites hors commits ; la simulation par graines sous-estime l'adaptativité | **Acceptée.** La simulation de l'instrument 4 ne donne qu'une borne inférieure du taux de faux passage, et elle ne certifie que la stratégie simulée. |
| b. Corrélation intra-grappe ; effet plafond ; covariance des paramètres publiés ; n_exp/N proche de 0 ou de 1 | **Acceptées.** L'unité de rééchantillonnage devient la grappe (dépôt ou famille de tâches). |
| c1 à c4 | **Acceptées.** |

### Bilan

- Deux rejets : la permutation par quantiles et le test d'homogénéité comme porte.
- Une erreur de ma part reconnue sans réserve : la portée d'E1-H_B.
- Un point maintenu en partie : le guichet budgété à un bit (voir (c), réponse 1).

## (b) Expériences corrigées

Convention révisée :
- L'unité de rééchantillonnage est la grappe de tâches. Pour E1′, c'est la campagne.
- Avant chaque expérience, on calcule l'erreur-type attendue. Si la marge m est inférieure à environ 2,9 erreurs-types (règle illustrative pour 80 % de puissance d'un test d'équivalence à 5 %), l'issue « équivalence » est déclarée hors d'atteinte d'avance, et l'issue indécise réfute le dimensionnement (P11).
- Le manifeste haché avant ouverture contient le plan, les seuils, la règle de fusion, la loi retenue et le texte des affirmations.

### E1′. L'adaptation passe-t-elle au niveau du genre ? (questions 1, 2 et 3)

Elle ne touche jamais l'ensemble tenu à l'écart.

- **Dispositif.** Sur des genres de développement : G1 est coupé en G1-porte et G1-scellé, et G2 est un genre distinct que la boucle ne lit pas. La boucle d'amélioration est scriptée, avec K imposé par tirage à graine publique (par exemple 1, 4 ou 16 cycles), sur 30 campagnes par niveau. Un détecteur mécanique gelé sert d'ancre de difficulté sur G1-scellé et sur G2.
- **Estimandes.**
  - U_cas = score(G1-porte) − score(G1-scellé).
  - U_genre = [gain sur G1-scellé entre le cycle 0 et le cycle K] − [gain sur G2 sur la même période].
- **H_A.** U_genre > m : lire une tranche d'un genre adapte les détecteurs à tout le genre.
- **H_B.** L'intervalle de U_genre tient dans ±m.
- **Contrôle négatif.** Un bras à retour fictif (mêmes candidats, mêmes budgets, même règle d'arrêt, retour tiré au hasard) doit donner U_cas ≈ 0 et U_genre ≈ 0. Sinon la coupe est déséquilibrée.
- **Ce que chaque issue falsifie.**
  - H_A réfute mon régime du T1 (« par parties scellées du même genre »), ainsi que l'option « refaire dans le même genre » de la question 3.
  - H_B réfute la fuite de genre pour cette classe de boucles. B a posé lui-même cette condition de réfutation.
- **Limite.** La boucle scriptée sous-estime l'adaptation humaine (objection de E et de F à B, que je reprends contre moi). H_B ne vaut donc pas licence pour une boucle humaine ; H_A s'y transpose a fortiori.

### E2′. Qu'ajoute l'état interne, et par quelle voie ? (affirmation ii)

- **Bras.** T (détecteur texte nommé) ; T + T₂ (descriptif) ; T + Z_rejeu ; T + Z_int. Z_rejeu désigne les activations des mêmes poids relisant exactement le texte que lit T. Les sondes ont la même classe et le même budget de recherche (P6).
- **Métrique principale.** Détection à taux de fausses alertes apparié sur les honnêtes de Q. Le seuil est estimé sur une moitié des honnêtes de Q et appliqué à l'autre, selon une procédure gelée.
- **Métrique secondaire.** Seuil transféré du développement, avec le taux réel de fausses alertes de chaque bras rapporté à côté.
- **Préalable.** Mesurer l'écart numérique maximal entre Z_int et Z_rejeu. Si T lit tout le contexte, les deux doivent coïncider aux arrondis près, et seul le duel β reste ouvert.
- **Duel α (accès au contexte).**
  - H_A : gain(T + Z_int) − gain(T + Z_rejeu) > m.
  - H_B : l'intervalle tient dans ±m.
  - H_A réfute « l'apport tient à une meilleure lecture du même texte ». Si T lit tout le contexte, H_A réfute aussi R1 : il existe alors un état non journalisé.
  - H_B réfute « l'état interne porte ce que le texte lu par T ne contient pas ».
- **Duel β (écart de calcul).**
  - H_A : gain(T + Z_rejeu) − gain(T) > m.
  - H_B : l'intervalle tient dans ±m.
  - H_A réfute « T extrait déjà ce que les poids calculent à partir de ce texte ».
  - H_B, jointe à α-H_B, réfute (ii) relativement à T.
- **Contrôles négatifs.**
  - Sonde sur étiquettes permutées.
  - États internes permutés par strate, passés dans la fusion gelée sans réentraînement. E propose ce contrôle contre D ; je l'adopte.
- **Vérifications avant ouverture.**
  - Effet plafond : si T détecte déjà plus de 1 − m en développement, le duel est déclaré non jugeable.
  - Présence d'honnêtes dans Q (P4).
  - Lisibilité de l'état interne (P5).
- **Portée.** Un seul genre : tout verdict est conditionnel à ce genre et à ce T.

### E3′. Dégradation ou inducteur ? (validité de ii)

- **Plan 2×2.** Inducteur actif ou inerte (même position, même longueur, contenu neutre), croisé avec une issue dégradée ou intacte. Les alertes sont lues au même instant de trajectoire.
- **Contraste intra-tâche.** Depuis un même préfixe, plusieurs tirages après le point de bifurcation. Les tâches dont tous les tirages ont la même issue ne contribuent pas, et l'effectif utile est annoncé en conséquence.
- **Duel D.**
  - H_A : à inducteur actif, taux d'alerte(dégradé) − taux d'alerte(intact) > m.
  - H_B : l'intervalle tient dans ±m.
  - H_A réfute « la sonde ne lit que l'inducteur ». H_B réfute « la sonde lit la dégradation ».
- **Duel C.**
  - H_A : à issue intacte, taux d'alerte(actif) − taux d'alerte(inerte) > m.
  - H_B : l'intervalle tient dans ±m.
  - H_A réfute « la sonde est aveugle à l'inducteur », ce qui borne la portée de (ii) aux dégradations ainsi induites. H_B réfute l'objection « détecteur de consigne ».
  - Les quatre combinaisons se lisent, y compris « sensible aux deux ».
- **Cellule spontanée (dégradé, sans inducteur).** Elle est observationnelle et rapportée à part. Elle n'est utilisée que si un prédicteur lisant le seul énoncé initial ne sépare pas les bras (AUROC entre 0,45 et 0,55). Sinon elle est confondue avec la difficulté.
- **Étiquettes.** Sur un sous-échantillon d'« intacts », une seconde suite de tests écrite indépendamment donne un taux de désaccord. Au-delà d'un plafond fixé d'avance, le duel C n'est pas jugeable.

### E4′. Écart à la loi (affirmation i)

- **Préalables sans ouverture.**
  - La loi est nommée, avec ses paramètres et leur covariance (P3).
  - La chaîne de mesure reproduit la loi dans les conditions publiées.
  - Un dépositaire, qui n'est pas auteur de détecteur, vérifie sur les seules covariables de Q que Var f(x) > m². Sinon l'expérience n'est pas jugeable.
- **Marge.** m est le plus petit écart qui importe. Il est distinct de σ_pub, justifié par écrit et gelé. Ce choix relève d'un jugement. Le contrôle mécanique porte seulement sur sa date.
- **Statistique.** Intervalles signés par tranche de x fixée d'avance. Pas de résidu moyen, pas de somme de valeurs absolues.
- **H_A.** Au moins une tranche est hors ±m, après correction de multiplicité.
- **H_B.** Toutes les tranches sont dans ±m.
- **Loi nulle.** Séries simulées conditionnellement aux x couverts, avec l'incertitude publiée.
- **Contrôle positif.** Un écart injecté de moyenne nulle mais conditionnellement non nul doit être détecté.
- **Double calcul.** Si P3 le permet, y est calculé sur les étiquettes mécaniques et sur les sorties du détecteur. Un écart présent seulement dans le second calcul est imputé à l'instrument.
- **Ce que chaque issue falsifie.** H_A réfute « la loi s'étend à ce genre ». H_B réfute « ce genre échappe à la loi sur l'étendue de x couverte ».

### E5′. Exposition (question 3)

- **Duel « cas ».** Double différence du T1, complétée par un placebo : une fausse date d'exposition entre deux versions antérieures, sur la même partition vu/non vu, doit donner une interaction nulle. Sans deux versions antérieures, le duel n'est pas jugeable.
  - H_A : interaction > m. Elle réfute « garder tel quel ».
  - H_B : intervalle dans ±m. Elle réfute « mémorisation de cas », et rien de plus.
- **Duel « genre ».**
  - H_A : [progrès après exposition sur les cas non vus de Q] − [progrès sur un genre tiers Q′] > m. Elle réfute « les cas non vus restent hors genre ».
  - H_B : intervalle dans ±m. Elle réfute la fuite de genre.
  - L'existence de Q′ est une HYPOTHÈSE. Sans Q′, seul le duel « cas » est jugeable, et il faut le dire.
- **Non-jugeabilité.** Part exposée proche de 0 ou de 1. Exposition liée à la difficulté sans version antérieure.

### Instruments

- Le point à 1 % de fausses alertes n'est plus confirmatoire.
- Le seuil d'AUROC mécanique est un diagnostic rapporté.
- La simulation du critère de passage est une borne inférieure.
- L'effectif illustratif du T1 est à refaire : environ 860 paires effectives pour une marge de ±5 points, ou une marge de ±6 points à 600 paires, avant correction de grappe.

## (c) Réponse à la question de l'arbitre

### Ce qui est établi

Aucun résultat empirique : le bloc FAITS ne contient aucun fait VÉRIFIÉ. Trois points de méthode sont des conséquences formelles de définitions, valables sous leurs hypothèses, et aucun n'est une mesure :

1. Une coupe à l'intérieur d'un genre ne peut pas détecter une adaptation au genre, car le terme commun s'élimine par soustraction. Cinq critiques sur cinq le relèvent, et je le concède.
2. Sous R1 (HYPOTHÈSE d'architecture posée par B), l'état interne est une fonction du contexte. (ii) ne peut alors signifier que « T ne lit pas tout » ou « T n'extrait pas tout », relativement à un T nommé.
3. Un seuil fixé en développement ne garantit pas des taux de fausses alertes égaux entre bras sur un genre nouveau.

### Ce qui ne l'est pas

- Si la fuite de genre existe et de quelle taille (E1′).
- Si l'équipe a vu un résultat tiré de l'ensemble avant de changer d'affirmation (P2).
- Si l'ensemble contient des honnêtes (P4) et des états internes lisibles (P5).
- Quelle est la loi (P3, référence à vérifier).
- Si un second genre jamais consulté existe.
- Si R1 tient dans l'implémentation.
- Tous les effets et tous les effectifs.

### Réponses révisées

Les certitudes sont subjectives et illustratives. Les antériorités sont celles du T1, citées de mémoire.

**1. À quoi sert l'ensemble ? À la portée seulement.**
- Le guichet à un bit du T1 n'est plus recommandé par défaut. Il reste défendable par une borne théorique sur l'information rendue, mais aucun contraste interne à l'ensemble ne peut vérifier qu'il n'a pas adapté les détecteurs au genre.
- Énoncé réfutable : E1′-H_B me donnerait tort pour une boucle scriptée.
- Antériorité : Dwork, Feldman, Hardt, Pitassi, Reingold & Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis ».
- Contrôle sans avis : le journal d'accès au fichier haché ne montre aucune lecture avant le gel.
- Certitude : 85 % pour « portée », 80 % pour « pas au critère ».

**2. Quand le consulter ? Une seule fois, au gel.**
- Une réserve scellée n'est valide que pour de nouvelles analyses sur les mêmes détecteurs gelés. Elle ne vaut pas pour des détecteurs modifiés après la première ouverture, qui auraient reçu une information de genre.
- Énoncé réfutable : E1′-H_B rétablirait mon régime « par parties » du T1.
- Antériorité : Armitage, McPherson & Rowe (1969), « Repeated significance tests on accumulating data ».
- Contrôle sans avis : les hachés du manifeste et des tranches sont antérieurs à l'ouverture ; aucun commit de détecteur ne se situe entre l'ouverture et l'usage de la réserve.
- Certitude : 75 %.

**3. Si des auteurs l'ont vu ? Cela dépend de quatre éléments.**
- La date, l'objet et la symétrie, comme au T1, plus le **niveau** : cas ou genre.
- Si l'exposition est postérieure au dernier commit, on garde l'ensemble.
- Si elle est antérieure, il est déclassé pour ces détecteurs. « Refaire » doit alors désigner un autre genre : retirer des cas du même genre ne rétablit pas « genre non vu ».
- Jeter n'est justifié dans aucun cas, car les cas vus servent à E5′.
- Énoncé réfutable : les deux duels d'E5′.
- Antériorité : Kaufman, Rosset, Perlich & Stitelman (2012), « Leakage in Data Mining: Formulation, Detection, and Avoidance ».
- Contrôle sans avis : l'ordre entre horodatages d'accès et dates de commit ; le placebo de fausse date.
- Certitude : 80 % pour « cela dépend », 65 % pour la règle.

**4. Le changement d'affirmation modifie-t-il les réponses ? En partie.**
- Ce qui ne change pas : la séparation entre critère et ensemble, et la consultation unique.
- Ce qui change :
  - l'ensemble doit contenir des honnêtes et des états internes (P4, P5) ;
  - (ii) devient un énoncé relatif à un T nommé, décomposé en α et β ;
  - (i) demande une loi nommée et une marge m distincte de son incertitude ;
  - pour (ii), c'est l'asymétrie d'exposition qui biaise.
- Énoncé réfutable : aucune requête sur l'ensemble n'est antérieure au document qui acte le changement. Une seule requête antérieure le réfute.
- Antériorité : Kerr (1998), « HARKing: Hypothesizing After the Results are Known ».
- Contrôle sans avis : l'ordre des horodatages.
- Certitude : 75 %.

### L'expérience à faire en premier

D'abord trois vérifications par inventaire, sans ouvrir l'ensemble :
- l'ordre des horodatages (P2) ;
- la présence d'honnêtes et d'états rejouables (P4, P5) ;
- l'identification de la loi (P3).

Ensuite **E1′**. Elle ne touche pas l'ensemble, et ses deux issues modifient les réponses 2 et 3 :
- H_A impose « une seule fois » et « refaire dans un autre genre » ;
- H_B rétablit le régime par parties, me donne raison contre les cinq critiques pour une boucle scriptée, et laisse ouverte la question pour une boucle humaine.

## Ce qui peut être réfuté ici

Huit duels :
- un dans E1′ ;
- deux dans E2′ ;
- deux dans E3′ ;
- un dans E4′ ;
- deux dans E5′.

Deux rejets (C-c2 pour la permutation par quantiles, C-c3 comme porte) que leurs auteurs peuvent contester. Rien ici n'est un résultat.

FIN-DE-CELLULE