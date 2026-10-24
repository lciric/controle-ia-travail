# Contre-lecture R2 (troisième) — brouillon v6 du préenregistrement « confrontation d'essaims autonomes sous un juge externe »

- **Contre-lecteur** : sous-agent neuf (modèle de la famille Anthropic, Claude Opus 5.5), lancé pour cette seule tâche.
  Je n'ai écrit ni ce brouillon, ni les brouillons v1 à v5, ni le noyau, ni aucun organisme, ni les deux contre-lectures
  précédentes de la confrontation, ni celle de l'étape 1 du programme « gradient ». Je n'appartiens ni à la lignée
  « conv-audit » (auteur du brouillon et du noyau) ni à « session-depot » (lanceur, lignées imposées).
- **Biais déclaré** : je suis un modèle de la famille Anthropic, comme deux des trois espèces d'amorçage (Fable, Opus),
  comme l'auteur du code et des traces de sabotage, et comme le correcteur de l'organisme écrit par Gemini. Un avantage
  ou un désavantage de famille dans les textes « écrits par Claude » me serait difficile à détecter de l'intérieur.
- **Heures (UTC, `date -u`)** : début 2026-10-24 19:43 ; fin de rédaction 2026-10-24 20:26.
- **Méthode** : vérification de toutes les empreintes compagnon ; lecture du texte, des sections conception/moisson, du
  code au commit `e82c341` (via `EMPREINTES-v8.txt`), des tests, des deux rapports précédents, des registres, des
  messages n° 12 à 18, de la documentation de la banque et du collisionneur. Exécution hors réseau dans une **copie** à
  moi, conteneur root, espace de noms de montage et de réseau privé (`unshare --mount --net`), `env -i`,
  `/opt/essaim-m3-venv-v1/bin/python -B` (numpy 2.4.6, pytest 9.1.1). Aucune commande git d'écriture, aucun réseau vers
  une interface de modèle ni une source de moisson, aucune clé lue, aucun script de la relève de Gemini exécuté, aucun
  processus laissé derrière (vérifié `pgrep -u 60000..60010`). Rien écrit hors de `…/r2-confrontation-v6/travail` et
  `…/rapport`.
- **Notation** : `P/` = dossier des pièces ; `E/` = `P/essaim-m3-refonte-v1/` ; « l. » = ligne.

## Empreinte du texte relu

- `E/prereg/brouillon-confrontation-essaims-v6.md` — **`0ce8c3963805625ae75c954a63a2342d7bb125caa3b7fcdabf9b9b8a3cce05f2`** (compagnon `.sha256` : OK, empreinte
  attendue `0ce8c396…` confirmée).
- `E/prereg/sections-conception-moisson-v1.md` — `180a39af…` (OK). `E/EMPREINTES-v8.txt` — `eda52e16…` (OK) ; les
  **80 fichiers de code** qu'il liste et qui sont fournis sont tous conformes (80 « OK ») ; les 35 manquants sont les
  données, les organismes de la relève et les sorties de simulation, retirés exprès. `P/collisionneur_v2.py` —
  `213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd` (= empreinte attendue dans `appels.py` et dans
  l'en-tête de la v6). `P/CLAUDE.md`, `P/prereg.py`, `P/gabarit-preregistrement-v1.md`, les deux rapports précédents,
  la compilation des décisions, l'extrait des registres, le résumé de banque : tous compagnons OK.
- Les 14 empreintes de code citées en en-tête de la v6 (analyse, banque, simulateur, 11 fichiers du noyau, juge)
  correspondent toutes aux fichiers livrés (CR2-07 traité).

## Verdict

**scellable après corrections**

1. La substance tient et les acquis des v1–v5 sont réels. J'ai rejoué la suite de tests en conteneur root avec
   `unshare` réel : **74 passent, 1 sauté (réseau arXiv coupé), 5 échouent uniquement faute des pièces absentes**
   (`organismes/gemini-v2/`, les fichiers `banque/*.json` non fournis), pas pour un défaut de code. Le validateur du
   dépôt (`controle_ia.prereg.problemes`) ne rend **aucun problème** sur la v6 (CR2-01 traité, rejoué). Isolation
   (CR-01), relevé gelé (CR-04), vue sans `attaques.json` (CR-06), bras gelé apparié (CR-08), phase de conception,
   moisson, double désignation : tous outillés et testés, vérifiés par exécution.
2. Mais cinq points **majeurs** restent, dont trois sont des écarts code ↔ texte que les ajouts de la v6 n'ont pas
   refermés et un que la v6 a elle-même introduit : le **devis de la confrontation** contredit le mécanisme de
   réservation du noyau (CR3-01) ; la règle **N-039 b du champion** retient le score d'une génération **invalidée**, pas
   de la dernière valide (CR3-02) ; **H-E3 sur les défenses** n'est pas outillée (journaux non scellés, non comptés —
   CR3-03) ; une **ligne de la liste d'arrêt est « à écrire »** alors que la panne qu'elle couvre est actuelle (crédit
   Gemini épuisé — CR3-04) ; la **réponse à CR2-05** (cohérence de signe par course) ne corrige pas la sous-estimation
   de l'intervalle de H-E1 (CR3-05).
3. Aucun blocage dirimant : les cinq bloquants du premier relecteur sont traités et re-vérifiés (fuite, gardes, bras
   gelé, métrique, H-E2 descriptive). Les corrections sont bornées ; deux touchent le code, les autres le texte et le
   devis. D'où « scellable après corrections ».

