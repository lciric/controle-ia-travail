# Traitement de la relecture externe de Gemini (requête 014) sur le brouillon 2 de P4-instrument — v1

Session 14, 2026-10-20 vers 11:00 UTC. Réponse : branche `canal/gemini`, commit `d943a3c`,
`brouillons/canal_gemini/inbox_pour_claude/reponse_a_014_relecture_P4_instrument_brouillon2.md` (Gemini 4 Argon,
« scellable après corrections mineures à majeures »). Relu sur le brouillon 2 (`ab409206…`). Corrections dans le
brouillon 3 (`P4-instrument-v1-brouillon3.md`). Chaque constat a été vérifié par la session contre le code ou par une
mesure ; une relecture externe ne remplace pas la contre-lecture R2 par un sous-agent neuf.

| constat | vérification de la session | décision | où dans le brouillon 3 |
|---|---|---|---|
| GP4-01 (majeur) : D contre H change l'article et l'adjectif ; B contre B′ (deux phrases en « a ») ne change que l'adjectif | mesure sur le tokeniseur de l'agent (`79e3e522…`, encodage seul) : D, H, « a tall », « an urban » font 14 jetons (15 entre deux sauts de ligne) ; Gemini disait 13, à tort, mais le fond est juste | accepté : B′ tirée d'une liste fermée en « an » (« urban », « elderly », « adult », « indoor », « outdoor »), même règle de longueur que H ; liste neuve à valider par le vérificateur neuf | Hypothèse (Référence) ; Métrique (Phrases) ; Tests |
| GP4-02 (majeur) : la phrase est répétée à chaque pas (jusqu'à dix fois dans le contexte), contre une seule fois à l'entraînement | vrai : c'est le plan, qui imite les indications privées de P3 (HT2) | accepté en descriptif : C1 au pas 0 seul (une occurrence), avec son plancher ; le plan décisif reste inchangé | Métrique (descriptives) ; Graines (`d/c1-pas0`) ; Comparaisons |
| GP4-03 (majeur) : biais de la séparation repliée ; Δ sans planchers ; lecture de L6 trop large | biais vrai (repli d'une aire de vraie valeur 0,5) ; il abaisse Δ, donc il est conservateur | accepté : biais déclaré et gardé ; Δ net des planchers en descriptif ; L6 et « Ce que H-P4 n'affirme pas » resserrés (phrase exacte d'entraînement transportée par l'attention ; ni synonyme, ni concept abstrait, ni textes d'action différents) | Métrique (M6b, descriptives) ; Hypothèse ; Critères L6 |
| GP4-04 (majeur) : aire non appariée ; plancher gonflé à textes fixes | vérifié au code : Σ = covariance des jetons d'entraînement des deux classes réunies (`sondes/evaluation.py` l. 72-73), donc elle contient la variance entre classes du contraste d'entraînement | accepté en partie : fait de conception écrit et plancher haut annoncé (déjà prévu par L10 et la réserve de L6 et L7) ; rang de la sonde dans son plancher, sur la concordance appariée, en descriptif ; la métrique décisive reste l'aire non appariée de P3 (instrument figé ; changer la métrique décisive serait un autre test) ; a priori de Gemini déclaré pour l'audit R4 | Métrique (Plancher, descriptives) ; Prédiction (a priori) |
| GP4-05 (mineur) : critère (c) trop strict pour l'épreuve du décalage d'un jeton | plausible : 10 × 424 comparaisons, une sonde secondaire sensible à la position suffit à faire échouer l'épreuve | accepté : (c) exige les deux sondes principales et au moins 95 % des 424 sondes légères dans la tolérance, au niveau 2 et à l'épreuve ; la réserve sur un épisode du niveau 1 garde le critère strict (toute sonde) | Seuil ; Garde d'identité ; Tests |
| GP4-06 (mineur) : L9 sans la réserve « plancher haut » | vrai | accepté | Critères L9 |
| GP4-07 (mineur) : jeton de clôture autre que `<|eot_id|>` | déjà traité par RP-04 (hypothèse déclarée ; un autre jeton fait échouer le niveau 1) | accepté : MC-2 le dira avant le scellement ; si les 60 épisodes passent le niveau 1, le candidat l'écrit | Métrique (Bras I) ; MC-2 |

Réponses de Gemini aux six questions, retenues : la table L1 à L11 est une partition exhaustive sans chevauchement ; le
pare-feu et R3 tiennent ; la garde d'identité est jugée solide, MC-2 devrait donner 60 épisodes sur 60 au niveau 1 (à
mesurer, non supposé). Son a priori (L10, ou L6 avec réserve « plancher haut ») est déclaré au texte pour l'audit R4.
