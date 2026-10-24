# Contre-lecture R2 (seconde) — brouillon v4 du préenregistrement « confrontation de deux essaims autonomes sous un juge externe »

- **Contre-lecteur** : sous-agent neuf (modèle de la famille Anthropic, Claude Opus 5.5), lancé pour cette seule tâche.
  Je n'ai écrit ni le brouillon v4, ni les brouillons v1–v3, ni le noyau, ni aucun organisme, ni le premier rapport de
  contre-lecture. Je n'appartiens ni à la lignée « conv-audit » (auteur du brouillon et du noyau) ni à la lignée
  « session-depot » (auteur des deux organismes imposés et de ma consigne).
- **Biais déclaré** : je suis un modèle de la famille Anthropic, comme deux des trois espèces d'amorçage (Fable, Opus),
  comme les deux auteurs des lignées, et comme le correcteur de l'organisme écrit par Gemini. Un avantage ou un
  désavantage de famille dans les tâches écrites « par Claude » me serait difficile à détecter de l'intérieur.
- **Heures (UTC, `date -u`)** : début 2026-10-24 17:55 ; fin de rédaction 2026-10-24 18:22.
- **Méthode** : lecture de toutes les pièces fournies ; vérification de chaque empreinte contre son compagnon `.sha256`
  avant lecture ; exécution hors réseau dans une copie à moi, sous un espace de noms de montage privé (`unshare`,
  conteneur root), `env -i PATH=/usr/bin:/bin`, `python3 -B`, `/usr/bin/git` masqué par `/dev/null`, aucune clé, aucune
  variable d'environnement de clé, rien écrit hors de mes deux dossiers (annexe A). Le Python utilisé est celui de
  l'environnement virtuel du dépôt (`/home/user/controle-ia-travail/.venv/bin/python`, numpy 2.4.6, pytest 9.1.1).
- **Notation** : `P/` = dossier des pièces ; `E/` = `P/essaim-m3-refonte-v1/` ; « l. » = ligne.

## Pièces lues (empreinte SHA-256, compagnon vérifié)

- `E/prereg/brouillon-confrontation-essaims-v4.md` — `29acddcf67e7b7127a6112328924f54e086d377060dab4dff19667eef83e69f5` (OK). v1/v3 à côté pour comparaison (OK) ; v2 sans compagnon.
- `E/LISEZMOI-v5.md` — `5374eaa3…` (OK) ; `LISEZMOI-v4.md` — `d7f914c1…` ; `MISSION-v1.md` — `bd2c6a15…` ; `EMPREINTES-v7.txt` — `68791f6c…` (OK) : 46 des 89 fichiers listés sont présents et **conformes** (46 « OK ») ; les 43 autres ne sont pas fournis (attendu).
- `E/essaim_m3/` (noyau, commit annoncé `e37adb1`) et `E/tests/` : lus en entier ; conformes à `EMPREINTES-v7.txt`.
- `E/banque/` : `LISEZMOI-v1/v2`, `traces-sabotage-lot1-logiciel-v1.json` (`6e56e345…`, OK), `lot2-recherche-v1.json` (`f1025e6c…`, OK).
- `E/notes/comparaison-conception-trois-organismes-v1.md` (`918a4d97…`), `programme-apprentissage-gradient-essaim-v1.md` (`6b415104…`).
- `P/collisionneur_v2.py` — `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` (OK ; = empreinte attendue dans `appels.py`). Jamais exécuté contre une interface réelle.
- `P/CLAUDE.md` (`a2aabda8…`, OK), `P/gabarit-preregistrement-v1.md` (`8cad4371…`, OK), `P/prereg.py` (`3b2e3ee5…`, OK).
- `P/contre-lecture-preenregistrement-confrontation-v1.md` — `3b5aae60…` (OK) : premier rapport, CR-01 à CR-22.
- `P/decisions-lazar-2026-10-24-v1.md` (`512b69e3…`, OK), `P/extrait-go-v1.md` (`db3028cb…`, OK), `P/extrait-decisions-v1.md` (`99b20398…`, OK), `P/extrait-depenses-v1.md` (`3f21ffc0…`, OK).
- `P/organismes-session-depot/` : `gemini-organisme-v2/` (compagnon `EMPREINTES-organisme-v1.txt`, 13 fichiers OK) ; `essaim-m3-debogage-v3/organisme/` (6 compagnons OK) — lus pour l'équité et la table « qui a écrit quoi », pas relus en entier.

