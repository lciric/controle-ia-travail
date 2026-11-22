# Contre-lecture (classe B) — outils de l'épreuve, v4

- **Commit et dossier.** Commit 8ca87520, dossier `docs/notes/memoire-conception-v1/epreuve-outils-v1/`.
- **Pièces lues.**
  - `recherche_autorisee_v1.py` (980657b8…), lu en entier.
  - `verifier_citations_v4.py` (6a127ac3…), lu par son écart avec la v3.
  - `test_outils_epreuve_v4.py` (22ed7b7a…).
  - Les trois empreintes sont conformes à leurs compagnons.
- **Contexte lu.** `epreuve-bibliothecaire-v3.md`, en-tête « Version 3 », points 1 à 5, et rien d'autre.
- **Cloisonnement.** Je n'ai ouvert aucun fichier des deux dossiers « ne-pas-lire » : je les ai seulement comptés et testés avec des chemins construits.

## Verdicts

- **recherche_autorisee_v1.py : non conforme.** L'outil montre au bras « memo » les 38 fichiers du dossier `epreuve-essai-1-ne-pas-lire-bibliothecaire-v1/`. Il les laisse lister, lire et chercher.
- **verifier_citations_v4.py : non conforme.** Il porte la même règle, et accepte donc ces lectures. Un dossier exclu déclaré comme ouvert est ignoré au lieu d'être compté comme manquement.

## Défauts

1. **Grave : la règle commune laisse ouvert le dossier de l'essai 1** (`chemin_autorise`, `EXCLUS_DOSSIERS`, ligne 46 de la v3, reprise par la v4).
   - Seul le dossier de la banque est exclu. Le dossier `epreuve-essai-1-ne-pas-lire-bibliothecaire-v1/` passe par l'autorisation de `docs/notes/memoire-conception-v1/`.
   - **Mesure.** `lister docs/notes/memoire-conception-v1 --bras memo` rend 38 chemins de ce dossier, soit tous ceux qu'il compte au commit. `chemin_autorise_bras(…/epreuve-essai-1-ne-pas-lire-bibliothecaire-v1/x.md, "memo")` vaut `(True, "")`.
   - **Risque.** Ce dossier contient au moins le verdict de l'examinateur de l'essai 1. L'essai 1 portait sur les 90 questions, donc aussi sur la moitié « réserve » que l'essai 2 réemploie. Un répondant du bras « memo » pourrait y lire des questions, des clés ou des réponses de l'essai 2.
   - **Correction.** Exclure tout segment qui contient « ne-pas-lire », plutôt qu'une liste de noms. Ajouter un essai pour chacun des deux dossiers.
   - **Avant l'essai 2.** Vérifier qu'aucun répondant n'a déjà employé l'outil à ce commit.
2. **Moyen : la porte 1 ne peut rien prouver si le répondant peut lire ou écrire en dehors de l'outil.**
   - **Lecture hors de l'outil.** Elle n'est détectée que si le fichier lu est cité. Un fichier exclu lu par le shell, puis non cité, ne laisse aucune trace. Seules les chaînes-canaris le verraient, et elles ne sont pas codées.
   - **Journal écrit à la main.** Le journal est un JSONL ordinaire. Un répondant qui peut écrire y ajoute des lignes, et le vérificateur les accepte. Mutation : une ligne `"action": "empreinte"`, que l'outil n'écrit jamais, fait accepter une citation. Le vérificateur ne regarde ni l'action, ni le commit, ni le bras de la ligne.
   - **Correction de procédure.** Les répondants n'ont que cet outil : pas de Bash, de Read ni de Grep. Le journal est hors de leur portée d'écriture. Il est scellé après chaque lot.
   - **Correction de code.**
     - L'outil écrit `commit`, `bras` et l'heure à chaque ligne du journal.
     - Le vérificateur refuse une ligne dont l'action n'est pas `lire` ou `chercher`, ou dont le commit ou le bras diffère.
     - On peut ajouter un chaînage par empreinte, chaque ligne portant l'empreinte de la précédente.
