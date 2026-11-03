# Vérification des phrases modifiées — réponse v6 à Shi Feng et Eyon Jang — v1

Vérificateur neuf, mardi 3 novembre 2026, de 18:07:56 à 18:15 UTC environ (`date -u`). Je n'ai écrit aucune version des réponses de Lazar Ciric, ni aucun registre, ni aucune vérification. Je n'ai ouvert aucune réponse de numéro 1 à 4 de ce dossier ; j'ai lu la v5 (pour recalculer l'écart) et les deux rapports sur la v5.

Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-jang-feng-v6-v1.md`, sha256 `661c528d7062dd677e69a0bbd988357869864317841118223d21ed0a28e73439` (vérifiée).

## Pièces et sources

| abréviation | fichier ou page | empreinte, moyen |
|---|---|---|
| [LISTE] | `brouillons/redaction-finale-v1/phrases-modifiees-jang-feng-v6.md` | sha256 `a9bc465f0242358644b0676b4258a8a8e326611980b070dce87cf63f91878723` (vérifiée) |
| [V6] | `…/jang-feng/reponse-v6.md` | sha256 `78cabf74b48b4e45db5e28da733fc2bbd3e02a3eab8685d8dac9dcf0dda6a36e` (vérifiée, et par son `.sha256`) ; corps au-dessus du trait, fin de ligne comprise : `2e883e79a0dd5176e44a29b09b7fccc5bb8acb8b4fe85a069a4c393cd69f8fa3` |
| [V5] | `…/jang-feng/reponse-v5.md` | sha256 `e075bd8b48733dc44866abfe22caf170e9fe388802837f8bb2df6fc3c471cac5` (vérifiée par son `.sha256`) |
| [CHIF5], [MENT5] | `…/jang-feng/verification-chiffres-v5.md`, `…/jang-feng/lecture-mentor-v5.md` | `4618ed030edad5d45aa3f7d3c02cdd2a048adfbb2b7d8a1a298b3deeb3f8cb29`, `7584a07c286ca7bffeea2bd14f22f9ead26a99940b435cc69db9104a7a3bec5a` (vérifiées par leurs `.sha256`) |
| [TAY] | Taylor et coll., « Auditing Games for Sandbagging », arXiv 2512.07810 v1, `docs/sources/pdf/2512.07810v1.pdf` | `.sha256` compagnon : OK ; texte extrait par moi (`pdftotext`), pages 1, 3, 4, 8, 22, 71 lues ; pages = index du PDF |
| [TICE] | Tice et coll., arXiv 2412.01784 v3, `docs/sources/pdf/2412.01784v3.pdf` | `.sha256` compagnon : OK ; page 9 lue |
| [JANG] | Jang et coll., « Exploration Hacking », arXiv 2604.28182 v1, page HTML | `WebFetch` par moi : trois questions sur les caractères 0 à 100 000, une sur 100 000 à 118 306 (annexes B.2, B.3). Transcription par un petit modèle : vérifiée, **non opposable au sens de R7** ; aucune figure lue |
| [P3] | `lciric/ideation-organism`, `resultats/controle-p3-premier-test/README.md` au commit `7c7b688` | `git show` dans le clone `/home/claude/ideation-organism` (aucun `git fetch`) ; sha256 du fichier `2485d5095094c2dc7f761cbe972172c88291305c6da1df50b58c0c3c1272bf88`, identique à `faff48b` ; page publique chargée sans connexion (`WebFetch`), chiffres identiques |
| [README] | même dépôt, `README.md` au commit `7c7b688`, ligne 127 | `git show` |
| [SCV] | `lciric/sycophancy-construct-validity`, `README.md` au commit `146b2a4` (celui que cite la réponse à Heimersheim, question 2) | clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity`, `git show` |
| [AUTRES] | huit réponses finales : `kirchner-q1/reponse-v3.md` `3592a009…`, `kirchner-q2/reponse-v3.md` `4611a645…`, `ibrahim-q1/reponse-v4.md` `a1646baa…`, `ibrahim-q2/reponse-v3.md` `1aece077…`, `heimersheim-q2/reponse-v3.md` `b0557977…`, `scheurer/reponse-v3.md` `d4eb67c5…`, `colognese-ward-q1/reponse-v3.md` `5e25e472…`, `colognese-ward-q2/reponse-v3.md` `faa02321…` | chacune vérifiée par son `.sha256` (8 sur 8 : OK) ; texte au-dessus du trait |

## Complétude de la liste

