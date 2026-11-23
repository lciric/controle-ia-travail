"""Essais du programme de la ligne 1 de carte du bras A (`scripts/course_ligne_1_bras_a_v1.py`) et de sa liste blanche
(`scripts/liste_blanche_ligne_1_bras_a_v1.py`). Processeur seul ; aucune instance, aucun réseau, aucune clé.

Comme les essais du lanceur v7 : une configuration d'essai à entropie fictive n'a jamais de constat de départ (M-2) ;
la course simulée est donc jouée sous une configuration **déclarée réelle**, sur un **texte fictif**, dans un dossier
temporaire, avec le modèle jouet. Le dossier temporaire n'est rempli que **par la liste blanche** (modules calculés par
programme, données de la course) : la course de bout en bout y tourne dans un processus à part dont le chemin
d'import ne voit que ce dossier, ce qui éprouve aussi que la liste blanche suffit."""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import instrument_appariement_v4 as iv
from controle_ia.organismes_discrets import lanceur_bras_a_v7 as la
from controle_ia.scellement import sceller

DEPOT = Path(__file__).resolve().parents[1]
ENTROPIE_FICTIVE = 271828182845904523536028747135266249775     # fictive, déclarée telle dans le texte fictif
REF = json.loads((DEPOT / la.CHEMIN_CONFIGURATION_DE_REFERENCE).read_text(encoding="utf-8"))
COURSE = "scripts/course_ligne_1_bras_a_v1.py"
LISTE = "scripts/liste_blanche_ligne_1_bras_a_v1.py"


def _charger(relatif, nom):
    spec = importlib.util.spec_from_file_location(nom, DEPOT / relatif)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


co = _charger(COURSE, "course_ligne_1_bras_a_v1")
lb = _charger(LISTE, "liste_blanche_ligne_1_bras_a_v1")


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _texte_fictif(entropie: int) -> str:
    corps = {"Hypothèse": "h", "Prédiction chiffrée et signe attendu": "p", "Métrique": "m", "Seuil": "s",
             "Plan d'analyse": f"entropie racine : {entropie}", "Critères de lecture gelés": "c", "Liste d'arrêt": "l",
             "Contre-lecture": "brouillon " + "a" * 64 + " ; rapport " + "b" * 64}
    return "# Texte fictif des essais de la course de la ligne 1\n\n" + "".join(f"## {k}\n\n{v}\n\n" for k, v in corps.items())


def _poser(racine: Path, relatif: str) -> None:
    (racine / relatif).parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(DEPOT / relatif, racine / relatif)


NOM_CONFIGURATION = "prereg/configuration-essai-course-ligne-1.json"
NOM_PLAN = "plan-des-taches-essai.json"
MAINTENANT = datetime.now(timezone.utc).replace(microsecond=0)
INSTANT = MAINTENANT.strftime("%Y-%m-%dT%H:%M:%SZ")
REGISTRE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
            f"| GO-2026-11-23-150 | 2026-11-01 | calcul | bras A, ligne 1 de carte | 18 USD | 2099-12-31 | Lazar | essai |\n")
TARIFS = {"carte_usd_h": 1.1833, "stockage_usd_h": 0.05, "telechargement_usd_go": 0.05, "date_utc": INSTANT}


