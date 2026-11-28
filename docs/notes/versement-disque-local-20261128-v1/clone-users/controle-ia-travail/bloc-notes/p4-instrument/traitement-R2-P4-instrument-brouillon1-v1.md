# Traitement de la contre-lecture R2 du brouillon 1 de P4-instrument, et décisions sur les questions du plan — v1

Session 14, 2026-10-20 vers 10:45 UTC. Brouillon relu : brouillon 1 (`41e5f035…`). Rapport R2 (`108a8d1f…`) : « scellable
après corrections », six majeurs, cinq mineurs. Corrections écrites dans le brouillon 2 (`P4-instrument-v1-brouillon2.md`).
Le brouillon 1 reste tel quel (R12). La session n'a calculé aucune grandeur de P4 ni de P3 ; aucune activation, aucun
score.

## Constats

| constat | décision | où dans le brouillon 2 |
|---|---|---|
| RP-01 (majeur) : la ligne « plancher haut » prime sur un succès | accepté : le plancher haut qualifie le seul cas « non au-dessus » (L10, placée après les lignes de succès) ; C1 au-dessus d'un plancher haut se lit par L6 ou L7, avec la réserve « plancher haut : le contraste est vu par des directions quelconques ; la sonde les dépasse » | Seuil (« Plancher haut ») ; Critères L6, L7, L10 ; Réserves |
| RP-02 (majeur) : « aveugle » pour une aire inversée | accepté : « au-dessous » défini (borne haute < 1 − quantile 0,95, plancher symétrique, `evaluation.py` l. 79) ; ligne L9 « contraste vu, de signe inversé : instrument non aveugle, mal orienté » ; L11 « non détecté à cette puissance », « aveugle » seulement qualifié | Seuil ; Prédiction (P4-C1) ; Critères L9, L11 |
| RP-03 (majeur) : la référence B contre H retire « honest » | accepté, correction recommandée : bras B′ (première phrase de la même liste après B, longueur de H) ; M6a = séparation de B contre B′ ; M6b = aire(D contre H) − séparation(B contre B′) ; B contre H en descriptif ; L7 « spécificité non établie » au lieu de « consigne changée » ; volume 300 passes (+ ≈ 3 minutes de carte) | Hypothèse (« Référence ») ; Métrique (Bras, Phrases, M6a, M6b, descriptives) ; Plan 1 ; Garde d'identité (alignement) ; Graines |
| RP-04 (majeur) : jeton de fin déduit de la longueur | accepté : présence du jeton de fin lue par `jetons − jetons_notes` de P3 ; critère (a) et MC-3 : longueur retokenisée = `jetons_notes`, sans tolérance ; hypothèse « jeton de fin = `<|eot_id|>` » déclarée, avec ce qu'un autre jeton entraîne ; colonnes ajoutées à la table des données lues ; artefact testé | Données lues ; MC-3 ; Métrique (Bras I) ; Seuil ; Garde d'identité ; Tests |
| RP-05 (majeur) : puissance sur des hypothèses réfutées par le verdict de P3 | accepté : deux scénarios ; les valeurs réalisées de P3 font référence (erreur type ≈ 0,0194 ; aire minimale détectable ≈ 0,63 à 0,65 pour des planchers de 0,57 à 0,60, ≈ 0,85 pour 0,80) ; recalcul vérifié par la session (2,80 × 0,0194 ≈ 0,054) | Prédiction (P4-C1) ; Plan 5 ; Nombres de P3 déjà connus |
| RP-06 (majeur) : autorité de dépense liée au mandat | accepté, et dépassé par un fait neuf : R-269 (GO-2026-10-20-07) étend la délégation jusqu'au 2026-11-30, indépendamment du mandat, 10 USD au plus par lancement ; GO-2026-10-20-06 prolonge GO-2026-10-04-08 au 2026-11-30 ; la ligne d'accord cite GO-2026-10-20-07 ou un message de Lazar du jour ; le lanceur refuse un GO échu ou une borne au-dessus de 10 USD | En-tête (« GO et dépense ») ; Plan 7 ; Liste d'arrêt |
| RP-07 (mineur) : ordre et cohérence de la table | accepté : tout arrêt écrit un résumé avec son motif (L2 lisible) ; L3 « rapportés s'ils sont calculés » ; « M6 en échec » sorti de la ligne de spécificité (L8 « référence non lue ») | Plan 1.6 ; Critères L1 à L3, L8 |
| RP-08 (mineur) : nul trop propre ; tolérance (c) non éprouvée sur le modèle réel | accepté : part des actions à score égal sous D et sous H, toujours rapportée, déclencheur R4 si > 0 ; épreuve de la tolérance (c) sur l'instance (contexte décalé d'un jeton : doit passer ; action échangée : doit échouer) ; en cas d'échec de l'épreuve, niveau 2 désactivé (épisode exclu entier) et réserve | Seuil (audit R4) ; Métrique (descriptives) ; Garde d'identité ; Audit de symétrie ; Réserves |
| RP-09 (mineur) : empreintes de registres périmées ; sources secondaires | accepté : registres cités à la version relue au brouillon 2, à relire au candidat ; nombres de P3 cités à `lecture-p3.json` (`c221d955…`) | Documents qui font foi ; Nombres de P3 déjà connus |
| RP-10 (mineur) : formes lisibles par le module ; chemin du verdict complété | accepté : `Révision du modèle : `0e9e39f…`` ; « Configuration de P4 (empreinte canonique) : `…` » ; une ligne « Module de P4 : `chemin` : `empreinte` » par fichier, garde `exiger_module_cite` ; verdict complété exigé à `docs/verdicts/verdict-P3-premier-test-i-a-v2.md`, scellé, annoncé au registre | En-tête ; Plan 2 ; Tests |
| RP-11 (mineur) : formulations | accepté : « fait rapporté ; T0.7 peut le citer ; aucun choix de T0.7 n'en découle sans son propre préenregistrement » ; « nœud de Lazar (branche (C) de la note) » ; l'ordre vient de R-262, pas de P4 ; « reconstruites, garde d'identité à deux niveaux » ; deux écarts à l'entraînement déclarés en HT1 | Hypothèse ; HT1 ; Pare-feu ; Critères ; Réserves |

