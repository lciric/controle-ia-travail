"""Essais de l'épreuve d'isolement v8 et des attendus v7 (essai Lean D-1a ; contre-lecture Fable 5.2 des corrections du
troisième essai, 59b0ec03…). Copie de `test_lean_essai_epreuve_v7.py` (inchangé, R12), portée sur la v8, plus :
- B1 : le cas Lean de la limite de mémoire jugé sur la seule compilation ; objet de contrôle de la contre-lecture (compilation
  en échec d'elle-même, vérificateur tué par la mémoire) : écart ; conditions indépendantes (résultat systemd, classement,
  code, ligne témoin) ;
- signal d'un chemin de cgroupe faux et pics rapportés sur au moins trois relevés ;
- mémoire de la machine entière pour trois passages en parallèle : lecture de /proc/meminfo, relevé pendant le bloc,
  critères écrits d'avance, `mesurer` de bout en bout sur un bac factice ;
- attendus v7 = v6 plus le seul cas Lean de la limite de mémoire réécrit.
"""
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import pytest

from controle_ia.lean_essai import epreuve_isolement_v8 as E

RACINE = Path(__file__).resolve().parents[1]
ART = RACINE / "scripts" / "lean_essai_d1a_v4" / "artefacts_r5_v4"
COMPILER = RACINE / "scripts" / "lean_essai_d1a_v11" / "compiler_comme_bac_v1.sh"
CHAINE = os.environ.get("LEAN_ESSAI_D1A_CHAINE", "")
avec_chaine = pytest.mark.skipif(not CHAINE, reason="chaîne épinglée absente : LEAN_ESSAI_D1A_CHAINE non posée (essai sauté, "
                                                    "pas réussi)")
ATT5 = json.loads((ART / "attendus-v5.json").read_text(encoding="utf-8"))
ATT6 = json.loads((ART / "attendus-v6.json").read_text(encoding="utf-8"))
ATT7 = json.loads((ART / "attendus-v7.json").read_text(encoding="utf-8"))


def ligne_lean(nom, issue, detail):
    """Une ligne de tentative telle que `lean --json` l'écrit (message d'information échappé)."""
    return json.dumps({"severity": "information", "data": f"ISOLEMENT {nom} {issue} {detail}\n"}, ensure_ascii=False)


# ---- jugement des tentatives -----------------------------------------------------------------------------------------------

def test_tentatives_lues_dans_le_json_de_lean():
    texte = "\n".join([ligne_lean("a", "ECHEC", "no such file or directory (error code: 2)\n  file: /srv"),
                       ligne_lean("b", "REUSSI", "écrit")])
    assert E.tentatives(texte) == {"a": "ECHEC", "b": "REUSSI"}
    assert E.details_tentatives(texte)["a"] == "no such file or directory (error code: 2)"


def test_echec_sans_valeur_de_preuve():
    cas = {"tentatives": {"reseau-dns": "ECHEC", "reseau-curl-ip": "ECHEC"},
           "echecs_invalides": ["could not execute external process"]}
    sain = "\n".join([ligne_lean("reseau-dns", "ECHEC", "code 1 socket.gaierror: [Errno -3]"),
                      ligne_lean("reseau-curl-ip", "ECHEC", "code 7 curl: (7) Failed to connect")])
    assert E.juger_tentatives(cas, sain) == []
    artefact = "\n".join([ligne_lean("reseau-dns", "ECHEC", "code 255 could not execute external process 'python3'"),
                          ligne_lean("reseau-curl-ip", "ECHEC", "code 7 curl: (7) Failed to connect")])
    ecarts = E.juger_tentatives(cas, artefact)
    assert len(ecarts) == 1 and "reseau-dns" in ecarts[0] and "sans valeur de preuve" in ecarts[0]


def test_sain_vivant():
    cas = {"tentatives": {"ecriture-tmp": "REUSSI", "ecriture-item": "REUSSI"}}
    assert E.sain_vivant(cas, ligne_lean("ecriture-tmp", "REUSSI", "écrit") + "\n" + ligne_lean("ecriture-item", "REUSSI", "x"))
    assert not E.sain_vivant(cas, ligne_lean("ecriture-tmp", "REUSSI", "écrit"))
    assert not E.sain_vivant(cas, "")   # sortie du troisième essai : aucune tentative


