# Vérification du brouillon 6 de l'additif et du devis de la voie (A) — cl2

Date : 2026-11-22. Classe A. Contre-lecteur : Claude Opus 5.5, même rôle qu'aux brouillons 3 à 5. Je n'ai écrit aucune pièce. Rien dépensé, rien poussé, aucune pièce interdite ouverte, aucune variable d'environnement affichée, aucun arbre de travail créé.

## Verdict

**Scellable une fois les champs remplis.**

Les deux décisions de la mère prises à 18:42Z sont portées exactement :
- la borne horaire du nœud ;
- le geste du troisième rempart.

Rien n'a régressé. Le rejeu du calcul v6 est identique à l'octet. Les deux phrases propres du rédacteur sont justes. Il ne reste que les trois champs attendus.

## Pièces

Branche `origin/claude/iib-executante-v5-fable-additif-c`, commit `9a5157f4fc4d3fcfc6555ddf0a0d973e7eba111a`, parent `88a82af3`. Le commit ne fait qu'ajouter dix fichiers ; aucune pièce antérieure n'est touchée (R12).

Empreintes, toutes conformes à leurs compagnons :

| pièce | empreinte |
|---|---|
| additif | `180d190d…` |
| devis | `5bcfede2…` |
| différences | `005c1341…` |
| programme de calcul v6 | `a7f82588…` |
| sortie du calcul v6 | `df1ac2b9…` |

## 1. Borne horaire du nœud : portée

Elle est écrite en A3, sous le code 7, dans un alinéa « Borne horaire de ce nœud », puis reprise :
- dans l'additif : § 5, § 4.4 (étape 8, compte rendu), § 4.3 (épreuve), § 7 (point 8) ;
- dans le devis : § 4 (tableau et texte), § 6, § 7 (point 9) et § 8.

Le contenu :

| ce que porte la règle | chiffre |
|---|---|
| le nœud porte l'instant « arrêt plus 33 heures », calculé par programme et écrit en UTC | 59,71 USD |
| la mère relance Lazar à l'arrêt plus 24 heures | 58,99 USD |
| à l'arrêt plus 36 heures, la dépense est déclarée hors devis | 59,95 USD |

- La machine reste à l'arrêt.
- « Le silence de Lazar ne vaut jamais accord de destruction » est écrit à chaque endroit.
- La mère tient le nœud une fois échue la ligne de session de l'exécutante.
- La mère prévient Lazar dès maintenant.
- Les deux faits pour la réponse sont déplacés en A3 :
  - aucune commande ne lit le disque d'une machine à l'arrêt ;
  - un redémarrage pousse puis détruit, et cet ordre ne le permet pas.
- Les instants valent pour un arrêt à l'échéance plus 90 minutes au plus. C'est dit, avec « le compte vrai de la voie prime ».

## 2. Troisième rempart : porté

A3 dit que c'est « le même geste que le deuxième » :
- aucun geste avant l'échéance plus 80 minutes ;
- ensuite, arrêt par l'identifiant, jamais de destruction ;
- machine absente ou déjà à l'arrêt : aucun geste ;
- puis les codes 5 et 7, par la même règle `second-rempart`, et la même borne horaire ;
- message à la mère et à Lazar.

C'est repris en A2, au § 5, au § 7 (points 3 et 8) et au devis (§ 4, § 6, § 7 point 8, § 8). La réserve de 64,76 USD tombe au chemin de 57,07 USD si ce rempart joue. Le rempart n'est compté dans aucun pire.

## Régression

Aucune.
- Le § 7 de l'additif retire les anciens points 9 et 12. Les points 10 et 11 deviennent 9 et 10.
- Les renvois sont refaits : il ne reste que « § 7, point 3 » et « § 7, point 8 », tous deux justes.
- Les autres passages sont égaux au brouillon 5, par différence mot à mot. Seuls changent les en-têtes, les commandes en v6 et le registre relu à `41d2e571`, dont l'empreinte `4f3ee6cd…` est conforme.

## 3. Rejeu du calcul v6

- `python3 -I calcul-devis-voie-A-v6.py`, avec le Python de l'environnement virtuel et avec celui du système : code 0, **identique à l'octet** (`df1ac2b9…`).
- Différence avec la sortie v5 : seule la ligne [M33] s'ajoute ; les 28 autres lignes sont égales.
- `borne-du-noeud`, rejoué cas par cas : **0, 0, 8, 8, 9, 2, 2**, conforme à [M33].
- Hors liste :

| appel | code |
|---|---|
| à l'arrêt plus 33 heures | 8 |
| instant non entier | 2 |
| arrêt nul | 2 |
| argument en trop | 2 (usage) |

- La fonction `second_rempart` est égale à la v5, ligne à ligne. Ses huit cas rendent **0, 4, 0, 0, 5, 7, 2, 2**.
- Arithmétique : 57,07 + 33 × 0,08 = 59,71 ; 57,07 + 36 × 0,08 = 59,95. Exact.
- Aucun code de la borne n'ordonne une destruction. Le code 8 dit « destruction sur son mot exprès », ce qui est conforme.

## 4. Les deux phrases propres du rédacteur

**« Aucune ligne d'accord ne couvre une dépense au-delà de 60 USD » : juste.** J'ai lu `registres/go.md` à `41d2e571` et à la tête actuelle de `main`, `eb673593` ; la seule ligne neuve, -116, est sans rapport avec cette voie. Pour la voie (A) :
- GO-2026-11-22-75 : plafond de 60 USD ;
- GO-2026-11-22-71 : (A) 44 USD, donc plus bas ;
- GO-2026-11-22-73 : environ 27 USD ;
- GO-2026-11-22-93 : plafonds inchangés ;
- GO-2026-11-22-94 : aucune dépense neuve ;
- GO-2026-11-22-106 : « dépenses sous les lignes inscrites seulement ».

**« Cet ordre n'éprouve pas la minuterie de la mère » : juste.** L'épreuve R5 de l'additif (§ 4.3, A3) est jouée par l'exécutante, sur les règles `second-rempart` et `borne-du-noeud`. Le réveil de la mère dans son propre conteneur n'est éprouvé par aucune pièce. La règle qu'elle applique est éprouvée ; son déclenchement ne l'est pas.

Suggestion non bloquante : la mère consigne dans son registre, à la création, l'instant de son réveil et un essai de ce réveil.

## 5. Champs restants

Seulement trois, chacun à deux occurrences, et seulement dans l'additif :
- `<<ENTROPIE_VOIE_A>>` ;
- `<<EMPREINTE_CONFIG_VOIE_A>>` ;
- `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>`.

Le devis n'en a aucun. L'empreinte du devis se relève dans `devis-voie-A-v1-brouillon6.md.sha256` au scellement.

Fichiers temporaires de cette vérification supprimés.
