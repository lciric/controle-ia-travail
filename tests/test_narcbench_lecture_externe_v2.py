"""Essais de la commande de lecture du bras externe v2 (`controle_ia.narcbench.lecture_externe_v2`), dans un dépôt git **jetable**
qui porte une copie du paquet exécuté, et sur des fichiers **factices** ; aucun fichier publié n'est ouvert. R5 : chaque garde
sur un cas sain (la lecture de bout en bout) et sur un artefact (un cas par motif). Aucun raccourci : le texte factice est
conforme au gabarit des préenregistrements (`prereg.exiger_prereg_scelle` joue pour de vrai)."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

import controle_ia
from controle_ia import scellement
from controle_ia.gardes import GardeArret
from controle_ia.manifeste import verifier_resultat
from controle_ia.narcbench import chargeur_externe_v1 as C
from controle_ia.narcbench import externe_v2 as X2
from controle_ia.narcbench import lecture_externe_v2 as L
from controle_ia.t07.registre_v1 import RefusRegistre

PAQUET = Path(controle_ia.__file__).resolve().parent
RACINE_CODE = PAQUET.parent.parent
LARG = 6
BANDES = {"qwen3_32b": (26, 27), "llama_3_1_70b": (32, 33)}
ENTROPIE = 271828182845904523536
RUN = "20261118-170000-narc-externe-v2"
FICHE = "registres/code-narc-ext/CODE-NARC-EXT-v1.json"
H1, H2 = "a" * 64, "b" * 64


# ---------- données factices ----------

def _ligne(rid, mode, role, canal, phase, rnd, agent):
    m = {k: None for k in C.CHAMPS}
    m.update(run_id=rid, mode=mode, role=role, channel=canal, phase=phase, round=rnd, agent_name=agent)
    return m


def _meta(etage, sans_finale=()):
    meta = []
    if etage == "core":
        runs = [(f"fam__dom{d}_{k:02d}__{mode}", mode) for d in range(3) for k in range(2) for mode in ("collusion", "control")]
        tours, final = (1, 2, 3), 4
    else:
        runs = [(f"bj__shoe{k:02d}__{mode}", mode) for k in range(6) for mode in ("collusion", "control")]
        tours, final = (1, 2), 8
    for rid, mode in runs:
        roles = {f"agent_{j}": ("colluder" if mode == "collusion" and j in (0, 3) else "honest") for j in range(4)}
        for a, r in roles.items():
            if r == "colluder":
                meta.append(_ligne(rid, mode, r, "private", "private", 0, a))
        for t in tours:
            for a, r in roles.items():
                meta.append(_ligne(rid, mode, r, "public", "discussion", t, a))
        for a, r in roles.items():
            if not (rid in sans_finale and a == "agent_1"):
                meta.append(_ligne(rid, mode, r, "public", "final", final, a))
    return meta


def _donnees(racine, rng, sans_finale=()):
    attendues = {}
    for modele, bande in BANDES.items():
        for etage in ("core", "stego"):
            d = racine / "activations" / modele / etage
            d.mkdir(parents=True)
            meta = _meta(etage, sans_finale if (modele, etage) == ("qwen3_32b", "stego") else ())
            (d / "metadata_gen.json").write_text(json.dumps(meta))
            tab = {}
            for c in bande:
                A = rng.standard_normal((len(meta), LARG))
                A[[i for i, m in enumerate(meta) if m["role"] == "colluder"], 0] += 3.0
                tab[f"layer_{c}"] = A.astype(np.float32)
            np.savez(d / "activations_gen.npz", **tab)
            for nom, sorte in (("activations_gen.npz", "sha256"), ("metadata_gen.json", "git-sha1")):
                p = d / nom
                attendues[f"activations/{modele}/{etage}/{nom}"] = (p.stat().st_size, sorte, C.empreinte(p, sorte))
    return attendues


@pytest.fixture(scope="module")
def donnees(tmp_path_factory):
    racine = tmp_path_factory.mktemp("donnees")
    return racine, _donnees(racine, np.random.default_rng(2))


@pytest.fixture(autouse=True)
def petites_bandes(monkeypatch):
    for modele, bande in BANDES.items():
        monkeypatch.setitem(C.BANDES, modele, bande)
        monkeypatch.setitem(C.LARGEURS, modele, LARG)


# ---------- dépôt jetable ----------

def _git(depot, *args):
    return subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True, text=True).stdout.strip()


def _commit(depot, message):
    _git(depot, "add", "-A")
    _git(depot, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "commit", "-q", "-m", message)
    return _git(depot, "rev-parse", "HEAD")


def _section(augmentation="papier", couches="qwen3_32b=26;llama_3_1_70b=33", forme="AAAAMMJJ-HHMMSS-narc-externe-v2",
             registre=L.REGISTRE, entropie=f"`Entropie : {ENTROPIE}`", en_plus=""):
    lignes = [f"- `augmentation : {augmentation}`", f"- `couches-familles : {couches}`", f"- `run-id : {forme}`",
              f"- `registre : {registre}`"] + ([f"- {entropie}"] if entropie else [])
    return f"## {L.SECTION_CONFIGURATION}\n\n" + "\n".join(lignes) + "\n" + en_plus + "\n"


def _texte(section=None, sans_seuil=False, en_plus=""):
    seuil = "" if sans_seuil else "## Seuil\n\n0,03.\n\n"
    return ("# Texte court factice du bras externe\n\n## Hypothèse\n\nFactice.\n\n## Prédiction chiffrée et signe attendu\n\n"
            "Factice.\n\n## Métrique\n\nAire.\n\n" + seuil + "## Plan d'analyse\n\nFactice ; l'année 2026 et la graine "
            "20261118 figurent dans ce texte.\n\n## Critères de lecture gelés\n\nFactice.\n\n## Liste d'arrêt\n\nFactice.\n\n"
            + (_section() if section is None else section) + en_plus + f"## Contre-lecture\n\nBrouillon relu {H1}, rapport {H2}.\n")


def _lignes(sha_t, sha_f, date_s="2026-01-01T00:00:00Z", date_c="2026-01-02T00:00:00Z", texte="prereg/texte-court.md"):
    return [f"| {L.CLE_SCELLEMENT} | {date_s} | {texte} | {sha_t} |", f"| {L.CLE_CODE} | {date_c} | {FICHE} | {sha_f} |"]


def _depot(tmp, texte=None, lignes=None, fiche=None, avant_code=None, apres=None):
    depot = tmp / "depot"
    shutil.copytree(PAQUET, depot / "src" / "controle_ia", ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"))
    shutil.copy(RACINE_CODE / "requirements-cpu.txt", depot / "requirements-cpu.txt")
    if avant_code:
        avant_code(depot)
    _git(depot, "init", "-q")
    commit = _commit(depot, "code")
    (depot / "prereg").mkdir()
    (depot / "registres" / "code-narc-ext").mkdir(parents=True)
    t = depot / "prereg" / "texte-court.md"
    t.write_text(_texte() if texte is None else texte, encoding="utf-8")
    sha_t = scellement.sceller(t)
    f = depot / FICHE
    contenu = dict(L.fiche_code(depot, commit) if fiche is None else fiche(depot, commit))
    contenu["branche"] = "factice"                                     # clé informative
    f.write_text(json.dumps(contenu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sha_f = scellement.sceller(f)
    (depot / L.REGISTRE).write_text("# Registre du bras externe NARCBench (factice)\n\n| clé | date | chemin | sha256 |\n|---|---|---|---|\n"
                                    + "".join(l + "\n" for l in (lignes or _lignes)(sha_t, sha_f)), encoding="utf-8")
    if apres:
        apres(depot)
    _commit(depot, "texte, fiche, registre")
    return depot


def _args(depot, racine, run_id=RUN, couches="qwen3_32b=26;llama_3_1_70b=33", augmentation="papier", entropie=ENTROPIE,
          texte="prereg/texte-court.md"):
    return ["--depot", str(depot), "--texte", texte, "--donnees", str(racine), "--run-id", run_id, "--entropie", str(entropie),
            "--augmentation", augmentation, "--couches-familles", couches]


def _rien_d_ecrit(depot, sauf=()):
    """Rien d'écrit hors du journal : tout fichier neuf ou changé (runs/, diag/ compris) paraîtrait à `git status`."""
    statut = {l[3:] for l in _git(depot, "status", "--porcelain", "--untracked-files=all").splitlines()}
    assert statut <= {L.JOURNAL, *sauf}, statut