## Questions ouvertes du plan (`plan-code-et-chaine-v1.md`, section 7) : décisions de la session (routine)

| question | décision |
|---|---|
| 1. Entropie | gardée ; consignée par R-268. |
| 2. Emplacement du code | `docs/procedures/P4-instrument-v1/`, hors de l'arbre gelé (P3 reste ouvert : addendum 2, P3b). |
| 3. Tolérances de la garde | gardées (5·10⁻², 10 %, 0,005) ; MC-2 et MC-3 les éprouvent avant le scellement ; la tolérance (c) est en plus éprouvée sur le modèle réel (RP-08). |
| 4. Variante « autre agent » | exclue (liste fermée de l'option A1). |
| 5. Phrases B | liste validée par le contre-lecteur R2, neuf (RP-03) ; B′ tirée de la même liste. |
| 6. Ordre des lancements | P4 d'abord, seul ; pas d'instance commune avec P3b (textes, instances et lectures séparés ; le gain de ≈ 0,6 USD ne vaut pas le couplage). |
| 7. Délégation | résolue par R-269 (GO-2026-10-20-07). |
| 8. Effet d'un échec sur P3b et T0.7 | un échec est un nœud de Lazar (branche (C)) ; l'ordre vient de R-262 et de la règle du témoin positif ; ce que devient P3b est sa décision. |
| 9. Instance de P4 | détruite après la récupération vérifiée. |
| 10. Lecture conditionnée au verdict complété | garde dans le code (chemin, sceau, ligne du registre). |
| 11. Mesures de conception sur les textes honnêtes | acceptées au titre de R1 (propriétés des entrées, aucun score ; le contre-lecteur R2 est d'accord). |
| 12. Filtre d'offre | gardé égal à celui de P3 (chaîne éprouvée). |
| Économie (plan, 5.2) : sans la suite complète des tests sur l'instance | non : la suite complète tourne sur l'instance, comme pour P3 (≈ 0,55 USD). |
