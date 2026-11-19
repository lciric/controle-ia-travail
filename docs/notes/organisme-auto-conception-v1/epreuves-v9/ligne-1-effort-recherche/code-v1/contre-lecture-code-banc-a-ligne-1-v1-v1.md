# Contre-lecture du code du banc A de la ligne 1 (épreuves v9, effort de recherche compté dans le seuil) — v1, compte rendu recopié

**Provenance.** Le contre-lecteur s'est arrêté au premier refus d'un outil, comme sa consigne le demandait, et n'a pas écrit son fichier. Ce texte est son compte rendu final, recopié tel quel par la session du compte organisme (2026-11-19, vers 15:40Z), sans rien changer au fond ; seuls les titres de section sont ajoutés. Le refus : la garde R10 du dépôt (`.claude/hooks/garde_calcul.py`) a bloqué une commande de recherche de texte dont le motif contenait un arrêt de processus par motif ; aucun processus n'était visé. Faux positif probable de la garde, non éprouvé par la session, qui ne rejoue pas la commande refusée. Partie non faite : la recherche systématique de motifs dangereux dans le code.

Contre-lecteur : modèle S, choisi parce que la seule place du modèle K sur ce compte est prise et que son autre version tire sur la même limite d'usage ; ce n'est pas un refus. Le code est écrit par le modèle L′ ; la mère en a été avertie et l'accepte (pièce de code, classe B).

## Verdict

Conforme après corrections.

## 1. Empreintes

- Toutes les empreintes compagnons du dossier de la ligne 1 sont conformes (aucun écart relevé).
- Le préenregistrement v5 a l'empreinte 523adfd7…0fb9. La version scellée sur main, comparée par `git show`, a la même empreinte, octet pour octet.

## 2. Essais rejoués

