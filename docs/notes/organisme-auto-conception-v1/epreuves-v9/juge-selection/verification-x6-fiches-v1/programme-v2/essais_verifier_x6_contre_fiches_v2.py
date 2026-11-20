"""Essais du programme de vérification X6 — v2. Fichiers synthétiques seulement.

Lancement : python3 -B -m pytest -q -p no:cacheprovider essais_verifier_x6_contre_fiches_v2.py
Développeur, modèle L′.
"""

import hashlib
import json
import os
import subprocess
import sys
import tempfile

import pytest

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import verifier_x6_contre_fiches_v2 as v  # noqa: E402

PROGRAMME = os.path.join(ICI, "verifier_x6_contre_fiches_v2.py")
RACINE_ESSAIS = os.path.join(ICI, "essais-fichiers")

# Identifiants synthétiques reconnaissables, pour vérifier qu'aucun ne fuit.
CLES = [f"SYNTH-CLE-{i:03d}-ZQX" for i in range(94)]
RETENUES_ABSENTES = ["SYNTH-RETENUE-A-ZQX", "SYNTH-RETENUE-B-ZQX"]
VALEUR_SECRETE = "SYNTH-VALEUR-SECRETE-ZQX"
MARQUE = "ZQX"


def _sha(octets):
    return hashlib.sha256(octets).hexdigest()


@pytest.fixture
def dossier():
    os.makedirs(RACINE_ESSAIS, exist_ok=True)
    return tempfile.mkdtemp(dir=RACINE_ESSAIS)


def _ecrire(dossier, nom, objet):
    chemin = os.path.join(dossier, nom)
    octets = json.dumps(objet, ensure_ascii=False).encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    return chemin, _sha(octets)


def _fiches(dossier, cles=CLES):
    objet = {c: {"texte": VALEUR_SECRETE, "rang": i, "sous": {"x": c}} for i, c in enumerate(cles)}
    return _ecrire(dossier, "fiches.json", objet)


def _objet_extraction(retenues):
    """Copie synthétique de forme identique à l'extraction réelle (clés et types)."""
    return {
        "chemin": "SYNTH-CHEMIN-ZQX/journal.json",
        "commit": "0" * 40,
        "extraction": {
            "comptes_par_classe": {"a_corriger": len(retenues)},
            "doublons": [],
            "identifiants_par_classe": {"a_corriger": list(retenues)},
            "noms_cles": ["SYNTH-NOM-1-ZQX", "SYNTH-NOM-2-ZQX"],
            "objets_a_classe": len(retenues),
            "source_identifiant": {"cle": 2, "parent": 0},
        },
        "fichiers_trouves": 1,
        "issue": "conforme",
        "octets_journal": 957,
        "sha256_journal": "1" * 64,
        "suffixe": "/SYNTH-SUFFIXE-ZQX.json",
        "version": "SYNTH-VERSION-ZQX",
    }


def _extraction(dossier, retenues):
    return _ecrire(dossier, "extraction.json", _objet_extraction(retenues))


def _lancer(dossier, retenues=RETENUES_ABSENTES, cles=CLES, fausse=None, capsys=None):
    f, hf = _fiches(dossier, cles)
    e, he = _extraction(dossier, retenues)
    if fausse == "fiches":
        hf = "0" * 64
    if fausse == "extraction":
        he = "0" * 64
    s = os.path.join(dossier, "sortie.json")
    v.executer(f, e, s, hf, he)
    return f, e, s, hf, he


def _lire_sortie(s):
    with open(s, "rb") as fh:
        return fh.read()


# --- cas sain ---------------------------------------------------------------

def test_cas_sain(dossier):
    f, e, s, hf, he = _lancer(dossier)
    octets = _lire_sortie(s)
    objet = json.loads(octets)
    assert list(objet) == ["nombre_de_cles", "retenues_presentes", "empreintes"]
    assert objet["nombre_de_cles"] == 94
    assert objet["retenues_presentes"] == [False, False]
    assert objet["empreintes"] == {"fiches": hf, "extraction": he}
    with open(s + ".sha256", "rb") as fh:
        assert fh.read().decode() == f"{_sha(octets)}  sortie.json\n"
    r = subprocess.run(["sha256sum", "-c", "sortie.json.sha256"], cwd=dossier,
                       capture_output=True)
    assert r.returncode == 0


