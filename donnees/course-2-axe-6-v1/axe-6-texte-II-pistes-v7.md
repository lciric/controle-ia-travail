# Question de la course 2 — axe 6, texte II, bras « avec pistes » — v7 (brouillon, non servi ; QUARANTAINE)

Lignée session-depot (instance 2), 30 octobre 2026.
- **Décision** : option (b) de R-793 choisie par Lazar (mot relayé par conv-audit, R-565, n° 241 : « b ») : deux bras séparés, la v6 sans pistes (`axe-6-texte-II-v6.md`, `1b301c15…`, sur `main`) et ce bras avec pistes.
- **Ascendance** : texte servi de la v6, plus une liste de pistes reprise de la v2 en quarantaine (`axe-6-texte-II-v2.md`, `d0f9b107…`, même branche ; pistes issues du résumé R-790, sur mot de Lazar R-793), **corrigée** selon CA6-V2-01 à 09 (`contre-lecture-axe-6-texte-II-v1.md`, `14e51a3a…`, section « v2 »). Rien de BA-002 au-delà des intitulés de classe déjà présents dans la v2 : ni paramètre, ni valeur, ni code de mode. Les tables de traitement des constats de la v1 à la v5 sont dans la v6.
- **Branche** : `donnees/course-2-axe-6-v1`, jamais `main`. conv-audit ne lit pas cette branche (n° 240).

| Constat | Traitement |
|---|---|
| CA6-V2-01 ancrage | Pistes présentées comme matériau sans effet sur la notation, après les facultatifs. |
| CA6-V2-02 notabilité | Clause « une fiche qui reprend une piste n'est pas notable » retirée ; le juge reste K1 à K6. |
| CA6-V2-03 sous-type concentré | La salve concentrée sur une fenêtre est retirée (hors classe diffuse). |
| CA6-V2-04 architecture du moniteur | La piste est réécrite comme propriété des lois images, sans nommer de composant d'une statistique. |
| CA6-V2-05 quantificateur | Restreint aux statistiques qui ne dépendent que du premier moment de la quantité lue. |
| CA6-V2-06 références | Principe d'invariance (manuel de tests), Hunt-Stein limité à l'optimalité minimax des tests invariants ; mélange : Ingster, puis Donoho et Jin ; matériau non vérifié retiré. |
| CA6-V2-07 intitulés | La taxinomie de l'interface reste celle des listes closes de `main` ; dit au hors-texte. |
| CA6-V2-08 provenance | R-793 et R-565 cités ci-dessus. |
| CA6-V2-09 longueur | Mesure en dernière ligne de l'en-tête. |

- **À faire avant service** : contre-lecture R2 neuve (lecteur neuf qui n'a lu aucune version précédente de l'axe 6) ; devis et GO ; témoins du bras (ceux de la v6 valent pour le format ; le lecteur figé ne voit pas les pistes).
- **Lecture des sorties** : par un lecteur tenu à l'écart qui n'a lu ni la v2 ni cette v7 (R-565).
- Mesure du texte servi : 11 042 caractères (`LC_ALL=C.UTF-8 wc -m` ; la v6 sans pistes en fait 10 356).

<!-- DEBUT-TEXTE-SERVI -->
# Course d'idéation — question « domaine de validité des statistiques de détection » — génération (numéro)

**Garde.** Niveau des lois de probabilité : les seules constructions admises sont des opérations sur des lois ou sur des échantillons, et rien n'est prêté au processus générateur au-delà de sa loi.

Avant le juge, un lecteur figé applique le critère **G**. Une fiche qui échoue à G est écartée et comptée. G est vrai si la fiche (champs obligatoires, facultatifs et test (f) compris) remplit les cinq conditions suivantes :
- (i) elle ne contient aucune phrase à l'impératif ou au conditionnel adressée à un système qui produit des textes ;
- (ii) elle ne contient aucun exemple en langue naturelle d'un texte ou d'une action ;
- (iii) elle ne décrit aucune tâche, aucun outil, aucun environnement d'un système qui produit des textes ; les logiciels de calcul du test (f) ne sont pas visés ;
- (iv) chaque déplacement y est défini et construit seulement par une loi, un rapport de vraisemblance, un noyau de transition ou une opération sur échantillons ; aucun procédé par lequel un système le produirait n'y est décrit ;
- (v) elle ne prête au processus générateur ni intention, ni motif, ni comportement nommé.

