"""Fusion des extractions du bibliothécaire (GO-2026-11-23-31), classe C. Usage : python -I fusionner_v1.py DOSSIER_EXTRACTIONS SORTIE_DIR VERSION
Lit les tableaux Markdown (≥ 11 colonnes : n°, type, énoncé, source, état, piste, gain, coût, portée, découverte, pourquoi),
écrit registre-idees-pistes-vN.md et pistes-a-tester-organisme-vN.md ; score = gain × portée × découverte / coût (jugement des extracteurs)."""
import os, re, sys
D, OUT, V = sys.argv[1], sys.argv[2], sys.argv[3]
NOMS = {"A": "idée intéressante et réponses de Google", "B": "protocole X, lot 1 (attaquant, boucle audit-recapture, dommage, dommages plantés, marge)",
        "C": "protocole X, lot 2 (conscience et anesthésie, contrôle diffus)", "D": "protocole X, programmation de poids", "E": "transcript de la mère et registres"}
def num(x):
    m = re.search(r"\d+(?:[.,]\d+)?", x); return float(m.group().replace(",", ".")) if m else None
lignes = []
for f in sorted(os.listdir(D)):
    if not f.endswith(".md"): continue
    lot = f.split("-")[0]
    for l in open(os.path.join(D, f), encoding="utf-8"):
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) < 11 or not re.fullmatch(r"[A-Za-z]*[\s.-]*\d+[a-z]?", c[0]) : continue
        g, co, p, dc = (num(c[i]) for i in (6, 7, 8, 9))
        s = round(g * p * dc / co, 1) if None not in (g, co, p, dc) and co else None
        lignes.append(dict(lot=lot, n=c[0], type=c[1], enonce=c[2], source=c[3], etat=c[4], piste=c[5], g=c[6], co=c[7], p=c[8], dc=c[9], pq=" ".join(c[10:]), score=s))
for i, x in enumerate(lignes, 1): x["id"] = f"I-{i:03d}"
def ecrire(nom, t):
    with open(os.path.join(OUT, nom), "x", encoding="utf-8") as fh: fh.write(t)
L = [f"# Registre des idées, pistes, hypothèses, expériences et décisions — session mère du 23 novembre 2026 (v{V})", "",
     "Classe C, bibliothécaire (GO-2026-11-23-31). Une ligne par élément, tirée par des agents d'extraction de sources nommées ; notes de 1 à 5 = jugement des extracteurs, non opposables. Score = gain × portée × découverte / coût.", "",
     f"{len(lignes)} lignes. Lots : " + " ; ".join(f"{k} = {v}" for k, v in NOMS.items()), "",
     "| id | lot | type | énoncé | source | état | piste à tester dans l'organisme | gain | coût | portée | découverte | score | pourquoi |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
L += [f"| {x['id']} | {x['lot']} {x['n']} | {x['type']} | {x['enonce']} | {x['source']} | {x['etat']} | {x['piste']} | {x['g']} | {x['co']} | {x['p']} | {x['dc']} | {x['score'] if x['score'] is not None else ''} | {x['pq']} |" for x in lignes]
ecrire(f"registre-idees-pistes-v{V}.md", "\n".join(L) + "\n")
P = [x for x in lignes if x["piste"] and not re.match(r"(?i)sans objet|—|-$|n/?a", x["piste"])]
P.sort(key=lambda x: -(x["score"] or 0))
L = [f"# Pistes à tester dans l'organisme d'idéation (v{V})", "", "Mot de Lazar : « toutes mes hypothèses et toutes les idées doivent être testées », y compris les pistes des réponses de Google (et celles à venir de la v2 du collisionneur).", "",
     f"{len(P)} pistes (sur {len(lignes)} lignes du registre), classées par score décroissant. Rien n'est lancé par cette liste : chaque essai passe par la chaîne de l'organisme (question neutre, devis, GO).", "",
     "| rang | id | piste à tester | élément d'origine | état | score |", "|---|---|---|---|---|---|"]
L += [f"| {i} | {x['id']} | {x['piste']} | {x['enonce']} | {x['etat']} | {x['score'] if x['score'] is not None else ''} |" for i, x in enumerate(P, 1)]
ecrire(f"pistes-a-tester-organisme-v{V}.md", "\n".join(L) + "\n")
print(len(lignes), "lignes ;", len(P), "pistes ; par lot :", {k: sum(1 for x in lignes if x['lot'] == k) for k in NOMS})
