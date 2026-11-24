# Ordre de lancement proposé — course de dose–réponse de l'organisme à consigne cachée — v4

[v4 : corrections N1 à N4 de la vérification de la v3 (même contre-lecteur, relayées mot pour mot par la mère le 24 novembre 2026 vers 15:25 UTC), rien d'autre. La v3 reste telle quelle (R12).]

[v3 : corrections de la contre-lecture neuve de la v2 (Opus 5.5, `docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-ordre-lancement-dose-reponse-v2-opus-v1.md`, sur main, R-5307) : B1 (deux branches, au mot de Lazar), B2, M1 à M4 et m1 à m9, mot pour mot ou mieux ; m8 corrigé autrement (voir section 5). Commit du code inchangé : `a02b6540070aa5731875d07fbbe124f2dbe27f3b`. Les v1 et v2 restent telles quelles (R12).]

Pièce de classe A (ordre d'une course payante), proposée par le développeur, contre-lue (R2), scellée par la mère, jouée par la mère seulement. Texte qui fait foi : `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (`2263c5c447d17e0d2b045ba1a6421c681809df2ec8bafbcc3226aa6dd3f31c41`). Ligne de GO : `GO-2026-11-24-25` (calcul, 90 USD, échéance au registre le 15 décembre 2026). Bornes : une A100 SXM4 80 Go, au plus 1,30 USD de l'heure, 16 cœurs, 128 000 Mo de mémoire vive, disque d'au moins 300 Go, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go. Dépôt : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` (jamais `lciric/controle-ia`). Plafond : 90 USD cumulés sur toutes les tentatives ; alerte unique à 72 USD.

## 0. Préalables (aucune création sans eux)

1. Ligne `CODE-DOSE-REPONSE-CONSIGNE-CACHEE` : déjà inscrite sur main (R-5306), pièce `registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-a02b6540070aa5731875d07fbbe124f2dbe27f3b-v1.json` (`1521cbc9ba259b289883cfa0985f063eed7c2657397347326b1e7a578b2c0b63`).

1 bis. Avant l'étape 1, la mère inscrit sur main une pièce neuve, `registres/code-dose-reponse-consigne-cachee/DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v1.json`, scellée. Elle porte :
- l'identifiant de la session de lancement (la mère elle-même si elle lance) ;
- la phrase « aucune action générée sous un texte de la pièce jointe (7a5f633c…) ni du fichier du premier test (a68468fe…) » ;
- le renvoi à la ligne CODE.

La mère inscrit aussi sa ligne `DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE` au registre des scellements, avant que l'étape 1 copie ce registre sur la branche de lancement. Sans cette ligne : aucune création. (Le code ne contrôle pas cette ligne : la session de lancement la vérifie à la main, `grep DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE registres/scellements-v1.md` sur la branche de lancement, avant `controles`.)

2. Banque de 64 tâches : inscrite (R-5306), ligne `BANQUE-DOSE-REPONSE-CONSIGNE-CACHEE`, fichier `donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json` sur la branche `banque/dose-reponse-consigne-cachee-v1`, empreinte attendue `0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4`.

3. Texte de désignation de la course pour le critère 3 : au jour de cet ordre, il n'est pas scellé (candidat 4, option A ou B non tranchée). **Aucune création sans l'un des deux mots de Lazar, consigné au registre des décisions :**
   - **(a) « lancer sans désignation »** : `designation_critere_3` vaut `null`, et la course ne rejugera jamais le critère 3 (texte scellé, liste d'arrêt). Cet ordre se joue tel quel (sections 1 à 5), sans `--designation`.
   - **(b) « attendre la désignation »** : la création attend le scellement du texte et l'inscription de ses trois lignes (`DESIGNATION-CRITERE-3`, `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, `SONDES-LUES-CRITERE-3`). Il faut aussi une version 3 de l'amorce, qui ajoute `designation_critere_3.chemin` aux fichiers extraits sur l'instance (classe B : contre-lecture, commit neuf, ligne CODE neuve), puis un ordre v4. **Le code a02b6540 ne peut pas jouer une course désignée** : son amorce n'extrait sur l'instance que les fichiers cités `piece_jointe`, `consignes_premier_test` et `banque`, alors que `controles_v2.controler_registre` y vérifie le texte de désignation par son empreinte (arrêt après l'installation). Ce qu'il faudra, sans l'écrire ici :
     - l'amorce v3 : ajouter `designation_critere_3` à la liste des clés dont le chemin est extrait (si la clé n'est pas `null`), comme pour `piece_jointe`, `consignes_premier_test` et `banque` ;
     - un essai neuf qui joue les contrôles sur une configuration désignée, désignation extraite (cas sain) et absente (artefact) ;
     - le commit neuf du code, sa ligne CODE neuve (le chemin de la pièce porte le nouveau commit), puis l'ordre v4, qui appelle `scripts/ecrire_configuration_dose_reponse_v2.py … --designation <fichier JSON {chemin, sha256, lignes_registre}>` et cite les trois lignes.

   La branche jouée est celle du mot de Lazar, transmis par la mère.

4. Nœud tranché : les deux contrôles croisés sont reportés à une course suivante (décision de Lazar, R-5280) ; quinze conditions.

5. Session de lancement : `python3 -m venv <bloc-notes>/venv-dr && . <bloc-notes>/venv-dr/bin/activate && pip install -r requirements-cpu.txt -r requirements-pilotage.txt`, environnement créé une fois, ici, et activé ensuite par `. <bloc-notes>/venv-dr/bin/activate` (`torch` est exigé : `controles_v2` importe `environnements.pilote_a`, qui importe `torch` ; `vastai==1.8.3` lit `VAST_API_KEY` par son nom). Activer l'environnement en tête de chaque appel du terminal. `HF_TOKEN` lu par son nom, avec accès au modèle Llama-3.1-8B-Instruct (`controles` charge le tokeniseur seul pour le rapport des longueurs en jetons, avant toute création ; rien n'est affiché que des comptes). `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` est écrit en dur dans la commande de création ; le dépôt `origin` de la session doit être `lciric/controle-ia-travail`.

