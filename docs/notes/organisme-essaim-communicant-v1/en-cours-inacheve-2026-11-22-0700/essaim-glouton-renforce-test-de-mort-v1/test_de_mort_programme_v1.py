#!/usr/bin/env python3
"""Test de mort par programme en monde planté (levier 2 de la recommandation, section C.1) — v1. Aucun appel de modèle,
aucun réseau, aucune dépense.

Deux rôles séparés, dans cet ordre :
1. **Fournisseur de tranche** (côté noyau, seul à toucher le monde) : `fournir_tranches` tire des épisodes (traits,
   sous-population, issue) **tenus à l'écart** (graines propres, distinctes des données servies, de l'oracle et du juge), les
   écrit dans un fichier JSON et rend son empreinte. C'est ce que fait déjà le noyau quand il sert une tranche à
   l'expérimentateur (`T.lignes_de_tranche(monde, racine, tache)`, patch v66) ; ici le monde est le monde planté.
2. **Juge programmé** (`test_de_mort_programme`) : ne reçoit que (loi de la carte, chemin du fichier de tranche, empreinte
   attendue, nom de la tranche). Il ne lit **ni la loi vraie, ni le devis du monde, ni l'archive, ni l'oracle**.

Règle chiffrée, écrite avant toute course (c'est la statistique gelée du test de mort actuel, `M.test_de_mort`, recopiée) :
  s = moyenne sur les n = 400 épisodes de la tranche de [log p_carte(y | z, g) − log m̂(y)], m̂ = marginale empirique de la
  tranche avec comptes + 0,5 ; plancher 1e-12 ; **« survit » si s ≥ 0,02, « éliminée » sinon** ; « refus » si la tranche
  n'a pas l'empreinte attendue, si la loi n'est pas évaluable (loi non finie ou erreur), ou si la garde relève une lecture
  interdite.

Garde de lecture (R5 : éprouvée sur le cas sain et sur des mutations) : pendant l'appel du juge,
- un crochet d'audit (`sys.addaudithook`) refuse toute ouverture de fichier autre que le fichier de tranche et tout import des
  modules du monde ;
- un profil (`sys.setprofile`) relève tout appel d'une fonction qui lit ou rejoue le monde (compilation du devis, oracle,
  tirage d'issues, ancien test de mort, fournisseur de tranche, générateur, vérificateur) ;
- tout argument en plus est refusé, et une « loi » qui a la forme d'un devis de monde (clés `effets`, `distracteurs`) aussi.
Une seule violation ⇒ le juge ne rend aucun verdict (`LectureLoiRefusee`).

Épreuves (sur les 12 mondes MR-2 de développement, régénérés comme la v1 des bases) :
- E1 équivalence : sur les mêmes épisodes (même générateur aléatoire), le juge programmé lu sur fichier rend exactement la
  statistique de `M.test_de_mort` (qui, elle, tire ses issues de la loi vraie) ;
- E2 objets de contrôle : la loi du monde (vraie par construction : doit survivre) ; trois fausses par construction (uniforme,
  marginale fixe de l'oracle, loi du monde aux pentes et décalages inversés : doivent être éliminées) ; la copie de la loi
  d'archive K1 (statistique contre la marginale, sans archive : **doit survivre** ; c'est le juge, contre le nul de l'archive,
  qui l'écarte ; la statistique « au-delà de l'archive » sur la même tranche, rapportée à part, vaut 0) ;
- E3 bruit : 20 tranches tenues à l'écart par monde, taux de survie de chaque carte, comparé au verdict « attendu » de
  l'oracle (gain contre la marginale ≥ 0,02) ; et accord avec `M.test_de_mort` sur des tranches distinctes ;
- E4 garde : cas sain (aucun refus) ; mutations A (le juge ouvre la partie scellée du monde), B (il recompile la loi vraie en
  mémoire), C (il reçoit le devis du monde en argument), D (il tire de nouvelles issues du monde) : chacune doit être refusée.

Graines : `SeedSequence(20261122, spawn_key=(tâche, monde, …))` ; tâche 3 tranches tenues à l'écart, 4 équivalence, 5 ancien
test sur tranches distinctes, 6 jeu planté. Usage : python -I -B test_de_mort_programme_v1.py SORTIE.json DOSSIER_TRANCHES [MONDES…]
"""
import datetime
import hashlib
import json
import os
import sys

import numpy as np

V1_DOSSIER = "/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1"
RACINE = 20261122
N_TRANCHE = 400
SEUIL = 0.02
REPETITIONS = 20


def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


