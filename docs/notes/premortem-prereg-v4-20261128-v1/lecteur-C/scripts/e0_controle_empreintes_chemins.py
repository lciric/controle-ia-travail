"""É0 — contrôle par programme des empreintes et des chemins cités par les trois pièces.
Pour chaque suite hexadécimale d'au moins 7 chiffres : longueur ; forme (entière, abrégée par « … ») ; présence au dépôt
(compagnons .sha256 de l'arbre de travail, puis recherche du texte dans l'arbre, puis aux commits 42cdfcf29, 5817bb0a5 et sur
la branche de la banque) ; fichier désigné par le compagnon ; recalcul de l'empreinte quand le fichier est sur disque et
n'est pas d'un type fermé (*.npz, *.safetensors, consigne privée : jamais ouverts, compagnon seulement).
Pour chaque chemin entre accents graves : présence dans l'arbre de travail ou aux mêmes commits."""
import hashlib, json, os, re, subprocess, sys
from pathlib import Path

RACINE = Path(sys.argv[1]); PIECES = [Path(p) for p in sys.argv[2:5]]; SORTIE = Path(sys.argv[5])
REFS = ["42cdfcf29", "5817bb0a5", "origin/banque/dose-reponse-consigne-cachee-v1"]
FERMES = re.compile(r"\.(npz|npy|safetensors)$|consignes?-privees?|consigne-privee|P3-consignes|ii-b-saboteur-budget", re.I)

def git(*a):
    return subprocess.run(["git", "-C", str(RACINE), *a], capture_output=True, text=True).stdout

# index des compagnons de l'arbre de travail
index = {}
for dossier, _, fichiers in os.walk(RACINE):
    if "/.git" in dossier: continue
    for f in fichiers:
        if f.endswith(".sha256"):
            p = Path(dossier) / f
            try: ligne = p.read_text(errors="replace").split()
            except OSError: continue
            if ligne and re.fullmatch(r"[0-9a-f]{64}", ligne[0]):
                index.setdefault(ligne[0], []).append(str((Path(dossier) / f[:-7]).relative_to(RACINE)))

def sha_fichier(rel):
    p = RACINE / rel
    if not p.is_file(): return None
    if FERMES.search(rel): return "non recalculée (type fermé : compagnon seul)"
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for bloc in iter(lambda: fh.read(1 << 20), b""): h.update(bloc)
    return h.hexdigest()

def chercher(jeton):
    """Où le jeton figure-t-il ? (arbre de travail : compagnons, puis texte ; puis refs)"""
    r = {"compagnons": index.get(jeton, [])[:6]}
    if len(jeton) == 64 and r["compagnons"]:
        rel = r["compagnons"][0]
        r["recalcul"] = sha_fichier(rel)
        r["recalcul_egal"] = (r["recalcul"] == jeton) if r["recalcul"] and len(r["recalcul"]) == 64 else None
    g = git("grep", "-l", "-F", "-I", jeton, "--", ".", ":!brouillons/prereg-v4-c-furtif-g1").split("\n")
    r["texte_arbre"] = [x for x in g if x][:6]
    r["texte_arbre_n"] = len([x for x in g if x])
    if not r["compagnons"] and not r["texte_arbre"]:
        for ref in REFS:
            g = git("grep", "-l", "-F", "-I", jeton, ref, "--", "registres", "runs", "diag", "docs/verdicts", "donnees", "prereg").split("\n")
            g = [x for x in g if x]
            if g:
                r.setdefault("texte_refs", {})[ref] = g[:4]
    return r

