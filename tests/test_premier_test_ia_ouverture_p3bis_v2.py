"""Fermeture et ouverture de P3-bis, v2 (`premier_test_ia.ouverture_p3bis_v2` ; texte de P3-bis, brouillon 9, `eb65773f…`,
plan, points 1, 6 et 8, « Liste d'arrêt », « Ce que le code et la chaîne doivent changer », points 2 (c) et 5 ; contre-lecture
du code v1, `7a074ad1…`, CP-01 à CP-09, CP-11, CP-15 à CP-17) : cas sains et artefacts (R5).
- Paquet des lectures : taille fixe, longueur de l'archive comprimée sur 8 octets (CP-04 : bornes, flux fini exactement après
  elle), sel neuf, seule l'empreinte imprimée, aucun fichier en clair ; artefacts de la v1 gardés.
- Archives et second paquet : nom de membre absolu ou à « .. », membre non ordinaire, nom en double, morceaux non
  consécutifs, index illisible ou d'un autre run, chemin hors de `donnees/<run>/` (CP-09) ; artefacts de la v1 gardés.
- Lectures fermées : durées écrites dans le paquet (CP-05), motif du dépliage imprimé et motif de la mise en paquet gardé dans
  l'espace fermé (CP-11), entropie exigée en mode décisif (CP-17), clone non git (CP-09).
- Garde d'ouverture : trois décisions, modes `pleine`, `reduite`, `pleine-anticipee` ; « ouvrir » sans garde adaptée conforme
  n'ouvre jamais (CP-01) ; une seule « ouvrir pleinement » après une ouverture réduite lue au journal ; antériorités strictes
  (CP-17) ; chaque refus de la liste d'arrêt avec son code (CP-02) ; journal au format exact, relu à chaque tentative,
  `deja-ouverte`, journal hors format, journal impossible (CP-06) ; paquets faux ou communs ; extraction en échec après la
  ligne du journal ; ligne de commande sans `--instant` (CP-08) ; fichier d'issue (accord exigé, sceau vérifié, CP-16)."""
import json
import os
import subprocess
import sys
import tarfile
import zlib
from pathlib import Path

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.premier_test_ia import ouverture_p3bis_v2 as ob
from controle_ia.scellement import sceller

RUN = "20261120-120000-p3bis-jouet"
RL, RLC = "20261120-130000-p3bis-lecture", "20261120-130100-p3bis-lc"
ESPACE = ob.ESPACE_DEFAUT
INSTANT = ob.instant_utc("2026-11-25T12:00:00Z")
PLUS_TARD = ob.instant_utc("2026-11-27T12:00:00Z")
DATE_PAQUET = "2026-11-12T12:00:00Z"
AVANT = "2026-11-10T10:00:00Z"
DATE_DECISION_LIGNE = "2026-11-20T12:30:00Z"

# motifs du registre de T0.7, recopiés de `src/controle_ia/t07/registre_v1.py` (sha256
# 914b8f374ce8f8bc6550d03c34c5f6c2a97ac93b8ce44da24fd88229185ffca0 ; dernier commit qui le touche 72be6999, présent à `main`
# 04a1b392 ; l. 39-43), comme le motif de T0.6 (CP-15) : l'essai n'importe aucun module de T0.7
MOTIFS_T07 = (r"[0-9a-f]{64}", r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", r"[A-Z0-9]+(?:-[A-Z0-9]+)+", "%Y-%m-%dT%H:%M:%SZ")
# liste fermée des codes de refus et en-tête du journal, recopiés du texte (brouillon 9, plan, point 8, l. 671-691)
CODES_DU_TEXTE = ("registre-absent, ligne-absente, ligne-double, ligne-mal-formee, sceau-faux, compagnon-absent, "
                  "date-posterieure, cle-inconnue, rendez-vous-non-consecutif, rendez-vous-non-croissant, "
                  "ligne-apres-decision-finale, ni-scores-ni-ouvrir, decision-maintenir, garde-adaptee-absente, "
                  "garde-adaptee-posterieure, deja-ouverte, paquet-faux")
ENTETE_DU_TEXTE = ("| clé | date | mode | appui | paquets | motif |", "|---|---|---|---|---|---|")


def _git(d, *args):
    return subprocess.run(["git", "-C", str(d), *args], check=True, capture_output=True, text=True).stdout


def _depot(d: Path) -> Path:
    d.mkdir(parents=True, exist_ok=True)
    _git(d, "init", "-q", "-b", "calcul")
    _git(d, "config", "user.email", "t@example.invalid")
    _git(d, "config", "user.name", "t")
    (d / ".gitignore").write_text("donnees/\n", encoding="utf-8")
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "init")
    return d


def _ecrire_scelle(d: Path, chemin: str, contenu: bytes) -> str:
    p = d / chemin
    p.parent.mkdir(parents=True, exist_ok=True)
    for f in (p, Path(str(p) + ".sha256")):
        f.unlink(missing_ok=True)
    p.write_bytes(contenu)
    return sceller(p)


def _run_fabrique(d: Path) -> dict:
    contenus = {f"donnees/{RUN}/{n}": f"{n} {k}".encode() * (300 + 50 * k) for k, n in enumerate(ob.DONNEES_EXIGEES)}
    contenus[f"diag/{RUN}/{ob.EPISODES}"] = json.dumps({"fiches": list(range(400))}).encode()
    for c, b in contenus.items():
        _ecrire_scelle(d, c, b)
    return contenus


def _sorties_fabriquees(d: Path, issue="vu", ligne=4) -> list[str]:
    _ecrire_scelle(d, f"runs/{RL}/manifeste.json", b'{"commande": "lecture de P3"}')
    _ecrire_scelle(d, f"diag/{RL}/lecture-p3.json", json.dumps({"resultat": {"issue": "x" * 300}}).encode())
    _ecrire_scelle(d, f"runs/{RLC}/manifeste.json", b'{"commande": "lecture complementaire"}')
    _ecrire_scelle(d, f"diag/{RLC}/lecture-p3bis.json",
                   json.dumps({"resultat": {"issue_mecanique": {"issue": issue, "ligne": ligne}}}).encode())
    (d / ESPACE).mkdir(exist_ok=True)
    (d / ESPACE / "lecture-p3.sortie").write_text('{"issue_mecanique": "..."}\n', encoding="utf-8")
    (d / ESPACE / "lecture-p3.erreurs").write_text("", encoding="utf-8")
    return ob.sorties_des_lectures(d, [RL, RLC], ESPACE)


@pytest.fixture
def clone(tmp_path):
    """Clone fermé : run fermé en second paquet (fichiers en clair retirés, comme dans un clone neuf)."""
    d = _depot(tmp_path / "clone")
    contenus = _run_fabrique(d)
    ob.fermer_run(d, RUN, taille_morceau=4096)
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "run")
    for c in list(contenus) + [x + ".sha256" for x in contenus]:
        (d / c).unlink()
    return {"d": d, "contenus": contenus}


# ================================================================================================= paquet des lectures
def test_fermer_taille_fixe_longueur_sur_8_octets_corps_comprime_puis_bourre(clone, capsys):
    d = clone["d"]
    deplies = ob.deplier_run(d, RUN, ESPACE)
    chemins = _sorties_fabriquees(d)
    originaux = {c: (d / c).read_bytes() for c in chemins if not c.endswith(ob.DEPLIE)}
    sha = ob.fermer(d, RUN, [RL, RLC], ESPACE, entropie=4242)
    assert capsys.readouterr().out == sha + "\n"                                   # seule l'empreinte est imprimée
    cible = d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES
    octets = cible.read_bytes()
    assert len(octets) == ob.TAILLE_PAQUET_LECTURES == 16_783_360 == 1_639 * 10_240
    assert [c for c in chemins + deplies if (d / c).exists()] == [] and not (d / ESPACE).exists()   # rien en clair
    _, archive = ob.relire_paquet_lectures(octets, 4242)
    fichiers = dict(ob.membres_de(archive))
    assert {c: fichiers[c] for c in originaux} == originaux
    corps = ob.membres_de(octets)[1][1]
    n = int.from_bytes(corps[:8], "big")                                            # CP-04 : 8 octets, poids fort en tête
    assert 0 < n < ob.TAILLE_CORPS_LECTURES - 8 and ob.decomprimer(corps[8:8 + n], bourre_permise=False)[0] == archive
    assert len(zlib.compress(corps[8:])) >= len(corps[8:])                         # flux et bourre incompressibles
    autre = ob.paquet_lectures(ob.tar_de([("x", b"y" * 5000)], tarfile.PAX_FORMAT), ob.tirer_sel())
    assert len(autre) == len(octets) and autre[:512] == octets[:512] and autre[1024:1536] == octets[1024:1536]
    assert autre[-1024:] == octets[-1024:] == bytes(1024) and autre[512:544] != octets[512:544]


