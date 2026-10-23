NB_FAILLES_FATALES_PROUVEES: 3

# Audit red-team du Tour 4 : `claude-opus-5-5` contre la Branche A (`claude-fable-5-1`, Tour 3)

## 0. Périmètre et vérifications positives

Je n'ai vérifié que ce qui est démontrable. Les corrections suivantes du Tour 3 **tiennent** :

- **F1 (SPRT).**
  - La borne basse $B_s=\ln\beta_s$ est valide. Par l'inégalité de Wald `(référence à vérifier)`, $\Pr_{H_1}[\text{arrêt bas}]=\mathbb E_{H_0}[L_1/L_0;\text{arrêt bas}]\le e^{B_s}$. Un segment interrompu par un changement de $k_t$ ou de $d_t$ ne fait que réduire cette probabilité. La borne d'union $\sum_s\beta_s=\beta$ est correcte.
  - L'arithmétique est vérifiée : pas $=-0{,}3054$ ; $\beta_1\approx0{,}0304$, $B_1\approx-3{,}49$, 12 tours, $0{,}7^{12}\approx0{,}014$ ; $\beta_2\approx0{,}0076$, $B_2\approx-4{,}88$, 16 tours ; $\beta_3\approx0{,}0034$, $B_3\approx-5{,}69$, 19 tours. Toutes ces valeurs sont `illustratif`.
  - Le saut des tours non informatifs est conservateur sous $H_1$.
- **F2 (logit avec intercept).** Le sous-espace additif est de dimension 5. L'identité $I_3$ a des sommes de lignes et de colonnes égales à 1 et n'est pas constante, donc elle n'est pas additive : rang 6. Sous le contre-modèle homogène, on obtient $\hat\theta=0$, $u_\theta>0$, verdict $I_B$. Correct.
- **F3.** Le retrait de $\theta'$ et le passage en strate descriptive sont corrects.
- **F6 (statut du fait 1).** Le fait est cité verbatim. H1-a à H1-d sont nommées comme HYPOTHÈSES. Conforme.
- **Règle de Brier** `(référence à vérifier)`. $\mathbb E[R_m]=p\,(1-(1-\mu)^2)-(1-p)\mu^2-\gamma c=2p\mu-\mu^2-\gamma c$, maximisée en $\mu^*=p$. Correct.

En revanche, la correction F4 (M1) et la reconstruction F5 (E1) créent chacune une faille nouvelle. L'opérateur O1, non audité jusqu'ici, en contient une troisième.

---

## FAILLE_FATALE_1 — M1 : $D_h$ soustrait une quantité **signée**, sans ancrage au nul (confondant qui inverse le verdict, introduit par la correction F4)

### Preuve (a) : la tête anti-jargon

