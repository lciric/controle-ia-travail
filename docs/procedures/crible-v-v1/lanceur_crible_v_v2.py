"""Lanceur du crible (v) de l'organisme d'idéation — code v2 (fichier neuf, R12 ; `lanceur_crible_v_v1.py` reste en place,
inchangé), scellé à 2026-11-17T02:29:27Z (`date -u`) ; suit la v1 (`2636bcb1…`) par les corrections du tour 1 de sa contre-lecture
et les seuls changements de nom de la version (section « Contre-lecture », en fin d'en-tête). La v1 était dérivée du lanceur
v74 du pilote MR-2
(`orchestrator/demonstrations/pilote_mr2_v74.py` de l'arbre de l'organisme, tête 605e0f6, **lu, non modifié**).

Texte : `crible-v-version-foi-v2.md` (version qui fera foi v2), sections « Plan d'analyse » (partie B), « Liste d'arrêt »,
« Devis » (sous-section qui fait foi : B_a, règle de M, garde de départ). Ce qui change par rapport au lanceur du pilote :
- **20 mondes** du secret du crible (`graine_monde_crible`, étiquette « crible-v-v1 ») ; épisodes de développement à l'étiquette
  neuve ; oracle `cle("oracle-crible-v", empreinte du devis)` ; étiquettes C8 « certifiée » de `verifier_v4` gardées à la
  génération (`CERTIFIEES.json`, privé) ;
- **mondes en files parallèles** : M files (1 ou 2, règle de M), chacune avec ses quatre relais (ports de la configuration v12
  décalés de 10 par file : 4 M relais ouverts), plafond de chaque relais = (mondes de sa file) × plafond de session ; dans une
  file, les mondes l'un après l'autre ; **les quatre appels d'un monde partent ensemble** (un fil par appel) ;
- **borne par appel B_a = 900 s**, donc par monde : un appel plus long est **coupé** (commande tuée), compté « échec »,
  journalisé dans `coupures-crible-v-v1.jsonl` (relu : une coupure sans trace arrête), jamais repris, compté au plafond de
  session dans les dollars (l'amont a pu facturer) ; ce n'est **pas** une panne de relais (aucun abandon) ;
- **abandon d'un fournisseur** (voie de relais à clé commune : Pr-2 et Pr-4, Pr-1, Pr-3) dès qu'un de ses appels finit en panne
  de relais (codes 2, 3, 4, 6 de la commande, causes `modele_servi`, `usage_absent`) : ses appels restants « échec » sans être
  lancés ; **arrêt du crible** (aucune dépense de plus) si ce fournisseur n'a encore aucun appel répondu, ou si le minimum de
  16 mondes complets n'est plus possible ;
- **corps servi** (gabarit, archive {K1}, épisodes) relu et **égal pour les quatre appels d'un monde** avant ses appels ;
- **garde de départ** : arrêt sans appel si le temps restant avant l'échéance de la minuterie est sous 6 000 + 3 D + ⌈20/M⌉ × B_a ;
- mode réel : configuration v12 à son empreinte, numpy 2.5.3, texte et addendum d'empreintes à leurs empreintes (code du crible),
  relevé de la **sonde neuve** du chemin des relais du crible, lignes κv1 et κv2 au montant exact, engagement des mondes,
  registre des lancements (un seul lancement par texte), D relevée et M de la règle.

Sous-commandes (sorties imprimées : empreintes et contrôles seulement ; aucune loi, aucun devis) :
  secret   CHEMIN_PRIVE/secret.bin
  generer  --arbre ORCH --secret S --phrase-fichier F --texte T --texte-sha256 H --sortie PRIVE/MONDES.json [--processus K]
  preparer --arbre ORCH --mondes M --mondes-sha256 H
  sonde    --arbre ORCH --mode a_blanc|reel --go-kv1 GO --go-kv2 GO --registre-go R --registre-lancements F --sortie D
           (payante en mode réel : jamais jouée par le développeur)
  jouer    --arbre ORCH --mode a_blanc|reel --mondes M --mondes-sha256 H --certifiees C --certifiees-sha256 HC --files 1|2
           --sortie D ; mode réel, exigés : --go-kv1 --go-kv2 --registre-go --texte --texte-sha256 --mondes-shas
           --registre-lancements --releve-sonde --addendum --addendum-sha256 --echeance-utc-s --duree-d-s
           à blanc seulement : [--scenarios NOM=SCENARIO,…] [--lent W:NOM,…] [--borne-essai-s X] [--decalage-ports P]
           [--echeance-utc-s E --duree-d-s D] (garde de départ essayée)
  mesurer  --arbre ORCH --sortie D --mondes M --mondes-sha256 H --certifiees C --certifiees-sha256 HC --texte-sha256 H
  lire     --sortie D --ecrire F
  rapatrier --source D --destination X --mondes M --mondes-sha256 H --arbre ORCH
Codes : 0 conforme ; 2 refus nommé (rien appelé) ; 3 arrêt (pièces versées).

Contre-lecture
- Rapport : `contre-lecture-code-crible-v-tour1-v1.md` (même dossier), empreinte
  `05809ac265f80e766690e43d5741f1fbd890e9057773658c0cfc4e4a6d959675` ; contre-lecteur neuf, d'un autre modèle que l'auteur de
  la v1 (R2) ; verdict « corrections » : quatre majeures (M1 à M4), quatre mineures (m1 à m4), cinq remarques facultatives
  (f1 à f5) et des points pour la mère (§ 5).
- Cette version : v2, écrite par un rédacteur neuf, qui n'a écrit ni la v1 ni le rapport, par le programme de couples
  `corriger_lanceur_crible_v_v1_vers_v2_tour1_v1.py` (même dossier, scellé avec son compagnon), depuis la v1
  `2636bcb1deefc0a7dc1427bb476b7c0e2efdc1b5ae6d9e76c3a7c2ac592d7725` ; chaque ancien présent une fois ; les couples du rapport
  sont recopiés tels qu'il les écrit (le programme retrouve leur ancien et leur nouveau, à l'identique, parmi les blocs du rapport).
- Réponse point par point :
  - M1 (l'outil de la session refuse le plafond de κv1 écrit « 104.39 USD (sur crédits) ») : correction de l'outil de la
    session, hors de ce lanceur ; le lecteur des lignes de GO de ce lanceur (`lire_go_du_crible`, lecteur v66 de l'arbre)
    accepte cette forme (rapport, M1 ; rejoué par le rédacteur sur les deux lignes du texte) ; rien ne change ici.
  - M2 (à M = 2, un arrêt levé dans une file n'arrêtait l'autre qu'une fois la file 0 finie) : appliquée, couple du rapport ;
    chaque file tourne dans une enveloppe qui, dès qu'une exception sort de la file, pose l'arrêt sous le verrou, puis la relève ;
    l'autre file s'arrête avant son monde suivant (seuls les appels déjà en vol finissent ; aucune dépense de plus).
  - M3 (la règle d'abandon dépendait de l'ordre de traitement des quatre appels d'un monde) : appliquée, deux couples du
    rapport ; les résultats des appels d'un monde sont d'abord tous recueillis, puis traités sous le verrou, les appels répondus
    vus du lanceur avant les autres (ordre des noms gardé entre égaux) ; « perdu en entier » ne dépend plus de l'ordre des noms.
  - M4 (dollars lus aux journaux des relais et dépense d'un appel coupé, sans essai) : correction des essais et du banc, hors de
    ce lanceur ; les deux textes que visent les mutations M29 et M30 proposées par le rapport restent ici inchangés, une fois
    chacun (contrôle de sortie du programme).
  - m1 (repli silencieux à zéro dans les dollars) : appliquée, couple du rapport ; un appel lancé, non coupé, sans ligne au
    journal de son relais prend le coût rendu par la commande (zéro seulement si la commande n'en a rendu aucun) ; la source
    écrite reste « journal_relais », comme le couple l'écrit.
  - m2 (portes du mode réel sans essai propre) : correction des essais ou de la répétition, hors de ce lanceur.
  - m3 (cadence de la minuterie : procédure et amorce) : hors de ce lanceur.
  - m4 (option de configuration acceptée en mode réel) : appliquée, couple du rapport ; la configuration rejoint les options de
    l'essai à blanc, refusées en mode réel (la machine ne la passe jamais).
  - f1 à f5 : remarques facultatives, aucune correction exigée ; rien d'appliqué.
  - Points pour la mère (§ 5) : non tranchés ici.
- Changements de nom, conséquences du nom neuf (R12), non corrections du rapport : la version que le lanceur écrit dans ses
  pièces passe à « lanceur-crible-v-v2 », et le lanceur que portent les empreintes du code du crible (addendum, manifeste,
  relevé de la sonde) est ce fichier, `lanceur_crible_v_v2.py`, pour que le code attesté soit celui qui tourne. Les pièces qui
  nomment le lanceur v1 (programme machine, outil de la session, essais, banc, répétition, gabarits, procédure) ne jouent pas
  cette v2 tant que leurs versions neuves ne la nomment pas.
- Rien d'autre ne change de la v1 à la v2 : en tête (version, heure, cette section), les cinq couples du rapport et les deux
  changements de nom ; noms des fichiers écrits, sous-commandes, options, gardes et nombres sont ceux de la v1.
- Rejeu exigé après les couples : essais (paliers unitaire, jouer, mesure) et banc de mutations, joués contre cette v2 ; sorties
  et empreintes rendues à la mère, hors de ce fichier.
"""

import argparse
import concurrent.futures
import copy
import datetime
import hashlib
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
import threading
import time

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)
import crible_v_commun_v1 as K  # noqa: E402

