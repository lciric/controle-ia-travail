"""Essais du programme de la ligne 1 de carte du bras A, version 2 (`scripts/course_ligne_1_bras_a_v2.py`) et de sa
liste blanche, version 2 (`scripts/liste_blanche_ligne_1_bras_a_v2.py`). Processeur seul ; aucune instance, aucun
réseau, aucune clé. Rien n'est lu sous `docs/sources/` : le guide joué ici est un **guide fictif, déclaré tel** (son
texte le dit), posé dans un dossier temporaire sous `essai/guide-fictif-v1/`, et ses chemins et empreintes fictifs
sont **injectés par l'essai** à la place des constantes du lanceur v8 (en processus par `monkeypatch`, dans un
processus à part par un petit programme d'amorce hors du dossier posé, qui remplace les constantes en mémoire avant de
jouer la course ; le fichier du lanceur sur disque, et donc son empreinte, ne changent pas).

Comme pour la version 1 : la course simulée est jouée sous une configuration **déclarée réelle**, sur un **texte
fictif**, dans un dossier temporaire rempli **par la liste blanche** (modules calculés par programme, données), avec le
modèle jouet ; la course de bout en bout tourne dans un processus à part dont le chemin d'import ne voit que ce dossier.
Ajouts de la contre-lecture de la préparation v1 (`83ec8586…`) : D1 (exception hors `GardeArret`, avant et pendant le
jeu), D2 (déterminisme versé au manifeste), m3 (compteur relevé autour du chargement), m4 (coupe à 20 % côté course),
m5 (plus d'argument `--guide`, ni dans la course ni dans la liste blanche)."""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets import instrument_appariement_v4 as iv
from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la
from controle_ia.scellement import sceller

DEPOT = Path(__file__).resolve().parents[1]
ENTROPIE_FICTIVE = 271828182845904523536028747135266249775     # fictive, déclarée telle dans le texte fictif
REF = json.loads((DEPOT / la.CHEMIN_CONFIGURATION_DE_REFERENCE).read_text(encoding="utf-8"))
COURSE = "scripts/course_ligne_1_bras_a_v2.py"
LISTE = "scripts/liste_blanche_ligne_1_bras_a_v2.py"
CONFIGURATION_REELLE = "prereg/T0.7-organismes-discrets-v-a-v2-config-lanceur-ligne-1-v2.json"
PLAN_REEL = "docs/notes/relance-organismes-discrets-v1/etape-a-ligne-1-v1/plan-des-taches-v2.json"


def _charger(relatif, nom):
    spec = importlib.util.spec_from_file_location(nom, DEPOT / relatif)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


co = _charger(COURSE, "course_ligne_1_bras_a_v2")
lb = _charger(LISTE, "liste_blanche_ligne_1_bras_a_v2")


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


# --- Guide fictif, déclaré tel ----------------------------------------------------------------------------------------

DOSSIER_GUIDE_FICTIF = "essai/guide-fictif-v1"
TEXTE_GUIDE_FICTIF = ("GUIDE FICTIF D'ESSAI — ce texte n'est pas le guide H1-classification ; il ne sert qu'aux essais "
                      "de la course de la ligne 1 sur le modèle jouet.\n")


def poser_guide_fictif(racine: Path, dossier: str = DOSSIER_GUIDE_FICTIF, texte: str = TEXTE_GUIDE_FICTIF) -> dict:
    """Écrit et scelle l'invite et l'index fictifs ; rend la clé `guide` qui les nomme (empreintes fictives)."""
    d = racine / dossier
    (d / "invites").mkdir(parents=True, exist_ok=True)
    f = d / "invites" / "H1-classification.txt"
    f.write_text(texte, encoding="utf-8")
    sceller(f)
    index = d / "index.json"
    index.write_text(json.dumps({"objet": "index fictif d'essai",
                                 "invites": [{"id": "H1-classification", "fichier": "invites/H1-classification.txt",
                                              "sha256": _sha(f)}]}), encoding="utf-8")
    sceller(index)
    return {"identifiant": "H1-classification", "fichier": f"{dossier}/invites/H1-classification.txt",
            "sha256": _sha(f), "index": f"{dossier}/index.json", "index_sha256": _sha(index)}


