"""Validateur renforcé des préenregistrements (v2) : un cas sain et des artefacts par contrôle (R5), plus les essais
qui tuent les mutants survivants signalés par la contre-lecture de la v1 (Sonnet 5.5, 28 novembre 2026, remarque 12).

Tout se joue dans de faux dépôts bâtis dans un dossier temporaire ; rien ne lit le vrai dépôt. La garde de lecture est
éprouvée par un crochet d'audit (`sys.addaudithook`) qui enregistre chaque ouverture de fichier pendant l'essai.
"""
import hashlib
import os
import re
import subprocess
import sys

import pytest

from controle_ia import prereg_renforce_v2 as pr
from controle_ia.gardes import GardeArret
from controle_ia.prereg import SECTIONS, problemes

REMPLISSAGE = ("Ce paragraphe décrit la section avec assez de mots pour passer le seuil de longueur : il nomme "
               "l'objet mesuré, la population, la statistique, le sens attendu et la règle de décision, sans rien "
               "laisser à remplir ni renvoyer à un texte absent du dépôt. ")

# ---------- crochet d'audit : toute ouverture de fichier pendant un essai ----------

_OUVERTS: list | None = None


def _crochet(evenement, args):
    """Enregistre les ouvertures en lecture (les écritures de l'essai lui-même ne comptent pas)."""
    if evenement != "open" or _OUVERTS is None or not args or not isinstance(args[0], (str, bytes, os.PathLike)):
        return
    mode = args[1] if len(args) > 1 else None
    drapeaux = args[2] if len(args) > 2 and isinstance(args[2], int) else 0
    if isinstance(mode, str) and any(c in mode for c in "wax+"):
        return
    if drapeaux & (os.O_WRONLY | os.O_RDWR | os.O_CREAT):
        return
    _OUVERTS.append(os.fsdecode(args[0]))


sys.addaudithook(_crochet)


@pytest.fixture
def ouvertures():
    global _OUVERTS
    _OUVERTS = []
    yield _OUVERTS
    _OUVERTS = None


def gardes_ouverts(liste):
    return [x for x in liste if pr.est_garde(x) or pr.est_garde(os.path.realpath(x))]


# ---------- faux dépôt ----------

def git(racine, *args):
    subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True)


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def ecrire(racine, rel, contenu, compagnon=False):
    p = racine / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    octets = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    p.write_bytes(octets)
    if compagnon:
        (racine / (rel + ".sha256")).write_text(f"{sha(octets)}  {p.name}\n", encoding="utf-8")
    return sha(octets)


def init_git(r):
    git(r, "init", "-q", "-b", "main")
    git(r, "config", "user.email", "test@example.invalid")
    git(r, "config", "user.name", "test")


def committer(r, msg="etape"):
    git(r, "add", "-A")
    git(r, "commit", "-q", "-m", msg)


@pytest.fixture
def faux_depot(tmp_path):
    """Faux dépôt : un code suivi sans compagnon, deux rapports et un brouillon scellés, un fichier gardé scellé, un
    fichier gardé sans compagnon."""
    r = tmp_path / "depot"
    r.mkdir()
    init_git(r)
    h = {
        "code": ecrire(r, "src/paquet/module.py", "".join(f"ligne {i}\n" for i in range(1, 21))),
        "autre": ecrire(r, "src/paquet/autre.py", "autre\n"),
        "rapport1": ecrire(r, "docs/contre-lectures/rapport-1-v1.md", "rapport de la contre-lecture 1\n", compagnon=True),
        "rapport2": ecrire(r, "docs/contre-lectures/rapport-2-v1.md", "rapport de la contre-lecture 2\n", compagnon=True),
        "brouillon": ecrire(r, "brouillons/p-v1-brouillon1.md", "brouillon relu\n", compagnon=True),
        "garde": ecrire(r, "src/controle_ia/iib/poids.py", "secret\n", compagnon=True),
        "garde_sans_compagnon": ecrire(r, "src/controle_ia/iib/autre.py", "secret 2\n"),
    }
    committer(r, "init")
    return r, h


def texte_sain(h, contre_lecture=None, metrique_extra=""):
    corps = {s: REMPLISSAGE for s in SECTIONS}
    corps["Métrique"] = (REMPLISSAGE + f"La statistique est calculée par `src/paquet/module.py:3-5` "
                         f"(empreinte `{h['code']}`, préfixe `{h['code'][:12]}…`), voir aussi `docs/contre-lectures/`. "
                         "Les sorties iront sous `runs/<identifiant>/`, `diag/…/scores.json` et `docs/*.md`. "
                         + metrique_extra)
    corps["Contre-lecture"] = contre_lecture or (
        f"* **Contre-lecture 1** — agent neuf Claude Fable 5.2 ; brouillon relu `brouillons/p-v1-brouillon1.md` "
        f"(`{h['brouillon']}`) ; rapport `docs/contre-lectures/rapport-1-v1.md` (`{h['rapport1']}`).\n"
        f"* **Contre-lecture 2** — vérification des corrections par Opus 5.5 ; brouillon "
        f"`brouillons/p-v1-brouillon1.md` (`{h['brouillon']}`), rapport `docs/contre-lectures/rapport-2-v1.md` "
        f"(`{h['rapport2']}`) ; rien à reporter.")
    return "# Préenregistrement de test\n\n" + "\n".join(f"## {s}\n\n{corps[s]}\n" for s in SECTIONS)


def poser(racine, texte, nom="prereg/p-v1.md"):
    p = racine / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return p


def controle(racine, texte, **kw):
    return pr.verifier_renforce(poser(racine, texte), racine=racine, **kw)


def ajout(h, phrase):
    return texte_sain(h, metrique_extra=phrase)


def avec(liste, lettre, motif=""):
    return [x for x in liste if x.startswith(f"({lettre})") and motif in x]


# ========== cas sain, ligne de commande ==========

def test_sain_aucun_probleme_ni_avertissement(faux_depot, ouvertures):
    r, h = faux_depot
    p = poser(r, texte_sain(h))
    assert problemes(p) == []
    assert pr.verifier_renforce(p, racine=r) == ([], [])
    assert pr.problemes_renforces(p, racine=r) == []
    assert gardes_ouverts(ouvertures) == []


def test_ligne_de_commande(faux_depot, tmp_path, capsys):
    r, h = faux_depot
    sain = poser(r, texte_sain(h), "prereg/a-v1.md")
    faux = poser(r, texte_sain(h).replace(h["rapport1"], "e" * 64), "prereg/b-v1.md")
    assert pr._main(["--racine", str(r), str(sain)]) == 0
    assert pr._main(["--racine", str(r), str(faux)]) == 1
    latin = r / "prereg" / "latin-v1.md"
    latin.write_bytes("## Hypothèse\n\ncafé\n".encode("latin-1"))
    assert pr._main(["--racine", str(r), str(latin), str(sain)]) == 1      # ne plante pas, traite la suite
    sortie = capsys.readouterr().out
    assert "non lisible en UTF-8" in sortie and sortie.rstrip().endswith("conforme")