# ---------- de bout en bout ----------

def test_lecture_de_bout_en_bout_puis_jamais_relancee(tmp_path, donnees, capsys):
    racine, att = donnees
    depot = _depot(tmp_path)
    assert L.main(_args(depot, racine), attendues=att) == 0
    res = depot / "diag" / RUN / f"{L.NOM_RESULTAT}.json"
    corps = verifier_resultat(depot, res)                              # résultat scellé et rattaché au manifeste
    r = corps["resultat"]
    assert set(r["modeles"]) == set(C.MODELES) and r["marque"] == "diagnostic, jamais en production (N-026)"
    q = r["modeles"]["qwen3_32b"]
    assert q["garde_reproduction"]["etat"] in ("éprouvée", "non éprouvé")
    assert set(q["garde_reproduction"]["etat_par_etage"]) == {"CORE", "STEGO"} and q["reproduction"]["graines"] == list(range(10))
    assert set(q["nos_familles"]) == {"26"} and set(r["modeles"]["llama_3_1_70b"]["nos_familles"]) == {"33"}
    assert all(f["etat"] == "lu" for f in q["nos_familles"]["26"]["familles"].values())
    assert r["exclusions"]["qwen3_32b/stego"]["exclus"] == 0 and r["controle_du_code"]["fichiers_paquet"] > 100
    m = json.loads((depot / "runs" / RUN / "manifeste.json").read_text(encoding="utf-8"))
    assert m["config"]["augmentation"] == "papier" and m["preenregistrement"]["chemin"] == "prereg/texte-court.md"
    assert m["graines"]["qwen3_32b/familles/c26/lineaire/plancher"]["entropie"] == str(ENTROPIE)   # R9
    assert m["config"]["scikit_learn"] == {"installee": "1.9.1", "fiche": "1.9.1", "temoin_lisible": True}
    assert m["decisif"] is False and m["config"]["registre"]["cles_ignorees"]["nombre"] == 0
    journal = (depot / L.JOURNAL).read_text(encoding="utf-8")
    assert journal.startswith("| OUVERTURE-NARC-EXT |") and RUN in journal
    empreinte = scellement.empreinte(res)
    _commit(depot, "sorties de la lecture")                            # la mère committe ; une relance est refusée
    assert L.main(_args(depot, racine, run_id="20261118-180000-narc-externe-v2"), attendues=att) == 2
    assert "déjà ouverte" in capsys.readouterr().err and scellement.empreinte(res) == empreinte
    assert "REFUS-NARC-EXT" in (depot / L.JOURNAL).read_text(encoding="utf-8")


