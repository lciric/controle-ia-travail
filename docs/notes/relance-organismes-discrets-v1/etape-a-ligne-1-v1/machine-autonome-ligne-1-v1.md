# Ligne 1 de carte du bras A : machine autonome, sans SSH, version 1

- **Date (UTC)** : 2026-11-23. Rédacteur : Claude Opus 5.5, agent délégué par la session du bras A. Écrite sur processeur seul : aucune dépense, aucune instance, aucune clé lue, aucun réseau hors git. Rien de cette note n'a tourné hors du processeur ; aucune commande de création n'a été jouée.
- **Objet** : la première création a échoué parce que le conteneur de la session n'a pas de liaison TCP brute (pas de SSH, seulement HTTPS sur 443). Décision du deuxième étage : **machine autonome**. La machine clone une branche d'entrée qui ne porte que la liste blanche, vérifie les empreintes posées, joue la ligne, verse sur une branche de sortie neuve, prouve la poussée, puis se détruit par son propre identifiant. La séquence v2 (`sequence-ligne-1-v2.md`) reste en vigueur pour tout ce qui ne touche pas au transport : sections 0 à 3, 4 (m1, m2), 6 (arguments de la course, échéance de 6 h), 7 (versement scellé avant toute destruction), 8 à 10. Ses sections 5 et 6 (pose par `scp`, surveillance par `ssh`) sont remplacées par ce qui suit.
- **Conventions fixées par la session mère** (elles remplacent mes propositions) : jeton du dépôt nommé `GH_TOKEN` sur l'instance ; adresse du dépôt **sans jeton**, identification par une aide (`credential.helper`) donnée au clone puis inscrite dans la configuration du clone avant toute extraction et toute poussée (leçon R-5101) ; destruction par l'interface HTTPS du loueur (`DELETE …/instances/$CONTAINER_ID/`), arrêt simple par `PUT {"state":"stopped"}`, sans `pip install vastai` sur l'instance ; branche d'entrée `entree/bras-a-ligne-1-v1`, branche de sortie `calcul/bras-a-ligne-1-v1` (deux noms neufs) ; la commande de création part de la session mère, et le programme de ce dépôt ne fait que l'imprimer.

## Pièces

| pièce | chemin | sha256 |
|---|---|---|
| construction de la branche d'entrée | `scripts/construire_branche_entree_ligne_1_bras_a_v1.py` | compagnon `.sha256` |
| amorce de la machine | `scripts/amorce_ligne_1_bras_a_v1.sh` | compagnon `.sha256` |
| lanceur de la session (`creation`, `etat`, `verification`) | `scripts/lanceur_machine_ligne_1_bras_a_v1.py` | compagnon `.sha256` |
| essais | `tests/test_amorce_ligne_1_bras_a_v1.py` | compagnon `.sha256` |
| liste blanche v2 (appelée, inchangée) | `scripts/liste_blanche_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| programme de la course v2 (joué, inchangé) | `scripts/course_ligne_1_bras_a_v2.py` | compagnon `.sha256` |
| constat de départ (posé sous le nom `constat-ligne-1.json`) | `docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/constat-ligne-1-20261123T024626Z.json` | compagnon `.sha256` |

## 1. Branche d'entrée (cloisonnement)

`PYTHONPATH=src .venv/bin/python scripts/construire_branche_entree_ligne_1_bras_a_v1.py [--pousser]`

- Elle appelle la liste blanche v2 (36 modules, 12 fichiers de données avec compagnons, les 4 fichiers du guide) et ajoute `requirements-gpu.txt`, `requirements-cpu.txt`, `requirements-donnees.txt`, le constat sous le nom `constat-ligne-1.json` et `empreintes-posees.txt` : **57 fichiers**, rien d'autre (contrôlé après le commit par `git ls-tree`, qui doit rendre exactement cette liste).
- Elle est construite dans un **dépôt git temporaire, hors de l'arbre de travail**, comme **branche orpheline** ; chaque fichier est pris **un par un** au commit source (`git show <commit>:<chemin>`) ; l'arbre de travail doit être propre sur ces chemins.
- **Les quatre fichiers du guide** (l'invite « H1-classification », l'index et leurs deux compagnons, sous `docs/sources/`) sont pris par `git show origin/main:<chemin>` **redirigé directement dans le fichier** : rien n'est affiché, rien n'est lu ni empreinté par le programme. Leurs empreintes sont **données** et écrites telles quelles dans `empreintes-posees.txt` : invite `69d50fb9…5540`, son compagnon `fb943fdb…b266`, index `adb4b8bc…ae2d9`, son compagnon `ba9648b1…316c`. Celles de l'invite et de l'index sont confrontées aux constantes de la liste blanche v2 ; un écart arrête.
- **Cloisonnement** : chaque chemin posé est confronté à `est_cloisonne_ici` de la liste blanche v2 (garde statique du bras A, plus les chemins cloisonnés de la session). Seuls les quatre chemins du guide y échappent, et seulement ceux-là.
- Le message du commit porte `Commit-source: <commit>`. L'amorce le lit et le passe à `--commit` de la course. Le compte rendu dit si ce commit est présent sur une branche distante.
- `--pousser` pousse **la seule branche d'entrée**, par une désignation explicite (refspec), jamais en force. Si elle existe déjà sur le dépôt distant à un autre commit, c'est un refus (R12 : nouvelle version, nouveau nom, par exemple `entree/bras-a-ligne-1-v2`).
- **Essai ici, sans poussée**, au commit `d7cd184f…` : 57 fichiers, commit d'entrée `533334b3…`. Ce commit changera : la session mère reconstruit la branche au commit qui porte les présentes pièces, puis la pousse.

## 2. Commande de création (imprimée, jamais exécutée par le dépôt)

`PYTHONPATH=src .venv/bin/python scripts/lanceur_machine_ligne_1_bras_a_v1.py creation --offre <offre> --commit-entree <commit d'entrée>`