def test_problemes_de_base_en_tete(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("## Seuil\n", "## Seuil mal nommé\n"))
    assert pb[0] == "section absente : Seuil"


# ========== remarque 1 : appariement empreinte -> chemin ==========

def test_appariement_empreinte_d_un_autre_fichier(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace(f"(empreinte `{h['code']}`", f"(empreinte `{h['autre']}`"))
    assert avec(pb, "a", "appariée à src/paquet/module.py non vérifiée (ce n'est pas l'empreinte de ce fichier")
    assert avec(pb, "a", "elle désigne src/paquet/autre.py")


def test_appariement_rapport_croise_dans_la_contre_lecture(faux_depot):
    r, h = faux_depot
    t = texte_sain(h)
    i = t.index("* **Contre-lecture 2**")
    t = t[:i] + t[i:].replace(f"(`{h['rapport2']}`)", f"(`{h['rapport1']}`)")
    pb, _ = controle(r, t)
    assert problemes(poser(r, t)) == []
    assert avec(pb, "a", "appariée à docs/contre-lectures/rapport-2-v1.md")


def test_appariement_par_disque_sans_compagnon(faux_depot):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, f"Autre code `src/paquet/autre.py` (`{h['autre']}`)."))
    assert pb == [] and av == []


def test_appariement_fichier_garde_par_compagnon_sans_ouverture(faux_depot, ouvertures):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, f"Poids `src/controle_ia/iib/poids.py` (`{h['garde']}`)."))
    assert pb == [] and av == []
    assert gardes_ouverts(ouvertures) == []


def test_appariement_fichier_garde_sans_compagnon(faux_depot, ouvertures):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, f"Poids `src/controle_ia/iib/autre.py` (`{h['garde_sans_compagnon']}`)."))
    assert avec(pb, "a", "src/controle_ia/iib/autre.py est gardé et aucun compagnon ne la porte")
    assert gardes_ouverts(ouvertures) == []


def test_appariement_ligne_de_table_par_rang(faux_depot):
    r, h = faux_depot
    ligne = (f"\n\n| a | b | ea | eb |\n|---|---|---|---|\n| `src/paquet/module.py` | `src/paquet/autre.py` | "
             f"`{h['code']}` | `{h['autre']}` |\n")
    pb, _ = controle(r, ajout(h, ligne))
    assert not avec(pb, "a")
    croise = ligne.replace(h["code"], "X").replace(h["autre"], h["code"]).replace("X", h["autre"])
    pb, _ = controle(r, ajout(h, croise))
    assert len(avec(pb, "a", "non vérifiée")) == 2


def test_appariement_table_nombres_differents_rien_n_est_apparie(faux_depot):
    r, h = faux_depot
    ligne = f"\n\n| `src/paquet/module.py` | `src/paquet/autre.py` | `{h['autre']}` |\n"
    pb, av = controle(r, ajout(h, ligne))
    assert not avec(pb, "a") and avec(av, "a", "non appariée")


def test_appariement_strict_libelle_intercale(faux_depot):
    """« `chemin` ; brouillon 2 (`empreinte`) » : l'empreinte n'est pas celle du chemin, elle n'est pas appariée."""
    r, h = faux_depot
    pb, av = controle(r, ajout(h, f"Code `src/paquet/module.py` ; brouillon 2 (`{h['brouillon']}`)."))
    assert not avec(pb, "a") and avec(av, "a", "non appariée")


def test_appariement_version_ancienne_dans_l_historique(faux_depot):
    r, h = faux_depot
    (r / "src/paquet/autre.py").write_text("autre, version 2\n")
    committer(r)
    pb, av = controle(r, ajout(h, f"Code `src/paquet/autre.py` (`{h['autre']}`)."))
    assert not avec(pb, "a") and avec(av, "a", "version ancienne de src/paquet/autre.py")


def test_appariement_historique_plafonne_et_commit_cite(faux_depot, monkeypatch):
    r, h = faux_depot
    premier = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    (r / "src/paquet/autre.py").write_text("autre, version 2\n")
    committer(r)
    monkeypatch.setattr(pr, "PLAFOND_HISTORIQUE", 0)
    pb, _ = controle(r, ajout(h, f"Code `src/paquet/autre.py` (`{h['autre']}`)."))
    assert avec(pb, "a", "non vérifiée (ce n'est pas l'empreinte de ce fichier")
    pb, av = controle(r, ajout(h, f"Code `src/paquet/autre.py` (`{h['autre']}`) au commit `{premier[:10]}`."))
    assert not avec(pb, "a") and avec(av, "a", f"commit {premier[:12]}")


def test_appariement_chemin_absent(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, f"Code `src/paquet/disparu.py` (`{h['autre']}`)."))
    assert avec(pb, "a", "chemin absent") and avec(pb, "c", "src/paquet/disparu.py")


def test_appariement_compagnon_perime(faux_depot):
    r, h = faux_depot
    (r / "docs/contre-lectures/rapport-1-v1.md").write_text("modifié après scellement\n")
    pb, av = controle(r, texte_sain(h))
    assert not avec(pb, "a") and avec(av, "a", "compagnon périmé")


def test_empreinte_du_fichier_vide(faux_depot):
    r, h = faux_depot
    ecrire(r, "src/paquet/vide.py", "")
    committer(r)
    pb, av = controle(r, ajout(h, f"Vide `src/paquet/vide.py` (`{pr.EMPREINTE_VIDE}`)."))
    assert not avec(pb, "a") and avec(av, "a", "fichier vide")


def test_non_appariee_marque_hors_depot(faux_depot):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, f"Poids du modèle, hors dépôt : `{'7' * 63 + 'a'}`."))
    assert not avec(pb, "a") and avec(av, "a", "déclarée hors dépôt")
    pb, _ = controle(r, ajout(h, f"Poids du modèle : `{'7' * 63 + 'a'}`."))
    assert avec(pb, "a", "ne désigne aucun fichier")


# ========== (a) empreintes : existence, longueur, casse (remarque 4) ==========

def test_a_empreinte_inventee_hors_contre_lecture(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, f"Référence `{'0123456789abcdef' * 4}`."))
    assert avec(pb, "a", "0123456789abcdef" * 4)


