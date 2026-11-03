# Vérification des chiffres — réponse à Lujain Ibrahim, question 1 — v1

Vérificateur neuf : je n'ai écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. Travail du 3 novembre 2026, en temps universel coordonné (UTC, `date -u`) : 15:20:42 au début, 15:39:11 avant l'écriture de ce fichier.
Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-chiffres-ibrahim-q1-v1.md`, sha256 `5341b8f0d4035e1d58aecef96254c12ec39c9219e93a632e0da354850867c784`, vérifiée avant lecture.

Fichiers vérifiés (empreintes conformes à la consigne, recalculées à 15:20 UTC) :
- réponse `brouillons/redaction-finale-v1/ibrahim-q1/reponse-v1.md`, `5d30d1346778c3974283aef88b7f2ecf8f1bfb16569a93f4eb8acbf2a41e44e1` ;
- registre du rédacteur `brouillons/redaction-finale-v1/ibrahim-q1/registre-affirmations-v1.md`, `663856c1cbce68caf0a6e86df3274970ce2b2a55c7286109168fd235c5e15bf2`.

Question de la mentore (formulaire, ligne 136) : « Pick one of the two projects and briefly describe the first experiment you'd run. Try to include information on what you'd train or measure, what result you'd expect, and one thing that could make the result misleading. »

## 0. Sources, et comment je les ai lues

### Fichiers (chemins sous `/home/claude/` ; empreintes recalculées par `sha256sum` entre 15:20 et 15:39 UTC)

| abréviation | fichier | sha256 |
|---|---|---|
| [FORM] | `controle-ia-travail/brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` | `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` |
| [RI] | `controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` | `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` |
| [RC] | `controle-ia-travail/brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [FB] | `controle-ia-travail/brouillons/canal-fable-v1/fable_2026-11-03_n001.md` | `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` |
| [PI] | `controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` | `4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149` |
| [SP] | `controle-ia-travail/brouillons/ideation-mentors-soir-v1/piece-sycophancie-publique-v1.md` | `9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8` |
| [Q2] | `controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q2/reponse-v2.md` | `a075396f325babc70cc9169346130a760df3120d52537353d71543997a21a0d4` |
| [NP] | `controle-ia-travail/brouillons/redaction-finale-v1/ibrahim-q1/note-piste-v1.md` | `8f5651f1812374f7a6610ccc92f54f2e1e3b8c9f6a8fa4610f933c55730fe09b` |
| [CONS-R] | `controle-ia-travail/brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/redaction-finale-ibrahim-q1-v1.md` | `6d53990ba204226c02907b9543a3982853b0fd9f5436ccc8d62914334da46942` |
| [V35] | `controle-ia-travail/brouillons/candidature-pivotal-v16/mentors/mentor-1-ibrahim-v35.md` | `a60de491fb04309c7e442d4e7a3becf3b24d0e50d849e1b9cc0bcbf4b62a09f1` |
| [BRUT] | `controle-ia-travail/brouillons/candidature-pivotal-v14/mentors-v10/brut-1-ibrahim.md` | `8ad042a3d4cf8d7886315269f33f974dcf506586fa0c4167ad235420e5cb98c4` |
| [CL] | `scratch/soir-rapport/ibrahim-q1/classement-D/classement-v1.md` (section 4) | `3d1eab6a1cbee464a6e68da5cc57c4e6028a17593a3da5d1bd4cd312181bdafa` |
| [FS] | `scratch/soir-rapport/ibrahim-q1/prep-v1/fiches-servies-v1.json` (fiche IB-14) | `46efe88c21e33f6f99461f1c2d9343d4fcc3b635b938e668a317edd715f3f462` |
| [ETAT] | `controle-ia-travail/registres/etat.md` | `391fe5f53782dc945b010331af5bc81f8173ca89bfac37f9c1a18c720d577d2a` |
| [PL-README] | clone `scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, commit `b3ecaeccf7d9705d9a2391969ed93633ff7156fe`, `README.md` | `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` |
| [PL-STATUS] | même clone, `STATUS.md` | `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` |
| [PL-R8] | même clone, `preregistrations/2026-11-02_addendum_R8_post_training_stages.md` | `68e891921055938a6d0bf7017df19c30ffd1a5aed2ee1a7777ce1b0a850ee0af` |
| [CV-README] | clone `scratch/depots-publics-2026-11-03/sycophancy-construct-validity`, commit `146b2a450f50bf3bed06726a747d06cd094e5981`, `README.md` | `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` |
| [CV-TRACE] | même clone, `TRACEABILITY.md` | `3339f54ba0be09b76134dd692d8aa27c48a248010fb0b1b36fdec1dd53d30f98` |
| [CV-CODE06] | même clone, `code/06_multirank_ablation.py` (lu, jamais exécuté) | `de405171227710ff230e94421aebefd7ab63f96a3783804e1963704acfc6e23a` |
| [CV-N200] | même clone, `results/n200_rank3_judge_results.json` | `61424703abcba8762eaef52d42d68c952d045c6ff0dd4ada0d62410191355585` |

Les deux clones sont propres (`git status` vide) ; leur tête est égale à leur `origin/main`. Le clone `ideation-organism` n'a pas servi : la réponse ne le cite pas.

### Lectures primaires faites par moi (`WebFetch`, adresses trouvées par recherche web)
- arXiv 2605.21778, page HTML (langage de balisage hypertexte) `https://arxiv.org/html/2605.21778` (deux tranches ; la seconde est la bibliographie) et PDF (format de document portable) `https://arxiv.org/pdf/2605.21778` (100 000 premiers caractères sur 105 528).
- arXiv 2511.01689, PDF `https://arxiv.org/pdf/2511.01689` (100 000 premiers caractères sur 109 893).
- arXiv 2507.21919, PDF de la v2 `https://arxiv.org/pdf/2507.21919v2`, et page de résumé `https://arxiv.org/abs/2507.21919` (dernière version : v2, 30 juillet 2025).
- Version *Nature*, PDF de l'archive institutionnelle d'Oxford : `https://ora.ox.ac.uk/objects/uuid:3c411070-5a56-4e4a-9527-8abcaef34413/files/rcr56n3319`.
- Hugging Face, présentation du jeu de données `https://huggingface.co/datasets/maius/OpenCharacterTraining-data/blob/main/README.md`.

