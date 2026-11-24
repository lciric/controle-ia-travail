# Proposition H — Tour III.2 : critique croisée de méthode

**Pièces reçues.** Sept propositions (A, B, C, D, E, F, G, I) sont présentes et complètes. Aucune pièce manquante ou tronquée.

---

## Sur la proposition A

**(a) Défauts de méthode.**
E1 (placebo par coupure en deux du monde de référence) : si la population de référence contient des sous-groupes latents (types de tâches, niveaux de difficulté), la variance placebo est gonflée et le seuil de détection relevé — le test devient conservateur par construction, masquant une dérive réelle de B. E3 (vérité construite par gabarits programme + relecture humaine) : les gabarits reprennent la structure lexicale de la référence cachée, qui est précisément ce que le programme de recouvrement exploite. La fidélité mesurée du programme est donc surestimée sur cette vérité — fuite entre l'instrument et son étalon. E6 teste la cohérence contre un agent scripté « top-k » mais aucune fiche n'est servie à un modèle : l'espace des stratégies explorées est restreint au geste le plus simple, et tout geste intermédiaire (promotion partielle, appui mixte) échappe au test.

**(b) Conditions de perte de puissance.**
E1 : soient $\sigma^2_B$ la variance d'estimation de B sur $n_{\text{jum}}$ jumeaux et $\Delta_B$ l'écart inter-mondes. Le rapport $R = |\Delta_B|/\sigma_B$ est non concluant dès que $n_{\text{jum}} < 4\sigma^2_B / \Delta^2_B$ (HYPOTHÈSE, illustratif). Si la loi de B est Beta$(a,b)$ avec $a+b$ petit, $\sigma_B \propto 1/\sqrt{n_{\text{jum}}}$ décroît lentement. E2 : avec 60 paires par strate et 0 fausse alerte, la borne Clopper-Pearson vaut $\approx 0{,}05$ ; le test ne distingue pas FPR = 0 de FPR = 0,04. Plus généralement, pour toute loi de bruit de lecture où $\text{FPR}_{1/m} \in [0{,}02;0{,}05]$, l'essai est non concluant. E6 : si la règle de cohérence a un taux d'acceptation basal $p_0 > 1 - \delta/2$ (illustratif), la marge appariée de 0,10 est absorbée par la variance et le test n'a aucune puissance.

