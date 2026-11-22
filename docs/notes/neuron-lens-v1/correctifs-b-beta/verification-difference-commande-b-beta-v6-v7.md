# Vérification de la différence entre la commande v6 et la commande v7, du code de course v3 et de la garde de priorité

Verdict : **employable** (0 défaut majeur, 7 défauts mineurs, aucun bloquant ; les n° 1, 2, 4 et 5 valent d'être corrigés avant le feu si cela ne coûte rien).

Vérificateur neuf (R2), 2026-11-18, branche `claude/brave-galileo-jhp684`. Rien exécuté du loueur de cartes ; aucune variable secrète lue ; aucun fichier existant modifié.

## 1. Différence v6 → v7 (diff complet lu)

Toutes les différences sont annoncées dans l'en-tête de la v7 ((A) ligne de calcul GO-35, (B) crédit levé et garde de priorité, (C) clé). Aucun seuil, aucune mesure, aucune issue, aucune étape de la course (§ 2 de la v7) n'est touché ; les seuils 75 / 45,0 / 67,5 USD, 2,62 USD/h, 1,85-2,62, 25,38 h sont identiques.
Différences vérifiées une à une :
- Substitutions de GO : GO-2026-11-18-02 → GO-2026-11-18-35 au crochet (variable `GO_ID=` devant la commande de création) et à la machine (`-e GO_ID=`), lignes 132-133 de la v7 ; les deux occurrences restantes de -02 (lignes 6 et 33) sont des mentions de la décision mère, correctes.
- Dépôt réduit v2 → v3 : liste `66ee33c2…`, commit source `a5ae50a6`, branche `course/neuron-lens-b-beta-reduit-v3`, amorce `amorce_neuron_lens_b_beta_v3.sh` (lignes 122-134, 206).
- Condition de crédit (§ 0 point 3, ligne 37 du tableau) remplacée par la garde de priorité ; `can_pay`, `has_billing`, `billing_failed` conservés. Étape 10 bis ajoutée ; veille (étape 11), étape 15 et § 2 (contrôles) étendus à la garde de priorité.
- Pièces qui font foi : empreintes abrégées mises à jour (vérifiées, § 4).
Aucune différence non annoncée de fond. Une réserve de cohérence : n° 5 ci-dessous.

## 2. Code v3 contre v2

`diff` des huit couples : seules différences = ligne d'en-tête ajoutée, renommages v2→v3 (lanceur, partie 2, amorce, dépôt réduit, essais), `GO_ATTENDU = "GO-2026-11-18-35"` (seul changement de fond, `b_beta_lancer_v3.py:53`), et dans l'essai à blanc `GO_ID=…-35` / `GO=GO-2026-11-18-35` (lignes 74, 96, 121) et l'intitulé « v2 ». Recherche de références résiduelles à des noms v2 dans les fichiers v3 : aucune qui devrait être v3 (`controles_b_beta_v2`, `controles_b0_v2`, `verdicts_b_beta_v4` sont des pièces non renommées et inchangées, correctes). Liste `MODULES` du lanceur, listes de modules et d'essais du dépôt réduit v3 (lignes 35-39, 53) et variable `ESSAIS` de l'amorce (ligne 46) pointent toutes vers les noms v3/v5/v3 ; la liste du dépôt réduit rejouée (§ 5) le confirme.
Étape 7 : nom d'amorce `amorce_neuron_lens_b_beta_v3.sh`, branche `course/neuron-lens-b-beta-reduit-v3`, identifiant de GO identique au crochet et à la machine, et égal à `GO_ATTENDU` (contrôle code 17, lanceur ligne 191).
Simulation du crochet (`decider` du crochet, commande tirée du texte de l'étape 7, `<…>` remplacés par des valeurs factices, `date(2026,11,18)`, `cwd` = dépôt de course) : **v7 → PASSE** (identifiant vu : GO-2026-11-18-35 seul) ; **v6 → REFUSE** (« GO-2026-11-18-02 est un GO de type 'décision', pas « calcul » »). Même simulation sur le bloc de l'étape 10 bis : passe.
Ligne GO-2026-11-18-35 de `registres/go.md` : type calcul, accordée 2026-11-18, échéance 2026-11-25, par Lazar, 75 USD ; aucune révocation ne la cite. GO-2026-11-18-02 : type décision.

## 3. Essais joués

`PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider` sur les six fichiers demandés : **163 passés, 0 échec, 2 avertissements** (divisions numériques déjà présentes, sans rapport). Garde de priorité seule : **10 passés**.
Complément : lancement réel de la garde de priorité (module, `python -m`) avec un faux outil du loueur en variable `VASTAI_OUTIL` (deux appels de 2 s chacun) : fichier de PID écrit, première ligne de journal `continuer`, crédit 40,0, en ~7 s ; la garde a été arrêtée par son PID.

## 4. Empreintes

Compagnons `.sha256` vérifiés (OK) : `b_beta_lancer_v3.py`, `addendum_partie2_b_beta_v3.py`, `amorce_neuron_lens_b_beta_v3.sh`, `depot_reduit_neuron_lens_b_beta_v3.py`, `garde_priorite_bbis_v1.py`, `test_neuron_lens_garde_priorite_bbis_v1.py`, `test_neuron_lens_b_beta_lancer_v3.py`, `test_neuron_lens_etapes_b_beta_v5.py`, `test_neuron_lens_montage_b_beta_v3.py`, `essai_a_blanc_amorce_neuron_lens_b_beta_v2.sh`, `essai-a-blanc-amorce-b-beta-v2.txt`, `commande-b-beta-v7.md`, `mot-lazar-cle-b-beta-2026-11-18-v1.md`. Empreintes abrégées de la table « Pièces qui font foi » : toutes égales (582fd9ef, 4f955a25, 91ef6986, 692cc064, 75b5db7e, 7e3bdf29, e1e0742c, fdc27dd1, b6f90dd8, 2201f998, db50aaaf, 3ef73748, 71833192) ; la v6 reste à `23c431d3` comme citée.
Journal de l'essai à blanc v2 contre v1 : mêmes cas, 0 écart, verdict « conforme, 0 écart » ; seules différences = commits/listes, temps (location_s 15 contre 11), groupes, objets lus (412 contre 403). Le libellé périmé « étapes égales à celles du lanceur v2 » est déclaré par la v7.

## 5. Dépôt réduit

`depot_reduit_neuron_lens_b_beta_v3.py a5ae50a6… <dossier neuf>` rejoué : **83 fichiers, `liste_sha256` = `66ee33c2cc511ecefa4bda72078f37b38e9ab71122e7c9954c85ba3f45d49f37`** (égale à l'attendue), commit réduit `d7ccccf8…`, paquet `1cfceb95…` (égaux à la v7 et au journal). Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/ff3e16f4-e2c5-5d31-b08c-99762b9cded7/scratchpad/verif-reduit/neuf`. La garde de priorité n'est pas dans le dépôt réduit (commit source antérieur) : voulu, elle tourne côté conteneur.

## 6. Garde de priorité (`src/controle_ia/neuron_lens/garde_priorite_bbis_v1.py`)

La règle de la mère est tenue : période 600 s, bornée à 900 s (`surveiller`, essai ValueError) ; seuil strict `< 12` (12,0 ne détruit pas, essai) ; destruction de la seule machine des lentilles par son identifiant (`destroy instance <ID> -y`, essai : aucun autre identifiant détruit), réessayée 5 fois par `detruire_verifie`, puis absence prouvée par `sv.absente` ; non prouvée → état `destruction_non_prouvee`, code 4 ; crédit illisible 3 fois → destruction ; liste illisible → étape B bis supposée en marche ; seul le crédit est lu de `show user` ; l'étape B bis n'est lue que par son identifiant. Étape 10 bis : syntaxe valide (`bash -n` sur le bloc extrait), PID écrit par la garde elle-même (`--fichier-pid`), `VASTAI_OUTIL` et `PATH` posés, chemin de PID `pid-priorite-b-beta-v1.txt` cohérent avec la veille (`pid-$1-b-beta-v1.txt`, `$1` = priorite) et son `grep`.

## Défauts

**Majeurs : aucun.**

**Mineurs**

1. **Sortie silencieuse sur une seule lecture « machine des lentilles absente »** — `garde_priorite_bbis_v1.py`, `tour()` (retour `lentilles_absentes`) et `surveiller()` : si la liste, lue sans erreur, ne contient pas (encore, ou transitoirement) la machine, la garde finit avec le code 0, sans nouvelle lecture. Juste après la création (liste du loueur en retard) elle ne s'arme pas ; en cours de route une lecture anormale la tue et l'étape B bis n'est plus protégée jusqu'à la prochaine ligne « MORTE » de la veille (jusqu'à 5 minutes plus la réaction). La v7 couvre le premier tour (« état `continuer` exigé à la première ligne, sinon destruction »), pas le cas en cours de route. Correction : relire la liste 3 fois à 20 s d'écart avant de conclure, donner à cet état un code de sortie distinct (par exemple 5), et écrire dans la v7 la conduite à tenir (relire par `suivi_vast_v6 instance <ID>`, ne détruire que sur preuve).
2. **Preuve d'absence plus faible que celle de l'étape 15** — `detruire_et_prouver`, dernière ligne : `sv.absente(id_lentilles, appel)` sans `non_vide` ni témoin ; l'étape 15 de la v7 exige `--non-vide`. Une liste vide lue au code 0 prouverait « l'absence ». Correction : `sv.absente(id_lentilles, appel, non_vide=True)`.
3. **Pas de garde contre une exception dans la boucle** — `main()` / `rapporter` : une erreur d'écriture du journal (dossier absent, disque plein) pendant ou après la destruction lève une exception ; l'état final n'est pas rendu, le code de sortie est celui d'une trace Python, non 3 ou 4. La veille ne verrait que « MORTE ». Correction : `try/except OSError` autour de l'écriture du journal avec repli sur la sortie standard, et `except Exception` dans `main` qui journalise et sort en code 4 si une destruction était engagée.
4. **Vérification du premier tour de l'étape 10 bis fragile** — `commande-b-beta-v7.md`, bloc de l'étape 10 bis : `sleep 5` puis `tail -1` du journal. Avec deux lectures du loueur (liste, crédit) de plusieurs secondes chacune, la première ligne peut ne pas être écrite (le `tail` échoue, la chaîne `&&` s'arrête avant l'inscription du PID : bruyant mais déroutant) ; et le journal n'est pas effacé avant l'armement (seul le fichier de PID l'est) : à un réarmement, `tail -1` peut montrer la ligne d'une garde précédente. Correction : `rm -f` du journal avant l'armement (ou le nommer par identifiant de course) et attendre jusqu'à 60 s une ligne (`for i in $(seq 12); do [ -s journal ] && break; sleep 5; done`). Aussi : « Toute branche d'échec des étapes 7 à 10 : destruction » devrait dire « 7 à 10 bis ».
5. **Registres et note de clé non alignés sur la v7** — `registres/go.md`, ligne GO-2026-11-18-35 : cite « commande v6 » et garde la condition de départ « crédit ≥ 117 USD », que la v7 dit levée par Lazar (R-3319) ; `docs/notes/neuron-lens-v1/mot-lazar-cle-b-beta-2026-11-18-v1.md` dit « aucune v7 » et « restent, inchangées : les trois montants de la condition de crédit » (périmé) ; R-3319 n'apparaît dans aucun registre de cette branche (seulement dans l'en-tête de la v7). Ni le crochet ni le lanceur ne lisent ces textes, donc rien ne casse, mais la levée d'une condition de départ repose sur une citation de seconde main. Correction : une ligne dans `registres/decisions.md` (mot de Lazar R-3319, verbatim, qui lève la condition et appelle la garde) et un addendum daté à la note de clé (sans réécrire la note), ou une ligne nouvelle au registre des GO.
6. **Aucun essai n'épingle la valeur littérale de `GO_ATTENDU`** — `tests/test_neuron_lens_b_beta_lancer_v3.py:16` et les autres essais lisent `L.GO_ATTENDU` : ils passeraient avec n'importe quelle valeur. Seul l'essai à blanc (`GO=GO-2026-11-18-35`) la couvre. Correction : un essai d'une ligne `assert L.GO_ATTENDU == "GO-2026-11-18-35"`.
7. **Étape 15** (`commande-b-beta-v7.md`) : « garde de priorité arrêtée par PID après `ps -p <PID> -o args=` » ; elle s'est déjà terminée dans trois cas prévus (destruction, étape B bis finie, machine absente). Dire « si elle vit encore ». Cosmétique.

## Cas demandés explicitement

- Machine des lentilles absente de la liste juste après la création : voir n° 1 (la garde finit en code 0 ; la v7 exige `continuer` à la première ligne, donc destruction par l'étape 15 par précaution ; sûr mais coûteux).
- Garde morte : couverte par la veille toutes les 5 minutes (ligne MORTE → réarmement par 9, 10, 10 bis) ; pas de couverture entre deux lignes (≤ 5 min plus la réaction), acceptable.
- `instance` rend une erreur pendant la destruction : `lire` lève, `detruire_verifie` la prend comme « non absente » et retente 5 fois (20 s d'écart) ; le dernier mot est `sv.absente` ; sinon `destruction_non_prouvee`, code 4 (essai `test_destruction_non_prouvee_rendue`). Conforme, sans repli silencieux, sous réserve du n° 3 (exception d'écriture).
