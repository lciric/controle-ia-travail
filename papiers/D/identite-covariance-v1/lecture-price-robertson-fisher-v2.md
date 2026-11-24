# Lecture de Price (1970), Robertson (1966), Fisher (1930), Price (1972) et Frank et Slatkin (1992), pour l'identité de variance du théorème 1 — v2

Lecteur neuf, Claude Opus 5.5, effort élevé, 24 novembre 2026. La v2 remplace la v1 (`lecture-price-robertson-fisher-v1.md`), qui reste intacte. Aucun fichier du dépôt n'a été modifié.

## Verdict

- **Price 1970 : citation juste.** Inchangé depuis la v1.
- **Robertson 1966 : citation juste, avec les pages 97 et 99.** Inchangé depuis la v1.
- **Fisher 1930 : la citation, telle qu'écrite, est inexacte. La marque [F] de la v1 est levée, et le jugement « analogue » est confirmé, sur pièces.**
  - Fisher énonce le théorème p. 35 (p. 59 du PDF), en temps continu, pour le paramètre malthusien m, et avec la « genetic variance » au sens additif.
  - Notre identité n'est ni ce théorème ni un cas particulier exact de son énoncé. C'est l'**analogue en un pas de temps discret**, pour des types qui se transmettent à l'identique et dans un environnement tenu fixe, de la **composante du changement de valeur sélective moyenne due à la sélection naturelle**, au sens de la lecture de Price 1972 et de Frank et Slatkin 1992.
  - Dans notre cadre, cette composante est d'ailleurs tout le changement.
  - Deux formules sont à corriger :
    - « the variance form being Fisher's fundamental theorem » (contribution 2) ;
    - « i.e. Fisher's (1930) fundamental theorem in this setting » (billet).
- La notice bibliographique `fisher1930` (« Clarendon Press, Oxford, 1930 ») est **exacte**, vérifiée sur la page de titre.

## 1. Fisher 1930 — chapitre II, lu sur le scan

**Le livre.**
- Page de titre (p. 13 du PDF, relue sur image) : « THE GENETICAL THEORY OF NATURAL SELECTION BY R. A. FISHER, Sc.D., F.R.S. OXFORD AT THE CLARENDON PRESS 1930 ».
- Verso de la page de titre (p. 14 du PDF) : « Printed in Great Britain ».
- La notice du manuscrit est donc juste.
- Correspondance des pages : dans le chapitre II, page imprimée n = page n + 24 du PDF. Je l'ai contrôlé sur les pp. 25–37 et 41–42.

**L'énoncé exact (p. 35 imprimée, p. 59 du PDF, relu sur image à 300 points par pouce).**
- La phrase qui précède : « If therefore the time element dt is positive, the total change of fitness W dt is also positive, and indeed the rate of increase in fitness due to all changes in gene ratio is exactly equal to the genetic variance of fitness W which the population exhibits. We may consequently state the fundamental theorem of Natural Selection in the form: »
- L'énoncé, en italique : « *The rate of increase in fitness of any organism at any time is equal to its genetic variance in fitness at that time.* »
- La dérivation finit en haut de la même page sur « Σ(α dp) = Σ(pqaα) dt = W dt ». Ici a est l'excès moyen (« average excess ») et α l'effet moyen (« average effect »), comme définis pp. 30–31.
- Price 1972 relève que des facteurs 2 manquent dans ces équations de l'édition de 1930 (p. 135, point iii). L'énoncé n'en est pas affecté.
- La mère situait le théorème p. 35, chapitre II : c'est confirmé.

**Ce que Fisher entend par « genetic variance » (pp. 30–34 imprimées, pp. 54–58 du PDF).**
- **Excès moyen** d'une substitution de gènes : la différence de moyenne du caractère entre deux moitiés de la population, l'une portant un gène, l'autre son alternative (p. 30).
- **Effet moyen** : « the difference produced, on the average, in the total stature of the population, for each such gene substitution » (p. 31).
- **Valeur génétique** : Fisher construit une valeur « attendue » X par somme d'incréments propres à chaque gène, ajustés pour que x − X ne garde aucune part liée aux gènes. Il montre que la variance de X vaut W = Σ(pqaα) (pp. 32–33). Puis : « this quantity we may distinguish as the *genetic* variance in the chosen measurement x » (p. 33).
- La variance est dite génétique parce que X « is determined solely by the genes present in the individual, and is built up of the average effects of these genes » (p. 33).
- Fisher la distingue de la variance génotypique, qui contient la dominance et les effets non additifs entre gènes : « The genetic variance as here defined is only a portion of the variance determined genotypically » (p. 34).
- C'est la **variance génétique additive** au sens moderne. Price 1972 le dit en toutes lettres (p. 129, voir § 2).

