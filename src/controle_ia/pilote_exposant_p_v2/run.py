"""Lanceur du pilote de l'exposant p, version 2 (instance de calcul ; mode jouet sur processeur pour les essais).

    PYTHONPATH=src python -m controle_ia.pilote_exposant_p_v2.run --config C --stimuli S --run-id ID --prereg P \
        [--revisions acces-hf.txt]
    PYTHONPATH=src python -m controle_ia.pilote_exposant_p_v2.run --config C --stimuli S --run-id ID --jouet

Ordre gelé (préenregistrement, brouillon 2, section « Plan d'analyse ») :
 0. gardes (R1 avant tout, configuration, marqueurs, citations du préenregistrement, stimuli et modèle stylisé) ;
    manifeste ; tokeniseur du modèle lu : choix du jumeau neutre, consigné avant tout passage avant (R-S10) ;
 1. modèle de base : directions publiées, témoin positif Wealth × Gender sur le sous-ensemble 0 (décisif ; identité des
    ancres par la norme et par les rangs des maxima d'axe) → arrêt « instrument non validé », code 3, sorties écrites,
    y compris en mode jouet (tolérances jouet consignées) ;
 2. modèle de base, descriptif : isotropes, Wealth × Gender sur les sous-ensembles 1 à 7, seulement si le temps qui
    reste couvre aussi les blocs décisifs à venir (contre-lecture R2, I5) ;
 3. modèle lu : tokeniseur comparé à celui du modèle de base ; directions, moitiés, interaction ; isotropes (décisif)
    → arrêt code 3 s'ils sortent de la tolérance ;
 4. (E, R) sur les 32 sous-ensembles (sur le seul sous-ensemble 0 si « exclu » ou directions non identifiées) ;
 5. 60 plans de différences aléatoires, plan k sur le sous-ensemble k mod 32 (décisif) ;
 6. si la lecture est possible : Wealth × Gender sur le modèle lu, 32 sous-ensembles (décisif, sensibilité) ; puis,
    qualificatifs (sautés et consignés si le temps manque) : (N, R) sur 32 sous-ensembles, K = 8 plans de référence
    sur les 31 autres sous-ensembles ;
 7. descriptifs ; lecture gelée (`analyse`) ; sorties scellées (`diag/<run>/`).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import signal
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from ..gardes import GardeArret, exiger_sans_signal, lever_sur_term, motif_d_arret, relever_term_apres
from ..manifeste import creer_manifeste, ecrire_resultat, generateur
from ..pilote_exposant_p import ancres as AN
from ..pilote_exposant_p import directions as D
from ..pilote_exposant_p import references as REF
from ..pilote_exposant_p.ajustement import ajuster_plan, bootstrap_ancres, bootstrap_moyenne, intervalle_percentile
from ..pilote_exposant_p.amont import verifier_copie
from ..pilote_exposant_p.run import TokeniseurJouet
from ..scellement import sceller
from . import analyse as A
from . import courbes as C
from . import stimuli as ST

TACHES = ["differences_aleatoires", "bootstrap_difference", "bootstrap_sensibilite", "bootstrap_jumeau",
          "bootstrap_ancres", "jouet"]
DIRS_TEMOIN = ("Gender", "Wealth", "Formal", "Literary", "Age", "Tense", "Sentiment")
FAMILLE_CONTRASTIVE = ("Gender", "Wealth", "Age", "Tense", "Sentiment")
MARQUEUR = re.compile(r"<<[A-Z0-9_]+>>")
CONSTANTES_LECTURE = {
    "delta_equivalence": "DELTA_EQUIVALENCE", "seuil_cos": "SEUIL_COS", "cos_min_moities": "COS_MIN_MOITIES",
    "part_max_echecs": "PART_MAX_ECHECS", "seuil_residu": "SEUIL_RESIDU", "niveau": "NIVEAU", "k_famille": "K_FAMILLE",
    "p_publie_wg": "P_PUBLIE_WG", "intercepts_publies_wg": "INTERCEPTS_PUBLIES_WG",
    "norme_ancres_publiee": "NORME_ANCRES_PUBLIEE", "tol_norme_relative": "TOL_NORME_RELATIVE",
    "rang_min_ancres": "RANG_MIN_ANCRES", "tol_p_identiques": "TOL_P_IDENTIQUES",
    "tol_intercept_identiques": "TOL_INTERCEPT_IDENTIQUES", "intervalle_p_differentes": "INTERVALLE_P_DIFFERENTES",
    "cos_min_directions_publiees": "COS_MIN_DIRECTIONS_PUBLIEES", "intervalle_isotrope": "INTERVALLE_ISOTROPE",
    "demi_largeur_suspecte": "DEMI_LARGEUR_SUSPECTE"}


def progres(**kv) -> None:
    t = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("PROGRES " + t + "".join(f" {k}={str(v).replace(' ', '_')}" for k, v in kv.items()), file=sys.stderr, flush=True)


def sha(chemin: str | Path) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


def _norm(v):
    return list(v) if isinstance(v, (tuple, list)) else v


# --- gardes -------------------------------------------------------------------------------------------------------

def exiger_config(cfg: dict, chemin_stimuli: Path, chemin_config: Path | None = None, prereg_texte: str | None = None,
                  reel: bool = False) -> None:
    """Constantes de lecture du code = configuration ; empreintes citées = fichiers lus ; commit amont ; en run réel :
    aucun marqueur `<<…>>` dans la configuration ni dans les stimuli (dont <<DOI_R9_BIS>> et la vérification humaine),
    et le préenregistrement cite les empreintes de la configuration et des stimuli lus (contre-lecture R2, M4)."""
    lec = cfg["lecture"]
    ecarts = [k for k, nom in CONSTANTES_LECTURE.items() if _norm(lec.get(k)) != _norm(getattr(A, nom))]
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
    if reel:
        textes = {"stimuli": Path(chemin_stimuli).read_text(encoding="utf-8")}
        if chemin_config is not None:
            textes["configuration"] = Path(chemin_config).read_text(encoding="utf-8")
        if prereg_texte is not None:
            textes["préenregistrement"] = prereg_texte
        restes = {k: sorted(set(MARQUEUR.findall(t))) for k, t in textes.items() if MARQUEUR.search(t)}
        if restes:
            raise GardeArret(f"marqueurs restants (dont <<DOI_R9_BIS>> tant que R9-bis n'est pas archivé) : {restes}")
        if prereg_texte is None or chemin_config is None:
            raise GardeArret("run réel : préenregistrement et configuration requis pour vérifier les citations")
        manquants = [n for n, h in (("configuration", sha(chemin_config)), ("stimuli", sha(chemin_stimuli)))
                     if h not in prereg_texte]
        if manquants:
            raise GardeArret(f"le préenregistrement ne cite pas l'empreinte des fichiers lus : {manquants}")


def exiger_meme_lecture(tok_lu, tok_t, ids: np.ndarray, n: int = 50) -> None:
    lot = ids[:n].ravel().tolist()
    if tok_lu.bos_token_id != tok_t.bos_token_id or tok_lu.convert_ids_to_tokens(lot) != tok_t.convert_ids_to_tokens(lot):
        raise GardeArret("le tokeniseur du modèle lu ne lit pas les ancres comme celui du modèle de base")


def exiger_revision(nom: str, revision: str, attendues: dict | None) -> None:
    """Révision relevée par le script d'instance (`acces-hf.txt`) = révision chargée (contre-lecture R2, M6)."""
    if attendues is None:
        return
    if attendues.get(nom) != revision:
        raise GardeArret(f"{nom} : révision chargée {revision} ≠ révision relevée par le script {attendues.get(nom)}")


