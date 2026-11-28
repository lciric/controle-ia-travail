"""É0 — contrôle par programme de la pièce (G1) : empreintes (longueur, présence au dépôt, fichier désigné), chemins,
versions, et accord avec le texte des arbitrages (D) et le registre des accords. Aucun fichier interdit n'est ouvert :
pour les archives de sondes, de planchers et les verdicts de sondes, seuls les compagnons `.sha256` et les textes
qui citent l'empreinte sont cherchés (noms et empreintes)."""
import hashlib, json, re, subprocess, sys
from pathlib import Path

D = Path("/home/user/controle-ia-travail")
G1 = D / "brouillons/prereg-v4-c-furtif-g1/G1-architecture-h1-h2-v1-brouillon-gemini-1.md"
ARB = D / "brouillons/prereg-v4-c-furtif-g1/arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md"
t = G1.read_text(encoding="utf-8")
COMMITS = ["HEAD", "42cdfcf29", "5817bb0a5"]
INTERDITS = (".npz", ".safetensors", ".pt")

def git(*a):
    return subprocess.run(["git", "-C", str(D), *a], capture_output=True, text=True).stdout

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

# nom que le brouillon associe à chaque empreinte, et chemin attendu au dépôt (None : à chercher)
ATTENDU = {
 "85bd40235f3668c66adffc2ff18139ff1a0c402f3aaa24cca70db0217f755bf0": ("N-026", "docs/decisions/decision-N-026-v1.md"),
 "084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4": ("N-029", "docs/decisions/decision-N-029-v1.md"),
 "c8a00b3f885ae3e9c4f1971dd620fbb64389a4557e6f24d3520b1c56deba4c2f": ("N-054", "docs/decisions/decision-N-054-v1.md"),
 "3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d": ("N-056 / decision-N-056-v1.md", "docs/decisions/decision-N-056-v1.md"),
 "012ddc44baca981620ff2a81211998fd437f6b336436d33406b119227c406628": ("P-066", "docs/decisions/proposition-P-066-saboteur-diffus-par-construction-v1.md"),
 "76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d622bdad4c37755e67e": ("taches-evaluation.json", None),
 "0e9e39f249a16976918f6564b8830bc894c89659": ("révision de meta-llama/Llama-3.1-8B-Instruct", None),
 "d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5": ("prereg/T0.7-sondes-v0-v1.md", "prereg/T0.7-sondes-v0-v1.md"),
 "64946a47db66ea8c8257f21a14d0433de275dd505b63cd378012159df9af1914": ("src/controle_ia/bases/scores_jetons.py", "src/controle_ia/bases/scores_jetons.py"),
 "b329f9b5ac93d8a8648eef4643843acf5abe0e936164534afacc130ce9a6f5dd": ("src/controle_ia/bases/bris_egalite_v1.py", "src/controle_ia/bases/bris_egalite_v1.py"),
 "35a0983404d7a10d0bb736fa37307a108501785a207c27346be1cd02bab11ba8": ("src/controle_ia/bases/sequentiel.py", "src/controle_ia/bases/sequentiel.py"),
 "4bf4ef35a2c734d19e67f02235c6dc4302ff1b89fd1fccf23b800dae68373ea6": ("src/controle_ia/bases/trace_lite.py", "src/controle_ia/bases/trace_lite.py"),
 "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4": ("tokenizer.json", None),
 "1040674cb321766a0e2a7fa1e0c610384df6c4fac4109dd50c42dfbb03181ed3": ("evaluation.py", "src/controle_ia/sondes/evaluation.py"),
 "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796": ("plancher_v2.py", "src/controle_ia/t07/plancher_v2.py"),
 "701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60": ("« activations et projections » (1)", None),
 "94ca013c66e5dbd35b3ea55ec8aa4eb7b299e5dd63a95f7ccea7ced8d120f224": ("« activations et projections » (2)", None),
 "374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79": ("« activations et projections » (3)", None),
 "f3228b4b25a5140b3b8fa8c7ac994a727d61f9d986b0539f8ea5956eb5fba30a": ("src/controle_ia/barreau8_moniteurs/passe_recalcul_v6.py", "src/controle_ia/barreau8_moniteurs/passe_recalcul_v6.py"),
 "29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e": ("config.json", None),
 "189fb0c0d7fd8a527db217c0a60a0e013f0394cd8800f9697a666a9e75e5f7fd": ("generation_config.json", None),
 "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424": ("tokenizer_config.json", None),
 "9b33c624fe9c4be2909cee9ea764f6e19d31e7767affd64bb6f763d0032a1e5c": ("verdict-P3-bis-v1.md", None),
 "c3a017ce1e8b0c41dee1e430f142590e88bd7104eada02b3a973ac98c0da28d0": ("verdict-P3-bis-v1-issue.json", None),
 "8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4": ("prereg/lecture-sondes-barreau8-v1.md", "prereg/lecture-sondes-barreau8-v1.md"),
 "8325ba1c052db3d9b6431265e37f03b1014fae6b2e391948edce231a1952a30d": ("contre-lecture-r2-etages-1-2-v1.md", "registres/contre-lectures/contre-lecture-r2-etages-1-2-20261128-v1.md"),
 "893eee8ff515b02a7dd70f7de9f62fb2037f9d76b4ad5acd590b6b035a4e5c0c": ("test_oracles_r5_cloture_etages_1_2.py", "tests/test_oracles_r5_cloture_etages_1_2.py"),
 "59a2a571c687da0e1a6c84cd3e2bc5f9cb3a8e016bbcc4bb3f52d6f0b61020ac": ("contre-epreuve-r2-volets-11-13-v1.md", "registres/contre-lectures/contre-epreuve-r2-volets-11-13-20261128-v1.md"),
 "a39bdffe76bb444d5700499fbc1d1ed354f23119370e8ad4a8b40a4c0732ec28": ("test_contre_epreuve_v4_r5.py", "tests/test_contre_epreuve_v4_r5.py"),
 "3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306": ("src/controle_ia/prereg.py", "src/controle_ia/prereg.py"),
}
cites = sorted(set(re.findall(r"[0-9a-f]{38,}", t)))
assert set(cites) == set(ATTENDU), set(cites) ^ set(ATTENDU)