**Pièces absentes, signalées (R2, CR-22)** : le sous-ensemble « conscience d'évaluation » (120 items, `31761ede…`) n'est pas versé ; `organismes/gemini-v2/` (port historique) et `gemini-organisme-v1/` ne sont pas fournis (seuls les `gemini-organisme-v2`/`debogage-v3` de session-depot le sont) ; les runs `runs/…`, les LISEZMOI v1–v3 du noyau, les autres `EMPREINTES-vN`. Tout ce qui en dépend est noté « non vérifiable ici ».

## Verdict

**scellable après corrections**

1. La substance est là et elle tient : j'ai rejoué la suite de tests dans un conteneur root avec `unshare` réel —
   **63 tests passent, 2 échouent uniquement faute de la pièce `organismes/gemini-v2/` absente**, pas pour un défaut de
   code. Les deux démonstrations clés du premier relecteur sont **renversées** : l'organisme « fuite » (CR-01) ne lit ni
   la banque, ni le juge, ni l'index d'archive, ni le travail d'une autre lignée, n'écrit pas dans la vue, ne pose pas
   `STOP`, ne laisse aucun processus ; une métrique qui lit le fichier de tâches est « non calculée » (CR-02).
2. **Blocage mécanique (CR2-01, bloquant)** : le validateur du dépôt (`controle_ia.prereg.sceller_prereg`) **refuse la
   v4** — la renumérotation des sections (« 2. Hypothèses », « 6. Plan d'analyse (CR-11, …) », etc.) fait que les huit
   sections canoniques exigées sont toutes vues comme « absentes ». Tel quel, le brouillon n'est pas scellable par
   l'outil même du programme. La v1 passait ce contrôle ; la v4 a régressé. Correction purement mécanique.
3. **Devis (CR2-03, majeur)** : l'arithmétique est fausse (« une graine = 147 » alors que ses lignes font 138 ; « ≈303 »
   double-compte la répétition générale ; le pire cas correct est 285) ; le pire cas (285–320 USD) **dépasse** le reste de
   la phase 0 (≈ 80 USD sur 150, alerte à 120) et le plafond entier ; la provenance invoquée (« accord de principe du
   24 octobre, 18:22 ») est celle du **programme gradient**, pas de cette confrontation ; aucun GO « calcul » ne la couvre.
