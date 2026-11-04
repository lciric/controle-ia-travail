"""Pilote de l'exposant p, v3 : les quatre retouches de code demandées par la contre-lecture R2 du brouillon 2
(`brouillons/pilote-exposant-p-v1/contre-lecture-v2/contre-lecture-pilote-exposant-p-v2.md`, ligne 188, I1 et I3).
Chaque retouche sur un cas sain et sur un artefact (R5) :
- `analyse.NE_MONTRE_PAS` (couple 17) et `analyse.QUALIF_JUMEAU["au-dessus du jumeau"]` (couple 18), mot pour mot, et
  la lecture du lanceur v3 qui les porte ;
- bloc 0 de `run` : nombre de jetons et dernier sous-jeton de chaque porteur, rapportés (I1) ;
- `go` : règle d'extension du registre des GO, alignée sur la garde de `main` (R-389, I3), avec les quatre essais de la
  contre-lecture, le registre réel de `main` et le même verdict que la garde de `main` ;
- amorce et script d'instance v3 : ceux de la v2 aux seules substitutions déclarées ; étape « verifier » de l'amorce
  sur une extension légitime et sur une extension contradictoire.
"""
from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pytest

from controle_ia.manifeste import graines, verifier_resultat
from controle_ia.pilote_exposant_p.run import TokeniseurJouet
from controle_ia.pilote_exposant_p_v2 import analyse as A2
from controle_ia.pilote_exposant_p_v2 import go as GO2
from controle_ia.pilote_exposant_p_v2 import run as RUN2
from controle_ia.pilote_exposant_p_v2 import stimuli as ST
from controle_ia.pilote_exposant_p_v3 import analyse as A
from controle_ia.pilote_exposant_p_v3 import go as GO
from controle_ia.pilote_exposant_p_v3 import run as RUN

RACINE = Path(__file__).resolve().parents[1]
BROUILLON = RACINE / "brouillons" / "pilote-exposant-p-v1"
CONFIG = BROUILLON / "config-pilote-exposant-p-v2.json"
STIMULI = BROUILLON / "stimuli-pilote-exposant-p-v2.json"
BROUILLON_3 = BROUILLON / "preregistrement-pilote-exposant-p-v1-brouillon3.md"
COUPLES = BROUILLON / "contre-lecture-v2" / "couples-contre-lecture-pilote-exposant-p-v2.json"
MAIN = Path(os.environ.get("DEPOT_MAIN", "/home/user/controle-ia-travail"))
GO_CITE = "GO-2026-11-04-03"
JOUR = date(2026, 11, 5)


def _couple(ancien_contient: str) -> dict:
    cs = [c for c in json.loads(COUPLES.read_text(encoding="utf-8")) if ancien_contient in c["ancien"]]
    assert len(cs) == 1, ancien_contient
    return cs[0]


# --- couples 17 et 18 -------------------------------------------------------------------------------------------

def test_ne_montre_pas_couple_17_sain_et_artefact():
    c17 = _couple("E et R sont faites de fins de phrase courtes")
    b3 = BROUILLON_3.read_text(encoding="utf-8")
    assert c17["nouveau"] in A.NE_MONTRE_PAS and A.NE_MONTRE_PAS in b3            # mot pour mot, couple et brouillon 3
    assert c17["ancien"] in A2.NE_MONTRE_PAS and A2.NE_MONTRE_PAS not in b3        # artefact : la v2 dit encore faux
    for k, t in A.PHRASES.items():
        if k in A.ISSUES_BORNEES:
            assert t.count(A.NE_MONTRE_PAS) == 1 and c17["ancien"] not in t
            assert t == A2.PHRASES[k].replace(A2.NE_MONTRE_PAS, A.NE_MONTRE_PAS)  # rien d'autre ne change
        else:
            assert t == A2.PHRASES[k]
    v = dict(p_er="2.1", ic_er="2 ; 2.2", p_rd="2.0", ic_rd="1.9 ; 2.1", d="+0.1", ic_d="0 ; 0.2", d_wg="+0.9",
             ic_wg="0.7 ; 1.1", brute="égal", cos="0.12", cos_e="0.4", cos_r="0.8", motif="m")
    assert all("{" not in A.phrase(k, **v) for k in A.PHRASES)
    assert A.NE_MONTRE_PAS in A.phrase("égal", **v) and A.NE_MONTRE_PAS not in A2.phrase("égal", **v)
    with pytest.raises(RuntimeError, match="trouvée 0 fois"):                       # borne absente : arrêt, pas de repli
        A._remplacer_borne({"au-dessus": "phrase sans borne"}, A2.NE_MONTRE_PAS, A.NE_MONTRE_PAS)
    with pytest.raises(RuntimeError, match="trouvée 1 fois"):                       # borne hors des issues tranchées
        A._remplacer_borne({"exclu": A2.NE_MONTRE_PAS}, A2.NE_MONTRE_PAS, A.NE_MONTRE_PAS)


