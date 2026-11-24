# Contre-lecture de la consigne d'enveloppe v2 et de son code (classe B)

Verdict : **utilisable après corrections** (1 bloquante, 0 majeure, 4 mineures, 2 suggestions).

Fichiers lus : docs/procedures/banque-dose-reponse-consigne-v2/consigne-extracteur-v2.txt ; docs/procedures/T0.5-extraction-v1/consigne-extracteur-v1.txt, consigne-contre-verificateur-v1.txt, verifier-sortie-v1.py, invite-cibles-v1.txt ; invite H9 (par charger_invite) ; src/controle_ia/environnements/extraire_banque_dose_reponse_v1.py et _v2.py ; reextraction_echantillon_96_v1.py et _v2.py ; rejeu_contre_verification_banque_v1.py. Aucun fichier interdit ouvert, aucun module lancé en mode réel (seul un import de contrôle, sans exécution).

## Ce qui est vérifié et tient

- Le diff v1/v2 de la consigne est une seule insertion (étape 2b, lignes 14 à 21) ; rien d'autre ne change (étape 5 et suivantes identiques).
- La liste des six interdits (lignes 15 à 20 de la consigne v2) est identique, mot pour mot et dans l'ordre, à la liste de l'invite H9 (comparaison par programme : égalité exacte).
- extraire_banque_dose_reponse_v2 : le diff avec la v1 se réduit à l'en-tête, aux noms de module (ligne « modules » épinglée, aide en ligne, commande du manifeste), à la constante CONSIGNE_EXTRACTEUR_V2, à son empreinte dans `fichiers_scelles` et à la lecture de la consigne à la préparation (ligne 524). `fichiers_scelles` est appelé de la même façon à la préparation (ligne 486) et à chaque lecture suivante ; aucune incohérence d'épinglage dans ce module. La consigne v1 reste épinglée sans être employée : inoffensif.
- La fonction `lire` recopiée dans reextraction_echantillon_96_v2.py (lignes 172 à 229) est identique à l'originale de rejeu_contre_verification_banque_v1.py (lignes 91 à 146) à deux lignes blanches près (diff par programme). Elle juge donc exactement comme l'original ; son seul écart utile est de comparer les empreintes avec `eb` de la v2, ce qui est voulu et cohérent avec `_scelles` et `_ouvrir`.
- Les deux modules s'importent sans erreur.

## Remarques

