# Ordre de lancement proposé — course de dose–réponse de l'organisme à consigne cachée — v6

[v6 : corrections V5-B2, V5-m1 et V5-m2 de la vérification de la v5 (relayées par la mère le 24 novembre 2026 vers 16:56 UTC) ; V5-B1 réglé par la mère (R-5328 : pièce de `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` sous `registres/code-lecteur-du-texte-dose-reponse/`, même empreinte). Rien d'autre ne change. La v5 reste telle quelle (R12).]

[v5 : branche (b) du préalable 3 jouée, au mot de Lazar (GO-2026-11-24-31 : « (b) avec (A) ») : course désignée pour le critère 3, option A, texte de désignation scellé `prereg/G0-critere-3-designation-course-v1.md` (`19dbc99edb551a4e1bbbef0ea28a5a860bd739b69d84d60ccf43c2de03125c31`). Code du lancement : commit `6b2b821a28f8bebebae2188d9f020ce731464306` (amorce et lanceur v3, qui extraient le texte de désignation sur l'instance ; lecteur du texte v2). Changent seulement : préalables 1 et 3, section 1 (commit du code, texte de désignation et fichier de désignation portés sur la branche de lancement), section 2 (historique complet, vérification du code du lecteur, lanceur et amorce v3), section 5 (étapes du lecteur du texte et des doses jugées). La v4 reste telle quelle (R12).]

Pièce de classe A (ordre d'une course payante), proposée par le développeur, contre-lue (R2), scellée par la mère, jouée par la mère seulement. Texte qui fait foi : `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (`2263c5c447d17e0d2b045ba1a6421c681809df2ec8bafbcc3226aa6dd3f31c41`). Ligne de GO : `GO-2026-11-24-25` (calcul, 90 USD, échéance au registre le 15 décembre 2026). Bornes : une A100 SXM4 80 Go, au plus 1,30 USD de l'heure, 16 cœurs, 128 000 Mo de mémoire vive, disque d'au moins 300 Go, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go. Dépôt : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` (jamais `lciric/controle-ia`). Plafond : 90 USD cumulés sur toutes les tentatives ; alerte unique à 72 USD.

## 0. Préalables (aucune création sans eux)

1. Ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` **v2**, commit `6b2b821a28f8bebebae2188d9f020ce731464306` : **déjà inscrite sur main** (R-5327), pièce `registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json` (`79358ccbfc50be27f053e0666759bc7ddc99ca41bc48e6a5ffdc2629bca0d109` ; le chemin porte le commit, comme l'exige `controles_v2.controler_registre`). La ligne v1 (`a02b6540070aa5731875d07fbbe124f2dbe27f3b`, R-5306) reste inscrite ; le lancement ne joue que le code de `6b2b821a28f8bebebae2188d9f020ce731464306`.

1 bis. Avant l'étape 1, la mère inscrit sur main une pièce neuve, `registres/code-dose-reponse-consigne-cachee/DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v1.json`, scellée. Elle porte :
- l'identifiant de la session de lancement (la mère elle-même si elle lance) ;
- la phrase « aucune action générée sous un texte de la pièce jointe (7a5f633c…) ni du fichier du premier test (a68468fe…) » ;
- le renvoi à la ligne CODE.

La mère inscrit aussi sa ligne `DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE` au registre des scellements, avant que l'étape 1 copie ce registre sur la branche de lancement. Sans cette ligne : aucune création. (Le code ne contrôle pas cette ligne : la session de lancement la vérifie à la main, `grep DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE registres/scellements-v1.md` sur la branche de lancement, avant `controles`.)

2. Banque de 64 tâches : inscrite (R-5306), ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE`, fichier `donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json` sur la branche `banque/dose-reponse-consigne-cachee-v1`, empreinte attendue `0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4`.

3. Texte de désignation de la course pour le critère 3 : **branche (b) jouée** (mot de Lazar, GO-2026-11-24-31, option A). La création exige, au registre des scellements de main copié sur la branche de lancement, ces quatre lignes, et les contrôles d'avant création les vérifient (`designation_critere_3.lignes_registre`, CL-06 de la contre-lecture du lecteur ; liste d'arrêt du texte de désignation) :
   - `DESIGNATION-CRITERE-3` : inscrite (R-5308), `prereg/G0-critere-3-designation-course-v1.md`, `19dbc99e…` ;
   - `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` : **déjà inscrite sur main** (R-5327 ; chemin corrigé R-5328), pièce `registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json` (`f6bc347aeaa424127d0a6614dd5cf2d7d55de524f1c7f132f1532e099b053013`, écrite par `lecteur_texte_dose_reponse_v2.py ecrire-fichier-code`) ; contre-lecture et vérification citées : `contre-lecture-1-lecteur-texte-et-amorce-v3-v1.md` (`cabdf135…`), `verification-1-lecteur-texte-v2.md` (`b4f69832…`, « prêt ») ;
   - `SONDES-LUES-CRITERE-3` : **déjà inscrite sur main** (R-5327), pièce `registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md` (`b354fc38608d62cb2036d61104508032f0656d374260497ba2d5e44158be9773`) ;
   - `CODE-MOTS-ET-COUT-T06` : inscrite.

   Le texte de désignation demande ces lignes « avant la création de l'instance » : toute ligne inscrite après la création rendrait la course non désignée (CL-06). Sans l'une d'elles : aucune création.

4. Nœud tranché : les deux contrôles croisés sont reportés à une course suivante (décision de Lazar, R-5280) ; quinze conditions.

5. Session de lancement : `python3 -m venv <bloc-notes>/venv-dr && . <bloc-notes>/venv-dr/bin/activate && pip install -r requirements-cpu.txt -r requirements-pilotage.txt`, environnement créé une fois, ici, et activé ensuite par `. <bloc-notes>/venv-dr/bin/activate` (`torch` est exigé : `controles_v2` importe `environnements.pilote_a`, qui importe `torch` ; `vastai==1.8.3` lit `VAST_API_KEY` par son nom). Activer l'environnement en tête de chaque appel du terminal. `HF_TOKEN` lu par son nom, avec accès au modèle Llama-3.1-8B-Instruct (`controles` charge le tokeniseur seul pour le rapport des longueurs en jetons, avant toute création ; rien n'est affiché que des comptes). `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` est écrit en dur dans la commande de création ; le dépôt `origin` de la session doit être `lciric/controle-ia-travail`.

6. Calendrier : fin effective de l'accord : celle du registre, 16 décembre 00:00 UTC (le code lit le lendemain 00:00 UTC de l'échéance du registre). Pour tenir aussi la lettre du devis, aucune création après le 12 décembre à 07:00 UTC (le lanceur refuse déjà tout jour après le 12 décembre).

7. Appels du terminal sans état : `GO_ID=GO-2026-11-24-25`, l'activation de l'environnement et l'export du jeton GitHub (section 2) se répètent en tête de chaque appel.

## 1. Branche de lancement (session de la mère)

**À partir du commit du code `C = 6b2b821a28f8bebebae2188d9f020ce731464306`, jamais de `main`** : le lanceur et l'amorce exigent que `src/`, `scripts/`, `tests/`, `.claude/`, `pyproject.toml` et `requirements-*.txt` du commit de lancement égalent ceux de `C`. Sur la branche de lancement ne s'ajoutent que des données et des registres. L'arbre principal de la mère n'est pas basculé : la branche vit dans un arbre de travail du bloc-notes, et **toutes les commandes des sections 1 à 4 se jouent depuis `<bloc-notes>/lancement-dr`** (`cd` en tête de chaque appel) ; jamais le lanceur de main.

```bash
set -euo pipefail
git worktree add <bloc-notes>/lancement-dr -b lancement/dose-reponse-v1 6b2b821a28f8bebebae2188d9f020ce731464306
cd <bloc-notes>/lancement-dr && . <bloc-notes>/venv-dr/bin/activate
git fetch origin main banque/dose-reponse-consigne-cachee-v1
git checkout origin/main -- registres/go.md registres/scellements-v1.md
git checkout origin/main -- prereg/G0-critere-3-designation-course-v1.md prereg/G0-critere-3-designation-course-v1.md.sha256
git checkout origin/main -- registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json.sha256 registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md.sha256 registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json.sha256
printf '%s\n' '{"chemin": "prereg/G0-critere-3-designation-course-v1.md", "sha256": "19dbc99edb551a4e1bbbef0ea28a5a860bd739b69d84d60ccf43c2de03125c31", "lignes_registre": ["DESIGNATION-CRITERE-3", "CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE", "SONDES-LUES-CRITERE-3", "CODE-MOTS-ET-COUT-T06"]}' > <bloc-notes>/designation-critere-3.json
git checkout origin/banque/dose-reponse-consigne-cachee-v1 -- donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256
grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md || { echo "préalable 1 bis absent : aucune création"; exit 1; }   # arrêt : ne rien jouer de plus
PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v2.py donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json 6b2b821a28f8bebebae2188d9f020ce731464306 --designation <bloc-notes>/designation-critere-3.json
git add -f donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256 prereg/T0.6-dose-reponse-configuration-course-v1.json prereg/T0.6-dose-reponse-configuration-course-v1.json.sha256 prereg/G0-critere-3-designation-course-v1.md prereg/G0-critere-3-designation-course-v1.md.sha256 registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json.sha256 registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md.sha256 registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-6b2b821a28f8bebebae2188d9f020ce731464306-v2.json.sha256 registres/go.md registres/scellements-v1.md
git commit -m "Lancement de la course de dose-réponse désignée : configuration, banque, texte de désignation, registres"
git push -u origin lancement/dose-reponse-v1
```

Empreinte attendue de la banque : `0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4` (ligne BANQUE ; le script de configuration la lit sur le compagnon et les contrôles la comparent à la ligne). `--designation` porte le fichier de désignation écrit ci-dessus (chemin, empreinte et les quatre lignes du préalable 3) ; la configuration le reprend sous `designation_critere_3`, et l'amorce v3 extrait le texte de désignation sur l'instance, où `controles_v2.controler_registre` vérifie son empreinte et les quatre lignes. Le texte scellé, la pièce jointe et le fichier du premier test sont déjà au commit `C`. La configuration doit égaler, clé pour clé, celle que reconstruit le code.

## 2. Contrôles, puis création imprimée

Avant `controles`, dans un appel qui commence par les mêmes `cd` et activation : historique complet, puis vérification du code du lecteur du texte et du code de T0.6 qu'il reprend (liste d'arrêt du texte de désignation : « la ligne `CODE-MOTS-ET-COUT-T06` absente à la création de l'instance, ou le code qu'elle cite altéré : aucune création ») :

