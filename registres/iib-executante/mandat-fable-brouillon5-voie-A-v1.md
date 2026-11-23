# Mandat — rédacteur Fable : brouillon 5 de l'additif et du devis de la voie (A) — v1

Pièce de travail (classe C), écrite par l'exécutante neuve le 2026-11-22 vers 18:22Z. Mandat précédent : `mandat-fable-brouillon4-voie-A-v1.md` ; ses interdits restent en vigueur. Effort demandé : xhigh (GO-2026-11-22-114 : révision importante ; les choix sont faits).

## Ce que tu rédiges
Le **brouillon 5**, au-dessus de ton brouillon 4 (commit 6d88fbf5 ; R12 : le 4 reste intact). Il porte toute la vérification du brouillon 4 : `registres/iib-executante/contre-lecture-voie-A-v1/note-verification-brouillon4-voie-A-cl2.md` (b5e73a07…, « scellable après corrections »), avec les décisions de la mère prises à 18:21Z (étage 2, GO-2026-11-22-106) :
1. **Seuil du second rempart : l'échéance plus 80 minutes** (et non plus 10).
   - Pire cas : 57,23 USD.
   - Création de la course au plus tard le 2026-11-24 à 14:30Z.
   - Refais [M29], [M30] et [M32] par le programme : `calcul-devis-voie-A-v5.py` et sa sortie.
2. **Rapatriement non vérifié à deux heures** : machine gardée à l'arrêt, disque gardé, nœud à Lazar. **Aucune destruction sans rapatriement vérifié.** Pire cas : 59,30 USD. Retire le code 6, qui détruisait « vérifié ou non ».
3. **Mineur** : un instant d'arrêt placé dans le futur doit être refusé ; ajoute un huitième cas.
4. **Troisième rempart tenu par la mère** : elle double la minuterie dans son conteneur dès la création, sur la même échéance absolue. Écris-le, sans le compter dans le pire cas.

Si l'arithmétique d'une sortie de la vérification des gardes du lanceur ne change pas, ne la rejoue pas. Dis-le dans la note des différences du brouillon 4 au 5.

## Rendu
Dans le worktree `/tmp/claude-0/-home-user-controle-ia-travail/7aecb6e8-82ef-5d3e-813e-5cb037afe20b/scratchpad/fable` (branche locale `fable-b3-local`, à 6d88fbf5), même dossier :
- `additif-ordre-course-voie-A-v1-brouillon5.md` ;
- `devis-voie-A-v1-brouillon5.md` ;
- `differences-voie-A-brouillon4-vers-5-v1.md` ;
- les programmes v5 et leurs sorties.
Chaque pièce porte son compagnon `.sha256`. Un seul commit local, sans poussée. Réponds en 8 lignes.
