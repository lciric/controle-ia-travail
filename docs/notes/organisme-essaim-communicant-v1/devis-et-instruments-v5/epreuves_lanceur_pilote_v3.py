#!/usr/bin/env python3
"""Épreuves (R5) du lanceur v3 et du registre v2, sur le faux fournisseur qui tient sa facture. Rejoue :
- les cas de la v4 (sains, gardes, A1 à A10), portés sur l'interface v3 ;
- les attaques N1 à N5 et V3a, V4a de la vérification de la v4
  (`devis-et-instruments-v4/verification-v1/outils/attaques_lanceur_v4_cl_v1.py`, `attaque_concurrence_v4_cl_v1.py`),
  sous leur forme réelle ;
- les écritures impossibles (réserve, arrêt).
Critère : code attendu ; ligne d'arrêt au journal ; dépense comptée ≥ facture et ≤ plafond — sauf cas « limite » déclarés,
dont le résultat est rapporté tel quel (V3a et V4a sous un transport admis, A8).
Aucun appel, aucun réseau. Graines : SeedSequence(20261126).spawn(16) (R9).
Usage : python -I -B epreuves_lanceur_pilote_v3.py SORTIE.json DOSSIER_NEUF"""
import hashlib
import json
import multiprocessing as mp
import os
import sys
import time

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import adaptateur_fournisseur_v1 as A  # noqa: E402
import faux_fournisseur_v1 as F  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import lanceur_pilote_essaim_v3 as L  # noqa: E402
import registre_depense_v2 as RG  # noqa: E402

RACINE_GRAINES = 20261126
P, PRIX = GP.plan_pstd(), GP.PRIX_GELES
BORNE = GP.borne_pire(P, PRIX)["pire_usd"]
ENTREE_ATTENDUE = {"proposeur": int((9000 + 3200) * 3.3), "message": int(3000 * 3.3)}
ENTREE_AU_PLAFOND = dict(GP.PLAFOND_ENTREE_OCTETS)
SS = np.random.SeedSequence(RACINE_GRAINES).spawn(16)


def entree(octets):
    return lambda appel: "x" * octets[appel["role"]]


def plaf_e(k, texte):
    return GP.PLAFOND_ENTREE_JETONS["proposeur"] if len(texte) > 20000 else GP.PLAFOND_ENTREE_JETONS["message"]


def plaf_s(k, mt):
    return mt


class Honnete(F.FauxFournisseur):
    """Transport d'épreuve qui MESURE ses envois (forme exigée du transport réel)."""

    def envoyer(self, requete):
        rep = F.FauxFournisseur.envoyer(self, requete)
        rep["tentatives"] = 1 + self._relances_reelles
        return rep


class Tueur(Honnete):
    def __init__(self, *a, tuer_au=101, **kw):
        super().__init__(*a, **kw)
        self.tuer_au, self.tue = tuer_au, False

    def envoyer(self, requete):
        rep = Honnete.envoyer(self, requete)
        if self.k == self.tuer_au and not self.tue:
            self.tue = True
            raise KeyboardInterrupt("processus tué après facturation")
        return rep


class Menteur(F.FauxFournisseur):
    """A3 sous sa forme réelle : relances cachées ET « tentatives = 1 »."""

    def envoyer(self, requete):
        rep = F.FauxFournisseur.envoyer(self, requete)
        rep["tentatives"] = 1
        return rep


class ReflexionMuette(Honnete):
    """A4 sous sa forme réelle : réflexion facturée, absente de l'usage rendu."""

    def envoyer(self, requete):
        rep = Honnete.envoyer(self, requete)
        if rep.get("usage"):
            rep["usage"].pop("reasoning_tokens", None)
            rep["usage"].pop("completion_tokens_details", None)
        return rep


class Lent(Honnete):
    def envoyer(self, requete):
        time.sleep(0.002)
        return Honnete.envoyer(self, requete)


