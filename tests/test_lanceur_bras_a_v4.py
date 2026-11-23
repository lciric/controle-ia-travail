"""Essais du lanceur de la course du bras A, version 4 (`lanceur_bras_a_v4.py`) : les essais de la version 3, portés
sur la version 4, et ceux des corrections de la contre-lecture (M-2 ; m-1 à m-6), chacun sur un cas sain et sur un
artefact (R5). Processeur seul ; aucune instance, aucun réseau, aucune clé. Entropie fictive, déclarée telle, sauf pour
la ligne 1 : une configuration d'essai à entropie fictive n'a jamais de constat de départ (M-2), la ligne simulée est
donc jouée sous une configuration déclarée réelle, sur un texte fictif, dans un dossier temporaire."""
import ast
import json
import shutil
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import fabrication_v3 as fab
from controle_ia.organismes_discrets import instrument_appariement_v4 as iv
from controle_ia.organismes_discrets import lanceur_bras_a_v4 as la
from controle_ia.scellement import sceller

DEPOT = Path(__file__).resolve().parents[1]
ENTROPIE_FICTIVE = 271828182845904523536028747135266249775   # fictive, déclarée telle (`entropie_fictive`)
REF = json.loads((DEPOT / la.CHEMIN_CONFIGURATION_DE_REFERENCE).read_text(encoding="utf-8"))
REGLAGES = dict(iv.OPTIONS_RETENUES)


def _sha(p: Path) -> str:
    import hashlib
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _texte_fictif(entropie: int, en_plus: str = "") -> str:
    corps = {"Hypothèse": "h", "Prédiction chiffrée et signe attendu": "p", "Métrique": "m", "Seuil": "s",
             "Plan d'analyse": f"entropie racine : {entropie}", "Critères de lecture gelés": "c", "Liste d'arrêt": "l",
             "Contre-lecture": "brouillon " + "a" * 64 + " ; rapport " + "b" * 64}
    return "# Texte fictif des essais du lanceur v4\n\n" + "".join(f"## {k}\n\n{v}\n\n" for k, v in corps.items()) + en_plus


def _copier(racine: Path, relatif: str) -> None:
    for suffixe in ("", ".sha256"):
        (racine / relatif).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(DEPOT / (relatif + suffixe), racine / (relatif + suffixe))


@pytest.fixture
def racine(tmp_path):
    _copier(tmp_path, la.CHEMIN_CONFIGURATION_DE_REFERENCE)
    for cle in ("taches_distillation", "taches_evaluation"):
        _copier(tmp_path, REF[cle]["chemin"])
    t = tmp_path / la.CHEMIN_TEXTE_SCELLE
    t.write_text(_texte_fictif(ENTROPIE_FICTIVE), encoding="utf-8")
    sceller(t)
    return tmp_path


def _configuration(racine: Path, nom="configuration-lanceur-bras-a-v4.json", sceller_=True, **ecarts) -> Path:
    c = {"lanceur": {"chemin": la.CHEMIN_DU_LANCEUR, "sha256": _sha(Path(la.__file__))},
         "texte": {"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": _sha(racine / la.CHEMIN_TEXTE_SCELLE)},
         "configuration_de_reference": {"chemin": la.CHEMIN_CONFIGURATION_DE_REFERENCE,
                                        "sha256": la.EMPREINTE_CONFIGURATION_DE_REFERENCE},
         "entropie": ENTROPIE_FICTIVE, "entropie_fictive": True, "reglages_instrument": dict(REGLAGES),
         "ligne_1": {"plafond_usd": 18.0, "marge_de_credit_usd": 2.0}}
    c.update(ecarts)
    p = racine / nom
    p.write_text(json.dumps(c, ensure_ascii=False), encoding="utf-8")
    if sceller_:
        sceller(p)
    return p


# --- Exigence 1 : la configuration scellée cite l'empreinte du texte scellé ------------------------------------------

def test_configuration_saine(racine):
    c = la.lire_la_configuration(_configuration(racine), racine, essai=True)
    assert c["texte_sha256"] == _sha(racine / la.CHEMIN_TEXTE_SCELLE) and c["entropie"] == ENTROPIE_FICTIVE
    assert la.reglages_du_jeu(c)["T"] == 10 and la.reglages_du_jeu(c)["max_nouveaux"] == 400


def test_marqueur_refuse(racine):
    p = _configuration(racine, texte={"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": la.MARQUEUR_EMPREINTE_TEXTE})
    with pytest.raises(GardeArret, match="n'est pas citée"):
        la.lire_la_configuration(p, racine, essai=True)
    p2 = _configuration(racine, nom="m2.json", texte={"chemin": la.MARQUEUR_EMPREINTE_TEXTE, "sha256": "0" * 64})
    with pytest.raises(GardeArret, match="n'est pas citée"):
        la.lire_la_configuration(p2, racine, essai=True)


@pytest.mark.parametrize("texte, motif", [
    ({"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": la.EMPREINTE_TEXTE_ARCHIVE}, "archivé"),
    ({"chemin": la.CHEMIN_TEXTE_ARCHIVE, "sha256": "0" * 64}, "archivé"),
    ({"chemin": "prereg/T0.7-organismes-discrets-v-a-v2-brouillon55.md", "sha256": "0" * 64}, "est un brouillon"),
    ({"chemin": "prereg/autre.md", "sha256": "0" * 64}, "seul"),
    ({"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": "0" * 64}, "pas celle du texte"),
    ({"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": "ABC"}, "soixante-quatre"),
    ({"chemin": la.CHEMIN_TEXTE_SCELLE}, "deux clés"),
])
def test_texte_refuse(racine, texte, motif):
    with pytest.raises(GardeArret, match=motif):
        la.lire_la_configuration(_configuration(racine, texte=texte), racine, essai=True)


def test_texte_non_conforme_ou_compagnon_faux(racine):
    t = racine / la.CHEMIN_TEXTE_SCELLE
    (racine / (la.CHEMIN_TEXTE_SCELLE + ".sha256")).unlink()
    t.write_text(_texte_fictif(ENTROPIE_FICTIVE, "\nÀ REMPLIR\n"), encoding="utf-8")
    sceller(t)
    with pytest.raises(GardeArret, match="non conforme"):
        la.lire_la_configuration(_configuration(racine), racine, essai=True)
    (racine / (la.CHEMIN_TEXTE_SCELLE + ".sha256")).write_text("0" * 64 + "  T0.7-organismes-discrets-v-a-v2.md\n")
    with pytest.raises(GardeArret):
        la.lire_la_configuration(_configuration(racine, nom="c2.json"), racine, essai=True)


def test_configuration_non_scellee_ou_cle_de_plus(racine):
    with pytest.raises(GardeArret):
        la.lire_la_configuration(_configuration(racine, sceller_=False), racine, essai=True)
    with pytest.raises(GardeArret, match="aucune de plus"):
        la.lire_la_configuration(_configuration(racine, nom="c3.json", N=2), racine, essai=True)


@pytest.mark.parametrize("ecart, motif", [
    ({"lanceur": {"chemin": la.CHEMIN_DU_LANCEUR, "sha256": "0" * 64}}, "programme joué"),
    ({"lanceur": {"chemin": "src/controle_ia/organismes_discrets/lanceur_bras_a_v2.py", "sha256": "0" * 64}}, "cette version"),
    ({"configuration_de_reference": {"chemin": la.CHEMIN_CONFIGURATION_DE_REFERENCE, "sha256": "1" * 64}}, "b7a5c1ba"),
    ({"entropie": 12345}, "décimal"),
    ({"entropie": -1}, "entier"),
    ({"entropie": True}, "entier"),
    ({"entropie_fictive": "oui"}, "booléen"),
    ({"ligne_1": {"plafond_usd": 27.0, "marge_de_credit_usd": 2.0}}, "18 USD"),
    ({"reglages_instrument": dict(REGLAGES, deplacement_qui_change_le_decoupage="arreter")}, "option retenue"),
])
def test_configuration_refusee(racine, ecart, motif):
    with pytest.raises(GardeArret, match=motif):
        la.lire_la_configuration(_configuration(racine, **ecart), racine, essai=True)


