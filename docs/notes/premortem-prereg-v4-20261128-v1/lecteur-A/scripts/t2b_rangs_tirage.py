"""T2(b) — l'empreinte 0065065b... est-elle dans tirage.json ? Rangs de la banque de dose-reponse dans l'ordre du tirage,
rangs examines au-dela, premier rang libre, effectif residuel. Ne lit que des identifiants et des cles de structure."""
import json, re, sys, hashlib
depot, D = sys.argv[1], sys.argv[2]
p_tir = depot + "/diag/20261006-134235-t05-corpus/tirage.json"
brut = open(p_tir, encoding="utf-8").read()
tir = json.loads(brut)
ordre = tir["resultat"]["ordre"]
rang = {x: k for k, x in enumerate(ordre)}
sortie = {"tirage_sha256": hashlib.sha256(brut.encode("utf-8")).hexdigest(), "candidats_ordonnes": len(ordre),
          "cles_resultat": sorted(tir["resultat"].keys()),
          "0065065b_dans_tirage_json": "0065065b" in brut,
          "76cdeace_dans_tirage_json": "76cdeace" in brut,
          "empreintes_64_hex_dans_tirage_json": sorted(set(re.findall(r"\b[0-9a-f]{64}\b", brut)))}
def base(i):  # « 2506.03670v1 » -> « 2506.03670 »
    return re.sub(r"v\d+$", "", i)
def ids(obj):
    r = obj["resultat"]
    out = {}
    for cle, v in r.items():
        if isinstance(v, list):
            out[cle] = [(t.get("identifiant") or t.get("id") or t.get("papier") or t.get("arxiv_id")) if isinstance(t, dict) else t for t in v]
    return out, {cle: (sorted(v[0].keys()) if isinstance(v, list) and v and isinstance(v[0], dict) else None) for cle, v in r.items()}
banque = json.load(open(D + "/taches-banque.json"))
i_b, cles_b = ids(banque)
sortie["banque_cles"] = cles_b
tb = [base(x) for x in i_b["taches"]]
rb = sorted(rang[x] for x in tb)
sortie["banque"] = {"taches": len(tb), "rang_min": rb[0], "rang_max": rb[-1], "hors_tirage": [x for x in tb if x not in rang]}
sortie["banque_remplacements"] = banque["resultat"]["remplacements"] if len(json.dumps(banque["resultat"]["remplacements"])) < 600 else "long"
hors = json.load(open(D + "/taches-hors-banque.json"))
sortie["hors_banque_cles_resultat"] = {k: (type(v).__name__, len(v) if hasattr(v, "__len__") else None) for k, v in hors["resultat"].items()} if isinstance(hors.get("resultat"), dict) else str(type(hors.get("resultat")))
try:
    i_h, cles_h = ids(hors)
    sortie["hors_banque_cles"] = cles_h
    th = []
    for cle, v in i_h.items():
        th += [base(x) for x in v if isinstance(x, str)]
    rh = sorted(rang[x] for x in th if x in rang)
    sortie["hors_banque"] = {"identifiants": len(th), "rangs": rh}
except Exception as e:  # structure autre : on le dit
    sortie["hors_banque_erreur"] = repr(e)
    rh = []
# banque initiale : fiches de corpus.json = rangs 0 a 124 (texte scelle de T0.6, plan, point 1)
corpus = json.load(open(depot + "/diag/20261006-134235-t05-corpus/corpus.json"))
rc = corpus.get("resultat", corpus)
sortie["corpus_cles"] = sorted(rc.keys()) if isinstance(rc, dict) else type(rc).__name__
sortie["premier_rang_apres_le_64e_retenu"] = rb[-1] + 1
sortie["plus_haut_rang_examine"] = max(rb + rh)
sortie["premier_rang_jamais_examine"] = max(rb + rh) + 1
sortie["candidats_restants_apres_le_64e_retenu"] = len(ordre) - (rb[-1] + 1)
sortie["candidats_jamais_examines"] = len(ordre) - (max(rb + rh) + 1)
sortie["rangs_examines_pour_64_retenus"] = rb[-1] + 1 - 125
sortie["taux_de_retenue_banque_dose_reponse"] = 64 / (rb[-1] + 1 - 125)
print(json.dumps(sortie, ensure_ascii=False, indent=1))
