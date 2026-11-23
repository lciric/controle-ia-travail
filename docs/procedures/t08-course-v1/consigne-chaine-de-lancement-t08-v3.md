# Consigne — écrire la chaîne de lancement de la course de la base boîte noire (T0.8) — v3

- **Version 3** : remplace la version 2 (`a0da4962bedaa17b4dfc2bb27910ae4f36c982fb67e1b38341be304b6b8a20be`, gardée). Ce qui change : § 3.5 (commit local de la course : conditions, en réponse à la question du développeur du 22 novembre) ; § 4 (un essai ajouté) ; § 2 et § 5 (renvois : ordre de course au brouillon 3, commandes pour le brouillon des commandes, nom de la branche de rendu). Fait à connaître : la garde de l'instance a été resserrée au `resume.json` de 7b dans le code aligné (commit `01fe0ea57`, décision de la session mère), ce qui est la lettre du texte ; le commit du code à prendre est celui que citera `CODE-T08`, donné par la session mère. Rien d'autre.
- **Version 2** : remplaçait la version 1 (`722ceb5e475c1cf06137f5482175f041b1a25b6c8f43636acdd873c2e8f44a67`, gardée) après la contre-lecture 1 des pièces de la course (`prereg/contre-lectures/T0.8-pieces-de-course-v1-brouillon1-cl1.md`, `3ea629e8b1818f885a655776a0ce025dcad9f8ce2f93fa5123690ec40961e2c6`). Ce qui change : § 3.3 (échantillon de l'audit extrait par programme, constat L-2 ; sortie sans nombre de résultat, m-L1), § 3.4 et § 3.5 (plafond restant, O-2 ; accord prolongé, O-3), § 4 (cinq essais ajoutés : O-2, O-3, m-O2, L-2, m-L1), et les renvois à l'ordre de course, passé au brouillon 2. Rien d'autre.
- **Nature** : mandat (classe C). Le code qu'il commande est de classe B : contre-lecture par un autre modèle, puis vérification des corrections par le même contre-lecteur.
- **Écrite** le 2026-11-22 par le rédacteur du texte de T0.8 (modèle B). **Pour** : un développeur neuf du modèle A, lancé par la session mère ; ce peut être celui de l'alignement du code, après son rendu.
- **Pourquoi** : le code de la course et de la lecture existe (`src/controle_ia/t08/`), mais rien ne le lance sur une machine louée. Son développeur l'a écrit le 14 novembre : « aucun script de lancement n'est écrit » ; la lecture réelle n'a pas d'entrée en ligne de commande ; les configurations réelles sont à écrire (rapport `docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md`, § 6, sur la branche du code). Sans cette chaîne, aucune création n'est possible.

## 1. La règle de conception : copier, ne pas réécrire

La course de confirmation a une chaîne éprouvée : `scripts/lancer_t06_v13.sh` et `scripts/amorce_instance_t06_v11.sh`, mûris sur treize et onze versions, chacune née d'un défaut vu en réel (minuterie, verrou des consignations, clonage réduit, masquage des clés, inventaire vide, offre retirée). **Tu pars de ces deux fichiers, copiés sous des noms neufs, et tu n'y changes que ce que cette consigne nomme.** Chaque ligne changée est déclarée dans ton rapport, avec sa raison. Une réécriture, même plus propre, n'est pas ce qui est demandé : elle perdrait ces corrections.

## 2. Ce que tu lis, et ce que tu n'ouvres jamais

**À lire** : le texte de T0.8, `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon14.md` (branche `prep/t08-texte-complet-fable-v1`) — « Plan d'analyse » (points 1 à 5 et 10), « Liste d'arrêt », « Machine, devis et dépense », « Ordre des lectures et embargo » ; l'ordre de course, `docs/procedures/t08-course-v1/ordre-course-t08-v1-brouillon3.md` ; le code de T0.8 au commit aligné (branche de l'alignement), dont `course_v1.py`, `lecture_v1.py`, `entrees_v1.py`, `configuration_v1.py`, `essai_jouet_v1.py` ; les deux scripts de la course de confirmation nommés au § 1, le module de session qu'ils appellent et leurs listes d'essais ; `.claude/hooks/garde_calcul.py` ; l'en-tête de `registres/go.md` et les lignes `GO-2026-11-10-12`, `GO-2026-11-22-79`, `GO-2026-11-22-93`.

