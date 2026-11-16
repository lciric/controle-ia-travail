# Contre-lecture de la procédure de la machine du jeu relancé de l'idée 1.1, tour 2 (v1)

- **Auteur** : contre-lecteur neuf (R2), lettre C. Il n'a écrit aucune pièce (pièces de la lettre A). Il est aussi l'auteur du rapport du tour 1.
- **Heures (UTC, `date -u`)** : de 21:45Z à 21:50Z environ.
- **Pièce jugée** : `procedure-machine-jeu-idee-1-1-v3.md` (empreinte lue dans son compagnon, vérifiée `OK`) ; les 15 compagnons du dossier : `OK`.
- **Lu en entier** : rapport du tour 1 ; procédure v3 ; `corriger_procedure_v2_vers_v3_v1.py` ; différentiel v1 → v3 (`diff`) ; amorce, devis, rapport, sortie de répétition de la v3.
- **Rejoué** : la répétition locale entière, dossier neuf du bloc-notes, 21:45:41Z à 21:47:50Z : **110 cas, 0 écart** (aucun appel au loueur, aucune machine, aucune dépense).
- **Recoupé** (lecture seule) : `origin/main` = `396c4a0c…` ; `14a0dfc5…` en est ancêtre ; GO-2026-11-16-09 et -10 présents à `registres/go.md` (échéance des deux : 2026-11-22) ; R-3016 et R-3017 présents ; addendum de relance scellé sous `prereg/`.

## Verdict : `corrections`

La procédure v3 applique fidèlement les couples qui la visent et ne change rien d'autre. Mais **l'ensemble n'est pas scellable** : la majeure M1 du tour 1 n'est corrigée que dans le texte de la procédure, pas dans l'amorce qu'elle décrit, et la majeure M2 renvoie à une ligne du devis qui n'existe pas encore. La conception tient (pas de `a_refaire`).

## 1. Fidélité des corrections (différentiel v1 → v3)

`diff` v1 → v3 : seules les zones attendues changent. Couple par couple, le « nouveau » est celui du rapport du tour 1, mot pour mot :

| Couple | Où | État |
|---|---|---|
| 3 (M1, § 1 pas 7) | reprise toutes les 5 minutes, 20 minutes avant l'échéance, aucun « stopped » | appliqué, exact |
| 4 (M1, geste 13) | « RESERVE : poussée des sorties impossible », rien détruire | appliqué, exact |
| 6 (M2, § 2 point 4) | échéance 2026-11-22 au plus tôt | appliqué, exact |
| 7, 8, 9, 10 (M3) | D7 tranché par GO-10, deux GO cités, addendum déjà scellé | appliqués, exacts |
| 12 (m1), 13 (m2), 14 (m3), 15 (m4), 18 (m7) | gestes 5, 13, 11, § 5, statut | appliqués, exacts |
| 1, 2 (M1, amorce) | `reprise_sorties` dans l'amorce | **non appliqués** : l'amorce v1 est inchangée (empreinte `ede38bb6…`, zéro occurrence de `reprise_sorties`) |
| 5, 11 (M2, devis) | ligne d'échéance, GO-10 | **non appliqués** : devis v1 inchangé |
| 16, 17 (m5, m6, devis) | pire cas au-delà de 1 à 3 USD ; trafic réseau | **non appliqués** |
| réécriture du rapport (M3) | D7 présenté comme ouvert | **non faite** : rapport v1 inchangé |

La v3 le dit elle-même (§ 6, « hors de cette pièce »). Conséquence : le texte de la procédure décrit un comportement de l'amorce (reprise des poussées machine vivante, ligne « RESERVE : poussée des sorties impossible ») que l'amorce v1 n'a pas. Je l'ai vérifié : la seule ligne « RESERVE » de l'amorce v1 concerne des fichiers hors dossiers ou des compagnons faux ; la poussée qui échoue appelle toujours `arret … 4`, donc « stopped ».

