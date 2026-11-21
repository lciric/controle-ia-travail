"""Idée 1.1 — étape 0, version 4 (mutations et lecture v4). Version 3 : étape 0, version 3 (mutations v3 ; déclarations de la lecture v3). Version 2 : étape 0, version 2 (contre-lecture `8def0cf5…` : E1, m9, m10 ; modules v2). Version 1 : étape 0 du préenregistrement scellé `3ffe1739…` (« Étapes », 0 ; « Écarts, nœuds… », préalables 1 et 2 ;
« Coût et durée »). Ce module **n'écrit que des comptes, des temps et des empreintes**, jamais un résultat du jeu ; tout ce
qu'il rend est destiné à l'addendum d'empreintes (fichier d'étape 0 scellé).

Contenu :
1. **Préalable 1** : (a) les 16 noms empruntés par `nul_v9.py` présents dans les modules de `94bfd92` ; (b) essai E9 ;
   (c) **route première** : les essais d'origine du v9 (`test_nul_v9.py`, `d42a50eb…`) rejoués depuis une vue assemblée
   **hors du dépôt** (paquet `pole` de `94bfd92`, `pole/nul_v9.py`, `demonstrations/`, `essais/`, chaque fichier vérifié par
   empreinte), dans un interpréteur fils isolé (`-I -B`) dont le dossier courant et le dossier temporaire sont la vue
   elle-même ; aucun fichier de copie n'est lancé depuis son dossier. Classement : un essai qui échoue ou ne s'importe pas
   bloque, sauf s'il appartient à la classe `GrainesEtPreenregistrement`, déclarée par le texte comme route « à défaut » ;
   alors un essai réécrit est exigé — **aucun n'est écrit dans cette version** : un tel échec bloque aussi (« réécriture
   exigée, absente »), à lever par un texte ou un addendum neuf.
2. **Préalable 2** : empreinte de la preuve v3 (`a481c873…`) et du rapport de vérification (`b2f92646…`).
3. **Essais d'égalité** E0 (100 répétitions, archive A0, ligne Q1, graines (98, r) : La ≡ J8 à 10⁻¹² nat), E9, EP (50
   mondes de `essai_projection_cas_v1.py`, vue assemblée hors du dépôt : 10⁻⁹ nat sur chaque log e de bloc et sur le
   processus minimum), ED (jumeau contre J9 aux huit instants : 2·10⁻³ nat).
4. **Banc de mutations** et cas sains (`mutations_idee_1_1_v1`), critères de mort écrits de H7 et comptes de Hn.
5. **Chronométrage** : 20 répétitions d'essai de chacune des 30 lignes, graines (97, k), le programme n'écrivant que des
   temps ; durée attendue D = (Σ lignes, bras : temps × répétitions) / p ; **règle de réduction appliquée mécaniquement**.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import numpy as np

from ..gardes import GardeArret
from . import banc_idee_1_1_v2 as B
from . import mutations_idee_1_1_v4 as MU
from . import projection_bras_v1 as PB
from . import projection_commun_v1 as cm
from . import vue_v9_v1 as VV

RACINE_DEPOT = VV.RACINE_DEPOT
EMPREINTE_PREUVE_V3 = "a481c873a317a710923ee6134f410f45b5dd14392738b768ecad0fdffb3547c1"
CHEMIN_PREUVE_V3 = "docs/notes/organisme-idees-juge-v1/preuve-idee-1-1-poids-du-nul-v3.md"
EMPREINTE_VER = "b2f92646eea8a80051c798685c2ae00f013008acda26e6f214d115b0cb2705b9"
CHEMIN_VER = "docs/notes/organisme-idees-juge-v1/verification-preuve-v3-et-brouillon4-idee-1-1-v1.md"
DOSSIER_PROJECTION = RACINE_DEPOT / "docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection"
FICHIERS_EP = {"essai_projection_commun_v1.py": "1f4ada977b6cdb96378f3c913df0119bcf6fc333981217ecbbb3583b38f2ca54",
               "essai_projection_methodes_v1.py": "29704896ec641feff607d42c2636c456e372a2a9f4deb589efd4b8256c8b4105",
               "essai_projection_cas_v1.py": None}      # empreinte de son seul compagnon (le texte ne la cite pas)
CAS_EP = ("T01_copie_membre_lineaire", "T02_bord_une_loi_connue", "T03_poids_extremes", "T04_bord_loi_aveugle_constante",
          "T05_copie_coupure_archive", "T06_copie_coupure_hors_archive", "T07_copie_sous_population",
          "T08_copie_coupure_archive_bruit_commun", "T09_copie_deux_niveaux_archive", "T10_monde_coupure_carte_neuve",
          "T11_monde_lineaire_carte_surconfiante", "T12_monde_coupure_carte_autre_membre")
CLASSE_A_DEFAUT = "GrainesEtPreenregistrement"
CLASSES_ATTENDUES_REJOUABLES = ("MembresNulV9", "CertificatMorceaux", "EvaluateurV9", "TricheursParMorceaux", "LectureGelee",
                                "DescriptionPublique")
ESSAIS_REECRITS: dict = {}       # aucun dans cette version (voir l'en-tête)
DUREE_MAX_ATTENDUE_H = 32.0
PROCESSUS_MAX = 3
CHRONO_REPETITIONS = 20
TOL_E0, TOL_EP, TOL_ED = 1e-12, 1e-9, 2e-3
LIGNES_JUGEABLES = tuple(i for i, n in enumerate(B.NOMS) if n != "H7")


def sha256(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# --- préalables --------------------------------------------------------------------------------------------------------
def prealable_2() -> dict:
    sortie = {}
    for chemin, attendu in ((CHEMIN_PREUVE_V3, EMPREINTE_PREUVE_V3), (CHEMIN_VER, EMPREINTE_VER)):
        h = sha256(RACINE_DEPOT / chemin)
        if h != attendu:
            raise GardeArret(f"préalable 2 : {chemin} d'empreinte {h[:12]}… ≠ {attendu[:12]}… : la preuve change, préalable rouvert")
        sortie[chemin] = h
    return sortie


RUNNER = r'''
import importlib.util, json, os, sys, traceback, unittest
vue, sortie, filtre = sys.argv[1], sys.argv[2], sys.argv[3:]
sys.path.insert(0, vue)
res = {"import": None, "essais": []}
try:
    spec = importlib.util.spec_from_file_location("test_nul_v9", os.path.join(vue, "essais", "test_nul_v9.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    res["import"] = "ok"
except BaseException:
    res["import"] = traceback.format_exc()[-3000:]
    json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False)
    sys.exit(0)
def plat(s):
    for t in s:
        if isinstance(t, unittest.TestSuite):
            yield from plat(t)
        else:
            yield t
for t in plat(unittest.defaultTestLoader.loadTestsFromModule(mod)):
    classe = type(t).__name__
    if filtre and classe not in filtre:
        continue
    r = unittest.TestResult()
    t.run(r)
    if r.errors or r.failures:
        statut = "echoue"
    elif r.skipped:
        statut = "saute"
    else:
        statut = "passe"
    detail = "\n".join(tb for _, tb in (r.errors + r.failures))[-2000:]
    res["essais"].append({"id": t.id(), "classe": classe, "statut": statut, "detail": detail})
json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False)
'''


def rejeu_essais_v9(dossier_travail: Path, filtre=()) -> dict:
    """Condition (c) du préalable 1 : vue assemblée hors du dépôt, essais d'origine importés et joués un à un."""
    dossier_travail = Path(dossier_travail).resolve()
    vue = dossier_travail / "vue-v9"
    attendu = VV.assembler_vue(vue)
    tmp = vue / "tmp-essais"
    tmp.mkdir()
    sortie = dossier_travail / "rejeu-v9.json"
    env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(tmp), "TMPDIR": str(tmp), "LANG": "C.UTF-8",
           "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
    t0 = time.time()
    r = subprocess.run([sys.executable, "-I", "-B", "-c", RUNNER, str(vue), str(sortie), *filtre], cwd=str(vue), env=env,
                       capture_output=True, text=True)
    duree = time.time() - t0
    if r.returncode != 0 or not sortie.is_file():
        raise GardeArret(f"rejeu des essais du v9 : interpréteur fils en échec ({r.returncode}) : pas de jeu\n{r.stderr[-2000:]}")
    res = json.loads(sortie.read_text(encoding="utf-8"))
    VV.verifier_vue(vue, attendu)
    res["duree_s"] = round(duree, 1)
    res["vue"] = {"fichiers": len(attendu), "empreinte_de_la_liste": hashlib.sha256(json.dumps(attendu, sort_keys=True).encode()).hexdigest()}
    res["classement"] = classer_rejeu(res, filtre)
    return res