**Jamais** : aucun fichier de `diag/`, `runs/` ou `donnees/` d'une course réelle ; aucune branche `calcul/…` ni `verdict/…`, sauf, pour le programme de la branche d'entrée, les **noms** et les **compagnons `.sha256`** des cinq fichiers de la liste blanche ; aucun fichier de `docs/verdicts/` ; aucune pièce du saboteur à budget, du bras A ni du bras d'attaque ; aucune recherche récursive large. Données factices seulement. **Tu ne crées aucune machine, tu n'appelles pas le loueur** : tes programmes vérifient et impriment ; la création est à l'exécutante, sous l'ordre de course. Un refus d'outil n'est ni rejoué ni contourné.

## 3. Les cinq pièces à rendre

### 3.1 Branche d'entrée — `scripts/construire_branche_entree_t08_v1.py`

Règle du texte (« Liste d'arrêt », troisième puce) : le fichier de sondes n'est jamais copié sur la machine, ni comme fichier ni comme objet git ; la machine ne clone que la branche d'entrée et le code cité.

- Extrait par `git show <commit>:<chemin>`, sans les ouvrir autrement, les fichiers de la liste blanche du point 1 du plan **que la course lit**, et rien de plus : de la branche de sortie de 7b, ceux des cinq fichiers `mesures-t06.npz`, `textes-actions-t06.jsonl`, `episodes-t06.json`, `manifeste.json`, `lecture-cout-t06.json` que `course_v1.py` et `entrees_v1.py` demandent, avec leurs compagnons ; de `main`, le fichier des tâches d'évaluation, les consignes de P3, le guide de classification, l'invite dérivée ; le texte scellé de T0.8 et la configuration réelle de la course, que la commande reçoit. Tu relèves dans le code la liste exacte des entrées de la course et tu la déclares ; un fichier que le point 1 du plan ne nomme pas n'entre pas.
- Vérifie chaque empreinte contre celle que porte le texte scellé de T0.8 (les cinq de 7b) ou contre le compagnon (les autres) ; un écart arrête tout.
- Écrit une branche **neuve, orpheline**, qui ne contient que ces fichiers à leurs chemins, copiés à l'octet ; refuse d'écrire sur une branche qui existe.
- Contrôle final par programme : la liste des fichiers de la branche est exactement la liste blanche ; aucun nom ne commence par `lecture-sondes-t06` ; aucun `resume.json`, `distillation-t06.json`, activation ni adaptateur ; l'histoire de la branche ne contient aucun objet d'une autre branche.
- `base-a-t08.json` n'y va pas : il ne sert qu'à la lecture, sur processeur, hors de la machine.
- Essais (R5) : cas sain ; artefacts — une empreinte fausse, un fichier interdit glissé dans la liste, une branche déjà là.

### 3.2 Configuration réelle de la course — `prereg/T0.8-configuration-course-v1.json`, scellée

Sur le modèle de `essai_jouet_v1.configs` : chemins et empreintes des entrées, valeurs gelées, spécification de l'agent et des deux juges, les sept marqueurs de configuration. Les valeurs viennent du texte scellé, jamais d'ailleurs ; le code refuse déjà tout écart (`exiger_valeurs_gelees`, `exiger_marqueurs`, `exiger_marqueurs_au_texte`). Elle ne peut être finie qu'après le scellement du texte (commit du code, entropie) : tu rends un programme qui l'écrit à partir du texte scellé, et son essai sur un texte factice.

### 3.3 Lecture en ligne de commande — entrée et configuration réelle

Une entrée `python -m controle_ia.t08.lire_v1 --config … --run-id … --prereg …` qui ne fait qu'appeler `lecture_v1.executer_lecture`, et le programme qui écrit sa configuration réelle (liste blanche de la lecture, `base-a-t08.json` et `lecture-cout-t06.json` compris, à leurs empreintes inscrites). Aucune règle de lecture n'y est écrite : elles sont dans `lecture_v1.py`, contre-lu. Une entrée de même forme pour le passage à blanc (`lecture_v1.passage_a_blanc_reel`) sur le registre réel.

**Échantillon de l'audit R4 (constat L-2).** Quand l'audit se déclenche, `lecture_v1.py` désigne l'échantillon dans le résultat (clés des actions tirées, coût lu, scores des juges) mais n'en extrait ni le texte des actions ni les sorties des juges. Or le lecteur doit relire, pour chaque action tirée, le coût contre le texte de l'action et la sortie du juge contre son score, sans ouvrir les fichiers d'entrée entiers. L'entrée en ligne de commande écrit donc, après le résultat et sans le changer, un fichier d'échantillon scellé (`echantillon-audit-r4-t08.json`) : pour les seules clés que le résultat désigne, le texte de l'action, le coût lu, la sortie de chaque juge et son score, recopiés des entrées à l'octet. Le tirage reste celui de `lecture_v1.py` ; aucune règle de lecture n'est touchée ; audit non déclenché : aucun fichier.

**Sortie sans nombre de résultat (constat m-L1).** L'entrée n'imprime, sur la sortie standard et la sortie d'erreur, que des noms d'étape et d'état : les lignes `PROGRES` de `lecture_v1.py`, qui ne portent que cela, les chemins et les empreintes des fichiers écrits, et les messages d'arrêt. Aucun nombre tiré des résultats, aucune étiquette de dose, aucune phrase d'une table n'y passe. Tu relèves si un message d'arrêt de `lecture_v1.py` porte un nombre tiré des résultats, et tu le déclares sans le changer.

### 3.4 Lanceur — `scripts/lancer_t08_v1.sh`, copie de `scripts/lancer_t06_v13.sh`

Mêmes sous-commandes, mêmes codes de sortie. Ce qui change, et rien d'autre :

- les noms (`t08`), la branche de sortie par défaut, la branche d'entrée, l'amorce citée par son empreinte ;
- la ligne de GO, toujours par la variable `GO_ID` ; fin de validité et plafond lus au registre, **prolongations comprises** (constat O-3). La garde de calcul contrôle l'échéance de chaque identifiant d'accord que porte la commande, sans suivre les prolongations ; l'accord d'origine, `GO-2026-11-10-12`, échoit le 30 novembre ; les lignes `GO-2026-11-22-79` et `GO-2026-11-22-93` le prolongent au 31 décembre, et leur colonne « plafond » renvoie à l'accord d'origine au lieu de porter un montant. Jusqu'au 30 novembre, la commande porte `GO-2026-11-10-12`. À partir du 1er décembre, elle porte `GO-2026-11-22-79` et aucun identifiant échu, nulle part dans la commande ; le lanceur vérifie que cette ligne prolonge `GO-2026-11-10-12` et lit le plafond à la ligne d'origine. **Tu ne modifies pas la garde de calcul** ; si la chaîne ne tient pas sans la changer, tu t'arrêtes et tu l'écris à la session mère ; le plafond de la course est **120 USD cumulés sur toutes les tentatives**, dépense antérieure relevée au registre des dépenses ; l'heure passée à l'amorce pour la minuterie est celle où la dépense projetée au prix de l'offre atteint le **plafond restant**, 120 USD moins cette dépense antérieure (constat O-2) ; un reste nul ou négatif : aucune création ; compte rendu à **40 USD** ;
- les bornes de l'offre, celles de « Machine » : une carte A100 SXM4 80 Go, au plus 1,30 USD de l'heure, au moins 8 cœurs effectifs, 64 Go de mémoire vive, 100 Go de disque, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go, fiabilité et débit filtrés comme pour 7b ;
- **aucune relance sur une carte H200**, ni automatique ni proposée ;
- **aucun couperet de temps** ; deux heures sans ligne de progression : alerte, sans arrêt.

### 3.5 Amorce — `scripts/amorce_instance_t08_v1.sh`, copie de `scripts/amorce_instance_t06_v11.sh`

Ce qui change, et rien d'autre :

- le clonage : la branche d'entrée seule, et le code au commit cité par `CODE-T08`, une seule branche, extraction limitée à ce que la course importe ; jamais la branche de sortie de 7b ;
- avant tout calcul : `entrees_v1.exiger_instance_sans_interdits`, le commit du code égal à celui du texte scellé, le texte scellé intact ;
- le commit local de la course : `manifeste.creer_manifeste` exige un arbre propre et le texte scellé sous la racine, et consigne la tête de la racine ; le texte scellé cite le commit du code et ne peut donc pas s'y trouver ; la tête de la course est donc un enfant du commit du code, fait par l'amorce avant la course, et `course_v1.exiger_code_au_commit` compare les chemins gelés à ce commit. Conditions, tenues par programme : (i) son seul parent est le commit que cite `CODE-T08` ; (ii) il n'ajoute que les entrées de la liste blanche de la course à leurs chemins, le texte scellé, la configuration réelle de la course et leurs compagnons — rien sous un chemin gelé, rien d'autre ; la liste est écrite avant, et contrôlée avant la course ; (iii) les entrées viennent de la branche d'entrée seule ; (iv) il est poussé avec les sorties, ancêtre de la tête de la branche de sortie ; (v) auteur et date fixés si cela ne coûte rien, pour qu'il se refasse à l'identique hors de la machine — sinon tu le dis ; (vi) tu rends la commande par laquelle l'exécutante vérifie, après la poussée et par les noms seuls, le parent et la liste des chemins ajoutés. Tu dis aussi comment l'amorce de la course de confirmation faisait ce geste ;
- la liste d'essais ciblée et figée de T0.8, dans un fichier à part, avec le nombre attendu ;
- les modèles : Llama-3.1-8B-Instruct et Llama-3.2-3B-Instruct aux révisions du texte, chargés l'un après l'autre ;
- la commande jouée : `python -m controle_ia.t08.course_v1 --config … --run-id … --prereg …`, une fois ;
- la minuterie du plafond : inchangée dans son mécanisme, avec les montants de T0.8 ; à l'heure où la dépense projetée au prix de l'offre atteint le plafond restant (120 USD moins la dépense antérieure sous cet accord, passée par le lanceur ; constat O-2), elle consigne et pousse les résultats partiels, puis détruit ;
- la fin : sorties scellées poussées sur la branche de sortie, marqueur de fin normale seulement si rien ne reste à pousser ; les bras propres à la course de confirmation (audit de fuite, sondes) sont retirés, et cela se déclare ligne par ligne.

## 4. Essais exigés avant de rendre (R5 : cas sain et artefact pour chaque garde)

- Mode jouet de l'amorce et du lanceur, de bout en bout, sur processeur, sans réseau du loueur ni dépense : la chaîne entière jusqu'à la poussée, deux fois, sorties égales.
- Minuterie : cas sain (heure non atteinte : rien) ; artefact (heure passée : consignation puis ordre de destruction).
- Garde de calcul : commande de création imprimée admise avec un GO valide ; refusée sans GO, avec un GO échu, avec un GO d'un autre type.
- Offre : hors bornes (prix, carte, mémoire) refusée ; H200 refusée.
- Clonage : un fichier interdit présent sur la machine arrête avant tout calcul.
- Plafond restant (O-2) : dépense antérieure nulle, l'heure de la minuterie est celle du plafond entier ; dépense antérieure non nulle, l'heure est plus proche, au montant près ; reste nul ou négatif, aucune création.
- Accord prolongé (O-3) : à une date simulée antérieure au 30 novembre, commande admise avec `GO-2026-11-10-12` ; à une date simulée postérieure, refusée avec `GO-2026-11-10-12`, admise avec `GO-2026-11-22-79`, plafond lu 120 USD par renvoi à la ligne d'origine ; refusée après le 31 décembre ; refusée avec une ligne de prolongation d'un autre accord.
- Antériorité au passage à blanc (m-O2) : lignes `SCELLEMENT-T08` et `CODE-T08` antérieures à l'heure de la machine, code 0 ; ligne `SCELLEMENT-T08` postérieure à l'heure de la machine, refus.
- Alerte de deux heures (m-O2) : une ligne de progression récente, rien ; deux heures écoulées sans ligne, alerte, sans arrêt ni destruction.
- Échantillon de l'audit (L-2), sur la lecture jouet : audit déclenché, le fichier d'échantillon ne porte que les clés désignées par le résultat, et le résultat garde son empreinte ; audit non déclenché, aucun fichier ; une clé hors de l'échantillon demandée, refus.
- Sortie de la lecture (m-L1), sur la lecture jouet : aucune ligne imprimée ne porte un nombre tiré des résultats ; artefact : une ligne qui en porte un fait échouer l'essai.
- Commit local de la course : liste déclarée exacte et parent égal au commit cité, la course part ; artefacts — un fichier de plus, un fichier de moins, un fichier sous un chemin gelé, un parent autre que le commit cité : arrêt avant tout calcul.
- La différence, ligne par ligne, entre chaque fichier copié et son modèle de la course de confirmation, avec la raison de chaque ligne.

## 5. Ce que tu rends

Une branche poussée (`t08/chaine-de-lancement-v1`, nom donné par la session mère), le commit proposé, les empreintes des fichiers, un rapport court scellé (ce qui est fait, essais et nombres, différences déclarées avec la chaîne de la course de confirmation, ce que tu n'as pas pu vérifier, tout refus d'outil, ce que tu as lu et ce que tu n'as pas ouvert), et **les commandes exactes de chaque étape de l'ordre de course**, pour son brouillon des commandes.

## 6. Ce qui n'est pas à toi

La création de la machine, la surveillance, la destruction, les lignes de registre, la lecture et le verdict. Un besoin de changer une règle du texte de T0.8 ou une valeur gelée du code : tu t'arrêtes et tu l'écris à la session mère.
