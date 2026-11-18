# Contre-lecture du lanceur de l'organisme d'idéation, lignée Kimi, version 11 — v1

Contre-lecteur neuf (Opus 5.5, sous-agent) : je n'ai écrit ni le lanceur v11, ni ses essais, ni le v9, ni l'addendum v4.
Date : 2026-11-18, vers 08:00Z. Dépôt au commit `379b7123` (branche `claude/eloquent-tesla-e52a0b`) ; registre des GO lu sur
`origin/main` = `98ed6786` après `git fetch origin +refs/heads/main:refs/remotes/origin/main`.
Rien lu des fiches de proposeurs ni des consignes ou réponses de juge (ni `/home/user/sorties-course-ideation-organismes-discrets-v8/`,
ni `runs/epreuve-temoins-seuls-v4/reponse-du-juge.md`) ; de l'épreuve des témoins seuls, seul `issue.json` (sceau vérifié).
Aucun appel payant, aucun relais, aucune course.

Pièces : `scripts/lancer_course_ideation_organismes_discrets_v11.py` (pas encore de compagnon `.sha256`) ;
`scripts/lancer_course_ideation_organismes_discrets_v9.py` (`63a54d04…`, égal à son compagnon) ;
`docs/notes/organismes-discrets-v1/organisme-ideation-v1/temoins-organisme-discrets-v6.json` ;
`docs/notes/organismes-discrets-v1/organisme-ideation-v1/addendum-temoins-et-carbon-v4.md` (`3c6f9448…`, égal à son compagnon) ;
`tests/test_lancer_course_ideation_organismes_discrets_v11.py` ; orchestrateur `/home/user/lciric/ideation-organism/orchestrator`.

## Verdict

**Autorisable** — le code est le v9 avec les seuls changements annoncés, les témoins v6 épinglés sont les bons et se chargent
par l'orchestrateur épinglé. Trois conditions de départ, sans changement de code (constats 1 à 3, significatifs), sont à
remplir par la mère avant le feu ; sinon la garde refuse (constats 1 et 2) ou le plafond de la ligne n'est plus tenu par
programme (constat 3).

## Vérifications

1. **Diff du code contre le v9.** `diff v9 v11` : en-tête (nouveau paragraphe v11, puis le texte du v9 gardé « pour mémoire ») ;
   `VERSION` ; la pièce `temoins` (chemin v6 et empreinte `07c80a23…` au lieu de v1 `1c6eef38…`) ; `DECISION` (deux lignes au
   lieu d'une) ; `DOSSIER_SORTIES`, `SOUS_DOSSIER_RUNS`, `SUFFIXE_RUN` en v11. Rien d'autre : `PERIMETRE_GO`, bornes 11,3,
   `LIGNEES_EXTERNES`, délais, verrou, gardes, superviseur, commandes, inchangés. **Conforme** à l'annonce et au § 6 de
   l'addendum v4 (« le v9 avec les témoins v6 épinglés ; rien d'autre » — la série de runs, la sortie et la version suivent
   nécessairement de R12).
2. **Empreinte des témoins v6.** `sha256sum` du fichier = `07c80a23eed67acb8457deefb5ad45135c54683eddc37949a2de60426a838a42`,
   égale à l'épingle (ligne 167) et au compagnon. **Conforme.**
3. **Chargement par l'orchestrateur épinglé (épreuve à sec).** Dossier neuf `/tmp/cl-v11-kimi-Vhid`, environnement réduit
   `env -i PATH=/usr/bin:/bin HOME=<tmp> LANG=C.UTF-8`, `/usr/local/bin/python3 -I -B`, préfixe de cache d'octets dans le
   dossier temporaire. Rejoué tel quel : `construire_liste_blanche` du lanceur (les trois pièces question v3, faits v3,
   témoins v6) puis `mesurer_consignes(commande_mesure(...))`. Résultat : liste blanche écrite et scellée par
   l'orchestrateur, contenu égal aux empreintes attendues (`09ba5ad6…`) ; mesure `sans_appel: true` (le chemin passe par
   `charger_temoins`, `pole/ideation_v2.py` l. 1730) ; gardes de taille tenues (consigne 11 560 caractères, marge 228 440 ;
   planchers Kimi 0,0696 et 0,0685 USD sous 1,7 et 1,5). Appel direct de `charger_temoins` avec la même liste : 4 témoins,
   classes vrai / jumeau / faux_falsifiabilite / faux_anteriorite, attendus conformes. Le clone n'a pas été modifié par
   l'épreuve. **Conforme.**
