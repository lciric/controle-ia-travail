"""Calcul de la vérification courte du différentiel de T0.8, du brouillon 6 au brouillon 8 (candidat) — v1.

Usage (depuis la racine du dépôt) : PYTHONPATH=src python3 <ce script> DOSSIER_TEMPORAIRE
Lecture seule sur le dépôt ; écrit dans DOSSIER_TEMPORAIRE seulement (copies du brouillon 8 pour passer le validateur).
N'imprime aucun extrait des brouillons : des empreintes, des comptes, des numéros de ligne, des booléens.
"""
import difflib, hashlib, json, re, sys
from pathlib import Path

from controle_ia.prereg import problemes, GABARIT

B = "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon%d.md"
T = "brouillons/t08-code-compte4-v1/"
RAPPORT6 = "prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon6-verification-courte-v1.md"
J16 = "registres-provisoires/compte-4-2026-11-14-v16.md"
J11 = "registres-provisoires/compte-4-2026-11-14-v11.md"
J10 = "registres-provisoires/compte-4-2026-11-14-v10.md"   # empreinte seulement, jamais lu
ATTENDU = {
    B % 8: "129b1db245e186040256c8630dfb585bcd2a1e1ab4ea7b8ff817696fbd3220a7",
    B % 7: "1877e384cc639cd627b92af87f8c72775db160034d85ebf701dcc3256da4c017",
    B % 6: "ff7b0ddda5294aaba7b51276f6dfb5c857a9df4c6c0c444d723cf28fd68c92c6",
    B % 4: "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5",
    RAPPORT6: "8794f9d7f772d85b76b2d2364f5e23dc8f2843f192e8b89b90c0c0246c287322",
    T + "faire-couples-t08-brouillon7-v1.py": "3756a1bc40424ffae979607c721cfbb0e1c741f74166f3a10c982420862d51a3",
    T + "couples-t08-brouillon7-v1.json": "ee0eec6ce32d31938ba6942fa74db51dfa41ffd4066da10d2174dd298c8fee93",
    T + "sortie-application-t08-brouillon7-v1.json": "9564d885e24ff82a65904b91466dcd3963b2bb471ae371cafc1819133d2aa709",
    T + "faire-couples-t08-brouillon8-v1.py": "f0ab03563a68b3b4789ca4c672b3fcc7e3ac5306871a8e31ca629fa090361883",
    T + "couples-t08-brouillon8-v1.json": "8451cb7e7ecbad8e8c643c8787327712b36705d7552e456338a9ca3475e466b4",
    T + "sortie-application-t08-brouillon8-v1.json": "cbff15303c05f85778141e21489daf638273f7292284b5dc3aedeb0c7082b869",
    T + "appliquer-couples-t08-v1.py": "87e8464236a57ecbade88c90df0d98c50d0f3a502afc3ce81be913cb6f845c31",
    J16: "190fb7ed632c52c36f3ece7d837b84d9f9529f830553bf46c1ae10021cec9288",
    J11: "d1784495329b1aafb08e7c6193aa4835b1d8d6137a4055e40bc9d38b0905c74e",
}
GELEES = ["Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Critères de lecture gelés", "Liste d'arrêt"]
SEPT = ["CODE_MOTS_ET_COUT_T06", "RUN_7B", "EMPREINTES_ENTREES_7B", "ENTROPIE_T08", "GO_T08", "LIGNE_DEPENSE_T08", "LIGNE_MOT_LAZAR_T5_19"]
MOT = "go a pour T5-19"
MOTS_MODELE = re.compile(r"claude|opus|sonnet|haiku|fable|anthropic|openai|gpt|gemini|llama|mistral|qwen|deepseek|gemma", re.I)
SESSION = re.compile(r"session_[0-9A-Za-z]{10,}")
HEX64 = re.compile(r"\b[0-9a-f]{64}\b")
CHEMIN = re.compile(r"`((?:brouillons|prereg|registres-provisoires)/[^`<> ]+)`")

