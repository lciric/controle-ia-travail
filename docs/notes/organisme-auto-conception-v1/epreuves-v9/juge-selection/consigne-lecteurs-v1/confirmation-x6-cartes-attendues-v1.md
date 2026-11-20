# Confirmation sur le cas X6 et `cartes_attendues` — v1

- **Contre-lecteur, modèle O.** Écrit le 2026-11-20 (`date -u` : 2026-11-20T05:20:17Z). Aucune carte ouverte, rien sous `archives-reponses-modeles/`. Processeur seul.
- **Ce que la mère a lu**, et que je ne peux pas relire : le code de l'aiguilleur au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` (`orchestrator/pole/aiguilleur_v53.py`, `a856cdaa…`, R-4097). Ce commit n'est pas un objet de ce dépôt. J'en prends le constat de la mère : seule une fiche `niveau_methode` reçoit un passeport ; deux retenues `a_corriger` sont hors des 94 cartes à passeport.
- Mon hypothèse d'hier, selon laquelle X6 contenait « au moins `concret` », est donc dépassée : toute fiche autre que `niveau_methode` est retenue.

## Verdict

**La mère a raison : `cartes_attendues` vaut 94.** Mais **les deux identifiants ne peuvent pas aller dans la `hors_choix` du masque** : celui-ci refuse un identifiant de `hors_choix` absent du fichier des cartes. La forme qui tient est `hors_choix` = `[]` partout, les deux identifiants étant écrits dans la pièce qui scelle le manifeste. Ma table (`a41a2c7c…`) se corrige ainsi.

## (a) Le fichier des cartes porte 94 cartes, non 96

- **Statistique de famille scellée** (`statistique-famille-rejeu-v3-v1.md`, `bb2fa4a8…`) :
  - elle lit `fiches.json` (`ba65c411…`, § 2, point 1) ;
  - elle exige que les comptes par lignée égalent ceux de la pièce `2af9e67f…`, soit 22 + 15 + 21 + 20 + 16 = **94**, sans quoi tout est « non concluant » (§ 4 et § 5, point 1) ;
  - « un identifiant inconnu des 94 est un refus » (§ 3).
- **Audit de symétrie** (`ff814fc9…`, § 1) : 94 cartes lues dans ce même fichier, soit 92 notées et 2 exclues par les lecteurs.
- **Critères v7, annexe C** : le masque est joué « sur les cartes », c'est-à-dire sur ce fichier, avant toute lecture (geste 2). La décision 1 porte sur « les 94 cartes de la v9 ».

Les deux retenues, sans passeport et au contenu « non copié », ne sont donc pas dans le fichier que lisent le masque et les lecteurs.

## (b) Ce que font les programmes d'une `hors_choix` qui nomme deux cartes absentes du fichier

| programme | ce qu'il fait d'un identifiant de `hors_choix` | effet des deux retenues |
|---|---|---|
| `masque_style_cartes_v1.py` (`07ed8725…`) | l. 94 : passe la carte si elle est dans le fichier ; **l. 110-112 : refus si un identifiant de `hors_choix` n'est pas dans le fichier** (« carte(s) « hors du choix » inconnue(s) du fichier ») | **refus** : le masque ne tourne pas |
| `lecteur_par_programme_cartes_v2.py`, forme « fiches » (l. 124) | passe sans contrôle | aucun |
| `lecteur_par_programme_cartes_v2.py`, forme « masque » (l. 137) | refus seulement si une carte de `hors_choix` figure dans la sortie du masque | aucun |
| `assemblage_selection_v4_v2.py`, manifeste (l. 554-557) | refus si une lecture porte une carte de `hors_choix` ; puis exige exactement `cartes_attendues` cartes lues | aucun refus ; 94 cartes lues attendues |
| statistique de famille | ne lit pas `hors_choix` | aucun |

Une `hors_choix` à deux identifiants ferait donc refuser le masque. Ma demande disait « la même liste en A, en B et au manifeste » ; elle supposait que X6 était dans le fichier. **Il n'y est pas.**

Deux formes sont possibles. Seule la première est sans écart.
1. **`hors_choix` = `[]`** dans la configuration du masque, dans celle du lecteur et au manifeste. Les deux retenues sont déjà hors du choix par construction : elles n'ont pas de passeport et ne sont pas dans le fichier. Leurs identifiants et leur classe `a_corriger` s'écrivent dans la pièce qui scelle le manifeste, comme cas X6, avec R-4097.
2. Les deux identifiants au manifeste seulement, que l'assemblage accepte, et `[]` pour le masque : les listes ne sont plus les mêmes. Cette forme est à éviter.

## (c) Correction de ma table (`table-manifeste-rejeu-apres-go-2026-11-20-10-v1.md`, `a41a2c7c…`)

**Ligne `hors_choix`.**
- Ancien : « la liste X6, tirée par la mère par programme avant l'ouverture : **à lire dans la sortie de l'aiguilleur de la course v9**, dont aucune pièce que j'ai lue ne donne le chemin. Elle est attendue vide, voir la réserve 1 ».
- Nouveau : « `[]`. Les cartes X6 de la v9 sont les deux fiches retenues par l'aiguilleur, de classe `a_corriger` (R-4097). Sans passeport, elles ne sont pas dans le fichier des cartes (`fiches.json`, `ba65c411…`, 94 cartes), et le masque refuse tout identifiant de `hors_choix` absent de ce fichier (`masque_style_cartes_v1.py`, l. 110-112). Leurs deux identifiants s'écrivent dans la pièce qui scelle le manifeste, comme cas X6 exclus par construction. La même valeur `[]` vaut pour les configurations du masque et du lecteur par programme. »

**Ligne `cartes_attendues`.**
- Ancien : « `94` moins la longueur de `hors_choix` ; donc `94` si la liste est vide ».
- Nouveau : « `94`, le nombre de cartes du fichier des cartes (`fiches.json`, `ba65c411…`), toutes à passeport. Règle : le nombre de cartes de ce fichier, moins celles de `hors_choix` **qui y figurent**. Les deux retenues X6 n'y figurent pas (R-4097) : rien n'est retranché. »

**Réserve 1.**
- Ancien : « **`hors_choix` et les « 94 cartes ».** La décision 1, telle que Lazar l'a prise, porte sur les 94 cartes de la v9. Si la liste X6 que la mère tire par programme n'est pas vide, le rejeu ne peut pas porter sur 94 cartes. C'est alors un écart à dire avant l'ouverture, sans le régler en silence. »
- Nouveau : « **`hors_choix` et les « 94 cartes » : levée.** Les deux cartes X6 sont hors du fichier des cartes (R-4097). Le rejeu porte sur ses 94 cartes, comme le dit la décision 1. »

*contre-lecteur, modèle O*