**Décompte : 0 bloquante, 5 majeures, 5 mineures, 2 de forme.**

---

## Corrections

### Majeures

**CR3-01 — majeure — le devis de la confrontation contredit le mécanisme de réservation du noyau ; le plafond demandé ne couvre pas le pire cas.**
- **Où** : v6 § « Devis au pire cas et GO » l. 240-253 (règle « pire cas = somme des plafonds de ses appels … défenses »
  ; ligne « confrontation (12 paires applicables × défense de 60 tâches + 6 attaques au pire cas, 15,1) | 181,2 » ;
  « une graine 1 697,5 » ; « plafond demandé 3 520 ») ; `confrontation.py` l. 191, 197, 207 ; `boucle.Noyau.recharger`
  l. 97-98 (`plafond_total_usd` relu du manifeste, dépense cumulée).
- **Ce qui est** (rejoué, `travail/scripts/audit_defense.py`, `calcul_devis.py`) :
  - le noyau donne à **chaque défense** le budget **entier** d'une génération : `appels_max = 160`, `usd_max = 37`
    (constaté : `budget_defense = {appels_max:160, usd_max:37.0, …, recherches_max:0}`). Le pire cas d'une défense est
    donc **37 USD** (plafond de réservation sur 160 appels), pas 15,1. Le « 15,1 » vaut 66 appels × 0,231 (60 tâches +
    6 attaques), mais le serveur ne borne pas le défendeur à 66 appels : il peut en émettre 160. La ligne confrontation
    au pire cas est **12 × 37 = 444**, pas 181,2 ; elle contredit la règle que la v6 énonce elle-même deux lignes plus
    haut (« amorçages au max du modèle, rondes, générations, défenses »).
  - la confrontation n'est **pas une course distincte** : elle tourne sur la course adaptative rechargée
    (`confronter` → `recharger`), dont `--plafond-total` vaut celui du manifeste (961,3) et dont la dépense cumulée
    inclut déjà amorçage + conception + générations. Au pire cas, la course adaptative atteint 961,3 (6,3 + 400 + 555) :
    il ne reste **rien** pour la confrontation, qui serait coupée par le plafond (`PLAFOND`), avec le biais d'ordre des
    paires (CR-13 e du relecteur n° 1) puisque l'ordre des paires n'est pas tiré. Le devis additionne pourtant
    « 961,3 + 181,2 » comme deux postes séparés, ce qu'aucun mécanisme ne réalise.
  - conséquence arithmétique (rejoué) : avec la défense à 37, pire cas d'une graine = 961,3 + 444 + 555 = **1 960,3** ;
    deux graines + répétition = **≈ 4 038 USD** > plafond demandé **3 520**. La règle « somme des plafonds ≤ GO » n'est
    pas tenue une fois la confrontation correctement imputée.
- **Correction proposée** : ou bien donner à la course adaptative un `--plafond-total` qui couvre explicitement la
  confrontation (961,3 + 12 × 37 = 1 405,3), recalculer le total (≈ 4 038) et demander ce GO ; ou bien plafonner la
  défense (budget propre de confrontation, par ex. `appels_max` réduit) et dire ce plafond dans le texte ET dans le
  code. Refaire la ligne « confrontation » au vrai pire cas (37/défense) et réconcilier « une graine » et « plafond
  demandé ». Dire comment la confrontation reçoit un budget dans `recharger` (le code n'accepte pas de `--plafond-total`
  à la confrontation : il relit celui du manifeste).

**CR3-02 — majeure — le champion (N-039 b, « la règle qui décide ») retient le score d'une génération invalidée, pas de la dernière génération valide.**
- **Où** : v6 § « Métrique » l. 86 (« la lignée de plus grand score témoin à sa **dernière génération valide** ») ;
  `confrontation.designations_et_concours` l. 116 (`temoin = {l: v[-1] …}`) via `boucle.Noyau._scores_finaux`
  l. 627-634 (itère sur **toutes** les lignes, sans filtrer `invalide` ni `phase`).
- **Ce qui est** (rejoué, `travail/scripts/demo_champion2.py`) : une lignée a g0 et g1 **valides** puis g2
  **`INVALIDE_MODELE`** (panne de modèle non conforme). `_scores_finaux` garde le score témoin de g2 (invalide) et
  `designations_et_concours` retient `v[-1]` = **0,125** (la génération invalide), alors que la dernière génération
  **valide** (g1) a un score témoin de **0,0**. Le champion N-039 b est donc calculé sur une génération que H-E3
  déclare invalide. Incohérence interne : pour les attaques et les métriques, `Confrontation._derniere_generation`
  (l. 161-163) filtre bien `statut == "OK"` ; seul le témoin du champion ne filtre pas.
- **Correction proposée** : dans `_scores_finaux` (ou dans `designations_et_concours`), ne garder que les lignes
  `statut == "OK" and not invalide and not phase`, et prendre le score de la **dernière génération valide** par lignée ;
  ajouter un test (cas sain : dernière génération valide ; artefact : dernière génération invalidée ⇒ témoin = celui de
  la dernière valide). Sinon, restreindre la désignation aux lignées sans invalidation et le dire.