@pytest.fixture(scope="module")
def racine(tmp_path_factory):
    """Dossier posé par la liste blanche seule : modules calculés par programme, données de la course."""
    r = tmp_path_factory.mktemp("instance")
    modules = lb.modules_importes(DEPOT, [COURSE, la.CHEMIN_DU_LANCEUR])
    assert COURSE in modules and la.CHEMIN_DU_LANCEUR in modules
    assert not [x for x in modules if lb.est_cloisonne_ici(x)]
    for x in modules:
        _poser(r, x)
    for x in (la.CHEMIN_CONFIGURATION_DE_REFERENCE, REF["taches_distillation"]["chemin"], REF["taches_evaluation"]["chemin"]):
        _poser(r, x)
        _poser(r, x + ".sha256")
    t = r / la.CHEMIN_TEXTE_SCELLE
    t.write_text(_texte_fictif(ENTROPIE_FICTIVE), encoding="utf-8")
    sceller(t)
    c = {"lanceur": {"chemin": la.CHEMIN_DU_LANCEUR, "sha256": _sha(DEPOT / la.CHEMIN_DU_LANCEUR)},
         "texte": {"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": _sha(t)},
         "configuration_de_reference": {"chemin": la.CHEMIN_CONFIGURATION_DE_REFERENCE,
                                        "sha256": la.EMPREINTE_CONFIGURATION_DE_REFERENCE},
         "entropie": ENTROPIE_FICTIVE, "entropie_fictive": False, "reglages_instrument": dict(iv.OPTIONS_RETENUES),
         "ligne_1": {"plafond_usd": 18.0, "marge_de_credit_usd": 2.0}}
    (r / NOM_CONFIGURATION).write_text(json.dumps(c), encoding="utf-8")
    sceller(r / NOM_CONFIGURATION)
    config = la.lire_la_configuration(r / NOM_CONFIGURATION, r)
    plan = la.plan_des_taches(config)
    (r / NOM_PLAN).write_text(json.dumps({"configuration_du_lanceur": {"sha256": config["sha256"]},
                                          "fabrication": [x["identifiant"] for x in plan["fabrication"]],
                                          "verification": [x["identifiant"] for x in plan["verification"]],
                                          "ouvertes": plan["ouvertes"], "gardees": plan["gardees"]}), encoding="utf-8")
    sceller(r / NOM_PLAN)
    constat = la.constat_de_depart_ligne_1(config, go_id="GO-2026-11-23-150", texte_du_registre_go=REGISTRE,
                                           maintenant=MAINTENANT, credit_lu_usd=20.0, tarifs=TARIFS)
    (r / "constat.json").write_text(json.dumps(constat), encoding="utf-8")
    return r


def _args(racine: Path, dossier: str, **ecarts) -> list[str]:
    a = {"--racine": str(racine), "--configuration": str(racine / NOM_CONFIGURATION),
         "--lanceur-chemin": la.CHEMIN_DU_LANCEUR, "--lanceur-sha256": _sha(DEPOT / la.CHEMIN_DU_LANCEUR),
         "--constat": str(racine / "constat.json"), "--plan-scelle": str(racine / NOM_PLAN),
         "--creation-instance-utc": INSTANT, "--dossier": str(racine / dossier), "--commit": "0" * 40,
         "--guide": "aucun", "--mode": "jouet"}
    a.update(ecarts)
    return [x for k, v in a.items() if v is not None for x in (k, v)]


def _jouer_a_part(racine: Path, args: list[str]) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONPATH=str(racine / "src"), PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, str(racine / COURSE)] + args, cwd=racine, env=env, capture_output=True,
                          text=True, timeout=3000)


# --- De bout en bout, sur le modèle jouet, dans le dossier posé par la liste blanche ----------------------------------

LONG = os.environ.get("COURSE_LIGNE_1_ESSAI_LONG") == "1"