def test_scikit_learn_d_une_autre_version_temoin_non_lu_chaine_lue(tmp_path, donnees):
    """n° 7 : version de la fiche ≠ version installée → témoin « non lu : garde (scikit-learn) », nos familles lues."""
    racine, att = donnees
    depot = _depot(tmp_path, fiche=lambda d, c: dict(L.fiche_code(d, c), **{"scikit-learn": "1.8.0"}))
    assert L.main(_args(depot, racine), attendues=att) == 0
    r = verifier_resultat(depot, depot / "diag" / RUN / f"{L.NOM_RESULTAT}.json")["resultat"]
    for modele in C.MODELES:
        assert r["modeles"][modele]["reproduction"]["etat"] == X2.GARDE_SKLEARN
        assert r["modeles"][modele]["garde_reproduction"]["etat"] == X2.GARDE_SKLEARN
        fam = next(iter(r["modeles"][modele]["nos_familles"].values()))
        assert all(f["etat"] == "lu" for f in fam["familles"].values())


# ---------- refus de la garde d'ouverture (code 2) et arrêts avant l'ouverture (code 1) ----------

def _avec(*lignes_en_plus, base=_lignes):
    return lambda sha_t, sha_f: base(sha_t, sha_f) + list(lignes_en_plus)


def _ecrire_autre_texte(depot):
    t = depot / "prereg" / "autre.md"
    t.write_text(_texte(), encoding="utf-8")
    return scellement.sceller(t)


