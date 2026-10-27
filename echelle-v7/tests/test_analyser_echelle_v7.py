"""Gardes et lecture de `analyser_echelle_v7.py` (R5 ; CLU-01, CLV-01, CLV-07, CLV-08, CLW-01, CLW-02, CLW-04, CLW-09, CLZ-01,
CLZ-02, CLZ-11, CLY-01, CLY-02, CLY-06, CLY-08, CLY-14, et les gardes de la v2) :
- lecture mécanique sur des intervalles fabriqués : une branche par issue, conditions de « positif » et de « inverse »
  refusées une à une, issues non confirmées et désaccord des deux sens, issues compatibles (« nul » avec « pas de
  fuite » ou une fuite de signe inverse, CLW-01), fuite de signe inverse lue modèle par modèle : tenue par des modèles
  différents dans les deux sens, par le même avec l'autre dans un seul (CLV-01), réserves de chaque issue (CLW-02),
  restreintes aux modèles prononcés (CLV-01), et chaque cas rejoué en miroir (sens échangés) ; conditions manquantes
  chiffrées (CLZ-02), pour chaque issue tenue dans un seul sens (CLV-07) ; cohérence des deux sens (CLU-01) :
  artefacts de cl6 (écart d'échelle porté par un modèle différent dans chaque sens) pour « positif », « inverse » et
  « nul », bornes de l'écart ponctuel, un seul modèle incohérent, issues qui ne la demandent pas ; texte des réserves
  (modèle et sens nommés, CLU-05) ;
- intégration sur des activations synthétiques à vérité connue : positif confirmé dans les deux sens ; signatures
  croisées de signes opposés sous une fuite égale, en dimension 256, et leur miroir, cas sain sous H_A, contexte du jeu
  b plus faible (CLU-01) ; signature du
  jeu a, de signe positif (CLY-01) et négatif (CLZ-01), au petit et au grand (CLW-09) ; signature du jeu b ;
  signatures croisées négatives, dans les deux ordres (CLV-01) ; effet vrai masqué par une signature négative
  (CLZ-01) ; « nul » tenu dans les deux sens avec « pas de fuite » dans un seul (CLW-01) ; réserve « profondeur » sur
  quatre couches, pour chaque issue, cas sain et artefact (CLZ-11, CLV-08) ; forces de paires inégales sans fausse
  réserve (CLY-02) ; nul strict ; invariance par translation ; témoin de permutation sensible ;
- gardes du mode décisif (commit, arbre, numpy) et d'identité (une sous-garde par test, script de mesure compris,
  CLW-04).
Lancement : python -m pytest -q echelle-v7/tests
"""
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys

import numpy as np
import pytest

ICI = pathlib.Path(__file__).resolve().parent
SCRIPTS = ICI.parent / "scripts"


def charger(nom):
    spec = importlib.util.spec_from_file_location(nom, SCRIPTS / f"{nom}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


AN = charger("analyser_echelle_v7")
N_BOOT_ESSAI = 300
COMMIT_ESSAI = "c" * 40
PETITS = {"petit": {"modele": "essai/petit", "revision": "r-petit", "couches": [4, 6], "dimension": 64},
          "grand": {"modele": "essai/grand", "revision": "r-grand", "couches": [4, 6], "dimension": 64}}


@pytest.fixture(scope="module")
def stimuli(tmp_path_factory):
    d = tmp_path_factory.mktemp("stim") / "s"
    subprocess.run([sys.executable, "-I", "-B", str(SCRIPTS / "construire_echelle_v2.py"), str(d)], check=True,
                   capture_output=True)
    return d / "echelle-v2.json"


@pytest.fixture(autouse=True)
def reglages(monkeypatch):
    monkeypatch.setattr(AN, "N_BOOT", N_BOOT_ESSAI)
    monkeypatch.setattr(AN, "ATTENDUS", PETITS)
    monkeypatch.setattr(AN, "etat_scripts", lambda: (COMMIT_ESSAI, True))


def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def sceller(f):
    f = pathlib.Path(f)
    (f.parent / (f.name + ".sha256")).write_text(f"{sha(f)}  {f.name}\n", encoding="utf-8")


def fabriquer(dossier, stimuli, alpha, graine, nom="petit", force_c=4.0, beta=0.0, signature=0.0, signature_b=0.0,
              kappa=0.0, tau=0.15, translation=0.0, d=64, couches=(4, 6), alpha_couches=None, contexte_b=1.0,
              **manifeste):
    """x = contenu + s_f·F + s_c·κ(jeu, paire)·C + cadrage + bruit (+ translation), avec
    F = alpha·C + F⊥ + beta·(contrastes entre paires du jeu a) + signature·(moyenne des particularités du jeu a)
        + signature_b·(moyenne des particularités du jeu b).
    Toutes les couches sauf la dernière portent un contexte deux fois plus faible ; contexte_b multiplie l'effet du
    contexte sur les stimuli du jeu b. λ vrai (concept) ≈ alpha, ou alpha_couches[c] à la couche c."""
    doc = json.loads(pathlib.Path(stimuli).read_text(encoding="utf-8"))
    st = doc["stimuli"]
    rng = np.random.default_rng(graine)
    base = np.linalg.qr(rng.normal(size=(d, 4)))[0].T
    C, Fp = base[0] * force_c, base[2] * 2.0
    contenus = rng.normal(size=(64, d))
    cadrage = {}
    for s in st:
        cle = (s["jeu"], s["paire"], s["classe"])
        if cle not in cadrage:
            cadrage[cle] = rng.normal(size=d) * tau
    kap = {(j, p): 1.0 + kappa * rng.normal() for j in ("a", "b") for p in range(6)}
    diffs = [cadrage[("a", j, "eval")] - cadrage[("a", j, "reel")] for j in range(6)]
    signes = rng.choice([-1.0, 1.0], size=6)
    gen = sum(sg * dj for sg, dj in zip(signes, diffs))
    gen = gen / np.linalg.norm(gen) * force_c
    sig = sum(diffs) / 6
    sig = sig / np.linalg.norm(sig) * force_c
    sig_b = sum(cadrage[("b", j, "eval")] - cadrage[("b", j, "reel")] for j in range(6)) / 6
    sig_b = sig_b / np.linalg.norm(sig_b) * force_c
    decal = rng.normal(size=d)
    decal = decal / np.linalg.norm(decal) * translation
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True)
    ids, sorties = [s["id"] for s in st], {}
    bruit = rng.normal(size=(len(st), d))
    for k, c in enumerate(couches):
        ech = 1.0 if k == len(couches) - 1 else 0.5
        a_c = (alpha_couches or {}).get(c, alpha)
        F = a_c * C * ech + Fp + beta * gen + signature * sig + signature_b * sig_b
        X = np.empty((len(st), d))
        for i, s in enumerate(st):
            sf = 0.5 if s["format"] == "qcm" else -0.5
            sc = 0.5 if s["classe"] == "eval" else -0.5
            kb = contexte_b if s["jeu"] == "b" else 1.0
            X[i] = contenus[s["contenu"]] + sf * F + sc * kap[(s["jeu"], s["paire"])] * kb * C * ech \
                + cadrage[(s["jeu"], s["paire"], s["classe"])] + bruit[i] + decal
        f = dossier / f"activations-L{c}.npy"
        np.save(f, X.astype(np.float16))
        sceller(f)
        sorties[f.name] = sha(f)
    f_ids = dossier / "ids.json"
    f_ids.write_text(json.dumps(ids) + "\n", encoding="utf-8")
    sceller(f_ids)
    sorties["ids.json"] = sha(f_ids)
    m = {"modele": PETITS[nom]["modele"], "revision": PETITS[nom]["revision"], "couches": list(couches), "dimension": d,
         "type_nombre": "bfloat16", "limite": None, "sha256_stimuli": sha(stimuli), "rendu_premier": "<gabarit>",
         "dernier_jeton": "<fin>", "sha256_sorties": sorties, "script": "mesurer_echelle_v7.py",
         "sha256_script": sha(SCRIPTS / "mesurer_echelle_v7.py")}
    m.update(manifeste)
    (dossier / "manifeste-mesure.json").write_text(json.dumps(m), encoding="utf-8")
    sceller(dossier / "manifeste-mesure.json")
    return dossier