def constantes_fictives(guide: dict) -> dict:
    return {"CHEMIN_DU_GUIDE": guide["fichier"], "EMPREINTE_DU_GUIDE": guide["sha256"],
            "CHEMIN_DE_L_INDEX_DU_GUIDE": guide["index"], "EMPREINTE_DE_L_INDEX_DU_GUIDE": guide["index_sha256"]}


GUIDE_REEL = {"identifiant": "H1-classification", "fichier": la.CHEMIN_DU_GUIDE, "sha256": la.EMPREINTE_DU_GUIDE,
              "index": la.CHEMIN_DE_L_INDEX_DU_GUIDE, "index_sha256": la.EMPREINTE_DE_L_INDEX_DU_GUIDE}

NOM_CONFIGURATION = "prereg/configuration-essai-course-ligne-1-v2.json"
NOM_PLAN = "plan-des-taches-essai-v2.json"
MAINTENANT = datetime.now(timezone.utc).replace(microsecond=0)
INSTANT = MAINTENANT.strftime("%Y-%m-%dT%H:%M:%SZ")
REGISTRE = ("| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
            f"| GO-2026-11-23-150 | 2026-11-01 | calcul | bras A, ligne 1 de carte | 18 USD | 2099-12-31 | Lazar | essai |\n")
TARIFS = {"carte_usd_h": 1.1833, "stockage_usd_h": 0.05, "telechargement_usd_go": 0.05, "date_utc": INSTANT}
ETAT: dict = {}


def _configuration_et_plan(r: Path, guide: dict, nom_conf: str, nom_plan: str) -> tuple[Path, Path]:
    t = r / la.CHEMIN_TEXTE_SCELLE
    c = {"lanceur": {"chemin": la.CHEMIN_DU_LANCEUR, "sha256": _sha(DEPOT / la.CHEMIN_DU_LANCEUR)},
         "texte": {"chemin": la.CHEMIN_TEXTE_SCELLE, "sha256": _sha(t)},
         "configuration_de_reference": {"chemin": la.CHEMIN_CONFIGURATION_DE_REFERENCE,
                                        "sha256": la.EMPREINTE_CONFIGURATION_DE_REFERENCE},
         "entropie": ENTROPIE_FICTIVE, "entropie_fictive": False, "reglages_instrument": dict(iv.OPTIONS_RETENUES),
         "ligne_1": {"plafond_usd": 18.0, "marge_de_credit_usd": 2.0}, "guide": guide}
    (r / nom_conf).write_text(json.dumps(c), encoding="utf-8")
    sceller(r / nom_conf)
    config = la.lire_la_configuration(r / nom_conf, r)
    plan = la.plan_des_taches(config)
    (r / nom_plan).write_text(json.dumps({"configuration_du_lanceur": {"sha256": config["sha256"]},
                                          "fabrication": [x["identifiant"] for x in plan["fabrication"]],
                                          "verification": [x["identifiant"] for x in plan["verification"]],
                                          "ouvertes": plan["ouvertes"], "gardees": plan["gardees"]}), encoding="utf-8")
    sceller(r / nom_plan)
    return r / nom_conf, r / nom_plan


