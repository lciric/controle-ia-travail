# Pièce 1 du billet — paragraphe de méthode sur nos lentilles (brouillon anglais) et registre des affirmations — v1

- Heure (UTC) : 2026-11-19T10:06:16Z. Session des lentilles. Mot de Lazar « 1 2 et 3 » (événement `785de8fe…`, 2026-11-19T10:05:29Z), lu comme « pièces
  1, 2 et 3 de `place-lentilles-billet-v1.md` (`a6e91e25…`) dans le billet » (lecture transmise à la mère, à relire à la source).
- Statut : **brouillon** pour le rédacteur du billet ; place proposée : section « Limits » ou en tête de la section de la lecture par
  lentille (pièce 2). Chaque chiffre renvoie au registre ci-dessous (R6). Aucun chiffre de la littérature (R7).

## Paragraphe (anglais)

> **A lens we fitted ourselves, on the same model.** Before reading any probe direction through a lens, we checked the tool. We fitted
> our own output-side (R) and input-side (S) lenses for Llama-3.1-8B-Instruct with the public neighbour code (stdlogits/neuron-lens,
> commit 849bfe16), on 932 full 128-token documents, and re-ran the published checks under a plan sealed before the run, read by a fresh
> agent who matched the run's own verdict code. Outcome: "partial", the outcome we had predicted. Our R lens beats the logit lens in the
> first half of the network (smallest margin 0.287 at layer 4, threshold 0.20), and our S lens reads the input side at layer 0 (0.817,
> threshold 0.60). But lenses fitted on the two halves of the corpus differ slightly beyond the frozen bound at a few early layers (up to
> 0.111, bound 0.10), and the read-versus-steering check misses at one layer (55 of 64 directions pass at layer 8, 58 required). A lens
> reads what a direction pushes on average, not what a probe detects in an episode; any lens reading below is a description that can
> raise a suspicion about a probe, never clear it.

## Registre des affirmations

| affirmation | valeur | pièce (chemin, empreinte) |
|---|---|---|
| lentilles R et S ajustées par nous, code voisin au commit 849bfe16 | — | `docs/notes/neuron-lens-v1/texte-gele-tranche-b-beta-v1.md` (`f5d46860…`), « Énoncé » et « Documents » |
| 932 documents pleins de 128 jetons | 932 | même texte, « Énoncé », l. 75-76 ; `b-beta-ajustement-R.json` (`rows_sha256` `a6afd972…`) |
| plan scellé avant la course, lecteur neuf, accord avec le code de verdicts de la course | — | `lecture-b-beta/verdict-b-beta-v1.md` (`3a9b947e…`), en-tête et « Verdict, en mots simples » ; plan v2 `391c3b1a…` |
| issue « partiel », prédite | « partiel » ; prédiction « partiel », confiance 0,5 | verdict `3a9b947e…` ; texte gelé, « Prédiction chiffrée », dernière ligne |
| avance sur la lentille des logits : plus petit écart 0,287 à la couche 4, seuil 0,20 | 0,2872 | verdict `3a9b947e…`, ligne B-3 |
| lecture côté entrée à la couche 0 : 0,817, seuil 0,60 | 0,8167 | verdict, ligne B-5 |
| moitiés du corpus : jusqu'à 0,111, borne 0,10, à quelques premières couches | 0,1114 (R, cible `mid`, couche 0) ; six couches-cibles au-dessus | verdict, ligne B-1 |
| lecture contre pilotage : 55 directions sur 64 à la couche 8, 58 exigées | 0,8594 ; seuil 0,90 | verdict, ligne B-2 |
| « reads what a direction pushes on average » | — | texte gelé, « Critères de lecture gelés », après le tableau du verdict d'ensemble |
| accord de Lazar sur le verdict | « go accepter » | `lecture-b-beta/accord-lazar-verdict-b-beta-v1.md` (`8469add5…`) |

## À trancher par le rédacteur du billet
- « 64 directions » : le verdict parle de « pôles » ; 64 pôles retenus par couche (« aucun pôle écarté », verdict, réserves R4).
- Le paragraphe ne dit rien de la lecture contre ablation (couche 15 hors règle) : hors verdict d'ensemble ; à ajouter si la pièce 2
  parle des couches tardives.