@pytest.mark.parametrize("n", [33, 63, 65, 72])
def test_a_longueur_invalide(faux_depot, n):
    r, h = faux_depot
    s = (h["autre"] * 2)[:n]
    pb, _ = controle(r, ajout(h, f"Référence `{s}`."))
    assert avec(pb, "a", f"longueur d'empreinte invalide ({n} caractères)")


def test_a_empreinte_de_65_caracteres_issue_d_une_vraie(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, f"Code `src/paquet/autre.py` (`{h['autre']}a`)."))
    assert avec(pb, "a", "65 caractères")


@pytest.mark.parametrize("cas", ["vraie", "inventee"])
def test_a_majuscules(faux_depot, cas):
    r, h = faux_depot
    s = h["autre"].upper() if cas == "vraie" else "AB" * 32
    pb, _ = controle(r, ajout(h, f"Référence `{s}`."))
    assert avec(pb, "a", "majuscules")


def test_a_quarante_caracteres(faux_depot):
    r, h = faux_depot
    tete = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    pb, av = controle(r, ajout(h, f"Commit `{tete}`."))
    assert not avec(pb, "a") and not avec(av, "a", "40 caractères")
    pb, av = controle(r, ajout(h, f"Révision externe `{'1a' * 20}`."))
    assert not avec(pb, "a") and avec(av, "a", "40 caractères")


@pytest.mark.parametrize("n", [32, 128])
def test_a_longueurs_md5_sha512(faux_depot, n):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, f"Autre `{('9f' * 64)[:n]}`."))
    assert not avec(pb, "a") and avec(av, "a", f"suite de {n} caractères")


@pytest.mark.parametrize("n", [63, 64, 65])
def test_a_suite_collee_a_une_lettre_ignoree(faux_depot, n):
    r, h = faux_depot
    s = ("0123456789abcdef" * 5)[:n]
    pb, av = controle(r, ajout(h, f"Identifiant `g{s}`."))
    assert not avec(pb, "a") and not avec(av, "a", "0123456789abcdef")


def test_a_compagnon_orphelin_ne_compte_pas(faux_depot):
    r, h = faux_depot
    orphelin = "f" * 63 + "1"
    (r / "docs" / "disparu-v1.md.sha256").write_text(f"{orphelin}  disparu-v1.md\n", encoding="utf-8")
    pb, _ = controle(r, ajout(h, f"Référence `{orphelin}`."))
    assert avec(pb, "a", orphelin)


def test_a_fichier_non_suivi_sans_compagnon_ne_compte_pas(faux_depot):
    r, h = faux_depot
    h_libre = ecrire(r, "docs/non-suivi-v1.md", "ni suivi ni scellé\n")
    pb, _ = controle(r, ajout(h, f"Référence `{h_libre}`."))
    assert avec(pb, "a", h_libre)


def test_a_liste_sha256sum_et_marqueur_binaire(faux_depot):
    r, h = faux_depot
    ha = ecrire(r, "docs/lot/a.txt", "a\n")
    hb = ecrire(r, "docs/lot/b.bin", b"\x00b")
    (r / "docs" / "lot" / "empreintes.sha256").write_text(f"{ha}  a.txt\n{hb} *b.bin\n", encoding="utf-8")
    pb, _ = controle(r, ajout(h, f"Lot `{ha}` et `{hb}`."))
    assert not avec(pb, "a")


def test_a_compagnon_d_une_ligne_au_nom_ancien(faux_depot):
    """Un compagnon d'une ligne dont le nom ne désigne aucun fichier vaut pour le fichier dont il porte le nom."""
    r, h = faux_depot
    hx = ecrire(r, "docs/renomme-v1.md", "contenu\n")
    (r / "docs" / "renomme-v1.md.sha256").write_text(f"{hx}  ancien-nom.md\n", encoding="utf-8")
    pb, _ = controle(r, ajout(h, f"Référence `{hx}`."))
    assert not avec(pb, "a")


def test_a_compagnon_suivi_n_est_pas_un_fichier_designe(faux_depot):
    r, h = faux_depot
    h_compagnon = sha((r / "docs/contre-lectures/rapport-1-v1.md.sha256").read_bytes())
    pb, _ = controle(r, ajout(h, f"Référence `{h_compagnon}`."))
    assert avec(pb, "a", h_compagnon)


def test_a_compagnon_sous_git_ignore(faux_depot):
    r, h = faux_depot
    faux = "d" * 63 + "4"
    (r / ".git" / "piege.txt").write_text("x")
    (r / ".git" / "piege.txt.sha256").write_text(f"{faux}  piege.txt\n")
    pb, _ = controle(r, ajout(h, f"Référence `{faux}`."))
    assert avec(pb, "a", faux)


def test_a_hors_depot_git_avertissement(tmp_path):
    r = tmp_path / "sans-git"
    h = {"code": ecrire(r, "src/paquet/module.py", "".join(f"ligne {i}\n" for i in range(1, 21))),
         "rapport1": ecrire(r, "docs/contre-lectures/rapport-1-v1.md", "r1\n", compagnon=True),
         "rapport2": ecrire(r, "docs/contre-lectures/rapport-2-v1.md", "r2\n", compagnon=True),
         "brouillon": ecrire(r, "brouillons/p-v1-brouillon1.md", "b\n", compagnon=True)}
    t = texte_sain(h).replace(f"(empreinte `{h['code']}`", "(empreinte non citée")
    pb, av = controle(r, t)
    assert avec(pb, "b", h["code"][:12])                         # le préfixe ne se résout plus
    assert "index git indisponible : seuls les compagnons comptent" in av
    pb, _ = controle(r, texte_sain(h))
    assert not avec(pb, "a")                                     # appariée : vérifiée sur disque


def test_a_fichier_suivi_illisible(faux_depot, monkeypatch):
    r, h = faux_depot
    vrai = pr._hacher
    monkeypatch.setattr(pr, "_hacher", lambda p: (_ for _ in ()).throw(OSError("refus")) if p.name == "autre.py"
                        else vrai(p))
    pb, av = controle(r, ajout(h, f"Référence `{h['autre']}`."))
    assert avec(pb, "a", h["autre"]) and any("illisible" in x for x in av)


def test_mutation_q1_empreintes_de_la_contre_lecture_inventees(faux_depot):
    r, h = faux_depot
    t = texte_sain(h)
    cl = t.index("## Contre-lecture")
    faux = t[:cl] + pr.HEX64.sub(lambda m: sha(m.group(0).encode()), t[cl:])
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []
    assert len(avec(pb, "a")) == 3
    assert len(avec(pb, "e", "sans empreinte vérifiée")) == 2