def test_retenue_presente_dans_l_ordre(dossier):
    retenues = [RETENUES_ABSENTES[0], CLES[17]]
    _, _, s, _, _ = _lancer(dossier, retenues=retenues)
    objet = json.loads(_lire_sortie(s))
    assert objet["retenues_presentes"] == [False, True]
    assert objet["nombre_de_cles"] == 94


def test_deux_retenues_presentes_ordre_inverse(dossier):
    _, _, s, _, _ = _lancer(dossier, retenues=[CLES[5], RETENUES_ABSENTES[1]])
    assert json.loads(_lire_sortie(s))["retenues_presentes"] == [True, False]


# --- artefacts : refus ---------------------------------------------------------

def _aucune_sortie(dossier):
    s = os.path.join(dossier, "sortie.json")
    return not os.path.lexists(s) and not os.path.lexists(s + ".sha256")


@pytest.mark.parametrize("fausse", ["fiches", "extraction"])
def test_empreinte_fausse(dossier, fausse):
    with pytest.raises(v.Refus) as exc:
        _lancer(dossier, fausse=fausse)
    assert "empreinte" in str(exc.value) and fausse in str(exc.value)
    assert _aucune_sortie(dossier)


def test_empreinte_verifiee_avant_decodage(dossier, monkeypatch):
    appels = []
    monkeypatch.setattr(v.json, "loads", lambda *a, **k: appels.append(1))
    with pytest.raises(v.Refus):
        _lancer(dossier, fausse="extraction")
    assert appels == []


def test_fiches_non_json_a_bonne_empreinte(dossier):
    chemin = os.path.join(dossier, "fiches.json")
    octets = b"pas du json " + MARQUE.encode()
    with open(chemin, "xb") as fh:
        fh.write(octets)
    e, he = _extraction(dossier, RETENUES_ABSENTES)
    with pytest.raises(v.Refus) as exc:
        v.executer(chemin, e, os.path.join(dossier, "sortie.json"), _sha(octets), he)
    assert MARQUE not in str(exc.value)
    assert _aucune_sortie(dossier)


def test_fiches_racine_liste(dossier):
    f, hf = _ecrire(dossier, "fiches.json", [{"a": 1}])
    e, he = _extraction(dossier, RETENUES_ABSENTES)
    with pytest.raises(v.Refus):
        v.executer(f, e, os.path.join(dossier, "sortie.json"), hf, he)
    assert _aucune_sortie(dossier)


def test_fiches_cle_en_double(dossier):
    chemin = os.path.join(dossier, "fiches.json")
    octets = b'{"SYNTH-D-ZQX": 1, "SYNTH-D-ZQX": 2}'
    with open(chemin, "xb") as fh:
        fh.write(octets)
    e, he = _extraction(dossier, RETENUES_ABSENTES)
    with pytest.raises(v.Refus) as exc:
        v.executer(chemin, e, os.path.join(dossier, "sortie.json"), _sha(octets), he)
    assert MARQUE not in str(exc.value)


@pytest.mark.parametrize("retenues", [
    [RETENUES_ABSENTES[0]],
    RETENUES_ABSENTES + ["SYNTH-RETENUE-C-ZQX"],
    [],
    [RETENUES_ABSENTES[0], RETENUES_ABSENTES[0]],
    [RETENUES_ABSENTES[0], 7],
])
def test_extraction_mal_comptee(dossier, retenues):
    with pytest.raises(v.Refus) as exc:
        _lancer(dossier, retenues=retenues)
    assert MARQUE not in str(exc.value)
    assert _aucune_sortie(dossier)


def _sans(chemin_cle, remplacement=None, supprimer=True):
    objet = _objet_extraction(RETENUES_ABSENTES)
    cible = objet
    for cle in chemin_cle[:-1]:
        cible = cible[cle]
    if supprimer:
        del cible[chemin_cle[-1]]
    else:
        cible[chemin_cle[-1]] = remplacement
    return objet


@pytest.mark.parametrize("objet", [
    _sans(["extraction"]),
    _sans(["extraction"], [], supprimer=False),
    _sans(["extraction"], "SYNTH-ZQX", supprimer=False),
    _sans(["extraction", "identifiants_par_classe"]),
    _sans(["extraction", "identifiants_par_classe"], ["SYNTH-ZQX"], supprimer=False),
    _sans(["extraction", "identifiants_par_classe", "a_corriger"]),
    _sans(["extraction", "identifiants_par_classe", "a_corriger"],
          {"SYNTH-A-ZQX": 1, "SYNTH-B-ZQX": 2}, supprimer=False),
    {"identifiants_par_classe": {"a_corriger": RETENUES_ABSENTES}},  # forme du v1
    [RETENUES_ABSENTES],
])
def test_extraction_niveau_manquant_ou_mal_forme(dossier, objet):
    f, hf = _fiches(dossier)
    e, he = _ecrire(dossier, "extraction.json", objet)
    with pytest.raises(v.Refus) as exc:
        v.executer(f, e, os.path.join(dossier, "sortie.json"), hf, he)
    assert MARQUE not in str(exc.value)
    assert _aucune_sortie(dossier)