def test_sel_neuf_a_chaque_mise_en_paquet(tmp_path):
    empreintes = set()
    for k in (1, 2):
        d = _depot(tmp_path / f"d{k}")
        _sorties_fabriquees(d)
        empreintes.add(ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None))
    assert len(empreintes) == 2


@pytest.mark.parametrize("artefact, motif", [
    ("trop gros", "trop grosses pour la taille fixe"), ("sel absent", "sel absent"), ("sel dérivé", "dérivé de l'entropie"),
    ("relecture fausse", "la relecture ne redonne"), ("corps tronqué", "corps de 16780799 octets")])
def test_fermer_artefacts_aucun_paquet_et_fichiers_gardes(tmp_path, monkeypatch, artefact, motif):
    d = _depot(tmp_path / "d")
    chemins = _sorties_fabriquees(d)
    if artefact == "trop gros":
        monkeypatch.setattr(ob, "TAILLE_CORPS_LECTURES", 100)
    elif artefact == "sel absent":
        monkeypatch.setattr(ob, "tirer_sel", lambda: b"")
    elif artefact == "sel dérivé":
        monkeypatch.setattr(ob, "tirer_sel", lambda: (4242).to_bytes(32, "big"))
    elif artefact == "relecture fausse":
        vraie = ob.relire_paquet_lectures
        monkeypatch.setattr(ob, "relire_paquet_lectures", lambda o, e=None: (vraie(o, e)[0], b"autre"))
    else:
        monkeypatch.setattr(ob, "tirer_bourre", lambda n: ob.secrets.token_bytes(n - 1))
    with pytest.raises(GardeArret, match=motif):
        ob.fermer(d, RUN, [RL, RLC], ESPACE, entropie=4242, imprimer=lambda x: None)
    assert not (d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES).exists()
    assert all((d / c).exists() for c in chemins)


def test_fermer_gardes_simples(tmp_path):
    d = _depot(tmp_path / "d")
    with pytest.raises(GardeArret, match="aucune sortie de lecture"):
        ob.fermer(d, RUN, [RL, RLC], ESPACE)
    _sorties_fabriquees(d)
    ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None)
    _sorties_fabriquees(d)
    with pytest.raises(GardeArret, match="R12"):
        ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None)


def _avec_longueur(octets: bytes, n: int) -> bytes:
    m = ob.membres_de(octets)
    return ob.tar_de([(ob.NOM_SEL, m[0][1]), (ob.NOM_CORPS, n.to_bytes(8, "big") + m[1][1][8:])])