3. **Moyen : un dossier exclu déclaré comme ouvert est ignoré par le vérificateur** (lignes 238 à 242 de la v4).
   - Mutations : le dossier de la banque, ou `diag/`, déclaré dans `fichiers_ouverts`, laisse la porte 1 tenir. En v3, la porte tombait.
   - Le point 2 de l'en-tête de l'épreuve v3 ignore les dossiers déclarés. Mais un dossier **exclu** déclaré signale un accès hors de l'outil.
   - **Correction.** N'ignorer qu'un dossier autorisé au bras. Un dossier exclu reste un manquement.
4. **Faible : journal des deux bras mêlés.** Si le même journal contient des lignes des deux bras, le vérificateur lancé en `--bras base` compte comme manquement la lecture du mémo par un agent du bras « memo » (mutation). Il faut un journal par bras, et l'écrire dans le mandat de l'examinateur. Le point 2 (bras écrit dans chaque ligne) règle aussi ce cas.
5. **Faible : champ `agent` non décrit.** La réponse doit porter un champ `agent` égal au nom écrit au journal. Sans lui, toute citation devient une « lecture hors outil » ; l'erreur va du côté sûr. Le format décrit en tête des deux scripts ne mentionne pas ce champ : il faut l'ajouter au format et au mandat.
6. **Faible : chemins mal servis par l'outil.**
   - L'outil refuse un chemin absolu dans le dépôt. `RACINE_DEPOT` n'est fixé que par `vc4.main`, alors que le vérificateur accepte ce chemin. Ça va du côté sûr, mais l'outil et le vérificateur ne disent pas la même chose.
   - `git ls-tree` sans `-z` met les noms non ASCII entre guillemets. Il n'y en a aucun au commit.
   - Un motif d'expression régulière catastrophique peut bloquer `chercher`, sans rien laisser fuir.

## Ce qui tient (vérifié)

- **Chemins tordus refusés.** Banque directe, banque par `../`, chemin absolu (refusé par l'outil), `diag/x` : « REFUS ». Aucune empreinte n'est rendue pour un chemin refusé. `./CLAUDE.md` est accepté, ce qui est juste.
- **Liens symboliques.** Aucun lien symbolique ni sous-module au commit. De toute façon, `git show` d'un lien n'en rend que la cible.
- **Bras « base ».** Le dossier du mémo est fermé à `lire`, à `empreinte`, à `chercher` et à `lister` : zéro chemin. Aucune copie du mémo ne figure hors de ce dossier, ni par son nom, ni par `git grep` dans `registres/`, `docs/decisions/` et `CLAUDE.md`.
- **Journal.** Chaque fichier dont une ligne est montrée est journalisé avant l'affichage, par `lire` et par `chercher`. `lister` et `empreinte` ne montrent pas de contenu.
- **Vérificateur.**
  - Un fichier cité absent du journal de son agent : manquement.
  - Une citation présente au journal : acceptée.
  - Journal absent ou ligne sans chemin : arrêt.
- **Absence de régression des règles de la v3.**
  - Sur l'arbre : 0 fichier hors de la sous-liste des demandes ; aucun autorisé refusé par un nom de dossier.
  - Accents retirés.
  - `demande-x/r.md` refusé.
  - Banque et `quarantaine` refusées en dernier segment.
  - Barre finale retirée.
- **Essais du dépôt.** 11 passent.

## Fichiers

- Arbre au commit, sans les dossiers « ne-pas-lire » : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/arbre4.txt`
- Règles rejouées : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/citations_regles_v4.py`
- Journal de l'outil pendant les essais : `/tmp/claude-0/-home-user-controle-ia-travail/843c976b-9f50-5dab-a935-be69fc2798dc/scratchpad/mut/j4.jsonl`
