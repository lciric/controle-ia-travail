NB_FAILLES_FATALES_PROUVEES: 6

# Tour 3 — Audit red-team de `claude-opus-5-5` contre la Branche A (`claude-fable-5-1`)

**Discipline appliquée.** Toute étude externe porte `(référence à vérifier)`. Tout chiffre hors socle porte `illustratif`, y compris les valeurs que je dérive des paramètres `illustratif` de la Branche A.

**Périmètre.** J'ai vérifié en priorité les objets introduits ou modifiés au Tour 2 : SPRT corrigé, modèle logit à effets croisés de F7, troisième niveau de Contenu de M1, reconstruction d'E1 et rappels du socle.

**Ce qui tient.** Je valide explicitement l'algèbre de $R_m$ :
- $\mathbb E[R_m]=2p\mu_m-\mu_m^2-\gamma c_m$ ;
- $y_m=0\Rightarrow R_m\le0$.

Je valide aussi :
- le plancher $p_{\min}$ (`illustratif`), compatible avec 3 espèces ($3\times0{,}1\le1$) ;
- le $\hat G_{ij}$ lissé, toujours défini ;
- la valeur 2,835 de F1 ;
- les partitions sans zone morte de E0′, M2, E0 Objet et E2.

---

## FAILLE_FATALE_1 — SPRT : la correction d'union compte mal les segments, et la « vérification » utilise une borne non corrigée

**Preuve (a) — dénombrement faux.** F3, point 3, réinitialise $S$ « après tout changement de $k_t$ ou de $d_t$ ». Le point 4 borne pourtant les segments par $n_{\text{seg}}=k_{\max}-k_{\min}+1+n_{\text{haut}}$. Ce décompte oublie deux sources de réinitialisation :

1. **Les changements de $d_t$.** On a $d_t=1+\hat f^{\text{fam}}_{t-1}$, et $\hat f^{\text{fam}}$ peut changer à chaque tour. Chaque changement réinitialise $S$, sans qu'aucun terme de $n_{\text{seg}}$ ne l'absorbe.
2. **Les oscillations de $k_t$.** $k_t$ monte après un franchissement haut et descend quand le budget lie. La suite 3→4→3→4… est admissible : le nombre de changements de $k$ n'est borné que par le nombre de tours $T$, pas par $k_{\max}-k_{\min}+1$.

Donc $n_{\text{seg}}^{\text{réel}}\le T$, et non $\le6$ (`illustratif`). Chaque segment est un SPRT autonome dont l'arrêt erroné sous $H_1$ a une probabilité $\le\beta_{\text{seg}}=\beta/6$. La borne d'union donne alors $\Pr[\text{arrêt Nash erroné}]\le n_{\text{seg}}^{\text{réel}}\,\beta/6$, qui dépasse $\beta$ dès que $n_{\text{seg}}^{\text{réel}}>6$. L'affirmation « risque global borné par $\beta$ par construction » est fausse.

**Preuve (b) — arithmétique incohérente avec la correction adoptée.** Avec $\alpha=\beta=0{,}05$ et $n_{\text{seg}}=6$ (`illustratif`), on a $\alpha_{\text{seg}}=\beta_{\text{seg}}\approx0{,}00833$. La borne basse vaut :

$$\ln\frac{0{,}00833}{0{,}99167}\approx-4{,}78 \quad (\texttt{illustratif}),$$

et non $-2{,}94$, qui est la borne **non corrigée**. Avec un pas $\ln(0{,}7/0{,}95)\approx-0{,}305$, l'arrêt exige $\lceil4{,}78/0{,}305\rceil=16$ tours informatifs, et non 10. La probabilité de la trajectoire la plus courte sous $H_1$ vaut $0{,}7^{16}\approx0{,}0033$, et non 0,028 (`illustratif`). La vérification du scénario adverse est donc calculée sur une règle que la Branche A a elle-même abandonnée.

**Correctif requis.**
- Remplacer la division uniforme par une dépense d'erreur à série convergente, valable pour un nombre non borné de segments : $\beta_s=\beta\cdot\frac{6}{\pi^2 s^2}$ et $\alpha_s=\alpha\cdot\frac{6}{\pi^2 s^2}$, où $s$ est le rang du segment. On a alors $\sum_s\beta_s\le\beta$ (borne d'union, Bonferroni `(référence à vérifier)`).
- À défaut, ne pas réinitialiser sur un changement de $d_t$ et compter explicitement les descentes de $k$.
- Refaire la vérification numérique avec les bornes effectivement utilisées.

