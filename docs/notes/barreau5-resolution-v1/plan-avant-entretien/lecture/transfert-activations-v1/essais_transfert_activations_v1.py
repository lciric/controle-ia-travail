"""Essais du transfert des activations du barreau 5 — v1 : chaque garde vue verte sur un cas sain et rouge sur un artefact
(R5). Processeur seul, aucun réseau, aucune dépense : les dépôts git sont fabriqués dans un dossier temporaire, la
minuterie joue contre un faux `curl`. Lancer depuis la racine du dépôt :
  PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider \
    docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/transfert-activations-v1/essais_transfert_activations_v1.py
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
RACINE_DEPOT = ICI.parents[5]
sys.path.insert(0, str(ICI))
import transfert_activations_v1 as ta  # noqa: E402

RUN = "20261122-200000-b5f-lecture"
FIGE = "c76e79169"


def sh(*a, cwd=None):
    return subprocess.run(list(a), cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def h(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def fabriquer_activations(n_series=3, n_actions=25):
    """Faux inventaire et faux fichiers (octets quelconques : aucune activation réelle)."""
    fichiers = {}
    for s in range(n_series):
        for c in (7, 15, 23):
            for t in range(n_actions):
                chemin = f"activations/serie-{s}/c{c}/tache{t % 5}__p{t:03d}.npy"
                fichiers[chemin] = f"{s}-{c}-{t}".encode() * 7
    inv = {"fichiers": [{"chemin": k, "octets": len(v), "sha256": h(v)} for k, v in sorted(fichiers.items())]}
    return fichiers, inv


@pytest.fixture
def depot(tmp_path):
    """Dépôt distant nu, clone, commit prouvé sur la branche de lecture ; second commit hors de cette branche."""
    nu = tmp_path / "nu.git"
    sh("git", "init", "-q", "--bare", str(nu))
    d = tmp_path / "clone"
    sh("git", "init", "-q", str(d))
    sh("git", "-C", str(d), "config", "user.email", "e@x")
    sh("git", "-C", str(d), "config", "user.name", "e")
    sh("git", "-C", str(d), "remote", "add", "origin", str(nu))
    fichiers, inv = fabriquer_activations()
    o = json.dumps(inv, sort_keys=True).encode()
    base = d / "donnees" / RUN
    base.mkdir(parents=True)
    (base / "inventaire-activations.json").write_bytes(o)
    (base / "inventaire-activations.json.sha256").write_text(f"{h(o)}  inventaire-activations.json\n")
    (d / "traces-b5f-lecture").mkdir()
    final = {"run_id": RUN, "fichiers": [{"chemin": f"donnees/{RUN}/inventaire-activations.json", "octets": len(o),
                                          "sha256": h(o)}]}
    (d / "traces-b5f-lecture" / "inventaire-final.json").write_text(json.dumps(final))
    sh("git", "-C", str(d), "add", "-A")
    sh("git", "-C", str(d), "commit", "-q", "-m", "prouve")
    commit = sh("git", "-C", str(d), "rev-parse", "HEAD")
    sh("git", "-C", str(d), "push", "-q", "origin", f"HEAD:refs/heads/{ta.BRANCHE_LECTURE}")
    sh("git", "-C", str(d), "fetch", "-q", "origin")
    return d, commit, fichiers, inv


def commit_artefact(d: Path, modifier) -> str:
    """Commit local (non poussé, ou poussé selon l'artefact) après une modification."""
    modifier(d)
    sh("git", "-C", str(d), "add", "-A")
    sh("git", "-C", str(d), "commit", "-q", "-m", "artefact")
    return sh("git", "-C", str(d), "rev-parse", "HEAD")


# --- accord ------------------------------------------------------------------------------------------------------------

LIGNE = ("| GO-2026-11-22-117 | 2026-11-22 | calcul | Barreau 5 | plafond 33 USD (9 + 24) | 2026-11-30 | Lazar | accords |")


def test_accord_sain():
    assert ta.exiger_accord(LIGNE, "2026-11-22")["echeance"] == "2026-11-30"


@pytest.mark.parametrize("registre,jour", [
    (LIGNE, "2026-12-01"),                                        # après l'échéance
    (LIGNE.replace("| calcul |", "| dépôt distant |"), "2026-11-22"),
    (LIGNE.replace("| Lazar |", "| mère |"), "2026-11-22"),
    (LIGNE + "\n" + LIGNE, "2026-11-22"),                         # en double
    ("", "2026-11-22"),                                           # absente
])
def test_accord_artefacts(registre, jour):
    with pytest.raises(ta.Refus):
        ta.exiger_accord(registre, jour)


def test_accord_registre_reel_lisible():
    """La ligne réelle de l'accord est lue (sans afficher le registre) et admise aujourd'hui ou refusée hors période."""
    reg = (RACINE_DEPOT / "registres" / "go.md").read_text(encoding="utf-8")
    a = ta.exiger_accord(reg, "2026-11-25")
    assert a["accord"] == ta.ACCORD
    with pytest.raises(ta.Refus):
        ta.exiger_accord(reg, "2026-12-14")


# --- preuve de l'inventaire ----------------------------------------------------------------------------------------------

def test_preuve_saine(depot):
    d, commit, fichiers, inv = depot
    p = ta.preuve_inventaire(d, commit, RUN)
    assert len(p["fichiers"]) == len(inv["fichiers"]) and p["commit"] == commit


def test_preuve_commit_hors_branche(depot):
    d, commit, _, _ = depot
    c2 = commit_artefact(d, lambda d: (d / "x.txt").write_text("x"))
    with pytest.raises(ta.Refus, match="absent de la branche"):
        ta.preuve_inventaire(d, c2, RUN)


def _pousser(d, c):
    sh("git", "-C", str(d), "push", "-q", "-f", "origin", f"{c}:refs/heads/{ta.BRANCHE_LECTURE}")
    sh("git", "-C", str(d), "fetch", "-q", "origin")


def test_preuve_compagnon_discordant(depot):
    d, _, _, _ = depot
    c2 = commit_artefact(d, lambda d: (d / "donnees" / RUN / "inventaire-activations.json.sha256").write_text("0" * 64 + "  x\n"))
    _pousser(d, c2)
    with pytest.raises(ta.Refus, match="compagnon"):
        ta.preuve_inventaire(d, c2, RUN)


def test_preuve_inventaire_final_discordant(depot):
    d, _, _, _ = depot
    def m(d):
        p = d / "traces-b5f-lecture" / "inventaire-final.json"
        x = json.loads(p.read_text()); x["fichiers"][0]["sha256"] = "1" * 64; p.write_text(json.dumps(x))
    c2 = commit_artefact(d, m)
    _pousser(d, c2)
    with pytest.raises(ta.Refus, match="inventaire final"):
        ta.preuve_inventaire(d, c2, RUN)


def test_preuve_chemin_hors_forme(depot):
    d, _, _, inv = depot
    def m(d):
        x = json.loads(json.dumps(inv)); x["fichiers"][0]["chemin"] = "lecture/scores/x-pli0.json"
        o = json.dumps(x, sort_keys=True).encode()
        (d / "donnees" / RUN / "inventaire-activations.json").write_bytes(o)
        (d / "donnees" / RUN / "inventaire-activations.json.sha256").write_text(f"{h(o)}  inventaire-activations.json\n")
        f = d / "traces-b5f-lecture" / "inventaire-final.json"
        y = json.loads(f.read_text()); y["fichiers"][0].update(sha256=h(o), octets=len(o)); f.write_text(json.dumps(y))
    c2 = commit_artefact(d, m)
    _pousser(d, c2)
    with pytest.raises(ta.Refus, match="hors de la forme"):
        ta.preuve_inventaire(d, c2, RUN)


@pytest.mark.parametrize("commit,run", [("abc", RUN), ("a" * 40, "20261122-200000-b5f-repetition")])
def test_preuve_arguments_refuses(depot, commit, run):
    with pytest.raises(ta.Refus):
        ta.preuve_inventaire(depot[0], commit, run)


def test_inventaire_en_double():
    x = {"fichiers": [{"chemin": "activations/a/c7/t__p001.npy", "octets": 3, "sha256": "a" * 64}] * 2}
    with pytest.raises(ta.Refus, match="double"):
        ta.lire_inventaire(json.dumps(x).encode())


# --- vérification de la copie -----------------------------------------------------------------------------------------

def _copie(tmp_path, fichiers):
    dossier = tmp_path / "volume" / RUN
    for c, b in fichiers.items():
        p = dossier / c
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b)
    return dossier


