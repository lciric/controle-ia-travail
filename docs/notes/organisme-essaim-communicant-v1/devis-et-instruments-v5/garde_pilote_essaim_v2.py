#!/usr/bin/env python3
"""Gardes d'arrêt dures du pilote P-std de l'essaim — v2 (contre-lecture de la v3). Bibliothèque standard seule ; aucun appel.

Reprend les plafonds, le plan et la borne de `garde_pilote_essaim_v1.py` (valeurs inchangées), avec ces changements :
- **plan, prix et plafond gelés** : `PLAN_SHA256` (empreinte du plan P-std canonique), `PRIX_GELES` = tarif de Kimi de la table
  (2,0 ; 10,0 USD par million, lu par `calcul_devis_essaim_v4.tarifs()` et comparé), plafond ≤ borne ; tout écart refusé (24) ;
- **échecs** (relancés ou abandonnés) comptés dans un seul budget de ⌊10 % × 744⌋ = 74 (A10) ; une relance doit être
  l'entrée du plan identique en tout (A9) ;
- **usage absent, illisible ou négatif** : l'appel est compté à sa réserve entière, puis arrêt 16 (A7) ;
- **toute exception après l'envoi** : l'appel est compté à sa réserve entière, puis arrêt 17 (A5) ;
- l'état initial (dépense, appels réglés, échecs, messages) vient du registre persistant (`registre_depense_v1`), jamais de zéro (A2).
"""
import hashlib
import json
import math

PLAFOND_SORTIE = {"proposeur": 24000, "message": 2000}
PLAFOND_SORTIE_ABSOLU = 24000
PLAFOND_ENTREE_JETONS = {"proposeur": 20000 + 3200, "message": 6000}
OCTETS_PAR_JETON_HAUT = 2.8
PLAFOND_ENTREE_OCTETS = {r: int(PLAFOND_ENTREE_JETONS[r] * OCTETS_PAR_JETON_HAUT) for r in PLAFOND_SORTIE}
SURCOUT_FORMAT = 256
MESSAGES_PAR_MONDE = 12
PART_ECHECS = 0.10
PRIX_GELES = (2.0, 10.0)
CODES = {10: "sortie", 11: "entrée", 12: "messages", 13: "échecs et relances", 14: "dépense", 15: "plan", 16: "facturation hors borne",
         17: "erreur après envoi", 21: "registre absent", 22: "registre altéré", 23: "course close", 24: "configuration refusée"}
APPELS_PAR_GENERATION = {"a": {"proposeur": 8, "message": 4}, "c": {"proposeur": (9, 9, 8), "message": 0}}


class ArretCourse(Exception):
    def __init__(self, code, detail):
        super().__init__(f"arrêt {code} ({CODES[code]}) : {detail}")
        self.code, self.garde, self.detail = code, CODES[code], detail


def plan_pstd(mondes=12, generations=3, bras=("a", "c")):
    plan = []
    for w in range(mondes):
        for b in bras:
            for g in range(1, generations + 1):
                np_ = APPELS_PAR_GENERATION[b]["proposeur"]
                np_ = np_[g - 1] if isinstance(np_, tuple) else np_
                for i in range(np_):
                    plan.append({"id": f"w{w:02d}-{b}-g{g}-proposeur-{i:02d}", "monde": w, "bras": b, "generation": g, "role": "proposeur"})
                for i in range(APPELS_PAR_GENERATION[b]["message"]):
                    plan.append({"id": f"w{w:02d}-{b}-g{g}-message-{i:02d}", "monde": w, "bras": b, "generation": g, "role": "message"})
    return plan


def empreinte_plan(plan):
    return hashlib.sha256(json.dumps(plan, sort_keys=True, separators=(",", ":")).encode()).hexdigest()




def cout(entree, sortie, prix):
    return (entree * prix[0] + sortie * prix[1]) / 1e6


def reserve_dure(role, octets, max_tokens, prix):
    return cout(octets + SURCOUT_FORMAT, max_tokens, prix)