def analyser(tmp_path, stimuli, petit, grand, nom="sortie", repetition=False, commit=COMMIT_ESSAI):
    sortie = tmp_path / nom
    args = [str(stimuli), str(petit), str(grand), "12345", str(sortie)]
    args += ["--repetition"] if repetition else ["--commit-attendu", commit]
    code = AN.principal(args)
    lu = json.loads((sortie / "analyse-echelle-v7.json").read_text(encoding="utf-8")) if code == 0 else None
    return code, lu


# ---------- lecture mécanique ----------

def r_fictif(lp, lg, dl, lp_ba=None, lg_ba=None, dl_ba=None, sp=(0.1, 0.5), sp_ba=None, cert=(0.8, 0.8),
             cert_ba=None, prof=False, prof_ba=False, ssi=(0.1, 0.5), ssi_ba=None, ecart=None):
    """Intervalles fabriqués ; le sens b→a reprend ceux du sens a→b, sauf mention. `prof` vaut pour toutes les issues
    (booléen) ou pour celles d'un ensemble ; `ssi` est l'intervalle de la spécificité de signe inverse (−λ − ν), le même
    pour les deux modèles, ou un dictionnaire par modèle. `ecart` est le point de λ_a→b(m) − λ_b→a(m) (CLU-01), le même
    pour les deux modèles, ou un dictionnaire par modèle ; par défaut, la différence des milieux des deux intervalles de
    λ du modèle ; son intervalle est le point ± 0,1."""
    lp_ba, lg_ba, dl_ba = lp_ba or lp, lg_ba or lg, dl_ba or dl
    sp_ba, cert_ba, ssi_ba = sp_ba or sp, cert_ba or cert, ssi_ba or ssi

    def par_modele(v, k):
        return list(v[k] if isinstance(v, dict) else v)

    if ecart is None:
        ecart = {"petit": (lp[0] + lp[1]) / 2 - (lp_ba[0] + lp_ba[1]) / 2,
                 "grand": (lg[0] + lg[1]) / 2 - (lg_ba[0] + lg_ba[1]) / 2}
    point = {k: (ecart[k] if isinstance(ecart, dict) else ecart) for k in ("petit", "grand")}

    def drapeau(p, x):
        return x in p if isinstance(p, (set, frozenset)) else p

    return {"petit": {"ab": {"A_ctx_fixe_ic": [cert[0], 0.95], "lambda_ic": list(lp)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[0], 0.95], "lambda_ic": list(lp_ba)}},
            "grand": {"ab": {"A_ctx_fixe_ic": [cert[1], 0.95], "lambda_ic": list(lg)},
                      "ba": {"A_ctx_fixe_ic": [cert_ba[1], 0.95], "lambda_ic": list(lg_ba)}},
            "delta_lambda_ic": {"ab": list(dl), "ba": list(dl_ba)},
            "specificite_ic": {"ab": list(sp), "ba": list(sp_ba)},
            "specificite_signe_inverse_ic": {k: {"ab": par_modele(ssi, k), "ba": par_modele(ssi_ba, k)}
                                             for k in ("petit", "grand")},
            "profondeur_contraire": {x: {"ab": drapeau(prof, x), "ba": drapeau(prof_ba, x)} for x in AN.ISSUES},
            "ecart_sens": point, "ecart_sens_ic": {k: [point[k] - 0.1, point[k] + 0.1] for k in point}}


def miroir(kw):
    """Échange les deux sens d'un cas fabriqué (R4 appliquée aux tests : chaque règle vaut dans les deux sens)."""
    ab = {"sp": (0.1, 0.5), "cert": (0.8, 0.8), "ssi": (0.1, 0.5),
          **{k: kw[k] for k in ("lp", "lg", "dl", "sp", "cert", "ssi") if k in kw}}
    ba = {**ab, **{k[:-3]: kw[k] for k in ("lp_ba", "lg_ba", "dl_ba", "sp_ba", "cert_ba", "ssi_ba") if k in kw}}
    out = {**ba, **{k + "_ba": v for k, v in ab.items()}}
    out["prof"], out["prof_ba"] = kw.get("prof_ba", False), kw.get("prof", False)
    if "ecart" in kw:                                    # λ_a→b − λ_b→a change de signe (CLU-01)
        e = kw["ecart"]
        out["ecart"] = {k: -v for k, v in e.items()} if isinstance(e, dict) else -e
    return out


P, G, D = AN.FSI["petit"], AN.FSI["grand"], AN.FSI_DEUX       # fuite de signe inverse, par modèle (CLV-01)
POS = dict(lp=(0.7, 1.1), lg=(0.0, 0.2), dl=(0.5, 1.0))
INV = dict(lp=(0.0, 0.2), lg=(0.7, 0.9), dl=(-0.9, -0.5), sp=(-0.6, -0.1))
FSI = dict(lp=(-1.1, -0.9), lg=(-1.0, -0.85), dl=(-0.2, 0.2))              # les deux modèles sous −δ, et « nul »
FSI_SEULE = dict(lp=(-1.1, -0.9), lg=(-0.6, -0.4), dl=(-0.6, -0.3))       # les deux modèles sous −δ, seuls
FSI_P = dict(lp=(-1.0, -0.6), lg=(-0.1, 0.1), dl=(-1.0, -0.5))             # le petit seul sous −δ
FSI_G = dict(lp=(-0.1, 0.1), lg=(-1.0, -0.6), dl=(0.5, 1.0))               # le grand seul sous −δ
FSI_P_NUL = dict(lp=(-0.6, -0.3), lg=(-0.5, -0.2), dl=(-0.2, 0.2))         # le petit sous −δ, et « nul »
FSI_G_NUL = dict(lp=(-0.5, -0.2), lg=(-0.6, -0.3), dl=(-0.2, 0.2))         # le grand sous −δ, et « nul »
PDF_NUL = dict(lp=(0.05, 0.22), lg=(0.0, 0.2), dl=(-0.10, 0.15))           # « pas de fuite » et « nul »
PDF = dict(lp=(-0.1, 0.2), lg=(-0.2, 0.2), dl=(-0.2, 0.3))
NUL = dict(lp=(0.3, 0.6), lg=(0.35, 0.6), dl=(-0.2, 0.2))
IND = dict(lp=(0.3, 0.9), lg=(0.1, 0.6), dl=(-0.1, 0.6))
# cas fabriqués de cl6 (CLU-01) : sous H_0, l'écart d'échelle porté par un modèle différent dans chaque sens
ART_POS = dict(lp=(0.85, 1.15), lg=(0.40, 0.60), dl=(0.35, 0.65),
               lp_ba=(0.40, 0.60), lg_ba=(-0.10, 0.10), dl_ba=(0.35, 0.65))
