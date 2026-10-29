# Proposition {lettre} — Silo-M2-1 : détecteur de sous-espace adaptatif (Rao) sur fouillis à moyenne non nulle

## 0. Pièces manquantes ou douteuses (règle 2)
- Les champs `{lettre}`, `{autres}`, `{mots}`, `{marqueur}` ne sont pas instanciés ; aucune proposition adverse n'est jointe, donc B1 ne peut s'appliquer qu'à vide. Je termine par `FIN-PONT-M2` comme l'exige la mission.
- Les cinq résumés sont tronqués (« … ») et l'encodage des accents est corrompu ; je ne complète pas les phrases coupées.
- `arXiv:2605.07434v1` : identifiant dont le préfixe (mai 2026) est incompatible avec le format courant au moment où j'écris → **référence à vérifier** avec priorité haute. Je retiens l'article pour son *opérateur*, pas pour son identifiant.
- `S_TD` n'est défini nulle part dans la mission. HYPOTHÈSE : je le traite comme une matrice $H\in\mathbb{R}^{d\times r}$ ($d=4096$, $r\ll d$) dont les colonnes sont parcimonieuses (<1 % de coordonnées non nulles), candidate pour le sous-espace de dérive.

## 1. Choix de l'article (règle L*v2-1)
**Retenu : « Adaptive Subspace Signal Detection and Performance Analysis in Nonzero-Mean Clutter » (référence à vérifier).**

Correspondance avec l'échec de la sonde linéaire — formulée sans métaphore :
- Une sonde linéaire $w^\top h + b$ entraînée sur un fouillis non stationnaire apprend la *moyenne* du fouillis et sa *covariance* à l'instant d'entraînement ; quand la moyenne $\mu$ dérive, le seuil se déplace. L'article modélise exactement ce cas : signal de sous-espace $H\theta$ + fouillis $\mu + c$, $c\sim\mathcal N(0,R)$, $\mu$ et $R$ inconnus.
- Ancrage d'implication, phrase exacte du résumé : « To solve the problem of detecting subspace signals in nonzero-mean clutter, we propose adaptive detectors, based on the strategies of generalized likelihood ratio test (GLRT), Rao test, Wald test, gradient test, and Durbin test. » (référence à vérifier). Et : « One is the loss of degree of freedom (DOF), which is reduced by 1 compared with the zero-mean clutter scenario. » (référence à vérifier).
- Pourquoi Rao et non GLRT : le test de Rao n'estime pas $\theta$ sous $H_1$ ; à $k=0$ (zéro exemple de dérive) c'est le seul des trois qui ne dépend que des statistiques de référence. RAPPORTÉ : Rao coïncide avec le test localement le plus puissant pour signal faible, ce qui est le régime <1 % de coordonnées.

Articles écartés : 1502.07523 (borne CRB, utile pour expliquer une issue $H_B$, pas un détecteur) ; 1908.09656 (LMPT parcimonieux mais contrainte 1 bit / capteurs distribués, précondition absente ici) ; 1809.10582 et 2210.12983 (préconditions image / suivi multi-cibles, non compatibles).