def borne_pire(plan, prix):
    aux_plafonds = sum(cout(PLAFOND_ENTREE_JETONS[a["role"]], PLAFOND_SORTIE[a["role"]], prix) for a in plan)
    rmax = max(reserve_dure(r, PLAFOND_ENTREE_OCTETS[r], PLAFOND_SORTIE[r], prix) for r in PLAFOND_SORTIE)
    echecs = math.floor(PART_ECHECS * len(plan))
    exces = max(reserve_dure(r, PLAFOND_ENTREE_OCTETS[r], PLAFOND_SORTIE[r], prix) - cout(PLAFOND_ENTREE_JETONS[r], PLAFOND_SORTIE[r], prix)
                for r in PLAFOND_SORTIE)
    total = aux_plafonds + echecs * rmax + exces
    return {"appels_du_plan": len(plan), "echecs_au_plus": echecs, "appels_au_plus": len(plan) + echecs,
            "aux_plafonds_de_jetons_usd": round(aux_plafonds, 4), "reserve_dure_max_usd": round(rmax, 6),
            "echecs_usd": round(echecs * rmax, 4), "exces_d_un_appel_usd": round(exces, 6), "pire_usd": round(total, 4)}


def parametres_geles(plafond):
    return {"plan_sha256": PLAN_SHA256, "prix_usd_par_million": list(PRIX_GELES), "plafond_depense_usd": plafond,
            "plafonds": {"sortie": PLAFOND_SORTIE, "entree_jetons": PLAFOND_ENTREE_JETONS, "entree_octets": PLAFOND_ENTREE_OCTETS,
                         "surcout_format": SURCOUT_FORMAT, "messages_par_monde": MESSAGES_PAR_MONDE, "part_echecs": PART_ECHECS}}


