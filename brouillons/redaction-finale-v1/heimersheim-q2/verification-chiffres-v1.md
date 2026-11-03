# Heimersheim, question 2 — vérification des chiffres de `reponse-v1.md` — v1

Vérificateur neuf (sous-agent) : je n'ai écrit ni la réponse, ni son registre, ni aucune version des réponses de Lazar Ciric au formulaire Pivotal. 3 novembre 2026, de 13:07 à 13:13, temps universel coordonné (`date -u`). Consigne : `brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/verification-chiffres-heimersheim-q2-v1.md`, sha256 `3f043da83f820eb15f411ccb4ff983f84fa65e8d475b6cd7a8d327d0b1d60e3d` (recalculée, conforme).

Fichiers vérifiés (empreintes recalculées avant lecture, conformes) :
- réponse : `brouillons/redaction-finale-v1/heimersheim-q2/reponse-v1.md`, `61b484ae91e8461690eae2663e7dbbff81a01e7eaa2e51b4ba5cf92dc914d4f1` ;
- registre du rédacteur : `brouillons/redaction-finale-v1/heimersheim-q2/registre-affirmations-v1.md`, `143a876524e19c66afbc64e5dabc7bb6e83c8524c3a517d25311e6f8efce8548` ;
- question : `brouillons/candidature-pivotal-v16/formulaire-site-colle-par-lazar-2026-11-03-1209.txt` (`57393598f012eb641e709db42efe4b52321c7061e0ff8954910f061019f7b5c6`), lignes 20 à 24 : « Why do you want to work on Mechanistic Interpretability? », « Max. 150 words ». La réponse fait 130 mots séparés par des espaces (`wc -w` sur sa première ligne), comme le dit son pied.

## Sources

Clones sous `/home/claude/scratch/depots-publics-2026-11-03/` ; fichiers internes relatifs à `/home/claude/controle-ia-travail`. Aucun `git fetch` : état des clones au clonage (12:21 selon le registre). Aucun code des dépôts exécuté ; le fichier JSON a été lu par `python3 -I` hors du dépôt.

