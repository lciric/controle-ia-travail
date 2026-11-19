"""Essais de l'enveloppe de conservation des réponses brutes v1 (lanceur v9, additif v2i ; règle de Lazar R-3661 : « il faut
TOUJOURS récupérer ce qui est récupérable »). Cas sain (réponse conservée octet pour octet, identique à la réponse rendue,
en-têtes, lot, numéros d'appel exclusifs, passage dans la garde de crédit v5), artefacts (dossier absent, relatif, lien, non
inscriptible, étiquette ou usage refusés : rien n'est lancé ; écriture impossible après l'appel : appel arrêté, réponse non
rendue, coût déclaré compté) et mutations (conservation sautée, erreur avalée). Commandes factices locales seulement : aucun
appel réel, aucune clé."""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import threading
from pathlib import Path

import pytest

sys.dont_write_bytecode = True
RACINE = Path(__file__).resolve().parents[1]
CHEMIN = RACINE / "scripts" / "enveloppe_conservation_reponses_v1.py"
GARDE = RACINE / "scripts" / "garde_credit_relais_v5.py"
PY = sys.executable

# Commande factice : lit la consigne, écrit sur la sortie d'erreur, imprime une réponse (octets non UTF-8 compris) puis la
# ligne JSON du contrat ; en option, retire le dossier de conservation pendant l'appel (écriture impossible ensuite).
FAUSSE_COMMANDE = r'''
import json, os, shutil, sys
consigne = sys.stdin.buffer.read()
sys.stderr.buffer.write(b"diagnostic: lu " + str(len(consigne)).encode() + b" octets\n")
if os.environ.get("RETIRER"):
    shutil.rmtree(os.environ["RETIRER"])
if os.environ.get("MARQUEUR"):
    open(os.environ["MARQUEUR"], "w").close()
sys.stdout.buffer.write(b"\xff\xfe octets bruts \xe9\n")
cout = float(os.environ.get("COUT", "0.42"))
sys.stdout.buffer.write((json.dumps({"texte": "fiche é " + consigne.decode("utf-8", "replace")[:20], "cout_usd": cout,
                                     "modele_servi": "modele-essai"}, ensure_ascii=False) + "\n").encode("utf-8"))
sys.exit(int(os.environ.get("CODE", "0")))
'''


def _commande(tmp_path):
    p = tmp_path / "fausse_commande.py"
    p.write_text(FAUSSE_COMMANDE, encoding="utf-8")
    return [PY, "-I", "-B", str(p)]


def _env(**k):
    e = {"PATH": "/usr/local/bin:/usr/bin:/bin", "LANG": "C.UTF-8", "ROLE_POLE": "proposeur_ideation",
         "MODELE_DEMANDE_POLE": "modele-essai", "PLAFOND_SESSION_USD": "6.05"}
    e.update({n: str(v) for n, v in k.items()})
    return e


def _jouer(tmp_path, dossier, etiquette="argon", consigne=b"Lot 3 sur 11 du catalogue des m\xc3\xa9canismes", script=CHEMIN, **env):
    nue = subprocess.run(_commande(tmp_path), input=consigne, capture_output=True, env=_env(**{k: v for k, v in env.items()
                                                                                               if k not in ("RETIRER", "MARQUEUR")}))
    p = subprocess.run([PY, "-I", "-B", str(script), str(dossier), etiquette, "--"] + _commande(tmp_path), input=consigne,
                       capture_output=True, env=_env(**env))
    return nue, p


def _appels(dossier):
    return sorted(d for d in Path(dossier).iterdir() if d.is_dir())


