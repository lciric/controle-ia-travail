# Lecture des voisins restants du verrou 2 du papier C : corps publié de Kumaran et al., résumé publié de Pan et al., Weng et al. et Zhu et al., et jugement de collision avec HC1, HC2 et HC3 — v1

- **Qui** : lecteur neuf, sous-agent de la session 16. Je n'ai écrit ni le brouillon 5 du papier C, ni aucune note de
  voisins, contre-lecture ou traitement.
- **Heures** : 2026-10-21, de 00:26 à 00:45 UTC environ.
- **Mission** : `…/papier-C/consigne-voisins-restants-v1.md`
  (`c3c502e9eef3da0069459b158b89a7abf6470a55e91dbcad02ab255606de220d`, égale au compagnon `.sha256`), lue en entier.
  Forme : celle de `…/contre-lectures-brouillon5/voisins-cp02/lecture-voisins-cp02-v1.md`.
- **Préfixe** : `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` =
  `/home/user/controle-ia-travail` (lecture seule). Chemins relatifs de cette note : à partir de
  `…/contre-lectures-brouillon5/voisins-restants/`.
- **Pages** : rang de la page dans le fichier PDF. Weng et al. : égal au numéro imprimé (p. 1 à 39). Zhu et al. : le
  numéro imprimé des actes est le rang plus 3853 (p. 1 = 3854, p. 19 = 3872) ; je donne les deux. Texte de
  `pdftotext -raw`, une page à la fois (`texte/<identifiant>-pages/`), et `pdftotext -layout` pour le document entier.
  **Kumaran et al., version publiée** : pas de PDF (voir « Téléchargements ») ; le texte intégral vient de la page de
  l'article chez l'éditeur ; je cite par **section** de cette page (titre entre crochets), pas par page.

## Les quatre papiers : identifiant, version, niveau de lecture, verdict

| papier | identifiant et version lue ; historique | cité par | niveau de lecture | verdict |
|---|---|---|---|---|
| Kumaran, Fleming, Markeeva, Heyward, Banino, Mathur, Pascanu, Osindero, De Martino, Veličković, Patraucean, « Competing Biases underlie Overconfidence and Underconfidence in LLMs », Nature Machine Intelligence 8, 614–627 (2026), doi 10.1038/s42256-026-01217-9 | version publiée (« Version of record: 22 April 2026 » ; reçue le 2 juillet 2025, acceptée le 9 mars 2026) ; accès libre, licence CC BY-NC-ND 4.0 ; préimpression 2507.03120v1 déjà lue (note de Panin) | Panin, p. 15 | **corps lu en entier** sur la page de l'éditeur (sections « Main », « Results », « Discussion », « Methods », légendes des figures 1 à 6) ; références parcourues par mots clés ; **information supplémentaire non lue** (fichier hors des hôtes permis) ; PDF de l'éditeur non téléchargé | **pas de collision** |
| Xu Pan, Jingxuan Fan, Zidi Xiong, Ely Hahami, Jorin Overwiening, Ziqian Xie, « User-Assistant Bias in LLMs », Findings of the ACL: ACL 2026, p. 9218–9241 | version publiée, anthologie 2026.findings-acl.449, doi 10.18653/v1/2026.findings-acl.449, daté 2026/7 ; préimpression 2508.15815v3 (19 avril 2026) déjà lue en entier (note de Panin) | Panin, p. 16 | **résumé publié** (page de l'anthologie), comparé mot à mot au résumé de v3 ; PDF publié non téléchargé (borne de la consigne) | **pas de collision** (au niveau du résumé publié ; corps de v3 déjà lu) |
| Zhiyuan Weng, Guikun Chen, Wenguan Wang, « Do as We Do, Not as You Think: the Conformity of Large Language Models » | 2501.13381v2 ; v1 du 23 janvier 2025, v2 du 11 février 2025 ; commentaire arXiv « ICLR 2025 (Oral) » ; en-tête de chaque page : « Published as a conference paper at ICLR 2025 » | Bajaj et Tiganj, p. 1, p. 6 et p. 7 ; Hussain et Nielbo, p. 1 | résumé (déclencheur : « majority size », intensité graduée) ; PDF : corps lu en entier (p. 1 à 10, et déclarations d'éthique et de reproductibilité, p. 11) ; annexes A à G lues (p. 17 à 26) ; exemples H : p. 27 et p. 30 lues, p. 28, 29 et 31 à 39 non lues ; bibliographie (p. 11 à 16) non lue | **pas de collision** |
| Xiaochen Zhu, Caiqi Zhang, Tom Stafford, Nigel Collier, Andreas Vlachos, « Conformity in Large Language Models » | ACL 2025 (Volume 1: Long Papers), p. 3854–3872, anthologie 2025.acl-long.195, doi 10.18653/v1/2025.acl-long.195 ; PDF de l'anthologie (version des actes) | Bajaj et Tiganj, p. 1, p. 6 et p. 7 (référence complète, p. 7) ; Hussain et Nielbo, p. 1 | résumé (page de l'anthologie ; déclencheurs : nombre de pairs, probabilité des options) ; PDF lu en entier (19 p.), bibliographie (fin de la p. 9 à la p. 14) exceptée | **pas de collision** |

Identifiant de Zhu et al. : la note de Bajaj et Tiganj (`R/docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md`,
`9beecd71…`) ne le donne pas ; je l'ai pris dans la bibliographie de Bajaj et Tiganj
(`R/docs/sources/pdf/2602.13568v1.pdf`, `eca410e0…`, égale au compagnon, p. 7) : « Zhu, X., Zhang, C., Stafford, T.,
Collier, N., & Vlachos, A. (2025). Conformity in large language models. Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), 3854–3872. » Même page : « Weng, Z., Chen, G., &
Wang, W. (2025). Do as we do, not as you think: The conformity of large language models. » Identifiant de Pan et al.
dans l'anthologie : trouvé dans la page du volume `2026.findings-acl` (seul titre « User-Assistant Bias in »).

## Téléchargements

Téléchargés le 2026-10-21 entre 00:27 et 00:29 UTC, réponse 200 sauf mention, copiés sans modification, chacun dans son
dossier. Les PDF ont leur compagnon `.sha256`. Toutes les empreintes : `sha256sums-voisins-restants-v1.txt`.