HEX = re.compile(r"(?<![0-9a-zA-Z])([0-9a-f]{7,})(?![0-9a-zA-Z])(…|\.\.\.)?")
CHEMIN = re.compile(r"`([^`\s]+)`")
out = {}
for piece in PIECES:
    texte = piece.read_text(encoding="utf-8")
    lignes = texte.split("\n")
    vus, jetons = {}, []
    for nl, ligne in enumerate(lignes, 1):
        for m in HEX.finditer(ligne):
            j, abrege = m.group(1), bool(m.group(2))
            if j.isdigit() and len(j) < 16: continue        # nombres décimaux (ex. 0,00833 sans virgule : exclus)
            cle = (j, abrege)
            if cle in vus: vus[cle]["lignes"].append(nl); continue
            avant = ligne[max(0, m.start() - 110):m.start()].replace("`", "")
            d = {"jeton": j, "longueur": len(j), "abrege": abrege, "lignes": [nl], "contexte_avant": avant[-110:]}
            if abrege:
                complets = sorted({k for k in index if k.startswith(j)})
                d["prefixe_de"] = complets[:3]; d["prefixe_unique_parmi_les_compagnons"] = len(complets) == 1
                if not complets:
                    g = [x for x in git("grep", "-l", "-F", "-I", j, "--", "registres", "runs", "diag").split("\n") if x]
                    d["prefixe_dans_registres"] = g[:4]
                elif len(complets) == 1:
                    d["designe"] = index[complets[0]][:3]
            else:
                d["forme"] = {64: "sha256", 40: "sha1 (révision)"}.get(len(j), "LONGUEUR ANORMALE")
                d.update(chercher(j))
            vus[cle] = d; jetons.append(d)
    chemins = []
    for nl, ligne in enumerate(lignes, 1):
        for m in CHEMIN.finditer(ligne):
            c = m.group(1).strip(".,;:()")
            if not re.search(r"[A-Za-z]", c) or " " in c: continue
            if not (("/" in c and re.search(r"\.[a-z0-9]{2,11}$|/$", c)) or re.search(r"\.(md|py|json|jsonl|npz|safetensors|txt)$", c)): continue
            if any(x["chemin"] == c for x in chemins): continue
            e = {"chemin": c, "ligne": nl, "dans_arbre": (RACINE / c).exists()}
            if not e["dans_arbre"]:
                base = c.split("/")[-1]
                trouve = [x for x in git("ls-files", "--", f"*{base}").split("\n") if x and x.endswith(base)]
                e["meme_nom_dans_arbre"] = trouve[:4]
                if not trouve and "/" in c:
                    for ref in REFS:
                        if git("ls-tree", "--name-only", ref, "--", c).strip():
                            e.setdefault("present_a", []).append(ref)
                if not trouve and "/" not in c:
                    for ref in REFS:
                        g = [x for x in git("ls-tree", "-r", "--name-only", ref).split("\n") if x.endswith("/" + base) or x == base]
                        if g: e.setdefault("present_a", {})[ref] = g[:2] if isinstance(e.get("present_a"), dict) else None
            chemins.append(e)
    out[piece.name] = {"sha256": hashlib.sha256(piece.read_bytes()).hexdigest(), "jetons": jetons, "chemins": chemins}
SORTIE.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
for nom, d in out.items():
    print("=" * 20, nom, d["sha256"][:8], "| jetons hexadécimaux distincts :", len(d["jetons"]))
    for j in d["jetons"]:
        if j["abrege"]:
            etat = "abrégé ; " + ("désigne " + str(j.get("designe")) if j.get("designe") else ("préfixe de %d compagnons" % len(j["prefixe_de"]) if j["prefixe_de"] else "AUCUN compagnon ; registres : " + str(j.get("prefixe_dans_registres"))))
        elif j["forme"] == "LONGUEUR ANORMALE":
            etat = "!!! LONGUEUR %d" % j["longueur"]
        else:
            ou = j["compagnons"][:2] or j["texte_arbre"][:2] or j.get("texte_refs")
            etat = j["forme"] + " ; " + ("compagnon de " + str(j["compagnons"][:2]) + (" ; recalcul égal" if j.get("recalcul_egal") else (" ; recalcul : " + str(j.get("recalcul"))[:40])) if j["compagnons"] else ("PAS de compagnon ; cité dans " + str(ou) if ou else "!!! INTROUVABLE au dépôt"))
        print(f"  l.{j['lignes'][0]:>3} {j['jeton'][:12]}{'…' if len(j['jeton'])>12 else ''} [{j['longueur']}] {etat}\n        contexte : …{j['contexte_avant'][-70:]}")
    print("  -- chemins :", len(d["chemins"]))
    for c in d["chemins"]:
        if not c["dans_arbre"]:
            print("   ABSENT de l'arbre :", c["chemin"], "| même nom :", c.get("meme_nom_dans_arbre"), "| refs :", c.get("present_a"))