ART_INV = dict(lp=(0.40, 0.60), lg=(0.85, 1.15), dl=(-0.65, -0.35), sp=(-0.6, -0.1),
               lp_ba=(-0.10, 0.10), lg_ba=(0.40, 0.60), dl_ba=(-0.65, -0.35))
ART_NUL = dict(lp=(0.05, 0.35), lg=(0.05, 0.35), dl=(-0.2, 0.2), lp_ba=(0.85, 1.15), lg_ba=(0.85, 1.15))


def sens_ba(cas):
    return {k + "_ba": v for k, v in cas.items()}


CAS_LIRE = [
    # les deux sens d'accord
    (POS, "positif", 0),
    ({**POS, "sp": (-0.1, 0.6)}, "positif", 1),
    ({**POS, "sp_ba": (-0.1, 0.6)}, "positif", 1),                          # spécificité dans le sens b→a
    ({**POS, "prof": True}, "positif", 1),                                   # profondeur (CLY-08)
    ({**POS, "prof_ba": True}, "positif", 1),                                # profondeur dans le sens b→a (CLZ-01)
    (INV, "inverse", 0),
    ({**INV, "sp": (-0.6, 0.1)}, "inverse", 1),
    ({**INV, "sp_ba": (-0.6, 0.1)}, "inverse", 1),
    ({**INV, "prof": True}, "inverse", 1),
    (FSI, D, 0),                                                             # les deux modèles, dans les deux sens
    (dict(lp=(-0.1, 0.1), lg=(-0.65, -0.5), dl=(0.47, 0.64)), G, 0),
    (dict(lp=(-0.7, -0.5), lg=(-0.1, 0.1), dl=(-0.69, -0.52)), P, 0),
    (PDF, "pas de fuite", 0),
    (NUL, "nul", 0),
    (IND, "indécis", 0),
    # conditions de « positif » refusées une à une (dans les deux sens : le cas fabriqué les porte aux deux)
    ({**POS, "lp": (0.2, 1.1), "lp_ba": (0.2, 1.1)}, "indécis", 0),          # λ(petit) borne basse ≤ δ (CLY-14)
    ({**POS, "lg": (-0.3, 0.2), "lg_ba": (-0.3, 0.2)}, "indécis", 0),        # λ(grand) borne basse ≤ −δ
    (dict(lp=(1.6, 2.1), lg=(1.0, 1.3), dl=(0.4, 0.9)), "indécis", 0),      # λ(grand) ≥ 1
    ({**POS, "dl": (0.2, 1.0), "dl_ba": (0.2, 1.0)}, "indécis", 0),          # Δλ borne basse ≤ δ
    # conditions de « inverse » refusées une à une, en miroir (CLZ-11)
    ({**INV, "lg": (0.2, 0.9), "lg_ba": (0.2, 0.9)}, "indécis", 0),          # λ(grand) borne basse ≤ δ
    ({**INV, "lp": (-0.3, 0.2), "lp_ba": (-0.3, 0.2)}, "indécis", 0),        # λ(petit) borne basse ≤ −δ
    (dict(lp=(1.0, 1.3), lg=(1.6, 2.1), dl=(-0.9, -0.4)), "indécis", 0),    # λ(petit) ≥ 1
    ({**INV, "dl": (-0.9, -0.2), "dl_ba": (-0.9, -0.2)}, "indécis", 0),      # Δλ borne haute ≥ −δ
    # certification
    ({**POS, "cert": (0.6, 0.65)}, "non certifiable", 0),
    ({**POS, "cert": (0.6, 0.8)}, "certification asymétrique (grand seulement)", 0),
    ({**POS, "cert": (0.8, 0.6)}, "certification asymétrique (petit seulement)", 0),
    ({**POS, "cert": (0.6, 0.8), "cert_ba": (0.6, 0.6)}, "non certifiable", 0),     # deux échecs différents
    ({**IND, "cert": (0.6, 0.6), "cert_ba": (0.8, 0.8)}, "indécis", 0),              # un sens non certifié, l'autre indécis
    # un seul sens lit une issue (CLZ-01, CLZ-02) : non confirmée
    ({**POS, **sens_ba(IND)}, "positif non confirmé (sens b→a)", 0),                 # signature du jeu a (CLY-01)
    ({**POS, "cert_ba": (0.6, 0.8)}, "positif non confirmé (sens b→a)", 0),          # b→a non certifié
    ({**INV, **sens_ba(IND)}, "inverse non confirmé (sens b→a)", 0),
    ({**FSI_SEULE, **sens_ba(IND)}, f"{D} non confirmé (sens b→a)", 0),
    ({**FSI_P, **sens_ba(IND)}, f"{P} non confirmé (sens b→a)", 0),
    ({**FSI_G, **sens_ba(IND)}, f"{G} non confirmé (sens b→a)", 0),
    ({**FSI_P_NUL, **sens_ba(IND)}, f"{P} non confirmé (sens b→a)", 0),              # première étape tenue
    ({**PDF, **sens_ba(IND)}, "pas de fuite non confirmé (sens b→a)", 0),
    ({**NUL, **sens_ba(IND)}, "nul non confirmé (sens b→a)", 0),
    ({**IND, **sens_ba(POS)}, "positif non confirmé (sens a→b)", 0),                 # signature du jeu b
    ({**NUL, "cert": (0.6, 0.6), "cert_ba": (0.8, 0.8)}, "nul non confirmé (sens a→b)", 0),     # a→b non certifié
    # deux issues différentes (CLZ-01 : signature négative du jeu a, masquage d'un effet vrai)
    ({**FSI_SEULE, **sens_ba(PDF)}, "désaccord des deux sens", 0),
    ({**NUL, **sens_ba(POS)}, "désaccord des deux sens", 0),
    ({**PDF, **sens_ba(POS)}, "désaccord des deux sens", 0),
    ({**POS, **sens_ba(INV)}, "désaccord des deux sens", 0),
    # fuite de signe inverse tenue par un modèle différent dans chaque sens (CLV-01) : aucune issue commune
    ({**FSI_P, **sens_ba(FSI_G)}, "désaccord des deux sens", 0),            # cas fabriqué de cl5
    ({**FSI_G, **sens_ba(FSI_P)}, "désaccord des deux sens", 0),
    ({**FSI_P_NUL, **sens_ba(FSI_G_NUL)}, "nul", 2),                         # « nul » commun ; deux réserves
    # le même modèle dans les deux sens, l'autre dans un seul (CLV-01) : réserve, même étape
    ({**FSI, **sens_ba(FSI_P)}, P, 1),
    ({**FSI, **sens_ba(FSI_G)}, G, 1),
    ({**FSI_P_NUL, **sens_ba(FSI_P)}, P, 0),                                 # « nul » dans un seul sens, placé après
    # issues compatibles (CLW-01) : « nul » tenu dans les deux sens est prononcé ; l'issue tenue dans un seul sens et
    # placée avant lui devient une réserve
    ({**PDF_NUL, **sens_ba(NUL), "ecart": -0.2}, "nul", 1),                  # cas fabriqué de cl4 ; λ de chaque
    ({**PDF_NUL, **sens_ba(NUL)}, "désaccord des deux sens", 0),             # modèle à δ près d'un sens à l'autre,
    # sinon (λ(petit) 0,135 et 0,45, λ(grand) 0,10 et 0,475 au milieu des intervalles), cohérence rompue : la v6
    # lisait « nul » (CLU-01)
    # (la v6 lisait « nul » avec deux et trois réserves ; λ de chaque modèle à plus de δ d'un sens à l'autre, CLU-01)
    ({**FSI, **sens_ba(NUL)}, "désaccord des deux sens", 0),                  # deux fuites de signe inverse, un sens
    ({**FSI, **sens_ba(PDF_NUL)}, "désaccord des deux sens", 0),
    ({**PDF_NUL, **sens_ba(PDF_NUL)}, "pas de fuite", 0),                     # première issue commune
    ({**FSI, **sens_ba(FSI_SEULE)}, D, 0),                                    # « nul » dans un seul sens, placé après
    # réserves de chaque issue (CLW-02), restreintes aux modèles prononcés (CLV-01)
    ({**FSI, "ssi": (-0.1, 0.4)}, D, 2),                                      # non spécifique, pour chaque modèle
    ({**FSI, "ssi": {"petit": (-0.1, 0.4), "grand": (0.1, 0.5)}}, D, 1),
    ({**FSI, "ssi_ba": (-0.1, 0.4)}, D, 2),
    ({**FSI, "prof": True}, D, 2),
    ({**FSI, "ssi": (-0.1, 0.4), "prof_ba": True}, D, 4),
    ({**FSI_P, "ssi": {"petit": (0.1, 0.5), "grand": (-0.5, 0.2)}}, P, 0),   # modèle non prononcé : aucune réserve
    ({**FSI_P, "prof": {G}}, P, 0),
    ({**FSI_P, "prof": {P}}, P, 1),
    ({**FSI_G, "ssi_ba": {"petit": (0.1, 0.5), "grand": (-0.5, 0.2)}}, G, 1),
    ({**PDF, "prof": True}, "pas de fuite", 1),
    ({**NUL, "prof_ba": True}, "nul", 1),
    ({**NUL, "ssi": (-0.5, -0.1)}, "nul", 0),                                 # la spécificité de signe inverse ne vise
    ({**POS, "ssi": (-0.5, -0.1)}, "positif", 0),                             # que la fuite de signe inverse
    # cohérence des deux sens (CLU-01) : artefacts de cl6, la v6 lisait « positif », « inverse », « nul » sans réserve
    (ART_POS, "désaccord des deux sens", 0),
    (ART_INV, "désaccord des deux sens", 0),
    (ART_NUL, "désaccord des deux sens", 0),
    # bornes de la cohérence : |écart ponctuel| ≤ δ (borne comprise), pour chacun des deux modèles
    ({**POS, "ecart": 0.25}, "positif", 0),
    ({**POS, "ecart": 0.26}, "désaccord des deux sens", 0),
    ({**POS, "ecart": -0.25}, "positif", 0),
    ({**POS, "ecart": -0.26}, "désaccord des deux sens", 0),
    ({**POS, "ecart": {"petit": 0.0, "grand": 0.3}}, "désaccord des deux sens", 0),
    ({**POS, "ecart": {"petit": -0.3, "grand": 0.0}}, "désaccord des deux sens", 0),
    ({**INV, "ecart": 0.26}, "désaccord des deux sens", 0),
    ({**INV, "ecart": -0.2}, "inverse", 0),
    ({**NUL, "ecart": {"petit": 0.0, "grand": -0.4}}, "désaccord des deux sens", 0),
    ({**NUL, "ecart": 0.2}, "nul", 0),
    # la cohérence ne vise que les issues qui comparent les deux modèles : fuite de signe inverse (même modèle dans les
    # deux sens, CLV-01) et « pas de fuite » (quatre λ dans [−δ ; δ]) ne la demandent pas ; « nul » sans la cohérence
    # cède à « pas de fuite », placé avant lui
    ({**FSI, "ecart": 0.5}, D, 0),
    ({**PDF, "ecart": 0.35}, "pas de fuite", 0),
    ({**PDF_NUL, "ecart": 0.35}, "pas de fuite", 0),
    # la cohérence ne joue pas sur une issue tenue dans un seul sens
    ({**POS, **sens_ba(IND), "ecart": 0.5}, "positif non confirmé (sens b→a)", 0),
]


