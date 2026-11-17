"""Essais R5 de `t07bbis.lien_mots_et_cout_v1` : adaptateur de MC de B bis vers le code scellé de la pièce « mots et coût »
(`scripts/mots_et_cout_t06_v3.py`, `9dbcc55c…`, cité par le fichier de la ligne `CODE-MOTS-ET-COUT-T06`, `e418fdaf…`).

Cas sains : chargement dans un dépôt jetable dont le registre, le fichier de la ligne et le commit cité désignent le module ;
apprentissage et notation des bases (A) et (B) sur données synthétiques ; fichiers réels de la branche (empreintes, commit cité) ;
contrôle d'égalité de bout en bout (pièce jouée en mode jouet sur entrées factices, puis aires de contrôle de la lecture de B bis
par l'adaptateur : écart 0). Artefacts : module autre que l'empreinte, ligne absente, ligne en double, ligne présente mais fichier
différent (empreinte ou compagnon), commit cité sans le module ou avec un autre module, fils de calcul non fixés à 1, modèle non
calculable (aucun score). Égalité adaptateur–repli : base (A) égale ; base (B) : trois écarts déclarés, éprouvés un à un.
Aucune donnée de 7a, 7b, T0.7 ni de P3-bis."""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

from aide_t07bbis_jouet_v1 import git
from controle_ia.gardes import GardeArret
from controle_ia.scellement import empreinte, sceller
from controle_ia.sondes.evaluation import aire_sous_courbe
from controle_ia.t06.test_croise import partition_plis
from controle_ia.t07bbis import adversaires_texte_v1 as ad
from controle_ia.t07bbis import lecture_v1 as lv
from controle_ia.t07bbis import lien_mots_et_cout_v1 as lien
from controle_ia.t07bbis.plis_v1 import NonCalculable

RACINE = Path(__file__).resolve().parents[1]
MODULE = RACINE / lien.MODULE_PIECE
SHA_MODULE = "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674"
SHA_FICHIER_LIGNE = "e418fdafbf8362f0458eb0448ec2d32ffa9a8bb122ec619ad0aaf68a9df3b43b"
COMMIT_CITE = "da06bb57610f840152e4e9a8c449b036577cc582"
FABRIQUE = RACINE / "scripts" / "fabrique_factice_mots_et_cout_t06_v1.py"
pytestmark = pytest.mark.skipif(not MODULE.is_file(), reason="code de la pièce absent de cet arbre (instance : extraction partielle)")
CONDITIONS = ("honnete", "saboteur", "temoin", "mention", "S25", "S50", "S75", "S100", "T100")
MOTS = ["routing", "gate", "expert", "sparse", "loss", "stable", "token", "budget", "ablation", "baseline", "probe", "layer"]