def lire_revisions(chemin: str | Path) -> dict:
    r = {}
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        if ligne.strip():
            x = json.loads(ligne)
            if x.get("acces") and x.get("revision"):
                r[x["modele"]] = x["revision"]
    return r


def charger_reserve(tokenizer, n: int, revision: str, flux=None) -> tuple[np.ndarray, list[str]]:
    """`ancres.charger_reserve` de la v1, dont le manque d'entrées devient un arrêt consigné (`GardeArret`). `flux` :
    itérable de textes (essais) à la place du flux FineWeb-edu."""
    if flux is None:
        try:
            return AN.charger_reserve(tokenizer, n, revision)
        except RuntimeError as e:
            raise GardeArret(str(e)) from e
    ids: list[list[int]] = []
    lot: list[str] = []

    def vider():
        enc = tokenizer(lot, truncation=True, max_length=AN.LONGUEUR, add_special_tokens=True, padding=False)
        for x in enc["input_ids"]:
            if len(x) >= AN.LONGUEUR and len(ids) < n:
                ids.append(list(x[:AN.LONGUEUR]))

    for t in flux:
        lot.append(t)
        if len(lot) >= AN.TAILLE_LOT_TEXTES:
            vider()
            lot = []
            if len(ids) >= n:
                break
    if lot and len(ids) < n:
        vider()
    if len(ids) < n:
        raise GardeArret(f"flux {AN.JEU} : {len(ids)} entrées de {AN.LONGUEUR} jetons < {n} demandées")
    tab = np.asarray(ids, dtype=np.int64)
    return tab, [tokenizer.decode(x) for x in tab]


class Horloge:
    """Durée projetée : moyenne des plans déjà faits, ou durée prévue par plan (configuration) avant le premier."""

    def __init__(self, duree_max_s: float, duree_plan_prevue_s: float, temps=time.time):
        self.temps = temps
        self.t0 = temps()
        self.max = duree_max_s
        self.prevue = duree_plan_prevue_s
        self.durees: list[float] = []

    def ecoulee(self) -> float:
        return self.temps() - self.t0

    def par_plan(self) -> float:
        return float(np.mean(self.durees)) if self.durees else self.prevue

    def tient(self, n_plans: int) -> bool:
        return self.ecoulee() + n_plans * self.par_plan() <= self.max


class ArretInstrument(Exception):
    def __init__(self, sortie: dict):
        super().__init__(sortie.get("instrument", {}).get("motif", "instrument non validé"))
        self.sortie = sortie


# --- pilote -------------------------------------------------------------------------------------------------------

