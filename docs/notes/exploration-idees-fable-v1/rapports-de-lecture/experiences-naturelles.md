# Expériences et données datées : ce qui fait naître le lien ou la découverte

Dossier des sources : `/tmp/claude-0/-home-user-controle-ia-travail/7225ef84-cf06-5367-97a0-6c2a4e600e2b/scratchpad/sources/experiences-naturelles/` ; empreintes complètes dans `sha256sums.txt` du même dossier (16 premiers signes ci-dessous). « p. N » = page du fichier PDF ; numéro imprimé entre crochets s'il est lu. Plusieurs fichiers sont des versions de travail, pas la version publiée : c'est signalé à chaque fois, et les chiffres peuvent différer de la version publiée.

## Cas 1 — domaines disjoints, découverte par un lien

### 1. Swanson 1986 et la découverte fondée sur la littérature
- **Swanson 1986**, Perspect. Biol. Med. 30(1):7-18 : PDF **non obtenu** (Project MUSE, payant ; la notice PubMed 3797213 n'a pas de résumé). Méthode décrite **de mémoire, à vérifier sur PDF** : deux littératures qui ne se citent pas (huile de poisson ; syndrome de Raynaud) reliées par des termes intermédiaires (viscosité du sang, agrégation des plaquettes, réactivité vasculaire).
- **Confirmation ultérieure** : DiGiacomo, Kremer, Shah 1989, Am. J. Med. 86:158-164 (résumé PubMed lu par eutils ; **résumé seulement**). Essai à double insu, 32 patients tirés au sort entre huile de poisson et huile d'olive. « Five of 11 patients (45.5 percent) with primary Raynaud's phenomenon ingesting fish oil … could not be induced … compared with one of nine patients (11 percent) … (p = 0.05) » ; effet « in patients with primary, but not secondary, Raynaud's ». Petit essai, effet limité au Raynaud primaire.
- **Revue récente** : Kastrin, Cestnik, Lavrač 2025, « Recent Advances and Future Directions in Literature-Based Discovery », arXiv:2506.12385 (`lbd_review2025.pdf`, d859c530a715a66d). Lu sur PDF, p. 2 : présente le modèle A-B-C et dit l'hypothèse « later confirmed by clinical research [8] » (réf. 8 = DiGiacomo 1989). **Attention** : la revue écrit p. 2 que le Raynaud est associé à « reduced blood viscosity » et l'huile de poisson à « high blood viscosity », ce qui inverse la chaîne de Swanson (de mémoire : le Raynaud va avec une viscosité élevée, l'huile de poisson la réduit) ; c'est à vérifier sur Swanson 1986 avant toute citation. P. 9 : jusqu'à 27 % des erreurs viennent de la normalisation des entités (« accounting for up to 27% of errors in some evaluations [15] ») et il n'existe pas de ressource comparable hors des sciences de la vie. Cette revue ne donne **aucun chiffre d'évaluation à date gelée**.
- **Henry et McInnes 2017** (J. Biomed. Inform. 74:20-32) et **Sebastian et al. 2017** : PDF **non obtenus** (Elsevier et Cambridge payants ; la copie PeerJ de Thilakaratne 2019 et Dyport 2024 sur BMC sont bloquées par une vérification anti-robot, que je n'ai pas contournée). La question « que valent ces méthodes à date gelée » reste **sans réponse vérifiée** pour la littérature biomédicale. Seules les deux épreuves suivantes sont lues.

### 2. Épreuves à date gelée hors biomédecine
- **Tshitoyan et al. 2019**, Nature 571:95-98 ; copie OSTI (`tshitoyan2019_osti.pdf`, e3044cfb24b3c0de). Lu sur PDF.
  - Dispositif : environ 3,3 millions de résumés (1922-2018), dont 1,5 million jugés pertinents (p. 5) ; plongements de mots ; classement des matériaux par similarité avec « thermoelectric ».
  - Date gelée, p. 2 : « 18 different 'historical' text corpora consisting only of abstracts published before cutoff years between 2001 and 2018 » ; les 50 premières prédictions étaient « on average eight times more likely to have been studied as thermoelectrics within the next five years as compared to a randomly chosen unstudied material … and also three times more likely than a random material with a non-zero DFT bandgap ».
  - Exemple, p. 2 : CuGaTe2 aurait été dans les 5 premiers quatre ans avant sa publication en 2012.
  - Réserves : p. 10, sur les 50 premières prédictions faites avec le corpus complet, « 48 materials (32%) had already been studied as thermoelectrics in papers that were not represented in our corpus ». Le « succès » mesure une co-mention future, pas une propriété vérifiée. Même tendance pour trois autres mots-clés (p. 4), mais les chiffres sont dans les annexes, non lus.
  - Nature de la preuve : épreuve rétrospective à date gelée (observationnelle).
- **Krenn et Zeilinger 2020**, PNAS 117 ; version arXiv:1906.06843v2 (`krenn2020.pdf`, d9031cba31228cff), pas la version PNAS. Lu sur PDF.
  - Dispositif : réseau sémantique de concepts tiré de 750 000 articles depuis 1919 (p. 1) ; un réseau de neurones prédit si deux concepts non reliés le seront dans 5 ans.
  - Résultat, p. 5 : « The ROC validation curves for 1995, 2005 and 2017 (trained with SEMNET using data from only 1990, 2000 and 2012 and earlier …) are consistently and significantly non-random, with AUC2017 = 0.85 ».
  - Limite : la restriction aux paires partageant moins de 20 % de voisins (p. 6) est la seule garde contre les liens triviaux ; aucune vérification de la valeur scientifique des liens prédits.

### 3. Jeppesen et Lakhani 2010 — la marginalité dans la recherche diffusée à l'extérieur
- Version de travail Harvard DASH, « Forthcoming » (`jeppesen2010b.pdf`, 77a3c885d55615e8), pas la mise en page publiée de Organization Science 21:1016-1033.
- Dispositif, p. 2 : « 166 science challenges involving over 12,000 scientists » (concours InnoCentive) ; 49 problèmes sur 166 résolus, soit 29,5 % (p. 24).
- Résultat sur la distance, p. 31 [imprimé 30] : « for every increment increase in the self-assessed 'Problem-Expertise Distance' scale, the odds of creating a winning solution increase by 3.3% (significant at the 10% level with a standard error of 0.017) ». Autre résultat : être une femme accroît la probabilité de gagner de 23,4 % (seuil de 1 %).
- Taille effective : enquête auprès de 320 résolveurs (288 hommes, 32 femmes) sur 93 des 166 problèmes (p. 32) ; 64,4 % des gagnants et 30,1 % des non-gagnants ont répondu (p. 26).
- Nature de la preuve : corrélation (modèle de sélection en deux étapes). La distance est **auto-déclarée** ; les auteurs reconnaissent eux-mêmes ce biais de mesure (p. 32-33).
- Effet faible et significatif seulement à 10 %. Même modèle, p. 31 : « solvers who indicate fewer scientific interests, i.e. specialists, are more likely to develop winning solutions » (seuil de 10 %), ce qui va **contre** l'idée reçue.

### 4. Catalini 2018 — Jussieu (désamiantage)
- PDF **non obtenu** : MIT DSpace a renvoyé une erreur 429 (pare-feu) et CORE une vérification anti-robot ; je n'ai pas contourné. Lu sur la page HTML IDEAS/RePEc (**résumé seulement**) : « colocation increases the likelihood of joint research by 3.5 times, an effect that is mostly driven by lab pairs that face higher search costs ex ante. … separation does not negatively affect collaboration between previously colocated labs. However, while colocated labs grow increasingly similar in topics and literature cited, separated ones embark on less correlated research trajectories. … after colocation, labs are more likely to pursue both lower-quality projects (a selection effect) and high-quality projects (an effort effect). Opposite effects on quality are observed after separation. »
- Nature de la preuve : expérience naturelle (contraintes de placement des laboratoires). La taille de l'échantillon et les coefficients ne sont pas vérifiés.
- La proximité accroît la dispersion de la qualité (plus de projets faibles et plus de projets forts) et **rapproche** les sujets : la proximité fait naître des collaborations, mais réduit la divergence des trajectoires.

### 5. Boudreau et al. 2017 — expérience aléatoire sur les coûts de recherche d'un partenaire
- Seule la version de travail a été lue : Boudreau, Ganguli, Gaule, Guinan, Lakhani 2012, « Colocation and Scientific Collaboration: Evidence from a Field Experiment », HBS WP 13-023 (`boudreau2017_wp.pdf`, d87b1fe61239dcf5). La version publiée (ReStat 99:565-576) n'est pas lue ; d'après le résumé cité par la recherche sur la toile, elle annonce +75 %, chiffre non vérifié sur PDF.
- Dispositif, p. 10 : 435 candidats invités à un symposium de financement en imagerie ; répartition **aléatoire** dans des salles pour une séance de 90 minutes ; 7 149 paires dans une même salle (p. 16).
- Résultat, p. 6 : « being in the same room at the event increases the likelihood of collaboration by about 70% (from 0.16% to 0.28%) » ; 19 paires co-candidates contre 11 attendues sans effet (p. 16).
- Effet plus fort pour les anciens coauteurs, pour les paires comprenant une femme et pour les paires travaillant dans des domaines cliniques **proches** (p. 3). La rencontre fabrique surtout des liens **proches**, pas lointains.

### 6. Azoulay et al. — décès de vedettes ; incitations
- **Azoulay, Fons-Rosen, Graff Zivin**, NBER w21788, version révisée de juin 2018 (`azoulay_funeral_nber.pdf`, 982ea8fac45f88fc), pas la version AER 2019.
  - Dispositif : 452 vedettes des sciences de la vie mortes prématurément (p. 2) ; 3 076 sous-champs traités ; différence de différences contre des sous-champs témoins (p. 11, 13).
  - Résultats, p. 19-20 : publications des collaborateurs −20,7 % ; publications des non-collaborateurs « 100 × (e0.082 − 1) = 8.6% » ; effet net d'environ 5,2 %, imprécis.
  - P. 2 : les contributions supplémentaires sont « disproportionately likely to be highly cited » et viennent de chercheurs « not previously active in the deceased superstar's field ».
  - Nature de la preuve : expérience naturelle (mort prématurée), 41 % de morts soudaines (p. 9).
  - Le mécanisme proposé est la barrière à l'entrée des extérieurs (p. 25-28). C'est un résultat sur l'**entrée** des extérieurs, pas sur un lien entre domaines.
- **Azoulay, Graff Zivin, Manso**, NBER w15466 (2009) (`azoulay_incentives_nber.pdf`, b2a27e65849ebcc1), pas la version RAND 2011.
  - Dispositif : 73 chercheurs de l'Institut médical Howard Hughes contre 393 lauréats de prix de début de carrière financés par les Instituts nationaux de la santé ; pondération par score de propension et différence de différences.
  - Résultats, p. 6 : publications +39 %, et « the magnitude jumps to 96% when focusing on the number of publications in the top percentile » (p. 25 : 97 % ; écart interne à la version de travail). Les chercheurs Howard Hughes « 'flop' more often … : they publish 35% more articles that fail to clear the (vintage-adjusted) citation bar of their least well cited pre-appointment work ».
  - Limite, p. 27 : « we cannot rule out a more nuanced selection story ». Corrélation corrigée, pas d'assignation aléatoire.

### 10. Boudreau, Guinan, Lakhani, Riedl 2016 — comment on note la nouveauté et la proximité
- Version publiée, Management Science 62:2765-2783, lue sur une copie tierce (gwern.net) (`boudreau2016_gwern.pdf`, 1f8c5b24307df883).
- Dispositif, p. 2 [2766] : 142 évaluateurs et 150 propositions, chaque évaluateur assigné **au hasard** à 15 propositions, soit 2 130 paires, en triple insu.
- Résultats :
  - p. 2 [2766] : « evaluators gave systematically lower scores to research proposals that were closer to their own areas of expertise … accounts for 1.1 points of variation on a 10-point evaluation scale » (écart-type de 1,7 après effets fixes) ;
  - p. 3 [2767] : « more novel proposals are associated with lower evaluations, with magnitudes … comparable to those associated with intellectual distance. It is proposals with particularly high levels of novelty … that account for this result. (For low levels … scores were increasing …) ».
- Nature de la preuve : causale pour la distance (assignation aléatoire) ; **non** causale pour la nouveauté (p. 3 : « not possible to experimentally vary the novelty »).

### 11. Chan, Dow, Schunn 2015 — sources d'inspiration proches ou lointaines
- Manuscrit des auteurs (`chan2015_ms.pdf`, f58a0a96479f1d86).
- Dispositif, p. 7 de la version sous presse : plateforme OpenIDEO, 12 défis, 2 341 concepts, dont 707 qui citent des sources ; distance mesurée par allocation de Dirichlet latente, validée contre des jugements humains (r = 0,51, p. 15) ; critère : être retenu par un jury d'experts (16 %).
- Résultat, p. 22 : « a 1-unit increase in DISTMAX predicted a .33 decrease in the log-odds of being shortlisted … p < .05 », avec un intervalle large (−0,06 à −0,60). P. 25 : distance moyenne −0,40, p < 0,05. Pente sans variation entre les défis (p. 24).
- Ce résultat va **contre** l'idée reçue : les sources **proches** sont associées à de meilleures idées.
- Limites, p. 26 : corrélation ; conditionnel aux concepts qui citent leurs sources ; sélection par un jury.

### 12. Teodoridis, Bikard, Vakili 2019
- Version acceptée LBS (`teodoridis2019_lbs.pdf`, d61dab908f818a16).
- Expérience naturelle : l'effondrement soviétique a accéléré le rythme dans certains domaines des mathématiques (p. 3).
- Résultats, p. 29 : dans les domaines lents, les spécialistes produisent « approximately 22 percent fewer citation-weighted publications » que les généralistes après 1989 ; dans les domaines rapides, « specialists increased their citation-weighted publication output relative to generalists by approximately 83 percent » ; les généralistes y perdent 37 %.
- L'avantage du généraliste (lien entre domaines) dépend du rythme du domaine ; il **s'inverse** quand la frontière bouge vite.

## Cas 2 — groupes qui explorent en parallèle, plus ou moins reliés

### 7a. Derex et Boyd 2016 (`derex2016.pdf`, 9734905a2ef864ec) — lu sur PDF
- Dispositif, p. 5 : 144 étudiants de Montpellier en groupes de 6 (12 groupes par condition) ; 72 essais ; paysage à deux trajectoires dépendantes du chemin. Groupes entièrement reliés contre trois sous-groupes de 2 avec des contacts occasionnels (p. 2).
- Résultat, p. 2 : « fully connected groups were able to discover A3 (50% of groups) and B3 (33.3%), but none … both … 91.7% of partially isolated groups discovered A3, 66.7% discovered B3, and 58.3% discovered both ».
- Contrepartie, p. 3 (figure 3) : « Fully connected groups outperformed partially connected groups in the short run before being trapped on local optima ».
- Nature de la preuve : expérience aléatoire en laboratoire, petit nombre de groupes. P. 4 : les auteurs expliquent leur écart avec Mason et Watts par la forme du paysage (chez Mason et Watts, toute position est accessible depuis toute autre).

### 7b. Bernstein, Shore, Lazer 2018 (`bernstein2018_dash.pdf`, 2b761816e7b1f164) — lu sur PDF
- Dispositif, p. 6 : triades tirées au sort entre influence constante, intermittente et nulle ; problème du voyageur de commerce ; 17 tours ; 514 observations triade-essai (tableau 1, p. 3).
- Résultat, p. 3 : « CT triads found the optimal solution in 33.3% of trials, IT triads … 48.3% … and NT triads … 44.1% (the difference between IT and CT was significant after controlling for covariates) ».
- La moyenne de l'influence intermittente vaut celle de l'influence constante, et sa meilleure solution vaut celle de l'absence d'influence. Les triades sans influence trouvent 1,108 fois plus de solutions distinctes que les triades à influence intermittente (P = 0,010), sans trouver l'optimum plus souvent (p. 3).

### 8. Lazer et Friedman 2007 contre Mason et Watts 2012
- **Lazer et Friedman 2007**, ASQ 52:667-694 ; copie tierce typeset.io (`lazer2007_typeset.pdf`, 2196149bd8e590ab). Simulation multi-agents sur des paysages NK (N = 20, K = 5, 1 000 paysages, p. 12) ; réseau linéaire contre réseau entièrement relié (100 agents).
  - P. 1 [667] : « the more efficient the network at disseminating information, the better the short-run but the lower the long-run performance … For intermediate time frames, there is an inverted-U ».
  - P. 13 : « the linear network performs significantly better » à long terme.
- **Mason et Watts 2012**, PNAS 109:764-769 : PDF **non obtenu** (PNAS et PMC bloqués par une vérification anti-robot). Résumé PubMed lu par eutils (**résumé seulement**) : « 256 Web-based experiments in which groups of 16 individuals … In contrast to prior work, however, we found that efficient networks outperformed inefficient networks, even in a problem space with qualitative properties thought to favor inefficient networks ».
- **Ce qui se contredit** :
  - la simulation dit que le réseau lent préserve la diversité et gagne à long terme ;
  - l'expérience humaine dit que le réseau efficace gagne.
- **Explication proposée par un tiers** : Shore, Bernstein, Lazer 2014/2015, HBS WP 14-075 (`shore2015_factsfiguring.pdf`, 9d7bcc449c36de43), p. 6 : « While Lazer and Friedman (2007) found that inefficient networks with a long average path length … explored more, Mason and Watts (2012) found that inefficient networks—with, importantly, a high level of local clustering not present in Lazer and Friedman's (2007) networks—explored less ». Leur propre expérience (organisations de 16 personnes) : le regroupement local accroît l'exploration de l'**information**, mais réduit l'exploration des **solutions** (résumé, p. 3).
- **Lecture** : « relier moins » ne suffit pas ; ce qui compte, c'est la longueur des chemins sans regroupement local, la forme du paysage (Derex, p. 4) et l'horizon.

### 9. Uzzi et Spiro 2005 ; Burt 2004
- **Uzzi et Spiro 2005**, AJS 111:447-504 ; épreuve d'auteur (`uzzi2005.pdf`, c26039cb2831d87c).
  - Dispositif, p. 19 : 2 092 personnes et 474 comédies musicales de Broadway (1945-1989) ; mesure Q du « petit monde ».
  - Résultat, p. 42 : « at the predicted bliss point of Q (about 2.6), a musical's probability of being a hit is about 2.5 times greater than the lowest value of Q (about 1.4), while the probability of a flop drops by 20% » ; succès artistique environ 3 fois plus probable au point optimal. Les auteurs précisent que le succès souffre davantage de trop peu de connexion que de trop.
  - Nature de la preuve : corrélation sur données d'archives ; modèles annuels sur N = 45 et N = 37 (p. 22).
- **Burt 2004**, AJS 110:349-399 ; scan ProQuest sans couche de texte, lu sur image (`burt2004.pdf`, b0e94133ac8afa02).
  - Dispositif : gestionnaires de la chaîne d'approvisionnement d'une entreprise d'électronique ; 455 idées notées par deux dirigeants (tableau 4, p. 33 [381]).
  - Résultat, p. 32 [380], tableau 3 : valeur moyenne des idées de 2,4 pour une contrainte de réseau faible contre 1,5 pour une contrainte forte ; idées écartées 14 % contre 43 %. P. 33 [381] : t = −5,8 et −3,9 selon le juge ; corrélation de −0,43 chez les cadres supérieurs.
  - Nature de la preuve : corrélation dans une seule entreprise. Les juges, eux-mêmes intégrateurs entre unités, préfèrent peut-être les idées de courtiers (note 16, p. 33).

### 13. Modèles de langage mis en réseau (2024-2026) — deux lectures
- **Regan, Gournail, Oka 2024**, arXiv:2406.12374v3 (`regan2024.pdf`, 472d4c6fcc44a585).
  - Dispositif, p. 4 : 25 agents GPT-3.5-Turbo, 4 tours de débat, 100 questions de mathématiques MMLU posées 3 fois.
  - Tableau 1, p. 4 : connexion totale 67,7 ± 1,1 % (125 000 jetons par tour) ; aléatoire 68,2 ± 0,5 % (28 600) ; réseau sans échelle caractéristique 64,8 ± 1,0 % ; déconnecté 63,9 ± 0,4 %.
  - Des nœuds centraux biaisés entraînent le groupe (p. 3). Le résultat porte sur la justesse d'une réponse unique, pas sur la diversité.
- **Chen et al. 2026**, « Diversity Collapse in Multi-Agent LLM Systems », arXiv:2604.18005v2 (`arxiv2604.18005.pdf`, 2cd3f6709853bb0e), prépublication non revue.
  - Idéation ouverte, diversité mesurée par le score de Vendi.
  - P. 1 : « dense communication topologies accelerate premature convergence … this collapse arises primarily from the interaction structure rather than inherent model insufficiency ».
  - P. 7 : l'écriture à l'aveugle avant discussion (« Nominal Group Technique ») maximise la diversité initiale ; les sous-groupes maintiennent le conflit constructif.
  - P. 5 : la collaboration interdisciplinaire par rôles donne la diversité la plus **faible** (Vendi 4,65 contre 8,08).
  - Les chiffres de topologie ne sont lus que sur figure.
- Voisin noté sans lecture approfondie : Li et al. 2024, arXiv:2406.11776. La topologie voisine fait +2 % sur MATH et 40 % de jetons en moins (p. 2 du fichier téléchargé, lequel ne fait que 2 pages ; fichier non gardé).

## Synthèse (huit lignes)
**Cas 1 (domaines disjoints)**
1. Le lien entre littératures se prédit à date gelée : environ 8 fois le hasard pour les matériaux (Tshitoyan) et une aire sous la courbe de 0,85 en physique quantique (Krenn). La valeur de ces liens et le cas biomédical (Swanson, Henry et McInnes) n'ont pas été vérifiés ici.
2. La distance du résolveur aide faiblement : +3,3 % de chances par cran, seuil de 10 %, distance auto-déclarée (Jeppesen). Chan trouve l'inverse pour les sources d'inspiration lointaines, et Teodoridis l'inverse quand le domaine va vite.
3. Les juges pénalisent la très forte nouveauté et la proximité avec leur domaine (Boudreau 2016, assignation aléatoire). La mort d'une vedette ouvre l'entrée des extérieurs (+8,6 %, Azoulay). La tolérance à l'échec s'accompagne de plus de succès extrêmes et de 35 % d'échecs en plus (corrélation).

**Cas 2 (groupes en parallèle)**
4. La proximité et la rencontre créent des liens (×3,5 à Jussieu, expérience naturelle ; +70 % dans une salle tirée au sort), surtout entre proches, et font converger les sujets (Catalini).
5. La connexion partielle ou intermittente bat la connexion totale sur l'optimum (58 % contre 0 %, Derex ; 48 % contre 33 %, Bernstein), au prix d'un départ plus lent.
6. Contradiction : Lazer et Friedman (simulation) favorisent le réseau lent, Mason et Watts (humains) le réseau efficace. Le regroupement local et la forme du paysage l'expliqueraient (Shore ; Derex).
7. Les données corrélationnelles disent qu'un degré intermédiaire de connexion est le meilleur (Uzzi) et que le courtage entre groupes va avec de meilleures idées (Burt).
8. Chez les modèles de langage, la connexion dense contracte la diversité. Les réseaux clairsemés égalent la connexion totale pour bien moins cher ; c'est en prépublication, et sur la justesse plus que sur la découverte.

## Non vérifié
- Swanson 1986 (PDF payant) ; la chaîne exacte des intermédiaires.
- Henry et McInnes 2017 ; Sebastian et al. 2017 ; toute évaluation à date gelée en biomédecine.
- Catalini 2018 : texte intégral (refus MIT et CORE) ; taille de l'échantillon, coefficients et page.
- Mason et Watts 2012 : texte intégral (refus PNAS et PMC) ; chiffres hors résumé.
- Boudreau et al. 2017, version publiée : le chiffre de +75 % ; seule la version de travail (+70 %) est lue.
- Versions publiées d'Azoulay 2019 (AER) et 2011 (RAND), et de Jeppesen et Lakhani 2010 : les pages et chiffres peuvent différer des versions de travail lues.
- Tshitoyan : résultats sur trois autres mots-clés (annexes non lues).
- Chen et al. 2026 : valeurs numériques par topologie (figures seulement).
