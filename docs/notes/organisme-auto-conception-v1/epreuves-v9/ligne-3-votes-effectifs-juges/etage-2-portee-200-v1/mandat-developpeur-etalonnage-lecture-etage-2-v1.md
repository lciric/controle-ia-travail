VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-I -B`

AUCUNE COMMANDE DE LISTE HORS DE TON DOSSIER. TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

**AUCUNE COMMANDE SUR UN CHEMIN SOUS `archives-reponses-modeles/`. AUCUN VERDICT RÉEL N'EXISTE : TOUT S'ÉPROUVE SUR DES VERDICTS FACTICES.**

# Mandat du développeur — étalonnage et lecture unique de l'étage 2 à 200 (ligne 3, organisme v9) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur l'inventaire (gestes 17 et 18) et l'accord de la mère (R-4272 et suivantes : travail sur processeur seul ; ordre générateur, fragments, étalonnage, lecture, puis additif de code). Pièce d'instrument (classe B) : vérification par un autre modèle (S), vérification des corrections par le même ; puis l'additif de code de l'étage 2, scellé par la mère.

## Qui

Un développeur neuf, modèle O, qui n'a écrit ni le texte de la ligne 3, ni ses additifs, ni le banc de l'étage 1, ni le code d'appel, ni le générateur. Tu signes « développeur, modèle O ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier L3 = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`.
- Le texte v7 `L3/preenregistrement-ligne-3-votes-effectifs-juges-v7.md` (`4e3680d9…`) : « Plan d'analyse » § « Étage 2 » en entier (l. 243 à 300 : bras de l'étage 2, lecture par colonne, **lecture unique**, l. 297), « Graines » (l. 301 à 305 : racine 2026111936 pour le rééchantillonnage de la lecture), « Critères de lecture gelés » (l. 307 à 351 : table de l'étage 2, audit de symétrie, rangs), « Liste d'arrêt » (l. 352 à 389), annexe A (l. 562 : `etalonner_ligne_3_v1.py`, `lire_ligne_3_v1.py`). Lis-les en entier.
- L'additif 3 v3 (sur `origin/main`, `prereg/organisme-auto-conception-v9/`, `71b7a876…`), § 4.2 (tailles à 200) ; le verdict « portée à 200 » v2 (`02928723…`, **issue B** : comparaisons d'agrégations **descriptives**, aucun « oui » possible ; rangs atteignables : 1 et 3 ; ρ′ − ρ rapporté comme mesure).
- Le banc de l'étage 1 (code v4 de la portée à 200, `L3/code-portee-200-v4/`, et son prédécesseur) : **réutilise** ses estimateurs (votes effectifs, ρ, ρ′, bras d'agrégation, rééchantillonnage des comptes de configurations), par import à empreinte vérifiée ou par copie déclarée, sans les réécrire.
- Le code d'appel v4 (`L3/etage-2-portee-200-v1/code-appel-v4/`, `082d19d6…`) : format du dépôt scellé des verdicts que tu lis ; le générateur v3 (`L3/etage-2-portee-200-v1/generateur-v3/`, `f5de9c3c…`) : format de la banque, du journal de construction et du partage.

## Ce que tu écris (ton dossier, sous-dossier `etalonnage-lecture-v1/`)

1. **`etalonner_ligne_3_v1.py`** : lit **la seule moitié « étalonnage »** (refus nommé s'il touche une ligne de la moitié « lecture ») ; poids, seuil et ρ d'étalonnage, à la lettre du texte ; les écrit et les scelle (`.sha256`) ; manifeste (R9).
2. **`lire_ligne_3_v1.py`**, **lecture unique** : refuse de tourner si son rapport existe déjà, si l'étalonnage n'est pas scellé, si **l'audit de symétrie** (règle R4) n'est pas écrit et scellé avant (l. 297, 305 (10), 347-350) ; lit la moitié « lecture » ; rééchantillonnage sur la racine **2026111936** (`SeedSequence`, clés en constantes) ; lecture par colonne (matrice juge × auteur) ; table de l'étage 2 **en issue B** (comparaisons d'agrégations descriptives, rangs 1 et 3 seuls atteignables, « ρ′ − ρ positif pour les deux juges » rapporté comme mesure sans verdict) ; « non concluant par manque de témoins » si moins de 40 témoins complets dans la moitié « lecture » (compteur coupé compris) ; juge « non mesuré » (plus de 10 % d'absents, plus de la moitié de répétitions identiques) ; audit « trop propre » ; rapport scellé ; manifeste.
3. **`essais_etalonnage_lecture_ligne_3_v1.py`** (pytest) : sur **verdicts factices** produits par des juges scriptés (lois de l'étage 1, valeurs plantées connues) : estimations proches des valeurs plantées à grand n ; chaque garde de la liste d'arrêt qui touche l'étalonnage et la lecture, **cas sain et artefact** (R5), dont : étalonnage qui lit la moitié « lecture » → refus ; lecture rejouée → refus ; lecture sans audit de symétrie scellé → refus ; coupure au pire cas du calcul plafond v2 (197 témoins complets, dont 100 de la moitié lecture) → lu ; moins de 40 complets → « non concluant par manque de témoins » ; issue B → aucun « oui » rendu.
4. **`rapport-developpeur-etalonnage-lecture-etage-2-v1.md`** : ce qui est réutilisé du banc (chemins, empreintes) ; ce que la lettre ne fixe pas (silences, non tranchés) ; essais (commande, comptes) ; **ce que l'additif de code devra porter** (fichiers, empreintes, commandes, racine 2026111936 autorisée, ordre étalonnage → audit de symétrie → lecture).
5. **`table-empreintes-etalonnage-lecture-v1.txt`**.

Essais : `env -C DOSSIER /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider F` sur ta copie (tâche de fond s'ils sont longs). Chaque fichier avec son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`).

Ton dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/developpeur-etalonnage-lecture-etage-2/`.

## Interdits

Voir en tête. Aucun appel à un fournisseur de modèles, aucune dépense, aucune clé, aucun réseau. Aucune écriture dans le dépôt de travail ni dans le clone de l'organisme, aucun commit. Rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune publication d'artefact. Aucun identifiant de modèle dans les pièces. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
