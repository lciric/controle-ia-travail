"""Essais du remplacement unique de la ligne `CODE-T07` (`scripts/remplacer_ligne_code_t07_v1.py`, R-2604 (1)) — v1.

Tous sur des **copies** (dossiers temporaires de pytest) ; jamais sur le vrai registre. Copie de départ : le registre des
scellements tel qu'il est au commit `c2fab6cc` (fusion du correctif du cache, `9061a5da…`), lu par `git show`, et le fichier
`CODE-T07-v2.json` de ce commit. Cas sain (octets hors de la ligne inchangés, trace scellée), lecteurs après remplacement
(`lire_registre_t07` et la garde « exactement une » avec les clés de l'étape A et les marques de la configuration v8,
`lire_lignes_actuelles`, `code_t07_v1 verifier`), témoins (ligne ajoutée au lieu d'être remplacée : refus ; ancienne ligne :
`verifier` refuse l'arbre corrigé), cas fautifs (registre, ancienne ligne, nouvelle ligne, journal, trace) : refus, rien d'écrit.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from controle_ia.scellement import sceller
from controle_ia.t07 import code_t07_v1 as ct
from controle_ia.t07 import lecture_v2 as lv
from controle_ia.t07 import registre_v1 as rg

RACINE_DEPOT = Path(__file__).resolve().parents[1]
SCRIPT = RACINE_DEPOT / "scripts" / "remplacer_ligne_code_t07_v1.py"
COMMIT_FUSION = "c2fab6cc7267b76228a75dc3e2e08bc7aa038961"
SHA_REGISTRE_FUSION = "9061a5dab171b111223b9596b6a042718a51bce250152c54eeee4f5d29d96265"
ANCIENNE = ("| CODE-T07 | 2026-11-11T05:40:34Z | registres/code-t07/CODE-T07-v2.json | "
            "d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c |")
CHEMIN_V3 = "registres/code-t07/CODE-T07-v3.json"
DATE_NEUVE = "2026-11-13T23:00:00Z"
MAINTENANT = rg.instant_utc("2026-11-13T23:30:00Z")

_spec = importlib.util.spec_from_file_location("remplacer_ligne_code_t07_v1", SCRIPT)
rl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rl)


def _git(d: Path, *args, texte=True):
    return subprocess.run(["git", "-C", str(d), *args], capture_output=True, text=texte, check=True).stdout


def _au_commit(chemin: str) -> bytes:
    try:
        return _git(RACINE_DEPOT, "show", f"{COMMIT_FUSION}:{chemin}", texte=False)
    except subprocess.CalledProcessError:
        pytest.skip(f"{chemin} au commit {COMMIT_FUSION[:8]} illisible (clone sans ce commit)")


def _cles_etape_a():
    """Clés de la garde de l'étape A, comme `lecture_v2` les forme avec `code_t07_exige` vrai (l. 410-414)."""
    exigees = rg.EXIGEES_ETAPE_A + (rg.CODE_T07,)
    permises = tuple(k for k in rg.PERMISES_ETAPE_A + (rg.VERDICT_P3BIS,) if k not in exigees)
    refusees = {k: v for k, v in rg.REFUSEES_ETAPE_A.items() if k != rg.VERDICT_P3BIS}
    marques = tuple(json.loads(_au_commit("prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"))["marques_autres_taches"])
    return exigees, permises, refusees, marques


def _ecrire_scelle(racine: Path, chemin: str, octets: bytes) -> str:
    p = racine / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(octets)
    return sceller(p)


@pytest.fixture
def copie(tmp_path):
    """Racine jetable : registre au commit de fusion, `CODE-T07-v2.json` de ce commit, `CODE-T07-v3.json` écrit à la tête du dépôt
    (mécanisme `code_t07_v1.ecrire_fichier_code`), scellés ; dossier de la trace."""
    racine = tmp_path / "racine"
    reg = racine / "registres" / "scellements-v1.md"
    reg.parent.mkdir(parents=True)
    octets = _au_commit("registres/scellements-v1.md")
    assert hashlib.sha256(octets).hexdigest() == SHA_REGISTRE_FUSION
    reg.write_bytes(octets)
    _ecrire_scelle(racine, "registres/code-t07/CODE-T07-v2.json", _au_commit("registres/code-t07/CODE-T07-v2.json"))
    tete = _git(RACINE_DEPOT, "rev-parse", "HEAD").strip()
    ct.ecrire_fichier_code(RACINE_DEPOT, tete, racine / CHEMIN_V3)
    sha3 = sceller(racine / CHEMIN_V3)
    (racine / "traces").mkdir()
    nouvelle = rg.ecrire_ligne(rg.CODE_T07, DATE_NEUVE, CHEMIN_V3, sha3)
    return {"racine": racine, "registre": reg, "avant": octets, "nouvelle": nouvelle, "trace": racine / "traces" / "trace-v1.md",
            "tete": tete}


