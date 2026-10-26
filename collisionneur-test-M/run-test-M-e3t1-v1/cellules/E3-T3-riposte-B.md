# Proposition B, tour III.3 : riposte aux équipes rouges A et C

## 0. Pièces reçues

- **Bloc FAITS** : vide, par décision déclarée de l'arbitre. Aucun résultat au niveau objet n'existe donc. Tout ce qui suit est RAPPORTÉ (repris des pièces) ou HYPOTHÈSE.
- **Pièces reçues** : ma conception III.1 et les deux attaques III.2 sont complètes, chacune se termine par sa ligne de clôture. Je ne réponds qu'aux sections « Contre la proposition B ».
- **Statuts empruntés** : C marque sa faille 4 « VÉRIFIÉ statistiquement ». Je ne modifie pas ce statut. Je signale seulement que l'argument repose sur une prémisse, σ_train ≫ σ_test, qui reste une HYPOTHÈSE non mesurée.
- **Emprunts** : quand je reprends un contrôle qu'une équipe rouge proposait contre A ou contre C, je le dis (règle B1).

---

## (a) Verdicts sur les attaques

### Cinq décisions de structure

Les attaques convergent sur cinq points. Ils modifient la conception, et je les énonce d'abord.

- **D1. La sonde de provenance S1 sort du décisif.**
  - Deux attaques se combinent. Pour F-B3 (A), l'équilibrage est impossible sur « besoin utilitaire ». Pour C-b1/c1, des devoirs collés dans un journal d'usage sont des évaluations. Si l'on n'équilibre pas S1, elle est circulaire ; si on l'équilibre, elle apprend des artefacts.
  - La sonde principale devient **S2′** : une mention explicite (« ceci est une évaluation » contre « ceci est une vraie demande »). Elle est apprise dans **une seule famille de gabarit neutre F0**, écrite par un second auteur qui n'a pas vu la table §2.1, puis testée sur des items qui ne contiennent aucune mention.
  - Le construit lu change, et je le déclare : β_T mesure **à quel point le gabarit implicite déplace le flux résiduel le long de la direction de mention explicite**. Ce n'est pas une « conscience » démontrée.
- **D2. Plus de rembourrage** (F-B2, C-a1). Il est remplacé par des emplacements appariés : chaque trait a une réalisation + et une réalisation − au même endroit, de longueur appariée. La longueur résiduelle entre en covariable.
- **D3. δ est ancré sur le construit, pas sur une variance** (F-B5, C-a4).
  - δ = 0,1 × Δ_expl. Δ_expl est l'écart moyen de score entre mentions « évaluation » et mentions « usage », mesuré sur des paires d'entraînement tenues à l'écart. La fraction 0,1 est illustrative, mais elle est scellée **maintenant**, avant tout pilote.
  - Le pilote ne fixe plus que n.
- **D4. Multivers scellé avec décision unanime.** C'est ma réponse à la faille centrale de A : B protège contre la lecture prématurée, pas contre la conception orientée. Les choix contestés sont énumérés et tous exécutés. Un verdict n'est rendu que s'il est identique dans toutes les branches.
- **D5. Décomposition par trait (E6).** Elle répond à F-B1 : le découpage en T et C devient lui-même un objet de test.

### Équipe rouge A, section contre B