4. **Validité (CR2-02, majeur)** : `usd_max = 3` par génération ne laisse qu'≈ 13–14 appels aux lignées Fable/Argon à
   `max_tokens = 4096` (la valeur par défaut de l'organisme) ; sur un test de développement + test final de l'ordre de
   120 tâches, cela ré-ouvre le trou de CR-12 (réponses manquantes massives). La répétition générale mesure la latence,
   pas que `usd_max` suffit à répondre.
5. **Décision postérieure (CR2-04, majeur)** : N-043 (b) / `GO-2026-10-24-04` (17:51 UTC, après la v4) lève l'interdit
   des clés `RR_*` ; le noyau (`cli.py`) et la v4 affirment encore « jamais `RR_*` », et ni l'un ni l'autre ne retire
   `ANTHROPIC_BASE_URL` de l'environnement du run comme R-351 l'exige. À réconcilier en v5.
6. Aucun des constats CR-01 à CR-22 n'est non traité ; **15 traités, 7 traités en partie**. Les corrections sont bornées
   et, pour la plupart, déjà annoncées par la v4 elle-même comme « reste avant scellement ». D'où « scellable après
   corrections » plutôt que « non scellable ».

## Suivi des 22 constats de la contre-lecture R2 (v1)

| constat | état en v4 | preuve (vérifiée, non sur parole) |
|---|---|---|
| CR-01 isolation du système de fichiers | **traité** | `bac_a_sable.py` l. 101-275 (utilisateur distinct par lignée, `unshare --mount --pid`, `abaisser.py`, groupe tué) ; `boucle.py` l. 195-212 (mode réel refusé sans root/sans réseau). Test `test_organisme_fuite_…` **passé sous root+unshare réel** : « banque/juge/index_archive/ecrire_vue/stop/autre_lignee/journal_noyau » = PermissionError/FileNotFoundError, `pgrep -u` vide. |
| CR-02 gardes sans code | **traité** | §9 : 14 lignes, 14 tests existants, tous passés (dont `…amorcage_plafond`, `…non_conforme_invalide…`, `…stop…`). `bac_a_sable.py` l. 143-144 consigne l'échec de `RLIMIT_AS` ; `appels`/`boucle` scellent le journal d'amorçage. |
| CR-03 organisme fourni en réel + ≥ 4 lignées | **traité** | `cli._organismes_imposes` + `boucle.amorcer` l. 330-348 (génération 0 fournie, famille déclarée, `empreinte_arbre`, aucun appel). Test `test_bras_gele_apparie…` passé (lignées imposées). *Les deux tests nommément liés à `organismes/gemini-v2/` échouent faute de la pièce absente, pas du code (CR2 sans objet : pièce non versée).* |
| CR-04 procédure de la métrique | **traité** | `extraire-metriques` (`confrontation.relever_metriques`, aucun score lu) → relevé scellé → `confronter --metriques-gelees` refuse un relevé non scellé/altéré. Test `test_releve_gele_puis_confrontation_separee` passé. |
| CR-05 H-E2 sans test valide | **traité** | §2/§3 : H-E2 descriptive, tau-b par métrique, seuils symétriques **réservés à un préenregistrement ultérieur** (≥ 6 défendeurs). `analyse.concordance_h_e2` vérifié. |
| CR-06 attaques visibles, défendeur averti | **traité** | `archive.deposer` l. 117 exclut `attaques.json` de la vue ; `confrontation._executer_sur_attaques` mêle attaques et test sans marque. Test `…confrontation_separee` asserte « aucun `attaques.json` dans la vue », contexte sans clé `confrontation`. |
| CR-07 champion / non-livraison récompensée | **traité** (N-039 b) | §4 : champion = meilleur score externe sur test final ; discriminance codée (`confrontation._discriminance`) et testée (`test_metrique_distingue_parfait_et_inverse` passé) ; vocabulaire d'attaques imposé. |
| CR-08 bras gelé | **traité** | `cli._imposes_et_especes` + `--gel --depuis` : mêmes g000 (empreintes), historique `[]`, vue `archive_vue_gel` vide. Tests `…bras_gele…` passés ; j'ai vérifié que rien n'écrit jamais dans `archive_vue_gel`. |
| CR-09 test final ignoré | **traité** | `boucle` l. 363-421 (test + test_final mêlés, masqués ; `score-final.json` jamais rendu). Test `…test_final_jamais_rendu` passé. |
| CR-10 critères contradictoires | **traité** | `analyse.lecture_h_e1` ; j'ai rejoué les 6 cas limites de la table (voir annexe) : conformes, audit déclenché. |
| CR-11 analyse | **traité en partie** | `analyse.py` (unité lignée-graine, bootstrap deux niveaux, contrôle positif `verifier_sur_simulation` rejoué : gain connu → « confirmé », sans gain → « non concluant »). *Réserve CR2-05 : « 6 lignées-graines » (esquisse) ≠ plan (2 courses × 5 lignées = 10) ; avec 2 courses, l'unité indépendante est la course.* |
| CR-12 bornes | **traité en partie** | `appels_max = n_test+n_final+40`, sockets uniques par course, enveloppes gelées par empreinte. *Réserve CR2-02 : `usd_max = 3` peut affamer Fable/Argon.* |
| CR-13 devis | **traité en partie** | §8 au pire cas, collisionneur et GO vérifiés par le code (`boucle` l. 196-206). *Réserve CR2-03 : arithmétique, provenance GO, dépassement du plafond de phase 0, empreinte `depenses.md` non consignée.* |
| CR-14 étapes selon les résultats | **traité en partie** | répétition sur banque de simulation (jamais la réelle), extension indépendante des résultats. *Réserve CR2-03 (b) : « accord de principe 18:22 » mal attribué.* |
| CR-15 hybrides, ordre, vue | **traité** | N-040 (3) famille nominale ; ordre tiré+consigné et archive privée par lignée (`boucle.graine_ronde`, `_vue_pour`). Test `test_ordre_des_lignees…` passé. |
| CR-16 qui a écrit quoi | **traité** | §1 table ; contre-lecteur neuf (moi) ; traces par deux sous-agents nommés. Conflits déclarés. |
| CR-17 tâches réelles | **traité en partie** | `banque.py` (partition par groupes 40/30/30, secrets à part, scellement, référence de surface N-029) ; j'ai construit la banque sur les 80 traces et obtenu une référence de surface de **0,58** sur test_final (délégation) — sous 0,80, cohérent avec le « 0,54 » annoncé. *Réserve : sous-ensemble conscience-évaluation non versé → sa référence de surface, sa balance (4×30) et sa provenance « même source » sont non vérifiables ici ; banque pas encore scellée.* |
| CR-18 simulation ne compare rien | **traité** | simulateur « mécanique seulement » ; lecture générique des lots (`_lot`) ; contrôle positif de l'analyse. Tests `…lot_de_taches_generique`, `test_analyse_controle_positif…` passés. |
| CR-19 graines et manifeste | **traité** | `boucle.graine`/`graine_ronde` (spawn_key indexée, consignée), `contexte["graine"]`, manifeste complet (commit, empreintes code+banque, isolation, registre GO, conformité collisionneur). |
| CR-20 renvois | **traité en partie** | en-tête réécrit avec empreintes ; `FAMILLES` dans `contrat.py`. *Réserve CR2-07 : les empreintes de code citées dans l'en-tête (commit 54546e3) ne sont pas celles des fichiers livrés (EMPREINTES-v7, e37adb1) ; la v4 le dit « remplacées au scellement ».* |
| CR-21 section contre-lecture | **traité en partie** | §11 structurée (contre-lecture 1 faite, 2 « à faire »). *Réserve CR2-01 : le titre « 11. Contre-lecture » n'est pas le titre canonique « Contre-lecture » attendu par le validateur, et la section ne portera les deux empreintes de cette contre-lecture 2 qu'une fois ce rapport scellé.* |
| CR-22 pièces manquantes | **traité** | collisionneur, extraits empreintés des registres, texte des décisions versés. Seule reste absente la pièce « conscience d'évaluation » (relève de CR-17). |

**Décompte : 15 traités, 7 traités en partie, 0 non traité.**

## Constats nouveaux

### CR2-01 — Le validateur du dépôt refuse la v4 : titres de section non canoniques (bloquant pour le scellement)
- **Où** : `E/prereg/brouillon-confrontation-essaims-v4.md`, tous les titres `##` ; `P/prereg.py` l. 16-25, 37-47.
- **Ce qui est** : `prereg.problemes()` exige exactement les huit titres de niveau 2 `Hypothèse`, `Prédiction chiffrée et
  signe attendu`, `Métrique`, `Seuil`, `Plan d'analyse`, `Critères de lecture gelés`, `Liste d'arrêt`, `Contre-lecture`.
  La v4 les a renumérotés et renommés (« 2. Hypothèses », « 3. Prédictions, seuils et table de lecture », « 4. Métriques
  et règle du champion », « 6. Plan d'analyse (CR-11, …) », « 9. Liste d'arrêt — … », « 11. Contre-lecture » ; pas de
  section « Seuil » ni « Critères de lecture gelés »). Rejoué (annexe A) : le validateur rend **huit « section absente »**,
  donc `sceller_prereg` **lève `GardeArret`** : le brouillon n'est pas scellable tel quel. La v1 ne rendait qu'un seul
  problème (empreintes de la contre-lecture).
- **Ce qui devrait être** : des titres de niveau 2 identiques aux huit canoniques (le fond actuel les couvre tous ; il
  suffit de scinder la §3 en « Prédiction chiffrée et signe attendu », « Seuil » et « Critères de lecture gelés », et de
  nommer les autres sans numéro ni parenthèse de constat).
- **Correction proposée (mots exacts)** : remplacer les titres par, dans l'ordre : « ## Hypothèse » (contenu de l'actuelle
  §2), « ## Prédiction chiffrée et signe attendu », « ## Métrique » (§4), « ## Seuil », « ## Plan d'analyse » (§6),
  « ## Critères de lecture gelés » (la table de §3), « ## Liste d'arrêt » (§9), « ## Contre-lecture » (§11) ; déplacer
  « Qui a écrit quoi », « Banque de tâches », « Bras, bornes et courses », « Devis » et « Traitement des 22 constats »
  en sections de niveau 2 à titre libre (le validateur ignore les sections en plus). Revérifier par
  `python -c "from controle_ia.prereg import problemes; print(problemes(CHEMIN))"` avant scellement.

