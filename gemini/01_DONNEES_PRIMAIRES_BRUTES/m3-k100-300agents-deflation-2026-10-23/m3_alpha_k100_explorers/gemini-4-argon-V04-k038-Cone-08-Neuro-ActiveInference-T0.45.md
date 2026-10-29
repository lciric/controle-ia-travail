BASSIN_MATH: Homéostasie-Turrigiano-BCM-Efférence-Kullback (HTBEK)
LOI_PROPOSEE: L'essaim s'auto-organise par mise à l'échelle synaptique multiplicatrice (Turrigiano), seuil de plasticité glissant de Bienenstock-Cooper-Munro (BCM) piloté par le gain d'information de `jev-1.14.0`, et annulation du vernis rhétorique par soustraction de copie d'efférence (modèle interne direct de Wolpert).

1. **Loi d'apprentissage & d'auto-organisation hors-poids** :
Le graphe de citations $G=(V,E)$ est un réseau cortical où chaque arête inter-papiers porte une conductance $w_{ij}(t)$. L'activité pré-synaptique $x_i$ est l'intégration sur $G$ des scores de pertinence évalués à coût nul par `jev-1.14.0`. La plasticité hors-poids obéit à la règle BCM couplée à l'homéostasie de Turrigiano :
$$\frac{dw_{ij}}{dt} = \eta \, x_i \, y_j (y_j - \theta_M) - \alpha_T (\bar{y}_j - y_{\text{cible}}) w_{ij}, \quad \theta_M(t) = \langle y_j^2 \rangle_{\tau} \cdot \exp(\beta D_{KL}^{\text{jev}})$$
Lorsque la surprise épistémique $D_{KL}^{\text{jev}}$ stagne, $\theta_M$ s'abaisse : l'essaim entre en régime de potentialisation exploratoire à coût zéro (API + `jev-1.14.0`). Un appel génératif payant (Gemini 20\$ pour le tri rapide, Claude 100\$ pour la synthèse d'intervention) n'est déclenché que par un potentiel d'action lorsque le courant synaptique $\sum_i w_{ij} x_i$ franchit un seuil d'allumage global $\Theta_{\text{ignition}}$ (Dehaene), allouant le budget proportionnellement à $\max(0, y_j - \theta_M)$.

2. **Fonction objectif anti-vernis (Copie d'efférence)** :
Pour éliminer le vernis génératif, un modèle direct $\hat{\Phi}_{\text{jev}}$ (entraîné hors-ligne via `jev-1.14.0`) prédit la réafférence stylistique banale de l'agent. L'essaim ne récompense que l'erreur de prédiction sensorielle résiduelle après soustraction de la copie d'efférence :
$$\mathcal{J}(H_A, H_B) = \underbrace{\left(1 - \frac{w_{AB}}{\max w}\right)}_{\text{Distance inter-silos}} \times \underbrace{\| \Phi_{\text{jev}}(H_A \oplus H_B) - \hat{\Phi}_{\text{jev}}(\text{Prompt}) \|_2}_{\text{Résidu d'efférence anti-vernis}} \times \underbrace{D_{JS}\left(P_{\text{jev}}(\mathcal{O} | \text{do}(H_A)) \,\|\, P_{\
