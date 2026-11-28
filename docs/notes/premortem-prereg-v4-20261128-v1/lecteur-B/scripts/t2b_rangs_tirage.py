"""Témoin T2 (b) : l'empreinte 0065065b… est-elle « dans tirage.json » ? Rangs consommés et premier rang libre.
Entrées : tirage.json (dépôt), taches-banque.json, corpus de sélection et bilan d'extraction de la banque de la
dose-réponse (branche origin/banque/dose-reponse-consigne-cachee-v1, extraits par git show)."""
import hashlib, json, re, sys
from pathlib import Path
S = Path(sys.argv[1])
tir_p = Path("/home/user/controle-ia-travail/diag/20261006-134235-t05-corpus/tirage.json")
brut = tir_p.read_bytes(); tir = json.loads(brut)
ordre = tir["resultat"]["ordre"]; rang = {a: i for i, a in enumerate(ordre)}
sans_v = lambda i: re.sub(r"v\d+$", "", i)
bq_b = (S / "taches-banque.json").read_bytes(); bq = json.loads(bq_b)["resultat"]
E = "0065065b8958968235f13c48d4e423708fd5aaebb64f8eed6ec553e3c56459e4"
corpus0 = json.loads(Path("/home/user/controle-ia-travail/diag/20261006-134235-t05-corpus/corpus.json").read_text())["resultat"]
sel = json.loads((S / "corpus-selection-banque-dose-reponse.json").read_text())["resultat"]
bil = json.loads((S / "bilan-extraction-banque.json").read_text())["resultat"]
rb = sorted(rang[sans_v(t["identifiant"])] for t in bq["taches"])
rh = sorted(rang[sans_v(i)] for i in bil["entrainement"])
rs = sorted(f["rang_tirage"] for f in sel["fiches"])
sortie = {
 "tirage_sha256": hashlib.sha256(brut).hexdigest(),
 "cles_de_tirage_json": {"racine": sorted(tir), "resultat": sorted(tir["resultat"])},
 "identifiants_dans_ordre": len(ordre),
 "occurrences_de_0065065b_dans_tirage_json": brut.count(b"0065065b"),
 "chaines_de_64_hex_dans_tirage_json": sorted(set(re.findall(rb"\b[0-9a-f]{64}\b", brut).__iter__()).__len__() if False else [x.decode() for x in set(re.findall(rb"\b[0-9a-f]{64}\b", brut))]),
 "0065065b_est_l_empreinte_de": "taches-banque.json (banque de la dose-réponse)" if hashlib.sha256(bq_b).hexdigest() == E else "?",
 "banque_initiale_T0.5_rangs_examines_indice_0": [min(f["rang_tirage"] for f in corpus0["fiches"]), max(f["rang_tirage"] for f in corpus0["fiches"])],
 "banque_dose_reponse": {"taches": len(rb), "rangs_indice_0": [rb[0], rb[-1]], "rangs_indice_1": [rb[0] + 1, rb[-1] + 1]},
 "selection_de_la_banque_dose_reponse": {"examines": len(rs), "rangs_examines_indice_0": [rs[0], rs[-1]], "resume": {k: sel["resume"][k] for k in ("premier_rang", "dernier_rang", "examines", "gardes", "exclus")}},
 "papiers_retenus_et_extraits_hors_banque": {"nombre": len(rh), "rangs_indice_0": rh},
 "premier_rang_apres_la_banque": {"indice_0": rb[-1] + 1, "indice_1": rb[-1] + 2, "restants": len(ordre) - (rb[-1] + 1)},
 "premier_rang_jamais_examine": {"indice_0": rs[-1] + 1, "indice_1": rs[-1] + 2, "restants": len(ordre) - (rs[-1] + 1)},
 "rendement_observe_taches_retenues_par_papier_examine": {"T0.5": [96, 125], "dose_reponse_selection": [sel["resume"]["gardes"], sel["resume"]["examines"]], "dose_reponse_apres_extraction": [len(rb) + len(rh), len(rs)]},
}
print(json.dumps(sortie, indent=1, ensure_ascii=False))