Écart recalculé par moi, phrase à phrase, entre le corps de [V5] et celui de [V6] : 10 phrases nouvelles (la liste en compte 11 parce qu'elle coupe « (Fig. 34) » en deux) ; elles sont toutes dans [LISTE], et [LISTE] n'en contient aucune qui ne soit pas dans [V6]. Rien n'a changé hors de la liste.

## Tableau des phrases « + »

| n° | phrase « + » ou partie | source et emplacement | verdict |
|---|---|---|---|
| 1 | « In the auditing game (Taylor et al., arXiv 2512.07810) » | [TAY] p. 1 : Jordan Taylor premier auteur, 13 auteurs, 8 décembre 2025 | **exact** |
| 2 | « imitating a weaker model beat black-box detection » | [TAY] p. 1 (« Black-box approaches were defeated by effective imitation of a weaker model ») ; p. 3, constat 1 | **exact** |
| 3 | « probes did better » (ajout) | [TAY] p. 3, constat 2 : sondes linéaires « significantly more effective than black-box approaches » ; p. 3, résultats du jeu : les sondes de tromperie ont signalé à raison un modèle | **exact** (nuance : les sondes n'auraient pas attrapé Oak, p. 22 ; la phrase ne dit pas le contraire) |
| 4 | « but were misled by decoys » (ajout) | [TAY] p. 3-4, constat 2 : « distractor behaviours such as double negatives which caused false positives for probes » ; p. 3 : « false positives due to distractor behaviours » | **exact** (« decoys » rend « distractor behaviours ») |
| 5 | « training on a single correct demonstration elicited full performance from the (password-locked) sandbaggers » | [TAY] p. 1 ; p. 4, constat 3 (« successful at fully eliciting all sandbagging models ») ; p. 8 (« Sandbagging model organisms were password-locked ») ; p. 4, limite (« Password-locked models may be easier to elicit ») | **exact** |
| 6 | « On fine-tuned locks » | [TAY] p. 4 : « Both sandbagging model organisms were fine-tuned from a single base model » ; [JANG] § 3.2 : organisme conditionnel WMDP fait par « the same two-stage SFT distillation technique », celui du § 4.2 | **exact** (transcription pour Jang) |
| 7 | « with full demonstrations, that justifies weight access » | [TAY] p. 4 (une démonstration correcte complète) ; [JANG] § 4.2 : « verify as a sense check that SFT on full benign traces does quickly recover suppressed capabilities » | **exact** (la phrase restreint la portée ; « justifies » : opinion) |
| 8 | « That compares the same weights with and without trigger » | [JANG] § 4.1 : « We evaluate each perturbed adapter on BigCodeBench with trigger present (treatment) and absent (control) » | **exact** (transcription) |
| 9 | « which start at different scores » | [JANG] § 3.2 : « The locked model without trigger retains this performance [~65 %], while with trigger present it passes only ~20% » | **exact** (transcription ; nuance : le texte ne donne pas les valeurs à σ = 0 du balayage, qui viennent du jeu de test tenu à part du § 3.2 ; la figure 7 n'est pas lue) |
| 10 | « RL-locked organisms (§3.1) have no trigger to remove » | [JANG] § 3.1 : « There is no password or trigger phrase that unlocks their true performance » ; « We use "RL locking" » ; aucun organisme conditionnel au § 3.1 | **exact** (transcription) |
| 11 | « the comparison that validates the method, before any audit » | [TICE] p. 9 : comparaison à des modèles non saboteurs « which would be unavailable in real-world applications » | opinion, cohérente avec sa source (hors décompte) |
| 12 | « The improvement ratio ξ used after the auditing game » | [TAY] p. 22, § 6.5.2 : « After the game, we investigated whether injecting noise into model weights… » ; p. 3, fig. 2 : techniques « only investigated after the game » | **exact** (la correction facultative de [CHIF5] est appliquée) |
| 13 | « is a maximum over noise levels and seeds, and a maximum can only grow as draws are added, so a model hiding nothing can score above 1 » | [TAY] p. 71, annexe C.15 (maximum sur σ et graines, divisé par la moyenne sans bruit) ; [TICE] p. 9 (« performance continues to increase as we sample from a greater number of seeds ») ; [TAY] p. 22 (ξ = 1,038 ± 0,076 sur les tâches non sabotées) | **exact** |
| 14 | « Their unlocked conditions reach ξ = 1.26 (Fig. 34) » | [TAY] p. 71, fig. 34 : Oak sur Tic Tac Toe, « ξ (password unlocked)=1.26 », le plus haut des 16 panneaux déverrouillés (puis 1,20 ; 1,17 ; 1,16 ; 1,15) | **exact** (réserve mineure : « Their » n'a pas d'antécédent nommé, et le paragraphe précédent finit sur le papier de Jang, qui a lui aussi des figures d'annexe numérotées au-delà de 30) |
| 15 | « In my first preregistered test on real activations » | [P3] l. 1 : « first white-box test on real activations (control programme) » ; l. 3 : « first white-box test of the AI-control programme » ; [README] l. 127 : « (P3, control programme) ». Or [SCV] (dépôt public cité par la réponse à Heimersheim) : réplication **préenregistrée** de l'ablation de rang 3 sur Llama-3.1-8B-Instruct (juillet 2026) et test de remplacement du flux résiduel D36, préenregistré le 29 juillet 2026 | **plus fort que sa source** : la source borne « premier » au programme de contrôle ; Lazar a des tests préenregistrés sur des activations réelles antérieurs au 19 octobre |
| 16 | « the deception probe's interval cleared chance (lower bound 0.53) » | [P3] l. 14 : sonde « deception », intervalle à 97,5 % [0,5313 ; 0,6183] | **exact** |
| 17 | « but not the 0.95 quantile of 200 covariance-matched random probes (0.57) » | [P3] l. 14 (0,5717) et l. 50 (200 sondes tirées de N(0, Σ), Σ la covariance des jetons d'entraînement) ; [README] l. 127 (« 200 random probes matched in covariance ») | **exact** |
| 18 | « not detected at this power » | [P3] l. 7 et l. 10 | **exact** (mot pour mot) |
| 19 | « and the null does not exclude AUCs below 0.63 » | [P3] l. 30 (réserve 2) et l. 82 : 0,6315 | **exact** (la réserve exigée par le verdict est portée) |
| 20 | lien `https://github.com/lciric/ideation-organism/blob/7c7b688/resultats/controle-p3-premier-test/README.md` | clone : commit `7c7b688` présent, ancêtre de `faff48b`, fichier présent, empreinte identique aux deux commits ; page publique servie sans connexion | **exact** |
| 21 | « with both Qwen3-14B recipes of Eyon's paper » | [JANG] annexe B.2 : « Base model: Qwen3-14B with a rank-32 LoRA adapter » (verrouillage par renforcement) ; annexe B.3 : « We fine-tune a base model (Qwen3-14B) », « LoRA rank: 32 » (distillation) | **exact** (transcription) |
| 22 | « (the base trained on a weaker model's honest attempts, same adapter rank) » | même source : les deux recettes portent un adaptateur de bas rang (LoRA) de rang 32, donc « same adapter rank » a un sens pour les deux ; le reste est le plan | **exact** pour « same adapter rank » (transcription ; lève le doute de [MENT5] § 4 sur l'adaptateur des organismes verrouillés par renforcement) ; le reste : plan, voir réserve 3 |
| 23 | « So weight access is a strong elicitation tool » | [TAY] p. 4, constat 3 ; [JANG] § 4.2 | **exact** comme appui d'une opinion |
| 24 | « and white-box perturbation, so far, an unvalidated detector of intent » | [TAY] p. 22 : « unreliable and does not distinguish sandbagging from benign underelicitation » ; [JANG] § 6.1 : « a promising white-box detection technique » (prometteur n'est pas validé : pas de contradiction) | **exact** comme appui d'une opinion |

Hors décompte (opinions, dites comme telles ou par leur forme) : la thèse « Weight access is best at getting a hidden capability back, and least proven at telling why it was hidden » (appuyée par [TAY] p. 4, constat 3 : « Removing sandbagging is not the same as detecting it ») ; n° 11 ; « the null is a score-matched benign model through the same grid » (réserve 2) ; « evidence only against a matched benign control ».

## Réserves (sans correction exigée)

1. **« Their unlocked conditions » (n° 14).** Juste sur le fond, mais « Their » renvoie implicitement à Taylor et coll., nommés deux paragraphes plus haut, alors que la phrase précédente du paragraphe 3 parle du papier de Jang. Un lecteur pressé peut chercher la figure 34 chez Jang.
2. **« the null is a score-matched benign model through the same grid ».** Proposition de Lazar dite à l'indicatif, sans source ; juste après « Their unlocked conditions… », elle peut se lire comme une description du nul de Taylor et coll., qui comparent en fait les mêmes poids avec et sans mot de passe (p. 71, annexe C.15). Pas d'homme de paille nommé (le « not 1.0 » de la v5 est retiré).
3. **Témoin « jamais verrouillé » (plan).** « The base trained on a weaker model's honest attempts » est la recette de Cedar chez Taylor et coll. sans le mot de passe (p. 3, constat 1 : « trained to imitate an actual weaker model's outputs ») ; l'objection 1.c de [MENT5] (un verrou inconditionnel par une autre recette) n'est que partiellement levée : « honest » porte seul la différence ; la précision proposée par [MENT5], « with no reasoning about underperforming », n'est pas reprise.
4. **Transcriptions.** Les verdicts n° 6, 8, 9, 10, 21 et 22 reposent sur des lectures de la page HTML de 2604.28182 par `WebFetch` (petit modèle), non opposables au sens de R7 ; aucun PDF empreinté de ce papier dans `docs/sources/pdf/`.

## Cohérence avec les autres réponses finales

- **P3 (0,53 ; 0,57 ; 0,63 ; 200 sondes aléatoires appariées en covariance)** : aucune des huit autres réponses ne le cite (recherche de « 0.53 », « 0.57 », « 0.63 », « P3 », « controle-p3 », « random probe », « covariance », « deception probe », « real activations », « first preregistered » : aucun résultat). Pas d'écart de nombres, de portée ni de statut possible ; les nombres de la v6 sont ceux de [P3] et de [README].
- **Portée du mot « first »** (n° 15) : la réponse à Heimersheim (question 2) cite `sycophancy-construct-validity` au commit `146b2a4`, dont la page publique décrit une réplication préenregistrée (juillet 2026) et un test D36 préenregistré (29 juillet 2026), tous deux sur les activations de Llama-3.1-8B-Instruct. « My first preregistered test on real activations » est donc incohérent avec ce que le dossier montre ailleurs. Seule incohérence trouvée.
- **Liens** : la v6 épingle `ideation-organism` à `7c7b688` ; les réponses à Kirchner (questions 1 et 2) et à Scheurer épinglent le même dépôt à `faff48b`. Même dépôt, deux commits, tous deux présents ; le fichier de P3 est identique aux deux (même empreinte) et `7c7b688` est le commit qui publie P3. Pas d'incohérence de contenu ; rien à changer.
- Aucune autre réponse ne cite Taylor et coll., Tice et coll. ni Jang et coll. ; rien à confronter.

## Traces de résultats internes

Aucune dans le corps de la v6 : ni « nul v9 », ni validation du nul, ni « pooled », ni « 1,000 », ni résultat non publié. Le seul résultat de Lazar cité est P3, public au commit cité.

## Compte de mots

Corps au-dessus du trait, découpage sur les blancs (`python3 -I`, `len(corps.split())`) : **500 mots** (3 226 caractères, fin de ligne comprise), comme le pied ; par paragraphe : 19, 70, 139, 112, 135, 25 ; un lien, compté un mot. La visée « 500 au plus » est tenue, sans marge.

## Problèmes et corrections minimales

1. **n° 15, plus fort que sa source (à corriger)** : « In my first preregistered test on real activations » → « In my control programme's first preregistered test on real activations » (502 mots) ; à mots constants : « In my control programme's first preregistered activation test » (500 mots).
2. Réserve 1 (facultatif) : « Their unlocked conditions » → « Taylor et al.'s unlocked conditions » (+2 mots).
3. Réserve 2 (facultatif) : « the null is a score-matched benign model » → « the null should be a score-matched benign model » (+1 mot).
4. Réserve 3 (facultatif, plan) : ajouter « with no reasoning about underperforming » après « honest attempts » (+5 mots), ou laisser.

## Décompte par verdict (24 affirmations factuelles dans les phrases « + »)

- exact : **23** (dont 6 par transcription non opposable : n° 6, 8, 9, 10, 21, 22 ; nuances : n° 3, 9, 14)
- inexact : **0**
- non vérifiable : **0**
- plus fort que sa source : **1** (n° 15)
- liens : 1 sur 1, même dépôt, commit `7c7b688` présent, fichier présent dans le clone, page publique.
- hors décompte : 4 opinions et le plan.

## Réserves du vérificateur

- 2604.28182 lu seulement par questions ciblées à `WebFetch` ; figures 7, 33 et 37 non lues.
- `curl` non essayé ; aucun outil n'a demandé d'approbation. Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucun `git fetch`, aucun code des dépôts exécuté. Fichiers de travail temporaires : `/tmp/verif-jf-v6/` (textes extraits des PDF du dépôt).
