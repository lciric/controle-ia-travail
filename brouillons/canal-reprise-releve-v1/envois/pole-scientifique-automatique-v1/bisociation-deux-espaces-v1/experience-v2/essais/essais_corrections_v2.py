"""Essais des corrections v2 (décisions de Lazar R-600 ; contre-lecture du code `contre-lecture-code-experience-v2-v1.md`).
Chaque correction a un cas sain et un artefact qui échoue vraiment. Plomberie seulement : mondes jouets, ou
RACINE_VALIDATION aux indices ≥ 950 000 (hors de toute plage du § 7) ; RACINE n'est jamais employée ; aucun contraste de
décision, aucune moyenne de Δ(N, ·), aucun résultat de V1 à V9 n'est calculé ni lu (seuls des égalités, des comptes,
des exceptions et le signe « non nul » d'une variation de cosinus de plomberie).
Usage : PYTHONPATH=<dépôt>/src python3 -B -m pytest -q -p no:cacheprovider essais/essais_corrections_v2.py
"""
import numpy as np
import pytest

from jouets_v2 import monde_jouet

import bras_v2 as br
import graines_v2 as gr
import invocation_unique_v2 as inv
import lecture_v2 as le
import mesures_v2 as ms
import monde_v2 as mo
import noyaux_v2 as ny
import validation_v2 as va
from controle_ia.gardes import GardeArret

RV = gr.RACINE_VALIDATION
K_REPLANT, K_JUMELLE, K_INERTES, K_CONC = 952_000, 953_000, 954_000, 955_000


# --- Q-01 (b) : replanter sur le même monde de base ----------------------------------------------------------

def _premiers_replantes(n, k0=K_REPLANT, cond="M_bien"):
    out = []
    for i in range(k0, k0 + 400):
        L = mo.generer(cond, RV, i).latent(mo.JETON_MESURE)
        if L.replantations > 0 and L.tentatives == 0:
            out.append((i, L))
            if len(out) == n:
                return out
    raise AssertionError("aucun monde replanté trouvé sur 400 graines d'essai")


def test_q01_sain_replantation_garde_le_monde_de_base():
    for i, L in _premiers_replantes(3):
        f, champ, groupe, arts = mo.monde_de_base("M_bien", RV, i, tentative=0)
        assert L.n_champs == f
        assert mo.signature_base(L.champ, L.groupe, L.arts) == mo.signature_base(champ, groupe, arts)
        assert len(L.plantes) == 18 and len(L.echecs_plantation) == L.replantations


def test_q01_artefact_regeneration_entiere_change_le_monde_de_base(monkeypatch):
    # la comparaison a du pouvoir : le monde de base d'une autre tentative diffère ; et l'ancienne règle (régénération
    # entière dès le premier échec) donne, sur les mêmes graines, un monde dont la base n'est plus celle de la tentative 0
    cas = _premiers_replantes(3)
    for i, L in cas:
        assert mo.signature_base(*mo.monde_de_base("M_bien", RV, i, tentative=1)[1:]) != \
            mo.signature_base(L.champ, L.groupe, L.arts)
    monkeypatch.setattr(mo, "MAX_REPLANTATIONS", 0)
    differe = 0
    for i, _ in cas:
        L0 = mo.generer("M_bien", RV, i).latent(mo.JETON_MESURE)
        assert L0.tentatives > 0 and L0.replantations == 0
        differe += mo.signature_base(L0.champ, L0.groupe, L0.arts) != \
            mo.signature_base(*mo.monde_de_base("M_bien", RV, i, tentative=0)[1:])
    assert differe == len(cas)


def test_q01_inertes_replantes_comme_M_bien_et_SP_sans_plantation():
    # M_inertes replante sous le code 1, donc garde les latents de M_bien même après replantation ; SP ne plante rien.
    # (L'identité bit à bit des mondes sans échec avec le code d'avant est vérifiée à part :
    # plomberie-corrections-v2/identite_ancien_nouveau_v1.py.)
    for i, _ in _premiers_replantes(2):
        assert mo.empreinte_latents(mo.generer("M_bien", RV, i)) == mo.empreinte_latents(mo.generer("M_inertes", RV, i))
    L = mo.generer("SP", RV, K_REPLANT).latent(mo.JETON_MESURE)
    assert L.replantations == 0 and L.plantes == []


