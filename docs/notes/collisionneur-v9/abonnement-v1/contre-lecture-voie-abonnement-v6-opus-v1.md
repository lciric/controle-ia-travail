# Contre-lecture de la voie abonnement v6 (Opus 5.5 neuf)

Écrit à 2026-11-22T19:40:32Z. Classe B. Objet : voie_abonnement_v6.py, test_voie_abonnement_v6.py, ../reprise-v8d-v1/vague_abonnement_v2.sh. Motif : GO-2026-11-22-114 (« high » pour une cellule de collisionneur), demande de la mère.

- Premier passage : conforme ; diff limité à l'en-tête, VERSION, EFFORTS_SESSION (max, xhigh, high) et l'aide de --effort ; recueil v6 et script de poussée des kits sans dépendance bloquante. Non bloquants : N1 (aucun essai positif de « --effort high » en ligne de commande), N2 (le recueil v6 appelle voie_abonnement_v5.py recueillir : la fiche de réponse d'un kit v6 portera programme « voie-abonnement-v5 », écart de traçabilité seul), N3 (commentaire « v5 » dans le script de vague v2).
- Corrections : N1 (essai positif par monkeypatch, refus de « medium » en essai séparé), N3. N2 consigné, non corrigé (le recueil n'est pas modifié).
- Vérification des corrections par le même contre-lecteur : « corrections conformes » ; 38 essais sur 38.
