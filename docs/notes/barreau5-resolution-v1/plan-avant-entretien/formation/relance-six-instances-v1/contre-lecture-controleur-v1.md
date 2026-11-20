# Contre-lecture du contrôleur du registre candidat (`controler_registre_candidat_v1.py`, sha256 5bb9751f…)

**Verdict : utilisable**, à condition de le jouer avec l'interpréteur de l'environnement de formation (`$S/venv-b5f/bin/python`). Trois remarques mineures suivent ; aucune ne bloque.

## Ce qui est demandé

- **Il lit le fichier tel quel.** Le chemin est passé aux deux sous-processus. Le premier lit par `lire_registre(Path)`, le second par `read_text(encoding="utf-8")`, et les deux passent par le même `engagement_v1`. L'empreinte du fichier est relevée avant et après la lecture. Rien n'est écrit.
- **Il appelle les bons codes, chacun isolé.**
  - Premier sous-processus : `formation_v1.lire_code_et_accord`.
  - Second sous-processus : `lecture_v1.relance_du_registre`.
  - Chacun a son propre `PYTHONPATH`, un répertoire courant neutre et un environnement réduit.
  - L'empreinte de `formation_v1.py` (de d116bf78), celle de `lecture_v1.py` (ed0999df…, celle que citent `CODE-LECTURE-B5F` et `EPREUVE-B5F`) et celle de `engagement_v1.py` (565d4e51…, des deux côtés) sont vérifiées avant la lecture.
  - Le chemin du module chargé est contrôlé dans chaque arbre.
- **Il n'accepte rien de mal formé.**
  - Il exige en plus : les instances exactement [1,2,3,4,5,7] et dans cet ordre, l'accord GO-2026-11-19-86, et le commit d116bf78.
  - Toute erreur, toute sortie illisible et tout dépassement du délai mènent au refus.
  - L'épreuve de l'auteur joue 20 cas, tous conformes.
  - J'ai rejoué le cas sain sur le registre de `origin/main` à jour plus la ligne : ACCEPTÉ, code de sortie 0.

## Un artefact que seule la seconde lecture refuse
**Par le contenu du registre, il n'en existe pas.** Le code figé lit avec le même `engagement_v1.py`, identique à l'octet. Son expression `_RELANCE` est la même que celle de `formation_v1`. Et `relance_du_registre` ne fait rien de plus que : présence de la ligne, contenu conforme à `_RELANCE`, instances triées. `lire_code_et_accord` fait tout cela et davantage, et le contrôleur exige ensuite l'ordre exact. Tout registre qui passe la première lecture passe donc la seconde.

**Par l'arbre, il en existe un.** Je l'ai joué dans `$S/relance/verif-ctrl/` :
- Arbre figé dont `controle_ia/gardes.py`, fichier non épinglé, est altéré pour lever une erreur : la première lecture passe, la seconde refuse (« code de lecture figé (lecture_v1.relance_du_registre) : … RuntimeError »). Le refus de la seconde lecture remonte bien.
- Même arbre, avec un changement sans effet dans `gardes.py` : ACCEPTÉ (voir la remarque 1).
- Interpréteur système, sans torch : REFUSÉ, à juste titre, mais pour une raison d'environnement (voir la remarque 2).

## Remarques mineures
1. **L'arbre figé n'est épinglé que par deux fichiers.** Seuls `lecture_v1.py` et `engagement_v1.py` sont vérifiés ; les autres modules importés ne le sont pas (`gardes`, `scellement`, `manifeste`). Sans effet sur l'acceptation, puisque la seconde lecture est plus faible que la première. Pour la propreté, extraire l'arbre figé à neuf par `git archive c76e79169eee337ce66c7d88f62d039e853eebfc src`, juste avant le contrôle.
2. **Interpréteur.** Jouer avec `$S/venv-b5f/bin/python`. Le contrôleur reprend son propre interpréteur (`sys.executable`) pour les sous-processus, et `formation_v1` importe torch.
3. **Ce que le contrôleur ne vérifie pas.** Il ne dit pas que le candidat est le registre de `main` plus une seule ligne, sans retouche des lignes antérieures. Ajouter, ou faire à la main : `head -n -1 CANDIDAT | cmp - <(git show origin/main:registres/barreau5-familles-jumelles-v1.md)`. Accessoire : avec `-c`, le répertoire courant (`/`) entre dans le chemin des modules ; l'option `-P` de Python 3.11 l'en retirerait.
