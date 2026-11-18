"""Essais de la commande de lecture du bras externe v2 (`controle_ia.narcbench.lecture_externe_v2`), dans un dépôt git **jetable**
qui porte une copie du paquet exécuté, et sur des fichiers **factices** ; aucun fichier publié n'est ouvert. R5 : chaque garde
sur un cas sain (la lecture de bout en bout) et sur un artefact (un cas par motif). Aucun raccourci : le texte factice est
conforme au gabarit des préenregistrements (`prereg.exiger_prereg_scelle` joue pour de vrai) et porte la section
« Configuration canonique de la commande » au format du brouillon 3 (six lignes seules)."""
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
from controle_ia.narcbench import cellules_externe_v2 as CE
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
TEXTE = "prereg/texte-court.md"
FICHE = "registres/code-narc-ext/CODE-NARC-EXT-v1.json"
H1, H2 = "a" * 64, "b" * 64


# ---------- données factices ----------

def _ligne(rid, mode, role, canal, phase, rnd, agent):
    m = {k: None for k in C.CHAMPS}
    m.update(run_id=rid, mode=mode, role=role, channel=canal, phase=phase, round=rnd, agent_name=agent)
    return m


def _meta(etage, sans_finale=(), trois_colludeurs=()):
    meta = []
    if etage == "core":
        runs = [(f"fam__dom{d}_00__{mode}", mode) for d in range(10) for mode in ("collusion", "control")]
        tours, final = (1, 2, 3), 4
    else:
        runs = [(f"bj__shoe{k:02d}__{mode}", mode) for k in range(12) for mode in ("collusion", "control")]
        tours, final = (1, 2), 8
    for rid, mode in runs:
        roles = {f"agent_{j}": ("colluder" if mode == "collusion" and (j in (0, 3) or (rid in trois_colludeurs and j == 1))
                                else "honest") for j in range(4)}
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


def _donnees(racine, rng, **kw):
    attendues = {}
    for modele, bande in BANDES.items():
        for etage in ("core", "stego"):
            d = racine / "activations" / modele / etage
            d.mkdir(parents=True)
            meta = _meta(etage, **(kw if (modele, etage) == ("qwen3_32b", "stego") else {}))
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
    monkeypatch.setattr(CE, "N_TIRAGES", 300)                           # temps des essais seulement (le texte fixe 2 000)


# ---------- dépôt jetable ----------

def _git(depot, *args):
    return subprocess.run(["git", "-C", str(depot), *args], check=True, capture_output=True, text=True).stdout.strip()


