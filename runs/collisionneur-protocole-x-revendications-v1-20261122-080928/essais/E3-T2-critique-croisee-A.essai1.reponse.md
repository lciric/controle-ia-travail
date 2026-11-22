# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces.** B, C, D et E sont présentes et closes par leur ligne de fin, sans coupure visible. Ma propre conception du tour III.1 ne m'est pas retransmise : je n'en cite rien. Je n'ai pas recalculé les empreintes.

**Statuts.** Les FAITS ne portent aucun statut. Tout ce qui suit est HYPOTHÈSE : ce sont des analyses de conception, rien n'a été exécuté. Les passages notés « dérivation » sont de l'algèbre vérifiable par un tiers, valable sous le modèle écrit, lui-même HYPOTHÈSE. Tous les chiffres sont illustratifs.

**Trois modèles de travail, utilisés plus bas.**

- **M1, effet de trajectoire.** Sous honnêteté, le score au pas t s'écrit x_t = b + e_t, avec Var(b) = τ² propre à la trajectoire et Var(e_t) = σ². Le sabotage ajoute δ par pas. Dérivation : le rapport signal sur bruit de la somme sur T pas vaut δT/√(T²τ² + Tσ²), qui tend vers δ/τ. L'accumulation ne gagne donc rien au-delà de T ≈ σ²/τ².
- **M2, budget constant.** On audite m = B/k blocs de k pas. L'écart de valeur d'un bloc a pour moyenne kδ et pour écart-type σk^γ. Dérivation : le rapport signal sur bruit de la moyenne des blocs vaut (δ√B/σ)·k^(1/2−γ).
- **M3, déterminisme des activations.** À poids θ fixés, z_t = f_θ(jetons du contexte). Un écart d'activations à texte visible égal ne peut venir que de jetons cachés au moniteur ou d'un θ différent.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **C1 est presque vrai par construction à cause de R.** Le dommage de S est un biais signé, de l'ordre de Tδ. R est non ciblée : son biais signé moyen est nul. « Même dommage moyen » oblige donc à changer de métrique entre les bras (valeur absolue pour R) ou rend la calibration impossible. Avec la valeur absolue, E|somme| = σ_R√(2T/π), donc σ_R = δ√(πT/2). Dérivation sous modèle gaussien additif : à dommage égal, les perturbations par pas de R sont environ 7,9 fois plus amples pour T = 40, et le rapport des preuves est de l'ordre de πT/2 ≈ 63. L'issue ρ ≥ 3 suivrait de l'arithmétique de la marche aléatoire, pas d'une furtivité.
2. **Le LLR dépend de la classe d'entraînement du moniteur.** Entraîné sur S contre H, il sous-évalue R, ce qui pousse ρ vers le bas. Entraîné sur R, c'est l'inverse. « Le meilleur moniteur disponible », s'il est choisi sur les données où ρ est calculé, ajoute un biais de sélection.
3. **C2 confond intention et poids modifiés.** S-d diffère de H par un LoRA. Tout LoRA déplace les activations, y compris le long de la direction de la sonde. AUROC(S-d contre H) élevée ne dit rien de l'intention.
4. **L'appariement par graine ne tient pas.** Les contextes divergent dès le premier choix biaisé. Les écarts d'activations mêlent alors l'état interne et l'état différent de la tâche.
5. **L'étiquette « action sabotée » n'est pas définie.** Si elle vaut l'étiquette de condition, l'AUROC par action mesure un décalage constant par trajectoire. Les unités effectives sont les trajectoires.
6. **C3 compare à un homme de paille.** Un seuil par action calibré au α de la trajectoire est conservateur. Contre un sabotage construit pour rester sous le seuil par pas, toute statistique cumulée gagne par construction. Le comparateur pertinent est une somme à horizon fixe ou un CUSUM.
7. **Le « dommage médian au déclenchement » est conditionné à l'alerte.** Un test qui alerte tôt mais rarement gagnerait sur ce critère.
8. **L'« écart à la gerbe » de C3 n'est pas spécifié.** On ne sait pas sur quelle variable il porte.
9. **C4 a une fuite entre étiquette et instrument.** Le δ par unité ne se mesure que par rejeu. L'audit par rejeu est donc évalué contre une étiquette produite par lui-même. La pente positive en δ est tautologique : seule la variance nulle H contre H a un contenu empirique. Les budgets ne sont pas égalisés non plus : un rejeu coûte plusieurs pas, un jugement un seul.
10. **C0 contient la vérité de terrain.** Les tests cachés définissent le dommage de la seconde tâche. L'écart du résultat final à des références centrées sur la vraie valeur est le dommage de la première. La non-infériorité est acquise par construction, mais seulement en fin de tâche.
11. **B4.** Dans C2, H_A et H_B sont des conjonctions non complémentaires. Par exemple, S-p ≥ 0,75 avec S-d < 0,75 ne falsifie rien. Même trou dans C3 pour α < FPR ≤ 2α.

