# Essai Lean, D-1a — procédure du poste local — v10 (vérificateur du noyau réparé ; troisième essai, voie (a))

- **Pour** : la session mère, qui en tire la consigne v3 du poste local (Claude Code sur l'ordinateur de Lazar).
- **Écrit par** : un développeur neuf (Opus 5.5), qui n'a écrit ni le harnais ni sa contre-lecture.
- **Remplace** : `procedure-poste-local-d1a-v9.md` (`7f69fece…`), qui reste versée telle quelle (R12), comme les v6 à v8.
  Le texte de la v9 est repris ci-dessous ; seuls changent l'en-tête, la section « Changements depuis v9 », et les passages
  qu'elle nomme (sections 0, 2 et 3).
- **Sources** : R-2438 (cause du second essai), R-2439 (mot de Lazar : « Réparer d'abord, puis relancer ») ; rapport du poste
  `rapport-poste-local-d1a-v2.md` (`b2bace9b…`, branche `donnees/lean-outillage-d1a-poste-local-v2`, tête `3b2a74a2`) ;
  R-2425 et R-2426 (voie (a)) ; procédure v9 et ses sources.
- **Code** : branche `prep/lean-outillage-d1a-v10`, commit `d7e42c26d0085cda3fa895b3380136a21b576975`, parti de `b0b8667a` (procédure v9 ;
  code du second essai `32a40613`), non fusionné.
  - Module : `controle_ia.lean_essai.minuterie_v7` (inchangé).
  - Pilote : `scripts/lean_essai_d1a_v9/piloter_poste_v9.sh`. Phase « avant » : il copie et lance
    `scripts/lean_essai_d1a_v2/installer_chaine_v2.sh`, `src/controle_ia/lean_essai/sonde_reseau_v2.py`,
    `scripts/lean_essai_d1a_v8/essai_lecture_bac_v1.sh`, puis `scripts/lean_essai_d1a_v9/essai_compilation_verificateur_v1.sh`
    sur `src/controle_ia/lean_essai/verificateur_noyau_v5.lean`. Phase « apres » : `executeur_bac_v5.py`,
    `epreuve_isolement_v5.py`, `verificateur_noyau_v5.lean` (et `gardes_lean_v4.py`, `sonde_reseau_v1.py`, inchangés).
- **Statut** : le vérificateur v5 est **compilé et joué hors machine contre la chaîne épinglée** (Lean 4.35.0, commit
  `eb6cafb7…` ; Mathlib `56a00585…` et son cache) : voir « Changements depuis v9 », points 6 et 7. Rien n'a tourné sur une
  machine ni contre l'interface réelle de Hetzner. Contre-lecture courte à faire ; cette procédure ne vaut que sous une
  consigne neuve de la mère.

## Changements depuis v9

Cause du second essai (R-2438) : `verificateur_noyau_v4.lean` ne compile pas sous Lean 4.35.0 (`CollectAxioms.collect`
inconnu…) ; G-L7 échoue partout ; `noyau` 0 sur 18. Mot de Lazar (R-2439) : réparer d'abord, puis relancer.

1. **Vérificateur du noyau v5** (`verificateur_noyau_v5.lean` ; la v4 reste, R12) : porté vers Lean 4.35.0, même conception,
   même sortie. Six changements, chacun renvoyé aux sources de la chaîne (chemin et ligne) dans l'en-tête du fichier :
   `Lean.collectAxioms` ; `Options.set` ; `unsafe enableInitializersExecution` ; `importModules … (loadExts := true)` ;
   rejeu par `Kernel.Environment.replay`, et environnement d'impression et d'aller-retour = imports + constantes acceptées par
   ce rejeu (l'ancien `Environment.replay`, déprécié, rendait un environnement sans contexte de réalisation des imports, où
   toute élaboration échoue) ; en-tête d'imports exact de 4.35.0 (`Init` ordinaire et `meta`, puis `Mathlib`).
   Mesuré hors machine : environ 8 s et 2,1 Gio de mémoire anonyme par passage (extensions de Mathlib chargées), sous la
   borne du bac (6 Gio). **Exécuteur et épreuve v5** (`executeur_bac_v5.py`, `epreuve_isolement_v5.py`) : copies des v4 dont
   seul le vérificateur change (son nom est en dur dans l'exécuteur v4).
2. **Essai R5 neuf, « le vérificateur compile sur la machine »** (`essai_compilation_verificateur_v1.sh`), joué par le pilote
   v9 à la fin de la phase « avant », **avant la coupure**, après « bac lit Mathlib.olean » :
   - cas sain : le vérificateur, copié 0644 et lu par `bac`, compile avec le `lean` et le `LEAN_PATH` installés
     (`/opt/harnais/chaine-v1.json`) : code 0 **et aucun message** (un avertissement sortirait sur la sortie standard du
     vérificateur et ferait échouer G-L7) ;
   - artefact : une copie volontairement cassée du même fichier est refusée (code non nul, message `error`) ;
   - non conforme : le pilote s'arrête, code non nul, **ni coupure, ni pilote « apres »** ; section 5, compte rendu.
3. **Même vérificateur avant et après la coupure** : après la copie sous `/opt/harnais/noyau`, le pilote compare (`cmp`) ce
   fichier à celui compilé avant la coupure ; différent : arrêt avant l'épinglage.
4. **Section 0 : un terminal WSL ouvert pendant tout l'essai** (incident R-2434 : sans fenêtre WSL ouverte, WSL arrête Ubuntu
   et tue les processus détachés, minuterie comprise) : un terminal Ubuntu ouvert par Lazar **avant l'essai à blanc** et
   gardé ouvert **jusqu'à l'inventaire final** de la section 5. `stat` du vérificateur : la v5.
5. **Troisième essai sous `GO-2026-11-10-13`** : 0,56 USD dépensés sur 65 (serveurs 175751342 et 175838427) ;
   `--deja-depense-usd 0.56`. **Déclaration : troisième machine sous cette ligne, accordée par Lazar (R-2439)** ; la garde
   « une machine par GO » est contournée par construction, comme en R-2426 : branche du poste **neuve**, partie du commit
   ci-dessus, dont `V` ne porte aucune pièce du premier ni du second essai (ni `rattrapage-machine-d1a-*-v1.json`, ni
   `journal-creations-machines-v1.jsonl`). **Une** préparation, **une** création, comme toujours. Essai à la main
   (2026-11-12, code de cette branche, registres de `b0b8667a` puis de `main` `300ebb5a`, `V` vide) : préparation acceptée ;
   seconde préparation dans le même `V` refusée ; déjà-dépensé retenu 0,56 (avec les registres de `main`, trois lignes non
   standard sous cette ligne de GO exigent de le déclarer).
6. **Essais hors machine** : `tests/test_lean_essai_verificateur_v5.py` (avec la chaîne épinglée, variable
   `LEAN_ESSAI_D1A_CHAINE` ; sans elle, sautés en le disant) et `tests/test_lean_essai_pilote_v9.py` ; jeu complet par
   `scripts/lean_essai_d1a_v9/essai_verificateur_hors_machine_v1.py` (journal `essai-verificateur-hors-machine-v1.json` dans
   `V`) ; mutations `scripts/lean_essai_d1a_v9/mutations_harnais_v9.py` (journal `journal-mutations-harnais-v9.json`).
7. **Écarts du jeu hors machine, non réparés ici, à trancher avant le troisième essai** (36 cas jugés conformes sur 39) :
   - **bloquant** : l'artefact `noyau_simproc_hors_noyau_v4.lean` ne compile pas sous Lean 4.35.0 (G-L1 :
     `Function._hors_noyau` absent, comme au second essai) ; tant qu'il n'est pas refait, **le premier pas `noyau` sera non
     conforme sur la machine** et le pilote « apres » s'y arrêtera ;
   - `gl5_vacuite_v1.lean` (attendu « accepté », transmis au relecteur) est refusé par G-L5 : Mathlib imprime
     `∀ x < 0, 0 < x → x ^ 2 < 0`, sans le type de `x` (option `pp.mathlib.binderPredicates`), et l'aller-retour refuse à bon
     droit ce texte ambigu (il se relit sur `ℕ`) ; refus à tort, du côté prudent ; l'épreuve sera non conforme sur ce cas.
   - Correctifs **éprouvés hors machine, non appliqués** (hors du mandat « rien d'autre que la compilation » ; décision de la
     mère) : (a) simproc : sous 4.35.0 le simproc de l'agent n'est jamais appelé (`This simp argument is unused`, `and_self`
     réécrit d'abord) ; avec `simp only [↓tricheHorsNoyau, and_self]` (pré-procédure), l'item compile et le rejeu du
     vérificateur v5 le refuse en nommant `etape_1._hors_noyau` (G-L8, l'attendu) ; il faudrait un artefact neuf, des
     attendus neufs et une épreuve qui les lise ; (b) vacuité : `pp.mathlib.binderPredicates` à faux dans les options
     d'impression du vérificateur (`Mathlib/Util/PPOptions.lean` l. 24) imprime `∀ (x : ℝ), x < 0 → 0 < x → x ^ 2 < 0`,
     dont l'aller-retour réussit ; l'item sain est inchangé ; il faudrait un vérificateur v6.

## Rappel : changements de la v8 à la v9

Corrections de la contre-lecture (`contre-lecture-courte-harnais-d1a-v8.md`) et voie (a) retenue par Lazar (R-2426). Aucun
code neuf.

1. **GO du second essai : `GO-2026-11-10-13`** (seul bloquant de la contre-lecture, constats 12 et 13). Le code n'accepte que
   cet identifiant (`garde_go_v1.py`, l. 21 et 88-93). Toutes les commandes portent `--go GO-2026-11-10-13` ; le point 7 de la
   v8 (« un GO neuf est nécessaire ») est retiré, et son affirmation était inexacte : la ligne de dépense inscrite ne fait
   pas refuser la préparation, ce sont les pièces du premier essai dans `V` (constat 12).
2. **Déclaration : seconde machine sous `GO-2026-11-10-13`, garde « une machine par GO » contournée par construction, sur
   mot de Lazar (R-2426).** La garde ne voit une machine antérieure que par le journal des créations et le fichier de
   rattrapage présents dans `V` (le motif de `registres/depenses.md` ne lit pas la ligne inscrite « serveur 175751342 »). La
   branche du poste **neuve**, `donnees/lean-outillage-d1a-poste-local-v2`, part de `32a40613` : son `V` ne porte **ni**
   `rattrapage-machine-d1a-*-v1.json` **ni** `journal-creations-machines-v1.jsonl` du premier essai ; la garde n'a donc rien
   à refuser. Ce contournement est voulu, déclaré, et ne vaut que pour ce second essai : **une** préparation, **une**
   création, comme toujours. Essai à la main (cas B de la contre-lecture, refait le 2026-11-12) : registres de `main`, `V`
   vide, `GO-2026-11-10-13` : préparation **acceptée** ; une seconde préparation dans le même `V` : **refusée**.
3. **Déjà-dépensé déclaré : `--deja-depense-usd 0.28`** (constat 14) : le premier serveur (175751342) a coûté 0,28 USD sous
   ce GO ; le devis compte la dépense réelle. Plafond inchangé (65 USD).
4. **Précautions de la contre-lecture**, inscrites aux sections 0, 2 et 3 :
   - `stat -c %a src/controle_ia/lean_essai/verificateur_noyau_v4.lean` doit rendre `644` sur le poste avant le pilote
     (sinon `chmod 644` de ce seul fichier dans le clone, sans commit) : le vérificateur est copié par `scp` sans `-p` et lu
     par `bac` (constat 11) ;
   - après L5, avant le pilote : `ssh-keygen -R <adresse du serveur>` si cette adresse est déjà connue du poste (adresse
     réattribuée : `accept-new` refuserait, constat 10) ;
   - `--prefixe-poste 24` **seulement après** `MV7 adresses-sortie` : `P` est le préfixe conseillé par la mesure ; si la
     mesure rend 32 alors que le premier essai a établi plusieurs adresses de sortie du même /24, le signaler à Lazar
     avant L2 ; jamais plus large que 24 (constat 10).
5. **L3** : la recette de la référence de suivi est à reprendre mot pour mot ; le message de la garde (« pousser avec
   `git push -u` ») ne la donne pas (constat 5).

## Changements depuis v6

## Changements depuis v6

(Le premier tour de la v7 ne portait que le point 1 sans l'essai de lecture, et les points 2 et 3 sans `~/.ssh` ni la sonde
v2 ; tout est repris ici.)

Tirés du premier essai (`noyau` non conforme, 0/18 ; rapport du poste, Incidents et Écarts) et de la liste de Lazar (R-2415).

1. **Lecture de la chaîne par `bac`** (cause de l'arrêt : fichiers compilés de Mathlib tirés du cache en `-rw-------`).
   - `installer_chaine_v2.sh` = `installer_chaine_v1.sh` (inchangé, R12) plus `chmod -R a+rX` sur `/opt/elan`,
     `/opt/mathlib`, `/opt/pybac`, après `go-w` et avant le montage en lecture seule ;
   - plus une **garde de lisibilité** (code 5, ligne « ARRÊT » au journal d'installation) : aucun fichier ni dossier de ces
     arbres fermé aux autres, aucun dossier non traversable, aucun exécutable non exécutable par les autres ; `bac` (par
     `runuser`) lit `/opt`, `/opt/harnais`, les trois racines, `Mathlib.olean`, le Python du bras S, les dossiers existants
     de `LEAN_PATH`, et exécute `lean` et ce Python.
   - **Essai R5 neuf « `bac` lit `Mathlib.olean` »** (`essai_lecture_bac_v1.sh`), joué par le pilote à la fin de la phase
     « avant », avant la coupure : cas sain (un octet de `Mathlib.olean` vraiment lu par `bac`), témoin 0644 lu, artefact
     0600 refusé. Non conforme : le pilote s'arrête.
2. **Pilote, clé d'hôte et `~/.ssh`** (incident 5, écart 7) : `scp` reçoit aussi `-o StrictHostKeyChecking=accept-new`, comme
   `ssh` ; la première copie, qui précède tout `ssh`, enregistre la clé d'hôte d'un serveur jamais vu (une clé **différente**
   d'une clé déjà connue reste refusée). Le pilote crée `~/.ssh` (700) s'il manque. Plus de `ssh … true` préalable.
3. **Faux « ouverte » du résolveur après la coupure** (incident 6) :
   - `sonde_reseau_v2.py` (la v1 reste, R12) interroge le résolveur système sur **un nom aléatoire jamais demandé**
     (`<32 hexadécimaux>.example.com`) : aucune réponse en cache possible. Une adresse ou un « nom inexistant » revenu :
     « ouverte » ; aucune réponse (EAI_AGAIN) : « fermée » ; toute autre cause : « indéterminée », qui est un écart.
   - Les trois sondes du pilote (avant, après coupure, fin) sont la v2. L'exécuteur du bac importe toujours la v1, copiée
     dans `/opt/harnais` ; elle est protégée par le point suivant.
   - Après la coupure et avant la sonde, le pilote vide le cache du résolveur du serveur (`resolvectl flush-caches`) ; réseau
     coupé, le cache ne peut plus se remplir. Commande absente ou en échec : arrêt du pilote.
4. **Source SSH en réseau** (incident 4, écart 6 ; **accordé par Lazar**) : le poste sort par au moins deux adresses IPv4 du
   même /24, et le port 22 n'était joignable qu'environ une fois sur huit avec une règle à une seule adresse.
   - `MV7 adresses-sortie --ip-poste IP_POSTE` (section 0) mesure, par 16 requêtes à un service qui renvoie l'adresse vue,
     le nombre d'adresses de sortie ; il ne rend que des comptes et `prefixe_conseille` : **32** si la seule adresse vue est
     `IP_POSTE`, **24** si toutes sont dans son /24 ; code 1 (et aucune suite) si une adresse sort du /24 ou si rien n'a
     répondu. Jamais une adresse écrite.
   - `acces-creer` et `acces-couper` prennent `--prefixe-poste P` (défaut 32 ; 24 au plus large, tout autre refusé) ; la
     source des règles est `IP_POSTE/P`. La règle sortante de coupure ne change pas : le trafic sortant reste coupé.
   - `garde-poste` contrôle aussi le /24 du poste : toute adresse `a.b.c.x` du même /24 dans un fichier versé est refusée.
5. **Clone `--single-branch`** (incident 3, écart 5) : `fichier_pousse` (inchangé) lit l'amont de la branche ; L3 prescrit
   désormais la référence de suivi (voir L3).
6. **Section 0** : poste sous WSL (Ubuntu) prévu ; jeton de `gh` pour `git` sur le dépôt privé ; essai à blanc « fin et
   reprise » = relance réelle de l'hôte de la session, vérifiée par l'heure de démarrage du processus.
7. **GO** : *(texte de la v8 remplacé par le point 1 des changements depuis v8 : `GO-2026-11-10-13`, branche du poste neuve
   sans les pièces du premier essai dans `V`.)*
8. Module `minuterie_v7` (copie de la v6, R12), d'où `MV7` partout ; pilote `piloter_poste_v8.sh` ; noms des sorties du pilote (`*-v6.*`) et des fichiers
   écrits sur la machine (`journal-installation-v1.txt`, `chaine-v1.json`) gardés.
9. Essais : `tests/test_lean_essai_minuterie_v7.py`, `tests/test_lean_essai_pilote_v8.py`, `tests/test_lean_essai_sonde_v2.py` ;
   mutations `scripts/lean_essai_d1a_v8/mutations_harnais_v8.py` (journal `journal-mutations-harnais-v8.json`).

## Rappel : ce qui changeait de la v5 à la v6

- **CLC5-02** : trois tâches de la mère au lieu de deux.
  - Une dans sa session, à `H`.
  - **Deux qui ouvrent une session neuve**, à `H + 30 min` et à `H + 24 h`.
  - Les identifiants des trois sont inscrits dans `registres/etat.md` et dans chaque passation.
  - Lazar pose son propre rappel à `H + 1 h`.
- **CLC5-04** : une ligne « en tâche jusqu'à … » dans `registres/etat.md`, écrite par la mère à l'armement, pour que la
  routine de reprise ne détruise pas le serveur au travail.
- **CLC5-05** : les commandes du harnais tournent **hors du bac à sable de Claude Code** sur le poste, après un essai à blanc.
- **CLC5-07** : **aucune donnée du poste de Lazar dans un fichier versé ou poussé**.
  - Son adresse IPv4 ne vit qu'en mémoire, comme argument de commande. Le fichier d'accès ne la porte plus.
  - La clé part sans son commentaire, souvent `utilisateur@machine`. Les sorties ne portent que des chemins relatifs au
    clone.
  - **`garde-poste` précède chaque commit.**
- **Mot « armée »** : il porte l'empreinte (sha256) du fichier de rattrapage lu par la mère. `creer-et-armer` exige cette
  empreinte (`--empreinte-mere`) et la compare avant tout appel.
- **Création** :
  - la clé SSH et le pare-feu sont pris dans le fichier d'accès poussé : plus de `--cle-ssh` ni de `--pare-feu` ;
  - une seconde préparation est refusée, même dans un clone sans journal des créations (CLC5-03) ;
  - le contrôle de survie n'est plus trompé par la course de l'`exec` (CLC5-01).
- **Bornes** :
  - `detruire` et `inventaire` rendent le code 5 au-delà de 8 minutes de panne passagère ;
  - le pilote borne chaque commande SSH.

## Rôles et règle d'or

- **Session locale** : clone du dépôt, jeton `HCLOUD_TOKEN` dans son environnement (lu par son nom, jamais affiché ni écrit),
  SSH vers la machine. Elle seule crée.
- **Session mère** : dans le nuage, sans SSH, avec son propre `HCLOUD_TOKEN`. Elle lit et détruit par identifiant, par des
  requêtes de l'interface, sans aucun code de la branche.
- **Lazar** : relaie entre les deux sessions, qui ne se parlent pas. Il donne à la session locale l'adresse IPv4 publique du
  poste, **dans la conversation seulement**.
- **Règle d'or** :
  - aucune création avant le mot « armée » de la mère, avec son empreinte ;
  - une seule préparation, une seule création ; jamais de recréation ; jamais de relance d'une minuterie.

## 0. Prérequis du poste (session locale)

1. **Dépôt** :
   - **un seul clone** de `https://github.com/lciric/controle-ia-travail` ; `git remote -v` le montre, jamais
     `lciric/controle-ia` ;
   - branche de travail à soi, au nom fixé par la consigne, partie du commit ci-dessus, poussée avec `git push -u` ;
   - **poste sous Windows** : tout se fait sous WSL (Ubuntu), clone dans le système de fichiers Linux (jamais sous
     `/mnt/c`) ; le premier lancement d'Ubuntu est fait par Lazar ;
   - **terminal WSL ouvert pendant tout l'essai** (v10, incident R-2434) : un terminal Ubuntu ouvert par Lazar avant
     l'essai à blanc, gardé ouvert jusqu'à l'inventaire final de la section 5 ; vérifié avant l'essai à blanc et avant L1
     (sinon, aucune préparation) ; s'il se ferme après L5 : `MV7 verifier-minuterie` tout de suite, et non conforme :
     `MV7 detruire --identifiant N`, jamais de relance ;
   - **dépôt privé** : `git` (clone, fetch, push, et la lecture `git ls-remote` de `creer-et-armer`) reçoit le jeton de `gh`
     par l'environnement du seul processus (`GIT_CONFIG_*` ou l'assistant d'identification de `gh`), jamais écrit dans un
     fichier ni affiché ;
   - **toutes les commandes se lancent depuis la racine du clone**.
2. **Outils** :
   - Python 3.11 ou plus récent (essais passés sous 3.11 et 3.13 ; bibliothèque standard seule pour la minuterie) ;
   - `git`, `ssh`, `ssh-keygen`.
3. **Jeton** : `HCLOUD_TOKEN` est posé par Lazar dans l'environnement de la session. C'est un jeton en lecture et écriture du
   projet de l'essai. Jamais `env`, `printenv` ni affichage.
4. **Hors du bac à sable de Claude Code (CLC5-05)** : les commandes du harnais (`minuterie_v7`, pilote) tournent sans le bac
   à sable, selon le réglage que Lazar choisit. Elles sont pré-autorisées, pour qu'aucune destruction n'attende une demande
   de permission. **Essai à blanc** avant L1 :
   - `python3 -c "import subprocess; p = subprocess.Popen(['sleep', '900'], start_new_session=True); print(p.pid)"`,
     puis, dans une **autre** commande, `kill -0 <PID>`, qui doit réussir ;
   - après une fin puis une reprise **réelles** de la session — l'hôte de la session est relancé, pas seulement la
     conversation — `kill -0 <PID>` doit réussir encore ; ensuite `kill <PID>` (R10). La relance se vérifie par l'heure de
     démarrage : `ps -o lstart= -p <PID de l'hôte de la session>` doit être **plus récente** que
     `ps -o lstart= -p <PID du sleep>` ;
   - `python3 -c "import urllib.request; print(sorted(urllib.request.getproxies()))"` n'imprime que des noms, jamais une
     valeur. Il doit rendre `[]`, ou un mandataire du système, jamais un mandataire propre à la session ;
   - si l'un des trois échoue : arrêt, compte rendu à Lazar, aucune préparation.
5. **Adresses de sortie** (avant L2) : `MV7 adresses-sortie --ip-poste IP_POSTE`.
   - Code 0 : retenir `prefixe_conseille` comme `P` (32 ou 24), passé à `acces-creer` et à `acces-couper`. **Jamais
     `--prefixe-poste 24` sans cette mesure.** Si elle rend 32 alors que le premier essai a établi plusieurs adresses de
     sortie du même /24 (rapport, incident 4), le signaler à Lazar avant L2.
   - Code 1 (adresse hors du /24, ou aucune réponse) : arrêt, compte rendu à Lazar, aucune préparation.
   - La commande ne rend aucune adresse ; rien de sa sortie n'est versé.
6. **Vérificateur du noyau** : `stat -c %a src/controle_ia/lean_essai/verificateur_noyau_v5.lean` doit rendre `644`.
   Sinon `chmod 644` de ce seul fichier dans le clone, sans commit, puis refaire le `stat`.
7. **Ordinateur** :
   - sur secteur, veille coupée, **capot ouvert**, pas de déconnexion de la session, jusqu'à la destruction ;
   - sous macOS, `caffeinate -i -w <PID de la minuterie>`, lancé détaché après L6 (il n'empêche pas la veille capot fermé).
8. **Notation** :
   - `MV7` désigne `PYTHONPATH=src python3 -B -m controle_ia.lean_essai.minuterie_v7` ;
   - `V` désigne `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1` ;
   - `IP_POSTE` est l'adresse donnée par Lazar ; elle n'est jamais écrite dans un fichier du clone ;
   - tout fichier passé à `--journal` ou à `--sortie` porte un nom neuf (R12).
9. **Avant chaque commit** : `MV7 garde-poste --ip-poste IP_POSTE && git commit …`.
   - La commande lit l'index git et refuse (code 1) s'il porte l'adresse du poste, une adresse de son /24, son dossier
     personnel ou le chemin du clone.
   - Elle n'en écrit jamais la valeur, seulement la nature.

## 1. Avant la création

### L1 (locale) — préparer, une seule fois

```
MV7 preparer --go GO-2026-11-10-13 --heure-limite-creation <T_LIM> --heure-tache-mere <H>
```

- `T_LIM` et `H` sont fixés par la consigne, en ISO 8601 UTC.
- **Refus** :
  - `T_LIM` déjà passée ;
  - `H` moins de 2 heures après `T_LIM`, ou plus de 47 heures après maintenant ;
  - GO invalide ;
  - machine déjà inscrite sous ce GO ;
  - **un autre fichier `rattrapage-machine-d1a-*` déjà dans `V` (CLC5-03)**.
- **Fichier écrit** : `V/rattrapage-machine-d1a-<jeton12>-v1.json`. Il contient :
  - le jeton, les étiquettes fixes et le nom ;
  - l'heure de préparation et l'heure limite de création ;
  - l'échéance au plus tard `H − 1 h` ;
  - **les trois tâches de la mère** (heure, mode, message autosuffisant avec les formes `curl`) ;
  - **la ligne d'état de la mère** et l'heure du rappel de Lazar (`H + 1 h`) ;
  - les commandes de destruction du poste.

### L2 (locale) — clé SSH et pare-feu étiquetés

```
ssh-keygen -t ed25519 -N "" -C lean-outillage-d1a -f <dossier hors du dépôt>/cle-lean-d1a
MV7 acces-creer --rattrapage V/rattrapage-machine-d1a-<jeton12>-v1.json \
    --cle-publique <dossier hors du dépôt>/cle-lean-d1a.pub --ip-poste IP_POSTE --prefixe-poste P
```

- **Objets créés** (gratuits) : une clé SSH et un pare-feu, nommés `lean-outillage-d1a-<jeton12>` et étiquetés `essai`,
  `pas`, `go`, `creation=<jeton>`. Le pare-feu porte les règles d'installation (SSH depuis le seul réseau
  `IP_POSTE/P`).
- La clé est envoyée **sans son commentaire**.
- **Fichier écrit** : `V/acces-machine-d1a-<jeton12>-v1.json`, avec les identifiants et l'empreinte de la clé, **sans
  l'adresse du poste ni les règles**.

### L3 (locale) — pousser avant toute création

- `MV7 garde-poste --ip-poste IP_POSTE`, puis committer et pousser les deux fichiers.
- **Référence de suivi** (clone `--single-branch`, premier essai) : après `git push -u origin <branche>`,
  `git fetch origin <branche>:refs/remotes/origin/<branche>` puis `git remote set-branches --add origin <branche>` ;
  `git rev-parse --abbrev-ref @{upstream}` doit rendre `origin/<branche>`. Sinon `creer-et-armer` s'arrête avant tout appel
  (« branche sans amont »).
- Donner à Lazar, pour la mère :
  - la branche et le commit ;
  - le jeton ;
  - les identifiants de la clé et du pare-feu, et l'empreinte de la clé.

### M1 à M6 (mère) — s'armer avant la création

- **M1 — lire** : `git fetch` de la branche du poste, relecture des deux fichiers, et calcul de **l'empreinte sha256 du
  fichier de rattrapage tel que poussé**.
- **M2 — même projet** : par son propre jeton,
  - `GET /v1/ssh_keys?label_selector=creation%3D<jeton>` doit rendre une seule clé, de même identifiant et de même
    empreinte ;
  - `GET /v1/firewalls?label_selector=creation%3D<jeton>` doit rendre un seul pare-feu, de même identifiant ;
  - des réponses, n'afficher que les identifiants et les noms : les règles portent l'adresse du poste.
  - Sinon : **arrêt, aucune création**.
- **M3 — droit d'écrire** : `POST /v1/firewalls` avec `{"name": "preuve-ecriture-mere-<jeton12>", "labels": {"essai":
  "lean", "preuve": "mere"}}`, puis `DELETE` du même identifiant, puis `GET`, qui doit rendre 404. C'est gratuit. Un 401 ou un
  403 : arrêt.
- **M4 — destruction à blanc** : les deux listes (par étiquettes et par nom) ne rendent aucun serveur.
- **M5 — trois tâches** (CLC5-02), aux heures absolues du fichier, chacune avec son message recopié tel quel :
  - **T1**, à `H` : rappel dans la session mère (`send_later`).
  - **T2**, à `H + 30 min` : **tâche programmée qui ouvre une session neuve** à son déclenchement.
  - **T3**, à `H + 24 h` : de même.
  - Relire les trois après création : actives, prochaine heure exacte.
  - La session qui porte T1 n'est pas archivée avant « aucun serveur de l'essai ».
- **M5 bis — ligne d'état** (CLC5-04) : recopier `ligne_etat_mere` du fichier dans `registres/etat.md`, avec les identifiants
  des trois tâches, puis committer. La reprendre dans chaque passation jusqu'à la destruction confirmée.
  - La routine de reprise (R-2322) ne détruit pas un serveur en tâche avant l'heure de cette ligne.
  - Au-delà de cette heure, ou si la ligne manque, elle le détruit.
- **M6 — signaler** : dire à Lazar « armée », avec **l'empreinte sha256 du fichier de rattrapage**, les identifiants des
  tâches, `H`, `H + 30 min` et `H + 24 h`.
  - Lazar le transmet à la session locale, et pose son rappel personnel à `H + 1 h` : console de Hetzner, zéro serveur
    attendu.
  - **Sans ce mot, aucune création.**

## 2. Création (session locale)

### L4 — juste avant

- `MV7 inventaire` doit rendre « aucun serveur de l'essai ».
- L'heure doit être avant `T_LIM`.
- Le mot « armée » doit être reçu, avec son empreinte.

### L5 — création détachée, une seule fois

```
MV7 creer-et-armer --go GO-2026-11-10-13 --rattrapage V/rattrapage-machine-d1a-<jeton12>-v1.json \
    --empreinte-mere <empreinte du mot « armée »> --type ccx33 --lieu <lieu du devis> --deja-depense-usd 0.56 \
    --journal V/journal-creation-d1a-<jeton12>-v1.jsonl --detache --sortie V/sortie-creation-d1a-<jeton12>-v1.log
```

- **Ce que rend la commande** : tout de suite, le PID du processus détaché et le chemin relatif de la sortie.
- **Ce que fait le processus**, dans l'ordre :
  1. contrôles, avant tout appel :
     - empreinte égale à celle du mot « armée » ;
     - aucun autre fichier de rattrapage ;
     - heure limite ;
     - fichiers de rattrapage **et** d'accès poussés (lus par `git ls-remote`) ;
     - GO, seconde machine refusée, type dans la liste du devis, taux d'au moins 1,25, devis ;
  2. intention écrite avant l'appel ;
  3. création avec la clé et le pare-feu du fichier d'accès ; si la réponse se perd, rattrapage par l'étiquette pendant
     10 minutes ;
  4. minuterie détachée, d'échéance `min(création + 48 h, H − 1 h)` ;
  5. **contrôle de survie par `poll()`** : processus vivant et première ligne « garder » en 120 secondes ; sinon,
     destruction immédiate par l'identifiant.
- **Attendre** la fin du processus (`kill -0 <PID>` toutes les 15 secondes, 15 minutes au plus), puis lire la sortie.
- **Fin normale** : la dernière ligne est un objet JSON avec `identifiant`, `echeance`, `minuterie.pid`,
  `minuterie.fichier_pid` et `minuterie.journal` (chemins relatifs au clone).
- **Toute autre fin** : section 4. **Aucun second essai** ; le code le refuse de toute façon.

### L6 — dans la minute

```
MV7 verifier-minuterie --fichier-pid <minuterie.fichier_pid> --journal-minuterie <minuterie.journal>
```

- Il doit rendre `"conforme": true`.
- Sinon, refaire deux minutes plus tard. Encore non conforme : `MV7 detruire --identifiant <N> --journal <neuf>`, puis
  `MV7 inventaire`, arrêt, compte rendu. **Jamais de relance de la minuterie.**

### L7 — pousser et signaler, tout de suite

- `MV7 garde-poste --ip-poste IP_POSTE`, puis pousser : le journal des créations, le fichier PID, le journal et la sortie de
  la minuterie, la sortie et le journal de la création.
- Donner à Lazar, pour la mère : l'identifiant, l'échéance et le PID.

## 3. Pendant le travail (session locale)

- **Adresse du serveur** : `MV7 adresse-serveur --identifiant N`. Cette adresse est utilisée seulement en argument, jamais
  versée.
- **Clé d'hôte** : avant le premier pilote, si l'adresse du serveur est déjà dans `~/.ssh/known_hosts` du poste
  (`ssh-keygen -F <adresse du serveur>` rend une ligne), `ssh-keygen -R <adresse du serveur>` ; sinon rien.
- **Ordre** :
  1. `scripts/lean_essai_d1a_v9/piloter_poste_v9.sh avant <adresse du serveur> <clé privée> <commit de Mathlib>` ;
     code non nul (installation, garde de lisibilité, sonde, « bac lit Mathlib.olean », « le vérificateur compile sur la
     machine ») : **ni coupure, ni pilote « apres »** ; section 5, compte rendu ;
  2. `MV7 acces-couper --rattrapage … --ip-poste IP_POSTE --prefixe-poste P`, puis
     `MV7 verifier-coupure --serveur N --pare-feu F --journal <neuf>` (adresses masquées) ;
  3. `piloter_poste_v9.sh apres <adresse du serveur> <clé privée> <dossier de sorties hors du clone>`.
- **Le pilote se lance en arrière-plan**, sorties dans des fichiers : l'installation dépasse la limite d'une commande de
  premier plan. Chaque commande SSH est bornée par `timeout` côté serveur ; une connexion qui pend l'est par
  `ConnectTimeout` et `ServerAlive*`.
- **Pièces du pilote** : elles ne vont dans `V` qu'après `MV7 garde-poste --ip-poste IP_POSTE --fichier <pièce>` (code 0).
- **À chaque reprise de session, et au moins toutes les heures** : lire la sortie de la création et le fichier PID, puis
  `MV7 verifier-minuterie … --journal-minuterie …`.
  - Non conforme deux fois, à 2 minutes d'écart : `MV7 detruire --identifiant N`.
  - Jamais de relance.
- **Ne jamais** renommer le serveur ni toucher à ses étiquettes.
- **Machine injoignable** : `MV7 inventaire`. Si le serveur est absent (la mère, la minuterie ou la routine de reprise l'a
  détruit) : **ne pas recréer**, compte rendu.
- **Commande bornée** : `detruire` ou `inventaire` qui rend le code 5 (panne passagère de plus de 8 minutes), ou qu'un outil
  coupe sans code : refaire 15 minutes plus tard, puis prévenir Lazar et la mère.

## 4. Fin anormale de la création (session locale)

1. `MV7 detruire --pas d1a --journal <neuf>` tout de suite.
   - Code 0 : lire `detruits`.
   - **Code 3** : Lazar détruit à la main, par l'identifiant, dans la console.
   - Codes 4 et 5 : refaire.
2. `MV7 inventaire` doit rendre « aucun serveur de l'essai ».
3. **Quinze minutes plus tard**, refaire 1 et 2.
4. Compte rendu à Lazar ; aucun second essai.

## 5. Fin normale

1. **Locale** : `MV7 detruire --identifiant N --journal <neuf>`. Code 3 : destruction à la main.
2. **Locale** : `MV7 inventaire` doit rendre « aucun serveur de l'essai », avec `ips_primaires_non_attribuees` vide. Sinon,
   le signaler sans rien supprimer.
3. **Locale** : `MV7 acces-supprimer --rattrapage …`.
4. **Locale** : `MV7 verifier-minuterie …`. Si la minuterie vit encore, l'arrêter par son PID (`kill <PID>`, R10).
5. **Locale** : `MV7 garde-poste --ip-poste IP_POSTE`, puis pousser toutes les pièces. Lazar prévient la mère.
6. **Mère** :
   - relire par son propre jeton (M4) ;
   - inscrire l'arrêt dans `registres/arrets.md` et clore la ligne « en tâche jusqu'à » ;
   - alors seulement, désarmer T1 à T3, ou les laisser tourner : elles ne trouveront rien.
   - Aucune copie publique avant une relecture des pièces versées (CLC5-07).

## 6. Codes de sortie de `minuterie_v7`

| Code | Sens |
|---|---|
| 0 | Fait. |
| 1 | Arrêt : refus, ou serveur créé puis détruit ; erreur inattendue, avec une trace aux chemins masqués. Lire le message. |
| 2 | Usage. |
| **3** | **Destruction refusée durablement (401 ou 403)** : le détruire à la main par son identifiant. |
| **4** | **Rattrapage à refaire** : `detruire --pas d1a` maintenant, puis quinze minutes plus tard. |
| **5** | **Panne passagère plus longue que la borne** : refaire dans 15 minutes, puis prévenir Lazar et la mère. |

## 7. Réserves

- **Aucun appel réel n'a été fait.** Les premières lectures réelles sont M2 et M4, faites par la mère.
- **Le vérificateur v5 n'a tourné que hors machine, sans isolement** (mode « essai-local » de l'exécuteur v5) : dans le
  bac (bwrap, systemd, `MemoryMax=6G`), son premier passage est l'essai R5 de compilation (avant la coupure), puis le
  premier pas `noyau`. Mesuré hors machine : environ 8 s et 2,1 Gio de mémoire anonyme par passage, plus 6,9 Gio de pages
  des fichiers `.olean` (récupérables), contre 0,4 Gio de mémoire anonyme pour la compilation d'un item.
- **La minuterie locale meurt avec l'ordinateur** (extinction, déconnexion). Les garde-fous de fond sont T1 à T3, la ligne
  d'état lue par la routine de reprise, et le rappel de Lazar.
- **Coût au pire**, garde-fous locaux morts :
  - jusqu'à `H` (47 heures après la préparation au plus) si T1 agit ; `H + 30 min` si seule T2 agit ; `H + 24 h` si seule T3
    agit, soit 71 heures, environ 30 USD pour `ccx33` (extrapolation de la contre-lecture, non vérifiée ici) ;
  - au-delà, seuls le rappel de Lazar et la routine de reprise restent.
- **Le bac à sable et le mandataire du poste ne sont pas éprouvés ici.** L'essai à blanc du point 4 de la section 0 en décide.
- **`garde-poste`** :
  - il ne lit que ce qu'on lui donne (l'index git, ou des fichiers nommés) ;
  - il ne connaît ni le nom de la machine ni celui de l'utilisateur, seulement l'adresse, le dossier personnel et le chemin
    du clone. Le reste tient à la discipline de la consigne.
