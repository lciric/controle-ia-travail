# Attestation sur les graines — développeur du code v2 du banc A, ligne 1 — v1

Atteste : développeur, modèle L′. Heure (`date -u`) : 2026-11-19T22:01:04Z.

**Pendant l'écriture et les essais du code v2, je n'ai dérivé aucune graine des racines 2026111901, 2026111902 ni 2026111903.**

## Sur quoi je fonde cette phrase

Ce que j'ai exécuté, en tout et pour tout (bloc-notes seulement : copie d'essai `developpeur-banc-a-v2/travail-copie-essais/`, dépôt git à part ; organisme d'essai `developpeur-banc-a-v2/organisme/`) :

1. Lectures et empreintes (`sha256sum`, `cat`, `grep`, `sed -n`, `git log`, `git show`) dans le dépôt de travail. Extraction de `memoire_v53.py` par `git show` : aucun code de l'épreuve n'est exécuté.
2. Mise en place de la copie d'essai : `cp`, `git init`, `git add`, `git commit` (dans le bloc-notes) ; l'outil `outils/preparer_v2.py`, qui ne fait qu'écrire la configuration v2, calculer des empreintes et commettre dans la copie. Il n'importe pas le banc.
3. Suites d'essais complètes, par pytest, sur la copie : les 42 essais du code v1, deux fois ; les essais du code v2, quatre fois (56 essais, puis 58). Toutes ces passes ont réussi, y compris le dernier essai, `test_zz_aucune_racine_interdite_derivee`. Celui-ci vérifie dans le processus que la table des premières dérivations du banc (`B.GRAINES.premieres`) ne contient ni 2026111901, ni 2026111902, ni 2026111903. Dans le code du banc, la dérivation passe par `Graines.__call__` (seul appel à `graine_de_tache` dans le code du banc et dans le code v2, vérifié par lecture), qui consigne chaque racine dérivée.
4. Racines employées par les essais : la racine des essais, 2026111900, seule. Là où un essai passe une configuration à l'étalonnage, à l'analyse ou à la décisive, il y place 2026111900 (`racines` réécrites dans les essais des corrections 3, 7 et 8 et dans l'essai A12). Deux essais seulement passent la configuration réelle, et ils s'arrêtent avant toute dérivation :
   - l'essai de la correction 2 appelle `etalonner`, qui rend la sortie scellée déjà présente (`reprendre_sortie`) avant toute ligne qui dérive une graine ;
   - l'essai de la correction 5 appelle `decisive`, qui lève `DecisionMereRequise` avant `GRAINES(racine décisive, "ouverture|decisive")`.
   L'essai de la reprise concurrente appelle `main tout` ; celui-ci rend le code 4 avant `preparer`. Les seuls sous-processus lancés par les essais exécutent `python -c pass`, une attente (`time.sleep`) ou `git` : aucun n'importe le banc.
5. Contrôle R4 par mutations (`outils/mutations_v2.py`) : 18 passes de pytest, chacune limitée à un seul essai, sur une copie mutée. Ces passes n'exécutent pas `test_zz` ; pour elles, l'affirmation repose sur la lecture de chaque essai muté :
   - chacun emploie la racine des essais, ou échoue avant tout appel qui dériverait une racine du préenregistrement ;
   - mutation de `DecisionMereRequise` : l'essai échoue à la boucle des artefacts, avant d'appeler `decisive` ;
   - mutation du contrôle des processus vivants : l'essai échoue avant `main`. Et dans toute copie mutée, `preparer` refuserait de toute façon un code dont l'empreinte diffère de la configuration v2.
6. Je n'ai lancé ni l'étalonnage, ni la course décisive, ni la fumée, ni `--reel`, ni aucune étape du lanceur hors des essais.

Limite : le contrôle par programme (`test_zz`) ne couvre que les passes complètes (point 3). Pour les passes de mutation (point 5), l'affirmation repose sur ma lecture des essais et du code, non sur un contrôle exécuté.