def test_extrait_sonde_borne():
    long = "x" * (E.EXTRAIT_SONDE + 10)
    ex = E.extrait_sonde({"sortie_compilation": long, "erreurs_compilation": "e" * 5000, "compilation": {"code": 1}})
    assert len(ex["sortie_compilation_extrait"]) == E.EXTRAIT_SONDE and ex["sortie_compilation_tronquee"]
    assert len(ex["erreurs_compilation_extrait"]) == E.EXTRAIT_ERREURS and ex["erreurs_compilation_tronquees"]
    assert ex["sonde_muette"] and ex["code_compilation"] == 1
    assert not E.extrait_sonde({"sortie_compilation": ligne_lean("a", "ECHEC", "x")})["sonde_muette"]


def test_statuts_genres():
    rendus = [{"genre": "isolement Lean", "ok": False}, {"genre": "isolement Lean", "ok": True},
              {"genre": "Python", "ok": True}, {"genre": "limites", "ok": False}, {"genre": "limites", "ok": True}]
    assert E.statuts_genres(rendus, {"isolement Lean": False, "Python": True}) == {
        "isolement Lean": "épreuve morte", "Python": "conforme", "limites": "non conforme"}
    assert E.statuts_genres(rendus, {"isolement Lean": True})["isolement Lean"] == "non conforme"


# ---- épreuve entière avec un bac factice -------------------------------------------------------------------------------------

def res_lean(sortie="", code=0, incident=None, resultat_c=None, incident_c=None, resultat_v=None, incident_v=None):
    gardes = {g: {"ok": True, "motifs": []} for g in ("G-L1", "G-L2", "G-L3", "G-L3+", "G-L4", "G-L5", "G-L6", "G-L7", "G-L8")}
    return {"verdict": {"accepte_gardes": True, "gardes": gardes, "rejeu_ok": True, "enonces_imprimes": {},
                        "impressions": {}, "axiomes": {}},
            "sortie_compilation": sortie, "erreurs_compilation": "", "compilation": {"code": code, "resultat": resultat_c},
            "noyau": {"resultat": resultat_v}, "isolement": True, "incident_bac": incident,
            "incident_compilation": incident_c, "incident_noyau": incident_v,
            "processus_residuels": [], "dossiers_restants": []}


def res_python(stdout="", code=0, incident=None):
    return {"execution": {"code": code, "duree_murale_s": 0.1}, "stdout": stdout, "stderr": "", "isolement": True,
            "incident_bac": incident, "processus_residuels": [], "dossiers_restants": []}


def sortie_attendue(cas):
    return "\n".join(ligne_lean(n, issue, "détail") for n, issue in cas["tentatives"].items())


class BacFactice:
    """Rend, pour chaque fichier, la sortie que l'attendu exige ; `casser` dit quels fichiers rendent une sortie vide (sonde
    morte, comme au troisième essai)."""
    casser: set = set()
    attendus: dict = {}

    def __init__(self, cfg, *a, **k):
        self.cfg = cfg

    def _cas(self, source):
        for groupe, liste in self.attendus.items():
            if isinstance(liste, list):
                for c in liste:
                    if isinstance(c, dict) and (ART / c["fichier"]).read_text(encoding="utf-8") == source:
                        return groupe, c
        raise AssertionError("source inconnue")

    def verifier_lean(self, item, source, m):
        groupe, c = self._cas(source)
        if c["fichier"] in self.casser:
            return res_lean("", code=1)
        if groupe == "isolement_lean":
            return res_lean(sortie_attendue(c))
        if groupe == "limites_lean":
            return res_lean("", code=1, incident="mémoire", resultat_c="oom-kill", incident_c="mémoire",
                            resultat_v="oom-kill", incident_v="mémoire")
        r = res_lean()
        r["verdict"]["accepte_gardes"] = c["accepte"]
        for g in c.get("echecs", []):
            r["verdict"]["gardes"][g] = {"ok": False, "motifs": ["m"]}
        if "rejeu" in c:
            r["verdict"]["rejeu_ok"] = c["rejeu"]
        for nom, morceaux in c.get("enonce_contient", {}).items():
            r["verdict"]["enonces_imprimes"][nom] = " ".join(morceaux)
        for nom, morceaux in c.get("impression_contient", {}).items():
            r["verdict"]["impressions"][nom] = " ".join(morceaux)
        for nom, ax in c.get("axiomes_contient", {}).items():
            r["verdict"]["axiomes"][nom] = ax
        r["sortie_compilation"] = " ".join(c.get("sortie_agent_contient", []))
        return r

    def executer_python(self, item, code):
        groupe, c = self._cas(code)
        if c["fichier"] in self.casser:
            return res_python("", code=1)
        out = " ".join(c.get("stdout_contient", []))
        if "tentatives" in c:
            out += "\n" + "\n".join(f"ISOLEMENT {n} {i} détail" for n, i in c["tentatives"].items())
        code_ = c.get("code", 1 if c.get("code_non_nul") else 0)
        return res_python(out, code_, c.get("incident_attendu"))


