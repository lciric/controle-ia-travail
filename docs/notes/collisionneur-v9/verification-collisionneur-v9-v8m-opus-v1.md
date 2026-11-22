# Vérification de la v8m (420394f9…), v3

**Verdict : à corriger, par un essai seulement ; le code est juste.** 518 essais passent, 11 sont sautés, sans aucune clé.

**L'argent, à la lecture du code et par les mutants**
- **Au plus trois envois par cellule et par lancement.** Si le premier essai finit vide en `max_tokens`, le rejeu prend la place de la relance : deux envois. Si la relance finit vide, le rejeu vient après : trois envois. Un rejeu encore vide passe au code 9, rien n'est écrit, et la cellule n'est plus renvoyée à la reprise.
- **Garde et devis.** Avant le rejeu, le pire cas, le plafond et la ligne sont vérifiés comme pour tout envoi, au plafond de relance. La déclaration vient après ces gardes, avant l'envoi. Le devis de reprise compte deux relances sous `--effort-max`.
- **« xhigh » documenté** pour Fable 5.2, Fable 5.1 et Opus 5.5. Opus 4.6 ne va que jusqu'à high puis max : son rejeu part bien à « high ».
- **Opus 4.6 :** réflexion adaptative, « high » sans l'option, « max » avec.

**Sans option :** aucun écart avec la v8l sur 484 compositions, avec et sans options, pour les réglages, le devis et le sceau. La seule différence est l'effort d'Opus 4.6, qui était voulue.

**Bloquant**
1. Le rejeu ne doit partir que sur « max_tokens sans texte ». Aucun essai ne l'éprouve contre une fin `end_turn` vide : le mutant qui rejoue aussi dans ce cas survit (J3). Correction : un essai où une réponse vide finie en `end_turn` sous `--effort-max` donne VIDE, sans aucun rejeu ni déclaration.

**Non-bloquants**
- Le mutant J11 survit, mais il est équivalent : un rejeu vide s'arrête au code 9 avant toute nouvelle décision de rejeu.
- Si un rejeu est refusé par le plafond ou la ligne, la relance suivante reprend la cellule au premier essai, et non au rejeu. Ce comportement existait déjà chez Anthropic.
- K5, K13 et K14 survivent, comme avant.

**Mutants :** 18 rejoués, 13 pris, 5 survivants (J3, J11, K5, K13, K14). Programme : `verif-v8k/mutations_v3.py`.
