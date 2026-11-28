"""Témoin T2 (a) : que vérifie `controle_ia.prereg.problemes` ? Épreuve par mutations sur des copies des deux brouillons
(écrites dans le dossier de rendu, jamais dans le dépôt). Une mutation « vue » rend une liste non vide."""
import hashlib, json, re, sys
from pathlib import Path
from controle_ia.prereg import problemes

depot = Path("/home/user/controle-ia-travail/brouillons/prereg-v4-c-furtif-g1")
tmp = Path(sys.argv[1]); tmp.mkdir(parents=True, exist_ok=True)
pieces = {"G0": depot / "G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md",
          "G1": depot / "G1-architecture-h1-h2-v1-brouillon-gemini-1.md"}

def essai(nom, texte):
    p = tmp / f"{nom}.md"; p.write_text(texte, encoding="utf-8")
    return problemes(p)

HEX = re.compile(r"\b[0-9a-f]{64}\b")
def muts(t):
    cl = t.index("## Contre-lecture")
    faux = t[:cl] + HEX.sub(lambda m: hashlib.sha256(m.group(0).encode()).hexdigest(), t[cl:])
    return {
        # ce que la passation (§ 3, point 1) prête au validateur
        "p1_neuvieme_titre_##_ajoute (exactement 8 titres)": t.replace("## Seuil", "## Annexe libre\n\ntexte\n\n## Seuil", 1),
        "p2_sous_sections_en_####_au_lieu_de_###": re.sub(r"(?m)^### ", "#### ", t),
        "p2b_sous_sections_en_gras_sans_diese": re.sub(r"(?m)^### (.+)$", r"**\1**", t),
        "p3_FILS_BLAS_retire": t.replace("FILS_BLAS=1", "").replace("FILS_BLAS", "FILS"),
        "p4_SeedSequence_retiree": t.replace("SeedSequence", "graine"),
        "p5_sdpa_et_passe_recalcul_v6_retires": t.replace("sdpa", "eager").replace("passe_recalcul_v6", "autre_passe"),
        "p6_titre_numerote (## 1. Hypothèse)": t.replace("## Hypothèse", "## 1. Hypothèse", 1),
        "p7_une_seule_empreinte_par_contre_lecture": t[:cl] + re.sub(r"`[0-9a-f]{64}`", "`…`", t[cl:], count=0).replace("`…`", "`" + "a"*64 + "`"),
        # ce qu'il ne peut pas voir
        "q1_empreintes_de_la_contre_lecture_remplacees_par_des_empreintes_inventees": faux,
        "q2_toutes_les_empreintes_du_texte_inventees": HEX.sub(lambda m: hashlib.sha256(m.group(0).encode()).hexdigest(), t),
        "q3_chemins_inexistants": t.replace("src/controle_ia/", "src/nexiste_pas/"),
        "q4_corps_des_sections_remplace_par_un_mot": re.sub(r"(^## (?!Contre-lecture).+?$)(.*?)(?=^## )", lambda m: m.group(1) + "\n\nx\n\n", t, flags=re.M | re.S),
        "q5_seuil_contradictoire (0,00833 devient 0,5)": t.replace("0{,}00833", "0{,}5"),
    }

sortie = {}
for nom, chemin in pieces.items():
    t = chemin.read_text(encoding="utf-8")
    sortie[nom] = {"empreinte": hashlib.sha256(chemin.read_bytes()).hexdigest(), "intact": problemes(chemin), "mutations": {}}
    for k, v in muts(t).items():
        assert v != t or k.startswith("p3") , k
        sortie[nom]["mutations"][k] = {"texte_change": v != t, "problemes": essai(f"{nom}-{k[:2]}", v)}
print(json.dumps(sortie, indent=1, ensure_ascii=False))