VERSION = "lanceur-crible-v-v2"
CONFIG_V12_SHA256 = "f69503dd4ba5e57a8bde230b3861571549d9598382808a8f3c0f4fa664ea818b"
CONFIG_REL = os.path.join("exemples", "pilote-mr2-v70", "configuration-pilote-mr2-v12.json")
ARBRE_TETE = "605e0f60f3eed0948948e6a4eb15cb73de1d03de"
FICHIERS_DU_CRIBLE = ("crible_v_commun_v1.py", "lanceur_crible_v_v2.py", "mesure_crible_v_v1.py", "lire_crible_v_v1.py")
PROGRAMME_MESURE = os.path.join(ICI, "mesure_crible_v_v1.py")
PROGRAMME_LECTURE = os.path.join(ICI, "lire_crible_v_v1.py")
NOMS = {"cartes": "CARTES.json", "partiel": "CARTES-partiel.json", "dollars": "DOLLARS.json", "releve": "releve-crible-v-v1.json",
        "manifeste": "manifeste-crible-v-v1.json", "coupures": "coupures-crible-v-v1.jsonl",
        "sortie": "sortie-mesure-crible-v-v1.json", "fictive": "sortie-fictive-crible-v-v1.json",
        "piece": "mesure-crible-v-v1.json", "lecture": "lecture-crible-v-v1.json", "releve_sonde": "releve-sonde-crible-v-v1.json"}
DECALAGE_FILE = 10
SCENARIO_A_BLANC = "k1_plus"
CHAMPS_A_BLANC = ("scenarios", "lent", "borne_essai_s", "decalage_ports", "configuration")
_ARBRE = {}


def maintenant():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")


def imprimer(objet):
    print(json.dumps(objet, ensure_ascii=False, sort_keys=True))


# --- arbre de l'organisme (modules lus, jamais modifiés) ----------------------------------------------------------------------

def charger_arbre(orch):
    """Les modules de l'arbre (tête 605e0f6) : cœur du pilote, proposeurs (v70, v72), sonde v74, audit, lanceur v74 ; la
    configuration v12 à son empreinte. Rend un objet d'attributs P, PR, PC, S, AU, L74, CONF, ORCH."""
    orch = os.path.realpath(orch)
    if _ARBRE.get("orch") == orch:
        return _ARBRE["A"]
    if not os.path.isfile(os.path.join(orch, "pole", "pilote_mr2_v70.py")):
        raise K.Refus(f"arbre de l'organisme absent : {orch}")
    if orch not in sys.path:
        sys.path.insert(0, orch)
    from pole import audit_pilote_v70 as AU  # noqa: E402
    from pole import pilote_mr2_v70 as P  # noqa: E402
    from pole import proposeurs_pilote_v70 as PR  # noqa: E402
    from pole import proposeurs_pilote_v72 as PC  # noqa: E402
    from pole import sonde_pilote_v74 as S  # noqa: E402
    from demonstrations import pilote_mr2_v74 as L74  # noqa: E402
    for mod in (AU, P, PR, PC, S, L74):
        if not os.path.realpath(mod.__file__).startswith(orch + os.sep):
            raise K.Refus(f"module {mod.__name__} chargé hors de l'arbre {orch}")

    class A:
        pass
    a = A()
    a.P, a.PR, a.PC, a.S, a.AU, a.L74, a.ORCH = P, PR, PC, S, AU, L74, orch
    a.CONF = os.path.join(orch, CONFIG_REL)
    _ARBRE.update(orch=orch, A=a)
    return a


def lire_configuration_v12(A, chemin=None):
    """Ligne d'arrêt « configuration autre que v12 (identité, bornes, plafonds, réglages) » : l'empreinte du fichier est celle
    de la v12 (`f69503dd…`, bloc gelé du pilote), puis la lecture v72 (contrôles de la v70)."""
    chemin = chemin or A.CONF
    if not os.path.isfile(chemin) or K.sha256_fichier(chemin) != CONFIG_V12_SHA256:
        raise K.Refus("configuration autre que la v12 (empreinte ≠ f69503dd…) : arrêt avant tout appel")
    try:
        conf, _ = A.PC.lire_configuration(chemin)
    except A.P.Refus as e:
        raise K.Refus(f"configuration : {e}") from None
    return conf


def conf_de_la_file(conf, k):
    """La configuration vue par la file k : ports de la v12 décalés de 10 × k (rien d'autre ne change)."""
    c = copy.deepcopy(conf)
    for p in c["proposeurs"].values():
        p["port"] = p["port"] + DECALAGE_FILE * k
    return c


def fournisseurs(conf):
    """Voies de relais à clé commune, lues dans la configuration (même variable de clé) : {dialecte : proposeurs} (« claude » :
    Pr-2 et Pr-4 ; « gemini » : Pr-1 ; « astra » : Pr-3)."""
    par_cle, nom = {}, {}
    for n in K.PROPOSEURS:
        p = conf["proposeurs"][n]
        par_cle.setdefault(p["variable_cle"], []).append(n)
        nom.setdefault(p["variable_cle"], set()).add(p["dialecte"])
    if any(len(v) != 1 for v in nom.values()):
        raise K.Refus("configuration : une clé commune à deux dialectes")
    return {next(iter(nom[k])): tuple(sorted(v)) for k, v in par_cle.items()}


def empreintes_du_code_crible():
    return {f: K.sha256_fichier(os.path.join(ICI, f)) for f in FICHIERS_DU_CRIBLE}


def empreintes_du_code(A):
    """Code du crible et code gelé de l'arbre lu par le crible (liste des fichiers gelés du lanceur v74)."""
    out = {"crible/" + f: s for f, s in empreintes_du_code_crible().items()}
    out.update({"orchestrator/" + r: s for r, s in A.L74.empreintes_du_code().items()})
    return out


def exiger_addendum(chemin, sha):
    """Ligne d'arrêt « empreinte différente : texte, monde, pièce servie, gabarit, configuration, programme de mesure, module
    importé » : l'addendum d'empreintes est à son empreinte et porte, pour chaque fichier du code du crible, une ligne
    « <empreinte>  <nom> » égale au fichier présent."""
    if not chemin or not os.path.isfile(chemin) or K.sha256_fichier(chemin) != sha:
        raise K.Refus("addendum d'empreintes absent ou à empreinte différente")
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()
    for nom, s in empreintes_du_code_crible().items():
        lignes = re.findall(r"\b([0-9a-f]{64})\s+(?:\S*/)?" + re.escape(nom) + r"\b", texte)
        if not lignes or any(x != s for x in lignes):
            raise K.Refus(f"addendum d'empreintes : {nom} absent ou à empreinte différente du fichier présent ({s[:12]}…)")


# --- mondes : génération, chargement, préparation ---------------------------------------------------------------------------------

def _generer_un(arg):
    orch, graine = arg
    A = charger_arbre(orch)
    V4, _, _ = A.P.charger_mr2()
    spec, rap, refus = A.P.sans_chemin_v52b(V4.generer_v4, graine)
    if spec is None:
        return None, None, list(refus)
    certif = sorted(k for k, v in rap["sensibilite"].items()
                    if v["etiquette"].startswith("certifiée") and v["classe"] != "latente")
    return spec, {"certifiees": certif, "conforme": bool(rap["conforme"])}, list(refus)


def generer_mondes(A, secret, phrase, texte_sha256, processus=1):
    """C-15 du pilote, pour 20 mondes : graine `graine_monde_crible`, les 8 tirages de `generer_v4` ; un monde sans tirage
    conforme en 8 → Refus (arrêt avant tout appel). Rend (mondes, certifiées par monde, contrôles sans contenu)."""
    graines = [K.graine_monde_crible(secret, phrase, texte_sha256, r) for r in K.MONDES]
    args = [(A.ORCH, g) for g in graines]
    if processus > 1:
        import multiprocessing
        with multiprocessing.get_context("spawn").Pool(processus) as pool:
            res = pool.map(_generer_un, args, chunksize=1)
    else:
        res = [_generer_un(x) for x in args]
    mondes, certif, ctl = [], {}, []
    for r, (spec, c, refus) in zip(K.MONDES, res):
        if spec is None:
            raise K.Refus(f"monde {r} : aucun tirage conforme en {K.TIRAGES_PAR_MONDE} (refus {refus}) : arrêt avant tout appel")
        A.P.exiger_dimensions(spec)
        sha = A.P.sha_spec(spec)
        ids = {e["id"] for e in spec["effets"]}
        if not set(c["certifiees"]) <= ids:
            raise K.Refus(f"monde {r} : étiquettes C8 hors des effets du monde")
        mondes.append({"monde": r, "spec": spec, "spec_sha256": sha})
        certif[str(r)] = {"spec_sha256": sha, "certifiees": c["certifiees"], "tirages_refuses": refus}
        ctl.append({"monde": r, "spec_sha256": sha, "tirages_refuses": refus, "conforme": c["conforme"]})
    return mondes, {"version": "certifiees-crible-v-v1", "mondes": certif}, ctl


def ecrire_prive_json(A, chemin, objet, liste_blanche):
    return A.P.ecrire_prive(chemin, objet, liste_blanche)


def charger_mondes(A, chemin, sha_attendue, shas_mondes=None):
    """C-1 du pilote, pour 20 mondes : fichier hors de tout dépôt, empreinte égale à celle du registre, mondes numérotés 1 à 20,
    empreinte de chaque devis recalculée (et égale à la liste du registre si donnée)."""
    A.P.exiger_hors_depot(chemin, "fichier des mondes")
    if not isinstance(sha_attendue, str) or not re.fullmatch(r"[0-9a-f]{64}", sha_attendue):
        raise K.Refus("empreinte attendue du fichier des mondes : 64 chiffres hexadécimaux")
    if not os.path.isfile(chemin) or K.sha256_fichier(chemin) != sha_attendue:
        raise K.Refus("fichier des mondes absent ou d'empreinte différente de celle du registre")
    with open(chemin, encoding="utf-8") as f:
        mondes = json.load(f)
    if not isinstance(mondes, list) or len(mondes) != K.N_MONDES:
        raise K.Refus(f"fichier des mondes : exactement {K.N_MONDES} mondes")
    vus = set()
    for w in mondes:
        if not isinstance(w, dict) or set(w) != {"monde", "spec", "spec_sha256"} or isinstance(w["monde"], bool) \
                or w["monde"] not in K.MONDES or w["monde"] in vus:
            raise K.Refus("monde : clés {monde, spec, spec_sha256}, numéros 1 à 20 une fois chacun")
        vus.add(w["monde"])
        if A.P.sha_spec(w["spec"]) != w["spec_sha256"]:
            raise K.Refus(f"monde {w['monde']} : empreinte du devis différente")
        A.P.exiger_dimensions(w["spec"])
    if shas_mondes is not None and sorted(shas_mondes) != sorted(w["spec_sha256"] for w in mondes):
        raise K.Refus("empreintes des mondes ≠ celles du registre")
    return sorted(mondes, key=lambda w: w["monde"])


