# Choix de Lazar — les deux lecteurs du texte neuf du bras A

- **Contexte** : case « lecteurs » de la section 13 du texte neuf (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon3.md`, `72e34bdeea768ff70d7429c9a46ec91d09c0bb41e4307388a6893b21499f7e3c`) ; après le choix d'un agent neuf pour les ancres (`choix-de-lazar-juge-des-ancres-v1.md`, `139af8a159f01f829b14f0bb10a330f4edfb03dfec98d62d4899d3d8bd97c735`), la relance a dit à Lazar que les deux lecteurs se choisiraient hors de la famille Claude, « par exemple OpenAI et Google ».
- **Mot de Lazar**, direct, dans la session de relance : événement `2b85afbf-0f46-4fe0-a21f-e44db2d52625`, 2026-11-19T07:34:04Z (heure relevée sur l'événement), verbatim « on peut utulise gpt6.2 et carbon ».
- **Transcription** : session de relance, 2026-11-19T07:34:54Z.

## Lecture de la relance, déclarée (dite à Lazar, qui peut la corriger)

1. Le mot désigne **les deux lecteurs** de l'instrument (appariement et couverture), non les juges des ancres.
2. « gpt6.2 » : le modèle de la famille OpenAI que le programme a déjà joué sous l'identifiant `gpt-6.2-astra` (lanceur `scripts/lancer_bras_juge_ideation_organismes_discrets_v5.py`, `ea4c0c92…`, ligne 103). « carbon » : le modèle de la famille Google de la lignée Carbon de l'organisme d'idéation, `gemini-4-carbon` (lanceur `scripts/lancer_bras_juge_ideation_organismes_discrets_v4.py`, `343539af…`, ligne 93).
3. Les deux familles sont distinctes, et hors de la liste des familles exclues (Llama, Qwen : `docs/notes/bras-a-contre-lecture-habilitee-v1/familles-moniteurs-agent-bras-a-v1.md`, `1753a9d94f8a2c4004a16ef9cdb0c362936ebab439b6f84404ee40916bff6a06`) ; l'agent neuf des ancres est alors de la famille Claude, troisième famille.

## Ce que le mot ne fixe pas (reste à la case « lecteurs », avant scellement)

Identifiants de version exacts tels que servis par chaque fournisseur ; réglages (température 0, longueur de sortie maximale, budget de pensée) ; découpage des messages ; tarifs relevés et datés ; devis des lectures et ligne de GO. Aucun appel avant le scellement du texte et de la configuration.

## Réserve dite à Lazar

Dans le bras du juge externe de l'organisme d'idéation, `gpt-6.2-astra` a rendu un classement illisible (deux témoins non tenus ; `runs/bras-juge-ideation-organismes-discrets-v5/`). La tâche était autre (classer des fiches d'idées) ; ici le texte éprouve chaque lecteur avant toute lecture décisive, et un lecteur qui échoue arrête le bras avant la distillation.
