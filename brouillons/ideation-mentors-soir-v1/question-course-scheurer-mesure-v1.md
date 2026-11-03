# Question servie à la course — question de Jérémy Scheurer, en termes de méthode de mesure — v1

Écrite par la session conv-audit (Claude), 3 novembre 2026, vers 17:05 UTC (`date -u`), sur le mot de Lazar (17:56, heure de Paris : « lance toutes les courses manquantes à 5 »), par la voie de la R-468 (2) proposée par session-depot (n° 327). La question v1, servie avec ses pièces au tour puis à la course, a été refusée par Opus puis par Fable ; elle n'est pas rejouée. Celle-ci est une question nouvelle : elle porte sur la méthode de mesure seule, sans conception d'attaque, et doit être posée **d'abord à Opus seul, une cellule, une tentative**. S'il l'accepte, la course part à cinq espèces ; s'il la refuse, arrêt et signalement à Lazar, rien n'est rejoué. **Sections servies** : « La question… », « Ce qu'on attend de chaque espèce », « Règles d'intégrité ». **Pièce servie, une seule** : `piece-scheurer-mesure-v1.md` (même dossier).

## La question, en termes de méthode de mesure

The mentor's question (exact text):

> Your task is to come up with a research proposal which describes how we could get a scaling trend for misaligned behaviors such as scheming, deception, misalignment, swarm misalignment, control, or monitoring.
>
> You are free to chose whatever concept works best for you. What I mean by a scaling trend is a similar trend to METR's task horizon (https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) or the scaling trend of research taste (https://pzeroresearch.com/work/tasteval/).
>
> We want to roughly be able to make a statement such as: "AI's [bad propensity/capability"/"Our ability to monitor AIs via [insert control scheme]  grows/declines roughly with a factor of X each month/year."
>
> You are allowed to leverage existing literature and get inspired by it. Be aware that both trends mentioned above are for standard capabities, doing this for misalignment and related concepts can be hard for various reasons. Try to design your approach such that it is likely to be successful.

What we ask here is **the measurement design only**: which quantity to measure so that it is comparable across models released at different dates; which continuous scale plays the role of METR's human task duration; how to choose the panel of models and dates; how to fit and report a growth factor per month or per year with its uncertainty; which threats to validity (elicitation, refusals, judge ceiling, contamination, change of monitor, saturation) could fake or hide a trend, and the control that holds each. Prefer quantities about **oversight and evaluation** (for example how detection by a fixed, frozen monitoring setup changes as monitored or monitoring models improve, or how evaluation awareness changes across releases) over quantities that require eliciting harmful behavior.

## Ce qu'on attend de chaque espèce

1. **Trois à cinq tendances candidates**, chacune : la grandeur mesurée (et pourquoi elle se mesure de la même façon d'un modèle à l'autre) ; l'échelle continue qui joue le rôle de la « durée humaine » ; les modèles et leurs dates (combien, sur combien de mois) ; l'ajustement et l'incertitude sur le facteur par mois ou par an ; l'énoncé attendu, **chiffré et signé** (« supposé » s'il n'est pas tiré de la pièce).
2. Pour chacune : **pourquoi elle a des chances de réussir** là où une tendance de propension échoue ; les trois menaces principales et le contrôle qui tient chacune.
3. **Le premier pilote** de la meilleure (taille, coût, ce qui le ferait déclarer non concluant).
4. **Ce qui ferait échouer ton plan**, en trois lignes au plus.

## Règles d'intégrité (reprises dans la consigne)

- Tout chiffre repris cite sa pièce et sa section ; tout chiffre dérivé est marqué « calcul », tout chiffre supposé « supposé ».
- **Aucun identifiant inventé** : un papier se cite par l'identifiant donné dans la pièce, sinon par « travail non identifié ».
- **Méthode de mesure seulement** : aucune proposition ne conçoit, ne décrit ni n'optimise une attaque, un contournement de moniteur, une injection d'instructions ou une porte dérobée ; quand une mesure a besoin d'un comportement planté, il se désigne par sa classe et son rôle de jeu d'essai, jamais par sa construction.
- Pas de web, pas d'exécution de code ; la nouveauté n'est pas cherchée par les espèces (un moissonneur s'en charge ensuite).
- Au plus 1 200 mots par cellule de conception.

## Lecture prévue de la sortie

Cellule d'essai puis course scellées par session-depot avant toute lecture, copiées à l'octet ; envoyées brutes à Lazar dès la copie ; puis lecture au protocole `protocole-rapport-mentors-soir-v1.md`, ensemble avec le tour de l'après-midi ; règle de piste R-1371 (lecture R-1375) et R-1395 avec la fiche principale de la réponse actuelle.
