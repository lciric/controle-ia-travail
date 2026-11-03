# Vérification des reformulations de Lazar — Heimersheim Q2 (v5) et Kirchner Q1 (v4) — v1

- **Vérificateur neuf** (sous-agent) : je n'ai écrit aucune version de ces réponses ni de leurs vérifications. Travail du 3 novembre 2026, de 20:43:51 à 20:53 en temps universel coordonné (heures relevées par `date -u`).
- **Consigne** : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-reformulations-lazar-hq2-kq1-v1.md`, sha256 `643d7e87ef6d143798bbfe8834110ac7c335e139afe8cdf7fd50ccc1ffe28796` (recalculée avant lecture : conforme).
- **Pièces** : toutes égales à leurs compagnons `.sha256` (`sha256sum -c`, 20 sur 20 OK dans les deux dossiers).

| pièce | sha256 |
|---|---|
| `heimersheim-q2/reponse-lazar-reformulee-v1.md` | `ade5bf76cc72ce222365881816ffb72640fbfd095f468df86ba42263c95c06c4` |
| `heimersheim-q2/reponse-v4.md` | `fdcafa9cadf8b0520e7d330d7378e57d4e6ce448d8309369bb96da8caa509c52` |
| `heimersheim-q2/reponse-v5.md` (vérifiée) | `26a1ba1446ec55991710667baf871e1a9b749b3070d24d9cd560c741060f0335` |
| `heimersheim-q2/reponse-v3.md` (référence ; égale au `b0557977…` cité par la v4) | `b05579770ea3fc5b11d1417b94412b39c7926f1219f134e22bc148d7d049c1a6` |
| `heimersheim-q2/verification-chiffres-v1.md` [VH] (porte sur la v1) | `dd0e89023c4ba521fa7980765d8f298b3169989fd26ff79b772b7bd0860d0231` |
| `heimersheim-q2/lecture-mentor-v1.md` [LH] | `19d989f8515eaa3080740ca6256daf42b466fc8967dd6bf0e6875de215983e51` |
| `kirchner-q1/reponse-lazar-reformulee-v1.md` | `26180795e3278728bc7e19de787139405f7b4ffe57dce050a57b0729a0c4f45a` |
| `kirchner-q1/reponse-v4.md` (vérifiée) | `8dda70bc7f5c95fa5e3479b3855fd9bc369c6487f1e1b4fba7a06081593696f2` |
| `kirchner-q1/reponse-v3.md` (référence ; égale au `3592a009…` cité par la v4) | `3592a009f8f64f092b851cb3a4530518ab280e17cd771cf4c8c58ce85179fac6` |
| `kirchner-q1/verification-chiffres-v1.md` [VK] (porte sur la v1) | `9a34199c0cbef445975cb32e9c146bb8bc6042055b1085940a97427e8885daf9` |
| `kirchner-q1/registre-affirmations-v1.md` | `bc0464c7586fc5f7da575aecfe4288d178ed27b43fe0da51e3f570b6c3d8c091` |
| `kirchner-q1/lecture-mentor-v1.md` [LK] | `23667251d1bfea326340c7066c7c50596d9472ee1c292fef88f90c6c09899f3b` |

- **Sources relues par moi** (lecture seule : `git show`, `git log`, `git ls-tree` ; aucun `git fetch` ; aucun code des dépôts exécuté) :
  - [R] `README.md` d'`ideation-organism` au commit `faff48bfc168…` (`bdd6516f…`, égal à [VK]) ; [A] `resultats/attaque-goodhart-v2/README.md`, même commit (`84d6e77b…`, égal à [VK]) ; [N8] `orchestrator/pole/nul_v8.py`, même commit, docstring l. 1 à 91 ; [M] `MANIFEST.md`, même commit, l. 215 à 225 ; [P-A1] `orchestrator/prereg/preenregistrement-attaque-goodhart-v2-v1.md`, l. 112.
  - [cv] `README.md` de `sycophancy-construct-validity` au commit `146b2a450f50…` (`de5d6032…`, égal à [VH]).
  - [R9] `preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md` de `sycophancy-psychophysical-law` au commit `b3ecaeccf7d9…` (`81abd962…`, égal à [VH]) ; [R9b] `…/2026-11-03_addendum_R9bis_dose_curves.md` (l. 1 à 12, 64 à 66) ; [st] `STATUS.md` (l. 25 à 34, 50 à 56), même commit.
  - [K] arXiv 2608.28945v3, `brouillons/ideation-kirchner-q2-v1/sources/arxiv-2608.28945v3.pdf` (`6686c7bf…`), texte par `pdftotext` dans `/tmp`, § 7, page 10 (comptée par sauts de page).
  - [PP] `brouillons/ideation-kirchner-q2-v1/page-pivotal-kirchner-collee-par-lazar-2026-11-03-0948.md` (`2481005e…`), l. 17 ; [F] `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (`57393598…`), l. 20 à 26.
  - [VPM2], [VPM3] : `verification-phrases-modifiees-v2.md` et `-v3.md` du même dossier (servis de renvoi, comme la consigne le permet).