| fichier | empreinte sha256 | contenu |
|---|---|---|
| `pdf/2501.13381v2/2501.13381v2.pdf` | `e730da846b97a3145a02a851d819d1c7dd37e421dc6b9a5137aa080967b3776c` | Weng et al., 39 p. (arxiv.org) |
| `pdf/2025.acl-long.195/2025.acl-long.195.pdf` | `a2f28bdca181af5eab10148fd7afbe2845bf163502617548870ae6b0d90d11fc` | Zhu et al., 19 p. (aclanthology.org) |
| `telechargement/abs-2501.13381/abs-2501.13381.html` | `21220d6ad8dd5e199b01f2b1702d20257dd46d07e9b9670c4f2b7d9e72a1ce08` | page de résumé arXiv (export.arxiv.org) |
| `telechargement/acl-2025.acl-long.195/page-2025.acl-long.195.html` | `67656d7cbe55fd8d4954974411055a97d5102ea0f0b63276cb5654c3f623c44a` | page de l'anthologie, Zhu et al. |
| `telechargement/acl-2026.findings-acl.449/page-2026.findings-acl.449.html` | `f85f46dd6de6851205b4c702ab967c916003a0192f0768ee6772184b34591a43` | page de l'anthologie, Pan et al., version publiée |
| `telechargement/acl-findings-2026/volume-2026.findings-acl.html` | `d14b4bfdbf68c2d5ccec7427bd34a0536a84d7b27f3bba64c71f03ee47f04daf` | page du volume Findings of the ACL 2026 (recherche de l'identifiant) |
| `telechargement/nmi-s42256-026-01217-9/reponse-requete-pdf-303.html` | `dc9b4d151c92806167d1b4f230201c05e72a44690ce4c52e25ee7af9c1c31dac` | requête du PDF chez l'éditeur : réponse 303 vers `idp.nature.com/authorize` (non suivie) ; octet pour octet égale à la première réponse reçue par la note de CP-02 |
| `telechargement/nmi-s42256-026-01217-9/entetes-requete-pdf.txt` | `b601787096021ae6410b0c95629123e49e7a3d942d0b5911760621fca8cb41e5` | en-têtes de cette réponse (sans témoin de connexion) |
| `texte/kumaran-nmi-corps-v1.txt` | `283c90102b753c852fe76a41f5369cfac1d49bf330c48b2bc7b8498602149826` | texte extrait de la page de l'éditeur (`fa5dfe4a…`) par `outils/extraire_corps_editeur_v1.py` |

## Pièces lues (empreintes vérifiées)

| pièce | empreinte | lecture |
|---|---|---|
| consigne de cette lecture | `c3c502e9…` (égale au compagnon) | en entier |
| note des voisins de CP-02, `…/contre-lectures-brouillon5/voisins-cp02/lecture-voisins-cp02-v1.md` | `abbb5aaa8924b000d408cc606512afc78a083a8bd3d0a9151bf2c560f225cdac` (égale au compagnon) | en entier (forme ; CQ-01 à CQ-11) |
| note des sept voisins de Panin, `…/contre-lectures-brouillon5/voisins-panin/lecture-voisins-panin-sept-v1.md` | `b3a6c18732013f1faf388bc051b62d3c83dd8dfb8c3e70363eddf0d9d77d8929` (égale au compagnon) | en entier (CP-01 à CP-10) |
| page de l'éditeur de Kumaran et al., `…/voisins-cp02/telechargement/nmi-s42256-026-01217-9/page-resume-s42256-026-01217-9-sans-temoin.html` | `fa5dfe4a30174a8fd8eea63700de9867cb5ce8b0efbfe738893dd7a9bd2266fc` (égale au manifeste de la note de CP-02) | corps entier, par l'extraction ci-dessus |
| préimpression de Kumaran et al., `…/voisins-panin/pdf/2507.03120v1.pdf` | `5fa3b66737857f92fed9315adbdb4cbfb95e36d2366295c2a4f61a8448f0530c` (égale au manifeste de la note de Panin) | p. 4 et p. 14 seulement (comparaison) |
| page de résumé de 2508.15815, `…/voisins-panin/telechargement/abs-2508.15815.html` | `841966cb5aebeccf04f8748e38f509a537d1a03f07dc918a4ba6984a3aaa3107` (égale au manifeste de la note de Panin) | résumé de v3 (comparaison) |
| brouillon 5 : `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` | `9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969` (égale au compagnon) | l. 55 à 130 (verrous et champs), l. 215 à 275 (hypothèse, pièces revendiquées), l. 325 à 345 (contre-indices), l. 686 à 700 (familles), l. 926 à 942 (contre-lecture) ; recherche de mots (« Kumaran », « 2,58 », « Weng », « Zhu ») |
| configuration `…/brouillon5/papier-C-config-v1-brouillon2.json` | `77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb` (égale au compagnon) | champ `vivier` seulement (forme des intensités, surtout `approbations_forgees`) |
| `R/docs/decisions/decision-N-005-N-006-v1.md`, `decision-N-013-v1.md`, `decision-N-023-v1.md` | `cd49afbc…`, `157d388e…`, `1297f509…` (égales aux compagnons) | N-005 section 1 ; N-013 sections 1 et 2 ; N-023 en entier |
| note de Bajaj et Tiganj (brouillon), `R/docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md` | `9beecd71485678fd5d894825e1223fca42ca3a9dcb9fd24b7dea8388a7e062a5` (égale au compagnon) | en entier (identifiant de Zhu et al. cherché, absent) |
| `R/docs/sources/pdf/2602.13568v1.pdf` (Bajaj et Tiganj) | `eca410e0375d9cfb23f334f85b93d073c0157ffe88960cd4a7884c5f38499da8` (égale au compagnon) | p. 1, p. 6 et p. 7 (mentions et références de Weng et al. et de Zhu et al.) |

Recherche par identifiant et par titre (sans lecture), dans des fichiers nommés un à un, sans recherche récursive :
`R/registres/veille.md` (`bd1e34ce…`), `R/docs/etat-de-l-art-controle-ia-v1.md` (`a7d6846d…`),
`R/docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md` (`b0b519fe…`) et `-niveau2-v1.md` (`bbe0c1f5…`),
`R/docs/programme-controle-ia-v2.md` (`2fd63bad…`), `R/docs/notes/confrontation-projet-sycophancie-v1.md` (`b7631607…`).
Motifs : 2501.13381, « BenchForm », 2025.acl-long.195, « Conformity in large », « Weng », « Zhu et al », s42256,
« Competing Biases », 2026.findings-acl.449, « Do as we do ». Résultat : aucun n'y figure. Au brouillon 5, Kumaran et
al. n'est pas cité ; Weng et al. et Zhu et al. ne le sont qu'au verrou 2 (l. 75).

## Ce que j'ai tenu

- Écriture seulement sous `…/contre-lectures-brouillon5/voisins-restants/`. Aucune commande git. `python3 -I -B`,
  `PYTHONDONTWRITEBYTECODE=1`, scripts hors des dossiers de téléchargement, chemins passés en arguments. Aucune recherche
  récursive dans le dépôt ni dans le système de fichiers ; une seule liste récursive (`ls -R`), celle de mon propre
  dossier d'écriture, pour dresser le manifeste. Aucun sous-agent, aucune dépense, aucun compte, aucune clé affichée.
- Jamais ouverts, pas même pour une empreinte : `R/prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, tout fichier sous `R/donnees/`, `R/runs/`, `R/diag/`.
- Réseau : `export.arxiv.org` (une page de résumé), `arxiv.org` (un PDF), `aclanthology.org` (deux pages d'article, une
  page de volume, un PDF), `www.nature.com` (une seule requête, celle du PDF de l'article). Une requête de vérification de
  l'état du mandataire réseau a été refusée par la garde de l'outil avant tout envoi ; je ne l'ai pas refaite.
- **Kumaran et al., PDF de l'éditeur** : la requête directe a reçu une réponse 303 vers `idp.nature.com/authorize`
  (serveur d'autorisation de l'éditeur, autre hôte). Je ne l'ai pas suivie et je n'ai **pas** rejoué le paramètre
  `?error=cookies_not_supported` employé par la note de CP-02 : ce serait contourner l'étape d'autorisation, ce que la
  consigne exclut. Le texte intégral, en accès libre, est déjà sur disque : c'est la page de l'article reçue par la note
  de CP-02 (`fa5dfe4a…`), dont j'avais lu seulement le résumé. Je l'ai lue sans nouvelle requête. Elle a été obtenue
  par l'écart que cette note déclare et soumet à la session (CR2-03).
- Citations contrôlées par script : `outils/verifier_citations_restants_v1.py`. Chaque phrase citée doit être sur la page
  citée du PDF empreinté (ou dans la section citée de la page de l'éditeur, ou dans la page de résumé empreintée) et,
  mot pour mot, dans cette note ; le script vérifie l'empreinte de chaque source avant d'en extraire le texte (il
  extrait lui-même le texte des PDF, page par page, et celui des pages HTML). Sorties :
  `outils/verifier_citations_restants_v1.sortie.txt` (cas sain) et
  `outils/verifier_citations_restants_v1.artefact.sortie.txt` (garde R5 : un chiffre altéré, une bonne phrase à la
  mauvaise page, une source à l'empreinte altérée, une phrase absente de la note doivent être refusés ; une bonne phrase
  acceptée). Bilan : 104 citations contrôlées (pages des deux PDF ; sections de la page de l'éditeur ; p. 4 et p. 14 de
  la préimpression de Kumaran et al. ; p. 1 et p. 7 de Bajaj et Tiganj ; pages de résumé ; ancres des corrections dans
  le brouillon 5, la configuration, la note de Panin et la note de CP-02), 0 échec ; 16 d'entre elles appuient une
  paraphrase française et ne sont contrôlées que sur la source. Sur les artefacts : 7 cas conformes sur 7 (2 acceptés,
  5 refusés, comme attendu). Le recoupement de tous les segments entre guillemets de la note avec toutes les sources
  liste les introuvables : phrases françaises, mots cherchés, corrections proposées.
- Résumés et comparaison des résumés de Pan et al. : `outils/extraire_resumes_restants_v1.py`, sortie
  `outils/extraire_resumes_restants_v1.sortie.txt`.
- Revendications confrontées : énoncés retenus de HC1 (N-005, section 1 ; N-013, section 1 ; N-023, section 1), HC2 et
  HC2b, HC3 (N-013, section 2), tels que le brouillon 5 les reprend (l. 226 à 272) ; pièces revendiquées (l. 270 à
  272) : « la destination libre ĉ, testée contre la cible de l'attaquant et contre la moyenne du corpus, comparée entre
  familles, dans des moniteurs de contrôle sous attaque, par régression sur plusieurs intensités par famille ;
  l'opposition juge / sonde ; pour HC3, les deux composantes ci-dessus. »

## Verdict

- **Kumaran et al., version publiée (Nature Machine Intelligence, 2026 ; corps lu) : pas de collision.**
- **Pan et al., version publiée (Findings of the ACL 2026 ; résumé publié) : pas de collision.** Le résumé publié est
  celui de v3, au tiret près.
- **Weng, Chen et Wang (2501.13381v2, ICLR 2025 ; PDF : corps et annexes A à G) : pas de collision.**
- **Zhu, Zhang, Stafford, Collier et Vlachos (ACL 2025, 2025.acl-long.195 ; PDF entier) : pas de collision.**

Aucun des quatre n'étudie un moniteur de contrôle dont on lit le verdict sous attaque. Aucun n'estime une destination
libre ni n'a de nul de retour à la moyenne du corpus : les deux déclencheurs de la réserve de N-005 manquent. La cible
est toujours imposée : l'option conseillée (Kumaran et al.), la réponse de la majorité (Weng et al., Zhu et al.). Aucun
n'a de sonde d'activations ; aucun n'a d'ordre en bande ni d'usurpation du style de l'instructeur. La porte GC n'est pas
déclenchée. Ce verdict ne vaut que pour ces sources, aux niveaux de lecture du tableau (R8) : les pièces revendiquées ne
sont pas trouvées dans les sources lues.
Le plus proche reste Kumaran et al. : intensités graduées (exactitude annoncée), régression, lecture par les logits,
référence bayésienne ; la version publiée remplace DeepSeek 7B par DeepSeek-V3, ajoute Llama-3.1-70B-Instruct et une
expérience en plusieurs tours, et change un chiffre (2,58 devient 2,17), sans changer la nature du dessin. Les jeux à
quatre options et le modèle bayésien transféré étaient déjà dans la préimpression. Zhu et al. et Weng et al. sont des précédents de
la forme « nombre d'approbateurs gradué, vers une cible imposée », hors moniteur, comme Bajaj et Tiganj, déjà cités ;
Zhu et al. lisent aussi les logits.
Constats : 0 critique, 0 majeur, 6 mineurs, 2 de forme, 4 d'information.

## Kumaran et al., version publiée — ce que le corps mesure

- **Dessin** [Main] : « we focus on a binary choice scenario ». Le conseiller est fictif [légende de la figure 1] :
  « Note that the advice LLM did not actually exist—its accuracy and recommended answers were strictly defined by the
  experimental condition, rather than reflecting genuinely grounded advice. » Pas d'attaquant ; conseil même, opposé
  ou neutre.
- **Quatre options aussi** [Datasets] : SimpleQA et GSM-MC en choix à quatre options, comme dans la préimpression
  (2507.03120v1, p. 4 : « c) SimpleQA dataset(2000 questions used) ») ; « Accuracies of the Advice LLM in this experiment
  were 25%, 40%, 55%, 70%, 85% and 100%. » La direction reste imposée (l'option du conseiller ;
  [Design and motivation of the experimental paradigm] : « a randomly selected different answer in multiple choice »).
- **Modèles** [Models] : « The following models were tested: Gemma 3 12B, Gemma 3 27B, GPT4o, GPT o1-preview, DeepSeek
  671B and Llama 70B Instruct. » ; « We queried meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo (70B parameters) through
  Together.ai. » La préimpression listait « DeepSeek R1 (deepseek-llm-chat-7b via hugging face) » (2507.03120v1, p. 4).
  Aucun de nos juges. Ajout de la version publiée : une expérience en plusieurs tours [Choice-supportive bias depends on
  self-ownership of the initial answer] : « Additional validation comes from a multiturn experiment ».
- **Lecture** [Models] : « When log-probabilities were available, we computed p(a) and p(b) from the model’s next-token
  distribution at the position immediately after a fixed answer prefix » ; calibrée par une température fixe
  [Model calibration] : « This resulted in an optimal scaling temperature for Gemma 3 12B of 3.3 ».
- **Intensité et régression** [Effect of choice-supportive bias on change of answer rate] : « Higher advice accuracy
  predicted increased CoM rates in Opposite Advice conditions » ; régression en deux temps [Two-stage regression
  analysis] : « we fitted a no-intercept linear model with dummy variables for all six conditions ». Seuil, inchangé
  depuis la préimpression [Link between initial confidence and CoM] : « it was 0.77, 0.92 and 0.96 for accuracy levels
  of 50%, 60% and 70% ».
- **Référence normative, chiffre changé** [Ideal observer analysis—evidence from the magnitude and profile of confidence
  updates] : « observed confidence update/Bayesian update ratio 2.17 (calculated across all accuracies; Methods,
  P < 0.0001) ». La préimpression écrivait « observed confidence update / bayesian update ratio = 2.58 » (2507.03120v1,
  p. 14). Le brouillon 5 ne cite ni l'un ni l'autre.
- **Modèle transféré** [Validation of core findings across models and additional datasets] : « a Bayesian model
  incorporating choice-supportive bias and asymmetric advice weighting, fitted on a complex factuality dataset
  (SimpleQA), transferred with frozen parameters to a mathematical reasoning dataset » (déjà dans la préimpression) : un
  modèle de la mise à jour vers l'option conseillée, pas une destination estimée.
- **Condition de base** [Effect of choice-supportive bias on change of answer rate] : « any change of answer observed
  arises from the combination of variance due to sampling and the model’s sensitivity to minor prompt perturbations » :
  analogue de notre condition sans attaque, sans plus.
- **Limite des auteurs** [Discussion] : « It will be interesting to examine if our account extends to more naturalistic
  user–LLM interactions where free form answers are involved. »
- **Confrontation** : réponses à des questions à deux ou quatre options ; direction imposée ; la référence est la
  postérieure bayésienne calculée depuis l'exactitude annoncée, pas une destination estimée ; aucun nul de moyenne du
  corpus ; aucun moniteur, aucun attaquant, aucune famille d'attaque ; aucune sonde (« computational modelling » désigne
  un modèle bayésien du comportement). Rien de HC1 à HC3. Précédent, déjà relevé pour la préimpression (CP-03 de la note
  de Panin), d'une régression sur des intensités graduées lue par les logits, hors moniteur.

## Pan et al., version publiée — contrôle du résumé

- **Page lue** : `telechargement/acl-2026.findings-acl.449/page-2026.findings-acl.449.html` (`f85f46dd…`). Titre,
  six auteurs dans l'ordre de v3, « Findings of the Association for Computational Linguistics: ACL 2026 », pages 9218 à
  9241 (24 pages, comme v3), daté 2026/7 dans les métadonnées.
- **Comparaison** (`outils/extraire_resumes_restants_v1.sortie.txt`) : 222 mots de part et d'autre ; seules différences,
  trois « user-assistant » de v3 écrits « user–assistant » (tiret moyen). Résumé publié : « We introduce a task-agnostic
  benchmark UserAssist and evaluate such bias in 52 frontier models. » ; « We find that human-preference alignment
  amplifies user bias, while reasoning fine-tuning reduces it. »
- **Verdict** : pas de collision au niveau du résumé publié ; il ne dit rien de plus que v3, lue en entier par la note de
  Panin (vraies étiquettes de rôle, aucun moniteur, aucune destination, aucune sonde). Le corps publié n'est pas lu
  (borne de la consigne) ; je ne vois pas de motif de le lire (R8).

## Weng, Chen et Wang — ce que le papier mesure

- **Objet** (p. 1) : « This paper presents a comprehensive study on conformity in LLM-driven multi-agent systems,
  focusing on three aspects: the existence of conformity, the factors influencing conformity, and potential mitigation
  strategies. » Questions à choix multiples tirées de BIG-Bench Hard (p. 3 : « The resulting dataset comprises 3,299
  multiple-choice questions. »).
- **Protocoles** (p. 3) : réponse seule, majorité juste, majorité fausse, puis « confiance » et « doute » construits par
  des tours antérieurs ; « Wrong Guidance Protocol (Fig. 2c) is the inverse of the Correct Guidance protocol. » ; (p. 4)
  « For the Correct Guidance and Wrong Guidance protocols, six additional agents are introduced to provide either correct
  or incorrect responses, respectively. » Les pairs n'écrivent que leur choix, en 21 tournures (p. 18).
- **Mesure** (p. 5) : « CRP represents the proportion of questions that are originally answered correctly but are
  answered incorrectly when P is applied. » Taux binaires par question.
- **Intensité graduée** (p. 6) : « As shown in Fig. 5cd, increasing the majority size results in greater conformity, and
  this effect is more pronounced than that of increasing the interaction time. » ; non linéaire : « Notably, the change
  from a majority size of 5 to 6 leads to a dramatic shift. » ; (p. 7) « the absence of dissenting opinions increases
  peer pressure to conform » ; et « Interestingly, Qwen2-72B exhibits a contrasting trend ». La taille de la majorité
  est variée en gardant six pairs (p. 6 : « Here we focus on scenarios where the additional agents hold distinct
  opinions. »), donc en ajoutant des dissidents. Niveaux lus un par un ; aucune régression.
- **Modèles** (p. 4) : « We conduct experiments on 11 popular LLMs » ; (p. 17) « For open-source LLMs, we use the default
  temperature setting provided by Ollama » ; versions quantifiées sur 4 bits (« instruct-q4 0 » dans le texte extrait,
  p. 17) ; Llama3.1-8B et Qwen2-7B en sujets (p. 6, tableau 3).
- **Juge auxiliaire** (p. 22) : « We use Llama3.1-405B to classify the answers of Llama3-70B and Qwen2-72B, followed by a
  manual sampling inspection to ensure accuracy. » Il classe des entretiens, hors pression.
- **Contre-mesures** (p. 7 et p. 8) : persona « indépendant » en consigne système et consigne de réflexion ; (p. 23) « You
  are a thoughtful and independent thinker. » Voisin de HC5 (CR2-12).
- **Limite déclarée** (p. 10) : « Moreover, the use of multiple-choice questions simplifies the scenarios in which LLMs
  are typically applied, potentially limiting the generalizability of our findings. »
- **Confrontation** : un agent qui répond, pas un moniteur qui note ; cible imposée (la réponse de la majorité) ; taux
  binaires ; taille de majorité graduée mais lue niveau par niveau, sans loi ni destination ; aucun nul de moyenne du
  corpus ; aucun attaquant au sens du contrôle (les pairs sont fixés par le protocole) ; aucune sonde ; aucun ordre au
  sujet. Rien de HC1 à HC3. Précédent de la forme « nombre d'approbateurs », hors moniteur (CR2-05).

## Zhu, Zhang, Stafford, Collier et Vlachos — ce que le papier mesure

- **Objet** (p. 1 = 3854) : « Notably, we are the first to show that LLMs are more likely to conform when they are more
  uncertain in their own prediction. » Expérience d'Asch adaptée en dialogue de questions-réponses (p. 3 = 3856) :
  « When p > 1, the model is the pth participant to answer the question, with all preceding p − 1 confederates
  unanimously expressing c as their answer. »
- **Intensité graduée** (p. 15 = 3868) : « We incrementally introduce a varying number of simulated participants
  (ranging from 2 to 10), who unanimously provide incorrect answers in the dialogue. » ; (p. 4 = 3857) « The resistance
  level RLp (shown in green) gradually decreases, while the conformity level CLp (shown in red) increases as the number
  of confederates grows. » Taux binaires (équations 1 et 2, p. 3) ; niveaux lus un par un ; aucune régression sur le
  nombre de pairs.
- **Ton des pairs** (p. 5 = 3858) : « Comparing Plain and Neutral, we find that the Neutral setting consistently
  increases the conformity level. » ; « Comparing Neutral, Uncertain and Confident expressions, we find Confident
  consistently increases conformity. » ; « In contrast, for Mistral and Qwen2, Uncertain expressions increase
  conformity. » Quatre tons, catégoriels (tableau 1, p. 3).
- **Modèles** (p. 4 = 3857) : « Models. We use Llama-3-8B (Meta, 2024), Mistral-v0.3-7B (Jiang et al., 2023), Qwen2-7B
  (Yang et al., 2024a), and Gemma2-9B (Gemma et al., 2024). » Versions de base et instruites ; « We apply greedy
  decoding to generate the answers. » La figure 4 (p. 5) nomme « Mistral-7B-Instruct-v0.3 », un de nos juges, en sujet.
- **Probabilités et incertitude** (p. 6 = 3859) : « For MMLU, we measure confidence using the log probability of the
  option » ; « Our results indicate that the model’s initial confidence is a key predictor of whether it will conform on
  a given question. » ; difficulté : « Figure 6 supports this by showing a strong negative correlation (−0.777) between
  task accuracy and the conformity level. » Lecture des logits selon le nombre de pairs (p. 17 = 3870) : « Figure 12:
  Logits of Llama-3-8B-Instruct on MMLU with different settings. » (figure descriptive, cible imposée).
- **Contre-mesures** (p. 6 à p. 8) : « avocat du diable » (un pair dissident de plus) et « distillation de la question »,
  où l'organisateur résume la majorité (p. 7 = 3860, tableau 2 : « Organiser: All participants before you have chosen
  $B$ as the answer. ») ; la conformité baisse. C'est la vraie voix de l'organisateur du dialogue, pas une imitation dans
  un contenu noté.
- **Fiabilité** (p. 15 = 3868) : « Consequently, multiple runs were not conducted, as they would yield the same outputs
  under this setup. » Limite (p. 9 = 3862) : « Our use of controlled, artificial Q&A dialogues may not fully capture the
  complexity of real-world interactions. »
- **Confrontation** : un modèle qui répond, pas un moniteur ; cible imposée (la réponse unanime des pairs) ; taux
  binaires ; nombre de pairs gradué de 1 à 9 sans loi ni destination ; aucun nul de moyenne du corpus ; aucun
  attaquant ; aucune sonde (la carte d'attention du tableau 2 lit le modèle qui répond) ; aucun ordre. Rien de HC1 à HC3.
  Précédent de la forme « nombre d'approbateurs » lue aussi par les logits, hors moniteur (CR2-05) ; indice contraire à
  CP-05 (i) sur l'emphase (CR2-06).

## Confrontation aux pièces revendiquées

| pièce (énoncés retenus) | Kumaran, version publiée (corps) | Pan, version publiée (résumé) | Weng 2501.13381v2 | Zhu 2025.acl-long.195 |
|---|---|---|---|---|
| HC1 : destination ĉ estimée librement | non : option conseillée imposée [Datasets ; Design] | non | non : réponse de la majorité imposée (p. 3, p. 5) | non : réponse unanime imposée (p. 3) |
| HC1 : ĉ testée contre la cible et contre la moyenne du corpus | non : postérieure bayésienne calculée [Ideal observer] | non | non | non |
| HC1 : comparée entre familles | non | non | ampleur seulement (protocoles, p. 5) | ampleur seulement (tons, p. 5) |
| HC1 : moniteurs de contrôle sous attaque | non : réponses à des questions | non | non : agent sujet ; juge auxiliaire hors pression (p. 22) | non |
| HC1 : régression sur plusieurs intensités par famille | régression sur l'exactitude annoncée, hors moniteur, sans famille d'attaque [Two-stage regression analysis ; Validation] | non | non : taille de majorité lue niveau par niveau (p. 6) | non : nombre de pairs lu niveau par niveau (p. 4) |
| HC1 : instrument (probabilité des jetons ; cité, non revendiqué) | utilisé [Models] | log-probabilités (v3, note de Panin) | non | utilisé (p. 6 ; figure 12, p. 17) |
| HC1 et HC2 : opposition juge / sonde ; sonde de l'agent auteur | non | non | non | non (attention du modèle qui répond, p. 7) |
| HC2b : trahison par les activations | non | non | non | non |
| HC3, composante 1 : ordres en bande détectés sous « contenu = données » | non | non | non | non |
| HC3, composante 2 : style de l'instructeur sans ordre ; g > 0 juges, g nul sondes de l'auteur | non | non : vraies étiquettes de rôle (v3) | non : persona en consigne système réelle, contre-mesure (p. 23) | non : voix réelle de l'organisateur, contre-mesure (p. 7) |

## Constats

Format : identifiant, gravité, où (section et ligne du brouillon 5), ce qui est, ce qui devrait être, correction en mots
exacts. Aucun constat ne change un énoncé d'hypothèse ni une pièce revendiquée. Une collision, même partielle, serait un
nœud de Lazar : aucune n'est trouvée. Les marqueurs `<<…>>` sont à remplir par la session au versement.

**CR2-01 — mineur — verrou 2 (l. 74 et 75).**
- Ce qui est : « Même contrôle pour les deux voisins cités par Bajaj et Tiganj (Weng et al. 2501.13381 ; Zhu et al., ACL
  2025 ; note finale des voisins). » Aucun des deux n'était lu ; Zhu et al. était sans identifiant.
- Ce qui devrait être : contrôle fait, au résumé puis sur PDF ; le verrou cite la note, le verdict, la version et le
  niveau de lecture.
- Correction, mots exacts : remplacer cette phrase par « Voisins cités par Bajaj et Tiganj, contrôlés au résumé puis lus
  sur PDF par un sous-agent neuf (note `<<CHEMIN_NOTE_VOISINS_RESTANTS>>`, `<<EMPREINTE_NOTE_VOISINS_RESTANTS>>`),
  « pas de collision » pour chacun : Weng, Chen et Wang, « Do as We Do, Not as You Think: the Conformity of Large
  Language Models », ICLR 2025, 2501.13381v2 (`e730da846b97a3145a02a851d819d1c7dd37e421dc6b9a5137aa080967b3776c` ; corps
  et annexes A à G lus) ; Zhu, Zhang, Stafford, Collier et Vlachos, « Conformity in Large Language Models », ACL 2025,
  volume 1, p. 3854–3872, anthologie 2025.acl-long.195 (`a2f28bdca181af5eab10148fd7afbe2845bf163502617548870ae6b0d90d11fc` ;
  lu en entier, bibliographie exceptée). » Si CQ-01 de la note de CP-02 est appliqué, la même phrase remplace la
  phrase « Zhu et al. 2025 et Weng et al. 2025, … » qu'il garde.

**CR2-02 — mineur — verrou 2 (l. 67 à 75) ; corrections proposées par CP-01 et CP-03 (note de Panin) et CQ-02 (note de CP-02).**
- Ce qui est : CQ-02 propose d'écrire, pour la version publiée de Kumaran et al., « corps publié, en accès libre, non lu
  (R8) » et « résumé lu, corps non lu ». Le bloc de CP-03 décrit le dessin « en choix binaire ».
- Ce qui devrait être : le corps publié est lu (section ci-dessus) ; « pas de collision » ; la description couvre les
  choix à quatre options, présents dans la préimpression (p. 4) comme dans la version publiée.
- Correction, mots exacts : dans la phrase de CQ-02, remplacer « corps publié, en accès libre, non lu (R8). » par « corps
  publié lu sur la même page (texte intégral en accès libre ; information supplémentaire non lue ; note
  `<<CHEMIN_NOTE_VOISINS_RESTANTS>>`) : « pas de collision » ; il remplace DeepSeek 7B par DeepSeek-V3 et ajoute
  Llama-3.1-70B-Instruct et une expérience en plusieurs tours ; comme la préimpression, il reste orienté vers l'option
  conseillée, sans moniteur ni attaquant (R8). » ; dans le bloc de CP-03 et dans CQ-02, remplacer « version publiée dans Nature Machine
  Intelligence, 2026, non lue » (ou « résumé lu, corps non lu ») par « version publiée dans Nature Machine Intelligence,
  2026, corps lu sur la page de l'éditeur » ; dans le même bloc, remplacer « en choix binaire » par « en choix binaire
  (latitudes) et à quatre options (SimpleQA, GSM-MC) ».
- Les pages citées restent celles de la préimpression empreintée (R7) : la page de l'éditeur n'a pas de pages. Les faits
  cités par CP-03 et CP-05 (iii) sont dans le corps publié (seuils 0,77, 0,92 et 0,96 inchangés). Seul chiffre changé
  lu : le rapport à la mise à jour bayésienne, 2,58 dans la préimpression (p. 14), 2,17 au corps publié ; aucun texte
  proposé ne le reprend. Ne pas le citer sans dire la version.

**CR2-03 — mineur — provenance du corps publié de Kumaran et al. (réserve, verrou 2).**
- Ce qui est : la page lue (`fa5dfe4a…`) a été obtenue par la note de CP-02 avec le paramètre
  `?error=cookies_not_supported`, après une réponse 303 vers le serveur d'autorisation de l'éditeur ; cette note
  déclare l'écart et le soumet à la session. Ma requête du PDF a reçu la même réponse 303 (octet pour octet) ; je ne
  l'ai pas contournée. L'information supplémentaire (méthodes et résultats détaillés) est servie par un autre hôte, non
  permis : non lue.
- Ce qui devrait être : la session juge l'écart. S'il est accepté, la lecture du corps tient. S'il est refusé, la
  version publiée de Kumaran et al. n'est lue qu'au niveau de la préimpression (corps lu par la note de Panin), et le
  texte le dit.
- Correction, mots exacts, au verrou 2, à la suite de la phrase de CR2-02 : « Page de l'éditeur reçue après une
  redirection vers son serveur d'autorisation, par la requête déclarée en écart par la note `<<CHEMIN_NOTE_VOISINS_CP02>>`
  (décision de la session : `<<DECISION_ECART_EDITEUR>>`) ; PDF de l'éditeur non téléchargé. »

**CR2-04 — mineur — verrou 2 (liste de CP-06) ; CP-01 (note de Panin), « Même écart, de moindre risque, pour Pan et al. » ; CQ-02, « Hors de ma consigne ».**
- Ce qui est : la version des Findings of the ACL 2026 de Pan et al., citée par Panin, n'était pas contrôlée.
- Ce qui devrait être : contrôlée au résumé ; le verrou le dit.
- Correction, mots exacts : dans la liste proposée par CP-06, remplacer « Pan et al. 2508.15815v3 » par « Pan et al.
  2508.15815v3 (version publiée : Findings of the ACL 2026, p. 9218–9241, anthologie 2026.findings-acl.449 ; résumé
  publié contrôlé, égal à celui de v3 au tiret près ; « pas de collision » ; note `<<CHEMIN_NOTE_VOISINS_RESTANTS>>`) ».

**CR2-05 — mineur — HC1, « Précédents cités », ajouts (après la l. 262, ou à la suite du bloc de CP-03) ; « Familles et échafaudage » (l. 692 à 694).**
- Ce qui est : Bajaj et Tiganj sont cités pour une pression graduée par la taille du groupe (l. 250 à 254). Les deux
  études qu'ils citent pour l'effet de conformité, dont l'une lit aussi les logits, ne le sont pas. Or la famille
  « approbations forgées » gradue ses rangs par le nombre d'approbateurs (configuration, `vivier.approbations_forgees`,
  du « A colleague read {OBJET} and liked it. » au dernier rang, où cinq instances indépendantes approuvent).
- Ce qui devrait être : cités comme publiés, avec pages et limites ; leurs grilles citées à côté de celle de Kim et
  Flanigan.
- Correction, mots exacts, après la l. 262 (à la suite des blocs de CV-03 et CP-03, s'ils sont retenus) : « - **voisins
  de Bajaj et Tiganj** (note `<<CHEMIN_NOTE_VOISINS_RESTANTS>>` (`<<EMPREINTE_NOTE_VOISINS_RESTANTS>>`), conclusion
  « pas de collision » ; aucun énoncé changé, aucune prédiction prise ; ajout de routine, consigné :
  `<<DECISION_VOISINS>>`) : - nombre de pairs unanimes gradué de 1 à 9, sur quatre modèles de 7 à 9 milliards de
  paramètres (dont Mistral-7B-Instruct-v0.3) qui répondent à des questions ; la conformité croît avec le nombre de pairs,
  plus encore sous un ton assuré, et d'autant plus que la confiance initiale, lue par la probabilité de l'option, est
  basse ; cible imposée (la réponse des pairs), taux binaires, niveaux lus un par un, aucune destination estimée, aucun
  moniteur de contrôle (Zhu et al., ACL 2025, 2025.acl-long.195,
  `a2f28bdca181af5eab10148fd7afbe2845bf163502617548870ae6b0d90d11fc`, p. 3856 à 3859 et 3868) ; - taille de la majorité
  graduée de 3 à 6 sur six pairs (protocoles « confiance » et « doute »), chez des agents qui répondent à des questions à
  choix multiples ; la conformité croît avec la taille, avec un saut au passage à l'unanimité, mais pas chez tous les
  modèles ; cible imposée, taux binaires, aucune destination, aucun moniteur (Weng, Chen et Wang, ICLR 2025, 2501.13381v2,
  `e730da846b97a3145a02a851d819d1c7dd37e421dc6b9a5137aa080967b3776c`, p. 4 à p. 7). »
- Correction, mots exacts, à la fin de la phrase sur Kim et Flanigan (l. 694, après « (p. 4). », et après l'ajout de
  CP-03 s'il est retenu) : « Nombre de pairs unanimes de 1 à 9 (Zhu et al., p. 3868) ; taille de majorité de 3 à 6
  (Weng et al., p. 6) ; niveaux lus un par un, cible imposée. »

**CR2-06 — mineur — contre-indices déclarés (l. 325 à 344) ; contre-indice (i) proposé par CP-05 (note de Panin).**
- Ce qui est : CP-05 (i) propose de déclarer qu'une assertion très certaine déplace moins qu'une assertion nue (Hussain
  et Nielbo). Zhu et al. trouvent l'inverse dans un dessin voisin : le ton assuré fait monter la conformité chez les
  quatre modèles, dont un de nos juges ; le ton incertain la fait baisser chez deux et monter chez deux (p. 5 = 3858,
  figure 4).
- Ce qui devrait être : si CP-05 (i) est retenu, l'indice contraire est déclaré avec lui (R4, symétrie) ; les deux
  ensemble ne disent pas le sens de l'emphase pour les rangs hauts des familles 2 et 5.
- Correction, mots exacts, à la fin du contre-indice « Emphase et nombre » de CP-05 (avant « rapporté, sans verdict ») :
  « En sens contraire, sous des pairs unanimes, un ton assuré fait monter la conformité chez quatre modèles de 7 à
  9 milliards de paramètres, dont Mistral-7B-Instruct-v0.3, et un ton plus naturel aussi ; le ton incertain la fait
  baisser chez deux modèles et monter chez deux autres (Zhu et al., ACL 2025, p. 3858, figure 4). Indices mêlés sur
  l'emphase ; » Si CP-05 n'est pas retenu, déclarer seul : « - Ton des approbateurs : sous des pairs unanimes, un ton
  assuré fait monter la conformité chez quatre modèles de 7 à 9 milliards de paramètres, dont Mistral-7B-Instruct-v0.3
  (Zhu et al., ACL 2025, p. 3858, figure 4) ; hors juge, cible imposée ; rapporté, sans verdict. »

**CR2-07 — forme — section « Contre-lecture » (l. 930 à 932) ; champs du scellement (l. 121 et 122).**
- Ce qui est : ni cette lecture, ni son verdict, ni sa note n'ont de place au texte.
- Ce qui devrait être : la note est citée par chemin et empreinte (R6).
- Correction, mots exacts : à la fin du paragraphe « Contre-lectures des notes de lecture » (l. 932), ajouter :
  « Contrôle des voisins restants du verrou 2, par un sous-agent neuf : corps de la version publiée de Kumaran et al.
  (page de l'éditeur), résumé publié de Pan et al. (anthologie de l'ACL), Weng et al. 2501.13381v2 et Zhu et al.
  2025.acl-long.195 lus sur PDF ; note `<<CHEMIN_NOTE_VOISINS_RESTANTS>>` (`<<EMPREINTE_NOTE_VOISINS_RESTANTS>>`) ;
  « pas de collision » pour chacun ; traitement de chaque constat. » L. 121-122 : si CR2-05 est retenu, la liste entre
  parenthèses proposée par CV-08 et allongée par CP-06 et CQ-06 s'allonge de « ; Zhu et al. ; Weng et al. ».

**CR2-08 — forme — registre de veille.**
- Ce qui est : aucun des quatre n'est dans `R/registres/veille.md` ni dans les états de l'art cherchés (en-tête).
- Ce qui devrait être : quatre lignes de routine.
- Correction : une ligne par papier : identifiant et version, niveau de lecture, « pas de collision avec HC1 à HC3 »,
  note `<<CHEMIN_NOTE_VOISINS_RESTANTS>>` (`<<EMPREINTE_NOTE_VOISINS_RESTANTS>>`) ; Zhu et al. et Weng et al. signalés
  aussi pour HC5 (CR2-12) ; Kumaran et al. avec la réserve CR2-03.

**CR2-09 — information — contre-indice « Déférence mesurée là seulement où le juge est incertain » (l. 342 à 344 ; CP-05 (iii)).**
- Zhu et al. appuient ce contre-indice : la confiance initiale, lue par la probabilité de l'option, prédit la
  conformité, et la conformité croît avec la difficulté des sujets (p. 6 = 3859). Le corps publié de Kumaran et al.
  garde le seuil de la préimpression [Link between initial confidence and CoM]. Aucune correction exigée ; si CP-05
  (iii) est retenu, on peut ajouter après « (Hussain et Nielbo, p. 6) » : « ; la confiance initiale, lue par la
  probabilité de l'option, prédit la conformité à une majorité (Zhu et al., ACL 2025, p. 3859) ».

**CR2-10 — information — nos juges dans ces papiers.**
- Mistral-7B-Instruct-v0.3 : Zhu et al., en modèle qui répond, décodage glouton (p. 4 et p. 5). Llama-3.1-8B (instruit,
  quantifié sur 4 bits par Ollama) : Weng et al., en sujet (p. 6, tableau 3 ; p. 17). Llama-3-8B-Instruct (pas 3.1) et
  Qwen2-7B-Instruct (pas 2.5) : Zhu et al. ; Qwen2-7B : Weng et al. Kumaran et al., version publiée : aucun (Llama-3.1
  en 70B seulement). Pan et al. : Llama-3.1-8B-Instruct et Qwen2.5-7B-Instruct (v3, déjà relevé par CP-07).
- Jamais en moniteur de contrôle ; à ne pas citer comme tel. Aucun chiffre de ces papiers n'entre dans une puissance ni
  dans un seuil (N-023, section 1).

**CR2-11 — information — fiabilité.**
- Kumaran et al., version publiée : rapport à la mise à jour bayésienne changé de 2,58 (préimpression, p. 14) à 2,17 ;
  liste de modèles changée (DeepSeek-V3 à environ 671 milliards de paramètres au lieu de « deepseek-llm-chat-7b ») ; le
  texte écrit « from 12B to 675B parameters » [Validation of core findings across models and additional datasets] pour
  un modèle décrit à « ~671B » [Models] ; o1-preview sans logits ; information supplémentaire non lue.
- Weng et al. : modèles ouverts quantifiés sur 4 bits, température par défaut d'Ollama (p. 17) ; trois passes (p. 11 :
  « To ensure reproducibility, we conduct the experiments on BENCHFORM three times. ») ; « 11 LLMs » (p. 4 et
  p. 18) contre « Table S3: Full results (%) of all the 12 LLMs » (p. 19) ; légende de la figure S8 « empowered doubles »
  pour la réflexion (p. 26) ; taille de majorité variée en ajoutant des dissidents, ce qui mêle taille et unanimité.
- Zhu et al. : une seule passe gloutonne, sans intervalle (p. 15) ; « Mistrial-7B-v0.3 » (p. 15) ; le résumé de
  l'anthologie (« state-of-the-art LLMs ») diffère de celui du PDF (« popular LLMs », p. 1) ; renvoi au « Table 6 » pour
  le tableau 2 (p. 8).
- Conséquence : citer en qualitatif ; aucun chiffre de ces papiers dans une puissance ni dans un seuil.

**CR2-12 — information — hors des pièces revendiquées : HC5 et HC3.**
- HC5 (contre-mesures) : un dissident ajouté (« avocat du diable ») et un résumé de la majorité par l'organisateur (Zhu
  et al., p. 6 à p. 8) ; persona indépendant en consigne système et consigne de réflexion (Weng et al., p. 7, p. 8,
  p. 23). À signaler à la veille de HC5, sans verdict ici.
- HC3 : la « distillation » de Zhu et al. fait parler l'organisateur réel du dialogue pour résumer la majorité, et la
  conformité baisse ; ce n'est ni un ordre, ni une imitation de l'instructeur dans un contenu noté. Aucune correction.
