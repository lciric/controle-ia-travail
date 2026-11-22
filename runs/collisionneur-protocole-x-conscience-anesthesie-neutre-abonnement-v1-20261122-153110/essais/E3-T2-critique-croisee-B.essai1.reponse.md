# Proposition B — tour III.2 : critique croisée de méthode

**Pièces.** J'ai lu le fichier en entier. Les conceptions A, C, D, E et F sont présentes et complètes : chacune se termine par FIN-DE-CELLULE. Je n'ai pas recalculé les empreintes. Le bloc FAITS reproduit la QUESTION.

**Statuts et chiffres.** Chaque objection est une HYPOTHÈSE de méthode : aucune n'a été testée. Les propriétés statistiques que j'invoque sont des résultats classiques RAPPORTÉS, non revérifiés ici : unimodalité des mélanges, variance d'une AUROC ou d'une différence de corrélations, règle de trois. Tous les chiffres sont illustratifs. Ceux que je reprends d'une proposition sont ses propres seuils, qu'elle marque déjà illustratifs. Pour chaque contrôle de (c), une issue positive réfute le critère visé et une issue négative réfute mon objection (B4).

Étiquettes :
- **[conf]** : variable confondante ;
- **[constr]** : vrai par construction ;
- **[fuite]** : fuite entre la construction de l'instrument et son évaluation.

## Sur la proposition A

**(a) Défauts de méthode**
- **E1 [constr].** Un transformeur en inférence est déterministe. La « distribution des écarts sans perturbation » est donc un Dirac en 0. La binarisation n'a pas de loi nulle, et le témoin « perturbation de norme nulle → 0 case » ne peut pas échouer.
- **E1 [constr].** R5 retire les têtes « qui transportent l'information entre positions éloignées ». Or PCI-T compte les cases significatives en t′ > t : il compte ce que la lésion retire. Une AUROC(R5 contre R4) élevée est attendue sans rien dire de la transposition.
- **E1 [conf].** R3 conserve les valeurs singulières de chaque matrice, mais pas le gain de leur produit : ‖W₂W₁‖ dépend de l'alignement entre V₂ et U₁, que le tirage détruit. R1 et R3 peuvent donc se séparer par le seul gain de bout en bout. Les jumeaux iso-spectraux de C et d'E ont le même défaut.
- **E1 [conf].** Le R² d'un scalaire calculé « sur R1–R6 » dépend de la dispersion du plan choisi. Inclure R2 et R3 gonfle la variance entre groupes et rend R² ≥ 0,9 accessible par ce seul contraste.
- **E1, pseudo-réplication.** Il n'y a qu'un réseau entraîné par architecture. Les 200 textes × 20 sites sont des répétitions de ce réseau ; une AUROC entre réseaux calculée sur ces sites est une pseudo-réplication. J'emprunte ici la règle de D, qui interdit de compter les jetons comme des configurations indépendantes.
- **E3 [constr].** À texte imposé, une intervention en couche ℓ laisse les couches inférieures à ℓ exactement intactes.
  - Si la sonde lit ces couches, sa puissance est nulle par construction.
  - Si elle lit l'aval, la précaution « couches non modifiées directement » est sans objet.
  - Le choix reste à fixer.
- **E4 [conf], rétrécissement ridge.** Quand le bruit augmente, la pénalité ridge choisie par validation croisée augmente. Elle rétrécit davantage l'espace de grande dimension (b3) que b2. Le rapport gain(b3)/gain(b2) baisse alors par l'estimateur, sans que le cerveau y soit pour rien.
- **E4 [conf], réponse hémodynamique.** Une réponse hémodynamique commune à tous les états confond l'état avec la modification du couplage neurovasculaire sous propofol.

**(b) Conditions de perte de puissance**
- **PCI-T.** L'indice devient non jugeable si la proportion p̂ de cases significatives sort de [ε, 1 − ε] : H(p̂) tend vers 0 au dénominateur et la variance du rapport diverge. De plus, la normalisation c·log n / n converge lentement : à n = L×T fini, un écart inférieur à son biais n'est pas interprétable.
- **Tests entre réseaux.** Avec n₁ et n₂ réseaux, la plus petite p-valeur unilatérale d'un test de rangs vaut 1/C(n₁+n₂, n₁). Pour 1 réseau contre 5, elle vaut 1/6.
- **E2.** La chute relative 1 − P(α)/P(0) n'a pas d'intervalle borné si l'intervalle de P(0) − hasard contient 0 (cas de Fieller).
- **E3.**
  - La borne 3/N suppose N tirages de Bernoulli indépendants. Si un épisode dure en moyenne m positions, la borne devient environ 3m/N.
  - Si les scores spontanés sortent du support de la loi d'entraînement (rapport de densités non borné), le taux de fausses alertes mesuré sur positions intactes n'estime pas celui des queues.
