"""Contre-lecture banque v3 — k1 : empreintes, équivalence v1 -> v3 par la règle écrite, clé et recherche de la clé.

N'imprime jamais la clé : seulement son nombre de bits, des booléens et des noms de fichiers.
Usage : python3 -I k1_equivalence_cle_v1.py BANQUE_DIR RACINE_ESSAIM DOSSIER_CONTRE_LECTURE
"""
import hashlib
import json
import pathlib
import sys

import numpy as np

B, R, MOI = (pathlib.Path(x) for x in sys.argv[1:4])
PARTS = ("train", "test", "test_final")
CHAMPS = ("famille", "texte", "etiquettes", "verite", "source")
out = []


def dire(*a):
    out.append(" ".join(str(x) for x in a))


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def compagnon(p: pathlib.Path):
    c = p.with_name(p.name + ".sha256")
    return c.read_text(encoding="utf-8").split()[0] if c.exists() else None


# 1. Empreintes
dire("1. Empreintes")
lignes = (B / "EMPREINTES-banque-v3-v1.txt").read_text(encoding="utf-8").splitlines()
n_ok = 0
for l in lignes:
    h, nom = l.split("  ", 1)
    p = B / nom
    bon = p.exists() and sha(p) == h and compagnon(p) == h
    n_ok += bon
    if not bon:
        dire("   ÉCART :", nom)
dire(f"   EMPREINTES-banque-v3-v1.txt : {n_ok}/{len(lignes)} lignes conformes (fichier = ligne = compagnon) ;"
     f" compagnon de la liste conforme : {sha(B / 'EMPREINTES-banque-v3-v1.txt') == compagnon(B / 'EMPREINTES-banque-v3-v1.txt')}")
tous = [p for p in sorted(B.rglob("*")) if p.is_file() and not p.name.endswith(".sha256")]
sans, faux = [], []
for p in tous:
    c = compagnon(p)
    if c is None:
        sans.append(str(p.relative_to(B)))
    elif c != sha(p):
        faux.append(str(p.relative_to(B)))
dire(f"   tous les fichiers du dossier banque/ : {len(tous)} ; sans compagnon {sans} ; compagnon faux {faux}")
listes = {str(p.relative_to(B)) for p in tous if str(p.relative_to(B)).startswith("construction-v3/")}
dans_liste = {l.split('  ', 1)[1] for l in lignes}
dire(f"   fichiers de construction-v3/ absents de EMPREINTES-banque-v3-v1.txt : {sorted(listes - dans_liste)}")
attendus = {"banque-confrontation-v3.json": "157a2b45a8d9fd88cc5dca2f483c2dc79457d781d44f9802b2c053f530c0011d",
            "banque-confrontation-v3-secret.json": "a13217b8c72da77a89d871f012272dff778478dbaeb67607535d26254ea6a427",
            "banque-confrontation-v3-cle.json": "2decc65964b6f8ea865244b37954dcf616efb71d7cdef75b59568313d447558a",
            "banque-confrontation-v1.json": "f1387a20cb272d2e8c205102147dfee71cd1d372f7f5d2ad4ff8233783cc83cc",
            "banque-confrontation-v1-secret.json": "c68d7d4ba34b49b85a9327adfe21d30cc8118f1d100a47db2a47e97329715caf",
            "banque-confrontation-v2.json": "52beb637823b72f475fd1ddcf446e9b79cafa5d2cd47d16c08b663d2b9388d10",
            "contre-lectures/banque-v2-cl1/CONTRE-LECTURE-banque-v2-v1.md": "5ee8df413e7d7285137826a8976142ff0d5141f1063d3e2c37d25cb544cc9566"}
for nom, h in attendus.items():
    dire(f"   {nom} : empreinte citée au LISEZMOI-v5 / constructeur = fichier = compagnon : {sha(B / nom) == h == compagnon(B / nom)}")