def episodes_du_monde(A, spec, n=K.EPISODES_DEVELOPPEMENT):
    """Règle des graines des épisodes du bloc gelé du pilote, étiquette neuve « crible-v-v1 » : SeedSequence(entier gros-boutiste
    des 16 premiers octets de sha256(« crible-v-v1|episodes-developpement| » ∥ empreinte du devis)), 400 instances, issues de la
    loi compilée, même générateur."""
    import numpy as np
    _, M, _ = A.P.charger_mr2()
    loi = A.P.compiler_monde(spec)
    cle = int.from_bytes(hashlib.sha256((K.ETIQUETTE_EPISODES + "|" + A.P.sha_spec(spec)).encode()).digest()[:16], "big")
    rng = np.random.default_rng(np.random.SeedSequence(cle))
    Z, G = M.tirer_instances(rng, n, spec["dimension"], spec["sous_populations"])
    Y = M.tirer_issues(rng, M.probas(loi, Z, G))
    return [{"z": [float(x) for x in z], "g": int(g), "y": int(y)} for z, g, y in zip(Z, G, Y)]


def preparer_crible(A, mondes):
    """Mondes préparés comme la mesure les prépare (oracle de 12 000 instances à `cle("oracle-crible-v", …)`, K1 du monde) : la K1
    servie est celle que la mesure retire des composantes comptées ; plus la première conditionnelle (lois de référence de C-16)."""
    V4, M, MP = A.P.charger_mr2()
    out = {}
    for w in mondes:
        spec = w["spec"]
        o = M.Oracle(M.compiler_monde(spec), spec["dimension"], spec["sous_populations"], n=K.ORACLE_N,
                     graine=V4.P1.cle(K.ETIQUETTE_ORACLE, w["spec_sha256"]))
        k1, eid_k1, infos = M.k1_du_monde(spec, o)
        cond = {e["id"]: e["composante_condition"] for e in spec["effets"] if e["type"] == "interaction_xor"}
        premiere = sorted(c for c, b in cond.items() if b not in cond)
        if len(premiere) != 1:
            raise K.Refus(f"monde {w['monde']} : première conditionnelle absente ou non unique (lois de référence de C-16)")
        out[w["monde"]] = {"spec": spec, "sha": w["spec_sha256"], "o": o, "infos": infos, "eid_k1": eid_k1, "k1": k1,
                           "premiere": premiere[0], "condition": cond[premiere[0]],
                           "secondes": sorted(c for c in cond if c != premiere[0])}
    return out


def preparer_les_mondes(A, chemin_mondes, sha_mondes, octets_max, shas_mondes=None):
    """C-1 → C-17 sans appel, pour 20 mondes ; rend (mondes, pm_, servis, contrôles publics, contrôles privés)."""
    P = A.P
    mondes = charger_mondes(A, chemin_mondes, sha_mondes, shas_mondes)
    for w in mondes:
        P.compiler_monde(w["spec"])
    pm_ = preparer_crible(A, mondes)
    try:
        c16_public, c16_prive = P.jouer_c16(pm_)
        episodes = {w: episodes_du_monde(A, pm_[w]["spec"]) for w in sorted(pm_)}
        c17 = P.jouer_c17(pm_, episodes)
    except P.Refus as e:
        raise K.Refus(f"C-16 ou C-17 en défaut : {e}") from None
    exiger_gabarit(P)
    servis, ctl_ep = {}, {}
    for w in sorted(pm_):
        archive, sha_arch = P.heritage_k1(pm_[w])
        texte = P.texte_servi(archive, episodes[w])
        n = len(texte.encode("utf-8"))
        if octets_max is not None and n > octets_max:
            raise K.Refus(f"monde {w} : texte servi de {n} octets > {octets_max}")
        ecarts = P.verifier_texte_servi(texte, archive, episodes[w])
        if ecarts:
            raise K.Refus(f"monde {w} : texte servi non conforme : {ecarts}")
        ctl_ep[str(w)] = P.controle_episodes(episodes[w])
        if not all(ctl_ep[str(w)].values()):
            raise K.Refus(f"monde {w} : épisodes servis non conformes : {ctl_ep[str(w)]}")
        servis[w] = {"texte": texte, "archive": archive, "episodes": episodes[w], "archive_sha256": sha_arch,
                     "texte_sha256": hashlib.sha256(texte.encode("utf-8")).hexdigest(), "octets": n,
                     "episodes_sha256": hashlib.sha256(K.json_canonique(episodes[w])).hexdigest()}
    controles = {"mondes": P.monde_au_manifeste(mondes, sha_mondes), "c16": c16_public,
                 "c17": {"instances": c17["instances"], "cartes": c17["cartes"], "ecart_max": c17["ecart_max"]},
                 "heritages_sha256": {str(w): s["archive_sha256"] for w, s in servis.items()},
                 "textes_servis": {str(w): {"sha256": s["texte_sha256"], "octets": s["octets"], "episodes_sha256": s["episodes_sha256"],
                                            "relu_conforme": True} for w, s in servis.items()},
                 "episodes_servis": ctl_ep, "gabarit_sha256": P.gabarit_sha256()}
    P.exiger_manifeste_sans_loi(controles)
    return mondes, pm_, servis, controles, {"c16": c16_prive}


# --- corps servis égaux, files, garde de départ ----------------------------------------------------------------------------------

def corps_de_l_appel(A, servi, gabarit_sha):
    """Le corps servi à un appel, relu depuis ses pièces : (texte, empreintes du texte, de l'archive, des épisodes, du gabarit)."""
    texte = A.P.texte_servi(servi["archive"], servi["episodes"])
    return {"texte": texte, "texte_sha256": hashlib.sha256(texte.encode("utf-8")).hexdigest(),
            "archive_sha256": hashlib.sha256(K.json_canonique(servi["archive"])).hexdigest(),
            "episodes_sha256": hashlib.sha256(K.json_canonique(servi["episodes"])).hexdigest(), "gabarit_sha256": gabarit_sha}


def exiger_corps_egaux(corps_par_proposeur, servi):
    """Ligne d'arrêt « corps servi différent entre les quatre appels d'un monde » : quatre empreintes égales, et égales à celles
    des pièces préparées (texte, archive, épisodes, gabarit) ; arrêt avant les appels du monde."""
    cles = ("texte_sha256", "archive_sha256", "episodes_sha256", "gabarit_sha256")
    vus = {tuple(c[k] for k in cles) for c in corps_par_proposeur.values()}
    attendu = (servi["texte_sha256"], hashlib.sha256(K.json_canonique(servi["archive"])).hexdigest(), servi["episodes_sha256"],
               K.GABARIT_SHA256)
    if len(vus) != 1 or vus != {attendu} or sorted(corps_par_proposeur) != sorted(K.PROPOSEURS):
        raise K.Arret("corps servi différent entre les quatre appels du monde (ou des pièces préparées) : arrêt avant ses appels")


def repartir_en_files(m):
    """File k (0 ≤ k < M) : les mondes k + 1, k + 1 + M, … dans l'ordre."""
    if m not in (1, 2):
        raise K.Refus("files : M = 1 ou 2 (règle de M)")
    return [[w for w in K.MONDES if (w - 1) % m == k] for k in range(m)]


def exiger_garde_de_depart(echeance_utc_s, m, d, horloge=time.time):
    """Ligne d'arrêt « minuterie de la machine » : arrêt (A) sans appel si le temps restant avant l'échéance est inférieur au
    budget de pire cas (6 000 s + 3 D + ⌈20/M⌉ × B_a)."""
    if echeance_utc_s is None or d is None:
        raise K.Refus("garde de départ : échéance de la minuterie et D exigées")
    budget = K.budget_depart_s(m, d)
    reste = float(echeance_utc_s) - horloge()
    if reste < budget:
        raise K.Refus(f"garde de départ : {reste:.0f} s avant l'échéance < budget de pire cas {budget:.0f} s "
                      f"(M = {m}, D = {d:g} s) : arrêt (A) sans appel")
    return {"reste_s": round(reste), "budget_s": budget, "M": m, "D_s": d}


def exiger_m_de_la_regle(m, d):
    regle = K.m_de_la_regle(d)
    if regle is None:
        raise K.Refus(f"budget de durée « non lançable » (D = {d!r} s, au-delà de 15 400 s ou non relevée) : mot de la mère")
    if m != regle:
        raise K.Refus(f"M = {m} ≠ M de la règle ({regle}) pour D = {d:g} s")
    return regle


# --- un appel, borné par B_a ----------------------------------------------------------------------------------------------------

