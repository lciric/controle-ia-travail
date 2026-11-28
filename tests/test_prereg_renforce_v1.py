"""Validateur renforcé des préenregistrements (v1) : un cas sain et un artefact par contrôle (R5).

Tout se joue dans un faux dépôt bâti dans un dossier temporaire ; rien ne lit le vrai dépôt. Les mutations q1 à q4
reprennent celles du lecteur B (`docs/notes/premortem-prereg-v4-20261128-v1/lecteur-B/scripts/t2a_validateur_mutations.py`)
qui relèvent de ces contrôles : empreintes de la contre-lecture inventées, toutes les empreintes inventées, chemins
inexistants, corps des sections réduit à un mot.
"""
import hashlib
import re
import subprocess

import pytest

from controle_ia import prereg_renforce_v1 as pr
from controle_ia.gardes import GardeArret
from controle_ia.prereg import SECTIONS, problemes

REMPLISSAGE = ("Ce paragraphe décrit la section avec assez de mots pour passer le seuil de longueur : il nomme "
               "l'objet mesuré, la population, la statistique, le sens attendu et la règle de décision, sans rien "
               "laisser à remplir ni renvoyer à un texte absent du dépôt. ")


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


@pytest.fixture
def faux_depot(tmp_path):
    """Faux dépôt : un code suivi par git sans compagnon, un rapport et un brouillon scellés, un fichier gardé."""
    r = tmp_path / "depot"
    r.mkdir()
    git(r, "init", "-q", "-b", "main")
    git(r, "config", "user.email", "test@example.invalid")
    git(r, "config", "user.name", "test")
    h = {
        "code": ecrire(r, "src/paquet/module.py", "".join(f"ligne {i}\n" for i in range(1, 21))),
        "rapport1": ecrire(r, "docs/contre-lectures/rapport-1-v1.md", "rapport de la contre-lecture 1\n", compagnon=True),
        "rapport2": ecrire(r, "docs/contre-lectures/rapport-2-v1.md", "rapport de la contre-lecture 2\n", compagnon=True),
        "brouillon": ecrire(r, "brouillons/p-v1-brouillon1.md", "brouillon relu\n", compagnon=True),
        "garde": ecrire(r, "donnees/activations.npz", b"\x00poids\x01", compagnon=True),
        "garde_sans_compagnon": ecrire(r, "donnees/autres.npy", b"\x00autres\x01"),
    }
    git(r, "add", "-A")
    git(r, "commit", "-q", "-m", "init")
    return r, h


def texte_sain(h, contre_lecture=None):
    corps = {s: REMPLISSAGE for s in SECTIONS}
    corps["Métrique"] = (REMPLISSAGE + f"La statistique est calculée par `src/paquet/module.py:3-5` "
                         f"(empreinte `{h['code']}`, préfixe `{h['code'][:12]}…`), voir aussi `docs/contre-lectures/`. "
                         "Les sorties iront sous `runs/<identifiant>/`, `diag/…/scores.json` et `docs/*.md`.")
    corps["Contre-lecture"] = contre_lecture or (
        f"* **Contre-lecture 1** — agent neuf Claude Fable 5.2 ; brouillon relu `brouillons/p-v1-brouillon1.md` "
        f"(`{h['brouillon']}`) ; rapport `docs/contre-lectures/rapport-1-v1.md` (`{h['rapport1']}`).\n"
        f"* **Contre-lecture 2** — vérification des corrections par Opus 5.5 ; brouillon `{h['brouillon']}`, "
        f"rapport `{h['rapport2']}` ; rien à reporter dans le code ni dans les critères gelés, et aucune "
        "remarque ouverte ne reste.")
    return "# Préenregistrement de test\n\n" + "\n".join(f"## {s}\n\n{corps[s]}\n" for s in SECTIONS)


def poser(racine, texte, nom="prereg/p-v1.md"):
    p = racine / nom
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return p


def controle(racine, texte, **kw):
    return pr.verifier_renforce(poser(racine, texte), racine=racine, **kw)


def avec(liste, lettre, motif=""):
    return [x for x in liste if x.startswith(f"({lettre})") and motif in x]


# ---------- cas sain ----------

def test_sain_aucun_probleme(faux_depot):
    r, h = faux_depot
    p = poser(r, texte_sain(h))
    assert problemes(p) == []
    assert pr.verifier_renforce(p, racine=r) == ([], [])
    assert pr.problemes_renforces(p, racine=r) == []