def classer_rejeu(res: dict, filtre=()) -> dict:
    if res.get("import") != "ok":
        return {"passe": False, "raison": "essais d'origine non importables : pas de jeu", "a_defaut": []}
    echecs = [e for e in res["essais"] if e["statut"] != "passe"]
    bloquants = [e["id"] for e in echecs if e["classe"] != CLASSE_A_DEFAUT]
    a_defaut = [e["id"] for e in echecs if e["classe"] == CLASSE_A_DEFAUT]
    sans_reecrit = [i for i in a_defaut if i not in ESSAIS_REECRITS]
    classes = {e["classe"] for e in res["essais"]}
    manquantes = [c for c in CLASSES_ATTENDUES_REJOUABLES if c not in classes and (not filtre or c in filtre)]
    ok = not bloquants and not sans_reecrit and not manquantes and (bool(filtre) or len(res["essais"]) > 0)
    return {"passe": ok and not filtre, "essais": len(res["essais"]), "passes": len(res["essais"]) - len(echecs),
            "bloquants": bloquants, "a_defaut": a_defaut, "reecriture_exigee_absente": sans_reecrit,
            "classes_manquantes": manquantes, "filtre": list(filtre),
            "raison": "rejeu partiel (filtre) : n'est pas le préalable" if filtre else
                      ("route première passée" if ok else "pas de jeu : essai d'origine en échec ou réécriture absente")}