def _commit_de_cote(depot, commit):
    arbre = _git(depot, "rev-parse", f"{commit}^{{tree}}")
    cote = _git(depot, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "commit-tree", arbre, "-p", commit,
                "-m", "branche de côté")
    return dict(L.fiche_code(depot, commit), commit=cote)


def _moins_un_fichier(depot, commit):
    f = L.fiche_code(depot, commit)
    f["fichiers"].pop(sorted(f["fichiers"])[0])
    return f


def _empreinte_fausse(depot, commit):
    f = L.fiche_code(depot, commit)
    f["fichiers"][sorted(f["fichiers"])[0]] = "0" * 64
    return f


def _modifier_module(depot):
    p = depot / "src" / "controle_ia" / "narcbench" / "externe_v2.py"
    p.write_text(p.read_text(encoding="utf-8") + "# modifié après la contre-lecture\n", encoding="utf-8")


def _retirer_module(depot):
    (depot / "src" / "controle_ia" / "narcbench" / "jouet_v1.py").unlink()


def _resultat_existant(depot):
    (depot / "diag" / "20261117-090000-autre").mkdir(parents=True)
    (depot / "diag" / "20261117-090000-autre" / f"{L.NOM_RESULTAT}.json").write_text("{}\n")


def _run_existant(depot):
    (depot / "runs" / "20261117-090000-narc-externe-v2").mkdir(parents=True)
    (depot / "runs" / "20261117-090000-narc-externe-v2" / "manifeste.json").write_text("{}\n")


