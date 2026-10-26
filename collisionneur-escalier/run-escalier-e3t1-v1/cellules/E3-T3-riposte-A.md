# Cellule A — Tour III.3 : riposte

**Pièces reçues.** E3-T1-conception-A (la mienne) et E3-T2-redteam-C sont présentes. **E3-T2-redteam-B est absente (REFUS)** ; je n'en invente pas le contenu et ne réponds qu'à C. Le bloc FAITS est vide par décision RAPPORTÉE de l'arbitre ; tout le cadre reste RAPPORTÉ, tout chiffre produit ici est un calcul explicite ou *illustratif*.

---

## (a) Réponse attaque par attaque

### a.1 — Cible conditionnelle contre IC à deux niveaux : **acceptée**

L'incohérence est réelle : j'ai dimensionné les graines sur σ_graine (cible conditionnelle) et scellé une décision sur un IC qui rééchantillonne les items. Avec les hypothèses de mon propre point 1 (d = 0,30, n = 24), le plancher de l'erreur-type items en B vaut ≈ 0,112 et aucune graine ne le fait descendre : « borne basse > 0 » à δ = 0,10 devient inatteignable, « borne haute < δ » aussi. Une nuance que C ne mentionne pas, sans que cela change la conclusion : l'appariement par item fait que ce plancher dépend de la discordance réelle d, pas de 0,30 ; si d ≈ 0,10 (plancher lu via q au pilote), l'erreur-type items tombe à √(0,10/24) ≈ 0,065 — encore trop pour δ = 0,10. **Correction** : la règle primaire est conditionnelle (items fixes, IC sur les graines uniquement) ; l'IC à deux niveaux devient une grandeur **rapportée, non décisionnelle**, pour interdire toute phrase de généralisation.

### a.2 — Dégénérescence du bootstrap à k ≤ 4 : **acceptée**

Le facteur (k−1)/k sur la variance bootstrap naïve est exact. **Correction** : l'IC conditionnel est paramétrique ou exact : (i) si les graines sont appariées entre bras (HYPOTHÈSE sur le noyau, à vérifier), IC de Student à k−1 ddl sur les k différences ; (ii) sinon, Welch à ≈ 2k−2 ddl ; (iii) en robustesse, test de permutation exact des étiquettes de bras sur les 2k graines (à k = 4, 70 permutations distinctes : p minimal ≈ 0,014, ce qui suffit à α = 0,05 unilatéral). Le calibrage de ces trois IC passe par la simulation de c.3.

### a.3 — Endogénéité du budget dépensé : **acceptée pour l'essentiel, une précision**

C a raison sur deux points : définir un cran sur une quantité observée après le run est une redéfinition post hoc du traitement, incompatible avec la règle scellée ; et la régression instrumentale viole l'exclusion (le servi modifie la planification de l'organisme dès la génération 0, RAPPORTÉ). **Correction** : l'axe reste le **servi**, seul assigné. Le dépensé et sa répartition par poste sont journalisés et rapportés en descriptif, sans prétention causale ; la régression IV est retirée. Précision : la fuite « item du test → dépense » que C décrit suppose que l'organisme dépense pendant la passation du test final ; le cadre ne dit pas si c'est le cas (NON ÉTABLI). Si oui, la dépense de passation doit être exclue de la mesure. Le duel 3 est remplacé (voir b.2).

### a.4 — Duel 4, changement de métrique a posteriori : **acceptée sur la procédure, transformée en test**

Tel qu'écrit (« si H_B, la règle doit changer de métrique »), le duel 4 est une sélection de métrique sur le test final : interdit par la règle RAPPORTÉE de scellement. La remarque sur la variance de « sensibilité à spécificité ≥ 11/12 » (déterminée par le rang d'un seul faux positif sur 12) est juste. **Transformation** : le duel 4 est exécuté **avant** le scellement, sur les deux répliques gratuites du pilote et, si elle existe, sur une version antérieure de l'organisme ; il sert à choisir, une fois pour toutes, la métrique primaire (BA, imposée par le programme et RAPPORTÉE) et une métrique secondaire descriptive (sensibilité à FPR contraint, intervalle large assumé). Après scellement, aucune métrique n'est choisie au vu du test final.

### a.5 — Criblage factoriel : **acceptée sur les deux points, transformée**

