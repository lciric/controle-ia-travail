"""v6 (R-2433) : essais de la v5 rejoués sur la v6, puis embargo, formes de clés élargies, données personnelles, paquets incrémentaux et README public. Copie expurgée du dépôt (`scripts/depot_expurge.py`, R-104, R-105) : l'appariement des retraits ne traverse pas
les dossiers, aucun fichier que le code charge n'est retiré, et aucun fichier retiré ne survit dans une archive gardée
(cas sain et artefact, R5)."""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import io
import subprocess
import tarfile
import zipfile
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("depot_expurge_v6", RACINE / "scripts" / "depot_expurge_v6.py")
de = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(de)


def test_appariement_par_segment():
    assert de.correspond("docs/sources/invites-2606.07054-v1/invites/B1.txt",
                         "docs/sources/invites-2606.07054-v1/invites/*.txt")       # appariement par segment
    assert not de.correspond("docs/sources/invites-2606.07054-v1/derivees/B1-env-a-v1.txt",
                             "docs/sources/invites-2606.07054-v1/*.txt")          # le défaut de la première version
    assert not de.correspond("docs/sources/invites-2606.07054-v1/verification.txt",
                             "docs/sources/invites-2606.07054-v1/invites/*.txt")
    assert de.correspond("donnees/run/sorties.tar", "donnees/**")
    assert not de.correspond("donnees-bis/x", "donnees/**")


def test_segment_double_etoile_au_milieu():
    motif = "brouillons/**/corpus-primaire-*/**"
    assert de.correspond("brouillons/corpus-primaire-v1/a.md", motif)                      # zéro dossier
    assert de.correspond("brouillons/canal/envois/x/corpus-primaire-v2/sous/b.json", motif)
    assert not de.correspond("brouillons/canal/corpus-primaire-v1", motif)                # le dossier seul, sans fichier
    assert not de.correspond("brouillons/canal/corpus-secondaire-v1/a.md", motif)
    assert not de.correspond("docs/corpus-primaire-v1/a.md", motif)


def test_corpus_et_lots_de_tournoi_jamais_dans_la_copie():
    """Le corpus intégral des idées ne quitte jamais le dépôt privé. Cas sains : une note voisine et le compagnon
    `.sha256` du lot restent."""
    assert de.motif_de("brouillons/canal-reprise-releve-v1/envois/p/corpus-primaire-v3/idee-001.md") is not None
    assert de.motif_de("livrables/lot-ideation-tournoi-v47-v1.zip") is not None
    assert de.motif_de("livrables/lot-ideation-tournoi-v47-v1.zip.sha256") is None
    assert de.motif_de("brouillons/canal-reprise-releve-v1/envois/p/synthese-v1.md") is None


def test_releve_de_gemini_jamais_dans_la_copie():
    """R-348 : la clé Vast.ai gardée par Lazar (N-038 (c)) est écrite en clair sous `gemini/` ; ce dossier ne passe
    jamais dans la copie expurgée. Cas sain : un fichier du programme reste."""
    porteur = "gemini/11_EDIFICE_CERTIFIE_54_CORRECTIFS_L_STAR_V2_TAIF/run_campagne_gpu_72h_5_volets_llama3.py"
    assert de.motif_de(porteur) is not None
    assert de.motif_de("gemini/README.md") is not None
    assert de.motif_de("src/controle_ia/scellement.py") is None
    assert de.motif_de("gemini-bis/x.py") is None


def test_fichiers_charges_par_le_code_jamais_retires():
    suivis = subprocess.run(["git", "-C", str(RACINE), "ls-files"], capture_output=True, text=True,
                            check=True).stdout.split("\n")
    charges = [f for f in suivis if any(de.correspond(f, g) for g in de.GARDES)]
    assert len(charges) == 34                       # invites des deux papiers (18 + 7) et gabarits adaptés (6), index
    assert all(de.motif_de(f) is None for f in charges)


def test_retrait_d_un_fichier_charge_arrete(monkeypatch):
    monkeypatch.setattr(de, "RETRAITS", de.RETRAITS + [("docs/sources/invites-2606.07054-v1/derivees/*.txt", "x")])
    with pytest.raises(SystemExit, match="chargé par le code"):
        de.motif_de("docs/sources/invites-2606.07054-v1/derivees/B1-env-a-v1.txt")


def _zip(membres: dict[str, bytes]) -> bytes:
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w") as z:
        for nom, contenu in membres.items():
            z.writestr(nom, contenu)
    return tampon.getvalue()


