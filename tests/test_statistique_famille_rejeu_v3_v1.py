"""Essais de la statistique de famille du rejeu à blanc v3 (programme
`docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/statistique_famille_rejeu_v3_v1.py`).

Données SYNTHÉTIQUES seulement, fabriquées ici : 94 cartes inventées (identifiants, espèces, voies, notes, listes), dans un
dossier temporaire. Aucune carte réelle, aucun fichier de la course v9 n'est ouvert. Cas sain, artefacts (dans les deux
sens), refus d'empreinte, refus de lire un autre champ que l'espèce, stratification exacte, calibration sous le nul,
non-concluant sur petits effectifs, reproductibilité, R12."""
import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
import pytest

RACINE = Path(__file__).resolve().parents[1]
REL = "docs/notes/organisme-auto-conception-v1/epreuves-v9/juge-selection/statistique_famille_rejeu_v3_v1.py"


def _charger():
    spec = importlib.util.spec_from_file_location("statistique_famille_rejeu_v3_v1", RACINE / REL)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


S = _charger()
SENTINELLE_CONTENU = "TEXTE-DE-CARTE-SYNTHETIQUE-QUI-NE-DOIT-JAMAIS-SORTIR"
SENTINELLE_META = "AUTRE-CHAMP-META-QUI-NE-DOIT-JAMAIS-SORTIR"
ETIQ = {v: k for k, v in S.LIGNEE_DE.items()}
# Voies synthétiques : famille 37 (Opus 22 + Fable 15), autres 57 (Argon 21, Astra 20, Carbon 16), comme la pièce.
PLAN_VOIES = {"I": (10, 10), "P": (20, 30), "N": (7, 17)}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fabriquer(rng, totaux=None):
    """94 cartes synthétiques : {id: (lignée, voie)}, fiches au format de l'orchestrateur (contenu, empreinte, meta)."""
    totaux = totaux or S.TOTAUX_PIECE
    fam = [l for l in ("Opus", "Fable") for _ in range(totaux[l])]
    aut = [l for l in ("Argon", "Astra", "Carbon") for _ in range(totaux[l])]
    rng.shuffle(fam)
    rng.shuffle(aut)
    cartes, ids = {}, set()
    for voie, (nf, na) in PLAN_VOIES.items():
        for lignee in fam[:nf] + aut[:na]:
            while True:
                i = "f" + rng.bytes(6).hex()
                if i not in ids:
                    break
            ids.add(i)
            cartes[i] = (lignee, voie)
        fam, aut = fam[nf:], aut[na:]
    for lignee in fam + aut:                       # reste éventuel (totaux non conformes)
        i = "f" + rng.bytes(6).hex()
        cartes[i] = (lignee, "P")
    fiches = {i: {"contenu": {"titre": f"{SENTINELLE_CONTENU} {k}", "mecanisme": "x " * 50},
                  "empreinte": "0" * 64,
                  "meta": {"case": [k % 4, 1], "fournisseur": "claude", "passe": 1, "origine": "proposition",
                           "proposeur": ETIQ[l], "autre": SENTINELLE_META}}
              for k, (i, (l, _)) in enumerate(cartes.items())}
    return cartes, fiches


def est_fam(l):
    return l in S.FAMILLE_DES_LECTEURS


def selection_liste(cartes, notes, vise, veto, exclues=()):
    """Format « liste de cartes » (comme le lecteur F de la v2)."""
    return {"cartes": [{"id": i, "voie": None if i in exclues else v, "exclue": i in exclues,
                        "notes": {"fine": None if i in exclues else notes[i]}, "dans_nombre_vise": i in vise}
                       for i, (_, v) in sorted(cartes.items())],
            "veto": {"liste": [{"id": i} for i in veto]}}


def selection_objet(cartes, notes):
    """Format « objet par identifiant » (lecteur par programme : voie et D seulement)."""
    return {"par_carte": {i: {"voie": v, "D": notes[i]} for i, (_, v) in cartes.items()}}


CORR_LISTE = {"cartes": "cartes", "id": "id", "voie": "voie", "note": "notes/fine", "exclue": "exclue",
              "nombre_vise": {"drapeau": "dans_nombre_vise"}, "veto": {"liste": "veto/liste", "id": "id"}}
CORR_OBJET = {"cartes": "par_carte", "id": None, "voie": "voie", "note": "D", "nombre_vise": None, "veto": None}