# --- essais d'égalité -----------------------------------------------------------------------------------------------------
def _tirer_sans_geler_tout(rep, quoi: tuple) -> None:
    rep.engagements = {q: rep.construire_engagement(q) for q in quoi}
    rep.empreintes_gel = {q: g.empreinte for q, g in rep.engagements.items()}
    rep.journal = {}
    rep.etat = "gelee"
    rep.tirer()


def essai_E0(V, racine: int, n: int = 100) -> dict:
    ecarts, officiels = [], 0
    for r in range(n):
        rep = B.Repetition(V, racine, B.INDICE["Q1"], r, cle=(98, r), archive_A0=True, actifs=())
        _tirer_sans_geler_tout(rep, ("J8", "La"))
        P8, _ = B.pieces_communes(V, rep.engagements["J8"], rep.tirages_de("J8"))
        Pa, cache = B.pieces_communes(V, rep.engagements["La"], rep.tirages_de("La"))
        _, _, mor = B.separer(V, rep.engagements["La"].engagement["bibliotheque"])
        if mor:
            raise GardeArret("E0 : La sous l'archive A0 porte des membres par morceaux")
        lw8, lwa = P8.log_w()[0], Pa.log_w()[0]
        ecarts.append(max(abs(a - b) for a, b in zip(lw8, lwa)))
        e8 = V.J.nf.evaluer_v2(rep.engagements["J8"], rep.tirages_de("J8"))
        ea = V.limite.evaluer_v9(rep.engagements["La"], rep.tirages_de("La"))
        officiels += int(e8["trajectoire_log_w"] != ea["trajectoire_log_w"] or e8["promue"] != ea["promue"])
    ok = max(ecarts) <= TOL_E0 and officiels == 0
    return {"repetitions": n, "ecart_max": max(ecarts), "evaluations_officielles_differentes": officiels, "passe": ok}