def _preuve(inv):
    return {"run_id": RUN, "commit": "c" * 40, "inventaire_sha256": "d" * 64, "fichiers": inv["fichiers"]}


def test_copie_saine(tmp_path):
    fichiers, inv = fabriquer_activations()
    c = ta.verifier_copie(_preuve(inv), _copie(tmp_path, fichiers))
    assert c["complet"] and c["comptes"]["conforme"] == len(fichiers) and c["en_trop"] == 0


@pytest.mark.parametrize("artefact,statut", [("manquant", "manquant"), ("octet", "empreinte"), ("taille", "taille"),
                                             ("lien", "lien"), ("trop", None)])
def test_copie_artefacts(tmp_path, artefact, statut):
    fichiers, inv = fabriquer_activations()
    dossier = _copie(tmp_path, fichiers)
    cible = dossier / inv["fichiers"][4]["chemin"]
    if artefact == "manquant":
        cible.unlink()
    elif artefact == "octet":
        b = bytearray(cible.read_bytes()); b[0] ^= 1; cible.write_bytes(bytes(b))
    elif artefact == "taille":
        cible.write_bytes(cible.read_bytes() + b"x")
    elif artefact == "lien":
        autre = tmp_path / "ailleurs.npy"; autre.write_bytes(cible.read_bytes()); cible.unlink(); cible.symlink_to(autre)
    else:
        (dossier / "activations" / "intrus.npy").write_bytes(b"x")
    c = ta.verifier_copie(_preuve(inv), dossier)
    assert not c["complet"]
    if statut:
        assert c["comptes"][statut] == 1
    else:
        assert c["en_trop"] == 1


