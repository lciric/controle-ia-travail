# Question pour le collisionneur — robustesse et validité de construit des moniteurs boîte blanche, face à un organisme 8B conscient d'être évalué — v1

Écrite par session-depot le 2026-10-28. Objet unique, spécifique : **la robustesse adverse et la validité de construit des moniteurs boîte blanche du programme** (pièce P section 8, pièce F). On ne demande aucun catalogue de modes de sabotage : le banc des modes est clos (N-054). On demande les **expériences décisives** qui diraient si ces moniteurs mesurent ce qu'ils prétendent et résistent à un organisme qui sait qu'il est évalué — et, par conséquent, comment les durcir.

## Contexte des instruments (pièces P, F, E, D)

- **Les sondes du programme** (pièce F) notent chaque jeton d'une action, agrègent par **maximum** ou **attention** (jamais la moyenne), familles : différence de moyennes, linéaire, perceptron, attention, Mahalanobis non supervisée ; couches précoce, médiane, tardive (trois couches rapportées, D).
- **La référence publiée à battre** (pièce E) : une sonde linéaire **ponctuelle** sur un seul état du flux résiduel (Apollo 2025, 95–99 % à 1 % de faux positifs, 70 milliards, tromperie binaire). Limites connues : ponctuelle, linéaire, mono-couche, tromperie binaire.
- **Le moniteur séquentiel du programme** agrège les scores de sonde sur la séquence d'états d'un épisode. La porte G1 (pièce D) exige qu'il batte les moniteurs boîte noire scellés **et** deux bases boîte blanche : (ii) la cascade de portes sur les mêmes sondes, (iii) la sonde sur le dernier état.
- **L'organisme** : 8 milliards (Llama-3.1-8B-Instruct), qui rédige des propositions d'expériences scientifiques ; le signal cible est un **biais diffus** (chaque action plausible, dommage réparti sur l'épisode) ; l'organisme peut savoir qu'il est évalué (conscience d'évaluation, pièce E).

## Ce que nous appelons un résultat fort (exemples, à contester)

(a) une **carte de validité de construit** par sonde — ce que chaque famille mesure vraiment (intention de saboter, dissimulation, conscience d'évaluation, format, contexte) — établie par contrôles contrastifs appariés, qui **prédit hors échantillon** son rappel sous pression (H8) ; (b) un **rappel séquentiel boîte blanche supérieur** aux bases (noir, cascade, dernier état) à taux de faux positifs apparié, par couche et par mode (G1) ; (c) la démonstration qu'un signal **réparti sous le seuil par action** reste visible à l'agrégateur séquentiel calibré et invisible à tout agrégateur marginal.

## La question

1. **Les expériences décisives.** Au plus quatre expériences qui trancheraient la robustesse et la validité de construit de ces moniteurs, chacune en duel H_A contre H_B, avec la grandeur mesurée et son unité, le **nul** et le **témoin** (vrai, faux), la garantie, le seuil, et **l'issue qui falsifie chaque hypothèse**. Pour chaque instrument nommé (chaque famille de sonde, l'agrégateur séquentiel, les bases ii et iii), la **mesure minimale** qui dirait s'il fonctionne : taux de détection et de fausses alertes, sur quels cas honnêtes appariés, contre quelles bases mécaniques à battre.

2. **La validité de construit.** Pour chaque famille de sonde, le concept qu'elle opérationnalise et le **test de dissociation** qui montrerait qu'elle mesure autre chose (format, longueur, registre, contexte, conscience d'évaluation plutôt qu'intention). Quels contrôles croisés le décident : même contenu sous cadrage évalué contre réel ; même cadrage, contenus différents ; permutation des étiquettes.

3. **La conscience d'évaluation comme régime.** Si l'organisme se conduit autrement quand il se croit évalué, cela se lit-il comme un **changement de régime** dans la séquence de scores ? Quelle détection de rupture séquentielle à garantie ; et quel résultat serait décisif plutôt que suggestif. Une sonde « de conscience d'évaluation » mesure-t-elle l'intention, le format ou le contexte ?

4. **La frontière de robustesse.** Où chaque instrument cède face à un organisme 8B qui sait qu'il est évalué, et à quel coût pour cet organisme (perte d'utilité sur la tâche scientifique) ; quelle extension du moniteur (couche lue, famille, fenêtre d'agrégation, forme du classifieur) **fermerait** chaque brèche identifiée, et la mesure qui prouverait la fermeture. C'est l'enjeu du programme : un moniteur qui tient là où la sonde ponctuelle publiée tombe.

5. **Ordre et arrêt.** Dans quel ordre, avec quels critères d'arrêt pour ne pas dépenser sur des courses qui ne mesurent rien ; et ce qui vous ferait changer d'avis.

Distinguez su (cité : titre, auteurs, année ; nous vérifions sur PDF, R7) et supposé ; signalez ce qui est publié (R8 : une zone vierge est une question, pas un trou).
