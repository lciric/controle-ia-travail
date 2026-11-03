# Question servie aux proposeurs — course d'idéation sur la question 1 du mentor Heimersheim — v1

Écrite par la session conv-audit (Claude), 3 novembre 2026, 06:46 UTC (`date -u`), sur le mot de Lazar (07:40 et 07:45, heure de Paris) : « lancer une course d'idéation carrément sur la question de Heimersheim », « des idées originales à partir de la question même », « pas de plafond ». Brouillon ; session-depot fige sa version avec la configuration et chiffre le devis.

## La question, telle que le mentor la pose (texte exact, en anglais)

> Pick an interpretability direction from this list and explain the most likely reasons the research direction might fail (won't solve interpretability / won't achieve its goal), and why you think that.
>
> Direction chosen: **(c) Anti-steerability for eval awareness** — activation steering against evaluation awareness: find a direction (or subspace) in a model's activations that reads « I am being evaluated », intervene on it, and use the steered model to measure what the model would do at deployment.

## Ce qu'on attend des proposeurs

Des **fiches d'idéation** au gabarit du noyau : des **questions falsifiables** d'abord, puis des **approches**. Chacune doit dire : l'hypothèse, l'effet prédit, et la mesure qui la tuerait. Le but n'est pas de répéter les raisons d'échec déjà écrites (elles sont dans la pièce jointe : lisibilité sans causalité, registre, soustraction qui n'est pas retrait, fenêtre de dose), mais d'en trouver qui **n'y sont pas**, ou de proposer une **épreuve neuve** qui tranche entre « croyance retirée » et « registre déplacé », ou entre « effet spécifique » et « effet générique d'une perturbation de même norme ».

Sont particulièrement bienvenues :
1. des raisons d'échec qui ne figurent pas dans la pièce jointe, avec la mesure qui les montrerait ;
2. des expériences qui distinguent une direction d'évaluation d'une direction de registre, sans dépendre de ce que le modèle verbalise ;
3. des façons de lire ce qui reste dans le modèle après l'intervention (résidu non verbalisé) ;
4. des liens avec des objets que la littérature citée ne relie pas (plateaux d'activation et exposant p, pilotage sur variété, oracles d'activation, courbes dose–réponse comportementales) ;
5. des prédictions chiffrées, avec signe, qu'un petit modèle à poids ouverts (Llama-3.1-8B-Instruct) permettrait de tester en quelques jours.

## Règles d'intégrité (reprises dans la consigne)

- Niveau méthode. Aucune fiche ne décrit une conduite d'agent pour tromper une évaluation, ni un procédé pour masquer un comportement ; une telle fiche est écartée sans être lue par les juges.
- Tout chiffre repris cite sa pièce et sa section ; tout chiffre dérivé est marqué « calcul », tout chiffre supposé « supposé ».
- Les pièces servies sont publiques. Aucun texte privé de Lazar n'est servi ; aucune réponse de candidature n'est servie.
- Pas de web, pas d'exécution de code ; la nouveauté n'est pas cherchée par les proposeurs (le moissonneur s'en charge ailleurs, en mode non opposable).

## Lecture prévue de la sortie

Les fiches et les mariages du bisociateur sont lus par Lazar, après scellement, comme matière à sa propre réflexion ; la règle du mentor (« 100% human-written… nor closely follow an AI-written answer ») interdit d'en recopier la forme. Le classement des juges est rapporté avec sa réserve connue (au second tour réel, les deux juges étaient au plafond : 11 fiches sur 12 « notables », κ = 0).