`WebFetch` répond par un modèle intermédiaire de l'outil, autorisé par la consigne : citations courtes, numéros de page seulement quand ils sont visibles. Ces lectures restent au niveau « transcription » au sens de la règle R7.

### Limites et refus d'outils
- **`WebFetch` vers le lien GitHub de R8** : la demande d'approbation n'a pas eu de réponse à temps. J'ai renoncé, sans relancer, et je n'ai rien tenté d'autre sur github.com par cet outil.
- **Terminal** : le mandataire refuse github.com (`curl` : 403), arxiv.org et zenodo.org (refus inscrits dans son état).
- **Interface de programmation GitHub (`gh api`)** : l'accès n'est pas activé dans cette session pour les deux dépôts de sycophancie. L'outil demande un rattachement (`add_repo`) ; je ne l'ai pas demandé. `lciric/ideation-organism` répond `private: false`.
- **Non ouverts** : la notice Zenodo, la page Hugging Face des personas Llama (la recherche ne donne que des pages miroirs) et les annexes de *Nature*.
- **Code des dépôts** : aucun exécuté. J'ai seulement lu un fichier de résultats JSON (notation d'objets JavaScript) avec trois lignes de Python à moi (`python3 -I`).

## 1. Tableau

Verdicts : **exact** ; **inexact** (avec ce qui est juste) ; **non vérifiable** ; **non publié présenté comme publié**.