def deposer(tmp, fiches, selections, corr=None, nom="r"):
    d = tmp / nom
    d.mkdir()
    pf = d / "fiches.json"
    pf.write_text(json.dumps(fiches, ensure_ascii=False), encoding="utf-8")
    corr = corr or {"piece": "correspondance synthétique", "ensembles": {
        n: (CORR_OBJET if n == "programme" else CORR_LISTE) for n in selections}}
    pc = d / "correspondance.json"
    pc.write_text(json.dumps(corr, ensure_ascii=False), encoding="utf-8")
    argv = ["--fiches", str(pf), "--sha-fiches", sha(pf), "--correspondance", str(pc), "--sha-correspondance", sha(pc),
            "--sortie", str(d / "sortie.json"), "--resume", str(d / "resume.md"), "--essai-synthetique"]
    for n, sel in selections.items():
        ps = d / f"selection-{n}.json"
        ps.write_text(json.dumps(sel, ensure_ascii=False), encoding="utf-8")
        argv += ["--selection", n, str(ps), sha(ps)]
    return d, argv


def lancer(argv):
    return S.executer(S.analyser_arguments(argv))[0]


# ---------------------------------------------------------------- cas sain : aucun signal, p non petite
def cas_equilibre(cartes):
    """Note maximale et nombre visé à la part exacte de la famille dans chaque voie employée : écart stratifié nul."""
    par = {v: {"f": sorted(i for i, (l, vv) in cartes.items() if vv == v and est_fam(l)),
               "a": sorted(i for i, (l, vv) in cartes.items() if vv == v and not est_fam(l))} for v in PLAN_VOIES}
    haut = par["I"]["f"][:2] + par["I"]["a"][:2] + par["P"]["f"][:2] + par["P"]["a"][:3]       # 4/20·… : 2+2 = 4 attendus
    vise = par["I"]["f"][2:4] + par["I"]["a"][2:4] + par["P"]["f"][2:4] + par["P"]["a"][3:6]
    veto = par["I"]["f"][4:6] + par["I"]["a"][4:6]
    notes = {i: (16 if i in haut else 10) for i in cartes}
    return notes, vise, veto


def test_cas_sain_aucun_signal(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(1))
    notes, vise, veto = cas_equilibre(cartes)
    sel = selection_liste(cartes, notes, set(vise), veto)
    _, argv = deposer(tmp_path, fiches, {"F": sel, "O": sel, "assemblage": sel,
                                         "programme": selection_objet(cartes, notes)})
    out = lancer(argv)
    assert out["especes"]["totaux_conformes_a_la_piece"]
    assert not out["lecture"]["signal_present_quelque_part"]
    for nom in ("F", "O", "assemblage"):
        for liste in ("note_maximale", "nombre_vise"):
            t = out["ensembles"][nom]["listes"][liste]
            assert abs(t["ecart_stratifie"]) < 1e-12
            assert t["p_permutation_bilaterale"] == 1.0 and t["p_exacte_bilaterale"] == pytest.approx(1.0)
            assert t["lecture"]["verdict"] == "absent"
    assert out["ensembles"]["programme"]["listes"]["veto"] == {"sans_objet": "liste absente de la correspondance ou de la sélection"}


def test_cas_sain_aleatoire_p_non_petite(tmp_path):
    rng = np.random.default_rng(7)
    cartes, fiches = fabriquer(rng)
    ids = sorted(cartes)
    notes = {i: int(rng.integers(8, 13)) for i in ids}            # notes indépendantes de l'espèce
    exclues = set(ids[:2])
    reste = ids[2:]
    vise = set(rng.choice(reste, 9, replace=False).tolist())
    veto = rng.choice(reste, 6, replace=False).tolist()
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, vise, veto, exclues)})
    out = lancer(argv)
    assert out["ensembles"]["F"]["non_notees"] == 2 and out["ensembles"]["F"]["population_notees"] == 92
    for liste in ("note_maximale", "nombre_vise", "veto"):
        t = out["ensembles"]["F"]["listes"][liste]
        assert t["p_permutation_bilaterale"] > 0.05, (liste, t["p_permutation_bilaterale"])
        assert t["lecture"]["verdict"] != "signal présent"