def _sha_fichier(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def admis(*classes):
    return {(c.__module__, c.__qualname__): _sha_fichier(sys.modules[c.__module__].__file__) for c in classes}


ADMIS = admis(Honnete, Tueur, Lent, F.FauxFournisseur)


def chemins(d, nom):
    return RG.Chemins(os.path.join(d, f"registre-{nom}.jsonl"), os.path.join(d, f"etat-{nom}", "ancre.json"), os.path.join(d, f"etat-{nom}", "cle"))


def ff(i=0, cls=Honnete, **kw):
    kw.setdefault("rng", np.random.default_rng(SS[i]))
    return cls(PRIX, **kw)


def adapt(t):
    return A.AdaptateurChatCompletions(t, "kimi-gele")


def resultat(nom, garde_visee, codes, attendu, depense, plafond, facture, limite=None):
    sous = facture > depense + 1e-9
    au_dela = plafond is not None and depense > plafond + 1e-9
    tenu = codes == attendu and (limite is not None or (not sous and not au_dela))
    return {"cas": nom, "garde": garde_visee, "codes_attendus": attendu, "codes_rendus": codes, "depense_comptee_usd": round(depense, 6),
            "facture_du_faux_fournisseur_usd": round(facture, 6), "plafond_usd": plafond, "sous_compte": sous, "au_dela_du_plafond": au_dela,
            "limite_declaree": limite, "tenu": tenu}


def jouer(d):
    os.makedirs(d)
    R = []
    k = [0]

    def j():
        k[0] += 1
        return os.path.join(d, f"journal-{k[0]:03d}.jsonl")

    def courses(nom, garde_visee, attendu, t, ent=entree(ENTREE_ATTENDUE), plafond_registre=None, creer=True, invocations=1, ch=None,
                ad=None, transports=None, limite=None, **kw):
        ch = ch or chemins(d, nom)
        if creer:
            L.creer_registre(ch, plafond_registre)
        codes, dep, plaf = [], 0.0, None
        for _ in range(invocations):
            try:
                code, g = L._courir(P, ad or adapt(t), ent, j(), ch, ADMIS if transports is None else transports, **kw)
            except KeyboardInterrupt:
                code, g = "processus tué", None
            codes.append(code)
        try:
            r = RG.Registre(ch, L.parametres, BORNE)
            dep, plaf = r.etat()["depense"], r.plafond
            r.fermer()
        except RG.RegistreRefuse as ex:
            dep, plaf = _depense_brute(ch), None
        R.append(resultat(nom, garde_visee, codes, attendu, dep, plaf if plaf is not None else (plafond_registre or BORNE), getattr(t, "facture", 0.0), limite))
        return ch

    # --- sains ---
    courses("sain : P-std entier", "toutes", [0], ff(0))
    courses("sain : tout au plafond de jetons", "sortie, entrée, dépense", [0], ff(1, entree=plaf_e, sortie=plaf_s), ent=entree(ENTREE_AU_PLAFOND))
    courses("sain : 74 échecs relancés", "échecs", [0], ff(2, erreurs_aux=range(0, 148, 2)))
    courses("sain : pire extrême (plafonds, 74 échecs facturés)", "dépense", [0],
            ff(3, entree=plaf_e, sortie=plaf_s, erreurs_aux=range(0, 148, 2), erreur_facturee=True), ent=entree(ENTREE_AU_PLAFOND))
    courses("sain : processus tué pendant l'appel 101, puis reprise", "registre persistant", ["processus tué", 0], ff(4, cls=Tueur), invocations=2)
    # --- configuration (A1, A6, N4, N5, transports) ---
    ch = chemins(d, "A1")
    L.creer_registre(ch)
    t = ff(5)
    P2 = P + [dict(a, id=a["id"] + "-bis") for a in P if a["role"] == "proposeur"]
    code, _ = L._courir(P2, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    R.append(resultat("A1 plan doublé", "plan", [code], [15], 0.0, BORNE, t.facture))
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS, plafond_depense=10 ** 6)
    R.append(resultat("A1b plafond 1e6 passé à courir", "configuration", [code], [24], 0.0, BORNE, t.facture))
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS, prix=(0.0, 0.0))
    R.append(resultat("A6 prix (0, 0)", "configuration", [code], [24], 0.0, BORNE, t.facture))
    ch = chemins(d, "N4")
    os.makedirs(os.path.dirname(ch.ancre))
    RG.creer(ch, L.parametres(10 ** 6))  # registre forgé directement, plafond 1e6
    t = ff(5)
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    R.append(resultat("N4 registre forgé par RG.creer avec plafond 1e6", "registre", [code], [24], 0.0, BORNE, t.facture))

    class Adapt3(A.AdaptateurChatCompletions):
        def appeler(self, appel, texte, mt):
            for _ in range(2):
                self.transport.envoyer({"model": self.modele, "messages": [{"role": "user", "content": texte}], "max_tokens": mt})
            return super().appeler(appel, texte, mt)
    t = ff(6)
    courses("N5 sous-classe de l'adaptateur qui envoie trois fois", "configuration", [24], t, ad=Adapt3(t, "kimi-gele"))
    t = ff(6, cls=Menteur, relances_internes=2, relances_declarees=0)
    courses("V3a transport menteur NON admis (classe hors liste)", "configuration", [24], t)
    t = ff(6, cls=ReflexionMuette, reflexion_hors=8000)
    courses("V4a transport à réflexion muette NON admis", "configuration", [24], t)
    t = ff(6)
    code, _ = L.courir_pilote(adapt(t), entree(ENTREE_ATTENDUE), j())
    R.append(resultat("courir_pilote avec un faux transport et l'adaptateur générique : refusé", "configuration", [code], [24], 0.0, BORNE, t.facture))
    # --- limites : la même chose sous un transport ADMIS (le transport réel serait fautif) ---
    t = ff(7, cls=Menteur, relances_internes=2, relances_declarees=0, entree=plaf_e, sortie=plaf_s)
    courses("V3a sous transport admis (relances cachées, tentatives=1 rendues)", "aucune : hors de portée du code", [0], t,
            ent=entree(ENTREE_AU_PLAFOND), transports={**ADMIS, **admis(Menteur)},
            limite="non arrêtée par le code : relecture du transport réel, tentatives mesurées, essai de fumée (H1), limite chez le fournisseur")
    t = ff(7, cls=ReflexionMuette, reflexion_hors=8000, entree=plaf_e, sortie=plaf_s)
    courses("V4a sous transport admis (réflexion facturée, absente de l'usage)", "aucune : hors de portée du code", [0], t,
            ent=entree(ENTREE_AU_PLAFOND), transports={**ADMIS, **admis(ReflexionMuette)},
            limite="non arrêtée par le code : H2 à établir à l'essai de fumée, champ de réflexion du fournisseur lu par l'adaptateur, limite chez le fournisseur")
    # --- registre : N1, N2, A2, absent, altéré ---
    t = ff(8)
    courses("A2 seconde invocation après une fin", "course close", [0, 23], t, invocations=2)
    t = ff(8)
    ch = chemins(d, "N1")
    L.creer_registre(ch)
    L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    autre = RG.Chemins(os.path.join(d, "ailleurs", "registre-N1b.jsonl"), ch.ancre, ch.cle)
    os.makedirs(os.path.dirname(autre.registre))
    try:
        L.creer_registre(autre)
        code = "créé"
    except RG.RegistreRefuse as ex:
        code = ex.code
    R.append(resultat("N1 registre neuf ailleurs, même ancre : création refusée", "registre", [code], [22], 0.0, BORNE, 0.0))
    ch_b = chemins(d, "N1-tiers")
    L.creer_registre(ch_b)  # registre neuf avec sa propre ancre, présenté sous l'ancre du pilote N1
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), RG.Chemins(ch_b.registre, ch.ancre, ch.cle), ADMIS)
    R.append(resultat("N1b registre neuf présenté sous l'ancre de la course", "registre", [code], [22], 0.0, BORNE, 0.0))
    # N2 : tronqué puis re-scellé (avec la clé) ; puis re-scellé sans la clé
    t = ff(9, cls=Tueur, tuer_au=40)
    ch = chemins(d, "N2")
    L.creer_registre(ch)
    try:
        L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    except KeyboardInterrupt:
        pass
    premiere = open(ch.registre, encoding="utf-8").readline()
    open(ch.registre, "w", encoding="utf-8").write(premiere)
    cle = open(ch.cle, "rb").read()
    mac, n = RG._sceau(cle, premiere.encode())
    open(ch.sceau, "w").write(json.dumps({"hmac": mac, "lignes": n}) + "\n")
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    R.append(resultat("N2 tronqué à la création puis re-scellé avec la clé", "registre (ancre)", [code], [22], 0.0, BORNE, 0.0))
    h = hashlib.sha256(premiere.encode()).hexdigest()
    open(ch.sceau, "w").write(json.dumps({"hmac": h, "lignes": 1}) + "\n")
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    R.append(resultat("N2b tronqué puis re-scellé sans la clé (empreinte nue)", "registre (sceau)", [code], [22], 0.0, BORNE, 0.0))
    courses("registre absent", "registre", [21], ff(10), creer=False)
    # N3 : deux processus, même registre
    ch = chemins(d, "N3")
    L.creer_registre(ch)
    q = mp.get_context("fork").Queue()

    def enfant(i):
        t = Lent(PRIX, entree=plaf_e, sortie=plaf_s, rng=np.random.default_rng(SS[11 + i]))
        try:
            code, _ = L._courir(P, adapt(t), entree(ENTREE_AU_PLAFOND), os.path.join(d, f"journal-N3-{i}.jsonl"), ch, ADMIS)
            q.put((i, code, t.facture))
        except Exception as ex:  # noqa: BLE001
            q.put((i, type(ex).__name__, t.facture))
    ps = [mp.get_context("fork").Process(target=enfant, args=(i,)) for i in (1, 2)]
    ps[0].start()
    time.sleep(0.5)
    ps[1].start()
    out = sorted([q.get() for _ in ps])
    [p.join() for p in ps]
    try:
        r2 = RG.Registre(ch, L.parametres, BORNE)
        dep = r2.etat()["depense"]
        r2.fermer()
        relu = "relu"
    except RG.RegistreRefuse as ex:
        dep, relu = _depense_brute(ch), f"refus {ex.code} (course close)"
    R.append(resultat(f"N3 deux processus simultanés (le second, lancé 0,5 s après) ; registre {relu} après", "verrou", [o[1] for o in out], [0, 25],
                      dep, BORNE, sum(o[2] for o in out)))
    # N3b : course entrelacée dans le même processus (seconde ouverture pendant la première)
    ch = chemins(d, "N3b")
    L.creer_registre(ch)

    class Entrelace(Honnete):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            self.resultat_b = None

        def envoyer(self, requete):
            if self.k == 5 and self.resultat_b is None:
                tb = ff(12)
                self.resultat_b = L._courir(P, adapt(tb), entree(ENTREE_ATTENDUE), j(), ch, ADMIS)[0]
                self.facture += tb.facture
            return Honnete.envoyer(self, requete)
    t = Entrelace(PRIX, rng=np.random.default_rng(SS[13]))
    code_a, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, {**ADMIS, **admis(Entrelace)})
    dep = _depense_brute(ch)
    R.append(resultat("N3b course B lancée pendant l'appel 5 de la course A, même registre", "verrou", [code_a, t.resultat_b], [0, 25],
                      dep, BORNE, t.facture))
    # registre changé hors de la course, pendant la course (relecture avant chaque réserve)
    ch = chemins(d, "pendant")
    L.creer_registre(ch)

    class Saboteur(Honnete):
        def envoyer(self, requete):
            if self.k == 20:
                with open(ch.registre, "a", encoding="utf-8") as f:
                    f.write('{"n": 999}\n')
            return Honnete.envoyer(self, requete)
    t = Saboteur(PRIX, rng=np.random.default_rng(SS[14]))
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, {**ADMIS, **admis(Saboteur)})
    R.append(resultat("registre changé pendant la course (ligne ajoutée hors course)", "registre (relu avant chaque réserve)", [code], [22],
                      _depense_brute(ch), BORNE, t.facture))
    # écriture de l'arrêt impossible (l. 155 de la v2) : arrêt au journal, code 26, jamais avalé
    ch = chemins(d, "arret-impossible")
    L.creer_registre(ch)
    vrai = RG._ecrire_atomique

    def panne(chemin, texte):
        raise OSError("disque plein (artefact)")
    RG._ecrire_atomique = panne
    try:
        code, _ = L._courir(P, adapt(ff(15)), entree(ENTREE_ATTENDUE), j(), ch, ADMIS, max_tokens_par_role={"proposeur": 24001})
    finally:
        RG._ecrire_atomique = vrai
    jr = [json.loads(x) for x in open(os.path.join(d, f"journal-{k[0]:03d}.jsonl"), encoding="utf-8")]
    try:
        RG.Registre(ch, L.parametres, BORNE).fermer()
        apres = "relu"
    except RG.RegistreRefuse as ex:
        apres = ex.code
    R.append({"cas": "écriture de l'arrêt impossible au registre (arrêt 10 provoqué)", "garde": "écriture (jamais avalée)",
              "codes_attendus": [26, 22], "codes_rendus": [code, apres], "ligne_d_arret": jr[-1],
              "tenu": code == 26 and apres == 22 and jr[-1].get("inscrit_au_registre") is False})
    # écriture impossible, forme indépendante des droits : sceau remplacé par un dossier pendant la course
    ch = chemins(d, "sceau-dossier")
    L.creer_registre(ch)

    class Bloque2(Honnete):
        def envoyer(self, requete):
            if self.k == 9:
                os.remove(ch.sceau)
                os.makedirs(ch.sceau)
            return Honnete.envoyer(self, requete)
    t = Bloque2(PRIX, rng=np.random.default_rng(SS[15]))
    code, _ = L._courir(P, adapt(t), entree(ENTREE_ATTENDUE), j(), ch, {**ADMIS, **admis(Bloque2)})
    jr = [json.loads(x) for x in open(os.path.join(d, f"journal-{k[0]:03d}.jsonl"), encoding="utf-8")]
    R.append(resultat("écriture de la réserve impossible (sceau remplacé par un dossier) : aucun appel", "écriture (jamais avalée)", [code], [22],
                      _depense_brute(ch), BORNE, t.facture))
    R[-1]["ligne_d_arret"] = jr[-1]
    # --- gardes de la v4, sous la v3 ---
    try:
        adapt(ff(1, relances_internes=2))
        R.append({"cas": "A3 relances internes déclarées (2)", "tenu": False})
    except A.ConfigurationRefusee:
        R.append({"cas": "A3 relances internes déclarées (2) : adaptateur refusé", "garde": "configuration", "codes_attendus": ["refus"], "codes_rendus": ["refus"], "tenu": True})
    courses("A3b relances cachées, tentatives mesurées 3", "facturation hors borne", [16], ff(1, relances_internes=2, relances_declarees=0))
    courses("A4 réflexion rendue hors de completion_tokens", "sortie", [10], ff(1, entree=plaf_e, sortie=plaf_s, reflexion_hors=8000), ent=entree(ENTREE_AU_PLAFOND))
    courses("A5 panne après facturation", "erreur après envoi", [17], ff(1, panne_apres_facture_au=30))
    courses("A7 sortie négative", "facturation hors borne", [16], ff(1, usage_negatif_au=3))
    courses("A7b usage absent", "facturation hors borne", [16], ff(1, usage_absent_au=7))
    courses("modèle servi différent", "facturation hors borne", [16], ff(1, modele_servi="autre"))
    courses("A8 entrée rendue 256 000 au dernier appel, plafond 176,6", "entrée", [11],
            ff(1, entree=lambda k, tx: 256000 if k == 743 else plaf_e(k, tx), sortie=plaf_s), ent=entree(ENTREE_AU_PLAFOND), plafond_registre=176.6,
            limite="un appel hors H3 n'est borné que par la fenêtre du modèle et la limite chez le fournisseur")
    courses("A10 tous les appels échouent, relancer=False", "échecs", [13], ff(1, erreurs_aux=range(0, 10 ** 6)), relancer=False)
    courses("75 échecs relancés", "échecs", [13], ff(2, erreurs_aux=range(0, 150, 2)))
    courses("max_tokens 24 001", "sortie", [10], ff(1), max_tokens_par_role={"proposeur": 24001})
    courses("entrée de 64 961 octets", "entrée", [11], ff(1), ent=entree({"proposeur": GP.PLAFOND_ENTREE_OCTETS["proposeur"] + 1, "message": 9900}))
    courses("plafond du registre 50 USD", "dépense", [14], ff(0), plafond_registre=50.0)
    ch = chemins(d, "sans")
    L.creer_registre(ch)
    code, _ = L._courir(P, None, entree(ENTREE_ATTENDUE), j(), ch, ADMIS)
    R.append(resultat("aucun adaptateur", "client", [code], [20], 0.0, BORNE, 0.0))
    g = GP.Garde(P, PRIX, BORNE)
    msg = next(a for a in P if a["role"] == "message")
    for a in P[:P.index(msg)]:
        g.avant(a, "x", 10)
        g.apres(a, {"entree": 1, "sortie": 1})
    g.avant(msg, "x", 2000)
    g.echec(msg)
    try:
        g.avant(dict(msg, role="proposeur"), "x" * 60000, 24000)
        code = 0
    except GP.ArretCourse as ex:
        code = ex.code
    R.append({"cas": "A9 relance déguisée", "garde": "plan", "codes_attendus": [15], "codes_rendus": [code], "tenu": code == 15})
    R.extend(jouer_transport_reel(d, j))
    return R


