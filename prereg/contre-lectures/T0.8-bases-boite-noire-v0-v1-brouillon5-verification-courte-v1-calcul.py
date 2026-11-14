"""Calcul de la vérification courte du différentiel du brouillon 4 au brouillon 5 de T0.8 (vérificateur neuf, modèle B).

Lecture seule ; bibliothèque standard, `controle_ia.prereg` et `git show|ls-tree|log` (lecture) dans l'arbre de la branche.
Usage : PYTHONPATH=src python3 prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v1-calcul.py
(depuis /home/user/controle-ia-travail). N'écrit aucun fichier ; imprime un rapport JSON.
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

R = Path("/home/user/controle-ia-travail")
A = "/home/user/t08-code-compte4-v1"
D = R / "brouillons/t08-code-compte4-v1"
B4 = R / "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md"
B5 = R / "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon5.md"
COMMIT = "453a71e1c6729d7ec5d43e3a4a0e3522dfd38579"

def sha(b): return hashlib.sha256(b).hexdigest()
def shaf(p): return sha(Path(p).read_bytes())
def git(*a): return subprocess.run(["git", "-C", A, *a], check=True, capture_output=True).stdout

sortie = {}

# 1. Rejeu des couples sur le brouillon 4
t4, t5 = B4.read_text(encoding="utf-8"), B5.read_text(encoding="utf-8")
couples = json.loads((D / "couples-t08-brouillon5-v1.json").read_text(encoding="utf-8"))
def section_de(texte, pos):
    titres = [(m.start(), m.group(1).strip()) for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M)]
    nom = "(en-tête)"
    for debut, titre in titres:
        if debut <= pos: nom = titre
    return nom
t, journal = t4, []
for c in couples:
    n = t.count(c["ancien"])
    journal.append({"id": c["id"], "occurrences_avant": n, "section": section_de(t, t.find(c["ancien"])) if n else None,
                    "sha_ancien": sha(c["ancien"].encode())[:16], "sha_nouveau": sha(c["nouveau"].encode())[:16],
                    "long_ancien": len(c["ancien"]), "long_nouveau": len(c["nouveau"]),
                    "ancien_dans_b4_d_origine": t4.count(c["ancien"])})
    assert n == 1, c["id"]
    t = t.replace(c["ancien"], c["nouveau"], 1)
sortie["1_rejeu"] = {"sha_b4": shaf(B4), "sha_b5": shaf(B5), "sha_couples": shaf(D / "couples-t08-brouillon5-v1.json"),
                     "nombre_couples": len(couples), "ids": [c["id"] for c in couples],
                     "sha_rejeu": sha(t.encode("utf-8")), "rejeu_egal_b5_a_l_octet": t.encode("utf-8") == B5.read_bytes(),
                     "journal": journal}

# 1 bis. Les couples versés sont-ils ceux que le script v3 écrit avec les paramètres versés ? (fonction `couples` extraite, sans exécuter `principal`)
src = (D / "faire-couples-t08-brouillon5-v3.py").read_text(encoding="utf-8")
esp = {}
exec(compile(src.replace("\nprincipal()\n", "\n"), "faire-v3", "exec"), esp)
p = json.loads((D / "parametres-t08-brouillon5-v1.json").read_text(encoding="utf-8"))
regen = json.dumps(esp["couples"](p), ensure_ascii=False, indent=1) + "\n"
sortie["1bis_couples_regeneres_egaux"] = regen.encode("utf-8") == (D / "couples-t08-brouillon5-v1.json").read_bytes()
sortie["1bis_script_cite_par_le_brouillon_5"] = re.findall(r"faire-couples-t08-brouillon5-v\d+\.py", t5)

# 2. Sections, à l'octet
def decoupe(texte):
    m = re.split(r"^(## +.+?\s*)$", texte, flags=re.M)
    d = {"(en-tête)": m[0]}
    for titre, corps in zip(m[1::2], m[2::2]):
        assert titre.strip() not in d
        d[titre.strip()[3:].strip()] = corps
    return d
s4, s5 = decoupe(t4), decoupe(t5)
sortie["2_titres_egaux"] = list(s4)[1:] == list(s5)[1:]
sortie["2_sections"] = {k: {"egale_a_l_octet": s4[k] == s5[k], "sha4": sha(s4[k].encode())[:16], "sha5": sha(s5[k].encode())[:16],
                            "couples": [j["id"] for j in journal if j["section"] == k]} for k in s5}
plan4, plan5 = s4["Plan d'analyse"], s5["Plan d'analyse"]
c19 = next(c for c in couples if c["id"] == "T5-19")
ajout = c19["nouveau"][: len(c19["nouveau"]) - len(c19["ancien"])]
sortie["2_plan"] = {"t5_19_nouveau_finit_par_ancien": c19["nouveau"].endswith(c19["ancien"]),
                    "plan5_sans_l_ajout_egal_plan4": plan5.replace(ajout, "", 1) == plan4,
                    "ajout_une_seule_ligne": ajout.count("\n") == 1 and ajout.endswith("\n"), "longueur_ajout": len(ajout)}
l4, l5 = t4.split("\n"), t5.split("\n")
import difflib
ops = [(o, i1 + 1, i2, j1 + 1, j2) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, l4, l5, autojunk=False).get_opcodes() if o != "equal"]
sortie["2_lignes_changees"] = [{"op": o, "b4": [i1, i2], "b5": [j1, j2], "section_b5": section_de(t5, sum(len(x) + 1 for x in l5[: j1 - 1]))} for o, i1, i2, j1, j2 in ops]

# 4. Empreintes du code au commit
arbre = git("ls-tree", "-r", "--name-only", COMMIT, "--", "src/controle_ia/t08/", "tests/").decode().split("\n")
fichiers = sorted(f for f in arbre if (f.startswith("src/controle_ia/t08/") and f.endswith(".py")) or re.fullmatch(r"tests/test_t08_.*\.py", f))
autres_t08 = sorted(f for f in arbre if f.startswith("src/controle_ia/t08/") and not f.endswith(".py"))
piece = (D / "empreintes-code-t08-453a71e1-v1.md").read_text(encoding="utf-8")
table = {m.group(1): (int(m.group(2)), m.group(3)) for m in re.finditer(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \|$", piece, flags=re.M)}
recalc = {}
for f in fichiers:
    b = git("show", f"{COMMIT}:{f}")
    recalc[f] = (b.count(b"\n"), sha(b))
sortie["4_code"] = {"commit_complet_resolu": git("rev-parse", "--verify", COMMIT + "^{commit}").decode().strip(),
                    "n_fichiers_arbre": len(fichiers), "n_fichiers_piece": len(table),
                    "memes_fichiers": sorted(table) == fichiers, "fichiers_non_py_sous_t08": autres_t08,
                    "ecarts": {f: {"piece": table.get(f), "recalcul": recalc.get(f)} for f in sorted(set(table) | set(recalc)) if table.get(f) != recalc.get(f)},
                    "tests_tous_en_v1": all(re.fullmatch(r"tests/test_t08_.*_v1\.py", f) for f in fichiers if f.startswith("tests/")),
                    "commit_dans_b5": t5.count(COMMIT), "sha_piece": shaf(D / "empreintes-code-t08-453a71e1-v1.md"),
                    "sha_piece_dans_b5": t5.count(shaf(D / "empreintes-code-t08-453a71e1-v1.md"))}

# 4 bis. Empreintes des pièces citées par les passages neufs
cites = {
    "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md": R,
    "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon3.md": R,
    "prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon3-verification-courte-v1.md": R,
    "brouillons/t08-code-compte4-v1/empreintes-code-t08-453a71e1-v1.md": R,
    "brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1.md": R,
    "brouillons/t08-code-compte4-v1/verification-courte-corrections-t08-v1.md": R,
    "brouillons/t08-code-compte4-v1/verification-corrections-2-t08-v1.md": R,
    "registres-provisoires/compte-4-2026-11-14-v3.md": R,
    "registres-provisoires/compte-4-2026-11-14-v6.md": R,
    "docs/notes/t08-code-compte4-v1/rapport-developpeur-t08-v1.md": Path(A),
    "docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-t08-v1.md": Path(A),
    "docs/notes/t08-code-compte4-v1/rapport-developpeur-corrections-2-t08-v1.md": Path(A),
}
neuf = "".join(c["nouveau"] for c in couples)
res = {}
for ch, racine in cites.items():
    f = racine / ch
    e = {"existe": f.exists()}
    if f.exists():
        h = shaf(f)
        comp = Path(str(f) + ".sha256")
        e.update({"sha": h, "sha_dans_passages_neufs": neuf.count(h), "sha_dans_b5": t5.count(h),
                  "compagnon": (comp.read_text().split()[0] == h) if comp.exists() else "absent"})
        if racine == Path(A):
            try: e["sha_au_commit_453a71e1"] = sha(git("show", f"{COMMIT}:{ch}"))
            except subprocess.CalledProcessError: e["sha_au_commit_453a71e1"] = "absent du commit"
    res[ch] = e
sortie["4bis_pieces_citees"] = res
sortie["4bis_empreintes_des_passages_neufs"] = sorted(set(re.findall(r"\b[0-9a-f]{64}\b", neuf)))
connues = {e.get("sha") for e in res.values()}
sortie["4bis_empreintes_neuves_non_rattachees"] = sorted(set(re.findall(r"\b[0-9a-f]{64}\b", neuf)) - connues - set(re.findall(r"\b[0-9a-f]{64}\b", t4)))
sortie["4bis_commits_cites_passages_neufs"] = sorted(set(re.findall(r"\b[0-9a-f]{40}\b", neuf)))

# 5. Identifiants de modèles
motif = re.compile(r"(?i)claude|opus|fable|sonnet|haiku|anthropic|gpt|gemini")
sortie["5_identifiants"] = {"b4": [[i + 1, m.group(0), l[max(0, m.start() - 40): m.end() + 40]] for i, l in enumerate(l4) for m in motif.finditer(l)],
                            "b5": [[i + 1, m.group(0), l[max(0, m.start() - 40): m.end() + 40]] for i, l in enumerate(l5) for m in motif.finditer(l)],
                            "modele_A_b5": t5.count("modèle A"), "modele_B_b5": t5.count("modèle B"),
                            "modele_A_b4": t4.count("modèle A"), "modele_B_b4": t4.count("modèle B")}

# 6. Forme
sys.path.insert(0, str(R / "src"))
from controle_ia.prereg import problemes, GABARIT
sortie["6_forme"] = {"problemes_b5": problemes(B5), "problemes_b4": problemes(B4),
                     "marqueurs_b5": {m: t5.count(m) for m in sorted(set(GABARIT.findall(t5)))},
                     "COMMIT_CODE_T08_nu_dans_b5": t5.count("COMMIT_CODE_T08")}
print(json.dumps(sortie, ensure_ascii=False, indent=1))