# ---------------------------------------------------------------- artefacts : signal planté, dans les deux sens (R4)
@pytest.mark.parametrize("sens", ["plus", "moins"])
def test_artefact_signal_plante(tmp_path, sens):
    cartes, fiches = fabriquer(np.random.default_rng(2))
    cible = (lambda l: est_fam(l)) if sens == "plus" else (lambda l: not est_fam(l))
    favoris = sorted(i for i, (l, _) in cartes.items() if cible(l))
    notes = {i: (16 if i in favoris[:12] else 11) for i in cartes}
    vise = set(favoris[12:25])
    veto = favoris[25:37]                                    # veto assemblé de plusieurs titulaires : 12 cartes
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, vise, veto),
                                         "programme": selection_objet(cartes, notes)})
    out = lancer(argv)
    attendu = "famille des lecteurs sur-représentée" if sens == "plus" else "famille des lecteurs sous-représentée"
    for nom, listes in (("F", ("note_maximale", "nombre_vise", "veto")), ("programme", ("note_maximale",))):
        for liste in listes:
            t = out["ensembles"][nom]["listes"][liste]
            assert t["p_permutation_bilaterale"] < 0.01, (nom, liste, t["p_permutation_bilaterale"])
            assert t["p_exacte_bilaterale"] < 0.01
            assert t["lecture"]["verdict"] == "signal présent" and t["lecture"]["sens"] == attendu
    assert out["lecture"]["signal_present_quelque_part"] and out["lecture"]["audit_R4_declenche"]
    # le descriptif par lignée est rendu, sans test
    lig = out["ensembles"]["F"]["listes"]["note_maximale"]["par_lignee_descriptif"]
    assert set(lig) == set(S.LIGNEES) and not any(k.startswith("p_") for v in lig.values() for k in v)
    assert sum(v["n_liste"] for v in lig.values()) == 12


# ---------------------------------------------------------------- effectifs trop petits : « non concluant », jamais « absent »
def test_petits_effectifs_non_concluant(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(3))
    fam = sorted(i for i, (l, _) in cartes.items() if est_fam(l))
    notes = {i: 10 for i in cartes}
    notes[fam[0]] = notes[fam[1]] = 12                       # note maximale : 2 cartes
    fam_i = sorted(i for i, (l, v) in cartes.items() if est_fam(l) and v == "I" and i not in fam[:2])
    veto = fam_i[:3]                        # 3 cartes de la famille dans la voie I (10 sur 20) : p minimale 0,21 > 0,05
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(), veto)})
    out = lancer(argv)
    L = out["ensembles"]["F"]["listes"]
    assert L["note_maximale"]["lecture"]["verdict"] == "non concluant"
    assert any("moins de 3" in r for r in L["note_maximale"]["lecture"]["raisons_non_concluant"])
    assert L["veto"]["p_minimale_atteignable"] > 0.05
    assert L["veto"]["lecture"]["verdict"] == "non concluant"
    assert L["nombre_vise"]["lecture"]["verdict"] == "non concluant"         # liste vide


def test_totaux_non_conformes_tout_non_concluant(tmp_path):
    tot = dict(S.TOTAUX_PIECE, Opus=21, Argon=22)
    cartes, fiches = fabriquer(np.random.default_rng(4), totaux=tot)
    favoris = sorted(i for i, (l, _) in cartes.items() if est_fam(l))
    notes = {i: (16 if i in favoris[:20] else 11) for i in cartes}
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(favoris[20:29]), favoris[29:35])})
    out = lancer(argv)
    assert not out["especes"]["totaux_conformes_a_la_piece"]
    assert set(out["lecture"]["verdicts"].values()) == {"non concluant"}


# ---------------------------------------------------------------- refus d'empreinte
def test_refus_empreinte_selection(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(5))
    notes, vise, veto = cas_equilibre(cartes)
    d, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)})
    k = argv.index("--selection")
    argv[k + 3] = "0" * 64
    with pytest.raises(S.Refus, match="empreinte"):
        lancer(argv)
    assert not (d / "sortie.json").exists()
    assert S.main(argv) == 2


def test_refus_empreinte_fiches_et_fichier_modifie(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(5))
    notes, vise, veto = cas_equilibre(cartes)
    d, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)})
    (d / "fiches.json").write_text((d / "fiches.json").read_text(encoding="utf-8") + " ", encoding="utf-8")
    with pytest.raises(S.Refus, match="fiches : empreinte"):
        lancer(argv)


def test_refus_hors_essai_si_fiches_pas_celles_de_la_v9(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(5))
    notes, vise, veto = cas_equilibre(cartes)
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)})
    argv.remove("--essai-synthetique")
    with pytest.raises(S.Refus, match="course v9"):
        lancer(argv)


def test_empreinte_illisible_refusee(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(5))
    notes, vise, veto = cas_equilibre(cartes)
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)})
    argv[argv.index("--sha-correspondance") + 1] = "ABC"
    with pytest.raises(S.Refus, match="illisible"):
        lancer(argv)