@pytest.fixture
def epreuve_factice(tmp_path, monkeypatch):
    monkeypatch.setattr(E, "LEURRE", tmp_path / "leurre" / "leurre-v1.txt")
    monkeypatch.setattr(E, "manifeste", lambda racines=None: "m")
    monkeypatch.setattr(E, "PIEGES_HOTE", ())
    monkeypatch.setattr(E.subprocess, "run", lambda *a, **k: subprocess.CompletedProcess(a, 0, "", ""))
    monkeypatch.setattr(E.X, "Bac", BacFactice)
    BacFactice.attendus = ATT7
    for n in ("items", "sorties"):
        (tmp_path / n).mkdir()
    cfg = E.X.Config(lean="/l", lean_path="/p", verificateur_sha256="x", mode="bac", racine_items=tmp_path / "items",
                     racine_sorties=tmp_path / "sorties")

    def jouer(casser=()):
        BacFactice.casser = set(casser)
        return E.epreuve(cfg, ART)
    jouer.cfg = cfg
    return jouer


def test_epreuve_cas_sain_conforme(epreuve_factice):
    r = epreuve_factice()
    assert r["statut"] == "conforme" and r["conforme"], [c for c in r["cas"] if not c["ok"]]
    assert r["sains"] == {"isolement Lean": True, "Python": True}
    iso = [c for c in r["cas"] if c["genre"] == "isolement Lean"]
    assert len(iso) == 5 and all("sortie_compilation_extrait" in c and not c["sonde_muette"] for c in iso)
    assert [c["genre"] for c in r["cas"]].count("limites Lean") == 1
    assert len(r["cas"]) == 21 + 5 + 4 + 5 + 1


def test_epreuve_morte_quand_le_sain_ne_rend_rien(epreuve_factice):
    """Artefact R5 : le troisième essai rejoué (les cinq sondes Lean muettes, cas sain compris)."""
    r = epreuve_factice(casser={c["fichier"] for c in ATT7["isolement_lean"]})
    assert r["statut"] == "épreuve morte" and not r["conforme"] and r["genres_morts"] == ["isolement Lean"]
    assert r["genres"]["isolement Lean"] == "épreuve morte" and r["genres"]["Python"] == "conforme"
    assert all(c["sonde_muette"] for c in r["cas"] if c["genre"] == "isolement Lean")


def test_non_conforme_quand_le_sain_vit_et_un_artefact_echoue(epreuve_factice):
    r = epreuve_factice(casser={"iso_lecture_v3.lean"})
    assert r["statut"] == "non conforme" and r["genres"]["isolement Lean"] == "non conforme" and not r["genres_morts"]


def test_epreuve_morte_python(epreuve_factice):
    r = epreuve_factice(casser={"iso_persistance_ecrire_v1.py"})
    assert r["statut"] == "épreuve morte" and r["genres_morts"] == ["Python"]