# 2. Équivalence par la règle écrite
dire("\n2. Équivalence v1 -> v3 (code à moi, règle du manifeste et de la clé)")
v1 = json.loads((B / "banque-confrontation-v1.json").read_text(encoding="utf-8"))
s1 = json.loads((B / "banque-confrontation-v1-secret.json").read_text(encoding="utf-8"))
v2 = json.loads((B / "banque-confrontation-v2.json").read_text(encoding="utf-8"))
v3 = json.loads((B / "banque-confrontation-v3.json").read_text(encoding="utf-8"))
s3 = json.loads((B / "banque-confrontation-v3-secret.json").read_text(encoding="utf-8"))
cle = json.loads((B / "banque-confrontation-v3-cle.json").read_text(encoding="utf-8"))
E = int(cle["entropie_seed_sequence"])
io = v3["manifeste"]["identifiants_opaques"]
hE = hashlib.sha256(str(E).encode("ascii")).hexdigest()
dire(f"   clé : {E.bit_length()} bits (compatible avec secrets.randbits(128) : {E.bit_length() <= 128}) ; écriture décimale canonique : {cle['entropie_seed_sequence'] == str(E)}")
dire(f"   sha256(écriture décimale) = manifeste = fichier de clé = 9cb96341… : {hE == io['entropie_sha256'] == cle['entropie_sha256'] and hE.startswith('9cb963419466f6eb')}")
e_v2 = None
for k, v in (v2["manifeste"].get("identifiants_opaques") or {}).items():
    if "entropie" in k and not k.endswith("sha256"):
        try:
            e_v2 = int(v)
        except (TypeError, ValueError):
            pass
dire(f"   clé différente de l'entropie de la v2 et de l'entropie de partition de la v1 : {E != e_v2 and E != int(v1['manifeste']['entropie_seed_sequence'])} (entropie v2 lue au manifeste v2 : {e_v2 is not None})")
dire(f"   clés du fichier de clé : {sorted(cle)} ; « banque » : {cle['banque']} ; règle = règle du manifeste : {cle['regle'] == io['regle']}")
taches = [(p, t) for p in PARTS for t in v1[p]]
perm = np.random.default_rng(np.random.SeedSequence(E)).permutation(len(taches))
att = {p: [] for p in PARTS}
sec = {}
for i, (p, t) in enumerate(taches):
    nid = f"t-{int(perm[i]) + 1:04d}"
    att[p].append({"id": nid, **{k: t[k] for k in CHAMPS}})
    d = dict(s1[t["id"]])
    d["id_v1"] = t["id"]
    sec[nid] = d
for p in PARTS:
    att[p].sort(key=lambda x: x["id"])
sec = {k: sec[k] for k in sorted(sec)}
for p in PARTS:
    dire(f"   {p} : {len(v3[p])} tâches (v1 : {len(v1[p])}) ; égales à la reconstruction : {v3[p] == att[p]} ;"
         f" ordre des champs égal : {[list(t) for t in v3[p]] == [list(t) for t in att[p]]} ;"
         f" triée par identifiant : {[t['id'] for t in v3[p]] == sorted(t['id'] for t in v3[p])} ;"
         f" mêmes tâches que la v1 (contenu, multiensemble) : {sorted(json.dumps({k: t[k] for k in CHAMPS}, sort_keys=True) for t in v3[p]) == sorted(json.dumps({k: t[k] for k in CHAMPS}, sort_keys=True) for t in v1[p])}")