def test_mutation_q2_toutes_les_empreintes_inventees(faux_depot):
    r, h = faux_depot
    faux = pr.HEX64.sub(lambda m: sha(m.group(0).encode()), texte_sain(h))
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []
    assert len(avec(pb, "a")) == 4 and avec(pb, "e")


# ========== (b) préfixes ==========

def test_b_prefixe_inconnu(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace(f"`{h['code'][:12]}…`", "`9a9a9a9a9a9a…`"))
    assert avec(pb, "b", "9a9a9a9a9a9a…")


@pytest.mark.parametrize("ellipse", ["...", "..", "‥", "⋯"])
def test_b_formes_d_ellipse(faux_depot, ellipse):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace(f"`{h['code'][:12]}…`", f"`9a9a9a9a9a9a{ellipse}`"))
    assert avec(pb, "b", "9a9a9a9a9a9a")


def test_b_prefixe_nu_entre_accents_graves(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, "Révision `9f8e7d6c5b4a`."))
    assert avec(pb, "b", "9f8e7d6c5b4a")
    pb, _ = controle(r, ajout(h, f"Révision `{h['code'][:12]}`."))
    assert not avec(pb, "b")


def test_b_prefixe_de_commit_accepte(faux_depot):
    r, h = faux_depot
    tete = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    pb, _ = controle(r, ajout(h, f"Au commit `{tete[:9]}…` et `{tete[:10]}`."))
    assert not avec(pb, "b")


def test_b_prefixe_ambigu_avertissement_seulement(faux_depot):
    r, h = faux_depot
    for nom, h_faux in (("x", "12345678" + "a" * 56), ("y", "12345678" + "b" * 56)):
        ecrire(r, f"docs/{nom}.txt", nom)
        (r / "docs" / f"{nom}.txt.sha256").write_text(f"{h_faux}  {nom}.txt\n", encoding="utf-8")
    pb, av = controle(r, ajout(h, "Préfixe `12345678…`."))
    assert not avec(pb, "b") and avec(av, "b", "ambigu")


def test_b_ignores_date_trop_court_sans_chiffre_colle(faux_depot):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, "Mentions `20261128…`, `20261128153000…`, `1234567…`, `deadbeefcafe…` et "
                                  "x9a9a9a9a9a9a…."))
    assert not avec(pb, "b") and not avec(av, "b")
    pb, _ = controle(r, ajout(h, "Numéro `12345678…`."))
    assert avec(pb, "b", "12345678")


# ========== (c) chemins ==========

def test_c_chemin_inexistant(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("`docs/contre-lectures/`", "`docs/absent/fichier-v1.md`"))
    assert avec(pb, "c", "docs/absent/fichier-v1.md")


def test_mutation_q3_chemins_inexistants(faux_depot):
    r, h = faux_depot
    faux = texte_sain(h).replace("src/paquet/", "src/nexiste_pas/").replace("docs/contre-lectures/", "docs/nexiste_pas/")
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []
    assert avec(pb, "c", "src/nexiste_pas/module.py") and avec(pb, "c", "docs/nexiste_pas/rapport-1-v1.md")


@pytest.mark.parametrize("racine_chemin", ["runs", "livrables", "registres", "scripts", "tests", "diag"])
def test_c_toutes_les_racines(faux_depot, racine_chemin):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, f"Voir `{racine_chemin}/absent-v1.txt`."))
    assert avec(pb, "c", f"{racine_chemin}/absent-v1.txt")


def test_c_dedoublonnage(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, "Voir `docs/absent-v1.md`, puis encore `docs/absent-v1.md`."))
    assert len(avec(pb, "c", "docs/absent-v1.md")) == 1


@pytest.mark.parametrize("suffixe", [":21", ":0", ":19-25", ":6-4", ":3,21", ":L21", ":19–25"])
def test_c_lignes_hors_du_fichier(faux_depot, suffixe):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("module.py:3-5", "module.py" + suffixe))
    assert avec(pb, "c", "lignes hors du fichier (20 lignes)")


@pytest.mark.parametrize("suffixe", [":1", ":20", ":1-20", ":L3", ":L3-L5", ":3–5", ":3,5", ":fonction",
                                     "::test_x", "#titre"])
def test_c_formes_legitimes(faux_depot, suffixe):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("module.py:3-5", "module.py" + suffixe))
    assert not avec(pb, "c")


def test_c_fichier_sans_saut_final(faux_depot):
    r, h = faux_depot
    ecrire(r, "src/paquet/court.py", "a\nb\nc")
    pb, _ = controle(r, ajout(h, "Voir `src/paquet/court.py:3`."))
    assert not avec(pb, "c")
    pb, _ = controle(r, ajout(h, "Voir `src/paquet/court.py:4`."))
    assert avec(pb, "c", "(3 lignes)")


def test_c_suffixe_sur_un_dossier(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("`docs/contre-lectures/`", "`docs/contre-lectures:3`"))
    assert avec(pb, "c", "dossier")


@pytest.mark.parametrize("motif", ["docs/absent-*.md", "src/absent…", "docs/absent-[ab].md", "docs/$NOM.md",
                                   "docs/absent-?.md", "docs/{a,b}.md", "runs/<id>/", "registres/passations/AAAA-MM-JJ-HHMM.md",
                                   "docs/rapport-XXX.md", "docs/rapport-NNN.md", "docs/absent..."])
def test_c_motifs_ignores(faux_depot, motif):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, f"Voir `{motif}`."))
    assert not avec(pb, "c")


def test_c_nom_avec_espaces(faux_depot):
    r, h = faux_depot
    ecrire(r, "docs/mon dossier/é a.md", "x\n")
    pb, _ = controle(r, ajout(h, "Voir `docs/mon dossier/é a.md`."))
    assert not avec(pb, "c")


def test_c_commande_entre_accents_graves(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, "Lancer `src/paquet/module.py --graine 3 sorties/`."))
    assert not avec(pb, "c")
    pb, _ = controle(r, ajout(h, "Lancer `src/paquet/absent.py --graine 3`."))
    assert avec(pb, "c", "src/paquet/absent.py")


def test_c_point_point_qui_sort_de_la_racine(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, ajout(h, "Voir `docs/../../hors.txt`."))
    assert avec(pb, "c", "sort de la racine")


# ========== remarques 2 et 3 : garde de lecture ==========