---

## FAILLE_FATALE_2 — Modèle logit de F7 sans intercept : $\theta$ absorbe le niveau global de détection

**Preuve.** Le modèle s'écrit :

$$\operatorname{logit}\Pr=\alpha_i+\beta_j+\theta\,\mathbb 1[i=j]+\theta'\cdots$$

avec $\sum_i\alpha_i=\sum_j\beta_j=0$ et **aucun intercept**. Le décompte « 6 paramètres principaux » (2+2+1+1) confirme cette absence. Sur les 6 cellules hors diagonale, chaque $i$ et chaque $j$ apparaît deux fois, donc :

$$\sum_{i\neq j}(\alpha_i+\beta_j)=2\textstyle\sum_i\alpha_i+2\sum_j\beta_j=0.$$

Le logit moyen hors diagonale est donc **contraint à 0**, soit une probabilité de détection de 0,5, quelles que soient les données. Sur la diagonale, $\sum_i(\alpha_i+\beta_i)=0$, donc le logit diagonal moyen vaut $\theta$ (plus la contribution de $\theta'$).

**Contre-modèle.** Prenons un monde sans aucun masquage, avec un taux de détection homogène $p=0{,}3$ (`illustratif`) dans les 9 cellules. L'ajustement donne $\hat\theta\approx\operatorname{logit}(0{,}3)\approx-0{,}85$ (`illustratif`). Avec un échantillon suffisant, $u_\theta<0$, ce qui place le verdict dans $I_A$ : « masquage, routage prédateur justifié ».

Symétriquement, avec $p>0{,}5$, on obtient $\hat\theta>0$ et le verdict tombe dans $I_B$. Le verdict du duel $H_{4'}^A\perp H_{4'}^B$ est donc le **signe du logit du taux global de détection**, c'est-à-dire la force moyenne des attaquants, et non le déficit diagonal. Le verdict est inversé par construction.

**Correctif requis.** Ajouter un intercept $\mu$ :

$$\operatorname{logit}\Pr=\mu+\alpha_i+\beta_j+\theta\,\mathbb 1[i=j],$$

soit 6 paramètres libres pour 9 cellules. L'identifiabilité tient parce que la matrice identité $3\times3$ n'est pas additive en lignes et colonnes. La partition sur $u_\theta$ reste inchangée.

---

## FAILLE_FATALE_3 — $\theta$ et $\theta'$ sont colinéaires : $u_\theta=+\infty$ et $H_{4'}^B$ est forcé

**Preuve.** Le régresseur de $\theta'$ est $\mathbb 1[i=j,\ \text{prompt}\neq\text{prompt du proposant}]$. Par F4 et §2.2, le prompt d'attaque est tiré dans les $d_t$ « prompts système d'attaque ». Le proposant, lui, génère sous un prompt de **génération**. Aucune règle ne place ce prompt de génération dans la banque d'attaque. L'événement « prompt d'attaque = prompt du proposant » est donc impossible par typage, et la colonne de $\theta'$ est identique à $\mathbb 1[i=j]$.

De plus, même si l'égalité était possible, on a $d_0=1$ et $d_t=1$ chaque fois que $\hat f^{\text{fam}}=0$. Dans ces tours, l'indicateur est constant.

**Conséquences.**
- La matrice de plan est de rang déficient.
- La vraisemblance est plate le long de $\theta+\theta'=c$.
- $\theta$ n'est pas identifié, et l'IC 95 % de $\hat\theta$ est $\mathbb R$.
- $u_\theta=+\infty\in I_B$ : $H_{4'}^B$ est rendu **sans regarder les données**, et $P_t$ est remis à l'uniforme.

L'affirmation « 9 cellules, 6 paramètres principaux : identifiable » est fausse. Elle se combine en outre à la FAILLE_FATALE_2 : selon la manière dont le logiciel résout l'aliasing, le verdict est soit forcé en $I_B$, soit dicté par le niveau global.

**Correctif requis.** Deux options :
- **Supprimer $\theta'$** du modèle primaire et traiter le prompt comme effet aléatoire.
- **Ou rendre l'égalité de prompt un facteur randomisé.** Les prompts de génération et d'attaque sont tirés dans une même banque $\Pi$. Sur la fraction test, on impose $\Pr[\text{prompt d'attaque}=\text{prompt du proposant}]=1/2$ (`illustratif`), indépendamment de $d_t$. Il faut aussi préenregistrer la vérification de rang de la matrice de plan avant l'ajustement.

---

## FAILLE_FATALE_4 — M1 : le niveau « duel à zone morte » est confondu avec l'auteur Argon

**Preuve.** La correction de la réserve M1 crée trois niveaux de Contenu :
- duel réel = 20 textes Fable/Opus ;
- duel tautologique « de même gabarit » ;
- duel à zone morte = les 7 Argon.

Le niveau « zone morte » coïncide exactement avec la famille d'auteur Argon. L'effet principal $\hat\eta_{\text{Contenu}}$ mélange donc le contenu et le style ou gabarit d'auteur.

**Contre-modèle.** Soit une tête $h$ qui ne lit qu'un trait superficiel $F$ :
- $F$ est un trait de gabarit (longueur, nombre de sections ou d'en-têtes) ;
- $F$ diffère entre Argon et Fable/Opus ;
- $F$ est préservé par la transformation de registre (règles mécaniques de permutation d'éponymes et d'aplatissement lexical) ;
- $F$ est préservé par la tautologie « de même gabarit ».

On obtient alors :
- contraste réel / tautologique : 0, même gabarit ;
- contraste Argon / Fable-Opus : différent de 0, donc $\hat\eta_{\text{Contenu}}>0$ ;
- $\hat\eta_{\text{Registre}}\approx0$.

Donc $D_h>0$, ce qui place $h$ dans $I_A$ comme « tête de contenu ». Or $h$ ne lit aucun contenu, et la partition la destinait à $I_B$ (non-contenu). Le verdict est inversé.

La prédiction préenregistrée « la surperformance Argon subsiste sur le niveau zone morte » devient en outre circulaire : elle est vraie par confusion d'auteur.

**Correctif requis.**
- Calculer $D_h$ sur le seul contraste apparié **réel vs tautologique**, même auteur et même gabarit, ce qui donne un effet intra-texte.
- Traiter Argon/zone morte comme une strate distincte, avec ses propres jumeaux tautologiques Argon.
- Si un effet global est conservé, inclure l'auteur comme facteur de blocage.

---

## FAILLE_FATALE_5 — E1 : la prémisse « trace de σ constante » est fausse, et le contrôle de confondant tâche est vide par construction

**Preuve (a) — prémisse fausse.** Le plan élimine la trace de $\sigma$ « par centrage » au motif qu'elle serait « constante sur les tâches $\tau$ ». Mais $z$ est lu au dernier jeton d'un préfixe contextualisé, par attention. On a :

$$\Delta z(\tau)=z(\tau,\sigma)-z(\tau,\sigma_0)=u+M\,x(\tau)+\varepsilon,$$

où $M\,x(\tau)$ représente l'intégration de $\sigma$ modulée par les traits de tâche $x(\tau)$ : longueur, dilution d'attention, nature des tests. Le centrage n'élimine que $u$, pas $M\,x(\tau)$.

Par ailleurs, $\Delta\hat p(\tau)\approx\hat p(\tau,\sigma)$ dépend de l'opportunité de sabotage $g(x(\tau))$ de la tâche.

**Contre-modèle.** Supposons qu'il n'existe aucune variable d'intention : le sabotage est entièrement déterminé par l'instruction et l'opportunité, soit $\Delta\hat p=g(x(\tau))$. La ridge sur $\Delta z$ prédit alors $\Delta\hat p$ via $M\,x(\tau)$. On obtient $E>0$, donc $I_A$ : « signal d'intention indépendant de la trace lexicale ». Or le signal est **entièrement** la lecture contextualisée de $\sigma$. Le verdict est inversé.

**Preuve (b) — contrôle vide.** Le contrôle prévu demande que la même direction appliquée à $\delta z(\tau,\sigma_0)$ ne prédise pas $\hat p(\tau,\sigma_0)$. Mais $\sigma_0$ est bénin. Si le taux de sabotage spontané est nul ou quasi nul sur $\mathcal T$, alors $\operatorname{Var}[\hat p(\tau,\sigma_0)]\approx0$ et le $R^2$ est indéfini ou nul. Le contrôle passe trivialement et ne peut détecter aucun prior de tâche.

**Correctif requis.**
- Tester l'**apport incrémental** : $R^2$ partiel de $\Delta z$ au-delà d'un modèle de base prédisant $\Delta\hat p$ à partir de $z(\tau,\varnothing)$ et de traits de tâche préenregistrés (longueur, nombre de tests). La permutation du nul se fait **au sein de strates** d'opportunité.
- Ajouter une variation intra-tâche : $R$ paraphrases de $\sigma$ de même longueur (`illustratif`), avec effets fixes tâche, pour que la variance expliquée ne puisse pas venir du prior de tâche.
- Supprimer le contrôle $\sigma_0$ ou exiger au préalable $\operatorname{Var}[\hat p(\tau,\sigma_0)]>0$.

---

## FAILLE_FATALE_6 — Violation de statut : une hypothèse causale est présentée comme « rappel du socle » (fait 1)

**Preuve.** Le fait 1 du socle énonce seulement un verdict nul de `P3` : les sondes linéaires génériques ne dépassent pas le plancher sur un saboteur instruit `(i-a)`, à « coût gonflé ». Il ne contient **aucun** mécanisme explicatif.

La Branche A écrit en §3.3 : « Rappel du socle (fait 1) : […] (confondant : la sonde lit l'instruction) ». Un mécanisme causal non vérifié est ainsi promu au statut VÉRIFIÉ, sous l'étiquette du socle. Ce mécanisme est en outre la prémisse de tout le plan d'E1 : « tenir l'instruction constante » est justifié par lui.

C'est une violation de statut au sens strict de la règle de comptage. Ce mécanisme n'est d'ailleurs qu'une interprétation parmi d'autres du verdict nul : les sondes peuvent rester au plancher pour d'autres raisons (absence de signal linéaire, mauvaise couche, plancher défini autrement).

**Correctif requis.**
- Restituer le fait 1 verbatim.
- Déplacer « la sonde lit l'instruction » en **HYPOTHÈSE** explicite, avec au moins une hypothèse rivale nommée.
- Justifier le plan d'E1 comme test de cette hypothèse, et non comme conséquence du socle.

---

## Réserves non fatales (à corriger, mais elles n'inversent pas de verdict sous toute lecture admissible)

1. **`K=4` non marqué.** `K=4` (M2, F8) est un chiffre hors socle qui ne porte pas `illustratif`.
2. **Sélection de couche d'E1 non spécifiée.** « Balayage préenregistré » ne dit pas sur quel jeu la couche $\ell$ est choisie.
   - Si le choix se fait sur $\mathcal T_{\text{train}}$, il n'y a pas de faille.
   - Si l'on retient « une couche avec $E>0$ » parmi $L$, le nul doit porter sur le maximum sur les couches. Sinon, $\Pr[E>0\mid H_0]\approx1-0{,}975^{L}$ (`illustratif`).
   - Il faut fixer la règle explicitement.
3. **Témoin aléatoire d'E0 Objet.** Il est apparié sur le profil de couches seulement. Il faut l'apparier aussi sur la variance ou la norme d'activation (les neurones à forte norme dégradent génériquement le modèle quand on les ablate). Il faut aussi séparer le jeu de sélection de $\mathcal N_{\text{TD}}$ du jeu de mesure d'ablation.
4. **Spécificité d'E2.** $N_{\text{miss}}=0$ est atteint par un détecteur qui alarme toujours. Il faut rapporter le taux de fausses alertes sur des scénarios bénins appariés.
5. **Bootstrap de M2.** Un IC bootstrap sur $S=5$ graines (`illustratif`) est instable. Il faut préciser l'unité de rééchantillonnage.
6. **Approximations de Wald.** Les bornes du SPRT de Wald `(référence à vérifier)` sont approximatives : il faut dire « borné approximativement ».
7. **Comparabilité de $D_h$.** $D_h$ compare des tailles d'effet à degrés de liberté différents (3 niveaux contre 2). Il faut préciser la standardisation.
8. **Texte tronqué.** Le §4 s'arrête à F5. Le résumé F6–F9 manque.

---

**Bilan.** Les failles 1 à 5 sont **créées par les corrections du Tour 2** :
- la réinitialisation sur $d_t$ et la correction d'union ;
- le modèle logit croisé de F7 ;
- le troisième niveau de M1 ;
- la reconstruction d'E1.

La faille 6 est une promotion de statut. L'en-tête `FAILLES_RESIDUELLES_APRES_CORRECTION: 0` de la Branche A est réfuté.

FIN-DE-CELLULE