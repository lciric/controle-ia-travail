# Traçabilité des chiffres et des énoncés du README — v1

Rédigée le 2026-10-07 par la session, à la demande de Lazar (« rédige un readme pour les recruteurs et les gens de BlueDot auprès desquels j'ai demandé une bourse career transition »). Document interne (R6) : chaque chiffre et chaque énoncé factuel de `README.md` (copie scellée : `README-v1.md`) renvoie ici à un chemin et à une empreinte SHA-256 (16 premiers caractères ; empreinte complète par `sha256sum` ou dans le `.sha256` compagnon de la source). Les énoncés repris de la proposition de projet (`livrables/candidature-ea-funds-v1/proposal-v1.md`, relue par un sous-agent neuf, R-097) gardent sa traçabilité (`livrables/candidature-ea-funds-v1/tracabilite-proposal-v1.md`).

## 1. Chiffres

| chiffre du README | section | source | empreinte | emplacement |
|---|---|---|---|---|
| phase 0 commencée le 5 octobre 2026 ; porte G0 le 1er novembre 2026 | Statut ; Roadmap | `CLAUDE.md` ; `registres/etat.md` | (vivants) | « Phase en cours » |
| 31 prédictions sur 31 confirmées ; 342 cellules statistiques et 544 trajectorielles ; 0 contraire | En une minute ; Progress | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757` | lignes 29-30 |
| fausses alarmes de 0,21 à 0,35 au lieu de 0,05 sous effet épisode | Progress | `docs/notes/resultats-T0.3-v1.md` | `9ab618edae17e757` | point 6 (règle de Ville) ; voir aussi la traçabilité de la proposition |
| harnais validé sur Llama-3.1-8B-Instruct, carte H200, contextes jusqu'à 1 192 jetons ; rejeu au bit près, accord avec le chemin de référence, sensibilité au défaut injecté, gardes testées ; après une v1 non concluante et une v2 partielle | En une minute ; Progress | `docs/verdicts/verdict-T0.4-critere-1-G0-v3.md` ; `registres/etat.md` | `63444faa4ce253fc` | verdict, l. 11 (lecture gelée) et l. 18 (domaine : 1 192 jetons en production, 1 087 en strict) ; état, ligne de T0.4 |
| 98 PDF d'arXiv ; 24 rapports ; 3 497 citations contrôlées par script ; 0 échec ; 147 lignes de corrections ; aucun énoncé revendiqué occupé en entier | En une minute ; Progress | `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` | `bbe0c1f523ad83e1` | lignes 7, 11, 16, 30 et 58 |
| 18 invites transcrites et vérifiées ; 96 papiers (64 pour le pilote, 32 en réserve) ; règle scellée et tirage par graine | Progress | `registres/etat.md` | (vivant) | ligne de T0.5 (« invites transcrites et vérifiées (18) » ; « pilote de 64 papiers, réserve de 32 ») ; règle de sélection `8f43dcae…` |
| procédure d'extraction scellée après trois contre-lectures et une vérification | Progress | `docs/procedures/T0.5-extraction-v1.md` ; `registres/etat.md` | `d23bd62fe1611b87` | état, en-tête de la passation de 08:02 UTC (R-086, R-092) |
| adaptateurs à dose réglable, dose 0 = modèle de base au bit près ; cinq familles de sondes, plancher apparié en covariance ; réimplémentation de TRACE (2606.07054) | Progress | `registres/etat.md` | (vivant) | lignes de T0.6, T0.7 et T0.8 |
| environ 20 dollars de calcul | Progress | `registres/depenses.md` ; `registres/etat.md` | (vivants) | estimation de ≈ 17,8 dollars le 2026-10-07 à 07:40 UTC, plus les disques (≈ 0,303 dollar de l'heure) ; même arrondi que la proposition |
| 644 tests, environ 15 minutes sur processeur | En une minute ; Reproduce | message du commit `a0d8777` : « 644 tests réussis (917 s) » | — | suite complète du 2026-10-07 vers 11:20 UTC |
| relecture du pilote : deux contre-lectures, une vérification courte, deux relectures des différentiels ; la majeure sur l'environnement hérité par les tests du script | How the work is done | `brouillons/T0.5-pilote-8B-v1-brouillon7.md`, section « Contre-lecture » ; `registres/decisions.md`, R-101 | (brouillon non scellé) ; rapports `prereg/contre-lectures/T0.5-pilote-rapport-relecture-differentiel-b5-v1.md` (`43f0df464806bd23`) | Y-1 du rapport ; test `test_environnement_de_l_instance_sans_effet` |
| P3 : 120 dialogues de cinq tours reproduits au bit près ; trois leçons | About me | `docs/brief-claude-code-programme-complet-v2.md` ; `docs/programme-controle-ia-v2.md` | `9261932a11f29e86` ; `2fd63badb5afea48` | brief, ligne 150 ; programme, l. 84 et section « Leçons de P3 appliquées » |
| proposition de 8 pages | Reading path | `livrables/candidature-ea-funds-v1/proposal-v1.pdf` | `35226dfdf7bf1e36` | R-097 |

## 2. Énoncés

| énoncé du README | source | empreinte |
|---|---|---|
| problème, pari, trois papiers, question pivot, résultats publiés quel que soit le signe | `livrables/candidature-ea-funds-v1/proposal-v1.md`, sections 1 à 4 | voir R-097 |
| citation de Terekhov et al. (« seem theoretically and empirically less promising for mitigating diffuse threats », p. 2) | `docs/sources/pdf/2606.08892v2.pdf` | `aea0f2d192f3744f` (page 2 ; correction n° 123 du niveau 2) |
| moniteurs influencés par la rhétorique de l'agent (2505.23575) ; score injecté adopté (2510.09462) | proposition, section 2 ; rapports de lecture du niveau 2 | PDF `docs/sources/pdf/2505.23575v3.pdf`, `2510.09462v2.pdf` (sceaux compagnons) |
| lemme d'additivité, théorème négatif par groupes de permutations, attaques qui gardent la loi des scores ou seulement leur dépendance | `docs/notes/note-mathematique-lemme-theoreme-v3.md` ; décision N-003/N-004 | `dfe4fe0fc4d02501` |
| règles de travail (préenregistrement scellé, relecteur neuf, verdict de porte par un relecteur neuf, gardes éprouvées, traçabilité, graines, gouvernance) | `CLAUDE.md` (R1 à R14, hiérarchie de décision) ; brief v2 | `9261932a11f29e86` |
| qui fait quoi (Lazar décide ; agents Claude Code sous règles écrites ; erreurs corrélées des relecteurs ; validation humaine payée au plan financé) | proposition, section 5, « Who does what » | voir R-097 |
| contenu de G0 et calendrier des mois 1 à 7 ; pivot si G1 échoue | proposition, sections 4, 6 et 7 | voir R-097 |
| `donnees/` exclu du suivi sauf les sorties de l'extraction, à purger avant publication | `docs/procedures/T0.5-extraction-v1.md`, section 8 ; R-095 (N-014 (a)) | `d23bd62fe1611b87` |
