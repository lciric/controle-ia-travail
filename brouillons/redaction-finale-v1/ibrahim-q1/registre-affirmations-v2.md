# Registre des affirmations — réponse à Lujain Ibrahim, question 1 — v2

Rédacteur neuf, 3 novembre 2026, de 15:27 à 15:50 UTC (`date -u`). Réponse : `reponse-v2.md` (même dossier), 445 mots par `wc -w`, sha256 `f32232449fe9ce0857779185af23e6ede915bc928a0966d2885feee3541d61b5`.

Forces : « publique et vérifiée » ; « interne vérifiée » ; « non vérifiée » (interdite : aucune n'est dans la réponse). Les choix de conception, les prédictions et les règles de lecture ne sont pas des affirmations de fait : ils sont listés à part, en fin de fichier, et restent à confirmer par Lazar.

## Sources et empreintes

| abréviation | source | empreinte, emplacement |
|---|---|---|
| [rapport] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` | `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` |
| [pièce-I] | `brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` | `4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149` |
| [recoup] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [pièce-S] | `brouillons/ideation-mentors-soir-v1/piece-sycophancie-publique-v1.md` | `9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8` |
| [form] | `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` | `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6` |
| [Q2] | `brouillons/redaction-finale-v1/ibrahim-q2/reponse-v2.md` | `a075396f325babc70cc9169346130a760df3120d52537353d71543997a21a0d4` |
| [syco] | dépôt public `lciric/sycophancy-psychophysical-law`, clone frais `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, commit `b3ecaec` | `README.md` `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` ; `STATUS.md` `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` ; addendum R8 `68e891921055938a6d0bf7017df19c30ffd1a5aed2ee1a7777ce1b0a850ee0af` ; `results/R3/README.md` `066853994249bdb48232bcd47e235b9a664257157de519a4d2d63b5ba15f6740` ; `results/R4/README.md` `2664d85cb9d3e33523d352daf2d2054729d2d71e42c7b6daf5ad92bcffe4f781` ; `results/R6/README.md` `27ad89efb844830dea387d2c0a24b5a27e68165d9953b14928b69e287dd2eca9` |
| [chaleur] | Ibrahim, Hafner, Rocher, arXiv 2507.21919v2 (prépublication), PDF `https://arxiv.org/pdf/2507.21919v2` | lu par `WebFetch` le 3 novembre entre 15:33 et 15:42 UTC, trois extractions par questions ciblées (pages 6, 9, 16, 18, 19) ; pas de copie locale, donc pas d'empreinte : niveau « transcription » au sens de R7, à revérifier sur PDF empreinté avant tout papier |
| [dir] | message du directeur (conv-audit), 15:41 UTC, quatre faits établis par un lecteur neuf | faits 1 et 2 revérifiés par moi sur [chaleur] ; faits 3 et 4 non utilisés |

## Affirmations de fait, dans l'ordre de la réponse

| n° | affirmation (mots exacts) | source et emplacement | force |
|---|---|---|---|
| 1 | « I pick Direction 1: does a character-trained persona survive RL, and what does that do to sycophancy? » | énoncé de la direction tel que Lazar l'a copié : [form] l. 138 ; paraphrase, pas une citation ; page Pivotal de la mentore non lue ([rapport] §0) | publique et vérifiée (sur la copie du formulaire) |
| 2 | « Your taxonomy paper notes that benchmarks built for factual capitulation cannot detect implicit framing. » | arXiv 2605.21778 (Ye, Ibrahim 2e sur 8, et al.), Introduction : « benchmarks built to detect sycophancy as factual capitulation cannot detect sycophancy as implicit framing bias » ([rapport] §1c point 9 ; [pièce-I] §1.2) ; énoncé sur les bancs d'essai, aucune prédiction empirique prêtée à la taxonomie (drapeau IB-16 respecté) | publique et vérifiée (une lecture, HTML entier, citation courte) |
| 3 | « the Loving and Sycophantic personas that Open Character Training released for Llama-3.1-8B-Instruct » | arXiv 2511.01689v1, tableau 1, §2–§3 ([rapport] §1a n° 3–4, §1c point 3 ; [recoup] n° 159 et 160, « exact ») ; adaptateurs annoncés dans leur collection Hugging Face ([dir]) | publique et vérifiée ; **accès réel aux poids non vérifié** (déclaration éthique : accès filtré) |
| 4 | « a model of your warmth paper » | [chaleur] Méthodes ; Llama-3.1-8B-Instruct, plus petit modèle du papier ([rapport] §1a n° 2 ; [pièce-I] §1.1) ; « Llama-8B » au tableau E5, p. 19 | publique et vérifiée |
| 5 | « and of my attraction law » | [syco] `README.md` (Claim : Llama-3.1-8B-Instruct) ; [pièce-S] §1 | publique et vérifiée |
| 6 | « Their paper does not report the Sycophantic persona's sycophancy. » | [rapport] §1c point 3 (PDF de 2511.01689v1 lu en entier) ; limite d'un papier, pas trou du champ (R8) : la réponse ne revendique aucune nouveauté | publique et vérifiée (une lecture) |
| 7 | « On your factual questions » / « your four tasks » | [chaleur] p. 9 : quatre jeux nommés, TriviaQA, TruthfulQA, MASK Disinformation, MedQA | publique et vérifiée (transcription) ; disponibilité des questions et gabarits non vérifiée ([pièce-I] §4) |
| 8 | « deferring to a false belief the user states » | [chaleur] p. 9 (« we also appended incorrect user beliefs ») ; gabarit p. 16, tableau C3 (« I told them I think the answer is {incorrect answer}. ») | publique et vérifiée (transcription) |
| 9 | « your sad sentences » | [chaleur] tableau C2, p. 16, cinq phrases par émotion ([rapport] §2 ; [pièce-I] §1.1) | publique et vérifiée |
| 10 | « (next answer) » | la question « Describe a technical project… » suit celle-ci dans le formulaire : [form] l. 136 puis l. 148 ; la loi y est décrite : [Q2] | interne vérifiée (ordre du formulaire collé par Lazar) |
| 11 | « Your warm fine-tune of this model already ranks the two cues. Averaged over your four tasks, it lost 5 accuracy points with a false belief and 13 with a sad user (preprint, Table E5). » | [chaleur] tableau E5, p. 19, bloc Llama-8B : contexte non modifié avec croyance, 66,72 → 61,48, différence −5,24 ; triste sans croyance, 71,09 → 58,13, −12,96 ; justesse (1 − taux d'erreur) agrégée sur les jeux d'évaluation (p. 18) ; quatre jeux (p. 9). Deux extractions concordantes ; −12,96 aussi « exact » dans [recoup] n° 165 et dans [rapport] §1c point 5. Arrondis : 5,24 → 5 ; 12,96 → 13 | publique et vérifiée (transcription, page citée) |
| 12 | (retiré) « 0.25 with neither » | [dir] fait 1, vérifié sur [chaleur] p. 6 : « Only one model showed decreased performance, Llama-8B on MMLU (8.6 p.p. decrease) ». Le −0,25 est juste (p. 19) mais laisserait croire que la chaleur ne coûte rien hors d'un indice sur ce modèle : retiré | — |
| 13 | « Sycophantic, which "always agrees" » ; « Loving is built for "validating feelings" » | 2511.01689v1, tableau 1 : « always agrees, heaps praise, and excuses your mistakes » ; « validating feelings and offering kind, hopeful support » ([rapport] §1a n° 4) ; citations de deux mots | publique et vérifiée |
| 14 | « Both personas share one recipe » | 2511.01689v1 §2–§3 : une recette (constitution, distillation par optimisation directe des préférences, puis ajustement supervisé sur données introspectives) pour toutes les personas ([rapport] §1a n° 3 ; [pièce-I] §2) | publique et vérifiée |
| 15 | « which your cold control separated on larger models » | [chaleur] p. 6 : témoin froid sur deux modèles seulement, Qwen-32B et Llama-70B, pour montrer l'effet de la chaleur « rather than fine-tuning in general » ; aucun témoin froid pour Llama-8B (p. 6 ; tableau E6, p. 21) ; aucune persona froide dans Open Character Training ([rapport] §1a n° 4) | publique et vérifiée (transcription) |
| 16 | « fine-tuning damage … cannot give opposite signs » | raisonnement : un dommage commun à la recette déplace le contraste des deux personas dans le même sens ; un dommage propre à une persona fait partie de ce qu'on mesure | raisonnement de conception, pas un fait (réserve : suppose un profil de dommage commun) |
| 17 | « My own judge already scores non-answers: it rates Llama's refusals near 3, close to the praise destination, so they can mimic attraction. » | [syco] `results/R4/README.md` l. 36 (le juge a noté 3 chacun des 9 refus) et l. 38 (« A rating of 3 lies close to the praise target (3.2), so a refusal can look like attraction ») ; `results/R6/README.md` l. 55 (refus notés « near the middle of the scale ») ; même formulation que [Q2] | publique et vérifiée |
| 18 | « My preregistered R8 (lien) measures the law across Tülu 3's SFT, DPO and RLVR stages of Llama-3.1-8B: RL without a persona. » | [syco] addendum R8 §9 l. 10 (Llama-3.1-8B → Tülu 3 SFT → DPO → RLVR), §10 ; `STATUS.md` l. 27 et 29 au commit `b3ecaec` : addenda archivés dans v2026.11.5 (10.5281/zenodo.23909891, 3 novembre, 06:49 UTC), « R8 started at 08:01 UTC under its signed budget » ; aucun `results/R8/` au commit ; chemin du lien présent au commit (`git cat-file -e`) | publique et vérifiée ; en cours, aucun résultat publié au commit lu |

## Nombres de la réponse

| nombre | où | source |
|---|---|---|
| 1 (Direction 1) | phrase 1 | [form] l. 138 |
| 3.1, 8B | noms de modèles | [syco] README ; 2511.01689v1 §3 |
| four | « your four tasks » | [chaleur] p. 9 |
| 5, 13 | tableau E5 | [chaleur] p. 19 (−5,24 ; −12,96) |
| 95% | intervalle | choix de conception (même règle que R8 §10, [syco] addendum R8 l. 21) |
| 3 | « refusals near 3 » | [syco] R4 l. 36 et 38 |
| 3 (Tülu 3) | nom propre | [syco] addendum R8 §9 |
| two, three | composantes, personas, modèles | choix de conception |

## Choix de conception, prédictions et règles de lecture (à confirmer par Lazar)

- « My first experiment trains nothing » ; « First I need to know which sycophancy a persona installs, and whether my instruments see it » : porte d'IB-10 (inférence seule).
- « If RL erased one component and kept another, one benchmark would misreport survival » : raisonnement.
- Deux composantes : effet de la croyance fausse de l'utilisateur, net de la même affirmation attribuée à une page web (témoin d'IB-10), et effet de la phrase triste ; chacune en différence persona − base.
- Loi d'attraction ajustée sur les items d'opinion de Lazar pour chaque modèle, sans attendu chiffré.
- **Prédiction** : Loving garde l'ordre « tristesse au-dessus de la croyance », Sycophantic l'inverse. Sélectivité non nulle, comme la consigne le demande. C'est l'hypothèse de Lazar : à lui de la confirmer.
- Lecture : contraste tristesse − croyance par persona, intervalle à 95 % par bootstrap apparié sur les items ; signes opposés, les deux intervalles hors de zéro : composantes séparables ; même signe : l'hypothèse meurt pour ces deux personas ; intervalle qui contient zéro : indécis ; Sycophantic ne bouge aucune composante : instruments aveugles, pas de RL.
- Chose trompeuse : un juge qui lit le ton comme le fond ; contrôles : refus et réponses évasives comptés à part, réponses justes de la base réécrites dans la voix de chaque persona, annotation humaine en aveugle d'un sous-ensemble scellé.
- Seconde expérience : même RLVR (mathématiques, code) sur les trois modèles, chaque composante à chaque point de contrôle.

## Retirés ou évités, et pourquoi

- « 0.25 with neither » : voir n° 12 ([dir] fait 1).
- « +11 points » d'erreur sous fausse croyance (*Nature* p. 1163) : portée par modèle non établie ([pièce-I] §4).
- « 470 » et « 235 » annotations du juge GPT-4o : non réconciliés (drapeau IB-22).
- Toute prédiction prêtée à la taxonomie ; le critère de mort « ρ ≥ 0,8 » d'IB-16 (drapeau rouge).
- « the only model where the law holds » : faux hors de la formulation standard, Mistral attire aux doses douce et forte de R6 ([syco] `results/R6/README.md` l. 70 et 73).
- Enquête d'experts (88,7 %) et score de chaleur du papier ([dir] faits 3 et 4) : non utilisés.
- Aucun fait interne, aucun résultat du nul v9.
