# Organisme écrit par Gemini, v5.2 — `gemini-organisme-v5-2`

Reçu le 25 octobre 2026 à 12:52 (heure de Paris, UTC+1) de Lazar, en une seule pièce : l'analyse de Gemini, ses
décisions de conception, son script PowerShell et son message (`livraison/recu-gemini-v5-2-v1.txt`, 133 714 octets,
`b06ada665cfe24b06444f211105015d3e8bd55047d1d0519e02fa404911876bc`). C'est la réponse à
`DEMANDE-v5-2-faits-moisson-v2.md` (zip `a0dadd85…`, remis à Lazar à 12:23 Paris ; faits sur la moisson servie par le
noyau et sur ce que la v5.1 en faisait ; **aucune valeur suggérée**). Rangé par la lignée « conv-audit » vers 12:00 UTC
sur la branche `outils/gemini-organisme-v5-2`, tirée de `outils/gemini-organisme-v5-1` (`7f9cd2e`), jamais `main`.
**Rien n'a tourné en réel** : aucune clé, aucune dépense.

**Verdict : la v5.2 est l'objet candidat du second pilote** (décision de Lazar, 12:20 Paris : « v5.2 d'abord ») ; 28 de
ses 29 essais passent en isolation ; le 29e, écrit par Gemini, échoue sur sa dernière assertion par un défaut de l'essai
(voir Réserves) ; reproductible d'un processus à l'autre ; vérifiée sous le noyau par les cas sains du lanceur du pilote
(pièces du préenregistrement).

## Comment les fichiers ont été obtenus

Le script n'a **pas été exécuté**. `livraison/extraire_herestrings.py` (le même outil, octet pour octet, que pour les v4,
v5 et v5.1 : `21e9489b…`) a écrit les quatre fichiers du script (`manifeste.json`, `principal.py`, `CONCEPTION.md`,
`tests/test_moissonneur_v5.py`) ; les quinze autres sont ceux de la v5.1 (arbre `50ffcd7d…`), que Gemini dit conservés
« octet pour octet » — vérifié par empreintes. Empreintes : `EMPREINTES-organisme-v1.txt`. Empreinte d'arbre de
`organisme/` (`boucle.empreinte_arbre`, celle que le noyau consigne au manifeste) :
**`4fcdc7db518bf3659eabd90f03ae8ddbf003ea5b4966c850657e917efef30125`** (19 fichiers).

## Ce qui change depuis la v5.1 (vérifié fichier par fichier, pas d'après le message)

