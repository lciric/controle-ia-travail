"""Assemblage de la course du volet A de « Neuron Lens » (Qwen3-8B) — v3 (remplace la v2 après sa contre-lecture,
`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-2-code-volet-a-lot1-v2-et-assemblage.md`, remarques 1 à 10 ; modules
`volet_a_sondes_v2`, `volet_a_lectures_v2`, `volet_a_donnees_v1`, `volet_a_extraction_v1` inchangés).

Met en œuvre l'« ordre fixe de la course » du texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md`
(`34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131`, Plan d'analyse A.1) : (1) empreintes vérifiées (addendum, partie 2,
écrite par l'appelant), (2) cas sains **avant toute lecture** des contrastes, (3) sondes et lectures, (4) rapport complet. Fonctions scellées
employées : `decisions_volet_a_v4.py` ; modules du premier lot : `volet_a_donnees_v1`, `volet_a_extraction_v1`, `volet_a_sondes_v2`,
`volet_a_lectures_v2`. Aucun code du dépôt voisin n'est importé : les lentilles sont lues comme des fichiers.

Lectures déclarées : la sonde « à étiquettes permutées » permute en respectant les groupes (`permuter_par_groupe`) ; la sonde sur composantes principales prend k plafonné au rang de l'apprentissage (min(k, n_app − 1, d) ; à
k = 512 sur 140 exemples d'apprentissage, k = 139), la valeur effective est rapportée ; l'A.5 (description jointe) rapporte les indices des 8 premiers neurones de chaque détecteur parcimonieux ; leurs
étiquettes et lectures du catalogue sont jointes au rapport après la course (sans critère) ; la lecture R (A.1, point 5) est rapportée
comme les 20 premiers jetons gardés. `exiger_cas_sains=False` n'existe que pour l'essai de fumée sur un modèle miniature : la sortie est
alors marquée « fumée » et ne vaut rien comme résultat.

Graines (v2) : chaque découpe emploie ses propres graines « permutées », « directions » (une par couche), « tirages_a3 », « neurones
aléatoires » (commune à ses couches et budgets) et « rééchantillonnage » ; l'intervalle apparié de A-ii reçoit les 5 graines
« rééchantillonnage » des 5 découpes du contraste, une par découpe. A2 rapporte en plus, hors condition, les ρ des témoins « sonde
permutée » et « direction de C3 » (C3 court en premier). Le nombre d'avertissements de convergence de la régression logistique est
rendu (`avertissements_convergence`) pour le manifeste.

Ajouts v3 (lectures déclarées) :
- A3 : les passes après retrait n'extraient que le flux de la couche lue, sans cache (seules les invites d'origine sont gardées en
  cache) ; la chute est `AUROC(sonde, invites d'origine) − AUROC(sonde, invites après retrait)` **sur les mêmes exemples** (ceux dont
  le texte n'est pas vidé par le retrait ; leur nombre est rapporté) ; une AUROC non calculable (une seule classe restante) donne NaN,
  que les règles scellées refusent : la course s'arrête alors, mais les mesures brutes sont déjà écrites ;
- mesures brutes rendues à l'appelant **par contraste, dès qu'il est fini, et avant les décisions** (`ecrire_brut`), pour être scellées ;
- mémoire : la lecture sans lentille `W_E[v] − m` ne dépend pas de la couche ; une seule matrice est construite et partagée par les
  quatre lecteurs (statistiques de référence propres à chaque couche, avec sa graine) ; mémoire vive minimale déclarée : 64 Go ;
  `W_U` restreint aux gardés calculé une fois ; tris stables ;
- P : les quatre jetons doivent être parmi les gardés (plus strict que « P sans jeton parmi les gardés » ; l'addendum les y a vus) ;
  gardés strictement croissants exigés ;
- la sonde à étiquettes permutées n'est apprise que pour C1 et C2 (témoins de A2 et A1) ; le témoin « direction de C3 » d'une
  découpe d est la sonde de C3 de la découpe de même rang d, à la même couche ;
- la sonde sur composantes principales centre-réduit les composantes avant la régression (« traits centrés-réduits ») ;
- cas sains (i) et (ii) : les 10 premiers sur le **vocabulaire entier** sont rapportés à côté (pour (ii), centrage par la moyenne des
  gardés, comme pour la lecture) ;
- audit R4 « trop beau » (déclencheur des règles scellées) joué dans la même course, rapporté, sans changer les règles : (a) sixième
  découpe de chaque contraste, graine = enfant d'indice 5 de la graine du contraste (`spawn(6)[5]` : « graine suivante »), mesures
  complètes ; (b) retrait vérifié sur le texte : aucun jeton retiré ne reste dans une invite après retrait ; (c) « direction permutée
  sans P » lue ainsi : à chaque découpe de C2 et couche, sonde réapprise sur les invites de C2 **dont les jetons de P sont retirés**
  (sans nouvelle tokenisation), et rang de P de sa direction (deux signes) — lecture à confirmer par la mère avant tout usage.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass

import numpy as np
from sklearn.metrics import roc_auc_score

from controle_ia.neuron_lens import decisions_volet_a_v4 as da
from controle_ia.neuron_lens import volet_a_donnees_v1 as vd
from controle_ia.neuron_lens import volet_a_extraction_v1 as ve
from controle_ia.neuron_lens import volet_a_lectures_v2 as vl
from controle_ia.neuron_lens import volet_a_sondes_v2 as vs

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


def _r_transporte(res: Ressources, u, couche):
    t = np.asarray(res.R[couche], float) @ np.asarray(u, float)
    return t / np.sqrt(np.mean(t ** 2) + 1e-6) * res.gamma_final


def lecture_r(res: Ressources, u, couche, vocabulaire_entier=False):
    """Logits de la lentille R d'un vecteur du flux : `W_U (γ ⊙ norm(J_L u))` (norme RMS de la colonne, ε = 1e-6), sur les gardés
    (`W_U` restreint aux gardés calculé une fois) ou sur le vocabulaire entier."""
    t = _r_transporte(res, u, couche)
    if vocabulaire_entier:
        return res.U @ t
    if getattr(res, "_U_g", None) is None:
        res._U_g = np.asarray(res.U[res.gardes])
    return res._U_g @ t


def _premiers(res, scores, k=10, gardes=True):
    o = np.argsort(-np.asarray(scores), kind="stable")[:k]
    ids = res.gardes[o] if gardes else o
    return [[int(i), res.tok.decode([int(i)])] for i in ids]


def cas_sains(res: Ressources, lecteurs: dict) -> dict:
    dec = lambda i: res.tok.decode([int(i)])
    out = {}
    if res.owl is None or res.german is None:
        raise ValueError("pièces des cas sains (i) et (ii) absentes")
    out["i_owl"] = vl.cas_sain_owl(lecture_r(res, res.owl["ecriture"], 8), res.gardes, dec)
    out["i_owl_vocabulaire_entier"] = _premiers(res, lecture_r(res, res.owl["ecriture"], 8, vocabulaire_entier=True), gardes=False)
    c = vl.direction_lecture(res.german["porte"], res.german["montee"], res.german["gamma"], -1, res.german["lobe_negatif"])
    s_brute = da.empreintes(res.E, res.gardes, res.S_mid[1]) @ c
    out["ii_german"] = vl.cas_sain_german(s_brute, res.gardes, dec)
    m = np.asarray(res.E, dtype=np.float64)[res.gardes].mean(0)
    s_tout = (np.asarray(res.E, dtype=np.float64) - m) @ (np.asarray(res.S_mid[1], dtype=np.float64).T @ c)
    out["ii_german_vocabulaire_entier"] = _premiers(res, s_tout, gardes=False)
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

    def flux(self, listes_ids, positions, couche):
        """Flux de la seule couche `couche`, sans cache (passes de A3 après retrait)."""
        if not listes_ids:
            return np.zeros((0, 0))
        r, _ = ve.extraire(self.res.modele, [list(x) for x in listes_ids], list(positions), [couche], appareil=self.res.appareil)
        return r[couche]


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


def construire_lecteurs(res: Ressources, graines: vd.Graines):
    """Quatre lecteurs ; la matrice sans lentille (`W_E[v] − m`) est construite une fois et partagée (lecture déclarée v3)."""
    F_0 = da.empreintes(res.E, res.gardes, None)
    out = {}
    for l in vd.COUCHES:
        F_s = da.empreintes(res.E, res.gardes, res.S_out[l])
        g = graines.references_par_couche[l]
        out[l] = vl.LecteurCouche(F_s, F_0, da.stats_reference(F_s, g), da.stats_reference(F_0, g))
    return out


def _restreindre(ex, limite):
    garde_g = set()
    for cl in (0, 1):
        garde_g |= set(sorted({e.groupe for e in ex if e.classe == cl})[:limite // 2])
    return [e for e in ex if e.groupe in garde_g]


def courir(res: Ressources, graines: vd.Graines | None = None, limite: int | None = None, exiger_cas_sains: bool = True,
           n_tirages_a3: int = 200, n_tirages_hasard: int = 20, n_reechantillonnage: int = 2000, ecrire_brut=None,
           forcer_audit: bool = False):
    """Course complète du volet A. `limite`, `exiger_cas_sains=False`, des nombres de tirages réduits et `forcer_audit` ne servent
    qu'à la fumée. `ecrire_brut(nom, contenu)` : appelé avec les mesures de chaque contraste dès qu'il est fini, avant les décisions."""
    fumee = (limite is not None) or (not exiger_cas_sains) or n_tirages_a3 != 200 or n_tirages_hasard != 20 \
        or n_reechantillonnage != 2000 or forcer_audit
    graines = graines or vd.arbre_de_graines()
    vs.AVERTISSEMENTS["convergence"] = 0
    res.gardes = np.asarray(res.gardes)
    if not np.all(np.diff(res.gardes) > 0):
        raise ValueError("jetons gardés non strictement croissants : arrêt")
    verifier_gardes(res.gardes) if not fumee else None
    ecrire_brut = ecrire_brut or (lambda nom, contenu: None)
    lecteurs = construire_lecteurs(res, graines)
    sortie = {"fumee": fumee, "cas_sains": cas_sains(res, lecteurs)}
    ecrire_brut("cas-sains", sortie["cas_sains"])
    if exiger_cas_sains and not sortie["cas_sains"]["tous_passes"]:
        sortie["verdict_i"] = "chaîne en défaut"
        return sortie
    idx_P = np.searchsorted(res.gardes, vd.P_PLANTES)
    if np.any(idx_P >= len(res.gardes)) or not np.all(res.gardes[np.minimum(idx_P, len(res.gardes) - 1)] == np.array(vd.P_PLANTES)):
        raise ValueError("P n'a pas tous ses jetons parmi les gardés : arrêt")
    ctx = {"res": res, "ext": Extracteur(res), "lecteurs": lecteurs, "idx_P": idx_P, "debut": vd.debut_du_texte(res.tok),
           "sondes_c3": {}, "limite": limite, "n_tirages_a3": n_tirages_a3, "n_tirages_hasard": n_tirages_hasard}
    brut, jeux = {}, {}
    for c in CONTRASTES:
        ex = vd.charger(c)
        if limite:  # fumée : les `limite // 2` premiers groupes de chaque classe
            ex = _restreindre(ex, limite)
        jeux[c] = ex
        brut[c] = [_mesurer_decoupe(ctx, c, ex, d, graines.decoupes[c][d]) for d in range(vd.N_DECOUPES)]
        ids, _ = _rendre(res, ex)
        sortie[f"longueur_{c}"] = _auc([e.classe for e in ex], [len(_texte(x, ctx["debut"])) for x in ids])
        ecrire_brut(f"mesures-{c}", {"decoupes": brut[c], "longueur": sortie[f"longueur_{c}"]})
    sortie["mesures"] = brut
    sortie.update(_decider(brut, graines, n_reechantillonnage))
    if "trop beau" in sortie["audit"] or forcer_audit:
        sortie["audit_trop_beau"] = _audit_trop_beau(ctx, jeux, graines, brut)
        ecrire_brut("audit-trop-beau", sortie["audit_trop_beau"])
    sortie["avertissements_convergence"] = int(vs.AVERTISSEMENTS["convergence"])
    return sortie


def _mesurer_decoupe(ctx, c, ex, d, gr, sondes_c3_de=None):
    """Mesures d'une découpe d'un contraste, à chaque couche. `sondes_c3_de` : rang de découpe des sondes de C3 témoins (défaut : d)."""
    res, ext, debut, limite = ctx["res"], ctx["ext"], ctx["debut"], ctx["limite"]
    ids, pos = _rendre(res, ex)
    y = np.array([e.classe for e in ex])
    g = np.array([e.groupe for e in ex])
    R_all, N_all = ext(ids, pos)
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
    poids_sac = sac.poids_par_jeton()
    poids_g = np.array([poids_sac.get(int(t), 0.0) for t in res.gardes])
    presents = np.array([freq.get(int(t), 0) >= 2 for t in res.gardes])
    y_perm = permuter_par_groupe(y[app], g[app], gr["permutees"]) if c in ("C1", "C2") else None
    par_couche = {}
    for l in vd.COUCHES:
        s = vs.apprendre_sonde(R_all[l][app], y[app], g[app])
        w = da.ramener_au_flux(s.w_std, s.sigma)
        if c == "C3":
            ctx["sondes_c3"][(d, l)] = w
        w_perm = None
        if y_perm is not None:
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
        lec = ctx["lecteurs"][l]
        U_alea = vl.directions_aleatoires(len(w), gr["directions"][l])
        w_c3 = ctx["sondes_c3"][(d if sondes_c3_de is None else sondes_c3_de, l)]
        if c == "C2":
            m["a1"] = vl.mesure_a1(lec, ctx["idx_P"], w, U_alea, w_perm, w_c3)
        if c == "C1":
            m["a2"] = vl.mesure_a2(lec, w, poids_g, presents, U_alea, w_permutee=w_perm, w_c3=w_c3)
        if c in ("C1", "C2"):
            m["a3"] = _mesure_a3(ctx, s, l, lec, w, ids, R_all[l], tst, y, freq, sac, gr["tirages_a3"])
        diff = R_all[l][app][y[app] == 1].mean(0) - R_all[l][app][y[app] == 0].mean(0)
        m["lecture_r_difference"] = [int(res.gardes[i]) for i in np.argsort(-lecture_r(res, diff, l), kind="stable")[:20]]
        m["lecture_r_poids"] = [int(res.gardes[i]) for i in np.argsort(-lecture_r(res, w, l), kind="stable")[:20]]
        m["aii"] = _mesure_aii(N_all[l][app], y[app], g[app], N_all[l][tst], N_o[l] if ood_ex else None,
                               R_all[l][app], R_all[l][tst], R_o[l] if ood_ex else None, gr["neurones_aleatoires"],
                               ctx["n_tirages_hasard"], y_test=y[tst], y_ood=y_o if ood_ex else None)
        par_couche[l] = m
    return par_couche


def _mesure_a3(ctx, sonde, l, lec, w, ids, R_l, tst, y, freq, sac, graine, verifier_retrait=False):
    """Chutes d'AUROC de la sonde (non réapprise) après retrait des 20 jetons S, de 200 tirages appariés, des 20 jetons du sac ;
    base et retrait sur les mêmes exemples (lecture déclarée v3) ; flux de la seule couche l, sans cache."""
    res, ext, debut = ctx["res"], ctx["ext"], ctx["debut"]
    score_orig = {i: float(v) for i, v in zip(tst, sonde.scores(R_l[tst]))}
    restes = []

    def chute(jetons):
        nouv, gard = [], []
        for i in tst:
            r = _retirer_dans_invite(ids[i], debut, jetons)
            if r is None:
                continue
            nouv.append(r)
            gard.append(i)
        if verifier_retrait:
            s_j = set(jetons)
            restes.append(sum(any(t in s_j for t in x[debut:-2]) for x, _ in nouv))
        ys = y[gard]
        if len(set(ys.tolist())) < 2:
            return float("nan"), len(tst) - len(gard)
        Rn = ext.flux([x for x, _ in nouv], [p for _, p in nouv], l)
        base = _auc(ys, [score_orig[i] for i in gard])
        return base - _auc(ys, sonde.scores(Rn)), len(tst) - len(gard)

    jet_s = vl.jetons_a3(lec, w, res.gardes)
    chute_s, ec_s = chute(jet_s)
    tir = vl.tirages_apparies_a3(jet_s, freq, res.gardes, graine, n=ctx["n_tirages_a3"])
    chutes_al = [chute(t)[0] for t in tir]
    pos, neg = sac.premiers()
    chute_sac, ec_sac = chute(pos + neg)
    presents_test = sum(any(j in set(_texte(ids[i], debut)) for i in tst) for j in jet_s)
    out = {"chute_s": chute_s, "chutes_aleatoires": chutes_al, "chute_sac": chute_sac, "jetons_s": jet_s,
           "jetons_s_presents_test": int(presents_test), "exemples_ecartes": ec_s, "exemples_ecartes_sac": ec_sac,
           "n_jetons_sac": len(pos) + len(neg)}
    if verifier_retrait:
        out["invites_avec_jeton_retire_restant"] = int(sum(restes))
    return out


def _audit_trop_beau(ctx, jeux, graines, brut):
    """Audit R4 « trop beau » (lectures déclarées en tête) : (a) sixième découpe, (b) retrait vérifié sur le texte, (c) direction de
    C2 sans P."""
    res, debut = ctx["res"], ctx["debut"]
    out = {"sixieme_decoupe": {}, "retrait_verifie": {}, "c2_sans_P": []}
    racine = np.random.SeedSequence(vd.ENTROPIE).spawn(4)
    sixiemes = {}
    for ic, c in ((2, "C3"), (0, "C1"), (1, "C2")):  # même ordre que la course : C3 d'abord (témoin de A1)
        enfant = racine[ic].spawn(6)[5]
        t = dict(zip(vd.TACHES, enfant.spawn(len(vd.TACHES))))
        t["directions"] = dict(zip(vd.COUCHES, t["directions"].spawn(4)))
        sixiemes[c] = _mesurer_decoupe(ctx, c, jeux[c], 5, t)
        out["sixieme_decoupe"][c] = sixiemes[c]
    for c in ("C1", "C2"):  # (b) sur la première découpe, couche 14 (déclaré)
        ex = jeux[c]
        ids, pos = _rendre(res, ex)
        y = np.array([e.classe for e in ex])
        g = np.array([e.groupe for e in ex])
        app, tst = vd.decoupe(ex, graines.decoupes[c][0]["permutation"])
        R_all, _ = ctx["ext"](ids, pos)
        s = vs.apprendre_sonde(R_all[14][app], y[app], g[app])
        w = da.ramener_au_flux(s.w_std, s.sigma)
        sac = vs.apprendre_sac([_texte(ids[i], debut) for i in app], y[app], g[app])
        freq = {}
        for i in app:
            for j in set(_texte(ids[i], debut)):
                freq[j] = freq.get(j, 0) + 1
        out["retrait_verifie"][c] = _mesure_a3(ctx, s, 14, ctx["lecteurs"][14], w, ids, R_all[14], tst, y, freq, sac,
                                               graines.decoupes[c][0]["tirages_a3"], verifier_retrait=True)
    ex = jeux["C2"]  # (c)
    ids, _ = _rendre(res, ex)
    sans = [_retirer_dans_invite(x, debut, list(vd.P_PLANTES)) for x in ids]
    y = np.array([e.classe for e in ex])
    g = np.array([e.groupe for e in ex])
    R_all, _ = ctx["ext"]([x for x, _ in sans], [p for _, p in sans])
    for d in range(vd.N_DECOUPES):
        app, _ = vd.decoupe(ex, graines.decoupes["C2"][d]["permutation"])
        par = {}
        for l in vd.COUCHES:
            s = vs.apprendre_sonde(R_all[l][app], y[app], g[app])
            w = da.ramener_au_flux(s.w_std, s.sigma)
            par[l] = ctx["lecteurs"][l].rang_p(w, ctx["idx_P"])
        out["c2_sans_P"].append(par)
    return out


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
        comp, k_eff = vs.composantes(R_app, y_app, g_app, {"id": R_tst} | ({"ood": R_ood} if R_ood is not None else {}), k)
        out["pca_k_effectif"][k] = k_eff  # lecture déclarée : k plafonné au rang de l'apprentissage
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
                                                        [m["y_ood"] for m in ms],
                                                        [graines.decoupes[c][d]["reechantillonnage"] for d in range(5)], n=n_reech)
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
