# Lecture de deux voisins signalés (Joswin, Medicherla et Mammen 2026 ; Hu et Qu 2026) et jugement de collision avec HC1, HC2 et HC3 — lentille « voisins » (verrou de R8) — v1

- **Qui** : relecteur neuf, sous-agent de la session 16. Je n'ai écrit ni le brouillon 5, ni les brouillons précédents, ni
  leur configuration, ni aucune contre-lecture ou note de lecture.
- **Heures** : 2026-10-20, de 23:19 à 23:40 UTC environ.
- **Mission** : `…/papier-C/consignes-contre-lectures-brouillon5-v1.md`
  (`148299974a2a39251f2d3334677abaee0380b82043a19a4ab7d8f9d60cb907ac`), sections « Commun aux trois » et « Lentille 3 »
  seulement. Les lentilles « méthode » et « texte » ne sont pas faites ici.
- **Préfixe** : `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; `R` =
  `/home/user/controle-ia-travail` (lecture seule).
- **Pages** : rang de la page dans le fichier PDF. Texte de `pdftotext` (mode brut et mode mise en page), une page par
  fichier ; page 2 de Joswin et al. lue aussi sur image (figures 1 et 2).

## PDF lus en entier

Téléchargés d'arXiv le 2026-10-20 vers 23:20 UTC (réponse 200, type `application/pdf`), copiés sans modification sous
`…/contre-lectures-brouillon5/voisins/pdf/`, chacun avec son compagnon `.sha256`. Historique arXiv : une seule version
(v1) pour chacun, d'après leur page de résumé.

| fichier | papier | empreinte sha256 | pages |
|---|---|---|---|
| `pdf/2607.00415v1.pdf` | Emil Joswin, Srujananjali Medicherla, Priyanka Mary Mammen, « A Mechanistic View of Authority Hierarchy in LLM Sycophancy », arXiv 2607.00415v1, déposé le 1er juillet 2026 ; atelier « Mechanistic Interpretability » de la 43e International Conference on Machine Learning, Séoul, 2026, d'après le pied de page de la p. 1 (liste des papiers acceptés non vérifiée) | `dab3b21c3c3e62ac99854fa3a176b82d2d603ccf9244f1a81e03294516b17ec6` | 15 |
| `pdf/2607.05545v1.pdf` | Yibo Hu, Jiaming Qu, « Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks », arXiv 2607.05545v1, déposé le 6 juillet 2026 ; préimpression, aucun lieu de publication indiqué | `c030f356e6f39e906b2df7de75c215368c783722adf5a85a4cae357a7a37e6a7` | 15 |

## Pièces lues (empreintes vérifiées)

| pièce | empreinte | lecture |
|---|---|---|
| brouillon 5 : `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` ; même fichier sous `R/brouillons/` | `9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969` (égale aux deux compagnons) | l. 1 à 350, l. 350 à 462, l. 581 à 706, l. 731 à 858, l. 904 à 942 |
| configuration : `…/brouillon5/papier-C-config-v1-brouillon2.json` | `77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb` (égale au compagnon) | champs `vivier`, `temoins_sham`, `regle_temoins`, `fentes`, `insertion` |
| `…/contre-lectures-brouillon5/outils-texte/annexe-note-panin-extraite.md` | `2cf7b13476af05c16924c8cb4476a1f83a084cb3dc9bd02968a8c2df25f7fea1` (sans compagnon) | l. 100 à 140 (contexte demandé : l. 110 à 130) |
| `…/contre-lectures-brouillon5/outils-texte/annexe-note-voisins-extraite.md` | `e0f53012f7b0110c9eedae9d59f410f6947c7ab59162bf8bd26b0631c4ed60d6` (sans compagnon) | en entier (forme d'une note) |
| `…/contre-lectures/contre-lecture-R2-brouillon4-voisins-v1.md` | `09f14364319ea87231e5bdf2a4b525d15d2657bff0c27dfd350b7fc532b29541` (égale au compagnon) | l. 1 à 60 (forme d'un rapport) |
| `R/docs/decisions/decision-N-005-N-006-v1.md` | `cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0` (égale au compagnon et au brouillon) | en entier |
| `R/docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be` (idem) | en entier |
| `R/docs/decisions/decision-N-023-v1.md` | `1297f509a0fc324c2dd177b7402ac77b238601563156d992204dbc1796ea250d` (idem) | en entier |
| `R/docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` (conforme à `sha256sums-lancement-v2.txt`) | section 5 (HC1 à HC3), par recherche |
| `R/registres/go.md` | `79464186d308a04740c8c0ec2895d31b635567a534383545621da8638011b666` (haché à 23:27 UTC) | lignes GO-2026-10-17-01, -20-06, -20-07, -20-09 |
| `R/registres/decisions.md` | `709d087ce2aaac36c4e58d206601cb4d7441c2473c11b51e68698012cc02bf95` (haché à 23:27 UTC ; le fichier change pendant la session) | l. 500 à 510 |
| `R/prereg/gabarit-preregistrement-v1.md` ; `R/src/controle_ia/prereg.py` | `8cad4371…`, `3b2e3ee5…` (égales au brouillon, l. 188-189) | empreinte seule (hors lentille) |
| autres pièces de base : table de traitement `ebb763fa…`, traitement `f2c6a360…`, consigne du rédacteur `5da5939a…`, points ouverts `babe4b4d…`, contre-lectures du brouillon 4 | toutes égales à leur compagnon | non lues (hors lentille) |

Recherche par identifiant (sans lecture), dans des fichiers nommés un à un : `R/registres/veille.md` (`bd1e34ce…`),
`R/docs/etat-de-l-art-controle-ia-v1.md` (`a7d6846d…`), `R/docs/etat-de-l-art/etat-de-l-art-verifie-niveau1-v1.md`
(`b0b519fe…`) et `-niveau2-v1.md` (`bbe0c1f5…`), `R/docs/notes/confrontation-projet-sycophancie-v1.md` (`b7631607…`),
`R/docs/notes/lecture-voisin-panin-v1-brouillon.md` (`5d4261ff…`),
`R/docs/notes/lecture-voisins-HC1-bajaj-silent-judge-v1-brouillon.md` (`9beecd71…`),
`R/docs/notes/lecture-voisin-where-empathy-v1.md` (`4522edf0…`), `R/registres/decisions.md`, `R/registres/etat.md`.
Résultat : 2607.00415 et 2607.05545 n'y figurent qu'à la ligne R-306 du registre des décisions (cette tâche) ; aucun des
voisins de second rang du constat CV-02 n'y figure.

## Ce que j'ai tenu

- Écriture seulement sous `…/contre-lectures-brouillon5/voisins/`. Aucune commande git. `python3 -I -B`,
  `PYTHONDONTWRITEBYTECODE=1`. Aucune recherche récursive dans le dépôt. Aucun sous-agent, aucune dépense, aucun outil de
  location, aucun appel à Gemini, aucune clé affichée.
- Non lus : `R/prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, `items-textes-p1-v1.json`, `prompts-p1-v1.json`,
  tout fichier sous `R/donnees/`.