**CR3-03 — majeure — H-E3 revendique les journaux de défense « scellés », mais le code ne les scelle ni ne compte les appels non conformes en défense (R5, R6).**
- **Où** : v6 § « Hypothèse » H-E3 l. 57 (« 0 appel `MODELE_NON_CONFORME` sur l'union des journaux scellés (amorçage,
  rondes de conception, générations, **défenses**) ») ; `confrontation._executer_sur_attaques` l. 207-211 (lit
  `serveur.n_appels`, **pas** `serveur.non_conformes` ; aucun `archive.sceller` du journal de défense).
- **Ce qui est** (rejoué, `travail/scripts/audit_defense.py`) : les journaux d'appels des défenses sont écrits sous
  `espace/travail/confrontation/<a>__vers__<b>/defense/noyau/journal-appels.jsonl` et ne portent **aucun** compagnon
  `.sha256` (`journaux_de_defense_scelles = []`) ; ils ne sont pas copiés dans `archive/`. Un `MODELE_NON_CONFORME`
  pendant une défense pose bien `serveur.arret` (plus aucun appel servi) mais n'est **ni compté ni remonté** par la
  confrontation, et « invalide la génération et arrête la lignée » (texte de H-E3) n'a pas de sens pour une défense.
  La garde H-E3 pour les défenses est donc sur parole : non scellée (R6), non testée (R5).
- **Correction proposée** : sceller chaque journal de défense (comme les journaux de génération le sont via
  `archive.deposer`) et, dans `_executer_sur_attaques`, lire `serveur.non_conformes` et le remonter dans le rapport de
  confrontation ; ajouter un test sain + artefact. À défaut, retirer « défenses » de la portée de H-E3 et le dire comme
  limite.

**CR3-04 — majeure — une ligne de la liste d'arrêt est « à écrire » (pas de code ni de test), alors que la panne qu'elle couvre est actuelle.**
- **Où** : v6 § « Liste d'arrêt » dernière ligne (« crédit d'un fournisseur épuisé (HTTP 402) … si une espèce
  d'amorçage est indisponible au lancement, la course n'est pas lancée (vérifié par un appel de contrôle avant la
  course) | **vérification du lanceur (à écrire par session-depot…)** ») ; `extrait-registres-v3.md` R-361 (« crédit du
  compte de `GEMINI_API_KEY` épuisé … bloque aussi les courses de l'étape 1 qui appellent gemini-4-argon ») ;
  `messages-conv-audit/…n18.md` § 5.
- **Ce qui est** : trois des cinq lignées sont de famille `gemini` (la gemini-argon auto-écrite + les deux imposées),
  et l'amorçage de la gemini-argon auto-écrite passe par un appel à `GEMINI_ARGON`. Le crédit Gemini est **épuisé**
  (HTTP 402, R-361, non encore rechargé dans les pièces). `cli.lancer` exige seulement la **présence** de
  `GEMINI_API_KEY` (l. 180), pas un crédit valide ; `appels.py` rend `ECHEC_API` sur 402 mais ne refuse pas de lancer.
  La garde « appel de contrôle par espèce avant la course » n'existe donc pas dans le code (contrairement aux autres
  lignes de la liste, qui citent toutes un test existant) : c'est la régression que CR-02 (relecteur n° 1) avait fait
  corriger pour les autres gardes, ré-ouverte pour celle-ci.
- **Correction proposée** : coder l'appel de contrôle par espèce avant la course (statut `OK` exigé, sinon refus de
  lancer) et son test (cas sain ; artefact : une espèce en 402 ⇒ la course ne part pas), avant le scellement ; ou, si la
  vérification reste au lanceur, le préenregistrement doit pointer le test du lanceur (chemin + nom), comme pour toutes
  les autres lignes. Lier explicitement au nœud « recharge Gemini » (R-361) : tant que le crédit n'est pas rétabli, le
  run des lignées gemini ne peut pas satisfaire H-E0.

**CR3-05 — majeure — la « cohérence de signe par course » (réponse de la v6 à CR2-05) ne corrige pas la sous-estimation de l'intervalle de H-E1 sous une dérive commune aux lignées d'une même course.**
- **Où** : v6 § « Seuil » l. 99-101 et § « Critères de lecture gelés » ligne 3 (« … **et** moyenne de Δ positive dans
  chacune des deux courses ») ; § « Plan d'analyse » l. 113-119 (bootstrap de niveau 1 sur les lignées-graines) ;
  `analyse.difference_h_e1` l. 74-77 (`idx_paires = rng.integers(0, n, size=n)` avec n = 10).
- **Ce qui est** (rejoué, **non opposable, R7**, `travail/scripts/caracteristiques_h_e1.py`, modèle illustratif : base
  par lignée U(0,60 ; 0,80), effet de course partagé c ~ N(0, σ), gain de lignée ~ N(0, 0,05), **moyenne vraie du gain
  nulle**, 60 tâches de test final, 400 répétitions) : le bootstrap de niveau 1 rééchantillonne les **10
  lignées-graines** comme échangeables, alors qu'elles sont groupées en **2 courses** qui partagent banque, conditions
  d'appel du jour et tirages d'ordre (la v6 le dit : « la réplication indépendante est la course (n = 2) »). Sous effet
  nul, le taux de « confirmé » passe de 0,8 % (σ = 0) à **10 %** (σ = 0,10) ; et la règle de cohérence de signe par
  course **ne change rien** (`confirme_table_du_code` = `confirme_avec_regle_par_course_v6` dans les trois scénarios),
  parce qu'une dérive de course positive rend les deux moyennes positives et satisfait la règle au lieu de la filtrer.
  La réponse de la v6 nomme le bon problème mais la correction est inopérante sur l'erreur de type I ; avec 2 courses
  seulement, aucun intervalle rééchantillonnant les courses n'est praticable.
