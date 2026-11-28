"""Compte chaque ancre (« ancien ») des paires proposees dans le candidat 1 : (a) dans le texte tel quel ; (b) apres
application des paires precedentes, dans l'ordre ; verifie que chaque paire du JSON est recopiee mot pour mot dans le
rapport du correcteur (notation « \\n »). N'ecrit rien ; imprime un JSON."""
import hashlib
import json
import sys
from pathlib import Path

cand, paires_json, rapport = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
texte = cand.read_text(encoding="utf-8")
paires = json.loads(paires_json.read_text(encoding="utf-8"))
rap = rapport.read_text(encoding="utf-8")
sortie = {"candidat_sha256": hashlib.sha256(cand.read_bytes()).hexdigest(), "paires": []}
t = texte
for p in paires:
    a, n = p["ancien"], p["nouveau"]
    ligne = texte[:texte.find(a)].count("\n") + 1 if a in texte else None
    entree = {"source": p["source"], "compte_candidat1": texte.count(a), "ligne_debut": ligne,
              "compte_apres_paires_precedentes": t.count(a),
              "ancien_dans_rapport": rap.count(a.replace("\n", "\\n")),
              "nouveau_dans_rapport": rap.count(n.replace("\n", "\\n")),
              "nouveau_contient_ancien": a in n}
    t = t.replace(a, n, 1) if t.count(a) == 1 else t
    sortie["paires"].append(entree)
# aucune ancre ne doit reparaitre dans un « nouveau » d'une autre paire (sinon double application)
autres = []
for i, p in enumerate(paires):
    for j, q in enumerate(paires):
        if i != j and p["ancien"] in q["nouveau"]:
            autres.append((i + 1, j + 1))
sortie["ancre_i_dans_nouveau_j"] = autres
sortie["texte_final_sha256"] = hashlib.sha256(t.encode("utf-8")).hexdigest()
print(json.dumps(sortie, ensure_ascii=False, indent=1))