| fichier | état |
|---|---|
| 15 fichiers (`__init__.py`, `memoire_isvd.py`, `mitose_spectrale.py`, `CORRECTIONS-v1/2/3.md`, `metrique/` (4), `tests/test_organisme.py`, `test_corrections_v1/2/3.py`, `test_question_ouverte_v4.py`) | inchangés (empreintes égales) |
| `manifeste.json` | nom `organisme-gemini-m3-v5-2`, version `5.2.0`, description |
| `principal.py` (1 557 → 1 697 lignes ; diff `verification-v1/diff-principal-v51-v52.txt`) | `VERSION` ; `RESULTATS_MAX_PAR_RECHERCHE` 5 → **10** ; `RECHERCHES_MAX_PAR_MOISSON` **6** ; `TELECHARGEMENTS_MAX_PAR_MOISSON` **3** ; `MAX_CARACTERES_EXTRAIT_DOC` **2 400** ; `_extraire_passages_denses_document` (début + zone dense ou médiane) ; `_charger_corpus_archive` (lit `travail/corpus/` de la vue d'archive) ; `_enregistrer_telechargement` lit `fichier_texte` quand `tronque` ou texte vide (jusqu'à 120 000 caractères), C-12 gardée (0 appel imbriqué sous `_VERROU`, vérifié par l'outil) ; `_executer_moisson` : six requêtes de réserve couvrant les quatre sources, jusqu'à 6 recherches et 3 téléchargements, 12 notices (résumés jusqu'à 1 100 caractères), extraits jusqu'à 2 400 ; à g0, le corpus entre dans l'induction **et** dans un bloc dédié des consignes de tâche (plus coupé par `regles_apprises[:600]`) ; plafonds de sortie inchangés (16 384 / 24 576 / 8 192, rabattus au `max_tokens_appel` du noyau) |
| `CONCEPTION.md` | § 2.10 ajouté |
| `tests/test_moissonneur_v5.py` | deux essais ajoutés (28 → voir Réserves) |

Nombres de Gemini : tous les siens. Primitives appelées : `especes`, `budget`, `appeler`, `rechercher`, `telecharger` ;
mêmes importations que la v5.1 (`json, math, re, shutil, threading, time, unicodedata, concurrent.futures, pathlib`) ;
aucun accès réseau, sous-processus ni variable d'environnement (recherche de motifs, pas de preuve). Lectures de
fichiers : `fichier_texte` rendu par le noyau, `travail/corpus/` de la vue d'archive, sa propre mémoire — tous dans ce que
le contrat lui ouvre.

## Essais et mécanique (`verification-v1/`)

Toutes les exécutions : utilisateur `nobody`, réseau coupé (`unshare -n`), environnement vide, `python -I -B`, copie à
part.
- **28 essais passés, 1 en échec** (`tests-isolation-v52-v1.log`, 4,5 s) : les 27 de la v5.1 et
  `test_v5_2_lecture_corpus_archive_generations_precedentes` passent ;
  `test_v5_2_exploitation_4_sources_dont_web_6_recherches_3_telechargements_et_extraits_riches` passe toutes ses
  assertions mécaniques (6 recherches sur les 4 sources avec `n` = 10, 3 téléchargements, `fichier_texte` lu, repère
  documentaire présent dans la consigne de tâche) et **échoue sur la dernière** : le marqueur de fin de document n'est
  pas dans la mémoire spectrale, parce que le code de Gemini n'y garde que les 420 premiers caractères de l'extrait
  (`principal.py`, l. 768 : `extrait_doc[:420]`) alors que l'extrait garde la fin du document (vérifié : le marqueur
  est dans l'extrait, à sa fin). Défaut de l'essai, ou intention non réalisée : rien n'est corrigé par nous, consigné.
- **Reproductibilité** : sous le faux noyau déterministe (cas B : tâches et question, moisson fermée ; cas D : moisson
  ouverte, 2 recherches, 1 téléchargement), les relevés complets (appels, recherches, téléchargements, fichiers, hors
  durées) sont **identiques** pour les graines de hachage 0, 1 et 2 (`v52-B-h*.json`, `v52-D-h*.json`) : cas D, 29 appels,
  2 recherches, 1 téléchargement.
- **Verrou** : `verrous-imbriques-v52-v1.log` — 0 appel imbriqué.
- **Sous le noyau** (`5d1d4fd` + R-410, commit `b1c7f4b6`) : cas sains des essais du lanceur du second pilote
  (`prereg/pieces-pilote2-gemini-v5-2/simulation-lanceur-v1/` sur la branche du pilote).

## Réserves

1. L'essai en échec ci-dessus : à dire à Gemini (par Lazar) pour une v5.2.1 ; sans effet sur la mécanique de la course.
2. Le message de Gemini dit « 29 passed » : non reproduit ici (28).
3. Lecture de `fichier_texte` jusqu'à 120 000 caractères et de `travail/corpus/` : plus de texte entre dans les consignes
   (jusqu'à 12 notices de 1 100 caractères et 3 extraits de 2 400 par moisson, plus le corpus d'archive) ; l'effet sur
   le coût d'entrée se mesure au pilote.

## Imposer cette lignée

`--organisme-impose gemini-organisme-v5-2=<racine>/outils/gemini-organisme-v5-2/organisme@gemini`, sous un
préenregistrement et un GO qui la nomment, avec `--recherches-max`, `--telechargements-max` non nuls et les quatre sources.
