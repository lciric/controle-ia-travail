"""Renvois par l'interface des demandes arrêtées par le classifieur — v5.

v5 (décision de la mère, 2026-11-22T18:22Z, relance déclarée après troncature) : --effort-attendu (xhigh par défaut,
ou high) ; l'arrêt de la v3 vaut désormais pour tout effort retenu différent de l'effort attendu ; l'effort attendu
est écrit dans la ligne d'ouverture du journal (« ecart_declare » quand il n'est pas xhigh).

v4 : le motif de l'identifiant de GO admet trois chiffres au rang final (GO-2026-11-22-103 refusé par la v3, avant
tout appel, à 17:42Z).

v3 (décision de la mère, 2026-11-22 vers 16:58Z) : un effort retenu autre que xhigh arrête l'appel avant tout envoi
d'un texte (cohérent avec « aucun repli ») ; l'essai est journalisé et rendu, code 3.

v2 (contre-lecture v1 « conforme avec réserves ») : (1) --journaux-precedents obligatoire ; (2) un envoi sans ligne
« tentative » (processus tué en vol) est compté au pire ; (3) les empreintes des textes du premier envoi sont écrites
ici, et tout autre texte (renvoi resserré) doit figurer dans --textes-admis, liste d'empreintes passée à la main ;
(4) un effort retenu autre que xhigh est journalisé « effort abaissé » et rendu, et un forfait de 0,05 USD est retenu
sur le plafond pour la garde de départ et l'essai d'effort ; (5) limite déclarée : le GO passé par --go n'est contrôlé
que par sa présence au registre ; la mère le choisit.

Mots de Lazar : GO-2026-11-22-90 et GO-2026-11-22-96 ; dépense sous la ligne chiffrée passée par --go (devis
devis-renvois-api-v1.md, 7008a11e…, plafond total 17,50 USD).

Enveloppe courte autour de l'exécutant vérifié de la passe X (`passe_x_na_v4.py`, chargé par son chemin après contrôle
de son empreinte) : mêmes transports, mêmes gardes (pièce par empreinte et garde de motifs, configuration scellée, GO,
garde de départ, essai d'effort, arrêts n° 12 et 13, quarantaine sans lecture, clés par leur nom, modèle servi).
Changements, et seulement eux :
- un plan d'envoi scellé attribue à chaque proposeur un texte (chemin et empreinte) ; chaque texte passe la garde de
  motifs du module ;
- chaque chaîne n'a qu'un maillon : aucun repli vers un autre modèle (refusé à la lecture du plan) ;
- aucune relance d'office : un refus ou un défaut est journalisé et rendu ; le renvoi resserré est un nouvel appel de ce
  programme, sur un plan neuf ;
- envois l'un après l'autre ; réserve par tentative ramenée au pire calculé le plus haut du plan (au plus 4,89 USD) ;
- plafond de l'appel = 17,50 USD moins la dépense déjà journalisée par les appels précédents (--journaux-precedents,
  coûts au pire quand inconnus) ;
- garde de coupure du module pour le texte « groupe-2 » (forme de la passe X) ; garde réduite (fin normale, texte non
  vide) pour les autres textes. Le programme n'affiche ni ne rend aucun texte de réponse.
"""
import argparse, hashlib, importlib.util, json, os, re, sys
from decimal import Decimal as D

LOT11 = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-11-passe-x-v4/passe_x_na_v4.py"
PLAFOND_TOTAL = D("17.50")
PIRE_MAX = D("4.89")
GO_FIXES = ("GO-2026-11-22-90", "GO-2026-11-22-96")
VERSION = "renvois-api-v1"  # version de configuration inchangée
FORFAIT_ESSAIS = D("0.05")
TEXTES_FIXES = {"groupe-2": "fc9bed7ffdadca5f2a8d288d2cacece0953c8e8f95671b7ddc3f8cf36ab153c9",
                "question-servie": "2bf01492ef6862998f354bc4c473629a52b5359e5186a93db7fa156eb4e37e38"}


def charger_lot11():
    b = open(LOT11, "rb").read()
    if open(LOT11 + ".sha256").read().split()[0] != hashlib.sha256(b).hexdigest():
        raise SystemExit("REFUS : module du lot 11 v4 différent de son compagnon")
    s = importlib.util.spec_from_file_location("passe_x_na_v4", LOT11)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    m.VERSION = VERSION
    m.PIRE_TENTATIVE = PIRE_MAX
    return m


P = charger_lot11()