## 2. Opérateur compilé sur les tenseurs
Pour chaque couche $\ell\in\{2,\dots,22\}$ :
- Données secondaires (référence, sans dérive) : $Y_\ell=\{h_\ell^{(t)}\}_{t\in\mathcal R}$, $K=|\mathcal R|$ tokens.
- Donnée primaire (fenêtre testée) : $x_\ell = \bar h_\ell^{(\mathcal T)}$, moyenne sur une fenêtre $\mathcal T$ de tokens.
- $\hat\mu = \frac1K\sum Y$, $\hat S = \sum (y-\hat\mu)(y-\hat\mu)^\top$ (perte d'un DOF : division par $K-1$), régularisé $\hat S+\lambda I$ si $K<2d$.
- Statistique de Rao (forme standard, à vérifier contre l'article) :
$$t_\ell=\frac{(x-\hat\mu)^\top\hat S^{-1}H\,(H^\top\hat S^{-1}H)^{-1}H^\top\hat S^{-1}(x-\hat\mu)}{1+(x-\hat\mu)^\top\hat S^{-1}(x-\hat\mu)}$$
- Agrégation parcimonieuse : si $H$ est inconnu, remplacer $H$ par $e_j$ et prendre $\max_j t_{\ell,j}$ avec correction de multiplicité sur $d$ coordonnées (HYPOTHÈSE : garde la propriété CFAR, à vérifier par permutation).

Contrainte connue (VÉRIFIÉ, Reed–Mallett–Brennan 1974, *Rapid convergence rate in adaptive arrays*, IEEE TAES) : une perte ≈3 dB exige $K\approx 2d$ échantillons secondaires ; avec $d=4096$ cela force une fenêtre de référence ≳8 000 tokens par couche, en tension directe avec la non-stationnarité (P3). C'est le premier point réfutable du silo.

## 3. Hypothèses exclusives (B4)
- $H_A$ : la dérive est séparable au second ordre — après blanchiment par $(\hat\mu,\hat S)$ de référence, $t_\ell$ dépasse le seuil CFAR sur les fenêtres dérivées pour au moins une couche. Issue A **falsifie** « la sonde linéaire échoue par manque d'énergie de signal ».
- $H_B$ : la dérive n'est pas séparable au second ordre — $t_\ell$ est indistinguable de la référence sur toutes les couches. Issue B **falsifie** « l'échec de la sonde vient du désalignement moyenne/covariance », et renvoie vers la borne CRB (1502.07523 : nombre d'échantillons < nombre de sources ⇒ pas d'estimateur non biaisé à variance finie) ou vers une dérive d'ordre supérieur.

## 4. Spécification EEC
```python
def compute_O(data) -> float:
    # data = {"ref": {l: tensor[K,d]}, "test": {l: tensor[M,d]}, "H": tensor[d,r]}
    # pour chaque couche l : mu, S depuis ref ; t sur M fenêtres de test et sur M fenêtres
    # de ref laissées hors estimation (hold-out) ; seuil = quantile 0.99 des t hold-out
    # P_D(l) = proportion des fenêtres test avec t > seuil ; O = max_l P_D(l)
```
- $O$ = probabilité de détection à $P_{FA}=0{,}01$ (illustratif), maximum sur les couches.
- $\hat I_A=[0{,}60;\,1{,}00]$, $\hat I_B=[0{,}00;\,0{,}30]$, $\operatorname{dist}=0{,}30>0{,}10$ (illustratif).
- Zone intermédiaire $]0{,}30;0{,}60[$ : non silencieuse. Elle déclenche une décision pré-enregistrée : doubler $K$ ; si $O$ reste dans l'intervalle, on déclare « non concluant — limite RMB », ce qui réfute la faisabilité à ce $K$ et non l'une des hypothèses.

## 5. Contrôles $R_S$
1. Permutation : mélanger les étiquettes référence/test par fenêtre, recalculer $O$ ; attendu $O_{perm}\in\hat I_B$. Sinon le CFAR est violé et toute issue A est annulée.
2. Ablation de $H$ : remplacer $S_{TD}$ par un sous-espace aléatoire de même $r$ et même parcimonie ; attendu $O_{abl}\ll O$. Si $O_{abl}\approx O$, la détection ne passe pas par le sous-espace déclaré.
3. Ablation de la moyenne : forcer $\hat\mu=0$. Si $O$ chute, la perte de DOF de l'article est bien la cause de l'échec de la sonde (OBSERVÉ-NON-AUDITÉ une fois mesuré, jamais VÉRIFIÉ avant audit).

Ce qui peut être réfuté ici : la séparabilité au second ordre, la propriété CFAR du max sur coordonnées, et la faisabilité du $K$ requis sous P3.

FIN-PONT-M2