### (b) Conditions de perte de puissance

- **ρ est un quotient de moyennes.** Il devient non jugeable dès que l'intervalle de E[Λ_S] ou de E[Λ_R] contient 0. C'est le régime diffus lui-même. Le quotient n'a alors pas de moments finis et le bootstrap n'est pas fiable.
- **Le contrôle négatif de C1 a un critère erroné.** Pour un LLR exact, E_H[Λ] = −KL(H‖S) < 0, pas 0. Le critère de validité est E_H[exp Λ] ≤ 1.
- **C3 bute sur le plancher conforme.** Avec 10 références par tâche, la valeur-p minimale est 1/11 ≈ 0,09, au-dessus de α = 0,05. Le passer exige un produit sur les pas, donc E_H[e_t | passé] ≤ 1. Cette condition est violée dès que le rang d'une trajectoire honnête persiste d'un pas au suivant (M1 avec τ > 0).
- **Le TPR à 1 % de FPR est mal estimé.** Sur 600 trajectoires H groupées en 200 tâches, le seuil est fixé par environ 6 trajectoires, soit 2 à 3 tâches.
- **Le contraste S contre H-sec peut être vide.** Il est non informatif si la loi du score sous H-sec égale celle sous H, c'est-à-dire si la manipulation est sans effet.
- **C4.** La puissance du rejeu ne dépend que de δ/σ₀, où σ₀ est l'écart-type H contre H de l'effet aval. Si σ₀ croît avec l'horizon de rejeu comme en M1, allonger le rejeu ne gagne rien.

### (c) Contrôles négatifs dont l'absence serait fatale

