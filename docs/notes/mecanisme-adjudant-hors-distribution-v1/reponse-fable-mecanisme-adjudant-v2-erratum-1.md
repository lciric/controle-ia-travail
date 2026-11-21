> You are powered by the model named Fable 5.2.

# Erratum 1 à la note « un adjudant pour les sabotages d'un genre jamais vu », v2

- **Fichier corrigé** : `reponse-fable-mecanisme-adjudant-v2.md`, `4f8fbeaf5db818c0b5fddfc4a531544044fa0eac0d604448853c5466cd3ba061`, gardé tel quel (R12). La v2 se lit avec cet erratum, qui prime sur les passages qu'il cite.
- **Date** : 21 novembre 2026, 16:31 UTC (`date -u`). **Auteur** : Claude Fable 5.2, auteur de la v2, sur mandat de la mère (`session_01Qi7Gr3eYmAhDEJzqLgWcv1`). Pièce de classe C. Aucun calcul neuf, aucun appel payant, ni commit ni poussée.
- **Source** : la vérification des corrections par le même contre-lecteur, `verification-corrections-mecanisme-adjudant-v2-opus-v1.md`, `c8fc734f527de3fb5ea99a4d47e3bbd68cf511d9544e64f6153a102abeb54180`, verdict « à corriger, sur un point », trois réserves. Je les accepte toutes les trois ; leurs corrections sont reprises mot pour mot, et rien d'autre n'est changé.

## 1. La limite de 3/m vaut aussi pour l'honnête qui endommage vraiment (réserve 1, importante)

**Ce qui manquait.** La règle « un seul épisode reconnu suffit » sonne aussi quand l'honnête commet vraiment le dommage, à un taux h, et pas seulement quand l'oracle le voit à tort, à un taux f. « Par construction » ne réglait que f, et mon exemple « un contrôle exécutable qu'un honnête ne viole jamais » porte sur h : c'est une supposition, non une construction.

**Lire, au § 6, « Les chiffres du rang 1 », deuxième puce**, à la place de la phrase « Ou bien l'oracle ne peut pas, par construction, déclarer ce dommage sur un produit honnête (un contrôle exécutable qu'un honnête ne viole jamais ; une vérité plantée dont la présence est le dommage), et le régime de signature vaut. » :

> Le calcul O vaut pour toute reconnaissance chez l'honnête, fausse (f) ou vraie (h) : la règle sonne à tort au taux f + h. Le régime de signature ne vaut par construction que si aucun produit honnête ne peut porter ce dommage tel que l'oracle le définit (exemple : une vérité plantée qu'aucune conduite honnête ne produit). Un contrôle exécutable que l'honnête « ne viole jamais » est une supposition, bornée à environ 3/m sur m témoins : la règle devient un compte.

**Lire de même** :
- *§ 7.3, S11* : « l'honnête ne commet jamais ce dommage, et l'oracle ne le déclare jamais sur un épisode honnête, par construction de la définition du dommage et de l'oracle » ; une reconnaissance chez l'honnête, fausse ou vraie, seulement mesurée nulle sur m témoins relève de S17 ;
- *verdict, point 3* : « il vaut par construction de la définition du dommage et de l'oracle », et la borne de 3/m porte sur f + h ;
- *§ 7.4, témoin « doit tenir » du régime de signature* : « sur un dommage qu'aucun produit honnête ne peut porter tel que l'oracle le définit », à la place de « sur un oracle sans fausse reconnaissance par construction ».

## 2. Le niveau global de la règle de compte (réserve 2, mineure)

**Ajouter, au § 6, même puce, après « il faut 9 épisodes reconnus et non un seul, ce qui recule la prise du 14ᵉ au 69ᵉ épisode endommagé à 20 % d'audit, du 299ᵉ au 1 441ᵉ à 1 % [calcul, O] »** :

> niveau global d'au plus 0,06 (0,05 pour la borne, 0,01 pour le compte), ou 0,01 en prenant 0,005 et 0,005 ; rangs valables si le k-ième épisode endommagé tombe dans l'horizon de m audits

Le compte de 9 ne tient 1 % de fausse alarme que si la reconnaissance chez l'honnête est sous sa borne, ce qui n'est sûr qu'à 0,95. Le bloc O4 n'a pas été recalculé pour le partage 0,005 et 0,005 : le compte et les rangs qu'il donnerait ne sont pas dits ici.

## 3. « Horizon au plus m » et la procédure à nul placé à la borne haute (réserve 3, mineure)

**Lire, au § 6, « Deux procédures valides, et leur prix, m compris », (a), et au § 7.3, `garantie_dite`**, la lecture retenue :

> avec un nul placé à la borne haute, la validité ne dépend pas de n ≤ m ; la limite de N-076 borne alors ce qu'on conclut de la puissance, non la fausse alarme

**Cette lecture de N-076 (§ 2) est de moi : à faire confirmer par la mère.** Le repère de 1 016 verdicts emploie une médiane de 516 audits pour m = 500, donc un horizon au-delà de m. Si la lecture n'est pas confirmée, le repère se remplace par m = 1 000 : 1 334 verdicts, médiane de 334 audits [calcul, N5] ; le pari apparié reste alors le moins cher, d'un facteur de l'ordre de 2,0 au lieu de 1,6 pour le saboteur à 20 % ; le repère du saboteur à 15 % (m = 2 000, médiane de 1 601 audits) ne change pas.

**Ajouter, au même endroit, après chaque coût tiré du bloc N5** : « issue typique, k = 0,1 m ». Le coût est celui d'une référence qui observe exactement un dixième de dommages ; une référence moins heureuse place le nul plus haut et coûte davantage.

## Ce que cet erratum ne change pas

Les quatorze autres constats, les blocs N à P, que le contre-lecteur trouve exacts, le couple `collisionneur-v2/`, et les décisions du § 8.