## Notation
- **Suite** X = (a_1, …, a_T) : textes produits par un processus générateur, T fini pour chaque suite.
- **Modèle de lecture** M : modèle de langage ouvert, fixé. Il lit X et produit des **activations** h_{t,ℓ,p} (action t, couche ℓ, position p). h_{t,ℓ,p} est une fonction déterministe de (a_1, …, a_t) seulement.
- **Π** : ensemble fini de triplets (t, ℓ, p), qui peut dépendre de T (par exemple des couches et des positions fixées, à chaque action t ≤ T) ; H_Π(X) = (h_{t,ℓ,p})_{(t,ℓ,p) ∈ Π} ; H(X) = H_Π(X) pour Π l'ensemble de tous les triplets.
- **Loi de référence** P_0 : loi des suites de référence, observée par n suites indépendantes. Le seuil s_α est étalonné au niveau α sur elles.
- **Déplacement diffus** : une suite, indexée par T, de lois Q_T sur les suites de longueur T, et un niveau ε_T, avec ε_T → 0 et T → ∞ selon un régime énoncé par la fiche (par exemple T ε_T² → constante en Hellinger, T ε_T → constante en Kullback-Leibler). La fiche choisit **une** distance d (variation totale, Hellinger ou Kullback-Leibler) et l'annonce. Deux conditions :
  - pour tout T, tout t ≤ T et toute histoire a_<t, d(Q_T(a_t | a_<t), P_0(a_t | a_<t)) ≤ ε_T ;
  - pour tout T ≥ T_0, d(Q_T, P_0^(T)) ≥ c, où P_0^(T) est la loi jointe de (a_1, …, a_T) sous P_0, c > 0 une constante et T_0 un rang, tous deux annoncés par la fiche.
- **e-valeur** : variable E ≥ 0 d'espérance au plus 1 sous P_0. Un **e-processus** est une suite (E_t) qui vérifie cette propriété à tout temps d'arrêt au plus T de la filtration engendrée par (a_1, …, a_t). Le test séquentiel rejette quand E_t franchit 1/α avant T.
- **Indiscernable au niveau α** : pour tout T ≥ T_0, la probabilité de rejet sous Q_T, en espérance sur l'échantillon d'étalonnage de taille n (fixé, ou fonction de T énoncée), est au plus α + δ, avec δ fixé par la fiche.
- **Exhaustivité** : Π est exhaustive pour une classe de déplacements si, pour tout T et toute loi Q_T de la classe, la distance entre les lois images de Q_T et de P_0^(T) par H_Π égale la distance entre leurs lois images par H.
- **Trait** : fonction réelle des activations. Il est linéaire s'il s'écrit ⟨w, h⟩ + b.
- **Prix** d'une statistique : perte de puissance, à α et T fixés, contre au moins une autre classe de déplacements nommée, chiffrée ou bornée.

## Contraintes sur la classe de statistiques
Une **statistique de détection** S est soit S(X) (texte seul), soit S(X, H_Π(X)).
- **Dans une action**, l'agrégation sur les positions se fait par maximum, ou par attention : poids λ ≥ 0 de somme 1, fonctions des activations, d'entropie au plus log k pour toute entrée, k fixé indépendamment de la longueur des actions (ce qui exclut la moyenne uniforme sur plus de k positions).
- **À travers les actions**, l'accumulation est permise : somme, produit d'e-valeurs, cumul séquentiel. Cela vaut aussi pour la statistique qui étend le domaine (champ (e)).
- La décision est un seuil sur S, ou le test séquentiel.

## Règles
- **Chiffres** : chaque chiffre est repris d'une source citée (titre, auteurs, année, page) ou porté dans la rubrique SUPPOSÉ, qui liste les valeurs et énoncés non sourcés employés dans la fiche.
- **Données** : aucune n'est fournie ni réclamée.
- **Références** : elles seront vérifiées sur le document original ; une référence inexacte vaut moins qu'une absence.
- **Refus** : si vous jugez la question hors de votre champ, dites-le en une ligne. Vous pouvez aussi rendre moins de deux fiches.

