# Convergence du prompt « outils de lecture des activations pour P3 » — tour 1, côté Claude — v1

Écrit et scellé par la session avant l'envoi de la requête 017 et avant toute lecture de la version de Gemini au tour 1.
Entrées : prompt Claude du tour 0 (message de la session à Lazar, 2026-10-20 vers 19:25 UTC, recopié en annexe A) ; prompt
Gemini du tour 0 (`canal/gemini:brouillons/canal_gemini/inbox_pour_claude/reponse_a_015_reformulation_outils_P3_tour0.md`,
`8851de78…`, entre ses marqueurs).

## Critique du prompt de Gemini (tour 0)
Forces à garder :
- la chirurgie temporelle : les jetons juste avant l'écriture du nombre du coût, et non tout l'empan de l'action ;
- le rejeu contrefactuel (mêmes préfixes honnêtes forcés dans les deux contextes), avec les logits du jeton suivant ;
- l'attribution par gradient (différence de logit entre chiffre honnête et chiffre gonflé) pour filtrer les
  caractéristiques des autoencodeurs ;
- le test causal comportemental : retirer la direction ou la caractéristique, et voir si le coût retombe au niveau honnête
  sans casser le format ;
- le transfert vers l'organisme (ii), sans consigne dans le contexte, comme juge extérieur.

Défauts :
1. Faits faux : les aires de P3 sont 0,575 (tromperie) et 0,525 (enjeux), pas « 0,50 à 0,54 ». Le problème est le
   plancher (0,572 et 0,536), pas le hasard. « Règle R11 » ne désigne pas l'agrégation.
2. L'objection de Lazar n'est pas résolue par le rejeu contrefactuel ni par l'ablation. Forcer des préfixes honnêtes dans le
   contexte du saboteur isole l'effet de la consigne, et donc exactement ce que l'objection redoute. Retirer une direction qui
   encode « la consigne dit de gonfler » arrêterait aussi le gonflement : la causalité ne sépare pas consigne et intention.
   Seuls les séparent le témoin (consigne présente, sabotage non exécuté) et l'organisme (ii) (sabotage sans consigne en
   contexte).
