# Rapport du développeur sur les corrections du code de l'étape B bis de T0.7 (modèle A), v1

**Déclaration** : rédigé sans vue des données de 7b ; aucune sortie de 7a, 7b, T0.7 ou P3-bis lue ; rien lu sous `diag/`, `runs/`,
`donnees/` du dépôt de travail ; aucune machine, aucun appel réseau, aucune dépense.

- **Auteur** : « modèle A », auteur du code de B bis et de l'adaptateur de MC ; lecteur d'aucun verdict.
- **Date (UTC, `date -u`)** : 2026-11-14, après 15:50 (fin de la contre-lecture) jusqu'à 16:11.
- **Objet** : corrections demandées par la contre-lecture du code (« modèle C »),
  `brouillons/T0.7-etape-B-bis-v1/code/contre-lecture-code-modele-c-v1.md`,
  `e553a85eee20326b9da435a3832a5e0ad4d6b9c703c368826deecf6fc94cfd38`, verdict « scellable après corrections », lue en entier.
- **Commits** (branche `prep/t07bbis-code-v1`, jamais poussée) : départ `ffde97be` (contre-lecture versée par la mère) ;
  corrections `189868e639c098a0da6a58da10c0d2caf318edac` ; ce rapport et la sortie des essais, commit suivant.
- **Rapports antérieurs inchangés (R12)** : `rapport-developpeur-v1.md` `0b694da9…`, `essais-sortie-v1.txt` `aa50f075…`,
  `rapport-developpeur-adaptateur-mc-v1.md` `91a7caf0…`, `essais-sortie-adaptateur-mc-v1.txt` `8fde6e2d…`,
  `contre-lecture-code-modele-c-v1.md` `e553a85e…` (empreintes revérifiées à 16:08:59Z).

## 1. Verdict

