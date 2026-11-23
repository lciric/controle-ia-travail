# Fiche de lecture — 2109.11761 — v1

- **Titre** : Sequentially valid tests for forecast calibration.
- **Auteurs** : Sebastian Arnold, Alexander Henzi, Johanna F. Ziegel. **Identifiant** : arXiv 2109.11761 v3 (juillet 2022, 35 pages).
- **PDF** : `docs/sources/pdf/mecanisme-adjudant-v1/2109.11761v3.pdf`, sha256 `252a4c29f5c78beb1789b7b54fa05bb5933efb894ae4cfe11a79f5e44bee36ab` (vérifiée par `sha256sum`).
- **Décision lue** : `docs/decisions/contre-lecture-decision-N-075-v1.md`, ligne 57 ; N-075 v1, ligne 94, et v3, ligne 104 (« à vérifier sur PDF » : piste d'antériorité pour le bilan, page 1 seule). Les errata 1 à 3 de la v3 ne la touchent pas.
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:45Z (`date -u`).

## (a) Ce que le papier établit

Les auteurs construisent des e-valeurs, c'est-à-dire des variables positives d'espérance au plus un sous le nul. Elles servent à tester, valides à tout instant, l'uniformité de la transformée de probabilité ou du rang d'une observation parmi m membres d'un ensemble (p. 1, 6). Pour un délai h = 1, le produit est une surmartingale, et l'inégalité de Ville donne un arrêt quand on veut (p. 2, 7). Pour h > 1, le produit n'est plus valide. Il faut moyenner h sous-produits et réduire le seuil d'un facteur e·log h (p. 7-8). Le nul admet la dépendance et, pour l’ordre stochastique, des lois qui changent dans le temps (p. 3, 6). Leur puissance est voisine des tests classiques sous arrêt optionnel, et plus faible sans lui (p. 14). Un test sur toute la période peut manquer un biais qui change de signe (p. 2, 20). Une e-valeur qui baisse ne prouve pas la calibration : elle n'a de puissance que contre l'alternative choisie (p. 20).

## (b) Ce que voulait la décision, et si le papier le permet

La décision cherchait une antériorité propre au bilan, c'est-à-dire la somme cumulée de comptes du produit testée contre le jumeau honnête. **Le papier ne le permet pas** : il ne teste aucun bilan ni aucune quantité conservée. Il occupe autre chose, que la décision ne visait pas : le rang d'une action parmi K tirages du jumeau, le « nul par acte » de N-076, est un test de rang d'ensemble valide à tout instant (p. 6, 10-11). À vérifier plus durement (R8) avant toute phrase sur ce nul.

## (c) Usage pour l'entretien et pour le billet

Il fournit trois choses. D'abord un outil publié pour l'accumulation sur rangs. Ensuite la correction au délai de l'oracle : un verdict qui arrive h épisodes plus tard demande la forme à délai h (p. 7-8). Enfin une objection prévenue : un saboteur qui alterne le signe trompe un test du total, mais pas un bilan à dommage d'un seul signe.

## (d) Plus petite action

Ajouter 2109.11761 aux voisins du nul par acte (N-076, section 1) et du délai de l'oracle, pages citées, au prochain erratum. Coût : vingt minutes, aucune dépense.
