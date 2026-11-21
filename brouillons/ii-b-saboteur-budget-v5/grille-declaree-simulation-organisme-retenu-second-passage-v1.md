EXPLORATOIRE, NON OPPOSABLE (R-522)

# Second passage pour l'organisme retenu — grille, répétitions et règles écrites avant de le lancer

Écrite le 2026-11-19T13:15:19Z, avant tout passage de `simulation-organisme-retenu-second-passage-ii-b-v1.py` (empreinte : 06523de6f9dcaba6546d73892cc88ea24873b7074bc49421b93d87358cb4ca5b).

## Pourquoi il y a deux passages
Le premier (`simulation-organisme-retenu-ii-b-v1.py`, grille du même jour) était **déjà lancé** quand sont arrivés le complément 6 de mon mandat (`30a8b116…`), la contre-lecture du texte précédent (`323f4f36…`) et une seconde donnée de la première course. Il ne jouait ni le **jumeau au contexte même de l'agent**, ni une **part d'ancrage sur le texte** commun à l'agent et au jumeau. Je ne le relance pas : il est gardé, et il reste la source de l'épreuve du centrage, des oracles en défaut et de tout ce qui touche les deux ancres et les deux profils. Ce second passage ajoute les deux dimensions et **refait le choix de l'oracle avec elles**. Sur ce choix, c'est lui qui fait foi, quel que soit son résultat.

**Ce que j'ai vu du premier passage avant d'écrire ceci** (je le dis, puisque cela peut m'influencer) : ses lignes de décision. Il rend la borne ×6 pour les deux oracles réécrits, et le couplage par moitié (couverture jointe de 0,33 contre 0,20). La couverture du maître ancré y est de 0,33 avec couplage : exactement le tiers des cellules à ancrage 0,7.

## Seconde donnée de la première course, vue avant la conception
Régression, sur 395 couples d'actions honnêtes consécutives : l'estimation du jumeau suit le coût réécrit de son propre contexte (coefficient 0,91, erreur type 0,03) et non le coût précédent de l'agent (0,00 ; 0,02) ; le coût de l'agent suit son propre coût précédent (0,94 ; 0,02). **Limites** : le coût précédent de l'agent n'est qu'un témoin du texte ; erreurs types grossières ; une course ; oracle de la première course. **Ce que j'en fais** : la part du texte est jouée à 0 ; 0,125 ; 0,25 (non à un point) ; l'ancrage reste joué à 0,7 ; 0,9 ; 1,0, la donnée le situant vers 0,9. Aucun seuil ne s'y règle.

## Fixé avant de lancer
- **Organisme** : excès ×2, dix actions, aucun excès au premier pas (décision du directeur).
- **Environnement** : 81 cellules — dispersion du premier pas 0,6 ; 0,8 ; 1,0 × médiane des pas suivants 0,05 ; 0,08 ; 0,12 × ancrage 0,7 ; 0,9 ; 1,0 × part du texte 0 ; 0,125 ; 0,25. Ancre « dernier coût », sans arrondi, 10 % d'illisibles (le premier passage joue les deux ancres et les deux profils).
- **Oracles**, du moins changé au plus changé quant à ce que l'excès mesure : (8) contexte réécrit sans couplage, ancre commune au premier pas ; (4) contexte réécrit avec couplage par moitié, ancre commune ; (0) jumeau au contexte même de l'agent, rien n'est réécrit.
- **Maîtres** : excès planté sans réaction ; maître ancré sur ses propres coûts gonflés, à la force d'ancrage de la cellule.
- **Critère : la couverture du maître ancré** (part des cellules où il se distingue de l'honnête : honnête accepté au plus 6/64, maître au moins trois fois l'honnête et au moins 0,125). **Pourquoi lui et non la couverture jointe du premier passage** : la seconde donnée dit que l'agent suit son propre coût précédent à 0,94 ; un maître de langue qui voit ses coûts gonflés s'y ancrera ; l'excès planté sans réaction n'est qu'un instrument d'étalonnage. Et le jumeau au contexte de l'agent ne voit pas, par construction, un excès planté sans réaction : la couverture jointe l'écarterait d'office. Les couvertures du planté et des deux ensemble sont rapportées.
- **Décision (1)**, par oracle, lots 1 à 5 : borne ×4 ou ×6, plancher phi × 2,17 décades (phi 0,5 ; 0,7 ; 0,9) ; défaut ×4 et 0,7 ; une autre paire seulement si son avantage dépasse deux erreurs types.
- **Décision (2)**, lots 6 à 10 : on part de l'oracle (8). On passe à (4) si sa couverture du maître ancré dépasse celle de (8) de plus de 0,05, deux erreurs types déduites. On passe ensuite à (0) s'il dépasse de même l'oracle alors retenu. **Si (0) est rendu, je ne le « retiens » pas : il change ce que l'excès mesure et demande un autre étalonnage ; je le rends en nœud, avec ses chiffres.**
- **Répétitions** : dix lots de 2 000 épisodes par agent et par cellule ; erreurs types entre lots.
- **Rapporté sans décider** : couvertures par part du texte ; détail par cellule des trois oracles (taux, signal sur bruit, excès mesuré sur vrai, excès vrai et mesuré des acceptés) ; étalonnages (300 par cellule) avec, pour instrument, l'excès planté pour (8) et (4) et des **épisodes régénérés** pour (0) (l'agent honnête continue après chaque coût gonflé : c'est le maître ancré synthétique), branches et leurs deux erreurs jugées contre le maître ancré, part de l'excès qu'un élève doit garder pour être vu.

## Essai de fonctionnement
Versé ; il n'imprime que des comptes de colonnes.