def test_qualif_jumeau_couple_18_sain_et_artefact():
    c18 = _couple("« au-dessus du jumeau »")
    dedans = c18["nouveau"].split("(", 1)[1].rsplit(")", 1)[0]
    ancien = c18["ancien"].split("(", 1)[1].rsplit(")", 1)[0]
    assert dedans in A.QUALIF_JUMEAU["au-dessus du jumeau"] and c18["nouveau"] in BROUILLON_3.read_text(encoding="utf-8")
    assert ancien in A2.QUALIF_JUMEAU["au-dessus du jumeau"] and ancien not in A.QUALIF_JUMEAU["au-dessus du jumeau"]
    assert dedans not in A2.QUALIF_JUMEAU["au-dessus du jumeau"]                     # artefact : la v2 en dit trop
    assert {k: v for k, v in A.QUALIF_JUMEAU.items() if k != "au-dessus du jumeau"} == \
        {k: v for k, v in A2.QUALIF_JUMEAU.items() if k != "au-dessus du jumeau"}
    assert all("{" not in t.format(d="+0.1", ic="0 ; 0.2", motif="m") for t in A.QUALIF_JUMEAU.values())
    assert A2.QUALIF_JUMEAU is not A.QUALIF_JUMEAU and A.QUALIF_FAMILLE is A2.QUALIF_FAMILLE


def _plans(p_er=2.4, p_rd=2.0, p_wg=3.0, p_n=2.0, K=8, S=32, M=60):
    """Plans synthétiques (repris de `tests/test_pilote_exposant_p_v2.py`)."""
    rng = np.random.default_rng(5)
    pl = []
    for s in range(S):
        pl.append({"role": "lu", "famille": "ER", "nom": "E×R", "sous_ensemble": s, "garde": True,
                   "p": p_er + 0.05 * rng.standard_normal(), "residu": 0.01})
        pl.append({"role": "lu", "famille": "temoin_lu", "nom": "Wealth×Gender", "sous_ensemble": s, "garde": True,
                   "p": p_wg + 0.05 * rng.standard_normal()})
        pl.append({"role": "lu", "famille": "NR", "nom": "N×R", "sous_ensemble": s, "garde": True,
                   "p": p_n + 0.05 * rng.standard_normal()})
    mu = p_rd + 0.1 * rng.standard_normal(M)
    for k in range(M):
        pl.append({"role": "lu", "famille": "rd_rd", "nom": f"rd{2*k}×rd{2*k+1}", "sous_ensemble": k % S, "garde": True,
                   "p": mu[k] + 0.05 * rng.standard_normal()})
        if k < K:
            pl += [{"role": "lu", "famille": "rd_famille", "nom": f"rd{2*k}×rd{2*k+1}", "sous_ensemble": s,
                    "garde": True, "p": mu[k] + 0.05 * rng.standard_normal()} for s in range(S) if s != k % S]
    return pl


SORTIE = {"instrument": {"valide": True}, "temoin_positif": {"p": 3.0, "ancres_identiques": True},
          "directions_lu": {"cosinus": {"E·R": 0.02, "E_A·E_B": 0.8, "R_A·R_B": 0.7}}}
CFG = {"bootstrap": {"B_difference": 1000}}
GR = graines(RUN.TACHES, 7)


