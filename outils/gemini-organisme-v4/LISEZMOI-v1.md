# Organisme écrit par Gemini, v4 (question ouverte) — `gemini-organisme-v4`

Reçu le 25 octobre 2026 à 00:44 (heure de Paris) de Lazar, qui relaie Gemini : un script PowerShell qui écrit les 16
fichiers de `organisme/` sur sa machine, et le message de relais de Gemini (`livraison/`). Rangé par la lignée
« conv-audit » le 24 octobre 2026, 22:49 UTC, sur la branche `outils/gemini-organisme-v4`, jamais `main`. La v3
(`outils/gemini-organisme-v3`, `320cd34`, arbre `3e6fe2e9…`) reste intacte (R12) : **le pilote préenregistré tourne sur
la v3**, décision de Lazar du 24 octobre, 23:52 (Paris). **Rien n'a tourné en réel** : aucune clé, aucune dépense.

## Comment les fichiers ont été obtenus

Le script n'a **pas été exécuté**. `livraison/extraire_herestrings.py` lit les blocs `Write-Utf8NoBomLf "$org\…" @' … '@`
et écrit chaque fichier tel que le script l'aurait écrit (UTF-8 sans marque d'ordre d'octets, fins de ligne LF, sans
fin de ligne finale : un bloc `@'…'@` de PowerShell ne contient ni la fin de ligne qui suit `@'` ni celle qui précède
`'@`). Réextraction vérifiée identique. Empreintes des deux pièces reçues : `livraison/EMPREINTES-livraison-v1.txt`.
Empreinte d'arbre de `organisme/` (`boucle.empreinte_arbre`, celle que le noyau consigne au manifeste) :
`c5ada33581fd7675f2cec5331d9a9a50ff80271b543c22eef80a64882730c1b9` ; empreintes par fichier : `EMPREINTES-organisme-v1.txt`.

## Ce qui change depuis la v3 (vérifié fichier par fichier contre l'arbre `3e6fe2e9…`, pas d'après le message)

| fichier | état |
|---|---|
| `__init__.py`, `memoire_isvd.py`, `CORRECTIONS-v1.md`, `CORRECTIONS-v2.md`, `metrique/__init__.py`, `metrique/calculer.py`, `metrique/attaques.json`, `tests/test_organisme.py`, `tests/test_corrections_v1.py`, `tests/test_corrections_v2.py` | contenu identique à la v3 ; seule la fin de ligne finale manque (effet du script) — « octet pour octet » est donc faux d'un octet, le contenu est le même |
| `metrique/definition.md` | annoncé « intact » : contenu identique, marque d'ordre d'octets initiale (U+FEFF) de la v3 retirée, fin de ligne finale absente |
| `manifeste.json` | nom `organisme-gemini-m3-v4`, version `4.0.0`, description |
| `mitose_spectrale.py` | rien de la v3 retiré ; `planifier_castes_question_ouverte(especes, budget, historique)` ajoutée : 1 à 5 castes selon les appels restants et la pente des scores de `historique` — `monoculture_analytique`, `monoculture_croisee`, `sonde_orthogonale_onsager`, `critique_adversariale_limites`, puis `arbitre_synthese_contradictoire` |
| `principal.py` | rien de la v3 retiré (changent : la ligne d'import, `VERSION`, le `return` final qui ajoute `question_ouverte` au bilan) ; ajoutés `_parser_contribution_question_ouverte`, `_ecrire_reponse_question` (écriture atomique), `_traiter_question_ouverte` ; dans `executer`, **après** toutes les tâches de test, si `contexte["question_ouverte"]` est une chaîne non vide : délibération des castes (chacune reçoit la question, la mémoire spectrale, les règles induites, les positions des castes précédentes avec consigne d'orthogonalité), arbitrage, écriture de `reponse-question.md` (réponse finale ; raisonnement ; ce qui vient de quelle caste ; ce dont l'essaim n'est pas sûr ; bloc `--- ORGANISATION ---` : appels, castes, votes et poids, mémoire ayant servi) ; abstention écrite si tous les appels échouent ; les contributions entrent dans la mémoire du successeur ; dans le `finally`, un fichier minimal est garanti si une erreur a interrompu avant l'écriture. Sans question : flux v3, aucun fichier en plus |
| `CONCEPTION.md` | § 2.7 ajouté |
| `tests/test_question_ouverte_v4.py` | nouveau, 3 essais hors ligne (faux `noyau_client`) |

Primitives appelées : `noyau_client.especes`, `budget`, `appeler` seulement ; aucun import de réseau, de sous-processus
ni d'import dynamique dans `organisme/*.py` et `metrique/*.py` (vérifié par recherche de motifs, pas par preuve).
`max_tokens` demandés pour la question : 1 200 par caste, 1 500 pour l'arbitre.

## Tests et mécanique

- `pytest -q organisme/tests` : **20 passés** (17 de la v3 + 3), exécutés en isolation : utilisateur `nobody`, espace
  de noms réseau séparé (`unshare -n`), environnement vide, `python -I -B`, copie à part de l'arbre.
- Sous le noyau `5ab6ab7` (`outils/essaim-m3-gradient-v1-travail`, tête réunie, 110 tests), en simulation, isolation
  réseau, sans clé, graine 11, deux générations, 60 appels par génération, 24/8/8 tâches factices :
  amorçage `ORGANISME_IMPOSE_VALIDE` (empreinte d'arbre `c5ada335…` au manifeste), deux générations `OK`, successeur
  valide, 41 puis 36 appels, trois castes planifiées, aucune erreur consignée, aucun `reponse-question.md` (aucune
  question dans le contexte : le noyau n'a pas encore la primitive). Pièces : `simulation-noyau-5ab6ab7/` ; les scores
  de simulation ne comparent rien et sont hors de toute décision.

## Réserves

1. La primitive `question_ouverte` n'existe pas encore dans le noyau (spécifiée au canal, message n° 28 § 3) : la v4 ne
   peut répondre à aucune question avant qu'elle soit codée et essayée (cas sain et artefact).
2. La question est traitée après les tâches de test, dans les appels et le temps qui restent (avec 160 appels et 120
   tâches : ≈ 37 appels ; la garde interne des 75 % du temps peut couper la délibération) ; à mesurer, pas à corriger
   d'ici (la conception est celle de Gemini).
3. Les castes lisent le `score` de `historique` (pression d'exploration) : permis par le contrat (§ 2).
4. Les dires du message de relais sur l'identité « octet pour octet » et sur `definition.md` « intact » sont inexacts
   d'un octet ; sans effet sur le code.

## Imposer cette lignée

`--organisme-impose gemini-organisme-v4=<racine>/outils/gemini-organisme-v4/organisme@gemini` (famille nominale
`gemini`, N-040 (3)), seulement une fois la primitive codée, sous un préenregistrement et un GO qui la nomment.
