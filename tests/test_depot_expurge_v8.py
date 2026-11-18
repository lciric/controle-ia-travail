"""v8 (R-3174) : essais de la v7 rejoués sur la v8 (seul le script chargé change ; trois essais adaptés là où la v8
change le résultat attendu : chemins de l'embargo devenus permanents, nom du script), puis retrait permanent par nom
(cas sain et artefact pour chaque fragment, R5), arrêt sur un chemin sensible hors des dossiers visés, contenu jamais
lu, liste réelle du dépôt, mode à blanc. v7 (R-2672, R-2679) : essais de la v6 rejoués sur la v7 (inchangés, seul le script chargé change), puis retraits par
nom (`brouillons/pain-axis-*`, notes de l'autre projet), gardes des noms et des identifiants d'objets git, chacun avec
cas sain et artefact (R5). v6 (R-2433) : essais de la v5 rejoués sur la v6, puis embargo, formes de clés élargies, données personnelles, paquets incrémentaux et README public. Copie expurgée du dépôt (`scripts/depot_expurge.py`, R-104, R-105) : l'appariement des retraits ne traverse pas
les dossiers, aucun fichier que le code charge n'est retiré, et aucun fichier retiré ne survit dans une archive gardée
(cas sain et artefact, R5)."""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import io
import json
import subprocess
import tarfile
import zipfile
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("depot_expurge_v8", RACINE / "scripts" / "depot_expurge_v8.py")
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
        attendu = de.RAISON_PERMANENTE if de.retrait_permanent(chemin) else de.RAISON_EMBARGO   # v8 : permanent d'abord
        assert de.motif_de(chemin) == attendu, chemin
    assert sum(de.retrait_permanent(c) for c in vises) == 6                    # bras-attaque, mode-tenu, bras-informe
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
    (tmp_path / "e/docs/notes/g0/lecture-7a-v1").mkdir(parents=True)          # v8 : sous embargo seulement
    (tmp_path / "e/docs/notes/g0/lecture-7a-v1/piece.md").write_text(f"cle {fausse}\n", encoding="utf-8")
    _git_factice(tmp_path / "e", "add", "-A")
    _git_factice(tmp_path / "e", "commit", "-q", "-m", "embargo")
    monkeypatch.setattr(de, "RACINE", tmp_path / "e")
    monkeypatch.setenv("FAUSSE_API_KEY", fausse)
    readme = tmp_path / "README-public.md"
    readme.write_text("# public\n\nContact: lciric@ens-paris-saclay.fr\n", encoding="utf-8")
    assert de.main(["HEAD", str(tmp_path / "s"), "--readme", str(readme)]) == 0
    copie = tmp_path / "s/controle-ia-expurge"
    assert not (copie / "docs/notes/g0/lecture-7a-v1").exists()
    assert (copie / "README.md").read_text(encoding="utf-8") == readme.read_text(encoding="utf-8")
    expurge = (copie / "EXPURGE.md").read_text(encoding="utf-8")
    assert "lecture-7a-v1/piece.md" not in expurge and "1 under embargo" in expurge
    (tmp_path / "e/notes-contact.md").write_text("ecrire a lciric@ens-paris-saclay.fr\n", encoding="utf-8")
    _git_factice(tmp_path / "e", "add", "-A")
    _git_factice(tmp_path / "e", "commit", "-q", "-m", "adresse")
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "s2"), "--readme", str(readme)]) == 1
    assert "notes-contact.md : adresse électronique de Lazar" in capsys.readouterr().err
    assert list((tmp_path / "s2").glob("*.bundle")) == []


# --- v7 (R-2672, R-2679) -------------------------------------------------------------------------------------------

P013 = "docs/decisions/proposition-P-013-T0.7-temoins-pain-axis-v1.md"


