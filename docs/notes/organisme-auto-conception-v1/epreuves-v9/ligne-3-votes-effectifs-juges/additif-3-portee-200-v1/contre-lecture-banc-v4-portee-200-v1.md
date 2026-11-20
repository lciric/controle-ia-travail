# Contre-lecture du banc v4, mode « portée à 200 » — v1

Pièce de travail (classe C) sur un instrument (classe B). Contre-lecteur, modèle S. Mandat `mandat-contre-lecteur-banc-v4-portee-200-v1.md` (`2e9b029a…`, empreinte vérifiée). Règle d'aveugle tenue : aucune mesure de l'étage 1 ouverte. Aucune racine 2026112031 à 33 ni 2026111931 à 37 dérivée ; seule la racine des essais a servi. Aucune écriture dans le dépôt.

## Verdict : Conforme

Aucune correction exigée. Quatre précisions à porter à l'additif de code (§ 3 ci-dessous), non bloquantes.

## 1. Différentiels
Les quatre `diff -u` refaits (banc, essais, contrôle, chronométrage) sont égaux à ceux du développeur, aux deux lignes d'en-tête près (chemins et dates). Hors du § 5 de l'additif 3, rien ne change ; `cellule_puissance`, `resoudre_dissymetrie`, `erreurs_equilibrees_formules`, `holm`, `p_valeur_unilaterale`, `puissance_qui_decide` et les autres fonctions de calcul sont absents du différentiel du banc. Empreintes des cinq fichiers du mandat et du banc v3 : égales aux compagnons ; additif 3 (`71b7a876…`) et additif 2 (`f5562d20…`) relus sur `origin/main`, empreintes égales.