- **E4.** Quand la pente du gain en k est inférieure à son écart-type d'estimation, k̂* tend vers la plus petite fenêtre testée : le raccourcissement vient alors du rapport signal/bruit. Le rapport des gains est non jugeable dès que l'intervalle de gain(b2) contient 0.

**(c) Contrôles négatifs dont l'absence est fatale**
- **E1 : une loi nulle stochastique.** Perturbations de même norme dans des directions tirées au hasard, ou mêmes perturbations sur des entrées à jetons permutés.
- **E1 : une lésion ciblée de têtes à courte portée,** appariée en perte à R5.
- **E1 : un témoin aléatoire apparié en gain du jacobien de bout en bout,** et non en spectre matrice par matrice.
- **E4 : une « fausse sédation » tirée de la loi du bruit sous sédation.** Spectre et autocorrélation sont estimés sur le repos au même palier ; un bruit blanc de même niveau ne suffit pas.

## Sur la proposition C

**(a) Défauts de méthode**
- **Exp.1 [conf].** Local et global sont confondus avec la distance (3 jetons contre 150). Les « négatifs durs » du tableau (c) gardent ce confondant. Toute réduction de l'horizon effectif donne donc D > 0. E prévoit le croisement distance × type de règle qui manque ici.
- **Exp.1 [fuite].** Choisir les têtes par score d'induction ou de portée revient à un masque positionnel appris. L'exclusion des masques est ainsi contournée.
- **Exp.1 [conf].** Le témoin est apparié en norme L2 des logits. Or le softmax est invariant à l'ajout d'une constante aux logits : une part de cette norme est sans effet sur la sortie. Il faut apparier en KL ou en perte.
- **Exp.1, critère d'abolition.** « S_global indiscernable de 0 (p > 0,05) » prend un non-rejet pour une abolition. La règle favorise H_A1 à mesure que l'expérience devient moins précise. Il faut un test d'équivalence avec une marge fixée.
- **Exp.2 [fuite].** T_long est sélectionné sur la réduction de surprise d'un modèle de référence, c'est-à-dire sur l'issue.
  - Si la référence est le modèle testé, G_global est minoré et le mode bas est exclu : biais vers H_B2.
  - Si la référence est un modèle plus grand, les échecs du petit modèle forment un mode d'aptitude : biais vers H_A2.
- **Exp.2, réfutation de H_A2.** Régresser « les cas de faible G_global » sur des covariables revient à conditionner sur la variable dépendante. La variance expliquée sur cet échantillon tronqué est biaisée.
- **Exp.3, règle de décision.** La règle de (b) n'inclut pas le banc de moyennes glissantes proposé en (c). Le LLM à poids aléatoires ne le remplace pas : avec une attention presque uniforme, il moyenne tout le contexte et n'est pas apparié en autocorrélation au modèle entraîné.
- **Exp.3 [conf].** La base ne contient ni F0, ni pauses, ni marqueurs prosodiques de frontière. Les couches contextuelles peuvent alors capter une prosodie corrélée à la syntaxe.
- **Exp.3, charge de preuve asymétrique.** H_B3 tombe sur un seul couple couche × région parmi 16 × 200. H_A3 n'est réfutée qu'avec BF₀₁ ≥ 3 dans toutes les régions.
- **Exp.4 [constr].** La binarisation par quantile de (c) fixe la densité de chaque couche. Elle efface ainsi l'étendue de propagation, celle-là même qu'une lésion de l'intégration réduit. La définition de (b) et la correction de (c) ne mesurent pas la même chose.

