# Contre-lecture du collisionneur v9-v8r (garde d'entrée de l'arrière-plan = 4 × (entrée du flux + sortie maximale prévue))

- **Classe B.** Auteur : session fille des collisionneurs (Opus 5.5). Contre-lecteur : un Opus 5.5 neuf, sous-agent, distinct des précédents, qui n'a pas écrit le code ; essais sur des copies, aucun réseau, `git status` propre. 24 novembre 2026.
- **Verdict : conforme**, trois remarques mineures, aucune double multiplication, aucun affaiblissement de la garde Google commune.
- **Essais du contre-lecteur** :
  - en flux, rien ne change ; en arrière-plan, la garde (4 × (1 050 + 65 536 + 32 768) = 397 416) entre dans le pire cas, dans juger et dans le journal ;
  - une entrée au-delà de la garde est arrêtée ;
  - rejugement juste dans les trois cas : essai v8o, essai v8p ou v8q, essai v8r ; garde de 680 516 pour la critique croisée de Carbon des bancs plantés ;
  - `verifier` de la v8r tient sur les deux copies, y compris le rejugement écrit en v8q ;
  - devis juste : 28,74 USD au pire, étage III de la dynamique de l'évasion, sans relance.
- **Remarques gardées, déclarées, sans nouvelle version** :
  - (R1) trois textes disent encore « × 4 » : la docstring de `ecarts_rejugement_arriere_plan`, le motif écrit dans la ligne de rejugement et l'aide du devis. La garde calculée et journalisée est juste ; le texte du motif est inexact.
  - (R2) pour un essai journalisé à la forme v8r, le rejugement reprend `garde_entree` telle quelle, sans la recalculer : un durcissement possible.
  - (R3) la garde est très large (environ 12,7 fois l'entrée facturée sur la dynamique) ; le devis de reprise (`pire_tours_2_3`) ne compte pas l'arrière-plan. La garde de dépense de chaque cellule le compte, donc aucun dépassement n'est possible.
