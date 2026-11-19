"""Verification des corrections du brouillon 2 (texte neuf « validite de l'adaptateur pour les sondes apprises sur la tache »
et son devis), par un verificateur neuf (Claude Opus 5.5). Programme ecrit a neuf ; l'outil d'application du redacteur
n'est ni importe ni execute.

Sources des couples :
  (1) le rapport scelle de la contre-lecture (Markdown, section 2), source principale ;
  (2) l'outil scelle des remarques de la contre-lecture, lu par son arbre syntaxique (module ast), jamais execute :
      recoupement, chaine par chaine.
Les textes exacts des changements « hors correction » (HT1 a HT15, HD1 a HD7) sont lus, comme donnees seulement, dans
l'outil du redacteur par son arbre syntaxique (jamais execute), pour la reconstruction exacte ; la difference residuelle
est aussi listee sans eux.

Aucun score ouvert. N'ecrit que les sorties nommees et, pour l'essai du validateur, des copies au dossier temporaire donne.
Usage : python3 -B verifier-corrections-brouillon2-v1.py <racine du depot> <sortie .json> <sortie .md> <dossier temporaire>
"""
import ast
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

RACINE = Path(sys.argv[1]).resolve()
SORTIE_JSON = Path(sys.argv[2])
SORTIE_MD = Path(sys.argv[3])
TMP = Path(sys.argv[4])

DOS = "docs/notes/barreau5-resolution-v1/premiere-lecture/"
F = {
    "texte1": "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon1.md",
    "texte2": "prereg/validite-adaptateur-sondes-apprises-sur-la-tache-v1-brouillon2.md",
    "devis1": DOS + "devis-relecture-meme-chemin-v1-brouillon1.md",
    "devis2": DOS + "devis-relecture-meme-chemin-v1-brouillon2.md",
    "rapport": DOS + "contre-lecture-validite-adaptateur-sondes-tache-v1-brouillon1-v1.md",
    "outil_remarques": DOS + "contre-lecture-outils-v1/remarques-contre-lecture-v1.py",
    "outil_redacteur": DOS + "outils-brouillon2-v1/appliquer-corrections-brouillon2-v1.py",
    "table": DOS + "table-corrections-brouillon2-v1.md",
    "validateur": "src/controle_ia/prereg.py",
}
ATTENDU = {  # prefixes du mandat du verificateur, empreintes entieres recalculees ici
    "texte1": "c5cd92596af8083c5643d1877a9e1a5eed8c3ea77b926b03303f0db263306d43",
    "texte2": "b346d5bd432a798cafd454d2dbec8fda52c98a43ef6108877d0ea04f5947d5d1",
    "devis1": "d4694c11a7c4bad9772a968f1f69751e4740ebe5d16fbffb3645d3afebaa2f3d",
    "devis2": "35eb699660fed749870505fdd660ca6d94d3ad739edcc81b9034a2311943fb90",
    "rapport": "13bde37898a0a6f6f71aab4bffc6142df8af71691277e8f923925942a374239c",
    "outil_remarques": "a37fc7da85d25ade2792038d7c5f14e6b92553f9f3c1fc1c69a63ea8a9855dca",
    "outil_redacteur": "2a88a1baf2650fe462abad2093adc7a2001fb27f44a30133fd9d26f951876d71",
    "table": "d4d6c9c8635574a62ed713954e17b8591d351441bea9035e81839be74fd049b6",
    "validateur": "3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306",
}
sortie = {"empreintes": {}, "erreurs": []}


def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


for k, chemin in F.items():
    h = sha_octets((RACINE / chemin).read_bytes())
    sortie["empreintes"][chemin] = h
    if h != ATTENDU[k]:
        sortie["erreurs"].append(f"empreinte differente : {chemin}")
T = {k: (RACINE / F[k]).read_text(encoding="utf-8") for k in ("texte1", "texte2", "devis1", "devis2")}
NOM_FICHIER = {F["texte1"]: "texte", F["devis1"]: "devis"}


