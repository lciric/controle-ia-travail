#!/usr/bin/env python3
"""Gardes d'arrêt dures du pilote P-std de l'essaim — v1 (réserve R6 de la vérification de la v2). Bibliothèque standard seule.
Aucun appel, aucun réseau : ce module ne connaît aucun fournisseur ; le lanceur lui soumet chaque appel avant et après.

Gardes, appliquées AVANT chaque appel et AU CUMUL ; toute garde franchie lève `ArretCourse(code, garde, detail)` : la course
s'arrête, une ligne de journal est écrite, aucun repli, aucune poursuite.
| code | garde | avant l'appel | après l'appel |
|---|---|---|---|
| 10 | sortie | `max_tokens` demandé ≤ plafond du rôle (proposeur 24 000 ; message 2 000) | sortie rendue ≤ plafond du rôle |
| 11 | entrée | octets du texte servi ≤ plafond d'octets du rôle (plafond de jetons × 2,8 octets) | entrée rendue ≤ plafond de jetons du rôle (proposeur 23 200 ; message 6 000) |
| 12 | messages | appels de message du monde ≤ 12 et du pilote ≤ 144 | — |
| 13 | relances | relances ≤ ⌊10 % × appels du plan⌋ (74 sur 744) | — |
| 14 | dépense | dépense cumulée + réserve dure de l'appel ≤ plafond de dépense | dépense cumulée ≤ plafond |
| 15 | plan | l'appel est l'entrée suivante du plan gelé, jamais rejouée | — |
| 16 | facturation hors borne | — | sortie ≤ `max_tokens` envoyé ; entrée ≤ octets + 256 (hypothèse H3) ; usage complet |

Borne dure d'un appel (réserve) : (octets + 256) × prix d'entrée + `max_tokens` × prix de sortie. Elle tient si :
H1 le fournisseur facture au plus l'usage rendu ; H2 la sortie (réflexion comprise) ne dépasse pas `max_tokens` ; H3 un jeton
couvre au moins un octet (découpage par octets), plus 256 jetons de mise en forme ; H4 un appel échoué coûte au plus sa réserve.
H2 et H3 sont contrôlées après chaque appel (code 16) ; H1 et H4 se contrôlent sur la facture (réponse 14, A.4, point 1).
Un appel échoué est compté à sa réserve entière (facturation inconnue).

Plafond de dépense = vrai pire calculable : Σ sur le plan des coûts aux plafonds de jetons + relances au plus × la réserve dure
maximale + l'excès d'un seul appel au-delà du plafond de jetons d'entrée (la course s'arrête au premier, code 11).
"""
import math

ROLES = ("proposeur", "message")
PLAFOND_SORTIE = {"proposeur": 24000, "message": 2000}          # PROPOSITION du pilote v1 (§ 1, plafonds), gelée ici
PLAFOND_SORTIE_ABSOLU = 24000                                   # commande du directeur : 24 000 jetons par appel, tout rôle
PLAFOND_ENTREE_JETONS = {"proposeur": 20000 + 3200, "message": 6000}  # section D haut + surcroît supposé ; message : pilote v1
OCTETS_PAR_JETON_HAUT = 2.8                                     # pièce : devis auto-conception v1, l. 40 (« haut : 2,8 »)
PLAFOND_ENTREE_OCTETS = {r: int(PLAFOND_ENTREE_JETONS[r] * OCTETS_PAR_JETON_HAUT) for r in ROLES}
SURCOUT_FORMAT = 256                                            # HYPOTHÈSE H3 : jetons de mise en forme par appel
MESSAGES_PAR_MONDE = 12
PART_RELANCES = 0.10                                            # marge de relances (devis d'affinage v5, lue par le devis v3)
CODES = {10: "sortie", 11: "entrée", 12: "messages", 13: "relances", 14: "dépense", 15: "plan", 16: "facturation hors borne"}

assert all(v <= PLAFOND_SORTIE_ABSOLU for v in PLAFOND_SORTIE.values())


class ArretCourse(Exception):
    def __init__(self, code, detail):
        super().__init__(f"arrêt {code} ({CODES[code]}) : {detail}")
        self.code, self.garde, self.detail = code, CODES[code], detail