def test_q01_cles_de_replantation_cinq_elements_sans_collision():
    ss = gr.sequence(RV, 1, 7, gr.ROLE_MONDE, tentative=0, replantation=2)
    assert tuple(ss.spawn_key) == (1, 7, 0, 0, 2)
    etats = {tuple(gr.sequence(RV, 1, 7, 0, **kw).generate_state(4)) for kw in
             ({}, {"tentative": 1}, {"tentative": 0, "replantation": 1}, {"tentative": 1, "replantation": 1},
              {"tentative": 0, "replantation": 2})}
    assert len(etats) == 5
    for kw in ({"replantation": 0}, {"replantation": -1}):
        with pytest.raises(GardeArret):
            gr.sequence(RV, 1, 7, gr.ROLE_MONDE, **kw)
    with pytest.raises(GardeArret):
        gr.sequence(RV, 1, 7, gr.ROLE_OBS_CONCEPTS, replantation=1)      # rôle autre que 0 : refusé


def test_q01_taux_rapportes_par_nombre_de_champs_et_regeneration_soumise_a_S11():
    lignes = [{"exclu": None, "tentatives": 0, "replantations": 1 if i < 30 else 0, "n_champs": 2 + i % 3, "bras": {}}
              for i in range(100)]
    r = ms.verifier_taux(lignes, "M_bien")                           # 30 % de replantés : rapporté, sans arrêt
    assert r["taux_replantes"] == 0.30 and r["par_nombre_de_champs"]["2"]["n"] == 34
    lignes[0]["tentatives"] = lignes[1]["tentatives"] = lignes[2]["tentatives"] = 1
    with pytest.raises(GardeArret):                                  # 3 % de régénérations entières : arrêt (S11)
        ms.verifier_taux(lignes, "M_bien")


# --- Q-04 « copie » : la jumelle de V4 ------------------------------------------------------------------------

def test_q04_sain_copie_change_le_cosinus_des_paires_plantees_sur_3_mondes():
    for m in range(K_JUMELLE, K_JUMELLE + 3):
        w, j = mo.generer("M_bien", RV, m), mo.generer("M_bien", RV, m, surcharge={"jumelle": True})
        assert mo.empreinte_latents(w) == mo.empreinte_latents(j)
        assert w.obs.etiq_co == j.obs.etiq_co and w.obs.etiq_op == j.obs.etiq_op
        L = w.latent(mo.JETON_MESURE)
        change = [w.obs.cos[p["a"], p["b"]] != j.obs.cos[p["a"], p["b"]] for p in L.plantes]
        assert all(change)                                           # chaque paire plantée bouge (valeurs non lues)
        # règle déterministe : l'article de plus grand indice prend les mots propres du domaine de l'autre
        Lj = j.latent(mo.JETON_MESURE)
        for p in Lj.plantes:
            bas, haut = min(p["a"], p["b"]), max(p["a"], p["b"])
            assert Lj.arts[haut]["dom_mots"] == Lj.arts[bas]["dom"] and "dom_mots" not in Lj.arts[bas]


def _echanger(sac, d_de, d_vers):
    return [f"d{d_vers}_" + x[len(f"d{d_de}_"):] if x.startswith(f"d{d_de}_") else x for x in sac]


