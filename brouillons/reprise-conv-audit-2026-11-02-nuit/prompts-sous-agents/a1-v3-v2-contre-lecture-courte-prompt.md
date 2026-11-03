Tu es le contre-lecteur neuf (règle R2) du texte de la **seconde course d'A1-v3**. Tu n'as écrit ni la v1 scellée, ni ce brouillon, ni le code, ni l'audit. Français, sans sigle non développé ; toute heure vient de `date -u`.

## Ce que tu lis
- **Le brouillon** : `/home/claude/wt/a1-v3-seconde/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v2-brouillon1.md` (`c76ac6bc9e1f94a05962bac3f0d4667f0705d2f2e07db7853923e43160370d29`) ; **le diff** depuis la v1 : `…/diff-attaque-goodhart-v3-v1-vers-v2-brouillon1.txt` (`9dd6d2ff…`) ; **le rapport du rédacteur** : `…/rapport-redaction-attaque-goodhart-v3-v2-brouillon1.md` (`ec4e797f…`), ses scripts et sorties sous `/home/claude/scratch/a1-v3-seconde-redacteur/`.
- **La v1 scellée** : `/home/claude/wt/a1-v3-seconde/orchestrator/prereg/preenregistrement-attaque-goodhart-v3-v1.md` (`898d5be4…`, compagnon égal).
- **L'audit A9** de la première course : `/home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/a1-v3-seconde-course-v1/audit-A9-a1-v3-premiere-course-v1.md` (`ed078aaa…`).
- **Le GO** : GO-2026-11-03-01, dans `/home/claude/controle-ia-travail/registres/go.md` (lis la ligne en entier).
- Le code au commit gelé `9776ed0` : `/home/claude/wt/a1-v3-seconde/orchestrator/demonstrations/attaque_goodhart_v3.py` et `pole/attaque_goodhart_v3.py` (lecture seule).

## Décision du directeur, à vérifier dans le texte
**Source du registre des GO** : le registre de `main` est refusé en entier par le lecteur du lanceur (seize identifiants en double) ; la copie du registre se prend sur la branche `canal/conv-audit-n04`, à un commit qui porte la ligne GO-2026-11-03-01 (comme la première course, qui l'avait prise au commit `e9d7b78d` de cette branche), sans retouche, et la sortie de `grep -n "GO-2026-11-03-01"` sur la copie et sur le registre de `main` est écrite au journal de lancement avant la course.

## Ce que tu fais (contre-lecture **courte, sur le delta**)
1. Vérifie que le diff ne contient **que** les 36 changements listés (section 0.6), un par un, et qu'aucune hypothèse, prédiction, métrique, critère de lecture, audit, garde de la liste d'arrêt, ni le bloc d'empreintes du code ne change (sauf ce que la liste dit).
2. Rejoue l'épreuve du lanceur du rédacteur si tu le peux (sans réseau, sans modèle, jamais `--moteur reel`, aucun `.sha256` dans le dépôt : un compagnon simulé dans un dossier temporaire seulement) ; dis ce qui passe et ce qui est refusé.
3. Vise en particulier : la règle de la section 8 qui admet la course et la conclusion de l'audit A9, citées exactement ; la graine neuve ; le GO (montant 400 USD exactement, échéance, refus de GO-2026-11-02-21 en ligne de commande) ; la source du registre (décision ci-dessus) ; l'hôte nommé et la session gardée active avec une période nettement inférieure à 5 minutes, l'observation hors du conteneur ; la fin brutale acceptée et dite ; les 4,245753 USD non imputés ; le PID du guetteur ; « rapportée avec la course arrêtée, jamais seule » ; aucun marqueur restant ; la commande exacte (seuls chemins, GO et texte changent).
4. Le danger relevé par le rédacteur : GO-2026-11-02-21 reste valide et rien dans le code n'empêche une relance de la v1 ; dis ce que le texte doit en dire (la règle de la section 8 interdit-elle déjà une relance sous la v1 ?).

## Rendu
Rapport `/home/claude/scratch/a1-v3-v2-contre-lecture/contre-lecture-courte-attaque-goodhart-v3-v2-brouillon1.md` : verdict (scellable / scellable après couples / non scellable) ; bloquants, importants, mineurs ; couples « ancien → nouveau » (texte exact, chaque « ancien » unique dans le brouillon) dans `couples-contre-lecture-attaque-goodhart-v3-v2-brouillon1.json`. Réponse finale : verdict, comptes, chemins et sha256.

## Interdits
Aucun commit, aucun `.sha256` dans un dépôt, aucun fichier existant modifié ; rien sous `donnees/` ; aucun `git fetch`, `checkout`, `stash` ; aucun réseau, aucun modèle ; `nice -n 10 python3 -I -B`.
