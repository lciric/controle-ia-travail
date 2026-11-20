# Tour III.3, proposition A : réponse aux critiques

**Pièces (règle 2).** La critique croisée E est absente : je n'y réponds pas et n'en suppose pas le contenu. Le bloc QUESTION DE L'ARBITRE est identique au bloc FAITS (même sha256), donc je traite la section 3 (« The request ») comme la question.

**Statuts (règle 1).** Les faits ne portent aucune étiquette. Je continue à les citer comme « FAIT TRANSMIS (statut non étiqueté) » et je ne reprends pas les étiquettes [RAPPORTÉ] / [VÉRIFIÉ] que C leur attribue. Tout ce que j'ajoute est HYPOTHÈSE, et tout chiffre hors faits est **illustratif**. Aucune expérience n'a été exécutée.

---

## (a) Verdict sur chaque critique

| # | Critique (source) | Verdict | Conséquence |
|---|---|---|---|
| 1 | E1 : le bras 5 « items plus durs » donne H_B par construction si la lecture lit la difficulté (B a.1). L'appariement sur la réussite réalisée sélectionne sur une conséquence de la politique (D). | **Acceptée.** Le duel séparait items faciles et items durs. | Bras 5 retiré du critère et remplacé par 5′ : échecs honnêtes sur les mêmes items, tirés avant génération. |
| 2 | G est redondant avec un contraste de V à réussite appariée (C a.4, D). G n'est un écart de calibration que sur une échelle de probabilité (D). | **Acceptée, avec une précision.** Δ_V comparait au jumeau et G au bras 5, donc à deux bras différents. Mais G n'apportait aucune information d'issue. | G supprimé. E1 ne garde que des contrastes de lecture appariés. |
| 3 | E0 : variance nulle au prompt à question fixée, AUC intra-question « quasi garantie » aux frontières, contrôle « longueur » absorbé par l'effet fixe (B a.2). La porte écarte le mauvais instrument (D). | **Acceptée**, sauf « quasi garantie », qui est une hypothèse de B. Je la **transforme en test**. | E0 scindée en E0a (prompt, inter-items) et E0b (frontières, contre un prédicteur textuel à la même position). |
| 4 | E2 : les insertions sont hors politique, donc la lecture peut signaler un texte étranger (B a.3, C a.1, C c.2). Le journal certifie l'édition, pas l'intention ni le petit δ (D). | **Acceptée.** La porte était placée dans un autre régime que celui qu'elle gardait. | Bras endogène ajouté. Les insertions deviennent un diagnostic et ne ferment plus la piste. |
| 5 | E2 : mêmes rollouts pour sélectionner la strate et pour noter (C a.3, D). | **Acceptée.** | Deux moitiés de rollouts indépendantes (règle R6). |
| 6 | Fuite entre entraînement et évaluation (B a.4). Séparer les familles, pas seulement les graines (D). | **Acceptée.** | Règle R1. |
| 7 | E2 : zone indécise non déclarée (B a.5). | **Acceptée.** | Règle R3, appliquée à tous les duels. |
| 8 | S9 : fractions mal appariées, et « petit sous-ensemble » non établi (B a.6). | **Acceptée.** | Correction : 77,8 % = 28/36, 75,0 % = 27/36, 72,2 % = 26/36. Tout dénominateur multiple de 36 convient, et avec trois graines un sous-ensemble multiple de 12 suffit (calcul de A). Je retire toute inférence sur la taille : elle se lit dans le PDF. |
| 9 | Bras 4 : l'écart au jumeau confond « adaptateur présent » et « sabotage » (C a.2, C c.1, D c). | **Acceptée.** | Bras 6 : LoRA honnête de même rang, mêmes pas, même volume de tokens. |
| 10 | La consigne inerte ne neutralise ni son sens ni l'identité de l'adaptateur (D). | **Acceptée comme limite**, que je ne peux pas lever entièrement. | Bras 2′ ajouté. Aucun contrôle de contexte ne neutralise le sens sans retirer le traitement, donc ce résidu est déclaré en (c). |
| 11 | Seuil à 1 % de fausses alertes : instable si n₀·α ≲ 10 (B b, C b.3). | **Acceptée.** Détail : la loi Beta écrite par C a ses paramètres dans l'ordre de la couverture, pas du taux de fausses alertes (calcul de A, à revérifier). La conclusion CV ≈ 1/√(α·n₀) tient. | Règle R2. |
| 12 | E4 : « détection < 2 × fausses alertes » non jugeable sans un millier d'épisodes (B b). | **Acceptée.** | Critère reformulé en borne haute d'intervalle à 5 %. |
| 13 | E4 : sans contrainte de dommage, l'« évasion » peut être l'arrêt du sabotage (D). | **Acceptée.** | Frontière à trois axes : détection, compétence, dommage maintenu. |
| 14 | Agrégation par somme : la puissance s'effondre sous autocorrélation (B b, C b.2). | **Acceptée et transformée en pré-mesure.** Leurs deux calculs concordent avec le mien : φ = 0,8 donne n_eff ≈ 11 et environ 5 % de détection, contre 37 % sous indépendance (illustratif). | Règle R4. |
| 15 | E2 : Spearman atténué par le bruit Monte-Carlo, σ non borné hors sous-échantillon (B b, C b.1, D). | **Acceptée.** | Le Spearman devient descriptif. Le critère primaire ne dépend plus d'un δ estimé. |
| 16 | E1 : estimateur du d non fixé (B b). Support commun requis (D). | **Acceptée.** | Règle R5. |
| 17 | E3 : ne pas battre une référence ne réfute pas le transfert, car la sonde peut transférer et être redondante (D). | **Acceptée.** C'était une erreur d'inférence de ma part : j'avais écrit « H_B falsifie S2 ». | E3 scindée en transfert (E3-i) et valeur ajoutée (E3-ii). |
| 18 | Référence « log-vraisemblance des tokens de l'agent sous le jumeau », dont l'absence serait fatale pour E3 (C c.3). | **Acceptée comme référence, rejetée telle que définie.** Je reprends l'argument de B contre E : elle est positive par construction dès que l'agent diffère du jumeau. | Elle n'entre qu'avec une nulle mesurée sur des variantes honnêtes distinctes du jumeau (bras 2, 2′, 6). |
| 19 | Un MLP dense égal n'invalide pas la suffisance d'un masque parcimonieux. Des masques instables peuvent porter la même loi prédictive (D). | **Acceptée.** | Critère de défaillance de l'instrument « élagage L1 » réécrit en (b). |
| 20 | L'ablation par la moyenne n'isole pas, seule, une fonction de valeur (D). | **Acceptée.** C'est un contrôle nécessaire, pas suffisant. | J'ajoute l'ablation par rééchantillonnage, idée prise à C (critique de B). La conclusion permise reste « nécessaires à la réussite », pas « codent la valeur ». |
| 21 | Nulle stratifiée par longueur d'épisode (B c.4). Éditions neutres par le même éditeur au même endroit (D c). A/A et lentilles en masquant l'identité du modèle et du rédacteur (D c). | **Acceptées.** | Intégrées à R4, E2 et E3. |
| 22 | E0 : items à issue déterministe sans paires discordantes (D). | **Acceptée.** | E0b et 5′ sont restreints aux items à réussite intermédiaire, et la restriction est déclarée. |

