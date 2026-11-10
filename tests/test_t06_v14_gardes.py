"""Chaîne v14 de T0.6, gardes en Python (préparée, non adoptée : option (c) de Lazar, R-2079) : `session_v13` (ligne de GO de la course lue dans la configuration et au
registre, plafond de la configuration borné par celui de la ligne, calendrier vérifié contre la ligne, GO de la course lu dans la configuration citée), `configuration_v7`
(toute configuration validée contre le registre, aucun identifiant en dur), `lanceur_v7` (copie du v6 ; course ou épreuve reçue de l'amorce par `--epreuve`), la
configuration de 7b v2 (brouillon 1) et la ligne `GO-2026-11-10-01` recopiée telle quelle du registre de `main` (lecture seule, R-2077).
Cas sain et artefact (R5) pour chaque garde neuve : GO de la configuration ≠ GO reçu, ligne absente, échue, révoquée, plafond de la configuration > plafond de la ligne,
calendrier au-delà de l'échéance de la ligne, ancienne valeur GO-2026-11-02-28 absente du code v14. Aucun réseau, aucun appel à Vast ; dates relatives au jour de l'essai,
sauf pour la ligne réelle de `main`, éprouvée à jours explicites (16, 22, 23 et 24 novembre 2026)."""
from __future__ import annotations

import ast
import contextlib
import difflib
import io
import json
import re
import subprocess
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.scellement import sceller, verifier
from controle_ia.t06 import configuration_v6 as cf6
from controle_ia.t06 import configuration_v7 as cf7
from controle_ia.t06 import lanceur_v6 as la6
from controle_ia.t06 import lanceur_v7 as la7
from controle_ia.t06 import session_v12 as s12
from controle_ia.t06 import session_v13 as s13
from controle_ia.t06.lanceur import empreinte_config
from controle_ia.t06.session import GardeSession

RACINE = Path(__file__).resolve().parents[1]
T06 = RACINE / "src" / "controle_ia" / "t06"
NOTES14 = RACINE / "docs" / "notes" / "g0-deux-semaines-v1" / "t06-chaine-v14"
CONFIG_7B_V1 = RACINE / "prereg" / "T0.6-organismes-config-7b-v1.json"
CONFIG_7B_V2 = NOTES14 / "config-t06-7b-v2-brouillon1.json"
ANCIEN = "GO-" + "2026-11-02-28"          # écrit en deux morceaux : ce fichier d'essais cherche la valeur dans le code v14, il ne doit pas la porter lui-même en un seul bloc
NEUF_MAIN = "GO-2026-11-10-01"
COURSE = "GO-2099-03-03-01"        # ligne de course à dates relatives (calcul, 200 USD avec commentaire, comme la ligne réelle)
PETITE = "GO-2099-03-03-02"        # ligne de calcul à 150 USD : un plafond de configuration de 200 la dépasse
DECISION = "GO-2099-03-03-03"      # ligne de type « décision »
ECHUE = "GO-2099-03-03-04"         # ligne de calcul échue hier
REVOQUEE = "GO-2099-03-03-05"      # ligne révoquée par GO-2099-03-03-06
ABSENTE = "GO-2099-03-03-09"
ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"
LIGNE_MAIN = "| GO-2026-11-10-01 | 2026-11-10 | calcul | **Prolongation de GO-2026-11-02-28 (T0.6, course de confirmation 7b, et T0.7 sur la même machine) jusqu'au 2026-11-23**, périmètre et conditions inchangés (préenregistrements de T0.6 et T0.7 contre-lus, scellés, committés et poussés avant la course ; instance H200 ou A100 chez Vast.ai ; aucun budget de temps qui coupe une étape ; sortie scellée avant lecture ; verdict par lecteur neuf) ; **non cumulé** : dépense totale sous GO-2026-11-02-28 et sous cette ligne ≤ 200 USD. Ligne neuve, parce qu'une seconde ligne au même identifiant ne peut pas dépasser l'échéance d'origine (R-389, garde de calcul) ; la chaîne gelée v13 de T0.6 ne lit en mode course que GO-2026-11-02-28 (R-2077) | 200 USD (plafond de GO-2026-11-02-28, non cumulé) | 2026-11-23 | Lazar | R-2077 ; mot de Lazar dans la session mère `session_01QPDgKgACWyCkCN8HjqwNXy`, reçu vers 06:04 UTC le 10 novembre 2026 : « (a) pour les deux GO, prolongés au 23 » |"          # recopiée telle quelle de `git show main:registres/go.md` (main 31327cd8, lecture seule)


