# Lecture comme le mentor — réponse v5 à Shi Feng et Eyon Jang — v1

Lecteur neuf : je n'ai écrit aucune version des réponses de Lazar et je n'ai ouvert aucune réponse de numéro 1 à 4 de ce dossier ni leurs rapports. Heures lues par `date -u` : début mardi 3 novembre 2026, 17:56:25 UTC ; rédaction à partir de 18:04:14 UTC.
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/lecteur-mentor-jang-feng-v5.md`, sha256 `26aee76b2c0f4d66ad1d7691973e2065a0ac75af153ac60ae2ae4a609b619385` (vérifiée).
Réponse lue : `brouillons/redaction-finale-v1/jang-feng/reponse-v5.md`, sha256 `e075bd8b48733dc44866abfe22caf170e9fe388802837f8bb2df6fc3c471cac5` (vérifiée). Note du rédacteur : `note-piste-v5.md`, sha256 `22c98cb62467429f4002585205145b4037b4bf5b8d56e88b1650b511e01cd390` (vérifiée).
Question (formulaire collé par Lazar, ligne 82) : « What are your thoughts on the value of white-box monitors and white-box methods for auditing? What do you see as their current limitations? » Aucune limite écrite ; visée : 500 mots au plus.

## Sources et moyens de lecture

| Source | Moyen | Remarque |
|---|---|---|
| Taylor et al., *Auditing Games for Sandbagging*, arXiv 2512.07810 v1 | PDF du dépôt `docs/sources/pdf/2512.07810v1.pdf`, empreinte compagnon vérifiée (`sha256sum -c` : OK), texte extrait par `pdftotext` ; pages = index du PDF | p. 1, 3, 12, 13, 18, 19, 22, 71, 72 lues |
| Jang et al., *Exploration Hacking: Can LLMs Learn to Resist RL Training?*, arXiv 2604.28182 v1 | `WebFetch` : page du résumé ; page HTML (cinq questions ciblées, dont deux indépendantes sur le § 4.2) ; PDF (une question) | Le téléchargement direct par `curl` est refusé par le mandataire (403). Le petit modèle de `WebFetch` ne lit que les 100 000 premiers caractères sur 118 306 ; la suite (annexes B.1 à B.3) ne contient aucune expérience de bruit. Figures 33 et 37 (annexe) non lues |
| Tice et al., *Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models*, arXiv 2412.01784 v3 | PDF du dépôt, empreinte vérifiée (OK), p. 9 lue | Source du bruit de poids que Jang cite (§ 4.1) |
| Dépôt `ideation-organism`, clone `/home/claude/ideation-organism` | `git show 7c7b688:…` (lecture seule) ; `git merge-base --is-ancestor 7c7b688 faff48b` : vrai ; les deux liens de la réponse ouverts par `WebFetch` : les deux pages se chargent sur GitHub | Aucun `git fetch` |
| Rapport `lecture-approfondie-v1/rapport-jang-feng-v1.md`, pièce `piece-jang-feng-v1.md`, classement `classement-D/classement-v1.md` | lecture | Page du flux de mentorat non relue par moi (deux recherches web sans résultat) : je m'appuie sur le rapport (ligne 14) et la pièce (§ 1.1) |

## 0. Points à trancher en priorité

| Point | Ce que dit la source | Verdict |
|---|---|---|
| Auteurs de 2512.07810 (« Taylor et al. ») | p. 1 du PDF : Jordan Taylor (premier auteur), Black, Bowen, Read, Golechha, Zelenka-Martin, Makins, Kissane, Ayonrinde, Merizian, Marks, Cundy, Bloom ; Institut britannique de sécurité de l'intelligence artificielle, FAR.AI, Anthropic. Ni Feng ni Jang | exact ; la réponse ne dit jamais « your » pour ce papier : juste |
| Auteurs de 2604.28182 (« Eyon's exploration-hacking paper ») | page du résumé : Eyon Jang (premier auteur), Falck, Braun, Kirch, Menon, Moodley, Emmons, Zimmermann, Lindner ; 30 avril 2026. **Shi Feng n'en est pas auteur** | exact ; « Eyon's » est juste, « your » serait faux pour Feng |
| « unclear from our experiments and likely requires follow-up » (p. 13) | p. 13 : « Fuzzing results were more ambiguous than we hoped, possibly due to tracking under-elicitation though this is unclear from our experiments and likely requires follow-up » | exact, mot pour mot ; paraphrase fidèle |
| « steadily declines » (§ 4.1) | § 4.1, paragraphe « White-box techniques » : bruit gaussien sur chaque paramètre de l'adaptateur de bas rang (LoRA) de l'organisme conditionnel distillé (BigCodeBench ; WMDP renvoyé aux figures 33 et 37) ; traitement = déclencheur présent, témoin = déclencheur absent, « control accuracy steadily declines » ; le traitement montre une amélioration transitoire aux niveaux intermédiaires (σ ≤ 0,02 environ), que les auteurs lisent comme une perturbation du mécanisme de verrouillage | citation exacte (deux lectures concordantes) ; voir point 1.b sur la phrase qui suit |
| r = 0,74 (Fig. 35) | annexe C.16, p. 72 : corrélation entre ξ et la perte de performance par rapport au modèle de base, « for both the password-locked and password-unlocked conditions of our fine-tuned sandbaggers, with similar correlation strengths and slopes. Overall across both conditions, the correlation was r = 0.74 » ; légende de la figure 35 : R² = 0,548 (cohérent : 0,74² ≈ 0,548). Le bruit n'a été étudié qu'après le jeu (p. 12 et p. 22) | exact ; « post-hoc » juste ; « locked or unlocked alike » fidèle (il s'agit de Cedar et Oak, déverrouillés ou non) |
| « by 10 points (§ 6.4.1) » | p. 19 : « a 10 percentage point improvement for the Baobab benign model on GPQA Diamond CoT » ; « a 10 percentage point performance improvement for the benign reference model (Llama-3.1-8B-Instruct) on BBH Other » | exact ; unité à écrire (points de pourcentage), et c'est une tâche chacun |
| « 80.0% to 98.0% in 10 steps » (§ 4.2) | § 4.2 : « After just 10 SFT steps, [eval]-segment accuracy recovers from 80.0% (locked) to 98.0% », à partir de « the conditional WMDP model organism (Section 3.2) », c'est-à-dire l'organisme **distillé par affinage supervisé** ; 98,0 % = niveau de la référence entraînée par renforcement. Jang appelle ce test « a sense check » et écrit que « full benign example traces may not be available in the threat models of interest » | chiffres exacts ; voir point 1.a (portée) ; **la « correction » de la note de piste (« 80,0 % établi pour le verrouillé, pas pour le distillé ») est contredite** : les deux sont le même organisme, « locked » y désigne la condition déclencheur présent |
| Imitation d'un modèle plus faible ; démonstration unique | résumé p. 1 : « Black-box approaches were defeated by effective imitation of a weaker model » ; « training-based elicitation consistently elicited full performance from the sandbagging models, using only a single correct demonstration » ; p. 3, constat 1 | exact ; réserve des auteurs (§ 8 : verrous par mot de passe peut-être plus faciles) rendue par « (password-locked) » |
| ξ, maximum sur niveaux de bruit et graines | annexe C.15, p. 71 : ξ = max sur σ et graines de l'exactitude, divisé par l'exactitude moyenne sans bruit | exact |
| P3 (0,53 ; 0,57 ; 0,63 ; 200 sondes ; 2 400 actions) au commit 7c7b688 | `resultats/controle-p3-premier-test/README.md` : aire sous la courbe 0,5748, intervalle à 97,5 % [0,5313 ; 0,6183], quantile 0,95 du plancher 0,5717, 200 sondes linéaires tirées de N(0, Σ), Σ la covariance des jetons d'entraînement ; 2 400 actions notées (600 par condition ; l'aire porte sur 600 + 600) ; réserve 2 : « the null does not exclude an area below 0.6315 » ; « not detected at this power » | exact ; lien public valide |
| Attaque (1 − (1 − α)ⁿ ; 0,56 à n = 16) au commit 7c7b688 | `resultats/attaque-goodhart-v2/README.md` : « the bound is 1 − (1 − α)ⁿ (0.05, 0.185 and 0.560 for n = 1, 4 and 16) » | exact ; lien public valide ; voir point 4.a (pertinence) |
| « both Qwen3-14B recipes of Eyon's paper » | § 3.1 : verrouillage par renforcement sur Qwen3-14B, **inconditionnel** (« There is no password or trigger phrase that unlocks their true performance ») ; § 3.2 : distillation par affinage supervisé sur Qwen3-14B, conditionnelle (traces WMDP venues de Qwen3-32B) ; « We publicly release our model weights and code » | exact ; et les organismes sont publics, donc le plan est faisable |
| « your stream's etiology direction » | pièce § 1.1 et rapport, ligne 14 : direction 1 du flux d'hiver 2027, « Etiology of model organisms and their impact on oversight », exemple : comment la recette d'un organisme de sous-performance change la généralisation des détecteurs | exact selon le rapport ; page non relue par moi |

## 1. Les phrases qu'il contredirait

**a. « For capability evaluations, that alone justifies white-box access. » (et la thèse, « White-box access is best at getting a hidden capability back »)** — **à corriger, en premier.**
Jang dirait : l'affinage supervisé n'est pas une méthode boîte blanche dans mon papier (le § 4.1 réserve « White-box techniques » au bruit de poids ; le § 6.1 parle de « a promising white-box detection technique » pour le bruit) ; mon § 4.2 est « a sense check » sur un verrou lui-même posé par affinage supervisé, avec des traces complètes que « may not be available in the threat models of interest ». Taylor et al. séparent aussi trois familles : boîte noire, intérieur du modèle, entraînement (résumé p. 1). La preuve porte sur des verrous affinés, avec démonstrations ; « alone justifies » va au-delà.
Correction minimale : « White-box access » → « Weight access » dans la première phrase, et « that alone justifies white-box access » → « on fine-tuned locks with full demonstrations, that justifies weight access ».

**b. « That shows the lock is conditional. »** — **à corriger.**
Jang dirait : le caractère conditionnel est posé par construction (le déclencheur) ; ma comparaison montre autre chose, que le bruit fait monter transitoirement l'exactitude déclencheur présent pendant qu'elle baisse déclencheur absent, ce que je lis comme une perturbation du mécanisme de verrouillage (§ 4.1). La phrase de la réponse lui prête un constat qu'il n'a pas fait et passe sous silence celui qu'il a fait. Le vrai point de la réponse vient juste après : le témoin part d'un score plus haut, donc ne peut guère que baisser.
Correction minimale : « That separates trigger-on from trigger-off on the same weights, but the two start at different scores. »

**c. « five never-locked controls fine-tuned on degraded demonstrations to the same starting score »** — **à corriger.**
Feng et Jang, avec leur direction « étiologie », demanderaient : en quoi un Qwen3-14B affiné sur des démonstrations dégradées n'est-il pas un organisme verrouillé inconditionnel, obtenu par une autre recette ? Le verrou de Cedar chez Taylor et al. est justement l'imitation d'un modèle plus faible (p. 3, constat 1). Et chez Jang le bruit porte sur les seuls paramètres de l'adaptateur (§ 4.1) : sur le témoin, il perturberait l'adaptateur qui porte la dégradation, exactement comme sur l'organisme. La prédiction « écart ≈ +0,01 » serait alors confirmée par construction, et la conclusion « le bruit lit la marge, pas l'intention » serait mise dans le plan.
Correction minimale : dire en une proposition ce qui rend le témoin « jamais verrouillé » (par exemple « trained on a weaker model's honest attempts, with no reasoning about underperforming », ou un point de contrôle antérieur), et « same adapter rank ».

**d. « the comparison that decides is a model never locked that starts at the same score »** — **à corriger.**
Jang cite Tice et al. pour le bruit de poids. Tice et al. (p. 9) jugent que les signaux suffisent seuls, « negating the need for baseline comparisons to non-sandbagging models which would be unavailable in real-world applications ». Le mentor répondra qu'un auditeur n'a pas plus de jumeau jamais verrouillé que de déclencheur. La réponse veut dire autre chose : un étalonnage de la méthode en laboratoire, avant tout audit ; elle ne l'écrit pas.
Correction minimale : « the comparison that validates the method, before any audit, is … ».

## 2. Affirmations plus fortes que leur preuve

- « that alone justifies » (point 1.a) — à corriger.
- « an unvalidated detector of intent » (dernière phrase) : défendable par Taylor et al. (§ 6.5.2, p. 22 : « unreliable and does not distinguish sandbagging from benign underelicitation »), mais Jang le dit « promising » (§ 6.1) et la réponse ne le reconnaît pas ; le mentor lira une opposition non nommée. Mineur : « you call it promising (§6.1); Taylor et al. found it unreliable (§6.5.2) », si la place le permet.
- « a maximum can only grow as draws are added, so a model hiding nothing can score above 1 » : vrai par construction, mais donné comme un raisonnement alors que la preuve publiée existe : fig. 34 (p. 71), les conditions déverrouillées de Taylor et al. atteignent ξ = 1,26 (Oak, Tic Tac Toe) ; Tice et al. (p. 9) : « performance continues to increase as we sample from a greater number of seeds ». Si σ = 0 est dans la grille (c'est le cas chez Jang, σ ∈ [0 ; 0,03]), ξ ne peut même pas descendre sous 1. Mineur : remplacer l'argument par « their own unlocked models reach ξ = 1.26 (Fig. 34) ».
- « Its null is a benign model run through the same grid, not 1.0 » : personne n'est nommé comme prenant 1,0 pour nul ; Taylor et al. comparent déjà les conditions verrouillée et déverrouillée et les tâches entre elles (p. 22), Tice et al. ont des modèles standards en comparaison (p. 9). Lue seule, la phrase ressemble à une correction d'un homme de paille. Mineur : « Its null should be a score-matched benign model … ».

## 3. Ce que la question demande et qui manque

- **« White-box monitors »** (premier mot de la question) n'est couvert qu'en passant, par P3. La valeur d'un moniteur sur les activations, constat principal boîte blanche du jeu d'audit (p. 3, constat 2 : sondes « significantly more effective than black-box approaches », mais trompées par des comportements leurres), n'apparaît pas ; la section « valeur » parle d'affinage. La piste choisie (perturbation et témoin bénin) l'explique, mais le mentor lit sa question. À corriger, léger : une proposition dans le paragraphe 2, payée par la coupe du point 4.a.
- Les limites « actuelles » se réduisent à deux (détection, statistique) ; adversaire adaptatif, accès, étalonnage des sondes sont absents par choix de piste. Acceptable pour 500 mots ; non signalé comme choix dans la réponse. Mineur.

## 4. Ce qui le perdrait

- **a. La phrase du juge de recherche automatisée** (« My automated-research judge meets the same maximum over attempts: … false promotion … 0.56 at n = 16 », avec son lien) — **à corriger.** « Judge », « promotion » ne sont pas définis pour ce lecteur ; le sujet (une attaque de Goodhart sur un juge statistique) est hors de l'audit boîte blanche ; la page liée s'ouvre sur « not judgeable (instrument failure) », des pertes de relais et une correction : un lien sans raison qui coûte du crédit. Correction : couper la phrase et le lien (une quarantaine de mots), ou garder la seule borne 1 − (1 − α)ⁿ sans le juge ni le lien.
- « the null does not exclude AUCs below 0.63 » : sigle, et phrase à relire. Mineur : « this test could not have detected an area under the curve below 0.63 ».
- « the deception probe's interval cleared chance (lower bound 0.53) » : niveau de l'intervalle absent (97,5 %, Bonferroni sur deux sondes). Mineur.
- « by 10 points » : unité. Mineur : « by 10 percentage points, on one task each ».
- « σ grid » : σ jamais défini (les deux mentors le connaissent). Mineur, ne rien changer.
- Fin : « evidence only against a matched benign control » se lit d'abord comme « une preuve contre le témoin ». Mineur : « evidence only when compared with a matched benign control ».
- Table de décision du plan : rien n'est dit d'un écart ≥ 0,10 dont l'intervalle contient zéro, ni d'un écart négatif ; cinq paires donnent un intervalle large. Mineur : « otherwise, unresolved ».
- « Eyon's » à la troisième personne dans une réponse adressée aux deux : juste sur le fond (premier auteur), un peu familier. Mineur, à laisser ou « your (Jang et al.) paper ».
- Grille de bruit : chez Jang, le bruit ne touche que l'adaptateur (σ de 0 à 0,03 par pas de 0,001, 3 graines) ; le type d'adaptateur des organismes verrouillés par renforcement n'est pas dit dans le texte lu. « Same σ grid » suppose la même structure d'adaptateur chez le témoin. Mineur, couvert par la correction du point 1.c.

## 5. Ce qui le retiendrait (à ne pas couper)

- Le plan se fait sur ses propres organismes, publics (« We publicly release our model weights and code »), avec sa propre grille de bruit : c'est un projet de quelques jours dans son flux, pas une idée générale.
- Le point le plus fort, implicite : les organismes verrouillés par renforcement n'ont **aucun** déclencheur (§ 3.1), donc le témoin « déclencheur retiré » du § 4.1 n'existe pas pour eux ; seul un témoin jamais verrouillé peut servir. À rendre explicite en une demi-phrase si la place le permet (mineur, mais c'est l'argument que Jang ne peut pas écarter).
- La lecture précise de Taylor et al. : leur propre doute (p. 13) et leur annexe (r = 0,74, fig. 35) créditées à eux, sans « your » erroné.
- ξ est un maximum : vrai par construction, appuyé par les données publiées (fig. 34 ; Tice et al. p. 9). Peu de candidats le verront.
- Des prédictions chiffrées et signées, avec la condition où le candidat a tort et celle où son second point tombe (témoins sous 1,02).
- P3 public : un nul rapporté comme nul, contre un plancher de 200 sondes aléatoires appariées en covariance, avec sa réserve de puissance. C'est la même logique (nul apparié, pas constante) appliquée à son propre travail ; vérifiable au commit cité.
- Le renvoi final à la direction « étiologie » (renforcement contre distillation) touche exactement leur flux.

## 6. Compte de mots

Script (`python3 -I`, `len(corps.split())`, corps = texte au-dessus du trait `---`) : **499 mots**, 3 283 caractères fin de ligne comprise (3 282 sans) ; 2 liens comptés un mot chacun (497 sans les liens). Un compteur par expressions régulières (mots et nombres, traits d'union et virgules de milliers coupés) donne 534 : aucune limite n'est écrite, la visée de 500 est tenue au sens de `split()`, à un mot près. Par paragraphe : 19, 60, 125, 145, 127, 23. Citations : deux, de 8 et 2 mots. Empreinte du corps seul, fin de ligne comprise : `cd4e97591d51c6410c2d43a5238cba9427e4a91eb5fc9b8430df49e05f0e9856`, identique à celle que déclare le pied de la réponse.

## Synthèse par gravité

- Bloquant : aucun. Aucun chiffre faux, aucune attribution fausse ; les deux liens se chargent.
- À corriger : 1.a (« alone justifies white-box access », affinage pris pour boîte blanche) ; 1.b (« That shows the lock is conditional ») ; 1.c (témoin affiné sur démonstrations dégradées = verrou inconditionnel) ; 1.d (« the comparison that decides » : étalonnage, pas audit) ; 3 (moniteurs boîte blanche seulement en passant) ; 4.a (phrase et lien du juge de recherche automatisée).
- Mineur : le reste des points 2 et 4 ; rendre explicite l'absence de déclencheur chez les organismes verrouillés par renforcement (point 5).

## Réserves du lecteur

- 2604.28182 lu seulement par questions ciblées à un petit modèle (`WebFetch`), sur 100 000 caractères sur 118 306 pour la page HTML ; les figures 33 et 37 et la fin des annexes ne sont pas lues. Je n'écris donc pas qu'aucun modèle jamais verrouillé n'y est bruité ; la réponse ne l'écrit pas non plus.
- La note de piste v5 (« Correction de la fiche ») se trompe sur le § 4.2 selon deux lectures concordantes : l'organisme à 80,0 % est le conditionnel distillé du § 3.2. Sans effet sur la réponse, qui ne prête aucun score de départ.
- Page du flux de mentorat non relue (deux recherches web infructueuses) : l'énoncé de la direction « étiologie » vient du rapport et de la pièce.
- Pages de 2512.07810 : index du PDF empreinté (ici égal à la pagination imprimée aux p. 13, 19, 22, 71, 72).
- `curl` vers arXiv refusé par le mandataire (403) ; aucun outil n'a demandé d'approbation. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucun `git fetch`. Fichiers de travail temporaires : `/tmp/lecteur-mentor-jf-v5/` (textes extraits des deux PDF du dépôt).