def test_v7_pain_axis_retire_par_nom_sain_et_artefact():
    """`brouillons/pain-axis-*` : dossiers à toute profondeur, fichiers posés dans `brouillons/` et compagnons."""
    vises = ["brouillons/pain-axis-brainstorm-v1.md", "brouillons/pain-axis-brainstorm-v1.md.sha256",
             "brouillons/pain-axis-canal-v1/envois/n01/piece.json", "brouillons/pain-axis-creatif-v1/a.md.sha256",
             "brouillons/pain-axis-programme-fusionne-v1/travail/voisin-where-empathy/extrait-texte-v1.txt",
             "brouillons/pain-axis-programme-fusionne-v5/etat-des-lieux-reprise-v1.md"]
    for chemin in vises:
        assert de.retire_par_nom(chemin) == de.RAISON_PAIN_AXIS, chemin
        assert de.motif_de(chemin) == de.RAISON_PAIN_AXIS, chemin     # avant RETRAITS : le fichier n'est jamais lu
        assert de.motif_de(chemin) in de.RAISONS_PAR_NOM
    sains = ["brouillons/canal-reprise-releve-v1/envois/p/synthese-v1.md", "brouillons/painaxis-v1/a.md",
             "brouillons-bis/pain-axis-v1/a.md", "docs/brouillons/pain-axis-v1/a.md", "brouillons/pain-axis",
             "src/controle_ia/sondes/base.py", P013]
    for chemin in sains:
        assert de.retire_par_nom(chemin) is None, chemin
    assert de.motif_de("brouillons/canal-reprise-releve-v1/envois/p/synthese-v1.md") is None
    assert de.motif_de(P013) is None and P013 in de.GARDES_SIGNALES      # gardé, nommé, rapporté dans le bilan


def test_v7_autre_projet_retire_par_nom_sain_et_artefact():
    """`docs/notes/regard-ou-raisons-*` et `docs/notes/collisionneur-regard-ou-raisons-*` : dossiers, fichiers, compagnons."""
    vises = ["docs/notes/regard-ou-raisons-confondants-v1/question-v1.md",
             "docs/notes/regard-ou-raisons-confondants-v1/question-v1.md.sha256",
             "docs/notes/regard-ou-raisons-bilan-v1.md", "docs/notes/regard-ou-raisons-bilan-v1.md.sha256",
             "docs/notes/collisionneur-regard-ou-raisons-v1/acteurs/a1/bilan.json",
             "docs/notes/collisionneur-regard-ou-raisons-croisement-v1.md"]
    for chemin in vises:
        assert de.motif_de(chemin) == de.RAISON_AUTRE_PROJET, chemin
    sains = ["docs/notes/collisionneur-diversite-idees-v1/bilan.md", "docs/notes/regard-v1.md",
             "docs/notes/organisme-conception-propre-v1/lecture.md", "docs/regard-ou-raisons-v1/a.md"]
    for chemin in sains:
        assert de.retire_par_nom(chemin) is None, chemin
    assert de.motif_de("docs/notes/collisionneur-diversite-idees-v1/bilan.md") is None
    # hors des dossiers visés, le nom n'est pas retiré en silence : il arrête la copie (essai de bout en bout plus bas)
    assert de.porte_un_nom_retire("docs/regard-ou-raisons-v1/a.md")


def test_v7_noms_retires_dans_une_archive_gardee():
    """Un membre d'archive dont le chemin porte un nom retiré est trouvé, où que soit le dossier, à toute profondeur."""
    assert de.survivants("a.zip", _zip({"notes.md": b"x", "brouillons/autre-v1/n.md": b"y"}), set()) == []      # sain
    assert de.survivants("a.zip", _zip({"brouillons/pain-axis-canal-v1/n.md": b"x"}), set()) == [
        "a.zip!brouillons/pain-axis-canal-v1/n.md"]
    assert de.survivants("a.zip", _zip({"lot-v1/copie/Pain-Axis-resume.md": b"x"}), set()) == [
        "a.zip!lot-v1/copie/Pain-Axis-resume.md"]                                         # préfixe, casse
    assert de.survivants("a.tar", _tar({"./docs/notes/regard-ou-raisons-v1/q.md": b"x"}), set()) == [
        "a.tar!docs/notes/regard-ou-raisons-v1/q.md"]
    assert de.survivants("a.zip", _zip({"d.tar": _tar({"x/collisionneur-regard-ou-raisons-v1.md": b"x"})}), set()) == [
        "a.zip!d.tar!x/collisionneur-regard-ou-raisons-v1.md"]                            # imbriqué


