**Pièces et statuts.**

- Le bloc QUESTION DE L'ARBITRE reproduit le bloc FAITS (texte identique à la lecture, même empreinte déclarée ; je n'ai pas recalculé les sha256). Il ne pose aucune question propre au tour : je traite le livrable du tour III.2 dans la forme qu'il fixe.
- Les pièces B, C, D, E sont présentes et se terminent par leur ligne de fin ; aucune coupure visible. Ma conception A du tour III.1 n'est pas transmise : je ne m'y réfère pas.
- Statuts. Ce que je cite des pièces est OBSERVÉ-NON-AUDITÉ (lecture). Les conséquences algébriques que je tire de leurs définitions sont OBSERVÉ-NON-AUDITÉ (à recalculer par un tiers). Mes diagnostics de confusion sont des HYPOTHÈSES. Les deux références que j'ajoute sont RAPPORTÉES de mémoire. Rien n'est VÉRIFIÉ.
- Tous mes chiffres sont illustratifs : ils découlent des effectifs illustratifs des pièces, par l'approximation de Hanley & McNeil (1982, « The meaning and use of the area under a receiver operating characteristic (ROC) curve », *Radiology*).
- Je ne modifie aucun statut posé par les auteurs ; je signale seulement où VÉRIFIÉ est apposé sur un énoncé que les faits transmis ne contiennent pas.

## Sur la proposition B

### (a) Défauts de méthode