def test_code_de_sortie_epreuve_morte(monkeypatch):
    monkeypatch.setattr(E.X, "charger_config", lambda *a, **k: None)
    for statut, conforme, code in (("épreuve morte", False, 3), ("non conforme", False, 1), ("conforme", True, 0)):
        monkeypatch.setattr(E, "epreuve", lambda cfg, art, s=statut, c=conforme: {"statut": s, "conforme": c})
        assert E.main(["epreuve"]) == code


def test_juger_limite_lean_cas_sain():
    cas = ATT7["limites_lean"][0]
    assert E.juger_limite_lean(cas, res_lean("", code=1, incident="mémoire", resultat_c="oom-kill", incident_c="mémoire",
                                             resultat_v="oom-kill", incident_v="mémoire")) == []


def test_juger_limite_lean_objet_de_controle_b1():
    """Compilation en échec d'elle-même (code 1, `exit-code`, aucune ligne « ALLOUE »), vérificateur tué par la mémoire :
    `incident_bac` vaut « mémoire » ; le juge v7 rendait zéro écart, le juge v8 en rend."""
    cas = ATT7["limites_lean"][0]
    res = res_lean("", code=1, incident="mémoire", resultat_c="exit-code", incident_c=None, resultat_v="oom-kill",
                   incident_v="mémoire")
    ecarts = E.juger_limite_lean(cas, res)
    assert any("résultat systemd 'exit-code'" in x for x in ecarts) and any("incident None" in x for x in ecarts)
    from controle_ia.lean_essai import epreuve_isolement_v7 as E7
    assert E7.juger_limite_lean(ATT6["limites_lean"][0], res) == []   # le défaut de la v7, reproduit


@pytest.mark.parametrize("champs,motif", [
    ({"resultat_c": "exit-code", "incident_c": "mémoire"}, "résultat systemd"),     # classement seul juste
    ({"resultat_c": "oom-kill", "incident_c": None}, "incident None"),               # résultat seul juste
    ({"resultat_c": "oom-kill", "incident_c": "délai"}, "incident 'délai'"),
    ({"resultat_c": "timeout", "incident_c": "délai"}, "résultat systemd 'timeout'"),
])
def test_juger_limite_lean_conditions_independantes(champs, motif):
    cas = ATT7["limites_lean"][0]
    ecarts = E.juger_limite_lean(cas, res_lean("", code=1, incident="mémoire", **champs))
    assert any(motif in x for x in ecarts), ecarts


def test_juger_limite_lean_code_et_ligne_temoin():
    cas = ATT7["limites_lean"][0]
    tue = dict(resultat_c="oom-kill", incident_c="mémoire", incident="mémoire")
    assert any("code 0" in x for x in E.juger_limite_lean(cas, res_lean("", code=0, **tue)))
    assert any("ALLOUE" in x for x in E.juger_limite_lean(cas, res_lean("ALLOUE 1400000000", code=1, **tue)))


def test_noter_admet_l_incident_de_compilation_attendu():
    rendus = []
    E._noter(rendus, [], "limites Lean", ATT7["limites_lean"][0], res_lean("", code=1, incident="mémoire",
             resultat_c="oom-kill", incident_c="mémoire"), [])
    assert rendus[0]["ok"]
    rendus = []
    E._noter(rendus, [], "gardes Lean", {"fichier": "x.lean"}, res_lean("", incident="mémoire"), [])
    assert not rendus[0]["ok"] and "incident du bac mémoire" in rendus[0]["ecarts"]


def test_limite_lean_porte_ses_deux_incidents(epreuve_factice):
    r = epreuve_factice()
    cas = [c for c in r["cas"] if c["genre"] == "limites Lean"]
    assert len(cas) == 1 and cas[0]["ok"] and cas[0]["incident_compilation"] == "mémoire"
    assert cas[0]["incident_noyau"] == "mémoire" and cas[0]["temps"]["resultat"] == "oom-kill"


