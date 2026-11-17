"""Essais du code du crible (v) — v1 (fichier neuf, R12) : chaque ligne de la liste d'arrêt sur un cas sain et sur un artefact
(R5), les calculs de la mesure recalculés indépendamment, la lecture gelée à ses bornes, et l'essai à blanc complet avec relais
factices (aucun appel réel, aucune clé). Joués contre le code d'un dossier donné (`--code`) : le dossier du crible, ou une copie
mutée par le banc de mutations (`banc_mutations_crible_v_v1.py`), qui exige que chaque mutation fasse échouer au moins un essai
attendu.

Usages (chaque palier écrit un JSON de résultats : {essais: [{nom, ligne, cas, ok, detail}], echecs}) :
  python3 -I -B essais_crible_v_v1.py unitaire --code DOSSIER --arbre ORCH --essai DOSSIER_ESSAI --sortie R.json
  python3 -I -B essais_crible_v_v1.py jouer    --code DOSSIER --arbre ORCH --essai DOSSIER_ESSAI --travail DOSSIER_NEUF --sortie R.json
  python3 -I -B essais_crible_v_v1.py mesure   --code DOSSIER --arbre ORCH --essai DOSSIER_ESSAI --reference DOSSIER_JOUE
          --travail DOSSIER_NEUF --sortie R.json
DOSSIER_ESSAI porte `prive/` (secret d'essai, phrase d'essai, MONDES.json, CERTIFIEES.json et leurs engagements, tirés par
`generer` du lanceur sur un secret d'essai public) et `texte-essai.txt` : jamais un monde ni un secret du crible.
"""
import argparse
import copy
import hashlib
import importlib
import itertools
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import time
import traceback

RESULTATS = []


def essai(nom, ligne, cas):
    def deco(f):
        f._essai = (nom, ligne, cas)
        return f
    return deco


def jouer_essais(fonctions, contexte):
    for f in fonctions:
        nom, ligne, cas = f._essai
        try:
            detail = f(contexte)
            ok = True
        except AssertionError as e:
            ok, detail = False, f"assertion : {e}"
        except Exception as e:  # noqa: BLE001
            ok, detail = False, f"{type(e).__name__} : {str(e)[:300]} | {traceback.format_exc()[-400:]}"
        RESULTATS.append({"fonction": f.__name__, "nom": nom, "ligne": ligne, "cas": cas, "ok": ok, "detail": str(detail)[:600]})
        print(f"{'OK ' if ok else 'ECHEC'} {nom} ({cas}) : {str(detail)[:160]}", flush=True)


def doit_refuser(f, *motifs, classe=None):
    try:
        f()
    except Exception as e:  # noqa: BLE001
        if classe is not None and not isinstance(e, classe):
            raise AssertionError(f"refus d'une autre classe : {type(e).__name__} : {e}") from None
        m = str(e)
        if motifs and not any(x in m for x in motifs):
            raise AssertionError(f"refus pour une autre raison : {m[:200]}") from None
        return m[:200]
    raise AssertionError("aucun refus")


# --- contexte ---------------------------------------------------------------------------------------------------------------------

class Ctx:
    pass


def charger(code, arbre, essai_dir):
    sys.path.insert(0, code)
    c = Ctx()
    c.code, c.arbre, c.essai = code, arbre, essai_dir
    c.K = importlib.import_module("crible_v_commun_v1")
    c.L = importlib.import_module("lanceur_crible_v_v1")
    c.MC = importlib.import_module("mesure_crible_v_v1")
    c.LI = importlib.import_module("lire_crible_v_v1")
    c.PA = importlib.import_module("partie_a_crible_v_v1")
    c.A = c.L.charger_arbre(arbre)
    c.mr2 = os.path.join(arbre, "mr2_v68")
    c.V4, c.M, c.P1, c.CS = c.MC.charger_mr2(c.mr2)
    c.prive = os.path.join(essai_dir, "prive")
    c.mondes_f = os.path.join(c.prive, "MONDES.json")
    c.certif_f = os.path.join(c.prive, "CERTIFIEES.json")
    if os.path.isfile(c.mondes_f):
        c.H = c.K.sha256_fichier(c.mondes_f)
        c.HC = c.K.sha256_fichier(c.certif_f)
        c.mondes = json.load(open(c.mondes_f, encoding="utf-8"))
    c.texte_sha = c.K.sha256_fichier(os.path.join(essai_dir, "texte-essai.txt"))
    return c


# =================================================================================================================================
# palier unitaire
# =================================================================================================================================

@essai("graine des mondes", "graines (R9)", "sain")
def u_graine_sain(c):
    s, ph, e = bytes(32), "phrase publique d'essai", "00" * 32
    g = [c.K.graine_monde_crible(s, ph, e, r) for r in range(1, 21)]
    assert g == [c.K.graine_monde_crible(s, ph, e, r) for r in range(1, 21)], "rejeu différent"
    assert len(set(g)) == 20 and all(x >= 2 ** 64 for x in g)
    import hashlib as h
    attendu = 2 ** 64 + int.from_bytes(h.sha256(b"crible-v-v1\x00" + s + b"\x00" + ph.encode() + b"\x00" + bytes(32) + b"\x00" + bytes([1])).digest()[:8], "big")
    assert g[0] == attendu, "forme de la graine ≠ celle du texte (étiquette crible-v-v1, r sur un octet)"
    return "20 graines distinctes, forme du texte"


@essai("graine des mondes", "graines (R9)", "artefact")
def u_graine_artefact(c):
    s, ph, e = bytes(32), "p", "00" * 32
    for args in ((bytes(31), ph, e, 1), (s, "a\x00b", e, 1), (s, "", e, 1), (s, ph, e, 0), (s, ph, e, 21), (s, ph, "00", 1),
                 (s, ph, e, True)):
        doit_refuser(lambda: c.K.graine_monde_crible(*args))
    return "secret court, phrase nulle ou vide, r hors de 1 à 20, empreinte courte : refusés"


@essai("règle de M et budget de durée", "devis : règle de M", "sain")
def u_regle_m(c):
    K = c.K
    assert K.m_de_la_regle(0) == 1 and K.m_de_la_regle(12400) == 1 and K.m_de_la_regle(12400.5) == 2
    assert K.m_de_la_regle(15400) == 2 and K.m_de_la_regle(15401) is None and K.m_de_la_regle(None) is None
    assert K.budget_depart_s(1, 0) == 24000 and K.budget_depart_s(2, 0) == 15000 and K.budget_depart_s(1, 12400) == 61200
    assert K.B_A_S == 900 and K.N_MONDES == 20
    return "M = 1 jusqu'à 12 400 s, 2 jusqu'à 15 400 s, non lançable au-delà ; garde 24 000 + 3 D (M = 1), 15 000 + 3 D (M = 2)"


@essai("garde de départ (minuterie)", "minuterie de la machine", "sain")
def u_garde_sain(c):
    r = c.L.exiger_garde_de_depart(time.time() + 61200, 1, 5000)
    assert r["budget_s"] == 39000
    return f"marge suffisante : {r}"


@essai("garde de départ (minuterie)", "minuterie de la machine", "artefact")
def u_garde_artefact(c):
    return doit_refuser(lambda: c.L.exiger_garde_de_depart(time.time() + 38000, 1, 5000), "garde de départ")


@essai("table W_min recalculée", "seuil", "sain")
def u_w_min(c):
    for n in range(16, 21):
        assert c.K.w_min_calcule(n) == c.K.W_MIN[n] == 4
    c.LI.exiger_table_w_min()
    return "W_min = 4 pour n_c de 16 à 20"


@essai("placebo exact", "placebo", "sain")
def u_placebo_sain(c):
    ell, db, de = [1, 0, 2, 0, 1, 3], [1.0] * 6, [3.0] * 6
    Ls, Ss, n = c.MC.placebo_exact(ell, db, de, 2)
    c.MC.exiger_placebo(n, 6, 2, 2)
    att = [sum(ell) - ell[i] - ell[j] for i, j in itertools.combinations(range(6), 2)]
    assert Ls == att and n == 15
    assert abs(Ss[0] - (1 - (6 + 6) / 24)) < 1e-12
    r = c.MC.resume_placebo(Ls, Ss, 4)
    assert abs(r["p_choix"] - sum(1 for x in att if x <= 4) / 15) < 1e-12
    return "C(6, 2) = 15 ensembles, L_P et S_P exacts, p_choix exact"


@essai("placebo exact", "placebo", "artefact")
def u_placebo_artefact(c):
    a = doit_refuser(lambda: c.MC.exiger_placebo(math.comb(20, 10), 20, 10, 11), "taille")
    b = doit_refuser(lambda: c.MC.exiger_placebo(math.comb(20, 10) - 1, 20, 10, 10), "incomplète")
    return f"taille k_R + 1 : {a} ; énumération tronquée : {b}"