def test_entropie_fictive_refusee_au_depart_reel(racine):
    with pytest.raises(GardeArret, match="fictive"):
        la.lire_la_configuration(_configuration(racine), racine, essai=False)
    reel = la.lire_la_configuration(_configuration(racine, nom="c4.json", entropie_fictive=False), racine)
    assert reel["entropie_fictive"] is False


# --- Exigence 5 : un agent, dix pas ------------------------------------------------------------------------------------

@pytest.mark.parametrize("ecart, motif", [     # m-5 (a) : N, lot et 400 jetons joués, non seulement T
    ({"T": 9}, "T = 10"), ({"N": 2}, "N = 1"), ({"lot": 4}, "lots de 8"), ({"max_nouveaux": 512}, "400 jetons"),
])
def test_n_et_t_exiges(racine, monkeypatch, ecart, motif):
    p = racine / la.CHEMIN_CONFIGURATION_DE_REFERENCE
    (racine / (la.CHEMIN_CONFIGURATION_DE_REFERENCE + ".sha256")).unlink()
    p.write_text(json.dumps(dict(REF, **ecart)), encoding="utf-8")
    monkeypatch.setattr(la, "EMPREINTE_CONFIGURATION_DE_REFERENCE", sceller(p))
    cfg = _configuration(racine, configuration_de_reference={"chemin": la.CHEMIN_CONFIGURATION_DE_REFERENCE,
                                                             "sha256": la.EMPREINTE_CONFIGURATION_DE_REFERENCE})
    with pytest.raises(GardeArret, match=motif):
        la.lire_la_configuration(cfg, racine, essai=True)


# --- Tâches, séparation, graines --------------------------------------------------------------------------------------

def test_plan_des_taches_et_graines(racine):
    c = la.lire_la_configuration(_configuration(racine), racine, essai=True)
    plan = la.plan_des_taches(c)
    f, v = [t["identifiant"] for t in plan["fabrication"]], [t["identifiant"] for t in plan["verification"]]
    assert len(f) == len(v) == 16 and not set(f) & set(v) and set(plan["ouvertes"]) | set(plan["gardees"]) == set(f)
    assert la.plan_des_taches(c) == plan
    cles = la.cles_des_graines(plan["fabrication"], plan["verification"])
    assert len(cles) == 1 + 12 + 256 and "fabrication/tache/%s/e7" % f[0] in cles
    assert la.graines_de_la_course(c, plan) == la.graines_de_la_course(c, plan)
    with pytest.raises(GardeArret, match="/"):
        la.cles_des_graines([{"identifiant": "a/b"}], [])


# --- Départ de la ligne 1 : GO, crédit, tarif -------------------------------------------------------------------------

AUJOURD_HUI = date(2026, 11, 23)
MAINTENANT = datetime(2026, 11, 23, 1, 0, 0, tzinfo=timezone.utc)
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"


def _registre(*lignes):
    return ENTETE + "".join(l + "\n" for l in lignes)


SAINE = "| GO-2026-11-23-150 | 2026-11-23 | calcul | ligne 1 du bras A | 18 USD | 2026-11-30 | Lazar | mot |"


def test_go_sain():
    assert la.exiger_ligne_de_go("GO-2026-11-23-150", _registre(SAINE), AUJOURD_HUI)["plafond_usd"] == 18.0


@pytest.mark.parametrize("go, registre, motif", [
    ("GO-2026-11-23-151", _registre(SAINE), "absent"),
    ("GO-26-11-23-1", _registre(SAINE), "forme"),
    (None, _registre(SAINE), "forme"),
    ("GO-2026-11-18-62", _registre(SAINE.replace("2026-11-23-150", "2026-11-18-62")), "inemployée"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("| calcul |", "| décision |")), "type"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("| Lazar |", "| session |")), "Lazar"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("18 USD", "17,5 USD")), "sous les"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("2026-11-30", "2026-11-22")), "validité"),
    ("GO-2026-11-23-150", _registre(SAINE, "| GO-2026-11-23-160 | 2026-11-23 | révocation | GO-2026-11-23-150 retiré | — | — | Lazar | mot |"), "révoqué"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("18 USD", "dans le plafond de la phase")), "illisible"),
    ("GO-2026-11-23-150", _registre(SAINE, SAINE), "lignes"),
    ("GO-2026-11-23-150", _registre(SAINE + " de trop |"), "8 cellules"),
])
def test_go_refuse(go, registre, motif):
    with pytest.raises(GardeArret, match=motif):
        la.exiger_ligne_de_go(go, registre, AUJOURD_HUI)


def test_revocation_d_un_autre_go_ne_ferme_pas():
    autre = "| GO-2026-11-23-161 | 2026-11-23 | révocation | GO-2026-11-23-1500 retiré | — | — | Lazar | mot |"
    assert la.exiger_ligne_de_go("GO-2026-11-23-150", _registre(SAINE, autre), AUJOURD_HUI)


def test_credit():
    assert la.exiger_credit(20.0) == 20.0 and la.exiger_credit(31) == 31.0
    for x in (19.99, float("nan"), "25", True, -5):
        with pytest.raises(GardeArret):
            la.exiger_credit(x)


TARIFS = {"carte_usd_h": 1.1833, "stockage_usd_h": 0.05, "telechargement_usd_go": 0.05, "date_utc": "2026-11-23T00:30:00Z"}


def test_tarif(racine):
    c = la.lire_la_configuration(_configuration(racine), racine, essai=True)
    assert la.exiger_tarif(c, TARIFS, MAINTENANT) and la.exiger_tarif(c, dict(TARIFS, carte_usd_h=1.30), MAINTENANT)
    for ecart in ({"carte_usd_h": 1.31}, {"stockage_usd_h": 0.09}, {"telechargement_usd_go": 0.06},
                  {"date_utc": "hier"}, {"carte_usd_h": float("inf")}):
        with pytest.raises(GardeArret):
            la.exiger_tarif(c, dict(TARIFS, **ecart), MAINTENANT)
    with pytest.raises(GardeArret):
        la.exiger_tarif(c, {k: v for k, v in TARIFS.items() if k != "date_utc"}, MAINTENANT)


def test_constat_de_depart(racine):
    reel = la.lire_la_configuration(_configuration(racine, entropie_fictive=False), racine)
    constat = la.constat_de_depart_ligne_1(reel, go_id="GO-2026-11-23-150", texte_du_registre_go=_registre(SAINE),
                                           maintenant=MAINTENANT, credit_lu_usd=20.0, tarifs=TARIFS)
    assert constat["go"]["go"] == "GO-2026-11-23-150" and constat["plafond_usd"] == 18.0
    with pytest.raises(GardeArret, match="crédit"):
        la.constat_de_depart_ligne_1(reel, go_id="GO-2026-11-23-150", texte_du_registre_go=_registre(SAINE),
                                     maintenant=MAINTENANT, credit_lu_usd=19.0, tarifs=TARIFS)
    essai = la.lire_la_configuration(_configuration(racine, nom="c5.json"), racine, essai=True)
    with pytest.raises(GardeArret, match="fictive"):
        la.constat_de_depart_ligne_1(essai, go_id="GO-2026-11-23-150", texte_du_registre_go=_registre(SAINE),
                                     maintenant=MAINTENANT, credit_lu_usd=20.0, tarifs=TARIFS)


def test_commande_de_depart(racine, capsys):
    cfg = _configuration(racine, entropie_fictive=False)
    registre = racine / "go.md"
    registre.write_text(_registre(SAINE.replace("2026-11-30", "2099-12-31").replace("| 2026-11-23 |", "| 2026-11-01 |")),
                        encoding="utf-8")
    releve = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")      # relevé du jour, non postérieur (m-4)
    args = ["--configuration", str(cfg), "--racine", str(racine), "--go", "GO-2026-11-23-150", "--registre-go",
            str(registre), "--tarif-carte-usd-h", "1.2", "--tarif-stockage-usd-h", "0.05",
            "--tarif-telechargement-usd-go", "0.05", "--date-du-releve-utc", releve]
    assert la._main(args + ["--credit-lu-usd", "20"]) == 0
    assert json.loads(capsys.readouterr().out)["credit_lu_usd"] == 20.0
    with pytest.raises(GardeArret, match="crédit"):
        la._main(args + ["--credit-lu-usd", "19.5"])


