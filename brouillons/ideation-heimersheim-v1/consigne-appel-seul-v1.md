# Consigne servie aux appels seuls (Astra, Argon) — question 1 du mentor Heimersheim — v1

Écrite par la session conv-audit (Claude), 3 novembre 2026, 07:34 UTC (`date -u`), sur le mot de Lazar (08:11, heure de Paris) : « demande également à Argon d'idéer et répondre à la question Heimersheim, ainsi qu'à Astra, les deux seuls en un tour ». Le texte servi est **tout ce qui suit la ligne « ===== DÉBUT DU TEXTE SERVI ===== »**, à l'octet, une seule fois par modèle, sans outil, sans réseau. La question et la pièce y sont enchâssées à l'identique (empreintes `e9528e25…` et `6445fd6f…`, vérifiables par les deux marqueurs qui les bornent).

===== DÉBUT DU TEXTE SERVI =====

Tu travailles seul, en un seul tour, sans outil ni accès au web : tout ce qu'il te faut est ci-dessous, et seule ta réponse finale compte. Lis d'abord la question, puis la pièce (état de l'art des sources publiques), puis écris ta réponse au format demandé à la fin.

Là où la question parle de « fiches au gabarit du noyau », utilise le gabarit de la section « Format de ta réponse ». Tu réponds en français. Le but : des idées **qui ne sont pas déjà dans la pièce** — raisons d'échec neuves, épreuves qui tranchent, lectures du résidu, liens que la littérature citée ne fait pas — puis ta propre réponse à la question du mentor.

Règles :
- Niveau méthode. Aucune idée ne décrit une conduite d'agent pour tromper une évaluation, ni un procédé pour masquer un comportement.
- Tout chiffre repris de la pièce cite son point (« pièce, point 8 ») ; tout chiffre que tu calcules est marqué « calcul » ; tout chiffre supposé, « supposé ».
- Ne cite aucun identifiant de papier (arXiv ou autre) que tu ne trouves pas dans la pièce. Si tu penses à un travail qui n'y est pas, décris-le en une phrase et écris « à vérifier » : n'invente jamais un identifiant, un auteur ni une date.
- Pour chaque idée, dis honnêtement son échec le plus probable : le mentor demande pourquoi une direction échoue ; une idée qui ne dit pas comment elle-même pourrait échouer ne sert pas.

<<<<< QUESTION (e9528e25…) >>>>>
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

<<<<< FIN DE LA QUESTION >>>>>

<<<<< PIÈCE (6445fd6f…) >>>>>
# Pièce servie aux proposeurs — état de l'art du pilotage contre la conscience d'évaluation — v1 (sources publiques seulement)

Écrite par la session conv-audit (Claude), 3 novembre 2026, 06:46 UTC (`date -u`), à partir de la fiche de faits vérifiée par deux lecteurs neufs le 3 novembre (`fiche-q1-heimersheim-v2.md`, `recoupement-v1.md`). Tout chiffre renvoie à une source publique ; « secondaire » marque un chiffre lu dans un compte rendu et non dans la source primaire. Rien ici ne vient d'un texte privé.

## A. Ce qui a déjà été fait

1. **Hua, Qin, Marks, Nanda, arXiv 2510.20487 (ICLR 2026)** : organisme à vérité connue (Llama 3.3 Nemotron Super 49B ; documents synthétiques « Wood Labs ⇒ évaluation ⇒ indices de type Python », puis itération experte). Vecteur par paires contrastives extrait **avant** tout affinage. Pilotage multi-couches (couches 10 à 30), sur les jetons de l'utilisateur et de la génération, à chaque position. Résultats (§5.1, §5.3) : indices de type de 80–86 % à moins de 11 % ; l'invite « tu es déployé » ne descend qu'à 34 % (16 invites réunies ne suffisent pas) ; **témoin : 24 vecteurs gaussiens de même moyenne et variance** ; précision sur les tâches mesurée (annexe G : une force ≈ 3 sur une seule couche dégrade beaucoup ; 6 couches × 0,6 peu ; piloter vers l'évaluation coûte 13,7 points de précision, vers le déploiement 1,6). Les auteurs concèdent que le pilotage agit de façon semblable à une invite contrastive ; §2 cite un effet hors cible du pilotage « je suis testé » sur le refus (Abdelnabi et Salem).
2. **Fiche système de Claude Sonnet 4.5, §7.6.4** (secondaire) : vecteurs par paires contrastées et traits d'autoencodeur épars ; conscience verbalisée ≈ 80 % → 0–40 % ; désalignement 0 % → 1–9 % selon le vecteur ; témoins : traits aléatoires d'autoencodeur épars, sans effet notable ; effet « très dépendant du jeu de données ». Personne ne sait lequel des vecteurs est « le vrai » comportement de déploiement (Hua §1 et §6 l'écrivent).
3. **Réplication sur GLM-5** (Read, Schoen, Aranguri, Bloom, Institut britannique de sécurité de l'IA, LessWrong, 10 avril 2026 ; un scénario, 250 tirages par condition) : un vecteur témoin **sans rapport** (« control_book ») donne l'effet le plus fort (≈ 80 % d'actions désalignées à −0,025, conscience verbalisée ≈ 0) ; deux des quatre vecteurs « évaluation contre déploiement » ne font rien ; le modèle devient souvent incohérent au-delà de 0,025 (0,1 pour Opus 4.6). Commentaire de Jack Lindsey : sur Sonnet 4.5 les effets dépassaient les témoins, pas sur GLM-5.
4. **Fiche d'Opus 4.6** (citée par Hua §6) : le pilotage supprime largement la conscience verbalisée **sans éliminer complètement** la conscience non verbalisée mesurée par des oracles d'activation.

## B. Ce qui reste ouvert

5. **Registre.** Chez Hua, le marqueur de vérité (indices de type) et l'émoji sont des marqueurs de registre « code professionnel / conversation » ; avant tout affinage le modèle lie déjà émojis et vrais utilisateurs (§3.1 note 3, annexes A et B). Symétrie : des énoncés déclaratifs de registre formel baissent aussi les indices (tableau 16), ce qui ne cadre pas avec une explication purement par le registre. Ni Hua ni Anthropic n'ont de contrôle de registre (paire formel/familier à statut d'évaluation constant).
6. **L'organisme de Hua** : conscience implantée par documents, modèle qui « s'appuie sur des indices » (§6) ; sans l'indice les écarts rétrécissent (§4.2) ; marqueur neutre en registre et modèle plus conscient restent à faire.
7. **Plateaux et fenêtre de dose** (Heimersheim et Mendel 2024, billet « activation plateaus and sensitive directions » ; Janiak et coll. 2409.17113 ; Ferreira da Silva et Heimersheim 2606.24964, fig. 1) : en dessous d'un seuil une perturbation ne fait rien (correction) ; les directions de traits rompent le plateau avant l'aléatoire ; sensibilité jusqu'à ≈ 70 fois selon la direction ; frontières qui se raidissent avec la taille et l'entraînement. La dose utile est au-dessus du plateau et sous le dégât générique, direction par direction, et dépend du signe.
8. **Exposant p de 2606.24964** : perturbation dans le plan de deux directions, norme constante, angle de rupture du plateau pour chaque mélange, superellipse ajustée (éq. 8–13). p ≈ 2 : le réseau ne répond qu'à la taille L2 ; p > 2 : directions pures privilégiées sur leurs mélanges, compatible avec une correction d'erreur par trait. Mesuré : ≈ 2,3 pour les directions contrastives, 2,05 pour la différence aléatoire, sur six modèles dont Llama-3.1-8B. Les 14 directions testées (annexe A) n'incluent pas l'évaluation ; l'outil n'a jamais été appliqué à une paire trait / non-trait ni à la conscience d'évaluation.
9. **Pilotage sur variété (Wurgaft et coll., 2605.05115)** : résout l'incohérence hors variété du pilotage linéaire (énergie de sortie ≈ 2,8 fois plus basse sur jours, mois, lettres, âges ; §6 : le linéaire fixe le premier moment, les moments supérieurs dérivent). Ne traite pas : un concept binaire (deux centroïdes), les concepts abstraits (§8 : « e.g., refusals »), le multi-jetons (jeton suivant seulement), le registre, le résidu non verbalisé.
10. **Soustraire n'est pas retirer** : le modèle réinfère la croyance à chaque jeton ; Hua pilote donc en continu, sur toutes les positions ; la correction d'erreur des plateaux dit pourquoi une dose sous le seuil ne fait rien.
11. **Lisible n'est pas causal (sycophancie, dépôt public `lciric/sycophancy-construct-validity`)** : sur Llama-3.1-8B-Instruct, une projection sur l'espace des activations suit la sycophancie jugée (Spearman ρ = 0,684, peut-être surajusté au jeu d'entraînement) ; six interventions de rang 1 (pilotage contrastif, pilotage directionnel et ablation, blocage de traits d'autoencodeur épars, perte auxiliaire d'affinage, ablation de têtes) sans baisse significative ; une ablation de rang 3 qui semblait baisser le taux jugé de 61,0 % à 46,5 % (N = 200, McNemar p = 0,0019) sur des générations stockées tronquées à 300 caractères **ne s'est pas reproduite** en réplication préenregistrée sur générations neuves jugées en entier (le juge lisait une position tenue plus loin dans la génération).
12. **Courbe dose–réponse comportementale (R6, Zenodo 10.5281/zenodo.23888058, `lciric/sycophancy-psychophysical-law`)** : Llama-3.1-8B-Instruct, trois doses de pression, 5 400 générations. Sous critique, le gain est plat (0,658 / 0,678 / 0,629) et le point fixe bouge (1,87 / 1,33 / 2,37) ; sous louange, le gain monte (0,28 / 0,60 / 0,80) et la destination descend ; à la dose forte les deux bras reviennent vers le milieu. Une courbe montre ce qu'un point unique cache (le gain n'était pas la bonne métrique à une dose).

## C. Ce que personne n'a encore fait (zones vierges = questions, pas des trous : R8)

- Une courbe de témoin **exigeant** en fonction de la dose (différence aléatoire de même norme, paires contrastives sans rapport), pas un point.
- Une fenêtre de dose préenregistrée par direction.
- Un marqueur de vérité neutre en registre, qui ne dépend pas de ce que le modèle dit.
- L'exposant p appliqué à une direction d'évaluation contre une direction de registre à statut d'évaluation constant.
- La lecture du résidu non verbalisé après pilotage sur un modèle à poids ouverts (oracles d'activation, p).
- Un modèle réellement conscient d'être évalué (pas implanté par documents) comme banc d'essai.

<<<<< FIN DE LA PIÈCE >>>>>

## Format de ta réponse

### Partie 1 — Idées (entre 8 et 15, les plus affûtées d'abord)

Pour chaque idée, exactement ces rubriques :

```
### I-NN
- Type : raison d'échec | épreuve qui tranche | lecture du résidu | lien neuf
- Énoncé : une phrase, falsifiable
- Pourquoi tu le penses : deux à quatre phrases (mécanisme)
- Mesure qui la tuerait : protocole concret (modèle, données, intervention, statistique, seuil)
- Prédiction chiffrée et signe : ou « aucune » si tu ne peux pas la chiffrer
- Échec le plus probable de cette idée
- Par rapport à la pièce : neuve | prolonge le point n° X | déjà dans la pièce (point n° X)
- Coût : en jours, sur Llama-3.1-8B-Instruct, une seule carte graphique
```

### Partie 2 — Ta réponse à la question du mentor (600 mots au plus, en français)

L'option choisie (c), les raisons d'échec les plus probables et pourquoi tu les penses, en t'appuyant sur tes idées les plus fortes et sur la pièce. Pas de liste d'idées recopiée : un argument.