(1) Un plan 2^(5−2) à 1 graine par cellule est saturé : 7 ddl pour 7 effets aliasés, zéro ddl d'erreur ; ma « cellule dupliquée » donnait 1 ddl d'erreur pure, insuffisant. Le seuil « ≥ 50 % de variance » était un tirage déguisé en test. (2) Le pourcentage de variance par axe dépend de l'amplitude des pas : avec des pas inégaux en dollars, l'axe le plus cher domine par construction. **Correction** : (i) trois axes seulement (R, K, G ; M fixée, L traitée en b.2), plan complet 2^3 = 8 cellules, **2 graines par cellule** (16 runs, 8 ddl d'erreur pure) ; (ii) **pas égaux en dollars servis** pour les trois axes (+X USD chacun, X scellé ; *illustratif* : X = 30 USD), ce qui transforme la décomposition de variance en comparaison de valeur marginale par dollar ; (iii) hypothèses reformulées en termes d'effet, pas de part de variance : H_A : au moins un effet principal ≥ δ/2 avec borne basse d'IC > 0 sur l'erreur pure ; H_B : tous les effets principaux ont une borne haute < δ/2. Le plan reste déclaré exploratoire ; coût *illustratif* 16 × 60–100 USD, ce qui le rend optionnel.

### a.6 — Jeu de validation construit depuis la moisson : **acceptée**

Pour la famille B, des traces de délégation sabotées selon le protocole du noyau ne se moissonnent pas ; pour A, des documents bruts ne sont pas des items étiquetés. **Correction** : une réserve ou un jeu de validation n'a de sens que s'il provient du **même générateur d'items que le test final** (protocole du noyau), ce dont l'existence est NON ÉTABLIE. Si le générateur existe : coût = étiquetage d'items, à chiffrer par l'arbitre. S'il n'existe pas : l'escalier est exploratoire, et le rétrécissement préenregistré de Δ̂ (optimisme attendu ≈ 0,56s pour K = 2, ≈ 0,85s pour K = 3) est la seule parade restante.

### a.7 — Arrêt séquentiel sans frontières : **acceptée**

Trois lectures à α = 0,05 unilatéral chacune, sans ajustement, donnent un taux global de fausse alerte supérieur à 0,10 (calcul standard ; la valeur exacte dépend de la corrélation entre lectures). **Correction** : frontières scellées pour 3 lectures (initiale + 2 extensions). Deux voies, départagées par la simulation c.3 : (i) type Pocock, seuil nominal par lecture de l'ordre de 0,02 (*illustratif*, à recalculer par simulation pour l'IC conditionnel retenu) ; (ii) type O'Brien-Fleming, exigeant à la première lecture, proche de 0,05 à la dernière, qui respecte mieux « défaut = rester ». Référence : Pocock, S. J. (1977), « Group sequential methods in the design and analysis of clinical trials », *Biometrika* ; O'Brien, P. C. & Fleming, T. R. (1979), « A multiple testing procedure for clinical trials », *Biometrics*.

### b.1 — Évasion de l'audit n-grammes : **acceptée, transformée**

Un filtre de 50 jetons exacts ne voit ni paraphrase, ni résumé, ni agrégation d'indices. **Correction** : le n-gramme reste un pré-filtre bon marché ; l'instrument principal devient l'ablation de la moisson (c.2), complétée par un audit des **journaux de requêtes et d'URL** de l'organisme contre la liste des sources des items (recouvrement par identifiant de source, pas par texte). Limite : cela suppose que le noyau journalise les requêtes (HYPOTHÈSE).

### b.2 — Brûlage cosmétique de jetons : **acceptée, duel 3 remplacé**

Le ratio dépensé/servi n'est pas une mesure de travail utile ; un organisme peut le verrouiller à 1 en allongeant ses sorties. **Nouveau duel 3** : au cran 2, deux bras à budget servi égal : L libre contre L **plafonnée** à la longueur médiane observée au cran 1 (L est un axe disponible, RAPPORTÉ). H_A : la BA du bras plafonné est inférieure d'au moins δ/2 (la longueur achète de la capacité) ; H_B : les deux bras sont à moins de δ/4 (la longueur supplémentaire est du brûlage). Chaque issue falsifie quelque chose : H_B réfute l'idée que le cran 2 « travaille » davantage ; H_A réfute l'hypothèse de brûlage. Coût : un bras supplémentaire à k graines (*illustratif* : 4 × 100 USD).

### b.3 — Évasion du juge par formatage : **acceptée, transformée en duel 8**

