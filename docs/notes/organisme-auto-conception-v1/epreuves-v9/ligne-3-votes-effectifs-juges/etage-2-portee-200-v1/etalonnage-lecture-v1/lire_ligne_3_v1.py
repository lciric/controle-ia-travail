#!/usr/bin/env python3
"""Lecture unique de l'étage 2 à 200 témoins — ligne 3 de l'organisme v9 (votes effectifs des juges croisés) — v1.

Plan de code : annexe A du texte v7 (`preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, 4e3680d9…), l. 562 ;
« Mesures de l'étage 2 » (l. 293), « Lecture par colonne » (l. 295), « Lecture unique » (l. 297), racine 2026111936 du
rééchantillonnage de l'étage 2 (l. 303), ordre des gestes (l. 305 (9) et (10)), table de l'étage 2 (l. 333 à 343), audit de
symétrie (l. 347 à 350), plafond (l. 384, 388). Tailles à 200 : additif 3 v3 (71b7a876…, § 4.2 ; seuil de 40 témoins
complets gardé à la lettre). **Issue B** du verdict « portée à 200 » v2 (02928723…) : comparaisons d'agrégations
descriptives ; rangs 2 et 4 inatteignables ; **aucun « oui » n'est rendu** ; « ρ′ − ρ positif pour les deux juges » se
rapporte comme une mesure, sans verdict sur la correction ; le reste est non concluant.

Ce que fait ce programme, et rien d'autre :
- **avant toute lecture d'un verdict**, il refuse de tourner : si son rapport existe déjà (lecture unique) ou si son dossier
  existe ; si la pièce d'étalonnage n'est pas scellée (empreinte et compagnon) ou ne nomme pas la banque et les verdicts
  d'étalonnage du dépôt ; si l'audit de symétrie (règle R4) n'est pas écrit et scellé, ne cite pas l'empreinte de la pièce
  d'étalonnage, ou porte un contrôle non tenu ; si la racine 2026111936 n'est pas autorisée (additif de code, par chemin et
  empreinte) ; si le dépôt porte une exécution plus récente que celle qu'on lui nomme ;
- il lit alors tout : la banque, les verdicts des deux moitiés, l'état des juges, le rapport d'exécution et le journal du
  compteur du code d'appel v4 ; il recalcule l'étalonnage et exige l'égalité avec la pièce scellée ;
- il mesure, par les fonctions du banc de l'étage 1 v4 (importé par empreinte, via `etalonner_ligne_3_v1.py`, lui aussi
  importé par empreinte) : ρ entre juges sur le bloc A, son intervalle et les votes effectifs ; ρ′ de chaque juge et ρ′ − ρ
  (intervalle apparié) ; les bras U, C, S-Opus, S-Argon, R-Argon, R-Opus-2, F, P sur la moitié « lecture » ; les comparaisons
  descriptives ; le témoin apparié ; la lecture par colonne ; la table par juge ; le coût apparié relu au journal ;
- il applique la table de l'étage 2 en issue B et l'audit « trop propre » / « trop sale », puis écrit et scelle son rapport
  et un manifeste (règle R9). Le rapport est une **aide** : le verdict est prononcé par un agent neuf (règle R13).

Rééchantillonnage : `numpy.random.SeedSequence(2026111936, spawn_key=(clé,))`, table des clés gelée (`CLES_TACHES`) ;
2 000 tirages, centiles, stratifié par classe, sur les comptes de configurations (fonctions du banc). Mode « essais » des
essais seulement : racine 2026111930 ; aucune autre racine n'est dérivable.

Usage (après l'étalonnage scellé et l'audit de symétrie scellé ; jamais lancé par l'auteur sur de vrais verdicts) :
    python3 -I -B lire_ligne_3_v1.py --banque BANQUE.json --banque-sha HEX --depot DEPOT --execution K \
        --rapport-execution-sha HEX --etalonnage DOSSIER/etalonnage/etalonnage-etage-2-ligne-3-v1.json \
        --etalonnage-sha HEX --audit AUDIT.json --audit-sha HEX --autorisation-additif CHEMIN --empreinte-additif HEX
Écrit DOSSIER/lecture/ (DOSSIER = parent du dossier de l'étalonnage). Codes : 0 rapport écrit ; 2 refus.

Développeur, modèle O.
"""
from __future__ import annotations

import json
import sys
import types
from fractions import Fraction
from pathlib import Path

VERSION = "lire_ligne_3_v1"

# --- le programme d'étalonnage, importé par empreinte (ses lectures communes et le chargeur du banc v4) ------------------
ETALONNER = ("etalonner_ligne_3_v1.py", "37a63c9b02eb6483edb088ee01f7dab90aaac80127c56c24e081545831291919")
NOM_MODULE_ETALONNER = "etalonner_ligne_3_v1"


def charger_etalonner():
    chemin = Path(__file__).resolve().parent / ETALONNER[0]
    try:
        octets = chemin.read_bytes()
    except OSError:
        raise RuntimeError("etalonner_ligne_3_v1.py absent à côté de ce programme") from None
    import hashlib
    if hashlib.sha256(octets).hexdigest() != ETALONNER[1]:
        raise RuntimeError("etalonner_ligne_3_v1.py d'une autre empreinte que celle de ce programme : aucun import")
    m = sys.modules.get(NOM_MODULE_ETALONNER)
    if m is not None:
        f = getattr(m, "__file__", None)
        if f is None or hashlib.sha256(Path(f).read_bytes()).hexdigest() != ETALONNER[1]:
            raise RuntimeError("module etalonner_ligne_3_v1 déjà chargé avec une autre empreinte")
        return m
    m = types.ModuleType(NOM_MODULE_ETALONNER)
    m.__file__ = str(chemin)
    sys.modules[NOM_MODULE_ETALONNER] = m
    try:
        exec(compile(octets, str(chemin), "exec"), m.__dict__)
    except BaseException:
        del sys.modules[NOM_MODULE_ETALONNER]
        raise
    return m


ET = charger_etalonner()
Refus = ET.Refus

# --- issue de la portée (verdict scellé) -----------------------------------------------------------------------------------
ISSUE_PORTEE = "B"
OUI_POSSIBLE = False                       # issue B : additif 3, § 3 ; texte l. 343