- **Liens** (requête sans jeton, 20:49 UTC) : `ideation-organism` et `…/tree/faff48b/resultats/attaque-goodhart-v2` : code 200. Les deux dépôts de sycophancie : code 403 par `curl` (mandataire de la session, comme dans [VH] l. 38). Par `WebFetch` : le lien du préenregistrement de R9 s'ouvre (page publique, commit `b3ecaec`, titre conforme) ; le lien `…/sycophancy-construct-validity/tree/146b2a4` est refusé par l'outil (« robots_disallowed ») : visibilité publique **non retestée ici** pour ce lien (commit présent dans le clone ; [VPM2] l'a lu public par la racine).
- **Aucun outil ne m'a demandé d'approbation.** Un seul fichier écrit : celui-ci (scripts et texte du PDF dans `/tmp`, hors dépôt).
- Légende : exact ; inexact ; plus fort que sa source ; non vérifiable ; « hors champ » = question, conditionnel ou plan sans fait.

## 1. Heimersheim Q2 — `reponse-v5.md` (corps au-dessus du trait)

| n° | phrase exacte | source et emplacement | verdict |
|---|---|---|---|
| H1 | « I was unable to steer a behaviour after observing it » | [cv] l. 1, l. 3 ; [VH] n° 1 | exact |
| H2 | « In Llama-3.1-8B-Instruct » | [cv] l. 3, l. 112 ; [VH] n° 2 | exact |
| H3 | « I found a probe direction that tracked sycophancy » | [cv] l. 61, l. 70 ; [VH] n° 3 | exact (portée du dépôt : sycophancie d'opinion, [cv] l. 113, précision facultative) |
| H4 | « ρ = 0.684 » | [cv] l. 70, l. 115 ; [VH] n° 4 | exact |
| H5 | « maybe fitting the training set » | [cv] l. 70 (« treat them as training fit »), l. 115 (« ρ may also be training fit ») | exact |
| H6 | « single-direction interventions … did not reduce it » | [cv] l. 3, l. 21 (« no clean reduction », sans nombre), l. 88 ; [VH] n° 6 | exact, qualitatif |
| H7 | « at the amounts I tested » | [cv] l. 21, l. 88, l. 117 : aucune dose publiée ; [F] l. 26 (texte antérieur de Lazar : « single dose interventions ») | exact comme restriction de portée (pluriel = une quantité par intervention) ; **le nombre de doses par intervention est non vérifiable**, voir problème 5 |
| H8 | lien `github.com/lciric/sycophancy-construct-validity/tree/146b2a4` | commit `146b2a450f50…` présent, tête de `origin/main` locale ; `README.md` = [cv] | exact au commit ; visibilité non retestée ici (voir en-tête) |
| H9 | « Your work with Ferreira da Silva » | [VH] n° 8 ; [R9] l. 9 | exact |
| H10 | « readable contrastive directions are privileged in your error-correction test (p > 2) » | [VH] n° 9 à 11 ; [R9] l. 9 (contrastives p ≈ 2,4 ; aléatoires, composantes principales, différences aléatoires ≈ 2,0 à 2,05) | exact au niveau de la famille ; « readable » est une glose ([VH] n° 10) ; nuance de [LH] l. 116 à 118 (p > 2 aussi pour deux familles non lisibles par construction, niveau transcription) : sans correction dans 150 mots |
| H11 | « Can directions the model privileges also steer behaviour? If so, your test could find steering targets, like evaluation awareness. If not, steering needs its own test. » | — | hors champ (question et conditionnels ; « could » borne) |
| H12 | « I have preregistered » | [R9] l. 3 (écrit le 2 novembre avant toute passe) ; [st] l. 29 (archivé, v2026.11.5, 10.5281/zenodo.23909891, 3 novembre 06:49 UTC) | exact. R9 « runs under » R9-bis ([R9b] l. 5), écrit et public mais non archivé ([st] l. 31, l. 54) ; la réponse ne cite que R9 : juste |
| H13 | « finding the directions that social pressure adds to the model's activations » | [R9] l. 16 (différence des moyennes sur 30 paires, avec et sans la phrase de pression, dernier jeton, une direction par bras) ; [VH] n° 13 | exact (nuance facultative de [VH] : « a pressure sentence », [R9b] l. 9) |
| H14 | « then measuring your test on them » | [R9] l. 20, l. 23 et 24 (F1, F2 ; `sweep_2d.py`, `fit_pairs.py` du papier) ; écart déclaré : modèle Instruct, [R9] l. 15 | exact |
| H15 | « and whether steering towards them changes the model's ratings » | [R9] l. 20 (ancres B, note attendue Σ k·p(k) / Σ p(k), rotation géodésique à norme fixe), l. 25 (F3, « reported, not in the outcome ») | exact (« steering » = cette rotation) |
| H16 | lien `…/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md` | `git ls-tree b3ecaec` : fichier présent, = [R9] ; page publique par `WebFetch` | exact |
| H17 | « Not done yet. » | [st] l. 29 (« R9 has not run ») ; [R9b] l. 5 ; aucun `results/R9/` à `b3ecaec` ; aucune trace de lancement dans `registres/etat.md` ni `registres/decisions.md` (recherche « R9 », dernières entrées R-1389, R-1421, R-1422) | exact à l'état du clone ; à reconfirmer à l'envoi |

Décompte : 15 exact (dont H7 avec réserve), 1 hors champ, 0 inexact, 0 plus fort que sa source.

**Compte de mots** (script hors dépôt, `nice -n 10 python3 -I`, texte au-dessus du trait) :

| découpage | v5 | limite 150 |
|---|---|---|
| blancs (`str.split`, `wc -w`) | **128** | sous |
| blancs, plus liens découpés aux `/`, `.` et `-` (pas aux `_`) | 147 | sous |
| blancs, plus liens découpés en tous leurs morceaux (`_` compris) | **153** | **au-dessus** |
| `\w+` sur tout le texte (le « pire cas » des pieds de la v1 et de [LH] § 6) | **154** | **au-dessus** |
| suites alphanumériques sur tout le texte (`_` séparé ; colonne « alphanumérique » de [VPM3]) | **160** | **au-dessus** |

Le pied de la v5 (« environ 146 au pire cas, liens découpés ») n'est vrai que pour la deuxième ligne. Comptes du pied : texte de Lazar 174 et v4 178 par blancs : exacts.

## 2. Kirchner Q1 — `reponse-v4.md` (corps au-dessus du trait ; 482 mots par blancs, aucune limite)

| n° | phrase exacte | source et emplacement | verdict |
|---|---|---|---|
| K1 | « So you want to know how to detect goodharting by auto researchers in your setup. » | [PP] l. 17 (« how do we reliably catch them gaming the setup? ») ; [VK] n° 1 | exact (paraphrase) |
| K2 | « My question was adjacent: if we use this selection function will they fail to goodhart and if they do how? » | [R] l. 5 ; [A] l. 15 ; [VK] n° 2 | exact (cadrage) |
| K3 | « I created an auto research setup. » | [R] l. 3, l. 7 ; [VK] n° 3 | exact |
| K4 | « Agents using LMs propose laws about AI control. » | [R] l. 3, l. 57 ; [VPM2] n° 1 | exact |
| K5 | « All are blind predictions. » | [R] l. 45 (« predictions sealed *before* the data existed ») | exact |
| K6 | « None of the agents decides what survives. » | [R] l. 3 | exact |
| K7 | « Created in Oct with AI code agents. » | [R] l. 5 | exact |
| K8 | « Rules I gave it here https://github.com/lciric/ideation-organism. » | [R] l. 5 (« under written rules »), l. 63 (R5), l. 231 (R12, R5, R9 seulement) ; [M] l. 224 et 225 (programme de conception, registres, décisions du directeur : exclus) | **plus fort que sa source** : le lien ne montre pas les règles données ; il montre le système, dit construit sous règles écrites, et en nomme trois. Lien : code 200 |
| K9 | « Decided by a frozen testing procedure. » | [R] l. 3, l. 45 | exact |
| K10 | « Calculates e-values on new random seeds derived from the law's hash. » | [R] l. 57 (« fresh draws seeded by the hash of the commitment »), l. 68 (l'engagement : contrastes, seuils, budget, graines) | exact en substance ; « law's hash » = empreinte de l'engagement qui porte la loi (très léger) |
| K11 | « Null is composed of all laws previously accepted. » | [N8] l. 11 à 13 (nul = bibliothèque aveugle du juge + nul des filles + nul d'archive [+ membres ajustés en v8]), l. 71 et 72 ; [R] l. 57 (« a library of blind predictors ») ; v3 : « a null containing every accepted law » ([VK] n° 6) | **plus fort que sa source** : le nul *contient* les lois acceptées, il n'en est pas composé |
| K12 | « Ville + e-BH between submissions. » | [R] l. 90, l. 106, l. 122 ; [VK] n° 6 | exact (réserve de [VK] : e-BH entre fiches d'une génération) |
| K13 | « 929 tests run. » | [R] l. 116 (« 906 passed, 8 failed, 15 skipped … (929 tests) ») ; [LK] 2.3 | **plus fort que sa source** : 914 joués, 15 sautés |
| K14 | « I mutated the code intentionally 224 times and the tests caught every mutation, for the expected reason. » | [R] l. 108, l. 117 | exact |
| K15 | « I then attempted to attack it using scripted cheaters on toy problems. » | [R] l. 80 ; [A] l. 15 | exact |
| K16 | « Goodhart by luck, the only cheat that made it into a top 3 placement in your paper » | [K] § 7, p. 10 (« Only one reached the top three on its leaderboard, a lucky re-run of an already effective method » ; « re-run the same model, hoping noise produces a higher score ») | exact (« Goodhart by luck » est l'étiquette de Lazar pour la relance chanceuse) |
| K17 | « (it didn't pass your hold out choice either) » | [K] p. 10 (« no cheating attempt is ever the method we report ») ; [VPM2] n° 3 (§ 2.3, p. 4 ; figure 32a) | exact |
| K18 | « never got promoted here: 0/200 times by renaming an already accepted law. » | [R] l. 84 (T17s, 0 / 200), l. 100 (0 sur 1 000) | exact |
| K19 | « What passed was a mixture or changed version of already accepted laws 75-95% of 200 trials. » | [R] l. 85 à 88 (75 %, 85 %, 95 %, 80,5 %), l. 94 | exact (exploratoire) |
| K20 | « My null didn't have any of these in it. » | [R] l. 82 ; [VK] n° 13 | exact |
| K21 | « By expanding my null to a fitted pooling of all known laws I was able to stop them. » | [R] l. 82, l. 85 à 88 (0 / 200), l. 96 ; [N8] l. 32 (𝓝₈ ⊇ 𝓝₇) | exact |
| K22 | « 0/1000 for each of the 11 ways to kill it that I pre registered. Nov 1st. » | [R] l. 96, l. 100 | exact |
| K23 | « While true new laws continued to pass ~98% of the time. » | [R] l. 102 (0,983 et 0,978) | exact |
| K24 | « I then let LMs attack it. Given the judge's description. With or without its decisions. Nov 2nd https://github.com/lciric/ideation-organism/tree/faff48b/resultats/attaque-goodhart-v2 . » | [A] l. 7, l. 24 ; [P-A1] l. 112 (« le juge … est décrit exactement (boîte blanche) ») ; lien : code 200, dossier présent à `faff48b` | exact |
| K25 | « These toy problems were made only from laws that are already accepted. » | [A] l. 21 à 23 | exact |
| K26 | « If something passes, it is a false claim of a new law. » | [A] l. 21 (« every promotion is a false promotion ») | exact |
| K27 | « One problem was able to be constructed by changing accepted laws per subpopulation. » | [A] l. 23 (W2 : recombinaison par morceaux des deux mêmes lois d'archive) ; [N8] l. 84 | exact (« changing » se lit mieux « switching between », très léger) |
| K28 | « This isn't covered by my null. » | [A] l. 23 ; [N8] l. 83 à 85 | exact |
| K29 | « On that problem, the only model that I could get to finish got a law accepted all 12 times it ran. Whether or not it knew about the decisions. » | [A] l. 7 (« on W2, Argon was promoted in 12 of 12 units »), l. 9 (Argon : 96 suites sur 96, aucune tentative perdue) | exact ; réserve de [VK] n° 19 : « times it ran » = unités, 12 par bras |
| K30 | « The other problem, which my null does cover, wasn't testable. » | [A] l. 7 (« not judgeable (instrument failure) »), l. 22 | exact |
| K31 | « Monitoring bug and spending limit I shared accidentally blocked one provider. » | [A] l. 7 (guetteur, 306 tentatives), l. 9 (garde de dépense commune, 1 212 tentatives) | exact |
| K32 | « I thought that if the attacker knew about the decisions it would allow them to goodhart better. » | [P-A1] l. 101 et 102 (P5) ; [A] l. 7 (P5 fausse) ; [VK] n° 21 | exact |
| K33 | « There weren't many chances for this to happen. 11 out of the 12 accepted laws happened on their first try. Before there was a decision to learn from. » | [A] l. 7 (« 11 of them at the first attempt with or without feedback ») ; [VPM3] n° 1 | exact (« not many » = « barely ») |
| K34 | « So here, if I hid my scores or limited the number of submissions it wouldn't have stopped them. » | déduction de K29 et K33 ; [VK] n° 23 | exact (« here ») |
| K35 | « The two attacks that were successful both used my judge's own record. First what it accepted, then its description. » | [R] l. 94 ; [P-A1] l. 112 ; [VK] n° 24 | exact (synthèse) |
| K36 | « The fix is to expand my null to include some of these combinations. Which I pre registered on Nov 2nd. » | [VK] n° 25 ; [VPM2] n° 7 (scellé le 2 novembre à 23:19 UTC, commit `66dbcf1`) | exact (le 3 novembre à 00:19, heure de Paris) ; c'est un plan public, aucun résultat interne n'est dit |
| K37 | « And expected to lose power on true weak interactions. » | [VK] n° 25 ; [VPM2] n° 7 (P4, P7) | exact |
| K38 | « Have a pre registered retry of my attack. » | [VK] n° 30 ; commit `4848ad9` parent direct de `faff48b` (`git log`) | exact ; réserve : la page liée dit encore « A new preregistration is being written » ([A] l. 11) |
| K39 | « Haven't gotten any real hypothesis accepted yet. » | [R] l. 132 ; [VK] n° 31 | exact (ambiguïté de « real » : [LK] 4.6) |

Décompte : 36 exact, 3 plus fort que sa source (K8, K11, K13), 0 inexact, 0 non vérifiable ; 2 liens justes.

## 3. Contrôle des corrections listées sous le trait

**Heimersheim (v4, 4 corrections ; v5, raccourci)**
1. « measured » → « tracked » : juste ([cv] l. 70, l. 115).
2. « contrastive directions, which can be read from » : juste ([VH] n° 9 ; [R9] l. 9).
3. Phrase de R9 : juste. « Une prédiction que R9 ne fait pas » : [R9] l. 11 (« The author's prior, stated: no prediction »). Nuance : F3 est une hypothèse signée (critique baisse, éloge monte), rapportée hors de l'issue ([R9] l. 25) ; la correction reste juste.
4. « amount » → « amounts » : le texte de la v5 est juste (« interventions » au pluriel, une quantité chacune), mais **la raison donnée, « plusieurs doses », n'a pas de source** : [cv] ne publie aucune dose, et le texte antérieur de Lazar dit « single dose interventions » ([F] l. 26). Voir problème 5.
- v5 : fond inchangé depuis la v4 (mots comparés phrase à phrase) ; seule glose resserrée, « readable contrastive directions » (H10). Changements non listés de la v4 : virgule après « 0.684 », « the » avant « training set » : forme seulement.
- Texte de Lazar relu en entier : aucune affirmation fausse laissée.

**Kirchner (v4, 14 corrections)**
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14 : justes, chacune à sa source (respectivement [K] p. 10 ; [A] l. 21 ; [R] l. 3 ; [R] l. 3 et 45 ; [R] l. 117, citation exacte ; [R] l. 80 ; [R] l. 82, citation exacte ; lignes mortelles du juge, [R] l. 100 ; [P-A1] l. 112 ; [A] l. 22 ; [A] l. 7 ; « here », [VK] n° 23 ; orthographe).
10. Texte juste, **raison incomplète** : Argon a fini les deux mondes (96 suites sur 96, [A] l. 9) ; ce qui impose « On that problem », c'est que « all 12 times » ne vaut que sur W2 (sur W1, Argon seul : 1 sur 12, [A] l. 7).
- **Changement non listé** : « can only be made from » → « were made only from » (K25). Justifié (les mondes sont faits ainsi par choix, non par nécessité), mais absent de la liste.
- Texte de Lazar relu en entier (diff mot à mot, 29 écarts, tous rattachés à une correction sauf celui-ci) : trois affirmations plus fortes que leur source restent, présentes dès son texte (K8, K11, K13).

## 4. Problèmes et corrections minimales (du plus grave au plus léger)

1. **Heimersheim Q2, compte au pire cas au-dessus de la limite dure.** 154 en `\w+`, 153 liens découpés en tous leurs morceaux, 160 en alphanumérique, contre 150 au plus ; le pied dit « environ 146 ». Sûr seulement pour un compteur par blancs (128). Gravité : à décider par Lazar avant de coller (un compteur par blancs est le plus probable ; même alerte que R-1422 pour la v3).
   - Correction minimale, lien épinglé gardé : `(R9, github.com/lciric/sycophancy-psychophysical-law/blob/b3ecaec/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md)` → `(R9, github.com/lciric/sycophancy-psychophysical-law/tree/b3ecaec/preregistrations)`. Compte : 128 par blancs ; 150 au pire cas, sur les trois découpages stricts (exactement la limite). Le dossier existe à `b3ecaec` ; le fichier de R9 y est le seul nommé « R9 ».
   - Avec marge : `(R9, github.com/lciric/sycophancy-psychophysical-law)` : 147 au pire cas (repli déjà noté en R-1422) ; le lien n'est plus épinglé.
2. **Kirchner, K8 « Rules I gave it here <lien> »** : plus fort que sa source (règles non publiées ; [M] l. 224 et 225).
   - « Created in Oct with AI code agents. Rules I gave it here https://github.com/lciric/ideation-organism. » → « Created in Oct with AI code agents, under written rules I gave them. Code here https://github.com/lciric/ideation-organism. » (source : [R] l. 5, « under written rules »).
3. **Kirchner, K11 « Null is composed of all laws previously accepted. »** : plus fort que sa source (le nul contient aussi la bibliothèque aveugle du juge, [N8] l. 11 à 13).
   - → « The null contains all laws previously accepted. » (formule de la v3 vérifiée, [VK] n° 6).
4. **Kirchner, K13 « 929 tests run. »** : 15 tests sautés, non joués ([R] l. 116).
   - → « 929 tests. » (formule de la v3 ; [VK] n° 7 : ne jamais écrire « passed ») ; ou « A suite of 929 tests (906 pass; the 8 failures are provenance checks). »
5. **Heimersheim, raison de la correction 4 (« plusieurs doses ») sans source**, contredite par le texte antérieur de Lazar ([F] l. 26 : « single dose interventions »). Le texte de la v5 reste juste ; rien à changer dans la réponse. Mais Heimersheim lira « amounts » avec ses plateaux ([LH] § 1) : si Lazar a testé une seule dose par intervention, « at the amounts I tested » ne doit pas devenir, à l'oral, un balayage. À corriger dans le pied (traçabilité), et à confirmer par Lazar.
6. **Kirchner, changement non listé** (K25) : ajouter à la liste du pied « 15. « can only be made from » → « were made only from » : les mondes ont été construits ainsi ([A] l. 21 à 23) ». Texte : rien à changer.
7. **Kirchner, raison de la correction 10 incomplète** : à corriger dans le pied (« sur W1, Argon seul : 1 sur 12 ; "all 12 times" ne vaut que sur W2 », [A] l. 7, l. 9). Texte : rien à changer.
8. **Très légers, facultatifs** (aucun n'est faux) :
   - K10 : « derived from the law's hash » → « derived from the hash of the law's commitment » ([R] l. 57) ;
   - K27 : « by changing accepted laws per subpopulation » → « by switching between two accepted laws per subpopulation » ([A] l. 23) ;
   - K38 : la page liée ([A] l. 11) dit encore « being written » pour la relance, déjà scellée (`4848ad9`) ; la mettre à jour est une décision de Lazar (page publique) ;
   - H10 : « readable contrastive directions » peut laisser croire que la lisibilité cause le privilège ([LH] l. 116 à 118) ; pas de place dans 150 mots, à garder pour l'entretien ;
   - H17 et H8 : reconfirmer « Not done yet » et la visibilité publique de `sycophancy-construct-validity` juste avant l'envoi (non retestée ici : 403 par `curl`, refus « robots » par `WebFetch`). La date propre de R9 (4 novembre, 02:00, heure de Paris, [R9] l. 31) passe cette nuit ; R9 reste alors « registered unchanged » : la phrase « I have preregistered » reste juste.