def lire_scelle(chemin: str) -> bytes:
    b = open(chemin, "rb").read()
    comp = chemin + ".sha256"
    if not os.path.exists(comp) or open(comp).read().split()[0] != hashlib.sha256(b).hexdigest():
        raise P.Refus(f"pièce sans compagnon ou d'empreinte différente : {os.path.basename(chemin)}")
    return b


def lire_plan(chemin: str, c: dict, admis=()) -> dict:
    """Plan : {"version": VERSION, "attribution": [{"proposeur", "texte", "chemin", "sha256"}]}. Rend proposeur -> nom."""
    plan = json.loads(lire_scelle(chemin))
    if set(plan) != {"version", "attribution"} or plan["version"] != VERSION:
        raise P.Refus("plan d'envoi mal formé")
    ids = {p["id"] for p in c["proposeurs"]}
    attr, textes, empreintes = {}, {}, {}
    for a in plan["attribution"]:
        if set(a) != {"proposeur", "texte", "chemin", "sha256"} or a["proposeur"] in attr \
                or not re.fullmatch(r"[a-z0-9-]{3,64}", a["texte"]):
            raise P.Refus("attribution mal formée")
        if a["texte"] in empreintes and empreintes[a["texte"]] != a["sha256"]:
            raise P.Refus("un même nom de texte porte deux empreintes")
        if TEXTES_FIXES.get(a["texte"], a["sha256"]) != a["sha256"] or \
                (a["texte"] not in TEXTES_FIXES and a["sha256"] not in admis):
            raise P.Refus(f"texte non admis : {a['texte']}")
        attr[a["proposeur"]] = a["texte"]
        empreintes[a["texte"]] = a["sha256"]
        textes[a["texte"]] = a["chemin"]
    if set(attr) != ids:
        raise P.Refus("chaque proposeur doit avoir exactement un texte")
    for p in c["proposeurs"]:
        if len(p["chaine"]) != 1:
            raise P.Refus("aucun repli vers un autre modèle : un seul maillon par proposeur")
    P.EMPREINTES_TEXTES = dict(empreintes)
    P.RANGS_TEXTES = {n: (P.RANGS_TEXTES_ORIG.get(n, ()) if n == "groupe-2" else ()) for n in empreintes}
    lus = {n: P.verifier_piece(ch, n) for n, ch in textes.items()}
    return attr, lus


P.RANGS_TEXTES_ORIG = dict(P.RANGS_TEXTES)


def depense_precedente(journaux) -> D:
    total = D(0)
    for j in journaux or []:
        envois, faites = {}, {}
        for l in open(j, encoding="utf-8"):
            d = json.loads(l)
            t = d.get("type_ligne")
            if t in ("envoi", "tentative"):
                k = (d.get("proposeur"), d.get("relance"), d.get("modele_demande"))
                (envois if t == "envoi" else faites)[k] = (envois if t == "envoi" else faites).get(k, 0) + 1
            if t == "tentative":
                total += D(d.get("pire_usd") if d.get("cout_inconnu") else d.get("cout_usd", "0"))
        for k, n in envois.items():  # envoi orphelin (processus tué en vol) : compté au pire
            total += PIRE_MAX * max(0, n - faites.get(k, 0))
        total += FORFAIT_ESSAIS
    return total


def garde_reduite(texte, fin):
    if fin not in ("end_turn", "stop", "STOP"):
        return "réflexion épuisée" if not (texte or "").strip() else "texte coupé"
    if not (texte or "").strip():
        return "texte coupé"
    return None


