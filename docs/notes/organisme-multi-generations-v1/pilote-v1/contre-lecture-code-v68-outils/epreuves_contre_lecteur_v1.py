"""Épreuves directes du contre-lecteur sur le code v68 du pilote MR-2 — v1 (outil de `contre-lecture-code-pilote-v68-v1.md`).

Aucun réseau hors de la boucle locale (un relais à amont factice), aucune clé, aucun appel de modèle. Les mondes de
développement (secret public nul) sont lus pour deux épreuves ; **rien de leur contenu n'est écrit** : la sortie ne porte que
des booléens, des comptes, des motifs du gardien et des empreintes.

  ulimit -v 6000000 ; OMP_NUM_THREADS=2 python3 -I -B epreuves_contre_lecteur_v1.py ORCHESTRATEUR MONDES.json SHA BAC SORTIE.json
"""

import copy
import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

ORCH, MONDES, SHA_MONDES, BAC, SORTIE = sys.argv[1:6]
sys.path.insert(0, ORCH)
from pole import audit_pilote_v68 as AU  # noqa: E402
from pole import pilote_mr2_v68 as P  # noqa: E402
from pole import proposeurs_pilote_v68 as PR  # noqa: E402

import importlib.util  # noqa: E402

_s = importlib.util.spec_from_file_location("commande_v68", os.path.join(ORCH, "exemples", "pilote-mr2-v68", "commandes",
                                                                         "commande_pilote_v68.py"))
C = importlib.util.module_from_spec(_s)
_s.loader.exec_module(C)
CONF = os.path.join(ORCH, "exemples", "pilote-mr2-v68", "configuration-pilote-mr2-v9.json")
V4, M, MP = P.charger_mr2()
import numpy as np  # noqa: E402

res = {}
os.makedirs(BAC, exist_ok=True)
conf, _ = PR.lire_configuration(CONF)
F0 = {"type": "softmax", "poids": [[0.0] * 8] * 3, "biais": [0.0, 0.0, 0.0]}

# E1 — appel « complet », témoin conforme, mais aucun corps du relais sur disque : arrêt attendu par le texte (« réponse brute
# (corps entier…) absente → arrêt »).
texte = "consigne d'épreuve"
sha_t = hashlib.sha256(texte.encode()).hexdigest()


class R1:
    returncode, stderr = 0, ""
    stdout = json.dumps({"etat": "complet", "texte": "[]", "cout_usd": 0.1, "consigne_sha256": sha_t,
                         "temoin_relais": {"relais": "relais-pilote-v68-astra", "consigne_recue_sha256": sha_t,
                                           "outils": [], "messages": 1, "systeme": None}})


try:
    a = PR.appeler(conf, "astra", texte, os.path.join(BAC, "e1", "astra"), executer=lambda *x, **k: R1())
    res["E1_complet_sans_corps_du_relais"] = {"arret": False, "etat": a["etat"], "corps_relais_sha256": a["corps_relais_sha256"]}
except PR.ArretPilote as e:
    res["E1_complet_sans_corps_du_relais"] = {"arret": True, "motif": str(e)}

# E1b — corps présent mais la dernière ligne ne rend aucune empreinte du corps : admis ?


def ex_1b(cmd, **k):
    with open(cmd[cmd.index("--sortie-brute") + 1], "w") as f:
        f.write("{}")
    return R1()


try:
    a = PR.appeler(conf, "astra", texte, os.path.join(BAC, "e1b", "astra"), executer=ex_1b)
    res["E1b_corps_sans_empreinte_rendue"] = {"arret": False, "etat": a["etat"]}
except PR.ArretPilote as e:
    res["E1b_corps_sans_empreinte_rendue"] = {"arret": True, "motif": str(e)}

# E2 — délai de l'adaptateur (la commande est tuée, aucune dernière ligne) : « échec » et abandon du proposeur, ou arrêt du pilote ?


def ex_2(cmd, **k):
    raise subprocess.TimeoutExpired(cmd, k.get("timeout"), output="", stderr="")


try:
    a = PR.appeler(conf, "astra", texte, os.path.join(BAC, "e2", "astra"), executer=ex_2)
    res["E2_delai_de_l_adaptateur"] = {"arret_du_pilote": False, "etat": a["etat"], "panne": a["panne"]}
except PR.ArretPilote as e:
    res["E2_delai_de_l_adaptateur"] = {"arret_du_pilote": True, "motif": str(e)}

# E3 — forme des identifiants servis.
res["E3_modele_servi"] = {s: C.modele_conforme(d, s) for d, s in (
    ("gpt-6-astra", "gpt-6-astra"), ("gpt-6-astra", "gpt-6-astra-2026-10-15"), ("gpt-6-astra", "gpt-6-astra-20261015"),
    ("gemini-4-argon", "gemini-4-argon-001"), ("gemini-4-argon", "gemini-4-argon-preview-10-2026"),
    ("gemini-4-argon", "models/gemini-4-argon"), ("claude-opus-5-5", "claude-opus-5-5"))}