@pytest.mark.parametrize("groupe", ["isolement_lean", "python"])
def test_temoin_sain_obligatoire(epreuve_factice, tmp_path, monkeypatch, groupe):
    """R2 : des attendus sans cas sain dans un genre d'isolement sont refusés avant tout item."""
    att = json.loads(json.dumps(ATT7))
    for c in att[groupe]:
        c.pop("sain", None)
    art = tmp_path / "art"
    shutil.copytree(ART, art)
    (art / "attendus-v7.json").write_text(json.dumps(att, ensure_ascii=False))
    with pytest.raises(E.X.ErreurBac, match="sans cas sain"):
        E.epreuve(epreuve_factice.cfg, art)


# ---- v8 : signal d'un chemin de cgroupe faux --------------------------------------------------------------------------------

def temps(duree=4.5, n=40, pic=4 * 10**8, isolement=True):
    return {"isolement": isolement, "duree_service_s": duree, "memoire_echantillons": n,
            "memoire_pic_echantillonne_octets": pic}


def test_signal_memoire_cas_sain():
    s = E.signal_memoire([("a", temps()), ("b", temps(duree=0.3, n=2, pic=7)), ("c", None)])
    assert s == {"chemin_cgroupe_faux": False, "lancements_sans_releve": [],
                 "pics_rapportes_octets": {"a": 4 * 10**8, "b": None}}   # b : moins de trois relevés, non rapporté


def test_signal_memoire_chemin_faux():
    s = E.signal_memoire([("a", temps()), ("b", temps(n=0, pic=None))])
    assert s["chemin_cgroupe_faux"] and s["lancements_sans_releve"] == ["b"] and s["pics_rapportes_octets"] == {}


def test_signal_memoire_unite_breve_ou_sans_isolement():
    s = E.signal_memoire([("bref", temps(duree=0.4, n=0, pic=None)), ("local", temps(n=0, pic=None, isolement=False))])
    assert not s["chemin_cgroupe_faux"] and s["pics_rapportes_octets"] == {"bref": None}


def test_epreuve_porte_le_signal_sans_en_dependre(epreuve_factice, monkeypatch):
    origine = BacFactice.verifier_lean

    def sans_releve(self, item, source, m):
        r = origine(self, item, source, m)
        r["compilation"].update(temps(n=0, pic=None))
        return r
    monkeypatch.setattr(BacFactice, "verifier_lean", sans_releve)
    r = epreuve_factice()
    assert r["memoire"]["chemin_cgroupe_faux"] and r["statut"] == "conforme" and r["conforme"]
    assert r["memoire"]["pics_rapportes_octets"] == {}


# ---- v8 : mémoire de la machine entière pour trois passages en parallèle --------------------------------------------------------

GIO = 1 << 30


def meminfo(total, dispo):
    return f"MemTotal:       {total // 1024} kB\nMemFree:        {dispo // 2048} kB\nMemAvailable:   {dispo // 1024} kB\n" \
           f"HugePages_Total:       0\n"


def test_lire_meminfo(tmp_path):
    f = tmp_path / "meminfo"
    f.write_text(meminfo(32 * GIO, 30 * GIO))
    d = E.lire_meminfo(f)
    assert d["MemTotal"] == 32 * GIO and d["MemAvailable"] == 30 * GIO and d["HugePages_Total"] == 0


def test_releve_machine(tmp_path):
    tranche, f = tmp_path / "cg" / "bacmesure00000000.slice" / "memory.peak", tmp_path / "meminfo"
    f.write_text(meminfo(32 * GIO, 30 * GIO))
    with E.ReleveMachine(tranche, f, periode=0.02) as rel:
        time.sleep(0.1)
        tranche.parent.mkdir(parents=True)
        tranche.write_text(f"{3 * GIO}\n")
        f.write_text(meminfo(32 * GIO, 26 * GIO))
        time.sleep(0.15)
        tranche.write_text(f"{2 * GIO}\n")          # (tranche recréée : le plus-haut relevé est gardé)
        time.sleep(0.1)
        tranche.write_text("")                      # retrait du cgroupe : aucun relevé, pas d'arrêt
        f.write_text("illisible")
        time.sleep(0.1)
        f.write_text(meminfo(32 * GIO, 29 * GIO))
    m = rel.resultat()
    assert m["memoire_totale_octets"] == 32 * GIO and m["dispo_avant_octets"] == 30 * GIO
    assert m["dispo_apres_octets"] == 29 * GIO and m["dispo_min_octets"] == 26 * GIO
    assert m["pic_tranche_octets"] == 3 * GIO and m["pic_tranche_echantillons"] >= 3 and m["dispo_echantillons"] >= 3


