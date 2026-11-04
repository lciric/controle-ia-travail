"""Garde de chaîne de la table v4 (`runs_nuit.chaine_table_v4_v1`, point I1 de la contre-lecture R2), sur processeur,
sans téléchargement : P3 jouet, témoin et réparation jouets de `resolution_graine_lot_v3`, table v4 écrite et scellée.

Cas sains (R5) : chaîne conforme et recalcul de réception égal à l'octet (4 retrouvées) ; chaîne conforme avec une
cible non retrouvée (entrée `non_resolu` attendue). Artefacts, chacun arrêté : **une retrouvée rétrogradée en
`non_resolu`** (table par ailleurs cohérente et que le chargeur du rejeu v4 accepte : le trou que ferme la garde) ;
`resultat_reparation_sha256` faux ; entrée de la table v3 retirée ; entrée en trop hors des cibles ; identifiants d'une entrée changés ; entrée qui ne
cite pas le sceau ; réparation arrêtée (`arret.json`) ; autre configuration ; table resérialisée (même contenu, autres
octets, rescellée) : chaîne conforme mais réception refusée à l'octet."""
import json
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.manifeste import creer_manifeste, ecrire_resultat
from controle_ia.runs_nuit import chaine_table_v4_v1 as ch
from controle_ia.runs_nuit import resolution_graine_lot_v2 as rv2
from controle_ia.runs_nuit import resolution_graine_lot_v3 as rv
from controle_ia.scellement import sceller, verifier

from test_premier_test_ia_run import entropie_fixe  # noqa: F401  (fixture réutilisée)
from test_resolution_graine_lot_v1 import _preparer
from test_resolution_graine_lot_v3 import _config_v4, _table_v3_jouet
from test_runs_nuit_v1 import source  # noqa: F401  (fixture réutilisée)


def _ecrire_table(table: dict, chemin: Path) -> Path:
    chemin.write_bytes(ch.octets_de_table(table))
    sceller(chemin)
    return chemin


