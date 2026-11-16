# Contre-lecture de la procédure de la machine du jeu relancé de l'idée 1.1, tour 3 (v1)

- **Auteur** : contre-lecteur neuf (R2), lettre C. Il n'a écrit aucune pièce (pièces de la lettre A). Il est aussi l'auteur des rapports des tours 1 et 2.
- **Heures (UTC, `date -u`)** : de 21:53Z à 21:57Z environ.
- **Pièce jugée** : `procedure-machine-jeu-idee-1-1-v4.md` (empreinte `996c8a5cbe9d7cacba32124118dff30af8eb47ebf431a9c72925a7619687b24f`, lue sur disque et dans son compagnon) ; les 19 compagnons du dossier : `OK`.
- **Lu** : rapport du tour 2 ; différentiel v3 → v4 (`diff`) ; programme `corriger_procedure_v3_vers_v4_tour2_v1.py` ; § 1, § 2 et gestes 12 à 16 de la v4 ; amorce v1 (recherche de `reprise_sorties` : 0 occurrence ; empreinte `ede38bb6…` inchangée) ; contenu du dossier.
- **Rejoué** : la répétition locale entière, dossier neuf du bloc-notes, 21:53:5xZ à 21:56:06Z : **110 cas, 0 écart, code 0** (aucun appel au loueur, aucune machine, aucune dépense).
- **Recoupé** (lecture seule) : `origin/main` = `396c4a0c098b…` (local et `ls-remote`) ; `14a0dfc5…` en est ancêtre ; addendum de relance présent sous `prereg/`.

## Verdict : `corrections`

La v4 applique fidèlement les corrections du tour 2 qui visaient cette pièce (m1', m2', m3') et ne change rien d'autre. Elle est cependant **inscellable telle quelle** : la majeure M1' du tour 2 reste entière (amorce, devis et rapport n'ont pas de version neuve, la procédure décrit un comportement que l'amorce du dossier n'a pas). La v4 le déclare elle-même (statut, § 6). La conception tient (pas de `a_refaire`).

## 1. Fidélité des corrections (différentiel v3 → v4)

`diff` v3 → v4 : sept zones, toutes attendues, et toutes produites par le programme de couples. Contrôles faits :

- empreinte de la v3 = `e91a9020…` (celle exigée par le programme) ; chaque « ancien » du programme figure une fois dans la v3 ; la v4 est exactement la v3 passée aux huit couples (titre, statut, version, m1', m2', m3', trois couples de § 6) : le différentiel ne contient rien d'autre.
- **m1'** : appliqué, exact (« lue à 21:47Z : `396c4a0c…` » ; fait recoupé : tête de `main` = `396c4a0c…`, `14a0dfc5…` ancêtre).
- **m2'** : appliqué, exact (§ 2 point 3).
- **m3'** : appliqué, exact (geste 13, ligne 201) : les deux `test ! -e` sont en tête de la commande de recopie ; la commande se lit et se tape telle quelle (les `<run>` et `$R` sont substitués par l'opérateur comme dans le reste du geste).
- **M1', points 1 à 3** : hors de cette pièce, non appliqués, déclarés (§ 6). Constat : toujours absents du dossier (`ls`) : ni `amorce_jeu_idee_1_1_v2.sh`, ni devis v2, ni rapport v2, ni lanceur v2, ni sortie de répétition d'une amorce v2.
- **M1', point 4** : **refus motivé** par la v4 (les pièces neuves n'existent pas ; les nommer ferait citer des fichiers absents). Je juge le motif **recevable pour la v4 prise comme étape** (écrire une procédure qui nomme des fichiers absents serait pire), mais il ne peut pas valoir scellement : voir M1'' ci-dessous.

La phrase du tour 2 « supprimer ... une fois la dépendance levée » est bien gardée en attente : la v4 écrit (statut et § 6) qu'elle ne part pas au feu. Cohérent.

## 2. Corrections exigées

### Majeure