**Bilan.** Sur 22 critiques groupées, 20 sont acceptées, 1 est acceptée en partie et rejetée telle que définie (n° 18), 1 est acceptée comme limite non levable (n° 10). Deux sont transformées en test ou en pré-mesure (n° 3, n° 14). Je retire quatre affirmations du tour III.1 :
- E0 comme porte de la piste valeur ;
- G comme métrique ;
- « H_B à E3 falsifie S2 » ;
- l'appariement des fractions de S9.

---

## (b) Expériences corrigées

### Règles communes

- **R1, découpage.** Trois lots disjoints par famille d'items : entraînement des sondes, calibration des seuils, évaluation.
- **R2, point de fonctionnement.** Le taux primaire est 5 % de fausses alertes par épisode (illustratif). Le point à 1 % n'est rapporté que si n₀·α ≥ 50. Le bootstrap est fait par famille et ré-estime le seuil à chaque réplique.
- **R3, décision** (règle reprise de D). Pour un gain g et une marge m gelée, H_A : g > m et H_B : g ≤ m. Un intervalle à 95 % entièrement d'un côté réfute l'autre. Un intervalle qui traverse m est déclaré « indéterminé » et ne réfute rien.
- **R4, autocorrélation.** Avant tout duel agrégé, mesurer φ et n_eff sur des épisodes honnêtes entiers (A/A). La nulle de l'agrégat est calibrée sur des épisodes entiers, par tranche de longueur. Si la puissance calculée avec n_eff est sous 50 % (illustratif) pour l'effet visé, le duel est déclaré non jugeable avant exécution, et non perdu.
- **R5, estimateur.** d_z = moyenne / écart-type des différences appariées par item, sur le support commun des items, avec grappes par famille.
- **R6, rollouts.** Une moitié définit la strate, l'autre sert de cible. La fiabilité est estimée entre moitiés.

