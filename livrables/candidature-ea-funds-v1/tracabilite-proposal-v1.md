# Traçabilité des chiffres et des énoncés de la proposition de projet — v1

Rédigée le 2026-10-07 par la session. Document interne (R6) : chaque chiffre et chaque énoncé de `proposal-v1.md` renvoie ici à un chemin et à une empreinte SHA-256 (16 premiers caractères ; empreinte complète dans le fichier `.sha256` compagnon de la source, ou par `sha256sum`). Il ne part pas chez le financeur.

## 1. Chiffres

| chiffre de la proposition | section | source | empreinte | emplacement |
|---|---|---|---|---|
| 31 prédictions sur 31 confirmées ; 342 cellules statistiques et 544 trajectorielles ; 0 contraire | 1, 3, 6 | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757` | ligne 30 ; aussi `registres/etat.md`, ligne de T0.3 |
| fausses alarmes de 0,21 à 0,35 sous effet épisode et de 0,17 sous corrélation entre agents, au lieu de 0,05 | 3 | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757` | point 6 (tableau de la règle de Ville) ; reprise abrégée dans `docs/decisions/decision-N-007-N-008-v1.md` (`ab7dc9bb2c96704a`), section 1 |
| une partie du lemme (répartition entre agents au même pas) reste à tester | 3 | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757` | table E, point 1 (« L4 … n'est pas testé ») |
| pivot : classe K, autocorrélation ou co-élévation ; classe C adaptative, statistiques locales seulement | 3 | `docs/notes/resultats-T0.3-v1.md` ; `docs/decisions/decision-N-003-N-004-v1.md` | `9ab618edae17e757` ; `cc1be39369bc4dae` | table E, point 4 ; point 5 (0,46 → 0,0515) ; décision, T3 |
| l'énoncé de 2606.10456 ne tient pas pour sa propre construction | 3 | `docs/decisions/decision-N-003-N-004-v1.md` | `cc1be39369bc4dae` | section 1, « Antériorité » (T0.3, P6.5 : 0,072 / 0,126 / 0,253 au lieu de 0,05) |
| harnais validé sur Llama-3.1-8B-Instruct, critère 1 de G0, carte H200, après une v1 non concluante et une v2 partielle ; domaine : contextes jusqu'à 1 192 jetons ; revalidation avant le pilote | 1, 6 | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` ; `registres/etat.md` | `63444faa4ce253fc` ; voir l'empreinte de l'état au commit | verdict, section 1 ; état, lignes de T0.4 (domaine de validité, R-052) et de T0.5 (revalidation, P-007) |
| 98 PDF d'arXiv ; 24 rapports ; 3 497 citations ; 0 échec ; 147 lignes de corrections | 6 | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` | `bbe0c1f523ad83e1` | lignes 7, 11, 16 et 58 |
| aucun énoncé revendiqué occupé en entier | 5 | même synthèse ; lot 6 : `docs/decisions/proposition-N-015-v1.md` (occupation partielle de H6, nœud ouvert) | `bbe0c1f523ad83e1` | ligne 30 de la synthèse |
| au moins huit pièces retirées des revendications | 5 | `docs/decisions/decision-N-013-v1.md` ; `docs/decisions/decision-N-005-N-006-v1.md` ; `docs/decisions/decision-N-007-N-008-v1.md` | `157d388ef5d0f4df` ; `cd49afbc924cb1dd` ; `ab7dc9bb2c96704a` | N-013, sections 1 (probabilité du jeton), 2 (ordres en bande), 3 (poids réglables), 6 (bruit sur les poids), 7 (instrument de H5, mécanisme de H7) ; N-006, section 3 (quorum entre familles) ; N-007, section 1 (« application aux sondes ») |
| 18 invites ; 96 papiers (64 pour le pilote, 32 en réserve) ; procédure d'extraction scellée après trois contre-lectures et une vérification | 6 | `registres/etat.md` | `4f697da76d56177b` | ligne de T0.5 ; procédure `docs/procedures/T0.5-extraction-v1.md` (scellée, `d23bd62f…`) |
| 602 tests automatisés | 6 | `python -m pytest --collect-only -q` au commit `971725e` : « 602 tests collected » ; suite complète relancée le 2026-10-07 vers 07:44 UTC sur le même code : « 602 passed in 346.43s (0:05:46) » | — | sortie dans le message du commit de ce livrable |
| environ 20 dollars de calcul dépensés | 6 | `registres/depenses.md` | `f5dc9bc2834325bf` | relevé du 2026-10-06 à 13:25 UTC : ≈ 12,3 dollars, plus les disques à ≈ 0,303 dollar de l'heure ; calcul : ≈ 12,3 + 18,25 × 0,303 ≈ 17,8 dollars le 2026-10-07 à 07:40 UTC, arrondi à « environ 20 » (les disques restent facturés jusqu'au geste de N-012) |
| devis du plan entier : 800 à 1 200 heures-équivalent A100, 1 200 à 2 700 dollars stockage compris | 11 | `livrables/premier-rendu-v1/devis-v1.md` | `16d71febf1491780` | section 2, ligne « Total » |
| montants des trois scénarios | 1, 11 | `livrables/candidature-ea-funds-v1/budget-v2.csv` | (scellé avec ce livrable) | toutes les lignes |
| parts du scénario central (65,4 % ; 6,5 % ; 7,8 % ; 4,4 % ; 5,5 % ; 1,3 % ; 90,9 % ; 9,1 %) | 11 | calcul sur `budget-v2.csv` : montant de la ligne divisé par 91 740, arrondi au dixième | — | — |
| P3 : 120 dialogues de cinq tours reproduits au bit près | 12 | `docs/brief-claude-code-programme-complet-v2.md` | `9261932a11f29e86` | ligne 150 (« 120 chaînes de cinq tours ») |
| leçons de P3 (fenêtre tronquée, catégoriel plat contre ordinal) ; non-transfert de Llama à Qwen | 4, 9, 12 | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48` | section 10, « Leçons de P3 appliquées » ; section 15 |
| citation de Terekhov et al. (« seem theoretically and empirically less promising… ») | 2 | `docs/sources/pdf/2606.08892v2.pdf` | `aea0f2d192f3744f` | page 2 (lignes 117 à 119 de `pdftotext -f 2 -l 2`) ; correction n° 123 de `docs/etat-de-l-art/niveau2-v1/corrections-v1.md` (`747b07561d93642c`) |

## 2. Énoncés retenus

| énoncé de la proposition | source | empreinte |
|---|---|---|
| lemme L (invariance terminale, séparation avec le maximum, lecture toujours valide, détection avant le dommage) ; théorème T (aveuglement, impossibilité, garanties locales, classes C et K) ; ce qui est revendiqué et ce qui est cité | `docs/decisions/decision-N-003-N-004-v1.md` | `cc1be39369bc4dae` |
| deux précautions du lemme (GROW, 2208.07610 ; Θ(γ), 2601.20022) ; budget total borné comme choix de modélisation déclaré ; environnement « reconstruit » | `docs/decisions/decision-P-008-v1.md` | `ac9551b044c10ca9` |
| H2 retenue ; quatre bases ajoutées ; critère de G1 sans F1, planchers rapportés | `docs/decisions/decision-N-007-N-008-v1.md` | `ab7dc9bb2c96704a` |
| HC1 à destination libre ; porte GC ; HC5 (quorum par type d'accès) | `docs/decisions/decision-N-005-N-006-v1.md` | `cd49afbc924cb1dd` |
| HC1 sans la lecture par probabilité du jeton comme pièce revendiquée ; HC3 ; HC4 (régime « contexte seul » ; 2609.36490, p. 1) ; HC5 ; HC2b « trahison par les activations » ; H6 sans le bruit sur les poids ; H5 ; H7 ; bras « sonde du lecteur » | `docs/decisions/decision-N-013-v1.md` | `157d388ef5d0f4df` |
| H6 : précédent de Poser (2405.05466) cité sans trancher N-015 ; la formulation reste compatible avec les options (a) et (b) du nœud | `docs/decisions/proposition-N-015-v1.md` | voir son `.sha256` |
| hypothèses H1, Tr, H8, HC2, HC6, H3, H4′ ; portes G2, G3 ; invariants de protocole ; bascules ; succès | `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48` |

## 3. Références citées (PDF récupérés et scellés par la session)

Chaque PDF est dans `docs/sources/pdf/`, avec son compagnon `.sha256` ; provenance dans `docs/sources/pdf/provenance-*.md` ; titres relevés dans ces fichiers de provenance. Le titre de 2604.01151 a été lu sur la page 1 du PDF (`pdftotext`).

| identifiant | empreinte | | identifiant | empreinte |
|---|---|---|---|---|
| 2606.08892v2 | `aea0f2d192f3744f` | | 2505.23575v3 | `04c44d4ac7c4d2c1` |
| 2607.07368v1 | `d72cae4337e824e4` | | 2510.09462v2 | `96c16e33b27b9633` |
| 2607.02514v2 | `9baceea4719a5ff2` | | 2607.08066v1 | `f22075f04c845a50` |
| 2605.31593v1 | `037f653703ec0da1` | | 2606.07897v2 | `e025464dba714bb5` |
| 2604.01151v3 | `bde99a620dbbb406` | | 2508.07805v1 | `4cc15dcde9a22a79` |
| 2512.03109v2 | `b7a46e4cf781aec0` | | 2609.36490v1 | `eb6d5bbe9bfaff0a` |
| 2607.06503v2 | `ae2a2d307373c145` | | 2412.01784v3 | `7fbe44ec6d764951` |
| 2606.07054v1 | `9e169bb5eced6fb2` | | 2405.05466v2 | `aa781893236e877a` |
| 2605.27690v2 | `ebcbb371a78f3d4a` | | 2606.10456v2 | `aaeedd1e7a88203e` |
| 2504.10374v1 | `5f802d679344fe5e` | | 2208.07610v2 | `e9e5fd4e0096e3be` |
| | | | 2601.20022v2 | `8d090f3171ef76ca` |

Références ajoutées après la relecture (citées dans le texte par leur identifiant ; toutes lues au niveau 2 ou au lot 6, rapports dans `docs/sources/lecture-pdf-niveau2/` ; descriptions tirées de `docs/etat-de-l-art/niveau2-v1/anteriorite-v1.md`, sections H2, Tr, HC1, et de la décision N-013) :

| identifiant | empreinte | | identifiant | empreinte |
|---|---|---|---|---|
| 2604.16824v1 (SafeDream) | `ad860956062a13a0` | | 2603.12277v6 | `609332fdfaae3583` |
| 2604.28129v1 | `f656c9b7e7fbd5d6` | | 2605.16626v2 (SLEIGHT-Bench) | `1ba418227095eeea` |
| 2510.09459v2 (FIPER) | `df815e61dc535ff2` | | 2605.15377v2 | `fe591700228b29dc` |
| 2603.15809v1 | `29316c29e444175f` | | 2603.13791v1 | `0b2b155024d67bae` |
| 2606.18276v1 | `8332adc89c0d75f8` | | 2605.09684v1 (MonitoringBench) | `35bb09b49f85578e` |
| 2410.02736v2 (CALM) | `d67bb6157df77fad` | | 2506.14261v4 | `4b0960622664e77d` |
| 2508.19461v1 | `24365928b67324f9` | | 2412.09565v2 | `9c23a613c5c7e3a2` |
| 2511.00554v1 | `17708292f357ddee` | | 2507.12691v3 | `0c00a77b0c07bb9a` |

## 4. Réserves

- Relecture par un sous-agent neuf : `relecture-proposal-v1.md` (rapport intégral et traitement) ; 11 remarques sur 12 appliquées, la remarque sur H6 (nœud N-015 ouvert) laissée avec motif.

- Les descriptions des travaux cités suivent les documents de décision et les rapports de lecture du niveau 2. Pendant la rédaction, seuls la citation de 2606.08892 (page 2) et le titre de 2604.01151 ont été relus sur le PDF.
- « To our knowledge, after a systematic search » (section 2, coût de déplacement d'une sonde) est une affirmation d'absence (R8). Elle repose sur les recherches affirmatives du 2026-10-06 (`docs/sources/recherche-affirmative-20261006/`, non opposables) et sur les lectures du niveau 2. La revendication correspondante est HC4, telle que N-013 l'a fixée.
- La proposition mentionne la famille (iii) d'organismes (70B) dans le seul scénario ambitieux, comme le budget ; le programme la prévoit « si la licence le permet » et P-002 la limite au 70B.
- Mise en page : `scripts/document_pdf.sh` (pandoc 3.9 du venv, puis Chromium par Playwright) ; feuille de style `proposal-v1.css`. Le PDF n'est pas reproductible au bit près (dates internes du PDF) ; son texte l'est depuis `proposal-v1.md`.
