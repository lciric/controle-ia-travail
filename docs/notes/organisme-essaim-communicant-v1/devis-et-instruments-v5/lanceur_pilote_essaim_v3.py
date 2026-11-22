#!/usr/bin/env python3
"""Lanceur du pilote P-std de l'essaim — v3 (vérification de la v4 : N1 à N5, l. 116 et l. 155). Aucun client réel câblé.

Ce qui change par rapport à `lanceur_pilote_essaim_v2.py` :
- **chemins écrits en dur** pour le pilote (`CHEMINS_PILOTE`, à citer dans le GO) : registre sous la racine du dépôt,
  ancre et clé du sceau hors du dépôt. `courir_pilote()` ne prend aucun chemin ; `_courir()` (chemins donnés) ne sert qu'aux
  épreuves, avec un dossier d'état propre ;
- registre v2 (`registre_depense_v2`) : verrou exclusif tenu pendant toute la course, sceau à secret, ancre hors du fichier,
  relecture complète **avant chaque réserve** ; plafond du registre comparé à la borne ;
- **adaptateur et transport admis par liste, classe EXACTE** (`type(x)`, jamais `isinstance`) : (module, classe) →
  empreinte sha256 du fichier du module, écrite en dur. Pour le pilote : l'adaptateur `AdaptateurKimiStrict`
  (`adaptateur_kimi_strict_v1.py`, `6b8e9553…`) et le transport `TransportKimiReel` (`transport_kimi_reel_v1.py`,
  `4bba649c…`, envois mesurés sur la connexion), tous deux du dossier versé
  `docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1/`, importés de là à leur empreinte ; l'adaptateur de
  base qu'ils étendent doit être `adaptateur_fournisseur_v1.py` à `67704c1e…`. Aucune sous-classe n'est admise ;
- écriture de la réserve impossible ⇒ aucun appel, arrêt écrit au journal (22) ; écriture de l'arrêt impossible au registre
  ⇒ ligne d'arrêt au journal avec `inscrit_au_registre: false` et code 26 (jamais avalée).
Limites (le code du lanceur seul ne les voit pas) : un transport admis qui cacherait ses relances en rendant
`tentatives = 1`, ou qui recevrait une réflexion facturée sans aucune trace dans l'usage — le transport réel admis mesure ses
envois sur la connexion et rend `usage = None` si le champ de réflexion manque, ce que ses propres épreuves établissent ; un détenteur de la clé qui réécrit registre, sceau et ancre. Seuls la
relecture du transport réel, l'essai de fumée sous GO (H1, H2) et la limite chez le fournisseur (204 USD) les couvrent.
"""
import datetime
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import adaptateur_fournisseur_v1 as A  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import racine_depot_v1 as RAC  # noqa: E402
import registre_depense_v2 as RG  # noqa: E402

CODE_SANS_CLIENT = 20
CODE_ARRET_NON_INSCRIT = 26
REGISTRE_PILOTE_REL = "runs/pilote-essaim-pstd/registre-depense-v2.jsonl"
ETAT_PILOTE = os.path.join(os.path.expanduser("~"), ".local", "state", "controle-ia", "pilote-essaim-pstd")
CHEMINS_PILOTE = RG.Chemins(RAC.chemin(REGISTRE_PILOTE_REL), os.path.join(ETAT_PILOTE, "ancre-registre-v2.json"),
                            os.path.join(ETAT_PILOTE, "cle-sceau-registre-v2"))
TRANSPORT_DOSSIER_REL = "docs/notes/organisme-essaim-communicant-v1/transport-kimi-reel-v1"
ADAPTATEUR_BASE_SHA = "67704c1e42a0308a4f511ddc82e58666e6741b9b954f78072fd55a64c7eff1e4"  # adaptateur_fournisseur_v1.py
ADAPTATEURS_ADMIS_PILOTE = {("adaptateur_kimi_strict_v1", "AdaptateurKimiStrict"):
                            "6b8e955300d657b9f7ed784e544d878026810859bd6f534c5aad22f1a367de9b"}
TRANSPORTS_ADMIS_PILOTE = {("transport_kimi_reel_v1", "TransportKimiReel"):
                           "4bba649ce1d1b62ea5f50225e62a5eb5666592014033e174b47cca34533aa5a6"}
ADAPTATEURS_ADMIS_EPREUVES = {("adaptateur_fournisseur_v1", "AdaptateurChatCompletions"): ADAPTATEUR_BASE_SHA}


def charger_transport_pilote():
    """Importe le transport réel et l'adaptateur strict depuis leur dossier versé ; vérifie leurs empreintes."""
    d = RAC.chemin(TRANSPORT_DOSSIER_REL)
    for (mod, _), sha in list(ADAPTATEURS_ADMIS_PILOTE.items()) + list(TRANSPORTS_ADMIS_PILOTE.items()):
        if hashlib.sha256(open(os.path.join(d, mod + ".py"), "rb").read()).hexdigest() != sha:
            raise GP.ArretCourse(24, f"{mod}.py d'empreinte différente de la gelée")
    if d not in sys.path:
        sys.path.insert(1, d)
    import adaptateur_kimi_strict_v1 as AS
    import transport_kimi_reel_v1 as T
    return AS, T