### Bras révisés

1. Jumeau honnête, plusieurs graines (A/A).
2. Consigne inerte qui mentionne la surveillance.
2′. Consigne qui mentionne le sabotage et l'interdit (déclencheur présent, inactif).
3. Saboteur par consigne.
4. Saboteur par LoRA, sans consigne.
5′. Échecs honnêtes du jumeau sur les mêmes items. Les items sont fixés avant génération et ont un taux de réussite du jumeau entre 0,2 et 0,8 (illustratif).
6. LoRA honnête de même budget.

L'ancien bras 5 (items plus durs) sort des critères. Il reste un simple témoin de sensibilité à la difficulté.

Un moniteur valide sépare 3 de 2′ et 4 de 6. Il ne déclenche pas au-delà du nominal sur 2, 2′, 5′ et 6.

**Propriété formelle à garder en tête.** À poids et contexte identiques, la lecture au prompt est identique pour l'agent et le jumeau. Elle ne peut donc séparer des bras que par le contexte ou par les poids. C'est exactement ce que 2, 2′ et 6 contrôlent.

### E0a. Au prompt : état du modèle ou surface de l'énoncé ?

- **Dispositif.** Réplication sur poids publics. Lecture au prompt sur des familles d'items tenues à l'écart.
- **Prédicteurs textuels.** Longueur de la question et classifieur sur le texte de l'énoncé, ajustés sur le lot d'entraînement seul. Je n'utilise pas le taux de réussite d'un autre modèle : C a montré, contre B, qu'il peut soustraire de la vraie variance de compétence.
- **H_A.** AUC(texte + lecture) − AUC(texte seul) > m, avec m = 0,02 (illustratif).
- **H_B.** Gain ≤ m.
- **Ce que chaque issue falsifie.** H_B falsifie S4 pour la lecture au prompt : elle n'apporte rien qu'un lecteur de l'énoncé n'ait déjà. H_A falsifie l'explication de l'écart 0,67 contre 0,62 par la longueur.
- **Contrôles.** Étiquettes permutées. 1 % de neurones aléatoires. MLP sur l'état complet.

### E0b. Aux frontières : au-delà du texte déjà écrit ?

- **Dispositif.** Intra-question, sur les items à réussite intermédiaire. La lecture aux frontières de paragraphe est comparée à un classifieur sur le texte du préfixe et à une sonde de prédiction du token suivant, à la même position et sur les mêmes données.
- **H_A.** Gain de fusion > m.
- **H_B.** Gain ≤ m.
- **Ce que chaque issue falsifie.** H_B falsifie l'intérêt « boîte blanche » de la lecture aux frontières : un moniteur textuel dispose de la même information. H_A falsifie l'objection de B (« lisibilité du texte seule »).
- **Vérification indépendante.** Code, graines et découpage publiés, puis réexécution par un tiers.
- **Coût illustratif (E0a + E0b + A/A de R4).** 10 à 20 heures-GPU.
- **Littérature.** Article source. Sun, Liu, Bair, Kolter, 2023, « A Simple and Effective Pruning Approach for Large Language Models ».