octets = json.dumps({**att, "manifeste": v3["manifeste"]}, ensure_ascii=False, indent=1) + "\n"
dire(f"   octets reconstruits (manifeste repris) = 157a2b45… : {hashlib.sha256(octets.encode('utf-8')).hexdigest() == sha(B / 'banque-confrontation-v3.json')}")
dire(f"   secret v3 = secret v1 + id_v1 (valeurs et ordre des clés) : {s3 == sec and list(s3) == list(sec) and all(list(s3[k]) == list(sec[k]) for k in sec)}")
octets_s = json.dumps(sec, ensure_ascii=False, indent=1) + "\n"
dire(f"   octets du secret reconstruits = a13217b8… : {hashlib.sha256(octets_s.encode('utf-8')).hexdigest() == sha(B / 'banque-confrontation-v3-secret.json')}")
ids3 = [t["id"] for p in PARTS for t in v3[p]]
dire(f"   identifiants : {len(set(ids3))} distincts sur {len(ids3)} ; = t-0001…t-0200 : {sorted(ids3) == [f't-{k:04d}' for k in range(1, 201)]} ; communs avec la v1 : {len(set(ids3) & set(s1))}")
m1, m3 = v1["manifeste"], v3["manifeste"]
diff = sorted(k for k in set(m1) | set(m3) if m1.get(k) != m3.get(k))
dire(f"   manifeste : clés qui diffèrent de la v1 {diff} ; ordre des clés = v1 + identifiants_opaques : {list(m3) == list(m1) + ['identifiants_opaques'] or list(m3) == list(m1)}")
dire(f"   manifeste : quand_utc {m3['quand_utc']} ; numpy de construction {io.get('numpy')} ; dérivée de {io['derivee_de']['sha256'][:8]}… / {io['derivee_de']['secret_sha256'][:8]}… ; clés de identifiants_opaques {sorted(io)}")
perm_v2 = None
if e_v2 is not None:
    perm_v2 = np.random.default_rng(np.random.SeedSequence(e_v2)).permutation(len(taches))
    dire(f"   permutations v2 et v3 : {int((perm_v2 == perm).sum())} rangs communs sur 200 (hasard : ~1)")

# 3. Recherche de la clé
dire("\n3. Recherche de la clé (écriture décimale entière, fenêtres de 12 chiffres, hexadécimal, fenêtres de 12 caractères hexadécimaux)")
dec = str(E)
hx = format(E, "x")
motifs = [("décimal entier", dec.encode()), ("hexadécimal entier", hx.encode()), ("hexadécimal entier (majuscules)", hx.upper().encode())]
fen = [dec[i:i + 12].encode() for i in range(len(dec) - 11)] + [hx[i:i + 12].encode() for i in range(len(hx) - 11)]
fen += [hx.upper()[i:i + 12].encode() for i in range(len(hx) - 11)]
cible_cle = (B / "banque-confrontation-v3-cle.json").resolve()


def chercher(fichiers, etiquette):
    touches, n = [], 0
    for p in fichiers:
        if p.resolve() == cible_cle:
            continue
        try:
            o = p.read_bytes()
        except OSError:
            continue
        n += 1
        entiers = [nom for nom, m in motifs if m in o]
        partiels = sum(1 for m in fen if m in o)
        if entiers or partiels:
            touches.append((str(p), entiers, partiels))
    dire(f"   {etiquette} : {n} fichiers lus ; fichiers touchés : {len(touches)}")
    for t in touches:
        dire(f"      {t[0]} : entier {t[1]} ; fenêtres partielles {t[2]}")


chercher([p for p in sorted(B.rglob("*")) if p.is_file()], "dossier banque/ (récursif, clé exclue)")
chercher([p for p in sorted(R.iterdir()) if p.is_file()], "racine de l'essaim (un niveau)")
chercher([p for p in sorted((R / "essaim_m3").glob("*.py"))] + [p for p in sorted((R / "essaim_m3" / "noyau").glob("*.py"))], "code essaim_m3/*.py et essaim_m3/noyau/*.py")
chercher([p for p in sorted(MOI.rglob("*")) if p.is_file()], "mes propres fichiers (/var/tmp/contre-lecture-banque-v3-v1)")
a8 = json.loads((B / "construction-v3/artefacts-v1/A8-cle-fausse.json").read_text(encoding="utf-8"))
dire(f"   A8 (clé fausse) : clé différente de la vraie : {int(a8['entropie_seed_sequence']) != E} ; reprend l'empreinte vraie : {a8.get('entropie_sha256') == hE}")
print("\n".join(out))
