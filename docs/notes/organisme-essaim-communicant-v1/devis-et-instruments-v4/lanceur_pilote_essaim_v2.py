#!/usr/bin/env python3
"""Lanceur du pilote P-std de l'essaim — v2 (contre-lecture de la v3 : A1 à A10). Aucun client réel n'est câblé ici :
l'appel passe par `adaptateur_fournisseur_v1.AdaptateurChatCompletions`, dont le transport est injecté (faux fournisseur
dans les épreuves ; `TransportNonCable` sinon). Une exécution directe est refusée (code 20).

Refus avant tout appel (code 24 sauf mention) :
- plan différent du plan P-std gelé (empreinte `PLAN_SHA256`) — code 15 ;
- plafond de dépense au-dessus de la borne calculée ;
- prix différents de `PRIX_GELES` ou de `calcul_devis_essaim_v4.tarifs()["kimi"]` (pièces lues à leur empreinte) ;
- couche d'appel qui n'est pas l'adaptateur vérifié, ou relances internes ≠ 0 ;
- registre de dépense absent (21), altéré (22) ou clos (23).
Pendant la course : chaque réserve est écrite et scellée dans le registre AVANT l'appel ; règlement, échec, réserve comptée
et arrêt y sont écrits après. Toute garde franchie arrête la course (code, ligne au journal et au registre). Toute exception
après l'envoi compte l'appel à sa réserve entière (16 ou 17). Une course close ne repart jamais : une seconde invocation après
une fin ou un arrêt est refusée (23) ; après une mort du processus, la réserve en suspens est comptée comme un échec et la
course reprend au plan.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adaptateur_fournisseur_v1 as A  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import registre_depense_v1 as RG  # noqa: E402

CODE_SANS_CLIENT = 20


def _t():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def prix_de_la_table():
    import calcul_devis_essaim_v4 as C4
    prix, _ = C4.tarifs()
    return tuple(prix["kimi"])


def parametres(plafond):
    return json.loads(json.dumps(GP.parametres_geles(plafond)))


def creer_registre(chemin, plafond_depense=None):
    """Étape unique, avant la première invocation : crée le registre avec plan, prix et plafond gelés."""
    borne = GP.borne_pire(GP.plan_pstd(), GP.PRIX_GELES)["pire_usd"]
    plafond = borne if plafond_depense is None else float(plafond_depense)
    if plafond > borne + 1e-9:
        raise GP.ArretCourse(24, f"plafond {plafond} > borne {borne}")
    RG.creer(chemin, parametres(plafond))
    return plafond


class Journal:
    def __init__(self, chemin):
        self.f = open(chemin, "x", encoding="utf-8")

    def ecrire(self, **l):
        self.f.write(json.dumps(dict(t=_t(), **l), ensure_ascii=False, sort_keys=True) + "\n")
        self.f.flush()

    def fermer(self):
        self.f.close()


def _verifier_configuration(plan, adaptateur, plafond_depense, prix):
    if GP.empreinte_plan(plan) != GP.PLAN_SHA256:
        raise GP.ArretCourse(15, "plan différent du plan P-std gelé")
    table = prix_de_la_table()
    if table != GP.PRIX_GELES:
        raise GP.ArretCourse(24, f"prix de la table {table} ≠ gelés {GP.PRIX_GELES}")
    if prix is not None and tuple(prix) != GP.PRIX_GELES:
        raise GP.ArretCourse(24, f"prix fournis {tuple(prix)} ≠ gelés {GP.PRIX_GELES}")
    borne = GP.borne_pire(plan, GP.PRIX_GELES)["pire_usd"]
    if plafond_depense is not None and float(plafond_depense) > borne + 1e-9:
        raise GP.ArretCourse(24, f"plafond {plafond_depense} > borne {borne}")
    if not isinstance(adaptateur, A.AdaptateurChatCompletions) or adaptateur.relances_internes != 0 \
            or getattr(adaptateur.transport, "relances_internes", None) != 0:
        raise GP.ArretCourse(24, "couche d'appel non vérifiée (adaptateur exigé, relances internes 0)")


def courir(plan, adaptateur, fournisseur_entree, chemin_journal, chemin_registre, plafond_depense=None, relancer=True,
           prix=None, max_tokens_par_role=None):
    """Rend (code, garde). Code 0 : plan entier joué. `plafond_depense` doit égaler celui du registre (ou être omis)."""
    j = Journal(chemin_journal)
    garde, reg = None, None
    try:
        if adaptateur is None:
            j.ecrire(evenement="arret", code=CODE_SANS_CLIENT, garde="client", detail="aucun adaptateur : refus")
            return CODE_SANS_CLIENT, None
        _verifier_configuration(plan, adaptateur, plafond_depense, prix)
        if not os.path.exists(chemin_registre):
            raise RG.RegistreRefuse(21, "registre absent : le créer d'abord (creer_registre), une seule fois")
        plafond_reg = json.loads(open(chemin_registre, encoding="utf-8").readline())["parametres"]["plafond_depense_usd"]
        if plafond_depense is not None and abs(float(plafond_depense) - plafond_reg) > 1e-9:
            raise GP.ArretCourse(24, f"plafond {plafond_depense} ≠ plafond du registre {plafond_reg}")
        reg = RG.Registre(chemin_registre, parametres(plafond_reg))
        etat = reg.etat()
        if etat["suspens"] is not None:
            s = etat["suspens"]
            reg.ecrire(evenement="compte_a_la_reserve", id=s["id"], cout_usd=s["reserve_usd"], abandon=False,
                       motif="réserve en suspens à la réouverture (processus interrompu pendant l'appel)")
            etat = reg.etat()
        garde = GP.Garde(plan, GP.PRIX_GELES, plafond_reg, etat)
        dern = reg.lignes[-1]
        if dern["evenement"] in ("echec", "compte_a_la_reserve") and not dern.get("abandon"):
            garde.relance_due(plan[garde.prochain])
        mt = dict(GP.PLAFOND_SORTIE, **(max_tokens_par_role or {}))
        j.ecrire(evenement="debut", depense_reprise_usd=round(garde.depense, 6), appels_regles=garde.prochain, echecs=garde.echecs,
                 plafond_depense_usd=plafond_reg, borne=garde.borne)
        while garde.prochain < len(plan):
            appel = garde.a_relancer or plan[garde.prochain]
            texte = fournisseur_entree(appel)
            reserve = garde.avant(appel, texte, mt[appel["role"]])
            reg.ecrire(evenement="reserve", id=appel["id"], role=appel["role"], reserve_usd=reserve)
            try:
                rep = adaptateur.appeler(appel, texte, mt[appel["role"]])
            except A.ErreurFournisseur as ex:
                try:
                    garde.echec(appel, abandon=not relancer)
                finally:
                    reg.ecrire(evenement="echec", id=appel["id"], cout_usd=reserve, abandon=not relancer, motif=str(ex)[:120])
                j.ecrire(evenement="echec", id=appel["id"], reserve_usd=round(reserve, 6), depense_usd=round(garde.depense, 6))
                continue
            except A.AnomalieReponse as ex:
                garde.compter_reserve()
                envois = getattr(ex, "envois", 1)
                garde.depense += (envois - 1) * reserve  # envois cachés rendus par le transport : une réserve par envoi
                reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=envois * reserve, abandon=True, motif=str(ex)[:120])
                raise GP.ArretCourse(16, f"anomalie de réponse ({ex}) — compté à la réserve")
            except Exception as ex:  # noqa: BLE001  (aucun repli : compté à la réserve, arrêt)
                garde.compter_reserve()
                reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=reserve, abandon=True, motif=type(ex).__name__)
                raise GP.ArretCourse(17, f"{type(ex).__name__}: {ex} — compté à la réserve")
            usage = rep.get("usage") if isinstance(rep, dict) else None
            avant = garde.depense
            try:
                c = garde.apres(appel, usage)
            except GP.ArretCourse:
                reg.ecrire(evenement="regle", id=appel["id"], cout_usd=garde.depense - avant, usage=usage if isinstance(usage, dict) else None,
                           motif="arrêt à la clôture (coût réel, ou réserve si l'usage est anormal)")
                raise
            reg.ecrire(evenement="regle", id=appel["id"], cout_usd=c, usage=usage)
            j.ecrire(evenement="appel", id=appel["id"], usage=usage, cout_usd=round(c, 6), depense_usd=round(garde.depense, 6))
        reg.ecrire(evenement="fin", depense_usd=garde.depense)
        j.ecrire(evenement="fin", code=0, depense_usd=round(garde.depense, 6), appels_regles=garde.prochain, echecs=garde.echecs)
        return 0, garde
    except (GP.ArretCourse, RG.RegistreRefuse) as ex:
        dep = garde.depense if garde else None
        j.ecrire(evenement="arret", code=ex.code, garde=GP.CODES.get(ex.code, "?"), detail=ex.detail, depense_usd=dep)
        if reg is not None and ex.code not in (21, 22, 23):
            try:
                reg.ecrire(evenement="arret", code=ex.code, detail=str(ex.detail)[:200], depense_usd=dep)
            except OSError:
                pass
        return ex.code, garde
    finally:
        j.fermer()


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : lanceur_pilote_essaim_v2.py JOURNAL.jsonl (neuf) — refuse toujours : aucun transport câblé", file=sys.stderr)
        return 2
    code, _ = courir(GP.plan_pstd(), None, None, argv[1], argv[1] + ".registre")
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