def test_v7_identifiant_git_sain_et_artefact(tmp_path):
    """L'identifiant d'objet git calculé est celui de git ; une copie renommée d'un fichier retiré par nom, membre
    d'une archive gardée, est trouvée par cet identifiant ; un membre différent ne l'est pas."""
    piece = b"piece retiree par nom\n"
    (tmp_path / "f").write_bytes(piece)
    attendu = subprocess.run(["git", "hash-object", str(tmp_path / "f")], capture_output=True, text=True,
                             check=True).stdout.strip()
    assert de.identifiant_git(piece) == attendu
    assert de.identifiant_git(b"") == de.BLOB_VIDE
    ids = frozenset({attendu})
    assert de.survivants("a.zip", _zip({"notes.md": b"autre texte\n"}), set(), ids) == []                       # sain
    assert de.survivants("a.zip", _zip({"notes/innocent.md": piece}), set(), ids) == ["a.zip!notes/innocent.md"]
    assert de.survivants("a.zip", _zip({"d.tar": _tar({"n.md": piece})}), set(), ids) == ["a.zip!d.tar!n.md"]


def _depot_par_nom(depot: Path, fausse: str) -> None:
    _depot_factice(depot, copie_cachee=False)
    (depot / "brouillons/pain-axis-essai-v1/travail").mkdir(parents=True)
    (depot / "brouillons/pain-axis-essai-v1/travail/piece.md").write_text(f"cle {fausse}\n", encoding="utf-8")
    (depot / "brouillons/pain-axis-essai-v1/annexe.md").write_text("piece sans cle\n", encoding="utf-8")
    (depot / "brouillons/pain-axis-note-v1.md").write_text("note\n", encoding="utf-8")
    (depot / "brouillons/pain-axis-note-v1.md.sha256").write_text("0" * 64 + "  pain-axis-note-v1.md\n", encoding="utf-8")
    (depot / "brouillons/pain-axis-essai-v1/vide.txt").write_bytes(b"")
    (depot / "brouillons/autre-v1").mkdir()
    (depot / "brouillons/autre-v1/voisin.md").write_text("voisin sain\n", encoding="utf-8")
    (depot / "brouillons/autre-v1/vide.txt").write_bytes(b"")                 # même objet vide qu'un fichier retiré : sain
    (depot / "docs/notes/regard-ou-raisons-essai-v1").mkdir(parents=True)
    (depot / "docs/notes/regard-ou-raisons-essai-v1/question.md").write_text("question\n", encoding="utf-8")
    (depot / "docs/notes/collisionneur-regard-ou-raisons-essai-v1.md").write_text("bilan\n", encoding="utf-8")
    (depot / "docs/decisions").mkdir(parents=True)
    (depot / P013).write_text("proposition\n", encoding="utf-8")
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "par nom")


