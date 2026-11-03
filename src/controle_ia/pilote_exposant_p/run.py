"""Lanceur du pilote de l'exposant p (instance de calcul ; mode jouet sur processeur pour les essais et la répétition).

    PYTHONPATH=src python -m controle_ia.pilote_exposant_p.run --config C --stimuli S --run-id ID --prereg P
    PYTHONPATH=src python -m controle_ia.pilote_exposant_p.run --config C --stimuli S --run-id ID --jouet

Ordre (gelé) : gardes ; manifeste ; modèle de base (témoin) : directions publiées, témoin positif Wealth × Gender sur le
sous-ensemble d'ancres 0 — arrêt « instrument non validé » s'il échoue —, puis plans descriptifs ; modèle lu :
directions, plans isotropes — arrêt s'ils sortent de la tolérance —, plan (E, R) sur S sous-ensembles, famille des
différences aléatoires, puis plans descriptifs ; analyse gelée ; sorties scellées (`diag/<run>/`). Un bloc décisif qui
ne tient plus dans le plafond de durée arrête le run ; un bloc descriptif est alors sauté et consigné.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..scellement import sceller
from . import analyse as A
from . import ancres as AN
from . import directions as D
from . import references as REF
from . import stimuli as ST
from .ajustement import ajuster_plan, bootstrap_ancres, bootstrap_difference, bootstrap_moyenne, intervalle_percentile
from .amont import verifier_copie

TACHES = ["differences_aleatoires", "bootstrap_difference", "bootstrap_ancres", "jouet"]
DIRS_TEMOIN = ("Gender", "Wealth", "Formal", "Literary", "Age", "Tense", "Sentiment")
FAMILLE_CONTRASTIVE = ("Gender", "Wealth", "Age", "Tense", "Sentiment")


def progres(**kv) -> None:
    t = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + t + "".join(f" {k}={str(v).replace(' ', '_')}" for k, v in kv.items()), file=sys.stderr, flush=True)


def sha(chemin: str | Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def exiger_config(cfg: dict, chemin_stimuli: Path) -> None:
    """Gardes de cohérence : constantes de lecture du code = configuration ; empreintes citées = fichiers lus."""
    lec = cfg["lecture"]
    attendu = {"delta_equivalence": A.DELTA_EQUIVALENCE, "seuil_cos": A.SEUIL_COS, "p_publie_wg": A.P_PUBLIE_WG,
               "tol_p_identiques": A.TOL_P_IDENTIQUES, "tol_intercept_identiques": A.TOL_INTERCEPT_IDENTIQUES,
               "intervalle_p_differentes": list(A.INTERVALLE_P_DIFFERENTES), "intervalle_isotrope": list(A.INTERVALLE_ISOTROPE),
               "cos_min_directions_publiees": A.COS_MIN_DIRECTIONS_PUBLIEES, "part_max_echecs": A.PART_MAX_ECHECS,
               "norme_ancres_publiee": A.NORME_ANCRES_PUBLIEE, "tol_norme_relative": A.TOL_NORME_RELATIVE}
    ecarts = [k for k, v in attendu.items() if lec.get(k) != v]
    if ecarts:
        raise GardeArret(f"configuration ≠ constantes gelées du code d'analyse : {ecarts}")
    if sha(chemin_stimuli) != cfg["stimuli_sha256"]:
        raise GardeArret(f"stimuli {chemin_stimuli} : empreinte ≠ celle citée par la configuration")
    for nom, h in cfg["references_sha256"].items():
        if sha(REF.DOSSIER / nom) != h:
            raise GardeArret(f"référence publiée {nom} : empreinte ≠ celle citée par la configuration")
    prov = verifier_copie()
    if prov["commit"] != cfg["amont_commit"]:
        raise GardeArret("copie amont d'un autre commit que celui cité par la configuration")


class _Horloge:
    def __init__(self, duree_max_s: float):
        self.t0 = time.time()
        self.max = duree_max_s
        self.durees: list[float] = []

    def ecoulee(self) -> float:
        return time.time() - self.t0

    def tient(self, n_plans: int) -> bool:
        moy = float(np.mean(self.durees)) if self.durees else 0.0
        return self.ecoulee() + n_plans * moy <= self.max


class Pilote:
    def __init__(self, cfg: dict, stim: dict, jouet: bool, rng_jouet: np.random.Generator | None):
        self.cfg, self.stim, self.jouet = cfg, stim, jouet
        self.rng_jouet = rng_jouet
        self.plans: list[dict] = []
        self.grilles: dict[str, np.ndarray] = {}
        self.sautes: list[dict] = []
        self.horloge = _Horloge(cfg["plafonds"]["duree_max_s"])
        # tailles : section « jouet » en répétition, sinon section réelle ; paramètres scientifiques : toujours réels
        self.g = cfg["jouet"] if jouet else cfg
        self.angles = np.linspace(0.0, cfg["grille"]["angle_max_deg"], self.g["grille"]["n"])
        self.par = self.g["ancres"]["par_sous_ensemble"]
        self.S = self.g["ancres"]["sous_ensembles"]
        self.paires_iso = cfg["isotropes"]["paires"][: self.g.get("isotropes_paires_max", len(cfg["isotropes"]["paires"]))]
        self.etape = "mise en place"

    # -- modèles -------------------------------------------------------------------------------------------------
    def charger(self, role: str):
        import torch

        if self.jouet:
            from transformers import LlamaConfig, LlamaForCausalLM

            torch.manual_seed(1 if role == "temoin" else 2)
            m = LlamaForCausalLM(LlamaConfig(**self.cfg["jouet"]["modele"])).eval()
            return m, TokeniseurJouet(self.cfg["jouet"]["modele"]["vocab_size"]), {"jouet": role}
        from huggingface_hub import HfApi
        from transformers import AutoModelForCausalLM, AutoTokenizer

        nom = self.cfg["modeles"][role]
        rev = HfApi().model_info(nom).sha
        tok = AutoTokenizer.from_pretrained(nom, revision=rev)
        m = AutoModelForCausalLM.from_pretrained(nom, revision=rev, dtype=getattr(torch, self.cfg["dtype"]),
                                                 attn_implementation=self.cfg["attention"]).to("cuda").eval()
        return m, tok, {"nom": nom, "revision": rev, "attention": m.config._attn_implementation,
                        "dtype": str(next(m.parameters()).dtype)}

    # -- plans ---------------------------------------------------------------------------------------------------
    def plan(self, modele, role, famille, nom, d1, d2, ids, acts, s, decisif=False, garde=True, cos=None):
        from .balayage import balayer_plan_ancres

        exiger_sans_signal(f"plan {famille}/{nom}/{s}")
        t = time.time()
        sl = AN.sous_ensembles(self.par, self.S)[s]
        import torch

        g = balayer_plan_ancres(modele, torch.as_tensor(ids[sl]), acts[sl], d1, d2, self.angles, self.couche_p,
                                self.couche_m, self.cfg["lot_balayage"])
        if not np.all(np.isfinite(g)):
            raise GardeArret(f"grille non finie : {famille}/{nom}/{s}")
        r = ajuster_plan(self.angles, g, self.cfg["seuil_f"], self.cfg["fenetre_deg"])
        dur = time.time() - t
        self.horloge.durees.append(dur)
        cle = f"{role}|{famille}|{nom}|{s}"
        self.grilles[cle] = g.astype(np.float32)
        rec = {"role": role, "famille": famille, "nom": nom, "sous_ensemble": s, "cos": cos, "garde": garde,
               "decisif": decisif, "duree_s": round(dur, 2), **r}
        self.plans.append(rec)
        progres(etape=self.etape, famille=famille, plan=nom, s=s, p=f"{r['p']:.3f}", duree_s=f"{dur:.1f}")
        return rec

    def bloc(self, nom_bloc: str, travaux: list, decisif: bool) -> bool:
        """`travaux` : liste de fonctions sans argument ; True si le bloc a été fait."""
        if not self.horloge.tient(len(travaux)):
            if decisif:
                raise GardeArret(f"plafond de durée projeté dépassé avant le bloc décisif {nom_bloc}")
            self.sautes.append({"bloc": nom_bloc, "plans": len(travaux), "motif": "plafond de durée projeté"})
            progres(etape=self.etape, bloc_saute=nom_bloc)
            return False
        for f in travaux:
            f()
        return True

    # -- exécution -----------------------------------------------------------------------------------------------
    def executer(self) -> dict:
        import torch

        cfg, stim = self.cfg, self.stim
        pub = REF.charger_directions()
        sortie: dict = {"jouet": self.jouet}
        # réserve et ancres
        self.etape = "réserve"
        m_t, tok_t, info_t = self.charger("temoin")
        n_res = self.g["ancres"]["reserve"]
        if self.jouet:
            ids = AN.reserve_jouet(n_res, cfg["jouet"]["modele"]["vocab_size"], self.rng_jouet)
            textes, rev_jeu = [], "jouet"
        else:
            rev_jeu = AN.revision_du_jeu()
            ids, textes = AN.charger_reserve(tok_t, n_res, rev_jeu)
        if self.S * self.par > ids.shape[0]:
            raise GardeArret("réserve plus petite que les ancres demandées")
        sortie["reserve"] = {"n": int(ids.shape[0]), "empreinte_ids": AN.empreinte_ids(ids), "revision_jeu": rev_jeu,
                             "ancres": self.S * self.par, "textes_ancres_sous_ensemble_0": textes[:self.par]}
        self.ids = ids
        self.couche_p = cfg["couche_perturbation"]
        from .balayage import activations_jetons, activations_textes, couche_de_mesure

        # ---- modèle de base (témoin) ----
        self.etape = "témoin : directions"
        self.couche_m = couche_de_mesure(m_t, cfg["decalage_mesure"])
        sortie["modele_temoin"] = info_t | {"couche_mesure": self.couche_m}
        dt = {}
        for n in DIRS_TEMOIN:
            a, b = ST.paires(stim, n)
            dt[n] = D.difference_de_moyennes(activations_textes(m_t, tok_t, a, self.couche_p),
                                             activations_textes(m_t, tok_t, b, self.couche_p))
        cos_pub = {n: (D.cosinus(dt[n], pub[n]) if dt[n].shape == pub[n].shape else float("nan")) for n in DIRS_TEMOIN}
        c_dir = A.controle_directions_publiees({n: cos_pub[n] for n in ("Gender", "Wealth")})
        sortie["temoin_directions"] = {"cosinus_avec_publiees": cos_pub, "controle": c_dir}
        n_t = self.g["plans"]["temoin"]["WG_sous_ensembles"] * self.par
        acts_t = activations_jetons(m_t, torch.as_tensor(ids[:n_t]), self.couche_p, cfg["lot_activations"])
        norme0 = float(np.linalg.norm(acts_t[:self.par], axis=1).mean())
        self.etape = "témoin : Wealth × Gender"
        cos_wg = D.cosinus(dt["Wealth"], dt["Gender"])
        r0 = self.plan(m_t, "temoin", "temoin_positif", "Wealth×Gender", dt["Wealth"], dt["Gender"], ids, acts_t, 0,
                       decisif=True, cos=cos_wg)
        c_tp = A.controle_temoin_positif(r0["p"], tuple(r0["intercepts"]), norme0)
        c_tp["norme_ancres_sous_ensemble_0"] = norme0
        sortie["temoin_positif"] = c_tp
        if not self.jouet and not A.instrument_valide(c_dir, c_tp):
            sortie["instrument"] = {"valide": False, "motif": "témoin positif ou directions publiées hors tolérance"}
            raise ArretInstrument(sortie)
        self.etape = "témoin : descriptifs"
        iso = D.isotropes_papier(cfg["isotropes"]["n"], acts_t.shape[1], cfg["isotropes"]["graine_torch"])
        paires_iso = self.paires_iso
        self.bloc("temoin_isotropes", [lambda i=i, j=j: self.plan(m_t, "temoin", "isotrope", f"iso{i}×iso{j}", iso[i], iso[j],
                                                                   ids, acts_t, 0, cos=D.cosinus(iso[i], iso[j]))
                                       for i, j in paires_iso], decisif=False)
        self.bloc("temoin_WG_sous_ensembles", [lambda s=s: self.plan(m_t, "temoin", "temoin_positif", "Wealth×Gender", dt["Wealth"],
                                                                      dt["Gender"], ids, acts_t, s, cos=cos_wg)
                                               for s in range(1, self.g["plans"]["temoin"]["WG_sous_ensembles"])], decisif=False)
        del m_t
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        # ---- modèle lu ----
        self.etape = "lu : directions"
        m, tok, info = self.charger("lu")
        if not self.jouet:
            if tok.bos_token_id != tok_t.bos_token_id or tok.convert_ids_to_tokens(ids[:50].ravel().tolist()) != \
                    tok_t.convert_ids_to_tokens(ids[:50].ravel().tolist()):
                raise GardeArret("le tokeniseur du modèle lu ne lit pas les ancres comme celui du modèle de base")
        self.couche_m = couche_de_mesure(m, cfg["decalage_mesure"])
        sortie["modele_lu"] = info | {"couche_mesure": self.couche_m}
        dl = {}
        noms = [("E", None), ("R", None), ("E_naif", None), ("E_naif_inverse", None), ("E_echelle", None)] + \
               [(n, None) for n in DIRS_TEMOIN]
        for n, mo in noms:
            a, b = ST.paires(stim, n, mo)
            dl[n] = D.difference_de_moyennes(activations_textes(m, tok, a, self.couche_p), activations_textes(m, tok, b, self.couche_p))
        for mo in ("A", "B"):
            for n in ("E", "R"):
                a, b = ST.paires(stim, n, mo)
                dl[f"{n}_{mo}"] = D.difference_de_moyennes(activations_textes(m, tok, a, self.couche_p),
                                                           activations_textes(m, tok, b, self.couche_p))
        cosl = {f"{x}·{y}": D.cosinus(dl[x], dl[y]) for x, y in (
            ("E", "R"), ("E_naif", "R"), ("E_naif_inverse", "R"), ("E", "E_echelle"), ("E_A", "E_B"), ("R_A", "R_B"),
            ("R", "Formal"), ("E", "Formal"), ("E", "Literary"), ("R", "Literary"), ("Formal", "Literary"))}
        sortie["directions_lu"] = {"cosinus": cosl}
        acts_res = activations_jetons(m, torch.as_tensor(ids), self.couche_p, cfg["lot_activations"])
        Mrd = self.g["differences_aleatoires"]["paires_disjointes_M"]
        rd, idx = D.differences_aleatoires(acts_res, 2 * Mrd, generateur(self.graines["differences_aleatoires"]),
                                           self.g["differences_aleatoires"]["k_moy"])
        acts = acts_res[:self.S * self.par]
        iso = D.isotropes_papier(cfg["isotropes"]["n"], acts.shape[1], cfg["isotropes"]["graine_torch"])
        P = self.g["plans"]["lu"]

        self.etape = "lu : isotropes"
        self.bloc("lu_isotropes", [lambda i=i, j=j: self.plan(m, "lu", "isotrope", f"iso{i}×iso{j}", iso[i], iso[j], ids, acts, 0,
                                                              decisif=True, cos=D.cosinus(iso[i], iso[j]))
                                   for i, j in paires_iso], decisif=True)
        p_iso = np.array([x["p"] for x in self.plans if x["role"] == "lu" and x["famille"] == "isotrope"])
        c_iso = A.controle_isotrope(float(np.nanmean(p_iso)) if np.isfinite(p_iso).any() else float("nan"),
                                    float(np.mean(~np.isfinite(p_iso))))
        sortie["isotrope_lu"] = c_iso
        if not self.jouet and not c_iso["valide"]:
            sortie["instrument"] = {"valide": False, "motif": "isotropes du modèle lu hors tolérance"}
            raise ArretInstrument(sortie)
        sortie["instrument"] = {"valide": bool(A.instrument_valide(c_dir, c_tp, c_iso)), "jouet": self.jouet}

        self.etape = "lu : plan (E, R)"
        cos_er = cosl["E·R"]
        exclu = abs(cos_er) >= A.SEUIL_COS
        n_er = 1 if exclu else P["ER_sous_ensembles"]
        self.bloc("lu_ER", [lambda s=s: self.plan(m, "lu", "ER", "E×R", dl["E"], dl["R"], ids, acts, s, decisif=True,
                                                  garde=not exclu, cos=cos_er) for s in range(n_er)], decisif=True)
        self.etape = "lu : différences aléatoires"
        trav = []
        for k in range(Mrd):
            c = D.cosinus(rd[2 * k], rd[2 * k + 1])
            if abs(c) >= A.SEUIL_COS:
                self.plans.append({"role": "lu", "famille": "rd_rd", "nom": f"rd{2*k}×rd{2*k+1}", "sous_ensemble": 0,
                                   "cos": c, "garde": False, "decisif": True, "p": float("nan"), "exclu_cos": True})
                continue
            trav.append(lambda k=k, c=c: self.plan(m, "lu", "rd_rd", f"rd{2*k}×rd{2*k+1}", rd[2 * k], rd[2 * k + 1], ids, acts, 0,
                                                   decisif=True, cos=c))
        self.bloc("lu_rd_rd", trav, decisif=True)

        self.etape = "lu : descriptifs"
        desc = []
        for k in range(P["E_rd"]):
            desc.append(("lu_E_rd", lambda k=k: self.plan(m, "lu", "E_rd", f"E×rd{k}", dl["E"], rd[k], ids, acts, 0,
                                                          cos=D.cosinus(dl["E"], rd[k]))))
            desc.append(("lu_R_rd", lambda k=k: self.plan(m, "lu", "R_rd", f"R×rd{k}", dl["R"], rd[k], ids, acts, 0,
                                                          cos=D.cosinus(dl["R"], rd[k]))))
        fam = FAMILLE_CONTRASTIVE[: self.g.get("famille_contrastive_max", len(FAMILLE_CONTRASTIVE))]
        for i in range(len(fam)):
            for j in range(i + 1, len(fam)):
                c = D.cosinus(dl[fam[i]], dl[fam[j]])
                desc.append(("lu_contrastives", lambda i=i, j=j, c=c: self.plan(
                    m, "lu", "contrastive", f"{fam[i]}×{fam[j]}", dl[fam[i]], dl[fam[j]], ids, acts, 0,
                    garde=abs(c) < A.SEUIL_COS, cos=c)))
        for s in range(P["WG_sous_ensembles"]):
            desc.append(("lu_WG", lambda s=s: self.plan(m, "lu", "temoin_positif", "Wealth×Gender", dl["Wealth"], dl["Gender"],
                                                        ids, acts, s, cos=D.cosinus(dl["Wealth"], dl["Gender"]))))
        for k in range(P["mixtes_rd"]):
            for n in ("Gender", "Wealth"):
                desc.append(("lu_mixtes", lambda k=k, n=n: self.plan(m, "lu", "mixte", f"{n}×rd{k}", dl[n], rd[k], ids, acts, 0,
                                                                     cos=D.cosinus(dl[n], rd[k]))))
        for s in range(P["moities_sous_ensembles"]):
            for mo in ("A", "B"):
                desc.append(("lu_moities", lambda s=s, mo=mo: self.plan(m, "lu", f"moitie_{mo}", f"E_{mo}×R_{mo}", dl[f"E_{mo}"],
                                                                        dl[f"R_{mo}"], ids, acts, s,
                                                                        cos=D.cosinus(dl[f"E_{mo}"], dl[f"R_{mo}"]))))
        for s in range(P["E_Rpapier_sous_ensembles"]):
            desc.append(("lu_E_Rpapier", lambda s=s: self.plan(m, "lu", "E_Rpapier", "E×Formal", dl["E"], dl["Formal"], ids, acts,
                                                               s, cos=cosl["E·Formal"])))
        for nb in dict.fromkeys(b for b, _ in desc):
            self.bloc(nb, [f for b, f in desc if b == nb], decisif=False)
        sortie["rd_indices_sha256"] = hashlib.sha256(np.ascontiguousarray(idx).tobytes()).hexdigest()
        return sortie


class ArretInstrument(Exception):
    def __init__(self, sortie: dict):
        super().__init__(sortie.get("instrument", {}).get("motif", "instrument non validé"))
        self.sortie = sortie


class TokeniseurJouet:
    """Tokeniseur de répétition : mots → identifiants par empreinte, BOS = 1. Aucun téléchargement."""

    bos_token_id = 1

    def __init__(self, vocab: int):
        self.vocab = vocab

    def _ids(self, t: str) -> list[int]:
        return [1] + [3 + int(hashlib.sha256(w.encode()).hexdigest(), 16) % (self.vocab - 3) for w in t.split()]

    def __call__(self, t, return_tensors=None, **_):
        import torch

        if isinstance(t, list):
            return {"input_ids": [self._ids(x) for x in t]}
        x = self._ids(t)
        return {"input_ids": torch.tensor([x]) if return_tensors == "pt" else x}

    def decode(self, ids) -> str:
        return " ".join(str(int(i)) for i in ids)

    def convert_ids_to_tokens(self, ids):
        return [str(int(i)) for i in ids]


def analyser(pilote: Pilote, sortie: dict, graines: dict) -> dict:
    """Lecture gelée (R1) : issue principale, phrase, secondaires descriptifs, audit de symétrie."""
    plans = pilote.plans
    lu = [x for x in plans if x["role"] == "lu"]

    def ps(famille, nom=None, garde=True):
        return np.array([x["p"] for x in lu if x["famille"] == famille and (nom is None or x["nom"] == nom)
                         and (x.get("garde", True) or not garde)], dtype=np.float64)

    rng = generateur(graines["bootstrap_difference"])
    B = pilote.cfg["bootstrap"]["B_difference"]
    cos_er = sortie["directions_lu"]["cosinus"]["E·R"]
    p_er, p_rd = ps("ER"), ps("rd_rd")
    n_rd_tot = len([x for x in lu if x["famille"] == "rd_rd"])
    ech_er = float(np.mean(~np.isfinite(p_er))) if p_er.size else 1.0
    ech_rd = float(np.mean(~np.isfinite(p_rd))) if p_rd.size else 1.0
    d = bootstrap_difference(p_er, p_rd, B, rng)
    lect: dict = {"cos_ER": cos_er, "delta": d, "echecs_ER": ech_er, "echecs_rd": ech_rd,
                  "plans_rd_mesures": int(p_rd.size), "plans_rd_exclus_cos": int(n_rd_tot - p_rd.size)}
    if not sortie["instrument"]["valide"] and not pilote.jouet:
        issue = "instrument non validé"
    elif abs(cos_er) >= A.SEUIL_COS:
        issue = "exclu"
    elif ech_er > A.PART_MAX_ECHECS or ech_rd > A.PART_MAX_ECHECS:
        issue = "non concluant"
        lect["motif_non_concluant"] = "part d'ajustements impossibles au-dessus de 20 %"
    else:
        issue = A.issue_principale(d["ic"][0], d["ic"][1])
    f = lambda x: f"{x:.2f}"
    ic = lambda v: f"{v[0]:.2f} ; {v[1]:.2f}"
    if issue == "exclu":
        lect["phrase"] = A.phrase("exclu", cos=f"{abs(cos_er):.2f}")
    elif issue == "instrument non validé":
        lect["phrase"] = A.phrase(issue, motif=sortie["instrument"].get("motif", ""))
    elif np.isfinite(d["delta"]):
        lect["phrase"] = A.phrase(issue, p_er=f(d["moyenne_plan"]), ic_er=ic(d["ic_plan"]), p_rd=f(d["moyenne_ref"]),
                                  ic_rd=ic(d["ic_ref"]), d=f"{d['delta']:+.2f}", ic_d=ic(d["ic"]))
    else:
        lect["phrase"] = "non concluant : écart incalculable"
    lect["issue"] = issue
    # stabilité : retrait d'un sous-ensemble d'ancres à la fois
    if p_er.size > 2 and p_rd.size > 1:
        dl = [np.nanmean(np.delete(p_er, i)) - np.nanmean(p_rd) for i in range(p_er.size)]
        lect["delta_retrait_d_un_sous_ensemble"] = [float(np.nanmin(dl)), float(np.nanmax(dl))]
    # secondaires (descriptifs, non lus comme décision)
    sec = {}
    rng2 = generateur(graines["bootstrap_ancres"])
    for fam in ("isotrope", "rd_rd", "E_rd", "R_rd", "contrastive", "temoin_positif", "mixte", "moitie_A", "moitie_B", "E_Rpapier", "ER"):
        v = ps(fam)
        if v.size:
            sec[fam] = bootstrap_moyenne(v, B, rng2)
    if p_rd.size and p_er.size:
        m_er = float(np.nanmean(p_er))
        sec["rang_ER_dans_rd"] = float(np.mean(p_rd[np.isfinite(p_rd)] < m_er))
        pc = ps("contrastive")
        if pc.size:
            sec["rang_ER_dans_contrastives"] = float(np.mean(pc[np.isfinite(pc)] < m_er))
    t = [x for x in plans if x["role"] == "temoin" and x["famille"] == "temoin_positif" and x["sous_ensemble"] == 0]
    if t and t[0]["famille"] == "temoin_positif":
        cle = "temoin|temoin_positif|Wealth×Gender|0"
        if cle in pilote.grilles:
            bs = bootstrap_ancres(pilote.angles, pilote.grilles[cle], pilote.cfg["bootstrap"]["B_ancres"], rng2)
            sec["temoin_positif_base_ic_ancres"] = list(intervalle_percentile(np.array([x["p"] for x in bs])))
    lect["secondaires"] = sec
    lect["residu_median_er"] = float(np.nanmedian([x["residu"] for x in lu if x["famille"] == "ER"])) if p_er.size else None
    lect["ic_delta"] = d["ic"]
    lect["temoin_positif"] = sortie.get("temoin_positif")
    lect["audit_symetrie"] = A.declencheurs_symetrie(lect)
    return lect


def principal(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--stimuli", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--racine", default=".")
    ap.add_argument("--jouet", action="store_true")
    a = ap.parse_args(argv)
    racine = Path(a.racine)
    signal.signal(signal.SIGTERM, lever_sur_term)
    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    if not a.jouet and a.prereg is None:
        raise GardeArret("run réel sans préenregistrement scellé : R1 interdit de lancer")
    exiger_config(cfg, Path(a.stimuli))
    stim = ST.exiger_stimuli_conformes(a.stimuli, REF.charger_json()["directions_hachages_invites"])
    chemin_m, man = creer_manifeste(racine, a.run_id, cfg | {"stimuli_chemin": str(a.stimuli)}, TACHES,
                                    entropie=cfg["entropie"], decisif=not a.jouet, prereg=a.prereg,
                                    autoriser_depot_sale=a.jouet, commande=" ".join(["run"] + (argv or sys.argv[1:])))
    pil = Pilote(cfg, stim, a.jouet, generateur(man["graines"]["jouet"]) if a.jouet else None)
    pil.graines = man["graines"]
    dossier = racine / "diag" / a.run_id
    try:
        try:
            sortie = pil.executer()
        except ArretInstrument as e:
            sortie = e.sortie
            sortie["arret_instrument"] = True
        lecture = analyser(pil, sortie, man["graines"]) if not sortie.get("arret_instrument") else {
            "issue": "instrument non validé", "phrase": A.phrase("instrument non validé", motif=sortie["instrument"]["motif"])}
        dossier.mkdir(parents=True, exist_ok=True)
        ch_g = dossier / "grilles.npz"
        np.savez_compressed(ch_g, angles_deg=pil.angles, **{k: v for k, v in pil.grilles.items()})
        sceller(ch_g)
        ecrire_resultat(racine, chemin_m, "plans", {"plans": pil.plans, "blocs_sautes": pil.sautes,
                                                    "grilles_sha256": sha(ch_g)})
        ecrire_resultat(racine, chemin_m, "sorties", sortie)
        ecrire_resultat(racine, chemin_m, "lecture", lecture)
        resume = {"issue": lecture["issue"], "phrase": lecture["phrase"], "duree_s": round(pil.horloge.ecoulee(), 1),
                  "plans": len(pil.plans), "blocs_sautes": len(pil.sautes)}
        ecrire_resultat(racine, chemin_m, "resume", resume)
        print(json.dumps(resume, ensure_ascii=False))
        return 3 if sortie.get("arret_instrument") else 0
    except BaseException as e:
        try:
            dossier.mkdir(parents=True, exist_ok=True)
            ecrire_resultat(racine, chemin_m, "arret", {"motif": motif_d_arret(e), "etape": pil.etape,
                                                        "plans_faits": len(pil.plans), "plans": pil.plans})
        finally:
            relever_term_apres(e)
        raise


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
