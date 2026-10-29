# Proposition A — Tour III.2 : critique croisée de méthode

**Pièces reçues.** Les conceptions B et C sont présentes, non coupées (chacune se termine par sa ligne de fin). Les faits (pièces A à D) sont ceux du tour précédent ; la pièce D ne contient toujours ni « mémoire qui refuse les redites » ni « héritage récompensé ». Je ne résume ni ne fusionne B et C (B1) ; quand je m'appuie sur un point de l'une pour critiquer l'autre, je le dis.

**Statuts.** Ce qui vient des pièces est RAPPORTÉ ou VÉRIFIÉ (contenu). Mes lectures comparées sont OBSERVÉ-NON-AUDITÉ. Mes calculs sur les chiffres des pièces sont marqués « calcul » et restent illustratifs.

---

## Sur la proposition B

### (a) Défauts de méthode

**B-a1. La qualité q reste dans le score et confond toutes les comparaisons contre O4 et b_eloigne.**
Le score r_p = √(q_i q_j)·(1−D²)^(β/2)·w(C) garde q. Or, dans les mondes de la pièce B, « q est indépendante de la vérité » [RAPPORTÉ, § 3], et B lui-même montre (§ 1.1) qu'il faudrait β ≈ 27 pour que l'éloignement pèse autant qu'un facteur 9 de q² [calcul de B, que je retrouve : ln 9 / −ln 0,922 ≈ 27]. Les témoins O4 et b_eloigne n'ont **pas** de q. Si Z perd contre O4 dans E1, on ne saura pas si c'est w(C) qui n'apporte rien ou q qui ajoute du bruit. L'ablation Z₀ (α = 0) isole w(C) dans le même régime de q, mais ne sauve pas la comparaison Z contre max(O4, Z₀, b_eloigne), qui est pourtant le critère d'adoption. [OBSERVÉ-NON-AUDITÉ]

**B-a2. E2 est vrai par construction dans les mondes de la pièce B, et B le sait (S5) sans en tirer la conséquence.**
La vérité des mondes est « opérateur latent non moyeu commun » [RAPPORTÉ, § 5] : une paire valide partage typiquement une étiquette. Pour des vecteurs de concepts creux, C_ij ne varie alors qu'avec l'IDF de l'étiquette partagée et le nombre d'étiquettes de chaque fiche. Dans le **monde sans moyeu** d'E2, l'IDF des étiquettes partagées devient presque constant ; w(C) devient une constante sur les paires valides et Z ≡ Z₀ à l'arrondi près. H_B (« équivalence ») est alors vraie quel que soit le mécanisme réel : E2 ne peut pas falsifier H_B. Pour qu'E2 ait un sens, il faut des mondes où le recouvrement conceptuel est gradué — exactement l'extension que B refuse en S5 comme « tautologique ». Il y a une tension interne non résolue : soit on étend les mondes (et il faut spécifier l'observation des concepts pour éviter la tautologie), soit E2 est vide.

**B-a3. E3 (« monde import ») passe ou s'arrête par construction.**
Dans ce monde, les vrais ponts n'ont « pas de partage d'opérateur ». Mais l'étage commun exige une étiquette partagée pour qu'une paire soit valide [RAPPORTÉ, § 5]. Les vraies paires ne sont donc jamais valides, et la précision vaut 0 pour tous les bras. Alors Δ_import = 0 pour Z et Δ_import − Δ_normal = −Δ_normal < 0 pour tout bras qui gagne dans le monde normal : H_A passe trivialement, par le mécanisme même que la pièce B dénonce en § 7.2. Et le témoin b_eloigne y tombe lui aussi à 0, ce qui déclenche l'arrêt prévu par B (« s'il chute, on arrête »). E3 est donc soit trivialement positif, soit auto-abortif. Pour le rendre jugeable, il faut relâcher l'étage commun dans ce monde (paires valides sans pont d'étiquette) et le dire d'avance.