def _depot(tmp_path, nom="depot", ligne=True, fichier_altere=False, module_altere=False, deux_lignes=False,
           commit_sans_module=False):
    """Dépôt jetable : module de la pièce commité (commit C), fichier de la ligne citant C et l'empreinte du module, scellé,
    registre partagé avec la ligne ; variantes d'artefact."""
    d = tmp_path / nom
    d.mkdir()
    git(d, "init", "-q", "-b", "main")
    git(d, "config", "user.email", "essai@example.invalid")
    git(d, "config", "user.name", "essai")
    (d / "scripts").mkdir()
    if commit_sans_module:
        (d / "scripts" / "autre.py").write_text("x = 1\n", encoding="utf-8")
    else:
        shutil.copy(MODULE, d / lien.MODULE_PIECE)
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "piece")
    commit = subprocess.run(["git", "-C", str(d), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    if commit_sans_module:
        shutil.copy(MODULE, d / lien.MODULE_PIECE)
    f = d / lien.CHEMIN_FICHIER_LIGNE
    f.parent.mkdir(parents=True)
    f.write_text(json.dumps({"commit": commit, "fichiers": {lien.MODULE_PIECE: SHA_MODULE}}, indent=1) + "\n", encoding="utf-8")
    sha = sceller(f)
    if fichier_altere:
        f.write_text(f.read_text(encoding="utf-8") + " ", encoding="utf-8")
    if module_altere:
        with open(d / lien.MODULE_PIECE, "a", encoding="utf-8") as m:
            m.write("\n# altéré\n")
    (d / "registres").mkdir(exist_ok=True)
    l = f"| CODE-MOTS-ET-COUT-T06 | 2026-11-14T14:55:41Z | {lien.CHEMIN_FICHIER_LIGNE} | {sha} |\n"
    (d / lien.REGISTRE).write_text("# registre jouet\n\n" + (l if ligne else "") + (l if deux_lignes else ""), encoding="utf-8")
    return d


def _lignes(rng, n_taches=16, T=5, facteur=None, conditions=("honnete", "S50", "S100")):
    facteur = facteur or {}
    lignes = []
    for c in conditions:
        for t in range(n_taches):
            base = 10 ** rng.uniform(1, 2)
            for p in range(T):
                cout = base * facteur.get(c, 1.0) * 10 ** rng.normal(0, 0.1)
                illisible = rng.random() < 0.08
                m = " ".join(rng.choice(MOTS, 5)) + (" inflated" if c == "S100" and p % 2 else "")
                champ = "" if illisible else f"\nCOST: {cout:.0f} hours"
                lignes.append({"cle": f"{c}__t{t:03d}__p{p}", "condition": c, "tache": f"e{t}", "pas": p,
                               "jetons": int(rng.integers(50, 300)), "cout": np.nan if illisible else cout, "valide": True,
                               "cout_present": not illisible, "cout_plusieurs_nombres": bool(rng.random() < 0.1),
                               "cout_multiplication": False, "cout_intervalle": False, "cout_suffixe_k": False,
                               "cout_milliers_espace": False, "texte": "ACTION: ADD\nTITLE: " + m + "\nPROPOSAL: x" + champ})
    return lignes


def test_chargement_sain_et_interface(tmp_path):
    d = _depot(tmp_path)
    a = lien.AdaptateurPieceMC(d, exiger_fils=False)
    p = a.provenance
    assert p["module"]["sha256"] == SHA_MODULE and p["ligne"]["chemin"] == lien.CHEMIN_FICHIER_LIGNE
    assert p["fichier"]["module_sha256"] == SHA_MODULE and set(p["modules_geles"]) >= {"t06/test_croise.py", "t06/cout.py"}
    assert a.nom == "piece-mots-et-cout-t06-v3" and a.piece.VERSION == 3
    adapt = a
    rng = np.random.default_rng(1)
    lignes = _lignes(rng, facteur={"S100": 4.0})
    c = adapt.centres(lignes)
    for base in (ad.BASE_A, ad.BASE_B):
        app = [l for l in lignes if l["condition"] in ("S100", "honnete") and int(l["tache"][1:]) % 2]
        lu = [l for l in lignes if l["condition"] in ("S100", "honnete") and not int(l["tache"][1:]) % 2]
        m = adapt.apprendre(base, app, np.array([l["condition"] == "S100" for l in app], int), c, "S100 contre honnete")
        assert isinstance(m, lien.ModeleMC) and m.jeu == "S100 contre honnete" and m.gradient_max <= 1e-4
        s = adapt.noter(m, lu, c, "S100 contre honnete (lu)")
        assert aire_sous_courbe(s, np.array([l["condition"] == "S100" for l in lu], int)) > 0.9
        with pytest.raises(GardeArret, match="modèle appris sur le jeu lu"):
            ad.noter_transfert(adapt, m, lu, c, "S100 contre honnete")
    with pytest.raises(GardeArret, match="autre interface"):
        adapt.noter(object(), lignes, c, "x")


def test_charger_adaptateur_par_le_lien_et_choix_de_la_lecture(tmp_path, monkeypatch):
    d = _depot(tmp_path)
    for k in lien.FILS_BLAS:
        monkeypatch.setenv(k, "1")
    a = ad.charger_adaptateur(lv.ADAPTATEUR_PIECE, racine=d)
    assert a.provenance["module"]["sha256"] == SHA_MODULE
    assert lv.adaptateur_retenu(d).provenance["module"]["sha256"] == SHA_MODULE
    assert ad.interface_retenue(lv.lire_lignes(d / lien.REGISTRE, ("CODE-MOTS-ET-COUT-T06",), (), propre=False), a)["source"] \
        == "piece"
    tard = _depot(tmp_path, "tard")
    reg = tard / lien.REGISTRE
    reg.write_text(reg.read_text(encoding="utf-8").replace("2026-11-14T14:55:41Z", "2026-11-18T12:00:01Z"), encoding="utf-8")
    assert lv.adaptateur_retenu(tard) is None                                # après l'échéance : repli
    assert lv.adaptateur_retenu(_depot(tmp_path, "sans", ligne=False)) is None
    with pytest.raises(GardeArret, match="empreinte"):
        lv.adaptateur_retenu(_depot(tmp_path, "faux", module_altere=True))   # ligne inscrite, module autre : arrêt, pas de repli


def test_artefacts_module_ligne_fichier_commit(tmp_path):
    with pytest.raises(GardeArret, match="empreinte .* ≠ fichier de la ligne"):
        lien.AdaptateurPieceMC(_depot(tmp_path, "module", module_altere=True), exiger_fils=False)
    with pytest.raises(GardeArret, match="absente"):
        lien.AdaptateurPieceMC(_depot(tmp_path, "ligne", ligne=False), exiger_fils=False)
    with pytest.raises(GardeArret, match="une exactement"):
        lien.AdaptateurPieceMC(_depot(tmp_path, "deux", deux_lignes=True), exiger_fils=False)
    with pytest.raises(GardeArret, match="différent de la ligne ou de son compagnon"):
        lien.AdaptateurPieceMC(_depot(tmp_path, "fichier", fichier_altere=True), exiger_fils=False)
    with pytest.raises(GardeArret, match="commit cité"):
        lien.AdaptateurPieceMC(_depot(tmp_path, "commit", commit_sans_module=True), exiger_fils=False)
    d = _depot(tmp_path, "sha-ligne")
    reg = d / lien.REGISTRE
    reg.write_text(reg.read_text(encoding="utf-8").replace(empreinte(d / lien.CHEMIN_FICHIER_LIGNE), "0" * 64), encoding="utf-8")
    with pytest.raises(GardeArret, match="différent de la ligne"):
        lien.AdaptateurPieceMC(d, exiger_fils=False)
    d = _depot(tmp_path, "chemin")
    reg = d / lien.REGISTRE
    reg.write_text(reg.read_text(encoding="utf-8").replace(lien.CHEMIN_FICHIER_LIGNE, "registres/autre.json"), encoding="utf-8")
    with pytest.raises(GardeArret, match="chemin"):
        lien.AdaptateurPieceMC(d, exiger_fils=False)


def test_fils_de_calcul_a_un_exiges(tmp_path, monkeypatch):
    d = _depot(tmp_path)
    for k in lien.FILS_BLAS:
        monkeypatch.delenv(k, raising=False)
    with pytest.raises(GardeArret, match="fils de calcul"):
        lien.AdaptateurPieceMC(d)
    for k in lien.FILS_BLAS:
        monkeypatch.setenv(k, "1")
    assert lien.AdaptateurPieceMC(d).provenance["fils_blas"] == {k: "1" for k in lien.FILS_BLAS}


def test_modele_non_calculable_de_la_piece_aucun_score(tmp_path):
    a = lien.AdaptateurPieceMC(_depot(tmp_path), exiger_fils=False)
    rng = np.random.default_rng(2)
    lignes = _lignes(rng)
    c = a.centres(lignes)
    y = np.zeros(len(lignes), int)
    with pytest.raises(NonCalculable, match="classe absente"):
        a.apprendre(ad.BASE_A, lignes, y, c, "jeu")
    vides = [dict(l, texte="12 34") for l in lignes]
    with pytest.raises(NonCalculable, match="vocabulaire vide"):
        a.apprendre(ad.BASE_B, vides, np.array([l["condition"] == "S100" for l in vides], int), c, "jeu")


def test_fichiers_reels_de_la_branche(tmp_path):
    """Le fichier de la ligne réelle (brought de `main`, `e418fdaf…`) désigne le module de la branche (`9dbcc55c…`) et le commit
    cité porte ce module."""
    f = RACINE / lien.CHEMIN_FICHIER_LIGNE
    if not f.is_file():
        pytest.skip("fichier de la ligne absent de cet arbre")
    r = lien.lire_fichier_ligne(RACINE, {"chemin": lien.CHEMIN_FICHIER_LIGNE, "sha256": SHA_FICHIER_LIGNE})
    assert r["module_sha256"] == SHA_MODULE == empreinte(MODULE) and r["commit"] == COMMIT_CITE
    present = subprocess.run(["git", "-C", str(RACINE), "cat-file", "-e", f"{COMMIT_CITE}^{{commit}}"], capture_output=True)
    if present.returncode != 0:
        pytest.skip("commit cité absent de ce clone")
    import hashlib
    assert hashlib.sha256(lien.octets_au_commit(RACINE, COMMIT_CITE, lien.MODULE_PIECE)).hexdigest() == SHA_MODULE
    with pytest.raises(GardeArret, match="différent de la ligne"):
        lien.lire_fichier_ligne(RACINE, {"chemin": lien.CHEMIN_FICHIER_LIGNE, "sha256": "0" * 64})


def _aires(interface, base, lignes, pos, plis, centres):
    aires, scores = [], []
    for k in (0, 1):
        app = [l for l in lignes if l["condition"] in (pos, "honnete") and plis[l["tache"]] != k]
        lu = [l for l in lignes if l["condition"] in (pos, "honnete") and plis[l["tache"]] == k]
        m = interface.apprendre(base, app, np.array([l["condition"] == pos for l in app], int), centres, pos)
        s = interface.noter(m, lu, centres, f"{pos} (lu)")
        scores.append(s)
        aires.append(aire_sous_courbe(s, np.array([l["condition"] == pos for l in lu], int)))
    return (aires[0] + aires[1]) / 2.0, np.concatenate(scores)


def test_egalite_adaptateur_et_repli_base_a_et_ecarts_declares_base_b(tmp_path):
    a = lien.AdaptateurPieceMC(_depot(tmp_path), exiger_fils=False)
    rep = ad.RepliMC()
    rng = np.random.default_rng(5)
    lignes = _lignes(rng, n_taches=32, facteur={"S50": 1.5, "S100": 3.0})
    plis = partition_plis(sorted({l["tache"] for l in lignes}), 7)
    ca, cr = a.centres(lignes), rep.centres(lignes)
    assert ca == cr                                                          # centres de tâche égaux
    for pos in ("S50", "S100"):
        aa, sa = _aires(a, ad.BASE_A, lignes, pos, plis, ca)
        ar, sr = _aires(rep, ad.BASE_A, lignes, pos, plis, cr)
        assert aa == ar and np.max(np.abs(sa - sr)) <= 1e-8 * (1.0 + np.max(np.abs(sr)))
    # base (B) : (i) mots : lettres seules (pièce) contre suites \w+ contenant une lettre (repli)
    texte = "gpu4 run_x 3x 12 Gate"
    assert a.piece.mots_de(texte) == frozenset({"gpu", "run", "x", "gate"}) and ad.mots(texte) == {"gpu4", "run_x", "3x", "gate"}
    app = [l for l in lignes if l["condition"] in ("S100", "honnete")]
    y = np.array([l["condition"] == "S100" for l in app], int)
    mp, mr = a.apprendre(ad.BASE_B, app, y, ca, "S100"), rep.apprendre(ad.BASE_B, app, y, cr, "S100")
    # (ii) échelle : aucune réduction (pièce) contre traits réduits (repli)
    assert set(mp.interne["moyennes"].values()) == {0.0} and set(mp.interne["ecarts"].values()) == {1.0}
    assert not np.allclose(mr.mu, 0.0)
    # (iii) point (c) : « coût présent » lu sur le texte (pièce) contre les six formes du champ du coût des mesures (repli)
    assert mp.interne["noms"][-4:] == ["cout_normalise", "illisible", "sans_centre", "cout_present"]
    assert ad.TRAITS_B == ("cout_normalise", "illisible", "sans_centre") + ad.FORMES_COUT
    assert all(a.piece.cout_present(l["texte"], __import__("controle_ia.environnements.propositions",
                                                             fromlist=["lire_action"]).lire_action) == l["cout_present"]
               for l in lignes)
    bp, _ = _aires(a, ad.BASE_B, lignes, "S100", plis, ca)
    br, _ = _aires(rep, ad.BASE_B, lignes, "S100", plis, cr)
    assert 0.5 < bp <= 1.0 and 0.5 < br <= 1.0                               # les deux se calculent ; leurs aires diffèrent


def _piece_par_chemin():
    spec = importlib.util.spec_from_file_location("piece_mots_et_cout_essai_bbis", MODULE)
    m = importlib.util.module_from_spec(spec)
    sys.modules["piece_mots_et_cout_essai_bbis"] = m
    spec.loader.exec_module(m)
    return m


@pytest.mark.skipif(not FABRIQUE.is_file(), reason="fabrique factice de la pièce absente de cet arbre")
def test_controle_d_egalite_de_bout_en_bout_piece_jouet_contre_adaptateur(tmp_path):
    """La pièce, jouée en mode jouet sur entrées factices (sa fabrique), écrit `issue-mots-et-cout-t06.json` ; la lecture de B bis
    recalcule les aires de contrôle par l'adaptateur : égalité à 10⁻¹² (écart 0) ; par le repli : base (A) égale, base (B)
    différente (réserve R-MC, sans nœud, comme le texte le veut pour le repli)."""
    sys.path.insert(0, str(RACINE / "scripts"))
    try:
        import fabrique_factice_mots_et_cout_t06_v1 as fab
    finally:
        sys.path.remove(str(RACINE / "scripts"))
    d = _depot(tmp_path)
    for rel in ("prereg/T0.8-base-A-mots-et-cout-v1.md", "prereg/T0.6-organismes-v0-v1.md"):
        (d / rel).parent.mkdir(parents=True, exist_ok=True)
        for s in ("", ".sha256"):
            shutil.copy(RACINE / (rel + s), d / (rel + s))
    git(d, "add", "-A")
    git(d, "commit", "-q", "-m", "textes et registre jouets")
    entrees, run = tmp_path / "entrees", "20261111-151701-t06-reel"
    fab.fabriquer(entrees, run, fab.config_allegee(RACINE), graine=3)
    r = _piece_par_chemin().executer(d, run, "jouet", racine_entrees=entrees, run_id="20261114-160000-mots-et-cout-t06-jouet",
                                     tirages=30, permutations=10)
    issue = json.loads((d / "diag" / r["run_id"] / "issue-mots-et-cout-t06.json").read_text(encoding="utf-8"))
    with np.load(entrees / "donnees" / run / "mesures-t06.npz") as z:
        col = {c: np.array(z[c]) for c in z.files}
    textes = {json.loads(l)["cle"]: json.loads(l)["texte"]
              for l in (entrees / "donnees" / run / "textes-actions-t06.jsonl").read_text(encoding="utf-8").splitlines() if l}
    lignes = []
    for i in range(col["cle"].size):
        l = {c: (v[i].item() if hasattr(v[i], "item") else v[i]) for c, v in col.items()}
        l["cle"], l["tache"], l["condition"] = str(l["cle"]), str(l["tache"]), str(l["condition"])
        l["texte"] = textes[l["cle"]]
        lignes.append(l)
    from controle_ia.harnais.run_harnais_factice import graine_entiere
    man = json.loads((entrees / "runs" / run / "manifeste.json").read_text(encoding="utf-8"))
    plis = partition_plis([l["tache"] for l in lignes], graine_entiere(man["graines"]["partition-taches"]))
    assert issue["plis"] == plis
    a = lien.AdaptateurPieceMC(d, exiger_fils=False)
    doses = (0.25, 0.5, 0.75, 1.0)
    ctrl = ad.controle_egalite(lv.aires_controle_mc(a, lignes, plis, a.centres(lignes), doses), issue, "piece")
    assert ctrl["statut"] == "égalité vérifiée" and not ctrl["noeud"] and set(ctrl["ecarts"]) == {"S25", "S50", "S75", "S100"}
    assert all(e == 0.0 for e in ctrl["ecarts"].values())
    rep = ad.RepliMC()
    aires_r = lv.aires_controle_mc(rep, lignes, plis, rep.centres(lignes), doses)
    assert all(aires_r[dz][0] == issue["doses"][dz]["aire_n029"] for dz in aires_r)            # base (A) : égalité exacte
    cr = ad.controle_egalite(aires_r, issue, "repli")
    assert cr["statut"] == "écart (repli)" and not cr["noeud"] and cr["reserves"]               # base (B) : écart déclaré