PROPOSES = [
 {"id": "VT8C-01", "constat": "VT8-01",
  "ancien": "s'écrit au remplissage de `MOT_LAZAR_T5_19`.",
  "nouveau": "s'écrit au remplissage de `MOT_LAZAR_T5_19` (marqueur du brouillon 7 ; au brouillon 8, ce marqueur étant rempli par le mot de Lazar, elle s'écrit au remplissage de `LIGNE_MOT_LAZAR_T5_19`)."},
 {"id": "VT8C-02", "constat": "VT8-02",
  "ancien": "**non scellable avant son mot** (marqueur `MOT_LAZAR_T5_19`, plan, point 1) ;",
  "nouveau": "**non scellable avant son mot** (marqueur `MOT_LAZAR_T5_19` du brouillon 7, plan, point 1 ; mot donné, brouillon 8 : non scellable avant son inscription par la session mère, marqueur `LIGNE_MOT_LAZAR_T5_19`) ;"},
 {"id": "VT8C-03", "constat": "VT8-03",
  "ancien": "liste des marqueurs de l'en-tête complétée ; déclaration de vue bornée au brouillon 8 ;",
  "nouveau": "liste des marqueurs de l'en-tête complétée ; ligne de la table des marqueurs et renvoi de l'entrée « Contre-lecture du code de T0.8 » portés au marqueur neuf ; déclaration de vue bornée au brouillon 8 et étendue à ce que son auteur a lu de (ii-b) ;"},
]


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lire(p): return Path(p).read_text(encoding="utf-8")
def court(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def sections(texte):
    m = re.split(r"^## +(.+?)\s*$", texte, flags=re.M)
    d = {"(en-tête)": m[0]}
    for t, c in zip(m[1::2], m[2::2]):
        d[t.strip()] = c
    return d


def section_de(texte, pos):
    nom = "(en-tête)"
    for m in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M):
        if m.start() <= pos:
            nom = m.group(1).strip()
    return nom


def rejouer(texte, couples):
    journal = []
    for c in couples:
        n = texte.count(c["ancien"])
        pos = texte.find(c["ancien"])
        journal.append({"id": c["id"], "occurrences_avant": n, "section": section_de(texte, pos) if n else None,
                        "ligne": texte.count("\n", 0, pos) + 1 if n else None,
                        "long_ancien": len(c["ancien"]), "long_nouveau": len(c["nouveau"]),
                        "ancien_different_du_nouveau": c["ancien"] != c["nouveau"]})
        if n == 1:
            texte = texte.replace(c["ancien"], c["nouveau"], 1)
    return texte, journal


def blocs(a, b, tb):
    out = []
    la, lb = a.split("\n"), b.split("\n")
    pos = [0]
    for l in lb: pos.append(pos[-1] + len(l) + 1)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
        if op != "equal":
            out.append({"op": op, "avant": [i1 + 1, i2], "apres": [j1 + 1, j2], "section_apres": section_de(tb, pos[j1])})
    return out


