"""Textes servis de la passe X en groupes thématiques — v1 (réponse 36 de Fable, C.3 ; message de la mère de 12:46Z).
Les dix-huit corps sont ceux de la pièce v2 (13928f87…), recalculés par son programme et contrôlés. Chaque texte : le
préambule fixe, une ligne vide, puis les pièces du groupe, chacune sous son séparateur « [Pièce k sur 18] » (numéro
d'origine). Trois groupes de six, et six moitiés de trois pour la relance « groupe scindé ». N'affiche aucun corps."""
import hashlib, importlib.util, json, os, sys
V2 = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/passe-x-piece-fusionnee-v2/former_piece_fusionnee_passe_x_v2.py"
DEVIS = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/devis-passe-x-v3/calcul_devis_passe_x_v3.py"
P18 = "/home/user/main-lecture/docs/notes/demandes-fable-api-2026-11-22-v1/question-neutre-idees-originales-forme-2-servie-v1.md"
E_PIECE_V2 = "13928f876d23bd3d8f99b4d6b4e4576f3d655045b4fb604d07ebe27da9c45bbc"
GROUPES = {1: (1, 2, 3, 9, 15, 18), 2: (4, 5, 6, 7, 8, 17), 3: (10, 11, 12, 13, 14, 16)}
PREAMBULE = ("Voici {n} questions de recherche, numérotées comme dans une liste de dix-huit. Répondez à chacune, dans "
             "l'ordre, sous un titre de la forme « Réponse k », où k est le numéro de la pièce. Chaque réponse fait au "
             "plus 600 mots. Terminez par une ligne seule : FIN DES RÉPONSES.")
NOMBRES = {6: "six", 3: "trois"}
sha = lambda b: hashlib.sha256(b).hexdigest()
spec = importlib.util.spec_from_file_location("devis_v3", DEVIS)
dv = importlib.util.module_from_spec(spec); spec.loader.exec_module(dv)
_, corps_l, _ = dv.lire()
c18, _ = dv.corps(open(P18, "rb").read().decode("utf-8"))
tous = corps_l + [c18]
sep = lambda k: "[Pièce %d sur 18]" % k
piece_v2 = "\n\n".join(sep(k) + "\n\n" + tous[k - 1] for k in range(1, 19)) + "\n"
if sha(piece_v2.encode()) != E_PIECE_V2:
    sys.exit("REFUS : les dix-huit corps ne redonnent pas la pièce v2")
assert sorted(sum(GROUPES.values(), ())) == list(range(1, 19))
def texte(rangs):
    return PREAMBULE.format(n=NOMBRES[len(rangs)]) + "\n\n" + "\n\n".join(sep(k) + "\n\n" + tous[k - 1] for k in rangs) + "\n"
unites = {}
for g, rangs in GROUPES.items():
    unites[f"groupe-{g}"] = rangs
    unites[f"groupe-{g}-moitie-a"] = rangs[:3]
    unites[f"groupe-{g}-moitie-b"] = rangs[3:]
os.makedirs(sys.argv[1], exist_ok=False)
out = {"groupes": {k: list(v) for k, v in GROUPES.items()}, "preambule_sha256": sha(PREAMBULE.encode()), "textes": {}}
for nom, rangs in unites.items():
    b = texte(rangs).encode("utf-8")
    with open(os.path.join(sys.argv[1], nom + ".md"), "xb") as f:
        f.write(b)
    out["textes"][nom] = {"rangs": list(rangs), "sha256": sha(b), "octets": len(b)}
print(json.dumps(out, ensure_ascii=False, indent=1))
