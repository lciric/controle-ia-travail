"""Essai du contre-lecteur (modèle S), v3 : quatre natures. Plant à moi : Opus, premier rendu, sur les bons dont le fragment
« voisins » est piège « reprise assumée » ET sur les mauvais voisin_nomme ; Argon, premier rendu, sur les bons conformes non
citants seulement. Recalcul par boucle simple. (b) : une banque dont fragments_sha256 est celui d'un AUTRE fichier valide
est refusée même si le journal est cohérent avec le fichier passé."""
import json

import numpy as np
import pytest

import essais_etalonnage_lecture_ligne_3_v3 as E

ET = E.ET
NAT = {"VN": "conforme_non_citant", "VC": "conforme_citant", "VF": "fautif", "VP": "conforme_piege_reprise_assumee"}


def plante(t, fid, e):
    if e["rendu"] != 1:
        return False
    if e["juge"] == "juge-opus":
        return (t["classe"] == "bon" and fid == "VP") or (t["classe"] == "mauvais" and t["item"] == "voisin_nomme")
    return t["classe"] == "bon" and fid == "VN"


def test_quatre_natures_plant_a_moi(tmp_path):
    m = E.fabriquer(tmp_path, erreurs=np.zeros((200, 5), dtype=bool), plante=plante)
    E.etalonner(m)
    c = json.loads(m["etalonnage"].read_text(encoding="utf-8"))[ET.CLE_RESERVES]["par_juge"]
    for j in ET.JUGES:
        att = {}
        for t in m["temoins"]:
            if t["moitie"] != "etalonnage":
                continue
            fid = m["voisins"][t["identifiant_interne"]]
            tombe = (t["classe"] == "mauvais" and t["item"] == "reserves_tenues") or plante(t, fid, {"juge": j, "rendu": 1})
            a = att.setdefault(NAT[fid], [0, 0])
            a[0] += int(tombe)
            a[1] += 1
        assert {k: [v["compte"], v["sur"]] for k, v in c[j]["par_voisins"].items()} == att
        assert set(att) == set(ET.NATURES_VOISINS) == {"conforme_non_citant", "conforme_citant", "fautif",
                                                        "conforme_piege_reprise_assumee"}
    assert c["juge-opus"]["par_voisins"]["conforme_piege_reprise_assumee"]["compte"] > 0
    assert c["juge-argon"]["par_voisins"]["conforme_piege_reprise_assumee"]["compte"] == 0
    assert c["juge-argon"]["par_voisins"]["conforme_non_citant"]["compte"] > 0


def test_banque_d_un_autre_fichier_de_fragments_refusee_meme_si_journal_coherent(tmp_path):
    m = E.fabriquer(tmp_path)
    (tmp_path / "autre").mkdir()
    fr = json.loads(m["fragments"].read_text(encoding="utf-8"))
    fr["version"] = "autre-valide"
    f2 = tmp_path / "autre" / "fragments.json"
    h2 = ET.ecrire_scelle(f2, fr)
    assert h2 != m["fragments_sha"]
    j = json.loads(m["journal"].read_text(encoding="utf-8"))
    j["fragments_sha256"] = h2
    j2 = tmp_path / "autre" / "journal-construction.json"
    hj2 = ET.ecrire_scelle(j2, j)
    with pytest.raises(ET.Refus, match="fragments_sha256 est absent ou différent"):
        E.executer_etalonnage(m, m["depot"] / "verdicts-moitie-etalonnage-execution-1.json",
                              E.sha_compagnon(m["depot"] / "verdicts-moitie-etalonnage-execution-1.json"),
                              m["racine"] / "d", journal=j2, journal_sha=hj2, fragments=f2, fragments_sha=h2)
    assert not (m["racine"] / "d").exists()
