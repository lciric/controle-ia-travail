"""Recoupement du solveur de l'auteur par celui du réfutateur, sur les mondes de l'auteur — v1.

Réfutation, mise au point exploratoire, aucune revendication. Le banc de l'auteur (`banc_universelle_v1.py`, lu seul, jamais
modifié) fabrique ses mondes avec ses graines et calcule ses log W ; le solveur du réfutateur (`attaque_universelle_v1.py`,
classe `Lot`, écrit à part) encadre les mêmes maxima sur les mêmes tirages, les mêmes partitions et les mêmes questions.
Pour chaque méthode et chaque instant lu, on compare :
- validité du certificat de l'auteur : son log W doit rester sous la borne « haut » du réfutateur (statistique calculée avec
  les valeurs atteintes par un point admissible). Un dépassement voudrait dire que son dénominateur est sous une
  vraisemblance qu'un membre du nul atteint : hypothèse H4 rompue ;
- largeur de son certificat : « bas » du réfutateur (statistique certifiée à 10⁻⁴ nat) moins son log W ; positif = son
  certificat est plus lâche (coût en puissance pour lui, jamais en validité) ;
- décision : promotion chez l'un et pas chez l'autre.
Troisième mode, « tranchant » : les mondes tranchants et les cartes « loterie » de l'attaque du réfutateur (ses graines),
jugés par le code de l'auteur (ses fonctions, ses réglages ; seules les partitions lui sont passées toutes faites, les
mêmes que celles du réfutateur) : le code de l'auteur tient-il sa taille sous l'attaque la plus dure ?
Usage : python recoupement_universelle_v1.py puissance|taille|tranchant MONDES_PAR_CAS SORTIE.json [processus]
Graines : celles de l'auteur — SeedSequence(entropy=20261115201 (puissance) ou 20261115101 (taille), spawn_key=(indice du
cas, r)), scindée en (monde, sous-ensembles)."""
import json, math, os, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import numpy as np  # noqa: E402
import banc_universelle_v1 as b  # noqa: E402  (banc de l'auteur)
import attaque_universelle_v1 as a  # noqa: E402  (solveur du réfutateur)

CAS_TAILLE = ("interieur", "sommet", "extreme", "bruite", "sous_population", "grille", "v8")
CAS_PUISSANCE = (("neuve", 0.25), ("neuve", 0.40), ("neuve", 0.55))
ENTROPIES = {"taille": 20261115101, "puissance": 20261115201}
METHODES = ("v8", "limite", "v9", "v9_dense", "moitie_jugee", "croisee", "sous_echantillons", "confiance")


def encadrer(G, Wq, classe):
    lot = a.Lot(G, Wq, partitions=classe)
    att, cert = lot.converger(600)
    return att.max(1), cert.max(1)


def un_monde(args):
    sorte, cas, i_cas, r = args
    s_monde, s_sous = np.random.SeedSequence(entropy=ENTROPIES[sorte], spawn_key=(i_cas, r)).spawn(2)
    w = b.preparer(b.monde(cas, s_monde))
    sous = b.sous_ensembles(s_sous)
    auteur = b.evaluer(w, sous, METHODES)
    n, y, lq = b.N, w["y"], w["lq"]
    masques = b.masques(w["z"], w["g"], w["arch"], "v9")
    G = a.composantes(w["Ak"], y, masques, b.K)
    T, Td, Tm = b.INSTANTS, b.INSTANTS_DENSES, (25, 50, 75, 100)
    tout = np.arange(masques.shape[0])
    moi = {}

    def prefixes(ts, base=None, debut=0):
        W = np.zeros((len(ts), n))
        for i, t in enumerate(ts):
            W[i, debut:debut + t] = 1.0
        return W if base is None else W * base[None, :]

    for nom, classe, ts in (("v8", [0], T), ("limite", [0, 1], T), ("v9", tout, T), ("v9_dense", tout, Td)):
        Wq = prefixes(ts)
        att, cert = encadrer(G, Wq, classe)
        moi[nom] = (Wq @ lq - cert, Wq @ lq - att)
    Wq = prefixes(Tm, debut=100)
    att, cert = encadrer(G, Wq, tout)
    moi["moitie_jugee"] = (Wq @ lq - cert, Wq @ lq - att)
    pair = (np.arange(n) % 2 == 0).astype(float)
    Wq = np.concatenate([prefixes(T, base=pair), prefixes(T, base=1.0 - pair)])
    att, cert = encadrer(G, Wq, tout)
    moi["croisee"] = tuple(a.log_moyenne_exp((Wq @ lq - v).reshape(2, len(T)), 0) for v in (cert, att))
    Wq = np.concatenate([prefixes(T, base=np.asarray(s_b, dtype=float)) for s_b in sous])
    att, cert = encadrer(G, Wq, tout)
    moi["sous_echantillons"] = tuple(a.log_moyenne_exp((Wq @ lq - v).reshape(len(sous), len(T)), 0) for v in (cert, att))
    d1 = np.zeros(n); d1[:100] = 1.0
    c = float(lq[:100].sum()) - math.log(1.0 / b.BETA_CONFIANCE)
    lignes = []
    for t in Tm:
        d0 = np.zeros(n); d0[100:100 + t] = 1.0
        for lam in b.LAMBDAS:
            lignes.append(d0 + lam * d1)
    Wq = np.array(lignes)
    att, cert = encadrer(G, Wq, tout)
    lam_v = np.tile(np.array(b.LAMBDAS), len(Tm))
    lq0 = np.array([lq[100:100 + t].sum() for t in Tm])
    moi["confiance"] = tuple(lq0 - (v - lam_v * c).reshape(len(Tm), len(b.LAMBDAS)).min(1) for v in (cert, att))
    out = {}
    for m in METHODES:
        lw_auteur, seuil = auteur[m]
        bas, haut = moi[m]
        out[m] = {"exces_sur_la_borne_haute": float(np.max(lw_auteur - haut)),           # > 0 : certificat de l'auteur en défaut
                  "largeur_du_certificat_de_l_auteur": float(np.max(bas - lw_auteur)),   # > 0 : son certificat est plus lâche
                  "largeur_de_mon_encadrement": float(np.max(haut - bas)),
                  "promue_auteur": bool(np.max(lw_auteur) >= seuil), "promue_moi": bool(np.max(bas) >= seuil),
                  "promotion_possible_au_plus": bool(np.max(haut) >= seuil)}
    return out