def _remplacer(c, **kw):
    a = dict(racine=c["racine"], registre=c["registre"], ancienne=ANCIENNE, nouvelle=c["nouvelle"], trace=c["trace"],
             maintenant=MAINTENANT, heure=lambda: "2026-11-13T23:31:00Z")
    a.update(kw)
    return rl.remplacer(**a)


def _rien_ecrit(c, octets_avant=None):
    assert c["registre"].read_bytes() == (c["avant"] if octets_avant is None else octets_avant)
    assert not c["trace"].exists() and not Path(str(c["trace"]) + ".sha256").exists()
    assert not Path(str(c["registre"]) + rl.SUFFIXE_TMP).exists()


# ---------------------------------------------------------------------------------------------------------------- cas sain

def test_cas_sain_seule_la_ligne_change_trace_scellee(copie):
    r = _remplacer(copie)
    apres = copie["registre"].read_bytes()
    attendu = copie["avant"].replace((ANCIENNE + "\n").encode(), (copie["nouvelle"] + "\n").encode(), 1)
    assert apres == attendu and apres != copie["avant"]
    lav, lap = copie["avant"].decode().split("\n"), apres.decode().split("\n")
    assert len(lav) == len(lap) and [k for k, (x, y) in enumerate(zip(lav, lap)) if x != y] == [r["ligne_numero"] - 1]
    assert r["sha256_avant"] == SHA_REGISTRE_FUSION and r["sha256_apres"] == hashlib.sha256(apres).hexdigest()
    t = copie["trace"].read_text(encoding="utf-8")
    assert "```\n" + ANCIENNE + "\n```" in t and "```\n" + copie["nouvelle"] + "\n```" in t
    assert SHA_REGISTRE_FUSION in t and r["sha256_apres"] in t and "2026-11-13T23:31:00Z" in t
    assert r["trace_sha256"] == hashlib.sha256(copie["trace"].read_bytes()).hexdigest()
    assert Path(str(copie["trace"]) + ".sha256").read_text(encoding="utf-8").split()[0] == r["trace_sha256"]
    assert r["commit_cite"] == copie["tete"]
    assert not Path(str(copie["registre"]) + rl.SUFFIXE_TMP).exists()


def test_autres_octets_gardes_meme_irreguliers(copie):
    """Espaces et tabulation en fin d'une autre ligne, ligne vide en plus, pas de saut de ligne final : seuls les octets de la
    ligne CODE-T07 changent (aucune normalisation)."""
    irregulier = copie["avant"].replace(b"\n\n", b" \t\n\n\n", 1).rstrip(b"\n")
    copie["registre"].write_bytes(irregulier)
    _remplacer(copie)
    assert copie["registre"].read_bytes() == irregulier.replace(ANCIENNE.encode(), copie["nouvelle"].encode(), 1)


def test_ligne_code_t07_en_premiere_et_en_derniere_position(copie):
    for octets in ((ANCIENNE + "\n").encode() + copie["avant"].replace((ANCIENNE + "\n").encode(), b"", 1),
                   copie["avant"].replace((ANCIENNE + "\n").encode(), b"", 1) + ANCIENNE.encode()):
        copie["registre"].write_bytes(octets)
        for p in (copie["trace"], Path(str(copie["trace"]) + ".sha256")):
            p.unlink(missing_ok=True)
        _remplacer(copie)
        assert copie["registre"].read_bytes() == octets.replace(ANCIENNE.encode(), copie["nouvelle"].encode(), 1)


def test_a_blanc_rien_ecrit(copie):
    r = _remplacer(copie, a_blanc=True)
    assert r["a_blanc"] and r["sha256_avant"] == SHA_REGISTRE_FUSION
    _rien_ecrit(copie)


def test_seconde_execution_refusee(copie):
    _remplacer(copie)
    octets = copie["registre"].read_bytes()
    with pytest.raises(rl.RefusRemplacement, match="diffère de l'ancienne attendue|déjà présent"):
        _remplacer(copie, trace=copie["racine"] / "traces" / "trace-v2.md")
    assert copie["registre"].read_bytes() == octets


