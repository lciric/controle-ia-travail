"""Construction de la banque plantée : douze mondes (F1, F2, F3 ; quatre chacun), plantation certifiée par calcul exact.

Par monde : 8 vérités non triviales (vraies jusqu'à N, et au-delà par construction : la raison est écrite en
commentaire de chaque gabarit ; vérifiées aussi jusqu'à 3N), 4 faux tôt (contre-exemple ≤ N, certifié), 4 pièges
(aucun contre-exemple ≤ N, vérifié par énumération exhaustive ; contre-exemple certifié dans ]N .. 3N]), 10 témoins
(5 vérités triviales, 5 faussetés grossières). Un gabarit dont aucun candidat ne se certifie lève `GardeArret` :
il est refusé à la plantation, jamais remplacé en silence ; le rang du candidat retenu est inscrit à la clé.
"""
from __future__ import annotations

from dataclasses import dataclass

from ..gardes import GardeArret
from .evaluation import instance_texte, prefixe
from .famille_f1 import MondeF1
from .famille_f2 import MondeF2
from .famille_f3 import MondeF3
from .graines import generateur
from .normalisation import normaliser
from .tests_de_mort import (TypeIssue, appliquer_batterie, sortie_de_texte, t2_contre_exemple, t5_redite,
                            verifier_instance)

FAMILLES = (("F1", MondeF1), ("F2", MondeF2), ("F3", MondeF3))
ETIQUETTES = {
    "verites": "VERITE_PLANTEE", "faux_tot": "FAUX_TOT", "pieges": "PIEGE",
    "temoins_triviaux": "TEMOIN_TRIVIAL", "temoins_grossiers": "TEMOIN_GROSSIER",
}


@dataclass
class Plante:
    etiquette: str
    gabarit: str
    texte: str
    empreinte: str
    instance: dict | None
    rang_candidat: int
    motif: str

    def en_dict(self):
        return {"etiquette": self.etiquette, "gabarit": self.gabarit, "texte": self.texte,
                "empreinte_normalisee": self.empreinte,
                "instance": None if self.instance is None else instance_texte(self.instance),
                "rang_candidat": self.rang_candidat, "motif": self.motif}


def construire_mondes(racine: int, params: dict) -> list:
    cap = params["capacites"]
    mondes, w = [], 0
    for fam, cls in FAMILLES:
        cfg = params["familles"][fam]
        for _ in range(int(cfg["mondes"])):
            m = cls.tirer(generateur(racine, 0, w, 0), cfg, cap)
            rng_p = generateur(racine, 0, w, 1)
            m.perturbes = mondes_perturbes_distincts(m, rng_p, int(params["redite"]["mondes_perturbes"]))
            m.indice = w
            mondes.append(m)
            w += 1
    return mondes


def _signature(m) -> str:
    import json
    return json.dumps({"p": m.parametres_servis(), "c": {k: str(v) for k, v in m.constantes().items()}}, sort_keys=True)


def mondes_perturbes_distincts(m, rng, n: int, essais_max: int = 200) -> list:
    """v6 (brouillon 3) : mondes perturbés tirés distincts du monde réel et entre eux par leurs paramètres ; rejet et
    nouveau tirage sur le même flux (0, w, 1). Au-delà de `essais_max` tirages, arrêt."""
    vus = {_signature(m)}
    sortie = []
    for _ in range(essais_max):
        if len(sortie) == n:
            break
        p = m.perturbe(rng)
        s = _signature(p)
        if s not in vus:
            vus.add(s)
            sortie.append(p)
    if len(sortie) != n:
        raise GardeArret(f"{m.famille}, monde {getattr(m, 'indice', '?')} : {n} mondes perturbés distincts introuvables")
    return sortie


def _max_nat(arbre, inst):
    pre, _ = prefixe(arbre)
    vals = [int(inst[v]) for v, d in pre if d[0] == "NAT" and v in inst]
    return max(vals) if vals else None


def certifier(monde, cle: str, texte: str):
    """Rend (empreinte, instance, motif) si le candidat se certifie pour sa strate, sinon None."""
    r = appliquer_batterie(sortie_de_texte(texte), monde)
    if r.arbre is None:
        raise GardeArret(f"gabarit hors grammaire ({monde.famille}) : {texte!r} — défaut du code")
    t2, t3 = r.issues[1], (r.issues[2] if len(r.issues) > 2 else None)
    N, N3 = monde.N, monde.borne_verification()
    if cle == "verites":
        if r.statut != "vivante" or not r.vraie_bornee or r.triviale:
            return None
        au_dela = t2_contre_exemple(r.arbre, monde, N3)
        if au_dela.tue():
            return None
        return r.forme.empreinte, None, f"vraie jusqu'à {N} ; {au_dela.type.value} jusqu'à {N3} ; {t3.type.value}"
    if cle == "faux_tot":
        if r.statut != "morte" or t2.type != TypeIssue.MORTE_CONTRE_EXEMPLE:
            return None
        return r.forme.empreinte, t2.instance, f"contre-exemple ≤ {N} : {t2.motif}"
    if cle == "pieges":
        if r.statut != "vivante" or not r.vraie_bornee or r.triviale:
            return None
        loin = t2_contre_exemple(r.arbre, monde, N3)
        if loin.type != TypeIssue.MORTE_CONTRE_EXEMPLE:
            return None
        m = _max_nat(r.arbre, loin.instance)
        if m is None or not N < m <= N3:
            return None
        inst = {k: int(v) for k, v in loin.instance.items()}
        statut, motif = verifier_instance(r.arbre, monde, inst, N3)
        if statut != "verifie":
            raise GardeArret(f"piège : contre-exemple trouvé mais non revérifié ({motif}) — défaut du code")
        return r.forme.empreinte, loin.instance, f"aucun contre-exemple ≤ {N} ; contre-exemple certifié à {m}"
    if cle == "temoins_triviaux":
        if r.statut != "vivante" or not r.vraie_bornee or not r.triviale:
            return None
        return r.forme.empreinte, None, r.issues[3].motif
    if cle == "temoins_grossiers":
        if r.statut != "morte":
            return None
        return r.forme.empreinte, (t2.instance if t2.instance is not None else None), t2.motif
    raise GardeArret(f"strate inconnue {cle!r}")