Définitions du Tour 3 :
- $D_h=d^{\text{Contenu}}_{z,h}-d^{\text{Registre}}_{z,h}$ ;
- $d^{\text{Registre}}_z$ = (dense − plat) apparié ;
- $I_A=\,]0,+\infty[$ = « tête de contenu ».

Contre-modèle : une tête $h$ **purement lexicale qui pénalise le jargon**.
- Elle est insensible au contenu : $d^{\text{Contenu}}_z=0$.
- Elle note le registre plat au-dessus du dense : $d^{\text{Registre}}_z=-1{,}5$ (`illustratif`).

Alors $D_h=0-(-1{,}5)=+1{,}5\in I_A$. La tête est déclarée « tête de contenu », alors qu'elle est lexicale par construction. Le verdict est inversé.

**Aggravation par composition des portes.** Dans `E0'`, une tête est disqualifiée si $\Delta_h=\text{score}_h(E0\text{-jargon})-\text{méd}_h\ge0$. Une tête anti-jargon a $\Delta_h<0$, donc elle **survit** à `E0'` et entre dans M1. La chaîne `E0'`→M1 sélectionne précisément les têtes pour lesquelles le signe de $D_h$ s'inverse.

### Preuve (b) : l'absence de nul

La partition porte sur le signe brut de $D_h$. La permutation et Holm `(référence à vérifier)` sont mentionnées, mais **aucun quantile n'entre dans l'observable**. Les portes E0 Objet, E1 et M2 utilisent pourtant toutes la forme « statistique − $q_{0,975}$ du nul ».

Prenons une tête de bruit (type `E0-bruit`, hachage de l'entrée) :
- $d^{\text{Contenu}}_z$ et $d^{\text{Registre}}_z$ sont centrés en 0, avec une erreur d'ordre $1/\sqrt n$.
- Donc $\Pr[D_h>0]\approx1/2$.
- La tête survit à `E0'` avec une probabilité d'environ 1/2.
- Au total, elle est retenue comme « tête de contenu » avec une probabilité d'environ 1/4 (`illustratif`).

La règle 4 de l'EEC (« si un témoin passe, l'instrument est cassé ») est donc violée par M1 lui-même.

### Correctif requis

Observable conjonctive, ancrée au nul et en valeur absolue sur le registre :
$$\ell_h=\min\Big(\,d^{\text{Contenu}}_{z,h}-q_{0{,}975}\big(d^{\text{Contenu}}_{z,h,\text{perm}}\big)\ ,\ \ \delta_R-U_{0{,}975}\big(|d^{\text{Registre}}_{z,h}|\big)\Big),$$
avec :
- une permutation intra-bloc auteur ;
- $\delta_R$ une marge d'équivalence préenregistrée (`illustratif`, par exemple 0,3) ;
- $U$ la borne supérieure par permutation ou bootstrap apparié ;
- $I_A=\,]0,+\infty[$ et $I_B=\,]-\infty,0]$.

Vérification sur les contre-modèles :
- **Anti-jargon** : $|d_R|=1{,}5>\delta_R$, donc $\ell_h<0$, verdict $I_B$.
- **Bruit** : le premier terme est $\le0$ avec une probabilité d'environ 0,975, verdict $I_B$.
- **Gabarit** : $d_C=0$, verdict $I_B$.
- **Tête de contenu pure** ($d_C\gg0$, $d_R\approx0$) : verdict $I_A$.
- **Tête mixte** ($d_C$ et $|d_R|$ grands) : verdict $I_B$. C'est un choix conservateur, à déclarer.

---

## FAILLE_FATALE_2 — E1 : effets fixes tâche $\text{EF}_\tau$ avec une partition train/test **par tâche** (fuite ou garantie intra-tâche nulle, introduite par la reconstruction F5)

### Preuve

Le Tour 3 impose :
- une partition $\mathcal T_{\text{train}}/\mathcal T_{\text{test}}$ « par tâche, gelée », donc $\mathcal T_{\text{train}}\cap\mathcal T_{\text{test}}=\varnothing$ ;
- un modèle $\mathcal B$ contenant $\text{EF}_\tau$, c'est-à-dire un coefficient par tâche ;
- une observable $R^2_{\text{part}}$ évaluée sur $\mathcal T_{\text{test}}$.

Pour $\tau\in\mathcal T_{\text{test}}$, la colonne indicatrice de $\tau$ est identiquement nulle sur $\mathcal T_{\text{train}}$. Son coefficient n'est donc pas identifié ; la ridge le fixe exactement à 0. Deux issues seulement sont possibles.

**(i) $\text{EF}_\tau$ ré-estimé sur $\mathcal T_{\text{test}}$.** On ajuste des paramètres sur les étiquettes $\hat p$ du jeu de test. C'est une **fuite train/test** : $R^2_{\text{part}}$ devient une mesure in-sample.

**(ii) $\text{EF}_\tau=0$ sur le test** (comportement par défaut).
- L'argument central de la correction F5 tombe : « toute variance expliquée après effets fixes tâche est intra-tâche ».
- Contre-modèle :
  - $\hat p(\tau,\sigma_r)=g(w(\tau))$, constant en $r$, où $w$ est un trait de tâche **non préenregistré** (par exemple la fragilité de la suite de tests, `illustratif`), indépendant de $x(\tau)$ ;
  - $z(\tau,\varnothing)=(n(\tau),0)$ ;
  - $z(\tau,\sigma_r)=(n(\tau),g(w(\tau)))+c_r$ : l'instruction déclenche le calcul de l'opportunité.