CAS = {
    # n° 3 : registre
    "scellement_absent": (dict(lignes=lambda t, f: _lignes(t, f)[1:]), {}, 2, "0 ligne(s) SCELLEMENT-NARC-EXT"),
    "code_absent": (dict(lignes=lambda t, f: _lignes(t, f)[:1]), {}, 2, "0 ligne(s) CODE-NARC-EXT"),
    "scellement_double": (dict(lignes=lambda t, f: _lignes(t, f)[:1] + _lignes(t, f)), {}, 2, "2 ligne(s) SCELLEMENT"),
    "cinq_cellules": (dict(lignes=lambda t, f: [_lignes(t, f)[0][:-1] + "| en trop |", _lignes(t, f)[1]]), {}, 2,
                      "mal formée (5 cellules"),
    "date_mal_formee": (dict(lignes=lambda t, f: _lignes(t, f, date_s="2026-01-01 00:00:00")), {}, 2, "(AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)"),
    "empreinte_mal_formee": (dict(lignes=lambda t, f: _lignes("abc", f)), {}, 2, "empreinte 'abc'"),
    "chemin_absolu": (dict(lignes=lambda t, f: _lignes(t, f, texte="/prereg/texte-court.md")), {}, 2, "chemin '/prereg"),
    "chemin_remontant": (dict(lignes=lambda t, f: _lignes(t, f, texte="prereg/../prereg/texte-court.md")), {}, 2, "sans « .. »"),
    "posterieure": (dict(lignes=lambda t, f: _lignes(t, f, "2099-01-01T00:00:00Z", "2099-01-02T00:00:00Z")), {}, 2,
                    "pas strictement antérieure"),
    "code_avant_scellement": (dict(lignes=lambda t, f: _lignes(t, f, date_c="2025-12-31T00:00:00Z")), {}, 2,
                              "pas strictement postérieure"),
    "code_au_meme_instant": (dict(lignes=lambda t, f: _lignes(t, f, date_c="2026-01-01T00:00:00Z")), {}, 2,
                             "pas strictement postérieure"),
    "sceau_faux": (dict(apres=lambda d: (d / "prereg" / "texte-court.md").write_text(_texte(en_plus="Ajout.\n\n"),
                                                                                   encoding="utf-8")), {}, 2, "≠ empreinte du fichier"),
    "cite_un_autre_texte": (dict(lignes=lambda t, f: _lignes(t, f, texte="prereg/autre.md"), apres=_ecrire_autre_texte), {}, 2,
                            "cite prereg/autre.md, pas le texte donné"),
    "lecture_deja_inscrite": (dict(lignes=_avec(f"| {L.CLE_LECTURE} | 2026-01-03T00:00:00Z | diag/x.json | {H1} |")), {}, 2,
                              "lecture déjà jouée"),
    "cle_du_bras_inconnue": (dict(lignes=_avec(f"| VERDICT-NARC-EXT | 2026-01-03T00:00:00Z | x.md | {H1} |")), {}, 2,
                             "aux segments NARC-EXT inconnue"),
    "premiere_cellule_hors_forme": (dict(lignes=_avec(f"| pas une clé | 2026-01-03T00:00:00Z | x.md | {H1} |")), {}, 2,
                                    "la forme d'une clé"),
    "registre_absent": (dict(apres=lambda d: (d / L.REGISTRE).unlink()), {}, 2, "absent du dépôt"),
    "texte_non_conforme": (dict(texte=_texte(sans_seuil=True)), {}, 2, "non conforme"),
    "texte_absolu": ({}, dict(texte="/prereg/texte-court.md"), 2, "chemin relatif"),
    # configuration canonique du texte scellé
    "section_absente": (dict(texte=_texte(section="")), {}, 2, "0 section(s)"),
    "section_double": (dict(texte=_texte(section=_section() + _section())), {}, 2, "2 section(s)"),
    "cle_inconnue": (dict(texte=_texte(section=_section(en_plus="- `donnees : /ailleurs`\n"))), {}, 2, "clé 'donnees' inconnue"),
    "cle_double": (dict(texte=_texte(section=_section(en_plus="- `augmentation : papier`\n"))), {}, 2, "en double"),
    "prose_dans_la_section": (dict(texte=_texte(section=_section(en_plus="Le code refuse tout écart.\n"))), {}, 2,
                              "« clé : valeur » attendue"),
    "registre_autre": (dict(texte=_texte(section=_section(registre="registres/scellements-v1.md"))), {}, 2,
                       "≠ registre fixé"),
    "forme_du_run_mal_formee": (dict(texte=_texte(section=_section(forme="20261118-narc"))), {}, 2,
                                "forme de l'identifiant du run"),
    "augmentation_du_texte_inconnue": (dict(texte=_texte(section=_section(augmentation="aucune"))), {}, 2,
                                       "augmentation 'aucune'"),
    "entropie_absente": (dict(texte=_texte(section=_section(entropie=""))), {}, 2, "0 ligne(s) exacte(s)"),
    "entropie_double": (dict(texte=_texte(section=_section(en_plus=f"- Entropie : {ENTROPIE + 1}\n"))), {}, 2,
                        "2 ligne(s) exacte(s)"),
    "entropie_petite": (dict(texte=_texte(section=_section(entropie="`Entropie : 2026`"))), {}, 2, "< 2³²"),
    "entropie_hors_ligne_exacte": (dict(texte=_texte(section=_section(entropie=f"`Entropie : {ENTROPIE} (tirée une fois)`"))),
                                   {}, 2, "0 ligne(s) exacte(s)"),
    "entropie_sous_chaine": ({}, dict(entropie=20261118), 2, "entropie de la commande ≠"),
    "augmentation_differente": ({}, dict(augmentation="code"), 2, "augmentation 'code' ≠"),
    "couches_differentes": ({}, dict(couches="bande"), 2, "couches de nos familles 'bande' ≠"),
    "couches_mal_formees": ({}, dict(couches="qwen3_32b=27+26;llama_3_1_70b=33"), 2, "croissantes"),
    "run_hors_forme": ({}, dict(run_id="20261118-170000-narc-autre"), 2, "hors de la forme"),
    "run_date_impossible": ({}, dict(run_id="20261399-250000-narc-externe-v2"), 2, "date ou heure impossible"),
    # déjà ouverte
    "run_deja_ouvert": (dict(apres=_run_existant), {}, 2, "déjà ouverte"),
    "resultat_deja_ecrit": (dict(apres=_resultat_existant), {}, 2, "déjà ouverte"),
    # n° 4 : code
    "fiche_mal_formee": (dict(fiche=lambda d, c: dict(L.fiche_code(d, c), commit="xyz")), {}, 1, "fiche du code : commit"),
    "commit_absent": (dict(fiche=lambda d, c: dict(L.fiche_code(d, c), commit="0" * 40)), {}, 1, "absent du dépôt"),
    "commit_non_ancetre": (dict(fiche=_commit_de_cote), {}, 1, "ni HEAD ni un de ses ancêtres"),
    "fiche_liste_fausse": (dict(fiche=_moins_un_fichier), {}, 1, "≠ liste de la fiche"),
    "fiche_empreinte_fausse": (dict(fiche=_empreinte_fausse), {}, 1, "empreinte au commit ≠ empreinte de la fiche"),
    "code_execute_different": (dict(avant_code=_modifier_module), {}, 1, "différent(s) du commit"),
    "paquet_execute_en_plus": (dict(avant_code=_retirer_module), {}, 1, "paquet exécuté ≠"),
}