def appeler_borne(A, conf, nom, texte, dossier_appel, jeton, python, borne_s, executer=subprocess.run):
    """Un appel, une session neuve (C-10 du pilote), par la commande gelée de la configuration v12, sur le relais de la file
    (`conf` de la file) ; **coupé à `borne_s`** (B_a) : la commande est tuée, l'appel compté « échec » (cause
    `au_dela_de_B_a`, aucune panne, aucun abandon), au plafond de session dans les dépenses. Réponse brute et témoin d'isolement
    écrits et scellés avant toute extraction ; mêmes arrêts que `appeler` du pilote (réponse sans dernière ligne, corps du relais
    absent pour un appel rendu, témoin non conforme, coût au-dessus du pire cas)."""
    PR = A.PR
    p = conf["proposeurs"][nom]
    if os.path.exists(dossier_appel):
        raise K.Arret(f"{nom} : dossier de session existant (session neuve exigée)")
    os.makedirs(dossier_appel)
    session = os.path.join(dossier_appel, "session")
    os.makedirs(session)
    avant = sorted(os.listdir(session))
    brut = os.path.join(dossier_appel, "corps-relais.json")
    cmd = PR.commande_d_un_proposeur(conf, nom, brut, python)
    env = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "PLAFOND_SESSION_USD": repr(float(p["plafond_session_usd"])),
           "ROLE_POLE": PR.ROLE, "MODELE_DEMANDE_POLE": p["modele"], "RELAIS_JETON_POLE": jeton}
    sha_texte = hashlib.sha256(texte.encode("utf-8")).hexdigest()
    debut = time.time()
    coupe = False
    try:
        r = executer(cmd, input=texte, capture_output=True, text=True, encoding="utf-8", cwd=session, env=env, timeout=float(borne_s))
        code, sortie, erreur = r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        code, erreur, coupe = None, "appel plus long que B_a : commande tuée", True
        sortie = json.dumps({"etat": "echec", "cause": "au_dela_de_B_a", "erreur": "appel coupé à B_a (commande tuée)",
                             "cout_usd": float(p["plafond_session_usd"]), "cout_origine": "plafond_de_session"})
    duree = round(time.time() - debut, 3)
    derniere = PR._derniere_ligne(sortie)
    brut_sha = K.sha256_fichier(brut) if os.path.isfile(brut) else None
    reponse = {"proposeur": nom, "code": code, "sortie_standard": sortie, "sortie_erreur": (erreur or "")[-4000:],
               "derniere_ligne": derniere, "corps_relais": "corps-relais.json" if brut_sha else None,
               "corps_relais_sha256": brut_sha, "duree_s": duree, "coupe_a_B_a": coupe, "borne_s": borne_s}
    sha_rep = K.ecrire_scelle_json(os.path.join(dossier_appel, "reponse-brute.json"), reponse)
    if derniere is None:
        raise K.Arret(f"{nom} : réponse brute sans dernière ligne JSON (code {code})")
    etat = "echec" if coupe or code != 0 else derniere.get("etat")
    if etat not in ("complet", "tronque", "echec"):
        raise K.Arret(f"{nom} : état rendu inconnu {etat!r}")
    if not coupe and brut_sha is not None and derniere.get("brut_sha256") not in (None, brut_sha):
        raise K.Arret(f"{nom} : corps du relais ≠ empreinte rendue par la commande")
    if etat in ("complet", "tronque"):
        if brut_sha is None or derniere.get("brut_sha256") != brut_sha or not K.compagnon_egal(brut):
            raise K.Arret(f"{nom} : appel rendu sans corps du relais scellé sur disque (M-4)")
    tr = None if coupe else derniere.get("temoin_relais")
    apres = sorted(os.listdir(session))
    temoin = {"proposeur": nom, "relais_attendu": f"relais-pilote-v70-{nom}", "relais": (tr or {}).get("relais"),
              "session_neuve": avant == [], "fichiers_ecrits_dans_la_session": apres,
              "texte_servi_sha256": sha_texte, "texte_recu_sha256": (tr or {}).get("consigne_recue_sha256"),
              "consigne_commande_sha256": derniere.get("consigne_sha256"),
              "outils": (tr or {}).get("outils"), "messages": (tr or {}).get("messages"), "systeme": (tr or {}).get("systeme"),
              "appelant": (tr or {}).get("appelant"), "reglages": (tr or {}).get("reglages"),
              "environnement_commande": sorted(env), "reponse_brute_sha256": sha_rep, "coupe_a_B_a": coupe}
    if tr is not None:
        conditions = PR.conditions_du_temoin(temoin, sha_texte, p["reglages"], apres)
        temoin["conditions"] = conditions
        temoin["conforme"] = all(conditions.values())
    else:
        temoin["conforme"] = None
    sha_tem = K.ecrire_scelle_json(os.path.join(dossier_appel, "temoin-isolement.json"), temoin)
    if temoin["conforme"] is False:
        raise K.Arret(f"{nom} : témoin d'isolement non conforme ({sorted(k for k, v in temoin['conditions'].items() if not v)})")
    if etat in ("complet", "tronque") and temoin["conforme"] is not True:
        raise K.Arret(f"{nom} : réponse rendue sans témoin d'isolement")
    cause = derniere.get("cause")
    panne = (not coupe) and code in PR.CODES_PANNE
    abandon = panne or ((not coupe) and cause in PR.CAUSES_ABANDON)
    r = {"proposeur": nom, "etat": etat, "code": code, "cause": cause, "cout_usd": float(derniere.get("cout_usd") or 0.0),
         "jetons": derniere.get("jetons"), "raison_arret": derniere.get("raison_arret"),
         "modele_servi": derniere.get("modele_servi"), "erreur": derniere.get("erreur"), "duree_s": duree,
         "reponse_brute_sha256": sha_rep, "temoin_sha256": sha_tem, "corps_relais_sha256": brut_sha,
         "texte_servi_sha256": sha_texte, "panne": panne, "abandon": abandon, "coupe_a_B_a": coupe,
         "texte": derniere.get("texte") if etat != "echec" else None}
    if cause in PR.CAUSES_ARRET:
        raise K.Arret(f"{nom} : coût lu {r['cout_usd']} USD au-dessus du pire cas de l'appel : arrêt (code 3)", appel=dict(r, texte=None))
    return r


def exiger_part(depense, p, nom):
    """Ligne d'arrêt « dépense d'un fournisseur atteignant sa part » : la part (20 × plafond de session) serait atteinte au pire
    cas de l'appel suivant → arrêt ; jamais de ligne d'extension."""
    part = K.N_MONDES * p["plafond_session_usd"]
    if depense + p["plafond_session_usd"] > part + 1e-9:
        raise K.Arret(f"{nom} : la part {part:.2f} USD serait atteinte au pire cas de l'appel suivant : arrêt")
    return part


def exiger_gabarit(P):
    """Ligne d'arrêt « empreinte différente : … gabarit » : le gabarit servi est celui du pilote (`e77d3041…`), inchangé."""
    if P.gabarit_sha256() != K.GABARIT_SHA256:
        raise K.Refus("gabarit servi ≠ e77d3041… (gabarit du pilote, inchangé) : arrêt avant tout appel")


def exiger_pieces_de_l_appel(dossier_appel, nom):
    """Ligne d'arrêt « réponse brute ou témoin d'isolement absent » : arrêt (code 3), pièces versées."""
    for f in ("reponse-brute.json", "temoin-isolement.json"):
        c = os.path.join(dossier_appel, f)
        if not os.path.isfile(c) or not K.compagnon_egal(c):
            raise K.Arret(f"{nom} : {f} absent ou différent de son compagnon : arrêt (code 3)")


def journaliser_coupure(chemin, ligne):
    """Ligne d'arrêt « appel plus long que B_a » : la coupure est écrite et relue ; sans trace, arrêt."""
    try:
        with open(chemin, "a", encoding="utf-8") as f:
            f.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")
        with open(chemin, encoding="utf-8") as f:
            lu = [json.loads(x) for x in f if x.strip()]
    except (OSError, ValueError) as e:
        raise K.Arret(f"coupure à B_a sans trace dans le journal ({type(e).__name__}) : arrêt") from None
    if ligne not in lu:
        raise K.Arret("coupure à B_a sans trace dans le journal : arrêt")


# --- règle d'abandon et minimum encore possible ----------------------------------------------------------------------------------

class Etat:
    """État partagé des files (sous verrou) : appels, cartes, dépenses, abandons, arrêt."""

    def __init__(self, conf):
        self.verrou = threading.Lock()
        self.conf = conf
        self.f_de = {n: f for f, ns in fournisseurs(conf).items() for n in ns}
        self.appels, self.cartes, self.gardien = [], [], []
        self.depense = {n: 0.0 for n in K.PROPOSEURS}
        self.abandonnes = {}          # fournisseur → cause
        self.repondus_f = {f: 0 for f in fournisseurs(conf)}
        self.resultat = {}            # (monde, nom) → « repondu » | « non_repondu »
        self.arret, self.arret_classe = None, None

    def peut_encore_etre_complet(self, w):
        def moitie(props):
            if any(self.resultat.get((w, p)) == "repondu" for p in props):
                return True
            return any((w, p) not in self.resultat and self.f_de[p] not in self.abandonnes for p in props)
        return moitie(K.MOITIE_B) and moitie(K.MOITIE_E)

    def minimum_possible(self):
        return sum(1 for w in K.MONDES if self.peut_encore_etre_complet(w)) >= K.MIN_COMPLETS


def repondu_au_lanceur(r, cartes):
    """« Répondu » vu du lanceur : complet avec au moins une carte admise au gardien, emplacement ≤ 6 (l'évaluabilité, qui
    demande l'oracle, est jugée par la mesure)."""
    return r["etat"] == "complet" and any(c["etat"] == "admise" and c["emplacement"] <= K.CARTES_MAX for c in cartes)


def traiter_resultat(E, w, nom, ligne, r, cs, info):
    """Sous le verrou : dépense, cartes, règle d'abandon (fournisseur), arrêt si le fournisseur n'a encore aucun appel répondu
    ou si le minimum de mondes complets n'est plus possible."""
    E.depense[nom] += r["cout_usd"]
    E.cartes += cs
    E.gardien.append({"monde": w, "proposeur": nom, "lecture": info})
    E.appels.append(dict(ligne, appele=True, **{k: v for k, v in r.items() if k not in ("texte", "proposeur")}))
    f = E.f_de[nom]
    rep = repondu_au_lanceur(r, cs)
    E.resultat[(w, nom)] = "repondu" if rep else "non_repondu"
    if rep:
        E.repondus_f[f] += 1
    if r["abandon"] and f not in E.abandonnes:
        E.abandonnes[f] = f"monde {w}, {nom} : code {r['code']}, cause {r['cause']}"
        if E.repondus_f[f] == 0:
            E.arret = f"fournisseur {f} abandonné sans aucun appel répondu (perdu en entier) : arrêt du crible"
            E.arret_classe = "fournisseur_abandonne"
        elif not E.minimum_possible():
            E.arret = f"fournisseur {f} abandonné : le minimum de {K.MIN_COMPLETS} mondes complets n'est plus possible"
            E.arret_classe = "fournisseur_abandonne"