@pytest.mark.parametrize("kw, attendu, n_reserves", CAS_LIRE)
def test_lire(kw, attendu, n_reserves):
    lecture, reserves, detail = AN.lire(r_fictif(**kw))
    assert lecture == attendu and len(reserves) == n_reserves
    assert set(detail["lecture_par_sens"]) == {"a→b", "b→a"}


@pytest.mark.parametrize("kw, attendu, n_reserves", CAS_LIRE)
def test_lire_miroir(kw, attendu, n_reserves):
    """Les deux sens jouent le même rôle : échanger a→b et b→a échange seulement le sens nommé (R4, CLZ-01)."""
    lecture, reserves, _ = AN.lire(r_fictif(**miroir(kw)))
    echange = {"(sens a→b)": "(sens b→a)", "(sens b→a)": "(sens a→b)"}
    for a, b in echange.items():
        if attendu.endswith(a):
            attendu = attendu[: -len(a)] + b
            break
    assert lecture == attendu and len(reserves) == n_reserves


def test_conditions_manquantes_chiffrees():
    """CLZ-02 : la lecture rapporte ce qui manque dans l'autre sens, chiffré, certification comprise."""
    _, _, detail = AN.lire(r_fictif(**POS, dl_ba=(0.195, 1.25), cert_ba=(0.8, 0.517)))
    (cle, manque), = detail["conditions_manquantes"].items()
    assert cle == "positif (a→b), dans le sens b→a"
    assert any("certification b→a du grand" in m and "0.517" in m for m in manque)
    assert any("Δλ_b→a 0.195" in m for m in manque)