# ------------------------------------------------------------------------------------------- (1) couples du rapport
def couples_du_rapport(md):
    debut = md.index("## 2. Remarques numérotées")
    fin = md.index("## 3. Outils de la contre-lecture")
    lignes = md[debut:fin].split("\n")
    entete = re.compile(r"^\*\*Correction (\S+)\*\* \((texte|devis) : `([^`]+)` ; texte « avant » trouvé (\d+) fois\)$")
    out, i = [], 0
    while i < len(lignes):
        m = entete.match(lignes[i])
        if not m:
            i += 1
            continue
        ident, genre, chemin = m.group(1), m.group(2), m.group(3)
        blocs = []
        for etiquette in ("Avant :", "Après :"):
            while lignes[i] != etiquette:
                i += 1
            i += 1
            assert lignes[i] == "", (ident, etiquette)
            i += 1
            bloc = []
            while i < len(lignes) and lignes[i].startswith(">"):
                bloc.append(lignes[i][2:] if lignes[i].startswith("> ") else lignes[i][1:])
                i += 1
            blocs.append("\n".join(bloc))
        out.append(dict(id=ident, genre=genre, fichier=chemin, avant=blocs[0], apres=blocs[1]))
    return out


RAP = couples_du_rapport((RACINE / F["rapport"]).read_text(encoding="utf-8"))


# ------------------------------------------------------------------------------------- (2) arbre syntaxique des outils
def evaluer(noeud, noms):
    if isinstance(noeud, ast.Constant):
        return noeud.value
    if isinstance(noeud, ast.BinOp) and isinstance(noeud.op, ast.Add):
        return evaluer(noeud.left, noms) + evaluer(noeud.right, noms)
    if isinstance(noeud, ast.Name):
        return noms[noeud.id]
    if isinstance(noeud, (ast.Tuple, ast.List)):
        return [evaluer(e, noms) for e in noeud.elts]
    raise ValueError("forme non prevue : " + ast.dump(noeud)[:200])


def constantes_de_module(arbre):
    noms = {}
    for n in arbre.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            try:
                noms[n.targets[0].id] = evaluer(n.value, noms)
            except (ValueError, KeyError):
                pass
    return noms


arbre = ast.parse((RACINE / F["outil_remarques"]).read_text(encoding="utf-8"))
noms = constantes_de_module(arbre)
OUTIL = []
for n in arbre.body:
    if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, "id", None) == "rem":
        a = n.value.args
        ident, classe = evaluer(a[0], noms), evaluer(a[1], noms)
        for k, (fich, avant, apres) in enumerate(evaluer(a[4], noms), 1):
            OUTIL.append(dict(id=f"{ident}.{k}", classe=classe, fichier=fich, avant=avant, apres=apres))
recoupement = dict(nombre_rapport=len(RAP), nombre_outil=len(OUTIL), ecarts=[])
for r, o in zip(RAP, OUTIL):
    for champ in ("id", "fichier", "avant", "apres"):
        if r[champ] != o[champ]:
            recoupement["ecarts"].append((r["id"], champ))
recoupement["identiques"] = len(RAP) == len(OUTIL) == 44 and not recoupement["ecarts"]
sortie["recoupement_rapport_outil"] = recoupement
CLASSE = {o["id"]: o["classe"] for o in OUTIL}
sortie["compte_par_classe"] = {c: sum(1 for o in OUTIL if o["classe"] == c) for c in ("bloquante", "majeure", "mineure")}
sortie["compte_par_fichier"] = {g: sum(1 for r in RAP if r["genre"] == g) for g in ("texte", "devis")}


# ------------------------------------------------------------------------------------------------ (3) controles
def ligne_de(texte, position):
    return texte.count("\n", 0, position) + 1


def lignes_occupees(texte, morceau):
    p = texte.find(morceau)
    if p < 0:
        return None
    return [ligne_de(texte, p), ligne_de(texte, p + len(morceau) - 1)]


controles = []
for c in RAP:
    b1 = T["texte1"] if c["genre"] == "texte" else T["devis1"]
    b2 = T["texte2"] if c["genre"] == "texte" else T["devis2"]
    controles.append(dict(
        id=c["id"], classe=CLASSE[c["id"]], genre=c["genre"],
        avant_dans_brouillon1=b1.count(c["avant"]),
        apres_dans_brouillon2=b2.count(c["apres"]),
        avant_encore_dans_brouillon2=(b2.count(c["avant"]) if c["avant"] not in c["apres"] else "contenu dans l'apres"),
        lignes_de_l_apres_dans_brouillon2=lignes_occupees(b2, c["apres"])))
sortie["controles_par_couple"] = controles
sortie["synthese_couples"] = dict(
    avant_unique_dans_brouillon1=all(x["avant_dans_brouillon1"] == 1 for x in controles),
    apres_present_une_fois_dans_brouillon2=all(x["apres_dans_brouillon2"] == 1 for x in controles),
    avant_parti_du_brouillon2=all(x["avant_encore_dans_brouillon2"] in (0, "contenu dans l'apres") for x in controles))

