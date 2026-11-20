"""Essais du verrou des graines décisives (code v5 ; préenregistrement v11, B8, versions 7, 9 et 10 ; note D6 ; décisions de
la mère R-4123 et R-4182, remarque 4 de l'annexe H, « Version 9 », points (a) à (e) ; « Ce qui demande un code v5 », points 4
et 6). Chaque condition du verrou a son cas sain et son artefact (règle R5) :
- le texte présenté est scellé, au sens de `controle_ia.scellement.verifier` (compagnon d'une ligne, au bon nom, empreinte
  égale) ;
- la pièce d'autorisation existe au chemin gelé sous la racine de l'arbre lancé et est scellée ;
- elle porte quatre lignes « nom : valeur », dans l'ordre de la décision R-4123 ;
- l'identifiant du GO est bien formé et figure dans la première colonne d'une ligne de `registres/go.md` de l'arbre lancé ;
- le commit de la pièce est celui que le texte inscrit en tête ; l'empreinte de la pièce est celle du texte présenté, recalculée ;
- l'heure est en UTC (forme seule) ;
- chaque module lancé a l'empreinte que la table du texte lui donne, et la table n'en nomme pas d'autre ;
- l'autorisation est vérifiée de nouveau avant le lancement d'une couche décisive ;
- le manifeste inscrit l'empreinte du texte présenté, celle de la pièce et l'heure, à la place de l'empreinte de la version 6.
Les arbres sont factices, dans un dossier temporaire ; aucune graine décisive n'est dérivée (l'essai final le contrôle)."""

import hashlib
import importlib.util
import json
import os
import sys

import pytest

from aides_heritage_etage_processeur_v1 import FREQUENCES_D_ESSAI, chemin_env, prop
from controle_ia.heritage_etage_processeur_v1 import constantes as K
from controle_ia.heritage_etage_processeur_v1 import graines as GR
from controle_ia.heritage_etage_processeur_v1 import tirages as TI

COMMIT_ESSAI = "0123456789abcdef0123456789abcdef01234567"
AUTRE_COMMIT = "fedcba9876543210fedcba9876543210fedcba98"
GO_ESSAI = "GO-2099-01-01-01"
HEURE_DATE_U = "Fri Nov 20 10:57:51 UTC 2026"
CHAMPS = ("identifiant du GO", "commit du code", "empreinte du texte scellé", "heure")
PAQUET = "src/controle_ia/heritage_etage_processeur_v1/"


def _sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def _sceller(chemin):
    sha = _sha(chemin)
    with open(str(chemin) + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def _table_des_modules():
    """La table du code lancé, calculée ici à part du module `graines` : chaque fichier `.py` du paquet et le `__init__.py` du
    paquet parent ; une ligne hors de `src/` (ignorée par le contrôle des modules) pour que la table ressemble à celle du texte."""
    paquet = os.path.dirname(os.path.abspath(GR.__file__))
    lignes = [(_sha(os.path.join(paquet, f)), PAQUET + f) for f in sorted(os.listdir(paquet)) if f.endswith(".py")]
    lignes.append((_sha(os.path.join(os.path.dirname(paquet), "__init__.py")), "src/controle_ia/__init__.py"))
    lignes.append(("e" * 64, "tests/test_heritage_etage_processeur_v1_verrou.py"))
    return lignes


def _ecrire_texte(chemin, commit=COMMIT_ESSAI, table=None, deux_lignes_de_commit=False):
    t = ["# Texte d'essai du verrou", "", "- Auteur : essai.",
         f"- Commit du code d'analyse : **`{commit}`** (essai). Table des empreintes :", "", "  ```"]
    t += [f"  {h}  {p}" for h, p in (table if table is not None else _table_des_modules())]
    t += ["  ```", ""]
    if deux_lignes_de_commit:
        t += [f"- Commit du code d'analyse : **`{AUTRE_COMMIT}`** (seconde ligne).", ""]
    t += ["Le commit du code d'analyse est inscrit en tête.", ""]
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(t))
    return _sceller(chemin)


def _ecrire_go(racine, lignes=None):
    chemin = os.path.join(racine, "registres", "go.md")
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    corps = lignes if lignes is not None else [
        f"| {GO_ESSAI} | 2099-01-01 | calcul | essai du verrou | — | 2099-01-01 | essai | essai |",
        "| GO-2099-01-01-03 | 2099-01-01 | calcul | essai | — | 2099-01-01 | essai | GO-2099-01-01-02 |",
        "| GO-essai | 2099-01-01 | calcul | identifiant mal formé | — | 2099-01-01 | essai | essai |"]
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("# Registre des GO (essai)\n\n| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
                "|---|---|---|---|---|---|---|---|\n" + "\n".join(corps) + "\n")