def test_conditions_manquantes_de_chaque_issue_d_un_seul_sens():
    """CLV-07 : chaque issue tenue dans un seul sens reçoit ce qui lui manque dans l'autre, pas seulement la première ;
    « non confirmé » et « désaccord » ne portent aucune réserve."""
    lecture, reserves, detail = AN.lire(r_fictif(**PDF_NUL, **sens_ba(IND)))
    assert lecture == "pas de fuite non confirmé (sens b→a)" and reserves == []
    assert set(detail["conditions_manquantes"]) == {"pas de fuite (a→b), dans le sens b→a",
                                                    "nul (a→b), dans le sens b→a"}
    lecture, reserves, detail = AN.lire(r_fictif(**FSI_P_NUL, **sens_ba(PDF)))
    assert lecture == "désaccord des deux sens" and reserves == []
    assert set(detail["conditions_manquantes"]) == {f"{P} (a→b), dans le sens b→a", "nul (a→b), dans le sens b→a",
                                                    "pas de fuite (b→a), dans le sens a→b"}


def test_fuite_de_signe_inverse_croisee_rapportee_modele_par_modele():
    """CLV-01 : dans le cas croisé, ce qui manque est rapporté pour le modèle de chaque sens, chiffré."""
    lecture, _, detail = AN.lire(r_fictif(**FSI_P, **sens_ba(FSI_G)))
    assert lecture == "désaccord des deux sens"
    assert detail["issues_tenues_par_sens"] == {"a→b": [P], "b→a": [G]}
    assert detail["conditions_manquantes"] == {f"{P} (a→b), dans le sens b→a": ["borne haute de λ_b→a(petit) 0.100 < −δ"],
                                               f"{G} (b→a), dans le sens a→b": ["borne haute de λ_a→b(grand) 0.100 < −δ"]}


NS = AN.NON_SPECIFIQUE
CAS_RESERVES = [      # texte des réserves : modèle nommé, sens nommé (CLU-05)
    ({**FSI, "ssi": {"petit": (-0.1, 0.4), "grand": (0.1, 0.5)}}, D, [f"{NS} (petit)"]),
    ({**FSI, "ssi": {"petit": (0.1, 0.5), "grand": (-0.1, 0.4)}}, D, [f"{NS} (grand)"]),
    ({**FSI_G, "ssi_ba": {"petit": (0.1, 0.5), "grand": (-0.5, 0.2)}}, G, [f"{NS} (grand)"]),
    ({**FSI_P, "ssi": {"petit": (-0.5, 0.2), "grand": (0.1, 0.5)}}, P, [f"{NS} (petit)"]),
    ({**FSI_P, "prof": {P}}, P, [AN.PROFONDEUR[P]]),
    ({**FSI, "ssi": (-0.1, 0.4), "prof_ba": True}, D,
     [f"{NS} (petit)", f"{NS} (grand)", AN.PROFONDEUR[P], AN.PROFONDEUR[G]]),
    ({**FSI, **sens_ba(FSI_P)}, P, [f"{G} lu dans le seul sens a→b (non confirmé)"]),
    ({**FSI, **sens_ba(FSI_G)}, G, [f"{P} lu dans le seul sens a→b (non confirmé)"]),
    ({**PDF_NUL, **sens_ba(NUL), "ecart": -0.2}, "nul", ["pas de fuite lu dans le seul sens a→b (non confirmé)"]),
    ({**FSI_P_NUL, **sens_ba(FSI_G_NUL)}, "nul", [f"{P} lu dans le seul sens a→b (non confirmé)",
                                                    f"{G} lu dans le seul sens b→a (non confirmé)"]),
    ({**POS, "sp_ba": (-0.1, 0.6), "prof": True}, "positif", [NS, AN.PROFONDEUR["positif"]]),
    ({**INV, "sp": (-0.6, 0.1)}, "inverse", [NS]),
]


@pytest.mark.parametrize("kw, attendu, textes", CAS_RESERVES)
def test_texte_des_reserves(kw, attendu, textes):
    """CLU-05 : le texte de chaque réserve, pas seulement leur nombre ; en miroir, le sens nommé s'échange."""
    lecture, reserves, _ = AN.lire(r_fictif(**kw))
    assert lecture == attendu and reserves == textes
    lecture, reserves, _ = AN.lire(r_fictif(**miroir(kw)))
    miroirs = [x.replace("sens a→b", "sens #").replace("sens b→a", "sens a→b").replace("sens #", "sens b→a")
               for x in textes]
    assert lecture == attendu and sorted(reserves) == sorted(miroirs)


@pytest.mark.parametrize("cas, issue", [(ART_POS, "positif"), (ART_INV, "inverse"), (ART_NUL, "nul")])
def test_coherence_rompue_rapportee_chiffree(cas, issue):
    """CLU-01 : l'issue tenue dans les deux sens sans la cohérence est rapportée avec l'écart chiffré de chaque modèle
    qui la rompt ; la cohérence des deux modèles figure toujours au détail."""
    lecture, reserves, detail = AN.lire(r_fictif(**cas))
    assert lecture == "désaccord des deux sens" and reserves == []
    assert detail["issues_tenues_par_sens"] == {"a→b": [issue], "b→a": [issue]}
    (cle, manque), = detail["conditions_manquantes"].items()
    assert cle == f"{issue} (a→b et b→a), cohérence des deux sens"
    assert len(manque) == 2 and manque[0].startswith("cohérence des deux sens du petit")
    assert manque[1].startswith("cohérence des deux sens du grand")
    assert [c["tenue"] for c in detail["coherence_des_sens"]] == [False, False]


def test_coherence_saine_rapportee():
    lecture, _, detail = AN.lire(r_fictif(**POS, ecart={"petit": 0.02, "grand": -0.05}))
    assert lecture == "positif" and detail["conditions_manquantes"] == {}
    assert detail["coherence_des_sens"] == [
        {"condition": "cohérence des deux sens du petit : |λ_a→b − λ_b→a| = |0.020| ≤ δ (intervalle [-0.080 ; 0.120])",
         "tenue": True},
        {"condition": "cohérence des deux sens du grand : |λ_a→b − λ_b→a| = |-0.050| ≤ δ (intervalle [-0.150 ; 0.050])",
         "tenue": True}]


def test_aire_ponderee_egale_aire_dupliquee():
    rng = np.random.default_rng(0)
    pos, neg = rng.normal(size=7).round(1), rng.normal(size=9).round(1)
    wp, wn = rng.integers(0, 3, size=7).astype(float), rng.integers(1, 3, size=9).astype(float)
    dup_p, dup_n = np.repeat(pos, wp.astype(int)), np.repeat(neg, wn.astype(int))
    attendu = np.mean([(a > b) + 0.5 * (a == b) for a in dup_p for b in dup_n])
    assert AN.auroc_pondere(pos, wp, neg, wn) == pytest.approx(attendu)


