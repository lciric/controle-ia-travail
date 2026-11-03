# Groupement des fiches de la piste Ibrahim (question 1) — ensemble, version 1

Groupeur neuf, aveugle au classement. Entrée lue seule : `/home/claude/scratch/soir-rapport/ibrahim-q1/piste/fiches-a-grouper-ensemble-v1.json` (sha256 `e3afb86950d457411d1d989635ed63ebb5ea34b6264bc1b30a172ad1dc267c81`, vérifiée avant lecture), 23 fiches, IB-01 à IB-23.

Un groupe est un type d'expérience, défini par la question que la première expérience tranche.

## Définitions des groupes

Écrites le 2026-11-03 à 14:54:21 UTC (heure d'écriture du fichier, lue par `date -u -r`), après lecture des 23 fiches et avant toute affectation. Elles ne sont plus modifiées ensuite. Seule cette ligne d'heure a été corrigée, avant toute affectation : la première version portait 14:54:09, une heure qui ne venait pas de `date -u` (voir « Trace »).

### 1. Survie au renforcement
Définition :
La première expérience tranche si ce que l'entraînement de caractère a installé (l'écart de la persona à la base, ou la sycophancie que porte cet écart) survit à un apprentissage par renforcement dont la récompense ne dit rien du social.
On compare persona et base avant et après ce renforcement, au premier tour ou au fil des tours ; la réponse attendue est « tient, s'érode ou s'efface », pas « pourquoi ».

Critère : la prédiction principale porte sur le maintien ou l'érosion, après un renforcement à récompense vérifiable, d'un écart persona − base (y compris son évolution au fil des tours), sans que son objet principal soit la relation entre deux composantes ni la comparaison de deux types de récompense.

### 2. Cause : contenu de la récompense
Définition :
La première expérience tranche si c'est le contenu de la récompense (des préférences humaines) qui produit ou amplifie la sycophancie, plutôt que le seul fait d'optimiser.
On fait varier le type de récompense (préférences, vérifiable, non informative ou à étiquettes permutées) à déplacement de politique apparié.

Critère : la prédiction compare au moins deux types de récompense, ou un type et un témoin non informatif, sur une mesure de sycophancie, et sa justification est l'attribution de la sycophancie à l'optimisation des préférences.

### 3. Structure du construit
Définition :
La première expérience tranche si la sycophancie de la persona est une seule chose ou des composantes dissociables : sociale contre factuelle, ton chaleureux contre capitulation sur le fond.
On mesure deux composantes sur les mêmes modèles et l'on teste leur présence relative, leur couplage ou leur dissociation.