# --- plan gelé du pilote P-std ------------------------------------------------------------------------------------------------
APPELS_PAR_GENERATION = {"a": {"proposeur": 8, "message": 4}, "c": {"proposeur": (9, 9, 8), "message": 0}}


def plan_pstd(mondes=12, generations=3, bras=("a", "c")):
    """Liste ordonnée des appels : (identifiant, monde, bras, génération, rôle). (a) : 4 agents × 2 appels de proposeur et
    4 messages par génération ; (c) : 26 appels de proposeur sur trois générations (9, 9, 8). 744 appels pour P-std."""
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


def cout(entree, sortie, prix):
    return (entree * prix[0] + sortie * prix[1]) / 1e6


def reserve_dure(role, octets, max_tokens, prix):
    return cout(octets + SURCOUT_FORMAT, max_tokens, prix)


def borne_pire(plan, prix):
    """Vrai pire calculable sous les gardes (USD) et sa décomposition."""
    aux_plafonds = sum(cout(PLAFOND_ENTREE_JETONS[a["role"]], PLAFOND_SORTIE[a["role"]], prix) for a in plan)
    rmax = max(reserve_dure(r, PLAFOND_ENTREE_OCTETS[r], PLAFOND_SORTIE[r], prix) for r in ROLES)
    relances = math.floor(PART_RELANCES * len(plan))
    exces = max(reserve_dure(r, PLAFOND_ENTREE_OCTETS[r], PLAFOND_SORTIE[r], prix) - cout(PLAFOND_ENTREE_JETONS[r], PLAFOND_SORTIE[r], prix)
                for r in ROLES)
    total = aux_plafonds + relances * rmax + exces
    return {"appels_du_plan": len(plan), "relances_au_plus": relances, "appels_au_plus": len(plan) + relances,
            "aux_plafonds_de_jetons_usd": round(aux_plafonds, 4), "reserve_dure_max_usd": round(rmax, 6),
            "relances_usd": round(relances * rmax, 4), "exces_d_un_appel_usd": round(exces, 6), "pire_usd": round(total, 4)}


