"""Vérification courte du différentiel de T0.8, du brouillon 8 au brouillon 9 (candidat) — calcul, v1.

Usage (depuis la racine du dépôt) : PYTHONPATH=src python3 CE_SCRIPT DOSSIER_TEMPORAIRE
Lecture seule sur le dépôt ; écrit seulement dans DOSSIER_TEMPORAIRE (vide ou neuf) : les couples régénérés, le rejeu par
l'outil de l'auteur, et des copies du brouillon 9 aux marqueurs remplis d'une valeur factice pour passer le validateur.
N'imprime aucun extrait des brouillons ni des journaux : des nombres, des booléens, des empreintes, des identifiants de
constats et de couples, des chemins. La liste des mots de modèles est codée (rot13) pour qu'aucun n'y soit écrit en clair.
"""
import codecs, difflib, hashlib, json, re, subprocess, sys
from pathlib import Path

from controle_ia import prereg

B = "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon%d.md"
C = "brouillons/t08-code-compte4-v1/"
R = "prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon8-verification-courte-v1"
J = "registres-provisoires/compte-4-2026-11-14-"
ATTENDU = {
    B % 9: "dae4cc12a2e9de07d97fc8e5739c5cf5db79b98f234be30d94c52dbf72fb64ef",
    B % 8: "129b1db245e186040256c8630dfb585bcd2a1e1ab4ea7b8ff817696fbd3220a7",
    B % 4: "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5",
    R + ".md": "220fe2fd8fedef8a06626e22f630fdd916f58675d5c441473be9c62dcca7b6fc",
    R + "-calcul.py": "c738299edb8c720ad78f3dc626ab986b7adf6f5fcfab2d6ef160ab1b7f6ca266",
    C + "faire-couples-t08-brouillon9-v1.py": "b015b54f8c5a11308c8fec547dbc35f87d0aaa64c2fcc61039e84d9d526af1aa",
    C + "couples-t08-brouillon9-v1.json": "f10703563b80399bd1b7db1e40259501bfce4d1a1c9859d3fcb60b44431c6095",
    C + "sortie-application-t08-brouillon9-v1.json": "290477e7af98dbb16bd927f75f63adf0222e2261cf1e87f666ebbb6b1340ee77",
    C + "appliquer-couples-t08-v1.py": "87e8464236a57ecbade88c90df0d98c50d0f3a502afc3ce81be913cb6f845c31",
    J + "v10.md": None, J + "v11-sans-identifiants.md": None, J + "v16.md": None, J + "v17.md": None, J + "v19.md": None,
}
GELEES = ["Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Critères de lecture gelés", "Liste d'arrêt"]
SEPT = ["CODE_MOTS_ET_COUT_T06", "EMPREINTES_ENTREES_7B", "ENTROPIE_T08", "GO_T08", "LIGNE_DEPENSE_T08",
        "LIGNE_MOT_LAZAR_T5_19", "RUN_7B"]
MOTS = [codecs.decode(m, "rot13") for m in
        ["pynhqr", "bchf", "fbaarg", "unvxh", "snoyr", "tcg", "trzvav", "yynzn", "zvfgeny", "djra", "naguebcvp", "bcranv",
         "qrrcfrrx", "tebx", "zrgn-", "tbbtyr", "cuv-"]]