@pytest.fixture(scope="module")
def racine(tmp_path_factory):
    """Dossier posé par la liste blanche seule (modules, données), plus le guide fictif ; constantes du guide du
    lanceur remplacées, pour tout ce module d'essais, par les chemins et empreintes fictifs."""
    r = tmp_path_factory.mktemp("instance")
    modules = lb.modules_importes(DEPOT, [COURSE, la.CHEMIN_DU_LANCEUR])
    assert COURSE in modules and la.CHEMIN_DU_LANCEUR in modules
    assert "src/controle_ia/environnements/invites.py" in modules and "src/controle_ia/harnais/modeles.py" in modules
    assert not [x for x in modules if lb.est_cloisonne_ici(x)]
    for x in modules:
        _poser(r, x)
    for x in (la.CHEMIN_CONFIGURATION_DE_REFERENCE, REF["taches_distillation"]["chemin"], REF["taches_evaluation"]["chemin"]):
        _poser(r, x)
        _poser(r, x + ".sha256")
    t = r / la.CHEMIN_TEXTE_SCELLE
    t.write_text(_texte_fictif(ENTROPIE_FICTIVE), encoding="utf-8")
    sceller(t)
    guide = poser_guide_fictif(r)
    mp = pytest.MonkeyPatch()
    for k, v in constantes_fictives(guide).items():
        mp.setattr(la, k, v)
    conf, plan = _configuration_et_plan(r, guide, NOM_CONFIGURATION, NOM_PLAN)
    config = la.lire_la_configuration(conf, r)
    constat = la.constat_de_depart_ligne_1(config, go_id="GO-2026-11-23-150", texte_du_registre_go=REGISTRE,
                                           maintenant=MAINTENANT, credit_lu_usd=20.0, tarifs=TARIFS)
    (r / "constat.json").write_text(json.dumps(constat), encoding="utf-8")
    amorce = tmp_path_factory.mktemp("amorce") / "amorce_guide_fictif.py"
    amorce.write_text("import json, runpy, sys\n"
                      "from controle_ia.organismes_discrets import lanceur_bras_a_v8 as la\n"
                      "for k, v in json.loads(sys.argv[1]).items():\n"
                      "    setattr(la, k, v)          # guide FICTIF, injecté par l'essai\n"
                      "course = sys.argv[2]\n"
                      "sys.argv = [course] + sys.argv[3:]\n"
                      "runpy.run_path(course, run_name='__main__')\n", encoding="utf-8")
    ETAT.update(guide=guide, amorce=amorce)
    yield r
    mp.undo()


def _args(racine: Path, dossier: str, **ecarts) -> list[str]:
    a = {"--racine": str(racine), "--configuration": str(racine / NOM_CONFIGURATION),
         "--lanceur-chemin": la.CHEMIN_DU_LANCEUR, "--lanceur-sha256": _sha(DEPOT / la.CHEMIN_DU_LANCEUR),
         "--constat": str(racine / "constat.json"), "--plan-scelle": str(racine / NOM_PLAN),
         "--creation-instance-utc": INSTANT, "--dossier": str(racine / dossier), "--commit": "0" * 40,
         "--mode": "jouet"}
    a.update(ecarts)
    return [x for k, v in a.items() if v is not None for x in (k, v)]


def _jouer_a_part(racine: Path, args: list[str], guide_fictif: bool = True,
                  delai_s: int = 3000) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONPATH=str(racine / "src"), PYTHONDONTWRITEBYTECODE="1")
    if guide_fictif:
        commande = [sys.executable, str(ETAT["amorce"]), json.dumps(constantes_fictives(ETAT["guide"])),
                    str(racine / COURSE)] + args
    else:
        commande = [sys.executable, str(racine / COURSE)] + args
    return subprocess.run(commande, cwd=racine, env=env, capture_output=True, text=True, timeout=delai_s)


def _journal(racine: Path, nom: str) -> str:
    return (racine / nom / co.NOM_DU_JOURNAL).read_text(encoding="utf-8")


# --- De bout en bout, sur le modèle jouet, avec le guide fictif ----------------------------------------------------------

LONG = os.environ.get("COURSE_LIGNE_1_ESSAI_LONG") == "1"