def _tar(membres: dict[str, bytes]) -> bytes:
    tampon = io.BytesIO()
    with tarfile.open(fileobj=tampon, mode="w") as t:
        for nom, contenu in membres.items():
            info = tarfile.TarInfo(nom)
            info.size = len(contenu)
            t.addfile(info, io.BytesIO(contenu))
    return tampon.getvalue()


def _git_factice(depot: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(depot), "-c", "user.name=essai", "-c", "user.email=essai@invalid",
                    "-c", "commit.gpgsign=false", *args], check=True, capture_output=True)


def test_fichier_retire_survivant_dans_une_archive(tmp_path):
    retire = b"page d'un papier de tiers"
    empreintes = {hashlib.sha256(retire).hexdigest(), hashlib.sha256(b"").hexdigest()}
    assert de.survivants("a.zip", _zip({"notes.md": b"notre texte", "vide.txt": b""}), empreintes) == []  # cas sain
    assert de.survivants("a.zip", _zip({"autre/nom.txt": retire}), empreintes) == ["a.zip!autre/nom.txt"]   # par empreinte
    assert de.survivants("a.tar", _tar({"./docs/sources/pdf/2601.00001v1.pdf": b"x"}), empreintes) == [
        "a.tar!docs/sources/pdf/2601.00001v1.pdf"]                                                           # par chemin
    assert de.survivants("a.zip", _zip({"dedans.tar": _tar({"p.txt": retire})}), empreintes) == [
        "a.zip!dedans.tar!p.txt"]                                                                            # imbriqué
    with pytest.raises(SystemExit, match="format non examiné"):
        de.survivants("a.zip", _zip({"b.gz": gzip.compress(retire)}), empreintes)
    # paquet git : un fichier retiré du dernier commit mais présent dans l'historique est trouvé
    depot = tmp_path / "depot"
    depot.mkdir()
    _git_factice(depot, "init", "-q", "-b", "main")
    (depot / "docs/sources/pdf").mkdir(parents=True)
    (depot / "docs/sources/pdf/2601.00001v1.pdf").write_bytes(b"%PDF de tiers")
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "1")
    _git_factice(depot, "rm", "-q", "docs/sources/pdf/2601.00001v1.pdf")
    (depot / "a.md").write_text("notre texte", encoding="utf-8")
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "2")
    _git_factice(depot, "bundle", "create", "-q", str(tmp_path / "p.bundle"), "main")
    assert de.survivants("p.bundle", (tmp_path / "p.bundle").read_bytes(), set()) == [
        "p.bundle!docs/sources/pdf/2601.00001v1.pdf"]


def _depot_factice(depot: Path, copie_cachee: bool, compresse: bool = False) -> None:
    depot.mkdir()
    _git_factice(depot, "init", "-q", "-b", "main")
    (depot / "README.md").write_text("# essai\n\n" + de.PARAGRAPHE_README + "\n", encoding="utf-8")
    (depot / "docs/sources/pdf").mkdir(parents=True)
    (depot / "docs/sources/pdf/2601.00001v1.pdf").write_bytes(b"%PDF copie d'un papier de tiers")
    (depot / "livrables/candidature-ea-funds-v1").mkdir(parents=True)        # retiré ; sa feuille de style reste ailleurs
    (depot / "livrables/candidature-ea-funds-v1/style.css").write_bytes(b"body { margin: 0 }")
    (depot / "livrables/rendu-v1").mkdir()
    (depot / "livrables/rendu-v1/style.css").write_bytes(b"body { margin: 0 }")
    membres = {"notes.md": b"notre texte", "rendu-v1/style.css": b"body { margin: 0 }"}
    if copie_cachee:
        membres["copie/papier.pdf"] = b"%PDF copie d'un papier de tiers"
    (depot / "livrables/rendu-v1.zip").write_bytes(_zip(membres))
    if compresse:
        (depot / "livrables/journal.txt.gz").write_bytes(gzip.compress(b"journal"))
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "factice")