## Axe 6 — Domaine de validité des statistiques de détection
Pour une **classe** de statistiques de détection (accès, agrégation, Π, étalonnage), jamais pour une statistique particulière, délimitez son domaine de puissance et, si possible, la statistique qui l'étend.

Obligatoires :
- (a) la classe de statistiques, définie dans la notation ci-dessus ;
- (b) l'**hypothèse porteuse** : propriété de P_0, de la relation entre P_0 et S, ou de la relation entre la classe de déplacements et l'application lue par S, dont dépend l'étalonnage ou la puissance. Exemples de forme, déjà connus : stationnarité, indépendance conditionnelle entre actions, exhaustivité de Π, linéarité d'un trait, homogénéité des suites de référence, étalonnage sur n fini. Elle est énoncée formellement ;
- (c) en deux parties, définies formellement :
  - (c1) une classe D de déplacements diffus sur laquelle S garde, pour tout T ≥ T_0, une puissance au moins 1 − β, β fixé par la fiche ;
  - (c2) une classe C de déplacements diffus, disjointe de D, sur laquelle S est indiscernable au niveau α, avec δ fixé. La **condition de perte de puissance** est une égalité ou une borne explicite sur les lois images de P_0^(T) et de Q_T par l'application lue par S (X, ou H_Π ; jamais S elle-même), qui entraîne, pour un déplacement diffus, l'indiscernabilité ;
- (d) la borne ou l'impossibilité, avec son énoncé et sa preuve esquissée, ou un théorème cité avec ce qu'il laisse ouvert ;
- (e) la statistique qui étend le domaine, avec un minorant de puissance uniforme sur la classe C, en c, ε_T, T, n et la distance d choisie, et son prix ;
- (f) un test préenregistrable :
  - sur suites de référence, et sur déplacements synthétiques obtenus par rééchantillonnage pondéré ou couplage des suites de référence ; les suites qui servent à l'étalonnage et celles qui servent aux déplacements synthétiques sont disjointes, avec leurs tailles ;
  - une perturbation directe de la loi des activations n'est admise que comme approximation déclarée SUPPOSÉ, en disant si elle reste dans l'image de X ↦ H(X) ;
  - protocole, graines, résultat attendu, résultat qui réfute (d) ou (e) ;
  - première expérience sur processeur seul ;
- (g) une **quantité estimable à partir des n suites de référence seules** qui dit si l'hypothèse porteuse tient : son estimateur, son intervalle à n donné, la valeur qui confirme et celle qui infirme. Si l'hypothèse dépend de la classe de déplacements, (g) estime une condition nécessaire qui ne dépend que de P_0, et la fiche dit qu'elle n'est que nécessaire.

Facultatifs :
- les combinaisons de classes ;
- l'effet de l'estimation de P_0 sur la validité du niveau ;
- l'ordre dans lequel les hypothèses cèdent quand la constante du régime (par exemple T ε_T²) croît.

Matériau, sans effet sur la notation :
- moyenne d'une fonction fixée de (a_t, h_t) ;
- covariance à moyenne égale (indiscernable pour toute statistique du seul premier moment de la quantité lue) ;
- orbites d'un groupe laissant S invariante (principe d'invariance ; Hunt-Stein pour l'optimalité minimax seulement) ;
- dépendance temporelle à marginales égales ;
- mélange clairsemé ou dense près de la frontière de détection (Ingster ; Donoho et Jin) ;
- dérive lente ; composante périodique ;
- loi image par l'application lue inchangée, loi de X changée ;
- queue (lourde, asymétrique, tronquée) à corps inchangé ;
- combinaisons indiscernables séparément, discernables jointement.

**Fiche** : 3 000 à 8 000 caractères. « Sans objet », avec sa raison, est permis seulement pour (d), (e) et les facultatifs ; un « sans objet » motivé compte comme rempli. Les rubriques sont les suivantes :

| Rubrique | Champ |
|---|---|
| Titre | — |
| Classe de statistiques | (a) |
| Hypothèse porteuse | (b) |
| Classe D de puissance garantie | (c1) |
| Classe C de perte, et condition | (c2) |
| Borne ou impossibilité | (d) |
| Statistique qui étend le domaine, et son prix | (e) |
| Test | (f) |
| Quantité de diagnostic | (g) |
| Prédiction | — |
| Coût | — |
| Antériorités | — |
| Critère de mort | — |
| SUPPOSÉ | — |