def test_lecture_v3_porte_les_phrases_v3_sain_et_artefact():
    lec = RUN.lire(_plans(), SORTIE, GR, CFG, jouet=True)
    lec2 = RUN2.lire(_plans(), SORTIE, GR, CFG, jouet=True)
    assert lec["issue"] == lec2["issue"] == "au-dessus" and lec["jumeau"]["qualificatif"] == "au-dessus du jumeau"
    assert A.NE_MONTRE_PAS in lec["phrase"] and "telle que construite" in lec["phrase"]
    assert A2.NE_MONTRE_PAS in lec2["phrase"] and "telle que construite" not in lec2["phrase"]   # artefact : v2
    sans_phrase = lambda d: {k: v for k, v in d.items() if k != "phrase"}
    assert sans_phrase(lec) == sans_phrase(lec2)                                   # la lecture elle-même ne change pas
    assert RUN.lire.__code__ is RUN2.lire.__code__ and RUN.principal.__code__ is RUN2.principal.__code__
    for f in (RUN.lire, RUN.analyser, RUN.principal):
        assert f.__globals__["A"] is A and f.__globals__["Pilote"] is RUN.Pilote and f.__globals__["lire"] is RUN.lire
    assert RUN2.lire.__globals__["A"] is A2 and RUN2.principal.__globals__["Pilote"] is RUN2.Pilote


# --- bloc 0 : sous-jetons des porteurs (I1) ---------------------------------------------------------------------

class TokeniseurSousMots(TokeniseurJouet):
    """Tokeniseur d'essai qui coupe aussi aux traits d'union : « chatbot-eval » → chatbot, -, eval (artefact : des
    porteurs distincts finissent par le même sous-jeton)."""

    def _ids(self, t: str) -> list[int]:
        return super()._ids(" ".join(t.replace("-", " - ").split()))

    def convert_ids_to_tokens(self, ids):
        return [f"j{int(i)}" for i in ids]


VOCAB = 2**31        # vocabulaire du tokeniseur d'essai : assez grand pour qu'aucun mot n'en heurte un autre par empreinte


def _stim():
    return json.loads(STIMULI.read_text(encoding="utf-8"))


def test_sous_jetons_des_porteurs_sain_et_artefact():
    stim = _stim()
    n = len(stim["quadruplets"])
    neutres = ST.choisir_neutres(stim, lambda t: len(TokeniseurJouet(VOCAB)(t)["input_ids"]))["choix"]
    sain = RUN.sous_jetons_porteurs(stim, TokeniseurJouet(VOCAB), neutres)
    r = sain["resume"]
    assert r["evaluation"]["porteurs"] == r["deploiement"]["porteurs"] == n and sain["seuil"] is None
    assert r["neutre"]["porteurs"] == sum(1 for v in neutres.values() if v)
    assert r["evaluation"]["derniers_distincts"] == {"F": n, "C": n} and r["evaluation"]["partages"] == []
    assert set(r["evaluation"]["jetons_porteur"]["F"]) == {1}                       # un mot = un jeton (jouet)
    p0 = sain["porteurs"][0]
    assert set(p0) == {"id", "role", "porteur", "registre_F", "registre_C"}
    assert set(p0["registre_F"]) == {"jetons_phrase", "jetons_porteur", "dernier_id", "dernier_sous_jeton"}
    # artefact : sous-jetons ; « eval » termine model-eval, eval, chatbot-eval, LLM-eval ; « benchmark » deux porteurs
    art = RUN.sous_jetons_porteurs(stim, TokeniseurSousMots(VOCAB), None)
    ra = art["resume"]["evaluation"]
    assert ra["derniers_distincts"]["F"] < n and ra["mots_distincts"] == n
    tok = TokeniseurSousMots(VOCAB)
    groupes = {frozenset(g["porteurs"]) for g in ra["partages"] if g["registre"] == "F"}
    assert frozenset({"model-eval", "eval", "chatbot-eval", "LLM-eval"}) in groupes
    assert frozenset({"benchmark", "AI-benchmark"}) in groupes
    g_eval = [g for g in ra["partages"] if g["registre"] == "F" and "LLM-eval" in g["porteurs"]][0]
    assert g_eval["dernier_sous_jeton"] == tok.convert_ids_to_tokens([tok._ids("eval")[-1]])[0]
    assert max(ra["jetons_porteur"]["F"]) == 3 and art["resume"]["neutre"]["porteurs"] == 0
    # deux porteurs au même dernier sous-jeton entre rôles : rapportés aussi
    stim["quadruplets"][0]["porteur_D"] = "family-eval"
    entre = RUN.sous_jetons_porteurs(stim, TokeniseurSousMots(VOCAB), None)["partages_entre_roles"]
    assert any("deploiement:family-eval" in g["porteurs"] and "evaluation:LLM-eval" in g["porteurs"] for g in entre)