def test_intervalle_non_fini():
    with pytest.raises(AN.Arret):
        AN.intervalle([0.1, float("nan")])


def test_partitions():
    assert len(AN.PARTITIONS) == 10 and all(sum(p) == 0 and p[0] == 1 for p in AN.PARTITIONS)


def test_tirage_paires_conditionne():
    class Rng:
        def __init__(self):
            self.n, self.vrai = 0, np.random.default_rng(0)

        def choice(self, *a, **k):
            return self.vrai.choice(*a, **k)

        def integers(self, lo, hi, size):
            self.n += 1
            return np.zeros(size, dtype=int) if self.n in (1, 3) else self.vrai.integers(lo, hi, size=size)

    compteur = {"a": 0, "b": 0}
    moities = (np.arange(0, 24), np.arange(24, 48))
    _, wp = AN.tirer(Rng(), moities, compteur)
    assert (wp["a"] > 0).sum() >= 2 and (wp["b"] > 0).sum() >= 2 and compteur == {"a": 1, "b": 1}
    rng, c = np.random.default_rng(1), {"a": 0, "b": 0}
    assert all(min((v > 0).sum() for v in AN.tirer(rng, moities, c)[1].values()) >= 2 for _ in range(20000))


# ---------- intégration ----------

def test_positif_confirme(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 1),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 2, nom="grand"))
    assert code == 0 and r["lecture"] == "positif" and r["reserves"] == []
    assert r["petit"]["ab"]["lambda"] == pytest.approx(1.0, abs=0.25)
    assert r["petit"]["ba"]["lambda"] == pytest.approx(1.0, abs=0.25)
    assert r["petit"]["couche"] == 6 and r["grand"]["couche"] == 6


def test_signature_du_jeu_a_non_confirmee(tmp_path, stimuli):
    """CLY-01 : au petit, le format ne pousse que la signature propre aux cadrages a ; aucun concept ne fuit."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.0, 41, tau=0.4, signature=2.0),
                       fabriquer(tmp_path / "g", stimuli, 0.0, 42, nom="grand", tau=0.4))
    assert code == 0 and r["lecture"] == "positif non confirmé (sens b→a)"
    # le sens a→b seul aurait lu « positif » (la lecture de la v2) : c'est le danger que le sens b→a écarte
    assert r["lecture_par_sens"] == {"a→b": "positif", "b→a": "indécis"}
    assert r["delta_lambda_ic"]["ab"][0] > 0.25 and r["petit"]["ab"]["lambda_ic"][0] > 0.25
    assert r["petit"]["ba"]["lambda"] < r["petit"]["ab"]["lambda"] - 0.3
    (manque,) = r["conditions_manquantes"].values()
    assert any(m.startswith("borne basse de Δλ_b→a") for m in manque)


def test_signature_negative_du_jeu_a(tmp_path, stimuli):
    """CLZ-01 : la même signature, de signe négatif, ne fabrique plus une « fuite de signe inverse »."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.0, 41, tau=0.4, signature=-2.0),
                       fabriquer(tmp_path / "g", stimuli, 0.0, 42, nom="grand", tau=0.4))
    assert code == 0 and r["lecture"] == f"{P} non confirmé (sens b→a)"
    # le sens a→b seul (la lecture de la v3) aurait lu « fuite de signe inverse »
    assert r["lecture_par_sens"]["a→b"] == P and r["petit"]["ab"]["lambda_ic"][1] < -0.25


@pytest.mark.parametrize("options_petit, options_grand, tenues", [
    ({"signature": -2.0}, {"signature_b": -2.0}, {"a→b": [P], "b→a": [G]}),
    ({"signature_b": -2.0}, {"signature": -2.0}, {"a→b": [G], "b→a": [P]})])
def test_signatures_croisees_negatives(tmp_path, stimuli, options_petit, options_grand, tenues):
    """CLV-01 : signature négative d'un seul jeu à chaque taille, de jeux différents, aucun concept. Chaque sens tient la
    fuite de signe inverse d'un modèle différent (la v5 la prononçait, sans réserve) ; aucun modèle ne la tient dans
    les deux sens : rien n'est prononcé."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.0, 41, tau=0.4, **options_petit),
                       fabriquer(tmp_path / "g", stimuli, 0.0, 42, nom="grand", tau=0.4, **options_grand))
    assert code == 0 and r["lecture"] == "désaccord des deux sens" and r["reserves"] == []
    assert r["issues_tenues_par_sens"] == tenues


@pytest.fixture
def d256(monkeypatch):
    """Activations synthétiques en dimension 256 (le recouvrement fortuit d'une signature avec le contexte y est plus
    petit qu'en dimension 64 ; CLU-01)."""
    monkeypatch.setattr(AN, "ATTENDUS", {k: {**v, "dimension": 256} for k, v in PETITS.items()})


@pytest.mark.parametrize("o_petit, o_grand, graine, issue", [
    ({"signature": 1.3}, {"signature_b": -1.3}, 900, "positif"),      # jeu a poussé vers le haut au 8B, b vers le bas au 70B
    ({"signature": -1.3}, {"signature_b": 1.3}, 904, "inverse")])     # miroir
def test_signatures_croisees_opposees_sous_fuite_egale(tmp_path, stimuli, d256, o_petit, o_grand, graine, issue):
    """CLU-01, artefact de cl6 : fuite égale aux deux tailles (λ 0,5 et 0,5, vérité H_0), signature d'un seul jeu à
    chaque taille, de jeux différents et de signes opposés, dimension 256. Chaque sens tient « positif » (ou « inverse »)
    par un modèle différent ; la v6 le prononçait sans réserve. L'écart de chaque modèle entre les sens dépasse δ : la
    lecture est « désaccord des deux sens », l'écart rapporté."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.5, graine, d=256, **o_petit),
                       fabriquer(tmp_path / "g", stimuli, 0.5, graine + 1, nom="grand", d=256, **o_grand))
    assert code == 0 and r["issues_tenues_par_sens"] == {"a→b": [issue], "b→a": [issue]}
    assert r["lecture"] == "désaccord des deux sens" and r["reserves"] == []
    assert all(abs(r["ecart_sens"][k]) > 0.25 for k in ("petit", "grand"))
    assert list(r["conditions_manquantes"]) == [f"{issue} (a→b et b→a), cohérence des deux sens"]


def test_coherence_saine_sous_HA(tmp_path, stimuli, d256):
    """CLU-01, cas sain : H_A (λ 1,0 et 0,2), dimension 256 ; chaque modèle garde son λ d'un sens à l'autre."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 900, d=256),
                       fabriquer(tmp_path / "g", stimuli, 0.2, 901, nom="grand", d=256))
    assert code == 0 and r["lecture"] == "positif" and r["reserves"] == []
    assert all(abs(r["ecart_sens"][k]) < 0.1 for k in ("petit", "grand"))
    assert [c["tenue"] for c in r["coherence_des_sens"]] == [True, True]