**La mesure de la valeur sélective : le paramètre malthusien (pp. 25–27 et 34 imprimées).**
- m est la racine réelle de l'équation ∫ e^{−mx} l_x b_x dx = 1, où l_x est la survie à l'âge x et b_x le taux de reproduction à cet âge (p. 26).
- Fisher le décrit ainsi : il « measures the relative rate of increase or decrease of a population when in the steady state ». Puis : « m may appropriately be termed the Malthusian parameter of population increase » (p. 26).
- Il en donne une lecture actuarielle : c'est le taux d'intérêt auquel la valeur présente des naissances attendues vaut un (p. 27).
- Dans la section « Natural Selection », Fisher applique ses définitions « to the special characteristic m which measures the relative rate of increase or decrease ». Puis : « Since m measures fitness to survive by the objective fact of representation in future generations, the quantity pqaα will represent the contribution of each factor to the genetic variance in fitness » (p. 34).
- La dynamique est en temps continu : d/dt log(p/q) = a, d'où dp = pqa dt (p. 34).
- Fisher ajoute que p : q doit être évalué en pondérant les individus par leur valeur reproductive (p. 35).

**Environnement (pp. 41–42 imprimées, pp. 65–66 du PDF).**
- Contre l'accroissement dû à la sélection naturelle, « at a rate equal to the genetic variance in fitness which that population maintains, is to be set off the very considerable item of the deterioration of its inorganic and organic environment » (p. 42).
- Fisher le dit déjà p. 37, point (3) : « Fitness may be increased or decreased by changes in the environment ».
- Le théorème porte donc sur une part du changement, pas sur le changement total. Price 1972 l'établit en détail.

**La recension (v1).** Elle n'apporte rien sur le théorème. Sa seule information utile est l'édition américaine, Oxford University Press, New York, 272 pages (recension, p. 167). Le scan d'archive.org la rend sans objet.

## 2. Lecture moderne : Price 1972 et Frank et Slatkin 1992

**Price 1972, « Fisher's “fundamental theorem” made clear », Ann. Hum. Genet. 36:129–140.** L'en-tête p. 129 du PDF porte « Ann. Hum. Genet., Lond. (1972), 36, 129 », et la dernière page est numérotée 140.
- **Énoncé et pages.** Price cite l'énoncé « (1930, p. 35; 1958, p. 37) » (p. 129). Notre lecture du scan le confirme.
- **Variance génétique additive.** Il écrit le théorème ∂_NS M/∂t = W, « where W is what Fisher termed the ‘genetic variance in fitness’ but which more commonly at present would be called the additive genetic variance in fitness » (p. 129).
- **Sélection naturelle seule.** « The main cause of misunderstanding about the theorem is that everyone has supposed that Fisher was talking about the total change dM/dt rather than just the fraction of this due to natural selection » (p. 130).
- **Partition.** dM = ∂_NS M + ∂_EC M (éq. 2.1, p. 129) :
  - la composante de la sélection naturelle est Σ b_t Q_T − Σ b_t Q_t : les coefficients de régression de la valeur sélective sur les fréquences alléliques sont tenus fixes, et seules les fréquences bougent (éq. 2.7, p. 130) ;
  - la composante de l'environnement est Σ b_T Q_T − Σ b_t Q_T (éq. 2.8, p. 130).