@pytest.mark.skipif(not LONG, reason="course entière sur le jouet : COURSE_LIGNE_1_ESSAI_LONG=1 pour la jouer")
def test_course_de_bout_en_bout_sur_le_modele_jouet_avec_un_guide_fictif(racine):
    debut = time.time()
    # un fil (réglage du déterminisme) : ≈ 3 min par lot de huit sur ce processeur, ≈ 50 min en tout ; délai 2 h
    r = _jouer_a_part(racine, _args(racine, "sorties-1"), delai_s=7200)
    duree = time.time() - debut
    d = racine / "sorties-1"
    journal = _journal(racine, "sorties-1")
    assert "REFUS" not in journal, journal + r.stderr
    assert "octets vérifiés, guide chargé" in journal and "FIN : code" in journal
    manifeste = json.loads((d / co.NOM_DU_MANIFESTE_DE_LIGNE).read_text(encoding="utf-8"))
    assert manifeste["ligne"] == 1 and manifeste["commit"] == "0" * 40 and len(manifeste["graines"]) == 269
    g = manifeste["resume"]["guide"]
    assert g["fichier"].startswith(DOSSIER_GUIDE_FICTIF) and g["sha256"] == g["sha256_charge"] == ETAT["guide"]["sha256"]
    assert manifeste["resume"]["determinisme"]["appareil"] == "cpu"
    assert manifeste["resume"]["determinisme"]["relus"]["algorithmes_deterministes"] is True
    episodes = la.lire_les_episodes_de_la_ligne_1(d / co.SOUS_DOSSIER_DES_EPISODES)
    print(f"\nREJEU JOUET AVEC GUIDE FICTIF : code {r.returncode}, durée {duree:.0f} s, {len(episodes)} épisodes, "
          f"arrêt {manifeste['arret']!r}")
    if r.returncode == 0:
        assert manifeste["arret"] is None and manifeste["resume"]["episodes"] == 128 and len(episodes) == 128
    else:                                                  # arrêt pendant le jeu (coupe A14 du jouet) : dit, écrit
        assert r.returncode == 3 and manifeste["arret"] and "ARRÊT PENDANT LE JEU" in journal, journal + r.stderr
    sha = la.sceller_le_versement(d, manifeste)
    appels = []
    assert la.detruire_l_instance("123456", d, appels.append)["manifeste_du_versement_sha256"] == sha and appels == ["123456"]


def test_course_arretee_au_plafond_avec_le_guide_fictif(racine):
    """Toujours jouée (rapide) : création datée de 12,97 h moins 20 s avant l'horloge ; le plafond est franchi au
    relevé qui suit le chargement (m3) ou au premier lot ; le manifeste porte le guide et le déterminisme (D2)."""
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
    journal = _journal(racine, "sorties-plafond")
    assert "ArretDePlafond" in journal and "FIN : code" in journal, journal + r.stderr
    assert "compteur avant le chargement du modèle" in journal and "déterminisme réglé (cpu, 1 fil(s))" in journal
    if r.returncode == 2:                                  # franchi au relevé d'après le chargement (m3)
        assert "REFUS AVANT JEU" in journal and not (d / co.SOUS_DOSSIER_DES_EPISODES).exists()
        return
    assert r.returncode == 3, journal + r.stderr
    manifeste = json.loads((d / co.NOM_DU_MANIFESTE_DE_LIGNE).read_text(encoding="utf-8"))
    assert manifeste["arret"].startswith("ArretDePlafond") and manifeste["resume"]["partiel"] is True
    assert manifeste["resume"]["guide"]["sha256_charge"] == ETAT["guide"]["sha256"]
    assert manifeste["resume"]["determinisme"]["appareil"] == "cpu" and manifeste["resume"]["determinisme"]["deterministe"]
    sha = la.sceller_le_versement(d, manifeste)
    assert la.exiger_manifeste_du_versement_scelle(d) == sha


# --- Refus avant jeu : chacun écrit au journal avec « FIN », rien n'est joué (code 2) --------------------------------

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
    journal = _journal(racine, nom)
    assert code == 2 and "REFUS AVANT JEU" in journal and "FIN : code 2" in journal
    assert re.search(motif, journal), journal
    assert not (racine / nom / co.SOUS_DOSSIER_DES_EPISODES).exists()