# Application sequentielle (ordre du rapport) : unicite verifiee a chaque pas, dans le texte deja modifie.
appl = {"texte": T["texte1"], "devis": T["devis1"]}
pas_non_uniques = []
for c in RAP:
    n = appl[c["genre"]].count(c["avant"])
    if n != 1:
        pas_non_uniques.append((c["id"], n))
    appl[c["genre"]] = appl[c["genre"]].replace(c["avant"], c["apres"], 1)
sortie["application_sequentielle_pas_non_uniques"] = pas_non_uniques


# ------------------------------------------------------------------- (4) difference residuelle, sans donnee du redacteur
def residus(a, b):
    """Blocs de lignes qui different entre a (brouillon 1 corrige des seuls couples) et b (brouillon 2)."""
    la, lb = a.split("\n"), b.split("\n")
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        avant, apres = "\n".join(la[i1:i2]), "\n".join(lb[j1:j2])
        sm = difflib.SequenceMatcher(None, avant, apres, autojunk=False)
        morceaux = []
        for op2, a1, a2, b1, b2 in sm.get_opcodes():
            if op2 != "equal":
                morceaux.append(dict(op=op2, retire=avant[a1:a2], ajoute=apres[b1:b2]))
        out.append(dict(op=op, lignes_brouillon1_corrige=[i1 + 1, i2], lignes_brouillon2=[j1 + 1, j2], morceaux=morceaux))
    return out


RES = {"texte": residus(appl["texte"], T["texte2"]), "devis": residus(appl["devis"], T["devis2"])}

# ---------------------------------------------------- (5) reconstruction exacte avec les changements declares (donnees)
arbre_r = ast.parse((RACINE / F["outil_redacteur"]).read_text(encoding="utf-8"))
noms_r = constantes_de_module(arbre_r)
HORS = {"devis": noms_r["HORS_DEVIS"], "texte": noms_r["HORS_TEXTE"]}
PLACE = noms_r["EMPREINTE_DEVIS2"]
recon = dict(appl)
hors_releve = []
for genre in ("devis", "texte"):
    for ident, quoi, avant, apres in HORS[genre]:
        n = recon[genre].count(avant)
        hors_releve.append(dict(id=ident, genre=genre, avant_unique=n == 1,
                                avant_dans_l_apres_d_un_couple=any(avant in c["apres"] for c in RAP if c["genre"] == genre)))
        recon[genre] = recon[genre].replace(avant, apres, 1)
recon["texte"] = recon["texte"].replace(PLACE, sha_octets(recon["devis"].encode("utf-8")))
sortie["hors_correction_declares"] = hors_releve
sortie["reconstruction"] = dict(
    devis_egal_au_brouillon2=recon["devis"] == T["devis2"], texte_egal_au_brouillon2=recon["texte"] == T["texte2"],
    empreinte_devis_reconstruit=sha_octets(recon["devis"].encode("utf-8")),
    empreinte_texte_reconstruit=sha_octets(recon["texte"].encode("utf-8")))

# Attribution de chaque bloc residuel a un changement declare (son « apres » contient le texte ajoute du bloc).
for genre in ("texte", "devis"):
    for bloc in RES[genre]:
        ajoute = "".join(m["ajoute"] for m in bloc["morceaux"])
        cands = []
        for ident, quoi, avant, apres in HORS[genre]:
            ap = apres.replace(PLACE, sha_octets(recon["devis"].encode("utf-8")))
            if all(m["ajoute"] in ap for m in bloc["morceaux"] if m["ajoute"]) and all(
                    m["retire"] in avant for m in bloc["morceaux"] if m["retire"]):
                cands.append(ident)
        bloc["attribue_a"] = cands
sortie["blocs_residuels"] = {g: [dict(lignes_brouillon2=b["lignes_brouillon2"], attribue_a=b["attribue_a"],
                                      nombre_de_morceaux=len(b["morceaux"])) for b in RES[g]] for g in RES}
sortie["blocs_residuels_non_attribues"] = {g: [b["lignes_brouillon2"] for b in RES[g] if not b["attribue_a"]] for g in RES}

# Lignes ou les changements declares tombent dans le brouillon 2 (pour la table)
lignes_hors = {}
for genre in ("texte", "devis"):
    for ident, quoi, avant, apres in HORS[genre]:
        ap = apres.replace(PLACE, sha_octets(recon["devis"].encode("utf-8")))
        cible = T["texte2"] if genre == "texte" else T["devis2"]
        # partie neuve : ce qui, dans l'apres, n'est pas dans l'avant
        lignes_hors[ident] = lignes_occupees(cible, ap)