### CV2-1 — bloquante — la réextraction de l'échantillon d'octobre emploie toujours la consigne v1
Fichier : src/controle_ia/environnements/reextraction_echantillon_96_v2.py, lignes 88 à 89 :
`modele = (racine / eb.Chemins().dossier_procedure / eb.FICHIERS_PROCEDURE["consigne_extracteur"]).read_text(...)`.
Dans la v2 de `extraire_banque_dose_reponse`, `FICHIERS_PROCEDURE["consigne_extracteur"]` désigne encore `consigne-extracteur-v1.txt` (ligne 115 ; seule la préparation de l'extraction de la banque a été changée, ligne 524). Le diff v1/v2 de la réextraction ne touche pas ces lignes. Conséquence : le diagnostic « consigne v2 sur les 16 papiers d'octobre » donnerait aux extracteurs la consigne v1, avec un manifeste qui épingle pourtant la consigne v2 (`fichiers_scelles` contient `consigne_extracteur_v2`) et un en-tête qui affirme le contraire (« prend la consigne v2 »). Le résultat serait un second tirage de la v1, étiqueté v2 : défaut grave et silencieux, aucune garde ne le voit.
Correction : remplacer ces deux lignes par `modele = (racine / eb.CONSIGNE_EXTRACTEUR_V2).read_text(encoding="utf-8")`. Ajouter une garde ou un test : après `preparer`, le fichier `consigne.txt` de chaque dossier contient « 2b. Before going on » (et un test de mutation : avec la consigne v1, le test échoue). Aucun test n'existe pour les modules v2 (tests/ ne couvre que la v1) : au moins un test sur la préparation des deux modules, avec dépôt factice, est à ajouter.

### CV2-2 — mineure — en-têtes à auto-référence fausse
extraire_banque_dose_reponse_v2.py ligne 1 : « copie de `extraire_banque_dose_reponse_v2.py` » ; reextraction_echantillon_96_v2.py ligne 2 : « Copie de `reextraction_echantillon_96_v2.py` » (et ligne 2-3 « prend la consigne v2 », faux tant que CV2-1 n'est pas corrigé). Correction : écrire `..._v1.py` ; relire l'en-tête de la réextraction après CV2-1.

### CV2-3 — mineure — le texte de l'étape 2b déborde la demande par une formule plus étroite que la liste
consigne-extracteur-v2.txt, ligne 21. La question posée phrase par phrase ne couvre que trois des six interdits (méthode, dispositif, résultats) ; les trois autres (références aux figures, contributions nommées, noms d'auteurs) ne sont couverts que par la phrase suivante (« reveals an item of the list »). Pas de critère nouveau, mais l'écart de formulation peut faire oublier les contributions nommées. Correction proposée : terminer la question par « or contains a figure or table reference, a named contribution or contribution list, or an author name ». Sans changement de sens, le texte reste fidèle à H9.

### CV2-4 — mineure — contradiction de portée avec la dernière phrase de la consigne
Ligne 33 (v1 inchangée) : « Apart from the file names and the check in step 5, follow the prompts as written. » L'étape 2b introduit une seconde vérification qui modifie la réponse à H9. Correction : « Apart from the file names and the checks in steps 2b and 5 ».

### CV2-5 — mineure — « avant l'écriture » et « Save h9.json again »
La demande de Lazar dit « relecture avant l'écriture ». L'étape 2b relit après une première écriture de h9.json puis réécrit si changement. L'état final est le même, et c'est un bon choix (le fichier existe déjà, la vérification porte sur lui), mais c'est un écart de lettre à consigner. Précision utile : « when saving again, change only the "research_questions" field ; leave "affiliations" and "costs" unchanged » : sans cela, rien n'empêche une réécriture complète d'altérer les deux autres champs.

### CV2-6 — suggestion — risque d'énoncé trop appauvri et d'exclusions
Le contrôle mécanique (verifier-sortie-v1.py, ligne 126) rend invalide un énoncé de moins de 200 caractères ; « never add content » interdit de compenser, et l'étape 5 dit de laisser une erreur qu'on ne peut corriger sans inventer. Un extracteur zélé peut donc produire un énoncé court, donc un papier invalide, donc des reprises (tentatives 2 et 3) et, au-delà du seuil de 16 exclusions aux tentatives 1 et 2, un arrêt. Rien d'illégitime ici, mais à rapporter dans l'essai sur les 16 papiers : compter énoncés courts et longueur médiane avant et après. Un énoncé qui retire des phrases décrivant des jeux de données « du cadre antérieur » est aussi un risque d'ambiguïté (la phrase d'étape 2b exclut la méthode du papier, mais « datasets » dans le contexte antérieur est permis par H9 : la phrase de l'étape 2b le dit bien avec « this paper's own », ce qui suffit).

### CV2-7 — suggestion — pièces d'accompagnement
(a) Aucune empreinte compagnon `.sha256` pour consigne-extracteur-v2.txt : `verifier` la refuse tant qu'elle n'existe pas (R6) ; à sceller après correction, donc avant tout lancement. (b) Pas de test pour les deux modules v2 (voir CV2-1) ; la lecture recopiée mériterait un test d'équivalence avec `rejeu_contre_verification_banque_v1.lire` sur un dossier factice. (c) La garde « module du diagnostic changé » (`_ouvrir`) épingle bien le fichier v2 de la réextraction, mais pas `rejeu_contre_verification_banque_v1.py`, dont `_resultat_96`, `CORPUS_96` et `RUN_96` sont encore importés : comme avant, inchangé, mais le module restant importe aussi la v1 de `extraire_banque_dose_reponse` (deux versions chargées côte à côte, sans conflit).

## Jugement sur (a)

La consigne v2 n'ajoute que le rappel et la relecture. La liste est fidèle. Le seul critère nouveau est la question phrase par phrase, qui reformule « ne révèle pas » en « ne dit rien sur la méthode propre, le dispositif ou les résultats du papier » ; c'est une paraphrase, ni plus lâche ni plus stricte, avec la nuance de CV2-3. Les cibles, les citations et l'étape 4 ne sont pas touchées (l'énoncé est fixé à l'étape 2b avant l'étape 4, ce qui est même plus cohérent que dans la v1 ; la garde de fuite par n-grammes de l'étape 5 reste le seul cas d'édition tardive). Pas de contradiction avec « never add content » : « rephrase » est déjà permis par la v1 (étape 5).

## Jugement sur (b) et (c)

Le code de l'extraction de la banque est cohérent. Le code de la réextraction a le défaut CV2-1, qui rend l'essai sans objet tant qu'il n'est pas corrigé. Repli silencieux : CV2-1 en est un (la consigne employée n'est pas celle que le manifeste annonce). Aucun autre repli relevé.
