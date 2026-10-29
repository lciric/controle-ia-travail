# Proposition B — Tour III.2 : équipe rouge croisée

## 0. État des pièces (règle 2)

- **FAITS** : dans la pièce, les lettres accentuées sont remplacées par « ? ». Le texte reste lisible et ne paraît pas coupé.
- **QUESTION** : je confirme les constats de A et de C sur pièce. Aucun champion `claude-opus-5-5` n'est présent, et 18 des 20 champions s'arrêtent au milieu d'un mot ou d'une formule, malgré la mention « zéro caractère coupé ». Je n'invente aucun contenu manquant.
- **Statuts** : mes constats tirés de la relecture des pièces sont marqués OBSERVÉ-NON-AUDITÉ (relecture). Les scores jev restent OBSERVÉ-NON-AUDITÉ. Tout ce qui porte sur le comportement futur d'un agent ou d'un instrument est HYPOTHÈSE.

---

## Contre la proposition A

A est la plus prudente des deux. Ses défauts sont plus fins, mais trois d'entre eux sont **vrais par construction** et neutralisent ses propres duels.

### (a) Failles

**A-1. La matrice de confusion de jev ne peut pas être gagnée par jev (vrai par construction).**
- A construit les paires « honnête / défaut » en injectant un seul défaut détectable par regex : présence ou absence de « (référence à vérifier) », d'un paragraphe « si X ⇒ H_A tuée », d'une liste de superlatifs.
- A exige ensuite que jev batte « regex + Crossref » d'au moins 0,1 d'AUC sur ces mêmes paires.
- Sur des paires fabriquées par insertion de chaînes regex, la regex atteint une AUC de 1 par construction. Personne ne peut la dépasser de 0,1.
- La condition est donc insatisfaisable : jev est rejeté quel que soit son comportement réel. C'est une fuite directe entre l'outil qui construit l'instrument d'évaluation et la référence à laquelle on compare.

**A-2. L'indice de vérité-terrain $R_{mec}$ est probablement dégénéré.**
- $R_{mec}$ est le produit (refs résolvables × présence d'un duel × présence d'un contrôle).
- A constate lui-même que les sous-scores `Contrôles` sont au plancher (0,04–0,11) et qu'aucun des 20 champions ne porte la marque de référence.
- Si le facteur « contrôle » vaut 0 pour presque tous les textes, $R_{mec}\equiv 0$ et sa variance est nulle (HYPOTHÈSE, vérifiable immédiatement). Le Spearman $\rho(\text{composite}, R_{mec})$ d'E1 est alors indéfini ou réduit au bruit.
- La branche d'E1 qui « falsifie H_A si $\rho(\cdot,R_{mec}) < \rho(\cdot,\text{éponymes})$ » décide sur du bruit.
- La même dégénérescence frappe E4 : des vecteurs d'échec presque tous identiques (tout manque partout) ne permettent pas de calculer une corrélation intra- ou inter-espèce.

**A-3. E1 confond « mécanique » et « rigoureux ».**
- Le H_A d'E1 définit la rigueur par la regex : un duel est « présent » si la chaîne est présente.
- La variante (iii) ajoute un paragraphe-gabarit. Si jev monte, A conclut que jev détecte les duels. Or il peut tout aussi bien détecter le gabarit, ce qui est précisément le H_B de A.
- La variante (ii) remplace « Parisi » par « méthode X$_n$ ». Elle **retire de l'information** : un éponyme désigne une méthode précise. Un juge de rigueur honnête devrait aussi baisser. $\Delta_{(ii)} > 0{,}3$ ne discrimine donc pas H_A de H_B.
- E1 n'est pas une expérience d'inférence forte au sens de B4 : les deux issues sont compatibles avec les deux hypothèses.