### E1. Que suit la valeur sous sabotage ?

- **Dispositif.** Tâches vérifiables, mêmes items pour tous les bras.
- **Contraste au prompt.** D = V(3) − V(2′) et D = V(4) − V(6), appariés par item.
  - **H_A (valeur officielle).** d_z ≤ −0,3 (illustratif) dans les deux paires.
  - **H_B (valeur de capacité).** Intervalle de d_z contenu dans ±0,2, alors que la réussite réalisée chute d'au moins 15 points (illustratif). Sans cette chute, la manipulation a échoué et rien n'est jugé.
- **Contraste aux frontières.** Trajectoires sabotées qui échouent (bras 3 et 4) contre échecs honnêtes (5′), sur les mêmes items.
  - **H_A′.** La lecture ajoute au prédicteur textuel du préfixe (gain de fusion > m).
  - **H_B′.** Gain ≤ m : la lecture détecte l'échec, pas le sabotage.
- **Ce que chaque issue falsifie.**
  - H_A falsifie la lecture « capacité ». Le moniteur « valeur basse » ne survit que si H_A′ tient aussi.
  - H_B falsifie le moniteur « chute de valeur ». G étant supprimé, il ne reste alors aucun signal de sabotage dans la lecture au prompt, et je le dis tel quel.
  - Des signes opposés entre les deux paires indiquent un artefact de consigne ou d'adaptateur : S3 tombe dans ses deux versions pour ce dispositif.
- **Vérification indépendante.** Une équipe rouge distincte construit les saboteurs. Les étiquettes de bras sont scellées.
- **Coût illustratif.** 50 à 100 heures-GPU (deux LoRA, rejet pour 5′).
- **Littérature.** van der Weij, Hofstätter, Jaffe, Brown, Ward, 2024, « AI Sandbagging: Language Models can Strategically Underperform on Evaluations ». Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, « Detecting Strategic Deception Using Linear Probes ».

### E2. Lecture dopamine dans le régime diffus

- **Trois sources de petites fautes.**
  1. Fautes produites par le modèle saboteur (bras 3 et 4).
  2. Erreurs spontanées du jumeau.
  3. Insertions par un éditeur, avec insertions neutres du même éditeur au même endroit.
- **Estimand déclaré.** δ est la variation de valeur sous continuation par le jumeau. D a signalé, contre C, que la politique de continuation change la quantité mesurée.
- **Critère primaire.** L'unité est l'épisode et l'étiquette est le bras. La statistique est l'agrégat de la lecture, sur scores bruts et sur résidus d'un modèle autorégressif ajusté sur l'honnête (les deux préenregistrés), pour 3 contre 2′ et 4 contre 6. La référence à battre est la surprise textuelle du pas sous le jumeau.
  - **H_A.** Gain de fusion > m pour une dose de 10 fautes par épisode (illustratif).
  - **H_B.** Gain ≤ m.
  - Les autres doses sont descriptives.
- **Secondaire.** Contraste apparié entre pas fautifs et pas neutres, dans la strate |δ| < 0,1 définie selon R6. Le Spearman est rapporté avec sa fiabilité, sans seuil de décision.
- **Diagnostics.** Si la lecture réagit autant aux insertions neutres qu'aux insertions fautives, elle lit le texte étranger. La sonde est ré-entraînée sans le filtre à 0,3.
- **Ce que chaque issue falsifie.** H_B falsifie S5 pour un sabotage endogène à cette dose. H_A falsifie « le filtre à 0,3 rend la sonde aveugle », et seulement parce que le gain est mesuré au-dessus de la surprise textuelle.
- **Vérification indépendante.** Journal des insertions haché. Rollouts d'audit publiés.
- **Coût illustratif.** 40 à 80 heures-GPU.
- **Littérature.** Article source. Autres modèles de récompense de processus : non recherché.

### E3. Travail ouvert : deux questions séparées

