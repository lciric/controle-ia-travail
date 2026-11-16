# Contre-lecture du programme de lecture de l'audit R4 de la base (A) (v1)

Contre-lecteur neuf (R2, modèle C), 2026-11-16, 17:15 à 17:16 UTC (`date -u`). Je n'ai écrit ni le programme ni son essai. Je n'ai ouvert aucune donnée de 7a, 7b, T0.6 (résultats), T0.7, P3-bis, de l'étape B bis, du bras d'attaque ni du mode tenu à l'écart ; rien sous `diag/`, `runs/`, `donnees/`. Calcul léger (essai de quelques secondes, jouets seulement).

## Verdict : conforme

Le programme lit le seul booléen `audit_r4.declenche`, après contrôle du compagnon et de l'empreinte rendue par l'hôte, et n'imprime qu'une ligne d'état. Aucune autre donnée du fichier ne peut sortir. Aucune correction n'est exigée. Trois remarques mineures, sans effet sur le verdict, sont en fin de rapport.

## Empreintes vérifiées

| pièce | sha256 | compagnon |
|---|---|---|
| `lecture_audit_r4_base_a_mere_v1.py` | `2e486465cae1e5793320490ef6078510257a5a9fc97e73c0e42159e167747445` (égale à celle de la tâche) | conforme |
| `essai_lecture_audit_r4_base_a_mere_v1.sh` | `b0906d988f43fd5a9287f19237136c076b843b95017e643859ffbd25d7aa538c` | conforme |
| `essai-lecture-audit-r4-base-a-mere-sortie-v1.txt` | (compagnon) | conforme |

## 1. Nom et place du champ dans le code de la pièce

Code cité : ligne `CODE-MOTS-ET-COUT-T06` de `registres/scellements-v1.md` (l. 16), registre `registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json`, commit `da06bb57610f840152e4e9a8c449b036577cc582`, fichier `scripts/mots_et_cout_t06_v3.py`. Son empreinte lue au commit (`9dbcc55c…c4e674`) égale celle du registre. Dans ce fichier :

- `FICHIER_BASE_A = "base-a-t08.json"` (l. 220) ;
- la fonction `audit_r4` (l. 1388) rend un dictionnaire dont la clé `"declenche"` vaut `bool(motifs)` (l. 1433), donc un vrai booléen ;
- ce dictionnaire est mis dans la racine du document sous la clé `"audit_r4"` (l. 1501) ;
- l'écriture passe par `_json_texte` (l. 281 : objet JSON, `sort_keys=True`, `allow_nan=False`, indentation 2) puis `sceller` (l. 1535) ;
- le texte scellé de T0.8 (`prereg/T0.8-base-A-mots-et-cout-v1.md`, l. 111 et 135) place l'audit R4 dans `base-a-t08.json` et l'action « relecture avant `ISSUE-MOTS-ET-COUT-T06` » : cohérent avec le point 3 de GO-2026-11-16-07 (registre `go.md`, l. 348).

Le chemin lu par le programme (`audit_r4` puis `declenche`, racine objet) est donc le bon. Le compagnon produit par `controle_ia.scellement` est « `<sha256>  <nom>` » sur une ligne (`_LIGNE`, l. 27 de `scellement.py`), format que le programme exige.

## 2. Rien d'autre n'est imprimé, écrit ou gardé

Lecture complète du code :

- Sortie : une seule ligne sur la sortie standard, trois formes (`déclenché`, `non déclenché`, `refus — <motif>`), rien sur l'erreur. Le `-h` est désactivé (`add_help=False`) et `error` est surchargée : argparse ne peut ni afficher d'usage ni sortir par son propre chemin. Un `except Exception` final n'imprime que le nom du type.
- Motifs de refus : aucun ne contient une valeur lue. Les motifs de type n'affichent que le nom du type Python ; la clé en double dit « nom non affiché » ; les erreurs JSON et UTF-8 ne montrent que le nom de l'exception. Seuls 12 caractères d'une empreinte de fichier ou de l'hôte sont montrés dans les refus d'empreinte : une empreinte tronquée d'un fichier entier n'apprend rien sur son contenu (et l'hôte la connaît déjà).
- Écriture : aucune (`read_bytes`, `read_text` seulement). L'essai vérifie par `cmp` que le fichier n'est pas modifié (S3b).
- Gardé : l'objet décodé est supprimé (`del doc`, `del audit`) dès le booléen extrait ; la fonction rend un booléen seul. Le texte et les octets sont supprimés. Aucun cache, aucun fichier temporaire, aucune variable d'environnement lue.
- Bibliothèque standard seule ; lancement conseillé `python3 -I -B`.

## 3. Refus

