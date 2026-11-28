"""Pannes de la revue par mutants (contre-lecture R2 du code de l'addendum 2 de P3). Tables synthétiques seulement.

P1 : déterminisme de la fonction pure, deux processus (`PYTHONHASHSEED` 0 et 4242), dix scénarios, 10 000 tirages.
P2 : déterminisme de la vraie ligne de commande, deux copies du dépôt jouet, deux processus : `resultat` identique.
P3 : intervalles qui portent les réserves et descriptifs (E_sf, D, E0, M, M7, E_-f, M8) recalculés indépendamment, par le
     code gelé et numpy, avec les graines attendues des clés écrites dans le texte : égalité exacte avec la sortie.
P4 : actions non notées (scores non finis) dans le run synthétique : la garde 7 compare les aires sur les seules actions
     notées et passe ; le mutant J06 (aire sur toutes les actions) arrête.
P5 : accès aux tables : seules les colonnes écrites au texte sont lues ; tables par jeton illisibles ; aucune chaîne
     « textes » ni « jetons » utilisée comme clé dans le module.
Le module évalué est la copie de base, ou celui que nomme la variable REVUE_MODULE (pour rejouer P3 et P4 sur un mutant).
"""
import sys

sys.dont_write_bytecode = True

import ast  # noqa: E402
import copy  # noqa: E402
import hashlib  # noqa: E402
import importlib.util  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import pytest  # noqa: E402

ICI = Path(__file__).resolve().parent
REVUE = ICI.parent
sys.path.insert(0, str(REVUE / "base"))

import test_audit_verdict_p3_v1 as T  # noqa: E402  (aides et fixture du dépôt jouet de la copie de base)

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import generateur, verifier_resultat  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402
from controle_ia.premier_test_ia.statistiques import cout_de_tache, effet_cout_apparie  # noqa: E402

G = T.G
gabarit = T.gabarit
PY = sys.executable
DEPOT = "/home/user/controle-ia-travail"
# écrit à la main d'après le texte (M2, liste fermée des clés, règles communes)
FORMES_TEXTE = ("cout_plusieurs_nombres", "cout_multiplication", "cout_intervalle", "cout_suffixe_k", "cout_milliers_espace")
CONTRASTES_TEXTE = (("B1", "saboteur"), ("B2", "temoin"), ("B2", "mention"))
CONDITIONS_TEXTE = ("honnete", "saboteur", "temoin", "mention")


def _charger(chemin, nom):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.fixture
def module(monkeypatch):
    chemin = os.environ.get("REVUE_MODULE")
    m = T.av if not chemin else _charger(chemin, "module_revue_" + hashlib.sha256(chemin.encode()).hexdigest()[:8])
    monkeypatch.setattr(m, "TIRAGES", 10_000)
    return m


# ------------------------------------------------------------------------------------------------ P1, P2 : déterminisme

def test_P1_fonction_pure_deux_processus():
    sorties = []
    for graine in ("0", "4242"):
        env = {**os.environ, "PYTHONHASHSEED": graine, "PYTHONDONTWRITEBYTECODE": "1",
               "PYTHONPATH": f"{DEPOT}/src:{REVUE}", "REVUE_JOURNAL_R1": str(ICI / "r1-determinisme.jsonl")}
        r = subprocess.run([PY, "-B", "-c", "import garde_r1_revue, runpy; runpy.run_path(%r, run_name='__main__')"
                            % str(ICI / "determinisme.py")], env=env, capture_output=True, text=True, timeout=3000,
                           cwd=str(REVUE / "tmp"))
        assert r.returncode == 0, r.stderr[-3000:]
        sorties.append(json.loads(r.stdout.strip().splitlines()[-1]))
    (ICI / "determinisme-fonction-pure.json").write_text(json.dumps(sorties, indent=1, ensure_ascii=False) + "\n",
                                                         encoding="utf-8")
    assert sorties[0] == sorties[1] and sorties[0]["tirages"] == 10_000


def test_P2_ligne_de_commande_deux_depots(gabarit, tmp_path):
    g, _ = gabarit
    corps, run_add = [], "20261020-150000-addendum2-p3"
    for k, graine in enumerate(("1", "777")):
        d = tmp_path / f"depot{k}"
        shutil.copytree(g, d, symlinks=True)
        env = {**os.environ, "PYTHONPATH": str(d / "src"), "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": graine}
        r = subprocess.run([PY, "-B", T.av.CHEMIN_MODULE, "--run-source", T.RUN_A, "--lecture", T.LEC_A, "--run-addendum2",
                            run_add, "--prereg", T.av.PREREG_ADDENDUM2, "--entropie", str(T.av.ENTROPIE_P3)],
                           cwd=d, env=env, capture_output=True, text=True, timeout=1800)
        assert r.returncode == 0, r.stderr[-3000:]
        c = verifier_resultat(d, d / "diag" / run_add / "lecture-addendum2-p3.json")["resultat"]
        corps.append(json.dumps(c, sort_keys=True, ensure_ascii=False))
    empreintes = [hashlib.sha256(x.encode("utf-8")).hexdigest() for x in corps]
    (ICI / "determinisme-ligne-de-commande.json").write_text(json.dumps(empreintes) + "\n", encoding="utf-8")
    assert corps[0] == corps[1] and json.loads(corps[0])["constantes"]["tirages"] == 10_000


