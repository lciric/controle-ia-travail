# Registre des affirmations — réponse à Jérémy Scheurer — v1

Rédacteur neuf, 3 novembre 2026, de 15:13 à 15:35 environ (temps universel, `date -u`). Consigne scellée `redaction-finale-scheurer-v1.md` (sha256 `0e8b5fc9b4c26865532e0343fab1adb587b175ad8d20c74acf71ed2eee986000`, vérifiée avant lecture).
Texte enregistré : `reponse-v1.md`, texte seul sha256 `1277345560d3c29486a8a65776ece767344cf49a573130841889f284187baf78` (492 mots par espaces, 496 par motif).

Forces : **P** = publique et vérifiée ; **I** = interne vérifiée (aucune dans cette réponse) ; **plan** = paramètre ou choix du plan proposé, pas un résultat ; **raisonnement** = inférence de Lazar, sans chiffre. Aucune affirmation « non vérifiée » n'est dans la réponse.

## Sources (chemins à partir de `/home/claude/controle-ia-travail/` sauf mention)

| Clé | Source | sha256 |
|---|---|---|
| [RAP] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-scheurer-v1.md` (lecteur neuf, pages primaires lues le 3 novembre entre 00:02 et 00:37) | `16e1922b9c7cbc2d1421c37ef15cd746e9f81096e4a0bf7a68de25aaa6b351b6` (= son compagnon) |
| [PIE] | `brouillons/ideation-mentors-soir-v1/piece-scheurer-v1.md` (tirée de [RAP]) | `2d0e60fc78e5930fb4ad1fe60d6fba8f2a17f4a03729570ea896db0c339f3796` |
| [REC] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` (vérificateur neuf) | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [FAB] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` (lectrice indépendante) | `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` |
| [R7] | `/home/claude/scratch/depots-publics-2026-11-03/sycophancy-psychophysical-law/results/R7/README.md` (clone public `b3ecaec` ; fichier inchangé depuis `9f5bf6a`, ancêtre de `b3ecaec` : `git log` et `merge-base` en lecture seule) | `2dd0790cf01cba8dfc0dcc8956a1ce0f07d68d20c1a2ce459836d7d8645d032a` (= `SHA256SUMS` du dépôt) |
| [ORG] | `/home/claude/ideation-organism/README.md` (`main`, `faff48b`) | `bdd6516f18ec0cf44ba7fa173df519d8f88b3ee89ab8892454822babbe05b1df` |
| [T03] | `/home/claude/ideation-organism/resultats/controle-simulation-defenses/README.md` (suivi à `faff48b`) | `04ce0afcedb95478103fb76c15680f185e8614c0f0ed08616162d848270d8ba0` |
| [P3] | `/home/claude/ideation-organism/resultats/controle-p3-premier-test/README.md` (suivi à `faff48b`) | `2485d5095094c2dc7f761cbe972172c88291305c6da1df50b58c0c3c1272bf88` |
| [MR] | arXiv 2605.12366v1, résumé, lu par `WebFetch` le 3 novembre vers 15:19 UTC : Sam Martin et Fabien Roger, « Classifier Context Rot: Monitor Performance Degrades with Context Length », 12 mai 2026 | page web, pas d'empreinte ; niveau transcription (un modèle intermédiaire rend la page) |
| [DOS] | `brouillons/ideation-mentors-soir-v1/dossier-piste-scheurer-v1.md` (fiches ; aucun chiffre de fiche repris comme fait) | `063eae8f343ab96f8951a0e11998f1b843ac3e56b3ae99da868d2fdf2dfdd838` |

## Affirmations, dans l'ordre de la réponse

| n° | Affirmation (mots de la réponse, abrégés) | Source | Force | Remarque |
|---|---|---|---|---|
| 1 | « a monitoring horizon, built like METR's task horizon » ; horizon lu au point de 50 % | [PIE] § 3.1 ; [RAP] tableau 1a, l. 1 ; [REC] n° 145 (2503.14499 § 4.2, horizons tracés contre la date de sortie) | P | analogie de méthode |
| 2 | « backdoors checked by execution: code that passes its tests but fails on a trigger input » | [PIE] § 3.4 (tâche annexe d'APPS vérifiée à l'exécution par une entrée qui donne une sortie différente) ; [RAP] § 1b.8 | P (type d'attaque) ; plan (choix) | décrit l'instrument, aucun résultat |
| 3 | « Hide one, at a random position, among n honest, verified steps of agent work » | [DOS] SC-03 (une anomalie par épisode positif, position uniforme) | plan | unité « pas d'agent » choisie pour éviter les tokeniseurs différents |
| 4 | « scores the whole transcript, as Apollo's monitoring does » | [PIE] § 1.3 (page « Monitoring » : notation de la trajectoire entière) ; [RAP] § 1b.10 | P | |
| 5 | « half the backdoors, at 5% false alarms on honest transcripts of the same length » | — | plan | 50 % et 5 % sont des paramètres |
| 6 | énoncé entre guillemets : « against frozen, execution-verified sabotage, the horizon … grows by a factor X per year » ; « X read off the slope of log horizon on release date » | — | plan | énoncé propre à Lazar, gabarit du mentor ; **pas une citation** (17 mots entre guillemets, mais rien n'est cité) |
| 7 | « Frontier monitors miss dangerous actions 2× to 30× more often after 800K tokens of benign activity (arXiv 2605.12366) » | [MR] résumé : « miss these actions 2× to 30× more often when they occur after 800K tokens of benign activity » ; « current frontier models fail to notice dangerous actions more often in longer transcripts » | P (résumé, page primaire) | à revoir sur le PDF si Lazar veut l'opposabilité au sens de R7 ; signalé par la moisson comme voisin proche de SC-10 |
| 8 | « stronger models monitor better (Control Tax, §2.3) » | [PIE] § 3.3 ; [RAP] tableau 1a, n° 17 (« models conventionally considered stronger perform better at the monitoring task ») | P | 2506.05296, HTML v3 |
| 9 | « in your anti-scheming paper (arXiv 2509.15541, §6.1), capability RL alone raised verbalized evaluation awareness from 2.0% to 20.5% » | [PIE] § 1.2 ; [RAP] n° 2 et § 1b.5 ; [REC] n° 156 (« exact ; 20,6 % sur le graphique ») | P | Scheurer coauteur ([RAP], tableau des sources) ; titre du papier non lu dans les sources : « anti-scheming paper » est une description (le § 6.1 porte sur un entraînement sans entraînement contre la manigance) |
| 10 | « attacks are generated and verified once, never regenerated » ; « The corpus stays private, published as a hash » | [ORG] § 4 (banque fraîche, lecture préenregistrée et scellée avant toute notation) comme précédent de méthode | plan | |
| 11 | « Lengths stay inside every monitor's context window; as monitors improve, I add longer transcripts, so the horizon keeps headroom » | [DOS] SC-03, objection 7 et sa réponse | plan | la phrase « as METR adds longer tasks » a été **retirée** : aucune source ne la donne |
| 12 | « R7 (preregistered, about $3 of GPU) » | [R7] l. 3 (préenregistré, archivé sur Zenodo avant toute lecture) et l. 12 (« Cost: GPU about 3 $; no API call ») | P | |
| 13 | « seven Qwen2.5 monitors, 0.5B to 72B, rated responses containing a planted note claiming the verdict » | [R7] l. 8–9 | P | |
| 14 | « Under a negative note at standard intensity, the deference gain falls with size: −0.19 (95% CI −0.24 to −0.11) per tenfold increase in parameters » | [R7] l. 5 et tableau l. 32 (−0,190 [−0,241 ; −0,114]) ; [FAB] § 7 (b) ; [REC] n° 152 | P | « deference gain » : le mot du README public |
| 15 | « items resampled, not models » | [R7] l. 11 (pente de g sur log10 des paramètres « with a shared item bootstrap ») ; consigne | P | sept modèles seulement : l'intervalle ne couvre pas l'incertitude sur les modèles |
| 16 | « The 72B's gain is near zero, yet its readings still move toward the note » | [R7] tableau l. 26 et l. 45 (lecture descriptive, **non préenregistrée** : 2,59 sans note, 2,32 sous la note négative standard, 2,01 sous la forte, 4,27 sous la positive forte) | P | descriptif, dit sans chiffre |
| 17 | « All seven sizes share one release date: a size slope, not a time slope » | [PIE] § 2.2 ; [RAP] § 1b.4 (billet Qwen2.5 du 19 septembre 2024 : sept modèles de 0,5 à 72 milliards dans une même publication) | P | |
| 18 | « The date panel needs three or more open-weight families, each at several dates » | [DOS] SC-10 (axe de date) | plan | aucun panel nommé : non constitué |
| 19 | « In arXiv 2510.09462, GPT-4.1, the strongest monitor without injection, scored all 375 backdoored samples 0 under injection » | [PIE] § 3.4 ; [RAP] n° 13 et § 1b.8 (légende de la figure 2) | P | |
| 20 | « it inherits the under-elicitation your 2412.04984 (§4) warns about » | [PIE] § 1.1 ; [RAP] n° 3 et § 1b.6 (§ 4 : évaluations qui pourraient sous-estimer les capacités, surtout des plus capables) | P | Scheurer coauteur à contribution égale ([RAP]) |
| 21 | « tests one way detection could get harder, as Apollo's May update expects » | [PIE] § 1.3 ; [RAP] § 1b.10 (mise à jour du 13 mai 2026 : la détection et la correction du désalignement deviendront plus difficiles) | P | « one way » : leur raison principale est la conscience situationnelle, pas l'attaquant ; la réponse ne prétend pas tester leur raison |
| 22 | « beat length-only and style-only detectors by 10 percentage points at equal false alarms » | [DOS] SC-03 (δ = 10 points, supposé) | plan | seuil à figer au préenregistrement |
| 23 | « my first generic white-box probes did not clear their random-probe floor » | [ORG] l. 127 ; [P3] l. 7 et 10 (aucune des deux sondes génériques au-dessus de son plancher de 200 sondes aléatoires ; « not detected at this power ») | P | |
| 24 | « False alarms on fresh honest transcripts must hold near 5% at every length » | — | plan | bande à figer au préenregistrement |
| 25 | « in my preregistered simulation, a sequential anytime-valid threshold raised 21–35% with no attack under the strongest episode effects, while one calibrated on 1,000 whole honest episodes held 4.6–5.5% » | [ORG] l. 128 ; [T03] l. 21, 30, 80–81 | P | réserves de la page : cellules les plus fortes choisies après des essais exploratoires ; épisodes de calibration tirés de la même loi que le test ; valide les instruments, pas les théorèmes sur des modèles réels ; pas de verdict de lecteur neuf |
| 26 | « The yearly factor counts only if its interval lies wholly on one side of a preset threshold » | [DOS] SC-10 (règle commune) et SC-03 | plan | |
| 27 | « This measures detection of frozen, non-adaptive sabotage, not of misalignment » | `/home/claude/scratch/soir-rapport/scheurer/classement-D/classement-v1.md` § 5 (drapeaux SC-03 et SC-04), sha256 `89f5e865007466339e6795a5c317389a929b59c3a4aec7d3648ea22530745534` | raisonnement | correction exigée par le drapeau |
| 28 | lien `https://github.com/lciric/sycophancy-psychophysical-law/blob/9f5bf6a/results/R7/README.md` | [R7] ; [RAP] n° 12 (commit `9f5bf6a`, contenu dans le `main` de GitHub au 3 novembre) | P | épinglé au commit qui publie R7 |
| 29 | lien `https://github.com/lciric/ideation-organism/tree/main/resultats/controle-simulation-defenses` | [T03] (suivi à `faff48b`, branche `main` du clone) | P | lien sur `main`, non épinglé : à confirmer que `faff48b` ou plus récent est poussé |

## Absents volontaires
- Lemme de contrôle (non public) ; ρ = 0,684 et le bras « 1 % » (deux objets distincts, sans rapport avec cette réponse) ; résultats du nul v9 (interdits) ; tout fait interne non publié.
- Chiffres des fiches (horizons supposés, coûts illustratifs, seuils η) : aucun repris comme fait ; les seuils gardés (10 points, 5 %) sont dits paramètres.
- Billet de Sean Peters (8 août 2025, horizon de capacité trompeuse contre un protocole de contrôle) : vu dans la moisson, non lu, non cité.