@pytest.mark.parametrize("chemin, garde", [
    ("donnees/x.npz", True), ("a/b.npy", True), ("m/model.safetensors", True), ("m/MODEL.SAFETENSORS", True),
    ("donnees/x.npz.sha256", False), ("prereg/P3-consignes-v1.md.sha256", False),
    ("brouillons/g0-criteres-2-3-v1/consignes-privees-v1.md", True),
    ("brouillons/g0-criteres-2-3-v1/consignes-privees-v2/a.txt", True),
    ("autre/g0-criteres-2-3-v1/consignes-privees-v2/a.txt", True),
    ("brouillons/g0-criteres-2-3-v1/autre.md", False),
    ("brouillons/consignes-privees-v1.md", False),
    ("brouillons/ii-b-saboteur-budget-v5/x.py", True), ("ii-b-saboteur-budget-v9/x.md", True),
    ("prereg/P3-consignes-v1.md", True), ("brouillons/P3-consignes-v1-brouillon1.md", True),
    ("x/P3-consignes-v1-candidat/y.md", True), ("prereg/p3-CONSIGNES-v1.md", True),
    ("prereg/P3-bis-consignes-v1.md", False),
    ("src/controle_ia/iib/a.py", True), ("controle_ia/iib/a.py", True), ("src/controle_ia/iibis.py", False),
    ("src/controle_ia/IIB/a.py", True),
    ("./src/controle_ia/iib/a.py", True), ("docs/../src/controle_ia/iib/a.py", True),
    ("src//controle_ia//iib/a.py", True), ("/abs/depot/src/controle_ia/iib/a.py", True),
    ("docs/note.md", False),
])
def test_est_garde(chemin, garde):
    assert pr.est_garde(chemin) is garde


def test_garde_aucun_fichier_garde_ouvert_par_l_index(faux_depot, ouvertures):
    r, h = faux_depot
    ecrire(r, "brouillons/ii-b-saboteur-budget-v9/secret.md", "secret\n")
    ecrire(r, "prereg/P3-consignes-v1.md", "consignes\n")
    ecrire(r, "x/P3-consignes-v1-candidat/y.md", "consignes\n")
    ecrire(r, "donnees/activations.npz", b"\x00\x01", compagnon=True)
    committer(r, "gardes")
    index = pr.Index(r)
    index.suivis()
    assert gardes_ouverts(ouvertures) == []
    assert set(index.gardes_sautes) >= {"brouillons/ii-b-saboteur-budget-v9/secret.md", "prereg/P3-consignes-v1.md",
                                        "x/P3-consignes-v1-candidat/y.md", "donnees/activations.npz",
                                        "src/controle_ia/iib/autre.py", "src/controle_ia/iib/poids.py"}
    assert any(c.endswith("activations.npz.sha256") for c in ouvertures)        # le compagnon, lui, est lu


def test_garde_lien_symbolique_suivi_non_hache(faux_depot, ouvertures):
    r, h = faux_depot
    os.symlink("../src/controle_ia/iib/poids.py", r / "docs" / "lien.md")
    ecrire(r, "donnees/x.npz", b"\x00npz")
    os.symlink("../donnees/x.npz", r / "docs" / "lien2.md")
    committer(r, "liens")
    pr.Index(r).suivis()
    assert gardes_ouverts(ouvertures) == []
    assert not [x for x in ouvertures if x.endswith(("lien.md", "lien2.md"))]


def test_garde_lien_symbolique_cite_avec_lignes(faux_depot, ouvertures):
    r, h = faux_depot
    os.symlink("../src/controle_ia/iib/poids.py", r / "docs" / "lien.md")
    pb, av = controle(r, ajout(h, "Voir `docs/lien.md:1`."))
    assert not avec(pb, "c") and avec(av, "c", "lien symbolique")
    assert gardes_ouverts(ouvertures) == [] and not [x for x in ouvertures if x.endswith("lien.md")]


def test_garde_lien_symbolique_apparie(faux_depot, ouvertures):
    r, h = faux_depot
    os.symlink("../src/controle_ia/iib/poids.py", r / "docs" / "lien.md")
    pb, _ = controle(r, ajout(h, f"Voir `docs/lien.md` (`{h['garde']}`)."))
    assert avec(pb, "a", "lien symbolique")
    assert gardes_ouverts(ouvertures) == []


def test_garde_dossier_parent_lien_vers_l_exterieur(faux_depot, tmp_path, ouvertures):
    r, h = faux_depot
    dehors = tmp_path / "dehors"
    dehors.mkdir()
    (dehors / "f.txt").write_text("a\nb\n")
    os.symlink(str(dehors), r / "docs" / "rep")
    pb, av = controle(r, ajout(h, "Voir `docs/rep/f.txt:1`."))
    assert avec(av, "c", "hors de la racine")
    assert not [x for x in ouvertures if x.endswith("f.txt")]


def test_garde_dossier_parent_lien_vers_un_dossier_garde(faux_depot, ouvertures):
    r, h = faux_depot
    os.symlink("../src/controle_ia/iib", r / "docs" / "rep")
    pb, av = controle(r, ajout(h, "Voir `docs/rep/autre.py:1`."))
    assert avec(av, "c", "fichier gardé")
    assert not [x for x in ouvertures if x.endswith(("rep/autre.py", "iib/autre.py"))]


def test_garde_chemin_garde_qui_mene_ailleurs(faux_depot, ouvertures):
    """`src/controle_ia/iib` lien vers un dossier ordinaire : le chemin cité reste gardé, rien n'est ouvert."""
    r, h = faux_depot
    ecrire(r, "autre/x.py", "a\n")
    os.rename(r / "src" / "controle_ia" / "iib", r / "src" / "controle_ia" / "iib-ancien")
    os.symlink("../../autre", r / "src" / "controle_ia" / "iib")
    pb, av = controle(r, ajout(h, "Voir `src/controle_ia/iib/x.py:1`."))
    assert avec(av, "c", "fichier gardé")
    assert gardes_ouverts(ouvertures) == []


def test_garde_compagnon_lien_symbolique_non_lu(faux_depot, ouvertures):
    r, h = faux_depot
    os.symlink("../src/controle_ia/iib/autre.py", r / "docs" / "piege.md.sha256")
    pr.Index(r)
    assert not [x for x in ouvertures if x.endswith("piege.md.sha256")]
    assert gardes_ouverts(ouvertures) == []


def test_garde_point_point_cite_vers_un_fichier_garde(faux_depot, ouvertures):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, "Voir `docs/../src/controle_ia/iib/autre.py:1` et "
                                  "`brouillons/../src/controle_ia/iib/poids.py:1`."))
    assert len(avec(av, "c", "fichier gardé")) == 2
    assert gardes_ouverts(ouvertures) == []


def test_garde_racine_sous_dossier(faux_depot, ouvertures):
    """Racine passée = `src` : `git ls-files` rend `controle_ia/iib/…`, qui reste gardé."""
    r, h = faux_depot
    index = pr.Index(r / "src")
    index.suivis()
    assert gardes_ouverts(ouvertures) == []
    assert "controle_ia/iib/poids.py" in index.gardes_sautes
    assert index.depot == r.resolve()


