# Préenregistrement — arène coévolutive synthétique : défense « mélange d'équilibre » contre défense « unique réentraînée » — v1 — BROUILLON 1 (non scellé)

Identifiant : **PREREG-ARENE-MELANGE-EQUILIBRE-V1**. Tâche : piste 3 du brainstorm P-041 (décision de Lazar R-695, « gooo », 31 octobre 2026, `registres/decisions.md` ligne R-695), test (b), sur processeur. Pilote de **mécanisme** : aucun modèle de langage, aucun texte, aucune entrée de modèle. « L'attaquant » est un choix de paramètres dans une famille bornée de lois synthétiques.

- Auteur : sous-agent neuf Opus 5.5 (lignée conv-audit), branche `canal/conv-audit-n04`.
- Date (UTC) : 2026-10-31, 07:45 (relevé `date -u`).
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient la version gelée de `arene_melange_v1.py` ; HEAD au moment du brouillon : `5919719a`, commit intermédiaire posé par l'agent parent, qui ne contient pas la version présente du code).
- Documents qui font foi (chemin + empreinte) :
  - `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` — `08360a9402ff81d7d9146ed833d60e687f1be4d9acd0be3ab2867403dda8eb10` (pistes 2, 3, 4, 5) ;
  - `…/p-041-pont-vers-les-vrais-modeles-v1/reponse-pont-p041-vrais-modeles-v1.md` — `e98d9f5a0ccbf6a77675fc922b318eec67d4838acf3b1e0ea8657b79928155a3` ;
  - `…/p-041-pont-vers-les-vrais-modeles-v1/comparaison-avec-session-depot-v1.md` — `0b87e8f24254899214b1a938436dec88c19e37b60d43185832019d53baf43332` ;
  - `docs/notes/anteriorite-P-041-v1/idee-P-041-est-elle-bonne-fusion-v3.md` (branche `origin/main`) — `343617ca195316a0339a8864eccf62f42275f551ee9144c3eaa6047ff7c02345` (trois scores (i), (ii), (iii)) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; validateur `src/controle_ia/prereg.py` — `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` ; manifeste `src/controle_ia/manifeste.py` — `1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d`.
