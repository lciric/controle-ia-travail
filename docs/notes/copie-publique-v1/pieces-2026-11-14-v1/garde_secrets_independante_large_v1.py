"""Recherche indépendante de formes de clés sur l'arbre neuf et dans ses archives (à toute profondeur).
N'affiche jamais un jeton : chemin, forme, longueur, marque factice. Usage : python garde… ARBRE SCRIPT_V7"""
import importlib.util, json, os, re, sys
from pathlib import Path

arbre, script = Path(sys.argv[1]), Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("de7", script); de = importlib.util.module_from_spec(spec); spec.loader.exec_module(de)
FORMES = [("sk-ant-", re.compile(rb"sk-ant-[A-Za-z0-9_\-]{6,}")),
          ("sk-", re.compile(rb"(?<![A-Za-z0-9_\-])sk-(?!ant-)[A-Za-z0-9_\-]{12,}")),
          ("ghp_", re.compile(rb"gh[pousr]_[A-Za-z0-9]{8,}")),
          ("hf_", re.compile(rb"(?<![A-Za-z0-9])hf_[A-Za-z0-9]{8,}")),
          ("AKIA", re.compile(rb"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])")),
          ("AIza", re.compile(rb"AIza[0-9A-Za-z_\-]{6,}"))]
MARQUE = re.compile(rb"faux|factice|essai|fake|cle-fa|exemple|example", re.I)
valeurs = de.valeurs_secretes()
bilan = {"fichiers": 0, "membres_d_archives": 0, "archives": 0, "variables_de_cles_comparees": len(valeurs),
         "valeurs_d_environnement_trouvees": 0, "jetons": [], "chemins_sous_embargo": 0, "chemins_portant_un_nom_retire": []}

def examine(nom, contenu, profondeur=0):
    for var, v in valeurs.items():
        if v and v in contenu:
            bilan["valeurs_d_environnement_trouvees"] += 1
            bilan["jetons"].append({"chemin": nom, "forme": "valeur d'une variable de l'environnement", "marque": False})
    for forme, motif in FORMES:
        for m in motif.finditer(contenu):
            ligne = contenu[contenu.rfind(b"\n", 0, m.start()) + 1: (contenu.find(b"\n", m.end()) if contenu.find(b"\n", m.end()) >= 0 else len(contenu))]
            bilan["jetons"].append({"chemin": nom, "forme": forme, "longueur": len(m.group(0)),
                                    "marque_dans_le_jeton": bool(MARQUE.search(m.group(0))),
                                    "marque_dans_la_ligne": bool(MARQUE.search(ligne))})
    if de.est_archive(contenu) or contenu[:2] == b"\x1f\x8b":
        if profondeur == 0:
            bilan["archives"] += 1
        for membre, c in de._membres(nom, contenu):
            bilan["membres_d_archives"] += 1
            examine(f"{nom}!{membre}", c, profondeur + 1)

for racine, dossiers, fichiers in os.walk(arbre):
    if ".git" in dossiers:
        dossiers.remove(".git")
    for f in fichiers:
        p = Path(racine) / f
        rel = p.relative_to(arbre).as_posix()
        bilan["fichiers"] += 1
        if de.sous_embargo(rel):
            bilan["chemins_sous_embargo"] += 1
            continue                                   # jamais lu
        if de.porte_un_nom_retire(rel):
            bilan["chemins_portant_un_nom_retire"].append(rel)
        examine(rel, p.read_bytes())
print(json.dumps(bilan, ensure_ascii=False, indent=1))