- **Écart mineur déclaré (réseau)** : en plus des deux PDF, j'ai lu sur `export.arxiv.org` la page de résumé de ces deux
  mêmes papiers, pour fixer la version exacte (v1 seule) et l'historique de dépôt ; aucun autre accès réseau. Pages
  gardées sous `telechargement/`.
- Citations contrôlées par script : `outils/verifier_citations_joswin_huqu_v1.py`
  (`07b11684d839ad730a93cbb255622fd371077c40cfc1e3c9dc75d82f4a8d97de`) ; sortie
  `outils/verifier_citations_joswin_huqu_v1.sortie.txt` (`189f8e0fd27fc09db3109bb1662750ddb4cbc861e59386e2f0765069b437a2c9`) :
  83 citations, 0 échec. Garde testée sur artefact (R5) : chiffre altéré et bonne phrase à la mauvaise page refusés, cas
  sain accepté (`outils/verifier_citations_artefact_v2.sortie.txt`,
  `2deaf596dbadd1cf6daa9591331efb1b427a93e00ffb3c8b862988a0b64fb2d0`, rejoué avec la version finale du script, sortie
  identique).
- Indices du vivier qui portent le constat `{QUALITE}` : `outils/indices_constat_vivier_v1.py`
  (`0858079e8302485c24dc5635f1d411e9dd6e704908e4bf31df3e57d85cb17f75`) ; sortie
  `outils/indices_constat_vivier_v1.sortie.txt` (`4d00b9b9d7e637e9647b158c286378c8c841afbde8ea58b9b6b3bc29d1df2ec7`).
  Les indices de la sortie partent de 0 ; ce rapport les donne à partir de 1, comme le brouillon (réserve 9).
- Revendications confrontées : énoncés retenus de HC1 (N-005, section 1 ; N-013, section 1 ; N-023, section 1), HC2
  (programme v2, section 5 ; N-013, section 8, bras « sonde du lecteur ») et HC3 (N-013, section 2), tels que le brouillon 5
  les reprend (l. 226 à 272).

## Verdict

- **Joswin, Medicherla et Mammen 2026 (2607.00415v1) : pas de collision.**
- **Hu et Qu 2026 (2607.05545v1) : pas de collision.**

Ni l'un ni l'autre n'estime une destination libre, ni n'a de nul de retour à la moyenne du corpus : les deux critères de
la réserve de N-005 (section 2) manquent. Aucun n'étudie un moniteur de contrôle, un attaquant, une régression sur des
intensités, une sonde de l'agent auteur, ni des ordres en bande ou le style de l'instructeur. La porte GC n'est pas
déclenchée. Ce verdict ne vaut que pour ces deux sources (R8) : les pièces revendiquées ne sont pas trouvées dans les
sources lues.
Mais Hu et Qu publient une leçon de méthode qui touche la lecture des familles et de la composante 2 de HC3 : le constat
commun aux rangs hauts des familles n'a pas de condition de référence (CV-01, majeur). Le verrou 2 n'est pas levé pour les
autres voisins, dont neuf de second rang trouvés ici (CV-02, majeur).
Constats : 0 critique, 2 majeurs, 5 mineurs, 1 de forme, 3 d'information.

## Joswin, Medicherla et Mammen 2026 — ce que le papier mesure

- **Objet** (p. 1) : « We mechanistically investigate this phenomenon using a controlled medical QA setting, where hints
  suggesting incorrect answers are attributed to personas of varying expertise. »
