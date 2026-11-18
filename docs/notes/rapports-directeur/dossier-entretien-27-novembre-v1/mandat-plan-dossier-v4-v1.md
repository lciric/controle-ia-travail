# Mandat du rédacteur neuf du plan du dossier d'entretien v4 — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:10Z, sur le mot de Lazar « oui go » (R-3302) et GO-2026-11-18-30. Langue : français, sans sigle seul : chaque chose est nommée par ce qu'elle est et ce qu'elle fait (l'identifiant vient en appui seulement).

## Objet
Écrire **le plan** du dossier de l'entretien du 27 novembre 2026 avec le Transformative AI Fund, version 4, sous `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/plan-dossier-v4-v1.md`, scellé. Ce n'est **pas** le dossier : c'est la liste exacte de ce qui doit y entrer, qui l'écrit, avec quelles sources, dans quel ordre, et à quelle date au plus tard, pour que tout soit prêt le **24 novembre** (au plus tard le 25 ; R-2382). Deux terrains : **le contrôle boîte blanche des menaces diffuses** (l'échelle des barreaux 1 à 8 du LISEZMOI v1) et **l'organisme d'idéation** (second terrain : son juge comme surveillant ; courses du 17 et du 18 novembre ; auto-conception ; affinage des idées des mentors).

## Ce que tu lis — et seulement cela
- `docs/notes/rapports-directeur/dossier-entretien-27-novembre-v1/LISEZMOI.md` ; les manifestes de parties `dossier-entretien-fusionne-v3-parties.json` (et v2 pour comparaison) — **noms et empreintes des parties seulement** ; ne lis pas le contenu des parties de résultats.
- `brouillons/entretien-taif-v3/` : les **noms** des fichiers ; tu peux lire en entier le programme de l'entretien de version la plus haute et sa version condensée en 30 minutes, et l'en-tête (statut, date, sources) du socle de preuves de version la plus haute.
- `docs/notes/rapports-directeur/ce-qui-manque-approche-peut-marcher-v1.md` et `premisses-trace-interne-v1.md` (textes de cadrage, sans résultat).
- `registres/scellements-v1.md` : la **colonne des clés et des dates** seulement (quelles pièces sont scellées, quand) ; `registres/go.md` (lignes GO-2026-11-10-08, GO-2026-11-14-09, GO-2026-11-18-14 à -33) ; `registres/decisions.md` : les lignes **R-3125, R-3129, R-3284 à R-3308** et les lignes que celles-ci citent nommément, par leur numéro, rien d'autre.
- `registres/etat.md` : l'en-tête et le tableau des tâches.
- Les **noms** de fichiers sous `docs/notes/` qui concernent l'organisme d'idéation, les organismes discrets, la copie publique expurgée (`scripts/depot_expurge*`), la lecture par lentille neuronale.

## Ce que tu ne lis jamais
Aucun résultat, aucune issue, aucun score, aucune aire, aucun texte de sortie ni de verdict de 7a, 7b, T0.6, T0.7 (étape A comprise), de la base « mots et coût », de l'étape B, de l'étape B bis, du premier test boîte blanche bis (P3-bis) ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; aucune fiche ni consigne de l'organisme d'idéation ; aucun sujet de saboteur discret (noms et états seulement). Pas de recherche récursive dans le dépôt. Si tu ouvres par erreur quelque chose d'interdit, arrête et déclare-le.

## Ce que le plan doit contenir
1. **Table des parties du dossier v4** : pour chacune, état actuel (fait, à mettre à jour, à écrire), pièce source (chemin, empreinte), **qui l'écrit** (rôle, en respectant les exclusions : la mère n'écrit ni ne lit aucune section de résultats de l'étape B, de l'étape B bis, de P3-bis ; un lecteur neuf ou une session autorisée le fait), date au plus tard.
2. **L'échelle des barreaux 1 à 8** à jour par **nom et état** (scellé, joué, verdict scellé, en cours, à faire), d'après les clés du registre des scellements et les lignes du registre des décisions ; pour les barreaux 6, 7 et 8, ce qui manque avant le 24 (GO-2026-11-18-30).
3. **L'organisme d'idéation** : ce qu'on peut présenter (par nom et état) et ce qui manque.
4. **La copie publique expurgée** : état du script (versions 8 à 11), ce qui manque pour la régénérer ; rappelle que la régénération est une publication qui exige un GO exprès de Lazar.
5. **Le calendrier** jusqu'au 24, jour par jour, avec les dépendances (verdict de l'étape B bis le 22 au plus tard ; sections de résultats ensuite ; assemblage ; vérification par un lecteur neuf).
6. **Les décisions à demander à Lazar**, au format : décision en une phrase ; enjeu ; deux ou trois options avec avantage et inconvénient ; recommandation et confiance ; défaut sous 48 heures.

## Ce que tu rends
- Le plan, scellé : `PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>` ; ne commite pas, ne pousse pas, n'écris pas dans `registres/`.
- Ton dernier message : chemin et empreinte du plan, le calendrier en dix lignes au plus, les décisions à demander à Lazar, et toute lecture faite hors de ce périmètre.