def test_relecture_du_paquet_des_lectures_refuse_les_alterations():
    archive = ob.tar_de([("diag/x/lecture-p3bis.json", b"{}" * 2000)], tarfile.PAX_FORMAT)
    sel = ob.tirer_sel()
    octets = ob.paquet_lectures(archive, sel)
    assert ob.relire_paquet_lectures(octets) == (sel, archive)
    n = len(ob.comprimer(archive))
    with pytest.raises(GardeArret, match="16783359 octets"):
        ob.relire_paquet_lectures(octets[:-1])
    altere = bytearray(octets)
    altere[1536 + 8 + n // 2] ^= 0xFF                                               # un octet au milieu du flux xz
    with pytest.raises(GardeArret, match="flux xz illisible"):
        ob.relire_paquet_lectures(bytes(altere))
    # CP-04 : longueur hors des bornes, ou flux qui ne finit pas exactement après elle
    for longueur, motif in ((0, "hors de"), (ob.TAILLE_CORPS_LECTURES, "hors de"), (n - 1, "tronqué"),
                            (n + 1, "aucune bourre n'est permise")):
        with pytest.raises(GardeArret, match=motif):
            ob.relire_paquet_lectures(_avec_longueur(octets, longueur))
    assert ob.relire_paquet_lectures(_avec_longueur(octets, n))[1] == archive       # cas sain refait de même
    with pytest.raises(GardeArret, match="membres"):
        ob.relire_paquet_lectures(ob.tar_de([("sel.bin", sel), (ob.NOM_CORPS, ob.corps_lectures(archive))]))
    with pytest.raises(GardeArret, match="sel nul"):
        ob.relire_paquet_lectures(ob.paquet_lectures(archive, bytes(32)))


def test_motifs_du_registre_egaux_aux_chaines_recopiees_de_t07():
    assert (ob.SHA.pattern, ob.DATE.pattern, ob.CLE.pattern, ob.FORMAT_DATE) == MOTIFS_T07
    assert MOTIFS_T07[2] != r"[A-Z0-9]+(?:-[A-Z0-9]+)*"                            # artefact : une clé sans tiret passerait


def test_codes_de_refus_et_en_tete_du_journal_egaux_au_texte():
    assert ", ".join(ob.MOTIFS_REFUS) == CODES_DU_TEXTE and len(ob.MOTIFS_REFUS) == 17
    assert ob.ENTETE_JOURNAL == ENTETE_DU_TEXTE and ob.MODES == ("pleine", "reduite", "pleine-anticipee")
    with pytest.raises(ValueError, match="hors de la liste fermée"):
        ob.RefusOuverture("journal-impossible", "x")


# ================================================================================================= archives (CP-09)
def _tar_brut(entrees) -> bytes:
    import io
    flux = io.BytesIO()
    with tarfile.open(fileobj=flux, mode="w", format=tarfile.USTAR_FORMAT) as tf:
        for nom, octets, genre in entrees:
            ti = tarfile.TarInfo(nom)
            ti.type = genre
            ti.size = len(octets) if genre == tarfile.REGTYPE else 0
            if genre == tarfile.SYMTYPE:
                ti.linkname = "ailleurs"
            tf.addfile(ti, io.BytesIO(octets) if genre == tarfile.REGTYPE else None)
    return flux.getvalue()


def test_membres_de_cas_sain_et_noms_ou_genres_refuses():
    assert ob.membres_de(_tar_brut([("a/b.json", b"{}", tarfile.REGTYPE)])) == [("a/b.json", b"{}")]
    for entrees, motif in (([("/abs/x", b"1", tarfile.REGTYPE)], "nom de membre"),
                           ([("a/../x", b"1", tarfile.REGTYPE)], "nom de membre"),
                           ([("lien", b"", tarfile.SYMTYPE)], "pas un fichier ordinaire"),
                           ([("x", b"1", tarfile.REGTYPE), ("x", b"2", tarfile.REGTYPE)], "en double")):
        with pytest.raises(GardeArret, match=motif):
            ob.membres_de(_tar_brut(entrees))
    with pytest.raises(GardeArret, match="illisible"):
        ob.membres_de(b"pas une archive" * 100)


# ================================================================================================= second paquet
def test_second_paquet_morceaux_index_relecture_et_episodes_exclus(tmp_path):
    d = _depot(tmp_path / "d")
    contenus = _run_fabrique(d)
    index = ob.fermer_run(d, RUN, taille_morceau=4096)
    assert len(index["morceaux"]) >= 2 and max(m["taille"] for m in index["morceaux"]) <= 4096
    relu = ob.relire_run(d, RUN)
    assert relu == {c: (d / c).read_bytes() for c in ob.fichiers_du_run(d, RUN)} and set(contenus) <= set(relu)
    _git(d, "add", "-A")
    _git(d, "commit", "-qm", "run")
    ob.exiger_aucun_clair(d, RUN)
    _git(d, "add", "-f", f"diag/{RUN}/{ob.EPISODES}")
    with pytest.raises(GardeArret, match="suivis en clair"):
        ob.exiger_aucun_clair(d, RUN)


@pytest.mark.parametrize("artefact, motif", [("sel absent", "sel absent"), ("morceau trop gros", "hors de"),
                                             ("fichier absent", "absents ou sans compagnon"), ("relecture fausse", "relecture")])
def test_second_paquet_artefacts_rien_ne_reste(tmp_path, monkeypatch, artefact, motif):
    d = _depot(tmp_path / "d")
    _run_fabrique(d)
    taille = 4096
    if artefact == "sel absent":
        monkeypatch.setattr(ob, "tirer_sel", lambda: b"")
    elif artefact == "morceau trop gros":
        taille = ob.TAILLE_MORCEAU_MAX + 1
    elif artefact == "fichier absent":
        (d / "donnees" / RUN / "scores-p3.npz").unlink()
    else:
        vraie = ob.relire_run
        monkeypatch.setattr(ob, "relire_run", lambda r, run: {**vraie(r, run), "donnees/x": b"en trop"})
    with pytest.raises(GardeArret, match=motif):
        ob.fermer_run(d, RUN, taille_morceau=taille)
    assert not list((d / "diag" / RUN).glob(ob.PAQUET_RUN + "*")) and not (d / "diag" / RUN / ob.INDEX_RUN).exists()


def _index(d: Path) -> Path:
    return d / "diag" / RUN / ob.INDEX_RUN


def _reecrire_index(d: Path, transformer) -> None:
    p = _index(d)
    texte = transformer(p.read_text(encoding="utf-8"))
    Path(str(p) + ".sha256").unlink()
    p.write_text(texte, encoding="utf-8")
    sceller(p)


def test_relecture_du_second_paquet_index_morceaux_et_chemins(tmp_path):
    """CP-09 : index illisible, d'un autre run, morceaux non consécutifs, morceau altéré ; chemin hors de donnees/<run>/."""
    d = _depot(tmp_path / "d")
    _run_fabrique(d)
    ob.fermer_run(d, RUN, taille_morceau=4096)
    sain = _index(d).read_text(encoding="utf-8")
    assert ob.relire_run(d, RUN)
    cas = (("illisible", lambda t: t[:-20], "illisible"),
           ("autre run", lambda t: t.replace(f'"run": "{RUN}"', '"run": "20261120-999999-autre"'), "autre run"),
           ("non consécutifs", lambda t: t.replace(f"{ob.PAQUET_RUN}.001", f"{ob.PAQUET_RUN}.002", 1), "non consécutifs"),
           ("morceaux vides", lambda t: json.dumps({**json.loads(t), "morceaux": []}), "non consécutifs"))
    for nom, transformer, motif in cas:
        _reecrire_index(d, transformer)
        with pytest.raises(GardeArret, match=motif):
            ob.relire_run(d, RUN)
        _reecrire_index(d, lambda t: sain)
    assert ob.relire_run(d, RUN)                                                    # index rétabli : cas sain
    # chemin hors de donnees/<run>/ : second paquet fabriqué à la main, scellé comme le vrai
    e = _depot(tmp_path / "e")
    archive = ob.tar_de([(f"donnees/{RUN}/a", b"1"), ("autre/x", b"2")], tarfile.PAX_FORMAT)
    octets = ob.paquet_run(archive, ob.tirer_sel())
    dossier = e / "diag" / RUN
    dossier.mkdir(parents=True)
    (dossier / f"{ob.PAQUET_RUN}.000").write_bytes(octets)
    index = {"version": 1, "run": RUN, "paquet": ob.PAQUET_RUN, "sha256": ob._sha(octets), "taille": len(octets),
             "taille_morceau_max": 90_000_000,
             "morceaux": [{"nom": f"{ob.PAQUET_RUN}.000", "sha256": sceller(dossier / f"{ob.PAQUET_RUN}.000"),
                           "taille": len(octets)}]}
    (dossier / ob.INDEX_RUN).write_text(json.dumps(index), encoding="utf-8")
    sceller(dossier / ob.INDEX_RUN)
    with pytest.raises(GardeArret, match="hors de donnees/<run>/"):
        ob.relire_run(e, RUN)


def test_deplier_cas_sain_puis_chemin_present_ou_suivi(clone):
    d, contenus = clone["d"], clone["contenus"]
    deplies = ob.deplier_run(d, RUN, ESPACE)
    assert deplies == list(ob.fichiers_lus(RUN)) and len(deplies) == 8
    assert all((d / c).read_bytes() == b for c, b in contenus.items() if c in deplies)
    assert _git(d, "status", "--porcelain", "--untracked-files=all") == ""
    with pytest.raises(GardeArret, match="déjà suivis ou présents"):
        ob.deplier_run(d, RUN, ESPACE)


def test_exclure_localement_hors_d_un_clone_git(tmp_path, monkeypatch):
    """CP-09 : dossier hors d'un clone git : garde (cas sain : clone, motif ajouté une seule fois). Plafond de recherche
    de git posé sur le dossier de l'essai : git ne remonte jamais vers un dépôt qui l'engloberait."""
    monkeypatch.setenv("GIT_CEILING_DIRECTORIES", str(tmp_path))
    d = _depot(tmp_path / "d")
    ob.exclure_localement(d, ["/x/", "/x/"])
    ob.exclure_localement(d, ["/x/"])
    assert (d / ".git" / "info" / "exclude").read_text(encoding="utf-8").splitlines().count("/x/") == 1
    (tmp_path / "pas-git").mkdir()
    with pytest.raises(GardeArret, match="n'est pas un clone git"):
        ob.exclure_localement(tmp_path / "pas-git", ["/x/"])


# ================================================================================================= lectures fermées
def _lectures_factices(monkeypatch, issue="vu"):
    """Lectures remplacées par deux processus qui écrivent des sorties fabriquées (la vraie chaîne est jouée par l'essai
    différentiel et par le bout en bout décisif) ; seules les commandes changent."""
    def commandes(run, lecture, lecture_c, prereg, entropie):
        code = ("import json, pathlib, sys\nfor d in sys.argv[1:]:\n    p = pathlib.Path(d)\n    p.mkdir(parents=True)\n"
                f"    (p / 'sortie.json').write_text(json.dumps({{'issue': {issue!r}}}))\nprint('{{}}')\n")
        return [("lecture de P3", "lecture-p3", [sys.executable, "-c", code, f"runs/{lecture}", f"diag/{lecture}"]),
                ("lecture complémentaire", "lecture-p3bis", [sys.executable, "-c", code, f"runs/{lecture_c}",
                                                              f"diag/{lecture_c}"])]
    monkeypatch.setattr(ob, "commandes_des_lectures", commandes)


def test_lectures_fermees_cas_sain_durees_dans_le_paquet(clone, monkeypatch):
    d = clone["d"]
    _lectures_factices(monkeypatch)
    sortie = []
    assert ob.lectures_fermees(d, RUN, RL, RLC, entropie=4242, imprimer=sortie.append) == 0
    assert sortie[:4] == ["code dépliage du second paquet : 0", "code lecture de P3 : 0", "code lecture complémentaire : 0",
                          "code mise en paquet : 0"] and sortie[4].startswith("paquet des lectures : ") and len(sortie) == 5
    _, archive = ob.relire_paquet_lectures((d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES).read_bytes())
    durees = json.loads(dict(ob.membres_de(archive))[f"{ESPACE}/{ob.DUREES}"])        # CP-05 : classe 2, dans le paquet
    assert set(durees["durees"]) == {"depliage_s", "lecture-p3_s", "lecture-p3bis_s", "chaine_avant_mise_en_paquet_s"}
    assert all(v >= 0 for v in durees["durees"].values()) and not (d / ESPACE).exists()


def test_lectures_fermees_motif_de_la_mise_en_paquet_garde_dans_l_espace_ferme(clone, monkeypatch):
    """CP-11 : un refus de `fermer` n'imprime qu'un code ; son motif est écrit dans l'espace fermé, qui reste en place."""
    d = clone["d"]
    _lectures_factices(monkeypatch)
    monkeypatch.setattr(ob, "tirer_sel", lambda: b"")
    sortie = []
    assert ob.lectures_fermees(d, RUN, RL, RLC, imprimer=sortie.append) == 1
    assert sortie[-1] == "code mise en paquet : 1" and not any("sel" in x for x in sortie)
    assert "sel absent" in (d / ESPACE / ob.ERREURS_MISE_EN_PAQUET).read_text(encoding="utf-8")
    assert (d / ESPACE / ob.DUREES).is_file() and not (d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES).exists()


def test_lectures_fermees_depliage_refuse_imprime_code_et_motif(tmp_path):
    """CP-11 : le motif d'un refus du dépliage (intégrité du second paquet, aucune issue) est imprimé."""
    d = _depot(tmp_path / "d")
    sortie = []
    assert ob.lectures_fermees(d, RUN, RL, RLC, imprimer=sortie.append) == 1
    assert sortie[0] == "code dépliage du second paquet : 1" and sortie[1].startswith("motif du dépliage : ")
    assert "compagnon" in sortie[1] or "absent" in sortie[1]


def test_lectures_fermees_mode_decisif_exige_l_entropie(clone, capsys):
    d = clone["d"]
    with pytest.raises(GardeArret, match="sans --entropie"):
        ob.lectures_fermees(d, RUN, RL, RLC, prereg="prereg/p.md", imprimer=lambda x: None)
    with pytest.raises(GardeArret, match="sans --entropie"):
        ob._main(["lectures-fermees", "--racine", str(d), "--run", RUN, "--lecture", RL, "--lecture-complementaire", RLC,
                  "--prereg", "prereg/p.md"])
    assert not (d / ESPACE).exists()                                                # rien n'est déplié


# ================================================================================================= garde d'ouverture
def _ligne(cle, date, chemin, sha):
    return f"| {cle} | {date} | {chemin} | {sha} |"


def _decision(d, n, decision, date):
    chemin = ob.FICHIER_DECISION.format(n=n)
    return chemin, _ecrire_scelle(d, chemin, f"# Rendez-vous de P3-bis\n\nDécision : {decision}\nDate : {date}\n".encode())


def _monter(d, *, ecrits=True, normal=True, t07_present=False, rdv=(), garde=False, scellement_t07=False, extra=(),
            date_ecrits=AVANT, date_garde="2026-11-19T10:00:00Z", date_scellement="2026-11-18T10:00:00Z",
            texte_garde=b"texte scelle de T0.7 avec la garde adaptee"):
    """Registres de la garde : écrits de T0.7, lignes de T0.7 au registre des scellements, décisions du rendez-vous
    (décision, date de la décision et date de la ligne), ligne de la garde adaptée. Le journal n'est pas touché."""
    (d / "registres").mkdir(exist_ok=True)
    lignes = ["# Registre des préalables de P3-bis", ""]
    if ecrits:
        for k in ob.CLES_ECRITS:
            chemin = f"prereg/T0.7-ecrit-{k.lower()}.md"
            lignes.append(_ligne(k, date_ecrits, chemin, _ecrire_scelle(d, chemin, k.encode())))
    sha_t07 = _ecrire_scelle(d, "prereg/T0.7-sondes-v0-v1.md", b"texte scelle de T0.7 avec la garde adaptee")
    sha_garde = sha_t07 if texte_garde == b"texte scelle de T0.7 avec la garde adaptee" else \
        _ecrire_scelle(d, "prereg/T0.7-autre.md", texte_garde)
    chemin_garde = "prereg/T0.7-sondes-v0-v1.md" if sha_garde == sha_t07 else "prereg/T0.7-autre.md"
    if garde:
        lignes.append(_ligne(ob.CLE_GARDE_ADAPTEE, date_garde, chemin_garde, sha_garde))
    for n, x in enumerate(rdv, start=1):
        decision, date = x[0], x[1]
        date_ligne = x[2] if len(x) > 2 else date
        chemin, sha = _decision(d, n, decision, date)
        lignes.append(_ligne(f"RENDEZ-VOUS-P3BIS-{n}", date_ligne, chemin, sha))
    lignes += list(extra)
    (d / ob.REGISTRE_PREALABLES).write_text("\n".join(lignes) + "\n", encoding="utf-8")
    sc = ["# Registre des scellements (T0.6, T0.7, P3-bis)", "", _ligne("SCELLEMENT-P3BIS", AVANT, "prereg/p3bis.md", "a" * 64)]
    if normal:
        for cle, nom in ((ob.SCORES_T07, "scores-actions-t07.npz"), (ob.SONDES_T07, "sondes-t07.json")):
            chemin = f"diag/t07-run/{nom}"
            sha = _ecrire_scelle(d, chemin, nom.encode())
            if not t07_present:
                (d / chemin).unlink()                                      # D8 : compagnon seul, fichier fermé de T0.7 absent
            sc.append(_ligne(cle, "2026-11-22T10:00:00Z", chemin, sha))
    if scellement_t07:
        sc.append(_ligne(ob.SCELLEMENT_T07, date_scellement, "prereg/T0.7-sondes-v0-v1.md", sha_t07))
    (d / ob.REGISTRE_SCELLEMENTS).write_text("\n".join(sc) + "\n", encoding="utf-8")


@pytest.fixture
def ouvrable(clone):
    """Clone fermé dont les deux paquets sont faits (lectures fabriquées, issue « vu »)."""
    d = clone["d"]
    ob.deplier_run(d, RUN, ESPACE)
    originaux = {c: (d / c).read_bytes() for c in _sorties_fabriquees(d) if not c.endswith(ob.DEPLIE)}
    ob.fermer(d, RUN, [RL, RLC], ESPACE, imprimer=lambda x: None)
    return {"d": d, "originaux": originaux, "contenus": clone["contenus"]}


def _ouvrir(d, mode="pleine", sortie="sortie", instant=INSTANT, **k):
    lignes = []
    r = ob.ouvrir(d, mode, RUN, d.parent / sortie, date_paquet=DATE_PAQUET, instant=instant, imprimer=lignes.append, **k)
    return r, lignes


def _journal(d) -> list[dict]:
    return ob.exiger_format_journal((d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8"))


def _refus(d, code, mode="pleine", sortie="sortie", instant=INSTANT, motif=None):
    """Un refus : le bon code, rien d'ouvert, une ligne de plus au journal, au format exact, avec ce code."""
    avant = len(_journal(d)) if (d / ob.JOURNAL_OUVERTURES).exists() else 0
    with pytest.raises(ob.RefusOuverture) as e:
        _ouvrir(d, mode, sortie, instant)
    assert e.value.code == code, str(e.value)
    if motif:
        assert motif in e.value.texte, e.value.texte
    assert not (d.parent / sortie).exists()
    j = _journal(d)
    assert len(j) == avant + 1 and j[-1]["cle"] == ob.CLE_REFUS and j[-1]["mode"] == mode
    assert j[-1]["motif"].startswith(f"{code} : ")
    return e.value, j[-1]


def _sha_paquets(d):
    sha_l = (d / ob.dossier_ferme(RUN) / (ob.PAQUET_LECTURES + ".sha256")).read_text(encoding="utf-8").split()[0]
    sha_r = json.loads((d / "diag" / RUN / ob.INDEX_RUN).read_text(encoding="utf-8"))["sha256"]
    return f"{sha_l} {sha_r}"


def _sha_ligne(d, registre, cle):
    for x in (d / registre).read_text(encoding="utf-8").splitlines():
        if x.startswith(f"| {cle} |"):
            return x.split("|")[4].strip()
    raise AssertionError(cle)


def test_chemin_normal_ouverture_pleine_sans_le_fichier_de_t07_journal_exact(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    r, lignes = _ouvrir(d)
    assert r["mode"] == "pleine" and r["chemin"] == "chemin normal" and r["reserves"] == []
    s = d.parent / "sortie"
    assert {c: (s / c).read_bytes() for c in ouvrable["originaux"]} == ouvrable["originaux"]
    assert all((s / c).read_bytes() == b for c, b in ouvrable["contenus"].items())    # second paquet ouvert aussi
    appui = (f"SCORES-T07={_sha_ligne(d, ob.REGISTRE_SCELLEMENTS, 'SCORES-T07')} "
             f"SONDES-T07={_sha_ligne(d, ob.REGISTRE_SCELLEMENTS, 'SONDES-T07')}")
    attendu = "\n".join(ENTETE_DU_TEXTE + (f"| OUVERTURE-P3BIS | 2026-11-25T12:00:00Z | pleine | {appui} | "
                                           f"{_sha_paquets(d)} | - |",)) + "\n"
    assert (d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8") == attendu       # format exact du texte (CP-02)
    assert lignes[0].startswith("ouverture pleine (chemin normal)")
    with pytest.raises(GardeArret, match="R12"):                                     # dossier de sortie déjà là : erreur
        _ouvrir(d)                                                                  # d'appel, sans ligne au journal
    assert len(_journal(d)) == 1
    _refus(d, "deja-ouverte", sortie="s2")                                          # après « pleine », aucune ouverture
    _refus(d, "deja-ouverte", "pleine-anticipee", sortie="s3")


def test_chemin_normal_fichier_de_t07_present_verifie(ouvrable):
    d = ouvrable["d"]
    _monter(d, t07_present=True)
    (d / "diag/t07-run/sondes-t07.json").write_bytes(b"altere")                      # artefact : fichier présent altéré
    _refus(d, "ni-scores-ni-ouvrir", motif="présent, d'empreinte")
    _monter(d, t07_present=True)                                                    # cas sain : fichier présent et égal
    assert _ouvrir(d, sortie="s2")[0]["mode"] == "pleine"


def test_branche_1_reduite_puis_ouvrir_pleinement_puis_plus_rien(ouvrable):
    """« ouvrir » avec la garde adaptée en vigueur : `reduite` seulement ; puis une seule décision « ouvrir pleinement »,
    après l'ouverture réduite lue au journal : `pleine-anticipee` ; puis `deja-ouverte`."""
    d = ouvrable["d"]
    rdv1 = ("ouvrir", "2026-11-20T12:20:00Z", DATE_DECISION_LIGNE)
    _monter(d, normal=False, rdv=[rdv1], garde=True, scellement_t07=True)
    _refus(d, "ni-scores-ni-ouvrir", "pleine-anticipee", sortie="s0", motif="ouverture réduite seulement")
    _refus(d, "ligne-absente", "pleine", sortie="s0", motif="exige SCORES-T07")
    r, lignes = _ouvrir(d, "reduite")
    assert r["mode"] == "reduite" and r["chemin"].startswith("branche 1") and lignes[0].startswith("ouverture réduite")
    sha_rdv1 = _sha_ligne(d, ob.REGISTRE_PREALABLES, "RENDEZ-VOUS-P3BIS-1")
    sha_garde = _sha_ligne(d, ob.REGISTRE_PREALABLES, ob.CLE_GARDE_ADAPTEE)
    j = _journal(d)
    assert (j[-1]["cle"], j[-1]["mode"], j[-1]["appui"], j[-1]["paquets"], j[-1]["motif"]) == (
        "OUVERTURE-P3BIS", "reduite", f"RENDEZ-VOUS-P3BIS-1={sha_rdv1} GARDE-ADAPTEE-T07-P3BIS={sha_garde}",
        _sha_paquets(d), "-")
    _refus(d, "deja-ouverte", "reduite", sortie="s1", instant=PLUS_TARD)            # après « reduite », pas de « reduite »
    # « ouvrir pleinement » écrite après l'ouverture réduite : pleine-anticipee, appui sur la ligne 2
    _monter(d, normal=False, rdv=[rdv1, ("ouvrir pleinement", "2026-11-26T10:00:00Z")], garde=True, scellement_t07=True)
    r, _ = _ouvrir(d, "pleine-anticipee", sortie="s2", instant=PLUS_TARD)
    assert r["mode"] == "pleine-anticipee" and "nœud de Lazar" in r["chemin"]
    assert _journal(d)[-1]["appui"] == f"RENDEZ-VOUS-P3BIS-2={_sha_ligne(d, ob.REGISTRE_PREALABLES, 'RENDEZ-VOUS-P3BIS-2')}"
    _refus(d, "deja-ouverte", "pleine", sortie="s3", instant=PLUS_TARD + 60)


def test_complement_pleine_apres_la_reduite(ouvrable):
    d = ouvrable["d"]
    rdv1 = ("ouvrir", "2026-11-20T12:20:00Z", DATE_DECISION_LIGNE)
    _monter(d, normal=False, rdv=[rdv1], garde=True, scellement_t07=True)
    _ouvrir(d, "reduite")
    _monter(d, normal=True, rdv=[rdv1], garde=True, scellement_t07=True)              # SCORES-T07 et SONDES-T07 inscrites
    r, _ = _ouvrir(d, "pleine", sortie="s2", instant=PLUS_TARD)
    assert r["chemin"] == "complément de l'ouverture réduite"
    assert [x["mode"] for x in _journal(d) if x["cle"] == "OUVERTURE-P3BIS"] == ["reduite", "pleine"]


def test_ouvrir_sans_garde_adaptee_conforme_n_ouvre_jamais(ouvrable):
    """CP-01 : sous « ouvrir », aucune branche 2 : garde adaptée absente, postérieure (égalité comprise, CP-17), citant un
    autre texte, ou T0.7 non scellé : refus en tout mode, rien d'ouvert."""
    d = ouvrable["d"]
    rdv1 = ("ouvrir", "2026-11-20T12:20:00Z", DATE_DECISION_LIGNE)
    cas = ((dict(garde=False, scellement_t07=True), "garde-adaptee-absente", "aucune ligne GARDE-ADAPTEE"),
           (dict(garde=True, scellement_t07=False), "garde-adaptee-absente", "T0.7 non scellé"),
           (dict(garde=True, scellement_t07=True, date_garde=DATE_DECISION_LIGNE), "garde-adaptee-posterieure",
            "GARDE-ADAPTEE-T07-P3BIS datée"),
           (dict(garde=True, scellement_t07=True, date_scellement=DATE_DECISION_LIGNE), "garde-adaptee-posterieure",
            "SCELLEMENT-T07 datée"),
           (dict(garde=True, scellement_t07=True, date_garde="2026-11-21T10:00:00Z"), "garde-adaptee-posterieure", ""),
           (dict(garde=True, scellement_t07=True, texte_garde=b"autre texte de T0.7"), "garde-adaptee-absente",
            "ne cite pas le texte scellé"))
    for k, (reglages, code, motif) in enumerate(cas):
        _monter(d, normal=False, rdv=[rdv1], **reglages)
        _refus(d, code, "reduite", sortie=f"r{k}", motif=motif)
        _refus(d, code, "pleine-anticipee", sortie=f"a{k}")
        _refus(d, "ligne-absente", "pleine", sortie=f"p{k}")
    assert not [x for x in _journal(d) if x["cle"] == "OUVERTURE-P3BIS"]
    _monter(d, normal=False, rdv=[rdv1], garde=True, scellement_t07=True,              # cas sain : une seconde avant
            date_garde="2026-11-20T12:29:59Z", date_scellement="2026-11-20T12:29:59Z")
    assert _ouvrir(d, "reduite", sortie="sain")[0]["mode"] == "reduite"


def test_branche_2_ouvrir_pleinement_et_maintenir(ouvrable):
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z"), ("ouvrir pleinement", "2026-11-23T09:00:00Z")])
    _refus(d, "ni-scores-ni-ouvrir", "reduite", sortie="s0", motif="sans dernière décision « ouvrir »")
    _refus(d, "ligne-absente", "pleine", sortie="s0")
    r, _ = _ouvrir(d, "pleine-anticipee")
    assert r["chemin"].startswith("branche 2") and [x["decision"] for x in r["decisions"]] == ["maintenir",
                                                                                              "ouvrir pleinement"]


def test_suite_des_decisions_refusee(ouvrable):
    """« ouvrir » suivi d'autre chose qu'une seule « ouvrir pleinement » après une ouverture réduite lue au journal, ou
    « ouvrir pleinement » suivi de quoi que ce soit : `ligne-apres-decision-finale`."""
    d = ouvrable["d"]
    o = ("ouvrir", "2026-11-20T12:20:00Z", DATE_DECISION_LIGNE)
    suites = ([o, ("maintenir", "2026-11-21T12:10:00Z")],
              [o, ("ouvrir pleinement", "2026-11-21T12:10:00Z")],                 # aucune ouverture réduite au journal
              [("ouvrir pleinement", "2026-11-20T12:10:00Z"), ("maintenir", "2026-11-21T12:10:00Z")],
              [("ouvrir pleinement", "2026-11-20T12:10:00Z"), ("ouvrir", "2026-11-21T12:10:00Z")])
    for k, rdv in enumerate(suites):
        _monter(d, normal=False, rdv=rdv, garde=True, scellement_t07=True)
        _refus(d, "ligne-apres-decision-finale", "pleine-anticipee", sortie=f"s{k}")
    # ouverture réduite faite, puis « ouvrir pleinement » datée AVANT elle, ou suivie d'une autre ligne : refus
    _monter(d, normal=False, rdv=[o], garde=True, scellement_t07=True)
    _ouvrir(d, "reduite")
    _monter(d, normal=False, rdv=[o, ("ouvrir pleinement", "2026-11-24T10:00:00Z")], garde=True, scellement_t07=True)
    _refus(d, "ligne-apres-decision-finale", "pleine-anticipee", sortie="t1", instant=PLUS_TARD)
    _monter(d, normal=False, rdv=[o, ("ouvrir pleinement", "2026-11-26T10:00:00Z"), ("maintenir", "2026-11-26T11:00:00Z")],
            garde=True, scellement_t07=True)
    _refus(d, "ligne-apres-decision-finale", "pleine-anticipee", sortie="t2", instant=PLUS_TARD)


def test_ecrit_apres_la_mise_en_paquet_accepte_avec_reserve(ouvrable):
    d = ouvrable["d"]
    _monter(d, date_ecrits="2026-11-15T10:00:00Z")
    r, lignes = _ouvrir(d)
    assert len(r["reserves"]) == 3 and all("écrit après la lecture fermée" in x for x in r["reserves"])
    assert sum(x.startswith("réserve : ") for x in lignes) == 3


def _remplacer(d, chemin, avant, apres):
    p = d / chemin
    texte = p.read_text(encoding="utf-8")
    assert avant in texte
    p.write_text(texte.replace(avant, apres, 1), encoding="utf-8")


def _ajouter(d, chemin, ligne):
    p = d / chemin
    p.write_text(p.read_text(encoding="utf-8") + ligne + "\n", encoding="utf-8")


def _premiere(d, chemin, prefixe):
    return [x for x in (d / chemin).read_text(encoding="utf-8").splitlines() if x.startswith(prefixe)][0]


REFUS = {
    "registre absent": (lambda d: (d / ob.REGISTRE_PREALABLES).unlink(), "registre-absent"),
    "ligne absente": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, "| ECRIT-ENGAGEMENT-ETAPE-A-P3BIS |", "x"),
                      "ligne-absente"),
    "ligne en double": (lambda d: _ajouter(d, ob.REGISTRE_PREALABLES, _premiere(d, ob.REGISTRE_PREALABLES, "| ECRIT-PERIM")),
                        "ligne-double"),
    "date mal formée": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, AVANT, "2026-11-10"), "ligne-mal-formee"),
    "date impossible": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, AVANT, "2026-02-30T10:00:00Z"), "ligne-mal-formee"),
    "colonnes": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, f"| {AVANT} |", "|"), "ligne-mal-formee"),
    "sceau faux": (lambda d: (d / "prereg/T0.7-ecrit-ecrit-perimetre-jeux-p3bis.md").write_bytes(b"autre"), "sceau-faux"),
    "fichier cité absent": (lambda d: (d / "prereg/T0.7-ecrit-ecrit-perimetre-jeux-p3bis.md").unlink(), "sceau-faux"),
    "compagnon absent": (lambda d: (d / "prereg/T0.7-ecrit-ecrit-lancement-relance-p3bis.md.sha256").unlink(),
                         "compagnon-absent"),
    "date postérieure": (lambda d: _remplacer(d, ob.REGISTRE_PREALABLES, AVANT, "2026-11-25T12:00:00Z"), "date-posterieure"),
    "clé inconnue": (lambda d: _ajouter(d, ob.REGISTRE_PREALABLES, _ligne("AUTRE-CLE-P3BIS", AVANT, "x.md", "b" * 64)),
                     "cle-inconnue"),
    "première cellule": (lambda d: _ajouter(d, ob.REGISTRE_PREALABLES, _ligne("écrit libre", AVANT, "x.md", "b" * 64)),
                         "ligne-mal-formee"),
    "ni T0.7 ni ouvrir": (lambda d: _monter(d, normal=False), "ni-scores-ni-ouvrir"),
    "maintenir": (lambda d: _monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z")]), "decision-maintenir"),
    "ligne après ouvrir": (lambda d: _monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:10:00Z"),
                                                                    ("maintenir", "2026-11-21T12:10:00Z")]),
                           "ligne-apres-decision-finale"),
    "ligne après ouvrir pleinement": (lambda d: _monter(d, normal=False, rdv=[("ouvrir pleinement", "2026-11-20T12:10:00Z"),
                                                                               ("maintenir", "2026-11-21T12:10:00Z")]),
                                      "ligne-apres-decision-finale"),
    "non croissants": (lambda d: _monter(d, normal=False, rdv=[("maintenir", "2026-11-21T12:10:00Z"),
                                                                ("ouvrir", "2026-11-21T12:10:00Z")]),
                       "rendez-vous-non-croissant"),
    "non consécutifs": (lambda d: (_monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z"),
                                                                  ("ouvrir", "2026-11-21T12:10:00Z")]),
                                   _remplacer(d, ob.REGISTRE_PREALABLES, "RENDEZ-VOUS-P3BIS-2", "RENDEZ-VOUS-P3BIS-3")),
                        "rendez-vous-non-consecutif"),
    "numéro 01": (lambda d: (_monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:10:00Z")]),
                             _remplacer(d, ob.REGISTRE_PREALABLES, "RENDEZ-VOUS-P3BIS-1", "RENDEZ-VOUS-P3BIS-01")),
                  "cle-inconnue"),                  # clé lue au motif [1-9][0-9]* du lecteur de T0.7 (R-2103)
    "décision avant le rendez-vous": (lambda d: _monter(d, normal=False, rdv=[("ouvrir", "2026-11-19T12:10:00Z")]),
                                      "ligne-mal-formee"),
    "décision datée après sa ligne": (lambda d: _monter(d, normal=False, rdv=[("ouvrir pleinement", "2026-11-21T12:10:00Z",
                                                                               "2026-11-21T12:09:59Z")]),
                                      "ligne-mal-formee"),
    "décision, autre fichier": (lambda d: (_monter(d, normal=False, rdv=[("ouvrir", "2026-11-20T12:10:00Z")]),
                                           _remplacer(d, ob.REGISTRE_PREALABLES, "rendez-vous-P3-bis-v1.md",
                                                      "rendez-vous-P3-bis-v2.md")),
                                "ligne-mal-formee"),
    "décision inconnue": (lambda d: _monter(d, normal=False, rdv=[("ouvrir tout", "2026-11-20T12:10:00Z")]),
                          "ligne-mal-formee"),
    "garde adaptée en double": (lambda d: (_monter(d, normal=False, garde=True),
                                           _remplacer(d, ob.REGISTRE_PREALABLES, "# Registre", "| GARDE-ADAPTEE-T07-P3BIS | "
                                                      f"{AVANT} | prereg/T0.7-sondes-v0-v1.md | {'c' * 64} |\n# Registre")),
                                "ligne-double"),
    "empreinte de la ligne autre": (lambda d: _remplacer(
        d, ob.REGISTRE_PREALABLES, (d / "prereg/T0.7-ecrit-ecrit-perimetre-jeux-p3bis.md.sha256").read_text(
            encoding="utf-8").split()[0], "f" * 64), "sceau-faux"),
    "SCORES-T07 compagnon autre": (lambda d: (d / "diag/t07-run/scores-actions-t07.npz.sha256").write_text(
        "d" * 64 + "  scores-actions-t07.npz\n", encoding="utf-8"), "ni-scores-ni-ouvrir"),
    "SCORES-T07 postérieure": (lambda d: _remplacer(d, ob.REGISTRE_SCELLEMENTS, "| SCORES-T07 | 2026-11-22T10:00:00Z",
                                                    "| SCORES-T07 | 2026-11-25T12:00:00Z"), "ni-scores-ni-ouvrir"),
    "SCORES-T07 en double": (lambda d: _ajouter(d, ob.REGISTRE_SCELLEMENTS, _premiere(d, ob.REGISTRE_SCELLEMENTS,
                                                                                       "| SCORES-T07")), "ligne-double"),
    "SONDES-T07 mal formée": (lambda d: _remplacer(d, ob.REGISTRE_SCELLEMENTS, "| SONDES-T07 | 2026-11-22T10:00:00Z |",
                                                   "| SONDES-T07 | 2026-11-22 |"), "ligne-mal-formee"),
}