4. **Garde de GO sur le registre de `main`.** `verifier_go` sur `origin/main:registres/go.md` au 2026-11-18 : une seule ligne
   principale, `GO-2026-11-18-17`, plafond 11,3 USD ≥ pire cas 11,3, échéance 2026-11-22, Lazar. Variantes ajoutées au
   registre (simulation, sous le dossier de travail temporaire) :
   - ligne `| GO-2026-11-18-17 | … | calcul | extension : … lignée kimi … |` (8 colonnes) : **hors du compte**, GO-17 reconnu ;
   - même ligne commençant par « Extension » : hors du compte (comparaison en minuscules) ;
   - ligne d'un autre identifiant, cellule commençant par « extension de GO-2026-11-18-17 : … » : hors du compte, GO-17 reconnu ;
   - cellule commençant par `**Extension**` (gras) : **refus** (« 2 ligne(s) principale(s) ») ;
   - ligne qui cite GO-17 sans commencer par « extension » et porte les trois expressions : **refus** (2 lignes principales) ;
   - ligne citant GO-17 à 9 colonnes : **refus** (« mal formée ») ;
   - au 2026-11-23 : refus (hors période).
   Le refus est sûr (rien ne part) mais bloque le départ ; voir constat 2.
5. **Essais.** `PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_lancer_course_ideation_organismes_discrets_v11.py` :
   6 réussis ; ceux du v9 : 18 réussis. Ils testent ce qui change : épingle des témoins v6 et pièces communes inchangées ;
   pièces vérifiées sur le dépôt réel ; égalité de code au v9 hors de 15 lignes de diff à mots permis ; GO-17 reconnu sur le
   registre de `main` ; témoins v6 dans la commande de course ; lignée inconnue refusée. Manques : constat 5.
6. **En-tête.** Vrai sur chaque point vérifiable : v9 `63a54d04…` inchangé et jamais joué (ni `runs/course-ideation-organismes-discrets-v9/`
   ni dossier de sortie v9) ; témoins `07c80a23…` ; addendum `3c6f9448…` scellé ; épreuve des témoins seuls : `issue.json`
   (sceau vérifié) code 0, quatre témoins `tenu: true` pour le juge Opus, 0,163 USD relevés au relais ; série et sortie v11 ;
   usage `… v11.py kimi` conforme à `commande_exacte`. Non vérifiable par moi : « signalé à la mère avant départ » (condition
   de GO-17). Réserves de forme : constats 2 et 6.

## Constats

### Significatifs

1. **Cache d'octets dans le clone épinglé : le départ sera refusé tel quel.** `/home/user/lciric/ideation-organism/orchestrator/pole/__pycache__/`
   existe (14 fichiers `.pyc`, 2026-11-18 07:24:12Z) ; `git status --porcelain --ignored` n'est pas vide, donc
   `verifier_orchestrateur` (v11 l. 534-541) refuse. Cause très probable : `tests/test_epreuve_temoins_seuls_v2..v4.py`
   importent `pole` depuis le clone (`from pole.adaptateurs import Resultat`) sans `-B` ; la routine de reprise (`python -m pytest -q`)
   le recréera à chaque passage. À faire avant le feu : retirer ce dossier par son chemin exact, puis ne plus lancer la suite
   d'essais sans `-B` (ou `PYTHONDONTWRITEBYTECODE=1`) entre ce retrait et le départ ; à terme, ces essais devraient poser
   `sys.dont_write_bytecode = True` avant l'import. Pas un défaut du v11 (la garde fait son travail), mais une condition de
   départ non remplie aujourd'hui.