class Garde:
    """État des gardes d'une course. `avant(appel, texte, max_tokens)` puis `apres(appel, usage)` ou `echec(appel)`."""

    def __init__(self, plan, prix, plafond_depense=None):
        self.plan, self.prix = list(plan), tuple(prix)
        self.ids = [a["id"] for a in self.plan]
        if len(set(self.ids)) != len(self.ids):
            raise ValueError("plan à identifiants répétés")
        self.borne = borne_pire(self.plan, self.prix)
        self.plafond_depense = self.borne["pire_usd"] if plafond_depense is None else float(plafond_depense)
        self.prochain = 0            # index de la prochaine entrée du plan
        self.en_cours = None         # (appel, réserve, octets, max_tokens, relance)
        self.depense = 0.0
        self.relances = 0
        self.relances_max = math.floor(PART_RELANCES * len(self.plan))
        self.messages = {}
        self.messages_total = 0
        self.messages_max_total = sum(1 for a in self.plan if a["role"] == "message")
        self.a_relancer = None       # appel échoué en attente de relance

    # -- avant l'appel --------------------------------------------------------------------------------------------------------
    def avant(self, appel, texte, max_tokens):
        if self.en_cours is not None:
            raise ArretCourse(15, f"appel {appel.get('id')} soumis avant la clôture de {self.en_cours[0]['id']}")
        relance = self.a_relancer is not None and appel.get("id") == self.a_relancer["id"]
        if self.a_relancer is not None and not relance:
            raise ArretCourse(15, f"{appel.get('id')} soumis alors que {self.a_relancer['id']} attend sa relance")
        if not relance:
            if self.prochain >= len(self.plan) or appel != self.plan[self.prochain]:
                attendu = self.plan[self.prochain]["id"] if self.prochain < len(self.plan) else "aucun (plan épuisé)"
                raise ArretCourse(15, f"appel {appel.get('id')} hors plan (attendu {attendu})")
        else:
            if self.relances + 1 > self.relances_max:
                raise ArretCourse(13, f"relance {self.relances + 1} > {self.relances_max} permises (10 % de {len(self.plan)})")
        role = appel["role"]
        if not isinstance(max_tokens, int) or isinstance(max_tokens, bool) or max_tokens <= 0:
            raise ArretCourse(10, f"max_tokens invalide : {max_tokens!r}")
        if max_tokens > PLAFOND_SORTIE[role] or max_tokens > PLAFOND_SORTIE_ABSOLU:
            raise ArretCourse(10, f"max_tokens {max_tokens} > plafond {PLAFOND_SORTIE[role]} ({role})")
        octets = len(texte.encode("utf-8"))
        if octets > PLAFOND_ENTREE_OCTETS[role]:
            raise ArretCourse(11, f"entrée de {octets} octets > plafond {PLAFOND_ENTREE_OCTETS[role]} ({role})")
        if role == "message" and not relance:
            n = self.messages.get(appel["monde"], 0) + 1
            if n > MESSAGES_PAR_MONDE or self.messages_total + 1 > self.messages_max_total:
                raise ArretCourse(12, f"message {n} du monde {appel['monde']} (plafond {MESSAGES_PAR_MONDE}), total {self.messages_total + 1}")
        res = reserve_dure(role, octets, max_tokens, self.prix)
        if self.depense + res > self.plafond_depense + 1e-12:
            raise ArretCourse(14, f"dépense {self.depense:.6f} + réserve {res:.6f} > plafond {self.plafond_depense:.6f} USD")
        self.en_cours = (appel, res, octets, max_tokens, relance)
        if relance:
            self.relances += 1
            self.a_relancer = None
        else:
            self.prochain += 1
            if role == "message":
                self.messages[appel["monde"]] = self.messages.get(appel["monde"], 0) + 1
                self.messages_total += 1
        return res

    # -- après l'appel --------------------------------------------------------------------------------------------------------
    def apres(self, appel, usage):
        if self.en_cours is None or self.en_cours[0]["id"] != appel["id"]:
            raise ArretCourse(15, f"clôture de {appel.get('id')} sans appel ouvert")
        _, res, octets, max_tokens, _ = self.en_cours
        self.en_cours = None
        try:
            e, s = int(usage["entree"]), int(usage["sortie"])
        except (KeyError, TypeError, ValueError):
            self.depense += res
            raise ArretCourse(16, f"usage incomplet pour {appel['id']} : {usage!r} (compté à la réserve)")
        c = cout(e, s, self.prix)
        self.depense += max(c, 0.0)
        role = appel["role"]
        if s > PLAFOND_SORTIE[role]:
            raise ArretCourse(10, f"sortie rendue {s} > plafond {PLAFOND_SORTIE[role]} ({appel['id']})")
        if e > PLAFOND_ENTREE_JETONS[role]:
            raise ArretCourse(11, f"entrée rendue {e} jetons > plafond {PLAFOND_ENTREE_JETONS[role]} ({appel['id']})")
        if s > max_tokens:
            raise ArretCourse(16, f"sortie {s} > max_tokens envoyé {max_tokens} ({appel['id']})")
        if e > octets + SURCOUT_FORMAT:
            raise ArretCourse(16, f"entrée {e} jetons > {octets} octets + {SURCOUT_FORMAT} (hypothèse H3) ({appel['id']})")
        if e < 0 or s < 0:
            raise ArretCourse(16, f"usage négatif pour {appel['id']} : {usage!r}")
        if self.depense > self.plafond_depense + 1e-12:
            raise ArretCourse(14, f"dépense cumulée {self.depense:.6f} > plafond {self.plafond_depense:.6f} USD")
        return c

    def echec(self, appel):
        """Appel échoué (erreur du fournisseur) : compté à sa réserve entière ; la relance éventuelle est le même appel."""
        if self.en_cours is None or self.en_cours[0]["id"] != appel["id"]:
            raise ArretCourse(15, f"échec de {appel.get('id')} sans appel ouvert")
        _, res, _, _, _ = self.en_cours
        self.en_cours = None
        self.depense += res
        self.a_relancer = appel
        if self.depense > self.plafond_depense + 1e-12:
            raise ArretCourse(14, f"dépense cumulée {self.depense:.6f} > plafond {self.plafond_depense:.6f} USD")
        return res

    def abandon(self):
        """Un appel échoué qu'on ne relance pas : la carte compte « rien » ; la course continue au plan."""
        self.a_relancer = None

    def termine(self):
        return self.prochain == len(self.plan) and self.en_cours is None and self.a_relancer is None
