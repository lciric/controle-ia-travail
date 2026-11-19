"""Banc A de la ligne 1 des épreuves de la course v9 de l'organisme d'idéation (« l'effort de recherche compté dans le seuil
de promotion ») — étage sur processeur seul, version 1 du code.

**Préenregistrement qui fait foi, à la lettre** : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`,
sha256 `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9`, scellé au commit `7dcd6a44` (clé
PREREG-ORGANISME-V9-LIGNE-1). `verifier_preenregistrement` refuse de tourner si le fichier cité n'a pas cette empreinte.

Ce module porte (annexe A, `banc_ligne1_v1.py`) : mondes à effet et sans effet, lignées et variantes scriptées, texte des
cartes, tranches, étages amont (mémoire anti-redite par `memoire_v53.bardeaux` et `memoire_v53.jaccard` sur le texte brut —
une seule définition, `similarite`, partagée avec le bras d-E2 —, règle « affinage », quota d'aiguillage), course pleine,
registre des essais par bras, jugement à paramètres (réécriture appel pour appel de `a_blanc_v59.juger_carte`), les deux
vérités, les bras a, b, c, d, a′ (« a_prime »), T0, d-E1, d-E2, d-E3, la statistique D1 ; gardes A1 à A6 et A10.

Aucun réseau, aucun modèle, aucune clé, aucune dépense. Le dépôt de l'organisme est importé en lecture seule (lancer avec
`python3 -B`, `PYTHONDONTWRITEBYTECODE=1`).
"""

import copy
import datetime
import hashlib
import importlib
import importlib.abc
import json
import math
import os
import random
import socket
import subprocess
import sys

import journal_ligne1_v1 as JL

VERSION = "banc-ligne1-v1"
PREREG_CHEMIN = "prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md"
PREREG_SHA256 = "523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9"
PREREG_COMMIT = "7dcd6a44c777f3aea55b5c68ef8547f9f83438fa"
PREREG_CLE = "PREREG-ORGANISME-V9-LIGNE-1"
DOSSIER_CODE = os.path.dirname(os.path.abspath(__file__))
CHEMIN_CONFIGURATION = os.path.join(DOSSIER_CODE, "configuration_ligne1_v1.json")
FICHIERS_CODE = ("configuration_ligne1_v1.json", "banc_ligne1_v1.py", "journal_ligne1_v1.py", "rejouer_journal_ligne1_v1.py",
                 "etalonnage_ligne1_v1.py", "lancer_ligne1_v1.py", "analyse_ligne1_v1.py")
BRAS = ("a", "b", "c", "d", "a_prime", "T0", "d_E1", "d_E2", "d_E3")
BRAS_INTERDITS_A_L_ETALONNAGE = ("a", "b", "c", "d", "a_prime", "d_E1", "d_E2", "d_E3")


# --- exceptions nommées (aucun repli silencieux, règle R5) -----------------------------------------------------------------
class ArretBanc(RuntimeError):
    """Base des arrêts du banc."""


class PreenregistrementRefuse(ArretBanc):
    """Le préenregistrement cité n'est pas lisible ou n'a pas l'empreinte scellée : le banc refuse de tourner."""


class ConfigurationRefusee(ArretBanc):
    pass


class GardeA1EmpreinteOrganisme(ArretBanc):
    pass


class GardeA2Connexion(ArretBanc):
    pass


class GardeA3Appariement(ArretBanc):
    pass


class GardeA4Registre(ArretBanc):
    pass


class GardeA5CompteM(ArretBanc):
    pass


class GardeA6Jugement(ArretBanc):
    pass


class GardeA10NonFini(ArretBanc):
    pass


class GardeA17BrasEtalonnage(ArretBanc):
    pass


# --- préenregistrement, configuration ---------------------------------------------------------------------------------------
def sha256_octets(octets):
    return hashlib.sha256(octets).hexdigest()


def sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def racine_depot():
    """Racine du dépôt de travail (le code vit sous docs/notes/…/code/)."""
    sortie = subprocess.run(["git", "-C", DOSSIER_CODE, "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if sortie.returncode != 0:
        raise PreenregistrementRefuse("racine du dépôt introuvable (git rev-parse)")
    return sortie.stdout.strip()


COPIE_DU_COMPTE = ("docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/"
                   "preenregistrement-ligne-1-effort-recherche-v5.md")


def verifier_preenregistrement(depot=None, chemin=PREREG_CHEMIN, attendue=PREREG_SHA256):
    """Lit le préenregistrement scellé : dans l'arbre de travail au chemin cité ; sinon au commit de scellement
    (`git show 7dcd6a44:<chemin>`) ; sinon la copie à l'octet du compte (R-3879). Refuse de tourner si les octets lus n'ont
    pas l'empreinte du scellement. Rend la provenance."""
    depot = depot or racine_depot()
    local = os.path.join(depot, chemin)
    octets = None
    if os.path.isfile(local):
        with open(local, "rb") as f:
            octets, source = f.read(), f"arbre de travail : {chemin}"
    else:
        sortie = subprocess.run(["git", "-C", depot, "show", f"{PREREG_COMMIT}:{chemin}"], capture_output=True)
        if sortie.returncode == 0:
            octets, source = sortie.stdout, f"commit {PREREG_COMMIT} : {chemin}"
        elif os.path.isfile(os.path.join(depot, COPIE_DU_COMPTE)):
            with open(os.path.join(depot, COPIE_DU_COMPTE), "rb") as f:
                octets, source = f.read(), f"copie à l'octet du compte : {COPIE_DU_COMPTE}"
    if octets is None:
        raise PreenregistrementRefuse(f"préenregistrement {chemin} introuvable (arbre, commit {PREREG_COMMIT[:8]}, copie) : refus")
    sha = sha256_octets(octets)
    if sha != attendue:
        raise PreenregistrementRefuse(f"préenregistrement {chemin} : empreinte {sha} ≠ {attendue} (scellée) : refus")
    return {"chemin": chemin, "sha256": sha, "source": source, "cle": PREREG_CLE, "commit_scellement": PREREG_COMMIT}


def charger_configuration(chemin=CHEMIN_CONFIGURATION):
    with open(chemin, "rb") as f:
        octets = f.read()
    config = json.loads(octets)
    p = config.get("preenregistrement", {})
    if p.get("chemin") != PREREG_CHEMIN or p.get("sha256") != PREREG_SHA256:
        raise ConfigurationRefusee("configuration : le préenregistrement cité n'est pas celui qui fait foi")
    return config, sha256_octets(octets)


def horodatage():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


# --- garde A2 : aucune connexion, aucun adaptateur de modèle ----------------------------------------------------------------
MODULES_INTERDITS = ("anthropic", "openai", "httpx", "requests", "urllib3", "aiohttp", "google", "claude_agent_sdk",
                     "claude_code_sdk", "mistralai", "cohere", "ollama")
PREFIXES_ADAPTATEURS = ("pole.adaptateur_", "pole.adaptateurs_v")


def _refus_connexion(*a, **k):
    raise GardeA2Connexion("garde A2 : le banc a tenté d'ouvrir une connexion : refus")


class _BloqueurAdaptateurs(importlib.abc.MetaPathFinder):
    def find_spec(self, nom, chemin=None, cible=None):
        if nom.split(".")[0] in MODULES_INTERDITS or nom.startswith(PREFIXES_ADAPTATEURS):
            raise GardeA2Connexion(f"garde A2 : chargement d'un adaptateur ou d'un client de modèle refusé ({nom})")
        return None


_GARDE_A2 = {"installee": False}


def installer_garde_a2():
    """Toute ouverture de connexion lève `GardeA2Connexion` ; tout import d'un client de modèle ou d'un adaptateur de
    l'organisme aussi. Idempotent."""
    if _GARDE_A2["installee"]:
        return
    socket.socket.connect = _refus_connexion
    socket.socket.connect_ex = _refus_connexion
    socket.create_connection = _refus_connexion
    socket.getaddrinfo = _refus_connexion
    sys.meta_path.insert(0, _BloqueurAdaptateurs())
    _GARDE_A2["installee"] = True


def verifier_aucun_adaptateur():
    charges = [m for m in sys.modules if m.split(".")[0] in MODULES_INTERDITS or m.startswith(PREFIXES_ADAPTATEURS)]
    if charges:
        raise GardeA2Connexion(f"garde A2 : modules d'adaptateur ou de client chargés : {charges}")


# --- organisme (A1) -------------------------------------------------------------------------------------------------------
SP = NF = NUL8 = CYC = MEM = BF = PR = OUT = AB = None
ORGANISME = {}


def verifier_empreintes_organisme(dossier_pole, attendues):
    """Garde A1 : chaque fichier nommé par le préenregistrement doit avoir l'empreinte attendue ; refus avant tout tirage."""
    ecarts = {}
    for nom, sha in sorted(attendues.items()):
        chemin = os.path.join(dossier_pole, nom)
        reel = sha256_fichier(chemin) if os.path.isfile(chemin) else None
        if reel != sha:
            ecarts[nom] = reel
    if ecarts:
        raise GardeA1EmpreinteOrganisme(f"garde A1 : empreinte(s) de l'organisme différente(s) de la liste scellée : {ecarts}")
    return dict(attendues)


def charger_organisme(racine_orchestrateur, config):
    """A2 puis A1, puis import en lecture seule ; vérifie que les modules chargés sont bien les fichiers vérifiés."""
    global SP, NF, NUL8, CYC, MEM, BF, PR, OUT, AB
    installer_garde_a2()
    racine_orchestrateur = os.path.realpath(racine_orchestrateur)
    dossier_pole = os.path.join(racine_orchestrateur, config["organisme"]["dossier"])
    attendues = config["organisme"]["fichiers"]
    if ORGANISME.get("racine") == racine_orchestrateur:
        verifier_empreintes_organisme(dossier_pole, attendues)
        return ORGANISME
    if ORGANISME:
        raise GardeA1EmpreinteOrganisme("organisme déjà chargé depuis un autre dossier dans ce processus : refus")
    verifier_empreintes_organisme(dossier_pole, attendues)
    sys.dont_write_bytecode = True
    if racine_orchestrateur not in sys.path:
        sys.path.insert(0, racine_orchestrateur)
    modules = {}
    for nom in ("selection_pari", "nul_filles_v2", "nul_v8", "cycle", "memoire_v53", "boucle_fermee_v59",
                "proposeurs_references_v59", "outils", "a_blanc_v59"):
        modules[nom] = importlib.import_module(f"pole.{nom}")
    for nom, module in modules.items():
        fichier = os.path.realpath(module.__file__)
        if fichier != os.path.realpath(os.path.join(dossier_pole, nom + ".py")) or sha256_fichier(fichier) != attendues[nom + ".py"]:
            raise GardeA1EmpreinteOrganisme(f"garde A1 : le module chargé pole.{nom} n'est pas le fichier vérifié ({fichier})")
    verifier_aucun_adaptateur()
    SP, NF, NUL8, CYC = modules["selection_pari"], modules["nul_filles_v2"], modules["nul_v8"], modules["cycle"]
    MEM, BF, PR, OUT, AB = (modules["memoire_v53"], modules["boucle_fermee_v59"], modules["proposeurs_references_v59"],
                            modules["outils"], modules["a_blanc_v59"])
    if (AB.K, AB.DIM) != (config["monde"]["issues"], config["monde"]["traits"]):
        raise ConfigurationRefusee("configuration : nombre d'issues ou de traits différent de celui du mode à blanc")
    charges = sorted(m for m in sys.modules if m == "pole" or m.startswith("pole."))
    ORGANISME.update(racine=racine_orchestrateur, dossier_pole=dossier_pole, fichiers=dict(attendues),
                     modules_charges={m: sha256_fichier(sys.modules[m].__file__) for m in charges
                                      if getattr(sys.modules[m], "__file__", None)})
    return ORGANISME


def commit_organisme(racine_orchestrateur):
    sortie = subprocess.run(["git", "-C", racine_orchestrateur, "rev-parse", "HEAD"], capture_output=True, text=True)
    return sortie.stdout.strip() if sortie.returncode == 0 else None


# --- graines (règle R9) --------------------------------------------------------------------------------------------------------
class Graines:
    """`boucle_fermee_v59.graine_de_tache` (SeedSequence(racine, spawn_key=(clé de la tâche,))) ; consigne l'horodatage de la
    première dérivation par racine (manifeste, garde A14)."""

    def __init__(self):
        self.premieres = {}

    def __call__(self, racine, tache):
        if racine not in self.premieres:
            self.premieres[racine] = horodatage()
        return BF.graine_de_tache(racine, tache)


GRAINES = Graines()


def rng_tache(racine, tache):
    return random.Random(GRAINES(racine, tache))


# --- garde A10 ------------------------------------------------------------------------------------------------------------
def exiger_fini(valeurs, quoi):
    for v in valeurs:
        if not (isinstance(v, (int, float)) and math.isfinite(v)):
            raise GardeA10NonFini(f"garde A10 : valeur non finie dans {quoi} : {v!r}")
    return valeurs


# --- paramètres ---------------------------------------------------------------------------------------------------------------
def parametres(config, forces, s, c):
    """Paramètres d'une course : la configuration, les quatre forces (dans l'ordre des cibles 0,90 ; 0,50 ; 0,30 ; 0,15) et
    le couple (s, c) des lois tranchantes, fixés par l'étalonnage (ou par les valeurs d'essai, racine des essais)."""
    roles = config["monde"]["roles"]
    vraies = [r for r in roles if r["a_effet"]]
    if len(forces) != len(vraies) or len(roles) != config["monde"]["lignees"]:
        raise ConfigurationRefusee("forces : une par rôle vrai ; rôles : un par lignée")
    exiger_fini(list(forces) + [s, c], "paramètres")
    etendus, i = [], 0
    for r in roles:
        r = dict(r)
        if r["a_effet"]:
            r["force"] = float(forces[i])
            i += 1
        etendus.append(r)
    return {"config": config, "roles": etendus, "forces": [float(f) for f in forces], "s": float(s), "c": float(c),
            "K": config["monde"]["issues"], "DIM": config["monde"]["traits"], "L": config["monde"]["lignees"],
            "G": config["proposeurs"]["generations"]}


# --- jugement (réécriture appel pour appel de a_blanc_v59.juger_carte) ; garde A6 --------------------------------------------
def juger(loi, loi_monde, archive, racine, tache, *, tirages, alpha, entrainement, nombre_instants, K=3, DIM=2):
    """`a_blanc_v59.juger_carte` avec le nombre de tirages, le niveau, la taille d'entraînement et le nombre d'instants en
    paramètres. À 200 tirages, α = 0,05, 100 instances d'entraînement et 8 instants, sortie identique au bit près (essai 1)."""
    rng = random.Random(GRAINES(racine, f"{tache}|plan"))
    ent = SP.tirer_instances(rng, entrainement, DIM)
    q_ent = AB._frequences([SP.tirer_categorie(rng, SP.proba(loi_monde, x, [], 0)) for x in ent], K)
    standard = list(SP.BIBLIOTHEQUE_STANDARD) + [{"nom": "marginale_entrainement", "type": "fixe", "probas": q_ent}]
    instances = SP.tirer_instances(rng, tirages, DIM)
    biblio = standard + NUL8.membres_archive_v8(dict(archive), None, K, DIM)
    gele = SP.geler_engagement(NF.construire_engagement_v2("fiche", loi, instances, K, alpha, biblio, 0, None,
                                                           CYC.instants_reguliers(tirages, nombre_instants)))
    graines = {"noyau": GRAINES(racine, f"{tache}|noyau"), "frais": GRAINES(racine, f"{tache}|frais|{gele.empreinte}")}
    tir = SP.tirer_frais(gele, loi_monde, graines["frais"], graine_noyau=graines["noyau"])
    ev = NF.evaluer_v2(gele, tir, graine_noyau=graines["noyau"])
    exiger_fini(ev["trajectoire_log_w"], f"trajectoire ({tache})")
    exiger_fini([ev["log_richesse_finale"], ev["log_richesse_max"]], f"richesse ({tache})")
    return ev, {"empreinte_engagement": gele.empreinte, "graines": graines, "membres_du_nul": len(biblio),
                "membres_d_archive": len(biblio) - len(standard)}


def juger_banc(loi, loi_monde, racine, tache, juge, K=3, DIM=2):
    return juger(loi, loi_monde, {}, racine, tache, tirages=juge["tirages"], alpha=juge["alpha"],
                 entrainement=juge["entrainement"], nombre_instants=juge["instants"], K=K, DIM=DIM)


LOIS_A6 = None


def lois_essai_a6(K=3):
    """Dix lois de types variés (softmax, transformee, si_sinon, fixe, mélange) pour la garde A6 et l'essai 1."""
    base = {"type": "softmax", "poids": [[0.4, -0.2], [-0.3, 0.5], [0.1, 0.2]], "biais": [0.1, -0.1, 0.0]}
    forte = {"type": "softmax", "poids": [[1.2, -0.7], [-0.9, 1.1], [0.3, 0.4]], "biais": [0.0, 0.2, -0.2]}
    return [base, forte,
            {"type": "transformee", "base": base, "puissance": 1.3, "inclinaison": [0.0, 0.2, -0.1]},
            {"type": "transformee", "base": forte, "puissance": 0.55, "inclinaison": [0.0, -0.3, 0.25]},
            {"type": "si_sinon", "condition": {"indice": 0, "seuil": 1.3}, "si": {"type": "fixe", "probas": [0.75, 0.125, 0.125]},
             "sinon": {"type": "fixe", "probas": [0.3, 0.3, 0.4]}},
            {"type": "si_sinon", "condition": {"indice": 1, "seuil": 1.6}, "si": {"type": "fixe", "probas": [0.05, 0.9, 0.05]},
             "sinon": {"type": "fixe", "probas": [0.35, 0.4, 0.25]}},
            {"type": "fixe", "probas": [0.2, 0.5, 0.3]},
            {"type": "melange", "composantes": [forte, {"type": "fixe", "probas": [1 / K] * K}], "poids": [0.5, 0.5]},
            {"type": "softmax", "poids": [[-1.5, 0.2], [0.8, -0.4], [0.0, 0.9]], "biais": [0.3, 0.0, -0.3]},
            {"type": "transformee", "base": {"type": "softmax", "poids": [[-1.5, 0.2], [0.8, -0.4], [0.0, 0.9]],
                                             "biais": [0.3, 0.0, -0.3]}, "puissance": 1.6, "inclinaison": [0.0, 0.0, 0.3]}]


def verifier_jugement_identique(racine, *, nombre_instants=8, tirages=200, alpha=0.05, entrainement=100, lois=None):
    """Garde A6 : le jugement du banc rend, sur dix lois, la sortie de `a_blanc_v59.juger_carte` au bit près (issue et
    détail) ; refus avant l'étalonnage sinon. Le monde est la loi `forte`, le jugement à archive vide."""
    lois = lois or lois_essai_a6()
    monde = lois[1]
    for i, loi in enumerate(lois):
        tache = f"garde-A6|loi={i}"
        ref, dref = AB.juger_carte(loi, {"loi": monde}, {}, racine, tache)
        ev, d = juger(loi, monde, {}, racine, tache, tirages=tirages, alpha=alpha, entrainement=entrainement,
                      nombre_instants=nombre_instants)
        if JL.empreinte(ref) != JL.empreinte(ev) or JL.empreinte(dref) != JL.empreinte(d):
            raise GardeA6Jugement(f"garde A6 : le jugement du banc diffère de a_blanc_v59.juger_carte (loi {i}) : refus")
    return len(lois)


# --- monde planté ---------------------------------------------------------------------------------------------------------------
def monde_sans_effet(rng, alphas):
    g = [rng.gammavariate(a, 1.0) for a in alphas]
    s = sum(g)
    return {"type": "fixe", "probas": [x / s for x in g]}


def tirer_tranche(loi_monde, rng, episodes, DIM):
    """Comme `a_blanc_v59.creer_tranche` : les instances d'abord, puis l'issue de chacune."""
    instances = SP.tirer_instances(rng, episodes, DIM)
    issues = [SP.tirer_categorie(rng, SP.proba(loi_monde, x, [], 0)) for x in instances]
    return {"instances": instances, "issues": issues}


def marginale_empirique(issues, K):
    return [issues.count(k) / len(issues) for k in range(K)]


def objets_communs(course, racine, P):
    """Objets d'une course communs aux deux classes (tâches sans la classe : « course | lignée | objet ») : rôle, monde,
    hypothèse, tranche exploratoire, tranche fraîche (D1), instances d'oracle."""
    cfg, K, DIM, L = P["config"]["monde"], P["K"], P["DIM"], P["L"]
    cles = [rng_tache(racine, f"course={course}|lignee={l}|role").random() for l in range(L)]
    ordre = sorted(range(L), key=lambda l: (cles[l], l))
    indice_role = {l: k for k, l in enumerate(ordre)}
    lignees = []
    for l in range(L):
        role = P["roles"][indice_role[l]]
        r_monde = rng_tache(racine, f"course={course}|lignee={l}|monde")
        if role["a_effet"]:
            loi_monde = SP.loi_softmax_aleatoire(r_monde, K, DIM, role["force"])
            r_h = rng_tache(racine, f"course={course}|lignee={l}|hypothese")
            sd = cfg["bruit_hypothese_vraie"] * role["force"]
            hypothese = {"type": "softmax", "poids": [[round(w + r_h.gauss(0.0, sd), 6) for w in ligne] for ligne in loi_monde["poids"]],
                         "biais": list(loi_monde["biais"])}
        else:
            loi_monde = monde_sans_effet(r_monde, cfg["dirichlet_sans_effet"])
            if role["role"] == "fausse_diffuse":
                hypothese = SP.loi_softmax_aleatoire(rng_tache(racine, f"course={course}|lignee={l}|hypothese"), K, DIM,
                                                     cfg["force_hypothese_diffuse"])
            else:
                hypothese = None
        tranche = tirer_tranche(loi_monde, rng_tache(racine, f"course={course}|lignee={l}|tranche"), cfg["episodes_tranche"], DIM)
        fraiche = tirer_tranche(loi_monde, rng_tache(racine, f"course={course}|lignee={l}|tranche_fraiche"),
                                cfg["episodes_tranche"], DIM)
        oracle = None
        if role["a_effet"]:
            inst = SP.tirer_instances(rng_tache(racine, f"course={course}|lignee={l}|oracle"), cfg["instances_oracle"], DIM)
            probs = [SP.proba(loi_monde, x, [], 0) for x in inst]
            marg = [sum(p[k] for p in probs) / len(probs) for k in range(K)]
            oracle = {"instances": inst, "P": probs, "log_marg": [math.log(m) for m in marg]}
        lignees.append({"l": l, "role": role["role"], "a_effet": role["a_effet"], "cible": role["cible"],
                        "force": role.get("force"), "loi_monde": loi_monde, "hypothese": hypothese, "tranche": tranche,
                        "fraiche": fraiche, "oracle": oracle,
                        "marginale_tranche": marginale_empirique(tranche["issues"], K)})
    return {"course": course, "racine": racine, "lignees": lignees}


def empreinte_commune(lignee):
    """Empreinte de ce qu'une lignée partage entre classes (garde A3)."""
    return JL.empreinte({k: lignee[k] for k in ("l", "role", "loi_monde", "hypothese", "tranche", "fraiche")})


# --- statistique du test de mort (D1) et oracle --------------------------------------------------------------------------------
def statistique_test_de_mort(loi, tranche, K):
    """`proposeurs_references_v59.TEST_DE_MORT`, comme le script de l'expérimentateur du mode à blanc : gain moyen par
    épisode du log-score de la loi sur la marginale empirique de la tranche (comptes lissés à 0,5), en nat."""
    comptes = [0.5] * K
    for y in tranche["issues"]:
        comptes[y] += 1
    s = sum(comptes)
    log_marg = [math.log(c / s) for c in comptes]
    total = 0.0
    for x, y in zip(tranche["instances"], tranche["issues"]):
        p = SP.proba(loi, x, [], 0)
        total += math.log(max(p[y], 1e-12)) - log_marg[y]
    return total / len(tranche["issues"])


def gain_oracle(loi, oracle):
    """Gain attendu de la loi sur la marginale du monde (nat par épisode), espérance exacte sur les issues, moyenne sur les
    instances d'oracle fixées du monde, à la façon de `a_blanc_v59.oracle` (non arrondi)."""
    total = 0.0
    for x, p, in zip(oracle["instances"], oracle["P"]):
        q = SP.proba(loi, x, [], 0)
        total += sum(pk * (math.log(max(qk, 1e-12)) - lm) for pk, qk, lm in zip(p, q, oracle["log_marg"]))
    return total / len(oracle["instances"])


def etiquette_oracle(gain, seuil_vraie):
    if gain >= seuil_vraie:
        return "vraie"
    if gain <= 0.0:
        return "fausse"
    return "indeterminee"


# --- variantes scriptées et texte des cartes ----------------------------------------------------------------------------------
def variantes(lignee, rng, n, P):
    """`n` variantes d'un appel. Lignées vraies et fausses diffuses : `transformee` de l'hypothèse (puissance uniforme dans
    [0,4 ; 1,6], inclinaison gaussienne d'écart-type 0,3 sur les issues 2 et 3). Lignées tranchantes : `si_sinon`, trait i
    tiré dans {0, 1}, seuil s + écart uniforme dans [−0,15 ; 0,15], confiance c sur une issue tirée au hasard (le reste
    partagé à parts égales), hors de la région la marginale empirique de la tranche."""
    cfg, K = P["config"]["monde"], P["K"]
    sortie = []
    for _ in range(n):
        if lignee["role"] == "fausse_tranchante":
            i = rng.randrange(P["DIM"])
            seuil = round(P["s"] + rng.uniform(-cfg["ecart_seuil_tranchant"], cfg["ecart_seuil_tranchant"]), 6)
            issue = rng.randrange(K)
            si = [P["c"] if k == issue else (1.0 - P["c"]) / (K - 1) for k in range(K)]
            sortie.append({"type": "si_sinon", "condition": {"indice": i, "seuil": seuil}, "si": {"type": "fixe", "probas": si},
                           "sinon": {"type": "fixe", "probas": list(lignee["marginale_tranche"])}})
        else:
            a, b = cfg["puissance_variante"]
            g = round(rng.uniform(a, b), 6)
            incl = [0.0] + [round(rng.gauss(0.0, cfg["inclinaison_ecart_type"]), 6) for _ in range(K - 1)]
            sortie.append({"type": "transformee", "base": lignee["hypothese"], "puissance": g, "inclinaison": incl})
    return sortie


def ecrire_valeur(v):
    """Signe, deux décimales ; toute valeur qui s'arrondit à zéro s'écrit « +0.00 » (jamais « -0.00 »)."""
    r = round(float(v), 2)
    if r == 0.0:
        return "+0.00"
    return "%+.2f" % r


def issue_et_confiance(loi_si):
    p = loi_si["probas"]
    k = max(range(len(p)), key=lambda i: (p[i], -i))
    return k, p[k]


def texte_carte(loi):
    """Texte d'une carte, mot par mot (préenregistrement, « Texte d'une carte »)."""
    if loi["type"] == "transformee":
        h, g = loi["base"], loi["puissance"]
        mots = [f"w{k}{j}{ecrire_valeur(w * g)}" for k, ligne in enumerate(h["poids"]) for j, w in enumerate(ligne)]
        mots += [f"b{k}{ecrire_valeur(b * g)}" for k, b in enumerate(h["biais"])]
        mots += [f"i{k}{ecrire_valeur(loi['inclinaison'][k])}" for k in range(1, len(loi["inclinaison"]))]
        return " ".join(mots)
    if loi["type"] == "si_sinon":
        issue, conf = issue_et_confiance(loi["si"])
        mots = [f"t{ecrire_valeur(loi['condition']['indice'])}", f"s{ecrire_valeur(loi['condition']['seuil'])}",
                f"y{ecrire_valeur(issue)}", f"c{ecrire_valeur(conf)}"]
        mots += [f"m{k}{ecrire_valeur(p)}" for k, p in enumerate(loi["sinon"]["probas"])]
        return " ".join(mots)
    raise ValueError(f"type de carte inattendu dans le banc : {loi['type']!r}")


# --- étages amont ------------------------------------------------------------------------------------------------------------
def similarite(texte_a, texte_b, taille_bardeau):
    """La seule définition de la similarité du banc (mémoire anti-redite et bras d-E2) : `memoire_v53.jaccard` sur
    `memoire_v53.bardeaux` des textes bruts."""
    return MEM.jaccard(MEM.bardeaux(texte_a, taille_bardeau), MEM.bardeaux(texte_b, taille_bardeau))


def decider_memoire(texte, comparees, seuil, taille_bardeau, epsilon):
    """Rend (similarité la plus haute, refusée) ; refusée si une similarité vaut le seuil ou plus (s + 1e-12 >= 0,6)."""
    sims = [similarite(texte, t, taille_bardeau) for t in comparees]
    plus_haute = max(sims) if sims else 0.0
    return plus_haute, any(s + epsilon >= seuil for s in sims)


def derive(loi, jugee, rayon):
    """« Dérive » : `transformee`, même hypothèse et puissance à moins du rayon ; `si_sinon`, même trait, même issue et
    seuil à moins du rayon."""
    if loi["type"] != jugee["type"]:
        return False
    if loi["type"] == "transformee":
        return loi["base"] == jugee["base"] and abs(loi["puissance"] - jugee["puissance"]) < rayon
    if loi["type"] == "si_sinon":
        return (loi["condition"]["indice"] == jugee["condition"]["indice"]
                and issue_et_confiance(loi["si"])[0] == issue_et_confiance(jugee["si"])[0]
                and abs(loi["condition"]["seuil"] - jugee["condition"]["seuil"]) < rayon)
    return False


def decider_affinage(loi, lois_jugees, rayon, deja_une):
    """Rend (dérive, refusée) : au plus une variante par appel dérivée d'une carte déjà jugée et éliminée de la lignée."""
    d = any(derive(loi, j, rayon) for j in lois_jugees)
    return d, bool(d and deja_une)


def decider_quota(restantes, quota):
    return list(restantes[:quota]), list(restantes[quota:])


def identifiant_reception(course, classe, l, g, rang):
    return f"c{course:04d}-{classe}-l{l}-g{g}-r{rang:02d}"


_MECANISMES = {}


def mecanismes_code():
    """Empreintes des fichiers de code qui portent chaque mécanisme (journal) ; calculées une fois par processus."""
    if _MECANISMES:
        return _MECANISMES
    banc = sha256_fichier(os.path.join(DOSSIER_CODE, "banc_ligne1_v1.py"))
    f = ORGANISME.get("fichiers", {})
    _MECANISMES.update({
        "reception": {"banc_ligne1_v1.py": banc, "outils.py": f.get("outils.py")},
        "memoire": {"banc_ligne1_v1.py": banc, "memoire_v53.py": f.get("memoire_v53.py")},
        "affinage": {"banc_ligne1_v1.py": banc},
        "quota": {"banc_ligne1_v1.py": banc},
        "jugement": {"banc_ligne1_v1.py": banc, "selection_pari.py": f.get("selection_pari.py"),
                     "nul_filles_v2.py": f.get("nul_filles_v2.py"), "nul_v8.py": f.get("nul_v8.py"), "cycle.py": f.get("cycle.py"),
                     "boucle_fermee_v59.py": f.get("boucle_fermee_v59.py")},
        "registre": {"banc_ligne1_v1.py": banc},
        "promotion_e_bh": {"banc_ligne1_v1.py": banc, "cycle.py": f.get("cycle.py")},
        "promotion_bonferroni": {"banc_ligne1_v1.py": banc},
        "promotion_seule": {"banc_ligne1_v1.py": banc},
        "choix_c": {"banc_ligne1_v1.py": banc},
        "promotion_c": {"banc_ligne1_v1.py": banc},
        "arret": {"banc_ligne1_v1.py": banc},
    })
    return _MECANISMES


# --- course pleine d'une classe ------------------------------------------------------------------------------------------------
def jouer_course_pleine(communs, classe, P, journal, memoire_seuil=None):
    """La course pleine d'une classe (aucune lignée arrêtée) : propositions, étages amont, jugements, vérités, D1.
    `memoire_seuil` : réglage de la mémoire, lu de la configuration (paramètre exposé pour l'artefact de la garde A15)."""
    cfg = P["config"]
    K, DIM, L, G = P["K"], P["DIM"], P["L"], P["G"]
    course, racine = communs["course"], communs["racine"]
    n_var = cfg["proposeurs"]["engagements_par_appel"][classe]
    mem = cfg["memoire"]
    seuil_mem = mem["seuil"] if memoire_seuil is None else memoire_seuil
    code = mecanismes_code()
    lignees = communs["lignees"]
    textes = {lg["l"]: [] for lg in lignees}          # textes reçus de la lignée, refusés compris, dans l'ordre d'arrivée
    cles_textes = {lg["l"]: [] for lg in lignees}
    jugees = {lg["l"]: [] for lg in lignees}          # lois jugées (toutes éliminées tant que la lignée est en course)
    cle_monde = {lg["l"]: journal.objet(lg["loi_monde"]) for lg in lignees}
    receptions, jugements, appels = [], {}, []
    for g in range(1, G + 1):
        numero = 0
        for lg in lignees:
            l = lg["l"]
            rng = rng_tache(racine, f"classe={classe}|course={course}|lignee={l}|generation={g}|variantes")
            lois = variantes(lg, rng, n_var, P)
            d1 = [statistique_test_de_mort(x, lg["tranche"], K) for x in lois]
            ordre = sorted(range(len(lois)), key=lambda j: (-d1[j], j))
            premier = numero + 1
            appel = []
            for rang, j in enumerate(ordre, 1):
                loi, texte = lois[j], texte_carte(lois[j])
                ident = identifiant_reception(course, classe, l, g, rang)
                cle_loi, cle_texte = journal.objet(loi), journal.objet(texte)
                emp = JL.empreinte({"loi": loi, "texte": texte})
                numero += 1
                r = {"id": ident, "l": l, "g": g, "rang": rang, "type": loi["type"], "empreinte": emp,
                     "empreinte_loi": JL.empreinte(loi), "loi": loi, "texte": texte, "mots": len(texte.split()),
                     "caracteres": len(texte), "d1": d1[j], "d1_fraiche": statistique_test_de_mort(loi, lg["fraiche"], K),
                     "numero_course_pleine": numero, "premier_essai_appel": premier, "refus": None, "jugee": False}
                journal.decision("tronc", "reception", "reception", code["reception"],
                                 {"course": course, "classe": classe, "lignee": l, "generation": g, "rang": rang,
                                  "loi": cle_loi, "texte": cle_texte},
                                 {"identifiant": ident, "empreinte": emp})
                # étage 1 : mémoire anti-redite (une seule voie, liste de la lignée)
                smax, refusee = decider_memoire(texte, textes[l], seuil_mem, mem["taille_bardeau"], mem["epsilon"])
                journal.decision("tronc", "memoire", "memoire", code["memoire"],
                                 {"identifiant": ident, "texte": cle_texte, "comparees": list(cles_textes[l]),
                                  "seuil": seuil_mem, "taille_bardeau": mem["taille_bardeau"], "epsilon": mem["epsilon"]},
                                 {"similarite_max": smax, "refusee": refusee})
                textes[l].append(texte)
                cles_textes[l].append(cle_texte)
                r["similarite_max"] = smax
                r["refus_memoire"] = refusee
                if refusee:
                    r["refus"] = "memoire"
                appel.append(r)
                receptions.append(r)
            # étage 2 : règle « affinage »
            deja = False
            cles_jugees = [journal.objet(x) for x in jugees[l]]
            for r in appel:
                if r["refus"]:
                    continue
                d, refusee = decider_affinage(r["loi"], jugees[l], cfg["affinage"]["rayon"], deja)
                journal.decision("tronc", "affinage", "affinage", code["affinage"],
                                 {"identifiant": r["id"], "loi": journal.objet(r["loi"]), "jugees_eliminees": cles_jugees,
                                  "rayon": cfg["affinage"]["rayon"], "deja_une_dans_l_appel": deja},
                                 {"derive": d, "refusee": refusee})
                if refusee:
                    r["refus"] = "affinage"
                elif d:
                    deja = True
            # étage 3 : quota d'aiguillage
            restantes = [r["id"] for r in appel if not r["refus"]]
            pris, ecartes = decider_quota(restantes, cfg["quota"])
            journal.decision("tronc", "quota", "quota", code["quota"], {"restantes": restantes, "quota": cfg["quota"]},
                             {"jugees": pris, "ecartees": ecartes})
            par_id = {r["id"]: r for r in appel}
            for i in ecartes:
                par_id[i]["refus"] = "quota"
            for i in pris:
                r = par_id[i]
                r["jugee"] = True
                tache = f"course={course}|lignee={l}|generation={g}|carte={i}"
                ev, detail = juger_banc(r["loi"], lg["loi_monde"], racine, tache, cfg["juge"], K, DIM)
                cle_ev = journal.objet(ev)
                journal.decision("tronc", "jugement", "jugement", code["jugement"],
                                 {"identifiant": i, "loi": journal.objet(r["loi"]), "loi_monde": cle_monde[l], "archive": {},
                                  "racine": racine, "tache": tache, "tirages": cfg["juge"]["tirages"],
                                  "alpha": cfg["juge"]["alpha"], "entrainement": cfg["juge"]["entrainement"],
                                  "instants": cfg["juge"]["instants"]},
                                 {"issue": cle_ev, "empreinte_engagement": detail["empreinte_engagement"]})
                verite = None
                if lg["a_effet"]:
                    gain = gain_oracle(r["loi"], lg["oracle"])
                    exiger_fini([gain], f"oracle ({i})")
                    verite = {"gain": gain, "etiquette": etiquette_oracle(gain, cfg["verite"]["seuil_vraie"])}
                else:
                    verite = {"gain": None, "etiquette": "fausse"}
                jugements[i] = {"ev": ev, "cle_ev": cle_ev, "l": l, "g": g, "verite": verite, "tache": tache,
                                "empreinte_engagement": detail["empreinte_engagement"]}
            for i in pris:
                jugees[l].append(par_id[i]["loi"])
            appels.append({"l": l, "g": g, "receptions": len(appel), "jugees": len(pris)})
    return {"course": course, "classe": classe, "n_var": n_var, "receptions": receptions, "jugements": jugements,
            "appels": appels, "appels_programmes": len(appels),
            "empreintes_communes": {lg["l"]: empreinte_commune(lg) for lg in lignees},
            "lignees": [{k: lg[k] for k in ("l", "role", "a_effet", "cible", "force")} for lg in lignees],
            "cle_monde": cle_monde}


def verifier_appariement(pleine_a, pleine_b, appels_attendus):
    """Garde A3 : mêmes appels programmés, mêmes mondes, rôles, hypothèses et tranches entre les deux classes d'une course."""
    if pleine_a["appels_programmes"] != appels_attendus or pleine_b["appels_programmes"] != appels_attendus:
        raise GardeA3Appariement(f"garde A3 : appels programmés {pleine_a['appels_programmes']} et "
                                 f"{pleine_b['appels_programmes']} (attendu {appels_attendus} dans chaque classe)")
    if pleine_a["empreintes_communes"] != pleine_b["empreintes_communes"]:
        raise GardeA3Appariement("garde A3 : monde, rôle, hypothèse ou tranche différents entre les deux classes d'une course")
    return True


# --- registre, règles de promotion, bras -------------------------------------------------------------------------------------
_CONTEXTE = {"etalonnage": False}


class contexte_etalonnage:
    """Pendant l'étalonnage, seul le témoin T0 peut être joué (garde A17)."""

    def __enter__(self):
        _CONTEXTE["etalonnage"] = True
        return self

    def __exit__(self, *a):
        _CONTEXTE["etalonnage"] = False
        return False


def numeroter(receptions_vivantes, n_var, lignees_en_course, m_s):
    """Garde A4 : numéros 1..m_r dans l'ordre d'arrivée ; m_r = somme des variantes reçues des lignées en course ; m_r ≥ m_s."""
    numeros = [[r["id"], k] for k, r in enumerate(receptions_vivantes, 1)]
    m_r = len(numeros)
    attendu = n_var * len(lignees_en_course)
    recues = sorted({r["l"] for r in receptions_vivantes})
    if m_r != attendu or recues != sorted(lignees_en_course) or [n for _, n in numeros] != list(range(1, m_r + 1)) or m_r < m_s:
        raise GardeA4Registre(f"garde A4 : registre incomplet (m_r = {m_r}, attendu {attendu}, m_s = {m_s})")
    return numeros, m_r


def m_par_definition(receptions_vivantes, cumul_precedent):
    """Compte m sous chaque définition d'« un essai » (E0 retenue ; E1, E2, E3 de rechange), fixé avant toute issue."""
    m_r = len(receptions_vivantes)
    return {"E0": m_r,
            "E1": len({r["empreinte_loi"] for r in receptions_vivantes}),
            "E2": sum(1 for r in receptions_vivantes if not r["refus_memoire"]),
            "E3": cumul_precedent + m_r}


def regle_e_bh(cartes, alpha, m_fixe, m_passe):
    """Bras a, a′, d, d-E* : appartenance à `retenues` de `cycle.appliquer_multiplicite` (la fonction de l'organisme), sur
    une copie profonde des issues. Garde A5 : m passé = m fixé avant les issues."""
    if m_passe != m_fixe:
        raise GardeA5CompteM(f"garde A5 : m passé à la règle ({m_passe}) ≠ compte fixé avant les issues ({m_fixe})")
    issues = {i: {"verdict_final": "survit" if ev["promue"] else "eliminee", "motif": "", "pari": copy.deepcopy(ev)}
              for i, ev in cartes}
    res = CYC.appliquer_multiplicite(issues, alpha, m_fixe=m_passe)
    if res["m"] != m_fixe:
        raise GardeA5CompteM(f"garde A5 : la règle a lu m = {res['m']} au lieu de {m_fixe}")
    return list(res["retenues"]), issues


def regle_bonferroni(cartes, alpha, G, m_s):
    """Bras b : trajectoire qui atteint log(G·m_s/α) à l'un des instants de lecture (seuil propre, fixé avant les tirages)."""
    seuil = math.log(G * m_s / alpha) if m_s else math.inf
    return [i for i, ev in cartes if any(v >= seuil for v in ev["trajectoire_log_w"])]


def regle_seule(cartes):
    """Témoin T0 : la carte seule atteint 1/α (`promue` de l'évaluateur)."""
    return [i for i, ev in cartes if ev["promue"]]


def choisir_c(cartes, instant):
    """Bras c : la carte de plus haute valeur de trajectoire au quatrième instant ; ex æquo, le plus petit identifiant."""
    if not cartes:
        return None
    return sorted(cartes, key=lambda c: (-c[1]["trajectoire_log_w"][instant - 1], c[0]))[0][0]


def jouer_bras(nom, pleine, communs, P, journal, cache_confirmations, m_passe_decalage=0):
    """Rejoue la course pleine sous la règle d'un bras (arrêts de lignées propres au bras). `m_passe_decalage` n'existe que
    pour l'artefact de la garde A5 (m abaissé d'une unité)."""
    if _CONTEXTE["etalonnage"] and nom in BRAS_INTERDITS_A_L_ETALONNAGE:
        raise GardeA17BrasEtalonnage(f"garde A17 : bras {nom} calculé pendant l'étalonnage : étalonnage invalide")
    if nom not in BRAS:
        raise ValueError(f"bras inconnu : {nom}")
    cfg = P["config"]
    G, alpha = P["G"], cfg["alpha"]
    code = mecanismes_code()
    partie = f"bras={nom}"
    en_course = sorted(lg["l"] for lg in communs["lignees"])
    lignee_de = {lg["l"]: lg for lg in communs["lignees"]}
    receptions, jugements = pleine["receptions"], pleine["jugements"]
    cumul = 0
    gens, tirages, confirmations, m_portes = [], 0, [], 0
    for g in range(1, G + 1):
        vivantes = [r for r in receptions if r["g"] == g and r["l"] in en_course]
        jug = [r["id"] for r in vivantes if r["jugee"]]
        m_s = len(jug)
        numeros, m_r = numeroter(vivantes, pleine["n_var"], en_course, m_s)
        m_def = m_par_definition(vivantes, cumul)
        cumul += m_r
        journal.decision(partie, "registre", "registre", code["registre"],
                         {"generation": g, "lignees_en_course": list(en_course),
                          "receptions": [[r["id"], r["l"], r["empreinte_loi"], r["refus_memoire"]] for r in vivantes],
                          "cumul_precedent": cumul - m_r, "m_s": m_s, "n_var": pleine["n_var"]},
                         {"numeros": numeros, "m_r": m_r, "m": m_def})
        cartes = [(i, jugements[i]["ev"]) for i in jug]
        cartes_j = [[i, jugements[i]["cle_ev"]] for i in jug]
        tirages += m_s * cfg["juge"]["tirages"]
        info = {"g": g, "en_course": list(en_course), "m_r": m_r, "m_s": m_s, "m_def": m_def}
        if nom in ("a", "a_prime", "d", "d_E1", "d_E2", "d_E3"):
            definition = {"a": None, "a_prime": None, "d": "E0", "d_E1": "E1", "d_E2": "E2", "d_E3": "E3"}[nom]
            a_niveau = alpha if nom == "a" else alpha / G
            m_brut = m_s if definition is None else m_def[definition]
            m = max(m_brut, m_s)
            if m != m_brut:
                m_portes += 1
            promues, _ = regle_e_bh(cartes, a_niveau, m, m + m_passe_decalage)
            journal.decision(partie, "promotion", "promotion_e_bh", code["promotion_e_bh"],
                             {"generation": g, "cartes": cartes_j, "alpha": a_niveau, "m": m, "m_brut": m_brut, "m_s": m_s,
                              "definition_essai": definition or "cartes_jugees"},
                             {"promues": promues})
            info.update(m=m, m_brut=m_brut, alpha=a_niveau)
        elif nom == "b":
            promues = regle_bonferroni(cartes, alpha, G, m_s)
            journal.decision(partie, "promotion", "promotion_bonferroni", code["promotion_bonferroni"],
                             {"generation": g, "cartes": cartes_j, "alpha": alpha, "G": G, "m_s": m_s},
                             {"promues": promues})
            info.update(m=m_s, alpha=alpha / G)
        elif nom == "T0":
            promues = regle_seule(cartes)
            journal.decision(partie, "promotion", "promotion_seule", code["promotion_seule"],
                             {"generation": g, "cartes": cartes_j}, {"promues": promues})
        else:  # bras c
            bc = cfg["bras_c"]
            choisie = choisir_c(cartes, bc["instant_tri"])
            journal.decision(partie, "choix_c", "choix_c", code["choix_c"],
                             {"generation": g, "cartes": cartes_j, "instant": bc["instant_tri"]}, {"choisie": choisie})
            promues = []
            if choisie is not None:
                r = next(x for x in vivantes if x["id"] == choisie)
                lg = lignee_de[r["l"]]
                tache = f"course={communs['course']}|lignee={r['l']}|generation={g}|carte={choisie}|confirmation"
                a_conf = alpha / G
                if tache not in cache_confirmations:
                    ev_c, det_c = juger(r["loi"], lg["loi_monde"], {}, communs["racine"], tache,
                                        tirages=bc["tirages_confirmation"], alpha=a_conf, entrainement=cfg["juge"]["entrainement"],
                                        nombre_instants=bc["instants_confirmation"], K=P["K"], DIM=P["DIM"])
                    cache_confirmations[tache] = (ev_c, det_c)
                ev_c, det_c = cache_confirmations[tache]
                cle_c = journal.objet(ev_c)
                journal.decision(partie, "jugement", "jugement", code["jugement"],
                                 {"identifiant": choisie, "loi": journal.objet(r["loi"]), "loi_monde": pleine["cle_monde"][r["l"]],
                                  "archive": {}, "racine": communs["racine"], "tache": tache,
                                  "tirages": bc["tirages_confirmation"], "alpha": a_conf,
                                  "entrainement": cfg["juge"]["entrainement"], "instants": bc["instants_confirmation"]},
                                 {"issue": cle_c, "empreinte_engagement": det_c["empreinte_engagement"]})
                seuil = math.log(G / alpha)
                promue = any(v >= seuil for v in ev_c["trajectoire_log_w"])
                journal.decision(partie, "promotion", "promotion_c", code["promotion_c"],
                                 {"generation": g, "issue": cle_c, "seuil_log": seuil}, {"promue": promue})
                tirages += bc["tirages_confirmation"]
                confirmations.append({"g": g, "id": choisie, "promue": promue,
                                      "trajectoire": ev_c["trajectoire_log_w"],
                                      "empreinte_engagement": det_c["empreinte_engagement"],
                                      "empreinte_engagement_tri": jugements[choisie]["empreinte_engagement"]})
                if promue:
                    promues = [choisie]
        arretees = sorted({jugements[i]["l"] for i in promues})
        suivante = [l for l in en_course if l not in arretees]
        journal.decision(partie, "arret", "arret", code["arret"],
                         {"generation": g, "en_course": list(en_course), "promues": [[i, jugements[i]["l"]] for i in promues]},
                         {"arretees": arretees, "en_course_suivante": suivante})
        info["promues"] = list(promues)
        gens.append(info)
        en_course = suivante
    return {"bras": nom, "generations": gens, "tirages": tirages, "confirmations": confirmations, "m_portes_a_m_s": m_portes,
            "appels_emis": sum(len(x["en_course"]) for x in gens)}


# --- course entière ---------------------------------------------------------------------------------------------------------
def entete_journal(course, classe, racine, P, sha_config, prereg):
    return {"version_banc": VERSION, "course": course, "classe": classe, "racine": racine,
            "preenregistrement": {"chemin": PREREG_CHEMIN, "sha256": PREREG_SHA256},
            "configuration_sha256": sha_config, "parametres": {"forces": P["forces"], "s": P["s"], "c": P["c"]},
            "organisme": {"commit": P["config"]["organisme"]["commit"], "fichiers": ORGANISME.get("fichiers")},
            "code": {n: sha256_fichier(os.path.join(DOSSIER_CODE, n)) for n in FICHIERS_CODE
                     if os.path.isfile(os.path.join(DOSSIER_CODE, n))}}


def sortie_brute(pleine, bras):
    """Sortie brute d'une course et d'une classe (lue par l'analyse ; aucune loi longue, aucune trajectoire de bras)."""
    recs = [{k: r[k] for k in ("id", "l", "g", "rang", "type", "empreinte", "empreinte_loi", "mots", "caracteres", "d1",
                               "d1_fraiche", "numero_course_pleine", "premier_essai_appel", "refus", "refus_memoire",
                               "similarite_max", "jugee")} for r in pleine["receptions"]]
    jug = {i: {"l": j["l"], "g": j["g"], "trajectoire": j["ev"]["trajectoire_log_w"], "promue_seule": j["ev"]["promue"],
               "verite": j["verite"], "empreinte_engagement": j["empreinte_engagement"]} for i, j in pleine["jugements"].items()}
    return {"course": pleine["course"], "classe": pleine["classe"], "n_var": pleine["n_var"], "lignees": pleine["lignees"],
            "appels_programmes": pleine["appels_programmes"], "appels": pleine["appels"], "receptions": recs,
            "jugements": jug, "bras": bras, "empreintes_communes": pleine["empreintes_communes"]}


def jouer_course(course, racine, P, dossier, sha_config, prereg, bras=BRAS, ecrire=True, memoire_seuil_par_classe=None,
                 communs_par_classe=None):
    """Une course, les deux classes : objets communs, course pleine par classe, garde A3, bras. Écrit un journal et une sortie
    brute par classe (scellés). `memoire_seuil_par_classe` et `communs_par_classe` n'existent que pour les artefacts des
    gardes A15 et A3."""
    cfg = P["config"]
    communs = objets_communs(course, racine, P)
    classes = tuple(cfg["proposeurs"]["engagements_par_appel"])
    pleines, sorties, fichiers = {}, {}, {}
    journaux = {}
    for classe in classes:
        com = (communs_par_classe or {}).get(classe, communs)
        if ecrire:
            chemin = os.path.join(dossier, f"journal-c{course:04d}-{classe}.jsonl.xz")
            journaux[classe] = JL.Journal(chemin + ".partiel", entete_journal(course, classe, racine, P, sha_config, prereg))
        else:
            journaux[classe] = JL.JournalNul()
        seuil = (memoire_seuil_par_classe or {}).get(classe)
        pleines[classe] = jouer_course_pleine(com, classe, P, journaux[classe], memoire_seuil=seuil)
    verifier_appariement(pleines[classes[0]], pleines[classes[1]], P["L"] * P["G"])
    for classe in classes:
        com = (communs_par_classe or {}).get(classe, communs)
        cache = {}
        res = {nom: jouer_bras(nom, pleines[classe], com, P, journaux[classe], cache) for nom in bras}
        sorties[classe] = sortie_brute(pleines[classe], res)
    if ecrire:
        for classe in classes:
            j = journaux[classe]
            j.fermer()
            final = os.path.join(dossier, f"journal-c{course:04d}-{classe}.jsonl.xz")
            os.remove(j.chemin + ".sha256")
            os.replace(j.chemin, final)
            sha_j = sha256_fichier(final)
            with open(final + ".sha256", "w", encoding="utf-8") as f:
                f.write(f"{sha_j}  {os.path.basename(final)}\n")
            fichiers[os.path.basename(final)] = {"sha256": sha_j, "octets_bruts": j.octets_bruts, "lignes": j.nombre_lignes,
                                                "octets": os.path.getsize(final)}
            chemin_s = os.path.join(dossier, f"sortie-c{course:04d}-{classe}.json.xz")
            sha_s, taille = ecrire_json_xz_scelle(chemin_s, sorties[classe])
            fichiers[os.path.basename(chemin_s)] = {"sha256": sha_s, "octets": taille}
    return {"course": course, "sorties": sorties, "pleines": pleines, "communs": communs, "fichiers": fichiers}


def ecrire_json_xz_scelle(chemin, objet):
    """JSON canonique compressé (xz, préréglage 6, déterministe), écrit sous un nom provisoire puis renommé, compagnon
    `.sha256`."""
    import lzma
    if os.path.exists(chemin):
        raise FileExistsError(f"{chemin} déjà présent : on n'écrase jamais (R12)")
    provisoire = chemin + ".partiel"
    with open(provisoire, "wb") as brut:
        with lzma.LZMAFile(brut, mode="wb", format=lzma.FORMAT_XZ, preset=6) as xz:
            xz.write(JL.canonique(objet) + b"\n")
    os.replace(provisoire, chemin)
    sha = sha256_fichier(chemin)
    with open(chemin + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha, os.path.getsize(chemin)


def lire_json_xz_verifie(chemin):
    """Lit un fichier compressé scellé après vérification de son compagnon (sinon `ArretBanc`)."""
    import lzma
    with open(chemin + ".sha256", encoding="utf-8") as f:
        attendue = f.read().split()[0]
    if sha256_fichier(chemin) != attendue:
        raise ArretBanc(f"{chemin} : empreinte différente de son compagnon")
    with lzma.open(chemin, "rb") as f:
        return json.loads(f.read())


def ecrire_json_scelle(chemin, objet):
    if os.path.exists(chemin):
        raise FileExistsError(f"{chemin} déjà présent : on n'écrase jamais (R12)")
    texte = json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n"
    provisoire = chemin + ".partiel"
    with open(provisoire, "w", encoding="utf-8") as f:
        f.write(texte)
    os.replace(provisoire, chemin)
    sha = sha256_fichier(chemin)
    with open(chemin + ".sha256", "w", encoding="utf-8") as f:
        f.write(f"{sha}  {os.path.basename(chemin)}\n")
    return sha


def lire_json_verifie(chemin):
    with open(chemin + ".sha256", encoding="utf-8") as f:
        attendue = f.read().split()[0]
    if sha256_fichier(chemin) != attendue:
        raise ArretBanc(f"{chemin} : empreinte différente de son compagnon")
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def verifier_scelle_fichier(chemin):
    """Vrai si le fichier existe et correspond à son compagnon `.sha256`."""
    try:
        with open(chemin + ".sha256", encoding="utf-8") as f:
            attendue = f.read().split()[0]
    except (OSError, IndexError):
        return False
    return os.path.isfile(chemin) and sha256_fichier(chemin) == attendue
