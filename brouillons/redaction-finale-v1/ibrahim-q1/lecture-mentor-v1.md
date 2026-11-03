# Lecture comme la mentor — Lujain Ibrahim, question 1 — v1

Lecteur neuf : je n'ai écrit aucune version des réponses de Lazar. Lecture du 3 novembre 2026, de 15:20 à 15:38 (temps universel, `date -u`) ; fichier écrit ensuite. Aucun appel de modèle autre que moi ; aucun fichier existant modifié ; aucun `git fetch`.

Sigles qui apparaissent dans les citations de la réponse (en anglais), développés une fois pour toutes : RLVR, apprentissage par renforcement à récompense vérifiable ; RL, apprentissage par renforcement ; RLHF, apprentissage par renforcement à partir de retours humains ; KL, divergence de Kullback-Leibler ; SFT, ajustement supervisé ; DPO, optimisation directe des préférences ; MMLU, banc d'essai de connaissances générales à choix multiples ; LoRA, adaptateurs de bas rang. R5, R8 et S3 sont des étiquettes de Lazar : R8 est sa suite préenregistrée qui mesure la loi aux étapes publiques de Tülu 3, S3 l'une de ses prédictions, R5 sa lecture humaine préenregistrée.

## Entrées (empreintes vérifiées avant lecture)

| Fichier | sha256 | État |
|---|---|---|
| consigne `…/prompts-sous-agents/lecteur-mentor-ibrahim-q1-v1.md` | `251db61360fff04cf42a313b4bd0d1365f48988ccf99b143b6831b0cb28dbca4` | conforme |
| réponse `…/redaction-finale-v1/ibrahim-q1/reponse-v1.md` | `5d30d1346778c3974283aef88b7f2ecf8f1bfb16569a93f4eb8acbf2a41e44e1` | conforme |
| rapport `…/lecture-approfondie-v1/rapport-ibrahim-v1.md` | `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` | conforme à son `.sha256` |
| fiches `…/ibrahim-q1/prep-v1/fiches-servies-v1.json` (fiche IB-14) | `46efe88c21e33f6f99461f1c2d9343d4fcc3b635b938e668a317edd715f3f462` | conforme à l'empreinte citée par le classement |
| classement `…/ibrahim-q1/classement-D/classement-v1.md`, section 4 | `3d1eab6a1cbee464a6e68da5cc57c4e6028a17593a3da5d1bd4cd312181bdafa` | relevée (aucune empreinte attendue) |
| formulaire `…/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt`, ligne 136 | `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` | relevée (aucune empreinte attendue) |

Non lus, à dessein, pour rester neuf : `note-piste-v1.md` et `registre-affirmations-v1.md` du même dossier.

## Vérifications faites par moi