def test_guide_reel_absent_refuse_avant_jeu(racine):
    """Sans injection : la configuration nomme le vrai guide (constantes du lanceur v8), absent de ce dossier : refus
    par la vérification des octets, avant le chargement du modèle, code 2."""
    with pytest.MonkeyPatch.context() as mp:
        for k, v in constantes_fictives(GUIDE_REEL).items():
            mp.setattr(la, k, v)
        conf, plan = _configuration_et_plan(racine, GUIDE_REEL, "prereg/configuration-essai-guide-reel.json",
                                            "plan-essai-guide-reel.json")
        config = la.lire_la_configuration(conf, racine)
        constat = la.constat_de_depart_ligne_1(config, go_id="GO-2026-11-23-150", texte_du_registre_go=REGISTRE,
                                               maintenant=MAINTENANT, credit_lu_usd=20.0, tarifs=TARIFS)
    (racine / "constat-guide-reel.json").write_text(json.dumps(constat), encoding="utf-8")
    r = _jouer_a_part(racine, _args(racine, "refus-guide-reel", **{"--configuration": str(conf),
                                                                     "--plan-scelle": str(plan),
                                                                     "--constat": str(racine / "constat-guide-reel.json")}),
                      guide_fictif=False)
    journal = _journal(racine, "refus-guide-reel")
    assert r.returncode == 2 and "REFUS AVANT JEU" in journal and "fichier du guide" in journal, journal + r.stderr
    assert "modèle chargé" not in journal and "déterminisme réglé" not in journal


def test_guide_fictif_sans_injection_refuse(racine):
    """La configuration d'essai nomme le guide fictif ; joué sans injection, le lanceur v8 (constantes réelles) refuse
    la configuration : un guide autre que celui inscrit ne passe jamais."""
    r = _jouer_a_part(racine, _args(racine, "refus-sans-injection"), guide_fictif=False)
    journal = _journal(racine, "refus-sans-injection")
    assert r.returncode == 2 and "`guide.fichier`" in journal, journal + r.stderr


def test_dossier_existant_refuse(racine):
    (racine / "deja").mkdir()
    assert _jouer_a_part(racine, _args(racine, "deja")).returncode == 2
    assert not any((racine / "deja").iterdir())


def test_argument_guide_n_existe_plus():
    """m5 et consigne : le guide vient de la configuration ; `--guide` est refusé par la course et par la liste."""
    with pytest.raises(SystemExit):
        co._arguments(_args(Path("."), "x") + ["--guide", "aucun"])
    with pytest.raises(SystemExit):
        lb.main(["--configuration", CONFIGURATION_REELLE, "--lanceur-chemin", la.CHEMIN_DU_LANCEUR,
                 "--plan-scelle", PLAN_REEL, "--guide", "aucun"])


# --- Chargement du guide : cas sain et artefacts, sur des fichiers fictifs en dossier temporaire ------------------------

@pytest.fixture
def guide_temporaire(tmp_path, monkeypatch):
    g = poser_guide_fictif(tmp_path)
    for k, v in constantes_fictives(g).items():
        monkeypatch.setattr(la, k, v)
    return tmp_path, g


def test_charger_le_guide_sain(guide_temporaire):
    r, g = guide_temporaire
    texte, sha, guide = co.charger_le_guide(la, {"guide": g}, r)
    assert texte == TEXTE_GUIDE_FICTIF and sha == g["sha256"] and guide == g


def test_charger_le_guide_octets_alteres(guide_temporaire):
    r, g = guide_temporaire
    (r / g["fichier"]).write_text(TEXTE_GUIDE_FICTIF + "x", encoding="utf-8")
    with pytest.raises(GardeArret, match="fichier du guide .* empreinte sur disque"):
        co.charger_le_guide(la, {"guide": g}, r)


