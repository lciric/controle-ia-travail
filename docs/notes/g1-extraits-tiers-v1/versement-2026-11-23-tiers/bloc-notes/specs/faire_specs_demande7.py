import json, os, subprocess
S = os.environ['S']; DEP = '/home/user/controle-ia-travail'; REF = 'origin/prep/g1-brouillon7-fable-v1'
def lignes(src):
    return subprocess.run(['git', 'show', f'{REF}:{src}'], cwd=DEP, check=True, capture_output=True).stdout.decode().split('\n')
def P(L, k, t):
    assert L[k-1].count(t) == 1, (k, t); return {"ligne": k, "ancien": t}
d = 'docs/notes/g1-brouillon7-fable-v1/calculs/'
L = lignes(d + 'calculs-g1-brouillon7-v1.py')
assert L[112].startswith('titre("2.') and L[161].startswith('# ----') and L[113].startswith('# Proposition')
json.dump({"source": d + 'calculs-g1-brouillon7-v1.py', "ref": REF, "empreinte_attendue": "57eb11a2324b9e35",
  "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-calculs-g1-brouillon7-script-v1.md",
  "titre": "script des calculs du devis du brouillon 7 de G1, paragraphes 1 à 3",
  "objet": "demande 7 du rédacteur successeur : arithmétique du devis et du bruit de seuil.",
  "plages": [[1, 113], [117, 161]], "passages_en_clair": [P(L, 113, "GO-2026-11-18-48 ; ")]},
  open(S + '/specs/spec-calculs-g1-brouillon7-script-v1.json', 'w'), ensure_ascii=False, indent=2)
L = lignes(d + 'calculs-g1-brouillon7-v1-sortie.txt')
json.dump({"source": d + 'calculs-g1-brouillon7-v1-sortie.txt', "ref": REF, "empreinte_attendue": "ed8677f61d4cbfd0",
  "sortie": "docs/notes/g1-extraits-tiers-v1/extrait-calculs-g1-brouillon7-sortie-v1.md",
  "titre": "sortie des calculs du devis du brouillon 7 de G1, paragraphes 1 à 3",
  "objet": "demande 7 du rédacteur successeur : arithmétique du devis et du bruit de seuil.",
  "plages": [[1, 35]], "passages_en_clair": [P(L, 11, "GO-2026-11-18-48 ; ")]},
  open(S + '/specs/spec-calculs-g1-brouillon7-sortie-v1.json', 'w'), ensure_ascii=False, indent=2)
print('ok')
