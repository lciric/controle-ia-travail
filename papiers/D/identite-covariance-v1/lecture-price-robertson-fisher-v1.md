# Lecture de Price (1970), Robertson (1966) et d'une recension de Fisher (1930), pour l'identité de variance du théorème 1 — v1

Lecteur neuf, Claude Opus 5.5, effort élevé, 24 novembre 2026. Aucun fichier du dépôt n'a été modifié.

## Verdict

- **Price 1970 : citation juste.** Notre identité est l'équation (4) de Price (p. 520) avec trois choix : valeur sélective z = β, trait q = β, terme de transmission nul (Δq_i = 0). Le dénominateur z̄ = E_μ[β] y est déjà. Price prévoit lui-même cet usage hors de la génétique, sur un exemple de sélection par survie (p. 520). L'algèbre est vérifiée en arithmétique exacte.
- **Robertson 1966 : citation juste, mais il faut citer les pages.**
  - L'identité de covariance figure bien dans cet article, sous deux formes :
    - la forme phénotypique, où la différentielle de sélection vaut la covariance avec la survie divisée par la survie moyenne (p. 97) ;
    - la forme génétique, appelée aujourd'hui « secondary theorem » : ΔG = cov(cX)_g, où c est la survie relative (p. 99).
  - Robertson annonce un développement théorique « ailleurs » (p. 106). Ce texte ultérieur n'a pas été lu ici.
- **Fisher 1930 : citation partiellement juste et surdimensionnée, non opposable jusqu'à la lecture du chapitre II.**
  - Notre forme est l'**analogue en temps discret, à transmission parfaite et sans génétique**, du théorème fondamental. Elle n'est pas le théorème lui-même, qui porte sur la variance génétique additive de la valeur sélective malthusienne.
  - « the variance form being Fisher's fundamental theorem » et « i.e. Fisher's (1930) fundamental theorem in this setting » sont à affaiblir.
  - La recension fournie ne dit rien du théorème fondamental.

## 1. Price 1970, « Selection and Covariance », Nature 227:520–521

Le PDF est un scan sans couche de texte. Je l'ai rendu en images (`img/price-1.png`, `img/price-2.png`) et lu à l'écran.

**Énoncé (p. 520, colonne de gauche).**
- Équation (1) : « ΔQ = Cov(z,q)/z̄ ».
- Elle est donnée comme valable « for a single gene or for any linear function of any number of genes at any number of loci », quels que soient la dominance, l'épistasie et le mode de reproduction.
- Forme par régression, juste en dessous : ΔQ = β_zq σ_q²/z̄.

**Usage hors génétique (p. 520, colonne de droite, haut).**
- Citation : « It can also be applied to non-genetical selection. For example, if students' expectations of passing a certain course vary with IQ and if student IQs do not change appreciably during the course, then equation 1 (with its variables suitably redefined) will give the difference in mean IQ between students entering the course and those completing it (and equation 4 below will apply if IQs do change during the course). »
- C'est exactement notre structure : une sélection par survie, avec un trait qui ne change pas.

**Dérivation (p. 520, colonne de droite).**
- z_i est le nombre de gamètes « réussis » de l'individu i, c'est-à-dire sa valeur sélective ; q_i est la fréquence du gène chez i ; Δq_i = q′_i − q_i.
- Équation (3) : Q₂ = q̄ + Cov(z,q)/z̄ + Σz_iΔq_i/Nz̄.
- Équation (4) : ΔQ = Q₂ − Q₁ = Cov(z,q)/z̄ + Σz_iΔq_i/Nz̄.
- L'équation (1) est l'équation (4) quand le second terme, le terme de transmission, est nul ou s'annule en moyenne.
- La covariance est celle de la population (dénominateur N, « population variable », p. 520).

