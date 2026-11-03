# Vérification de la reformulation de Lazar — réponse à Jérémy Scheurer — v1

Vérificateur neuf : je n'ai écrit aucune version de cette réponse. 3 novembre 2026, de 23:21:41 à 23:30:20, temps universel (`date -u`). Consigne `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-reformulation-lazar-scheurer-v1.md`, sha256 `515dd79d59c132604579e9d794d99216b14bb5c1762e0e3697ea173b9bea0ea7`, vérifiée avant lecture.

## Verdict

1. **Aucune affirmation fausse** dans `reponse-v4.md`. Les 18 corrections sont justes ; une seule est incomplète (n° 13).
2. **Deux passages disent plus que la référence vérifiée**, et il faut les corriger avant l'envoi. Le premier porte sur la mise à jour d'Apollo : la v4 a perdu le « one way » de la v3, sur une affirmation de l'employeur de Scheurer. Le second porte sur le seuil calibré : la v4 a perdu le « from the same law » de la v3, juste après « new honest behaviour ».
3. Les liens fonctionnent tous. La v4 fait 610 mots (séparés par des blancs), contre 500 pour la v3 ; aucune limite n'est écrite.

## Pièces et sources

Dossier `brouillons/redaction-finale-v1/scheurer/`. Toutes les empreintes sont conformes à leurs compagnons `.sha256` : `reponse-lazar-reformulee-v1.md`, `reponse-v4.md`, `reponse-v3.md`, `registre-affirmations-v1.md` [REG], `verification-chiffres-v1.md` [VER], `lecture-mentor-v1.md` [LEC].

| Clé | Source | Accès |
|---|---|---|
| [R7] | `git show b3ecaec:results/R7/README.md`, clone `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law` | lu en entier ; numéros de ligne du fichier |
| [T03] | `git show faff48b:resultats/controle-simulation-defenses/README.md`, clone `/home/claude/ideation-organism` | lu en entier ; sha256 `04ce0afc…d8ba0`, égal à [REG] et [VER] |
| [PDF-2510] | `docs/sources/pdf/2510.09462v2.pdf`, compagnon conforme ; texte extrait par `pdftotext` | **seule source opposable** au sens de la règle R7 |
| [W-2605] | https://arxiv.org/abs/2605.12366 (v1, 12 mai 2026, Martin et Roger), résumé | `WebFetch`, niveau transcription |
| [W-2506] | https://arxiv.org/pdf/2506.05296 (v3, 2 mars 2026), § 2.3 « Results », p. 3 | `WebFetch` ; la page de résumé ne contenait pas le corps |
| [W-2509] | https://arxiv.org/abs/2509.15541 (auteurs) et `/pdf/2509.15541` (§ 6.1, p. 17) | `WebFetch` ; 100 000 caractères lus sur 113 209, passage trouvé |
| [W-2412] | https://arxiv.org/pdf/2412.04984 (v2), § 4 « Limitations » | `WebFetch` ; 100 000 caractères lus sur 120 518, passage trouvé |
| [W-APU] | https://apolloresearch.ai/blog/apollo-update-may-2026 (13 mai 2026) | `WebFetch` |
| [W-APM] | https://www.apolloresearch.ai/monitoring/what-makes-a-good-monitoring-prompt (23 juillet 2026) | `WebFetch` |
| [GH] | lien R7 ouvert par `WebFetch` ; `gh api` en lecture sur `lciric/ideation-organism` | 3 novembre 2026, vers 23:25 |

## Tableau des affirmations de `reponse-v4.md` (corps au-dessus du trait)