# --- relais ----------------------------------------------------------------------------------------------------------------------

def lancer_les_relais(A, conf, files, mode, sortie, jeton, scen, procs, environ=None):
    """4 M relais : pour la file k, ses quatre relais aux ports décalés, plafond = (mondes de la file) × plafond de session,
    nombre d'appels = mondes de la file ; état de chacun contrôlé champ par champ (B-2 du pilote)."""
    PR = A.PR
    etats = {}
    for k, mondes_k in enumerate(files):
        ck = conf_de_la_file(conf, k)
        n = len(mondes_k)
        plafonds = {nom: n * ck["proposeurs"][nom]["plafond_session_usd"] for nom in K.PROPOSEURS}
        for nom in K.PROPOSEURS:
            journal = os.path.join(sortie, f"journal-relais-f{k}-{nom}.jsonl")
            appelant = ck["proposeurs"][nom]["dialecte"] if mode == "reel" else "factice:" + scen.get((k, nom), SCENARIO_A_BLANC)
            procs[(k, nom)], _ = PR.lancer_relais(ck, nom, journal, appelant, jeton, python=sys.executable, environ=environ,
                                                  plafond=plafonds[nom], max_appels=n)
        etats[str(k)] = PR.exiger_relais_prets(ck, mode, plafonds=plafonds, max_appels=n)
    return etats


def arreter_les_relais(A, procs):
    for proc in procs.values():
        A.PR.arreter_relais(proc)


def dollars_depuis_les_journaux(E, files, sortie, conf):
    """Dollars de chaque appel tels que les journaux des relais les donnent (coût au prix de la configuration), rattachés au
    monde par l'empreinte de la consigne reçue ; un appel coupé à B_a sans ligne : plafond de session ; non lancé : 0."""
    lignes = {}
    for k, _ in enumerate(files):
        for nom in K.PROPOSEURS:
            j = os.path.join(sortie, f"journal-relais-f{k}-{nom}.jsonl")
            if os.path.isfile(j):
                with open(j, encoding="utf-8") as f:
                    for x in f:
                        if x.strip():
                            o = json.loads(x)
                            lignes.setdefault((nom, o.get("consigne_recue_sha256")), []).append(o)
    out = []
    par = {(a["monde"], a["proposeur"]): a for a in E.appels}
    for w in K.MONDES:
        for nom in K.PROPOSEURS:
            a = par.get((w, nom))
            if a is None or not a.get("appele"):
                out.append({"monde": w, "proposeur": nom, "cout_config_usd": 0.0, "source": "non_lance"})
                continue
            j = lignes.get((nom, a.get("texte_servi_sha256")), [])
            if j:
                out.append({"monde": w, "proposeur": nom, "cout_config_usd": round(sum(x["cout_usd"] for x in j), 8),
                            "source": "journal_relais"})
            elif a.get("coupe_a_B_a"):
                out.append({"monde": w, "proposeur": nom, "source": "plafond_coupure",
                            "cout_config_usd": float(conf["proposeurs"][nom]["plafond_session_usd"])})
            else:
                out.append({"monde": w, "proposeur": nom, "cout_config_usd": float(a.get("cout_usd") or 0.0), "source": "journal_relais"})
    return {"version": "dollars-crible-v-v1", "appels": out}


# --- mode réel ------------------------------------------------------------------------------------------------------------------

def lire_go_du_crible(A, registre, go_kv1, go_kv2, aujourd_hui=None):
    """Les deux lignes κv1 (crédits de Claude) et κv2 (hors crédits), lues par le lecteur v66 au montant exact ; identifiants
    distincts ; périmètre contenant les mots de la ligne proposée."""
    try:
        return A.PR.lire_go_de_lignes(K.GO_CRIBLE, registre, {"kv1": go_kv1, "kv2": go_kv2}, aujourd_hui)
    except A.P.Refus as e:
        raise K.Refus(f"lignes de GO du crible : {e}") from None


def exiger_releve_sonde(A, conf, chemin, files):
    """Ligne d'arrêt « relevé de sonde absent, invalide ou d'un autre code » : contrôles du module de la sonde v74 (faits relus
    des pièces, conclusions recalculées), sous le code du crible (empreintes) et la configuration v12 ; le relevé dit le chemin des
    relais du crible (lanceur, ports de la file 0) ; refus avant tout dossier."""
    attendu = {"configuration_sha256": A.PR.empreinte_configuration(conf), "code_sha256": empreintes_du_code(A)}
    try:
        sha = A.S.exiger_releve(conf, chemin, attendu)
    except A.P.Refus as e:
        raise K.Refus(f"relevé de la sonde : {e}") from None
    with open(chemin, encoding="utf-8") as f:
        r = json.load(f)
    c = r.get("crible") or {}
    if c.get("lanceur") != VERSION or c.get("ports") != {n: conf["proposeurs"][n]["port"] for n in K.PROPOSEURS}:
        raise K.Refus("relevé de la sonde : fait par un autre lanceur ou sur un autre chemin de relais que celui du crible")
    return sha


def exiger_mode_reel(A, args, conf):
    """Gardes du mode réel, avant toute préparation, tout dossier et tout relais."""
    manquants = [o for o in ("go_kv1", "go_kv2", "registre_go", "texte", "texte_sha256", "mondes_shas", "registre_lancements",
                             "releve_sonde", "addendum", "addendum_sha256", "echeance_utc_s", "duree_d_s")
                 if getattr(args, o, None) in (None, "")]
    if manquants:
        raise K.Refus(f"mode réel : options exigées absentes : {manquants}")
    a_blanc = [o for o in CHAMPS_A_BLANC if getattr(args, o, None) not in (None, "", 0)]
    if a_blanc:
        raise K.Refus(f"mode réel : options de l'essai à blanc refusées : {a_blanc}")
    import numpy as np
    if np.__version__ != conf["numpy_exige"]:
        raise K.Refus(f"mode réel : numpy {np.__version__} ≠ {conf['numpy_exige']}")
    if K.sha256_fichier(args.texte) != args.texte_sha256:
        raise K.Refus("texte scellé : empreinte différente")
    exiger_addendum(args.addendum, args.addendum_sha256)
    exiger_m_de_la_regle(args.files, args.duree_d_s)
    garde = exiger_garde_de_depart(args.echeance_utc_s, args.files, args.duree_d_s)
    releve_sha = exiger_releve_sonde(A, conf, args.releve_sonde, args.files)
    go = lire_go_du_crible(A, args.registre_go, args.go_kv1, args.go_kv2)
    A.P.lire_engagement(args.mondes, args.mondes_sha256, args.texte_sha256)
    lire_engagement_crible(A, args.mondes, args.mondes_sha256, args.certifiees_sha256)
    A.P.exiger_hors_depot(args.registre_lancements, "registre des lancements")
    if os.path.exists(args.registre_lancements):
        with open(args.registre_lancements, encoding="utf-8") as f:
            if any(json.loads(x).get("texte_sha256") == args.texte_sha256 for x in f if x.strip()):
                raise K.Refus("mode réel : un lancement réel a déjà eu lieu pour ce texte (tout second lancement est un nœud)")
    return go, releve_sha, garde


def lire_engagement_crible(A, chemin_mondes, sha_mondes, sha_certifiees):
    """L'engagement du crible lie aussi le fichier des étiquettes C8 (empreinte) au fichier des mondes."""
    c = chemin_mondes + ".certifiees.engagement.json"
    A.P.exiger_hors_depot(c, "engagement des étiquettes C8")
    try:
        with open(c, encoding="utf-8") as f:
            e = json.load(f)
    except (OSError, ValueError):
        raise K.Refus("engagement des étiquettes C8 absent ou illisible") from None
    if e.get("fichier_mondes_sha256") != sha_mondes or e.get("certifiees_sha256") != sha_certifiees:
        raise K.Refus("engagement des étiquettes C8 : fichier des mondes ou des étiquettes différent")
    return e


def exiger_certifiees(A, chemin, sha, mondes):
    A.P.exiger_hors_depot(chemin, "fichier des étiquettes C8")
    if not os.path.isfile(chemin) or K.sha256_fichier(chemin) != sha:
        raise K.Refus("fichier des étiquettes C8 absent ou d'empreinte différente")
    with open(chemin, encoding="utf-8") as f:
        d = json.load(f)
    if d.get("version") != "certifiees-crible-v-v1" or sorted(d.get("mondes", {})) != sorted(str(w["monde"]) for w in mondes) \
            or any(d["mondes"][str(w["monde"])].get("spec_sha256") != w["spec_sha256"] for w in mondes):
        raise K.Refus("fichier des étiquettes C8 : mondes différents de ceux du fichier des mondes")
    return d


# --- jouer -----------------------------------------------------------------------------------------------------------------------