- **Ce qui compte comme « environnement ».** Fisher range la dominance et l'épistasie dans l'environnement ; il ne retient comme effet de la sélection naturelle que « the additive or linear effects of changes in gene frequencies » (p. 130). Citation de Fisher (1941), donnée p. 130 : « A change in the proportion of any pair of genes itself constitutes a change in the environment ».
- **Effet moyen.** L'effet moyen est le coefficient de régression partielle de la valeur sélective sur la fréquence individuelle de l'allèle (éq. 5.3, p. 137). La dérivation complète est donnée pp. 137–139.
- **Changement total.** L'égalité dM/dt = W, que d'autres auteurs ont démontrée, ne vaut que sous des conditions qui éliminent tout changement d'« environnement », c'est-à-dire b_T = b_t (p. 131).
- **Étalon mouvant.** La sélection augmente la valeur sélective « to live under the conditions that existed an instant earlier » (p. 131).
- **Généralité.** Le théorème est très général : il dépend seulement du lissage par une grande population et de l'absence de sélection méiotique et gamétique (p. 139).
- **Cadre.** Le théorème est dérivé « in the full form that Fisher intended (continuous time model, with weighting by reproductive value) » (résumé, p. 140).

**Frank et Slatkin 1992, TREE 7:92–95.**
- **Lecture courante.** Elle n'est exacte que sous des conditions restrictives : « no epistasis, no linkage disequilibrium and no frequency dependence » (p. 92). Elle diffère de ce que Fisher voulait dire, d'après Price et Ewens (p. 92).
- **Partition (éq. 1, p. 93, relue sur image).** ΔW̄ = (W̄′|E − W̄|E) + (W̄′|E′ − W̄′|E), « where primes denote one time step or instant into the future ».
  - Le premier terme est « the change in fitness caused by natural selection because there is a constant frame of reference, the initial environmental state E ».
  - Ils ajoutent : « The Fundamental Theorem states that the change in fitness caused by natural selection is equal to the additive variance in fitness » (p. 93).
- **Glossaire (encadré 1, p. 93).**
  - Effet moyen d'une substitution : le changement moyen du phénotype mesuré « in the context of the current population ».
  - Variance génétique additive, pour un locus : le carré de l'effet moyen multiplié par la variance de la fréquence génique.
- **Allèles et environnement (p. 95).** Pour Fisher, tout changement de valeur sélective dû à un changement d'effet moyen est un effet d'environnement ; la sélection agit « according to the additive variance in fitness associated with allele frequency ».
- Frank et Slatkin écrivent la partition aussi pour « one time step », mais ils **ne donnent pas** la normalisation discrète (division par w̄). Celle-ci vient de l'équation de Price 1970 (p. 520).

## 3. Nouveau jugement de nos deux formules

**Ce que notre identité dit, dans les termes de Fisher.**
- **Valeur sélective w = β.** C'est une probabilité de survie à un tour de filtrage, en temps discret. Ce n'est pas un paramètre malthusien.
- **Transmission.** Les types se transmettent à l'identique, comme des clones : un survivant garde son β. Toute la variance de β entre types est « additive » : la régression de w sur les indicatrices de type est exacte. Donc variance additive = variance totale = Var_μ(β).
- **Environnement.** Les strates, les lois et les taux de détection sont fixes. Le résumé du manuscrit le pose : « fixed strata, priors and detection rates ». Le terme d'environnement de Price (éq. 2.8, p. 130) et de Frank et Slatkin (éq. 1, second terme, p. 93) est donc nul. Le changement dû à la sélection est tout le changement.
- **Forme discrète.** E_{π_A}[β|Π_tr] − E_μ[β] = Var_μ(β)/E_μ[β]. De façon équivalente, Δw̄/w̄ = Var(w/w̄) : la variation relative de la valeur sélective moyenne égale la variance de la valeur sélective relative. Les deux sont vérifiées en arithmétique exacte (`verif_fisher_analogue_v2.out` : 37/150 et 37/50).

**Classement : un analogue, ni le théorème, ni un cas particulier exact de son énoncé.**
- L'énoncé de Fisher (p. 35) porte sur trois choses :
  - un **taux** instantané (dt), en temps continu ;
  - une valeur sélective mesurée par le **paramètre malthusien** m (pp. 26, 34) ;
  - la **variance génétique additive**, sans division par la moyenne (pp. 33–35 ; Price 1972, p. 129).