def test_v7_copie_de_bout_en_bout_retraits_par_nom(tmp_path, monkeypatch, capsys):
    """Cas sain : les fichiers retirés par nom ne sont ni copiés, ni lus (une clé y est posée : la copie passe), ni
    listés par chemin ; le voisin reste ; le chemin nommé dans GARDES_SIGNALES reste et paraît dans le bilan."""
    fausse = "1a2b3c4d5e6f7a8b" * 4
    depot = tmp_path / "n"
    _depot_par_nom(depot, fausse)
    monkeypatch.setattr(de, "RACINE", depot)
    monkeypatch.setenv("FAUSSE_API_KEY", fausse)
    assert de.main(["HEAD", str(tmp_path / "s")]) == 0
    copie = tmp_path / "s/controle-ia-expurge"
    suivis = subprocess.run(["git", "-C", str(copie), "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    assert not any("pain-axis" in f and f != P013 for f in suivis) and not any("regard-ou-raisons" in f for f in suivis)
    assert not (copie / "brouillons/pain-axis-essai-v1").exists() and not (copie / "brouillons/pain-axis-note-v1.md").exists()
    assert not (copie / "brouillons/pain-axis-note-v1.md.sha256").exists()
    assert not (copie / "docs/notes/regard-ou-raisons-essai-v1").exists()
    assert (copie / "brouillons/autre-v1/voisin.md").exists() and (copie / "brouillons/autre-v1/vide.txt").exists()
    assert (copie / P013).exists()
    expurge = (copie / "EXPURGE.md").read_text(encoding="utf-8")
    for nom in ("pain-axis-essai-v1", "pain-axis-note-v1", "piece.md", "regard-ou-raisons-essai", "question.md"):
        assert nom not in expurge, nom                                          # compté, jamais listé
    assert "7 withheld by name, counted only" in expurge                        # 5 + 2
    assert f"| {de.RAISON_PAIN_AXIS} | 5 |" in expurge and f"| {de.RAISON_AUTRE_PROJET} | 2 |" in expurge
    assert "`scripts/depot_expurge_v8.py` (written after that commit" in expurge  # le dépôt factice n'a pas le script
    bilan = json.loads((tmp_path / "s/bilan.json").read_text(encoding="utf-8"))
    assert bilan["fichiers_retires_par_nom"] == 7 and bilan["chemins_gardes_signales"] == [P013]
    assert bilan["identifiants_git_retires_par_nom"] == 6                       # sept fichiers, dont un vide, écarté
    brut = (tmp_path / "s/bilan.json").read_text(encoding="utf-8")
    assert "pain-axis-essai" not in brut and "regard-ou-raisons-essai" not in brut and fausse not in brut


def _ajoute(depot: Path, chemin: str, contenu: bytes) -> None:
    (depot / chemin).parent.mkdir(parents=True, exist_ok=True)
    (depot / chemin).write_bytes(contenu)
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "artefact")


@pytest.mark.parametrize("chemin, contenu, message", [
    ("docs/notes/resume-pain-axis-v1.md", b"resume\n", "hors des dossiers visés"),                # nom, hors de brouillons/
    ("brouillons/regard-ou-raisons-essai-v2/q.md", b"q\n", "hors des dossiers visés"),            # nom, hors de docs/notes/
    ("docs/notes/innocent-v1.md", b"piece sans cle\n", "identifiant d'objet git"),                # copie renommée
    ("livrables/lot-v1.zip", None, "survivent dans une archive gardée"),                          # copie dans une archive
    ("livrables/lot-v2.zip", b"", "survivent dans une archive gardée"),                           # nom dans une archive
])
def test_v7_copie_refusee_artefacts_par_nom(tmp_path, monkeypatch, capsys, chemin, contenu, message):
    depot = tmp_path / "n"
    _depot_par_nom(depot, "1a2b3c4d5e6f7a8b" * 4)
    if contenu is None:
        contenu = _zip({"notes/innocent.md": b"piece sans cle\n"})
    elif contenu == b"":
        contenu = _zip({"brouillons/pain-axis-essai-v1/autre.md": b"texte neuf\n"})
    _ajoute(depot, chemin, contenu)
    monkeypatch.setattr(de, "RACINE", depot)
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "s")]) == 1
    err = capsys.readouterr().err
    assert message in err and "aucun paquet écrit" in err
    assert list((tmp_path / "s").glob("*.bundle")) == [] and not (tmp_path / "s/bilan.json").exists()


def test_v7_noms_du_depot_reel_tous_vises_ou_nommes():
    """Dans le dépôt réel, tout chemin suivi qui porte un nom retiré est retiré par nom, sous embargo, ou nommé dans
    GARDES_SIGNALES : sinon la copie s'arrêterait (cet essai le dit avant)."""
    suivis = subprocess.run(["git", "-C", str(RACINE), "ls-files"], capture_output=True, text=True,
                            check=True).stdout.split("\n")
    portes = [f for f in suivis if f and any(x in f.lower() for x in de.FRAGMENTS_PAR_NOM)]
    assert len([f for f in portes if f.startswith("brouillons/pain-axis-")]) >= 104
    hors = [f for f in portes if not de.retire_par_nom(f) and not de.sous_embargo(f) and f not in de.GARDES_SIGNALES
            and not any(de.correspond(f, m) for m, _ in de.RETRAITS)]
    assert hors == []


# --- v8 (R-3174) ---------------------------------------------------------------------------------------------------