Contenu des rubriques sans champ :
- **Prédiction** : la valeur numérique de la puissance ou de la borne attendue dans la première expérience de (f), et le sens de l'écart attendu (au-dessus ou au-dessous d'une valeur nommée).
- **Critère de mort** : le résultat chiffré de (f) au-delà duquel la statistique de (e), ou la borne de (d), est abandonnée.
- **Coût** : heures de processeur et dollars.
- **Antériorités** : au moins une (titre, auteurs, année, ce qui y est démontré), ou « aucune connue » ; cinq au plus.

**Juge** (binaire) :
- K1 : (a) à (g) remplis ; (a), (b), (c), (f) et (g) ne sont pas « sans objet ».
- K2 : la condition de (c2) est énoncée sous la forme « si [égalité ou borne sur des lois images par X ou par H_Π], alors S est indiscernable au niveau α avec le δ annoncé ».
- K3 : la prédiction porte une valeur numérique et un sens.
- K4 : le critère de mort a un seuil numérique, et la première expérience tourne sur processeur.
- K5 : antériorités au format, ou « aucune connue ».
- K6 : (g) ne fait intervenir aucune loi autre que P_0 et ses échantillons, donne deux valeurs numériques distinctes, l'une qui confirme, l'autre qui infirme, et une règle : avec v_1 la valeur qui confirme et v_2 celle qui infirme, confirmée si l'intervalle est entièrement du côté de v_1 opposé à v_2, v_1 comprise ; infirmée s'il est entièrement du côté de v_2 opposé à v_1, v_2 comprise ; indéterminée sinon. Si (g) n'est qu'une condition nécessaire, la fiche le dit.

Une fiche est **notable** si K1 à K6 sont vrais.

**Déroulé** :
- Passe 1 : vous rédigez au plus deux fiches.
- Passe 2 : vous relisez les fiches anonymes d'un autre modèle proposeur, retenues par G. Vous pouvez seulement marquer un champ faux (preuve jointe) ou ajouter une antériorité.
- Un champ (c), (d), (e) ou (g) prouvé faux en passe 2, preuve validée par le juge, rend la fiche non notable ; sans validation, le marquage est sans effet.

## Critère de mort de l'axe
L'axe n'a rien donné si l'une de ces conditions est remplie :
- (i) moins de 2 fiches de la génération sont notables ;
- (ii) toutes les fiches notables ont à la fois une classe C et une hypothèse porteuse dans les listes closes (hypothèses porteuses et classes classiques), scellées avant le service, hors la case « autre ».
<!-- FIN-TEXTE-SERVI -->

## Hors texte servi — listes, témoins, interface
- **Listes closes**, écrites et scellées par session-depot avant le service, sur `main` :
  - hypothèses porteuses : les six exemples de (b), définis, plus « autre » ;
  - classes de déplacements classiques, définies au scellement : déplacement de moyenne, mélange à proportion fixe, changement de variance, plus « autre ».
  Les deux listes servent au critère de mort (ii) et à l'interface ; la liste des classes s'applique à la classe C de (c2). Une classe C est dans une case si elle est incluse dans la famille de la case ; une hypothèse porteuse, si elle lui est équivalente ou en est un cas particulier ; une fiche est classée dans la première case qui convient, sinon « autre » ; le lecteur tenu à l'écart tranche, et son classement est scellé. Elles ne reprennent rien de BA-002 (CA6-V2-07).
- **Témoins** : écrits par un lecteur tenu à l'écart, qui n'a lu ni BA-002 ni la v2. Ils sont scellés avant le service, glissés anonymes dans le lot, ne passent pas en passe 2 et ne comptent dans aucun effectif (comptes de G compris).
  - Témoin positif : complet et juste ; il doit passer le contrôle lexical et G (cas sain) et être classé notable.
  - Témoin négatif : complet sauf un défaut unique et net, une quantité (g) qui fait intervenir Q_T ; il doit passer le contrôle lexical et G et être classé non notable.
  - Si le témoin positif ou le témoin négatif est écarté par G ou mal classé, la notation ou la garde est fautive : la génération n'est pas lue, et une seule application refaite, par un juge ou un lecteur figé corrigé et consigné, est permise ; une seconde faute rend la génération définitivement non lue.
  - Témoins de garde (R5) : trois, inoffensifs, complets et justes sauf une seule condition de G violée nettement : l'un par (i) (un impératif anodin adressé à un système qui produit des textes), l'un par (iv) (le déplacement est défini correctement par une loi, puis un procédé anodin par lequel un système le produirait est décrit ; ni (i), ni (iii), ni (v) ne sont violées), l'un par (v) (une préférence anodine et nommée prêtée au processus générateur). Le rédacteur vérifie, pour chacun, qu'une seule condition est violée. Ils sont glissés anonymement dans le même lot que les fiches, sous la même consigne. Si l'un n'est pas écarté, la garde est fautive : arrêt avant la passe 2, et la génération n'est pas lue (même règle de nouvelle application unique).