def test_sain_ligne_de_commande(faux_depot):
    r, h = faux_depot
    p = poser(r, texte_sain(h))
    assert pr._main(["--racine", str(r), str(p)]) == 0


def test_artefact_ligne_de_commande(faux_depot):
    r, h = faux_depot
    p = poser(r, texte_sain(h).replace(h["rapport1"], "e" * 64))
    assert pr._main(["--racine", str(r), str(p)]) == 1


def test_problemes_de_base_en_tete(faux_depot):
    r, h = faux_depot
    texte = texte_sain(h).replace("## Seuil\n", "## Seuil mal nommé\n")
    pb, _ = controle(r, texte)
    assert pb[0] == "section absente : Seuil"


# ---------- (a) empreintes complètes ----------

def test_a_empreinte_inventee_hors_contre_lecture(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace(h["code"], "0123456789abcdef" * 4))
    assert avec(pb, "a", "0123456789abcdef" * 4)


def test_a_empreinte_portee_par_compagnon_seul(faux_depot):
    """Fichier non suivi par git mais scellé : son compagnon suffit."""
    r, h = faux_depot
    h_libre = ecrire(r, "docs/libre-v1.md", "non suivi\n", compagnon=True)
    pb, _ = controle(r, texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + f"Référence `{h_libre}`. ", 1))
    assert not avec(pb, "a")


def test_a_compagnon_orphelin_ne_compte_pas(faux_depot):
    r, h = faux_depot
    orphelin = "f" * 63 + "1"
    (r / "docs" / "disparu-v1.md.sha256").write_text(f"{orphelin}  disparu-v1.md\n", encoding="utf-8")
    pb, _ = controle(r, texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + f"Référence `{orphelin}`. ", 1))
    assert avec(pb, "a", orphelin)


def test_a_fichier_non_suivi_sans_compagnon_ne_compte_pas(faux_depot):
    r, h = faux_depot
    h_libre = ecrire(r, "docs/non-suivi-v1.md", "ni suivi ni scellé\n")
    pb, _ = controle(r, texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + f"Référence `{h_libre}`. ", 1))
    assert avec(pb, "a", h_libre)


def test_a_liste_sha256sum_a_plusieurs_lignes(faux_depot):
    r, h = faux_depot
    ha = ecrire(r, "docs/lot/a.txt", "a\n")
    hb = ecrire(r, "docs/lot/b.txt", "b\n")
    (r / "docs" / "lot" / "empreintes.sha256").write_text(f"{ha}  a.txt\n{hb}  b.txt\n", encoding="utf-8")
    pb, _ = controle(r, texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + f"Lot `{ha}` et `{hb}`. ", 1))
    assert not avec(pb, "a")


def test_a_hors_depot_git_seuls_les_compagnons(tmp_path):
    r = tmp_path / "sans-git"
    h = {"code": ecrire(r, "src/paquet/module.py", "".join(f"ligne {i}\n" for i in range(1, 21))),
         "rapport1": ecrire(r, "docs/contre-lectures/rapport-1-v1.md", "r1\n", compagnon=True),
         "rapport2": ecrire(r, "docs/contre-lectures/rapport-2-v1.md", "r2\n", compagnon=True),
         "brouillon": ecrire(r, "brouillons/p-v1-brouillon1.md", "b\n", compagnon=True)}
    pb, _ = controle(r, texte_sain(h))
    reste = [x for x in pb if x.startswith("(")]
    assert len(reste) == 2 and avec(reste, "a", h["code"]) and avec(reste, "b", h["code"][:12])


def test_mutation_q1_empreintes_de_la_contre_lecture_inventees(faux_depot):
    r, h = faux_depot
    t = texte_sain(h)
    cl = t.index("## Contre-lecture")
    faux = t[:cl] + pr.HEX64.sub(lambda m: sha(m.group(0).encode()), t[cl:])
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []          # le validateur de base ne voit rien
    assert len(avec(pb, "a")) == 3
    assert len(avec(pb, "e", "sans empreinte qui désigne")) == 2