```bash
cd <bloc-notes>/lancement-dr && . <bloc-notes>/venv-dr/bin/activate \
  && { [ "$(git rev-parse --is-shallow-repository)" = false ] || git fetch --unshallow origin; } \
  && PYTHONPATH=src python -P -B scripts/lecteur_texte_dose_reponse_v2.py verifier-code
```

Code autre que 0 : aucune création. En particulier, si `verifier-code` refuse encore le commit `da06bb57` (cité par `CODE-MOTS-ET-COUT-T06`) après le `git fetch --unshallow` : nœud de Lazar, aucune création.

Les pièces des lignes `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, `SONDES-LUES-CRITERE-3` et `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` v2 sont portées sur la branche de lancement (section 1, V5-B2) : `verifier-code` et les contrôles d'avant création les lisent à leurs chemins du registre.

Jeton GitHub de l'instance : `_3`, repli `_2`. Dans **chaque** appel du terminal qui joue `creation`, la commande de création imprimée ou `surveillance`, précéder la commande de `export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}"`. Le lanceur la choisit alors, et la masque. Les appels du terminal ne gardent pas leurs variables : l'export se répète à chaque appel. Si l'amorce refuse avec « clonage impossible » ou « poussée initiale de la branche … refusée », l'instance se détruit seule en 3 minutes environ. Rejouer alors `creation` sans cet export (repli sur `_2`) ; c'est un essai de création de plus, trois au plus, et sa dépense entre dans la dépense antérieure. Attendre que `timeout -k 5 120 vastai show instances` ne la liste plus (au plus 40 minutes, sinon destruction par l'identifiant après relevé de la branche), avant de rejouer `creation`.