def test_copie_de_bout_en_bout_saine_puis_artefact(tmp_path, monkeypatch, capsys):
    _depot_factice(tmp_path / "sain", copie_cachee=False)
    monkeypatch.setattr(de, "RACINE", tmp_path / "sain")
    assert de.main(["HEAD", str(tmp_path / "sortie-sain")]) == 0
    (paquet,) = (tmp_path / "sortie-sain").glob("*.bundle")
    clone = tmp_path / "clone"
    subprocess.run(["git", "clone", "-q", str(paquet), str(clone)], check=True, capture_output=True)  # sans -b
    assert not (clone / "docs/sources/pdf/2601.00001v1.pdf").exists()
    assert (clone / "docs/sources/pdf/2601.00001v1.pdf").name in (clone / "EXPURGE.md").read_text(encoding="utf-8")
    assert (clone / "livrables/rendu-v1.zip").exists()
    assert de.REMPLACEMENT_README in (clone / "README.md").read_text(encoding="utf-8")

    _depot_factice(tmp_path / "artefact", copie_cachee=True)
    monkeypatch.setattr(de, "RACINE", tmp_path / "artefact")
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "sortie-artefact")]) == 1
    assert "livrables/rendu-v1.zip!copie/papier.pdf" in capsys.readouterr().err
    assert list((tmp_path / "sortie-artefact").glob("*.bundle")) == []


def test_garde_des_secrets_saine_et_artefact():
    """R-349 : valeurs de clés de l'environnement et formes connues, dans un fichier ou dans une archive gardée ; la
    valeur n'est jamais dite ; chemins, noms de configuration et valeurs courtes ne sont pas lus comme des clés ; `RR_*`
    le sont depuis R-351."""
    fausse = "0123456789abcdef" * 4
    env = {"FAUSSE_API_KEY": fausse, "RR_ANTHROPIC_API_KEY": "rr" + "7" * 30, "SESSION_TOKEN_FILE": "/run/jeton/abc123def456ghi789",
           "GIT_CONFIG_KEY_0": "http.https://example.invalid/.extraheader", "HOME": "/root", "COURT_TOKEN": "a1b2"}
    valeurs = de.valeurs_secretes(env)
    assert set(valeurs) == {"FAUSSE_API_KEY", "RR_ANTHROPIC_API_KEY"}
    assert de.secrets_dans("notes.md", b"aucun secret ici", valeurs) == []
    trouve = de.secrets_dans("src/config.py", ("CLE = '" + fausse + "'").encode(), valeurs)
    assert trouve == ["src/config.py : valeur de FAUSSE_API_KEY"] and fausse not in " ".join(trouve)
    assert de.secrets_dans("b.py", b"x = 'sk-ant-" + b"A" * 30 + b"'", {}) == ["b.py : clé Anthropic"]
    brut = de.secrets_dans("livrables/r.zip", _zip({"d/e.txt": fausse.encode()}), valeurs)
    assert "livrables/r.zip!d/e.txt : valeur de FAUSSE_API_KEY" in brut  # zip non compressé : aussi l'archive elle-même
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("d/e.txt", ("prefixe " * 50 + fausse).encode())
    compresse = de.secrets_dans("livrables/c.zip", tampon.getvalue(), valeurs)
    assert compresse == ["livrables/c.zip!d/e.txt : valeur de FAUSSE_API_KEY"], "compressé : seul le membre la révèle"


def test_copie_refusee_si_un_secret_est_garde(tmp_path, monkeypatch, capsys):
    _depot_factice(tmp_path / "secret", copie_cachee=False)
    fausse = "fedcba9876543210" * 4
    (tmp_path / "secret" / "notes-cle.md").write_text(f"cle : {fausse}\n", encoding="utf-8")
    _git_factice(tmp_path / "secret", "add", "-A")
    _git_factice(tmp_path / "secret", "commit", "-q", "-m", "secret")
    monkeypatch.setattr(de, "RACINE", tmp_path / "secret")
    monkeypatch.setenv("FAUSSE_API_KEY", fausse)
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "sortie-secret")]) == 1
    err = capsys.readouterr().err
    assert "notes-cle.md : valeur de FAUSSE_API_KEY" in err and fausse not in err
    assert list((tmp_path / "sortie-secret").glob("*.bundle")) == []


def test_archive_d_un_format_non_examine_arrete(tmp_path, monkeypatch):
    _depot_factice(tmp_path / "gz", copie_cachee=False, compresse=True)
    monkeypatch.setattr(de, "RACINE", tmp_path / "gz")
    with pytest.raises(SystemExit, match="format non examiné"):
        de.main(["HEAD", str(tmp_path / "sortie-gz")])
    assert list((tmp_path / "sortie-gz").glob("*.bundle")) == []


