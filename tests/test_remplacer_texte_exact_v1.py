"""Essais de `scripts/remplacer_texte_exact_v1.py` (pytest) — développeur, modèle L′.

Chaque contrôle est une fonction `verif_*(script, dossier)` qui lève AssertionError en cas d'écart :
  - les essais ordinaires l'appliquent à l'outil (cas sain et artefact de chaque refus, R5) ;
  - le contrôle « trop beau » (R4) l'applique à des copies de l'outil où un défaut est réintroduit, et exige qu'elle échoue.
L'outil est appelé par son chemin, dans un sous-processus (`python3 -B -I`), comme le feront les agents.
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

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "remplacer_texte_exact_v1.py"
SUFFIXE_JOURNAL = ".journal-remplacements-v1.json"


# ---------------------------------------------------------------------------------------------------------------- outillage

def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lancer(script: Path, *args) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-B", "-I", str(script), *[str(a) for a in args]],
                          capture_output=True, text=True, timeout=60)


def ecrits(sortie: Path) -> list[Path]:
    s = str(sortie)
    return [Path(s), Path(s + ".sha256"), Path(s + SUFFIXE_JOURNAL), Path(s + SUFFIXE_JOURNAL + ".sha256")]


def poser(dossier: Path, cible: bytes, remplacements) -> tuple[Path, Path, Path]:
    dossier.mkdir(parents=True, exist_ok=True)
    c, j = dossier / "cible.txt", dossier / "remplacements.json"
    c.write_bytes(cible)
    if isinstance(remplacements, bytes):
        j.write_bytes(remplacements)
    else:
        j.write_bytes(json.dumps(remplacements, ensure_ascii=False).encode("utf-8"))
    return c, j, dossier / "sortie.txt"


def attendre_succes(script: Path, dossier: Path, cible: bytes, remplacements, attendu: bytes, *options) -> dict:
    c, j, s = poser(dossier, cible, remplacements)
    octets_json = j.read_bytes()
    r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", s, *options)
    assert r.returncode == 0, (r.returncode, r.stderr)
    assert "FAIT" in r.stdout, r.stdout
    assert c.read_bytes() == cible, "la cible a changé"
    sortie = s.read_bytes()
    assert sortie == attendu, (sortie, attendu)
    comp, journal_p, comp_j = ecrits(s)[1:]
    assert comp.read_bytes() == f"{sha(attendu)}  {s.name}\n".encode(), comp.read_bytes()
    jb = journal_p.read_bytes()
    assert comp_j.read_bytes() == f"{sha(jb)}  {journal_p.name}\n".encode()
    journal = json.loads(jb.decode("utf-8"))
    assert journal["cible_sha256"] == sha(cible)
    assert journal["remplacements_sha256"] == sha(octets_json)
    assert journal["sortie_sha256"] == sha(attendu)
    n = len(json.loads(octets_json.decode("utf-8")))
    assert journal["nombre_remplacements"] == n and len(journal["detail"]) == n
    assert journal["outil_sha256"] == sha(Path(script).read_bytes())
    return {"journal": journal, "stderr": r.stderr, "sortie": s}


def attendre_refus(script: Path, dossier: Path, cible: bytes, remplacements, motif: str) -> str:
    c, j, s = poser(dossier, cible, remplacements)
    jb = j.read_bytes()
    r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", s)
    assert r.returncode == 2, (r.returncode, r.stderr)
    assert "REFUS" in r.stderr and motif in r.stderr, r.stderr
    assert not any(os.path.lexists(p) for p in ecrits(s)), "un fichier a été écrit malgré le refus"
    assert c.read_bytes() == cible and j.read_bytes() == jb
    return r.stderr


# ---------------------------------------------------------------------------------------------------------------- cas sains

def verif_sain_simple(script, d):
    res = attendre_succes(script, d, b"un\ndeux\ntrois\n", [{"ancien": "deux", "neuf": "2"}], b"un\n2\ntrois\n")
    det = res["journal"]["detail"][0]
    assert det["ligne_cible"] == 2 and det["octet_debut_cible"] == 3
    assert det["occurrences_neuf_avant"] == 0 and det["occurrences_neuf_apres"] == 1


def verif_sain_octets(script, d):
    """Marque d'ordre des octets, CRLF, LF, CR seul, non-ASCII, espaces de fin, fin de fichier sans saut : tout est gardé."""
    tete = b"\xef\xbb\xbf" + "début\r\n".encode()
    zone1 = "ligne é 🙂".encode()
    milieu = " \t \r\nmilieu\nseul\rCR\r\n".encode()
    zone2 = "fin".encode()
    queue = b" sans saut \t"
    cible = tete + zone1 + milieu + zone2 + queue
    rempl = [{"ancien": "fin", "neuf": "FIN"}, {"ancien": "ligne é 🙂", "neuf": "LIGNE ü"}]
    attendu = tete + "LIGNE ü".encode() + milieu + b"FIN" + queue
    res = attendre_succes(script, d, cible, rempl, attendu)
    sortie = res["sortie"].read_bytes()
    assert sortie.startswith(tete) and sortie.endswith(queue) and milieu in sortie
    assert sortie.count(b"\r\n") == cible.count(b"\r\n") and sortie.count(b"\r") == cible.count(b"\r")
    assert res["stderr"] == ""


