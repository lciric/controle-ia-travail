# Traitement des vérifications de la synthèse v3 « comment détecter » (tour 2) — v1

Session 14, 2026-10-20 vers 18:30 UTC. La session corrige, faute de place pour un troisième chantier de sous-agents
(deux au plus à la fois, R-216, R-270) ; elle n'a écrit ni la v1, ni la v2, ni la v3, ni les extractions, ni les
vérifications. Rapports traités :
- sens : `…/revue-detection/verification-v3-sens-v1.md` (`256f918174e95f2e2991f39be90c0c89378e7030856aab4f342140911d1428ba`),
  « non conforme », deux majeurs, cinq moyens, sept mineurs ;
- fidélité : `…/revue-detection/verification-v3-fidelite-v1.md`
  (`987b39ea1ea612206bbabc44ce4ff66102adf4da19f10cbe0199b2c9422fa875`), « conforme après corrections », trois mineurs,
  quatre de forme.

Tous les constats sont acceptés, avec la correction proposée par leur rapport. Les phrases et chiffres ajoutés viennent de
ces rapports, qui les donnent à la page et à la ligne ; la session n'a ouvert aucun PDF et n'ajoute aucun chiffre.
Différentiel : `…/revue-detection/correction-tour3/appliquer_corrections_v4.py` (2 blocs, 46 remplacements, chacun
trouvé une seule fois). v4 : `…/revue-detection/synthese-comment-detecter-v4.md`.

| constat | décision | où (v4) |
|---|---|---|
| VV3-sens-01 (majeur) : P3-P3 comparé à des contrastes de type T1 | accepté : contrastes séparés par type ; analogues de P3-P3 cités ([PAR] « Backdoors » 0,844 et 0,768 ; [LB] 0,58 à 0,95 ; [DYL] 0,74 ; rappel 0,03 de [BX]) ; [BX] et [YS] rangés en T1 ; « rien d'écrit dans l'empan lu » retiré pour eux ; rang 2 : hypothèse écrite, pouvoir « faible à moyen » | section 1, point 2 ; 2.1 ([BX], [PAR]) ; section 3, rangs 2, 3 et 9 ; « ce qui a changé » |
| VV3-sens-02 (majeur) : échec de la question généralisé à tort | accepté : issue selon les données d'apprentissage de la sonde (Roleplaying contre Pairs) ; rang 4 ; prédiction de E2 ; nœud E2 ; piège de E2 | section 1, point 1 ; rang 4 ; table E2 ; section 5 |
| VV3-sens-03 : [AU] « en moyenne » ; « +X » ; « +System » | accepté | section 1, point 2 ; 2.1 ([AU]) ; rang 3 |
| VV3-sens-04 : T1 « à contexte égal » | accepté : « à consigne égale » ; prédicteurs triviaux et coûts déjà déclarés pour T1 partout ; T1 ne vaut qu'avec T4 au champ et dans E2 | règles communes ; table E2 ; confiance |
| VV3-sens-05 : manipulation du nombre | accepté : inconvénient et recommandation de la note cités ; facteur « contexte » précisé ; prédiction de la proposition D reprise ; confiance 50 % | section 4 ; nœud « E2 et manipulation » |
| VV3-sens-06 : mention absente de T0.6 ; coût de T0.6 | accepté : témoin et mention à jouer ; coût « à deviser », avec P-015 ; nœud de dépense possible | table, coûts et contrôles de E2 et E3 ; dépense |
| VV3-sens-07 : « E3, seule voie » | accepté : E3, ou E2 sur épisodes neufs selon la règle gelée 1 | recommandation (4) ; nœud « Revendication » |
| VV3-sens-08 : bras « moyenne » de P3b ; couches multiples | accepté : bras (iii) hors du GO de N-028, extension (nœud) ; couches multiples restreintes à T0.7 et aux épisodes neufs | table E1 ; concepts, couches, positions |
| VV3-sens-09 : confiances | accepté : raisons hors sujet retirées ; raisons tirées des faits | confiance |
| VV3-sens-10 : couches | accepté : [BX] p. 3 en contre ; [CA] ne compare pas ; rang 6 « faible à moyen » | section 1, point 1 ; rang 6 |
| VV3-sens-11 et VV3-fidelite-04 : [AP] p. 23, deux sondes | accepté | section 1, point 1 ; rang 4 |
| VV3-sens-12 : E4 « fixé d'avance » | accepté : bras écrit dans un texte scellé avant toute lecture de E1 à E3 | table E4 |
| VV3-sens-13 : capacité de Llama ([DYL] p. 5) | accepté : phrase citée, transposition déclarée (R8) | section 1, point 1 |
| VV3-sens-14 (a) à (e) | accepté : « peut tenir » ; P3-P4 et T3 neufs ; oracle (T4 ; P3-P4 n'est pas un test) ; ligne nouvelle pour N-028 ; E2 sur la condition qui réplique P3 | 2.2 ; table E1, E2 ; nœud « Revendication » |
| VV3-fidelite-01 : règle gelée citée avec un mot changé | accepté : « jamais « ne sépare pas » ; a fortiori jamais « pas de trace » » | règles communes ; table E1 |
| VV3-fidelite-02 : [AU] « en moyenne » | accepté (avec VV3-sens-03) | section 1 ; rang 3 |
| VV3-fidelite-03 : dilution | accepté : chiffres de la colonne « Dilution » de [PAR] ; maximum brut contre maxima appris | 2.2 ; rang 7 |
| VV3-fidelite-05 : Bonferroni | accepté : « règle de cette synthèse » | règles communes |
| VV3-fidelite-06 : Qwen3-4B | accepté : moyennes écrites à côté | table E2 |
| VV3-fidelite-07 : « v1 : 60 % » | accepté : « pour E1 et E2 ensemble » | confiance |

**Suite** : vérification neuve des sections 1, 3, 4 et 5 de la v4 (sens, et fidélité de chaque phrase et chiffre ajoutés
à sa page), par un sous-agent qui n'a écrit aucune version ni aucune vérification ; puis transmission à Lazar.