| n° | Phrase de la v4 (abrégée) | Source et emplacement | Verdict | Remarque |
|---|---|---|---|---|
| 1 | « Something akin to the METR task horizon » | [VER] n° 1 (horizon au point de 50 % ; 2503.14499 § 4.2, horizons tracés contre la date de sortie) | exact | analogie de méthode |
| 2 | « Backdoors verified through execution … pass its test suite, but not when given a certain input » | [VER] n° 2 : [PDF-2510] p. 5, § 4.1 ; consignes en annexe, p. 24 et 26 | exact | |
| 3 | « Insert this at a random point in n steps … known to be honest » | [REG] n° 3 | plan | |
| 4 | « A trusted monitor with open weights rates the full trace. Similar to the Apollo monitoring prompt work. » | [W-APM] : « For this post, we assume full-trajectory grading » ; [VER] n° 3 et [LEC] 1.1. Moniteurs évalués : sonnet-4.6, gpt-5.4 et gemini-2.5-flash, aucun dit à poids ouverts | exact (portée) | La ressemblance vaut pour la note de trace entière, pas pour le type de moniteur. La v3 vérifiée avait la même ambiguïté. Voir P6. |
| 5 | « The horizon is how large n can be … 5% false positives on honest traces of length n » | [REG] n° 5 | plan | |
| 6 | énoncé entre guillemets ; « X is derived from the rate of change in the log of horizon over model release dates » | [REG] n° 6 ; [VER] hors décompte | plan | n'est pas une citation |
| 7 | « There is a rate of change we can observe and only the monitor changes over time » | [VER], hors décompte : la v3 disait « the curve exists », raisonnement appuyé sur 2605.12366 | **plus fort que sa source** (léger) | Aucune évolution dans le temps n'est encore observée. Les sources donnent une courbe selon la longueur et un classement par force. Voir P3. |
| 8 | « Three frontier monitors miss subtly dangerous actions 2x-30x more often after 800k tokens of benign behaviour (2605.12366) » | [W-2605], résumé : « on a dataset that requires identifying when a coding agent takes a subtly dangerous action, » ; « Opus 4.6, GPT 5.4, and Gemini 3.1 miss these actions 2× to 30× more often » ; « when they occur after 800K tokens of benign activity than when they occur on their own » ; [VER] n° 4 ; [LEC] 2.1 | exact | La fourchette ne figure qu'au résumé ([VER] n° 4). Niveau transcription. |
| 9 | « we know stronger models monitor better (control tax section 2.3) » | [W-2506] § 2.3 « Results », p. 3 : « models conventionally considered stronger perform better at the monitoring task » ; [VER] n° 5 | exact | portes dérobées sur APPS ; ni taille ni contexte long : la correction 8 est donc fondée |
| 10 | « In your paper on scheming you show an increase in verbalised awareness of evaluations from capability RL going from 2.0% to 20.5% (2509.15541 section 6.1) » | [W-2509] : § 6.1 « Anti-scheming increases frequency of models referencing being evaluated », p. 17, légende de la figure 15 : « (2.0% → 20.5%) » ; « after capability-focused RL training on an experimental model without anti-scheming training ». Auteurs : Scheurer est 6e sur 19 ; Lazar n'y figure pas ; [VER] n° 6 | exact | Le graphique porte 20,6 %. Un seul modèle expérimental. |
| 11 | « So we freeze … generated once … not be regenerated and kept private only publishing a hash … within the limits of monitor context windows » | [REG] n° 10 et 11 | plan | syntaxe ambiguë : voir P5 |
| 12 | « We have a trend line already for monitor size. » | [R7] l. 5 et l. 38 (« The trend exists under the down note only ») ; [VER] n° 7 | exact, avec les deux phrases suivantes | La réserve de [VER] n° 7 est levée par « only under the negative note », comme dans la v3. Le mot « preregistered » est absent, il n'y a donc plus de lecture « prédiction confirmée ». |
| 13 | « 7 different sized monitors (Qwen2.5) ranging from .5b to 72b » | [R7] l. 8 | exact | |
| 14 | « rate answers that contained a planted note claiming the verdict » | [R7] l. 9 (« claiming the verdict is negative ("down") or positive ("up") ») | exact | |
| 15 | « I expected … a trend by size under both types of notes. Which there was only under the negative note. » | [R7] l. 5 et 38 (M3 faux) | exact | |
| 16 | « −0.19 (95% CI −0.24 to −0.11) in the deference gain, at standard intensity, per 10 fold increase in model size » | [R7] l. 5 ; l. 32 : « −0.190 [−0.241, −0.114] » (note négative, intensité standard) | exact | |
| 17 | « (resampling items not models) » | [R7] l. 11 (« with a shared item bootstrap ») | exact | |
| 18 | « The 72b had a gain close to 0, however its readings still shifted towards the planted note » | [R7] l. 5 et 26 (g = −0,070 [−0,162 ; 0,058] et −0,059 [−0,106 ; 0,001]) ; l. 45, lecture descriptive non préenregistrée : 2,59 sans note, 2,32 et 2,01 sous les notes négatives, 4,27 sous la note positive forte ; [VER] n° 12 | exact | |
| 19 | « Full curves are available. » | [R7] l. 41, 43 et 59 | exact | |
| 20 | « There is only one release date for all seven sizes. So this is a rate of change over size not time. » | [VER] n° 14 (billet Qwen2.5 du 19 septembre 2024) | exact | niveau transcription, non relu ici |
| 21 | « a panel for release date using at least 3 families of open weights » | [REG] n° 18 | plan | |
| 22 | lien `…/sycophancy-psychophysical-law/blob/b3ecaec/results/R7/README.md` | [GH] : page publique ; titre, « Outcome: C, not the predicted A. » et « Cost: GPU about 3 $ » lus ; commit `b3ecaeccf7d9…` | lien valide | |
| 23 | « Depends who is attacking. » | appuyé sur le n° 24 | raisonnement | |
| 24 | « Gpt 4.1 in 2510.09462 failed to detect any of the 375 samples with backdoors under prompt injection » | [PDF-2510] p. 5 : légende de la figure 2 (« a score of 0 to all 375 backdoored code samples ») ; § 4.1 (« the monitor labels all 375 backdoored GPT-5 samples as benign (score 0), despite GPT-4.1 being the strongest monitor when the injection is not present ») | exact | Vérifié sur PDF empreinté. Le contexte (APPS, attaquant GPT-5) est omis. **Réserve sur la référence** : [LEC] 2.7 situe la légende p. 4 ; elle est p. 5, comme le dit [VER]. |
| 25 | « another tier using backdoors from current models … expect it to inherit under elicited behaviours (2412.04984 section 4) » | [W-2412] § 4 « Limitations » : « our evaluations might underestimate models' scheming capabilities, particularly for more capable models » ; sous-section « Uncertainty in Capability Elicitation » ; Scheurer à contribution égale ; [VER] n° 17 | exact sur le fond | Le papier parle de capacités sous-élicitées, pas de comportements. Voir P4. |
| 26 | « Will keep this separate and use the static backdoors as the rate of change » | — | plan | |
| 27 | « Can compare the two to see whether detection gets harder, as the May update from Apollo expects » | [W-APU] : « Detection and correction of misalignment will also get harder, mainly because models will have stronger situational awareness ». Le billet ne parle ni d'attaquants, ni de portes dérobées, ni d'horizon. [VER] n° 18 et [LEC] 1.2 n'ont jugé la v3 exacte que grâce à « one way » | **plus fort que la référence** (moyen) | Voir P1. |
| 28 | « backdoors from a held out generator … 10 percentage points better than length and style based methods … same false positive rate » | [REG] n° 22 | plan | |
| 29 | « If false positives are not held near 5% on new honest behaviour at varying lengths » | [REG] n° 24 | plan | |
| 30 | « In my pre-registered simulation, a sequential anytime-valid threshold got false positives of 21%-35% under the strongest effect of episodes » | [T03] l. 1 et 3 (préenregistrée, lancée une seule fois le 4 octobre 2026) ; l. 16 (aucune attaque ; règle de Ville sur un e-processus de mélange normal unilatéral, α = 0,05) ; l. 21 et 22 (τ = 0,2 : 0,21 à n₀ = 200, 0,35 à n₀ = 1 000) ; [VER] n° 20 et 21 | exact | Le singulier « the strongest effect » est exact : les deux bornes sont à τ = 0,2. Les cellules ont été choisies après des essais exploratoires (l. 80) ; la page le dit. |
| 31 | « When using a threshold created from 1000 episodes of honest behaviour using this method got 4.6%-5.5% » | [T03] l. 30 : « A conformal threshold calibrated on K = 1,000 whole honest episodes, drawn from the same law as the test, gives 0.046 to 0.055 in all 17 settings, for both statistics read » ; l. 32 et 82 : la robustesse à un décalage entre calibration et déploiement n'est pas testée ; [VER] n° 22 ; [LEC] 2.3 | **chiffres exacts, plus fort que la référence dans son contexte** (moyen) | La phrase suit le critère « new honest behaviour ». Sans « from the same law » (présent dans la v3), elle laisse lire une tenue sous décalage. Voir P2. |
| 32 | lien `…/ideation-organism/tree/faff48b/resultats/controle-simulation-defenses` | [GH] : `gh api` : dépôt public (`private: false`), commit `faff48bfc168…` présent, dossier présent à `faff48b` (`README.md`, objet `81236c60…`, égal à [VER] ; `pieces/`) | lien valide | `WebFetch` a été refusé par le site (« robots_disallowed ») : c'est une limite de l'outil, le lien n'est pas cassé |
| 33 | « The yearly factor's interval does not lie wholly on one side of a pre-registered threshold » | [REG] n° 26 | plan | |
| 34 | « … detect a fixed form of sabotage and not an agent's misalignment » | [REG] n° 27 | raisonnement (portée) | |