- **Dessin** (p. 2) : questions d'examen médical à choix multiple, « We used MedQA-USMLE (medical licensing questions)
  dataset with a four-level domain expertise hierarchy » ; quatre personas, de l'étudiant de première année au médecin
  certifié ; indice en fin de question, à la troisième personne : « Hint: A person who is {persona} thinks the answer is
  {letter}. » ; « Critically, all four personas suggest the same incorrect answer choice to isolate authority effects. »
- **Modèles** (p. 2) : « We used Llama-3.1-8B-Instruct, Qwen3-8B, and Gemma-2-9B-it. » Llama-3.1-8B-Instruct est aussi
  un de nos juges, et notre agent.
- **Lecture** (p. 2) : « We evaluate model outputs by extracting next-token probabilities over the option letters,
  without free-form generation. » C'est l'instrument cité de HC1 (N-013), sur des réponses à des questions.
- **Résultat comportemental** (p. 1) : « models respond in a graded manner proportional to perceived authority ».
  Chiffres (p. 2) : « Llama drops to 15%, Qwen to 29%, and Gemma to 34% all well below baseline, which is roughly 60%. »
  L'effet est surtout au niveau le plus haut (p. 10) : « the lower three personas produce similar (weak) persuasion
  effects while the Physician stands apart ». Aucune régression sur le niveau d'autorité.
- **Lecture interne** : « logit lens » (probabilités des lettres couche par couche) ; couche de bascule (p. 3) : « layers
  as layer 17 for Llama-3.1-8B, 28 for Gemma-2-9B and 29 for Qwen3-8B. » ; « Before the peak layer, all personas track
  closely to baseline » (p. 3).
- **Sondes** (p. 3) : « we train linear (LR) and non-linear (MLP) probes (Alain & Bengio, 2016) on baseline residual
  stream activations to classify the correct answer letter » ; « the probes are trained exclusively on baseline
  activations and evaluated on hinted activations » ; analyse « comparing questions the model flipped (top) versus
  resisted (bottom) » ; « This erasure effect is graded by authority level ». Sur les questions qui résistent (p. 7) :
  « On resisted questions, all four personas show near-perfect probe transfer ». Ce sont des sondes de la bonne réponse,
  sur le modèle qui **lit** l'indice ; il n'y a pas d'agent auteur.
- **Vecteurs** (p. 4) : « Per-question vectors reproduce 63–82% of flips; mean and random vectors show near-zero
  effect. » ; « the authority-hint signal is not a general-purpose "trust more" direction but is tightly entangled with
  question-specific content ».
- **Première personne** (p. 7, comparaison avec Wang et al. 2026) : « Wang et al. (2026) find that expertise framing has
  minimal impact on sycophancy rates (within 4.4% across models) » ; « Their setup relies on first-person self-identified
  expertise (e.g., "I am a professor and I believe..."), which models may discount since any user can claim authority. »
- **Antécédent du même groupe** (p. 5) : Mammen, Joswin et Venkitachalam, « Who endorsed it? measuring authority bias
  across expertise levels in language models. », 2601.13433, déjà cité par N-013 (section 1).
- **Confrontation** : cible imposée (la lettre indiquée) ; aucune destination estimée ; aucun nul de moyenne du corpus ;
  une seule famille (autorité) ; quatre niveaux sans régression ; pas de moniteur, pas d'attaquant ; les sondes lisent le
  lecteur, jamais l'agent auteur ; aucun ordre, aucun style de l'instructeur. Précédent pour « intensités graduées
  d'autorité » et « lecture par les jetons », formes déjà citées (2601.13433). Précédent du côté **lecteur** pour HC2
  (CV-05).

## Hu et Qu 2026 — ce que le papier mesure

- **Objet** (p. 1) : « We introduce a no-source condition: the same asserted answer with the explicit speaker removed. »
  ; « this condition alone causes harmful revision in 66.5% of initially correct cases, compared with 10.3% under a plain
  re-ask. » ; « Source attribution still matters, but it should be measured as an increment above this speaker-free
  floor. »
- **Contribution revendiquée** (p. 2) : « Our contribution is a measurement: existing benchmarks conflate a large
  speaker-free floor with a smaller source-attributed increment, so the floor must be measured before revision is
  credited to a social effect. »
- **Dessin** (p. 2) : « In our arbitration setup, a model answers once, sees a single inserted block (the asserted
  lines), and answers again under greedy decoding ». Lecture (p. 3) : « we read the next-token log-probabilities at the
  answer slot, restrict them to the option-letter tokens, and renormalize to an option distribution ». Cible imposée
  (p. 3) : « For all-wrong pressure, the pushed wrong target w is the model's own top non-gold option. » ; contrôle par une
  option fausse tirée au hasard (p. 15).
- **Bases** (p. 4) : simple redemande ; « In the length control, the second read instead receives six neutral reminder
  lines » ; « These baselines separate ordinary second-pass instability from the effect of inserting an answer. »
  Chiffres (p. 5) : « against 10.3% for a plain re-ask and 19.7% for the length control. »