Tous les constats demandés sont corrigés (B1, B2, M1, M2, M3, m1, m2, m5, m7), chacun avec un essai qui joue son cas sain et
son artefact ; m3 et m4 sont déclarés (interprétations 19 à 21), m6 est conforme. **105 essais passent** sur l'arbre complet ;
sur l'arbre que l'instance extrait (simulation de l'extraction partielle), **83 passent et 22 sautent**, et l'amorce exige
désormais ces 83. Reste à prouver sur la carte, à la répétition à blanc de mardi : l'apprentissage sur « cuda » (M2) et la chaîne de
l'amorce sur les vraies branches.

## 2. Une ligne par constat

| constat | fait | où | essai (cas sain ; artefact) |
|---|---|---|---|
| **B1** (bloquant) | L'égalité `tête == commit de la fiche` est remplacée par « le commit de la fiche est un **ancêtre** de la tête » (`git merge-base --is-ancestor` ; objet absent, tête illisible ou non-ancêtre → arrêt) ; contrôle fichier par fichier des empreintes de `fiche["fichiers"]` gardé, fichier absent → arrêt par la garde, motif nommé (au lieu d'une
erreur non gardée) ; `gardes_d_entree` rend la tête. Le même contrôle est joué côté session par `lancer commande` (sous-commande `ancetre RACINE COMMIT`, facultatif selon la contre-lecture, fait). | `registre_bbis_v1.exiger_ancetre`, `exiger_ancetre_de_la_fiche`, `main` (`ancetre`) ; `marche_v1.gardes_d_entree` ; `scripts/lancer_bbis_v1.sh` | `test_t07bbis_chaine_instance_v1::test_gardes_d_entree_commit_de_la_fiche_ancetre_cas_sain_et_artefacts` : dépôt jetable, C0 = code, fiche écrite par `ecrire_fiche_code` citant C0, C1 = lignes ; `BBIS_INSTANCE=1` → **passe** (et passe encore sur un commit local descendant de C1). Artefacts : (i) fiche citant un commit d'une branche voisine → « n'est pas un ancêtre » ; fiche citant un commit absent → « absent du dépôt » ; (ii) code modifié par un commit postérieur → « empreinte ≠ fiche » ; code retiré → « absent : arrêt » ; (iii) tête = C0 sans les lignes → refus (registre absent). Côté session : COMMIT d'une branche voisine → refus. `bout_en_bout::test_marche_reelle_refusee…` mis à jour (fiche jouet `cccc…` → « absent du dépôt »). |
| **B2** (bloquant) | `/scripts/lancer_bbis_v1.sh*` ajouté à `MOTIFS`. | `scripts/amorce_bbis_v1.sh` | `test_motifs_de_l_amorce_couvrent_les_chemins_des_essais` : `MOTIFS` lus dans l'amorce, dépôt jetable portant les chemins que les essais ouvrent (les quatre scripts, `prereg/T0.7-etape-B-bis-v1.md`, `prereg/P3-consignes-v1.md` et leurs compagnons, `tests/conftest.py`, `requirements-gpu.txt`, registres nommés, `t06/test_croise.py`) **et** tout le code et tous les essais du paquet (`src/controle_ia/t07bbis/*.py`, `tests/test_t07bbis_*.py`, `tests/aide_t07bbis_*.py` : tout ce que la fiche de `CODE-BBIS` peut citer), plus dix chemins interdits ; `sparse-checkout set --no-cone` : tout présent, aucun interdit. Artefact : motif de `lancer` retiré → `scripts/lancer_bbis_v1.sh` seul manquant. |
| **M1** (majeur, décision de la mère) | Après les copies (fichiers cités par le registre propre, entrées de 7b, fichiers cités par la configuration de 7b, compagnons compris, tous accumulés dans `COPIES`), l'amorce fait un **commit local** (`git add --sparse -f` des seules copies, `commit --allow-empty`), **jamais poussé** ; elle exige parent = COMMIT et `git status --porcelain --untracked-files=all` vide, sinon arrêt ; contrôle redit juste avant la marche (arbre propre, tête = commit local). La marche (arbre propre exigé en marche réelle, inchangé) écrit au manifeste : `commit` = commit local (par `creer_manifeste`) et `config.entrees_locales` = {commit, parent, fichiers ajoutés avec leur identifiant d'objet git}. La branche de sortie `donnees/t07-etape-b-bis-v1` est créée **après** la marche **depuis COMMIT** : le commit local n'entre jamais dans ce qui est poussé. | `scripts/amorce_bbis_v1.sh` (`commit_local_entrees`, étapes 7 et 8) ; `marche_v1.entrees_locales`, `marche` | `test_commit_local_des_entrees_arbre_propre_et_branche_de_sortie` (extrait de l'amorce joué par bash sur un dépôt jetable extrait par les vrais `MOTIFS`, entrées non suivies et ignorées hors des motifs) : arbre propre après le commit, parent = COMMIT, objets git égaux, branche de sortie depuis COMMIT sans le commit local, sorties de la marche gardées, entrées retirées de l'arbre. Artefacts : fichier non suivi resté hors des copies → « arbre non propre » (code 2) ; aucune copie → arrêt ; parent ≠ COMMIT → arrêt ; dépôt sans commit → `entrees_locales` refuse en marche réelle. Sur la chaîne vraie (jouet) : `bout_en_bout::test_commit_local_des_entrees_et_arret_ecrit_sur_une_course_jouet` (arbre propre après le commit local ; manifeste citant commit et parent ; la marche n'écrit que sous `runs/<run>` et `diag/<run>`, aucun fichier suivi touché). |
| **M2** (majeur) | Toute erreur levée **après la création du manifeste** (relecture, préparation, apprentissage et notation — une `RuntimeError` de torch comprise —, contrôle carte-processeur, écriture des fichiers fermés), hors garde de débit, écrit `diag/<run>/arret-marche-bbis.json` (scellé, rattaché au manifeste : étape, type, motif, garde ou non, fin de la pile, journal des durées, `scores_ecrits: false` ; aucune aire) et rend le **code fermé 4** ; l'amorce a un cas 4 (traces poussées, instance arrêtée). L'apprentissage réel sur la carte se prouve à la répétition à blanc de mardi, avant `GO-BBIS` (non fait ici). | `marche_v1.marche` (corps déplacé dans `_apres_manifeste`, étape tenue à jour), `main` ; `scripts/amorce_bbis_v1.sh` (cas 4) | `bout_en_bout::test_commit_local_des_entrees_et_arret_ecrit…` : erreur « CUDA error » simulée dans `apprendre_source` après une relecture vraie → arrêt écrit, scellé, sans aire, aucun fichier de scores, relecture gardée. `test_codes_fermes_de_la_marche` : 0 scores, 3 débit, 4 arrêt écrit, 2 refus d'entrée ; cas 4 présent dans l'amorce. |
| **M3** (majeur) | Le journal porte la **ligne de compte entière** de pytest (passés, sautés, durée) ; `-rs` nomme chaque essai sauté dans `essais.txt` (poussé avec les traces) ; **au moins `MIN_ESSAIS` = 83 passés** exigés, sinon arrêt. 83 est le compte exact de la simulation de l'extraction partielle (§ 4) ; sautent sur l'instance : `bout_en_bout` 8 essais sur 9 (course jouet absente), `etat_impose` 6, `lien_mots_et_cout` 8 (code de la pièce exclu). | `scripts/amorce_bbis_v1.sh` (étape 5, `compte_passes`, `MIN_ESSAIS`) | `test_compte_des_essais_passes_et_minimum` : compte lu sur six lignes types (passés seuls, échecs et passés, sautés seuls, aucune, vide) ; `MIN_ESSAIS` écrit une fois, au moins 60 ; `-rs` et ligne entière présents. |
| **m1** | `lire_fuites` : ligne `AUDIT-FUITES-T07` absente → « non disponible » (seul cas du texte) ; fichier présent mais illisible ou hors du domaine de `t07.criteres_v1.valider_audit_fuites` → **arrêt de la lecture**, motif écrit, jamais « non disponible ». L'audit est lu **avant** toute grandeur (au début de la lecture) ; place de R-F dans la liste des réserves inchangée. | `lecture_v1.lire_fuites`, `lire` | `test_reserves_de_fuites_recopiees_ou_absentes` : sain (fuite recopiée ; aucune fuite → liste vide) ; artefacts : `[]`, texte illisible, ancien format sans consigne ni champs, séparation 0,5 hors de [0,70 ; 1], jeux vides → arrêt, motif nommé, « non disponible » absent. |
| **m2** | `_sans_aire` ne lit plus les clés du dictionnaire `plis` (tâche → pli, au premier niveau seulement) comme des clés d'aire ; ses valeurs doivent être des entiers 0 ou 1. | `marche_v1._sans_aire` | `test_sans_aire_identifiants_de_taches_commencant_par_aire` : tâches `aire-1`, `aire_2` → pas d'arrêt ; artefacts : vraie clé d'aire au sommet et en profondeur, `plis` non au sommet, valeur 0,83 ou booléenne → arrêt. |
| **m3** | Aucun changement de code (décision de la mère) ; déclaré : interprétation 19. | — | essai inchangé (`apprentissage::test_controle_carte_processeur…`). |
| **m4** | Aucun changement de code ; déclaré : interprétations 20 et 21. | — | — |
| **m5** | L'amorce en essai local **n'écrit plus rien** (`mkdir` de ses dossiers déplacé après la sortie de l'essai) ; `lancer commande` la joue avec `RACINE_AMORCE` sur un dossier jetable (`mktemp -d`), retiré par `rmdir` (qui échoue, donc refuse, si l'amorce y a écrit) ; **garde d'offre** : `commande` prend `OFFRE.json` et `OFFRE_ID` (13 arguments) et exige `registre_bbis_v1 offre OFFRE.json OFFRE_ID` (bornes du devis et `id` égal). | `scripts/amorce_bbis_v1.sh`, `scripts/lancer_bbis_v1.sh`, `registre_bbis_v1.exiger_offre(offre, identifiant)` | `test_essai_local_sans_ecriture_et_garde_d_offre_de_la_commande` : amorce en essai → aucun dossier créé ; `commande` saine sur le dépôt jetable de B1 → commande imprimée, dossier jetable vide et retiré ; artefacts : `id` 98 ≠ 99, H200, étiquette autre → refus ; COMMIT d'une branche voisine → refus (B1) ; douze arguments → refus. `registre::test_scripts_de_session…` mis à jour (13 arguments ; fiche absente → refus par la garde d'ancêtre). |
| **m6** | Conforme au texte (LEX « non calculable » → E3, motif écrit) ; rien à faire. | — | — |
| **m7** | Boucle de copie des fichiers cités par le registre propre placée entre deux marques dans l'amorce et jouée par l'essai (le texte joué est celui de l'amorce, sans recopie). | `scripts/amorce_bbis_v1.sh` (`copie-des-fichiers-cites`) | `test_boucle_de_copie_des_fichiers_cites_sain_et_artefact` : dépôt jetable extrait par les vrais `MOTIFS` ; fichier cité hors des motifs (`docs/verdicts/…`) et compagnons recopiés depuis la tête, contenu égal ; cité mais absent de la tête : rien écrit. Artefacts : `docs/notes/…`, `…lecture-sondes-t06…`, `donnees/bras-attaque…` cités → « chemin interdit cité », code 2. |

## 3. Interprétations déclarées (suite des 18 du rapport v1)

19. **(m3) Moment du contrôle carte-processeur** : le couple (cellule, pli) tiré d'avance est contrôlé juste après l'apprentissage
    **complet** de sa source (sonde finale, 800 directions, sondes du nul, ENC), non juste après la sonde finale. Le texte (« un
    (cellule, pli) tiré par graine est réappris sur le processeur ») n'impose aucun moment ; au pire, une erreur de chaîne se
    découvre après plusieurs heures de carte. Le docstring de `marche_v1` (« joué dès qu'il est appris ») et le § 5, interprétation
    4, du rapport v1 sont à lire ainsi.
20. **(m4) Chemin de `SCORES-BBIS`** : la ligne cite `diag/<run-bbis>/sondes-bbis.json` (fichier fermé scellé qui porte l'empreinte
    de chaque morceau `scores-bbis-NNN.npz`, de `sondes-bbis.npz` et des planchers), non les fichiers de scores eux-mêmes ; la
    lecture vérifie chaque morceau contre ces empreintes (source « non calculable » sinon).
21. **(m4) Graines au manifeste** : le manifeste de la marche porte quatre clés fixes (`bbis/interne/e0`, `bbis/interne/e1`,
    `bbis/egalite-carte`, `bbis/chemin-impose`) ; toutes les autres clés dérivées (par cellule, pli, réétiquetage, direction)
    sont écrites dans `sondes-bbis.json`, champ `graines_derivees`, sous la même entropie (celle de la fiche de `CODE-BBIS`).
22. **(B1) Condition d'usage** : le commit du code cité par la fiche doit rester dans l'histoire de la branche `BRANCHE_CODE` qui
    porte les lignes (fusion qui le garde ; ni écrasement en un seul commit, ni rebasage, ni reprise à la main) ; sinon la garde
    arrête, avant la location si `lancer commande` est joué (contrôle `ancetre`), dans la marche sinon. Le dépôt de la session
    (`RACINE` de `commande`) doit contenir COMMIT.
23. **(M1) Ce que cite le manifeste** : son `commit` est le commit local des entrées, jamais poussé ; il se reconstruit comme
    COMMIT (poussé) plus les fichiers de `config.entrees_locales.fichiers`, dont les identifiants d'objet git se vérifient
    contre la branche de 7b. Le commit local porte **toutes** les copies, `donnees/` comprise (ajout forcé), et pas seulement
    les fichiers qui troublaient l'arbre. La branche de sortie part de COMMIT : la création de branche retire de l'arbre les entrées
    de 7b (devenues inutiles) et garde les sorties de la marche (non suivies ou ignorées) ; l'essai sur la course jouet établit
    que la marche ne touche aucun fichier suivi.
24. **(M2) Portée de l'arrêt écrit** : tout ce qui suit la création du manifeste, pas seulement l'apprentissage sur la carte.
    Conséquence déclarée : une garde (`GardeArret`) levée dans la relecture, l'apprentissage ou l'écriture rend désormais le code 4
    avec un fichier d'arrêt (elle rendait 2 sans fichier) ; le champ `garde` dit lequel. Avant le manifeste, codes 2 (garde) et 1
    (autre) inchangés. Motif coupé à 4 000 caractères, pile aux 6 000 derniers ; les messages des gardes ne portent aucune aire.
25. **(M3) Tenue de `MIN_ESSAIS`** : 83 est le compte exact de la simulation au commit `189868e6`. Tout essai ajouté ou retiré au
    paquet impose de recompter et de réécrire ce nombre (un nombre trop haut arrête l'instance à l'étape 5, avant la marche ; trop
    bas, il affaiblit le contrôle). Un essai qui échoue arrête toujours, comme avant.
26. **(m1) Domaine de l'audit** : la forme est contrôlée par `valider_audit_fuites` de T0.7, la consigne étant prise dans le
    fichier lui-même ; son égalité à la ligne `CONSIGNE-AUDIT-FUITES-T07` relève de T0.7 (B bis ne lit pas cette ligne).
27. **(m5) Signature de `commande`** : `commande RACINE OFFRE.json OFFRE_ID COMMIT BRANCHE_CODE RUN_7B BRANCHE_7B RUN_BBIS
    ECHEANCE_UTC_S FEU RELANCES IMAGE` ; `OFFRE.json` porte les clés de la garde d'offre et `id`. Ordre des contrôles : arguments,
    offre, amorce en essai, création, ancêtre ; puis la commande est imprimée.
28. **Noms des fichiers de code** : les fichiers corrigés gardent leur nom (fixé par le texte scellé ; aucun compagnon `.sha256`
    pour le code) ; la version précédente reste au commit `ffde97be` ; seule la fiche de `CODE-BBIS` fera foi des empreintes. Les
    livrables écrits (rapports, sorties) sont neufs et versionnés (R12).

## 4. Essais

- **Arbre complet** (copie de travail = commit `189868e6`), 16:02:46Z → 16:05:44Z :
  `PYTHONPATH=src python -m pytest -q -rs -p no:cacheprovider --color=no tests/test_t07bbis_*.py` → **105 passed**, 0 sauté,
  4 avertissements (fork de l'épreuve de niveau à deux processus, déclaré au rapport v1), 2 min 56 s. Soit les 96 d'avant
  plus 9 : 8 dans `tests/test_t07bbis_chaine_instance_v1.py` (neuf) et 1 dans `test_t07bbis_bout_en_bout_v1.py`.
- **Simulation de l'extraction partielle de l'instance** (M3) : clone sans extraction de la seule branche `prep/t07bbis-code-v1`
  dans un dossier jetable du bloc-notes de la session, `MOTIFS` lus dans l'amorce, `sparse-checkout init --no-cone` / `set
  --no-cone --stdin` / `checkout 189868e6` (`docs/notes/` et `diag/` absents), puis la commande de l'étape 5 → **83 passed, 22
  skipped**, code 0, 60 s. Les 22 essais sautés sont nommés dans la sortie.
- Sortie complète : `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v1.txt` (`8bfdb66e…`, scellée).
- Essais neufs ou changés : `chaine_instance` (B1, B2, m7, M1, codes de M2, M3, m5, m2) ; `bout_en_bout` (+1 : M1 et M2 sur
  la chaîne vraie ; message de B1) ; `lecture` (m1, essai réécrit) ; `registre` (signature de `commande`, garde d'ancêtre).
  Aide neuve : `tests/aide_t07bbis_depot_v1.py` (dépôts jetables, extraits de l'amorce lus entre leurs marques, motifs).

## 5. Refus de la garde d'isolement de la copie de travail

Trois refus, tous de forme (« commande trop complexe à vérifier, à découper en commandes simples ») ; chaque geste refusé a été
arrêté, puis refait par l'outil d'édition ou en commandes séparées, comme la garde le demande ; aucun refus de fond, aucun
contournement :
1. édition de `marche_v1.py` par un script Python en document intégré → mêmes changements faits par l'outil d'édition ;
2. ajout de l'essai m2 par document intégré suivi de pytest dans la même commande → ajout par l'outil d'édition, pytest seul ;
3. écriture de la sortie des essais par une commande composée → écrite par l'outil d'écriture, après lecture des deux sorties.

## 6. Ménage déclaré

Les dossiers vides `/root/bbis-t07-v1/traces` et `/root/bbis-t07-v1`, créés sur la machine de la session à 14:35 par l'ancien
essai de `lancer commande` (défaut m5), ont été retirés par `rmdir` (qui ne retire qu'un dossier vide) ; vérifié absents après
les deux passes d'essais neuves.

## 7. Réserves et ce qui reste avant `CODE-BBIS`

- **M2 sur la carte** : la répétition à blanc de mardi 17 doit jouer `entrainer` (famille linéaire et famille attention, double
  précision, algorithmes déterministes) sur « cuda » sur des jetons synthétiques, puis `controle_carte_processeur` ; résultat
  écrit avant `GO-BBIS`. Rien ici n'a tourné sur une carte.
- **Chaîne de l'amorce sur les vraies branches** : extraction, copies, commit local, propreté de l'arbre et branche de sortie
  depuis COMMIT ne sont éprouvés que sur des dépôts jetables ; la répétition à blanc doit les jouer (version de git de l'image
  au moins 2.34 pour `add --sparse`, déjà exigée par les poussées).
- **Seconde lecture courte du différentiel** `ffde97be..189868e6` par un lecteur neuf (point 4 de la contre-lecture) : à faire.
- `CODE-BBIS` doit citer le commit corrigé (`189868e6` ou un descendant qui ne change pas le code) ; l'épreuve de niveau
  complète se joue sous l'entropie de cette ligne ; `MIN_ESSAIS` à recompter si un essai change d'ici là.

## 8. Empreintes neuves (SHA-256, commit `189868e6`)

| fichier | empreinte |
|---|---|
| `scripts/amorce_bbis_v1.sh` | `a91817a66d36fbae025aab992fd4298488e8d6b918e5339561230892ff40dc88` |
| `scripts/lancer_bbis_v1.sh` | `e34edcf35a19f282164695843b8a101516125869bec28c60e822f4e175223d67` |
| `src/controle_ia/t07bbis/lecture_v1.py` | `9d11ba2bcc7af34fd2ef81a9be4daebcbb744923905cf02cea401c55dd4a154c` |
| `src/controle_ia/t07bbis/marche_v1.py` | `018c0709f362e3abee7395fa72bca50d3bd223a43527f7b53d37712575de0a1e` |
| `src/controle_ia/t07bbis/registre_bbis_v1.py` | `cee62b1f0154c6245ae00e7958024de8e399bef2889651211209f107bc8b36ea` |
| `tests/aide_t07bbis_depot_v1.py` (neuf) | `9053799df1ddcff07eba1dff1bc39cb381fd8de73fe76187bcaa76824e0ec07b` |
| `tests/test_t07bbis_chaine_instance_v1.py` (neuf) | `f7884ffe43502ffa58f3abbcd25d3e3fd18ed6c4ca20d936cd5bfcb3e62a4b65` |
| `tests/test_t07bbis_bout_en_bout_v1.py` | `228e87789aa9e0d7125aa7475adfb56836c039752f7f4bd767d5549b438da0d2` |
| `tests/test_t07bbis_lecture_v1.py` | `cbbc69cd4136d9b0576e576133ea761a7cc490a9cf18f3fcfbf51e37056aa04a` |
| `tests/test_t07bbis_registre_v1.py` | `9ec9965be3a5539e89f7f85f3bff9301ffb20227ad3c1f10ef63dfecf1c1c5ba` |
| `brouillons/T0.7-etape-B-bis-v1/code/essais-sortie-corrections-v1.txt` | `8bfdb66e8d06d05317666a832e467d905430ff40872adde8b0d77e335ee61fd9` |

Inchangés depuis `3f5a807d` : `commun_v1`, `validation_imbriquee_v1`, `apprentissage_carte_v1`, `plis_v1`,
`adversaires_texte_v1`, `etat_impose_v1`, `conjointe_v1`, `lien_mots_et_cout_v1`, `scripts/enumerer_issues_bbis_v1.py`,
`scripts/epreuve_niveau_deux_plis_bbis_v1.py` et les autres essais du paquet.
