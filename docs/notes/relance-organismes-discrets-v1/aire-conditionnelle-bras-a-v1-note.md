# Programme de l'aire conditionnelle, bras A — version 1, et garde statique version 14 : note du code

Écrit le 22 novembre 2026 par un agent de la session de relance (Opus 5.5), sur processeur seul, sans réseau hors poussage git, sans dépense. Décision de la session mère : option (a′), confiance 0,7. **Non contre-lu.**

## Verdict

Le point d'entrée en commande de l'aire conditionnelle existe : lancé à part par l'enchaînement de la lecture de la discrétion (version 2), il joue l'étape (n) réelle de bout en bout sur une livraison fabriquée (code 0, une ligne JSON, vingt aires confrontées au fichier scellé des grandeurs). La garde statique version 14 l'admet et ne rend aucune violation sur `src/` et `scripts/` du dépôt. **Réserve bloquante pour la commande réelle** : l'enchaînement version 2 importe la garde statique **version 13**, qui refuse désormais le dépôt (elle voit le nouveau programme et la garde version 14) ; la commande réelle de l'enchaînement s'arrête donc avant tout constat tant qu'un enchaînement version 3, branché sur la garde version 14, n'existe pas (réserve 1).

## Fichiers

| fichier | sha256 |
|---|---|
| `src/controle_ia/organismes_discrets/aire_conditionnelle_bras_a_v1.py` | `0f1e76409e07b7535b2e18bf312ff031164608a77b010a46d2dd847e45696df2` |
| `src/controle_ia/organismes_discrets/cloisonnement_bras_a_v14.py` | `44e8497275795c9bfb50c857dc21d80a049f9ded6eefe792c21a00ffb041d7f6` |
| `tests/test_aire_conditionnelle_bras_a_v1.py` | `7de4d82f391f9733e64b08391f2a55771aa3dae63a452b6583131ef3800d4cf9` |
| `docs/notes/relance-organismes-discrets-v1/preuve-difference-garde-v14-v1.py` | `b9787b1dccf56f3a6261e95e6ce9b4a11c016cc353cb539672a77894d749c0ec` |

Compagnons `.sha256` à côté de chacun. Code appelé, non modifié : analyse version 13 (`a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf`), enchaînement version 2 (`3b3c3a8be03968531ae43e4f14612105dd8494fc489b53956c4d123ad123ea0a`), garde statique version 13 (`fa915de2a81b27751860479d2cfe6472dabb004d4790dafd186210aacd0604d6`).

## Ce que fait le programme de l'aire conditionnelle

1. **Avant tout** (ni arguments, ni entrée standard, ni pièce lus) : cherche, paquet par paquet sur `sys.path`, par le chercheur de chemins de Python et sans exécuter aucun paquet, le fichier que l'import de `controle_ia.organismes_discrets.analyse_bras_a_v13` prendrait ; son empreinte doit valoir exactement `a7ebf29f…`, sinon code 4. Import ensuite **sans cache de code compilé** (préfixe de cache porté sur un dossier vide, écriture du cache coupée) ; après l'import, le module chargé doit venir de ce fichier, toujours à la même empreinte.
2. Lit les arguments du contrat (`--configuration`, `--sortie`, `--fichier-des-unites`, `--sortie-d-origine`) et l'entrée standard (quatre clés, clé en double et constantes non numériques refusées) ; met les comptes d'actions désappariées dans la forme que l'analyse attend (table (tâche, épisode) → compte, par dose écrite ; un épisode écrit deux fois est refusé, rien n'est retiré ni calculé).
3. Compose les trois fonctions de l'analyse : lecture du fichier des rangs (usage de l'aire conditionnelle) → `aires_conditionnelles` → `ecrire_fichier_des_grandeurs_de_l_etape_n` ; écrit la ligne `{"aires": {dose: {moniteur: sortie}}, "cles": [...]}`.
4. Codes : 0 ligne écrite ; 3 arrêt de la lecture de la discrétion (consigné par l'analyse), sortie standard vide ; 4 garde (de l'analyse : l'étape seule est nommée, **jamais son message** ; ou du programme : empreinte, forme de l'entrée), une ligne d'erreur ; 8 erreur inattendue, son type seul ; 2 erreur d'arguments (`argparse`). L'enchaînement ne rend rien des codes 2 et 8.