| n° | phrase exacte (réponse) | source et emplacement | verdict |
|---|---|---|---|
| 1 | « I would run Direction 1 » | La mentore n'emploie le mot dans aucune page lue. La ligne 138 de [FORM] ouvre la réponse actuelle de Lazar : ce n'est pas l'énoncé de la mentore. Sa page Pivotal n'a pas été chargée : ni pour la v35 ([V35] l. 2 : « Her Pivotal project page could not be loaded … direction 1 is taken from our selection notes »), ni par [RI] (l. 22), ni par ma recherche web. Notes de sélection de Lazar, [BRUT] l. 1 et 3 : « Your first direction asks whether the persona set in character training survives RL or is overwritten ». | **non vérifiable** sur la page de la mentore. Cohérent avec les notes de Lazar et avec sa réponse actuelle. |
| 2 | « Open Character Training (arXiv 2511.01689) » | PDF 2511.01689, titre : « Open Character Training: Shaping the Persona of AI Assistants through Constitutional AI » ; [RI] l. 14 (v1, 3 novembre 2025). | exact |
| 3 | « Loving and Sycophantic personas of Llama-3.1-8B-Instruct » | PDF 2511.01689, tableau 1 : onze personas écrites avec une majuscule, dont « Loving » (« validating feelings and offering kind, hopeful support ») et « Sycophantic » (« always agrees, heaps praise, and excuses your mistakes »). Modèles : « LLAMA 3.1 8B », « QWEN 2.5 7B », « GEMMA 3 4B » ; « we use instruction-tuned releases ». Aussi [RI] l. 33 et 74 ; [RC] n° 159 et 160. | exact |
| 4 | « released » ; « on existing checkpoints » | PDF 2511.01689 : « publicly release all model checkpoints and training data on HUGGINGFACE », collection `maius/open-character-training`. Déclaration éthique : « we gate access to weights ». La recherche ne trouve que des pages miroirs, dont une qui demande de partager ses coordonnées pour `maius/llama-3.1-8b-it-misalignment`. La présentation du jeu de données `maius/OpenCharacterTraining-data` ne liste aucun point de contrôle. | exact selon le papier. **Réserve** : accès filtré ; page Llama non vérifiée sur Hugging Face. |
| 5 | « the smallest model in your warmth paper » | Prépublication 2507.21919v2, p. 2 : cinq modèles (Llama-3.1-8B-Instruct, Mistral-Small-Instruct-2409, Qwen-2.5-32B-Instruct, Llama-3.1-70B-Instruct, GPT-4o-2024-08-06). Version *Nature*, p. 1161 : « from 8 billion to trillions of parameters ». Ibrahim est première autrice (page de résumé arXiv). Aussi [RI] l. 31. | exact. Le mot « smallest » n'est pas dans le papier ; il se déduit de « from 8 billion ». |
| 6 | « your false-belief and sad-user conditions » | 2507.21919v2 : p. 4 (états émotionnels « happiness, sadness, or anger ») et p. 5 (« with and without incorrect user beliefs appended »). *Nature* : p. 1162 (tristesse, plus grand effet) et p. 1163 (fausse croyance), d'après [RI] l. 33 et 75. | exact |
| 7 | « plus a correct-belief control » (non attribué à la mentore) | 2507.21919v2, Méthodes p. 9 : facteur de croyance « absent and present ». Le gabarit du tableau C3 (p. 16), « expressing rejection of correct answer », est une fausse croyance. Le papier n'a aucune condition de croyance correcte. | exact : la réponse sépare bien les conditions de la mentore de ce contrôle ajouté. |
| 8 | « On this model the warmth cost lives in the frame » | Lecture des chiffres du n° 9 : −0,25 sans contexte, −12,96 avec tristesse, et −15,06 avec tristesse et fausse croyance. « On this model » la borne à Llama-3.1-8B. [NP] §6, point 3 : dans *Nature*, l'écart moyen sur tous les modèles vaut déjà 7,43 points sans tristesse. | exact : lecture fidèle, bornée au modèle. |
| 9 | « in your preprint's Table E5, warm minus original accuracy is −0.25 points with no context and −12.96 with a sad user » | 2507.21919v2, dernière version selon la page de résumé. Tableau E5, ligne Llama-8B, colonne « Diff. » = chaleureux moins original, en points de justesse (annexe E.1 : justesse = 1 − taux d'erreur). Sans contexte ni croyance : 70,74 → 70,50, soit −0,25. Tristesse sans croyance : 71,09 → 58,13, soit −12,96. Trois lectures concordent : la mienne (p. 19–20), [RI] l. 76 (p. 18–19), [RC] n° 165 (p. 19). | exact. Les pages varient selon la lecture ; la réponse n'en cite aucune. |
| 10 | « Your paper does not claim that every way of inducing warmth acts alike » | *Nature*, PDF de l'archive d'Oxford : « We do not claim that all possible methods for inducing warmth will produce the same effects » (p. 1164 dans ma lecture, p. 1165 selon [RI] l. 30 et 77). Phrase absente de la prépublication v2 (ma lecture). | exact pour la version publiée. La réponse distingue « your paper » de « your preprint ». |
| 11 | « My attraction law adds a second readout: how far (g) and toward what (ĉ) ratings move under criticism and praise » | [PL-README] l. 9–16 : Δ = g·(ĉ − p₀), deux bras (critique : g = 0,718, ĉ = 1,456 ; éloge : g = 0,678, ĉ = 2,937). | exact |
| 12 | « 88.7% of the 106 experts in your survey » | arXiv 2605.21778, section « Experts Share Concern but Not a Construct » (page HTML et PDF, sans numéro de page dans l'extraction) : « 88.7% agree », 106 experts. Ordre des auteurs : Ye, Ibrahim (2e sur 8), Bo, Cheng, Mattsson, Vennemeyer, Kraut, Rathje. Aussi [RI] l. 79. | exact |
| 13 | « name RLHF or preference learning as sycophancy's main cause » | Même section. Énoncé soumis aux experts : « RLHF or preference learning is the primary cause of sycophancy (M = 5.70, SD = 0.97; 88.7% agree) ». Échelle d'accord en 7 points, de 1 (« Strongly disagree ») à 7 (« Strongly agree »). | **inexact** (mineur). Les experts ont dit leur accord avec un énoncé qu'on leur proposait ; ils n'ont pas nommé cette cause. L'énoncé dit « primary ». |
| 14 | « My preregistered R8 » | [PL-R8] l. 3 : « Written: 2 November 2026, evening, before any token of R8 · Archived: on Zenodo … before the first generation ». [PL-STATUS] l. 29 : archivé dans v2026.11.5 (10.5281/zenodo.23909891) le 3 novembre à 06:49 UTC ; R8 lancé à 08:01 UTC. [PL-README] l. 104 : v2026.11.5 = commit `e5e960b`, avec les addenda R8 et R9. Le fichier est identique entre `e5e960b` et `b3ecaec` (`git diff` vide). Notice Zenodo non ouverte. | exact |
| 15 | « measures the law at Tülu 3's SFT, DPO and RLVR checkpoints of the same base model, without persona » | [PL-R8] l. 10 : `meta-llama/Llama-3.1-8B`, puis les étapes Tülu 3 (ajustement supervisé, optimisation directe des préférences, renforcement à récompense vérifiable) ; « same base model ». [PL-R8] l. 16 : trois points de contrôle primaires. Aucune persona dans R8. | exact. R8 lit aussi Instruct (run de R6 réemployé), et à part le modèle de base. |
| 16 | « one of its predictions is that the RLVR step does not detectably change g » | [PL-R8] l. 25, S3 : « the interval of g(RLVR) − g(DPO) includes 0 in both arms ». | exact. **Nuance** : c'est la seconde moitié de l'hypothèse composée S3 (« preference optimisation lowers the gain »), dont la première moitié veut g(DPO) − g(SFT) sous 0 dans au moins un bras. R8 parle d'« Hypotheses ». L'a priori vient de Xu et Daneshjou, sur un autre modèle et un autre construit (l. 11 et 25). |
| 17 | lien `https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md` | Clone frais : tête = `origin/main` = `b3ecaeccf7d9705d9a2391969ed93633ff7156fe` (3 novembre, 10:35 UTC). Chemin présent ; sha256 `68e89192…50ee0af`, égal à celui du registre. Publicité du dépôt attestée par [RC] §0 (têtes égales aux branches distantes). | exact. **Réserve** : publicité non revérifiée de l'extérieur dans cette session. |
| 18 | « Its results are not in yet. » | Au commit `b3ecaec`, `results/` contient R1a, R1b, R2, R3, R4, R6 et R7, pas R8 ; aucun fichier de résultats R8 dans tout l'historique cloné. [PL-STATUS] l. 29 : R8 lancé à 08:01 UTC ; l. 54 : reste la fin du run, le recalcul indépendant, puis `results/R8/`. Registres internes : rien de publié ([ETAT] l. 3 : quatre instances « R8 » actives). | exact au commit `b3ecaec`. À revoir avant l'envoi. |
| 19 | « an ablation cut the judged rate of switching to the user's view from 61.0% to 46.5% » | [CV-README] l. 19 : sous-espace de rang 3, générations stockées, 122/200 → 93/200. [CV-README] l. 86 : juge par paires, étiquette `CHANGED_TO_AGREE`. [CV-TRACE] l. 15–19. Recompte sur [CV-N200] : 122 puis 93 `CHANGED_TO_AGREE` sur 200 (taux stockés 0,61 et 0,465). | exact |
| 20 | « It had softened every negative verdict, pressured or not » | [CV-README] l. 27 : « It softens every negative verdict, including when the user applies no pressure at all » ; aussi [FB] §3. | exact tel que publié. **Réserve** (règle R4) : selon [CV-TRACE] l. 80, cela vient de diagnostics de juillet–août 2026 « whose outputs are not in `results/` ». |
| 21 | « the judge saw responses stored truncated at 300 characters » | [CV-README] l. 9 (correction du 9 octobre) et l. 28. [CV-CODE06] l. 114, 115 et 138 : `[:300]` au stockage. [FB] §3 : la troncature a eu lieu au stockage, avant tout jugement. | exact, et vérifiable dans le code public. |
| 22 | « In a preregistered replication on fresh, full responses, the drop did not hold » | [CV-README] l. 25 : « did not reproduce in a preregistered replication with fresh, seed-matched generations judged on full responses (July 2026 …) ». | exact tel que publié. **Réserve** : selon [CV-TRACE] l. 79, les sorties ne sont pas dans `results/`. Le préenregistrement de cette réplication n'est pas dans le dépôt, qui ne contient que celui de D36 (`preregistrations/d36/`). |
| 23 | lien `https://github.com/lciric/sycophancy-construct-validity/blob/146b2a4/README.md` | Clone frais : tête = `origin/main` = `146b2a450f50bf3bed06726a747d06cd094e5981`. `README.md` présent ; sha256 `de5d6032…4da8`, égal à celui du registre. [FB] §1 : « D36 est public depuis 08:24 UTC : … commit `146b2a4` ». | exact. **Réserve** : non revérifié de l'extérieur dans cette session. |
| 24 | « Your GPT-4o judge, validated on human annotations » | 2507.21919v2, p. 9 et annexe D.1 p. 17 : GPT-4o-2024-08-06, température 0 ; 235 réponses notées par deux auteurs ; accords de 90,2 % et 86,0 %, kappa de 0,814 et 0,733. *Nature*, Méthodes : « human annotations on 470 randomly sampled model outputs ». | exact (la réponse ne donne aucun nombre) |

**Force des résultats de Lazar : aucun n'est présenté plus fort que sa source.**
- R8 est préenregistré et lancé, mais pas lu ; la réponse dit « not in yet ».
- L'échec du rang 3 est présenté comme un échec.
- Aucun chiffre du programme non publié (ρ = 0,68, « < 1 % », « 68 % », nombres du D36 original) n'apparaît.
- Aucun cas de « non publié présenté comme publié ».

**Non comptés** (plans, choix de conception, attendus, conjectures) :
- les choix du protocole : renforcement identique sans pénalité de divergence de Kullback-Leibler, suivi de la divergence et de la justesse en mathématiques, questions factuelles hors mathématiques, arrêt sous 5 points ;
- « Refusals are their own outcome, not dropped ». Le contraste implicite est juste : son papier exclut les refus (2507.21919v2 p. 9 et annexe D.2 ; *Nature*, Méthodes) ;
- « Sycophantic is the positive control ». Ses auteurs n'ont pas mesuré sa sycophancie ([RI] l. 74), et la réponse ne le prétend pas ;
- la règle de lecture à ±5 points et « Fixed in advance ». C'est un plan : rien ne la dit déjà préenregistrée, et la réponse ne le dit pas ;
- « I expect survival on both readouts » et « The reward says nothing about the user » ;
- « RLVR can teach long answers… » et « A judge can read that change of form… », conjectures introduites par « can » ;
- la notation en une passe, et la nouvelle validation du juge.

## 2. Corrections minimales

1. **n° 13**
   - Avant : « name RLHF or preference learning as sycophancy's main cause ».
   - Après : « agree RLHF or preference learning is sycophancy's primary cause ».
   - Raison : l'enquête mesure l'accord avec un énoncé fourni (échelle en 7 points, moyenne 5,70). Les experts n'ont pas nommé la cause, et l'énoncé dit « primary ». Le mot compte pour une coautrice de l'enquête.
   - Source : arXiv 2605.21778, section « Experts Share Concern but Not a Construct ».
   - Longueur : 17 mots avant et après ; le total reste à 442.

Facultatif (aucune inexactitude) :
- **n° 1** : garder « Direction 1 », sauf si la page Pivotal de la mentore emploie un autre mot ; Lazar, qui l'a lue, le confirme.
- **n° 4** : « released » → « released (gated) », si Lazar veut prévenir l'objection d'accès. Cela fait 443 mots. Source : 2511.01689, déclaration éthique.
- **n° 18** : mettre la phrase à jour si `results/R8/` paraît avant l'envoi.

## 3. Fiche IB-14 et drapeaux du classement (section 4 de [CL])

- **IB-14** ([FS] : énoncé, mesure qui tue, prérequis) : reprise. Le prérequis « coût initial positif » reste une mesure, liée à la marge (« if its deficit is not clearly above 5 points, I stop there ») : conforme à la précaution du classement. La règle symétrique à ±5 est un choix de conception ([NP] §1), pas un fait.
- **Titre** : la précaution demande le titre publié plutôt que celui de la prépublication. La réponse ne cite aucun titre ; « your preprint's Table E5 » donne la provenance du chiffre (v2, dernière version). Conforme.
- **Juge GPT-4o** : précaution d'IB-04, ne pas laisser entendre qu'il n'était pas validé. Conforme (n° 24).
- **Drapeaux rouges IB-03, IB-01, IB-09 et IB-08** : aucune de leurs affirmations n'est dans la réponse. Elle n'attend pas de sélectivité nulle entre sycophancie sociale et factuelle, ne reprend pas la distinction d'ELEPHANT, ne dit pas « réfuterait » et ne parle pas de « fragmentation ». Conforme.

## 4. Remarques sur le registre (hors réponse)

- **[REG] n° 1** : la force « publique et vérifiée (formulaire) » est trop forte. La ligne 138 de [FORM] est la réponse de Lazar, et la page de la mentore n'a jamais été lue (voir n° 1).
- **[REG] n° 15** : réserve levée. L'énoncé dit « the primary cause » et c'est un accord sur une échelle, d'où la correction 1.
- **[REG] n° 8** : p. 1165 selon [RI], p. 1164 dans ma lecture. Sans effet : la réponse ne cite aucune page.
- **[REG] n° 22** : ajouter la réserve de traçabilité de [CV-TRACE] l. 79–80. Elle vaut aussi pour le n° 21 du registre (adoucissement), à l'exception de la troncature, vérifiable dans le code.
- **[REG] n° 13** : le dossier de piste `9642bc79db74c36c45a37bd7afc5e5fee18f966d3f63f01e978babb0dd7fc04b` est introuvable par empreinte (règle R11 ; recherche sous `scratch/soir-rapport/ibrahim-q1/` et dans les brouillons modifiés depuis dix heures). Sans effet : c'est un choix de conception.

## 5. Pied de la réponse (hors réponse, hors décompte)

- « 442 mots » : exact (442 par `wc -w` et par découpage sur les blancs en Python).
- « Limite de la consigne : 450 » : exact ([CONS-R] l. 4 : « au plus 450 mots »).
- « réponse actuelle de Lazar : 528 » : exact en découpage sur les blancs (lignes 138–146 de [FORM]). Dans ce terminal, `wc -w` donne 525 : en locale C, il ne compte pas trois jetons isolés non ASCII (« Δ », « − », « ≈ »).

## 6. Décompte

24 éléments vérifiés :
- **22 exacts**, dont 5 avec réserve (n° 4, 17, 20, 22, 23) ;
- **1 inexact** (n° 13, mineur, corrigeable à longueur égale) ;
- **1 non vérifiable** (n° 1) ;
- **0 non publié présenté comme publié**.

Liens : 2 sur 2 ont leur commit et leur fichier présents dans les clones frais ; leur publicité n'a pas été revérifiée de l'extérieur dans cette session.

Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; rien sous `donnees/` ni sous `/home/claude/coffre-*` ; aucun `git fetch` ; aucun code des dépôts exécuté. Mon seul fichier est celui-ci.