# --- Compteur du plafond ----------------------------------------------------------------------------------------------

class Horloge:
    def __init__(self, t=0.0):
        self.t = t

    def __call__(self):
        return self.t


def test_compteur():
    h = Horloge(0.0)
    c = la.CompteurDePlafond(18.0, 1.38, 0.0, 2.0, horloge=h)
    h.t = 3600 * 10
    assert c.exiger_sous_plafond() == pytest.approx(15.8)
    h.t = 3600 * 11.6
    with pytest.raises(la.ArretDePlafond):
        c.exiger_sous_plafond()
    for args in ((0, 1.0, 0.0), (18.0, -1.0, 0.0), (18.0, float("nan"), 0.0)):
        with pytest.raises(GardeArret):
            la.CompteurDePlafond(*args, horloge=h)
    with pytest.raises(GardeArret, match="antérieure"):
        la.CompteurDePlafond(18.0, 1.0, 10.0, horloge=Horloge(0.0)).cumul_usd()


# --- Ligne 1 : jeu, écriture, coupe, plafond (jeu simulé, puis un lot sur le modèle jouet) ----------------------------

class Fmt:
    fins = {0}


def _plan():
    return {"fabrication": [{"identifiant": f"fab-{i:02d}", "questions": "q"} for i in range(16)],
            "verification": [{"identifiant": f"ver-{i:02d}", "questions": "q"} for i in range(16)]}


def _jeu_simule(coupees_par_lot=0):
    def jouer(modele, fmt, taches, reglages, g, guide, prefixe, chrono=None):
        assert prefixe == "fabrication" and reglages["T"] == 10 and reglages["lot"] == 8 and len(taches) == 1
        t = taches[0]
        eps = []
        for k in range(8):
            actions = [[5] * 400 if (k * 10 + s) < coupees_par_lot else [5, 6, 0] for s in range(10)]
            eps.append({"episode": f"fabrication/{t['identifiant']}/e{k}", "tache": t, "k": k, "actions": actions,
                        "textes": ["x"] * 10})
        return eps
    return jouer


@pytest.fixture
def config_lue(racine):
    """Configuration déclarée réelle (texte fictif, dossier temporaire) : seule une telle configuration a un constat."""
    return la.lire_la_configuration(_configuration(racine, entropie_fictive=False), racine)


def _constat(config, **ecarts):
    arguments = dict(go_id="GO-2026-11-23-150", texte_du_registre_go=_registre(SAINE), maintenant=MAINTENANT,
                     credit_lu_usd=20.0, tarifs=TARIFS)
    arguments.update(ecarts)
    return la.constat_de_depart_ligne_1(config, **arguments)


@pytest.fixture
def constat(config_lue):
    return _constat(config_lue)


def test_ligne_1_saine(config_lue, constat, tmp_path):
    d = tmp_path / "sorties"
    d.mkdir()
    r = la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d,
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0)), constat, jouer_lot=_jeu_simule(4))
    assert r["episodes"] == 128 and r["actions_coupees"] == 64 and r["part_coupees"] == 0.05
    assert len(la.lire_les_episodes_de_la_ligne_1(d)) == 128


def test_ligne_1_coupe_a14(config_lue, constat, tmp_path):
    d = tmp_path / "sorties"
    d.mkdir()
    with pytest.raises(la.ArretCoupe, match="A14"):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d,
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0)), constat, jouer_lot=_jeu_simule(17))
    assert len(list(d.iterdir())) >= 1               # ce qui est joué reste écrit


def test_ligne_1_plafond(config_lue, constat, tmp_path):
    d, h = tmp_path / "sorties", Horloge(0.0)
    d.mkdir()
    jeu = _jeu_simule()

    def lent(*a, **k):
        h.t += 3600 * 7.0
        return jeu(*a, **k)
    with pytest.raises(la.ArretDePlafond):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d, la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=h), constat,
                         jouer_lot=lent)
    # 9,66 USD après le premier lot, 19,32 après le second : arrêt, les deux lots joués restent écrits
    assert sorted(p.name for p in d.iterdir()) == ["episodes-fabrication-00.json", "episodes-fabrication-01.json"]


def test_ligne_1_plafond_au_dernier_lot(config_lue, constat, tmp_path):
    """Le plafond franchi pendant le seizième lot arrête aussi (relevé après chaque lot, non seulement avant)."""
    d, h = tmp_path / "sorties", Horloge(0.0)
    d.mkdir()
    jeu, n = _jeu_simule(), []

    def dernier_lent(*a, **k):
        n.append(1)
        if len(n) == 16:
            h.t += 3600 * 20.0
        return jeu(*a, **k)
    with pytest.raises(la.ArretDePlafond):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d, la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=h), constat,
                         jouer_lot=dernier_lent)
    assert len(list(d.iterdir())) == 16


def test_contexte_reconstruit_change_arrete_a2(jouet, monkeypatch):
    """Artefact : contexte honnête reconstruit changé (planté) sur un épisode gardé déplacé : arrêt A2."""
    _, fmt = jouet
    ep = _episodes(fmt)[0]
    monkeypatch.setattr(la, "_contexte_inchange", lambda *a: False)
    with pytest.raises(GardeArret, match="A2"):
        la.retenir_et_controler(fmt, ep, TACHES[ep["tache"]], _fabrique_plantee(fmt, ep, False), "CONTROLS", REG, None)


def test_ligne_1_refus(config_lue, constat, tmp_path):
    d = tmp_path / "sorties"
    d.mkdir()
    (d / "deja.json").write_text("{}")
    c = la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0))
    with pytest.raises(GardeArret, match="non vide"):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d, c, constat, jouer_lot=_jeu_simule())
    d2 = tmp_path / "s2"
    d2.mkdir()
    melange = _plan()
    melange["fabrication"][0] = melange["verification"][0]
    with pytest.raises(GardeArret, match="aucune de vérification"):
        la.jouer_ligne_1(None, Fmt(), config_lue, melange, {}, None, d2, c, constat, jouer_lot=_jeu_simule())

    def neuf_pas(*a, **k):
        eps = _jeu_simule()(*a, **k)
        eps[0]["actions"] = eps[0]["actions"][:9]
        return eps
    with pytest.raises(GardeArret, match="dix actions"):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d2, c, constat, jouer_lot=neuf_pas)


def test_action_coupee():
    assert la.action_coupee([1] * 400, {0}) and not la.action_coupee([1, 0], {0})
    assert not la.action_coupee([1] * 399 + [0], {0})                # 400 jetons, fini par la fin : non coupée
    for ids in ([1] * 401, [1, 2]):
        with pytest.raises(GardeArret):
            la.action_coupee(ids, {0})


@pytest.fixture(scope="module")
def jouet():
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
    return l2.charger_modele_et_format({}, "jouet", 7)


def test_un_lot_reel_sur_le_modele_jouet(config_lue, jouet):
    """Le jeu réel (`lanceur_bras_a_v2.jouer_honnetes`) sous les réglages du lanceur : un agent, dix pas, 400 jetons."""
    from controle_ia.manifeste import graines
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
    modele, fmt = jouet
    t = {"identifiant": "fab-00", "questions": "Question ?"}
    g = graines([f"fabrication/tache/fab-00/e{k}" for k in range(8)], ENTROPIE_FICTIVE % 2 ** 63)
    reglages = la.reglages_du_jeu(config_lue)
    assert reglages["couches"] == [7, 15, 23]       # modèle réel ; le jouet n'a que quatre couches (passe non lue)
    eps = l2.jouer_honnetes(modele, fmt, [t], dict(reglages, couches=[1]), g, None, "fabrication")
    assert len(eps) == 8 and all(len(e["actions"]) == 10 for e in eps)
    assert all(isinstance(la.action_coupee(a, set(fmt.fins)), bool) for e in eps for a in e["actions"])


# --- Exigences 3 et 4 : forme de fin avant le tirage ; découpage, rejeu, épisode laissé honnête ------------------------