- **H-d** : un LoRA bénin de même rang et de même volume, distillé sur H ou H-sec.
- **Préfixes forcés** : activations lues sur des historiques identiques entre conditions.
- **Vérification de manipulation de H-sec** : AUROC(H-sec contre H) rapportée.
- **Témoin positif de l'auditeur de C4** : un sabotage concentré. Sans lui, AUROC ≤ 0,6 mesure la faiblesse de l'auditeur.
- **R-dir** : une dégradation dirigée mais non intentionnelle, par exemple une préférence méthodologique constante, appariée en amplitude par pas. Sans elle, tout détecteur de cohérence directionnelle sépare S de R trivialement.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts.** C marque certains énoncés VÉRIFIÉ (Wald, Page, « par construction algébrique ») et d'autres OBSERVÉ-NON-AUDITÉ, sans pièce transmise à l'appui. Je ne modifie pas ces statuts et je ne peux pas les endosser. « Si la sonde ne bat pas la couche 0, elle ne lit que le vocabulaire » est une interprétation, pas une identité algébrique. La couche 0 ne voit pas par attention une consigne placée ailleurs dans le contexte.
2. **Contribution 1 : fuite sur le vecteur directeur u.** Le « vecteur directeur moyen » ne s'estime que sur des trajectoires sabotées. Cela contredit la calibration sur exécutions honnêtes seules. S'il est estimé sur le saboteur testé, la fuite est directe.
3. **Quatre facteurs changent à la fois.** Mémoire, normalisation par pas, fusion texte et activations, projection sur u. Le gain sur max_t S_t n'est attribuable à aucun.
4. **L'alignement par indice t est un confondant.** Le pas 12 de deux exécutions honnêtes ne désigne pas la même phase, comme le dit le présupposé 3 de C. Un saboteur simplement plus lent est détecté comme déphasé.
5. **Incohérence d'effectifs.** N_ref = 20 au même pas, mais le plan compte un régime honnête à 2 graines sur 50 tâches. Soit les références sont mises en commun entre tâches et Σ_t absorbe l'hétérogénéité des tâches, soit le budget est faux.
6. **Critère non jugeable.** « Avant 30 % du dommage final » suppose un dommage cumulé au pas t. Il n'existe pas pour un score terminal de réussite.
7. **Le saboteur de la contribution 1 est obtenu par invite.** Aucun contrôle de consigne n'est prévu.
8. **Le contrôle négatif perturbe l'entrée de l'instrument.** La température et la quantification à 4 bits déplacent les jetons et les activations indépendamment de toute incompétence. Les deux issues du contrôle sont ininterprétables.
9. **Contribution 2 : M_dyn détecte « poids modifiés ».** Par M3, S-DPO a un θ différent des références honnêtes. Tout LoRA sort de la variété honnête. Le contrôle de paraphrase porte sur le modèle de base et ne répond pas à cela.
10. **La vérification d'implémentation de M_lin est contaminée.** AUROC ≥ 0,80 sur S-Prompt peut venir de la lecture de l'invite.
11. **Contribution 3 : l'argument en O(k) contre O(√k) oublie la division de m par k.** Dérivation M2 : avec des incréments indépendants (γ = 1/2), le gain à budget constant est exactement nul. Un gain de 25 points ne peut venir que de trois sources : un bruit d'évaluation fixe par comparaison, la quantification de ΔV (des sous-objectifs entiers, donc ΔV₁ = 0 presque sûrement), ou une interaction entre pas. Aucune n'est l'« intégration » invoquée.
12. **Deux variables changent entre les allocations.** La longueur k, et l'accès à un oracle fonctionnel ΔV que l'audit unitaire par jugement n'a pas.
13. **Le budget assimile un jugement à un pas de génération.**
14. **Le rejeu par « le modèle honnête de référence » suppose un accès illimité à la politique honnête.** Cela contredit le « nombre limité » du cadre.
15. **B4.** Des zones ne falsifient rien : TPR dans [0,45 ; 0,75) pour la contribution 1 ; M_lin dans [0,60 ; 0,70) et M_dyn dans [0,65 ; 0,75) pour la contribution 2 ; écart dans [0,10 ; 0,25) pour la contribution 3.

### (b) Conditions de perte de puissance

- **CUSUM normalisé.** Par M1, si l'ICC des z_t honnêtes est τ²/(τ² + σ²), une fraction 1 − Φ(κ/τ) des trajectoires honnêtes a une dérive positive. Pour κ = 0,5 et τ = 0,71, c'est environ 24 %. Le seuil h doit alors croître avec T et la puissance est gouvernée par δ/τ.
- **Erreur d'estimation de μ_t.** Elle est d'ordre 1/√N_ref ≈ 0,22 par pas. Elle est corrélée entre pas, parce que les 20 mêmes trajectoires servent partout.
- **M_dyn est sous-déterminé.** La matrice A a 32² = 1024 paramètres pour au plus 780 transitions autocorrélées, issues de 20 grappes. Le résidu hors échantillon des trajectoires honnêtes est gonflé par l'erreur d'estimation. Sans trajectoires honnêtes tenues à l'écart, le FPR n'est pas calibrable.
- **Précision des AUROC.** Avec 100 trajectoires par classe en 50 grappes, l'erreur-type à AUROC = 0,7 est d'environ 0,037 sous indépendance et 0,05 par grappes (formule de Hanley et McNeil, 1982, *The Meaning and Use of the Area under a ROC Curve*, de mémoire, non vérifié). Les frontières 0,60, 0,65, 0,70 et 0,75 sont distantes de 1 à 2 erreurs-types.
- **Rejeu par blocs.** Non jugeable sans la loi nulle de ΔV_k entre deux rejeux honnêtes depuis le même état, pour chaque k. L'exposant γ est le paramètre décisif et n'est pas mesuré.