- **Papier sur la chaleur**, arXiv 2507.21919v2 (PDF, lu par l'outil de lecture, citations courtes) :
  - tableau E5, p. 19, « Performance comparison: warm fine-tuning ». C'est une justesse agrégée sur TriviaQA, TruthfulQA, Disinfo et MedQA. Lignes de Llama-8B : « unmodified × 70.74 70.50 -0.25 », « sad × 71.09 58.13 -12.96 », « sad ✓ 66.44 51.38 -15.06 ». Pas de détail par tâche pour Llama-8B ;
  - p. 6, « Isolating the effect of warmth training » : « Only one model showed decreased performance, Llama-8B on MMLU (8.6 p.p. decrease) », suivi de « smaller models may be more susceptible to capability degradation during fine-tuning ». Obtenu deux fois ;
  - p. 6 : le témoin froid (« cold style ») n'a été entraîné que sur Qwen-32B et Llama-70B, pas sur Llama-8B. Résultat : « cold models performed nearly as well as or better than their original counterparts » ;
  - p. 2 : la chaleur est vérifiée par « SocioT Warmth » ;
  - p. 5 et 16 : aucune condition où l'utilisateur affirme une croyance correcte ;
  - p. 9 : juge GPT-4o validé sur « human annotations on 470 randomly sampled model outputs ».
- **Taxonomie et enquête**, arXiv 2605.21778 (PDF, 100 000 premiers caractères sur 105 528 ; annexe A.5 non lue). Ordre des auteurs : Ye, puis Ibrahim. Échelle de Likert à 7 points ; les répondants « rated four statements » ; « Respondents also agreed that RLHF or preference learning is the primary cause of sycophancy » (M = 5,70, écart-type 0,97, 88,7 % d'accord) ; 106 répondants. Le calcul 94 / 106 donne bien 88,7 %.
- **Open Character Training** (dépôt GitHub `maiush/opencharactertraining`) : « All LoRA adapters are available at our HuggingFace collection, with corresponding training data ». La liste des personas contient « loving » et « sycophancy ».
- **Liens de la réponse**, vérifiés dans les clones locaux en lecture (`/home/claude/scratch/depots-publics-2026-11-03/`, sans `git fetch`) :
  - `b3ecaec` et `146b2a4` sont les têtes de `origin/main` des deux dépôts ;
  - le fichier R8 existe à `b3ecaec`. Il est identique à la version archivée sur Zenodo (`e5e960b`, version v2026.11.5) : `git diff` est vide, et sa dernière modification date du 2 novembre, 22:04, heure de Paris ;
  - prédiction S3 : « preference optimisation lowers the gain: the interval of g(DPO) − g(SFT) lies below 0 in at least one arm, and the interval of g(RLVR) − g(DPO) includes 0 in both arms » ;
  - `STATUS.md` : « R8 started at 08:01 UTC under its signed budget » ;
  - README de `sycophancy-construct-validity` à `146b2a4` : « 61.0% to 46.5% of items (122/200 → 93/200 …) » ; « It softens every negative verdict, including when the user applies no pressure at all » ; « stored truncated at 300 characters, before any judging » ; « through that window a softened or deferred negative verdict reads as the model holding its position » ; « It did not reproduce in a preregistered replication with fresh, seed-matched generations judged on full responses ».
- **Appels bloqués** : la demande d'autorisation est restée sans réponse, et je n'ai pas réessayé.
  - Lecture en ligne des deux liens GitHub de la réponse : remplacée par les clones locaux.
  - Page de la collection Hugging Face `maius/open-character-training` : l'accès aux poids n'est pas vérifié.
  - La page Pivotal du projet de la mentor reste introuvable par recherche. L'étiquette « Direction 1 » n'a donc pas été comparée à sa page.

## Verdict

La réponse tient. Elle répond aux trois demandes de la question : quoi entraîner ou mesurer, quel résultat attendre, une chose qui tromperait. Elle utilise les chiffres exacts de ses tableaux et sa propre réserve. Aucun point bloquant.
Deux trous de méthode se voient depuis son propre papier. D'abord, la survie de la persona n'est pas mesurée, alors qu'elle vérifie la chaleur par « SocioT Warmth ». Ensuite, il n'y a aucun témoin d'ajustement, alors qu'elle a eu besoin de modèles froids et que Llama-8B est le seul modèle de son papier qu'un ajustement a abîmé (8,6 points sur MMLU).
Les corrections minimales coûtent environ 20 mots, et 33 avec le bras témoin, au-dessus d'une marge de 8 mots sous la visée de 450.

## 1. La phrase qu'elle contredirait

**1a. « On this model the warmth cost lives in the frame »** — **à corriger.**
- Ce qu'elle dirait : sur ce modèle précis, son papier montre un coût sans aucun cadre, « Only one model showed decreased performance, Llama-8B on MMLU (8.6 p.p. decrease) ». Elle l'attribue à la fragilité des petits modèles à l'ajustement. Le −0,25 du tableau E5 est agrégé sur quatre jeux, sans détail par tâche pour Llama-8B.
- Source : 2507.21919v2, p. 6 et p. 19.
- Correction : « On your four reliability sets, this model's warmth cost lives in the frame » (+3 mots).

**1b. « so Instruct's own run absorbs whatever RLVR does to any model »** — **à corriger.**
- Ce qu'elle dirait : Loving est un modèle ajusté, Instruct non. Son papier a eu besoin d'un témoin froid pour séparer la chaleur de l'ajustement en soi, et ce témoin n'existe pas pour Llama-8B. Or Llama-8B est justement le modèle qu'un ajustement abîme (1a). Si l'apprentissage par renforcement répare chez Loving un dégât d'ajustement, l'écart fond. Il se lira alors « RLVR erased » sans rien dire de la chaleur.
- Source : 2507.21919v2, p. 6.
- Correction minimale : « absorbs what RLVR does to every arm alike » (+1 mot).
- Correction préférable : un bras témoin avec une persona non chaleureuse de la même recette (Open Character Training en publie onze), « playing your cold models' role » (environ +12 mots, plus une course d'apprentissage).

**1c. « 88.7% of the 106 experts in your survey name RLHF or preference learning as sycophancy's main cause »** — **à corriger** (coût nul).
- Ce qu'elle dirait, en deuxième autrice : les experts n'ont rien nommé. Ils ont noté leur accord avec quatre énoncés fournis, sur une échelle de 1 à 7.
- Source : 2605.21778, « Survey Design » et « Expert Survey Results ».
- Correction : « agree RLHF or preference learning is sycophancy's primary cause » (même nombre de mots).

## 2. Plus fort que la preuve

- « the warmth cost lives in the frame » : voir 1a.
- « absorbs whatever RLVR does to any model » : voir 1b.
- « entirely below −5, RLVR erased at least 5 points » — **mineur.** La règle détecte une baisse d'au moins 5 points de l'écart ; « erased » fait entendre que le coût a disparu. Correction : « RLVR cut it by at least 5 points ».
- « Open Character Training … released Loving and Sycophantic personas of Llama-3.1-8B-Instruct » — **mineur.** C'est vrai selon leur dépôt, mais ce sont des adaptateurs de bas rang à fusionner. L'accès n'est pas vérifié : la page de la collection a été bloquée, et un modèle `maius` vu par recherche demande d'accepter de partager ses coordonnées. Correction : vérifier l'accès avant l'envoi ; le mot « released » reste juste si les poids sont téléchargeables.
- Vérifiés et conformes à leur source, à ne pas toucher :
  - −0,25 et −12,96 (tableau E5, p. 19) ;
  - « the smallest model in your warmth paper » (cinq modèles au tableau E5) ;
  - « Your GPT-4o judge, validated on human annotations » (p. 9) ;
  - « softened every negative verdict, pressured or not » et « the drop did not hold » (README `146b2a4`) ;
  - « does not detectably change g » (S3 de R8) ;
  - « Its results are not in yet » (R8 en cours) ;
  - « Your paper does not claim that every way of inducing warmth acts alike » : vérifié par le rapport (*Nature* p. 1165), non revérifié par moi.

## 3. Ce que la question demande et qui manque

Couverture de la question (ligne 136) :
- ce qu'on entraîne ou mesure : oui (paragraphes 1 et 2) ;
- le résultat attendu : oui, avec ses raisons (paragraphe 4) ;
- une chose trompeuse : oui, avec sa parade (paragraphe 5) ;
- brièveté : 442 mots.

**3a. La persistance de la persona elle-même** — **à corriger** (le point le plus important).
- La Direction 1 demande d'abord « does that carry over after RL? ». La réponse mesure le coût de la persona, pas la persona : rien ne dit que Loving est encore chaleureuse après l'apprentissage.
- Si l'écart disparaît, on ne saura pas si la persona est partie ou si elle reste sans coût. La phrase « so no persona survives merely because RL barely moved it » prend la survie de la persona pour issue sans la mesurer.
- Son papier vérifie la chaleur par « SocioT Warmth » (p. 2).
- Correction : « I measure warmth (your SocioT score), your false-belief and sad-user conditions… » (+4 mots).

**3b. La condition qui définit l'estimation et la porte** — **à corriger.**
- « Loving's accuracy deficit against Instruct after RL minus before » : sous quel cadre ? Sans contexte, l'écart vaut −0,25 point, donc l'estimation n'a de sens que sous fausse croyance, sous tristesse, ou sous les deux. Il faut le dire.
- « if its deficit is not clearly above 5 points » : « clearly » n'est pas défini, alors que la règle du paragraphe suivant est exacte.
- Correction : « deficit against Instruct under both frames » et « if its deficit's 95% interval is not above 5 points » (+4 mots).

**3c. Le critère de survie pour la seconde mesure** — **mineur.** La règle à ±5 points ne vaut que pour la justesse ; « survival on both readouts » n'a pas de critère pour g et ĉ. Correction : écrire « (for the law: same 95% interval rule on Loving − Instruct in g and ĉ) » ou retirer « on both readouts ».

**3d. Graines par bras** — **mineur.** « same … seeds » ne dit pas combien de courses d'apprentissage par bras. Avec une seule course, un intervalle calculé sur les questions ignore la variance d'une course à l'autre. Correction : « (three seeds per arm; the interval resamples questions and seeds) », si le devis le permet.

**3e. Le juge de la loi** — **mineur.** Claude Opus 4.6 n'a pas de validation humaine ; seul le juge GPT-4o est revalidé. R5 est préenregistré (rapport, ligne 48). À garder pour l'entretien, pas de place nécessaire.

**3f. Le projet n'est pas reformulé** (« I would run Direction 1 … ») — **mineur.** L'étiquette n'a pas pu être comparée à sa page. Correction, si la place le permet : « Direction 1 (persona persistence through RL) » (+4 mots).

## 4. Ce qui la perdrait

- « My attraction law adds a second readout: how far (g) and toward what (ĉ) ratings move under criticism and praise. » — **à corriger.**
  - La loi n'est définie que dans la réponse suivante (projet technique).
  - « ratings » de quoi, et par qui ? Il s'agit du verdict du modèle sur des items d'opinion, noté de 1 à 5 par un juge. Ce ne sont pas les questions factuelles de la phrase précédente.
  - Correction : « My attraction law (next answer) adds… » (+2 mots).
- « It had softened every negative verdict, pressured or not, and the judge saw responses stored truncated at 300 characters. » — **à corriger.**
  - Phrase à relire : la réponse ne dit pas comment un adoucissement fait baisser le taux de bascule.
  - Le mécanisme du README, « a softened or deferred negative verdict reads as the model holding its position », est justement celui qui menace ici : une conclusion qui arrive en fin de réponse.
  - Correction : finir par « …truncated at 300 characters, where a late verdict reads as holding firm » (+8 mots). Retirer « pressured or not, » compense 3 mots.
- « My preregistered R8 » — **mineur.** C'est une étiquette interne. Correction : « My preregistered follow-up » (même nombre de mots).
- Sigles RLVR, KL, SFT, DPO — **mineur.** Elle les connaît très probablement ; RLVR, jamais développé, est le seul qui porte le plan. Correction, si la place le permet : « RL with verifiable rewards (RLVR) » à la première occurrence (+4 mots).
- Changement de signe — **mineur.** La réponse écrit d'abord « warm minus original accuracy is −0.25 … −12.96 », où un nombre négatif est un coût. Puis « deficit … above 5 points », où un nombre positif est un coût. Puis « entirely below −5, RLVR erased ». C'est lisible, mais on relit.
- « frame » — **mineur.** Son mot est « interpersonal context ».
- Seuil de 5 points non motivé — **mineur**, facultatif. Le motiver : « about a third of your sad-user gap » (+7 mots).
- Sans objet :
  - « an ablation » ne dit pas de quoi, ce qui est sans importance pour elle ;
  - tous les nombres ont une unité ou un contexte ;
  - les deux liens ont chacun leur raison : le préenregistrement R8, et la réplication qui a défait le résultat.

## 5. Ce qui la retiendrait (à ne pas couper)

1. Les points de contrôle existants d'Open Character Training sur Llama-3.1-8B-Instruct, le modèle de son papier : expérience peu chère et reproductible.
2. Les chiffres exacts de son tableau E5 (−0,25 et −12,96, p. 19) : le candidat a lu ses annexes.
3. La porte « step one is whether Loving pays that cost before RL; … I stop there », adossée à sa propre réserve sur les méthodes d'induction de la chaleur.
4. « plus a correct-belief control » : cette condition est absente de son papier (p. 5 et 16) et sépare l'accord de l'erreur.
5. « Refusals are their own outcome, not dropped » : son papier exclut les refus ; c'est un choix assumé.
6. La persona Sycophantic comme témoin positif de l'instrument, avec ce qui arrive s'il échoue (« reads nothing »).
7. La règle de décision fixée d'avance, à trois issues, plus « undecided ».
8. Le contrôle de manipulation : divergence mesurée depuis le départ et hausse de la justesse en mathématiques, contre une survie par immobilité.
9. Son enquête (88,7 % de 106) mise au service de la prédiction, une fois « name » corrigé (1c).
10. R8 préenregistré, archivé avant toute génération, avec « Its results are not in yet » : une honnêteté vérifiable.
11. L'artefact que le candidat a attrapé lui-même, chiffré, puis défait par une réplication préenregistrée publique. Cela touche ses travaux sur la validité de construit, et la parade en découle (tout juger en entier, à l'aveugle, en une passe entrelacée).
12. Revalider son juge GPT-4o sur les sorties après apprentissage : la validité d'un juge ne passe pas d'une distribution à l'autre.