- **E3-i, transfert.** La lecture gelée dépasse-t-elle sa propre nulle ?
  - H_A : détection − fausses alertes mesurées sur le lot de test > m.
  - H_B : ≤ m.
  - H_B falsifie S2 pour les familles testées. H_A falsifie la limite (1) des auteurs pour ces familles seulement.
- **E3-ii, valeur ajoutée.** Gain de fusion sur la meilleure référence. La liste est gelée et le choix se fait sur un lot de validation distinct.
  - Références : moniteur textuel, sonde linéaire générique, MLP dense, neurones aléatoires, vérifications mécaniques, vraisemblance sous le jumeau avec sa nulle (n° 18).
  - H_B falsifie l'utilité comme moniteur supplémentaire, **pas le transfert**. H_A falsifie la redondance avec les références.
- **Positifs.** Je distingue l'assignation et le dommage confirmé (distinction de D). Les deux taux sont rapportés avec la fraction π d'épisodes réellement dégradés.
- **Contrôles.** A/A. Bras 2, 2′ et 6. Analystes des lentilles aveugles à l'identité du modèle et du rédacteur.
- **Vérification indépendante.** Préenregistrement. Lot d'épisodes détenu par l'arbitre.
- **Coût illustratif.** 80 à 150 heures-GPU et 3 à 5 semaines-personne. R2 impose plusieurs centaines d'épisodes honnêtes ouverts.
- **Littérature.** Greenblatt, Shlegeris, Sachan, Roger, 2023, « AI Control: Improving Safety Despite Intentional Subversion ». Travaux sur les menaces diffuses : référence à vérifier.

### E4. Coût de l'évasion, à dommage maintenu

