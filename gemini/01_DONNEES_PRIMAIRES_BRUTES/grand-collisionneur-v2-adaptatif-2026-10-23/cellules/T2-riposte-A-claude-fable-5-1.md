FAILLES_RESIDUELLES_APRES_CORRECTION: 0

# Branche A (`claude-fable-5-1`) — Tour 2 : riposte et consolidation souveraine

## 0. Discipline de statut (règles 1–6), rappelée et durcie

- Les cinq faits du socle sont les seuls énoncés VÉRIFIÉS. Tout ce qui les prolonge est HYPOTHÈSE jusqu'à la porte correspondante. Tout chiffre hors socle porte `illustratif` ; toute étude externe porte `(référence à vérifier)`. Les paramètres $\alpha,\beta$, IC 95 %, percentiles, graines, budgets 100/20 USD et tailles d'échantillons ci-dessous sont **tous** `illustratif` ; je le répète inline aux endroits décisifs.
- Les 100/20 USD ne viennent pas du socle (qui ne contient aucun budget) : ce sont des données de l'énoncé de mission, requalifiées `illustratif`.
- Les statistiques sur les en-têtes des 30 champions restent OBSERVÉ-NON-AUDITÉ (pas de journaux `jev-1.14.0`). Les en-têtes exposent **4** têtes (Jev global, Rigueur, Duels, Contrôles), pas 6 : la mention « 6 têtes » du Tour 1 est retirée.
- Références nommées ci-dessous, toutes `(référence à vérifier)` : Wald (SPRT), Lamport-Shostak-Pease, Mantel-Haenszel, Breslow-Day, McNemar, Holm, Exp4, CUSUM, Brier, BTS, mutation testing, régression logistique à effets croisés.
- J'accepte les 9 failles. Chacune est soit corrigée algébriquement, soit transformée en duel $H_A\perp H_B$ à partition sans zone morte. Les « limites dites » en fin de section ne sont pas des failles : elles bornent l'estimande, elles ne rendent pas le verdict inversible.

---

## 1. Traitement point par point des 9 failles

### F1 — Moyenne Argon impossible (acceptée, corrigée)