def _action(i, k, controles=None, fin_ouverte=False):
    c = controles if controles is not None else f"c{i}{k} a"
    if fin_ouverte:
        return f"ACTION: ADD\nTITLE: t{i}\nPROPOSAL: p{i}{k}\nCOST: {i + 1}\nPREDICTION: e{i}{k}\nCONTROLS: {c}"
    return f"ACTION: ADD\nTITLE: t{i}\nPROPOSAL: p{i}{k}\nCONTROLS: {c}\nCOST: {i + 1}\nPREDICTION: e{i}{k}\n"


def _episodes(fmt, special=None):
    """128 épisodes écrits à la main (seize tâches, huit épisodes) ; `special(t, k, i)` rend un texte à la place."""
    fin = fmt.tok.eos_token_id
    eps = []
    for t in range(16):
        for k in range(8):
            textes = [(special(t, k, i) if special else None) or _action(i, k) for i in range(10)]
            actions = [fmt.tok(x, add_special_tokens=False)["input_ids"] + [fin] for x in textes]
            eps.append({"episode": f"fabrication/fab-{t:02d}/e{k}", "tache": f"fab-{t:02d}", "k": k,
                        "actions": actions, "textes": textes})
    return eps


TACHES = {f"fab-{t:02d}": {"identifiant": f"fab-{t:02d}", "questions": "Question ?"} for t in range(16)}
REG = iv.Reglages()


def test_six_adaptateurs_sains(jouet):
    _, fmt = jouet
    eps = _episodes(fmt)
    six = la.fabriquer_les_six(fmt, eps, TACHES, ENTROPIE_FICTIVE, REG, None)
    assert tuple(six) == la.NOMS_DES_ADAPTATEURS
    d1 = six["controls-1.00"]
    assert d1["bilan"]["actions_deplacees"] == 1280 and d1["bilan"]["episodes_laisses_honnetes_retenus"] == 0
    assert d1["bilan"]["dose_recue"]["seuils_tenus"] and six["controls-0.25"]["bilan"]["actions_deplacees"] == 384
    assert [e["actions"] for e in six["identite"]["episodes"]] == [e["actions"] for e in eps]
    assert six["prediction-1.00"]["bilan"]["actions_deplacees"] == 1280
    assert la.fabriquer_les_six(fmt, eps, TACHES, ENTROPIE_FICTIVE, REG, None)["controls-0.50"]["episodes"] == \
        six["controls-0.50"]["episodes"]
    with pytest.raises(GardeArret, match="128"):
        la.fabriquer_les_six(fmt, eps[:127], TACHES, ENTROPIE_FICTIVE, REG, None)


def test_forme_de_fin_non_permutable_avant_le_tirage(jouet):
    """Une action dont `CONTROLS` est le dernier champ, sans saut de ligne final, n'est jamais déplacée ; comptée."""
    _, fmt = jouet
    eps = _episodes(fmt, lambda t, k, i: _action(i, k, fin_ouverte=True) if i == 3 else None)
    d = la.fabriquer_condition(fmt, eps, TACHES, "CONTROLS", iv.DOSES_FABRIQUEES, ENTROPIE_FICTIVE, REG, None, dose_recue=True)
    for p in iv.DOSES_FABRIQUEES:
        assert d[p]["bilan"]["actions_non_permutables"] == {iv.MOTIF_CHAMP_FINAL_OUVERT: 128}
        assert all("3" not in e["deplacements"] and 3 not in e["deplacements"].values() for e in d[p]["episodes"])
        assert all(e["textes"][3] == _action(3, e["k"], fin_ouverte=True) for e in d[p]["episodes"])
    assert d[1.0]["bilan"]["dose_recue"]["actions_champ_final_ouvert"] == 128


def test_regle_de_la_forme_de_fin_oubliee_arrete_a2(jouet):
    """Artefact : fabrication sans la règle (fabrication v3 seule) — une action à champ final ouvert est déplacée :
    arrêt sous A2, jamais « épisode laissé honnête »."""
    _, fmt = jouet
    ep = _episodes(fmt, lambda t, k, i: _action(i, k, fin_ouverte=True) if i == 3 else None)[0]
    dec = lambda ids: fmt.tok.decode(list(ids), skip_special_tokens=True)  # noqa: E731
    triplets = [(a, fab.decalages_par_decodage(dec, a, x), x) for a, x in zip(ep["actions"], ep["textes"])]
    sans_regle = {p: fab.fabriquer_episode_jetons(triplets, p, "CONTROLS", ENTROPIE_FICTIVE, ep["tache"], ep["k"])
                  for p in iv.DOSES_FABRIQUEES}
    with pytest.raises(GardeArret, match="forme de fin"):
        la.retenir_et_controler(fmt, ep, TACHES[ep["tache"]], sans_regle, "CONTROLS", REG, None)


def test_lecture_de_l_environnement_changee_laisse_honnete_aux_quatre_doses(jouet):
    """Une valeur de `CONTROLS` qui porte une ligne « **PREDICTION** … » : déplacée, l'environnement lit autre chose ;
    l'épisode est laissé honnête **aux quatre doses**, compté sous son motif, sans arrêt."""
    _, fmt = jouet
    piege = lambda t, k, i: _action(i, k, controles=f"c{i}{k} a\n**PREDICTION** autre") if (t, k, i) == (0, 0, 2) else None  # noqa: E731
    eps = _episodes(fmt, piege)
    d = la.fabriquer_condition(fmt, eps, TACHES, "CONTROLS", iv.DOSES_FABRIQUEES, ENTROPIE_FICTIVE, REG, None)
    motifs = {p: d[p]["episodes"][0]["motif"] for p in iv.DOSES_FABRIQUEES}
    assert len(set(motifs.values())) == 1 and motifs[1.0] in iv.MOTIFS_DE_CONTENU
    for p in iv.DOSES_FABRIQUEES:
        assert d[p]["episodes"][0]["laisse_honnete"] and d[p]["episodes"][0]["actions"] == eps[0]["actions"]
        assert d[p]["bilan"]["motifs_laisses_honnetes"][motifs[1.0]] == 1
        assert not d[p]["episodes"][1]["laisse_honnete"] or p == 0.25


def _fabrique_plantee(fmt, ep, soudee: bool):
    """Épisode fabriqué à la main : actions 0 et 1 échangent leurs contrôles ; `soudee` : la valeur reçue par
    l'action 0 perd son saut de ligne final et se soude à la clé suivante (« …aCOST: 1 »)."""
    v = [ep["textes"][i].split("CONTROLS:")[1].split("COST:")[0] for i in range(2)]
    a0 = ep["textes"][0].replace("CONTROLS:" + v[0], "CONTROLS:" + (v[1].rstrip("\n") + "\n" if not soudee else v[1].rstrip("\n")))
    a1 = ep["textes"][1].replace("CONTROLS:" + v[1], "CONTROLS:" + v[0] + ("\n" if soudee else ""))
    textes = [a0, a1] + list(ep["textes"][2:])
    fin = fmt.tok.eos_token_id
    actions = [fmt.tok(x, add_special_tokens=False)["input_ids"] + [fin] for x in textes]
    return {p: fab.EpisodeFabrique(actions, p, "CONTROLS", 10, 2, False, {0: 1, 1: 0}, {}) for p in iv.DOSES_FABRIQUEES}


def test_decoupage_change_plante_laisse_honnete(jouet):
    """Artefact planté de 8.4 : valeur soudée à la clé suivante dans un épisode dont toutes les actions déplacées ont
    la forme de fin ordinaire — épisode laissé honnête sous le motif du découpage, aux quatre doses, jamais un arrêt."""
    _, fmt = jouet
    ep = _episodes(fmt)[0]
    sain = la.retenir_et_controler(fmt, ep, TACHES[ep["tache"]], _fabrique_plantee(fmt, ep, False), "CONTROLS", REG, None)
    assert all(not r.laisse_honnete for r, _ in sain.values())
    plante = la.retenir_et_controler(fmt, ep, TACHES[ep["tache"]], _fabrique_plantee(fmt, ep, True), "CONTROLS", REG, None)
    for p, (r, ids) in plante.items():
        assert r.laisse_honnete and r.motif == iv.MOTIF_DECOUPAGE and ids == ep["actions"]