def test_chaine_table_v4_sains_et_artefacts(source, tmp_path):
    from conftest import committer

    depot, f, c, tp, pieces0, fmt_j, cl, connus, autres = _preparer(source, tmp_path)
    t3 = _table_v3_jouet(depot, tmp_path, tmp_path / "table0.json")
    committer(depot)
    conf = _config_v4(depot, f, c, tp, t3)
    r_t = rv.executer(conf, depot, "20261104-130000-v4-temoin-jouet", None, rv.ETAPE_TEMOIN,
                      autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    ch_t = depot / "diag" / "20261104-130000-v4-temoin-jouet" / "resolution-graine-lot-v3-temoin.json"
    assert r_t["lecture"] == rv.LECTURE_EXACT
    rv.executer(conf, depot, "20261104-130100-v4-reparation-jouet", None, rv.ETAPE_REPARATION, str(ch_t),
                autoriser_depot_sale=True, entropie_essai=3)
    committer(depot)
    ch_r = depot / "diag" / "20261104-130100-v4-reparation-jouet" / "resolution-graine-lot-v3-reparation.json"
    table = rv.construire_table_v4(conf, depot, None, str(ch_r), fmt=fmt_j)
    sortie = tmp_path / "R1-table-tokenisation-v4-jouet.json"
    sha = rv.ecrire_table_v4(table, sortie)
    assert sortie.read_bytes() == ch.octets_de_table(table) and verifier(sortie) == sha
    # ---- cas sain : chaîne conforme, recalcul de réception égal à l'octet
    res = ch.exiger_chaine(depot, sortie, ch_r, conf)
    assert res["retrouvees"] == 4 and res["non_retrouvees"] == 0 and res["table_sha256"] == sha
    assert res["resultat_reparation_sha256"] == verifier(ch_r) and res["entrees_v3"] == len(table["episodes"]) - 4
    assert ch.recalculer_a_la_reception(conf, depot, None, ch_r, sortie, fmt=fmt_j)["recalcul_egal_a_l_octet"]
    # ---- artefact central : une retrouvée rétrogradée en non_resolu, table cohérente par ailleurs
    e0 = autres[0]
    faux = json.loads(sortie.read_text(encoding="utf-8"))
    i0 = next(i for i, x in enumerate(faux["episodes"]) if x["episode"] == e0)
    faux["episodes"][i0] = rv.entree_non_resolue(e0, faux["episodes"][i0]["trajectoire_p3"], "rétrogradée")
    faux["non_resolus_v4"] = [e0]
    faux["comptes"]["retrouvees_v4"] -= 1
    faux["comptes"]["identifiants"] -= 1
    faux["comptes"]["non_resolu"] = faux["comptes"].get("non_resolu", 0) + 1
    p = _ecrire_table(faux, tmp_path / "table-retrogradee.json")
    assert rv2.charger_table_v4(p, None)["version"] == 4           # le chargeur du rejeu v4 l'accepte
    with pytest.raises(GardeArret, match="identifiants » ≠ retrouvées"):
        ch.exiger_chaine(depot, p, ch_r, conf)
    # ---- resultat_reparation_sha256 faux
    t = json.loads(sortie.read_text(encoding="utf-8"))
    t["resultat_reparation_sha256"] = "0" * 64
    with pytest.raises(GardeArret, match="resultat_reparation_sha256"):
        ch.exiger_chaine(depot, _ecrire_table(t, tmp_path / "table-sha-faux.json"), ch_r, conf)
    # ---- entrée de la table v3 retirée
    t = json.loads(sortie.read_text(encoding="utf-8"))
    v3 = [x for x in t["episodes"] if x["episode"] not in set(autres)]
    if v3:
        t["episodes"].remove(v3[0])
        with pytest.raises(GardeArret, match="table v3 citée"):
            ch.exiger_chaine(depot, _ecrire_table(t, tmp_path / "table-v3-retiree.json"), ch_r, conf)
    # ---- entrée en trop hors des cibles (la table v3 jouet est vide : l'entrée retirée ci-dessus ne peut s'y éprouver)
    t = json.loads(sortie.read_text(encoding="utf-8"))
    intrus = json.loads(json.dumps(next(x for x in t["episodes"] if x["episode"] == e0)))
    intrus["episode"] = "intrus/0000.00000v1/e0"
    t["episodes"].append(intrus)
    p_i = _ecrire_table(t, tmp_path / "table-intrus.json")
    assert rv2.charger_table_v4(p_i, None)["version"] == 4
    with pytest.raises(GardeArret, match="table v3 citée"):
        ch.exiger_chaine(depot, p_i, ch_r, conf)
    # ---- identifiants d'une entrée changés (sans revérification par P3 ici : la chaîne compare au résultat)
    t = json.loads(sortie.read_text(encoding="utf-8"))
    ent = next(x for x in t["episodes"] if x["episode"] == e0)
    ent["actions"][0]["p3"] = ent["actions"][0]["p3"][::-1] if len(set(ent["actions"][0]["p3"])) > 1 \
        else ent["actions"][0]["p3"] + [4]
    with pytest.raises(GardeArret, match="identifiants de l'entrée"):
        ch.exiger_chaine(depot, _ecrire_table(t, tmp_path / "table-ids-faux.json"), ch_r, conf)
    # ---- entrée qui ne cite pas le sceau du résultat
    t = json.loads(sortie.read_text(encoding="utf-8"))
    next(x for x in t["episodes"] if x["episode"] == e0)["resolution_graine"]["resultat_sha256"] = "1" * 64
    with pytest.raises(GardeArret, match="ne cite pas le sceau"):
        ch.exiger_chaine(depot, _ecrire_table(t, tmp_path / "table-sceau-faux.json"), ch_r, conf)
    # ---- autre configuration
    with pytest.raises(GardeArret, match="autre configuration"):
        ch.exiger_chaine(depot, sortie, ch_r, {**conf, "seuil_lecture_lot": 0.5})
    # ---- table resérialisée (autres octets, même contenu, rescellée) : chaîne conforme, réception refusée
    p2 = tmp_path / "table-reserialisee.json"
    p2.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sceller(p2)
    assert ch.exiger_chaine(depot, p2, ch_r, conf)["retrouvees"] == 4
    with pytest.raises(GardeArret, match="à l'octet"):
        ch.recalculer_a_la_reception(conf, depot, None, ch_r, p2, fmt=fmt_j)
    # ---- cas sain avec une non retrouvée : résultat réécrit sous un manifeste neuf (même configuration)
    corps = json.loads(ch_r.read_text(encoding="utf-8"))["resultat"]
    for x in corps["episodes"]:
        if x["episode"] == e0:
            x.update(statut="non_resolu", ids=None, empreinte=None, empreinte_retrouvee=False, cause="jouet")
    m, _ = creer_manifeste(depot, "20261104-130200-v4-reparation-jouet", conf, ["aucun-tirage-propre"], entropie=3,
                           autoriser_depot_sale=True, commande=f"{rv.COMMANDE} --etape {rv.ETAPE_REPARATION}")
    ch_r2 = ecrire_resultat(depot, m, "resolution-graine-lot-v3-reparation", corps)
    committer(depot)
    table2 = rv.construire_table_v4(conf, depot, None, str(ch_r2), fmt=fmt_j)
    s2 = tmp_path / "table-une-non-retrouvee.json"
    rv.ecrire_table_v4(table2, s2)
    res2 = ch.exiger_chaine(depot, s2, ch_r2, conf)
    assert res2["retrouvees"] == 3 and res2["non_retrouvees"] == 1
    # la table de la première réparation ne passe pas la chaîne du second résultat (sceau différent)
    with pytest.raises(GardeArret, match="resultat_reparation_sha256"):
        ch.exiger_chaine(depot, sortie, ch_r2, conf)
    # ---- réparation arrêtée : arret.json dans son dossier
    (depot / "diag" / "20261104-130200-v4-reparation-jouet" / "arret.json").write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="arret.json"):
        ch.exiger_chaine(depot, s2, ch_r2, conf)