@pytest.mark.parametrize("cas", sorted(REFUS))
def test_refus_de_la_garde_code_de_la_liste_fermee_rien_ouvert_et_journalise(ouvrable, cas):
    d = ouvrable["d"]
    _monter(d)
    modifier, code = REFUS[cas]
    modifier(d)
    refus, ligne = _refus(d, code)
    assert ligne["date"] == "2026-11-25T12:00:00Z" and ligne["paquets"] == "-"       # paquets non lus
    assert [x["cle"] for x in _journal(d)] == ["REFUS-OUVERTURE-P3BIS"]


def test_appui_presente_d_un_refus(ouvrable):
    d = ouvrable["d"]
    _monter(d, normal=False, rdv=[("maintenir", "2026-11-20T12:10:00Z")], garde=True)
    _, ligne = _refus(d, "decision-maintenir", "reduite")
    assert ligne["appui"] == (f"RENDEZ-VOUS-P3BIS-1={_sha_ligne(d, ob.REGISTRE_PREALABLES, 'RENDEZ-VOUS-P3BIS-1')} "
                              f"GARDE-ADAPTEE-T07-P3BIS={_sha_ligne(d, ob.REGISTRE_PREALABLES, ob.CLE_GARDE_ADAPTEE)}")
    _monter(d, normal=False)
    _, ligne = _refus(d, "ni-scores-ni-ouvrir", "pleine-anticipee", sortie="s2")
    assert ligne["appui"] == "-"


