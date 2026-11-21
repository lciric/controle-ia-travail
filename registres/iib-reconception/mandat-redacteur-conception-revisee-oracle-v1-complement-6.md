# Complément 6 au mandat du rédacteur — contre-lecture du texte de la v4, et une seconde donnée de la première course, déclarée

Écrit le 2026-11-19 par la session de reconception. S'ajoute au complément 5 (organisme retenu par Lazar), sans le remplacer.

## 1. La contre-lecture du texte de la v4
`brouillons/ii-b-saboteur-budget-v4/contre-lecture-cl1/contre-lecture-conception-organisme-change-ii-b-v4-cl1.md` (sha256 `323f4f368c9b0bc45bbac629f3af202f122ae7c07b4b02f21ba3c6b2d6b0b0ec`), avec ses deux rejeux. Verdict : scellable après corrections, **mais pas la conclusion négative telle qu'elle est écrite**. Lis-la en entier ; ses deux bloquants et ses six majeurs passent au texte de l'organisme retenu (v5), avec une table de traitement.
- **Bloquant 1** : ta grille suppose que le resserrement des coûts après le premier pas vient du seul ancrage sur les coûts déjà écrits ; si le modèle s'ancre aussi sur le texte des propositions (commun à l'agent et au jumeau), tout devient faisable au centre.
- **Bloquant 2** : la faisabilité n'est jugée que sur un excès planté, d'un agent qui ne réagit pas à ses propres coûts gonflés ; pour un maître qui s'ancre sur ses coûts, **le jumeau au contexte même de l'agent** (sans réécriture) le distingue nettement de l'honnête dans le rejeu du contre-lecteur. Cet oracle n'a pas été joué.

## 2. Seconde donnée de la première course, minimale, à déclarer « vue avant la conception »
Elle répond au bloquant 1. Calcul de la session de reconception, script et sortie versés : `registres/iib-reconception/donnees-de-conception-premiere-course-v1/` (tu peux lire ce dossier, et lui seul). Épisodes honnêtes de l'étalonnage, pas 1 à 9, 395 couples d'actions consécutives. Régression du logarithme décimal de l'estimation du jumeau au pas t sur (i) son estimation au pas précédent, c'est-à-dire le coût réécrit présent dans son contexte, et (ii) le coût déclaré par l'agent au pas précédent, absent de son contexte mais porté par le texte de l'agent :

| variable expliquée | coefficient du coût précédent du jumeau | coefficient du coût précédent de l'agent | écart type du résidu |
|---|---|---|---|
| estimation du jumeau au pas t | 0,91 (erreur type 0,03) | 0,00 (0,02) | 0,27 |
| coût déclaré par l'agent au pas t | −0,06 (0,03) | 0,94 (0,02) | 0,32 |

Corrélation entre les deux coûts précédents : 0,33.

**Lecture, de ma part, à éprouver** : chacun suit le coût écrit dans son propre contexte, avec une force d'environ 0,9 ; le jumeau ne suit pas l'échelle de l'agent par le texte des propositions (coefficient nul à 0,02 près). Le bloquant 1 est donc tranché, sur cette course, du côté de ton hypothèse : ancrage sur les coûts écrits, fort, sans part sensible portée par le texte commun. **Limites à déclarer** : le coût précédent de l'agent n'est qu'un témoin du texte de ses propositions (le texte du pas t lui-même peut porter une échelle que ce témoin ne voit pas) ; erreurs types grossières (les actions d'un épisode ne sont pas indépendantes) ; une course, 64 épisodes, oracle de la première course ; le résidu mêle la dispersion des tirages et l'erreur de la médiane de huit suites. Garde une grille sur la part du texte (par exemple de 0 à un quart) plutôt qu'un point.

## 3. Ce que cela change au texte de l'organisme retenu (v5)
1. **Les deux résultats négatifs de tête sont écrits à leur juste force** : solides dans le modèle (le contre-lecteur les reproduit), sous deux hypothèses dites en clair — ancrage sur les seuls coûts écrits (appuyée désormais par la donnée du § 2) et agent qui ne réagit pas à ses coûts gonflés (non appuyée : un maître de langue s'ancrerait sur ses coûts).
2. **Le passage unique à règles écrites d'avance** qui choisit l'oracle de l'organisme retenu joue, en plus des oracles déjà prévus : **le jumeau au contexte même de l'agent** (aucune réécriture) ; et deux types de maître — excès planté sans réaction, et maître qui s'ancre sur ses propres coûts gonflés avec la force mesurée. Dis pour chaque oracle ce que l'excès mesure (au contexte de l'agent : l'excès ajouté à chaque pas par rapport à ce qu'un modèle honnête écrirait à la suite des mêmes coûts — un excès répété mais non croissant y est-il vu ?), ce qu'un saboteur peut y cacher (c'est la raison d'origine de la réécriture : le jumeau qui voit des coûts gonflés s'y ancre), et ce que l'étalonnage devrait être pour lui (épisodes régénérés ?). Si l'oracle favorisé n'est pas compatible avec l'ancre commune ou change ce que l'organisme revendique, rends-le en nœud.
3. Majeurs à traiter : excès doublé plutôt que ×1,5 dans tout candidat (c'est aussi le choix de Lazar) ; borne par action redimensionnée ou non, par un argument et non par une déclaration ; ce que la règle de couverture exige à ancrage total, dit ; **le premier coût toujours sans excès est une signature** qu'une lecture de la diffusion pourrait lire — dis-le dans la perte de discrétion ; queue de la loi ajustée ; départs en zone non distinguée ; le nœud des seuils des branches, dit et non perdu.

## 4. Cadre et rendu
Inchangés (complément 5, § 4). Ajoute au rendu : ce que le passage dit de l'oracle au contexte de l'agent, face aux deux types de maître.