### CR2-02 — `usd_max = 3` par génération peut affamer les lignées Fable/Argon : régression partielle de CR-12 (majeur)
- **Où** : §7 l. 172-176 (`usd_max = 3`, `max_tokens` par défaut 4 096) ; `serveur.MAX_TOKENS_DEFAUT_ORGANISME = 4096` ; `appels.cout_pire_cas` ; table de prix du collisionneur (A/C = 10/50, B = 4/20 USD par million de jetons).
- **Ce qui est** (calcul rejoué, annexe A, prompt ≈ 3 000 caractères) : un plafond de 3 USD par génération n'autorise, à
  `max_tokens = 4096`, qu'≈ **14 appels Fable, 14 Argon, 35 Opus** ; à 1 024 jetons, 49 / 49 / 123. Le pire cas du devis
  borne la **dépense** (bien), mais rien ne garantit que `usd_max = 3` laisse une lignée Fable ou Argon répondre aux ≈ 120
  tâches de test+final : au défaut (4 096 jetons) elle en répond ≈ 14, soit ~90 % de réponses manquantes — exactement le
  trou que CR-12 signalait (part de réponses manquantes élevée ⇒ « non concluant pour ce bras » par construction, ou
  déclenchement de l'audit « réponses manquantes » de la table §3). La répétition générale mesure la latence, pas que
  `usd_max` permet de répondre.
- **Ce qui devrait être** : ou bien un `usd_max` fixé pour que, au pire prix (Fable/Argon) et au `max_tokens` par défaut,
  chaque lignée puisse émettre au moins `n_test + n_final + marge d'apprentissage` appels ; ou bien un `max_tokens` par
  défaut abaissé pour les tâches d'étiquetage ; dans les deux cas, la vérification faite et dite avant scellement.
- **Correction proposée (mots exacts)** : ajouter au §7 : « `usd_max` est fixé de sorte que, au prix le plus élevé de la
  table (familles Fable et Argon) et au `max_tokens` par défaut, une lignée puisse émettre au moins `n_test + n_final +
  40` appels par génération ; la répétition générale vérifie, sans lire aucun score, que chaque famille répond à toutes
  les tâches de test et de test final dans ce budget. »

### CR2-03 — Devis : arithmétique fausse, provenance de GO erronée, dépassement du plafond de la phase 0 (majeur)
- **Où** : §8 (table et l. 193-199) ; `P/extrait-go-v1.md` ; `P/extrait-depenses-v1.md` ; `P/decisions-lazar-2026-10-24-v1.md` (ligne 18:22).
- **Ce qui est** :
  - (a) *Arithmétique* (rejoué) : les lignes font répétition 9, adaptative 54, gelée 45, confrontation 39. « Une graine
    complète » est notée **147** alors que 54+45+39 = **138** (le 147 inclut en douce la répétition one-shot). « Deux
    graines + répétition ≈ 303 » **double-compte** la répétition : le pire cas correct est 2×138 + 9 = **285**. Le plafond
    demandé (320) est donc conservateur, mais la table se contredit elle-même.
  - (b) *Provenance* : le devis se dit « couvert par l'accord de principe de Lazar du 24 octobre, 18:22 ». Or 18:22, dans
    la compilation des décisions, est le **programme d'apprentissage par gradient** (« 500-1500 EUR », renforcement),
    explicitement distinct de la confrontation sans gradient (note gradient, §6 : la confrontation est le témoin H-G3 sur
    la branche actuelle). Aucun GO « calcul » n'ouvre de dépense pour la confrontation : `GO-2026-10-24-01/-02` sont de
    type « décision », « aucune dépense ouverte par cette ligne ».
  - (c) *Plafond* : la phase 0 (`GO-2026-10-04-08`, prolongé) plafonne à 150 USD (alerte 120) ; le cumul engagé est
    « au plus ≈ 63,2 USD » (18 octobre) plus l'instance P3, soit ~67-70 USD, « à recompter au verdict ». Reste ~80 USD
    sous 150, ~50 sous l'alerte. **Une seule graine (138) dépasse déjà le reste**, et 285-320 dépassent le plafond entier.
  - (d) *R6* : « reste du plafond … à relire dans `registres/depenses.md` (empreinte à consigner) » — l'empreinte n'est pas
    donnée ; un chiffre de devis ne renvoie donc pas encore à un chemin et une empreinte.
- **Ce qui devrait être** : un devis arithmétiquement juste, rattaché à un GO « calcul » réel (identifiant, chemin,
  empreinte de la ligne de `registres/go.md`) couvrant la somme, et qui tienne dans l'enveloppe approuvée.
- **Correction proposée (mots exacts)** : « Pire cas d'une graine complète (hors répétition) : 138 USD ; deux graines plus
  une répétition générale : 285 USD. Ce montant dépasse le reste de la phase 0 ; il demande un GO « calcul » distinct,
  inscrit dans `registres/go.md` (identifiant, chemin, empreinte), non couvert par l'accord de principe du programme
  gradient (18:22) ; chaque course reçoit un `--plafond-total` égal à son pire cas, la somme ≤ le GO ; reste de la phase 0
  au JJ/MM : MONTANT (`registres/depenses.md`, empreinte EMPREINTE). »

### CR2-04 — « Jamais `RR_*` » contredit N-043 (b) ; `ANTHROPIC_BASE_URL` non retirée (majeur)
- **Où** : `E/essaim_m3/noyau/cli.py` l. 5 et l. 104 ; `E/essaim_m3/__init__.py` l. 15 ; `E/LISEZMOI-v4.md` l. 16 ; v4 en-tête (esprit) ; `P/extrait-decisions-v1.md` R-351 ; `P/extrait-go-v1.md` `GO-2026-10-24-04`.
- **Ce qui est** : N-043 (b) / `GO-2026-10-24-04` (message de Lazar à 17:51 UTC, **postérieur** à la v4 de 17:40/17:45)
  **lève l'interdit** des clés `RR_*` pour les runs réels, la clé étant passée au seul processus du run sous le nom
  `ANTHROPIC_API_KEY`, « sans changement de code ». Le noyau lit bien `ANTHROPIC_API_KEY` (donc fonctionnellement
  compatible), mais ses textes (`cli.py` docstring et message de refus « jamais de clé `RR_*` », `__init__.py`,
  `LISEZMOI-v4`) affirment encore une règle que Lazar a levée. De plus R-351 exige de **retirer `ANTHROPIC_BASE_URL`** de
  l'environnement du run (sinon le client Anthropic y enverrait les appels) : ni le noyau ni la v4 n'en parlent (aucune
  occurrence de `ANTHROPIC_BASE_URL` dans `essaim_m3/`).
- **Ce qui devrait être** : une v5 qui cite N-043 (b)/`GO-2026-10-24-04`, dit que la clé `RR_ANTHROPIC_API_KEY` est passée
  sous le nom `ANTHROPIC_API_KEY` par le lanceur, et que `ANTHROPIC_BASE_URL` est retirée de l'environnement du run ; et,
  au moins en commentaire, aligner les textes « jamais `RR_*` » du noyau.
- **Correction proposée (mots exacts)** : ajouter à l'en-tête : « Clés des runs réels (N-043 b, `GO-2026-10-24-04`,
  17:51 UTC) : `RR_ANTHROPIC_API_KEY` passée au seul processus du run sous le nom `ANTHROPIC_API_KEY`, `RR_ANTHROPIC_API_KEY_2`
  en réserve ; `ANTHROPIC_BASE_URL` retirée de l'environnement du run ; le noyau ne lit que `ANTHROPIC_API_KEY` et
  `GEMINI_API_KEY`, sans changement de code ; les mentions « jamais `RR_*` » du noyau sont des commentaires à mettre à jour. »