- Code et sorties de ce dossier (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/`) :
  - `arene_melange_v1.py` — empreinte du code au brouillon 1 : `6402dc6b2998d2f48262ddfe1d4d0d13b6a6115fcc8d01852c3b7c8182fd0d3b` (à recalculer au gel : le code de décision **refuse de partir** si l'empreinte du fichier exécuté n'apparaît pas dans le texte scellé) ;
  - empreinte de la configuration `CONFIG_V1` : `6685585fcfc028e0617d6786eb78bdb4fc159930af8fdf0444be1085f960d2ca` (vérifiée de même par le code) ;
  - `essais/test_arene_melange_v1.py` — `52168b51dd2eff313af8dfcf4b7fbcd9c410f9111553240ba0687f0fa9a8d085` (à recalculer au gel) ;
  - `calcul-puissance-arene-melange-v1.py` — `65df7c5228b31ffb23a320009af278909e012973b1e76d42a05c7e1b215c1f5b` ; sa sortie `calcul-puissance-arene-melange-v1-sortie.txt` — `17863f83097d8380fae23dfbfdf00fc5e2ce3d7349ade194c2be020dbca63fda` (désignée **(M)** ci-dessous) ;
  - pilote sur racine d'essai `essai-pilote-racine-essai-v2.json` — `f094b495381db7e342e73432ccb16abfe1bdc06498c4f77928cd7e2d7aff78c5` (code `9ed8c8b5…`, même configuration ; voir § « Écarts de conception faits sur la racine d'essai »).

Tout nombre de ce texte vient de (M) (section citée entre crochets, par exemple [M § 2]) ou est un marqueur de gel (valeur laissée à Lazar). **Aucune lecture n'a été faite sur la racine de décision RACINE = 20261201 ni sur RACINE_TENUE = 20261202.**

## Résumé de dix lignes pour Lazar

1. Question : dans une arène coévolutive synthétique où l'attaquant joue en dernier, un défenseur qui tire au hasard l'un des moniteurs passés selon les poids d'équilibre du jeu à somme nulle (bras B) détecte-t-il mieux la meilleure réponse adverse finale qu'un moniteur unique réentraîné sur toutes les attaques passées (bras A, protocole de Bailey et collègues) ?
2. Témoins : C, mélange **uniforme** des mêmes types de moniteurs (sans programme linéaire) ; D, moniteur **unique à capacité égale** (autant de paramètres que le mélange de B), réentraîné sur toutes les attaques (hypothèse rivale : le mélange gagne parce qu'il porte plus de paramètres).
3. Famille bornée : mélanges de 3 gaussiennes en dimension 6, paramètres dans une boîte, contrainte de comportement « distance ≤ δ à une loi cible » (piste 2), deux valeurs de δ.
4. Pilote sur la racine d'essai (24 instances × 2 δ) [M § 2] : B − A sur (iii) = +0,125 (δ = 1,6) et +0,037 (δ = 2,4) ; mais D − B = +0,186 à δ = 1,6 ; B ≈ C ; B perd environ 0,06 sur les familles tenues à l'écart (ii).
5. Prédiction : H1 confirmée (signe +, les deux δ) ; **mais** la capacité égale fait au moins aussi bien, le programme linéaire n'apporte rien au-delà de l'uniforme (audit R4 attendu), et le gain sur (iii) se paie sur (ii).
6. Puissance [M § 3, § 4 bis] : avec S1 = 0,02 et N = 100 instances par δ, puissance 0,995 à un effet vrai de 0,03 ; erreur de première espèce ≤ 0,0013 (deux δ exigés).
7. Temps [M § 5] : 23,9 s de processeur par tâche ; N = 100 → 79,5 min de processeur, 41 min de mur sur 2 cœurs (plafond visé : 2 h de mur sur 2 cœurs).
8. Quatorze seuils à geler par Lazar (S1 à S14), chacun avec recommandation ; aucun défaut ne s'applique.
9. Rien sur les vrais modèles : un résultat ici dit seulement si le mécanisme « mélange d'équilibre » fait quelque chose dans une famille bornée connue.
10. Avant scellement : contre-lecture par un modèle différent (R2), gel des seuils par Lazar, recalcul des empreintes.

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels : ni sur Llama, ni sur les sondes de Bailey et collègues, ni sur la boucle à 70 tours. Le monde est une famille de lois que nous avons écrite (`reponse-pont-p041-vrais-modeles-v1.md` § 0 : un succès sur une famille bornée ne contredit pas Bailey et ne transporte pas).
- Aucune revendication d'antériorité ni de nouveauté : la zone « mélange d'équilibre de moniteurs contre attaquant adaptatif » n'est pas vérifiée (R8) ; références ci-dessous **SUPPOSÉ**.
- Aucun énoncé sur les moniteurs quadratiques, les réseaux profonds, d'autres dimensions, d'autres familles ou un attaquant en boîte noire.
- (iii) est une **borne haute** de la vraie valeur du jeu (l'attaquant est un optimiseur local) : on ne parle pas de « valeur du jeu certifiée ».
- Ni porte, ni dépense, ni modification de P-041 : le résultat est une pièce pour le tour 2 du collisionneur et pour la décision de Lazar sur P-041 v2.

## Antériorité (toutes SUPPOSÉ, non lues sur PDF pour ce texte)

Double oracle (McMahan, Gordon et Blum 2003) ; réponse stratégique à une population de politiques (Lanctot et collègues 2017) ; défenses randomisées contre attaques adverses (Pinot et collègues 2020). Bailey et collègues, arXiv `2412.09565v2`, lu sur PDF par session-depot (R-874) : seul le protocole est repris ici (réentraînement d'un moniteur sur toutes les attaques passées, attaquant qui répond au dernier moniteur) ; **aucun chiffre** de ce papier n'est repris (R7).

## Hypothèse

Renvoi : brainstorm P-041 piste 3 (« la réponse correcte à une suite de meilleures réponses adverses est un mélange aux poids d'équilibre ») ; piste 2 (famille paramétrée par la perte de comportement δ que l'attaquant accepte) ; piste 4 (nouveauté résiduelle) ; piste 5 (coût par contournement). Scores de la fusion v3 de P-041 : (i) familles vues, (ii) familles tenues à l'écart, (iii) générateur adaptatif contre la défense figée, l'attaquant jouant en dernier.

- **H1 (principale)** : contre la meilleure réponse adverse finale (l'attaquant joue en dernier, contre la défense figée après T tours), le taux de détection du bras B (mélange d'équilibre, double oracle) **dépasse** celui du bras A (moniteur unique réentraîné sur toutes les attaques passées), aux deux valeurs de δ.
- **H0** : pas de différence entre B et A sur (iii).
- **Hypothèse rivale R-cap** : si B dépasse A, c'est parce que le mélange porte plus de paramètres (T + 1 moniteurs linéaires contre un seul). Témoin : bras D, moniteur unique « maxout » (log-somme-exp de T + 1 scores linéaires), **même nombre de paramètres** que le mélange de B au même tour, réentraîné sur toutes les attaques passées. R-cap est soutenue si D fait au moins aussi bien que B.
- **Hypothèse rivale R-pl** : si B dépasse A, ce n'est pas le programme linéaire (les poids d'équilibre) mais le seul fait de tirer au hasard parmi plusieurs moniteurs. Témoin : bras C, mélange **uniforme** de moniteurs entraînés comme ceux de A (sans résolution du jeu).
- **Hypothèses de travail** : (a) l'oracle du défenseur (maximisation du taux de détection lissé au seuil α, plusieurs départs déterministes) est une meilleure réponse approchée, la même pour les quatre bras ; (b) l'oracle de l'attaquant (programmation quadratique séquentielle, SLSQP, sous contrainte, départs tirés) est une meilleure réponse approchée ; son insuffisance est contrôlée par un attaquant final renforcé ; (c) la loi propre est N(0, I) et connue du code, pas des bras, qui ne voient que des échantillons.

## Prédiction chiffrée et signe attendu

Toutes les valeurs ci-dessous viennent du pilote sur la **racine d'essai** (24 instances par δ ; (M), § cités). Elles ne sont pas opposables : la décision se lit sur RACINE, jamais lue.

| # | Quantité | Signe prédit | Ordre de grandeur prédit [source] | Réfutation |
|---|---|---|---|---|
| P1 | Δ(B, A) sur (iii), δ1 = 1,6 et δ2 = 2,4 | **+** aux deux δ | δ1 : +0,12 (pilote +0,1249, IC95 [+0,1085 ; +0,1398]) ; δ2 : +0,04 (pilote +0,0367, IC95 [+0,0344 ; +0,0391]) [M § 2] | borne haute à 95 % < 0 pour un δ (le mélange perd), ou borne haute < S1 aux deux δ |
| P2 | Δ(B, D) sur (iii) | **−** à δ1 ; **≈ 0** à δ2 | δ1 : −0,19 (pilote −0,1862, IC95 [−0,2015 ; −0,1730]) ; δ2 : +0,005 (pilote +0,0048, IC95 [+0,0021 ; +0,0073]) [M § 2] | borne basse à 95 % > 0 à δ1 (le mélange bat la capacité égale) |
| P3 | Δ(B, C) sur (iii) | **≈ 0** aux deux δ | δ1 : −0,008 (pilote −0,0083, IC95 [−0,0202 ; +0,0004]) ; δ2 : 0,000 (pilote −0,0000, IC95 [−0,0032 ; +0,0033]) [M § 2] | IC90 hors de [−S7 ; +S7] dans un δ |
| P4 | Δ(B, A) sur (ii) (non-régression) | **−** aux deux δ | δ1 : −0,06 (pilote −0,0560, IC95 [−0,0852 ; −0,0240]) ; δ2 : −0,06 (pilote −0,0595, IC95 [−0,0887 ; −0,0298]) [M § 2] | borne basse à 95 % ≥ −S5 aux deux δ |
| P5 | Δ(B, A) sur le coût par contournement (fraction de δ) | **+** | δ1 : +0,17 (pilote +0,1706) ; δ2 : +0,30 (pilote +0,3021) ; part censurée (non contourné à δ) : A 0,06 ; B 0,48 ; C 0,50 ; D 0,50 [M § 2, § 6] | borne haute à 95 % < 0 (descriptif) |
| P6 | Nouveauté résiduelle par tour | décroissante dans les quatre bras | du tour 1 (1,000 par définition) au tour 8 : A 0,144 ; B 0,170 ; C 0,084 ; D 0,187 [M § 6] | moyenne au tour 8 ≥ 0,5 dans un bras (descriptif) |
| P7 | (iii) par tour, contre la meilleure réponse du tour | A plat ; B, C, D croissants | tour 1 → tour 8 : A 0,030 → 0,025 ; B 0,030 → 0,100 ; C 0,030 → 0,106 ; D 0,030 → 0,194 [M § 6] | descriptif |

**Verdicts prédits** (sous les valeurs recommandées des seuils) : Table 1 ligne 5 (H1 confirmée) ; Table 2 « régression avérée » (arbitrage (iii) contre (ii)) ; Table 3 « la capacité égale fait au moins aussi bien » (R-cap non exclue, plutôt soutenue) ; Table 4 « équivalence B ≈ C », qui **déclenche l'audit R4** (consigne de Lazar : « si le mélange uniforme égale le mélange d'équilibre, audit »). Confiance de l'auteur dans le signe de P1 aux deux δ : 0,85 ; dans P2 à δ1 : 0,8 ; dans P3 : 0,7 ; dans P4 : 0,75.

Lecture anticipée, à ne pas confondre avec un résultat : si ces prédictions tiennent, le mécanisme « tirer au hasard parmi plusieurs moniteurs » bat le moniteur unique de Bailey dans ce monde, mais ni les poids d'équilibre ni le hasard ne battent un moniteur unique plus riche à paramètres égaux ; ce serait un argument **contre** la piste 3 comme méthode propre, et pour « capacité » comme explication.

## Métrique

Notations : une **tâche** = (δ, instance) ; une instance fixe la loi cible ; les deux δ partagent la loi cible d'une instance (appariement entre δ). Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i (seuil calibré au quantile 1 − α des scores de 20 000 échantillons propres communs aux bras d'une tâche ; α = S9).

- **(iii) principale, V(bras)** : après T tours (S12), défense figée ; l'attaquant calcule deux meilleures réponses (standard : 12 départs tirés + départ « tiré vers l'origine » + les attaques passées du bras, 512 échantillons de Monte-Carlo par composante ; renforcée : 48 départs, 200 itérations, mêmes autres règles), sous la contrainte distance ≤ δ et la boîte ; chaque réponse est évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections** (l'attaque la plus forte trouvée). Unité : proportion dans [0 ; 1].
- **Écart apparié** Δ(X, Y) = moyenne sur les instances de V(X) − V(Y), à δ fixé.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de **RACINE_TENUE** (racine à part), deux sous-familles alternées : déplacement aléatoire dans la boule de comportement (rayon tiré entre 0,5 δ et δ) ; tout le budget sur une composante tirée vers l'origine avec échelles tirées. 3 999 échantillons par loi. Score = moyenne des 50 taux de détection. Rapporté aussi par sous-famille. Courbe par tour : (ii) de la défense déployée à chaque tour.
- **(i) familles vues** : moyenne des taux de détection de la défense finale sur les attaques produites pendant la trajectoire du bras (descriptif).
- **Coût par contournement** (piste 5) : plus petit budget δ' ∈ [0 ; δ] tel que la meilleure réponse (3 départs + attaques passées) contre la défense finale est détectée au plus au seuil de contournement S14 ; bissection en 5 pas ; rapporté en fraction de δ ; **censuré à 1** si non contourné à δ (part censurée rapportée par bras ; l'écart en fraction est alors une borne basse de l'écart vrai).
- **Nouveauté résiduelle** (piste 4) : au tour t, norme du résidu du déplacement θ_t − θ* après projection orthogonale (moindres carrés) sur l'espace engendré par les déplacements des tours 1 à t − 1, divisée par la norme du déplacement (dimension des paramètres : 36 ; T = 8 ≪ 36, la saturation n'est donc pas triviale).
- **Contrôles** : taux de fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants ; valeur du jeu restreint de B ; écart entre attaquant standard et renforcé ; poids finaux de B (support, pureté, égalité à l'uniforme).
- **Intervalles** : rééchantillonnage apparié des instances, 10 000 tirages, percentiles ; IC95 bilatéral (2,5 % et 97,5 %) pour les tests de signe ; IC90 (5 % et 95 %) pour les équivalences (deux tests unilatéraux à 5 %). Graines du rééchantillonnage : `SeedSequence(entropy=RACINE, spawn_key=(code_delta, code_contraste, 0, 0, 99))`.

## Seuil

**Tous les seuils sont à geler par Lazar en une ligne datée de `registres/decisions.md`. Aucun défaut ne s'applique.** Pour chacun : la valeur (marqueur), la recommandation de l'auteur, sa raison, la source.

**S1 — effet minimal d'intérêt sur Δ(B, A) (iii)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **+0,02** (deux fois α).
- Raison : un gain de détection plus petit que deux fois le taux de fausses alertes est négligeable à ce point de fonctionnement ; valeur fixée sur ce principe, non sur le pilote. Puissance de la règle « estimation ≥ S1 et borne basse 95 % > 0 aux deux δ » : effet minimal détectable à 0,8 = 0,03 dès N = 20 ; à N = 100, puissance 0,995 à e = 0,03 et 0,251 à e = 0,02 [M § 3, S1 = 0,02]. Autres options : 0 (signe seul ; effet minimal détectable 0,02 à N = 40 [M § 3, S1 = 0,00]) ; 0,05 (effet minimal détectable 0,06 [M § 3, S1 = 0,05]).

**S2 — erreur de première espèce**
- Valeur : À REMPLIR par Lazar.
- Recommandation : IC95 bilatéral par δ (2,5 % unilatéral), **conjonction exigée aux deux δ** (test intersection-union, sans correction).
- Raison : erreur de première espèce simulée à e = 0, S1 = 0, deux δ exigés : ≤ 0,0013 pour tout N de la grille ; un δ seul : 0,019 à 0,053 [M § 3, « Erreur de première espèce »]. Le rééchantillonnage simulé emploie l'approximation de Student, la décision le percentile : écart déclaré.

**S3 — puissance visée**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,9** à un effet vrai de 0,03 sur (iii), et ≥ 0,95 pour la non-régression (S5) et l'équivalence (S7) sous écart vrai nul.
- Raison : la règle principale est bon marché ; la contrainte vient des contrôles (S5, S7) [M § 4 bis].

**S4 — nombre d'instances N par valeur de δ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **N = 100** (200 tâches).
- Raison : puissance principale 0,995 à e = 0,03 [M § 3] ; non-régression avec S5 = 0,03 sous écart vrai nul : 0,969 [M § 4 bis] ; équivalence B − C avec S7 = 0,01 : 0,954, avec S7 = 0,02 : 1,000 [M § 4 bis] ; temps projeté 79,5 min de processeur, 41,0 min de mur sur 2 cœurs [M § 5]. Autres options : N = 60 (24,6 min de mur ; non-régression 0,764 avec S5 = 0,03) ; N = 150 (61,5 min de mur ; non-régression 0,998).

**S5 — tolérance de non-régression sur (ii), Δ(B, A)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,03**.
- Raison : plus petite tolérance de la grille dont le test a une puissance ≥ 0,95 sous écart vrai nul à N = 100 (S5 = 0,02 : 0,588 ; 0,03 : 0,969 ; 0,05 : 1,000) [M § 4 bis]. Le pilote donne −0,056 et −0,060 [M § 2] : sous S5 = 0,03, la régression serait jugée avérée ; sous S5 = 0,05 et N = 100, la puissance de « sans régression » si l'écart vrai vaut −0,025 est 0,845 [M § 4 bis]. **Choix sensible** : Lazar fixe S5 en sachant que la valeur pilote est autour de −0,06.

**S6 — marge d'équivalence pour Δ(B, D)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (= S1).
- Raison : « équivalents » veut dire « écart plus petit que l'effet minimal d'intérêt » ; demi-largeur de l'IC95 attendue à N = 100 : 0,0071 (δ1), 0,0013 (δ2) [M § 4].

**S7 — marge d'équivalence pour Δ(B, C)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (= S1).
- Raison : même principe ; puissance d'équivalence à N = 100 sous écart nul : 1,000 [M § 4 bis]. Option plus exigeante : 0,01 (0,954).

**S8 — plafond de temps**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **2 h de mur sur 2 cœurs** pour l'exécution de décision (`timeout 7200` externe, deux processus d'un fil chacun), et **600 s de processeur par tâche** (garde interne `plafond_cpu_tache_s`).
- Raison : temps mesuré par tâche : moyenne 23,85 s, médiane 24,20 s, maximum 32,01 s ; N maximal sous 2 h au temps maximal : 218 [M § 5].

**S9 — taux de fausses alertes α et tolérance**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **α = 0,01** ; garde |taux mesuré − α| ≤ 0,005.
- Raison : point de fonctionnement usuel des moniteurs ; fausses alertes finales mesurées au pilote : moyenne 0,0100, min 0,0077, max 0,0132 [M § 6].

**S10 — déclencheur d'audit « trop beau / trop mauvais » sur Δ(B, A) (iii)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **|Δ(B, A)| ≥ 0,25** dans un δ, un seul seuil pour les deux sens ; plus la règle de Lazar : **moyenne de V(B) ≥ 0,99** dans un δ.
- Raison : le pilote donne au plus +0,125 [M § 2] ; un doublement serait suspect.

**S11 — budgets de comportement δ (deux valeurs)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **δ1 = 1,6 et δ2 = 2,4** (0,4 et 0,6 fois la distance cible r = 4), fixés **avant** la première exécution.
- Raison : non choisis sur le pilote. Réserve : à δ2, le bras A est presque entièrement contourné (V(A) = 0,0008 [M § 1]) ; la ligne 3 de la Table 1 (dégénérescence) ne se déclenche pas au pilote (V(B) = 0,0374 > 2α). Option : δ = (1,2 ; 1,6), à choisir **sur le seul critère de non-dégénérescence de A**, non mesurée.

**S12 — nombre de tours T**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **T = 8**.
- Raison : la nouveauté résiduelle décroît de 1,000 à 0,084–0,187 au tour 8 [M § 6] ; T ≪ dimension des paramètres (36) ; temps par tour au plus 0,72 s (D) [M § 5].

**S13 — oracle du défenseur (identique pour les quatre bras)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **« détection »** (maximisation du taux de détection lissé au seuil α ; départs : solution logistique, puis directions des moyennes de composantes des lois d'entraînement).
- Raison : le double oracle exige une meilleure réponse au gain « détection à α » ; la régression logistique moyenne les composantes et n'en est pas une (écart de conception déclaré ci-dessous). Option : « logistique » (variante du code, plus proche de l'entraînement des sondes chez Bailey et collègues) ; sur une instance d'essai, elle rendait B identique à A (§ « Écarts »).

**S14 — seuil de contournement pour le coût par contournement**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,10** (dix fois α).
- Raison : un moniteur linéaire dédié à une composante plafonne vers un tiers de détection sur une loi à trois composantes ; avec un seuil de 0,5, le contournement devenait gratuit (§ « Écarts ») ; parts censurées au pilote avec 0,10 : A 0,06 ; B 0,48 ; C 0,50 ; D 0,50 [M § 6].

**Paramètres du monde (gelés avec la configuration, empreinte `6685585f…` ci-dessus)** : d = 6 ; K = 3 ; r = 4 ; écart-type cible 1 ; boîte |μ| ≤ 5, écarts-types dans [0,5 ; 1,5] ; 2 000 échantillons propres et 2 001 d'attaque par entraînement ; 4 départs de meilleure réponse par tour, 100 itérations ; 256 échantillons de Monte-Carlo par composante (512 au final) ; température 0,25 ; 8 départs d'entraînement ; 300 itérations L-BFGS-B ; garde de non-convergence 5 %.

## Plan d'analyse

### 1. Monde
Loi propre N(0, I_6). Loi cible d'une instance : 3 composantes, moyennes de norme r = 4 dans des directions tirées (graine de l'instance), écarts-types 1. Loi d'attaque : 3 composantes appariées aux composantes cibles, moyennes et écarts-types diagonaux dans la boîte. **Contrainte de comportement** : distance = racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées (pour des gaussiennes diagonales : ‖μ_k − μ*_k‖² + ‖σ_k − σ*_k‖²) ≤ δ. C'est une borne haute de la distance de Wasserstein entre mélanges ; choisie parce qu'elle est exacte, lisse et lisible.

### 2. Bras (une trajectoire coévolutive par bras et par tâche)
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (graine commune ; reproductibilité bit à bit vérifiée par garde). Puis, pour t = 1 … T : l'attaquant calcule une meilleure réponse contre la défense déployée ; le défenseur se met à jour.
- **A** : déploie le dernier moniteur ; met à jour par un moniteur linéaire entraîné contre le mélange uniforme de toutes les attaques passées (loi cible comprise).
- **B** : matrice de gains G (moniteur i × attaque j, taux évalués sur des échantillons fixés par attaque) ; déploie p = stratégie d'équilibre du défenseur (programme linéaire, HiGHS) ; après la nouvelle attaque, q = stratégie d'équilibre de l'attaquant sur la matrice élargie ; nouveau moniteur linéaire entraîné contre le mélange q ; ligne ajoutée.
- **C** : moniteurs entraînés comme A ; déploie le mélange uniforme de tous ses moniteurs.
- **D** : déploie un seul moniteur maxout à t unités au tour t (T + 1 unités à la fin, autant que le mélange final de B : vérifié par essai) ; entraîné contre le mélange uniforme de ses attaques passées.
Défense finale : après la mise à jour du tour T. L'attaquant joue en dernier (§ Métrique).

### 3. Graines (R9)
- **RACINE = 20261201** (décision), **RACINE_TENUE = 20261202** (familles tenues à l'écart de la décision) ; RACINE_ESSAI = 20261291 et RACINE_ESSAI_TENUE = 20261292 (plomberie et puissance, seules lues). Quatre entiers fixés avant toute exécution, sans lien avec un résultat ; aucune autre racine permise en décision.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25. Codes de bras : commun 0, A 1, B 2, C 3, D 4. Rôles : loi cible 0 ; propre d'entraînement 1 (commun aux bras : nombres aléatoires communs) ; attaques d'entraînement 2 ; calibration 3 (commune) ; fausses alertes 4 (commune) ; Monte-Carlo de l'attaquant 5 ; départs de l'attaquant 6 ; évaluation 7 ; initialisation du maxout 8 ; lois tenues 9 et leurs échantillons 10 (racine tenue) ; final 11 (sous-clés 1 à 6) ; coût 12 ; rééchantillonnage 99.
- Manifeste par run (`src/controle_ia/manifeste.py`, `creer_manifeste(decisif=True, prereg=…)`) : configuration et empreinte, versions de Python, numpy, scipy, empreinte du code, racines, commit.

### 4. Comparaisons et multiplicité
- Décisive : Δ(B, A) sur (iii), aux deux δ (intersection-union, S2).
- Qualifiantes (lues seulement si H1 n'est pas réfutée) : Δ(B, A) sur (ii) contre −S5 ; Δ(B, D) sur (iii) avec la marge S6 ; Δ(B, C) sur (iii) avec la marge S7. Elles qualifient la lecture et ne sont pas corrigées pour la multiplicité (déclaré) ; chacune est lue aux deux δ.
- Descriptives : coût par contournement, nouveauté résiduelle, (i), courbes par tour de (ii) et (iii), Δ(C, A), Δ(D, A), Δ(B, D) sur (ii), sous-familles de (ii).

### 5. Ordre d'exécution
(1) Essais du code (`python3 -m pytest -q …/essais`) ; (2) une seule invocation `arene_melange_v1.py decision --prereg prereg/<nom>.md --instances 0:N --run-id <AAAAMMJJ-HHMMSS-arene-melange-v1>` sous `timeout` (S8), arbre git propre ; (3) analyse écrite par le même processus (`analyse-arene.json`, scellé par `ecrire_resultat`) ; (4) lecture par un sous-agent neuf (R13), qui applique les tables ci-dessous.

### 6. Écarts de conception faits sur la racine d'essai (avant toute décision, déclarés)
1. Oracle du défenseur : sur une instance d'essai (instance 0, δ1), l'oracle logistique donnait des poids d'équilibre purs (un seul moniteur) et B ≈ A (0,070 contre 0,069) ; remplacé, **pour les quatre bras à l'identique**, par l'oracle « détection » (S13). Raison de principe : le double oracle suppose une meilleure réponse au gain mesuré. Ce changement a été fait après avoir vu ce résultat d'essai : réserve R3/R4 déclarée ; la contre-lecture doit le juger.
2. Seuil de contournement : 0,5 → 0,10 (S14), parce que le contournement devenait gratuit (fraction de δ proche de 0 pour B sur la même instance).
3. Attaquant final renforcé ajouté (contrôle de l'optimiseur) ; au pilote v2, écart standard − renforcé : moyenne au plus 0,0005 en valeur absolue, maximum 0,0093, et Δ(B, A) inchangé (+0,1252 contre +0,1253 ; +0,0371 contre +0,0371) [M § 6].
4. Projections après SLSQP comptées au-delà de 10⁻⁶ seulement (8 978 au pilote v1 avec 10⁻⁹, toutes de l'ordre de la tolérance numérique ; 23 au pilote v2) [M § 6].
5. Garde d'empreinte du code dans `exiger_identite_prereg`, ajoutée après le pilote v2 (aucun changement de calcul ; configuration inchangée).
Le pilote v1 (`essai-pilote-racine-essai-v1.json`, `f34e33d7…`) est conservé, non utilisé pour la puissance (l'attaquant renforcé n'y était pas).

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites. Chaque table se lit **de haut en bas ; la première ligne vraie décide** ; la dernière est le complémentaire. Notation : pour un contraste à δ fixé, est = moyenne, lb95 / ub95 = bornes de l'IC95, IC90 = intervalle à 90 %.

**V0** = aucune condition de la liste d'arrêt ∧ nombre de tâches exécutées = 2 × N (S4) ∧ racines du manifeste = RACINE et RACINE_TENUE ∧ empreintes du code et de la configuration = celles du texte scellé ∧ toutes les gardes de fausses alertes passées.

**Déclencheurs d'audit (R4), un seul seuil pour les deux sens** :
- moyenne de V(B) ≥ 0,99 dans un δ (règle de Lazar) ;
- |est Δ(B, A)| ≥ S10 dans un δ ;
- **B ≈ C** : IC90 de Δ(B, C) ⊂ [−S7 ; +S7] aux deux δ (règle de Lazar : le mélange uniforme égale le mélange d'équilibre) ; ou V(B) = V(C) au bit près sur une tâche ; ou poids finaux de B égaux à l'uniforme (à 10⁻⁶) sur une tâche où B a au moins 2 moniteurs ;
- poids finaux de B purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ (mélange dégénéré) ;
- contrôle de l'optimiseur : moyenne de (V standard − V renforcé) > 0,01 pour un bras dans un δ, ou Δ(B, A) qui diffère de plus de 0,01 entre attaquant standard et renforcé ;
- moyenne de (valeur du jeu restreint de B − V(B)) < −0,01 dans un δ (l'attaquant final ferait moins bien que les attaques déjà connues) ;
- V(D) = V(A) au bit près sur toutes les tâches d'un δ (capacité non exercée).

**Contenu de l'audit** : relecture du code par un sous-agent neuf ; rejeu de 10 tâches sur **RACINE_ESSAI** avec un attaquant quatre fois plus fort (départs et itérations) ; vérification que B déploie bien les poids du programme linéaire et C l'uniforme ; journal des poids. **Issue** : « artefact trouvé » si et seulement si le rapport scellé constate une erreur de code, un chemin non exercé, ou un contraste décisif ou qualifiant qui change de plus de 0,01 sous l'attaquant renforcé ; sinon « pas d'artefact ».

### Table 1 — H1 sur (iii), Δ(B, A)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant** (audit en attente) |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle du préenregistrement |
| 3 | dans un δ, la moyenne de V est ≤ 2α pour les quatre bras | **non concluant** : jeu dégénéré (tout est contourné) |
| 4 | ub95 Δ(B, A) < 0 dans au moins un δ | **le mélange perd** : H1 réfutée (signe contraire) |
| 5 | est ≥ S1 ∧ lb95 > 0, aux deux δ | **H1 confirmée** |
| 6 | lb95 > 0 aux deux δ (et est < S1 dans un δ) | **effet positif sous le seuil d'intérêt** : H0 rejetée, H1 non confirmée |
| 7 | ub95 < S1 aux deux δ | **H1 réfutée à l'effet minimal** (pas d'effet d'intérêt) |
| 8 | est ≥ S1 ∧ lb95 > 0 dans exactement un δ | **H1 confirmée pour un budget seulement** : dépend de δ |
| 9 | sinon | **non concluant** (imprécis) |

Les Tables 2 à 4 se lisent seulement si la Table 1 rend la ligne 5, 6 ou 8.

### Table 2 — non-régression sur (ii), Δ(B, A)

| # | Condition | Lecture |
|---|---|---|
| 1 | lb95 ≥ −S5 aux deux δ | **sans régression** sur les familles tenues à l'écart |
| 2 | ub95 < −S5 dans au moins un δ | **régression avérée** : le gain sur l'attaquant adaptatif se paie sur les familles tenues à l'écart (arbitrage, pas un gain net) |
| 3 | sinon | **régression non exclue** |

### Table 3 — hypothèse rivale « capacité », Δ(B, D) sur (iii)

Classement par δ, dans cet ordre : « ≈ » si IC90 ⊂ [−S6 ; +S6] ; sinon « B > D » si lb95 > 0 ; sinon « D > B » si ub95 < 0 ; sinon « ? ».

| # | Condition | Lecture |
|---|---|---|
| 1 | « ? » dans un δ | **rivale non tranchée** |
| 2 | « B > D » dans un δ et « D > B » dans l'autre | **dépend de δ** |
| 3 | « D > B » dans au moins un δ (l'autre « D > B » ou « ≈ ») | **la capacité égale fait au moins aussi bien** : le gain du mélange sur A ne lui est pas propre (R-cap soutenue) |
| 4 | « B > D » dans au moins un δ (l'autre « B > D » ou « ≈ ») | **le mélange va au-delà de la capacité** (R-cap écartée) |
| 5 | « ≈ » aux deux δ | **mélange et capacité égale équivalents** à S6 près |

### Table 4 — rôle du programme linéaire, Δ(B, C) sur (iii)

Même classement avec S7 (« ≈ », « B > C », « C > B », « ? »).

| # | Condition | Lecture |
|---|---|---|
| 1 | « ? » dans un δ | **non tranché** |
| 2 | « B > C » dans un δ et « C > B » dans l'autre | **dépend de δ** |
| 3 | « C > B » dans au moins un δ (l'autre « C > B » ou « ≈ ») | **l'uniforme fait au moins aussi bien que l'équilibre** |
| 4 | « B > C » dans au moins un δ (l'autre « B > C » ou « ≈ ») | **les poids d'équilibre apportent** au-delà du hasard uniforme |
| 5 | « ≈ » aux deux δ | **équivalence** : le programme linéaire n'apporte rien à S7 près ; **déclencheur d'audit** ; lecture valable seulement après un audit rendu « pas d'artefact » |

**Phrase de synthèse** (à écrire par le lecteur R13, en recopiant les lectures) : « Table 1 : … ; Table 2 : … ; Table 3 : … ; Table 4 : … ». Les mesures descriptives (coût, nouveauté résiduelle, courbes) sont rapportées avec leur IC, sans verdict.

## Liste d'arrêt

| Condition | Action | Garde et essai (R5 : cas sain et artefact) |
|---|---|---|
| Lancement en décision sans préenregistrement scellé, conforme, portant l'identifiant, les racines et les empreintes du code et de la configuration | pas de départ ; aucune graine de décision tirée | `exiger_prereg_arene` ; essais `test_decision_refusee_sans_prereg_scelle` (brouillon non scellé), `test_decision_refusee_prereg_scelle_d_une_autre_experience` (scellé d'une autre expérience ; la partie scellement passe sur un vrai scellé), `test_identite_prereg_sain_et_artefacts` |
| Racine de décision employée en essai, ou racine des tenues égale à la racine principale | arrêt | `exiger_racines_essai` ; `test_racines_essai_sain`, `test_racines_essai_artefact`, `test_cli_essai_refuse_racine_de_decision` |
| Fichier de sortie existant (essai) ou dossier de run existant (décision) | arrêt (R12) | `test_cli_essai_refuse_d_ecraser` ; `creer_manifeste` (essais du dépôt `tests/test_manifeste.py`) |
| Arbre git non propre au lancement de décision | arrêt | `creer_manifeste` (essais du dépôt) |
| Programme linéaire non résolu, ou valeurs primale et duale différentes de plus de 10⁻⁷ | arrêt | `resoudre_jeu` ; `test_jeu_sain`, `test_jeu_artefact` |
| Matrice de gains non finie, hors [0 ; 1], ou non bidimensionnelle | arrêt | `test_jeu_artefact` |
| Poids de mélange négatifs, non finis, ou de somme ≠ 1 | arrêt | `exiger_poids` ; `test_poids_sain_et_artefact` |
| Loi d'attaque hors de la boîte ou à distance > δ après projection | arrêt | `exiger_admissible` ; `test_admissibilite_sain_et_artefact` |
| Nombre d'échantillons non multiple de K | arrêt | `test_echantillonnage_stratifie` |
| Paramètres ou scores de moniteur non finis ; moniteur non calibré ; score propre de variance nulle | arrêt | `test_moniteur_gardes` |
| Taux de fausses alertes d'une défense finale hors de α ± 0,005 (S9) | arrêt | `exiger_fpr` ; `test_garde_fausses_alertes_sain_et_artefact` |
| Part d'entraînements non convergés > 5 % dans une tâche | arrêt | `exiger_convergence` ; `test_garde_convergence_et_identite_tour0` (et déclenchement réel observé en essai avec 60 itérations) |
| Moniteur du tour 0 non reproductible bit à bit | arrêt | `exiger_meme_moniteur` ; `test_garde_convergence_et_identite_tour0` |
| Temps processeur d'une tâche > 600 s (S8) | arrêt | `test_plafond_de_temps_processeur` |
| Temps de mur total > S8 | arrêt par `timeout` externe, consigné ; **contrôle externe non couvert par les essais du code** | — |
| Aucun départ de l'attaquant ne rend de point fini | arrêt | garde dans `meilleure_reponse` (non provoquée par un essai : réserve) |
| Reproductibilité : deux exécutions d'une même tâche diffèrent hors temps mesurés | arrêt | `test_reproductibilite_bit_a_bit` |
| Nombre de tâches exécutées ≠ 2 × N ; exécution en plusieurs invocations ; paramètre changé après une lecture | V0 fausse ; non concluant | contrôle du lecteur R13 (manifeste unique, horodatage) |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| numpy < 1.25 | arrêt (R9) | `exiger_numpy_minimal` (essais du dépôt) |
| Marqueur de gel restant, ou contre-lecture sans ses deux empreintes | pas de scellement | validateur `problemes` ; `test_brouillon_non_conforme_au_validateur` |
| Ligne de gel absente de `registres/decisions.md`, ou valeurs différentes du texte ; remarques de contre-lecture non traitées | pas de scellement ; **contrôle manuel** (le validateur ne le vérifie pas) | — |

## Rôles

- Auteur : sous-agent neuf Opus 5.5 (lignée conv-audit), auteur du code et de ce brouillon.
- Contre-lecteur (R2) : un sous-agent neuf **d'un autre modèle** (Fable 5.1 ou Sonnet 5.5), qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `arene_melange_v1.py`, `essais/test_arene_melange_v1.py`, `calcul-puissance-arene-melange-v1.py` et sa sortie, `LISEZMOI-arene-melange-v1.md`, le brainstorm et la fusion v3 de P-041. Points à juger en priorité : l'écart de conception n° 1 (oracle changé après une observation d'essai) ; la définition de D comme « capacité égale » ; la sensibilité du verdict à S5.
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni contre-lecteur ni analyste ; applique les Tables 1 à 4 ; son verdict est scellé puis soumis à Lazar.
- Lazar : gèle S1 à S14 ; donne le GO de l'exécution de décision (processeur, aucune dépense).

## Contre-lecture

À REMPLIR — contre-lecteur d'un autre modèle (identifiant), empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
