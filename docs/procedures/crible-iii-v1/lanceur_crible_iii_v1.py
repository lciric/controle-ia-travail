"""Lanceur du crible (iii) — v1 (fichier neuf ; dérivé du lanceur v74 du pilote MR-2, `demonstrations/pilote_mr2_v74.py` de l'arbre
605e0f6, qui n'est pas modifié : sa configuration v12, ses relais, sa commande, son gardien, son texte servi G0, ses contrôles C-16
et C-17 et son lecteur du relevé de la sonde v74 sont repris tels quels, par import depuis l'arbre).

Pièce qui fait foi : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-version-foi-v1.md` (`91b4bf30…`), sections
« Métrique », « Plan d'analyse », « Liste d'arrêt » ; noyau : `crible_iii_v1.py` (même dossier).

Sous-commandes (sorties imprimées : empreintes et contrôles seulement ; aucun monde, aucune loi, aucun texte servi) :
  secret    FICHIER_PRIVE
  generer   --arbre A --secret S --phrase-fichier F --texte-sha256 H --sortie PRIVE/MONDES.json [--processus 4] [--public]
  preparer  --arbre A --mondes M --mondes-sha256 H --texte-sha256 T
  jouer     --mode a_blanc|reel --arbre A --mondes M --mondes-sha256 H --texte-sha256 T --sortie DOSSIER --echeance-utc-s E
            --releve-sonde RELEVE
            à blanc : [--bornes-a-blanc APPEL,MONDE,MARGE] [--scenarios-a-blanc FICHIER]
            réel, exigés : --texte T --registre-go R --go-credits GO --go-hors GO --mondes-shas S1,…,S20
                           --registre-lancements FICHIER (hors dépôt) --addendum ADDENDUM
  rapatrier --source DOSSIER --destination DOSSIER --mondes M --mondes-sha256 H
  empreintes --arbre A                (empreintes du code du crible et des pièces de l'arbre qu'il emploie : pour l'addendum)
  sonde-gabarits --mode a_blanc|reel --arbre A --mondes M_PUBLIC --mondes-sha256 H --texte-sha256 T --sortie DOSSIER
            --releve-sonde RELEVE [--scenarios-a-blanc F] ; réel : --registre-go R --go-sonde GO (κiii0) --registre-lancements F
            (trois appels sur le monde de développement 1 : G1 par Pr-2, G2 par Pr-4 et par Pr-2 ; aucune couverture lue)
(la mesure et la lecture sont `mesure_crible_iii_v1.py` et `lire_crible_iii_v1.py`, même dossier).
Codes : 0 conforme (crible mené au bout, ou arrêté par la ligne du minimum : « non concluant », mesure permise) ; 2 refus nommé
(rien appelé) ; 3 arrêt (pièces versées ; ni mesure ni lecture d'issue).
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import multiprocessing
import os
import platform
import secrets
import socket
import subprocess
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_iii_v1 as N  # noqa: E402
import mesure_crible_iii_v1 as ME  # noqa: E402

VERSION = "lanceur-crible-iii-v1"
DOSSIER_DU_CODE = "docs/procedures/crible-iii-v1"
FICHIERS_DU_CRIBLE = ("crible_iii_v1.py", "lanceur_crible_iii_v1.py", "mesure_crible_iii_v1.py", "lire_crible_iii_v1.py",
                      "relais_factice_crible_iii_v1.py")
CONFIGURATION_FICHIER_SHA = "f69503dd4ba5e57a8bde230b3861571549d9598382808a8f3c0f4fa664ea818b"   # configuration v12
CONFIGURATION_SHA = "184ba783d8939bb3e0720b818727465a0444b087309386050efd8aca28beef65"           # empreinte_configuration
TETE_ARBRE = "605e0f60f3eed0948948e6a4eb15cb73de1d03de"
ETIQUETTE_EPISODES = "crible-iii-v1|episodes-developpement"
REGLE_DES_GRAINES = ("racine : entier de l'empreinte sha256 du texte qui fait foi ; ensembles de H : SeedSequence(racine, "
                     "spawn_key=(r, 40)) ; rééchantillonnage : (99, b) ; monde r : graine_monde_crible (étiquette crible-iii-v1, "
                     "secret, phrase, empreinte du texte, r) puis les 8 tirages de generer_v4 ; épisodes : SeedSequence(entier "
                     "gros-boutiste des 16 premiers octets de sha256(« crible-iii-v1|episodes-developpement| » + empreinte du "
                     "devis)) ; oracle : cle(« oracle-crible-iii », empreinte du devis) ; jeton des relais : secrets.token_hex(16)")
PHRASE_PUBLIQUE = "développement public, jamais pour un vrai monde"


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def sha_fichier(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def imprimer(o):
    print(json.dumps(o, ensure_ascii=False, sort_keys=True, default=list))


def ecrire_scelle(chemin, objet):
    return ME.ecrire_scelle(chemin, objet)


# --- arbre de l'organisme (lecture seule) ----------------------------------------------------------------------------------------

class Arbre:
    """Modules du pilote pris dans l'arbre 605e0f6 : P (cœur v70), PR (proposeurs v70), PC (configuration v12), S74 (sonde v74),
    L74 (lanceur v74, pour `attendu_du_releve` et la configuration gelée)."""

    def __init__(self, racine):
        racine = os.path.abspath(racine)
        if not os.path.isdir(os.path.join(racine, "pole")):
            raise N.Refus(f"arbre de l'organisme illisible : {racine}")
        if racine not in sys.path:
            sys.path.insert(0, racine)
        from pole import pilote_mr2_v70 as P
        from pole import proposeurs_pilote_v70 as PR
        from pole import proposeurs_pilote_v72 as PC
        from pole import sonde_pilote_v74 as S74
        from demonstrations import pilote_mr2_v74 as L74
        self.racine, self.P, self.PR, self.PC, self.S74, self.L74 = racine, P, PR, PC, S74, L74
        self.V4, self.M, _ = P.charger_mr2()

    def configuration(self):
        """Configuration v12 de l'arbre, seule permise ; sinon arrêt avant tout appel."""
        if sha_fichier(self.L74.CONFIGURATION) != CONFIGURATION_FICHIER_SHA:
            raise N.Refus("configuration autre que v12 (fichier de l'arbre différent)")
        conf, _ = self.PC.lire_configuration(self.L74.CONFIGURATION)
        return exiger_configuration(self, conf)

    def empreintes(self):
        return self.L74.empreintes_du_code(self.racine)


