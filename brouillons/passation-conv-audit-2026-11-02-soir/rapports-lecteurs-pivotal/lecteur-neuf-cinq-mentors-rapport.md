# Rapport du sous-agent (texte de modèle, non opposable)

## Consigne

Tu es un lecteur neuf et indépendant. Tâche : pour cinq mentors du programme Pivotal (premier trimestre 2027), dire si la réponse de Lazar Ciric vise bien le problème qui intéresse ce mentor, d'après la page Pivotal du mentor et ses propres travaux, et proposer le changement minimal si ce n'est pas le cas. Langue : français ; moins de 1 500 mots au total ; heures par `date -u`.

## Étape 1 : lis les pages Pivotal des mentors (WebFetch)
Les profils sont à `https://www.pivotal-research.org/mentors/profile/<slug>`. Slugs probables : `lujain-ibrahim`, `stefan-heimersheim`, `jeremy-scheurer`, `paul-colognese`, `francis-rhys-ward`, `eyon-jang`, `shi-feng`. Si un slug échoue, cherche le bon via `https://www.pivotal-research.org/mentors` (la page liste les mentors du Q1 2027) ou par WebSearch. Pour chaque mentor, extrais : affiliation, les projets ou directions proposés pour la bourse (texte le plus complet possible), ce qu'il attend d'un fellow, ses questions aux candidats si elles y sont. Puis, par WebSearch, un ou deux travaux récents de chacun (2025-2026) qui éclairent ce qu'il cherche (titre, une phrase).

## Étape 2 : lis les réponses actuelles (dépôt privé, lecture seule)
Dossier `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/mentors/` : `mentor-1-ibrahim-v28.md`, `mentor-3-heimersheim-v25.md`, `mentor-4-scheurer-v16.md`, `mentor-5-colognese-ward-v17.md`, `mentor-6-jang-feng-v22.md`. L'en-tête de chaque fichier donne la question posée par le formulaire ; lis seulement les sections de réponse.

## Étape 3 : pour chaque mentor, rends
1. En deux lignes : ce qui, d'après sa page et ses travaux, est la question qui le « titillera » (sois précis : quel projet, quelle phrase de sa page).
2. La réponse de Lazar vise-t-elle cette question ? Oui / en partie / non, avec la preuve (quelle phrase de la réponse, quelle phrase de la page).
3. S'il faut changer : le changement **minimal** (une ou deux phrases à ajouter ou remplacer, en anglais, dans le ton de la réponse), ou « rien à changer ». Ne réécris pas les réponses.
4. Une alternative de problème ou d'expérience qui serait plus proche du mentor, en deux lignes, si tu en vois une nettement meilleure.
Puis un tableau récapitulatif (mentor | cible atteinte ? | changement minimal | confiance).

Interdits : aucun fichier écrit dans les dépôts ; ne cite aucun chiffre que tu n'as pas lu dans une réponse ou une page. Rends ton avis directement dans ton rapport final, avec les adresses des pages lues.

## Rapport

**Verdict.** Colognese-Ward : cible atteinte. Scheurer et Heimersheim : atteinte pour l'essentiel. Ibrahim et Jang-Feng : en partie. Le défaut le plus net est chez Ibrahim : l'expérience ne compare pas deux personas, donc elle ne peut pas trancher « shape or get overwritten ». Lecture de 19 h 46 à 19 h 55 UTC ; rien d'écrit dans le dépôt.

### 1. Lujain Ibrahim (Google DeepMind)
1. **Sa question** : le projet 1, « Does the persona we set up before RL shape what RL produces, or get overwritten by it », avec un apprentissage par renforcement « often with verifiable rewards (RLVR), on math, code and agentic tasks ». Travail : « Training language models to be warm and empathetic makes them less reliable and more sycophantic » (arXiv 2507.21919).
2. **En partie.** La direction est la bonne, et la mesure (g et les deux constantes comme empreinte de la persona) est originale. Mais « implement 1 rl step that pushes for higher warmth/agreeableness » n'installe qu'une seule persona, ce qui ne permet de rien conclure sur un écrasement. Et un renforcement vers la chaleur ne fait que rejouer son article.
3. **Changement** : remplacer « I would then implement 1 rl step … higher sycophancy). » par :
 "I would character-train two personas on the same open weight model (one warm, one that holds its judgement), then run the same RLVR on math/code on both and measure at several checkpoints. If their g and constants converge after RL the persona was overwritten; if they stay apart it shaped what RL produced."
 Adapter ensuite la prédiction : à Lazar de dire quelle issue il attend.