**(c) Contrôles négatifs fatalement absents.**
Aucun contrôle de la corrélation inter-lecteurs de l'oracle : tous les duels impliquant l'oracle supposent implicitement des erreurs indépendantes entre lecteurs. Si les lecteurs partagent un biais systématique (même famille de modèle, même invite), les taux de fausses alertes sont sous-estimés et la chaîne 2→4 n'est plus validée. E3 ne contrôle pas si l'édition du tiers (retrait d'un passage) laisse un artefact stylistique détectable par le moniteur indépendamment du fond — un tel artefact gonflerait la détection apparente.

---

## Sur la proposition B

**(a) Défauts de méthode.**
Duel 1a repose entièrement sur le simulateur des calculs de conception, dont la fidélité au moniteur réel n'est ni mesurée ni contrôlée. Le résultat est vrai du simulateur par construction, pas du banc. Duel 2 propose deux types de paires nulles (même document / deux lectures disjointes ; deux productions honnêtes de la même tâche) sans séparer bruit de lecture et variance de génération : le taux de fausses alertes mesuré est un mélange confondant ces deux sources. Duel 3 utilise une annotation humaine à deux annotateurs avec arbitrage des désaccords, mais l'arbitrage est un jugement subjectif non étalonné ; si l'arbitre favorise systématiquement les paraphrases larges, le rappel du repéreur est gonflé.

**(b) Conditions de perte de puissance.**
Duel 1a : avec $K$ réplicats par monde, l'erreur-type de l'écart est $\propto 1/\sqrt{K}$. Pour $K = 10$ (illustratif), distinguer $R = 2$ de $R = 3$ exige que $|\Delta_B|$ dépasse $\approx 2{,}5 \cdot \text{SE}$, soit un écart improbable si B est proche de 0 ou 1. Duel 5 : la métrique d'évasion est la différence de taux d'acceptation entre bras, avec $\Delta = 0{,}10$ et $n = 100$ (illustratif). Sous $H_0$, la puissance d'un test de McNemar apparié pour détecter un effet de 0,10 est $\approx 0{,}50$ (illustratif) — insuffisante. Duel 2 : même limitation que A-E2, 60 paires par strate.

**(c) Contrôles négatifs fatalement absents.**
Pas de test de fidélité du simulateur (Duel 1a) par rapport au moniteur réel — un « simulateur-check » comparant une statistique résumée simulée à la même statistique sur un petit lot réel est absent. Duel 3 ne contrôle pas si le repéreur de la même famille que le moniteur partage des erreurs corrélées (biais de famille partagée).

---

## Sur la proposition C

**(a) Défauts de méthode.**
Plusieurs usages du statut `[VÉRIFIÉ]` portent sur des affirmations analytiques discutables (« publier conjointement A et B évite toute perte d'information [VÉRIFIÉ] » — ce qui est une propriété d'information, non une identité algébrique). Décision 3 : le choix (b) à confiance 0,85 repose sur l'HYPOTHÈSE que les contrôles paraphrasés sont fréquents, sans mesure préalable ; la confiance ne reflète pas cette incertitude. E1 : les seuils $\delta_A = 0{,}03$ et $\delta_B = 0{,}08$ sont asymétriques sans justification par les variances respectives — le test est biaisé vers $H_A$. E2 : le seuil $\tau(m)$ est estimé sur le lot d'étalonnage puis traité comme fixe sur le lot de validation ; l'erreur d'estimation de $\tau$ n'est pas propagée.

**(b) Conditions de perte de puissance.**
E1 : si $\text{Var}(\hat{B}) > (\delta_B/2)^2 / N$, l'intervalle de confiance pour $\Delta\hat{B}$ contient 0 et $\delta_B$ simultanément, rendant le test non concluant. Avec $N = 200$ et $B \approx 0{,}10$, cela arrive dès que $B(1-B)/N > 0{,}0004$, soit $B > 0{,}08$ (VÉRIFIÉ, arithmétique). E3 : si la sensibilité du moniteur est proche du plafond ($1-q < 0{,}05$), l'écart $\hat{q}_{\text{prog}} - \hat{q}_{\text{rep}}$ est compressé sous le seuil de détection. E4 : le modèle Beta$(a,b)$ pour les effets aléatoires de l'oracle impose une forme unimodale ; toute distribution bimodale du biais (deux « régimes » de lecteurs) n'est pas couverte.

**(c) Contrôles négatifs fatalement absents.**
E3 : aucun contrôle de l'artefact d'édition — un document modifié par le tiers sans retrait de contrôle (retrait factice) n'est pas prévu, contrairement à F. E5 : pas de contrôle vérifiant que les fiches du saboteur « top-$K$ » ne sont pas distinguables des fiches honnêtes par des traits de surface (longueur, nombre de statistiques citées) indépendants de la cohérence.

---

## Sur la proposition D

**(a) Défauts de méthode.**
E1 introduit des « perturbations connues d'acceptation et d'abstention, sans dommage ». Le mécanisme de perturbation n'est pas défini : modifier le seuil du moniteur confond la perturbation avec un changement d'instrument ; modifier la distribution des tâches confond avec un changement de monde. Le test mesure la réponse à un artefact de conception, pas à un changement écologique. E3 fixe des seuils très exigeants (rappel ≥ 98 %, illustratif) : si aucun des deux instruments ne les atteint, les deux hypothèses sont « falsifiées » en même temps — la structure du duel est incohérente. D mentionne un « hybride audité » pour la décision 3, mais la règle de bascule entre programme et repéreur dépend des données de l'échantillon de mise au point, sans correction pour cette dépendance.

**(b) Conditions de perte de puissance.**
E2 : « borne inférieure de détection au moins 80 % sur la plus petite strate » — si la plus petite strate a $n_s < 25$ (illustratif) épisodes endommagés, la borne inférieure binomiale à 95 % pour 20/25 détections est $\approx 0{,}61$, bien sous 0,80. Le critère est mathématiquement inatteignable pour des strates petites. E5 : le seuil de 90 % de détection du sabotage et 5 % de fausses alertes impose une courbe ROC très favorable. Sous toute loi jointe de la règle de cohérence et du saboteur telle que l'AUC < 0,95, le test est non concluant.

**(c) Contrôles négatifs fatalement absents.**
E1 : aucun contrôle vérifiant que le mécanisme de perturbation lui-même n'introduit pas de confond. E4b : « même simulation sans réallocation » n'est pas assorti d'une contrainte sur les graines aléatoires ; des graines différentes pourraient créer des écarts spurieux. Pas de contrôle de corrélation inter-lecteurs de l'oracle dans aucun duel.

---

## Sur la proposition E

**(a) Défauts de méthode.**
Décision 2 : « parmi les seuils au moins égaux à 1/m, choisir le plus sensible compatible avec le plafond sur les honnêtes » — si $J$ seuils sont testés (un par valeur entière de $k$), la sélection du meilleur crée un biais de sur-ajustement sur le lot d'étalonnage ; la sensibilité observée sur le lot final sera inférieure à la sensibilité étalonnée. Décision 3 : l'adjudication indépendante est un troisième jugement, non une vérité de terrain ; si l'adjudicateur partage un biais avec le repéreur (même formation linguistique), l'audit est circulaire. Décision 1 : soustraire le « contraste négatif » des écarts entre mondes suppose l'additivité des effets ; pour des proportions proches de 0 ou 1, l'additivité sur l'échelle naturelle ne tient pas (HYPOTHÈSE).

**(b) Conditions de perte de puissance.**
Décision 1 duel : le seuil de 5 points (illustratif) pour l'excès de variation de B sur A suppose des variances d'estimation comparables. Si B est estimée sur $n_B \ll n_A$ données, $\text{Var}(\hat{B}) \gg \text{Var}(\hat{A})$, et un excès de 5 points est compatible avec la variance pure de $\hat{B}$, rendant le test non concluant. Décision 2 : la sensibilité ne peut pas être évaluée sur le lot d'étalonnage si celui-ci ne contient que des paires honnêtes (comme proposé par d'autres) ; le critère « aucun seuil utile » n'est pas calculable à l'étalonnage. Décision 5 : la puissance du duel dépend de la spécificité de la « règle de preuve gelée » de l'honnête. Si cette règle est vague, les fiches honnêtes sont hétérogènes et les erreurs de bonne foi brouillent le signal.