- **Correction proposée** : dire explicitement que, avec 2 courses, l'intervalle du bootstrap de niveau 1 (sur les
  lignées-graines) **sous-estime** la variance quand une dérive est commune aux lignées d'une course, et que la règle de
  signe par course ne la corrige pas ; soit ajouter des courses (niveau 1 = course), soit déclarer H-E1 **descriptive**
  comme H-E2, soit ajouter au verdict « confirmé » une condition qui borne l'effet de course (par ex. écart entre les
  deux moyennes de course sous un seuil). Le chiffre ci-dessus n'est pas opposable ; le sens (type I > nominal sous
  variance de course) l'est.

### Mineures

**CR3-06 — mineure — les déclencheurs de l'audit de symétrie (ligne 1 de la table) ne sont calculés ni testés par le code.**
- **Où** : v6 § « Critères de lecture gelés » ligne 1 (|Δ| ≥ 0,30, témoin g0 < 0,05 / > 0,95, variance nulle entre
  lignées-graines, part de manquantes 0 % / 100 %) ; `analyse.lecture_h_e1` l. 95 (lit `resultat["audit"]`, fourni par
  l'appelant ; rien dans `analyse.py` ne calcule ces quatre déclencheurs). `test_analyse_controle_positif_et_lecture`
  ne couvre que `lecture_h_e1({"audit": True})`.
- **Correction** : écrire et tester une fonction qui calcule `audit` (les quatre déclencheurs) et `invalide` (la ligne
  2) à partir des Δ et des réponses, et la nommer dans le plan ; sinon R4/R5 reposent sur l'analyste à la main.

**CR3-07 — mineure — la condition « moyenne de Δ positive dans chacune des deux courses » du verdict « confirmé » est hors du code gelé et absente du contrôle positif.**
- **Où** : v6 § « Plan d'analyse » l. 125-126 (« appliquée par l'analyste sur les deux moyennes rapportées (pas de code
  nouveau) ») ; `analyse.lecture_h_e1` l. 102-103 (ne teste que `bas > 0 and difference >= 0,10`) ;
  `verifier_sur_simulation` (ne construit pas la structure par course).
- **Correction** : coder la condition par course dans `lecture_h_e1` (ou une enveloppe nommée) et l'inclure au contrôle
  positif, pour que le critère de confirmation soit gelé au sens de R1, pas appliqué de mémoire.

