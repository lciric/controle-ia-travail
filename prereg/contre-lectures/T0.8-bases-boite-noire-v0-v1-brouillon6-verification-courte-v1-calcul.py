"""Vérification courte du différentiel de T0.8, du brouillon 5 au brouillon 6 (candidat) — calcul, v1.

Lecture seule ; à lancer depuis la racine du dépôt : PYTHONPATH=src python3 <ce fichier>
N'imprime aucun extrait des brouillons : des identifiants de couples, des numéros de ligne, des nombres, des
empreintes et des titres de sections seulement (aucun identifiant de modèle dans la sortie).
"""
import difflib, hashlib, json, re, sys
from pathlib import Path

from controle_ia.prereg import problemes, GABARIT

B = "brouillons/T0.8-bases-boite-noire-v0-v1-brouillon%d.md"
CL = "prereg/contre-lectures/T0.8-bases-boite-noire-v0-v1-brouillon5-verification-courte-v%d.md"
COUPLES = "brouillons/t08-code-compte4-v1/couples-t08-brouillon6-v1.json"
SORTIE_APPL = "brouillons/t08-code-compte4-v1/sortie-application-t08-brouillon6-v1.json"
ATTENDU = {
    B % 6: "ff7b0ddda5294aaba7b51276f6dfb5c857a9df4c6c0c444d723cf28fd68c92c6",
    B % 5: "0c0e43270a819974168646406e349f48b6441d9afbdfaeb9d78b976228aba22b",
    B % 4: "7da0c3839a7a714b441b018b3cceb704ec431434498653db1496ca839c38c5b5",
    CL % 3: "f788bb73baa0d71f826d4778c2b2e2c55baa20383f2f49e777d670d849df6d7e",
}
GELEES = ["Hypothèse", "Prédiction chiffrée et signe attendu", "Métrique", "Seuil", "Critères de lecture gelés", "Liste d'arrêt"]
PLAN = "Plan d'analyse"
# mots cherchés pour les identifiants de modèles (comptés, jamais recopiés)
MOTS = re.compile(r"claude|opus|sonnet|haiku|fable|anthropic|gpt|gemini", re.I)
# couples proposés par ce rapport (section 3)
PROPOSES = [
 {"id": "VT6C-01", "constat": "VT6-01",
  "ancien": "script `brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon6-v1.py` ; aucune autre ligne ne change.",
  "nouveau": "ajoute l'entrée « Contre-lecture 4 » et la relecture suivante (section « Contre-lecture ») et met à jour le titre et, dans cet en-tête, les lignes « Auteurs » et « Date » ; script `brouillons/t08-code-compte4-v1/faire-couples-t08-brouillon6-v1.py`, couples `brouillons/t08-code-compte4-v1/couples-t08-brouillon6-v1.json` ; aucune autre ligne ne change."},
 {"id": "VT6C-02", "constat": "VT6-04",
  "ancien": "**non scellable avant la vérification courte du différentiel du brouillon 4 au brouillon 5** et avant les six marqueurs.",
  "nouveau": "**non scellable avant la vérification courte du différentiel du brouillon 5 au brouillon 6** (celle du brouillon 4 au brouillon 5 est faite : contre-lecture 4), avant le mot de Lazar sur T5-19 et avant les six marqueurs."},
]


def sha(b): return hashlib.sha256(b).hexdigest()
def court(s): return sha(s.encode("utf-8"))[:16]
def lire(ch): return Path(ch).read_bytes()

def compagnon(ch):
    p = Path(ch + ".sha256")
    return p.exists() and p.read_text(encoding="utf-8").split()[0] == sha(lire(ch))

def decoupe(texte):
    """Sections de niveau 2, à l'octet (titre compris) ; « (en-tête) » avant le premier titre."""
    m = list(re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M))
    d = {"(en-tête)": texte[:m[0].start()]}
    for k, e in enumerate(m):
        d[e.group(1).strip()] = texte[e.start(): m[k + 1].start() if k + 1 < len(m) else len(texte)]
    return d

def section_de(texte, pos):
    titre = "(en-tête)"
    for e in re.finditer(r"^## +(.+?)\s*$", texte, flags=re.M):
        if e.start() <= pos: titre = e.group(1).strip()
        else: break
    return titre

def ligne_de(texte, pos): return texte.count("\n", 0, pos) + 1

