# Contre-lecture de l'amorce du rejeu des activations, voie (A), v1 (classe B)
Essais : 37 passent. Sondes faites dans une copie du bloc-notes (demo.py) : elles confirment B1, B3, M1, M4.
Fichiers lus : le module (1336 lignes), l'ordre gabarit, la garde des accords, les extraits du devis et de la notice, les essais en partie.

## Bloquants
B1. Minuterie fragile (l. 1033-1069) : aucune protection contre une exception. Un fichier de PID à moitié écrit (`int("")`) ou un journal qui ne peut plus écrire (disque plein, risque réel) tue le processus détaché : plus de coupure ni de destruction à 4,5 h côté machine. Démontré : ValueError, aucun geste de destruction. Correction : boucle entière sous `try/except Exception` (journal en `try`), destruction dans un `finally`, lecture du PID tolérante.
B2. Minuterie morte sans que personne le sache (l. 777-788, 1306-1309). Si `CONTAINER_API_KEY` est absente, `ClientVastRest("")` lève Refus, le processus meurt (sorties vers /dev/null) et la machine continue sans minuterie. Aucune vérification de vie après `Popen`. Correction : `armer_minuterie` attend `minuterie.txt` (2 à 5 s) et vérifie `poll() is None`, sinon REFUS DE DÉPART ; exiger `CONTAINER_API_KEY` non vide avant tout.
B3. `executer` sans filet (l. 941-1027) : toute exception inattendue (OSError d'écriture dans `tirer` ou `verser`, AttributeError dans `garde_activations` sur un morceau qui n'est pas un dictionnaire, démontré) sort sans `finir` : ni versement, ni arrêt ; un verrou déjà posé interdit la reprise. La machine brûle jusqu'à la minuterie, résultats perdus. Correction : `try/except Exception` autour du corps, appel de `finir("ERREUR INATTENDUE")`, et `verser` tolérant par étape.

## Majeurs
M1. Surveillance externe : absence prise pour réponse valide (l. 348, 471-475, 1157). `instances()` renvoie `[]` si la clé manque (réponse `{}` ou message d'erreur en 200) : `surveiller` conclut « absente : surveillance finie » (démontré, 6 h écoulées) ; `detruire` répond « déjà absente » sans geste. Correction : exiger la clé `instances` et une liste ; absence confirmée par deux relevés espacés.
M2. `surveiller`, relevé en échec (l. 1153-1156) : boucle sans seuil ni contrôle d'horloge ; si l'interface répond en erreur (clé, quota), aucune coupure ne part. Correction : l'horloge se juge sans le relevé ; au-delà de 4,5 h, tenter la destruction sans relevé ; après N échecs, sortie bruyante.
M3. Coupure qui échoue = fin de la surveillance (l. 1166 : Refus remonté, code 2). Étiquette inattendue, ou six relectures sans disparition : plus aucune tentative. Correction : nouvelles tentatives avec alarme, jamais de sortie tant que l'instance existe.
M4. Rapport de l'essai à blanc : garde faible (l. 648-662). Le nom d'une archive cité n'importe où, même sous « non écrit », suffit (démontré) ; un compagnon absent est ignoré en silence (l. 653). Correction : compagnon exigé ; lire le champ nommé par la notice (clé `tailles` dans le faux cas de l'essai), taille > 0.
M5. Destruction sans attestation pour `refus-depart` et `machine-arretee-en-echec` (l. 451, 465 ; CLI l. 1256) : un simple mot supprime la machine sans preuve de rapatriement, contre « rapatriement attesté, ou coupure nommée » et la règle de récupération. Correction : attestation exigée pour ces deux raisons ; seules `coupure-horloge` et `coupure-depense` s'en passent.
M6. Création incertaine sans fiche (l. 375-394, 1131-1136). Délai dépassé, réponse illisible ou écriture de la fiche en échec : une machine peut exister sans fiche, donc sans surveillance externe (la minuterie interne reste). Correction : écrire avant la création une fiche provisoire (heure de demande, étiquette, identifiant nul) et laisser `surveiller` retrouver l'instance par l'étiquette.
M7. Poussée sans contrôle de taille (l. 886-914). Un fichier de plus de 100 Mo (limite de GitHub) fait échouer son lot ; le code abandonne alors tous les lots suivants (`return None`) : perte de ce qui était récupérable. Correction : écarter et inventorier les fichiers de plus d'environ 95 Mo ; poursuivre les autres lots ; rapporter l'échec.