# E4 — une feuille softmax hors de ±4 est refusée ; la même loi écrite « transformee » (puissance) dans la grammaire servie.
w = [[5.25, 0, 0, 0, 0, 0, 0, 0], [0.0] * 8, [-2.0, 0, 0, 1.0, 0, 0, 0, 0]]
hors = {"type": "softmax", "poids": w, "biais": [0.3, 0.0, -0.1]}
g = 5.25 / 4.0
dedans = {"type": "transformee", "puissance": g,
          "base": {"type": "softmax", "poids": [[x / g for x in l] for l in w], "biais": [0.3 / g, 0.0, -0.1 / g]}}
arbre_hors = {"type": "si_sinon", "condition": {"indice": 2, "seuil": 0.1}, "si": hors, "sinon": F0}
arbre_dedans = {"type": "si_sinon", "condition": {"indice": 2, "seuil": 0.1}, "si": dedans, "sinon": F0}
rng = np.random.default_rng(np.random.SeedSequence(20261113))
Z, G = M.tirer_instances(rng, 4000, 8, 3)
res["E4_borne_et_transformee"] = {"softmax_5_25": P.garder_loi(arbre_hors), "transformee_equivalente": P.garder_loi(arbre_dedans),
                                  "ecart_max_des_probabilites": float(np.max(np.abs(M.probas(arbre_hors, Z, G) - M.probas(arbre_dedans, Z, G))))}

# E5 — extraction des propositions : formes de réponse plausibles.
props = json.dumps([{"enonce": "a", "loi_predictive": F0}])
formes = {"bloc_json": "```json\n" + props + "\n```", "json_nu": props, "bloc_sans_etiquette": "```\n" + props + "\n```",
          "bloc_JSON_majuscules": "```JSON\n" + props + "\n```", "phrase_puis_json_nu": "Voici mes lois :\n" + props,
          "deux_blocs_le_second_seul_valable": "```json\n{\"brouillon\": 1}\n```\nFinal :\n```json\n" + props + "\n```",
          "objet_propositions": "```json\n" + json.dumps({"propositions": json.loads(props)}) + "\n```"}
res["E5_extraction"] = {}
for nom, t in formes.items():
    cs, info = P.cartes_d_un_appel(1, "astra", t)
    res["E5_extraction"][nom] = {"cartes": len(cs), "admises": sum(c["etat"] == "admise" for c in cs), "lecture": info["lecture"]}

# E6 — rapatriement : ce que la garde voit et ne voit pas (lois et textes synthétiques, aucun monde).
src = os.path.join(BAC, "e6-source")
os.makedirs(os.path.join(src, "monde-1", "astra"))
loi_compilee = {"type": "par_sous_population", "lois": {str(k): arbre_hors for k in range(3)}}
with open(os.path.join(src, "monde-1", "astra", "corps-relais.json"), "w") as f:
    json.dump({"erreur": "amont HTTP 429", "corps_amont": "Rate limit reached in organization org-EXEMPLE on tokens per min ; "
               "Incorrect API key provided: sk-proj-********EXEM"}, f)
with open(os.path.join(src, "monde-1", "astra", "temoin-isolement.json"), "w") as f:
    json.dump({"loi_vraie": loi_compilee, "graine": 2 ** 64 + 12345, "episodes_developpement": [{"z": [0.0] * 8, "g": 0, "y": 1}]}, f)
with open(os.path.join(src, "secret.bin"), "wb") as f:
    f.write(bytes(32))
try:
    r = AU.rapatrier(src, os.path.join(BAC, "e6-dest"), None)
    res["E6_rapatriement"] = {"refus": False, "copies": [c[0] for c in r["copies"]], "laisses": r["laisses"], "aucun_monde": r["aucun_monde"]}
except P.Refus as e:
    res["E6_rapatriement"] = {"refus": True, "motif": str(e)}
src2 = os.path.join(BAC, "e6b-source")
os.makedirs(src2)
with open(os.path.join(src2, "CARTES.json"), "w") as f:
    json.dump({"spec": {"effets": [], "distracteurs": []}}, f)
try:
    AU.rapatrier(src2, os.path.join(BAC, "e6b-dest"), None)
    res["E6b_devis_sans_empreinte_du_fichier"] = {"refus": False}
except P.Refus as e:
    res["E6b_devis_sans_empreinte_du_fichier"] = {"refus": True}

# E8, E10 — mondes de développement : K1 servie au gardien, taille et pièces des textes servis (booléens et comptes seulement).
mondes = P.charger_mondes_prives(MONDES, SHA_MONDES)
pm_ = P.preparer(mondes)
k1 = {}
for wd in sorted(pm_):
    arch, _ = P.heritage_k1(pm_[wd])
    ep = P.episodes_de_developpement(pm_[wd]["spec"])
    t = P.texte_servi(arch, ep)
    k1[str(wd)] = {"k1_servie_admise_au_gardien": P.garder_loi(arch[0]["loi"]) is None,
                   "k1_plus_grand_coefficient_sous_4": max(abs(x) for l in arch[0]["loi"]["poids"] for x in l) < 4.0,
                   "octets_du_texte": len(t.encode()), "episodes": len(ep),
                   "cles_du_contexte": sorted(json.loads(t[t.find("```json\n") + 8:t.rfind("\n```")])),
                   "traits_non_constants": sum(len({e["z"][j] for e in ep}) > 1 for j in range(8)),
                   "issues_vues": sorted({e["y"] for e in ep}), "sous_populations_vues": sorted({e["g"] for e in ep})}