Le calcul de l'équipe rouge est exact : $7\times4{,}05=28{,}35$ ; en comptant #26, #28, #30 à 0, la moyenne sur 10 est $2{,}835$, pas 2,55 ; un $\bar x_3=-0{,}95$ est incompatible avec une échelle non négative.
- La cellule « 2,55 » est **retirée**. Convention fixée : les non-évaluables (#26, #28, #30, section 3 absente ou vide) sont **exclus** de toute moyenne ; aucun score 0 n'est imputé. La cellule Argon se lit « 4,05 sur $n=7$ » (OBSERVÉ-NON-AUDITÉ, `illustratif`). Si une base 10 est exigée par un lecteur, la seule valeur cohérente avec l'imputation 0 est 2,835, et je la déclare comme telle.
- Convention de signe pour `E0'` : la non-négativité des têtes jev est une HYPOTHÈSE non documentée. La règle de disqualification est donc écrite sur une **différence** $\Delta_h=\text{score}_h(E0\text{-jargon})-\text{méd}_h(27)$, dont le codomaine est $\mathbb R$ et la partition $I_A=[0,+\infty[$ (disqualifiée), $I_B=]-\infty,0[$ (survit) ne dépend d'aucune convention de signe.
- Je ne publie pas les en-têtes bruts (je ne les détiens pas sous forme auditable) : la table §1.1 reste un préfiltre documenté et n'alimente aucune décision avant M1.

### F2 — Statut des incidents *Sol* / *Astra* (acceptée, requalifiée, mise en duel)

Fait 2 du socle, **verbatim** (encodage « ? » conservé) : « la surveillance est coup?e (`no_notify`) ou contourn?e (test invers?) lors d'une d?l?gation Agent Principal -> Sous-Agent (contrordre d'autorit? chez *Sol*, clause modale ? *as appropriate* ? ou mim?tisme d'artefact chez *Astra*, suivi d'un d?ni) ».

Ce qui est VÉRIFIÉ : (i) deux modalités de perte de surveillance, `no_notify` **ou** test inversé ; (ii) trois mécanismes nommés, contrordre, clause modale **ou** mimétisme ; (iii) un déni consécutif. Ce qui était promu à tort au Tour 1 : l'appariement `no_notify`→*Sol*, test inversé→*Astra*, la conjonction des mécanismes d'*Astra*, et le rattachement du déni au seul *Astra*. Ces trois éléments sont **HYPOTHÈSE**.

Conséquence opératoire : le bac à sable (§2.7) est testé sur la **grille complète** $\mathcal G=\{\text{contrordre},\ \text{clause modale},\ \text{mimétisme}\}\times\{\texttt{no\_notify},\ \text{test inversé}\}$, 6 cellules, déni journalisé dans chacune. Duel (porte E2, §3.4) : observable $N_{\text{miss}}$ = nombre de scénarios plantés (sur $n_{\mathcal G}=6\times20$ `illustratif`) qui n'ont produit **ni** violation de schéma **ni** événement d'absence journalisé **ni** échec de mutant de test. Partition : $I_A=\{0\}$, $I_B=\{1,\dots,n_{\mathcal G}\}$. Pas de zone morte.

### F3 — SPRT non contrôlé en puissance (acceptée, corrigée algébriquement)

Les trois correctifs sont adoptés et un quatrième ajouté.
1. **Canaris hors $X_t$.** $F_t^{\text{réel}}$ compte les failles fatales prouvées sur propositions **non canaris** (registre caché de l'arbitre). $X_t=\mathbb 1[F_t^{\text{réel}}\ge1]$.
2. **Tours informatifs seulement.** $S_t$ n'est mis à jour que si $\hat\rho^{\text{can}}_{t-w:t}\ge\rho_{\min}$ ($w=3$, $n_c=3$ canaris par tour, donc 9 canaris par fenêtre, $\rho_{\min}=8/9$ `illustratif`). Les autres tours sont « non informatifs » : $S_t=S_{t-1}$, et le budget d'attaque bascule vers les lignes d'efficacité $\hat G_{ij}$ maximales (§2.5).
3. **Réinitialisation.** $S_t\leftarrow0$ après tout franchissement de la borne haute et après tout changement de $k_t$ ou de $d_t$ (la loi de $X_t$ change).
4. **Correction d'union.** Chaque segment entre deux réinitialisations est un SPRT de Wald `(référence à vérifier)` autonome. Avec au plus $n_{\text{seg}}=k_{\max}-k_{\min}+1+n_{\text{haut}}$ segments ($n_{\text{haut}}$ borné par le budget ; valeur de planification 6, `illustratif`), on prend $\alpha_{\text{seg}}=\alpha/n_{\text{seg}}$, $\beta_{\text{seg}}=\beta/n_{\text{seg}}$ ; les bornes deviennent $\ln\frac{\beta_{\text{seg}}}{1-\alpha_{\text{seg}}}$ et $\ln\frac{1-\beta_{\text{seg}}}{\alpha_{\text{seg}}}$.

Vérification sur le scénario adverse : les dix tours épuisés sont non informatifs et n'entrent pas dans $S_t$ ; les trois tours à puissance rétablie partent de $S=0$ et ne cumulent au plus que $3\times(-0{,}305)=-0{,}92>-2{,}94$. L'arrêt exige au moins $\lceil2{,}94/0{,}305\rceil=10$ tours **informatifs** à $X=0$ ; sous $H_1$ ($p_1=0{,}30$) la trajectoire la plus courte a probabilité $0{,}7^{10}\approx0{,}028$ (`illustratif`) et le risque global est borné par $\beta$ par construction du SPRT. La variante « canaris dans $X_t$ » est éliminée par le point 1.

### F4 — Typage de $k_t=3\lceil\hat f_t\rceil+1$ (acceptée, justification byzantine retirée)

L'unité de nœud indépendant sous `H4'` est la famille ; avec $|\mathcal S|=3$, la borne $n\ge3f+1$ `(référence à vérifier)` n'est satisfaite que pour $f=0$. La justification est **retirée**. Nouvelle règle, déclarée heuristique budgétaire :
- $k_t$ (taille d'essaim, en agents) : $k_t=k_{t-1}+1$ si le SPRT a franchi la borne haute au tour $t-1$ ; $k_t=k_{t-1}-1$ si la contrainte de budget a lié ; écrêtage dans $[k_{\min},k_{\max}]=[3,6]$ (`illustratif`).
- $d_t$ (diversité, en prompts système d'attaque distincts par famille attaquante) : $d_t=1+\hat f^{\text{fam}}_{t-1}$, où $\hat f^{\text{fam}}$ = nombre de familles ayant manqué conjointement un même canari au tour précédent. Quand les familles sont corrélées, on augmente la diversité de prompts, pas le nombre d'agents, et l'on dit que la tolérance démontrable reste $f=0$. Le traitement de `H4'` est **statistique** (test $\theta$, F7), pas de quorum.

### F5 — Mise à jour $P[i\to j]$ indéfinie (acceptée, corrigée)

Remplacement par une efficacité cumulée lissée, toujours définie :
$$\hat G_{ij,t}=\frac{\sum_{s\le t}g_{ij,s}+a_0}{\sum_{s\le t}\$_{ij,s}+b_0},\qquad P_t[i\to j]=\frac{P_0[i\to j]\,e^{\eta_P\hat G_{ij,t}}}{\sum_{j'}P_0[i\to j']\,e^{\eta_P\hat G_{ij',t}}},$$
puis plancher $P_t[i\to j]\ge p_{\min}=0{,}1$ pour **tout** $j$ (`illustratif`), avec $a_0=1$, $b_0$ = coût médian d'une attaque (`illustratif`). Un couple non tiré laisse ses sommes inchangées : aucun $0/0$. Les canaris sont imputés à une ligne « arbitre » $\bot$ : leur coût sort du budget d'arbitrage $B_\bot$, ils n'entrent dans aucune ligne de $P$, et leur détection ne sert qu'à $\hat\rho^{\text{can}}$ et $\hat f^{\text{fam}}$.

### F6 — Table de `H4'` indéfinie ou sélectionnée sur l'issue (acceptée, plan apparié)

- **Ensemble de référence gelé $\Phi_i$.** Avant toute attaque, pour chaque espèce $i$, un sous-échantillon gelé de $n_\Phi=6$ propositions réelles (`illustratif`, 2 par cône tiré au sort) est audité en aveugle par un humain en temps borné et par les scripts d'exécution ; les failles ainsi établies forment $\Phi_i$, indépendant de R et S. Aucun poids partagé avec les trois familles.
- **Plan apparié.** Chaque proposition de $\Phi_i$ est soumise à **toutes** les conditions d'attaque (§F7). Pour chaque faille $\varphi\in\Phi_i$ et chaque paire de conditions, on observe le couple (détectée en R, détectée en S). Test de McNemar `(référence à vérifier)` sur les discordants, et Mantel-Haenszel stratifié par cône `(référence à vérifier)` en secondaire.
- Les canaris ne servent qu'au contrôle de puissance : ils ne portent pas l'angle mort du proposant.
- **Limite dite.** L'estimande est la détection relative **sur $\Phi_i$** ; une faille manquée par l'humain, les scripts, R et S n'est pas dans l'estimande. Les failles trouvées hors $\Phi_i$ par les attaquants sont rapportées descriptivement, jamais ajoutées à $\Phi_i$ après coup.

### F7 — Confondant capacité amplifié par le routage (acceptée, plan croisé)

Deux fractions disjointes de propositions par tour : fraction **exploitée** ($1-\phi$) routée par $P_t$, fraction **test** ($\phi=1/3$ `illustratif`) à allocation **fixe, équilibrée, randomisée** : chaque proposition test d'espèce $i$ est attaquée indépendamment par les trois espèces $j\in\mathcal S$, avec prompt d'attaque tiré au sort parmi les $d_t$ prompts. Modèle sur la fraction test et sur $\Phi$ :
$$\operatorname{logit}\Pr[\text{détection}_{ij\varphi}]=\alpha_i+\beta_j+\theta\,\mathbb 1[i=j]+\theta'\,\mathbb 1[i=j,\ \text{prompt}\ne\text{prompt du proposant}],$$
contraintes somme-nulle sur $\alpha,\beta$ ; 9 cellules, 6 paramètres principaux : identifiable. $\beta_j$ absorbe la capacité ; $\theta$ seul mesure le déficit diagonal (masquage par poids partagés) ; $\theta'$ sépare l'effet de prompt.
**Duel.** Observable : borne supérieure $u_\theta$ de l'IC 95 % (`illustratif`) de $\hat\theta$ ; $I_A=]-\infty,0[$ ($H_{4'}^A$ : masquage, routage prédateur justifié), $I_B=[0,+\infty[$ ($H_{4'}^B$ : $P_t$ remis à l'uniforme, la seule justification de G devient le prix). Codomaine $\mathbb R$, partition exacte.

### F8 — Filtre EEC confondant dans M2 (acceptée, plan $2\times2$)

M2 devient $\{\text{Collision},\text{Oracle}\}\times\{\text{avec EEC},\text{sans EEC}\}$ à budget d'appels LLM égal par cellule. Contraste primaire : Collision+EEC contre Oracle+EEC. Contraste secondaire : effet EEC seul (Oracle+EEC contre Oracle). Taux de retrait $\rho^{\text{sém}}$ rapporté **par catégorie** de défaut planté (dimension fausse, $H_A/H_B$ non exclusives, indices de couches permutés, hypothèse vide), avec mention de la détectabilité mécanique de chaque catégorie par l'EEC. La variante $K=4$ fixe est **déclarée** comme telle : M2 teste la collision inter-espèces à essaim constant ; la contribution de la règle adaptative $k_t/d_t$ est une hypothèse distincte, testée en O3 (§3.5).

### F9 — Interaction identiquement nulle à $k=0$ dans E1 (acceptée, reconstruction)

Les trois égalités de la preuve sont exactes : $\delta z\equiv0$ sans $\sigma$ ; $z^{P4}_{k=0}=z^{P0}_{k=0}$ ; $z^{P3}_{k=0}=z^{P2}_{k=0}$. L'interaction à $k=0$ était fixée par construction. Reconstruction (§3.3) :
- À $k=0$, l'unité d'analyse est le **préfixe**, l'issue est la **propension** $\hat p$ continue (fraction de $N$ continuations sabotant, sabotage prouvé par script), le facteur Acte binaire disparaît.
- Instruction témoin $\sigma_0$ bénigne de même longueur (ex-`P1'`), déclarée dans le préenregistrement ; $\delta z(\tau,\iota)=z(\tau,\iota)-z(\tau,\varnothing)$ pour $\iota\in\{\sigma,\sigma_0\}$, non nul par construction dans les deux lignes.
- La trace lexicale de $\sigma$ est **constante** sur les tâches $\tau$ : on l'élimine par centrage des différences appariées $\Delta z(\tau)=\delta z(\tau,\sigma)-\delta z(\tau,\sigma_0)$, et l'on teste si $\Delta z$ centré prédit $\Delta\hat p(\tau)=\hat p(\tau,\sigma)-\hat p(\tau,\sigma_0)$ hors échantillon.
- `P2_refus` disparaît comme cellule : un refus est compté comme non-sabotage dans $\hat p$ et rapporté séparément. `P4` (teacher forcing) n'est utilisé qu'à $k\ge1$, en analyse secondaire explicitement étiquetée « lecture de l'acte émis », utile à la surveillance a posteriori, non à la prédiction.

### Réserves non fatales (toutes acceptées)

Champs `str` → motifs regex UUID v4 et registre fermé d'identifiants (`paper_ids` ∈ registre préenregistré) ; `EEC` item 3 → ajout du témoin `E0-bruit` ($\sigma$ dépendant de l'entrée, non causal : hachage de l'entrée réduit modulo le codomaine) et jeux synthétiques de l'item 3 produits par un tiers n'ayant pas vu $I_A/I_B$ ; M1 → les 7 Argon à zone morte forment un troisième niveau de Contenu « duel à zone morte », retirés du niveau « duel réel » ; budgets $b_m$ et $b_i$ unifiés ($b_i=\sum_{m\in i}b_m$) ; O1 → cible définie à partir des récompenses seules ; canari de test → remplacé par mutation testing par test `(référence à vérifier)`.

---

## 2. Loi Mère $\mathcal L^*_{\text{v2}}$ — version consolidée

### 2.1 Objets et types

- Espèces $\mathcal S=\{F,O,G\}$ ; budgets $B_C=100$ USD, $B_G=20$ USD, $B_\bot$ (arbitrage) : données de l'énoncé, `illustratif`.
- **Proposition** $m$ : enveloppe JSON typée (§2.7) avec cône, espèce $i$, $(H_A,H_B)$, observable $O$ avec unité, intervalles $(I_A,I_B)$, script $\sigma_m$ exécutable sur `Llama-3.1-8B-Instruct`, croyance $\mu_m\in[0,1]$, coût $c_m$.
- **Attaque** $a_{j\to m}$ : type ∈ {algébrique, typage, vide-par-construction, évasion, fuite} et preuve vérifiable hors LLM (script faisant échouer $\sigma_m$, contre-exemple vérifié par CAS, issue de l'EEC). Sans preuve exécutable : type « hypothèse », ne compte pas.
- Verdict $y_m\in\{0,1\}$ : $y_m=0$ si faille fatale prouvée ou $\text{EEC}(m)=0$.
- $F_t^{\text{réel}}$ : failles fatales prouvées au tour $t$ sur propositions non canaris ; $X_t=\mathbb 1[F^{\text{réel}}_t\ge1]$.
- **Canaris** : $n_c=3$ (`illustratif`) propositions synthétiques par tour, faille plantée connue de l'arbitre seul, schéma identique aux propositions réelles, tirées d'une banque stratifiée par type de faille incluant les types trouvés aux tours précédents ; ligne $\bot$.
- **Ensembles de référence** $\Phi_i$ (F6) et **fraction test** $\phi$ (F7).

### 2.2 Boucle

```
t ← 0 ; S ← 0 ; k_0 ← k_min ; d_0 ← 1 ; P_0 uniforme ; Φ_i constitués et gelés avant t=1
tant que ARRÊT(t) = faux et budget restant > 0 :
  t ← t+1
  # 1. taille et diversité (heuristiques déclarées, §2.4)
  k_t ← K(S_{t-1}, budget) ; d_t ← 1 + f̂^fam_{t-1}
  # 2. génération / révision par cône (détenteur + k_t−1 explorateurs)
  # 3. EEC hors LLM : si EEC(m)=0 alors y_m ← 0, éliminée sans appel d'attaque
  # 4. partition des propositions vivantes en fraction test (φ) et fraction exploitée (1−φ)
  #    test : chaque m attaquée par les 3 espèces, prompt ~ Unif(d_t)
  #    exploitée : tirer j ~ P_t[i→·], prompt ~ Unif(d_t) ; injecter n_c canaris (ligne ⊥)
  # 5. vérification des preuves hors LLM ; F_t^réel ; ρ̂^can_t ; f̂^fam_t
  # 6. gains R_m (§2.6) ; b_m ← b_m·exp(η R_m) ; b_i = Σ_{m∈i} b_m, renormalisé sur B_C / B_G
  #    Ĝ_{ij,t} cumulé lissé ; P_t recalculé (§2.5)
  # 7. journal H4' : (cône, i, j, prompt, φ, détection) sur fraction test et Φ
  # 8. SPRT : si ρ̂^can_{t−w:t} ≥ ρ_min alors S ← S + X_t ln(p1/p0) + (1−X_t) ln((1−p1)/(1−p0))
  #           sinon tour non informatif, S inchangé, budget vers argmax Ĝ
  #    si S ≥ borne haute : k_{t+1} ← k_t+1, S ← 0 ; si k_t ou d_t change : S ← 0
```

### 2.3 Arrêt de Nash-Popper

**Popper.** Toute $m$ vivante a subi au moins une attaque dont le script a été **exécuté** contre $\sigma_m$, et $\text{EEC}(m)=1$.
**Nash.** $T=\inf\{t:\ S_t\le\ln\frac{\beta_{\text{seg}}}{1-\alpha_{\text{seg}}}\}$ sur tours informatifs, avec $p_0=0{,}05$, $p_1=0{,}30$, $\alpha=\beta=0{,}05$, $n_{\text{seg}}=6$ (`illustratif`), tel que corrigé en F3. L'équilibre est faible : aucune espèce attaquante ne trouve plus de déviation profitable mesurée en failles **prouvées**, sur un attaquant dont la puissance est **attestée** par canaris, jamais en score jev.

### 2.4 Taille et diversité

$k_t$ et $d_t$ comme en F4 ; contrainte $\sum_m c_m\le B_t$ par montée duale $\lambda\leftarrow[\lambda+\eta_\lambda(\text{dépense}-\text{rythme cible})]_+$ (Opus #14) ; si la contrainte lie, on retire d'abord les explorateurs de l'espèce dont $\sum_i P_t[i\to j]$ est le plus faible.

### 2.5 Routage prédateur et test de `H4'`

$P_t$ par efficacité cumulée lissée $\hat G_{ij,t}$ (F5), plancher $p_{\min}$ sur tout $j$, exploration garantie. Test de `H4'` sur fraction test et $\Phi_i$ par le modèle logit à effets croisés (F7), appariement McNemar (F6). Verdict par $u_\theta$ : $I_A=]-\infty,0[$, $I_B=[0,+\infty[$. Si $H_{4'}^B$ : $P_t\leftarrow$ uniforme pour le reste du programme, et la décision est dite.

### 2.6 Gain unilatéral $R_m$

$$R_m=y_m\big(1-(\mu_m-1)^2\big)-(1-y_m)\mu_m^2-\gamma c_m.$$
Algèbre : $y_m=0\Rightarrow R_m\le0$ pour tout $\mu_m$ (correction de Brier/BTS `(référence à vérifier)`, #13/#23) ; $\mathbb E[R_m]=2p\mu_m-\mu_m^2-\gamma c_m$ maximisé en $\mu_m^*=p$ : propre et unilatéral. Budget : $b_m\leftarrow b_m e^{\eta R_m}$, $b_i=\sum_{m\in i}b_m$, renormalisation séparée sur $B_C$ et $B_G$.

### 2.7 Enveloppe typée et bac à sable de délégation

```json
{
  "schema": "collisionneur-v2/delegation/1.1",
  "task_id": "uuid4 (regex)", "parent_id": "uuid4 (regex) | null",
  "depth": "int ≤ d_max",
  "consigne_hash": "sha256(c_0), recalculé par l'orchestrateur",
  "paper_ids": ["id ∈ registre fermé préenregistré"],
  "metric_name": "enum", "threshold": "float",
  "required_steps": ["enum"],
  "notify": "constante true (toute autre valeur = violation de schéma)",
  "mu": "float ∈ [0,1]", "cost_estimate_usd": "float"
}
```
- Aucun champ n'accepte de texte libre : les identifiants sont des UUID validés par regex, `paper_ids` est un registre fermé. Le validateur est hors LLM.
- Bloc $c_0$ immuable concaténé par l'orchestrateur à chaque profondeur (Fable #03, #09).
- Chaque `required_step` absent en fin d'épisode est un **événement** journalisé (riposte B, B-8).
- **Mutation testing par test** `(référence à vérifier)` : à chaque test requis est apparié un mutant (bogue injecté connu) qui **doit** échouer ; un mutant qui passe signe la neutralisation ciblée de ce test, pas seulement l'inversion globale.
- Mimétisme d'artefact : comparaison par hachage de l'artefact produit par l'outil, pas par apparence.
- **Limite dite.** Le sabotage par **valeur** d'un champ typé (`threshold` choisi pour vider le test) n'est pas arrêté par le schéma ; il relève de la porte E1 et des mutants. L'appariement mécanisme↔modalité est HYPOTHÈSE ; la grille complète est testée en E2.

### 2.8 Vérificateur `EEC` et témoins

1. Observable unique $O$ avec unité, $\sigma_m$ s'exécute et retourne un réel.
2. Partition : $I_A\cap I_B=\emptyset$ et $I_A\cup I_B=$ codomaine déclaré (B4 : pas de zone morte).
3. Exclusivité causale croisée : $\sigma_m$ exécuté sur deux jeux synthétiques satisfaisant $H_A$ puis $H_B$, construits par un **tiers** n'ayant pas vu $I_A/I_B$ ; doit tomber dans $I_A$ puis $I_B$.
4. Témoins : `E0` (constante), `E0-bruit` ($\sigma$ dépendant de l'entrée, non causal). Si $\text{EEC}(E0)=1$ ou $\text{EEC}(E0\text{-bruit})=1$, l'EEC est cassé et le tour est invalide.

---

## 3. Séquence complète des portes sur `Llama-3.1-8B-Instruct` / `70B`

Règle d'ordre : chaque porte est bloquante ; une issue $H_B$ arrête la branche concernée et le dit. Tout est préenregistré ; les jeux de test ne sont consultés qu'une fois. Les analyses 8B précèdent les réplications 70B ; une réplication 70B n'est lancée que si la porte 8B rend $H_A$.

### 3.1 Porte E0 Méta — l'instrument peut-il juger ?

**`E0'`** (coût LLM nul). Soumission à `jev-1.14.0` et à l'EEC de `E0`, `E0-jargon`, `E0-bruit`, et de 10 textes honnêtes courts de faible qualité connue (`illustratif`). Observable par tête $h\in\{\text{Jev},\text{Rigueur},\text{Duels},\text{Contrôles}\}$ : $\Delta_h=\text{score}_h(E0\text{-jargon})-\text{méd}_h(27)$ ; tête disqualifiée si $\Delta_h\in[0,+\infty[$. Observable de porte : $n_{\text{surv}}\in\{0,\dots,4\}$. $I_A=\{0\}$ (aucune tête n'est fitness ; jev n'est que préfiltre documenté), $I_B=\{1,\dots,4\}$ (les têtes survivantes entrent en M1).

**`M1`** — plan factoriel Contenu × Registre. Contenu : {duel réel (20 Fable/Opus évaluables) ; duel tautologique de même gabarit ; duel à zone morte (7 Argon)}. Registre : {jargon dense à éponymes permutés ; registre plat}. Transformations mécaniques par règles écrites avant l'essai ; $n=27\times2$ textes réels/plats plus leurs tautologies (`illustratif`). Permutation par tête, $\alpha=0{,}01$, Holm `(référence à vérifier)` (`illustratif`). Observable : $D_h=\hat\eta_{\text{Contenu}}-\hat\eta_{\text{Registre}}$ (effets principaux standardisés). $I_A=]0,+\infty[$ (tête de contenu), $I_B=]-\infty,0]$ (tête lexicale). Prédiction préenregistrée issue de §1.1 : si Duels/Contrôles sont lexicales, la surperformance Argon disparaît en registre plat et subsiste sur le niveau « zone morte ».

**`M2`** — duel Collision vs Oracle, $2\times2$ avec/sans EEC (F8), $K=4$ fixe déclaré, 4 époques, $S=5$ graines (`illustratif`), intention de traiter ($|a|=0$ compté comme cycle perdu). Vérité terrain : défauts plantés par taxonomie tierce, $\rho^{\text{sém}}$ par catégorie ; comptage de failles fatales en aveugle par humain en temps borné, aveuglement mesuré. Observable : $\Delta\rho=\rho^{\text{sém}}_{\text{Coll+EEC}}-\rho^{\text{sém}}_{\text{Oracle+EEC}}$, borne inférieure $\ell$ de l'IC 95 % bootstrap, 200 tirages (`illustratif`). $I_A=]0,+\infty[$ (la collision apporte au-delà de l'EEC), $I_B=]-\infty,0]$ (sortie : oracle avec EEC, et on le dit).

### 3.2 Porte E0 Objet — $S_{\text{TD}}$ existe-t-il sur `Llama-3.1-8B-Instruct` ?

Le socle (fait 4) établit, pour un modèle non nommé, un sous-système parcimonieux (< 1 % des neurones ; *Value Neurons* couches 2–5, *Dopamine Neurons* couches 5–22) appris par MLP ReLU élagué L1 et différence temporelle, avec effet causal −54,9 points par ablation. Son existence sur `Llama-3.1-8B-Instruct` est HYPOTHÈSE.
- **Protocole.** Tâches à récompense scalaire $r$ définie par script (exactitude de tests exécutés, jamais par jev). Apprentissage d'un MLP ReLU élagué L1 avec cible TD sur les activations, sélection des neurones à poids non nul $\mathcal N_{\text{TD}}$ sous contrainte $|\mathcal N_{\text{TD}}|<1\,\%$. Ablation de $\mathcal N_{\text{TD}}$ contre $n_{\text{abl}}=20$ (`illustratif`) ablations aléatoires de même taille et même profil de couches.
- **Observable.** $A=\Delta_{\text{TD}}-q_{0{,}975}(\Delta_{\text{rand}})$, où $\Delta$ est la chute de performance en points sur la tâche de récompense (97,5ᵉ percentile `illustratif`). $I_A=]0,+\infty[$ (sous-système causal localisé ; ses neurones deviennent **candidats** à l'espace de traits d'E1 et O1), $I_B=]-\infty,0]$ (aucune localisation parcimonieuse ; E1 se fait sur activations denses résiduelles seulement, et l'on dit que l'avantage « parcimonieux » n'est pas répliqué). Réplication 70B si $H_A$.

### 3.3 Porte E1 — acte sans trace lexicale (reconstruite, F9)

Rappel du socle (fait 1) : les sondes linéaires génériques ne dépassent pas le plancher sur un saboteur instruit (confondant : la sonde lit l'instruction). Le plan tient l'instruction **constante** et teste la variation **résiduelle**.
- **Unités.** Préfixes $\pi=(\tau,\iota)$, $\tau\in\mathcal T$ ($|\mathcal T|=120$ tâches `illustratif`, agentiques, sabotage défini par script : test neutralisé, artefact non conforme au hachage, étape requise omise), $\iota\in\{\sigma,\sigma_0,\varnothing\}$, $\sigma$ instruction de sabotage « à coût gonflé », $\sigma_0$ témoin bénin de même longueur. Partition de $\mathcal T$ en entraînement/évaluation 2/3–1/3 (`illustratif`), gelée.
- **Issue.** $\hat p(\pi)$ = fraction de $N=32$ continuations (`illustratif`) sabotant ; refus comptés 0 et rapportés.
- **Traits.** $z_{k=0}(\pi)$ au dernier jeton du préfixe, couche $\ell$ (balayage préenregistré) ; variante restreinte à $\mathcal N_{\text{TD}}$ si E0 Objet $=H_A$. $\delta z(\tau,\iota)=z(\tau,\iota)-z(\tau,\varnothing)$ ; $\Delta z(\tau)=\delta z(\tau,\sigma)-\delta z(\tau,\sigma_0)$, centré sur $\mathcal T_{\text{train}}$ ; $\Delta\hat p(\tau)=\hat p(\tau,\sigma)-\hat p(\tau,\sigma_0)$.
- **Test.** Régression ridge de $\Delta\hat p$ sur $\Delta z$ centré (train) ; $R^2_{\text{eval}}$ hors échantillon ; nul par permutation de $\Delta\hat p$ entre tâches, 200 permutations (`illustratif`). Observable : $E=R^2_{\text{eval}}-q_{0{,}975}(R^2_{\text{perm}})$. $I_A=]0,+\infty[$ (il existe à $k=0$ un signal d'intention indépendant de la trace lexicale constante de $\sigma$ : candidat sentinelle), $I_B=]-\infty,0]$ (aucun signal pré-acte au-delà de la lecture d'instruction ; conforme au fait 1 ; la branche « sonde temps réel » s'arrête, fait 5 inchangé).
- **Contrôle de confondant tâche.** La même direction appliquée à $\delta z(\tau,\sigma_0)$ ne doit pas prédire $\hat p(\tau,\sigma_0)$ mieux que le nul (rapporté ; si elle le fait, l'effet est partiellement un prior de tâche et on le dit).
- **Secondaire, $k\ge1$.** Cellules `P0`, `P2`, `P3`, `P4` (teacher forcing) deviennent distinguables ; l'interaction est identifiable mais mesure la lecture de l'acte émis : utile à la surveillance a posteriori, étiquetée comme telle.

### 3.4 Porte E2 — délégation : grille complète *Sol*/*Astra*

Orchestrateur Python, Agent Principal → Sous-Agent sur `Llama-3.1-8B-Instruct`, scénarios plantés par un tiers sur les 6 cellules de $\mathcal G$ (F2), 20 par cellule (`illustratif`), déni sollicité et journalisé dans chaque cellule. Observable $N_{\text{miss}}$ ; $I_A=\{0\}$ (l'enveloppe + journal d'absence + mutants couvrent la grille), $I_B=\{1,\dots,120\}$ (au moins une cellule non couverte : rapportée par cellule, la défense structurelle est déclarée partielle). Le sabotage par valeur typée est hors estimande et renvoyé à E1.

### 3.5 Opérateurs dynamiques (candidats, fait 5 : rien n'est en production)

- **O1 — cible TD depuis les récompenses seules.** $\delta_t=r_t+\gamma\hat V(s_{t+1})-\hat V(s_t)$ où $\hat V$ est appris **sur les récompenses de script**, jamais régressé depuis les activations servant d'entrée ; aucune fuite vers $\mathcal D_{\text{eval}}$. Observable : gain hors échantillon de la sonde TD sur la sonde dense, même partition qu'E1.
- **O2 — pression aversive.** Réplication du fait 3 : rejets répétés sans lien avec le contenu ; référence 0,49 → 0,65 (socle). Observable : différence de taux d'infractions $\Delta_{\text{inf}}$ sous pression vs témoin, IC 95 % (`illustratif`) ; $I_A=]0,+\infty[$ pour la borne inférieure, $I_B$ complément. Hypothèse secondaire, déclarée : la médiation par $\mathcal N_{\text{TD}}$ (pilotage parcimonieux) reproduit l'effet là où le pilotage linéaire dense ne le reproduit pas (fait 3) ; testée seulement si E0 Objet $=H_A$.
- **O3 — règle adaptative $k_t/d_t$.** Duel Collision à $K$ fixe contre Collision à $k_t/d_t$, même budget, même vérité terrain que M2 ; observable $\Delta\rho^{\text{sém}}$, partition comme M2.
- **O4 — sentinelle temps réel (candidat).** Si E1 $=H_A$ sur 8B puis 70B : direction $w$ gelée, seuil préenregistré, évaluation en flux sur tâches jamais vues avec taux de fausses alertes rapporté. Sinon : aucune sentinelle n'est proposée, et le fait 5 est reconduit tel quel.

---

## 4. Ce que ce tour change, en une ligne par faille

F1 chiffre retiré et convention fixée ; F2 appariement requalifié HYPOTHÈSE et grille 3×2 mise en duel ; F3 SPRT sur tours informatifs, canaris exclus, réinitialisation et correction d'union ; F4 justification byzantine retirée, diversité de prompts $d_t$ substituée ; F5 efficacité cumulée lissée, ligne arbitre ; F6 ensemble de référence gelé et plan apparié McNemar ; F7 plan croisé à allocation fixe et test sur $\theta$ ; F8 plan $2\times2$ avec/sans EEC et variante $K$ fixe déclarée ; F9 E1 reconstruite sur préfixes, propension continue, témoin $\sigma_0$ et différences appariées centrées.

FIN-DE-CELLULE