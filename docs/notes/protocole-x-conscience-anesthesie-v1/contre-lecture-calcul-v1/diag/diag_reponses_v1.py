"""Contre-lecture du calcul illustratif v1 : détail réponse par réponse.

Reprend `mesurer` du script original (importé sans modification, mêmes graines, même ordre
des tirages) et consigne, pour chaque réponse : nombre de « uns » de la matrice 48 x 128
(total, ligne de la position perturbée, lignes suivantes), indice du script, indice sans la
ligne perturbée, indice rapporté à des matrices mélangées de même nombre de uns, indice
binarisé contre un écart-type calculé sans la position 0, rapport de participation brut et
en coordonnées réduites, gain brut et gain relatif. Une variante du bruit à amplitude figée
(tirée de la passe propre) est ajoutée pour isoler l'effet de l'amplitude dépendante de l'état.

Usage : python3 -I diag_reponses_v1.py SCRIPT_ORIGINAL DOSSIER_POIDS RESULTATS_ORIGINAUX SORTIE_JSON NOM_CONDITION...
"""
import importlib.util
import json
import math
import sys

import numpy as np

spec = importlib.util.spec_from_file_location("ci", sys.argv[1])
ci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ci)


def passe_variante(W, ids, perturbation=None, alpha=1.0, eta=0.0, graine_bruit=None, bruits_fixes=None, enregistrer=None):
    """Copie de ci.passe ; si bruits_fixes est donné, le bruit ajouté après le bloc c est
    bruits_fixes[c] (identique dans les deux passes) ; si enregistrer est une liste, on y
    range le bruit effectivement ajouté. Sans ces deux options, identique à ci.passe."""
    n = len(ids)
    x = W["wte.weight"][ids] + W["wpe.weight"][:n]
    masque = np.triu(np.full((n, n), -1e9, dtype=np.float32), k=1)
    rng = np.random.default_rng(graine_bruit) if eta > 0 else None
    n_site = None
    for c in range(ci.N_COUCHES):
        if c == ci.L0:
            n_site = float(np.linalg.norm(x[ci.T0]))
            if perturbation is not None:
                x = x.copy()
                x[ci.T0] = x[ci.T0] + perturbation
        p = f"h.{c}."
        a = ci.norme_couche(x, W[p + "ln_1.weight"], W[p + "ln_1.bias"])
        qkv = a @ W[p + "attn.c_attn.weight"] + W[p + "attn.c_attn.bias"]
        q, k, v = np.split(qkv, 3, axis=-1)
        q = q.reshape(n, ci.N_TETES, -1).transpose(1, 0, 2)
        k = k.reshape(n, ci.N_TETES, -1).transpose(1, 0, 2)
        v = v.reshape(n, ci.N_TETES, -1).transpose(1, 0, 2)
        s = q @ k.transpose(0, 2, 1) / math.sqrt(q.shape[-1]) + masque
        s = s - s.max(-1, keepdims=True)
        e = np.exp(s)
        att = e / e.sum(-1, keepdims=True)
        o = (att @ v).transpose(1, 0, 2).reshape(n, ci.D)
        x = x + alpha * (o @ W[p + "attn.c_proj.weight"] + W[p + "attn.c_proj.bias"])
        m = ci.norme_couche(x, W[p + "ln_2.weight"], W[p + "ln_2.bias"])
        h = ci.gelu(m @ W[p + "mlp.c_fc.weight"] + W[p + "mlp.c_fc.bias"])
        x = x + alpha * (h @ W[p + "mlp.c_proj.weight"] + W[p + "mlp.c_proj.bias"])
        if bruits_fixes is not None:
            x = x + bruits_fixes[c]
        elif rng is not None:
            eff = np.sqrt((x ** 2).mean(-1, keepdims=True))
            b = eta * eff * rng.standard_normal(x.shape).astype(np.float32)
            if enregistrer is not None:
                enregistrer.append(b)
            x = x + b
    return x, n_site


def lz_melange(b, rng, n=3):
    """Indice LZ brut rapporté à celui de matrices mélangées de même nombre de uns."""
    plat = b.reshape(-1)
    if plat.sum() == 0 or plat.sum() == plat.size:
        return None
    s = "".join("1" if v else "0" for v in plat)
    c = ci.lz76(s)
    ref = []
    for _ in range(n):
        q = plat.copy()
        rng.shuffle(q)
        ref.append(ci.lz76("".join("1" if v else "0" for v in q)))
    return c / float(np.mean(ref))


def rapport_participation(R):
    return ci.rapport_participation(R)