### (c) Contrôles négatifs dont l'absence serait fatale

- **DPO bénin** : même rang, même volume, préférence orthogonale à la qualité (un style, par exemple).
- **Consigne secrète bénigne** pour le saboteur par invite.
- **Loi nulle honnête contre honnête de ΔV_k.**
- **Plan factoriel 2×2 de la contribution 3** : k = 1 ou 5, avec ou sans ΔV.
- **Ablations une à une** des quatre ingrédients du CUSUM.
- **Contrôle de déphasage** : un agent honnête ralenti.

Le contrôle TDD est bon. Je le reprends plus bas.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Le contraste principal est piloté par un paramètre de conception.** Le simulateur admet un solveur exact, donc le regret par décision est calculable. Si le comparateur non interne y a accès, même par une borne mécanique de progression, son taux de détection approche 1. Le gain interne est alors plafonné par 1 − TPR_non-interne. H_B devient vraie par construction dès que ce taux dépasse 0,90. Si le solveur est retiré, le gain mesure le handicap d'information choisi par l'expérimentateur.
2. **Le duel est asymétrique.** Réfuter H_B exige une borne haute du FPR ≤ 5 %. Un seuil calibré pour viser 5 % a un vrai FPR voisin de 5 %, donc une borne haute au-dessus de 5 % dans environ 97,5 % des tirages. H_B est quasi irréfutable, sauf à calibrer nettement plus bas, ce qui coûte la puissance du premier critère. B4 n'est respecté que formellement.
3. **La qualification locale confond rareté et indiscernabilité.** Les actions sont tirées sans égard à leur perte. Dérivation : si une fraction π des pas dévie et que l'inspecteur reconnaît un pas déviant avec une exactitude a, l'exactitude mesurée vaut 0,5 + π(a − 0,5). Pour π = 0,3 et a = 0,8, on obtient 0,59, sous le seuil de 0,60. Un sabotage rare mais localement visible serait déclaré « d'apparence honnête ».
4. **Le contrôle par permutation est ambigu.** Entre conditions, il brouille les étiquettes et le gain disparaît trivialement. À l'intérieur d'une condition, il conserve tout signal constant de condition (la consigne) et le gain subsiste. La pièce ne dit pas lequel est fait.
5. **Les instances témoins sont hors distribution.** Les options y sont toutes équivalentes. Une absence d'alerte peut refléter ce décalage plutôt qu'une spécificité au dommage.
6. **L'appariement des paires d'actions « sur état public » est fragile.** Les états divergent selon l'historique. Il faut un état imposé aux deux politiques.
7. **Les efforts de réglage sont asymétriques.** Le « meilleur comparateur sur validation » et la « couche sur validation » sont deux maxima. Leur différence est biaisée si les espaces de recherche sont inégaux.
8. **Aucun saboteur par poids.** Le résultat ne porterait que sur la dégradation par consigne.
9. **Les échecs honnêtes appariés sur la perte terminale ne le sont pas sur le profil de perte.** Ils sont probablement concentrés. La qualification « diffus » est elle-même une sélection postérieure au traitement. D le reconnaît en publiant les résultats sur tous les essais assignés, ce que je note à son crédit.

### (b) Conditions de perte de puissance