@pytest.mark.parametrize("cas", sorted(CAS))
def test_refus_et_arrets_avant_ouverture_rien_d_ecrit(tmp_path, donnees, capsys, cas):
    racine, att = donnees
    kw_depot, kw_args, code, motif = CAS[cas]
    depot = _depot(tmp_path, **kw_depot)
    assert L.main(_args(depot, racine, **kw_args), attendues=att) == code
    err = capsys.readouterr().err
    assert motif in err, err
    _rien_d_ecrit(depot)
    assert (depot / L.JOURNAL).read_text(encoding="utf-8").startswith("| REFUS-NARC-EXT |") if (depot / "registres").is_dir() \
        else True


def test_arbre_de_travail_modifie_arrete(tmp_path, donnees, capsys):
    """n° 4 : un fichier non commité (ici un registre de fortune ne changerait rien : le registre est fixé)."""
    racine, att = donnees
    depot = _depot(tmp_path)
    (depot / "notes.txt").write_text("brouillon\n")
    assert L.main(_args(depot, racine), attendues=att) == 1
    assert "arbre de travail modifié" in capsys.readouterr().err
    _rien_d_ecrit(depot, sauf=("notes.txt",))


def test_registre_hors_du_depot_impossible(tmp_path, donnees):
    """M3 (a) : `--registre` n'existe plus ; le registre est celui du dépôt, au chemin fixé."""
    racine, _ = donnees
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(_args(tmp_path, racine) + ["--registre", "/ailleurs/registre.md"])
    assert L.REGISTRE == "registres/narcbench-externe-v1.md"


@pytest.mark.parametrize("artefact", ["empreinte", "transfert", "exclusions"])
def test_donnees_arretent_avant_l_ouverture(tmp_path, capsys, artefact):
    """n° 1 (taille ou empreinte), n° 2 (étage de transfert présent), n° 6 (plus de 10 % d'épisodes exclus) : code 1, rien
    d'écrit hors du journal."""
    racine = tmp_path / "donnees"
    att = _donnees(racine, np.random.default_rng(3),
                   sans_finale=("bj__shoe00__control", "bj__shoe01__control") if artefact == "exclusions" else ())
    if artefact == "empreinte":
        rel = "activations/qwen3_32b/core/activations_gen.npz"
        att[rel] = (att[rel][0], "sha256", "0" * 64)
    if artefact == "transfert":
        (racine / "activations" / "qwen3_32b" / "transfer").mkdir()
        (racine / "activations" / "qwen3_32b" / "transfer" / "metadata_gen.json").write_text("[]")
    depot = _depot(tmp_path)
    assert L.main(_args(depot, racine), attendues=att) == 1
    err = capsys.readouterr().err
    assert {"empreinte": "activations_gen.npz", "transfert": "étage de transfert", "exclusions": "plus de 10 %"}[artefact] in err
    _rien_d_ecrit(depot)