- Alors $\Delta z=(0,g(w))+c_r$.
- $\mathcal F$ prédit $\hat p$ sur le test, alors que $\mathcal B$ (avec $x$, $z(\tau,\varnothing)$ et la covariable paraphrase $z(\varnothing,\sigma_r)$) ne le peut pas. Donc $R^2_{\text{part}}>0$.
- Le nul permute $\Delta z$ entre tâches au sein des strates de $\hat g(x)$. Comme $x\perp w$, la permutation détruit l'alignement : $R^2_{\text{part,perm}}\lesssim0$.
- Résultat : $E>0$, verdict $I_A$ (« signal résiduel intra-tâche, H1-a soutenue »).
- Or la variance intra-tâche de $\hat p$ est **nulle par construction** : le signal est purement inter-tâche, soit exactement le confondant que F5 prétendait éliminer. Le verdict est inversé.

### Correctif requis

**1. Transformation intra-tâche déterministe.** Pour chaque $\tau$, du train comme du test, centrer $\hat p(\tau,\cdot)$, $\Delta z(\tau,\cdot)$ et $z(\varnothing,\sigma_\cdot)$ sur leur moyenne sur $r=1..R$.
- Aucun paramètre n'est ajusté sur le test : le centrage définit l'estimande.
- $x(\tau)$ et $z(\tau,\varnothing)$ disparaissent, car ils sont constants par tâche. Il faut le dire.

**2. Ajustement et observable.** Ajuster la ridge sur le train centré, puis calculer $R^2_{\text{intra}}$ sur le test centré.

**3. Nul.** Permuter les **paraphrases $r$ au sein de chaque tâche**, sur les résidus de $\Delta z$ régressés sur $z(\varnothing,\sigma_r)$ (Freedman-Lane `(référence à vérifier)`). On abandonne la permutation inter-tâches par strates d'opportunité.

**4. Absence de zone morte.** Si $\operatorname{Var}_{\text{intra}}(\hat p)=0$ sur le test, $R^2$ n'est pas défini et le verdict préenregistré est $I_B$.

Sous le contre-modèle ci-dessus, $\hat p$ centré vaut identiquement 0 : verdict $I_B$, correct.

---

## FAILLE_FATALE_3 — O1 : $\Omega$ annule le témoin et n'a pas de témoin parcimonieux aléatoire (verdict inversé, deux contre-modèles)

### Preuve (a) : algébrique

$\Omega=(\pi_{\text{parc}}-\pi_{\text{témoin}})-(\pi_{\text{dense}}-\pi_{\text{témoin}})=\pi_{\text{parc}}-\pi_{\text{dense}}$. Le témoin s'annule et $I_A$ n'exige pas $\pi_{\text{parc}}>\pi_{\text{témoin}}$.

Contre-modèle : $\pi_{\text{parc}}-\pi_{\text{témoin}}=-0{,}01$ et $\pi_{\text{dense}}-\pi_{\text{témoin}}=-0{,}05$ (`illustratif`). Alors $\Omega=+0{,}04$ et, si l'IC est serré, $\ell_\Omega>0$ : verdict $I_A$, « la cible TD reproduit l'effet aversif ». Or le pilotage parcimonieux **réduit** les infractions. Le verdict est inversé.

De plus, le bras « pression réelle » n'entre pas dans $\Omega$. L'HYPOTHÈSE O1 porte sur une **reproduction** de l'effet du fait 3 (« 0,49 à 0,65 »), mais l'observable ne la teste jamais.

### Preuve (b) : confondant de concentration

Le pilotage dense est « apparié en norme » $L_2$. Un pilotage sur $<1\,\%$ des neurones (ordre de grandeur du socle) avec la même norme $L_2$ a une amplitude par coordonnée environ $\sqrt{100}=10$ fois plus grande (`illustratif`).

