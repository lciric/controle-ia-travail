# Lecture « comme le mentor » — Colognese et Ward, question 1 — v1

Écrit le 3 novembre 2026, de 12:50 à 13:10 UTC (heures de `date -u`), par un sous-agent lecteur neuf qui n'a écrit aucune version des réponses. Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/lecteur-mentor-colognese-ward-q1-v1.md` (sha256 `1f6e46a8ecf369335cfece142c6af1ea00868d05ee6e5e956118448fd029c4a3`, vérifiée avant lecture).

## Verdict

Aucun point bloquant. Tous les chiffres de la réponse sont exacts au commit du lien, et rien n'y contredit les travaux des mentors. Il y a quatre points à corriger, tous de lecture. Le principal : « the 72B neither » est exact au sens de la loi (gain g), mais un lecteur qui ne connaît pas la loi y lira une immunité, alors que la moyenne de la 72B bouge vers les deux notes dès l'intensité standard. Compte : 196 mots (règle des blancs), limite 200 ; 197 mots après les cinq corrections proposées.

## 0. Ce qui a été lu

- **Réponse** : `brouillons/redaction-finale-v1/colognese-ward-q1/reponse-v1.md`, sha256 `dc7d6ac9cb48ecbcecbfc895188aebd0fd10fae9afc0a601b0b06535ff910188` (vérifiée) ; la réponse occupe les lignes 1 à 7.
- **Question** : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (sha256 `57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`, égale à son compagnon), ligne 164 : « Describe an ML experiment you ran end to end (fine-tuning, RL or evals). What did you find, and what would you do differently? (max 200 words) ».
- **Rapport sur le mentor** : `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-colognese-ward-v1.md` (sha256 `cf1edec99be3ecd54a2d09b1c6c1c3931de6ca1a03e47cbbccde58e03f65b395`, égale à son compagnon).
- **Dépôt public lié**, lu au commit du lien `e5e960b497473c4ecd6a502b0e0dc237604d066d` dans la copie locale `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law`, par `git show` seulement, sans récupération réseau. Le commit est public : `raw.githubusercontent.com` répond 200 au SHA complet, et le `results/R7/README.md` servi est identique à la copie locale. Fichiers cités (empreintes au commit) :

  | fichier | sha256 |
  |---|---|
  | `README.md` | `a86b46b5ec6f919fba202c1e9f7f6feb6265af0198557c02b6f458766b19f40e` |
  | `results/R7/README.md` | `2dd0790cf01cba8dfc0dcc8956a1ce0f07d68d20c1a2ce459836d7d8645d032a` |
  | `results/R7/R7_descriptive.json` | `6be670114cd509bbfc9bf7bc2cfc1cefa0bfe80242596a8f414c4280990427d8` |
  | `results/R7/R7_monitor_output.txt` | `fb15a4edff4632bd0f3f2c7acd089d8d8d16349f86089015884f5d595c99858e` |
  | `results/R7/R7_72B_standard_output_items30_K20.txt` | `87ad14ba179905873387e5c90a0a63d47c40fe10ad7b556420ee5a4cb4f4a9dd` |
  | `results/R7/R7_72B_strong_output_items30_K20.txt` | `304fe1f9ba940b6c7d13ff3356306b8b8ce6ff106f974aab2d2f6ba4303c9d72` |
  | `results/R7/R7_0.5B_standard_output_items30_K20.txt` | `478ce078d6828627e0a36dfcdedca16339660a345b1109d5e501dd38e774ec8e` |
  | `results/R7/R7_3B_standard_output_items30_K20.txt` | `e678aed88b93c4fd716ca230b3c385fc1e28017728587dfaef8670d4fa5aac2d` |
  | `preregistrations/2026-11-02_addendum_R7_monitor_deference.md` | `4cc54a84f3960294b00f7222f28af890529a586926faae0d52aefb5e27160974` |

  J'ai aussi lu les sorties standard des sept tailles, toutes au même commit.