# (fragment, artefacts fabriqués qui doivent être retirés, voisins sains qui doivent rester). Les voisins sains sont
# des noms fabriqués ou des noms réels du dépôt qui ne portent aucun fragment (seuls des noms, jamais des contenus).
CAS_V8 = [
    ("bras-attaque",
     ["docs/notes/bras-attaque/n.md", "prereg/bras-attaque-p3bis-v1.md", "prereg/bras-attaque-p3bis-v1.md.sha256",
      "src/controle_ia/Bras-Attaque/x.py"],
     ["docs/notes/bras-b-v4/attaque-v1.md", "docs/notes/bras-a-attaquer-generique/a.md"]),
    ("bras-informe",
     ["brouillons/x/anteriorite-bras-informe-v2.md", "tests/bras-informe-v1/test_x.py"],
     ["docs/notes/bras-non-informatif-v1/a.md", "docs/notes/bras-b/informe-v1.md"]),
    ("verification-externe-bras",
     ["docs/notes/verification-externe-bras-v1/plan.md", "scripts/verification-externe-bras-v1.py"],
     ["docs/notes/verification-externe-v1/bras-b.md", "docs/notes/verification-externe-juges-v1/plan.md"]),
    ("evasion-moniteurs",
     ["docs/notes/collisionneur-evasion-moniteurs-v1/a.md", "diag/20261118-evasion-moniteurs/r.json"],
     ["docs/notes/moniteurs-evasion-v1/a.md", "docs/notes/evasion-v1/moniteurs.md"]),
    ("4-familles-evasion",
     ["docs/notes/programme-et-4-familles-evasion/a.md", "runs/4-familles-evasion-v1/manifeste.json"],
     ["docs/notes/programme-et-4-familles-v1/a.md", "docs/notes/programme-et-3-familles-evasion/a.md"]),
    ("pilier-attaque",
     ["docs/notes/ideation-pilier-attaque-v1/organisme-v1/x.md", "rapports/pilier-attaque-v1/r.md"],
     ["docs/notes/ideation-pilier-defense-v1/a.md", "docs/notes/pilier-v1/attaque.md"]),
    ("attaque-publiee",
     ["docs/notes/reproduction-attaque-publiee-v1/a.md", "prereg/temoin-attaque-publiee-bailey-v1.md",
      "prereg/temoin-attaque-publiee-bailey-v1.md.sha256"],
     ["docs/notes/attaques-de-juge-generique-v1/a.md", "prereg/preenregistrement-attaque-goodhart-v3-v4.md"]),
    ("organismes-discrets",
     ["docs/notes/organismes-discrets-v1/a.md", "runs/20261118-organismes-discrets-v2/manifeste.json",
      "registres/organismes-discrets-v1.md"],
     ["docs/notes/organisme-boucle-reelle-v1/a.md", "docs/notes/organismes-v1/discrets.md"]),
    ("mode-tenu-a-l-ecart",
     ["donnees/mode-tenu-a-l-ecart-v1/a.md", "diag/x/MODE-TENU-A-L-ECART.json"],
     ["docs/notes/mode-tenu-ouvert-v1/a.md", "docs/notes/mode-generique-v1/a-l-ecart.md"]),
]


@pytest.mark.parametrize("fragment, artefacts, sains", CAS_V8, ids=[c[0] for c in CAS_V8])
def test_v8_retrait_permanent_sain_et_artefact(fragment, artefacts, sains):
    assert fragment in de.FRAGMENTS_PERMANENTS
    for chemin in artefacts:
        assert de.fragment_sensible(chemin) == fragment, chemin
        assert de.retrait_permanent(chemin), chemin
        assert de.motif_de(chemin) == de.RAISON_PERMANENTE, chemin          # avant RETRAITS : jamais lu
        assert de.porte_un_nom_retire(chemin), chemin
    for chemin in sains:
        assert de.fragment_sensible(chemin) is None, chemin
        assert not de.retrait_permanent(chemin) and not de.sensible_hors_dossiers(chemin), chemin
        assert de.motif_de(chemin) is None, chemin


def test_v8_neuf_fragments_et_onze_dossiers():
    assert len(de.FRAGMENTS_PERMANENTS) == 9 and {c[0] for c in CAS_V8} == set(de.FRAGMENTS_PERMANENTS)
    assert set(de.DOSSIERS_PERMANENTS) == {"docs", "prereg", "brouillons", "src", "scripts", "tests", "donnees",
                                           "runs", "diag", "registres", "rapports"}
    assert de.RAISON_PERMANENTE in de.RAISONS_PAR_NOM
    assert de.RAISON_PERMANENTE.startswith("bras d'attaque et familles sensibles (conception d'organismes saboteurs "
                                           "discrets, évasion des moniteurs) : exclus de toute copie publique sans mot "
                                           "exprès de Lazar ; filtrés par nom, contenu jamais lu")


def test_v8_permanent_ne_se_leve_pas_avec_l_embargo(monkeypatch):
    """Au verdict de P3-bis, l'embargo se lève (fragments et motifs vidés) : le retrait permanent reste."""
    monkeypatch.setattr(de, "EMBARGO_FRAGMENTS", ())
    monkeypatch.setattr(de, "EMBARGO_MOTIFS", ())
    for _, artefacts, _ in CAS_V8:
        for chemin in artefacts:
            assert not de.sous_embargo(chemin)
            assert de.motif_de(chemin) == de.RAISON_PERMANENTE, chemin
    assert de.motif_de("docs/notes/g0/lecture-7a-v1/a.md") is None            # l'embargo seul, lui, se lève