def essai_E9(V, racine: int, repetitions: int = 2) -> dict:
    """J9 sans ses membres par morceaux (`nul_v9.sans_morceaux`, évalué par `evaluer_v9`) ≡ J8 (`evaluer_v2`), valeur pour
    valeur ; en plus (essai du code de ce banc, hors texte) : richesses détaillées de J8, J9, La, Ld arrondies à six
    décimales = évaluations officielles."""
    k = MU.CLES["E9"]
    echecs, detail, n = [], [], 0
    for i in LIGNES_JUGEABLES:
        for r in range(repetitions):
            rec, rep = B.jouer_repetition(V, racine, i, r, cle=(97, k, i, r))
            g9 = rep.engagements["J9"]
            gs = V.J.sp.geler_engagement(V.v9.sans_morceaux(g9.engagement))
            ts = {"empreinte_engagement": gs.empreinte, "issues": list(rep.issues), "plan_execution": "ordre_naturel"}
            ev9s = V.v9.evaluer_v9(gs, ts)
            n += 1
            if "J8" in rep.engagements:
                ev8 = V.J.nf.evaluer_v2(rep.engagements["J8"], rep.tirages_de("J8"))
                if ev8 != ev9s:
                    echecs.append((B.NOMS[i], r, "E9"))
                for q, ev in (("J8", ev8), ("J9", V.v9.evaluer_v9(g9, rep.tirages_de("J9"))),
                              ("La", V.limite.evaluer_v9(rep.engagements["La"], rep.tirages_de("La"))),
                              ("Ld", V.limite.evaluer_v9(rep.engagements["Ld"], rep.tirages_de("Ld")))):
                    if [round(v, 6) for v in rec[q]["log_w"]] != ev["trajectoire_log_w"] or rec[q]["promue"] != ev["promue"]:
                        detail.append((B.NOMS[i], r, q))
            else:
                ev9 = V.v9.evaluer_v9(g9, rep.tirages_de("J9"))
                if [round(v, 6) for v in rec["J9"]["log_w"]] != ev9["trajectoire_log_w"] or rec["J9"]["promue"] != ev9["promue"]:
                    detail.append((B.NOMS[i], r, "J9"))
    return {"evaluations": n, "echecs_E9": echecs, "echecs_identite_detaillee": detail, "passe": not echecs and not detail,
            "graines": f"(97, {k}, i_ligne, r), r < {repetitions}, lignes {list(LIGNES_JUGEABLES)}"}


def essai_ED(V, racine: int, repetitions: int = 2) -> dict:
    k = MU.CLES["ED"]
    ecarts = []
    for i in LIGNES_JUGEABLES:
        for r in range(repetitions):
            rec, _ = B.jouer_repetition(V, racine, i, r, cle=(97, k, i, r))
            ecarts.append(rec["ED_ecart_T8"])
    return {"repetitions": len(ecarts), "ecart_max": max(ecarts), "passe": max(ecarts) <= TOL_ED,
            "graines": f"(97, {k}, i_ligne, r), r < {repetitions}"}


def vue_projection(dossier: Path) -> Path:
    """Vue hors du dépôt des trois fichiers de la course de conception employés par EP, vérifiés par empreinte."""
    dossier = Path(dossier).resolve()
    if RACINE_DEPOT.resolve() in dossier.parents:
        raise GardeArret("vue de projection sous le dépôt : interdit")
    dossier.mkdir(parents=True)
    for nom, attendu in FICHIERS_EP.items():
        src = DOSSIER_PROJECTION / nom
        h = sha256(src)
        comp = Path(str(src) + ".sha256").read_text(encoding="utf-8").split()[0]
        if h != comp or (attendu is not None and h != attendu):
            raise GardeArret(f"EP : {nom} d'empreinte {h[:12]}… non conforme")
        (dossier / nom).write_bytes(src.read_bytes())
        if sha256(dossier / nom) != h:
            raise GardeArret(f"EP : recopie de {nom} altérée")
    return dossier


