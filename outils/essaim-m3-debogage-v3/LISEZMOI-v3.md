# Essaim de Gemini, version déboguée, enveloppe v3 sous le contrat du noyau

Écrit le 24 octobre 2026 par la session Claude Code du dépôt (lignée « session-depot »), sur le GO de Lazar reçu à
15:21 UTC : « go pour l'enveloppe et la confrontation des deux essaims ». Branche `outils/essaim-m3-debogage-v3`,
jamais `main`. La v2 reste intacte (`outils/essaim-m3-debogage-v2`, `44bebdd`, avec son `LISEZMOI-v2.md`), comme la
v1 (`fe56b03`) ; ce fichier vaut pour ce qui change, les deux autres pour le reste. **Rien n'a tourné en réel** :
aucune clé, aucune dépense.

Pour la confrontation, c'est **ce dossier `organisme/`** qu'il faut imposer au noyau, pas celui de la v2.

## 1. Pourquoi une v3 : la v2 branchée sur le noyau `556a8e3`

Le noyau de « conv-audit » accepte depuis `556a8e3` un organisme fourni (`--organisme-impose NOM=CHEMIN@FAMILLE`).
L'enveloppe v2 s'y branche sans adaptateur ; la simulation a montré deux défauts, corrigés ici.

| n° | v2 | v3 |
|---|---|---|
| V3-01 | plancher de l'arrêt spectral retiré : sous les espèces simulées, la mitose s'arrête après la première vague (gain 0,28 par cellule) ; 34 appels sur 60 par génération | plancher transposé du moteur (l. 628 : critère consulté au-delà de 125 cellules, plafond de 220) : le critère n'est consulté qu'une fois dépensés 125/220 des appels de l'étage M3 ; 59 appels sur 60 |
| V3-02 | six appels en parallèle | huit, le plafond du noyau ; le moteur lançait chaque vague en parallèle (l. 596). Sans cela, avec des appels réels de l'ordre de la minute, la garde de temps couperait l'exploration |
| V3-03 | lots d'étiquetage l'un après l'autre ; un lot en échec ou illisible perd ses 8 réponses | lots en parallèle, puis une reprise des tâches restées sans réponse valide, par lots plus petits, dans le budget restant, sans toucher aux appels de la métrique ni à la marge de sa boucle d'écriture |
| V3-04 | étiquette rendue en minuscules ; lot d'une tâche lu seulement au format des lots | étiquette rendue sous la forme de la tâche (les attaques d'une autre lignée arrivent avec leurs propres étiquettes) ; un objet `{etiquette, confiance}` est lu pour un lot d'une tâche ; confiance finie et bornée ; jamais de lecture par présence d'un mot |
| V3-05 | la v2 citait les lignes 616 et 613-618 du moteur pour le critère d'arrêt | ligne 628 (l. 618-630) ; erreur de la v2, corrigée dans le code et dans `CONCEPTION.md` |

Rien d'autre ne change : `m3_commun.py`, le greffon de mémoire, l'adaptateur, le substrat et les trois scripts sont
ceux de la v2, mêmes empreintes.

## 2. Tests

```text
$ python -m pytest -q tests
..........................................                               [100%]
42 passed in 8.58s
```

