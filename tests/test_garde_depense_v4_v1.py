"""Gardes de dépense et surveillance de la relance v4 de R1 (`runs_nuit.garde_depense_v4_v1`, points I2 et I3 de la
contre-lecture R2) : cas sain et artefact pour chaque règle (R5), sans réseau, sans instance."""
import pytest

from controle_ia.gardes import GardeArret
from controle_ia.runs_nuit import garde_depense_v4_v1 as gd

T0 = "2026-11-05T10:00:00Z"


def _arme(**k):
    h = gd.heure_destruction(T0, 1.40, 0.1, 6.0)
    v = {"identifiant": "29999999", "T0": T0, "prix_horaire": 1.40, "disque": 0.1, "deja_imputees": 6.0,
         "heure_destruction": h["heure_destruction"]}
    v.update(k)
    return v


def test_destruction_par_identifiant_seulement():
    assert gd.commande_destruction(29999999) == ["vastai", "destroy", "instance", "29999999"]
    assert gd.commande_destruction("29999999") == ["vastai", "destroy", "instance", "29999999"]
    for faux in (None, "", "r1-v4-temoin", "2999*", "0", "-3", "12 13", True, "1e5"):
        with pytest.raises(GardeArret):
            gd.commande_destruction(faux)


def test_heure_de_destruction_et_refus_sans_marge():
    h = gd.heure_destruction(T0, 1.40, 0.0, 0.0)
    assert h["H_min"] == pytest.approx(57 / 1.40 * 60 - 15, abs=0.1) and h["heure_destruction"] == "2026-11-07T02:27:51Z"
    h2 = gd.heure_destruction(T0, 1.40, 0.1, 6.0)          # dépenses imputées (session 1) et disque
    assert h2["H_min"] == pytest.approx((57 - 6.1) / 1.40 * 60 - 15, abs=0.1)
    with pytest.raises(GardeArret, match="plus de marge"):
        gd.heure_destruction(T0, 1.40, 0.0, 56.9)
    with pytest.raises(GardeArret):
        gd.heure_destruction(T0, 0.0, 0.0, 0.0)
    with pytest.raises(GardeArret, match="format"):
        gd.heure_destruction("2026-11-05 10:00", 1.40, 0.0, 0.0)


def test_decision_horaire_seuils_45_et_57():
    ident = [29999999]
    assert gd.decision_horaire(_arme(), "2026-11-05T13:00:00Z", ident)["action"] == "rien"
    d = gd.decision_horaire(_arme(deja_imputees=40.0), "2026-11-05T13:00:00Z", ident)
    assert d["action"] == "alerte" and d["alerte"] and d["commande"] is None
    d = gd.decision_horaire(_arme(deja_imputees=52.0), "2026-11-05T13:00:00Z", ident)
    assert d["action"] == "detruire" and d["commande"] == ["vastai", "destroy", "instance", "29999999"]
    # fin de l'amorce lue au journal : destruction (l'instance reste facturée après l'amorce)
    d = gd.decision_horaire(_arme(), "2026-11-05T13:00:00Z", ident, ["AMORCE 2026-11-05T12:59:00Z : fin, code 0"])
    assert d["action"] == "detruire" and d["motif"].startswith("fin de l'amorce")
    # identifiant absent du listing : rien n'est détruit
    assert gd.decision_horaire(_arme(deja_imputees=50.0), "2026-11-05T13:00:00Z", [])["action"] == "absente"
    # prompt sans identifiant, sans T0, sans prix : échec visible, alerte, rien n'est détruit
    for k in ("identifiant", "T0", "prix_horaire"):
        p = _arme()
        p.pop(k)
        d = gd.decision_horaire(p, "2026-11-05T13:00:00Z", ident)
        assert d["action"] == "echec_visible" and d["alerte"] and d["commande"] is None


def test_epreuves_du_complement_aux_seuils_v4():
    e = {x["epreuve"][:2]: x for x in gd.epreuves()}
    assert e["1 "]["action"] == "absente" and e["1 "]["commande"] is None
    assert e["2 "]["action"] == "echec_visible" and e["2 "]["alerte"]
    assert e["3 "]["action"] == "rien" and e["3 "]["depense"] == pytest.approx(1.79, abs=0.01)
    assert e["4a"]["action"] == "absente" and e["4a"]["commande"] is None
    assert e["4b"]["action"] == "alerte" and e["4c"]["action"] == "detruire"
    assert e["4d"]["action"] == "echec_visible"


JOURNAL = """AMORCE 2026-11-05T10:01:00Z : relance v4 de R1, session reparation, commit abc, plafond de l'amorce 2200 min
2026-11-05T10:01:05Z début : relance v4 de R1, session reparation, MODE=reel COMMIT=abc BRANCHE=b DELAI_ETAPE_MIN=2100 TEMOIN_RUN=x
2026-11-05T10:02:00Z témoin lu au commit : diag/x/r.json (lecture : exact)
2026-11-05T10:40:00Z tests : 358 passed in 1200.5s (0:20:00)
2026-11-05T10:41:00Z étape reparation : run r, délai externe 2100 min (garde contre une boucle folle)
PROGRES 2026-11-05T10:45:00Z etape=reparation voie=lot_fidele cibles=89 lots=28
PROGRES 2026-11-05T11:45:00Z etape=reparation episodes=10/89 retrouves=10
PROGRES 2026-11-05T12:45:00Z etape=reparation episodes=20/89 retrouves=19
PROGRES 2026-11-05T12:50:00Z etape=temoin lot=2 lecture=exact pas=10 accord=1.0 captures=8/8
une ligne quelconque qui dit un résultat
"""