def ou(h):
    """Fichiers du dépôt qui portent cette chaîne : compagnons .sha256 d'abord (ils nomment le fichier désigné)."""
    res = {}
    for c in COMMITS:
        l = git("grep", "-I", "-l", "-F", h, c, "--", ".").split()
        comp = [x.split(":", 1)[1] for x in l if x.endswith(".sha256")]
        res[c] = {"compagnons": comp[:4], "nb_compagnons": len(comp), "nb_textes": len(l)}
    return res

lignes = []
for h in cites:
    nom, chemin = ATTENDU[h]
    r = {"empreinte": h, "longueur": len(h), "nom_dans_le_brouillon": nom}
    r["longueur_valide"] = len(h) in (40, 64)
    if chemin:
        p = D / chemin
        r["chemin_au_depot"] = chemin
        r["existe"] = p.exists()
        if p.exists() and not chemin.endswith(INTERDITS):
            r["empreinte_recalculee_egale"] = (sha(p) == h)
            if not r["empreinte_recalculee_egale"]:
                r["empreinte_du_fichier"] = sha(p)
        r["nom_du_brouillon_egal_au_nom_du_fichier"] = (Path(chemin).name == Path(nom.split(" / ")[-1]).name)
    else:
        o = ou(h)
        r["trouvee"] = {c: v for c, v in o.items() if v["nb_textes"]}
        if not r["trouvee"] and len(h) == 65:      # essais de voisinage : un caractère en trop
            vois = {}
            for i in range(len(h)):
                c = h[:i] + h[i + 1:]
                l = git("grep", "-I", "-l", "-F", c, "HEAD", "--", ".").split()
                if l: vois[c] = {"position_du_caractere_en_trop": i, "exemples": [x.split(":", 1)[1] for x in l if x.endswith(".sha256")][:3] or [x.split(":", 1)[1] for x in l][:3]}
            r["voisines_a_un_caractere_pres"] = vois
    lignes.append(r)

# chemins cités entre accents graves
chemins = sorted(set(m for m in re.findall(r"`([A-Za-z0-9_./\-]+\.(?:py|md|json|npz|safetensors|txt))`", t)))
etat_chemins = []
for c in chemins:
    p = D / c
    if p.exists(): etat_chemins.append({"chemin": c, "etat": "existe (chemin complet)"})
    else:
        ici = [x for x in git("ls-files", f"*{Path(c).name}").split() if Path(x).name == Path(c).name]
        etat_chemins.append({"chemin": c, "etat": ("nom nu, trouvé à : " + " ; ".join(ici[:3])) if ici else "absent du dépôt (HEAD)"})

