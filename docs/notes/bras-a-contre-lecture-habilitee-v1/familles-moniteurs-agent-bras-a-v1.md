# Familles des modèles des six moniteurs, de l'agent et de l'élève distillé — bras A des organismes discrets — v1

- **Objet** : la case « familles » du brouillon 2 du préenregistrement neuf du bras A (`prereg/T0.7-organismes-discrets-v-a-v2-brouillon2.md`, empreinte `8db1899ace90ee5196a58d792b6f744a95a8cbf3a86c9551d5bff161293fc38c`, section 13, ligne 739 ; usage : section 3.4, ligne 252, et garde « familles des lecteurs », ligne 633). Pièce empreintée pour choisir les deux lecteurs de l'appariement et de la couverture.
- **Auteur** : contre-lecteur neuf et habilité, sous-agent délégué par la session mère (session `session_013QMayjsoZJFBUCqcnvD5h1`) ; Claude Opus 5.5 (`claude-opus-5-5`). Écrit le 2026-11-19 à partir de 06:51 UTC (`date -u`). Rapport compagnon : `docs/notes/bras-a-contre-lecture-habilitee-v1/contre-lecture-habilitee-b7-brouillon2-v1.md`.
- **Règle** : nom de famille seulement ; aucune version, aucun poids, aucun seuil. Chaque famille est établie par une pièce empreintée (empreintes complètes en fin de fichier) ; une famille qu'aucune pièce n'établirait serait écrite « non établie ».
- **Liste gelée des six moniteurs** : texte archivé sans exécution, `prereg/T0.7-organismes-discrets-v-a-v1.md`, lignes 138 à 149, qui ne nomme aucun modèle (règle d'anonymisation, ligne 16).

| rôle, décrit par sa fonction | famille du modèle | source (chemin, empreinte, ligne) |
|---|---|---|
| base décisive « mots et coût » : la plus forte de deux prédicteurs linéaires, l'un sur des traits tirés des champs de l'action, l'autre sur un sac de mots, le coût déclaré et la forme du champ du coût (moniteur 1) | aucune : sans modèle de langue | texte archivé (`06ab6a2f…`), ligne 142 ; `prereg/T0.8-base-A-mots-et-cout-v1.md` (`72b067d5…`), ligne 40 ; `prereg/T0.6-organismes-v0-v1.md` (`ef31feff…`), ligne 575 |
| classifieur lexical : régression logistique régularisée sur le seul sac de mots (moniteur 2) | aucune : sans modèle de langue | texte archivé (`06ab6a2f…`), ligne 143 |
| moniteur boîte noire par action, qui lit l'action en contexte (moniteur 3) | Llama | `registres/decisions.md`, ligne 376 (D1, « moniteur boîte noire », défaut appliqué : même modèle que l'agent, et un modèle plus faible de la même famille) ; `docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md` (`2dec994f…`), ligne 3 (D1 : juges de la taille de l'agent et plus petit) ; `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1ba…`), lignes 17 à 19 (l'agent) ; `docs/decisions/decision-N-029-v1.md` (`084e3052…`), lignes 20 à 22 (juge par action « modèle selon la décision D1 ») ; borne : `docs/decisions/decision-N-060-v3.md` (`2b448f69…`), lignes 24 et 25 |
| agrégateur séquentiel : statistique par épisode des scores du moniteur boîte noire (moniteur 4) | aucune en propre ; il agrège les scores du moniteur 3 : Llama par ce moniteur | texte archivé (`06ab6a2f…`), ligne 145 ; `docs/decisions/decision-N-029-v1.md` (`084e3052…`), lignes 37 et 38 |
| classifieur de surface : forme de l'action seule, sans mot ni valeur de coût (moniteur 5) | aucune : sans modèle de langue | texte archivé (`06ab6a2f…`), ligne 146 |
| juge d'une autre lignée, qui lit l'action en contexte sur un sous-échantillon déclaré d'avance (moniteur 6) | Qwen | `docs/decisions/decision-N-053-v1.md` (`2204256d…`), ligne 34 ; texte archivé (`06ab6a2f…`), ligne 147 (renvoi à N-053, point 4) ; `docs/decisions/decision-N-060-v3.md` (`2b448f69…`), ligne 25 |
| agent : le modèle du programme qui écrit les plans de recherche (honnête et rejeu) | Llama | `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1ba…`), lignes 17 et 18 ; texte archivé (`06ab6a2f…`), ligne 17 (clé `agent` de cette configuration) |
| élève distillé : le modèle de l'agent muni d'un adaptateur de rang faible appris sur les transcriptions | Llama (celle de l'agent) | `prereg/T0.6-organismes-config-7b-v1.json` (`b7a5c1ba…`), lignes 5 à 18 ; texte archivé (`06ab6a2f…`), ligne 39 ; brouillon 2 (`8db1899a…`), lignes 52 et 127 |

**Notes.**
- Moniteur boîte noire par action : sa famille est établie par la décision D1 (registre des décisions, ligne 376), dont les deux options sont de la famille Llama, et recoupée par P-010 et la configuration de l'agent. Le registre des décisions est un registre vivant sans compagnon : son empreinte ci-dessous est celle du fichier au moment de la lecture ; la pièce est la ligne 376. Le modèle exact retenu pour le bras A n'est inscrit dans aucune pièce scellée du bras (texte archivé, ligne 16 ; devis v2 du bras A, ligne 109) : cela ne change pas la famille.
- La décision N-060 version 3 (lignes 24 et 25 : « ni Llama ni Qwen ») nomme les mêmes deux familles ; la version 4 la reprend inchangée sur ce point (`docs/decisions/decision-N-060-v4.md`, ligne 23).
- Aucune autre exclusion n'est établie par les pièces lues. En particulier, aucune pièce lue n'exclut la famille des agents qui rédigent ou contre-lisent les textes du programme ; si on la veut exclue, c'est à décider ailleurs.

**Empreintes complètes des sources.**
- `prereg/T0.7-organismes-discrets-v-a-v1.md` : `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05`
- `prereg/T0.8-base-A-mots-et-cout-v1.md` : `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d`
- `prereg/T0.6-organismes-v0-v1.md` : `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169`
- `prereg/T0.6-organismes-config-7b-v1.json` : `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`
- `docs/decisions/decision-N-053-v1.md` : `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae`
- `docs/decisions/decision-N-029-v1.md` : `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4`
- `docs/decisions/decision-N-060-v3.md` : `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591`
- `docs/decisions/decision-N-060-v4.md` : `e14779987cf61ae65f4690a0bbb94f373bd0e48f8cdeabb0bd2b31b99b1af241`
- `docs/decisions/proposition-P-010-T0.8-moniteur-par-action-v1.md` : `2dec994f347e8a157cfd45aefb48db41466313e27958f6dbe3d9e325537fff63`
- `registres/decisions.md` (registre vivant, au moment de la lecture) : `fa9b926dfb8e024bce7b2a50aaa98a77d7133cb7c804c9f8d460cf21905e55ba`
- `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md` (objet `2e29b6403` de la branche `claude/pensive-bardeen-1fv7hw`) : `83240ca61d7c300fc9f4ca802560a6010a2a7c2eb48dd58fe2c214ee03524ecd`
- brouillon 2 (même objet) : `8db1899ace90ee5196a58d792b6f744a95a8cbf3a86c9551d5bff161293fc38c`

familles exclues pour les deux lecteurs : Llama, Qwen.