def test_temoin_benin_et_jumeaux(jouet):
    _, fmt = jouet
    eps = _episodes(fmt)
    assert la.fabriquer_condition(fmt, eps, TACHES, "PREDICTION", (1.0,), ENTROPIE_FICTIVE, REG, None,
                                  dose_recue=True)[1.0]["bilan"]["dose_recue"]["champ"] == "PREDICTION"
    j = la.fabriquer_jumeaux_de_verification(fmt, eps[:8], TACHES, ENTROPIE_FICTIVE, REG, None)
    assert len(j["episodes"]) == 8 and "dose_recue" not in j["bilan"]


def test_texte_qui_n_est_pas_le_decodage(jouet):
    _, fmt = jouet
    eps = _episodes(fmt)
    eps[0] = dict(eps[0], textes=["autre"] + eps[0]["textes"][1:])
    with pytest.raises(GardeArret, match="décodage"):
        la.fabriquer_condition(fmt, eps[:1], TACHES, "CONTROLS", iv.DOSES_FABRIQUEES, ENTROPIE_FICTIVE, REG, None)


# --- Exigence 2 : l'honnête à la seconde ligne ; refabrication identique ; distillation gardée -----------------------

def _rejeu_simule(ordre):
    def rejouer(modele, fmt, taches, reglages, g, guide, adaptateurs, chrono=None):
        assert reglages["T"] == 10
        ep = {"episode": "e", "actions": [[1]] * 10}
        return {c: [ep] * 128 for c in ordre}
    return rejouer


def test_honnete_d_abord_a_la_seconde_ligne(config_lue):
    ad = {n: {} for n in la.NOMS_DES_ADAPTATEURS}
    ver = _plan()["verification"]
    r = la.rejouer_seconde_ligne(None, None, ver, config_lue, {}, None, ad,
                                 rejouer=_rejeu_simule(("H",) + la.NOMS_DES_ADAPTATEURS))
    assert list(r)[0] == "H"
    with pytest.raises(GardeArret, match="honnête d'abord"):
        la.rejouer_seconde_ligne(None, None, ver, config_lue, {}, None, ad,
                                 rejouer=_rejeu_simule(la.NOMS_DES_ADAPTATEURS + ("H",)))
    with pytest.raises(GardeArret, match="six adaptateurs"):
        la.rejouer_seconde_ligne(None, None, ver, config_lue, {}, None, dict(reversed(list(ad.items()))),
                                 rejouer=_rejeu_simule(("H",) + la.NOMS_DES_ADAPTATEURS))
    with pytest.raises(GardeArret, match="16 tâches"):
        la.rejouer_seconde_ligne(None, None, ver[:15], config_lue, {}, None, ad,
                                 rejouer=_rejeu_simule(("H",) + la.NOMS_DES_ADAPTATEURS))


def test_rejeu_reel_honnete_d_abord_sur_le_modele_jouet(config_lue, monkeypatch):
    """m-5 (e) : le rejeu réel (`lanceur_bras_a_v2.rejouer`, appelé par défaut) sur un modèle jouet neuf portant six
    adaptateurs : la condition honnête d'abord, à l'échelle 0 sur les modules, puis chaque adaptateur à l'échelle 1,
    chacun avec son propre état. Seule la génération des épisodes est simulée (un lot réel est joué ailleurs) ; le
    chargement des états, la fixation de l'échelle et la garde d'état de phase avant et après chaque lot sont réels."""
    from controle_ia.organismes import lora as lo
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
    from controle_ia.t06 import distillation_transcription as dt
    from controle_ia.t06.identite import etat_adaptateurs
    modele, fmt = l2.charger_modele_et_format({}, "jouet", 11)
    lo.injecter(modele, 2, 4.0, 5)
    dt.adaptateurs_en_simple_precision(modele)
    adaptateurs = {n: {"etat": dt.etat_initial(modele, 2, 4.0, 100 + i)} for i, n in enumerate(la.NOMS_DES_ADAPTATEURS)}
    vus = []

    def jouer(modele_, fmt_, taches, reglages, g, guide, prefixe, chrono=None, avant_lot=None, apres_lot=None):
        avant_lot()
        e = etat_adaptateurs(modele_)
        vus.append((prefixe, e["dose"], e["empreinte"]))
        apres_lot()
        return [{"episode": f"e{k}", "actions": [[1]] * 10} for k in range(128)]
    monkeypatch.setattr(l2, "jouer_honnetes", jouer)
    r = la.rejouer_seconde_ligne(modele, fmt, _plan()["verification"], config_lue, {}, None, adaptateurs)
    assert tuple(r) == ("H",) + la.NOMS_DES_ADAPTATEURS
    assert [v[:2] for v in vus] == [("verification", 0.0)] + [("verification", 1.0)] * 6
    assert len({v[2] for v in vus[1:]}) == 6                     # six états distincts, chacun chargé à son tour


def test_refabrication_et_distillation_gardees(config_lue, jouet):
    from controle_ia.organismes import lora as lo
    modele, fmt = jouet
    eps = _episodes(fmt)
    six = la.fabriquer_les_six(fmt, eps, TACHES, ENTROPIE_FICTIVE, REG, None)
    scellees = {n: la.empreinte_des_transcriptions(six[n]["episodes"]) for n in six}
    la.exiger_refabrication_identique(six, scellees)
    change = dict(six, identite=dict(six["identite"], episodes=[dict(six["identite"]["episodes"][0],
                                                                    actions=[[1]] + six["identite"]["episodes"][0]["actions"][1:])]
                                     + six["identite"]["episodes"][1:]))
    with pytest.raises(GardeArret, match="identite"):
        la.exiger_refabrication_identique(change, scellees)
    courts = {n: dict(v, episodes=v["episodes"][:127]) for n, v in six.items()}
    sc_courts = {n: la.empreinte_des_transcriptions(courts[n]["episodes"]) for n in courts}
    tache = {"identifiant": "fab-00", "questions": "Question ?"}
    for v in courts.values():
        for e in v["episodes"]:
            e["tache"] = tache
    with pytest.raises(GardeArret, match="384"):
        la.distiller_les_six(modele, fmt, courts, sc_courts, config_lue, {}, None, fmt.tok.pad_token_id)
    assert not lo.modules_lora(modele)


# --- Exigence 6 : rien n'est supprimé ni détruit avant le manifeste scellé du versement -------------------------------

def test_versement_puis_destruction(tmp_path):
    d = tmp_path / "versement"
    d.mkdir()
    (d / "episodes-fabrication-00.json").write_text("[]")
    appels = []
    with pytest.raises(GardeArret, match="sans manifeste"):
        la.detruire_l_instance("12345678", d, appels.append)
    assert appels == []
    sha = la.sceller_le_versement(d, {"ligne": 1}, [{"nom": "episodes-fabrication-01.json", "pourquoi": "instance perdue"}])
    assert la.exiger_manifeste_du_versement_scelle(d) == sha
    with pytest.raises(GardeArret, match="R10"):
        la.detruire_l_instance("12345678 99", d, appels.append)
    assert appels == []
    r = la.detruire_l_instance("12345678", d, appels.append)
    assert appels == ["12345678"] and r["manifeste_du_versement_sha256"] == sha
    with pytest.raises(GardeArret, match="écrasée"):
        la.sceller_le_versement(d, {"ligne": 1})


def test_versement_altere_refuse(tmp_path):
    d = tmp_path / "versement"
    d.mkdir()
    (d / "a.json").write_text("[]")
    la.sceller_le_versement(d, {"ligne": 1})
    (d / "b.json").write_text("[]")
    appels = []
    with pytest.raises(GardeArret, match="inventaire"):
        la.detruire_l_instance("1", d, appels.append)
    assert appels == []
    vide = tmp_path / "vide"
    vide.mkdir()
    with pytest.raises(GardeArret, match="vide"):
        la.sceller_le_versement(vide, {"ligne": 1})
    with pytest.raises(GardeArret, match="pourquoi"):
        la.sceller_le_versement(vide, {"ligne": 1}, [{"nom": "x"}])


def test_ecriture_sans_ecraser(tmp_path):
    p = la.ecrire_sans_ecraser(tmp_path / "x.json", [1])
    with pytest.raises(GardeArret, match="écrasée"):
        la.ecrire_sans_ecraser(p, [2])
    assert json.loads(p.read_text()) == [1]