def _ecrire_piece(racine, valeurs, noms=CHAMPS, sceller=True):
    chemin = os.path.join(racine, K.CHEMIN_PIECE_D_AUTORISATION)
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(f"{n} : {v}" for n, v in zip(noms, valeurs)) + "\n")
    if sceller:
        _sceller(chemin)
    return chemin


def _arbre(base, go=GO_ESSAI, commit=COMMIT_ESSAI, heure=HEURE_DATE_U, empreinte=None, table=None,
           deux_lignes_de_commit=False):
    """Un arbre factice sain par défaut : texte scellé, registre des GO, pièce scellée. Rend (racine, texte, pièce)."""
    racine = str(base / "arbre")
    texte = os.path.join(racine, "prereg", "texte-essai-v1.md")
    sha_texte = _ecrire_texte(texte, table=table, deux_lignes_de_commit=deux_lignes_de_commit)
    _ecrire_go(racine)
    piece = _ecrire_piece(racine, (go, commit, empreinte or sha_texte, heure))
    return racine, texte, piece


def test_constantes_sans_empreinte_du_texte():
    """Point 4 du code v5 (note D6 ; silence n° 13) : la constante qui portait l'empreinte de la version 6 est retirée ; aucune
    empreinte de 64 chiffres hexadécimaux n'est écrite dans `constantes.py` ; l'en-tête dit la version 11 ; le chemin de la
    pièce est celui de la décision R-4123."""
    import re
    assert not hasattr(K, "PREENREGISTREMENT_SHA256")
    with open(K.__file__, encoding="utf-8") as f:
        texte = f.read()
    assert not re.search(r"[0-9a-f]{64}", texte) and "4aee136b" not in texte
    assert "préenregistrement v11" in texte.split("\n")[0] and "v6" not in texte.split("\n")[0]
    assert K.CHEMIN_PIECE_D_AUTORISATION == "prereg/organisme-auto-conception-v9/palier-0b/autorisation-verrou-palier-0b-v1.md"
    assert K.CHAMPS_DE_LA_PIECE == CHAMPS


def test_verrou_cas_sain_sans_graine_decisive(tmp_path):
    """Cas sain : l'autorisation se construit sur un arbre factice conforme, sous les deux formes d'heure admises ; elle est
    vérifiée de nouveau avant un lancement décisif (sans rien tirer) ; un manifeste écrit avec elle (couche « essai ») inscrit
    l'empreinte du texte présenté, celle de la pièce et l'heure ; aucune graine décisive n'est dérivée."""
    racine, texte, piece = _arbre(tmp_path)
    a = GR.Autorisation(texte, racine)
    assert (a.sha_texte, a.sha_piece, a.go, a.commit, a.heure) == (_sha(texte), _sha(piece), GO_ESSAI, COMMIT_ESSAI,
                                                                   HEURE_DATE_U)
    r2, t2, _ = _arbre(tmp_path / "iso", heure="2026-11-20T10:57:51Z")
    assert GR.Autorisation(t2, r2).heure == "2026-11-20T10:57:51Z"
    r3, t3, _ = _arbre(tmp_path / "jour-a-un-chiffre", heure="Sun Nov  1 09:05:00 UTC 2026")  # `date -u`, jour d'un chiffre
    assert GR.Autorisation(t3, r3)
    g = GR.Graines(autorisation=a)
    for couche in GR.COUCHES_DECISIVES:
        assert TI.exiger_autorisation_pour(couche, g)
    case = {"famille": "A", "proposeur": "sourd-egal", "config": prop("sourd-egal"), "dose": 0.25, "taux": 0.25,
            "bras": ("1", "2", "3")}
    TI.lancer_famille(g, "essai", [case], lambda c: FREQUENCES_D_ESSAI, 2, str(tmp_path / "run"), COMMIT_ESSAI, {})
    chemin_m = str(tmp_path / "run" / "manifeste.json")
    with open(chemin_m, encoding="utf-8") as f:
        m = json.load(f)
    assert "preenregistrement_sha256" not in m
    assert (m["texte_sha256"], m["piece_d_autorisation_sha256"], m["heure_d_autorisation"]) == (a.sha_texte, a.sha_piece,
                                                                                                a.heure)
    assert TI.verifier_manifeste(chemin_m) == m["etiquettes"]["nombre"]
    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()
    assert g.etiquettes and all(e.startswith("couche=essai|") for e in g.etiquettes)


def _supprimer(chemin):
    os.remove(chemin)