6. Calendrier : fin effective de l'accord : celle du registre, 16 décembre 00:00 UTC (le code lit le lendemain 00:00 UTC de l'échéance du registre). Pour tenir aussi la lettre du devis, aucune création après le 12 décembre à 07:00 UTC (le lanceur refuse déjà tout jour après le 12 décembre).

7. Appels du terminal sans état : `GO_ID=GO-2026-11-24-25`, l'activation de l'environnement et l'export du jeton GitHub (section 2) se répètent en tête de chaque appel.

## 1. Branche de lancement (session de la mère)

**À partir du commit du code `C = a02b6540070aa5731875d07fbbe124f2dbe27f3b`, jamais de `main`** : le lanceur et l'amorce exigent que `src/`, `scripts/`, `tests/`, `.claude/`, `pyproject.toml` et `requirements-*.txt` du commit de lancement égalent ceux de `C`. Sur la branche de lancement ne s'ajoutent que des données et des registres. L'arbre principal de la mère n'est pas basculé : la branche vit dans un arbre de travail du bloc-notes, et **toutes les commandes des sections 1 à 4 se jouent depuis `<bloc-notes>/lancement-dr`** (`cd` en tête de chaque appel) ; jamais le lanceur de main.

```bash
set -euo pipefail
git worktree add <bloc-notes>/lancement-dr -b lancement/dose-reponse-v1 a02b6540070aa5731875d07fbbe124f2dbe27f3b
cd <bloc-notes>/lancement-dr && . <bloc-notes>/venv-dr/bin/activate
git fetch origin main banque/dose-reponse-consigne-cachee-v1
git checkout origin/main -- registres/go.md registres/scellements-v1.md
git checkout origin/banque/dose-reponse-consigne-cachee-v1 -- donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256
grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md || { echo "préalable 1 bis absent : aucune création"; exit 1; }   # arrêt : ne rien jouer de plus
PYTHONPATH=src python scripts/ecrire_configuration_dose_reponse_v2.py donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json a02b6540070aa5731875d07fbbe124f2dbe27f3b
git add -f donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256 prereg/T0.6-dose-reponse-configuration-course-v1.json prereg/T0.6-dose-reponse-configuration-course-v1.json.sha256 registres/go.md registres/scellements-v1.md
git commit -m "Lancement de la course de dose-réponse : configuration, banque, registres"
git push -u origin lancement/dose-reponse-v1
```