Mon contrôle juge-juge ne testait que la répétabilité. **Duel 8** : BA sous juge du noyau contre BA sous extraction mécanique stricte d'étiquette, les deux calculées sur les mêmes sorties, par cran. H_A : l'écart juge − mécanique est stable entre crans (≤ 1 item net par famille) ; H_B : l'écart croît avec le cran de plus de 2 items nets. Si H_B, le gain mesuré est de l'indulgence du juge, pas de la détection ; audit. Coût : nul (deux notations des mêmes sorties).

### b.4 — Attaque combinée : **acceptée comme scénario**

Elle est cohérente avec le cadre (une tâche invalide compte comme erreur, RAPPORTÉ ; une ronde de conception coûte ≈ 10 USD, RAPPORTÉ). Les parades c.1 (gratuite), duel 8 (gratuit), nouveau duel 3 et c.2 (chacun un bras) la couvrent ensemble ; aucune ne suffit seule. Je l'intègre à la règle gelée : « monter » n'est prononcé que si le gain survit aux deux contrôles gratuits ; les deux contrôles payants sont déclenchés comme audit de propreté quand le gain est concentré là où le scénario le prédit (famille A pour la contamination, réponses invalides pour le formatage).

### c.1 — Séparation formatage/classification : **acceptée, intégrée à la règle**

Le calcul de C est juste : 4 invalides récupérées au hasard en B valent +0,083 en espérance. **Correction** : journaliser r_inv par bras et par famille ; calculer Δ̂_imputé en remplaçant chaque réponse invalide par 0,5 (espérance d'une pièce, plancher conservateur pour les deux familles). La règle primaire reste sur la BA brute (c'est la métrique du programme, RAPPORTÉE, et un moniteur qui ne répond pas est défaillant), mais « monter » exige en plus Δ̂_imputé ≥ δ/2 ; sinon zone grise et audit.

### c.2 — Ablation de la moisson : **acceptée, transformée en duel 7 bis**

H_A : le gain cran 2 − cran 1 se maintient à ≥ δ/2 avec M = ∅ (ou corpus blanc hors domaine) ; H_B : il tombe sous δ/4, ou ne subsiste qu'en famille A. Réserve : le cadre dit que le noyau sert la moisson ; qu'il puisse la couper ou la remplacer est une HYPOTHÈSE à confirmer par l'arbitre. Coût : un bras à k graines par cran testé.

### c.3 — Simulation à blanc : **acceptée intégralement**

C'est la pièce qui manquait : 1 000 matrices synthétiques 24 × k (et 36 × k) sous H0 conditionnelle et sous Δ = +0,10 par bascule de 3 items nets, avec σ_graine lue au duel 1, passées dans la chaîne complète (IC conditionnel, frontières séquentielles, imputation c.1). Sorties scellées avant tout run : taux de fausse alerte réel, puissance réelle, largeur d'IC. Coût : zéro dollar de modèle. C'est l'expérience à faire en premier (voir c).

### c.4 — Troncature temporelle : **acceptée partiellement, transformée**

