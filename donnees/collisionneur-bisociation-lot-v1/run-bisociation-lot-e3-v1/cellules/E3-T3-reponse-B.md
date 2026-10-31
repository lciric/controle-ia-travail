# Proposition B — Tour III.3 : réponse aux critiques

## (a) Traitement des critiques adressées à B

---

### A-critique-1 (Appariement qui retire la variable testée, Exp. 1)

**Acceptée.** L'appariement « même distance textuelle » neutralise une composante du trou (divergence lexicale, Vilhena 2014 — SUPPOSÉ). Si le trou est défini comme un profil multicouche (canal social faible ET structure commune forte), apparier sur la composante textuelle revient à conditionner sur une partie du prédicteur, réduisant la puissance à la seule composante résiduelle (citations). A a raison : cela ramène au retour à la moyenne (A0).

**Correction :** Les témoins sont appariés sur taille de niche, âge et taux de croissance uniquement. La distance textuelle devient une covariable *mesurée* mais non appariée, dont l'effet est estimé dans la régression. Cela préserve la variance du trou nécessaire à la discrimination.

---

### A-critique-2 (Contrôle négatif vide, Exp. 1)

**Acceptée.** Par construction, les témoins n'ont aucun pont à T₀+5 ; le contrôle ne peut rien mesurer. C pointe le même défaut (fuite temporelle dans la sélection des témoins).

**Correction :** Le contrôle négatif est remplacé par la **rétrodiction inversée (A0)** : calculer le trou à T₀, puis « prédire » les ponts apparus *avant* T₀ (entre T₀−5 et T₀). Un signal positif là mesure le retour à la moyenne et l'autocorrélation, pas la fertilité. Si l'AUPRC de la rétrodiction inversée n'est pas significativement inférieure à l'AUPRC prospective (T₀ → T₀+5), l'expérience entière est viciée par A0 et H_A est morte.