**Notre identité comme cas particulier.**
- On prend la loi μ_tr = π_no(· | Π_tr) comme population P₁, z_i := β, q_i := β et Δq_i := 0.
- Δq_i = 0 tient parce que β est une fonction fixe de la politique : un survivant garde son β.
- La loi des survivants est π_A(· | Π_tr), de densité β/E_μ[β] par rapport à μ_tr (preuve de la partie 1 du manuscrit). Elle joue le rôle de P₂.
- L'équation (4) donne alors : E_{π_A}[β | Π_tr] − E_μ[β] = Cov_μ(β, β)/E_μ[β] = Var_μ(β)/E_μ[β].
- Conditions, toutes satisfaites :
  1. aucun terme de transmission ;
  2. w = β ;
  3. z = β ;
  4. normalisation par w̄ = E_μ[β] > 0 (l'équation (1) l'inclut déjà) ;
  5. moments pris sous μ_tr, sans correction d'échantillon.
- Nuance : l'équation imprimée de Price est écrite pour une fréquence génique. Notre usage relève de la clause « with its variables suitably redefined » de la p. 520, que Price énonce lui-même.

**Vérification par calcul** : `verif_price_robertson_v1.py`, sortie dans `verif_price_robertson_v1.out`, arithmétique exacte (`fractions`).
- L'exemple du manuscrit (poids 1/2, 1/3, 1/6 ; survies 1/10, 2/5, 9/10) donne 37/150 par les quatre voies :
  1. repondération directe ;
  2. Cov/z̄ de Price ;
  3. Q₂ − Q₁ par l'équation (3) ;
  4. Var/E.
- Sur 2 000 tirages rationnels, les quatre voies coïncident, ainsi que les trois premières avec un trait quelconque distinct de β.
- L'exemple de la variante R2 (survie à l'audit 1/2 → 37/50) est retrouvé comme 1/2 + Cov/E = 1/2 + 6/25.

**Remarque.** Price écrit qu'une relation aussi simple n'a pas, à sa connaissance, été reconnue auparavant (p. 521, point « Fifth »). Il ne cite pas Robertson.

## 2. Robertson 1966, « A mathematical model of the culling process in dairy cattle », Animal Production 8:95–108

Couche de texte présente. Les équations des pages 97 et 99 ont été relues sur image (`img/rob-04.png`, `img/rob-06.png`). La page 1 du PDF est une page de garde ; la page 2 du PDF est la p. 95 de la revue.

**Forme phénotypique, intra-génération (p. 97).**
- q̄ = Kp est la survie moyenne. L'équation (3) exprime la survie relative (1/q̄)(dq/dy).
- Citation : « Since the covariance of yield with survival is q̄D, it follows that the regression coefficient of relative survival on yield is given by (1/q̄) b_qy = D/V_t … (4) ».
- D est la différentielle de sélection, c'est-à-dire l'écart de rendement moyen entre les survivantes et l'ensemble.
- L'affirmation se lit donc D = Cov(y, q)/q̄. C'est notre identité avec le trait y remplacé par β : D = Cov(β, β)/E[β] = Var(β)/E[β].
- Robertson l'énonce en passant, sans démonstration, pour le rendement laitier.

**Forme génétique, le « secondary theorem » (p. 99).**
- Citation : « It can easily be shown that the expected change ΔG_X in a character X produced by any selection process is given by the expression ΔG_X = V_gX b_cX.g ».
- V_gX est la variance génétique du caractère. b_cX.g est la régression génétique de l'avantage sélectif sur le caractère.
- Robertson définit l'avantage sélectif au haut de la même page comme la survie relative : « relative survival (or, in the term generally used in population genetics, selective advantage) », phrase qui commence p. 98.
- Il ajoute : « This equation applies to all characters, irrespective of the nature of the selection itself. » Puis : « ΔG = cov(cX)_g = 4 cov(cS) ».
- La démonstration n'est pas donnée (« It can easily be shown »).

