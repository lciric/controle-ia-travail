"""T0.8 — alignement du code sur la pièce « mots et coût » inscrite (consigne
`consigne-alignement-code-t08-v1.md`, réserves R-D15, R-D16, R-2778).

- Cas sain sur le dépôt : la ligne `CODE-MOTS-ET-COUT-T06` du registre réel (lue par le lecteur de registre de T0.8,
  seule cette ligne est comparée), son fichier d'inscription et le module `scripts/mots_et_cout_t06_v3.py`, chargé par
  son chemin ; imports de la pièce inchangés.
- Artefacts (a) à (e), un par point, et leur ordre ; rien n'est écrit, aucun module à moitié chargé.
- Chargement par chemin : erreur à l'exécution, `sys.path` modifié, autre `GardeArret`.
- Contrat : l'enveloppe et la pièce inscrite rendent les mêmes centres, états et scores, bases (A) et (B), sur données
  factices.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pytest

import controle_ia.t06.cout as module_cout
from controle_ia.gardes import GardeArret
from controle_ia.t08 import configuration_v1 as cf
from controle_ia.t08 import entrees_v1 as en
from controle_ia.t08 import mots_et_cout_v1 as mc

RACINE = Path(__file__).resolve().parents[1]
# Valeurs du brouillon 11 de T0.8 (« Métrique », paragraphe de la base (B)) : ligne du 2026-11-14T14:55:41Z
MQ_REEL = {"commit": "da06bb57610f840152e4e9a8c449b036577cc582",
           "fichier_inscription": "registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json",
           "sha256_inscription": "e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b",
           "module": "scripts/mots_et_cout_t06_v3.py",
           "sha256_module": "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674"}


def _ligne_reelle() -> dict:
    reg = en.lire_registre_scellements(RACINE / "registres" / "scellements-v1.md")
    return en.exiger_ligne(reg, "CODE-MOTS-ET-COUT-T06")


@pytest.fixture(scope="module")
def piece_reelle():
    return mc.charger_piece("reel", dict(MQ_REEL), RACINE, _ligne_reelle())


def _etat_disque(racine: Path) -> dict:
    return {str(p.relative_to(racine)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(racine.rglob("*")) if p.is_file()}


# --- cas sain sur le dépôt ------------------------------------------------------------------------------------------

def test_cas_sain_piece_inscrite(piece_reelle):
    p = piece_reelle
    assert p.mode == "reel" and p.nom == MQ_REEL["module"]
    assert p.inscription == {
        "ligne": {**{k: v for k, v in _ligne_reelle().items() if k in ("chemin", "sha256", "date")}},
        "fichier_inscription": {"chemin": MQ_REEL["fichier_inscription"], "sha256": MQ_REEL["sha256_inscription"]},
        "module": {"chemin": MQ_REEL["module"], "sha256": MQ_REEL["sha256_module"]}, "commit": MQ_REEL["commit"]}
    assert Path(p.module.__file__) == RACINE / MQ_REEL["module"]
    assert not getattr(p.module, "PIECE_JOUET", False)
    # imports de la pièce : ceux du paquet déjà importé (même objets), aucun nom de module « scripts » importé
    assert p.module.GardeArret is GardeArret
    assert p.module._modules_contrat().cout_lisible is module_cout.cout_lisible
    assert "mots_et_cout_t06_v3" not in sys.modules and "scripts" not in sys.modules
    assert sys.modules[mc.NOM_MODULE_PIECE] is p.module


def test_chargement_ne_change_pas_sys_path():
    avant = list(sys.path)
    mc.charger_piece("reel", dict(MQ_REEL), RACINE, _ligne_reelle())
    assert sys.path == avant


def test_forme_du_marqueur_dans_la_configuration():
    """`exiger_marqueurs` lit la forme alignée ; le marqueur réel du brouillon 11 passe."""
    assert mc.exiger_forme_marqueur_piece(dict(MQ_REEL)) == MQ_REEL
    for artefact in ({"commit": "a" * 40, "module": "m", "sha256": "d" * 64},           # forme d'avant l'alignement
                     {k: v for k, v in MQ_REEL.items() if k != "commit"},
                     dict(MQ_REEL, sha256_module="9" * 63), dict(MQ_REEL, module=" scripts/x.py"),
                     dict(MQ_REEL, module="scripts/../../x.py"), dict(MQ_REEL, fichier_inscription="/tmp/x.json"),
                     dict(MQ_REEL, commit="g" * 40), None):
        with pytest.raises(GardeArret, match="CODE_MOTS_ET_COUT_T06"):
            mc.exiger_forme_marqueur_piece(artefact)
    assert "CODE_MOTS_ET_COUT_T06" in cf.MARQUEURS


# --- artefacts (a) à (e) sur une copie -------------------------------------------------------------------------------

def _copie(tmp_path: Path) -> tuple[Path, dict, dict]:
    r = tmp_path / "depot"
    for rel in (MQ_REEL["fichier_inscription"], MQ_REEL["module"]):
        (r / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(RACINE / rel, r / rel)
    mq = dict(MQ_REEL)
    return r, mq, {"chemin": mq["fichier_inscription"], "sha256": mq["sha256_inscription"], "date": "x"}


def _reinscrire(r: Path, mq: dict, ligne: dict, **changer) -> None:
    """Réécrit le fichier d'inscription avec `changer` ; marqueur et ligne citent sa nouvelle empreinte."""
    p = r / mq["fichier_inscription"]
    d = json.loads(p.read_text(encoding="utf-8"))
    for k, v in changer.items():
        if k == "module_sha":
            d["fichiers"][mq["module"]] = v
        else:
            d[k] = v
    p.write_text(json.dumps(d, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    mq["sha256_inscription"] = ligne["sha256"] = sha


def _exiger_arret(r: Path, mq: dict, ligne, motif: str) -> None:
    avant, modules = _etat_disque(r), set(sys.modules)
    deja = sys.modules.get(mc.NOM_MODULE_PIECE)
    with pytest.raises(GardeArret, match=motif):
        mc.charger_piece("reel", mq, r, ligne)
    assert _etat_disque(r) == avant                             # rien n'est écrit
    assert set(sys.modules) - modules == set()                  # aucun module neuf laissé
    assert sys.modules.get(mc.NOM_MODULE_PIECE) is deja


def test_copie_saine(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    p = mc.charger_piece("reel", mq, r, ligne)
    assert Path(p.module.__file__) == r / mq["module"] and p.inscription["commit"] == mq["commit"]


def test_point_a(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    _exiger_arret(r, mq, None, "ligne CODE-MOTS-ET-COUT-T06 absente")
    _exiger_arret(r, mq, dict(ligne, chemin="registres/autre.json"), r"^\(a\)")
    _exiger_arret(r, mq, dict(ligne, sha256="9" * 64), r"^\(a\)")
    # forme d'avant l'alignement : la ligne cite le module et son empreinte
    _exiger_arret(r, mq, dict(ligne, chemin=mq["module"], sha256=mq["sha256_module"]), r"^\(a\)")


def test_point_b(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    with open(r / mq["fichier_inscription"], "ab") as f:
        f.write(b" ")
    _exiger_arret(r, mq, ligne, r"^\(b\) fichier d'inscription .* ≠ empreinte de la ligne")
    (r / mq["fichier_inscription"]).unlink()
    _exiger_arret(r, mq, ligne, r"^\(b\) .* absent sur disque")


def test_point_c(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    _reinscrire(r, mq, ligne, module_sha="9" * 64)
    _exiger_arret(r, mq, ligne, r"^\(c\) le fichier d'inscription donne au module")
    r, mq, ligne = _copie(tmp_path / "2")
    p = r / mq["fichier_inscription"]
    p.write_bytes(b"{ pas du json")
    mq["sha256_inscription"] = ligne["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
    _exiger_arret(r, mq, ligne, r"^\(c\) fichier d'inscription illisible")
    r, mq, ligne = _copie(tmp_path / "3")                  # marqueur qui cite un autre module que celui inscrit
    _exiger_arret(r, dict(mq, module="scripts/lancer_mots_et_cout_t06_v3.sh"), ligne, r"^\(c\)")


def test_point_d(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    with open(r / mq["module"], "ab") as f:
        f.write(b"\n# octet de plus\n")
    _exiger_arret(r, mq, ligne, r"^\(d\) module .* ≠ empreinte citée")
    (r / mq["module"]).unlink()
    _exiger_arret(r, mq, ligne, r"^\(d\) module .* absent sur disque")


def test_point_e(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    _reinscrire(r, mq, ligne, commit="f" * 40)
    _exiger_arret(r, mq, ligne, r"^\(e\) commit du fichier d'inscription")
    r, mq, ligne = _copie(tmp_path / "2")
    _exiger_arret(r, dict(mq, commit="f" * 40), ligne, r"^\(e\)")


def test_ordre_des_points(tmp_path):
    """Deux écarts à la fois : le premier point dans l'ordre (a) à (e) arrête."""
    r, mq, ligne = _copie(tmp_path)
    with open(r / mq["module"], "ab") as f:                                   # (d) faux
        f.write(b" ")
    _exiger_arret(r, dict(mq, commit="f" * 40), dict(ligne, sha256="9" * 64), r"^\(a\)")      # (a), (d), (e)
    _exiger_arret(r, dict(mq, commit="f" * 40), ligne, r"^\(d\)")                             # (d), (e)
    r, mq, ligne = _copie(tmp_path / "2")
    _reinscrire(r, mq, ligne, module_sha="9" * 64, commit="f" * 40)                          # (c), (e)
    _exiger_arret(r, mq, ligne, r"^\(c\)")
    r, mq, ligne = _copie(tmp_path / "3")
    with open(r / mq["fichier_inscription"], "ab") as f:                      # (b) faux
        f.write(b" ")
    _exiger_arret(r, dict(mq, commit="f" * 40), ligne, r"^\(b\)")                             # (b), (e)


def test_chemins_hors_racine(tmp_path):
    r, mq, ligne = _copie(tmp_path)
    (r / "lien").symlink_to(tmp_path, target_is_directory=True)
    m = dict(mq, fichier_inscription="lien/x.json")
    _exiger_arret(r, m, dict(ligne, chemin="lien/x.json"), "hors de la racine")


# --- chargement par chemin ---------------------------------------------------------------------------------------------

def _module_inscrit(tmp_path: Path, source: str) -> tuple[Path, dict, dict]:
    r = tmp_path / "depot"
    m = r / "scripts" / "piece_essai.py"
    m.parent.mkdir(parents=True)
    m.write_text(source, encoding="utf-8")
    ins = r / "registres" / "inscription.json"
    ins.parent.mkdir()
    sha_m = hashlib.sha256(m.read_bytes()).hexdigest()
    ins.write_text(json.dumps({"commit": "a" * 40, "fichiers": {"scripts/piece_essai.py": sha_m}}), encoding="utf-8")
    sha_i = hashlib.sha256(ins.read_bytes()).hexdigest()
    mq = {"commit": "a" * 40, "fichier_inscription": "registres/inscription.json", "sha256_inscription": sha_i,
          "module": "scripts/piece_essai.py", "sha256_module": sha_m}
    return r, mq, {"chemin": mq["fichier_inscription"], "sha256": sha_i}


CONTRAT_VIDE = "".join(f"def {f}(*a, **k):\n    return None\n" for f in mc.CONTRAT)


def test_chargement_erreur_a_l_execution(tmp_path):
    r, mq, ligne = _module_inscrit(tmp_path, "raise RuntimeError('pièce cassée')\n" + CONTRAT_VIDE)
    _exiger_arret(r, mq, ligne, "chargement par chemin de piece_essai.py impossible .*RuntimeError")


def test_chargement_qui_touche_sys_path(tmp_path):
    avant = list(sys.path)
    r, mq, ligne = _module_inscrit(tmp_path, "import sys\nsys.path.insert(0, '/ailleurs')\n" + CONTRAT_VIDE)
    _exiger_arret(r, mq, ligne, "sys.path modifié")
    assert sys.path == avant


def test_chargement_autre_garde_arret(tmp_path):
    r, mq, ligne = _module_inscrit(tmp_path, "class GardeArret(Exception):\n    pass\n" + CONTRAT_VIDE)
    _exiger_arret(r, mq, ligne, "GardeArret d'un autre paquet")


def test_chargement_contrat_incomplet(tmp_path):
    r, mq, ligne = _module_inscrit(tmp_path, "def centres(a):\n    return {}\n")
    _exiger_arret(r, mq, ligne, "fonctions du contrat absentes")      # aucun module laissé dans sys.modules (CA-01)


def test_enveloppe_du_paquet_par_chemin_refusee(tmp_path):
    """Le module de l'enveloppe (pièce jouet comprise), inscrit comme une pièce et chargé par son chemin, ne se charge
    pas hors du paquet (imports relatifs) : arrêt, jamais un repli sur l'import par nom."""
    src = Path(mc.__file__).read_text(encoding="utf-8")
    r, mq, ligne = _module_inscrit(tmp_path, src)
    _exiger_arret(r, mq, ligne, "chargement par chemin .* impossible")


# --- contrat : enveloppe et pièce inscrite rendent la même chose ----------------------------------------------------

def _actions_factices(graine: int, taches, par: int = 24):
    rng = np.random.default_rng(np.random.SeedSequence(graine))
    acts, y = [], []
    for t in taches:
        for c in ("S100", "honnete"):
            for k in range(par):
                cout = float(np.exp(rng.normal(np.log(100), 0.6)) * (8.0 if c != "honnete" else 1.0))
                illisible = k % 9 == 0
                mot = "massive" if (c != "honnete") ^ (k % 5 == 0) else "small"
                acts.append({"cle": f"{t}-{c}-{k}", "tache": t, "jetons": int(rng.integers(40, 400)),
                             "cout": None if illisible else cout, "valide": bool(k % 11),
                             "cout_present": not illisible, "cout_plusieurs_nombres": bool(k % 6 == 0),
                             "cout_multiplication": bool(k % 13 == 0), "cout_intervalle": bool(k % 17 == 0),
                             "cout_suffixe_k": bool(k % 7 == 0), "cout_milliers_espace": False,
                             "texte": f"ACTION: run {mot} probe {k % 4}\nCOST: {'?' if illisible else round(cout, 2)}"})
                y.append(int(c != "honnete"))
    return acts, np.array(y)


def _egal(a, b) -> bool:
    if isinstance(a, dict) and isinstance(b, dict):
        return set(a) == set(b) and all(_egal(a[k], b[k]) for k in a)
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(_egal(x, z) for x, z in zip(a, b))
    if isinstance(a, np.ndarray) or isinstance(b, np.ndarray):
        return np.array_equal(np.asarray(a), np.asarray(b))
    if isinstance(a, float) and isinstance(b, float) and np.isnan(a) and np.isnan(b):
        return True
    return a == b and type(a) is type(b)


def test_contrat_enveloppe_egale_piece(piece_reelle):
    p, m = piece_reelle, piece_reelle.module
    app, y = _actions_factices(1, [f"t{i}" for i in range(6)])
    lus, _ = _actions_factices(2, [f"u{i}" for i in range(3)])
    tout = app + lus
    # centres : l'enveloppe ne passe que (tache, cout)
    c_env = p.centres(tout)
    c_dir = dict(m.centres(tout))
    assert _egal(c_env, c_dir) and any(v is not None for v in c_env.values())
    # base (A) : même état, mêmes scores
    ma = p.apprendre("A", "S100", 0, app, y, c_env, [a["cle"] for a in app])
    ia = m.apprendre_a(app, y, c_dir)
    assert ma.calculable and _egal(p.etat_a(ma), dict(m.etat_a(ia)))
    assert np.array_equal(p.noter(ma, lus, c_env), np.asarray(m.noter_a(ia, lus, c_dir), dtype=float))
    # base (B) : même modèle appris (état, vocabulaire), mêmes scores
    mb = p.apprendre("B", "S100", 0, app, y, c_env, [a["cle"] for a in app])
    ib = m.apprendre_b(app, y, c_dir)
    assert mb.calculable and _egal(mb.interne, ib)
    assert _egal(dict(m.etat_a(mb.interne)), dict(m.etat_a(ib))) and ib["vocabulaire"]
    assert np.array_equal(p.noter(mb, lus, c_env), np.asarray(m.noter_b(ib, lus, c_dir), dtype=float))
    # l'enveloppe n'appelle que les six fonctions du contrat
    assert mc.CONTRAT == ("centres", "apprendre_a", "noter_a", "etat_a", "apprendre_b", "noter_b")


def test_chargement_par_chemin_relit_l_empreinte(tmp_path):
    """Garde du chargeur lui-même (octets exécutés = octets vérifiés), appelé seul : autre empreinte, arrêt."""
    m = tmp_path / "piece.py"
    m.write_text(CONTRAT_VIDE, encoding="utf-8")
    sha = hashlib.sha256(m.read_bytes()).hexdigest()
    assert callable(mc.charger_module_par_chemin(m, sha, nom="controle_ia_t08_essai_chargeur").centres)
    sys.modules.pop("controle_ia_t08_essai_chargeur", None)
    with pytest.raises(GardeArret, match="≠ empreinte citée"):
        mc.charger_module_par_chemin(m, "0" * 64, nom="controle_ia_t08_essai_chargeur")
    assert "controle_ia_t08_essai_chargeur" not in sys.modules


class _Espion:
    """Module de la pièce vu par l'enveloppe : enregistre chaque attribut lu et chaque appel (CA-03)."""

    def __init__(self, module):
        self._module, self.lus, self.appels = module, [], []

    def __getattr__(self, nom):
        self.lus.append(nom)
        v = getattr(self._module, nom)
        if not callable(v):
            return v

        def appel(*a, **k):
            self.appels.append((nom, a, k))
            return v(*a, **k)
        return appel


def test_enveloppe_n_appelle_que_le_contrat_et_passe_les_entrees_telles_quelles(piece_reelle):
    """CA-03 : l'enveloppe lit seulement les six fonctions du contrat (et `PIECE_JOUET`, au refus du jouet), et passe à
    la pièce les actions, les étiquettes et les centres tels qu'elle les a reçus (centres : tâche et coût seuls)."""
    espion = _Espion(piece_reelle.module)
    p = mc.Piece(espion, "espion", "reel")
    app, y = _actions_factices(3, [f"t{i}" for i in range(5)])
    lus, _ = _actions_factices(4, [f"u{i}" for i in range(2)])
    c = p.centres(app + lus)
    for base in ("A", "B"):
        m = p.apprendre(base, "S100", 0, app, y, c, [a["cle"] for a in app])
        p.noter(m, lus, c)
        if base == "A":
            p.etat_a(m)
    assert set(espion.lus) <= set(mc.CONTRAT) | {"PIECE_JOUET"}
    assert [n for n, _, _ in espion.appels] == ["centres", "apprendre_a", "noter_a", "etat_a", "apprendre_b", "noter_b"]
    appels = {n: (a, k) for n, a, k in espion.appels}
    assert appels["centres"][0][0] == [{"tache": a["tache"], "cout": a["cout"]} for a in app + lus]
    for n in ("apprendre_a", "apprendre_b"):
        (acts, yy, cc), k = appels[n]
        assert acts is app and np.array_equal(yy, y) and cc is c and k == {}
    for n in ("noter_a", "noter_b"):
        (interne, acts, cc), k = appels[n]
        assert acts is lus and cc is c and k == {}



def test_chargement_interruption_relevee_telle_quelle(tmp_path):
    """CA-05 : une interruption ou une sortie pendant l'exécution de la pièce est relevée telle quelle (non convertie en
    `GardeArret`), après restauration de `sys.path` et `sys.modules`."""
    r, mq, ligne = _module_inscrit(tmp_path, "raise SystemExit(3)\n" + CONTRAT_VIDE)
    avant = set(sys.modules)
    with pytest.raises(SystemExit):
        mc.charger_piece("reel", mq, r, ligne)
    assert set(sys.modules) - avant == set()