Avant d'imprimer, le programme vérifie par `git ls-remote` que la branche d'entrée est sur le dépôt distant au commit donné et que la branche de sortie n'y est pas. Il imprime une seule ligne, à jouer **depuis la racine du dépôt** (le chemin de `--onstart` est relatif) :

```
GO_ID=GO-2026-11-22-148 vastai create instance <offre> --image pytorch/pytorch:2.14.1-cuda13.0-cudnn9-runtime --disk 150 --label bras-a-ligne-1-v1 --cancel-unavail --raw --env "-e GH_TOKEN=$GH_TOKEN -e HF_TOKEN=$HF_TOKEN -e GO_ID=GO-2026-11-22-148 -e BRANCHE_ENTREE=entree/bras-a-ligne-1-v1 -e BRANCHE_SORTIE=calcul/bras-a-ligne-1-v1 -e COMMIT_ENTREE=<commit d'entrée> -e AMORCE_SHA256=<empreinte de l'amorce> -e AVANT_CREATION_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)" --onstart scripts/amorce_ligne_1_bras_a_v1.sh
```

- Les secrets n'y paraissent que **par leur nom** (`$GH_TOKEN`, `$HF_TOKEN`). Le shell de la session les développe au moment de la commande. La clé du loueur n'est pas dans la commande : `vastai` la lit dans sa configuration.
- `AVANT_CREATION_UTC` est relevée par ce même shell **juste avant** l'appel. Elle est antérieure à la création, donc prudente : le compteur compte un peu plus, jamais moins.
- `--cancel-unavail` : si l'offre n'est plus disponible, la création échoue au lieu de créer une instance arrêtée.
- `--onstart` : `vastai` lit le fichier et en passe le texte comme script de démarrage. Le type de lancement est celui par défaut de la ligne de commande (`ssh`). Aucun SSH n'est utilisé, et aucune clé n'est ajoutée au compte.
- **Interdit** : `--explain` (il imprime la requête, variables développées comprises).
- Le piège de la garde de calcul tient toujours : cette ligne ne s'écrit jamais dans une note ou un registre par une commande Bash. On l'écrit avec l'outil d'écriture de fichiers.

## 3. L'amorce sur la machine (`scripts/amorce_ligne_1_bras_a_v1.sh`)