# versions de bibliothèques
vers = {}
for lib, v in (("transformers", "5.18.0"), ("tokenizers", "0.23.2")):
    occ = git("grep", "-I", "-h", "-E", rf"^{lib}==", "HEAD", "--", "requirements*.txt").split()
    vers[lib] = {"brouillon": v, "fichiers_requirements_du_depot": sorted(set(occ))}

# accord avec le registre des accords et le texte (D)
go = (D / "registres/go.md").read_text(encoding="utf-8")
lg = {k: next(l for l in go.splitlines() if l.startswith(f"| {k} ")) for k in ("GO-2026-11-28-02", "GO-2026-11-28-03")}
arb = ARB.read_text(encoding="utf-8")
def present(mot, texte): return bool(re.search(mot, texte))
MOTS = {  # choix décisifs du brouillon (G1) : sont-ils dans le texte (D) ? dans la ligne du registre ?
 "H1 globale seule primaire": (r"global est seul primaire|seul primaire", r"seul primaire|global"),
 "saboteur soutenu S_soutenu porteur de H1": (r"S_\{\\text\{soutenu\}\}", r"soutenu"),
 "combinaison ½(LLM + lex), γ = 1": (r"\\gamma = 1", r"gamma|γ"),
 "analyse du juge ≤ 256 jetons": (r"256", r"256"),
 "LEACE TSQR + post-max": (r"LEACE", r"LEACE"),
 "gain net face à J (H2)": (r"gain net positif face à \$?J", r"gain net"),
 "S1-G1 (écart de sabotage ≥ 0,25)": (r"S1-G1", r"S1-G1"),
 "S_G2N-top4, π0 = 0,25, τ0 = 0,85": (r"\\tau_0=0\{,\}85|tau_0", r"0,85|tau_0"),
 "six comparateurs (S_last, S_max, S_casc-cont, S_BB-seq, S_BB-max, TRACE-lite)": (r"S_\{\\text\{casc-cont\}\}", r"casc|cascade"),
 "plafond 65 USD et 30 h": (r"65\s*\\?text\{? ?USD|65 USD", r"65 USD"),
 "pari apparié (N-055)": (r"pari appari", r"pari appari"),
 "référence honnête m, n, source (N-076)": (r"N-076", r"N-076"),
 "treize décisions du 5 novembre (GO-2026-11-05-07)": (r"GO-2026-11-05-07|DG1-", r"GO-2026-11-05-07|DG1-"),
 "témoin apparié (N-074, GO-2026-11-18-48)": (r"N-074|GO-2026-11-18-48", r"N-074|GO-2026-11-18-48"),
 "banc exécutable de N-060 v3 point 5": (r"N-060", r"N-060"),
}
accord = []
for nom, (m_arb, m_go) in MOTS.items():
    accord.append({"choix": nom, "dans_le_brouillon_G1": present(m_arb, t) or present(m_go, t),
                   "dans_le_texte_des_arbitrages": present(m_arb, arb) or present(m_go, arb),
                   "dans_la_ligne_GO_02": present(m_go, lg["GO-2026-11-28-02"]), "dans_la_ligne_GO_03": present(m_go, lg["GO-2026-11-28-03"])})
decisions_citees = sorted(set(re.findall(r"`(N-\d+|P-\d+|GO-\d{4}-\d\d-\d\d-\d+)`", t)))
couts = {"montants_USD_dans_le_texte_D": sorted(set(re.findall(r"(\d[\d ]*)\s*(?:\\text\{ ?USD\}|USD)", arb))),
         "durees_dans_le_texte_D": sorted(set(re.findall(r"[~+]?\d+\s*(?:h|min) GPU[^,;)]*", arb)))}
sortie = {"piece": str(G1.relative_to(D)), "sha256": sha(G1), "empreintes": lignes, "chemins": etat_chemins, "versions": vers,
          "decisions_et_accords_cites_par_le_brouillon": decisions_citees, "accord_brouillon_texte_registre": accord, "couts_chiffres_dans_D": couts}
print(json.dumps(sortie, indent=1, ensure_ascii=False))