def _t():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def prix_de_la_table():
    import calcul_devis_essaim_v4 as C4
    prix, _ = C4.tarifs()
    return tuple(prix["kimi"])


def borne():
    return GP.borne_pire(GP.plan_pstd(), GP.PRIX_GELES)["pire_usd"]


def parametres(plafond):
    return json.loads(json.dumps(GP.parametres_geles(plafond)))


def creer_registre(chemins, plafond_depense=None):
    b = borne()
    plafond = b if plafond_depense is None else float(plafond_depense)
    if plafond > b + 1e-9:
        raise GP.ArretCourse(24, f"plafond {plafond} > borne {b}")
    for p in (chemins.registre, chemins.ancre, chemins.cle):
        os.makedirs(os.path.dirname(p), exist_ok=True)
    RG.creer(chemins, parametres(plafond))
    return plafond


def creer_registre_pilote():
    """Étape unique avant le pilote, sous GO : registre au chemin écrit en dur, ancre et clé hors du dépôt."""
    return creer_registre(CHEMINS_PILOTE)


class Journal:
    def __init__(self, chemin):
        self.f = open(chemin, "x", encoding="utf-8")

    def ecrire(self, **l):
        self.f.write(json.dumps(dict(t=_t(), **l), ensure_ascii=False, sort_keys=True) + "\n")
        self.f.flush()

    def fermer(self):
        self.f.close()


def _sha_module_nom(nom):
    mod = sys.modules.get(nom)
    fichier = getattr(mod, "__file__", None)
    return hashlib.sha256(open(fichier, "rb").read()).hexdigest() if fichier else None


def _sha_module(obj):
    return _sha_module_nom(type(obj).__module__)


def _admis(obj, liste, quoi):
    cle = (type(obj).__module__, type(obj).__qualname__)
    if cle not in liste or liste[cle] != _sha_module(obj):
        raise GP.ArretCourse(24, f"{quoi} de classe {cle[0]}.{cle[1]} non admis (classe exacte et empreinte du module exigées)")


def _verifier_configuration(plan, adaptateur, plafond_depense, prix, transports_admis, adaptateurs_admis):
    if GP.empreinte_plan(plan) != GP.PLAN_SHA256:
        raise GP.ArretCourse(15, "plan différent du plan P-std gelé")
    table = prix_de_la_table()
    if table != GP.PRIX_GELES or (prix is not None and tuple(prix) != GP.PRIX_GELES):
        raise GP.ArretCourse(24, f"prix ≠ gelés {GP.PRIX_GELES}")
    if plafond_depense is not None and float(plafond_depense) > borne() + 1e-9:
        raise GP.ArretCourse(24, f"plafond {plafond_depense} > borne {borne()}")
    _admis(adaptateur, adaptateurs_admis, "adaptateur")
    if _sha_module_nom("adaptateur_fournisseur_v1") != ADAPTATEUR_BASE_SHA:
        raise GP.ArretCourse(24, "adaptateur de base d'empreinte différente")
    if getattr(adaptateur, "relances_internes", None) != 0:
        raise GP.ArretCourse(24, "relances internes de l'adaptateur ≠ 0")
    t = adaptateur.transport
    _admis(t, transports_admis, "transport")
    if getattr(t, "relances_internes", None) != 0:
        raise GP.ArretCourse(24, "relances internes du transport ≠ 0")


def courir_pilote(adaptateur, fournisseur_entree, chemin_journal):
    """Seule voie du pilote, sous GO : chemins écrits en dur ; adaptateur `AdaptateurKimiStrict` et transport
    `TransportKimiReel` seuls admis (classes exactes, empreintes gelées)."""
    return _courir(GP.plan_pstd(), adaptateur, fournisseur_entree, chemin_journal, CHEMINS_PILOTE, TRANSPORTS_ADMIS_PILOTE,
                   adaptateurs_admis=ADAPTATEURS_ADMIS_PILOTE)