res["E8_E10_textes_servis_des_mondes_de_developpement"] = k1
res["E10_gabarit_sha256"] = P.gabarit_sha256()

# E11 — Q-1 : valeurs de plafond pour 36 000 jetons chez Argon et Astra, lues par `lire_configuration`.


def conf_q1(plafond, borne, d):
    import shutil
    shutil.copytree(os.path.dirname(CONF), d)
    c = os.path.join(d, "configuration-pilote-mr2-v9.json")
    with open(c, encoding="utf-8") as f:
        k = json.load(f)
    for n in ("argon", "astra"):
        k["proposeurs"][n].update(plafond_session_usd=plafond, borne_sortie_jetons=borne, part_usd=round(4 * plafond, 2))
        k["go"]["pi2"]["parts_usd"][n] = round(4 * plafond, 2)
    k["go"]["pi2"]["montant_usd"] = round(8 * plafond + 3.0, 2)
    with open(c, "w", encoding="utf-8") as f:
        json.dump(k, f)
    try:
        kk, _ = PR.lire_configuration(c)
        return {"admise": True, "pi2_usd": kk["go"]["pi2"]["montant_usd"], "part_usd": kk["proposeurs"]["argon"]["part_usd"],
                "borne_max_payee": PR.borne_de_sortie_max(plafond, 10.0, 50.0, kk["octets_entree_max"])}
    except P.Refus as e:
        return {"admise": False, "motif": str(e)}


res["E11_Q1"] = {f"{p}_USD_{b}_jetons": conf_q1(p, b, os.path.join(BAC, f"e11-{i}")) for i, (p, b) in enumerate(
    ((2.33, 36000), (2.34, 36000), (2.5, 36000), (2.5, 39000), (2.0, 29000), (2.0, 36000)))}
res["E11_pire_cas_par_appel_usd"] = {
    "argon_astra_36000": (52000 + 1024) * 10.0 / 1e6 + 36000 * 50.0 / 1e6,
    "argon_astra_29000": (52000 + 1024) * 10.0 / 1e6 + 29000 * 50.0 / 1e6,
    "fable52_64000": (52000 + 1024) * 8.0 / 1e6 + 64000 * 40.0 / 1e6,
    "opus55_89000": (52000 + 1024) * 4.0 / 1e6 + 89000 * 20.0 / 1e6}

# E12 — le relais réserve le pire cas que la commande déclare : une requête qui déclare 0,000001 USD pour 10⁶ jetons.
import socket  # noqa: E402

s = socket.socket()
s.bind(("127.0.0.1", 0))
port = s.getsockname()[1]
s.close()
conf2 = copy.deepcopy(conf)
conf2["proposeurs"]["argon"]["port"] = port
proc, info = PR.lancer_relais(conf2, "argon", os.path.join(BAC, "journal-relais-e12.jsonl"), "factice:k1_seul", python=sys.executable)
try:
    ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    corps = json.dumps({"modele": "gemini-4-argon", "consigne": "```json\n" + json.dumps(
        {"lois_retenues": [{"loi": F0}], "monde": {"traits": 8}}) + "\n```", "max_tokens": 10 ** 6, "pire_cas_usd": 1e-6}).encode()
    codes = []
    for _ in range(2):
        try:
            with ouvreur.open(urllib.request.Request(f"http://127.0.0.1:{port}/appel", data=corps, method="POST",
                                                     headers={"Content-Type": "application/json"}), timeout=20) as r:
                codes.append(r.status)
        except urllib.error.HTTPError as e:
            codes.append(e.code)
    with ouvreur.open(f"http://127.0.0.1:{port}/relais/etat", timeout=10) as r:
        etat = json.loads(r.read())
    res["E12_relais_pire_cas_declare"] = {"statuts": codes, "champs_de_l_etat": sorted(etat), "regle_usd": etat["regle_usd"],
                                          "plafond_usd": etat["plafond_usd"]}
finally:
    PR.arreter_relais(proc)

# E17 — nombres démesurés dans une loi : refus motivé au gardien, jamais une exception.
res["E17_seuil_entier_demesure"] = P.garder_loi({"type": "si_sinon", "condition": {"indice": 1, "seuil": 10 ** 400}, "si": F0, "sinon": F0})
res["E17_frequence_demesuree"] = P.garder_loi({"type": "transformee", "base": F0, "oscillation": {
    "amplitude": 1.0, "frequence": 1e308, "trait": 0, "issue": 0}})

with open(SORTIE, "x", encoding="utf-8") as f:
    json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    f.write("\n")
print(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