def test_cas_sain_reponse_conservee_identique_a_la_reponse_rendue(tmp_path):
    dossier = tmp_path / "conservation"
    dossier.mkdir()
    nue, p = _jouer(tmp_path, dossier)
    assert p.returncode == 0 and p.stdout == nue.stdout and p.stderr == nue.stderr      # rendu tel quel
    (appel,) = _appels(dossier)
    assert appel.name == "argon-appel-0001"
    rep = list(appel.glob("*-reponse.bin"))
    err = list(appel.glob("*-erreur.bin"))
    ent = list(appel.glob("*-entetes.json"))
    assert len(rep) == len(err) == len(ent) == 1
    assert rep[0].read_bytes() == p.stdout and err[0].read_bytes() == p.stderr          # octet pour octet
    assert rep[0].name.startswith("argon-appel-0001-lot-03-") and rep[0].name.endswith("Z-reponse.bin")
    e = json.loads(ent[0].read_text(encoding="utf-8"))
    assert e["reponse"]["sha256"] == hashlib.sha256(p.stdout).hexdigest() and e["reponse"]["octets"] == len(p.stdout)
    assert e["erreur"]["sha256"] == hashlib.sha256(p.stderr).hexdigest()
    assert (e["lot"], e["appel"], e["etiquette"], e["code_commande"]) == ("03", 1, "argon", 0)
    assert e["environnement_lu"] == {"ROLE_POLE": "proposeur_ideation", "MODELE_DEMANDE_POLE": "modele-essai", "PLAFOND_SESSION_USD": "6.05"}
    assert e["cout_declare_usd"] == pytest.approx(0.42) and e["consigne"]["octets"] > 0
    assert not list(appel.glob(".*"))                                                    # aucun temporaire laissé


def test_juge_sans_lot_et_code_de_la_commande_rendu(tmp_path):
    dossier = tmp_path / "c"
    dossier.mkdir()
    nue, p = _jouer(tmp_path, dossier, etiquette="carbon", consigne=b"fiche a juger", CODE=7)
    assert p.returncode == 7 and p.stdout == nue.stdout
    (appel,) = _appels(dossier)
    assert list(appel.glob("carbon-appel-0001-lot-sans-lot-*-reponse.bin"))
    assert json.loads(next(appel.glob("*-entetes.json")).read_text())["code_commande"] == 7


def test_numeros_d_appel_exclusifs_sous_appels_simultanes(tmp_path):
    dossier = tmp_path / "c"
    dossier.mkdir()
    sorties = []

    def un():
        sorties.append(_jouer(tmp_path, dossier, etiquette="astra")[1])
    fils = [threading.Thread(target=un) for _ in range(6)]
    for f in fils:
        f.start()
    for f in fils:
        f.join()
    assert all(p.returncode == 0 for p in sorties)
    noms = [d.name for d in _appels(dossier)]
    assert noms == [f"astra-appel-{n:04d}" for n in range(1, 7)]
    for d in _appels(dossier):
        assert len(list(d.glob("*-entetes.json"))) == 1


def test_dans_la_garde_de_credit_v5_la_reponse_est_rendue_et_conservee(tmp_path):
    dossier, arrets = tmp_path / "c", tmp_path / "arrets"
    dossier.mkdir()
    consigne = b"Lot 11 sur 11 du catalogue"
    nue = subprocess.run(_commande(tmp_path), input=consigne, capture_output=True, env=_env())
    p = subprocess.run([PY, "-I", "-B", str(GARDE), str(arrets), "argon", "--", PY, "-I", "-B", str(CHEMIN), str(dossier), "argon",
                        "--"] + _commande(tmp_path), input=consigne, capture_output=True, env=_env())
    assert p.returncode == 0 and p.stdout == nue.stdout
    (appel,) = _appels(dossier)
    assert next(appel.glob("*-lot-11-*-reponse.bin")).read_bytes() == nue.stdout


@pytest.mark.parametrize("cas", ["absent", "relatif", "lien", "fichier", "etiquette", "usage"])
def test_artefacts_refus_avant_tout_appel(tmp_path, cas):
    marqueur = tmp_path / "commande-lancee"
    vrai = tmp_path / "vrai"
    vrai.mkdir()
    dossier = {"absent": tmp_path / "absent", "relatif": Path("relatif"), "lien": tmp_path / "lien",
               "fichier": tmp_path / "fichier", "etiquette": vrai, "usage": vrai}[cas]
    if cas == "lien":
        dossier.symlink_to(vrai)
    if cas == "fichier":
        dossier.write_text("x")
    argv = [PY, "-I", "-B", str(CHEMIN), str(dossier), "Argon!" if cas == "etiquette" else "argon",
            "++" if cas == "usage" else "--"] + _commande(tmp_path)
    p = subprocess.run(argv, input=b"Lot 1 sur 11 du catalogue", capture_output=True, env=_env(MARQUEUR=marqueur))
    assert p.returncode == 2 and not marqueur.exists()                                   # rien n'est lancé
    o = json.loads(p.stdout.decode().strip().splitlines()[-1])
    assert o["texte"] == "" and o["cout_usd"] == 1e-06 and "enveloppe_conservation_reponses_v1" in o["erreur"]
    assert not list(vrai.iterdir())