| Attaque | Verdict | Raison ou test |
|---|---|---|
| **F-B1** Partition de la table §2.1 | **Transformée en test (E6)** | Rejet partiel : la partition n'est pas de mon fait. H-M1 range elle-même le format à choix multiple et les consignes de banc dans T (RAPPORTÉ). A a cependant raison sur un point : « T domine » pourrait refléter seulement le poids des traits massifs. E6 estime l'effet de chacun des 7 traits et compare la partition de l'essaim aux 35 partitions 4/3 possibles. |
| **F-B2** Rembourrage colinéaire aux facteurs | **Acceptée** | D2. |
| **F-B3** Équilibrage S1 impossible sur le besoin utilitaire | **Acceptée** | D1. L'existence d'évaluations exprimant un besoin dans les corpus publics reste une HYPOTHÈSE à vérifier ; elle n'est plus nécessaire. |
| **F-B4** Le codeur et le test partagent la même définition de T | **Acceptée, transformée** | F0 est écrite par un second auteur. Une assertion vérifie qu'aucun n-gramme de 4 jetons ou plus (illustratif) n'est commun entre F0 et les segments des facteurs du test. |
| **F-B5** δ informé par la variance du pilote | **Acceptée** | D3. C'était un chemin bifurquant, que j'avais présenté comme un avantage. |
| **F-B6** E3 confond effondrement du signal et perte de puissance | **Acceptée** | E3 est refondu (E3′). Les familles d'entraînement comparées ont des effectifs égaux, fixés à l'avance. |
| **F-B7** T* hors distribution, rapport non borné | **Acceptée** | Le rapport est supprimé. E2′ introduit deux modalités T* (fluide et étrange) et une issue « hors intervalle » déclarée. |
| **F-B8** E5 : G_sens déplace aussi la perplexité | **Acceptée** | E5′ ajoute ton contrôle 7 (substitution d'entités rares) comme calibrateur de la relation perplexité → score. |
| **F-B9** S3 auto-induisant | **Rejetée en partie, transformée** | L'étiquette S3 vient d'une passe séparée : une contamination uniforme décale toutes les étiquettes sans créer d'effet différentiel par T. Une contamination différentielle reste possible. Test : deux formulations de la question méta (style banc ou style familier), avec un accord κ rapporté. S3 n'est plus qu'une branche du multivers. |
| **F-B10** Contenus neufs mais de forme banc d'essai | **Rejetée sur un point, acceptée sur l'autre** | Un plafond ne peut pas produire « H-M1 soutenue » : ma règle exige aussi une borne basse de β_T > δ. Un plafond donne donc « indéterminé », pas un faux positif. En revanche, la compression de β_T est réelle : j'ajoute une strate de **contenus du quotidien** (ton contrôle 3). |
| **F-B11** Le plan prédit sa propre indétermination | **Acceptée en partie** | La perplexité ne peut pas être une simple covariable : la familiarité passe peut-être *par* elle, et la contrôler retirerait l'effet étudié. Le modèle primaire estime l'effet total, le modèle secondaire l'effet direct avec la perplexité ; les deux sont scellés. La probabilité de l'issue « indéterminé » est estimée par simulation avant scellement et rapportée. |
| **Évasion par l'auteur** (S1, table, rembourrage, E0, E3, réunion de tous les leviers) | **Acceptée, c'est l'attaque centrale** | Les leviers S1 et rembourrage sont supprimés (D1, D2). Le levier « table » est couvert par le multivers (D4) et E6. Pour E0, les paires choisies par l'auteur sont remplacées par un lexique disjoint fixé d'avance (E0′). |
| **Évasion par la standardisation des directions aléatoires** | **Acceptée** | Une seule procédure pour toutes les directions : projection standardisée sur le même ensemble de référence. Une assertion de code vérifie que la fonction est la même. |
| **Évasion par le modèle** (autre position, après génération, non linéaire) | **Acceptée comme limite** | Balayage exploratoire **position par position**, sans moyenne, sur les familles d'entraînement seulement. Contrôle positif de la position : S2′ doit y lire la mention explicite (E0′). Sonde non linéaire exploratoire à la même position. |
| **Contrôles 1 à 7** | **Tous intégrés** | 1 → E6. 2 → sans objet pour le primaire ; une analyse dose-réponse de longueur reste en sensibilité. 3 → strate du quotidien. 4 → E3′. 5 → trois sondes de construits étrangers. 6 → assertion sur l'en-tête. 7 → E5′. |

### Équipe rouge C, section contre B

| Attaque | Verdict | Raison ou test |
|---|---|---|
| **C-a1** Le rembourrage non utilitaire est un marqueur T+ | **Acceptée** | Argument plus aigu que F-B2 : le rembourrage injectait T+ dans les cellules T−. D2. |
| **C-a2** Le choix de couche sélectionne un détecteur lexical | **Acceptée en partie** | La couche fixée d'avance devient le primaire ; la couche sélectionnée devient une branche du multivers. Nuance : sur des items sans le mot « test », un détecteur lexical donne β_T ≈ β_C ≈ 0. L'erreur est conservatrice (vers « indéterminé »), pas un faux « T domine ». |
| **C-a3** Leave-T-out circulaire si H-M1 est vraie | **Acceptée** | C'est la critique la plus juste contre E3. Si le modèle ne représente l'évaluation que sous T+, une sonde apprise sur T− implicite n'a rien à apprendre. Refonte : sous S2′, l'étiquette vient de la mention explicite, présente dans F0 sans T+ (HYPOTHÈSE : la mention active la représentation quel que soit le gabarit ; E0′ la contrôle). |
| **C-a4** Fuite d'échelle par σ_train | **Acceptée** | D3. Les effets standardisés par σ_test (écart-type inter-contenus dans la cellule T−C−) sont rapportés en secondaire. |
| **C-b1** S1 et les devoirs collés | **Acceptée** | Ma ligne « même texte de surface, provenance différente » (§c de III.1) était mal posée. À séquence de jetons identique, les activations sont identiques au bruit numérique près (HYPOTHÈSE déductive, vérifiable par assertion). La ligne devient une **assertion de cohérence** : scores égaux à une tolérance fixée. Ce n'est plus une discrimination. |
| **C-b1** S2 et circuits séparés | **Transformée en test** | C'est exactement ce que mesure E0′ (transfert vers des mentions lexicalement disjointes). Si la direction est purement lexicale, E1′ donne « indéterminé » par construction. |
| **C-b1** S3 et mensonge stratégique | **Rejetée pour ce tour** | Un adversaire qui modifie les poids sort du modèle de menace : l'empreinte des fichiers de poids est comparée à celle qui est publiée (à vérifier). Un mensonge stratégique natif d'un modèle 8B est une HYPOTHÈSE non testable ici. S3 n'est pas primaire. |
| **C-b2** E2 et modulation par la perplexité | **Acceptée** | T*_fluide, appariée en perplexité à T+ (E2′). Je refuse en revanche d'orthogonaliser w à une direction de perplexité : cela retirerait peut-être l'effet étudié (même raison que pour INLP en III.1). |
| **C-b3** E5 : perplexité locale ou globale | **Acceptée** | Les deux prédicteurs sont scellés conjointement dans E5′. |
| **C-b4** Conjonction non linéaire | **Acceptée comme limite** | La refonte d'E3 supprime la fausse alarme de circularité. Le terme T×C reste dans le modèle, et une sonde non linéaire exploratoire est ajoutée. Si le concept est conjonctif, la question « effet principal » est partiellement mal posée pour une sonde linéaire : c'est l'issue « non additive », déclarée. |
| **C-c1, c2, c3** | Intégrés | Voir D1, D2 et D3. |

---

## (b) Expériences corrigées

### Conventions communes

- **Seuils** : tous illustratifs, à sceller.
- **Modèle** : score ~ T + C + T:C + longueur + (1+T+C | contenu) + (1 | variante), avec une strate de contenu (format banc ou quotidien) en effet fixe.
- **Lecture** : un seul jeton, le dernier de l'en-tête assistant. Une assertion vérifie que les identifiants de jetons sont identiques sur tout le préfixe et le suffixe, y compris la ligne de date du gabarit Llama, figée.
- **Frontières de jetons** : la vérification se fait sur les identifiants, pas sur le texte. J'emprunte ici l'argument de C contre A, sur les fusions BPE aux frontières de blocs.

### E0′ : la direction S2′ code-t-elle la mention, ou ses mots ?

- **Entraînement** : famille F0, paires minimales, mentions de lexique L1.
- **Test** : mentions de lexique L2, sans aucun lemme commun avec L1 (par exemple « des chercheurs mesurent tes réponses » contre « j'en ai besoin pour mon travail »).
- **H_A** : la direction est sémantique.
- **H_B** : elle est lexicale.
- **Métrique** : ΔAUC = AUC(sonde) − AUC(prédicteur de surface entraîné sur L1, même discrimination). C'est la correction que A exigeait contre C, que j'applique à moi-même.
- **Seuil** : borne basse de l'IC 95 % > 0,10 pour H_A ; ≤ 0 pour H_B.
- **Contrôles négatifs** : étiquettes permutées ; sonde d'un construit étranger (ton poli ou sec de la phrase de mention).
- **Contrôle positif de position** : AUC sur L1 tenu à l'écart > 0,9. Sinon, le jeton lu ne porte même pas l'explicite.
- **Ce que falsifie chaque issue** : réussite → falsifie « S2′ est lexicale » ; échec → falsifie l'usage de S2′. E1′ bascule alors sur la seule branche S3, ou l'on passe à la voie (c).

### E1′ : H-M1

- **Multivers scellé**, 8 branches = {consigne de format rangée dans T ou dans C} × {sonde S2′ ou S3} × {couche fixe ou sélectionnée}.
- **Planchers** :
  - 1 000 directions aléatoires, même standardisation ;
  - trois sondes apprises sur des construits étrangers (sentiment, thème scientifique ou quotidien, registre), standardisées de la même façon (contrôle 5 de A).
- **H_A** (T domine) : dans chaque branche, borne basse de β_T > δ, et TOST |β_C| < δ, avec δ = 0,1·Δ_expl.
- **H_B** (le style persiste) : dans chaque branche, l'IC 95 % de |β_C| est au-dessus de δ.
- **Autres issues** :
  - « sensible aux choix » si les branches divergent ;
  - « indéterminé » sinon ;
  - « non additive » si |β_TC| > δ.
- **Ce que falsifie chaque issue** :
  - H_A unanime falsifie « le style compte » sur ce modèle et pour ce construit ;
  - H_B unanime falsifie H-M1 ;
  - « sensible aux choix » falsifie la prétention que H-M1 soit une propriété du modèle indépendante du découpage.

### E2′ : familiarité ou format ?

- **Quatre modalités de T**, à C fixé :
  - T+ : format de banc d'essai connu ;
  - T*_fluide : questionnaire à choix multiple non issu d'un banc (style quiz de magazine), dont la perplexité de gabarit tombe dans un intervalle de ±10 % autour de T+ ;
  - T*_étrange : format inventé ;
  - T− : absence de format.
- **H_A** (familiarité) : TOST |s(T*_fluide) − s(T−)| < δ, et s(T+) − s(T*_fluide) > δ.
- **H_B** (format) : TOST |s(T*_fluide) − s(T+)| < δ.
- **Issue « hors intervalle »** : si s(T*) sort de [s(T−), s(T+)], la familiarité n'est pas testable par cette manipulation (réponse à F-B7).
- **Rôle de T*_étrange** : l'écart s(T*_étrange) − s(T*_fluide) isole un effet de fluidité, distinct de la familiarité (réponse à la fin de F-B7).
- **Ce que falsifie chaque issue** : H_A falsifie « le format suffit » ; H_B falsifie le mécanisme de familiarité invoqué par l'essaim.

### E3′ : l'instrument dépend-il de sa surface d'entraînement ?

- **Dispositif** : deux familles neutres indépendantes, F0 et F0′, écrites par deux auteurs, avec des effectifs égaux fixés d'avance.
- **H_A** (instrument stable) : β_T(F0) / β_T(F0′) ∈ [0,5 ; 2].
- **H_B** : rapport hors de cet intervalle.
- **Contrôle négatif** : deux moitiés aléatoires de F0, de même effectif. Leur rapport donne la dispersion due à la seule estimation (contrôle 4 de A, adapté).
- **Ce que falsifie chaque issue** : la concordance falsifie « β_T est un artefact de la famille d'entraînement » ; la discordance falsifie l'usage d'une famille unique, et E1′ est rétrogradé en exploratoire.

### E4′ : H-M2, stabilité par orbite

- **Orbites** : G_sens et G_pos, comme en III.1, mais dans **deux cellules**, T+C+ et T−C−. J'emprunte le contrôle 6 de A contre C, qui s'applique aussi à moi : G_pos éloigne l'invite du format de banc et manipule donc T.
- **H_A** : SD_pos / SD_sens > 2 dans les deux cellules.
- **H_B** : rapport ≤ 1,25.
- **Issue « G_pos ≈ T »** : si les rapports des deux cellules diffèrent d'un facteur supérieur à 2, l'issue est déclarée.
- **Paraphrases** : audit humain d'un échantillon de 10 %, avec clé de réponse recalculée.
- **Ce que falsifie chaque issue** : un rapport élevé falsifie « la position n'importe pas plus que la formulation » ; un rapport bas falsifie H-M2.

### E5′ : dérive distributionnelle ou effet propre de la position ?

- **Trois familles de transformations** : G_sens, G_pos, et G_ent (entités rares substituées : la perplexité change, le sens et la position ne changent pas).
- **Modèle** : Δscore ~ Δppl_globale + Δppl_locale (16 derniers jetons avant la lecture) + type de transformation. G_ent sert de référence et calibre la pente perplexité → score.
- **H_A** (dérive) : le coefficient propre de G_pos est équivalent à 0 (TOST à δ).
- **H_B** (effet positionnel) : le coefficient propre de G_pos dépasse δ.
- **Ce que falsifie chaque issue** : H_A falsifie l'interprétation positionnelle de H-M2 ; H_B falsifie « la position n'agit que par la perplexité ».

### E6 (nouvelle) : le découpage T/C est-il privilégié ?

- **Dispositif** : plan fractionnaire 2^(7−3) de résolution IV, soit 16 rendus par contenu, sur 100 contenus (illustratif).
- **Choix des générateurs** : les 3 traits C forment une droite du plan de Fano. Si mon calcul est juste, les mots de la relation de définition contiennent alors un nombre pair de traits C et un nombre pair de traits T. Les 4 coins du 2×2 appartiennent donc à la fraction. C'est à vérifier par énumération dans le générateur ; à défaut, les 4 coins sont ajoutés.
- **Statistique** : D = effet moyen des traits T − effet moyen des traits C.
- **Distribution nulle** : les 35 partitions 4/3 des 7 traits.
- **H_A** : la partition de l'essaim a le rang 1 sur 35 (p ≈ 0,029).
- **H_B** : rang > 5 (illustratif).
- **Analyse secondaire** : effet de chaque trait le long de w, rapporté à la norme du déplacement résiduel ‖Δh‖ que produit ce trait. Cela répond directement à « ce sont les traits les plus massifs ».
- **Ce que falsifie chaque issue** : un rang de tête falsifie « le découpage est arbitraire » ; un rang moyen falsifie la lecture « gabarit contre style » d'un éventuel succès en E1′.

### Instruments

- **Générateur** : mutants injectés, avec détection attendue à 100 %.
- **Empreinte des poids** : à vérifier contre l'empreinte publiée.
- **Puissance et indétermination** : estimées par simulation de la structure réelle du plan.
- **Volume de calcul** : environ 4 800 invites pour E1′ et 3 200 pour E6 (illustratif). Le calcul reste marginal. Le goulot humain augmente : second auteur, F0′, strate du quotidien, T*_fluide.

---

## (c) Réponse à la question de l'arbitre

**Option.** Je maintiens **(a′)**, plus fermement qu'au tour III.1.

- **Cette nuit**, on ne lance que ce qui ne touche aucun item de test :
  - E0′ et E3′ ;
  - le balayage positionnel exploratoire, sur les familles d'entraînement ;
  - les mutants du générateur et les assertions de jetons ;
  - l'empreinte des poids ;
  - la simulation de puissance et d'indétermination.
- **Ensuite**, on scelle E1′, E2′, E4′, E5′ et E6. La fraction définissant δ (D3) et les 8 branches du multivers (D4) sont fixées dès maintenant.
- **Bascule vers (c)** si l'une de ces conditions manque : un relecteur neuf, ou un second auteur pour F0/F0′.
- **(b) reste écartée** : la complaisance demande sa propre mesure comportementale.

**Ce qui est établi.** Rien au niveau objet : le bloc FAITS est vide. Ne sont acquises que des déductions sur le plan, vérifiables à la lecture et non par l'expérience :

1. La prédiction et la réfutation de H-M1, telles que la question les rapporte, peuvent être satisfaites ensemble. Un critère unique est donc nécessaire.
2. À séquence de jetons identique, les activations sont identiques au bruit numérique près (HYPOTHÈSE déductive). Une sonde de pure provenance ne peut rien apprendre sur des textes identiques, et S1 ne peut pas servir à équilibrer T.
3. Le sens de « β_T > β_C » dépend de la partition des traits. Cette dépendance doit être mesurée (E6), pas présumée.

**Ce qui n'est pas établi.** Toutes ces questions restent des HYPOTHÈSES :

- l'existence d'une direction linéaire de « conscience d'évaluation » dans Llama-3.1-8B-Instruct ;
- le transfert de la direction de mention explicite vers l'implicite ;
- la domination de T, son mécanisme (familiarité, format ou fluidité), et l'additivité de T et C ;
- H-M2 et sa lecture en termes de dérive distributionnelle ;
- la capacité d'une sonde linéaire, lue sur un seul jeton avant génération, à saisir un concept peut-être conjonctif ou tardif.

**L'expérience à faire en premier : E0′.**

- **Ce qu'elle oppose** : une direction sémantique (H_A) à une direction lexicale (H_B), sur des mentions de lexique disjoint, contre un prédicteur de surface entraîné sur la même discrimination.
- **Pourquoi elle d'abord** :
  - elle ne lit aucun item de test ;
  - elle coûte moins d'une heure de carte graphique (illustratif) ;
  - chacune de ses deux issues décide de la suite. Une réussite rend S2′ admissible pour E1′. Un échec réduit E1′ à la branche S3, ou renvoie à (c).
- **Ce qu'elle ne prouve pas** : une « conscience ». Elle garantit seulement qu'un « T domine » futur ne viendrait pas d'un détecteur de mots.

---

## Ce qui reste réfutable dans cette riposte

1. **D1** suppose qu'une mention explicite active la représentation quel que soit le gabarit. Si E3′ montre que β_T dépend fortement de la famille d'entraînement, S2′ hérite du défaut que je reprochais à S1.
2. **D3** : la fraction 0,1 de Δ_expl est un choix de fond, sans justification empirique. Un relecteur peut en défendre une autre, mais seulement avant scellement.
3. **D4** : la règle d'unanimité sur 8 branches augmente la probabilité de l'issue « sensible aux choix ». Si la simulation la donne majoritaire même sous un effet vrai de taille δ, le multivers est trop large et doit être réduit avant scellement.
4. **E6** : la propriété du plan de Fano (les 4 coins dans la fraction) est un calcul de ma part, à vérifier par énumération.

FIN-DE-CELLULE