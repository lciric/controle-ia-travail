"""Paires « chemin cité (empreinte complète) » du brouillon 6 : vérifie l'empreinte sur disque pour les chemins du dépôt
permis (jamais sous donnees/, runs/, diag/, traces/, ni P3-consignes, items, prompts, textes-actions) et, pour les
chemins de versement proposés (docs/notes/contre-lectures-papier-C-v1/…, docs/procedures/papier-C-v1/…, brouillons/…
absents du dépôt), sur la pièce du bloc-notes de même nom de base, cherchée dans une liste fixe de dossiers."""
import re, sys, hashlib, os
R = "/home/user/controle-ia-travail"; P = sys.argv[1]
B6 = open(f"{P}/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md", encoding="utf-8").read()
t = re.sub(r"\s+", " ", B6)
paires = re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|json|py|pdf|txt))`[^`]{0,40}?\(`([0-9a-f]{64})`", t)
interdit = re.compile(r"(^donnees/|^runs/|^diag/|^traces/|P3-consignes|items-textes|prompts-p1|textes-actions)")
dossiers = [P, f"{P}/brouillon5", f"{P}/brouillon6", f"{P}/brouillon6/travail", f"{P}/traitement-brouillon5",
            f"{P}/verrou-famille1", f"{P}/contre-lectures", f"{P}/mesures", f"{P}/outils", f"{P}/brouillon5/notes",
            f"{P}/brouillon5/outils"] + [f"{P}/contre-lectures-brouillon5/{d}" for d in
            ["texte", "methode", "voisins", "voisins-panin", "voisins-second-rang", "voisins-cp02", "voisins-restants",
             "contre-lecture-courte-voisins", "voisins-cv2-03"]]
def h(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
vus = set()
for chemin, emp in paires:
    if (chemin, emp) in vus: continue
    vus.add((chemin, emp))
    if interdit.search(chemin): print("non lu (interdit) :", chemin); continue
    pr = os.path.join(R, chemin)
    if os.path.isfile(pr):
        print(("OK      " if h(pr) == emp else "ÉCART   "), "dépôt :", chemin); continue
    base = os.path.basename(chemin); trouve = [os.path.join(d, base) for d in dossiers if os.path.isfile(os.path.join(d, base))]
    if trouve:
        ok = any(h(x) == emp for x in trouve)
        print(("OK      " if ok else "ÉCART   "), "bloc-notes :", chemin, "←", [x.replace(P, "…") for x in trouve])
    else:
        print("ABSENT  ", chemin)
print("paires :", len(vus))
