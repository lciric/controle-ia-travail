# Collisionneurs v8d, compte rendu 25 : essaim, contre-lecture de la v1 et réponse 13 portées dans une v2 (sans dépense)

22 novembre 2026, 06:30Z.

- Contre-lecture de la v1 par un Opus neuf : **à corriger**. Bloquants : B1 anonymat rompu (identifiants à compteur, ordre de publication : un salon signé se recolle à la prépublication et aux revues du même auteur) ; B2 un agent peut forger un bloc d'arbitre dans une prépublication, servi dans les invites des autres. Le reste tient (tout appel par `executer_cellule`, devis recalculé à l'identique, hasard et reprise). Huit remarques.
- La v2, en cours chez le développeur (Opus 5.5), porte B1, B2, les remarques, et les choix de la réponse 13 de Fable (2153c96c…) : part par modèle = sa référence isolée, enveloppe = somme ; parts non bloquantes pour le pilote ; cycles = le plus grand de 2 à 4 qui tient (commande `cycles`) ; ordre simultané ; salons et revues reçues servis en entier ; noms de modèle signalés puis publiés (défaut de Fable, contre la remarque R1 du contre-lecteur ; réglable), décompte dans `verifier` ; temps 0 = III.1 mot pour mot sans en-tête ; consignes de Fable mot pour mot ; simulation du coût d'un cycle sur les journaux existants (commande `simuler`, sans dépense, sans lecture des textes).
- Puis vérification par le même contre-lecteur. Rien ne part avant le mot de Lazar.
