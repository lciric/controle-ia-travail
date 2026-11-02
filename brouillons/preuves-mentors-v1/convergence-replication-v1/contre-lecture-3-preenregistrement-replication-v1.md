# Contre-lecture 3 (R2) du préenregistrement de réplication sur graine neuve de la course de convergence des règles de défense — brouillon 3, sur les différences du brouillon 2 au brouillon 3 — rapport v1

**Verdict : scellable après corrections mineures (listées) — 5 remarques « CL3-nn » au § 3 (2 obligatoires : CL3-01 et CL3-02 ; 3 recommandées : CL3-03 à CL3-05). Aucune ne touche une hypothèse, une prédiction, une confiance, une métrique, un seuil, une table, la spécification v2, le code v3, ses essais ou l'implémentation B v2.** Les 13 remarques de la contre-lecture 2 sont appliquées fidèlement, le diff ne contient aucun autre changement de fond, les écarts d'auteur sont justes ; le défaut qui reste est hérité des brouillons précédents et hors du diff : la condition de départ sur la charge de la machine est ambiguë (CL3-01).

- Contre-lecteur : sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`). Même modèle que l'implémentation B et que l'auteur de la contre-lecture 1, instance distincte : je n'ai écrit ni ce texte, ni la spécification, ni le code v3, ni B, ni les contre-lectures 1 et 2.
- Date : 2 novembre 2026, ≈ 00:50 à 01:10 UTC. Aucun fichier existant modifié, aucun réseau, aucun commit, aucune clé lue, aucune ref `donnees/*`. Seul fichier créé dans le dépôt : celui-ci (son compagnon `.sha256` est à écrire par la session, § 5). Calculs sous `nice -n 10`, interpréteur sans écriture de bytecode (`-B`), copies jetables dans le dossier temporaire de la session, supprimées.
- **Rien de ce qui est interdit à cette contre-lecture n'a été fait** : la course n'a pas été lancée ; aucune racine n'a été dérivée (ni du brouillon 3, ni d'une variante, ni d'un texte synthétique) ; `sceller` n'a jamais été appelé ; aucun essai lent ; l'autorisation de décision du code v3 est restée vide (`{'prereg_sha256': None, 'racines': None}` relevé après mes appels).
- Objet : `preenregistrement-replication-convergence-v1-brouillon3.md` (461 lignes, `73d2252ff2beec8e77eb1d6b33ab58c6b77c986b64cffdda23c7ce704f1ffbe1`), lu par son diff avec le brouillon 2 (`74c66bd38e5288c65128ffddcd08d5ba7442cde9797c8fb7b58308b01ae32a0d`) : `differences-brouillon2-brouillon3-replication-v1.diff` (`ecaf40a1534a088ac4ad66b73358108bfd1e72f6f9b6f981698d406cc666d8d8`, 13 blocs, lu en entier ; je l'ai régénéré par `diff -u` : identique hors la ligne d'en-tête horodatée), plus, en entier, les sections touchées, la Liste d'arrêt, les Issues écrites d'avance, les Rôles et la section Contre-lecture. Lus avec lui : la contre-lecture 2 (`121154a45bab67bc217988ac7fc0300448931cc9c22b3ae015fa80cde76f8b5d`, §§ 3 et 4 en entier), le rapport de rédaction (`5b0f27d9b367554417c742007ab75877e33ef1f04d1ea74f7707a5b5cf4fb61a`), les passages de code, d'essais, de rapport de validation de B et de registres que le brief désigne, `prereg.py` et `scellement.py`.
- Sigles : R2 = règle « contre-lecture par un lecteur neuf » ; R6 = règle « empreinte compagnon `.sha256` de chaque pièce » ; V0 = contrôle de plomberie du texte (clauses (a) à (l)) ; A = code de la course ; B = implémentation indépendante de la statistique ; E1 à E5 = les cinq fichiers d'entrée de B (résultats, manifeste, texte scellé, fichiers originaux, analyse de A).
- « CL2-nn » = remarque numéro nn de la contre-lecture 2 ; « CL3-nn » = remarque numéro nn de celle-ci. « Obligatoire » = à appliquer avant le scellement ; « recommandée » = à appliquer sauf raison écrite. Numéros de ligne : brouillon 3 (461 lignes).

## 1. En six lignes

1. **Fidélité.** Les 13 remarques de la contre-lecture 2 sont appliquées. Contrôle mécanique : chaque bloc de remplacement des §§ 3 et 4 de la contre-lecture 2 a été cherché dans le brouillon 3 ; sont exacts mot pour mot CL2-02 (3 blocs), CL2-03 (3), CL2-05 (5), CL2-06 (étapes 3 et 7), CL2-07 (titre et rôle de la contre-lecture 2), CL2-12, CL2-13 et trois des cinq marqueurs ; les autres ne diffèrent que par les ajouts déclarés (§ 6).
2. **Pas d'autre changement de fond.** Sur 13 blocs du diff, les seules lignes de tableau modifiées sont quatre lignes de la Liste d'arrêt (cellules « condition » ou « action ») ; aucune valeur de seuil, de prédiction, de confiance ni aucune table de lecture n'est touchée ; l'identité de code et de configuration n'a pas bougé (bloc d'identité régénéré par moi : égal au texte, hors la ligne de B écrite à la main).
3. **Titre et statut finals dès le brouillon 3 : acceptable**, aux conditions du § 2, point 3.
4. **Un défaut hérité à corriger** : la condition de départ sur la charge dit « consignation » dans sa colonne d'action, alors que V0 (a) et la ligne 1 de l'issue globale en feraient une cause de « non jugeable (plomberie) » sans reprise possible (CL3-01).
5. **Le reste est de la cohérence** : phrases « seule date et entrée » à corriger si des corrections sont appliquées (CL3-02) ; environnement du rejeu de deux tâches (CL3-03) ; « manifeste de réplication » à préciser car un autre existe sous `runs/` (CL3-04) ; rapport de rédaction cité sans chemin ni empreinte (CL3-05).
6. **Le validateur `prereg.problemes` est muet** sur une copie jetable où j'ai rempli les deux marqueurs (avec ou sans mes corrections) ; il refuse chacun des quatre oublis simulés (§ 4). La liste R6 est complète : 31 fichiers, 31 compagnons, `sha256sum -c` passe sur les 31 ; il faudra y ajouter ce rapport (§ 5).

## 2. Réponses aux sept points du brief

| # | Point | Verdict | Ce que j'ai trouvé |
|---|---|---|---|
| 1 | CL2-01 à CL2-13 appliquées fidèlement ; cinq écarts d'auteur justes | **conforme** | 13 sur 13 appliquées. Les écarts déclarés par le rédacteur sont tous justes, vérifiés dans le code et les pièces (§ 6). Deux détails non déclarés, bénins : CL2-10 écrit « croît avec l'information cherchée et n'est pas “28 min par graine” » là où la contre-lecture 2 écrivait « est proportionnel à … » (l'affirmation est plus faible, donc plus sûre) ; CL2-01 attribue à « son rapport » la suppression du script de mutations de la v1, que le rapport de B ne dit pas (le fichier n'existe plus sur disque : constaté). Aucune correction demandée. |
| 2 | Aucun autre changement de fond | **conforme** | Lecture des 13 blocs, plus comparaison mot à mot des lignes longues. Tout changement se rattache à une remarque CL2 ou à une mise à jour déclarée (horodatages de revérification, auteur du brouillon 3, déclaration (2) et (4), Plan 8 point 12, rôles). Aucune hypothèse, prédiction, confiance, métrique, aucun seuil (τ, z*, 0,001, G = 2, N = 100, S8), aucune table (R1, R0, R3, Rii, prédictions, issue globale) n'est modifié. La phrase nouvelle « Le brouillon 3 ne change aucune hypothèse … » (Déclaré (4)) est vraie. |
| 3 | « Titre et statut finals dès le brouillon 3 » | **acceptable** | Raisons : (a) le validateur ne voit ni le titre ni le statut ; les écrire au scellement aurait fait entrer dans les octets qui fixent les racines des passages jamais relus ; en les finalisant, la contre-lecture 3 les relit (titre identique au texte de CL2-07 ; statut identique, plus la mention de la contre-lecture 3). (b) Le risque d'un texte qui se dit « scellé » avant de l'être est couvert : la ligne « Date » porte encore « À REMPLIR », donc `problemes` refuse le scellement, et le nom du fichier dit « brouillon3 ». (c) Le brouillon 3, archivé, gardera un statut qui parle d'un texte scellé qu'il n'est pas : lecture trompeuse possible pour un tiers, sans conséquence pour la course ; je ne demande pas de correction. **Conditions** : au scellement, redire vraies les affirmations du statut (spécification v2, code v3, essais et B v2 inchangés depuis la contre-lecture 2 : vrai aujourd'hui, empreintes égales sur disque et dans le commit `6151e597` ; aucune racine dérivée ; aucun texte de la réplication de convergence sous `prereg/`, aucun manifeste sous `runs/`) ; et, si des corrections sont appliquées, remplacer les deux phrases « seule date et entrée » (CL3-02). |
| 4 | Contrôle V0 (l) (rejeu de deux tâches) exécutable tel qu'écrit, sans rien écrire sous `runs/` ni `diag/` | **exécutable, avec une précision** (CL3-03) | Vérifié par lecture du code, **non exécuté** (l'exécuter dérive des racines d'un texte scellé, interdit ici). Les noms existent avec les paramètres attendus : `autoriser_decision_regles(chemin, cfg, instances, lam, reference)` (code v3, l. 386-403) ; `executer_tache_regles(instance, code_delta, racine, racine_tenue, cfg, regles, lambdas, references, complete, serialiser)` (l. 695-739). Séquence valide : `autoriser_decision_regles(<texte scellé>, v4.CONFIG_V4, "0:100", 0.3, "moyenne")`, puis, pour i = 0 et 1, `executer_tache_regles(i, 1, ρ, ρ_t, v4.CONFIG_V4, REGLES, (0.3,), ("moyenne",), False, serialiser=True)`, (ρ, ρ_t) étant les racines posées par l'autorisation (égales à celles du manifeste par V0 (c)) ; c'est exactement ce que fait `_travail` en décision (l. 843-855). Rien n'est écrit : l'écriture de fichiers n'existe, dans le code v3 et dans l'arène v4, que dans `main` (modes essai et décision), `_consigner_pids` (pool) et `_ecrire_nouveau`, aucun sur le chemin de `executer_tache_regles`. « Comme E6 » est juste pour l'exécution (E6 pose l'autorisation à la main parce que les racines d'origine sont interdites ; le lecteur, lui, passe par `autoriser_decision_regles`). Champs « hors temps processeur » : `cpu_tache_s`, `cpu_trajectoire_s`, `cpu_final_s`, `cpu_s` (+ `version`), comme dans `sans_temps` des essais. Durée : le journal donne 11,5 s + 12,6 s de processeur pour ces deux tâches (journal, l. 476-481), soit de l'ordre de 30 s de mur avec le chargement : « ≈ 35 s de processeur » est un majorant sans conséquence. **Précision manquante** : l'environnement du rejeu n'est pas dit ; la course et E6 tournent avec `OMP_NUM_THREADS=1` ; sans lui, sur 2 cœurs, l'égalité au bit n'est pas garantie (CL3-03). |
| 5 | Liste R6 complète ; compagnon et `sha256sum -c` partout | **conforme** | `find … -type f ! -name '*.sha256' ! -path '*/__pycache__/*'` : 31 fichiers ; 31 compagnons, tous d'une ligne ; aucun orphelin ; aucun `__pycache__` ni cache de test ; `sha256sum -c` : 31 sur 31 « OK » ; `controle_ia.scellement.verifier` (format, nom de base, empreinte) : 31 sur 31 conformes. La liste du rapport de rédaction (26 fichiers) + les 5 pièces de B v2 déjà scellées = exactement les 31 fichiers, sans doublon ni manque. `git status --porcelain` sur le dossier : vide avant mon rapport (tout est commité). **À ajouter : ce rapport** (§ 5). Les 37 empreintes du brouillon 3 se rattachent toutes à une pièce : 32 à un compagnon scellé, 5 au bloc d'identité que j'ai régénéré (configuration et quatre fichiers de bibliothèque). |
| 6 | Deux marqueurs restants : forme exacte, contenu ; validateur muet après simulation sur copie jetable | **conforme** | Exactement deux occurrences de « À REMPLIR » (l. 9 et l. 461) et aucun gabarit `<<…>>`. Formes exactes et contenu : § 4. Simulation (copie dans le dossier temporaire de la session, hors du dépôt, supprimée ensuite : constaté) : état actuel → `['section vide ou à remplir : Contre-lecture']` ; marqueurs remplis → `[]`, avec ou sans mes corrections ; oublis simulés refusés (§ 4). |
| 7 | Condition « charge à une minute ≤ 1,0 » | **ambiguë ; à corriger** (CL3-01) | Voir ci-dessous. |

**Point 7 en détail — ce que le texte exige, et ce qui arrive sinon.** Le texte la dit en quatre endroits : S8 (l. 199), Plan 5 étape 5 (l. 260), Liste d'arrêt (l. 401), réponse à CL-08 (l. 438). Mot à mot, elle exige : (1) un relevé de `uptime` (première valeur, moyenne sur une minute) ≤ 1,0 « au départ », consigné — sans dire où, ni à quel instant exact (dans la copie propre à l'étape 5, ou juste avant l'étape 6), ni combien de relevés sont permis ; (2) « aucune autre tâche de calcul lancée pendant la course », c'est-à-dire pendant 28 min à plus d'une heure sur 2 cœurs que la course occupe déjà entièrement avec ses 2 processus ; ce second point ne peut pas être garanti par la session (S8 écrit lui-même que « la machine est partagée avec d'autres sessions »). Si elle n'est pas remplie : — **charge > 1,0 au départ** → colonne d'action « pas de départ ». Ni arrêt, ni écart, ni nœud de décision : la course n'a pas commencé et le texte n'est pas touché. Le texte ne dit pas si l'on peut attendre et relever à nouveau (rien ne l'interdit ; c'est la lecture naturelle) ni jusqu'à quand. — **autre tâche lancée pendant la course** → colonne d'action « consignation ». Mais V0 (a) exige « aucune condition de la liste d'arrêt » et la ligne 1 de l'issue globale rend « non jugeable (plomberie) » pour toute « condition d'arrêt » ; la note sous le tableau n'exempte que trois autres lignes (interdits de procédure). Lue à la lettre, la présence d'un test lancé par une autre session pendant la course rendrait donc la réplication non jugeable, sans reprise prévue (le Plan 7 ne traite que `timeout` et signal, et le texte exclut toute seconde course pour changer l'issue), pour une cause sans effet sur le calcul : racines, graines, résultat de chaque tâche et garde de 600 s de processeur ne dépendent pas de la charge ; seule la durée de mur en dépend, avec une marge ×4 (`timeout 7200`). Charges à une minute relevées aujourd'hui : 1,70 à 00:36 UTC (rapport de rédaction), 0,81 à 00:51, 0,24 à 01:01, 2,51 à 01:03 UTC (mes contrôles y contribuent, d'autres sessions aussi) : la condition est satisfiable, mais elle fluctue et il faudra des relevés répétés. La correction CL3-01 fixe la lecture (attente permise, autre tâche seulement consignée).

## 3. Corrections, avec texte de remplacement prêt à coller

Chaque chaîne « Remplacer » apparaît exactement une fois dans le brouillon 3 (vérifié par la simulation). Toutes ont été appliquées ensemble sur la copie jetable : le validateur est resté muet et la garde d'identité du code v3 (`exiger_identite_prereg_regles`, fonction pure) a accepté le texte obtenu.

### CL3-01 — Condition de départ sur la charge : lire « attente permise, autre tâche consignée » (point 7) — obligatoire

Constat : § 2, point 7. Ajouter, **après la ligne 414** (« Les lignes « Lecture d'un résultat de la réplication avant scellement » … non des gardes de code au sens de R5. »), un paragraphe, et pointer vers lui depuis S8 et l'étape 5.

Paragraphe à ajouter après la ligne 414 (séparé par une ligne vide) :

```text
**Ligne « Charge à une minute > 1,0 au départ, ou autre tâche de calcul lancée pendant la course »** : condition de procédure sans effet sur le calcul — les racines, les graines, le résultat de chaque tâche et la garde de 600 s de processeur ne dépendent pas de la charge ; seule la durée de mur en dépend (d'où la marge de `timeout 7200`). Lecture fixée. (a) **Au départ** : le relevé `uptime` (première valeur, moyenne sur une minute), pris dans la copie propre immédiatement avant la commande du Plan 5, étape 6, doit être ≤ 1,0 ; sinon la course n'est pas lancée (« pas de départ ») ; attendre et relever à nouveau est permis, sans limite de durée ni de nombre de relevés, et n'est ni un écart au préenregistrement ni un nœud de décision ; chaque relevé est consigné. (b) **Pendant la course** : une tâche de calcul lancée par une autre session est consignée (relevé de `uptime` et des tâches actives à la fin de la course) et n'a aucun effet sur la lisibilité : elle ne rend fausse ni V0 (a), ni vraie la ligne 1 de l'issue globale ; seuls ses effets éventuels sur `timeout 7200` ou sur la garde de processeur sont traités à leur propre ligne.
```

S8 (ligne 199) :

Remplacer

```text
relevée par `uptime` et consignée, et aucune autre tâche de calcul lancée pendant la course.
```

par

```text
relevée par `uptime` et consignée, et aucune autre tâche de calcul lancée pendant la course (lecture fixée dans la note sous le tableau de la Liste d'arrêt).
```

Plan 5, étape 5 (ligne 260) :

Remplacer

```text
`uptime` : charge à une minute ≤ 1,0, consignée ; aucune autre tâche de calcul lancée pendant la course.
```

par

```text
`uptime` : charge à une minute ≤ 1,0, consignée ; aucune autre tâche de calcul lancée pendant la course (lecture fixée dans la note sous le tableau de la Liste d'arrêt).
```

Si la session préfère la lecture stricte (toute tâche concurrente rend la course non jugeable), il faut l'écrire en toutes lettres et prévoir de quoi la faire respecter (annonce aux autres sessions, verrou) ; je le déconseille : la lecture stricte fait dépendre une réplication de 28 minutes de ce que d'autres sessions lancent pendant ce temps, sans aucun effet sur le résultat.

### CL3-02 — Phrases « seule date et entrée » : à aligner si des corrections sont appliquées — obligatoire (conséquence)

Constat : le Plan 5 étape 4 (l. 259) dit que le brouillon 3 est « complété de la seule date de scellement … et de l'entrée « Contre-lecture 3 » », et le traitement de CL2-07 (l. 453) dit « il ne reste à écrire que la date de scellement et l'entrée ». Ces deux phrases deviennent fausses dès qu'une correction de la présente contre-lecture est appliquée ; elles figureraient dans le texte scellé. (Sans objet si la session refuse toutes les autres corrections ; l'entrée du § 4 doit alors le dire.)

Plan 5, étape 4 (ligne 259) :

Remplacer

```text
complété de la seule date de scellement (relevée par `date -u`) et de l'entrée « Contre-lecture 3 », est écrit sous
```

par

```text
complété de la date de scellement (relevée par `date -u`), de l'entrée « Contre-lecture 3 » et des corrections qu'elle demande (traitées une à une dans cette entrée), est écrit sous
```

Traitement de CL2-07 (ligne 453) :

Remplacer

```text
il ne reste à écrire que la date de scellement et l'entrée « Contre-lecture 3 », toutes deux vues par le validateur.
```

par

```text
il ne reste à écrire, hors les corrections que demande la contre-lecture 3, que la date de scellement et l'entrée « Contre-lecture 3 », toutes deux vues par le validateur.
```

### CL3-03 — Rejeu de deux tâches (V0 (l)) : dire l'environnement — recommandée

Constat : § 2, point 4. Le rejeu doit tourner comme la course (`PYTHONPATH=src`, `OMP_NUM_THREADS=1`, `python -B`), faute de quoi l'égalité au bit peut échouer pour une raison étrangère au code, et le texte ne permet pas de reprendre une course.

Ligne 282, clause (l) :

Remplacer

```text
(code v3, texte scellé, racines du manifeste ; autorisation par `autoriser_decision_regles` sur le texte scellé, puis
```

par

```text
(code v3, texte scellé, racines du manifeste ; environnement de la commande de la course : `PYTHONPATH=src`, `OMP_NUM_THREADS=1`, `python -B` ; autorisation par `autoriser_decision_regles` sur le texte scellé, puis
```

### CL3-04 — « Un seul manifeste de réplication » : désigner celui de cette réplication (V0 (k), Plan 3 point (3)) — recommandée

Constat : `runs/20261102-005705-essaim-ho-replication/` existe (réplication d'une autre étude, l'essaim hors échantillon). Un lecteur qui appliquerait à la lettre « un seul manifeste de réplication sous `runs/` » en compterait deux. Les manifestes de cette réplication portent le suffixe de la commande du Plan 5, étape 6 : `-replication-regles-defense`.

Ligne 282, clause (k) :

Remplacer

```text
un seul manifeste de réplication sous `runs/` (plus, au plus, celui d'une course interrompue consignée)
```

par

```text
un seul manifeste de cette réplication sous `runs/` (dossier dont le nom se termine par `-replication-regles-defense`, comme dans la commande du Plan 5, étape 6 ; plus, au plus, celui d'une course interrompue consignée)
```

Ligne 244, Plan 3 point (3) :

Remplacer

```text
un seul manifeste de réplication existe sous `runs/` (plus, au plus, celui d'une course interrompue et consignée, § Plan 7)
```

par

```text
un seul manifeste de cette réplication existe sous `runs/` (dossier dont le nom se termine par `-replication-regles-defense` ; plus, au plus, celui d'une course interrompue et consignée, § Plan 7)
```

### CL3-05 — Rapport de rédaction cité sans chemin ni empreinte (R6) — recommandée

Constat : le traitement de CL2-04 (l. 450) renvoie à « rapport de rédaction du brouillon 3 » : pièce du dossier, scellée, non désignée. Ligne 450 :

Remplacer

```text
(liste et commande : rapport de rédaction du brouillon 3)
```

par

```text
(liste et commande : `brouillons/preuves-mentors-v1/convergence-replication-v1/rapport-redaction-replication-v3.md`, `5b0f27d9b367554417c742007ab75877e33ef1f04d1ea74f7707a5b5cf4fb61a`)
```

## 4. Les deux marqueurs restants : forme exacte, contenu prévu, simulation

**Marqueur 1 — date de scellement (ligne 9, hors des sections : vu par le validateur).** Remplacer exactement

```text
texte scellé le À REMPLIR (date et heure UTC relevées par `date -u` au scellement, non estimées).
```

par

```text
texte scellé le AAAA-MM-JJ à HH:MM UTC (heure relevée par `date -u` au scellement, non estimée).
```

où `AAAA-MM-JJ à HH:MM` est le relevé de `date -u '+%Y-%m-%d à %H:%M'`, pris immédiatement avant d'écrire le fichier sous `prereg/` puis de le sceller (`controle_ia.prereg.sceller_prereg`) ; c'est la forme du brouillon 2, avec « relevée » et « estimée » au singulier. Rien d'autre sur cette ligne.

**Marqueur 2 — entrée « Contre-lecture 3 » (ligne 461, dernière ligne du texte, dans la section « Contre-lecture »).** Remplacer la ligne entière qui commence par `**Contre-lecture 3** — À REMPLIR (sous-agent neuf, courte, …` par la ligne suivante, **une seule ligne**. `<<EMPREINTE_RAPPORT_CL3>>` est à remplacer par la somme sha256 de ce rapport (donnée dans mon message de rendu ; recalculable par `sha256sum`) : tant qu'il reste, le validateur refuse (« marqueurs de gabarit restants »), ce qui est voulu. La liste de traitement est celle des remarques CL3-01 à CL3-05 supposées toutes acceptées ; à ajuster pour toute remarque refusée (écrire « refusée » et la raison dans le traitement, et retirer la mention correspondante de la dernière proposition) ; le verdict reste celui du contre-lecteur.

```text
**Contre-lecture 3** — sous-agent neuf (Claude Sonnet 5.5, `claude-sonnet-5-5` ; même modèle que B et que l'auteur de la contre-lecture 1, instance distincte ; n'a écrit ni ce texte, ni la spécification, ni le code v3, ni B, ni les contre-lectures 1 et 2), courte, sur les différences du brouillon 2 au brouillon 3 (`brouillons/preuves-mentors-v1/convergence-replication-v1/differences-brouillon2-brouillon3-replication-v1.diff`, empreinte `ecaf40a1534a088ac4ad66b73358108bfd1e72f6f9b6f981698d406cc666d8d8`), 2 novembre 2026 ; brouillon relu : `brouillons/preuves-mentors-v1/convergence-replication-v1/preenregistrement-replication-convergence-v1-brouillon3.md`, empreinte `73d2252ff2beec8e77eb1d6b33ab58c6b77c986b64cffdda23c7ce704f1ffbe1` ; rapport : `brouillons/preuves-mentors-v1/convergence-replication-v1/contre-lecture-3-preenregistrement-replication-v1.md`, empreinte `<<EMPREINTE_RAPPORT_CL3>>` ; verdict : scellable après corrections mineures ; traitement : CL3-01 (condition de départ sur la charge : attente permise, autre tâche seulement consignée), CL3-02 (étape 4 et traitement de CL2-07 : mention des corrections de la contre-lecture 3), CL3-03 (rejeu de V0 (l) dans l'environnement de la course), CL3-04 (V0 (k) et Plan 3 : manifeste de cette réplication) et CL3-05 (rapport de rédaction cité par chemin et empreinte) : acceptées et appliquées ; aucune autre modification du texte que ces corrections, la date de scellement et cette entrée.
```

Contenu : identité du contre-lecteur et de son indépendance (même modèle que B, instance distincte) ; objet relu (le diff et ses deux textes) ; brouillon relu, chemin et empreinte du brouillon 3 (73d2252f…, c'est-à-dire avant les corrections) ; rapport, chemin et empreinte ; verdict ; traitement une remarque par remarque ; mention des seules modifications autorisées. Trois empreintes distinctes de 64 chiffres une fois le gabarit remplacé (le validateur en exige deux par entrée).

**Simulation du validateur (`controle_ia.prereg.problemes`).** Copie jetable du brouillon 3 dans un dossier créé sous le dossier temporaire de la session (hors du dépôt), modifiée en mémoire puis écrite ; aucun appel à `sceller` ; dossier supprimé ensuite (constaté). Entrée simulée avec une empreinte factice pour mon rapport.

| Cas simulé | Résultat de `problemes` |
|---|---|
| État actuel (fichier du dépôt, lecture seule) | `['section vide ou à remplir : Contre-lecture']` |
| Date remplie + entrée remplie, avec les corrections CL3-01 à CL3-05 | `[]` |
| Date remplie + entrée remplie, sans aucune des corrections (toutes refusées) | `[]` |
| Gabarit `<<EMPREINTE_RAPPORT_CL3>>` oublié | `['marqueurs de gabarit restants : <<EMPREINTE_RAPPORT_CL3>>']` |
| Date oubliée | `['marqueur À REMPLIR restant hors des sections exigées']` |
| Entrée non remplie | `['section vide ou à remplir : Contre-lecture']` |
| Entrée avec une seule empreinte distincte | `['contre-lecture 3 sans ses deux empreintes (brouillon relu et rapport)']` |

Sur le texte final simulé, la garde d'identité du code v3 `exiger_identite_prereg_regles(texte, CONFIG_V4, "0:100", 0.3, "moyenne")` est conforme. L'autorisation de décision est restée vide après tous mes appels : aucune racine n'a été dérivée.

## 5. Règle R6 (empreintes compagnons)

État au moment de ma lecture : complet (§ 2, point 5). **À faire par la session avant le scellement du texte** : sceller ce rapport, sans quoi la phrase du texte « chaque pièce de ce dossier … a son compagnon » est fausse au scellement, et l'entrée de contre-lecture 3 cite un rapport sans compagnon :

```text
cd /home/claude/controle-ia-travail && D=brouillons/preuves-mentors-v1/convergence-replication-v1 && PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller $D/contre-lecture-3-preenregistrement-replication-v1.md
find $D -type f ! -name '*.sha256' ! -path '*/__pycache__/*' | while read f; do [ -f "$f.sha256" ] || echo "SANS COMPAGNON $f"; done
```

(Le second ordre doit rester muet.) Les pièces nées après le scellement (sorties de la course, sortie de B) seront scellées à leur création, comme le dit le Plan 5.

## 6. Les écarts d'auteur du rapport de rédaction : vérification

| Écart déclaré | Verdict | Vérification |
|---|---|---|
| CL2-01 (iii) : V0 (h) compte **six** fichiers lus par B en réplication, non « leurs compagnons » | **juste** | `implementation_b_v2.py`, `analyser_fichiers` (l. 1434-1531) : `noter(...)` est appelée six fois en mode réplication — E1, deux fois E4 (analyse et résultats originaux, par empreintes épinglées, sans compagnon), E3, E2, E5 — et jamais pour un compagnon. Les compagnons de E1, E2, E3, E5 sont bien lus et vérifiés (`lire_fichier_verifie` sans empreinte imposée), mais ne figurent pas dans `empreintes_fichiers`. Le texte de la contre-lecture 2 (« … et leurs compagnons ») aurait rendu V0 (h) fausse. Empreintes épinglées citées : `18b80112…` (analyse), `d07ece47…` (résultats) : exactes. |
| CL2-01 (i) et (ii) : la liste fermée nomme le **listage des noms** de dossiers et le **script de mutations de la v1** | **juste** (une nuance) | Rapport de validation de B v2, section « Fichiers ouverts » : listage (`ls`) des trois dossiers « noms seulement » ; `scratchpad/mut/mutations.py` (« mon script de mutations de la v1, lu pour l'adapter ») ; `scratchpad/v2/` « supprimés à la fin » ; `/tmp/pytest-of-root/`. Chaque entrée de cette liste est couverte par les listes fermées du brouillon 3 (CLAUDE.md, consigne, entrées, fichiers v1 et v2 de `implementation-b/`, interpréteur et bibliothèques, temporaires, listage). Le dossier `mut/` et le dossier `v2/` n'existent plus (constaté). Nuance : « supprimés à la fin selon son rapport » couvre aussi `mut/`, dont le rapport ne dit pas la suppression ; sans conséquence (facultatif : écrire « supprimés à la fin (selon son rapport pour ses brouillons de la v2 et ses dossiers d'essais) »). Ligne 5 et ligne 271 du rapport : modèle `claude-sonnet-5-5` : exact. |
| CL2-04 (ii) : « chaque pièce de ce dossier » étendue aux sous-dossiers (+ 4 entrées de B, 5 fichiers de B v1, 3 fichiers neufs) | **juste** | 31 sur 31 (§ 2, point 5). Empreinte de la contre-lecture 2 écrite en clair : `121154a4…` exacte ; commit `3221a7b4` existe et contient le fichier à cette empreinte. |
| CL2-10 : essais qui scellent un texte temporaire synthétique = **E4, C8, C9, E9, E10** (non E4, E9, E10) | **juste** | `prereg_scelle` (essais du code v3, l. 124-128) appelée dans E4 (l. 377, 382, 390, 395), C8 (l. 418), C9 (l. 451) ; `sceller` appelé dans E9 (complément, l. 445) et E10 (l. 481). Aucun autre essai ne scelle. |
| CL2-11 : chemin du rejeu précisé (autorisation puis tâche sérialisée, rien sous `runs/` ni `diag/`) | **juste** | § 2, point 4. |
| Autres ajouts (déclarés) | justes | Chiffres de CL2-08 « 18,5 et 28,9 erreurs-types » : recalculés par moi dans l'analyse de la course originale (`18b80112…`, `R3 - R2 (V_iii_final)`, moyenne ÷ (écart-type ÷ √100)) : 18,471 et 28,943. Revérifications datées (sceaux de la course originale, bloc d'identité) : je les ai refaites, toutes conformes. `6151e597` est ancêtre de `HEAD` (aujourd'hui `09bbab36` ; le texte écrit `0348a83d`, vrai au moment où il l'a été) et les empreintes de 15 pièces dans ce commit égalent le disque. |

## 7. Vérifié, non vérifié, observations

**Vérifié par moi** : diff régénéré identique ; les 13 remarques ; 37 empreintes du brouillon 3 rattachées à une pièce ; sceaux de la course originale (manifeste, PID, résultats, analyse, préenregistrement original : `verifier` conforme) ; bloc d'identité régénéré (`identite`, qui ne fait qu'imprimer ; aucune racine) égal au texte hors la ligne de B ; compagnons ; commit `6151e597` ; décision R-1086, point 5 (« N = 100, seuil “graines neuves” > 2, implémentation B par une autre famille (Sonnet) ») et R-1075 (21:30 et 21:36, Paris, « go » nommant la réplication de la convergence) ; options de ligne de commande de B v2 contre la commande de l'étape 7 (toutes existent, sans `--plomberie-fausse`) ; renvois internes (« § Issues écrites d'avance », « Conséquence de chaque issue, point 1 », « § Plan 7 », « § Plan 5, étape 3 ») existent.

**Non vérifié** : je n'ai rejoué ni les essais du code v3 (43), ni ceux de B v2 (560), ni la campagne de mutations, ni V0 (l) (voir plus haut), ni la commande de l'étape 7 (elle exige les sorties de la course). Je m'en remets au journal des essais, au rapport de validation de B et à la contre-lecture 2 pour ces points.

**Observations sans correction demandée** : (a) la mention « Claude Opus 5.5 » pour l'**auteur du code v3** (CL2-01, CL2-09, Rôles) vient du texte de la contre-lecture 2 ; aucune pièce du dossier ne la porte (l'en-tête du code ne nomme pas l'auteur) : la session peut la confirmer, ou n'écrire « Claude Opus 5.5 » que pour l'auteur de la spécification. (b) `registres/decisions.md` est modifié dans l'arbre par une autre session (pas par moi) ; sans lien avec ce dossier. (c) Le brouillon 3 et le diff citent encore, ligne 19, `HEAD = 0348a83d` : phrase datée, vraie quand elle a été écrite ; la vérification `git merge-base --is-ancestor` reste à refaire au scellement, comme le texte le dit. (d) Machine partagée : la charge à une minute est passée de 0,24 à 2,51 en deux minutes (mes contrôles et d'autres sessions) ; pour la course, annoncer aux autres sessions une fenêtre de calcul exclusive est une précaution d'exploitation (hors texte).
