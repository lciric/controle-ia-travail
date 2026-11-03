"""Remplit le gabarit scellé de cohérence finale : <<FICHIERS>> (liste des réponses finales avec empreintes) et <<VERSION>>.
Usage : remplir_coherence_v1.py correspondances.json version sortie.md
correspondances.json : {"titre": "chemin relatif au dépôt", ...}"""
import json, hashlib, sys
R = '/home/claude/controle-ia-travail/'
G = R + 'brouillons/reprise-conv-audit-2026-11-02-nuit/prompts-sous-agents/coherence-finale-gabarit-v1.md'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
assert sha(G) == open(G + '.sha256').read().split()[0], 'gabarit modifié'
corr, vers, sortie = sys.argv[1:4]
C = json.load(open(corr))
lignes = [f"- {titre} : `{R}{p}` (sha256 `{sha(R + p)}`)" for titre, p in C.items()]
t = open(G).read().replace('<<FICHIERS>>', '\n'.join(lignes)).replace('<<VERSION>>', vers)
open(sortie, 'w').write(t); print(sortie, hashlib.sha256(t.encode()).hexdigest())