# --- graines (règle R9) -------------------------------------------------------------------------------------------------
RACINE_ESSAIS = 2026111930
RACINE_LECTURE = 2026111936                # texte l. 303 : « rééchantillonnage de l'étage 2 »
RACINES_TOUJOURS_REFUSEES = (2026111931, 2026111932, 2026111933, 2026111934, 2026111935, 2026111937,
                             2026112031, 2026112032, 2026112033)
CLES_TACHES = {"rho_entre_juges_bloc_A": 1, "ecarts_rho_prime_moins_rho": 2, "comparaisons_bloc_A": 3,
               "comparaisons_bras_R": 4, "lecture_par_colonne": 5}
REGLE_DES_GRAINES = "numpy.random.SeedSequence(racine, spawn_key=(clé,)) ; numpy.random.default_rng ; numpy ≥ 1.25"
TIRAGES = 2000                             # texte, « Intervalles »

# --- seuils gelés (texte « Seuil », « Critères de lecture gelés », « Audit de symétrie » ; additif 3, § 4.2) -------------
SEUIL_COMPLETS_LECTURE = 40                # l. 337 ; gardé à 40 (additif 3, § 7, nœud 2 ; GO-2026-11-20-36)
TAUX_ERREUR_PRISE = (Fraction(5, 100), Fraction(45, 100))   # l. 182 : « entre 0,05 et 0,45 »
DEMI_LARGEUR_RHO_MAX = 0.25                # l. 182
SEUIL_ABSENTS = Fraction(1, 10)            # l. 337 : « plus de 10 % »
MARGE_COMPARAISON = 0.05                   # l. 178, 180
BORNE_NUL_OU_NEGATIF = 0.10                # l. 181
TROP_PROPRE_DISTANCE = 0.02                # l. 348
TROP_SALE_EE = 0.40                        # l. 349
TROP_SALE_RHO = -0.2                       # l. 349
EPS = 1e-12

# --- pièces d'entrée et sorties --------------------------------------------------------------------------------------------
PIECE_AUDIT = "audit de symétrie (règle R4), étage 2, ligne 3"
CONTROLES_AUDIT = ("verite_non_servie", "consigne_servie_empreinte_attendue", "lecteur_rend_absent_pour_illisible",
                   "appariement_temoin_verdict", "juges_scriptes_parfait_et_hasard")
SOUS_DOSSIER = "lecture"
FICHIER_RAPPORT = "rapport-lecture-etage-2-ligne-3-v1.json"
FICHIER_MANIFESTE = "manifeste-lecture-etage-2-ligne-3-v1.json"

MOTS_TABLE = {
    "rang_1": "non concluant",
    "rang_1_manque": "non concluant par manque de témoins",
    "rang_3": "non : un juge répété vaut le collège",
    "mesure_decorrele": ("non concluant sur la correction (issue B : aucun « oui » possible) ; mesure rapportée : le "
                         "croisement décorrèle les erreurs (ρ′ − ρ « positif » pour les deux juges)"),
    "rang_5": "non concluant",
}


# --- graines ------------------------------------------------------------------------------------------------------------


class Graines:
    """Racine du mode : « essais » → 2026111930 ; « reel » → 2026111936, seulement sur l'additif de code scellé (chemin et
    empreinte), vérifié **avant toute dérivation et toute lecture**. Toute autre racine : jamais."""

    def __init__(self, mode: str, autorisation=None):
        if mode == "essais":
            self.racine = RACINE_ESSAIS
            self.autorisation = None
        elif mode == "reel":
            if autorisation is None:
                raise Refus("racine 2026111936 : refus sans autorisation (additif de code de l'étage 2 scellé)")
            chemin, emp = autorisation
            if not ET.est_empreinte(emp):
                raise Refus("racine 2026111936 : empreinte de l'additif mal formée")
            ET.garde_chemins([chemin])
            try:
                h = ET.sha256_fichier(chemin)
            except OSError:
                raise Refus("racine 2026111936 : additif absent") from None
            if h != emp:
                raise Refus("racine 2026111936 : empreinte de l'additif différente de l'attendue")
            self.racine = RACINE_LECTURE
            self.autorisation = {"chemin_additif": str(chemin), "empreinte_additif": emp}
        else:
            raise Refus(f"mode inconnu : {mode!r}")
        if self.racine in RACINES_TOUJOURS_REFUSEES:
            raise Refus("racine refusée")
        self.mode = mode
        self.derivations = []

    def rng(self, tache: str):
        import re
        import numpy as np
        m = re.match(r"^(\d+)\.(\d+)", np.__version__)
        if not m or (int(m.group(1)), int(m.group(2))) < (1, 25):
            raise Refus("numpy ≥ 1.25 exigé (règle R9)")
        if tache not in CLES_TACHES:
            raise Refus(f"tâche {tache!r} absente de la table gelée")
        self.derivations.append({"racine": self.racine, "tache": tache, "cle": CLES_TACHES[tache]})
        return np.random.default_rng(np.random.SeedSequence(self.racine, spawn_key=(CLES_TACHES[tache],)))


# --- outils --------------------------------------------------------------------------------------------------------------


def _f(x):
    return ET._flottant(x)


def proportion(k, n) -> dict:
    return {"compte": int(k), "sur": int(n), "taux": (int(k) / int(n)) if n else None}


def tableaux_complets(ids, banque, par_temoin):
    """y ; tenté, vote, présent (verdict lisible) (n, 5) ; items rendus « faux » (n, 5, 5) ; un absent vaut rejet."""
    import numpy as np
    y, tente, vote = ET.tableaux(ids, banque, par_temoin)
    present = np.zeros_like(tente)
    items = np.zeros(tente.shape + (len(ET.ITEMS),), dtype=bool)
    for i, t in enumerate(ids):
        for c, (j, r, _b) in enumerate(ET.COLONNES):
            v = par_temoin[t][(j, r)]["verdict"]
            if v is not None:
                present[i, c] = True
                items[i, c] = [v["items"][k] for k in ET.ITEMS]
    return y, tente, vote, present, items


def classes_suffisantes(y) -> bool:
    """Au moins deux témoins de chaque classe : sans cela, ni la covariance intra-classes ni le rééchantillonnage
    stratifié ne sont définis ; la grandeur est « non mesurée », nommée, jamais un arrêt brut."""
    return int(y.sum()) >= 2 and int((~y).sum()) >= 2