**M1''. La procédure v4 décrit une amorce qui n'existe pas ; la chaîne de pièces n'est pas livrée.** Faits vérifiés : l'amorce du dossier (`amorce_jeu_idee_1_1_v1.sh`, `ede38bb6…`) ne contient aucune reprise (0 occurrence de `reprise_sorties`) ; or le § 1 pas 7 de la v4 décrit « reprise toutes les 5 minutes jusqu'à 20 minutes avant l'échéance ... aucun « stopped » tant que les sorties ne sont pas poussées » et le geste 13 décrit « RESERVE : poussée des sorties impossible, ne rien détruire ». Avec l'amorce v1, une poussée qui échoue appelle l'arrêt en code 4 puis « stopped » : la machine attendrait sa destruction sans les sorties poussées, le comportement exact que M1 du tour 1 voulait écarter. Le devis v1 n'a toujours ni la ligne d'échéance (la v4 renvoie pourtant à « devis § 1 » au § 2 point 4), ni le pire cas au-delà de l'ordre de grandeur de 1 à 3 USD, ni le trafic réseau ; le rapport v1 présente encore D7 comme ouvert, alors que le § 2 point 2 de la v4 le dit tranché (GO-2026-11-16-10).

À livrer avant le feu, en fichiers neufs (R12), puis tour 4 (je rejouerai la répétition) :
1. `amorce_jeu_idee_1_1_v2.sh` portant la reprise, avec ses compagnons ; **un lanceur v2** (le lanceur v1 nomme l'amorce par son chemin et `controle-ligne` cherche `/root/amorce_jeu_idee_1_1_v1.sh` : la v4 le relève déjà) ; une répétition neuve avec les deux cas : poussée refusée trois fois puis acceptée (machine vivante, sorties poussées, aucun « stopped » avant) ; poussée jamais acceptée (reprises journalisées, arrêt en code 4 à l'échéance − 20 minutes, sorties intactes sur disque) ; sortie gardée et scellée.
2. `devis-machine-jeu-idee-1-1-v2.md` portant les couples 5, 11, 16, 17 du tour 1.
3. `rapport-machine-jeu-idee-1-1-v2.md` ne présentant plus D7 comme ouvert.
4. Procédure v5 appliquant les couples du tour 2 (point 4), dont les « ancien » suivants figurent chacun **une seule fois** dans la v4 (vérifié) :
   - `` `amorce_jeu_idee_1_1_v1.sh` (côté machine) `` → `` `amorce_jeu_idee_1_1_v2.sh` (côté machine) `` ;
   - `` `sortie-repetition-machine-jeu-idee-1-1-v1.txt` (sortie gardée : 110 cas, 0 écart) `` → nom et nombre de cas de la sortie de la répétition de l'amorce v2 ;
   - `` `devis-machine-jeu-idee-1-1-v1.md`, `rapport-machine-jeu-idee-1-1-v1.md`, et cette procédure. `` → `` `devis-machine-jeu-idee-1-1-v2.md`, `rapport-machine-jeu-idee-1-1-v2.md`, et cette procédure. `` ;
   - `` > /root/amorce_jeu_idee_1_1_v1.sh && bash /root/amorce_jeu_idee_1_1_v1.sh `` → le même avec le nom que le lanceur v2 aura écrit (à recopier du lanceur) ;
   - le passage du statut `` ne part pas au feu sans l'amorce v2, le devis v2, le rapport v2, la version suivante de cette\n  procédure qui les nomme et un tour 3 rendu `scellable` (§ 6) `` (une fois, avec sa coupure de ligne) → à supprimer quand la dépendance est levée ; la phrase « Cette version ne part donc pas au feu avec l'amorce v1 » figure **deux fois** dans la v4 (statut du § 6 et réponse point par point) : l'ancien d'un couple devra inclure assez de contexte pour être unique.

### Mineures