sortie["lignes_des_changements_declares_dans_brouillon2"] = lignes_hors

# ------------------------------------------------------------------------------- (6) lignes annoncees par la table
table = (RACINE / F["table"]).read_text(encoding="utf-8")
annonces = {}
for m in re.finditer(r"^\| (\S+) \| (?:bloquante|majeure|mineure) \|[^\n]*\| (texte|devis), l\. ([0-9]+)(?:(?: et | à )([0-9]+))?",
                     table, re.M):
    annonces[m.group(1)] = dict(fichier=m.group(2), lignes=[int(m.group(3)), int(m.group(4) or m.group(3))])
for m in re.finditer(r"^\| (HT\d+|HD\d+(?: à HD\d+)?) \| (texte|devis), l\. ([0-9]+)(?:(?: et | à )([0-9]+))?", table, re.M):
    annonces[m.group(1)] = dict(fichier=m.group(2), lignes=[int(m.group(3)), int(m.group(4) or m.group(3))])
ecarts_lignes = []
for c in controles:
    a = annonces.get(c["id"])
    vrai = c["lignes_de_l_apres_dans_brouillon2"]
    if a is None or vrai is None or not (a["lignes"][0] <= vrai[1] and vrai[0] <= a["lignes"][1]):
        ecarts_lignes.append(dict(id=c["id"], annonce=a, reel=vrai))
for ident, vrai in lignes_hors.items():
    a = annonces.get(ident)
    if a is None:
        continue
    if vrai is None or not (a["lignes"][0] <= vrai[1] and vrai[0] <= a["lignes"][1]):
        ecarts_lignes.append(dict(id=ident, annonce=a, reel=vrai))
sortie["lignes_annoncees_par_la_table"] = dict(nombre=len(annonces), ecarts=ecarts_lignes)

# ------------------------------------------------------------------- (7) constantes de HT10 contre la table du texte
ligne67 = [l for l in T["texte2"].split("\n") if l.startswith("| texte égal moins adaptateur seul (99 %) |")]
ht10 = T["texte2"][T["texte2"].index("**Deux crochets, leur source et leur place.**"):]
ht10 = ht10[:ht10.index("\n")]
nombres = lambda s: re.findall(r"[+−-]?\d,\d{4}", s)
sortie["HT10_constantes"] = dict(
    ligne_de_table_unique=len(ligne67) == 1,
    nombres_table=nombres(ligne67[0]) if ligne67 else None, nombres_HT10=nombres(ht10),
    egaux=(nombres(ligne67[0]) == nombres(ht10)) if ligne67 else False,
    etats_HT10=re.findall(r"dose (0,25|0,5|0,75|1), (non établie|contraire)", ht10))


def etat_par_intervalle(bas, haut):
    v = lambda s: float(s.replace("−", "-").replace(",", "."))
    return "contraire" if v(haut) < 0 else ("au-dessus" if v(bas) > 0 else "non établie")


if ligne67:
    trip = re.findall(r"([+−-]\d,\d{4}) \[([+−-]\d,\d{4}) ; ([+−-]\d,\d{4})\]", ligne67[0])
    sortie["HT10_constantes"]["etat_deduit_des_intervalles"] = [etat_par_intervalle(b, h) for _, b, h in trip]

# ---------------------------------------------------------------------------------------- (8) validateur et scellement
sys.path.insert(0, str(RACINE / "src"))
from controle_ia.prereg import problemes  # noqa: E402

TMP.mkdir(parents=True, exist_ok=True)
val = {"brouillon2": problemes(RACINE / F["texte2"]), "brouillon1": problemes(RACINE / F["texte1"])}
MARQ = ["<<COMMIT_CODE_VSAT>>", "<<CONTRE_LECTURE_1>>", "<<DECISION_9_MOT>>", "<<PIECES_PLANIFICATION_VERSEES>>",
        "<<DEVIS_RELECTURE>>"]
val["marqueurs_occurrences"] = {m: [ligne_de(T["texte2"], p.start()) for p in re.finditer(re.escape(m), T["texte2"])]
                                for m in MARQ}
REMPLI = {
    "<<COMMIT_CODE_VSAT>>": "0123456789abcdef0123456789abcdef01234567 (essai)",
    "<<CONTRE_LECTURE_1>>": "**Contre-lecture 1** : brouillon relu `" + ATTENDU["texte1"] + "`, rapport `" + ATTENDU["rapport"]
                            + "` (essai)",
    "<<DECISION_9_MOT>>": "mot de Lazar (essai)",
    "<<PIECES_PLANIFICATION_VERSEES>>": "pieces versees (essai)",
    "<<DEVIS_RELECTURE>>": "devis en brouillon, aucune dépense (essai)",
}