**Résumé de l'article (p. 107, point 6).**
- Citation : « A direct estimate of the genetic gain by selection can, however, be obtained from the covariance for any character between the mean relative survival of progeny groups and their mean value for the character. »

**Paternité.**
- L'identité de covariance figure bien dans cet article : la forme phénotypique p. 97, la forme génétique p. 99.
- L'article annonce une suite à la discussion (p. 106) : « The covariance between survival and character … can be used to give a direct estimate of the genetic change due to culling. The theoretical aspects of this will be further developed elsewhere. »
- Il ne cite aucun texte de Robertson de 1966 ou 1968 sur ce point. Ses références (p. 107–108) sont Abplanalp 1961, Barker et Robertson 1966 (lactations), Curnow 1961, Hinks 1965, Robertson et Lerner 1949.
- Le développement « ailleurs » est vraisemblablement Robertson 1968 (« The spectrum of genetic variation »), d'après ce que je sais. C'est **non opposable** : ce texte n'a pas été lu.
- Citer Robertson 1966 n'est donc pas une erreur de citation, mais le citer sans page cache que :
  - la forme qui nous sert, phénotypique et sans hérédité, n'y est qu'énoncée en passant (p. 97) ;
  - la forme célèbre est génétique (p. 99).
- Dans notre cadre, β est transmis parfaitement : un survivant garde son β, comme si l'héritabilité valait 1. Covariance génétique et covariance phénotypique y coïncident ; les deux pages s'appliquent.

## 3. Fisher 1930 — non opposable jusqu'à la lecture du chapitre II

