# Contre-lecture du code de la course — organisme retenu du saboteur à budget, v5 (cl1)

Date : 2026-11-22. Classe B. Contre-lecteur : Claude Opus 5.5, neuf (auteur d'aucune de ces pièces). Rien poussé, aucune dépense, aucun loueur, aucun modèle externe. Aucune pièce interdite ouverte : ni consigne privée, ni branche d'essai, ni résultat de mesure, ni pièce côté sondes.

## Verdict

**Course autorisable après corrections.** Le code ne porte aucun bloquant. Il reste trois corrections à faire (M1, m1, m2), puis ma vérification courte. Deux nœuds sont à trancher par l'ordre ou par Lazar avant la création : la course sur une machine neuve (C1), et la confirmation du mot sur la première action « gardée ».

## Ce qui a été vérifié

- **Base et arbres.**
  - `git log c97231b38..HEAD` de `p1` rend les quatre correctifs, puis 0018.
  - Mon worktree neutre `scratchpad/cl-p1` part de `c97231b38` et reçoit par `git am` les correctifs 0014 à 0017. Son arbre vaut `1b395646c2df70bf8181290fcf24ca38cd5a4f40`, comme annoncé.
  - Avec 0018 en plus, son arbre vaut `93b4e384ebd6b20e05cfec5c00819b539aecfbb0`, comme annoncé.
  - Les sceaux des pièces sous `registres/iib-executante/p1-code-course-v1/` sont conformes.
- **Essais rejoués dans mon worktree.**
  - Liste figée v6 à la tête 0017 : **288 passed** (10 min 14 s).
  - Essai du moteur à torch (torch 2.14.1, transformers 5.18.0, scipy 1.17.1, dans un environnement à part du bloc-notes) : **2 passed**.
  - Liste de la course à la tête 0018 (arbre `93b4e384…`), torch compris : **292 passed** (10 min 38 s). La liste v6 y est entière, donc ses 290 essais aussi.
- **Poussée par lot (0014), conforme.**
  - Après le sceau, le vrai script de consignation est appelé. La branche distante est ensuite vérifiée par le lanceur lui-même : fichiers suivis, fichiers propres, tête égale à `refs/remotes/origin/<branche>`. Le clonage est complet et non limité à une branche, donc la référence suivie se met à jour à la poussée.
  - Un refus donne une marque de progrès, une ligne sur la sortie d'erreur et une entrée au journal du résumé ou de l'arrêt.
  - Trois refus de suite lèvent `GardeArret`. L'amorce écrit alors `arret.json`, consigne, puis met la machine à l'état « stopped » par son identifiant, disque gardé.
  - Un délai dépassé arrête le groupe du script par `killpg` sur son identifiant (R10).
  - Aucun secret n'est imprimé : la sortie standard part dans DEVNULL, et les erreurs de git vont dans des fichiers.
  - Cas sain et artefacts éprouvés (R5) : origine qui refuse, script qui rend 0 sans pousser, délai dépassé, mode réel sans script.
- **Course (0015 à 0017), conforme au texte scellé.**
  - Rien n'est changé dans les tours, le tour de contrôle, s(R), la cible, le minimum, la règle, la distillation ni l'évaluation : `tours_v5`, `regle_v5` et `distillation_v5` ne sont pas touchés.
  - L'oracle est relu sur la désignation scellée, et les conditions ne sont pas rejouées.
  - Une configuration différente de celle du manifeste de l'étalonnage est refusée.
  - Un mode réel sans distillateur ou sans poussée est refusé.
  - Les gardes levées dans un tour se propagent (aucun `except` dans `boucle_des_tours`).
  - Aucun texte dans les tours (`exiger_aucun_texte`).
  - Aucun score de moniteur, aucune moyenne ni médiane sur les jetons.
  - Les replis sont écrits (0016).
  - L'amorce de la course diffère de celle de l'étalonnage par les cinq changements déclarés et par eux seuls (`diff`). Le clonage prend `diag/*-iib-*/`, `runs/*-iib-*/` et `donnees/*-iib-*/`.
  - `IIB_AMORCE` n'admet que deux valeurs.
- **Graines (R9).** À la tête 0017, j'ai relevé sur la course jouet 6 735 clés d'étalonnage, 5 219 clés de course et 5 clés de distillation, sans aucune clé commune. Le correctif 0018 suit la section 14 à la lettre (préfixe `…course/`, même entropie), avec une garde avant le premier tour. Lu : conforme.

## Bloquants

Aucun.

## Majeurs

**M1 — le second passage de la course n'est refusé que sur le même disque.**
- `exiger_course_non_jouee` lit `diag/<étalonnage>/tours|evaluation` dans la copie locale.
- Une machine neuve clone `COMMIT`, qui ne porte pas les sorties poussées sur la branche d'essai. Sous une branche neuve, elle rejouerait donc la course entière.
- Même sur le même disque, une course morte avant l'écriture du premier tour peut être relancée.
- **Correction exacte.**
  1. Dans `_executer_course`, avant le premier tour, écrire et sceller `diag/<étalonnage>/course-engagee-iib-v5.json` (run, instant), le pousser par `versement`, et faire refuser `exiger_course_non_jouee` s'il existe.
  2. Dans `amorce_instance_iib_course_v5.sh`, juste après le calcul de `RUN_ETAL` :
     - faire `git ls-remote --exit-code origin "refs/heads/essai/iib-course-engagee-$RUN_ETAL"` ; un code 0 vaut refus ;
     - puis pousser cette référence (`git push origin HEAD:refs/heads/essai/iib-course-engagee-$RUN_ETAL`) avant l'installation ;
     - écrire un essai pour le cas sain (référence absente) et un pour l'artefact (référence présente : refus).

## Mineurs

- **m1 — identifiants de l'étalonnage absents ou incomplets en mode réel.** Ils donnent aujourd'hui « faux positifs non calculés », écrit mais non refusé. **Correction** : dans `_executer_course`, en mode réel, refuser si `len(ids)` diffère de `lots` dans `diag/<étalonnage>/resume.json` (attendu 28), ou s'il vaut 0.
- **m2 — délai de la consignation trop court.** `DELAI_CONSIGNATION_S = 3000` est sous le pire du script, environ 3 375 s (verrou 1 500, trois poussées de 600, attentes 15 + 60). **Correction** : 3 600 s.
- **m3 — saut dans l'essai neuf de 0018.** `test_prefixe_de_la_course_artefacts` contient un `pytest.skip`. Un saut ferait refuser la ligne « N passed » de l'amorce. **Correction** : `assert course["conditions"]["issue"] in ("N", "P")`.
- **m4 — coût de la seconde location dans le rapport.** Le rapport écrit « environ 2 USD ». Le devis (l. 55, [L56] [L57]) dit environ 2,0 USD, et **environ 6,5 au pire**. L'ordre doit citer les deux chiffres.

## Points ouverts du développeur

1. **Moteur à torch** : joué sur processeur par le développeur et par moi (2 passed). Il reste à le jouer sur carte, aux premières minutes de la machine, par la liste de la course. **Non bloquant.** `TESTS_ATTENDUS=292` pour la liste de la course, 290 pour la liste v6.
2. **C1, une ou deux machines** : le devis compte une seule location, et le code demande une machine neuve. C'est un écart au devis, couvert par la réserve de 10 USD et sous le plafond. **Bloquant pour l'ordre, pas pour le code.** Il faut le mot de Lazar. Recommandation : machine neuve ; détruire celle de l'étalonnage après le rapatriement vérifié ; porter `IIB_DEPENSE_ANTERIEURE_USD` à la dépense de l'étalonnage plus le stockage à l'arrêt.
3. **C2, accord** : GO-2026-11-21-70 couvre « étalonnage puis course », plafond 60 USD cumulé. Le même `go_id` est juste. **Pas un nœud.**
4. **Dernier jour de création, le 26/11** (création exclue à partir du 2026-11-27T00:00Z) : c'est une borne de calendrier, pas un défaut du code.
5. **Préfixe propre** : levé par 0018. Rien n'avait encore été tiré pour la course, donc changer le préfixe ne déplace aucune mesure. **Non bloquant.**
6. **Première action « gardée »** : R-4708 la dit appliquée sous GO-2026-11-21-69 « sans réponse ». C'est un nœud de conception. **Un mot explicite de Lazar** est recommandé avant le scellement de l'ordre de la course. Non bloquant pour le code.