def sha(chemin):
    return sha_octets(open(chemin, "rb").read())


def verifier(chemin):
    s, c = sha(chemin), open(chemin + ".sha256", encoding="utf-8").read().split()[0]
    if s != c:
        raise SystemExit(f"refus : {chemin} d'empreinte {s}, compagnon {c}")
    return s


SHA_V1 = verifier(os.path.join(V1_DOSSIER, "bases_sans_modele_v1.py"))
sys.path.insert(0, V1_DOSSIER)
import bases_sans_modele_v1 as B  # noqa: E402  (vérifie et importe les outils v1 à v4 ; régénère les mondes)

M, P1 = B.M, B.P1
probas = M.probas  # évaluateur de la grammaire : seule fonction des outils dont le juge a besoin


# =============================================================================================================================
# Garde de lecture
# =============================================================================================================================
class LectureLoiRefusee(Exception):
    pass


MODULES_INTERDITS = {"monde_riche_v4", "generateur_mondes_v2", "verifier_monde_v2", "verifier_monde_kimi_v1",
                     "puissance_monde_riche_v1", "puissance_monde_riche_v2", "puissance_monde_riche_v3",
                     "bases_sans_modele_v1", "base_gloutonne_renforcee_v1"}
FICHIERS_INTERDITS = {m + ".py" for m in MODULES_INTERDITS}
FONCTIONS_INTERDITES = {"compiler_monde", "compiler_v4", "_developper", "_conditions", "conditions_v4", "k1_du_monde",
                        "monde_restreint", "tirer_issues", "test_de_mort", "jeu_plante_mr1", "calibrer", "diluer",
                        "generer_monde_synthetique", "generer_monde_v4", "generer_v4", "verifier_v4", "regenerer",
                        "fournir_tranches", "donnees_servies"}


class _Garde:
    active = False
    permis = set()
    violations = []


def _crochet(evenement, args):
    if not _Garde.active:
        return
    if evenement == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
        p = os.path.realpath(os.fsdecode(args[0]))
        if p not in _Garde.permis:
            _Garde.violations.append(f"ouverture refusée : {p}")
            raise PermissionError(f"garde du test de mort : ouverture refusée ({p})")
    if evenement == "import" and args and str(args[0]).split(".")[-1] in MODULES_INTERDITS:
        _Garde.violations.append(f"import refusé : {args[0]}")
        raise ImportError(f"garde du test de mort : import refusé ({args[0]})")


sys.addaudithook(_crochet)


def _profil(cadre, evenement, arg):
    if evenement != "call":
        return
    co = cadre.f_code
    q = getattr(co, "co_qualname", co.co_name)
    if (os.path.basename(co.co_filename) in FICHIERS_INTERDITS or q in FONCTIONS_INTERDITES
            or q.startswith("Oracle.") or q.startswith("OracleCache.")):
        _Garde.violations.append(f"appel relevé : {q} ({os.path.basename(co.co_filename)})")


def juger_sous_garde(juge, loi, chemin, sha_attendu, nom, **en_plus):
    """Appelle `juge(loi, chemin, sha_attendu, nom)` sous la garde. Rend le verdict du juge, ou lève LectureLoiRefusee."""
    if en_plus:
        raise LectureLoiRefusee(f"argument(s) en plus refusé(s) : {sorted(en_plus)}")
    if isinstance(loi, dict) and ({"effets", "distracteurs"} & set(loi)):
        raise LectureLoiRefusee("une loi en forme de devis de monde (clés effets / distracteurs) est refusée")
    _Garde.permis = {os.path.realpath(chemin)}
    _Garde.violations = []
    _Garde.active = True
    sys.setprofile(_profil)
    try:
        try:
            res = juge(loi, chemin, sha_attendu, nom)
        except (PermissionError, ImportError) as ex:
            res = None
            _Garde.violations.append(f"{type(ex).__name__} : {ex}")
    finally:
        sys.setprofile(None)
        _Garde.active = False
    if _Garde.violations:
        raise LectureLoiRefusee("; ".join(_Garde.violations[:5]))
    return res