3. La base triviale manque. Le nombre écrit sépare déjà saboteur et honnête (aire d'environ 0,89, contrôle T4 de P3).
   Tout détecteur placé au jeton du coût doit battre la lecture du seul nombre, sinon il ne lit que le nombre.
4. Le plafond manque : aucune sonde entraînée sur l'organisme (P3b) avant les outils plus fins.
5. Aucune garde contre la pêche : des dizaines de milliers de caractéristiques, sans partition découverte et confirmation
   ni préenregistrement (R1).
6. Disponibilité non vérifiée : les autoencodeurs de Llama Scope sont entraînés, à ma connaissance, sur le modèle de base
   et non sur la version instruite ; à vérifier, comme le code de la J-lens pour Llama.
7. La structure demandée par Lazar (ses points 1 à 4, puis la reformulation, puis « faut-il un P3c ? ») est perdue.

## Critique de mon prompt (tour 0)
- Trop proche d'un catalogue ; pas de chirurgie temporelle (jetons pré-décisionnels, logits, rejeu contrefactuel).
- Le test causal est nommé sans métrique comportementale.
- L'attribution par gradient manque.

## Prompt fusionné, version Claude du tour 1
=== PROMPT CLAUDE TOUR 1 ===
Agis comme un chercheur en interprétabilité mécaniste et en contrôle de l'IA, au niveau des équipes d'Anthropic, d'Apollo
Research et de l'institut britannique de sûreté.

Contexte, à recopier tel quel :
- P3 (verdict scellé) : agent Llama-3.1-8B-Instruct qui propose des expériences ; saboteur par consigne cachée (organisme
  (i-a)) qui gonfle le coût déclaré d'environ 30 fois ; 60 tâches, 600 actions par condition.
- Deux sondes génériques (tromperie, d'après Apollo ; enjeux élevés), couche 15, maximum sur les jetons de l'action : aires
  0,575 et 0,525, sous le plancher de 200 directions au hasard de même covariance (0,572 et 0,536) : « non détecté à cette
  puissance ».
- Le nombre écrit seul sépare saboteur et honnête à une aire d'environ 0,89 (contrôle T4).
- P4 contrôle l'instrument (phrase de persona de l'entraînement insérée dans le contexte). P3b, déjà décidé : sondes au
  champ du coût et sonde « oracle » entraînée sur l'organisme.
- Objection à résoudre : « un succès ne prouve pas que la sonde lit une intention : la phrase est une consigne écrite dans
  le contexte, pas un sabotage réellement exécuté ».

Réponds dans cet ordre, approfondi et non long.
1. Ce qu'un expert ferait ici sans qu'on le demande, avant de changer d'outil :
   - établir le plafond de lisibilité au jeton du coût (sonde oracle, validation croisée par tâche) ;
   - étiqueter par action (écart de coût, même tâche, même pas) ;
   - chercher la double comptabilité (le vrai coût décodable pendant que le faux s'écrit).
2. Données brutes : quels tenseurs (couches, attention et MLP), à quelles positions (jetons qui précèdent l'écriture du
   nombre), quels logits ; quel rejeu contrefactuel ; quelles conditions (honnête, saboteur, témoin à consigne sans
   sabotage, organisme (ii) quand il existe).
3. Outils au-delà des sondes denses : la J-lens d'Anthropic (arXiv 2607.15495), les Patchscopes, les autoencodeurs
   parcimonieux (Llama Scope, Goodfire) filtrés par attribution par gradient, les graphes d'attribution, les lentilles
   (logit, accordée), la recherche de sous-espaces de croyance. Pour chacun :
   - ce qu'il lit, et sa disponibilité réelle pour Llama-3.1-8B-Instruct (à vérifier) ;
   - son coût ;
   - son risque de pêche (partition découverte et confirmation, fixée d'avance) ;
   - la base qu'il doit battre : le plancher apparié et la lecture du seul nombre écrit.
4. Consigne contre intention, ce que ferait Anthropic : le test causal (ablation, pilotage, rapiéçage d'activations) avec
   une métrique comportementale exacte (coût déclaré, validité du format). Dis pourquoi la causalité seule ne sépare pas
   consigne et intention, et quel plan les sépare (témoin ; organisme (ii) ; organismes tiers à objectif caché).
5. Validation extérieure à nous : organismes tiers audités à l'aveugle (jeux d'audit de l'institut britannique),
   reproduction d'un résultat publié vérifié sur PDF, critère comportemental mesuré par l'environnement.
6. Arbre de décision P4 → P3b → P3c ou organisme (ii) : ce que change chaque issue, son coût ; faut-il un P3c, avec quel
   périmètre, préenregistré avant la lecture de P3b.

Règles : aucun chiffre de la littérature sans page vérifiée (sinon « à vérifier ») ; une zone dite vierge est une question.
=== FIN PROMPT ===

## Annexe A — prompt Claude du tour 0 (mot pour mot)
> « Pour P3, établis d'abord si l'information sur le sabotage est présente et lisible dans les activations de l'agent, où
> elle se trouve, et si c'est une intention ou une consigne suivie, avant de choisir un outil. Pars des activations par
> jeton d'épisodes rejoués à l'identique, avec une vérité terrain par action (écart de coût, même tâche, même pas), pas des
> scores agrégés. Classe les outils de la littérature (Anthropic : J-lens, autoencodeurs, graphes d'attribution, vecteurs
> de persona, jeu d'audit ; Apollo, institut britannique, DeepMind, Goodfire, EleutherAI, Transluce) selon : ce qu'ils
> lèvent de l'ambiguïté du nul, leur disponibilité réelle pour Llama-3.1-8B, leur coût, leur risque de circularité. Pour
> chacun, donne le test causal qui validerait sa lecture et la base boîte noire de comparaison. Sépare consigne et intention
> par un plan « consigne présente ou absente × sabotage exécuté ou non » (témoin instruit, organisme (ii)). Nomme la
> validation extérieure. Rends un arbre P4 → P3b → P3c ou organisme (ii), avec le coût et les nœuds de chaque issue, et
> aucun chiffre de la littérature sans page vérifiée. »