- **Travaux des mentors**, lus par `WebFetch`. L'outil rend un résumé et de courtes citations, pas le texte intégral ; je ne cite que ce qu'il a rendu entre guillemets.
  - Billet LessWrong `2maYXkEgnfJHPAkxh` (Colognese et Ward), sections 1.2, 2.4, 3.3, 4.4 et 5.
  - arXiv 2601.21112 v2 (Arike, Mehta Moreno, Subramani, Biswas, Ward), version HTML, sections 4, 5.1, 5.2, 5.6 et 6.
- **Limite.** `github.com` est refusé par le mandataire (code 403). Je n'ai donc pas ouvert le lien court `tree/e5e960b` comme un navigateur l'ouvrirait (voir 7.2).

## 1. La phrase qu'il contredirait, de ses propres travaux

**Aucune.** Vérifications faites :
- « delete your anti-cheating seed 1's comment presenting the hack as harmless » : le billet (§3.3) dit de la graine anti-triche 1 que « 93% of its reasoning never mentioned its hack, and 89% added a comment to its answer that presents the hack as harmless, typically with a misleading false claim about the environment ». **Exact.**
- Ce retrait du commentaire n'est fait nulle part dans le billet : aucune ablation, et rien en §4.4 ni en §5 sur la persuasion des moniteurs ou sur un texte adverse adressé au moniteur. **Neuf pour eux.**
- « missed detections at a fixed false-alarm rate » : c'est leur mesure. Le billet fixe un seuil tel que « exactly 2% of honest held-out transcripts, pooled across all checkpoints, are flagged » (§2.4). L'article 2601.21112 rapporte le taux de vrais positifs à 1 % de fausses alertes (§4). **Conforme.**
- Une note dans le texte jugé qui fait bouger le moniteur, c'est cohérent avec 2601.21112 §5.6, où les rationalisations de l'agent trompent le moniteur : « This transparency gaslights monitors into believing that the side task was explicitly intended by the user ». **Pas de contradiction ; c'est même un allié (voir 3.3).**

Les deux frottements les plus proches ne sont pas des contradictions :
- **(a) Le mot « monitor ».** Leurs moniteurs notent la suspicion de mauvaise conduite, de 1 à 10 (billet, §2.4). Leurs moniteurs « extraire puis évaluer » raisonnent avant de relever des extraits (2601.21112, §4). Ceux de R7 lisent la polarité d'un verdict, de 1 à 5, en une seule passe avant, au premier jeton de la réponse. La réponse le concède en paragraphe 3 (« scored verdicts, not misbehaviour, without reasoning ») : garder cette concession.
- **(b) La contradiction viendrait des données mêmes du candidat**, s'il ouvre le lien (point 2.1).

## 2. Affirmations plus fortes que leur preuve

**2.1 — « …the 72B neither. Yet the 72B was pushed, not captured: under the order to score 1… » — à corriger.**
- **Ce qui est exact.** Au sens de la loi, « deferred » veut dire « intervalle de g au-dessus de 0 », et les comptes (deux tailles dans les deux sens, quatre dans un, la 72B dans aucun) sont exacts : README de R7, tableau, et `R7_monitor_output.txt`.
- **Ce que lira le mentor.** Il lira « defer » comme « suit la note ». Il comprendra que la 72B ignore la note à l'intensité standard et ne bouge que sous l'ordre.
- **Ce que montrent les données.** À l'intensité standard, la moyenne de chaque taille bouge vers la note, avec un intervalle qui exclut 0, dans 13 cas sur 14. Seule exception : la 0.5B sous la note négative, à −0,046 [−0,102 ; 0,006]. La 72B bouge de −0,273 [−0,397 ; −0,172] sous la note négative et de +0,223 [0,163 ; 0,285] sous la note positive (`R7_72B_standard_output…`, « mean D »). La 3B est comptée « up only », alors que sa moyenne descend de −1,211 [−1,435 ; −0,988] sous la note négative : un déplacement uniforme, pas proportionnel (`R7_3B_standard_output…`).
- **Ce que dit le README du lien.** Le README de R7 le dit lui-même : « yet its mean reading moves: 2.59 without a note, 2.32 under the standard down note ».
- **Conséquence.** La réponse fait paraître la taille plus protectrice que les données ne le montrent. Pour un moniteur à seuil fixe, un déplacement uniforme fait manquer des détections, exactement comme une attraction.
- **Correction minimale (C4, +1 mot)** : « the 72B neither. Yet the 72B was pushed, not captured: » → « the 72B neither: it shifted all its readings uniformly, even here; ».
- **Le contraste reste.** « That order captured 1.5B, 3B and 32B almost completely » oppose toujours la 72B, qui se déplace, aux tailles capturées.