**(b) Conditions de perte de puissance**
- **Exp.1.** λ* est le premier franchissement d'un seuil sur une courbe bruitée. Quand Var(Ŝ_global) augmente, λ̂* est biaisé vers le bas ; S_local y est alors plus haut, et D est biaisé vers le haut.
- **Exp.2, mélanges.** Un mélange π·N(μ₁, σ²) + (1 − π)·N(μ₂, σ²) a une densité unimodale si |μ₁ − μ₂| ≤ 2σ pour π = ½, et ce seuil croît quand π s'éloigne de ½. Un mode de 3 % peut exister sans bimodalité de la densité ; le test de Hartigan et Hartigan (1985, « The dip test of unimodality ») n'a alors aucune puissance.
- **Exp.2, dépendance.** La loi nulle du dip suppose des observations indépendantes. Les positions d'un même livre sont autocorrélées, donc la p-valeur est anticonservatrice. Enfin, une résidualisation linéaire sur une covariable discrète à effet non linéaire produit des résidus multimodaux sans changement de régime.
- **Exp.3.** Pour des corrélations faibles, Var(Δr̂) ≈ 2(1 − ρ)/n_eff, où ρ est la corrélation entre prédictions de base et complètes.
  - Détecter Δr = 0,025 (α unilatéral 0,01, puissance 0,8) exige N·n_eff/(2(1 − ρ)) ≥ (3,17/0,025)² ≈ 16 000.
  - Avec ρ = 0,9 et N = 15, il faut au moins 213 volumes indépendants par état et par sujet.
  - C'est plus que ce que fournit un récit de 5 à 8 minutes à TR de 2 s.
- **Exp.4.** Le test de DeLong suppose des unités indépendantes. Deux cents séquences d'un même réseau n'en sont pas pour une conclusion qui porte sur des réseaux.

**(c) Contrôles négatifs dont l'absence est fatale**
- **Exp.1 :** paires local-distant contre global-proche.
- **Exp.2 :** une cible fixe précédée d'historiques variés (le témoin d'E).
- **Exp.3 :** une base enrichie de F0 et de pauses, et le banc de lissage inscrit dans la règle de décision.
- **Exp.4 : le modèle entraîné sondé sur jetons permutés.** S'il s'écarte autant de lui-même que du jumeau iso-spectral, l'indice mesure l'adéquation entre l'entrée et le modèle, pas l'organisation du réseau.

## Sur la proposition D

**(a) Défauts de méthode**
- **Duel humain.** D ne précise pas si le décodeur est réentraîné à chaque palier, et R_bloc ≤ 0,2 change de sens selon la réponse.
  - Si le décodeur appris à la veille est appliqué aux paliers, R mesure la stabilité d'une topographie.
  - S'il est réentraîné, R mesure la présence d'une information quelconque.
- **Duel artificiel [constr].** Atténuer l'attention vers les jetons antérieurs au début de la suite supprime l'information de bloc et épargne l'information interne à la suite, par construction. D le reconnaît (« témoin de possibilité »). Mais H_B ne réfute alors que le pipeline : c'est un témoin positif, pas un duel au sens de B4.
- **Thermomètre [fuite].** D ne dit pas d'où viennent les « axes gelés ». S'ils sont appris sur des états étiquetés par la dissociation, l'étiquette entre dans l'instrument. L'ordre de lecture de la matrice est en outre un paramètre libre de la longueur LZ.

**(b) Conditions de perte de puissance**
- **Plafond de l'AUC.** Sous lois binormales, AUROC = Φ(d′/√2).
  - Une atténuation commune a de d′ donne R_local ≥ 0,8 et R_bloc ≈ a ≤ 0,2 dès que d′_local,veille ≥ √2·Φ⁻¹(0,9)/a (environ 9 pour a = 0,2) et que d′_bloc,veille est petit.
  - Le profil H_A naît alors d'une seule perte de rapport signal/bruit.
  - Il faut donc comparer des rétentions de d′, et non de E.
- **Règle des intervalles simultanés.** Si R_bloc vaut 0, obtenir une borne supérieure inférieure à 0,2 exige E_bloc,veille ≳ 11·SE(E_palier) par participant (z simultané ≈ 2,2). En deçà, la règle déclare « indécis » presque partout.
- **Thermomètre.**
  - Certifier au plus 5 % de fausses alertes, sans en observer aucune, exige au moins 60 négatifs indépendants (règle de trois).
  - Détecter un gain de 10 points par test de McNemar, avec 20 % de paires discordantes, exige environ (2,80)²·0,20/0,10² ≈ 157 positifs indépendants.

**(c) Contrôles négatifs dont l'absence est fatale**
- **Humain : la veille dégradée par un bruit tiré de la loi des paliers.** Si elle reproduit le profil, la cible n'est pas un profil d'anesthésie.
- **Duel artificiel : une intervention candidate sans accès à la frontière de suite,** jugée contre le même témoin diffus. Sans elle, ce duel ne réfute rien sur le réseau.
- **Thermomètre : deux ordres de lecture fixés d'avance.** Si le classement s'inverse de l'un à l'autre, le score est invalidé.