def _config_jouet(tmp_path, **modifs) -> Path:
    """Configuration jouet réduite (reprise de `tests/test_pilote_exposant_p_v2.py`)."""
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    cfg["jouet"].update({"grille": {"n": 7}, "ancres": {"par_sous_ensemble": 4, "sous_ensembles": 3, "reserve": 200},
                         "differences_aleatoires": {"k_moy": 4, "paires_disjointes_M": 3}, "isotropes_paires_max": 2,
                         "famille_contrastive_max": 2, "famille_K": 2, "stylise_tirages": 10,
                         "plans": {"temoin": {"WG_sous_ensembles": 2},
                                   "lu": {"ER_sous_ensembles": 3, "WG_sous_ensembles": 3, "NR_sous_ensembles": 3,
                                          "E_Rpapier_sous_ensembles": 1, "moities_sous_ensembles": 1, "E_rd": 1,
                                          "R_rd": 1, "mixtes_rd": 1}}})
    cfg["jouet"]["tolerances_instrument"] = dict(cfg["jouet"]["tolerances_instrument"], seuil_cos=1.01, cos_min_moities=-1.0)
    cfg["bootstrap"]["B_ancres"] = 10
    cfg["bootstrap"]["B_difference"] = 200
    for k, v in modifs.items():
        if k == "tolerances":
            cfg["jouet"]["tolerances_instrument"] = v
        else:
            cfg[k] = v
    ch = tmp_path / "config.json"
    ch.write_text(json.dumps(cfg), encoding="utf-8")
    return ch


def test_bloc_0_au_niveau_du_lanceur_arret_instrument_jouet(depot, tmp_path):
    """Lanceur v3 de bout en bout en mode jouet, sur le chemin le plus court : arrêt « instrument non validé » (code 3,
    tolérances jouet impossibles). Les sous-jetons sont consignés dans les sorties scellées quand même : ils précèdent
    tout passage avant. (Le run jouet complet, 585,8 s sur la machine chargée du 4 novembre, est rapporté dans
    `rapport-retouches-v3-v1.md` ; la phrase v3 de la lecture est couverte par l'essai de `lire` ci-dessus.)"""
    cfg = _config_jouet(tmp_path, tolerances={"tol_p_identiques": 0.0, "tol_intercept_identiques": 0.0,
                                               "intervalle_p_differentes": [20.0, 21.0], "intervalle_isotrope": [20.0, 21.0]})
    run_id = "20261105-000000-jouet-v3-arret"
    code = RUN.principal(["--config", str(cfg), "--stimuli", str(STIMULI), "--run-id", run_id, "--racine", str(depot),
                          "--jouet"])
    assert code == 3
    diag = depot / "diag" / run_id
    s = verifier_resultat(depot, diag / "sorties.json")["resultat"]
    n = len(_stim()["quadruplets"])
    sj = s["porteurs_sous_jetons"]
    assert s["arret_instrument"] and sj["resume"]["evaluation"]["porteurs"] == sj["resume"]["deploiement"]["porteurs"] == n
    assert sj["resume"]["neutre"]["porteurs"] == s["jumeau"]["quadruplets_retenus"] and sj["seuil"] is None
    assert verifier_resultat(depot, diag / "resume.json")["resultat"]["issue"] == "instrument non validé"
    plans = json.loads((diag / "plans.json").read_text())["resultat"]["plans"]
    assert all(x["role"] == "temoin" for x in plans)                               # aucun plan du modèle lu


# --- registre des GO : règle d'extension (I3, R-389) ------------------------------------------------------------

ENTETE = "| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n|---|---|---|---|---|---|---|---|\n"


def _ligne(go=GO_CITE, accorde="2026-11-04", typ="calcul", peri="**Pilote de l'exposant p** (essai)", plafond="30 USD",
           fin="2026-11-18", par="Lazar", ref="essai") -> str:
    return f"| {go} | {accorde} | {typ} | {peri} | {plafond} | {fin} | {par} | {ref} |\n"