def exiger_configuration(arbre, conf):
    if arbre.PR.empreinte_configuration(conf) != CONFIGURATION_SHA:
        raise N.Refus("configuration autre que v12 (empreinte de la configuration lue différente)")
    for p in N.PROPOSEURS:
        if conf["proposeurs"][p]["credits"] != "claude":
            raise N.Refus(f"{p} : crédits de Claude attendus (variante, R-2992)")
    return conf


def exiger_releve_sonde(arbre, conf, chemin):
    """Le relevé de la sonde v74 (configuration v12, déjà jouée) : exigé sans condition, lu par le lecteur gelé du pilote."""
    try:
        return arbre.S74.exiger_releve(conf, chemin, arbre.L74.attendu_du_releve(conf, arbre.racine))
    except arbre.P.Refus as e:
        raise N.Refus(f"relevé de la sonde v74 : {e}") from None


# --- mondes : graine du crible, huit tirages de generer_v4 ------------------------------------------------------------------------

def _generer_un(args):
    racine_arbre, graine, r = args
    a = Arbre(racine_arbre)
    spec, rap, refus = a.P.sans_chemin_v52b(a.V4.generer_v4, graine)
    if spec is None:
        return {"monde": r, "spec": None, "refus": list(refus)}
    a.P.exiger_dimensions(spec)
    return {"monde": r, "spec": spec, "spec_sha256": a.P.sha_spec(spec), "refus": list(refus),
            "conforme": bool(rap and rap["conforme"])}


def exiger_mondes_generes(res):
    """Un monde sans tirage conforme en 8 → arrêt avant tout appel ; vingt devis distincts."""
    if len(res) != N.N_MONDES or any(x["spec"] is None for x in res):
        r = next((x for x in res if x["spec"] is None), {"monde": None, "refus": "nombre de mondes"})
        raise N.Refus(f"monde {r['monde']} : aucun tirage conforme en 8 (refus {r['refus']}) : arrêt avant tout appel")
    mondes = [{"monde": x["monde"], "spec": x["spec"], "spec_sha256": x["spec_sha256"]} for x in sorted(res, key=lambda x: x["monde"])]
    if len({w["spec_sha256"] for w in mondes}) != N.N_MONDES:
        raise N.Refus("mondes : deux devis égaux")
    return mondes


def generer(a):
    arbre = Arbre(a.arbre)
    if a.public:
        secret, phrase = bytes(32), PHRASE_PUBLIQUE
    else:
        secret = arbre.P.lire_secret(a.secret)
        with open(a.phrase_fichier, "rb") as f:
            b = f.read()
        if not b.endswith(b"\n") or b.count(b"\n") != 1:
            raise N.Refus("phrase : une ligne finie par un retour à la ligne")
        phrase = b[:-1].decode("utf-8")
    arbre.P.exiger_hors_depot(a.sortie, "fichier des mondes")
    rs = (1,) if a.un_seul else N.MONDES
    if a.un_seul and not a.public:
        raise N.Refus("generer --un-seul : monde de développement public seulement (sonde des gabarits)")
    graines = [(arbre.racine, N.graine_monde_crible(secret, phrase, a.texte_sha256, r), r) for r in rs]
    with multiprocessing.get_context("spawn").Pool(min(a.processus, len(graines))) as pool:
        res = pool.map(_generer_un, graines)
    if a.un_seul:
        if res[0]["spec"] is None:
            raise N.Refus(f"monde 1 : aucun tirage conforme en 8 (refus {res[0]['refus']})")
        mondes = [{"monde": 1, "spec": res[0]["spec"], "spec_sha256": res[0]["spec_sha256"]}]
    else:
        mondes = exiger_mondes_generes(res)
    d = os.path.dirname(os.path.abspath(a.sortie))
    sha = arbre.P.ecrire_prive(a.sortie, {"version": VERSION, "texte_sha256": a.texte_sha256, "public": bool(a.public),
                                          "mondes": mondes}, [d])
    arbre.P.ecrire_prive(a.sortie + ".engagement.json",
                         {"version": VERSION, "texte_sha256": a.texte_sha256, "fichier_mondes_sha256": sha, "public": bool(a.public),
                          "mondes_sha256": [w["spec_sha256"] for w in mondes]}, [d])
    imprimer({"fichier_mondes_sha256": sha, "controles": [{"monde": x["monde"], "spec_sha256": x["spec_sha256"],
                                                           "conforme": x["conforme"], "tirages_refuses": x["refus"]}
                                                          for x in sorted(res, key=lambda x: x["monde"])]})
    return 0


def lire_mondes(chemin, sha_attendue, repetes_permis=False):
    with open(chemin, "rb") as f:
        b = f.read()
    if hashlib.sha256(b).hexdigest() != sha_attendue:
        raise N.Refus("fichier des mondes : empreinte différente")
    doc = json.loads(b)
    mondes = doc.get("mondes") if isinstance(doc, dict) else None
    if not isinstance(mondes, list) or [w.get("monde") for w in mondes] != list(N.MONDES):
        raise N.Refus(f"fichier des mondes : {N.N_MONDES} mondes numérotés de 1 à {N.N_MONDES} attendus")
    if not repetes_permis and len({w["spec_sha256"] for w in mondes}) != N.N_MONDES:
        raise N.Refus("fichier des mondes : devis en double")
    return doc, mondes


# --- préparation : textes servis G0, G1, ensembles de H, C-16, C-17 -----------------------------------------------------------------

