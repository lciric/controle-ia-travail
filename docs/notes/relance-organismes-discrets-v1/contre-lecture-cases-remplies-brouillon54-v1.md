# Contre-lecture courte (R2) des cases remplies du brouillon 54 — organismes discrets, bras A

Objet : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon54.md` (`59ad88f93d84f7cf3acbf11cdf8eecfe61469e7e75e3618dc69c8f2265de45dd`) contre le brouillon 53.

**Verdict : conforme.** Aucun défaut.

## Différences
`diff` : seules les lignes 1, 3, 1469 et 1472 changent.

## Ligne 1469 (case « nœuds »)
- R-4186 (registre des décisions de la branche principale `main`, la branche courante n'ayant pas ces lignes) : 2026-11-20T10:17:53Z, pièce `2845ca37…`, mots rapportés sans recopie : conforme.
- R-4048 : consigne de Lazar, aucune ligne neuve ne nomme l'accord visé avant le tirage de la table : conforme à « aucune ligne de GO ne les porte, et c'est voulu ».
- R-3785 : 11:55:34Z ; passation `2026-11-19-1230.md` point 4 : six fiches du bras A (présente sur `main`) ; commit `aa9c616fa` : 2026-11-19T12:27:08Z ; GO-2026-11-19-52 et R-3802 : mot de Lazar 12:38:35Z, fiches 1 (a), 2 (b), 3 (a), 4 (b), 5 (b), 6 (b) : conforme.
- Remarque sans correction : R-4186 dit « mots rapportés, non relus à la source » ; l'inscription ne le répète pas et renvoie au registre.

## Ligne 1472 (case « lecteurs et juge des ancres »)
- Mistral : 24 corps, tous identiques : `model` = `mistral-large-4-0`, `messages`, `max_tokens` = 32768, `reasoning_effort` = `high`, `stream` = vrai ; pas de température ; hôte `api.eu.mistral.ai` ; chemin `/v1/chat/completions` : conforme.
- Gemini : 8 corps identiques : `contents`, `generationConfig` = {`maxOutputTokens` 65536, `thinkingConfig` {`thinkingLevel` `XHIGH`}} ; hôte `generativelanguage.googleapis.com` ; chemin `/v1beta/models/gemini-4-neon:generateContent` : conforme.
- Programme : la fonction du chemin occupe les lignes 2068 à 2073 ; ses deux retours sont aux lignes 2071 et 2072 : conforme.
- Réserve non bloquante : « GO-2026-11-21-86 » n'est pas dans le registre de la branche courante, il est sur `main` (ligne de vérification de la clé de Mistral, température retirée d'avance) : conforme à l'inscription.

## Validateur
`prereg.problemes` rend un seul marqueur « À REMPLIR restant hors des sections exigées » : lignes 1475 (entier racine) et 1482 (module des cinq moniteurs), les deux cases déclarées ouvertes.

Aucune réponse brute ouverte ; aucun contenu de message lu.