EXT = dict(accorde="2026-11-05", peri="extension : plafond relevé (essai)")


def test_go_extension_conforme_du_go_cite_valide():
    texte = ENTETE + _ligne() + _ligne(**EXT, plafond="—")
    r = GO.verifier(texte, GO_CITE, 17, JOUR)
    assert r["valide"] and r["extensions"] == [4] and r["plafond_usd"] == 30.0 and r["ligne_plafond"] == 3
    assert any("illisible" in c for c in r["consignes"])                           # plafond illisible : consigné
    with pytest.raises(GO2.GoInvalide, match="en double"):                         # artefact : la v2 la refusait
        GO2.verifier(texte, GO_CITE, 17, JOUR)


def test_go_extension_qui_releve_le_plafond_lu_sur_l_extension():
    texte = ENTETE + _ligne(plafond="10 USD") + _ligne(**EXT, plafond="40 USD")
    r = GO.verifier(texte, GO_CITE, 17, JOUR)
    assert r["plafond_usd"] == 40.0 and r["ligne_plafond"] == 4
    with pytest.raises(GO.GoInvalide, match="pire cas"):                           # sans l'extension : 10 < 17
        GO.verifier(ENTETE + _ligne(plafond="10 USD"), GO_CITE, 17, JOUR)
    with pytest.raises(GO.GoInvalide, match="pire cas"):                           # extension qui baisse : lue aussi
        GO.verifier(ENTETE + _ligne() + _ligne(**EXT, plafond="12 USD"), GO_CITE, 17, JOUR)
    futur = GO.verifier(ENTETE + _ligne(plafond="20 USD") + _ligne(**(EXT | {"accorde": "2026-11-06"}), plafond="40 USD"),
                        GO_CITE, 17, JOUR)
    assert futur["plafond_usd"] == 20.0 and any("pas encore en vigueur" in c for c in futur["consignes"])


@pytest.mark.parametrize("modif, motif", [
    ({"typ": "dépense"}, "type « dépense »"),
    ({"fin": "2026-12-31"}, "plus lointaine"),
    ({"peri": "plafond relevé, sans le mot (essai)"}, "ne commence pas par « extension »"),
    ({"accorde": "2026-11-03"}, "antérieure"),
    ({"par": "session"}, "non accordée par Lazar"),
    ({"fin": "bientôt"}, "dates illisibles"),
])
def test_go_extension_non_conforme_du_go_cite_refusee(modif, motif):
    texte = ENTETE + _ligne() + _ligne(**(EXT | modif))
    with pytest.raises(GO.GoInvalide, match=f"ligne en conflit.*{motif}") as e:
        GO.verifier(texte, GO_CITE, 17, JOUR)
    assert GO.GARDE_MAIN in str(e.value)


def test_go_doublon_non_conforme_d_un_autre_identifiant_valide_avec_avertissement():
    autre = _ligne(go="GO-2026-10-01-01", accorde="2026-10-01", peri="autre étude", fin="2026-10-30")
    texte = ENTETE + _ligne() + autre + autre                                       # doublon exact : non conforme
    r = GO.verifier(texte, GO_CITE, 17, JOUR)
    assert r["valide"] and any("GO-2026-10-01-01" in a and GO.GARDE_MAIN in a for a in r["avertissements"])
    conforme = ENTETE + _ligne() + autre + _ligne(go="GO-2026-10-01-01", accorde="2026-10-02", peri="extension x",
                                                   fin="2026-10-30")
    r2 = GO.verifier(conforme, GO_CITE, 17, JOUR)
    assert r2["valide"] and not any(GO.GARDE_MAIN in a for a in r2["avertissements"])
    assert any("répétés ailleurs" in a for a in r2["avertissements"])


def _depuis_main(chemin: str) -> str:
    """Fichier vivant de `main` : l'arbre de `main` s'il est sur la machine, sinon `origin/main` du dépôt (instance).
    Ni l'un ni l'autre : échec, pas de saut (R5)."""
    f = MAIN / chemin
    if f.is_file():
        return f.read_text(encoding="utf-8")
    r = subprocess.run(["git", "-C", str(RACINE), "show", f"origin/main:{chemin}"], capture_output=True, text=True)
    if r.returncode != 0:
        pytest.fail(f"{chemin} de main introuvable ({MAIN} absent, origin/main illisible)")
    return r.stdout