- Le fichier memoire_v53.py du commit a41b7b50 est absent de ce compte. Les 8 autres fichiers de l'organisme ont les empreintes attendues, d'après une copie du commit 94bfd92 sous docs/notes/organisme-courbe-dose-reponse-v1/.
- Rejoué dans une copie du bloc-notes (dépôt `git init` à part, rien d'écrit dans le dépôt), avec un substitut écrit par le contre-lecteur de `bardeaux` et `jaccard` (ensembles de suites de trois mots, rapport d'intersection à l'union). L'empreinte de ce substitut est portée dans la copie de la configuration.
- Résultat : 41 essais passés, 1 échoué, sur 42. Le seul échec est `test_essai11_texte_et_memoire`, à la ligne `monkeypatch.setattr(B.MEM, "Memoire", …)` : le substitut n'a ni la classe `Memoire` ni `texte_fiche`. Artefact du substitut, pas une faute du code.
- Les similarités écrites d'avance de l'essai 11 (8/10, 7/11, 6/12, 4/6) passent avec le substitut.
- L'interception de la voie écartée (`Memoire`, `texte_fiche`, `normaliser_texte` jamais appelées) n'est donc pas vérifiée. À rejouer avec le vrai fichier.

## 3. Fidélité au préenregistrement

Aucun écart de fond trouvé sur : monde planté, rôles permutés, textes de cartes, étages amont (une seule voie bardeaux/jaccard, liste par lignée, seuil 0,6 avec 1e-12), bras a, a′, b, c, d, T0, d-E1 à d-E3, deux vérités, M1 à M5, D1, table de lecture (7 lignes), prédictions P1 à P11, étalonnage (forces, grille, T0 seul, portes), audit (trois traits, deux étiquettes, intervalles à 95 %, portes lues sur intervalles, régression pair/impair), gardes A1 à A17, A13 par identifiant de processus (R10).

- Graines R9 : `graine_de_tache` de l'organisme, avec une racine par étape. L'horodatage de première dérivation est consigné, A14 est vérifiée dans le lanceur.
- Aucune lecture de résultat décisif. Une observation : le rapport (§ 5) dit avoir relu, sur deux courses d'essai à paramètres non étalonnés, des comptes de refus et « 1,94 contre 2,0 » cartes jugées par appel. C'est une quantité de porte sur la racine des essais, sans choix modifié. À consigner comme telle ; toute modification du code motivée par ce chiffre serait un réglage a posteriori.
- La fumée a calculé ses propres portes et sa table sur des racines disjointes. Elle n'imprime que des durées, tailles, comptes et sceaux.

## Corrections (numérotées)

1. etalonnage_ligne1_v1.py, `nettoyer_partiels` (ligne ~140-143, appelée par `jouer_courses`) : l'`os.remove` efface les fichiers `.partiel` d'une course interrompue. CLAUDE.md « récupérer ce qui est récupérable » et R-3851 interdisent d'effacer une sortie de course avant versement. Déplacer vers un dossier `partiels-recuperes/`, inventorié dans le manifeste, au lieu d'effacer. La commande de lancement (code-v1/commande-lancement-banc-a-ligne1-v1.md, « Suivi, reprise ») dit « effacés » : à corriger aussi.
2. etalonnage_ligne1_v1.py, `etalonner` (ligne ~330, branche « sortie déjà présente ») : une reprise renvoie la sortie scellée sans appeler `exiger_portes`. Si une porte était manquée, `etalonner` rend le code 0 en silence. La course décisive refuse ensuite, mais avec un message trompeur. Appeler `exiger_portes` aussi dans cette branche (repli silencieux, R5).
3. etalonnage_ligne1_v1.py, `dichotomie` (ligne ~46-60) : quand la garde A9 tire (cible manquée en 10 pas), la liste des pas n'est écrite nulle part. Écrire un fichier scellé des pas avant de lever l'exception (récupération).
4. essais/test_banc_ligne1_v1.py, `test_essai02…` (dernière boucle, ~lignes 82-86) : « d rend les décisions de a′ quand m_r = m_s » compare deux appels identiques `regle_e_bh(cartes, 0.05/6, m, m)`. Tautologie, qui ne teste ni `jouer_bras("d")` ni `jouer_bras("a_prime")`. Le réécrire sur une course où tous les essais sont jugés, ou sur une sortie pleine fabriquée, en comparant les promotions des deux bras.
5. R5 : des gardes ajoutées par le développeur (rapport § 4.17) n'ont aucun essai sain/artefact : `DecisionMereRequise` (part d'indéterminées > 20 % à la sortie de l'étalonnage), `exiger_code_commis`, refus de la course décisive si une porte est manquée ou si le code ou la configuration diffèrent de ceux de l'étalonnage, refus des racines différentes de celles du préenregistrement (`preparer`), refus d'écraser (`FileExistsError`), chemin de reprise (`course_deja_faite`, `nettoyer_partiels`). Ajouter ces essais, ou retirer ces gardes (silence comblé).
6. lancer_ligne1_v1.py, `empaqueter` (manifeste du dépôt, ligne ~295) : R-3851 demande « noms, tailles, empreintes des morceaux et du tout ». Le manifeste porte les morceaux et chaque membre, mais pas d'empreinte du tout. Ajouter une empreinte d'ensemble (par exemple celle de la liste triée des membres et de leurs empreintes).
7. lancer_ligne1_v1.py, `decisive` (ligne ~213-226) et etalonnage_ligne1_v1.py (`sortie` de `etalonner`, ligne ~395) : R9 demande les versions dans le manifeste par run. La sortie de l'étalonnage n'a ni version de Python ni de numpy, ni commit de l'organisme. Les ajouter.

## Recommandations, non bloquantes

- (a) `rejouer_journal` ne vérifie pas que le `m` de la décision de promotion est celui que la décision de registre a calculé pour la définition donnée. De plus, personne ne confronte la sortie brute (lue par l'analyse) aux promotions du journal. Ajouter ce recoupement dans le rejeu.
- (b) Marge du dépôt : environ 400 Mo contre le plafond de 500 Mo, soit 20 %. Les 155 Mo d'étalonnage peuvent aller hors dépôt, au choix de la mère.

## Avis sur les cinq choix (le préenregistrement ne les fixe pas ; le contre-lecteur ne tranche pas)

- 4.1 Largeur du texte : garder `%+.2f` (littéral du préenregistrement : « +0.00 »), longueurs rapportées sans arrêt. Un format à largeur fixe contredirait la chaîne « +0.00 ». La similarité se calcule mot à mot, donc la largeur ne change pas les bardeaux, et la longueur n'est pas auditée. Mettre en tête de la sortie de l'étalonnage tout écart de longueur par type. Confiance 0,8.
- 4.2 Confiance des lois tranchantes, (1−c)/2 sur chacune des deux autres issues : garder. Cela suit la forme [0,75 ; 0,125 ; 0,125] du chronométrage de l'annexe B, et aucune autre répartition n'est plus naturelle. Confiance 0,85.
- 4.3 Marginale de la tranche : garder les fréquences brutes, littéral de « marginale empirique de la tranche ». Le lissage à 0,5 reste dans la seule statistique du test de mort. Le risque d'une fréquence nulle est négligeable (de l'ordre de 1e-8 par lignée). Confiance 0,85.
- 4.4 Niveau du bras c dans la graine : garder 0,05/6. Alors `promue` de l'engagement de confirmation coïncide avec la décision (log(6/0,05)). La trajectoire ne dépend pas du niveau, seule la graine en dépend, et la validité n'est pas touchée. Dire dans l'addendum que ce niveau entre dans la graine. Confiance 0,7.
- 4.5 Cartes indéterminées de l'audit : les garder hors des aires de l'étiquette d'effet (vraie contre fausse), dans la table croisée, comme le fait le code ; calculer en plus, rapportée sans porte, la convention où elles comptent comme non vraies, par symétrie avec les deux conventions de M3. Confiance 0,65.
- Porte A15 (écart de cartes jugées par appel, 1,94 contre 2,0 sur deux courses d'essai) : le calcul de refus dit que l'écart vient surtout de la classe « peu ». Il y faut deux variantes à même seuil arrondi et même issue pour la mémoire, ou une paire dérivée pour la règle « affinage », donc quelques pour cent. Estimation actuelle 0,06 ± 0,02 environ, paramètres non étalonnés. Risque de tirer la porte faible (de l'ordre de 1 à 5 % : estimation non opposable). Recommandation : garder la porte telle quelle (littérale). Si elle tire, c'est un arrêt, puis un écart au préenregistrement scellé, donc un nœud de Lazar : aucun relâchement a posteriori. Écrire dans l'addendum, avant l'étalonnage, ce que la mère fait si elle tire : retour à Lazar, avec la décomposition des refus par étage et par rôle, que l'étalonnage rapporte déjà. Confiance 0,7.

## Ce qui n'a pas été fait

Essais rejoués : 41 passés, 1 échoué sur 42 (échec dû au substitut de memoire_v53). Aucun étalonnage, aucune course décisive, jamais `--reel`. Aucun réseau, aucune écriture dans le dépôt, aucune lecture de clé ni de dossier interdit. Non fait : recherche systématique de motifs dangereux dans le code (arrêtée au refus) ; essai 11 avec le vrai memoire_v53.py.