- **m1''. Contexte de § 2 point 3** : la v4 écrit « tour 3 rendu `scellable` », or ce tour 3 ne l'est pas ; la formule reste vraie comme condition, mais elle devra devenir « tour 4 » ou le numéro du dernier tour dans la v5. → ancien `` tour 3 rendu `scellable`. `` (fin du § 2 point 3 ; le même groupe de mots figure aussi au statut, ancien à allonger : `` Contre-lecture de cette procédure, de l'amorce et du devis par un lecteur neuf (R2), tour 3 rendu `scellable`. ``) → nouveau le même avec le numéro de tour valable à la v5.
- Aucune autre mineure.

### Remarques facultatives (aucune exigée)

- F2 et F4 du tour 1 (noms seulement au geste 8 ; ligne sur `None` au geste 9) : toujours ouvertes, déclarées.
- Pour mémoire : la sortie de répétition `...-rejeu-procedure-v4.txt` (21:53Z, du développeur) a le même contenu que la sortie gardée aux horodatages, chemins et identifiants près (110 cas) ; mon rejeu donne le même résultat. Ces sorties de rejeu ne prouvent rien de plus pour la reprise, l'amorce étant inchangée.

## 3. Points demandés, relus après corrections

1. **Tirages** : inchangé et tenu (versions `3.13.18 2.4.6 1.17.1` contrôlées avant tout clonage, même commit, même addendum, même commande).
2. **Gardes** : rejouées, 110 cas, 0 écart ; chacune a son cas sain et son artefact. Les corrections du tour 2 n'ont touché aucune garde. **La reprise de M1 reste non éprouvée** (pas d'amorce qui la porte).
3. **Clés, branche, poussées** : inchangé, tenu (cas des clés factices passés dans ma répétition).
4. **Gestes** : m3' appliqué et tapable ; le piège du geste 13 (« RESERVE ») est décrit mais ne repose sur aucune amorce livrée (M1'').
5. **Devis** : arithmétique du tour 1 inchangée et juste ; lignes manquantes (M1'', point 2).
6. **Hors périmètre, identifiants** : rien de 7a, 7b, T0.6, T0.7 ; aucun identifiant de modèle dans la v4 (recherche faite).

## Points pour la mère

- **Rien ne part au feu avec cet ensemble.** Un rédacteur neuf doit livrer amorce v2, lanceur v2, répétition neuve, devis v2, rapport v2, puis procédure v5 ; contre-lecture au tour 4. Le travail restant est borné et déjà spécifié ci-dessus (couples du tour 2 et du tour 1).
- **La v4 est une étape honnête, pas une pièce défectueuse** : ce qu'elle écrit sur la reprise est la cible voulue ; ce qui manque est la livraison de l'amorce.
- **Restes de la liste du tour 1**, inchangés : minuterie 49 h 45 contre 48 h (à trancher, recommandation : accepter) ; réseau pendant le jeu (à faire dire par le feu) ; rappel programmé à l'échéance ; permission de la ligne neuve par Lazar ; renouvellement du jeton après la preuve de destruction (nœud de Lazar) ; ligne de GO « calcul » à inscrire (périmètre « idée 1.1 », `3.5 USD`, échéance 2026-11-22 au plus tôt) ; dossier à commiter ; `COMMIT` à relire au feu (la tête de `main` bouge).
- **Fichiers parasites** `/s.txt` et `/commande-coupee.txt` : constatés présents à la racine (listage), non touchés ; à effacer par une personne.

## Déclaration

- Rôle : contre-lecteur neuf (R2), lettre C ; aucune pièce modifiée ; aucun commit ; ce fichier est neuf.
- Accès extérieurs : un `git ls-remote origin main` en lecture seule (tête de `main`) ; la répétition n'utilise qu'un dépôt jouet local. Aucun appel au loueur, aucune machine, aucune dépense, aucune poussée. Aucune clé lue ou affichée ; le texte du verbe interdit n'a pas été tapé dans une commande.
- Lu : rien sous `diag/`, `runs/`, `donnees/` ; rien de `/home/user/jeu-idee-1-1-copie-v1` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque.
- Calcul : léger (une répétition d'environ 2 minutes 15, dossier du bloc-notes `rep-c3/`).
- Incidents de ma main : aucun.
