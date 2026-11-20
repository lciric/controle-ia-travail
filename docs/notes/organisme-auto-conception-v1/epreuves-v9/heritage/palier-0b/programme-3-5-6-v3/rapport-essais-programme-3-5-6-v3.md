# Rapport des essais v3 du programme des étapes 3 à 6 (programme v2 inchangé) — v1

**EN ATTENTE DU MOT DE LAZAR.** Pièce de travail (classe C). Développeur, modèle O, 2026-11-20. Rien n'est lancé en vrai, aucune graine décisive, aucune écriture dans le dépôt, aucun commit.

- Vérification de la v2 : `P0B/verification-programme-3-5-6-v2-v1.md` (`beeaf621ff128f7956206c586019c70034531eeadb58cf2ea107fca3df469a43`, contrôlée contre son compagnon). Verdict « À corriger », point 3 : le retour de `lancer` n'était plus éprouvé ; une permutation (chemin, empreinte) → (empreinte, chemin) passait les essais.
- **Le programme reste la v2, inchangé** : `lancer_etapes_3_5_6_v2.py`, `1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`. L'empreinte a été recalculée sur le fichier versé `P0B/programme-3-5-6-v2/` et sur ma copie du bloc-notes : égales. Les essais chargent ma copie et contrôlent son empreinte à l'import. Le fichier n'est pas recopié dans `programme-3-5-6-v3/`.

## 1. Ce qui change (essais seulement ; `differentiel-essais-v2-v3.diff`)

- **Chargement.** Le programme v2 est chargé par son chemin (`../../programme-3-5-6-v2/lancer_etapes_3_5_6_v2.py`), et son empreinte est exigée égale à `1f04cb46…`. Pour la seule preuve du mutant, la variable `PROGRAMME_3_5_6_MUTANT` fait charger une autre copie, sans contrôle d'empreinte.
- **`test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue`** appelle désormais `_verifier_le_retour(r)`. Il y vérifie que :
  - `r["frequences"]` et `r["reglages"]` sont des couples (chemin, empreinte) ;
  - le chemin est celui du fichier gelé de son étape (`etape-5/frequences-m12-v1.json`, `etape-6/reglages-v1.json`), et il existe ;
  - l'empreinte est égale au SHA-256 du fichier et à son compagnon ;
  - `r["manifestes"]` a exactement les clés 3 à 6, chacune égale à l'empreinte du `manifeste.json` de son étape.
- **`test_v3_main_imprime_le_retour_de_lancer`** (neuf) : `main` est joué sur le cas sain planté. Ses lignes imprimées sont relues (« étape N : manifeste EMPREINTE », « fréquences gelées : CHEMIN EMPREINTE », « réglages gelés : CHEMIN EMPREINTE ») et soumises aux mêmes contrôles que le retour. `main` appelle `lancer` sans couche : le temps de l'essai, `lancer` est donc remplacé par lui-même, sous « essai-de-forme » et aux tailles réduites, pour ne dériver aucune graine d'une couche des étapes.
- **`test_v3_arret_au_point_5_aucun_retour_ni_gele_imprime`** (neuf). Sur l'arrêt au point 5 (planté) :
  - `main` (comme `lancer`) s'arrête sans rien rendre et n'imprime rien ;
  - seuls les manifestes sur disque portent les empreintes : l'étape 6 avec l'issue « arrêt », les fréquences à l'étape 5.
- Le reste du fichier est celui des essais v2, à l'octet hors du docstring de tête, du chargement et de ces ajouts.

**Écart à la demande.** La demande voulait une sortie de `main` qui « se relise en JSON ». Or le programme v2, qui ne doit pas changer, imprime des lignes « nom : valeurs », non du JSON. L'essai relit donc cette forme ligne à ligne, et toute ligne hors de cette forme le fait échouer. Une sortie JSON demanderait un programme v3 : rien n'en a été écrit.

## 2. Preuve par défaut planté

- **Mutant.** Le mutant est une copie du programme v2 dans un dossier jetable du bloc-notes (`mutant-v3/`), mutée par `sed`. Une seule ligne change, l. 240 : `"frequences": (chemin_f, sha_f), "reglages": (chemin_r, sha_r)` devient `"frequences": (sha_f, chemin_f), "reglages": (sha_r, chemin_r)` (`diff` : un seul hunk).
- **Résultat.** Fichier d'essais v3 joué entier contre le mutant (`PROGRAMME_3_5_6_MUTANT`) : **2 échoués, 29 passés**. Les deux échecs sont les essais neufs ou renforcés :
  - `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue` (assertion du retour : le premier membre est une empreinte, non le chemin du fichier) ;
  - `test_v3_main_imprime_le_retour_de_lancer` (même assertion sur la sortie de `main`).

  Les 29 autres passent, ce qui reproduit le constat du vérificateur. Journal : `essais-v3-mutant.log`.
- **Nettoyage.** La copie mutée a ensuite été supprimée (`rm -r mutant-v3`). Le programme v2 a été recontrôlé après : `1f04cb46…`.

## 3. Essais

```
env -C <bloc-notes>/dev-palier-0b-v6/code-v6 PYTHONPATH=src HERITAGE_DEPOT=/home/user/controle-ia-travail HERITAGE_COPIE_ORGANISME=<bloc-notes>/dev-palier-0b-v6/code-organisme-94bfd92/orchestrator /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider <bloc-notes>/dev-palier-0b-v6/programme-3-5-6-v3/tests/test_lancer_etapes_3_5_6_v3.py <bloc-notes>/dev-palier-0b-v6/code-v6/tests/test_heritage_etage_processeur_v1_zz_aucune_graine_decisive.py
```

Les essais ont tourné en tâche de fond, sur la copie du code v6 égale à la table `639335b9…`. **32 passés, 0 échoué** (835 s ; journal `essais-v3.log`) : les 31 essais du fichier (29 de la v2 et 2 neufs) et l'essai final « aucune graine décisive » du code v6. Seule la couche « essai-de-forme » a été dérivée.

Aucune chaîne réduite n'a été cherchée pour finir « tenue » par un autre réglage. L'essai de la chaîne garde la forme de la v2 : « tenue », ou arrêt par la seule cause du point 5.

## 4. Fichiers (sous-dossier `programme-3-5-6-v3/`, chacun avec son compagnon)

`tests/test_lancer_etapes_3_5_6_v3.py` (`cf1608c3f6aff89534076c2f21c8db0ed9b0060deaee4d49f4e8a49c85ab0fb7`), `differentiel-essais-v2-v3.diff`, `essais-v3.log`, `essais-v3-mutant.log`, ce rapport, `table-empreintes-programme-3-5-6-v3.txt`.

## 5. Écarts

- La sortie de `main` est relue dans sa forme réelle, non en JSON (§ 1).
- Les deux variables d'environnement des essais, comme avant.
- Une copie mutée a été créée puis supprimée dans le bloc-notes.
- Aucune commande de liste ni de recherche de processus ; aucune commande d'arrêt ; aucun refus de permission, de classifieur ni de garde.

Développeur, modèle O.