**Décompte des affirmations factuelles (liens compris)** : 23 au total. 20 exactes : n° 1, 2, 4, 8, 9, 10, 12 à 20, 22, 24, 25, 30 et 32. 3 plus fortes que leur source ou que la référence : n° 7 (léger), 27 (moyen) et 31 (moyen). 0 inexacte, 0 non vérifiable, 0 lien cassé.

## Contrôle des corrections du directeur (sous le trait)

| n° | Verdict | Appui |
|---|---|---|
| 1 | juste | [W-2509] : 19 auteurs, Scheurer 6e, Lazar absent |
| 2 | juste | [R7] l. 5 et 32 |
| 3 | juste | définition, [VER] n° 2 |
| 4 | juste | plan de la v3 (« of the same length ») |
| 5 | juste | Le mot « honest » est celui de la v3 et de [T03]. « At a random point » est un choix de plan de la v3 ([REG] n° 3), pas la correction d'un fait : « at some point » n'était pas faux. |
| 6 | juste | v3 (« only the monitor moves ») |
| 7 | juste | [W-2605] ; lien réparé et valide |
| 8 | juste | [W-2506] : le § 2.3 classe les moniteurs par capacité, pas par nombre de paramètres, et sur APPS, pas en contexte long |
| 9 | juste | style ; « increasing propensity » était ambigu |
| 10 | juste | [R7] l. 9, 38, 5, 26 et 45 |
| 11 | juste | [PDF-2510] p. 5 ; lien réparé et valide |
| 12 | juste | [W-2412] § 4 : l'incertitude est dite, sans sens prédit |
| 13 | **incomplète** | Ce que la mise à jour attend est bien rendu, mais le « one way » de la v3, dont dépendait l'exactitude ([VER] n° 18, [LEC] 1.2), est perdu. Voir P1. |
| 14 | juste au regard de la v3 | C'est un changement de plan (un générateur tenu à l'écart est un test plus dur qu'un lot tenu à l'écart), pas la correction d'un fait : à confirmer par Lazar. |
| 15 | juste | [T03] l. 30 : 5,5 % dépasse 5 % ; la règle « greater than 5% » tuerait déjà la méthode propre de Lazar |
| 16 | juste | [T03] l. 1, 3, 16 et 67 |
| 17 | juste au regard de la v3 | plan ([REG] n° 26) |
| 18 | juste | — |

