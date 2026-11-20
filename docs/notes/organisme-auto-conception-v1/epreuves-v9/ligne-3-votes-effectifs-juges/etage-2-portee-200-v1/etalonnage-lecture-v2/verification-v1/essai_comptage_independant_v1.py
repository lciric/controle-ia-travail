"""Essai du contre-lecteur (modèle S) : le comptage « cartes tombées sur reserves_tenues » de la v2 retrouve-t-il un plant
que j'ai choisi moi-même, autre que celui du développeur, avec un verdict absent ? Mon recalcul est fait ici, par boucle simple,
depuis la banque factice et la table des fragments, sans les fonctions du programme."""
import json

import numpy as np

import essais_etalonnage_lecture_ligne_3_v2 as E

ET = E.ET


def plante(t, fid, e):
    # Argon, premier rendu : bons dont le fragment « voisins » est conforme non citant ET citants de la banque ;
    # Opus, premier rendu : mauvais dont le fragment « voisins » est fautif (item voisin_nomme) de niveau discret.
    if e["rendu"] != 1:
        return False
    if e["juge"] == "juge-argon":
        return t["classe"] == "bon" and t["citation"] and fid == "VN"
    return t["classe"] == "mauvais" and t["item"] == "voisin_nomme" and t["niveau"] == "discret"


def test_plant_propre_et_absent(tmp_path):
    plan = E.plan_factice(E.banque_factice(200))
    cal_a = [p for p in plan if p["bloc"] == "A" and p["moitie"] == "etalonnage" and p["juge"] == "juge-argon"]
    absent_id = cal_a[0]["id"]
    m = E.fabriquer(tmp_path, erreurs=np.zeros((200, 5), dtype=bool), plante=plante, absents={absent_id})
    E.etalonner(m)
    piece = json.loads(m["etalonnage"].read_text(encoding="utf-8"))
    c = piece[ET.CLE_RESERVES]["par_juge"]
    absent_t = cal_a[0]["temoin"]
    NAT = {"VN": "conforme_non_citant", "VC": "conforme_citant", "VF": "fautif"}
    for j in ET.JUGES:
        att = {}
        exclus = 0
        for t in m["temoins"]:
            if t["moitie"] != "etalonnage":
                continue
            if j == "juge-argon" and t["identifiant_interne"] == absent_t:
                exclus += 1
                continue
            fid = m["voisins"][t["identifiant_interne"]]
            tombe = (t["classe"] == "mauvais" and t["item"] == "reserves_tenues") or plante(t, fid, {"juge": j, "rendu": 1})
            k = (t["classe"], "citant" if t["citation"] else "non_citant", t["item"] or "aucun (bon)", NAT[fid])
            a = att.setdefault(k, [0, 0])
            a[0] += int(tombe)
            a[1] += 1
        lu = {(s["classe"], s["citation"], s["item_plante"], s["voisins"]): [s["compte"], s["sur"]] for s in c[j]["strates"]}
        assert lu == att
        assert c[j]["verdicts_absents_exclus"] == exclus
        assert sum(x["sur"] for x in c[j]["par_classe"].values()) == 100 - exclus
        # marges recomposées
        tot = sum(v[0] for v in att.values())
        assert sum(x["compte"] for x in c[j]["par_classe"].values()) == tot
        assert sum(x["compte"] for x in c[j]["par_voisins"].values()) == tot
        assert sum(x["compte"] for x in c[j]["par_citation"].values()) == tot
        assert sum(x["compte"] for x in c[j]["par_item_plante"].values()) == tot
    assert c["juge-argon"]["verdicts_absents_exclus"] == 1 and c["juge-opus"]["verdicts_absents_exclus"] == 0
    assert sum(x["compte"] for x in c["juge-argon"]["par_classe"].values()) > 0