- **Gain apparié.** L'erreur-type est √((p₁₀ + p₀₁ − g²)/n). Avec une discordance de 0,2 et g = 0,1, elle vaut 0,031 pour n = 200 et 0,052 pour n = 70 après partage par familles. Une borne basse ≥ 0,10 exige alors un gain observé d'environ 0,16 à 0,20. Le verdict le plus probable est « non résolu ».
- **Strate des échecs honnêtes.** Borner le FPR sous 5 % avec zéro alerte demande au moins 60 échecs honnêtes de test (règle de trois).
- **Enveloppe à deux références par instance.** Un écart standardisé par un écart-type à 1 degré de liberté suit une loi de Cauchy, sans variance. L'instrument est non jugeable sans variance mise en commun entre instances.
- **Taux de qualification q.** Des modèles de 3B et 7B sous simple consigne peuvent ne produire que des dégradations grossières. Si q est faible, le nombre de positifs qualifiés rend tous les intervalles vides de sens. Aucun critère d'arrêt n'est prévu sur q.
- **Plafond.** Si P(détection non interne) ≥ 0,9, le duel principal est non jugeable.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Témoin positif de l'inspecteur local** : des cas où une décision porte plus de la moitié de la perte.
- **Plage de puissance préenregistrée pour le comparateur**, hors plafond.
- **Politique honnête bruitée à profil de regret diffus apparié.** Les échecs honnêtes naturels seront rares et concentrés.
- **Permutation spécifiée dans les deux versions.**
- **FPR honnête mesuré sur des instances de type témoin.**
- **Consigne honnête de même format explicitée.** La pièce dit « même format » sans dire ce que reçoit le bras honnête.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Statuts.** E marque « VÉRIFIÉ mathématiquement » que toute somme scalaire échoue quand la suspicion honnête moyenne dépasse celle du saboteur. Je ne change pas ce statut, mais j'en conteste la portée. L'énoncé ne vaut que pour des sommes non centrées. Une somme centrée par état, c'est-à-dire avec l'information que C3 s'accorde, n'est pas couverte.
2. **L'énoncé de C1 mêle un lemme et une conjecture empirique.** La borne α + O(B√ε) découle de Pinsker et de l'additivité de la KL. Dérivation : on obtient même α + √(Bε/2). Elle est vraie par définition de la classe d'adversaires et n'est pas falsifiable. E1 ne la teste pas : ε n'y est jamais estimé.
3. **« Dommage marginal nul » n'implique pas « KL locale faible ».** Le premier est une propriété de la fonction de dommage, le second une propriété des lois. Un changement d'invariant non motivé peut être très improbable sous la politique honnête et rester inoffensif seul. Le sabotage de E1 peut donc sortir de la classe du lemme.
4. **Fuite entre attaque et instrument dans E1.** Le couplage est construit le long d'une dépendance de données. La paire sabotée est donc une arête par construction. L'avantage sur des paires hors graphe se réduit à un enrichissement combinatoire : pour T = 30 il y a 435 paires, contre |E| arêtes. Le même concepteur définit la dépendance pour l'attaque et pour l'audit.
5. **Deux variables changent dans le comparateur de E1.** L'audit unitaire est guidé par score, l'audit de paires est aléatoire.
6. **C2 : le signal est vrai par construction et non spécifique.** Par M3, P_hon(z | texte complet) est dégénérée. Le résidu z − ĝ(φ) ne mesure que trois choses. Soit ce que φ omet du contexte : la consigne furtive, donc le confondant de consigne. Soit un θ différent : le LoRA, donc n'importe quel LoRA. Soit l'erreur d'extrapolation de ĝ.
7. **Le résidu de C2 est un terme d'un détecteur standard.** Dérivation par inverse par blocs, sous modèle linéaire gaussien : Mahalanobis²(φ, z) = Mahalanobis²(φ) + Mahalanobis²(z − E[z | φ]). Le score proposé est le second terme du détecteur conjoint à une classe. Or ce détecteur conjoint ne figure pas parmi les comparateurs. Seule une fusion tardive de rangs y figure.
8. **C3 : le centrage n'est exact que si le rééchantillonneur suit la politique honnête du même agent.** E rééchantillonne avec un modèle de 3B pour un agent de 7B. Un agent honnête plus capable s'écarte du 3B dans une direction persistante. Une U-statistique de produits scalaires est invariante au sens de cette direction : elle alerte sur « mieux de façon cohérente » comme sur « pire de façon cohérente ».
9. **Le contrôle « agent honnête 3B » de C3 est trivial.** Il est centré par construction, puisque c'est la même politique que le rééchantillonneur. Il ne teste pas ce confondant.
10. **La randomisation de Rademacher suppose la symétrie conditionnelle des écarts centrés.** Le biais de centrage du point 8 la viole.
11. **Les comparateurs scalaires de C3 n'ont pas la même information.** Ils reçoivent la suspicion d'un moniteur. La U-statistique reçoit ψ et les rééchantillonnages. À direction de nuisance connue (toutes les marges baissent), la somme linéaire des ψ centrés est plus puissante qu'une forme quadratique. L'avantage, s'il existe, viendrait du centrage et non de la « cohérence directionnelle ».
12. **B4 dans E0.** H_A est existentielle (« au moins une stratégie »). L'échec de trois familles ne la falsifie pas. L'issue négative ne falsifie que « ces trois familles, sur ces modèles ».