CLE_FACTICE = "sk-FAUSSE-cle-d-epreuve-0123456789abcdef"


def jouer_transport_reel(d, j):
    """Le transport réel versé (`transport-kimi-reel-v1`), sous l'adaptateur strict et les listes d'admission DU PILOTE,
    contre le faux serveur local de ce même dossier (127.0.0.1, clé factice). Aucun réseau sortant."""
    AS, T = L.charger_transport_pilote()
    import faux_serveur_kimi_v1 as FS
    R = []
    rng = np.random.default_rng(np.random.SeedSequence(RACINE_GRAINES, spawn_key=(99,)))
    sorties = rng.integers(3000, 12801, size=2000)

    def regle(extra=None):
        def f(k, corps):
            r = {"completion": int(min(sorties[k % 2000], corps.get("max_tokens") or 0)) if (corps.get("max_tokens") or 0) > 2000 else 300}
            if extra:
                r.update(extra(k, corps) or {})
            return r
        return f

    def transport(srv):
        return T.TransportKimiReel(amont=srv.url, environ={"KIMI_API_KEY": CLE_FACTICE}, delai_silence_s=5, delai_total_s=20)

    def course(nom, garde_visee, attendu, extra=None, fabrique=None, adaptateurs=None, limite=None):
        ch = chemins(d, f"reel-{len(R):02d}")
        L.creer_registre(ch)
        with FS.FauxServeurKimi(regle(extra)) as srv:
            try:
                ad = (fabrique or AS.AdaptateurKimiStrict)(transport(srv))
            except A.ConfigurationRefusee:
                R.append({"cas": nom, "garde": garde_visee, "codes_attendus": attendu, "codes_rendus": ["refus à la construction"],
                          "tenu": attendu == ["refus à la construction"] and srv.nombre == 0, "requetes_au_serveur": srv.nombre})
                return
            code, _ = L._courir(P, ad, entree(ENTREE_ATTENDUE), j(), ch, L.TRANSPORTS_ADMIS_PILOTE,
                                adaptateurs_admis=L.ADAPTATEURS_ADMIS_PILOTE if adaptateurs is None else adaptateurs)
            facture, n = srv.facture_usd, srv.nombre
        lignes = [json.loads(x) for x in open(ch.registre, encoding="utf-8")]
        reserves = sum(1 for x in lignes if x["evenement"] == "reserve")
        r = resultat(nom, garde_visee, [code], attendu, _depense_brute(ch), BORNE, facture, limite)
        r.update(requetes_au_serveur=n, reserves_ecrites=reserves, une_requete_par_reserve=(n == reserves))
        r["tenu"] = r["tenu"] and n == reserves
        R.append(r)

    course("réel sain : P-std entier, transport réel et adaptateur strict, 4 échecs", "toutes", [0],
           extra=lambda k, c: {"statut": 429} if k in (5, 300) else ({"statut": 500, "facture": (12000, c["max_tokens"])} if k == 50
                                                                      else ({"coupure_apres": 2, "facture": (12000, 1000)} if k == 100 else None)))

    class StrictDerive(AS.AdaptateurKimiStrict):
        pass
    course("réel : sous-classe de l'adaptateur strict", "configuration", [24], fabrique=StrictDerive)
    course("réel : adaptateur générique avec le transport réel, sous les listes du pilote", "configuration", [24],
           fabrique=lambda tr: A.AdaptateurChatCompletions(tr, T.MODELE))
    course("réel : adaptateur strict, empreinte gelée différente", "configuration", [24],
           adaptateurs={("adaptateur_kimi_strict_v1", "AdaptateurKimiStrict"): "0" * 64})
    course("réel : champ de réflexion absent de l'usage (appel 3)", "facturation hors borne", [16],
           extra=lambda k, c: {"usage": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150}} if k == 3 else None)
    course("réel : réflexion rendue hors de completion_tokens (appel 3, 30 000)", "sortie", [10],
           extra=lambda k, c: {"reflexion_hors": 30000} if k == 3 else None)
    course("réel : autre modèle servi (appel 3)", "facturation hors borne", [16], extra=lambda k, c: {"modele": "kimi-k3"} if k == 3 else None)
    course("réel : facture au-delà de l'usage rendu, sans trace (appel 3, 8 000 jetons cachés)", "aucune : hors de portée du code", [0],
           extra=lambda k, c: {"facture": (12000, 8300)} if k == 3 else None,
           limite="facture cachée sans trace dans l'usage : H1, rapprochement de la console à l'essai de fumée, limite chez le fournisseur")
    return R