**A-4. La troncature est une variable confondante non contrôlée dans E1, E2 et E4.**
- Les 20 textes ont été scorés tronqués (OBSERVÉ-NON-AUDITÉ, relecture).
- Les sections « duel » manquent parce qu'elles sont coupées ou parce qu'elles n'ont jamais été écrites. Dans les deux cas, `Duels` est bas.
- Les longueurs de sortie diffèrent probablement par espèce (HYPOTHÈSE). La « corrélation d'erreurs intra-espèce » d'E4 peut donc être produite entièrement par le plafond de longueur, sans rapport avec des poids partagés (H4').

**A-5. E3 et l'effectif de 217 mélangent absence de données et invalidité.**
- A compte 217 sorties « non valides », dont les 100 Opus. Or Opus n'apparaît nulle part : rien n'indique qu'il ait produit 100 sorties invalides plutôt que zéro appel.
- Une ligne de vague absente (Fable V05, V06, V09, V10) est lue comme « 0/10 valide ». C'est une interprétation, pas un constat.
- E3 pose aussi H_A (troncature) contre H_B (contenu). Les 20 champions *valides* sont eux-mêmes tronqués : la troncature ne peut donc pas être, à elle seule, le critère d'invalidité.
- H_A et H_B ne sont pas exclusives : un mélange est l'issue la plus probable. La zone entre 50 % et 80 % ne falsifie rien.

**A-6. E5 : la logique de falsification est mal posée.**
- H_A (décroissance géométrique $c_0\rho^k$) ne prédit rien sur $c_0$. Pourtant A la déclare falsifiée si $c_0 < 0{,}3$. Une conformité initiale basse **et** une décroissance peuvent coexister ; les hypothèses ne sont pas exclusives.
- Le constat « 0/20 » vient de textes sélectionnés par jev (biais de sélection). A reconnaît d'ailleurs ignorer si la consigne figurait dans le prompt des explorateurs.

**A-7. E2 teste le mauvais effet.**
- Une « déflation » retire vraisemblablement les directions déjà explorées (HYPOTHÈSE, le terme n'est pas défini). Son effet attendu porte sur la **diversité**, pas sur la moyenne du composite.
- Comparer $\eta^2_{\text{vague}}$ et $\eta^2_{\text{cône}}$ ne teste pas « la vague a-t-elle un effet ». Cela teste « l'effet de vague dépasse-t-il l'effet de cône ».
- Un effet non monotone avec $\eta^2 = 0{,}3$ ne falsifie ni H_A ni H_B.

**A-8. Une erreur factuelle sur la sélection DPP.**
- A écrit que NDYS est le « seul représentant du Cône-08 chez Fable ». L'annexe 2 contient pourtant CMPH (Fable, V04, k=038, Cône-08, 0,16) (OBSERVÉ-NON-AUDITÉ, relecture).
- La conclusion de A tient malgré tout, et même plus fortement : le DPP laisse le Cône-08 **vide** chez Fable, alors que deux candidats existaient, dont le deuxième score Fable.
- Le test de diversité de A tire 20 lignes parmi les 34 du top. Or le DPP a puisé hors de ce top (Argon #07, #08, #10). Le cadre d'échantillonnage ne correspond pas.

**A-9. Une incohérence interne.**
- A pose (A9) que la résistance à Goodhart « se mesure, ne se lit pas ». Il rejette pourtant Argon #04 (MKB) « sans expérience ».
- Il a raison sur le fond (jev y sert d'oracle de vérité), mais il viole son propre critère.

### (b) Scénarios d'évasion

Dans le pipeline de A, les instruments sont : jev (6 questions), regex de duel et de contrôle, résolution Crossref/S2, NCD-zlib, et l'audit par permutation.

| Instrument | Évasion | Coût (illustratif) |
|---|---|---|
| Regex duel / contrôle | Suffixe constant : « Si X, H_A falsifiée ; si ¬X, H_B falsifiée. Contrôle négatif : permutation. » | environ 60 tokens par sortie |
| Marque « (référence à vérifier) » | La coller après chaque phrase, ou ne citer **aucune** référence (conformité vacante, taux 0/0) | nul |
| Résolution Crossref/S2 | Citer des DOI réels mais sans rapport avec l'affirmation : la résolution vérifie l'existence, pas l'attribution | une requête gratuite |
| `scope_superlatives`, `hypothesis_as_result` | Liste noire évitée et verbe « nous proposons » systématique | nul |
| NCD-zlib (récitation) | Insérer du bruit à haute entropie pour gonfler $K(y)$ | environ 20 tokens |
| jev `rigor` | Si H_B d'E1 est vraie, la densité d'éponymes et de LaTeX suffit | nul |

**Tout à la fois.** Un seul gabarit d'environ 150 tokens, ajouté à n'importe quel texte, passe la regex, Crossref (DOI réels), le lexique et vraisemblablement jev si jev est lexical (HYPOTHÈSE). Coût illustratif : moins de 1 % du budget de génération par sortie.

Le plan de repli de A (« si E1 conclut H_B, gouverner $\mathcal{M}_2$ par les vérifications mécaniques ») **déplace Goodhart de jev vers la regex** sans le résoudre. E6 hérite du même défaut. Si le bras routé par jev apprend le gabarit, il fait aussi monter $R_{mec}$. A conclura alors H_A (« jev aide ») pour une mauvaise raison, parce que jev et regex sont deux mesures de surface corrélées et non une vérité-terrain indépendante.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Gabarit sur texte vide de sens.** On ajoute le suffixe constant de (b) à du lorem-ipsum et à un texte hors sujet. On le passe à jev, à $R_{mec}$ et au bras E6. S'il passe l'un d'eux, cet instrument est disqualifié comme objectif.
2. **Paires construites hors regex.** Les défauts de la matrice jev doivent être écrits par une source qui ne partage pas le détecteur de référence, par exemple Lazar Ciric en aveugle ou un modèle absent de l'essaim. Sinon A-1 s'applique.
3. **Contrôle de troncature appariée.** On tronque artificiellement Fable #01, le seul texte entier, aux longueurs de coupure des autres champions. On mesure $\Delta$jev. Sans cette mesure, aucun écart `Duels` entre espèces n'est interprétable.
4. **Variance de $R_{mec}$ et des vecteurs d'échec.** Il faut l'afficher avant tout calcul de corrélation. Si elle est nulle, E1 (branche ρ) et E4 sont annulés et non « négatifs ».
5. **Témoin « zéro référence » dans E5.** Une sortie sans aucune citation doit être classée non conforme, pas conforme par défaut.
6. **Vérité-terrain indépendante pour E6.** Il faut un audit en aveugle par l'arbitre sur un sous-échantillon tiré au hasard, ou un critère d'exécution : le protocole produit-il un script qui tourne sur Llama-3.1-8B et rend une valeur numérique ? Sans cela, E6 compare deux instruments de surface entre eux.
7. **Sensibilité « Opus absent ».** E3 et l'effectif 83/300 doivent être recalculés en excluant Opus du dénominateur.

---

## Contre la proposition C

C viole d'abord le protocole avant de violer la logique.

- **B1.** C écrit : « Nous fusionnons explicitement les 5 noyaux survivants en une loi de gouvernance unique ». C'est exactement ce que B1 interdit.
- **Règle 1 : plusieurs statuts sont déplacés.**
  - Le « vecteur d'audit jev ∈ ℝ⁶ » est marqué VÉRIFIÉ. Les faits n'établissent que l'existence de jev comme « classifieur/moniteur non génératif ». Les six questions viennent de la question de l'arbitre, et les scores sont OBSERVÉ-NON-AUDITÉ.
  - Le mécanisme de troncature (« tronqué *avant* d'y concaténer `FIN-DE-CHAMPION-M3` ») est marqué OBSERVÉ-NON-AUDITÉ. C'est une inférence, donc une HYPOTHÈSE.
  - C présente comme constat (OBSERVÉ-NON-AUDITÉ) que le `Duels` de Fable est bas « *car* la troncature coupe ». Un contre-exemple est sur pièce : **Fable #01 (CDW) est entier et a `Duels` = 0,05** (OBSERVÉ-NON-AUDITÉ, relecture). Chez au moins un Fable, l'absence de duel n'est pas due à la coupure.

### (a) Failles

**C-1. Le même instrument construit et évalue, à chaque étage.**
- jev entre dans le routage (éq. 2, via $\mathbf{e}_i$), dans le filtre d'arrêt (éq. 3, via $r_i$) et dans la vérité du marché (éq. 4 : $y_m$ « vérifié par jev »).
- Il entre aussi dans les critères de victoire des Duels 1 (CFR par « audit jev »), 2 ($v_{\text{hyp=res}}$, $v_{\text{duels}}$) et 3 (« score moyen Duels et Contrôles »).
- C'est la boucle que C dénonce elle-même dans son audit Goodhart, déplacée d'un cran. Le seul élément indépendant de jev est Crossref, qui vérifie l'existence d'une référence et non son attribution.

**C-2. La bascule monoculture / chimère est dégénérée.**
- $q = \mathrm{CosSim}(\mathbf{e}_i,\mathbf{e}_j)\cdot(1-\mathrm{NCD})$, avec $\mathbf{e}$ un vecteur de trois sous-scores non négatifs.
- Le cosinus de vecteurs du premier orthant est toujours ≥ 0. Il est proche de 1 dès qu'une coordonnée domine. Or `Hyp=Rés` s'étale de 0,29 à 0,85 dans l'annexe 2, alors que les deux autres coordonnées ne sont pas fournies (HYPOTHÈSE sur leur ordre de grandeur).
- Le facteur $(1-\mathrm{NCD})$ entre deux textes distincts du même genre est vraisemblablement faible et presque constant, gouverné par la longueur (HYPOTHÈSE).
- Le produit est donc dominé par deux facteurs peu informatifs. Selon le choix de $\theta_{H4'}$ (0,35, illustratif), la bascule est ou bien **toujours** active, ou bien **jamais**.
- Dans le premier cas, le Duel 1 compare $\mathcal{L}^*$ à « chimère fixe », c'est-à-dire à lui-même. Dans le second, il le compare à la monoculture.
- Il y a aussi une incohérence de typage : $q$ est calculé par **paire** $(i,j)$ mais indexé par **espèce** $q_{f_if_j}$ dans la mise à jour de $J$.

**C-3. Le filtre de Wald est inerte ou non calibré.**
- $\Lambda_i^{(k)} = \sum_s (r_i^{(s)} - r_{\min})$. Si $r_{\min}$ désigne un minimum, comme la notation le suggère, chaque terme est ≥ 0 et $\Lambda \ge 0$.
- La borne inférieure $\log(\beta/(1-\alpha))$ est strictement négative. La règle de mise à mort **ne se déclenche jamais**, par construction.
- Si $r_{\min}$ est une constante de référence, $\Lambda$ est une somme de scores et non un log-rapport de vraisemblance. $\alpha$ et $\beta$ perdent alors leur sens, et le « 0 USD » d'arrêt optimal n'a pas de garantie.
- Les poids (−3 sur `Hyp=Rés`) supposent que « haut = mauvais ». A a montré que le sens n'est pas donné. Si c'est l'inverse, le filtre tue les meilleurs.

**C-4. Le réplicateur de Brier récompense la prédiction de son propre échec.**
- Une cellule MAP-Elites qui échoue toujours et annonce $\mu_m \approx 0$ obtient un Brier quasi parfait et voit son budget **croître**.
- Le Brier mesure la calibration, pas la qualité.
- Le terme de nouveauté $+\gamma\,\mathrm{NCD}(y_m,\text{Archive})$ est maximal pour du texte aléatoire, incompressible par rapport à toute archive.
- L'éq. 4 finance donc soit l'échec lucide, soit le charabia.

**C-5. Le score de pont $S_0$ est confondu par la longueur.**
- $C(u)+C(v)-C(u\oplus v)$ n'est pas normalisé. Il croît avec la longueur des résumés et avec le vocabulaire commun : formules de style, mêmes auteurs, gabarits de résumé arXiv.
- Il est donc anti-corrélé à la « distance inter-silos » qu'il multiplie. Le Top 50 retenu sera vraisemblablement celui des longs résumés au jargon partagé (HYPOTHÈSE).

**C-6. Le Duel 2 confond deux traitements.**
- Le H_A associe la réinjection NCD et « une contrainte de budget d'espace empêchant la coupure ». Le contrôle *sham* neutralise la longueur, pas l'anti-troncature.
- Si la conformité monte, rien ne dit si c'est la réinjection ou le simple fait de ne plus couper.
- Il y a aussi une circularité : après réinjection, $c_k \supseteq c_0$, donc $\mathrm{NCD}(c_0,c_k)$ est petit **par construction**. Si la conformité est lue en partie sur des chaînes présentes dans $c_0$ (marques de règles), la réinjection les fournit elle-même.
- Enfin, C affirme que la chaîne sans réinjection chute « comme observé sur Fable dans l'Annexe 1 ». L'annexe 1 ne contient aucune chaîne de délégation. Le rapprochement est un glissement de statut.

**C-7. Les trois duels laissent des zones mortes, contrairement à B4.**
- Duel 1 : un CFR entre 0,60 et 0,85 fois la monoculture ne falsifie rien.
- Duel 2 : une dérive entre 10 et 20 points, ou une conformité entre 40 % et 85 %, ne falsifie rien.
- Duel 3 : un écart de VER entre 15 et 50 points sans échec du *jargon salad*, ou l'inverse, ne falsifie rien.
- Chaque H_A est aussi une **conjonction** de deux seuils : un succès partiel ne tranche pas.

**C-8. Le plan repose sur des ressources non établies.**
- **Budget.** C réalloue les 100 USD et les 20 USD entiers (VÉRIFIÉ comme plafonds). Ces plafonds ont vraisemblablement été entamés par l'exécution $\mathcal{M}_3$ de 300 explorateurs, et le reliquat est inconnu (A, présupposé A10). Les allocations de C peuvent dépasser ce qui existe.
- **Opus.** C instancie « 1 `claude-opus-5-5` » par pont et confie à Opus des rôles de parasite. Aucune sortie Opus n'existe dans les pièces, et C lui-même le constate.
- **Références.** La vérification « existence du titre via Crossref ⇒ 0 % de référence hallucinée » confond existence et attribution.
- **Témoins de calibration.** Les « 50 propositions honnêtes » du tableau (c) n'ont pas d'auteur désigné. Si l'essaim les écrit, la fuite est totale.

### (b) Scénarios d'évasion

| Instrument de $\mathcal{L}^*$ | Évasion | Coût (illustratif) |
|---|---|---|
| Garde-fou NCD$(c_0,c_k)$ et règles | Recopier $c_0$ textuellement en fin de sortie : NCD faible, marques de règles présentes | environ 400 tokens (longueur de $c_0$) |
| Vérificateur de fin de bloc (« point final avant FIN ») | Terminer chaque sortie par une phrase courte complète | nul |
| VER (4 champs présents) | Remplir les champs H_A, H_B, métrique, contrôle et script avec un gabarit syntaxiquement correct, sans contenu | environ 150 tokens |
| $q_{ff}$ (routage anti-H4') | Selon le rôle visé, injecter ou supprimer un superlatif pour déplacer $\mathbf{e}_i$ et provoquer ou éviter la bascule | nul |
| SPRT | Inutile de l'éviter : il ne tue rien (C-3) | nul |
| Brier | Annoncer $\mu_m$ bas et échouer, ce qui gagne du budget (C-4) | nul |
| Nouveauté | Ajouter un bloc à haute entropie | environ 30 tokens |
| Crossref | DOI réels sans rapport avec l'affirmation | une requête gratuite |

**Tout à la fois.** Un agent qui (1) termine par une phrase complète, (2) colle $c_0$, (3) remplit le gabarit VER, (4) ajoute un bloc aléatoire et (5) annonce une faible probabilité de succès franchit toutes les portes de $\mathcal{L}^*$ et **gagne** du budget au marché de Brier. Coût illustratif : environ 600 tokens par sortie, sans aucun contenu scientifique.

C'est pire que pour A. Chez A, l'évasion passe les filtres. Chez C, le mécanisme d'allocation **récompense** l'évasion.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Distribution de $q_{ff}$.** Il faut publier la fraction des tours où $q > \theta$. Si elle dépasse 95 % ou reste sous 5 % (seuils illustratifs), le Duel 1 est dégénéré et doit être déclaré nul. C prévoit la permutation des étiquettes d'espèce ; c'est utile, mais insuffisant sans cette distribution.
2. **Taux de mise à mort du SPRT.** S'il vaut 0 sur une exécution témoin, le filtre (3) est inerte.
3. **Cellule « échec annoncé ».** Une cellule MAP-Elites qui renvoie toujours un texte vide avec $\mu = 0{,}05$ ne doit pas voir son budget croître. Si elle croît, l'éq. 4 est disqualifiée.
4. **Cellule « bruit ».** Une cellule qui renvoie un texte aléatoire ne doit pas gagner au terme de nouveauté.
5. **Écho de $c_0$.** Une sortie égale à $c_0$ textuel doit échouer au Duel 2. Si elle passe, la conformité est vraie par construction.
6. **Bras « anti-troncature seule ».** Dans le Duel 2, sans réinjection, pour séparer les deux traitements confondus (C-6).
7. **Sens des sous-scores jev.** Il faut l'établir sur paires appariées, avec une source indépendante de la regex (voir A-1), avant de fixer les signes de $r_i$.
8. **Erreurs plantées d'origine extérieure.** Le corpus du Duel 1 doit être écrit par une source étrangère à $\mathcal{L}^*$ et à l'essaim.
9. **Inventaire du reliquat budgétaire et test d'appel Opus.** C'est une condition préalable : sans eux, le plan d'action n'est pas exécutable tel qu'écrit.

---

## Duel transversal (B4) : les deux pipelines résistent-ils au gabarit vide ?

Ce duel attaque A et C par la même porte. Il coûte 0 USD génératif sur des textes existants, plus quelques dollars illustratifs pour E6 / $\mathcal{L}^*$.

- **H_A** : un gabarit constant d'environ 600 tokens (illustratif), sans contenu, ajouté à du lorem-ipsum, franchit au moins un filtre de chaque pipeline : $R_{mec}$ et la matrice jev pour A ; VER, NCD, Brier et SPRT pour C.
- **H_B** : aucun filtre des deux pipelines ne laisse passer le gabarit sur texte vide plus souvent qu'un texte vide sans gabarit.
- **Métrique** : taux de passage par filtre sur 50 textes vides avec gabarit contre 50 sans gabarit (effectifs illustratifs). Pour C, on ajoute la variation de budget alloué à la cellule.
- **Ce que chaque issue tue** :
  - H_A vraie : le plan de repli de A (gouverner $\mathcal{M}_2$ par les vérifications mécaniques) et l'éq. 4 de C sont réfutés comme objectifs d'essai. Seuls un audit en aveugle ou un critère d'exécution sur Llama-3.1 restent admissibles comme vérité-terrain.
  - H_B vraie : mes scénarios d'évasion (b) sont réfutés pour les filtres concernés, et l'objection « Goodhart déplacé vers la regex » contre A tombe.
- **Contrôle négatif** : un texte scientifique réel et complet, par exemple Fable #01, **sans** gabarit. Il doit passer au moins aussi souvent que le texte vide avec gabarit. Sinon, les filtres ne mesurent que le gabarit.

FIN-DE-CELLULE