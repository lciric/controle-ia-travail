BASSIN_MATH: Routage-Énergie-Libre-Attendue-Précision-Hiérarchique (REPH)
LOI_PROPOSEE: π* = argmin_π G(π) , G(π) = −E_q[ I(s ; o | π, famille m) ] + D_KL[ q(o|π) ‖ p(o|C) ] + λ·coût_USD(π) , avec I pondérée par (1−ρ_m) où ρ_m = corrélation d'erreurs intra-famille estimée par jev-1.14.0.

1. **Mécanisme hors-poids.** L'essaim est un modèle génératif hiérarchique : niveau 0 = consigne, niveaux k = sous-agents délégués. Chaque délégation envoie une prédiction descendante (consigne reformulée) ; le sous-agent renvoie l'erreur de prédiction ε_k = o_k − ĝ(consigne_k). La dérive H9 est l'accumulation Σ_k D_KL[q_k(consigne) ‖ q_0] ; elle est corrigée par précision adaptative Π_k ∝ 1/Var
