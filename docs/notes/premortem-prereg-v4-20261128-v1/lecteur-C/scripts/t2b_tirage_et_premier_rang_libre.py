"""T2(b) — « l'empreinte 0065065b… est dans tirage.json » (passation v4, § 4, point 1 : « 64 tâches fraîches après
0065065b… dans tirage.json ») : vrai ou faux ? Et quel est le premier rang libre du tirage ?
Entrées : tirage.json (dépôt), taches-banque.json et bilan-extraction.json (extraits par git show de la branche
origin/banque/dose-reponse-consigne-cachee-v1), corpus.json (dépôt)."""
import hashlib, json, re, sys
from pathlib import Path

tirage_p, banque_p, bilan_p, corpus_p, sortie = map(Path, sys.argv[1:6])
brut = tirage_p.read_bytes()
tir = json.loads(brut)
ordre = tir["resultat"]["ordre"]
rang = {a: i for i, a in enumerate(ordre)}
sans_version = lambda x: re.sub(r"v\d+$", "", x)
banque = json.loads(banque_p.read_text())["resultat"]
bilan = json.loads(bilan_p.read_text())["resultat"]
corpus = json.loads(corpus_p.read_text())["resultat"]

out = {"tirage_sha256": hashlib.sha256(brut).hexdigest(), "banque_sha256": hashlib.sha256(banque_p.read_bytes()).hexdigest(),
       "tirage_cles": {"racine": sorted(tir), "resultat": sorted(tir["resultat"])}, "candidats_ordonnes": len(ordre)}
# (1) l'empreinte de la banque figure-t-elle dans tirage.json, sous quelque forme que ce soit ?
texte = brut.decode("utf-8")
out["chaine_0065065b_dans_tirage_json"] = "0065065b" in texte
out["toute_empreinte_de_64_chiffres_dans_tirage_json"] = sorted(set(re.findall(r"\b[0-9a-f]{64}\b", texte)))
out["tirage_json_contient_des_taches"] = any(k in texte for k in ("questions", "cibles", "tests_publics", "identifiant"))
# (2) rangs
r_corpus = sorted(f["rang_tirage"] for f in corpus["fiches"])
out["banque_initiale"] = {"papiers_examines": len(r_corpus), "rangs": [r_corpus[0], r_corpus[-1]], "taches_gardees": corpus["resume"]["gardes"]}
r_banque = sorted(rang[sans_version(t["identifiant"])] for t in banque["taches"])
out["banque_dose_reponse"] = {"taches": len(r_banque), "rang_min": r_banque[0], "rang_max": r_banque[-1]}
statuts = {k: (rang[sans_version(k)], v["statut"]) for k, v in bilan["statuts"].items()}
r_hors = sorted(rang[sans_version(x)] for x in bilan["entrainement"])
out["examines_par_l_extraction_de_la_banque"] = {
    "papiers_a_statut": len(statuts), "rang_max_examine": max(r for r, _ in statuts.values()),
    "retenus_hors_banque_au_dela_du_64e": {"n": len(r_hors), "rangs": r_hors, "fichier": "taches-hors-banque.json", "sha256": bilan["taches_hors_banque_sha256"]},
    "exclus_apres_extraction": {k: {"rang": rang[sans_version(k)], "motif": m} for k, m in bilan["exclus"].items()},
    "rangs_sans_statut_entre_125_et_le_max": [r for r in range(125, max(r for r, _ in statuts.values()) + 1) if r not in {x for x, _ in statuts.values()}]}
mx = out["examines_par_l_extraction_de_la_banque"]["rang_max_examine"]
n_examines = mx - 125 + 1
n_retenus = len(r_banque) + len(r_hors)
out["premier_rang_apres_la_banque"] = r_banque[-1] + 1
out["premier_rang_jamais_examine"] = mx + 1
out["candidats_restants_a_partir_du_premier_rang_jamais_examine"] = len(ordre) - (mx + 1)
out["taux_de_retenue_observe_rangs_125_a_max"] = {"retenus": n_retenus, "papiers": n_examines, "taux": n_retenus / n_examines}
out["papiers_a_examiner_pour_64_taches_a_ce_taux"] = round(64 / (n_retenus / n_examines), 1)
out["verdict_T2b"] = ("FAUX : tirage.json ne contient ni l'empreinte 0065065b… ni aucune tâche ; il ordonne des papiers candidats. "
                      "0065065b… est l'empreinte de taches-banque.json (autre branche). « Après 0065065b… » ne désigne un rang "
                      "que par la banque : dernier rang de la banque %d ; premier rang après la banque %d ; premier rang jamais "
                      "examiné %d (les rangs %d à %d ont été examinés par l'extraction de la banque : %d tâches retenues hors banque)."
                      % (r_banque[-1], r_banque[-1] + 1, mx + 1, r_banque[-1] + 1, mx, len(r_hors)))
sortie.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print(json.dumps(out, ensure_ascii=False, indent=1))