def test_charger_le_guide_index_altere(guide_temporaire):
    r, g = guide_temporaire
    (r / g["index"]).write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="index du guide"):
        co.charger_le_guide(la, {"guide": g}, r)


def test_charger_le_guide_compagnon_absent(guide_temporaire):
    r, g = guide_temporaire
    (r / (g["fichier"] + ".sha256")).unlink()
    with pytest.raises(GardeArret, match="compagnon"):
        co.charger_le_guide(la, {"guide": g}, r)


def test_charger_le_guide_index_qui_nomme_un_autre_fichier(tmp_path, monkeypatch):
    g = poser_guide_fictif(tmp_path)
    autre = tmp_path / DOSSIER_GUIDE_FICTIF / "invites" / "autre.txt"
    autre.write_text(TEXTE_GUIDE_FICTIF, encoding="utf-8")
    sceller(autre)
    index = tmp_path / g["index"]
    index.write_text(json.dumps({"invites": [{"id": "H1-classification", "fichier": "invites/autre.txt",
                                              "sha256": g["sha256"]}]}), encoding="utf-8")
    (tmp_path / (g["index"] + ".sha256")).unlink()
    sceller(index)
    g = dict(g, index_sha256=_sha(index))
    for k, v in constantes_fictives(g).items():
        monkeypatch.setattr(la, k, v)
    with pytest.raises(GardeArret, match="l'index nomme"):
        co.charger_le_guide(la, {"guide": g}, tmp_path)


def test_charger_le_guide_lien_symbolique_refuse(guide_temporaire):
    r, g = guide_temporaire
    f = r / g["fichier"]
    vrai = r / "ailleurs.txt"
    f.rename(vrai)
    f.symlink_to(vrai)
    with pytest.raises(GardeArret, match="lien symbolique"):
        co.charger_le_guide(la, {"guide": g}, r)


# --- D1, m4 : en processus, modèle et jeu remplacés --------------------------------------------------------------------

class _FormatFictif:
    fins = (0,)


def _sans_determinisme(fils, appareil):
    return {"deterministe": True, "fils": fils, "appareil": appareil, "torch": "essai"}


@pytest.fixture
def en_processus(monkeypatch, racine):
    monkeypatch.setattr(co, "charger_le_lanceur", lambda r, chemin, sha: la)
    monkeypatch.setattr(co, "regler_le_determinisme", _sans_determinisme)   # l'état global de torch reste intact
    return racine


def test_exception_avant_jeu_dite_et_code_2(monkeypatch, en_processus):
    """D1 : une `OSError` du chargement du modèle (cache absent, mémoire, pilote) : refus dit, trace, « FIN », code 2."""
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2

    def panne(*a, **k):
        raise OSError("cache du modèle absent (essai)")
    monkeypatch.setattr(l2, "charger_modele_et_format", panne)
    code = co.main(_args(en_processus, "d1-avant"))
    journal = _journal(en_processus, "d1-avant")
    assert code == 2 and "REFUS AVANT JEU (exception) : OSError" in journal and "Traceback" in journal
    assert "FIN : code 2" in journal and not (en_processus / "d1-avant" / co.SOUS_DOSSIER_DES_EPISODES).exists()


def test_exception_pendant_le_jeu_dite_et_code_3(monkeypatch, en_processus):
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
    monkeypatch.setattr(l2, "charger_modele_et_format", lambda *a, **k: (object(), _FormatFictif()))

    def panne(*a, **k):
        raise RuntimeError("mémoire de la carte épuisée (essai)")
    monkeypatch.setattr(la, "jouer_ligne_1", panne)
    code = co.main(_args(en_processus, "d1-pendant"))
    journal = _journal(en_processus, "d1-pendant")
    assert code == 3 and "ARRÊT PENDANT LE JEU (exception) : RuntimeError" in journal and "FIN : code 3" in journal
    m = json.loads((en_processus / "d1-pendant" / co.NOM_DU_MANIFESTE_DE_LIGNE).read_text(encoding="utf-8"))
    assert m["arret"].startswith("RuntimeError") and m["resume"]["partiel"] is True
    assert m["resume"]["determinisme"] == _sans_determinisme(1, "cpu")