def essai_EP(racine: int, dossier_travail: Path, n: int = 50) -> dict:
    """Le module de projection de ce banc (forme scindée, sans W^reste), contre `m3_toutes_coupures` et
    `_blocs_projection` du code de la course (vue hors du dépôt) : ≤ 10⁻⁹ nat sur chaque log e de bloc et sur le
    processus minimum."""
    import importlib
    vue = vue_projection(Path(dossier_travail) / "vue-projection")
    sys.path.insert(0, str(vue))
    try:
        cm0 = importlib.import_module("essai_projection_commun_v1")
        me0 = importlib.import_module("essai_projection_methodes_v1")
        cs0 = importlib.import_module("essai_projection_cas_v1")
        for m_ in (cm0, me0, cs0):
            if Path(m_.__file__).resolve().parent != vue:
                raise GardeArret(f"EP : {m_.__name__} chargé hors de la vue")
        k = MU.CLES["EP"]
        e_bloc, e_min = 0.0, 0.0
        for w in range(n):
            rng = B.generateur(racine, 97, k, w)
            m = cs0.construire(rng, CAS_EP[w % len(CAS_EP)])
            L_, Q, y, z, g = m["L"], m["Q"], m["y"], m["z"], m["g"]
            q = []
            for b, (a, e) in enumerate(cm0.BLOCS):
                q.append((b, np.zeros(e - a, int)))
                q.append((b, g[a:e]))
            for j in range(cm0.D):
                for b, (a, e) in enumerate(cm0.BLOCS):
                    rang = np.argsort(np.argsort(z[a:e, j]))
                    for i in range(1, 25):
                        q.append((b, (rang >= i).astype(int)))
            ref = me0._blocs_projection(L_, Q, y, q, 2, me0.IT_PROJ, None, chaud=True)
            ref_min = me0.m3_toutes_coupures(m)
            Qb = np.stack([Q[a:e] for a, e in cm.BLOCS])
            qs = {b: PB.questions_j9p(z, g, b) for b in range(PB.NB)}
            proj = PB.projeter(L_, Qb, qs, 2, range(PB.NB))
            le = PB.valeurs_e(proj, Qb, {b: y[a:e] for b, (a, e) in enumerate(cm.BLOCS)})
            # ordre de `ref` : (bloc 0..7 : lin, sp), puis trait 0 (blocs, 24), puis trait 1 (blocs, 24)
            mien = [le[b][0] if t == 0 else le[b][1] for b in range(PB.NB) for t in (0, 1)]
            for j in range(cm.D):
                for b in range(PB.NB):
                    mien += list(le[b][2 + 24 * j:2 + 24 * (j + 1)])
            e_bloc = max(e_bloc, float(np.max(np.abs(np.asarray(mien) - ref))))
            proc, _ = PB.processus_j9p(le, z)
            e_min = max(e_min, float(np.max(np.abs(proc.min(0) - ref_min))))
    finally:
        sys.path.remove(str(vue))
        for nom in ("essai_projection_commun_v1", "essai_projection_methodes_v1", "essai_projection_cas_v1"):
            sys.modules.pop(nom, None)
    return {"mondes": n, "ecart_max_log_e_bloc": e_bloc, "ecart_max_processus_minimum": e_min,
            "passe": e_bloc <= TOL_EP and e_min <= TOL_EP, "graines": f"(97, {k}, w), w < {n} ; cas T01 à T12 en cycle"}


# --- chronométrage et règle de réduction -----------------------------------------------------------------------------------
GROUPE_DU_TEMPS = {"jumeau": "jumeau", "J9-Dc": "jumeau", "projection_J9-P": "J9-P", "J9-P_valeurs": "J9-P",
                   "projection_La-P": "La-P", "La-P_valeurs": "La-P"}


def chronometrer(V, racine: int, n: int = CHRONO_REPETITIONS, lignes=None) -> dict:
    """Temps moyen par répétition et par groupe de bras, pour chaque ligne (graines (97, k, i_ligne, r)) ; le programme
    n'écrit que des temps."""
    k = MU.CLES["chronometrage"]
    sortie = {}
    for i in (range(len(B.LIGNES)) if lignes is None else lignes):
        tot = {"base": 0.0, "jumeau": 0.0, "J9-P": 0.0, "La-P": 0.0}
        for r in range(n):
            t0 = time.perf_counter()
            rec, rep = B.jouer_repetition(V, racine, i, r, cle=(97, k, i, r))
            mur = time.perf_counter() - t0
            seg = dict(rep.temps)
            groupes = {"base": 0.0, "jumeau": 0.0, "J9-P": 0.0, "La-P": 0.0}
            for cle, v in seg.items():
                groupes[GROUPE_DU_TEMPS.get(cle, "base")] += v
            groupes["base"] += max(0.0, mur - sum(seg.values()))
            for g, v in groupes.items():
                tot[g] += v
        sortie[B.NOMS[i]] = {g: v / n for g, v in tot.items()}
    return {"repetitions_par_ligne": n, "secondes_par_repetition": sortie, "graines": f"(97, {k}, i_ligne, r), r < {n}"}