def essai(nom, texte):
    p = TMP / nom
    p.write_text(texte, encoding="utf-8")
    return problemes(p)


t = T["texte2"]
for m, r in REMPLI.items():
    # n'importe quelle occurrence hors de la table finale ; la table finale est traitee a part
    corps, table_fin = t.split("## Marqueurs à remplir avant le scellement")
    corps = corps.replace("`" + m + "`", r).replace(m, r)
    t = corps + "## Marqueurs à remplir avant le scellement" + table_fin
val["essai_marqueurs_remplis_table_gardee"] = essai("essai-a.md", t)
t_sans_table = t.split("## Marqueurs à remplir avant le scellement")[0].rstrip("\n") + "\n"
val["essai_marqueurs_remplis_table_retiree"] = essai("essai-b.md", t_sans_table)
t_c = T["texte2"].split("## Marqueurs à remplir avant le scellement")[0].rstrip("\n") + "\n"
for m, r in REMPLI.items():
    if m != "<<CONTRE_LECTURE_1>>":
        t_c = t_c.replace("`" + m + "`", r).replace(m, r)
t_c = t_c.replace("`<<CONTRE_LECTURE_1>>`", "entrée écrite (essai, sans empreinte entière du rapport)")
val["essai_table_retiree_sans_empreinte_entiere_du_rapport"] = essai("essai-c.md", t_c)
sortie["validateur"] = val

# ------------------------------------------------------------------------- (9) couples proposes par le verificateur
PROPOSES = json.loads((Path(__file__).parent / "couples-proposes-verification-v1.json").read_text(encoding="utf-8"))
prop = []
cible = {"texte": T["texte2"], "devis": T["devis2"]}
for c in PROPOSES:
    prop.append(dict(id=c["id"], genre=c["genre"], avant_dans_brouillon2=cible[c["genre"]].count(c["avant"]),
                     lignes=lignes_occupees(cible[c["genre"]], c["avant"])))
    assert c["avant"] != c["apres"], c["id"]
appl3 = dict(cible)
for c in PROPOSES:
    assert appl3[c["genre"]].count(c["avant"]) == 1, ("non unique au pas", c["id"])
    appl3[c["genre"]] = appl3[c["genre"]].replace(c["avant"], c["apres"], 1)
for c, pr in zip(PROPOSES, prop):
    pr["apres_present_apres_application"] = appl3[c["genre"]].count(c["apres"])
sortie["couples_proposes"] = dict(controles=prop,
                                  tous_uniques_dans_brouillon2=all(p["avant_dans_brouillon2"] == 1 for p in prop),
                                  validateur_apres_application=essai("essai-d.md", appl3["texte"]))
# les « apres » des 44 couples restent entiers apres application des couples proposes, sauf ceux que l'on corrige expres
sortie["couples_proposes"]["apres_de_la_contre_lecture_touches"] = [
    c["id"] for c in RAP if appl3[c["genre"]].count(c["apres"]) != 1]

# --------------------------------------------------------------------------------------------------------- sorties
SORTIE_JSON.write_text(json.dumps(sortie, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
md = ["# Différence résiduelle entre les brouillons 1 (corrigés des seuls 44 couples) et 2 — sortie de "
      "`verifier-corrections-brouillon2-v1.py`", ""]
for genre in ("texte", "devis"):
    md.append(f"## {genre}")
    md.append("")
    for b in RES[genre]:
        md.append(f"### lignes du brouillon 2 : {b['lignes_brouillon2'][0]} à {b['lignes_brouillon2'][1]} ; attribué à : "
                  f"{', '.join(b['attribue_a']) or 'AUCUN'}")
        md.append("")
        for m in b["morceaux"]:
            md.append(f"- {m['op']} — retiré : « {m['retire']} » — ajouté : « {m['ajoute']} »")
        md.append("")
SORTIE_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
resume = {k: sortie[k] for k in ("erreurs", "recoupement_rapport_outil", "compte_par_classe", "compte_par_fichier",
                                 "synthese_couples", "application_sequentielle_pas_non_uniques", "reconstruction",
                                 "blocs_residuels_non_attribues")}
resume["validateur_brouillon2"] = val["brouillon2"]
resume["ecarts_de_lignes_table"] = sortie["lignes_annoncees_par_la_table"]
resume["couples_proposes"] = sortie["couples_proposes"]
print(json.dumps(resume, indent=1, ensure_ascii=False))
