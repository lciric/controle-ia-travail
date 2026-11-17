# Contre-lecture du code v4 de B bis, tour 2 : le dixième fichier (table conjointe v2) et son essai

- Lecteur : contre-lecteur neuf (R2) ; n'a écrit aucun fichier de B bis, ni le code v4, ni le dixième fichier, ni son essai, ni la
  contre-lecture du tour 1. Périmètre : le dixième fichier et son essai seulement (les neuf fichiers du code v4 ont été lus au
  tour 1 par un autre lecteur ; je ne les ai pas relus, hors la fonction `lire_lignes` de `lecture_v3` dont dépend la correction).
- Date (UTC, `date -u`) : début 2026-11-17T04:11:48Z ; écriture de ce fichier 2026-11-17T04:14:04Z.
- Pièces lues en entier, empreintes recalculées par `sha256sum` :
  1. `brouillons/T0.7-etape-B-bis-v1/second-addendum-v2/code/src/controle_ia/t07bbis/conjointe_v2.py` —
     `8a1b47324a3de57f1d89d327e5e9e538e3574c7fbef8def1a0f7a69392f9b9f7` (égale à l'empreinte annoncée et au compagnon `.sha256`)
  2. `brouillons/T0.7-etape-B-bis-v1/second-addendum-v2/code/tests/test_t07bbis_conjointe_v2.py` —
     `a8397f2a761001e65de5f250c481bcd1d2cdc00e30ef1ef7492e240bfa270962` (égale à l'empreinte annoncée et au compagnon `.sha256`)
- Références :
  3. `src/controle_ia/t07bbis/conjointe_v1.py` — `ea3bc383649e3e81c09f08c28e3bd7b2e7723167e164762369bd815820e332cd`. **Ce fichier
     n'est pas sur `main`** (le paquet `t07bbis` n'y existe pas) : lu sur la branche `prep/t07bbis-code-v1`
     (commit `af0adb141d66ad4b1e9981e90729c24fdea071af`), par `git show` et `git archive`.
  4. `lecture_v3.py` — absent de `main` lui aussi ; lu dans le dossier du brouillon
     (`…/second-addendum-v2/code/src/controle_ia/t07bbis/lecture_v3.py`,
     `c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec`, empreinte égale à celle du tour 1) : lignes 505 à 648
     en entier (`RefusLecture`, `CLES_PROPRES`, `REMPLACABLES_PROPRES`, `lire_lignes`, `exiger_ordre_propre`), le reste par repérage.
  5. `…/second-addendum-v2/contre-lecture-code-v4-tour1-v1.md` —
     `7f7afee0abc7d961047746ec1c807c2f31a8ea0a266934df69f90b329978302c` : § 1 (M1) et § 7 (correction exigée) en entier.
- Aucun fichier ouvert sous `diag/`, `runs/`, `donnees/`, ni `lecture-sondes-t06.json`, ni aucun résultat de course.

## 1. Verdict

**Scellable avec corrections : 0 majeur, 1 mineur exigé (hors des deux fichiers), 2 remarques facultatives.**

- Le majeur M1 est **correctement corrigé**. Les deux fichiers peuvent entrer tels quels, sous leurs empreintes ci-dessus, dans la
  fiche remplaçante de `CODE-BBIS` : aucune correction exigée ne touche leur contenu.
- Le mineur exigé (a) : la « ligne dans l'aide aux différentiels » demandée par le tour 1 (§ 7) n'existe pas, et aucun essai ne
  refait `conjointe_v2` depuis `conjointe_v1`. J'ai refait ce contrôle à la main (§ 2) : égalité exacte. Il reste à la mère soit
  d'ajouter le différentiel sous un nom neuf, soit de déclarer que le contrôle scellé ici en tient lieu.

## 2. Égalité avec `conjointe_v1` hors les changements de M1

`diff` de `conjointe_v1.py` (branche `prep/t07bbis-code-v1`) contre `conjointe_v2.py` : cinq blocs, aucun autre.

| Lieu | Ancien | Nouveau | Exigé par M1 |
|---|---|---|---|
| docstring du module, ligne 1 | « …, v1. » | « …, v2. » plus cinq lignes qui décrivent le changement | oui (docstring du module) |
| `gardes_conjointe`, import | `from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes` | `from .lecture_v3 import CLES_PROPRES, REMPLACABLES_PROPRES, RefusLecture, lire_lignes` | oui, mot pour mot |
| `gardes_conjointe`, appel | `…, propre=True)` | `…, propre=True,` / `remplacables=REMPLACABLES_PROPRES)` | oui, mot pour mot |
| `main`, docstring | `conjointe_v1 --racine` | `conjointe_v2 --racine` | oui |
| `main`, `commande=` | `…t07bbis.conjointe_v1` | `…t07bbis.conjointe_v2` | oui |

Contrôle par programme : les quatre couples du tour 1 (chacun exigé à une occurrence exactement) appliqués à `conjointe_v1.py`
donnent `conjointe_v2.py` à la seule docstring du module près (une ligne changée, cinq ajoutées). Lignes C0 à C6, phrases, états,
`table_famille`, `table_conjointe`, `calculer`, `__all__` : identiques octet pour octet.

Points regardés et sans défaut :
- La ligne 31 garde `from .lecture_v1 import MU_ALLUMEE, MU_MUETTE, MU_NC` (inchangée, comme exigé). Les trois valeurs sont égales
  dans `lecture_v1` (ligne 43) et `lecture_v3` (ligne 49) : aucun effet.
- `REGISTRE_PROPRE` vient toujours de `registre_bbis_v1` (comme le tour 1 l'écrit) ; même valeur que dans `registre_bbis_v2`.
- `CLES_PROPRES` est le même tuple dans `lecture_v1` et `lecture_v3`.
- `lecture_v3.lire_lignes` : deux lignes au plus pour une clé de `remplacables`, la seconde strictement postérieure, la seconde
  rendue (la première sous `remplace`) ; trois lignes, ou seconde non postérieure : `RefusLecture`, repris en `GardeArret` par
  `gardes_conjointe`. Les clés `LECTURE-BBIS`, `VERDICT-BBIS`, `CONJOINTE-BBIS` restent à une ligne (`REMPLACABLES_PROPRES` ne
  contient que `CODE-BBIS`).
- La docstring du module dit « Les neuf fichiers du code v4 restent inchangés » : je ne l'ai pas vérifié (hors périmètre).

## 3. L'essai couvre-t-il R5 (cas sain et artefact)

| Essai | Ce qu'il fait | Constat |
|---|---|---|
| G1, cas sain | registre à deux lignes `CODE-BBIS` (la seconde après `GO-BBIS`), quatre fichiers scellés fabriqués ; la garde passe et rend les chemins | passe ; va jusqu'aux quatre contrôles de sceau |
| G2, artefact | trois lignes `CODE-BBIS` | refus : « table conjointe refusée : ligne CODE-BBIS en double ou mal formée » |
| G3, artefact | seconde ligne antérieure à la première | refus : « table conjointe refusée : ligne CODE-BBIS remplacée : la seconde ligne n'est pas strictement postérieure à la première » |

Les trois cas demandés sont couverts. Épreuve de l'essai lui-même : le même fichier d'essai pointé sur `conjointe_v1` donne
G1 en échec (« ligne CODE-BBIS en double ou mal formée »), G2 et G3 passent : G1 distingue donc bien la v2 de la v1.

Épreuves complémentaires de ma main (hors du dépôt, sur le registre fabriqué de l'essai) :
- seconde ligne à date **égale** à la première : refus (même message que G3) ;
- compagnon `.sha256` de `lecture-bbis.json` faux, registre à deux lignes `CODE-BBIS` : refus (sceau) ;
- ligne `CONJOINTE-BBIS` déjà inscrite, registre à deux lignes `CODE-BBIS` : refus (« la table conjointe est unique »).
Les gardes d'origine tiennent donc avec la ligne remplacée.

## 4. Identifiants de modèle

Aucun. Recherche sans casse dans les deux fichiers de noms de lignées et de fournisseurs (liste large) : zéro occurrence. Lecture
ligne par ligne : rien.

## 5. Clés, empreintes de données, résultats de course

Aucun. Aucune suite hexadécimale de 32 caractères ou plus, aucun nombre décimal de résultat dans les deux fichiers. L'essai
fabrique ses empreintes (`"a" * 64`, ou l'empreinte de `{}` calculée à la volée) et ses fichiers sous `tmp_path`. Les dates du
registre fabriqué sont des dates de registre (dont `2026-11-16T12:57:51Z`, qui ressemble à la date de la vraie première ligne
`CODE-BBIS`) : ni secret ni résultat. Les noms `diag/run-t07`, `diag/run-b` de l'essai sont des dossiers fabriqués sous `tmp_path`.

## 6. Essais lancés

- Commande demandée, sur `main` : `PYTHONPATH=src python -m pytest …/test_t07bbis_conjointe_v2.py -q --tb=short` →
  **erreur de collecte**, `ModuleNotFoundError: No module named 'controle_ia.t07bbis'`. Cause : le paquet `t07bbis` vit sur la
  branche `prep/t07bbis-code-v1`, pas sur `main`, et le dossier du brouillon n'est pas sur le chemin d'import. Ce n'est pas un
  défaut du code.
- Arbre assemblé hors du dépôt (dossier temporaire de session) : `src` de `prep/t07bbis-code-v1` par `git archive`, plus les
  modules du dossier `code/src/controle_ia/t07bbis/` du brouillon, plus l'essai ; empreintes des copies recontrôlées (égales).
  Résultat : **3 passés** (`3 passed in 2.19s`).

## 7. Corrections

**Exigée (mineur a) — différentiel de `conjointe_v2`.** Le tour 1 (§ 7) demandait « sa ligne dans l'aide aux différentiels ».
`code/tests/aide_t07bbis_differentiels_v4.py` ne contient aucune entrée `conjointe`, et l'essai du dixième fichier ne refait pas
le fichier depuis le précédent. L'aide v4 est l'un des neuf fichiers gardés inchangés (R12) : la ligne ne peut y entrer que sous
un nom neuf. Deux voies, au choix de la mère, à écrire dans la fiche remplaçante ou dans le rapport :
1. un fichier neuf (aide et essai, noms neufs) portant les quatre couples du § 2 et l'ajout de docstring, qui refait
   `conjointe_v2.py` depuis `conjointe_v1.py` et exige l'égalité ; ou
2. déclarer que le contrôle du § 2 de ce fichier scellé tient lieu de différentiel pour le dixième fichier.
Aucune des deux voies ne change les deux fichiers lus ici.

**Facultatives.**
- (b) G2 et G3 n'exigent que `match="CODE-BBIS"` : les deux messages de refus le contiennent, donc l'essai ne dit pas lequel des
  deux refus s'est produit. Les messages réels sont les bons (§ 3). Un motif plus serré (« en double » pour G2, « postérieure »
  pour G3) et un cas à date égale rendraient l'essai plus net ; cela changerait l'empreinte de l'essai.
- (c) Rappels pour la mère, déjà dans le tour 1 : le nom `conjointe_v2` est un écart de nom au plan (point 11) à déclarer ; la
  fiche remplaçante de `CODE-BBIS` doit lister le dixième fichier et son essai ; le compte des essais monte de 3
  (`MIN_ESSAIS` est un plancher et peut rester).

## 8. Incidents de ma main

- Un de mes scripts de contrôle, passé au shell sans protéger des accents graves, a fait tenter au shell
  `python -m controle_ia.t07bbis.conjointe_v1 --racine` : échec immédiat (« No module named 'controle_ia' »), rien exécuté, rien
  écrit. Contrôle relancé correctement.
- Le premier lancement de l'essai sur `main` (erreur de collecte) a pu écrire un cache d'octets dans
  `code/tests/__pycache__/` du brouillon (dossier déjà présent avant moi). Aucun autre fichier du dépôt écrit, hors ce
  fichier-ci et son compagnon.