## 2. Code, point par point
- Configuration gelée : répliques 2 000, tirages 2 000, écarts 0,05 ; 0,10 ; 0,15, lois 1 et 3, sept ρ, trois ρ′, n = 200 ; hors essai, `cfg != CONFIGURATION_PORTEE_200` refusé ; `main` passe la constante.
- Racines : `verifier_racine` (pure, appelée d'abord par `generateurs`) refuse 2026111931 à 37 avant tout autre test, avec ou sans autorisation ; 2026112031 à 33 exigent l'autorisation, la tâche de la table (31 : clés 2 et 12 ; 32 : clé 2 ; 33 : clé 12) et `.spawn(210)`. Les modes de l'étage 1 sont retirés de `MODES` ; `executer_etage_1` refuse hors essai ; `--decisif` est refusé par argparse (essayé, code 2). `CONFIGURATION_DECISIVE` reste en constante morte, inatteignable.
- Garde « dossier du code propre » : appelée dans `executer_portee_200` avant `verifier_racine` et avant toute dérivation (ordre vu au code et à l'exécution : refus « hors d'un dépôt git » avant le contrôle de l'autorisation). Elle refuse sortie sous le code ou égale, `archives-reponses-modeles/`, hors dépôt, `git status --porcelain` non vide ou en échec.
- Une exécution par dossier : contrôle avant dérivation ; dossier créé après le calcul, donc une exécution interrompue se relance dans le même dossier.
- Règle de lecture : comptes entiers, `2 * k >= R` → A (1 000 sur 2 000 est A, 999 est B), comparaison sans cellule faisable → B ; `comptes_gagnes` relit k et exige `k / R == p` (exact, la puissance étant une moyenne de booléens). L'aide ne porte aucun verdict.
- Chronométrage : dérive 2026112031 seule, n'imprime que trois lignes de durées ; son manifeste ne porte aucune puissance. Garde commune au banc, variables de chemin et autorisation vérifiées avant dérivation.
- Gardes déterministes (formules, treize mondes, ancres 1,2 d et 0,6 d, règle de lecture) avant le premier tirage.

## 3. Essais et défauts rejoués
- Essais, dans une copie du dossier du code (bloc-notes), avec le Python de l'environnement du dépôt (numpy 2.4.6) : **157 passed**. Rejoués aussi avec `python3` (numpy 2.5.3, l'interpréteur des commandes de lancement) : **157 passed**.
- Contrôle des défauts réintroduits, mode « visé », rejoué : essais visés sur le banc sain 123 passés ; **138 défauts vus sur 138**, aucun non vu ; familles : v1 27, contre-lecture 35, c2 1, v2 1, graines 6, silence 1 10, silence 2 11, égalité 2, v4_portee_200 39, v4_chronometrage 6 ; « tous vus : True ». Comptes égaux à ceux du rapport. Lecture des défauts neufs : aucun ne peut faire dériver une racine (chaque essai visé appelle `verifier_racine` avant tout appel dérivant). Le mode « complet » (157 / 138) n'a pas été rejoué ; le mode visé est celui du mandat.
- Manque : le chemin hors essai avec une autorisation juste n'est jamais exécuté de bout en bout (il dériverait) ; il est couvert par lecture (`main` → `Contexte("portee_200")` → `verifier_racine` → dérivations 2032 clé 2 et 2033 clé 12, 210 enfants). Aucune faute vue.

## 4. Remarques du rapport (§ 6)
1. Dossier du code à commiter entièrement avant le lancement : **garder** ; la garde est stricte (un fichier non suivi refuse). Rapports de défauts, différentiels et copies du v3 compris. Aucun fichier du dossier ne doit être ignoré par `.gitignore` sans que la mère le sache (un fichier ignoré passe la garde ; l'identité tient à `programme_sha256`).
2. Garde sur le chronométrage : **garder** (plus strict que la lettre, sans inconvénient).
3. Clés imposées plus strictement : **garder** ; conforme au tableau du § 2.
4. Compte relu sur la puissance : **garder** ; exact, vu.
5. « Près du seuil » bornes comprises (956 à 1 044) : **garder** ; mention seule, sans effet sur l'issue ; 0,478 × 2 000 = 956 et 0,522 × 2 000 = 1 044. À l'agent qui prononce de lire la mention.
6. Aide qui porte aussi la lecture du banc v3 : **garder**, utile au contrôle croisé.
7. Comparaison de `d`, a, b à l'étage 1 : **à l'agent qui prononce** (le code ne lit aucune mesure).
8. Interruption écrite au manifeste : **à la mère**.

## 5. Les deux commandes de lancement
Justes : même forme que le gabarit du § 5 de l'additif 3 et que l'additif 2 § 6 ; elles refusent proprement (essayées avec un additif absent : refus code 2, sans dérivation, sans dossier). Suffisantes pour l'additif de code à condition qu'il porte :
- (a) le chemin absolu de l'additif de code et l'empreinte de son compagnon (`CHEMIN`, `HEX`) ;
- (b) le commit du dossier du code, tous fichiers suivis et propres, avec l'empreinte de chaque fichier (`79865552…`, `6b9d2cbf…`) ;
- (c) **l'interpréteur** : les essais du développeur sont lancés avec le Python de l'environnement du dépôt (numpy 2.4.6), les commandes de lancement avec `python3` (numpy 2.5.3). Les 157 essais passent sous les deux, mais l'additif doit nommer l'interpréteur et la version de numpy retenus, car des flux de tirage non uniformes peuvent différer d'une version à l'autre de numpy ; le manifeste consigne `versions.numpy` ;
- (d) `DOSSIER` et `DOSSIER_NEUF` absents, hors du dossier du code ; `BANC_LIGNE_3_CHEMIN` et `CHRONOMETRAGE_LIGNE_3_CHEMIN` non posées ; chronométrage d'abord, mesure ensuite, une fois ; échéance 2026-11-30.

## 6. Écarts
Aucun écart au mandat. Fichiers de travail dans mon dossier : copie du code, différentiels refaits, additifs relus, rapport de défauts en sortie standard de la tâche.