def mesure(pic=6 * GIO, n_pic=40, total=32 * GIO, avant=30 * GIO, dispo_min=25 * GIO, n_dispo=40):
    return {"memoire_totale_octets": total, "dispo_avant_octets": avant, "dispo_min_octets": dispo_min,
            "dispo_echantillons": n_dispo, "dispo_apres_octets": avant, "pic_tranche_octets": pic,
            "pic_tranche_echantillons": n_pic}


PASSAGES = [{"accepte": True, "incident_bac": None}] * 3
SIGNAL_SAIN = {"chemin_cgroupe_faux": False}


def test_juger_parallele_cas_sain():
    v = E.juger_parallele(PASSAGES, mesure(), SIGNAL_SAIN)
    assert v["compte"] and v["motifs"] == []
    assert v["calcul"] == {"baisse_dispo_octets": 5 * GIO, "dispo_min_prudente_octets": 24 * GIO,
                           "seuil_pic_octets": 16 * GIO, "seuil_dispo_octets": 8 * GIO}


@pytest.mark.parametrize("passages,m,signal,motif", [
    ([{"accepte": False, "incident_bac": None}] + PASSAGES[1:], mesure(), SIGNAL_SAIN, "item sain refusé"),
    ([{"accepte": True, "incident_bac": "mémoire"}] + PASSAGES[1:], mesure(), SIGNAL_SAIN, "incident 'mémoire'"),
    (PASSAGES, mesure(), {"chemin_cgroupe_faux": True}, "chemin du cgroupe faux"),
    (PASSAGES, mesure(pic=None, n_pic=0), SIGNAL_SAIN, "mesure de la tranche absente"),
    (PASSAGES, mesure(n_pic=2), SIGNAL_SAIN, "mesure de la tranche absente"),
    (PASSAGES, mesure(n_dispo=2), SIGNAL_SAIN, "/proc/meminfo"),
    (PASSAGES, mesure(total=None), SIGNAL_SAIN, "/proc/meminfo"),
    (PASSAGES, mesure(pic=17 * GIO, dispo_min=13 * GIO), SIGNAL_SAIN, "pic de la tranche"),
    (PASSAGES, mesure(pic=6 * GIO, dispo_min=22 * GIO), SIGNAL_SAIN, "recoupement"),          # baisse 8 Gio > 6 + 1
    (PASSAGES, mesure(avant=12 * GIO, dispo_min=7 * GIO, pic=6 * GIO), SIGNAL_SAIN, "estimée au plus bas"),
    (PASSAGES, mesure(avant=12 * GIO, dispo_min=11 * GIO, pic=5 * GIO), SIGNAL_SAIN, "estimée au plus bas"),  # pic > baisse
])
def test_juger_parallele_artefacts(passages, m, signal, motif):
    v = E.juger_parallele(passages, m, signal)
    assert not v["compte"] and any(motif in x for x in v["motifs"]), v["motifs"]


def test_juger_parallele_bornes():
    assert E.juger_parallele(PASSAGES, mesure(pic=16 * GIO, dispo_min=15 * GIO), SIGNAL_SAIN)["compte"]
    assert not E.juger_parallele(PASSAGES, mesure(pic=16 * GIO + 1, dispo_min=15 * GIO), SIGNAL_SAIN)["compte"]
    assert E.juger_parallele(PASSAGES, mesure(pic=6 * GIO, dispo_min=23 * GIO), SIGNAL_SAIN)["compte"]   # baisse = pic + 1 Gio
    assert not E.juger_parallele(PASSAGES, mesure(pic=6 * GIO, dispo_min=23 * GIO - 1), SIGNAL_SAIN)["compte"]
    assert E.juger_parallele(PASSAGES, mesure(avant=14 * GIO, dispo_min=13 * GIO, pic=6 * GIO), SIGNAL_SAIN)["compte"]
    assert not E.juger_parallele(PASSAGES, mesure(avant=14 * GIO - 1, dispo_min=13 * GIO, pic=6 * GIO),
                                 SIGNAL_SAIN)["compte"]