**Phrases de Lazar laissées telles quelles** (texte entier relu) : aucune n'est fausse. L'une dit plus que la référence (n° 31, P2). Trois appellent une retouche légère (n° 7, 11 et 4 : P3, P5 et P6).

## Problèmes et corrections minimales, du plus grave au plus léger

**P1 — moyen (n° 27, correction 13).** « Can compare the two to see whether detection gets harder, as the May update from Apollo expects. » → « Can compare the two to test one way detection could get harder, as the May update from Apollo expects. »
Raison : la mise à jour dit « Detection and correction of misalignment will also get harder, mainly because models will have stronger situational awareness ». Elle ne parle pas d'attaquants. Comparer deux générations d'attaques sur des traces figées ne teste que la voie de l'attaquant. Scheurer travaille chez Apollo ; [LEC] 1.2 prévoyait son objection, que seul « one way » désamorçait. Coût : +2 mots.

**P2 — moyen (n° 31, phrase de Lazar non corrigée).** « When using a threshold created from 1000 episodes of honest behaviour using this method got 4.6%-5.5% » → « When using a threshold created from 1000 episodes of honest behaviour drawn from the same law as the test, this method got 4.6%-5.5% »
Raison : [T03] l. 30, 32 et 82. La phrase vient juste après « new honest behaviour at varying lengths » ; sans cette précision, elle fait croire que le seuil tient sous un décalage, ce qui n'a pas été testé. La v3 portait ce correctif ([LEC] 2.3). Coût : +7 mots.

