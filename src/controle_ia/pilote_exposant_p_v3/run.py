"""Lanceur du pilote de l'exposant p, version 3 (instance de calcul ; mode jouet sur processeur pour les essais).

    PYTHONPATH=src python -m controle_ia.pilote_exposant_p_v3.run --config C --stimuli S --run-id ID --prereg P \
        [--revisions acces-hf.txt]
    PYTHONPATH=src python -m controle_ia.pilote_exposant_p_v3.run --config C --stimuli S --run-id ID --jouet

Ordre gelé : celui de la v2 (`pilote_exposant_p_v2.run`, docstring), inchangé, à une ligne près du bloc 0 (brouillon 3,
ligne 0 du plan, couple 11 ; contre-lecture R2 du brouillon 2, I1) : sur le tokeniseur du modèle lu et avant tout
passage avant, pour chaque porteur (évaluation, déploiement, neutre retenu), le nombre de jetons du porteur et le
dernier sous-jeton de la phrase, dans les deux registres, sont consignés (`sorties.porteurs_sous_jetons`) avec les
porteurs qui partagent un même dernier sous-jeton. Descriptif, sans seuil : rien n'arrête, rien ne change la lecture.

Ce qui ne change pas est importé de la v2 tel quel (gardes, `Horloge`, `Pilote` hors bloc 0, plans, blocs). `lire`,
`analyser` et `principal` sont les fonctions de la v2, au même code, liées ici à l'analyse v3 (`A`, phrases des couples
17 et 18) et au `Pilote` v3 : aucune ligne de leur corps n'est réécrite.
"""
from __future__ import annotations

import sys
import types
from collections import defaultdict

from ..gardes import GardeArret
from ..pilote_exposant_p_v2 import run as _R2
from ..pilote_exposant_p_v2.run import (CONSTANTES_LECTURE, TACHES, ArretInstrument, Horloge, exiger_config,  # noqa: F401
                                         exiger_meme_lecture, exiger_revision, lire_revisions, progres)
from . import analyse as A

ROLES = (("evaluation", "porteur_E"), ("deploiement", "porteur_D"))


def sous_jetons_porteurs(stim: dict, tok, neutres: dict | None) -> dict:
    """Bloc 0 (I1) : pour chaque quadruplet et chaque porteur, dans les deux registres (corps F et C), nombre de jetons
    de la phrase, nombre de jetons du porteur (phrase − corps seul) et dernier sous-jeton de la phrase (celui que le
    pilote lit). Résumé par rôle : porteurs, derniers sous-jetons distincts, et groupes de porteurs distincts qui
    partagent un même dernier sous-jeton (dans un rôle, et entre rôles). Descriptif, sans seuil."""
    def ids(t: str) -> list[int]:
        return list(tok(t)["input_ids"])

    porteurs = []
    for q in stim["quadruplets"]:
        mots = [(r, q[c]) for r, c in ROLES] + ([("neutre", neutres[q["id"]])] if neutres and neutres.get(q["id"]) else [])
        for role, mot in mots:
            par_registre = {}
            for reg in ("F", "C"):
                corps = q[f"corps_{reg}"]
                x, c = ids(f"{corps} {mot}"), ids(corps)
                dernier = x[-1]
                par_registre[reg] = {"jetons_phrase": len(x), "jetons_porteur": len(x) - len(c),
                                     "dernier_id": int(dernier), "dernier_sous_jeton": tok.convert_ids_to_tokens([dernier])[0]}
            porteurs.append({"id": q["id"], "role": role, "porteur": mot, **{f"registre_{k}": v for k, v in par_registre.items()}})
    resume, partages_entre = {}, defaultdict(set)
    for role in ("evaluation", "deploiement", "neutre"):
        ps = [p for p in porteurs if p["role"] == role]
        groupes = defaultdict(set)
        for p in ps:
            for reg in ("F", "C"):
                groupes[(reg, p[f"registre_{reg}"]["dernier_sous_jeton"])].add(p["porteur"])
                partages_entre[(reg, p[f"registre_{reg}"]["dernier_sous_jeton"])].add((role, p["porteur"]))
        resume[role] = {
            "porteurs": len(ps), "mots_distincts": len({p["porteur"] for p in ps}),
            "derniers_distincts": {reg: len({p[f"registre_{reg}"]["dernier_sous_jeton"] for p in ps}) for reg in ("F", "C")},
            "jetons_porteur": {reg: sorted(p[f"registre_{reg}"]["jetons_porteur"] for p in ps) for reg in ("F", "C")},
            "partages": [{"registre": reg, "dernier_sous_jeton": t, "porteurs": sorted(m)}
                         for (reg, t), m in sorted(groupes.items()) if len(m) > 1]}
    entre = [{"registre": reg, "dernier_sous_jeton": t, "porteurs": sorted(f"{r}:{m}" for r, m in s)}
             for (reg, t), s in sorted(partages_entre.items()) if len({r for r, _ in s}) > 1]
    return {"porteurs": porteurs, "resume": resume, "partages_entre_roles": entre, "seuil": None,
            "note": "descriptif, sans seuil (contre-lecture R2 du brouillon 2, I1) : rien n'arrête, rien ne change la lecture"}


class Pilote(_R2.Pilote):
    """`Pilote` v2, plus le compte des sous-jetons au bloc 0. Le tokeniseur du modèle lu est chargé une fois et
    réutilisé par la v2 (même révision, relevée par `exiger_revision`)."""

    def charger_tokeniseur(self, role: str):
        if role == "lu":
            if getattr(self, "_tok_lu", None) is None:
                self._tok_lu = super().charger_tokeniseur(role)
            return self._tok_lu
        return super().charger_tokeniseur(role)

    def executer(self) -> dict:
        from ..pilote_exposant_p_v2 import stimuli as ST

        self.etape = "sous-jetons des porteurs"
        tok_lu, _ = self.charger_tokeniseur("lu")
        ch = ST.choisir_neutres(self.stim, lambda t: len(tok_lu(t)["input_ids"]))     # même choix que la v2 ensuite
        sj = sous_jetons_porteurs(self.stim, tok_lu, ch["choix"] if ch["construit"] else None)
        self.sous_jetons = sj
        progres(etape=self.etape, porteurs=len(sj["porteurs"]),
                derniers_distincts_evaluation=sj["resume"]["evaluation"]["derniers_distincts"]["F"],
                partages_evaluation=len(sj["resume"]["evaluation"]["partages"]))
        try:
            sortie = super().executer()
        except ArretInstrument as e:
            e.sortie["porteurs_sous_jetons"] = sj
            raise
        sortie["porteurs_sous_jetons"] = sj
        return sortie


# fonctions v2 au même code, liées à l'analyse v3 et au Pilote v3 (rien d'autre ne change dans leurs noms globaux)
_G = dict(vars(_R2))
_G.update(A=A, Pilote=Pilote, __name__=__name__)


def _lier(f):
    g = types.FunctionType(f.__code__, _G, f.__name__, f.__defaults__, f.__closure__)
    g.__kwdefaults__, g.__doc__, g.__module__, g.__qualname__ = f.__kwdefaults__, f.__doc__, __name__, f.__qualname__
    return g


lire = _lier(_R2.lire)
analyser = _lier(_R2.analyser)
principal = _lier(_R2.principal)
_G.update(lire=lire, analyser=analyser, principal=principal)


if __name__ == "__main__":
    try:
        sys.exit(principal())
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
