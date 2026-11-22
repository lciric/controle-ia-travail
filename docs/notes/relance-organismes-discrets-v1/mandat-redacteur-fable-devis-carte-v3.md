# Mandat du rédacteur Fable — devis de la course sur carte louée du bras A, version 3, sur le texte v2

Écrit le 2026-11-22 par la session de relance du bras A, sur la demande de la session mère (mot de Lazar « go scelle et lance », GO-2026-11-22-140 : aller vite, mais tout départ dans le cadre d'un devis scellé). Rédacteur : Claude Fable 5.2, session neuve, effort maximal (pièce décisive : devis, règle « Économie de Fable »). Langue : français ; nomme les choses par ce qu'elles sont.

## Ce que tu fais
Le devis de la carte en vigueur, `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v2.md` (`83240ca61d7c300f…`, 18 novembre, « version finale, non recontre-lue », fait sur le texte v1 et ses addenda), chiffre deux lignes de carte (ligne 1 : fabrication et rejeu honnête, 256 épisodes, plafond 27 USD, accordée par GO-2026-11-18-62 ; ligne 2 : la suite, plafond 75 USD sans mesure, 42 à 45 avec). Écris la **version 3** sur le **texte v2** du bras A : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md` (`cc55502ad4ef0fa1de5f8f4444975fec2eb7f3f77db8913c96f1bdf9225facb1`), dont le texte scellé ne différera que par l'entier racine, le titre et le statut. Lis 6.1 à 6.11 (6.11 : « Dépense à chiffrer »), 6.3 (ordre, dont l'arrêt d'office A18 à l'étape (i)), la liste d'arrêt 8.1 à 8.4, et 13.2.
1. Pour chaque ligne de carte : ce que le texte v2 lui fait jouer (épisodes, doses, adaptateurs, conditions), la durée et le prix, l'attendu, le pire cas, le plafond, sur les mêmes règles que la v2 (prix relevé ou borne de la configuration de référence ; les relevés de prix sont dans le devis v2 et `registres/depenses.md`, lignes qu'il cite).
2. Dis ce qui change de la v2 à la v3 et pourquoi ; si la ligne 1 est inchangée sur le fond, dis-le en une phrase : c'est elle qui peut partir la première.
3. Dis ce que l'arrêt d'office sous 80 actions relues (A18, étape (i)) épargne de la ligne 2.
4. Liste les conditions de 13.2 qui doivent être tenues avant chaque ligne (lanceur neuf citant l'empreinte du texte scellé, tarifs du jour, configuration scellée, etc.) ; ne les remplis pas.
5. Décisions pour Lazar, au format : décision en une phrase ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance ; défaut (aucun pour une dépense).

## Interdits
- Les lectures hors carte ne sont pas ton objet (devis à part, `devis-lectures-hors-carte-bras-a-v1-brouillon3.md`) : cite-les seulement pour le total.
- Aucun chiffre sans source (chemin, ligne ou empreinte) ; marque « M » (mesuré), « C » (calculé), « S » (supposé).
- Cloisonnement : n'ouvre, ne liste, ne cherche ni n'empreinte `bases/`, `sondes/`, tout chemin dont un élément commence par `t07`, rien de T0.8, `scripts/mots_et_cout_*`, `prereg/T0.6-organismes-v0-v1.md`, `docs/notes/bras-a-moniteurs-v1/`, `docs/notes/bras-a-contre-lecture-habilitee-v1/`, `docs/notes/bras-a-sans-interne-v1/`, `src/controle_ia/organismes_discrets/bras_a_v2_habilite*/`, `autres_moniteurs_v*`, `runs/`, `docs/sources/`, fichiers « consigne-privee » ou « conception-ii-b », `archives-reponses-modeles/` ; dans `registres/`, seulement `registres/depenses.md` aux lignes que le devis v2 cite. Le texte cite des chemins cloisonnés : tu ne les suis pas.
- Aucun réseau, aucune clé, aucune dépense.

## Rendu
Sur une branche à toi, `relance-bras-a/devis-carte-v3`, un seul fichier scellé (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller FICHIER`) : `docs/notes/relance-organismes-discrets-v1/devis-bras-a-v3.md`. Pousse ta branche, ne touche à rien d'autre. Un contre-lecteur neuf (Opus 5.5) le relira.
