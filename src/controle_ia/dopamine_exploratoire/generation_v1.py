"""Génération des réponses et notation, par lots scellés, avec reprise après coupure (exploratoire).

Recette du tableau 6 (p. 19) : température 1,0 ; top_p 0,95 ; un tirage par question ; invite « qwen-boxed » ; 16 000
jetons au plus par appel ; vLLM, `gpu_memory_utilization = 0,75`. Une graine par question, dérivée du manifeste (R9).

Deux générateurs, choisis explicitement (aucun repli silencieux de l'un à l'autre) :
- `GenerateurVllm` : sur la machine (vLLM installé à part, voir l'amorce) ;
- `GenerateurTransformers` : `generate` de transformers, une question à la fois (modèle jouet des essais, ou secours
  déclaré sur la machine).

Chaque ligne de lot garde les jetons de l'invite et de la réponse tels que générés : l'extraction des états internes rejoue
exactement ces jetons (aucun redécoupage du texte).
"""
from __future__ import annotations

import hashlib
from pathlib import Path

from ..gardes import GardeArret
from . import math500_v1
from .stockage_v1 import ecrire_jsonl, etat_lot, lire_jsonl, lots, nom_lot

RECETTE_TABLEAU_6 = {"temperature": 1.0, "top_p": 0.95, "n_tirages": 1, "max_jetons": 16000, "invite": "qwen-boxed",
                     "gpu_memory_utilization": 0.75}
FINS = ("arret", "longueur")


def exiger_recette(recette: dict, *, jouet: bool = False) -> dict:
    """La recette est celle du tableau 6 ; seul le modèle jouet peut réduire `max_jetons` (jamais en mode réel)."""
    for cle in ("temperature", "top_p", "n_tirages", "invite"):
        if recette.get(cle) != RECETTE_TABLEAU_6[cle]:
            raise GardeArret(f"recette de génération : {cle} = {recette.get(cle)!r}, {RECETTE_TABLEAU_6[cle]!r} attendu "
                             "(tableau 6, p. 19)")
    mj = recette.get("max_jetons")
    if isinstance(mj, bool) or not isinstance(mj, int) or mj < 1:
        raise GardeArret(f"max_jetons {mj!r} illisible")
    if not jouet and mj != RECETTE_TABLEAU_6["max_jetons"]:
        raise GardeArret(f"max_jetons = {mj} hors du modèle jouet : 16 000 attendu (tableau 6)")
    return recette


def tronquer_aux_arrets(jetons: list[int], decoder, arrets) -> tuple[list[int], bool]:
    """Coupe la réponse au premier jeton dont le préfixe décodé contient une chaîne d'arrêt (jeton compris)."""
    if not arrets or not any(a in decoder(jetons) for a in arrets):
        return list(jetons), False
    bas, haut = 1, len(jetons)
    while bas < haut:                      # le premier k tel que decoder(jetons[:k]) contient un arrêt (monotone)
        k = (bas + haut) // 2
        if any(a in decoder(jetons[:k]) for a in arrets):
            haut = k
        else:
            bas = k + 1
    return list(jetons[:bas]), True


class GenerateurTransformers:
    """`modele.generate` de transformers, une question à la fois, graine posée par question."""
    nom = "transformers"

    def __init__(self, modele, decoupeur, recette: dict, arrets=(), *, jouet: bool = False):
        self.modele, self.decoupeur, self.arrets = modele, decoupeur, tuple(arrets)
        self.recette = exiger_recette(recette, jouet=jouet)

    def generer(self, invites_ids: list[list[int]], graines: list[int]) -> list[dict]:
        import torch

        if len(invites_ids) != len(graines):
            raise GardeArret("autant de graines que d'invites attendu")
        sorties = []
        appareil = next(self.modele.parameters()).device
        for ids, g in zip(invites_ids, graines):
            torch.manual_seed(int(g))
            x = torch.tensor([ids], dtype=torch.long, device=appareil)
            with torch.no_grad():
                y = self.modele.generate(x, attention_mask=torch.ones_like(x), do_sample=True,
                                         temperature=self.recette["temperature"], top_p=self.recette["top_p"], top_k=0,
                                         max_new_tokens=self.recette["max_jetons"],
                                         eos_token_id=list(self.decoupeur.eos_ids),
                                         pad_token_id=self.decoupeur.pad_id)
            rep = [int(t) for t in y[0, len(ids):].tolist()]
            fin_eos = None
            for k, t in enumerate(rep):
                if t in self.decoupeur.eos_ids:
                    fin_eos = k
                    break
            if fin_eos is not None:
                rep = rep[: fin_eos + 1]
            rep, coupe = tronquer_aux_arrets(rep, self.decoupeur.decoder, self.arrets)
            fin = "arret" if (fin_eos is not None or coupe) else "longueur"
            sorties.append({"jetons": rep, "texte": self.decoupeur.decoder(rep), "fin": fin})
        return sorties