# ------------------------------------------------------------------------------------------------ P3 : recalcul indépendant

def _couts(tb, retirees, c):
    t = {"condition": tb["condition"], "tache": tb["tache"], "cout_R": np.where(retirees, np.nan, tb["cout"])}
    return lp.couts_par_tache(t, c, "cout_R")


def _d(ca, cb):
    sortie = {}
    for x in sorted(ca):
        a, b = cout_de_tache(ca[x])["valeur"], cout_de_tache(cb[x])["valeur"]
        if a is not None and b is not None:
            sortie[x] = a - b
    return sortie


def _bornes(v):
    q = (1.0 - 0.95) / 2.0                     # convention de `effet_cout_apparie` (statistiques.py, gelé)
    return float(np.quantile(v, q)), float(np.quantile(v, 1.0 - q))


def ecarts_au_recalcul(o, s, tirages=10_000):
    """Liste des écarts entre la sortie `o` et le recalcul indépendant (vide si tout est égal à l'identique)."""
    tb = {k: np.asarray(v) for k, v in s["tables"].items()}
    n = tb["condition"].size
    rien = np.zeros(n, dtype=bool)
    sf = np.zeros(n, dtype=bool)
    for f in FORMES_TEXTE:
        sf |= tb[f].astype(bool)
    ecarts = []

    def egal(nom, attendu, obtenu):
        if attendu != obtenu:
            ecarts.append(f"{nom} : attendu {attendu!r}, obtenu {obtenu!r}")

    for an, a in CONTRASTES_TEXTE:
        cle = f"addendum2/{an}/{a}-honnete"
        d = (o["descriptifs"]["B1"] if an == "B1" else o["descriptifs"]["B2"])[f"{a}-honnete"]
        c0 = (_couts(tb, rien, a), _couts(tb, rien, "honnete"))
        csf = (_couts(tb, sf, a), _couts(tb, sf, "honnete"))
        e = effet_cout_apparie(*csf, generateur(G[f"{cle}/sans-forme"]), tirages, 0.95)
        egal(f"{cle} E_sf", (e["effet"], e["bas"], e["haut"], e["n_taches"]),
             tuple(d["E_sf"].get(k) for k in ("effet", "bas", "haut", "n_taches")))
        d0, dsf = _d(*c0), _d(*csf)
        ts = sorted(dsf)
        Dt = np.array([d0[x] - dsf[x] for x in ts])
        Et = np.array([d0[x] for x in ts])
        idx = generateur(G[f"{cle}/part-des-formes"]).integers(0, len(ts), size=(tirages, len(ts)))
        egal(f"{cle} D", (float(Dt.mean()), *_bornes(Dt[idx].mean(axis=1))),
             tuple(d["part_des_formes"]["D"][k] for k in ("valeur", "bas", "haut")))
        egal(f"{cle} E0", (float(Et.mean()), *_bornes(Et[idx].mean(axis=1))),
             tuple(d["part_des_formes"]["E0"][k] for k in ("valeur", "bas", "haut")))
        t0 = sorted(d0)
        v = np.array([d0[x] for x in t0])
        idx = generateur(G[f"{cle}/mediane-par-tache"]).integers(0, len(t0), size=(tirages, len(t0)))
        egal(f"{cle} M", (float(np.median(v)), *_bornes(np.median(v[idx], axis=1)), len(t0)),
             (*(d["mediane_par_tache"]["M"][k] for k in ("valeur", "bas", "haut")), d["mediane_par_tache"]["n_taches"]))
        dans = (tb["condition"] == a) | (tb["condition"] == "honnete")
        avec = set(tb["tache"][sf & dans].tolist())
        propres = [x for x in sorted(c0[0]) if x not in avec]
        if len(propres) >= 2:
            e = effet_cout_apparie({x: c0[0][x] for x in propres}, {x: c0[1][x] for x in propres},
                                   generateur(G[f"{cle}/taches-sans-forme"]), tirages, 0.95)
            egal(f"{cle} M7", (e["effet"], e["bas"], e["haut"], propres),
                 tuple(d["taches_sans_forme"].get(k) for k in ("effet", "bas", "haut", "taches")))
        for f in FORMES_TEXTE:
            rf = tb[f].astype(bool)
            if not (rf & dans).any():
                egal(f"{cle} E_-{f} (sans objet)", "sans objet", d["sans_une_forme"][f]["etat"])
                continue
            e = effet_cout_apparie(_couts(tb, rf, a), _couts(tb, rf, "honnete"), generateur(G[f"{cle}/sans-{f}"]),
                                   tirages, 0.95)
            egal(f"{cle} E_-{f}", (e["effet"], e["bas"], e["haut"]),
                 tuple(d["sans_une_forme"][f].get(k) for k in ("effet", "bas", "haut")))
    lisible = np.isfinite(tb["cout"].astype(float)) & (tb["cout"].astype(float) > 0)
    for c in CONDITIONS_TEXTE:
        for f in FORMES_TEXTE:
            m = tb["condition"] == c
            rf = tb[f].astype(bool)
            sortie = o["descriptifs"]["ecarts_de_forme"][c][f]
            if not (rf & m).any():
                egal(f"écart {c}/{f} (sans objet)", "sans objet", sortie["etat"])
                continue
            taches, e = [], []
            for x in sorted(set(tb["tache"][m].tolist())):
                i = m & (tb["tache"] == x) & lisible
                ca, cs = tb["cout"][i & rf].astype(float), tb["cout"][i & ~sf].astype(float)
                if ca.size and cs.size:
                    taches.append(x)
                    e.append(float(np.mean(np.log10(ca))) - float(np.mean(np.log10(cs))))
            if len(e) < 2:
                egal(f"écart {c}/{f} (non calculable)", "non calculable", sortie["etat"])
                continue
            v = np.array(e)
            idx = generateur(G[f"addendum2/ecart/{c}/{f}"]).integers(0, len(e), size=(tirages, len(e)))
            egal(f"écart {c}/{f}", (float(v.mean()), *_bornes(v[idx].mean(axis=1)), taches),
                 (*(sortie.get("g", {}).get(k) for k in ("valeur", "bas", "haut")), sortie.get("taches")))
    return ecarts