def test_v8_registres_retires_par_nom_jamais_listes():
    """`registres/**` (retrait listé, avec chemin et empreinte) ne voit jamais un chemin sensible : le permanent passe avant."""
    assert de.motif_de("registres/organismes-discrets-v1.md") == de.RAISON_PERMANENTE
    assert de.motif_de("registres/etat.md") not in (None, de.RAISON_PERMANENTE)          # voisin : retrait listé, inchangé


@pytest.mark.parametrize("chemin", ["livrables/organismes-discrets-v1/a.md", "livrables/bras-attaque-v1.zip",
                                    "README-pilier-attaque.md", "gemini/evasion-moniteurs/x.py",
                                    "docs", "prep/mode-tenu-a-l-ecart-v1/a.md", "docsx/bras-informe/a.md",
                                    "bras-attaque"])
def test_v8_hors_des_dossiers_vises_arrete(chemin):
    if chemin == "docs":
        assert not de.sensible_hors_dossiers(chemin) and de.motif_de(chemin) is None     # cas sain
        return
    assert de.sensible_hors_dossiers(chemin)
    with pytest.raises(SystemExit, match="hors des dossiers visés"):
        de.motif_de(chemin)


def test_v8_membres_d_archive_sensibles():
    assert de.survivants("a.zip", _zip({"notes.md": b"x", "docs/notes/attaques-de-juge-generique-v1/a.md": b"y"}),
                         set()) == []                                                       # sain
    assert de.survivants("a.zip", _zip({"lot/organismes-discrets-v1/a.md": b"x"}), set()) == [
        "a.zip!lot/organismes-discrets-v1/a.md"]
    assert de.survivants("a.zip", _zip({"d.tar": _tar({"x/Verification-Externe-Bras-v1.md": b"x"})}), set()) == [
        "a.zip!d.tar!x/Verification-Externe-Bras-v1.md"]                                    # imbriqué, casse


class _Lectures:
    """Relève les membres de `git archive` dont le contenu est lu (`extractfile`)."""

    def __init__(self, monkeypatch):
        self.noms = []
        vrai = tarfile.TarFile.extractfile
        lectures = self

        def extractfile(tar, membre):
            lectures.noms.append(membre if isinstance(membre, str) else membre.name)
            return vrai(tar, membre)
        monkeypatch.setattr(tarfile.TarFile, "extractfile", extractfile)


SENSIBLES_FACTICES = ["docs/notes/bras-attaque/piece.md", "docs/notes/bras-attaque/piece.md.sha256",
                      "docs/notes/verification-externe-bras-v1/plan.md",
                      "prereg/temoin-attaque-publiee-bailey-v1.md", "prereg/bras-attaque-p3bis-v1.md",
                      "src/controle_ia/evasion-moniteurs-v1/m.py", "runs/20261118-organismes-discrets-v1/manifeste.json",
                      "registres/organismes-discrets-v1.md", "rapports/pilier-attaque-v1/r.md",
                      "donnees/mode-tenu-a-l-ecart-v1/a.md"]


def _depot_permanent(depot: Path, fausse: str) -> None:
    _depot_factice(depot, copie_cachee=False)
    for i, chemin in enumerate(SENSIBLES_FACTICES):
        (depot / chemin).parent.mkdir(parents=True, exist_ok=True)
        (depot / chemin).write_text(f"piece sensible {i}\ncle {fausse}\nlciric@ens-paris-saclay.fr\n", encoding="utf-8")
    (depot / "docs/notes/attaques-de-juge-generique-v1").mkdir(parents=True)
    (depot / "docs/notes/attaques-de-juge-generique-v1/a.md").write_text("voisin sain\n", encoding="utf-8")
    (depot / "registres").mkdir(exist_ok=True)
    (depot / "registres/etat.md").write_text("etat\n", encoding="utf-8")
    _git_factice(depot, "add", "-A")
    _git_factice(depot, "commit", "-q", "-m", "sensibles")


