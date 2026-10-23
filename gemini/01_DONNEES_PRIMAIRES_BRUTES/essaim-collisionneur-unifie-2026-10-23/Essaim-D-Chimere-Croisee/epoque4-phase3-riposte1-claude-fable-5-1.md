BASSIN_MATH: Jauge-TD-couplée-à-la-capacité

## 1. Réponse à l'équipe rouge (sans lissage)

- **Critique « proposition vide »** : acceptée. Avec `texte=''`, l'ensemble des affirmations émises est ∅ ; toute « défense » serait une fabrication a posteriori. Je n'en produis aucune.
- **Critique « échec silencieux `echec=None` »** : acceptée. Règle d'orchestration proposée : `si texte=='' ou fin=='max_tokens' avec types_blocs==['thinking'] ⇒ echec='troncature_raisonnement'`, message exclu de l'agrégation, relance avec plafond de raisonnement.
- **Critique « risque de propagation »** : acceptée. La présente réponse est donc la *première* proposition de l'Agent #1, pas une mutation d'un contenu antérieur.

Rien à réfuter.

## 2. Opérateur corrigé

Soit $D$ l'ensemble des *Dopamine Neurons* (couches 5–22, < 1 % des neurones, socle Xu et al., `arXiv:2602.00986v2`, référence à vérifier) et $t^\*$ le jeton de délégation Agent 1 → Agent 2. Opérateur parcimonieux (non dense, cf. échec du pilotage dense, socle 3) :

$$\Phi(x)=\sum_{n\in D} w_n\,\delta_n(x,t^\*),\qquad |D|\ll d$$

avec $\delta_n$ l'erreur TD lue sur le neurone $n$. Statistique de détection, **après soust