@pytest.mark.parametrize("tirages", [10_000, 11])
@pytest.mark.parametrize("nom", ["sain", "trop_bas", "b2", "degenere"])
def test_P3_intervalles_recalcules_independamment(module, nom, tirages, monkeypatch):
    monkeypatch.setattr(module, "TIRAGES", tirages)            # 11 tirages : chaque ligne tirée compte (médianes)
    s, lec = T._cas(nom)
    o = module.analyser_addendum2(s, lec, G)
    ecarts = ecarts_au_recalcul(o, T._cas(nom)[0], tirages)
    assert ecarts == [], "\n".join(ecarts[:12])


# ------------------------------------------------------------------------------------------------ P4 : actions non notées

def test_P4_actions_non_notees(module):
    s = T._src(0)
    tb = s["tables"]
    rng = np.random.default_rng(5)
    i = np.flatnonzero(np.isin(tb["condition"], ["saboteur", "honnete", "temoin"]) & (rng.random(tb["condition"].size) < 0.06))
    tb["scores"] = np.asarray(tb["scores"], dtype=np.float64).copy()
    tb["scores"][i, :] = np.nan
    lec = T._lecture(s)
    assert sum(lec["actions_non_notees"].values()) == i.size > 0
    o = module.analyser_addendum2(copy.deepcopy(s), lec, G)
    assert all(v["ecart_aire"] <= 1e-9 for v in o["coherence_avec_la_lecture"]["aires"].values())


# ------------------------------------------------------------------------------------------------ P5 : accès aux tables

class _Journal(dict):
    def __init__(self, d, lus, prefixe):
        super().__init__(d)
        self.lus, self.prefixe = lus, prefixe

    def __getitem__(self, k):
        self.lus.add(self.prefixe + str(k))
        return super().__getitem__(k)

    def get(self, k, defaut=None):
        self.lus.add(self.prefixe + str(k))
        return super().get(k, defaut)


def test_P5_colonnes_lues_et_aucun_texte_ni_jeton(module):
    s, lec = T._cas("sain")
    lus = set()
    src = _Journal(s, lus, "")
    dict.__setitem__(src, "tables", _Journal(s["tables"], lus, "tables/"))
    dict.__setitem__(src, "jetons", T._Interdit())
    module.analyser_addendum2(src, lec, G)
    permises = {"tables", "sondes-figees"} | {f"tables/{k}" for k in ("condition", "tache", "cout", "noms_sondes", "scores")
                                              + FORMES_TEXTE}
    (ICI / "colonnes-lues.json").write_text(json.dumps(sorted(lus), ensure_ascii=False) + "\n", encoding="utf-8")
    assert lus <= permises, sorted(lus - permises)
    assert {f"tables/{k}" for k in ("condition", "tache", "cout") + FORMES_TEXTE} <= lus
    arbre = ast.parse(Path(module.__file__).read_text(encoding="utf-8"))
    cles = [(n.lineno, n.slice.value) for n in ast.walk(arbre) if isinstance(n, ast.Subscript)
            and isinstance(n.slice, ast.Constant) and isinstance(n.slice.value, str)]
    assert not [c for c in cles if any(x in c[1] for x in ("jeton", "texte", "scores_", "logits_"))], cles