def repetitions_par_groupe(nom: str, reductions) -> dict:
    i = B.INDICE[nom]
    compte = {"base": B.REPETITIONS, "jumeau": 0, "J9-P": 0, "La-P": 0}
    for r in range(B.REPETITIONS):
        a = B.actifs_pour(i, r, reductions)
        compte["jumeau"] += int("jumeau" in a)
        compte["J9-P"] += int("J9-P" in a)
        compte["La-P"] += int("La-P" in a)
    return compte


def duree_attendue_h(temps: dict, reductions, p: int) -> float:
    if not 1 <= p <= PROCESSUS_MAX:
        raise GardeArret(f"p = {p} : 1 à 3 processus (texte)")
    tot = 0.0
    for nom, t in temps.items():
        rep = repetitions_par_groupe(nom, reductions)
        tot += sum(t[g] * rep[g] for g in t)
    return tot / p / 3600.0


def regle_de_reduction(temps: dict, p: int) -> dict:
    """Règle écrite d'avance : si D > 32 h, réductions 1 à 5 dans cet ordre, chacune en entier, jusqu'à D ≤ 32 h ; au-delà
    de la réduction 5 : pas de jeu, texte neuf. Décidée sur le seul chronométrage."""
    if set(temps) != set(B.NOMS):
        raise GardeArret("chronométrage incomplet : les 30 lignes sont exigées")
    appliquees, D = [], duree_attendue_h(temps, (), p)
    trace = [{"reductions": [], "D_h": D}]
    while D > DUREE_MAX_ATTENDUE_H and len(appliquees) < 5:
        appliquees.append(len(appliquees) + 1)
        D = duree_attendue_h(temps, tuple(appliquees), p)
        trace.append({"reductions": list(appliquees), "D_h": D})
    return {"processus": p, "reductions": appliquees, "D_h": D, "trace": trace,
            "jeu_permis": D <= DUREE_MAX_ATTENDUE_H,
            "libelles": [B.REDUCTIONS[k] for k in appliquees]}


# --- tout ------------------------------------------------------------------------------------------------------------------
def etape0(racine: int, dossier_travail: Path, *, p: int = PROCESSUS_MAX, journal=print) -> dict:
    V = VV.charger()
    res: dict = {"objet": "étape 0 de l'idée 1.1 (comptes, temps, empreintes ; aucun résultat de jeu)",
                 "preenregistrement": {"chemin": B.CHEMIN_PREREG, "sha256": B.EMPREINTE_PREREG}}
    t0 = time.time()
    res["prealable_2"] = prealable_2()
    res["copies"] = V.empreintes
    res["prealable_1"] = {"a_noms_empruntes": VV.exiger_noms_empruntes(V.J)}
    journal("préalable 1 (c) : rejeu des essais d'origine du v9 (vue hors du dépôt)")
    res["prealable_1"]["c_rejeu"] = rejeu_essais_v9(dossier_travail)
    journal("essais d'égalité")
    res["E0"] = essai_E0(V, racine)
    res["E9"] = essai_E9(V, racine)
    res["prealable_1"]["b_E9"] = res["E9"]["passe"]
    res["EP"] = essai_EP(racine, dossier_travail)
    res["ED"] = essai_ED(V, racine)
    journal("banc de mutations et cas sains")
    res["mutations"] = MU.jouer_banc(V, racine)
    journal("garde P4 : H7 et Hn, 200 répétitions chacune")
    h7, hn = MU.compter_garde(V, racine, "H7"), MU.compter_garde(V, racine, "Hn")
    res["garde_P4"] = {"H7": h7, "Hn": hn, "verdict": MU.verdict_garde(h7, hn)}
    journal("chronométrage : 20 répétitions de chacune des 30 lignes")
    res["chronometrage"] = chronometrer(V, racine)
    res["programme"] = regle_de_reduction(res["chronometrage"]["secondes_par_repetition"], p)
    res["cles_97"] = dict(MU.CLES)
    res["declarations"] = declarations_v3()
    res["duree_etape0_s"] = round(time.time() - t0, 1)
    res["bloquants"] = bloquants(res)
    res["jeu_permis"] = not res["bloquants"]
    return res