def test_q04_artefact_lecture_echange_laisse_le_cosinus_inchange():
    # l'ancienne lecture (R-585) reconstituée dans l'essai : les deux articles d'un pont échangent leurs mots propres
    for m in range(K_JUMELLE, K_JUMELLE + 3):
        w = mo.generer("M_bien", RV, m)
        L = w.latent(mo.JETON_MESURE)
        assert np.array_equal(np.asarray(mo.mo._cosinus(L.arts, "tf")), w.obs.cos)   # recalcul fidèle (sain)
        arts = [dict(a) for a in L.arts]
        for pl in L.plantes:
            da, db = L.arts[pl["a"]]["dom"], L.arts[pl["b"]]["dom"]
            arts[pl["a"]]["sac_domaine"] = _echanger(L.arts[pl["a"]]["sac_domaine"], da, db)
            arts[pl["b"]]["sac_domaine"] = _echanger(L.arts[pl["b"]]["sac_domaine"], db, da)
        cos_e = np.asarray(mo.mo._cosinus(arts, "tf"))
        assert not np.array_equal(cos_e, w.obs.cos)                  # l'échange a bien changé des cosinus…
        assert all(abs(cos_e[pl["a"], pl["b"]] - w.obs.cos[pl["a"], pl["b"]]) < 1e-12 for pl in L.plantes)  # …pas ceux des ponts
    # et le seuil V4 échoue sur une variation nulle (artefact qui échoue vraiment)
    ok = {"V1": {"meme": 0.54, "proche": 0.28, "eloigne": 0.03}, "V3": 0.05, "V5": {"ecart_max": 0.2}, "V6": 7.0,
          "plafond_oracle": 0.5, "V2": {"F": 0.05}}
    r = {"M_bien": ok, "M_moyen": ok, "jumelles": {"concordance": 1.0, "variation_cos": 0.0}}
    assert va.evaluer_seuils(r)["V4"] is False
    with pytest.raises(GardeArret):
        va.v4_jumelles(RV, range(K_JUMELLE, K_JUMELLE + 1), lecture="echange_ponts")


# --- M_inertes : latents bit à bit pendant l'invocation et dans V9 --------------------------------------------

def _lignes(cond, indices, surcharge=None):
    out = []
    for i in indices:
        w = mo.generer(cond, RV, i, surcharge)
        out.append(ms.executer_monde(w, cond, RV, i, ["c"]))
    return out


def test_inertes_sain_latents_egaux_monde_par_monde():
    idx = range(K_INERTES, K_INERTES + 5)
    assert ms.verifier_inertes_lignes(_lignes("M_bien", idx), _lignes("M_inertes", idx)) == 5


def test_inertes_artefact_code_12_aux_roles_0_a_3_ou_indice_manquant_arrete():
    idx = range(K_INERTES, K_INERTES + 5)
    bien = _lignes("M_bien", idx)
    faux = _lignes("M_inertes", idx, surcharge={"_code_latent_force": gr.CODES_CONDITION["M_inertes"]})
    with pytest.raises(GardeArret):
        ms.verifier_inertes_lignes(bien, faux)
    with pytest.raises(GardeArret):
        ms.verifier_inertes_lignes(bien[:-1], _lignes("M_inertes", idx))


def test_inertes_invocation_artefact_arret_avant_le_fichier_de_M_inertes(tmp_path, monkeypatch):
    from essais_complements_v2 import Executeur, _etape1_factice, _manifeste_sans_git, _petits_nombres, \
        _prerequis_factices
    _petits_nombres(monkeypatch)
    monkeypatch.setattr(ms, "verifier_reproduction", lambda c, m: {})
    monkeypatch.setattr(ms, "verifier_plafond_oracle", lambda m, c: True)

    def lancer(run_id, derive):
        ex = Executeur(tmp_path)
        base = ex.__call__

        def executer(cond, racine, indices, **kw):
            lignes = base(cond, racine, indices, **kw)
            if cond == "M_inertes" and derive:
                lignes[2]["empreinte_latents"] = "autre"
            return lignes
        return inv.invocation(tmp_path, run_id, 2, "v", "r", None, executer=executer,
                              etape1_fn=_etape1_factice({"M_bien": 11.0, "M_moyen": 11.0}),
                              creer_manifeste=_manifeste_sans_git, verifier_prerequis_fn=_prerequis_factices)
    res = lancer("20261101-000010-essai", derive=False)                # cas sain : passe (code 16 par défaut)
    assert any("resultats-M_inertes" in f for f in res["fichiers"])
    with pytest.raises(GardeArret):
        lancer("20261101-000011-essai", derive=True)
    ecrits = [p.name for p in tmp_path.rglob("resultat*") if "000011" in str(p)]
    assert any("M_bien" in n for n in ecrits)                        # la recherche voit bien les fichiers du run…
    assert not any("M_inertes" in n for n in ecrits)                 # …et aucun résultat de M_inertes n'est écrit


