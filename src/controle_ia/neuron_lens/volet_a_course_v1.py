"""Assemblage de la course du volet A de « Neuron Lens » (Qwen3-8B) — v1.

Met en œuvre l'« ordre fixe de la course » du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`, Plan d'analyse A.1) : (1) empreintes vérifiées (addendum, partie 2,
écrite par l'appelant), (2) cas sains **avant toute lecture** des contrastes, (3) sondes et lectures, (4) rapport complet. Fonctions scellées
employées : `decisions_volet_a_v4.py` ; modules du premier lot : `volet_a_donnees_v1`, `volet_a_extraction_v1`, `volet_a_sondes_v1`,
`volet_a_lectures_v1`. Aucun code du dépôt voisin n'est importé : les lentilles sont lues comme des fichiers.

Lectures déclarées : la sonde « à étiquettes permutées » permute en respectant les groupes (`permuter_par_groupe`) ; la sonde sur composantes principales prend k plafonné au rang de l'apprentissage (min(k, n_app − 1, d) ; à
k = 512 sur 140 exemples d'apprentissage, k = 139), la valeur effective est rapportée ; l'A.5 (description jointe) rapporte les indices des 8 premiers neurones de chaque détecteur parcimonieux ; leurs
étiquettes et lectures du catalogue sont jointes au rapport après la course (sans critère) ; la lecture R (A.1, point 5) est rapportée
comme les 20 premiers jetons gardés. `exiger_cas_sains=False` n'existe que pour l'essai de fumée sur un modèle miniature : la sortie est
alors marquée « fumée » et ne vaut rien comme résultat.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np
from sklearn.metrics import roc_auc_score

from controle_ia.neuron_lens import decisions_volet_a_v4 as da
from controle_ia.neuron_lens import volet_a_donnees_v1 as vd
from controle_ia.neuron_lens import volet_a_extraction_v1 as ve
from controle_ia.neuron_lens import volet_a_lectures_v1 as vl
from controle_ia.neuron_lens import volet_a_sondes_v1 as vs

CONTRASTES = ("C3", "C1", "C2")  # C3 d'abord : sa direction sert de témoin à A1
EMPREINTE_KEPT = "cd8a6c236cb1bd4a9ed16bf7981104457ae5f1fea65fe16bb7d902aa86307ac7"


@dataclass
class Ressources:
    modele: object                 # Qwen3ForCausalLM (ou miniature pour la fumée)
    tok: object                    # tokenizers.Tokenizer de Qwen3-8B
    E: np.ndarray                  # plongements [V, d]
    U: np.ndarray                  # désenchâssement [V, d]
    gamma_final: np.ndarray        # poids de la norme finale [d]
    R: dict                        # couche → J_L (sortie de la couche → sortie de la dernière couche)
    S_out: dict                    # couche → K_L (plongements → sortie de la couche)
    S_mid: dict                    # couche → K_L (plongements → entrée de la couche à portes)
    gardes: np.ndarray             # identifiants gardés, triés
    owl: dict | None = None        # {"ecriture": W_down[:, 344] de la couche 8}
    german: dict | None = None     # {"porte", "montee", "gamma", "lobe_negatif"} du pôle L1 n11672 −
    appareil: str = "cpu"


def verifier_gardes(gardes, attendue=EMPREINTE_KEPT):
    txt = "".join(f"{int(i)}\n" for i in sorted(gardes)).encode()
    if hashlib.sha256(txt).hexdigest() != attendue:
        raise ValueError("liste des jetons gardés différente de l'addendum")


def lecture_r(res: Ressources, u, couche):
    """Logits de la lentille R d'un vecteur du flux : `W_U (γ ⊙ norm(J_L u))` (norme RMS de la colonne, ε = 1e-6), sur les gardés."""
    t = np.asarray(res.R[couche], float) @ np.asarray(u, float)
    t = t / np.sqrt(np.mean(t ** 2) + 1e-6) * res.gamma_final
    return (res.U[res.gardes] @ t)