**Recension (PDF de 5 pages, pp. 167–171 d'une revue non identifiée, signée Charles A. Berger, S.J., p. 171).**
- Elle confirme l'éditeur pour l'édition américaine (« New York: Oxford University Press. Pp. 272 », p. 167) et cite la p. 20 du livre.
- Le reste porte sur la dominance, les mutations et la stabilité du gène (pp. 168–171).
- **Elle ne dit rien du théorème fondamental ni de la variance de la valeur sélective.** Elle ne peut rien trancher ici.

**Ce que je peux juger sans le livre, d'après ce que je sais, non opposable.**
- **(a) Le théorème porte-t-il sur la variance génétique additive de la valeur sélective ?**
  - Oui, selon la lecture courante : « The rate of increase in fitness of any organism at any time is equal to its genetic variance in fitness at that time » (chapitre II). La « genetic variance » de Fisher est ce qu'on appelle aujourd'hui la variance génétique additive.
  - La valeur sélective est le paramètre malthusien, en temps continu.
  - Selon la lecture de Price 1972 et d'Ewens 1989 (non lus ici), le théorème donne la seule part du changement de valeur sélective moyenne due à la sélection naturelle, l'« environnement » étant tenu fixe. Il ne donne pas le changement total.
  - Page et formulation exactes à vérifier dans le chapitre II.
- **(b) Notre « forme de variance » est-elle « Fisher's fundamental theorem in this setting » ?**
  - Seulement par analogie.
  - Dans notre cadre, il n'y a pas de génétique. La survie β est à la fois le trait et la valeur sélective. La transmission est parfaite, comme chez des clones. Il y a une seule étape discrète, et la valeur sélective est une probabilité de survie, non un taux malthusien.
  - Dans ce cas, toute la variance est trivialement « additive ». Le changement partiel égale le changement total, faute de termes de dominance, d'épistasie ou d'environnement. L'équation Δw̄ = Var(w)/w̄ est alors l'analogue discret et clonal du théorème. Le théorème en temps continu, appliqué à des clones, s'écrirait dm̄/dt = Var(m).
  - Ce n'est pas le théorème de Fisher lui-même. L'écrire « i.e. Fisher's fundamental theorem » ou « the variance form being Fisher's fundamental theorem » attribue à Fisher un énoncé discret sur la survie qu'il n'a pas écrit sous cette forme (à vérifier au chapitre II).
  - Formulation défendable : « the discrete-time, perfect-transmission analogue of Fisher's (1930) fundamental theorem ».

## 4. Phrases corrigées proposées (anglais)

Les phrases ne revendiquent rien de plus. Le passage marqué [F] dépend de la lecture du chapitre II du livre de Fisher : tant qu'elle n'est pas faite, on peut le retirer purement et simplement, sans perte pour la preuve.

**Résumé** (on précise quel terme de l'équation sert et quel rôle joue la survie) :
> « conditional stealth enrichment follows from a variance identity: the selection term of Price's covariance equation, with survival as both fitness and trait [price1970; see also robertson1966]. »

Variante plus courte, si la place manque :
> « conditional stealth enrichment follows from a variance identity, a special case of the Price–Robertson covariance identity. »

Cette phrase est déjà juste. On peut la garder telle quelle ; seule la contribution 2 et le billet appellent une correction.

**Contribution 2 :**
> « under Operator A we restate the variance identity for conditional enrichment: it is Price's covariance equation [price1970, Eq. (4), p. 520] with survival as both fitness and trait and no transmission term, equivalently Robertson's selection differential as a covariance with relative survival [robertson1966, pp. 97, 99]; [F] it is the discrete-time, perfect-transmission analogue of Fisher's fundamental theorem [fisher1930, Ch. II]. »

Version sans [F], si le chapitre II n'est pas lu avant envoi : supprimer le passage après le dernier point-virgule.

**Billet** (ligne 55) :
> « This is Price's (1970) covariance equation, with survival as both the fitness and the trait and no transmission term; Robertson (1966) states the same covariance form for selection by culling. [F] In this clonal, one-step setting it is the discrete-time analogue of Fisher's (1930) fundamental theorem, not the theorem itself, which concerns the additive genetic variance in (Malthusian) fitness. »

**Billet, ligne 17** (point de synthèse), même correction :
> « (a special case of the Price–Robertson covariance identity; [F] its variance form is a discrete-time analogue of Fisher's fundamental theorem) »

**Billet, ligne 119** (« Prior work ») : la phrase est juste pour Price et Robertson, qui couvrent aussi l'identité de covariance de la variante R2. Pour Fisher, écrire « (Price 1970; Robertson 1966; and, for the variance form, an analogue of Fisher 1930) » ou retirer Fisher.

**Bibliographie** :
- Les références de Price et Robertson sont exactes (revue, volume, pages vérifiés sur les PDF).
- Pour Fisher, « Clarendon Press, Oxford, 1930 » n'est pas vérifiable ici. La recension ne donne que l'édition américaine d'Oxford University Press, New York, 272 pages (p. 167).

## 5. Limites de ma lecture

- Le livre de Fisher n'a pas été lu. Tout ce qui le concerne, en § 3 et dans les passages [F], est non opposable : formulation, page, sens de « genetic variance ».
- Robertson 1968 (« The spectrum of genetic variation »), Price 1972 (« Fisher's “fundamental theorem” made clear ») et Ewens 1989 sont cités de mémoire comme pistes, non lus, non opposables.
- Je n'ai pas vérifié que l'expression « Price–Robertson identity » (ou « Robertson–Price ») est d'usage établi dans la littérature.
- Price 1970 est un scan. Les équations ont été lues sur images rendues à 150 points par pouce. Elles sont lisibles, mais sans couche de texte pour les recopier mécaniquement.
- La recension n'a ni revue ni date identifiées. D'après son contenu (congrès de septembre 1930, p. 168 ; livre de 1931 recensé à la suite, p. 171), elle date vraisemblablement de 1931.
- Le calcul vérifie l'algèbre de l'identité, pas la modélisation (Operator A comme repondération par β), qui relève du manuscrit.

Fichiers : extraits texte `*.txt`, images `img/`, script `verif_price_robertson_v1.py` et sa sortie `verif_price_robertson_v1.out`, tous dans `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/identite-covariance/`.