**Où il trouve `controle_ia`** : l'enchaînement version 2 le lance depuis une copie dans un dossier temporaire, avec `PYTHONPATH=<racine du code>/src` et le dossier de travail à la racine du code (`_environnement`, `jouer_l_aire_conditionnelle`). Le programme suit ce chemin ; il ne déduit rien de son propre emplacement (qui est une copie).

## Garde statique version 14 et preuve de la différence

Copie de la version 13 ; différences, toutes nommées : titre (ligne 1) et paragraphe « Ce qui change à la version 14 » (lignes 6 à 10) ; `PROGRAMMES_DE_L_AIRE_CONDITIONNELLE` = celle de la version 13 + `aire_conditionnelle_bras_a_v1.py` ; **`GARDES_STATIQUES` = celle de la version 13 + `cloisonnement_bras_a_v14.py`** — différence nécessaire, non prévue par la consigne : sans elle, la garde version 14 se refuse elle-même (elle écrit les noms réservés dans ses chaînes). Aucune empreinte n'entre dans la liste : les programmes autorisés le sont par chemin exact et doivent répondre à leur compagnon.

Sortie de `python docs/notes/relance-organismes-discrets-v1/preuve-difference-garde-v14-v1.py` (code 0) :

```
PROGRAMMES_DE_L_AIRE_CONDITIONNELLE : version 13 + 'src/controle_ia/organismes_discrets/aire_conditionnelle_bras_a_v1.py' (11 → 12 chemins)
GARDES_STATIQUES : version 13 + 'src/controle_ia/organismes_discrets/cloisonnement_bras_a_v14.py' (9 → 10 chemins)
--- cloisonnement_bras_a_v13.py
+++ cloisonnement_bras_a_v14.py
@@ -1 +1 @@
-"""Garde statique du bras A des organismes discrets, version 13 du code (préenregistrement
+"""Garde statique du bras A des organismes discrets, version 14 du code (préenregistrement
@@ -6,2 +6,5 @@
-donne `src` et `scripts`, depuis la racine du dépôt). `cloisonnement_bras_a_v12.py` n'est pas modifié (R12). **Ce qui
-change à la version 13** : le programme d'analyse et la garde statique de la version 13 rejoignent les programmes
+donne `src` et `scripts`, depuis la racine du dépôt). `cloisonnement_bras_a_v13.py` n'est pas modifié (R12). **Ce qui
+change à la version 14** (décision de la session mère, option (a′)) : le point d'entrée en commande de l'aire
+conditionnelle, `aire_conditionnelle_bras_a_v1.py`, rejoint les programmes de l'aire conditionnelle, par son chemin
+exact ; la garde statique de la version 14 rejoint les gardes statiques ; rien d'autre. **Ce qui avait changé à la
+version 13** : le programme d'analyse et la garde statique de la version 13 rejoignent les programmes
@@ -99,2 +102,3 @@
-PROGRAMMES_DE_L_AIRE_CONDITIONNELLE = tuple(PAQUET + f"analyse_bras_a_v{k}.py" for k in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
-GARDES_STATIQUES = tuple(PAQUET + f"cloisonnement_bras_a_v{k}.py" for k in (5, 6, 7, 8, 9, 10, 11, 12, 13))
+PROGRAMMES_DE_L_AIRE_CONDITIONNELLE = (tuple(PAQUET + f"analyse_bras_a_v{k}.py" for k in (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
+                                      + (PAQUET + "aire_conditionnelle_bras_a_v1.py",))
+GARDES_STATIQUES = tuple(PAQUET + f"cloisonnement_bras_a_v{k}.py" for k in (5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
PREUVE TENUE : seules différences — en-tête déclaré (lignes 1, 6 à 10 de la version 14) et un chemin ajouté à chacune des deux listes déclarées
```

La preuve, éprouvée sur des copies mutées (dossier temporaire de la session) : nom réservé retiré d'une autre liste → échec (code 1) ; deux chemins ajoutés à la liste de l'aire → échec ; une ligne de la docstring changée hors de l'en-tête → échec ; une autre liste de chemins changée → échec ; la ligne 1 d'en-tête retouchée → tenue (admise, comme déclaré).