def test_copie_selection_hors_inventaire(tmp_path):
    fichiers, inv = fabriquer_activations()
    with pytest.raises(ta.Refus, match="hors de l'inventaire"):
        ta.verifier_copie(_preuve(inv), _copie(tmp_path, fichiers), ["activations/zz/c15/t__p001.npy"])


def test_verifier_copie_bibliotheque_standard():
    """La sous-commande qui tourne sur le serveur n'importe rien hors de la bibliothèque standard au chargement."""
    arbre = ast.parse((ICI / "transfert_activations_v1.py").read_text(encoding="utf-8"))
    hauts = [n for n in arbre.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    noms = {a.name.split(".")[0] for n in hauts if isinstance(n, ast.Import) for a in n.names} \
        | {n.module.split(".")[0] for n in hauts if isinstance(n, ast.ImportFrom) and n.module}
    assert noms <= {"__future__", "hashlib", "json", "math", "re", "subprocess", "sys", "datetime", "pathlib"}


# --- sélections : égales au calcul figé ------------------------------------------------------------------------------

def _garde_figee():
    """`garde_des_activations` telle qu'au commit figé, exécutée hors de son module (sans torch), avec le générateur du
    manifeste figé ; `empreinte` et `sceller` remplacés par des équivalents sans effet de bord."""
    src = sh("git", "-C", str(RACINE_DEPOT), "show", f"{FIGE}:src/controle_ia/barreau5_familles/relecture_v1.py")
    man = sh("git", "-C", str(RACINE_DEPOT), "show", f"{FIGE}:src/controle_ia/manifeste.py")
    ns = {"Path": Path, "json": json, "np": np, "empreinte": lambda p: h(Path(p).read_bytes()), "sceller": lambda p: "x"}
    for texte, nom in ((man, "generateur"), (src, "garde_des_activations")):
        f = next(n for n in ast.parse(texte).body if isinstance(n, ast.FunctionDef) and n.name == nom)
        code = ast.get_source_segment(texte, f)
        if nom == "generateur":
            ns["GardeArret"] = RuntimeError
        exec(code, ns)
    return ns["garde_des_activations"], ns["generateur"]


def _manifeste(entropie=123456789):
    ss = np.random.SeedSequence(entropie, spawn_key=(77,))
    return {"graines": {"b5f/tirages/garde-activations": {"entropie": str(entropie), "spawn_key": ["77"],
                                                         "etat_controle": [int(x) for x in ss.generate_state(2)]}}}


@pytest.mark.parametrize("regle", ["couche_15", "une_sur_dix"])
def test_selection_egale_au_calcul_fige(tmp_path, regle):
    garde, generateur = _garde_figee()
    fichiers, inv = fabriquer_activations(n_series=4, n_actions=40)
    sorties = tmp_path / "sorties"
    for c, b in fichiers.items():
        p = sorties / c; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(b)
    m = _manifeste()
    garde(sorties / "activations", sorties, regle, m["graines"])
    attendu = json.loads((sorties / "garde-activations.json").read_text())["fichiers"]
    inv_fige = json.loads((sorties / "inventaire-activations.json").read_text())
    assert inv_fige == inv                                           # même forme d'inventaire que celle que lit la preuve
    assert sorted(ta.selection(regle, _preuve(inv), m)) == sorted(attendu)
    assert 0 < len(attendu) < len(inv["fichiers"])


def test_selection_graine_alteree():
    _, inv = fabriquer_activations()
    m = _manifeste(); m["graines"]["b5f/tirages/garde-activations"]["etat_controle"][0] += 1
    with pytest.raises(ta.Refus, match="graine"):
        ta.selection("une_sur_dix", _preuve(inv), m)


@pytest.mark.parametrize("regle,m", [("trois_couches", None), ("une_sur_dix", None), ("une_sur_dix", {"graines": {}})])
def test_selection_artefacts(regle, m):
    _, inv = fabriquer_activations()
    with pytest.raises(ta.Refus):
        ta.selection(regle, _preuve(inv), m)


# --- corps et commandes -----------------------------------------------------------------------------------------------

def test_corps_sains():
    v = ta.corps_volume()
    assert v["size"] == 200 and v["location"] == "hel1" and v["labels"]["accord"] == ta.ACCORD
    s = ta.corps_serveur("cx23", "1", "2", "3")
    assert s["volumes"] == [1] and s["location"] == "hel1" and s["labels"]["piece"] == ta.NOM_SERVEUR


@pytest.mark.parametrize("args", [("cx53", "1", "2", "3"), ("cx23", "x", "2", "3"), ("cx23", "1", "", "3")])
def test_corps_serveur_artefacts(args):
    with pytest.raises(ta.Refus):
        ta.corps_serveur(*args)


def test_commande_ne_porte_que_le_nom_du_jeton(monkeypatch):
    monkeypatch.setenv("HCLOUD_TOKEN", "SENTINELLE-SECRETE")
    c = ta.commande_hetzner("POST", "/volumes", ta.corps_volume())
    assert "$HCLOUD_TOKEN" in c and "SENTINELLE" not in c and "-K -" in c


def test_reduire_liste_retire_les_cles():
    brut = {"instances": [{"id": 5, "label": "b5f-lecture-v1", "actual_status": "stopped",
                           "extra_env": [["GH_TOKEN", "SENTINELLE"]], "onstart": "SENTINELLE", "dph_total": 1.1}]}
    r = ta.reduire_liste("vast", brut)
    assert "SENTINELLE" not in json.dumps(r) and r[0]["id"] == 5
    with pytest.raises(ta.Refus):
        ta.reduire_liste("autre", brut)


SERVEUR = {"id": 42, "name": ta.NOM_SERVEUR, "labels": dict(ta.LABELS, piece=ta.NOM_SERVEUR), "status": "running"}


def test_detruire_serveur_sain():
    assert ta.commande_detruire_serveur([SERVEUR, {"id": 7, "name": "autre"}], "42").count("DELETE") == 1


@pytest.mark.parametrize("liste,ident", [([SERVEUR], "43"), ([SERVEUR, SERVEUR], "42"), ([SERVEUR], "4x"),
                                         ([dict(SERVEUR, name="lean")], "42"),
                                         ([dict(SERVEUR, labels={"piece": ta.NOM_SERVEUR})], "42")])
def test_detruire_serveur_artefacts(liste, ident):
    with pytest.raises(ta.Refus):
        ta.commande_detruire_serveur(liste, ident)


def _constat(inv, **k):
    c = {"run_id": RUN, "commit": "c" * 40, "inventaire_sha256": "d" * 64, "portee": "inventaire",
         "selection_sha256": None, "attendus": len(inv["fichiers"]),
         "comptes": {"conforme": len(inv["fichiers"])}, "en_trop": 0, "complet": True}
    c.update(k)
    return c


VAST = [{"id": 900, "label": ta.ETIQUETTE_VAST, "actual_status": "stopped"}, {"id": 58936096, "label": "x"}]


def test_detruire_vast_sain():
    _, inv = fabriquer_activations()
    c = ta.commande_detruire_vast(VAST, "900", _preuve(inv), _constat(inv))
    assert c == f"GO_ID={ta.ACCORD} vastai destroy instance 900 -y"


@pytest.mark.parametrize("ident,modif", [("58936096", {}), ("900", {"complet": False}), ("900", {"commit": "e" * 40}),
                                         ("900", {"inventaire_sha256": "f" * 64}), ("900", {"portee": "selection"}),
                                         ("900", {"comptes": {"conforme": 1}})])
def test_detruire_vast_artefacts(ident, modif):
    _, inv = fabriquer_activations()
    with pytest.raises(ta.Refus):
        ta.commande_detruire_vast(VAST, ident, _preuve(inv), _constat(inv, **modif))


def test_detruire_vast_repli():
    _, inv = fabriquer_activations()
    sel = ta.selection("une_sur_dix", _preuve(inv), _manifeste())
    cs = _constat(inv, portee="selection", attendus=len(sel), comptes={"conforme": len(sel)},
                  selection_sha256=h("\n".join(sorted(sel)).encode()))
    ok = ta.commande_detruire_vast(VAST, "900", _preuve(inv), cs, (sel, "2026-11-23T10:00:00Z", "2026-11-26T10:00:01Z"))
    assert "destroy instance 900" in ok
    with pytest.raises(ta.Refus, match="délai"):              # repli avant le délai : refusé
        ta.commande_detruire_vast(VAST, "900", _preuve(inv), cs, (sel, "2026-11-23T10:00:00Z", "2026-11-25T10:00:00Z"))
    with pytest.raises(ta.Refus, match="autre sélection"):    # constat d'une autre sélection
        ta.commande_detruire_vast(VAST, "900", _preuve(inv), cs, (sel[:-1], "2026-11-23T10:00:00Z", "2026-11-27T10:00:00Z"))


def test_verifier_absence():
    assert "prouvée" in ta.verifier_absence([{"id": 7}], "42", "7")
    with pytest.raises(ta.Refus, match="toujours présent"):
        ta.verifier_absence([{"id": 7}, {"id": 42}], "42", "7")
    with pytest.raises(ta.Refus, match="témoin"):
        ta.verifier_absence([], "42", "7")


# --- dépense et délai --------------------------------------------------------------------------------------------------

BASE = {"volume_cree": "2026-11-21T12:00:00Z", "echeance_garde": "2026-12-21T12:00:00Z"}


def test_garde_depense_pire_cas_du_devis():
    """Devis v2, objet de contrôle vrai par construction : un mois et trois séances de 24 heures sur ccx13 → 23,56 USD."""
    r = ta.garde_depense(dict(BASE, seances=[{"type": "ccx13", "heures": 24}] * 3))
    assert r["cumul_projete_usd"] == 23.56 and r["verdict"] == "sous le plafond"


def test_garde_depense_attendu_du_devis():
    r = ta.garde_depense(dict(BASE, seances=[{"type": "cx23", "heures": 12}], nouvelle_seance="cx23"))
    assert r["cumul_projete_usd"] == 17.33 and r["nouvelle_seance"] == "admise"


@pytest.mark.parametrize("etat", [
    dict(BASE, seances=[{"type": "ccx13", "heures": 24}] * 4),                      # quatrième séance
    dict(BASE, seances=[{"type": "ccx13", "heures": 720}]),                         # serveur oublié un mois
    dict(BASE, echeance_garde="2027-01-21T12:00:00Z"),                              # deuxième mois sans ligne
    dict(BASE, seances=[{"type": "cx23", "heures": 6}], postes_vast={"usd": 8.64}),  # 72 h d'arrêt comptées ici
])
def test_garde_depense_coupures(etat):
    with pytest.raises(ta.Coupure):
        ta.garde_depense(etat)


def test_garde_depense_plafond_releve_refuse():
    with pytest.raises(ta.Refus):
        ta.garde_depense(dict(BASE, plafond_usd=30))


def test_echeance_vast():
    assert ta.echeance_vast("2026-11-23T10:00:00Z", "2026-11-26T09:00:00Z")["verdict"] == "dans le delai"
    assert ta.echeance_vast("2026-11-23T10:00:00Z", "2026-11-26T10:00:00Z")["verdict"] == "depasse"
    with pytest.raises(ta.Refus):
        ta.echeance_vast("2026-11-23T10:00:00Z", "2026-11-22T10:00:00Z")
    with pytest.raises(ta.Refus):
        ta.echeance_vast("2026-11-23 10:00", "2026-11-24T10:00:00Z")


def test_ligne_de_commande_n_ecrase_jamais(tmp_path):
    p = tmp_path / "x.json"; p.write_text("{}")
    with pytest.raises(ta.Refus, match="R12"):
        ta._ecrire_neuf(str(p), "{}")


# --- minuterie, contre un faux curl ----------------------------------------------------------------------------------

def _faux_curl(tmp_path, reponses_get):
    """Faux `curl` : journalise méthode et URL (et ce qu'il reçoit sur l'entrée standard, pour chercher le jeton dans ses
    arguments) ; GET rend la suite donnée, DELETE rend 204."""
    b = tmp_path / "bin"; b.mkdir()
    etat = tmp_path / "gets"; etat.write_text("\n".join(reponses_get) + "\n")
    (b / "curl").write_text(f"""#!/usr/bin/env bash
m=GET; u=""
while [ $# -gt 0 ]; do case "$1" in -X) m="$2"; shift;; http*) u="$1";; esac; shift; done
echo "$m $u ARGS:$*" >> {tmp_path}/appels
cat > /dev/null
if [ "$m" = GET ]; then r=$(head -n 1 {etat}); sed -i 1d {etat}; printf '%s' "${{r:-200}}"; else printf 204; fi
""")
    (b / "curl").chmod(0o755)
    return b


def _minuterie(tmp_path, args, env_plus):
    env = dict(os.environ, PATH=f"{_faux_curl(tmp_path, env_plus.pop('_gets', ['200', '404']))}:{os.environ['PATH']}",
               MINUTERIE_PAS_S="0", API_HETZNER="https://faux.invalid/v1", HCLOUD_TOKEN="SENTINELLE-SECRETE")
    env.update(env_plus)
    return subprocess.run(["bash", str(ICI / "minuterie_serveur_v1.sh"), *args], env=env, capture_output=True, text=True,
                          timeout=60)


def test_minuterie_saine(tmp_path):
    j = tmp_path / "j.txt"
    r = _minuterie(tmp_path, ["42", str(int(time.time()) + 1), str(j)], {})
    assert r.returncode == 0
    appels = (tmp_path / "appels").read_text()
    assert "DELETE https://faux.invalid/v1/servers/42" in appels and "404" in j.read_text()
    assert "SENTINELLE" not in appels and "SENTINELLE" not in j.read_text()


def test_minuterie_ne_juge_pas_par_le_code(tmp_path):
    """Artefact : DELETE répond 204 mais le serveur reste (GET 200) : pas de « fin », essais épuisés, code 4."""
    j = tmp_path / "j.txt"
    r = _minuterie(tmp_path, ["42", str(int(time.time())), str(j)], {"_gets": ["200", "200", "200"],
                                                                   "MINUTERIE_ESSAIS_MAX": "3"})
    assert r.returncode == 4 and "non prouvé" in j.read_text()


@pytest.mark.parametrize("args,env", [(["4x", "1", "j"], {}), (["42", "x", "j"], {}), (["42", "1", ""], {}),
                                      (["42", str(int(time.time()) + 25 * 3600), "j"], {}),
                                      (["42", "1", "j"], {"HCLOUD_TOKEN": ""})])
def test_minuterie_refus(tmp_path, args, env):
    args = [a if a != "j" else str(tmp_path / "j.txt") for a in args]
    r = _minuterie(tmp_path, args, dict(env))
    assert r.returncode == 2 and "REFUS" in r.stdout
    assert not (tmp_path / "appels").exists()


# --- clé SSH jetable, pare-feu, adresse de copie ------------------------------------------------------------------------

CLE = "ssh-ed25519 " + "A" * 68 + " b5f-transfert-v1"


def test_corps_cle_ssh():
    assert ta.corps_cle_ssh(CLE + "\n")["public_key"] == CLE
    for artefact in ("-----BEGIN OPENSSH PRIVATE KEY-----\nabc", "ssh-rsa " + "A" * 68, ""):
        with pytest.raises(ta.Refus):
            ta.corps_cle_ssh(artefact)


def test_corps_pare_feu():
    r = ta.corps_pare_feu("203.0.113.9")["rules"]
    assert r == [{"direction": "in", "protocol": "tcp", "port": "22", "source_ips": ["203.0.113.9/32"]}]
    for artefact in ("0.0.0.0", "10.1.2.3", "203.0.113", "203.0.113.09", "a.b.c.d"):
        with pytest.raises(ta.Refus):
            ta.corps_pare_feu(artefact)


import demande_rsync_vast_v1 as dr  # noqa: E402


class FauxClient:
    def __init__(self, reponse):
        self.reponse, self.appels = reponse, []

    def put(self, chemin, json_data=None, **k):
        self.appels.append((chemin, json_data))
        r = self.reponse

        class R:
            def raise_for_status(self):
                pass

            def json(self):
                return r
        return R()


def test_demande_rsync_saine(monkeypatch):
    monkeypatch.delenv("SONDE", raising=False)
    c = FauxClient({"success": True, "src_addr": "203.0.113.5", "src_port": 41022, "jeton": "SENTINELLE"})
    sortie = dr.principal(["900", RUN, "/mnt/HC_Volume_123"], client=c)
    assert "SENTINELLE" not in sortie and "vastai_kaalia@203.0.113.5::C.900//root/b5f-lecture-v1/depot/donnees/" in sortie
    assert c.appels[0][1]["src_id"] == "C.900" and c.appels[0][1]["dst_id"] == "local"
    assert c.appels[0][1]["dst_path"].startswith("/mnt/HC_Volume_123/b5f-activations-v1/")


def test_demande_rsync_sonde(monkeypatch):
    monkeypatch.setenv("SONDE", "1")
    c = FauxClient({"success": True, "src_addr": "h.example", "src_port": "22"})
    assert "inventaire-activations.json" in dr.principal(["900", RUN, "/mnt/HC_Volume_1"], client=c)


@pytest.mark.parametrize("argv,reponse", [
    (["90x", RUN, "/mnt/HC_Volume_1"], {}),
    (["900", "x", "/mnt/HC_Volume_1"], {}),
    (["900", RUN, "/root"], {}),
    (["900", RUN, "/mnt/HC_Volume_1"], {"success": False, "msg": "SENTINELLE"}),
    (["900", RUN, "/mnt/HC_Volume_1"], {"success": True, "src_addr": "a b;rm", "src_port": 22}),
    (["900", RUN, "/mnt/HC_Volume_1"], {"success": True, "src_addr": "h", "src_port": 70000}),
])
def test_demande_rsync_artefacts(monkeypatch, argv, reponse):
    monkeypatch.delenv("SONDE", raising=False)
    with pytest.raises(dr.Refus) as e:
        dr.principal(argv, client=FauxClient(reponse))
    assert "SENTINELLE" not in str(e.value)
