# Mandat « corpus v2 : tri à la lecture » des billets — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 18:35Z (GO-2026-11-18-43 ; R-3364). Langue : français, sans sigle seul.

## Pourquoi
Le corpus v1 (`manifeste-corpus-v1.json`, `7d063832…` ; rapport `rapport-corpus-et-grille-v1.md`, `0113a85e…` ; règle `regle-classement-et-appariement-v1.md`, `868f57ad…`) trie « billet de résultats empiriques » par programme et se trompe environ une fois sur trois (contrôle `controle-classement-dev-v1.json`). Il faut un tri **à la lecture**, avant un nouveau partage.

## Qui tu es
Un agent neuf, **trieur seulement** : tu n'écris ni ne modifies la grille des gestes, et tu ne seras pas codeur. Tu ne lis aucun résultat du programme (rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, aucun registre).

## Tâches
1. Lis le rapport, la règle et les scripts v1 (`docs/notes/billets-v1/scripts/`), et réemploie-les ; texte brut toujours **hors du dépôt** (`/home/user/billets-corpus-v2/`), une requête par seconde au plus, agent utilisateur générique.
2. Étiquettes : les sept de la v1, plus « autoencodeurs épars » et « ingénierie des activations » (méthodes sur l'état interne, proches des nôtres) ; pas « évaluations » ni « alignement de la chaîne de raisonnement ». Éclaircis l'écart de compte de l'étiquette « contrôle de l'IA » (411 billets rendus pour 889 affichés : pagination, filtres ?) et dis-le.
3. **Règle de tri à la lecture, écrite et scellée avant de trier** (`regle-tri-a-la-lecture-v2.md`) : est « billet de résultats empiriques » un billet dont l'objet principal est de rapporter une expérience des auteurs, avec au moins un chiffre ou une figure de résultat ; cas limites dits d'avance (essai avec une figure, annonce d'article, réplication, exposé théorique avec simulation).
4. Par année de 2022 à 2026 : lis les candidats par votes décroissants et retiens les **15 premiers vrais** billets de résultats ; pour chacun, lis des candidats peu notés (mêmes étiquettes, même année, tiers bas, rapport de longueur de 0,67 à 1,5) jusqu'à un **apparié vrai**, trois essais au plus ; un billet bien noté sans apparié est gardé et marqué. Pour chaque décision de tri : une ligne (identifiant, décision, motif en dix mots). Les dix commentaires les mieux notés de chaque billet bien noté.
5. **Nouveau partage** par programme (graine par `numpy.random.SeedSequence`, neuve et consignée), moitié « développement », moitié « tenue à l'écart », stratifié par année et par classe ; manifeste `manifeste-corpus-v2.json` ; dossier de la moitié tenue à l'écart rendu illisible après le partage.
6. Rapport `rapport-corpus-v2.md` : décomptes, taux de candidats écartés à la lecture, billets sans apparié, limites ; ce que la v2 change pour la grille (rien n'y est modifié par toi).

## Règles
Sorties scellées (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) ; ni commit, ni poussée, rien dans `registres/` ; disque : 300 Mo au plus ; arrêt au premier refus. Dernier message : chemins, empreintes, décomptes, points à trancher, lectures hors mandat.