def mot_ecart(point_defini: bool, lo, hi) -> str:
    """Texte l. 181 : « positif » si la borne basse dépasse 0 ; « nul ou négatif » si la borne haute est sous 0,10 et la
    borne basse ne dépasse pas 0 ; « indéterminé » sinon (et si l'estimation ou une borne est indéfinie)."""
    if not point_defini or lo is None or hi is None:
        return "indéterminé"
    if lo > 0:
        return "positif"
    if hi < BORNE_NUL_OU_NEGATIF and lo <= 0:
        return "nul ou négatif"
    return "indéterminé"


def mot_descriptif(ecart, lo, hi) -> str:
    """Comparaison descriptive (issue B) : écart = bras de comparaison moins agrégation étalonnée. Mots descriptifs
    seulement (texte l. 178, 180), aucun verdict."""
    if ecart is None or lo is None or hi is None:
        return "indéterminé"
    if ecart >= MARGE_COMPARAISON - EPS and lo > 0:
        return "C plus bas de la marge descriptive (écart ≥ 0,05, borne basse > 0) — descriptif, aucun verdict"
    if lo >= -MARGE_COMPARAISON and hi <= MARGE_COMPARAISON:
        return "équivalents dans ± 0,05 — descriptif, aucun verdict"
    if hi < 0:
        return "C plus haut (intervalle tout entier sous 0) — descriptif, aucun verdict"
    return "indéterminé — descriptif"


def bras_et_ecarts(banc, rng, err, y, noms, paires, B=TIRAGES) -> dict:
    """Taux de chaque bras (faux acceptés, vrais rejetés, erreur équilibrée) et écarts appariés (rééchantillonnage des
    comptes de configurations d'erreurs, stratifié par classe ; fonctions du banc v4)."""
    import numpy as np
    err = np.asarray(err, dtype=bool)
    A = err.shape[1]
    X = banc.motifs(A)
    cb = banc.comptes_configurations(err[None][:, y])
    cm = banc.comptes_configurations(err[None][:, ~y])
    nb, nm = int(y.sum()), int((~y).sum())
    fa = (cm[0] @ X) / nm
    vr = (cb[0] @ X) / nb
    ee = banc.ee_depuis_comptes(cb, cm, X, nb, nm)[0]
    db = banc.tirer_comptes(rng, cb, B)
    dm = banc.tirer_comptes(rng, cm, B)
    ee_b = banc.ee_depuis_comptes(db, dm, X, nb, nm)[:, 0, :]
    fa_b = ((dm.astype(float) @ X) / nm)[:, 0, :]
    vr_b = ((db.astype(float) @ X) / nb)[:, 0, :]
    taux = {n: {"faux_acceptes": float(fa[i]), "vrais_rejetes": float(vr[i]), "erreur_equilibree": float(ee[i])}
            for i, n in enumerate(noms)}
    ecarts = {}
    for nom, a, b in paires:
        i, j = noms.index(a), noms.index(b)
        out = {}
        for quoi, obs, boot in (("erreur_equilibree", ee, ee_b), ("faux_acceptes", fa, fa_b), ("vrais_rejetes", vr, vr_b)):
            lo, hi = banc._centiles(boot[:, i] - boot[:, j], 0)
            out[quoi] = {"ecart": float(obs[i] - obs[j]), "bas": _f(lo), "haut": _f(hi)}
        ecarts[nom] = out
    return {"temoins": int(y.size), "bons": nb, "mauvais": nm, "bras": taux, "ecarts": ecarts}


# --- lecture ---------------------------------------------------------------------------------------------------------------


def verifier_audit(audit, etalonnage_sha, banque_sha, rapport_sha) -> dict:
    if not isinstance(audit, dict) or audit.get("piece") != PIECE_AUDIT:
        raise Refus("audit de symétrie avant lecture : pièce d'une autre nature")
    if audit.get("etalonnage_sha256") != etalonnage_sha:
        raise Refus("audit de symétrie avant lecture : il ne cite pas l'empreinte de la pièce d'étalonnage scellée "
                    "(l'audit s'écrit après l'étalonnage, avant la lecture)")
    if audit.get("banque_sha256") != banque_sha or audit.get("rapport_execution_sha256") != rapport_sha:
        raise Refus("audit de symétrie avant lecture : banque ou rapport d'exécution d'une autre empreinte")
    c = audit.get("controles")
    if not isinstance(c, dict) or set(c) != set(CONTROLES_AUDIT):
        raise Refus("audit de symétrie avant lecture : les cinq contrôles de l. 350 ne sont pas tous écrits")
    non_tenus = [k for k in CONTROLES_AUDIT if c[k] != "tenu"]
    if non_tenus:
        raise Refus(f"audit de symétrie avant lecture : contrôle non tenu ({', '.join(non_tenus)}) : aucune lecture, la "
                    "mère est saisie")
    return {k: c[k] for k in CONTROLES_AUDIT}


def cout_apparie(journal_octets) -> dict:
    """Texte l. 291 : coût apparié vérifié après coup sur les coûts relevés au journal des appels (bloc A) ; k apparié =
    plus grand nombre impair de rendus du juge Argon dont le coût tient sous celui du collège, lu au plus proche parmi 1
    et 3. Coûts illisibles : k = 3, dit."""
    eng, reg = {}, {}
    for brut in journal_octets.decode("utf-8").splitlines():
        try:
            l = json.loads(brut)
        except ValueError:
            raise Refus("journal du compteur : ligne illisible") from None
        if l.get("type") == "engagement":
            eng[l.get("n")] = l
        elif l.get("type") == "reglement":
            reg[l.get("n")] = l
    couts = {j: [] for j in ET.JUGES}
    for n, l in reg.items():
        e = eng.get(n)
        if e is None or e.get("bloc") != "A" or e.get("juge") not in couts or not l.get("succes"):
            continue
        c = l.get("cout_releve")
        if isinstance(c, str):
            try:
                couts[e["juge"]].append(Fraction(c))
            except (ValueError, ZeroDivisionError):
                continue
    if not couts["juge-opus"] or not couts["juge-argon"]:
        return {"k_apparie": 3, "lu": False, "note": "coûts relevés illisibles au bloc A : k = 3 du texte, non vérifié"}
    c_o = sum(couts["juge-opus"]) / len(couts["juge-opus"])
    c_a = sum(couts["juge-argon"]) / len(couts["juge-argon"])
    rapport = (c_o + c_a) / c_a
    k = int(rapport)
    if k % 2 == 0:
        k -= 1
    k = max(k, 1)
    k_lu = 3 if k >= 3 else 1
    return {"k_apparie": k_lu, "lu": True, "k_impair_max": k, "cout_moyen_opus": str(c_o), "cout_moyen_argon": str(c_a),
            "rapport_cout_college_sur_argon": float(rapport),
            "note": ("k apparié égal au texte (3)" if k_lu == 3 else
                     "k apparié autre que 3 : bras R-Argon lu à k = 1 (texte l. 291), écart dit")}