- Notre identité porte sur un **pas discret**, une **probabilité de survie** et une variance **divisée par la moyenne**. Aucun choix de paramètres ne fait de notre identité une instance littérale de l'énoncé de la p. 35.
- C'est l'analogue en temps discret, et dans un cas dégénéré : transmission à l'identique, environnement fixe, partiel égal au total. C'est la lecture de Price 1972 (pp. 129–131) et de Frank et Slatkin 1992 (p. 93).
- **Remarque, de mon cru, non proposée pour le texte.** Il existe un cas particulier exact, en temps continu, mais ce n'est pas notre identité. Prenons le rejet répété comme une famille continue π_s ∝ β^s μ, où s est le nombre de tours rendu réel, et m = log β comme paramètre malthusien par tour. Alors d/ds E_s[log β] = Var_s(log β). C'est la forme clonale exacte du théorème.
  - Elle est vérifiée numériquement, avec un écart maximal de 1,7·10⁻¹⁰ sur 200 tirages (`verif_fisher_analogue_v2.out`).
  - Elle porte sur log β et sur un taux instantané. Sur un pas entier, elle n'égale pas la variance : 0,7150 contre 0,7592 sur l'exemple du manuscrit.
  - Elle ne justifie donc pas les formules actuelles. Je ne recommande pas de l'ajouter : ce serait revendiquer davantage.

**« the variance form being Fisher's fundamental theorem » (contribution 2).**
- C'est **inexact**. La variance de notre forme n'est pas le théorème de Fisher : c'en est un analogue discret.
- Marque [F] de la v1 : **levée**. Le jugement « analogue, pas le théorème » est confirmé, sur pièces (Fisher p. 35 ; Price 1972 pp. 129–130, 140 ; Frank et Slatkin p. 93).

**« i.e. Fisher's (1930) fundamental theorem in this setting » (billet, ligne 55).**
- C'est **inexact**. « in this setting » ne suffit pas, car le cadre change trois des éléments du théorème : le temps continu, le paramètre malthusien, la variance sans division par la moyenne.
- « i.e. » affirme une identité qui n'existe pas.
- Marque [F] **levée**, jugement confirmé.