def _module(nom, chemin=CHEMIN):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_dossier_non_inscriptible_refuse(tmp_path, monkeypatch, capsysbinary):
    M = _module("conservation_essai_acces")
    d = tmp_path / "c"
    d.mkdir()
    monkeypatch.setattr(M.os, "access", lambda *_a, **_k: False)
    assert M.principal([str(d), "argon", "--", "/bin/false"]) == 2
    assert b"non inscriptible" in capsysbinary.readouterr().out


def test_ecriture_impossible_apres_l_appel_arrete_l_appel(tmp_path):
    """Le dossier disparaît pendant l'appel : la réponse n'est pas rendue, code 9, le coût déclaré est compté, l'erreur dite."""
    dossier = tmp_path / "c"
    dossier.mkdir()
    nue, p = _jouer(tmp_path, dossier, RETIRER=dossier)
    assert p.returncode == 9
    assert b"octets bruts" not in p.stdout and b"fiche" not in p.stdout                  # réponse non rendue
    o = json.loads(p.stdout.decode().strip().splitlines()[-1])
    assert o["texte"] == "" and o["cout_usd"] == pytest.approx(0.42) and "conservation impossible" in o["erreur"]
    assert b"conservation impossible" in p.stderr


def test_ecriture_impossible_sans_cout_lisible_rien_sur_la_sortie(tmp_path):
    dossier = tmp_path / "c"
    dossier.mkdir()
    _nue, p = _jouer(tmp_path, dossier, RETIRER=dossier, COUT="0")
    assert p.returncode == 9 and p.stdout == b"" and b"conservation impossible" in p.stderr


def test_ecriture_atomique_jamais_d_ecrasement(tmp_path):
    M = _module("conservation_essai_atomique")
    d = tmp_path / "c"
    d.mkdir()
    M.ecrire_atomique(str(d), "x.bin", b"un")
    with pytest.raises(FileExistsError):
        M.ecrire_atomique(str(d), "x.bin", b"deux")
    assert (d / "x.bin").read_bytes() == b"un" and sorted(p.name for p in d.iterdir()) == ["x.bin"]


def _mutant(tmp_path, ancien, nouveau, nom):
    t = CHEMIN.read_text(encoding="utf-8")
    assert t.count(ancien) == 1, ancien
    p = tmp_path / f"{nom}.py"
    p.write_text(t.replace(ancien, nouveau), encoding="utf-8")
    return p


def test_mutation_conservation_sautee_attrapee(tmp_path):
    m = _mutant(tmp_path, "        conserver(dossier, etiquette, commande, consigne, p, debut, duree)\n", "        pass\n",
                "conservation_mutant_sautee")
    dossier = tmp_path / "c"
    dossier.mkdir()
    _nue, p = _jouer(tmp_path, dossier, script=m)
    assert p.returncode == 0 and not list(dossier.iterdir())                            # muté : rien de conservé
    _nue, p = _jouer(tmp_path, dossier)
    assert len(_appels(dossier)) == 1                                                    # vrai : conservé


def test_mutation_erreur_avalee_attrapee(tmp_path):
    m = _mutant(tmp_path, "        return CODE_ECRITURE_IMPOSSIBLE\n", "        pass\n", "conservation_mutant_avale")
    d1, d2 = tmp_path / "c1", tmp_path / "c2"
    d1.mkdir()
    d2.mkdir()
    nue, p = _jouer(tmp_path, d1, script=m, RETIRER=d1)
    assert p.returncode == 0 and b"octets bruts" in p.stdout                             # muté : réponse rendue sans copie
    _nue, p = _jouer(tmp_path, d2, RETIRER=d2)
    assert p.returncode == 9 and b"octets bruts" not in p.stdout


def test_l_environnement_n_est_jamais_recopie(tmp_path):
    dossier = tmp_path / "c"
    dossier.mkdir()
    _nue, p = _jouer(tmp_path, dossier, GEMINI_API_KEY="valeur-secrete-essai")
    for f in next(iter(_appels(dossier))).iterdir():
        assert b"valeur-secrete-essai" not in f.read_bytes(), f