```bash
cd <bloc-notes>/lancement-dr && grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md && . <bloc-notes>/venv-dr/bin/activate && export GO_ID=GO-2026-11-24-25 \
  && export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}" \
  && DR_BRANCHE_LANCEMENT=lancement/dose-reponse-v1 DR_AMORCE_SHA256=722390c3460a882f4b8f809533917e0bf2e0ec6b8fafde2311b885455f614e64 \
     DR_ESSAIS=8 bash scripts/lancer_dose_reponse_v3.sh controles <dossier neuf du bloc-notes>
cd <bloc-notes>/lancement-dr && grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md && . <bloc-notes>/venv-dr/bin/activate && export GO_ID=GO-2026-11-24-25 \
  && export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}" \
  && bash scripts/lancer_dose_reponse_v3.sh creation auto course <dépense antérieure relevée sur la facture du loueur, 0 à la première tentative> <même dossier>
```

`creation` imprime la commande littérale de création (revérifiée par la garde de calcul, `GO_ID` en tête) ; la mère la joue telle quelle, dans un appel qui commence par les mêmes `cd`, activation et exports. `DR_ESSAIS=8` : un lot d'essais de chaîne, condition honnête seule, tâches de la banque initiale, hors mesure (débit, mémoire, écriture, garde d'équivalence) ; `0` pour s'en passer.