class Pilote:
    def __init__(self, cfg: dict, stim: dict, jouet: bool, rng_jouet=None, revisions: dict | None = None):
        self.cfg, self.stim, self.jouet = cfg, stim, jouet
        self.rng_jouet = rng_jouet
        self.revisions = revisions
        self.plans: list[dict] = []
        self.grilles: dict[str, np.ndarray] = {}
        self.sautes: list[dict] = []
        self.horloge = Horloge(cfg["plafonds"]["duree_max_s"], cfg["plafonds"]["duree_plan_prevue_s"])
        self.g = cfg["jouet"] if jouet else cfg
        self.angles = np.linspace(0.0, cfg["grille"]["angle_max_deg"], self.g["grille"]["n"])
        self.par = self.g["ancres"]["par_sous_ensemble"]
        self.S = self.g["ancres"]["sous_ensembles"]
        self.paires_iso = cfg["isotropes"]["paires"][: self.g.get("isotropes_paires_max", len(cfg["isotropes"]["paires"]))]
        self.tol = cfg["jouet"].get("tolerances_instrument") if jouet else None
        self.etape = "mise en place"
        self.graines: dict = {}

    def charger_tokeniseur(self, role: str):
        if self.jouet:
            return TokeniseurJouet(self.cfg["jouet"]["modele"]["vocab_size"]), "jouet"
        from huggingface_hub import HfApi
        from transformers import AutoTokenizer

        nom = self.cfg["modeles"][role]
        rev = HfApi().model_info(nom).sha
        exiger_revision(nom, rev, self.revisions)
        return AutoTokenizer.from_pretrained(nom, revision=rev), rev

    def charger(self, role: str):
        import torch

        if self.jouet:
            from transformers import LlamaConfig, LlamaForCausalLM

            torch.manual_seed(1 if role == "temoin" else 2)
            m = LlamaForCausalLM(LlamaConfig(**self.cfg["jouet"]["modele"])).eval()
            return m, TokeniseurJouet(self.cfg["jouet"]["modele"]["vocab_size"]), {"jouet": role}
        from transformers import AutoModelForCausalLM

        nom = self.cfg["modeles"][role]
        tok, rev = self.charger_tokeniseur(role)
        m = AutoModelForCausalLM.from_pretrained(nom, revision=rev, dtype=getattr(torch, self.cfg["dtype"]),
                                                 attn_implementation=self.cfg["attention"]).to("cuda").eval()
        return m, tok, {"nom": nom, "revision": rev, "attention": m.config._attn_implementation,
                        "dtype": str(next(m.parameters()).dtype)}

    def plan(self, modele, role, famille, nom, d1, d2, s, statut="descriptif", garde=True, cos=None):
        from ..pilote_exposant_p.balayage import balayer_plan_ancres
        import torch

        exiger_sans_signal(f"plan {famille}/{nom}/{s}")
        t = time.time()
        sl = AN.sous_ensembles(self.par, self.S)[s]
        g = balayer_plan_ancres(modele, torch.as_tensor(self.ids[sl]), self.acts[sl], d1, d2, self.angles,
                                self.couche_p, self.couche_m, self.cfg["lot_balayage"])
        if not np.all(np.isfinite(g)):
            raise GardeArret(f"grille non finie : {famille}/{nom}/{s}")
        r = ajuster_plan(self.angles, g, self.cfg["seuil_f"], self.cfg["fenetre_deg"])
        dur = time.time() - t
        self.horloge.durees.append(dur)
        self.grilles[f"{role}|{famille}|{nom}|{s}"] = g.astype(np.float32)
        rec = {"role": role, "famille": famille, "nom": nom, "sous_ensemble": s, "cos": cos, "garde": garde,
               "statut": statut, "duree_s": round(dur, 2), **r}
        self.plans.append(rec)
        progres(etape=self.etape, famille=famille, plan=nom, s=s, p=f"{r['p']:.3f}", duree_s=f"{dur:.1f}")
        return rec

    def bloc(self, nom_bloc: str, travaux: list, statut: str, reserve: int = 0) -> bool:
        """Bloc décisif : arrêt s'il ne tient pas dans le plafond. Qualificatif ou descriptif : lancé seulement si le
        temps couvre aussi `reserve` plans décisifs à venir (I5) ; sinon sauté et consigné."""
        if statut == "décisif":
            if not self.horloge.tient(len(travaux)):
                raise GardeArret(f"plafond de durée projeté dépassé avant le bloc décisif {nom_bloc}")
        elif not self.horloge.tient(len(travaux) + reserve):
            self.sautes.append({"bloc": nom_bloc, "plans": len(travaux), "statut": statut,
                                "motif": f"plafond de durée projeté (réserve de {reserve} plans décisifs)"})
            progres(etape=self.etape, bloc_saute=nom_bloc)
            return False
        for f in travaux:
            f()
        return True

    def directions(self, m, tok, noms) -> dict:
        from ..pilote_exposant_p.balayage import activations_textes

        out = {}
        for n, mo in noms:
            a, b = ST.paires(self.stim, n, mo, getattr(self, "neutres", None))
            aa, bb = activations_textes(m, tok, a, self.couche_p), activations_textes(m, tok, b, self.couche_p)
            out[n if mo is None else f"{n}_{mo}"] = D.difference_de_moyennes(aa, bb)
            out[f"_brut_{n if mo is None else f'{n}_{mo}'}"] = (bb.astype(np.float64) - aa).mean(axis=0)
        return out

    def executer(self) -> dict:
        import torch

        from ..pilote_exposant_p.balayage import activations_jetons, couche_de_mesure

        cfg = self.cfg
        sortie: dict = {"jouet": self.jouet, "tolerances_jouet": self.tol}
        # 0. tokeniseur du modèle lu : jumeau neutre choisi avant tout passage avant (R-S10)
        self.etape = "jumeau neutre"
        tok_lu, rev_lu = self.charger_tokeniseur("lu")
        ch = ST.choisir_neutres(self.stim, lambda t: len(tok_lu(t)["input_ids"]))
        self.neutres = ch["choix"] if ch["construit"] else None
        sortie["jumeau"] = ch
        progres(etape=self.etape, retenus=ch["quadruplets_retenus"], construit=ch["construit"])
        # 1. modèle de base
        self.etape = "réserve"
        m_t, tok_t, info_t = self.charger("temoin")
        n_res = self.g["ancres"]["reserve"]
        if self.jouet:
            ids = AN.reserve_jouet(n_res, cfg["jouet"]["modele"]["vocab_size"], self.rng_jouet)
            textes, rev_jeu = [], "jouet"
        else:
            rev_jeu = AN.revision_du_jeu()
            ids, textes = charger_reserve(tok_t, n_res, rev_jeu)
        if self.S * self.par > ids.shape[0]:
            raise GardeArret("réserve plus petite que les ancres demandées")
        sortie["reserve"] = {"n": int(ids.shape[0]), "empreinte_ids": AN.empreinte_ids(ids), "revision_jeu": rev_jeu,
                             "ancres": self.S * self.par, "empreinte_ids_sous_ensemble_0": AN.empreinte_ids(ids[:self.par]),
                             "textes_ancres_sous_ensemble_0": textes[:self.par]}
        self.ids = ids
        self.couche_p = cfg["couche_perturbation"]
        self.couche_m = couche_de_mesure(m_t, cfg["decalage_mesure"])
        sortie["modele_temoin"] = info_t | {"couche_mesure": self.couche_m}
        self.etape = "témoin : directions"
        dt = self.directions(m_t, tok_t, [(n, None) for n in DIRS_TEMOIN])
        pub = REF.charger_directions()
        cos_pub = {n: (D.cosinus(dt[n], pub[n]) if dt[n].shape == pub[n].shape else float("nan")) for n in DIRS_TEMOIN}
        if self.jouet and not self.g.get("controle_directions_publiees", False):
            c_dir = {"valide": True, "cosinus": cos_pub, "regle": "non applicable en mode jouet (dimensions), consigné"}
        else:
            c_dir = A.controle_directions_publiees({n: cos_pub[n] for n in ("Gender", "Wealth")})
        sortie["temoin_directions"] = {"cosinus_avec_publiees": cos_pub, "controle": c_dir}
        n_t = self.g["plans"]["temoin"]["WG_sous_ensembles"] * self.par
        self.acts = activations_jetons(m_t, torch.as_tensor(ids[:n_t]), self.couche_p, cfg["lot_activations"])
        norme0 = float(np.linalg.norm(self.acts[:self.par], axis=1).mean())
        self.etape = "témoin : Wealth × Gender"
        cos_wg = D.cosinus(dt["Wealth"], dt["Gender"])
        tp = []
        self.bloc("temoin_WG", [lambda: tp.append(self.plan(m_t, "temoin", "temoin_positif", "Wealth×Gender", dt["Wealth"],
                                                            dt["Gender"], 0, "décisif", cos=cos_wg))], "décisif")
        r0 = tp[0]
        gp = REF.charger_grilles()["wealth_gender__l2"]
        ident = A.ancres_identiques(norme0, self.grilles["temoin|temoin_positif|Wealth×Gender|0"], gp)
        c_tp = A.controle_temoin_positif(r0["p"], tuple(r0["intercepts"]), ident, self.tol)
        c_tp["norme_ancres_sous_ensemble_0"] = norme0
        sortie["temoin_positif"] = c_tp
        if not A.instrument_valide(c_dir, c_tp):
            sortie["instrument"] = {"valide": False, "motif": "témoin positif ou directions publiées hors tolérance"}
            raise ArretInstrument(sortie)
        S, Mrd = self.S, self.g["differences_aleatoires"]["paires_disjointes_M"]
        P = self.g["plans"]["lu"]
        a_venir = len(self.paires_iso) + S + Mrd + P["WG_sous_ensembles"]
        self.etape = "témoin : descriptifs"
        iso = D.isotropes_papier(cfg["isotropes"]["n"], self.acts.shape[1], cfg["isotropes"]["graine_torch"])
        self.bloc("temoin_isotropes", [lambda i=i, j=j: self.plan(m_t, "temoin", "isotrope", f"iso{i}×iso{j}", iso[i],
                                                                   iso[j], 0, cos=D.cosinus(iso[i], iso[j]))
                                       for i, j in self.paires_iso], "descriptif", reserve=a_venir)
        self.bloc("temoin_WG_sous_ensembles", [lambda s=s: self.plan(m_t, "temoin", "temoin_positif", "Wealth×Gender",
                                                                      dt["Wealth"], dt["Gender"], s, cos=cos_wg)
                                               for s in range(1, self.g["plans"]["temoin"]["WG_sous_ensembles"])],
                  "descriptif", reserve=a_venir)
        del m_t
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        # 3. modèle lu
        self.etape = "lu : directions"
        m, tok, info = self.charger("lu")
        if not self.jouet:
            exiger_meme_lecture(tok, tok_t, ids)
        self.couche_m = couche_de_mesure(m, cfg["decalage_mesure"])
        sortie["modele_lu"] = info | {"couche_mesure": self.couche_m}
        noms = [("E", None), ("R", None), ("E_naif", None), ("E_naif_inverse", None), ("E_echelle", None),
                ("fe_fd", None), ("ce_cd", None), ("fe_ce", None), ("fd_cd", None)] + [(n, None) for n in DIRS_TEMOIN]
        noms += [(n, mo) for mo in ("A", "B") for n in ("E", "R", "Gender", "Wealth")]
        if self.neutres:
            noms.append(("N", None))
        dl = self.directions(m, tok, noms)
        cosl = {f"{x}·{y}": D.cosinus(dl[x], dl[y]) for x, y in (
            ("E", "R"), ("E_naif", "R"), ("E_naif_inverse", "R"), ("E", "E_echelle"), ("E_A", "E_B"), ("R_A", "R_B"),
            ("Gender_A", "Gender_B"), ("Wealth_A", "Wealth_B"), ("R", "Formal"), ("E", "Formal"), ("E", "Literary"),
            ("R", "Literary"), ("Formal", "Literary"), ("fe_fd", "ce_cd"), ("fe_ce", "fd_cd"))}
        if self.neutres:
            cosl.update({"N·R": D.cosinus(dl["N"], dl["R"]), "N·E": D.cosinus(dl["N"], dl["E"])})
        inter = dl["_brut_fe_fd"] - dl["_brut_ce_cd"]          # I = FE − FD − CE + CD (I8)
        sortie["directions_lu"] = {"cosinus": cosl, "interaction": {
            "norme_I_sur_norme_E": float(np.linalg.norm(inter) / np.linalg.norm(dl["_brut_E"])),
            "norme_I_sur_norme_R": float(np.linalg.norm(inter) / np.linalg.norm(dl["_brut_R"])),
            "cos_FE-FD_CE-CD": cosl["fe_fd·ce_cd"], "cos_FE-CE_FD-CD": cosl["fe_ce·fd_cd"]}}
        acts_res = activations_jetons(m, torch.as_tensor(ids), self.couche_p, cfg["lot_activations"])
        rd, idx = D.differences_aleatoires(acts_res, 2 * Mrd, generateur(self.graines["differences_aleatoires"]),
                                           self.g["differences_aleatoires"]["k_moy"])
        self.acts = acts_res[:S * self.par]
        iso = D.isotropes_papier(cfg["isotropes"]["n"], self.acts.shape[1], cfg["isotropes"]["graine_torch"])
        self.etape = "lu : isotropes"
        self.bloc("lu_isotropes", [lambda i=i, j=j: self.plan(m, "lu", "isotrope", f"iso{i}×iso{j}", iso[i], iso[j], 0,
                                                              "décisif", cos=D.cosinus(iso[i], iso[j]))
                                   for i, j in self.paires_iso], "décisif")
        p_iso = np.array([x["p"] for x in self.plans if x["role"] == "lu" and x["famille"] == "isotrope"])
        c_iso = A.controle_isotrope(float(np.nanmean(p_iso)) if np.isfinite(p_iso).any() else float("nan"),
                                    float(np.mean(~np.isfinite(p_iso))), self.tol)
        sortie["isotrope_lu"] = c_iso
        if not c_iso["valide"]:
            sortie["instrument"] = {"valide": False, "motif": "isotropes du modèle lu hors tolérance"}
            raise ArretInstrument(sortie)
        sortie["instrument"] = {"valide": True, "jouet": self.jouet}

        cos_er = cosl["E·R"]
        scos = (self.tol or {}).get("seuil_cos", A.SEUIL_COS)              # jouet seulement (consigné)
        smin = (self.tol or {}).get("cos_min_moities", A.COS_MIN_MOITIES)
        exclu = not math.isfinite(cos_er) or abs(cos_er) >= scos
        identifie = cosl["E_A·E_B"] >= smin and cosl["R_A·R_B"] >= smin
        lisible = not exclu and identifie
        sortie["lisible"] = {"exclu": exclu, "identifie": identifie, "lisible": lisible}
        self.etape = "lu : plan (E, R)"
        n_er = S if lisible else 1
        self.bloc("lu_ER", [lambda s=s: self.plan(m, "lu", "ER", "E×R", dl["E"], dl["R"], s, "décisif", garde=not exclu,
                                                  cos=cos_er) for s in range(n_er)], "décisif")
        self.etape = "lu : différences aléatoires"
        trav = []
        for k in range(Mrd):
            c = D.cosinus(rd[2 * k], rd[2 * k + 1])
            if abs(c) >= A.SEUIL_COS:
                self.plans.append({"role": "lu", "famille": "rd_rd", "nom": f"rd{2*k}×rd{2*k+1}", "sous_ensemble": k % S,
                                   "cos": c, "garde": False, "statut": "décisif", "p": float("nan"), "exclu_cos": True})
                continue
            trav.append(lambda k=k, c=c: self.plan(m, "lu", "rd_rd", f"rd{2*k}×rd{2*k+1}", rd[2 * k], rd[2 * k + 1],
                                                   k % S, "décisif", cos=c))
        self.bloc("lu_rd_rd", trav, "décisif")
        cos_wgl = D.cosinus(dl["Wealth"], dl["Gender"])
        if lisible:
            self.etape = "lu : sensibilité"
            self.bloc("lu_WG", [lambda s=s: self.plan(m, "lu", "temoin_lu", "Wealth×Gender", dl["Wealth"], dl["Gender"], s,
                                                      "décisif", cos=cos_wgl) for s in range(P["WG_sous_ensembles"])],
                      "décisif")
            self.etape = "lu : qualificatifs"
            if self.neutres:
                cos_nr = cosl["N·R"]
                self.bloc("lu_NR", [lambda s=s: self.plan(m, "lu", "NR", "N×R", dl["N"], dl["R"], s, "qualificatif",
                                                          garde=abs(cos_nr) < scos, cos=cos_nr) for s in range(S)],
                          "qualificatif")
            else:
                self.sautes.append({"bloc": "lu_NR", "plans": 0, "statut": "qualificatif", "motif": "jumeau non construit"})
            K = min(self.g.get("famille_K", A.K_FAMILLE), Mrd)
            fam = []
            for k in range(K):
                c = D.cosinus(rd[2 * k], rd[2 * k + 1])
                if abs(c) >= A.SEUIL_COS:
                    continue
                fam += [lambda k=k, s=s, c=c: self.plan(m, "lu", "rd_famille", f"rd{2*k}×rd{2*k+1}", rd[2 * k],
                                                        rd[2 * k + 1], s, "qualificatif", cos=c)
                        for s in range(S) if s != k % S]
            self.bloc("lu_famille", fam, "qualificatif")
        else:
            self.sautes.append({"bloc": "lu_WG, lu_NR, lu_famille", "plans": 0, "statut": "non lus",
                                "motif": "exclu" if exclu else "directions non identifiées"})
        self.etape = "lu : descriptifs"
        desc = []
        for k in range(P["E_rd"]):
            desc.append(("lu_E_rd", lambda k=k: self.plan(m, "lu", "E_rd", f"E×rd{k}", dl["E"], rd[k], 0,
                                                          cos=D.cosinus(dl["E"], rd[k]))))
            desc.append(("lu_R_rd", lambda k=k: self.plan(m, "lu", "R_rd", f"R×rd{k}", dl["R"], rd[k], 0,
                                                          cos=D.cosinus(dl["R"], rd[k]))))
        famc = FAMILLE_CONTRASTIVE[: self.g.get("famille_contrastive_max", len(FAMILLE_CONTRASTIVE))]
        for i in range(len(famc)):
            for j in range(i + 1, len(famc)):
                c = D.cosinus(dl[famc[i]], dl[famc[j]])
                desc.append(("lu_contrastives", lambda i=i, j=j, c=c: self.plan(
                    m, "lu", "contrastive", f"{famc[i]}×{famc[j]}", dl[famc[i]], dl[famc[j]], 0,
                    garde=abs(c) < A.SEUIL_COS, cos=c)))
        for k in range(P["mixtes_rd"]):
            for n in ("Gender", "Wealth"):
                desc.append(("lu_mixtes", lambda k=k, n=n: self.plan(m, "lu", "mixte", f"{n}×rd{k}", dl[n], rd[k], 0,
                                                                     cos=D.cosinus(dl[n], rd[k]))))
        for s in range(P["moities_sous_ensembles"]):
            for mo in ("A", "B"):
                desc.append(("lu_moities", lambda s=s, mo=mo: self.plan(m, "lu", f"moitie_{mo}", f"E_{mo}×R_{mo}",
                                                                        dl[f"E_{mo}"], dl[f"R_{mo}"], s,
                                                                        cos=D.cosinus(dl[f"E_{mo}"], dl[f"R_{mo}"]))))
        for s in range(P["E_Rpapier_sous_ensembles"]):
            desc.append(("lu_E_Rpapier", lambda s=s: self.plan(m, "lu", "E_Rpapier", "E×Formal", dl["E"], dl["Formal"],
                                                               s, cos=cosl["E·Formal"])))
        for nb in dict.fromkeys(b for b, _ in desc):
            self.bloc(nb, [f for b, f in desc if b == nb], "descriptif")
        sortie["rd_indices_sha256"] = hashlib.sha256(np.ascontiguousarray(idx).tobytes()).hexdigest()
        sortie["courbes_W"] = self.courbes()
        return sortie

    def courbes(self) -> dict:
        """Lecture descriptive des courbes d'un axe sur W (R9-bis), sous-ensemble 0 seulement."""
        rd, lus = {}, {}
        for x in self.plans:
            if x["role"] != "lu" or x["sous_ensemble"] != 0 or "p" not in x:
                continue
            g = self.grilles.get(f"lu|{x['famille']}|{x['nom']}|0")
            if g is None:
                continue
            c1, c2 = C.courbes_axes(g)
            n1, n2 = x["nom"].split("×")
            if x["famille"] in ("rd_rd", "rd_famille"):
                rd.setdefault(n1, c1)
                rd.setdefault(n2, c2)
            elif x["famille"] in ("ER", "NR", "temoin_lu"):
                lus.setdefault(n1, c1)
                lus.setdefault(n2, c2)
        return C.lecture(lus, rd, self.angles)