Ordre des contrôles conforme au docstring : nom exact `base-a-t08.json` ; empreinte de l'hôte en 64 chiffres minuscules ; fichier ordinaire non lien ; compagnon non lien, une ligne, bon format, bon nom ; empreinte du fichier égale au compagnon et à l'hôte ; UTF-8 ; JSON strict (clé en double, NaN et infinis refusés) ; racine objet ; `audit_r4` présent et objet ; `declenche` présent et de type `bool` (`1`, `"true"`, `null` refusés). Aucun repli : tout échec rend le code 1 et une ligne de refus. Mes essais complémentaires : exécution sous `LC_ALL=C`, `POSIX`, `en_US.ISO-8859-1`, avec `PYTHONIOENCODING=ascii` : la ligne sort bien (le mode `-I` ignore la variable, Python 3.13 force UTF-8) ; entier de 23 chiffres et `1e999` ailleurs dans le fichier : ignorés, sans effet ; `-h` : refus d'une ligne, code 1, rien sur l'erreur ; abréviations d'option (`--fich`, `--emp`) acceptées, sans conséquence.

## 4. Rejeu de l'essai (jouets seulement)

`bash essai_lecture_audit_r4_base_a_mere_v1.sh <dépôt> <bac neuf dans le dossier temporaire de session>` : code 0, « BILAN : 28 conformes sur 28 », « ESSAI : TOUT CONFORME ». Hors lignes de date, la sortie est identique octet pour octet à la sortie scellée. Couverture : 3 cas sains (déclenché, non déclenché, ordre des options inversé) et l'absence d'écriture ; 8 artefacts d'empreinte et de compagnon (dont A7, fichier altéré et rescellé, refusé par l'empreinte de l'hôte) ; 8 artefacts de champ (type chaîne, nombre, null, `audit_r4` booléen, racine liste, clé en double) ; 8 artefacts de fichier (JSON tronqué, non UTF-8, NaN, absent, lien symbolique, mauvais nom, option manquante, option inconnue). Chaque cas contrôle le code, une seule ligne, rien sur l'erreur, le texte exact ou le motif, et l'absence de toute valeur marquée `SECRET` ou `0.7777` plantée dans les champs voisins. Les jouets reproduisent la forme réelle de la pièce (racine objet, clés triées, `audit_r4` avec `motifs`, `items`, `echantillons`, compagnon de `sceller`). La garde est éprouvée sur cas sain et sur artefact (R5).

## 5. Comparaison au bloc M (`lecture_etat_ba_l2_mere_v1.py`)

Même modèle (bibliothèque standard, lecture seule, une ligne, motifs sans valeur). Différences, toutes dans le sens de la règle N-C :

- M passe par le registre (ligne `LECTURE-T08-BASE-A`, date, chemin) ; ce programme prend le fichier et l'empreinte rendue par l'hôte (celle du bloc B5b), sans lecture du registre : plus étroit, et le contrôle de l'empreinte contre l'hôte rattrape un fichier altéré et rescellé, ce que le compagnon seul ne ferait pas.
- M décode le document avec `json.loads` simple ; ici JSON strict (doublons, NaN) et suppression de l'objet décodé.
- M parcourt un chemin choisi par `--cle-json` ; ici le chemin est figé, et l'option est refusée (cas A24), ce qui ferme toute lecture d'un autre champ.
- M rend 0, 3 ou 2 selon l'état ; ici « déclenché » et « non déclenché » rendent tous deux 0 et l'état n'est porté que par la ligne imprimée. L'appelant doit donc lire la ligne, non le code. Les refus rendent 1. Cohérent avec « n'imprimer qu'une ligne d'état » ; à noter pour la mère.
- M peut laisser sortir un traceback sur une erreur d'appel (son `__main__` imprime `ERREUR D'APPEL` avec le message d'exception) ; ici rien de tel.

## Remarques mineures (sans effet sur le verdict)

1. Le code de sortie ne distingue pas « déclenché » de « non déclenché » (voir ci-dessus) : la mère doit tester la ligne exacte, et traiter tout autre texte, ou le code 1, comme un refus qui arrête avant l'inscription de `ISSUE-MOTS-ET-COUT-T06`.
2. Le programme ne vérifie pas le dossier ni la ligne `LECTURE-T08-BASE-A` du registre : le choix du fichier et la fraîcheur restent à la charge de l'hôte (empreinte rendue au bloc B5b) et de la commande. Cohérent avec le point 3 du GO, qui ne demande que l'état lu par programme.
3. Le docstring dit « ne lit du fichier que `audit_r4.declenche` » : le fichier entier est décodé en mémoire (inévitable pour du JSON) puis jeté ; le sens voulu (aucune autre valeur imprimée ni conservée) est exact.

Sceau : ce rapport est scellé par `PYTHONPATH=src .venv/bin/python -m controle_ia.scellement sceller`.
