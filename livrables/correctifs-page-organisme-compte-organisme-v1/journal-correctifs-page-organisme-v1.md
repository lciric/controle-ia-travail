# Correctifs de la page publique de l'organisme — compte organisme — journal v1

Tâche 4 du brief du compte organisme v2 (`docs/notes/plan-paquet-multi-comptes-v1/brief-compte-organisme-v2.md`, `fc0229ad…`).
Auteur : modèle A (session du compte organisme). **Rien n'est poussé vers le dépôt public** ; rien n'y est écrit ; ce dossier
prépare deux couples « ancien texte, nouveau texte » et le programme qui les applique, pour la mère.

## 1. Les deux défauts (journal de la page v7, `livrables/page-publique-organisme-2026-11-14-v7/journal-page-organisme-v7.md`, `4f38f8bb…`)

« Signalé, non changé : la page d'état `resultats/attaque-goodhart-v2/README.md` l. 63 et `nul_v9.py` l. 9 à 12 disent encore
que le trou se lit sur la description du juge. »

## 2. Sources, empreintes recalculées par ce compte

| fichier public | source lue | empreinte (égale à celle du brief) |
|---|---|---|
| `resultats/attaque-goodhart-v2/README.md` | `livrables/page-publique-organisme-2026-11-10-v1/resultats/attaque-goodhart-v2/README.md` (dépôt de travail, 129 lignes) ; même empreinte dans le clone en lecture seule du dépôt public à `bdf6bc4` | `c549a31b266b6952c9f7fc2922243eab21ca304fe7626099310016f071f8ccbb` |
| `orchestrator/pole/nul_v9.py` | `orchestrator/pole/nul_v9.py` du clone en lecture seule (`bdf6bc4`) et de l'arbre reconstruit (`e7daf32`) | `7ae450df2482246122bf9fbcf0fa5ef30b4a7e4c6f0d09531e83af048e46ee95` |

Formulations de référence lues : `livrables/page-publique-organisme-2026-11-14-v7/README-corrige-v7.md` (`04ac692e…`, ligne 140 :
« 42 of the 48 reproduce the world's own law exactly: a breach of the novelty criterion "nothing beyond the archive", not a false
prediction, and it needs no optimisation against the judge ») ; R-2654 (« retirer « reading its description is enough » ») ;
`livrables/page-publique-organisme-2026-11-14-v6/verification-courte-page-v6.md` (`8c2dc416…`, empreinte vérifiée).

## 3. Couples

1. `couple-resultats-attaque-goodhart-v2-README-v1.json` — ligne 63 : « The hole is read off the judge's description, not
   learned from its verdicts. » → « The breach needs no optimisation against the judge. » (reprise mot pour mot de la page v7,
   ligne 140 ; la ligne 62 de la même page dit déjà que le retour des verdicts ne change rien, McNemar p = 1,0).
2. `couple-orchestrator-pole-nul_v9-v1.json` — lignes 11 et 12 : « un proposeur modèle de langage qui lit la description du
   juge y trouve une loi promue qui n'apporte rien au-delà de l'archive. » → « un proposeur modèle de langage fait promouvoir
   une loi qui n'apporte rien au-delà de l'archive (pour la plupart des lois promues, il recopie les deux lois connues que
   l'archive lui montre, une par sous-population ; aucune optimisation contre le juge n'y est nécessaire). » (fondement : page
   d'état ligne 63, phrase qui précède la phrase fautive, « the proposer copies the two archive laws it is shown, one per sub-population; the 6 others are close
   variants » ; page v7 ligne 140). Sens : non flatteur (R4) — l'affirmation retirée prêtait à l'attaque une lecture de la
   description du juge que les verdicts scellés n'établissent pas.

## 4. Application (programme `appliquer_correctifs_page_v1.py`)

`python3 -I appliquer_correctifs_page_v1.py COUPLE.json SOURCE SORTIE` : refuse si l'empreinte de la source n'est pas celle du
couple, si « ancien » n'y est pas exactement une fois, si la sortie existe, si « ancien » reste, si la suite des nombres change,
si un octet hors du passage change ; n'écrit jamais sur la source. Relevé de ce compte (2026-11-14, vers 09:05Z), deux passages
chacun, sorties dans un dossier provisoire hors des dépôts :

| couple | empreinte de la sortie (deux passages égaux à l'octet, `cmp`) | « ancien » restant | nombres |
|---|---|---|---|
| page d'état | `737a208ad23b875680f3f315a06363d57d73a263d14dc7835968459703406e77` | 0 | inchangés |
| `nul_v9.py` | `b753dac15ddd5fb06a8f82dc7020db80b164718389b1baf352a86eeddf5ed6f7` | 0 | inchangés ; syntaxe Python relue (`ast.parse`) |

Artefacts : le programme refuse une source corrigée (empreinte ≠) et une sortie existante (code 2). Différences (`diff`) : une
ligne pour la page d'état (63) ; deux lignes remplacées par trois pour `nul_v9.py` (11 et 12 → 11 à 13 ; commentaire seulement).

## 5. Ce que ce compte ne résout pas — nœuds pour la mère

- **N-T4-1. Empreinte de `nul_v9.py`.** Appliquer le couple 2 change l'empreinte de `nul_v9.py` (`7ae450df…` → `b753dac1…`),
  que la page d'état cite (ligne 64), et que d'autres pièces peuvent citer (préenregistrement de la validation de v9, scellé ;
  rapports). **La recherche des citations dans l'arbre public a été refusée à ce compte par le classifieur** (PO-006 du journal
  provisoire ; non rejouée) : les lieux ne sont pas relevés ici. De plus, réécrire `nul_v9.py` en place contredit R12 (l'arbre a
  déjà connu une réécriture en place de ce fichier, commit `516feca`, constantes de description seulement). Options : (a) ne pas
  toucher `nul_v9.py` et dire l'erratum sur la page d'état (une phrase neuve, à rédiger, à relire) — avantage : aucune empreinte
  citée ne change ; inconvénient : le commentaire fautif reste dans le code public ; (b) appliquer le couple et mettre à jour toutes
  les citations de l'empreinte — avantage : code juste ; inconvénient : touche des pièces citées, peut-être scellées, et R12 ;
  (c) fichier neuf (`nul_v9_commentaire_corrige…`) : sans objet, le code ne change pas. **Recommandation : (a)**, confiance moyenne.
- **N-T4-2.** La page d'état corrigée change d'empreinte (`c549a31b…` → `737a208a…`) : toute pièce qui citerait l'empreinte de la
  page d'état (livrables de la page) est à relever par la mère.

## 6. Lecture par un second lecteur d'un autre modèle

À venir (sous-agent neuf, modèle B ≠ A), consignée dans un fichier neuf de ce dossier.