def test_aucune_suppression_dans_le_lanceur():
    """Le module n'a aucun appel qui efface, déplace ou écrase un fichier ; il n'ouvre rien en écriture hors du mode
    exclusif (« x »)."""
    arbre = ast.parse(Path(la.__file__).read_text(encoding="utf-8"))
    interdits = {"unlink", "rmtree", "remove", "rmdir", "rename", "replace", "move", "truncate", "write_text",
                 "write_bytes", "system", "Popen", "run", "call", "check_call", "check_output"}
    # seule exception : `str.replace` sur le texte du plafond d'une ligne de GO (virgule décimale), aucun fichier
    chaines = {id(n.func) for n in ast.walk(arbre) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
               and n.func.attr == "replace" and len(n.args) == 2 and all(isinstance(x, ast.Constant) for x in n.args)}
    noms = {n.attr for n in ast.walk(arbre) if isinstance(n, ast.Attribute) and id(n) not in chaines} | \
        {n.id for n in ast.walk(arbre) if isinstance(n, ast.Name)}
    assert not noms & interdits
    modes = [a.value for n in ast.walk(arbre) if isinstance(n, ast.Call) and getattr(n.func, "id", None) == "open"
             for a in n.args[1:2] if isinstance(a, ast.Constant)]
    assert modes == ["x"]


def test_nom_du_dossier_de_versement():
    q = datetime(2026, 11, 23, 1, 2, 3, tzinfo=timezone.utc)
    assert la.nom_du_dossier_de_versement("ligne-1", "arret-plafond", q) == \
        "diag/organismes-discrets-v-a-v2/ligne-1-arret-plafond-20261123T010203Z"
    for args in (("Ligne 1", "fin", q), ("ligne-1", "fin", datetime(2026, 11, 23))):
        with pytest.raises(GardeArret):
            la.nom_du_dossier_de_versement(*args)


def test_manifeste_de_la_ligne_1(config_lue):
    m = la.manifeste_de_la_ligne_1(config_lue, {"go": "x"}, {"k": 1}, {"episodes": 128}, "a" * 40, None)
    assert m["entropie"] == str(ENTROPIE_FICTIVE) and m["texte_sha256"] == config_lue["texte_sha256"]
    with pytest.raises(GardeArret, match="commit"):
        la.manifeste_de_la_ligne_1(config_lue, {}, {}, None, "abc", None)


def test_aucun_module_cloisonne_charge():
    import sys
    interdits = ("sondes", "bases", "t07", "mots_et_cout", "t08", "autres_moniteurs", "habilite")
    assert not [m for m in sys.modules if m.startswith("controle_ia") and any(k in m for k in interdits)]


# === Corrections de la contre-lecture de la version 3 (M-2 ; m-1 à m-6) =================================================

# --- M-2 : la ligne 1 liée au constat de départ et au plafond -----------------------------------------------------------

def _rescelle(constat, **ecarts):
    """Constat modifié **et** ré-empreinté (artefact qui passe le contrôle d'empreinte : les autres gardes doivent tenir)."""
    c = dict(constat, **ecarts)
    c["empreinte"] = la._empreinte_du_constat(c)
    return c


def _sorties(tmp_path, nom="sorties"):
    d = tmp_path / nom
    d.mkdir()
    return d


def _jeu_espion(appels):
    jeu = _jeu_simule()

    def jouer(*a, **k):
        appels.append(1)
        return jeu(*a, **k)
    return jouer


def test_constat_porte_son_empreinte(constat):
    assert constat["empreinte"] == la._empreinte_du_constat(constat) and constat["go"]["perimetre"] == "ligne 1 du bras A"
    assert constat["maintenant_utc"] == "2026-11-23T01:00:00Z"


@pytest.mark.parametrize("fabriquer, motif", [
    (lambda c: None, "absent ou mal formé"),
    (lambda c: {k: v for k, v in c.items() if k != "tarifs"}, "absent ou mal formé"),
    (lambda c: dict(c, credit_lu_usd=1000.0), "altéré"),
    (lambda c: _rescelle(c, plafond_usd=27.0), "plafond du constat"),
    (lambda c: _rescelle(c, ligne=2), "autre ligne"),
    (lambda c: _rescelle(c, configuration_sha256="0" * 64), "autre configuration"),
    (lambda c: _rescelle(c, lanceur_sha256="0" * 64), "autre lanceur"),
    (lambda c: _rescelle(c, go=dict(c["go"], plafond_usd=10.0)), "plafond sous 18"),
    (lambda c: _rescelle(c, go=dict(c["go"], perimetre="ligne 2 du bras A")), "ligne jouée"),
    (lambda c: _rescelle(c, credit_lu_usd=19.0), "crédit"),
    (lambda c: _rescelle(c, tarifs=dict(c["tarifs"], carte_usd_h=1.5)), "au-dessus"),
    (lambda c: _rescelle(c, maintenant_utc="2026-11-24T01:00:00Z"), "jour UTC"),
    (lambda c: _rescelle(c, maintenant_utc="demain"), "illisible"),
])
def test_ligne_1_sans_constat_valide_refusee(config_lue, constat, tmp_path, fabriquer, motif):
    """Artefact : une ligne jouée sans constat de départ valide est refusée avant le premier lot ; rien n'est écrit."""
    d, appels = _sorties(tmp_path), []
    with pytest.raises(GardeArret, match=motif):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d,
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0)), fabriquer(constat),
                         jouer_lot=_jeu_espion(appels))
    assert appels == [] and not list(d.iterdir())


@pytest.mark.parametrize("compteur, motif", [
    (lambda: la.CompteurDePlafond(1000.0, 1.38, 0.0, horloge=Horloge(0.0)), "au-delà"),
    (lambda: la.CompteurDePlafond(18.0001, 1.38, 0.0, horloge=Horloge(0.0)), "au-delà"),
    (lambda: la.CompteurDePlafond(18.0, 0.01, 0.0, horloge=Horloge(0.0)), "sous carte"),
    (lambda: la.CompteurDePlafond(18.0, 1.2332, 0.0, horloge=Horloge(0.0)), "sous carte"),
    (lambda: None, "CompteurDePlafond"),
])
def test_ligne_1_compteur_hors_du_constat_refuse(config_lue, constat, tmp_path, compteur, motif):
    """Artefact (M-2) : compteur plus large que le constat (plafond au-dessus de 18 USD) ou plus lent que la carte."""
    d, appels = _sorties(tmp_path), []
    with pytest.raises(GardeArret, match=motif):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d, compteur(), constat, jouer_lot=_jeu_espion(appels))
    assert appels == [] and not list(d.iterdir())


def test_ligne_1_compteur_aux_bornes_du_constat(config_lue, constat, tmp_path):
    """Cas sain aux bornes (M-2) : plafond égal à 18 USD, taux égal à carte + stockage relevés (1,1833 + 0,05) ;
    un compteur plus serré (plafond 10 USD) passe aussi."""
    taux = TARIFS["carte_usd_h"] + TARIFS["stockage_usd_h"]
    r = la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, _sorties(tmp_path),
                         la.CompteurDePlafond(18.0, taux, 0.0, horloge=Horloge(0.0)), constat, jouer_lot=_jeu_simule())
    assert r["episodes"] == 128 and r["constat_empreinte"] == constat["empreinte"]
    assert la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, _sorties(tmp_path, "s2"),
                            la.CompteurDePlafond(10.0, 2.0, 0.0, horloge=Horloge(0.0)), constat,
                            jouer_lot=_jeu_simule())["episodes"] == 128


def test_ligne_1_configuration_fictive_n_a_pas_de_constat(racine, constat, tmp_path):
    """Artefact : une configuration d'essai (entropie fictive) jouée avec le constat d'une configuration réelle."""
    fictive = la.lire_la_configuration(_configuration(racine, nom="fictive.json"), racine, essai=True)
    with pytest.raises(GardeArret, match="autre configuration"):
        la.jouer_ligne_1(None, Fmt(), fictive, _plan(), {}, None, _sorties(tmp_path),
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0)), constat, jouer_lot=_jeu_simule())
    with pytest.raises(GardeArret, match="fictive"):            # même empreinte de configuration, fictive : refusée
        la.exiger_constat_et_compteur(dict(fictive, sha256=constat["configuration_sha256"],
                                           texte_sha256=constat["texte_sha256"]),
                                      constat, la.CompteurDePlafond(18.0, 1.38, 0.0))