Empreinte attendue de la banque : `0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4` (ligne BANQUE ; le script de configuration la lit sur le compagnon et les contrôles la comparent à la ligne). `--designation …` seulement sous l'option (b) du préalable 3, et alors par l'ordre v4. Le texte scellé, la pièce jointe et le fichier du premier test sont déjà au commit `C`. La configuration doit égaler, clé pour clé, celle que reconstruit le code.

## 2. Contrôles, puis création imprimée

Jeton GitHub de l'instance : `_3`, repli `_2`. Dans **chaque** appel du terminal qui joue `creation`, la commande de création imprimée ou `surveillance`, précéder la commande de `export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}"`. Le lanceur la choisit alors, et la masque. Les appels du terminal ne gardent pas leurs variables : l'export se répète à chaque appel. Si l'amorce refuse avec « clonage impossible » ou « poussée initiale de la branche … refusée », l'instance se détruit seule en 3 minutes environ. Rejouer alors `creation` sans cet export (repli sur `_2`) ; c'est un essai de création de plus, trois au plus, et sa dépense entre dans la dépense antérieure. Attendre que `timeout -k 5 120 vastai show instances` ne la liste plus (au plus 40 minutes, sinon destruction par l'identifiant après relevé de la branche), avant de rejouer `creation`.

```bash
cd <bloc-notes>/lancement-dr && grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md && . <bloc-notes>/venv-dr/bin/activate && export GO_ID=GO-2026-11-24-25 \
  && export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}" \
  && DR_BRANCHE_LANCEMENT=lancement/dose-reponse-v1 DR_AMORCE_SHA256=85898915c131b4fd10f0d49cd3bae37942c53b1c4341bbd454ef5d3910cb6ebe \
     DR_ESSAIS=8 bash scripts/lancer_dose_reponse_v2.sh controles <dossier neuf du bloc-notes>
cd <bloc-notes>/lancement-dr && grep -q '^| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE ' registres/scellements-v1.md && . <bloc-notes>/venv-dr/bin/activate && export GO_ID=GO-2026-11-24-25 \
  && export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}" \
  && bash scripts/lancer_dose_reponse_v2.sh creation auto course <dépense antérieure relevée sur la facture du loueur, 0 à la première tentative> <même dossier>
```

`creation` imprime la commande littérale de création (revérifiée par la garde de calcul, `GO_ID` en tête) ; la mère la joue telle quelle, dans un appel qui commence par les mêmes `cd`, activation et exports. `DR_ESSAIS=8` : un lot d'essais de chaîne, condition honnête seule, tâches de la banque initiale, hors mesure (débit, mémoire, écriture, garde d'équivalence) ; `0` pour s'en passer.

Code 3, aucune offre conforme : rejouer la même commande `creation` toutes les 15 minutes, douze recherches au plus, puis nœud de Lazar ; aucune carte plus chère.

## 3. Surveillance

```bash
cd <bloc-notes>/lancement-dr && . <bloc-notes>/venv-dr/bin/activate \
  && export CONTROLE_IA_GITHUB_TOKEN="${CONTROLE_IA_GITHUB_TOKEN_3:?}" \
  && bash scripts/lancer_dose_reponse_v2.sh surveillance <identifiant> <même dossier>
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

Vérifier que les 64 blocs (1 920 épisodes) sont sur la branche de sortie, sceaux conformes, puis jouer la lecture **une seule fois**, sur processeur, dans un arbre de travail de la branche de sortie (code égal à a02b6540), jamais depuis main :

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