Code 3, aucune offre conforme : rejouer la même commande `creation` toutes les 15 minutes, douze recherches au plus, puis nœud de Lazar ; aucune carte plus chère.

## 3. Surveillance

```bash
cd <bloc-notes>/lancement-dr && . <bloc-notes>/venv-dr/bin/activate \
  && export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}" \
  && bash scripts/lancer_dose_reponse_v3.sh surveillance <identifiant> <même dossier>
```

Arrêt par l'identifiant (R10) sur processus mort ou dépense cumulée ≥ 90 USD ; alerte unique à 72 USD ; deux heures sans ligne de progression : alerte sans arrêt. L'instance porte la même garde (minuterie : à l'heure d'épuisement du plafond restant, consignation, poussée, destruction). Les lignes de progression ne portent que des comptes d'épisodes.

Tenue sur 24 heures : lancer la surveillance en arrière-plan, limite 7 200 000 ms. À chaque fin par délai, la relancer avec le même identifiant et le même dossier ; `progres.txt` et `compte-rendu-alerte.txt` persistent, donc l'alerte à 72 USD reste unique. Programmer un rappel de soi toutes les 2 heures au plus jusqu'à la fin. Si la session tombe, les gardes de l'instance tiennent : minuterie au plafond, arrêt sur un processus mort.

Lecture des sorties de la surveillance :
- **« ARRET mort … absente à deux relevés »** : la course peut avoir fini normalement (la fin normale de l'amorce écrit « destruction demandée (fin normale … versement prouvé …) », que la surveillance ne reconnaît pas comme une fin). Relever `git ls-remote origin refs/heads/calcul/dose-reponse-v1`, puis lire l'inventaire et le journal poussés (`traces/`) : « versement prouvé » vaut fin normale.
- **« ARRET depense »** : lire d'abord `journal-instance.txt`. Si la minuterie a écrit « DÉPENSE ÉPUISÉE », ne rien arrêter : attendre sa destruction, au plus 75 minutes, puis vérifier par `vastai show instances`. Sinon, arrêter par l'identifiant.
- **« FIN » ou « ARRET mort » du processus** : l'amorce a arrêté l'instance, disque gardé. Ne jamais la détruire avant que le versement soit prouvé, c'est-à-dire branche poussée et inventaire présent sur la branche. (Le message que la surveillance imprime après « FIN » invite à détruire « machine encore là » : cet ordre prime, versement prouvé d'abord.)

S'il manque quelque chose sur la branche : `timeout -k 5 120 vastai start instance <identifiant>`. Au second démarrage, l'amorce consigne, pousse puis détruit. Si le redémarrage n'est pas obtenu en 6 heures : nœud de Lazar (stockage à 0,08 USD de l'heure au plus).

Toute destruction se fait par `timeout -k 5 120 vastai destroy instance <identifiant>`, après le versement prouvé, et se consigne à `registres/arrets.md`. La dépense se consigne au registre des dépenses, relevée sur la facture du loueur.

Réserve : dépassement du plafond borné à environ 1,6 USD (à l'heure d'épuisement, la minuterie consigne jusqu'à 40 minutes puis détruit, marge jusqu'à 30 minutes), déclaré à Lazar s'il survient.

## 4. Reprise après une erreur de chaîne