def test_construire_egale_ecrire_ligne(copie):
    l = rl.construire(copie["racine"], CHEMIN_V3, DATE_NEUVE)
    assert l == copie["nouvelle"]
    with pytest.raises(rg.RefusRegistre):
        rl.construire(copie["racine"], "registres/code-t07/absent.json", DATE_NEUVE)


# --------------------------------------------------------------------------- lecteurs du code épinglé, après remplacement

def test_apres_remplacement_garde_lecteurs_et_verifier_acceptent(copie):
    exigees, permises, refusees, marques = _cles_etape_a()
    _remplacer(copie)
    lignes, ignorees = rg.lire_registre_detail(copie["registre"], exigees, permises, refusees, marques)   # « exactement une »
    _, date, chemin, sha = lignes[rg.CODE_T07]
    assert (date, chemin) == (DATE_NEUVE, CHEMIN_V3) and sha == rg.sha256_de(copie["racine"] / CHEMIN_V3)
    assert "GEL-T08" in ignorees and "SCELLEMENT-T08-BASE-A" in ignorees
    assert rg.lire_registre_t07(copie["registre"], exigees, permises, refusees, marques)[rg.CODE_T07][2] == CHEMIN_V3
    assert lv.lire_lignes_actuelles(copie["registre"], (rg.CODE_T07,))[rg.CODE_T07]["chemin"] == CHEMIN_V3
    v = rg.verifier_lignes({rg.CODE_T07: lignes[rg.CODE_T07]}, copie["racine"], MAINTENANT)
    assert v[rg.CODE_T07]["sha256"] == sha
    if _git(RACINE_DEPOT, "status", "--porcelain", "--untracked-files=all", "--", "src/controle_ia").strip():
        pytest.skip("src/controle_ia/ modifié dans l'arbre de travail : verifier refuserait (DF-02), essai non concluant ici")
    assert ct.main(["verifier", str(copie["racine"]), str(copie["registre"])]) == 0


def test_temoin_ancienne_ligne_refusee_par_verifier(copie):
    """Témoin : avant le remplacement, la ligne actuelle (C7 `b4cd9953`) refuse l'arbre corrigé (R-2601, § 5 de l'addendum)."""
    c7 = "b4cd9953d199dd8f220f5162e5868c5b00fd392d"
    if subprocess.run(["git", "-C", str(RACINE_DEPOT), "cat-file", "-e", f"{c7}^{{commit}}"]).returncode != 0:
        pytest.skip("commit b4cd9953 absent du clone")
    if subprocess.run(["git", "-C", str(RACINE_DEPOT), "diff", "--quiet", c7, "HEAD", "--", "src/controle_ia"]).returncode == 0:
        pytest.skip("src/controle_ia/ de la tête égal à celui de b4cd9953 : témoin sans objet")
    assert ct.main(["verifier", str(copie["racine"]), str(copie["registre"])]) == 2


def test_temoin_ligne_ajoutee_au_lieu_de_remplacee_refusee_par_la_garde(copie):
    exigees, permises, refusees, marques = _cles_etape_a()
    with open(copie["registre"], "a", encoding="utf-8") as f:
        f.write(copie["nouvelle"] + "\n")
    with pytest.raises(rg.RefusRegistre, match=r"2 ligne\(s\) CODE-T07, exactement une attendue"):
        rg.lire_registre_detail(copie["registre"], exigees, permises, refusees, marques)
    with pytest.raises(rl.RefusRemplacement, match=r"2 ligne\(s\) CODE-T07"):
        _remplacer(copie)