De plus, les témoins ne sont plus sélectionnés sur l'absence de lien à T₀+5. Ils sont tirés à T₀ parmi les paires n'ayant aucun lien à T₀, appariées par taille, âge et croissance. Certains témoins deviendront des ponts après T₀ (bruit d'étiquette) ; ce bruit est chiffré et intégré comme atténuation dans l'analyse (correction de Firth ou modèle à étiquettes bruitées).

---

### A-critique-3 (Paramètre de contrôle et paramètre d'ordre sur le même observable, Exp. 2)

**Acceptée en partie.** La densité de contacts (citations croisées) et la cascade traversante (citations croisées après T₀) sont effectivement mesurées sur le même graphe. La corrélation mécanique est réelle.

**Transformée en test :** En mondes inventés, le paramètre de contrôle est la densité de *prémisses partagées* (définie par le générateur, indépendante des citations), et le paramètre d'ordre est le nombre de *théorèmes mixtes validés* (vérité connue). Cela dissocie les deux. En littérature réelle, le paramètre de contrôle est remplacé par le nombre d'*objets mathématiques partagés* (extraits des AST LaTeX), mesuré sur une couche distincte du graphe de citations. Si la courbe n'apparaît qu'avec la densité de citations mais pas avec les objets mathématiques, l'effet est un artefact d'autocorrélation.

Ajout du contrôle demandé par A : des mondes inventés *sans* seuil planté (générateur purement additif, pas de percolation) sont analysés par la même chaîne. Si l'effondrement y est trouvé, la chaîne fabrique des transitions et Exp. 2 est invalidée.

---

### A-critique-4 (Métrique produit et bruit partagé, Exp. 3)

**Acceptée.** Le produit survie × couverture mêle deux quantités d'échelles différentes et cache les compromis exploration-exploitation (C formalise ce point : un essaim concentré peut avoir plus de survie mais moins de couverture, et le produit le pénalise).

**Correction :** La métrique produit est abandonnée. Les deux quantités sont rapportées séparément : (i) nombre total d'idées survivant aux tests de mort (absolu, pas un taux) ; (ii) nombre effectif de paires niche-niche couvertes (inverse de Simpson sur la distribution des paires touchées). Le test porte sur (i) seul, à couverture *minimale* préenregistrée (seuil : au moins 50 % des paires admissibles touchées par chaque condition — illustratif). Si une condition ne passe pas le seuil de couverture, son taux de survie n'est pas comparable.

Sur le bruit partagé : les conditions « essaim » et « indépendant » doivent utiliser la même famille de modèles pour les proposeurs (le test porte sur la communication, pas sur le modèle). Un second bras utilise une famille distincte pour les proposeurs indépendants ; la différence entre les deux bras indépendants borne le bruit partagé. Le consolidateur consomme des tokens comptés dans le budget total de l'essaim.

---

### A-critique-5 (Interpolation déguisée en intervention, Exp. 4)

**Acceptée.** La dose 7 est interpolée entre 5 et 10 ; tout modèle lisse y réussit. C démontre formellement que la puissance maximale du critère ne dépasse pas α = 10 % quand les deux modèles sont calibrés sur des données randomisées (la fonctionnelle observationnelle coïncide avec l'interventionnelle par construction).

**Correction :** La dose « jamais vue » est *extrapolée*, pas interpolée : dose 15 (au-delà de 10). De plus, le critère d'inclusion dans l'intervalle de prédiction est remplacé par une **comparaison de l'erreur quadratique moyenne** entre les deux modèles sur la dose extrapolée, avec test de permutation. Le placebo « couleur du fond » est remplacé par un **confondeur planté** en monde inventé (variable corrélée à la survie par un facteur caché, effet causal nul sur la fertilité) ; un modèle qui la retient comme « cause » est disqualifié. En littérature réelle, le contrôle est une variable corrélée au prestige de l'auteur du pont (ex. rang h-index du premier auteur), préenregistrée comme non causale de la fertilité.

---

### A-critique-6 (Fuite entre étalon et réglage, c1)

**Acceptée.** Si les mêmes schismes servent à choisir la résolution de SBM/Leiden et à évaluer le taux de détection, le 80 % est un ajustement.

**Correction :** Les schismes sont partitionnés en deux jeux disjoints *avant* toute analyse : schismes de réglage (pour choisir la résolution) et schismes de test (pour évaluer le taux de détection). Le partage est préenregistré et scellé.

---

### A-critique-7 (P8 : contradiction sur les 722 manuscrits)

**Rejetée partiellement.** A argue que « un agent unique long EST le régime réflexion profonde ». Le fait (RAPPORTÉ, porte-parole) dit « un seul prompt à un seul agent, ≈ 3 h de calcul en moyenne ». Je n'ai pas nié que c'est un agent long ; j'ai nié que l'architecture soit précisée, et que « pas de la réflexion profonde au sens technique » s'applique. Sur relecture, « au sens technique » était trop fort : l'architecture n'est pas publiée, donc le statut reste RAPPORTÉ. Le point corrigé : les 722 sont le *meilleur exemple disponible* du régime « tentatives indépendantes à réflexion longue », utilisable comme référence dans Exp. 3. L'essaim Navier-Stokes est le meilleur exemple du régime communicant. Les deux attaquent des problèmes bien posés ; la transposition au bisociateur (problèmes à poser) est une HYPOTHÈSE, pas un fait.

---

### C-critique-1 (Tautologie par construction, Exp. 1 — appariement textuel)

**Acceptée** — même diagnostic que A-critique-1. Voir correction ci-dessus.

---

### C-critique-2 (Fuite temporelle dans les témoins, Exp. 1)

**Acceptée** — même diagnostic que A-critique-2. Voir correction ci-dessus.

---

### C-critique-3 (Confondant d'échelle, Exp. 2)

**Acceptée en partie.** La taille N est endogène (corrélée à l'âge, au taux de croissance, à la pression du champ — Chu et Evans 2021, RAPPORTÉ). Comparer N = 100 et N = 2 000 confond l'effet de taille finie avec le changement sociologique.

**Transformée en test :** En mondes inventés, la taille est un paramètre libre du générateur, indépendant de l'« âge » ou du « régime sociologique ». L'effondrement est d'abord testé là. En littérature réelle, la taille est *stratifiée* par âge du champ et taux de croissance (régression avec ces covariables), et l'effondrement est testé sur les résidus. Si l'effondrement disparaît après stratification, l'effet était sociologique. De plus, le modèle nul est enrichi : recâblage temporel (permutation des dates des arêtes, préservant les corrélations temporelles et l'homophilie) en supplément du recâblage statique.

---

### C-critique-4 (Interpolation et puissance ≤ 10 %, Exp. 4)

**Acceptée** — la démonstration formelle de C est correcte. Voir correction A-critique-5.

---

### C-critique-b1 (Censure asymétrique dépendante du profil, Exp. 1)

**Acceptée comme risque.** Wang 2017 (RAPPORTÉ) montre que les paires distantes mettent plus longtemps à être reprises. Le taux de censure η dépend du profil, biaisant la précision@k contre les paires distantes.

**Transformée en test :** L'horizon h est allongé (h ≥ 5 ans, illustratif), et l'analyse est répétée à h = 3, 5, 8, 10 ans. Si le classement des méthodes s'inverse avec h (les paires distantes remontent), le biais de censure est documenté et le résultat est conditionné à l'horizon. Un modèle de survie (Cox) est ajouté comme analyse secondaire, traitant la censure à droite.

---

### C-critique-b2 (Biais de Simpson sous-échantillonné, Exp. 3)

**Acceptée.** Quand M ≫ N, l'inverse de Simpson est borné par N et ne mesure plus la diversité réelle.

**Correction :** La diversité est mesurée par le nombre de *grappes de concepts distinctes* (après regroupement par Jaccard > 0.5, seuil gelé) plutôt que par l'inverse de Simpson brut. Le nombre de grappes n'est pas borné par N. Le seuil de Jaccard est préenregistré.

---

### C-critique-b3 (Non-identifiabilité de l'effondrement, Exp. 2)

**Acceptée.** Avec 4 tailles et 12 points, la Fisher est quasi-singulière.

**Correction :** Le nombre de tailles est porté à ≥ 6 (en mondes inventés, cela ne coûte que du calcul — illustratif : 50, 100, 200, 500, 1 000, 2 000, 5 000 prémisses). En littérature réelle, le nombre de tailles accessibles est limité par le nombre de sous-domaines ; si < 5 tailles sont disponibles, l'effondrement n'est pas testable et le mot « transition de phase » est suspendu. Une sigmoïde lisse (Gumbel) est ajoutée comme modèle rival dans la comparaison BIC.

---

### C-critique-c2 (Contrôle d'identités mathématiques banales, c4)

**Acceptée.** L'extracteur AST signalera des isomorphismes triviaux (Cauchy-Schwarz, valeurs propres) partagés par toutes les niches quantitatives.

**Correction :** Un filtre TF-IDF sur les sous-arbres est ajouté : la pondération d'un objet mathématique partagé est inversement proportionnelle à sa fréquence dans le corpus global. Les identités ubiquitaires reçoivent un poids proche de zéro. Le contrôle négatif est : 50 paires de niches partageant uniquement des structures ubiquitaires (poids < seuil gelé) ; l'extracteur ne doit pas les classer comme « structure commune forte ».

---

### D-critique sur B — rehaussement de statuts

**Acceptée en partie.** Les statuts VÉRIFIÉ dans ma conception s'appliquent à l'*existence* de la référence (page ou résumé lu), pas au contenu détaillé ni aux chiffres opposables. La formulation « VÉRIFIÉ existence » était correcte pour Gu-Krenn 2024, Bettencourt 2015, etc. Cependant, les courbes de Uzzi 2013 ou Shi-Evans 2023, citées comme « VÉRIFIÉ », n'ont été lues que dans la revue du lot (OBSERVÉ-NON-AUDITÉ au mieux). La forme de la courbe reste RAPPORTÉ. Correction : chaque référence dans les expériences corrigées ci-dessous porte son statut exact.

---

### D-critique — contrôle négatif vide (Exp. 1), non-identifiabilité de la taille (Exp. 2), marge d'équivalence (Exp. 3 et 4), étalons de c4

Tous ces points recoupent ceux de A et C. Les corrections sont celles décrites ci-dessus. Sur la **marge d'équivalence** (Exp. 3 et 4) : D a raison qu'un non-rejet à p < 0,05 ne prouve pas l'équivalence. Correction : une marge d'équivalence δ₀ est préenregistrée (illustratif : δ₀ = 5 % absolu de taux de survie pour Exp. 3 ; δ₀ = 0,03 d'AUPRC pour Exp. 1). Le test TOST (two one-sided tests) est ajouté : si les deux tests unilatéraux rejettent, l'équivalence est déclarée. Sinon, le résultat est « non concluant ».

---

### A0 (Retour à la moyenne — artefact partagé par B, C, D)

**Acceptée comme risque majeur.** La rétrodiction inversée est le contrôle qui l'annule. Elle est ajoutée à Exp. 1 et Exp. 2 (voir corrections ci-dessus).

---

## (b) Expériences corrigées

### Exp. 1 corrigée : Trou vs distance (avec A0 et témoins non conditionnés sur le futur)

- **H_A / H_B** : inchangées.
- **Témoins** : tirés à T₀ parmi les paires sans lien à T₀, appariés par taille, âge, croissance (pas par distance textuelle). Bruit d'étiquette chiffré.
- **Contrôle négatif** : rétrodiction inversée (A0). Un « témoin popularité seul » (degré, âge, croissance) est ajouté comme troisième bras ; si H_A et H_B sont toutes deux battues par la popularité, le duel est sans objet.
- **Marge d'équivalence** : TOST avec δ₀ = 0,03 d'AUPRC (illustratif).
- **Analyses secondaires** : modèle de survie (Cox) pour traiter la censure différentielle ; répétition à h = 3, 5, 8, 10 ans.

### Exp. 2 corrigée : Forme de la courbe

- **Paramètre de contrôle** : objets mathématiques partagés (couche distincte des citations) en littérature réelle ; prémisses partagées en mondes inventés.
- **Tailles** : ≥ 6 en mondes inventés. En littérature réelle, si < 5 tailles disponibles après stratification, le mot « transition de phase » est suspendu.
- **Modèles rivaux** : cloche lisse, sigmoïde (Gumbel), seuil critique, monotone — comparés par BIC avec vraisemblance spécifiée pour la variance (surdispersion, pas variance binomiale simple).
- **Contrôles** : mondes sans seuil planté analysés par la même chaîne ; rétrodiction inversée ; modèle nul à recâblage temporel.

### Exp. 3 corrigée : Essaim vs indépendant

- **Métrique** : nombre d'idées survivantes (absolu), à couverture minimale (50 % des paires, illustratif). Diversité par grappes de concepts (pas Simpson).
- **Budget** : tokens du consolidateur inclus dans le budget de l'essaim.
- **Bras** : (1) essaim communicant (couplage intermédiaire) ; (2) N indépendants, même famille ; (3) N indépendants, famille distincte ; (4) essaim, messages mélangés aléatoirement. La différence (2)−(3) borne le bruit partagé.
- **Marge d'équivalence** : δ₀ = 5 % absolu de taux de survie (illustratif), TOST.

### Exp. 4 corrigée : Causalité

- **Dose extrapolée** : 15 (au-delà de 10), pas 7.
- **Critère** : comparaison de l'erreur quadratique moyenne entre modèle causal et modèle prédictif sur la dose extrapolée, test de permutation.
- **Contrôle négatif** : confondeur planté en monde inventé ; variable corrélée au prestige en littérature réelle ; préenregistrée comme non causale.
- **Contrôle de pré-tendance** : résultat antérieur au traitement ; un effet trouvé là invalide l'identification.

---

## (c) Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### Ce qui est établi (dans les faits servis)

1. Des prédicteurs de liens futurs entre concepts existent et atteignent des performances élevées (Gu-Krenn 2024, AUC > 0,9 — OBSERVÉ-NON-AUDITÉ, page arXiv lue). Leur signal est porté en grande partie par la centralité et le voisinage local.
2. La relation entre distance et impact dépend de la définition de l'impact et de l'horizon : cloche à court terme (Uzzi 2013 — RAPPORTÉ), monotone croissant quand la mesure intègre la structure latente (Shi-Evans 2023 — RAPPORTÉ), défavorable en moyenne mais favorable en variance (Fleming 2001 — RAPPORTÉ).
3. La connectivité partielle entre groupes favorise l'accumulation culturelle complexe en laboratoire (Derex-Boyd 2016 — VÉRIFIÉ existence, contenu RAPPORTÉ via revue).
4. Aucune transition de phase dans P(reprise | paire) n'a été mesurée dans la littérature (revue de fertilité, section 5 — OBSERVÉ-NON-AUDITÉ). Les transitions documentées portent sur la structure sociale (percolation des coauteurs — Bettencourt 2015, VÉRIFIÉ existence).
5. L'identification causale des paramètres qui *créent* la fertilité nécessite une source d'intervention ou une hypothèse d'invariance explicite ; l'apprentissage profond seul, sur données d'observation, apprend ce qui accompagne, pas ce qui cause (réponse conv-audit Q5 et relecture — RAPPORTÉ).

### Ce qui n'est pas établi

1. Que le « trou » (déficit de canal + structure commune) prédise les ponts mieux que la distance scalaire ou que la popularité seule.
2. Que la fertilité d'une paire soit prédictible ex ante au-delà de la centralité.
3. Que la transition de phase soit le bon modèle pour la fertilité (vs cloche lisse, vs monotone).
4. Que les essaims communicants ajoutent quelque chose au meilleur-de-N pour la génération d'idées (vs résolution de problèmes bien posés).
5. Que les résultats des courses internes se transportent à la science réelle.

### L'expérience à faire en premier

**Constitution de la base de ponts et témoins + rétrodiction inversée (A0).**

- **Pourquoi en premier** : sans elle, aucune des quatre expériences n'est testable, et l'artefact A0 (retour à la moyenne) n'est pas contrôlé. C'est la seule étape qui est à la fois nécessaire à tout le reste, de faible coût (~2–4 k€ de temps chercheur, HYPOTHÈSE), et qui peut tuer le programme entier si le résultat est positif (rétrodiction inversée aussi bonne que la prédiction prospective → toute la machinerie trou/distance est un artefact).
- **Protocole** : un lecteur aveugle (ne connaissant ni les définitions de trou, ni les scores) constitue 30–50 ponts historiques datés (dans des domaines couverts par arXiv, post-1991, pour compatibilité avec les sources LaTeX) et 100–150 témoins appariés par taille, âge, croissance. Le trou, la distance et la popularité sont calculés à T₀. L'AUPRC prospective (T₀ → T₀+5) et l'AUPRC de rétrodiction inversée (T₀ → T₀−5) sont comparées pour chaque mesure. Si AUPRC(rétrodiction) ≥ AUPRC(prospective) − δ₀ pour *toutes* les mesures, le programme de détection de trous est suspendu et le bisociateur conserve la règle actuelle (loin en domaine, proche en concept) en attendant un diagnostic de l'artefact.
- **Coût** : ~2–4 k€ illustratif (temps humain), ~50 € illustratif (calcul CPU pour les mesures).

FIN-DE-CELLULE