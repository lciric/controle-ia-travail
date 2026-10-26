# Proposition A — Tour III.1

**Pièce jointe :** le bloc FAITS est vide par décision de l'arbitre ; tout ce qui suit s'appuie sur la seule QUESTION. Aucun élément ci-dessous n'a donc le statut VÉRIFIÉ : ce que la question affirme sur le programme est RAPPORTÉ ; ce que j'en déduis est HYPOTHÈSE ou calcul explicite.

Pièces absentes que je signale sans les inventer : l'identité des modèles de langue appelés par les organismes ; la dérivation du coût (270/450 USD) ; l'existence et le contenu des pilotes 1 à 3 ; le texte des deux expériences principales ; le mode de rendu des scores à celui qui lance les courses.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Pourquoi ce n'est pas établi |
|---|---|---|---|
| S1 | Les scores du pilote 4 contiennent une information utile sur le **signe** et la **taille** de l'effet « réécriture de soi ». | HYPOTHÈSE | Une course par objet, σ(différence) ≈ 0,10–0,125 (RAPPORTÉ, raisonnement explicite). Un signe tiré d'une seule différence a, si l'effet vrai est ≤ 0,1, une probabilité d'être faux de l'ordre de 20–30 % (calcul : P(Z < −0,1/0,11) ≈ 0,18 ; illustratif). Le pilote 4 apporte donc au plus ~1 bit par famille, avant même la variance entre graines. |
| S2 | Lire les scores est la seule voie de contamination. | HYPOTHÈSE | Les faits mécaniques (durées, plantages, longueur des réécritures, coût en jetons) sont corrélés au comportement de l'organisme ; la lignée B, qui écrit les textes des pilotes *et* de la confrontation, les voit déjà. |
| S3 | Le contraste v6.2.1 vs v5.3 isole « la réécriture de la règle de récompense ». | HYPOTHÈSE | v6.2.1 est « la v6.2 de Gemini, corrigée par la lignée B » ; v5.3 est « plus simple ». La différence est multi-facteurs (version, corrections, taille du code). Aucune ablation (v6.2.1 avec réécriture désactivée) n'est mentionnée. |
| S4 | Trois graines par objet peuvent trancher à un seuil usuel. | HYPOTHÈSE (réfutable par calcul, §3) | Avec 3 contre 3 graines, un test de permutation sur les moyennes par graine n'a que 20 arrangements : p minimal = 1/20 = 0,05 unilatéral, 0,10 bilatéral. |
| S5 | La part `test` donne une estimation non biaisée. | HYPOTHÈSE | Les organismes reçoivent leur score sur `test` à chaque génération et se réécrivent : `test` est réutilisée adaptativement, ce qui gonfle les scores de génération en génération (problème du jeu de validation réutilisé). Seule `test_final` est propre. |
| S6 | Un « agent neuf » est un conteneur étanche. | HYPOTHÈSE | Ce qu'il écrit (signe et taille par famille) est lu ensuite par ceux qui assemblent le texte de (b) — dont la lignée B. Le texte scellé est lui-même un canal. |
| S7 | Celui qui lance les courses ne voit pas les scores. | NON ÉTABLI | « La lignée A lance tout ce qui dépense » et écrit l'étape 1. Si le score est écrit dans un journal lisible par le lanceur, la contamination de l'étape 1 passe par A, quelle que soit l'option. |
| S8 | Les familles de tâches des pilotes mesurent la même chose que celles des expériences principales. | HYPOTHÈSE | Banques distinctes ; aucune correspondance rapportée. |
| S9 | Coût : 270 USD attendus, 450 au pire. | RAPPORTÉ (dérivation absente) | Je dérive 270/6 = 45 USD par course (illustratif, dépend de la dérivation absente). |
| S10 | Le bruit se réduit à l'erreur binomiale. | RAPPORTÉ (raisonnement explicite) | Le calcul suppose l'indépendance des tâches et ignore la variance entre graines, ce que la question reconnaît. Aucun chiffre de variance entre graines n'existe (une course par objet). |

---

