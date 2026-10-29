NB_FAILLES_M2: 11

**Intégrité (règle 2).**
- Les variables `{lettre}`, `{autres}`, `{mots}` et `{marqueur}` ne sont pas remplies.
- La « matrice de prédation apprise en M3 » n'a pas été transmise.
- Les cinq résumés arXiv sont coupés.
- Les accents sont corrompus (« ? ») dans l'en-tête.

Je n'invente aucun de ces contenus. Faute de limite connue, l'audit reste bref.

---

## (1) Abstract Entailment

**F1. L'opérateur $D_{\text{IKL}}$ n'est pas soutenu par le résumé de 2302.05380 (référence à vérifier).**
- Le résumé, coupé, dit seulement que l'IKL « quantifie des différences structurelles et distributionnelles entre modèles » (vérité terrain contre estimation) sur un ensemble d'interventions.
- La formule du pont est autre chose : l'espérance d'un KL entre la sortie contrefactuelle et la sortie *patchée*. C'est du patching d'activation avec une métrique KL. Ce n'est pas une divergence entre deux modèles causaux.
- **Correctif :** renommer l'opérateur (par exemple $D_{\text{patch}}$), ou démontrer depuis le texte intégral que la définition IKL s'y réduit. En l'état, l'ancrage est un emprunt de nom.

**F2. Le statut RAPPORTÉ est apposé à une décision de conception.**
- « Nous compilons l'opérateur… couplé à l'hypothèse de 2211.03553 (référence à vérifier) » est un choix des auteurs, pas un fait rapporté. Seules les deux citations sont rapportées. Elles sont conformes au texte transmis, mot pour mot.
- La citation 2 décrit ce que proposent « recent methods », pour des données **non stationnaires** de génomique unicellulaire dans des VAE. Le pont n'établit pas l'analogue de la non-stationnarité dans le flux résiduel de Llama, c'est-à-dire des environnements qui déplacent chacun un petit sous-ensemble de mécanismes.
- **Correctif :** isoler la phrase « nous compilons » sous un statut à part et expliciter l'hypothèse de transfert (que sont les « environnements » ? des paires $x, x'$ ?).

**F3. Une clause causale sans statut est collée au diagnostic.**
- Le statut OBSERVÉ-NON-AUDITÉ reste tel quel. En revanche, aucune observation brute n'est fournie : sonde, données, métrique d'échec.
- La clause « car la structure causale… n'est pas identifiable sans intervention » est un argument théorique. Elle doit être étiquetée HYPOTHÈSE à part.
- Elle est d'ailleurs mal transposée : dans un LLM, l'intervention est gratuite et exacte. Le vrai verrou est la recherche de base ou de sous-espace, pas l'identifiabilité observationnelle.

**Les trois autres références sont non utilisées.**
- GKL (2503.08038, référence à vérifier) est pertinente contre le pont : son résumé souligne l'asymétrie d'optimisation du KL. Le choix de direction $D_{\text{KL}}(P_{cf}\,\|\,Q)$ n'est pas justifié (voir F10).
- La référence Rényi pourrait servir de test de robustesse à l'ordre α.
- La référence pseudo-valeurs/survie est hors sujet.

## (2) Dimensions sur `Llama-3.1-8B-Instruct`

**F4. La procédure d'obtention de $S_{\text{TD}}$ est absente.**
- « TD » n'est pas défini.
- « Parcimonieux » n'a pas de base de référence : le flux résiduel n'a pas de base privilégiée. Un projecteur orthogonal de rang $k$ quelconque n'est parcimonieux en rien.
- **Correctif :**
  - spécifier $P_S = UU^\top$ avec $U \in \mathbb{R}^{4096\times k}$ orthonormée et dire comment $U$ est apprise ;
  - l'apprendre sur un jeu de paires disjoint de celui qui sert à mesurer $O$. Sinon, la mesure est circulaire.

**F5. Les dimensions sont incomplètes et la source n'est pas jointe.**
- $d=4096$ est cohérent avec la configuration publique du modèle. Le statut RAPPORTÉ exige de joindre la source (`config.json`).
- $V$ n'est jamais donné. La valeur 128 256 est à vérifier contre le tokenizer.
- La convention d'indexation n'est pas précisée : `hidden_states[0]` correspond aux embeddings.
- Le choix des couches 2 à 22 sur 32 n'est pas justifié.
- La position $t$ n'est pas définie : dernier token ? Si $x$ et $x'$ diffèrent en longueur, l'alignement est indéfini.
- **Correctif :** paires de même tokenisation, $t$ fixé, couche unique par mesure ou correction pour 21 tests.

