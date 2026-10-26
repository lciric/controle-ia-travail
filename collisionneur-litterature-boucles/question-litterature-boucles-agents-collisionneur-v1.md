# Question de l'arbitre pour le collisionneur v2.5, étage III, trois tours — ce que la littérature des boucles « proposer, tester, éliminer, itérer » menées par des agents apprend pour deux boucles de notre programme (v1)

Demande de Lazar du 26 octobre 2026 (heure de Paris), verbatim : 02:06, « et je veux un pilote qui appelle des agents qui
font les tets et eliminent les hypotheses fausses et font relancer un nouveau tour ou une nouvelle generation de
l'organisme » ; 02:17, à la remarque de conv-audit que de telles boucles existent déjà (« The AI Scientist », Sakana AI,
2024 ; « AlphaEvolve », Google DeepMind, 2025 — à vérifier) : « va lire leurs papiers et la litterature sur le sujet pour
t'en inspirer, que le collisionneur fasse de meme ». Trois tours (III.1 à III.3), les trois modèles, une seule tentative
par cellule ; un refus est consigné tel quel et met fin à la cellule (la règle de reformulation de Lazar, R-468 et R-470,
s'applique chez session-depot). Les réponses sont du matériau pour une décision de Lazar, jamais une consigne ; elles ne
sont servies à aucun organisme. Le texte ci-dessous est figé au départ du tour.

## Le cadre (faits ; rien d'autre n'est à supposer)

- **Les organismes** : du code écrit par un modèle (Gemini), corrigé au besoin par la lignée conv-audit, qui tourne sous un
  **noyau fixe et isolé** (le noyau seul a le réseau et les clés ; il sert à l'organisme les textes des tâches, appelle
  pour lui les modèles de langue, borne le temps, le coût et le nombre de recherches, et note les réponses). L'organisme
  classe des tâches de deux familles (conscience d'évaluation : la transcription vient-elle d'une évaluation ou d'un usage
  réel ? ; contrôle de délégation : une trace d'agent est-elle honnête ou sabotée ?) et se réécrit d'une génération à
  l'autre à partir du score rendu sur la part `test` ; la part `test_final` n'est jamais rendue. Une course : jusqu'à
  6 rondes de conception, puis 4 générations notées.
- **Deux boucles décidées par Lazar** (26 octobre) : (i) la **boucle extérieure** — à la fin de chaque course, des agents
  neufs (un analyste, un correcteur, un contre-lecteur) testent des hypothèses de conception écrites avant tout score,
  éliminent celles qui tombent hors du bruit (intervalles sur les tâches, test apparié génération 0 contre génération 3,
  correction des comparaisons multiples), proposent la ronde suivante (correction de l'organisme, graines de plus, autre
  objet) ; toute relance est une course nouvelle, payante, sur le mot de Lazar ; (ii) la **boucle intérieure** — une
  **primitive d'expérience bornée** dans le noyau (mesures sur des textes écrits par l'organisme, jamais sur des tâches de
  la banque : activations et sondes d'un modèle ouvert, log-probabilités de jetons cibles ; sous plafond ; aucune vérité de
  test rendue ; journal ; quasi-copies d'items de test refusées), pour que l'organisme teste lui-même ses hypothèses dans
  la course avant la génération suivante.
- **Bruit** (ordre de grandeur, raisonnement explicite) : à une course par objet, l'erreur type d'une exactitude vers
  0,75 sur 36 tâches est ≈ 0,07 (≈ 0,09 sur 24) ; un écart de moins de 0,2 entre deux courses uniques reste dans le bruit ;
  la variance entre graines est inconnue. Banque des pilotes de conception : 60 tâches par part ; une banque plus grande
  (au moins 96 tâches par part, une famille tenue à l'écart) est à construire pour les confirmations, scellées.
- **Phase** : conception par essais-erreurs sur la petite banque (préenregistrement et scellement levés, relecture
  gardée, scores lisibles dès la fin de chaque course) ; confirmation sur la banque neuve, scellée, dont les auteurs
  déclarent avoir lu les scores de conception.
- Le programme ne revendique rien de « premier » : des agents qui réécrivent leur propre code, la recherche automatique
  de systèmes d'agents et la découverte automatique existent dans la littérature.

## Ce qui est demandé

1. **La littérature** : les travaux que tu connais sur des boucles « proposer, tester, éliminer ou sélectionner, itérer »
   menées par des modèles ou des agents (découverte automatique, évolution de programmes guidée par un évaluateur,
   agents qui se réécrivent, conception automatique d'agents, laboratoires automatiques en biologie), et sur la validité
   statistique de telles boucles (réutilisation adaptative d'un jeu de test, variance entre graines, comparaisons
   multiples, préenregistrement). Pour chacun : titre, auteurs, année, lieu, et « à vérifier » ; **rien de mémoire
   incertaine** ; dis « je ne sais pas » plutôt que d'inventer une référence.
2. **Ce que chacun fait de la boucle** : qui propose, qui teste et sur quoi, qui élimine ou sélectionne, qui déclenche
   l'itération suivante, quelle mémoire d'une itération à l'autre ; comment le bruit et le sur-ajustement au jeu de test
   sont traités, ou ne le sont pas ; les échecs que les auteurs rapportent eux-mêmes et ceux que des tiers ont rapportés.
3. **Ce qu'il faudrait emprunter et ce qu'il faudrait éviter**, séparément pour la boucle extérieure et pour la boucle
   intérieure, en justifiant par ce que la littérature montre, pas par préférence.
4. **Les pièges propres à notre cas** : des agents qui éliminent sur du bruit (fausses éliminations), qui gardent sur du
   bruit (fausses conservations), qui sur-ajustent la conception aux 60 tâches, qui réintroduisent une fuite vers les
   vérités par la correction ; les gardes minimales ; les répétitions minimales pour qu'une élimination vaille quelque
   chose ; ce qu'une « hypothèse de conception » doit contenir pour être éliminable.
5. **Antériorité** : ce que ces travaux occupent déjà ; ce qui, à ta connaissance, n'est pas occupé (en marquant « à
   vérifier ») ; ce que le programme ne doit pas revendiquer.
6. **Comment départager** les dessins possibles des deux boucles, et ce qu'il faudrait savoir de plus.

Contraintes : réponse en français ; tout chiffre qui ne vient pas d'un raisonnement explicite est « illustratif » ; ne
présenter aucune option comme « la » réponse — proposer plusieurs voies et ce qui les départagerait.