0. L'heure de départ est prise à la première ligne. Une variable de jouet hors du mode jouet est un refus immédiat. **Reprise** : si le fichier d'état `amorce-commencee` existe sur le disque (redémarrage du conteneur, qui rejoue le script de démarrage), **rien n'est relancé** (R12) : l'état est versé, la poussée tentée ou prouvée, puis destruction (ou arrêt). Ensuite : contrôle des arguments ; heure de création retenue ; **minuterie** lancée.
1. Clone de la seule branche d'entrée : `git -c credential.helper="$AIDE" clone -q --depth 1 --single-branch --no-checkout --branch entree/bras-a-ligne-1-v1 https://github.com/lciric/controle-ia-travail.git`, puis `git config credential.helper "$AIDE"` dans le clone, **puis** l'extraction. Le commit cloné doit être égal à `COMMIT_ENTREE`.
2. `sha256sum --strict -c empreintes-posees.txt`, et l'arbre ne doit porter **rien d'autre** que les fichiers listés. Sinon : versement d'un échec, scellé par la **bibliothèque standard seule** (le code reçu n'est pas exécuté), même format de manifeste que `sceller_le_versement`, puis poussée et destruction.
3. Constat : GO égal à GO-2026-11-22-148 ; création le **même jour UTC** que le constat (m1) ; une `AVANT_CREATION_UTC` antérieure au constat est un refus (hors séquence). L'échéance et l'heure du plafond sont refaites sur la création retenue. Ensuite : carte A100 et CUDA servie par le pilote au moins 13.0 (`nvidia-smi`) ; `requirements-gpu.txt` installé dans un environnement virtuel ; modèle de la configuration de référence mis au cache par `harnais.modeles.precharger_modele` (sans `GH_TOKEN` ni `CONTAINER_API_KEY` dans l'environnement de l'étape).
4. Course : `scripts/course_ligne_1_bras_a_v2.py` avec les arguments de la séquence v2, section 6 (configuration v2, lanceur v8 et son empreinte `2663d32d…`, `constat-ligne-1.json`, plan v2, `--creation-instance-utc` = création retenue, `--commit` = commit source, `--mode reel --hors-ligne`). Elle est lancée sans aucun des trois secrets dans son environnement, son PID est noté, et la minuterie l'arrête par ce PID (TERM, puis KILL) à l'échéance.
5. **Quel que soit le code** : versement sous `diag/organismes-discrets-v-a-v2/ligne-1-<fini|arret|echec|reprise>-<date>/`. Il contient les sorties de la course, `course.out`, le constat, `empreintes-posees.txt`, `amorce.json` (commits d'entrée et source, création retenue et sa source, marge, échéance, heure du plafond, code de la course, reprise, empreinte de l'amorce jouée et attendue) et le journal de l'amorce. Il est scellé par `lanceur_bras_a_v8.sceller_le_versement`. Si le manifeste de la ligne manque : manifeste minimal (`{"ligne": 1, "manifeste": "absent", "journal": <fin du journal de la course>}`) et manquant déclaré, comme la séquence v2, section 7.
6. Commit sur la branche de sortie **orpheline** `calcul/bras-a-ligne-1-v1`, qui ne porte que le versement ; poussée sans force, trois essais. **Preuve** : `git ls-remote origin refs/heads/calcul/bras-a-ligne-1-v1` doit rendre le commit local.
7. Poussée prouvée : **destruction** par l'identifiant (`DELETE https://console.vast.ai/api/v0/instances/$CONTAINER_ID/`, clé `CONTAINER_API_KEY`), redemandée chaque minute tant que la machine vit (après cinq demandes, un arrêt est demandé en plus). Poussée non prouvée : **arrêt seulement** (`PUT {"state": "stopped"}`), le disque est gardé. Au redémarrage par la session, l'amorce reprend sans rien relancer, repousse le même commit, puis se détruit.

**Minuterie** (processus à part, relit l'échéance et l'heure du plafond sur le disque à chaque pas) : à l'échéance (création + 6 h), elle arrête l'étape longue en cours (installation, téléchargement ou course) par son PID, puis le versement suit. À l'**heure du plafond** (création + (18 USD − frais fixes) ÷ taux du constat ; avec le constat du jour, (18 − 0,013 × 40) ÷ (1,12 + 0,072) ≈ 14,65 h), elle **détruit quel que soit l'état du versement** : c'est la borne de la dépense. Avant la lecture du constat, cette heure provisoire vaut création + 7 h. Un `CONTAINER_ID` non numérique est refusé : ni destruction ni arrêt ne partent, et le journal le dit.

