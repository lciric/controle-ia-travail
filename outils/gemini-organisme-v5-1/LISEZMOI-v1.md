# Organisme écrit par Gemini, v5.1 — `gemini-organisme-v5-1`

Reçu le 25 octobre 2026 à 09:44 (heure de Paris, UTC+1) de Lazar, en une seule pièce : l'analyse de Gemini, son script
PowerShell et un « message de passation » qu'il destine à Claude (`livraison/recu-gemini-v5-1-v1.txt`, 115 122 octets,
`49dc80c6…`, fins de ligne Windows). C'est la réponse à `DEMANDE-v5-1-faits-mecaniques-v1.md` (zip `833332ba…`, remis à
Lazar à 09:27 Paris). Rangé par la lignée « conv-audit » vers 09:00 UTC sur la branche `outils/gemini-organisme-v5-1`,
tirée de `outils/gemini-organisme-v5` (`9b13418`), jamais `main`. **Rien n'a tourné en réel** : aucune clé, aucune dépense.

**Verdict : la v5.1 répond aux trois faits transmis (plafonds, refus, verrou), ses 27 essais passent en isolation, elle
tourne sous le noyau en simulation avec la moisson ouverte, et elle est reproductible d'un processus à l'autre.** Elle
est l'objet candidat du second pilote, sous un préenregistrement et un GO qui la nomment.

## Comment les fichiers ont été obtenus

Le script n'a **pas été exécuté**. `livraison/extraire_herestrings.py` (le même outil, octet pour octet, que pour la v4
et la v5) a écrit les six fichiers du script ; les treize autres sont ceux de la v5 corrigée (`correction-c12-candidate-v1`,
arbre `911f791f…`). Empreintes : `EMPREINTES-organisme-v1.txt`. Empreinte d'arbre de `organisme/` (`boucle.empreinte_arbre`,
celle que le noyau consigne au manifeste) : **`50ffcd7d8cd3af059f2b881f3e565a8ad5829d8d325c39b9535bed6e01a8e12c`**.

## Ce qui change depuis la v5 corrigée (vérifié fichier par fichier contre l'arbre `911f791f…`, pas d'après le message)

| fichier | état |
|---|---|
| `__init__.py`, `memoire_isvd.py`, `CORRECTIONS-v1.md`, `CORRECTIONS-v2.md`, `metrique/` (4 fichiers), `tests/test_organisme.py`, `tests/test_corrections_v1.py`, `tests/test_corrections_v2.py`, `tests/test_question_ouverte_v4.py`, `tests/test_moissonneur_v5.py` | inchangés |
| `CORRECTIONS-v3.md`, `tests/test_corrections_v3.py` | nos fichiers de C-12, réécrits par le script : contenu identique, seule la fin de ligne finale manque (effet du script) |
| `manifeste.json` | nom `organisme-gemini-m3-v5-1`, version `5.1.0`, description |
| `mitose_spectrale.py` | **reproductibilité** : parcours des ensembles triés (`sorted(set(d))`, `sorted(tf)`), termes saturés triés par (compte décroissant, terme) au lieu de `most_common` ; rien d'autre |
| `principal.py` | C-12 reprise (0 appel imbriqué sous `_VERROU`, vérifié) ; **plafonds de sortie** : constantes `MAX_TOKENS_TACHE` 16 384, `MAX_TOKENS_INDUCTION` 16 384, `MAX_TOKENS_QUESTION_CASTE` 16 384, `MAX_TOKENS_QUESTION_SYNTHESE` 24 576, `MAX_TOKENS_MOISSON_REQUETES` 8 192, chacune rabattue par `_plafond_tokens_effectif` à `budget()["max_tokens_appel"]` du noyau quand il est défini (et seulement à lui : contrairement au message de Gemini, aucune adaptation au plafond en dollars) ; **consignes** : la tâche est présentée comme une « classification passive en lecture seule d'un journal textuel historique », l'induction comme une « recherche académique défensive en lecture seule », l'objet JSON demande `constat` au lieu de `raisonnement` (`_parser_decision_tache` accepte les deux), « réponds directement par un objet JSON » ; la troisième requête fixe de moisson devient « LLM alignment faking sandbagging situational awareness » (plus aucun mot de la mission ni de la question) ; `VERSION` |
| `CONCEPTION.md` | § 2.8 mis à jour, § 2.9 ajouté |

