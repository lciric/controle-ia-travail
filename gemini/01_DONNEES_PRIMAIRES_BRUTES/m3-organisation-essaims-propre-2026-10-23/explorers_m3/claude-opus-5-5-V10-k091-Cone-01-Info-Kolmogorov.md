**BASSIN_MATH: Fourchette Gács-Körner–Wyner (FGKW)**

**LOI_PROPOSEE:** $\Delta(S)=C_W(X_S)-C_{GK}(X_S)$. On mesure les deux termes par des longueurs de code estimées avec `jev-1.14.0` utilisé comme codeur, soit $L(\cdot)=-\log_2 p_{jev}$. Sur la topologie $G$, le budget $b$ et la population $S$, l'essaim maximise $\;\mathcal{J}=\dfrac{C_{GK}^{\text{vérif}}(X_S)-\lambda\,\Delta(S)-\mu\,L(c\mid m_{\text{feuille}})}{\$}$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Information commune extraite.** $C_{GK}$, l'information commune de Gács-Körner, est la partie commune que chaque agent peut calculer seul. Concrètement, ce sont les assertions convergentes et vérifiées par Crossref, arXiv ou Semantic Scholar. C'est le consensus légitime.
- **Information commune latente.** $C_W$, l'information de Wyner, est la cause latente minimale qui rend les sorties indépendantes. Elle inclut les erreurs partagées dues aux poids communs.
- **Interprétation de la fourchette.** L'écart $\Delta$ mesure la corrélation fallacieuse, c'est-à-dire le risque H4'.
- **Arêtes.** On conserve une arête $i\to j$ si $L(x_j)-L(x_j\mid x_i)>\kappa_{\text{arête}}$ et si elle n'augmente pas $\Delta$.
- **Choix de l'agent à créer.** Si $\Delta$ dépasse le seuil $\tau$ dans une monoculture, on crée un démolisseur Red-Team de famille opposée, chargé d'attaquer précisément le code latent commun. Si $C_{GK}$ stagne alors que $\Delta$ est faible, on crée un explorateur.
- **Monoculture ou chimère.** On passe en chimère si $\Delta_{\text{mono}}-\Delta_{\text{chim}}$ dépasse l'écart de coût par dollar. Gemini, limité à 20 USD, sert d'instrument de décorrélation ciblé.
- **Dérive de consigne (H9).** À chaque délégation, on calcule $L(c\mid m)$. Si ce coût croît, on réinjecte la consigne $c$ dans le message.
- **Apprentissage sans réentraînement.** L'essaim apprend via une mémoire externe de motifs $(G,\Delta,\text{gain})$, sans modifier les poids.

**2. Fonction objectif et anti-Goodhart**

$$R=\underbrace{C_{GK}^{\text{vérif}}}_{\text{API}}-\lambda\Delta-\mu L(c\mid m)-\nu\big[L(y)-L(y\mid y_{\text{fermé}})\big]^{-}-\rho\,I_{jev}(y;\text{style favori})$$

- **Terme de récitation.** Le terme en $y_{\text{fermé}}$ pénalise le contenu compressible par une exécution à livre fermé, donc la récitation de la mémoire paramétrique.
- **Anti-Goodhart.** Le juge n'est jamais la cible directe : il sert seulement de codeur. La vérité terrain provient des graphes bibliographiques, scellés et tirés au hasard. Le terme $\rho$ pénalise les sorties qui exploitent le style préféré du juge.

**3. Duel décisif ($H_A\perp H_B$)**

- **$H_A$ :** FGKW donne un $C_{GK}^{\text{vérif}}$ par dollar supérieur.
- **$H_B$ :** un essaim fixe ou i.i.d. fait aussi bien.

Le protocole comporte 200 tâches bibliographiques avec des faits scellés et deux types de pièges : 15 % de faux plausibles et des consignes déléguées sur cinq niveaux. Le budget est strictement égal pour tous les bras (120 USD au total).

| Bras | Configuration |
|---|---|
| A | FGKW |
| B | Topologie fixe |
| C | Agents i.i.d. tirés au hasard |
| D (contrôle négatif) | FGKW avec $\Delta$ permuté aléatoirement |

**Critères d'interprétation :**

1. On attend $A>B,C$ et $A>D$, avec un test de permutation à $p<0{,}01$.
2. On attend en outre que $\Delta$ prédise le taux d'erreurs partagées sur les faux plausibles (Spearman $>0{,}5$).
3. Si $D\approx A$, la loi est réfutée.