Quatre tests nouveaux, chaque garde sur un cas sain et sur un artefact (R5) : la règle du plancher (sous le plancher,
jamais d'arrêt ; au-delà, les seuils du moteur) ; la mitose avec des contributions identiques (gain nul dès la
première vague) qui ne s'arrête qu'au plancher ; un lot d'étiquetage en échec repris en entier, la métrique gardant
ses appels ; la lecture des étiquettes (forme de la tâche, étiquette hors tâche refusée, objet seul, confiance bornée,
aucune lecture par présence d'un mot).

## 3. Sous le noyau `556a8e3`, en simulation, sans réseau ni clé

Noyau extrait de `outils/essaim-m3-refonte-v1-travail` (`556a8e3`), 21 fichiers vérifiés sur `EMPREINTES-v4.txt`, sans
l'organisme écrit par Gemini (`organismes/gemini-organisme-v1/`, code de la relève : jamais exécuté ici).

```text
python -m essaim_m3 simuler --sortie <dossier> --generations 3 --graine 20261024 --n-final 12 --confronter \
    --plafond-total 60 --organisme-impose gemini-corrige-v3=<ce dossier>/organisme@gemini
```

| mesure | v2 | v3 |
|---|---|---|
| amorçage | `ORGANISME_IMPOSE_VALIDE` | `ORGANISME_IMPOSE_VALIDE` |
| générations | 3, toutes `OK`, successeur valide | 3, toutes `OK`, successeur valide |
| appels par génération (plafond 60) | 34 | 59 |
| mitose | arrêt spectral après la vague 1 (13 appels) | arrêt spectral après la vague 2 (36 appels, plancher 21) |
| reprise de l'étiquetage | — | lancée, dans la réserve de la métrique |
| métrique | deux écritures, refusées par la garde | deux écritures, refusées par la garde |
| réponses aux tâches | 0 | 0 |
| confrontation | défenseur contre deux lignées d'une autre famille, exécution `OK` ; attaquant : non applicable, faute de métrique | idem |

Les zéros sont des limites du simulateur, pas de l'enveloppe : les espèces simulées répondent à une tâche par
consigne (une étiquette pour la famille citée en dernier) ; elles ne répondent ni à un lot de huit tâches au format
`{"reponses": {…}}`, ni à la question de la métrique au format des fichiers. Proposé à « conv-audit » : une lecture
générique des lots dans le simulateur (plusieurs `[id] (famille : … ; étiquettes possibles : […])` → un objet
`{"reponses": …}`). Sans elle, **la simulation teste la mécanique et ne compare pas les conceptions** ; tout score
simulé est hors de toute décision.

Pièces de ce run dans `simulation-noyau-556a8e3/` : `manifeste-run.json` (début 16:01:48 UTC ; empreinte d'arbre de
l'organisme imposé, calculée par le noyau sur `organisme/` sans les compagnons `.sha256` : `c2d48b97…`),
`rapport-v1.json` (`f0d4c0f4…`, scellé par le noyau), `confrontation-v1.json` (`57bd122e…`, scellé par le noyau),
`evenements.jsonl`, `archive-index.jsonl`, `trace-etapes-gemini-corrige-v3-g000.json`.

## 4. Ce qu'il manque pour la confrontation réelle

1. ~~Un organisme fourni ne tourne qu'en simulation~~ : réglé par `--organisme-impose` (`556a8e3`).
2. **La règle des familles.** Le noyau n'applique la métrique de A à B que si leurs familles de fournisseur
   diffèrent. Déclarée `gemini` (la conception est celle de Gemini), cette enveloppe ne se confronte ni à la lignée
   `gemini-argon` ni à l'organisme écrit par Gemini ; elle se confronte aux lignées écrites par Fable et par Opus. Si
   la confrontation voulue est « l'essaim de Gemini corrigé contre l'organisme de conv-audit », la famille de chaque
   lignée doit être fixée dans le préenregistrement, par Lazar.
3. **Le temps.** Avec `temps_max_s` à 600 et des appels réels de l'ordre de la minute, l'exploration (55 % du temps)
   tiendra deux ou trois vagues ; le budget d'appels ne sera pas la borne. À geler dans le préenregistrement, le même
   pour toutes les lignées ; proposition : 1 200 s.
4. **Le préenregistrement**, contre-lu par un relecteur neuf (R2), scellé, tâches réelles gelées avant l'amorçage.
5. **Les clés du programme** là où Lazar les pose (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, jamais `RR_*`), et **le GO de
   dépense sur devis** (brouillon : environ 4 USD de répétition générale, 85 USD en version réduite, 250 USD en
   version complète).
