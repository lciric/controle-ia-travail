# Passation — rédacteur du texte de la base boîte noire (T0.8) et de ses pièces de course

- **Session** : `session_013QMayo5SNVbiUW6hGnPrCo`, fille de la session mère `session_013QMayjbmQUdDuDs2S3i3XD`. Modèle de la session : modèle B (Fable) jusqu'au 22 novembre au soir ; **Sonnet 5.5 depuis la reprise du 23 novembre**, ce qui compte pour les règles « qui conçoit » (pièces décisives) et « économie de Fable ». Suit les passations `2026-11-22-1857-…` et `2026-11-22-1944-…` (+ erratum 1), qui restent.
- **Mandat** : écrire le texte complet de la base boîte noire de T0.8 (à sceller au plus tard le 26 novembre, avant l'entretien du 1er décembre), puis ses pièces de course (ordre, consignes du lecteur et du juge de verdict) ; contre-lecture par un autre modèle. Mot de Lazar du 22 novembre : « je veux les résultats au plus vite » (économie d'usage levée pour T0.8).

## Fait (tout est sur `main` : la demande de fusion n° 61 est fusionnée)

- **Texte** : `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon15.md`, `8d68b7a01cbb534e0f4a0422bb7fa5a184d0c9455ec3c87dc343881345ee8d5f` — vérifié « conforme : scellable après les marqueurs » (`prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon15-verification-cl8-v1.md`, `fb23435a05ab97cc265f326efb9f0c6910541c69c6997db8d8ad3a8e6f3bb313`). Cinq marqueurs restent : `COMMIT_CODE_T08`, `ENTROPIE_T08`, `LIGNE_DEPENSE_T08`, `LIGNE_MOT_LAZAR_T5_19`, `VERIFICATION_CL8_T08`. Le brouillon 15 nomme la balise à cheval et la réponse finie sans balise (option (a), R-5045), sans écart au gel. **C'est lui qu'il faut sceller, pas le 14.**
- **Pièces de la course**, sous `docs/procedures/t08-course-v1/` : ordre de course au brouillon 9 (commandes en section 13 ; mot de Lazar `GO-2026-11-22-134` cité ; vérifié conforme, mineur r-9 traité côté chaîne), consigne du lecteur au brouillon 4, consigne du juge de verdict au brouillon 3 (tous vérifiés conformes), consigne de la chaîne de lancement v3 ; journaux des opérations à côté.
- **Programme de scellement** : version 3 (`brouillons/t08-texte-complet-fable-v1/finaliser-t08-scellement-v3.py`). La version 4, qui écrit aussi `prereg/T0.8-marqueurs-scellement-v1.json`, est écrite par le développeur de la chaîne (`session_013QMaykVEGYEXUpWBeemUjb`), branche `t08/scellement-v4` ; sa contre-lecture semble faite par une autre session (commit `eaea816b9`, « v5, mineures m-1 et m-2 de la contre-lecture de la v4 ») : **je ne l'ai ni faite ni lue**.

## Reste

1. **Scellement du texte**, dès les quatre valeurs de la session mère (commit du code aligné contre-lu avec sa chaîne, chemins de sa pièce d'empreintes et de son rapport de contre-lecture, ligne d'engagement, entropie) : jouer le programme de scellement de la version retenue par la mère (v4 ou v5), à blanc d'abord, `--entree` le brouillon 15, `--sha-entree` son empreinte, `--rapport-verification` le rapport `fb23435a…`, ligne des gardes R-5014. La mère scelle et inscrit ensuite `SCELLEMENT-T08`, puis `CODE-T08`.
2. **Contre-lecture courte de la version 4 du scellement** demandée par le développeur de la chaîne (message du 22 novembre, 21:50Z) : à confirmer auprès de la mère avant de la refaire.
3. Brouillon neuf de l'ordre seulement si une commande change ; les deux commandes de P7 (composées par moi) restent à confirmer par le contre-lecteur de la chaîne, sur le commit du code.

## Réserves

- Les faits relevés dans la garde de calcul, la lecture et le manifeste n'ont pas été relus par un contre-lecteur du code ; les essais du développeur de la chaîne les confirment ou non.
- Jamais joué avant la course : le mode réel sur une carte, le vrai loueur, la poussée vers le dépôt distant depuis un clone partiel.
- Point ouvert pour Lazar, non tranché : le mot « diffus » à la porte G1 contre la définition retenue par ce texte (section « Depuis le gel », point 5).
- La ligne R-5045 de la mère dit « DB8-8 (a) » pour le cas de la réponse finie sans balise ; c'est (b), l'option appliquée ; erratum demandé à la mère.
- Suite de tests complète non jouable dans ce conteneur (bibliothèques lourdes absentes) ; aucun fichier de `src/` ni de `tests/` touché par cette session.

## Prochaine action

Lire les messages de la session mère ; confirmer qui contre-lit la version du scellement ; attendre ses quatre valeurs ; sceller le brouillon 15.

## Branches et commits

`prep/t08-texte-complet-fable-v1` : entièrement fusionnée dans `main` (demande de fusion n° 61), tête `726862190` avant cette passation. Cette passation est sur `prep/t08-passation-redacteur-v2`, partie de `main` (aucune réécriture d'histoire). Autres branches citées : `t08/chaine-de-lancement-v1`, `t08/scellement-v4`, `prep/t08-code-aligne-v1`. Brouillon 15 : commit `e73109d64d992c6daba8a4ad66627b0a7d1d5538` ; ordre brouillon 9 : `7268621905a7b5074bbbcccea043163fee12f8c1`.

## Tâches planifiées actives

Aucune (la reprise programmée du 23 novembre à 08:00 UTC a été supprimée). Aucune instance de calcul, aucune dépense.

## Ce qui n'était pas encore sur GitHub

Rien d'utile : tout le travail est sur la branche, désormais dans `main`. Le bloc-notes de la session ne contient que des copies de fichiers suivis, un environnement de tests léger et des sorties d'essais jetables ; non versés.