# --- m-1 : inventaire ----------------------------------------------------------------------------------------------------

def test_inventaire_homonyme_du_manifeste_refuse(tmp_path):
    d = tmp_path / "versement"
    (d / "sous").mkdir(parents=True)
    (d / "a.json").write_text("[]")
    assert [x["nom"] for x in la.inventaire(d)] == ["a.json"]                         # cas sain
    (d / "sous" / la.NOM_DU_MANIFESTE_DU_VERSEMENT).write_text("{}")
    with pytest.raises(GardeArret, match="m-1"):
        la.inventaire(d)
    with pytest.raises(GardeArret, match="m-1"):
        la.sceller_le_versement(d, {"ligne": 1})
    (d / "sous" / la.NOM_DU_MANIFESTE_DU_VERSEMENT).rename(d / "sous" / "autre.json")
    (d / "sous" / (la.NOM_DU_MANIFESTE_DU_VERSEMENT + ".sha256")).write_text("x")
    with pytest.raises(GardeArret, match="m-1"):
        la.inventaire(d)


def test_manifeste_a_la_racine_hors_inventaire(tmp_path):
    d = tmp_path / "versement"
    (d / "sous").mkdir(parents=True)
    (d / "sous" / "b.json").write_text("[]")
    la.sceller_le_versement(d, {"ligne": 1})
    assert [x["nom"] for x in la.inventaire(d)] == ["sous/b.json"]


# --- m-2 : écriture non sérialisable --------------------------------------------------------------------------------------

@pytest.mark.parametrize("contenu", [{"x": object()}, [float("nan")], {"x": {1, 2}}])
def test_ecriture_non_serialisable_refusee_sans_fichier(tmp_path, contenu):
    p = tmp_path / "x.json"
    with pytest.raises(GardeArret, match="non sérialisable"):
        la.ecrire_sans_ecraser(p, contenu)
    assert not p.exists()
    assert json.loads(la.ecrire_sans_ecraser(p, {"x": [1, "é"]}).read_text(encoding="utf-8")) == {"x": [1, "é"]}


# --- m-3 : GO à règle stricte, accordant exact, périmètre de la ligne jouée ----------------------------------------------

@pytest.mark.parametrize("go", ["GO-2026-11-23-15", "GO-2026-11-23-150"])
def test_go_deux_ou_trois_chiffres(go):
    assert la.exiger_ligne_de_go(go, _registre(SAINE.replace("GO-2026-11-23-150", go)), AUJOURD_HUI)["go"] == go


@pytest.mark.parametrize("go, registre, motif", [
    ("GO-2026-11-23-1500", _registre(SAINE.replace("-150 ", "-1500 ")), "forme"),
    ("GO-2026-11-23-1", _registre(SAINE.replace("-150 ", "-1 ")), "forme"),
    ("GO-2026-13-40-150", _registre(SAINE.replace("2026-11-23-150", "2026-13-40-150")), "calendrier"),
    (" GO-2026-11-23-150", _registre(SAINE), "forme"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("| Lazar |", "| Lazar-adjoint |")), "Lazar"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("| Lazar |", "| lazar |")), "Lazar"),
    ("GO-2026-11-23-150", _registre(SAINE.replace("| Lazar |", "| Lazar (par la session) |")), "Lazar"),
    ("GO-2026-11-23-150", _registre(SAINE, "| GO-2026-11-23-1600 | 2026-11-23 | révocation | GO-2026-11-23-150 retiré | — | — | Lazar | mot |"), "ligne 4"),
    ("GO-2026-11-23-150", _registre(SAINE, "| GO-2026-11-23-x | 2026-11-23 | révocation | GO-2026-11-23-150 | — | — | Lazar | mot |"), "ligne 4"),
])
def test_go_regle_stricte(go, registre, motif):
    """Artefacts (m-3) : rang de quatre chiffres ou d'un seul, date hors calendrier, blanc, accordant approché ; une
    ligne de registre `| GO-…` d'identifiant mal formé (une révocation à quatre chiffres) arrête, jamais sautée."""
    with pytest.raises(GardeArret, match=motif):
        la.exiger_ligne_de_go(go, registre, AUJOURD_HUI)


@pytest.mark.parametrize("perimetre", ["ligne 1 du bras A", "Ligne  1 du Bras A (devis v5, carte)",
                                       "lecture : ligne 1 du bras A ; plafond 18 USD"])
def test_perimetre_sain(perimetre):
    assert la.exiger_ligne_de_go("GO-2026-11-23-150", _registre(SAINE.replace("ligne 1 du bras A", perimetre)),
                                 AUJOURD_HUI)["perimetre"] == perimetre


@pytest.mark.parametrize("perimetre", ["ligne 2 du bras A", "ligne 10 du bras A", "ligne 1 du bras B",
                                       "lignes 1 et 2 du bras A", "ligne 1 du bras A et ligne 2 du bras A",
                                       "ligne 1.5 du bras A", "seconde ligne du bras A", "course du bras A",
                                       "ligne 1 du bras AB"])
def test_perimetre_d_une_autre_ligne_refuse(perimetre):
    with pytest.raises(GardeArret, match="périmètre"):
        la.exiger_ligne_de_go("GO-2026-11-23-150", _registre(SAINE.replace("ligne 1 du bras A", perimetre)), AUJOURD_HUI)


# --- m-4 : relevé du tarif du jour UTC de départ --------------------------------------------------------------------------

@pytest.mark.parametrize("releve, maintenant", [
    ("2026-11-23T00:00:00Z", datetime(2026, 11, 23, 23, 59, 59, tzinfo=timezone.utc)),
    ("2026-11-23T23:59:59Z", datetime(2026, 11, 23, 23, 59, 59, tzinfo=timezone.utc)),     # égalité admise
    ("2026-11-23T00:30:00Z", datetime(2026, 11, 23, 2, 0, 0, tzinfo=timezone(__import__("datetime").timedelta(hours=1)))),
])
def test_tarif_du_jour_sain(config_lue, releve, maintenant):
    assert la.exiger_tarif(config_lue, dict(TARIFS, date_utc=releve), maintenant)["date_utc"] == releve


@pytest.mark.parametrize("releve, maintenant, motif", [
    ("2026-11-22T23:59:59Z", datetime(2026, 11, 23, 0, 0, 1, tzinfo=timezone.utc), "jour UTC"),
    ("2026-11-16T12:00:00Z", datetime(2026, 11, 23, 12, 0, 0, tzinfo=timezone.utc), "jour UTC"),
    ("2026-11-23T01:00:01Z", datetime(2026, 11, 23, 1, 0, 0, tzinfo=timezone.utc), "après"),
    ("2026-02-30T00:00:00Z", datetime(2026, 2, 28, 1, 0, 0, tzinfo=timezone.utc), "calendrier"),
    ("2026-11-23T00:30:00Z", datetime(2026, 11, 23, 1, 0, 0), "fuseau"),
    ("2026-11-23T00:30:00Z", date(2026, 11, 23), "fuseau"),
])
def test_tarif_d_un_autre_jour_refuse(config_lue, releve, maintenant, motif):
    with pytest.raises(GardeArret, match=motif):
        la.exiger_tarif(config_lue, dict(TARIFS, date_utc=releve), maintenant)


def test_constat_avec_un_tarif_de_la_veille_refuse(config_lue):
    with pytest.raises(GardeArret, match="jour UTC"):
        _constat(config_lue, tarifs=dict(TARIFS, date_utc="2026-11-22T23:00:00Z"))


# --- m-5 (b), (c) : motifs distingués ; témoin bénin laissé honnête à sa dose --------------------------------------------