`cloisonnement_bras_a_v14.violations_de_la_garde_statique(Path('.'))` sur le dépôt : `[]`. La même garde en version 13 : 25 violations, toutes dans les deux fichiers neufs.

## Essais

`tests/test_aire_conditionnelle_bras_a_v1.py`, 11 essais, **11 passés** :
- **de bout en bout** (cas sain) : l'enchaînement version 2 joue le constat, l'étape (m) réelle, verse, puis lance **le vrai programme** ; code 0, une seule ligne JSON aux vingt aires et vingt clés, les trois couples (moniteur, dose) fabriqués calculés et eux seuls, la ligne égale au fichier scellé des grandeurs écrit par l'analyse, quatre versements. Livraison **fabriquée** par l'aide des essais (`aide_bras_a_v13`, sortie, configuration et constat), fichier des rangs fabriqué par l'essai, **entropie fictive déclarée telle** (`ENTROPIE_FICTIVE = 20261122`), tâches et comptes inventés. Les sorties synthétiques de l'épreuve de forme v11 ne sont pas employées : elles sont rangées sous `docs/notes/bras-a-sans-interne-v1/`, que cette relance n'ouvre pas, et leur fichier des rangs n'est pas connu ;
- **arrêt, code 3** (artefact) : un moniteur hors des cinq dans le fichier — arrêt consigné à l'étape (n), relevé et versé par l'enchaînement, aucune ligne rendue, aucun fichier des grandeurs ;
- **programme d'une autre empreinte** (artefact) : copie retouchée inscrite à l'empreinte du vrai — refusée par l'enchaînement avant tout constat ;
- **analyse à l'empreinte altérée, ou absente** (artefacts, sur une copie de trois fichiers nommés dans un dossier temporaire) : code 4, une ligne, la marque que l'analyse retouchée poserait à l'import n'existe pas ; cas sain : l'analyse du dépôt passe l'empreinte et sa propre garde arrête sur des pièces absentes ;
- **entrée standard hors de sa forme** (six artefacts) : code 4 ;
- **garde statique version 14** : programme admis par son chemin, compagnons vérifiés, le même texte hors de la liste refusé, `[]` sur le dépôt.

`python -m pytest -q tests/test_aire_conditionnelle_bras_a_v1.py tests/test_enchainement_discretion_bras_a_v2.py` : **100 passés, 1 en échec** — `test_d1_la_commande_citee_est_le_vrai_module_par_la_commande_reelle` (enchaînement version 2) : sa commande réelle passe la garde **version 13** sur le dépôt, qui refuse maintenant les deux fichiers neufs (code 4 au lieu du code 5 attendu). C'est la réserve 1, attendue. Les essais « garde passée sur le dépôt » des gardes versions 6 à 13 : voir réserve 2.

## Réserves

1. **L'enchaînement version 2 ne peut plus jouer sa commande réelle sur ce dépôt** : il importe `cloisonnement_bras_a_v13`, qui refuse tout programme sous `src/` nommant la lecture du fichier des rangs — par construction, ce programme. Il faut un enchaînement version 3 qui n'en diffère que par l'import de la garde version 14 (et qui ajoute ce programme à ses programmes joués). Non fait : hors de la consigne.
2. Les essais des gardes versions 6 à 13 qui passent la garde sur le dépôt réel échouent désormais pour la même raison (leurs listes ne connaissent pas les fichiers neufs) : `pytest -k depot` sur les essais des gardes versions 6 à 13 — **8 en échec**, un par version (`test_la_garde_passee_sur_src_et_scripts_du_depot…`), 455 non retenus. Attendu ; à trancher par la session mère (marquer ces essais comme liés à leur version, ou les borner à l'arbre de leur commit).
3. Seule l'analyse est vérifiée à son empreinte par le programme ; les modules de la version 12 qu'elle importe ne le sont pas ici (l'enchaînement relève leurs empreintes). Entre la vérification et l'import, un fichier remis à l'identique entre-temps échapperait à la seconde empreinte.
4. Le compagnon `.sha256` du programme a été refait une fois avant tout commit (le texte avait changé : import direct au lieu d'un import par nom) ; la première empreinte (`81083eed…`) n'a jamais quitté l'arbre de travail.
