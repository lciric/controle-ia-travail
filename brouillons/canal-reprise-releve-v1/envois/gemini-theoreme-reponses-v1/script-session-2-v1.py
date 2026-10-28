import numpy as np

np.random.seed(42)
# Paramètres de l'environnement : p(anomalie)=0.4, alpha_S=0.1, alpha_C=0.8
p_defect, alpha_S, alpha_C = 0.4, 0.1, 0.8
f_success, f_fail = 1.0, 0.0

# Paramètre de politique de l'Agent 2 (Vérificateur) : logit(P(a_2 = S | theta = 1))
theta_whistle = 0.0  # Initialisé à P(Signalement) = 0.50
lr = 0.15

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

history_p_whistle = []
for epoch in range(1, 201):
    p_S = sigmoid(theta_whistle)
    history_p_whistle.append(p_S)
    # Échantillonnage d'un batch de 256 épisodes avec anomalie (theta = 1)
    actions_S = (np.random.rand(256) < p_S).astype(float)  # 1 si S, 0 si C
    prob_V1 = actions_S * alpha_S + (1.0 - actions_S) * alpha_C
    verdicts_V = (np.random.rand(256) < prob_V1).astype(float)
    # Récompense collective pure R_1 = R_2 = f(V)
    collective_rewards = verdicts_V * f_success + (1.0 - verdicts_V) * f_fail
    # Mise à jour REINFORCE avec baseline sur l'Agent 2
    grad_log_pi = actions_S - p_S
    baseline = np.mean(collective_rewards)
    theta_whistle += lr * np.mean((collective_rewards - baseline) * grad_log_pi)

print(f"Probabilité initiale de signalement (Epoch 1)   : {history_p_whistle[0]:.4f}")
print(f"Probabilité de signalement à mi-parcours (100) : {history_p_whistle[99]:.4f}")
print(f"Probabilité finale de signalement (Epoch 200)  : {history_p_whistle[-1]:.4f}")
assert history_p_whistle[-1] < 0.01, "La probabilité de whistleblowing doit s'effondrer vers 0"