def episodes_crible(arbre, spec, n=400):
    """400 épisodes de développement : règle du bloc gelé du pilote, étiquette neuve « crible-iii-v1 »."""
    import numpy as np
    loi = arbre.P.compiler_monde(spec)
    cle = int.from_bytes(hashlib.sha256((ETIQUETTE_EPISODES + "|" + arbre.P.sha_spec(spec)).encode()).digest()[:16], "big")
    rng = np.random.default_rng(np.random.SeedSequence(cle))
    Z, G = arbre.M.tirer_instances(rng, n, spec["dimension"], spec["sous_populations"])
    Y = arbre.M.tirer_issues(rng, arbre.M.probas(loi, Z, G))
    return [{"z": [float(x) for x in z], "g": int(g), "y": int(y)} for z, g, y in zip(Z, G, Y)]


_OUTILS = {}


def _outils(racine):
    if racine not in _OUTILS:
        _OUTILS[racine] = ME.OutilsMR2(racine)
    return _OUTILS[racine]


def preparer_crible(arbre, conf, mondes, texte_sha256, outils=None):
    """Avant tout appel : mondes compilés, K1 servie (celle que la mesure retire), C-16, épisodes, C-17, textes G0 et G1 bâtis et
    relus, pire G2 sous 53 000 octets, ensembles de H tirés et filtrés. Rend (servis, contrôles publics)."""
    P = arbre.P
    outils = outils or _outils(arbre.racine)
    racine = N.racine_graines(texte_sha256)
    pm_, episodes = {}, {}
    for w in mondes:
        P.exiger_dimensions(w["spec"])
        P.compiler_monde(w["spec"])
        spec, sha, o, k1, eid_k1, infos = outils.oracle_et_k1(w)
        cond = {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"}
        premiere = sorted(c for c, b in cond.items() if b not in cond)
        if len(premiere) != 1 or eid_k1 in cond.values():
            raise N.Refus(f"monde {w['monde']} : première conditionnelle non unique, ou condition = effet de K1")
        pm_[w["monde"]] = {"spec": spec, "sha": sha, "o": o, "k1": k1, "eid_k1": eid_k1, "infos": infos, "premiere": premiere[0]}
        episodes[w["monde"]] = episodes_crible(arbre, spec)
    try:
        c16, _ = P.jouer_c16(pm_)
        c17 = P.jouer_c17(pm_, episodes)
    except P.Refus as e:
        raise N.Refus(f"C-16 ou C-17 en défaut : {e}") from None
    servis, publics = {}, {}
    for r in sorted(pm_):
        archive, sha_arch = P.heritage_k1(pm_[r])
        g0 = P.texte_servi(archive, episodes[r])
        ecarts = P.verifier_texte_servi(g0, archive, episodes[r])
        ctl = P.controle_episodes(episodes[r])
        if ecarts or not all(ctl.values()):
            raise N.Refus(f"monde {r} : texte servi G0 ou épisodes non conformes ({ecarts}, {ctl})")
        n0 = len(g0.encode("utf-8"))
        if n0 > conf["octets_entree_max"]:
            raise N.Refus(f"monde {r} : G0 de {n0} octets > {conf['octets_entree_max']}")
        g1 = N.texte_g1(g0, P.CONSIGNE_PROPOSEUR)
        n1 = N.exiger_octets(g1, f"monde {r}, G1")
        n2 = N.exiger_octets(N.pire_texte_g2(g0), f"monde {r}, G2 au pire")
        traits_k1 = sorted(N.traits_employes(archive[0]["loi"]))
        h = N.filtre(N.tirer_ensembles_h(racine, r), [traits_k1])
        servis[r] = {"g0": g0, "g1": g1, "h": h["retenus"], "traits_archive": [traits_k1]}
        publics[str(r)] = {"g0_sha256": N.sha256_texte(g0), "g1_sha256": N.sha256_texte(g1), "octets_g0": n0, "octets_g1": n1,
                           "octets_g2_pire": n2, "archive_sha256": sha_arch, "h_k": h["k"],
                           "episodes_sha256": hashlib.sha256(N.json_canonique(episodes[r])).hexdigest()}
    controles = {"mondes": publics, "c16_admises": all(v["admise"] for v in c16.values()),
                 "c17": {"instances": c17["instances"], "cartes": c17["cartes"], "ecart_max": c17["ecart_max"]},
                 "gabarit_g0_sha256": P.gabarit_sha256(), "gabarits_neufs_sha256": N.gabarits_sha256(P.CONSIGNE_PROPOSEUR)}
    P.exiger_manifeste_sans_loi(controles)
    return servis, controles


def preparer(a):
    arbre = Arbre(a.arbre)
    conf = arbre.configuration()
    _, mondes = lire_mondes(a.mondes, a.mondes_sha256, repetes_permis=a.repetes_permis)
    _, controles = preparer_crible(arbre, conf, mondes, a.texte_sha256)
    imprimer(controles)
    return 0


# --- relais ---------------------------------------------------------------------------------------------------------------------

def lancer_relais(arbre, conf, nom, journal, mode, jeton, scenarios=None, part=None, n=None):
    """Relais d'un proposeur, plafond = sa part du crible (80 ou 180 USD), nombre d'appels = ceux du crible (40 ou 60), ou ceux de
    la sonde des gabarits. Réel : le lanceur du pilote. À blanc : le relais factice du crible (même relais, amont scripté)."""
    part = N.PARTS_USD[nom] if part is None else part
    n = N.APPELS_ATTENDUS[nom] if n is None else n
    if mode == "reel":
        return arbre.PR.lancer_relais(conf, nom, journal, conf["proposeurs"][nom]["dialecte"], jeton, python=sys.executable,
                                      plafond=part, max_appels=n)
    p = conf["proposeurs"][nom]
    cmd = [sys.executable, "-I", "-B", os.path.join(ICI, "relais_factice_crible_iii_v1.py"),
           "--relais-pilote", conf["relais"]["chemin_absolu"], "--port", str(p["port"]), "--nom", nom, "--dialecte", p["dialecte"],
           "--modele", p["modele"], "--plafond-usd", repr(float(part)), "--max-appels", str(n),
           "--prix-entree", repr(p["prix_entree_usd_par_million"]), "--prix-sortie", repr(p["prix_sortie_usd_par_million"]),
           "--borne-sortie", str(p["borne_sortie_jetons"]), "--appelant", "factice:normal", "--journal", journal,
           "--url-amont", p["url_amont"], "--variable-cle", p["variable_cle"], "--reglages", json.dumps(p["reglages"]),
           "--delai-amont-s", repr(float(p["delai_s"]) - 60), "--reflexion-comprise", "oui" if p["reflexion_comprise"] else "non"]
    if scenarios:
        cmd += ["--scenarios-crible", scenarios]
    env = arbre.PR.env_du_relais(p, jeton, os.environ, True)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", env=env)
    ligne = proc.stdout.readline()
    try:
        info = json.loads(ligne)
    except ValueError:
        err = proc.stderr.read()[:300] if proc.poll() is not None else ""
        arbre.PR.arreter_relais(proc)
        raise N.Refus(f"relais factice {nom} : n'a pas démarré ({err})") from None
    return proc, info


def exiger_relais_prets(arbre, conf, mode, parts=None, appels=None):
    out = {}
    for nom in N.PROPOSEURS:
        try:
            e = arbre.PR.etat_relais(conf, nom)
        except OSError as x:
            raise N.Refus(f"relais {nom} injoignable : {x}") from None
        ecarts = arbre.PR.controler_etat_relais(conf, nom, e, mode, (parts or N.PARTS_USD)[nom], (appels or N.APPELS_ATTENDUS)[nom])
        if ecarts:
            raise N.Refus(f"relais {nom} : état non conforme ({ecarts})")
        out[nom] = {k: e[k] for k in ("relais", "appelant", "pid", "plafond_usd", "fichier_sha256", "max_appels", "cle_presente",
                                      "reflexion_comprise")}
    return out


def ports_libres(conf):
    occupes = []
    for nom in N.PROPOSEURS:
        s = socket.socket()
        s.settimeout(2)
        if s.connect_ex(("127.0.0.1", conf["proposeurs"][nom]["port"])) == 0:
            occupes.append(conf["proposeurs"][nom]["port"])
        s.close()
    if occupes:
        raise N.Refus(f"ports des relais occupés : {occupes}")


# --- un appel : la chaîne du pilote (commande + relais), bornée par le crible ---------------------------------------------------

def statut_amont(dossier):
    try:
        with open(os.path.join(dossier, "corps-relais.json"), encoding="utf-8") as f:
            return (json.load(f) or {}).get("statut_amont")
    except (OSError, ValueError, AttributeError):
        return None


def fabriquer_appeler(arbre, conf, sortie, jeton, apres_appel=None):
    PR = arbre.PR

    def appeler(bras, nom, texte, r, delai):
        dossier = os.path.join(sortie, f"monde-{r}", bras)
        coupe = {"v": False}

        def executer(cmd, **kw):
            kw["timeout"] = float(delai)   # borne du crible : min(3 000 s, reste de la borne du monde)
            try:
                return subprocess.run(cmd, **kw)
            except subprocess.TimeoutExpired:
                coupe["v"] = True
                raise
        try:
            res = PR.appeler(conf, nom, texte, dossier, jeton, python=sys.executable, executer=executer)
        except PR.ArretPilote as e:
            a = getattr(e, "appel", None)
            ligne = "coût au-dessus du pire cas" if a is not None and a.get("cause") == "cout_excessif" else \
                "réponse brute ou témoin d'isolement absent"
            raise N.Arret(ligne, str(e), code=3, appel=a) from None
        if apres_appel is not None:
            apres_appel(bras, nom, r, dossier, res)
        for f in ("reponse-brute.json", "temoin-isolement.json"):
            c = os.path.join(dossier, f)
            if not (os.path.isfile(c) and ME._compagnon_egal(c)):
                raise N.Arret("réponse brute ou témoin d'isolement absent", f"monde {r}, {bras} : {f} absent ou ≠ compagnon",
                              appel=res)
        pire = PR.pire_cas_d_un_appel(conf["proposeurs"][nom], len(texte.encode("utf-8")))
        if res["etat"] in ("complet", "tronque") and res["cout_usd"] > pire + N.EPS:
            # un coût lu (usage) au-dessus du pire cas ; un appel coupé ou en échec est compté au pire cas ou au plafond de
            # session par la chaîne du pilote (borne, non lecture) : il n'est pas jugé ici
            raise N.Arret("coût au-dessus du pire cas", f"{nom} : {res['cout_usd']} USD > {pire:.6f}", appel=res)
        if res.get("cause") == "modele_servi":
            raise N.Arret("configuration autre que v12", f"{nom} : modèle servi différent de la configuration", appel=res)
        res = dict(res, limite_debit=statut_amont(dossier) == 429, coupe=coupe["v"], delai_s=round(float(delai), 3))
        return res
    return appeler


def fabriquer_gardien(arbre):
    def gardien(r, bras, nom, texte):
        cartes, info = arbre.P.cartes_d_un_appel(r, nom, texte)
        return cartes, info
    return gardien


# --- mode réel -------------------------------------------------------------------------------------------------------------------

def lire_engagement(chemin_mondes, sha_fichier, texte_sha256):
    c = chemin_mondes + ".engagement.json"
    try:
        with open(c, encoding="utf-8") as f:
            e = json.load(f)
    except (OSError, ValueError):
        raise N.Refus("engagement des mondes absent ou illisible") from None
    if e.get("texte_sha256") != texte_sha256 or e.get("fichier_mondes_sha256") != sha_fichier:
        raise N.Refus("engagement des mondes : texte ou fichier des mondes différent")
    return e


def exiger_mode_reel(a, arbre, conf):
    manquants = [o for o in ("texte", "registre_go", "go_credits", "go_hors", "mondes_shas", "registre_lancements", "addendum")
                 if not getattr(a, o)]
    if manquants:
        raise N.Refus(f"mode réel : options exigées absentes : {manquants}")
    if a.scenarios_a_blanc or a.bornes_a_blanc or a.repetes_permis:
        raise N.Refus("mode réel : aucun scénario factice, aucune borne réduite, aucun monde répété")
    import numpy as np
    if np.__version__ != conf["numpy_exige"]:
        raise N.Refus(f"mode réel : numpy {np.__version__} ≠ {conf['numpy_exige']}")
    if sha_fichier(a.texte) != a.texte_sha256:
        raise N.Refus("texte qui fait foi : empreinte différente")
    with open(a.addendum, encoding="utf-8") as f:
        add = f.read()
    for nom in FICHIERS_DU_CRIBLE:
        if f"{sha_fichier(os.path.join(ICI, nom))}  {DOSSIER_DU_CODE}/{nom}" not in add:
            raise N.Refus(f"addendum d'empreintes : {nom} absent ou différent (empreinte du code présent)")
    if a.texte_sha256 not in add:
        raise N.Refus("addendum d'empreintes : il ne cite pas le texte qui fait foi")
    with open(a.registre_go, encoding="utf-8") as f:
        go = N.lire_go_du_crible(f.read(), a.go_credits, a.go_hors, datetime.datetime.now(datetime.timezone.utc).date())
    e = lire_engagement(a.mondes, a.mondes_sha256, a.texte_sha256)
    shas = a.mondes_shas.split(",")
    if e.get("public") is not False or e.get("mondes_sha256") != shas or len(set(shas)) != N.N_MONDES:
        raise N.Refus("engagement : mondes publics, ou empreintes différentes de celles inscrites (--mondes-shas)")
    arbre.P.exiger_hors_depot(a.registre_lancements, "registre des lancements")
    if os.path.exists(a.registre_lancements):
        with open(a.registre_lancements, encoding="utf-8") as f:
            if any(json.loads(l).get("texte_sha256") == a.texte_sha256 for l in f if l.strip()):
                raise N.Refus("mode réel : un lancement réel a déjà eu lieu pour ce texte (second lancement : nœud)")
    return go


def bornes_de(a):
    if not a.bornes_a_blanc:
        return dict(N.BORNES_GELEES)
    x = [float(v) for v in a.bornes_a_blanc.split(",")]
    if len(x) != 3:
        raise N.Refus("--bornes-a-blanc APPEL,MONDE,MARGE")
    return {"appel_s": x[0], "monde_s": x[1], "marge_s": x[2]}


def ecrire_scenarios(sortie, servis, fichier):
    """Fichiers de scénarios du relais factice (un par relais) : mondes reconnus par l'empreinte de leur contexte servi."""
    with open(fichier, encoding="utf-8") as f:
        sc = json.load(f)
    mondes = {}
    for r, s in servis.items():
        i = s["g0"].find("```json\n")
        j = s["g0"].find("\n```", i + 8)
        mondes[hashlib.sha256(s["g0"][i + 8:j].encode("utf-8")).hexdigest()] = r
    textes_h = {N.sha256_texte(N.texte_g2(s["g0"], s["h"])): r for r, s in servis.items()}
    out = {}
    for nom, defaut in ((N.PR4, "D"), (N.PR2, "B")):
        c = os.path.join(sortie, "prive", f"scenarios-{nom}.json")
        with open(c, "x", encoding="utf-8") as f:
            json.dump({"mondes": mondes, "textes_h": textes_h, "defaut_g2": defaut,
                       "scenarios": {k: v for k, v in sc.items() if N.PROPOSEUR_DU_BRAS[k.split("|")[1]] == nom}}, f)
        out[nom] = c
    return out


def jouer(a, apres_appel=None):
    debut, t_debut = maintenant(), time.time()
    arbre = Arbre(a.arbre)
    conf = arbre.configuration()
    releve_sha = exiger_releve_sonde(arbre, conf, a.releve_sonde)
    go = None
    if a.mode == "reel":
        go = exiger_mode_reel(a, arbre, conf)
    elif a.mode != "a_blanc":
        raise N.Refus("mode : a_blanc ou reel")
    bornes = N.exiger_bornes(bornes_de(a), a.mode)
    if int(a.echeance_utc_s) - time.time() < N.garde_de_depart(bornes):
        raise N.Refus(f"garde de départ : moins de {N.garde_de_depart(bornes):.0f} s avant l'échéance : aucun appel")
    if os.path.exists(a.sortie):
        raise N.Refus("dossier de sortie existant")
    ports_libres(conf)
    _, mondes = lire_mondes(a.mondes, a.mondes_sha256, repetes_permis=a.repetes_permis and a.mode == "a_blanc")
    servis, controles = preparer_crible(arbre, conf, mondes, a.texte_sha256)
    os.makedirs(a.sortie)
    prive = os.path.join(a.sortie, "prive")
    os.makedirs(prive, mode=0o700)
    for r, s in servis.items():  # textes servis gardés sur la machine pour l'audit R4, jamais rapatriés
        for g in ("g0", "g1"):
            with open(os.path.join(prive, f"texte-{g}-monde-{r}.txt"), "x", encoding="utf-8") as f:
                f.write(s[g])
    scen = ecrire_scenarios(a.sortie, servis, a.scenarios_a_blanc) if a.scenarios_a_blanc else {}
    jeton = arbre.PR.nouveau_jeton()
    procs, relais, releve = {}, None, None
    try:
        for nom in N.PROPOSEURS:
            procs[nom], _ = lancer_relais(arbre, conf, nom, os.path.join(a.sortie, f"journal-relais-{nom}.jsonl"), a.mode, jeton,
                                          scen.get(nom))
        relais = exiger_relais_prets(arbre, conf, a.mode)
        if a.mode == "reel":
            with open(a.registre_lancements, "a", encoding="utf-8") as f:
                f.write(json.dumps({"texte_sha256": a.texte_sha256, "debut_utc": debut, "sortie": os.path.abspath(a.sortie)}) + "\n")
        plafonds = {p: float(conf["proposeurs"][p]["plafond_session_usd"]) for p in N.PROPOSEURS}
        releve = N.jouer_crible({r: {"g0": s["g0"], "g1": s["g1"], "h": s["h"]} for r, s in servis.items()},
                                fabriquer_appeler(arbre, conf, a.sortie, jeton, apres_appel), fabriquer_gardien(arbre),
                                time.time, int(a.echeance_utc_s), plafonds, N.PARTS_USD, bornes, a.mode,
                                N.racine_graines(a.texte_sha256), {r: s["traits_archive"] for r, s in servis.items()})
    except N.Refus:
        for proc in procs.values():
            arbre.PR.arreter_relais(proc)
        raise
    finally:
        for proc in procs.values():
            arbre.PR.arreter_relais(proc)
    sha_c = ecrire_scelle(os.path.join(a.sortie, "CARTES.json"), {"cartes": releve["cartes"],
                                                                  "appels": [{k: x[k] for k in ("monde", "bras", "proposeur", "etat")}
                                                                             for x in releve["appels"]]})
    sha_e = ecrire_scelle(os.path.join(a.sortie, "ENSEMBLES.json"), releve["ensembles"])
    sha_r = ecrire_scelle(os.path.join(a.sortie, "releve-crible-iii-v1.json"), releve)
    import numpy as np
    manifeste = {"version": VERSION, "mode": a.mode, "debut_utc": debut, "fin_utc": maintenant(),
                 "duree_s": round(time.time() - t_debut, 3), "texte_sha256": a.texte_sha256,
                 "mondes_fichier_sha256": a.mondes_sha256, "controles": controles, "configuration_sha256": CONFIGURATION_SHA,
                 "configuration_fichier_sha256": CONFIGURATION_FICHIER_SHA, "releve_sonde_sha256": releve_sha,
                 "code_du_crible_sha256": {f: sha_fichier(os.path.join(ICI, f)) for f in FICHIERS_DU_CRIBLE},
                 "code_de_l_arbre_sha256": arbre.empreintes(), "relais": relais, "go": go, "bornes": bornes,
                 "echeance_utc": datetime.datetime.fromtimestamp(int(a.echeance_utc_s), datetime.timezone.utc).isoformat(),
                 "files": {str(k): v for k, v in N.files_des_mondes().items()}, "regle_des_graines": REGLE_DES_GRAINES,
                 "environnement": {"python": platform.python_version(), "numpy": np.__version__, "plate_forme": platform.platform()},
                 "scenarios_a_blanc": bool(a.scenarios_a_blanc), "arret": releve["arret"], "cartes_sha256": sha_c,
                 "ensembles_sha256": sha_e, "releve_sha256": sha_r, "juge": None, "tests_de_mort": None}
    arbre.P.exiger_manifeste_sans_loi(manifeste)
    sha_m = ecrire_scelle(os.path.join(a.sortie, "manifeste-crible-iii-v1.json"), manifeste)
    comptes = {e: sum(1 for x in releve["appels"] if x["etat"] == e) for e in ("complet", "tronque", "echec", "non appele")}
    imprimer({"lanceur": VERSION, "mode": a.mode, "comptes": comptes, "complets": releve["complets"], "arret": releve["arret"],
              "depense_usd": releve["depense_usd"], "releve_sha256": sha_r, "manifeste_sha256": sha_m})
    return 0 if releve["arret"] is None or releve["arret"]["code"] == 0 else 3


# --- sonde des gabarits neufs (κiii0, obligatoire) ----------------------------------------------------------------------------------

SONDE_PARTS = {N.PR2: 4.0, N.PR4: 3.0}         # deux appels de Pr-2, un de Pr-4, au plafond de session : 7 USD au pire
SONDE_APPELS = {N.PR2: 2, N.PR4: 1}
SONDE_MOTS = ("Sonde des gabarits", "crible (iii)")
DENOMINATEUR_III_7 = 2.504888                  # coût moyen d'un appel de Pr-4 lu au pilote (pièce, « Mise à jour d'après le pilote »)


def exiger_ligne_sonde(texte_registre, ident, aujourd_hui):
    go = N.lire_registre_go(texte_registre)
    g = go.get(ident)
    if g is None or g["type"] != "calcul" or g["par"] != "Lazar":
        raise N.Refus(f"{ident} : ligne « calcul » accordée par Lazar exigée (sonde des gabarits, κiii0)")
    if g["echeance"] is None or not (g["accorde"] <= aujourd_hui <= g["echeance"]):
        raise N.Refus(f"{ident} hors de sa période")
    if N.GO_ENVELOPPE not in g["ref"] or any(m not in g["perimetre"] for m in SONDE_MOTS):
        raise N.Refus(f"{ident} : périmètre ou référence de la sonde des gabarits attendus (GO-2026-11-15-06)")
    m = N.PLAFOND.search(g["plafond"])
    if not m or abs(float(m.group(1).replace(",", ".")) - 7.0) > N.EPS:
        raise N.Refus(f"{ident} : plafond 7 USD attendu")
    return {"ident": ident, "plafond_usd": 7.0}


def sonde_gabarits(a):
    """Trois appels sur le monde de développement 1 (graine publique) : Pr-2 sous G1, puis Pr-4 et Pr-2 sous G2 (mêmes ensembles,
    texte égal à l'octet) ; analyse des ensembles, forme des cartes (gardien, évaluabilité), jetons, dollars ; **aucune couverture
    lue** ; règles d'avance de la pièce appliquées et III-7 calculée par sa règle (1 + c₁ / 2,504888), rapportées."""
    debut = maintenant()
    arbre = Arbre(a.arbre)
    conf = arbre.configuration()
    releve_sha = exiger_releve_sonde(arbre, conf, a.releve_sonde)
    with open(a.mondes, "rb") as f:
        octets = f.read()
    if hashlib.sha256(octets).hexdigest() != a.mondes_sha256:
        raise N.Refus("fichier des mondes : empreinte différente")
    doc = json.loads(octets)
    mondes = [w for w in doc.get("mondes", []) if w.get("monde") == 1]
    if doc.get("public") is not True or len(mondes) != 1:
        raise N.Refus("sonde des gabarits : le monde de développement 1, à graine publique, seulement (generer --public)")
    go = None
    if a.mode == "reel":
        if a.scenarios_a_blanc or not (a.registre_go and a.go_sonde and a.registre_lancements):
            raise N.Refus("sonde réelle : --registre-go, --go-sonde et --registre-lancements exigés, aucun scénario")
        with open(a.registre_go, encoding="utf-8") as f:
            go = exiger_ligne_sonde(f.read(), a.go_sonde, datetime.datetime.now(datetime.timezone.utc).date())
        arbre.P.exiger_hors_depot(a.registre_lancements, "registre des lancements")
        if os.path.exists(a.registre_lancements):
            with open(a.registre_lancements, encoding="utf-8") as f:
                if any(json.loads(l).get("go") == a.go_sonde for l in f if l.strip()):
                    raise N.Refus("sonde des gabarits déjà lancée sous cette ligne (une seule exécution)")
    elif a.mode != "a_blanc":
        raise N.Refus("mode : a_blanc ou reel")
    if os.path.exists(a.sortie):
        raise N.Refus("dossier de sortie existant")
    ports_libres(conf)
    servis, controles = preparer_crible(arbre, conf, mondes[:1], a.texte_sha256)
    s = servis[1]
    os.makedirs(os.path.join(a.sortie, "prive"), mode=0o700)
    jeton = arbre.PR.nouveau_jeton()
    scen = {}
    if a.scenarios_a_blanc:
        scen = ecrire_scenarios(a.sortie, {1: s}, a.scenarios_a_blanc)
    procs, appels, regles = {}, [], []
    appeler = fabriquer_appeler(arbre, conf, a.sortie, jeton)
    outils = _outils(arbre.racine)
    o = outils.oracle_et_k1(mondes[0])[2]
    try:
        for nom in N.PROPOSEURS:
            procs[nom], _ = lancer_relais(arbre, conf, nom, os.path.join(a.sortie, f"journal-relais-{nom}.jsonl"), a.mode, jeton,
                                          scen.get(nom), SONDE_PARTS[nom], SONDE_APPELS[nom])
        exiger_relais_prets(arbre, conf, a.mode, SONDE_PARTS, SONDE_APPELS)
        if a.mode == "reel":
            with open(a.registre_lancements, "a", encoding="utf-8") as f:
                f.write(json.dumps({"go": a.go_sonde, "debut_utc": debut, "sortie": os.path.abspath(a.sortie)}) + "\n")

        def un(bras, texte):
            r = appeler(bras, N.PROPOSEUR_DU_BRAS[bras], texte, 1, N.BORNES_GELEES["appel_s"])
            cartes = []
            if bras != "P1" and r.get("etat") in ("complet", "tronque"):
                cartes, _ = arbre.P.cartes_d_un_appel(1, N.PROPOSEUR_DU_BRAS[bras], r.get("texte") or "")
            ev = [outils.evaluable(c["loi"], o) for c in cartes if c["etat"] == "admise"]
            x = {k: v for k, v in r.items() if k not in ("texte", "modele_servi")}
            x.update(bras=bras, gabarit=N.GABARIT_DU_BRAS[bras], octets=len(texte.encode("utf-8")),
                     cartes_admises=sum(1 for c in cartes if c["etat"] == "admise"),
                     cartes_refusees=sum(1 for c in cartes if c["etat"] == "refusee"), cartes_non_evaluables=ev.count(False))
            appels.append(x)
            return r
        r1 = un("P1", s["g1"])
        lu = N.analyser_passe1(r1.get("texte") or "") if r1.get("etat") == "complet" else {"valides": [], "invalides": 0,
                                                                                            "ignores": 0, "lecture": "passe 1 " + str(r1.get("etat"))}
        f = N.filtre(lu["valides"], s["traits_archive"])
        ens = {"valides": len(lu["valides"]), "invalides": lu["invalides"], "ignores": lu["ignores"], "lecture": lu["lecture"],
               "retenus": f["k"], "doublons": f["doublons"], "retires_archive": f["retires_archive"]}
        if not f["retenus"]:
            regles.append("aucune liste d'ensembles analysable sous G1 : G1 réécrit, nouvelle sonde, crible non lancé")
        else:
            t2 = N.texte_g2(s["g0"], f["retenus"])
            for bras in ("D", "B"):
                r = un(bras, t2)
                if r.get("etat") == "tronque":
                    regles.append(f"appel sous G2 tronqué ({bras}) : gabarit réécrit, crible non lancé")
        for x in appels:
            if x["cartes_non_evaluables"]:
                regles.append(f"carte non évaluable ({x['bras']}) : gabarit réécrit, crible non lancé")
        arret = None
    except N.Arret as e:
        arret = {"ligne": e.ligne, "motif": e.motif}
    finally:
        for proc in procs.values():
            arbre.PR.arreter_relais(proc)
    c1 = next((x.get("cout_usd") for x in appels if x["bras"] == "P1"), None)
    rel = {"version": VERSION + "|sonde-gabarits", "mode": a.mode, "debut_utc": debut, "fin_utc": maintenant(), "go": go,
           "releve_sonde_v74_sha256": releve_sha, "controles": controles, "appels": appels,
           "ensembles": ens if "ens" in locals() else None, "regles_d_avance": {"declenchee": bool(regles) or arret is not None,
                                                                                "motifs": regles},
           "arret": arret, "depense_usd": round(sum(float(x.get("cout_usd") or 0.0) for x in appels), 8),
           "III_7": None if c1 is None else {"c1_usd": c1, "valeur": 1 + c1 / DENOMINATEUR_III_7,
                                             "fourchette": [1 + c1 / DENOMINATEUR_III_7 - 0.05, 1 + c1 / DENOMINATEUR_III_7 + 0.05]},
           "couverture": "non lue (règle de la pièce)"}
    sha = ecrire_scelle(os.path.join(a.sortie, "releve-sonde-gabarits-crible-iii-v1.json"), rel)
    imprimer({"sonde_gabarits": rel["regles_d_avance"], "arret": arret, "depense_usd": rel["depense_usd"], "III_7": rel["III_7"],
              "releve_sha256": sha, "appels": [{k: x.get(k) for k in ("bras", "etat", "cout_usd", "jetons", "cartes_admises",
                                                                         "cartes_non_evaluables")} for x in appels]})
    return 0 if arret is None else 3


# --- rapatriement -----------------------------------------------------------------------------------------------------------------

def rapatrier(a):
    """Copie du dossier de sortie sans `prive/` ; refus si un fichier copié porte un devis de monde."""
    import shutil
    _, mondes = lire_mondes(a.mondes, a.mondes_sha256, repetes_permis=a.repetes_permis)
    if os.path.exists(a.destination):
        raise N.Refus("destination existante")
    marques = [json.dumps(w["spec"]["effets"], ensure_ascii=False, sort_keys=True).encode()[:200] for w in mondes]
    marques += [json.dumps(w["spec"]["effets"], sort_keys=True).encode()[:200] for w in mondes]
    copies = []
    for d, sous, fichiers in os.walk(a.source):
        rel = os.path.relpath(d, a.source)
        if rel == "prive" or rel.startswith("prive" + os.sep) or "/prive" in rel:
            continue
        for f in fichiers:
            copies.append(os.path.join(rel, f) if rel != "." else f)
    for c in copies:
        with open(os.path.join(a.source, c), "rb") as f:
            b = f.read()
        if any(m in b for m in marques) or os.path.basename(c).startswith("MONDES"):
            raise N.Refus(f"rapatriement : un devis de monde dans {c} : rien n'en sort")
    for c in copies:
        os.makedirs(os.path.join(a.destination, os.path.dirname(c)), exist_ok=True)
        shutil.copy2(os.path.join(a.source, c), os.path.join(a.destination, c))
    imprimer({"aucun_monde": True, "fichiers": len(copies)})
    return 0


def empreintes(a):
    arbre = Arbre(a.arbre)
    out = {f"{DOSSIER_DU_CODE}/{f}": sha_fichier(os.path.join(ICI, f)) for f in FICHIERS_DU_CRIBLE}
    out.update({f"orchestrator/{k}": v for k, v in arbre.empreintes().items()})
    for rel, sha in sorted(out.items()):
        print(f"{sha}  {rel}")
    return 0


def refuse_ou_none(f, *a):
    """Motif d'un refus nommé de `f(*a)`, sinon None (essais R5)."""
    try:
        f(*a)
    except N.Refus as e:
        return str(e)
    return None


def main(argv):
    p = argparse.ArgumentParser(prog="lanceur_crible_iii_v1.py")
    s = p.add_subparsers(dest="commande", required=True)
    x = s.add_parser("secret")
    x.add_argument("fichier")
    x = s.add_parser("generer")
    for o in ("--arbre", "--texte-sha256", "--sortie"):
        x.add_argument(o, required=True)
    x.add_argument("--secret")
    x.add_argument("--phrase-fichier")
    x.add_argument("--processus", type=int, default=4)
    x.add_argument("--public", action="store_true")
    x.add_argument("--un-seul", action="store_true")
    for nom in ("preparer", "jouer", "rapatrier"):
        x = s.add_parser(nom)
        x.add_argument("--mondes", required=True)
        x.add_argument("--mondes-sha256", required=True)
        x.add_argument("--repetes-permis", action="store_true")
        if nom != "rapatrier":
            x.add_argument("--arbre", required=True)
            x.add_argument("--texte-sha256", required=True)
        if nom == "jouer":
            x.add_argument("--mode", required=True)
            x.add_argument("--sortie", required=True)
            x.add_argument("--echeance-utc-s", required=True)
            x.add_argument("--releve-sonde", required=True)
            for o in ("--bornes-a-blanc", "--scenarios-a-blanc", "--texte", "--registre-go", "--go-credits", "--go-hors",
                      "--mondes-shas", "--registre-lancements", "--addendum"):
                x.add_argument(o)
        if nom == "rapatrier":
            x.add_argument("--source", required=True)
            x.add_argument("--destination", required=True)
    x = s.add_parser("empreintes")
    x.add_argument("--arbre", required=True)
    x = s.add_parser("sonde-gabarits")
    for o in ("--mode", "--arbre", "--mondes", "--mondes-sha256", "--texte-sha256", "--sortie", "--releve-sonde"):
        x.add_argument(o, required=True)
    for o in ("--scenarios-a-blanc", "--registre-go", "--go-sonde", "--registre-lancements"):
        x.add_argument(o)
    a = p.parse_args(argv)
    try:
        if a.commande == "secret":
            d = os.path.dirname(os.path.abspath(a.fichier))
            while d != os.path.dirname(d):
                if os.path.exists(os.path.join(d, ".git")):
                    raise N.Refus("secret : jamais dans un dépôt")
                d = os.path.dirname(d)
            fd = os.open(a.fichier, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "wb") as f:
                s32 = secrets.token_bytes(32)
                f.write(s32)
            imprimer({"secret_sha256": hashlib.sha256(s32).hexdigest()})
            return 0
        if a.commande == "generer":
            if not a.public and not (a.secret and a.phrase_fichier):
                raise N.Refus("generer : --secret et --phrase-fichier (ou --public, développement seulement)")
            return generer(a)
        return {"preparer": preparer, "jouer": jouer, "rapatrier": rapatrier, "empreintes": empreintes,
                "sonde-gabarits": sonde_gabarits}[a.commande](a)
    except N.Refus as e:
        print(f"CRIBLE REFUS : {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
