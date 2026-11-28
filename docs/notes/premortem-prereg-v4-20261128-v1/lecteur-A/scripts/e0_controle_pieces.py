"""E0 — controle par programme des trois pieces : chaque empreinte citee (longueur, presence au depot, fichier designe),
chaque chemin, et les ecarts de citation entre pieces. Les empreintes sont cherchees (1) dans les compagnons `.sha256` de
l'arbre de travail et de cinq references git (sans extraction : `git grep`), (2) par calcul direct sur le fichier de l'arbre
de travail quand il n'est ni une archive d'activations, ni des poids, ni un verdict de sonde, ni une consigne privee.
Aucun fichier interdit n'est ouvert : pour eux, seul le compagnon est lu."""
import hashlib, json, pathlib, re, subprocess, sys
from collections import defaultdict

depot = pathlib.Path(sys.argv[1])
B = depot / "brouillons" / "prereg-v4-c-furtif-g1"
PIECES = {"G0": B / "G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md",
          "G1": B / "G1-architecture-h1-h2-v1-brouillon-gemini-1.md",
          "D": B / "arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md"}
REFS = ["HEAD", "42cdfcf29", "5817bb0a5", "origin/banque/dose-reponse-consigne-cachee-v1", "origin/main",
        "origin/passation/claude-mere-v4-20261128"]
INTERDITS = (".npz", ".safetensors", "verdict", "consignes-privees", "P3-consignes", "saboteur-budget", "sondes-", "plancher")

def git(*a):
    return subprocess.run(["git", "-C", str(depot), *a], capture_output=True, text=True).stdout

# index empreinte -> {(reference, chemin)} par les compagnons
index = defaultdict(set)
for ref in REFS:
    out = git("grep", "-I", "-E", "^[0-9a-f]{64}", ref, "--", "*.sha256")
    for ligne in out.splitlines():
        try:
            r, chemin, contenu = ligne.split(":", 2)
        except ValueError:
            continue
        m = re.match(r"([0-9a-f]{64})", contenu)
        if m:
            index[m.group(1)].add((ref, chemin[:-len(".sha256")]))
fichiers = {ref: set(git("ls-tree", "-r", "--name-only", ref).splitlines()) for ref in REFS}

def existe(chemin):
    return [ref for ref in REFS if chemin in fichiers[ref]]

def sha_direct(chemin):
    p = depot / chemin
    if not p.is_file() or any(x in chemin for x in INTERDITS):
        return None
    return hashlib.sha256(p.read_bytes()).hexdigest()

RE_HEX = re.compile(r"(?<![0-9a-f])[0-9a-f]{16,}(?![0-9a-f])")
RE_CHEMIN = re.compile(r"`((?:src|prereg|docs|diag|donnees|registres|tests|scripts|runs|brouillons)/[^`\s]+|[A-Za-z0-9_.\-]+\.(?:md|py|json|npz|safetensors|txt))`")
res = {"references": REFS, "pieces": {}}
for nom, p in PIECES.items():
    t = p.read_text(encoding="utf-8")
    emp = []
    for m in RE_HEX.finditer(t):
        h = m.group(0)
        ligne = t.count("\n", 0, m.start()) + 1
        avant = t[max(0, m.start() - 260):m.start()]
        chemins_avant = RE_CHEMIN.findall(avant)
        voisin = chemins_avant[-1] if chemins_avant else None
        e = {"empreinte": h, "longueur": len(h), "ligne": ligne, "chemin_voisin": voisin}
        if len(h) == 64:
            e["compagnons"] = sorted(f"{r}:{c}" for r, c in index.get(h, ()))[:4]
            d = None
            if voisin:
                cands = [voisin] + [c for ref in ("HEAD",) for c in fichiers[ref] if c.endswith("/" + voisin)]
                for c in cands:
                    d = sha_direct(c)
                    if d is not None:
                        e["calcul_direct"] = {"chemin": c, "sha256": d, "egal": d == h}
                        break
            e["designe_un_fichier_du_depot"] = bool(e["compagnons"]) or bool(e.get("calcul_direct", {}).get("egal"))
            e["mentions_ailleurs"] = len([x for x in git("grep", "-l", h, "HEAD").splitlines() if "prereg-v4-c-furtif-g1" not in x and "passation-v4-messages" not in x])
        emp.append(e)
    chemins = []
    for m in RE_CHEMIN.finditer(t):
        c = m.group(1)
        ligne = t.count("\n", 0, m.start()) + 1
        if "/" in c:
            ou = existe(c)
        else:
            ou = sorted({ref for ref in REFS for f in fichiers[ref] if f.endswith("/" + c) or f == c})
        chemins.append({"chemin": c, "ligne": ligne, "present_dans": ou})
    vus = {}
    for c in chemins:
        vus.setdefault(c["chemin"], c)
    res["pieces"][nom] = {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "empreintes": emp, "chemins": list(vus.values())}
print(json.dumps(res, ensure_ascii=False, indent=1))