class Garde:
    def __init__(self, plan, prix, plafond_depense, etat=None):
        self.plan, self.prix = list(plan), tuple(prix)
        self.borne = borne_pire(self.plan, self.prix)
        self.plafond_depense = float(plafond_depense)
        etat = etat or {"depense": 0.0, "regles": [], "echecs": 0}
        self.depense = float(etat["depense"])
        regles = list(etat["regles"])
        if regles != [a["id"] for a in self.plan[:len(regles)]]:
            raise ArretCourse(22, "appels réglés du registre hors de l'ordre du plan")
        self.prochain = len(regles)
        self.echecs = int(etat["echecs"])
        self.echecs_max = math.floor(PART_ECHECS * len(self.plan))
        self.messages = {}
        for a in self.plan[:self.prochain]:
            if a["role"] == "message":
                self.messages[a["monde"]] = self.messages.get(a["monde"], 0) + 1
        self.en_cours = None
        self.a_relancer = None
        if self.echecs > self.echecs_max:
            raise ArretCourse(13, f"échecs du registre {self.echecs} > {self.echecs_max}")

    def relance_due(self, appel):
        self.a_relancer = appel

    def avant(self, appel, texte, max_tokens):
        if self.en_cours is not None:
            raise ArretCourse(15, f"{appel.get('id')} soumis avant la clôture de {self.en_cours[0]['id']}")
        relance = self.a_relancer is not None
        if relance:
            if appel != self.a_relancer:
                raise ArretCourse(15, f"relance de {appel.get('id')} différente de l'entrée du plan attendue {self.a_relancer['id']}")
        elif self.prochain >= len(self.plan) or appel != self.plan[self.prochain]:
            attendu = self.plan[self.prochain]["id"] if self.prochain < len(self.plan) else "aucun"
            raise ArretCourse(15, f"appel {appel.get('id')} hors plan (attendu {attendu})")
        role = appel["role"]
        if not isinstance(max_tokens, int) or isinstance(max_tokens, bool) or max_tokens <= 0 \
                or max_tokens > PLAFOND_SORTIE[role] or max_tokens > PLAFOND_SORTIE_ABSOLU:
            raise ArretCourse(10, f"max_tokens {max_tokens!r} hors plafond {PLAFOND_SORTIE[role]} ({role})")
        octets = len(texte.encode("utf-8"))
        if octets > PLAFOND_ENTREE_OCTETS[role]:
            raise ArretCourse(11, f"entrée de {octets} octets > plafond {PLAFOND_ENTREE_OCTETS[role]} ({role})")
        if role == "message" and not relance:
            n = self.messages.get(appel["monde"], 0) + 1
            if n > MESSAGES_PAR_MONDE:
                raise ArretCourse(12, f"message {n} du monde {appel['monde']} (plafond {MESSAGES_PAR_MONDE})")
        res = reserve_dure(role, octets, max_tokens, self.prix)
        if self.depense + res > self.plafond_depense + 1e-12:
            raise ArretCourse(14, f"dépense {self.depense:.6f} + réserve {res:.6f} > plafond {self.plafond_depense:.6f} USD")
        self.en_cours = (appel, res, octets, max_tokens, relance)
        self.a_relancer = None
        return res

    def _fermer(self):
        a = self.en_cours
        self.en_cours = None
        return a

    def compter_reserve(self):
        """Appel ouvert compté à sa réserve entière (exception, usage anormal). Rend la réserve."""
        appel, res, _, _, _ = self._fermer()
        self.depense += res
        return appel, res

    def apres(self, appel, usage):
        if self.en_cours is None or self.en_cours[0] != appel:
            raise ArretCourse(15, f"clôture de {appel.get('id')} sans appel ouvert")
        _, res, octets, max_tokens, relance = self.en_cours
        try:
            e, s = usage["entree"], usage["sortie"]
            if not all(isinstance(x, int) and not isinstance(x, bool) for x in (e, s)) or e < 0 or s < 0:
                raise ValueError("usage non entier ou négatif")
        except (KeyError, TypeError, ValueError) as ex:
            self.compter_reserve()
            raise ArretCourse(16, f"usage anormal pour {appel['id']} : {usage!r} ({ex}) — compté à la réserve {res:.6f}")
        self._fermer()
        c = cout(e, s, self.prix)
        self.depense += c
        self.prochain += 1
        if appel["role"] == "message":
            self.messages[appel["monde"]] = self.messages.get(appel["monde"], 0) + 1
        role = appel["role"]
        if s > PLAFOND_SORTIE[role]:
            raise ArretCourse(10, f"sortie rendue {s} > plafond {PLAFOND_SORTIE[role]} ({appel['id']})")
        if e > PLAFOND_ENTREE_JETONS[role]:
            raise ArretCourse(11, f"entrée rendue {e} > plafond {PLAFOND_ENTREE_JETONS[role]} ({appel['id']})")
        if s > max_tokens:
            raise ArretCourse(16, f"sortie {s} > max_tokens envoyé {max_tokens} ({appel['id']})")
        if e > octets + SURCOUT_FORMAT:
            raise ArretCourse(16, f"entrée {e} > {octets} octets + {SURCOUT_FORMAT} (H3) ({appel['id']})")
        if self.depense > self.plafond_depense + 1e-12:
            raise ArretCourse(14, f"dépense cumulée {self.depense:.6f} > plafond {self.plafond_depense:.6f}")
        return c

    def echec(self, appel, abandon=False):
        """Échec rendu par le fournisseur : compté à la réserve ; un seul budget pour relances et abandons."""
        if self.en_cours is None or self.en_cours[0] != appel:
            raise ArretCourse(15, f"échec de {appel.get('id')} sans appel ouvert")
        _, res = self.compter_reserve()
        self.echecs += 1
        if abandon:
            self.prochain += 1
            if appel["role"] == "message":
                self.messages[appel["monde"]] = self.messages.get(appel["monde"], 0) + 1
        else:
            self.a_relancer = appel
        if self.echecs > self.echecs_max:
            raise ArretCourse(13, f"échec {self.echecs} > {self.echecs_max} permis (10 % de {len(self.plan)})")
        if self.depense > self.plafond_depense + 1e-12:
            raise ArretCourse(14, f"dépense cumulée {self.depense:.6f} > plafond {self.plafond_depense:.6f}")
        return res

    def termine(self):
        return self.prochain == len(self.plan) and self.en_cours is None and self.a_relancer is None


PLAN_SHA256 = "dc5a5cc6811dc955f69e3294706b61d51a53ea59c959d6ad5f61dcc00d945a5d"  # empreinte du plan P-std canonique (744 appels), écrite à la main
if empreinte_plan(plan_pstd()) != PLAN_SHA256:
    raise ImportError("plan P-std différent de son empreinte gelée")