**Ligne 17 du billet** (« the variance form being Fisher's fundamental theorem ») : même jugement, inexact.

**Ligne 119 du billet** (« The two identities are classical (Price 1970; Robertson 1966; Fisher 1930) »).
- C'est juste pour Price et Robertson.
- Pour Fisher, c'est trompeur : la seconde identité, la covariance de la variante R2, ne doit rien à Fisher, et la première n'en est qu'un analogue.

## 4. Phrases finales proposées (anglais)

Elles ne revendiquent rien de plus. La citation de Price 1972 est facultative ; si on la garde, il faut ajouter à la bibliographie : `\bibitem{price1972} G.~R.~Price, \emph{Fisher's ``Fundamental Theorem'' Made Clear}, Annals of Human Genetics, 36:129--140, 1972.` J'ai vérifié la revue, le volume et les pages sur le PDF.

**Résumé** : inchangé. « a special case of the Price–Robertson covariance identity » est juste, et le résumé ne nomme pas Fisher.

**Contribution 2** (LaTeX) :
> under Operator~A we restate the variance identity for conditional enrichment: it is the selection term of Price's covariance equation~\cite[Eqs.~(1), (4), p.~520]{price1970}, with survival as both fitness and trait and no transmission term, equivalently Robertson's selection differential written as a covariance with relative survival~\cite[pp.~97, 99]{robertson1966}. It is a one-step, discrete-time analogue of Fisher's fundamental theorem~\cite[p.~35]{fisher1930}, not the theorem itself, which concerns the rate of increase of Malthusian fitness due to natural selection and the additive genetic variance in fitness~\cite[pp.~129--130]{price1972}.

Version courte, sans Price 1972 :
> … with survival as both fitness and trait and no transmission term~\cite[p.~520]{price1970}; see also~\cite[pp.~97, 99]{robertson1966}. It is a one-step, discrete-time analogue of Fisher's fundamental theorem~\cite[p.~35]{fisher1930}, not the theorem itself.

**Billet, ligne 17** (entre parenthèses) :
> (a special case of the Price–Robertson covariance identity; it is a one-step, discrete-time analogue of Fisher's fundamental theorem, not the theorem itself)

**Billet, ligne 55** :
> This is the selection term of Price's (1970, p. 520) covariance equation, with survival as both the fitness and the trait and no transmission term; Robertson (1966, pp. 97, 99) gives the same covariance form for selection by culling. It is a one-step, discrete-time analogue of Fisher's (1930, p. 35) fundamental theorem, not the theorem itself: Fisher's theorem is a continuous-time statement that the rate of increase in (Malthusian) fitness due to natural selection equals the additive genetic variance in fitness (Price 1972, pp. 129–130).

**Billet, ligne 119** :
> The two identities are classical (Price 1970; Robertson 1966); the variance form is a discrete-time analogue of Fisher's (1930) fundamental theorem.

**Bibliographie** :
- `fisher1930` : exact, page de titre vérifiée (p. 13 du PDF).
- `price1970` et `robertson1966` : exacts, vérifiés en v1.

## 5. Rappel de la v1 (Price 1970, Robertson 1966), inchangé

**Price 1970 (p. 520).**
- Notre identité est l'équation (4), avec z = β, q = β et Δq_i = 0. Elle se réduit alors à l'équation (1), ΔQ = Cov(z,q)/z̄.
- Price prévoit l'usage hors de la génétique, avec l'exemple des étudiants qui achèvent un cours (p. 520).
- Vérification en arithmétique exacte : 37/150 par quatre voies, et 2 000 tirages (`verif_price_robertson_v1.out`).
- Price ne cite pas Robertson (p. 521, point « Fifth »).

**Robertson 1966.**
- Forme phénotypique : « the covariance of yield with survival is q̄D » (p. 97).
- Forme génétique, le « secondary theorem » : ΔG_X = V_gX b_cX.g et ΔG = cov(cX)_g, où c est la survie relative (p. 99).
- Robertson annonce un développement « ailleurs » (p. 106).

## 6. Limites de ma lecture

- **Lecture du scan de Fisher.** Le scan d'archive.org a une couche de texte bruitée. L'énoncé (p. 35) et les équations des pp. 33–35 ont été relus sur image, mais les définitions des pp. 26–34 surtout sur la couche texte.
  - La distinction typographique entre a (excès moyen) et α (effet moyen) est fine à l'image. Je l'ai attribuée d'après les définitions des pp. 30–31 et d'après Price 1972 (p. 134).
- **Ce que je n'ai pas lu.**
  - L'édition de 1958, ni Fisher 1941 : je ne les cite qu'à travers Price 1972 et Frank et Slatkin.
  - Ewens 1989 et Robertson 1968.
  - Les autres sections du chapitre II que celles citées, ni les pp. 43–50.
- **Frank et Slatkin** est un scan reconnu par lecture optique. L'équation (1) et l'encadré 1 ont été relus sur image (p. 93). Les autres citations viennent de la couche texte.
- **Le classement « analogue »** est mon jugement, appuyé sur les pages citées. Price 1972 et Frank et Slatkin ne traitent pas notre cas : un pas discret, des clones, une survie comme valeur sélective.
  - La normalisation par w̄ vient de Price 1970, pas de ces deux textes.
  - Aucun des deux n'écrit « discrete-time analogue » : l'expression est de moi.
- **La remarque sur la famille continue π_s ∝ β^s μ** est de mon cru, vérifiée numériquement seulement. Elle n'est pas proposée pour le texte.
- **Usage de l'expression « Price–Robertson identity »** : toujours non vérifié dans la littérature.
- **Les calculs** vérifient l'algèbre, pas la modélisation de l'opérateur A.

Fichiers, dans `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/identite-covariance/` :
- la v1, intacte ;
- les extraits `*.txt` ;
- les images `img/fisher-titre-013.png`, `img/fisher-058.png`, `img/fisher-059.png`, `img/fisher-p35-haut-059.png`, `img/fisher-p33-haut-057.png`, `img/frank-2.png` ;
- les scripts `verif_price_robertson_v1.py` et `verif_fisher_analogue_v2.py`, avec leurs sorties `.out`.