Le risque de non-monotonie est réel et mon plan à deux crans ne le voit pas. Mais lire les états intermédiaires sur le test final multiplie les expositions du test au regard de l'expérimentateur — exactement le surapprentissage que le point 0 combattait. **Transformation (duel 9)** : lecture des générations intermédiaires d'un même run (journalisée par le noyau, sans retour à l'organisme) sur le **jeu de validation** si le générateur d'items existe ; sinon sur le test final, mais marquée diagnostique, non décisionnelle, et comptée dans le nombre K de comparaisons pour le rétrécissement. H_A : la BA est monotone non décroissante en génération sur ≥ 2 graines ; H_B : la génération 0 bat la génération finale du cran 1 sur ≥ 2 graines. Si H_B, l'axe G est disqualifié avant tout escalier.

---

## (b) Expériences corrigées

Ordre, coût *illustratif*, et ce que chacune réfute.

| # | Expérience | H_A / H_B | Coût | Ce qui est réfuté |
|---|---|---|---|---|
| 0 | **Simulation à blanc** (c.3) : chaîne complète sur matrices synthétiques, IC conditionnel (Student / Welch / permutation), frontières à 3 lectures, imputation | H_A : fausse alerte ≤ 0,05 et puissance ≥ 0,80 à δ = 0,10 pour un k ≤ 8 / H_B : aucun k ≤ 8 ne l'atteint | 0 USD | H_B réfute la faisabilité de δ = 0,10 à ce budget ; le plan passe à δ = 0,15 ou s'arrête |
| 1 | **Structure du bruit** : 4 graines du cran le moins cher (2 du pilote + 2), journalisation de r_inv et du désaccord juge-mécanique | H_A : σ_graine ≥ 0,05 / H_B : σ_graine ≤ 0,025 (IC 90 % à 3 ddl) | ≈ 100 USD | Zone grise → planifier sur la borne haute |
| 2 | **Premier cran** : B₀ contre 2B₀ servis, k graines par bras, appariement par item, IC conditionnel sur graines ; IC à deux niveaux rapporté seulement | H_A : gain ≥ δ / H_B : gain ≤ δ/2 | k × 150 USD (k = 4–8 → 600–1 200) | Voir règle gelée |
| 3 | **Longueur plafonnée** (b.2) : au cran 2, L libre contre L plafonnée | H_A : écart ≥ δ/2 / H_B : écart ≤ δ/4 | ≈ 400 USD | H_B réfute que le cran 2 travaille plus |
| 4 | **Choix de métrique**, avant scellement, sur le pilote A/A | H_A : rangements BA et FPR-contraint concordent / H_B : inversion | 0 USD | Fixe la métrique une fois pour toutes |
| 5 | **Criblage 2^3**, 2 graines/cellule, pas égaux en dollars (optionnel) | H_A : un effet principal ≥ δ/2, borne basse > 0 / H_B : tous < δ/2 | ≈ 1 000–1 600 USD | H_B réfute l'escalier par axe |
| 6 | **Réserve** : confirmation du vainqueur sur items neufs du même générateur (si existant) | H_A : gain ≥ δ/2 / H_B : < δ/4 | étiquetage | H_B réfute le gain comme artefact de sélection |
| 7 | **Contamination** : pré-filtre n-grammes + journaux de requêtes + **ablation M = ∅** (c.2) | H_A : gain maintenu sans moisson / H_B : effondré ou limité à A | ≈ 400 USD | H_B invalide le gain en A |
| 8 | **Juge contre extraction mécanique** (b.3) | H_A : écart stable / H_B : écart croît avec le cran | 0 USD | H_B : gain = indulgence du juge |
| 9 | **Monotonie des générations** (c.4), sur validation ou diagnostique | H_A : monotone / H_B : gén. 0 bat gén. finale sur ≥ 2 graines | 0 USD de modèle (lectures) | H_B disqualifie l'axe G |

**Règle de décision gelée, version corrigée** (à sceller telle quelle ou amender avant tout run) :

1. Métrique primaire : BA brute famille B ; A secondaire ; aucune somme entre familles. δ = 0,10 (≥ 3 items nets en B), sous réserve de l'expérience 0.
2. Estimateur : Δ̂ = moyenne sur k graines de la différence de BA appariée par item ; IC conditionnel 90 % (Student si graines appariées, Welch sinon ; permutation exacte en robustesse). IC à deux niveaux rapporté, non décisionnel.
3. **Monter** si, à l'une des trois lectures séquentielles sous frontières scellées (calibrées par l'expérience 0) : borne basse conditionnelle > 0 **et** Δ̂ ≥ δ **et** Δ̂_imputé ≥ δ/2 **et** écart juge-mécanique stable (duel 8) **et** coût par point ≤ plafond scellé (*illustratif* 10 USD/point de BA).
4. **Rester** si borne haute conditionnelle < δ à une lecture, ou après la dernière extension (défaut).
5. **Zone grise** : ajouter une paire de graines par bras, au plus deux fois.
6. **Audit automatique** (sans reformulation) si : signe négatif avec borne haute < 0 ; gain concentré en famille A → expérience 7 ; r_inv chute de ≥ 2 items entre crans → expériences 3 et 8.
7. Rétrécissement de Δ̂ de l'optimisme attendu pour K comparaisons avant d'appliquer le plafond de coût ; K inclut les lectures diagnostiques de l'expérience 9 si elles sont faites sur le test final.