Critère : la prédiction porte sur la relation entre deux composantes (l'une présente sans l'autre, l'une qui bouge plus, les deux qui covarient ou non), ou sur l'existence d'une capitulation de fond au-delà du seul ton.

### 4. Forme du déplacement sous pression
Définition :
La première expérience tranche comment le modèle se déplace sous pression : quelle loi (mélange ou contraction), quel paramètre de la loi d'attraction (point fixe ou gain), quelle posture ou quelle dimension de la réponse porte le déplacement.
C'est une décomposition du déplacement mesuré, à modèle ou persona donnés, et non une question de survie à un entraînement ou de cause d'entraînement.

Critère : la prédiction oppose deux descriptions de la forme du déplacement (mélange contre contraction, point fixe contre gain, posture qui médie ou non, concession par dimension contre verdict global).

### 5. Validité de l'instrument
Définition :
La première expérience tranche si le juge ou le classifieur lit ce qu'il prétend lire (la position, pas le style ni le lexique), et s'il le lit de la même façon sur tous les points de contrôle.
L'objet mesuré est l'instrument, confronté à une référence extérieure (annotation humaine, clé vérifiable, prédicteur mécanique ou lexical).

Critère : la prédiction compare la sortie de l'instrument à une référence extérieure ou à un prédicteur concurrent, et sa conclusion porte sur l'instrument, pas sur le modèle.

### 6. Robustesse au codage
Définition :
La première expérience tranche si un effet mesuré (en pratique celui du renforcement sur la sycophancie) tient quand on change une règle raisonnable de codage des mêmes sorties : refus, abstentions, longueur jugée.
Sans référence extérieure, on recode les mêmes réponses de plusieurs façons fixées d'avance et l'on regarde si l'effet change de taille ou de signe.

Critère : la prédiction compare le même effet sous au moins deux règles de traitement des réponses non substantielles ou de la longueur.

<!-- fin des définitions -->

## Affectations

Écrites le 2026-11-03 à 14:56:56 UTC (heure prise par `date -u` dans la commande même qui ajoute cette partie), après les définitions ci-dessus et sans les retoucher.

Chaque fiche va à un seul groupe, celui de son idée principale. « Second choix » : la fiche relève presque autant d'un autre groupe ; « — » : aucun.

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| IB-01 | Survie au renforcement | Prédit que l'excès de validation injustifiée d'une conduite par Loving sur la base ne baisse pas de plus de 5 points après le renforcement : maintien d'un écart persona − base. | Structure du construit (son mécanisme sépare validation des émotions et validation de la conduite) |
| IB-02 | Survie au renforcement | Prédit que l'écart de comportement Loving − base perd moins qu'une marge fixée d'avance après un renforcement à récompense vérifiable, à déplacement mesuré : survie de la persona elle-même. | — |
| IB-03 | Structure du construit | Prédit que l'effet du renforcement sur la capitulation de la persona est plus grand dans le domaine social que dans le factuel : dissociation de deux composantes. | Survie au renforcement (le dispositif est persona contre base, avant et après renforcement) |
| IB-04 | Validité de l'instrument | Confronte le classifieur de persona et le juge de sycophancie à des paires annotées par des humains et à des prédicteurs mécaniques : lisent-ils la position ou le style. | — |
| IB-05 | Forme du déplacement sous pression | Oppose un modèle de mélange et un modèle de contraction pour la forme des distributions de notes sous pression. | — |
| IB-06 | Cause : contenu de la récompense | Compare un renforcement à récompense vérifiable à l'avant-renforcement et à un témoin à récompense non informative, sur le gain, pour éprouver l'attribution du gain à l'optimisation des préférences. | Survie au renforcement (c'est aussi un test de maintien du gain après renforcement) |
| IB-07 | Cause : contenu de la récompense | Prédit qu'un renforcement contre un modèle de récompense appris sur des préférences amplifie l'erreur sous fausse croyance de Loving plus que celle de la base. | — |
| IB-08 | Forme du déplacement sous pression | Demande quel paramètre de la loi d'attraction la persona déplace : le point fixe plutôt que le gain. | Cause : contenu de la récompense (sa justification est l'a priori sur l'origine de chaque paramètre, imitation ou optimisation des préférences) |
| IB-09 | Cause : contenu de la récompense | Compare, à déplacement de politique apparié, un renforcement sur préférences, un renforcement vérifiable et un témoin à étiquettes permutées, sur le gain. | — |
| IB-10 | Structure du construit | Demande si la persona Sycophantic capitule sur les faits ou n'est qu'un ton, avant tout entraînement. | Validité de l'instrument (sert aussi à vérifier que l'instrument factuel a prise sur la manipulation) |
| IB-11 | Forme du déplacement sous pression | Teste si une posture (refus, prise de distance) médie la descente sous éloge des items bien notés : ce qui porte le déplacement. | Robustesse au codage (un refus noté au milieu de l'échelle est aussi une affaire de codage) |
| IB-12 | Validité de l'instrument | Compare le juge à un détecteur lexical figé : le juge lit-il plus que le lexique, est-il remplaçable. | Forme du déplacement sous pression (conclurait aussi que le déplacement est porté par le lexique) |
| IB-13 | Forme du déplacement sous pression | Oppose une concession par dimension (l'écriture cédée, la thèse gardée) à un déplacement global du verdict. | Structure du construit (dissociation de deux composantes de la capitulation) |
| IB-14 | Survie au renforcement | Prédit que l'excès d'erreur de Loving sous fausse croyance ne baisse pas de plus de 5 points après renforcement, hors du domaine de la récompense. | — |
| IB-15 | Survie au renforcement | Prédit que Loving reste, après un renforcement sans récompense sociale, plus sensible que la base à l'intensification de la pression flatteuse. | Structure du construit (distingue chaleur observable et susceptibilité sociale résiduelle) |
| IB-16 | Structure du construit | Prédit que la persona Sycophantic élève plus la sycophancie sociale que la capitulation factuelle, et que les deux ne covarient pas : fragmentation du construit. | — |
| IB-17 | Survie au renforcement | Prédit qu'après renforcement l'adhésion à la persona décroît davantage du premier au cinquième tour : maintien mesuré au-delà du premier tour. | — |
| IB-18 | Survie au renforcement | Prédit qu'après renforcement sur échanges courts la capitulation de Loving remonte davantage que celle de la base entre le premier et le quatrième ou cinquième tour. | — |
| IB-19 | Structure du construit | Oppose, conversation par conversation, couplage et découplage de la chute de chaleur et de la capitulation tardive. | Survie au renforcement (le cadre est la dérive après renforcement au fil des tours) |
| IB-20 | Robustesse au codage | Compare la baisse de capitulation de Loving sous deux codages des abstentions : comptées non sycophantiques, ou items à réponse substantielle seuls. | — |
| IB-21 | Structure du construit | Prédit que l'érosion de la persona sous renforcement entraîne un recul proportionnel de son excès d'erreur : couplage entre persona et capitulation de fond. | Survie au renforcement (mesure aussi l'érosion de la persona) |
| IB-22 | Validité de l'instrument | Confronte le biais du juge à une référence (clé vérifiable ou panel humain aveugle) sur chaque point de contrôle, avant et après renforcement. | — |
| IB-23 | Robustesse au codage | Cherche un changement de signe de l'effet du renforcement sous six codages préenregistrés des refus et de la longueur jugée. | — |

## Effectifs

| Groupe | Fiches | Nombre |
|---|---|---|
| Survie au renforcement | IB-01, IB-02, IB-14, IB-15, IB-17, IB-18 | 6 |
| Cause : contenu de la récompense | IB-06, IB-07, IB-09 | 3 |
| Structure du construit | IB-03, IB-10, IB-16, IB-19, IB-21 | 5 |
| Forme du déplacement sous pression | IB-05, IB-08, IB-11, IB-13 | 4 |
| Validité de l'instrument | IB-04, IB-12, IB-22 | 3 |
| Robustesse au codage | IB-20, IB-23 | 2 |
| Total | | 23 |

Fiches à second choix (11) : IB-01, IB-03, IB-06, IB-08, IB-10, IB-11, IB-12, IB-13, IB-15, IB-19, IB-21.

## Limites

1. Les définitions ont été écrites après lecture des 23 fiches, non a priori, mais avant toute affectation : le découpage épouse l'espace des fiches lues. Risque de groupe taillé sur mesure : « Robustesse au codage » ne compte que 2 fiches.
2. « Survie au renforcement » et « Structure du construit » partagent le même dispositif (persona contre base, avant et après renforcement). J'ai tranché par l'objet de la prédiction (maintien d'un écart, ou relation entre deux composantes). Trancher par le dispositif mettrait IB-03, IB-19 et IB-21 en « Survie au renforcement » (6 fiches deviendraient 9, et « Structure du construit » tomberait à 2).
3. « Validité de l'instrument » et « Robustesse au codage » répondent à la même demande de la mentore (ce qui rendrait le résultat trompeur) ; je les sépare par la présence d'une référence extérieure. IB-22 est à la frontière : référence extérieure, mais son enjeu (fabriquer ou masquer un effet du renforcement) est celui de « Robustesse au codage ».
4. Deux seconds choix tiennent à la justification de la fiche, non à son dispositif, qui ne remplit pas le critère du groupe visé : IB-08 (« Cause : contenu de la récompense », par l'a priori sur l'origine du point fixe et du gain, sans comparaison de récompenses) et IB-10 (« Validité de l'instrument », comme vérification que la manipulation a prise, sans référence extérieure).
5. Tension dans les définitions elles-mêmes : le critère de « Forme du déplacement sous pression » nomme la « concession par dimension contre verdict global », qui recouvre aussi le critère de « Structure du construit » (deux composantes de la capitulation). IB-13 relève des deux par construction ; je l'ai mise en « Forme » parce qu'elle porte sur le gain de la loi d'attraction du modèle de départ, sans entraînement ajouté.
6. Aucun groupe pour la dynamique au fil des tours : IB-17 et IB-18 sont en « Survie au renforcement », IB-19 en « Structure du construit ». J'ai traité les tours comme un axe de mesure, non comme une question distincte ; un groupe « au fil des tours » aurait réuni ces trois fiches.
7. « Forme du déplacement sous pression » réunit des fiches sur le modèle de départ (IB-05, IB-11, IB-13) et une fiche qui compare persona et base (IB-08), la moins centrale du groupe.
8. Les groupes ne suivent pas les deux projets de la mentore, que la consigne ne nomme pas ; je ne les ai pas devinés. Je ne sais pas si ce groupement recoupe le groupement précédent d'une partie des fiches : je ne l'ai pas lu.
9. Les fiches emploient des sigles et des renvois internes (RLVR, KL, IC, R6, R8, S3). J'ai lu les trois premiers au sens courant (apprentissage par renforcement à récompense vérifiable, divergence de Kullback-Leibler, intervalle de confiance) et laissé les renvois internes tels quels, sans rien vérifier hors du fichier d'entrée.
10. Erreur de procédure, corrigée : la première écriture des définitions portait une heure (14:54:09) qui ne venait pas de `date -u`, car j'avais lancé `date -u` en même temps que l'écriture. La ligne d'heure, et elle seule, a été corrigée à 14:54:42 UTC (heure lue par `date -u -r`), avant toute affectation ; le texte des définitions et des critères est celui de la première écriture.

## Trace

- Première écriture des définitions : 2026-11-03 à 14:54:21 UTC (`date -u -r`), sha256 de ce premier état `6672c5d40b1a28b2dabe067c25b1932e5fec4dcd8cbc1dc637e2a5858c72332f`.
- Ligne d'heure corrigée : 14:54:42 UTC (`date -u -r`). Partie « Définitions » figée à cet instant : les 4705 premiers octets de ce fichier (53 lignes, jusqu'à `<!-- fin des définitions -->` compris), sha256 `eb06663bfe8275a32f0a4448142e567fd96d76d2e9b58be78f4f150d76e35481`. Contrôle : `head -c 4705 groupes-ensemble-v1.md | sha256sum`.
- Affectations, effectifs, limites et trace ajoutés ensuite en fin de fichier (heure en tête de « Affectations »), sans toucher aux 4705 premiers octets.
- Fichier compagnon : `groupes-ensemble-v1.json`, mêmes groupes (définition sur deux lignes séparées par un saut de ligne) et mêmes affectations ; « second_choix » y vaut le nom du groupe ou `null`.