**CR3-08 — mineure — l'amorçage du devis est calculé sur une consigne implicite ≈ 30 000 caractères, en deçà du pire cas réel.**
- **Où** : v6 § « Devis » l. 245 (« amorçage … 3,3 + 1,3 + 1,7 | 6,3 ») ; `contrat.prompt_amorcage` ;
  résumé de banque (texte jusqu'à 20 071 caractères).
- **Ce qui est** (rejoué, `calcul_devis.py`) : la consigne d'amorçage sans exemples fait 14 715 caractères ; avec les
  6 exemples de `train` (jusqu'à 20 071 caractères chacun) elle peut atteindre ≈ 135 000, et l'amorçage pire cas monte
  à ≈ 7,2 USD (3,65 + 1,46 + 2,05), non 6,3. Écart faible (≈ 0,9 USD/graine) mais un « pire cas » devrait prendre les
  exemples réels (à mesurer sur la banque scellée).
- **Correction** : recalculer l'amorçage avec la longueur réelle des 6 exemples d'amorçage de la banque.

**CR3-09 — mineure — les graines des deux courses et l'entropie d'analyse ne sont pas fixées dans le préenregistrement (R9, R1).**
- **Où** : v6 § « Plan d'analyse » l. 113 (« 2 courses adaptatives (graines distinctes) »), l. 118
  (« `SeedSequence(<entropie d'analyse consignée>)` »), l. 128-131 ; § « Devis » l. 264-265 (« la seconde graine est
  engagée avec la première »). Les valeurs ne sont pas données (le motif `<…>` en français n'est pas capté par le
  validateur, qui ne cherche que `<<NOM>>`).
- **Correction** : fixer les deux entropies de course et l'entropie d'analyse (ou dire qu'elles sont tirées par
  `SeedSequence()` et scellées en addendum avant tout run), pour empêcher toute relance avec une autre graine (R3).

**CR3-10 — mineure — l'en-tête d'espace de travail (`ANTHROPIC_CUSTOM_HEADERS`) n'a ni code ni test dans les pièces.**
- **Où** : v6 en-tête l. 31-33 ; aucune occurrence de `ANTHROPIC_CUSTOM_HEADERS` dans `essaim_m3/` ni dans
  `collisionneur_v2.py` (grep). R-361 indique que le SDK `anthropic` lit cette variable d'environnement (posée par le
  lanceur), ce qui est plausible et a fonctionné pour le collisionneur, mais le noyau ne la gère pas lui-même et rien
  ici ne le teste.
- **Correction** : dire que l'en-tête est passé par l'environnement du processus et lu par le SDK (aucun code du noyau),
  et le vérifier au moins par un appel de contrôle au lancement (lié à CR3-04). Non vérifiable ici (pas de réseau).

### Forme

**CR3-11 — forme — commit de `registres/depenses.md` incohérent entre le brouillon et l'extrait fourni (empreinte identique).**
- **Où** : v6 § « Devis » l. 262-263 (« `registres/depenses.md` au commit **`cea4218`** de `main`
  (`d2cd6979…`) ») ; `extrait-registres-v3.md` l. 1 (« Extraits des registres (main **`548773a`**) ») et l. 4
  (`registres/depenses.md` : `d2cd6979…`). L'empreinte `d2cd69791668afd1d2075bfdedefc7acd3f0b99de56419643c3a44f83b3e1fa0`
  est **identique** dans les deux (vérifié) : le fichier n'a pas changé, seul le nom du commit diffère. Préciser le même
  commit (R6 est satisfait par l'empreinte, mais la divergence de commit prête à confusion).

**CR3-12 — forme — préciser que la confrontation ne charge jamais de traits, pour expliciter la double sécurité du « sans gradient ».**
- **Où** : v6 § « Bras… » l. 231 (« `entrainements_max` 0 (sans gradient) »). Le texte repose sur `entrainements_max =
  0`. En réel, la confrontation ne passe pas `--traits`, donc `self.vues` est vide et `_entraineur` renvoie `None`
  même si `entrainements_max` était > 0 (`boucle.py` l. 332 : `… or not self.vues`). Le dire évite tout doute sur
  l'absence d'entraîneur en confrontation (voir point 3).

---

## Suivi des constats précédents

### Contre-lecture n° 1 (CR-01 à CR-22, sur la v1 ; rapport `3b5aae60…`)

Tous traités dès la v4 (relu par la contre-lecture n° 2 : 15 traités, 7 en partie) et confirmés en v6 par exécution,
sauf ce que les constats n° 2 ci-dessous reprennent. Re-vérifié par moi, root + `unshare` réel :

- **CR-01** (isolation du système de fichiers) : **traité**. `test_organisme_fuite_…` passe sous root ; l'organisme
  « fuite » ne lit ni banque, ni juge, ni index d'archive, ni le **dossier de travail** d'une autre lignée, n'écrit pas
  dans la vue, ne pose pas `STOP`, ne laisse aucun processus. Audit des droits (`audit_droits_vue.py`) : racine 0711,
  `travail/<lignée>` 0711, vue 0755/0555/0444, utilisateurs distincts (60000, 60001). *Réserve mineure, pas un
  constat nouveau* : le test « fuite » éprouve l'accès au **dossier de travail** d'une autre lignée
  (`.../travail/claude-opus-5-5`), mais la **vue** d'archive (`archive_vue/`) est en 0755/0444 et donc **lisible par
  tous les utilisateurs** ; c'est voulu en mode `--memoire-partagee`, mais en mode privé (défaut) une lignée peut lire
  la vue d'une autre (le contrat ne donne à chaque lignée que `archive_vue/<sa lignée>`, mais le système ne l'empêche
  pas). Sans effet sur la banque/le juge ; signalé pour mémoire.
- **CR-02** (gardes avec code et test) : **traité** pour 13 lignes (toutes passent sous root) ; **ré-ouvert** pour deux
  cas en v6 → CR3-03 (défenses) et CR3-04 (crédit épuisé / appel de contrôle « à écrire »).
- **CR-03** (lignées imposées, ≥ 4 lignées) : traité. `test_bras_gele_apparie_…`, `test_lignee_imposee_…` ; les
  lignées imposées entrent en réel et en simulation avec famille déclarée et empreinte d'arbre.
- **CR-04** (procédure de la métrique, gel) : traité. `extraire-metriques` sans lecture de score ; `confronter
  --metriques-gelees` refuse un relevé non scellé/altéré (`test_releve_gele_puis_confrontation_separee` passe).
- **CR-05** (H-E2 descriptive) : traité. `analyse.concordance_h_e2`, seuils réservés à un préenregistrement ultérieur.
- **CR-06** (attaques visibles, défendeur averti) : traité. Vue sans `attaques.json` (vérifié) ; défense sans marque,
  attaques mêlées au test de développement (contexte de défense sans clé `confrontation`, vérifié).
- **CR-07** (champion, non-livraison) : traité pour la discriminance (`test_metrique_distingue_parfait_et_inverse`
  passe) et le vocabulaire des attaques ; mais la **désignation** elle-même a l'écart CR3-02.
- **CR-08** (bras gelé apparié) : traité. `--gel --depuis` relance les mêmes g000 (empreintes égales, vérifié,
  `audit_g000_bras.py`), historique vide, vue vide (`archive_vue_gel`).
- **CR-09** (test final jamais rendu) : traité.
- **CR-10** (table de lecture, audit à double sens) : traité dans le texte ; déclencheurs non outillés → CR3-06.
- **CR-11 / CR-18** (analyse, contrôle positif) : traités ; `test_analyse_controle_positif_et_lecture` passe. Réserve
  d'unité → CR3-05 (reprise de CR2-05).
- **CR-12** (bornes) : traité ; sockets uniques par course, budgets fixés.
- **CR-13** (devis) : **ré-ouvert** → CR3-01 (confrontation) et CR3-08 (amorçage).
- **CR-14** (choix selon les résultats) : traité ; répétition sur banque de simulation, seconde graine engagée d'avance
  (mais graines non fixées → CR3-09).
- **CR-15** (hybrides, ordre, vue) : traité ; famille nominale (N-040), ordre tiré et consigné, archive privée par
  lignée (`test_ordre_des_lignees_…` passe).
- **CR-16** (qui a écrit quoi) : traité ; table § « Qui a écrit quoi », conflits déclarés.
- **CR-17** (tâches réelles, référence de surface) : traité ; banque scellée, `reference_traits_texte` (chiffres non
  rejouables ici, banque absente).
- **CR-19** (graines, manifeste) : traité ; `SeedSequence(entropie, spawn_key=…)` conforme au texte (vérifié dans
  `boucle.graine` et `graine_ronde`).
- **CR-20 / CR-21 / CR-22** : traités.

### Contre-lecture n° 2 (CR2-01 à CR2-09, sur la v4 ; rapport `1420d6fa…`)

- **CR2-01** (validateur, titres canoniques) : **traité**, rejoué — le validateur rend `[]` sur la v6 (huit titres
  canoniques présents, sections libres en plus).
- **CR2-02** (`usd_max` affame Fable/Argon) : **traité** — `usd_max = 37` par génération, 160 appels ; le pire cas d'un
  appel (0,231 USD à 37/160) couvre un appel Fable sur le texte le plus long de la banque (0,278 USD au plus pour
  4 096 jetons de sortie — à noter, légèrement au-dessus de 0,231 : au `max_tokens` par défaut 4 096, un appel Fable
  sur un texte de 20 071 caractères coûte au pire 0,278, donc 160 tels appels dépasseraient 37 ; le calcul « 36,8 USD
  pour 160 appels » suppose des textes plus courts en moyenne. Vérifier que `usd_max = 37` laisse bien répondre à
  toutes les tâches à la répétition générale, comme le texte le promet).
- **CR2-03** (devis, provenance, phase 0) : **partiellement ré-ouvert** → CR3-01 (confrontation) et CR3-08. La
  provenance du GO est corrigée (GO « calcul » distinct, ni GO-05 ni GO-06 ni l'accord gradient 18:22) et vérifiée dans
  l'extrait des registres ; l'empreinte de `depenses.md` concorde (CR3-11 sur le nom de commit).
- **CR2-04** (clés `RR_*`, `ANTHROPIC_BASE_URL`) : **traité** — `test_mode_reel_refuse_anthropic_base_url` passe ;
  en-tête d'espace de travail → CR3-10 (non testé ici).
- **CR2-05** (unité d'analyse, deux courses) : **partiellement traité** → CR3-05 (la cohérence de signe par course ne
  corrige pas l'intervalle). H-E1 restreinte aux auto-écrites est bien rapportée en descriptif.
- **CR2-06** (« test à ajouter » qui existe) : **traité** — le texte cite les tests existants.
- **CR2-07** (empreintes de l'en-tête) : **traité** — les 14 empreintes concordent avec `EMPREINTES-v8.txt`.
- **CR2-08** (balance des vérités) : **traité** — garde 60/40 dans `verifier_banque`
  (`test_verifier_banque_refuse_des_verites_desequilibrees` existe ; résumé de banque : 50/50 partout).
- **CR2-09** (sous-ensemble non versé) : la banque et le sous-ensemble ne sont pas dans les pièces de cette
  contre-lecture (seuls comptes agrégés, documentation, provenance) : non vérifiable ici (voir plus bas).

### Rapport « gradient étape 1 » (CE-02, même noyau)

**CE-02 ne s'applique pas à la confrontation.** L'entraîneur par gradient (`entrainement.py`) exécute l'objectif écrit
par l'organisme dans un sous-processus que `_limites` (l. 170-179) borne par `setrlimit` **sans** `setuid`, `unshare`
ni `setsid` : en réel (noyau root) il tournerait en root sans isolation, comme CE-02 le dit pour l'étape 1. Mais dans
la confrontation il **n'est jamais instancié** : (a) la v6 fixe `entrainements_max = 0` ; (b) surtout, en réel la
confrontation ne charge pas de traits (`--traits` non passé), donc `self.vues` est vide et `boucle._entraineur`
renvoie `None` même si `entrainements_max > 0` (l. 332) ; (c) `confrontation._executer_sur_attaques` ne crée un
entraîneur que si `traits_att is not None`, c'est-à-dire **en simulation seulement** (l. 183). Donc l'isolation
insuffisante de l'entraîneur reste un sujet pour l'étape 1 (gradient), hors du périmètre de cette confrontation. Voir
CR3-12 (le dire).

---

## Réponses aux sept points

1. **Chaque traitement CR-01…22 et CR2-01…09 est-il réel ?** Oui pour la grande majorité (vérifié par 74 tests qui
   passent et par lecture), avec quatre ré-ouvertures : CR-02 → CR3-03 et CR3-04 ; CR-07 → CR3-02 ; CR-13/CR2-03 →
   CR3-01 et CR3-08 ; CR2-05 → CR3-05. Le validateur du dépôt ne relève aucun problème sur la v6 (CR2-01 traité,
   rejoué), comme l'auteur l'affirme.

2. **Phase de conception et moisson.** Bornes réelles et testées : `--rondes-conception-max 8`, budget de ronde
   (`usd_max_conception 10`, `appels_max 160`, `temps_max_s 1800`), moisson 30 recherches / 20 téléchargements / 40 Mo,
   corpus empreinté et index scellé en fin de génération, texte rendu comme donnée, provenance (hôtes permis, liens
   rendus par une recherche de la génération), http refusé, source inconnue refusée. Tests
   `test_phase_de_conception_a_critere_d_arret_de_l_organisme`, `test_telechargeur_provenance_plafonds_et_extraction`,
   `test_moisson_de_bout_en_bout_en_simulation` passent (sain + artefacts, R5) ; `test_sources_reelles_de_moisson_si_reseau`
   sauté (réseau coupé), ce qui n'est pas un défaut. **Provenance** : l'organisme conçoit son critère d'arrêt
   (`fin_conception.json`), le noyau ne suggère rien (contrat § 5 bis) ; rejoué (`audit_g000_bras.py`) : la génération 0
   est bien l'organisme **issu** de la conception (`g000-concu`), même empreinte dans le bras gelé apparié, qui ne
   refait pas la conception (vue vide, historique vide). **Injection des textes moissonnés** : marqués donnée (contrat),
   organisme sans réseau ni clé, menace mesurée et rapportée — acceptable. **Scellement avant la génération 0** : la
   banque est scellée avant (R1) et rien de moissonné n'y entre. **Effet sur l'appariement du bras gelé** : nul (le bras
   gelé relance la g000 déjà conçue, sans phase de conception). **Arrêt sur plafond pendant la conception** (rejoué,
   `audit_plafond_conception.py`) : avec plafond nul, `arret_conception`, course arrêtée avant toute génération notée ;
   avec plafond faible, les rondes passent et la génération notée est plafonnée proprement. Conforme. *Réserve* : les
   deux lignées imposées font aussi 8 rondes de conception « à vide » (elles recopient leur code) et consomment du
   budget — dit par la v6, compté dans le devis (5 lignées × 8 rondes).

3. **L'entraîneur par gradient est-il servi pendant la confrontation ?** **Non** (voir CE-02 ci-dessus) : à ce commit,
   ni les générations (`entrainements_max = 0`, et `self.vues` vide en réel faute de `--traits`) ni les défenses
   (traits d'attaque seulement en simulation) n'instancient l'entraîneur. Son isolation serait **insuffisante** s'il
   tournait en réel (pas de `setuid`/`unshare`/`setsid` dans `entrainement._limites`), mais ce cas n'est pas atteint
   dans cette confrontation. À préciser dans le texte (CR3-12).

4. **Analyse et lecture.** Unité = lignée-graine ; intervalle = bootstrap à deux niveaux ; code `analyse.py` présent et
   testé ; contrôle positif rejoué (gain connu → « confirmé », gain nul → « non concluant »). **Mais** : l'intervalle
   traite 10 lignées-graines comme indépendantes alors que la réplication est la course (CR3-05) ; la condition « moyenne
   positive par course » du verdict « confirmé » est hors code (CR3-07) ; les déclencheurs d'audit (R4) ne sont pas
   calculés par le code (CR3-06). Double désignation et concours de métriques : codés et testés
   (`test_double_designation_du_champion_et_concours_de_metriques` passe), N-039 b reste la règle qui décide — mais son
   témoin a l'écart CR3-02. Table gelée : conforme au texte dans `lecture_h_e1`, sauf la condition par course et les
   déclencheurs d'audit. Contrôle positif : présent.

5. **Devis et plafonds.** Arithmétique interne cohérente (course adaptative 961,3 = 6,3 + 400 + 555 ; une graine
   1 697,5 ; total 3 512,3 — rejoué), **sauf la ligne confrontation** (15,1/défense au lieu de 37, donc 181,2 au lieu
   de 444) et **sauf la cohérence avec le mécanisme de réservation** : la confrontation s'impute au plafond de la course
   adaptative rechargée (961,3), déjà saturé au pire cas, et le plafond demandé (3 520) ne couvre pas le vrai pire cas
   (≈ 4 038). C'est CR3-01. Provenance du GO vérifiée (GO « calcul » distinct, non couvert par GO-05/GO-06/18:22 ;
   empreinte de `depenses.md` concordante). Moisson web (Brave) : jusqu'à ≈ 4 380 requêtes au total (rejoué : 2 100 par
   graine + 180 par répétition × 2 = 4 380, le texte dit « ≈ 4 400 »).

6. **Vérification des étiquettes par paires, banque, référence de surface.** Procédure décrite (10 paires,
   `SeedSequence(20261025)`, 5 par lot, sous-agent neuf anonymisé, seuil « au plus une paire en désaccord sur 10 »)
   mais **pas encore faite** (le § « Qui a écrit quoi » dit « à faire », le § « Contre-lecture » la liste comme reste
   avant scellement, le message n° 18 § 3 dit le résultat « dans mon prochain message ») : **non vérifiable ici**. Le
   format des identifiants publics (`cd-<lot>-L…-H/S`, `ce-<source>-NNNN`) et l'équilibre 50/50 par sous-ensemble sont
   cohérents avec le schéma documenté (rejoué sur des lots synthétiques, `audit_identifiants.py` : `verifier_banque`
   rend `[]`, 80/60/60, suffixe = vérité). `verifier_banque` applique bien la garde 60/40 (CR2-08). Référence de
   surface (0,69 / 0,50 sur test final) : non rejouable (banque absente) ; cohérente avec le seuil 0,80 (les deux
   familles restent).

7. **Reste (R1–R14, R3, R4, R9, chiffres, provenance des décisions).** R1 : le préenregistrement est complet et passe
   le validateur ; restent avant scellement la vérification d'étiquettes et les corrections ci-dessus. R3 : répétition
   sans lecture de score, seconde graine engagée d'avance — mais graines non fixées (CR3-09). R4 : audit prévu dans les
   deux sens, mais déclencheurs non outillés (CR3-06). R9 : graines dérivées conformes au code ; valeurs racines à
   fixer (CR3-09). R6 : chiffres rattachés à des empreintes, sauf les journaux de défense non scellés (CR3-03). R7 : pas
   de chiffre d'état de l'art opposable dans le texte ; mes propres chiffres de simulation sont déclarés non opposables.
   Provenance des décisions de Lazar : les nœuds cités (N-039 b, N-040, N-041 c, N-043 b, P-026 a ; GO-2026-10-24-02 à
   -06) concordent avec `extrait-registres-v3.md` et `decisions-lazar-2026-10-24-v1.md` (vérifié). R13 : le verdict de
   porte reste à un sous-agent neuf ; cette contre-lecture exécute R2.

---

## Ce que j'ai rejoué (tout sous `…/r2-confrontation-v6/travail/`, copies ; aucun réseau de modèle ; aucun processus laissé)

- **Empreintes** : les 80 fichiers de `EMPREINTES-v8.txt` présents → OK ; brouillon v6 = `0ce8c396…` (attendu) ;
  collisionneur = `213b52ef…` ; tous les compagnons des pièces OK (sauf les `banque/*.json` volontairement absents).
- **Tests** : conteneur root, `unshare --mount --net`, `env -i`, `/opt/essaim-m3-venv-v1/bin/python` →
  **74 passés, 1 sauté (réseau), 5 échoués faute des pièces absentes** (`organismes/gemini-v2/`, `banque/*.json`).
  Sorties `travail/sorties/tests-sortie-v1.txt` (`a7de0258…`), `-v2.txt` (`3b3311e4…`).
- **Validateur du dépôt** sur la v6 (copie de `prereg.py` + bouchons `gardes`/`scellement`) : **aucun problème**.
- **Devis** (`calcul_devis.py`, sortie `3c4f04a3…`) : amorçage, pire cas d'un appel, pire cas d'une défense (37, non
  15,1), total avec défense à 37 (≈ 4 038), amorçage pire cas réel (≈ 7,2), moisson (4 380).
- **Contexte de défense** (`audit_defense.py`, `49d84a0a…`) : budget de défense 160 appels / 37 USD ; journaux de
  défense **non scellés** ; sortie standard de `simuler`.
- **Droits de la vue d'archive** (`audit_droits_vue.py`, `f2c8bf4c…`) : utilisateurs distincts, vue 0755/0444.
- **Phase de conception et plafond** (`audit_plafond_conception.py`, `13c58013…`) : `arret_conception` sur plafond nul.
- **Appariement g000 adaptatif/gelé** (`audit_g000_bras.py`, `42a1c6d7…`) : même empreinte g000, vue gelée vide.
- **Champion sur génération invalidée** (`audit_invalide_champion.py`, `7a7eebb2…` ; `demo_champion2.py`, `0b19ec19…`) :
  le témoin retenu par `designations_et_concours` vient de la génération `INVALIDE_MODELE`, pas de la dernière valide.
- **Format des identifiants de banque** (`audit_identifiants.py`, `38661b2e…`) : schéma documenté, `verifier_banque` = [].
- **Caractéristiques de la règle H-E1** (`caracteristiques_h_e1.py`, sortie `ea5609eb…`, **non opposable R7**, 400
  répétitions) : sous effet nul, « confirmé » 0,8 % (σ_course 0), 2,0 % (0,05), **10 %** (0,10) ; la règle par course
  n'y change rien.

## Ce que je n'ai pas pu vérifier

- **La banque elle-même** (`banque-confrontation-v1.json` et son secret, le sous-ensemble public, les deux lots de
  traces) : non fournis (seuls comptes agrégés, documentation, provenance). Donc : partition réelle, équilibre fin,
  référence de surface 0,69 / 0,50, longueurs par tâche, et la **vérification d'étiquettes par paires** (non encore
  faite) ne sont pas vérifiables ici. J'ai pris `resume-banque-confrontation-v1.md`, `banque/LISEZMOI-v3.md` et
  `PROVENANCE-eval-awareness-v1.md` pour argent comptant.
- **Tout appel réel** (interdit, pas de réseau de modèle) : l'en-tête d'espace de travail (`ANTHROPIC_CUSTOM_HEADERS`,
  CR3-10), le passage de la clé `RR_*` sous le nom `ANTHROPIC_API_KEY`, les coûts réels, la latence, les refus de filtre
  de sûreté : non testés ; j'ai lu le code et le journal R-361.
- **Les lignées imposées** (`gemini-corrige-v3`, `gemini-organisme-v3`) et `organismes/gemini-v2/` : non fournies
  (hors périmètre) ; les deux tests qui les citent échouent faute de la pièce, pas pour un défaut de code. Je n'ai pas
  vérifié qu'elles tournent 8 rondes de conception sans incident ni qu'elles appellent `GEMINI_ARGON` (lié à CR3-04).
- **Les chiffres de ma simulation H-E1** reposent sur un modèle du relecteur (base, σ_course, σ_lignée posés) : ils
  établissent la **direction** (type I > nominal sous dérive de course ; règle de signe par course inopérante), pas des
  valeurs opposables (R7).
- **Le collisionneur** n'a jamais été exécuté contre une interface réelle ; `cout`, `cout_pire_cas`, `modele_conforme`
  lus statiquement et utilisés tels quels pour le devis.