def verif_sain_suppression(script, d):
    attendre_succes(script, d, b"a, b, c\n", [{"ancien": ", b", "neuf": ""}], b"a, c\n")


def verif_sain_zones_contigues(script, d):
    attendre_succes(script, d, b"abcdef", [{"ancien": "def", "neuf": "2"}, {"ancien": "abc", "neuf": "1"}], b"12")


def verif_sain_application_simultanee(script, d):
    """Le texte neuf du n° 1 contient l'ancien du n° 2 : il n'est pas relu ; le n° 2 agit à sa place d'origine."""
    attendre_succes(script, d, b"A puis B", [{"ancien": "A", "neuf": "xBx"}, {"ancien": "B", "neuf": "C"}], b"xBx puis C")


def verif_sain_neufs_identiques(script, d):
    attendre_succes(script, d, b"x=1; y=2;", [{"ancien": "1", "neuf": "0"}, {"ancien": "2", "neuf": "0"}], b"x=0; y=0;")


def verif_sain_neuf_deja_present(script, d):
    res = attendre_succes(script, d, b"alpha beta", [{"ancien": "alpha", "neuf": "beta"}], b"beta beta")
    det = res["journal"]["detail"][0]
    assert det["occurrences_neuf_avant"] == 1 and det["occurrences_neuf_apres"] == 2


def verif_sain_ancien_non_chevauchant(script, d):
    attendre_succes(script, d, b"xaay", [{"ancien": "aa", "neuf": "b"}], b"xby")


def verif_sain_json_echappements(script, d):
    rempl = b'[{"ancien": "\\u00e9t\\u00e9\\n", "neuf": "hiver\\r\\n"}]'
    res = attendre_succes(script, d, "été\r\nété\n".encode(), rempl, "été\r\nhiver\r\n".encode())
    assert res["stderr"] == ""


def verif_sain_option_sur_place_interdit(script, d):
    attendre_succes(script, d, b"un deux", [{"ancien": "deux", "neuf": "2"}], b"un 2", "--sur-place-interdit")


def verif_sain_avertissement_fin_de_ligne(script, d):
    res = attendre_succes(script, d, b"a\r\nb\r\n", [{"ancien": "b", "neuf": "b\nc"}], b"a\r\nb\nc\r\n")
    assert "AVERTISSEMENT" in res["stderr"] and len(res["journal"]["avertissements"]) == 1


# ---------------------------------------------------------------------------------------------------------------- artefacts

def verif_refus_ancien_absent(script, d):
    attendre_refus(script, d, b"un deux", [{"ancien": "trois", "neuf": "3"}], "trouvé 0 fois")


def verif_refus_ancien_double(script, d):
    err = attendre_refus(script, d, b"abc\nabc\n", [{"ancien": "abc", "neuf": "z"}], "trouvé 2 fois")
    assert "lignes 1, 2" in err


def verif_refus_ancien_chevauchant(script, d):
    attendre_refus(script, d, b"xaaay", [{"ancien": "aa", "neuf": "b"}], "trouvé 2 fois")