@pytest.mark.skipif(not LONG, reason="course entière sur le jouet (≈ 15 min) : COURSE_LIGNE_1_ESSAI_LONG=1 pour la jouer")
def test_course_de_bout_en_bout_sur_le_modele_jouet(racine):
    r = _jouer_a_part(racine, _args(racine, "sorties-1"))
    d = racine / "sorties-1"
    journal = (d / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")
    assert "REFUS" not in journal, journal + r.stderr
    manifeste = json.loads((d / co.NOM_DU_MANIFESTE_DE_LIGNE).read_text(encoding="utf-8"))
    assert manifeste["ligne"] == 1 and manifeste["commit"] == "0" * 40 and manifeste["depart"]["go"]["go"] == "GO-2026-11-23-150"
    assert len(manifeste["graines"]) == 269 and manifeste["resume"]["guide"] == {"identifiant": "aucun", "sha256": None}
    if r.returncode == 0:                                  # ligne jouée en entier
        assert manifeste["arret"] is None and manifeste["resume"]["episodes"] == 128
        assert len(la.lire_les_episodes_de_la_ligne_1(d / co.SOUS_DOSSIER_DES_EPISODES)) == 128
        assert manifeste["resume"]["secondes_par_episode"] > 0
    else:                                                  # arrêt pendant le jeu (coupe A14 du jouet) : dit, écrit
        assert r.returncode == 3 and manifeste["arret"] and "ARRÊT PENDANT LE JEU" in journal, journal + r.stderr
        assert any((d / co.SOUS_DOSSIER_DES_EPISODES).iterdir())
    # le versement se scelle sur ce dossier, puis la destruction passe (la fonction d'arrêt est simulée)
    sha = la.sceller_le_versement(d, manifeste)
    appels = []
    assert la.detruire_l_instance("123456", d, appels.append)["manifeste_du_versement_sha256"] == sha and appels == ["123456"]


def test_course_arretee_au_plafond_dans_le_dossier_de_la_liste_blanche(racine):
    """Toujours jouée (rapide) : constat et création datés de 12,97 h moins 20 s avant l'horloge, au tarif du constat
    (1,2333 USD par heure, plus 2 USD de téléchargement) : le plafond de 18 USD est franchi au plus tard après le
    premier lot ; l'arrêt est dit au journal et au manifeste, ce qui est joué reste écrit (code 3)."""
    ecoule = (18.0 - 2.0) / 1.2333 * 3600 - 20
    avant = datetime.fromtimestamp(MAINTENANT.timestamp() - ecoule, timezone.utc).replace(microsecond=0)
    instant = avant.strftime("%Y-%m-%dT%H:%M:%SZ")
    config = la.lire_la_configuration(racine / NOM_CONFIGURATION, racine)
    constat = la.constat_de_depart_ligne_1(config, go_id="GO-2026-11-23-150", texte_du_registre_go=REGISTRE,
                                           maintenant=avant, credit_lu_usd=20.0, tarifs=dict(TARIFS, date_utc=instant))
    (racine / "constat-ancien.json").write_text(json.dumps(constat), encoding="utf-8")
    r = _jouer_a_part(racine, _args(racine, "sorties-plafond", **{"--constat": str(racine / "constat-ancien.json"),
                                                                    "--creation-instance-utc": instant}))
    d = racine / "sorties-plafond"
    journal = (d / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")
    assert r.returncode == 3 and "ArretDePlafond" in journal, journal + r.stderr
    manifeste = json.loads((d / co.NOM_DU_MANIFESTE_DE_LIGNE).read_text(encoding="utf-8"))
    assert manifeste["arret"].startswith("ArretDePlafond") and manifeste["resume"]["partiel"] is True
    assert len(list((d / co.SOUS_DOSSIER_DES_EPISODES).iterdir())) <= 1
    sha = la.sceller_le_versement(d, manifeste)
    assert la.exiger_manifeste_du_versement_scelle(d) == sha


# --- Refus avant jeu : chacun écrit au journal, rien n'est joué (code 2) ----------------------------------------------

@pytest.mark.parametrize("ecart, motif", [
    ({"--lanceur-sha256": "0" * 64}, "empreinte sur disque"),
    ({"--lanceur-chemin": "src/controle_ia/organismes_discrets/lanceur_bras_a_v2.py"}, "empreinte sur disque|se nomme"),
    ({"--commit": "abc"}, "quarante"),
    ({"--creation-instance-utc": "2026-01-01T00:00:00Z"}, "antérieure au constat"),
    ({"--creation-instance-utc": "2099-01-01T00:00:00Z"}, "postérieure à l'horloge"),
    ({"--creation-instance-utc": "hier"}, "AAAA-MM-JJ"),
    ({"--mode": "reel"}, "seul le texte scellé"),
])
def test_refus_avant_jeu(racine, ecart, motif):
    nom = "refus-" + hashlib.sha256(json.dumps(ecart).encode()).hexdigest()[:8]
    code = _jouer_a_part(racine, _args(racine, nom, **ecart)).returncode
    journal = (racine / nom / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")
    assert code == 2 and "REFUS AVANT JEU" in journal
    assert re.search(motif, journal), journal
    assert not (racine / nom / co.SOUS_DOSSIER_DES_EPISODES).exists()


def test_constat_altere_refuse(racine):
    c = json.loads((racine / "constat.json").read_text(encoding="utf-8"))
    c["credit_lu_usd"] = 50.0                              # altération après coup : l'empreinte ne suit pas
    (racine / "constat-altere.json").write_text(json.dumps(c), encoding="utf-8")
    code = _jouer_a_part(racine, _args(racine, "refus-constat", **{"--constat": str(racine / "constat-altere.json")})).returncode
    assert code == 2 and "altéré" in (racine / "refus-constat" / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")


def test_plan_different_refuse(racine):
    p = json.loads((racine / NOM_PLAN).read_text(encoding="utf-8"))
    p["ouvertes"], p["gardees"] = p["gardees"], p["ouvertes"]
    (racine / "plan-autre.json").write_text(json.dumps(p), encoding="utf-8")
    sceller(racine / "plan-autre.json")
    code = _jouer_a_part(racine, _args(racine, "refus-plan", **{"--plan-scelle": str(racine / "plan-autre.json")})).returncode
    assert code == 2 and "ouvertes" in (racine / "refus-plan" / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")


def test_dossier_existant_refuse(racine):
    (racine / "deja").mkdir()
    assert _jouer_a_part(racine, _args(racine, "deja")).returncode == 2
    assert not any((racine / "deja").iterdir())           # rien n'y est écrit


def test_mode_jouet_refuse_sous_le_texte_reel(monkeypatch, racine):
    """En processus : le lanceur importé est celui du dépôt (même contenu) ; l'empreinte du texte réel est plantée."""
    monkeypatch.setattr(co, "charger_le_lanceur", lambda r, chemin, sha: la)
    monkeypatch.setattr(co, "EMPREINTE_TEXTE_REEL", _sha(racine / la.CHEMIN_TEXTE_SCELLE))
    code = co.main(_args(racine, "refus-jouet-reel"))
    assert code == 2 and "mode jouet sous le texte scellé réel" in (
        racine / "refus-jouet-reel" / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")


def test_guide_explicite(monkeypatch):
    assert co.charger_le_guide("aucun") == (None, None)
    with pytest.raises(GardeArret):
        co.charger_le_guide("autre")
    with pytest.raises(SystemExit):
        co._arguments(["--racine", "."])                   # --guide (et les autres) exigés, aucun défaut


# --- Compteur nourri du constat -----------------------------------------------------------------------------------

def test_compteur_du_constat(racine):
    config = la.lire_la_configuration(racine / NOM_CONFIGURATION, racine)
    constat = json.loads((racine / "constat.json").read_text(encoding="utf-8"))
    t0 = MAINTENANT.timestamp()
    c = co.compteur_du_constat(la, config, constat, MAINTENANT, horloge=lambda: t0 + 3600)
    assert c.plafond_usd == 18.0 and c.taux == pytest.approx(1.2333) and c.fixes == pytest.approx(2.0)
    assert c.cumul_usd() == pytest.approx(3.2333)
    la.exiger_constat_et_compteur(config, constat, c)
    with pytest.raises(GardeArret, match="positif"):
        co.compteur_du_constat(la, config, dict(constat, tarifs=dict(TARIFS, carte_usd_h=float("nan"))), MAINTENANT,
                               horloge=lambda: t0)


# --- Liste blanche ----------------------------------------------------------------------------------------------------

def test_liste_blanche_de_la_vraie_configuration():
    sortie = lb.liste_blanche(DEPOT, "prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json",
                              la.CHEMIN_DU_LANCEUR,
                              "docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json",
                              "aucun")
    assert COURSE in sortie["modules"] and "src/controle_ia/organismes_discrets/lanceur_bras_a_v2.py" in sortie["modules"]
    assert "prereg/T0.7-organismes-discrets-v-a-v2.md" in sortie["donnees"] and not sortie["manquants"]
    assert not any(lb.est_cloisonne_ici(x) for x in sortie["modules"] + sortie["donnees"])
    assert lb.liste_blanche(DEPOT, "prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json",
                            la.CHEMIN_DU_LANCEUR,
                            "docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json",
                            "H1-classification")["manquants"]


@pytest.mark.parametrize("chemin", ["bases/x.py", "src/controle_ia/sondes/x.py", "runs/a/b.json", "registres/go.md",
                                    "docs/sources/x/index.json", "src/controle_ia/organismes_discrets/autres_moniteurs_v11.py",
                                    "src/t07_x/a.py", "docs/notes/bras-a-sans-interne-v1/a.md", "a/consigne-privee-v1.md"])
def test_cloisonnement_de_la_liste_blanche(chemin):
    assert lb.est_cloisonne_ici(chemin)


def test_liste_blanche_refuse_un_chemin_cloisonne(monkeypatch):
    monkeypatch.setattr(lb, "modules_importes", lambda racine, depart: ["src/controle_ia/sondes/x.py"])
    with pytest.raises(lb.Refus, match="cloisonnés"):
        lb.liste_blanche(DEPOT, "prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v1.json",
                         la.CHEMIN_DU_LANCEUR,
                         "docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v1.json", "aucun")


def test_imports_dans_les_fonctions_et_relatifs():
    exiges, possibles = lb._imports("def f():\n    from ..a import b\n    import controle_ia.c\n",
                                    "controle_ia.x.y", False)
    assert "controle_ia.a" in exiges and "controle_ia.c" in exiges and "controle_ia.a.b" in possibles