def jouer(args, crochets=None):
    """L'essai à blanc ou le crible réel. `crochets` (essais du développeur, mode à blanc seulement) : {"executer": f(monde, nom)
    → exécuteur ou None, "apres_appel": f(monde, nom, dossier), "corps": f(monde, corps_par_proposeur)}."""
    crochets = crochets or {}
    debut = maintenant()
    A = charger_arbre(args.arbre)
    P, PR = A.P, A.PR
    conf = lire_configuration_v12(A, getattr(args, "configuration", None))
    go, releve_sha, garde, sans_reflexion = None, None, None, []
    if args.mode == "reel":
        if crochets:
            raise K.Refus("mode réel : aucun crochet d'essai")
        go, releve_sha, garde = exiger_mode_reel(A, args, conf)
        sans_reflexion = A.S.proposeurs_sans_reflexion(args.releve_sonde)
    elif args.mode == "a_blanc":
        if args.echeance_utc_s is not None:
            garde = exiger_garde_de_depart(args.echeance_utc_s, args.files, args.duree_d_s)
    else:
        raise K.Refus("mode : a_blanc ou reel")
    if os.path.exists(args.sortie):
        raise K.Refus("dossier de sortie existant")
    files = repartir_en_files(args.files)
    borne = K.B_A_S if args.mode == "reel" or not args.borne_essai_s else float(args.borne_essai_s)
    decalage = 0 if args.mode == "reel" else int(args.decalage_ports or 0)
    if decalage:
        conf = copy.deepcopy(conf)
        for p in conf["proposeurs"].values():
            p["port"] += decalage
    shas = args.mondes_shas.split(",") if args.mondes_shas else None
    mondes, pm_, servis, controles, prives = preparer_les_mondes(A, args.mondes, args.mondes_sha256, conf["octets_entree_max"], shas)
    certif = exiger_certifiees(A, args.certifiees, args.certifiees_sha256, mondes)
    os.makedirs(args.sortie)
    prive = os.path.join(args.sortie, "prive")
    os.makedirs(prive, mode=0o700)
    for w, s in servis.items():  # textes servis gardés sur la machine pour l'audit R4, jamais rapatriés
        with open(os.path.join(prive, f"texte-servi-monde-{w}.txt"), "x", encoding="utf-8") as f:
            f.write(s["texte"])
    K.ecrire_scelle_json(os.path.join(prive, "controles-prives.json"), prives)
    scen = {}
    for x in (args.scenarios or "").split(","):
        if x:
            nom, s = x.split("=", 1)
            for k in range(len(files)):
                scen[(k, nom)] = s
    lents = {(int(x.split(":")[0]), x.split(":")[1]) for x in (args.lent or "").split(",") if x}
    E = Etat(conf)
    jeton = PR.nouveau_jeton()
    coupures = os.path.join(args.sortie, NOMS["coupures"])
    procs, relais = {}, None
    boucle_locale = any(PR.amont_boucle_locale(conf["proposeurs"][n]["url_amont"]) for n in K.PROPOSEURS)
    mode = "reel_sur_doublure" if args.mode == "reel" and boucle_locale else args.mode

    def executeur(w, nom):
        f = crochets.get("executer")
        e = f(w, nom) if f else None
        if e is not None:
            return e
        if (w, nom) in lents:
            def lent(cmd, timeout=None, **kw):  # essai : la commande dort au-delà de la borne (coupure simulée réelle)
                return subprocess.run(["sleep", str(float(timeout) + 30)], timeout=timeout, capture_output=True, text=True)
            return lent
        return subprocess.run

    def jouer_un_appel(k, w, nom, corps, ligne):
        ck = conf_de_la_file(conf, k)
        dossier = os.path.join(args.sortie, f"monde-{w}", nom)
        r = appeler_borne(A, ck, nom, corps["texte"], dossier, jeton, sys.executable, borne, executeur(w, nom))
        if crochets.get("apres_appel"):
            crochets["apres_appel"](w, nom, dossier)
        exiger_pieces_de_l_appel(dossier, nom)
        if r["texte_servi_sha256"] != corps["texte_sha256"]:  # la session n'a reçu que le corps préparé du monde, rien d'autre
            raise K.Arret(f"{nom} : texte servi ≠ corps préparé du monde {w} : arrêt (code 3)", appel=dict(r, texte=None))
        if r["coupe_a_B_a"]:
            journaliser_coupure(coupures, {"monde": w, "proposeur": nom, "borne_s": borne, "duree_s": r["duree_s"],
                                           "etat": "echec", "reprise": False})
        A.L74.garder_reflexion_absente(ck, nom, dossier, r, sans_reflexion)
        return r

    def file(k, mondes_k):
        for w in mondes_k:
            with E.verrou:
                if E.arret:
                    return
            s = servis[w]
            corps = {nom: corps_de_l_appel(A, s, P.gabarit_sha256()) for nom in K.PROPOSEURS}
            if crochets.get("corps"):
                crochets["corps"](w, corps)
            exiger_corps_egaux(corps, s)
            lancer, lignes = [], {}
            with E.verrou:
                for nom in K.PROPOSEURS:
                    p = conf["proposeurs"][nom]
                    ligne = {"monde": w, "proposeur": nom, "file": k, "texte_servi_sha256": corps[nom]["texte_sha256"],
                             "archive_sha256": corps[nom]["archive_sha256"], "episodes_sha256": corps[nom]["episodes_sha256"],
                             "gabarit_sha256": corps[nom]["gabarit_sha256"]}
                    f = E.f_de[nom]
                    if f in E.abandonnes:
                        E.appels.append(dict(ligne, etat="echec", appele=False, cause=f"fournisseur abandonné ({E.abandonnes[f]})"))
                        E.resultat[(w, nom)] = "non_repondu"
                        continue
                    exiger_part(E.depense[nom], p, nom)
                    lancer.append(nom)
                    lignes[nom] = ligne
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
                futurs = {nom: ex.submit(jouer_un_appel, k, w, nom, corps[nom], lignes[nom]) for nom in lancer}
                erreurs, rendus = [], {}
                for nom in lancer:
                    try:
                        r = futurs[nom].result()
                    except Exception as e:  # noqa: BLE001 — après le départ des appels, tout est un arrêt (code 3)
                        erreurs.append((nom, e))
                        continue
                    cs, info = ([], None) if r["etat"] == "echec" else P.cartes_d_un_appel(w, nom, r["texte"])
                    rendus[nom] = (r, cs, info)
                for nom in sorted(rendus, key=lambda n: not repondu_au_lanceur(rendus[n][0], rendus[n][1])):  # répondus d'abord
                    r, cs, info = rendus[nom]
                    with E.verrou:
                        traiter_resultat(E, w, nom, lignes[nom], r, cs, info)
            if erreurs:
                with E.verrou:
                    for nom, e in erreurs:
                        a = getattr(e, "appel", None)
                        if a is not None:
                            E.depense[nom] += a["cout_usd"]
                            E.appels.append(dict(lignes[nom], appele=True, arret=True,
                                                 **{x: v for x, v in a.items() if x not in ("texte", "proposeur")}))
                        else:  # appel parti, pièces ou garde en défaut : porté au relevé, sa dépense lue au journal du relais
                            E.appels.append(dict(lignes[nom], appele=True, arret=True, etat="echec", cause=type(e).__name__))
                    if not E.arret:
                        E.arret = f"{type(erreurs[0][1]).__name__} : {erreurs[0][1]}"
                        E.arret_classe = "arret"
                return

    erreur_imprevue = None
    try:
        relais = lancer_les_relais(A, conf, files, args.mode, args.sortie, jeton, scen, procs)
        with open(os.path.join(args.sortie, "pids-relais.json"), "x", encoding="utf-8") as f:  # arrêt par PID (R10) après un feu d'arrêt
            json.dump(sorted(p.pid for p in procs.values()), f)
        if args.mode == "reel":  # le lancement réel est consigné quand les relais sont prêts, avant le premier appel
            with open(args.registre_lancements, "a", encoding="utf-8") as f:
                f.write(json.dumps({"texte_sha256": args.texte_sha256, "debut_utc": debut, "sortie": os.path.abspath(args.sortie),
                                    "lanceur": VERSION}) + "\n")
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(files)) as ex:
            def file_gardee(k, mk):
                try:
                    file(k, mk)
                except Exception as e:  # noqa: BLE001 — l'arrêt d'une file arrête aussitôt l'autre (aucune dépense de plus)
                    with E.verrou:
                        if not E.arret:
                            E.arret, E.arret_classe = f"{type(e).__name__} : {e}", "arret"
                    raise

            fs = [ex.submit(file_gardee, k, mk) for k, mk in enumerate(files)]
            for fu in fs:
                try:
                    fu.result()
                except (K.Arret, PR.ArretPilote, K.Refus) as e:
                    with E.verrou:
                        if not E.arret:
                            E.arret, E.arret_classe = f"{type(e).__name__} : {e}", "arret"
    except (K.Refus, P.Refus) as e:
        if not E.appels:
            arreter_les_relais(A, procs)
            raise K.Refus(str(e)) from None
        E.arret, E.arret_classe = f"{type(e).__name__} : {e}", "arret"
    except Exception as e:  # noqa: BLE001 — tout arrêt imprévu laisse relevé et manifeste partiels
        erreur_imprevue = e
        E.arret, E.arret_classe = f"{type(e).__name__} : {e}", "arret"
    finally:
        arreter_les_relais(A, procs)
    # appels non joués après un arrêt : comptés « échec », non lancés (aucune dépense de plus)
    faits = {(a["monde"], a["proposeur"]) for a in E.appels}
    for w in K.MONDES:
        for nom in K.PROPOSEURS:
            if (w, nom) not in faits:
                E.appels.append({"monde": w, "proposeur": nom, "etat": "echec", "appele": False,
                                 "cause": "non joué (crible arrêté)" if E.arret else "non joué"})
    E.appels.sort(key=lambda a: (a["monde"], K.PROPOSEURS.index(a["proposeur"])))
    export = {"cartes": E.cartes, "appels": [{"monde": a["monde"], "proposeur": a["proposeur"], "etat": a["etat"]} for a in E.appels]}
    nom_cartes = NOMS["cartes"] if E.arret is None or E.arret_classe == "fournisseur_abandonne" else NOMS["partiel"]
    sha_cartes = K.ecrire_scelle_json(os.path.join(args.sortie, nom_cartes), export)
    dollars = dollars_depuis_les_journaux(E, files, args.sortie, conf)
    sha_dollars = K.ecrire_scelle_json(os.path.join(args.sortie, NOMS["dollars"]), dollars)
    releve = {"version": VERSION, "mode": mode, "partiel": E.arret is not None, "arret": E.arret, "arret_classe": E.arret_classe,
              "appels": E.appels, "gardien": E.gardien, "depense_usd": E.depense, "abandonnes": E.abandonnes,
              "cartes_sha256": sha_cartes, "dollars_sha256": sha_dollars, "borne_par_appel_s": borne, "files": files,
              "coupures": sum(1 for a in E.appels if a.get("coupe_a_B_a")),
              "comptes": {e: sum(1 for a in E.appels if a["etat"] == e) for e in ("complet", "tronque", "echec")}}
    sha_releve = K.ecrire_scelle_json(os.path.join(args.sortie, NOMS["releve"]), releve)
    manifeste = {"version": VERSION, "mode": mode, "debut_utc": debut, "fin_utc": maintenant(), "partiel": E.arret is not None,
                 "arret": E.arret, "arret_classe": E.arret_classe, "controles": controles,
                 "configuration_sha256": PR.empreinte_configuration(conf), "configuration_fichier_sha256": CONFIG_V12_SHA256,
                 "code_sha256": empreintes_du_code(A), "environnement_de_calcul": environnement_de_calcul(A),
                 "relais": relais, "go": go, "releve_sonde_sha256": releve_sha, "proposeurs_sans_reflexion": sans_reflexion,
                 "garde_de_depart": garde, "files": files, "M": args.files, "borne_par_appel_s": borne,
                 "certifiees_sha256": args.certifiees_sha256, "texte_sha256": args.texte_sha256,
                 "releve_sha256": sha_releve, "cartes_sha256": sha_cartes, "cartes_fichier": nom_cartes, "dollars_sha256": sha_dollars,
                 "amont_boucle_locale": boucle_locale, "juge": None, "tests_de_mort": None, "experimentateur": None}
    P.exiger_manifeste_sans_loi({k: v for k, v in manifeste.items() if k not in ("go",)})
    sha_man = K.ecrire_scelle_json(os.path.join(args.sortie, NOMS["manifeste"]), manifeste)
    imprimer({"lanceur": VERSION, "mode": mode, "cartes_sha256": sha_cartes, "releve_sha256": sha_releve, "manifeste_sha256": sha_man,
              "comptes": releve["comptes"], "coupures": releve["coupures"], "abandonnes": E.abandonnes, "arret": E.arret,
              "arret_classe": E.arret_classe})
    if erreur_imprevue is not None:
        print(f"arrêt imprévu : {type(erreur_imprevue).__name__} : {erreur_imprevue}", file=sys.stderr)
    if E.arret is not None:
        print(f"arrêt : {E.arret}", file=sys.stderr)
        return 3
    return 0