# ---------------------------------------------------------------- une seule clé lue : l'espèce
class Espion(dict):
    """Enregistrement qui note chaque accès à ses clés."""
    acces = []

    def __getitem__(self, k):
        Espion.acces.append(("get", k))
        return dict.__getitem__(self, k)

    def __contains__(self, k):
        Espion.acces.append(("in", k))
        return dict.__contains__(self, k)

    def get(self, k, d=None):
        Espion.acces.append(("get", k))
        return dict.get(self, k, d)

    def keys(self):
        Espion.acces.append(("keys", None))
        return dict.keys(self)

    def items(self):
        Espion.acces.append(("items", None))
        return dict.items(self)

    def values(self):
        Espion.acces.append(("values", None))
        return dict.values(self)

    def __iter__(self):
        Espion.acces.append(("iter", None))
        return dict.__iter__(self)


def _espionner(o):
    if isinstance(o, dict):
        return Espion({k: _espionner(v) for k, v in o.items()})
    return o


def test_extraction_d_une_seule_cle():
    cartes, fiches = fabriquer(np.random.default_rng(6))
    enregistrements = {i: _espionner(r) for i, r in fiches.items()}      # le premier niveau (identifiants) est un dict simple
    Espion.acces = []
    esp = S.extraire_especes(enregistrements)
    assert esp == {i: l for i, (l, _) in cartes.items()}
    cles = {k for _, k in Espion.acces}
    assert cles == {"meta", "proposeur"}, cles
    assert {op for op, _ in Espion.acces} <= {"get", "in"}               # jamais de parcours d'un enregistrement


@pytest.mark.parametrize("chemin", [("contenu", "titre"), ("meta", "fournisseur"), ("meta",), ("meta", "proposeur", "x"),
                                    ("empreinte",)])
def test_refus_de_lire_un_autre_champ(chemin):
    _, fiches = fabriquer(np.random.default_rng(6))
    with pytest.raises(S.Refus, match="refusé"):
        S.extraire_especes(fiches, chemin=chemin)


def test_etiquette_hors_table_refusee_et_espece_absente_comptee():
    _, fiches = fabriquer(np.random.default_rng(6))
    i0, i1 = sorted(fiches)[:2]
    f2 = json.loads(json.dumps(fiches))
    f2[i0]["meta"]["proposeur"] = "prop-kimi"
    with pytest.raises(S.Refus, match="hors table"):
        S.extraire_especes(f2)
    f3 = json.loads(json.dumps(fiches))
    del f3[i1]["meta"]["proposeur"]
    assert S.extraire_especes(f3)[i1] is None


def test_sortie_sans_texte_ni_espece_par_carte(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(8))
    notes, vise, veto = cas_equilibre(cartes)
    d, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)})
    lancer(argv)
    for f in ("sortie.json", "resume.md"):
        texte = (d / f).read_text(encoding="utf-8")
        assert SENTINELLE_CONTENU not in texte and SENTINELLE_META not in texte
        assert not any(i in texte for i in cartes)                       # aucun identifiant : aucune espèce par carte
        assert (d / (f + ".sha256")).read_text(encoding="utf-8") == f"{sha(d / f)}  {f}\n"


# ---------------------------------------------------------------- stratification exacte
def test_permutations_gardent_les_effectifs_par_voie():
    rng = np.random.default_rng(9)
    strates = ["I"] * 20 + ["P"] * 50 + ["N"] * 24
    lab = np.array([1] * 10 + [0] * 10 + [1] * 20 + [0] * 30 + [1] * 7 + [0] * 17, dtype=np.int8)
    perm = S.permutations_stratifiees(lab, strates, 5000, np.random.default_rng(10))
    assert perm.shape == (5000, 94)
    st = np.array(strates)
    for s in ("I", "P", "N"):
        m = st == s
        assert (perm[:, m].sum(axis=1) == lab[m].sum()).all()           # effectif de la famille par voie, à chaque permutation
        assert (np.sort(perm[:, m], axis=1) == np.sort(lab[m])).all()
        assert len({tuple(r) for r in perm[:200, m]}) > 150              # les étiquettes bougent bien dans la voie
    # une liste prise dans une seule voie : le compte reste dans le support hypergéométrique de cette voie
    idx = np.flatnonzero(st == "N")[:8]
    k = perm[:, idx].sum(axis=1)
    assert k.min() >= max(0, 8 - 17) and k.max() <= 7
    del rng