def _depense_brute(ch):
    """Dépense lue ligne à ligne, sans contrôle (pour rapporter un registre refusé)."""
    dep, ouvert = 0.0, None
    try:
        for brut in open(ch.registre, encoding="utf-8"):
            try:
                l = json.loads(brut)
            except ValueError:
                continue
            ev = l.get("evenement")
            if ev == "reserve":
                ouvert = l
            elif ev in ("regle", "echec", "compte_a_la_reserve"):
                dep += l.get("cout_usd", 0.0)
                ouvert = None
    except OSError:
        return 0.0
    return dep + (ouvert["reserve_usd"] if ouvert else 0.0)


def main(argv):
    if len(argv) != 3 or os.path.exists(argv[1]) or os.path.exists(argv[2]):
        print("usage : epreuves_lanceur_pilote_v3.py SORTIE.json DOSSIER (neufs)", file=sys.stderr)
        return 2
    R = jouer(argv[2])
    out = {"version": "epreuves-lanceur-pilote-v3", "graines": f"SeedSequence({RACINE_GRAINES}).spawn(16)", "numpy": np.__version__,
           "prix_geles": list(PRIX), "plan_sha256": GP.PLAN_SHA256, "borne_pire_pstd": GP.borne_pire(P, PRIX),
           "registre_pilote": L.REGISTRE_PILOTE_REL, "transports_admis_pilote": len(L.TRANSPORTS_ADMIS_PILOTE),
           "cas": R, "tenus": sum(bool(r.get("tenu")) for r in R), "total": len(R)}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    for r in R:
        print("TENU  " if r.get("tenu") else "CASSÉ ", r.get("codes_attendus"), r.get("codes_rendus"), r["cas"],
              r.get("depense_comptee_usd", ""), r.get("facture_du_faux_fournisseur_usd", ""))
    return 0 if all(r.get("tenu") for r in R) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
