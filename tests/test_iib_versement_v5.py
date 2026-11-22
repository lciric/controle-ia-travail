"""Poussée de chaque lot dès qu'il est scellé, organisme retenu v5 (correctif 0014 ; ordre de l'étalonnage, §§ 4 et 7).

Constat de l'étalonnage : la branche d'essai restait au commit de lancement après dix-huit lots, l'amorce ne poussant qu'à la
fin du run, sur un arrêt, à la minuterie ou à un second démarrage. Ici : le **vrai** script de consignation de l'amorce (tiré
du texte de `scripts/amorce_instance_iib_v5.sh`), une origine nue locale, et le lanceur qui l'appelle après chaque lot puis
vérifie lui-même la branche distante. Cas sain, artefacts (origine qui refuse, script qui dit 0 sans pousser, délai), reprise
après un refus isolé, arrêt après trois refus de suite (R5 : aucun échec avalé)."""
import json
import os
import re
import subprocess
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.iib import lanceur_v5 as la
from controle_ia.iib import versement_v5 as vs
from controle_ia.iib.jouet_v5 import ModeleJouetDeLangue
from controle_ia.scellement import verifier

DEPOT = Path(__file__).resolve().parents[1]
AMORCE = DEPOT / "scripts" / "amorce_instance_iib_v5.sh"
BRANCHE = "essai/iib-explo-v99"
RUN = "20991231-000010-iib-jouet"


def git(d, *a, check=True):
    return subprocess.run(["git", "-C", str(d), *a], capture_output=True, text=True, check=check).stdout.strip()


def script_de_consignation(r: Path, t: Path) -> Path:
    """Le script `iib-consigner.sh` tel que l'amorce l'écrit : son en-tête (variables) puis le corps cité, à la lettre."""
    texte = AMORCE.read_text(encoding="utf-8")
    m = re.search(r"cat >> \"\$R/iib-consigner\.sh\" <<'CONSIGNER'\n(.*?)\nCONSIGNER\n", texte, re.S)
    assert m, "corps du script de consignation introuvable dans l'amorce"
    tete = (f"#!/usr/bin/env bash\nR='{r}'; BRANCHE='{BRANCHE}'; T='{t}'; JOURNAL='{t}/journal.txt'; MORCEAU_MAX='90000000'; "
            "POUSSEE_ATTENTE_S='0'\n")
    chemin = r / "iib-consigner.sh"
    chemin.write_text(tete + m.group(1) + "\n", encoding="utf-8")
    return chemin


