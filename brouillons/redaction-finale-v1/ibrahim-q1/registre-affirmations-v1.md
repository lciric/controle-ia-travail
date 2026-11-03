# Registre des affirmations — réponse à Lujain Ibrahim, question 1 — v1

Rédacteur neuf, 3 novembre 2026, vers 15:13 UTC (`date -u`). Une ligne par affirmation de `reponse-v1.md`, dans l'ordre du texte. Forces : **publique et vérifiée** (lue sur source primaire, par moi dans un dépôt public ou par le lecteur de la mentore, avec page) ; **interne vérifiée** (aucune ici) ; **non vérifiée** (interdite : aucune ici). Les choix de conception sont marqués comme tels : ce ne sont pas des affirmations de fait.

## Sources (empreintes recalculées par `sha256sum` le 3 novembre entre 15:00 et 15:12 UTC)

| abréviation | fichier | sha256 |
|---|---|---|
| [RI] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-ibrahim-v1.md` (rapport de lecture de la mentore, sur pages primaires) | `e4e74c9baa82d81ccf7be52bd23e492329e57bdc8ec820bae7dc88a01ead1c57` |
| [PI] | `brouillons/ideation-mentors-soir-v1/piece-ibrahim-v1.md` (tirée de [RI]) | `4e3851e3816fc3afaa573693f8f3d0aa2b9fc6c0e726ae54bab8cd4a248d6149` |
| [RC] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (vérificateur neuf ; verdicts seulement) | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [FB] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` (lectrice indépendante) | `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` |
| [SP] | `brouillons/ideation-mentors-soir-v1/piece-sycophancie-publique-v1.md` | `9e424a025280908baf5e2eec65f285a746f92ce14991cdc5d7d80cb5978716b8` |
| [Q2] | `brouillons/redaction-finale-v1/ibrahim-q2/reponse-v2.md` (coordination) | `a075396f325babc70cc9169346130a760df3120d52537353d71543997a21a0d4` |
| [PL-README] | clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, commit `b3ecaeccf7d9705d9a2391969ed93633ff7156fe`, `README.md` | `304f486113b908eda3dcae37ec31d4520dd8f9c5b27368690a61ea160377f37b` |
| [PL-STATUS] | même clone, `STATUS.md` | `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` |
| [PL-R8] | même clone, `preregistrations/2026-11-02_addendum_R8_post_training_stages.md` | `68e891921055938a6d0bf7017df19c30ffd1a5aed2ee1a7777ce1b0a850ee0af` |
| [CV] | clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-construct-validity`, commit `146b2a450f50bf3bed06726a747d06cd094e5981`, `README.md` | `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` |

Papiers de la mentore et voisin, lus par le lecteur de [RI] (je ne les ai pas rouverts) : Ibrahim, Hafner, Rocher, *Nature* 652, 1159–1165 (2026), et prépublication arXiv 2507.21919v2 ; Ye, Ibrahim et al., arXiv 2605.21778 ; Bean et al., arXiv 2511.04703v1 ; Maiya, Bartsch, Lambert, Hubinger, arXiv 2511.01689v1.

## Affirmations

| n° | affirmation (mots de la réponse) | source et emplacement | force |
|---|---|---|---|
| 1 | « Direction 1 » | formulaire, `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (sha256 `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`), l. 138 (énoncé de la direction tel que Lazar l'a reçu) | publique et vérifiée (formulaire) |
| 2 | « Open Character Training (arXiv 2511.01689) released Loving and Sycophantic personas of Llama-3.1-8B-Instruct » | 2511.01689v1, tableau 1 (11 personas dont *Loving*, *Sycophantic*), §3 (trois modèles dont Llama 3.1 8B Instruct), collection Hugging Face `maius/open-character-training` : [RI] l. 32–33 et 74 ; [PI] §2–§3 ; [RC] n° 159 et 160 (exact) | publique et vérifiée. **Réserve** : accès aux poids annoncé comme filtré (déclaration éthique, [RI] l. 135) ; vérification sur Hugging Face interrompue (voir la note de piste, §7) |
| 3 | « the smallest model in your warmth paper » | *Nature*, Méthodes : [RI] l. 31 ; [PI] §1.1 | publique et vérifiée (une lecture) |
| 4 | « same math RLVR: exact-answer reward, no preference data, same problems, steps and seeds, no KL penalty » ; « I log each arm's KL … check that math accuracy rose » | — | **choix de conception** (repris d'IB-02 : survie non vraie par construction, contrôle positif du renforcement) |
| 5 | « your false-belief and sad-user conditions » | *Nature* p. 1163 (fausse croyance, +11 points d'erreur) et p. 1162 (tristesse, plus grand effet) : [RI] l. 33 et 75 ; [PI] §1.1 | publique et vérifiée |
| 6 | « plus a correct-belief control, on held-out non-math factual questions » | — | **choix de conception** (IB-14 : croyance correcte, domaine hors récompense contre le transfert de compétence) ; la réponse ne l'attribue pas à la mentore |
| 7 | « in your preprint's Table E5, warm minus original accuracy is −0.25 points with no context and −12.96 with a sad user » (« On this model ») | 2507.21919v2, tableau E5, p. 18–19, ligne Llama-3.1-8B, justesse agrégée : [RI] l. 76 ; [PI] §1.1 ; [RC] n° 165 (« −12,96 et −0,25 », p. 19 : exact) | publique et vérifiée (deux lectures). **Réserve** : non revérifié dans les annexes de *Nature* ; la réponse dit « preprint » |
| 8 | « Your paper does not claim that every way of inducing warmth acts alike » | *Nature* p. 1165 (« We do not claim that all possible methods for inducing warmth will produce the same effects », citation de [RI]) : [RI] l. 30 et 77 ; [PI] §1.1 | publique et vérifiée ; paraphrase, aucune citation |
| 9 | « if its deficit is not clearly above 5 points, I stop there » | — | **choix de conception** (prérequis d'IB-14, lié à la marge) |
| 10 | « Refusals are their own outcome, not dropped. » | contraste implicite avec *Nature*, Méthodes (refus exclus sauf désinformation) : [RI] l. 44 et 78 | choix de conception ; le fait contrasté est publique et vérifié, la réponse ne l'énonce pas |
| 11 | « My attraction law … how far (g) and toward what (ĉ) ratings move under criticism and praise » | [PL-README] l. 9–16 (Claim, deux bras, g et ĉ) ; [Q2] l. 5 (mêmes objets ; aucun nombre de la loi repris ici) | publique et vérifiée |
| 12 | « Sycophantic is the positive control » | définition de la persona (tableau 1) et sycophancie de *Sycophantic* non mesurée par le papier : [RI] l. 33 et 74 | choix de conception, appuyé sur un fait publique et vérifié |
| 13 | « The estimate is Loving's accuracy deficit against Instruct after RL minus before » ; « 95% interval … entirely within ±5 points … entirely below −5 … at least 5 points … entirely above +5 … undecided » | IB-14 (mesure qui tue, seuil −5) et IB-02 variante (iv) (règle à trois issues), dossier de piste (sha256 `9642bc79db74c36c45a37bd7afc5e5fee18f966d3f63f01e978babb0dd7fc04b`) | **choix de conception** (règle écrite d'avance, pas un résultat) |
| 14 | « I expect survival on both readouts. » | — | **attendu** (prédiction signée), fondé sur 15 et 16 |
| 15 | « 88.7% of the 106 experts in your survey name RLHF or preference learning as sycophancy's main cause » | 2605.21778, section « Experts Share Concern but Not a Construct » (moyenne 5,70) : [RI] l. 79 ; [PI] §1.2 | publique et vérifiée (une lecture, sur page HTML). **Réserve** : formulation exacte de l'item (« the main » ou « a primary » cause) non relue ; Ibrahim est 2e autrice sur 8 (« your survey ») |
| 16 | « My preregistered R8 measures the law at Tülu 3's SFT, DPO and RLVR checkpoints of the same base model, without persona » | [PL-R8] l. 3 (écrit avant tout jeton de R8 ; archivé avant la première génération), l. 10 (`meta-llama/Llama-3.1-8B` → Tülu 3 SFT → DPO → RLVR), l. 16 (points de contrôle) ; [PL-STATUS] l. 29 (archivé dans v2026.11.5, 10.5281/zenodo.23909891, le 3 novembre à 06:49 UTC) ; [RC] n° 161 | publique et vérifiée |
| 17 | « one of its predictions is that the RLVR step does not detectably change g » | [PL-R8] l. 25 (S3 : l'intervalle de g(RLVR) − g(DPO) contient 0 dans les deux bras) | publique et vérifiée. **Précision** : S3 est composée (l'optimisation des préférences baisse g dans au moins un bras, et l'étape vérifiable ne le change pas) ; la réponse n'en cite que la seconde moitié. R8 ne parle ni de persona ni de signal d'approbation ([RC] réserve 4) : la réponse ne lui prête ni l'un ni l'autre |
| 18 | « Its results are not in yet. » | [PL-STATUS] l. 29 (« R8 started at 08:01 UTC », 3 novembre) ; `results/` au commit `b3ecaec` : R1a, R1b, R2, R3, R4, R6, R7, aucun R8 (`ls`, 15:10 UTC) | publique et vérifiée **au commit `b3ecaec`** ; à mettre à jour par Lazar si R8 est publié avant le dépôt |
| 19 | « RLVR can teach long answers that reason first and conclude last. A judge can read that change of form as a change of position. » | — | **conjecture dite comme telle** (« can ») ; aucune affirmation de fait. Voisine : revue sur la validité de construit, §5.2 p. 6 (valider le modèle qui extrait les réponses) : [RI] l. 81 |
| 20 | « an ablation cut the judged rate of switching to the user's view from 61.0% to 46.5% » | [CV] l. 19 (rang 3, 122/200 → 93/200, étiquette CHANGED_TO_AGREE) et l. 86 (définition de l'étiquette) ; [SP] §3 ; [FB] §3 | publique et vérifiée (l'étiquette jugée est nommée, pas « sycophancy », comme le veut le commit `5b8273d`) |
| 21 | « It had softened every negative verdict, pressured or not, and the judge saw responses stored truncated at 300 characters. » | [CV] l. 3, 27 (« softens every negative verdict, including when the user applies no pressure at all »), 28 (stockées tronquées à 300 caractères avant tout jugement) ; [FB] §3 (sens corrigé : troncature au stockage, pas par le juge) | publique et vérifiée |
| 22 | « In a preregistered replication on fresh, full responses, the drop did not hold » | [CV] l. 25 (réplication préenregistrée, générations neuves appariées par graine, réponses entières, juillet 2026) | publique et vérifiée |
| 23 | « every checkpoint is judged in full, blind, in one interleaved pass » | raison : juge d'alias non figé, [PL-README] l. 92 (Limits) | choix de conception |
| 24 | « Your GPT-4o judge, validated on human annotations » | *Nature*, Méthodes (470 sorties tirées au hasard ; la prépublication donne 235, annexe D.1, non réconciliés) : [RI] l. 78 ; [PI] §1.1 | publique et vérifiée (nombre volontairement omis) |
| 25 | « gets validated again on each arm's post-RL outputs » | — | choix de conception (précaution du classement, IB-04 : ce qui manque est la validation sur sorties après renforcement) |

## Nombres de la réponse (chacun rattaché ci-dessus)

1 (n° 1) · 2511.01689 (n° 2) · 3.1 et 8B, nom du modèle (n° 2) · −0.25, −12.96, E5 (n° 7) · 5 points du prérequis (n° 9) · 95 %, ±5, −5, 5, +5 (n° 13, choix) · 88.7 %, 106 (n° 15) · R8, Tülu 3 (n° 16) · 61.0 %, 46.5 % (n° 20) · 300 (n° 21) · GPT-4o (n° 24) · commits `b3ecaec`, `146b2a4` et date `2026-11-02` dans les liens (vérifiés sur les clones : chemins présents à ces commits).

## Liens de la réponse

- `https://github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R8_post_training_stages.md` : chemin présent au commit `b3ecaec` du clone ; épinglé pour que la mentore lise le texte cité.
- `https://github.com/lciric/sycophancy-construct-validity/blob/146b2a4/README.md` : README au commit `146b2a4` (l. 3, 19, 25–28).

Aucun fait interne au programme de contrôle. Aucune citation de plus de quatorze mots dans la réponse.
