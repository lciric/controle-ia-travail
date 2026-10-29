# Relecture de la proposition de projet par un sous-agent neuf, et traitement — v1

Le 2026-10-07, de 07:41 à 07:57 UTC environ. Relecteur : sous-agent neuf (il n'a pas écrit la proposition), en lecture seule. Il avait la liste explicite des documents qui font foi (programme v2 ; décisions N-003 à N-008, P-008, N-013 ; proposition N-015 ; état ; résultats de T0.3 ; synthèse et annexes du niveau 2 ; budget ; devis ; brief). Version relue : `proposal-v1.md` de 07:45 UTC (sha256 `eddb5fb9…`, d'après le relecteur), avant les corrections ci-dessous.

**Prononcé du relecteur** : fond fidèle aux décisions ; corrections à faire avant l'envoi ; aucune bloquante, 5 majeures, 7 mineures. Conformes selon lui : budget et parts, devis, 31/31 et 342/544, 98 PDF, 24 rapports, 3 497 citations, 147 lignes, 96 = 64 + 32, 602 tests (recomptés sur une copie hors du dépôt), environ 20 dollars, faits sur P3, énoncés du lemme et du théorème, citation de Terekhov et al. (p. 2), titres et auteurs des références. Rien à redire sur le critère de G1, la porte GC, HC2b et les trois corrections de P-008.

## Traitement, remarque par remarque

Chaque remarque a été vérifiée par la session sur la source citée avant d'être appliquée.