**B-a4. α, β et w ne sont pas gelés ; la procédure de fixation est une fuite potentielle.**
B écrit « à geler par Lazar » et prévoit un pilote « sur graines de validation distinctes, sans lecture des écarts ». Mais un pilote qui fixe α et β doit bien lire *quelque chose* ; si c'est la précision, c'est une lecture des écarts. Il faut dire quelle statistique (indépendante de la vérité plantée) sert à fixer α et β, ou les fixer a priori (par exemple β tel que la pénalité à cos = 0,28 vaille un rapport donné).

**B-a5. E5 teste le mauvais canal de manipulation.**
B recommande que le tirage n'utilise que R2 (étiqueteur-modèle hors boucle). Mais R2 lit le **texte** de la fiche, que le proposeur écrit. E5 ne mesure que l'inflation du champ déclaré R1, que le tirage ignore déjà : H_A y est vraie par construction. La manipulation pertinente est textuelle (insertion de termes rares dans le corps), et E5 ne la mesure pas. Ce n'est pas une conduite d'agent que de planter des jumelles textuelles dans un monde : c'est un cas honnête apparié.

**B-a6. Le noyau de lot K ne diversifie que les couples de domaines, pas les ponts.**
K_(ij),(kl) = ½[S_ik S_jl + S_il S_jk] avec S Gram des domaines : deux paires (i,j), (i,l) qui réutilisent la fiche i et le même pont rare, avec j et l dans des domaines orthogonaux, ont K ≈ 0 et ne se repoussent pas. Le lot peut donc dépenser ses trois fusions sur le même pont rare — reproche que C adresse à sa propre option 1b. B présente O3 comme un « stratifié pondéré » ; c'est exact, et cela veut dire qu'il n'ajoute rien au stratifié sur l'axe conceptuel. [OBSERVÉ-NON-AUDITÉ]

**B-a7. S1 est une bonne lecture, mais incomplète.**
Je confirme la lecture de B : le code trie les paires par s_ij croissant puis en garde max_paires = 3 [VÉRIFIÉ, pièce A, `paires.sort(key=lambda p: p[:3])`, `paires[:max_paires]`], alors que le bras (a) range « par (rang maximal, somme des rangs) » avec k = 4 paires [RAPPORTÉ, § 5]. Mais B oublie que le code tire **4 articles**, donc au plus 6 paires, dont 3 fusionnées ; un bras (a′) « code tel quel » n'a pas le même budget que les autres (12 paires sur 3 générations). Il faut soit porter k à 6 articles (15 paires, 4 gardées), soit comparer à budget égal en nombre de fusions, sinon l'écart (a′) − (b) est confondu par le budget.

**B-a8. Le passage à la course 2 n'a pas de puissance.**
Avec max_paires = 3 et 3 générations, chaque bras produit 9 fusions. Pour deux taux de filles recevables de 0,30 et 0,45 (illustratifs), l'erreur type de la différence vaut environ 0,22 [calcul] : rien n'est détectable. B l'admet en partie (« ne tranche pas E1 »), mais propose quand même un protocole de lecture ; il faut dire combien de fusions seraient nécessaires, ou renoncer.