## 1. Risque de contamination par option

Je raisonne en « bits transmis × lecteurs × sensibilité des choix ».

**Option (1), garder la règle.** Information numérique : aucune. Résidu : les faits mécaniques (S2) et, selon S7, le lanceur. Ce que la règle ne protège pas : le choix *du délai* lui-même. Attendre « plusieurs jours » n'est protecteur que si, pendant ce délai, aucun autre canal ne fuit. Coût : (b) attend l'étape 1, alors que (b) ne concerne pas l'étape 1.

**Option (2).** L'agent neuf lit les scores (quatre nombres par objet, deux familles × deux parts, plus quatre générations). Il écrit signe et taille par famille dans (b). Le texte de (b) encode donc environ 2 familles × (1 bit de signe + ~2 bits de classe de taille) ≈ 6 bits (illustratif). Tout lecteur de (b) — la lignée B, qui en écrit le texte — les reçoit. Ce que cela peut orienter dans la confrontation, même sans intention : la famille servie en priorité, le seuil (ancré sur la taille vue), la règle de lecture (un seuil « atteignable » ressemble à ce qu'on a vu). Force : forte sur le seuil, faible sur la banque. La réserve « déclarée » protège contre la citation explicite ; elle ne protège pas contre l'ancrage numérique, qui n'est pas intentionnel et que le déclarant ne peut pas attester de lui-même.