@essai("bras, épargne et pertes", "métrique", "sain")
def u_bras(c):
    mondes = [1, 2, 3, 4]
    q = {1: 0.9, 2: 0.2, 3: 0.81, 4: 0.8}
    ell = {1: 1, 2: 2, 3: 0, 4: 1}
    db = {w: 1.0 for w in mondes}
    de = {w: 3.0 for w in mondes}
    R = c.MC.bras(mondes, q, ell, None, None, None, db, de)
    assert R["a"] == [1, 0, 1, 0], R["a"]
    assert R["k"] == 2 and R["W"] == 2 and R["L"] == 3
    assert abs(R["S"] - (1 - (4 + 6) / 16)) < 1e-12
    assert abs(c.MC.epargne([1, 1], [3, 3], [0, 0]) - 0.75) < 1e-12
    return "a_w = 1 si q > 0,8 strictement ; W_R, L_R, S_R exacts"


@essai("rééchantillonnage des mondes", "graines (R9)", "sain")
def u_reechantillon(c):
    import numpy as np
    r = 12345
    i = c.MC.indices_reechantillon(r, 7, 50)
    att = np.stack([np.random.default_rng(np.random.SeedSequence(entropy=r, spawn_key=(99, b))).integers(0, 7, 7) for b in range(50)])
    assert (i == att).all(), "indices ≠ SeedSequence(entropy=racine, spawn_key=(99, b))"
    return "indices égaux à SeedSequence(entropy=racine, spawn_key=(99, b))"


def monde_essai(c, w=1):
    pm = c.MC.preparer_monde(c.M, c.P1, c.mondes[w - 1])
    jeu = c.MC.jeu_public(c.M, c.K.racine_des_graines(c.texte_sha), w)
    return pm, jeu


@essai("fonction de décision : entrées", "la fonction de décision reçoit autre chose…", "sain")
def u_decider_sain(c):
    pm, jeu = monde_essai(c)
    k1 = pm["k1"]
    lois = [c.MC.LoiBonMarche("argon", k1), c.MC.LoiBonMarche("opus55", k1)]
    r = c.MC.decider(c.M, c.CS, lois, k1, jeu)
    assert r == {"n": 2, "copies": 2, "q": 1.0, "a": 1}, r
    autre = c.M.monde_restreint(pm["spec"], [e["id"] for e in pm["spec"]["effets"] if e["classe"] in ("forte", "moyenne")])
    r2 = c.MC.decider(c.M, c.CS, [c.MC.LoiBonMarche("argon", autre)], k1, jeu)
    assert r2["copies"] == 0 and r2["a"] == 0, r2
    return "K1 seule : copie ; monde réduit aux fortes et moyennes : pas une copie"


@essai("fonction de décision : entrées", "la fonction de décision reçoit autre chose…", "artefact")
def u_decider_artefact(c):
    pm, jeu = monde_essai(c)
    k1 = pm["k1"]
    lois = [c.MC.LoiBonMarche("argon", k1)]
    a = doit_refuser(lambda: c.MC.decider(c.M, c.CS, lois, k1, pm["o"]), "jeu public")

    class JeuAIssues:
        def __init__(s):
            s.Z, s.G, s.Y, s.nsp = jeu.Z, jeu.G, [0] * len(jeu.G), 3
    b = doit_refuser(lambda: c.MC.decider(c.M, c.CS, lois, k1, JeuAIssues()), "jeu public")
    d = doit_refuser(lambda: c.MC.LoiBonMarche("astra", k1), "moitié chère")
    x = c.MC.LoiBonMarche("argon", k1)
    object.__setattr__(x, "proposeur", "fable52")
    e = doit_refuser(lambda: c.MC.decider(c.M, c.CS, [x], k1, jeu), "moitié chère")
    f = doit_refuser(lambda: c.MC.decider(c.M, c.CS, lois, [k1, k1], jeu), "K1 servie")
    g = doit_refuser(lambda: c.MC.decider(c.M, c.CS, lois, c.M.compiler_monde(pm["spec"]), jeu), "K1 servie")
    h = doit_refuser(lambda: c.MC.decider(c.M, c.CS, [{"proposeur": "argon", "loi": k1}], k1, jeu), "moitié bon marché")
    return f"oracle : {a} | issue : {b} | carte chère : {d} ; {e} | archive : {f} | loi plantée : {g} | autre objet : {h}"


@essai("règle : seuil strict et sens dirigé", "métrique (copie, a_w)", "sain")
def u_regle_strict(c):
    pm, jeu = monde_essai(c)
    k1 = pm["k1"]
    vrai = (False, (0.001, 0.001), (0.5, 0.5))      # copie au sens dirigé
    inverse = (False, (0.5, 0.5), (0.001, 0.001))   # copie seulement au minimum des deux sens
    d0 = c.MC.distances
    try:
        seq = iter([vrai] * 4 + [inverse])
        c.MC.distances = lambda *a, **k: next(seq)
        lois = [c.MC.LoiBonMarche("argon", {"type": "fixe", "probas": [1, 1, i + 1]}) for i in range(5)]
        r = c.MC.decider(c.M, c.CS, lois, k1, jeu)
        assert r["copies"] == 4 and r["q"] == 0.8 and r["a"] == 0, f"q = 0,8 doit donner a = 0 (« > » strict) et le sens dirigé : {r}"
        seq2 = iter([inverse] * 5)
        c.MC.distances = lambda *a, **k: next(seq2)
        r2 = c.MC.decider(c.M, c.CS, lois, k1, jeu)
        assert r2["copies"] == 0, f"sens dirigé (carte → K1) exigé, jamais le minimum des deux sens : {r2}"
    finally:
        c.MC.distances = d0
    assert c.MC.est_copie(inverse, "minimum") and not c.MC.est_copie(inverse, "dirige")
    assert c.MC.est_copie((False, (0.009, 0.05), (1, 1)), "global") and not c.MC.est_copie((False, (0.009, 0.05), (1, 1)), "dirige")
    return "q = 0,8 → a = 0 ; copie au sens dirigé seulement ; ε_strat exigé"


@essai("jeu public", "jeu public porteur d'issues ou tiré du secret", "sain")
def u_jeu_sain(c):
    import numpy as np
    racine = c.K.racine_des_graines(c.texte_sha)
    jeu = c.MC.jeu_public(c.M, racine, 5)
    rng = np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(5, 30)))
    Z, G = c.M.tirer_instances(rng, 2000, 8, 3)
    assert (jeu.Z == Z).all() and (jeu.G == G).all(), "jeu ≠ SeedSequence(entropy=racine, spawn_key=(r, 30))"
    assert c.MC.JeuPublic.__slots__ == ("r", "Z", "G", "nsp", "graine"), "le jeu public porte autre chose que traits et sous-populations"
    assert c.MC.empreinte_du_jeu(jeu) == c.MC.empreinte_du_jeu(c.MC.jeu_public(c.M, racine, 5))
    return "jeu de (r, 30), sans issue, empreinte reproductible"


@essai("jeu public", "jeu public porteur d'issues ou tiré du secret", "artefact")
def u_jeu_artefact(c):
    racine = c.K.racine_des_graines(c.texte_sha)
    a = doit_refuser(lambda: c.MC.jeu_public(c.M, racine, 2 ** 64 + 7), "indice r")
    jeu = c.MC.jeu_public(c.M, racine, 5)
    b = doit_refuser(lambda: setattr(jeu, "Y", [0]), "immuable")
    return f"graine du secret : {a} ; champ d'issue ajouté : {b}"


@essai("cartes valides", "couverture comptant une carte refusée, tronquée, au-delà de six, non évaluable", "sain")
def u_cartes_valides(c):
    k1 = {"type": "softmax", "poids": [[0] * 8, [1] + [0] * 7, [0] * 8], "biais": [0, 0, 0]}
    etat = {(1, "argon"): "complet", (1, "astra"): "tronque"}
    cartes = [{"monde": 1, "proposeur": "argon", "emplacement": 1, "etat": "admise", "loi": k1},
              {"monde": 1, "proposeur": "argon", "emplacement": 2, "etat": "refusee", "loi": k1},
              {"monde": 1, "proposeur": "argon", "emplacement": 7, "etat": "refusee", "loi": k1},
              {"monde": 1, "proposeur": "argon", "emplacement": 3, "etat": "admise", "loi": {"type": "inconnu"}},
              {"monde": 1, "proposeur": "astra", "emplacement": 1, "etat": "admise", "loi": k1}]
    v, comptes = c.MC.cartes_valides(etat, cartes, lambda loi, w: loi.get("type") == "softmax")
    assert [x["emplacement"] for x in v[(1, "argon")]] == [1] and v[(1, "astra")] == [], v
    assert comptes == {"refusees": 1, "au_dela_de_six": 1, "non_evaluables": 1, "d_appels_tronques": 1}, comptes
    return "seule la carte admise, évaluable, d'emplacement ≤ 6, d'un appel complet est valide"