# =============================================================================================================================
# Juge programmé (ne lit que la tranche)
# =============================================================================================================================
def test_de_mort_programme(loi, chemin, sha_attendu, nom, seuil=SEUIL):
    octets = open(chemin, "rb").read()
    if sha_octets(octets) != sha_attendu:
        return {"verdict": "refus", "motif": "empreinte de la tranche"}
    t = json.loads(octets.decode("utf-8"))["tranches"][nom]
    Z, G, Y = np.asarray(t["Z"], float), np.asarray(t["G"], int), np.asarray(t["Y"], int)
    n = len(Y)
    try:
        P = probas(loi, Z, G)
        K = P.shape[1]
        if not np.all(np.isfinite(P)):
            return {"verdict": "refus", "motif": "loi non finie"}
    except Exception as ex:  # noqa: BLE001
        return {"verdict": "refus", "motif": f"loi non évaluable : {type(ex).__name__}"}
    c = np.bincount(Y, minlength=K) + 0.5
    marg = c / c.sum()
    s = float(np.mean(np.log(np.maximum(P[np.arange(n), Y], M.PLANCHER)) - np.log(marg[Y])))
    return {"verdict": "survit" if s >= seuil else "éliminée", "statistique": s, "n": n}


# =============================================================================================================================
# Fournisseur de tranches (côté noyau : lit le monde)
# =============================================================================================================================
def fournir_tranches(loi_monde, D, nsp, rngs, chemin):
    """rngs : {nom : générateur} ; même procédé que `M.test_de_mort` (instances puis issues du monde). Écrit le fichier."""
    tr = {}
    for nom, rng in rngs.items():
        Z, G = M.tirer_instances(rng, N_TRANCHE, D, nsp)
        Y = M.tirer_issues(rng, probas(loi_monde, Z, G))
        tr[nom] = {"Z": Z.tolist(), "G": G.tolist(), "Y": Y.tolist()}
    octets = json.dumps({"version": "tranches-test-de-mort-v1", "n": N_TRANCHE, "tranches": tr}, separators=(",", ":")).encode()
    with open(chemin, "xb") as f:
        f.write(octets)
    s = sha_octets(octets)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{s}  {os.path.basename(chemin)}\n")
    return s


def rng_tache(*cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=tuple(int(x) for x in cle)))


# =============================================================================================================================
# Cartes du monde (objets de contrôle et jeu planté)
# =============================================================================================================================
def inverser(loi):
    if isinstance(loi, dict):
        out = {}
        for k, v in loi.items():
            if k in ("poids", "biais") and loi.get("type") == "softmax":
                out[k] = (-np.asarray(v, float)).tolist()
            else:
                out[k] = inverser(v)
        return out
    if isinstance(loi, list):
        return [inverser(x) for x in loi]
    return loi


def cartes_du_monde(spec, oc):
    W = M.compiler_monde(spec)
    k1, eid, infos, vraies, fausses = M.jeu_plante_mr1(spec, oc.o)
    cartes = {"CTRL-V-monde": (W, "survit"),
              "CTRL-F-uniforme": ({"type": "fixe", "probas": [1.0, 1.0, 1.0]}, "éliminée"),
              "CTRL-F-marginale-fixe": ({"type": "fixe", "probas": [float(x) for x in oc.o.marg]}, "éliminée"),
              "CTRL-F-monde-inverse": (inverser(W), "éliminée"),
              "CTRL-copie-K1": (json.loads(json.dumps(k1)), "survit")}
    for nom, v in vraies.items():
        if nom != "V-monde":
            cartes["plantee:" + nom] = (v["loi"], None)
    for nom, l in fausses.items():
        if nom != "F1-copie":
            cartes["plantee:" + nom] = (l, None)
    return cartes, k1


# =============================================================================================================================
# Mutations du juge (doivent être refusées)
# =============================================================================================================================
def mutations(spec, r):
    partie = os.path.join(B.NOTES, "sorties-v4", f"partie-v4-monde-{r}.json")

    def mut_a(loi, chemin, sha_attendu, nom):  # ouvre la partie scellée du monde
        json.load(open(partie, encoding="utf-8"))
        return test_de_mort_programme(loi, chemin, sha_attendu, nom)

    def mut_b(loi, chemin, sha_attendu, nom):  # recompile la loi vraie en mémoire et s'en sert
        W = M.compiler_monde(spec)
        t = json.loads(open(chemin, "rb").read().decode())["tranches"][nom]
        Z, G = np.asarray(t["Z"]), np.asarray(t["G"])
        Q, P = probas(W, Z, G), probas(loi, Z, G)
        s = float((Q * (np.log(np.maximum(P, M.PLANCHER)) - np.log(Q.mean(axis=0)))).sum(axis=1).mean())
        return {"verdict": "survit" if s >= SEUIL else "éliminée", "statistique": s}

    def mut_d(loi, chemin, sha_attendu, nom):  # tire de nouvelles issues du monde
        t = json.loads(open(chemin, "rb").read().decode())["tranches"][nom]
        Z, G = np.asarray(t["Z"]), np.asarray(t["G"])
        M.tirer_issues(np.random.default_rng(0), probas(M.compiler_monde(spec), Z, G))
        return test_de_mort_programme(loi, chemin, sha_attendu, nom)

    return {"A-ouvre-la-partie-du-monde": (mut_a, {}), "B-recompile-la-loi-vraie": (mut_b, {}),
            "C-devis-du-monde-en-argument": (test_de_mort_programme, {"monde": spec}),
            "D-tire-des-issues-du-monde": (mut_d, {})}