def test_forme_identique_a_l_extraction_reelle(dossier):
    # Mêmes clés, à chaque niveau, que l'extraction réelle ; valeurs synthétiques.
    objet = _objet_extraction(RETENUES_ABSENTES)
    assert list(objet) == ["chemin", "commit", "extraction", "fichiers_trouves", "issue",
                           "octets_journal", "sha256_journal", "suffixe", "version"]
    assert list(objet["extraction"]) == ["comptes_par_classe", "doublons",
                                         "identifiants_par_classe", "noms_cles",
                                         "objets_a_classe", "source_identifiant"]
    assert list(objet["extraction"]["identifiants_par_classe"]) == ["a_corriger"]
    f, hf = _fiches(dossier)
    chemin = os.path.join(dossier, "extraction.json")
    octets = (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode()
    with open(chemin, "xb") as fh:
        fh.write(octets)
    s = os.path.join(dossier, "sortie.json")
    v.executer(f, chemin, s, hf, _sha(octets))
    sortie = json.loads(_lire_sortie(s))
    assert sortie["nombre_de_cles"] == 94
    assert sortie["retenues_presentes"] == [False, False]


def test_extraction_decodee_avant_les_cartes_refus(dossier, monkeypatch):
    appels = []
    monkeypatch.setattr(v, "_cles_des_fiches", lambda o: appels.append(1))
    with pytest.raises(v.Refus):
        _lancer(dossier, retenues=[RETENUES_ABSENTES[0]])
    assert appels == []


def test_extraction_decodee_avant_les_cartes_ordre(dossier, monkeypatch):
    ordre = []
    vraie_ext, vraie_fiches = v._retenues_de_l_extraction, v._cles_des_fiches
    monkeypatch.setattr(v, "_retenues_de_l_extraction",
                        lambda o: (ordre.append("extraction"), vraie_ext(o))[1])
    monkeypatch.setattr(v, "_cles_des_fiches",
                        lambda o: (ordre.append("fiches"), vraie_fiches(o))[1])
    _lancer(dossier)
    assert ordre == ["extraction", "fiches"]


@pytest.mark.parametrize("deja", ["sortie.json", "sortie.json.sha256"])
def test_sortie_existante(dossier, deja):
    chemin_deja = os.path.join(dossier, deja)
    with open(chemin_deja, "xb") as fh:
        fh.write(b"ancien")
    with pytest.raises(v.Refus):
        _lancer(dossier)
    with open(chemin_deja, "rb") as fh:
        assert fh.read() == b"ancien"
    autre = "sortie.json.sha256" if deja == "sortie.json" else "sortie.json"
    assert not os.path.lexists(os.path.join(dossier, autre))


# --- clé de plus impossible -----------------------------------------------------

def test_cle_de_plus_dans_la_sortie_impossible(dossier, monkeypatch):
    monkeypatch.setattr(v, "CHAMPS_SORTIE",
                        ("nombre_de_cles", "retenues_presentes", "empreintes", "identifiants"))
    with pytest.raises(v.Refus):
        _lancer(dossier)
    assert _aucune_sortie(dossier)


def test_sortie_exactement_trois_champs_quelles_que_soient_les_entrees(dossier):
    _, _, s, _, _ = _lancer(dossier, retenues=[CLES[0], CLES[1]])
    objet = json.loads(_lire_sortie(s))
    assert set(objet) == {"nombre_de_cles", "retenues_presentes", "empreintes"}
    assert set(objet["empreintes"]) == {"fiches", "extraction"}
    assert all(isinstance(b, bool) for b in objet["retenues_presentes"])


# --- aucun identifiant dans la sortie ni à l'écran -------------------------------

def test_aucun_identifiant_dans_la_sortie(dossier):
    _, _, s, _, _ = _lancer(dossier, retenues=[CLES[3], RETENUES_ABSENTES[0]])
    texte = _lire_sortie(s).decode("utf-8")
    with open(s + ".sha256", "rb") as fh:
        texte += fh.read().decode("utf-8")
    assert MARQUE not in texte
    assert "SYNTH" not in texte
    assert VALEUR_SECRETE not in texte


def _principal_avec_constantes(monkeypatch, hf, he, argv, capsys):
    monkeypatch.setattr(v, "EMPREINTE_FICHES", hf)
    monkeypatch.setattr(v, "EMPREINTE_EXTRACTION", he)
    code = v.principal(argv)
    sortie = capsys.readouterr()
    return code, sortie.out + sortie.err


def test_ecran_fait_sans_identifiant(dossier, monkeypatch, capsys):
    f, hf = _fiches(dossier)
    e, he = _extraction(dossier, [CLES[2], RETENUES_ABSENTES[1]])
    s = os.path.join(dossier, "sortie.json")
    code, ecran = _principal_avec_constantes(
        monkeypatch, hf, he, ["--fiches", f, "--extraction", e, "--sortie", s], capsys)
    assert code == 0
    assert ecran == "FAIT\n"


@pytest.mark.parametrize("cas", ["une", "trois", "fausse", "existe", "illisible"])
def test_ecran_refus_sans_identifiant(dossier, monkeypatch, capsys, cas):
    f, hf = _fiches(dossier)
    retenues = {"une": [CLES[0]], "trois": CLES[:3]}.get(cas, RETENUES_ABSENTES)
    e, he = _extraction(dossier, retenues)
    s = os.path.join(dossier, "sortie.json")
    if cas == "fausse":
        hf = "f" * 64
    if cas == "existe":
        with open(s, "xb") as fh:
            fh.write(b"x")
    if cas == "illisible":
        f = os.path.join(dossier, "absent-" + MARQUE + ".json")
    code, ecran = _principal_avec_constantes(
        monkeypatch, hf, he, ["--fiches", f, "--extraction", e, "--sortie", s], capsys)
    assert code != 0
    assert ecran.startswith("REFUS : ")
    assert ecran.count("\n") == 1
    assert MARQUE not in ecran and "SYNTH" not in ecran
    assert VALEUR_SECRETE not in ecran


def test_arguments_invalides_sans_echo(capsys):
    with pytest.raises(SystemExit) as exc:
        v.principal(["--fiches", "SYNTH-A-ZQX", "--inconnu-ZQX"])
    assert exc.value.code != 0
    sortie = capsys.readouterr()
    assert MARQUE not in sortie.out + sortie.err


# --- le point d'entrée n'accepte que les constantes gelées -----------------------

def test_constantes_gelees():
    assert v.EMPREINTE_FICHES == (
        "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481")
    assert v.EMPREINTE_EXTRACTION == (
        "f5c7cc1ccd83bd8648d44c0c409e8a5fe79fbedca3af429f4ad44fb31e3659eb")


def test_aucune_option_d_empreintes_en_ligne_de_commande():
    with open(PROGRAMME, encoding="utf-8") as fh:
        source = fh.read()
    options = [ligne for ligne in source.splitlines() if "add_argument(" in ligne]
    assert len(options) == 3
    assert all(any(o in ligne for o in ('"--fiches"', '"--extraction"', '"--sortie"'))
               for ligne in options)


@pytest.mark.parametrize("option", ["--empreintes-attendues-essai", "--empreinte-fiches", "--emp"])
def test_option_d_empreinte_refusee(dossier, option):
    f, _ = _fiches(dossier)
    e, _ = _extraction(dossier, RETENUES_ABSENTES)
    s = os.path.join(dossier, "sortie.json")
    r = subprocess.run([sys.executable, "-B", PROGRAMME, "--fiches", f, "--extraction", e,
                        "--sortie", s, option, "0" * 64], capture_output=True, text=True)
    assert r.returncode != 0
    assert _aucune_sortie(dossier)


def test_ligne_de_commande_refuse_fichiers_synthetiques(dossier):
    # Les vraies empreintes gelées ne correspondent à aucun fichier synthétique.
    f, _ = _fiches(dossier)
    e, _ = _extraction(dossier, RETENUES_ABSENTES)
    s = os.path.join(dossier, "sortie.json")
    r = subprocess.run([sys.executable, "-B", PROGRAMME, "--fiches", f, "--extraction", e,
                        "--sortie", s], capture_output=True, text=True)
    assert r.returncode != 0
    assert r.stdout == ""
    assert r.stderr == "REFUS : empreinte du fichier fiches différente de l'attendue\n"
    assert _aucune_sortie(dossier)
