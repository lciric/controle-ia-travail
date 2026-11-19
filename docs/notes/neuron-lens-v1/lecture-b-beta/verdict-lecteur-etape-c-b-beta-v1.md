# Verdict du lecteur neuf, étape C (avant toute pièce portant gardes, déclencheurs ou verdicts écrits par la course) — tranche B-β — v1

Écrit le 2026-11-19 vers 07:41 UTC, selon le plan de lecture v2 (`391c3b1a…`), étape C. Calculs sous-jacents scellés :
`calcul-etape-b-b-beta-v1.json` (`52b61fc4…`) et `calcul-etape-b-complement-b-beta-v1.json` (`cd58f0c7…`), script
`calcul-verdicts-b-beta-v1.py` (`20762bc3…`) essayé sur les cas gelés (`sortie-essai-calcul-verdicts-b-beta-v1.txt`, `67cc180f…`, aucun écart).
Pièces de catégorie 2 ouvertes à ce stade : `b-beta-ajustement-R.json`, `b-beta-ajustement-S.json` (champs `diffs`, `diffs_float64`,
`diffs_recopie` seulement, après la liste de leurs clés) ; `b-beta-export.json` (liste des clés et types seulement, aucune valeur).

## Sous la règle en vigueur, gardes constatées sur la machine provisoirement inconnues
- Gardes recalculées sur les sorties brutes : (a), (b) (motif « effet nul »), (c), part « score » de (e), (j) — **toutes tenues**.
- Déclencheurs : A1, A2, A3, A4, A5 **non déclenchés** ; A6 non déclenché (B-6 « intermédiaire »).
- Mesures : B-1 « autre » ; B-2 « autre » ; B-3 « reproduit » ; B-4 rapportée ; B-5 « reproduit » ; B-6 « intermédiaire » ; B-7 « autre ».
- Verdict d'ensemble : **« partiel »** (rang 5).
- Aucune variante de lecture (T-1 à T-5 en lettre, O-1, O-2, O-4, O-5/O-6, O-9) ne change un verdict ; B-1 identique sur les trois
  séries de différences versées (`diffs`, `diffs_float64`, `diffs_recopie`).

## Table selon l'issue des gardes constatées sur la machine
| issue des gardes (d), (f) à (i), (k), (n) à (s), part « matrices » de (e) | verdict |
|---|---|
| toutes tenues | « partiel » (B-1 autre, B-2 autre, B-3 reproduit, B-5 reproduit ; B-6 intermédiaire ; B-7 autre) |
| une seule manquée | « chaîne en défaut » (rang 1), aucun verdict de mesure |
| une sans trace (O-7) | (i) « partiel » ; (ii) « partiel » sous réserve « garde non constatable » |
