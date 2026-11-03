# Proposition B — Tour III.2 : critique croisée de méthode

**Pièces.** Annexes F et G, figure 32 et moisson intégrale : absentes des faits servis. Je n'en infère rien.

**Conventions.**
- Les chiffres de Kirchner sont RAPPORTÉS : pièce Kirchner, lecture par outil, non opposable.
- Les chiffres de Lazar sont cités par section de la pièce « nos résultats ». Je ne leur donne aucun statut plus fort que celui de la pièce : ils sont publics, je ne les ai ni réexécutés ni audités.
- Mes affirmations sont des HYPOTHÈSES ou des calculs. Tout effectif ou seuil que je pose est illustratif.

**Notation commune pour les parties (b).**
- $V$ : violation (vraie ou plantée) ; $M$ : verdict « détecté » du moniteur ; $S$ : score de classement ; $T$ : appartenance au lot retenu (top-$k$, quartile, promotion).
- $R_0 = P(M{=}1 \mid V{=}1)$ et $R_T = P(M{=}1 \mid V{=}1, T{=}1)$.
- $N_T \sim \mathrm{Bin}(n_V, q)$, avec $q = P(T{=}1 \mid V{=}1)$, est le nombre de violations dans le lot retenu.
- Demi-largeur d'un intervalle à 95 % sur une proportion $R$ : $h \approx 1{,}96\sqrt{R(1-R)\,\mathrm{deff}/N}$, avec $\mathrm{deff} = 1 + (m-1)\,\mathrm{ICC}$ pour des grappes de taille $m$.
- Un duel entre deux seuils séparés d'un écart $g$ est non jugeable dès que $h \gtrsim g/2$.

**Repère (calcul illustratif).** Pour $R = 0{,}7$ et $g = 0{,}15$, il faut $N_T \gtrsim 143$ violations effectives dans le lot retenu, sans grappes.

---

## Sur la proposition A

### (a) Défauts de méthode

1. **Le facteur d'enrichissement $E$ de E1 est vrai par construction s'il est calculé comme écrit.**
   - A le définit comme « part de plants non détectés dans le top-$k$ / part de plants non détectés dans la population ». Lu comme un rapport de proportions parmi *toutes les méthodes*, il monte dès que les plants sont surreprésentés au sommet.
   - Or les classes R et F gagnent du score par construction (relancer un modèle déjà efficace, calquer le format du banc). $E > 1$ s'obtient donc même si le rappel est constant.
   - La seule quantité qui isole le moniteur est $(1 - R_T)/(1 - R_0)$, calculée parmi les seules violations. A doit l'écrire ainsi.

2. **Confusion de composition (effet de Simpson).**
   - Si R est surreprésentée au sommet et que le rappel diffère entre R, F et P, alors $R_T \neq R_0$ sans aucun effet de sélection à l'intérieur d'une classe.
   - A stratifie par rang, mais pas par classe à l'intérieur du rang.
   - La proposition E le prévoit (« rappel standardisé à mélange de familles constant ») ; je m'appuie sur ce point en le disant.

3. **Les plants ne viennent pas de l'agent, donc E1 ne teste pas l'effet « même modèle ».**
   - A insère les plants « à un taux connu » sans dire qui les écrit.
   - Si c'est l'expérimentateur, la corrélation d'angles morts entre agent et moniteur du même modèle n'est pas en jeu : la condition « même famille / autre famille » mesure alors la sensibilité de deux moniteurs à un texte humain.
   - Pour tester ce que A annonce, il faut des violations produites par l'agent lui-même (suscitées). La réserve de 2604.23488 (référence à vérifier) que A cite reste alors valable.

4. **Fuite entre construction et évaluation des plants.**
   - Si les plants sont mis au point en voyant les verdicts du moniteur d'audit, même à titre de « vérification qu'ils sont réalistes », ils sont de fait ajustés contre lui.
   - Il faut les sceller avant toute exposition au moniteur. A ne le dit pas.