# --- lecture gelée ------------------------------------------------------------------------------------------------

def _p_par_s(lu, famille, garde=True) -> dict[int, float]:
    return {x["sous_ensemble"]: x["p"] for x in lu if x["famille"] == famille and (x.get("garde", True) or not garde)}


def _ref(lu, retirer: int | None = None) -> list[tuple[int, float]]:
    return [(x["sous_ensemble"], x["p"]) for x in lu if x["famille"] == "rd_rd" and x.get("garde", True)
            and x["sous_ensemble"] != retirer]


def _echecs(vals) -> float:
    v = np.asarray(list(vals), dtype=np.float64)
    return float(np.mean(~np.isfinite(v))) if v.size else 1.0


def lire(plans: list[dict], sortie: dict, graines: dict, cfg: dict, jouet: bool) -> dict:
    """Lecture gelée (R1) : issue, phrase, qualificatifs, audit de retrait, secondaires, symétrie."""
    lu = [x for x in plans if x["role"] == "lu"]
    B = cfg["bootstrap"]["B_difference"]
    cosl = sortie["directions_lu"]["cosinus"]
    cos_er = cosl["E·R"]
    cos_m = {"E": cosl["E_A·E_B"], "R": cosl["R_A·R_B"]}
    p_er, p_wg, p_n = _p_par_s(lu, "ER"), _p_par_s(lu, "temoin_lu"), _p_par_s(lu, "NR")
    ref = _ref(lu)
    tol = (cfg.get("jouet", {}).get("tolerances_instrument") or {}) if jouet else {}
    seuils = {"seuil_cos": tol.get("seuil_cos", A.SEUIL_COS), "cos_min_moities": tol.get("cos_min_moities", A.COS_MIN_MOITIES)}

    def calculer(retirer: int | None = None) -> dict:
        per = {s: v for s, v in p_er.items() if s != retirer}
        pwg = {s: v for s, v in p_wg.items() if s != retirer}
        rf = _ref(lu, retirer)
        d = A.bootstrap_sous_ensembles(per, rf, B, generateur(graines["bootstrap_difference"]))
        dwg = A.bootstrap_sous_ensembles(pwg, rf, B, generateur(graines["bootstrap_sensibilite"])) if pwg else None
        issue, brute = A.issue_gelee(instrument_valide=sortie["instrument"]["valide"], cos_er=cos_er,
                                     cos_moities=cos_m, echecs_er=_echecs(per.values()),
                                     echecs_rd=_echecs(v for _, v in rf), ic_delta=d["ic"],
                                     ic_wg=dwg["ic"] if dwg else None, **seuils)
        return {"d": d, "dwg": dwg, "issue": issue, "brute": brute}

    base = calculer()
    d, dwg, issue = base["d"], base["dwg"], base["issue"]
    lect: dict = {"cos_ER": cos_er, "cos_moities": cos_m, "delta": d, "delta_WG": dwg, "issue": issue,
                  "issue_brute": base["brute"], "echecs_ER": _echecs(p_er.values()), "echecs_rd": _echecs(v for _, v in ref),
                  "plans_rd_mesures": len(ref),
                  "plans_rd_exclus_cos": len([x for x in lu if x["famille"] == "rd_rd" and not x.get("garde", True)])}
    f = lambda x: f"{x:.2f}" if math.isfinite(x) else "NaN"
    ic = lambda v: f"{f(v[0])} ; {f(v[1])}"
    vals = dict(p_er=f(d["moyenne_plan"]), ic_er=ic(d["ic_plan"]), p_rd=f(d["moyenne_ref"]), ic_rd=ic(d["ic_ref"]),
                d=(f"{d['delta']:+.2f}" if math.isfinite(d["delta"]) else "NaN"), ic_d=ic(d["ic"]),
                d_wg=(f"{dwg['delta']:+.2f}" if dwg and math.isfinite(dwg["delta"]) else "NaN"),
                ic_wg=ic(dwg["ic"]) if dwg else "NaN ; NaN", brute=base["brute"] or "",
                cos=f(abs(cos_er)), cos_e=f(cos_m["E"]), cos_r=f(cos_m["R"]),
                motif=sortie.get("instrument", {}).get("motif", ""))
    lect["phrase"] = A.PHRASES[issue].format(delta=A.DELTA_EQUIVALENCE, **vals)
    # qualificatifs (issues tranchées seulement)
    if issue in ("au-dessus", "au-dessous", "égal"):
        S = max([x["sous_ensemble"] for x in lu if x["famille"] == "ER"] + [0]) + 1
        moy = []
        for k in range(A.K_FAMILLE):
            nom = f"rd{2*k}×rd{2*k+1}"
            v = [x["p"] for x in lu if x["nom"] == nom and x["famille"] in ("rd_rd", "rd_famille") and x.get("garde", True)]
            if len(v) >= max(2, S // 2):
                moy.append(float(np.nanmean(v)) if np.isfinite(v).any() else float("nan"))
        pos = A.position_famille(d["moyenne_plan"], moy) if moy else {"position": "famille non mesurée",
                                                                       "motif": "bloc de famille non mesuré"}
        lect["famille"] = pos
        q1 = A.phrase_qualif(A.QUALIF_FAMILLE, pos["position"], ip=ic(pos.get("ip", [float("nan")] * 2)),
                             k=pos.get("K", 0), motif=pos.get("motif", ""))
        dn = A.bootstrap_apparie(p_er, p_n, B, generateur(graines["bootstrap_jumeau"])) if p_n else None
        nr_garde = all(x.get("garde", True) for x in lu if x["famille"] == "NR")
        qj = A.qualif_jumeau(dn) if (dn and nr_garde) else "jumeau non mesuré"
        lect["jumeau"] = {"delta_N": dn, "qualificatif": qj, "NR_garde": nr_garde}
        q2 = A.phrase_qualif(A.QUALIF_JUMEAU, qj, d=(f"{dn['delta']:+.2f}" if dn else "NaN"),
                             ic=ic(dn["ic"]) if dn else "NaN ; NaN",
                             motif=("jumeau non construit ou non mesuré" if not dn else "|cos(N, R)| ≥ 0,1"))
        rang = float(np.mean([v < d["moyenne_plan"] for _, v in ref])) if ref else float("nan")
        lect["rang_ER_parmi_plans_rd_un_sous_ensemble"] = rang
        lect["phrase"] += f" {q1} {q2} Rang de p̄(E, R) parmi les {len(ref)} plans de référence pris un à un : {f(rang)}."
        # audit de retrait d'un sous-ensemble (I3)
        instables = []
        for s in sorted(p_er):
            r = calculer(retirer=s)
            if r["issue"] != issue:
                instables.append(f"sans le sous-ensemble {s} : « {r['issue']} »")
        lect["audit_retrait"] = {"recalculs": len(p_er), "differentes": instables}
        lect["instable_au_retrait"] = instables
        if instables:
            lect["phrase"] += " Réserve : issue instable au retrait d'un sous-ensemble."
    # secondaires (descriptifs)
    sec = {}
    rng2 = generateur(graines["bootstrap_ancres"])
    for fam in ("isotrope", "rd_rd", "rd_famille", "E_rd", "R_rd", "contrastive", "temoin_lu", "mixte", "moitie_A",
                "moitie_B", "E_Rpapier", "ER", "NR"):
        v = np.array([x["p"] for x in lu if x["famille"] == fam and x.get("garde", True)], dtype=np.float64)
        if v.size:
            sec[fam] = bootstrap_moyenne(v, B, rng2)
    cle = "temoin|temoin_positif|Wealth×Gender|0"
    sec["identite_ancres"] = (sortie.get("temoin_positif") or {}).get("identite")
    lect["secondaires"] = sec
    lect["residu_median_er"] = (float(np.nanmedian([x["residu"] for x in lu if x["famille"] == "ER"]))
                                if p_er else None)
    lect["ic_delta"] = d["ic"]
    lect["temoin_positif"] = sortie.get("temoin_positif")
    lect["audit_symetrie"] = A.declencheurs_symetrie(lect)
    lect["_cle_temoin"] = cle
    return lect


def analyser(pilote: Pilote, sortie: dict, graines: dict) -> dict:
    lect = lire(pilote.plans, sortie, graines, pilote.cfg, pilote.jouet)
    cle = lect.pop("_cle_temoin")
    if cle in pilote.grilles:
        bs = bootstrap_ancres(pilote.angles, pilote.grilles[cle], pilote.cfg["bootstrap"]["B_ancres"],
                              generateur(graines["bootstrap_ancres"]))
        lect["secondaires"]["temoin_positif_base_ic_ancres"] = list(intervalle_percentile(np.array([x["p"] for x in bs])))
    return lect


def principal(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--stimuli", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    ap.add_argument("--racine", default=".")
    ap.add_argument("--revisions", default=None, help="acces-hf.txt du script d'instance (révisions relevées)")
    ap.add_argument("--jouet", action="store_true")
    a = ap.parse_args(argv)
    if not a.jouet and a.prereg is None:                    # R1, avant tout effet de bord (M5)
        raise GardeArret("run réel sans préenregistrement scellé : R1 interdit de lancer")
    racine = Path(a.racine)
    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    prereg_texte = Path(a.prereg).read_text(encoding="utf-8") if a.prereg else None
    exiger_config(cfg, Path(a.stimuli), Path(a.config), prereg_texte, reel=not a.jouet)
    stim = ST.charger(a.stimuli)
    pb = ST.problemes_stimuli(stim, REF.charger_json()["directions_hachages_invites"])
    if pb:
        raise GardeArret(f"{a.stimuli} non conforme à ses règles de construction : " + " ; ".join(pb[:10]))
    tirages = cfg["jouet"].get("stylise_tirages", ST.TIRAGES_STYLISE) if a.jouet else ST.TIRAGES_STYLISE
    stylise = ST.exiger_modele_stylise(stim["quadruplets"], tirages=tirages)
    revisions = lire_revisions(a.revisions) if a.revisions else None
    signal.signal(signal.SIGTERM, lever_sur_term)
    chemin_m, man = creer_manifeste(racine, a.run_id, cfg | {"stimuli_chemin": str(a.stimuli)}, TACHES,
                                    entropie=cfg["entropie"], decisif=not a.jouet, prereg=a.prereg,
                                    autoriser_depot_sale=a.jouet, commande=" ".join(["run"] + (argv or sys.argv[1:])))
    pil = Pilote(cfg, stim, a.jouet, generateur(man["graines"]["jouet"]) if a.jouet else None, revisions)
    pil.graines = man["graines"]
    dossier = racine / "diag" / a.run_id
    try:
        try:
            sortie = pil.executer()
        except ArretInstrument as e:
            sortie = e.sortie
            sortie["arret_instrument"] = True
        sortie["modele_stylise"] = {"tirages": tirages, **stylise}
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
                  "plans": len(pil.plans), "blocs_sautes": len(pil.sautes), "jouet": a.jouet}
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