class BacMesure:
    """Bac factice de `mesurer` : dans une tranche réservée, chaque passage fait monter `memory.peak` de la tranche et baisser
    `MemAvailable`, puis dure 0,3 s (assez pour trois relevés au moins)."""
    pic_tranche, baisse, ecrire_tranche, meminfo, total, avant = 6 * GIO, 5 * GIO, True, None, 32 * GIO, 30 * GIO
    tranches = []

    def __init__(self, cfg, *a, **k):
        self.cfg = cfg
        BacMesure.tranches.append(cfg.tranche)

    def verifier_lean(self, item, source, m):
        if self.cfg.tranche != "system.slice":
            if BacMesure.ecrire_tranche:
                chemin = self.cfg.racine_cgroup / self.cfg.tranche / "memory.peak"
                chemin.parent.mkdir(parents=True, exist_ok=True)
                chemin.write_text(f"{BacMesure.pic_tranche}\n")
            BacMesure.meminfo.write_text(meminfo(BacMesure.total, BacMesure.avant - BacMesure.baisse))
            time.sleep(0.3)
        t = temps()
        return {"verdict": {"accepte_gardes": True}, "compilation": dict(t), "noyau": dict(t, memoire_pic_echantillonne_octets=2 * GIO),
                "incident_bac": None}


@pytest.fixture
def mesure_factice(tmp_path, monkeypatch):
    monkeypatch.setattr(E.X, "Bac", BacMesure)
    BacMesure.tranches = []
    BacMesure.meminfo = tmp_path / "meminfo"
    BacMesure.meminfo.write_text(meminfo(BacMesure.total, BacMesure.avant))
    art = tmp_path / "art"
    art.mkdir()
    (art / "sain_v1.lean").write_text("theorem etape_1 : True := trivial\n")
    cfg = E.X.Config(lean="/l", lean_path="/p", verificateur_sha256="x", mode="bac", racine_cgroup=tmp_path / "cg")
    return lambda: E.mesurer(cfg, art, meminfo=BacMesure.meminfo, jeton="0a1b2c3d")


def test_mesurer_cas_sain(mesure_factice):
    r = mesure_factice()
    assert BacMesure.tranches == ["system.slice", "bacmesure0a1b2c3d.slice"] and r["tranche"] == "bacmesure0a1b2c3d.slice"
    assert r["parallele_3_compte"], r["parallele_3_motifs"]
    m = r["releve_machine"]
    assert m["pic_tranche_octets"] == 6 * GIO and m["pic_tranche_echantillons"] >= 3
    assert m["dispo_avant_octets"] == 30 * GIO and m["dispo_min_octets"] == 25 * GIO
    assert not r["memoire"]["chemin_cgroupe_faux"] and len(r["memoire"]["pics_rapportes_octets"]) == 12
    assert len(r["suite"]) == 3 and len(r["parallele_3"]) == 3


def test_mesurer_tranche_absente(mesure_factice, monkeypatch):
    monkeypatch.setattr(BacMesure, "ecrire_tranche", False)
    r = mesure_factice()
    assert not r["parallele_3_compte"] and any("mesure de la tranche absente" in x for x in r["parallele_3_motifs"])


def test_mesurer_recoupement_manque(mesure_factice, monkeypatch):
    monkeypatch.setattr(BacMesure, "baisse", 9 * GIO)
    r = mesure_factice()
    assert not r["parallele_3_compte"] and any("recoupement" in x for x in r["parallele_3_motifs"])


# ---- artefacts et attendus ---------------------------------------------------------------------------------------------------

