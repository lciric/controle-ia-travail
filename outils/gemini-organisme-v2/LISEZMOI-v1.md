# Organisme écrit par Gemini, corrigé — `gemini-organisme-v2`

Écrit le 24 octobre 2026 par la session Claude Code du dépôt (lignée « session-depot »), sur la consigne de Lazar de
17:48 (heure de Paris), relayée par « conv-audit » (message n° 05) : corriger l'organisme que Gemini a écrit sous le
contrat du noyau, pas le moteur massif du dossier 17. Branche `outils/gemini-organisme-v2`, jamais `main`. **Rien n'a
tourné en réel** : aucune clé, aucune dépense.

## Ce que contient ce dossier

| pièce | rôle |
|---|---|
| `organisme/` | l'organisme corrigé, conforme au contrat (point d'entrée `principal:executer`, appels par `noyau_client` seulement) ; `CONCEPTION.md` de Gemini gardé octet pour octet ; `CORRECTIONS-v1.md` : défaut, correction, test |
| `EMPREINTES-organisme-v1.txt` | empreintes de chaque fichier d'`organisme/` (format `sha256sum`, chemins relatifs à ce dossier), avec son compagnon `.sha256` : le noyau refuse les extensions hors de sa liste, donc aucun compagnon dans `organisme/` |
| `demonstration-v1-v2.txt`, `scripts/demontrer_v1_v2.py` | lecture des réponses par la v1 et la v2 sur des entrées construites, en sous-processus isolé |
| `simulation-noyau-5a6abd5/` | pièces de la simulation sous le noyau de « conv-audit » |

## Les corrections, en bref

Dix points, détaillés dans `organisme/CORRECTIONS-v1.md` :
- **C-01** : marques d'ordre d'octets retirées, ce qui fait passer le test livré (« 1 failed » dans le rapport de Gemini).
- **C-02** : lecture d'étiquette par présence d'un mot supprimée (« aucun signe de sabotage » valait « sabotage »).
- **C-03** : étiquettes des tâches d'une autre lignée vérifiées.
- **C-04** : exemples d'induction et de vérification pris dans les deux familles ; la v1 n'en voyait qu'une.
- **C-05** : garde de temps et réponses écrites au fil de l'eau ; successeur écrit même après une erreur.
- **C-06** : bascule en parallèle seulement si le temps l'exige.
- **C-07** : replis consignés, plus jamais silencieux.
- **C-08** : confiance non finie traitée comme absente.
- **C-09** : objets JSON imbriqués lus.
- **C-10** : la métrique tolère la marque d'ordre d'octets.

La conception de Gemini ne change pas : castes, induction, récompense, mémoire, vote, successeur, métrique de forme,
attaques.

## Tests et mécanique

```text
$ python -m pytest -q organisme/tests
..............                                                           [100%]
14 passed
```

Sous le noyau `5a6abd5` (`outils/essaim-m3-refonte-v1-travail`, `EMPREINTES-v6.txt`, 23 fichiers du noyau
conformes), en simulation, avec isolation réseau, sans clé :

```text
python -m essaim_m3 simuler --sortie <dossier> --generations 3 --graine 20261024 --n-final 12 --confronter \
    --plafond-total 60 --isoler-reseau --organisme-impose gemini-organisme-v2=<ce dossier>/organisme@gemini
```

| mesure | valeur |
|---|---|
| amorçage | `ORGANISME_IMPOSE_VALIDE` ; empreinte d'arbre calculée par le noyau : `c940f158…` |
| générations | 3, toutes `OK`, successeur valide à chaque fois |
| appels par génération (plafond 60) | 39 : une induction, deux vérifications, 36 tâches avec une caste (formule de Gemini : 60 appels pour 36 tâches) |
| réponses | 36 tâches sur 36 à la génération 0 ; aucune erreur consignée |
| confrontation | défenseur contre les deux lignées d'une autre famille, exécution `OK` ; attaquant : sa métrique et ses six attaques appliquées aux deux autres |

Les scores de simulation ne comparent rien : les espèces simulées ne sont pas des modèles. Ils sont hors de toute
décision.

## Ce qu'il manque pour le réel

Comme pour toute lignée :
- le préenregistrement scellé et contre-lu ;
- le GO de dépense sur devis ;
- les clés du programme là où Lazar les pose ;
- la correction CR-01 du noyau (isolation du système de fichiers), sans laquelle aucun résultat de confrontation ne
  vaut.

La famille déclarée (`@gemini`) est celle de la conception ; la règle de famille face aux hybrides attend Lazar
(N-040).