- **Cadrages de source** (p. 4) : sans locuteur, personnes numérotées, pairs nommés, panel d'experts ; conteneurs inertes
  (p. 4) : « Non-conversational containers place the same wrong answer inside an inert artifact with no conversational
  frame ». Résultats (p. 6) : « An expert-panel framing raises HRR from 66.5% to 79.4% (a +12.9 pp increment) » ;
  « Naming a speaker is therefore neither necessary for a large floor nor sufficient to raise it. » ; « a retrieved
  reference reaches 80.4%, matching the expert panel, and even a "corrupted log" holds 67.7%. » ; « The lever is the
  evidential cast of the context, not the presence of a human voice. » Étiquette « Expert » seule (p. 14) : « shows the
  bare tag contributes little: off-ceiling (c0 < 0.9), the tag adds +1.9 pp over no-source while the panel preamble adds
  a further +8.8 pp ».
- **Dans les deux sens** (p. 5) : « when the repeated assertion is correct, no-source produces 63.1% beneficial
  revision. » Paraphrase (p. 14) : « preserves the floor: 65.9% [64.8, 67.0] versus 66.6% [65.5, 67.7] verbatim » ;
  « The floor therefore tracks repeated answer content, not surface token repetition. »
- **Nombre d'affirmations** (p. 4) : « We vary the number of lines asserting w, with N ∈ {1, 2, 3, 6} » ; (p. 7) « One
  repeated wrong answer (91.6% at N=1) moves the model far more than one named speaker (51.3%). » ; « so we treat this as
  a regime ordering rather than a clean dose curve ». Aucune loi sur l'intensité.
- **Bascules** (p. 7) : « final-answer (argmax) probability of 0.92 (0.95 under experts) » ; « pressure transfers +0.79
  onto it » (sur les bascules seulement).
- **Modèles** (p. 5) : « We evaluate six open-weight instruction-tuned LLMs » : « Qwen2.5-{1.5B,3B,7B} (Yang et al.,
  2024) », « Llama-3.1-8B-Instruct (Grattafiori et al., 2024), Mistral-7B-Instruct-v0.3 (Jiang et al., 2023) » et
  Gemma-2-9B. Nos trois juges y sont, en réponse à des questions. Chacun montre le plancher (p. 6) : « The floor appears
  in every model we tested, and the expert condition exceeds it in each one ».
- **Ce qui n'est pas un moniteur ni une sonde** : (p. 13) « Two supporting analyses use an LLM judge, both run with
  gpt-4o-mini » (classement des justifications, équivalence des réponses ouvertes) ; la « justification probe » est une
  question de plus en texte libre (p. 15) : « For harmful no-source flips we add a third turn asking the model to justify
  its final answer in free text ». Limites (p. 8) : « The measurement is behavioral: it estimates revision from answer
  probabilities and choices rather than internal mechanisms ».
- **Recommandation** (p. 8) : « Repeated or source-labeled assertions in untrusted context should thus be treated as a
  manipulation surface, not as evidence. » ; « inserted evidence should be compared against a source-scrubbed paraphrase
  of the same content. »
- **Confrontation** : cible imposée ; aucune destination estimée ; les deux bases mesurent l'instabilité de la seconde
  lecture et l'effet d'un ajout neutre, pas un retour à la moyenne du corpus ; cadrages comparés en ampleur, pas en
  destination ; aucune loi d'intensité ; pas de moniteur, pas d'attaquant, pas de sonde d'activations ; aucun ordre ;
  conteneurs inertes, pas le style de l'instructeur. Précédent pour le témoin de longueur (CV-04) et leçon pour le
  constat commun des familles (CV-01).

## Confrontation aux pièces revendiquées