def _ajouter(chemin, octets=b"\nligne ajoutee apres le scellement\n"):
    with open(chemin, "ab") as f:
        f.write(octets)


def _compagnon(chemin, texte):
    with open(chemin + ".sha256", "w", encoding="utf-8") as f:
        f.write(texte)


def _table_alteree(quoi):
    t = _table_des_modules()
    if quoi == "empreinte":
        return [("0" * 64 if p == PAQUET + "audit.py" else h, p) for h, p in t]
    if quoi == "absent":
        return [(h, p) for h, p in t if p != PAQUET + "graines.py"]
    return t + [("1" * 64, PAQUET + "module_non_lance.py")]


def _artefact(nom, base):
    """Construit l'artefact `nom` ; rend (texte, racine) à présenter au verrou."""
    if nom == "texte-sans-compagnon":
        racine, texte, _ = _arbre(base)
        _supprimer(texte + ".sha256")
    elif nom == "texte-altere-apres-scellement":
        racine, texte, _ = _arbre(base)
        _ajouter(texte)
    elif nom == "compagnon-du-texte-a-deux-lignes":
        racine, texte, _ = _arbre(base)
        _compagnon(texte, f"{_sha(texte)}  {os.path.basename(texte)}\n{_sha(texte)}  autre.md\n")
    elif nom == "compagnon-du-texte-au-mauvais-nom":
        racine, texte, _ = _arbre(base)
        _compagnon(texte, f"{_sha(texte)}  autre-nom.md\n")
    elif nom == "piece-absente":
        racine, texte, piece = _arbre(base)
        _supprimer(piece)
        _supprimer(piece + ".sha256")
    elif nom == "piece-sans-compagnon":
        racine, texte, piece = _arbre(base)
        _supprimer(piece + ".sha256")
    elif nom == "piece-alteree-apres-scellement":
        racine, texte, piece = _arbre(base)
        _ajouter(piece, b" ")
    elif nom == "champs-dans-un-autre-ordre":
        racine, texte, _ = _arbre(base)
        _ecrire_piece(racine, (COMMIT_ESSAI, GO_ESSAI, _sha(texte), HEURE_DATE_U), noms=(CHAMPS[1], CHAMPS[0]) + CHAMPS[2:])
    elif nom == "piece-a-trois-lignes":
        racine, texte, _ = _arbre(base)
        _ecrire_piece(racine, (GO_ESSAI, COMMIT_ESSAI, _sha(texte)), noms=CHAMPS[:3])
    elif nom == "go-absent-du-registre":
        racine, texte, _ = _arbre(base, go="GO-2099-01-01-09")
    elif nom == "go-hors-de-la-premiere-colonne":
        racine, texte, _ = _arbre(base, go="GO-2099-01-01-02")  # seulement dans la colonne « référence »
    elif nom == "go-mal-forme":
        racine, texte, _ = _arbre(base, go="GO-essai")  # dans la première colonne, mais mal formé
    elif nom == "registre-des-go-absent":
        racine, texte, _ = _arbre(base)
        _supprimer(os.path.join(racine, "registres", "go.md"))
    elif nom == "commit-different-du-texte":
        racine, texte, _ = _arbre(base, commit=AUTRE_COMMIT)
    elif nom == "deux-lignes-de-commit":
        racine, texte, _ = _arbre(base, deux_lignes_de_commit=True)
    elif nom == "empreinte-du-texte-differente":
        racine, texte, _ = _arbre(base, empreinte="0" * 64)
    elif nom == "heure-non-utc":
        racine, texte, _ = _arbre(base, heure="2026-11-20 11:57:51+01:00")
    elif nom == "module-d-empreinte-differente":
        racine, texte, _ = _arbre(base, table=_table_alteree("empreinte"))
    elif nom == "module-absent-de-la-table":
        racine, texte, _ = _arbre(base, table=_table_alteree("absent"))
    elif nom == "module-non-lance-dans-la-table":
        racine, texte, _ = _arbre(base, table=_table_alteree("en-trop"))
    else:
        raise AssertionError(nom)
    return texte, racine


ARTEFACTS = ("texte-sans-compagnon", "texte-altere-apres-scellement", "compagnon-du-texte-a-deux-lignes",
             "compagnon-du-texte-au-mauvais-nom", "piece-absente", "piece-sans-compagnon", "piece-alteree-apres-scellement",
             "champs-dans-un-autre-ordre", "piece-a-trois-lignes", "go-absent-du-registre", "go-hors-de-la-premiere-colonne",
             "go-mal-forme", "registre-des-go-absent", "commit-different-du-texte", "deux-lignes-de-commit",
             "empreinte-du-texte-differente", "heure-non-utc", "module-d-empreinte-differente", "module-absent-de-la-table",
             "module-non-lance-dans-la-table")