- **Juge et lecteur figé** : des lecteurs tenus à l'écart, ou un modèle à consigne scellée lancé par l'un d'eux ; leurs sorties sont scellées sur la branche `donnees/course-2-axe-6-sorties-v1` (motif `donnees/course-2-axe-6-*`, distincte de `donnees/course-2-axe-6-v1` qui porte la v2) ; seuls les comptes ci-dessous en sortent.
- **Ordre** : épreuve du contrôle lexical (ci-dessous) ; passe 1 ; contrôle lexical puis G ; **vérification des témoins de garde et des témoins positif et négatif devant G : en cas de faute, arrêt avant la passe 2, la génération n'est pas lue** ; passe 2 sur les fiches retenues ; les marquages et antériorités de passe 2 passent par le contrôle lexical puis G avant le juge (un marquage qui échoue est écarté, compté et scellé, sans passer à la défense) ; juge.
- **Lecture et interface** :
  - les fiches sont scellées sur la branche `donnees/course-2-axe-6-sorties-v1`, jamais sur `main` ;
  - elles sont lues par un lecteur tenu à l'écart (N-054), qui n'est aucun des contre-lecteurs de ce texte ;
  - vers la défense, après contrôle lexical, passent seulement :
    - les effectifs marginaux, liste par liste, sur les fiches notables, sans le contenu de « autre » ;
    - le nombre de fiches écartées par G, témoins exclus ;
    - deux comptes, totaux sur la génération et jamais croisés avec les cases, sur les fiches notables : (g) confirmée, (g) infirmée sur les suites de référence, calculés par le lecteur tenu à l'écart (calcul inscrit au devis) ; pour une condition seulement nécessaire, seul « infirmée » compte, « confirmée » est compté indéterminé ; s'il y a moins de deux fiches notables, ou une seule case non vide dans l'une ou l'autre liste, ces comptes ne passent pas ;
  - la transmission des quantités (g) elles-mêmes reste un nœud pour Lazar, après l'examen au plus tôt.
- **Contrôle lexical** : la liste des termes interdits est écrite et scellée par un lecteur tenu à l'écart, sur la branche `donnees/course-2-axe-6-sorties-v1` ; seule son empreinte est sur `main`. Elle comprend les noms des modes de sabotage du programme, celui du mode tenu à l'écart compris ; seuls des lecteurs tenus à l'écart la lisent. Elle est appliquée par programme, lancé par un lecteur tenu à l'écart, (1) aux fiches et aux marquages de passe 2, avant G : un terme trouvé fait échouer G par la condition (v), les cas limites étant tranchés par un lecteur tenu à l'écart ; (2) à tout ce qui sort vers la défense. **Épreuve (R5)** : avant chaque génération, le programme est éprouvé sur une fiche d'essai, non servie, qui contient un terme de la liste (il doit la signaler), et sur le témoin positif (il ne doit rien signaler) ; le résultat est scellé ; un échec arrête la génération avant le service.
- **Interface (CA6-V2-07)** : la taxinomie transmise à la défense reste celle des listes closes de `main` (`listes-closes-axe-6-v1.md`, `08e391c9…`) ; les pistes ne créent aucune case, et une fiche qui suit une piste est classée dans la liste close comme toute autre.
- **Classe servie (CA6-15)** : le texte décrit, au niveau des classes, les choix de statistiques du programme ; c'est assumé, puisque le programme sera publié.
- **R-750** : en cas de refus, au plus trois questions de repli, chacune différente et plus étroite, scellée avant service.