@essai("cartes valides", "couverture comptant une carte refusée, tronquée, au-delà de six, non évaluable", "artefact")
def u_carte_au_dela(c):
    mondes = {w["monde"]: w for w in c.mondes}
    don = {"appels": [{"monde": w, "proposeur": p, "etat": "complet"} for w in mondes for p in c.K.PROPOSEURS],
           "cartes": [{"monde": 1, "proposeur": "argon", "emplacement": 7, "etat": "admise", "loi": {}}]}
    return doit_refuser(lambda: c.MC.lire_appels_et_cartes(don, mondes), "au-delà de la sixième")


@essai("dollars", "dollars des appels tronqués ou en échec", "sain")
def u_dollars(c):
    mondes = {w["monde"]: w for w in c.mondes}
    doc = {"version": "dollars-crible-v-v1", "appels": [{"monde": w, "proposeur": p, "cout_config_usd": 1.0, "source": "journal_relais"}
                                                        for w in mondes for p in c.K.PROPOSEURS]}
    d = c.MC.lire_dollars(doc, mondes)
    assert len(d) == 80
    r = c.MC.rapport_public_sur_configuration({"argon": (10.0, 50.0), "opus55": (4.0, 20.0), "astra": (10.0, 50.0), "fable52": (8.0, 40.0)})
    assert r == {"fable52": 1.0, "opus55": 1.0, "astra": 1.0, "argon": 0.2}, r
    doc2 = copy.deepcopy(doc)
    doc2["appels"][0]["source"] = "non_lance"
    doit_refuser(lambda: c.MC.lire_dollars(doc2, mondes), "non lancé")
    doc3 = copy.deepcopy(doc)
    doc3["appels"].pop()
    doit_refuser(lambda: c.MC.lire_dollars(doc3, mondes), "80 appels")
    return "80 appels exigés, prix publics : Pr-1 au cinquième du prix de la configuration, les autres égaux"


@essai("rejeu sous archive fictive", "rejeu sous archive fictive…", "artefact")
def u_fictive(c):
    a = doit_refuser(lambda: c.MC.rejeu_archive_fictive(c.M, c.CS, "/nonexistant/sortie.json", {}, {}, {}, {}, {}, None), "avant l'écriture")
    b = doit_refuser(lambda: c.MC.exiger_sortie_fictive({"version": "x", "k_R": 1, "S_R": 0.5, "archive": "", "seuil": 0.8,
                                                         "sortie_principale_sha256": "x", "a_lire": "", "W_R": 2}), "autre chose")
    return f"avant l'écriture : {a} ; rendant W : {b}"


@essai("configuration v12", "configuration autre que v12", "sain")
def u_conf_sain(c):
    conf = c.L.lire_configuration_v12(c.A)
    assert conf["version"] == "configuration-pilote-mr2-v12"
    return "v12 acceptée (f69503dd…)"