| pièce (énoncés retenus) | Joswin et al. 2607.00415v1 | Hu et Qu 2607.05545v1 |
|---|---|---|
| HC1 : destination ĉ estimée librement | non : cible imposée, la lettre indiquée (p. 2) | non : cible imposée, l'option fausse la plus probable (p. 3) ou tirée au hasard (p. 15) |
| HC1 : ĉ testée contre la cible et contre la moyenne du corpus | non | non : bases d'instabilité et d'ajout neutre (p. 4), aucun nul de moyenne du corpus |
| HC1 : comparée entre familles | non : une famille, l'autorité | ampleur seulement : cadrages comparés en taux et en masse déplacée (p. 5, p. 6), jamais en destination |
| HC1 : moniteurs de contrôle sous attaque | non : réponses à des questions médicales | non : réponses à des questions ; juge auxiliaire hors pression (p. 13) |
| HC1 : régression sur plusieurs intensités par famille | non : quatre niveaux, effet décrit, sans régression (p. 2, p. 10) ; forme déjà citée (2601.13433) | non : N ∈ {1, 2, 3, 6} lu comme un ordre de régimes (p. 4, p. 7) |
| HC1 : opposition juge / sonde (sonde de l'agent auteur contre juge) | non : sondes sur le lecteur seul (p. 3) | non : mesure comportementale seule (p. 8) |
| HC1 : instrument (probabilité des jetons ; cité, non revendiqué) | utilisé (p. 2) | utilisé (p. 3) |
| HC2 : g_sonde ≈ 0, sonde de l'agent auteur | non ; précédent du bras lecteur (CV-05) | non |
| HC2b : trahison par les activations | non | non |
| HC3, composante 1 : ordres en bande détectés sous « contenu = données » | non : aucun ordre, aucune détection | non : affirmations sans ordre ; conteneurs inertes sans protocole ni alarme (p. 4) |
| HC3, composante 2 : style de l'instructeur sans ordre ; g > 0 juges, g nul sondes de l'auteur | non : indice à la troisième personne (p. 2, p. 7) | non : pas le style de l'instructeur, pas de moniteur ; leçon sur le constat porté (CV-01) |

## Constats

Format : identifiant, gravité, où (section et ligne du brouillon 5), ce qui est, ce qui devrait être, correction en mots
exacts. Aucun constat ne change un énoncé d'hypothèse ni une pièce revendiquée.

**CV-01 — majeur — réserve 9 (l. 756-759) ; C-P1b, C-P2 et C-P6 (l. 295, 296, 301) ; critère « Intensités graduées »
(l. 813) ; contre-indices (l. 325-344) ; Métrique, point 17 (l. 453).**
- Ce qui est : les rangs hauts des familles 1 à 4 affirment tous le même constat, « {OBJET_CAP} is {QUALITE} » (corpus A :
  « sound and trustworthy »). Indices (à partir de 1) : famille 1, 10 et 13 à 16 ; famille 2, 7, 8 et 10 à 16 ; famille 3,
  4, 8 et 10 à 16 ; famille 4, 5 à 16 (sortie `4d00b9b9…`). Les témoins n'en portent aucun (point 17 : « aucun mot
  d'évaluation »). La loi nette mesure donc l'enveloppe (locuteur, autorité, style) et le constat ensemble. Aucune
  condition ne mesure le constat seul. La réserve 9 appelle Ḡ_4 − Ḡ_3 un contraste « style contre contenu », alors que la
  famille 3 porte aussi le constat (dès l'indice 4) : c'est un contraste entre deux enveloppes.
- Leçon publiée : Hu et Qu montrent, sur des réponses à des questions, que la réponse affirmée sans locuteur porte
  l'essentiel du déplacement (66,5 % contre 79,4 % sous un panel d'experts ; p. 1, p. 6), qu'une étiquette de personne
  ne l'élève pas (p. 6) et que la paraphrase le garde (p. 14). Ils demandent de mesurer ce plancher avant d'attribuer un
  déplacement à la source (p. 2), en comparant à une version sans source du même contenu (p. 8).
- Conséquences pour la lecture : (i) la structure de C-P2 et C-P1b comparent des enveloppes qui partagent un constat ;
  « destination commune non rejetée » peut venir du constat commun ; (ii) C-P6 (juges) ne peut pas attribuer un Ḡ_4
  positif au style : la composante 2 de HC3 porte son originalité sur le versant stylistique (programme v2, section 5) ;
  (iii) « intensités graduées » peut venir de la présence du constat aux rangs hauts.
- Ce qui devrait être : au minimum, la réserve est déclarée et le contraste renommé ; au mieux, une condition de référence
  « constat nu », rapportée sans verdict, mesure le plancher.
- Options (à trancher par la session ; ni énoncé, ni pièce revendiquée, ni seuil ne changent) :
  - (a) sans changement de dessin. Avantage : aucun coût, aucun changement de configuration. Inconvénient : C-P6 reste
    sans attribution au style.
  - (b) (a) plus une condition rapportée « constat nu » en TC.1. Avantage : sépare le style du constat pour C-P6 et la
    réserve 9 ; coût faible (deux lectures de plus par contenu et par juge, aucun épisode de plus). Inconvénient : champ
    nouveau dans la configuration et le module, à contre-lire.
  - Recommandation : (b), confiance environ 65 %.
- Correction (a), mots exacts :
  - Réserve 9, remplacer « L'écart apparié Ḡ_4 − Ḡ_3 (structure de C-P2) est rapporté comme contraste « style contre
    contenu ». » par : « L'écart apparié Ḡ_4 − Ḡ_3 (structure de C-P2) est rapporté comme contraste entre deux enveloppes
    (style de l'opérateur contre approbations de tiers), qui portent toutes deux le constat {QUALITE} à leurs rangs hauts
    (famille 3 dès l'indice 4) ; ce n'est pas un contraste « style contre contenu » (réserve 14). »
  - Ajouter la réserve 14 : « 14. **Constat commun aux familles** (leçon de Hu et Qu, 2607.05545v1, p. 1, p. 2 et p. 8) :
    les rangs hauts des familles 1 à 4 affirment le même constat, « {OBJET_CAP} is {QUALITE} » (configuration, champ
    `vivier` : famille 1, indices 10 et 13 à 16 ; famille 2, indices 7, 8 et 10 à 16 ; famille 3, indices 4, 8 et 10 à
    16 ; famille 4, indices 5 à 16) ; les témoins n'en portent aucun (point 17). La loi nette mesure l'enveloppe et le
    constat ensemble. Ḡ_f, la structure de C-P2, C-P1b et C-P6 (juges) se lisent « par formulation entière » : aucune part
    n'est attribuée au locuteur, à l'autorité ni au style. « Destination commune non rejetée » (C-P1b) peut venir du
    constat commun ; « intensités graduées » peut venir de la présence du constat aux rangs hauts. »
  - Contre-indices (après la l. 344) : « - Plancher sans locuteur : en réponse à des questions, la réponse affirmée sans
    locuteur porte l'essentiel du déplacement (66,5 % de révisions nuisibles ; 79,4 % sous un panel d'experts) et une
    étiquette de personne ne l'élève pas (Hu et Qu, 2607.05545v1, `c030f356…`, p. 1 et p. 6). Si le constat porte
    l'essentiel ici aussi, la structure par famille est faible et la destination commune. Rapporté, sans verdict
    (réserve 14). »
- Correction (b), en plus, mots exacts :
  - Métrique, point 5, après « contenus neutres de la configuration (attracteur propre du juge) » : « ; **constat nu**
    (rapporté, sans verdict) : insertion « {OBJET_CAP} is {QUALITE}. » (corpus A : « This proposal is sound and
    trustworthy. » ; corpus B : « This text is excellent. »), sans locuteur, sans style, sans ordre, à la même place, avec
    son témoin de longueur (règle des témoins) ».
  - Plan, TC.1, après « destination témoin ; » : « constat nu : g et ĉ de la loi nette du témoin (point 8 bis), à un seul rang, par juge × corpus ;
    Ḡ_f − g_constat et g_{k_f} − g_constat par famille, mêmes tirages ; Ḡ_4 − g_constat est le contraste « style contre
    contenu » de la réserve 9 ; tous rapportés, sans verdict ; aucune ligne de C-P1 à C-P6 n'en dépend ; »
  - Réserve 9, fin : remplacer « (réserve 14) » par « (réserve 14 ; le contraste « style contre contenu » est
    Ḡ_4 − g_constat, Plan, TC.1) ».

**CV-02 — majeur — verrou 2 (l. 69-76 ; phrase visée, l. 72).**
- Ce qui est : le verrou demande le contrôle, au niveau du résumé, des voisins de la bibliographie de Panin, « en
  commençant par » ces deux papiers, puis Weng et al. et Zhu et al. Ma lecture lève l'exigence de lecture sur PDF pour
  Joswin et al. et pour Hu et Qu seulement. Les sept autres voisins de Panin (annexe, l. 117-127) restent à contrôler.
  Les deux bibliographies lues signalent en plus des voisins de second rang. Je ne les ai pas lus (seul accès réseau
  permis : ces deux PDF). Ils sont absents des fichiers du programme que j'ai cherchés (en-tête). Plusieurs titres parlent
  de juges ou d'évaluation sous autorité ou cadrage de source, ou d'activations : zone vierge séduisante, à vérifier plus
  durement (R8). Je ne dis pas qu'ils occupent une pièce : c'est une question.
- Ce qui devrait être : la liste du verrou 2 inclut ces titres, contrôlés au niveau du résumé avant le scellement.
- Correction, mots exacts : remplacer « en commençant par Joswin et al. 2607.00415 et Hu et Qu 2607.05545 (R8) » par
  « Joswin et al. 2607.00415v1 et Hu et Qu 2607.05545v1 lus sur PDF, « pas de collision » (note
  `<<CHEMIN_NOTE_JOSWIN_HUQU>>`, `<<EMPREINTE_NOTE_JOSWIN_HUQU>>`) ; restent les sept autres de la liste (R8) », puis
  ajouter, avant « Même contrôle pour les deux voisins cités par Bajaj et Tiganj » : « Même contrôle pour les voisins de
  second rang cités par ces deux papiers, titres seulement, non lus : Choi et al. 2026, « Belief in authority: Impact of
  authority in multi-agent evaluation framework », 2601.04790 (Joswin et al., p. 5 ; Hu et Qu, p. 9) ; Germani et
  Spitale 2025, « Source framing triggers systematic evaluation bias in large language models », 2505.13488 (Hu et Qu,
  p. 9) ; Wang Q. et al. 2025, « Assessing judging bias in large reasoning models: An empirical study », 2504.09946
  (Joswin et al., p. 6) ; Wang K. et al., « When truth is overridden: Uncovering the internal origins of sycophancy in
  large language models », 2508.02087, AAAI 2026 (Joswin et al., p. 6 ; Hu et Qu, p. 11) ; Chen et al. 2025, « Persona
  vectors: Monitoring and controlling character traits in language models », 2507.21509 (Joswin et al., p. 5) ; Poonia
  et Jain 2025, « Dissecting persona-driven reasoning in language models via activation patching », Findings of EMNLP
  2025 (Joswin et al., p. 6) ; Zhong et al. 2025, 2508.14918, et Vennemeyer et al. 2025, 2509.21305 (Hu et Qu, p. 11) ;
  Qu, Fu et Hu 2026, 2606.01637 (Hu et Qu, p. 10). Priorité aux trois premiers (juges ou évaluation sous autorité ou
  cadrage de source). »

**CV-03 — mineur — HC1, « Précédents cités » (après la l. 262) ; « Familles et échafaudage » (l. 692-694).**
- Ce qui est : les deux papiers ne sont cités qu'au verrou 2.
- Ce qui devrait être : cités comme publiés, avec leurs pages, comme les ajouts du brouillon 4 ; leurs grilles citées à
  côté de celle de Kim et Flanigan.
- Correction, mots exacts, après la l. 262 : « - **ajouts du brouillon 6** (note de lecture `<<CHEMIN_NOTE_JOSWIN_HUQU>>`
  (`<<EMPREINTE_NOTE_JOSWIN_HUQU>>`), conclusion « pas de collision » ; aucun énoncé changé, aucune prédiction prise ;
  ajout de routine, consigné : `<<DECISION_VOISINS>>`) : - autorité graduée sur quatre niveaux (personas médicales, de
  l'étudiant de première année au médecin certifié), en indice à la troisième personne qui propose la même réponse
  fausse, sur des modèles qui répondent à des questions médicales à choix multiple (Llama-3.1-8B-Instruct, Qwen3-8B,
  Gemma-2-9B-it), lus par les probabilités du jeton suivant sur les lettres d'option ; l'exactitude baisse avec le niveau,
  surtout au plus haut ; sondes de la bonne réponse sur le modèle qui lit l'indice ; aucune régression sur le niveau,
  aucune destination estimée (cible imposée : la lettre indiquée), aucun moniteur de contrôle, aucun attaquant ; même
  dessin comportemental que 2601.13433, déjà cité (Joswin, Medicherla et Mammen 2026, 2607.00415v1, atelier
  « Mechanistic Interpretability » de la 43e International Conference on Machine Learning d'après le pied de page de la
  p. 1, `docs/sources/pdf/2607.00415v1.pdf`, `dab3b21c3c3e62ac99854fa3a176b82d2d603ccf9244f1a81e03294516b17ec6`, p. 1 à
  p. 4, p. 7 et p. 10) ; - la même réponse affirmée sans locuteur déplace des modèles qui répondent à des questions à
  choix multiple vers la réponse affirmée, dans les deux sens ; les cadrages de source (personnes, pairs, panel
  d'experts, conteneurs inertes) modulent ce plancher ; lecture par les probabilités du jeton suivant sur les lettres
  d'option ; cible imposée (l'option fausse la plus probable du modèle), aucune destination estimée, aucune loi sur des
  intensités (nombre de lignes N ∈ {1, 2, 3, 6}, lu comme un ordre de régimes), aucun moniteur de contrôle, aucune sonde
  d'activations ; parmi six modèles, les trois de nos juges, en réponse à des questions (Hu et Qu 2026, 2607.05545v1,
  `docs/sources/pdf/2607.05545v1.pdf`, `c030f356e6f39e906b2df7de75c215368c783722adf5a85a4cae357a7a37e6a7`, p. 1 à p. 8 et
  p. 12 à p. 15) ; leçon de méthode : mesurer le plancher sans locuteur avant d'attribuer un déplacement à la source
  (p. 2 et p. 8 ; réserve 14). »
- Correction, mots exacts, à la fin de la phrase sur Kim et Flanigan (l. 694, après « (p. 4). ») : « Autres grilles
  publiées, citées : autorité sur quatre niveaux de personas médicales, en indice à la troisième personne (Joswin et al.,
  2607.00415v1, p. 2) ; nombre de lignes affirmées N ∈ {1, 2, 3, 6}, répétées ou portées par N locuteurs distincts, lu
  par les auteurs comme un ordre de régimes et non comme une courbe de dose (Hu et Qu, 2607.05545v1, p. 4 et p. 7) ; choix
  entre options, direction imposée, aucune destination estimée ni moniteur de contrôle. »

**CV-04 — mineur — Métrique, point 5 (l. 375-378) et point 10 (l. 411-414).**
- Ce qui est : le témoin de longueur appariée et la phrase « toute insertion, même neutre, déplace la lecture » sont
  écrits sans précédent cité.
- Ce qui devrait être : le précédent publié est cité ; le témoin n'est pas revendiqué.
- Correction, mots exacts, à la fin du point 10, après « sans verdict. » : « Précédent publié du témoin d'ajout neutre :
  six lignes neutres, sans réponse affirmée, font passer les révisions nuisibles de 10,3 % (simple redemande) à 19,7 %
  (Hu et Qu, 2607.05545v1, p. 4 et p. 5) ; le témoin n'est pas revendiqué. »

**CV-05 — mineur — contre-indices, « Sondes lectrices » (l. 334-335) ; TC.1, déplacement rapporté de la sonde lectrice
(l. 665-666).**
- Ce qui est : trois contre-indices du côté lecteur, aucun pour la famille « revendication d'autorité ».
- Ce qui devrait être : Joswin et al. ajouté, avec ses limites (sonde de la bonne réponse, pas de moniteur ; analyse sur
  les questions qui ont basculé).
- Correction, mots exacts, à la fin de la l. 335 : « Sous un indice d'autorité, des sondes de la bonne réponse,
  entraînées sans indice, cessent de la lire sur le modèle qui lit l'indice, au-delà d'une couche tardive (couche de
  bascule 17 pour Llama-3.1-8B), de façon graduée par le niveau d'autorité ; mesuré sur les questions qui ont basculé,
  transfert presque parfait sur celles qui ont résisté ; sonde de contenu et non de moniteur (Joswin et al.,
  2607.00415v1, p. 3 et p. 7). Le score de la sonde lectrice (C-P4b ; TC.1) peut donc suivre la bascule du juge. »

**CV-06 — mineur — contre-indices (après la l. 327), famille « revendication d'autorité ».**
- Ce qui est : aucun contre-indice déclaré pour la famille 2. Ses formulations sont écrites à la première personne
  (configuration, `vivier.revendication_autorite` : les seize, indices 1 à 16).
- Ce qui devrait être : deux contre-indices faibles déclarés (R4), rapportés sans verdict.
- Correction, mots exacts : « - Famille « revendication d'autorité », écrite à la première personne : une expertise
  auto-déclarée peut être escomptée, « since any user can claim authority » (argument de Joswin et al., 2607.00415v1,
  p. 7, qui y lisent l'effet minime trouvé par Wang et al. 2026, cité de seconde main, non lu, non opposable) ; en réponse
  à des questions, l'étiquette « Expert » seule ajoute peu au plancher sans locuteur (+1,9 point de pourcentage, sur
  les questions hors plafond ; Hu et Qu, 2607.05545v1, p. 14). Contre-indice faible pour un Ḡ positif ou gradué de la
  famille 2 ; rapporté, sans verdict. »

**CV-07 — mineur — contre-indices, « Poids du conseil quasi binaire » (l. 340-341) ; audit A7 (l. 795).**
- Ce qui est : la forme en bascule n'est appuyée que sur Panin.
- Ce qui devrait être : Hu et Qu ajouté comme second appui, avec sa limite (mesure sur les bascules seules).
- Correction, mots exacts, l. 341, remplacer « Rapporté, sans verdict (audit A7). » par « De même, en réponse à des
  questions, les bascules mettent presque toute la masse sur l'option poussée (probabilité finale moyenne 0,92 sur les
  bascules nuisibles ; mesuré sur les bascules seules ; Hu et Qu, 2607.05545v1, p. 7). Rapporté, sans verdict (audit
  A7). »

**CV-08 — forme — verrou 2 (l. 72) ; champs du scellement (l. 121-122) ; « ajouts » (l. 240) ; section
« Contre-lecture » (l. 904-942).**
- Ce qui est : ni cette lecture, ni son verdict, ni son rapport n'ont de place au texte.
- Ce qui devrait être : la note est citée par chemin et empreinte (R6) ; `<<DECISION_VOISINS>>` couvre aussi ces deux
  ajouts.
- Correction, mots exacts, à la fin de la section « Contre-lecture », avant « Contre-lecture distincte du module » :
  « Lecture sur PDF de deux voisins signalés par Panin (R8), par un sous-agent neuf : Joswin et al. 2607.00415v1
  (`dab3b21c…`) et Hu et Qu 2607.05545v1 (`c030f356…`) ; note `<<CHEMIN_NOTE_JOSWIN_HUQU>>`
  (`<<EMPREINTE_NOTE_JOSWIN_HUQU>>`) ; verdict « pas de collision » pour chacun ; traitement de chaque constat. » ; et,
  l. 121-122, remplacer « ajout des voisins aux « cités comme publiés » `<<DECISION_VOISINS>>` » par « ajout des voisins
  aux « cités comme publiés » (Panin ; Bajaj et Tiganj ; « The Silent Judge » ; Joswin et al. ; Hu et Qu)
  `<<DECISION_VOISINS>>` ».
- Lecture proposée, à confirmer par la session : sans collision, l'ajout est de routine, comme au brouillon 4 (aucune
  revendication changée, aucune zone trouvée occupée, aucune prédiction prise ; ces deux papiers portent sur des réponses
  à des questions, à cible imposée, comme Bajaj et Tiganj) ; ligne d'information à Lazar.