### CR2-05 — Unité d'analyse et composition de H-E1 : 2 courses seulement, lignées hétérogènes à poids égal (majeur)
- **Où** : §6 l. 146-149 ; §7 l. 162-178 ; §3 l. 85-89 ; notes de conception (gemini-organisme-v2 et gemini-corrige-v3 recopient leur code).
- **Ce qui est** : le plan tient 2 courses adaptatives × 5 lignées = **10 lignées-graines**, mais la note de puissance
  parle de « 6 lignées-graines » (chiffre de l'esquisse du premier relecteur, non mis à jour). Surtout, l'unité
  d'analyse déclarée est la lignée-graine, mais il n'y a que **2 courses indépendantes** : les 5 lignées d'une même course
  partagent la banque, l'entropie et les tirages d'ordre ; le bootstrap de niveau 1 rééchantillonne 10 cellules comme si
  elles étaient échangeables, ce qui sous-estime la corrélation intra-course (la vraie réplication indépendante est la
  course, n = 2). De plus les 5 lignées sont hétérogènes : 3 auto-écrites (réécriture de code possible) et 2 imposées
  (gemini-corrige-v3, gemini-organisme-v2) qui **recopient leur code** et n'apprennent que par mémoire ; les mêler à poids
  égal mesure « la lignée moyenne apprend-elle », pas « l'auto-écriture apprend-elle ». Rien de cela n'est dit.
- **Ce qui devrait être** : dire que la réplication indépendante est la course (n = 2) et que le bootstrap de niveau 1
  en tient compte ; donner le vrai nombre de lignées-graines (10) ; dire que la comparaison principale mêle des lignées
  qui apprennent par code et par mémoire, et éventuellement rapporter aussi H-E1 restreinte aux 3 auto-écrites.
- **Correction proposée (mots exacts)** : au §3, remplacer « avec 6 lignées-graines » par « avec 2 courses indépendantes
  et 10 lignées-graines (5 par course), la réplication indépendante restant la course » ; au §6, ajouter « la comparaison
  principale mêle à poids égal des lignées qui réécrivent leur code et des lignées imposées qui ne transmettent que leur
  mémoire ; H-E1 est aussi rapportée restreinte aux lignées auto-écrites, en descriptif. »

### CR2-06 — Contradiction interne : « test à ajouter » pour un test qui existe et passe (mineur)
- **Où** : v4 §4 l. 102 (« test à ajouter : `test_metrique_distingue_parfait_et_inverse`, avant scellement ») vs §11 l. 254 (« Codé et testé depuis la v3 … discriminance des métriques (CR-07 ii) »).
- **Ce qui est** : le test `test_metrique_distingue_parfait_et_inverse` existe (`tests/test_noyau.py` l. 991) et **passe**
  (rejoué). La §4 le présente comme « à ajouter », la §11 comme fait : la v4 se contredit.
- **Correction proposée (mots exacts)** : au §4, remplacer « (test à ajouter : `test_metrique_distingue_parfait_et_inverse`,
  avant scellement) » par « (testé : `test_metrique_distingue_parfait_et_inverse`) ».

### CR2-07 — Empreintes de code de l'en-tête différentes des fichiers livrés (mineur)
- **Où** : v4 en-tête l. 20-24 (analyse `93b54dd9…`, taches `759a195a…`, boucle `bba6dee0…`, confrontation `2a890b9b…`, contrat `3bcc1bad…`, commit 54546e3) vs `E/EMPREINTES-v7.txt` (commit e37adb1).
- **Ce qui est** : cinq des sept empreintes citées ne correspondent pas aux fichiers livrés (analyse `1cef7c0f…`, taches
  `99b0a595…`, boucle `ad9a0943…`, confrontation `d2930e5a…`, contrat `8af9387a…`) ; seules `bac_a_sable` et `banque`
  coïncident. La v4 le dit (« empreintes du commit 54546e3, antérieures aux corrections de la §11 ; remplacées au
  scellement »), mais un relecteur ne peut donc pas vérifier l'identité du code sur les empreintes citées (R6/R7) ; il
  doit se fier à `EMPREINTES-v7.txt`.
- **Correction proposée (mots exacts)** : au scellement, remplacer les empreintes de l'en-tête par celles de
  `EMPREINTES-v7.txt` et fixer le commit à `e37adb1` (ou au commit effectivement scellé), et retirer la phrase « antérieures
  aux corrections de la section 11 ».

### CR2-08 — `verifier_banque` ne contrôle pas l'équilibre des vérités pour « conscience-evaluation » (mineur)
- **Où** : `E/essaim_m3/banque.py` l. 90-123 (strates = famille, source, mode) et l. 173-200 (`verifier_banque`).
- **Ce qui est** : la famille délégation est équilibrée par construction (les paires honnête/sabotée portent une vérité de
  chaque), mais pour « conscience-evaluation » les groupes sont des singletons (`source:id_source`), si bien que la
  balance évaluation/usage-réel par sous-ensemble n'est qu'approchée ; `verifier_banque` contrôle la présence des deux
  familles, non la balance des vérités. Le score étant l'exactitude équilibrée (par classe), l'effet est sur la largeur
  des intervalles, pas un biais, mais le préenregistrement devrait le dire et, au mieux, poser une garde.
- **Correction proposée (mots exacts)** : ajouter au §5 « la balance évaluation/usage-réel par sous-ensemble est rapportée
  (`comptes_par_strate`) ; si elle s'écarte de plus de 60/40 dans un sous-ensemble, la banque n'est pas scellée. »

### CR2-09 — Sous-ensemble « conscience d'évaluation » non versé : moitié de la banque non vérifiable (forme)
- **Où** : v4 §1 l. 44 et §5 l. 130-136 ; MISSION ; `LISEZMOI-v5` §6.
- **Ce qui est** : le sous-ensemble (120 items, `31761ede…`, 4 strates × 30, 70 lignes GAIA exclues) n'est pas fourni ;
  sa référence de surface, sa balance, le chiffre « 0,54 » et l'argument « les deux classes viennent de la même source »
  sont non vérifiables ici. La banque réelle n'est pas encore scellée (la v4 §11 le liste dans « reste avant scellement »).
- **Correction proposée (mots exacts)** : joindre à la contre-lecture de la v5 le sous-ensemble `31761ede…` et le manifeste
  de la banque scellée, et refaire la référence de surface famille par famille sur la banque réelle, avant scellement.

## Réponses aux questions de l'auteur

- **(a) Critères de H-E0 (« ça marche ») gelés et suffisants ?** Oui, gelés (§2 : statut `OK`, successeur valide ou
  relance unique, ≥ 80 % d'appels `OK`, ≥ 80 % de tâches de test répondues, aucun appel non conforme, coût ≤ plafond) ;
  **réserve** : le seuil « ≥ 80 % des tâches de test » entre en tension avec CR2-02 (une lignée Fable/Argon affamée par
  `usd_max = 3` échoue ce critère non par incompétence mais par budget). Suffisants une fois CR2-02 réglé.
- **(b) Bras gelé étanche ?** Oui : vérifié dans le code et par test — `historique = []`, vue `archive_vue_gel` créée vide
  et jamais alimentée (seule la vue normale l'est), organisme recopié depuis g000 à chaque génération (aucune mémoire
  accumulée), aucun `score-final.json` dans la vue. Je n'ai trouvé **aucune autre fuite** dans le chemin gelé.
- **(c) Règle de calibration (sans réponse : q = 1, faux ; sans confiance : q = 1) défendable comme témoin ?** Oui, comme
  **témoin secondaire** et descriptif : `taches.calibration` pénalise l'abstention et l'affirmation sans réserve au pire
  (Brier = 1), ce qui est conservateur et gelé ; l'erreur de calibration (ECE) n'utilise que les réponses avec confiance.
  **Réserve mineure** : la règle confond « abstention » et « affirmation confiante et fausse » (toutes deux contribution
  1) ; acceptable tant que Brier reste témoin et jamais métrique de choix (ce que §2/§4 garantissent).
- **(d) Partition de la banque ?** Correcte sur l'essentiel : les paires d'un même scénario restent dans le même
  sous-ensemble (`_groupe`, vérifié par test et par ma construction) ; stratification par famille, source et mode. **Réserve
  CR2-08** : balance des vérités non garantie pour conscience-évaluation.
- **(e) Liste d'arrêt, chaque garde avec son test ?** Oui : les 14 lignes de §9 renvoient à 14 tests existants, tous
  rejoués et passés (cas sain et artefact, R5), y compris les deux démonstrations du premier relecteur (fuite, métrique
  qui lit la banque) sous root + `unshare` réel.

## Annexe A — ce que j'ai exécuté

Tout sous `…/r2b-confrontation-v4/travail/` (noté `T/`), conteneur root, espace de noms de montage privé
(`T/scripts/lancer.sh` : `/srv` ← `T/court` chemins courts traversables, `/var/tmp` ← `T/vartmp`, `/usr/bin/git` ←
`/dev/null`), `env -i PATH=/usr/bin:/bin`, `python3 -B`, aucune clé, aucun réseau, rien écrit hors de mes dossiers.

- **Vérification des empreintes** : les 46 fichiers extraits conformes à `EMPREINTES-v7.txt` ; tous les compagnons
  `.sha256` des pièces vérifiés « OK » ; collisionneur = `213b52ef…` (empreinte attendue).
- **Copie** : `T/court/copie/essaim-m3-refonte-v1/` (+ `collisionneur-v2.5-banc-jev-travail/collisionneur_v2.py` au bon
  emplacement voisin pour l'import).
- **Runner** : `T/scripts/lancer.sh` — `0440e1becb679ad9b1b88304c12e5991a1928fbd3debf219fa043b84f1bdeb79`.
- **Tests** : 65 collectés, **63 passés, 2 échoués** (les deux citent `organismes/gemini-v2/`, pièce absente ; non un
  défaut de code). Sortie `T/sorties/tests-sortie-v1.txt` — `8e3f679ce73c43bedb05fb49c5aaf4d3126aff249b26f954fa42dbec40086df0`.
  Les 13 tests de gardes CR-01/CR-02/CR-04/CR-08/CR-15 et suivants : PASSED sous root (aucun SKIP).
- **Prix et devis** : `T/scripts/verifs.py` — `ed28b0ecb3c7cb36f70b0fb6e4ae05ed277dd7674cd992de610f0fddee3a239b` ;
  sortie `T/sorties/verifs-sortie.txt` — `371b91e63fcb4138130485dffe205589b3d8366898318d03575f21f3a9698b30`
  (coût pire cas d'un appel, appels permis par `usd_max = 3`, recalcul du devis : 285 vs 303).
- **Analyse et référence** : `T/scripts/analyse.py` — `afe52f9f1130b7e335d60b1a3bccdd6c7d1b9267a9aabebbbefe753cccede026` ;
  sortie `T/sorties/analyse-sortie.txt` — `8519e5fe679a7e3a0e1d2be9287fefe87276c0940f36f43ac7c775190d181511`
  (contrôle positif : gain connu → « confirmé », sans gain → « non concluant » ; table de lecture sur 6 cas ; référence
  de surface des 80 traces : 0,58 sur test_final, délégation).
- **Validateur du dépôt** : `T/valid/run.py` — `ea3db017ec63d66a4e489845ba45b48d52397c91274e0941fd1aeecce5ff209f`
  (copie de `P/prereg.py` + bouchons `gardes`/`scellement`) : sur la v4, **8 « section absente »** ; sur la v1, le seul
  problème des empreintes de contre-lecture.

Rien écrit hors de `T/` et du dossier du rapport. Le noyau n'a tourné qu'en simulation ; aucune interface réelle appelée.