## Sur la proposition E

**(a) Défauts de méthode**
- **E.I [constr].** H_I,A exige une « AUROC de confiance < 0,55 » sans rien exiger de sa valeur à c = 0. Un modèle de 1 milliard de paramètres déjà proche de 0,5 la satisfait par plancher.
- **E.I [conf].** Amortir la rétention d'état de Mamba revient à un filtre exponentiel en distance. Pour cette seule architecture, l'intervention « scalaire » accède donc à la distance, contrairement au principe anti-triche d'E. Le contraste Transformeur/Mamba confond l'architecture et la forme de l'intervention.
- **E.I [fuite].** Les têtes « à entropie d'attention élevée » sont, en moyenne, celles à large portée. La sélection est quasi positionnelle.
- **E.I, témoin plafond.** Le masque à 8 jetons abolit aussi le local-distant (35 jetons). Il n'existe donc aucun témoin positif sur les paires appariées en distance, qui sont celles qui décident. Une issue H_I,B n'y distingue pas un réseau non dissociable d'une batterie insensible.
- **E.I [fuite].** c* et la famille d'interventions sont choisis sur les items mêmes qui estiment l'ISA. Le maximum sur doses et familles porte donc un biais du gagnant. A sépare la sélection de l'évaluation ; E ne le fait pas.
- **E.II [conf].** Les sondes sont entraînées sur un autre corpus, et leur étalonnage varie avec le genre du texte. Un mélange de genres dans PG-19 suffit à rendre r(t) multimodal. La restauration au changement de paragraphe est elle aussi prédite par le texte lui-même.
- **E.IV, statuts.** E marque VÉRIFIÉ « compétence linguistique nulle » et « conditionnement spectral local conservé » pour un jumeau qui n'a pas été construit. Je ne change pas ces statuts. Je signale seulement que la conception en dépend sans qu'aucun audit soit décrit, et que le second énoncé ne garantit pas le gain de bout en bout (voir A).
- **E.IV [constr].** Les têtes d'induction transportent l'information entre positions, ce que l'impulsion mesure. Elles sont comparées à une lésion aléatoire appariée en norme résiduelle, et non en perte. Une AUROC de lésion élevée est donc attendue (même objection qu'au R5 d'A).
- **Attribution.** E rattache le résultat kétamine à Casali et coll., 2013. A et F le rattachent à Sarasso et coll., 2015, dont le titre nomme la kétamine. L'attribution d'E est à vérifier.

**(b) Conditions de perte de puissance**
- **E.II.** Avec 50 historiques par cible et un mode de 2 %, on attend un seul historique dans le mode : le dip calculé sur n = 50 n'a pas de puissance. Il faut regrouper les cibles dans un modèle hiérarchique, ou passer à plusieurs centaines d'historiques par cible. La loi nulle gaussienne de même spectre traite en revanche correctement l'autocorrélation.
- **E.III.** Un effet d'éveil à p < 0,001 n'établit pas la puissance pour un effet égal à 10 % de celui de l'éveil.
  - Le z attendu sous sédation vaut environ 0,1·z_éveil.
  - Une puissance de 0,8 à α unilatéral 0,01 exige donc z_éveil ≥ 32.
  - Sinon, « p ≥ 0,05 » réfute H_III,A par simple défaut de puissance.
- **E.IV.** S_spec est le minimum de deux AUROC estimées, et E[min] ≤ min E. La variance biaise donc S_spec vers le bas, c'est-à-dire vers H_IV,A, surtout avec peu de réseaux par condition.

**(c) Contrôles négatifs dont l'absence est fatale**
- **E.I : un témoin positif non positionnel sur les paires appariées en distance.** Par exemple, l'ablation d'un composant identifié pour la règle globale sur des données indépendantes.
- **E.II : une stratification par genre.** Si la multimodalité disparaît dans chaque strate, c'est un mélange de genres.
- **E.III : l'éveil bruité selon la loi du bruit sous sédation.** Le motif « couches basses maintenues, couches hautes éteintes » est aussi prédit par la seule baisse du rapport signal/bruit.
- **E.IV : une lésion ciblée de têtes à fonction locale, appariée en perte,** et des entrées à jetons permutés.

## Sur la proposition F

