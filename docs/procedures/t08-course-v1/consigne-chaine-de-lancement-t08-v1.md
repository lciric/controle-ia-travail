# Consigne — écrire la chaîne de lancement de la course de la base boîte noire (T0.8) — v1

- **Nature** : mandat (classe C). Le code qu'il commande est de classe B : contre-lecture par un autre modèle, puis vérification des corrections par le même contre-lecteur.
- **Écrite** le 2026-11-22 par le rédacteur du texte de T0.8 (modèle B). **Pour** : un développeur neuf du modèle A, lancé par la session mère ; ce peut être celui de l'alignement du code, après son rendu.
- **Pourquoi** : le code de la course et de la lecture existe (`src/controle_ia/t08/`), mais rien ne le lance sur une machine louée. Son développeur l'a écrit le 14 novembre : « aucun script de lancement n'est écrit » ; la lecture réelle n'a pas d'entrée en ligne de commande ; les configurations réelles sont à écrire (rapport `docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md`, § 6, sur la branche du code). Sans cette chaîne, aucune création n'est possible.

## 1. La règle de conception : copier, ne pas réécrire

La course de confirmation a une chaîne éprouvée : `scripts/lancer_t06_v13.sh` et `scripts/amorce_instance_t06_v11.sh`, mûris sur treize et onze versions, chacune née d'un défaut vu en réel (minuterie, verrou des consignations, clonage réduit, masquage des clés, inventaire vide, offre retirée). **Tu pars de ces deux fichiers, copiés sous des noms neufs, et tu n'y changes que ce que cette consigne nomme.** Chaque ligne changée est déclarée dans ton rapport, avec sa raison. Une réécriture, même plus propre, n'est pas ce qui est demandé : elle perdrait ces corrections.

## 2. Ce que tu lis, et ce que tu n'ouvres jamais

**À lire** : le texte de T0.8, `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon14.md` (branche `prep/t08-texte-complet-fable-v1`) — « Plan d'analyse » (points 1 à 5 et 10), « Liste d'arrêt », « Machine, devis et dépense », « Ordre des lectures et embargo » ; l'ordre de course, `docs/procedures/t08-course-v1/ordre-course-t08-v1-brouillon1.md` ; le code de T0.8 au commit aligné (branche de l'alignement), dont `course_v1.py`, `lecture_v1.py`, `entrees_v1.py`, `configuration_v1.py`, `essai_jouet_v1.py` ; les deux scripts de la course de confirmation nommés au § 1, le module de session qu'ils appellent et leurs listes d'essais ; `.claude/hooks/garde_calcul.py` ; l'en-tête de `registres/go.md` et les lignes `GO-2026-11-10-12`, `GO-2026-11-22-79`, `GO-2026-11-22-93`.

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

### 3.4 Lanceur — `scripts/lancer_t08_v1.sh`, copie de `scripts/lancer_t06_v13.sh`

Mêmes sous-commandes, mêmes codes de sortie. Ce qui change, et rien d'autre :

- les noms (`t08`), la branche de sortie par défaut, la branche d'entrée, l'amorce citée par son empreinte ;
- la ligne de GO, toujours par la variable `GO_ID` ; fin de validité et plafond lus au registre ; le plafond de la course est **120 USD cumulés sur toutes les tentatives**, dépense antérieure relevée au registre des dépenses ; compte rendu à **40 USD** ;
- les bornes de l'offre, celles de « Machine » : une carte A100 SXM4 80 Go, au plus 1,30 USD de l'heure, au moins 8 cœurs effectifs, 64 Go de mémoire vive, 100 Go de disque, stockage au plus 0,08 USD de l'heure, téléchargement au plus 0,05 USD par Go, fiabilité et débit filtrés comme pour 7b ;
- **aucune relance sur une carte H200**, ni automatique ni proposée ;
- **aucun couperet de temps** ; deux heures sans ligne de progression : alerte, sans arrêt.

### 3.5 Amorce — `scripts/amorce_instance_t08_v1.sh`, copie de `scripts/amorce_instance_t06_v11.sh`

Ce qui change, et rien d'autre :

- le clonage : la branche d'entrée seule, et le code au commit cité par `CODE-T08`, une seule branche, extraction limitée à ce que la course importe ; jamais la branche de sortie de 7b ;
- avant tout calcul : `entrees_v1.exiger_instance_sans_interdits`, le commit du code égal à celui du texte scellé, le texte scellé intact ;
- la liste d'essais ciblée et figée de T0.8, dans un fichier à part, avec le nombre attendu ;
- les modèles : Llama-3.1-8B-Instruct et Llama-3.2-3B-Instruct aux révisions du texte, chargés l'un après l'autre ;
- la commande jouée : `python -m controle_ia.t08.course_v1 --config … --run-id … --prereg …`, une fois ;
- la minuterie du plafond : inchangée dans son mécanisme, avec les montants de T0.8 ; à l'heure où la dépense projetée au prix de l'offre atteint le plafond, elle consigne et pousse les résultats partiels, puis détruit ;
- la fin : sorties scellées poussées sur la branche de sortie, marqueur de fin normale seulement si rien ne reste à pousser ; les bras propres à la course de confirmation (audit de fuite, sondes) sont retirés, et cela se déclare ligne par ligne.

## 4. Essais exigés avant de rendre (R5 : cas sain et artefact pour chaque garde)

- Mode jouet de l'amorce et du lanceur, de bout en bout, sur processeur, sans réseau du loueur ni dépense : la chaîne entière jusqu'à la poussée, deux fois, sorties égales.
- Minuterie : cas sain (heure non atteinte : rien) ; artefact (heure passée : consignation puis ordre de destruction).
- Garde de calcul : commande de création imprimée admise avec un GO valide ; refusée sans GO, avec un GO échu, avec un GO d'un autre type.
- Offre : hors bornes (prix, carte, mémoire) refusée ; H200 refusée.
- Clonage : un fichier interdit présent sur la machine arrête avant tout calcul.
- La différence, ligne par ligne, entre chaque fichier copié et son modèle de la course de confirmation, avec la raison de chaque ligne.

## 5. Ce que tu rends

Une branche poussée (`prep/t08-chaine-de-lancement-v1`), le commit proposé, les empreintes des fichiers, un rapport court scellé (ce qui est fait, essais et nombres, différences déclarées avec la chaîne de la course de confirmation, ce que tu n'as pas pu vérifier, tout refus d'outil, ce que tu as lu et ce que tu n'as pas ouvert), et **les commandes exactes de chaque étape de l'ordre de course**, pour son brouillon 2.

## 6. Ce qui n'est pas à toi

La création de la machine, la surveillance, la destruction, les lignes de registre, la lecture et le verdict. Un besoin de changer une règle du texte de T0.8 ou une valeur gelée du code : tu t'arrêtes et tu l'écris à la session mère.