## Moyens
m1. Préparation avec tous les secrets (l. 963) : `{**os.environ, "HF_TOKEN"}` laisse GH_TOKEN et CONTAINER_API_KEY à `pip install` (code de paquets tiers). Correction : `env_sans_secret()` plus HF_TOKEN seulement.
m2. Redémarrage (l. 944-949) : la minuterie n'est pas réarmée avant `finir`, qui peut durer des heures (git 1800 s par appel). Réarmer d'abord.
m3. Si le clone du script de démarrage échoue (l. 1081-1088, sans `set -e`), la partie machine ne part pas, aucune minuterie : seule la surveillance de session protège (environ 6,3 USD en 4,5 h, sous 11). Correction : minuterie rudimentaire (attente puis destruction) en tout premier dans le script.
m4. Minuterie : la réponse à la destruction n'est ni examinée (`success`) ni relue (l. 1060-1064) ; aucun contrôle des instances intouchables côté machine. Correction : relire l'inventaire comme `detruire()` et ajouter le contrôle.
m5. La passe peut partir presque à l'heure de coupure (l. 1002-1009) : aucun temps restant minimal ; course entre `coupe()` et l'écriture du PID (la minuterie lit « passe non lancée », la passe tourne jusqu'à l'échéance). Correction : revérifier `coupe()` après `Popen` et tuer ; exiger un temps restant minimal.
m6. `rapatrier` : `--commit-attendu` facultatif (l. 1252) ; l'attestation ne porte pas l'état (`etat`) de l'inventaire ; `detruire` ne vérifie ni branche ni fraîcheur. Rendre le commit obligatoire et reporter l'état. Chemins `../` de l'inventaire non refusés (lecture hors dossier, hachage seulement).
m7. `lire_ordre` ne borne pas le temps cumulé des tirages et poussées (git 1800 s par appel, 5 essais) par le temps restant avant l'échéance.

## Mineurs
n1. L. 773 : le commentaire avale `"TRANSFORMERS_OFFLINE": "1"` (jamais posée). n2. Secrets sur la ligne de commande de la création (visibles par `ps` côté session) : accepté par la docstring ; jeton à portée minimale. n3. La garde des secrets de `verser` saute tout fichier par préfixe de nom (l. 862) : conforme à la règle. n4. La machine ne valide pas `DEPOT_URL` (l. 1325) : refuser `lciric/controle-ia.git`. n5. Les lectures de `.morceaux.json` (préfixe « scores-… ») sont permises par la notice v6 : conforme.

## (f) Cas non éprouvés (R5)
Minuterie qui plante ou ne démarre pas ; relevé de Vast vide ou en erreur persistante ; échec de coupure ; exception hors Refus dans `executer` ; rapport d'essai qui nomme l'archive sans l'avoir écrite ; fichier trop gros ; création incertaine ; raisons `refus-depart` sans attestation.

## Points tenus
Intouchables et fiche vérifiées avant tout geste, étiquette exacte, relecture double ; accord par le crochet exact (11,00) ; horloge et dépense en valeur la plus haute ; passe sans secret (essai de l'environnement) ; branche neuve ; relecture distante de la tête ; inventaire scellé et aucun fichier de trop au rapatriement.

VERDICT : À CORRIGER (trois bloquants B1 à B3 ; majeurs M1 à M7 avant tout GO de lancement).