def test_garde_preenregistrement_garde_ou_lien_refuse(faux_depot, ouvertures):
    r, h = faux_depot
    for nom in ("prereg/P3-consignes-v1.md", "src/controle_ia/iib/p-v1.md", "x/P3-consignes-v1-b/p.md"):
        p = poser(r, texte_sain(h), nom=nom)
        with pytest.raises(GardeArret, match="garde de lecture"):
            pr.verifier_renforce(p, racine=r)
    os.symlink("p-v1.md", r / "prereg" / "lien-v1.md")
    poser(r, texte_sain(h))
    with pytest.raises(GardeArret, match="lien symbolique"):
        pr.verifier_renforce(r / "prereg" / "lien-v1.md", racine=r)
    assert gardes_ouverts(ouvertures) == []


def test_garde_preenregistrement_hors_racine(faux_depot, tmp_path, ouvertures):
    r, h = faux_depot
    dehors = tmp_path / "ailleurs" / "p-v1.md"
    dehors.parent.mkdir()
    dehors.write_text(texte_sain(h), encoding="utf-8")
    with pytest.raises(GardeArret, match="hors de la racine"):
        pr.verifier_renforce(dehors, racine=r)
    pb, _ = pr.verifier_renforce(dehors, racine=r, permettre_hors_racine=True)
    assert pb == []
    garde_dehors = tmp_path / "ailleurs" / "controle_ia" / "iib" / "x.md"
    garde_dehors.parent.mkdir(parents=True)
    garde_dehors.write_text("secret")
    with pytest.raises(GardeArret, match="garde de lecture"):
        pr.verifier_renforce(garde_dehors, racine=r, permettre_hors_racine=True)
    assert gardes_ouverts(ouvertures) == []


def test_garde_relatif_depuis_un_sous_dossier(faux_depot, monkeypatch, ouvertures):
    r, h = faux_depot
    poser(r, texte_sain(h), nom="src/controle_ia/iib/p-v1.md")
    monkeypatch.chdir(r / "src")
    with pytest.raises(GardeArret):
        pr.verifier_renforce("controle_ia/iib/p-v1.md", racine=".")
    assert gardes_ouverts(ouvertures) == []


def test_racine_du_depot(faux_depot, tmp_path):
    r, h = faux_depot
    assert pr.racine_du_depot(r / "src" / "paquet") == r.resolve()
    sans_git = tmp_path / "projet"
    (sans_git / "a" / "b").mkdir(parents=True)
    (sans_git / "CLAUDE.md").write_text("x")
    assert pr.racine_du_depot(sans_git / "a" / "b") == sans_git.resolve()


# ========== (d) longueur ==========

def test_mutation_q4_sections_reduites_a_un_mot(faux_depot):
    r, h = faux_depot
    t = texte_sain(h)
    faux = re.sub(r"(^## (?!Contre-lecture).+?$)(.*?)(?=^## )", lambda m: m.group(1) + "\n\nx\n\n", t, flags=re.M | re.S)
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []
    assert len(avec(pb, "d", "trop courte")) == len(SECTIONS) - 1


def test_d_seuil_parametre(faux_depot):
    r, h = faux_depot
    t = texte_sain(h).replace("## Seuil\n\n" + REMPLISSAGE, "## Seuil\n\nSeuil fixé à 0,05 en bilatéral, sans correction.")
    assert avec(controle(r, t)[0], "d", "Seuil (8 mots")
    assert not avec(controle(r, t, mots_min=8)[0], "d")


def test_d_contre_lecture_courte_et_saine(faux_depot):
    r, h = faux_depot
    cl = (f"* **Contre-lecture 1** : Fable 5.2 neuf, brouillon `brouillons/p-v1-brouillon1.md` (`{h['brouillon']}`), "
          f"verdict prête, aucune remarque ouverte.")
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl))
    assert not avec(pb, "d") and not avec(pb, "e")
    pb, _ = controle(r, texte_sain(h, contre_lecture=f"* **Contre-lecture 1** : Fable (`{h['brouillon']}`)."))
    assert avec(pb, "d", "Contre-lecture (4 mots, au moins 12)")


def test_d_section_repetitive(faux_depot):
    r, h = faux_depot
    t = texte_sain(h).replace("## Seuil\n\n" + REMPLISSAGE, "## Seuil\n\n" + "seuil fixé " * 20)
    assert avec(controle(r, t)[0], "d", "section répétitive : Seuil (2 mots distincts")


def test_d_ponctuation_ne_compte_pas(faux_depot):
    r, h = faux_depot
    t = texte_sain(h).replace("## Seuil\n\n" + REMPLISSAGE, "## Seuil\n\n" + "— | … " * 20 + "seuil fixé")
    assert avec(controle(r, t)[0], "d", "Seuil (2 mots")


# ========== (e) contre-lectures ==========

def test_e_entree_sans_modele(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("Claude Fable 5.2", "session indépendante"))
    assert avec(pb, "e", "contre-lecture 1 sans le modèle") and not avec(pb, "e", "contre-lecture 2")


def test_e_modele_dans_un_identifiant(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("par Opus 5.5", "par claude-opus-5-5"))
    assert not avec(pb, "e")


@pytest.mark.parametrize("faux", ["une fable sans morale", "un Operator", "le GPTq quantifié", "pièce écrite par Opus 5.5",
                                  "auteur : Fable 5.2", "rédigée par Gemini"])
def test_e_faux_modeles(faux_depot, faux):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("par Opus 5.5", faux))
    assert avec(pb, "e", "contre-lecture 2 sans le modèle")


def test_e_auteur_et_relecteur_nommes(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("par Opus 5.5", "par Fable 5.2 neuf, pièce écrite par Opus 5.5"))
    assert not avec(pb, "e")


def test_e_entree_sans_empreinte_verifiee(faux_depot):
    r, h = faux_depot
    t = texte_sain(h)
    i = t.index("* **Contre-lecture 2**")
    t = t[:i] + t[i:].replace(h["brouillon"], "1" * 64).replace(h["rapport2"], "2" * 64)
    pb, _ = controle(r, t)
    assert problemes(poser(r, t)) == []
    assert avec(pb, "e", "contre-lecture 2 sans empreinte") and not avec(pb, "e", "contre-lecture 1")