@essai("configuration v12", "configuration autre que v12", "artefact")
def u_conf_artefact(c):
    d = tempfile.mkdtemp()
    src = os.path.dirname(c.A.CONF)
    shutil.copytree(src, os.path.join(d, "x"))
    f = os.path.join(d, "x", os.path.basename(c.A.CONF))
    conf = json.load(open(f, encoding="utf-8"))
    conf["proposeurs"]["argon"]["plafond_session_usd"] = 2.0
    json.dump(conf, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    m = doit_refuser(lambda: c.L.lire_configuration_v12(c.A, f), "v12")
    shutil.rmtree(d)
    return f"plafond de Pr-1 changé : {m}"


@essai("addendum d'empreintes", "empreinte différente (programme de mesure, module importé)", "sain")
def u_addendum_sain(c):
    d = tempfile.mkdtemp()
    f = os.path.join(d, "addendum.md")
    open(f, "w").write("\n".join(f"- `{s}  docs/procedures/crible-v-v1/{n}`" for n, s in c.L.empreintes_du_code_crible().items()) + "\n")
    c.L.exiger_addendum(f, c.K.sha256_fichier(f))
    shutil.rmtree(d)
    return "addendum aux empreintes du code présent : accepté"


@essai("addendum d'empreintes", "empreinte différente (programme de mesure, module importé)", "artefact")
def u_addendum_artefact(c):
    d = tempfile.mkdtemp()
    f = os.path.join(d, "addendum.md")
    e = c.L.empreintes_du_code_crible()
    e["mesure_crible_v_v1.py"] = hashlib.sha256(open(os.path.join(c.code, "mesure_crible_v_v1.py"), "rb").read() + b" ").hexdigest()
    open(f, "w").write("\n".join(f"{s}  {n}" for n, s in e.items()) + "\n")
    m = doit_refuser(lambda: c.L.exiger_addendum(f, c.K.sha256_fichier(f)), "mesure_crible_v_v1.py")
    m2 = doit_refuser(lambda: c.L.exiger_addendum(f, "0" * 64), "empreinte différente")
    shutil.rmtree(d)
    return f"un octet de plus dans la mesure : {m} ; addendum d'une autre empreinte : {m2}"


@essai("module importé à empreinte fausse", "empreinte différente (module importé)", "artefact")
def u_module_faux(c):
    d = tempfile.mkdtemp()
    shutil.copytree(c.mr2, os.path.join(d, "mr2"))
    f = os.path.join(d, "mr2", "outils-v4", "monde_riche_v4.py")
    open(f, "a").write("\n# un octet\n")
    c.MC._MR2.clear()
    try:
        m = doit_refuser(lambda: c.MC.charger_mr2(os.path.join(d, "mr2")), "empreinte fausse")
        open(f + ".sha256", "w").write(f"{c.K.sha256_fichier(f)}  monde_riche_v4.py\n")  # compagnon refait : seule l'empreinte écrite arrête
        m += " ; compagnon refait : " + doit_refuser(lambda: c.MC.charger_mr2(os.path.join(d, "mr2")), "empreinte fausse")
    finally:
        c.MC._MR2.clear()
        c.MC.charger_mr2(c.mr2)
        shutil.rmtree(d)
    return m


@essai("gabarit servi", "empreinte différente (gabarit)", "sain")
def u_gabarit_sain(c):
    c.L.exiger_gabarit(c.A.P)
    return "gabarit e77d3041… accepté"


@essai("gabarit servi", "empreinte différente (gabarit)", "artefact")
def u_gabarit_artefact(c):
    P = c.A.P
    v = P.CONSIGNE_PROPOSEUR
    try:
        P.CONSIGNE_PROPOSEUR = v[:-1] + "!"
        m = doit_refuser(lambda: c.L.exiger_gabarit(P), "gabarit")
    finally:
        P.CONSIGNE_PROPOSEUR = v
    return f"un octet changé dans le gabarit : {m}"


@essai("corps servis égaux", "corps servi différent entre les quatre appels d'un monde", "sain")
def u_corps_sain(c):
    servi = corps_jouet(c)
    corps = {n: c.L.corps_de_l_appel(c.A, servi, c.A.P.gabarit_sha256()) for n in c.K.PROPOSEURS}
    c.L.exiger_corps_egaux(corps, servi)
    return "quatre empreintes égales"


@essai("corps servis égaux", "corps servi différent entre les quatre appels d'un monde", "artefact")
def u_corps_artefact(c):
    servi = corps_jouet(c)
    corps = {n: c.L.corps_de_l_appel(c.A, servi, c.A.P.gabarit_sha256()) for n in c.K.PROPOSEURS}
    s2 = dict(servi, episodes=servi["episodes"][1:])
    corps["opus55"] = c.L.corps_de_l_appel(c.A, s2, c.A.P.gabarit_sha256())
    return doit_refuser(lambda: c.L.exiger_corps_egaux(corps, servi), "corps servi différent")


def corps_jouet(c):
    P = c.A.P
    k1 = {"type": "softmax", "poids": [[0.0] * 8, [0.5] + [0.0] * 7, [0.0] * 8], "biais": [0.0, 0.1, 0.0]}
    archive = [{"identifiant": "F-000000000000", "loi": k1}]
    episodes = [{"z": [0.1 * i] * 8, "g": i % 3, "y": i % 3} for i in range(400)]
    texte = P.texte_servi(archive, episodes)
    return {"texte": texte, "archive": archive, "episodes": episodes, "texte_sha256": hashlib.sha256(texte.encode()).hexdigest(),
            "episodes_sha256": hashlib.sha256(c.K.json_canonique(episodes)).hexdigest()}


@essai("coupure à B_a journalisée", "appel plus long que B_a", "artefact")
def u_coupure(c):
    d = tempfile.mkdtemp()
    f = os.path.join(d, "coupures.jsonl")
    c.L.journaliser_coupure(f, {"monde": 1, "proposeur": "astra"})
    assert json.loads(open(f).read()) == {"monde": 1, "proposeur": "astra"}
    os.makedirs(os.path.join(d, "dossier.jsonl"))
    m = doit_refuser(lambda: c.L.journaliser_coupure(os.path.join(d, "dossier.jsonl"), {"monde": 2}), "sans trace", classe=c.K.Arret)
    shutil.rmtree(d)
    return f"coupure écrite et relue ; sans trace : {m}"


@essai("pièces de l'appel", "réponse brute ou témoin d'isolement absent", "artefact")
def u_pieces(c):
    d = tempfile.mkdtemp()
    for n in ("reponse-brute.json", "temoin-isolement.json"):
        c.K.ecrire_scelle_json(os.path.join(d, n), {"x": 1})
    c.L.exiger_pieces_de_l_appel(d, "astra")
    os.unlink(os.path.join(d, "temoin-isolement.json"))
    m = doit_refuser(lambda: c.L.exiger_pieces_de_l_appel(d, "astra"), "temoin-isolement", classe=c.K.Arret)
    shutil.rmtree(d)
    return f"appel complet avec ses pièces accepté ; témoin supprimé : {m}"


@essai("part d'un fournisseur", "dépense d'un fournisseur atteignant sa part", "sain")
def u_part_sain(c):
    p = {"plafond_session_usd": 2.34}
    assert abs(c.L.exiger_part(19 * 2.34 - 1e-9, p, "argon") - 46.8) < 1e-9
    return "part non atteinte (19 plafonds dépensés, un appel de plus permis)"


@essai("part d'un fournisseur", "dépense d'un fournisseur atteignant sa part", "artefact")
def u_part_artefact(c):
    return doit_refuser(lambda: c.L.exiger_part(19 * 2.34 + 0.01, {"plafond_session_usd": 2.34}, "argon"), "part", classe=c.K.Arret)


def etat_jouet(c):
    conf = c.L.lire_configuration_v12(c.A)
    return c.L.Etat(conf)


def r_jouet(etat, abandon=False):
    return {"etat": etat, "cout_usd": 0.1, "abandon": abandon, "code": 3 if abandon else 0, "cause": None}


CARTE_OK = [{"etat": "admise", "emplacement": 1}]


@essai("abandon d'un fournisseur", "fournisseur abandonné…", "sain")
def u_abandon_sain(c):
    E = etat_jouet(c)
    c.L.traiter_resultat(E, 1, "opus55", {"monde": 1}, r_jouet("complet"), CARTE_OK, None)
    c.L.traiter_resultat(E, 2, "fable52", {"monde": 2}, r_jouet("echec", abandon=True), [], None)
    assert E.arret is None, E.arret
    assert "claude" in E.abandonnes and E.minimum_possible()
    return "panne d'un fournisseur ayant déjà répondu, minimum encore possible : le crible continue (appels restants « échec »)"


@essai("abandon d'un fournisseur", "fournisseur abandonné…", "artefact")
def u_abandon_artefact(c):
    E = etat_jouet(c)
    c.L.traiter_resultat(E, 1, "argon", {"monde": 1}, r_jouet("echec", abandon=True), [], None)
    assert E.arret and "perdu en entier" in E.arret, E.arret
    E2 = etat_jouet(c)
    for w in (1, 2):
        for n in c.K.PROPOSEURS:
            c.L.traiter_resultat(E2, w, n, {"monde": w}, r_jouet("complet"), CARTE_OK, None)
    c.L.traiter_resultat(E2, 3, "opus55", {"monde": 3}, r_jouet("echec", abandon=True), [], None)
    assert E2.arret is None
    c.L.traiter_resultat(E2, 3, "argon", {"monde": 3}, r_jouet("echec", abandon=True), [], None)
    assert E2.arret and "minimum" in E2.arret, E2.arret
    assert E2.arret_classe == "fournisseur_abandonne"
    return f"première panne sans répondu : arrêt ; panne au monde 3 rendant le minimum impossible : {E2.arret}"


@essai("relevé de la sonde neuve", "relevé de sonde absent, invalide ou d'un autre code", "artefact")
def u_releve(c):
    conf = c.L.lire_configuration_v12(c.A)
    a = doit_refuser(lambda: c.L.exiger_releve_sonde(c.A, conf, "/nonexistant/releve.json", 1), "absent")
    d = tempfile.mkdtemp()
    f = os.path.join(d, "releve-sonde-crible-v-v1.json")
    c.K.ecrire_scelle_json(f, {"version": "releve-sonde-pilote-v74", "partiel": False, "borne_courte": True,
                               "pieces_sha256": {"commande": conf["commande"]["sha256"], "relais": conf["relais"]["sha256"]},
                               "configuration_sha256": c.A.PR.empreinte_configuration(conf), "code_sha256": {"autre": "code"}})
    b = doit_refuser(lambda: c.L.exiger_releve_sonde(c.A, conf, f, 1), "autre code")
    shutil.rmtree(d)
    return f"absent : {a} ; d'un autre code : {b}"


@essai("rapatriement sans monde", "mondes privés, jamais hors de la machine", "artefact")
def u_rapatrier(c):
    d = tempfile.mkdtemp()
    src = os.path.join(d, "src")
    os.makedirs(os.path.join(src, "monde-1", "argon"))
    c.K.ecrire_scelle_json(os.path.join(src, "CARTES.json"), {"cartes": [], "appels": []})
    open(os.path.join(src, "monde-1", "argon", "reponse-brute.json"), "w").write('{"episodes_developpement": []}')
    args = argparse.Namespace(source=src, destination=os.path.join(d, "dst"), mondes=c.mondes_f, mondes_sha256=c.H, arbre=c.arbre)
    m = doit_refuser(lambda: c.L.rapatrier(args), "interdits")
    assert not os.path.exists(os.path.join(d, "dst", "CARTES.json")), "rien ne doit être copié"
    shutil.rmtree(d)
    return m


@essai("partie A : champs du juge", "partie A", "sain")
def u_partie_a_sain(c):
    pm, _ = monde_essai(c)
    k1 = {"type": "softmax", "poids": [[0, 0], [1.0, 0], [0, 0]], "biais": [0, 0, 0]}
    autre = {"type": "softmax", "poids": [[0, 0], [0, 0], [0, 3.0]], "biais": [0, 0, 0]}  # un autre trait : hors du nul de K1
    doc = {"archive_initiale": [{"loi": k1}],
           "generations": [{"generation": g, "appels": [{"proposeur": p, "cartes": [{"loi": k1, "admise": True},
                                                                                    {"loi": autre, "admise": True}]}
                                                         for p in ("a", "b")]} for g in (1, 2)]}
    d = tempfile.mkdtemp()
    f = os.path.join(d, "r.json")
    json.dump(doc, open(f, "w"))
    k, par_g = c.PA.cartes_du_releve(c.PA.charger_garde(f))
    out = c.PA.partie_a(c.M, c.CS, 1, k, par_g, 2, 2)
    assert out["generations"]["1"]["parts_des_copies"]["a"]["q"] == 0.5, out
    assert out["generations"]["2"]["parts_des_copies"]["a"]["q"] == 1.0, "génération 2 : l'archive porte toutes les cartes de la génération 1"
    assert out["generations"]["2"]["archive_lois"] == 5
    t = open(os.path.join(os.path.dirname(os.path.dirname(c.code)), "notes", "organisme-boucle-reelle-v1",
                          "preenregistrement-boucle-reelle-organisme-v1-v2.md"), encoding="utf-8").read() \
        if os.path.isdir(os.path.join(os.path.dirname(os.path.dirname(c.code)), "notes")) else None
    if t is not None:
        assert c.PA.dimensions_de_s_v1(t) == (3, 2, 2)
    shutil.rmtree(d)
    return "lois, proposeurs et générations seulement ; copie de K1 comptée ; dimensions de S-V1 lues dans le texte (3, 2, 2)"


@essai("partie A : champs du juge", "partie A", "artefact")
def u_partie_a_artefact(c):
    doc = c.PA.DictGarde({"promue": True, "retenues": [1], "rejet": 1, "mort": 0})
    a = doit_refuser(lambda: doc["promue"], "champ du juge")
    b = doit_refuser(lambda: doc.get("retenues"), "champ du juge")
    e = doit_refuser(lambda: doc["rejet"], "champ du juge")
    f = doit_refuser(lambda: doc["mort"], "champ du juge")
    assert doc.items() == []
    return f"promue : {a} ; retenues : {b} ; rejet : {e} ; mort : {f}"


def corps_jouet_lecture(**k):
    n_c = k.get("n_c", 20)
    mondes = list(range(1, n_c + 1))
    q = k.get("q", 0.2)
    corps = {"n_c": n_c, "mondes_complets": mondes, "mondes_avec_C_T_positif": k.get("ct", 20),
             "fournisseurs": {"claude": {"repondus": 1}, "gemini": {"repondus": k.get("gem", 1)}, "astra": {"repondus": 1}},
             "par_monde": {str(w): {"q": q, "C_B": 1, "ell": w % 2} for w in mondes},
             "principal": {"S_R": k.get("S_R", 0.7), "S_R_ic95": [0, 1], "W_R": k.get("W_R", 0), "W_R_sur_n_c_ic95": [0, 1],
                           "L_R": k.get("W_R", 0), "L_R_sur_n_c_ic95": [0, 1], "k_R": k.get("k_R", 0), "W_B": k.get("W_B", 0),
                           "W_B_sur_n_c_ic95": [0, 1], "L_B": 0, "L_B_sur_n_c_ic95": [0, 1], "S_B": 0.88, "S_B_ic95": [0, 1],
                           "C_E_moins_C_B_moyenne": k.get("moy", 0.1), "C_E_moins_C_B_ic95": [-0.1, k.get("haut", 0.3)],
                           "placebo": {"p_choix": k.get("p", 0.5)}},
             "sensibilites": {}, "pertes_par_classe_sommees": {}, "par_proposeur": {}, "audit_R4": {"cartes_cheres_portant_seules": []}}
    return corps


@essai("lecture gelée : étages", "critères de lecture gelés", "sain")
def u_lecture(c):
    LI = c.LI
    man = {"partiel": False, "arret_classe": None}
    v = lambda **k: LI.lire(man, corps_jouet_lecture(**k), None)  # noqa: E731
    assert LI.lire({"partiel": True, "arret_classe": "arret", "arret": "x"}, None, None)["verdict"] == "non jugeable (arrêt)"
    assert LI.lire(man, None, None)["verdict"] == "non jugeable (arrêt)"
    assert LI.lire({"partiel": True, "arret_classe": "fournisseur_abandonne"}, corps_jouet_lecture(), None)["verdict"] == "non concluant"
    assert v(n_c=15)["verdict"] == "non concluant" and v(n_c=16)["verdict"] != "non concluant"
    assert v(gem=0)["verdict"] == "non concluant"
    assert v(ct=9)["verdict"] == "hors de la zone utile" and v(ct=10)["verdict"] != "hors de la zone utile"
    assert v(S_R=0.2499)["verdict"] == "pas d'épargne notable" and v(S_R=0.25)["verdict"] != "pas d'épargne notable"
    assert v(W_R=4, S_R=0.3)["verdict"] == "épargne avec perte établie" and v(W_R=3)["verdict"] == "épargne, perte possible non établie"
    assert v(W_R=0)["verdict"] == "épargne sans perte observée"
    assert v(k_R=3)["etages"]["4"]["verdict"] == "non éprouvable" and v(k_R=17)["etages"]["4"]["verdict"] == "non éprouvable"
    assert v(k_R=4, p=0.05)["etages"]["4"]["verdict"] == "mieux que le hasard"
    assert v(k_R=16, p=0.0501)["etages"]["4"]["verdict"] == "pas mieux que le hasard"
    assert v(k_R=3)["H_v"]["lecture"] == "H-v non éprouvée au crible"
    assert v(k_R=5, W_R=0)["H_v"]["lecture"] == "H-v non réfutée au crible"
    assert v(k_R=5, W_R=4)["H_v"]["lecture"] == "H-v réfutée au crible" and v(k_R=5, S_R=0.1)["H_v"]["lecture"] == "H-v réfutée au crible"
    assert v(k_R=5, W_R=2)["H_v"]["lecture"] == "non tranchée"
    assert v()["etages"]["5"]["verdict"] is None and v()["adoption"].startswith("aucune")
    return "étages 0 à 6 à leurs bornes ; lecture de H-v"


@essai("lecture gelée : prédictions", "prédiction chiffrée", "sain")
def u_predictions(c):
    LI = c.LI
    man = {"partiel": False, "arret_classe": None}

    def p(**k):
        return LI.lire(man, corps_jouet_lecture(**k), None)["predictions"]
    assert p(k_R=3)["V1"]["etat"] == "confirmée" and p(k_R=4)["V1"]["etat"] == "indécise" and p(k_R=8)["V1"]["etat"] == "réfutée"
    assert p(k_R=7)["V1"]["etat"] == "indécise" and p(S_R=0.2499)["V2"]["etat"] == "réfutée" and p(S_R=0.25)["V2"]["etat"] == "indécise"
    assert p(W_R=3)["V3"]["etat"] == "indécise" and p(k_R=16)["V5"]["etat"] == "réfutée" and p(q=0.31)["V6"]["etat"] == "indécise"
    assert p(q=0.79)["V6"]["etat"] == "indécise" and p(moy=-0.01, haut=0.0)["V7"]["etat"] == "indécise"
    assert p(S_R=0.55)["V2"]["etat"] == "confirmée" and p(S_R=0.5)["V2"]["etat"] == "indécise" and p(S_R=0.2)["V2"]["etat"] == "réfutée"
    assert p(W_R=4)["V3"]["etat"] == "confirmée" and p(W_R=1)["V3"]["etat"] == "indécise" and p(W_R=0)["V3"]["etat"] == "réfutée"
    assert p()["V4"]["etat"] == "rapportée sans verdict"
    assert p(k_R=3)["V5"]["etat"] == "confirmée" and p(k_R=4)["V5"]["etat"] == "réfutée" and p(k_R=17)["V5"]["etat"] == "indécise"
    assert p(q=0.3)["V6"]["etat"] == "confirmée" and p(q=0.5)["V6"]["etat"] == "indécise" and p(q=0.8)["V6"]["etat"] == "réfutée"
    assert p(moy=0)["V7"]["etat"] == "confirmée" and p(moy=-0.1, haut=0.1)["V7"]["etat"] == "indécise" \
        and p(moy=-0.2, haut=-0.01)["V7"]["etat"] == "réfutée"
    t = LI.lire(man, corps_jouet_lecture(W_R=0, S_R=0.6), None)["audit_R4"]["trop_propre"]
    assert t["W_R_nul_et_S_R_au_moins_0_6"] is True and t["W_B_nul"] is True
    return "V1 à V7 confirmées, indécises, réfutées à leurs bornes ; V4 sans verdict ; marques de l'audit R4"


UNITAIRES = [u_graine_sain, u_graine_artefact, u_regle_m, u_garde_sain, u_garde_artefact, u_w_min, u_placebo_sain, u_placebo_artefact,
             u_bras, u_reechantillon, u_decider_sain, u_decider_artefact, u_regle_strict, u_jeu_sain, u_jeu_artefact,
             u_cartes_valides, u_carte_au_dela, u_dollars, u_fictive, u_conf_sain, u_conf_artefact, u_addendum_sain,
             u_addendum_artefact, u_module_faux, u_gabarit_sain, u_gabarit_artefact, u_corps_sain, u_corps_artefact, u_coupure,
             u_pieces, u_part_sain, u_part_artefact, u_abandon_sain, u_abandon_artefact, u_releve, u_rapatrier, u_partie_a_sain,
             u_partie_a_artefact, u_lecture, u_predictions]


# =================================================================================================================================
# palier « jouer » : essai à blanc complet avec relais factices (aucun appel réel, aucune clé)
# =================================================================================================================================

def args_jouer(c, sortie, files, **k):
    a = argparse.Namespace(arbre=c.arbre, mode="a_blanc", mondes=c.mondes_f, mondes_sha256=c.H, certifiees=c.certif_f,
                           certifiees_sha256=c.HC, files=files, sortie=sortie, go_kv1=None, go_kv2=None, registre_go=None,
                           texte=None, texte_sha256=c.texte_sha, mondes_shas=None, registre_lancements=None, releve_sonde=None,
                           addendum=None, addendum_sha256=None, scenarios=None, lent=None, configuration=None, echeance_utc_s=None,
                           duree_d_s=None, borne_essai_s=None, decalage_ports=c.decalage)
    for x, v in k.items():
        setattr(a, x, v)
    return a


def lancer_jouer(c, nom, files, crochets=None, **k):
    sortie = os.path.join(c.travail, nom)
    try:
        code = c.L.jouer(args_jouer(c, sortie, files, **k), crochets)
    except c.K.Refus as e:
        return 2, sortie, str(e)
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == "Refus":
            return 2, sortie, str(e)
        raise
    return code, sortie, None


def relire(sortie, nom):
    return json.load(open(os.path.join(sortie, nom), encoding="utf-8"))


# Référence de la mesure : la moitié bon marché ne rend que des copies de K1 dans les mondes 1 à 5 (Pr-1 partout, Pr-2 aux cinq
# premiers appels) ; la moitié chère, des cartes au-delà de K1 partout : la règle appelle les chers dans ces cinq mondes, la moitié
# chère y porte seule des composantes (W_B > 0), le placebo est éprouvable (4 ≤ k_R ≤ n_c − 4).
SCENARIOS_REFERENCE = "argon=k1_seul,opus55=k1_plus;1=k1_seul;2=k1_seul;3=k1_seul;4=k1_seul;5=k1_seul"


@essai("essai à blanc complet, M = 1, coupure à B_a simulée", "appel plus long que B_a ; corps servis ; pièces", "sain")
def j_blanc_m1(c):
    code, s, err = lancer_jouer(c, "blanc-m1", 1, lent="3:astra", borne_essai_s=20, scenarios=SCENARIOS_REFERENCE)
    assert code == 0, f"code {code} {err}"
    rel = relire(s, "releve-crible-v-v1.json")
    assert rel["comptes"] == {"complet": 79, "tronque": 0, "echec": 1} and rel["coupures"] == 1, rel["comptes"]
    a = [x for x in rel["appels"] if x["monde"] == 3 and x["proposeur"] == "astra"][0]
    assert a["etat"] == "echec" and a["coupe_a_B_a"] and a["cause"] == "au_dela_de_B_a" and not a["abandon"], a
    cp = [json.loads(x) for x in open(os.path.join(s, "coupures-crible-v-v1.jsonl"))]
    assert cp == [{"monde": 3, "proposeur": "astra", "borne_s": 20, "duree_s": cp[0]["duree_s"], "etat": "echec", "reprise": False}]
    dol = {(x["monde"], x["proposeur"]): x for x in relire(s, "DOLLARS.json")["appels"]}
    assert dol[(3, "astra")]["source"] == "plafond_coupure" and dol[(3, "astra")]["cout_config_usd"] == 2.34, dol[(3, "astra")]
    assert all(v["source"] == "journal_relais" for k_, v in dol.items() if k_ != (3, "astra"))
    man = relire(s, "manifeste-crible-v-v1.json")
    assert man["files"] == [list(range(1, 21))] and len(man["relais"]["0"]) == 4
    servis = man["controles"]["textes_servis"]
    for x in rel["appels"]:
        assert x["texte_servi_sha256"] == servis[str(x["monde"])]["sha256"], "corps servi ≠ corps préparé"
    for w in range(1, 21):
        for n in c.K.PROPOSEURS:
            t = json.load(open(os.path.join(s, f"monde-{w}", n, "temoin-isolement.json")))
            assert t["texte_servi_sha256"] == servis[str(w)]["sha256"]
            assert t["conforme"] is (None if (w, n) == (3, "astra") else True)
    jn = [json.loads(x) for x in open(os.path.join(s, "journal-relais-f0-astra.jsonl"))]
    assert len(jn) == 19, "le relais n'a reçu que les appels non coupés (jamais de reprise)"
    c.reference = s
    return "80 appels, 1 coupure à B_a simulée (20 s) comptée « échec », journalisée, au plafond de session, jamais reprise"


@essai("essai à blanc complet, M = 2 (8 relais), deux coupures", "files parallèles ; appel plus long que B_a", "sain")
def j_blanc_m2(c):
    code, s, err = lancer_jouer(c, "blanc-m2", 2, lent="3:astra,4:opus55", borne_essai_s=20)
    assert code == 0, f"code {code} {err}"
    rel = relire(s, "releve-crible-v-v1.json")
    assert rel["comptes"] == {"complet": 78, "tronque": 0, "echec": 2} and rel["coupures"] == 2
    man = relire(s, "manifeste-crible-v-v1.json")
    assert man["files"] == [list(range(1, 21, 2)), list(range(2, 21, 2))] and sorted(man["relais"]) == ["0", "1"]
    for k in ("0", "1"):
        for n, e in man["relais"][k].items():
            p = {"fable52": 3.0, "opus55": 2.0, "argon": 2.34, "astra": 2.34}[n]
            assert abs(e["plafond_usd"] - 10 * p) < 1e-9 and e["max_appels"] == 10, (k, n, e)
    return "deux files de dix mondes, 4 relais par file (plafond = 10 plafonds de session), deux coupures"


@essai("panne de relais d'un fournisseur ayant répondu", "fournisseur abandonné…", "sain")
def j_panne_sain(c):
    code, s, err = lancer_jouer(c, "panne-sain", 1, scenarios="opus55=k1_plus;2=panne")
    rel = relire(s, "releve-crible-v-v1.json")
    assert code == 0 and rel["arret"] is None, (code, err, rel["arret"])
    claude = [x for x in rel["appels"] if x["proposeur"] in ("opus55", "fable52") and x["monde"] >= 3]
    assert all(x["etat"] == "echec" and x["appele"] is False for x in claude), "appels restants de la clé commune « échec » sans être lancés"
    return f"abandon de la voie à clé commune au monde 2 ; le crible continue ; {len(claude)} appels non lancés"


@essai("panne de relais d'un fournisseur", "fournisseur abandonné…", "artefact")
def j_panne_artefact(c):
    code, s, _ = lancer_jouer(c, "panne-premier", 1, scenarios="argon=panne")
    rel = relire(s, "releve-crible-v-v1.json")
    assert code == 3 and "perdu en entier" in (rel["arret"] or ""), (code, rel["arret"])
    assert all(x["appele"] is False for x in rel["appels"] if x["monde"] >= 2), "aucune dépense de plus après l'arrêt"
    code2, s2, _ = lancer_jouer(c, "panne-minimum", 1, scenarios="opus55=k1_plus;2=panne,argon=k1_plus;3=panne")
    rel2 = relire(s2, "releve-crible-v-v1.json")
    assert code2 == 3 and "minimum" in (rel2["arret"] or ""), (code2, rel2["arret"])
    assert rel2["arret_classe"] == "fournisseur_abandonne" and os.path.isfile(os.path.join(s2, "CARTES.json"))
    return f"première panne sans répondu : {rel['arret'][:80]} ; minimum impossible au monde 3 : {rel2['arret'][:80]}"


@essai("coût au-dessus du pire cas", "coût d'un appel au-dessus de son pire cas", "artefact")
def j_cout(c):
    code, s, _ = lancer_jouer(c, "cout", 1, scenarios="fable52=k1_plus;4=cout_excessif")
    rel = relire(s, "releve-crible-v-v1.json")
    assert code == 3 and "pire cas" in (rel["arret"] or ""), (code, rel["arret"])
    a = [x for x in rel["appels"] if x["monde"] == 4 and x["proposeur"] == "fable52"][0]
    assert a.get("arret") is True and a["appele"], a
    return f"arrêt code 3, dépense comptée : {rel['arret'][:100]}"


@essai("corps servi altéré", "corps servi différent entre les quatre appels d'un monde", "artefact")
def j_corps(c):
    def corps(w, cp):
        if w == 5:
            s = dict(cp["opus55"])
            s["episodes_sha256"] = "0" * 64
            cp["opus55"] = s
    code, s, _ = lancer_jouer(c, "corps", 1, crochets={"corps": corps})
    rel = relire(s, "releve-crible-v-v1.json")
    assert code == 3 and "corps servi" in (rel["arret"] or ""), (code, rel["arret"])
    assert not any(x["appele"] for x in rel["appels"] if x["monde"] >= 5), "arrêt avant les appels du monde"
    return rel["arret"][:120]


@essai("témoin d'isolement supprimé", "réponse brute ou témoin d'isolement absent", "artefact")
def j_temoin(c):
    def apres(w, n, d):
        if (w, n) == (2, "argon"):
            os.unlink(os.path.join(d, "temoin-isolement.json"))
    code, s, _ = lancer_jouer(c, "temoin", 1, crochets={"apres_appel": apres})
    rel = relire(s, "releve-crible-v-v1.json")
    assert code == 3 and "temoin-isolement" in (rel["arret"] or ""), (code, rel["arret"])
    return rel["arret"][:120]


@essai("garde de départ dans le lanceur", "minuterie de la machine", "artefact")
def j_garde(c):
    code, s, err = lancer_jouer(c, "garde", 1, echeance_utc_s=time.time() + 30000, duree_d_s=5000)
    assert code == 2 and "garde de départ" in (err or "") and not os.path.exists(s), (code, err)
    code2, s2, err2 = lancer_jouer(c, "garde-sain", 1, echeance_utc_s=time.time() + 61200, duree_d_s=5000)
    assert code2 == 0, (code2, err2)
    return f"échéance proche : refus avant tout dossier ({err[:80]}) ; marge suffisante : joué"


@essai("mode réel sans ses pièces", "toute dépense sans ligne « calcul »… ; relevé de sonde absent", "artefact")
def j_reel_refus(c):
    code, s, err = lancer_jouer(c, "reel", 1, mode="reel")
    assert code == 2 and "options exigées absentes" in (err or "") and not os.path.exists(s), (code, err)
    code2, s2, err2 = lancer_jouer(c, "reel-crochet", 1, crochets={"corps": lambda w, cp: None}, mode="reel")
    assert code2 == 2 and not os.path.exists(s2), (code2, err2)
    return f"refus avant tout dossier : {err[:100]}"


JOUER = [j_blanc_m1, j_blanc_m2, j_panne_sain, j_panne_artefact, j_cout, j_corps, j_temoin, j_garde, j_reel_refus]


# =================================================================================================================================
# palier « mesure » : la mesure jouée une fois sur l'essai à blanc, ses calculs recalculés indépendamment
# =================================================================================================================================

def copier_reference(c, nom):
    d = os.path.join(c.travail, nom)
    shutil.copytree(c.reference, d)
    for f in os.listdir(d):
        if f.startswith("sortie-") or f.startswith("mesure-crible") or f.startswith("lecture-"):
            os.unlink(os.path.join(d, f))
    return d


def lanceur_cli(c, *a):
    return subprocess.run([sys.executable, "-I", "-B", os.path.join(c.code, "lanceur_crible_v_v1.py"), *a], capture_output=True,
                          text=True)


@essai("mesure une seule fois par le lanceur, sortie scellée, lecture", "lecture avant le scellement ; mesure lancée deux fois", "sain")
def m_mesure(c):
    d = copier_reference(c, "mesure")
    r = lanceur_cli(c, "mesurer", "--arbre", c.arbre, "--sortie", d, "--mondes", c.mondes_f, "--mondes-sha256", c.H, "--certifiees",
                    c.certif_f, "--certifiees-sha256", c.HC, "--texte-sha256", c.texte_sha)
    assert r.returncode == 0, r.stderr[-600:]
    for f in ("sortie-mesure-crible-v-v1.json", "sortie-fictive-crible-v-v1.json", "mesure-crible-v-v1.json"):
        assert c.K.compagnon_egal(os.path.join(d, f)), f
    r2 = lanceur_cli(c, "lire", "--sortie", d, "--ecrire", os.path.join(d, "lecture-crible-v-v1.json"))
    assert r2.returncode == 0 and "lecture_sha256" in r2.stdout, r2.stderr
    c.mesure = d
    return "sortie principale puis fictive scellées, pièce de liaison, lecture écrite"


def cartes_synthetiques(c, d):
    """Jeu de cartes de référence de la mesure, écrit ici depuis les mondes d'essai (aucun appel) : la moitié bon marché ne rend
    que des copies de K1 aux mondes 1 à 5 (la règle y appelle les chers), K1 et le monde réduit à K1 et une composante moyenne
    ailleurs ; la moitié chère rend le monde réduit à K1 et toutes ses certifiées ; pièges : une carte au-delà de six, une carte
    refusée et une carte d'un appel tronqué, toutes trois porteuses du monde entier, une carte non évaluable ; l'appel de Pr-3 au
    monde 3 en échec (coupé à B_a, au plafond de session)."""
    K, M = c.K, c.M
    certif = json.load(open(c.certif_f))["mondes"]
    cartes, appels, dol = [], [], []
    prix = {"argon": 0.6, "opus55": 0.26, "astra": 0.42, "fable52": 2.5}
    for w in c.mondes:
        r, spec = w["monde"], w["spec"]
        pm = c.MC.preparer_monde(M, c.P1, w)
        k1, e1 = pm["k1"], pm["eid_k1"]
        moy = [e["id"] for e in spec["effets"] if e["classe"] == "moyenne" and e["id"] in certif[str(r)]["certifiees"]]
        rb = M.monde_restreint(spec, [e1] + moy[:1])
        re_ = M.monde_restreint(spec, [e1] + certif[str(r)]["certifiees"])
        tout = M.compiler_monde(spec)
        par = {"argon": [k1, k1] if r <= 5 else [k1, rb], "opus55": [k1], "astra": [re_], "fable52": [re_]}
        for p in K.PROPOSEURS:
            etat = "echec" if (r, p) == (3, "astra") else "tronque" if (r, p) == (4, "fable52") else "complet"
            appels.append({"monde": r, "proposeur": p, "etat": etat})
            if etat == "complet":
                for i, loi in enumerate(par[p], start=1):
                    cartes.append({"monde": r, "proposeur": p, "emplacement": i, "etat": "admise", "loi": loi})
            elif etat == "tronque":
                cartes.append({"monde": r, "proposeur": p, "emplacement": 1, "etat": "admise", "loi": tout})
            dol.append({"monde": r, "proposeur": p, "cout_config_usd": 2.34 if etat == "echec" else prix[p],
                        "source": "plafond_coupure" if etat == "echec" else "journal_relais"})
        if r == 2:
            cartes.append({"monde": r, "proposeur": "argon", "emplacement": 7, "etat": "refusee", "loi": tout})
            cartes.append({"monde": r, "proposeur": "opus55", "emplacement": 2, "etat": "refusee", "loi": tout})
            cartes.append({"monde": r, "proposeur": "opus55", "emplacement": 3, "etat": "admise", "loi": {"type": "inconnu"}})
    json.dump({"cartes": cartes, "appels": appels}, open(os.path.join(d, "CARTES.json"), "w"))
    json.dump({"version": "dollars-crible-v-v1", "appels": dol}, open(os.path.join(d, "DOLLARS.json"), "w"))


@essai("programme de mesure joué directement", "métrique (programme de mesure du dossier essayé)", "sain")
def m_programme(c):
    ref = os.path.join(c.travail, "programme")
    os.makedirs(ref)
    cartes_synthetiques(c, ref)
    so = os.path.join(ref, "sortie-mesure-crible-v-v1.json")
    r = subprocess.run([sys.executable, "-I", "-B", os.path.join(c.code, "mesure_crible_v_v1.py"), "mesurer", "--mr2", c.mr2,
                        "--texte-sha256", c.texte_sha, "--mondes", c.mondes_f, "--certifiees", c.certif_f, "--cartes",
                        os.path.join(ref, "CARTES.json"), "--dollars", os.path.join(ref, "DOLLARS.json"), "--configuration", c.A.CONF,
                        "--sortie", so, "--sortie-fictive", os.path.join(ref, "sortie-fictive-crible-v-v1.json")],
                       capture_output=True, text=True)
    assert r.returncode == 0, f"code {r.returncode} : {r.stderr[-500:]}"
    assert c.K.compagnon_egal(so) and c.K.compagnon_egal(os.path.join(ref, "sortie-fictive-crible-v-v1.json"))
    c.mesure = ref
    return "sortie principale puis sortie fictive scellées"


@essai("seconde mesure", "mesure lancée deux fois", "artefact")
def m_seconde(c):
    r = lanceur_cli(c, "mesurer", "--arbre", c.arbre, "--sortie", c.mesure, "--mondes", c.mondes_f, "--mondes-sha256", c.H,
                    "--certifiees", c.certif_f, "--certifiees-sha256", c.HC, "--texte-sha256", c.texte_sha)
    assert r.returncode == 2 and "une seule fois" in r.stderr, (r.returncode, r.stderr[-300:])
    return r.stderr.strip()[-160:]


@essai("mesure recalculée indépendamment", "métrique ; couverture ; dollars ; placebo ; rééchantillonnage ; jeu public", "sain")
def m_recalcul(c):
    import numpy as np
    K, MC, M = c.K, c.MC, c.M
    s = json.load(open(os.path.join(c.mesure, "sortie-mesure-crible-v-v1.json")))["corps"]
    cartes = json.load(open(os.path.join(c.mesure, "CARTES.json")))
    dollars = {(x["monde"], x["proposeur"]): x["cout_config_usd"] for x in json.load(open(os.path.join(c.mesure, "DOLLARS.json")))["appels"]}
    etat = {(a["monde"], a["proposeur"]): a["etat"] for a in cartes["appels"]}
    certif = json.load(open(c.certif_f))["mondes"]
    racine = K.racine_des_graines(c.texte_sha)
    pm_ = {w["monde"]: MC.preparer_monde(M, c.P1, w) for w in c.mondes}
    cache = {}
    val = {k: [] for k in etat}
    for x in cartes["cartes"]:  # validité recalculée ici, sans la fonction de la mesure
        k = (x["monde"], x["proposeur"])
        if x["emplacement"] <= 6 and x["etat"] == "admise" and etat[k] == "complet" and MC.evaluable(M, x["loi"], pm_[x["monde"]]):
            val[k].append(x)
    rep = {k: etat[k] == "complet" and bool(val[k]) for k in etat}
    complets = [w for w in range(1, 21) if any(rep[(w, p)] for p in K.MOITIE_B) and any(rep[(w, p)] for p in K.MOITIE_E)]
    assert s["n_c"] == len(complets) and s["mondes_complets"] == complets, (s["n_c"], len(complets))
    assert len(complets) == 20, "monde complet = au moins un appel répondu par moitié (le monde 3 n'a que trois appels)"
    ell, CB, CT = {}, {}, {}
    for w in complets:
        pm = pm_[w]
        excl = {pm["eid_k1"]} | MC.porte(pm, pm["k1"], cache)[0]
        compt = set(certif[str(w)]["certifiees"]) - excl
        cov = lambda props: set().union(*[MC.porte(pm, x["loi"], cache)[0] for p in props for x in val[(w, p)]] or [set()]) & compt  # noqa: E731
        CT[w], CB[w] = len(cov(K.PROPOSEURS)), len(cov(K.MOITIE_B))
        ell[w] = CT[w] - CB[w]
        assert s["par_monde"][str(w)]["C_T"] == CT[w] and s["par_monde"][str(w)]["C_B"] == CB[w], (w, s["par_monde"][str(w)], CT[w], CB[w])
        jeu = MC.jeu_public(M, racine, w)
        assert s["jeux_publics_sha256"][str(w)] == MC.empreinte_du_jeu(jeu), "jeu public ≠ celui de (r, 30)"
    rp = {"argon": 0.2, "opus55": 1.0, "astra": 1.0, "fable52": 1.0}
    db = {w: sum(dollars[(w, p)] * rp[p] for p in K.MOITIE_B) for w in complets}
    de = {w: sum(dollars[(w, p)] * rp[p] for p in K.MOITIE_E) for w in complets}
    a = [s["par_monde"][str(w)]["a"] for w in complets]
    cache_d = {}
    for w in complets:  # q_w recalculée ici : copies (sens dirigé, ε, ε_strat) parmi les seules cartes valides de la moitié bon marché
        jeu = MC.jeu_public(M, racine, w)
        lois = [x["loi"] for p in K.MOITIE_B for x in val[(w, p)]]
        cop = 0
        for loi in lois:
            eg, dd, _ = MC.distances(M, c.CS, loi, pm_[w]["k1"], jeu, cache_d)
            cop += bool(eg or (dd[0] < 0.01 and dd[1] < 0.04))
        q = cop / len(lois)
        assert abs(s["par_monde"][str(w)]["q"] - q) < 1e-12, (w, s["par_monde"][str(w)]["q"], q)
        assert s["par_monde"][str(w)]["a"] == (1 if q > 0.8 else 0)
    SR = 1 - (sum(db.values()) + sum(ai * de[w] for ai, w in zip(a, complets))) / (sum(db.values()) + sum(de.values()))
    assert abs(s["principal"]["S_R"] - SR) < 1e-9, (s["principal"]["S_R"], SR)
    WR = sum(1 for ai, w in zip(a, complets) if ai == 0 and ell[w] >= 1)
    assert s["principal"]["W_R"] == WR and s["principal"]["W_B"] == sum(1 for w in complets if ell[w] >= 1)
    kR = sum(a)
    assert s["principal"]["placebo"]["ensembles"] == math.comb(len(complets), kR) and s["principal"]["placebo"]["taille"] == kR
    n = len(complets)
    idx = np.stack([np.random.default_rng(np.random.SeedSequence(entropy=racine, spawn_key=(99, b))).integers(0, n, n) for b in range(10000)])
    ev = np.array([ell[w] for w in complets], float)
    lb = ev[idx].sum(axis=1) / n
    assert np.allclose(s["principal"]["L_B_sur_n_c_ic95"], [np.percentile(lb, 2.5), np.percentile(lb, 97.5)]), "rééchantillonnage"
    f = json.load(open(os.path.join(c.mesure, "sortie-fictive-crible-v-v1.json")))["corps"]
    assert set(f) == MC.CLES_FICTIVES and f["sortie_principale_sha256"] == c.K.sha256_fichier(os.path.join(c.mesure, "sortie-mesure-crible-v-v1.json"))
    lf = os.path.join(c.mesure, "lecture-crible-v-v1.json")
    if os.path.isfile(lf):
        lec = json.load(open(lf))
        assert lec["verdict"] and lec["predictions"]["V1"]["k_R"] == kR
    assert kR == 5 and s["principal"]["W_B"] >= 10 and WR >= 1, (kR, s["principal"]["W_B"], WR)
    assert s["cartes"] == {"refusees": 1, "au_dela_de_six": 1, "non_evaluables": 1, "d_appels_tronques": 1}, s["cartes"]
    Lr = sum(ell[w] for ai, w in zip(a, complets) if ai == 0)
    pc = sum(1 for A in itertools.combinations(range(n), kR) if sum(ell[complets[i]] for i in range(n) if i not in A) <= Lr) / math.comb(n, kR)
    assert abs(s["principal"]["placebo"]["p_choix"] - pc) < 1e-12, (s["principal"]["placebo"]["p_choix"], pc)
    return (f"n_c = {n}, k_R = {kR}, S_R = {SR:.4f}, W_R = {WR}, W_B = {s['principal']['W_B']}, p_choix = {pc:.4f} : égaux au recalcul (cartes valides, "
            f"couvertures hors K1, dollars publics, placebo, rééchantillonnage, jeux publics)")


@essai("exception de la mesure", "exception de la mesure (pas un refus nommé)", "artefact")
def m_exception(c):
    d = tempfile.mkdtemp()
    for f in os.listdir(c.code):
        if f.endswith(".py"):
            shutil.copyfile(os.path.join(c.code, f), os.path.join(d, f))
    p = os.path.join(d, "mesure_crible_v_v1.py")
    t = open(p).read().replace('    V4, M, P1, CS = charger_mr2(racine_mr2)\n    racine = K.racine_des_graines(texte_sha256)',
                               '    V4, M, P1, CS = charger_mr2(racine_mr2)\n    racine = K.racine_des_graines(texte_sha256) // 0', 1)
    open(p, "w").write(t)
    ref = copier_reference(c, "exception")
    so = os.path.join(ref, "sortie-mesure-crible-v-v1.json")
    r = subprocess.run([sys.executable, "-I", "-B", p, "mesurer", "--mr2", c.mr2, "--texte-sha256", c.texte_sha, "--mondes", c.mondes_f,
                        "--certifiees", c.certif_f, "--cartes", os.path.join(ref, "CARTES.json"), "--dollars", os.path.join(ref, "DOLLARS.json"),
                        "--configuration", c.A.CONF, "--sortie", so, "--sortie-fictive", so + ".fictive"], capture_output=True, text=True)
    shutil.rmtree(d)
    assert r.returncode not in (0, 2) and not os.path.exists(so), (r.returncode, os.path.exists(so))
    return f"division par zéro forcée : code {r.returncode}, aucune sortie"


MESURE = [m_mesure, m_seconde, m_programme, m_recalcul, m_exception]


def principal(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("palier", choices=("unitaire", "jouer", "mesure"))
    a.add_argument("--code", required=True)
    a.add_argument("--arbre", required=True)
    a.add_argument("--essai", required=True)
    a.add_argument("--travail", default=None)
    a.add_argument("--reference", default=None)
    a.add_argument("--decalage-ports", type=int, default=0)
    a.add_argument("--seulement", default=None)
    a.add_argument("--sortie", required=True)
    args = a.parse_args(argv)
    c = charger(os.path.abspath(args.code), os.path.abspath(args.arbre), os.path.abspath(args.essai))
    c.decalage = args.decalage_ports
    c.travail = args.travail
    if c.travail:
        os.makedirs(c.travail)
    debut = time.time()
    liste = {"unitaire": UNITAIRES, "jouer": JOUER, "mesure": MESURE}[args.palier]
    if args.seulement:
        liste = [f for f in liste if f.__name__ in args.seulement.split(",")]
    if args.palier == "mesure":
        c.reference = os.path.abspath(args.reference)
    jouer_essais(liste, c)
    out = {"palier": args.palier, "code": args.code, "essais": RESULTATS, "echecs": sum(1 for r in RESULTATS if not r["ok"]),
           "duree_s": round(time.time() - debut, 1)}
    with open(args.sortie, "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({"palier": args.palier, "essais": len(RESULTATS), "echecs": out["echecs"], "duree_s": out["duree_s"]}))
    return 0 if out["echecs"] == 0 else 1


if __name__ == "__main__":
    sys.exit(principal())
