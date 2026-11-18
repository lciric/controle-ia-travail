# Différences entre le brouillon 3 et le texte candidat de la version 1 du préenregistrement de l'étude par simulation des formulations du contraste à témoin apparié de la porte de fin de phase 1 (G1) — v1

- Écrit par le rédacteur des brouillons 2 et 3 (Claude Fable 5.2, `claude-fable-5-2`), le 18 novembre 2026 vers 22:55 UTC.
- Brouillon 3 : `prereg/formulation-g1-simulation-v1-brouillon3.md` — `d20d605cc3661e0e12d93c13c99476594033069c59aae19aee0afbed6b59ebb5` (inchangé).
- Vérification 1 : `prereg/contre-lectures/formulation-g1-simulation-v1-brouillon3-verif1.md` — `958707bd6d7641447cde37aad914a2b2e9491492c61a3104b1fc25f9005991ce` ; verdict « scellable après ces couples exacts », quatre couples de texte (C1 à C4), aucun de code.
- **Texte candidat** : `prereg/formulation-g1-simulation-v1.md` — empreinte au rendu : `d04da7903b89d0835ce16a77d5338e5a11ada20908f7c13dd65fd61191a08a87`. **Non scellé par le rédacteur** : la session mère le scelle par `controle_ia.prereg.sceller_prereg` ; aucun compagnon `.sha256` n'a été écrit.
- Écrit **par programme** depuis le brouillon 3 : `prereg/pieces-formulation-g1-v1/candidat-depuis-brouillon3-v1.py` (scellé), lancé par `.venv/bin/python -B prereg/pieces-formulation-g1-v1/candidat-depuis-brouillon3-v1.py . 7f73ec743` (`7f73ec743` : tête du dépôt à l'écriture, inscrite à l'en-tête). 23 remplacements exacts ; le programme s'arrête si un « avant » n'apparaît pas exactement une fois dans le brouillon 3. Le rejouer redonne le même texte, à l'octet près.
- `diff` du brouillon 3 au candidat : 20 lignes retirées, 36 ajoutées. `prereg.problemes` sur le candidat : aucune remarque (liste vide).
- **Code : inchangé.** C'est la v3, déjà scellée (empreintes à l'en-tête du candidat, égales à celles du brouillon 3). Aucun essai n'a été rejoué pour ce texte : rien de ce qu'ils couvrent ne change ; le vérificateur a rejoué les 105 essais de la v3. Aucune simulation n'a tourné, aucune issue n'a été lue.

## 1. Couples de la vérification 1, appliqués tels quels

| couple | endroit | appliqué |
|---|---|---|
| **C1** | « Choix de fond remis à Lazar », ligne « Décision » | tel quel |
| **C2** | « Points portés à Lazar », point 8, fin de phrase | tel quel |
| **C3**, premier passage | « Budgets d'épisodes du témoin, dits » : « Deux contrôles réduisent l'écart de budget, sans l'annuler … » | tel quel (deux remplacements : le début de la phrase, puis sa fin) |
| **C3**, second passage | « Ce que la règle peut encore devoir à sa construction » : « Le sixième rejeu éprouve cette pente … sans l'annuler … » | tel quel |
| **C4**, « Ordre » | lecture des variantes rapportées par `lecture_v3.indicateurs`, que `verdict` ne tabule pas | tel quel |
| **C4**, « Contre-lecture » | entrée « Vérification 1 du brouillon 3 », avec l'empreinte du brouillon relu ; le paragraphe « À venir » remplacé par la mention que la vérification est faite | tel quel ; **en plus**, l'empreinte entière du rapport est écrite entre parenthèses après « empreinte au compagnon `.sha256` », et un tableau de traitement suit l'entrée |

## 2. Points « hors couple » du rapport (§ 9 et remarques des § 4 et § 5), texte seul

| point | changement |
|---|---|
| « B à 300 » contre « B sur 300 » | règle 6 : « B sur 300 épisodes du témoin », comme le reste du texte et le code |
| δ à 50 tâches ; paliers établis pour des unités de dix épisodes | réserve ajoutée à l'hypothèse de travail (2), sous la garde de D-S4 ; sans effet sur la règle (400 et 600 tâches) |
| bornes « ≥ 19 » de l'essai de la garde appariée | dit à la déclaration 2 : marges écrites avant de jouer l'essai, jamais retouchées |
| la composante B sans la garde n'est pas conservée | **écrit en limite** à « Ce que l'étude ne dit pas » ; le code n'est pas changé |
| fourchette de P8 | rien à changer |

## 3. Mise au statut de version

| endroit | changement |
|---|---|
| titre | « (v1, brouillon 3) » → « (v1) » |
| paragraphe de statut | « version 1, texte candidat au scellement » ; la session mère scelle |
| en-tête | auteur ; date ; le brouillon 3 et la liste des différences 2 → 3 entrent avec leurs empreintes, la présente liste avec son chemin ; ligne « Commit du code d'analyse » (code de la v3 versé par la session mère, tête `7f73ec743` ; commit du lancement au manifeste du run) ; essais : « rejoués par le vérificateur » |
| « Ordre » | la relecture par un lecteur neuf est dite faite ; « ce texte scellé par la session mère » |
| liste d'arrêt | « sceller le texte final » → « sceller ce texte » ; « l'en-tête du texte final » → « l'en-tête de ce texte » |
| déclaration 5 | les ajouts du brouillon 3 sont dits relus par la vérification 1 |

## 4. Ce qui n'est pas fait

- Le texte candidat n'est pas scellé (mandat).
- Le texte de `__init__.py` nomme toujours les modules de la v1 (dit à l'en-tête).
- La ligne « Commit du code d'analyse » ne porte pas le commit du lancement, qui n'existe pas encore : il s'inscrit au manifeste du run.