def mesurer_detail(W, entrees, dims_lz, graine_dir, alpha=1.0, eta=0.0, graine_bruit=None, bruit_fige=False, rng_melange=None):
    propres, bruits = [], []
    for ids in entrees:
        if bruit_fige:
            enr = []
            x0, n_site = passe_variante(W, ids, alpha=alpha, eta=eta, graine_bruit=graine_bruit, enregistrer=enr)
            bruits.append(enr)
        else:
            x0, _, n_site = ci.passe(W, ids, alpha=alpha, eta=eta, graine_bruit=graine_bruit, avec_logits=False)
            bruits.append(None)
        propres.append((x0, n_site))
    tous = np.concatenate([x for x, _ in propres], axis=0)
    sigma = tous.std(axis=0) + 1e-12
    sigma_sans0 = np.concatenate([x[1:] for x, _ in propres], axis=0).std(axis=0) + 1e-12
    rng = np.random.default_rng(graine_dir)
    rep = []
    pr_brut, pr_reduit = [], []
    for (ids, (x0, n_site), br) in zip(entrees, propres, bruits):
        reps, reps_z = [], []
        for _ in range(ci.K_DIR):
            u = rng.standard_normal(ci.D).astype(np.float32)
            u = u / np.linalg.norm(u) * ci.EPS * n_site
            if bruit_fige:
                x1, _ = passe_variante(W, ids, perturbation=u, alpha=alpha, eta=eta, bruits_fixes=br)
            else:
                x1, _, _ = ci.passe(W, ids, perturbation=u, alpha=alpha, eta=eta, graine_bruit=graine_bruit, avec_logits=False)
            d = (x1 - x0)[ci.T0:]
            z = np.abs(d) / sigma
            r = {}
            for t in (1.0, 0.5, 2.0):
                b = z[:, dims_lz] > t
                r[f"lz{t}"] = ci.indice_lz(b)
                r[f"uns{t}"] = int(b.sum())
                r[f"uns_site{t}"] = int(b[0].sum())
                r[f"lz_hors_site{t}"] = ci.indice_lz(b[1:])
            r["lz_melange1.0"] = lz_melange(z[:, dims_lz] > 1.0, rng_melange)
            z0 = np.abs(d) / sigma_sans0
            r["uns1.0_sigma_sans_pos0"] = int((z0[:, dims_lz] > 1.0).sum())
            r["uns_hors_site1.0_sigma_sans_pos0"] = int((z0[1:, dims_lz] > 1.0).sum())
            r["lz1.0_sigma_sans_pos0"] = ci.indice_lz(z0[:, dims_lz] > 1.0)
            r["etendue_hors_site"] = float((z[1:] > 1.0).mean())
            r["gain_norme_final"] = float(np.linalg.norm(d[1:]) / (np.linalg.norm(u) + 1e-30))
            r["gain_relatif_moyen"] = float(np.mean(np.linalg.norm(d[1:], axis=1) / np.linalg.norm(x0[ci.T0 + 1:], axis=1)))
            r["norme_d_site_sur_u"] = float(np.linalg.norm(d[0]) / np.linalg.norm(u))
            r["norme_site_entree"] = n_site
            r["norme_x0_final_moy"] = float(np.mean(np.linalg.norm(x0[ci.T0:], axis=1)))
            rep.append(r)
            reps.append(d[1:].reshape(-1))
            reps_z.append((d[1:] / sigma).reshape(-1))
        pr_brut.append(rapport_participation(np.stack(reps)))
        pr_reduit.append(rapport_participation(np.stack(reps_z)))
    s0 = sigma / sigma_sans0
    return {"reponses": rep, "pr_brut": pr_brut, "pr_reduit": pr_reduit,
            "sigma_avec_sur_sans_pos0": {"mediane": float(np.median(s0)), "q90": float(np.quantile(s0, 0.9)), "max": float(s0.max())},
            "norme_pos0_final_moy": float(np.mean([np.linalg.norm(x[0]) for x, _ in propres])),
            "norme_pos_autres_final_moy": float(np.mean([np.linalg.norm(x[1:], axis=1).mean() for x, _ in propres]))}