class Renvois(P.Passe):
    def __init__(self, c, textes, environ, transport, quarantaine, journal, attribution, plafond):
        super().__init__(c, textes, environ, transport, quarantaine, journal)
        self.attribution = attribution
        self.p_x = plafond

    def _juger(self, p, nom_texte, classe, r, maillon):
        if classe == "réponse rendue" and nom_texte != "groupe-2":
            cause = garde_reduite(r["texte"], r["fin"])
            self._ecrire({"type_ligne": "garde réduite", "proposeur": p["id"], "cause": cause, "heure": P.heure()})
            return ("rendue", None) if cause is None else ("défaut", cause)
        return super()._juger(p, nom_texte, classe, r, maillon)

    def unite(self, p, g=None):
        nom = self.attribution[p["id"]]
        classe, r, maillon, rang = self.chaine(p, nom)
        issue, cause = self._juger(p, nom, classe, r, maillon)
        bilan = {"type_ligne": "unité", "proposeur": p["id"], "texte_servi": nom, "classe": classe, "issue": issue,
                 "cause": cause, "relance": None, "heure": P.heure()}
        self._ecrire(bilan)
        self.unites.append(bilan)
        return bilan

    def courir(self):
        for p in self.c["proposeurs"]:
            self.unite(p)
        return {"version": VERSION, "par_cle_usd": {k: P.usd(v) for k, v in self.cumul.items()},
                "arret_13": self.arret_13.is_set(),
                "unites": {u["proposeur"]: {"classe": u["classe"], "issue": u["issue"], "cause": u["cause"]}
                           for u in self.unites}}


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--configuration", required=True); a.add_argument("--plan-envoi", required=True)
    a.add_argument("--plan-garde", required=True); a.add_argument("--quarantaine", required=True)
    a.add_argument("--journal", required=True); a.add_argument("--go", required=True)
    a.add_argument("--journaux-precedents", nargs="*", required=True)
    a.add_argument("--textes-admis", nargs="*", default=[])
    a.add_argument("--effort-attendu", choices=("xhigh", "high"), default="xhigh")
    a.add_argument("--registre-go", default="/home/user/main-lecture/registres/go.md")
    a.add_argument("--reel", action="store_true")
    o = a.parse_args(argv)
    garde_j, reglages_j = o.journal + ".garde-depart.jsonl", o.journal + ".essai-reglages.jsonl"
    try:
        if not re.fullmatch(r"GO-2026-11-\d\d-\d{2,3}", o.go):
            raise P.Refus("identifiant de GO mal formé")
        c = P.lire_configuration(o.configuration)
        attribution, textes = lire_plan(o.plan_envoi, c, tuple(o.textes_admis))
        P.verifier_go(o.registre_go, GO_FIXES + (o.go,))
        plafond = PLAFOND_TOTAL - depense_precedente(o.journaux_precedents) - FORFAIT_ESSAIS
        if plafond <= 0:
            raise P.Refus("plafond total déjà atteint")
        plan = P.GD.lire_plan(o.plan_garde)
        if P.couples_de_la_configuration(c) - {(x["cle_var"], x["modele"]) for x in plan}:
            raise P.Refus("garde de départ : couple (clé, modèle) non couvert")
        for j in (o.journal, garde_j, reglages_j):
            if os.path.exists(j):
                raise P.Refus("journal déjà présent")
        if os.path.exists(o.quarantaine) or not P.hors_des_depots(o.quarantaine):
            raise P.Refus("la quarantaine doit être un dossier neuf, hors des dépôts")
        Renvois(c, textes, os.environ, P.transport_reel, o.quarantaine, o.journal, attribution, plafond)
        pires = {p["id"]: P.usd(P.pire(p["chaine"][0], len(textes[attribution[p["id"]]]))) for p in c["proposeurs"]}
        if not o.reel:
            print(json.dumps({"a_blanc": "conforme", "plafond_restant": P.usd(plafond), "pires": pires},
                             ensure_ascii=False))
            return 0
        g = P.GD.executer(plan, os.environ, P.transport_simple, garde_j)
        P.verifier_garde_couvre(c, plan, g)
        c = P.essayer_reglages(c, os.environ, P.transport_simple, reglages_j)
        abaisses = [p["id"] for p in c["proposeurs"]
                    if p["chaine"][0].get("extras", {}).get("output_config", {}).get("effort") != o.effort_attendu]
        if abaisses:
            print(json.dumps({"arret": "effort retenu différent de l'effort attendu", "effort_abaisse": abaisses}, ensure_ascii=False))
            return 3
        os.makedirs(o.quarantaine)
        r = Renvois(c, textes, os.environ, P.transport_reel, o.quarantaine, o.journal, attribution, plafond)
        r._ecrire({"type_ligne": "ouverture", "version": VERSION, "heure": P.heure(), "go": list(GO_FIXES) + [o.go],
                   "plafond_restant": P.usd(plafond), "textes": P.EMPREINTES_TEXTES,
                   "effort_abaisse": abaisses, "effort_attendu": o.effort_attendu,
                   "ecart_declare": (None if o.effort_attendu == "xhigh" else
                                     "relance après troncature à l'effort high, décision de la mère, 2026-11-22T18:22Z")})
        sortie = r.courir()
        sortie["effort_abaisse"] = abaisses
        print(json.dumps(sortie, ensure_ascii=False))
    except P.Refus as e:
        print("REFUS :", e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