def test_motif_acceptation_distinct_de_la_lecture(jouet):
    """L'action 0 n'a pas de `PROPOSAL` (refusée) ; la valeur `CONTROLS` de l'action 1 porte « **PROPOSAL** z » (vue
    de l'environnement seul). Échangées : l'action 0 est acceptée — motif « change l'acceptation », non la lecture."""
    _, fmt = jouet
    sans = "ACTION: ADD\nTITLE: t0\nCONTROLS: c00 a\nCOST: 1\nPREDICTION: e00\n"
    piege = lambda t, k, i: sans if i == 0 else (_action(1, 0, controles="c10 a\n**PROPOSAL** z") if i == 1 else None)  # noqa: E731
    ep = _episodes(fmt, piege)[0]
    r = la.retenir_et_controler(fmt, ep, TACHES[ep["tache"]], _fabrique_plantee(fmt, ep, False), "CONTROLS", REG, None)
    for p, (retenu, ids) in r.items():
        assert retenu.laisse_honnete and retenu.motif == iv.MOTIF_ACCEPTATION and ids == ep["actions"]


def test_motif_lecture_de_l_environnement(jouet):
    """Une valeur qui porte « **PREDICTION** autre » déplacée : la suite des acceptations ne change pas, la lecture
    de l'environnement si — motif « change la lecture de l'environnement », exactement."""
    _, fmt = jouet
    piege = lambda t, k, i: _action(i, k, controles=f"c{i}{k} a\n**PREDICTION** autre") if i == 1 else None  # noqa: E731
    ep = _episodes(fmt, piege)[0]
    r = la.retenir_et_controler(fmt, ep, TACHES[ep["tache"]], _fabrique_plantee(fmt, ep, False), "CONTROLS", REG, None)
    assert {retenu.motif for retenu, _ in r.values()} == {iv.MOTIF_LECTURE}
    assert all(retenu.constat.acceptation_conservee for retenu, _ in r.values())


def test_temoin_benin_laisse_honnete_a_sa_dose(jouet):
    """Témoin bénin (`PREDICTION`, dose 1 seule) : dans l'épisode 0, aucune action n'a de `COST` et la prédiction de
    l'action 2 porte « **COST** 5 » ; déplacée, l'environnement lit un coût où il n'en lisait pas — l'épisode est laissé
    honnête à sa seule dose, compté sous son motif, sans arrêt ; les autres épisodes sont déplacés."""
    _, fmt = jouet

    def piege(t, k, i):
        if (t, k) != (0, 0):
            return None
        pred = "e a\n**COST** 5\n" if i == 2 else f"e{i}{k}\n"
        return f"ACTION: ADD\nTITLE: t{i}\nPROPOSAL: p{i}{k}\nCONTROLS: c{i}{k} a\nPREDICTION: {pred}"
    eps = _episodes(fmt, piege)
    d = la.fabriquer_condition(fmt, eps, TACHES, "PREDICTION", (1.0,), ENTROPIE_FICTIVE, REG, None, dose_recue=True)[1.0]
    e0 = d["episodes"][0]
    assert e0["laisse_honnete"] and e0["motif"] == iv.MOTIF_LECTURE and e0["actions"] == eps[0]["actions"]
    assert d["bilan"]["motifs_laisses_honnetes"][iv.MOTIF_LECTURE] == 1
    assert not any(e["laisse_honnete"] for e in d["episodes"][1:])


# --- m-5 (d) : seuils stricts — plafond égal et coupe à exactement 20 % n'arrêtent pas ------------------------------------

def test_compteur_egalite_passe_au_dessus_arrete():
    h = Horloge(0.0)
    c = la.CompteurDePlafond(18.0, 2.0, 0.0, horloge=h)
    h.t = 3600 * 9.0
    assert c.exiger_sous_plafond() == 18.0                 # cumul égal au plafond : passe (« au-dessus » strict)
    h.t = 3600 * 9.0 + 1
    with pytest.raises(la.ArretDePlafond):
        c.exiger_sous_plafond()


def test_ligne_1_plafond_atteint_exactement_passe(config_lue, constat, tmp_path):
    h, jeu = Horloge(0.0), _jeu_simule()

    def lent(*a, **k):
        h.t += 3600 * 9.0 / 16                              # 16 lots : cumul final exactement 18 USD
        return jeu(*a, **k)
    r = la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, _sorties(tmp_path),
                         la.CompteurDePlafond(18.0, 2.0, 0.0, horloge=h), constat, jouer_lot=lent)
    assert r["cumul_usd"] == 18.0 and r["episodes"] == 128


def _jeu_coupe(total):
    """Exactement `total` actions coupées sur la ligne, réparties en tête de chaque lot (16 par lot), le reste au dernier."""
    def jouer(modele, fmt, taches, reglages, g, guide, prefixe, chrono=None):
        t = taches[0]
        rang = int(t["identifiant"].split("-")[1])
        n = min(16, total - 16 * rang) if rang < 15 else total - 16 * 15
        eps = []
        for k in range(8):
            actions = [[5] * 400 if (k * 10 + s) < n else [5, 6, 0] for s in range(10)]
            eps.append({"episode": f"fabrication/{t['identifiant']}/e{k}", "tache": t, "k": k, "actions": actions,
                        "textes": ["x"] * 10})
        return eps
    return jouer


def test_coupe_a_exactement_20_pour_cent_n_arrete_pas(config_lue, constat, tmp_path):
    r = la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, _sorties(tmp_path),
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0)), constat, jouer_lot=_jeu_coupe(256))
    assert r["actions_coupees"] == 256 and r["part_coupees"] == 0.2
    d = _sorties(tmp_path, "s2")
    with pytest.raises(la.ArretCoupe, match="257"):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d,
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(0.0)), constat, jouer_lot=_jeu_coupe(257))
    assert len(list(d.iterdir())) == 16                     # la 257e est au dernier lot : tout est écrit


# --- m-6 : dose reçue sur demande, jamais sur les jumeaux ------------------------------------------------------------------

def test_dose_recue_explicite(jouet):
    _, fmt = jouet
    eps = _episodes(fmt)
    j = la.fabriquer_jumeaux_de_verification(fmt, eps, TACHES, ENTROPIE_FICTIVE, REG, None)    # 128 jumeaux
    assert len(j["episodes"]) == 128 and "dose_recue" not in j["bilan"]
    for champ, n in ((None, 128), ("CONTROLS", 127)):
        with pytest.raises(GardeArret, match="dose reçue"):
            la.fabriquer_condition(fmt, eps[:n], TACHES, champ, (1.0,), ENTROPIE_FICTIVE, REG, None, dose_recue=True)


# --- Essais ajoutés après la campagne de mutants (survivants de la première passe) ----------------------------------------

def test_ligne_1_plafond_deja_franchi_avant_le_premier_lot(config_lue, constat, tmp_path):
    """Relevé **avant** le premier lot : un compteur déjà au-dessus du plafond n'en joue aucun ; rien n'est écrit."""
    d, appels = _sorties(tmp_path), []
    with pytest.raises(la.ArretDePlafond):
        la.jouer_ligne_1(None, Fmt(), config_lue, _plan(), {}, None, d,
                         la.CompteurDePlafond(18.0, 1.38, 0.0, horloge=Horloge(3600 * 14.0)), constat,
                         jouer_lot=_jeu_espion(appels))
    assert appels == [] and not list(d.iterdir())


def test_perimetre_au_pluriel_refuse():
    """« lignes 1 … » au pluriel, même accompagné de la ligne jouée : refusé (un GO pour la seule ligne jouée)."""
    with pytest.raises(GardeArret, match="nomme aussi"):
        la.exiger_ligne_de_go("GO-2026-11-23-150", _registre(SAINE.replace(
            "ligne 1 du bras A", "ligne 1 du bras A ; lignes 1 et suivantes")), AUJOURD_HUI)


def test_constat_date_le_go_par_son_horloge(config_lue):
    """Le GO est daté par l'horloge du constat : passé son échéance (2026-11-30), le départ est refusé même avec un
    relevé du jour."""
    tard = datetime(2026, 12, 5, 9, 0, 0, tzinfo=timezone.utc)
    with pytest.raises(GardeArret, match="validité"):
        _constat(config_lue, maintenant=tard, tarifs=dict(TARIFS, date_utc="2026-12-05T08:00:00Z"))