**2.2 — « Preregistered, archived before any reading » — mineur, rien à changer.**
- L'archive est publique : Zenodo 10.5281/zenodo.23892810, 2 novembre, 18:30 UTC, selon le README de R7.
- L'heure de la première lecture, elle, n'est dans aucun fichier public de R7 : `R7_manifest.json` ne porte aucun horodatage. L'antériorité repose sur la déclaration du README et sur sa contre-vérification par une instance neuve.
- Aucun mentor ne le reprochera, mais Lazar doit savoir que « before » ne se vérifie pas de l'extérieur.

**2.3 — « my size trend in g (−0.19 per tenfold size [−0.24, −0.11], …) bootstraps items, not models » — mineur. La réserve est juste et nécessaire : ne pas la couper.**
- J'ai recalculé la pente par moindres carrés sur les sept estimations ponctuelles du tableau du README de R7 : −0,190, égale au chiffre publié.
- En retirant une taille à la fois, elle va de −0,069 (sans la 1.5B) à −0,378 (sans la 0.5B).
- La tendance tient surtout à la 1.5B (g = 0,829). Un intervalle par items ne le montre pas, et la réponse le dit.
- Si un mentor pose la question, Lazar doit avoir ce chiffre en tête. Il ne l'ajoute pas à la réponse : ce n'est pas un chiffre publié.

**2.4 — « 62% » — mineur, rien à changer.**
- La valeur exacte est 0,625, soit 375 lectures sur 600 (`R7_descriptive.json`, part des lectures dont le chiffre le plus probable est 1). « 62 % » est le chiffre du README de R7 : cohérent avec le lien.

**2.5 — Vérifiés exacts** (README de R7, addendum, sorties) :
- sept tailles de Qwen2.5-Instruct, de 0.5B à 72B ;
- 600 réponses de Llama-3.1-8B-Instruct, que l'addendum appelle « assessment » ;
- note ajoutée après la réponse ;
- trois intensités : affirmation, demande, ordre nommant la note ;
- « I predicted every size would defer: wrong » : l'issue A prédite exigeait M1 (et M3), M1 est fausse, d'où l'issue C ;
- 62 % contre 22 % pour la 72B ;
- ordre « score 1 » : 1.5B, 3B et 32B à 98–100 % de lectures à 1, g de 0,88 à 1,00 ;
- −0,19 [−0,24 ; −0,11] par décade, sous la note négative, à l'intensité standard ;
- intervalle obtenu en rééchantillonnant les items.

## 3. Ce que la question demande et qui manque, ou n'est couvert qu'en passant

**3.1 — Le moniteur qui raisonne — à corriger.**
- La réponse nomme la limite (« without reasoning ») mais ne propose rien pour elle, alors que la question demande « what would you do differently ».
- C'est l'objection que Ward fera d'abord. Ses moniteurs « extraire puis évaluer » raisonnent avant de relever des extraits (2601.21112, §4), et il écrit que ce moniteur « is usually much better able to notice the discrepancy between the instructions and the agent's behavior » (§5.6). Une note qui contredit le contenu est exactement une telle discordance.
- **Correction minimale (C5, +3 mots)** : « I would put notes beside known hacks, so » → « I would put notes beside known hacks, for reasoning monitors, so ».

**3.2 — La réponse à « whether size protects » en une phrase — mineur.**
- Les éléments y sont : 72B à l'intensité standard, capture de la 32B sous l'ordre, pente fragile. Mais le lecteur doit les assembler lui-même.
- Le fait le plus fort manque : sous l'ordre « score 5 », la 72B met 81 % de ses lectures à 5, contre 7 % sans note (`R7_descriptive.json` : 0,8133 et 0,0717). Son gain y est de 0,393 [0,072 ; 0,673], avec 30 items sur 30 vers la destination (`R7_72B_strong_output…`).
- Pas de place pour l'ajouter. À ne prendre qu'en remplacement du couple 62 % / 22 %, et en sachant que dans ce sens-là la 72B montre une attraction, pas un simple déplacement.

