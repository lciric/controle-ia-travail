"""Pièce fusionnée de la passe X, v2 : les dix-sept pièces du devis v3 scellé, dans son ordre, plus la 18e pièce
(question-neutre-idees-originales-forme-2-servie-v1.md, 3b555174…, GO-2026-11-22-57), titre retiré, chaque corps à
l'octet, séparateur « [Pièce k sur 18] » (même règle que le devis v3, seul le total change). Rend aussi trois morceaux de
six pièces (1-6, 7-12, 13-18), même séparateur, pour la forme découpée proposée aux espèces Google. Contrôles : chaque
fichier source a l'empreinte attendue (deux du devis, la 18e) ; chaque corps se retrouve intact dans la pièce ; les
dix-sept premiers corps sont ceux du devis v3. N'affiche aucun corps ; n'écrase jamais."""
import hashlib, importlib.util, json, os, sys
DEVIS = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/devis-passe-x-v3/calcul_devis_passe_x_v3.py"
P18 = "/home/user/main-lecture/docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-idees-originales-forme-2-servie-v1.md"
E18 = "3b555174beef13f0c86a931f0faddb6068fdbb528acd739570a3b2ff71519f60"
E17 = "39fb4e93f26f6447822a9f548053b1ca8f8156d714d3d55bb8c0369a11b9db2a"
spec = importlib.util.spec_from_file_location("devis_v3", DEVIS)
dv = importlib.util.module_from_spec(spec); spec.loader.exec_module(dv)
sha = lambda b: hashlib.sha256(b).hexdigest()
rap, corps_l, bruts = dv.lire()
if sha(dv.fusion(corps_l, True).encode()) != E17:
    sys.exit("REFUS : les 17 corps ne redonnent pas la pièce v1 du devis")
b18 = open(P18, "rb").read()
if sha(b18) != E18:
    sys.exit("REFUS : empreinte de la 18e pièce")
c18, titre18 = dv.corps(b18.decode("utf-8"))
tous = corps_l + [c18]
sep = lambda k: "[Pièce %d sur 18]" % k
def joindre(rangs):
    return "\n\n".join(sep(k) + "\n\n" + tous[k - 1] for k in rangs) + "\n"
piece = joindre(range(1, 19))
assert all(c in piece for c in tous)
sortie = sys.argv[1]
os.makedirs(sortie, exist_ok=False)
out = {}
for nom, texte in [("piece-fusionnee-passe-x-v2.md", piece), ("morceau-1-pieces-1-a-6-v2.md", joindre(range(1, 7))),
                   ("morceau-2-pieces-7-a-12-v2.md", joindre(range(7, 13))), ("morceau-3-pieces-13-a-18-v2.md", joindre(range(13, 19)))]:
    b = texte.encode("utf-8")
    with open(os.path.join(sortie, nom), "xb") as f:
        f.write(b)
    out[nom] = {"sha256": sha(b), "octets": len(b), "signes": len(texte)}
out["piece_18"] = {"source_sha256": E18, "titre_retire_nomme_un_modele": "Fable" in (titre18 or ""), "signes_corps": len(c18)}
print(json.dumps(out, ensure_ascii=False, indent=1))