def cas_sains(res: Ressources, lecteurs: dict) -> dict:
    dec = lambda i: res.tok.decode([int(i)])
    out = {}
    if res.owl is None or res.german is None:
        raise ValueError("pièces des cas sains (i) et (ii) absentes")
    out["i_owl"] = vl.cas_sain_owl(lecture_r(res, res.owl["ecriture"], 8), res.gardes, dec)
    c = vl.direction_lecture(res.german["porte"], res.german["montee"], res.german["gamma"], -1, res.german["lobe_negatif"])
    s_brute = da.empreintes(res.E, res.gardes, res.S_mid[1]) @ c
    out["ii_german"] = vl.cas_sain_german(s_brute, res.gardes, dec)
    pos_v0 = int(np.searchsorted(res.gardes, vd.V0_CAS_SAIN))
    if res.gardes[pos_v0] != vd.V0_CAS_SAIN:
        raise ValueError("« Ġworld » absent des jetons gardés : arrêt")
    out["iii_synthetique"] = {l: vl.cas_sain_synthetique(lecteurs[l], pos_v0) for l in lecteurs}
    ok = out["i_owl"][0] and out["ii_german"][0] and all(all(v) for v in out["iii_synthetique"].values())
    out["tous_passes"] = bool(ok)
    return out


class Extracteur:
    """Passes du modèle avec cache par suite d'identifiants (les invites identiques ne repassent pas)."""

    def __init__(self, res: Ressources):
        self.res, self.cache = res, {}

    def __call__(self, listes_ids, positions):
        manquants = [(tuple(x), p) for x, p in zip(listes_ids, positions) if tuple(x) not in self.cache]
        uniques = list(dict.fromkeys(manquants))
        if uniques:
            r, n = ve.extraire(self.res.modele, [list(x) for x, _ in uniques], [p for _, p in uniques], vd.COUCHES,
                               appareil=self.res.appareil)
            for i, (x, _) in enumerate(uniques):
                self.cache[x] = ({l: r[l][i] for l in vd.COUCHES}, {l: n[l][i] for l in vd.COUCHES})
        sel = [self.cache[tuple(x)] for x in listes_ids]
        return ({l: np.stack([s[0][l] for s in sel]) for l in vd.COUCHES}, {l: np.stack([s[1][l] for s in sel]) for l in vd.COUCHES})


def permuter_par_groupe(y, g, graine):
    """Étiquettes permutées en respectant les groupes (lecture déclarée) : dans un groupe qui contient les deux classes (paires de C1,
    énoncés de C2), les étiquettes sont échangées avec probabilité 1/2 ; les groupes d'une seule classe (C3) voient leurs étiquettes
    permutées entre eux. Chaque groupe garde ainsi sa composition, et les plis internes groupés gardent les deux classes."""
    rng = np.random.default_rng(graine)
    y = np.asarray(y).copy()
    g = np.asarray(g)
    mixtes, simples = [], []
    for gg in dict.fromkeys(g.tolist()):
        idx = np.flatnonzero(g == gg)
        (mixtes if len(set(y[idx])) > 1 else simples).append(idx)
    for idx in mixtes:
        if rng.random() < 0.5:
            y[idx] = 1 - y[idx]
    if simples:
        lab = np.array([y[idx[0]] for idx in simples])
        lab = lab[rng.permutation(len(lab))]
        for idx, v in zip(simples, lab):
            y[idx] = v
    return y


def _rendre(res, exemples):
    rendus = [vd.rendre(res.tok, e.texte) for e in exemples]
    return [r[0] for r in rendus], [r[1] for r in rendus]


def _texte(ids, debut):
    return ids[debut:-2]  # sans préfixe, préambule ni marques de fin de tour (2 jetons)


def _retirer_dans_invite(ids, debut, jetons):
    t = vl.retirer(_texte(ids, debut), jetons)
    if not t:
        return None
    nouvelle = list(ids[:debut]) + t + list(ids[-2:])
    return nouvelle, len(nouvelle) - 3


def _auc(y, s):
    return float(roc_auc_score(y, s))