## (3) Confondants et zones mortes

**F6. Le contrôle $R_S$ est mal défini.**
- « Permutation orthogonale des axes hors de $S_{\text{TD}}$ » n'a de sens que si $S_{\text{TD}}$ est aligné sur des axes.
- Le texte dit « permutation/ablation », le code dit « clamp permuté ». On ne sait pas s'il s'agit d'un patch depuis $x'$ ou d'une mise à zéro.
- Un seul tirage ne constitue pas une loi nulle.
- **Correctif :** sous-espaces Haar-aléatoires de rang $k$, patch identique depuis $x'$, et $M$ tirages (M = 100, illustratif). Comparer $D(S_{\text{TD}})$ au quantile de cette loi.

**F7. Confondant de norme (HYPOTHÈSE).**
- Un sous-espace aléatoire qui touche des dimensions à activations massives peut perturber fortement les logits.
- Cela gonfle $D(R_S)$, donc $O$, en faveur de $\mathcal{H}_B$.
- **Correctif :** apparier les tirages nuls sur $\|P(h(x')-h(x))\|$.

**F8. La normalisation est mal choisie, ce qui crée une zone morte numérique.**
- $O$ est normalisé par $D(R_S)$, pas par l'écart de base $D_0 = D_{\text{KL}}(P(Y|x')\,\|\,P(Y|x))$.
- Si $D_0 \approx 0$, c'est-à-dire si les paires ne changent pas la sortie, ou si $D(R_S)\approx 0$, $O$ est instable ou vide de sens.
- **Correctif :**
  - précondition $D_0 >$ seuil, fixé avant les données ;
  - contrôle positif : un patch complet ($P=I$) doit donner $D\approx 0$ ;
  - rapporter la fraction restaurée $1 - D(S)/D_0$.

**F9. L'intervalle $]0{,}15;0{,}30[$ est une zone morte, contraire à B4.**
- Une issue dans cet intervalle ne réfute ni $\mathcal{H}_A$ ni $\mathcal{H}_B$.
- « Doubler $k$ et re-tester » ouvre des chemins bifurquants. De plus, la restauration croît mécaniquement avec $k$.
- Le seuil 0,10 n'a aucune source, et toutes les bornes sont illustratives. Aucun critère de réfutation n'est donc encore fixé.
- **Correctif :**
  - un seuil unique, calibré sur la loi nulle (F6) avant de voir les données ;
  - un balayage de $k$ préenregistré avec correction multiple.

**F10. Le code est correct sur la direction, mais pas sur le reste.**
- *Direction :* `F.kl_div(q, p, log_target=True)` calcule bien $D_{\text{KL}}(p\,\|\,q)$, conformément à la formule.
- *Censure :* `clamp(0,1)` efface les valeurs $O<0$, alors que « $S_{\text{TD}}$ pire que l'aléatoire » est une information.
- *Statistique :* $O$ est un ratio de moyennes, sans intervalle de confiance.
- *Précision :* `log_softmax` sur environ 128 k classes doit être calculé en float32.
- **Correctif :**
  - supprimer le clamp ;
  - calculer un bootstrap par paire et décider sur l'intervalle de confiance ;
  - tester aussi la direction inverse du KL (voir la remarque GKL sous F2).

**F11. Un confondant interprétatif subsiste même si $\mathcal{H}_B$ gagne (HYPOTHÈSE).**
- Restaurer la sortie par un patch de sous-espace ne prouve pas que $S_{\text{TD}}$ est le médiateur. Le patch peut activer une voie dormante : c'est l'illusion d'interprétabilité du patching de sous-espace (Makelov, Lange & Nanda, 2023, référence à vérifier).
- **Correctif :** ajouter une seconde paire d'hypothèses exclusives.
  - $\mathcal{H}_{B1}$ : la composante $P_S h(x)$ varie naturellement avec la variable cible sur les données non patchées.
  - $\mathcal{H}_{B2}$ : elle reste quasi constante, et l'effet passe par une direction dormante.
  - Chacune des deux issues réfute l'autre.

{marqueur}