def environnement_de_calcul(A):
    import numpy as np
    return {"python": platform.python_version(), "numpy": np.__version__, "plate_forme": platform.platform(),
            "arbre": A.L74.commit_de_l_arbre(), "regle_des_graines": (
                "mondes : graine_monde_crible (étiquette crible-v-v1, r = 1 à 20) ; épisodes : " + K.ETIQUETTE_EPISODES +
                " ; oracle : cle(oracle-crible-v, empreinte du devis) ; jeu public : SeedSequence(entropy=racine, spawn_key=(r, 30)) ;"
                " rééchantillonnage : (99, b) ; jeton des relais : secrets.token_hex(16)")}


# --- sonde neuve du chemin des relais du crible ------------------------------------------------------------------------------------

def sonde(args):
    """Sonde neuve (exigée, R-2992) : les quatre relais lancés par le lanceur du crible (ports de la file 0, plafond = part de la
    sonde de la configuration), deux appels par relais (consignes de la section « sonde » de la v12 : borne gelée, puis borne
    courte), faits tirés des pièces par le module de la sonde v74, relevé scellé sous le code du crible. Mode réel : lignes κv1 et
    κv2 au montant exact, registre des lancements de la sonde (une seule exécution) ; payante, jamais jouée par le développeur."""
    debut = maintenant()
    A = charger_arbre(args.arbre)
    P, PR, S = A.P, A.PR, A.S
    conf = lire_configuration_v12(A)
    if os.path.exists(args.sortie):
        raise K.Refus("sonde : dossier de sortie existant")
    go, reprise = None, None
    if args.mode == "reel":
        go = lire_go_du_crible(A, args.registre_go, args.go_kv1, args.go_kv2)
        ident = [args.go_kv1 + "#sonde-crible-v", args.go_kv2 + "#sonde-crible-v"]
        try:
            reprise = S.exiger_premier_lancement(args.registre_lancements, ident, None, None)
        except P.Refus as e:
            raise K.Refus(str(e)) from None
    elif args.mode != "a_blanc":
        raise K.Refus("mode : a_blanc ou reel")
    decalage = 0 if args.mode == "reel" else int(args.decalage_ports or 0)
    if decalage:
        conf = copy.deepcopy(conf)
        for p in conf["proposeurs"].values():
            p["port"] += decalage
    s = conf["sonde"]
    parts = PR.parts_de_la_sonde(conf)
    os.makedirs(args.sortie)
    jeton = PR.nouveau_jeton()
    procs, faits, relais, arret, en_cours, partis = {}, [], None, None, None, False
    try:
        for nom in K.PROPOSEURS:
            p = conf["proposeurs"][nom]
            appelant = p["dialecte"] if args.mode == "reel" else "factice:k1_plus"
            procs[nom], _ = PR.lancer_relais(conf, nom, os.path.join(args.sortie, f"journal-relais-{nom}.jsonl"), appelant,
                                             jeton, python=sys.executable, plafond=parts[nom], max_appels=len(S.APPELS))
        relais = PR.exiger_relais_prets(conf, args.mode, plafonds=parts, max_appels=len(S.APPELS))
        if args.mode == "reel":
            S.consigner_lancement(args.registre_lancements, ident, args.sortie, debut, reprise)
        for nom in K.PROPOSEURS:
            p = conf["proposeurs"][nom]
            for quoi in S.APPELS:
                b = None if quoi == "borne_gelee" else s["borne_courte_jetons"]
                en_cours, partis = (nom, quoi), True
                PR.appeler(conf, nom, s["consignes"][quoi], S.dossier_d_un_appel(args.sortie, nom, quoi), jeton,
                           python=sys.executable, borne=b)
                faits.append(S.faits_depuis_les_pieces(conf, nom, quoi, args.sortie))
                en_cours = None
    except (PR.ArretPilote, Exception) as e:  # noqa: BLE001
        arret = f"{type(e).__name__} : {e}"
        if en_cours is not None and os.path.isfile(os.path.join(S.dossier_d_un_appel(args.sortie, *en_cours), "reponse-brute.json")):
            try:
                faits.append(S.faits_depuis_les_pieces(conf, en_cours[0], en_cours[1], args.sortie))
            except (P.Refus, KeyError, TypeError, ValueError, OSError) as e2:
                arret += f" ; pièces de l'appel en cours illisibles : {e2}"
        if isinstance(e, P.Refus) and not partis:
            arreter_les_relais(A, procs)
            raise K.Refus(str(e)) from None
    finally:
        arreter_les_relais(A, procs)
    extra = {"lanceur": VERSION, "configuration_sha256": PR.empreinte_configuration(conf), "code_sha256": empreintes_du_code(A),
             "go": go, "reprise": reprise, "relais": relais, "parts_usd": parts,
             "crible": {"lanceur": VERSION, "ports": {n: conf["proposeurs"][n]["port"] for n in K.PROPOSEURS}, "file": 0,
                        "mode": args.mode},
             "consignes_sha256": {k: hashlib.sha256(v.encode("utf-8")).hexdigest() for k, v in s["consignes"].items()},
             "depense_usd": round(sum(f.get("cout_usd") or 0.0 for f in faits), 8),
             "a_lire_hors_du_code": "coût de chaque appel à rapprocher de la console par Lazar"}
    rel = S.releve(conf, faits, True, debut, maintenant(), arret is not None, arret, extra)
    sha = K.ecrire_scelle_json(os.path.join(args.sortie, NOMS["releve_sonde"]), rel)
    imprimer({"lanceur": VERSION, "releve_sonde_sha256": sha, "partiel": arret is not None, "arret": arret,
              "depense_usd": extra["depense_usd"]})
    return 3 if arret is not None else 0


# --- mesure (une seule fois), lecture, rapatriement --------------------------------------------------------------------------------

def mesurer(args):
    """La mesure **une seule fois** : CARTES.json et DOLLARS.json égaux à leurs compagnons et au manifeste, manifeste égal au
    sien, relevé non partiel (ou partiel par la seule règle d'abandon, lu « non concluant ») ; mondes et étiquettes du manifeste ;
    aucune sortie de mesure déjà présente ; programme lancé sans copie ; pièce de liaison scellée."""
    A = charger_arbre(args.arbre)
    d = args.sortie
    man_f = os.path.join(d, NOMS["manifeste"])
    man = K.lire_json_scelle(man_f, "manifeste")
    cartes = os.path.join(d, man.get("cartes_fichier") or "")
    dol = os.path.join(d, NOMS["dollars"])
    if man.get("partiel") and man.get("arret_classe") != "fournisseur_abandonne":
        raise K.Refus("mesure : relevé partiel (arrêt) : aucune mesure")
    if not os.path.isfile(cartes) or not K.compagnon_egal(cartes) or K.sha256_fichier(cartes) != man.get("cartes_sha256") \
            or not K.compagnon_egal(dol) or K.sha256_fichier(dol) != man.get("dollars_sha256"):
        raise K.Refus("mesure : CARTES.json ou DOLLARS.json ≠ leurs compagnons ou le manifeste")
    if args.mondes_sha256 != ((man.get("controles") or {}).get("mondes") or {}).get("fichier_mondes_sha256") \
            or args.certifiees_sha256 != man.get("certifiees_sha256"):
        raise K.Refus("mesure : fichier des mondes ou des étiquettes ≠ celui du manifeste")
    deja = [n for n in os.listdir(d) if n.startswith("sortie-mesure") or n.startswith("sortie-fictive") or n == NOMS["piece"]]
    if deja:
        raise K.Refus(f"mesure : déjà lancée dans ce dossier ({deja}) : une seule fois (seconde mesure refusée, run invalide)")
    if (man.get("code_sha256") or {}).get("crible/mesure_crible_v_v1.py") != K.sha256_fichier(PROGRAMME_MESURE):
        raise K.Refus("mesure : programme ≠ celui du manifeste")
    charger_mondes(A, args.mondes, args.mondes_sha256)
    if K.sha256_fichier(args.certifiees) != args.certifiees_sha256:
        raise K.Refus("mesure : étiquettes C8 d'empreinte différente")
    sortie, fictive = os.path.join(d, NOMS["sortie"]), os.path.join(d, NOMS["fictive"])
    debut = maintenant()
    r = subprocess.run([sys.executable, "-I", "-B", PROGRAMME_MESURE, "mesurer", "--mr2", os.path.join(A.ORCH, "mr2_v68"),
                        "--texte-sha256", args.texte_sha256, "--mondes", args.mondes, "--certifiees", args.certifiees,
                        "--cartes", cartes, "--dollars", dol, "--configuration", A.CONF, "--sortie", sortie,
                        "--sortie-fictive", fictive], capture_output=True, text=True, encoding="utf-8",
                       env={"PATH": "/usr/bin:/bin", "OMP_NUM_THREADS": "2"})
    if r.returncode != 0 or not os.path.isfile(sortie) or not os.path.isfile(fictive):
        raise K.Arret(f"mesure : programme en erreur (code {r.returncode}) : {r.stderr[-400:]}")
    piece = {"version": VERSION, "debut_utc": debut, "fin_utc": maintenant(), "cartes_sha256": K.sha256_fichier(cartes),
             "dollars_sha256": K.sha256_fichier(dol), "programme_sha256": K.sha256_fichier(PROGRAMME_MESURE),
             "sortie": NOMS["sortie"], "sortie_sha256": K.sha256_fichier(sortie), "sortie_fictive_sha256": K.sha256_fichier(fictive),
             "manifeste_sha256": K.sha256_fichier(man_f), "fichier_mondes_sha256": args.mondes_sha256,
             "certifiees_sha256": args.certifiees_sha256}
    imprimer(dict(piece, piece_sha256=K.ecrire_scelle_json(os.path.join(d, NOMS["piece"]), piece)))
    return 0


