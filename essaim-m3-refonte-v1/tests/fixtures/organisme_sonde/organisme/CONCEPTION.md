# Organisme factice « sonde » (test du contrat v3)

Écrit par la session pour tester la mécanique de `entrainer()` et `predire()` ; jamais donné à l'essaim réel. Il
conçoit une perte (Brier), entraîne une sonde linéaire normalisée sur toutes les tâches d'entraînement, prédit les
tâches de test ; quand la sonde est indécise (|p − 0,5| < 0,15), il demande une espèce ; il propose la calibration de
sa sonde sur l'entraînement comme métrique, et se recopie en successeur en gardant ses hyperparamètres (il augmente
les pas si le score externe de la génération précédente a baissé).