@pytest.mark.parametrize("nom", ARTEFACTS)
def test_verrou_artefact(nom, tmp_path):
    """Chaque artefact, sur un arbre factice par ailleurs sain : l'autorisation est refusée (`GraineRefusee`), rien n'est
    dérivé."""
    texte, racine = _artefact(nom, tmp_path)
    with pytest.raises(GR.GraineRefusee, match="autorisation refusée"):
        GR.Autorisation(texte, racine)
    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()


def test_verrou_verifie_de_nouveau_avant_un_lancement_decisif(tmp_path):
    """L'autorisation construite, la pièce changée puis rescellée (son empreinte du texte n'est plus celle du texte) : le
    lancement d'une couche décisive est refusé avant toute simulation ; un module dont l'empreinte change après la construction
    l'est aussi (la table du texte est réécrite et rescellée, pour que seul le module diffère)."""
    racine, texte, piece = _arbre(tmp_path)
    g = GR.Graines(autorisation=GR.Autorisation(texte, racine))
    assert TI.exiger_autorisation_pour("decisif", g)
    _ecrire_piece(racine, (GO_ESSAI, COMMIT_ESSAI, "0" * 64, HEURE_DATE_U))
    for couche in GR.COUCHES_DECISIVES:
        with pytest.raises(GR.GraineRefusee, match="autorisation refusée"):
            TI.exiger_autorisation_pour(couche, g)
    racine2, texte2, _ = _arbre(tmp_path / "module")
    g2 = GR.Graines(autorisation=GR.Autorisation(texte2, racine2))
    sha2 = _ecrire_texte(texte2, table=_table_alteree("empreinte"))
    _ecrire_piece(racine2, (GO_ESSAI, COMMIT_ESSAI, sha2, HEURE_DATE_U))
    with pytest.raises(GR.GraineRefusee, match="n'a pas l'empreinte que la table"):
        TI.exiger_autorisation_pour("decisif", g2)
    assert "decisif" not in GR.couches_derivees() and "confirmation" not in GR.couches_derivees()


def _scellement_du_depot():
    """Le module `controle_ia.scellement` du dépôt (HERITAGE_DEPOT), chargé sous un autre nom de paquet."""
    src = os.path.join(chemin_env("HERITAGE_DEPOT"), "src", "controle_ia")
    nom = "controle_ia_du_depot_pour_le_verrou"
    if nom not in sys.modules:
        spec = importlib.util.spec_from_file_location(nom, os.path.join(src, "__init__.py"), submodule_search_locations=[src])
        paquet = importlib.util.module_from_spec(spec)
        sys.modules[nom] = paquet
        spec.loader.exec_module(paquet)
    return importlib.import_module(nom + ".scellement")


def test_scelle_au_sens_du_depot(tmp_path):
    """Remarque 4, point (a) : « scellée » au sens de `controle_ia.scellement.verifier`. La réécriture du verrou
    (`graines.verifier_scelle`, ce paquet se lançant seul) accepte et refuse exactement ce que le module du dépôt accepte et
    refuse, sur un cas sain et sur six artefacts de compagnon."""
    depot = _scellement_du_depot()
    cas = {}
    for nom, compagnon in (("sain", "{h}  {n}\n"), ("sain-sans-saut-final", "{h}  {n}"), ("sain-lignes-vides", "\n{h}  {n}\n\n"),
                           ("absent", None), ("deux-lignes", "{h}  {n}\n{h}  {n}\n"), ("mauvais-nom", "{h}  autre.md\n"),
                           ("une-seule-espace", "{h} {n}\n"), ("empreinte-fausse", "{z}  {n}\n"), ("majuscules", "{H}  {n}\n")):
        f = tmp_path / f"fichier-{nom}.md"
        f.write_text(f"contenu {nom}\n", encoding="utf-8")
        h = _sha(f)
        if compagnon is not None:
            (tmp_path / (f.name + ".sha256")).write_text(
                compagnon.format(h=h, H=h.upper(), n=f.name, z="0" * 64), encoding="utf-8")
        try:
            depot.verifier(f)
            a = True
        except Exception:
            a = False
        try:
            GR.verifier_scelle(str(f))
            b = True
        except GR.GraineRefusee:
            b = False
        cas[nom] = (a, b)
    assert all(a == b for a, b in cas.values()), cas
    assert [n for n, (a, _) in cas.items() if a] == ["sain", "sain-sans-saut-final", "sain-lignes-vides"], cas