La v2 → v3 (programme `corriger_procedure_v2_vers_v3_v1.py`) ne change que le titre, le statut, la ligne de version, deux mots « cette version » et le fait de la tête de `main` : conforme à sa déclaration.

## 2. Corrections exigées

### Majeures

**M1'. L'amorce, le devis, le rapport et la liste des pièces n'ont pas suivi : la procédure décrit une amorce qui n'existe pas.** À livrer (fichiers neufs, R12) avant le feu :
1. `amorce_jeu_idee_1_1_v2.sh` portant la reprise (couples 1 et 2 du tour 1) ; ses compagnons ; ajouter à la répétition (version neuve) les deux cas exigés (poussée refusée trois fois puis acceptée : machine vivante, sorties poussées, aucun « stopped » avant ; poussée jamais acceptée : reprises journalisées, arrêt en code 4 à l'échéance − 20 minutes, sorties intactes sur le disque) ; sortie de répétition gardée et scellée ; je la rejouerai au tour 3. Le lanceur contient l'empreinte de l'amorce (contrôle de la ligne) : il faudra un lanceur v2 si cette empreinte y est figée.
2. `devis-machine-jeu-idee-1-1-v2.md` portant les couples 5, 11, 16, 17 (échéance de la ligne de GO, GO-10, pire cas au-delà de 1 à 3 USD, trafic réseau) ; sans la ligne d'échéance, « devis § 1 » (§ 2 point 4 de la procédure) renvoie à rien.
3. `rapport-machine-jeu-idee-1-1-v2.md` dont le verdict et le § 5 point 1 ne présentent plus D7 comme ouvert.
4. Procédure v4, qui nomme les pièces neuves. Couples (chaque « ancien » figure une fois dans la v3, vérifié) :
   - ancien `` `amorce_jeu_idee_1_1_v1.sh` (côté machine) `` → nouveau `` `amorce_jeu_idee_1_1_v2.sh` (côté machine) `` ;
   - ancien `` `sortie-repetition-machine-jeu-idee-1-1-v1.txt` (sortie gardée : 110 cas, 0 écart) `` → nouveau le nom et le nombre de cas de la sortie de la répétition de l'amorce v2 ;
   - ancien `` `devis-machine-jeu-idee-1-1-v1.md`, `rapport-machine-jeu-idee-1-1-v1.md`, et cette procédure. `` → nouveau `` `devis-machine-jeu-idee-1-1-v2.md`, `rapport-machine-jeu-idee-1-1-v2.md`, et cette procédure. `` ;
   - ancien `` > /root/amorce_jeu_idee_1_1_v1.sh && bash /root/amorce_jeu_idee_1_1_v1.sh `` (geste 6) → nouveau le même avec `v2` (le nom exact est celui que l'amorce v2 aura ; la forme du texte ci-dessus est à recopier du lanceur).
   - supprimer de la v4 la phrase « Cette version ne part donc pas au feu avec l'amorce v1 » une fois la dépendance levée, et l'écrire en réponse au tour 2.

### Mineures

**m1'. « 21:3xZ » (§ 2 point 1)** : valeur gardée telle quelle du rapport du tour 1, alors que la v3 donne la tête lue à 21:42Z (`396c4a0c…`). → ancien `ancêtre de la tête de `main` à 21:3xZ` → nouveau `ancêtre de la tête de `main` lue à 21:47Z : `396c4a0c…``.

**m2'. § 2 point 3 (« corrections faites »)** : devient faux tant que M1' n'est pas levée, et vrai seulement après le tour 3. → ancien `Contre-lecture de cette procédure et du devis par un lecteur neuf (R2), corrections faites.` → nouveau `Contre-lecture de cette procédure, de l'amorce et du devis par un lecteur neuf (R2), tour 3 rendu `scellable`.`

**m3'. Ordre du fetch au geste 13** : le texte met le `fetch` dans une parenthèse après la commande `git archive … | tar`. Le sens est « après » le fetch, ce qui se lit bien, mais « refuser si l'un des deux dossiers existe déjà » n'a pas de commande. Facultatif d'ajouter `test ! -e $R/runs/<run> && test ! -e $R/diag/organisme-idees-juge-v1/<run> &&` en tête. Je le classe en mineure parce que c'est un geste tapé tel quel par l'opérateur.

### Remarques facultatives (aucune exigée)

- F2 et F4 du tour 1 (noms seulement au geste 8 ; ligne sur `None` au geste 9) restent ouvertes ; déclarées comme telles par la v3.
- Si l'amorce v2 allonge le temps de vie de la machine après la fin du jeu, ajouter au devis le surcoût de la reprise (au plus 20 minutes avant l'échéance, donc rien ajouté au pire cas de 3,30 USD).

## 3. Points demandés, relus après corrections

1. **Tirages** : tenu (inchangé : versions `3.13.18 2.4.6 1.17.1` contrôlées avant tout clonage, même commit, même addendum, même commande).
2. **Gardes** : rejouées, 110 cas, 0 écart ; chacune a son cas sain et son artefact. Rien dans les corrections du tour 1 n'a touché les gardes. **La reprise de M1 n'est pas éprouvée**, faute d'amorce.
3. **Clés, branche, poussées** : inchangé, tenu. Le texte neuf de § 5 (poussées horaires déclarées, texte scellé l. 629) est exact.
4. **Gestes** : m1, m2, m3 appliqués, tapables (m3' en facultatif). La destruction par identifiant et le témoin sont intacts.
5. **Devis** : arithmétique du tour 1 inchangée et juste ; mais devis v1 sans échéance de GO, sans la mention du dépassement de l'ordre de grandeur de 1 à 3 USD (pire cas 3,24 à 3,30 USD), sans le trafic réseau. Il faut le devis v2 (M1' point 2).
6. **Hors périmètre, identifiants** : rien de 7a, 7b, T0.6, T0.7 ; aucun identifiant de modèle dans la v3.

## Points pour la mère

- **Rien ne part au feu avec cet ensemble** : il manque l'amorce v2 (avec ses deux cas de répétition), le devis v2, le rapport v2, la procédure v4 et un tour 3. Tout se fait par un rédacteur neuf avec le rapport du tour 1 ; je rejouerai la répétition.
- **Reste de la liste du tour 1**, inchangée : P1 (minuterie 49 h 45 contre 48 h : à trancher, recommandation accepter) ; P2 (réseau pendant le jeu : à faire dire par le feu) ; P3 (rappel programmé à l'échéance) ; P4 (permission de la ligne neuve par Lazar) ; P5 (renouveler le jeton après la preuve de destruction : nœud de Lazar) ; P6 (ligne de GO « calcul » à inscrire : périmètre « idée 1.1 », `3.5 USD`, échéance 2026-11-22 ; dossier à commiter ; `COMMIT` à relire).
- **Fichiers parasites** `/s.txt` et `/commande-coupee.txt` : toujours à effacer par une personne (non touchés ici).
- La tête de `main` bouge ; `COMMIT` se relit au feu.

## Déclaration

- Rôle : contre-lecteur neuf (R2), lettre C ; aucune pièce modifiée ; aucun commit ; ce fichier est neuf.
- Accès extérieurs : aucun (le dépôt distant jouet de la répétition est local ; la répétition fait un `ls-remote` en lecture seule, comme au tour 1). Aucun appel au loueur, aucune machine, aucune dépense, aucune poussée. Aucune clé lue ou affichée ; le texte du verbe interdit n'a pas été tapé.
- Lu : rien sous `diag/`, `runs/`, `donnees/` ; rien de `/home/user/jeu-idee-1-1-copie-v1` ; rien de 7a, 7b, T0.6, T0.7, P3-bis, du bras d'attaque.
- Calcul : léger (une répétition de ≈ 2 minutes, dossier du bloc-notes `rep-c2/`).
- Incidents de ma main : aucun (la commande de répétition a dépassé le délai de 120 s du premier plan et est passée en arrière-plan ; elle s'est terminée seule, code 0, sans processus resté vivant).