def test_coherence_rompue_par_un_contexte_plus_faible(tmp_path, stimuli, d256):
    """CLU-01, prix assumé (CLZ-02) : sous H_A, un contexte du jeu b plus faible (× 0,6) gonfle λ_a→b des deux modèles
    (λ est relatif au contexte du jeu mesuré) ; l'écart du 8B entre les sens dépasse δ, « positif » tenu dans les deux
    sens n'est pas prononcé."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 900, d=256, contexte_b=0.6),
                       fabriquer(tmp_path / "g", stimuli, 0.2, 901, nom="grand", d=256, contexte_b=0.6))
    assert code == 0 and r["issues_tenues_par_sens"] == {"a→b": ["positif"], "b→a": ["positif"]}
    assert r["lecture"] == "désaccord des deux sens" and r["ecart_sens"]["petit"] > 0.25


def test_signature_du_jeu_b(tmp_path, stimuli):
    """Miroir de CLY-01 : une signature propre aux cadrages b gonfle le seul sens b→a ; rien n'est prononcé."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.0, 41, tau=0.4, signature_b=2.0),
                       fabriquer(tmp_path / "g", stimuli, 0.0, 42, nom="grand", tau=0.4))
    assert code == 0 and r["lecture"] == "positif non confirmé (sens a→b)"
    assert r["lecture_par_sens"] == {"a→b": "indécis", "b→a": "positif"}


def test_masquage_d_un_effet_vrai(tmp_path, stimuli):
    """CLZ-01 : un écart d'échelle vrai (λ 1,0 et 0,2), masqué dans le sens a→b par une signature négative du jeu a,
    n'est plus lu « nul » : le sens b→a montre l'écart, la lecture est « désaccord des deux sens »."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 71, signature=-3.0),
                       fabriquer(tmp_path / "g", stimuli, 0.2, 72, nom="grand"))
    assert code == 0 and r["lecture"] == "désaccord des deux sens"
    assert r["lecture_par_sens"] == {"a→b": "nul", "b→a": "positif"}      # la v3 aurait lu « nul »


def test_signature_negative_au_grand(tmp_path, stimuli):
    """CLW-09 (miroir demandé par CLZ-01) : signature négative du jeu a au grand, aucun concept : rien n'est prononcé."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.0, 41, tau=0.4),
                       fabriquer(tmp_path / "g", stimuli, 0.0, 42, nom="grand", tau=0.4, signature=-2.0))
    assert code == 0 and r["lecture"] == f"{G} non confirmé (sens b→a)"
    assert r["issues_tenues_par_sens"] == {"a→b": [G], "b→a": []}


def test_nul_tenu_dans_les_deux_sens(tmp_path, stimuli):
    """CLW-01 : fuite faible et égale aux deux tailles, contexte du jeu b plus faible ; un sens tient « pas de fuite »
    et « nul », l'autre « nul » seul : la lecture est « nul », avec la réserve « pas de fuite » d'un seul sens (la v4
    aurait lu « désaccord des deux sens »)."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.15, 41, contexte_b=0.6),
                       fabriquer(tmp_path / "g", stimuli, 0.15, 42, nom="grand", contexte_b=0.6))
    assert code == 0 and r["lecture"] == "nul"
    assert r["issues_tenues_par_sens"] == {"a→b": ["nul"], "b→a": ["pas de fuite", "nul"]}
    assert r["reserves"] == ["pas de fuite lu dans le seul sens b→a (non confirmé)"]
    assert r["lecture_par_sens"] == {"a→b": "nul", "b→a": "pas de fuite"}     # ce que la v4 aurait comparé


@pytest.mark.parametrize("contraire", [False, True])
def test_profondeur_quatre_couches(tmp_path, stimuli, monkeypatch, contraire):
    """CLZ-11 : réserve « profondeur » calculée sur quatre couches (L* = la dernière, contexte le plus fort) : aux trois
    autres, λ(petit) < λ(grand) si `contraire`, sinon le même signe qu'en L*."""
    couches = (2, 3, 4, 6)
    monkeypatch.setattr(AN, "ATTENDUS", {k: {**v, "couches": list(couches)} for k, v in PETITS.items()})
    ap = {2: 0.0, 3: 0.0, 4: 0.0} if contraire else {2: 1.0, 3: 1.0, 4: 1.0}
    ag = {2: 0.8, 3: 0.8, 4: 0.8} if contraire else {2: 0.1, 3: 0.1, 4: 0.1}
    code, r = analyser(tmp_path, stimuli,
                       fabriquer(tmp_path / "p", stimuli, 1.0, 81, couches=couches, alpha_couches=ap),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 82, nom="grand", couches=couches, alpha_couches=ag))
    assert code == 0 and r["petit"]["couche"] == 6 and r["grand"]["couche"] == 6
    assert all(len(r["delta_lambda_par_profondeur"][s]) == 4 for s in ("ab", "ba"))
    assert r["profondeur_contraire"]["positif"] == {"ab": contraire, "ba": contraire}
    assert r["lecture"] == "positif"
    assert any(x.startswith("profondeur") for x in r["reserves"]) is contraire


@pytest.mark.parametrize("ap, ag, ap3, ag3, graine, issue, contraire", [
    (0.5, 0.5, 0.5, 0.5, 500, "nul", False),
    (0.5, 0.5, 1.0, 0.2, 502, "nul", True),                  # Δλ de 0,8 aux trois autres profondeurs
    (0.0, 0.0, 0.0, 0.0, 504, "pas de fuite", False),
    (0.0, 0.0, 0.6, 0.0, 506, "pas de fuite", True),         # λ(petit) de 0,6 aux trois autres
    (-0.8, 0.0, -0.8, 0.0, 508, P, False),
    (-0.8, 0.0, 0.5, 0.0, 510, P, True),                     # λ(petit) de +0,5 aux trois autres
    (0.0, -0.8, 0.0, -0.8, 512, G, False),
    (0.0, -0.8, 0.0, 0.5, 514, G, True)])                    # λ(grand) de +0,5 aux trois autres
def test_profondeur_quatre_couches_chaque_issue(tmp_path, stimuli, monkeypatch, ap, ag, ap3, ag3, graine, issue,
                                                contraire):
    """CLV-08 : la réserve « profondeur » de « nul », de « pas de fuite » et de chaque fuite de signe inverse, calculée
    par `principal` sur quatre couches (L* = la dernière) : cas sain (même λ aux trois autres profondeurs) et artefact
    (trois profondeurs sur quatre qui contredisent l'issue lue en L*). Les six premiers cas reprennent l'essai de cl5,
    aux mêmes graines."""
    couches = (2, 3, 4, 6)
    monkeypatch.setattr(AN, "ATTENDUS", {k: {**v, "couches": list(couches)} for k, v in PETITS.items()})
    code, r = analyser(tmp_path, stimuli,
                       fabriquer(tmp_path / "p", stimuli, ap, graine, couches=couches,
                                 alpha_couches={2: ap3, 3: ap3, 4: ap3}),
                       fabriquer(tmp_path / "g", stimuli, ag, graine + 1, nom="grand", couches=couches,
                                 alpha_couches={2: ag3, 3: ag3, 4: ag3}))
    assert code == 0 and r["petit"]["couche"] == 6 and r["grand"]["couche"] == 6
    assert r["lecture"] == issue
    assert r["profondeur_contraire"][issue] == {"ab": contraire, "ba": contraire}
    assert (AN.PROFONDEUR[issue] in r["reserves"]) is contraire