@pytest.mark.parametrize("embargo_leve", [False, True])
def test_v8_copie_de_bout_en_bout_permanent(tmp_path, monkeypatch, embargo_leve):
    """Cas sain : les chemins sensibles ne sont ni copiés, ni lus (une clé et une adresse de Lazar y sont posées : la
    copie passe), ni listés par chemin ; comptés sous la raison permanente, embargo levé ou non ; le voisin reste."""
    if embargo_leve:
        monkeypatch.setattr(de, "EMBARGO_FRAGMENTS", ())
        monkeypatch.setattr(de, "EMBARGO_MOTIFS", ())
    fausse = "9f8e7d6c5b4a3f2e" * 4
    depot = tmp_path / "p"
    _depot_permanent(depot, fausse)
    monkeypatch.setattr(de, "RACINE", depot)
    monkeypatch.setenv("FAUSSE_API_KEY", fausse)
    lectures = _Lectures(monkeypatch)
    assert de.main(["HEAD", str(tmp_path / "s")]) == 0
    assert not any(de.fragment_sensible(n) for n in lectures.noms)               # contenu jamais lu
    copie = tmp_path / "s/controle-ia-expurge"
    suivis = subprocess.run(["git", "-C", str(copie), "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    assert not any(de.fragment_sensible(f) for f in suivis)
    assert "docs/notes/attaques-de-juge-generique-v1/a.md" in suivis
    expurge = (copie / "EXPURGE.md").read_text(encoding="utf-8")
    bilan_brut = (tmp_path / "s/bilan.json").read_text(encoding="utf-8")
    for chemin in SENSIBLES_FACTICES:
        nom = chemin.split("/")[-2] if chemin.count("/") > 1 else Path(chemin).stem
        assert nom not in expurge and nom not in bilan_brut, nom                  # compté, jamais listé
    assert f"| {de.RAISON_PERMANENTE} | {len(SENSIBLES_FACTICES)} |" in expurge
    assert f"{len(SENSIBLES_FACTICES)} withheld by name, counted only" in expurge and "0 under embargo" in expurge
    assert "permanently (not lifted with the embargo)" in expurge
    assert "`registres/etat.md`" in expurge                                       # le voisin listé reste listé
    bilan = json.loads(bilan_brut)
    assert bilan["retraits_par_nom_par_motif"] == {de.RAISON_PERMANENTE: len(SENSIBLES_FACTICES)}
    assert bilan["identifiants_git_retires_par_nom"] == len(SENSIBLES_FACTICES)     # contenus distincts, non vides
    assert fausse not in bilan_brut


@pytest.mark.parametrize("chemin, contenu, message", [
    ("livrables/organismes-discrets-v1/a.md", b"x\n", "hors des dossiers visés"),          # dossier non visé
    ("Bras-Attaque-notes.md", b"x\n", "hors des dossiers visés"),                          # racine, casse
    ("gemini/evasion-moniteurs/x.py", b"x\n", "hors des dossiers visés"),                   # retrait listé, non visé
    ("docs/notes/innocent-v1.md", None, "identifiant d'objet git"),                        # copie renommée
    ("livrables/lot-v3.zip", b"", "survivent dans une archive gardée"),                     # nom dans une archive
])
def test_v8_arbre_jetable_artefacts_arretent(tmp_path, monkeypatch, capsys, chemin, contenu, message):
    """Artefacts : un chemin sensible hors des dossiers visés arrête sans être lu (une clé y est posée : seule la garde
    de nom parle) ; une copie renommée d'un fichier sensible, ou un membre d'archive sensible, arrête aussi."""
    fausse = "9f8e7d6c5b4a3f2e" * 4
    depot = tmp_path / "p"
    _depot_permanent(depot, fausse)
    if contenu is None:
        contenu = (depot / SENSIBLES_FACTICES[0]).read_bytes()
    elif contenu == b"":
        contenu = _zip({"docs/notes/pilier-attaque-v2/a.md": b"texte neuf\n"})
    else:
        contenu = f"cle {fausse}\n".encode()
    _ajoute(depot, chemin, contenu)
    monkeypatch.setattr(de, "RACINE", depot)
    monkeypatch.setenv("FAUSSE_API_KEY", fausse)
    lectures = _Lectures(monkeypatch)
    capsys.readouterr()
    assert de.main(["HEAD", str(tmp_path / "s")]) == 1
    err = capsys.readouterr().err
    assert message in err and "aucun paquet écrit" in err and fausse not in err
    assert "valeur de FAUSSE_API_KEY" not in err                                  # jamais lu : la garde des secrets se tait
    assert not any(de.sensible_hors_dossiers(n) for n in lectures.noms)
    assert list((tmp_path / "s").glob("*.bundle")) == [] and not (tmp_path / "s/bilan.json").exists()


def test_v8_gardes_signales_n_exemptent_pas_un_nom_sensible(tmp_path, monkeypatch, capsys):
    """Le nom ne peut pas être rendu sauf par `GARDES_SIGNALES` : la garde des fragments permanents n'a pas d'exception."""
    depot = tmp_path / "p"
    _depot_permanent(depot, "9f8e7d6c5b4a3f2e" * 4)
    _ajoute(depot, "livrables/bras-attaque-resume-v1.md", b"x\n")
    monkeypatch.setattr(de, "RACINE", depot)
    monkeypatch.setattr(de, "GARDES_SIGNALES", de.GARDES_SIGNALES + ("livrables/bras-attaque-resume-v1.md",))
    assert de.main(["HEAD", str(tmp_path / "s")]) == 1
    assert "hors des dossiers visés" in capsys.readouterr().err


def test_v8_a_blanc_comptes_seulement(tmp_path, monkeypatch, capsys):
    """Mode à blanc : comptes par motif, aucun chemin sensible imprimé, rien d'écrit, aucun contenu sensible lu ; cas
    sain (code 0) puis artefact (chemin sensible hors des dossiers visés : code 1)."""
    depot = tmp_path / "p"
    _depot_permanent(depot, "9f8e7d6c5b4a3f2e" * 4)
    monkeypatch.setattr(de, "RACINE", depot)
    avant = sorted(p.name for p in tmp_path.iterdir())
    capsys.readouterr()
    assert de.main(["HEAD", "--a-blanc"]) == 0
    sortie = capsys.readouterr().out
    bilan = json.loads(sortie)
    assert bilan["fichiers_retires_permanents"] == len(SENSIBLES_FACTICES)
    assert bilan["chemins_sensibles_hors_dossiers_vises"] == 0 and bilan["fichiers_gardes_meme_identifiant_qu_un_retire_par_nom"] == 0
    assert sum(bilan["chemins_sensibles_par_fragment"].values()) == len(SENSIBLES_FACTICES)
    assert bilan["retraits_permanents_par_dossier"] == {"docs": 3, "prereg": 2, "src": 1, "runs": 1, "registres": 1,
                                                        "rapports": 1, "donnees": 1}
    for chemin in SENSIBLES_FACTICES:
        for segment in chemin.split("/"):
            if de.fragment_sensible(segment) and segment not in de.FRAGMENTS_PERMANENTS:   # le fragment seul : clé du compte
                assert segment not in sortie, segment
    assert sorted(p.name for p in tmp_path.iterdir()) == avant                     # rien d'écrit
    _ajoute(depot, "livrables/organismes-discrets-v1/a.md", b"x\n")
    _ajoute(depot, "livrables/lot-v3.zip", _zip({"x/pilier-attaque-v2/a.md": b"y"}))
    assert de.main(["HEAD", "--a-blanc"]) == 1
    sortie = capsys.readouterr().out
    bilan = json.loads(sortie)
    assert bilan["chemins_sensibles_hors_dossiers_vises"] == 1 and bilan["verdict"] == "arrêt"
    assert bilan["membres_d_archive_portant_un_nom_sensible"] == 1
    assert "organismes-discrets-v1" not in sortie and "pilier-attaque-v2" not in sortie


def test_v8_depot_reel_aucun_chemin_garde_sensible():
    """Sur la liste réelle `git ls-files` : tout chemin qui porte un fragment sensible est retiré par nom, à titre
    permanent ; aucun n'est hors des dossiers visés ; aucun n'est gardé. Les messages ne donnent que des comptes."""
    suivis = [f for f in subprocess.run(["git", "-C", str(RACINE), "ls-files"], capture_output=True, text=True,
                                        check=True).stdout.split("\n") if f]
    sensibles = [f for f in suivis if de.fragment_sensible(f)]
    assert len(sensibles) >= 300, len(sensibles)                       # 341 au commit e87fb6ce (18 novembre 2026)
    hors = sum(1 for f in sensibles if de.sensible_hors_dossiers(f))
    assert hors == 0, f"{hors} chemins sensibles hors des dossiers visés"
    gardes = sum(1 for f in sensibles if de.motif_de(f) != de.RAISON_PERMANENTE)
    assert gardes == 0, f"{gardes} chemins sensibles non retirés à titre permanent"
    assert not any(de.fragment_sensible(f) for f in suivis if de.motif_de(f) is None)