PROPOSES = [
 {"id": "VT9C-01", "constat": "VT9-01",
  "ancien": "bornée au brouillon 7, VT6-03, puis au brouillon 8) :",
  "nouveau": "bornée au brouillon 7, VT6-03, puis au brouillon 8, puis au brouillon 9, VT8-04) :"},
 {"id": "VT9C-02", "constat": "VT9-02",
  "ancien": "aucune de ces pièces ne lui a montré de résultat",
  "nouveau": "aucune des pièces de (ii-b) ne lui a montré de résultat"},
 {"id": "VT9C-03", "constat": "VT9-03",
  "ancien": "depuis un brouillon antérieur à elle,",
  "nouveau": "depuis un brouillon antérieur à la session du compte 4,"},
 {"id": "VT9C-04", "constat": "VT9-05",
  "ancien": "ne nomme pas) : suit T5-19 chez Lazar ;",
  "nouveau": "ne nomme pas) : suit T5-19 chez Lazar (le mot de Lazar donné, brouillon 8, ne nommant que T5-19, son sort "
             "s'écrit au remplissage de `LIGNE_MOT_LAZAR_T5_19` : brouillon 9, VT8-05) ;"},
 {"id": "VT9C-05", "constat": "VT9-06",
  "ancien": "le mot de Lazar recopié ne porte que sur T5-19 : VT5-07 couvert par lui, ou porté à part)",
  "nouveau": "le mot de Lazar recopié ne nomme que T5-19 : la session mère écrit si la décision que ce mot tranche "
             "couvre VT5-07, ou s'il est porté à part)"},
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def lire(ch):
    return Path(ch).read_text(encoding="utf-8")


def decoupe(t):
    m = re.split(r"^## +(.+?)\s*$", t, flags=re.M)
    d = {"(en-tête)": m[0]}
    for titre, corps in zip(m[1::2], m[2::2]):
        d[titre.strip()] = corps
    return d


def section_de(t, pos):
    titres = [(x.start(), x.group(1).strip()) for x in re.finditer(r"^## +(.+?)\s*$", t, flags=re.M)]
    nom = "(en-tête)"
    for p, n in titres:
        if p <= pos:
            nom = n
    return nom


def appliquer(t, couples):
    journal = []
    for c in couples:
        n = t.count(c["ancien"])
        pos = t.find(c["ancien"])
        journal.append({"id": c["id"], "occurrences_avant": n, "section": section_de(t, pos) if n else None,
                        "ligne": t.count("\n", 0, pos) + 1 if n else None,
                        "long_ancien": len(c["ancien"]), "long_nouveau": len(c["nouveau"]),
                        "ancien_different_du_nouveau": c["ancien"] != c["nouveau"]})
        if n == 1:
            t = t.replace(c["ancien"], c["nouveau"], 1)
    return t, journal


def mots_de_modele(t):
    bas = t.lower()
    return sum(bas.count(m) for m in MOTS)


def problemes_texte(t, tmp, nom):
    p = tmp / nom
    p.write_text(t, encoding="utf-8")
    return prereg.problemes(p)


def principal():
    tmp = Path(sys.argv[1])
    tmp.mkdir(parents=True, exist_ok=True)
    s = {}

    # 0. empreintes
    e = {}
    for ch, att in ATTENDU.items():
        h = sha(Path(ch).read_bytes())
        comp = Path(ch + ".sha256")
        e[ch] = {"sha": h, "egale_a_la_consigne": (h == att) if att else None,
                 "compagnon": comp.exists() and comp.read_text().split()[0] == h}
    s["0_empreintes"] = e
    s["0_prereg_py"] = sha(Path("src/controle_ia/prereg.py").read_bytes())

    b4, b8, b9 = lire(B % 4), lire(B % 8), lire(B % 9)
    couples = json.loads(lire(C + "couples-t08-brouillon9-v1.json"))

    # 1. différentiel
    dates = re.findall(r"brouillon (\d) écrit le (\d{4}-\d{2}-\d{2}) à partir de (\d{2}:\d{2}) UTC", b9)
    s["1_dates_en_tete_b9"] = dates
    d9 = [x for x in dates if x[0] == "9"]
    regen = tmp / "couples-regeneres.json"
    if regen.exists():
        regen.unlink()
    r = subprocess.run([sys.executable, "-I", C + "faire-couples-t08-brouillon9-v1.py", d9[0][1], d9[0][2], str(regen)],
                       capture_output=True, text=True)
    s["1_regeneration_des_couples"] = {
        "date_et_heure_jouees": [d9[0][1], d9[0][2]], "code_retour": r.returncode,
        "sha_regenere": sha(regen.read_bytes()) if regen.exists() else None,
        "egal_aux_couples_verses_a_l_octet": regen.exists() and regen.read_bytes() == Path(C + "couples-t08-brouillon9-v1.json").read_bytes()}
    rejeu, journal = appliquer(b8, couples)
    s["1_rejeu_b8_vers_b9"] = {
        "nombre_couples": len(couples), "ids": [c["id"] for c in couples],
        "cles": sorted({k for c in couples for k in c}),
        "sha_rejeu": sha(rejeu.encode("utf-8")), "egal_b9_a_l_octet": rejeu.encode("utf-8") == Path(B % 9).read_bytes(),
        "journal": journal}
    outil = tmp / "rejeu-par-l-outil.md"
    if outil.exists():
        outil.unlink()
    r = subprocess.run([sys.executable, "-I", C + "appliquer-couples-t08-v1.py", B % 8, ATTENDU[B % 8],
                        C + "couples-t08-brouillon9-v1.json", ATTENDU[C + "couples-t08-brouillon9-v1.json"], str(outil),
                        ",".join(SEPT)], capture_output=True, text=True)
    so = json.loads(r.stdout) if r.returncode == 0 else {}
    sv = json.loads(lire(C + "sortie-application-t08-brouillon9-v1.json"))
    s["1_rejeu_par_l_outil_de_l_auteur"] = {
        "code_retour": r.returncode, "sha_sortie": so.get("sha_sortie"),
        "egal_b9_a_l_octet": outil.exists() and outil.read_bytes() == Path(B % 9).read_bytes(),
        "sortie_versee_egale_hors_chemin_de_sortie": {k: v for k, v in so.items() if k != "sortie"} == {k: v for k, v in sv.items() if k != "sortie"},
        "sortie_versee": {"sha_base_egale": sv["sha_base"] == ATTENDU[B % 8], "sha_couples_egale": sv["sha_couples"] == ATTENDU[C + "couples-t08-brouillon9-v1.json"],
                          "sha_sortie_egale": sv["sha_sortie"] == ATTENDU[B % 9], "nombre_couples": sv["nombre_couples"],
                          "marqueurs_permis_restants": sv["marqueurs_permis_restants"]}}
    l8, l9 = b8.split("\n"), b9.split("\n")
    ops = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, l8, l9, autojunk=False).get_opcodes():
        if op != "equal":
            pos = sum(len(x) + 1 for x in l9[:j1])
            ops.append({"op": op, "avant": [i1 + 1, i2], "apres": [j1 + 1, j2], "section_apres": section_de(b9, pos)})
    s["1_lignes_changees_b8_vers_b9"] = ops

    # 2. fidélité
    rapport = lire(R + ".md")
    sec3 = rapport.split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    cr = json.loads(re.search(r"```json\n(.*?)\n```", sec3, re.S).group(1))
    s["2_fidelite"] = {
        "ids_rapport": [c["id"] for c in cr],
        "trois_premiers_couples_egaux_au_rapport": [{k: c[k] for k in ("id", "ancien", "nouveau")} for c in cr]
        == [{k: c[k] for k in ("id", "ancien", "nouveau")} for c in couples[:3]],
        "constats_du_rapport_par_gravite": {g: len(re.findall(r"^- \*\*VT8-\d\d — " + g, rapport, flags=re.M)) for g in ("bloquant", "majeur", "mineur")},
        "verdict_du_rapport_conforme_apres": "**Conforme après les corrections listées.**" in rapport,
        "rapport_dit_0_bloquant_0_majeur_6_mineurs": "**0 bloquant, 0 majeur, 6 mineurs.**" in rapport}
    s9 = decoupe(b9)
    cl = s9["Contre-lecture"]
    ent = list(prereg.ENTREE.finditer(cl))
    e6 = [cl[x.start():(ent[k + 1].start() if k + 1 < len(ent) else len(cl))] for k, x in enumerate(ent) if x.group(1) == "6"]
    e6 = e6[0].split("\n\n")[0] if e6 else ""
    s["2_entree_contre_lecture_6"] = {
        "longueur": len(e6), "empreintes": sorted(set(prereg.EMPREINTE.findall(e6))),
        "empreintes_sont_b8_rapport_script": sorted(set(prereg.EMPREINTE.findall(e6))) == sorted([ATTENDU[B % 8], ATTENDU[R + ".md"], ATTENDU[R + "-calcul.py"]]),
        "constats_nommes": sorted(set(re.findall(r"VT8-\d\d", e6))), "couples_nommes": sorted(set(re.findall(r"VT8C-\d\d", e6))),
        "dit_0_bloquant_0_majeur_6_mineurs": "0 bloquant, 0 majeur, 6 mineurs" in e6,
        "dit_conforme_apres": "« conforme après les corrections listées »" in e6,
        "entrees_numerotees_b9": [x.group(1) for x in ent]}

    # 3. sections gelées
    s4, s8 = decoupe(b4), decoupe(b8)
    s["3_titres_egaux_b4_b8_b9"] = list(s4) == list(s8) == list(s9)
    s["3_sections"] = {n: {"b9_egale_b4": s9[n] == s4[n], "b9_egale_b8": s9[n] == s8[n],
                           "sha4": sha(s4[n].encode())[:16], "sha9": sha(s9[n].encode())[:16],
                           "couples": [j["id"] for j in journal if j["section"] == n]} for n in s9}
    s["3_gelees_egales_a_l_octet_au_b4"] = {n: s9[n] == s4[n] for n in GELEES}
    p4, p9 = s4["Plan d'analyse"].split("\n"), s9["Plan d'analyse"].split("\n")
    po = [o for o in difflib.SequenceMatcher(None, p4, p9, autojunk=False).get_opcodes() if o[0] != "equal"]
    ajout = p9[po[0][3]:po[0][4]] if len(po) == 1 and po[0][0] == "insert" else []
    sans = p9[:po[0][3]] + p9[po[0][4]:] if ajout else p9
    s["3_plan"] = {"plan9_egal_plan8_a_l_octet": s9["Plan d'analyse"] == s8["Plan d'analyse"],
                   "operations_b4_vers_b9": [list(o) for o in po], "ajout_une_seule_ligne": len(ajout) == 1,
                   "plan9_sans_l_ajout_egal_plan4": sans == p4,
                   "ligne_ajoutee_porte_T5_19_et_le_marqueur": len(ajout) == 1 and "T5-19" in ajout[0] and "<<LIGNE_MOT_LAZAR_T5_19>>" in ajout[0],
                   "longueur_ajout": len(ajout[0]) if len(ajout) == 1 else None}

    # 4. déclaration de vue
    def declaration(t):
        ligne = [x for x in t.split("\n") if x.startswith("- **Auteurs**")][0]
        return ligne.split("**Ce qu'elle a vu avant le scellement**", 1)[1]
    v8, v9 = declaration(b8), declaration(b9)
    neuf = [c["nouveau"] for c in couples if c["id"] in ("T9-03", "T9-04")]
    sav8, sav9 = s8["Ce que les auteurs savaient avant le scellement"], s9["Ce que les auteurs savaient avant le scellement"]
    so_ = [o for o in difflib.SequenceMatcher(None, sav8.split("\n"), sav9.split("\n"), autojunk=False).get_opcodes() if o[0] != "equal"]
    lj = sav9.split("\n")[so_[0][3]:so_[0][4]] if len(so_) == 1 else []
    journaux = {k: lire(k) for k in ATTENDU if k.startswith(J)}
    s["4_declaration_de_vue"] = {
        "longueur_b8_b9": [len(v8), len(v9)],
        "mots_dans_les_ajouts_T9-03_T9-04": {m: sum(x.count(m) for x in neuf) for m in ("seuil", "règle", "réglage", "critère", "prédiction", "signe")},
        "chiffres_dans_les_ajouts_hors_identifiants": sorted(set(re.findall(r"(?<![A-Za-z0-9-])\d+(?:[,.]\d+)?", " ".join(re.sub(r"VT\d-\d\d|7a|7b|T0\.\d", "", x) for x in neuf)))),
        "occurrences_ii_b_b8_b9": [b8.count("(ii-b)"), b9.count("(ii-b)")],
        "lignes_ii_b_b9": sorted({i + 1 for i, x in enumerate(l9) if "(ii-b)" in x}),
        "saboteur_a_budget_occurrences_b9": b9.count("saboteur à budget"),
        "borne_dite_au_brouillon_8_presente": "puis au brouillon 8) :" in v9,
        "borne_dite_au_brouillon_9": "brouillon 9" in v9,
        "section_savaient_b9_egale_b4": sav9 == s4["Ce que les auteurs savaient avant le scellement"],
        "section_savaient_operations_b8_vers_b9": [list(o) for o in so_],
        "section_savaient_une_seule_ligne_ajoutee_en_fin": len(so_) == 1 and so_[0][0] == "insert" and len(lj) == 1 and sav9.rstrip("\n").endswith(lj[0]),
        "ligne_ajoutee": {"longueur": len(lj[0]) if lj else None,
                          "mots": {m: lj[0].count(m) for m in ("seuil", "règle", "réglage", "critère")} if lj else None,
                          "constats_nommes": re.findall(r"VT\d-\d\d", lj[0]) if lj else None},
        "devis_7b_occurrences_par_ligne_b9": {i + 1: x.count("Devis de la confirmation 7b") for i, x in enumerate(l9) if "Devis de la confirmation 7b" in x},
        "duree_13_6_h_par_section_b9": {section_de(b9, m.start()): 1 for m in re.finditer(r"13,6", b9)},
        "duree_13_6_h_au_calendrier_du_b4": "13,6" in s4["Calendrier, et ce qui se passe s'il glisse"],
        "journaux": {k: {"entrees": re.findall(r"^## (C4-\d{4})", t, flags=re.M),
                         "occurrences_Devis": t.count("Devis"), "occurrences_T0.6": t.count("T0.6"),
                         "occurrences_ii_b": t.count("(ii-b)"),
                         "occurrences_7a": len(re.findall(r"\b7a\b", t)),
                         "mots_de_modele": mots_de_modele(t)} for k, t in journaux.items()},
        "journal_v10_nomme_rapport_b5_v3": "f788bb73baa0d71f826d4778c2b2e2c55baa20383f2f49e777d670d849df6d7e" in journaux[J + "v10.md"],
        "journal_v11_nomme_rapport_b6": "8794f9d7f772d85b76b2d2364f5e23dc8f2843f192e8b89b90c0c0246c287322" in journaux[J + "v11-sans-identifiants.md"],
        "journal_v19_nomme_rapport_b8_et_son_script": ATTENDU[R + ".md"] in journaux[J + "v19.md"] and ATTENDU[R + "-calcul.py"] in journaux[J + "v19.md"],
        "journal_v19_dit_0_bloquant_0_majeur_6_mineurs": "**0 bloquant, 0 majeur, 6 mineurs**" in journaux[J + "v19.md"],
        "journal_v19_dit_modele_different": "différent du modèle A" in journaux[J + "v19.md"],
        "journal_v17_nomme_b8": ATTENDU[B % 8] in journaux[J + "v17.md"],
        "journaux_qui_nomment_la_contre_lecture_du_code_de_T08": [k for k, t in journaux.items() if "contre-lecture-1-code-t08" in t or "verification-courte-corrections-t08" in t or "verification-corrections-2-t08" in t],
    }

    # 5. VT5-07 et la table
    table = {}
    for x in s9["Marqueurs à remplir avant le scellement"].split("\n"):
        m = re.match(r"\| `([A-Z0-9_]+)` \| (.*) \| (.*) \| (.*) \|$", x)
        if m:
            table[m.group(1)] = {"quand": m.group(3), "qui": m.group(4), "longueur_ce_qui_le_remplit": len(m.group(2)),
                                 "VT5-07": m.group(2).count("VT5-07"), "T5-19": m.group(2).count("T5-19")}
    s["5_table"] = table
    s["5_VT5-07"] = {"occurrences_b8_b9": [b8.count("VT5-07"), b9.count("VT5-07")],
                     "par_section_b9": {n: c.count("VT5-07") for n, c in s9.items() if "VT5-07" in c},
                     "liste_d_arret_nomme_VT5-07": "VT5-07" in s9["Liste d'arrêt"],
                     "entree_contre_lecture_4_dit_encore_suit_T5-19_chez_Lazar": b9.count("suit T5-19 chez Lazar")}

    # 6. marqueurs et forme
    s["6_problemes_b8"] = prereg.problemes(B % 8)
    s["6_problemes_b9"] = prereg.problemes(B % 9)
    cpt = {m: b9.count(m) for m in sorted(set(prereg.GABARIT.findall(b9)))}
    s["6_marqueurs_b9"] = cpt
    s["6_marqueurs_b9_sont_les_sept_une_fois"] = cpt == {f"<<{m}>>": 1 for m in SEPT}
    s["6_section_de_chaque_marqueur_b9"] = {m: section_de(b9, b9.find(m)) for m in cpt}
    t6 = b9
    for m in SEPT:
        if m != "LIGNE_MOT_LAZAR_T5_19":
            t6 = t6.replace(f"<<{m}>>", "valeur-factice")
    s["6_validateur_six_autres_remplis"] = problemes_texte(t6, tmp, "b9-six-remplis.md")
    s["6_validateur_sept_remplis"] = problemes_texte(t6.replace("<<LIGNE_MOT_LAZAR_T5_19>>", "valeur-factice"), tmp, "b9-sept-remplis.md")
    nouveaux = [c["nouveau"] for c in couples]
    emp = sorted(set(h for x in nouveaux for h in prereg.EMPREINTE.findall(x)) - set(prereg.EMPREINTE.findall(b8)))
    emp_tous = sorted(set(h for c in couples for h in prereg.EMPREINTE.findall(c["nouveau"])) - set(h for c in couples for h in prereg.EMPREINTE.findall(c["ancien"])))
    connus = {v: k for k, v in ATTENDU.items() if v}
    s["6_empreintes_ajoutees_par_les_couples"] = {h: connus.get(h, "inconnue") for h in emp_tous}
    s["6_empreintes_neuves_au_texte"] = {h: connus.get(h, "inconnue") for h in emp}
    chemins = sorted(set(p for x in nouveaux for p in re.findall(r"`((?:brouillons|prereg|registres-provisoires)/[^`]+)`", x)))
    s["6_chemins_cites_passages_neufs"] = {p: Path(p).exists() for p in chemins}
    s["6_forme"] = {
        "mots_de_modele_dans_les_nouveaux_des_14_couples": sum(mots_de_modele(x) for x in nouveaux),
        "mots_de_modele_dans_les_anciens_des_14_couples": sum(mots_de_modele(c["ancien"]) for c in couples),
        "mots_de_modele_par_ligne_b8": {i + 1: mots_de_modele(x) for i, x in enumerate(l8) if mots_de_modele(x)},
        "mots_de_modele_par_ligne_b9": {i + 1: mots_de_modele(x) for i, x in enumerate(l9) if mots_de_modele(x)},
        "identifiants_de_session_dans_les_nouveaux": sum(len(re.findall(r"session_[0-9A-Za-z]{10,}", x)) for x in nouveaux),
        "sessions_distinctes_b8_b9": [len(set(re.findall(r"session_[0-9A-Za-z]{10,}", t))) for t in (b8, b9)],
        "modele_A_b8_b9": [b8.count("modèle A"), b9.count("modèle A")],
        "modele_B_b8_b9": [b8.count("modèle B"), b9.count("modèle B")],
        "entete_dit_VT8C_01_a_03": "VT8C-01 à VT8C-03" in s9["(en-tête)"],
        "entete_cite_rapport_b8_et_son_empreinte": (R + ".md") in s9["(en-tête)"] and ATTENDU[R + ".md"] in s9["(en-tête)"],
        "entete_cite_script_et_couples_b9": (C + "faire-couples-t08-brouillon9-v1.py") in s9["(en-tête)"] and (C + "couples-t08-brouillon9-v1.json") in s9["(en-tête)"],
        "auteurs_dit_brouillons_5_a_9": "**brouillons 5 à 9 (candidats)**" in s9["(en-tête)"],
        "titre_dit_brouillon_9": l9[0].endswith("— v1 — brouillon 9 (candidat)"),
        "relectures_suivantes_b9": b9.count("**Relecture suivante, prévue avant le scellement**"),
        "relecture_du_brouillon_8_dite_faite": b9.count("**Relecture du brouillon 8 (faite : contre-lecture 6)**"),
    }

    # 8. couples proposés
    apres, jp = appliquer(b9, PROPOSES)
    sa = decoupe(apres)
    s["8_couples_proposes"] = {
        "journal": jp, "sha_apres": sha(apres.encode("utf-8")),
        "sections_changees": [n for n in s9 if sa[n] != s9[n]],
        "gelees_et_plan_inchanges": all(sa[n] == s9[n] for n in GELEES + ["Plan d'analyse"]),
        "marqueurs_inchanges": {m: apres.count(m) for m in cpt} == cpt,
        "problemes_apres": problemes_texte(apres, tmp, "b9-apres-couples-proposes.md"),
        "mots_de_modele_dans_les_nouveaux": sum(mots_de_modele(c["nouveau"]) for c in PROPOSES)}

    print(json.dumps(s, ensure_ascii=False, indent=1))


principal()