def _courir(plan, adaptateur, fournisseur_entree, chemin_journal, chemins, transports_admis, plafond_depense=None, relancer=True,
            prix=None, max_tokens_par_role=None, adaptateurs_admis=None):
    j = Journal(chemin_journal)
    garde, reg = None, None

    def arret(code, detail):
        dep = garde.depense if garde else None
        inscrit = None
        if reg is not None and code not in (21, 22, 23, 25):
            try:
                reg.ecrire(evenement="arret", code=code, detail=str(detail)[:200], depense_usd=dep)
                inscrit = True
            except (OSError, RG.RegistreRefuse) as ex:
                inscrit = False
                j.ecrire(evenement="arret", code=CODE_ARRET_NON_INSCRIT, garde="arrêt non inscrit au registre",
                         detail=f"arrêt {code} ({detail}) non écrit : {type(ex).__name__}", depense_usd=dep, inscrit_au_registre=False)
                return CODE_ARRET_NON_INSCRIT
        j.ecrire(evenement="arret", code=code, garde=GP.CODES.get(code, {25: "verrou", 26: "arrêt non inscrit"}.get(code, "?")),
                 detail=detail, depense_usd=dep, inscrit_au_registre=inscrit)
        return code

    try:
        if adaptateur is None:
            j.ecrire(evenement="arret", code=CODE_SANS_CLIENT, garde="client", detail="aucun adaptateur : refus")
            return CODE_SANS_CLIENT, None
        _verifier_configuration(plan, adaptateur, plafond_depense, prix, transports_admis,
                                ADAPTATEURS_ADMIS_EPREUVES if adaptateurs_admis is None else adaptateurs_admis)
        reg = RG.Registre(chemins, parametres, borne())
        if plafond_depense is not None and abs(float(plafond_depense) - reg.plafond) > 1e-9:
            raise GP.ArretCourse(24, f"plafond {plafond_depense} ≠ plafond du registre {reg.plafond}")
        etat = reg.etat()
        if etat["suspens"] is not None:
            s = etat["suspens"]
            reg.ecrire(evenement="compte_a_la_reserve", id=s["id"], cout_usd=s["reserve_usd"], abandon=False,
                       motif="réserve en suspens à la réouverture")
            etat = reg.etat()
        garde = GP.Garde(plan, GP.PRIX_GELES, reg.plafond, etat)
        dern = reg.lignes[-1]
        if dern["evenement"] in ("echec", "compte_a_la_reserve") and not dern.get("abandon"):
            garde.relance_due(plan[garde.prochain])
        mt = dict(GP.PLAFOND_SORTIE, **(max_tokens_par_role or {}))
        j.ecrire(evenement="debut", depense_reprise_usd=round(garde.depense, 6), appels_regles=garde.prochain, echecs=garde.echecs,
                 plafond_depense_usd=reg.plafond)
        while garde.prochain < len(plan):
            appel = garde.a_relancer or plan[garde.prochain]
            texte = fournisseur_entree(appel)
            reserve = garde.avant(appel, texte, mt[appel["role"]])
            try:
                reg.ecrire(evenement="reserve", id=appel["id"], role=appel["role"], reserve_usd=reserve)  # relit tout d'abord
            except (OSError, RG.RegistreRefuse) as ex:
                garde.en_cours = None
                code = ex.code if isinstance(ex, RG.RegistreRefuse) else 22
                j.ecrire(evenement="arret", code=code, garde="réserve non inscrite : aucun appel",
                         detail=f"{type(ex).__name__}: {ex}"[:200], depense_usd=garde.depense, inscrit_au_registre=False)
                return code, garde
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
                garde.depense += (envois - 1) * reserve
                reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=envois * reserve, abandon=True, motif=str(ex)[:120])
                raise GP.ArretCourse(16, f"anomalie de réponse ({ex}) — compté à la réserve")
            except Exception as ex:  # noqa: BLE001
                garde.compter_reserve()
                reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=reserve, abandon=True, motif=type(ex).__name__)
                raise GP.ArretCourse(17, f"{type(ex).__name__}: {ex} — compté à la réserve")
            usage = rep.get("usage") if isinstance(rep, dict) else None
            avant = garde.depense
            try:
                c = garde.apres(appel, usage)
            except GP.ArretCourse:
                reg.ecrire(evenement="regle", id=appel["id"], cout_usd=garde.depense - avant, usage=usage if isinstance(usage, dict) else None,
                           motif="arrêt à la clôture")
                raise
            reg.ecrire(evenement="regle", id=appel["id"], cout_usd=c, usage=usage)
            j.ecrire(evenement="appel", id=appel["id"], usage=usage, cout_usd=round(c, 6), depense_usd=round(garde.depense, 6))
        reg.ecrire(evenement="fin", depense_usd=garde.depense)
        j.ecrire(evenement="fin", code=0, depense_usd=round(garde.depense, 6), appels_regles=garde.prochain, echecs=garde.echecs)
        return 0, garde
    except (GP.ArretCourse, RG.RegistreRefuse) as ex:
        return arret(ex.code, ex.detail), garde
    finally:
        if reg is not None:
            reg.fermer()
        j.fermer()


def main(argv):
    if len(argv) != 2 or os.path.exists(argv[1]):
        print("usage : lanceur_pilote_essaim_v3.py JOURNAL.jsonl (neuf) — exécution directe refusée (le pilote se lance sous GO par courir_pilote)", file=sys.stderr)
        return 2
    code, _ = courir_pilote(None, None, argv[1])
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