Instance neuve, branche de sortie neuve, avec `DR_BRANCHE=calcul/dose-reponse-v1-reprise-1 DR_REPRISE_BRANCHE=<branche de la tentative> DR_REPRISE_RUN=<run de la tentative>` aux contrôles (dans le même appel que `controles`, avec les mêmes `cd`, activation et exports) ; dépense antérieure cumulée, relevée sur la facture du loueur. En reprise, `DR_ESSAIS=0` (seize essais de chaîne au plus sur toute la course). Un disque plus grand que 300 Go n'est pas demandable sans code neuf (configuration figée) : nœud. Les blocs poussés sont recopiés à l'octet dans le dossier de la nouvelle tentative, ceux d'un bloc commencé non poussé sont déclarés par épisode et rejoués avec leurs graines.

## 5. Après la course

Vérifier que les 64 blocs (1 920 épisodes) sont sur la branche de sortie, sceaux conformes, puis jouer la lecture **une seule fois**, sur processeur, dans un arbre de travail de la branche de sortie (code égal à 6b2b821a), jamais depuis main :

```bash
git fetch origin <branche de sortie de la dernière tentative>
git worktree add --detach <bloc-notes>/lecture-dr origin/<branche de sortie de la dernière tentative>
cd <bloc-notes>/lecture-dr && . <bloc-notes>/venv-dr/bin/activate \
  && PYTHONPATH=src python -m controle_ia.dose_reponse.lecture_v2 --run-id <AAAAMMJJ-HHMMSS>-dose-reponse-lecture \
     --dossier donnees/<run de la dernière tentative> --resultat-course diag/<run de la dernière tentative>/episodes-dose-reponse.json \
     --prereg prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md
```

En cas de reprise, un seul `--dossier` : celui de la **dernière** tentative. Écart à la contre-lecture (m8, « `--dossier` répété pour la course et chacune de ses reprises »), corrigé autrement : la reprise recopie à l'octet, dans le dossier de la nouvelle tentative, chaque bloc scellé des tentatives antérieures (`course_v2.reprendre`), si bien que ce dossier porte les 64 blocs ; répéter `--dossier` ferait lire deux fois les blocs repris, et `lecture_v2.charger_course` refuse un bloc en double (arrêt, aucune lecture). `--resultat-course` est celui de la dernière tentative (seule à écrire `episodes-dose-reponse.json` sur une course complète).

Le résultat `diag/<run lecture>/` (manifeste et `lecture-cout-dose-reponse.json`, scellés) est committé et poussé sur la branche de sortie de la dernière tentative, puis versé sur main par la mère ; aucune seconde lecture.

Puis verdict (R13) par un sous-agent neuf sur `diag/<run lecture>/lecture-cout-dose-reponse.json`, scellé, soumis à Lazar.

**Étapes du critère 3 (texte de désignation, plan, point 3), chacune scellée avant la suivante**, dans un arbre de travail de la branche de sortie (historique complet, `git fetch --unshallow` si besoin) :
- (a) ci-dessus : lecture du coût et verdict de la partie (i) du critère 2 ;
- (b) et (c) : lecteur du texte, une seule fois :

```bash
cd <bloc-notes>/lecture-dr && . <bloc-notes>/venv-dr/bin/activate \
  && bash scripts/lancer_lecteur_texte_dose_reponse_v2.sh --mode reel <run de la dernière tentative> <run lecture>
```

  Il écrit et scelle `issue-lecteur-du-texte-dose-reponse.json` (b), l'audit de symétrie (c), puis `doses-jugees-critere-3.json` (d) avec l'option A, la ligne K et sa phrase gelée. Code 2 : refus, rien d'écrit ; code 3 : arrêt, fichier d'arrêt seul. Une seconde exécution est refusée par la pièce.
- (d) vérification de `doses-jugees-critere-3.json` par un sous-agent neuf qui applique la table K du texte (R13) : il compare le fichier (d) aux fichiers (b) et (c) **écrits** (remarque VN-01 de la vérification du lecteur : la validation interne compare à des objets en mémoire) ; le fichier (d) porte deux clés de plus que le texte n'en nomme, `etats_temoins` et `audit_motifs`, qui servent à sa reconstruction champ à champ. Puis ligne `DOSES-JUGEES-CRITERE-3`, inscrite par la mère.
- (e) **seulement alors**, un score de sonde peut être calculé ou ouvert sur ce lancement, sous le texte de lecture des sondes. Avant la ligne `DOSES-JUGEES-CRITERE-3`, aucun score de sonde n'est calculé, écrit ni ouvert (sinon : lecture des sondes invalide pour le critère 3, nœud de Lazar).