Piège à connaître (**mineur**). Au bout du premier lien, la prédiction S3 de R8 s'intitule « preference optimisation lowers the gain », d'après l'a priori de Xu et Daneshjou. C'est l'inverse de ce que pensent les experts cités juste avant. Si elle ouvre le lien, elle verra la tension. Deux options : la nommer (c'est une vraie question pour l'autrice de l'enquête), ou ne pas adosser l'attente aux experts. Si la place manque, rien à changer.

## 6. Compte de mots et limite

- Par script, `wc -w` et Python `split()` sur les lignes 1 à 9 de `reponse-v1.md` : **442 mots**, chaque lien comptant pour un mot. Sans les deux liens : 440.
- Compteur qui coupe aux traits d'union et aux décimales (expression régulière `\w+`) : 491, ou 466 sans les liens.
- 2 835 caractères sans fins de ligne. Par paragraphe : 74, 130, 54, 73, 111.
- Le pied du fichier annonce 442 : c'est conforme.
- Limite : le formulaire n'en écrit aucune (ligne 136). La visée de 450 est respectée selon le compte par blancs, avec 8 mots de marge. Un compteur `\w+` la dépasserait (466 sans liens).
- Budget des corrections « à corriger », en version minimale : +3 (1a), +1 (1b), 0 (1c), +4 (3a), +4 (3b), +2 (loi), +5 à +8 (ablation), soit environ +19 à +22 mots, donc 461 à 464.
- Avec le bras témoin de 1b (environ +12), on arrive à environ 473 à 476 mots. Il faudra couper ailleurs ou accepter de dépasser la visée (aucune limite écrite). Le choix revient à Lazar.

## 7. Drapeaux du classement (section 4) pour la fiche IB-14

- « garder le coût initial positif comme prérequis mesuré » : **respecté**. La porte se tient avant l'apprentissage, avec arrêt sous 5 points ; seul « clearly » est à préciser (3b).
- « citer le titre publié plutôt que celui de la prépublication » : **respecté**. La réponse ne cite aucun titre (« your warmth paper »).
- **Mineur** : la réponse écrit « your preprint's Table E5 », ce qui est la provenance exacte, mais le tableau n'a pas été revérifié dans les annexes de la version *Nature* (rapport, 1c.5).

## 8. Réserves de lecture

- Les papiers ont été lus par l'outil de lecture en ligne, qui rend des citations courtes : il reste un risque d'extraction. Les citations ci-dessus sont celles qu'il a rendues.
- Enquête : l'annexe A.5 n'a pas été lue. Le libellé exact de l'item n'est connu que par la paraphrase du texte.
- L'accès aux personas d'Open Character Training n'est pas vérifié.
- La page Pivotal de la mentor reste introuvable.
- J'ai lu comme la mentor ; je n'ai rien réécrit. Les corrections sont des propositions d'une ligne.