def main():
    script, dossier, res_orig, sortie = sys.argv[1:5]
    conditions = sys.argv[5:]
    orig = json.load(open(res_orig))
    g = orig["graines"]
    W = ci.lire_safetensors(dossier + "/model.safetensors")
    dec = ci.Decoupeur(dossier + "/vocab.json", dossier + "/merges.txt")
    naturels = [np.array(dec.coder(t)[:ci.T]) for t in ci.PASSAGES]
    repetes = [np.array((dec.coder(m) * ci.T)[:ci.T]) for m in ci.MOTS_REPETES]
    dims_lz = np.sort(np.random.default_rng(g["dims_lz"]).choice(ci.D, ci.N_DIM_LZ, replace=False))
    rng_melange = np.random.default_rng(np.random.SeedSequence(4242).spawn(1)[0])
    sortie_d = {"jetons_repetes_longueurs": [len(dec.coder(m)) for m in ci.MOTS_REPETES],
                "exemple_jetons": dec.coder("Hello world"), "conditions": {}}
    for nom in conditions:
        if nom == "E|naturel":
            res = mesurer_detail(W, naturels, dims_lz, g["directions"], rng_melange=rng_melange); cle = ("partie1", "E_entraine|naturel")
        elif nom == "E|repetitif":
            res = mesurer_detail(W, repetes, dims_lz, g["directions"], rng_melange=rng_melange); cle = ("partie1", "E_entraine|repetitif")
        elif nom == "R1|naturel":
            res = mesurer_detail(ci.reinitialiser(W, g["reinit"][0]), naturels, dims_lz, g["directions"], rng_melange=rng_melange); cle = ("partie1", "R1_reinitialise|naturel")
        elif nom == "M1|naturel":
            res = mesurer_detail(ci.melanger(W, g["melange"][0]), naturels, dims_lz, g["directions"], rng_melange=rng_melange); cle = ("partie1", "M1_melange|naturel")
        elif nom.startswith("alpha="):
            a = float(nom.split("=")[1])
            res = mesurer_detail(W, naturels, dims_lz, g["directions"], alpha=a, rng_melange=rng_melange); cle = ("partie2", f"amortissement|alpha={a}")
        elif nom.startswith("eta="):
            parts = nom.split("|")
            e = float(parts[0].split("=")[1]); j = int(parts[1].replace("graine", ""))
            fige = len(parts) > 2 and parts[2] == "fige"
            res = mesurer_detail(W, naturels, dims_lz, g["directions"], eta=e, graine_bruit=g["bruit"][j - 1], bruit_fige=fige, rng_melange=rng_melange)
            cle = None if fige else ("partie2", f"bruit|eta={e}|graine{j}")
        else:
            raise SystemExit(nom)
        rs = res["reponses"]
        resume = {}
        for t in ("1.0", "0.5", "2.0"):
            v = np.array([r[f"lz{t}"] for r in rs]); u = np.array([r[f"uns{t}"] for r in rs]); us = np.array([r[f"uns_site{t}"] for r in rs])
            hs = np.array([r[f"lz_hors_site{t}"] for r in rs])
            resume[f"theta{t}"] = {"lz_moy_ec": [float(v.mean()), float(v.std())],
                                   "uns_mediane": float(np.median(u)), "uns_min_max": [int(u.min()), int(u.max())],
                                   "part_reponses_sans_un": float((u == 0).mean()),
                                   "part_reponses_moins_de_10_uns": float((u < 10).mean()),
                                   "part_uns_sur_ligne_site": float(us.sum() / max(u.sum(), 1)),
                                   "uns_hors_site_mediane": float(np.median(u - us)),
                                   "part_reponses_avec_uns_hors_site": float(((u - us) > 0).mean()),
                                   "lz_hors_site_moy_ec": [float(hs.mean()), float(hs.std())],
                                   "part_lz_sup_1_05": float((v > 1.05).mean())}
        lm = [r["lz_melange1.0"] for r in rs if r["lz_melange1.0"] is not None]
        resume["lz_rapporte_melange_theta1"] = [float(np.mean(lm)), float(np.std(lm)), len(lm)] if lm else None
        resume["lz1_sigma_sans_pos0_moy_ec"] = [float(np.mean([r["lz1.0_sigma_sans_pos0"] for r in rs])), float(np.std([r["lz1.0_sigma_sans_pos0"] for r in rs]))]
        resume["uns1_sigma_sans_pos0_mediane"] = float(np.median([r["uns1.0_sigma_sans_pos0"] for r in rs]))
        resume["uns_hors_site1_sigma_sans_pos0_mediane"] = float(np.median([r["uns_hors_site1.0_sigma_sans_pos0"] for r in rs]))
        resume["pr_brut_moy"] = float(np.mean(res["pr_brut"])); resume["pr_reduit_moy"] = float(np.mean(res["pr_reduit"]))
        resume["gain_brut_moy"] = float(np.mean([r["gain_norme_final"] for r in rs]))
        resume["gain_relatif_moy"] = float(np.mean([r["gain_relatif_moyen"] for r in rs]))
        resume["norme_d_site_sur_u_moy"] = float(np.mean([r["norme_d_site_sur_u"] for r in rs]))
        resume["norme_site_entree_moy"] = float(np.mean([r["norme_site_entree"] for r in rs]))
        resume["norme_x0_final_moy"] = float(np.mean([r["norme_x0_final_moy"] for r in rs]))
        resume["sigma_avec_sur_sans_pos0"] = res["sigma_avec_sur_sans_pos0"]
        resume["norme_pos0_final_moy"] = res["norme_pos0_final_moy"]
        resume["norme_pos_autres_final_moy"] = res["norme_pos_autres_final_moy"]
        if cle is not None:
            o = orig[cle[0]][cle[1]]
            resume["controle_identite_avec_original"] = {
                "lz_theta1.0": [o["lz_theta1.0"], resume["theta1.0"]["lz_moy_ec"]],
                "lz_theta0.5": [o["lz_theta0.5"], resume["theta0.5"]["lz_moy_ec"]],
                "lz_theta2.0": [o["lz_theta2.0"], resume["theta2.0"]["lz_moy_ec"]],
                "participation_moy": [o["participation"][0], resume["pr_brut_moy"]],
                "gain_moy": [o["gain_norme_final"][0], resume["gain_brut_moy"]]}
        sortie_d["conditions"][nom] = {"resume": resume, "reponses": rs, "pr_brut": res["pr_brut"], "pr_reduit": res["pr_reduit"]}
        print(nom, json.dumps(resume), flush=True)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(sortie_d, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