def courir(res: Ressources, graines: vd.Graines | None = None, limite: int | None = None, exiger_cas_sains: bool = True,
           n_tirages_a3: int = 200, n_tirages_hasard: int = 20, n_reechantillonnage: int = 2000):
    """Course complète du volet A. `limite`, `exiger_cas_sains=False` et des nombres de tirages réduits ne servent qu'à la fumée."""
    fumee = (limite is not None) or (not exiger_cas_sains) or n_tirages_a3 != 200 or n_tirages_hasard != 20 \
        or n_reechantillonnage != 2000
    graines = graines or vd.arbre_de_graines()
    verifier_gardes(res.gardes) if not fumee else None
    debut = vd.debut_du_texte(res.tok)
    lecteurs = {l: vl.LecteurCouche.construire(res.E, res.gardes, res.S_out[l], graines.references_par_couche[l]) for l in vd.COUCHES}
    sortie = {"fumee": fumee, "cas_sains": cas_sains(res, lecteurs)}
    if exiger_cas_sains and not sortie["cas_sains"]["tous_passes"]:
        sortie["verdict_i"] = "chaîne en défaut"
        return sortie
    idx_P = np.searchsorted(res.gardes, vd.P_PLANTES)
    if not np.all(res.gardes[idx_P] == np.array(vd.P_PLANTES)):
        raise ValueError("P n'a pas tous ses jetons parmi les gardés : arrêt")
    ext = Extracteur(res)
    pos_gardes = {int(g): i for i, g in enumerate(res.gardes)}
    brut = {}  # contraste → découpe → couche → mesures
    sondes_c3 = {}
    for c in CONTRASTES:
        ex = vd.charger(c)
        if limite:  # fumée : les `limite // 2` premiers groupes de chaque classe (les deux classes restent présentes)
            garde_g = set()
            for cl in (0, 1):
                garde_g |= set(sorted({e.groupe for e in ex if e.classe == cl})[:limite // 2])
            ex = [e for e in ex if e.groupe in garde_g]
        ids, pos = _rendre(res, ex)
        y = np.array([e.classe for e in ex])
        g = np.array([e.groupe for e in ex])
        R_all, N_all = ext(ids, pos)
        brut[c] = []
        for d in range(vd.N_DECOUPES):
            gr = graines.decoupes[c][d]
            app, tst = vd.decoupe(ex, gr["permutation"])
            ood_ex = vd.hors_distribution(c, {ex[i].groupe for i in tst}, [ex[i] for i in tst])
            if limite and c == "C1":
                ood_ex = [e for e in ood_ex if e.classe == 0] + [e for e in ood_ex if e.classe == 1][:limite]
            if ood_ex:
                ids_o, pos_o = _rendre(res, ood_ex)
                R_o, N_o = ext(ids_o, pos_o)
                y_o = np.array([e.classe for e in ood_ex])
            textes_app = [_texte(ids[i], debut) for i in app]
            sac = vs.apprendre_sac(textes_app, y[app], g[app])
            freq = {}
            for t in textes_app:
                for j in set(t):
                    freq[j] = freq.get(j, 0) + 1
            poids_g = np.array([sac.poids_par_jeton().get(int(t), 0.0) for t in res.gardes])
            presents = np.array([freq.get(int(t), 0) >= 2 for t in res.gardes])
            y_perm = permuter_par_groupe(y[app], g[app], gr["permutees"])
            par_couche = {}
            for l in vd.COUCHES:
                s = vs.apprendre_sonde(R_all[l][app], y[app], g[app])
                w = da.ramener_au_flux(s.w_std, s.sigma)
                if c == "C3":
                    sondes_c3[(d, l)] = w
                sp = vs.apprendre_sonde(R_all[l][app], y_perm, g[app])
                w_perm = da.ramener_au_flux(sp.w_std, sp.sigma)
                m = {"C_sonde": s.C, "auc_sonde_id": _auc(y[tst], s.scores(R_all[l][tst])),
                     "auc_sac_id": _auc(y[tst], sac.scores([_texte(ids[i], debut) for i in tst]))}
                if ood_ex:
                    m["auc_sonde_ood"] = _auc(y_o, s.scores(R_o[l]))
                    m["auc_sac_ood"] = _auc(y_o, sac.scores([_texte(x, debut) for x in ids_o]))
                    m["scores_sonde_ood"] = s.scores(R_o[l]).tolist()
                    m["y_ood"] = y_o.tolist()
                m["scores_sonde_id"] = s.scores(R_all[l][tst]).tolist()
                m["y_id"] = y[tst].tolist()
                lec = lecteurs[l]
                U_alea = vl.directions_aleatoires(len(w), gr["directions"][l])
                if c == "C2":
                    m["a1"] = vl.mesure_a1(lec, idx_P, w, U_alea, w_perm, sondes_c3[(d, l)])
                if c == "C1":
                    m["a2"] = vl.mesure_a2(lec, w, poids_g, presents, U_alea)
                if c in ("C1", "C2"):
                    m["a3"] = _mesure_a3(res, ext, s, l, lec, w, ids, tst, y, debut, freq, sac, gr["tirages_a3"], n_tirages_a3)
                m["lecture_r_difference"] = [int(res.gardes[i]) for i in np.argsort(
                    -lecture_r(res, R_all[l][app][y[app] == 1].mean(0) - R_all[l][app][y[app] == 0].mean(0), l))[:20]]
                m["lecture_r_poids"] = [int(res.gardes[i]) for i in np.argsort(-lecture_r(res, w, l))[:20]]
                m["aii"] = _mesure_aii(N_all[l][app], y[app], g[app], N_all[l][tst], N_o[l] if ood_ex else None,
                                       R_all[l][app], R_all[l][tst], R_o[l] if ood_ex else None, gr["neurones_aleatoires"],
                                       n_tirages_hasard, y_test=y[tst], y_ood=y_o if ood_ex else None)
                par_couche[l] = m
            brut[c].append(par_couche)
        sortie[f"longueur_{c}"] = _auc(y, [len(_texte(x, debut)) for x in ids])
    sortie["mesures"] = brut
    sortie.update(_decider(brut, graines, n_reechantillonnage))
    return sortie


def _mesure_a3(res, ext, sonde, l, lec, w, ids, tst, y, debut, freq, sac, graine, n_tirages):
    """Chutes d'AUROC de la sonde (non réapprise) sur le test après retrait des 20 jetons S, de 200 tirages appariés, des 20 jetons du sac."""
    base = _auc(y[tst], sonde.scores(ext([ids[i] for i in tst], [len(ids[i]) - 3 for i in tst])[0][l]))

    def chute(jetons):
        nouv, ys, ecartes = [], [], 0
        for i in tst:
            r = _retirer_dans_invite(ids[i], debut, jetons)
            if r is None:
                ecartes += 1
                continue
            nouv.append(r)
            ys.append(y[i])
        if len(set(ys)) < 2:
            return float("nan"), ecartes
        Rn, _ = ext([x for x, _ in nouv], [p for _, p in nouv])
        return base - _auc(np.array(ys), sonde.scores(Rn[l])), ecartes

    jet_s = vl.jetons_a3(lec, w, res.gardes)
    chute_s, ec_s = chute(jet_s)
    tir = vl.tirages_apparies_a3(jet_s, freq, res.gardes, graine, n=n_tirages)
    chutes_al = [chute(t)[0] for t in tir]
    pos, neg = sac.premiers()
    chute_sac, _ = chute(pos + neg)
    presents_test = sum(any(j in set(_texte(ids[i], debut)) for i in tst) for j in jet_s)
    return {"chute_s": chute_s, "chutes_aleatoires": chutes_al, "chute_sac": chute_sac, "jetons_s": jet_s,
            "jetons_s_presents_test": int(presents_test), "exemples_ecartes": ec_s, "n_jetons_sac": len(pos) + len(neg)}


def _mesure_aii(N_app, y_app, g_app, N_tst, N_ood, R_app, R_tst, R_ood, graine, n_tirages, y_test, y_ood):
    jeux = {"id": N_tst} | ({"ood": N_ood} if N_ood is not None else {})
    det = vs.detecteurs(N_app, y_app, g_app, jeux, graine, n_tirages)
    out = {"id": {}, "ood": {}}
    for nom, yy in (("id", y_test), ("ood", y_ood)):
        if nom not in det:
            continue
        for k, s in det[nom].items():
            out[nom][k] = float(np.mean([_auc(yy, x) for x in s])) if isinstance(s, list) else _auc(yy, s)
        out[nom + "_scores"] = {f"k{k}": det[nom][f"k{k}"].tolist() for k in vs.BUDGETS}
    out["pca_k_effectif"] = {}
    for k in vs.BUDGETS:
        k_eff = min(k, R_app.shape[0] - 1, R_app.shape[1])  # lecture déclarée : k plafonné au rang de l'apprentissage
        out["pca_k_effectif"][k] = k_eff
        comp = vs.composantes(R_app, y_app, g_app, {"id": R_tst} | ({"ood": R_ood} if R_ood is not None else {}), k_eff)
        out["id"][f"pca{k}"] = _auc(y_test, comp["id"])
        if R_ood is not None:
            out["ood"][f"pca{k}"] = _auc(y_ood, comp["ood"])
    ems = vs.ecart_moyen_standardise(N_app, y_app)
    out["huit_premiers_neurones"] = [int(i) for i in np.argsort(-ems, kind="stable")[:8]]
    return out


def _decider(brut, graines, n_reech):
    """Agrégation par couche sur les 5 découpes et application des règles scellées (`decisions_volet_a_v4`)."""
    L = vd.COUCHES
    dec = {}
    # A1 (C2)
    cl_a1 = [da.regle_couche([brut["C2"][d][l]["a1"]["condition"] for d in range(5)]) for l in L]
    a1 = da.verdict_a1(cl_a1)
    mieux_a1 = [[brut["C2"][d][l]["a1"]["rang_s"] < brut["C2"][d][l]["a1"]["rang_sans_lentille"] for d in range(5)] for l in L]
    # A2 (C1)
    a2_so = da.a2_sans_objet(float(np.mean([brut["C1"][d][l]["auc_sac_id"] for d in range(5) for l in L[:1]])))
    cl_a2 = [da.regle_couche([brut["C1"][d][l]["a2"]["condition"] for d in range(5)]) for l in L]
    mieux_a2 = [[brut["C1"][d][l]["a2"]["s_mieux_a2"] for d in range(5)] for l in L]
    # A3 (C1, C2)
    a3 = []
    for c in ("C1", "C2"):
        pc = []
        for l in L:
            ms = [brut[c][d][l]["a3"] for d in range(5)]
            pc.append({"chutes_sac": [m["chute_sac"] for m in ms],
                       "conditions": [da.condition_a3(m["chute_s"], m["chutes_aleatoires"], m["chute_sac"]) for m in ms],
                       "moins_que_moitie": [da.moins_que_moitie(m["chute_s"], m["chute_sac"]) for m in ms]})
        a3.append(da.verdict_a3(pc))
    dec["a1"], dec["a2_sans_objet"], dec["a3"] = a1, a2_so, a3
    dec["classes_a1"], dec["classes_a2"] = cl_a1, cl_a2
    dec["verdict_i"] = da.verdict_i(False, a1, da.sans_lentille_au_moins_partout(mieux_a1), da.sans_lentille_au_moins_partout(mieux_a2),
                                    a2_so, a3, da.s_fait_mieux(mieux_a1, cl_a1), da.s_fait_mieux(mieux_a2, cl_a2))
    # A-ii, par contraste
    aii = {}
    for c in ("C1", "C2", "C3"):
        ood = c != "C3"
        couches = []
        for l in L:
            ms = [brut[c][d][l] for d in range(5)]
            ent = {"sonde_id": float(np.mean([m["auc_sonde_id"] for m in ms])),
                   "neurones_id": {k: float(np.mean([m["aii"]["id"][f"k{k}"] for m in ms])) for k in vs.BUDGETS}}
            if ood:
                ent["sonde_ood"] = float(np.mean([m["auc_sonde_ood"] for m in ms]))
                ent["neurones_ood"] = {k: float(np.mean([m["aii"]["ood"][f"k{k}"] for m in ms])) for k in vs.BUDGETS}
                ent["borne_basse_ood"] = {}
                for k in vs.BUDGETS:
                    _, bas, _ = vs.borne_basse_appariee([m["aii"]["ood_scores"][f"k{k}"] for m in ms], [m["scores_sonde_ood"] for m in ms],
                                                        [m["y_ood"] for m in ms], graines.decoupes[c][0]["reechantillonnage"], n=n_reech)
                    ent["borne_basse_ood"][k] = bas
            couches.append(ent)
        v = da.verdict_aii(couches, a_un_hors_distribution=ood)
        partie = "ood" if ood else "id"
        meilleur = max(float(np.mean([brut[c][d][l]["aii"][partie][f"k{k}"] for d in range(5)])) for l in L for k in (1, 8, 64))
        sac = max(float(np.mean([brut[c][d][l][f"auc_sac_{partie}"] for d in range(5)])) for l in L)
        aii[c] = {"verdict": v, "qualificatif": da.qualificatif_texte(meilleur, sac, c), "couches": couches}
    dec["aii"] = aii
    rangs_med = [float(np.median([brut["C2"][d][l]["a1"]["rang_s"] for d in range(5)])) for l in L]
    egaux = da.neurones_egaux_partout(
        [max(float(np.mean([brut[c][d][l]["aii"]["id"][f"k{k}"] for d in range(5)])) for k in (1, 8, 64)) for c in aii for l in L],
        [float(np.mean([brut[c][d][l]["auc_sonde_id"] for d in range(5)])) for c in aii for l in L])
    dec["audit"] = da.audit_volet_a(rangs_med, egaux, a1, aii["C1"]["verdict"], aii["C3"]["verdict"])
    dec["verdict_i_affiche"] = da.en_attente(dec["verdict_i"], dec["audit"])
    return dec
