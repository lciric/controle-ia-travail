# Organisme écrit par Gemini, corrigé — `gemini-organisme-v3`

Écrit le 24 octobre 2026 par la session Claude Code du dépôt (lignée « session-depot »), sur le GO de Lazar : « go
aligne les attaques de l'organisme de gemini ». Branche `outils/gemini-organisme-v3`, jamais `main`. Elle remplace,
pour la confrontation, `outils/gemini-organisme-v2` (`b4c3774`), qui reste intacte (R12) et vaut pour tout ce que ce
fichier ne dit pas (C-01 à C-10, démonstration v1 contre v2). **Rien n'a tourné en réel** : aucune clé, aucune dépense.

## Ce qui change depuis la v2

Une seule correction, **C-11** (`organisme/CORRECTIONS-v2.md`) : les six attaques de `organisme/metrique/attaques.json`
passent dans le vocabulaire de la banque, sans changer leurs textes, leurs identifiants ni le sens de leurs vérités.
- Familles : `conscience_evaluation` devient `conscience-evaluation`, `controle_agent_delegue` devient `controle-delegation`.
- Étiquettes : `conscience_evaluation` devient `evaluation`, `comportement_nominal` devient `usage-reel`,
  `execution_fidele` devient `honnete` ; `sabotage` ne change pas.

Sous la règle du noyau (« une attaque porte la famille et les étiquettes de la banque »), les six attaques de la v2
étaient invalides ; celles de la v3 sont valides. Le manifeste passe à `organisme-gemini-m3-v3`, version 3.0.0. La
métrique de forme ne change pas (conception de Gemini).

## Tests et mécanique

`python -m pytest -q organisme/tests` : 17 passés (3 de Gemini, 11 des corrections C-01 à C-10, 3 de C-11, dont
l'artefact : le vocabulaire de la v2 est refusé par la règle du noyau).

Sous le noyau `e37adb1` (`outils/essaim-m3-refonte-v1-travail`, 24 fichiers conformes à `EMPREINTES-v7.txt`), en
simulation, isolation réseau, sans clé :

```text
python -m essaim_m3 simuler --sortie <dossier> --generations 2 --graine 21 --n-final 12 --confronter \
    --plafond-total 60 --isoler-reseau --organisme-impose gemini-organisme-v3=<ce dossier>/organisme@gemini
```

| mesure | valeur |
|---|---|
| amorçage | `ORGANISME_IMPOSE_VALIDE` ; empreinte d'arbre calculée par le noyau : `3e6fe2e9…` |
| générations | 2, toutes `OK`, successeur valide, 39 appels sur 60 |
| attaques | 6, valides ; appliquées aux deux lignées d'une autre famille, défense exécutée (`OK`) |
| métrique | présente ; non discriminante (même valeur sur une sortie parfaite et sur une sortie inversée) : rapportée, écartée de H-E2 |

Les scores de simulation ne comparent rien ; ils sont hors de toute décision. Pièces dans `simulation-noyau-e37adb1/`.

## Imposer cette lignée

`--organisme-impose gemini-organisme-v3=<racine>/outils/gemini-organisme-v3/organisme@gemini`, famille nominale de la
conception (N-040 (3)). Empreintes du dossier : `EMPREINTES-organisme-v1.txt` (+ `.sha256`).