def test_e_section_sans_entrees(faux_depot):
    r, h = faux_depot
    cl = f"Relue par un agent neuf ; brouillon `{h['brouillon']}`, rapport `{h['rapport1']}`."
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl + " " + REMPLISSAGE))
    assert avec(pb, "e", "section Contre-lecture sans le modèle")
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl.replace("agent neuf", "agent neuf Fable 5.2") + " " + REMPLISSAGE))
    assert not avec(pb, "e")


@pytest.mark.parametrize("puce", ["- **Contre-lecture {k}**", "**Contre-lecture {k}**", "### Contre-lecture {k}",
                                  "* Contre-lecture {k}", "+ Contre-lecture {k}"])
def test_e_formes_d_entree(faux_depot, puce):
    r, h = faux_depot
    cl = "\n".join(puce.format(k=k) + f" : Opus 5.5 ; brouillon `{h['brouillon']}`, rapport `{h['rapport1']}`. "
                   + REMPLISSAGE for k in (1, 2))
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl))
    assert not [x for x in pb if x.startswith("(")]
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl.replace("Opus 5.5", "un relecteur", 1)))
    assert avec(pb, "e", "contre-lecture 1 sans le modèle")


def test_e_phrase_du_corps_n_ouvre_pas_d_entree(faux_depot):
    r, h = faux_depot
    cl = texte_sain(h).split("## Contre-lecture\n\n")[1].strip()
    cl = cl.replace("rien à reporter.", "rien à reporter.\nContre-lecture 3 prévue plus tard, sans objet ici.")
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl))
    assert not avec(pb, "e")


# ========== robustesse (remarque 9) ==========

def test_lecture_latin1_absent_bom(faux_depot):
    r, h = faux_depot
    latin = r / "prereg" / "latin-v1.md"
    latin.parent.mkdir(exist_ok=True)
    latin.write_bytes("## Hypothèse\n\ncafé\n".encode("latin-1"))
    assert pr.verifier_renforce(latin, racine=r)[0][0].startswith("(lecture) fichier non lisible en UTF-8")
    assert pr.verifier_renforce(r / "prereg" / "absent-v1.md", racine=r)[0][0].startswith("(lecture) fichier illisible")
    pb, _ = controle(r, "\ufeff" + texte_sain(h))
    assert any(x.startswith("(lecture) octet d'ordre") for x in pb)


def test_nb_lignes_en_flux(tmp_path, monkeypatch):
    p = tmp_path / "gros.txt"
    p.write_bytes(b"x\n" * 3 + b"fin")
    monkeypatch.setattr(pr, "_nb_lignes", pr._nb_lignes)
    assert pr._nb_lignes(p) == 4
    p.write_bytes(b"")
    assert pr._nb_lignes(p) == 0


def test_index_partage_entre_fichiers(faux_depot, monkeypatch):
    r, h = faux_depot
    index = pr.Index(r)
    p1 = poser(r, ajout(h, f"Référence `{h['autre']}`."), nom="prereg/a-v1.md")
    p2 = poser(r, ajout(h, f"Référence `{'c' * 63}1`."), nom="prereg/b-v1.md")
    assert pr.problemes_renforces(p1, racine=r, index=index) == []
    appels = []
    monkeypatch.setattr(pr, "_hacher", lambda p: appels.append(p) or "0" * 64)
    assert avec(pr.problemes_renforces(p2, racine=r, index=index), "a")
    assert appels == []


# ========== archives (décision de la mère du 28 novembre 2026) : gardées, seul le compagnon compte ==========

ARCHIVES = ("src/lots/a-v1.tar", "src/lots/b-v1.zip", "src/lots/c-v1.tar.gz", "src/lots/d-v1.tgz", "src/lots/e-v1.7z",
            "src/lots/f-v1.gz", "src/lots/G-V1.ZIP")


@pytest.mark.parametrize("chemin", ARCHIVES)
def test_est_garde_archives(chemin):
    assert pr.est_archive(chemin) and pr.est_garde(chemin)
    assert pr.est_archive(chemin + "/") and pr.est_garde("./" + chemin + "/.")       # forme normalisée
    assert not pr.est_garde(chemin + ".sha256") and not pr.est_archive(chemin + ".sha256")


def archives_ouvertes(liste):
    return [x for x in liste if pr.est_archive(x) or pr.est_archive(os.path.realpath(x))]


def test_archive_saine_par_compagnon_sans_ouverture(faux_depot, ouvertures):
    r, h = faux_depot
    empreintes = {a: ecrire(r, a, b"\x1f\x8b archive " + a.encode(), compagnon=True) for a in ARCHIVES}
    committer(r, "archives")
    citations = " ".join(f"Lot `{a}` (`{e}`)." for a, e in empreintes.items())
    pb, av = controle(r, ajout(h, citations))
    assert pb == [] and av == []
    assert archives_ouvertes(ouvertures) == []
    assert any(x.endswith("a-v1.tar.sha256") for x in ouvertures)          # le compagnon, lui, est lu


def test_artefact_archive_sans_compagnon(faux_depot, ouvertures):
    r, h = faux_depot
    e = ecrire(r, "src/lots/x-v1.tar.gz", b"\x1f\x8b sans compagnon")
    committer(r, "archive")
    index = pr.Index(r)
    pb, av = pr.verifier_renforce(poser(r, ajout(h, f"Lot `src/lots/x-v1.tar.gz` (`{e}`), lignes `src/lots/x-v1.tar.gz:1`.")),
                                  racine=r, index=index)
    assert not avec(pb, "a") and avec(av, "a", "empreinte d'archive non vérifiée : src/lots/x-v1.tar.gz")
    assert avec(av, "c", "fichier gardé")
    pb, _ = pr.verifier_renforce(poser(r, ajout(h, f"Référence nue `{e}`.")), racine=r, index=index)
    assert avec(pb, "a", e)                                                  # jamais hachée : inconnue
    assert "src/lots/x-v1.tar.gz" in index.gardes_sautes
    assert archives_ouvertes(ouvertures) == []


# ========== vérification des corrections : défauts N1 à N4 ==========

@pytest.fixture
def envois_git(monkeypatch):
    """Enregistre chaque appel à git fait par l'index, avec les objets envoyés à `cat-file`."""
    appels = []
    vrai = pr.Index._git

    def espion(self, *args, entree=None):
        appels.append((args, (entree or b"").decode().split()))
        return vrai(self, *args, entree=entree)

    monkeypatch.setattr(pr.Index, "_git", espion)
    return appels


def objets_lus(appels):
    """Objets dont git a rendu le contenu (`cat-file --batch`)."""
    return {o for args, entree in appels if args[:2] == ("cat-file", "--batch") for o in entree}


def objets_demandes(appels):
    return {o for args, entree in appels if args and args[0] == "cat-file" for o in entree}


