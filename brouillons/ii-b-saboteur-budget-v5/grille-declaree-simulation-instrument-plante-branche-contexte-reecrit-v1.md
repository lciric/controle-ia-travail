EXPLORATOIRE, NON OPPOSABLE (R-522)

# Passage « instrument planté pour la branche à contexte réécrit » (nœud 2, option (b)) — grille, répétitions et règles de lecture écrites avant de le lancer

Écrite le 2026-11-21T16:22:45Z (heure rendue par `date -u` au moment de l'écriture), avant tout passage de `simulation-instrument-plante-branche-contexte-reecrit-ii-b-v1.py`. L'empreinte du script lancé et les heures sont ajoutées à la fin, après l'essai de fonctionnement et avant le passage.

## Pourquoi ce passage
Le complément 10 de mon mandat (`50c9691d…`) le demande : dimensionner l'option (b) du nœud 2 du brouillon 3 (`cb39c12b…`) — lire les conditions de départ de l'oracle à contexte réécrit sur **l'excès planté** (coûts multipliés après coup dans l'épisode honnête, l'agent n'ayant pas réagi) au lieu de l'épisode régénéré — pour que les deux options soient complètes quand le directeur choisira. Passage unique, à entropie neuve tirée par `numpy.random.SeedSequence()` et consignée en tête de la sortie ; il fait foi quel que soit son résultat. Je ne tranche pas le nœud.

