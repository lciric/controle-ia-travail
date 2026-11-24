"""Brouillon 6 : derniers renvois (suite du programme de corrections du brouillon 5 au brouillon 6)."""
import sys
from pathlib import Path
p = Path(sys.argv[1]); t = p.read_text(encoding="utf-8")
def r(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:80])
    t = t.replace(old, new)
r("| cas où une sortie existe au scellement : écrit, en écart déclaré | « Quand l'additif doit être scellé » ; nœud NL-10 |",
  "| scellement après la fin de la course : écrit, en écart déclaré | « Quand l'additif doit être scellé » ; nœud NL-0 |")
r("Ils sont fermés ici par le rédacteur du brouillon 5, avant la contre-lecture finale, qui relit ce brouillon-ci.",
  "Ils ont été fermés au brouillon 5 par son rédacteur, avant la contre-lecture finale, qui relit le brouillon 6.")
r("Rédacteur : Claude Fable 5.2 (en-tête, « Rédacteur du brouillon 5 »). Tout changement est dit ici ; rien d'autre ne change. Les changements 3 et 4 dépassent le report : ils sont des nœuds de Lazar (NL-9, NL-10).",
  "Rédacteur : Claude Fable 5.2 (en-tête, « Rédacteur des brouillons 5 et 6 »). Tout changement est dit ici ; rien d'autre ne change. Les changements 3 et 4 dépassent le report : ils sont des nœuds de Lazar (NL-9 ; NL-10, devenu NL-0 au brouillon 6).")
r("Mot de Lazar relayé par la session mère le 23 novembre, à citer au champ AD-1 s'il est inscrit au registre : « un résultat comparé, pas un résultat seul : go ».",
  "Le principe est accordé : mot de Lazar relayé par la session mère le 23 novembre, « un résultat comparé, pas un résultat seul : go », inscrit au registre des accords (GO-2026-11-23-17, point 4 : « résultat comparé dans l'additif (référence boîte noire, bases, jumeau honnête) »). Reste à Lazar la forme écrite ici.")
p.write_text(t, encoding="utf-8")