def test_lecture_aveugle_du_journal():
    f = gd.filtrer_journal(JOURNAL.splitlines())
    texte = "\n".join(f)
    for interdit in ("retrouves", "lecture", "accord", "captures", "voie", "résultat", "exact"):
        assert interdit not in texte, interdit
    assert "PROGRES 2026-11-05T11:45:00Z etape=reparation episodes=10/89" in f
    assert "2026-11-05T10:01:05Z DELAI_ETAPE_MIN=2100" in f and "2026-11-05T10:40:00Z tests : 358 passed" in f
    p = gd.projection_fin(f, "2026-11-05T13:00:00Z")
    # V0 10:45, V20 12:45 : 2 h pour 20 → 69 restants ≈ 6,9 h ; + 75 min
    assert p["k"] == 20 and p["F"] == "2026-11-05T21:09:00Z"
    assert gd.projection_fin(f[:4], "2026-11-05T13:00:00Z")["F"] is None
    fin = f + ["PROGRES 2026-11-05T20:00:00Z etape=reparation episodes=89/89"]
    assert gd.projection_fin(fin, "2026-11-05T20:00:00Z")["F"] == "2026-11-05T21:15:00Z"
    # demande d'extension si F dépasse l'heure de (ii)
    d = gd.decision_horaire(_arme(heure_destruction="2026-11-05T20:00:00Z"), "2026-11-05T13:00:00Z", [29999999], f)
    assert d["extension"] and d["alerte"]


def test_surveillance_valeurs_v4():
    f = [x for x in gd.filtrer_journal(JOURNAL.splitlines()) if "etape=temoin" not in x]
    assert gd.verifier_surveillance(f, "reparation")["verdict"] == "conforme"
    assert gd.verifier_surveillance(f[:2], "reparation")["verdict"] == "en_cours"
    # artefacts : une autre valeur lue → détruire
    for vieux, neuf in (("plafond de l'amorce 2200", "plafond de l'amorce 720"), ("DELAI_ETAPE_MIN=2100", "DELAI_ETAPE_MIN=600"),
                        ("tests : 358 passed", "tests : 329 passed"), ("cibles=89", "cibles=88"), ("lots=28", "lots=27")):
        j = JOURNAL.replace(vieux, neuf)
        assert j != JOURNAL
        g = [x for x in gd.filtrer_journal(j.splitlines()) if "etape=temoin" not in x]
        assert gd.verifier_surveillance(g, "reparation")["verdict"] == "detruire", neuf
    # valeurs de la session 2 lues en session 1 : détruire ; ligne du témoin en session 2 : détruire
    assert gd.verifier_surveillance(f, "temoin")["verdict"] == "detruire"
    assert gd.verifier_surveillance(gd.filtrer_journal(JOURNAL.splitlines()), "reparation")["verdict"] == "detruire"
    s1 = ["AMORCE 2026-11-05T10:01:00Z : relance v4 de R1, session temoin, commit abc, plafond de l'amorce 180 min",
          "2026-11-05T10:01:05Z DELAI_ETAPE_MIN=120", "2026-11-05T10:40:00Z tests : 358 passed",
          "PROGRES 2026-11-05T10:45:00Z etape=temoin lot=2"]
    assert gd.verifier_surveillance(s1, "temoin")["verdict"] == "conforme"


def test_prompts_armement_et_relecture():
    non_arme = gd.prompt_tache("destruction", "reparation")
    lu = gd.lire_prompt(non_arme)
    assert "identifiant" not in lu and gd.decision_destruction(lu, [29999999])["action"] == "echec_visible"
    h = gd.heure_destruction(T0, 1.40, 0.1, 6.0)
    v = _arme()
    arme = gd.prompt_tache("destruction", "reparation", v)
    lu = gd.lire_prompt(arme)
    gd.exiger_armement(lu, 29999999, T0, h, h["heure_destruction"])
    assert gd.decision_destruction(lu, [29999999])["commande"] == ["vastai", "destroy", "instance", "29999999"]
    with pytest.raises(GardeArret, match="identifiant relu"):
        gd.exiger_armement(lu, 29999998, T0, h, h["heure_destruction"])
    with pytest.raises(GardeArret, match="T0 relu"):
        gd.exiger_armement(lu, 29999999, "2026-11-05T10:00:01Z", h, h["heure_destruction"])
    with pytest.raises(GardeArret, match="départ"):
        gd.exiger_armement(lu, 29999999, T0, h, "2026-11-07T00:00:00Z")
    with pytest.raises(GardeArret, match="essai"):
        gd.exiger_armement(gd.lire_prompt(gd.prompt_tache("destruction", "reparation", v, essai=True)), 29999999, T0, h,
                           h["heure_destruction"])
    with pytest.raises(GardeArret, match="deux fois"):
        gd.lire_prompt(arme + "identifiant = 1\n")
    with pytest.raises(GardeArret):
        gd.prompt_tache("autre", "reparation")