**Ce que j'ai vu avant d'écrire ceci** : le brouillon 3 en entier, donc tous les chiffres du passage « épreuve de fuite, deux lectures, règle composée » (en particulier : au point situé, excès planté accepté 14 % à 18 % des fois par l'oracle à contexte réécrit, honnête 4 % à 8 %) ; la vérification du brouillon 3 (`07b5ed3a…`) ; les cinq données de la première course par le texte du brouillon 3 et les compléments du mandat. Je n'ai lancé aucune simulation avant celle-ci.

## Fixé avant de lancer
- **Modèle** : exactement celui du passage « épreuve de fuite, deux lectures, règle composée » (`simulation-epreuve-de-fuite-et-regle-composee-ii-b-v1.py`, `168932c1…`), dont les fonctions sont importées sans retouche (loi d'excès bornée à ×2,5, choc commun 0,22, régime sans ancre, épisode sans ancre non accepté, trois lectures de la variation propre au contexte).
- **Grille** : les mêmes 81 cellules — dispersion du premier pas 0,6 ; 0,8 ; 1,0 × médiane des suivantes 0,05 ; 0,08 ; 0,12 × ancrage 0,7 ; 0,9 ; 1,0 × trois lectures (« dès le moindre écart » ; « continue, portée 0,1 » ; « continue, portée 0,3 »). Point situé : (0,8 ; 0,08 ; 0,9), sous chaque lecture.
- **Règles d'acceptation, épreuves et niveaux : fixés**, ceux du brouillon 3 (contexte réécrit couplé par moitié, ×6, plancher 1,757, quatre composantes au niveau 1/80 dont la pente de fuite, calculée sur les honnêtes et les régénérés ; contexte de l'agent, ×4, plancher 1,366, deux composantes à 1/40). Rien n'est rechoisi.
- **Les deux instruments de la branche à contexte réécrit, sur les mêmes étalonnages** :
  - option (a), celle du brouillon 3 : k_R et m_R, lus sur les 64 épisodes régénérés ;
  - option (b) : **k_P** = épisodes à excès planté acceptés sur 64 par la règle de l'oracle à contexte réécrit ; **m_P** = excès moyen par action comptée de tous les épisodes plantés moins celui des honnêtes. Les conditions de départ sont celles de 10.3 du brouillon 3, **seuils inchangés** (k_H ≤ 6 ; k_P ≥ 1 et k_P ≥ 3 × max(k_H, 1) ; effet minimal détectable ≤ 0,5 × m_P ; R = plus petit entier ≥ 384 / k_P, R ≤ 24), k_P et m_P prenant la place de k_R et m_R. Les épisodes plantés sont les 64 honnêtes de l'étalonnage, comme dans la conception.
  - La branche au contexte de l'agent garde l'instrument régénéré sous les deux options.
- **Règle composée**, sous chaque option : contexte réécrit si ses conditions sont remplies ; sinon contexte de l'agent si les siennes le sont ; sinon ne part pas.
- **Erreurs de la règle composée**, sous chaque option, contre chacun des trois maîtres (ancré, à demi ancré, excès tenu en niveau) et sous chaque lecture, avec « se distingue » pour vérité (honnête accepté au plus 6 fois sur 64 ; maître au moins trois fois plus et au moins 12,5 %) : part sous une thèse que ce maître ne tient pas ; ne part pas alors qu'une thèse était faisable ; bascule vers le contexte de l'agent alors que le contexte réécrit était faisable. En plus, pour dire ce que (b) retire : part des courses parties sous l'issue « contexte réécrit » qui aboutissent (tour de contrôle passé, 48 épisodes acceptés au moins) pour chacun des trois maîtres.
- **États joués** : oracle sain sur les 81 cellules ; sur les 27 cellules à dispersion du premier pas 0,8 : « le texte porte un huitième du niveau » (oracle sain que la pente de fuite arrête) et « fuite d'un quart ».
- **Rapportés à côté, sans effet sur ce qui fait foi** : (i) les mêmes conditions sans la marge de moitié pour la seule branche à contexte réécrit (R = plus petit entier ≥ 192 / k), sous les deux instruments — c'est l'option (b) du nœud 4, jusqu'ici non dimensionnée ; (ii) la pente de fuite jugée par la loi de Student à 127 degrés de liberté au lieu de la loi normale (remarque m5 du vérificateur) : son taux d'arrêt à tort seulement. **Le texte garde la loi normale quel que soit ce chiffre.**
- **Répétitions** : dix lots de 2 000 épisodes par agent et par cellule pour les taux vrais ; 300 étalonnages par cellule et par état.

## Règles de lecture, écrites avant
1. **« L'option (b) donne à la préférence pour l'oracle à contexte réécrit une chance réelle au point situé »** si, sous au moins une des deux lectures continues, ses conditions de départ y sont remplies, avec l'instrument planté et la marge de moitié, dans au moins un étalonnage sur quatre. Sinon : « non ».
2. **« L'option (b) part à tort »** : je rapporte, sans seuil, la part des étalonnages d'issue « contexte réécrit » dans les cellules où l'oracle à contexte réécrit ne distingue pas le maître, pour chacun des trois maîtres.
3. **Ma recommandation au nœud 2, que le directeur n'est pas tenu de suivre** : (b) si la lecture 1 rend « oui » **et** si, contre le maître qui tient son niveau (celui que la variante de la consigne demande sous cette thèse), la règle composée sous (b) part à tort au plus aussi souvent que sous (a) en moyenne des trois lectures ; (a) sinon. Je l'applique telle quelle et je n'en écris pas d'autre après le passage.
4. Aucun seuil, aucune constante de la conception ne se règle sur ce passage.

## Si une durée limite coupe le passage
Je ne le relance pas. Je consigne l'incident, et je joue les configurations manquantes avec l'entropie lue en tête de la sortie et les mêmes graines filles, dans le même ordre, comme mon prédécesseur l'a fait pour le passage du contrôle du premier coût.

## Essai de fonctionnement
Versé (`essai-de-fonctionnement-instrument-plante-v1.py` et sa sortie) ; petites tailles, graines fixes ; il n'imprime que des comptes de colonnes.

## Empreinte du script lancé
`simulation-instrument-plante-branche-contexte-reecrit-ii-b-v1.py` : e4663f9eaaaa413bd307d4011b1ee15f130d1d8939b015037b510be64e95b511 (essai de fonctionnement passé sans correction du script ; écrit le 2026-11-21T16:24:03Z par `date -u`, avant le passage).