def test_inertes_v9_sain_et_artefact(monkeypatch):
    f = {**br.FONCTIONS}
    assert isinstance(va.v9_j_miroirs(RV, range(K_INERTES, K_INERTES + 3), fonctions=f), bool)
    vrai = mo.generer

    def generer_fautif(cond, racine, i, surcharge=None):
        if cond == "M_inertes":
            return vrai(cond, racine, i, {"_code_latent_force": gr.CODES_CONDITION["M_inertes"]})
        return vrai(cond, racine, i, surcharge)
    monkeypatch.setattr(mo, "generer", generer_fautif)
    with pytest.raises(GardeArret):
        va.v9_j_miroirs(RV, range(K_INERTES, K_INERTES + 3), fonctions=f)


# --- garde propre du glouton (pivot ≤ 10⁻¹² × max), éprouvée seule ------------------------------------------------

L_PIVOT_MINUSCULE = [[1.0, 1.0], [1.0, 1.0 + 1e-14]]   # défini positif (pivots 1 et ≈ 1e-14 > 0), pivot relatif < 1e-12


def test_glouton_sain_noyau_defini_positif_ordinaire():
    choisis, non_pos = ny.glouton_paires([[1.0, 0.5], [0.5, 1.0]], 2)
    assert sorted(choisis) == [0, 1] and non_pos == 0


def test_glouton_artefact_pivot_sous_le_seuil_relatif_leve_par_la_garde_propre(monkeypatch):
    ny.cholesky(L_PIVOT_MINUSCULE)                                  # la pièce A accepte ce noyau : ce n'est pas elle
    with pytest.raises(ny.NonDefiniePositive, match="pivot choisi"):
        ny.glouton_paires(L_PIVOT_MINUSCULE, 2)
    monkeypatch.setattr(ny, "SEUIL_PIVOT_RELATIF", 0.0)            # sans la garde propre, le glouton passerait
    assert len(ny.glouton_paires(L_PIVOT_MINUSCULE, 2)[0]) == 2


# --- déclencheurs d'audit : identités déclarées d'avance, concordance avec la vérité ------------------------------

def _decl(identites=None, concordance=None):
    c = {("N-b", X): {"estimation": 0.0} for X in le.X2} | {("N-a", X): {"ub95": 1.0} for X in le.X2}
    return le.declencheurs_audit(c, {"A3": True, "gain_controle": False}, {"M_bien": 0.1}, {"M_bien": 0.9},
                                 identites or {}, False, None, concordance)


def test_identites_sain_declarees_ou_hors_liste_ne_declenchent_pas():
    assert _decl({"V_concepts_absents": ["N_beta0"]}) == []
    assert _decl({"M_bien": ["N_q", "oracle"]}) == []
    dec, rap = le.identites_audit({"V_concepts_absents": ["N_beta0"], "M_bien": ["N_q"]})
    assert dec == {} and rap == {"V_concepts_absents": ["N_beta0"], "M_bien": ["N_q"]}


def test_identites_artefact_non_declarees_declenchent():
    assert any("identités" in d for d in _decl({"M_bien": ["N_beta0"]}))
    assert any("identités" in d for d in _decl({"V_concepts_absents": ["b"]}))
    assert any("identités" in d for d in _decl({"M_moyen": ["N_global"]}))