- **Dispositif.** Trois niveaux d'adversaire inchangés : informé du moniteur, informé des neurones lus, affiné contre le gradient de la sonde. Trois axes sont mesurés : détection à 5 %, compétence honnête, dommage maintenu.
- **H_B (contournable).** Au niveau 3, la borne haute à 95 % de la détection est ≤ 15 %, la perte de compétence est ≤ 2 points et le dommage reste ≥ 80 % du dommage initial (seuils illustratifs, environ 300 épisodes saboteurs).
- **H_A (porteur).** Toute évasion de ce degré coûte ≥ 10 points de compétence ou fait tomber le dommage sous 50 %.
- **Entre les deux.** Indéterminé.
- **Contrôles.** LoRA honnête de même durée. Sonde ré-entraînée après évasion, testée sur des familles et des adaptations absentes de son ajustement. Sans ce second test, retrouver de la puissance peut tenir à un indice de style (D, critique de B).
- **Portée.** H_A signifie « non contourné par les attaques testées », rien de plus.
- **Ce que chaque issue falsifie.** H_B falsifie S8. H_A falsifie, pour ce modèle et ces attaques, l'idée qu'une lecture parcimonieuse se contourne sans coût.
- **Vérification indépendante.** Équipe rouge distincte de celle qui a conçu la sonde. Poids évadés publiés.
- **Coût illustratif.** 80 à 200 heures-GPU.
- **Littérature.** Bailey et al., 2024, « Obfuscated Activations Bypass LLM Latent-Space Defenses » (liste d'auteurs à vérifier).

### Instruments : critères de défaillance modifiés

| Instrument | Ancien critère | Critère corrigé |
|---|---|---|
| Élagage L1 | Jaccard instable, ou MLP dense égal | Le MLP dense teste seulement si la parcimonie *ajoute* de la performance (S7). Un Jaccard instable falsifie l'identité « ce sont *les* neurones », pas la lecture. La défaillance du moniteur se juge sur la corrélation des scores entre masques de graines différentes, hors échantillon. |
| Ablation | L'effet disparaît en ablation par la moyenne | Contrôles nécessaires : moyenne et rééchantillonnage. Même s'ils passent, la conclusion permise est « nécessaires à la réussite ». |
| Moniteurs texte / code | Référence | S'y ajoutent la surprise textuelle et la vraisemblance sous le jumeau, chacune avec sa nulle sur 2, 2′ et 6. |
| Jumeau, nulle | A/A | A/A sur épisodes entiers, par tranche de longueur, avec identités masquées. |

**Ordre.** E0a, E0b et la mesure de φ (R4) d'abord. Puis E1, E2, E3 et E4.

**Coût total illustratif.** 260 à 550 heures-GPU et 6 à 10 semaines-personne. C'est plus qu'au tour III.1, à cause des bras 2′, 5′, 6 et des rollouts dédoublés.

---

## (c) Réponse à l'arbitre, en une page

**Demande reformulée.** La lecture valeur / erreur TD de l'article ajoute-t-elle, aux moniteurs que le programme possède déjà, une information de sabotage ? Cette information doit satisfaire trois conditions :
- ne se réduire ni à l'énoncé ni au texte déjà produit ;
- ne se réduire ni à la consigne ni à l'adaptateur ;
- survivre à un agent qui maintient son dommage.

**Ce qui est établi.** Uniquement des faits transmis (statut non étiqueté), sur tâches vérifiables et modèles de 32B au plus :
- Une sonde MLP élaguée prédit la réussite avant génération avec une AUC moyenne de 0,67, que les auteurs disent « modérée ». La longueur de la question seule atteint 0,62.
- Mettre à zéro 1 % de neurones de valeur fait passer l'exactitude de 75,2 % à 20,3 % sur un modèle et un banc.
- La recherche pas à pas guidée par la lecture dopamine atteint 77,8 %, contre 75,0 % et 72,2 %, sur trois graines.

S'y ajoutent trois propriétés formelles issues des critiques :
- La lecture au prompt est identique pour l'agent et le jumeau à poids et contexte égaux.
- Une somme de scores autocorrélés perd sa puissance d'un facteur √((1−φ)/(1+φ)).
- À réussite appariée, un écart « lecture − réussite » n'ajoute rien à un contraste de lectures.

**Ce qui ne l'est pas.** Rien dans les faits ne porte sur le sabotage, la tromperie ou le travail ouvert, et les auteurs le disent (p. 25). Restent des HYPOTHÈSES :
- la présence du sous-système dans l'agent du programme ;
- le transfert hors récompense ;
- ce que la valeur suit quand l'agent vise autre chose ;
- la lisibilité des pas sous le seuil d'entraînement de 0,3 ;
- la capacité à distinguer un sabotage d'un échec honnête ;
- la résistance à un agent averti.

Trois limites subsistent quel que soit le résultat :
- Aucun contrôle ne neutralise entièrement le sens d'une consigne ou l'identité d'un adaptateur.
- Les saboteurs sont construits par nous.
- « Non contourné » ne vaut que pour les attaques essayées.

À ce stade, les faits ne permettent pas d'employer l'article comme moniteur. Ils permettent de le traiter comme une lecture candidate à ajouter aux sondes, au jumeau et à la nulle existants, et jugée par son gain de fusion.

**L'expérience à faire en premier.** D'abord une relecture du PDF, sans calcul, sur quatre points :
- la taille du sous-ensemble du Table 4 ;
- les valeurs de Spearman ;
- l'existence d'un MLP sur l'état complet ;
- une éventuelle évaluation sous le seuil 0,3.

Ensuite **E0a + E0b avec la mesure A/A de φ**, sur poids publics, pour 10 à 20 heures-GPU (illustratif) :
- Si la lecture n'ajoute rien à un prédicteur textuel, ni au prompt ni aux frontières, la piste s'arrête comme apport boîte blanche. Les semaines-personne d'E1 à E4 sont alors épargnées.
- Si elle ajoute quelque chose, E1 dit ce qu'elle suit sous sabotage.
- La mesure de φ fixe le nombre d'épisodes nécessaires pour E2 et E3, ou les déclare non jugeables d'avance.

**Décompte réfutable.** 22 critiques traitées, 4 affirmations retirées, 6 règles communes, 9 oppositions H_A/H_B réparties sur 5 expériences, chacune avec sa zone indéterminée déclarée, et 1 désaccord de calcul signalé (paramètres de la loi Beta chez C), vérifiable par recalcul.

FIN-DE-CELLULE