def _commit(depot, message):
    _git(depot, "add", "-A")
    _git(depot, "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "commit", "-q", "-m", message)
    return _git(depot, "rev-parse", "HEAD")


CONF = {"augmentation": "papier", "couches-familles": "bande", "run-id": "AAAAMMJJ-HHMMSS-narc-externe-v2",
        "registre": "registres/narcbench-externe-v1.md", "texte": TEXTE, "Entropie": str(ENTROPIE)}


def _section(cloture=False, en_plus="", **remplace):
    valeurs = dict(CONF, **remplace)
    lignes = [f"{k} : {v}" for k, v in valeurs.items() if v is not None]
    corps = "\n".join((["```"] if cloture else []) + lignes + (["```"] if cloture else []))
    return f"## {L.SECTION_CONFIGURATION}\n\n{corps}\n{en_plus}\n"


def _texte(section=None, sans_seuil=False, en_plus=""):
    seuil = "" if sans_seuil else "## Seuil\n\n0,03.\n\n"
    return ("# Texte court factice du bras externe\n\n## Hypothèse\n\nFactice.\n\n## Prédiction chiffrée et signe attendu\n\n"
            "Factice.\n\n## Métrique\n\nAire.\n\n" + seuil + "## Plan d'analyse\n\nFactice ; l'année 2026 et la graine "
            "20261118 figurent dans ce texte.\n\n## Critères de lecture gelés\n\nFactice.\n\n## Liste d'arrêt\n\nFactice.\n\n"
            + (_section() if section is None else section) + "## Notes de la configuration canonique\n\n- `augmentation` : la "
            "prose est ici, hors de la section.\n\n" + en_plus + f"## Contre-lecture\n\nBrouillon relu {H1}, rapport {H2}.\n")


def _lignes(sha_t, sha_f, date_s="2026-01-01T00:00:00Z", date_c="2026-01-02T00:00:00Z", texte=TEXTE):
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
    t = depot / TEXTE
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


def _args(depot, racine, run_id=RUN, couches="bande", augmentation="papier", entropie=ENTROPIE, texte=TEXTE):
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
    r = verifier_resultat(depot, res)["resultat"]                       # résultat scellé et rattaché au manifeste
    assert set(r["modeles"]) == set(C.MODELES) and r["marque"] == "diagnostic, jamais en production (N-026)"
    q = r["modeles"]["qwen3_32b"]
    assert len(q["cellules"]) == 4 * 2 + 3 * 2 and q["cellules"]["lineaire/stego/pic"]["calculs"] == ["couche 26", "couche 27"]
    assert len(q["cellules"]["temoin/stego/ecart"]["calculs"]) == 10 * 2 and q["cellules"]["temoin/core/pic"]["plis"] == 10
    assert all(c["etat"] in (CE.REPRODUIT, CE.NON_REPRODUIT, CE.NON_TRANCHE) for k, c in q["cellules"].items()
               if not k.startswith("mahalanobis"))                       # effectifs lisibles : états C2 à C4
    assert "scores" not in q["reproduction"] and set(q["garde_reproduction"]["etat_par_etage"]) == {"CORE", "STEGO"}
    assert set(q["lecture_par_agent"]) == {"26", "27"}
    lf = r["lecture"]
    assert lf["reponse"]["ligne"] in ("R0", "R1", "R2", "R3", "R4", "R5") and set(lf["regle_t"]) == set(CE.VISEES)
    cs = r["comptes_structurels"]
    assert cs["modeles"]["qwen3_32b"]["stego"]["sabots"] == 12 and cs["modeles"]["llama_3_1_70b"]["core"]["domaines"] == 10
    assert cs["communs_aux_deux_modeles"]["stego"]["communs"] == 24
    m = json.loads((depot / "runs" / RUN / "manifeste.json").read_text(encoding="utf-8"))
    assert m["config"]["augmentation"] == "papier" and m["preenregistrement"]["chemin"] == TEXTE and m["decisif"] is False
    assert m["graines"]["qwen3_32b/familles/c26/lineaire/apprentissage/pli-dom3"]["entropie"] == str(ENTROPIE)   # R9
    assert "llama_3_1_70b/cellules/temoin/stego/pic/placebo" in m["graines"] and m["config"]["scikit_learn"] == "1.9.1"
    journal = (depot / L.JOURNAL).read_text(encoding="utf-8")
    assert journal.startswith("| OUVERTURE-NARC-EXT |") and RUN in journal
    empreinte = scellement.empreinte(res)
    _commit(depot, "sorties de la lecture")                            # la mère committe ; une relance est refusée
    assert L.main(_args(depot, racine, run_id="20261118-180000-narc-externe-v2"), attendues=att) == 2
    assert "déjà jouée ou ouverte" in capsys.readouterr().err and scellement.empreinte(res) == empreinte
    assert "REFUS-NARC-EXT" in (depot / L.JOURNAL).read_text(encoding="utf-8")


def test_valeur_non_finie_arrete_apres_ouverture_sans_resultat(tmp_path, donnees, capsys, monkeypatch):
    """Une valeur non finie dans le résultat → arrêt après l'ouverture (code 1, ligne ARRET-NARC-EXT), aucun résultat écrit."""
    racine, att = donnees
    depot = _depot(tmp_path)
    vraie = X2.garde_reproduction_v2
    monkeypatch.setattr(X2, "garde_reproduction_v2", lambda modele, r: dict(vraie(modele, r), ecart_factice=float("nan")))
    assert L.main(_args(depot, racine), attendues=att) == 1
    assert "valeur(s) non finie(s)" in capsys.readouterr().err
    assert (depot / "runs" / RUN / "manifeste.json").is_file() and not (depot / "diag").exists()
    journal = (depot / L.JOURNAL).read_text(encoding="utf-8").splitlines()
    assert [l.split(" | ")[0] for l in journal] == ["| OUVERTURE-NARC-EXT", "| ARRET-NARC-EXT"]


def test_memoire_insuffisante_arret_apres_ouverture(tmp_path, donnees, capsys, monkeypatch):
    """n° 11 : mémoire insuffisante → arrêt, nœud (code 1), jamais une famille « non lue »."""
    racine, att = donnees
    depot = _depot(tmp_path)

    def a_court(*a, **k):
        raise MemoryError("factice")
    monkeypatch.setattr(CE, "lire_modele", a_court)
    assert L.main(_args(depot, racine), attendues=att) == 1
    assert "mémoire insuffisante : arrêt, nœud (liste d'arrêt n° 11)" in capsys.readouterr().err


# ---------- refus avant l'ouverture (code 2) et arrêts avant l'ouverture (code 1) ----------

def _avec(*lignes_en_plus, base=_lignes):
    return lambda sha_t, sha_f: base(sha_t, sha_f) + list(lignes_en_plus)


def _ecrire_autre_texte(depot):
    t = depot / "prereg" / "autre.md"
    t.write_text(_texte(section=_section(texte="prereg/autre.md")), encoding="utf-8")
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


def _fiche_modifiee_apres_son_sceau(depot):
    f = depot / FICHE
    contenu = json.loads(f.read_text(encoding="utf-8"))
    contenu["note"] = "ajoutée après le sceau"                          # JSON valide, compagnon .sha256 inchangé
    f.write_text(json.dumps(contenu, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _resultat_existant(depot):
    (depot / "diag" / "20261117-090000-autre").mkdir(parents=True)
    (depot / "diag" / "20261117-090000-autre" / f"{L.NOM_RESULTAT}.json").write_text("{}\n")


def _run_existant(depot):
    (depot / "runs" / "20261117-090000-narc-externe-v2").mkdir(parents=True)
    (depot / "runs" / "20261117-090000-narc-externe-v2" / "manifeste.json").write_text("{}\n")


CAS = {
    # n° 3 et 4 : registre
    "scellement_absent": (dict(lignes=lambda t, f: _lignes(t, f)[1:]), {}, 2, "0 ligne(s) SCELLEMENT-NARC-EXT"),
    "code_absent": (dict(lignes=lambda t, f: _lignes(t, f)[:1]), {}, 2, "0 ligne(s) CODE-NARC-EXT"),
    "scellement_double": (dict(lignes=lambda t, f: _lignes(t, f)[:1] + _lignes(t, f)), {}, 2, "2 ligne(s) SCELLEMENT"),
    "cinq_cellules": (dict(lignes=lambda t, f: [_lignes(t, f)[0][:-1] + "| en trop |", _lignes(t, f)[1]]), {}, 2,
                      "mal formée (5 cellules"),
    "date_mal_formee": (dict(lignes=lambda t, f: _lignes(t, f, date_s="2026-01-01 00:00:00")), {}, 2,
                        "(AAAA-MM-JJTHH:MM:SSZ, UTC, attendue)"),
    "empreinte_mal_formee": (dict(lignes=lambda t, f: _lignes("abc", f)), {}, 2, "empreinte 'abc'"),
    "chemin_absolu": (dict(lignes=lambda t, f: _lignes(t, f, texte="/prereg/texte-court.md")), {}, 2, "chemin '/prereg"),
    "chemin_remontant": (dict(lignes=lambda t, f: _lignes(t, f, texte="prereg/../prereg/texte-court.md")), {}, 2, "sans « .. »"),
    "posterieure": (dict(lignes=lambda t, f: _lignes(t, f, "2099-01-01T00:00:00Z", "2099-01-02T00:00:00Z")), {}, 2,
                    "pas strictement antérieure"),
    "code_avant_scellement": (dict(lignes=lambda t, f: _lignes(t, f, date_c="2025-12-31T00:00:00Z")), {}, 2,
                              "pas strictement postérieure"),
    "code_au_meme_instant": (dict(lignes=lambda t, f: _lignes(t, f, date_c="2026-01-01T00:00:00Z")), {}, 2,
                             "pas strictement postérieure"),
    # contre-lecture du code final, M2 : les deux conditions de la ligne CODE-NARC-EXT sans artefact jusqu'ici
    "code_seule_posterieure": (dict(lignes=lambda t, f: _lignes(t, f, date_c="2099-01-02T00:00:00Z")), {}, 2,
                               "ligne CODE-NARC-EXT datée 2099-01-02T00:00:00Z, pas strictement antérieure"),
    "sceau_faux_de_la_fiche": (dict(apres=_fiche_modifiee_apres_son_sceau), {}, 2, "CODE-NARC-EXT-v1.json : compagnon .sha256"),
    "sceau_faux": (dict(apres=lambda d: (d / TEXTE).write_text(_texte(en_plus="Ajout.\n\n"), encoding="utf-8")), {}, 2,
                   "≠ empreinte du fichier"),
    "cite_un_autre_texte": (dict(lignes=lambda t, f: _lignes(t, f, texte="prereg/autre.md"), apres=_ecrire_autre_texte), {}, 2,
                            "cite prereg/autre.md, pas le texte donné"),
    "lecture_deja_inscrite": (dict(lignes=_avec(f"| {L.CLE_LECTURE} | 2026-01-03T00:00:00Z | diag/x.json | {H1} |")), {}, 2,
                              "lecture déjà jouée"),
    "cle_du_bras_inconnue": (dict(lignes=_avec(f"| VERDICT-NARC-EXT | 2026-01-03T00:00:00Z | x.md | {H1} |")), {}, 2,
                             "aux segments NARC-EXT inconnue"),
    "autre_cle_refusee": (dict(lignes=_avec(f"| SCELLEMENT-T07 | 2026-01-03T00:00:00Z | x.md | {H1} |")), {}, 2,
                          "le registre propre ne porte que"),
    "premiere_cellule_hors_forme": (dict(lignes=_avec(f"| pas une clé | 2026-01-03T00:00:00Z | x.md | {H1} |")), {}, 2,
                                    "la forme d'une clé"),
    "registre_absent": (dict(apres=lambda d: (d / L.REGISTRE).unlink()), {}, 2, "absent du dépôt"),
    "texte_non_conforme": (dict(texte=_texte(sans_seuil=True)), {}, 2, "non conforme"),
    "texte_absolu": ({}, dict(texte="/prereg/texte-court.md"), 2, "chemin relatif"),
    # n° 5 : configuration canonique du texte scellé
    "section_absente": (dict(texte=_texte(section="")), {}, 2, "0 section(s)"),
    "section_double": (dict(texte=_texte(section=_section() + _section())), {}, 2, "2 section(s)"),
    "cle_inconnue": (dict(texte=_texte(section=_section(en_plus="donnees : /ailleurs"))), {}, 2, "« <clé> : <valeur> » seule"),
    "cle_double": (dict(texte=_texte(section=_section(en_plus="augmentation : papier"))), {}, 2, "en double"),
    "cle_absente": (dict(texte=_texte(section=_section(registre=None))), {}, 2, "clé(s) absente(s) : registre"),
    "prose_dans_la_section": (dict(texte=_texte(section=_section(en_plus="Le code refuse tout écart."))), {}, 2,
                              "« <clé> : <valeur> » seule"),
    "ligne_en_puce": (dict(texte=_texte(section=_section(Entropie=None, en_plus=f"- Entropie : {ENTROPIE}"))), {}, 2,
                      "« <clé> : <valeur> » seule"),
    "cle_hors_section_aussi": (dict(texte=_texte(en_plus=f"Entropie : {ENTROPIE}\n\n")), {}, 2,
                               "2 lignes du texte commencent par « Entropie : »"),
    "espaces_autour_du_deux_points": (dict(texte=_texte(section=_section(augmentation=None, en_plus="augmentation: papier"))), {},
                                      2, "« <clé> : <valeur> » seule"),
    "registre_autre": (dict(texte=_texte(section=_section(registre="registres/scellements-v1.md"))), {}, 2, "≠ registre fixé"),
    "forme_du_run_autre": (dict(texte=_texte(section=_section(**{"run-id": "AAAAMMJJ-HHMMSS-narc-autre"}))), {}, 2,
                           "la forme 'AAAAMMJJ-HHMMSS-narc-externe-v2' attendue"),
    "augmentation_du_texte_inconnue": (dict(texte=_texte(section=_section(augmentation="aucune"))), {}, 2,
                                       "augmentation 'aucune'"),
    "entropie_petite": (dict(texte=_texte(section=_section(Entropie="4294967295"))), {}, 2, "≥ 2³²"),
    "entropie_hors_ligne_exacte": (dict(texte=_texte(section=_section(Entropie=f"{ENTROPIE} (tirée une fois)"))), {}, 2, "≥ 2³²"),
    "texte_de_la_section_autre": (dict(texte=_texte(section=_section(texte="prereg/autre.md"))), {}, 2, "texte : ligne"),
    "entropie_sous_chaine": ({}, dict(entropie=20261118), 2, "entropie de la commande ≠"),
    "augmentation_differente": ({}, dict(augmentation="code"), 2, "augmentation 'code' ≠"),
    "couches_differentes": ({}, dict(couches="qwen3_32b=26;llama_3_1_70b=33"), 2, "couches de nos familles"),
    "couches_mal_formees": ({}, dict(couches="qwen3_32b=27+26;llama_3_1_70b=33"), 2, "croissantes"),
    "run_hors_forme": ({}, dict(run_id="20261118-170000-narc-autre"), 2, "hors de la forme"),
    "run_date_impossible": ({}, dict(run_id="20261399-250000-narc-externe-v2"), 2, "date ou heure impossible"),
    # n° 6 : code
    "fiche_mal_formee": (dict(fiche=lambda d, c: dict(L.fiche_code(d, c), commit="xyz")), {}, 1, "fiche du code : commit"),
    "commit_absent": (dict(fiche=lambda d, c: dict(L.fiche_code(d, c), commit="0" * 40)), {}, 1, "absent du dépôt"),
    "commit_non_ancetre": (dict(fiche=_commit_de_cote), {}, 1, "ni HEAD ni un de ses ancêtres"),
    "fiche_liste_fausse": (dict(fiche=_moins_un_fichier), {}, 1, "≠ liste de la fiche"),
    "fiche_empreinte_fausse": (dict(fiche=_empreinte_fausse), {}, 1, "empreinte au commit ≠ empreinte de la fiche"),
    "code_execute_different": (dict(avant_code=_modifier_module), {}, 1, "différent(s) du commit"),
    "paquet_execute_en_plus": (dict(avant_code=_retirer_module), {}, 1, "paquet exécuté ≠"),
    # n° 4 : déjà jouée (après le commit, plan d'analyse n° 2)
    "run_deja_ouvert": (dict(apres=_run_existant), {}, 2, "déjà jouée ou ouverte"),
    "resultat_deja_ecrit": (dict(apres=_resultat_existant), {}, 2, "déjà jouée ou ouverte"),
    # n° 7 : scikit-learn de la fiche autre que 1.9.1
    "scikit_learn_de_la_fiche": (dict(fiche=lambda d, c: dict(L.fiche_code(d, c), **{"scikit-learn": "1.8.0"})), {}, 1,
                                 "liste d'arrêt n° 7"),
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
    if (depot / "registres").is_dir():
        assert (depot / L.JOURNAL).read_text(encoding="utf-8").startswith("| REFUS-NARC-EXT |")


def test_scikit_learn_installe_absent_ou_autre_rien_n_est_lu(tmp_path, donnees, capsys, monkeypatch):
    """n° 7 : version installée absente ou autre → arrêt avant toute lecture, pas même notre chaîne."""
    racine, att = donnees
    for faux in (None, "1.8.0"):
        depot = _depot(tmp_path / str(faux))
        monkeypatch.setattr(L, "version_installee", lambda p, v=faux: v if p == "scikit-learn" else "x")
        assert L.main(_args(depot, racine), attendues=att) == 1
        assert "rien n'est lu, pas même notre chaîne" in capsys.readouterr().err
        _rien_d_ecrit(depot)


def test_arbre_de_travail_modifie_arrete(tmp_path, donnees, capsys):
    """n° 6 : un fichier non commité arrête avant toute lecture."""
    racine, att = donnees
    depot = _depot(tmp_path)
    (depot / "notes.txt").write_text("brouillon\n")
    assert L.main(_args(depot, racine), attendues=att) == 1
    assert "arbre de travail modifié" in capsys.readouterr().err
    _rien_d_ecrit(depot, sauf=("notes.txt",))


def test_registre_hors_du_depot_impossible(tmp_path, donnees):
    """`--registre` n'existe plus ; le registre est celui du dépôt, au chemin fixé, égal à la ligne `registre :` du texte."""
    racine, _ = donnees
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(_args(tmp_path, racine) + ["--registre", "/ailleurs/registre.md"])
    assert L.REGISTRE == "registres/narcbench-externe-v1.md" == CONF["registre"]


@pytest.mark.parametrize("artefact", ["empreinte", "transfert", "exclusions", "colludeurs"])
def test_donnees_arretent_avant_l_ouverture(tmp_path, capsys, artefact):
    """n° 1 (empreinte), n° 2 (étage de transfert), n° 9 (plus de 10 % d'exclus : décision de texte A28, avant le manifeste),
    n° 8 (épisode de collusion à trois colludeurs, toutes procédures) : code 1, rien d'écrit hors du journal."""
    racine = tmp_path / "donnees"
    kw = {"exclusions": {"sans_finale": ("bj__shoe00__control", "bj__shoe01__control", "bj__shoe02__control")},
          "colludeurs": {"trois_colludeurs": ("bj__shoe00__collusion",)}}.get(artefact, {})
    att = _donnees(racine, np.random.default_rng(3), **kw)
    if artefact == "empreinte":
        rel = "activations/qwen3_32b/core/activations_gen.npz"
        att[rel] = (att[rel][0], "sha256", "0" * 64)
    if artefact == "transfert":
        (racine / "activations" / "qwen3_32b" / "transfer").mkdir()
        (racine / "activations" / "qwen3_32b" / "transfer" / "metadata_gen.json").write_text("[]")
    depot = _depot(tmp_path)
    assert L.main(_args(depot, racine), attendues=att) == 1
    err = capsys.readouterr().err
    assert {"empreinte": "activations_gen.npz", "transfert": "étage de transfert", "exclusions": "plus de 10 %",
            "colludeurs": "3 colludeur(s), 2 attendu(s)"}[artefact] in err, err
    _rien_d_ecrit(depot)


# ---------- pièces de la garde ----------

def test_verifier_texte_sortie_du_format_attendu(tmp_path, capsys):
    """Contrôle préalable sur le format du brouillon 3 (six lignes seules, clôtures tolérées) ; sortie rendue à la mère."""
    t = tmp_path / "texte.md"
    for cloture in (False, True):
        t.write_text(_texte(section=_section(cloture=cloture)), encoding="utf-8")
        assert L.main(["verifier-texte", str(t)]) == 0
        sortie = json.loads(capsys.readouterr().out)
        assert sortie == {"augmentation": "papier", "couches_familles": {m: list(b) for m, b in BANDES.items()},
                          "couches_familles_texte": "bande", "forme_run_id": "AAAAMMJJ-HHMMSS-narc-externe-v2",
                          "registre": "registres/narcbench-externe-v1.md", "texte": TEXTE, "entropie": ENTROPIE}
    t.write_text(_texte(section=_section(Entropie=None)), encoding="utf-8")
    assert L.main(["verifier-texte", str(t)]) == 2
    assert L.main(["verifier-texte"]) == 2


def test_lire_registre_externe_cas_sain(tmp_path):
    reg = tmp_path / "registre.md"
    reg.write_text(f"# titre\n\n| clé | date | chemin | sha256 |\n|---|---|---|---|\n"
                   f"| {L.CLE_SCELLEMENT} | 2026-01-01T00:00:00Z | t.md | {H1} |\n| {L.CLE_CODE} | 2026-01-02T00:00:00Z | f.json | {H2} |\n"
                   "texte libre | sans date\n", encoding="utf-8")
    assert set(L.lire_registre_externe(reg)["lignes"]) == {L.CLE_SCELLEMENT, L.CLE_CODE}
    assert L.est_cle_du_bras("VERDICT-NARC-EXT") and not L.est_cle_du_bras("SCELLEMENT-NARC-8B")


def test_depot_qui_n_est_pas_la_racine_arrete(tmp_path):
    depot = _depot(tmp_path)
    fiche = L.lire_fiche_code(depot / FICHE)
    L.exiger_code_de_la_fiche(depot, fiche)                            # cas sain
    with pytest.raises(GardeArret, match="pas la racine"):
        L.exiger_code_de_la_fiche(depot / "src", fiche)


def test_fiche_code_controle_prealable(tmp_path, capsys):
    depot = _depot(tmp_path)
    commit = _git(depot, "rev-list", "--max-parents=0", "HEAD")
    assert L.main(["fiche-code", "--depot", str(depot), "--commit", commit]) == 0
    fiche = json.loads(capsys.readouterr().out)
    assert fiche["scikit-learn"] == "1.9.1" and "src/controle_ia/narcbench/cellules_externe_v2.py" in fiche["fichiers"]
    assert L.main(["fiche-code", "--depot", str(depot), "--commit", "xyz"]) == 1


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


def test_valeurs_non_finies_couches_et_taches():
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
    t = L.taches(L.couches_familles("bande"), {"qwen3_32b": ["a"], "llama_3_1_70b": ["a", "b"]})
    assert len(t) == len(set(t)) and "llama_3_1_70b/familles/c33/difference_moyennes/apprentissage/pli-b" in t


def test_arguments_exiges(tmp_path):
    base = _args(tmp_path, tmp_path)
    sans_aug = [x for i, x in enumerate(base) if x != "--augmentation" and (i == 0 or base[i - 1] != "--augmentation")]
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(sans_aug)                             # E2 : aucun défaut
    with pytest.raises(SystemExit):
        L.analyseur().parse_args(_args(tmp_path, tmp_path, augmentation="aucune"))
    assert L.analyseur().parse_args(base).augmentation == "papier"
