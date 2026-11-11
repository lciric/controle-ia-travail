"""Essais R5 des gardes v4 (contre-lecture courte de la v3 `b6ca886d…`, R-2307) : cas de la v3 repris au format v4 du
vérificateur, et CLC3-01 (commentaire de documentation, imbrication k12), CLC3-02 (trous), CLC3-03 (imports exacts),
CLC3-06 (constantes de l'agent citées, noms hors ASCII), CLC3-11 (k07, k14, k15)."""
import json
from pathlib import Path

import pytest

from controle_ia.lean_essai import gardes_lean_v4 as G

ARTEFACTS = Path(__file__).resolve().parents[1] / "scripts" / "lean_essai_d1a_v4" / "artefacts_r5_v4"
NONCE = "0123456789abcdef0123456789abcdef"
TEXTUELLES = ("G-L2", "G-L3", "G-L3+", "G-L4", "G-L6")


def lire(nom):
    return (ARTEFACTS / nom).read_text(encoding="utf-8")


SAIN = lire("sain_v1.lean")


# ---- CLC2-01 : lexique ------------------------------------------------------------------------------------------------------

ATTAQUES = [
    "def T := { x : Int //-x = 0 }\naxiom cachee : False\n-- -/\n",
    "theorem t (x : Int) (p : Prop) (h : p) : p \\/-1 = x := Or.inl h\naxiom cachee : False\n-- -/\n",
    "def f : Id Int := do let x <--(1 : Int); pure x  @[init] def g : IO Unit := pure ()\n",
    'theorem «/-» : True := trivial\naxiom x : False\ntheorem «-/» : True := trivial\n',
    "def c := 'a'r\"\\\"\naxiom x : False -- \"\n",
    "def c := 1'\"'\naxiom x : False -- \"\n",
    "def c := x»\n",                      # « seul (mutation n02 de la contre-lecture courte)
    'def c := "a"--b\n',
    "def c := (x)'a'\n",
    "def c := é\"x\"\n",                  # é n'est pas une lettre pour Lean : le « \" » qui suit est collé
    'def c := "a"x\n',                    # littéral suivi d'un identifiant collé (seule la règle de fin de littéral le voit)
]


@pytest.mark.parametrize("src", ATTAQUES)
def test_lexique_v3_artefacts(src):
    with pytest.raises(G.ErreurLexicale):
        G.masquer(src)
    m = G.analyser_texte(src, 1)["motifs"]
    assert all(m[g] for g in TEXTUELLES), m


def test_lexique_v3_sains():
    src = ("-- « axiom » en commentaire\ntheorem h' (x₁' : ℝ) (s : Set ℝ) (f : ℝ → ℝ) : f '' s = f '' s ∧ f ⁻¹' s = f ⁻¹' s"
           " := ⟨rfl, rfl⟩\ndef paire := ⟨\"a\", 'b'⟩\ndef l := [\"a\",\"b\"]\ndef n := Nat.succ 1 -- fin\n"
           "def x := y--c\ndef r := r#\"brute \"sorry\" \"#\n#print \"x\"\n")
    m = G.masquer(src)
    assert "sorry" not in m and "axiom" not in m and "h'" in m and "⁻¹'" in m and "''" in m
    assert len(m) == len(src)
    assert all(not v for v in G.analyser_texte(SAIN, 2)["motifs"].values())


def test_predicats_d_identifiant_de_lean():
    assert G._debut_ident("ℝ") and G._debut_ident("π") and G._debut_ident("℘") and G._debut_ident("_")
    assert not G._debut_ident("λ") and not G._debut_ident("Σ") and not G._debut_ident("é") and not G._debut_ident("1")
    assert G._suite_ident("₁") and G._suite_ident("'") and G._suite_ident("9") and not G._suite_ident("¹")


# ---- CLC2-02 et CLC2-08 (n09, n10) : texte, seconde ligne --------------------------------------------------------------------

@pytest.mark.parametrize("ligne", [
    "simproc s (False) := fun _ => pure .continue", "dsimproc_decl d (x) := fun _ => pure .continue",
    "def t : Lean.Elab.Tactic.TacticM Unit := pure ()", "def m : MetaM Unit := pure ()", "def i : IO Unit := pure ()",
    "theorem a : True := by aesop (add safe tactic monTac)", "theorem a : True := by_elabq (pure q(trivial))",
    "set_option   debug.skipKernelTC true", "def s := skipKernelTC", "import Lean.Elab", "import Mathlib Lean",
    "def u := unsafeBaseIO (pure 1)",
])
def test_gl3_plus_mots_v3(ligne):
    m = G.analyser_texte(ligne + "\n", 1)["motifs"]
    assert m["G-L3+"] or m["G-L3"], m