def verif_refus_zones_chevauchantes(script, d):
    attendre_refus(script, d, b"abcdef", [{"ancien": "abcd", "neuf": "X"}, {"ancien": "cdef", "neuf": "Y"}], "chevauchent")


def verif_refus_ancien_repete_dans_la_liste(script, d):
    attendre_refus(script, d, b"abc", [{"ancien": "b", "neuf": "X"}, {"ancien": "b", "neuf": "Y"}], "chevauchent")


def verif_refus_neuf_jonction(script, d):
    attendre_refus(script, d, b"a_c", [{"ancien": "_", "neuf": "cc"}], "attendues")


def verif_refus_neuf_dans_ancien(script, d):
    attendre_refus(script, d, b"foo bar.", [{"ancien": "foo bar", "neuf": "foo"}], "attendues")


def verif_refus_ancien_vide(script, d):
    attendre_refus(script, d, b"a\n", [{"ancien": "", "neuf": "b"}], "texte ancien vide")


def _preexistant(script, d, indice):
    c, j, s = poser(d, b"un deux", [{"ancien": "deux", "neuf": "2"}])
    deja = ecrits(s)[indice]
    deja.write_bytes(b"ANCIEN CONTENU\n")
    r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", s)
    assert r.returncode == 2 and "existe déjà" in r.stderr, (r.returncode, r.stderr)
    assert deja.read_bytes() == b"ANCIEN CONTENU\n", "fichier préexistant réécrit"
    assert not any(os.path.lexists(p) for p in ecrits(s) if p != deja)
    assert c.read_bytes() == b"un deux"


def verif_refus_sortie_existe(script, d):
    _preexistant(script, d, 0)


def verif_refus_compagnon_existe(script, d):
    _preexistant(script, d, 1)


def verif_refus_journal_existe(script, d):
    _preexistant(script, d, 2)


def verif_refus_sortie_egale_cible(script, d):
    c, j, _ = poser(d, b"un deux", [{"ancien": "deux", "neuf": "2"}])
    r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", c)
    assert r.returncode == 2 and "existe déjà" in r.stderr, r.stderr
    assert c.read_bytes() == b"un deux"
    assert not os.path.lexists(str(c) + ".sha256")


def verif_refus_sortie_lien_pendant(script, d):
    c, j, s = poser(d, b"un deux", [{"ancien": "deux", "neuf": "2"}])
    vise = d / "vise.txt"
    os.symlink(vise, s)
    r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", s)
    assert r.returncode == 2 and "existe déjà" in r.stderr, r.stderr
    assert not os.path.lexists(vise)


def verif_refus_dossier_sortie_absent(script, d):
    c, j, _ = poser(d, b"un deux", [{"ancien": "deux", "neuf": "2"}])
    s = d / "nulle-part" / "sortie.txt"
    r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", s)
    assert r.returncode == 2 and "absent" in r.stderr, r.stderr
    assert not os.path.lexists(s.parent)


def verif_refus_cible_absente(script, d):
    _, j, s = poser(d, b"x", [{"ancien": "x", "neuf": "y"}])
    r = lancer(script, "--cible", d / "manque.txt", "--remplacements", j, "--sortie", s)
    assert r.returncode == 2 and "absent" in r.stderr, r.stderr
    assert not any(os.path.lexists(p) for p in ecrits(s))


def verif_refus_cible_dossier(script, d):
    _, j, s = poser(d, b"x", [{"ancien": "x", "neuf": "y"}])
    (d / "rep").mkdir()
    r = lancer(script, "--cible", d / "rep", "--remplacements", j, "--sortie", s)
    assert r.returncode == 2 and "pas un fichier ordinaire" in r.stderr, r.stderr
    assert not any(os.path.lexists(p) for p in ecrits(s))


def verif_refus_cible_non_utf8(script, d):
    attendre_refus(script, d, b"caf\xe9 au lait\n", [{"ancien": "lait", "neuf": "miel"}], "UTF-8 illisible")


def verif_refus_json_absent(script, d):
    c, _, s = poser(d, b"x", [{"ancien": "x", "neuf": "y"}])
    r = lancer(script, "--cible", c, "--remplacements", d / "manque.json", "--sortie", s)
    assert r.returncode == 2 and "absent" in r.stderr, r.stderr
    assert not any(os.path.lexists(p) for p in ecrits(s))