def rejouer(texte, couples):
    journal = []
    for c in couples:
        n = texte.count(c["ancien"])
        pos = texte.find(c["ancien"])
        journal.append({"id": c["id"], "occurrences_avant": n, "section": section_de(texte, pos) if n else None,
                        "ligne": ligne_de(texte, pos) if n else None,
                        "long_ancien": len(c["ancien"]), "long_nouveau": len(c["nouveau"]),
                        "nouveau_finit_ou_commence_par_ancien": c["nouveau"].startswith(c["ancien"]) or c["nouveau"].endswith(c["ancien"])})
        if n != 1: raise SystemExit(f"ARRÊT : {c['id']} trouvé {n} fois")
        texte = texte.replace(c["ancien"], c["nouveau"], 1)
    return texte, journal

def bloc_json(ch):
    sec = Path(ch).read_text(encoding="utf-8").split("## 3. Couples", 1)[1].split("## 4.", 1)[0]
    return json.loads(re.search(r"```json\n(.*?)\n```", sec, re.S).group(1))

def mots_par_ligne(texte):
    d = {}
    for i, l in enumerate(texte.split("\n"), 1):
        n = len(MOTS.findall(l))
        if n: d[str(i)] = n
    return d

r = {}
# 0. empreintes
r["0_empreintes"] = {ch: {"sha": sha(lire(ch)), "egale_a_la_consigne": sha(lire(ch)) == s, "compagnon": compagnon(ch)} for ch, s in ATTENDU.items()}
for ch in (CL % 1, CL % 2, COUPLES, SORTIE_APPL):
    r["0_empreintes"][ch] = {"sha": sha(lire(ch)), "compagnon": compagnon(ch)}
b4, b5, b6 = (lire(B % k).decode("utf-8") for k in (4, 5, 6))
couples = json.loads(Path(COUPLES).read_text(encoding="utf-8"))

# 1. rejeu
rej, journal = rejouer(b5, couples)
r["1_rejeu"] = {"nombre_couples": len(couples), "ids": [c["id"] for c in couples], "cles_des_couples": sorted({k for c in couples for k in c}),
                "sha_rejeu": sha(rej.encode("utf-8")), "rejeu_egal_b6_a_l_octet": rej.encode("utf-8") == lire(B % 6), "journal": journal}
sa = json.loads(Path(SORTIE_APPL).read_text(encoding="utf-8"))
r["1_sortie_application_versee"] = {"sha_base_egale": sa["sha_base"] == sha(lire(B % 5)), "sha_couples_egale": sa["sha_couples"] == sha(lire(COUPLES)),
                                    "sha_sortie_egale_b6": sa["sha_sortie"] == sha(lire(B % 6)), "nombre_couples": sa["nombre_couples"]}
l5, l6 = b5.split("\n"), b6.split("\n")
r["1_lignes_changees"] = [{"op": op, "b5": [i1 + 1, i2], "b6": [j1 + 1, j2], "section_b6": section_de(b6, len("\n".join(l6[:j1])) + 1)}
                          for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, l5, l6, autojunk=False).get_opcodes() if op != "equal"]

# 2. fidélité
v3, v1, v2 = bloc_json(CL % 3), bloc_json(CL % 1), bloc_json(CL % 2)
r["2_fidelite"] = {"ids_rapport_v3": [c["id"] for c in v3],
                   "quatre_premiers_couples_egaux_au_rapport_v3": [{"id": c["id"], "ancien": c["ancien"], "nouveau": c["nouveau"]} for c in v3] == couples[:4],
                   "bloc_v1_egal_v3": v1 == v3, "bloc_v2_egal_v3": v2 == v3,
                   "constats_du_rapport_v3_par_gravite": {g: len(re.findall(r"^- \*\*VT5-\d\d — " + g, Path(CL % 3).read_text(encoding="utf-8"), flags=re.M)) for g in ("bloquant", "majeur", "mineur")}}

# 3. sections
s4, s5, s6 = decoupe(b4), decoupe(b5), decoupe(b6)
r["3_titres_egaux_b4_b6"] = list(s4) == list(s6)
r["3_sections"] = {t: {"b6_egale_b4": s6[t] == s4.get(t), "b6_egale_b5": s6[t] == s5.get(t), "sha4": court(s4.get(t, "")), "sha6": court(s6[t]),
                       "couples": [j["id"] for j in journal if j["section"] == t]} for t in s6}