# --- le code de l'auteur sous l'attaque du réfutateur : mondes « tranchants » et cartes « loterie » ---------------------
CAS_TRANCHANTS = ("tranchant_v9", "tranchant_moitie", "tranchant_croisee", "tranchant_sous_echantillons", "tranchant_confiance")
VALIDES_AUTEUR = {"v9": "v9", "dense": "v9_dense", "moitie_jugee": "moitie_jugee", "croisee": "croisee",
                  "sous_echantillons": "sous_echantillons", "confiance": "confiance"}
TEMOINS = 40                                    # mondes sans pari gagné joués quand même, par cas


def un_monde_tranchant(args):
    """Un monde tranchant du réfutateur (mêmes graines que son attaque), jugé par le code de l'auteur et par le sien.
    Le code de l'auteur n'est joué que si un pari est gagné, ou pour les TEMOINS premiers mondes."""
    cas, r = args
    i_cas = a.CAS_TAILLE.index(cas)
    s_monde, s_issues, s_parts = np.random.SeedSequence(entropy=a.ENTROPIE_TAILLE, spawn_key=(i_cas, r)).spawn(3)
    parts = a.tirer_parts(np.random.default_rng(s_parts), 200)
    w = a.monde_tranchant(np.random.default_rng(s_monde), a.CAS_TRANCHANTS[cas], parts)
    y = a.tirer_issues(np.random.default_rng(s_issues), w["P"])
    Q = a.carte_loterie(w["P"], [(i, 2) for i, _ in w["paris"]])
    gagne = any(bool(y[i] == 2) for i, _ in w["paris"])
    if not gagne and r >= TEMOINS:
        return None
    moi = a.juger(w, y, Q, parts, a.VALIDES)
    wa = b.preparer({"arch": None, "z": w["z"], "g": w["g"], "Lc": w["S"], "P": w["P"], "Q": Q, "y": y})
    masques_v9 = w["masques"]
    b.masques = lambda z, g, arch, sorte: masques_v9 if sorte == "v9" else masques_v9[:2] if sorte == "limite" else masques_v9[:1]
    auteur = b.evaluer(wa, [pb.astype(float) for pb in parts], tuple(VALIDES_AUTEUR.values()))
    out = {"gagne": gagne}
    for m, ma in VALIDES_AUTEUR.items():
        lw, seuil = auteur[ma]
        out[m] = {"promue_auteur": bool(np.max(lw) >= seuil), "promue_moi": bool(moi[m][0]),
                  "exces_de_l_auteur_sur_ma_borne_haute": float(np.max(lw) - moi[m][3])}
    return out