| abréviation | fichier ou page | état | sha256 |
|---|---|---|---|
| [cv] | `sycophancy-construct-validity/README.md` | public ; `HEAD` = `146b2a450f50…` = `origin/main` local | `de5d6032d42cc2eb893e2d1339ae0c6423c4cebc2e1b7ecc83d35cf9c3154da8` |
| [tr] | `sycophancy-construct-validity/TRACEABILITY.md` | même commit | `3339f54ba0be09b76134dd692d8aa27c48a248010fb0b1b36fdec1dd53d30f98` |
| [sae] | `sycophancy-construct-validity/results/sae_residual_analysis.json` | même commit | `9211202be6cb01523bafdb65686ae79c672223b22a726789f5991906d3b98510` |
| [R9] | `sycophancy-psychophysical-law/preregistrations/2026-11-02_addendum_R9_feature_specific_error_correction.md` | public ; `HEAD` = `b3ecaeccf7d9…` = `origin/main` local | `81abd962afe1ba8f99840a8b54262b1820184e5a767139712d1e5898d28ce36e` |
| [R9b] | `sycophancy-psychophysical-law/preregistrations/2026-11-03_addendum_R9bis_dose_curves.md` | même commit | `8c7145036f06ccc8dcd6b4e918d002adb65a6f51917013595263526ec87c5009` |
| [st] | `sycophancy-psychophysical-law/STATUS.md` | même commit | `b0ed2c9802e4c9d17c385c1c533cc27e66188bcb05960fd88d8bab119c256bab` |
| [arx] | arXiv 2606.24964, page de résumé (`https://arxiv.org/abs/2606.24964`), lue par `WebFetch` vers 13:08 : version 1, seule version, soumise le 23 juin 2026 | primaire, niveau transcription (modèle intermédiaire, citations de 125 caractères au plus, page non empreintée ; règle R7) | — |
| [lec] | `brouillons/pilote-exposant-p-v1/lecture-2606-24964-v1.md` | interne | `3c550d93ae97e37309ef01a95e1829c946463edf1cd7013110c95c2eed815851` |
| [rec] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/recoupement-v1.md` | interne | `bea573aa1e62d5d5bfb1aa677a902c9ec977ea1740941eed5b4277bae0e4fe0a` |
| [rap] | `brouillons/candidature-pivotal-v16/lecture-approfondie-v1/rapport-heimersheim-v1.md` | interne | `b55e2f243974dcccb52480a0a2cd803dd7cf6497b430b4e9926b4f7eba8aabfd` |
| [fab] | `brouillons/canal-fable-v1/fable_2026-11-03_n001.md` | interne | `4b9bd5c929e272acd2910722765483bb7a05d53df352ec32e23adbd4992f9e96` |

## Tableau

| n° | phrase exacte (extrait de la réponse) | source et emplacement | verdict |
|---|---|---|---|
| 1 | « reading a behaviour did not let me control it » (le fait sous le « because ») | [cv] l. 1 (titre « Reading a Concept Is Not Controlling It »), l. 3 ; l. 25 à 30 (la baisse au rang 3 ne se reproduit pas) | exact |
| 2 | « In Llama-3.1-8B-Instruct » | [cv] l. 3 ; l. 112 (« One model. Llama 3.1 8B Instruct only. ») | exact |
| 3 | « a probe direction tracked sycophancy » | [cv] l. 61 (« The probe direction of *Geometry* below (ρ = 0.684) »), l. 70 (corrélation projection–comportement), l. 3 (« opinion sycophancy is linearly readable ») ; [tr] l. 42 et [sae] : clé `proj_probe` | exact. Le dépôt borne la portée à la sycophancie d'opinion ([cv] l. 3, l. 113). « probe » est le bon mot : l'autre projection du fichier, sur la direction d'addition d'activations contrastives, ne suit rien (`proj_caa.rho_original` = −0,059, [sae]) |
| 4 | « ρ = 0.684 » | [sae] `proj_probe.rho_original` = 0,684362912466355 ; [tr] l. 42 ; [cv] l. 61, 70, 115 ; [fab] § 3 | exact |
| 5 | « possibly training fit » | [cv] l. 115 (« so ρ may also be training fit »), l. 70 (« treat them as training fit ») ; [fab] § 3 (« may be training fit : juste ») | exact |
| 6 | « yet no single-direction intervention I tried reduced it » | [cv] l. 3 (« no single-direction intervention and no head ablation reduced the judged rate »), l. 21 (« produced no clean reduction » ; sorties brutes non gardées, aucun nombre), l. 88 ; [fab] § 3 | exact, qualitatif (le dépôt ne donne aucun nombre ; la réponse non plus) |
| 7 | lien « github.com/lciric/sycophancy-construct-validity » | clone frais ; commit `146b2a4` présent, tête de `origin/main` locale ; `README.md` présent | exact. Réserves : lien non épinglé, le lecteur verra la tête du jour ([fab] § 2 conseillait d'épingler ρ à `146b2a4`) ; visibilité publique non retestée depuis cette session (GitHub hors des adresses permises par le relais ; interface `gh` refusée, code 403) ; [fab] l. 5 parle de « dépôts publics » |
| 8 | « Your paper with Ferreira da Silva » | [arx] : auteurs, dans l'ordre, Francisco Ferreira da Silva et Stefan Heimersheim ; titre « Evidence for feature-specific error correction in LLMs » ; [lec] l. 14 ; [rap] l. 21 | exact |
| 9 | « finds that contrastive directions […] are privileged under your error-correction test » | [arx] résumé : directions « pures », « constructed from contrastive prompt pairs » ; « indicating that the pure directions are privileged » ; résultat reproduit sur six modèles ; [lec] § 3 (Gemma-2-9B, couche 2 : moyenne 2,42 [2,29 ; 2,62]) ; [rec] n° 7 | exact, au niveau de la famille : les paires varient (sur Llama, de 1,28 à 3,79, [lec] l. 68) ; le papier tient p > 2 pour nécessaire, non suffisant ([lec] l. 92) ; la réponse dit « privileged », pas « features » |
| 10 | « readable by construction » | [lec] l. 37 (différence des moyennes sur au moins 30 paires d'invites appariées, équations 4 et 5) ; [arx] (« constructed from contrastive prompt pairs ») | exact comme glose de la définition : une différence de moyennes sépare par construction les moyennes des deux classes. Le papier ne mesure pas la lisibilité |
| 11 | « (p > 2) » | [arx] résumé : « p>2 » pour les directions contrastives et deux autres familles de traits, p ≈ 2 pour les témoins aléatoires et en composantes principales ; [lec] l. 58 (légende de la figure 6, « Fitted exponents remain above p = 2 across all variations » ; moyennes des contrastives dans [2,24 ; 2,63], § 4.3) ; [rec] n° 44 | exact (seul un seuil entre dans la réponse, aucun nombre de l'article) |
| 12 | « I have preregistered both measurements » | [R9] l. 3 (écrit le 2 novembre, « before any forward pass of R9 ») ; [st] l. 29 (archivé dans la version v2026.11.5 sur Zenodo, 10.5281/zenodo.23909891, le 3 novembre à 06:49) ; [R9b] l. 3 et l. 5 (écrit le 3 novembre, avant toute passe) | exact. R9 seul porte déjà les deux mesures (F2 et F3). R9-bis est public au commit `b3ecaec`, mais son archive Zenodo reste à faire ([R9b] l. 3 ; [st] l. 54) ; la réponse ne cite pas Zenodo |
| 13 | « on the directions that social pressure adds to the activations » | [R9] l. 16 (deux directions : différence des moyennes, sur 30 paires, de l'activation au dernier jeton de l'invite avec et sans la phrase de pression, critique et éloge) | exact comme description de la construction. Nuance : [R9b] l. 9, sans la direction neutre jumelle, « "pressure" cannot be told apart from "any aside appended to the prompt" » |
| 14 | « your test » | [R9] l. 20 (les `sweep_2d.py` et `fit_pairs.py` du papier, réglages canoniques), l. 24 (F2) ; [R9b] l. 52 (F2 inchangée) | exact (écart déclaré : modèle Instruct au lieu du modèle de base du papier, [R9] l. 15) |
| 15 | « whether rotating toward them moves the model's ratings » | [R9] l. 20 (ancres B : note attendue Σ k·p(k) / Σ p(k) sur les jetons « 1 » à « 5 », à chaque angle de rotation), l. 25 (F3, « reported, not in the outcome ») ; [R9b] l. 54 à 57 (F3 en courbe, même statut) | exact. La « note » est l'espérance sur la loi du jeton suivant, pas une note générée ; la mesure est rapportée hors de l'issue, et la réponse ne dit pas qu'elle décide |
| 16 | « R9 and R9-bis » | titres de [R9] l. 1 et de [R9b] l. 1 | exact |
| 17 | lien « github.com/lciric/sycophancy-psychophysical-law » | clone frais ; commit `b3ecaec` présent, tête de `origin/main` locale ; [R9] et [R9b] présents sous `preregistrations/` | exact. Mêmes réserves qu'au n° 7 ; le lien mène à la racine, pas aux deux fichiers |
| 18 | « not yet run » | [R9b] l. 5 (« R9 has not run ») ; [st] l. 29 (« R9 has not run ») et l. 54 (reste à archiver R9-bis, signer son budget, lancer) ; aucun `results/R9/` au commit `b3ecaec`, ni sur la branche `origin/prereg/2026-11-02` (`git ls-tree`) ; aucune trace de lancement de R9 dans `registres/` | exact à l'état du clone. Dépend de l'heure d'envoi : à reconfirmer juste avant (fin fixée par [R9b] l. 66 : 10 novembre, 23:59, heure de Paris) |

Non comptés (motivation, question, conditionnels) : « I want to work on mechanistic interpretability because », « My question is whether a direction the network privileges also controls the behaviour it predicts. », « If yes, your test could screen steering targets, such as an evaluation-awareness direction; if no, privilege and control need separate tests. »

Force des résultats de Lazar : aucun n'est présenté plus fort que sa source. ρ porte sa réserve ; les interventions à une direction restent qualitatives ; ni « < 1 % » ni « 68 % » (non publics, [fab] § 2) ; ni la baisse au rang 3 ; R9 est dit non lancé.

## Corrections minimales

Aucune correction obligatoire.

Précisions facultatives (l'exactitude ne change pas) :
- n° 3 : « tracked sycophancy » → « tracked opinion sycophancy » ; raison : portée du dépôt ; source : [cv] l. 3 et l. 113.
- n° 13 : « that social pressure adds » → « that a pressure sentence adds » ; raison : c'est la construction, et pression et aparté quelconque ne se séparent qu'avec la direction neutre ; source : [R9] l. 16, [R9b] l. 9.
- Les deux ensemble : 132 mots séparés par des espaces ; au pire compte du pied de la réponse (148), 150, encore dans la limite.

## Décompte

- exact : 18 (réserves : n° 7 et 17, liens non épinglés et visibilité publique non retestée ici ; n° 18, à reconfirmer avant l'envoi ; n° 8 à 11, papier lu au niveau transcription) ;
- inexact : 0 ;
- non vérifiable : 0 ;
- non publié présenté comme publié : 0.