**B-a9. Points mineurs.** Le contrôle « concept leurre » d'E2 confond « plusieurs étiquettes partagées » et « parasites et homonymes » ; si Z y gagne, cela peut venir de l'IDF des parasites (dépend de leur fréquence) et non d'un artefact de mesure. Les références de la section 4 sont attribuées (auteurs, année, titre) ; je ne peux pas les vérifier et ne le prétends pas.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **E1.** Si l'écart-type apparié σ_d de Z − O4 sur les mondes donne σ_d/√n > δ/3,24 (δ = 2, α unilatéral 2,5 %, puissance 90 %), la supériorité n'est pas détectable ; B part de σ_d ≈ 0,77·√400 ≈ 15 points par monde [calcul sur la demi-largeur 1,5 de la pièce B], mais la variance de Z − O4 n'est pas celle de (a) − (b). Zone d'indifférence : si le vrai effet est entre 1 et 2 points, ni H_A (gain ≥ 2, IC > 0) ni H_B (TOST à ±2, qui demande un IC à 90 % de demi-largeur ≈ 1 entièrement dans ±2) n'est atteignable avec probabilité élevée ; l'issue « non concluant » est alors la plus probable, et les conditions « bien ET moyen » multiplient ce risque.
- **E2.** Si Var(C_ij | paire valide) → 0 dans le monde testé (étiquettes partagées d'IDF quasi constant), Z ≡ Z₀ et H_B est vraie par construction. Mesure à préenregistrer : coefficient de variation de C_ij parmi les paires valides, seuil minimal gelé.
- **E3.** Si P(vraie paire ∈ paires valides) = 0 sous l'étage commun, précision ≡ 0, test non jugeable (B-a3).
- **E4.** L'AUC exige un nombre suffisant de paires inter-domaines partageant un opérateur ; avec 8 domaines × 5 articles et une couverture 0,45 (monde « mal observé » [RAPPORTÉ]), ce nombre peut tomber sous quelques dizaines par monde et l'AUC a un intervalle qui couvre 0,5. Le « ratio intra / inter entre fiches d'opérateurs différents » est 0/0 quand l'espérance de la similarité inter est nulle (vecteurs creux) : non jugeable ; prendre une différence, pas un rapport, et exiger un dénominateur minimal.
- **E5.** Si la garde est le mécanisme IDF, l'inflation par des opérateurs **rares** n'est pas pénalisée ; le test n'a de puissance que contre l'inflation par moyeux. Condition : la distribution des étiquettes injectées doit couvrir les deux queues de l'IDF.
- **Placebo.** Le taux d'intervalles excluant 0 (3,2 % en pièce B) n'est interprétable que sur plusieurs dizaines de conditions ; sur une seule, un intervalle qui exclut 0 a 5 % de chance de survenir par hasard et ne devrait pas être un critère d'arrêt à lui seul.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Concepts permutés dans le tirage** (pas seulement dans E4) : Z avec les vecteurs de concepts permutés entre fiches doit retomber au niveau de Z₀. H_A : Z_perm − Z₀ a un IC contenant 0 ; H_B : Z_perm garde un gain, et w(C) agit par un artefact (par exemple la longueur des vecteurs). Absent chez B.
2. **q permutée** : Z avec q mélangée entre fiches doit égaler Z (puisque q ⊥ vérité dans ces mondes). Si Z chute, q porte de l'information fuitée du générateur. Absent.
3. **Étage commun sans « opérateur le plus rare »** : le choix post-tirage de l'opérateur le plus rare [RAPPORTÉ, § 5] est déjà une forme de (d1) appliquée à tous les bras ; il faut une version où l'opérateur retenu est tiré au hasard, sinon l'apport de w(C) est partiellement absorbé par l'étage commun. Absent.
4. **Bras (a′) à budget égal** (B-a7) : sans lui, S1 reste une conjecture.
5. **E3 réécrit** avec étage commun relâché, sinon le contrôle inversé est vide.

---

## Sur la proposition C

### (a) Défauts de méthode

**C-a1. Les mondes étendus (§ 3.1) sont vrais par construction tant que l'observation de l'espace C n'est pas spécifiée.**
C distingue « concept profond » et « terme de surface » dans la vérité plantée, mais ne dit jamais comment le vecteur c_i est **observé** dans le monde : couverture, parasites, homonymes, comme la pièce B le fait pour les opérateurs à trois niveaux [RAPPORTÉ, § 5]. Si le générateur étiquette « profond » et « surface » et que l'extracteur a accès à cette distinction (lexique scellé), le bras (f) gagne par construction. Je me sers ici de S5 de B, en le disant : B a vu le risque, C y tombe. Deux cas seulement sont honnêtes : (i) les termes de surface ne se distinguent des concepts que par leur fréquence documentaire — mais alors (d1) les évite déjà et le Duel 2 ne teste pas « le concept », il reteste l'IDF ; (ii) ils s'en distinguent par autre chose, et il faut dire quoi et avec quel bruit.

**C-a2. Le test de séparabilité (Mantel r_M < 0,10) n'a pas de ligne de base latente.**
Dans les mondes de la pièce B, les opérateurs sont partagés par **groupe** (« 3 opérateurs latents par groupe ») [RAPPORTÉ, § 5] et le partage de fond est concentré dans les champs [RAPPORTÉ, § 6] : la similarité conceptuelle **vraie** est corrélée à la proximité de domaine par construction du monde. Une représentation parfaitement honnête aurait un r_M > 0 dû au monde, non à la fuite. Le critère de C rejetterait une représentation honnête dans un monde réaliste, ou accepterait une représentation fuyante dans un monde où les concepts sont orthogonaux aux domaines. La fuite se mesure par r_M(observé) − r_M(latent, oracle) ; C n'a pas cette soustraction. Même remarque pour l'AMI.

**C-a3. Le Duel 1 est mal posé sur trois points.**
- Le noyau de sommets proposé pour H_B, S_ij = exp(−τ⟨d_i,d_j⟩²), est **petit pour les domaines proches et grand pour les éloignés** : dans un DPP, c'est une répulsion entre domaines **éloignés**, l'inverse de ce que H_B veut. La pièce B parle d'« exponentielle du cosinus » [RAPPORTÉ, § 6], ce qui désigne plutôt exp(τ cos) ou exp(τ cos²), semi-défini positif par exponentielle entrée par entrée d'un Gram. Tel quel, H_B est falsifiée avant tout run, et pas pour la bonne raison. [OBSERVÉ-NON-AUDITÉ, lecture de la formule]
- τ est « balayé » sur les mêmes mondes qui servent à juger : choisir le meilleur τ après coup favorise H_B par sélection ; il faut des graines de calibrage distinctes.
- Les issues ne sont pas exhaustives : si l'écart tombe entre +2 et +8, ou si la part de paires éloignées du Node-DPP dépasse 0,58 sans atteindre 0,65, aucune hypothèse n'est falsifiée et rien n'est dit (B4).

**C-a4. Le contrôle m = 1 du Duel 3 est faux tel qu'écrit.**
C affirme que 1b et 1c « sélectionnent mathématiquement la même paire » à m = 1. Mais w_ij (1b) utilise Σ idf² **non normalisé** et (1−cos²)^{α_D}, tandis que Q_e (1c) utilise un cosinus IDF **normalisé** et √(1−cos²). Les deux ordres ne coïncident pas en général. Le contrôle, s'il est exécuté, échouera pour une raison de définition, et déclenchera à tort la conclusion « artefact ». Il faut un score unique partagé par 1b et 1c, ou retirer ce contrôle.

**C-a5. Q_e confond proximité conceptuelle et nombre d'étiquettes observées.**
⟨c_i,c_j⟩_IDF normalisé décroît avec ‖c_i‖‖c_j‖, donc avec le nombre d'étiquettes de chaque fiche, qui est gonflé par les parasites (0,05 à 0,30 selon le niveau d'observation [RAPPORTÉ, § 5]). Une fiche bruitée est pénalisée indépendamment de son pont. Dans les mondes « moyen » et « mal observé », un gain ou une perte de (f) peut refléter la distribution des parasites, pas le concept. De plus, Φ(e) divise c_i ⊙ c_j par sa norme : si le pont est détecté par `ponts(a, b)` sur `operateurs` mais que les vecteurs de concepts ne partagent rien (lexiques distincts), on divise par zéro ; C ne dit pas que les deux lexiques coïncident.