def lire(args):
    r = subprocess.run([sys.executable, "-I", "-B", PROGRAMME_LECTURE, "--sortie", args.sortie, "--ecrire", args.ecrire],
                       capture_output=True, text=True, encoding="utf-8", env={"PATH": "/usr/bin:/bin"})
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    return r.returncode


PERMIS = re.compile(r"^(reponse-brute\.json|corps-relais\.json|temoin-isolement\.json|CARTES\.json|CARTES-partiel\.json|"
                    r"DOLLARS\.json|releve-crible-v-v1\.json|manifeste-crible-v-v1\.json|sortie-mesure-crible-v-v1\.json|"
                    r"sortie-fictive-crible-v-v1\.json|mesure-crible-v-v1\.json|lecture-crible-v-v1\.json|"
                    r"coupures-crible-v-v1\.jsonl|journal-relais-f[01]-[a-z0-9]+\.jsonl|releve-sonde-crible-v-v1\.json|"
                    r"journal-relais-[a-z0-9]+\.jsonl)(\.sha256)?$")


def rapatrier(args):
    """Copie des seules pièces permises ; refuse tout fichier qui porterait un monde, un texte servi, une graine, une loi compilée
    ou un identifiant de fournisseur (motifs de l'audit du pilote), et tout fichier différent de son compagnon : rien n'est copié
    alors ; jamais `prive/`."""
    A = charger_arbre(args.arbre)
    if os.path.exists(args.destination):
        raise K.Refus("rapatriement : destination existante")
    mondes = charger_mondes(A, args.mondes, args.mondes_sha256)
    lois = {hashlib.sha256(A.P.json_canonique(A.P.compiler_monde(w["spec"]))).hexdigest() for w in mondes}
    a_copier, laisses, refuses = [], [], []
    for racine, dossiers, fichiers in sorted(os.walk(args.source)):
        dossiers[:] = sorted(x for x in dossiers if x != "prive")
        for nom in sorted(fichiers):
            f = os.path.join(racine, nom)
            rel = os.path.relpath(f, args.source)
            if not PERMIS.match(nom):
                laisses.append(rel)
                continue
            m = None if nom.endswith(".sha256") else A.AU.motif_interdit(f, args.mondes_sha256, lois)
            (refuses.append([rel, m]) if m else a_copier.append(rel))
    if refuses:
        raise K.Refus(f"rapatriement : fichiers interdits, rien n'est rendu : {refuses[:5]}")
    copies = []
    for rel in a_copier:
        cible = os.path.join(args.destination, rel)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        shutil.copyfile(os.path.join(args.source, rel), cible)
        copies.append([rel, K.sha256_fichier(cible)])
    aucun = all(A.AU.motif_interdit(os.path.join(args.destination, r), args.mondes_sha256, lois) is None
                for r, _ in copies if not r.endswith(".sha256"))
    liste = {"version": VERSION, "copies": copies, "laisses": laisses, "aucun_monde": aucun}
    sha = K.ecrire_scelle_json(os.path.join(args.destination, "liste-rapatriement-crible-v-v1.json"), liste)
    imprimer({"copies": len(copies), "laisses": len(laisses), "aucun_monde": aucun, "liste_sha256": sha})
    return 0 if aucun else 3


# --- principal ------------------------------------------------------------------------------------------------------------------

def principal(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = a.add_subparsers(dest="commande", required=True)
    x = s.add_parser("secret")
    x.add_argument("chemin")
    x.add_argument("--arbre", required=True)
    x = s.add_parser("generer")
    for o in ("--arbre", "--secret", "--phrase-fichier", "--texte", "--texte-sha256", "--sortie"):
        x.add_argument(o, required=True)
    x.add_argument("--processus", type=int, default=1)
    x = s.add_parser("preparer")
    for o in ("--arbre", "--mondes", "--mondes-sha256"):
        x.add_argument(o, required=True)
    x = s.add_parser("sonde")
    for o in ("--arbre", "--mode", "--sortie"):
        x.add_argument(o, required=True)
    for o in ("--go-kv1", "--go-kv2", "--registre-go", "--registre-lancements", "--decalage-ports"):
        x.add_argument(o, default=None)
    x = s.add_parser("jouer")
    for o in ("--arbre", "--mode", "--mondes", "--mondes-sha256", "--certifiees", "--certifiees-sha256", "--sortie"):
        x.add_argument(o, required=True)
    x.add_argument("--files", type=int, required=True)
    for o in ("--go-kv1", "--go-kv2", "--registre-go", "--texte", "--texte-sha256", "--mondes-shas", "--registre-lancements",
              "--releve-sonde", "--addendum", "--addendum-sha256", "--scenarios", "--lent", "--configuration"):
        x.add_argument(o, default=None)
    x.add_argument("--echeance-utc-s", type=float, default=None)
    x.add_argument("--duree-d-s", type=float, default=None)
    x.add_argument("--borne-essai-s", type=float, default=None)
    x.add_argument("--decalage-ports", type=int, default=0)
    x = s.add_parser("mesurer")
    for o in ("--arbre", "--sortie", "--mondes", "--mondes-sha256", "--certifiees", "--certifiees-sha256", "--texte-sha256"):
        x.add_argument(o, required=True)
    x = s.add_parser("lire")
    x.add_argument("--sortie", required=True)
    x.add_argument("--ecrire", required=True)
    x = s.add_parser("rapatrier")
    for o in ("--source", "--destination", "--mondes", "--mondes-sha256", "--arbre"):
        x.add_argument(o, required=True)
    args = a.parse_args(argv)
    try:
        if args.commande == "secret":
            A = charger_arbre(args.arbre)
            imprimer({"secret_sha256": A.P.tirer_secret(args.chemin)})
        elif args.commande == "generer":
            A = charger_arbre(args.arbre)
            if K.sha256_fichier(args.texte) != args.texte_sha256:
                raise K.Refus("generer : texte ≠ son empreinte")
            secret = A.P.lire_secret(args.secret)
            with open(args.phrase_fichier, encoding="utf-8") as f:
                phrase = f.read().rstrip("\n")
            mondes, certif, ctl = generer_mondes(A, secret, phrase, args.texte_sha256, args.processus)
            blanche = [os.path.dirname(os.path.abspath(args.secret))]
            sha = A.P.ecrire_prive(args.sortie, mondes, blanche)
            A.P.ecrire_engagement(args.sortie, sha, mondes, args.texte_sha256, blanche)
            chemin_c = os.path.join(os.path.dirname(os.path.abspath(args.sortie)), "CERTIFIEES.json")
            sha_c = A.P.ecrire_prive(chemin_c, certif, blanche)
            A.P.ecrire_prive(args.sortie + ".certifiees.engagement.json",
                             {"version": VERSION, "fichier_mondes_sha256": sha, "certifiees_sha256": sha_c,
                              "texte_sha256": args.texte_sha256}, blanche)
            imprimer({"fichier_mondes_sha256": sha, "certifiees_sha256": sha_c, "controles": ctl})
        elif args.commande == "preparer":
            A = charger_arbre(args.arbre)
            conf = lire_configuration_v12(A)
            _, _, _, ctl, _ = preparer_les_mondes(A, args.mondes, args.mondes_sha256, conf["octets_entree_max"])
            imprimer(ctl)
        elif args.commande == "sonde":
            return sonde(args)
        elif args.commande == "jouer":
            return jouer(args)
        elif args.commande == "mesurer":
            return mesurer(args)
        elif args.commande == "lire":
            return lire(args)
        elif args.commande == "rapatrier":
            return rapatrier(args)
    except K.Refus as e:
        print(f"refus : {e}", file=sys.stderr)
        return 2
    except K.Arret as e:
        print(f"arrêt : {e}", file=sys.stderr)
        return 3
    except Exception as e:  # noqa: BLE001
        if type(e).__name__ == "Refus":  # Refus du cœur du pilote (pole.pilote_mr2_v70.Refus)
            print(f"refus : {e}", file=sys.stderr)
            return 2
        raise
    return 0


if __name__ == "__main__":
    sys.exit(principal())
