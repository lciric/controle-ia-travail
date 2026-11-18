# Mandat du préparateur de la commande de lecture — apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Tu es un sous-agent neuf. Lis d'abord `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md` : il te lie.

## Ta tâche
Écrire, sans rien exécuter sur les sorties de la course, la **commande exacte** que le lecteur-opérateur jouera, dans un seul fichier : `registres/t07-etape-b-bis/lecture-v1/commande-lecture-bbis-v1.md`, scellé par son compagnon. Tu ne lis **aucun** fichier de résultat (ni `diag/`, ni `donnees/`, ni `runs/` d'aucun run réel) : tu travailles d'après les textes scellés, le feu, les registres propres et le code.

## À lire
- `prereg/T0.7-etape-B-bis-v1.md` : « Plan d'analyse » (points 1, 2, 10, 11, 12), « Critères de lecture gelés », « Liste d'arrêt », « Données gardées », « Lignes de registre » ; les trois addenda, en entier pour ce qui touche la lecture, le registre, les branches, le module de lecture en vigueur, les réserves.
- `registres/t07-etape-b-bis/feu-bbis-v7.txt`, § 12 et § 13.
- `registres/t07-etape-b-bis-v1.md`, `registres/t07-etape-b-bis-v1-addenda-v1.md`, `registres/t07-etape-b-bis/code-bbis-v2.json`, `registres/t07-etape-b-bis/ABSENCE-B-BBIS-v1.json`.
- Le code : `src/controle_ia/t07bbis/` (lecture, registre, communs), ses essais `tests/test_t07bbis_*`, et les scripts qu'il cite. `registres/scellements-v1.md` : seulement les lignes des clés que le texte nomme « lues, jamais écrites » (recherche bornée à ces clés).

## Ce que la commande doit contenir, dans cet ordre
0. **Module de lecture en vigueur.** Le mandat de la session nomme `lecture_v2.py` ; la fiche de code inscrite porte aussi `lecture_v3.py`. Dis lequel est en vigueur d'après le texte, les addenda et la fiche, avec la ligne qui le fonde ; vérifie que les empreintes des fichiers de code du dépôt égalent celles de la fiche (commande donnée). Si le texte ne permet pas de trancher : écris-le comme point ouvert, ne choisis pas.
1. **Mise en place des fichiers** : comment le lecteur-opérateur obtient, sans les ouvrir à l'œil, les sorties de la course (branche `donnees/t07-etape-b-bis-v2`, tête dite) et les entrées de 7b et autres que le plan, point 1, nomme (sur quelles branches, relevé par les noms) ; vérification de la tête et des empreintes contre les compagnons et les lignes de registre.
2. **Preuve d'antériorité**, rejouée depuis un clone à histoire complète (le dépôt est récupéré en entier par la conductrice ; un clone local `git clone --no-hardlinks` dans le dossier temporaire convient si tu le juges conforme) : ce que le plan, point 2, et les addenda demandent (ordre des lignes du registre propre et de leurs commits ; premier commit qui ajoute `lecture-t07.json`, s'il existe, postérieur au commit qui ajoute `SCELLEMENT-BBIS` ; ce que les addenda ajoutent), par les noms et les commits seulement ; le fichier où elle est **inscrite à part** (nom neuf sous `registres/t07-etape-b-bis/lecture-v1/`, format, compagnon) ; ce qui vaut refus.
3. **Journal des ouvertures** du registre propre (`registres/t07-etape-b-bis-v1.md.ouvertures.md`) : comment il est créé avant la lecture, par quelle fonction du code si elle existe, sous quel format.
4. **Garde d'ouverture** (plan, point 10 (a)) : la commande, ce qu'elle vérifie (clés et fichiers du point 1, sceaux, antériorités, clé `VERDICT-P3BIS`), comment on sait qu'elle a passé ou refusé **sans lire de mesure**, et ce qui se passe au refus (rien n'est lu ; phrase gelée ; arrêt).
5. **Lecture** : la ligne de commande exacte (module, arguments, chemins, entropie et graines selon le plan, point 12, et les addenda), le dossier du run de lecture et son manifeste, la durée attendue sur 4 cœurs si le code la laisse estimer, le PID relevé, les sorties attendues (`diag/<run-bbis-lecture>/lecture-bbis.json` et autres), leur scellement **avant toute lecture humaine**, la ligne `LECTURE-BBIS` (format du registre propre, par quelle fonction).
6. **Ce que la conductrice commite** : la liste des chemins produits (sur la branche de travail ; dis si le texte veut les sorties de lecture sur une branche de données).
7. **Points ouverts et écarts** : tout endroit où le code, le texte, les addenda, le feu ou le mandat de la session ne s'accordent pas, sans le résoudre toi-même au-delà de ce que le texte tranche.

Tu peux jouer les essais du code de lecture (`python -m pytest -q tests/test_t07bbis_lecture_*.py … --basetemp=…`) pour vérifier que la chaîne tourne sur ses jouets ; tu ne joues rien sur les données réelles.

## Rendu
Le chemin et l'empreinte du fichier de commande ; le module en vigueur (nom) ; la liste des points ouverts (titres) ; les essais joués (noms, passés ou non) ; la liste des fichiers de résultat ouverts (attendue : aucun).