# ================================================================================================= journal (CP-02, CP-06)
SHA_A, SHA_B = "a" * 64, "b" * 64


def _lj(*cellules):
    return "| " + " | ".join(cellules) + " |"


def _texte_journal(*lignes):
    return "\n".join(ENTETE_DU_TEXTE + lignes) + "\n"


OUV_REDUITE = _lj("OUVERTURE-P3BIS", "2026-11-25T12:00:00Z", "reduite", f"RENDEZ-VOUS-P3BIS-1={SHA_A} "
                  f"GARDE-ADAPTEE-T07-P3BIS={SHA_B}", f"{SHA_A} {SHA_B}", "-")
OUV_PLEINE = _lj("OUVERTURE-P3BIS", "2026-11-26T12:00:00Z", "pleine", f"SCORES-T07={SHA_A} SONDES-T07={SHA_B}",
                 f"{SHA_A} {SHA_B}", "-")
REFUS_SAIN = _lj("REFUS-OUVERTURE-P3BIS", "2026-11-24T12:00:00Z", "pleine-anticipee", "-", "-",
                 "decision-maintenir : décision « maintenir »")


def test_format_du_journal_cas_sain_et_chaque_ligne_hors_format():
    lignes = ob.exiger_format_journal(_texte_journal(REFUS_SAIN, OUV_REDUITE, OUV_PLEINE))
    assert [(x["cle"], x["mode"]) for x in lignes] == [("REFUS-OUVERTURE-P3BIS", "pleine-anticipee"),
                                                       ("OUVERTURE-P3BIS", "reduite"), ("OUVERTURE-P3BIS", "pleine")]
    with pytest.raises(GardeArret, match="fichier vide"):                            # D-3 (R-2103) : fichier vide hors
        ob.exiger_format_journal("")                                                 # format (accepté avant R-2103)
    hors = {
        "cellule en trop": _lj("REFUS-OUVERTURE-P3BIS", "2026-11-24T12:00:00Z", "pleine", "-", "-", "deja-ouverte : x", "y"),
        "cellule en moins": _lj("REFUS-OUVERTURE-P3BIS", "2026-11-24T12:00:00Z", "pleine", "-", "deja-ouverte : x"),
        "clé inconnue": REFUS_SAIN.replace("REFUS-OUVERTURE-P3BIS", "REFUS-P3BIS"),
        "date mal formée": REFUS_SAIN.replace("2026-11-24T12:00:00Z", "2026-11-24 12:00"),
        "mode inconnu": OUV_PLEINE.replace("| pleine |", "| plein |"),
        "appui d'un autre mode": OUV_PLEINE.replace("| pleine |", "| pleine-anticipee |"),
        "appui à clé inconnue": REFUS_SAIN.replace("| - | - |", f"| AUTRE-T07={SHA_A} | - |"),
        "appui en prose": OUV_PLEINE.replace(f"SCORES-T07={SHA_A} SONDES-T07={SHA_B}", "registre des scellements"),
        "paquets d'une ouverture": OUV_PLEINE.replace(f"| {SHA_A} {SHA_B} | - |", "| - | - |"),
        "motif d'une ouverture": OUV_PLEINE[:-4] + " x |",
        "motif hors liste": REFUS_SAIN.replace("decision-maintenir :", "journal-impossible :"),
        "motif sans texte": REFUS_SAIN.replace(" : décision « maintenir »", ""),
        "sans barre finale": REFUS_SAIN[:-1],
    }
    for nom, ligne in hors.items():
        with pytest.raises(GardeArret, match="hors format"):
            ob.exiger_format_journal(_texte_journal(REFUS_SAIN, ligne))
    for texte, motif in ((_texte_journal(OUV_REDUITE, OUV_REDUITE), "ordre interdit"),
                         (_texte_journal(OUV_PLEINE, OUV_REDUITE), "ordre interdit"),
                         ("# Journal\n\n" + _texte_journal(REFUS_SAIN), "en-tête"),
                         (_texte_journal(REFUS_SAIN)[:-1], "sans saut de ligne"),
                         (_texte_journal(REFUS_SAIN, ""), "ligne 4")):
        with pytest.raises(GardeArret, match=motif):
            ob.exiger_format_journal(texte)