def test_sondes_v3_egales_aux_v2_plus_to_string():
    for c5, c6 in zip(ATT5["isolement_lean"], ATT7["isolement_lean"]):
        v2 = (ART / c5["fichier"]).read_text(encoding="utf-8")
        v3 = (ART / c6["fichier"]).read_text(encoding="utf-8")
        l2, l3 = v2.splitlines(), v3.splitlines()
        assert l3[0] == l2[0] and l3[1].startswith("-- v3 ") and l3[2].startswith("-- `String.take`")
        corps2, corps3 = l2[1:], l3[3:]
        assert len(corps2) == len(corps3)
        for a, b in zip(corps2, corps3):
            assert re.sub(r"\(([\w.]+)\.take (\d+)\)\.toString", r"(\1.take \2)", b) == a
        assert ".take " in v3 and all(re.search(r"\.take \d+\)\.toString", x) for x in corps3 if ".take " in x)


def test_attendus_v7_changements_declares():
    assert ATT7["version"] == "attendus-v7"
    assert sorted(k for k in set(ATT6) | set(ATT7) if ATT6.get(k) != ATT7.get(k)) == ["limites_lean", "note v7", "version"]
    assert ATT7["limites_lean"] == [{
        "nom": "mémoire d'un processus Lean (512M)", "fichier": "limite_memoire_lean_v1.lean", "etapes": 1,
        "resultat_compilation_attendu": "oom-kill", "incident_compilation_attendu": "mémoire",
        "compilation_code_non_nul": True, "sortie_absent": ["ALLOUE"]}]
    for groupe in ("isolement_lean", "python", "limites_python", "limites_lean", "lean", "noyau"):
        for c in ATT7[groupe]:
            assert (ART / c["fichier"]).is_file(), c["fichier"]
    assert E.ATTENDUS == "attendus-v7.json"


def test_artefact_memoire_lean_sans_mathlib_et_temoin():
    t = (ART / "limite_memoire_lean_v1.lean").read_text(encoding="utf-8")
    assert "import" not in t and "Array.replicate 200000000" in t and "ALLOUE" in t


# ---- avec la chaîne épinglée --------------------------------------------------------------------------------------------------

def chaine():
    d = json.loads(Path(CHAINE).read_text(encoding="utf-8"))
    return d["lean"], d["lean_path"]


def bac_a_sable_possible():
    if os.geteuid() != 0 or shutil.which("unshare") is None:
        return False
    return subprocess.run(["unshare", "--mount", "--net", "true"], capture_output=True).returncode == 0



sans_bac_a_sable = pytest.mark.skipif(not bac_a_sable_possible(),
                                      reason="bac à sable de montage impossible (root et unshare exigés) : sauté")


def compiler_dans_le_bac_a_sable(fichier, tmp_path):
    """Compile comme le bac (même commande, même environnement), sans que les tentatives touchent l'hôte."""
    lean, lp = chaine()
    racine_chaine = os.path.commonpath([lean, lp.split(":")[0]])
    sortie = tmp_path / "sortie"
    sortie.mkdir()
    p = subprocess.run(["bash", str(COMPILER), racine_chaine, lean, lp, str(fichier), str(sortie)],
                       capture_output=True, text=True, timeout=300)
    return p.returncode, (sortie / "compilation.out").read_text(encoding="utf-8")


@avec_chaine
@sans_bac_a_sable
@pytest.mark.parametrize("cas", ATT5["isolement_lean"], ids=lambda c: c["fichier"])
def test_sondes_v2_ne_compilent_pas_cause(cas, tmp_path):
    """Cause établie : l'élaboration de `tenter` échoue (String.Slice), chaque `#eval` est abandonné ; code 1, aucune tentative."""
    code, out = compiler_dans_le_bac_a_sable(ART / cas["fichier"], tmp_path)
    assert code == 1
    assert "String.Slice" in out and "but is expected to have type" in out and "ISOLEMENT" not in out
    assert "depends on the 'sorry' axiom" in out


@avec_chaine
@sans_bac_a_sable
@pytest.mark.parametrize("cas", ATT7["isolement_lean"], ids=lambda c: c["fichier"])
def test_sondes_v3_rendent_leurs_tentatives(cas, tmp_path):
    code, out = compiler_dans_le_bac_a_sable(ART / cas["fichier"], tmp_path)
    assert code == 0, out[:2000]
    assert set(E.tentatives(out)) == set(cas["tentatives"])
    if cas.get("sain"):
        assert E.sain_vivant(cas, out)