def _monde_concordance(etiquettes):
    w = monde_jouet([0, 1], [{"op:x"}, {"op:x"}], vrais=[(0, 1)])
    L = w.latent(mo.JETON_MESURE)
    L.arts = [{"dom": 0, "etiq_co": etiquettes, "fonds": [1, 2], "rares": {3}, "moyeu_concept": False},
              {"dom": 1, "etiq_co": {}, "fonds": [4], "rares": set(), "moyeu_concept": True}]
    return L


def test_concordance_sain_calcul_a_la_main_et_declencheur():
    L = _monde_concordance({"F1": "vrai", "R3": "vrai", "F5": "parasite", "H": "fuite"})
    assert ms.concordance_verite_monde(L) == (2, 4)
    assert ms.concordance_verite([{"exclu": None, "concordance_verite": (2, 4)},
                                  {"exclu": "x", "concordance_verite": (9, 9)},
                                  {"exclu": None, "concordance_verite": (8, 8)}]) == 10 / 12
    assert _decl(concordance={"M_bien": 10 / 12}) == []
    w = mo.generer("M_bien", RV, K_CONC)
    v, t = ms.concordance_verite_monde(w.latent(mo.JETON_MESURE))
    assert 0 < v <= t                                               # grandeur calculée sur un monde réel (plomberie)
    assert ms.concordance_verite_monde(mo.generer("NR_bien", RV, K_CONC).latent(mo.JETON_MESURE)) is None


def test_concordance_artefact_etiquettes_parfaites_declenchent():
    L = _monde_concordance({"F1": "vrai", "F2": "vrai", "R3": "vrai"})
    assert ms.concordance_verite_monde(L) == (3, 3)
    assert "concordance des étiquettes avec la vérité > 0,99" in _decl(concordance={"M_bien": 1.0, "INV": 0.5})
    assert "concordance des étiquettes avec la vérité > 0,99" in _decl(concordance=0.995)
    with pytest.raises(GardeArret):
        ms.concordance_verite_monde(_monde_concordance({"X9": "vrai"}))


# --- vue observée sans le nom de la condition ---------------------------------------------------------------------

def test_obs_sain_sans_condition():
    w = mo.generer("SP", RV, K_CONC)
    assert "condition" not in mo.Obs.__slots__
    with pytest.raises(mo.AccesLatent):
        w.obs.condition


def test_obs_artefact_bras_qui_lit_la_condition_leve():
    def bras_curieux(obs, rng, aux):
        return [] if obs.condition == "SP" else list(obs.valides[:12])
    w = mo.generer("M_inertes", RV, K_CONC)
    with pytest.raises(mo.AccesLatent):
        ms.executer_monde(w, "M_inertes", RV, K_CONC, ["N"], fonctions={**br.FONCTIONS, "N": bras_curieux})


# --- addendum d'écarts scellé avant la validation et l'invocation -------------------------------------------------

def test_addendum_sain_scelle_accepte(tmp_path):
    from controle_ia.scellement import sceller
    (tmp_path / "prereg").mkdir()
    a = tmp_path / "prereg" / inv.ADDENDUM
    # copie du texte fixé par EMPREINTE_ADDENDUM (CLA-04), scellée dans tmp_path seulement
    a.write_bytes((inv.DEPOT / "prereg" / inv.ADDENDUM).read_bytes())
    sceller(a)
    assert len(inv.exiger_addendum_scelle(tmp_path)) == 64


def test_addendum_artefact_absent_non_scelle_ou_modifie_refuse(tmp_path):
    from controle_ia.scellement import sceller
    with pytest.raises(GardeArret):
        inv.exiger_addendum_scelle(tmp_path)                         # absent
    (tmp_path / "prereg").mkdir()
    a = tmp_path / "prereg" / inv.ADDENDUM
    a.write_text("brouillon\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        inv.exiger_addendum_scelle(tmp_path)                         # présent, non scellé
    sceller(a)
    a.write_text("brouillon modifié après scellement\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        inv.exiger_addendum_scelle(tmp_path)                         # modifié après scellement