def test_coupe_a_20_pour_cent_cote_course(monkeypatch, en_processus):
    """m4 : chaque action coupée à 400 jetons (aucun jeton de fin) : 80 coupées par lot ; au quatrième lot, 320 > 256
    (20 % de 1 280) : `ArretCoupe`, code 3, quatre lots écrits, manifeste partiel. Le guide passé est le guide fictif."""
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
    monkeypatch.setattr(l2, "charger_modele_et_format", lambda *a, **k: (object(), _FormatFictif()))
    vus = []

    def jouer(modele, fmt, taches, reglages, g, guide, prefixe, chrono=None):
        vus.append(guide)
        t = taches[0]["identifiant"]
        return [{"episode": f"fabrication/{t}/e{k}", "k": k, "actions": [[1] * 400] * 10, "textes": [""] * 10}
                for k in range(8)]
    monkeypatch.setattr(co, "jeu_du_modele_jouet", lambda: jouer)
    code = co.main(_args(en_processus, "m4-coupe"))
    d = en_processus / "m4-coupe"
    journal = _journal(en_processus, "m4-coupe")
    assert code == 3 and "ArretCoupe" in journal and "FIN : code 3" in journal
    assert len(list((d / co.SOUS_DOSSIER_DES_EPISODES).iterdir())) == 4 and vus == [TEXTE_GUIDE_FICTIF] * 4
    m = json.loads((d / co.NOM_DU_MANIFESTE_DE_LIGNE).read_text(encoding="utf-8"))
    assert m["arret"].startswith("ArretCoupe") and m["resume"]["partiel"] is True


def test_compteur_releve_avant_et_apres_le_chargement(monkeypatch, en_processus):
    """m3 : le compteur est gardé juste avant le chargement du modèle ; un plafond franchi là refuse avant tout jeu."""
    from controle_ia.organismes_discrets import lanceur_bras_a_v2 as l2
    charges = []
    monkeypatch.setattr(l2, "charger_modele_et_format", lambda *a, **k: charges.append(1) or (object(), _FormatFictif()))
    monkeypatch.setattr(la.CompteurDePlafond, "exiger_sous_plafond",
                        lambda self: (_ for _ in ()).throw(la.ArretDePlafond("plafond (essai)")))
    code = co.main(_args(en_processus, "m3-avant"))
    assert code == 2 and charges == [] and "ArretDePlafond" in _journal(en_processus, "m3-avant")


# --- D2 : déterminisme ---------------------------------------------------------------------------------------------------

def test_determinisme_sur_carte_absente_refuse():
    torch = pytest.importorskip("torch")
    if torch.cuda.is_available():
        pytest.skip("carte présente : l'essai du refus n'a pas lieu d'être")
    with pytest.raises(GardeArret, match="indisponible"):
        co.regler_le_determinisme(1, "cuda")


# --- Liste blanche v2 -----------------------------------------------------------------------------------------------------