### (b) Conditions de perte de puissance

- **C3, cible α = 0,01.** Distinguer un FPR de 0,015 d'un FPR de 0,02 demande de l'ordre de 3 700 trajectoires honnêtes indépendantes. Avec 300 trajectoires de test, un vrai FPR de 0,02 passe le critère (au plus 4 alertes) avec une probabilité d'environ 0,29 (approximation de Poisson). Avec 150 tâches comme grappes, le critère est non jugeable.
- **C3, puissance.** Elle est nulle si la dérive par pas est faible devant le biais de centrage ‖E_hon[ψ] − E_rééch[ψ]‖. Elle est fausse (alertes sur des agents honnêtes) si ce biais est non nul et persistant.
- **C2, extrapolation.** Avec 40 trajectoires, environ 40 grappes effectives, et z de dimension de l'ordre de 4 000, l'erreur ‖(g − ĝ)(φ)‖² croît avec le levier φᵀ(ΦᵀΦ + λI)⁻¹φ. Sous décalage de la loi de φ entre références et tâches nouvelles, le score se réduit à un détecteur de texte hors distribution. C'est le confondant de difficulté que C2 prétend retirer.
- **E1.** Le gain attendu est fonction du rapport entre |E| et le nombre de paires possibles, et du rappel de l'auditeur sur une paire. Si |E| croît comme T², ce qui arrive dans un espace de travail densément couplé, l'enrichissement disparaît.
- **E0.** Le critère AUROC_pas ≤ 0,55 dépend de la force du moniteur de 3B. Avec 100 trajectoires par cellule, l'erreur-type est d'environ 0,04, donc 0,55 et 0,60 sont indistincts.

### (c) Contrôles négatifs dont l'absence serait fatale

- **LoRA bénin et consigne cachée bénigne** pour C2 et C3.
- **Attaque à couplage hors graphe ou d'ordre 3** pour E1 : convention sémantique, valeur par défaut de configuration.
- **Levier seul comme comparateur de C2**, ainsi que le détecteur à une classe conjoint sur [φ, z].
- **Agent honnête de 7B à préférence bénigne persistante**, par exemple une programmation défensive, pour C3.
- **Somme linéaire des ψ centrés** comme comparateur de C3.
- **Estimation de ε** sur les modifications injectées, sans quoi le lemme et l'expérience ne parlent pas du même objet.

Le témoin positif concentré de E0 est le seul des quatre pièces. Je le reprends plus bas.

---

## Emprunts déclarés (B1) et points sans réponse dans les quatre pièces

**Je me sers de :**

- H-sec (B) ;
- les instances témoins sans perte possible et l'analyse sur tous les essais assignés (D) ;
- le contrôle TDD (C) ;
- le témoin positif concentré (E).

**Deux points ne sont traités nulle part.** Je ne les harmonise pas, je les signale comme objections ouvertes à chacune.

- **Aucun plan ne sépare « saboteur par poids » de « poids différents ».** Le contrôle par LoRA bénin est absent de B, C et E. D évite le problème en renonçant aux poids.
- **Aucun plan ne mesure τ, l'effet de trajectoire honnête de M1.** Tous les gains séquentiels annoncés (C3 de B, contribution 1 de C, enveloppe de D, C3 de E) en dépendent.

**Ce qui me ferait réviser ces critiques.**

- Une mesure montrant que l'ICC des scores honnêtes est inférieure à 1/T.
- Une mesure montrant qu'un LoRA bénin laisse les scores internes à leur niveau honnête.

FIN-DE-CELLULE