# =============================================================================================================================
def courir_monde(r, dossier):
    spec, info = B.regenerer(r)
    oc = B.OracleCache(spec, r)
    W = M.compiler_monde(spec)
    D, nsp = spec["dimension"], spec["sous_populations"]
    cartes, k1 = cartes_du_monde(spec, oc)
    noms = sorted(cartes)
    # tranches : équivalence (une par carte, tâche 4) ; tenues à l'écart (REPETITIONS, tâche 3, partagées par les cartes)
    ch_eq = os.path.join(dossier, f"tranches-equivalence-monde-{r}.json")
    sha_eq = fournir_tranches(W, D, nsp, {nm: rng_tache(4, r, k) for k, nm in enumerate(noms)}, ch_eq)
    ch_te = os.path.join(dossier, f"tranches-tenues-a-l-ecart-monde-{r}.json")
    sha_te = fournir_tranches(W, D, nsp, {f"rep-{q}": rng_tache(3, r, q) for q in range(REPETITIONS)}, ch_te)
    res = {}
    for k, nm in enumerate(noms):
        loi, attendu = cartes[nm]
        ancien_eq = M.test_de_mort(loi, W, D, nsp, rng_tache(4, r, k))
        prog_eq = juger_sous_garde(test_de_mort_programme, loi, ch_eq, sha_eq, nm)
        reps = [juger_sous_garde(test_de_mort_programme, loi, ch_te, sha_te, f"rep-{q}") for q in range(REPETITIONS)]
        anciens = [M.test_de_mort(loi, W, D, nsp, rng_tache(5, r, k, q)) for q in range(REPETITIONS)]
        g_oracle = oc.o.gain(loi)
        attendu_oracle = "survit" if g_oracle >= SEUIL else "éliminée"
        # statistique « au-delà de l'archive {K1} » sur la tranche rep-0 (mesure, hors verdict)
        t0 = json.loads(open(ch_te, "rb").read().decode())["tranches"]["rep-0"]
        Z0, G0, Y0 = np.asarray(t0["Z"]), np.asarray(t0["G"]), np.asarray(t0["Y"])
        idx = np.arange(len(Y0))
        au_dela_k1 = float(np.mean(np.log(np.maximum(probas(loi, Z0, G0)[idx, Y0], M.PLANCHER))
                                   - np.log(np.maximum(probas(k1, Z0, G0)[idx, Y0], M.PLANCHER))))
        res[nm] = {"attendu_par_construction": attendu, "gain_oracle_contre_marginale": round(g_oracle, 6),
                   "attendu_oracle": attendu_oracle,
                   "equivalence": {"ancien": round(ancien_eq[0], 12), "programme": round(prog_eq["statistique"], 12),
                                   "ecart": abs(ancien_eq[0] - prog_eq["statistique"]),
                                   "verdicts_egaux": (ancien_eq[1] and prog_eq["verdict"] == "survit") or (not ancien_eq[1] and prog_eq["verdict"] == "éliminée")},
                   "verdict_rep0": reps[0]["verdict"], "statistique_rep0": round(reps[0]["statistique"], 6),
                   "survie_programme_sur_20": sum(x["verdict"] == "survit" for x in reps),
                   "survie_ancien_sur_20": sum(bool(a[1]) for a in anciens),
                   "statistique_moyenne_programme": round(float(np.mean([x["statistique"] for x in reps])), 6),
                   "au_dela_de_K1_rep0_mesure_hors_verdict": round(au_dela_k1, 6)}
        if attendu is not None:
            res[nm]["controle_tenu_rep0"] = reps[0]["verdict"] == attendu
            res[nm]["controle_tenu_sur_20"] = sum(x["verdict"] == attendu for x in reps)
    # garde : cas sain, puis mutations
    garde = {"sain": None, "mutations": {}}
    try:
        juger_sous_garde(test_de_mort_programme, W, ch_te, sha_te, "rep-0")
        garde["sain"] = "aucun refus (attendu)"
    except LectureLoiRefusee as ex:
        garde["sain"] = f"REFUS INATTENDU : {ex}"
    for nm, (fn, en_plus) in mutations(spec, r).items():
        try:
            v = juger_sous_garde(fn, W, ch_te, sha_te, "rep-0", **en_plus)
            garde["mutations"][nm] = {"refusee": False, "rendu": v}
        except LectureLoiRefusee as ex:
            garde["mutations"][nm] = {"refusee": True, "motif": str(ex)[:300]}
    return {"tranches": {"equivalence": {"fichier": os.path.basename(ch_eq), "sha256": sha_eq},
                         "tenues_a_l_ecart": {"fichier": os.path.basename(ch_te), "sha256": sha_te}},
            "cartes": res, "garde": garde, "eid_k1": oc.eid_k1}


