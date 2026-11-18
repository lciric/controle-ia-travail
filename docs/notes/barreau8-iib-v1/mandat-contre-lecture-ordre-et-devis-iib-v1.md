# Mandat de la contre-lecture de l'ordre exploratoire (brouillon 3) et du devis (brouillon 3) du saboteur à budget — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 19:35Z (GO-2026-11-18-30, GO-2026-11-18-37 ; lignes R-3389, R-3395 du registre des décisions, par leur numéro). Agent neuf, **autre modèle que le rédacteur** (qui était Opus 5.5). Langue : français, sans sigle seul. La session mère ne lit ni le mécanisme ni le sujet de cet agent de test.

## Qui tu es
Un **contre-lecteur neuf, du côté de l'agent de test** : tu n'as écrit ni la conception, ni le code, ni l'ordre, ni le devis. Tu n'as vu et ne verras **aucun interne de moniteur** (ni sonde, ni score, ni poids, ni `src/controle_ia/bases/`, ni `prereg/T0.8-*`, ni `prereg/T0.6-*`). Aucun résultat du programme. Tu es exclu de toute lecture des sondes du barreau 8. **Tentative franche** : à la première réponse refusée (classifieur, permission, crochet), tu t'arrêtes sans reformuler, découper ni contourner, et tu rends le texte exact du refus.

## Ce que tu contre-lis (dossier `brouillons/ii-b-saboteur-budget-v1/` du dépôt principal)
- `ordre-exploratoire-ii-b-v1-brouillon3.md` (`eed42f07329c5f064554b799f0d49ff0a1ed6e4571545c94dca3d6783f0c165f`), contre le brouillon 2 du même dossier, la conception brouillon 2, et le code de `origin/prep/iib-code-v3` (paquet `src/controle_ia/iib/`, par `git show` ; la tête peut avoir avancé : dis laquelle tu lis) ;
- `devis-ii-b-v1-brouillon3.md` (`016979ba01926f08be8ac243df75b716cf49ea63ea01e16dedd4302e61f991d4`), son script `calcul-devis-ii-b-v2.py` et sa sortie (rejoue le script) ;
- `noeuds-ii-b-pour-lazar-v1.md` (`66cd18dff444baba2e247706939635e5f70150e88ec8db4b28e14ce12b515a44`) ;
- les rapports sur le code : `docs/notes/barreau8-iib-v1/contre-lecture-code-iib-v2-v1.md` et `…/verification-courte-code-iib-v3-v1.md` ; de `registres/go.md`, la seule ligne GO-2026-11-10-08.
**Tu n'ouvres pas les deux fichiers de consigne privée** du dossier (noms commençant par `consigne-privee`).

## Ce que tu vérifies
1. **Marqueurs** : les 14 remplis le sont-ils juste (contre le code, la ligne d'accord, le journal) ? Les 16 en attente et les 2 neufs attendent-ils bien un fait à venir, et qui les remplit ?
2. **Ordre des opérations** : exécutable de bout en bout, sans cercle (code revu, commit de lancement, configuration, épreuves de l'oracle en réel sur la carte avant le premier épisode, essais du jetoniseur réel, arrêts) ; chaque arrêt est par identifiant (R10) ; gardes éprouvées sur cas sain et artefact (R5) ; graines (R9) ; aucune moyenne ni médiane sur les jetons dans une sonde.
3. **Les deux constats du rédacteur** : (i) la ligne d'accord dit « avec l'activité interne enregistrée », alors que la conception et le code n'enregistrent rien — est-ce exact ? Que coûterait d'enregistrer l'activité interne pendant la course (code, disque, durée, dollars), contre la recalculer plus tard (ce qu'il faut garder pour que ce soit possible : épisodes, adaptateurs, graines ; coût) ? Écris les deux branches sans trancher. (ii) l'amorce ne pousse pas les fichiers écrits par phase et par tour : est-ce exact (lis les lignes citées), et la correction proposée suffit-elle ?
4. **Devis** : chaque chiffre a-t-il sa source au dépôt ; arithmétique rejouée ; pire cas ; la variante B (ligne inscrite, plafond 60 USD, coupure 55) est-elle bien acceptée par la garde du code ; l'échéance de la ligne d'accord (2026-11-27) laisse-t-elle le temps de la course et de sa marge ?
5. **La note des nœuds** : chaque nœud au format de décision, en mots clairs, sans rien trancher à la place de Lazar ; un nœud manque-t-il ?

## Ce que tu rends
Rapport scellé `docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-v1.md` (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) : verdict pour l'ordre (« scellable en l'état », « scellable après corrections », « non scellable »), verdict pour le devis (« demandable en l'état », « demandable après corrections », « non demandable »), bloquants et majeurs avec couples avant → après, et les deux branches du constat (i) chiffrées. Rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun autre fichier de `registres/` ; pas de recherche récursive hors des chemins cités. Ni commit, ni poussée. **Ton dernier message ne nomme aucun sujet ni mécanisme de l'agent de test** : verdicts, chemin, empreinte, bloquants par identifiant et phrase neutre, les deux branches du constat (i) en une ligne chacune avec leur coût, refus éventuels mot pour mot, lectures hors mandat.
