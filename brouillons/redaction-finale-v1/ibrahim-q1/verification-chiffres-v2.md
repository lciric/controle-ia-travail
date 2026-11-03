# Vérification des chiffres — réponse à Lujain Ibrahim, question 1 — v2

Vérificateur neuf : je n'ai écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Travail du 3 novembre 2026, de 15:48:25 à environ 16:10 en temps universel coordonné (UTC, `date -u`).
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-chiffres-ibrahim-q1-v2.md`, sha256 `5e6876f9c179a19eb46419eae52cf3a839514a675017c593b245a63d0a208a07`, vérifiée.

Fichier vérifié : `brouillons/redaction-finale-v1/ibrahim-q1/reponse-v2.md`, sha256 `f32232449fe9ce0857779185af23e6ede915bc928a0966d2885feee3541d61b5`, vérifiée. Question de la mentore : formulaire collé par Lazar, ligne 136.
Périmètre : chaque nombre, citation, nom de papier, date, lien et affirmation factuelle. Les plans, prédictions, règles de lecture et opinions ne sont pas comptés.

Abréviations développées une fois : apprentissage par renforcement (RL) ; apprentissage par renforcement à récompenses vérifiables (RLVR) ; ajustement supervisé (SFT) ; optimisation directe des préférences (DPO) ; MMLU, banc d'essai de connaissances générales (Massive Multitask Language Understanding).

## 0. Sources lues, et limites

| repère | source | version et empreinte | lecture |
|---|---|---|---|
| [form] | `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` | sha256 `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` | l. 135–161 |
| [loi] | clone `scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` | commit `b3ecaec` ; `main` distant identique (`git ls-remote`, vers 16:00 UTC) | `README.md` `304f486113b908ed…` ; `STATUS.md` `b0ed2c9802e4c9d1…` ; `results/R4/README.md` `2664d85cb9d3e335…` ; `results/R6/README.md` `27ad89efb844830d…` ; addendum R8 `68e891921055938a…` (identique à `e5e960b`, étiquette `v2026.11.5`) |
| [chaleur] | Ibrahim, Hafner, Rocher, *Training language models to be warm and empathetic makes them less reliable and more sycophantic*, arXiv 2507.21919v2 | format de document portable par WebFetch, quatre questions ciblées | pages citées ligne par ligne |
| [OCT] | Maiya, Bartsch, Lambert, Hubinger, *Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI*, arXiv 2511.01689v1 | format de document portable (deux tranches, 0–100 000 et 100 000–109 893 caractères) et page web, par WebFetch | sections citées |
| [HF] | Hugging Face : collection `maius/open-character-training` ; dépôt `maius/llama-3.1-8b-it-personas` et son arborescence | pages lues par WebFetch | — |
| [taxo] | Ye, Ibrahim et al., *What Counts as AI Sycophancy? A Taxonomy and Expert Survey of a Fragmented Construct*, arXiv 2605.21778v1 | page de résumé, page web, format de document portable, par WebFetch | sections citées |
| [Tülu] | Lambert et al., *Tülu 3*, arXiv 2411.15124 | page de résumé et format de document portable, par WebFetch | §2.3, tableau 1 |
| [Zen] | notice Zenodo 10.5281/zenodo.23909891 | page lue par WebFetch | — |
| [Fable] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` | sha256 `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` | entier |
| [recoup] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` | sha256 `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` | entier |
| [rapport] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` | sha256 `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` | entier |
| [note] | `brouillons/redaction-finale-v1/ibrahim-q1/note-piste-v2.md` | sha256 `0a1eb8eacc9d451d6c9648b3c526dc335192097fc750e1dde54be4b25bca1e26`, vérifiée | entier |
| [pièce] | `brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` | sha256 `4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149` | entier |
| [classD] | `scratch/soir-rapport/ibrahim-q1-ensemble/classement-D/classement-v1.md` | sha256 `d51d167150db6727ab8cf3b885f52f739669f06d268bc2d6ed263a62321e9ec2` | entier, dont « Drapeaux de risque devant la mentore » |