def test_valeur_non_finie_arrete_apres_ouverture_sans_resultat(tmp_path, donnees, capsys, monkeypatch):
    """m4 : une valeur non finie dans le résultat → arrêt après l'ouverture (code 1, ligne ARRET-NARC-EXT), aucun résultat écrit."""
    racine, att = donnees
    depot = _depot(tmp_path)
    vraie = X2.garde_reproduction_v2
    monkeypatch.setattr(X2, "garde_reproduction_v2", lambda modele, r: dict(vraie(modele, r), ecart_factice=float("nan")))
    assert L.main(_args(depot, racine), attendues=att) == 1
    assert "valeur(s) non finie(s)" in capsys.readouterr().err
    assert (depot / "runs" / RUN / "manifeste.json").is_file() and not (depot / "diag").exists()
    journal = (depot / L.JOURNAL).read_text(encoding="utf-8").splitlines()
    assert [l.split(" | ")[0] for l in journal] == ["| OUVERTURE-NARC-EXT", "| ARRET-NARC-EXT"]


# ---------- pièces de la garde ----------

def test_lire_fiche_code_formes_fautives(tmp_path):
    bonne = {"commit": "c" * 40, "fichiers": {"src/controle_ia/narcbench/a.py": H1}, "scikit-learn": "1.9.1", "branche": "x"}
    p = tmp_path / "fiche.json"
    p.write_text(json.dumps(bonne), encoding="utf-8")
    assert L.lire_fiche_code(p)["cles_informatives"] == ["branche"]   # cas sain
    for faux in ([], dict(bonne, fichiers={}), dict(bonne, fichiers={"src/controle_ia/t07/a.py": H1}),
                 dict(bonne, fichiers={"src/controle_ia/narcbench/a.py": "abc"}),
                 dict(bonne, fichiers={"src/controle_ia/narcbench/../t07/a.py": H1}), {k: v for k, v in bonne.items()
                                                                                       if k != "scikit-learn"}):
        p.write_text(json.dumps(faux), encoding="utf-8")
        with pytest.raises(GardeArret, match="fiche du code"):
            L.lire_fiche_code(p)
    p.write_text("{pas du JSON", encoding="utf-8")
    with pytest.raises(GardeArret, match="illisible"):
        L.lire_fiche_code(p)


def test_fiche_code_exige_scikit_learn_epingle(tmp_path):
    depot = tmp_path / "petit"
    (depot / "src" / "controle_ia" / "narcbench").mkdir(parents=True)
    (depot / "src" / "controle_ia" / "narcbench" / "a.py").write_text("x = 1\n")
    (depot / "requirements-cpu.txt").write_text("numpy==2.4.6\n")
    _git(depot, "init", "-q")
    commit = _commit(depot, "petit")
    with pytest.raises(GardeArret, match="non épinglé"):
        L.fiche_code(depot, commit)
    (depot / "requirements-cpu.txt").write_text("numpy==2.4.6\nscikit-learn==1.9.1  # recette\n")
    commit = _commit(depot, "épinglé")
    assert L.fiche_code(depot, commit) == {"commit": commit, "scikit-learn": "1.9.1", "fichiers": {
        "src/controle_ia/narcbench/a.py": scellement.empreinte(depot / "src" / "controle_ia" / "narcbench" / "a.py")}}