**C-a6. Même confondante q que B.** (q_i q_j)^β reste dans Q_e, avec β libre, alors que les témoins b_eloigne et (d1) n'ont pas de q. L'ablation q ≡ 1 n'est prévue qu'au Duel 1.

**C-a7. L'option 2c ne résiste pas à ce qu'elle prétend bloquer.**
« Deux marqueurs formels dans le texte » est aussi gratuit qu'une déclaration. Le plafond |C_i| ≤ 3 peut tronquer l'opérateur-pont vrai : dans les mondes, une fiche porte 3 opérateurs latents de groupe, des opérateurs propres et un moyeu dans 25 % des cas [RAPPORTÉ, § 5] ; la probabilité que le pont vrai soit parmi les 3 déclarés est une mesure à préenregistrer. Enfin, calculer d_i « après soustraction du lexique mathématique » change la calibration des cosinus (0,54 / 0,28 / 0,03) dont tout le banc dépend ; la pièce B montre qu'un changement de pondération a déjà rendu les domaines indiscernables (TF-IDF : 0,11 contre 0,009) [RAPPORTÉ, § 9]. Il faut revalider le générateur après soustraction, et C ne le prévoit pas.

**C-a8. Statuts abusés.**
C marque VÉRIFIÉ ses propres dérivations (« VÉRIFIÉ mathématiquement », « puissance VÉRIFIÉE », « 0,00 USD VÉRIFIÉ »). Dans les faits, VÉRIFIÉ désigne le contenu des pièces par empreinte. Une dérivation de C est au mieux un calcul, et la puissance « > 0,99 » suppose que la variance de (f) − (b) est celle de (a) − (b), ce qui est une HYPOTHÈSE. Les « confiances 0,85 / 0,80 » sont des chiffres sans source. C traite le juge K1–K5 de la pièce C comme établi alors que c'est un brouillon « non contre-lu, non servi » avec des « [à trancher par Lazar] » [VÉRIFIÉ, en-tête et texte de la pièce C] ; je me sers ici de S6 de B. Les numéros de ligne cités pour la pièce A (142, 157-180, 212, 265…) ne sont pas vérifiables par moi : OBSERVÉ-NON-AUDITÉ.