**(c) Contrôles négatifs fatalement absents.**
Pas de contrôle de biais de l'adjudicateur (décision 3) — un lot de cas dont la réponse est connue par construction et soumis à l'adjudicateur est absent. Décision 2 : pas de contrôle pour la non-stationnarité de la distribution des tâches entre lot d'étalonnage et lot final.

---

## Sur la proposition F

**(a) Défauts de méthode.**
E1 utilise des intervalles de Clopper-Pearson pour borner $|\Delta\hat{A}|$, mais $\Delta\hat{A}$ est une différence de proportions, pas une proportion unique ; la garantie de couverture de Clopper-Pearson ne s'applique pas directement. Décision 2 (option conforme) : la garantie du *split conformal* est marginale, non conditionnelle à $m$. Si la distribution des écarts honnêtes-honnêtes dépend de $m$, le taux de fausses alertes conditionnel à certaines strates peut excéder la cible. Décision 3 (vérification différentielle avant/après retrait) : le repéreur est juge et partie — s'il ne détecte pas une paraphrase résiduelle, le dommage est admis comme valide, créant une fuite entre la désignation et la vérité terrain. E3 (retrait factice) : excellent contrôle, mais si le moniteur utilise des traits sémantiques, sa réaction au retrait factice n'est pas comparable à sa réaction au retrait réel — le contrôle ne teste que les artefacts de surface.

**(b) Conditions de perte de puissance.**
E2 : 300 paires pour un test binomial. Si le bruit de lecture varie par $m$ et qu'il y a 5 strates, 60 paires par strate — même limitation que A et B. E5 : 500 épisodes, seuil 0,20. Sous une loi binomiale, pour détecter un taux d'évasion de 0,25, la puissance d'un test exact unilatéral à 5 % est $\approx 0{,}72$ (illustratif) — limite. E4 : 200 paramétrages × 100 000 réplications. La grille est figée ; si le pire cas du FWER se situe dans une zone non couverte (corrélation extrême lectures honnêtes / sabotées), le test conclut à tort à l'absence de violation.

**(c) Contrôles négatifs fatalement absents.**
E1 : le contrôle négatif (deux moitiés du monde de référence) ne contrôle pas si le pipeline d'inférence (quantification FP8, vLLM) introduit du non-déterminisme qui dégraderait la reproductibilité. Décision 4.2 (option : tester l'excès sur le lot d'étalonnage puis geler) : aucun contrôle de l'inflation d'erreur liée à cette procédure à deux étages.

---

## Sur la proposition G

**(a) Défauts de méthode.**
Décision 1 (option : critères séparés sur $\Delta p_{\text{sig}}$ et $\Delta p_{\text{abs}}$) : ces deux écarts ne sont pas indépendants ($\Delta p_{\text{acc}} + \Delta p_{\text{sig}} + \Delta p_{\text{abs}} = 0$, VÉRIFIÉ) ; deux seuils séparés sur des grandeurs liées peuvent se contredire ou être conjointement irréalisables. Décision 3 (cascade hybride) : les cas routés au repéreur sont ceux où le programme lexical échoue — un échantillon sélectionné, systématiquement plus difficile. L'erreur du repéreur mesurée sur cet échantillon surestime son erreur globale. E4 fusionne les tests du FWER (4.2) et du produit dose × borne (4.1) ; en cas d'échec, l'attribution causale est impossible. Décision 5 (épisodes $K = 0$) : un analyste qui voit des épisodes à bruit pur peut apprendre à reconnaître l'absence de loi, ce qui modifie son comportement sur les épisodes $K > 0$ — confond.