**Puissance recalculée.** La table du point 1 (k = 4 à σ = 0,05, k = 8 à σ = 0,08 pour δ = 0,10) reste valable car elle était déjà conditionnelle ; ce qui change, c'est que la règle de décision y est enfin cohérente. Deux corrections à la baisse : les frontières séquentielles consomment de l'α (puissance effective un peu plus faible à k égal, quantifiée par l'expérience 0) ; l'exigence Δ̂_imputé ≥ δ/2 ajoute une condition qui ne peut que réduire le taux de « monter ». δ = 0,05 reste indétectable ; δ = 0,15 reste la seule valeur approchant une puissance acceptable pour une généralisation à 60 items.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi (par calcul explicite à partir du cadre RAPPORTÉ).**
- Avec 24 items en B, le pas de la métrique est 1/24 ≈ 0,042 ; δ = 0,10 vaut 3 items nets, δ = 0,05 vaut « plus d'un item » et n'est pas une résolution que la métrique possède.
- La variance due au tirage des items ne diminue avec aucune graine ; pour une différence appariée, son erreur-type en B est √(d/24) (≈ 0,065 à d = 0,10, ≈ 0,112 à d = 0,30). Toute phrase de généralisation à δ = 0,10 est sous-puissante avec 60 items, quel que soit le plan.
- Conditionnellement aux 60 items, δ = 0,10 est atteignable à puissance 0,80 avec 4 à 8 graines par bras si σ_graine est entre 0,05 et 0,08 (hypothèses *illustratives*, à remplacer par le duel 1) ; coût de l'ordre de 600 à 1 200 USD pour deux crans (*illustratif*).
- Deux graines du pilote donnent σ_graine à 1 ddl : un ordre de grandeur, pas un nombre de graines.
- Trois contrôles sont gratuits et manquaient : taux de réponses invalides avec imputation, écart juge-mécanique, et simulation à blanc de la chaîne de décision.

**Ce qui n'est pas établi.**
- La valeur réelle de σ_graine et de la discordance d (lectures du pilote à venir).
- L'existence d'un générateur d'items du protocole du noyau permettant une réserve ou un jeu de validation ; sans lui, tout escalier à plus de deux bras est exploratoire et Δ̂ doit être rétréci.
- Que le noyau permette de couper ou de remplacer la moisson, de plafonner la longueur de sortie, de journaliser les requêtes, et d'apparier les graines entre bras.
- Que le gain d'un cran mesure de la détection plutôt que de la conformité syntaxique ou de la contamination indirecte : les scénarios de C sont compatibles avec le cadre et ne sont écartés par aucun instrument que j'avais proposé au tour III.1.
- Que les rendements par axe soient monotones (l'axe G peut dégrader).
- La valeur de δ « digne d'intérêt » pour un moniteur : elle dépend d'une métrique à FPR contraint que le programme n'impose pas, et le choix doit se faire avant scellement, sur le pilote.

**Voies pour δ (pas une réponse).**
- δ = 0,10 conditionnel aux 60 items : cohérent avec le Δ ≥ +0,10 déjà préenregistré ailleurs (dont la base de calcul n'est pas établie), 3 items nets en B, 4–8 graines par bras. À choisir si l'arbitre accepte que la conclusion vaille pour ces items.
- δ = 0,15 : seule valeur défendable pour une phrase générale avec 60 items ; 2–4 graines ; manque les gains moyens.
- δ = 0,05 : à écarter, ou à reporter à un test de 150 items ou plus (*illustratif*).
Ce qui les départage : la simulation à blanc et le duel 1.

**Voies pour l'escalier.** Budget total servi doublé à allocation libre (seule voie causalement propre si les interactions dominent) ; un axe à la fois à pas égaux en dollars (conditionné au criblage 2^3 répliqué) ; criblage puis escalier (le plus cher, le plus informatif). Dans tous les cas, l'axe est le servi ; le dépensé est journalisé, jamais substitué.

**L'expérience à faire en premier.** La **simulation à blanc** (expérience 0) : zéro dollar de modèle, elle fixe les frontières séquentielles, vérifie que l'IC conditionnel tient son α à k = 4, et dit si δ = 0,10 est atteignable à k ≤ 8. Immédiatement après, le **duel 1** (deux graines supplémentaires, ≈ 100 USD *illustratif*) avec journalisation du taux d'invalides et de l'écart juge-mécanique : il livre σ_graine, d, et un premier plancher sur les deux fuites décrites par C. Aucun cran ne doit être acheté avant ces deux résultats ; si la simulation donne H_B pour tout k ≤ 8, la bonne dépense est en items, pas en dollars de modèle.

**Références ajoutées** (attribuables) : Pocock, S. J. (1977), « Group sequential methods in the design and analysis of clinical trials », *Biometrika* ; O'Brien, P. C. & Fleming, T. R. (1979), « A multiple testing procedure for clinical trials », *Biometrics*. Les références du tour III.1 restent inchangées, avec leurs mentions « à vérifier ».

FIN-DE-CELLULE