**Heure de création et marge** : la création retenue est `AVANT_CREATION_UTC`, relevée juste avant la commande. La marge est la latence de l'appel au loueur (quelques secondes), comptée en trop. À défaut de cette variable : départ de l'amorce − 30 min (`MARGE_S` = 1 800 s, déclarée), jamais avant l'horloge du constat (la création suit le constat). **Recoupement après coup** : `etat` donne `start_date` ; `verification --start-date <start_date>` exige que la création retenue soit au plus `start_date` (le compteur compte au moins depuis lui) ; sinon code 3, à rapporter.

## 4. La valeur des secrets n'entre dans aucun journal

- `set +x` ; l'adresse du dépôt ne porte jamais de jeton ; l'aide d'identification lit `GH_TOKEN` par son nom, au moment où git l'appelle.
- La clé du conteneur passe à `curl` **par l'entrée standard** (`curl -K -`, en-tête écrit par `printf`, qui est une commande interne du shell) : elle n'est ni sur une ligne de commande, ni dans un journal.
- Le journal de l'amorce passe par une fonction de masquage, qui remplace les valeurs de `GH_TOKEN`, `HF_TOKEN` et `CONTAINER_API_KEY` par « [masqué] ». Les sorties de git, de pip, du téléchargement et de la course sont masquées de même avant d'être versées. La course et le téléchargement tournent sans les secrets dont ils n'ont pas besoin.
- Le lanceur masque toute réponse du loueur avant de l'écrire : valeurs de `VAST_API_KEY`, `HF_TOKEN`, `GH_TOKEN` et `CONTAINER_API_KEY` présentes dans l'environnement, champs `*api_key*`, `*token*`, `*secret*`, `*password*`, et paires `[nom, valeur]` de ce genre (la fiche de l'instance porte les variables passées par `--env`, dans `extra_env`). `etat` n'écrit qu'une liste de champs nommés.
- **Essai** : dans chaque scénario jouet, les valeurs factices des trois secrets (et de la clé du loueur côté lanceur) ne figurent ni dans la sortie de l'amorce, ni dans aucun fichier sous la racine de la machine jouet, ni dans la branche poussée, ni dans les sorties du lanceur.
- Reste visible chez le loueur, par construction : les valeurs passées par `--env` sont dans la fiche de l'instance (`extra_env`), lisible avec la clé du compte. Ce sont les mêmes valeurs que dans l'environnement de la session.

## 5. Essais (`tests/test_amorce_ligne_1_bras_a_v1.py`, sur processeur)

Le monde jouet : un dépôt source local rempli par la liste blanche v2, un texte **fictif**, une configuration d'essai qui nomme un **guide fictif** (constantes injectées dans le lanceur v8 par un petit programme posé sur la branche, comme dans les essais de la course v2), un plan et deux constats d'essai. Un dépôt nu local joue GitHub ; un faux `curl` joue le loueur (il consigne la méthode et l'adresse, jamais d'en-tête) ; un petit serveur local joue la lecture de l'instance.

- **Construction** : la branche jouet ne porte que la liste (et `sha256sum -c` passe) ; huit refus avant toute extraction (chemins cloisonnés `bases/`, `sondes/`, `scripts/mots_et_cout_*`, `registres/` en renommage, empreinte donnée illisible, branche illisible, commit tronqué, chemin `..`) ; poussée refusée à un autre commit (R12) ; **vraie branche** construite sans poussée : 57 fichiers, les quatre seuls chemins cloisonnés sont ceux du guide, à leurs empreintes données, et le constat à la sienne.
- **Amorce** : refus des variables de jouet hors jouet (joué par `bash` et par `sh`) ; **mode court** (la course refuse le guide faute d'injection : code 2, manifeste minimal, versement scellé par le lanceur v8, poussée prouvée, une seule demande DELETE, `verification` passe) ; **arrêt au plafond** (création à 12,97 h : la course s'arrête, manifeste de la ligne versé) ; **empreinte posée fausse** (échec, scellement par la bibliothèque standard, course jamais lancée, destruction) ; **commit d'entrée différent** (échec, destruction) ; **poussée non prouvée** (crochet du dépôt nu qui refuse `calcul/*` : arrêt par PUT, aucune DELETE), puis **redémarrage** (reprise, aucune relance, le même versement repoussé, destruction) et troisième départ (seulement la destruction) ; **échéance déjà passée** (course jamais lancée, versement « arret ») ; **échéance pendant la course** (TERM au PID de la course, versement, destruction) ; **heure du plafond** (destruction par la minuterie avant toute poussée) ; **création relevée avant le constat** (échec). Le rejeu entier sur le modèle jouet est derrière `AMORCE_LIGNE_1_ESSAI_LONG=1`, non joué ici (environ 50 min sur ce processeur, selon le rejeu de la course v2).
- **Lanceur** : la commande imprimée ne porte que les noms des secrets ; après développement par un shell, `vastai.utils.parse_env` y lit bien les valeurs factices et toutes les variables ; offre nulle refusée ; vérification de l'entrée sur le dépôt distant (bon commit : imprime ; mauvais : refus) ; `etat` contre le serveur local (en-tête `Bearer` reçu, `start_date` converti vers le bas, valeur secrète masquée dans `status_msg`, prix réel au-dessus du constat : consigne de destruction) ; masquage ; `verification` refuse une branche absente.
- **Non éprouvé ici, par construction** : l'aide d'identification sur HTTPS (le dépôt nu local se passe d'identification), `nvidia-smi`, l'installation, le téléchargement du modèle, les appels réels au loueur, et le comportement de `--onstart` chez Vast.

## 6. Étapes de la session mère

1. Contre-lecture neuve de ces pièces (R2) ; puis, si une session habilitée à ouvrir `docs/sources/` est disponible, confrontation des quatre fichiers du guide extraits à leurs empreintes données (séquence v2, section 5, point 3). La machine les revérifie de toute façon.
2. Construire et pousser la branche d'entrée au commit qui porte ces pièces (`--pousser`) ; noter `commit_entree`.
3. Même jour UTC que le constat (2026-11-23 ; sinon nouveau relevé, nouveau constat, nouvelle branche d'entrée `…-v2`) : `creation --offre … --commit-entree …`, puis jouer la ligne imprimée depuis la racine du dépôt, `GH_TOKEN` et `HF_TOKEN` dans l'environnement.
4. Aussitôt : `etat --instance <identifiant> --constat <constat>` (m2 : prix réel au-dessus du taux du constat → destruction par l'identifiant ; `start_date` relevé).
5. Surveillance par `etat` (statut) et `git ls-remote origin refs/heads/calcul/bras-a-ligne-1-v1`, sans SSH.
6. `verification --start-date <start_date>`, puis `etat` : l'instance doit être absente ou détruite. Sinon, destruction par l'identifiant depuis la session (R10). Si elle est arrêtée sans poussée prouvée : la redémarrer (l'amorce repousse puis se détruit) ou la détruire après décision. Consigner arrêts, dépenses et état.

## 7. Ce qui reste à confirmer par la session mère

1. **`--onstart` chez Vast** : la longueur admise pour le script de démarrage (l'amorce fait environ 28 Ko ; une limite plus basse ferait échouer la création), que les variables `-e` y sont bien visibles en lancement `ssh`, et que le script est rejoué au redémarrage (l'amorce tient les deux cas). À défaut, le lancement `--entrypoint bash --args -c "echo <amorce en base64> | base64 -d > /root/amorce.sh && bash /root/amorce.sh"`, déjà employé par les lanceurs de l'étape B bis, est l'alternative. Il demande d'ajouter un mode au lanceur.
2. **Droits du jeton** `GH_TOKEN` : lecture de la branche d'entrée et création de la branche de sortie sur `lciric/controle-ia-travail`.
3. **Noms de branches** : la branche de sortie est d'usage unique. Une seconde tentative demande un nom neuf (`calcul/bras-a-ligne-1-v2`, option `--branche-sortie` du lanceur), et de même pour l'entrée. La manière de ramener le versement de `calcul/…` vers la branche de travail (copie nommée du dossier puis commit) reste à décider.
4. **Destruction forcée à l'heure du plafond** (≈ 14,65 h après la création) même sans versement prouvé : c'est votre consigne. Elle borne la dépense au prix de la perte des sorties si l'arrêt demandé n'a pas pris.
5. Le point 4 de la section 9 de la séquence v2 (noyau d'attention « defaut » ou `sdpa`) reste ouvert. L'amorce ne le tranche pas.