def test_gl3_plus_desactivable_et_imports_permis():
    assert not G.analyser_texte("import Mathlib.Tactic\nimport Aesop\n", 1)["motifs"]["G-L3+"]
    assert not G.analyser_texte("def i : IO Unit := pure ()\n", 1, supplementaires=False)["motifs"]["G-L3+"]


# ---- garde de fond : sortie du vérificateur du noyau -------------------------------------------------------------------------

def lignes_noyau(m=2, rejeu=True, erreur="", axiomes=None, genres=None, aller=None, absents=(), constantes=None,
                 definitions=None, imports_permis=True, nonce=NONCE, doublon=None, extra_avant_fin="", modules=None,
                 champs=None):
    axiomes, genres, aller, champs = axiomes or {}, genres or {}, aller or {}, champs or {}
    noms = [f"etape_{i}" for i in range(1, m + 1)] + ["enonce_item"]
    out = [{"type": "imports", "modules": modules if modules is not None else ["Init", "Mathlib"], "permis": imports_permis}]
    if imports_permis:
        cs = constantes if constantes is not None else [(n, "theoreme", "sure") for n in noms]
        out += [{"type": "constante", "nom": n, "genre": g, "surete": s} for n, g, s in cs]
        out.append({"type": "rejeu", "ok": rejeu, **({"erreur": erreur} if not rejeu else {})})
        if rejeu:
            for n in noms:
                if n in absents:
                    out.append({"type": "attendu", "nom": n, "present": False})
                    continue
                out.append({"type": "attendu", "nom": n, "present": True, "genre": genres.get(n, "theoreme"),
                            "axiomes": axiomes.get(n, ["propext", "Classical.choice", "Quot.sound"]),
                            "enonce": f"∀ (x : ℝ), 0 ≤ x ^ 2", "enonce_explicite": "@LE.le Real Real.instLE …",
                            "aller_retour": aller.get(n, True), "raison": "" if aller.get(n, True) else "différent",
                            "tronque": False, "metavariables": False, "messages_elaboration": 0, "constantes_agent": [],
                            **champs.get(n, {})})
                for cle in [k for k, x in champs.get(n, {}).items() if x is None]:
                    out[-1].pop(cle)
            for n, d in (definitions or {}).items():
                out.append({"type": "definition", "nom": n, "genre": d[0], "enonce": d[1], "valeur": d[2]})
    if doublon:
        out.append(doublon)
    texte = "\n".join(json.dumps(o, ensure_ascii=False) for o in out) + "\n" + extra_avant_fin
    texte += json.dumps({"type": "fin", "nonce": nonce}) + "\n"
    return texte


COMPIL = {"code": 0, "sortie": "", "olean_present": True}
INVENTAIRE = ["Item.ilean", "Item.lean", "Item.olean"]


def verif(sortie, code=0, tronquee=False):
    return {"code": code, "sortie": sortie, "nonce": NONCE, "sortie_tronquee": tronquee}


def echecs(v):
    return {g for g, x in v["gardes"].items() if not x["ok"]}


def evaluer(src=SAIN, sortie=None, inventaire=INVENTAIRE, **k):
    return G.evaluer(src, 2, COMPIL, verif(sortie if sortie is not None else lignes_noyau(), **k), inventaire)


def test_sain_toutes_les_gardes():
    v = evaluer()
    assert v["accepte_gardes"] and v["rejeu_ok"], {g: x["motifs"] for g, x in v["gardes"].items() if x["motifs"]}
    assert "forme explicite" in G.pour_relecteur(v)


def test_gl8_rejeu_en_echec():
    v = evaluer(sortie=lignes_noyau(rejeu=False, erreur="(kernel) declaration type mismatch, etape_1._hors_noyau"))
    assert "G-L8" in echecs(v) and any("_hors_noyau" in x for x in v["gardes"]["G-L8"]["motifs"])
    assert not v["accepte_gardes"]


def test_gl8_imports_hors_liste():
    v = evaluer(sortie=lignes_noyau(imports_permis=False))
    assert {"G-L3", "G-L8"} <= echecs(v)


def test_gl2_axiomes_par_le_noyau():
    v = evaluer(sortie=lignes_noyau(axiomes={"etape_2": ["propext", "sorryAx"]}))
    assert echecs(v) == {"G-L2"}
    v = evaluer(sortie=lignes_noyau(axiomes={"enonce_item": ["Lean.ofReduceBool"]}))
    assert echecs(v) == {"G-L2"}


def test_gl3_axiome_et_surete():
    cs = [("etape_1", "theoreme", "sure"), ("etape_2", "theoreme", "sure"), ("enonce_item", "theoreme", "sure"),
          ("cachee", "axiome", "sure")]
    assert "G-L3" in echecs(evaluer(sortie=lignes_noyau(constantes=cs)))
    cs[3] = ("boucle._unsafe_rec", "definition", "non-sure")
    v = evaluer(sortie=lignes_noyau(constantes=cs, definitions={"boucle._unsafe_rec": ("definition", "ℕ → ℕ", "…")}))
    assert echecs(v) == {"G-L3"}