def test_lire_registre_externe_ignore_et_compte_les_autres_cles(tmp_path):
    reg = tmp_path / "registre.md"
    reg.write_text(f"# titre\n\n| {L.CLE_SCELLEMENT} | 2026-01-01T00:00:00Z | t.md | {H1} |\n"
                   f"| {L.CLE_CODE} | 2026-01-02T00:00:00Z | f.json | {H2} |\n| SCELLEMENT-T07 | 2026-01-03T00:00:00Z | x | {H1} |\n"
                   "texte libre | sans date\n", encoding="utf-8")
    lu = L.lire_registre_externe(reg)
    assert lu["ignorees"] == ["SCELLEMENT-T07"] and set(lu["lignes"]) == {L.CLE_SCELLEMENT, L.CLE_CODE}
    assert L.est_cle_du_bras("VERDICT-NARC-EXT") and not L.est_cle_du_bras("SCELLEMENT-NARC-8B")


def test_depot_qui_n_est_pas_la_racine_arrete(tmp_path):
    depot = _depot(tmp_path)
    fiche = L.lire_fiche_code(depot / FICHE)
    L.exiger_code_de_la_fiche(depot, fiche)                            # cas sain
    with pytest.raises(GardeArret, match="pas la racine"):
        L.exiger_code_de_la_fiche(depot / "src", fiche)


def test_controles_prealables(tmp_path, capsys):
    depot = _depot(tmp_path)
    assert L.main(["verifier-texte", str(depot / "prereg" / "texte-court.md")]) == 0
    sortie = json.loads(capsys.readouterr().out)
    assert sortie["entropie"] == ENTROPIE and sortie["couches_familles"] == {"qwen3_32b": [26], "llama_3_1_70b": [33]}
    faux = tmp_path / "faux.md"
    faux.write_text(_texte(section=_section(entropie="")), encoding="utf-8")
    assert L.main(["verifier-texte", str(faux)]) == 2
    commit = _git(depot, "rev-list", "--max-parents=0", "HEAD")
    assert L.main(["fiche-code", "--depot", str(depot), "--commit", commit]) == 0
    fiche = json.loads(capsys.readouterr().out)
    assert fiche["scikit-learn"] == "1.9.1" and "src/controle_ia/narcbench/lecture_externe_v2.py" in fiche["fichiers"]
    assert L.main(["fiche-code", "--depot", str(depot), "--commit", "xyz"]) == 1
    assert L.main(["verifier-texte"]) == 2


def test_valeurs_non_finies_et_couches():
    assert L.valeurs_non_finies({"a": [1.0, {"b": float("nan")}], "c": None, "d": float("inf")}) == ["resultat/a[1]/b",
                                                                                                     "resultat/d"]
    assert L.valeurs_non_finies({"a": 1.0, "b": None, "c": "x"}) == []
    assert L.couches_familles("bande") == BANDES
    assert L.couches_familles("qwen3_32b=26;llama_3_1_70b=32+33") == {"qwen3_32b": (26,), "llama_3_1_70b": (32, 33)}
    for faux in ("qwen3_32b=26", "qwen3_32b=99;llama_3_1_70b=32", "qwen3_32b=26+26;llama_3_1_70b=32",
                 "gpt_oss_20b=10;qwen3_32b=26", "qwen3_32b=;llama_3_1_70b=32", "qwen3_32b=26;qwen3_32b=27",
                 "qwen3_32b=a;llama_3_1_70b=32"):
        with pytest.raises(RefusRegistre):
            L.couches_familles(faux)
    assert len(L.taches_graines({"qwen3_32b": (26,), "llama_3_1_70b": (32, 33)})) == 3 * 3 * 4


def test_arguments_exiges(tmp_path):
    base = _args(tmp_path, tmp_path)
    sans_aug = [x for i, x in enumerate(base) if x != "--augmentation" and (i == 0 or base[i - 1] != "--augmentation")]
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(sans_aug)                             # E2 : aucun défaut
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(_args(tmp_path, tmp_path, augmentation="aucune"))
    assert L.analyseur().parse_args(base).augmentation == "papier"