def main(argv):
    if len(argv) < 3 or os.path.exists(argv[1]):
        print("usage : test_de_mort_programme_v1.py SORTIE.json DOSSIER_TRANCHES [MONDES…] (sortie neuve)", file=sys.stderr)
        return 2
    dossier = argv[2]
    os.makedirs(dossier, exist_ok=True)
    mondes = [int(x) for x in argv[3:]] or list(range(12))
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    par_monde = {}
    for r in mondes:
        par_monde[str(r)] = courir_monde(r, dossier)
        pm = par_monde[str(r)]
        print(r, {k: (v.get("controle_tenu_rep0"), v["survie_programme_sur_20"]) for k, v in pm["cartes"].items() if k.startswith("CTRL")},
              "garde", pm["garde"]["sain"][:20], [m["refusee"] for m in pm["garde"]["mutations"].values()], flush=True)
    toutes = [(r, nm, v) for r, pm in par_monde.items() for nm, v in pm["cartes"].items()]
    ctrl = [(r, nm, v) for r, nm, v in toutes if v["attendu_par_construction"] is not None]
    resume = {
        "equivalence_ecart_max": max(v["equivalence"]["ecart"] for _, _, v in toutes),
        "equivalence_verdicts_egaux": [sum(v["equivalence"]["verdicts_egaux"] for _, _, v in toutes), len(toutes)],
        "controles_tenus_rep0": [sum(v["controle_tenu_rep0"] for _, _, v in ctrl), len(ctrl)],
        "controles_par_objet": {nm: {"tenus_rep0": sum(v["controle_tenu_rep0"] for _, n2, v in ctrl if n2 == nm),
                                     "tenus_sur_20_total": sum(v["controle_tenu_sur_20"] for _, n2, v in ctrl if n2 == nm),
                                     "mondes": sum(1 for _, n2, _ in ctrl if n2 == nm)}
                                for nm in sorted({n2 for _, n2, _ in ctrl})},
        "accord_avec_oracle_programme": [sum(v["survie_programme_sur_20"] if v["attendu_oracle"] == "survit" else REPETITIONS - v["survie_programme_sur_20"] for _, _, v in toutes), REPETITIONS * len(toutes)],
        "accord_avec_oracle_ancien": [sum(v["survie_ancien_sur_20"] if v["attendu_oracle"] == "survit" else REPETITIONS - v["survie_ancien_sur_20"] for _, _, v in toutes), REPETITIONS * len(toutes)],
        "garde_sain_sans_refus": sum(pm["garde"]["sain"].startswith("aucun") for pm in par_monde.values()),
        "mutations_refusees": {m: sum(pm["garde"]["mutations"][m]["refusee"] for pm in par_monde.values())
                               for m in next(iter(par_monde.values()))["garde"]["mutations"]},
        "mondes": len(par_monde)}
    out = {"version": "test-de-mort-programme-v1", "debut_utc": debut,
           "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "script_sha256": sha(os.path.abspath(__file__)), "v1_bases_sha256": SHA_V1, "imports_sha256": B.IMPORTS,
           "python": sys.version.split()[0], "numpy": np.__version__,
           "regle": {"n": N_TRANCHE, "seuil": SEUIL, "statistique": "moyenne de log p_carte(y) − log m̂(y), m̂ = comptes + 0,5",
                     "survit_si": "s ≥ 0,02"},
           "graines": {"racine": RACINE, "regle": "SeedSequence(RACINE, spawn_key=(tache, monde, carte|repetition[, repetition])) ; tâche 3 tranches tenues à l'écart, 4 équivalence, 5 ancien test sur tranches distinctes ; jeu planté : oracle de la v4 (P1.cle) ; mondes : graines de la v4"},
           "repetitions": REPETITIONS, "mondes": mondes, "resume": resume, "par_monde": par_monde}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