class GenerateurVllm:
    """vLLM (installé à part sur la machine). Paramètres du tableau 6 ; graine par question ; arrêts du gabarit."""
    nom = "vllm"

    def __init__(self, chemin_modele: str, recette: dict, arrets=(), *, longueur_max_modele: int | None = None):
        from vllm import LLM  # absent hors de la machine : erreur franche, aucun repli

        self.recette = exiger_recette(recette)
        self.arrets = tuple(arrets)
        self.llm = LLM(model=chemin_modele, gpu_memory_utilization=self.recette["gpu_memory_utilization"],
                       dtype="bfloat16", seed=0, max_model_len=longueur_max_modele or self.recette["max_jetons"] + 2048)

    def parametres(self, graine: int):
        from vllm import SamplingParams

        return SamplingParams(n=1, temperature=self.recette["temperature"], top_p=self.recette["top_p"],
                              max_tokens=self.recette["max_jetons"], seed=int(graine), stop=list(self.arrets))

    def generer(self, invites_ids: list[list[int]], graines: list[int]) -> list[dict]:
        if len(invites_ids) != len(graines):
            raise GardeArret("autant de graines que d'invites attendu")
        requetes = [{"prompt_token_ids": list(ids)} for ids in invites_ids]
        resultats = self.llm.generate(requetes, [self.parametres(g) for g in graines], use_tqdm=False)
        sorties = []
        for r in resultats:
            o = r.outputs[0]
            if o.finish_reason not in ("stop", "length"):
                raise GardeArret(f"fin de génération inattendue : {o.finish_reason!r}")
            sorties.append({"jetons": [int(t) for t in o.token_ids], "texte": o.text,
                            "fin": "arret" if o.finish_reason == "stop" else "longueur"})
        return sorties


def generer_par_lots(questions: list[dict], textes_invites: dict[str, str], decoupeur, generateur, dossier: Path,
                     taille_lot: int, graine_de) -> dict:
    """Écrit `dossier/lot-NNNNN.jsonl` (scellés). `graine_de(id) -> int`. Reprise : les lots scellés sont sautés.
    Rend le compte des lots écrits et sautés."""
    dossier = Path(dossier)
    ecrits = sautes = 0
    for i, lot in enumerate(lots(questions, taille_lot)):
        final = dossier / f"{nom_lot(i)}.jsonl"
        if etat_lot(final) == "scelle":
            deja = [x["id"] for x in lire_jsonl(final)]
            if deja != [q["id"] for q in lot]:
                raise GardeArret(f"{final.name} : questions différentes de celles du lot {i} (ordre ou jeu changé)")
            sautes += 1
            continue
        invites_ids = [decoupeur.encoder(textes_invites[q["id"]]) for q in lot]
        graines = [int(graine_de(q["id"])) for q in lot]
        sorties = generateur.generer(invites_ids, graines)
        if len(sorties) != len(lot):
            raise GardeArret(f"lot {i} : {len(sorties)} réponses pour {len(lot)} questions")
        lignes = []
        for q, ids, g, s in zip(lot, invites_ids, graines, sorties):
            if s["fin"] not in FINS:
                raise GardeArret(f"fin {s['fin']!r} inconnue")
            lignes.append({"id": q["id"], "graine": g, "jetons_invite": ids, "jetons_reponse": s["jetons"],
                           "n_jetons_reponse": len(s["jetons"]), "texte_reponse": s["texte"], "fin": s["fin"],
                           "invite_sha256": hashlib.sha256(textes_invites[q["id"]].encode("utf-8")).hexdigest(),
                           "generateur": generateur.nom})
        ecrire_jsonl(final, lignes)
        ecrits += 1
    return {"lots_ecrits": ecrits, "lots_sautes": sautes}


def noter_par_lots(questions: list[dict], dossier_generations: Path, dossier_notation: Path) -> dict:
    """Une notation par lot de génération (`lot-NNNNN.jsonl`, scellée) ; reprise comme la génération."""
    attendues = {q["id"]: q["reponse_attendue"] for q in questions}
    lots_g = sorted(Path(dossier_generations).glob("lot-*.jsonl"))
    if not lots_g:
        raise GardeArret(f"aucun lot de génération sous {dossier_generations}")
    ecrits = sautes = 0
    for lg in lots_g:
        final = Path(dossier_notation) / lg.name
        if etat_lot(final) == "scelle":
            sautes += 1
            continue
        lignes = []
        for g in lire_jsonl(lg):
            if g["id"] not in attendues:
                raise GardeArret(f"{lg.name} : question {g['id']!r} absente du jeu")
            n = math500_v1.noter(g["texte_reponse"], attendues[g["id"]], au_plafond=g["fin"] == "longueur")
            lignes.append({"id": g["id"], **n, "reponse_attendue": attendues[g["id"]], "fin": g["fin"]})
        ecrire_jsonl(final, lignes)
        ecrits += 1
    return {"lots_ecrits": ecrits, "lots_sautes": sautes}


def lire_recompenses(dossier_notation: Path) -> dict[str, int]:
    r = {}
    for f in sorted(Path(dossier_notation).glob("lot-*.jsonl")):
        for x in lire_jsonl(f):
            if x["id"] in r:
                raise GardeArret(f"question {x['id']!r} notée deux fois")
            if x["recompense"] not in (0, 1):
                raise GardeArret(f"récompense {x['recompense']!r} non binaire")
            r[x["id"]] = x["recompense"]
    return r