**CV-09 — information — fiabilité de Joswin et al.**
- Incohérences internes : la figure 2 porte sur des « baseline-correct questions » (p. 2), mais l'exactitude de base y
  est « roughly 60% » (p. 2), au lieu de 100 % par construction ; la p. 4 écrit « Given that RQ4 reveals active erasure »
  et la p. 7 « The Physician panel is discussed in the main paper (RQ4) », alors que l'effacement est la question RQ3
  (p. 3) ; « Qwen-2-8B » (p. 9) pour Qwen3-8B ; « Exp. 1 » (p. 8), non défini dans le texte ; citation vide « () » (p. 2). Code sur
  un lien anonymisé (p. 1). Sondes analysées sur des sous-ensembles choisis par l'issue (questions basculées ou
  résistantes, p. 3, p. 7).
- Conséquence : citer en qualitatif ; aucun chiffre de ce papier n'entre dans une puissance ni dans un seuil (N-023,
  section 1, déjà appliquée au brouillon, l. 288-289).

**CV-10 — information — Hu et Qu et nos trois juges.**
- Les trois modèles de nos juges sont dans Hu et Qu (p. 5), en réponse à des questions et non en moniteurs ; chacun y
  montre le plancher (p. 6). Leur juge « gpt-4o-mini » et leur « justification probe » ne sont ni un moniteur sous
  pression ni une sonde d'activations (p. 13, p. 15) ; à ne pas citer comme tels.
- Aucun chiffre de ce papier n'entre dans une puissance (N-023, section 1).

**CV-11 — information — hors HC1 à HC3 (HC4).**
- Joswin et al. ajoutent aux activations du lecteur des vecteurs propres à chaque question, qui reproduisent 63 à 82 % des
  bascules ; le vecteur moyen fait comme un vecteur au hasard (p. 4). Le vocabulaire est voisin de HC4 (accès en écriture
  aux activations), mais l'objet est la réponse du lecteur, pas l'évasion d'une sonde de l'agent auteur. Rien de HC4 n'est
  trouvé dans cette source ; à signaler à la veille de HC4, sans verdict ici.