def test_go_registre_reel_de_main_extension_legitime_acceptee_contradictoire_refusee():
    reg = _depuis_main("registres/go.md")
    r = GO.verifier(reg, GO_CITE, 17, date(2026, 11, 4))
    assert r["valide"] and r["plafond_usd"] >= 17 and r["periode"] == ["2026-11-04", "2026-11-18"]
    assert not any(GO.GARDE_MAIN in a for a in r["avertissements"])               # aucun doublon non conforme sur main
    legitime = reg.rstrip("\n") + "\n" + _ligne(**EXT, plafond="40 USD", ref="essai : extension légitime")
    rl = GO.verifier(legitime, GO_CITE, 17, JOUR)
    assert rl["valide"] and rl["plafond_usd"] == 40.0 and len(rl["extensions"]) == 1
    contradictoire = reg.rstrip("\n") + "\n" + _ligne(**EXT, fin="2026-12-31", ref="essai : échéance repoussée")
    with pytest.raises(GO.GoInvalide, match="ligne en conflit"):
        GO.verifier(contradictoire, GO_CITE, 17, JOUR)
    with pytest.raises(GO2.GoInvalide, match="en double"):                         # artefact : la v2 refusait la légitime
        GO2.verifier(legitime, GO_CITE, 17, JOUR)


def _garde_main(tmp_path):
    src = tmp_path / "garde_calcul_main.py"
    src.write_text(_depuis_main(".claude/hooks/garde_calcul.py"), encoding="utf-8")
    spec = importlib.util.spec_from_file_location("garde_calcul_main_essai", src)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_meme_verdict_que_la_garde_de_main(tmp_path, capsys):
    """La garde vit hors de `src/` : à défaut d'une lecture partagée, même verdict sur le registre de `main` et sur
    ses variantes. La garde bloque (code 2) sur tout doublon non conforme ; la v3 refuse s'il touche le GO cité et le
    signale en clair (« la garde de calcul de `main` bloquerait la création ») sinon."""
    garde = _garde_main(tmp_path)
    reg = _depuis_main("registres/go.md")
    cas = {"main": reg,
           "extension légitime": reg.rstrip("\n") + "\n" + _ligne(**EXT, plafond="40 USD"),
           "extension contradictoire": reg.rstrip("\n") + "\n" + _ligne(**EXT, fin="2026-12-31"),
           "doublon ailleurs": reg.rstrip("\n") + "\n" + _ligne(go="GO-2026-10-01-01", peri="x") * 2}
    for i, (nom, texte) in enumerate(cas.items()):
        f = tmp_path / f"registre-{i}.md"
        f.write_text(texte, encoding="utf-8")
        try:
            lu = garde.lire_go(f)
            bloque = False
        except SystemExit as e:
            assert e.code == 2
            bloque, lu = True, None
        try:
            r = GO.verifier(texte, GO_CITE, 17, JOUR)
            v3_signale = any(GO.GARDE_MAIN in a for a in r["avertissements"])
        except GO.GoInvalide as e:
            r, v3_signale = None, GO.GARDE_MAIN in str(e)
        assert bloque == v3_signale, nom
        if lu is not None:
            g = lu[GO_CITE]
            assert r["valide"] and [str(g["accorde"]), str(g["echeance"])] == r["periode"]
            assert g["type"] == "calcul" and g["par"] == "Lazar" and len(g["extensions"]) == len(r["extensions"])
    capsys.readouterr()


# --- amorce et script d'instance v3 -----------------------------------------------------------------------------