**Option (2').** Réduit le canal à : (i) l'agent neuf, (ii) l'assemblage mécanique du texte de (b) (concaténation par hachage, sans lecture), (iii) l'ouverture après les courses de (b). Reste : S7 (lanceur) ; et le fait que la lignée B, qui écrit le reste de (b) (métrique, plan d'analyse), doit le faire *sans savoir* ce qu'affirment les hypothèses — faisable si elle écrit d'abord, l'agent neuf ensuite, et si le scellé horodate cet ordre. Le gain de (2') sur (2) est mécaniquement vérifiable (hachages successifs) ; c'est son avantage.

**Option (3).** Information de score : zéro. Coût : hypothèses non calibrées. Mais d'après S1, la calibration apportée par le pilote 4 vaut ≈ 1 bit par famille au mieux ; la perte est faible. Résidu : les faits mécaniques, et le risque qu'une hypothèse « sans donnée » soit écrite de façon vague.

**Comment borner la contamination (toutes options) :** l'expérience E1 ci-dessous mesure directement si un rédacteur suit le signe des scores qu'on lui montre, y compris quand ce signe est faux. Mécaniquement : hachage et horodatage des textes principaux *avant* la fin du pilote 4 ; toute modification ultérieure est un diff lisible, pas une déclaration.

---

## 2. Autres dessins

**D1 — Menu d'hypothèses scellé, sélection mécanique.** Avant toute course, un agent n'ayant lu que les textes de conception écrit *trois* jeux d'hypothèses complets pour (b) : effet positif ≥ δ, effet nul (|Δ| < δ), effet négatif ≤ −δ, chacun avec son plan d'analyse. Un script, jamais un humain, choisit le jeu à partir des scores du pilote 4 selon une règle scellée (par exemple le signe de la différence sur `test_final` famille 1). L'index choisi n'est révélé qu'après les courses de (b). Fuite : log₂3 ≈ 1,6 bit, après coup. Exige : pipeline automatique de scoring, stockage scellé, règle de sélection écrite avant le pilote 4. Avantage : conforme au préenregistrement. Inconvénient : les trois jeux doivent être équitables, sinon le menu lui-même biaise.

**D2 — Hypothèses tirées de `test` seulement, confirmation sur `test_final`.** Compatible avec la structure actuelle (`test_final` jamais rendue). Mais à cause de S5, `test` est optimiste et ne protège que (b), pas les expériences principales : il ne résout pas la question posée. À garder comme diagnostic de fuite (E4).

**D3 — Pilote 4 pour la seule variance.** Un script ne sort que des statistiques sans signe : dispersion entre générations, accord inter-tâches, |Δ| sans orientation, étiquettes d'objets permutées. Limite majeure : une course par objet, donc *aucune* variance entre graines ne peut en sortir — la quantité justement manquante dans S10. Ce dessin répond à une question que le pilote 4 ne peut pas poser.

**D4 — Plan séquentiel.** Deux graines par objet d'abord ; deux de plus si |Δ| tombe dans une zone grise scellée. Exige une dépense d'α scellée et, surtout, une lecture intermédiaire des scores par quelqu'un — c'est une fuite programmée vers le lanceur (S7). Avec si peu de graines, la zone grise couvrira presque tout l'espace : gain de coût faible, complexité forte.

**D5 — Hypothèse d'équivalence (sans signe).** H₀ : |Δ| ≥ δ ; on cherche à montrer que la complexité apporte *moins* que δ. C'est la forme la plus fidèle à « valeur au-delà du bruit ». Problème : avec 3 graines et σ ≈ 0,11 par course, l'intervalle à 90 % sur Δ a une demi-largeur ≈ 1,64 × 0,11 × √(2/3) ≈ 0,15 (illustratif, sans variance entre graines) ; conclure l'équivalence exige δ ≥ 0,3, ce qui est la taille d'un effet énorme. L'équivalence n'est pas concluante à ce budget ; elle reste la bonne *forme* si le budget monte.

**D6 — Supprimer le pilote 4, courir (b) en aveugle d'étiquette.** Les 6 (ou 8) courses sont lancées maintenant ; le script masque les objets (X/Y) ; les hypothèses sont écrites sur les textes de conception ; le démasquage suit le gel de l'analyse. Le pilote 4 n'existe plus, donc ne contamine rien ; les faits mécaniques (coûts, durées) sortent des mêmes courses. Avec 8 courses (4 par objet, 360 USD illustratif, sous le pire cas rapporté), le p minimal de permutation passe à 1/70 ≈ 0,014 unilatéral. Ce que D6 perd : la phase « produire des hypothèses testables » demandée par Lazar ; je soutiens que cette phase, avec une course par objet, produit surtout du bruit (S1).

---

## (b) Expériences décisives en duel

### E1 — Le canal « hypothèses écrites » transmet-il le signe ?

- **H_A :** un rédacteur qui voit des scores de pilote écrit des hypothèses dont le signe suit celui des scores montrés, même quand ce signe est inversé artificiellement.
- **H_B :** le signe des hypothèses écrites est indépendant des scores montrés (il dépend des textes de conception seulement).
- **Dessin :** 3 bras × k rédacteurs (agents neufs, modèles ouverts, sessions jetables) écrivent la section hypothèses de (b). Bras 0 : sans scores. Bras + : scores réels. Bras − : mêmes scores avec les objets permutés. Les rédacteurs ignorent l'existence des autres bras.
- **Métrique :** fraction de rédacteurs dont le signe écrit concorde avec le signe montré, dans les bras + et − ; **contrôle négatif :** bras 0 (distribution de base des signes).
- **Seuil scellé :** concordance ≥ 0,8 dans les deux bras ⇒ H_B falsifiée (le canal transmet) ; concordance dans l'intervalle de base du bras 0 ± 0,2 ⇒ H_A falsifiée.
- **Ce que chaque issue falsifie :** si H_A tient, les options (2) et (2') sans isolement mécanique sont disqualifiées ; si H_B tient, la peur de contamination par le texte des hypothèses est sans objet et (2) devient acceptable.
- **Coût :** k = 6 par bras, ~50 k jetons par rédaction, < 20 USD (illustratif).

### E2 — La variance entre graines dépasse-t-elle le bruit binomial ?

- **H_A :** la variance entre graines de l'exactitude d'un objet fixe est ≤ 1,5 × la variance binomiale (0,75 × 0,25/36 ≈ 0,0052).
- **H_B :** elle est ≥ 3 × la variance binomiale.
- **Dessin :** s'obtient *dans* (b) sans course supplémentaire (3–4 graines par objet) ; mais il faut sceller à l'avance que cette lecture conditionne l'interprétation de E3, pas le seuil de E3.
- **Contrôle négatif :** re-noter deux fois la même sortie de course (déterminisme du noyau de scoring) ; une variance non nulle ici est un défaut d'instrument, pas une variance de graine.
- **Issue :** zone grise entre 1,5 et 3 → aucune des deux n'est falsifiée, et (b) n'est pas assez grand pour les séparer : à dire d'avance.

### E3 — Le duel principal de (b)

- **H_A :** l'organisme à réécriture de récompense atteint, sur `test_final`, génération 4, famille 1 (36 tâches), une exactitude moyenne par graine supérieure d'au moins δ = 0,20 à celle du contrôle.
- **H_B :** la différence est ≤ 0.
- Zone entre 0 et 0,20 : **non tranchée** (déclaré dans le texte scellé).
- **Unité :** la graine (une course). **Métrique :** Δ = moyenne des exactitudes par graine (v6.2.1) − moyenne (contrôle). **Test :** permutation exacte sur les étiquettes de course, unilatéral.
- **Règle de décision scellée (3 graines) :** H_B falsifiée seulement si Δ ≥ 0,20 **et** les 3 courses v6.2.1 dépassent les 3 courses contrôle (p = 0,05, seul résultat atteignable) ; H_A falsifiée si Δ ≤ 0 ou si une course contrôle dépasse la meilleure course v6.2.1.
- **Contrôle négatif indispensable (et absent du plan rapporté) :** le contrôle n'est pas v5.3 mais **v6.2.1 à réécriture désactivée** (même code, règle de récompense gelée). Sans cela, E3 tranche « v6.2.1 vs v5.3 », pas « réécriture vs pas de réécriture » (S3). Contrôle nul additionnel : v5.3 contre v5.3 (graines séparées), pour vérifier que la procédure donne Δ ≈ 0 quand il n'y a rien à trouver.
- **Ce que falsifie chaque issue :** H_A battue → la complexité ne vaut pas 0,20 à ce budget ; H_B battue → un effet ≥ 0,20 existe sur cette banque, ce qui n'établit rien sur les banques principales (S8).

### E4 — La réécriture exploite-t-elle la part `test` ?

- **H_A :** l'écart (score `test` − score `test_final`) croît entre génération 1 et génération 4 d'au moins 0,10 pour l'objet à réécriture, pas pour le contrôle.
- **H_B :** l'écart ne croît pas (différence de croissance ≤ 0).
- **Métrique :** (test₄ − test_final₄) − (test₁ − test_final₁), par graine. **Contrôle négatif :** l'objet sans réécriture.
- **Coût :** nul (toutes ces parts existent déjà dans (b)). **Issue :** si H_A tient, une partie de tout gain « sur test » est de l'ajustement au signal de récompense, et seule `test_final` compte ; si H_B tient, `test` est utilisable comme source d'hypothèses (D2) sans trop d'optimisme.

---

## 3. Écrire les hypothèses de (b) pour qu'elles tranchent

- **Unité d'analyse :** la graine. Les tâches sont partagées entre objets et entre graines ; une analyse « par tâche » (sign test apparié sur 36 tâches) a plus de puissance apparente mais traite les réponses d'une même course comme indépendantes, ce qu'elles ne sont pas (un même code répond à toutes). La garder comme analyse secondaire avec bootstrap par grappe (graine), jamais comme analyse primaire.
- **Effet minimal :** δ = 0,20 sur la famille à 36 tâches, dérivé de l'erreur type rapportée (2 × 0,10) ; 0,25 sur 24 tâches. En dessous, (b) ne tranche pas et doit le dire.
- **Nombre de graines :** 3 par objet autorise une seule issue favorable à H_A (p = 0,05 unilatéral) et rien au bilatéral ; 4 par objet (8 courses) donne p minimal ≈ 0,014 ; 5 par objet, 1/252 ≈ 0,004. À 45 USD par course (illustratif), 8 courses = 360 USD, dans le pire cas rapporté. **Réponse à « 3 suffisent-elles ? » : seulement pour un effet qui sépare totalement les deux groupes de courses, et seulement unilatéral.**
- **Familles et parts :** une seule analyse primaire (famille 36 tâches, `test_final`, génération 4). Famille 24 tâches : secondaire, descriptive. Part `test` : diagnostic (E4), jamais confirmatoire. Génération 1 : ligne de base pour E4.
- **Multiplicité :** avec deux contrastes primaires, Bonferroni donne α = 0,025, inatteignable à 3 graines (p minimal 0,05) ; c'est une seconde raison de n'avoir qu'un contraste primaire.
- **Ce que (b) ne pourra pas trancher :** la cause (sans ablation, S3) ; tout effet < 0,20 ; la variance entre graines au-delà d'une zone grise (E2) ; le transfert aux banques principales (S8) ; la part du code écrit par Gemini dans le résultat ; l'interaction entre familles.

---

## (c) Mesure minimale pour chaque instrument nommé

| Instrument | Cas honnêtes appariés | Taux à mesurer | Vérification mécanique à battre |
|---|---|---|---|
| **Agent neuf contre-lecteur** | n textes scellés honnêtes + n textes dans lesquels on a glissé une hypothèse dérivée de scores (nombre, signe, formulation ancrée) ; n = 10 + 10 (illustratif) | détection = fraction des textes contaminés signalés ; fausses alertes = fraction des honnêtes signalés | diff contre la version précédente + recherche de nombres/expressions de score + horodatage par hachage. Si le contre-lecteur ne dépasse pas le diff en détection à fausses alertes égales, il n'apporte rien. |
| **Réserve déclarée** | une réserve écrite n'a pas de « cas appariés » : elle ne détecte rien, elle atteste | aucun taux mesurable | dominée par : hachage du texte **avant** la disponibilité des scores. Si le hachage existe, la déclaration est redondante ; s'il n'existe pas, elle est invérifiable. |
| **Enveloppe scellée (préenregistrement)** | détection d'altération : 100 % par construction (hachage) | ce qu'elle ne détecte pas : la fuite par conversation, l'ancrage du rédacteur | horodatage par tiers ; contre-vérification : E1 mesure ce que le scellé ne couvre pas |
| **Audit de propreté** (résultat suspect) | résultats honnêtes vs résultats « trop propres » injectés (par exemple 3 courses strictement ordonnées par construction) | détection / fausses alertes du déclencheur | règle mécanique : déclenchement si p de permutation < 0,02 ou si la variance entre graines < 0,3 × binomiale (illustratif) ; l'audit humain doit battre cette règle |
| **Pilote 4 comme générateur d'hypothèses** | son signe par famille vs le signe obtenu dans (b) | « détection » = concordance de signe ; « fausse alerte » = signe inversé | base à battre : pile ou face (0,5) et l'hypothèse a priori « Δ = 0 ». Mesurable *après* (b), gratuitement : à inscrire dans le texte scellé. |
| **Sondes de l'étape 1** | la question les nomme sans détail ; je ne décris pas un instrument que je n'ai pas vu | — | pièce absente |

---

## 4. Ce qui est connu (références que je peux attribuer)

- Kerr, N. L. (1998), « HARKing: Hypothesizing After the Results are Known », *Personality and Social Psychology Review* — nommer le problème que l'option (2) crée à petite échelle.
- Simmons, Nelson & Simonsohn (2011), « False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant », *Psychological Science* — degrés de liberté du chercheur.
- Gelman & Loken (2014), « The Statistical Crisis in Science », *American Scientist* (et manuscrit 2013, « The garden of forking paths ») — les chemins multiples existent sans intention, ce qui est exactement le cas d'une réserve « déclarée ».
- Gelman & Carlin (2014), « Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors », *Perspectives on Psychological Science* — pertinent pour S1 : à faible puissance, le signe observé est peu fiable et la taille surestimée.
- Wagenmakers, Wetzels, Borsboom, van der Maas & Kievit (2012), « An Agenda for Purely Confirmatory Research », *Perspectives on Psychological Science* — séparation exploratoire/confirmatoire.
- Nosek, Ebersole, DeHaven & Mellor (2018), « The Preregistration Revolution », *PNAS*.
- MacCoun & Perlmutter (2015), « Blind analysis: Hide results to seek the truth », *Nature* ; Klein & Roodman (2005), « Blind Analysis in Nuclear and Particle Physics », *Annual Review of Nuclear and Particle Science* — base de D6.
- Dwork, Feldman, Hardt, Pitassi, Reingold & Roth (2015), « The reusable holdout: Preserving validity in adaptive data analysis », *Science* — base de S5/E4 : une part réutilisée avec retour d'information perd sa validité.
- Recht, Roelofs, Schmidt & Shankar (2019), « Do ImageNet Classifiers Generalize to ImageNet? », *ICML* — biais de sélection sur jeu de test réutilisé.
- Henderson, Islam, Bachman, Pineau, Precup & Meger (2018), « Deep Reinforcement Learning That Matters », *AAAI* ; Agarwal, Schwarzer, Castro, Courville & Bellemare (2021), « Deep Reinforcement Learning at the Edge of the Statistical Precipice », *NeurIPS* — variance entre graines, petit nombre de courses, intervalles bootstrap.
- Bouthillier et al. (2021), « Accounting for Variance in Machine Learning Benchmarks », *MLSys* — sources de variance, dont les graines ; référence à vérifier pour la liste exacte des auteurs.
- Lakens (2017), « Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses », *Social Psychological and Personality Science* — base de D5.
- Button et al. (2013), « Power failure: why small sample size undermines the reliability of neuroscience », *Nature Reviews Neuroscience*.
- Sur l'aveuglement en psychologie expérimentale (Dutilh et al., « Flexible yet fair: blinding analyses in experimental psychology », *Synthese*) : référence à vérifier (année et liste d'auteurs incertaines).

Aucune référence ci-dessus ne porte sur le cas précis « hypothèses de pilote écrites par un agent indépendant pour une expérience voisine » ; ce cas est une composition des précédentes, pas un résultat publié que je connaisse.

---

## 5. Comment départager

**Critères :**
1. **Valeur informationnelle du pilote 4 pour les hypothèses de (b)** — bornée par S1 à ~1 bit par famille ; mesurable après coup (ligne « pilote 4 » du tableau (c)).
2. **Exposition** — bits transmis × nombre de lecteurs × sensibilité des choix principaux ; la sensibilité se mesure par E1.
3. **Vérifiabilité mécanique** — une option est préférable si sa garantie est un hachage horodaté et non une déclaration : (2') et D1/D6 sont vérifiables ; (2) l'est à moitié ; (1) et (3) le sont trivialement.
4. **Coût de délai** — (1) seul paie des jours ; les autres non.
5. **Ce qui est tranchable au budget** — à 6 courses, aucune option ne change le fait que seul un effet ≥ 0,20 et une séparation totale des courses tranche.

**Ordre que ces critères suggèrent (sans en faire « la » réponse) :** si E1 montre que le canal texte transmet le signe, (3) ou D6 ; si E1 montre qu'il ne transmet rien, (2') devient acceptable ; (2) n'est jamais meilleure que (2') ; (1) n'achète qu'un délai. D6 domine (a)+(b) si Lazar accepte de perdre la phase descriptive — ce qui dépend de ce qu'il attend d'elle au-delà des faits mécaniques.

**Ce qu'il faudrait savoir de plus :**
- S7 : le lanceur (lignée A) voit-il les scores ? Si oui, toutes les options fuient vers l'étape 1 et le débat sur (b) est secondaire.
- Existe-t-il des pilotes antérieurs avec plusieurs graines d'un même objet ? Un seul chiffre de variance entre graines changerait δ et le nombre de courses.
- La dérivation de 45 USD par course : si une course coûte moins, 8 courses avec ablation deviennent possibles dans le budget rapporté.
- Si la lignée B peut livrer une v6.2.1 à réécriture désactivée : sans elle, (b) ne répond pas à la question de fond quelle que soit l'option retenue.

FIN-DE-CELLULE