**C-a9. Course 2 : 9 fusions par bras et un seuil de +15 points.** Même défaut que B-a8, mais chiffré : avec n = 9 et des taux de 0,30 contre 0,45 (illustratifs), la puissance est de l'ordre de 10 % [calcul]. Le seuil de « fréquence > 25 % » pour un moyeu est un paramètre du monde synthétique transposé sans justification aux fiches réelles. Le gain de « log W » repose sur le module `memoire`, non servi.

**C-a10. Le signe du terme conceptuel.** C ignore l'ambiguïté des mots rapportés de Lazar (« minimise leur proximité conceptuelle ») que B relève en S2. Si la lecture (ii) de B est confirmée, Q_e change de signe et les trois duels sont à réécrire ; C n'a pas de clause pour ce cas.

**C-a11. Antériorité.** C écrit « Stanley, Lehman (2011) » là où B écrit « Lehman et Stanley (2011) » pour le même titre ; ma mémoire va dans le sens de B, mais c'est à vérifier sur PDF. C présente l'Edge-DPP à qualité bisociative comme « zone vierge » ; c'est une question (R8), que B pose aussi ; aucune des deux ne cite de recherche faite.

### (b) Conditions mesurables de perte de puissance ou de non-jugeabilité

- **Seuil d'adoption.** « Borne inférieure de l'IC > +9 » pour une cible de +12 demande une demi-largeur < 3 ; si σ_d par monde dépasse environ 30 points (soit deux fois celui de la pièce B [calcul]), l'adoption devient impossible même quand l'effet vrai est +12. De même, « (f) − b_eloigne ≥ +3 avec borne inf > +1 » exige une demi-largeur < 2 ; la variance de cette différence est inconnue et peut être plus grande que celle de (a) − (b) si (f) et b_eloigne tirent des lots très corrélés (différence petite mais instable) ou très différents.
- **Duel 2.** Si df(termes de surface) ≫ df(concepts), (d1) et (f) coïncident sur le piège de surface et l'écart (f) − b_eloigne mesure l'IDF, pas le concept. Condition de jugeabilité : rapport des IDF moyens surface / concept gelé et proche de 1.
- **Duel 1.** Si, pour un τ, le noyau de sommets n'est pas défini positif, `tirage_glouton` saute les candidats (le `except NonDefiniePositive: continue` de la pièce A [VÉRIFIÉ]) et le bras dégénère silencieusement ; mesurer la fraction de mondes où le lot est plus court que k.
- **Q_e et parasites.** Si la corrélation de rang entre Q_e et |C_i| + |C_j| diffère de 0 dans un monde sans vérité (placebo), le score est biaisé par la longueur des vecteurs.
- **Mantel.** Si r_M(latent) > 0,10 dans les mondes (vraisemblable au vu de § 5 et § 6 de la pièce B), le critère rejette l'honnête : non jugeable sans ligne de base.
- **Monde inversé corrigé.** Δ_inv(f, c) − Δ_norm(f, c) ≤ −10 est satisfait par tout bras qui cible l'éloignement, y compris b_eloigne seul ; il ne discrimine pas « deux espaces » de « éloignement seul » : puissance nulle sur la question posée.
- **Liste d'arrêt 1.** « NonDefiniePositive sur ≥ 1 % des mondes avec γ = 10⁻³ » : avec S^paire semi-défini et Q_e ≥ 0, K + γI est défini positif en exact ; les échecs viendront de l'arithmétique (pivots ≈ 10⁻¹² quand Q_e ≈ 0) et ce seuil mesurera la précision flottante, pas la conception.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Concepts permutés entre fiches** pour (f) : H_A : (f)_perm retombe au niveau de b_eloigne (IC de la différence contenant 0) ; H_B : (f)_perm garde un gain, donc le gain de (f) ne vient pas des concepts. Absent chez C.
2. **Oracle latent pour la séparabilité** : la représentation vraie (opérateurs latents) soumise au même test de Mantel/AMI ; H_A : elle passe le critère ; H_B : elle le rate, et le critère mesure le monde, pas la fuite. Absent.
3. **Graines de calibrage distinctes pour τ, α_D, β** : H_A : le meilleur τ sur les graines de calibrage est aussi le meilleur sur les graines d'évaluation ; H_B : non, et le Duel 1 a sélectionné sur le bruit. Absent.
4. **Observation bruitée de C aux trois niveaux** de la pièce B (0,90 / 0,70 / 0,45 de couverture) : H_A : l'écart (f) − b_eloigne persiste à couverture 0,45 ; H_B : il s'annule, et l'ingrédient n'est utile qu'avec des concepts presque parfaitement observés. Absent (C-a1).
5. **q ≡ 1 dans tous les duels**, pas seulement le premier : H_A : les écarts ne changent pas ; H_B : ils changent, et q confond.
6. **Contrôle m = 1 corrigé** (score unique) : sinon le Duel 3 déclare un artefact par définition.
7. **Revalidation du générateur après soustraction du lexique** (C-a7) : H_A : cosinus 0,54 / 0,28 / 0,03 retrouvés sur graines de validation ; H_B : non, et l'hypothèse d'éloignement n'est plus satisfaite par le monde.

---

## Point commun, dit pour chacune et non fusionné

B et C gardent toutes deux la qualité q dans le score d'une paire, alors que le seul audit disponible [RAPPORTÉ, pièce B § 3] la montre indépendante de la vérité et dominante dans l'ordre glouton. Chez B, c'est √(q_i q_j) ; chez C, (q_i q_j)^β. Dans les deux cas, les témoins forts (b_eloigne, d1, O4) n'ont pas de q, et l'écart mesuré n'attribue pas. Chacune doit préenregistrer soit β = 0, soit une ablation q ≡ 1 systématique, soit un monde où q est corrélée aux ponts (non testé, pièce B § 6) — et dire lequel avant le run.

FIN-DE-CELLULE