2. **Forme de la ligne qui consigne le v11 : l'en-tête dit « ligne d'extension », l'addendum dit « ligne de forme ».**
   En-tête v11 (l. 10-11) : « la mère consigne le lanceur v11 et l'addendum par une ligne d'extension, que la garde ne compte
   pas ». Addendum v4 § 6 (l. 160-161) : « avant sa ligne de forme (la mère l'inscrit avec l'empreinte de cet addendum) ». Une
   « ligne de forme » au sens de GO-2026-11-18-11 (ligne principale neuve qui remplace l'ancienne) porterait le périmètre
   « lignée kimi » et ferait **deux** lignes principales : refus. La garde (l. 465-466) n'écarte que les cellules dont le texte
   commence littéralement par « extension » (sans gras, sans autre préfixe). Condition : la mère écrit une ligne à 8 colonnes
   dont la cellule de périmètre commence par « extension » (ex. `extension : lanceur v11 … témoins v6 …`), ou une ligne sans
   les trois expressions du périmètre ; et elle rejoue `verifier_go` (ou l'essai du registre de `main`) après l'avoir poussée.
   Corriger aussi le mot de l'un des deux documents par une note (pas de réécriture, R12).
3. **Le v9 reste lançable sous la même ligne de GO, et la garde de cumul du v11 ne le voit pas.** GO-17 nomme le lanceur v9 ;
   la garde de GO du v9 a le même périmètre et reconnaît GO-17 sur `main`. La garde de cumul de chaque lanceur ne compte que
   sa série (`runs/…-v9` pour l'un, `runs/…-v11` pour l'autre) et chacun a son verrou dans son dossier de sortie. Une course
   v9 (témoins v1, que GO-17 exclut par sa condition) puis une course v11 seraient deux fois 9,2 USD au pire sous un plafond de
   11,3, sans refus programmé. Aujourd'hui le v9 n'a jamais couru : le risque est une erreur d'opérateur. Condition : la ligne
   d'extension dit explicitement que le v9 n'est plus le lanceur de GO-17 et ne sera pas lancé. (Correction de code possible
   mais hors du périmètre annoncé : faire compter au v11 aussi la série v9.)

### Mineurs

4. Le v11 et ses essais n'ont pas encore de compagnon `.sha256` : M1 (`verifier_soi`) refuse tant que le lanceur n'est pas
   scellé. Attendu à ce stade (scellement après contre-lecture) ; à faire, et l'empreinte à donner à la mère.
5. Essais : aucun essai ne prouve qu'une ligne d'extension citant GO-17 reste hors du compte, alors que l'en-tête s'appuie
   dessus (vérifié ici par simulation, point 4). `test_go_kimi_du_registre_de_main_reconnu` se saute en silence si
   `origin/main` manque (repli silencieux, R5) et dépend de l'état du registre distant au moment de l'essai. Le filtre de
   `test_code_egal_au_v9_hors_des_lignes_annoncees` est large (« temoins », « lignée kimi » …) ; c'est le compte exact de
   15 lignes qui le rend serré.
6. En-tête : le texte du v9 « pour mémoire » est dans la même chaîne de documentation et garde ses propres « Usage : … v9.py
   kimi », « Essais : … v9.py », série « v9 » et « dossier de sortie du v9 » pour le verrou ; un lecteur pressé peut s'y
   tromper. Le paragraphe v11 ne redit pas que le verrou, désormais dans la sortie v11, n'exclut ni une course du v9 ni une
   course du v10 / v12 (Carbon) : « une course à la fois » reste une discipline d'opérateur (§ 6 de l'addendum, « chaque
   départ signalé »).
7. `DECISION` ne cite pas l'identifiant de la ligne de GO (« trouvée par son contenu ») ; le manifeste la porte par ailleurs
   (`go`), sans conséquence.