def _dates():
    auj = datetime.now(timezone.utc).date()
    ech = auj + timedelta(days=3)
    fin = datetime.combine(ech + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)
    return auj, ech, fin


def _lignes():
    auj, ech, _ = _dates()
    return (f"| {COURSE} | {auj} | calcul | course de confirmation (essai) | 200 USD (plafond de la ligne d'origine, non cumulé) | {ech} | Lazar | essai |\n"
            f"| {PETITE} | {auj} | calcul | ligne plus petite | 150 USD | {ech} | Lazar | essai |\n"
            f"| {DECISION} | {auj} | décision | un nœud tranché | — | {ech} | Lazar | essai |\n"
            f"| {ECHUE} | {auj - timedelta(days=10)} | calcul | ligne ancienne | 200 USD | {auj - timedelta(days=1)} | Lazar | essai |\n"
            f"| {REVOQUEE} | {auj} | calcul | ligne révoquée | 200 USD | {ech} | Lazar | essai |\n"
            f"| GO-2099-03-03-06 | {auj} | révocation | révoque {REVOQUEE} | — | {ech} | Lazar | essai |\n")


def _registre(d: Path, lignes: str | None = None, nom="go.md") -> Path:
    d.mkdir(parents=True, exist_ok=True)
    r = d / nom
    r.write_text(ENTETE + (_lignes() if lignes is None else lignes), encoding="utf-8")
    return r


def _config(go=COURSE, plafond=200, source=CONFIG_7B_V2, relatif=True) -> dict:
    c = json.loads(source.read_text(encoding="utf-8"))
    c["go_id"], c["plafond_usd"] = go, plafond
    if relatif:
        _, ech, fin = _dates()
        c["calendrier"] = {"dernier_jour_creation": str(ech - timedelta(days=1)), "fin_go_utc": fin.strftime("%Y-%m-%dT%H:%M:%SZ")}
    return c


# =========================================================================================================================================================
# 1. session_v13 : la ligne de la course est celle de la configuration, lue au registre ; plafond borné ; calendrier contre la ligne
# =========================================================================================================================================================
@pytest.mark.parametrize("plafond", [200, 200.0, 150, 0.5])
def test_session_v13_cas_sain_ligne_de_la_configuration_lue_au_registre(tmp_path, plafond):
    r = s13.go_de_la_configuration(_config(plafond=plafond), _registre(tmp_path), COURSE)
    assert r["go"] == COURSE and r["plafond_usd"] == 200.0 and r["plafond_configuration"] == float(plafond)


@pytest.mark.parametrize("cas, go_recu, go_config, plafond, motif", [
    ("go_config_different_du_go_recu", COURSE, PETITE, 100, f"go_id de la configuration ('{PETITE}') ≠ GO reçu ({COURSE})"),
    ("go_config_absent", COURSE, None, 100, "go_id de la configuration (None) ≠ GO reçu"),
    ("ligne_absente", ABSENTE, ABSENTE, 100, "absent du registre"),
    ("ligne_echue", ECHUE, ECHUE, 100, "hors de sa période de validité"),
    ("ligne_revoquee", REVOQUEE, REVOQUEE, 100, "révoqué par GO-2099-03-03-06"),
    ("ligne_decision", DECISION, DECISION, 100, "type 'décision'"),
    ("plafond_superieur_a_la_ligne", PETITE, PETITE, 200, "plafond de la configuration 200.0 > plafond 150.0 de la ligne"),
    ("plafond_superieur_de_peu", COURSE, COURSE, 200.01, "> plafond 200.0 de la ligne"),
    ("go_recu_illisible", "GO-X", "GO-X", 100, "identifiant de GO illisible"),
    ("go_recu_vide", "", "", 100, "identifiant de GO illisible"),
])
def test_session_v13_artefacts(tmp_path, cas, go_recu, go_config, plafond, motif):
    with pytest.raises(GardeSession, match=re.escape(motif)):
        s13.go_de_la_configuration(_config(go=go_config, plafond=plafond), _registre(tmp_path), go_recu)