def oid(r, rev, chemin):
    return subprocess.run(["git", "-C", str(r), "rev-parse", f"{rev}:{chemin}"], capture_output=True, text=True,
                          check=True).stdout.strip()


def test_n1_dossier_cite_aucun_objet_garde_demande(faux_depot, envois_git, ouvertures):
    r, h = faux_depot
    ecrire(r, "src/controle_ia/data.npz", b"\x00poids")
    h_ok = ecrire(r, "src/controle_ia/ok.py", "ok\n")
    committer(r, "dossier")
    gardes = {oid(r, "HEAD", "src/controle_ia/iib/poids.py"), oid(r, "HEAD", "src/controle_ia/iib/autre.py"),
              oid(r, "HEAD", "src/controle_ia/data.npz")}
    pb, av = controle(r, ajout(h, f"Dossier `src/controle_ia` (`{h_ok}`) et dossier `src/controle_ia/` (`{'5' * 63}a`)."))
    assert avec(av, "a", "à côté d'un dossier (src/controle_ia)")
    assert avec(pb, "a", "ne désigne aucun fichier") and not avec(pb, "a", h_ok)   # non appariée : connue ou non
    assert not (objets_demandes(envois_git) & gardes)
    assert gardes_ouverts(ouvertures) == []


def test_n1_historique_d_un_dossier_disparu_filtre_par_chemin(faux_depot, envois_git):
    """Un dossier effacé (absent du disque) : le journal git de ce chemin liste ses fichiers, dont un gardé ; seul le
    chemin cité exact est retenu, rien n'est demandé à `cat-file`."""
    r, h = faux_depot
    ecrire(r, "src/vieux/x.npz", b"\x00poids anciens")
    ecrire(r, "src/vieux/lisible.py", "lisible\n")
    committer(r, "vieux")
    garde = oid(r, "HEAD", "src/vieux/x.npz")
    lisible = oid(r, "HEAD", "src/vieux/lisible.py")
    git(r, "rm", "-rq", "src/vieux")
    committer(r, "efface")
    pb, _ = controle(r, ajout(h, f"Ancien dossier `src/vieux` (`{'6' * 63}b`)."))
    assert avec(pb, "a", "appariée à src/vieux non vérifiée (chemin absent)")
    assert garde not in objets_demandes(envois_git) and lisible not in objets_demandes(envois_git)


def test_n1_historique_ne_lit_que_le_chemin_exact(faux_depot, envois_git):
    r, h = faux_depot
    v1 = oid(r, "HEAD", "src/paquet/autre.py")
    (r / "src/paquet/autre.py").write_text("autre, version 2\n")
    (r / "src/paquet/voisin.py").write_text("voisin\n")
    committer(r)
    voisin = oid(r, "HEAD", "src/paquet/voisin.py")
    pb, av = controle(r, ajout(h, f"Code `src/paquet/autre.py` (`{h['autre']}`)."))
    assert avec(av, "a", "version ancienne")
    assert v1 in objets_lus(envois_git) and voisin not in objets_demandes(envois_git)


def test_n1_objet_arbre_jamais_lu_et_lecture_alignee(faux_depot, envois_git):
    """`src/x` est un dossier au premier commit, puis un fichier modifié deux fois : la révision citée désigne un arbre,
    qui n'est jamais lu, et la version ancienne du fichier est retrouvée."""
    r, h = faux_depot
    ecrire(r, "src/x/dedans.py", "dedans\n")
    committer(r, "x dossier")
    c1 = subprocess.run(["git", "-C", str(r), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    arbre = oid(r, c1, "src/x")
    git(r, "rm", "-rq", "src/x")
    h_v2 = ecrire(r, "src/x", "fichier, version 2\n")
    committer(r, "x fichier")
    (r / "src/x").write_text("fichier, version 3\n")
    committer(r, "x v3")
    pb, av = controle(r, ajout(h, f"Fichier `src/x` (`{h_v2}`) depuis le commit `{c1[:10]}`."))
    assert not avec(pb, "a") and avec(av, "a", "version ancienne de src/x")
    assert arbre not in objets_lus(envois_git)


def test_n1_historique_appel_direct_sur_un_dossier(faux_depot, envois_git):
    r, h = faux_depot
    index = pr.Index(r)
    assert index.historique("src/controle_ia", "0" * 64) is None
    assert index.historique("src/controle_ia/iib/poids.py", h["garde"]) is None
    assert not [a for a, _ in envois_git if a and a[0] in ("log", "cat-file")]


@pytest.mark.parametrize("forme", ["Contre-lecture {k} : {corps}", "Contre-lecture {k} — {corps}",
                                   "1. **Contre-lecture {k}** : {corps}", "{k}) Contre-lecture {k} : {corps}",
                                   "| Contre-lecture {k} | {corps} |"])
def test_n2_formes_d_entree_v1_decoupees(faux_depot, forme):
    r, h = faux_depot
    corps1 = f"Fable 5.2 neuf, brouillon `{h['brouillon']}`, rapport `{h['rapport1']}`. " + REMPLISSAGE
    corps2 = f"relue sans nommer personne, brouillon `{h['brouillon']}`, rapport `{h['rapport2']}`."
    cl = forme.format(k=1, corps=corps1) + "\n" + forme.format(k=2, corps=corps2)
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl))
    assert avec(pb, "e", "contre-lecture 2 sans le modèle") and not avec(pb, "e", "contre-lecture 1")


def test_n4_archive_avec_compagnon_et_empreinte_fausse(faux_depot, ouvertures):
    r, h = faux_depot
    e = ecrire(r, "src/lots/avec-v1.zip", b"PK archive", compagnon=True)
    committer(r, "archive")
    pb, av = controle(r, ajout(h, f"Lot `src/lots/avec-v1.zip` (`{'8' * 63}c`)."))
    assert avec(pb, "a", "l'archive src/lots/avec-v1.zip différente de celle de son compagnon")
    assert not avec(av, "a", "archive non vérifiée")
    pb, av = controle(r, ajout(h, f"Lot `src/lots/avec-v1.zip` (`{e}`)."))
    assert pb == [] and av == []
    assert archives_ouvertes(ouvertures) == []


def test_n3_empreinte_non_appariee_d_un_autre_fichier_de_la_ligne(faux_depot):
    r, h = faux_depot
    pb, av = controle(r, ajout(h, f"Code `src/paquet/module.py` signature `{h['autre']}`."))
    assert not avec(pb, "a") and avec(av, "a", "désigne src/paquet/autre.py, pas un chemin cité")
    pb, av = controle(r, ajout(h, f"Empreinte `{h['autre']}` du fichier `src/paquet/autre.py`."))
    assert not avec(av, "a", "pas un chemin cité")