def test_depot_jetable_verifier_refuse_avant_et_accepte_apres(tmp_path, monkeypatch):
    """R5 sans dépendre de l'état du dépôt : module factice, commit ancien cité par l'ancienne ligne, commit neuf (tête) par la
    nouvelle ; `verifier` refuse avant le remplacement, accepte après."""
    d = tmp_path / "code"
    m = d / "src" / "controle_ia" / "t07"
    m.mkdir(parents=True)
    _git(d, "init", "-q", "-b", "main")
    _git(d, "config", "user.email", "essai@example.invalid")
    _git(d, "config", "user.name", "essai")
    (m / "a.py").write_text("A = 1\n")
    (m / "b.py").write_text("B = 2\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "code ancien")
    vieux = _git(d, "rev-parse", "HEAD").strip()
    (m / "a.py").write_text("A = 3  # correctif\n")
    _git(d, "add", "-A")
    _git(d, "commit", "-q", "-m", "correctif")
    neuf = _git(d, "rev-parse", "HEAD").strip()
    monkeypatch.setattr(ct, "dossier_du_module", lambda: m)
    racine = tmp_path / "racine"
    ct.ecrire_fichier_code(d, vieux, racine / "registres" / "code-t07" / "CODE-T07-v2.json")
    ct.ecrire_fichier_code(d, neuf, racine / CHEMIN_V3)
    s2, s3 = sceller(racine / "registres" / "code-t07" / "CODE-T07-v2.json"), sceller(racine / CHEMIN_V3)
    ancienne = rg.ecrire_ligne(rg.CODE_T07, "2026-11-11T05:40:34Z", "registres/code-t07/CODE-T07-v2.json", s2)
    reg = racine / "registres" / "scellements-v1.md"
    reg.write_text("# Registre factice\n\n| SCELLEMENT-JEUX-T07-JD | 2026-11-10T08:22:50Z | x/a.jsonl | " + "0" * 64 + " |\n"
                   + ancienne + "\n| SCELLEMENT-T07 | 2026-11-11T07:11:42Z | prereg/t.md | " + "1" * 64 + " |\n", encoding="utf-8")
    assert ct.main(["verifier", str(racine), str(reg)]) == 2
    (racine / "traces").mkdir()
    nouvelle = rl.construire(racine, CHEMIN_V3, DATE_NEUVE)
    r = rl.remplacer(racine, reg, ancienne, nouvelle, racine / "traces" / "t.md", maintenant=MAINTENANT, heure=lambda: DATE_NEUVE)
    assert r["commit_cite"] == neuf
    assert ct.main(["verifier", str(racine), str(reg)]) == 0


# ------------------------------------------------------------------------------------------------------ cas fautifs

def _sans_ligne(c):
    c["registre"].write_bytes(c["avant"].replace((ANCIENNE + "\n").encode(), b"", 1))


def _deux_lignes(c):
    c["registre"].write_bytes(c["avant"] + (ANCIENNE + "\n").encode())


def _espace_final(c):
    c["registre"].write_bytes(c["avant"].replace((ANCIENNE + "\n").encode(), (ANCIENNE + " \n").encode(), 1))


def _retour_chariot(c):
    c["registre"].write_bytes(c["avant"].replace(b"\n", b"\r\n", 1))


def _separateur_unicode(c):
    c["registre"].write_bytes(c["avant"].replace(b"jamais r", "jamais r".encode(), 1))


def _non_utf8(c):
    c["registre"].write_bytes(c["avant"] + b"\xff\n")


def _journal_ouvert(c):
    Path(str(c["registre"]) + ".ouvertures.md").write_text(
        "| OUVERTURE-T07 | 2026-11-13T20:30:00Z | etape-A/20261111-151701-t06-reel | " + "2" * 64 + " | registre x |\n",
        encoding="utf-8")


def _trace_presente(c):
    c["trace"].write_text("trace antérieure\n", encoding="utf-8")


def _compagnon_trace_present(c):
    Path(str(c["trace"]) + ".sha256").write_text("0" * 64 + "  trace-v1.md\n", encoding="utf-8")


def _dossier_trace_absent(c):
    c["trace"] = c["racine"] / "absent" / "trace-v1.md"


REGISTRE_OU_TRACE_FAUTIFS = [
    ("aucune ligne CODE-T07", _sans_ligne, r"0 ligne\(s\) CODE-T07, exactement une attendue"),
    ("deux lignes CODE-T07", _deux_lignes, r"2 ligne\(s\) CODE-T07, exactement une attendue"),
    ("ligne du registre à un octet près (espace final)", _espace_final, "diffère de l'ancienne attendue"),
    ("retour chariot", _retour_chariot, "retour chariot"),
    ("séparateur de lignes unicode", _separateur_unicode, "séparateur de lignes"),
    ("registre non UTF-8", _non_utf8, "UTF-8 illisible"),
    ("ouverture déjà journalisée", _journal_ouvert, "OUVERTURE-T07 y est déjà"),
    ("trace déjà présente", _trace_presente, "déjà présent"),
    ("compagnon de la trace présent", _compagnon_trace_present, "déjà présent"),
    ("dossier de la trace absent", _dossier_trace_absent, "dossier de la trace"),
]


@pytest.mark.parametrize("nom,faute,motif", REGISTRE_OU_TRACE_FAUTIFS, ids=[x[0] for x in REGISTRE_OU_TRACE_FAUTIFS])
def test_registre_ou_trace_fautifs_refuses_rien_ecrit(copie, nom, faute, motif):
    faute(copie)
    octets = copie["registre"].read_bytes()
    with pytest.raises(rl.RefusRemplacement, match=motif):
        _remplacer(copie)
    assert copie["registre"].read_bytes() == octets
    if faute not in (_trace_presente, _compagnon_trace_present):
        assert not copie["trace"].exists()
    assert not Path(str(copie["registre"]) + rl.SUFFIXE_TMP).exists()


def _octet_change(s: str) -> str:
    return s[:-3] + ("0" if s[-3] != "0" else "1") + s[-2:]


ANCIENNES_FAUTIVES = [
    ("empreinte, un caractère changé", _octet_change(ANCIENNE), "diffère de l'ancienne attendue"),
    ("date, une seconde de plus", ANCIENNE.replace("05:40:34Z", "05:40:35Z"), "diffère de l'ancienne attendue"),
    ("espace final en plus", ANCIENNE + " ", "diffère de l'ancienne attendue"),
    ("deux espaces après la clé", ANCIENNE.replace("CODE-T07 |", "CODE-T07  |"), "diffère de l'ancienne attendue"),
    ("saut de ligne dedans", ANCIENNE + "\n", "saut de ligne"),
]


@pytest.mark.parametrize("nom,ancienne,motif", ANCIENNES_FAUTIVES, ids=[x[0] for x in ANCIENNES_FAUTIVES])
def test_ancienne_ligne_differente_d_un_octet_refusee(copie, nom, ancienne, motif):
    with pytest.raises(rl.RefusRemplacement, match=motif):
        _remplacer(copie, ancienne=ancienne)
    _rien_ecrit(copie)


def _nouvelles_fautives(c):
    sha3 = rg.sha256_de(c["racine"] / CHEMIN_V3)
    r = c["racine"]
    # fichier cité dont le contenu ne répond plus au compagnon
    _ecrire_scelle(r, "registres/code-t07/CODE-T07-v3b.json", (r / CHEMIN_V3).read_bytes())
    (r / "registres/code-t07/CODE-T07-v3b.json").write_bytes((r / CHEMIN_V3).read_bytes() + b" ")
    # fichier scellé, hors de la forme d'un fichier CODE-T07
    sx = _ecrire_scelle(r, "registres/code-t07/CODE-T07-v3c.json", b'{"commit": "abc"}\n')
    # fichier sans compagnon
    (r / "registres/code-t07/CODE-T07-v3d.json").write_bytes((r / CHEMIN_V3).read_bytes())
    sd = rg.sha256_de(r / "registres/code-t07/CODE-T07-v3d.json")
    e = rg.ecrire_ligne
    return [
        ("format non exact (deux espaces)", e(rg.CODE_T07, DATE_NEUVE, CHEMIN_V3, sha3).replace("| CODE-T07 |", "|  CODE-T07 |"),
         "format exact"),
        ("clé autre", e("CODE-T08", DATE_NEUVE, CHEMIN_V3, sha3), "clé 'CODE-T08'"),
        ("empreinte à 63 caractères", f"| CODE-T07 | {DATE_NEUVE} | {CHEMIN_V3} | {sha3[:-1]} |", "mal formée"),
        ("date hors format", f"| CODE-T07 | 2026-11-13 23:00:00 | {CHEMIN_V3} | {sha3} |", "mal formée"),
        ("date impossible", e(rg.CODE_T07, "2026-11-31T23:00:00Z", CHEMIN_V3, sha3), "impossible"),
        ("cinq cellules", e(rg.CODE_T07, DATE_NEUVE, CHEMIN_V3, sha3) + " x |", "5 cellule"),
        ("empreinte différente du fichier", e(rg.CODE_T07, DATE_NEUVE, CHEMIN_V3, "a" * 64), "empreinte"),
        ("fichier cité absent", e(rg.CODE_T07, DATE_NEUVE, "registres/code-t07/CODE-T07-v9.json", sha3), "absent"),
        ("fichier cité ≠ compagnon", e(rg.CODE_T07, DATE_NEUVE, "registres/code-t07/CODE-T07-v3b.json", sha3), "compagnon"),
        ("fichier cité sans compagnon", e(rg.CODE_T07, DATE_NEUVE, "registres/code-t07/CODE-T07-v3d.json", sd), "compagnon"),
        ("fichier hors forme CODE-T07", e(rg.CODE_T07, DATE_NEUVE, "registres/code-t07/CODE-T07-v3c.json", sx), "forme"),
        ("chemin avec « .. »", e(rg.CODE_T07, DATE_NEUVE, "registres/../registres/code-t07/CODE-T07-v3.json", sha3), "sans « .. »"),
        ("chemin absolu", e(rg.CODE_T07, DATE_NEUVE, "/" + CHEMIN_V3, sha3), "relatif"),
        ("chemin hors du motif recopié", e(rg.CODE_T07, DATE_NEUVE, "registres/code t07/v3.json", sha3), r"\[A-Za-z0-9"),
        ("même chemin que l'ancienne", e(rg.CODE_T07, DATE_NEUVE, "registres/code-t07/CODE-T07-v2.json",
                                         "d5eb0b665df187d158fa84deff733b0f382fc309510163625f7aaea1ae9a692c"), "même chemin"),
        ("date égale à l'ancienne", e(rg.CODE_T07, "2026-11-11T05:40:34Z", CHEMIN_V3, sha3), "pas strictement postérieure"),
        ("date antérieure à l'ancienne", e(rg.CODE_T07, "2026-11-10T00:00:00Z", CHEMIN_V3, sha3), "pas strictement postérieure"),
        ("date future", e(rg.CODE_T07, "2026-11-14T00:00:00Z", CHEMIN_V3, sha3), "dans le futur"),
        ("saut de ligne dedans", e(rg.CODE_T07, DATE_NEUVE, CHEMIN_V3, sha3) + "\n", "saut de ligne"),
    ]


def test_nouvelles_lignes_fautives_refusees_rien_ecrit(copie):
    cas = _nouvelles_fautives(copie)
    assert len(cas) >= 15
    for nom, nouvelle, motif in cas:
        with pytest.raises(rl.RefusRemplacement, match=motif):
            _remplacer(copie, nouvelle=nouvelle)
        _rien_ecrit(copie)


def test_registre_change_pendant_les_controles_refuse(copie, monkeypatch):
    vrai = rl.preparer

    def preparer_puis_toucher(*a, **k):
        p = vrai(*a, **k)
        with open(copie["registre"], "ab") as f:
            f.write(b"\n")
        return p

    monkeypatch.setattr(rl, "preparer", preparer_puis_toucher)
    with pytest.raises(rl.RefusRemplacement, match="changé pendant les contrôles"):
        _remplacer(copie)
    assert copie["registre"].read_bytes() == copie["avant"] + b"\n"
    assert not copie["trace"].exists()


# ------------------------------------------------------------------------------------------------------ ligne de commande

def _cli(*args):
    env = {**os.environ, "PYTHONPATH": str(RACINE_DEPOT / "src"), "PYTHONDONTWRITEBYTECODE": "1"}
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True, env=env)