def test_pdf_de_sous_dossier_retire():
    d = de
    assert any(d.correspond("docs/sources/pdf/bisociation-litterature-reelle-v1/arxiv-2306.01495.pdf", m) for m, _ in d.RETRAITS)
    assert not any(d.correspond("docs/sources/pdf/bisociation-litterature-reelle-v1/arxiv-2306.01495.pdf.sha256", m)
                   for m, _ in d.RETRAITS)


def test_v4_tar_gz_examine_et_gzip_non_tar_refuse(tmp_path):
    """v4 (R-1576) : un tar.gz est examiné comme un tar (cas sain : membres rendus) ; un gzip qui n'est pas un tar arrête (artefact)."""
    import gzip, io, tarfile
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as t:
        info = tarfile.TarInfo("a/b.txt"); donnees = b"bonjour"; info.size = len(donnees); t.addfile(info, io.BytesIO(donnees))
    membres = de._membres("x.tar.gz", buf.getvalue())
    assert membres == [("a/b.txt", b"bonjour")]
    with pytest.raises(SystemExit):
        de._membres("x.gz", gzip.compress(b"pas un tar du tout"))


# --- v6 (R-2433) ---------------------------------------------------------------------------------------------------

def test_v6_embargo_par_nom_sain_et_artefact():
    """Chemins sous embargo jusqu'au verdict de P3-bis : visés par nom, à toute profondeur ; voisins sains gardés."""
    vises = ["donnees/bras-attaque-v3/x.json", "donnees/mode-tenu-a-l-ecart-v1/a.md", "docs/notes/bras-attaque/n.md",
             "registres/index-bras-attaque-v8.md", "brouillons/x/anteriorite-bras-informe-v2.md",
             "diag/20261111-010101-t06-reel/lecture-sondes-t06.json", "diag/20261110-7a-course/r.json",
             "runs/20261111-7b-confirmation/manifeste.json", "donnees/lecture-b-7a-quarantaine-v1/l.json",
             "donnees/mesure-unanime-v15-sortie-v1/s.json", "prep/etiqueteur-v2-lecture-interrompue-reprise-v1/e.md",
             "docs/notes/g0-deux-semaines-v1/e3-ter-v1/lecture-7a-v1/lecture-A.md",
             "docs/notes/integration-bras-attaque-v1/a.md.sha256"]
    for chemin in vises:
        assert de.sous_embargo(chemin), chemin
        assert de.motif_de(chemin) == de.RAISON_EMBARGO, chemin
    sains = ["docs/notes/epreuve-etiqueteur-v1/n.md", "prereg/preenregistrement-mesure-unanime-v15.md",
             "docs/procedures/ordre-fille-course-confirmation-7b-v1-brouillon1.md", "diag/20261020-075740-p3-lecture/r.json",
             "src/controle_ia/sondes/base.py", "RENDU-fille-10-bras-b-v4-v1.md"]
    for chemin in sains:
        assert not de.sous_embargo(chemin), chemin
    assert de.motif_de("src/controle_ia/sondes/base.py") is None


def test_v6_embargo_dans_une_archive_gardee():
    assert de.survivants("a.zip", _zip({"notes.md": b"x"}), set()) == []
    assert de.survivants("a.zip", _zip({"docs/notes/bras-attaque/n.md": b"x"}), set()) == ["a.zip!docs/notes/bras-attaque/n.md"]


def test_v6_formes_de_cles_elargies():
    vraie = b"cle = 'sk-" + b"Ab3dE6gH9jK2mN5pQ8sT1vW4" + b"'"
    assert de.secrets_dans("c.py", vraie, {}) == ["c.py : clé de la forme sk-"]
    assert de.secrets_dans("c.py", b"x = 'sk-FAUX-" + b"A1" * 12 + b"'", {}) == []        # clé factice marquée
    assert de.secrets_dans("c.py", b"risk-" + b"a1" * 15, {}) == []                       # mot qui finit par « sk- »
    assert de.secrets_dans("c.py", b"id = AKIA" + b"ABCDEFGH23456789", {}) == ["c.py : clé AWS"]
    fausse = "fedcba9876543210" * 4                                                      # la valeur de l'environnement
    assert de.secrets_dans("c.py", f"sk-FAUX-{fausse}".encode(), {"FAUSSE_API_KEY": fausse.encode()}) == [
        "c.py : valeur de FAUSSE_API_KEY"]                                                # ne profite pas de la marque