**(b) Conditions de perte de puissance.**
E1 : $N = 200$ tâches, seuil $|\Delta p_{\text{abs}}| > 0{,}05$. Pour $p_{\text{abs}} \approx 0{,}10$, $\text{SE}(\hat{p}_{\text{abs}}) \approx 0{,}021$, d'où $\text{SE}(\Delta\hat{p}_{\text{abs}}) \approx 0{,}030$. L'intervalle de confiance à 95 % a une demi-largeur $\approx 0{,}059 > 0{,}05$ : le test ne peut pas conclure même sous un vrai $\Delta = 0{,}05$. E5 : 100 épisodes par bras, seuil +0,15. Sous une loi binomiale avec probabilité de base 0,20, la puissance pour détecter un écart de 0,15 est $\approx 0{,}55$ (illustratif). E3 : 120 contrôles en 4 strates = 30 par strate ; pour détecter un gain F1 de 0,15, le test apparié est sous-puissant.

**(c) Contrôles négatifs fatalement absents.**
E1 : pas de contrôle pour la non-stationnarité du générateur de tâches entre mondes (au-delà de ce que le moniteur mesure). E5 : le contrôle « Benjamini-Hochberg honnête doit être accepté dans les deux régimes » ne vérifie pas si la règle de cohérence distingue l'honnête BH d'un saboteur plus subtil que « top-k ». Aucun contrôle de famille partagée entre le repéreur et le moniteur évalué dans E3 (mentionné dans le texte mais non intégré au contrôle négatif).

---

## Sur la proposition I

**(a) Défauts de méthode.**
Le « fil conducteur » (3→2→4) est une hypothèse causale non testée comme telle — les trois duels D2, D3, D4 sont conçus séparément et ne testent pas la chaîne comme mécanisme conjoint ; un résultat favorable sur chacun ne prouve pas le mécanisme. D3 teste la prévalence des contrôles paraphrasés ($H_A : < \varepsilon$), propriété des documents, et non l'erreur du programme sur ces documents — confusion entre la fréquence du phénomène et l'erreur de l'instrument. Décision 4.1 (annexe scellée) : l'annexe contient les chiffres par strate et n'est publiée qu'avec l'énoncé garanti de la campagne suivante ; aucun mécanisme d'audit empêche que seules les strates favorables soient finalement publiées — fuite de sélection entre campagnes. D5b (deviner $k$) utilise un classifieur fixe, mais un agent-modèle pourrait inférer $k$ par des indices différents (structure des données, puissance statistique attendue) ; le test ne couvre pas cet espace.

**(b) Conditions de perte de puissance.**
D2 : $n = 100$ paires, borne Clopper-Pearson à 0 événements $\approx 0{,}03$. Si le vrai FPR est 0,04, la probabilité d'observer $\geq 1$ fausse alerte est $1 - (0{,}96)^{100} \approx 0{,}98$ (VÉRIFIÉ) — le test a une bonne puissance ici, mais la borne sera $\approx 0{,}07$, ne pouvant conclure que FPR ≤ 0,05. D3 : si la prévalence des paraphrases est $p_{\text{par}} = 0{,}05$, le nombre attendu dans 100 documents est $\approx 5$ ; le rappel sur 5 cas a un intervalle de confiance de Wilson de largeur $\approx 0{,}40$ — non concluant. D5a : $n = 200$, $\delta = 0{,}10$. Pour un vrai écart de 0,10, la puissance d'un test apparié est $\approx 0{,}85$ (illustratif) si la corrélation appariée est > 0,3 ; elle tombe sous 0,60 si les paires sont quasi-indépendantes.

**(c) Contrôles négatifs fatalement absents.**
D3 ne contrôle pas si le « second désignateur d'une autre famille » partage des biais issus de données d'entraînement communes — un test de concordance entre familles sur un lot de cas construits (paraphrases connues) est absent. D4 : pas de contrôle pour la direction du biais de $q$ en régime d'excès (sur-signalement gonflant la détection apparente vs. effet plancher abaissant la détection). D5b ne contrôle pas si les traits utilisés par le classifieur sont les mêmes que ceux qu'un agent-modèle exploiterait — le contrôle négatif (étiquettes permutées) ne teste que le classifieur, pas la fuite.

FIN-DE-CELLULE