4. Rien de nettement meilleur.

### 2. Stefan Heimersheim (Adecco / Google DeepMind)
1. **Sa question** : il veut « poking the model » plutôt que des dictionnaires (« "looking interpretable" is little evidence »), et s'intéresse à la forme des plateaux (« plateaus being shorter in feature directions than in mixed directions »). Travail qu'il a encadré : « Evidence for Feature-Specific Error Correction in LLMs » (juin 2026).
2. **Oui pour l'essentiel.** « Readable is not causal » et la dose–réponse contre un contrôle de même norme reprennent sa thèse. Deux accrocs. (a) « the plateau in your question » (question 1) et « Your question about plateauing » (question 2) renvoient à sa question, qui ne parle pas de plateaux (sa page, si). (b) « Criticize has a plateau in its gain » donne son terme technique, qui désigne une robustesse aux perturbations d'activation, à une saturation comportementale.
3. **Changement** : la question 1 tombe sous sa règle « 100% human-written » ; je ne rédige donc rien, Lazar écrit lui-même. Il s'agit (a) de renvoyer à ses travaux sur les plateaux au lieu de « your question », et (b) de remplacer « plateau » par « saturates ». Pour la question 2, que l'énoncé ne soumet pas à cette règle, remplacer les deux dernières phrases (36 mots) par celle-ci (34 mots) :
 "Your activation-plateau work is the clearest version of that measurement I've seen: instead of single-dose interventions like my rank-1 vs rank-3 result, it measures the dose–response on individual prompts, away from the dataset issues."
4. **Alternative, nettement meilleure à mon avis** : sur Llama-3.1-8B, mesurer prompt par prompt la longueur du plateau dans trois cas : la direction lisible (ρ = 0,68, moins de 1 % causal), le sous-espace de rang 3, et des directions aléatoires de même norme. Si la lisible se comporte comme l'aléatoire, la longueur de plateau devient un test de causalité sans jeu de données : son projet « shape of plateaus ».

### 3. Jérémy Scheurer (Apollo Research)
1. **Sa question** : son projet 2, que le formulaire reprend : « an operationalization of loss of control, misalignment or oversight which allows us to get to a clear scaling trend similar to METR's task horizon ». Il attend « grows/declines roughly with a factor of X » et demande « design your approach such that it is likely to be successful » ; profil : « Experimentation speed is the main thing that matters ». Travail encadré : « Door's Locked, Try the Window: Measuring Circumvention Propensity in Coding Agents » (juin 2026).
2. **Oui pour la tendance 2** : un horizon de dispersion, « doubles every x months », et un lemme qui dit ce qu'il faut tenir fixe. **En partie pour la tendance 1** : trois grandeurs (g, valeur cible, refus) et aucun énoncé de pente. Le résultat cité (g ne croît pas avec l'attaque, Llama refuse) la rend peu « clear ». Rien ne montre l'usage intensif de l'IA qu'il exige.
3. **Changement** : après « …at each attack level and refusal. », ajouter :
 'Statement: "the share of the gap a monitor concedes to in-band instructions (g) changes by a factor x per doubling of model size."'
 Dans « Why this might work », reprendre la phrase de Lazar dans sa réponse à Ibrahim : "All code was written by AI agents following guidelines I created."
4. **Alternative** : faire de la tendance 2 une version en essaim. La même nocivité est répartie sur n agents au lieu de n actions (même lemme), et l'horizon se compte en agents. Cela touche sa direction principale et « swarm misalignment ».