**P3 — léger (n° 7).** « There is a rate of change we can observe » → « There is a length curve we can observe »
Raison : aucune évolution de l'horizon dans le temps n'est encore observée. Les sources donnent une courbe selon la longueur (2605.12366) et un classement par force (Control Tax § 2.3). La v3 disait « the curve exists ». Coût : −1 mot.

**P4 — léger (n° 25).** « expect it to inherit under elicited behaviours » → « expect it to inherit under-elicitation »
Raison : le § 4 de 2412.04984 parle de capacités sous-estimées (« Uncertainty in Capability Elicitation »), pas de comportements ; « under-elicitation » est le mot de la v3. Coût : −2 mots.

**P5 — léger, clarté (n° 11, plan).** « They will not be regenerated and kept private only publishing a hash. » → « They will not be regenerated, and will be kept private, publishing only a hash. »
Raison : telle qu'écrite, la négation peut porter sur « kept private », ce qui inverserait le plan. Coût : +2 mots.

**P6 — léger, facultatif (n° 4).** « A trusted monitor with open weights rates the full trace. Similar to the Apollo monitoring prompt work. » → « A trusted monitor with open weights rates the full trace, as in the Apollo monitoring prompt work. »
Raison : le billet du 23 juillet 2026 note la trajectoire entière, mais avec sonnet-4.6, gpt-5.4 et gemini-2.5-flash, aucun à poids ouverts. Rattacher la comparaison au verbe limite la lecture « même type de moniteur ». Coût : 0 mot.

**P7 — léger, lisibilité, facultatif.** « in the deference gain, at standard intensity » → « in the deference gain (0 means no attraction), at standard intensity »
Raison : sans glose, −0,19 n'a pas d'échelle ([LEC] 4.1, « à corriger ») ; la v3 portait la glose. Coût : +4 mots.

**P8 — typographie, facultatif.** « Gpt 4.1 » → « GPT-4.1 » ; « .5b to 72b » → « 0.5B to 72B » ; « The 72b » → « The 72B » ; « (control tax section 2.3) » → « (Control Tax, arXiv 2506.05296, section 2.3) » ([LEC] 2.5, +2 mots).

**Remarque hors faits.** La v4 fait 610 mots (séparés par des blancs, lignes 1 à 13) ; le texte de Lazar en fait 625 et la v3 500. [LEC] § 6 : aucune limite écrite, visée 500. P1 et P2 ajoutent 9 mots. C'est à Lazar de choisir.

## Incidents et interdits

- `WebFetch` sur le lien `tree/faff48b` d'ideation-organism : refusé par le site (« robots_disallowed »). Je l'ai remplacé par `gh api` en lecture, passé sans demande d'approbation.
- La page de résumé de 2506.05296 ne contenait pas le corps ; j'ai lu son PDF par `WebFetch`.
- `grep` sur la sortie de `pdftotext` voyait un fichier binaire : je l'ai relancé avec `/usr/bin/grep -a`.
- Aucun outil n'a demandé d'approbation. Aucun commit, aucun `.sha256`, aucun `git fetch`. Seuls `git show` et `git log` ont été lancés, dans les deux clones nommés. Aucun fichier existant modifié, rien sous `donnees/` ni `/home/claude/coffre-*`, aucun code de dépôt exécuté. Aucun fichier temporaire : `pdftotext` écrivait sur la sortie standard.
