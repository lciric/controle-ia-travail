# Groupes des fiches « Jang et Feng » — version 1

Question des mentors (Shi Feng, Eyon Jang) : que valent les moniteurs et les méthodes d'audit en boîte blanche (lecture des activations, sondes, autoencodeurs épars), et quelles sont leurs limites actuelles ?

Entrée : `/home/claude/scratch/soir-rapport/jang-feng/piste/fiches-a-grouper-v1.json` (sha256 `ffa495ee97c3cd0afca35cc109c57a5914cc08da325506b0ad10399e658ff944`, vérifiée), 29 fiches.
Groupeur neuf, aveugle au classement.

## 1. Définitions des groupes

Écrites le 2026-11-03 à 17:21 UTC (heure de `date -u`), après lecture des fiches et **avant toute affectation**. Elles ne sont pas modifiées ensuite. Chaque groupe est une affirmation sur la valeur ou les limites que la réponse aux mentors soutiendrait ; une fiche en relève si elle teste cette affirmation, dans un sens ou dans l'autre.

### G1 — Calibrage de référence
Définition : le taux de fausses alertes et la sensibilité d'une sonde dépendent davantage de la distribution bénigne qui fixe son seuil ou son centrage que de la sonde elle-même ; hors domaine, hors recette ou hors politique, ils se dégradent.
Une référence bénigne propre au déploiement, sans aucun exemple positif, en rétablirait une grande part.
Critère : la fiche fait varier ou corrige la **source de la référence bénigne** (domaine, recette d'entraînement, politique) et prédit l'effet sur les fausses alertes, la sensibilité ou la sûreté.

### G2 — Corrélat ou variable
Définition : une sonde ou un trait qui discrimine peut lire un corrélat — la trace textuelle ou verbalisée, la recette d'entraînement, une séparabilité de distribution — plutôt que la variable qui produit le comportement.
L'aire sous la courbe ne dit donc ni la valeur causale de la direction, ni son transfert, ni son apport au-delà du texte.
Critère : la fiche oppose la **discrimination apparente** d'une sonde à un contrôle qui retire ou fait varier un corrélat (verbalisation ou moniteur texte fort, recette ou étiologie, plancher de directions aléatoires, intervention causale sur la direction).

### G3 — Accumulation
Définition : contre les menaces diffuses, la valeur d'une sonde vient de l'agrégation : un signal faible par action devient utile cumulé sur un épisode ou entre tâches (macro-protocole bayésien).
Cela suppose des scores peu corrélés entre tâches et avec les scores texte, et un seuil calibré sur des épisodes honnêtes entiers.
Critère : la métrique décisive porte sur un **agrégat de scores** (cumul séquentiel, macro-protocole, cumul contre maximum local) et la fiche fait varier la règle d'agrégation ou ce qui la rend efficace ; non sur une décision action par action.

### G4 — Adversaire informé
Définition : face à un modèle ou une entrée qui s'adapte au moniteur, la valeur de la boîte blanche dépend de l'information et de l'accès dont dispose l'adversaire (retour de verdicts, injection visant le moniteur).
Sans retour de verdict la sonde résisterait ; avec verdicts ou injection elle se dégrade ; lire le composant fiable plutôt que le non fiable peut contourner l'attaque.
Critère : la fiche place un **adversaire qui cherche à tromper le moniteur** (évasion en contexte, retouche des activations, injection) et fait varier l'information disponible ou la cible de lecture.

### G5 — Perturbation et témoin bénin
Définition : les méthodes qui perturbent le modèle (bruit de poids ou d'activations, affinage court, démonstrations) font réapparaître une capacité cachée, mais ne séparent la sous-performance délibérée de la sous-élicitation bénigne qu'une fois rapportées à un témoin bénin apparié.
La forme de la réponse (dose, pente initiale, localisation, nombre de démonstrations) porterait le signal du verrou, ou seulement une marge de capacité.
Critère : la fiche mesure une **récupération de performance sous perturbation** et la compare (ou prédit qu'elle ne se distingue pas) à celle d'un témoin bénin apparié.

### G6 — Interprétation par l'auditeur
Définition : les traits d'autoencodeurs épars et leurs descriptions sémantiques apporteraient une valeur d'audit propre — localiser et expliquer un comportement caché pour un auditeur — distincte de la discrimination par sonde.
Elle se mesure par la performance d'auditeurs aveugles (descriptions contre identifiants anonymes) ou par la reproduction du comportement en pilotant un petit ensemble de traits.
Critère : la mesure décisive de la fiche est **l'aide apportée à un auditeur** par les traits ou leurs descriptions, ou la localisation d'un comportement dans des traits qui l'expliquent.

## 2. Affectations

Faites après l'écriture des définitions ci-dessus (section 1 inchangée). Une fiche, un groupe (son idée principale) ; « second choix » quand une fiche relève presque autant d'un autre groupe. Fichier machine : `groupes-v1.json`.

| Fiche | Groupe | Raison | Second choix |
|---|---|---|---|
| JF-01 | G1 Calibrage de référence | La variable manipulée est la référence bénigne : le centrage propre à la recette déployée rétablit le gain perdu hors recette. | G3 Accumulation |
| JF-02 | G4 Adversaire informé | L'affirmation centrale est la survie de la sonde à l'évasion en contexte quand aucun verdict n'est rendu au modèle. | G1 Calibrage de référence |
| JF-03 | G2 Corrélat ou variable | Oppose l'aire en distribution à l'effet causal spécifique comme critère de choix d'une sonde qui transfère à une autre étiologie. | — |
| JF-04 | G4 Adversaire informé | Sonde sur les activations du moniteur fiable contre une injection qui vise sa note texte. | — |
| JF-05 | G1 Calibrage de référence | Sonde fixée, seul change le corpus de calibrage (Alpaca contre épisodes honnêtes du domaine) ; effet prédit sur les fausses alertes. | — |
| JF-06 | G1 Calibrage de référence | La variable manipulée est le domaine d'estimation de la loi des scores honnêtes, en domaine ou hors domaine. | G3 Accumulation |
| JF-07 | G4 Adversaire informé | La sensibilité du moniteur est prédite en fonction du nombre de verdicts exacts vus en contexte par le modèle surveillé. | — |
| JF-08 | G6 Interprétation par l'auditeur | La mesure finale est la valeur des descriptions de traits pour diagnostiquer un verrou ; le bruit ne sert qu'à fabriquer l'événement à expliquer. | G5 Perturbation et témoin bénin |
| JF-09 | G6 Interprétation par l'auditeur | Chaîne saut, traits déplacés, pilotage et descriptions aidant des auditeurs aveugles ; l'apport propre est la localisation et l'explication. | G5 Perturbation et témoin bénin |
| JF-10 | G5 Perturbation et témoin bénin | Saut sous affinage court rapporté à des témoins bénins sous-élicités, là où juge boîte noire et sonde passive échouent. | — |
| JF-11 | G2 Corrélat ou variable | Teste si la sonde apporte plus qu'un prédicteur fondé sur tout le texte, sur les réponses non verbalisées. | — |
| JF-12 | G2 Corrélat ou variable | Les traits suivraient la verbalisation du contexte (corrélat) plutôt que l'état de suppression de l'exploration. | — |
| JF-13 | G3 Accumulation | La mesure décisive est l'interaction cumul sur l'épisode contre maximum local, à risque par épisode égal. | G2 Corrélat ou variable |
| JF-14 | G1 Calibrage de référence | Centrer sur une référence bénigne propre à chaque recette, sans exemple positif, pour corriger le transfert hors recette. | — |
| JF-15 | G2 Corrélat ou variable | Direction fortement prédictive sans effet causal au-delà de directions aléatoires appariées. | — |
| JF-16 | G6 Interprétation par l'auditeur | Descriptions contre identifiants anonymes pour des auditeurs aveugles, à information et temps identiques. | — |
| JF-17 | G2 Corrélat ou variable | Corrélation au rang entre effet causal de l'ablation et transfert à un organisme d'une autre étiologie. | — |
| JF-18 | G2 Corrélat ou variable | La recette, pas seulement le comportement, fixerait ce que lit la sonde : corrélat de recette. | G1 Calibrage de référence |
| JF-19 | G5 Perturbation et témoin bénin | Bruit localisé balayé en dose contre témoin bénin apparié au même score de départ, et contre bruit uniforme. | — |
| JF-20 | G3 Accumulation | Cumul des scores contre maximum local, seuil calibré sur trajectoires bénignes entières. | — |
| JF-21 | G3 Accumulation | Filtre d'accumulation séquentielle sur scores de sonde contre le même cumul sur un moniteur texte. | — |
| JF-22 | G2 Corrélat ou variable | Plancher de directions aléatoires appariées en covariance pour retirer la séparabilité, selon que l'organisme verbalise ou non. | — |
| JF-23 | G3 Accumulation | Le gain dans le macro-protocole suivrait la décorrélation entre tâches des scores, non la valeur causale. | G2 Corrélat ou variable |
| JF-24 | G3 Accumulation | Ajout d'une sonde au macro-protocole bayésien, gain attribué à la moindre corrélation entre tâches. | — |
| JF-25 | G2 Corrélat ou variable | Le gain « sonde plus texte » ne subsisterait que sur les épisodes verbalisés : la sonde lirait la trace textuelle. | — |
| JF-26 | G5 Perturbation et témoin bénin | Pente initiale et gain maximal d'une dose–réponse de bruit contre un témoin sous-élicité par invite. | — |
| JF-27 | G5 Perturbation et témoin bénin | Gain par démonstrations rapporté à celui d'un témoin bénin de même famille. | — |
| JF-28 | G5 Perturbation et témoin bénin | Prédit que le bruit ne se distingue pas d'un témoin bénin apparié : il lirait une marge de capacité, pas l'intention. | — |
| JF-29 | G5 Perturbation et témoin bénin | Score de récupération corrigé par la récupération attendue d'un témoin bénin, contre le gain brut. | — |

Effectifs : G1 = 4 ; G2 = 8 ; G3 = 5 ; G4 = 3 ; G5 = 6 ; G6 = 3 ; total 29, aucune fiche hors groupe.
Fiches à second choix (8) : JF-01, JF-02, JF-06, JF-08, JF-09, JF-13, JF-18, JF-23.

## 3. Limites

1. **Aveugle au classement, pas au contenu.** Les définitions ont été écrites après lecture des 29 fiches (nécessaire pour qu'elles les couvrent) : risque que les groupes épousent les fiches plutôt que la question. Elles ont toutefois été posées sur disque avant toute affectation et n'ont pas été retouchées.
2. **G2 est large.** Il réunit trois sous-affirmations : « lisible n'est pas causal » (JF-03, JF-15, JF-17), « apport au-delà du texte ou de la verbalisation » (JF-11, JF-12, JF-22, JF-25) et « corrélat de recette » (JF-18). Le mécanisme commun (la sonde lit un corrélat, non la variable) justifie la fusion ; les séparer aurait donné 7 groupes, au-delà du plafond de 6. La réponse aux mentors gagnerait peut-être à les distinguer.
3. **G1 contre G2 sur le transfert entre recettes.** JF-14 (déplacement des activations bénignes, corrigible par centrage) et JF-18 (chemins internes différents) sont deux explications rivales du même défaut ; la frontière suit le mécanisme invoqué, non le phénomène observé. JF-01 et JF-14 sont presque redondantes.
4. **G1 contre G3 sur « épisodes entiers ».** Le calibrage sur épisodes honnêtes entiers apparaît dans les deux (JF-05, JF-20, JF-21). Règle appliquée : la source de la référence varie (domaine, recette, politique) → G1 ; la règle d'agrégation varie → G3. JF-01 et JF-06 sont mesurées dans le protocole d'accumulation mais manipulent la référence, d'où G1 avec G3 en second.
5. **G5 n'est pas entièrement boîte blanche.** Les démonstrations (JF-27) sont de l'élicitation boîte noire ; l'affinage court (JF-10) exige les poids mais ne lit pas les activations ; JF-29 est une correction de métrique. Le groupe répond donc à la question sur les limites de l'audit au sens large, pas seulement de la lecture des activations. Il contient aussi une fiche à signe négatif (JF-28) et une fiche qui teste en même temps la lecture rivale (JF-19).
6. **Fiches composites.** JF-08 et JF-09 enchaînent détection par perturbation, localisation dans des traits et aide aux auditeurs ; je les ai affectées à G6 d'après le point final et l'apport propre. Lues par leur première étape, elles relèveraient de G5.
7. **JF-23 pose une question de G2 dans le cadre de G3** (la valeur causale compte-t-elle dans l'accumulation ?) ; JF-13 a la symétrique (apport au-delà du texte, mesuré par le cumul).
8. **Redondances repérées, non traitées** (hors mandat) : JF-19 et JF-26 ; JF-09 et JF-10 ; JF-03 et JF-17 ; JF-01, JF-23 et JF-24 ; JF-13, JF-20 et JF-21 ; JF-05 et JF-06 ; JF-10, JF-27 et JF-29.
9. **Périmètre de lecture.** Seul le fichier d'entrée a été lu (avec la consigne). La routine de reprise du dépôt n'a pas été exécutée, la consigne interdisant toute autre lecture. Aucun outil n'a demandé d'approbation ; aucun appel réseau ni de modèle, aucun commit, aucun fichier `.sha256`.