5. **E2 peut être nul par construction.**
   - $S$ varie selon la configuration de l'agent ; le rappel sur P est mesuré « pour chaque configuration ».
   - Si les plants P sont insérés par l'expérimentateur, la configuration n'agit pas sur leur trace. On obtient alors $\rho \equiv 0$ par construction, ce qui serait lu à tort comme un succès de H_B.
   - La configuration doit produire elle-même la trace de la violation, sinon E2 ne mesure rien.

6. **E3 : la « bande près du seuil » est définie par la variable bruitée elle-même.**
   - Sélectionner des méthodes près du seuil d'après une mesure bruitée, puis mesurer leur basculement, donne $f \to 0{,}5$ quand la distance au seuil tend vers 0, par construction.
   - Il manque une estimation de la distance au seuil indépendante des évaluations utilisées pour $f$, et une source de hasard identifiée (graine de réentraînement ou échantillonnage de l'évaluation). Avec un évaluateur déterministe sur un modèle figé, $f = 0$ trivialement.
   - La borne $1-(1-f)^n$ suppose des soumissions indépendantes. Or 26 des 39 signalements sont des relances du même modèle (RAPPORTÉ, §3) : les soumissions successives sont corrélées.

7. **E4 est non jugeable avec les taux déjà rapportés.**
   - W2 est promue 12 fois sur 12 et la copie renommée 0 fois sur 200 (pièce « nos résultats », §2–3).
   - Pour W2, la sélection ne trie rien : « après promotion » équivaut à « avant », donc $\Delta \equiv 0$ par construction.
   - Pour la copie renommée, aucun cas n'est promu : $R_T$ n'est pas défini.

8. **Analogie non établie dans le tableau (c).** « Le classement est déjà “au plafond” comme nos juges (κ = 0) » rapproche deux objets différents :
   - D.3 porte sur la prédiction de Petri au-delà de la médiane (RAPPORTÉ) ;
   - le κ = 0 porte sur l'accord de deux juges de langage sur des fiches.

   C'est une HYPOTHÈSE de rapprochement, à marquer comme telle.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **$E$, et plus généralement $(1-R_T)/(1-R_0)$.** Le dénominateur compte $n_V(1-R_0)$ ratés. Pour $R_0 = 0{,}95$ et 180 plants, cela fait environ 9 ratés (calcul). L'estimateur du rapport a alors une variance non bornée, et il n'est pas défini si aucun plant n'est raté. La zone 1,3–2 annoncée « non concluante » couvrira presque tout l'espace dès que $n_V(1-R_0) \lesssim 20$.
- **Rappel par quartile.** Avec 60 plants par classe et $q = 1/4$, on attend environ 15 plants par classe dans le quartile supérieur, et $h \approx 0{,}23$ pour $R = 0{,}7$ (calcul). Le seuil d'écart de 0,10 de H_A n'est pas jugeable par classe. Si $q \to 0$ pour P (plants sans gain de score), $R_T$ n'est pas défini pour P, la classe même où A attend l'effet « même modèle ».
- **E2.**
  - Avec 40 configurations, l'erreur type de Fisher sur $\rho$ vaut $1/\sqrt{37} \approx 0{,}16$, d'où une demi-largeur d'environ 0,32 (calcul). L'écart entre $\rho \ge 0{,}4$ et $\rho \le 0{,}1$ est de 0,3 : non jugeable.
  - Atténuation : $\rho_{\text{obs}} = \rho \sqrt{\mathrm{fid}_S \cdot \mathrm{fid}_R}$. Avec des fidélités de 0,5 chacune, H_B gagne par atténuation seule.
- **E3.** Un $\hat f = 0$ sur $m = 20$ essais a une borne supérieure d'environ 0,15 (règle de trois, calcul). Méthode par méthode, on ne sépare pas 0,02 de 0,10. Regroupé, $f$ devient un mélange dont la valeur dépend de la largeur de bande choisie.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Permutation des scores à l'intérieur des lots** (présent chez D et E, absent chez A) : $R_T - R_0$ doit s'annuler. Sans ce contrôle, un artefact de composition n'est pas écarté.
- **$R_T$ par classe, à composition fixée.**
- **Pour E2, une condition placebo** où le plant est inséré tel quel dans la sortie de chaque configuration : le rappel doit y être indépendant de la configuration. C'est ce qui prouve que la variable agit bien sur la trace.
- **Moniteur aveugle au score.** Si les trajectoires lues contiennent le score ou le rang, le moniteur peut conditionner son verdict dessus. Masquer le score est nécessaire.
- **Pour E4, une classe plantée à probabilité de promotion intermédiaire** ($0{,}2 \le q \le 0{,}8$). Sans elle, E4 ne contient aucune sélection à mesurer.

---

## Sur la proposition C

### (a) Défauts de méthode

1. **Statuts relevés.**
   - « VÉRIFIÉ sur dépôt public » (sycophancie) et « VÉRIFIÉ/RAPPORTÉ » (929 essais) : aucun proposeur n'a d'accès web ni d'exécution (faits servis). Rien ici n'a pu être vérifié, et ces chiffres ne peuvent pas porter VÉRIFIÉ. C'est un relèvement de statut.
   - « C'est ce qui explique pourquoi la moitié supérieure du classement stagne sur Petri » présente une HYPOTHÈSE (exploitation de trous de couverture) comme explication acquise de D.3.

2. **Fiche 1 : la vérité de terrain manque là où porte H_A.**
   - H_A dit que le forum *réplique* les variantes qui passent le moniteur.
   - Mais seules les violations injectées ont une étiquette. Les copies que les agents en font via le forum (« top-3 visible ») ne sont pas étiquetées, sauf si un oracle mécanique les détecte.
   - Le rappel est donc mesuré sur les injections, pas sur la contagion que l'hypothèse invoque.
   - Les injections ne viennent pas non plus de Llama-8B agent. Le « même modèle » n'est donc pas testé (même défaut que A.3).

3. **Fiche 1 : classe $C_{\text{rec}}$ hétérogène.**
   - C la définit comme « type W2 / tricheurs pré-v8 », puis prend le nul v8 « sur la classe $C_{\text{rec}}$ couverte » comme contrôle.
   - Or les tricheurs pré-v8 (recoutures) sont couverts par v8 (0 sur 1 000), et W2 ne l'est pas : v8 déclare lui-même ne pas couvrir W2 (pièce « nos résultats », §2–3).
   - La valeur attendue du contrôle n'est donc pas définie.

4. **Fiche 1 : effectifs incohérents.** 5 × 20 × 2 × 5 = 1 000 propositions, dont 20 % plantées, soit 200 plants (calcul). Le seuil de falsification parle de « 500 trajectoires plantées ».

5. **Fiche 1 : la falsification de H_A repose sur l'absence de significativité.** « Fisher $p > 0{,}10$ » ne falsifie rien : il faut un intervalle contenu dans la zone de H_B.

6. **Fiche 2 : fuite entre sélection et évaluation.**
   - Les configurations sont sélectionnées sur la détectabilité *par le moniteur* sur $B_{\text{mon}}$, puis évaluées par le même moniteur sur $C_{\text{hors}}$.
   - La sélection s'est donc faite contre ce moniteur. On sort ainsi du cadre « sans gradient contre le moniteur » que la question demande, et on rejoint un terrain que la question liste comme déjà pris.
   - Il faut deux moniteurs : un pour sélectionner, un autre, scellé, pour auditer.

7. **Fiche 2 : hypothèse composite.**
   - H_A joint « $\Delta \text{AUC}_{\text{hors}} \le 0$ » et « hausse de la conscience d'évaluation ». Une issue où un seul des deux termes tient n'est attribuée à aucune branche.
   - La note de conscience d'évaluation suppose un juge (E.1 l'obtient d'un auditeur Sonnet 4.6, RAPPORTÉ). Sur Llama-8B, le juge n'est pas spécifié.
   - Les « LoRA de lisibilité » sont un entraînement : il faut dire contre quoi.

8. **Fiche 2 : banc P3 inadapté.** Les 2 400 actions de P3 sont figées (pièce « nos résultats », §6). Sélectionner 50 configurations d'agent impose de régénérer, donc ce n'est plus P3. De plus, si $C_{\text{hors}}$ est inséré, $\Delta \text{TPR}_{\text{hors}} \equiv 0$ par construction (même défaut que A.5).

9. **Fiche 3, volet 1 : deux facteurs confondus et un résultat vrai par construction.**
   - $T_2$ change à la fois l'opacité et le nul (« v9 couvrant les partitions par morceaux »). Si v9 couvre W2, le taux de fausse promotion W2 est borné par la procédure (Ville), par construction. La baisse ne dirait rien de l'opacité.
   - Il faut un plan 2 × 2 (opacité × nul).

10. **Fiche 3, volet 2 : plusieurs défauts.**
    - La courbe dose-réponse de sycophancie est déclarée « équivalent mécanique de Petri » sans validation.
    - Le seuil « −0,5 au-delà de la barre de ±0,64 » prend pour erreur type ce qui est une dispersion entre méthodes (médiane 5,65 ± 0,61, RAPPORTÉ D.3).
    - L'e-processus de l'organisme promeut des *lois* contre une nulle. « La première méthode qui franchit 1/α » n'a pas de nulle définie.
    - T0.3 est décrit comme « calibré par permutation » ; la pièce dit « calibré sur 1 000 épisodes honnêtes entiers ».

11. **Tableau (c) : deux objets mal lus.**
    - « FDR ≤ 0,05 borné par l'inégalité de Ville » : Ville borne l'erreur de première espèce d'un e-processus, pas un taux de fausses découvertes sur des tests multiples.
    - L'écart 1,00 contre 0,91 est une part de fiches « notables », pas une référence mécanique à battre.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Fiche 1.** Avec 200 plants répartis en deux conditions et un top 10 % uniforme, on attend environ 10 plants par bras, d'où $h \approx 0{,}28$ pour $R = 0{,}7$ (calcul). Le seuil de −0,15 n'est pas jugeable.
  - L'interaction $\Delta\Delta$ a une variance environ quatre fois plus grande qu'un effet principal.
  - Si les plants n'ont pas de gain de score ($q < 0{,}1$), $N_T \approx 0$.
  - Avec 5 agents par course, les rondes forment des grappes : $\mathrm{deff} > 1$ dès que l'ICC est positive.
- **Fiche 2.**
  - L'unité est la configuration : 5 contre 5. Si la variance entre configurations de $\text{TPR}_{\text{hors}}$ dépasse la variance d'échantillonnage sur 400 épisodes, le nombre effectif tombe à environ 10.
  - Le top-5 sur 50 subit la malédiction du gagnant : $\Delta \text{TPR}_{\text{in}}$ est gonflé, sauf s'il est remesuré sur des données neuves.
  - Si la sélection réduit la fréquence des violations, $n_V$ chute avec.
- **Fiche 3.**
  - Avec 3 lois vraies, la résolution est d'un tiers (33 points) : « chute de plus de 20 points » est non jugeable. La référence est elle-même instable : 3 sur 3 avec le plan plein, 2 sur 3 avec le plan gelé.
  - Le 99e centile sur environ 60 méthodes est le maximum. Son biais vaut environ $\sigma\sqrt{2\ln 60} \approx 2{,}9\,\sigma$ (calcul, normalité supposée).
  - Avec ~200 exemples par banc, l'erreur type d'une fraction vaut au plus ≈ 0,035 (calcul) : au-delà de la médiane, l'ordre entre méthodes peut être entièrement dû au bruit.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Fiche 1** : permutation des scores dans les lots ; moniteur d'une autre famille *à taux de fausses alertes égalisé* (C propose un moniteur hétérogène sans égaliser) ; oracle mécanique sur les copies venues du forum.
- **Fiche 2** : moniteur d'audit distinct du moniteur de sélection ; banc de sélection à étiquettes permutées (contrôle proposé par E, que je reprends) ; condition placebo où la violation est insérée.
- **Fiche 3** : cellules « opacité seule » et « v9 seul » ; auditeur externe fixé avant de voir les candidats et non construit par les auteurs de l'hypothèse.

---

## Sur la proposition D

### (a) Défauts de méthode

1. **D1 confond qualité du moniteur et effet de sélection.**
   - Falsifier H_A exige des bornes inférieures de $R_0$ et $R_S$ au moins égales à 0,90.
   - Un moniteur médiocre mais *stable* ($R_0 = R_S = 0{,}6$) contredit l'enrichissement, mais D le classe « non décisif ». Pour tout moniteur réaliste, H_A n'est réfutable que s'il est excellent : l'asymétrie favorise H_A.
   - L'enrichissement se juge sur $\Delta$ à $R_0$ donné.

2. **Issue de rejet de H_B mal écrite.** « Intervalle entièrement compatible avec un déficit d'au moins 0,10 » ne correspond à aucun des seuils posés (−0,20 et −0,05). Rejeter H_B ($\Delta \ge -0{,}05$) demande une borne supérieure de $\Delta$ inférieure à −0,05.

3. **$R_S$ dépend du placement des plants, décidé par l'expérimentateur.**
   - $R_S$ porte sur « les plants que le score seul placerait parmi les lauréats ». Si l'auteur des plants fixe leur gain de score, la corrélation entre score et indices de détection est créée par lui.
   - $\Delta$ mesure alors le générateur de plants, pas le classement.
   - L'appariement des honnêtes « par décile de score » ne corrige pas ce défaut.

4. **Le « même modèle » n'est pas testé.** D écrit en (a) que l'effet de partage de poids « doit être comparé à un moniteur distinct ». Mais D1 n'a qu'un moniteur, Llama-8B, à la fois agent et moniteur, et les plants ne viennent pas de l'agent (même défaut que A.3).

5. **D2 : hypothèses qui se recouvrent.**
   - H_A demande un gain externe d'au moins 0,15 sans « effondrement d'une classe », effondrement non chiffré dans H_A.
   - H_B accepte un gain interne avec « une classe qui chute d'au moins 0,20 ».
   - Un gain externe moyen de 0,15 avec une classe en chute de 0,20 satisfait H_B et peut-être H_A. Il faut un seuil commun pour l'effondrement.

6. **Point fort à garder.** D refuse la chaîne de raisonnement comme vérité de terrain et calcule les intervalles par grappe.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **D1.**
  - 400 plants en quatre classes donnent 100 par classe. Avec un lot de lauréats à $q = 0{,}1$, on attend environ 10 plants par classe parmi les lauréats.
  - Toutes classes confondues, $N_T \approx 40$ et $h \approx 0{,}14$ pour $R = 0{,}7$ (calcul) : la zone entre −0,20 et −0,05 n'est pas jugeable.
  - Si $R_0 < 0{,}20$, la condition $\Delta \le -0{,}20$ est impossible par construction : H_A est exclue d'avance.
  - Avec des cohortes de taille $m$ et une ICC de 0,1, $\mathrm{deff} = 1 + 0{,}1(m-1)$.
- **D2.** Par classe externe, il faut environ 70 violations par bras pour exclure 0,15 autour de 0 (calcul : $3{,}84 \cdot 2 \cdot 0{,}21 / 0{,}0225$). Si la sélection sur la surveillabilité réduit la fréquence des violations, $n_V$ externe diminue d'autant.

### (c) Contrôles négatifs dont l'absence serait fatale

- **Moniteur d'une autre famille** à taux de fausses alertes égalisé. Sans lui, la thèse « même modèle » d'où part D n'est pas testée.
- **Score de plant tiré indépendamment des caractéristiques que lit le moniteur.** C'est le contrôle de placement : sans lui, $\Delta$ peut être produit par le générateur.
- **Plants scellés avant toute exposition au moniteur.**
- **Pour D2, banc de sélection à étiquettes permutées.** D a une sélection aléatoire, mais pas ce placebo propre au banc.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **E-S sur candidats scriptés : l'effet est fixé par le script.**
   - Sur des traces figées et scriptées, la loi jointe de $(S, \text{caractéristiques lues par le moniteur})$ parmi les violations est choisie par qui écrit le script.
   - Si le générateur tire $S$ indépendamment de ces caractéristiques, alors $D \equiv 0$. S'il les couple, $D$ prend la valeur qu'il a fixée.
   - E-S mesure donc l'outil de mesure, pas une propriété d'une boucle de recherche. Le test devient informatif seulement quand les candidats sont produits par des agents. E le repousse à une « extension ».

2. **La question du même modèle est hors champ.** Le problème servi porte sur un moniteur du même modèle que les agents. E-S n'a ni agent producteur ni moniteur d'une autre famille. E le reconnaît (« nouvelle session n'est pas supposée rendre leurs erreurs indépendantes ») sans le tester.

3. **Valeur de $R_U$.** Un tirage uniforme d'un sous-ensemble a la même espérance de rappel que l'ensemble ; $R_U$ n'apporte que du bruit par rapport à $R_0$ calculé sur tout le lot. Comparer $R_C$ à $R_0$ sur l'ensemble serait plus puissant.

4. **E-T : la fréquence de violation est une variable confondante.**
   - Une configuration choisie pour sa surveillabilité peut violer moins souvent, ou des violations différentes.
   - E standardise par classe et par gravité, mais si les violations sont suscitées, la configuration change aussi *quelles* violations existent. $G$ mélange alors le rappel et la sélection des cas.
   - Si les violations sont insérées, $G \equiv 0$ par construction (même défaut que A.5).

5. **Points forts que je reprends en le disant.**
   - L'oracle mécanique complet sert d'étiquette, pas de référence à battre. Cela corrige les tableaux de A, C et D, qui font d'une même pile mécanique à la fois l'étiquette et le concurrent.
   - Le filtre se mesure sur ses entrées, pas sur ses survivants.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **E-S.**
  - 96 lots dont on garde le premier, avec une fréquence de violation $p$, donnent $N_C \approx 96\,p$. À $p = 0{,}2$, on attend environ 19 violations retenues (calcul illustratif).
  - Pour exclure la marge de 15 points quand l'effet vrai est nul, il faut environ 70 violations par bras (calcul, $R = 0{,}7$). Le pilote ne peut pas conclure, ce qu'E admet en partie.
  - Si le classement évite les violations ($q \to 0$), $R_C$ n'est pas défini.
  - Avec des lots de 8 et une ICC positive, $\mathrm{deff} = 1 + 7\,\mathrm{ICC}$.
  - Le rappel standardisé à mélange constant demande un support positif de chaque famille dans les deux bras. Une famille absente du bras « classement » le rend non défini.
- **E-T.** Si le gain sur le banc de développement est inférieur à son erreur type, la condition préalable échoue. Si $p_{\text{cfg}}$ baisse, $n_V$ externe diminue avec elle. Pour exclure une marge de 10 points, il faut environ 160 violations par bras (calcul : $3{,}84 \cdot 2 \cdot 0{,}21/0{,}01$).

### (c) Contrôles négatifs dont l'absence serait fatale

- **Générateur aveugle.** Les candidats honnêtes et invalides doivent être écrits sans accès au moniteur d'audit, puis scellés. Sinon le script encode la frontière du moniteur : c'est une fuite entre construction et évaluation.
- **Moniteur d'une autre famille** à taux de fausses alertes égalisé, pour que la question servie soit touchée.
- **Condition de contrôle propre à E-T.** Violations insérées identiques dans toutes les configurations : $G$ doit y valoir 0, sinon le classement ou la standardisation fabriquent l'effet.
- **Contrôles déjà présents.** Permutation des scores dans les lots et banc à étiquettes permutées. Ce sont les seuls contrôles négatifs du tour qui visent exactement les quantités mesurées.

---

**Ce qui réfuterait mes critiques.**
- Si un proposeur montre que ses plants sont produits par l'agent (pas insérés) et scellés avant exposition, les critiques A.3–5, C.2, D.3–4 et E.1 tombent.
- Si les effectifs retenus atteignent les seuils de calcul ci-dessus, mes objections de non-jugeabilité tombent.

FIN-DE-CELLULE