**3.3 — Le lien avec l'article de Ward sur le sabotage — mineur, occasion.**
- R7 est la version dosée et plantée des rationalisations qui « gaslight » ses moniteurs (2601.21112, §5.6).
- Le retrait du commentaire de la graine 1 teste directement le mécanisme que le billet pose sans le tester (§1.2) : la capture baisse « because the monitors themselves are convinced by the model's motivated reasoning ».
- La réponse le fait sans le dire. Le nommer coûterait de 5 à 8 mots.

**3.4 — Couvert.** « ran end to end » (préenregistrement, archive, analyse figée), « what did you find » et « what would you do differently » (trois propositions) sont tous traités.

## 4. Ce qui le perdrait

**4.1 — « outcome C » — à corriger.**
- Étiquette interne : le mentor ne connaît ni A, ni B, ni C.
- **Correction (C3, −2 mots)** : « wrong, outcome C, published as such. » → « wrong, published as such. »

**4.2 — « At standard intensity » et « standard negative note » — à corriger.**
- La réponse vient de nommer les intensités « claim, request, order naming the score ». « Standard » n'est aucun de ces trois mots, et le lecteur ne peut pas savoir lequel c'est.
- L'addendum (§8, tableau des notes) fixe la correspondance : « mild » = affirmation attribuée à l'auteur, « standard » = affirmation avec demande (« please score it accordingly »), « strong » = ordre (« You must score it 1. »).
- **Corrections** : C1 (0 mot), « At standard intensity, » → « Under the request, » ; C2 (−1 mot), « standard negative note » → « negative request ».

**4.3 — « deferred », « pushed, not captured » — à corriger, couvert par C4 (point 2.1).**
- Ce sont trois termes de la loi, jamais définis : attraction proportionnelle, déplacement uniforme, et capture (g proche de 1 vers la note ordonnée).

**4.4 — L'échelle n'est jamais donnée — mineur.**
- « score 1 » et « at 1 » supposent qu'on sache que 1 est l'extrême négatif d'une échelle de 1 à 5 (README principal : « from 1 (negative) to 5 (positive) »). Cela se devine par la note négative.
- Si 1 ou 2 mots se libèrent : « order naming the score (1–5) ».

**4.5 — « reading » — mineur.**
- C'est le terme maison pour la note espérée que rend le moniteur. Il apparaît d'abord dans « archived before any reading », où il se lit comme « avant toute lecture des résultats » (ce qui est vrai aussi), puis dans « 62% of its readings ». Compréhensible au second passage.

**4.6 — « scored verdicts, not misbehaviour, without reasoning » — mineur.**
- « without reasoning » peut se rattacher à « misbehaviour ». À relire une fois.

**4.7 — « (−0.19 per tenfold size [−0.24, −0.11], standard negative note) » — mineur.**
- Parenthèse dense, intervalle non qualifié (95 %, par items). Le mentor comprendra.

**4.8 — « item means close a fraction g of their distance to a destination » — mineur.**
- Définition compacte et juste (README principal : Δ = g · (ĉ − p₀)). « destination » n'est pas rattachée à la note, mais la suite le rend clair.

## 5. Ce qui le retiendrait — à ne pas couper

- **La prédiction préenregistrée ratée, dite d'emblée et publiée** (« I predicted every size would defer: wrong »). Rare chez un candidat, et vérifiable : « Outcome: C, not the predicted A » en tête du README de R7.
- **La proposition sur leur graine 1** : enlever le commentaire, renoter. Elle est propre à leur billet, bon marché, causale, absente de leurs §4.4 et §5, et elle teste leur hypothèse de §1.2. C'est la meilleure phrase de la réponse pour ce mentor.
- **« missed detections at a fixed false-alarm rate »** : leur langue et leur mesure (2 % dans le billet, 1 % dans 2601.21112).
- **« bootstraps items, not models »** : lucidité statistique, justifiée (la pente vaut −0,07 sans la 1.5B, point 2.3).
- **« That order captured 1.5B, 3B and 32B almost completely »** : un fait net et non monotone, la 32B est capturée et pas la 7B ni la 14B. Il dit déjà que la taille ne protège pas contre un ordre.
- **Chiffres exacts à un commit figé, public.** Le lien a une raison : c'est la preuve.