def test_forces_inegales_sans_fausse_reserve(tmp_path, stimuli):
    """CLY-02 : fuite purement spécifique, forces de cadrage inégales : ν reste bas (direction orthogonalisée)."""
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 1.0, 43, kappa=0.4),
                       fabriquer(tmp_path / "g", stimuli, 0.1, 44, nom="grand", kappa=0.4))
    assert code == 0 and r["petit"]["ab"]["nu"] < 0.2 and r["petit"]["ba"]["nu"] < 0.2
    assert not any("non spécifique" in x for x in r["reserves"])


def test_nul_strict(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p", stimuli, 0.5, 3, tau=0.05),
                       fabriquer(tmp_path / "g", stimuli, 0.5, 4, nom="grand", tau=0.05))
    assert code == 0 and r["lecture"] == "nul"


def test_invariance_par_translation(tmp_path, stimuli):
    a = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p0", stimuli, 0.6, 5),
                 fabriquer(tmp_path / "g0", stimuli, 0.2, 6, nom="grand"), nom="s0")[1]
    b = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p1", stimuli, 0.6, 5, translation=60.0),
                 fabriquer(tmp_path / "g1", stimuli, 0.2, 6, nom="grand", translation=60.0), nom="s1")[1]
    for nom in ("petit", "grand"):
        for s in ("ab", "ba"):
            for k in ("A_ctx_fixe", "A_ctx", "A_conf", "lambda"):
                assert b[nom][s][k] == pytest.approx(a[nom][s][k], abs=0.02), (nom, s, k)
    assert a["lecture"] == b["lecture"]


def test_temoin_de_permutation_sensible(tmp_path, stimuli):
    r0 = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p0", stimuli, 1.0, 7),
                  fabriquer(tmp_path / "g0", stimuli, 0.1, 8, nom="grand"), nom="s0")[1]
    r1 = analyser(tmp_path, stimuli, fabriquer(tmp_path / "p1", stimuli, 1.0, 7, beta=3.0),
                  fabriquer(tmp_path / "g1", stimuli, 0.1, 8, nom="grand"), nom="s1")[1]
    assert r1["petit"]["ab"]["nu"] > r0["petit"]["ab"]["nu"] + 0.3
    assert r1["specificite"]["ab"] < r0["specificite"]["ab"]


# ---------- mode décisif (CLY-06) ----------

def paire_saine(tmp_path, stimuli, **kw):
    return fabriquer(tmp_path / "p", stimuli, 1.0, 21, **kw), fabriquer(tmp_path / "g", stimuli, 0.1, 22, nom="grand")


def test_decisif_sain(tmp_path, stimuli):
    code, r = analyser(tmp_path, stimuli, *paire_saine(tmp_path, stimuli))
    assert code == 0 and not r["repetition"] and r["commit_scripts"] == COMMIT_ESSAI and r["numpy"] == "2.4.6"


def test_decisif_sans_commit_attendu(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    assert AN.principal([str(stimuli), str(p), str(g), "1", str(tmp_path / "s")]) == 2


def test_decisif_commit_different(tmp_path, stimuli):
    assert analyser(tmp_path, stimuli, *paire_saine(tmp_path, stimuli), commit="d" * 40)[0] == 1


def test_decisif_arbre_non_propre(tmp_path, stimuli, monkeypatch):
    monkeypatch.setattr(AN, "etat_scripts", lambda: (COMMIT_ESSAI, False))
    assert analyser(tmp_path, stimuli, *paire_saine(tmp_path, stimuli))[0] == 1


def test_decisif_numpy_different(tmp_path, stimuli, monkeypatch):
    monkeypatch.setattr(AN, "NUMPY_ATTENDU", "0.0.0")
    assert analyser(tmp_path, stimuli, *paire_saine(tmp_path, stimuli))[0] == 1


# ---------- identité et intégrité (une sous-garde par test, CLY-14) ----------

def test_artefact_dossiers_inverses(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    assert analyser(tmp_path, stimuli, g, p)[0] == 1


@pytest.mark.parametrize("champ, valeur", [("revision", "autre"), ("couches", [4, 6, 8]), ("dimension", 32),
                                           ("type_nombre", "float32"), ("sha256_stimuli", "0" * 64), ("limite", 100),
                                           ("rendu_premier", "<autre gabarit>"), ("dernier_jeton", "<autre>"),
                                           ("script", "mesurer_echelle_v4.py"), ("sha256_script", "0" * 64)])
def test_artefact_champ_du_manifeste(tmp_path, stimuli, champ, valeur):
    p, g = paire_saine(tmp_path, stimuli, **{champ: valeur})
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_ordre(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    ids = json.loads((p / "ids.json").read_text())
    ids[0], ids[1] = ids[1], ids[0]
    (p / "ids.json").write_text(json.dumps(ids) + "\n")
    sceller(p / "ids.json")
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_compagnon_absent(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    (p / "activations-L6.npy.sha256").unlink()
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_empreinte(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    X = np.load(p / "activations-L6.npy")
    X[0, 0] += 1
    np.save(p / "activations-L6.npy", X)
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def resceller_activations(p, X, nom="activations-L6.npy"):
    np.save(p / nom, X)
    sceller(p / nom)
    m = json.loads((p / "manifeste-mesure.json").read_text())
    m["sha256_sorties"][nom] = sha(p / nom)
    (p / "manifeste-mesure.json").write_text(json.dumps(m))
    sceller(p / "manifeste-mesure.json")


def test_artefact_non_fini(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    X = np.load(p / "activations-L6.npy")
    X[3, 2] = np.nan
    resceller_activations(p, X)
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_artefact_forme(tmp_path, stimuli):
    p, g = paire_saine(tmp_path, stimuli)
    resceller_activations(p, np.load(p / "activations-L6.npy")[:-1])
    assert analyser(tmp_path, stimuli, p, g)[0] == 1


def test_sortie_presente(tmp_path, stimuli):
    (tmp_path / "sortie").mkdir()
    assert AN.principal([str(stimuli), "x", "y", "1", str(tmp_path / "sortie"), "--repetition"]) == 2


def test_repetition_marquee(tmp_path, stimuli):
    p = fabriquer(tmp_path / "p", stimuli, 1.0, 31, modele="autre", revision=None)
    g = fabriquer(tmp_path / "g", stimuli, 0.1, 32, nom="grand", modele="autre", revision=None)
    assert analyser(tmp_path, stimuli, p, g, nom="d")[0] == 1
    code, r = analyser(tmp_path, stimuli, p, g, nom="r", repetition=True)
    assert code == 0 and r["repetition"] and r["lecture"].startswith("répétition, non décisive")