def test_v6_donnees_personnelles_saines_et_artefacts():
    assert de.personnelles_dans("a.md", b"git@github.com, noreply@anthropic.com, essai@x.invalid") == []
    assert de.personnelles_dans("a.md", b"auteur : someone@uni-research.edu") == []        # tiers : compté, pas arrêté
    assert de.courriels_de_tiers(b"auteur : someone@uni-research.edu ; x@y.invalid") == 1
    assert de.personnelles_dans("a.md", b"contact : lciric@ens-paris-saclay.fr") == ["a.md : adresse électronique de Lazar"]
    assert de.personnelles_dans("README.md", b"contact : lciric@ens-paris-saclay.fr", exempter_courriel=True) == []
    assert de.personnelles_dans("a.md", b"ssh root@5.6.7.8 -p 22") == ["a.md : adresse IP publique"]
    assert de.personnelles_dans("a.md", b"nvidia-cufft==12.0.0.61 ; 10.0.0.2 ; 127.0.0.1 ; 1.1.1.1:443") == []
    assert de.personnelles_dans("a.md", rb"C:\Users\lciri\Documents") == ["a.md : chemin personnel"]
    assert de.personnelles_dans("a.md", b"/home/lazar/x") == ["a.md : chemin personnel"]
    assert de.personnelles_dans("a.md", b"/home/user/controle-ia-travail /home/argon/.cle /Users/alice/x") == []
    assert de.personnelles_dans("a.zip", _zip({"n.md": b"lciric@ens-paris-saclay.fr"})) == [
        "a.zip!n.md : adresse électronique de Lazar"]


def test_v6_paquet_incremental_refuse(tmp_path):
    depot = tmp_path / "depot"
    depot.mkdir()
    _git_factice(depot, "init", "-q", "-b", "main")
    for i in (1, 2):
        (depot / f"f{i}.md").write_text(str(i), encoding="utf-8")
        _git_factice(depot, "add", "-A")
        _git_factice(depot, "commit", "-q", "-m", str(i))
    _git_factice(depot, "bundle", "create", "-q", str(tmp_path / "complet.bundle"), "main")
    _git_factice(depot, "bundle", "create", "-q", str(tmp_path / "incr.bundle"), "HEAD~1..main")
    assert de.survivants("complet.bundle", (tmp_path / "complet.bundle").read_bytes(), set()) == []   # cas sain
    with pytest.raises(SystemExit, match="incrémental"):
        de.survivants("incr.bundle", (tmp_path / "incr.bundle").read_bytes(), set())


def test_v6_copie_avec_embargo_et_readme_public(tmp_path, monkeypatch, capsys):
    """L'embargo n'est jamais lu (une clé y est posée : la copie passe quand même) ni listé par chemin ; le README
    public remplace celui du dépôt ; une adresse de Lazar dans un fichier gardé arrête."""
    _depot_factice(tmp_path / "e", copie_cachee=False)
    fausse = "0a1b2c3d4e5f6a7b" * 4
    (tmp_path / "e/docs/notes/bras-attaque").mkdir(parents=True)
    (tmp_path / "e/docs/notes/bras-attaque/piece.md").write_text(f"cle {fausse}\n", encoding="utf-8")
    _git_factice(tmp_path / "e", "add", "-A")
    _git_factice(tmp_path / "e", "commit", "-q", "-m", "embargo")
    monkeypatch.setattr(de, "RACINE", tmp_path / "e")
    monkeypatch.setenv("FAUSSE_API_KEY", fausse)
    readme = tmp_path / "README-public.md"
    readme.write_text("# public\n\nContact: lciric@ens-paris-saclay.fr\n", encoding="utf-8")
    assert de.main(["HEAD", str(tmp_path / "s"), "--readme", str(readme)]) == 0
    copie = tmp_path / "s/controle-ia-expurge"
    assert not (copie / "docs/notes/bras-attaque").exists()
    assert (copie / "README.md").read_text(encoding="utf-8") == readme.read_text(encoding="utf-8")
    expurge = (copie / "EXPURGE.md").read_text(encoding="utf-8")
    assert "bras-attaque/piece.md" not in expurge and "1 under embargo" in expurge
    (tmp_path / "e/notes-contact.md").write_text("ecrire a lciric@ens-paris-saclay.fr\n", encoding="utf-8")
    _git_factice(tmp_path / "e", "add", "-A")
    _git_factice(tmp_path / "e", "commit", "-q", "-m", "adresse")
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "s2"), "--readme", str(readme)]) == 1
    assert "notes-contact.md : adresse électronique de Lazar" in capsys.readouterr().err
    assert list((tmp_path / "s2").glob("*.bundle")) == []