def test_liste_blanche_de_la_vraie_configuration():
    sortie = lb.liste_blanche(DEPOT, CONFIGURATION_REELLE, la.CHEMIN_DU_LANCEUR, PLAN_REEL)
    assert COURSE in sortie["modules"] and la.CHEMIN_DU_LANCEUR in sortie["modules"]
    assert "src/controle_ia/environnements/invites.py" in sortie["modules"]
    assert CONFIGURATION_REELLE in sortie["donnees"] and PLAN_REEL in sortie["donnees"] and not sortie["manquants"]
    assert not any(lb.est_cloisonne_ici(x) for x in sortie["modules"] + sortie["donnees"])
    assert [x["chemin"] for x in sortie["guide"]] == [GUIDE_REEL["fichier"], GUIDE_REEL["fichier"] + ".sha256",
                                                      GUIDE_REEL["index"], GUIDE_REEL["index"] + ".sha256"]
    assert sortie["guide"][0]["sha256_attendu"] == GUIDE_REEL["sha256"] == "69d50fb972f3255c94430205ab09c4f21054185d7def25b061c7255d71cc5540"
    assert sortie["guide"][2]["sha256_attendu"] == GUIDE_REEL["index_sha256"] == "adb4b8bca7788baf2c4714df96dcdcc2c5043e8f1943542d0fbe1863491ae2d9"
    assert all(x["lu_par_ce_programme"] is False for x in sortie["guide"])
    assert sortie["nombre"] == len(sortie["modules"]) + len(sortie["donnees"]) + 4


def test_liste_blanche_ne_touche_pas_au_guide(monkeypatch):
    """Aucun accès disque sous `docs/sources/` pendant le calcul de la liste (ouverture, lecture, existence)."""
    touches = []
    for nom in ("read_text", "read_bytes", "is_file", "exists", "open", "stat"):
        orig = getattr(Path, nom)

        def espion(self, *a, _orig=orig, **k):
            if "docs/sources" in self.as_posix():
                touches.append(self.as_posix())
            return _orig(self, *a, **k)
        monkeypatch.setattr(Path, nom, espion)
    lb.liste_blanche(DEPOT, CONFIGURATION_REELLE, la.CHEMIN_DU_LANCEUR, PLAN_REEL)
    assert touches == []


def test_liste_blanche_constantes_egales_au_lanceur():
    """GUIDE_REEL est lu des constantes du lanceur à l'import de ce module, avant toute injection du guide fictif."""
    assert lb.GUIDE_IDENTIFIANT == la.IDENTIFIANT_DU_GUIDE == GUIDE_REEL["identifiant"]
    assert lb.GUIDE_FICHIERS == ((GUIDE_REEL["fichier"], GUIDE_REEL["sha256"]),
                                 (GUIDE_REEL["index"], GUIDE_REEL["index_sha256"]))
    assert lb.LANCEUR_ATTENDU == la.CHEMIN_DU_LANCEUR and lb.PROGRAMME_DE_LA_COURSE == COURSE


def test_liste_blanche_refuse_un_autre_lanceur():
    with pytest.raises(lb.Refus, match="lanceur"):
        lb.liste_blanche(DEPOT, CONFIGURATION_REELLE, "src/controle_ia/organismes_discrets/lanceur_bras_a_v7.py",
                         PLAN_REEL)


def test_liste_blanche_refuse_un_autre_guide():
    with pytest.raises(lb.Refus, match="guide"):
        lb.fichiers_du_guide({"guide": dict(GUIDE_REEL, sha256="0" * 64)})
    with pytest.raises(lb.Refus, match="guide"):
        lb.fichiers_du_guide({})


def test_liste_blanche_refuse_un_chemin_cloisonne(monkeypatch):
    monkeypatch.setattr(lb, "modules_importes", lambda racine, depart: ["src/controle_ia/sondes/x.py"])
    with pytest.raises(lb.Refus, match="cloisonnés"):
        lb.liste_blanche(DEPOT, CONFIGURATION_REELLE, la.CHEMIN_DU_LANCEUR, PLAN_REEL)


@pytest.mark.parametrize("chemin", ["bases/x.py", "src/controle_ia/sondes/x.py", "runs/a/b.json", "registres/go.md",
                                    "docs/sources/x/index.json", "src/controle_ia/organismes_discrets/autres_moniteurs_v11.py",
                                    "src/t07_x/a.py", "docs/notes/bras-a-sans-interne-v1/a.md", "a/consigne-privee-v1.md"])
def test_cloisonnement_de_la_liste_blanche(chemin):
    assert lb.est_cloisonne_ici(chemin)
