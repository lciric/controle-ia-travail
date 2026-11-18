# Mandat du développeur neuf des corrections du saboteur à budget — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18 vers 16:30Z, sur le mot direct de Lazar dans la session mère (R-3314, GO-2026-11-18-37) : « Option 1 : une tentative franche de correction du saboteur à budget, par un développeur neuf, arrêt au premier refus. […] : utilise opus 4.6 », puis « en cas de refus passe a sonnet 4.6 ». Langue : français, sans sigle seul.

## Qui tu es
Un **développeur neuf** (session dédiée). Tu n'as écrit ni la conception, ni le code v1, ni sa contre-lecture. C'est une **tentative franche et unique** de ta part : à la **première** réponse refusée (refus du classifieur de sécurité, refus d'une permission, refus du crochet de garde), tu t'arrêtes, tu ne reformules pas, tu ne découpes pas, tu ne contournes pas, et tu rends compte à la session mère du texte exact du refus. La décision de la suite revient à Lazar par la mère.

## Contexte (barreau 8 de l'échelle de l'entretien : « un sabotage vraiment diffus laisse-t-il une trace ? »)
- Ligne d'accord de la course, plus tard : GO-2026-11-10-08 (A100, 60 USD, échéance 2026-11-27), qui exige avant toute course : code rendu et contre-lu, devis inscrit, ordre exploratoire contre-lu et scellé, six épreuves de l'oracle passées en réel. **Ton mandat s'arrête au code corrigé et éprouvé sur processeur.**
- Code v1 : branche `origin/prep/iib-code-compte4-v1` (tête `3baecee7`, paquet `src/controle_ia/iib/`, essais `tests/test_iib_*`, 374 essais verts, répétition jouet, épreuves de l'oracle sur données factices).
- Contre-lecture du code v1 : `brouillons/iib-code-compte4-v1/contre-lecture-1-code-iib-v1.md` sur `origin/lot/compte-4-v1` (avec sa consigne et son calcul) : « autorisable après les corrections listées », 1 bloquant, 6 majeurs, 11 mineurs.
- **Bloquant** : des fragments de la consigne privée du maître se trouvent dans du code poussé sur `prep/iib-code-compte4-v1`. **Décision de la mère (sous l'autonomie GO-2026-11-18-26, sans réécriture d'historique)** : la branche v1 reste gelée telle quelle (rien n'y est poussé ni réécrit ; elle sera exclue de la copie publique) ; tu écris la version corrigée sur une **branche neuve partie de `main`**, dans laquelle **aucun fragment de la consigne privée n'apparaît dans le code ni dans les essais** : la consigne reste un fichier privé, lu à l'exécution par son chemin et vérifié par son empreinte. Tu n'écris **aucun outil de masquage** ni de réécriture de texte.
- Les conceptions et brouillons : `brouillons/ii-b-saboteur-budget-v1/` sur `origin/lot/compte-4-v1` (conception, ordre, devis, contre-lecture 1).

## Ce que tu fais
1. Lis la contre-lecture du code en entier, puis le code v1 et ses essais.
2. Sur ta branche neuve (celle de ta session), reporte le code v1 sans les fragments, puis applique les corrections : le bloquant (comme ci-dessus), les 6 majeurs, les mineurs que tu peux faire sans changer une règle de conception ; tout mineur non fait est déclaré.
3. Essais : les 374 essais existants (adaptés seulement là où une correction l'exige, chaque adaptation déclarée), plus un essai par correction ; chaque garde éprouvée sur un cas sain et sur un artefact (R5) ; graines par `numpy.random.SeedSequence` (R9). Répétition jouet rejouée, comparée à l'octet à celle de la v1 quand la correction ne doit rien changer.
4. Rapport de développeur scellé (`PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`) : corrections une par une (couple constat → changement → essai), comptes d'essais, écarts, ce qui reste avant la contre-lecture neuve (par un autre modèle) et avant l'ordre et le devis.
5. Commite et pousse **ta branche seulement** ; envoie à la session mère (`session_013QMayjsoZJFBUCqcnvD5h1`) un message court : branche, tête, empreinte du rapport, comptes d'essais, écarts, et tout refus rencontré, mot pour mot.

## Règles fermes
- **Aucune dépense, aucune machine louée, aucun modèle chargé** : processeur, données factices et jouet seulement.
- **Cloisonnement** : aucun résultat, aucune issue, aucun score de 7a, 7b, T0.6, T0.7, de la base « mots et coût », de l'étape B, de l'étape B bis, de P3-bis ; rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucune branche `calcul/` ou `donnees/` ; **aucun code, score ni poids de sonde ou de moniteur** (le saboteur doit être conçu et écrit sans rien voir d'un moniteur) ; pas de recherche récursive dans le dépôt hors de `src/controle_ia/iib/`, `tests/test_iib_*` et des dossiers cités.
- **Tu as lu la consigne privée** : tu es exclu de tout rôle de lecteur des sondes du barreau 8, et tu ne la recopies dans aucun message, rapport ou fichier versé.
- Aucune écriture dans `registres/` ni sur `main`.