def test_mutation_q2_toutes_les_empreintes_inventees(faux_depot):
    r, h = faux_depot
    faux = pr.HEX64.sub(lambda m: sha(m.group(0).encode()), texte_sain(h))
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []
    assert len(avec(pb, "a")) == 4 and avec(pb, "e")


# ---------- (b) préfixes ----------

def test_b_prefixe_inconnu(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace(f"`{h['code'][:12]}…`", "`9a9a9a9a9a9a…`"))
    assert avec(pb, "b", "9a9a9a9a9a9a…")


def test_b_prefixe_en_trois_points(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace(f"`{h['code'][:12]}…`", "`9a9a9a9a9a9a...`"))
    assert avec(pb, "b", "9a9a9a9a9a9a")


def test_b_prefixe_ambigu_avertissement_seulement(faux_depot):
    r, h = faux_depot
    for nom, h_faux in (("x", "12345678" + "a" * 56), ("y", "12345678" + "b" * 56)):
        ecrire(r, f"docs/{nom}.txt", nom)
        (r / "docs" / f"{nom}.txt.sha256").write_text(f"{h_faux}  {nom}.txt\n", encoding="utf-8")
    pb, av = controle(r, texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + "Préfixe `12345678…`. ", 1))
    assert not avec(pb, "b") and avec(av, "b", "ambigu")


def test_b_ignores_trop_court_ou_sans_chiffre(faux_depot):
    r, h = faux_depot
    ajout = "Mentions `1234567…` et `deadbeefcafe…`. "
    pb, av = controle(r, texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + ajout, 1))
    assert not avec(pb, "b") and not av


# ---------- (c) chemins ----------

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


@pytest.mark.parametrize("suffixe", [":21", ":0", ":19-25", ":6-4"])
def test_c_lignes_hors_du_fichier(faux_depot, suffixe):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("module.py:3-5", "module.py" + suffixe))
    assert avec(pb, "c", "lignes hors du fichier (20 lignes)")


@pytest.mark.parametrize("suffixe", [":1", ":20", ":1-20"])
def test_c_lignes_dans_le_fichier(faux_depot, suffixe):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("module.py:3-5", "module.py" + suffixe))
    assert not avec(pb, "c")


def test_c_suffixe_sur_un_dossier(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("`docs/contre-lectures/`", "`docs/contre-lectures:3`"))
    assert avec(pb, "c", "dossier")


def test_c_motifs_ignores(faux_depot):
    """Le texte sain cite `runs/<identifiant>/`, `diag/…/scores.json` et `docs/*.md` : aucun n'est signalé."""
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("`docs/*.md`", "`docs/absent-*.md` et `src/absent…`"))
    assert not avec(pb, "c")


def test_c_lignes_non_comptees_dans_un_fichier_garde(faux_depot, monkeypatch):
    r, h = faux_depot
    ecrire(r, "src/controle_ia/iib/secret.py", "x\n")
    vrai = pr._nb_lignes
    monkeypatch.setattr(pr, "_nb_lignes", lambda p: pytest.fail(f"fichier gardé ouvert : {p}") if "iib" in str(p)
                        else vrai(p))
    pb, av = controle(r, texte_sain(h).replace("`docs/contre-lectures/`", "`src/controle_ia/iib/secret.py:4`"))
    assert not avec(pb, "c") and avec(av, "c", "garde de lecture")


# ---------- (d) sections trop courtes ----------

def test_mutation_q4_sections_reduites_a_un_mot(faux_depot):
    r, h = faux_depot
    t = texte_sain(h)
    faux = re.sub(r"(^## (?!Contre-lecture).+?$)(.*?)(?=^## )", lambda m: m.group(1) + "\n\nx\n\n", t, flags=re.M | re.S)
    pb, _ = controle(r, faux)
    assert problemes(poser(r, faux)) == []
    assert len(avec(pb, "d")) == len(SECTIONS) - 1


def test_d_seuil_parametre(faux_depot):
    r, h = faux_depot
    t = texte_sain(h).replace("## Seuil\n\n" + REMPLISSAGE, "## Seuil\n\nSeuil fixé à 0,05 en bilatéral, sans correction.")
    assert avec(controle(r, t)[0], "d", "Seuil (8 mots")
    assert not avec(controle(r, t, mots_min=8)[0], "d")


# ---------- (e) contre-lectures ----------