JSON_ARTEFACTS = [
    ("syntaxe", b"[{", "JSON illisible"),
    ("pas_une_liste", b'{"ancien": "a", "neuf": "b"}', "une liste est attendue"),
    ("liste_vide", b"[]", "liste vide"),
    ("pas_un_objet", b'["a"]', "un objet est attendu"),
    ("cle_manquante", b'[{"ancien": "a"}]', "clés"),
    ("cle_en_trop", b'[{"ancien": "a", "neuf": "b", "nouveau": "c"}]', "clés"),
    ("valeur_non_chaine", b'[{"ancien": 1, "neuf": "b"}]', "chaînes"),
    ("cle_en_double", b'[{"ancien": "a", "ancien": "z", "neuf": "b"}]', "en double"),
    ("substitut_isole", b'[{"ancien": "\\ud800", "neuf": "b"}]', "non encodable"),
    ("non_utf8", b'\xff[{"ancien": "a", "neuf": "b"}]', "UTF-8 illisible"),
    ("marque_ordre_octets", b'\xef\xbb\xbf[{"ancien": "a", "neuf": "b"}]', "JSON illisible"),
    ("constante_nan", b'[{"ancien": "a", "neuf": NaN}]', "non standard"),
    ("ancien_vide", b'[{"ancien": "", "neuf": "b"}]', "texte ancien vide"),
    ("neuf_egal_ancien", b'[{"ancien": "a", "neuf": "a"}]', "égal à l'ancien"),
]


def verif_refus_json_cle_en_double(script, d):
    attendre_refus(script, d, b"a\n", JSON_ARTEFACTS[7][1], "en double")


def verif_refus_options(script, d):
    c, j, s = poser(d, b"un deux", [{"ancien": "deux", "neuf": "2"}])
    for opt in ("--sur-place", "--sur", "--en-place"):
        r = lancer(script, "--cible", c, "--remplacements", j, "--sortie", s, opt)
        assert r.returncode == 2, (opt, r.returncode, r.stderr)
        assert not any(os.path.lexists(p) for p in ecrits(s))
    r = lancer(script, "--cible", c, "--remplacements", j)
    assert r.returncode == 2 and "--sortie" in r.stderr
    assert c.read_bytes() == b"un deux"


def charger(script: Path):
    spec = importlib.util.spec_from_file_location(f"outil_{sha(str(script).encode())[:12]}", script)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def verif_refus_ecriture_interrompue(script, d):
    """Garde de nettoyage : une faute au 3ᵉ fichier retire les deux premiers et refuse (aucun repli silencieux)."""
    m = charger(script)
    c, j, s = poser(d, b"un deux", [{"ancien": "deux", "neuf": "2"}])
    vrai_fsync, appels = os.fsync, []

    def fsync_qui_casse(fd):
        appels.append(fd)
        if len(appels) == 3:
            raise OSError(28, "plus de place (simulé)")
        return vrai_fsync(fd)

    os.fsync = fsync_qui_casse
    try:
        with pytest.raises(m.Refus) as e:
            m.executer(c, j, s)
    finally:
        os.fsync = vrai_fsync
    assert "écriture impossible" in str(e.value) and "SAUF" not in str(e.value), str(e.value)
    assert len(appels) == 3
    assert not any(os.path.lexists(p) for p in ecrits(s)), [p for p in ecrits(s) if os.path.lexists(p)]
    assert c.read_bytes() == b"un deux"


SAINS = [verif_sain_simple, verif_sain_octets, verif_sain_suppression, verif_sain_zones_contigues,
         verif_sain_application_simultanee, verif_sain_neufs_identiques, verif_sain_neuf_deja_present,
         verif_sain_ancien_non_chevauchant, verif_sain_json_echappements, verif_sain_option_sur_place_interdit,
         verif_sain_avertissement_fin_de_ligne]
ARTEFACTS = [verif_refus_ancien_absent, verif_refus_ancien_double, verif_refus_ancien_chevauchant,
             verif_refus_zones_chevauchantes, verif_refus_ancien_repete_dans_la_liste, verif_refus_neuf_jonction,
             verif_refus_neuf_dans_ancien, verif_refus_ancien_vide, verif_refus_sortie_existe, verif_refus_compagnon_existe,
             verif_refus_journal_existe, verif_refus_sortie_egale_cible, verif_refus_sortie_lien_pendant,
             verif_refus_dossier_sortie_absent, verif_refus_cible_absente, verif_refus_cible_dossier,
             verif_refus_cible_non_utf8, verif_refus_json_absent, verif_refus_options, verif_refus_ecriture_interrompue]


