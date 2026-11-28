"""T2(a) — `controle_ia.prereg.problemes` verifie-t-il tout ce que la passation v4 lui prete (§ 3, point 1) ?
La passation ecrit : « exactement les 8 titres ## litteraux non numerotes (...), ## Contre-lecture portant au moins
2 SHA-256 a 64 caracteres, sous-sections en ### uniquement, FILS_BLAS = 1, SeedSequence nommee, et recalcul sdpa via
passe_recalcul_v6.py ». Epreuve : le validateur du depot (3b2e3ee5...) est joue sur les deux brouillons, puis sur des
mutants ecrits dans un dossier temporaire ; un mutant « vu » rend une liste non vide."""
import hashlib, json, pathlib, re, sys, tempfile
from controle_ia import prereg

depot = pathlib.Path(sys.argv[1])
B = depot / "brouillons" / "prereg-v4-c-furtif-g1"
pieces = {"G0": B / "G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md", "G1": B / "G1-architecture-h1-h2-v1-brouillon-gemini-1.md"}
res = {"prereg_py_sha256": hashlib.sha256((depot / "src/controle_ia/prereg.py").read_bytes()).hexdigest(), "pieces": {}, "mutants": {}}
tmp = pathlib.Path(tempfile.mkdtemp(prefix="t2a-"))
def joue(nom, texte):
    p = tmp / (nom + ".md"); p.write_text(texte, encoding="utf-8")
    return prereg.problemes(p)
for nom, p in pieces.items():
    t = p.read_text(encoding="utf-8")
    cl = prereg.sections(t).get("Contre-lecture", "")
    res["pieces"][nom] = {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "problemes": prereg.problemes(p),
                          "titres_niveau_2": re.findall(r"^## +(.+?)\s*$", t, flags=re.M),
                          "entrees_contre_lecture_reconnues": len(list(prereg.ENTREE.finditer(cl))),
                          "empreintes_distinctes_dans_la_section": len(set(prereg.EMPREINTE.findall(cl))),
                          "empreinte_du_brouillon_citee_dans_sa_section": hashlib.sha256(p.read_bytes()).hexdigest() in cl}
t0 = pieces["G0"].read_text(encoding="utf-8")
M = {}
# ce que la passation prete au validateur
M["sans FILS_BLAS (toutes les mentions retirees)"] = t0.replace("FILS_BLAS=1", "").replace("FILS_BLAS", "")
M["sans SeedSequence (toutes les mentions retirees)"] = t0.replace("SeedSequence", "generateur")
M["sans passe_recalcul_v6 ni sdpa"] = t0.replace("passe_recalcul_v6.py", "une_passe.py").replace("sdpa", "eager")
M["sous-sections en #### au lieu de ###"] = re.sub(r"(?m)^### ", "#### ", t0)
M["un neuvieme titre de niveau 2 ajoute"] = t0 + "\n## Annexe libre\n\ntexte\n"
M["section Contre-lecture : empreintes remplacees par deux empreintes inventees (aaaa..., bbbb...)"] = (
    t0[:t0.index("## Contre-lecture")] + "## Contre-lecture\n\n" + "a" * 64 + " " + "b" * 64 + "\n")
M["section Contre-lecture : une seule empreinte, repetee"] = (
    t0[:t0.index("## Contre-lecture")] + "## Contre-lecture\n\n" + "a" * 64 + " " + "a" * 64 + "\n")
M["chaque empreinte de 64 chiffres du texte alteree d'un chiffre (toutes fausses)"] = re.sub(
    r"\b([0-9a-f]{63})([0-9a-f])\b", lambda m: m.group(1) + ("0" if m.group(2) != "0" else "1"), t0)
M["seuil 0,50 remplace par 0,05 partout (regle de decision changee)"] = t0.replace("0{,}50", "0{,}05")
# ce que le validateur verifie vraiment
M["titre numerote (## 1. Hypothese)"] = t0.replace("## Hypothèse", "## 1. Hypothèse")
M["section Seuil videe"] = re.sub(r"(?s)## Seuil\n.*?## Plan d'analyse", "## Seuil\n\n## Plan d'analyse", t0)
M["marqueur A REMPLIR dans le texte"] = t0.replace("## Métrique", "## Métrique\n\nÀ REMPLIR")
M["marqueur de gabarit <<EMPREINTE>>"] = t0.replace("## Métrique", "## Métrique\n\n<<EMPREINTE>>")
for nom, t in M.items():
    pb = joue(re.sub(r"\W+", "-", nom)[:60], t)
    res["mutants"][nom] = {"vu": bool(pb), "problemes": pb}
res["verdict"] = ("FAUX : le validateur ne controle que la presence et la non-vacuite de huit titres, l'absence de marqueurs, et "
                  "deux chaines de 64 chiffres hexadecimaux distinctes dans la section Contre-lecture")
print(json.dumps(res, ensure_ascii=False, indent=1))