def tranchant(R, sortie, processus):
    import multiprocessing as mp
    t0 = time.time()
    doc = {"essai": "le code de l'auteur sous l'attaque « tranchant » du réfutateur", "mondes_par_cas": R,
           "graines": {"entropie": a.ENTROPIE_TAILLE, "spawn_key": "(indice du cas dans l'attaque, r), r = 0..R−1"},
           "note": "le code de l'auteur n'est joué que sur les mondes où un pari est gagné et sur les %d premiers mondes ; "
                   "ailleurs la carte a une vraisemblance presque nulle. Taux rapportés sur les R mondes." % TEMOINS, "cas": {}}
    with mp.get_context("fork").Pool(processus) as pool:
        for cas in CAS_TRANCHANTS:
            sorties = pool.map(un_monde_tranchant, [(cas, r) for r in range(R)], chunksize=20)
            joues = [s for s in sorties if s is not None]
            res = {"mondes": R, "mondes_juges_par_le_code_de_l_auteur": len(joues),
                   "mondes_a_pari_gagne": int(sum(1 for s in joues if s["gagne"])), "methodes": {}}
            for m in VALIDES_AUTEUR:
                ka = int(sum(1 for s in joues if s[m]["promue_auteur"])); km = int(sum(1 for s in joues if s[m]["promue_moi"]))
                res["methodes"][m] = {
                    "promotions_code_auteur": ka, "taux_code_auteur": round(ka / R, 5),
                    "intervalle_clopper_pearson_95_code_auteur": a.clopper_pearson(ka, R),
                    "promotions_code_refutateur_sur_les_memes_mondes": km,
                    "promue_chez_l_auteur_seul": int(sum(1 for s in joues if s[m]["promue_auteur"] and not s[m]["promue_moi"])),
                    "promue_chez_le_refutateur_seul": int(sum(1 for s in joues if s[m]["promue_moi"] and not s[m]["promue_auteur"])),
                    "temoins_sans_pari_gagne_promus_par_l_auteur": int(sum(1 for s in joues if not s["gagne"] and s[m]["promue_auteur"])),
                    "plus_grand_exces_de_l_auteur_sur_ma_borne_haute": float(max(s[m]["exces_de_l_auteur_sur_ma_borne_haute"] for s in joues))}
            doc["cas"][cas] = res
            print(cas, round(time.time() - t0, 1), "s", json.dumps({m: (v["promotions_code_auteur"], v["promotions_code_refutateur_sur_les_memes_mondes"])
                  for m, v in res["methodes"].items()}), flush=True)
    doc["duree_s"] = round(time.time() - t0, 1)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)


def main():
    sorte, R, sortie = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    processus = int(sys.argv[4]) if len(sys.argv) > 4 else 2
    if os.path.exists(sortie):
        raise SystemExit("sortie existante, jamais écrasée")
    if sorte == "tranchant":
        return tranchant(R, sortie, processus)
    cas_liste = CAS_PUISSANCE if sorte == "puissance" else CAS_TAILLE[:6]
    import multiprocessing as mp
    t0 = time.time()
    doc = {"essai": "recoupement du solveur de l'auteur", "sorte": sorte, "mondes_par_cas": R,
           "graines": {"entropie": ENTROPIES[sorte], "spawn_key": "(indice du cas chez l'auteur, r), r = 0..R−1"}, "cas": {}}
    with mp.get_context("fork").Pool(processus) as pool:
        for cas in cas_liste:
            i_cas = (CAS_PUISSANCE if sorte == "puissance" else CAS_TAILLE).index(cas)
            sorties = pool.map(un_monde, [(sorte, cas, i_cas, r) for r in range(R)], chunksize=2)
            res = {}
            for m in METHODES:
                ex = np.array([s[m]["exces_sur_la_borne_haute"] for s in sorties])
                la = np.array([s[m]["largeur_du_certificat_de_l_auteur"] for s in sorties])
                mi = np.array([s[m]["largeur_de_mon_encadrement"] for s in sorties])
                pa = np.array([s[m]["promue_auteur"] for s in sorties]); pm = np.array([s[m]["promue_moi"] for s in sorties])
                res[m] = {"mondes": R,
                          "plus_grand_exces_du_log_w_de_l_auteur_sur_la_borne_haute": float(ex.max()),
                          "mondes_ou_son_certificat_est_en_defaut_au_dela_de_1e-6": int((ex > 1e-6).sum()),
                          "largeur_de_son_certificat_mediane": float(np.median(la)), "largeur_de_son_certificat_max": float(la.max()),
                          "mondes_ou_son_certificat_depasse_0.01_nat": int((la > 1e-2).sum()),
                          "largeur_de_mon_encadrement_max": float(mi.max()),
                          "promotions_auteur": int(pa.sum()), "promotions_moi": int(pm.sum()),
                          "promue_chez_l_auteur_seul": int((pa & ~pm).sum()), "promue_chez_moi_seul": int((~pa & pm).sum())}
            doc["cas"][cas if isinstance(cas, str) else f"neuve_{cas[1]}"] = res
            print(cas, round(time.time() - t0, 1), "s", json.dumps({m: (v["mondes_ou_son_certificat_est_en_defaut_au_dela_de_1e-6"],
                  round(v["largeur_de_son_certificat_max"], 4), v["promotions_auteur"], v["promotions_moi"]) for m, v in res.items()}), flush=True)
    doc["duree_s"] = round(time.time() - t0, 1)
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