# ---------------------------------------------------------------------------------------------------------------- essais

@pytest.mark.parametrize("verif", SAINS + ARTEFACTS, ids=lambda f: f.__name__)
def test_outil(verif, tmp_path):
    verif(SCRIPT, tmp_path / "essai")


@pytest.mark.parametrize("nom, octets, motif", JSON_ARTEFACTS, ids=[a[0] for a in JSON_ARTEFACTS])
def test_json_artefact(nom, octets, motif, tmp_path):
    attendre_refus(SCRIPT, tmp_path, b"a\n", octets, motif)


def test_code_seul_en_bibliotheque_standard():
    """Bibliothèque standard seulement (aucun import du dépôt ni de paquet tiers)."""
    src = SCRIPT.read_text(encoding="utf-8")
    imports = {l.split()[1].split(".")[0] for l in src.splitlines() if l.startswith(("import ", "from "))}
    assert imports <= {"__future__", "argparse", "datetime", "hashlib", "json", "os", "sys", "pathlib"}, imports


# ------------------------------------------------------------------------------------- contrôle « trop beau » (R4)
# Chaque défaut est réintroduit dans une copie de l'outil ; le contrôle nommé doit le voir (échouer sur la copie).

MUTATIONS = [
    ("comptage_sans_chevauchement",
     [("i = meule.find(aiguille, i + 1)", "i = meule.find(aiguille, i + len(aiguille))")], verif_refus_ancien_chevauchant),
    ("controle_des_zones_retire", [("        if d2 < f1:\n", "        if False:\n")], verif_refus_zones_chevauchantes),
    ("lecture_en_mode_texte",
     [("return chemin.read_bytes()", 'return chemin.read_text(encoding="utf-8").encode("utf-8")')], verif_sain_octets),
    ("sortie_existante_reecrite",
     [("        if os.path.lexists(p):\n", "        if False:\n"), ('open(ch[cle], "xb")', 'open(ch[cle], "wb")')],
     verif_refus_sortie_existe),
    ("ancien_vide_accepte", [('        if a == "":\n', "        if False:\n")], verif_refus_ancien_vide),
    ("controle_du_neuf_retire", [("        if apres != avant + k:\n", "        if False:\n")], verif_refus_neuf_jonction),
    ("cle_en_double_acceptee",
     [("object_pairs_hook=_objet_sans_doublon, ", "")], verif_refus_json_cle_en_double),
    ("nettoyage_retire", [("                p.unlink()\n", "                pass\n")], verif_refus_ecriture_interrompue),
    ("application_sequentielle",
     [("    zones.sort(key=lambda z: (z[0], z[1]))\n",
       "    zones.sort(key=lambda z: (z[0], z[1]))\n"
       "    _seq = cible\n"
       "    for _r in remplacements:\n"
       "        _seq = _seq.replace(_r['ancien'], _r['neuf'], 1)\n"),
      ("    sortie = b\"\".join(morceaux)\n", "    sortie = _seq\n")],
     verif_sain_application_simultanee),
]


@pytest.mark.parametrize("nom, edits, verif", MUTATIONS, ids=[m[0] for m in MUTATIONS])
def test_trop_beau_defaut_reintroduit_vu(nom, edits, verif, tmp_path):
    src = SCRIPT.read_text(encoding="utf-8")
    for ancien, neuf in edits:
        assert src.count(ancien) == 1, (nom, ancien)
        src = src.replace(ancien, neuf)
    mutant = tmp_path / "mutant" / SCRIPT.name
    mutant.parent.mkdir()
    mutant.write_text(src, encoding="utf-8")
    compile(src, str(mutant), "exec")
    verif(SCRIPT, tmp_path / "temoin")          # le contrôle passe sur l'outil…
    with pytest.raises(AssertionError):         # … et échoue sur la copie défectueuse
        verif(mutant, tmp_path / "essai")