def poste(tmp: Path, refuse: bool = False) -> dict:
    """Origine nue (qui refuse toute poussée si `refuse`), dépôt extrait sous `R/amorce-depot` sur la branche d'essai, poussée
    initiale faite (comme l'amorce), monde jouet du lanceur."""
    from test_iib_lanceur_v5 import _monde

    origine, r = tmp / "origine.git", tmp / "R"
    subprocess.run(["git", "init", "-q", "--bare", str(origine)], check=True)
    d = r / "amorce-depot"
    subprocess.run(["git", "clone", "-q", str(origine), str(d)], check=True, capture_output=True)
    for k, v in (("user.name", "essai"), ("user.email", "essai@invalid"), ("commit.gpgsign", "false")):
        git(d, "config", k, v)
    (d / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    git(d, "checkout", "-q", "-b", BRANCHE)
    config = _monde(d)
    (d / "runs" / RUN).mkdir(parents=True)                   # le manifeste du run existe avant le premier lot (`executer`)
    (d / "runs" / RUN / "manifeste.json").write_text("{}\n", encoding="utf-8")
    git(d, "add", "-A")
    git(d, "commit", "-qm", "commit de lancement")
    git(d, "push", "-q", "origin", BRANCHE)
    if refuse:
        crochet = origine / "hooks" / "pre-receive"
        crochet.write_text("#!/bin/sh\necho 'refus planté (artefact)' >&2\nexit 1\n", encoding="utf-8")
        crochet.chmod(0o755)
    t = r / "iib"
    t.mkdir(parents=True)
    return {"origine": origine, "r": r, "d": d, "t": t, "config": config, "script": script_de_consignation(r, t)}


def sur_l_origine(p: dict) -> set:
    return set(git(p["origine"], "ls-tree", "-r", "--name-only", BRANCHE).splitlines())


def etalonner(p: dict, versement) -> dict:
    d = p["d"]
    return la.phase_etalonnage(p["config"], d, d / "diag" / RUN, ModeleJouetDeLangue(), la.MondeJouet(), {}, d / "donnees" / RUN,
                               carte=False, versement=versement)


@pytest.fixture(scope="module")
def sain(tmp_path_factory):
    p = poste(tmp_path_factory.mktemp("versement-sain"))
    v = vs.Versement(p["d"], {vs.CONSIGNER: str(p["script"])}, "jouet")
    res = etalonner(p, v)
    return {**p, "v": v, "res": res}


def test_cas_sain_chaque_lot_scelle_est_sur_la_branche_distante_aussitot(sain):
    v, res = sain["v"], sain["res"]
    assert res["lots"] == 28 and len(v.journal) == 28
    assert all(e["poussee"] == "faite" and e["code"] == 0 and e["cause"] is None for e in v.journal)
    distant = sur_l_origine(sain)
    for k in range(1, 29):
        lot = [n for n in distant if re.fullmatch(rf"diag/{RUN}/lots/lot-{k:03d}-etalonnage-[a-z]+\.json", n)]
        ids = [n for n in distant if re.fullmatch(rf"donnees/{RUN}/lots/ids-lot-{k:03d}-etalonnage-[a-z]+\.json", n)]
        assert len(lot) == 1 and len(ids) == 1 and lot[0] + ".sha256" in distant and ids[0] + ".sha256" in distant, k
    # un commit par lot, à la suite du commit de lancement (aucun lot n'a attendu le suivant)
    messages = git(sain["origine"], "log", "--format=%s", BRANCHE).splitlines()
    assert sum(m.startswith("(ii-b) : résultats et données légères (versement lot ") for m in messages) == 28
    # le motif « versement » ne laisse aucune trace de journal par lot (les consignations d'arrêt, elles, en laissent)
    assert not any(n.startswith("traces/") for n in distant)
    # les empreintes poussées sont celles des sorties scellées
    f = sain["d"] / "diag" / RUN / "lots" / "lot-001-etalonnage-honnete.json"
    assert git(sain["origine"], "show", f"{BRANCHE}:diag/{RUN}/lots/lot-001-etalonnage-honnete.json") + "\n" == f.read_text(encoding="utf-8")
    assert verifier(f)


def test_marques_de_progres_de_chaque_poussee_relayables_par_l_amorce(tmp_path, capfd):
    p = poste(tmp_path)
    v = vs.Versement(p["d"], {vs.CONSIGNER: str(p["script"])}, "jouet")
    f = p["d"] / "diag" / RUN / "lots" / "lot-001-essai.json"
    f.parent.mkdir(parents=True)
    f.write_text("{}\n", encoding="utf-8")
    assert v("lot 001 essai", [f])["poussee"] == "faite"
    lignes = [l for l in capfd.readouterr().err.splitlines() if l.startswith("PROGRES ")]
    motif = r"PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-zA-Z0-9_-]+=[^ ]+)+"          # MOTIF_PROGRES de l'amorce
    interdit = re.compile(r"au-dessus|interpr|échec|echec|aire=|bas=|haut=|ligne_|table_|plancher", re.I)  # MOTIF_INTERDIT de l'amorce
    assert lignes and all(re.fullmatch(motif, l) and not interdit.search(l) for l in lignes)
    assert "etape=versement" in lignes[-1] and "poussee=faite" in lignes[-1]


def test_artefact_origine_qui_refuse_trois_fois_de_suite_arret_lots_scelles_sur_le_disque(tmp_path, capfd):
    p = poste(tmp_path, refuse=True)
    v = vs.Versement(p["d"], {vs.CONSIGNER: str(p["script"])}, "jouet")
    with pytest.raises(GardeArret, match="refusée 3 fois de suite"):
        etalonner(p, v)
    assert [e["poussee"] for e in v.journal] == ["refusee"] * 3 and all(e["cause"] == "script_code_1" for e in v.journal)
    err = capfd.readouterr().err
    refus = [l for l in err.splitlines() if l.startswith("PROGRES ") and "etape=versement" in l]
    assert len(refus) == 3 and all("poussee=refusee" in l for l in refus) and "refus_de_suite=3" in refus[-1]
    assert err.count("VERSEMENT REFUSÉ") == 3                                    # visible hors des marques de progrès aussi
    lots = sorted((p["d"] / "diag" / RUN / "lots").glob("lot-*.json"))
    assert len(lots) == 3 and all(verifier(f) for f in lots)                     # rien de perdu : scellés sur le disque
    assert not any(n.startswith("diag/") for n in sur_l_origine(p))              # rien n'est passé, et c'est dit
    journal = (p["t"] / "journal.txt").read_text(encoding="utf-8")
    assert journal.count("poussée : tentative 3 refusée") == 3 and "poussée impossible (versement lot 001" in journal


def test_artefact_script_qui_rend_0_sans_pousser_vu_par_la_verification(tmp_path):
    p = poste(tmp_path)
    faux = tmp_path / "faux-consigner.sh"
    faux.write_text("#!/usr/bin/env bash\ngit add -A diag && git commit -qm faux >/dev/null\nexit 0\n", encoding="utf-8")
    v = vs.Versement(p["d"], {vs.CONSIGNER: str(faux)}, "jouet")
    f = p["d"] / "diag" / RUN / "lots" / "lot-001-essai.json"
    f.parent.mkdir(parents=True)
    f.write_text("{}\n", encoding="utf-8")
    e = v("lot 001 essai", [f])
    assert e["code"] == 0 and e["poussee"] == "refusee" and e["cause"] == "tete_non_poussee"
    nu = tmp_path / "rien.sh"
    nu.write_text("#!/usr/bin/env bash\nexit 0\n", encoding="utf-8")
    g = p["d"] / "diag" / RUN / "lots" / "lot-002-essai.json"
    g.write_text("{}\n", encoding="utf-8")
    assert vs.Versement(p["d"], {vs.CONSIGNER: str(nu)}, "jouet")("lot 002", [g])["cause"] == "fichier_non_suivi"


def test_un_refus_isole_ne_coute_rien_la_poussee_suivante_porte_le_lot_refuse(tmp_path):
    p = poste(tmp_path)
    v = vs.Versement(p["d"], {vs.CONSIGNER: str(p["script"])}, "jouet")
    crochet = p["origine"] / "hooks" / "pre-receive"
    crochet.write_text("#!/bin/sh\nexit 1\n", encoding="utf-8")
    crochet.chmod(0o755)
    d = p["d"] / "diag" / RUN / "lots"
    d.mkdir(parents=True)
    (d / "lot-001-essai.json").write_text("{}\n", encoding="utf-8")
    assert v("lot 001", [d / "lot-001-essai.json"])["poussee"] == "refusee" and v.refus_consecutifs == 1
    crochet.unlink()
    (d / "lot-002-essai.json").write_text("{}\n", encoding="utf-8")
    assert v("lot 002", [d / "lot-002-essai.json"])["poussee"] == "faite" and v.refus_consecutifs == 0
    assert {f"diag/{RUN}/lots/lot-001-essai.json", f"diag/{RUN}/lots/lot-002-essai.json"} <= sur_l_origine(p)


def test_delai_depasse_le_groupe_du_script_est_arrete_par_son_identifiant(tmp_path, monkeypatch):
    p = poste(tmp_path)
    lent = tmp_path / "lent.sh"
    temoin = tmp_path / "fils.pid"
    lent.write_text(f"#!/usr/bin/env bash\nsleep 300 &\necho $! > {temoin}\nwait\n", encoding="utf-8")
    monkeypatch.setattr(vs, "DELAI_CONSIGNATION_S", 2)
    f = p["d"] / "x.json"
    f.write_text("{}\n", encoding="utf-8")
    e = vs.Versement(p["d"], {vs.CONSIGNER: str(lent)}, "jouet")("lot lent", [f])
    assert e["code"] == "delai" and e["poussee"] == "refusee" and e["cause"] == "script_code_delai"
    fils = int(temoin.read_text().strip())
    try:
        os.kill(fils, 0)
        vivant = Path(f"/proc/{fils}/stat").read_text().split()[2] != "Z"
    except ProcessLookupError:
        vivant = False
    assert not vivant, "le fils du script (même groupe) devait être arrêté"


def test_mode_reel_exige_le_script_mode_jouet_sans_script_le_dit(tmp_path, capfd, monkeypatch):
    with pytest.raises(GardeArret, match="mode réel sans IIB_CONSIGNER"):
        vs.Versement(tmp_path, {}, "reel")
    with pytest.raises(GardeArret, match="absent du disque"):
        vs.Versement(tmp_path, {vs.CONSIGNER: str(tmp_path / "absent.sh")}, "reel")
    v = vs.Versement(tmp_path, {}, "jouet")                                      # cas sain : jouet, rien à pousser, et c'est écrit
    assert v("lot 001", [])["poussee"] == "sans_script" and "poussee=sans_script" in capfd.readouterr().err
    # la phase d'étalonnage en mode réel refuse de partir sans poussée par lot (avant tout calcul)
    from test_iib_lanceur_v5 import _monde

    config = _monde(tmp_path / "m")
    config["mode"] = "reel"
    monkeypatch.setattr(la.cf, "exiger_config_v5", lambda *a, **k: True)        # la seule garde visée : la poussée par lot
    monkeypatch.setattr(la, "exiger_accord", lambda *a, **k: "GO-2099-01-01-01")
    with pytest.raises(GardeArret, match="sans poussée par lot"):
        la.phase_etalonnage(config, tmp_path / "m", tmp_path / "m" / "d", None, None, carte=False)
    assert not (tmp_path / "m" / "d").exists()


def test_amorce_passe_le_script_au_lanceur_et_le_motif_versement_sans_trace():
    texte = AMORCE.read_text(encoding="utf-8")
    ligne = [l for l in texte.splitlines() if "controle_ia.iib.lanceur_v5 --phase etalonnage" in l and not l.lstrip().startswith("#")]
    assert len(ligne) == 1 and 'IIB_CONSIGNER="$R/iib-consigner.sh"' in ligne[0]
    assert 'case "$1" in "versement "*) TC=0;; *) TC=1;; esac; TRACE_CONSIGNATION=$TC consigner_partiel "$1"' in texte
    assert json.dumps(vs.CONSIGNER) == '"IIB_CONSIGNER"' and vs.REFUS_CONSECUTIFS_MAX == 3