def bloquants(res: dict) -> list[str]:
    b = []
    if not res["prealable_1"]["c_rejeu"]["classement"]["passe"]:
        b.append("préalable 1 (c) : " + res["prealable_1"]["c_rejeu"]["classement"]["raison"])
    for e in ("E0", "E9", "EP", "ED"):
        if not res[e]["passe"]:
            b.append(f"essai {e} manqué : arrêt avant le jeu ; défaut")
    if not res["mutations"]["toutes_tuees"]:
        b.append("une mutation survit : pas de jeu")
    if not res["mutations"]["cas_sains_passes"]:
        b.append("un cas sain manqué : pas de jeu")
    if res["garde_P4"]["verdict"]["bloque_le_jeu"]:
        b.append("garde P4 : critère de mort de H7 manqué, cas sain manqué, ou Hn sous gel anormal : pas de jeu, texte neuf")
    if not res["programme"]["jeu_permis"]:
        b.append("durée attendue > 32 h après toutes les réductions permises : pas de jeu, texte neuf")
    return b


# ==================================================================================================================
# Version 2 (contre-lecture `8def0cf5…`) : E1 (les essais d'égalité, rejouables par le lanceur, étape 2 du texte) ;
# m9, m10, comptes non écrits : déclarations imprimées dans le bloc d'addendum.
def essais_d_egalite(V, racine: int, dossier_travail: Path) -> dict:
    """E0, E9, EP, ED (étape 2 du texte) ; tout essai manqué arrête avant le jeu."""
    r = {"E0": essai_E0(V, racine), "E9": essai_E9(V, racine), "EP": essai_EP(racine, dossier_travail), "ED": essai_ED(V, racine)}
    manques = [k for k, v in r.items() if not v["passe"]]
    if manques:
        raise GardeArret(f"essai {', '.join(manques)} manqué : arrêt avant le jeu ; défaut")
    return r


def empreintes_ep() -> dict:
    """m10 : empreintes des trois fichiers de la course employés par EP (celle de `essai_projection_cas_v1.py` n'est
    pas citée par le texte : elle est inscrite à l'addendum)."""
    return {nom: sha256(DOSSIER_PROJECTION / nom) for nom in FICHIERS_EP}


def declarations() -> dict:
    return {
        "m9_graines_des_essais": "les essais prolongent les clés du texte : E0 (98, r, 0) et (98, r, 1) ; essais, mutations, "
                                  "chronométrage (97, k, …, 0) et (97, k, …, 1) (deux flux par répétition) ; k listés dans "
                                  "`cles_97` du fichier d'étape 0",
        "m10_empreintes_EP": empreintes_ep(),
        "m11": "le lanceur rejoue les essais, les dix-sept mutations et E0, E9, EP, ED ; il ne rejoue pas les comptes de H7 "
               "et de Hn (critère de mort, cas sain, Hn sous gel) : ils valent pour le code gelé par l'égalité, fichier par "
               "fichier, des empreintes du fichier d'étape 0 et de l'addendum (M2)",
        "comptes_non_ecrits_par_le_texte": {
            "E9": "2 répétitions de chacune des 29 lignes jugeables (toutes sauf H7)",
            "ED": "2 répétitions de chacune des 29 lignes jugeables",
            "EP": "50 mondes de `essai_projection_cas_v1.construire`, cas T01 à T12 en cycle",
            "mutation_certificat": "30 répétitions de Q8, de Q1 et de Q2 ; tuée par au moins une promotion de J9-P ; cas sain : "
                                   "aucune promotion sur les copies Q1, Q2 (Q8 rapporté)",
            "mutation_w_reste": "détecteur : carte log-linéaire de S1 (puissance 2, inclinaison [0,5 ; −0,5 ; 0]), 3 répétitions, "
                                "log W maximal de J9-P ≤ 10⁻⁶ exigé du code juste",
            "Hn_sous_gel": "bloque à 3 promotions ou plus sur 200, terme sur toutes les familles ou famille linéaire seule"},
    }



def declarations_v3() -> dict:
    """Déclarations v2, plus les lectures de la lecture gelée v3 (n2, n3, n4, n5, strates, m6), à inscrire à l'addendum."""
    from . import lecture_idee_1_1_v4 as LE3
    d = declarations()
    d["lectures_de_la_lecture_gelee"] = dict(LE3.LECTURES_DECLAREES)
    return d