r["3_gelees_egales_a_l_octet_au_b4"] = {t: s6[t] == s4[t] for t in GELEES}
p4, p5, p6 = s4[PLAN].split("\n"), s5[PLAN].split("\n"), s6[PLAN].split("\n")
ops = [o for o in difflib.SequenceMatcher(None, p4, p6, autojunk=False).get_opcodes() if o[0] != "equal"]
ajout = [p6[j] for o in ops for j in range(o[3], o[4])]
sans = [l for k, l in enumerate(p6) if not any(o[3] <= k < o[4] for o in ops)]
ligne5 = [l for l in p5 if l not in p4]
attendue = ligne5[0] if len(ligne5) == 1 else None
for c in couples:
    if c["id"] in ("VT5C-04", "T6-04") and attendue is not None:
        attendue = attendue.replace(c["ancien"], c["nouveau"], 1) if attendue.count(c["ancien"]) == 1 else None
r["3_plan"] = {"operations_b4_vers_b6": [[o[0], o[1] + 1, o[2], o[3] + 1, o[4]] for o in ops], "ajout_une_seule_ligne": len(ajout) == 1,
               "plan6_sans_l_ajout_egal_plan4": sans == p4, "longueur_ajout": len(ajout[0]) if len(ajout) == 1 else None,
               "ligne_ajoutee_b5_unique": len(ligne5) == 1,
               "ligne_b6_egale_ligne_b5_apres_VT5C-04_et_T6-04_seuls": len(ajout) == 1 and attendue == ajout[0],
               "chiffres_dans_la_ligne_b6_hors_identifiants": len(re.findall(r"\d", re.sub(r"VCT8B-01|VT5-03|T0\.8|t08|7b|brouillon 5|point 1|CODE-T08|SCELLEMENT-T08", "", ajout[0]))) if len(ajout) == 1 else None,
               "couples_dans_le_plan": [j["id"] for j in journal if j["section"] == PLAN]}

# 4. statut de T5-19 : comptes de mots, sans extrait
r["4_statut"] = {m: {"b5": b5.count(m), "b6": b6.count(m), "lignes_b6": [i for i, l in enumerate(l6, 1) if m in l]}
                 for m in ("soumise à la session mère", "nœud de Lazar", "non scellable avant son mot", "en attente de son mot", "non scellable avant")}
r["4_marqueur_pour_le_mot_de_Lazar"] = sorted(set(GABARIT.findall(b6)))

# 6. faits cités dans les passages neufs
neuf = "\n".join(c["nouveau"] for c in couples)
emp = sorted(set(re.findall(r"\b[0-9a-f]{64}\b", neuf)))
connues = {sha(lire(ch)): ch for ch in (B % 5, B % 4, CL % 1, CL % 2, CL % 3)}
r["6_empreintes_des_passages_neufs"] = {e: connues.get(e, "NON RATTACHÉE") for e in emp}
r["6_chemins_cites_passages_neufs"] = {ch: Path(ch).exists() for ch in sorted(set(re.findall(r"`((?:brouillons|prereg)/[^`]+)`", neuf)))}
d = re.search(r"brouillon 6 écrit le (\d{4}-\d{2}-\d{2}) à partir de (\d{2}:\d{2}) UTC", b6)
r["6_date_du_brouillon_6"] = list(d.groups()) if d else None

# 7. forme
r["7_forme"] = {"problemes_b6": problemes(B % 6), "problemes_b5": problemes(B % 5),
                "marqueurs_b6": {m: b6.count(m) for m in sorted(set(GABARIT.findall(b6)))},
                "mots_de_modele_par_ligne_b5": mots_par_ligne(b5), "mots_de_modele_par_ligne_b6": mots_par_ligne(b6),
                "mots_de_modele_dans_les_passages_neufs": len(MOTS.findall(neuf)),
                "modele_A": {"b5": b5.count("modèle A"), "b6": b6.count("modèle A")}, "modele_B": {"b5": b5.count("modèle B"), "b6": b6.count("modèle B")},
                "identifiants_de_session_passages_neufs": len(re.findall(r"session_[0-9A-Za-z]{10,}", neuf))}

# 8. couples proposés
t, jp = rejouer(b6, PROPOSES)
sp = decoupe(t)
tmp = Path(sys.argv[1]) if len(sys.argv) > 1 else None
pb = None
if tmp is not None:
    tmp.write_text(t, encoding="utf-8"); pb = problemes(tmp)
r["8_couples_proposes"] = {"journal": jp, "sha_apres": sha(t.encode("utf-8")), "sections_changees": [k for k in sp if sp[k] != s6[k]],
                           "marqueurs_inchanges": sorted(GABARIT.findall(t)) == sorted(GABARIT.findall(b6)), "problemes_apres": pb,
                           "mots_de_modele_dans_les_nouveaux": sum(len(MOTS.findall(c["nouveau"])) for c in PROPOSES)}
print(json.dumps(r, ensure_ascii=False, indent=1))