def test_ligne_de_commande_construire_a_blanc_remplacer_puis_refus(copie):
    r = copie["racine"]
    date = "2026-11-12T00:00:00Z"                       # passée : la commande compare à l'heure réelle de la machine
    c = _cli("construire", "--racine", str(r), "--chemin", CHEMIN_V3, "--date", date)
    assert c.returncode == 0, c.stderr
    nouvelle = c.stdout.strip()
    assert nouvelle == rg.ecrire_ligne(rg.CODE_T07, date, CHEMIN_V3, rg.sha256_de(r / CHEMIN_V3))
    base = ["remplacer", "--racine", str(r), "--registre", str(copie["registre"]), "--ancienne", ANCIENNE, "--nouvelle", nouvelle,
            "--trace", str(copie["trace"])]
    b = _cli(*base, "--a-blanc")
    assert b.returncode == 0 and "À BLANC, conforme" in b.stdout, b.stderr
    _rien_ecrit(copie)
    f = _cli(*base[:6], _octet_change(ANCIENNE), *base[7:])
    assert f.returncode == 2 and f.stderr.startswith("REFUS : ") and "diffère de l'ancienne attendue" in f.stderr
    _rien_ecrit(copie)
    o = _cli(*base)
    assert o.returncode == 0 and "REMPLACÉE" in o.stdout, o.stderr
    assert copie["registre"].read_bytes() == copie["avant"].replace(ANCIENNE.encode(), nouvelle.encode(), 1)
    assert Path(str(copie["trace"]) + ".sha256").is_file()
    d = _cli(*base[:-1], str(copie["racine"] / "traces" / "trace-v2.md"))
    assert d.returncode == 2 and "diffère de l'ancienne attendue" in d.stderr