@pytest.mark.parametrize("plafond", [0, -1, float("nan"), float("inf"), True, "200", None])
def test_session_v13_artefacts_plafond_de_configuration_illisible(tmp_path, plafond):
    with pytest.raises(GardeSession, match="plafond_usd de la configuration"):
        s13.go_de_la_configuration(_config(plafond=plafond), _registre(tmp_path), COURSE)


def test_session_v13_registre_absent_et_doublon_non_conforme(tmp_path):
    with pytest.raises(GardeSession, match="registre .* absent"):
        s13.go_de_la_configuration(_config(), tmp_path / "nulle-part.md", COURSE)
    auj, ech, _ = _dates()
    reg = _registre(tmp_path, _lignes() + f"| {COURSE} | {auj} | calcul | seconde ligne, pas une extension | 300 USD | {ech} | Lazar | essai |\n")
    with pytest.raises(GardeSession, match="en double"):
        s13.go_de_la_configuration(_config(), reg, COURSE)


def test_session_v13_calendrier_cas_sain_et_artefacts(tmp_path):
    reg = _registre(tmp_path)
    auj, ech, fin = _dates()
    r = s13.calendrier_de_la_configuration(_config(), reg, COURSE)
    assert r["fin_go_utc_s"] == int(fin.timestamp()) and r["echeance_go"] == str(ech) and r["plafond_ligne"] == 200.0
    # calendrier au-delà de l'échéance de la ligne : fin du GO un jour trop tard, ou dernier jour de création après la fin du GO
    c = _config()
    c["calendrier"]["fin_go_utc"] = (fin + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    with pytest.raises(GardeSession, match="≠ lendemain 00:00 UTC de l'échéance du GO"):
        s13.calendrier_de_la_configuration(c, reg, COURSE)
    c = _config()
    c["calendrier"]["dernier_jour_creation"] = str(ech + timedelta(days=1))
    with pytest.raises(GardeSession, match="après la fin du GO"):
        s13.calendrier_de_la_configuration(c, reg, COURSE)
    # jour donné après le dernier jour de création (la ligne est encore valide ce jour-là)
    with pytest.raises(GardeSession, match="dépassé"):
        s13.calendrier_de_la_configuration(_config(), reg, COURSE, ech)
    # le calendrier n'est jamais lu avant la ligne : une configuration au plafond excessif est refusée avant
    with pytest.raises(GardeSession, match="> plafond 150.0"):
        s13.calendrier_de_la_configuration(_config(go=PETITE), reg, PETITE)


def _main13(*argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = s13.main([str(a) for a in argv])
    return code, buf.getvalue().strip()


def test_session_v13_ligne_de_commande_codes_et_sorties(tmp_path):
    reg = _registre(tmp_path)
    cfg = tmp_path / "c.json"
    cfg.write_text(json.dumps(_config(plafond=180)), encoding="utf-8")
    auj, ech, fin = _dates()
    code, s = _main13("go-config", cfg, reg, COURSE)
    assert code == 0 and s == f"{COURSE} conforme (plafond de la ligne 200 USD, {auj} → {ech}) ; plafond de la configuration 180 ≤ 200", s
    code, s = _main13("calendrier-config", cfg, reg, COURSE, auj)
    assert code == 0 and s == f"fin_go_utc_s={int(fin.timestamp())} dernier_jour_creation={ech - timedelta(days=1)} echeance_go={ech} plafond_ligne=200", s
    for argv, motif in ((("go-config", cfg, reg, PETITE), "≠ GO reçu"), (("calendrier-config", cfg, reg, COURSE, ech), "dépassé"),
                        (("go-config", tmp_path / "absente.json", reg, COURSE), "JSON illisible"), (("go-config", cfg, reg, COURSE, "pas-une-date"), "Invalid isoformat")):
        code, s = _main13(*argv)
        assert code == 1 and motif in s, (argv, s)
    assert _main13("go-config", cfg, reg)[0] == 2 and _main13("calendrier-config", cfg)[0] == 2
    assert _main13("plafond-ligne", reg, PETITE)[0] == 0                                       # les sous-commandes de la v12 restent servies


def test_session_v13_go_de_la_course_cas_sain_et_artefacts(tmp_path):
    (tmp_path / "prereg").mkdir()
    (tmp_path / "prereg" / "c.json").write_text(json.dumps(_config(go=COURSE)), encoding="utf-8")
    lire = lambda c: (tmp_path / c).read_text(encoding="utf-8")                             # noqa: E731
    texte = "- Chemin de la configuration de T0.6 : `prereg/c.json`\n"
    assert s13.go_de_la_course(texte, lire) == COURSE
    for t, motif in (("rien\n", "cité 0 fois"), (texte + texte, "cité 2 fois"), ("- Chemin de la configuration de T0.6 : `prereg/absente.json`\n", "illisible (FileNotFoundError)")):
        with pytest.raises(GardeSession, match=re.escape(motif)):
            s13.go_de_la_course(t, lire)
    (tmp_path / "prereg" / "c.json").write_text(json.dumps({"go_id": "GO-X"}), encoding="utf-8")
    with pytest.raises(GardeSession, match="go_id de la configuration citée prereg/c.json illisible"):
        s13.go_de_la_course(texte, lire)


def test_session_v13_go_course_par_git_cas_sain_et_artefacts(tmp_path):
    d = tmp_path / "depot"
    subprocess.run(["git", "init", "-q", "-b", "main", str(d)], check=True)
    (d / "prereg").mkdir()
    (d / "prereg" / "c.json").write_text(json.dumps(_config(go=COURSE)), encoding="utf-8")
    (d / "prereg" / "p.md").write_text("- Chemin de la configuration de T0.6 : `prereg/c.json`\n", encoding="utf-8")
    for a in (["add", "-A"], ["-c", "user.email=t@example.invalid", "-c", "user.name=t", "commit", "-qm", "c"]):
        subprocess.run(["git", "-C", str(d), *a], check=True)
    h = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    assert _main13("go-course-git", d, h, "prereg/p.md") == (0, COURSE)
    assert _main13("go-course", d / "prereg" / "p.md", d) == (0, COURSE)
    code, s = _main13("go-course-git", d, h, "prereg/absent.md")
    assert code == 1 and "absent du commit" in s
    code, s = _main13("go-course-git", d, "abc", "prereg/p.md")
    assert code == 1 and "commit illisible" in s
    assert _main13("go-course", d / "prereg" / "absent.md", d)[0] == 1


# =========================================================================================================================================================
# 2. La ligne réelle GO-2026-11-10-01 (recopiée du registre de main) et la configuration de 7b v2 (brouillon 1), à jours explicites
# =========================================================================================================================================================
def test_ligne_reelle_de_main_lue_plafond_200_et_echeance_23(tmp_path):
    reg = _registre(tmp_path, LIGNE_MAIN + "\n")
    assert LIGNE_MAIN.startswith(f"| {NEUF_MAIN} | 2026-11-10 | calcul | ") and "| 2026-11-23 | Lazar |" in LIGNE_MAIN
    assert s12.plafond_de_la_ligne(reg, NEUF_MAIN) == 200.0                                   # « 200 USD (plafond de GO-2026-11-02-28, non cumulé) » : commentaire admis
    for jour in (date(2026, 11, 10), date(2026, 11, 16), date(2026, 11, 22), date(2026, 11, 23)):
        assert s12.ligne_go_calcul(reg, NEUF_MAIN, jour)["echeance"] == "2026-11-23"
    for jour in (date(2026, 11, 9), date(2026, 11, 24)):
        with pytest.raises(GardeSession, match="hors de sa période de validité"):
            s12.ligne_go_calcul(reg, NEUF_MAIN, jour)


def test_configuration_7b_v2_ne_differe_de_la_v1_que_par_trois_valeurs_et_est_scellee():
    v1 = json.loads(CONFIG_7B_V1.read_text(encoding="utf-8"))
    v2 = json.loads(CONFIG_7B_V2.read_text(encoding="utf-8"))
    def plat(d, p=""):
        for k, v in d.items():
            yield from (plat(v, p + k + ".") if isinstance(v, dict) else [(p + k, v)])
    a, b = dict(plat(v1)), dict(plat(v2))
    assert sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k)) == ["calendrier.dernier_jour_creation", "calendrier.fin_go_utc", "go_id"]
    assert (b["go_id"], b["calendrier.dernier_jour_creation"], b["calendrier.fin_go_utc"]) == (NEUF_MAIN, "2026-11-22", "2026-11-24T00:00:00Z")
    assert a["go_id"] == ANCIEN and b["plafond_usd"] == 200
    assert CONFIG_7B_V2.read_bytes() == (json.dumps(v2, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode()       # même forme d'écriture que la v1
    verifier(CONFIG_7B_V2)
    assert empreinte_config(v1) == "ca8003f90a9557ba42c8774e263407bdc2f4824b7f978f4c10f2e166ae97dd6d"                        # celle que cite le texte scellé de T0.6
    assert empreinte_config(v2) == "f5b4c4119dbf86909ce779668eb9f2c9b519be4d2aa0419564386330a152de1c"


@pytest.mark.parametrize("jour, attendu", [(date(2026, 11, 16), "conforme"), (date(2026, 11, 22), "conforme"), (date(2026, 11, 23), "dépassé"), (date(2026, 11, 24), "validité")])
def test_configuration_7b_v2_et_ligne_reelle_calendrier_les_16_22_23_et_24(tmp_path, jour, attendu):
    reg = _registre(tmp_path, LIGNE_MAIN + "\n")
    v2 = json.loads(CONFIG_7B_V2.read_text(encoding="utf-8"))
    if attendu == "conforme":
        r = s13.calendrier_de_la_configuration(v2, reg, NEUF_MAIN, jour)
        assert r["fin_go_utc_s"] == int(datetime(2026, 11, 24, tzinfo=timezone.utc).timestamp()) and r["dernier_jour_creation"] == "2026-11-22"
    else:
        with pytest.raises(GardeSession, match=attendu):
            s13.calendrier_de_la_configuration(v2, reg, NEUF_MAIN, jour)


def test_artefact_la_configuration_7b_v1_est_refusee_sous_la_ligne_neuve_et_la_v2_sous_l_ancienne(tmp_path):
    reg = _registre(tmp_path, LIGNE_MAIN + "\n")
    with pytest.raises(GardeSession, match="≠ GO reçu"):
        s13.go_de_la_configuration(json.loads(CONFIG_7B_V1.read_text(encoding="utf-8")), reg, NEUF_MAIN, date(2026, 11, 16))
    with pytest.raises(GardeSession, match="≠ GO reçu"):
        s13.go_de_la_configuration(json.loads(CONFIG_7B_V2.read_text(encoding="utf-8")), reg, ANCIEN, date(2026, 11, 16))


# =========================================================================================================================================================
# 3. configuration_v7 : toute configuration contre le registre, plus d'identifiant en dur
# =========================================================================================================================================================
def test_configuration_v7_cas_sain_course_7b_v2_et_ligne_relative(tmp_path):
    l = cf7.exiger_config_t06_v7(json.loads(CONFIG_7B_V2.read_text(encoding="utf-8")), _registre(tmp_path, LIGNE_MAIN + "\n"), date(2026, 11, 16))
    assert l["go"] == NEUF_MAIN and l["plafond_configuration"] == 200.0
    assert cf7.exiger_config_t06_v7(_config(), _registre(tmp_path / "b"))["go"] == COURSE
    assert cf7.exiger_config_t06_v7(_config(go=PETITE, plafond=150), _registre(tmp_path / "c"))["plafond_usd"] == 150.0


@pytest.mark.parametrize("go, plafond, motif", [(ABSENTE, 100, "absent du registre"), (ECHUE, 100, "validité"), (REVOQUEE, 100, "révoqué"), (DECISION, 100, "type 'décision'"),
                                                (PETITE, 200, "> plafond 150.0"), (COURSE, 0, "plafond_usd de la configuration"), ("GO-X", 100, "illisible")])
def test_configuration_v7_artefacts(tmp_path, go, plafond, motif):
    with pytest.raises(GardeArret, match=re.escape(motif)):
        cf7.exiger_config_t06_v7(_config(go=go, plafond=plafond), _registre(tmp_path))


def test_configuration_v7_sans_registre_aucune_validation_jamais_un_repli():
    for c in (_config(), json.loads(CONFIG_7B_V1.read_text(encoding="utf-8"))):
        with pytest.raises(GardeArret, match="registre des GO exigé"):
            cf7.exiger_config_t06_v7(c)


def test_configuration_v7_le_reste_est_valide_comme_en_v6(tmp_path):
    c = _config()
    c["doses_saboteur"] = [0.5]                                                                # la dose 1 est exigée (validation v3 inchangée)
    with pytest.raises(GardeArret, match="dose 1"):
        cf7.exiger_config_t06_v7(c, _registre(tmp_path))
    c = _config()
    del c["egalite_jetons_reels"]
    with pytest.raises(GardeArret, match="egalite_jetons_reels"):
        cf7.exiger_config_t06_v7(c, _registre(tmp_path))


def test_artefact_la_v6_lit_la_configuration_7b_v2_comme_une_epreuve(tmp_path):
    """Pourquoi un lanceur de run neuf : la v6 tient pour épreuve toute ligne autre que l'ancienne valeur ; avec le préenregistrement, elle refuserait la course v14."""
    v2 = json.loads(CONFIG_7B_V2.read_text(encoding="utf-8"))
    assert cf6.est_epreuve(v2) and not cf6.est_epreuve(json.loads(CONFIG_7B_V1.read_text(encoding="utf-8")))


# =========================================================================================================================================================
# 4. lanceur_v7 : copie du v6 ; course ou épreuve reçue par --epreuve ; registre du commit (racine) lu pour toute configuration
# =========================================================================================================================================================
class _ApresGardes(Exception):
    pass


def _racine(tmp_path, lignes=None) -> Path:
    """Racine factice : liens vers l'arbre du dépôt, sauf `registres/` qui porte le registre de l'essai."""
    r = tmp_path / "racine"
    r.mkdir()
    for p in RACINE.iterdir():
        if p.name not in ("registres", ".git"):
            (r / p.name).symlink_to(p)
    _registre(r / "registres", lignes)
    return r


def _jusqu_apres_gardes(module, config, racine, monkeypatch, prereg=None, **k):
    """Joue `executer` jusqu'à la première étape qui suit les gardes (chargement des tâches), remplacée par une sentinelle : aucun modèle, aucune invite, aucun fichier."""
    monkeypatch.setattr(module, "charger_taches_t06", lambda *a, **kw: (_ for _ in ()).throw(_ApresGardes()))
    module.executer(config, racine, "20261110-000000-t06-reel", prereg, **k)


def test_lanceur_v7_ne_differe_du_v6_que_par_les_lignes_attendues():
    a = (T06 / "lanceur_v6.py").read_text(encoding="utf-8").splitlines()
    b = (T06 / "lanceur_v7.py").read_text(encoding="utf-8").splitlines()
    assert b[0].startswith("# [v7") and b[1:] != a
    d = [l for l in difflib.unified_diff(a, b[1:], lineterm="", n=0) if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    assert len([l for l in d if l.startswith("-")]) == 9 and len([l for l in d if l.startswith("+")]) == 10, d
    attendus = ("configuration_v7", "lanceur_v7", "epreuve: bool = False", "exiger_config_t06_v7", "not epreuve", "déclarée par l'amorce (--epreuve)", "if epreuve and prereg",
                "épreuve à blanc (--epreuve)", '"--epreuve", action="store_true"', "epreuve=a.epreuve")
    assert all(any(m in l for m in attendus) for l in d if l.startswith("+")), [l for l in d if l.startswith("+")]
    assert la7.exiger_config_t06_v7 is cf7.exiger_config_t06_v7 and la7.COMMANDE.endswith("lanceur_v7") and not hasattr(la7, "est_epreuve")


def test_lanceur_v7_cas_sain_course_avec_preenregistrement_passe_les_gardes(tmp_path, monkeypatch):
    with pytest.raises(_ApresGardes):
        _jusqu_apres_gardes(la7, _config(), _racine(tmp_path), monkeypatch, prereg="prereg/factice.md")


def test_lanceur_v7_cas_sain_epreuve_sans_preenregistrement_passe_les_gardes(tmp_path, monkeypatch):
    with pytest.raises(_ApresGardes):
        _jusqu_apres_gardes(la7, _config(go=PETITE, plafond=15), _racine(tmp_path), monkeypatch, epreuve=True)


def test_artefact_le_lanceur_v6_refuse_la_course_v14_avec_son_preenregistrement(tmp_path, monkeypatch):
    with pytest.raises(GardeArret, match="épreuve à blanc avec un préenregistrement"):
        _jusqu_apres_gardes(la6, _config(), _racine(tmp_path), monkeypatch, prereg="prereg/factice.md")


@pytest.mark.parametrize("cas, config, k, motif", [
    ("course_reelle_sans_preenregistrement", "course", {}, "sans préenregistrement"),
    ("epreuve_avec_preenregistrement", "course", {"prereg": "prereg/factice.md", "epreuve": True}, "avec un préenregistrement"),
    ("ligne_absente", "absente", {"prereg": "prereg/factice.md"}, "absent du registre"),
    ("ligne_echue", "echue", {"prereg": "prereg/factice.md"}, "validité"),
    ("plafond_superieur", "petite", {"prereg": "prereg/factice.md"}, "> plafond 150.0"),
])
def test_lanceur_v7_artefacts_arret_aux_gardes(tmp_path, monkeypatch, cas, config, k, motif):
    c = {"course": _config(), "absente": _config(go=ABSENTE), "echue": _config(go=ECHUE), "petite": _config(go=PETITE)}[config]
    prereg = k.pop("prereg", None)
    with pytest.raises(GardeArret, match=re.escape(motif)):
        _jusqu_apres_gardes(la7, c, _racine(tmp_path), monkeypatch, prereg=prereg, **k)


def test_lanceur_v7_lit_le_registre_de_la_racine(monkeypatch):
    """Sur l'arbre réel (dont le registre ne porte pas la ligne de course de l'essai), la même configuration est arrêtée : le registre lu est `racine/registres/go.md`."""
    with pytest.raises(GardeArret, match=f"{COURSE} absent du registre"):
        _jusqu_apres_gardes(la7, _config(), RACINE, monkeypatch, prereg="prereg/factice.md")


def test_lanceur_v7_option_epreuve_transmise_par_la_ligne_de_commande(tmp_path, monkeypatch):
    f = tmp_path / "config.json"
    f.write_text(json.dumps(_config()), encoding="utf-8")
    sceller(f)
    vus = []
    monkeypatch.setattr(la7, "executer", lambda config, racine, run_id, prereg, **k: vus.append((prereg, k)) or {"factice": True})
    monkeypatch.setattr(la7, "resume_imprimable", lambda r: r)
    assert la7._main(["--config", str(f), "--run-id", "r", "--epreuve"]) == 0
    assert la7._main(["--config", str(f), "--run-id", "r", "--prereg", "p.md"]) == 0
    assert vus == [(None, {"epreuve": True}), ("p.md", {"epreuve": False})]


# =========================================================================================================================================================
# 5. Ancienne valeur en dur absente du code v14
# =========================================================================================================================================================
def _chaines_de_code_python(chemin: Path) -> list[str]:
    """Constantes chaînes d'un module, docstrings exclues (les notes d'historique peuvent citer l'ancienne valeur ; le code, jamais)."""
    arbre = ast.parse(chemin.read_text(encoding="utf-8"))
    docs = set()
    for n in ast.walk(arbre):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.body and isinstance(n.body[0], ast.Expr) \
                and isinstance(n.body[0].value, ast.Constant) and isinstance(n.body[0].value.value, str):
            docs.add(id(n.body[0].value))
    return [n.value for n in ast.walk(arbre) if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs]


def _lignes_de_code_shell(chemin: Path) -> list[str]:
    return [l for l in chemin.read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#")]


def test_ancienne_valeur_absente_du_code_v14_cas_sain_et_artefact():
    for f in ("session_v13.py", "configuration_v7.py", "lanceur_v7.py"):
        assert not [c for c in _chaines_de_code_python(T06 / f) if ANCIEN in c], f
    for f in ("lancer_t06_v14.sh", "amorce_instance_t06_v12.sh"):
        assert not [l for l in _lignes_de_code_shell(RACINE / "scripts" / f) if ANCIEN in l], f
    # artefact (R5) : la même recherche voit l'ancienne valeur là où elle est écrite en dur (v13, v11, configuration.py, session.py)
    assert [l for l in _lignes_de_code_shell(RACINE / "scripts" / "lancer_t06_v13.sh") if ANCIEN in l]
    assert [l for l in _lignes_de_code_shell(RACINE / "scripts" / "amorce_instance_t06_v11.sh") if ANCIEN in l]
    assert ANCIEN in _chaines_de_code_python(T06 / "configuration.py") and ANCIEN in _chaines_de_code_python(T06 / "session.py")