def test_permutation_et_exact_concordent():
    rng = np.random.default_rng(11)
    strates = ["I"] * 20 + ["P"] * 50 + ["N"] * 24
    lab = np.array([1] * 10 + [0] * 10 + [1] * 20 + [0] * 30 + [1] * 7 + [0] * 17, dtype=np.int8)
    ids = [f"f{k:012x}" for k in range(94)]
    especes = {i: ("Opus" if lab[k] else "Argon") for k, i in enumerate(ids)}
    lst = [ids[k] for k in (0, 1, 2, 3, 12, 20, 21, 22, 23, 24, 25, 40, 70)]
    lu = {"notees": {i: (strates[k], 1.0) for k, i in enumerate(ids)}, "listes": {"veto": lst},
          "note_maximale_valeur": 1.0, "cartes_dans_la_selection": 94, "non_notees": 0}
    r = S.calculer_ensemble("F", lu, especes, rng)
    t = r["listes"]["veto"]
    assert abs(t["p_permutation_bilaterale"] - t["p_exacte_bilaterale"]) < 0.01
    loi = S.loi_exacte([(20, 10, 4), (50, 20, 7), (24, 7, 2)])
    assert float(sum(loi.values())) == pytest.approx(1.0, abs=1e-15)


def test_calibration_sous_le_nul():
    """200 jeux nuls (listes tirées sans lien à l'espèce) : la part de p ≤ 0,05 reste au niveau ou dessous."""
    rng = np.random.default_rng(12)
    strates = ["I"] * 20 + ["P"] * 50 + ["N"] * 24
    lab = [1] * 10 + [0] * 10 + [1] * 20 + [0] * 30 + [1] * 7 + [0] * 17
    ids = [f"f{k:012x}" for k in range(94)]
    especes = {i: ("Fable" if lab[k] else "Astra") for k, i in enumerate(ids)}
    ps = []
    for _ in range(200):
        lst = rng.choice(ids, 12, replace=False).tolist()
        lu = {"notees": {i: (strates[k], 1.0) for k, i in enumerate(ids)}, "listes": {"nombre_vise": lst},
              "note_maximale_valeur": 1.0, "cartes_dans_la_selection": 94, "non_notees": 0}
        ps.append(S.calculer_ensemble("F", lu, especes, rng, n_perm=2000)["listes"]["nombre_vise"]["p_permutation_bilaterale"])
    assert np.mean(np.array(ps) <= 0.05) <= 0.10


def test_holm():
    adj = S.holm({"a": 0.01, "b": 0.04, "c": 0.03})
    assert adj["a"] == pytest.approx(0.03) and adj["c"] == pytest.approx(0.06) and adj["b"] == pytest.approx(0.06)


# ---------------------------------------------------------------- reproductibilité, R12, correspondance
def test_reproductible(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(13))
    rng = np.random.default_rng(14)
    notes = {i: int(rng.integers(8, 13)) for i in cartes}
    sel = {"F": selection_liste(cartes, notes, set(sorted(cartes)[:9]), sorted(cartes)[9:15])}
    a = lancer(deposer(tmp_path, fiches, sel, nom="a")[1])
    b = lancer(deposer(tmp_path, fiches, sel, nom="b")[1])
    assert a["ensembles"] == b["ensembles"] and a["graines"]["entropie"] == str(S.ENTROPIE)


def test_refus_ecrasement(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(15))
    notes, vise, veto = cas_equilibre(cartes)
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)})
    lancer(argv)
    with pytest.raises(S.Refus, match="R12"):
        lancer(argv)


@pytest.mark.parametrize("corr,motif", [
    ({"ensembles": {"G": CORR_LISTE}}, "inconnu"),
    ({"ensembles": {"F": dict(CORR_LISTE, texte="contenu")}}, "non permises"),
    ({"ensembles": {"F": dict(CORR_LISTE, voie="strate_absente")}}, "introuvable"),
    ({"ensembles": {"F": dict(CORR_LISTE, veto={"liste": "veto/liste", "id": "id", "x": 1})}}, "attendu"),
])
def test_correspondance_refusee(tmp_path, corr, motif):
    cartes, fiches = fabriquer(np.random.default_rng(16))
    notes, vise, veto = cas_equilibre(cartes)
    _, argv = deposer(tmp_path, fiches, {"F": selection_liste(cartes, notes, set(vise), veto)}, corr=corr)
    with pytest.raises(S.Refus, match=motif):
        lancer(argv)


def test_identifiant_inconnu_refuse(tmp_path):
    cartes, fiches = fabriquer(np.random.default_rng(17))
    notes, vise, veto = cas_equilibre(cartes)
    sel = selection_liste(cartes, notes, set(vise), veto + ["f000000000000"])
    _, argv = deposer(tmp_path, fiches, {"F": sel})
    with pytest.raises(S.Refus, match="absent des 94"):
        lancer(argv)