**(a) Défauts de méthode**
- **Exp.1 [conf], sélection par la marge.** Apparier en marge de logit retient les items G les plus faciles et les items L les plus difficiles.
  - Supposons que la marge à λ = 0 contienne une composante propre à chaque item, non reproduite sous perturbation.
  - Les items retenus régressent alors vers la moyenne de leur catégorie : G chute davantage, L moins.
  - On obtient S_anesth > 0 sans aucun mécanisme.
  - Permuter les étiquettes après l'appariement ne reproduit pas cette sélection asymétrique.
- **Exp.1, dépendance à la paramétrisation de la dose.** S_anesth intègre sur λ ∈ [0, 1] : toute reparamétrisation monotone de la dose change sa valeur. Comparer des interventions dont les doses sont incommensurables n'a donc pas d'objet. L'aire entre la courbe paramétrée (P̃_L, P̃_G) et la diagonale, elle, est invariante. L'« AUC de maintien » de C a le même défaut.
- **Exp.1, règle de décision.** La règle de (b) ne compare qu'au bruit sur les logits. L'élagage à perplexité égale n'apparaît qu'en (c).
- **Exp.2 [fuite].** Patcher « depuis des états à haut score d'intégration » transfère aussi du contenu. Si l'état donneur porte l'information qu'exige la sonde G, la restauration est attendue sans qu'aucun régime soit en jeu.
- **Exp.3 [fuite].** Aucune mesure indépendante n'est désignée pour établir la vérité terrain « traitement sémantique résiduel attesté ». Si elle vient de l'encodage lui-même, le taux de détection est circulaire.
- **Exp.4, instrument validé.** PCI suppose une stimulation magnétique couplée à l'EEG. Sur EEG spontané, on valide LZc ou wSMI, pas l'instrument transposé.
- **Exp.4, transformations isofonctionnelles.** Avec LayerNorm et GELU, rotations et rééchelonnements ne préservent pas la fonction en général. Seules certaines transformations sont exactes : par exemple les permutations d'unités cachées ou de têtes, ou le rééchelonnement compensé de Q et K. Sous permutation d'unités, une mesure lue dans un ordre fixe change. Un ρ_inv ≤ 1 révélerait alors un défaut réel, mais il faut le déclarer comme une dépendance à l'ordre de lecture.

**(b) Conditions de perte de puissance**
- **Exp.2.**
  - Pour une AUC proche de 0,5 et n₊ ≪ n₋, la variance de Hanley et McNeil (1982, « The meaning and use of the area under a receiver operating characteristic (ROC) curve ») donne SE ≈ √(1/(12 n₊)).
  - Avec 40 erreurs L (2 % de 2 000 positions), SE ≈ 0,046 et SE(ΔAUROC) ≈ 0,05.
  - L'écart entre les seuils 0,04 et 0,10 vaut alors environ 1,2 SE.
  - Un effet réel de 0,10 est classé H_2B avec une probabilité d'environ 0,12, et H_2A seulement une fois sur deux.
- **Exp.3.** La marge |Δr| ≤ 0,005 exige N·n_eff/(2(1 − ρ)) ≥ (1,64/0,005)² ≈ 108 000. Avec ρ = 0,9, il faut N·n_eff ≥ 21 600. H_3B est hors d'atteinte avec 15 à 30 sujets et quelques minutes de récit ; le duel retombe sur « indéterminé ». Pour k*(s), l'objection faite à A s'applique.
- **Exp.4.**
  - ρ_inv prend un maximum sur 𝒯_iso, et le maximum de K écarts bruités croît comme σ√(2 ln K). ρ_inv décroît donc avec le nombre de transformations essayées : 𝒯_iso doit être fini et fixé d'avance.
  - Avec un réseau entraîné contre 10 graines, l'AUROC ne prend que les valeurs {0 ; 0,1 ; … ; 1}, et la p-valeur minimale vaut 1/11.

**(c) Contrôles négatifs dont l'absence est fatale**
- **Exp.1 : des pseudo-catégories.** Appliquer la même sélection par la marge à deux moitiés de L. Un S_anesth > 0 signe l'artefact de sélection.
- **Exp.2 : des donneurs à score élevé mais au contenu sans rapport** avec la sonde.
- **Exp.3 : l'éveil bruité selon la loi du bruit sous sédation.** A l'a prévu, F non.
- **Exp.4 : des entrées à jetons permutés** pour le contraste C1.

FIN-DE-CELLULE