1. **« Π indépendant de D_u par construction » ne tient pas.** Effacer les noms rend les deux *mesures* disjointes, pas les deux *variables* indépendantes. Les types de prédicat de SemMedDB dépendent de la classe sémantique des concepts (un médicament « traite », un gène « interagit »). Π encode donc cette classe, qui covarie avec D_u et avec le taux de base de formation des liens (médicament–maladie). Un gain en D1 peut n'être que ce taux de base. La permutation des types détruit ce signal en même temps que la structure : elle ne les sépare pas.
2. **Fuite de l'extracteur vers la cible.** Π et l'étiquette positive (« première prédication 2006–2015 ») sortent du même extracteur. La propension d'un concept à produire des prédications extractibles est cause commune d'un voisinage riche et d'un lien futur détecté.
3. **Sélection sur une covariable bruitée.** L'échantillon est le quintile supérieur de D_u. Par régression vers la moyenne, les paires qui s'y lient ensuite sont celles dont D_u est surestimé (mots rares, plongements mal estimés). Π sert alors de seconde mesure de la proximité d'usage.
4. **D2 n'est pas testable dans l'expérience 7**, qui le vise pourtant. γ2 demande une variation de D_u, et l'échantillon la tronque. Le « contrôle négatif » de D2 (ajuster sur les paires proches) n'en est pas un : H1 n'y prédit pas un effet nul. Le signe d'une interaction en échelle logit dépend en outre du lien choisi quand le taux de base varie fortement avec D_u.
5. **D3, version non conditionnée vraie par construction.** σ = −log P̂ ; si B0 est calibré, P(L=1 | σ) = e^{−σ}. Comme F = 0 sans lien, E[F | σ] = e^{−σ}·E[F | σ, L=1] : la forme est dominée par un facteur imposé par la définition de σ. La version conditionnée, elle, conditionne sur un collisionneur : un lien formé malgré un σ élevé est sélectionné sur une qualité non observée.
6. **D4.** Le contrôle « M calculé avec des méthodes postérieures doit être nul » passe par définition (a_im = 0 avant l'existence de m) : il teste le codage des dates, rien d'autre. Les catalogues d'Ogburn & Thomas et de Merton portent sur des périodes sans corpus en texte intégral : M n'y est pas calculable. L'appariement ne contrôle pas le volume d'activité, qui gonfle à la fois M et la fréquence des multiples.
7. **D6** ne définit pas « plus près des nœuds » une fois le degré fixé : pas d'estimateur, pas de jugement possible. F (nombre de groupes) croît mécaniquement avec le nombre d'auteurs travaillant sur les extrémités.
8. **Calibration 1 (renommage).** Un jeton renommé a exactement le profil de fréquence et de degré de l'original : la « vérification mécanique à battre » atteint le plafond, rien ne peut la battre.
9. **D5 et ancrage (d).** Si la période de test doit suivre la coupure de Pythia ou d'OLMo, la fenêtre de fécondité [t+Δ, t+2Δ] n'est pas écoulée : F est censuré.
10. **B4.** D1 laisse une zone sans verdict : gain entre 0 et 0,02 avec intervalle excluant 0.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **ΔAUC-PR (D1).** Le niveau du hasard vaut la prévalence π. Le seuil absolu 0,02 n'est pas jugeable tant que π et la loi d'échantillonnage des négatifs (ratio r, « correction » non spécifiée) ne sont pas fixés : l'estimateur n'est pas invariant en r.
- **Π.** Puissance nulle quand Var(Π | log k_i k_j, CN, D_u, classe sémantique) → 0. Contrôle permuté non informatif quand la loi marginale des types a une entropie faible (type dominant de probabilité p_max → 1 : la permutation est presque l'identité).
- **Bruit d'extraction.** Avec un taux d'arêtes fausses ε, la probabilité qu'un voisinage de m_h arêtes soit intact décroît comme (1−ε)^{m_h} : Π tend vers le bruit pour les concepts de fort degré.
- **γ2.** Non identifiable quand Corr(Π, Π·D_u) → 1, ce qui arrive dès que Var(D_u | quintile supérieur) est petite.
- **Deux droites (D3).** « p < 0,05 par pente » est atteint pour des pentes arbitrairement petites quand n est grand ; non jugeable sans taille d'effet minimale. Non identifié si P(L=1 | σ, q) dépend d'une qualité q non observée.
- **OR de D4.** L'information vient des seules paires discordantes : puissance nulle quand P(M>0) → 0 ou 1 ; non jugeable quand l'écart-type de l'erreur de datation des adoptions est de l'ordre de τ.
- **Contrôle « |gain| < 0,005 ».** Exige un écart-type de ΔAUC-PR nettement sous 0,005, donc un nombre de positifs n₊ que la pièce ne calcule pas.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Cible placebo :** la simple co-mention future sans prédication. Si Π la prédit aussi bien, il mesure l'activité ou l'extractibilité.
- **Permutation des types à l'intérieur des strates de classe sémantique**, et modèle concurrent réduit à l'indicatrice de la paire de classes.
- **Cible indépendante de l'extracteur** (indexation humaine), pour rompre la fuite 2.
- **Méthodes placebo** de même fréquence et de même date d'apparition, pour M.
- **Simulation sous B0 seul** de la courbe F(σ), pour voir si la sélection suffit à produire un U inversé.

## Sur la proposition C

### (a) Défauts de méthode

1. **Fécondité contenant son prédicteur.** La définition formelle est Fécondité = s_R × (gain de proximité au cœur). Tester que s_R prédit cette grandeur serait vrai par construction. Le duel 1 emploie une autre cible (≥ 10 citations de communautés tierces) : le modèle formel et le test ne portent pas sur la même grandeur.
2. **Duel 2, branche inatteignable.** Les méthodes m sont des nœuds de V_t. ΔPMI(u,m) > 0 et ΔPMI(v,m) > 0 imposent des cooccurrences u–m et m–v, donc un chemin de longueur 2 et B_2(u,v) > 0. La strate « w_t élevé et B_2 = 0 », qui devait réfuter H_B, est vide par construction, sauf à exclure les méthodes de E^(S), ce que la pièce ne dit pas. H_A et H_B ne sont de plus pas exclusives : les deux OR peuvent dépasser 1,5.
3. **Appariement sur une variable postérieure (expérience 7).** Le facteur d'impact de la revue de 2016 est une conséquence de la qualité perçue de l'idée et du prestige des auteurs. Le fixer ouvre un chemin entre s_R et le prestige (à revue égale, une paire structurellement faible a été portée par des auteurs établis), lequel agit sur la reprise. Le sens du biais est inconnu.
4. **Groupes extrêmes.** Féconds (≥ 15 reprises) contre stériles (0), milieu supprimé : l'AUC sur extrêmes majore l'AUC en population. Les seuils 0,58 et 0,62 ne se lisent pas comme une discrimination ex ante.
5. **« M_0 à 0,50 par construction »** ne vaut que pour les variables appariées ; le score z d'Uzzi, qui fait partie de M_0, ne l'est pas. L'appariement « exact » sur des variables continues est de probabilité nulle : il faut des tolérances, donc un déséquilibre résiduel non rapporté.
6. **Fuite temporelle asymétrique.** S_H9 utilise `scibert_scivocab_uncased`, publié en 2019 (Beltagy, Lo & Cohan, 2019, « SciBERT: A Pretrained Language Model for Scientific Text », EMNLP ; RAPPORTÉ, date du corpus à vérifier), donc après t_0 = 2015. S_H3 est gelé en 2015. La lecture « H3 réfutée au profit de H9 » peut être un artefact de fuite. Le même modèle sert à extraire E^(R) à grande échelle.
7. **Asymétrie de taille.** L'appariement porte sur le produit des degrés, pas sur leur rapport. Le coût de Gromov-Wasserstein entre N_2(u) et N_2(v) dépend de l'écart de taille : s_R peut ne mesurer que la symétrie des degrés. Le minimum sur φ décroît en outre sous l'hypothèse nulle quand le nombre d'applications possibles croît.
8. **Unité d'analyse.** Un résumé à n concepts crée n(n−1)/2 paires qui partagent le sort de l'article. Les citations sont celles de l'article, pas de la paire.
9. **Jeux de calibration faits main.** Les 200 analogies « validées » (diffusion thermique et Fick) sont célèbres, donc énoncées dans tout corpus : fuite pour l'instrument textuel. Les faux amis sont choisis par l'auteur du modèle. I4 n'est validé qu'« après filtrage par Δ_lock », c'est-à-dire par un autre instrument sous test.
10. **Duel 3.** Masquer verbes et opérateurs fait chuter par construction toute chaîne qui extrait ses relations des verbes ; cela ne montre pas que la structure est ce qui prédit.
11. **Statuts.** La pièce appose VÉRIFIÉ sur des énoncés absents des faits transmis (équivalent « exact » de Noether, seuil λ_max > 1, disponibilité des bases). Je ne change pas ces statuts ; je note qu'aucune pièce transmise ne les fonde.
12. **B4.** Zones sans verdict : AUC(S_H3) dans [0,58 ; 0,62) ; écart avec S_H9 entre 0 et 0,05 ; contrôle permuté hors de [0,48 ; 0,52].

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **AUC à 500 + 500.** L'écart-type de l'estimateur vaut environ 0,018 près de 0,60 (illustratif). Les seuils 0,58 et 0,62 sont séparés de 2,2 écarts-types : si l'AUC vraie vaut 0,60, environ trois tirages sur quatre tombent dans la zone sans verdict.
- **Contrôle permuté.** Sous une AUC vraie de 0,50, l'écart-type est d'environ 0,018 ; l'estimateur sort de [0,48 ; 0,52] avec une probabilité d'environ 0,27 (illustratif). La branche « validation » échoue donc une fois sur quatre quand tout est correct, sauf à moyenner sur K permutations.
- **DeLong.** Un écart de 0,05 avec p < 0,01 demande un écart-type de la différence ≤ 0,019, donc une corrélation entre les deux estimateurs d'AUC d'au moins 0,41 (illustratif). En dessous, le critère conjoint est inatteignable pour un écart vrai de 0,05.
- **Grappes.** Avec m paires par article et une corrélation intra-article ρ_a, l'effectif efficace est n / (1 + (m−1)ρ_a) ; un bootstrap non groupé donne des intervalles trop étroits.
- **Δ_lock.** Sans puissance quand R²(Δ_lock ~ |N(u)|, |N(v)|) → 1, et quand la régularisation entropique ε est grande (le couplage tend vers la loi produit, qui ignore les types).
- **Duel 2.** P(B_2 = 0, w_t > 0) = 0 : l'OR sur cette strate n'est pas défini.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Encodeur entraîné jusqu'à 2015 seulement** pour S_H9 ; sans lui la branche « H9 l'emporte » n'est pas interprétable.
- **Réanalyse sans appariement sur la revue.**
- **Loi nulle de Δ_lock** sur des paires aléatoires appariées en tailles de voisinage et en rapport de degrés.
- **Contrôle intra-article :** s_R doit distinguer la paire visée de ses paires sœurs du même résumé.
- **Nul de volume pour les « jumeaux » :** nombre de coïncidences à 90 jours attendu sous un processus de Poisson d'intensité proportionnelle à l'activité du champ.
- **Cible placebo antérieure à t_0** (reprises passées) : s_R ne doit pas la prédire à covariables appariées.

## Sur la proposition D

### (a) Défauts de méthode

1. **S_struct ignore les types dans son terme principal.** Le terme de Gromov-Wasserstein ne compare que des distances de plus court chemin ; les types n'entrent que par μ·C(Π). Le contrôle de V1 (permuter les étiquettes d'opérateurs à topologie constante) laisse ce terme inchangé. Si le pouvoir prédictif vient de la forme ou de la taille des arbres, le gain subsiste après permutation et H_A est déclarée réfutée, alors qu'on a seulement montré que la mesure est aveugle aux types.
2. **Z sans partie positive.** Z = Σ α_m(u)α_m(v) : deux concepts qui abandonnent ensemble une méthode (deux taux négatifs) reçoivent une « co-exposition » positive. Les méthodes généralistes en croissance partout donnent Z > 0 à presque toutes les paires.
3. **V2, étiquette construite avec le futur.** Les multiples modernes doivent être « co-cités ensuite » au-delà d'un seuil : les jumeaux dont l'un a été ignoré sont exclus. La co-citation future covarie avec l'effervescence du champ, donc avec ΔZ. L'appariement des singletons sur l'impact à 5 ans conditionne sur une variable postérieure. Le contrôle par adverbes de même *fréquence* passe par construction : leur taux de croissance est presque nul, alors que Z est fait de taux de croissance.
4. **Cible de V1.** F_épist (gain de MDL sur des observations futures) n'a pas d'estimateur. La cible effective est le décile supérieur de citations, c'est-à-dire la reconnaissance sociale que la partie 1 séparait de la fécondité.
5. **Expérience 7.1.**
   - AUC_éq ≥ 0,80 est en grande partie acquis d'avance : les positifs sont *choisis* pour l'isomorphisme de leurs équations, puis l'aligneur d'équations doit le retrouver. Ce volet est un contrôle positif, pas une moitié d'hypothèse.
   - Désinfection différentielle : les couples positifs contiennent plus de phrases-ponts à retirer que les leurres. Volume et vocabulaire restants diffèrent selon la classe : l'étiquette fuit dans les traits.
   - Désinfecter le corpus ne désinfecte pas les poids : SciBERT, BGE et Qwen ont pu lire les manuels qui énoncent ces analogies. Seul le bras SVD-PPMI est propre. Le « contrôle positif de fuite » ne vérifie que la voie du corpus.
   - Les 40 couples sortent de quelques familles d'équations (diffusion, oscillateur, onde) : les unités ne sont pas indépendantes.
6. **V3.** Des chercheurs du domaine peuvent connaître l'issue des hypothèses historiques ; celui qui réécrit en « style neutre » la connaît. I_psych(u,v;t_0) n'est pas calculable pour des hypothèses antérieures aux corpus. d_max est un paramètre libre.
7. **Calibration 3.** Séparer une loi compressible d'un bruit incompressible par le gain de compression est vrai par définition de l'instrument.
8. **Multiples.** Seul le produit M·∫λ est identifiable, M (nombre d'équipes) n'étant pas observé. La fenêtre de 90 jours mesure aussi les délais de publication, qui diffèrent entre arXiv et PubMed.
9. **Statuts.** VÉRIFIÉ est apposé sur des énoncés hors des faits transmis ; je le signale sans rien modifier.
10. **B4.** V2 : |AUC_Z − AUC_χ| < 0,06 avec un maximum ≥ 0,55 ne réfute rien. V3 : AUC_vérité dans [0,55 ; 0,65) ne réfute rien, et H_B n'est réfutée que si la corrélation atteint aussi 0,35. 7.1 : AUC_texte ≤ 0,55 avec AUC_éq < 0,80 ne réfute rien.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **V3 à 60 + 60.** Écart-type de l'AUC d'environ 0,052 (illustratif). Si l'AUC vraie vaut 0,60, l'estimateur tombe sous 0,55 ou atteint 0,65 avec une probabilité totale d'environ 0,33 : un tiers des tirages « réfute » une hypothèse au hasard.
- **7.1.** Avec G familles d'équations de parts s_g, l'effectif efficace est borné par 1/Σ s_g². Si trois familles dominent, il est de l'ordre de 3, pas de 40.
- **Contrôle de V1.** Non informatif quand μ²·Var(C(Π)) ≪ Var(terme de Gromov-Wasserstein) : la loi de S_struct permuté coïncide avec celle de S_struct.
- **Z.** Perd son sens quand P(α_m(u) < 0, α_m(v) < 0) n'est pas négligeable. Perd sa puissance quand la première composante principale des α explique une part de variance proche de 1 : Z devient presque constant à l'intérieur d'une strate annuelle.
- **AUC_Z.** Biaisée vers le haut d'une quantité croissante en Corr(co-citation future, Z), puisque P(étiqueté multiple | multiple vrai) dépend de la co-citation.
- **Désinfection.** Non jugeable si la loi du nombre de tokens retirés diffère entre classes ; l'égalité des deux lois se teste avant toute AUC.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Désinfection factice des leurres**, à volume retiré égal.
- **Plongements neuronaux entraînés sur le seul corpus désinfecté** ; à défaut, AUC_texte ≥ 0,70 obtenu par un modèle préentraîné ne dit rien de H9.
- **S_struct à μ = 0** (topologie seule) et **sac d'étiquettes sans topologie**, rapportés séparément ; arbres aléatoires de même taille.
- **Termes placebo appariés en taux de croissance**, et Z restreint aux taux positifs.
- **Jumeaux définis sans critère de co-citation future**, comparés au nombre de coïncidences obtenu en permutant les dates de soumission à l'intérieur de chaque champ-année.
- **Question de reconnaissance** posée aux évaluateurs de V3, avec exclusion des items reconnus.

## Sur la proposition E

### (a) Défauts de méthode

1. **Étalon défini par l'instrument (expérience 7).** L'étalon-or est « partager un sous-arbre opératoire ». La branche qui réfute H_A exige que « l'alignement AST dépasse +0,15 » sur cet étalon : acquis par construction. Elle se réduit à la condition sur le texte.
2. **Pont par le nom de l'équation.** Deux concepts sans cooccurrence directe, mais régis par l'opérateur de Fokker-Planck, cooccurrent chacun avec le *nom* « Fokker-Planck ». C'est un chemin de longueur 2 que capte Adamic-Adar, donc B1. Le duel « texte contre B1 » peut échouer alors que le texte porte la structure par son nom, ou réussir grâce à ce nom sans rien extraire d'abstrait.
3. **Registre mathématique.** Les négatifs sont appariés en discipline, date et fréquence, pas en densité d'équations. « Sous-arbre non trivial » n'est pas défini ; s'il est générique (dérivée temporelle, exponentielle), les positifs sont simplement des paires de domaines mathématisés, que le texte sépare par le vocabulaire technique.
4. **Encodeur possiblement sous-entraîné.** Un RoBERTa-base entraîné de zéro en 24 à 48 heures peut échouer par manque d'entraînement. Aucun contrôle positif de compétence n'est prévu ; un échec serait alors attribué à H9.
5. **Extracteur postérieur à T_0 pour I_t.** Qwen2.5 ou Llama-3.1 reconnaissent mieux comme « méthode » une technique devenue célèbre après 2016. Le rappel de l'extraction dépend du succès futur : I_t corrèle avec la cible par l'extracteur.
6. **I_t confondu avec le volume, variable de H_B.** Le cosinus entre vecteurs TF-IDF creux est atténué quand les comptes sont faibles. Deux concepts dont le volume croît voient leur similarité monter mécaniquement, sans convergence réelle. Le placebo chronologique (permuter les dates d'adoption) casse aussi la tendance de volume : il ne sépare pas les deux explications. La couverture de PMC OA change dans le temps, ce qui ajoute une dérive de composition.
7. **Ontologies et attention.** Les curateurs enrichissent les concepts en cours d'étude. La profondeur de curation, donc C(φ), suit l'activité de recherche ; le degré de surface de B1 ne la contrôle qu'en partie. Pour les analogies historiques réfutées (calorique, éther), les conflits K(φ) figurent dans les ontologies *parce que* l'analogie a été réfutée.
8. **E3.** Le « progrès de compression » est la réduction de perte hors échantillon quand l'hypothèse est intégrée, mais l'ensemble 𝒟 n'est pas daté. S'il contient des observations postérieures à T_0, le prédicteur est une fonction de la cible ; il a de toute façon la forme de Y^épist. Les étiquettes « échec » (essai de phase II/III, rétractation) reflètent aussi toxicité, raisons commerciales et fraude, et les hypothèses arrivées en essai sont déjà sélectionnées. La fenêtre H4 donne à H_B un paramètre libre.
9. **U^hum.** La non-monotonie annoncée n'est pas garantie : si la divergence de Kullback-Leibler croît linéairement avec d^surf à S^struct fixé, U^hum est linéaire en d^surf.
10. **Section 5.3.** Le modèle est réfuté s'il ne bat pas B1 « **et** échoue au contrôle négatif ». Sans gain, le graphe permuté n'en donne pas non plus : « échouer au contrôle » n'est alors pas défini, et la condition peut être inatteignable. E1 emploie « ou ».
11. **Calibration 1 et expérience 7** partagent étalon et corpus (arXiv ≤ 2016, AST). Sans partition par famille d'équations, les seuils réglés sur l'une fuient dans l'autre.
12. **B4.** Zones sans verdict en 7.1 : gain entre +0,03 et +0,08 ; fausses alertes entre 15 % et 30 % ; détection réussie mais prédiction des mariages manquée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Étalon.** Sans puissance quand le rapport P(sous-arbre partagé | isomorphisme) / P(sous-arbre partagé | paire quelconque de domaines mathématisés) tend vers 1.
- **Familles.** Si les parts s_g des familles d'opérateurs suivent une loi à queue lourde, l'effectif efficace 1/Σ s_g² est très inférieur à 500 ; une permutation par bloc disciplinaire ne corrige pas cette dépendance.
- **AUC-PR.** La prévalence du plan est 500/3 000 = 1/6 : le hasard vaut 0,167 et les seuils ne valent que pour ce ratio.
- **I_t.** Biais de l'estimateur de l'ordre de (∂E[cos]/∂n)·Δn. Non jugeable quand Var(Δ log n) est grande devant la variance de la variation vraie de similarité ; sans puissance quand Corr(I_t, Δ log n) → 1.
- **Précision à 5 % (E3).** Sur N hypothèses, k = 0,05·N items, et l'écart-type d'une précision p vaut √(p(1−p)/k). La pièce ne fixe pas N ; pour N = 300 (illustratif), k = 15 et l'écart-type approche 0,13, au-dessus du seuil de 0,10. Il faut k de l'ordre de 100, soit N de l'ordre de 2 000 (illustratif).
- **S^struct.** Le maximum sur φ croît sous l'hypothèse nulle avec le nombre d'applications possibles ; sans puissance quand R²(S^struct ~ tailles des voisinages) → 1.
- **ΔBIC ≤ −10.** Atteint pour un effet arbitrairement petit quand n grandit ; à lire avec une taille d'effet.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Raréfaction :** I_t recalculé à nombre de tokens égal entre fenêtres et entre concepts ; termes placebo non méthodologiques de même fréquence et de même croissance.
- **Masquage des noms d'équations et des éponymes** dans le texte, et B1 recalculé sans eux.
- **Négatifs appariés en densité d'équations.**
- **Audit du rappel de l'extracteur de méthodes, stratifié par notoriété postérieure à T_0** ; variante par dictionnaire figé à T_0.
- **Scalaire de profondeur de curation** (nombre d'annotations) mis en concurrence avec S^struct.
- **Progrès de compression calculé sur 𝒟 ≤ T_0 seulement**, puis sur cibles permutées.

FIN-DE-CELLULE