def principal():
    tmp = Path(sys.argv[1]); tmp.mkdir(parents=True, exist_ok=True)
    R = {}
    R["0_empreintes"] = {p: {"sha": sha(p), "egale_a_la_consigne": sha(p) == s,
                              "compagnon": Path(p + ".sha256").read_text().split()[0] == sha(p)} for p, s in ATTENDU.items()}
    R["0_empreinte_journal_v10_non_lu"] = sha(J10)
    t4, t6, t7, t8 = (lire(B % k) for k in (4, 6, 7, 8))
    c7 = json.loads(lire(T + "couples-t08-brouillon7-v1.json")); c8 = json.loads(lire(T + "couples-t08-brouillon8-v1.json"))

    # 1. différentiel
    r7, j7 = rejouer(t6, c7); r8, j8 = rejouer(r7, c8)
    R["1_rejeu_b6_vers_b7"] = {"nombre_couples": len(c7), "ids": [c["id"] for c in c7], "cles": sorted({k for c in c7 for k in c}),
                               "sha_rejeu": hashlib.sha256(r7.encode()).hexdigest(), "egal_b7_a_l_octet": r7 == t7, "journal": j7}
    R["1_rejeu_b7_vers_b8"] = {"nombre_couples": len(c8), "ids": [c["id"] for c in c8], "cles": sorted({k for c in c8 for k in c}),
                               "sha_rejeu": hashlib.sha256(r8.encode()).hexdigest(), "egal_b8_a_l_octet": r8 == t8, "journal": j8}
    for n, base, cpl, sortie in (("7", B % 6, T + "couples-t08-brouillon7-v1.json", B % 7), ("8", B % 7, T + "couples-t08-brouillon8-v1.json", B % 8)):
        s = json.loads(lire(T + f"sortie-application-t08-brouillon{n}-v1.json"))
        R[f"1_sortie_application_versee_b{n}"] = {"sha_base_egale": s["sha_base"] == sha(base), "sha_couples_egale": s["sha_couples"] == sha(cpl),
                                                  "sha_sortie_egale": s["sha_sortie"] == sha(sortie), "nombre_couples": s["nombre_couples"],
                                                  "marqueurs_permis_restants": s["marqueurs_permis_restants"]}
    R["1_lignes_changees_b6_vers_b7"] = blocs(t6, t7, t7)
    R["1_lignes_changees_b7_vers_b8"] = blocs(t7, t8, t8)
    R["1_lignes_changees_b6_vers_b8"] = blocs(t6, t8, t8)
    R["1_dates_en_tete_b8"] = re.findall(r"brouillon (\d) écrit le (\d{4}-\d{2}-\d{2}) à partir de (\d{2}:\d{2}) UTC", t8)

    # 2. fidélité au rapport du brouillon 6
    sec = lire(RAPPORT6).split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    rap = json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))
    R["2_fidelite"] = {"ids_rapport": [c["id"] for c in rap],
                       "deux_premiers_couples_egaux_au_rapport": [(c["id"], c["ancien"], c["nouveau"]) for c in c7[:2]] == [(c["id"], c["ancien"], c["nouveau"]) for c in rap],
                       "constats_du_rapport_par_gravite": {g: len(re.findall(r"^- \*\*VT6-\d\d — " + g, lire(RAPPORT6), flags=re.M)) for g in ("bloquant", "majeur", "mineur")},
                       "verdict_du_rapport_conforme_apres": "**Conforme après les corrections listées.**" in lire(RAPPORT6)}
    cl = sections(t8)["Contre-lecture"]
    e5 = cl.split("- **Contre-lecture 5**", 1)[1].split("\n", 1)[0]
    R["2_entree_contre_lecture_5"] = {"longueur": len(e5), "empreintes": sorted(set(HEX64.findall(e5))),
                                      "constats_nommes": sorted(set(re.findall(r"VT6-\d\d", e5))), "couples_nommes": sorted(set(re.findall(r"VT6C-\d\d", e5))),
                                      "dit_0_bloquant_3_majeurs_4_mineurs": "0 bloquant, 3 majeurs, 4 mineurs" in e5,
                                      "dit_14_couples": "le rejeu des 14 couples rend le brouillon 6 à l'octet" in e5,
                                      "occurrences_MOT_LAZAR_T5_19_hors_LIGNE": len(re.findall(r"(?<!LIGNE_)MOT_LAZAR_T5_19", e5)),
                                      "occurrences_LIGNE_MOT_LAZAR_T5_19": e5.count("LIGNE_MOT_LAZAR_T5_19")}

    # 3. mot de Lazar
    j16 = lire(J16)
    s6, s7, s8, s4 = sections(t6), sections(t7), sections(t8), sections(t4)
    def ligne_t5(t): return [l for l in t.split("\n") if "phrase ajoutée au brouillon 5, VCT8B-01" in l]
    l6, l7, l8 = ligne_t5(t6), ligne_t5(t7), ligne_t5(t8)
    coupe = "(phrase ajoutée au brouillon 5, VCT8B-01 ; nœud de Lazar, "
    R["3_mot_de_Lazar"] = {
        "journal_v16_ligne_citee_egale_au_mot": f"\n> {MOT}\n" in j16, "journal_v16_lignes_de_citation": len(re.findall(r"^> ", j16, flags=re.M)),
        "occurrences_du_mot_entre_guillemets_b8": t8.count(f"« {MOT} »"), "occurrences_du_mot_b7": t7.count(MOT),
        "lignes_du_mot_b8": [i + 1 for i, l in enumerate(t8.split("\n")) if MOT in l],
        "ligne_T5_19_unique_b6_b7_b8": [len(l6), len(l7), len(l8)],
        "phrase_avant_la_parenthese_egale_b6_b8": l6[0].split(coupe)[0] == l8[0].split(coupe)[0],
        "phrase_avant_la_parenthese_egale_b6_b7": l6[0].split(coupe)[0] == l7[0].split(coupe)[0],
        "longueur_phrase_avant_la_parenthese": len(l8[0].split(coupe)[0]),
        "parenthese_presente_une_fois_b6_b7_b8": [l.count(coupe) for l in (l6[0], l7[0], l8[0])],
        "fin_de_ligne_apres_parenthese_b8_se_termine_par_marqueur": l8[0].endswith("`<<LIGNE_MOT_LAZAR_T5_19>>`) ;"),
        "option_dite_b8_ligne_du_plan": "**gardée**, option (a)" in l8[0],
        "occurrences_code_inchange_b8": t8.count("code inchangé"), "occurrences_option_a_b8": t8.count("option (a)"),
        "occurrences_VT5-07_b6_b8": [t6.count("VT5-07"), t8.count("VT5-07")],
        "MOT_LAZAR_T5_19_en_marqueur_b7_b8": [t7.count("<<MOT_LAZAR_T5_19>>"), t8.count("<<MOT_LAZAR_T5_19>>")],
    }

    # 4. sections gelées
    R["4_titres_egaux_b4_b8"] = list(s4) == list(s8)
    R["4_sections"] = {n: {"b8_egale_b4": s8[n] == s4.get(n), "b8_egale_b6": s8[n] == s6.get(n), "b8_egale_b7": s8[n] == s7.get(n),
                           "sha4": court(s4.get(n, "")), "sha8": court(s8[n]),
                           "couples_b7": [j["id"] for j in j7 if j["section"] == n], "couples_b8": [j["id"] for j in j8 if j["section"] == n]} for n in s8}
    R["4_gelees_egales_a_l_octet_au_b4"] = {n: s8[n] == s4[n] for n in GELEES}
    p4, p8 = s4["Plan d'analyse"].split("\n"), s8["Plan d'analyse"].split("\n")
    ops = [o for o in difflib.SequenceMatcher(None, p4, p8, autojunk=False).get_opcodes() if o[0] != "equal"]
    ajout = [p8[k] for o in ops for k in range(o[3], o[4])]
    sans = [l for l in p8 if l not in ajout]
    R["4_plan"] = {"operations_b4_vers_b8": ops, "ajout_une_seule_ligne": len(ajout) == 1 and all(o[0] == "insert" for o in ops),
                   "plan8_sans_l_ajout_egal_plan4": sans == p4, "ligne_ajoutee_est_la_ligne_T5_19": ajout == l8,
                   "longueur_ajout": len(ajout[0]) if ajout else None}

    # 5. marqueurs
    def marq(t): return {m: t.count(m) for m in sorted(set(GABARIT.findall(t)))}
    R["5_problemes"] = {f"b{k}": problemes(B % k) for k in (6, 7, 8)}
    R["5_marqueurs_b8"] = marq(t8)
    R["5_marqueurs_b8_sont_les_sept"] = marq(t8) == {f"<<{m}>>": 1 for m in sorted(SEPT)}
    table = s8["Marqueurs à remplir avant le scellement"]
    lignes_table = {m.group(1): [x.strip() for x in m.group(0).split("|")[1:-1]] for m in re.finditer(r"^\| `([A-Z0-9_]+)` \|.*$", table, flags=re.M)}
    R["5_table"] = {k: {"quand": v[2], "qui": v[3], "longueur_ce_qui_le_remplit": len(v[1])} for k, v in lignes_table.items()}
    R["5_table_nomme_les_sept"] = all(m in lignes_table for m in SEPT)
    ent = [l for l in s8["(en-tête)"].split("\n") if l.startswith("- **Marqueurs restants**")][0]
    liste = ent.split(") : ", 1)[1].split(". Remplis", 1)[0]
    R["5_en_tete_liste_des_restants"] = re.findall(r"`([A-Z0-9_]+)`", liste)
    R["5_en_tete_nomme_les_sept"] = sorted(re.findall(r"`([A-Z0-9_]+)`", liste)) == sorted(SEPT)
    R["5_en_tete_dit_sept"] = "(sept, une occurrence chacun" in ent
    # épreuve du validateur sur copies temporaires
    def essai(nom, remplis):
        t = t8
        for m in remplis: t = t.replace(f"<<{m}>>", "REMPLI")
        f = tmp / nom; f.write_text(t, encoding="utf-8"); return problemes(f)
    R["5_validateur_six_autres_remplis"] = essai("b8-six-remplis.md", [m for m in SEPT if m != "LIGNE_MOT_LAZAR_T5_19"])
    R["5_validateur_sept_remplis"] = essai("b8-sept-remplis.md", SEPT)

    # 6. déclaration de vue
    aut = [l for l in s8["(en-tête)"].split("\n") if l.startswith("- **Auteurs**")][0]
    vue = aut.split("**Ce qu'elle a vu avant le scellement**", 1)[1]
    aut6 = [l for l in s6["(en-tête)"].split("\n") if l.startswith("- **Auteurs**")][0].split("**Ce qu'elle a vu avant le scellement**", 1)[1]
    R["6_declaration_de_vue"] = {"longueur_b6_b8": [len(aut6), len(vue)], "occurrences_ii_b_dans_la_declaration": vue.count("(ii-b)"),
                                 "occurrences_ii_b_b8_entier": t8.count("(ii-b)"), "occurrences_ii_b_b6": t6.count("(ii-b)"),
                                 "lignes_ii_b_b8": [i + 1 for i, l in enumerate(t8.split("\n")) if "(ii-b)" in l],
                                 "chiffres_dans_la_declaration_hors_identifiants": re.findall(r"(?<![A-Za-z0-9-])\d+(?:[,.]\d+)?", re.sub(r"VT\d-\d\d|T0\.\d|P3|7a|7b|C7|brouillon \d", "", vue)),
                                 "mots_seuil_regle_reglage": {m: vue.count(m) for m in ("seuil", "règle", "réglage", "critère")},
                                 "mentions": {m: vue.count(m) for m in ("7a", "7b", "pièce HD", "sonde", "factices", "consigne privée")},
                                 "section_Ce_que_les_auteurs_savaient_egale_b4": s8["Ce que les auteurs savaient avant le scellement"] == s4["Ce que les auteurs savaient avant le scellement"],
                                 "contre_lecture_du_code_nommee_dans_la_declaration": "contre-lecture du code" in vue or "contre-lecture 1 de son code" in vue.split("(ii-b)")[0]}

    # 7. faits cités, forme
    neufs = "\n".join(c["nouveau"] for c in c7 + c8)
    connus = {sha(p): p for p in list(ATTENDU) + [J10]}
    R["7_empreintes_des_passages_neufs"] = {h: connus.get(h, "INCONNUE") for h in sorted(set(HEX64.findall(neufs)))}
    R["7_chemins_cites_passages_neufs"] = {p: Path(p).exists() for p in sorted(set(CHEMIN.findall(neufs)))}
    R["7_journal_v11"] = {"entrees": re.findall(r"^## (C4-\d{4})", lire(J11), flags=re.M), "cite_empreinte_rapport_b6": ATTENDU[RAPPORT6] in lire(J11),
                          "cite_empreinte_b7": ATTENDU[B % 7] in lire(J11), "cite_empreinte_journal_v10_egale_au_disque": sha(J10) in lire(J11),
                          "dit_modeles_differents": "**différents**" in lire(J11)}
    R["7_journal_v16"] = {"entrees": re.findall(r"^## (C4-\d{4})", j16, flags=re.M)}
    def mm(t): return {str(i + 1): len(MOTS_MODELE.findall(l)) for i, l in enumerate(t.split("\n")) if MOTS_MODELE.search(l)}
    R["7_forme"] = {"mots_de_modele_par_ligne_b6": mm(t6), "mots_de_modele_par_ligne_b8": mm(t8),
                    "mots_de_modele_dans_les_passages_neufs": len(MOTS_MODELE.findall(neufs)),
                    "identifiants_de_session_passages_neufs": len(SESSION.findall(neufs)),
                    "sessions_distinctes_b6_b8": [len(set(SESSION.findall(t6))), len(set(SESSION.findall(t8)))],
                    "modele_A_b6_b8": [t6.count("modèle A"), t8.count("modèle A")], "modele_B_b6_b8": [t6.count("modèle B"), t8.count("modèle B")],
                    "entrees_contre_lecture_b8": re.findall(r"^\s*-?\s*\**Contre-lecture (\d+)\**", cl, flags=re.M)}

    # 8. couples proposés
    r9, j9 = rejouer(t8, PROPOSES)
    f = tmp / "b8-apres-couples-proposes.md"; f.write_text(r9, encoding="utf-8")
    s9 = sections(r9)
    R["8_couples_proposes"] = {"journal": j9, "sha_apres": hashlib.sha256(r9.encode()).hexdigest(),
                               "sections_changees": [n for n in s8 if s8[n] != s9[n]], "marqueurs_inchanges": marq(r9) == marq(t8),
                               "problemes_apres": problemes(f), "mots_de_modele_dans_les_nouveaux": sum(len(MOTS_MODELE.findall(c["nouveau"])) for c in PROPOSES)}
    print(json.dumps(R, ensure_ascii=False, indent=1))


principal()