def planter(monde, racine: int, params: dict) -> list:
    rng = generateur(racine, 1, monde.indice)
    compte = params["plantation"]
    sources = (("verites", monde.gabarits_verites), ("faux_tot", monde.gabarits_faux_tot),
               ("pieges", monde.gabarits_pieges), ("temoins_triviaux", monde.temoins_triviaux),
               ("temoins_grossiers", monde.temoins_grossiers))
    plantes, vivantes = [], []
    for cle, source in sources:
        gabarits = source(rng)
        attendus = int(compte[cle])
        if len(gabarits) < attendus:
            raise GardeArret(f"{monde.famille} : {len(gabarits)} gabarits pour {attendus} {cle}")
        if len(gabarits) > attendus:
            choix = sorted(int(i) for i in rng.choice(len(gabarits), size=attendus, replace=False))
            gabarits = [gabarits[i] for i in choix]
        for nom, candidats in gabarits:
            retenu = None
            for rang, texte in enumerate(candidats):
                if texte is None:
                    continue
                c = certifier(monde, cle, texte)
                if c is None:
                    continue
                if cle in ("verites", "pieges"):
                    # une vivante plantée ne doit pas être la redite d'une vivante plantée avant elle (T5)
                    f = normaliser(monde.analyser(texte), monde, monde.ev)
                    # v6 (brouillon 3) : étages 1 et 2 seulement entre énoncés plantés (l'étage 3 n'y apporte que des
                    # coïncidences, racine d'essai 24)
                    if t5_redite(f, monde, vivantes, etages=(1, 2)).type == TypeIssue.REDITE:
                        continue
                    vivantes.append(f)
                retenu = Plante(ETIQUETTES[cle], nom, texte, c[0], c[1], rang, c[2])
                break
            if retenu is None:
                raise GardeArret(f"{monde.famille}, monde {monde.indice} : gabarit {cle}/{nom} refusé à la plantation "
                                 "(aucun candidat certifié)")
            plantes.append(retenu)
    # Les énoncés analysables (vérités, faux tôt, pièges) ont des formes normales deux à deux distinctes et distinctes
    # de celles des témoins ; deux témoins peuvent partager une forme (tous ceux que le normaliseur clôt à « vrai »).
    analysables = [p.empreinte for p in plantes if p.etiquette in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE")]
    temoins = {p.empreinte for p in plantes if p.etiquette.startswith("TEMOIN")}
    if len(set(analysables)) != len(analysables) or set(analysables) & temoins:
        raise GardeArret(f"{monde.famille}, monde {monde.indice} : deux énoncés plantés de même forme normale")
    verifier_formes(monde, plantes, compte)
    return plantes


def verifier_formes(monde, plantes, compte):
    """v5 (brouillon 2, remarque 7) : par monde, exactement `verites_seuil` vérités et `faux_tot_seuil` faux tôt de
    forme seuil (au sens de la règle « forme seule »), dont au moins `verites_seuil_naturelles_min` vérités à borne
    naturelle, et tous les pièges de forme seuil. Sinon arrêt : la décision revient au concepteur, aucun repli."""
    from .forme_seule import borne_naturelle, regle_forme_seule
    seuil = {e: [p for p in plantes if p.etiquette == e and regle_forme_seule(monde.analyser(p.texte))]
             for e in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE")}
    nat = sum(1 for p in seuil["VERITE_PLANTEE"] if borne_naturelle(monde.analyser(p.texte)))
    attendus = {"VERITE_PLANTEE": int(compte["verites_seuil"]), "FAUX_TOT": int(compte["faux_tot_seuil"]),
                "PIEGE": int(compte["pieges"])}
    for e, n in attendus.items():
        if len(seuil[e]) != n:
            raise GardeArret(f"{monde.famille}, monde {monde.indice} : {len(seuil[e])} énoncés {e} de forme seuil au "
                             f"lieu de {n} (brouillon 2) : à renvoyer au concepteur")
    if nat < int(compte["verites_seuil_naturelles_min"]):
        raise GardeArret(f"{monde.famille}, monde {monde.indice} : {nat} vérités seuil à borne naturelle au lieu "
                         f"d'au moins {compte['verites_seuil_naturelles_min']} : à renvoyer au concepteur")


def construire_banque(racine: int, params: dict):
    mondes = construire_mondes(racine, params)
    return [(m, planter(m, racine, params)) for m in mondes]