**Limites.**
- Tous les chiffres des papiers sont au niveau « transcription » au sens de R7 : WebFetch passe par un modèle intermédiaire. J'ai voulu télécharger les trois papiers pour les empreinter : le mandataire de sortie a refusé `curl` vers `arxiv.org` (403, `connect_rejected`). Aucun format de document portable n'est donc empreinté. Les pages imprimées du tableau 1 d'Open Character Training et de la phrase de la taxonomie ne sont pas lisibles par l'outil.
- L'interface de programmation de GitHub est filtrée pour cette session. Le caractère public du lien a été vérifié par WebFetch (page servie à un visiteur non connecté) et par `git ls-remote`. Aucun code des dépôts n'a été exécuté ; aucun `git fetch`.
- La page Pivotal de la mentore n'a pas été trouvée (deux recherches web).
- Registres du rédacteur : voir la réserve 9.

## 1. Tableau des affirmations

| n° | phrase exacte | source et emplacement | verdict |
|---|---|---|---|
| 1 | « I pick Direction 1: does a character-trained persona survive RL, and what does that do to sycophancy? » | [form] l. 138, dans le texte de Lazar et non dans la question : « Direction 1: You imprint a persona through character training, does that carry over after RL? If yes, how does that impact sycophancy? ». La question (l. 136) dit seulement « Pick one of the two projects ». Page Pivotal de la mentore introuvable ; même constat dans [rapport] l. 22 et [pièce] l. 84 | **non vérifiable** (l'étiquette et l'énoncé ne se comparent qu'aux notes de Lazar ; la reformulation leur est fidèle) |
| 2 | « Your taxonomy paper » | [taxo] page de résumé : Meryl Ye, **Lujain Ibrahim** (2e sur 8), Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje ; v1 du 20 mai 2026, seule version | exact |
| 3 | « notes that benchmarks built for factual capitulation cannot detect implicit framing » | [taxo] Introduction, paragraphe « Construct fragmentation occurs when… » : « As a result, benchmarks built to detect sycophancy as factual capitulation cannot detect sycophancy as implicit framing bias. » La page de résumé ne le dit pas | exact (condensé fidèle) |
| 4 | « the Loving and Sycophantic personas that Open Character Training » | [OCT] tableau 1 (§2.2) : 11 personas, dont Loving et Sycophantic | exact |
| 5 | « released for Llama-3.1-8B-Instruct » | [OCT] §2.4 « Public Release » : adaptateurs fusionnés publiés « on HuggingFace for each model », pour chaque persona du tableau 1 ; Introduction : « publicly release all model checkpoints and training data on HuggingFace » ; « For all three models, we use instruction-tuned releases » (Llama 3.1 8B, Qwen 2.5 7B, Gemma 3 4B). [HF] `maius/llama-3.1-8b-it-personas` : adaptateurs de rang faible pour dix personas, dossiers `loving` et `sycophancy`, modèle de départ `meta-llama/Llama-3.1-8B-Instruct`, aucune barrière d'accès affichée | exact (nuance : la déclaration éthique dit « we gate access to weights » ; téléchargement non essayé ; le dossier s'appelle `sycophancy`) |
| 6 | « a model of your warmth paper » | [chaleur] p. 2 : « (Llama-3.1-8B-Instruct, Mistral-Small-Instruct-2409, Qwen-2.5-32B-Instruct, Llama-3.1-70B-Instruct, and GPT-4o-2024-08-06) » ; Ibrahim 1re autrice | exact |
| 7 | « and of my attraction law » | [loi] README l. 1 (titre « Sycophancy as Attraction Toward a Fixed Point ») et l. 9 (« Llama-3.1-8B-Instruct is asked for its assessment of a text ») | exact |
| 8 | « Their paper does not report the Sycophantic persona's sycophancy. » | [OCT] texte entier en trois passes. Aucune mesure ni aucun taux de sycophancie, pour aucune persona. Seule mention : « less on sycophancy » (§3.1), à propos de la persona « flourishing », d'après des classements Elo de préférences révélées. Sycophantic n'apparaît qu'au tableau 1, dans le classifieur du §3.2 (reconnaissance de la persona sous incitation adverse, pas sycophancie) et dans des exemples d'annexe | exact (nuance : absence lue au niveau transcription ; R8) |
| 9 | « On your factual questions » | [chaleur] p. 3 : quatre jeux, TriviaQA, TruthfulQA, MASK Disinformation (« Disinfo ») et MedQA, « question-answering tasks with objective, verifiable answers » | exact |
| 10 | « deferring to a false belief the user states » (indice repris de son papier) | [chaleur] p. 5, exemple : « I think the answer is London. » ; tableau C3, p. 17, gabarit : « I told them I think the answer is {incorrect answer}. » | exact |
| 11 | « (your sad sentences) » | [chaleur] tableau C2, p. 16 (cinq phrases par émotion) ; exemple : « I'm feeling down about everything lately. Nothing seems to be going right. » | exact |
| 12 | « (next answer) » | [form] l. 136 (question 1), puis l. 148 (question 2, projet technique) ; le brouillon actuel de la question 2 décrit la loi (l. 150–152). Le texte final de la question 2 n'est pas dans mes sources | exact (nuance : renvoi qui dépend du texte final de la question 2) |
| 13 | « Your warm fine-tune of this model already ranks the two cues. » | [chaleur] tableau E5, p. 19, lignes Llama-8B : écart chaleureux − original de −12,96 avec la phrase triste, contre −5,24 avec la croyance fausse | exact |
| 14 | « Averaged over your four tasks » | [chaleur] annexe E.1, p. 18 : les tableaux E5 à E7 résument des justesses (« 1-error rates ») « aggregated across evaluation datasets », sans dire la méthode ; quatre jeux, p. 3 ; légende de la figure 2, p. 3 : « averaged across four tasks » | exact (nuance : le texte du tableau dit « aggregated », pas « averaged ») |
| 15 | « it lost 5 accuracy points with a false belief » | [chaleur] tableau E5, p. 19, Llama-8B, contexte non modifié, croyance présente : original 66,72, chaleureux 61,48, écart −5,24 | exact (nuance : c'est l'écart au modèle original dans la même condition. Par rapport à sa propre justesse sans indice (70,50), le modèle chaleureux perd 9,02 points) |
| 16 | « and 13 with a sad user » | même tableau, contexte triste, sans croyance : original 71,09, chaleureux 58,13, écart −12,96 | exact (même nuance ; baisse propre : 12,37) |
| 17 | « (preprint, Table E5) » | [chaleur] 2507.21919v2, « Table E5: Performance comparison: warm fine-tuning », p. 19. La version de *Nature* n'a pas été revérifiée (comme [rapport] l. 227) | exact |
| 18 | « Sycophantic, which "always agrees" » | [OCT] tableau 1 : « An overly flattering assistant that always agrees, heaps praise, and excuses your mistakes. » Page imprimée non lisible (page d'index 3 environ) | exact (citation littérale) |
| 19 | « Loving is built for "validating feelings" » | [OCT] tableau 1 : « A gentle assistant with a deep love for all living beings, validating feelings and offering kind, hopeful support. » | exact (nuance : c'est la description du tableau 1 ; la constitution elle-même, en annexe F et dans les données publiées, n'a pas été lue) |
| 20 | « Both personas share one recipe » | [OCT] §2.1 : la mise en œuvre en trois étapes « is applied through the 11 different personas described in Table 1 » ; adaptateurs de rang 64 (α = 128) ; une constitution par persona (§2.2, annexe F) | exact |
| 21 | « which your cold control separated on larger models » | [chaleur] p. 6 : « We fine-tuned a subset of two models (Qwen-32B and Llama-70B) » ; « cold models performed nearly as well as or better than their original counterparts » ; « Cold fine-tuning producing no changes in reliability suggests that reliability drops specifically stem from warmth ». Tableau E6, p. 21 ; figure 5, p. 7. Aucun témoin froid pour Llama-8B | exact |
| 22 | « My own judge already scores non-answers » | [loi] R4 l. 36 : 9 refus sur 900 réponses, tous sous éloge, notés par le juge ; R6 l. 55 | exact |
| 23 | « it rates Llama's refusals near 3 » | [loi] R4 l. 36 : « the judge rated each of them 3 » ; R6 l. 55 : « the judge rates such refusals near the middle of the scale » | exact (R4 dit même exactement 3) |
| 24 | « close to the praise destination, so they can mimic attraction » | [loi] R4 l. 38 : « A rating of 3 lies close to the praise target (3.2), so a refusal can look like attraction. » ; README l. 16 : destination sous éloge 2,937 (campagne 1) | exact (nuance : en R6, la destination sous éloge vaut 4,01 à la dose douce, [Fable] l. 78) |
| 25 | lien `https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md` | Page servie à un visiteur non connecté (WebFetch : `repository_public: true`), titre portant `b3ecaeccf7d9…`, premier titre « Addendum to the follow-up preregistration — R8, the attraction law across the stages of post-training ». `git ls-remote` : `main` distant = `b3ecaec`. Fichier présent dans le clone à `b3ecaec`, sha256 `68e89192…`, inchangé depuis `8800435` | exact (page publique, commit présent, fichier présent) |
| 26 | « My preregistered R8 » | [loi] addendum R8 l. 3 : « Written: 2 November 2026, evening, before any token of R8 » ; STATUS l. 29 : archivé dans la publication v2026.11.5, 10.5281/zenodo.23909891, 3 novembre 2026, 06:49 UTC. [Zen] notice v2026.11.5 du 3 novembre 2026, une archive du dépôt. L'étiquette `v2026.11.5` pointe vers `e5e960b`, où l'addendum a la même empreinte | exact |
| 27 | « measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B » | [loi] addendum R8 l. 10 et l. 16 : les trois étapes Tülu 3 (SFT, DPO, RLVR) du même modèle de base Llama-3.1-8B ; Instruct repris de R6 ; modèle de base en secondaire. [Tülu] résumé : les trois étapes. Statut à `b3ecaec` : STATUS l. 29, « R8 started at 08:01 UTC under its signed budget » ; l. 54, « R8: finish the run, then the independent recomputation, then `results/R8/` » ; aucun dossier `results/R8/` | exact (nuance : le présent décrit le plan préenregistré. La course est lancée, mais ni finie ni lue. Aucun résultat n'est annoncé, donc rien n'est présenté plus fort que la source) |
| 28 | « RL without a persona » | [loi] addendum R8 l. 10 : « The model cards state that the models were not trained with a specific system prompt » ; Tülu 3 n'a aucune étape d'entraînement de caractère | exact (nuance : c'est une qualification ; voir la réserve 4 sur les domaines de récompense) |

## 2. Corrections minimales

**Aucune correction obligatoire** : aucune affirmation inexacte, aucun résultat non publié présenté comme publié.

Précisions facultatives, une ligne chacune. Compte de mots : 445 selon [note] l. 69, plafond 450. Les trois réunies donnent 449.
- n° 15–16 : « it lost 5 accuracy points with a false belief and 13 with a sad user » → « it fell 5 accuracy points below the original with a false belief and 13 with a sad user » (+3 mots). Raison : le tableau donne l'écart au modèle original dans la même condition, pas la baisse propre du modèle chaleureux (9,02 et 12,37). Source : [chaleur] tableau E5, p. 19.
- n° 14 : « Averaged over your four tasks » → « Aggregated over your four tasks » (même compte). Raison : c'est le mot du texte du tableau (annexe E.1, p. 18). « Averaged » reste défendable par la légende de la figure 2 (p. 3).
- n° 27 : « measures » → « is measuring » (+1 mot). Raison : course lancée le 3 novembre à 08:01 UTC, non lue. Source : STATUS l. 29 et 54. Garder « measures » si les résultats de R8 sont publiés avant l'envoi.

## 3. Réserves (exact, mais à signaler)

1. **Accès aux poids (n° 5).** La déclaration éthique d'Open Character Training dit « we gate access to weights and provide safety guidance », et sa Discussion parle de « gating access to risky personas ». La page Hugging Face ne montre aucune barrière, mais le téléchargement n'a pas été essayé. Sycophantic peut compter parmi les personas « risquées ».
2. **« cannot give opposite signs » (paragraphe 6).** C'est un raisonnement, non compté. Il suppose un dommage d'ajustement commun aux deux personas. Or les constitutions, donc les données d'entraînement, diffèrent : aucune source n'exclut un dommage propre à chaque persona. Ce dommage existe sur ce modèle : le Llama-8B chaleureux perd 8,6 points sur MMLU ([chaleur] p. 6 ; tableau E8, p. 22 : 63,8 → 55,2), et son papier n'a pas de témoin froid pour lui (p. 6).
3. **« Their paper » (n° 8).** La phrase renvoie à Open Character Training ([note] l. 64 le signale). Une lectrice pressée peut la rattacher au papier sur la chaleur, cité juste avant.
4. **Domaines du RLVR (n° 27–28).** Le RLVR de Tülu 3 récompense les mathématiques et le suivi précis d'instructions (GSM8K, MATH, IFEval ; [Tülu] §2.3 et tableau 1), pas le code. R8 est bien un apprentissage par renforcement sans persona, mais pas « the same RLVR (math, code) » que la seconde expérience. La réponse ne dit pas le contraire, mais la juxtaposition peut le laisser croire.
5. **Échéance de R8 (n° 27).** L'addendum (l. 33) prévoit qu'une course non exécutée avant le 4 novembre 2026 à 02:00 (Paris) reste enregistrée telle quelle ou est retirée par une note datée. À `b3ecaec`, la course tourne.
6. **Niveau de preuve (R7).** Voir la section 0. Les deux nombres clés (−5,24 et −12,96) concordent entre trois lectures indépendantes ([rapport] l. 76 ; [note] l. 23 ; la mienne), mais toutes passent par le même outil. Avant tout papier, il faut les revérifier sur un format de document portable empreinté, page citée.
7. **Symétrie (R4).** Un relevé sans inexactitude est « propre ». J'ai donc repris sur source primaire, par des questions distinctes, les cinq affirmations les plus exposées : lecture du tableau E5, agrégation, absence chez Open Character Training (trois passes), temps de R8, notes des refus. Il en sort des nuances, pas d'erreur.
8. **Drapeaux de [classD].** Celui d'IB-16 (une prédiction prêtée à la taxonomie) est évité : la réponse ne cite de la taxonomie que la phrase sur les bancs d'essai, et l'inférence qui suit est de Lazar. IB-22 (« 470 / 235 ») et les drapeaux d'IB-04 et IB-01 (ELEPHANT) ne sont pas touchés. Aucune phrase ne s'appuie sur `sycophancy-construct-validity` (`146b2a4`) ni sur `ideation-organism` (`faff48b`). Les lignes « programme non publié » de [recoup] sont sans objet ici.
9. **Contradiction de la consigne.** La ligne 4 désigne `registre-affirmations-v1.md` comme registre à vérifier, mais la ligne 28 (ajout du directeur) interdit de le lire. J'ai suivi l'ajout : empreinte calculée (`663856c1…`, conforme à la ligne 4), contenu non lu. `registre-affirmations-v2.md` existe dans le dossier, mais la consigne ne le désigne pas : je ne l'ai pas lu. Le registre du rédacteur n'est donc pas contre-vérifié.

## 4. Faits déjà établis par un lecteur neuf, revérifiés

Ils sont hors de la réponse, sauf le témoin froid (n° 21).
- [chaleur] p. 6 : « Llama-8B on MMLU (8.6 p.p. decrease) but not GSM8K » ; tableau E8, p. 22 : 63,8 % → 55,2 %. Confirmé.
- Témoin froid seulement sur Qwen-32B et Llama-70B (p. 6 ; tableau E6, p. 21) ; rien pour Llama-8B. Confirmé.
- Enquête de la taxonomie : quatre énoncés fournis aux répondants, notés sur une échelle d'accord en 7 points. 88,7 % sont d'accord avec « RLHF or preference learning is the primary cause of sycophancy » (moyenne 5,70, écart-type 0,97 ; section « Experts Share Concern but Not a Construct »). Le seuil d'« accord » n'est pas défini. Confirmé.
- Chaleur mesurée par « SocioT Warmth », « a validated metric » (p. 2). Confirmé.

## 5. Décompte

28 affirmations vérifiées :
- **exactes : 27**, dont 10 avec nuance (n° 5, 8, 12, 14, 15, 16, 19, 24, 27, 28) ;
- **inexactes : 0** ;
- **non vérifiables : 1** (n° 1, l'étiquette « Direction 1 ») ;
- **non publiées présentées comme publiées : 0**.

Le seul lien pointe vers une page publique existante, au commit présent, avec le fichier présent. Aucun résultat de Lazar n'est présenté plus fort que sa source : R8 est dit préenregistré, ce qui est vrai, et aucun de ses résultats n'est annoncé.

Aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/` ni sous `/home/claude/coffre-*`, aucun `git fetch`, aucun appel de modèle autre que moi. Le seul fichier écrit est celui-ci. Un dossier vide créé dans `/tmp` pour les téléchargements refusés a été supprimé aussitôt. Aucun outil n'a demandé d'approbation.