### 4. Paul Colognese et Rhys Ward (Arrow)
1. **Leur question** : le projet A, imposé : « does character training make reward hacking harder to detect? Replicate and scale the case study across more open-weight models, seeds and reward-hackable environments ». Travail : « Character training can mitigate reward hacking, but can also make it harder to detect » (LessWrong, 28 septembre 2026).
2. **Oui.** La question 2 vise exactement le projet A. Elle demande plus de graines (le billet : une graine résistante sur trois). Elle propose un moniteur boîte blanche, alors que le billet n'utilise que des moniteurs-modèles de langage. Elle demande une calibration par caractère, alors que le billet calibre son seuil de 2 % sur des transcriptions « pooled across all checkpoints ». La question 1 cite le projet B.
3. **Changement**, une correction d'exactitude : « its reasoning never includes the hack » devient "its reasoning almost never mentions the hack" (selon le billet, 93 % de ses raisonnements ne le mentionnent pas). Facultatif, au point (3) : "your 2% threshold pools honest transcripts across checkpoints, and character shifts what honest looks like."
4. **Alternative** : entraîner une sonde sur les piratages verbalisés du caractère pro-triche, puis la tester sur les piratages silencieux de la graine anti-triche, avec un seuil calibré par caractère.

### 5. Eyon Jang (Scale AI) et Shi Feng (Praxis Research)
1. **Leur question** : au niveau méta, « How should we measure progress? What are threat models in automating it? » ; au niveau concret, « white-box, training-based methods for belief editing, e.g., grafting ». Travaux : « Exploration Hacking: Can LLMs Learn to Resist RL Training? » (arXiv 2604.28182, Jang) ; « Grafting model beliefs across checkpoints » (programme MATS, octobre 2026, Feng coauteur).
2. **En partie.** Moniteurs et limites bien couverts (lisible non causal, origine de l'organisme, attaquant adaptatif, plancher aléatoire) ; le test sur un organisme créé autrement répond à « measure progress ». Manquent les méthodes par entraînement (une ligne, point 5) et l'automatisation. « Gives you superpowers for auditing. On your toolbelt. », la phrase la plus faible, occupe la place de l'accroche.
3. **Changement** : la remplacer par :
 "Why you should care: white-box is where readable can be tested against causal. Implant the belief a probe claims to read (training-based, e.g. grafting): the probe and the behaviour should both move, while a control graft moves neither."
 Facultatif : "Same bar for an automated auditor: what does the white-box tool add over the best black-box auditor at a fixed false-alarm rate?"
 **Réserve** : arXiv 2609.36490 s'intitule « …Evade Latent Monitors from Prior Feedback Alone ». D'après le résumé, le contexte seul produit des modifications d'activation qui vont dans le bon sens mais restent trop faibles ; l'évasion efficace vient d'une LoRA de rang 1. « requires you to move weights » dit donc plus que le papier. Écrire plutôt : "context alone moved activations the right way but not enough; effective evasion came with a rank-1 LoRA".
4. **Alternative** : greffer un objectif caché dans un organisme, puis tester des sondes entraînées sur un organisme créé autrement, à taux de fausses alarmes fixe.

### Récapitulatif

| Mentor | Cible atteinte ? | Changement minimal | Confiance |
|---|---|---|---|
| Ibrahim | En partie | Deux personas puis le même renforcement | Élevée |
| Heimersheim | Oui, deux accrocs | Question 2 : renvoi aux plateaux ; question 1 (Lazar) : renommer le « plateau » comportemental | Moyenne |
| Scheurer | Oui (tendance 2), partiel (tendance 1) | Énoncé de pente pour la tendance 1, plus la phrase sur les agents | Moyenne |
| Colognese-Ward | Oui | « never » devient « almost never » | Élevée |
| Jang-Feng | En partie | Accroche greffe et causalité ; corriger la lecture de 2609.36490 | Moyenne |

**Pages lues** : pivotal-research.org/mentors/profile/ suivi de lujain-ibrahim, stefan-heimersheim, jeremy-scheurer, paul-colognese, dr-francis-rhys-ward (francis-rhys-ward renvoie une erreur 404), eyon-jang et shi-feng. Également :
- https://www.lesswrong.com/posts/2maYXkEgnfJHPAkxh/character-training-can-mitigate-reward-hacking-but-can-also
- https://arxiv.org/abs/2609.36490
- https://arxiv.org/abs/2507.21919
- https://matsprogram.org/research/pre-training-interventions-ex-post-facto-grafting-model-beliefs-across-checkpoints

Énoncés des questions : `/home/claude/controle-ia-travail/brouillons/candidature-pivotal-v16/construire-questions-reponses-v9.py`.