def test_gl4_genre_et_absence():
    assert echecs(evaluer(sortie=lignes_noyau(genres={"etape_1": "definition"}))) == {"G-L4"}
    assert {"G-L4", "G-L2", "G-L5"} <= echecs(evaluer(sortie=lignes_noyau(absents=("enonce_item",))))


def test_gl5_aller_retour():
    v = evaluer(sortie=lignes_noyau(aller={"enonce_item": False}))
    assert echecs(v) == {"G-L5"}


def test_gl6_constante_non_imprimee_et_imprimee():
    cs = [("etape_1", "theoreme", "sure"), ("etape_2", "theoreme", "sure"), ("enonce_item", "theoreme", "sure"),
          ("enonce_item.i", "definition", "sure")]
    assert echecs(evaluer(sortie=lignes_noyau(constantes=cs))) == {"G-L6"}
    v = evaluer(sortie=lignes_noyau(constantes=cs, definitions={"enonce_item.i": ("definition", "LE ℕ", "{ le := … }")}))
    assert v["accepte_gardes"] and "LE ℕ" in v["impressions"]["enonce_item.i"]


@pytest.mark.parametrize("cas", [
    dict(code=137), dict(code=None), dict(tronquee=True),
    dict(sortie=lignes_noyau(nonce="f" * 32)),
    dict(sortie=lignes_noyau() + json.dumps({"type": "attendu", "nom": "etape_1"}) + "\n"),       # ligne après la fin
    dict(sortie=lignes_noyau() + json.dumps({"type": "definition", "nom": "x", "genre": "definition", "enonce": "ℕ",
                                             "valeur": "1"}) + "\n"),                               # seule après la fin
    dict(sortie=lignes_noyau(extra_avant_fin="bruit hors JSON\n")),
    dict(sortie=lignes_noyau(doublon={"type": "attendu", "nom": "etape_1", "present": True})),
    dict(sortie=lignes_noyau(doublon={"type": "attendu", "nom": "etape_9", "present": True})),
    dict(sortie=lignes_noyau(doublon={"type": "inconnu"})),
    dict(sortie="\n".join(l for l in lignes_noyau().splitlines() if '"etape_2"' not in l or '"attendu"' not in l) + "\n"),
    dict(sortie=lignes_noyau().replace('{"type": "fin"', '{"type": "imports", "permis": true}\n{"type": "fin"')),
    dict(inventaire=INVENTAIRE + ["Lean.olean"]),
])
def test_gl7_artefacts(cas):
    assert "G-L7" in echecs(evaluer(**cas))


def test_gl1_et_texte_en_seconde_ligne():
    v = G.evaluer(SAIN, 2, {"code": 0, "sortie": "", "olean_present": False}, verif(lignes_noyau()), INVENTAIRE)
    assert "G-L1" in echecs(v)
    v = G.evaluer(lire("gl6_notation_v1.lean"), 2, COMPIL, verif(lignes_noyau()), INVENTAIRE)
    assert echecs(v) == {"G-L6"}   # le noyau passe, le texte échoue : l'échec reste un échec


def test_artefacts_v4_texte():
    for nom in ("gl0_lexique_lean_v3.lean", "gl0_lexique_guillemets_v2.lean", "gl0_lexique_colle_v2.lean"):
        m = G.analyser_texte(lire(nom), 2)["motifs"]
        assert all(m[g] for g in TEXTUELLES), nom
    for nom in ("noyau_simproc_hors_noyau_v4.lean", "noyau_run_cmd_hors_noyau_v3.lean", "gl3_simproc_execution_v3.lean",
                "gl3_aesop_tactique_v3.lean"):
        assert G.analyser_texte(lire(nom), 2)["motifs"]["G-L3+"], nom
    assert all(not v for v in G.analyser_texte(lire("noyau_instance_enonce_v3.lean"), 2)["motifs"].values())


# ---- v4 : CLC3-01, commentaire de documentation et imbrication ---------------------------------------------------------------

@pytest.mark.parametrize("src", [
    "/--/ -- -/ axiom faux : False\n",
    "/--/ -- -/ def s : String := \"\n\"\naxiom faux : False\n-- \"\n",
    "/- /- -/ -- -/ axiom faux : False\n",          # k12 : imbrication
    "/-! doc -/ axiom faux : False\n",
])
def test_lexique_v4_aucune_cachette(src):
    m = G.analyser_texte(src, 1)["motifs"]
    assert m["G-L3"], m


def test_artefact_documentation_v4():
    assert G.analyser_texte(lire("noyau_doc_commentaire_v4.lean"), 2)["motifs"]["G-L3"]


