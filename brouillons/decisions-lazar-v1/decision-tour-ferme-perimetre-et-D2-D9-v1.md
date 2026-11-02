# Décision — tour fermé (A2 à A4, ideation-organism) : périmètre du scellement et décisions D2 à D9 — v1

2 novembre 2026, rédigée par conv-audit après la deuxième contre-lecture neuve (`orchestrator/prereg/contre-lecture-preenregistrement-tour-ferme-v2.md`, 8a74dfd2…, dépôt public `82ad7a8`) et la lecture du brouillon 2 (`preenregistrement-tour-ferme-v1-brouillon2.md`, section 12 devis, section 14 décisions). Classe : « proposer avec recommandation » (périmètre interne d'une phase), défaut appliqué après 48 heures.

## 1. Périmètre

**Décision** : sceller l'étage 1 seul (après le code v62), ou écrire aussi l'étage 2 et sceller les deux ensemble.

**Enjeu** : l'étage 1 dit si la boucle réelle (proposeurs, gardien mécanique, tests de mort, juge gelé) retient des lois mieux qu'un bras aléatoire et qu'un bras recopie-mélange ; l'étage 2 éprouve les lois retenues sur la réserve tenue à l'écart (T), c'est-à-dire leur généralisation. Le code v62 est nécessaire dans les deux cas : la contre-lecture 2 montre que le chemin réel de l'étage 1 ne peut pas marcher (B7 : l'expérimentateur réel ne reçoit pas la loi à éprouver ; B8 : les proposeurs réels ne reçoivent pas la grammaire des lois ; B9 : la lecture gelée dit T1 sur une course saine si le bras réel ne retient rien en génération 1).

- **(a) Étage 1 seul.** Avantage : le cœur de l'étage 2 n'est pas écrit ; l'étage 1 ne touche pas T (contre-lecture 2, « Fuites de la réserve »), donc le texte de l'étage 2 pourra être scellé plus tard sans fuite, et seulement si la porte de l'étage 1 l'ouvre (si le bras réel retient trop peu, la porte refuse l'étage 2 de toute façon). Coût attendu ≈ 3,3 à 12 USD (plafond 15), 0,7 à 2,7 heures. Inconvénient : deux scellements et deux contre-lectures au lieu d'un ; la question de la généralisation attend.
- **(b) Étages 1 et 2 ensemble.** Avantage : un seul texte couvre la question entière. Inconvénient : écrire et éprouver le cœur de l'étage 2 (non écrit), brancher la réserve et ses gardes 11 et 12, D5, D6, D8 ; une contre-lecture plus lourde ; et du travail perdu si la porte de l'étage 1 refuse l'étage 2. Coût total ≈ 5 à 14 USD (plafonds 15 + 5).

**Recommandation : (a)**, confiance moyenne-haute. **Défaut sous 48 heures : (a).**

## 2. Décisions D2 à D9 (marqueurs `<<DECISION_Dn>>` du brouillon 2)

Écrites selon la recommandation de la première contre-lecture ; un refus = version nouvelle du texte.

| | Ce qui est écrit | Portée | Recommandation |
|---|---|---|---|
| D2 | fausse découverte définie par l'oracle, g₀ = 0,02 nat, nouveauté contre l'archive | étage 1 | accepter |
| D3 | témoins jamais retenus ni servis (sinon les générations 2 et 3 ne mesurent plus rien, essai L3) | étage 1 | accepter |
| D4 | bras recopie-mélange nourri par l'archive du bras réel | étage 1 | accepter |
| D5 | T entier pour les deux générations de l'étage 2, génération 1 seule décisive | étage 2 | reporter si (a) |
| D6 | bras aléatoire de contrôle à l'étage 2 (≈ 0,7 USD) ; pas de seconde réplique du bras aléatoire de l'étage 1 | étage 2 / étage 1 | reporter la première partie si (a) ; accepter la seconde |
| D7 | bras aléatoire jugé contre l'archive du bras réel de la même génération | étage 1 | accepter |
| D8 | test de mort de l'étage 2 = gain sur le prédicteur connu du moniteur | étage 2 | reporter si (a) |
| D9 | gardien mécanique seul pour les trois bras | étage 1 | accepter |

**Défaut sous 48 heures : D2, D3, D4, D7, D9 et la seconde partie de D6 acceptées ; D5, D8 et la première partie de D6 reportées au texte de l'étage 2.**

## 3. Ce qui suivra, dans l'ordre (routine, sauf le GO)

Code v62 (B7, B8, B9 et les couples de l'étage 1, T19 à T63 de la contre-lecture 2), essais, banc de mutations, répétition à blanc ; brouillon 3 ; troisième contre-lecture neuve ; chez session-depot les pièces de la section 14 (4) ; scellement ; **GO de Lazar sur le devis de l'étage 1 (plafond 15 USD)** ; course ; sortie scellée avant lecture ; verdict par un lecteur neuf (R13).