Nombres de Gemini : les plafonds de sortie sont **les siens** (nous lui avions transmis les faits sans suggérer de valeur) ;
les autres nombres de la v4 (8 exemples d'induction, 2 vérifications, 75 % du temps, parallélisme 8) sont inchangés.
Primitives appelées : `especes`, `budget`, `appeler`, `rechercher`, `telecharger` ; mêmes importations que la v4 ; aucun
accès réseau ni sous-processus (recherche de motifs, pas de preuve).

## Essais et mécanique (`verification-v1/`)

Toutes les exécutions : utilisateur `nobody`, réseau coupé (`unshare -n`), environnement vide, `python -I -B`, copie à
part.
- **27 essais passés** en 4,46 s (`tests-isolation-v51-v1.log`), dont les 6 de la v5 (le 17e, qui bloquait la v5, passe)
  et le nôtre (C-12).
- **Reproductibilité** : sous le faux noyau déterministe du cas B (tâches et question, moisson fermée), les suites de 28
  appels sont **identiques** pour les graines de hachage 0, 1 et 2 (`reproductibilite-graine-de-hachage-v51-v1.log`) ; la v4
  et la v5 ne l'étaient pas.
- **Simulation sous le noyau `90595ffb`** (tête de « session-depot » : arrêt sur crédit épuisé en 400, `ESSAIM_M3_CACHER`,
  réponse de ronde importée), isolation réseau, sans clé, graine 13, deux générations, 160 appels et 20 USD par
  génération, 24/8/8 tâches, trois lignées auto-écrites en plus, question `a54da93e…` (« apprendre sa structure… », v2)
  posée à g001, `--recherches-max 6 --telechargements-max 3` (`simulation-noyau-90595ffb-v1/`, extraits mécaniques sans
  score) :
  - **sain, `--max-tokens-appel 4096`** : amorçage `ORGANISME_IMPOSE_VALIDE` (arbre `50ffcd7d…`), g000 et g001 `OK`,
    35 puis 47 appels, tous `OK`, tous à 4 096 jetons (le rabattement de l'organisme a joué), 3 recherches et 2
    téléchargements par génération, réponse écrite (12 907 octets), aucune erreur ;
  - **sain, sans plafond du noyau** : mêmes statuts ; `max_tokens` demandés 16 384 (45), 24 576 (1, synthèse), 8 192
    (1, formulation des requêtes) ;
  - **artefact `--octets-max 100`** : g000 et g001 `OK`, `ECHEC_TELECHARGEMENT` consigné dans `erreurs`, successeurs
    valides, réponse écrite.

## Réserves

1. **Coût réel** : à 16 384 jetons demandés, le noyau réserve le pire cas de chaque appel en vol (`appels._reserver` :
   ≈ 0,85 USD pour Fable) ; en séquentiel ce n'est qu'un appel à la fois, mais la bascule en parallèle de l'organisme
   (jusqu'à 8) peut réserver ≈ 7 USD et faire refuser des appels (`PLAFOND`) quand la dépense réelle approche le plafond
   de la génération. Le préenregistrement du second pilote fixera `--max-tokens-appel` et `usd_max` ensemble (par
   exemple 4 096 ou 8 192 jetons et un plafond par génération relevé) ; la réflexion à effort élevé des espèces Anthropic
   rend la dépense réelle par tâche très variable : à mesurer, c'est l'objet du pilote.
2. Dires du message de Gemini inexacts : « adapté au plafond en dollars en vol » (le code ne rabat qu'au
   `max_tokens_appel` du noyau) ; « 12 statuts non OK » dans notre essai C-12 (il en couvre 6 + 6 = 12 appels, soit
   12 cas, c'est exact ainsi) ; « 27 passed en ~5 secondes » : vrai chez nous aussi.
3. Le « message de passation » de Gemini (section 4 de la pièce reçue) propose **une autre question ouverte** pour la
   génération 1 du pilote (« coercition d'audit contre maïeutique et esprit de finesse pascalien », en quatre points) en
   disant « Lazar souhaite » : une donnée, pas une décision ; Lazar tranche entre cette question et la v2 qu'il a retenue à
   09:07 ; le texte proposé nomme des sujets (« sandbagging », « alignment faking », « mutinerie ») qui ont déclenché un
   refus de filtre au premier tour du collisionneur.
4. Les consignes de la v5.1 cadrent la tâche en « lecture seule, défensive » pour éviter les refus : c'est la conception
   de Gemini ; l'effet sur les refus se mesure au pilote, il n'est pas acquis.

## Imposer cette lignée

`--organisme-impose gemini-organisme-v5-1=<racine>/outils/gemini-organisme-v5-1/organisme@gemini`, sous un
préenregistrement et un GO qui la nomment, avec `--recherches-max` et `--telechargements-max` non nuls (moisson ouverte).