# ---- v4 : CLC3-03, imports exacts ---------------------------------------------------------------------------------------------

@pytest.mark.parametrize("modules", [["Mathlib"], ["Init", "Mathlib", "Aesop"], [], ["Init", "Mathlib.Tactic"]])
def test_imports_exacts(modules):
    v = evaluer(sortie=lignes_noyau(modules=modules))
    assert {"G-L3", "G-L8"} <= echecs(v)


# ---- v4 : CLC3-02, trous de l'aller-retour ------------------------------------------------------------------------------------

@pytest.mark.parametrize("champs", [
    {"tronque": True}, {"enonce": "∀ (x : ℝ), ⋯"}, {"enonce_explicite": "@LE.le ⋯"}, {"metavariables": True},
    {"messages_elaboration": 1}, {"tronque": None}, {"metavariables": None}, {"messages_elaboration": None},
])
def test_trous_de_l_aller_retour(champs):
    v = evaluer(sortie=lignes_noyau(champs={"etape_2": champs}))
    assert echecs(v) == {"G-L5"}, v["gardes"]["G-L5"]


# ---- v4 : CLC3-06, constantes de l'agent et noms hors ASCII ----------------------------------------------------------------

def test_constantes_de_l_agent_citees():
    v = evaluer(sortie=lignes_noyau(champs={"etape_1": {"constantes_agent": ["carre"]}}))
    assert v["accepte_gardes"] and v["signalements"] == ["etape_1 cite des constantes de l'agent : carre"]
    assert G.pour_relecteur(v).index("Signalements") < G.pour_relecteur(v).index("Énoncés")
    assert echecs(evaluer(sortie=lignes_noyau(champs={"enonce_item": {"constantes_agent": ["carre"]}}))) == {"G-L5"}
    assert echecs(evaluer(sortie=lignes_noyau(champs={"etape_2": {"constantes_agent": None}}))) == {"G-L5"}


def test_noms_hors_ascii():
    noms = ["etape_1", "etape_2", "enonce_item"]
    cs = [(n, "theoreme", "sure") for n in noms] + [("Cοprime", "definition", "sure")]
    v = evaluer(sortie=lignes_noyau(constantes=cs, definitions={"Cοprime": ("definition", "ℕ → ℕ → Prop", "…")}))
    assert echecs(v) == {"G-L6"} and any("ο" in x for x in v["gardes"]["G-L6"]["motifs"])
    cs[-1] = ("x₁", "definition", "sure")
    assert evaluer(sortie=lignes_noyau(constantes=cs, definitions={"x₁": ("definition", "ℕ", "1")}))["accepte_gardes"]


# ---- v4 : CLC3-11 k07, k14, k15 ; exposition du rejeu -----------------------------------------------------------------------

def test_nonce_mal_forme():   # k07
    v = G.evaluer(SAIN, 2, COMPIL, {"code": 0, "sortie": lignes_noyau(nonce="court"), "nonce": "court"}, INVENTAIRE)
    assert echecs(v) == {"G-L7"} and any("nonce du harnais" in x for x in v["gardes"]["G-L7"]["motifs"])


def test_constante_en_double():   # k14
    noms = ["etape_1", "etape_2", "enonce_item"]
    cs = [(n, "theoreme", "sure") for n in noms] + [("etape_1", "theoreme", "sure")]
    assert echecs(evaluer(sortie=lignes_noyau(constantes=cs))) == {"G-L7"}


def test_deux_lignes_de_rejeu():   # k15
    sortie = lignes_noyau().replace('{"type": "fin"', '{"type": "rejeu", "ok": true}\n{"type": "fin"')
    assert "G-L7" in echecs(evaluer(sortie=sortie))


def test_rejeu_expose():
    v = evaluer(sortie=lignes_noyau(rejeu=False, erreur="(kernel) declaration type mismatch, 'faux_lemme'"))
    assert v["rejeu_present"] and "faux_lemme" in v["rejeu_erreur"] and not v["rejeu_ok"]
    v = evaluer(sortie=lignes_noyau(imports_permis=False))
    assert not v["rejeu_present"]


def test_attendus_v4_complets():
    a = json.loads(lire("attendus-v4.json"))
    for groupe in ("noyau", "observations_noyau", "lean", "isolement_lean", "python", "limites_python"):
        for c in a[groupe]:
            assert (ARTEFACTS / c["fichier"]).is_file(), c["fichier"]
    for c in a["noyau"]:
        assert {"G-L1", "G-L7"} <= set(c.get("passent", [])) or c["fichier"] == "sain_v1.lean", c["nom"]
        if c.get("rejeu") is False:
            assert c["constante_fautive"] and "G-L8" in c["sans_suppl"]["echecs"]