SUBSTITUTIONS = {
    "amorce_instance_pilote_exposant_p": [
        ("#!/usr/bin/env bash\n", "#!/usr/bin/env bash\n# Version 3 (brouillon 3 ; R12 : la v2 n'est pas modifiée) : GO vérifié par "
         "`controle_ia.pilote_exposant_p_v3.go`\n# (règle d'extension R-389 de la garde de `main` ; contre-lecture R2 du "
         "brouillon 2, I3) ; lance le script d'instance v3.\n"),
        ("pilote_exposant_p_v2.go", "pilote_exposant_p_v3.go"),
        ("amorce_instance_pilote_exposant_p_v2.sh", "amorce_instance_pilote_exposant_p_v3.sh"),
        ("pilote_exposant_p_instance_v2.sh", "pilote_exposant_p_instance_v3.sh"),
        ("<MODE>-v2", "<MODE>-v3"), ("-v2}", "-v3}")],
    "pilote_exposant_p_instance": [
        ("#!/usr/bin/env bash\n", "#!/usr/bin/env bash\n# Version 3 (brouillon 3 ; R12 : la v2 n'est pas modifiée) : lanceur "
         "`controle_ia.pilote_exposant_p_v3.run` (phrases des\n# couples 17 et 18, sous-jetons des porteurs au bloc 0) ; essais "
         "v3 ajoutés ; branche par défaut en -v3. Le reste est la v2.\n"),
        ("pilote_exposant_p_v2.run", "pilote_exposant_p_v3.run"),
        ("amorce_instance_pilote_exposant_p_v2.sh", "amorce_instance_pilote_exposant_p_v3.sh"),
        ("pilote_exposant_p_instance_v2.sh", "pilote_exposant_p_instance_v3.sh"),
        ("tests/test_script_pilote_exposant_p_v2.py\n                 tests/test_manifeste.py",
         "tests/test_script_pilote_exposant_p_v2.py\n                 tests/test_pilote_exposant_p_v3.py tests/test_manifeste.py"),
        ("ETUDE=$ETUDE (v2)", "ETUDE=$ETUDE (v3)"), ("<MODE>-v2", "<MODE>-v3"), ("-v2}", "-v3}")],
}


def appliquer(nom: str, texte: str) -> str:
    for a, b in SUBSTITUTIONS[nom]:
        assert a in texte, (nom, a)
        texte = texte.replace(a, b)
    return texte


@pytest.mark.parametrize("nom", sorted(SUBSTITUTIONS))
def test_scripts_v3_egaux_aux_v2_aux_substitutions_declarees(nom):
    v2 = (RACINE / "scripts" / f"{nom}_v2.sh").read_text(encoding="utf-8")
    v3 = (RACINE / "scripts" / f"{nom}_v3.sh").read_text(encoding="utf-8")
    assert v3 == appliquer(nom, v2)
    assert "controle_ia.pilote_exposant_p_v2." not in v3 and "pilote_exposant_p_v2.sh" not in v3
    assert "pilote_exposant_p_instance_v2" not in v3


def _amorce_verifier(tmp_path, texte: str):
    reg = tmp_path / "go.md"
    reg.write_text(texte, encoding="utf-8")
    env = {k: os.environ[k] for k in ("PATH", "LANG", "LC_ALL", "TMPDIR") if k in os.environ}
    env.update(AMORCE_ETAPE="verifier", GO_ID=GO_CITE, REGISTRE_GO=str(reg), DATE_GO=str(JOUR))
    return subprocess.run(["bash", str(RACINE / "scripts" / "amorce_instance_pilote_exposant_p_v3.sh")], env=env,
                          capture_output=True, text=True, timeout=120)


def test_amorce_v3_verifier_extension_legitime_et_contradictoire(tmp_path):
    ok = _amorce_verifier(tmp_path, ENTETE + _ligne() + _ligne(**EXT, plafond="40 USD"))
    assert ok.returncode == 0 and "vérifié" in ok.stdout and '"plafond_usd": 40.0' in ok.stdout, ok.stdout + ok.stderr
    ko = _amorce_verifier(tmp_path, ENTETE + _ligne() + _ligne(**EXT, fin="2026-12-31"))
    assert ko.returncode == 1 and "ligne en conflit" in ko.stdout and "aucune instance" in ko.stdout, ko.stdout


def test_go_v3_sans_dependance_hors_bibliotheque_standard():
    """L'amorce appelle `go` avant toute installation : le module et ses importations n'appellent que la bibliothèque
    standard (numpy et scipy absents du processus fils)."""
    code = ("import sys; sys.modules['numpy'] = None; sys.modules['scipy'] = None; "
            "from controle_ia.pilote_exposant_p_v3 import go; print(go.GARDE_MAIN)")
    r = subprocess.run([sys.executable, "-B", "-c", code], env={**os.environ, "PYTHONPATH": str(RACINE / "src")},
                       capture_output=True, text=True, timeout=60)
    assert r.returncode == 0, r.stderr