def lire(banque, banque_sha, depot, execution, rapport_sha, etalonnage, etalonnage_sha, audit, audit_sha,
         mode="reel", autorisation=None, n_temoins=ET.N_TEMOINS, banc=None, tirages=TIRAGES) -> dict:
    import numpy as np
    graines = Graines(mode, autorisation)                     # refus avant toute dérivation et toute lecture
    depot = Path(depot)
    ET.garde_chemins([banque, depot, etalonnage, audit])
    etalonnage = Path(etalonnage)
    if etalonnage.name != ET.FICHIER_PIECE or etalonnage.parent.name != ET.SOUS_DOSSIER:
        raise Refus("étalonnage avant lecture : la pièce n'est pas DOSSIER/etalonnage/" + ET.FICHIER_PIECE)
    dossier = etalonnage.resolve().parent.parent
    sortie = dossier / SOUS_DOSSIER
    if (sortie / FICHIER_RAPPORT).exists():
        raise Refus("lecture unique : le rapport de lecture existe déjà : refus de rejouer")
    if sortie.exists():
        raise Refus("lecture unique : dossier de lecture déjà présent sans rapport : refus, la mère est saisie")
    if isinstance(execution, bool) or not isinstance(execution, int) or execution < 1:
        raise Refus("exécution : entier positif attendu")

    # Étalonnage scellé, audit de symétrie scellé : avant toute lecture d'un verdict.
    try:
        piece = ET.lire_json_scelle(etalonnage, etalonnage_sha, "pièce d'étalonnage")
        ET.lire_par_empreinte(etalonnage.parent / ET.FICHIER_MANIFESTE,
                              ET.sha256_fichier(etalonnage.parent / ET.FICHIER_MANIFESTE), "manifeste d'étalonnage")
    except (Refus, OSError) as e:
        raise Refus(f"étalonnage avant lecture : pièce absente, non scellée ou d'une autre empreinte ({e}) : refus de "
                    "lire") from None
    if piece.get("piece") != ET.PIECE or piece.get("banque_sha256") != banque_sha:
        raise Refus("étalonnage avant lecture : pièce d'une autre nature ou d'une autre banque")
    try:
        audit_obj = ET.lire_json_scelle(audit, audit_sha, "audit de symétrie")
    except Refus as e:
        raise Refus(f"audit de symétrie avant lecture : absent, non écrit ou non scellé ({e}) : refus de lire") from None

    # Rapport d'exécution du code d'appel, et dernière exécution.
    rapport_chemin = depot / f"rapport-execution-{execution}.json"
    rapport = ET.lire_json_scelle(rapport_chemin, rapport_sha, "rapport d'exécution")
    for nom in (f"rapport-execution-{execution + 1}.json", f"manifeste-execution-{execution + 1}.json"):
        if (depot / nom).exists():
            raise Refus("dépôt : une exécution plus récente que celle nommée existe : refus, la mère est saisie")
    if rapport.get("version") != ET.VERSION_CODE_APPEL or rapport.get("execution") != execution:
        raise Refus("rapport d'exécution : version ou exécution autre")
    controles_audit = verifier_audit(audit_obj, etalonnage_sha, banque_sha, rapport_sha)
    depots = rapport.get("depots") or {}
    nom_lec = f"verdicts-moitie-lecture-execution-{execution}.json"
    nom_cal = f"verdicts-moitie-etalonnage-execution-{execution}.json"
    nom_etat = f"etat-des-juges-execution-{execution}.json"
    for nom in (nom_lec, nom_cal, nom_etat):
        if not ET.est_empreinte(depots.get(nom)):
            raise Refus(f"rapport d'exécution : empreinte de {nom} absente")
    if piece.get("verdicts_etalonnage", {}).get("sha256") != depots[nom_cal] \
            or piece["verdicts_etalonnage"].get("fichier") != nom_cal:
        raise Refus("étalonnage avant lecture : la pièce ne porte pas les verdicts d'étalonnage de ce dépôt")
    if piece.get("banc_v4_sha256") != ET.BANC_V4[1]:
        raise Refus("étalonnage avant lecture : banc d'une autre empreinte")

    # Tout est ouvert, une seule fois.
    banc = banc if banc is not None else ET.charger_banc()
    bq = ET.lire_banque(banque, banque_sha, n_temoins)
    v_cal = ET.lire_verdicts_moitie(depot / nom_cal, depots[nom_cal], "etalonnage", bq)
    v_lec = ET.lire_verdicts_moitie(depot / nom_lec, depots[nom_lec], "lecture", bq)
    etat = ET.lire_json_scelle(depot / nom_etat, depots[nom_etat], "état des juges")
    journal_chemin = depot / "journal-compteur.jsonl"
    try:
        journal = journal_chemin.read_bytes()
    except OSError:
        raise Refus("journal du compteur absent") from None
    if ET.sha256_octets(journal) != rapport.get("journal_sha256"):
        raise Refus("journal du compteur d'une autre empreinte que celle du rapport d'exécution : refus")

    # Étalonnage recalculé : égal à la pièce scellée.
    recalc = ET.etalonner(bq, v_cal, banc)
    for cle in ("bras_C", "bras_P", "rho_etalonnage", "rho_etalonnage_indefini", "identifiants_lus"):
        if recalc[cle] != piece.get(cle):
            raise Refus(f"étalonnage avant lecture : {cle} recalculé différent de la pièce scellée : refus")

    par_temoin = dict(v_cal["par_temoin"])
    par_temoin.update(v_lec["par_temoin"])
    ids = sorted(par_temoin)
    y, tente, vote, present, items = tableaux_complets(ids, bq, par_temoin)
    moitie = np.array([bq[t]["moitie"] for t in ids])
    lec = moitie == "lecture"
    bloc_a = tente[:, 0] & tente[:, 1]
    complet = tente.all(axis=1)
    err = vote != y[:, None]
    r = {"version": VERSION, "issue_de_la_portee": ISSUE_PORTEE,
         "verdict_portee_200_v2_sha256": ET.VERDICT_PORTEE_200_V2_SHA256,
         "aide": "aide de lecture, jamais le verdict : le verdict est prononcé par un agent neuf (règle R13)",
         "regle_d_un_absent": "verdict absent : jamais « notable », compté comme rejet (« Métrique »)"}

    # Témoins et causes d'un rang 1.
    n_lec_complets = int((complet & lec).sum())
    r["temoins"] = {"banque": len(ids), "bloc_A_tentes": int(bloc_a.sum()),
                    "bloc_A_tentes_moitie_lecture": int((bloc_a & lec).sum()), "complets_cinq_rendus": int(complet.sum()),
                    "complets_moitie_lecture": n_lec_complets, "complets_moitie_etalonnage": int((complet & ~lec).sum()),
                    "seuil_complets_moitie_lecture": SEUIL_COMPLETS_LECTURE,
                    "definition_d_un_complet": "les cinq rendus tentés (verdict obtenu, lisible ou non, ou absent compté "
                                               "comme rejet)",
                    "complets_selon_le_rapport_d_execution": rapport.get("complets")}
    r["arret_du_code_d_appel"] = rapport.get("arret")
    mesures_r = n_lec_complets >= SEUIL_COMPLETS_LECTURE
    classes_r = classes_suffisantes(y[complet]) and classes_suffisantes(y[complet & lec])
    classes_a = classes_suffisantes(y[bloc_a]) and classes_suffisantes(y[bloc_a & lec])
    r["temoins"]["classes_suffisantes"] = {"bloc_A": classes_a, "complets": classes_r}

    # Par juge : erreurs du bloc A, absents, répétitions identiques.
    juges = {}
    for c, j in enumerate(ET.JUGES):
        ya = y[bloc_a]
        e = err[bloc_a, c]
        tentes_ab = int(tente[:, [k for k, col in enumerate(ET.COLONNES) if col[0] == j]].sum())
        cols = [k for k, col in enumerate(ET.COLONNES) if col[0] == j]
        absents = int((tente[:, cols] & ~present[:, cols]).sum())
        ej = etat.get(j) or {}
        if ej.get("absents") != absents or ej.get("rendus_tentes_A_et_B") != tentes_ab:
            raise Refus("appariement : l'état des juges du code d'appel diffère des verdicts déposés : refus")
        fa = int(e[~ya].sum())
        vr = int(e[ya].sum())
        juges[j] = {"taux_erreur_bloc_A": proportion(int(e.sum()), int(e.size)),
                    "faux_acceptes_bloc_A": proportion(fa, int((~ya).sum())),
                    "vrais_rejetes_bloc_A": proportion(vr, int(ya.sum())),
                    "erreur_equilibree_bloc_A": 0.5 * (fa / max(int((~ya).sum()), 1) + vr / max(int(ya.sum()), 1)),
                    "absents_A_et_B": proportion(absents, tentes_ab),
                    "non_mesure_absents": tentes_ab > 0 and Fraction(absents, tentes_ab) > SEUIL_ABSENTS,
                    "part_identique_a_l_octet": ej.get("part_identique"),
                    "rho_prime_non_mesure_repetitions_identiques": bool(ej.get("rho_prime_non_mesure")),
                    "sans_erreur_sur_le_bloc_A": int(e.sum()) == 0}
    r["juges"] = juges

    # ρ entre juges sur le bloc A, votes effectifs.
    Ea = err[bloc_a][:, :2]
    ya = y[bloc_a]
    rng_rho = graines.rng("rho_entre_juges_bloc_A")
    if classes_a:
        S = banc.cov_intra_classes(Ea[None].astype(float), ya)
        rho, indef = banc.rho_moyenne(S)
        lo, hi, n_ind = banc.intervalles_rho_moyenne(Ea[None], ya, rng_rho, tirages)
    else:
        rho, indef = np.array([np.nan]), np.array([True])
        lo, hi, n_ind = np.array([np.nan]), np.array([np.nan]), np.array([0])
    rho_v = None if bool(indef[0]) else _f(rho[0])
    demi = None if (_f(lo[0]) is None or _f(hi[0]) is None) else (float(hi[0]) - float(lo[0])) / 2.0
    r["rho_entre_juges_bloc_A"] = {"valeur": rho_v, "indefini": bool(indef[0]), "bas": _f(lo[0]), "haut": _f(hi[0]),
                                   "demi_largeur": demi, "tirages_indefinis": int(n_ind[0]),
                                   "votes_effectifs_bruts": _f(banc.votes_effectifs(rho, 2)[0]),
                                   "votes_effectifs_tronques": _f(banc.tronquer_votes(banc.votes_effectifs(rho, 2), 2)[0])}

    # ρ′ et ρ′ − ρ, sur les témoins complets (les deux moitiés).
    mots = {}
    if mesures_r and not classes_r:
        mesures_r = False
        mots = {j: "indéterminé" for j in ET.JUGES}
        r["rho_prime_et_ecarts"] = ("non mesurés : 40 témoins complets ou plus dans la moitié « lecture », mais moins de "
                                    "deux témoins complets d'une classe : covariance et rééchantillonnage stratifié non "
                                    "définis ; mots « indéterminé »")
    elif mesures_r:
        E4 = err[complet][:, :4]
        yc = y[complet]
        S4 = banc.cov_intra_classes(E4[None].astype(float), yc)
        r12, i12 = banc.rho_paire(S4, 0, 1)
        X = banc.motifs(4)
        cb = banc.comptes_configurations(E4[None][:, yc])
        cm = banc.comptes_configurations(E4[None][:, ~yc])
        rng = graines.rng("ecarts_rho_prime_moins_rho")
        Sb = banc.cov_depuis_comptes(banc.tirer_comptes(rng, cb, tirages), banc.tirer_comptes(rng, cm, tirages), X)
        r12b, _ = banc.rho_paire(Sb, 0, 1)
        lo12, hi12 = banc._centiles(r12b[:, 0], 0)
        sortie_rp = {"temoins_complets": int(complet.sum()),
                     "rho_entre_juges_complets": {"valeur": None if bool(i12[0]) else _f(r12[0]), "bas": _f(lo12),
                                                  "haut": _f(hi12)}}
        for j, (a, b) in zip(ET.JUGES, ((0, 2), (1, 3))):
            rp, ip = banc.rho_paire(S4, a, b)
            rpb, _ = banc.rho_paire(Sb, a, b)
            lo_p, hi_p = banc._centiles(rpb[:, 0], 0)
            lo_d, hi_d = banc._centiles(rpb[:, 0] - r12b[:, 0], 0)
            defini = not bool(ip[0]) and not bool(i12[0])
            m = mot_ecart(defini, _f(lo_d), _f(hi_d))
            if juges[j]["rho_prime_non_mesure_repetitions_identiques"]:
                m = "non mesuré (plus de la moitié de répétitions identiques à l'octet)"
            mots[j] = m
            sortie_rp[j] = {"rho_prime": None if bool(ip[0]) else _f(rp[0]), "rho_prime_bas": _f(lo_p),
                            "rho_prime_haut": _f(hi_p),
                            "rho_prime_moins_rho": (_f(rp[0] - r12[0]) if defini else None),
                            "bas": _f(lo_d), "haut": _f(hi_d), "mot": m}
        r["rho_prime_et_ecarts"] = sortie_rp
    else:
        r["rho_prime_et_ecarts"] = ("non mesurés : moins de 40 témoins complets dans la moitié « lecture » ; aucune valeur "
                                    "partielle n'est rapportée comme une estimation (l. 384)")

    # Bras de la moitié « lecture » (bloc A) : U, F, C, P, S-Opus, S-Argon.
    w_c = np.array([piece["bras_C"]["poids"]])
    s_c = np.array([piece["bras_C"]["seuil"]])
    w_p = np.array([piece["bras_P"]["poids"]])
    s_p = np.array([piece["bras_P"]["seuil"]])

    def notables(masque, avec_r=False, k_argon=3):
        V = vote[masque][:, :2]
        V_pm = 2.0 * V[None] - 1.0
        out = {"U": V.all(axis=1), "F": V.any(axis=1),
               "C": banc.appliquer_seuil(banc.score(V_pm, w_c), s_c, w_c)[0],
               "P": banc.appliquer_seuil(banc.score(V_pm, w_p), s_p, w_p)[0],
               "S_Opus": V[:, 0], "S_Argon": V[:, 1]}
        if avec_r:
            va = vote[masque]
            out["R_Argon"] = (va[:, [1, 3, 4]].sum(axis=1) >= 2) if k_argon == 3 else va[:, 1]
            out["R_Opus_2"] = va[:, 0] & va[:, 2]
        return out

    ma = bloc_a & lec
    paires_a = [("U_moins_C", "U", "C"), ("S_Opus_moins_C", "S_Opus", "C"), ("S_Argon_moins_C", "S_Argon", "C")]
    rng_a = graines.rng("comparaisons_bloc_A")
    cout = cout_apparie(journal)
    comparaisons = {}
    groupe_a = None
    if classes_a:
        na = notables(ma)
        noms_a = ("C", "U", "S_Opus", "S_Argon", "F", "P")
        err_a = np.stack([na[k] != y[ma] for k in noms_a], axis=1)
        groupe_a = bras_et_ecarts(banc, rng_a, err_a, y[ma], noms_a, paires_a, tirages)
        for nom, _a, _b in paires_a:
            e = groupe_a["ecarts"][nom]["erreur_equilibree"]
            comparaisons[nom] = dict(e, mot=mot_descriptif(e["ecart"], e["bas"], e["haut"]),
                                     par_classe={k: groupe_a["ecarts"][nom][k] for k in ("faux_acceptes",
                                                                                          "vrais_rejetes")})
        r["bras_moitie_lecture_bloc_A"] = {k: groupe_a[k] for k in ("temoins", "bons", "mauvais", "bras")}
    else:
        for nom, _a, _b in paires_a:
            comparaisons[nom] = "non mesurée : moins de deux témoins d'une classe au bloc A"
        r["bras_moitie_lecture_bloc_A"] = "non mesurés : moins de deux témoins d'une classe au bloc A"
    r["regles_choisies_a_l_etalonnage"] = {"C": piece["bras_C"]["regle_choisie"], "P": piece["bras_P"]["regle_choisie"],
                                           "C_repli_poids_egaux": piece["bras_C"]["repli_poids_egaux"]}
    r["cout_apparie"] = cout
    if mesures_r:
        mr = complet & lec
        nr = notables(mr, avec_r=True, k_argon=cout["k_apparie"])
        noms_r = ("C", "U", "F", "P", "R_Argon", "R_Opus_2")
        err_r = np.stack([nr[k] != y[mr] for k in noms_r], axis=1)
        paires_r = [("R_Argon_moins_C", "R_Argon", "C"), ("U_moins_R_Argon", "U", "R_Argon"),
                    ("F_moins_R_Argon", "F", "R_Argon")]
        groupe_r = bras_et_ecarts(banc, graines.rng("comparaisons_bras_R"), err_r, y[mr], noms_r, paires_r, tirages)
        e = groupe_r["ecarts"]["R_Argon_moins_C"]["erreur_equilibree"]
        comparaisons["R_Argon_moins_C"] = dict(e, mot=mot_descriptif(e["ecart"], e["bas"], e["haut"]),
                                               par_classe={k: groupe_r["ecarts"]["R_Argon_moins_C"][k]
                                                           for k in ("faux_acceptes", "vrais_rejetes")})
        r["bras_moitie_lecture_complets"] = {k: groupe_r[k] for k in ("temoins", "bons", "mauvais", "bras")}
        r["temoin_apparie"] = {k: dict(groupe_r["ecarts"][k], verdict="aucun (hors de Holm, sans verdict, l. 289)")
                               for k in ("U_moins_R_Argon", "F_moins_R_Argon")}
        b = groupe_r["bras"]
        r["critere_fa38f9faa24e0_descriptif"] = {
            "references": ["U", "R_Argon"],
            "mot": banc.mot_fa38(b["P"]["faux_acceptes"], b["P"]["vrais_rejetes"],
                                 [(b["U"]["faux_acceptes"], b["U"]["vrais_rejetes"]),
                                  (b["R_Argon"]["faux_acceptes"], b["R_Argon"]["vrais_rejetes"])]),
            "note": "lecture descriptive (l. 320), sur les témoins complets de la moitié « lecture »"}
    else:
        cause_r = ("moins de 40 témoins complets dans la moitié « lecture »" if n_lec_complets < SEUIL_COMPLETS_LECTURE
                   else "moins de deux témoins complets d'une classe")
        comparaisons["R_Argon_moins_C"] = f"non mesurée : bras R non mesurés ({cause_r})"
        r["bras_moitie_lecture_complets"] = f"non mesurés : {cause_r}"
        r["temoin_apparie"] = "non mesuré : bras R non mesurés"
        r["critere_fa38f9faa24e0_descriptif"] = "non lu : bras R non mesuré"
    r["comparaisons_d_agregations"] = {"statut": "descriptives (issue B) : aucun test de Holm, aucun « bat de la marge », "
                                                 "aucun « oui »", "ecart": "bras de comparaison moins agrégation étalonnée",
                                       "comparaisons": comparaisons}

    # Lecture par colonne (une colonne, deux lignes) : bloc A, les 200 témoins.
    err_col = err[bloc_a][:, :2]
    rng_col = graines.rng("lecture_par_colonne")
    col = (bras_et_ecarts(banc, rng_col, err_col, ya, ("S_Opus", "S_Argon"), [("Opus_moins_Argon", "S_Opus", "S_Argon")],
                          tirages) if classes_a else {"mesure": "non mesurée : moins de deux témoins d'une classe"})
    r["lecture_par_colonne"] = {"auteur": "une seule colonne (fragments écrits par un seul auteur) ; aucune lecture par "
                                          "ligne", "reference": "vérité plantée", **col}

    # Table par juge (pour le directeur seul).
    table = {}
    for c, j in enumerate(ET.JUGES):
        t = {"par_item": {}, "par_niveau": {}, "par_citation_bons": {}}
        for it in ET.ITEMS:
            m = bloc_a & (~y) & np.array([bq[x]["item"] == it for x in ids])
            t["par_item"][it] = {"faux_acceptes": proportion(int(vote[m, c].sum()), int(m.sum()))}
        for nv in ET.NIVEAUX:
            m = bloc_a & (~y) & np.array([bq[x]["niveau"] == nv for x in ids])
            t["par_niveau"][nv] = {"faux_acceptes": proportion(int(vote[m, c].sum()), int(m.sum()))}
        for cit in (True, False):
            m = bloc_a & y & np.array([bq[x]["citation"] == cit for x in ids])
            t["par_citation_bons"]["citants" if cit else "non_citants"] = {
                "vrais_rejetes": proportion(int((~vote[m, c]).sum()), int(m.sum()))}
        # Lecture seconde : sur un mauvais au verdict présent, l'item planté n'est pas rendu faux.
        m = bloc_a & (~y) & present[:, c]
        rate = 0
        for i in np.flatnonzero(m):
            rate += int(items[i, c, ET.ITEMS.index(bq[ids[i]]["item"])])
        t["lecture_seconde_item_plante_non_rendu_faux"] = proportion(rate, int(m.sum()))
        t["absents"] = juges[j]["absents_A_et_B"]
        rp = r["rho_prime_et_ecarts"]
        t["rho_prime"] = rp[j]["rho_prime"] if isinstance(rp, dict) else "non mesuré"
        table[j] = t
    r["table_par_juge"] = {"destinataire": "le directeur seul (réserve 3)", "par_juge": table}

    # H-sévérité (P9), descriptive.
    r["h_severite_descriptive"] = {
        j: {"vrais_rejetes_plus_que_faux_acceptes": (juges[j]["vrais_rejetes_bloc_A"]["taux"] or 0)
            > (juges[j]["faux_acceptes_bloc_A"]["taux"] or 0)} for j in ET.JUGES}
    if groupe_a is not None:
        bA = groupe_a["bras"]
        r["h_severite_descriptive"]["U_moins_meilleur_juge_seul_moitie_lecture"] = \
            bA["U"]["erreur_equilibree"] - min(bA["S_Opus"]["erreur_equilibree"], bA["S_Argon"]["erreur_equilibree"])

    # Stabilité : écart rapporté ; son seuil (étage 1) n'est pas lu, rang 2 inatteignable en issue B.
    ml = bloc_a & lec
    if classes_a:
        rl, il = banc.rho_moyenne(banc.cov_intra_classes(err[ml][None, :, :2].astype(float), y[ml]))
    else:
        rl, il = np.array([np.nan]), np.array([True])
    r["stabilite_de_l_etalonnage"] = {
        "rho_etalonnage": piece["rho_etalonnage"], "rho_moitie_lecture": None if bool(il[0]) else _f(rl[0]),
        "ecart_absolu": (None if piece["rho_etalonnage"] is None or bool(il[0])
                         else abs(piece["rho_etalonnage"] - float(rl[0]))),
        "seuil": "non lu : il ne sert qu'au rang 2, inatteignable en issue B"}

    # Audit de symétrie (R4) : déclencheurs, les mêmes dans les deux sens.
    trop_propre, trop_sale = [], []
    for j in ET.JUGES:
        if juges[j]["sans_erreur_sur_le_bloc_A"]:
            trop_propre.append(f"{j} : aucune erreur sur les témoins du bloc A")
        if juges[j]["erreur_equilibree_bloc_A"] > TROP_SALE_EE:
            trop_sale.append(f"{j} : erreur équilibrée au-dessus de 0,40")
        if juges[j]["non_mesure_absents"]:
            trop_sale.append(f"{j} : plus de 10 % de verdicts absents")
    if rho_v is not None:
        if abs(rho_v) < TROP_PROPRE_DISTANCE or abs(1.0 - rho_v) < TROP_PROPRE_DISTANCE:
            trop_propre.append("ρ entre juges à moins de 0,02 de 0 ou de 1")
        if rho_v < TROP_SALE_RHO:
            trop_sale.append("ρ entre juges négative au-delà de −0,2")
    if isinstance(r["rho_prime_et_ecarts"], dict):
        for j in ET.JUGES:
            rp = r["rho_prime_et_ecarts"][j]["rho_prime"]
            if rp is not None and abs(1.0 - rp) < TROP_PROPRE_DISTANCE:
                trop_propre.append(f"{j} : ρ′ à moins de 0,02 de 1")
    r["audit_de_symetrie"] = {"controles_ecrits_avant_la_lecture": controles_audit, "trop_propre": trop_propre,
                              "trop_sale": trop_sale, "sous_reserve": bool(trop_propre or trop_sale)}

    # Table de l'étage 2, issue B.
    causes = []
    for j in ET.JUGES:
        tx = Fraction(juges[j]["taux_erreur_bloc_A"]["compte"], max(juges[j]["taux_erreur_bloc_A"]["sur"], 1))
        if tx < TAUX_ERREUR_PRISE[0] or tx > TAUX_ERREUR_PRISE[1]:
            causes.append(f"banc sans prise : {j}, taux d'erreur hors de [0,05 ; 0,45]")
    if demi is None or demi > DEMI_LARGEUR_RHO_MAX:
        causes.append("banc sans prise : intervalle de ρ trop large (demi-largeur au-dessus de 0,25 ou indéfinie)")
    for j in ET.JUGES:
        if juges[j]["non_mesure_absents"]:
            causes.append(f"{j} non mesuré : plus de 10 % de verdicts absents")
        if juges[j]["rho_prime_non_mesure_repetitions_identiques"]:
            causes.append(f"{j} non mesuré : plus de la moitié de ses répétitions identiques à l'octet")
    manque = n_lec_complets < SEUIL_COMPLETS_LECTURE
    if manque:
        arret = rapport.get("arret") or {}
        cause_arret = str(arret.get("motif")) if arret else "aucun arrêt écrit"
        causes.append(f"moins de 40 témoins complets dans la moitié « lecture » ({n_lec_complets}) ; arrêt du code "
                      f"d'appel : {cause_arret}")
    if causes:
        rang, mot = 1, MOTS_TABLE["rang_1_manque" if manque else "rang_1"]
    elif any(m == "nul ou négatif" for m in mots.values()):
        rang, mot = 3, MOTS_TABLE["rang_3"]
    elif mots and all(m == "positif" for m in mots.values()):
        rang, mot = None, MOTS_TABLE["mesure_decorrele"]
    else:
        rang, mot = 5, MOTS_TABLE["rang_5"]
    if mot.strip().lower().startswith("oui") or OUI_POSSIBLE:
        raise ET.Refus("issue B : un « oui » ne peut pas être rendu (faute du programme)")
    r["table_de_lecture"] = {"issue_de_la_portee": ISSUE_PORTEE, "oui_possible": OUI_POSSIBLE,
                             "rangs_atteignables": [1, 3], "rang": rang, "mot": mot, "causes_du_rang_1": causes,
                             "mots_rho_prime_moins_rho": mots or "non mesurés",
                             "jamais": "« non concluant par manque de témoins » n'est jamais lu comme un « non »",
                             "sous_reserve_audit": r["audit_de_symetrie"]["sous_reserve"]}
    r["quel_que_soit_le_verdict"] = ("aucune carte n'est tranchée par un juge ; l'agrégation de la configuration ne change "
                                     "pas ; toute suite est une décision de Lazar (l. 345)")

    # Écriture et scellement.
    sortie.mkdir(parents=False, exist_ok=False)
    h = ET.ecrire_scelle(sortie / FICHIER_RAPPORT, r)
    configuration = {"banque": str(Path(banque).resolve()), "banque_sha256": banque_sha, "depot": str(depot.resolve()),
                     "execution": execution, "rapport_execution_sha256": rapport_sha,
                     "etalonnage": str(etalonnage.resolve()), "etalonnage_sha256": etalonnage_sha,
                     "audit": str(Path(audit).resolve()), "audit_sha256": audit_sha, "mode": graines.mode,
                     "n_temoins": n_temoins, "tirages": tirages}
    manifeste = {
        "version": VERSION, "horodatage_utc": ET.horodatage(), "programme_sha256": ET.sha256_fichier(Path(__file__)),
        "etalonner_sha256": ETALONNER[1], "banc_v4_sha256": ET.BANC_V4[1],
        "configuration": configuration, "configuration_sha256": ET.sha256_octets(ET.json_octets(configuration)),
        "versions": ET.versions(),
        "graines": {"racine": graines.racine, "cles": dict(CLES_TACHES), "regle": REGLE_DES_GRAINES,
                    "derivations": graines.derivations, "autorisation": graines.autorisation},
        "commits": {"depot_de_travail": ET.commit_du_depot()},
        "pieces_qui_font_foi": {"texte_v7": ET.TEXTE_V7_SHA256, "additif_3_v3": ET.ADDITIF_3_V3_SHA256,
                                "verdict_portee_200_v2": ET.VERDICT_PORTEE_200_V2_SHA256,
                                "code_d_appel_v4": ET.CODE_APPEL_V4_SHA256},
        "sorties": {FICHIER_RAPPORT: h}}
    ET.ecrire_scelle(sortie / FICHIER_MANIFESTE, manifeste)
    return {"rapport": r, "rapport_sha256": h, "manifeste": manifeste, "sortie": str(sortie)}


def principal(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    noms = ("--banque", "--banque-sha", "--depot", "--execution", "--rapport-execution-sha", "--etalonnage",
            "--etalonnage-sha", "--audit", "--audit-sha", "--autorisation-additif", "--empreinte-additif")
    try:
        inconnus = [a for a in argv[0::2] if a not in noms]
        if inconnus or len(argv) != 2 * len(noms):
            raise Refus("arguments : exactement " + " ".join(noms))
        a = {n: ET._argument(argv, n) for n in noms}
        if not a["--execution"].isdigit():
            raise Refus("--execution : entier positif attendu")
        res = lire(a["--banque"], a["--banque-sha"], a["--depot"], int(a["--execution"]), a["--rapport-execution-sha"],
                   a["--etalonnage"], a["--etalonnage-sha"], a["--audit"], a["--audit-sha"], mode="reel",
                   autorisation=(a["--autorisation-additif"], a["--empreinte-additif"]))
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 — arrêt nommé, sans trace brute
        print(json.dumps({"arret": type(e).__name__, "message": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps({"rapport": res["sortie"], "rapport_sha256": res["rapport_sha256"],
                      "mot": res["rapport"]["table_de_lecture"]["mot"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
