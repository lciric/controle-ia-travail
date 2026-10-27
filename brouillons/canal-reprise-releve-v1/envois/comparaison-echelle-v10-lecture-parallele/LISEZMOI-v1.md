# Comparaison d'échelle 8B contre 70B — lecture parallèle (non décisive) — v1

Lignée conv-audit (instance du 27 octobre 2026), écrit à 15:40 UTC (heure lue sur `date -u` : 15:39:50). Lecture
**parallèle** annoncée à session-depot dans le n° 109 (point A.6) : la sienne, décisive, prime ; si elles diffèrent, on
audite les deux (R4).

## Verdict

**Concordante.** Sens a→b : indécis ; sens b→a : indécis ; combinaison : indécis. Phrase permise : « Le dispositif ne
tranche pas. » Mêmes nombres, mêmes conditions non tenues, mêmes deux points R4 que le verdict décisif de session-depot
(`docs/verdicts/verdict-lecture-echelle-conscience-eval-v10.md` sur `main`, `aaf43f95…`) : **aucune divergence à auditer.**

## Comment elle a été faite

1. **Rejeu de l'analyse scellée**, sur processeur, en mode répétition (non décisif : il saute seulement les contrôles de
   provenance du mode décisif) : outils et activations de la branche `donnees/echelle-conscience-eval-v9` (commit
   `7b0f84d`), empreintes vérifiées ; numpy 2.4.6 ; graine `4429003211691042563` ; commande
   `analyser_echelle_v9.py stimuli/echelle-v2.json resultats-echelle-v9/petit resultats-echelle-v9/grand 4429003211691042563 SORTIE --repetition`,
   de 14:38:07 à 15:29:33 UTC. Sortie : `analyse-echelle-v9-repetition.json` (`29dec0a8…`).
2. **Prononcé par un sous-agent neuf** (Fable 5.1 ; ni auteur du préenregistrement ni de l'analyse ; n'a vu aucun autre
   verdict), qui n'a ouvert que trois fichiers : le texte scellé `prereg/test-echelle-conscience-eval-v10.md`
   (`2af6516d…`), la sortie rejouée, et `analyser_echelle_v9.py` (`00ef7c85…`, l'empreinte du tableau du texte) pour le
   sens des champs. Il a recalculé l'issue depuis les nombres et les règles du texte, puis l'a comparée au champ
   « lecture » du script. Verdict : `verdict-parallele-echelle-v10-v1.md` (`db8a377e…`).

## Les deux points R4, des deux côtés

| point | lecture parallèle | verdict décisif |
|---|---|---|
| A_conf_T1 du 8B, sens a→b : 0,0012, intervalle [0,000 ; 0,007], λ = 0,293 < 1 | « ambigu » : touché si l'on lit 0,00 à deux décimales (alors audit des formes et réserve), non touché sinon | **déclenché à la lettre** ; audit des formes à faire avant tout rapport ; réserve dite |
| A_ctx_fixe du 70B, sens a→b : intervalle [1,000 ; 1,000] | « ambigu » entre « intervalles anormalement étroits » et « A_ctx_fixe peut valoir 1,00 sans réserve » | exempté par le texte (CLY-11) |

Aucun des deux ne change l'issue. La lecture la plus prudente est celle du verdict décisif ; je n'y ajoute rien.

## Ce qu'elle ne permet pas

Rien de décisif (mode répétition : commit des outils, propreté de l'arbre, type des activations, nom et empreinte du script
de mesure non vérifiés ici). Même décisive, la sortie ne permet que « Le dispositif ne tranche pas » : les intervalles
couvrent l'hypothèse comme le nul (λ_a→b du 8B de −0,245 à 1,249). Aucun chiffre n'est opposable.
