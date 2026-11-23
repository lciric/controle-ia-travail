# Passation — avis de Carbon et Neon sur les décisions de G1 (2026-11-23 06:24Z)

Session fille session_013QMaymuTq2guSdeqPHCBWV (Opus 5.5) ; mère session_013QMayjbmQUdDuDs2S3i3XD.

## Mandat
Avis de Carbon et de Neon sur l'énoncé du critère et les fiches 1 à 7 de G1 (pièce 3b95d11a…), puis sur le complément (fiche 2 v2, fiche 8, question du moindre coût ; a2a1a537…). GO-2026-11-22-130, plafond réel 3 USD ; relance accordée par la mère (R-5052), plafond compté au pire cas porté à 5 USD, arrêt si le réel atteint 3 USD.

## Fait
- Appels par docs/notes/memoire-conception-v1/appel-google-garde-v3-v6/appel_google_garde_v3_v6.py (9a8b01c2…), comme la consultation sabotage-selectif-avis-v1 : Carbon = gemini-4-carbon, Neon = gemini-4-neon (Google), clé GEMINI_API_KEY ; OPENAI_API_KEY_2 non employée.
- Premier envoi refusé par la garde de motifs (nom du directeur, deux fois) ; « mot de Lazar » → « mot du directeur », seule différence ; rien n'était parti (consoles versées dans appels/essai-bloque-garde-motifs/).
- Dossier : deux réponses valides. Complément : premier appel de Neon coupé (503 « high demand » de Google, défaut ERREUR_FLUX, texte partiel gardé en .defaut.md) ; Carbon refusé par le plafond ; relance : deux réponses valides.
- Coût réel (tarif × jetons) : Carbon dossier 0,265 ; Neon dossier 0,363 ; Neon complément en panne 0,490 (estimé) ; Neon complément relancé 0,435 ; Carbon complément 0,150 ; total 1,703 USD.
- Synthèse envoyée à la mère (tableau énoncé + fiches 1 à 8).

## Reste
Rien pour cette session. Inscription du coût au registre des dépenses : par la mère.

## Réserves
- Fiche 2 : au premier tour, les deux modèles ont répondu à l'ancienne version ; la v2 a ses réponses dans le complément.
- Compagnons .sha256 des deux journaux de course scellés trop tôt (avant la relance) ; non réécrits ; empreintes finales dans docs/notes/g1-avis-carbon-neon-v1/appels/erratum-1-empreintes-journaux-v1.md.
- Le mandat disait Neon « modèle OpenAI, clé OPENAI_API_KEY_2 » ; suivi le modèle de la consultation précédente (Google) ; signalé à la mère.

## Prochaine action
Aucune ; session close sur ce mandat.

## Branches et commits
avis/g1-carbon-neon-v1, dernier commit avant cette passation 15fd34f6. Dossier : docs/notes/g1-avis-carbon-neon-v1/.

## Instances et tâches planifiées actives
Aucune instance de calcul ; aucune tâche planifiée ; aucun processus en fond.

## Versement
Tout est sur la branche. Bloc-notes : une seule copie (comp.md) du complément de main, identique à l'octet (a2a1a537…), non versée car déjà sur main.