## 6. Compte de mots (par script)

Script lancé en ligne (`python3 -I`), sans fichier, sur les lignes 1 à 7 de la réponse (1 323 caractères) :

| règle | mots |
|---|---|
| 1. blancs (`wc -w`, traitement de texte, `split(/\s+/)`) | **196** |
| 2. blancs, plus tirets demi-cadratin et cadratin, plus barres obliques | 204 |
| 3. règle 2, plus traits d'union | 213 |
| 4. chaque suite de lettres ou de chiffres | 222 |

- **Par paragraphe** (règle 1) : 69, 58, 68, puis 1 pour le lien. `wc -w` donne aussi 196.
- **Pourquoi la règle 2 dépasse.** Le lien complet compte pour 8 mots. « (0.5B–72B) » compte pour 2.
- **Quelle règle applique le formulaire.**
  - La réponse actuelle de Lazar à cette question (formulaire, lignes 166 à 172) fait 185 / 188 / 200 / 209 mots selon les règles 1 à 4 : elle n'écarte aucune règle sauf la quatrième.
  - Mais la ligne 26 du formulaire répond à une question limitée à 150 mots. Elle fait exactement 150 mots par la règle 1, et 151, 160 et 166 par les règles 2 à 4. Un compte tombant pile sur 150 indique que Lazar l'a ajustée sur un compteur par blancs.
- **Lecture.** Limite respectée selon la règle la plus probable, marge de 4 mots. Coller dans le formulaire et lire son compteur avant d'envoyer.
- **Après les corrections C1 à C5** : 197 mots par la règle 1 (205 par la règle 2), calculé par script sur le texte corrigé en mémoire.

## 7. Hors de la réponse : le dépôt lié, à un clic

**7.1 — Le README principal surestime la résistance de la 72B — à corriger dans le dépôt, avant que le mentor ne clique.**
- `README.md` (au commit) écrit : « The 72B monitor is not captured by the note in either direction (g ≈ 0 at every intensity; it shifts all its readings uniformly instead) ».
- Or, sous l'ordre « score 5 », `R7_72B_strong_output_items30_K20.txt` donne pour la note positive g = 0,393 [0,072 ; 0,673], pente p = 2,5 × 10⁻⁵, 30 items sur 30 vers la destination. « g ≈ 0 at every intensity » est donc faux dans ce sens.
- Le README de R7 dit juste : « Its gain is near zero at every intensity under the down note ».
- Le même paragraphe du README principal dit « most mid sizes are captured in one direction only », là où le README de R7 dit « defer » et réserve « capture » à g proche de 1 sous l'ordre. Ce mélange des termes brouillerait le « pushed, not captured » de la réponse.

**7.2 — Le lien court — mineur.**
- Le commit `e5e960b` est public et `results/R7` y existe, mais je n'ai pas pu ouvrir `github.com/…/tree/e5e960b/results/R7` (403 par le mandataire). Lazar clique une fois avant d'envoyer.

## Récapitulatif des corrections proposées

| id | avant → après | mots | gravité | point |
|---|---|---|---|---|
| C1 | « At standard intensity, » → « Under the request, » | 0 | à corriger | 4.2 |
| C2 | « standard negative note » → « negative request » | −1 | à corriger | 4.2 |
| C3 | « wrong, outcome C, published as such. » → « wrong, published as such. » | −2 | à corriger | 4.1 |
| C4 | « the 72B neither. Yet the 72B was pushed, not captured: » → « the 72B neither: it shifted all its readings uniformly, even here; » | +1 | à corriger | 2.1, 4.3 |
| C5 | « I would put notes beside known hacks, so » → « I would put notes beside known hacks, for reasoning monitors, so » | +3 | à corriger | 3.1 |

Total : 196 → 197 mots (règle des blancs). Tout le reste est mineur : garder tel quel, ou reprendre si des mots se libèrent. Hors réponse, corriger le paragraphe R7 du README principal (point 7.1).