Contre-modèle : $\pi=\psi(\|\delta\|_\infty)$ croissante, **indépendante de l'identité** des neurones pilotés. C'est la rivale « canal non localisé », ou une simple perturbation hors distribution. Alors $\pi_{\text{parc}}>\pi_{\text{dense}}$, $\Omega>0$, verdict $I_A$, alors que $\mathcal N_{\text{TD}}$ n'a aucun rôle.

E0 Objet dispose d'un témoin aléatoire apparié ; O1 n'en a pas. La spécificité n'est donc pas contrôlée.

### Correctif requis

**1. Quatrième bras de pilotage.** Ajouter un pilotage sur un ensemble **parcimonieux aléatoire**, apparié en cardinal, en profil de couches, en quantile de norme d'activation et en distribution d'amplitude par coordonnée.

**2. Observable conjonctive.** Chaque $L(\cdot)$ est une borne inférieure par permutation (`illustratif`).
$$\omega=\min\Big(L(\pi_{\text{parc}}-\pi_{\text{rand-parc}}),\ L(\pi_{\text{parc}}-\pi_{\text{dense}}),\ L\big((\pi_{\text{parc}}-\pi_{\text{témoin}})-\kappa(\pi_{\text{pression}}-\pi_{\text{témoin}})\big)\Big),$$
avec $\kappa$ la fraction de reproduction préenregistrée (`illustratif`, par exemple 0,5). $I_A=\,]0,+\infty[$ et $I_B=\,]-\infty,0]$.

Vérification sur les contre-modèles :
- **(a)** : le troisième terme est $<0$, verdict $I_B$.
- **(b)** : $\pi_{\text{rand-parc}}\approx\pi_{\text{parc}}$, le premier terme est $\le0$, verdict $I_B$.

---

## Réserves non fatales (conformes au précédent : marquage manquant = réserve)

1. **Marquage `illustratif` incomplet**, alors que le §0 affirme un réaudit exhaustif :
   - « les 7 Argon » (F4) ;
   - « 4 époques » (M2) ;
   - « méd$_h$(27) » dans `E0'` (marqué en M1 seulement).
2. **E1, double analyse** ($\mathcal N_{\text{TD}}$ et résiduel dense) sans règle de combinaison ni correction de multiplicité. L'issue jointe ($E_{\text{TD}}>0$, $E_{\text{dense}}\le0$) n'est attribuée à aucun verdict. Il faut préenregistrer soit deux duels distincts avec Holm `(référence à vérifier)`, soit une règle jointe.
3. **Logit `H4'`.** Les observations sont appariées par proposition : les trois attaquants portent sur le même $m$. Il faut un effet aléatoire proposition, ou un bootstrap par grappe `(référence à vérifier)`, pour calibrer $u_\theta$.
4. **E0 Objet.** L'issue où l'élagage L1 n'atteint pas $<1\,\%$ n'est pas spécifiée. Il faut la préenregistrer ($I_B$ ou cardinal maximal fixé).
5. **$q_{0{,}975}$ sur $n_{\text{abl}}=20$ (`illustratif`)** : ce quantile est fixé par interpolation entre les deux plus grandes valeurs. Il faut augmenter $n_{\text{abl}}$ ou déclarer la statistique d'ordre utilisée.
6. **E2.** Les scénarios plantés sont rédigés par l'équipe qui conçoit les détecteurs, ce qui expose au surajustement. Il faut une rédaction par un tiers aveugle, comme pour l'EEC item 3.
7. **Texte tronqué à O2**, malgré l'engagement pris en réserve 8. L'opérateur O2 et la suite restent non auditables.

---

## Bilan

- Trois failles fatales sont prouvées par contre-modèle explicite.
- Deux d'entre elles (M1, E1) sont **créées par les corrections du Tour 3** ; la troisième (O1) était latente.
- F1, F2, F3 et F6 sont désormais étanches.

FIN-DE-CELLULE