| n° | gravité | remarque (résumé) | source vérifiée | traitement |
|---|---|---|---|---|
| 1 | majeure | Tr : « la robustesse max/attention est établie au niveau du jeton » est une affirmation déjà corrigée (établie dans le cadre testé seulement ; difficulté d'optimisation ; prémisse affaiblie par cinq sources) | `docs/etat-de-l-art/niveau2-v1/corrections-v1.md`, n° 33 (2506.14261v4, p. 6, 10, 19) ; `anteriorite-v1.md`, section Tr | **appliqué** : une étude, pas de preuve générale ; réserve des auteurs ; 2412.09565, 2511.00554, 2507.12691, 2609.36490 cités |
| 2 | majeure | pivot : « autocorrélation ou co-élévation » ne vaut qu'en classe K ; en classe C, un attaquant adaptatif ramène l'autocorrélation à son taux (0,46 → 0,0515) | `docs/notes/resultats-T0.3-v1.md`, point 5 et table E, point 4 ; décision N-003, T3 | **appliqué** : classe K, autocorrélation ou co-élévation ; classe C adaptative, statistiques locales seulement |
| 3 | majeure | H2 : manquent trois occupations partielles (SafeDream 2604.16824, 2604.28129, FIPER 2510.09459) ; seule la conjonction reste non publiée | `anteriorite-v1.md`, section H2 (« Reste revendicable : la conjonction… ») | **appliqué** : composantes publiées citées une à une ; la conjonction est la revendication, « dans les sources vérifiées » |
| 4 | majeure | HC1 : Panin non lu (« à lire avant toute revendication ») ; manquent 2606.18276, 2603.15809 et CALM 2410.02736 | `anteriorite-v1.md`, section HC1 ; décision N-005, section 2 ; R-091 et rapport du lot 6 (CALM) | **appliqué** : les trois sources citées, avec ce qu'elles font et ne font pas ; Panin signalé comme candidat à lire, avec la conséquence prévue par la porte GC |
| 5 | majeure | « quatre pièces retirées » : il y en a au moins huit | décision N-013, sections 2, 3 et 7 | **appliqué** : « au moins huit », liste complétée (ordres en bande, régime à poids réglables, instrument de H5, mécanisme de H7) |
| 6 | mineure | précédents « à citer » absents pour HC3, HC5, H5, H7 | décision N-013, sections 2, 4 et 7 | **appliqué** : une phrase « publié / revendiqué » pour chacune (2508.19461, 2510.09462, 2603.12277, 2605.16626 ; 2605.15377, 2603.13791, 2609.36490, 2605.09684) |
| 7 | mineure | 0,21–0,35 vaut pour l'effet épisode ; 0,17 sous corrélation entre agents | `resultats-T0.3-v1.md`, point 6 | **appliqué** |
| 8 | mineure | « la puissance ne dépend que du budget total » : vrai pour la somme terminale à horizon fixé, faux en lecture séquentielle | décision N-004, L1 et L3 ; `resultats-T0.3-v1.md`, table E, point 1 | **appliqué** |
| 9 | mineure | « after a systematic search » et « open core » sont des affirmations d'absence (R8) ; la détection de collusion en boîte blanche existe (NARCBench) | `registres/etat.md`, T0.2 ; `anteriorite-v1.md`, statistique de population | **appliqué** : « dans les sources vérifiées jusqu'ici » ; NARCBench nommé ; la revendication est la co-élévation lue par des sondes dans le temps |
| 10 | mineure | le résumé omet trois réserves (instrument seulement, L4 non testé ; domaine du harnais ; préenregistrements en brouillon) | `resultats-T0.3-v1.md` (réserve ; table E, point 1) ; `registres/etat.md`, T0.4 et T0.5 | **appliqué** : résumé, section 3 (L4) et section 6 (domaine : H200, au plus 1 192 jetons ; revalidation avant le pilote) |
| 11 | mineure | H6 : le bruit d'activations relève du nœud N-015, ouvert ; le texte retiendrait de fait l'option (a) | `docs/decisions/proposition-N-015-v1.md` | **non appliqué, motivé** : la proposition reprend l'énoncé en vigueur (décision N-013, section 6), qui compte le bruit d'activations, et cite Poser comme précédent ; N-015 est un nœud que seul Lazar tranche. Si Lazar retient (b), une v2 de la proposition retire le bruit d'activations des interventions revendiquées |
| 12 | mineure | « le budget comprend une validation humaine » : faux pour le scénario minimal | `budget-v2.csv` | **appliqué** : « mainline and ambitious budgets », aussi dans le tableau des risques |

## Rapport intégral du relecteur, tel que rendu

J'ai relu la proposition contre les documents qui font foi. Le fond suit les décisions pour l'essentiel, mais il faut corriger avant l'envoi : aucune erreur bloquante, 5 majeures et 7 mineures. J'ai travaillé en lecture seule : aucun fichier du dépôt n'a été modifié ni créé.

Version relue : `livrables/candidature-ea-funds-v1/proposal-v1.md` de 07:45 UTC (sha256 eddb5fb9…). Le fichier a changé pendant ma relecture, mais seul le balisage diffère de la version de 07:40.

Abréviations : `DEC/` = `docs/decisions/` ; `N2/` = `docs/etat-de-l-art/niveau2-v1/` ; `SYN` = `docs/etat-de-l-art/etat-de-l-art-verifie-niveau2-v1.md` ; `T03` = `docs/notes/resultats-T0.3-v1.md`.

| n° | passage | problème | source | correction | gravité |
|---|---|---|---|---|---|
| 1 | « Robust aggregation (maximum or attention) is established at token level. » | Affirmation déjà corrigée. Elle n'est établie que dans le cadre testé : nocivité, modèles de 7 à 14 milliards de paramètres, aucun gradient à travers le moniteur. Les auteurs évoquent une difficulté d'optimisation, et cinq sources affaiblissent la prémisse. | `N2/corrections-v1.md` n° 33 (2506.14261v4, p. 6, 10, 19) ; `N2/anteriorite-v1.md`, section Tr | « In one study (2506.14261), weight-level RL did not evade max/attention probes; this may reflect optimisation difficulty (see 2412.09565, 2511.00554). » | majeure |
| 2 | « If it does not, the negative theorem dictates the aggregator: autocorrelation over time, co-elevation across agents. » | C'est la formule du programme, restreinte par N-003 : elle ne vaut qu'en classe K. En classe C, un attaquant adaptatif ramène l'autocorrélation à son taux (0,46 → 0,0515). Le passage contredit aussi la puce « Local guarantees » de la même section. | `DEC/decision-N-003-N-004-v1.md` §1 (T3) ; `T03`, magnitude 5 et table E (point 4) | « …in class K, autocorrelation or co-elevation; against an adaptive class-C attacker, only local statistics. » | majeure |
| 3 | « …are published; the claim is this specific test. » (H2) | Il manque trois occupations partielles que la synthèse demande de citer : SafeDream 2604.16824 (somme de Page sur des états internes), 2604.28129 (dérive cumulée des activations), FIPER 2510.09459 (seuil calé sur des épisodes réussis seuls). | `SYN` §1, point 3 ; `N2/anteriorite-v1.md`, section H2 | Citer les trois et préciser que seule la conjonction reste non publiée. | majeure |
| 4 | « The claim is the free destination, tested in control monitors under attack, family by family. » | La revendication est posée avant la lecture de Panin (SSRN 7424179), exigée « avant toute revendication ». Il manque aussi 2606.18276 (attracteur libre hors attaque, p. 5-7), 2603.15809 (destination imposée en cadre adverse) et CALM 2410.02736. | `DEC/decision-N-005-N-006-v1.md` §2 ; `N2/anteriorite-v1.md`, section HC1 ; `registres/decisions.md`, R-091 | Citer ces sources et signaler que la porte GC dépend d'une lecture en cours. | majeure |
| 5 | « has already removed four pieces from our claims » | Il y en a au moins huit. S'ajoutent : les ordres en bande qui déplacent les juges (HC3), le régime à poids réglables (HC4), l'instrument de H5 et le mécanisme de H7. | `DEC/decision-N-013-v1.md` §2, 3, 7 | « at least eight pieces, including… » | majeure |
| 6 | « Quorums across judge families are already established and are cited. » ; « Diversity is measured by an attack-transfer matrix over a panel of probes. » (et HC3, H7) | Des précédents que N-013 dit « à citer » sont absents : 2508.19461, 2603.12277, 2605.16626, 2603.13791, 2605.15377, 2609.36490. | `DEC/decision-N-013-v1.md` §2, 4, 7 | Pour chaque hypothèse, une phrase qui sépare ce qui est publié de ce qui est revendiqué. | mineure |
| 7 | « false alarms reach 0.21–0.35 instead of 0.05 » | La plage 0,21–0,35 ne vaut que pour l'effet épisode. Sous corrélation entre agents, le taux est 0,17. Le raccourci vient de N-007. | `T03`, magnitude 6 | « 0.21–0.35 under episode effects, 0.17 under inter-agent correlation » | mineure |
| 8 | « Does power depend only on the total budget as fragmentation varies? » | Restreint par N-004 : vrai pour la somme terminale à n₀ fixé, faux en lecture séquentielle. | `DEC/decision-N-003-N-004-v1.md` §2 (L1, L3) ; `T03`, table E (point 1) | « Does the terminal sum's power, at fixed n₀, depend only on B? » | mineure |
| 9 | « after a systematic search » ; « This is the open core of Paper B. » | Ce sont des affirmations d'absence (R8), alors que le critère 8 reste ouvert et que les recherches affirmatives ne sont pas opposables. De plus, la détection de collusion en boîte blanche existe déjà (NARCBench). | `registres/etat.md`, T0.2 ; `SYN` §4 ; `N2/anteriorite-v1.md`, statistique de population | « In the sources verified so far… » | mineure |
| 10 | « It has been checked in a pre-registered simulation (31 of 31 predictions confirmed). Phase 0 has also validated the activation-logging harness […] Every gate has criteria frozen in advance » | Le résumé omet trois réserves. T0.3 vérifie surtout l'instrument, et L4 n'est pas testé. Le harnais est validé dans un domaine restreint (H200, au plus 1 192 jetons), avec une revalidation prévue avant le pilote. Les préenregistrements de G1 et du papier C sont encore des brouillons. | `T03`, « Réserve » ; `registres/etat.md`, T0.4, T0.5, « Derniers verdicts de porte » | « instrument checks » ; « within a stated domain » ; « to be sealed before data » | mineure |
| 11 | « …context reset, activation noise. » (H6) | Le bruit d'activations relève du nœud N-015, non tranché, dont la recommandation (b) est de ne plus le revendiquer. Le texte retient de fait l'option (a). | `DEC/proposition-N-015-v1.md` | Signaler le nœud, puis aligner le texte après la décision. | mineure |
| 12 | « The budget therefore includes paid human expert validation of the ground truth. » | Faux pour le scénario minimal (0 $), alors que le tableau des risques garde cette parade. | `livrables/candidature-ea-funds-v1/budget-v1.csv` | « The mainline and ambitious budgets include… » | mineure |

Par catégorie :
- (1) contradictions : lignes 1, 2 ;
- (2) restrictions des décisions non reprises : lignes 2, 6, 8 ;
- (3) nouveauté surévaluée : lignes 3, 4, 6, 9 ;
- (4) chiffres : lignes 5, 7, 12 ;
- (5) descriptions d'articles cités : ligne 1 ;
- nœud encore ouvert : ligne 11.

Rien à redire sur le critère de G1 (sans le F1), la porte GC, HC2b ou les trois corrections de P-008.

Conforme aux sources :
- le budget (montants et parts) et le devis (800 à 1 200 heures, 1 200 à 2 700 $) ;
- 31/31 et 342/544 ; 98 PDF, 24 rapports, 3 497 citations, 147 lignes ; 96 = 64 + 32 ;
- 602 tests : je les ai recomptés sur une copie hors du dépôt, 602 collectés ;
- environ 20 $ de calcul dépensé ;
- les faits sur P3 ;
- les énoncés du lemme et du théorème ;
- la citation de Terekhov et al. (p. 2), ainsi que les titres et auteurs des références.

**Verdict : le fond est fidèle aux décisions, mais il faut corriger avant l'envoi. Aucune bloquante ; 5 majeures (prémisse de Tr, agrégateur du pivot, antériorités de H2 et HC1, nombre de pièces retirées) ; 7 mineures.**
