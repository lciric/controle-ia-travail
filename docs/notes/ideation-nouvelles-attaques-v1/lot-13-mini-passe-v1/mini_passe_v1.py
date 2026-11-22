"""Lot 13 — mini-passe : une question servie seule, une requête par proposeur d'API — v1.

Enveloppe courte autour de l'exécutant du lot 11 v4 vérifié (`passe_x_na_v4.py`, chargé par son chemin après contrôle
de son empreinte) : mêmes transports, mêmes gardes G1 à G12 (pièce par empreinte et garde de motifs, configuration
scellée, GO, garde de départ, essai d'effort, pire ≤ 6,05 par tentative, garde Google v3, arrêts n° 12 et 13, repli
sur refus de classifieur, quarantaine sans lecture, clés par leur nom, modèle servi). Changements, et seulement eux :
- un texte unique, la question servie (empreinte écrite ici), au lieu des groupes ;
- une seule phase, sans barrière ;
- la garde de coupure réduite à ce qui vaut sans consigne de forme : fin normale et texte non vide (le modèle servi est
  tenu par la classe) ; une réponse rendue sans défaut est « rendue » ;
- une seule relance par proposeur : transport → la même requête ; réflexion épuisée ou texte coupé → un cran d'effort
  en moins (sans effort réglable : la même requête) ; second défaut : « sans réponse ».
"""
import argparse, hashlib, importlib.util, json, os, sys

LOT11 = "/home/user/controle-ia-travail/docs/notes/ideation-nouvelles-attaques-v1/lot-11-passe-x-v4/passe_x_na_v4.py"
TEXTE = ("/home/user/controle-ia-travail/docs/notes/organisme-essaim-communicant-v1/exploration-allumage-preparation-v1/"
         "question-neutre-exploration-et-allumage-servie-v1.md")
NOM_TEXTE = "question-servie"
EMPREINTE_TEXTE = "2bf01492ef6862998f354bc4c473629a52b5359e5186a93db7fa156eb4e37e38"
GO_EXIGES = ("GO-2026-11-22-70", "GO-2026-11-22-54")


def charger_lot11():
    b = open(LOT11, "rb").read()
    if open(LOT11 + ".sha256").read().split()[0] != hashlib.sha256(b).hexdigest():
        raise SystemExit("REFUS : module du lot 11 v4 différent de son compagnon")
    s = importlib.util.spec_from_file_location("passe_x_na_v4", LOT11); m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    m.EMPREINTES_TEXTES = {NOM_TEXTE: EMPREINTE_TEXTE}
    m.RANGS_TEXTES = {NOM_TEXTE: ()}
    m.VERSION = "mini-passe-v1"
    m.GO_EXIGES = GO_EXIGES
    return m


P = charger_lot11()


def garde_reduite(texte, fin):
    if fin not in ("end_turn", "stop", "STOP"):
        return "réflexion épuisée" if not (texte or "").strip() else "texte coupé"
    if not (texte or "").strip():
        return "texte coupé"
    return None


class MiniPasse(P.Passe):
    def _juger(self, p, nom_texte, classe, r, maillon):
        if classe == "réponse rendue":
            cause = garde_reduite(r["texte"], r["fin"])
            self._ecrire({"type_ligne": "garde réduite", "proposeur": p["id"], "cause": cause, "heure": P.heure()})
            return ("rendue", None) if cause is None else ("défaut", cause)
        if classe == "injoignable":
            return "défaut", "transport"
        if classe in ("réponse illisible", "défaut Google") and r and r.get("fin") in ("max_tokens", "length", "MAX_TOKENS"):
            return "défaut", "réflexion épuisée" if not (r.get("texte") or "").strip() else "texte coupé"
        return "fermée", None

    def unite(self, p, g=None):
        classe, r, maillon, rang = self.chaine(p, NOM_TEXTE)
        issue, cause = self._juger(p, NOM_TEXTE, classe, r, maillon)
        bilan = {"type_ligne": "unité", "proposeur": p["id"], "groupe": 0, "classe": classe, "issue": issue,
                 "cause": cause, "relance": None, "heure": P.heure()}
        if issue == "défaut" and not self.arret_13.is_set():
            bilan["relance"] = cause
            m2 = maillon if cause == "transport" else P.cran_en_moins(p["fournisseur"], maillon)
            c2, r2 = self.tentative(p, rang, m2, NOM_TEXTE, relance=cause)
            bilan["issue_relance"] = "rendue" if self._juger(p, NOM_TEXTE, c2, r2, m2)[0] == "rendue" else "sans réponse"
        self._ecrire(bilan)
        self.unites.append(bilan)
        return bilan

    def courir(self, en_parallele=True):
        self._phase((0,), en_parallele)
        return {"version": "mini-passe-v1", "par_cle_usd": {k: P.usd(v) for k, v in self.cumul.items()},
                "arret_13": self.arret_13.is_set(),
                "unites": {u["proposeur"]: u.get("issue_relance") or u["issue"] for u in self.unites}}


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("--configuration", required=True); a.add_argument("--plan-garde", required=True)
    a.add_argument("--quarantaine", required=True); a.add_argument("--journal", required=True)
    a.add_argument("--registre-go", default="/home/user/main-lecture/registres/go.md")
    a.add_argument("--reel", action="store_true")
    o = a.parse_args(argv)
    garde_j, reglages_j = o.journal + ".garde-depart.jsonl", o.journal + ".essai-reglages.jsonl"
    try:
        textes = {NOM_TEXTE: P.verifier_piece(TEXTE, NOM_TEXTE)}
        c = P.lire_configuration(o.configuration)
        P.verifier_go(o.registre_go)
        plan = P.GD.lire_plan(o.plan_garde)
        P.verifier_garde_couvre(c, plan, {"lignes": []}) if P.couples_de_la_configuration(c) - {
            (x["cle_var"], x["modele"]) for x in plan} else None
        for j in (o.journal, garde_j, reglages_j):
            if os.path.exists(j):
                raise P.Refus("journal déjà présent")
        if os.path.exists(o.quarantaine) or not P.hors_des_depots(o.quarantaine):
            raise P.Refus("la quarantaine doit être un dossier neuf, hors des dépôts")
        MiniPasse(c, textes, os.environ, P.transport_reel, o.quarantaine, o.journal)
        if not o.reel:
            print(json.dumps({"a_blanc": "conforme", "pires": {p["id"]: [P.usd(P.pire(m, len(textes[NOM_TEXTE])))
                                                                         for m in p["chaine"]] for p in c["proposeurs"]}}))
            return 0
        g = P.GD.executer(plan, os.environ, P.transport_simple, garde_j)
        P.verifier_garde_couvre(c, plan, g)
        c = P.essayer_reglages(c, os.environ, P.transport_simple, reglages_j)
        os.makedirs(o.quarantaine)
        passe = MiniPasse(c, textes, os.environ, P.transport_reel, o.quarantaine, o.journal)
        passe._ecrire({"type_ligne": "ouverture", "version": "mini-passe-v1", "heure": P.heure(), "go": list(GO_EXIGES),
                       "texte_sha256": EMPREINTE_TEXTE})
        print(json.dumps(passe.courir(), ensure_ascii=False))
    except P.Refus as e:
        print("REFUS :", e, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
