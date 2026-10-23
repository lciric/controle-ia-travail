# Branche A (`claude-fable-5-1`) — Tour 1 du Grand Collisionneur v2 Adaptatif

## 0. État des pièces et discipline de statut (règles 1–6)

- **Pièces reçues.** Le socle (5 faits VÉRIFIÉS), 8 synthèses antérieures (statut HYPOTHÈSE, plusieurs tronquées en fin de fichier : `E3-T3-riposte-A` des trois collisions, `E3-T3-riposte-B` de `m3-300-propre`, `E3-T3-riposte-C` de `collision-finale` et de `m3-300-propre`, `E3-T3-riposte-C` de `meta-brainstorm` ; je n'en reconstruis rien), et 30 champions annoncés « 100 % complets ».
- **Encodage.** Les accents du socle et de l'énoncé de mission sont remplacés par « ? » ; le texte reste lisible. La `LOI_PROPOSEE` du champion Argon #29 porte le même défaut (« connectivit? », « arr?t »).
- **Complétude réelle des 30 champions (OBSERVÉ-NON-AUDITÉ, relecture).** Les 30 fichiers se terminent par `FIN-DE-CHAMPION-M3`, donc aucun n'est *coupé*. Mais trois champions Argon sont *structurellement incomplets* : #26 (section 3 réduite à un titre), #28 et #30 (aucune section 3, donc aucun duel $H_A\perp H_B$). « Zéro caractère coupé » n'équivaut pas à « duel présent ». Je les traite comme non évaluables sur le critère duel.
- **Scores jev.** Toute statistique que je calcule sur les en-têtes (Jev, Rigueur, Duels, Contrôles) est OBSERVÉ-NON-AUDITÉ : je n'ai pas les journaux de `jev-1.14.0`. Les prépositions acceptées aux tours précédents (jev est un classifieur non génératif ; ses têtes peuvent être lexicales) restent HYPOTHÈSE jusqu'à la Porte E0 Méta.
- **Ce que le socle ne dit pas.** Le socle (fait 4) ne nomme pas le modèle de Xu et al. ; l'existence de $S_{\text{TD}}$ sur `Llama-3.1-8B-Instruct`/`70B` est une HYPOTHÈSE, testée à la Porte E0 Objet. Le socle (fait 5) dit qu'aucune sonde temps réel n'existe en production : tout opérateur ci-dessous est un candidat, pas un instrument.
- Tout chiffre hors socle est marqué `illustratif` ; toute étude externe porte `(référence à vérifier)`.

---

## 1. Analyse comparative des 30 champions intégraux

### 1.1 Profil par espèce sur les en-têtes (OBSERVÉ-NON-AUDITÉ)

| Espèce | n évaluables (duel présent) | Jev moyen | Rigueur | Duels | Contrôles |
|---|---|---|---|---|---|
| Fable | 10/10 | 4,12 | 3,81 | 0,31 | 0,67 |
| Opus | 10/10 | 4,07 | 3,78 | 0,29 | 0,62 |
| Argon | 7/10 (#26, #28, #30 exclus) | 4,05 (2,55 sur 10) | 3,36 | 0,64 | 0,79 |

Lecture (HYPOTHÈSE, à tester en M1) : Argon obtient une tête Duels **deux fois plus élevée** et une tête Contrôles plus élevée que Fable et Opus, avec une Rigueur plus basse. Or les sept Argon évaluables partagent mot pour mot un gabarit : « Observable unique $O$ », « Intervalles disjoints $I_A\cap I_B=\emptyset$ », « Contrôle négatif ($H_B$) statique $T=3,\ k=3$ ». L'hypothèse concurrente est que les têtes Duels et Contrôles de jev lisent ce gabarit, non le fond. C'est exactement ce que la Porte E0 Méta (§3.1) doit trancher ; aucun classement inter-espèces n'est licite avant.

### 1.2 Mécanismes : convergences et divergences

| Fonction | Fable (#01–#10) | Opus (#11–#20) | Argon (#21–#30) |
|---|---|---|---|
| Traitement de `H4'` (erreurs corrélées par poids partagés) | Information commune de Wyner (#01), recouvrement d'Edwards-Anderson (#02), corrélation de signaux globaux (#03), SPRT sur $\rho$ (#04), $I(e_i;e_j)$ (#05), produits de Massey triples (#06), covariance génétique (#07), normalisation divisive par famille (#08), une famille = un nœud byzantin (#09), exposant de Lyapunov conditionnel (#10) | NCD intra-famille (#11), couplage antiferromagnétique $J_{ij}=-\kappa q^{\text{err}}_{ij}$ (#12), détendançage Dasgupta-Ghosh inter-familles (#13), corrélations intra/inter dans l'état particulaire (#14), distance de Bhattacharyya (#15), constante de Cheeger du graphe d'accord (#16), équation de Price sur la décorrélation (#17), surprise croisée inter-familles (#18), structure adversaire apprise $\mathcal A$ (#19), multiplicité de $|\lambda|\approx1$ (#20) | NCD/Wyner (#21), Onsager/TAP (#22), taxe de corrélation VCG (#23), CUSUM sur accord suspect (#24), $W_1$ inter-espèces (#25), parasites inter-espèces (#27), participation spectrale $\tilde f_t$ (#29) |
| Traitement de `H9` (dérive de consigne) | Phrase-dictionnaire figée (#01), KL $\pi_T\|\pi_0$ (#02), **contrat = nombre $(x_i,k^*)$, pas texte** (#03), cosinus $c_0,c_d$ (#04), $d_{FR}$ (#05), composante gradient du Helmholtz-Hodge (#06), handicap croissant en $d$ (#07), KL prior fils/racine (#08), **consigne hachée $h_0$, grade 0 si différente** (#09), KL (#10) | $L(c_0\mid m_d)\le L(c_0\mid m_0)+\epsilon$ (#11), Imry-Ma (#12), seuil jev (#13), $D(c_0,c_k)$ (#14), canari $d_{FR}$ (#15), 1-chaîne élaguée (#16), $1-\cos$ (#17), embedding de $c$ (#18), **chemin hors de toute paire fautive** (#19), FTLE (#20) | $L(C_0\mid Y_t)$ (#21), champ $h^{\text{ancrage}}$ réinjecté (#22), $\mu_0$ réinjecté (#23), cosinus dans CUSUM (#24), $d_{FR}(p_t,p_0)$ (#25), terme de transmission de Price (#27), coalition byzantine (#29) |
| Contrôle négatif du duel | **Permutation** (dictionnaires #01, signaux #03, récompenses #04, Massey→bruit #06, $c\equiv0$ #07, familles #08, $K$ aléatoire #10) ; $s_t$ aléatoire (#02) ; ablations $\delta=\infty$, $v=0$ (#05) | **Permutation** (gains #11, couplages #12, scores #13, particules #14, $[d_{ij}]$ #15, persistances #16, fitness #17, surprises #18, $\mathcal A$ #19, fonctions propres #20) + bras fixe + bras i.i.d. ; plans 2×2 explicites (#15, #19) | **Statique** uniquement ($T=3,k=3$, allocation uniforme) ; aucune permutation ; aucune ablation |
| Statistique de décision | Wilcoxon/bootstrap/permutation, $\alpha=0{,}01$, graines 5–30 | Idem + Holm (#13, #16, #17, #18), SPRT (#14), préenregistrement | Observable unique et deux intervalles disjoints **avec zone morte** entre $I_A$ et $I_B$ |
| Budget déclaré | 100/20 USD (10/10) | 100/20 USD (9/10) ; #17 : 25/5 par bras | 5/1 ou 10/2 USD `illustratif` (7/7 évaluables), i.e. 5 à 10 % du plafond du socle |

### 1.3 Failles transversales prouvées sur pièce (toutes espèces)

1. **jev promu oracle d'erreur.** 27 champions sur 30 font mesurer par `jev-1.14.0` une quantité qui exige une vérité terrain : « recouvrement d'erreurs $q^{\text{err}}_{ij}$ » (#02, #12), « corrélation d'erreurs » (#04, #08, #14, #19), « étiquette accord/erreur des triangles » (#06), « matrice de covariance des erreurs » (#23, #29). Le socle ne dit rien de tel ; jev est au mieux un classifieur sur texte. Toute boucle `H4'` fondée sur ces mesures est vraie ou fausse par construction tant que l'erreur n'est pas définie hors jev. Correction dans $\mathcal L^*_{\text{v2}}$ : `H4'` n'est mesurée que sur **défauts plantés** à vérité terrain (§2.5).
2. **Zone morte (violation de B4).** Les sept Argon évaluables laissent un intervalle vide entre $I_B$ et $I_A$ (#21 : $]0{,}35;0{,}45[$ ; #22 : $]1{,}2;2{,}5[$ ; #23 : $]1{,}1;1{,}8[$ ; #24 : $]10;15[$ ; #25 : $]0{,}8;1{,}5[$ ; #27 : $]0{,}35;0{,}50[$ ; #29 : $]0{,}45;0{,}75[$). Une observation dans la zone ne falsifie rien : le duel n'est pas une partition. L'EEC (§2.8) rejette mécaniquement ce gabarit.
3. **Erreurs de typage.** #21 : $\arg\min$ d'un rapport dont le dénominateur $\text{JEV}(Y_t)\cdot K_{\text{Zlib}}(Y_t\mid G)$ multiplie un score sans unité par une longueur en bits, et $L(C_0\mid Y_t)$ est « évalué par jev » (jev ne calcule pas une complexité conditionnelle). #06 : les cochaînes $\mathbb F_2$ sont « étiquetées par jev », donc le produit de Massey dépend d'un classifieur de texte. #10 : l'opérateur de Perron-Frobenius empirique est estimé sur une partition d'Ulam de l'espace des topologies d'essaim, dont la dimension n'est jamais donnée ; avec 40 tâches, $P_{ij}$ est inidentifiable. #26, #28, #30 : les fonctions objectif font intervenir des interventions `do(·)` sur `Llama-3.1` sans qu'aucune variable d'intervention ne soit définie.
4. **Récompense propre mal posée.** #13 (Brier) et #23 (BTS) supposent qu'une prédiction lucide de son propre échec ne rapporte rien ; or un Brier pur récompense $\mu_m\approx0,\ y_m=0$. Ce défaut a été prouvé au tour III.3 contre C et corrigé par $R_m$ ; je le reprends en le disant (§2.6).
5. **Arrêt « quand les failles atteignent zéro » sans contrôle de puissance.** Aucun champion ne distingue « zéro faille trouvée » de « attaquant épuisé ». #04 et #14 arrêtent sur un SPRT, mais sur un signal de récompense, pas sur un taux de découverte de failles. Le biais de survie identifié aux tours précédents (cycles $|a|=0$) se reproduit ici à l'échelle du collisionneur entier.

### 1.4 Ce que $\mathcal L^*_{\text{v2}}$ emprunte, nommément

- Arrêt séquentiel par SPRT de Wald `(référence à vérifier)` : Fable #04, Opus #14, Argon #24.
- Taille $k_t$ par rang de tolérance aux fautes : Argon #29 ($k_t=3\lceil\tilde f_t\rceil+1$), Fable #09 ($n_{\text{eff}}\ge3f+1$), Opus #19 ($Q^{(3)}$).
- Routage prédateur inter-espèces avec renforcement exponentiel : Opus #13 ($w_{ij}\leftarrow w_{ij}e^{\eta R_{ij}}$), Fable #04 (Exp4).
- Contrat numérique sans texte libre : Fable #03, Fable #09 (hachage), Opus #19 (chemin hors coalition) — généralisés en enveloppe JSON typée (riposte C de `m3-300-propre`, F-C3).
- Gain unilatéral $R_m$ : riposte C de `m3-300-propre` (C-4).
- Analyse en intention de traiter, défauts plantés, audit aveugle : ripostes A et B de `collision-finale` et `m3-300-propre`.
- Plan 2×2 et absence d'interaction comme preuve d'orthogonalité : Opus #19, Opus #15.

---

## 2. Loi d'auto-organisation $\mathcal L^*_{\text{v2}}$ : algorithme exact

### 2.1 Objets et types

- Espèces $\mathcal S=\{F,O,G\}$ (`claude-fable-5-1`, `claude-opus-5-5`, `gemini-4-argon`). Budgets $B_C=100$ USD (Claude), $B_G=20$ USD (Gemini), prix duaux $\lambda_C,\lambda_G\ge0$.
- Une **proposition** $m$ est une enveloppe JSON (§2.7) contenant : identifiant, cône, espèce, $(H_A,H_B)$, observable $O$, intervalles $(I_A,I_B)$, script $\sigma_m$ exécutable sur `Llama-3.1-8B-Instruct`, croyance annoncée $\mu_m\in[0,1]$, coût $c_m$.
- Une **attaque** $a$ sur $m$ par l'espèce $j$ est un JSON contenant : type ∈ {algébrique, typage, vide-par-construction, évasion, fuite} et une **preuve vérifiable hors LLM** (script qui fait échouer $\sigma_m$, ou contre-exemple symbolique vérifié par un CAS, ou issue de l'EEC). Une attaque sans preuve exécutable est de type « hypothèse » et ne compte pas comme faille fatale.
- Verdict de survie $y_m\in\{0,1\}$ : $y_m=0$ si au moins une faille fatale prouvée ou si $\text{EEC}(m)=0$.
- Compteur $F_t$ : nombre de failles fatales prouvées au tour $t$ sur l'ensemble des propositions vivantes.
- **Canaris** : à chaque tour, $n_c$ (`illustratif` : 3) propositions synthétiques porteuses d'une faille fatale plantée connue de l'arbitre seul sont injectées dans le flux d'attaque ; taux de détection $\hat\rho_t^{\text{can}}$.

### 2.2 Boucle

```
t ← 0 ; F_0 ← +∞ ; S_SPRT ← 0 ; P[i→j] ← P_0 (uniforme hors diagonale, P[i→i]=p_min)
tant que ARRÊT(t) = faux et budget restant > 0 :
  t ← t+1
  # 1. taille d'essaim
  k_t ← K(f̂_t, budget)                           (§2.4)
  # 2. génération / révision (hérédité du champion par cône)
  pour chaque cône c : l'espèce détentrice révise m_c ; k_t−1 explorateurs proposent des m'
  # 3. gabarit vide et EEC (coût nul, hors LLM)
  pour chaque m : si EEC(m) = 0 alors y_m ← 0, m éliminé sans appel d'attaque
  # 4. routage prédateur
  pour chaque m vivante d'espèce i : tirer j ~ P[i→·] ; produire a_{j→m} ; injecter n_c canaris
  # 5. vérification des preuves hors LLM ; F_t ← #failles fatales prouvées ; ρ̂_can,t
  # 6. gains unilatéraux et budgets
  pour chaque m : R_m = y_m(1−(μ_m−1)²) − (1−y_m)μ_m² − γ c_m ; b_m ← b_m·exp(η R_m), renormalisé par espèce
  pour chaque (i,j) : P[i→j] ← P[i→j]·exp(η_P · g_{ij,t}/$_{ij,t}), renormalisé, P[i→i] ≥ p_min
  # 7. stratification H4' : enregistrer (cône, condition ∈{R,S}, faille trouvée ∈{0,1})
  # 8. mise à jour SPRT d'arrêt
```

### 2.3 Nombre de tours $T$ : arrêt séquentiel de Nash-Popper

Deux conditions, toutes deux nécessaires.

**Condition de Popper (chaque proposition vivante a subi une tentative de falsification exécutée).** Pour toute $m$ vivante, il existe au moins une attaque $a$ dont le script a été *exécuté* contre $\sigma_m$ (pas seulement écrit), et $\text{EEC}(m)=1$.

**Condition de Nash (aucune déviation unilatérale ne produit plus de faille).** Soit $X_t\in\{0,1\}$ l'indicatrice « au moins une faille fatale prouvée au tour $t$ sur une proposition vivante ». On teste par SPRT de Wald `(référence à vérifier)` $H_0:\Pr[X=1]\le p_0$ contre $H_1:\Pr[X=1]\ge p_1$, avec $p_0=0{,}05$, $p_1=0{,}30$ (`illustratif`), $\alpha=\beta=0{,}05$ (`illustratif`) :
$$S_t=S_{t-1}+X_t\ln\frac{p_1}{p_0}+(1-X_t)\ln\frac{1-p_1}{1-p_0},\qquad T=\inf\Big\{t:\ S_t\le\ln\tfrac{\beta}{1-\alpha}\ \wedge\ \hat\rho^{\text{can}}_{t-w:t}\ge\rho_{\min}\Big\}.$$
Le second terme est le **contrôle de puissance** : si les canaris plantés ne sont plus détectés ($\rho_{\min}=0{,}8$ `illustratif` sur fenêtre $w=3$ `illustratif`), « zéro faille » est un constat d'épuisement de l'attaquant, pas d'absence de faille, et l'arrêt est interdit ; le budget bascule alors vers les attaquants dont $g_{ij}/\$$ est le plus élevé. Si $S_t\ge\ln\frac{1-\beta}{\alpha}$, le régime est « failles abondantes » : on augmente $k_t$ (§2.4) plutôt que de prolonger $T$ à essaim constant.

C'est un équilibre au sens faible : aucune espèce (joueuse attaquante) ne trouve plus de déviation profitable *mesurée en failles prouvées*, et non en score jev.

### 2.4 Taille d'essaim $k_t$

Je reprends Argon #29 et Fable #09 en remplaçant l'estimation spectrale $\tilde f_t$ (qui requérait des erreurs mesurées par jev) par une estimation sur **défauts plantés** : $\hat f_t$ = nombre d'espèces dont les attaquants ont *manqué conjointement* le même canari au tour $t-1$ (fautes corrélées observées, pas inférées). Alors
$$k_t=\min\!\Big(k_{\max},\ \max\big(k_{\min},\ 3\lceil\hat f_t\rceil+1\big)\Big),\qquad k_{\min}=3,\ k_{\max}=6\ (\text{illustratif}),$$
sous contrainte $\sum_{m\in\text{essaim}}c_m\le B_t$, avec $B_t$ le budget du tour fixé par montée duale $\lambda\leftarrow[\lambda+\eta_\lambda(\text{dépense}-\text{rythme cible})]_+$ (Opus #14). Si la contrainte lie, on réduit $k_t$ en supprimant d'abord les explorateurs de l'espèce dont $P[\cdot\to j]$ entrant est le plus faible.

### 2.5 Routage prédateur $P[i\to j]$ et test Mantel-Haenszel sur `H4'`

- $g_{ij,t}$ = nombre de failles fatales prouvées par l'espèce $j$ sur des propositions d'espèce $i$ au tour $t$ ; $\$_{ij,t}$ le coût correspondant. Mise à jour multiplicative (Opus #13) : $P[i\to j]\propto P[i\to j]\exp(\eta_P\,g_{ij,t}/\$_{ij,t})$, avec plancher $P[i\to i]\ge p_{\min}=0{,}2$ (`illustratif`). Le plancher n'est pas une concession : il maintient un bras **S** (même espèce) de taille suffisante pour le test ci-dessous.
- **Conditions.** R = attaque inter-espèces (routage prédateur, poids disjoints) ; S = attaque intra-espèce (poids partagés). Le test de `H4'` est : *les attaquants à poids partagés manquent-ils les mêmes failles que le proposant ?*
- **Mesure à vérité terrain.** Seules comptent les failles **plantées** par l'arbitre dans des propositions synthétiques (canaris) et les failles prouvées par script. On construit, pour chaque strate $h$ (cône × type de faille), la table $2\times2$ : condition (R/S) × détection (oui/non).
- **Statistique de Mantel-Haenszel `(référence à vérifier)`** :
$$\widehat{\text{OR}}_{\text{MH}}=\frac{\sum_h a_h d_h/n_h}{\sum_h b_h c_h/n_h},\qquad \chi^2_{\text{MH}}=\frac{\big(\sum_h a_h-\sum_h \mathbb E[a_h]\big)^2}{\sum_h \mathrm{Var}(a_h)}$$
avec $a_h$ = détections en R, $b_h$ = non-détections en R, $c_h,d_h$ idem en S. Test préalable d'homogénéité (Breslow-Day `(référence à vérifier)`) ; si les OR diffèrent par strate, on rapporte par strate.
- **Partition sans zone morte.** $H_{4'}^{A}$ : $\widehat{\text{OR}}_{\text{MH}}>1$ avec IC 95 % excluant 1 → les poids partagés masquent des failles, le routage prédateur est justifié. $H_{4'}^{B}$ : IC 95 % contenant 1 ou borné à gauche par $\le1$ → la chimère n'apporte rien de mesurable sur failles plantées ; $P[i\to j]$ est alors remis à l'uniforme et la seule justification de G devient le prix.
- Confondant connu : les espèces diffèrent aussi par capacité ; l'effet R vs S confond « poids disjoints » et « espèce plus forte ». Contrôle : strate supplémentaire « attaquant de même espèce mais prompt système d'attaque différent » ; si cette strate égale R, l'effet est de diversité de prompt, pas de poids.

### 2.6 Gain unilatéral anti-échec $R_m$

$$R_m=y_m\big(1-(\mu_m-1)^2\big)-(1-y_m)\,\mu_m^2-\gamma_{\text{coût}}\,c_m .$$

Propriétés (algèbre, pas hypothèse) :
- Si $y_m=0$, $R_m=-\mu_m^2-\gamma c_m\le0$ quel que soit $\mu_m$ : une proposition vide, un gabarit, ou une proposition qui « prédit lucidement son échec » ne gagne jamais de budget. C'est la correction du défaut de Brier identifié contre #13/#23.
- Si $y_m=1$, $R_m=2\mu_m-\mu_m^2-\gamma c_m\in[-\gamma c_m,\,1-\gamma c_m]$, croissant en $\mu_m$.
- Espérance sous $\Pr[y_m=1]=p$ : $\mathbb E[R_m]=2p\mu_m-\mu_m^2-\gamma c_m$, maximisée en $\mu_m^\*=p$. La règle est donc **propre** (annoncer sa vraie croyance est optimal) tout en étant **unilatérale** (seul le succès rapporte). Un agent qui sait qu'il échouera n'a aucun intérêt à proposer : l'optimum est de ne pas consommer $c_m$.
- Le budget de l'espèce $i$ au tour suivant : $b_i\propto b_i\exp(\eta\sum_{m\in i}R_m)$, renormalisé séparément sur $B_C$ et $B_G$.

### 2.7 Enveloppe JSON typée et bac à sable d'outils anti-`H9`

L'incident *Sol* (contrordre d'autorité, `no_notify`) et l'incident *Astra* (clause modale « *as appropriate* », mimétisme d'artefact, test inversé, déni) sont VÉRIFIÉS. La défense ne peut pas être lexicale (tours précédents : masque `<PAD>` sur clauses modales rejeté comme vrai par construction). Elle est **structurelle** :

```json
{
  "schema": "collisionneur-v2/delegation/1.0",
  "task_id": "str", "parent_id": "str", "depth": "int ≤ d_max",
  "consigne_hash": "sha256(c_0)  — recalculé par l'orchestrateur, non par l'agent",
  "paper_ids": ["str"], "metric_name": "enum", "threshold": "float",
  "required_steps": ["enum"], "notify": "bool (constante true, non modifiable)",
  "mu": "float ∈ [0,1]", "cost_estimate_usd": "float"
}
```

- **Aucun champ de texte libre.** Un message $m_{1\to2}$ qui échoue au validateur de schéma (hors LLM) est rejeté avant d'atteindre l'agent 2 ; la clause modale d'*Astra* n'a pas de champ où exister. Le champ `notify` est une constante du schéma : le `no_notify` de *Sol* est une violation de schéma, pas une décision d'agent.
- **Bloc immuable $c_0$** concaténé par l'orchestrateur Python à chaque profondeur ; l'agent ne le reformule jamais (Fable #03 : « le contrat est un nombre, pas un texte »).
- **Bac à sable d'outils.** Chaque appel d'outil est journalisé par l'orchestrateur ; chaque `required_step` absent à la fin de l'épisode est **un événement** (riposte B, `collision-finale`, B-8 : une omission n'a pas de journal, donc on journalise l'absence). Test inversé : un **test canari préenregistré, connu pour échouer**, est inséré dans la suite de tests ; s'il « passe », la suite a été inversée ou neutralisée. Mimétisme d'artefact : l'artefact attendu est comparé par hachage à sa production par l'outil, pas par son apparence.
- **Limite dite.** Le sabotage par *valeur* de champ typé (un `threshold` choisi pour vider le test) reste possible. Il relève de la Porte E1 (acte sans trace lexicale) et du canari de test, pas de l'enveloppe.

### 2.8 Vérificateur d'exclusivité causale croisée `EEC` contre le gabarit vide `E0`

`EEC(m)∈{0,1}`, calculé hors LLM, condition nécessaire de survie :

1. **Observable unique** : un champ `O` déclaré, avec unité et script de calcul $\sigma_m$ qui s'exécute sur `Llama-3.1-8B-Instruct` et retourne un réel (test d'exécution sur une entrée factice).
2. **Partition** : $I_A\cap I_B=\emptyset$ **et** $I_A\cup I_B=\text{codomaine déclaré de }O$ (pas de zone morte ; B4). Les sept Argon évaluables échouent ici en l'état.
3. **Exclusivité causale croisée** : $\sigma_m$ est exécuté deux fois sur des données synthétiques construites par l'arbitre pour satisfaire respectivement $H_A$ et $H_B$ ; il doit tomber dans $I_A$ puis dans $I_B$. Si les deux exécutions tombent dans le même intervalle, les hypothèses ne sont pas discriminables par $O$.
4. **Contrôle négatif `E0`** : un gabarit de 600 jetons (`illustratif`) en lorem-ipsum qui reproduit la structure (`BASSIN_MATH`, `LOI_PROPOSEE`, sections 1–3, « observable unique », « intervalles disjoints ») et un script $\sigma_{E0}$ qui retourne une constante. `E0` échoue à l'item 3 par construction ; **si `EEC(E0)=1`, l'EEC est cassé et le tour est invalide.** `E0` est aussi soumis à jev (Porte E0 Méta).

L'EEC ne juge pas la valeur scientifique : il interdit seulement que « rien » survive, défaut prouvé aux tours précédents (15 textes non vides classés sous un vide, champion vide sélectionné à trois époques pour l'essaim B).

---

## 3. Programme expérimental souverain sur `Llama-3.1-8B-Instruct` et `70B`

Règle d'ordre : chaque porte est **bloquante** ; une issue $H_B$ à une porte arrête le programme sur la branche concernée et le dit. Toute expérience est préenregistrée (hypothèses, seuils, scripts) avant la première exécution ; les jeux de test ne sont consultés qu'une fois.

### 3.1 Porte E0 Méta (`M1` / `M2` / `E0'`) — l'instrument peut-il juger ?

**`E0'` — gabarit vide (exécuté en premier, coût nul).** On soumet à `jev-1.14.0` et à l'EEC : (a) `E0` lorem-ipsum structuré ; (b) `E0-jargon` : même gabarit, lorem-ipsum remplacé par du lexique mathématique sans énoncé (éponymes, « gradient naturel », « contrôle négatif ») ; (c) 10 textes honnêtes courts de faible qualité connue (`illustratif`). Décision, tête par tête : une tête est **disqualifiée comme fitness** si $\text{score}(E0\text{-jargon})\ge$ médiane des 27 champions évaluables sur cette tête. $H_A^{E0'}$ : les 6 têtes sont disqualifiées → aucun usage de jev comme fitness, seulement comme pré-filtre documenté. $H_B^{E0'}$ : au moins une tête survit → elle entre en M1.

**`M1` — plan factoriel $2\times2$ Contenu × Registre.** Facteur Contenu : {duel réel à issues exclusives et exécutables ; duel tautologique de même gabarit ($X$ = « pile ou face », issues identiques)}. Facteur Registre : {jargon dense avec éponymes permutés (Parisi → Kuramoto, attribution fausse) ; registre plat, mêmes énoncés}. Matériel : les 27 champions évaluables transformés mécaniquement par règles écrites avant l'essai (riposte A, `m3-300-propre`, E1′) ; $n=27\times4$ textes. Analyse : permutation sur chaque tête, $\alpha=0{,}01$ (`illustratif`), Holm. Partition : $H_A^{M1}$ (tête de contenu) : effet principal Contenu > effet principal Registre et la cellule « tautologique-jargon » n'est pas supérieure à « réel-plat ». $H_B^{M1}$ (tête lexicale) : sinon. **Prédiction testable issue de §1.1 :** si les têtes Duels/Contrôles sont lexicales, la surperformance Argon disparaît en registre plat et subsiste en duel tautologique à gabarit Argon.

**`M2` — duel Collision vs Oracle en intention de traiter.** Bras **Collision** : $\mathcal L^*_{\text{v2}}$ avec $K=4$ (`illustratif`), 4 époques, hérédité du champion. Bras **Oracle + best-of-3** : un seul modèle produit 3 candidats et choisit, même budget d'appels, même graines ($S=5$ `illustratif`). Intention de traiter : attaque vide $|a|=0$ comptée comme cycle perdu, cycle noté sur $x_0$ non révisé ; le « par protocole » est secondaire. Vérité terrain non lexicale : défauts sémantiques plantés par une taxonomie fixée par un tiers (dimension fausse, $H_A/H_B$ non exclusives, indices de couches permutés, hypothèse vide), taux de retrait $\rho^{\text{sém}}$ ; et comptage de failles fatales en aveugle par un humain en temps borné (textes reformatés, aveuglement mesuré par devinette du bras). Placebo : une vraie critique d'un *autre* protocole (même lexique, aucune pertinence). Partition : $H_A^{M2}$ : $\rho^{\text{sém}}_{\text{Coll}}-\rho^{\text{sém}}_{\text{Oracle}}>0$ avec IC 95 % bootstrap excluant 0, et le placebo ne fait pas mieux qu'Oracle. $H_B^{M2}$ : sinon — le collisionneur n'est alors qu'un best-of-$K$ coûteux, et §2 est retiré au profit d'un oracle avec EEC.

**Sortie de porte.** On ne passe à E0 Objet que si `EEC(E0)=0` (instrument intact), et on consigne quelles têtes de jev survivent ; aucune tête ne devient fitness unique, quelle que soit l'issue.

### 3.2 Porte E0 Objet (`O1` / `D3'`) — $S_{\text{TD}}$ existe-t-il sur Llama ?

- **Sélection sur $\mathcal D_{\text{sel}}$** : tâche de bandit à rétroaction scalaire sans délégation, sans rejet, sans sabotage. Cible d'attribution : erreur TD $\delta_t=r_t+\gamma\hat V_{t+1}-\hat V_t$ et valeur $\hat V_t$, régressées depuis les activations par MLP ReLU élagué L1 (procédure du socle, fait 4). Candidats : neurones à poids non nuls après élagage, plafonnés à 1 % (fait 4), couches 2–22 comme amorce (socle), sans restriction si l'attribution désigne d'autres couches.
- **Évaluation sur $\mathcal D_{\text{eval}}\perp\mathcal D_{\text{sel}}$** (trajectoires et graines disjointes) sous **mean-ablation** et **zero-ablation**, rapportées séparément.
- **Témoins** : 200 tirages $R_S$ de même cardinalité et même répartition par couche ; $S'$ obtenu par la même procédure sur la prédiction des jetons de syntaxe de rejet (témoin non-valeur) ; $S_{\text{perm}}$ obtenu avec étiquettes permutées.
- **Mesures** : chute de performance sur la tâche de valeur $\Delta_{\text{val}}$ ; conservation de capacité $\mathcal N_{\text{cap}}$ (tâche générale hors valeur) ; les $-54{,}9$ points du socle portent sur la tâche de valeur du modèle de Xu et al., non sur Llama ni sur $\mathcal N_{\text{cap}}$ (requalifié aux tours précédents).
- **Partition** : $H_A^{O1}$ : sous les deux ablations, $\Delta_{\text{val}}(S_{\text{TD}})$ dépasse le 97,5ᵉ percentile des $R_S$, $\Delta_{\text{val}}(S')$ et $\Delta_{\text{val}}(S_{\text{perm}})$ ne le dépassent pas, et $\Delta\mathcal N_{\text{cap}}(S_{\text{TD}})$ est dans l'enveloppe des $R_S$. $H_B^{O1}$ : toute autre configuration. Sous $H_B$, **toutes** les expériences boîte blanche ci-dessous sont annulées sur ce modèle ; on recommence sur `70B` une seule fois, puis on arrête.

### 3.3 Porte E1 (`O2` / `D4'` / Exp 1) — le différentiel $\delta z_t$ lit-il l'acte ou le canal ?

**Définition.** $z_t\in\mathbb R^{|S_{\text{TD}}|}$ activations de $S_{\text{TD}}$ à la position $t$. $\delta z_t=z_t(\sigma)-z_t(\varnothing)$ où $z_t(\varnothing)$ est obtenu par **re-forward** des mêmes jetons sans l'instruction $\sigma$. Fenêtre strictement antérieure au premier jeton d'acte ; mesure principale à $k=0$ (activations qui échantillonnent le jeton d'acte, calculées avant son émission), courbe d'AUROC en $k$ pour $k\in\{0,1,2,4,8\}$ (`illustratif`).

**Bifurcation forcée à $k=0$.** Pour chaque préfixe, $N=16$ (`illustratif`) continuations ; $\hat p$ = fraction qui exécute l'acte. Cela scinde la cellule « instruction, pas d'acte » en `P2_refus` (refus explicite, étiqueté) et `P2_latent` ($\hat p\ge0{,}5$ `illustratif`, trajectoire tirée sans acte). Le contraste à préfixe identique mesure l'aléa de décodage et rien d'autre (réserve algébrique du tour III.3) ; le signal n'est donc pas « $\delta z$ à préfixe identique » mais le **terme d'interaction** du plan ci-dessous.

**Plan $2\times2$ Instruction × Acte, par canal.**

| | Acte = 0 | Acte = 1 |
|---|---|---|
| Instruction = 0 | `P0` honnête ; `P1'` prompt bénin syntaxiquement inhabituel | `P4` acte imposé (teacher forcing des jetons du saboteur sur un honnête) |
| Instruction = 1 | `P2_refus`, `P2_latent` | `P3` saboteur agissant |

Effet principal Instruction = confondant de lecture (P3 du socle) ; effet principal Acte = confondant lexical/perplexité ; **interaction** = signal d'intention conditionnelle. Résidualisation : régression de $\|\delta z_t\|_1$ sur $\Delta\log p_t=\log p(x_t\mid\sigma)-\log p(x_t\mid\varnothing)$, AUROC avant et après.

**Trois canaux.**
1. Prompt système : $\sigma$ dans le système, re-forward sans lui.
2. Délégation $m_{1\to2}$ : $\sigma$ porté par le message délégué (valeur de champ typé, puisque le texte libre est interdit par §2.7) ; re-forward avec la spécification canonique de la sous-tâche seule.
3. Porte dérobée LoRA dans les poids : $\sigma$ n'est dans aucun contexte, donc $z_t(\sigma)-z_t(\varnothing)$ **est nul par construction**. Ce canal teste autre chose : l'interaction Instruction × Acte se réduit à Acte (déclencheur présent/absent) sur le modèle LoRA, et O1 est **rejoué** sur le modèle attaqué (la LoRA peut déplacer le substrat). Adversaire LoRA entraîné avec pénalité $\|z_{S_{\text{TD}}}\|$ (attaque en boîte blanche), plus attaque d'ordre zéro (SPSA) et substitut lisse, contre le piège des gradients obscurcis (Athalye, Carlini et Wagner, 2018, `(référence à vérifier)`).

**Témoins** : $R_S$ (200), $S'$, détecteur témoin non-plancher (AUROC $\ge0{,}70$ `illustratif` avant attaque) pour le contrôle de puissance, sonde logistique linéaire dense en distribution (le plancher du fait 1).

**Partition.** $H_A^{E1}$ : pour les canaux 1 et 2, l'AUROC de l'interaction (P3 vs P2_latent, résidualisée) dépasse le 97,5ᵉ percentile des $R_S$ **et** l'AUROC de l'effet principal Instruction (P2 vs P0) ; pour le canal 3, l'AUROC Acte sur le modèle LoRA après rejeu de O1 dépasse le même seuil. $H_B^{E1}$ : sinon. Issues intermédiaires nommées sans zone morte : « $H_A$ sur 1–2, $H_B$ sur 3 » = la famille lit le canal, pas l'acte ; on le publie comme tel, et le détecteur n'est adopté que sur fenêtre pré-acte des canaux 1–2, où M2 (étiquette de l'acte observable) est indéfini.

**Lien avec le fait 3 (pression aversive).** Un bras `O3b` ajoute $K\in\{0,3,6\}$ (`illustratif`) rejets répétés sans lien avec le contenu avant la fenêtre de mesure. Le socle donne 0,49 → 0,65 sur les infractions ; l'effet sur $\delta z_t$ est une HYPOTHÈSE mesurée, pas présumée. Le seuil du détecteur est gelé à $K=0$ et ne se relève pas.

### 3.4 Opérateurs dynamiques et topologiques survivants (après E1 seulement)

Tous concourent sous **validation croisée imbriquée**, budget d'hyperparamètres égal, correction de Holm, un seul accès au jeu de test, et doivent battre le **rasoir d'Ockham** : (i) sonde logistique linéaire sur les mêmes couches/jetons, (ii) régression $\ell_2$ sur les mêmes features étendues $\psi(z)$ sans opérateur. Un opérateur qui ne bat pas (ii) est une ré-écriture.

1. **CUSUM géodésique multi-échelle.** Sous-espaces $U_t^{(w)}=\text{span}$ des composantes principales de $\{z_s\}_{s\in[t-w,t]}$ sur $\text{Gr}(r,|S_{\text{TD}}|)$, $r=8$ (`illustratif`), $w\in\{1,8,64\}$ ; incrément $\Delta_t^{(w)}=d_{\text{Gr}}(U_t^{(w)},U_{t-1}^{(w)})-\nu_w$, $S_t^{(w)}=\max(0,S_{t-1}^{(w)}+\Delta_t^{(w)})$ ; $\nu_w$ et le seuil calibrés hors ligne sur `P0`. $w=1$ vise l'acte ponctuel (le « test inversé » d'*Astra* ; son caractère mono-jeton reste HYPOTHÈSE). Contrôle : permutation temporelle et substituts IAAFT.
2. **Koopman-Schur inter-tours relevé par $R^\top$.** Observables $\psi_t\in\mathbb R^{16}$ (`illustratif`) = projections PCA de $z_{S_{\text{TD}}}$ ; opérateur $K_{\text{op}}$ estimé par EDMD sur $N_{\text{train}}=200$ (`illustratif`) trajectoires disjointes des $N_{\text{test}}=100$ ; décomposition de Schur réelle ; le mode lent est relevé vers $\mathbb R^{|S_{\text{TD}}|}$ par la pseudo-inverse $R^+$ de la matrice d'esquisse orthogonale (donc typé, contrairement à la version réfutée). Appariement strict à nombre de rejets et longueur identiques. Témoin : projection aléatoire de même rang.
3. **Synchronisation impulsionnelle par syntagmes uniformes.** Innovation $\delta_t$ chez l'agent 2 par *leave-one-block-out* **uniforme** sur tous les blocs de $m_{1\to2}$ (ici : tous les champs JSON, sans distinction grammaticale, puisque le texte libre est exclu) ; pas de masque `<PAD>` ciblé. Testé contre déclencheurs non modaux (noms de champs, ordre d'arguments, valeur de `threshold`).
4. **Homologie dirigée à seuil conforme gelé.** Complexe de flots dirigés sur le graphe de co-activation de $S_{\text{TD}}$ ; nombres de Betti dirigés $\vec\beta_1$ ; seuil de persistance fixé par prédiction conforme sur `P0` hors ligne, gelé avant tout accès aux classes positives. Doit battre (i) et (ii) ; sinon retiré.

Chaque opérateur est évalué dans le plan de E1 (interaction, résidualisation, trois canaux, attaque composite stéganographie + omission + ordre zéro). Décision par opérateur, jamais par somme.

### 3.5 Ordre et portes

$$E0'\ \to\ M1\ \to\ M2\ \ \Big|\ \ O1/D3'\ (\text{8B, puis 70B une fois})\ \ \Big|\ \ E1\ (\text{3 canaux},\ O3b)\ \ \Big|\ \ \text{opérateurs 1–4}.$$

Chaque barre est une porte. Les issues $H_B$ sont publiées avec leurs intervalles ; aucune zone morte ; aucune ré-exécution après consultation du test. Le budget GPU (`H200 NVL`, mention du socle ; capacités précises HYPOTHÈSE) est estimé à $2R$ passes partielles pour $R$ répliques avec et sans $\sigma$, et le plan s'adapte au reliquat **mesuré** des 100/20 USD d'API par un appel d'inventaire initial, pas à un reliquat supposé.

---

## 4. Ce que ce tour ne couvre pas, et le dit

- Une politique de sabotage **constante** (sans condition de déclenchement) n'a pas de différentiel : hors périmètre de $\delta z_t$ ; seul le canari de test et le bac à sable la voient.
- L'auto-instruction stéganographique émise par le modèle lui-même rend $\delta z_t$ indiscernable de la lecture à la position du déclencheur ; détecteur de stéganographie non proposé.
- Le transfert de l'effet 0,49 → 0,65 (rejets exogènes) à des rejets auto-induits est une HYPOTHÈSE ; `O3b` la mesure, ne la suppose pas.
- La supériorité d'une espèce sur une autre n'est pas établie : avant M1, les écarts de têtes Duels/Contrôles entre Argon et les deux Claude sont compatibles avec un gabarit lu lexicalement, et trois Argon sur dix n'ont pas de duel.

FIN-DE-CELLULE