def test_e_entree_sans_modele(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("Claude Fable 5.2", "session indépendante"))
    assert avec(pb, "e", "contre-lecture 1 sans le modèle") and not avec(pb, "e", "contre-lecture 2")


def test_e_modele_dans_un_identifiant(faux_depot):
    r, h = faux_depot
    pb, _ = controle(r, texte_sain(h).replace("par Opus 5.5", "par claude-opus-5-5"))
    assert not avec(pb, "e")


def test_e_entree_sans_empreinte_resolue(faux_depot):
    """Deux empreintes présentes (le validateur de base passe) mais aucune ne désigne un fichier."""
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
                                  "* Contre-lecture {k}"])
def test_e_formes_d_entree(faux_depot, puce):
    r, h = faux_depot
    cl = "\n".join(puce.format(k=k) + f" : Opus 5.5 ; brouillon `{h['brouillon']}`, rapport `{h['rapport1']}`. "
                   + REMPLISSAGE for k in (1, 2))
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl))
    assert not [x for x in pb if x.startswith("(")]
    pb, _ = controle(r, texte_sain(h, contre_lecture=cl.replace("Opus 5.5", "un relecteur", 1)))
    assert avec(pb, "e", "contre-lecture 1 sans le modèle")


# ---------- garde de lecture ----------

@pytest.mark.parametrize("rel, garde", [
    ("donnees/x.npz", True), ("a/b.npy", True), ("m/model.safetensors", True),
    ("donnees/x.npz.sha256", False),
    ("brouillons/g0-criteres-2-3-v1/consignes-privees-v1.md", True),
    ("brouillons/g0-criteres-2-3-v1/consignes-privees-v2/a.txt", True),
    ("brouillons/g0-criteres-2-3-v1/autre.md", False),
    ("brouillons/ii-b-saboteur-budget-v5/x.py", True),
    ("prereg/P3-consignes-v1.md", True), ("brouillons/P3-consignes-v1-brouillon1.md", True),
    ("prereg/P3-bis-consignes-v1.md", False),
    ("src/controle_ia/iib/a.py", True), ("src/controle_ia/iibis.py", False),
    ("./src/controle_ia/iib/a.py", True),
])
def test_est_garde(rel, garde):
    assert pr.est_garde(rel) is garde


def test_garde_aucun_fichier_garde_hache(faux_depot, monkeypatch):
    r, h = faux_depot
    ecrire(r, "brouillons/ii-b-saboteur-budget-v9/secret.md", "secret\n")
    ecrire(r, "prereg/P3-consignes-v1.md", "consignes\n")
    git(r, "add", "-A")
    git(r, "commit", "-q", "-m", "gardes")
    haches = []
    vrai = pr._hacher
    monkeypatch.setattr(pr, "_hacher", lambda p: haches.append(str(p)) or vrai(p))
    t = texte_sain(h).replace(REMPLISSAGE, REMPLISSAGE + f"Données `{h['garde']}` et `{h['garde_sans_compagnon']}`. ", 1)
    pb, _ = controle(r, t)
    assert haches, "les fichiers suivis doivent avoir été hachés"
    assert not [x for x in haches if pr.est_garde(x.split(str(r) + "/", 1)[-1])]
    assert not avec(pb, "a", h["garde"])                     # compagnon d'un fichier gardé : compte
    assert avec(pb, "a", h["garde_sans_compagnon"])          # fichier gardé sans compagnon : jamais haché


def test_garde_preenregistrement_garde_refuse(faux_depot):
    r, h = faux_depot
    p = poser(r, texte_sain(h), nom="prereg/P3-consignes-v1.md")
    with pytest.raises(GardeArret, match="garde de lecture"):
        pr.verifier_renforce(p, racine=r)


def test_index_partage_entre_fichiers(faux_depot, monkeypatch):
    r, h = faux_depot
    index = pr.Index(r)
    p1 = poser(r, texte_sain(h), nom="prereg/a-v1.md")
    p2 = poser(r, texte_sain(h).replace(h["code"], "c" * 64), nom="prereg/b-v1.md")
    assert pr.problemes_renforces(p1, racine=r, index=index) == []
    appels = []
    monkeypatch.setattr(pr, "_hacher", lambda p: appels.append(p) or "0" * 64)
    assert avec(pr.problemes_renforces(p2, racine=r, index=index), "a")
    assert appels == []                                      # index déjà construit : rien n'est re-haché
