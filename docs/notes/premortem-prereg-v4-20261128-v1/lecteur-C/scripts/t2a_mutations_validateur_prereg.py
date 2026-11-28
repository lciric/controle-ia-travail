"""T2(a) — que vérifie `controle_ia.prereg.problemes` ? Mutations des deux brouillons (copies dans un dossier
temporaire, le dépôt n'est pas touché) : pour chaque propriété que la passation v4 (§ 3, point 1) prête au
validateur, on la viole et on regarde si `problemes` le voit."""
import hashlib, json, re, sys, tempfile
from pathlib import Path
from controle_ia import prereg

BROUILLONS = [Path(p) for p in sys.argv[1:3]]
SORTIE = Path(sys.argv[3])

def muter(texte, nom):
    if nom == "aucune (texte tel quel)": return texte
    if nom == "FILS_BLAS retiré partout": return texte.replace("FILS_BLAS", "FILS_XXXX")
    if nom == "SeedSequence retiré partout": return texte.replace("SeedSequence", "GenerateurQuelconque")
    if nom == "passe_recalcul_v6 et sdpa retirés": return texte.replace("passe_recalcul_v6", "passe_quelconque").replace("sdpa", "eager")
    if nom == "sous-sections ### devenues ####": return re.sub(r"(?m)^### ", "#### ", texte)
    if nom == "neuvième section ## ajoutée": return texte + "\n## Section en plus\n\nTexte.\n"
    if nom == "section Hypothèse en double": return texte + "\n## Hypothèse\n\nSeconde hypothèse contraire.\n"
    if nom == "empreintes de Contre-lecture remplacées par deux chaînes arbitraires":
        tete, _, cl = texte.rpartition("## Contre-lecture")
        k = [0]
        def r(m):
            k[0] += 1
            return ("a" if k[0] % 2 else "b") * 64
        return tete + "## Contre-lecture" + re.sub(r"\b[0-9a-f]{64}\b", r, cl)
    if nom == "Contre-lecture réduite à deux empreintes sans aucun nom de lecteur ni de rapport":
        tete, _, _ = texte.rpartition("## Contre-lecture")
        return tete + "## Contre-lecture\n\n" + "a" * 64 + " " + "b" * 64 + "\n"
    if nom == "toutes les autres empreintes du texte faussées (un chiffre changé)":
        tete, _, cl = texte.rpartition("## Contre-lecture")
        return re.sub(r"\b([0-9a-f]{63})([0-9a-f])\b", lambda m: m.group(1) + ("0" if m.group(2) != "0" else "1"), tete) + "## Contre-lecture" + cl
    if nom == "seuils et effectifs contradictoires (64 tâches devient 6 tâches)": return texte.replace("$64$", "$6$").replace("T=64", "T=6")
    if nom == "titre numéroté (## 1. Hypothèse)": return texte.replace("## Hypothèse", "## 1. Hypothèse", 1)
    if nom == "section Liste d'arrêt retirée":
        return re.sub(r"(?ms)^## Liste d'arrêt.*?(?=^## Contre-lecture)", "", texte)
    if nom == "section Seuil vidée":
        return re.sub(r"(?ms)^## Seuil\s*\n.*?(?=^## Plan d'analyse)", "## Seuil\n\n", texte)
    if nom == "marqueur À REMPLIR dans Métrique": return texte.replace("## Métrique", "## Métrique\n\nÀ REMPLIR", 1)
    if nom == "marqueur de gabarit <<SEUIL>>": return texte.replace("## Seuil", "## Seuil\n\n<<SEUIL>>", 1)
    if nom == "Contre-lecture à une seule empreinte":
        tete, _, _ = texte.rpartition("## Contre-lecture")
        return tete + "## Contre-lecture\n\n- **Contre-lecture 1** : " + "a" * 64 + "\n"
    raise ValueError(nom)

MUTATIONS = [
    ("aucune (texte tel quel)", "témoin"),
    ("FILS_BLAS retiré partout", "prêté par la passation"),
    ("SeedSequence retiré partout", "prêté par la passation"),
    ("passe_recalcul_v6 et sdpa retirés", "prêté par la passation"),
    ("sous-sections ### devenues ####", "prêté par la passation"),
    ("neuvième section ## ajoutée", "prêté par la passation (« exactement 8 »)"),
    ("section Hypothèse en double", "prêté par la passation (« exactement 8 »)"),
    ("empreintes de Contre-lecture remplacées par deux chaînes arbitraires", "sens de R2"),
    ("Contre-lecture réduite à deux empreintes sans aucun nom de lecteur ni de rapport", "sens de R2"),
    ("toutes les autres empreintes du texte faussées (un chiffre changé)", "fond"),
    ("seuils et effectifs contradictoires (64 tâches devient 6 tâches)", "fond"),
    ("titre numéroté (## 1. Hypothèse)", "vérifié réellement"),
    ("section Liste d'arrêt retirée", "vérifié réellement"),
    ("section Seuil vidée", "vérifié réellement"),
    ("marqueur À REMPLIR dans Métrique", "vérifié réellement"),
    ("marqueur de gabarit <<SEUIL>>", "vérifié réellement"),
    ("Contre-lecture à une seule empreinte", "vérifié réellement"),
]
out = {"module": "src/controle_ia/prereg.py", "module_sha256": hashlib.sha256(Path(prereg.__file__).read_bytes()).hexdigest(), "brouillons": {}}
with tempfile.TemporaryDirectory() as tmp:
    for b in BROUILLONS:
        t0 = b.read_text(encoding="utf-8")
        lignes = []
        for nom, classe in MUTATIONS:
            t = muter(t0, nom)
            p = Path(tmp) / "mutant.md"; p.write_text(t, encoding="utf-8")
            pb = prereg.problemes(p)
            lignes.append({"mutation": nom, "classe": classe, "texte_change": t != t0, "vu_par_problemes": bool(pb), "problemes": pb})
        # la branche « entrées Contre-lecture k » du validateur est-elle seulement exercée sur ces brouillons ?
        cl = prereg.sections(t0).get("Contre-lecture", "")
        out["brouillons"][b.name] = {"sha256": hashlib.sha256(b.read_bytes()).hexdigest(), "mutations": lignes,
            "entrees_contre_lecture_reconnues_par_le_validateur": len(list(prereg.ENTREE.finditer(cl))),
            "empreintes_distinctes_dans_la_section": len(set(prereg.EMPREINTE.findall(cl))),
            "empreinte_du_brouillon_lui_meme_citee_dans_sa_section": False,
            "empreintes_citees": sorted(set(x[:8] for x in prereg.EMPREINTE.findall(cl)))}
SORTIE.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
for n, d in out["brouillons"].items():
    print("==", n, d["sha256"][:8], "| entrées reconnues:", d["entrees_contre_lecture_reconnues_par_le_validateur"], "| empreintes citées:", d["empreintes_citees"])
    for l in d["mutations"]:
        print(f"  [{'VU ' if l['vu_par_problemes'] else 'non'}] ({l['classe']}) {l['mutation']} {'' if l['texte_change'] or l['mutation'].startswith('aucune') else ' !! mutation sans effet sur le texte'} {l['problemes'] if l['problemes'] else ''}")