def test_ligne_ecrite_verifiee_avant_l_ecriture(tmp_path):
    (tmp_path / "registres").mkdir()
    brute = ob.ligne_journal(ob.CLE_REFUS, INSTANT, "reduite", "-", "-", "deja-ouverte : déjà")
    ob.inscrire(tmp_path, brute)
    assert (tmp_path / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8") == _texte_journal(brute)   # en-tête créé
    with pytest.raises(GardeArret, match="mode"):
        ob.ligne_journal(ob.CLE_REFUS, INSTANT, "reduit", "-", "-", "deja-ouverte : x")
    with pytest.raises(GardeArret, match="motif"):
        ob.ligne_journal(ob.CLE_REFUS, INSTANT, "reduite", "-", "-", "inconnu : x")
    with pytest.raises(GardeArret, match="cellules"):
        ob.inscrire(tmp_path, brute[:-2] + "| x |")
    assert len(ob.exiger_format_journal((tmp_path / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8"))) == 1


def test_journal_hors_format_refus_ligne_mal_formee_et_ligne_neuve_qui_suit(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    (d / ob.JOURNAL_OUVERTURES).write_text(_texte_journal(REFUS_SAIN, "| ligne écrite à la main |"), encoding="utf-8")
    with pytest.raises(ob.RefusOuverture) as e:
        _ouvrir(d)
    assert e.value.code == "ligne-mal-formee" and "hors format" in e.value.texte and not (d.parent / "sortie").exists()
    lignes = (d / ob.JOURNAL_OUVERTURES).read_text(encoding="utf-8").splitlines()
    assert lignes[3] == "| ligne écrite à la main |"                                 # jamais corrigée en place
    assert ob.lire_ligne_journal(lignes[4])["motif"].startswith("ligne-mal-formee : ")
    # journal à l'ordre interdit (deux ouvertures réduites) : même refus
    (d / ob.JOURNAL_OUVERTURES).write_text(_texte_journal(OUV_REDUITE, OUV_REDUITE), encoding="utf-8")
    with pytest.raises(ob.RefusOuverture, match="ordre interdit"):
        _ouvrir(d)


def test_journal_impossible_a_ecrire_refus_rien_ouvert(ouvrable, capsys, monkeypatch):
    """CP-06 : le journal ne peut pas être écrit (chemin occupé par un dossier, ou dossier `registres/` absent) : refus
    (code 2), rien d'ouvert, aucune ligne."""
    d = ouvrable["d"]
    _monter(d)
    (d / ob.JOURNAL_OUVERTURES).mkdir()
    with pytest.raises(ob.JournalImpossible, match="impossible|Is a directory"):
        _ouvrir(d)
    assert not (d.parent / "sortie").exists()
    monkeypatch.setattr(ob.time, "time", lambda: INSTANT)
    assert ob._main(["ouvrir", "--racine", str(d), "--mode", "pleine", "--run", RUN, "--sortie", str(d.parent / "cli"),
                     "--date-paquet", DATE_PAQUET]) == 2
    assert capsys.readouterr().err.startswith("REFUS : ") and not (d.parent / "cli").exists()
    (d / ob.JOURNAL_OUVERTURES).rmdir()
    import shutil
    shutil.rmtree(d / "registres")
    with pytest.raises(ob.JournalImpossible, match="absent"):                        # registres/ absent : rien d'écrit
        _ouvrir(d, sortie="s2")
    assert not (d / "registres").exists() and not (d.parent / "s2").exists()


# ================================================================================================= paquets (CP-09)
def test_paquet_altere_refus_paquet_faux_journalise(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    p = d / ob.dossier_ferme(RUN) / ob.PAQUET_LECTURES
    sain = p.read_bytes()
    p.write_bytes(sain[:-1] + bytes([sain[-1] ^ 1]))                                 # sceau faux : paquets non lus
    _, ligne = _refus(d, "paquet-faux", motif="garde")
    assert ligne["paquets"] == "-" and ligne["appui"].startswith("SCORES-T07=")
    p.write_bytes(sain)
    m = d / "diag" / RUN / f"{ob.PAQUET_RUN}.000"
    b = m.read_bytes()
    m.write_bytes(b[:-1] + bytes([b[-1] ^ 1]))                                       # morceau altéré : empreintes connues
    _, ligne = _refus(d, "paquet-faux", sortie="s2")
    assert ligne["paquets"] == _sha_paquets(d)
    m.write_bytes(b)
    assert _ouvrir(d, sortie="s3")[0]["mode"] == "pleine"                            # paquets rétablis : cas sain


def test_chemins_communs_aux_deux_paquets_refus(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    archive = ob.tar_de([(f"diag/{RUN}/{ob.EPISODES}", b"{}"), (f"diag/{RLC}/lecture-p3bis.json", b"{}")],
                        tarfile.PAX_FORMAT)
    _ecrire_scelle(d, f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}", ob.paquet_lectures(archive, ob.tirer_sel()))
    _, ligne = _refus(d, "paquet-faux", motif="dans les deux paquets")
    assert ligne["paquets"] == _sha_paquets(d)


def test_paquets_autres_que_ceux_de_l_ouverture_reduite(ouvrable):
    d = ouvrable["d"]
    rdv1 = ("ouvrir", "2026-11-20T12:20:00Z", DATE_DECISION_LIGNE)
    _monter(d, normal=True, rdv=[rdv1], garde=True, scellement_t07=True)
    _ouvrir(d, "reduite")
    archive = ob.tar_de([(f"diag/{RLC}/lecture-p3bis.json", b'{"autre": 1}')], tarfile.PAX_FORMAT)
    _ecrire_scelle(d, f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}", ob.paquet_lectures(archive, ob.tirer_sel()))
    _refus(d, "paquet-faux", "pleine", sortie="s2", instant=PLUS_TARD, motif="autres que ceux de l'ouverture reduite")


def test_date_de_mise_en_paquet_illisible_refus(ouvrable):
    d = ouvrable["d"]
    _monter(d)
    with pytest.raises(ob.RefusOuverture) as e:                                      # ni --date-paquet ni commit du paquet
        ob.ouvrir(d, "pleine", RUN, d.parent / "s", instant=INSTANT, imprimer=lambda x: None)
    assert e.value.code == "paquet-faux" and "date de la mise en paquet" in e.value.texte
    _git(d, "add", "-f", f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}", f"{ob.dossier_ferme(RUN)}/{ob.PAQUET_LECTURES}.sha256")
    _git(d, "commit", "-qm", "paquet")
    assert ob.ouvrir(d, "pleine", RUN, d.parent / "s2", instant=INSTANT, imprimer=lambda x: None)["mode"] == "pleine"


def test_extraction_en_echec_apres_la_ligne_du_journal(ouvrable, monkeypatch):
    """CP-09 : l'écriture du dossier de sortie échoue après la ligne `OUVERTURE-P3BIS` : arrêt, rien laissé, le journal
    garde l'ouverture (sens prudent pour T0.7)."""
    d = ouvrable["d"]
    _monter(d)

    def rename(a, b):
        raise OSError("disque plein simulé")
    monkeypatch.setattr(ob.os, "rename", rename)
    with pytest.raises(GardeArret, match="extraction en échec après la ligne OUVERTURE-P3BIS"):
        _ouvrir(d)
    assert not (d.parent / "sortie").exists() and not list(d.parent.glob(".ouverture-*"))
    assert [x["cle"] for x in _journal(d)] == ["OUVERTURE-P3BIS"]


# ================================================================================================= ligne de commande
def test_ligne_de_commande_code_2_sur_refus_0_sur_ouverture_sans_instant(ouvrable, capsys, monkeypatch):
    d = ouvrable["d"]
    _monter(d, normal=False)
    monkeypatch.setattr(ob.time, "time", lambda: INSTANT)                            # horloge de l'essai (CP-08)
    args = ["ouvrir", "--racine", str(d), "--mode", "pleine", "--run", RUN, "--sortie", str(d.parent / "cli"),
            "--date-paquet", DATE_PAQUET]
    assert ob._main(args) == 2
    assert capsys.readouterr().err.startswith("REFUS : ni-scores-ni-ouvrir : ")
    _monter(d)
    assert ob._main(args) == 0 and (d.parent / "cli" / "diag" / RLC / "lecture-p3bis.json").is_file()
    with pytest.raises(SystemExit):                                                  # CP-08 : plus d'option --instant
        ob._main(args[:-2] + ["--instant", str(INSTANT)])
    with pytest.raises(SystemExit):                                                  # ancien mode « plein » refusé
        ob._main(["ouvrir", "--racine", str(d), "--mode", "plein", "--run", RUN, "--sortie", str(d.parent / "x")])
    with pytest.raises(GardeArret, match="mode"):
        ob.ouvrir(d, "plein", RUN, d.parent / "y", instant=INSTANT)
    assert len(_journal(d)) == 2                                                     # erreurs d'appel : aucune ligne


# ================================================================================================= fichier d'issue
def _issue(d, **doc):
    base = {"issue": "vu", "ligne": 4, "verdict": ob.VERDICT, "verdict_sha256": "e" * 64}
    base.update(doc)
    p = d / "docs" / "verdicts" / "verdict-P3-bis-v1-issue.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    for f in (p, Path(str(p) + ".sha256")):
        f.unlink(missing_ok=True)
    p.write_text(json.dumps({k: v for k, v in base.items() if v is not None}), encoding="utf-8")
    sceller(p)
    return p


def test_exposer_issue_accord_exige_et_sceau_de_la_lecture_verifie(tmp_path, capsys):
    """CP-16 : lignes 2 à 5 : `--lecture-p3bis` exigée, son sceau vérifié, accord avec l'issue mécanique ; ligne 1 sans."""
    lc = tmp_path / "lecture-p3bis.json"
    lc.write_text(json.dumps({"resultat": {"issue_mecanique": {"issue": "vu", "ligne": 4}}}), encoding="utf-8")
    sceller(lc)
    p = _issue(tmp_path)
    assert ob.exposer_issue(p, lc) == {"issue": "vu", "ligne": 4}
    assert ob._main(["exposer-issue", str(p), "--lecture-p3bis", str(lc)]) == 0
    assert json.loads(capsys.readouterr().out) == {"issue": "vu", "ligne": 4}
    with pytest.raises(GardeArret, match="--lecture-p3bis"):                         # accord exigé
        ob.exposer_issue(p)
    with pytest.raises(GardeArret, match="--lecture-p3bis"):
        ob._main(["exposer-issue", str(p)])
    assert ob.exposer_issue(_issue(tmp_path, issue="non lu", ligne=1)) == {"issue": "non lu", "ligne": 1}
    p = _issue(tmp_path)
    for doc, motif in (({"ligne": 5}, "hors de la table"), ({"issue": "peut-être"}, "hors de la table"),
                       ({"ligne": True}, "hors de la table"), ({"verdict": "autre.md"}, "hors de forme"),
                       ({"verdict_sha256": "E" * 64}, "hors de forme"), ({"verdict": None}, "clés")):
        with pytest.raises(GardeArret, match=motif):
            ob.exposer_issue(_issue(tmp_path, **doc), lc)
    with pytest.raises(GardeArret, match="désaccord .* nœud de Lazar"):
        ob.exposer_issue(_issue(tmp_path, issue="non vu", ligne=5), lc)
    lc.write_text(json.dumps({"resultat": {"issue_mecanique": {"issue": "vu", "ligne": 4}}}) + " ", encoding="utf-8")
    with pytest.raises(GardeArret, match="compagnon|empreinte"):                     # lecture altérée après son sceau
        ob.exposer_issue(_issue(tmp_path), lc)
    (Path(str(lc) + ".sha256")).unlink()
    with pytest.raises(GardeArret, match="compagnon|absent"):                        # lecture non scellée
        ob.exposer_issue(_issue(tmp_path), lc)
