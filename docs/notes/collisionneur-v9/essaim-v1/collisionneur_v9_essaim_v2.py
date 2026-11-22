#!/usr/bin/env python3
"""Collisionneur v9, mode « essaim » (v2) : société de cinq modèles sous pseudonymes, à budget égal au mode isolé.

v2 (même développeur, 22 novembre 2026) : copie de la v1 (c2db738c…, inchangée, R12), corrigée selon la contre-lecture d'un
Opus neuf : B1 identifiants opaques et fil trié (cycle, genre, identifiant), B2 balises de bloc refusées dans les textes
d'agents et l'injection ; R1 noms de modèle refusés (réglable) ; R2 enveloppe sur l'étage III seul, réserves ; R3 borne de
dépassement dite ; R4 vérification du bloc QUESTION, des relecteurs de toute prépublication, de l'historique du programme ;
R5 garde des lettres ; R6 MOTIF_NOTE restreint ; R7 empreinte de la question dans la clé du dossier ; R8 revues perdues.

Pièce d'instrument (classe B), écrite par Opus 5.5 le 22 novembre 2026 d'après la conception de Fable
(docs/notes/demandes-fable-api-2026-11-22-v1/reponse-7/relecture-fable-api.md, partie 2, « Le mode essaim ») et la note de
branchement preparation-branchement-essaim-opus-v1.md (même dossier que ce script). À contre-lire par un autre Opus.

Le mode isolé (v8d) n'est pas copié : il est IMPORTÉ tel quel (empreinte contrôlée au chargement) et CHAQUE appel de
modèle passe par son `executer_cellule` (garde v3 des réglages de Google, comptage de l'entrée, plafond du dossier, ligne,
relances déclarées, zéro pensée = arrêt code 10, coupure comptée au pire, refus avant l'envoi). Aucun autre chemin d'envoi.
Les tours neufs sont ajoutés au dictionnaire TOURS du module importé, sans toucher aux tours existants.

Déroulé (Fable) :
  temps 0 : brouillon privé (consigne du tour III.1 du mode isolé, mot pour mot), empreinte journalisée ;
  temps 1 : N cycles fixes ; par cycle, un appel par agent dans un ordre tiré et scellé ; sections balisées : salon,
            prépublication (versionnée), revues attribuées, erratums (ajout seul), textes à ouvrir au cycle suivant ;
            deux relecteurs tirés parmi les non-auteurs pour chaque prépublication déposée, revues dues au cycle suivant ;
  temps 2 : réponse finale privée (limite du tour III.3 du mode isolé), sans voir les réponses finales des autres.
Budget : enveloppe et répartition lues dans la configuration (classe A) ; part par agent et par temps contrôlée sur le
coût MESURÉ avant chaque appel (part épuisée : tour sauté, journalisé) ; le plafond du dossier reste tenu par
`executer_cellule` sur le pire cas.

Commandes (PYTHONPATH=src) :
  devis      --configuration C --question Q [--enveloppe-usd X]   pire cas par temps et total, sans réseau
  lancer     --configuration C --question Q --sortie D --plafond-usd X --ligne-usd X --cle-anthropic NOM --cle-openai NOM
             [--faits F] [--erreurs-plantees F] [--accepter-absence CELLULE] [--reprise]
  enveloppe  DOSSIER_ISOLE        coût total mesuré d'un dossier du mode isolé (à reporter dans la configuration)
  bilan      DOSSIER              entrée, sortie, pensées, coût par agent et par temps ; publications ; sans lire les textes
  verifier   DOSSIER              recontrôle du dossier (celui de la v8d, plus celui de l'essaim), sans réseau
"""
import argparse
import hashlib
import importlib.util
import json
import math
import re
import sys
from pathlib import Path

import numpy as np

VERSION = "collisionneur-v9-essaim-v2"
ICI = Path(__file__).resolve().parent
SCRIPT_V8D = ICI.parent / "collisionneur_v9_v8d.py"
SHA_V8D = "b780383874598f12b24c79e4087d335c8e01cda685e295f5116898fa3b1715ac"

# Tours neufs : préfixes distincts de ceux de la v8d (E1-, E2-, E3-), deux chiffres pour les cycles (aucun préfixe commun).
TOUR_BROUILLON = "W0-T1"
TOUR_FINALE = "W2-T1"
PHASES = ("temps0", "temps1", "temps2")
USAGE_PSEUDONYMES, USAGE_ORDRE, USAGE_RELECTEURS = 0, 1, 2
TIERS = "tiers"
MARGE_LIGNE = 200          # caractères de cadre par ligne de la liste des nouveautés (borne du devis)
COUPE_LIGNE = 200          # titre et première ligne affichés au plus sur ce nombre de caractères chacun
CAR_PAR_MOT = 7            # borne large de la v8d (devis)

# Noms qui ne doivent jamais paraître dans le cadre écrit par l'orchestrateur (pseudonymes, consignes, en-têtes).
MOTIF_NOMS_MODELES = re.compile(r"(?i)(?<![^\W_])(?:fable|opus|argon|astra|carbon|neon|kimi|claude|gemini|gpt|chatgpt|"
                                r"anthropic|openai|google|deepmind)(?![^\W_])")
# Note ou verdict dans une revue (choix du développeur, à trancher) : une revue est un texte, sans note ni verdict.
# v2 (R6) : restreint à une note chiffrée explicite ; les verdicts en mots ne sont plus détectés (à trancher).
MOTIF_NOTE = re.compile(r"(?i)\b(?:note|score)\s*[:=]\s*\d")
GENRES = ("SALON", "PREPUBLICATION", "REVUE", "ERRATUM", "OUVRIR")
MOTIF_BALISE = re.compile(r"^===\s*(FIN\s+)?([A-ZÉ]+)(?:\s+(\S+))?\s*===\s*$")
MOTIF_ID = re.compile(r"\b(?:salon|revue|erratum)-[0-9a-f]{6}\b|\bprepub-[0-9a-f]{6}(?:-v\d+)?\b")  # v2 (B1)
BALISES_BLOC = ("<<<", ">>>")  # v2 (B2) : jamais dans un texte d'agent ni dans l'injection
MOTIF_BLOC = re.compile(r"<<<DÉBUT ([A-Z-]+) (\S+) sha256=([0-9a-f]{64})>>>\n(.*?)\n<<<FIN \1 \2>>>", re.S)

ENTETE_ESSAIM = """Tu participes à une idéation scientifique entre plusieurs modèles de langue, arbitrée par un humain. Ton \
pseudonyme est {pseudo}. Les autres participants portent aussi des pseudonymes ; qui est derrière chacun n'a pas \
d'importance. Les prépublications et les revues circulent sans nom d'auteur."""

CONSIGNE_CYCLE = """Temps de société, cycle {k} sur {n}. Tu reçois ton brouillon, ta prépublication s'il y en a une, la \
liste des nouveautés du fil commun depuis ton dernier passage (titre et première ligne de chacune), les textes complets \
que tu as demandés, et les prépublications que tu dois revoir. Tous les échanges sont publics et journalisés ; il n'y a \
aucun message privé.
Livrable : des sections balisées exactement comme ci-dessous, chaque balise seule sur sa ligne ; toute section est \
facultative.
- Au plus {salons} messages de salon, de {mots_salon} mots au plus chacun (question, antériorité, expérience, désaccord) :
=== SALON ===
Titre : …
texte
=== FIN SALON ===
- Au plus une prépublication, de {mots_prepub} mots au plus. La première dépose ta prépublication ; les suivantes la \
révisent (nouvelle version ; l'ancienne reste lisible) :
=== PREPUBLICATION ===
Titre : …
texte
=== FIN PREPUBLICATION ===
- Une revue pour chaque prépublication qu'on te demande de revoir, nommée par son identifiant, de {mots_revue} mots au \
plus. Une revue est un texte : une objection vérifiable, une antériorité, un essai. Elle ne porte ni note, ni score, ni \
verdict :
=== REVUE identifiant-de-la-prépublication ===
texte
=== FIN REVUE ===
- Au plus {erratums} erratums de {mots_erratum} mots au plus, chacun sur l'un de tes propres textes, nommé par son \
identifiant. Un erratum s'ajoute à la suite ; l'original n'est jamais effacé :
=== ERRATUM identifiant ===
texte
=== FIN ERRATUM ===
- Les textes complets que tu veux lire au cycle suivant, au plus {ouvertures}, par leurs identifiants (une série « prepub-… » \
sans « -vN » donne la dernière version) ; ceux que tu demandes au dernier cycle te seront donnés pour ta réponse finale :
=== OUVRIR ===
identifiant, identifiant
=== FIN OUVRIR ===
Un texte au-delà de sa limite de mots, une revue qui porte une note ou un verdict, un erratum sur un texte qui n'est pas \
le tien, un texte qui contient « <<< » ou « >>> », ou une section mal balisée n'est pas publié. Rien d'autre que ces \
sections n'est lu.{noms}"""

CONSIGNE_FINALE = """Temps final : réponse finale privée. Personne ne la lira avant la fin, et tu ne vois pas celles des \
autres participants. Tu reçois ton brouillon, ta prépublication s'il y en a une, la liste de tout le fil commun (titre et \
première ligne) et les textes complets que tu as demandés au dernier cycle.
Livrable : (a) pour chaque critique reçue (revues, messages du salon) : acceptée, rejetée avec sa raison, ou transformée \
en test ; (b) les expériences corrigées ; (c) ta réponse à la question de l'arbitre, en une page : ce qui est établi, ce \
qui ne l'est pas, et l'expérience à faire en premier."""


# ---------- chargement de la v8d, tours neufs ----------

def charger_v8d(chemin=SCRIPT_V8D, sha=SHA_V8D):
    h = hashlib.sha256(Path(chemin).read_bytes()).hexdigest()
    if h != sha:
        raise SystemExit(f"ARRÊT : empreinte de la v8d {h} différente de {sha}")
    spec = importlib.util.spec_from_file_location("collisionneur_v9_v8d_pour_essaim", chemin)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def tour_cycle(k):
    return f"W1-C{k:02d}"


def tours_essaim(cfg):
    t = {TOUR_BROUILLON: {"nom": "brouillon", "mots": cfg["mots"]["brouillon"]}}
    for k in range(1, cfg["cycles"] + 1):
        t[tour_cycle(k)] = {"nom": "societe", "mots": cfg["mots"]["cycle"]}
    t[TOUR_FINALE] = {"nom": "reponse-finale", "mots": cfg["mots"]["finale"]}
    return t


def installer_tours(v, cfg):
    """Ajoute les tours de l'essaim à v.TOURS ; refuse de toucher un tour existant (ceux de la v8d restent tels quels)."""
    for tour, d in tours_essaim(cfg).items():
        if tour in v.TOURS and v.TOURS[tour] != d:
            raise v.Arret(v.CODE_USAGE, f"tour {tour} déjà présent dans TOURS avec un autre réglage")
        if any(tour != t and (tour.startswith(t) or t.startswith(tour)) for t in v.TOURS):
            raise v.Arret(v.CODE_USAGE, f"tour {tour} : préfixe commun avec un tour existant")
        v.TOURS[tour] = d


def phase_du_tour(tour):
    return {"W0": "temps0", "W1": "temps1", "W2": "temps2"}.get(tour[:2])


def decoupe_cid(v, cid):
    """(tour, lettre) d'une cellule de l'essaim, ou (None, None)."""
    for t in v.TOURS:
        if phase_du_tour(t) and cid.startswith(t + "-") and cid == v.id_cellule(t, cid[-1]):
            return t, cid[-1]
    return None, None


# ---------- configuration (classe A : paramètres, jamais codés en dur) ----------

def lire_configuration(v, chemin, exiger_enveloppe=True):
    try:
        cfg = json.loads(v.lire_entree(chemin))
    except ValueError as e:
        raise v.Arret(v.CODE_USAGE, f"configuration illisible ({e})")
    probl = []
    for cle in ("especes", "graine", "cycles", "repartition", "mots", "messages_salon_max", "erratums_max",
                "ouvertures_max", "relecteurs", "pseudonymes"):
        if cle not in cfg:
            probl.append(f"clé {cle} absente")
    if probl:
        raise v.Arret(v.CODE_USAGE, "configuration : " + " ; ".join(probl))
    rep = cfg["repartition"]
    if set(rep) != set(PHASES) or any(not isinstance(rep[p], (int, float)) or rep[p] < 0 for p in PHASES) \
            or abs(sum(rep.values()) - 1) > 1e-9:
        probl.append("repartition : temps0, temps1, temps2, positifs, de somme 1")
    if not isinstance(cfg["cycles"], int) or not 1 <= cfg["cycles"] <= 99:
        probl.append("cycles : entier de 1 à 99")
    if not isinstance(cfg["graine"], int) or cfg["graine"] < 0:
        probl.append("graine : entier positif")
    n = len(cfg["especes"]) if isinstance(cfg["especes"], list) else 0
    if not isinstance(cfg["relecteurs"], int) or cfg["relecteurs"] < 1:
        probl.append("relecteurs : entier positif")
    elif n < cfg["relecteurs"] + 1:
        probl.append("especes : au moins relecteurs + 1 agents")
    for cle in ("brouillon", "cycle", "finale", "salon", "prepublication", "revue", "erratum"):
        if not isinstance(cfg["mots"].get(cle), int) or cfg["mots"][cle] <= 0:
            probl.append(f"mots.{cle} : entier positif")
    pool = cfg["pseudonymes"]
    if not isinstance(pool, list) or len(set(pool)) != len(pool) or len(pool) < n + 1:
        probl.append("pseudonymes : liste sans doublon, au moins un de plus que d'agents (le tiers)")
    elif any(MOTIF_NOMS_MODELES.search(p) or not re.fullmatch(r"[^\W\d_]{2,20}", p) for p in pool):
        probl.append("pseudonymes : un seul mot de lettres, aucun nom de modèle ni de fournisseur")
    env = cfg.get("enveloppe_usd")
    if exiger_enveloppe and not (isinstance(env, (int, float)) and env > 0):
        probl.append("enveloppe_usd : coût mesuré du dossier isolé de la même question (commande « enveloppe »), positif")
    if probl:
        raise v.Arret(v.CODE_USAGE, "configuration : " + " ; ".join(probl))
    return cfg


def parts(cfg, n, enveloppe=None):
    env = cfg["enveloppe_usd"] if enveloppe is None else enveloppe
    return {p: env * cfg["repartition"][p] / n for p in PHASES}


# ---------- hasard : SeedSequence, dérivé par usage, consigné ----------

def generateur(tirage, *cles):
    ss = np.random.SeedSequence(tirage["entropie"], spawn_key=tuple(tirage["cle_dossier"]) + tuple(cles))
    return np.random.Generator(np.random.PCG64(ss))


def tirer(v, cfg, entropie, cle_dossier):
    tirage = {"entropie": entropie, "cle_dossier": cle_dossier, "numpy": np.__version__,
              "generateur": "PCG64(SeedSequence(entropie, spawn_key=cle_dossier + usage))"}
    pool = list(cfg["pseudonymes"])
    choisis = generateur(tirage, USAGE_PSEUDONYMES).choice(len(pool), len(v.LETTRES) + 1, replace=False)
    tirage["pseudonymes"] = {l: pool[int(i)] for l, i in zip(v.LETTRES, choisis[:-1])}
    tirage["pseudonyme_tiers"] = pool[int(choisis[-1])]
    tirage["ordre"] = [v.LETTRES[int(i)] for i in generateur(tirage, USAGE_ORDRE).permutation(len(v.LETTRES))]
    return tirage


def sans_version(tirage):
    return {c: x for c, x in tirage.items() if c != "numpy"}


def tirer_relecteurs(v, cfg, tirage, k, auteur):
    autres = [l for l in v.LETTRES if l != auteur]
    rng = generateur(tirage, USAGE_RELECTEURS, k, v.LETTRES.index(auteur))
    return sorted(autres[int(i)] for i in rng.choice(len(autres), cfg["relecteurs"], replace=False))


def cle_dossier(dossier):
    return [int(hashlib.sha256(Path(dossier).resolve().name.encode("utf-8")).hexdigest()[:8], 16)]


def tirages_du_dossier(v, cfg, dossier):
    """Écrits une fois (ecrire_neuf), relus et recontrôlés à chaque reprise : aucun hasard n'est retiré."""
    chemin = Path(dossier) / "tirages.json"
    if chemin.exists():
        texte, _ = v.lire_sceau(chemin)
        tirage = json.loads(texte)
        if sans_version(tirer(v, cfg, tirage["entropie"], tirage["cle_dossier"])) != sans_version(tirage):
            raise v.Arret(v.CODE_USAGE, "tirages.json ne se recalcule pas depuis sa graine : dossier altéré")
        return tirage
    tirage = tirer(v, cfg, cfg["graine"], cle_dossier(dossier))
    v.ecrire_neuf(chemin, json.dumps(tirage, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    v.ajouter_journal(dossier, {"tirages": tirage, "quand": v.maintenant(), "programme": VERSION})
    return tirage


# ---------- tableau : journal en ajout seul ----------

def elements(v, dossier):
    """Tous les éléments publiés, dans l'ordre de publication (injection comprise)."""
    out = []
    for e in v.lire_journal(dossier):
        if isinstance(e.get("injection"), dict):
            out.append(e["injection"])
        if "publication" in e:
            out.extend(e["elements"])
    return out


def publications(v, dossier):
    return {e["publication"]: e for e in v.lire_journal(dossier) if "publication" in e}


def sauts(v, dossier):
    return {e["saut"]: e for e in v.lire_journal(dossier) if "saut" in e}


def lire_element(v, dossier, el):
    texte, h = v.lire_sceau(Path(dossier) / el["chemin"])
    if h != el["sha256"]:
        raise v.Arret(v.CODE_USAGE, f"{el['id']} : empreinte différente du journal")
    return texte


def ecrire_element(v, dossier, ident, texte):
    """Écrit tableau/<id>.md une fois ; à la reprise, un fichier déjà écrit doit être le même (sinon arrêt)."""
    chemin = Path(dossier) / "tableau" / f"{ident}.md"
    if chemin.exists():
        _, h = v.lire_sceau(chemin)
        if h != v.empreinte(texte):
            raise v.Arret(v.CODE_USAGE, f"{ident} : tableau déjà écrit avec un autre texte")
        return h, f"tableau/{ident}.md"
    return v.ecrire_neuf(chemin, texte), f"tableau/{ident}.md"


def premiere_ligne(corps):
    for l in corps.splitlines():
        if l.strip():
            return l.strip()
    return ""


def titre_et_corps(texte):
    lignes = texte.strip("\n").splitlines()
    if lignes and re.match(r"^\s*Titre\s*:", lignes[0]):
        return lignes[0].split(":", 1)[1].strip() or None, "\n".join(lignes[1:])
    return None, "\n".join(lignes)


def couper(s):
    return s if len(s) <= COUPE_LIGNE else s[:COUPE_LIGNE] + " […coupé à l'affichage]"


def mots(texte):
    return len(texte.split())


# ---------- lecture des sections balisées ----------

def lire_sections(texte, marqueur):
    """Renvoie (sections, anomalies). Section : {genre, cible, texte}. Rien n'est inventé : une section mal balisée est
    écartée et nommée dans les anomalies (genre, ligne), jamais réparée."""
    sections, anomalies, courant, hors = [], [], None, 0
    for n, ligne in enumerate(texte.splitlines(), 1):
        m = MOTIF_BALISE.match(ligne.strip())
        if m:
            fin, genre, cible = bool(m.group(1)), m.group(2), m.group(3)
            genre = "PREPUBLICATION" if genre == "PRÉPUBLICATION" else genre  # graphie accentuée admise
            if genre not in GENRES:
                anomalies.append({"ligne": n, "anomalie": f"balise inconnue {genre}"})
                continue
            if fin:
                if courant is None or courant["genre"] != genre:
                    anomalies.append({"ligne": n, "anomalie": f"fin de {genre} sans ouverture"})
                else:
                    courant["texte"] = "\n".join(courant["lignes"]).strip("\n")
                    del courant["lignes"]
                    sections.append(courant)
                    courant = None
                continue
            if courant is not None:
                anomalies.append({"ligne": courant["ligne"], "anomalie": f"{courant['genre']} non fermée : écartée"})
            courant = {"genre": genre, "cible": cible, "ligne": n, "lignes": []}
            continue
        if courant is not None:
            courant["lignes"].append(ligne)
        elif ligne.strip() and ligne.strip() != marqueur:
            hors += len(ligne)
    if courant is not None:
        anomalies.append({"ligne": courant["ligne"], "anomalie": f"{courant['genre']} non fermée : écartée"})
    if hors:
        anomalies.append({"ligne": None, "anomalie": f"texte hors section : {hors} caractères, non lus"})
    return sections, anomalies


# ---------- vues du tableau pour un agent ----------

def rang_lt(a, b):
    return tuple(a) < tuple(b)


def dernier_appel(v, dossier, lettre, avant):
    """Rang de la dernière publication de l'agent avant `avant` (appel réellement fait), ou None."""
    rangs = [p["rang"] for p in publications(v, dossier).values() if p["lettre"] == lettre and rang_lt(p["rang"], avant)]
    return max(rangs, key=tuple) if rangs else None


def ouvertures_demandees(v, dossier, lettre, avant):
    r = dernier_appel(v, dossier, lettre, avant)
    if r is None:
        return []
    p = next(p for p in publications(v, dossier).values() if p["lettre"] == lettre and p["rang"] == r)
    return p["ouvrir"]


def resoudre(els, ident):
    """Élément désigné ; une série « prepub-xxxxxx » donne la dernière version publiée."""
    if re.fullmatch(r"prepub-[0-9a-f]{6}", ident):
        vers = [e for e in els if e["genre"] == "PREPUBLICATION" and e["serie"] == ident]
        return vers[-1] if vers else None
    return next((e for e in els if e["id"] == ident), None)


def ligne_nouveaute(el, lettre=None):
    g = el["genre"]
    if g == "SALON":
        meta = f"salon, {el['pseudonyme']}"
    elif g == "PREPUBLICATION":
        meta = "prépublication"
    elif g == "REVUE":
        meta = f"revue de {el['cible']}"
    else:
        meta = f"erratum à {el['cible']}"
    if lettre is not None and el["lettre"] == lettre:
        meta += ", toi"
    cadre = f"- [{el['id']}] {meta}, cycle {el['cycle']} : "
    texte = f"« {couper(el['titre'] or '(sans titre)')} » — {couper(el['premiere_ligne'])}"
    return cadre, texte


def bloc(genre, ident, texte):
    return f"<<<DÉBUT {genre} {ident} sha256={hashlib.sha256(texte.encode('utf-8')).hexdigest()}>>>\n{texte}\n" \
           f"<<<FIN {genre} {ident}>>>"


def entete_element(el):
    if el["genre"] == "SALON":
        return f"{el['id']} (salon, {el['pseudonyme']}, cycle {el['cycle']})"
    if el["genre"] == "REVUE":
        return f"{el['id']} (revue de {el['cible']}, cycle {el['cycle']})"
    if el["genre"] == "ERRATUM":
        return f"{el['id']} (erratum à {el['cible']}, cycle {el['cycle']})"
    return f"{el['id']} (prépublication, cycle {el['cycle']})"


def construire_invite(v, cfg, tirage, dossier, phase, k, lettre, rang):
    """Renvoie (invite, lecture). Le cadre (tout ce qu'écrit l'orchestrateur) est gardé contre les noms de modèle ; les
    textes des agents sont injectés entre balises, avec leur empreinte."""
    tour = {"temps0": TOUR_BROUILLON, "temps1": tour_cycle(k) if k else None, "temps2": TOUR_FINALE}[phase]
    mots_tour = v.TOURS[tour]["mots"]
    pseudo = tirage["pseudonymes"][lettre]
    faits, h_faits = v.lire_sceau(Path(dossier) / "faits.md")
    question, h_q = v.lire_sceau(Path(dossier) / "question-etage3.md")
    gabarit = v.PREAMBULE_GABARIT
    debut, reste = gabarit.split("\n\nRègles d'intégrité", 1)
    if not debut.startswith("Tu participes"):
        raise v.Arret(v.CODE_USAGE, "préambule de la v8d de forme inattendue")
    preambule = (ENTETE_ESSAIM.format(pseudo=pseudo) + "\n\nRègles d'intégrité"
                 + reste.format(mots=mots_tour, marqueur=v.MARQUEUR))
    cadre, morceaux, lecture = [], [], []

    def c(t):  # morceau de cadre
        cadre.append(t)
        morceaux.append(t)

    def injecter(genre, ident, texte, source):
        morceaux.append(bloc(genre, ident, texte))
        lecture.append({"genre": genre, "id": ident, "sha256": v.empreinte(texte), "source": source})

    c(preambule)
    morceaux.append(f"<<<DÉBUT FAITS sha256={h_faits}>>>\n{faits}\n<<<FIN FAITS>>>")
    if phase == "temps0":
        c(v.CONSIGNES["E3-T1"])
    elif phase == "temps1":
        c(CONSIGNE_CYCLE.format(k=k, n=cfg["cycles"], salons=cfg["messages_salon_max"], mots_salon=cfg["mots"]["salon"],
                                mots_prepub=cfg["mots"]["prepublication"], mots_revue=cfg["mots"]["revue"],
                                erratums=cfg["erratums_max"], mots_erratum=cfg["mots"]["erratum"],
                                ouvertures=cfg["ouvertures_max"]))
    else:
        c(CONSIGNE_FINALE)
    morceaux.append(f"<<<DÉBUT QUESTION DE L'ARBITRE sha256={h_q}>>>\n{question}\n<<<FIN QUESTION DE L'ARBITRE>>>")
    if phase != "temps0":
        els = [e for e in elements(v, dossier) if rang_lt(e["rang"], rang)]
        brouillon = v.cellule_valide(dossier, v.id_cellule(TOUR_BROUILLON, lettre))
        if brouillon:
            injecter("TON-BROUILLON", "brouillon", brouillon[0], v.id_cellule(TOUR_BROUILLON, lettre))
        else:
            c("Ton brouillon est absent (décision de l'arbitre) ; n'en invente pas le contenu.")
        miens = [e for e in els if e["lettre"] == lettre]
        mes_prepubs = [e for e in miens if e["genre"] == "PREPUBLICATION"]
        if mes_prepubs:
            el = mes_prepubs[-1]
            injecter("TA-PREPUBLICATION", el["id"], lire_element(v, dossier, el), el["chemin"])
        if miens:
            c("Tes textes publiés (identifiants) : " + ", ".join(e["id"] for e in miens) + ".")
        if phase == "temps1":
            depuis = dernier_appel(v, dossier, lettre, rang)
            nouveaux = [e for e in els if e["lettre"] != lettre and (depuis is None or rang_lt(depuis, e["rang"]))]
            titre_liste = "Nouveautés du fil commun depuis ton dernier passage"
        else:
            nouveaux = els
            titre_liste = "Tout le fil commun"
        if nouveaux:
            c(titre_liste + " (titre et première ligne) :")
            lignes = []
            for el in nouveaux:
                cadre_l, texte_l = ligne_nouveaute(el, lettre)
                cadre.append(cadre_l)
                lignes.append(cadre_l + texte_l)
            morceaux.append("\n".join(lignes))
        else:
            c(titre_liste + " : aucune.")
        demandes = ouvertures_demandees(v, dossier, lettre, rang)
        if demandes:
            c("Textes complets que tu as demandés :")
            for ident in demandes:
                el = resoudre(els, ident)
                if el is None:  # contrôlé à la publication ; défense en profondeur
                    raise v.Arret(v.CODE_USAGE, f"texte demandé {ident} introuvable")
                c(entete_element(el))
                injecter("TEXTE", el["id"], lire_element(v, dossier, el), el["chemin"])
        if phase == "temps1":
            a_revoir = [e for e in els if e["genre"] == "PREPUBLICATION" and e["cycle"] == k - 1
                        and lettre in e["relecteurs"]]
            if a_revoir:
                c("Prépublications que tu dois revoir à ce cycle (une revue chacune) :")
                for el in a_revoir:
                    injecter("A-REVOIR", el["id"], lire_element(v, dossier, el), el["chemin"])
            else:
                c("Aucune prépublication à revoir à ce cycle.")
    invite = "\n\n".join(morceaux) + "\n"
    texte_cadre = "\n".join(cadre)
    fuite = MOTIF_NOMS_MODELES.search(texte_cadre)
    if fuite or re.search(r"W\d-[A-Z]\d+-[a-z-]+-[A-Z]\b", texte_cadre) or "proposition " + lettre in texte_cadre:
        raise v.Arret(v.CODE_USAGE, f"{v.id_cellule(tour, lettre)} : nom de modèle ou identifiant interne dans le cadre "
                                    f"de l'invite (caractère {fuite.start() if fuite else '?'}) ; rien n'est envoyé")
    return invite, lecture


# ---------- publication d'une sortie de cycle ----------

def publier(v, cfg, tirage, dossier, cid, k, lettre, rang, texte):
    """Lit les sections, écrit chaque élément publiable une fois, puis une seule ligne de journal (atomique)."""
    els = [e for e in elements(v, dossier)]
    sections, anomalies = lire_sections(texte, v.MARQUEUR)
    pubs, refus, ouvrir, ouvrir_refus, noms = [], [], [], [], []
    compte = {g: sum(1 for e in els if e["genre"] == g) for g in ("SALON", "REVUE", "ERRATUM")}
    series = sorted({e["serie"] for e in els if e["genre"] == "PREPUBLICATION"})
    mienne = next((e["serie"] for e in els if e["genre"] == "PREPUBLICATION" and e["lettre"] == lettre), None)
    a_revoir = {e["id"] for e in els if e["genre"] == "PREPUBLICATION" and e["cycle"] == k - 1
                and lettre in e["relecteurs"]}
    miens = {e["id"] for e in els if e["lettre"] == lettre} | ({mienne} if mienne else set())
    n_salon = n_err = n_prepub = 0
    revus = set()
    for s in sections:
        g, corps = s["genre"], s["texte"]
        if g == "OUVRIR":
            for ident in MOTIF_ID.findall(corps):
                if ident in ouvrir:
                    continue
                if len(ouvrir) >= cfg["ouvertures_max"]:
                    ouvrir_refus.append({"id": ident, "motif": "au-delà du maximum"})
                elif resoudre(els + pubs, ident) is None:
                    ouvrir_refus.append({"id": ident, "motif": "inconnu"})
                else:
                    ouvrir.append(ident)
            continue
        limite = {"SALON": "salon", "PREPUBLICATION": "prepublication", "REVUE": "revue", "ERRATUM": "erratum"}[g]
        motif = None
        if not corps.strip():
            motif = "vide"
        elif mots(corps) > cfg["mots"][limite]:
            motif = f"{mots(corps)} mots > {cfg['mots'][limite]}"
        elif v.motifs_trouves(corps):
            motif = "motif interdit (" + ", ".join(t[0] for t in v.motifs_trouves(corps)) + ")"
        elif g == "SALON" and n_salon >= cfg["messages_salon_max"]:
            motif = "au-delà du nombre de messages"
        elif g == "PREPUBLICATION" and n_prepub >= 1:
            motif = "au-delà d'une prépublication par cycle"
        elif g == "REVUE" and s["cible"] not in a_revoir:
            motif = "revue non attribuée à ce cycle"
        elif g == "REVUE" and s["cible"] in revus:
            motif = "seconde revue de la même prépublication"
        elif g == "REVUE" and MOTIF_NOTE.search(corps):
            motif = "revue avec note ou verdict"
        elif g == "ERRATUM" and n_err >= cfg["erratums_max"]:
            motif = "au-delà du nombre d'erratums"
        elif g == "ERRATUM" and s["cible"] not in miens:
            motif = "erratum sur un texte qui n'est pas le sien"
        if motif:
            refus.append({"genre": g, "cible": s["cible"], "ligne": s["ligne"], "mots": mots(corps), "motif": motif,
                          "sha256": v.empreinte(corps)})
            continue
        titre, reste = titre_et_corps(corps)
        el = {"genre": g, "cycle": k, "rang": list(rang), "lettre": lettre, "titre": titre,
              "premiere_ligne": premiere_ligne(reste), "cible": s["cible"], "relecteurs": []}
        if g == "SALON":
            n_salon += 1
            compte["SALON"] += 1
            el["id"], el["pseudonyme"] = f"salon-{compte['SALON']}", tirage["pseudonymes"][lettre]
        elif g == "REVUE":
            revus.add(s["cible"])
            compte["REVUE"] += 1
            el["id"] = f"revue-{compte['REVUE']}"
        elif g == "ERRATUM":
            n_err += 1
            compte["ERRATUM"] += 1
            el["id"] = f"erratum-{compte['ERRATUM']}"
        else:
            n_prepub += 1
            if mienne is None:
                mienne = f"prepub-{len(series) + 1}"
            version = 1 + sum(1 for e in els + pubs if e["genre"] == "PREPUBLICATION" and e["serie"] == mienne)
            el.update(id=f"{mienne}-v{version}", serie=mienne, version=version, cible=None)
            if k < cfg["cycles"]:
                el["relecteurs"] = tirer_relecteurs(v, cfg, tirage, k, lettre)
            miens.add(el["id"])
        el["sha256"], el["chemin"] = ecrire_element(v, dossier, el["id"], corps)
        if MOTIF_NOMS_MODELES.search(corps):  # choix du développeur : signalé, publié tel quel
            noms.append(el["id"])
        miens.add(el["id"])
        pubs.append(el)
    v.ajouter_journal(dossier, {"publication": cid, "cycle": k, "rang": list(rang), "lettre": lettre,
                                "elements": pubs, "refuses": refus, "anomalies_balisage": anomalies,
                                "ouvrir": ouvrir, "ouvrir_refuses": ouvrir_refus, "noms_de_modele_signales": noms,
                                "dernier_cycle_sans_revue": k == cfg["cycles"],
                                "sha256_cellule": v.empreinte(texte), "quand": v.maintenant(), "programme": VERSION})
    return pubs


# ---------- injection des erreurs plantées ----------

def injecter_erreurs(v, cfg, tirage, dossier, chemin):
    """Crochet optionnel : un fichier scellé (F et F.sha256), injecté une fois comme message de salon du pseudonyme tiers
    au premier cycle. Sans fichier, rien n'est injecté et le journal le dit. La décision est prise une fois."""
    deja = [e for e in v.lire_journal(dossier) if "injection" in e]
    h = None
    if chemin:
        texte, h = v.lire_sceau(chemin)
    if deja:
        avant = deja[0]["injection"]
        if (avant or {}).get("sha256_source") != h:
            raise v.Arret(v.CODE_USAGE, "--erreurs-plantees différent de la décision consignée au premier lancement")
        return
    if not chemin:
        v.ajouter_journal(dossier, {"injection": None, "motif": "aucun fichier d'erreurs plantées : rien n'est injecté",
                                    "quand": v.maintenant(), "programme": VERSION})
        return
    texte = v.normaliser(texte)
    if v.motifs_trouves(texte):
        raise v.Arret(v.CODE_MOTIF, "erreurs plantées : motif interdit dans le fichier ; rien n'est injecté")
    titre, reste = titre_et_corps(texte)
    ident = "salon-1"
    if any(e["id"] == ident for e in elements(v, dossier)):
        raise v.Arret(v.CODE_USAGE, "injection après une publication : ordre du dossier rompu")
    h2, rel = ecrire_element(v, dossier, ident, texte)
    el = {"genre": "SALON", "id": ident, "cycle": 1, "rang": [1, -1], "lettre": TIERS, "titre": titre,
          "premiere_ligne": premiere_ligne(reste), "cible": None, "relecteurs": [],
          "pseudonyme": tirage["pseudonyme_tiers"], "sha256": h2, "chemin": rel,
          "source": Path(chemin).name, "sha256_source": h}
    v.ajouter_journal(dossier, {"injection": el, "quand": v.maintenant(), "programme": VERSION})


# ---------- budget : part contrôlée sur le coût mesuré ----------

def depense_agent(v, dossier, lettre, phase):
    s = 0.0
    for e in v.essais_journal(dossier):
        t, l = decoupe_cid(v, e["cellule"])
        if l == lettre and phase_du_tour(t) == phase:
            s += e.get("cout_usd", 0.0)
    return round(s, 6)


# ---------- déroulé ----------

def appel(v, cfg, tirage, dossier, phase, k, lettre, rang, plafond, absences, appelants):
    """Un tour d'un agent. Renvoie le statut : FAIT, SAUTE, ABSENCE."""
    tour = {"temps0": TOUR_BROUILLON, "temps1": tour_cycle(k) if k else None, "temps2": TOUR_FINALE}[phase]
    cid = v.id_cellule(tour, lettre)
    if phase == "temps1" and cid in publications(v, dossier):
        return "FAIT"
    if v.cellule_valide(dossier, cid):
        if phase == "temps1":  # reprise après une coupure entre la cellule et sa publication
            publier(v, cfg, tirage, dossier, cid, k, lettre, rang, v.cellule_valide(dossier, cid)[0])
        return "FAIT"
    if cid in sauts(v, dossier):
        return "SAUTE"
    if cid in absences:
        print(f"{cid} : absence acceptée par l'arbitre, non relancée", flush=True)
        return "ABSENCE"
    part = parts(cfg, len(v.LETTRES))[phase]
    deja = depense_agent(v, dossier, lettre, phase)
    if not v.essais_journal(dossier, cid) and deja >= part:
        v.ajouter_journal(dossier, {"saut": cid, "motif": "part épuisée", "phase": phase, "lettre": lettre,
                                    "depense_phase_usd": deja, "part_usd": round(part, 6), "rang": list(rang),
                                    "quand": v.maintenant(), "programme": VERSION})
        print(f"{cid} : part épuisée ({deja:.4f} ≥ {part:.4f} USD), tour sauté (journalisé)", flush=True)
        return "SAUTE"
    if v.statut_courant(dossier, cid) == "REFUS" or v.reglage_en_defaut(dossier, cid, v.MODELES[lettre]):
        raise v.Arret(v.CODE_PORTE, f"{cid} : dernier essai {v.statut_courant(dossier, cid)} refusé ou en défaut au même "
                                    f"réglage : non renvoyé ; --accepter-absence {cid}, ou décision de l'arbitre")
    invite, lecture = construire_invite(v, cfg, tirage, dossier, phase, k, lettre, rang)
    precedents = v.essais_journal(dossier, cid)
    if precedents and precedents[-1]["sha256_prompt"] != v.empreinte(invite):
        raise v.Arret(v.CODE_USAGE, f"{cid} : l'invite reconstruite à la reprise diffère de celle déjà envoyée ; "
                                    f"tableau ou tirages altérés ; rien n'est envoyé")
    v.ajouter_journal(dossier, {"lecture": cid, "sha256_prompt": v.empreinte(invite), "textes": lecture,
                                "rang": list(rang), "quand": v.maintenant(), "programme": VERSION})
    statut = v.executer_cellule(str(dossier), tour, lettre, invite, [], plafond, appelants)
    if statut != "OK":
        raise v.Arret(v.CODE_PORTE, f"{cid} : statut {statut} ; aucune suite sans décision de l'arbitre "
                                    f"(--accepter-absence {cid})")
    if phase == "temps1":
        publier(v, cfg, tirage, dossier, cid, k, lettre, rang, v.cellule_valide(dossier, cid)[0])
    return "FAIT"


def derouler(v, cfg, tirage, dossier, plafond, absences, appelants):
    ordre = tirage["ordre"]
    for i, l in enumerate(ordre):
        appel(v, cfg, tirage, dossier, "temps0", 0, l, (0, i), plafond, absences, appelants)
    manquants = [l for l in ordre if not v.cellule_valide(dossier, v.id_cellule(TOUR_BROUILLON, l))
                 and v.id_cellule(TOUR_BROUILLON, l) not in absences and v.id_cellule(TOUR_BROUILLON, l)
                 not in sauts(v, dossier)]
    if manquants:
        raise v.Arret(v.CODE_PORTE, f"brouillons manquants {manquants}")
    for k in range(1, cfg["cycles"] + 1):
        etats = [appel(v, cfg, tirage, dossier, "temps1", k, l, (k, i), plafond, absences, appelants)
                 for i, l in enumerate(ordre)]
        if all(e != "FAIT" for e in etats):
            if not any(e.get("arret_societe") for e in v.lire_journal(dossier)):
                v.ajouter_journal(dossier, {"arret_societe": k, "motif": "aucun agent appelé à ce cycle (parts épuisées "
                                                                         "ou absences) : fin du temps 1",
                                            "quand": v.maintenant(), "programme": VERSION})
            break
    n = cfg["cycles"] + 1
    for i, l in enumerate(ordre):
        appel(v, cfg, tirage, dossier, "temps2", 0, l, (n, i), plafond, absences, appelants)


def declarer_programme(v, dossier, reprise):
    h = v.empreinte_fichier(__file__)
    lignes = [e for e in v.lire_journal(dossier) if "programme_essaim" in e]
    if lignes and lignes[-1]["programme_essaim"]["sha256"] != h and not reprise:
        raise v.Arret(v.CODE_USAGE, f"dossier commencé sous un autre programme d'essaim "
                                    f"({lignes[-1]['programme_essaim']['sha256']}) ; ajoute --reprise pour le déclarer")
    v.ajouter_journal(dossier, {"programme_essaim": {"version": VERSION, "sha256": h, "sha256_v8d": SHA_V8D,
                                                     "reprise_declaree": bool(lignes) and lignes[-1]["programme_essaim"]
                                                     ["sha256"] != h},
                                "quand": v.maintenant()})


def lancer(v, a, appelants=None):
    appelants = appelants or v.APPELANTS
    dossier = Path(a.sortie)
    try:
        cfg = lire_configuration(v, a.configuration)
        installer_tours(v, cfg)
        v.fixer_composition(cfg["especes"], a.cle_anthropic, "ANTHROPIC_WORKSPACE_ID", a.cle_openai)
        hors = [x for x in a.accepter_absence if x not in {v.id_cellule(t, l) for t in tours_essaim(cfg)
                                                            for l in v.LETTRES}]
        if hors:
            raise v.Arret(v.CODE_USAGE, f"--accepter-absence : cellules hors de ce dossier {hors}")
        v.verifier_cles()
        v.verser_une_fois(dossier / "configuration.json", a.configuration, "--configuration")
        v.verser_une_fois(dossier / "faits.md", a.faits or a.question, "--faits (défaut : la question, comme le mode isolé)")
        v.verser_une_fois(dossier / "question-etage3.md", a.question, "--question")
        v.sceller_composition(dossier)
        v.declarer_script(dossier, a.reprise)
        declarer_programme(v, dossier, a.reprise)
        v.ouvrir_ligne(dossier, a.ligne_usd)
        v.consigner_absences(dossier, a.accepter_absence)
        tirage = tirages_du_dossier(v, cfg, dossier)
        injecter_erreurs(v, cfg, tirage, dossier, a.erreurs_plantees)
        derouler(v, cfg, tirage, dossier, a.plafond_usd, set(a.accepter_absence), appelants)
        v.ecrire_etat(str(dossier))
        print(f"Essaim fini ; dépense {v.depense(dossier):.2f} USD. Lance « bilan {dossier} » et « verifier {dossier} ».")
        return v.CODE_FINI
    except v.Arret as e:
        if (dossier / "journal.jsonl").exists() and v.LETTRES:
            v.ecrire_etat(str(dossier))
        print(f"ARRÊT (code {e.code}) : {e}", file=sys.stderr, flush=True)
        return e.code


# ---------- devis, enveloppe, bilan, vérification ----------

def pire_appel(v, m, caracteres):
    garde = v.garde_entree(math.ceil(caracteres / v.RATIO_PROJECTION_ENTREE))
    pire = v.cout_pire_garde(m, garde, m["max"])
    relances = 2 if (m["fournisseur"] == "gemini" and v.reglage_de_relance(m)[1]) else 1
    return pire, pire + relances * v.cout_pire_garde(m, garde, m["max_relance"])


def bornes_caracteres(v, cfg, faits, question):
    """Bornes larges des caractères d'invite par temps (choix du développeur : 7 caractères par mot, comme la v8d)."""
    n = len(cfg["especes"])
    mo = cfg["mots"]
    base = len(v.PREAMBULE_GABARIT) + len(ENTETE_ESSAIM) + 40 + len(faits) + len(question) + 600
    prepub = mo["prepublication"] * CAR_PAR_MOT + v.SURCOUT_BLOC
    par_appel = cfg["messages_salon_max"] + 1 + (n - 1) + cfg["erratums_max"]
    tous = n * cfg["cycles"] * par_appel + 1
    ligne = 2 * COUPE_LIGNE + MARGE_LIGNE
    mes_ids = cfg["cycles"] * par_appel * 20
    commun = mo["brouillon"] * CAR_PAR_MOT + v.SURCOUT_BLOC + prepub + mes_ids + cfg["ouvertures_max"] * (prepub + 120)
    return {"temps0": base + len(v.CONSIGNES["E3-T1"]),
            "temps1": base + len(CONSIGNE_CYCLE) + commun + tous * ligne + (n - 1) * prepub,
            "temps2": base + len(CONSIGNE_FINALE) + commun + tous * ligne}


def devis(v, a):
    try:
        cfg = lire_configuration(v, a.configuration, exiger_enveloppe=False)
        installer_tours(v, cfg)
        v.fixer_composition(cfg["especes"])
    except v.Arret as e:
        print(f"ARRÊT (code {e.code}) : {e}", file=sys.stderr)
        return e.code
    question = v.lire_entree(a.question)
    faits = v.lire_entree(a.faits) if a.faits else question
    env = a.enveloppe_usd if a.enveloppe_usd is not None else cfg.get("enveloppe_usd")
    car = bornes_caracteres(v, cfg, faits, question)
    appels = {"temps0": 1, "temps1": cfg["cycles"], "temps2": 1}
    n = len(v.LETTRES)
    pa = parts(cfg, n, env) if env else None
    print(f"Devis de l'essaim ({VERSION}), {n} agents, {cfg['cycles']} cycles, sans réseau.")
    print("| agent | temps | appels | invite (car., borne) | pire par appel | pire avec relances | pire du temps "
          "| borne mesurée (part + un appel) |")
    print("|---|---|---|---|---|---|---|---|")
    tot = {p: [0.0, 0.0, 0.0] for p in PHASES}
    for l in v.LETTRES:
        m = v.MODELES[l]
        for p in PHASES:
            pire, pire_rel = pire_appel(v, m, car[p])
            du_temps = appels[p] * pire_rel
            borne = min(du_temps, pa[p] + pire_rel) if pa else du_temps
            tot[p][0] += appels[p] * pire
            tot[p][1] += du_temps
            tot[p][2] += borne
            print(f"| {m['espece']} | {p} | {appels[p]} | {car[p]} | {pire:.2f} | {pire_rel:.2f} | {du_temps:.2f} | "
                  f"{borne:.2f} |")
    for p in PHASES:
        print(f"{p} : pire sans relance {tot[p][0]:.2f} USD ; avec relances {tot[p][1]:.2f} ; borne sous les parts "
              f"{tot[p][2]:.2f}" + (f" ; part par agent {pa[p]:.4f} USD (enveloppe {env:.2f} × "
                                    f"{cfg['repartition'][p]} / {n})" if pa else ""))
    print(f"TOTAL : pire sans relance {sum(t[0] for t in tot.values()):.2f} USD ; avec relances "
          f"{sum(t[1] for t in tot.values()):.2f} USD ; borne sous les parts {sum(t[2] for t in tot.values()):.2f} USD"
          + (f" ; enveloppe {env:.2f} USD" if env else " ; enveloppe non donnée"))
    print("Le plafond du dossier (--plafond-usd) est tenu avant chaque envoi par executer_cellule de la v8d sur le pire "
          "cas ; la part par agent est contrôlée sur le coût mesuré (un agent peut dépasser sa part d'au plus un appel).")
    return v.CODE_FINI


def enveloppe(v, a):
    dossier = Path(a.dossier)
    try:
        v.lire_composition(dossier)
    except (v.Arret, ValueError, KeyError) as e:
        print(f"ARRÊT : composition illisible ({e})", file=sys.stderr)
        return v.CODE_USAGE
    essais = v.essais_journal(dossier)
    par = {}
    for e in essais:
        par.setdefault(e["espece"], 0.0)
        par[e["espece"]] += e.get("cout_usd", 0.0)
    attendues = [v.id_cellule(t, l) for t in v.ORDRE_ETAGE[3] for l in v.LETTRES]
    valides = [c for c in attendues if v.cellule_valide(dossier, c)]
    hors = sorted({e["cellule"] for e in essais if not e["cellule"].startswith("E3-")})
    for esp, c in sorted(par.items()):
        print(f"{esp} : {c:.4f} USD")
    print(f"cellules E3 valides : {len(valides)} sur {len(attendues)} ; essais : {len(essais)} (échecs et relances compris)")
    if hors:
        print(f"RÉSERVE : essais hors de l'étage III dans ce dossier : {hors}")
    if len(valides) != len(attendues):
        print("RÉSERVE : dossier isolé incomplet ; son coût n'est pas une enveloppe comparable")
    print(f"enveloppe_usd = {v.depense(dossier):.4f}")
    return v.CODE_FINI if len(valides) == len(attendues) and not hors else v.CODE_USAGE


def charger_dossier(v, dossier):
    texte, _ = v.lire_sceau(Path(dossier) / "configuration.json")
    cfg = json.loads(texte)
    installer_tours(v, cfg)
    v.lire_composition(dossier)
    tirage = json.loads(v.lire_sceau(Path(dossier) / "tirages.json")[0])
    return cfg, tirage


def bilan(v, a):
    dossier = Path(a.dossier)
    try:
        cfg, tirage = charger_dossier(v, dossier)
    except (v.Arret, ValueError, KeyError) as e:
        print(f"ARRÊT : dossier illisible ({e})", file=sys.stderr)
        return v.CODE_USAGE
    pa = parts(cfg, len(v.LETTRES))
    print(f"Bilan de {dossier.name} ; enveloppe {cfg['enveloppe_usd']:.4f} USD ; ordre {tirage['ordre']}")
    print("| lettre | espèce | pseudonyme | temps | appels OK | essais | sauts | entrée | sortie | pensées | coût USD "
          "| part USD |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    sa = sauts(v, dossier)
    for l in v.LETTRES:
        for p in PHASES:
            es = [e for e in v.essais_journal(dossier) if decoupe_cid(v, e["cellule"])[1] == l
                  and phase_du_tour(decoupe_cid(v, e["cellule"])[0]) == p]
            ok = sum(1 for e in es if e["statut"] == "OK")
            ns = sum(1 for c, s in sa.items() if s["lettre"] == l and s["phase"] == p)
            u = lambda cle: sum((e.get("usage") or {}).get(cle) or 0 for e in es)
            pensees = u("reflexion") if v.MODELES[l]["fournisseur"] == "gemini" else "non séparées"
            print(f"| {l} | {v.MODELES[l]['espece']} | {tirage['pseudonymes'][l]} | {p} | {ok} | {len(es)} | {ns} | "
                  f"{u('entree')} | {u('sortie')} | {pensees} | {sum(e.get('cout_usd', 0) for e in es):.4f} | "
                  f"{pa[p]:.4f} |")
    for p in PHASES:
        es = [e for e in v.essais_journal(dossier) if phase_du_tour(decoupe_cid(v, e["cellule"])[0]) == p]
        print(f"{p} : {sum(e.get('cout_usd', 0) for e in es):.4f} USD (part totale {pa[p] * len(v.LETTRES):.4f})")
    pubs = publications(v, dossier)
    print("| lettre | salons | prépublications | revues | erratums | refusés | anomalies de balisage | ouvertures |")
    print("|---|---|---|---|---|---|---|---|")
    for l in v.LETTRES:
        ps = [p for p in pubs.values() if p["lettre"] == l]
        g = lambda genre: sum(1 for p in ps for e in p["elements"] if e["genre"] == genre)
        print(f"| {l} | {g('SALON')} | {g('PREPUBLICATION')} | {g('REVUE')} | {g('ERRATUM')} | "
              f"{sum(len(p['refuses']) for p in ps)} | {sum(len(p['anomalies_balisage']) for p in ps)} | "
              f"{sum(len(p['ouvrir']) for p in ps)} |")
    inj = [e for e in v.lire_journal(dossier) if "injection" in e]
    print("Erreurs plantées : " + ("non décidé" if not inj else "aucune injection" if inj[0]["injection"] is None else
                                   f"injectées ({inj[0]['injection']['id']}, sha256 {inj[0]['injection']['sha256']})"))
    print(f"Dépense totale : {v.depense(dossier):.4f} USD")
    return v.CODE_FINI


def verifier_essaim(v, dossier):
    dossier = Path(dossier)
    try:
        cfg, tirage = charger_dossier(v, dossier)
    except (v.Arret, ValueError, KeyError) as e:
        return [f"configuration, composition ou tirages illisibles : {e}"]
    probl = list(v.verifier(dossier))
    if sans_version(tirer(v, cfg, tirage["entropie"], tirage["cle_dossier"])) != sans_version(tirage):
        probl.append("tirages : ne se recalculent pas depuis la graine")
    els = elements(v, dossier)
    for el in els:
        try:
            lire_element(v, dossier, el)
        except v.Arret as e:
            probl.append(str(e))
        if el["genre"] == "PREPUBLICATION" and el["relecteurs"]:
            if el["lettre"] in el["relecteurs"] or len(set(el["relecteurs"])) != cfg["relecteurs"]:
                probl.append(f"{el['id']} : relecteurs {el['relecteurs']} (auteur compris ou nombre faux)")
            if el["relecteurs"] != tirer_relecteurs(v, cfg, tirage, el["cycle"], el["lettre"]):
                probl.append(f"{el['id']} : relecteurs différents du tirage")
        if el["genre"] == "REVUE" and MOTIF_NOTE.search(lire_element(v, dossier, el) if el.get("chemin") else ""):
            probl.append(f"{el['id']} : revue publiée avec une note ou un verdict")
    ids = [el["id"] for el in els]
    if len(ids) != len(set(ids)):
        probl.append("identifiants publiés en double")
    finales = {v.empreinte(v.cellule_valide(dossier, v.id_cellule(TOUR_FINALE, l))[0])
               for l in v.LETTRES if v.cellule_valide(dossier, v.id_cellule(TOUR_FINALE, l))}
    lectures = {}
    for e in v.lire_journal(dossier):
        if "lecture" in e:
            lectures.setdefault((e["lecture"], e["sha256_prompt"]), e)
    for e in v.essais_journal(dossier):
        t, l = decoupe_cid(v, e["cellule"])
        if t is None:
            probl.append(f"{e['cellule']} : cellule hors de l'essaim")
            continue
        lec = lectures.get((e["cellule"], e["sha256_prompt"]))
        if lec is None:
            probl.append(f"{e['cellule']} essai {e['essai']} : aucune lecture consignée pour cette invite")
            continue
        invite = v.lire_sceau(dossier / "essais" / f"{e['cellule']}.essai{e['essai']}.prompt.txt")[0]
        blocs = {(g, i): (h, txt) for g, i, h, txt in MOTIF_BLOC.findall(invite)}
        for x in lec["textes"]:
            b = blocs.get((x["genre"], x["id"]))
            if b is None or b[0] != x["sha256"] or v.empreinte(b[1]) != x["sha256"]:
                probl.append(f"{e['cellule']} essai {e['essai']} : bloc {x['genre']} {x['id']} absent ou altéré")
        for g, i, h, txt in MOTIF_BLOC.findall(invite):
            if h in finales:
                probl.append(f"{e['cellule']} essai {e['essai']} : une réponse finale paraît dans une invite")
    return probl


def verifier(v, a):
    probl = verifier_essaim(v, a.dossier)
    for x in probl:
        print("PROBLÈME :", x)
    print("Vérification : " + ("tout tient" if not probl else f"{len(probl)} problème(s)"))
    return v.CODE_FINI if not probl else v.CODE_USAGE


def principal(argv=None, appelants=None, v=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sous = p.add_subparsers(dest="commande", required=True)
    d = sous.add_parser("devis")
    d.add_argument("--configuration", required=True)
    d.add_argument("--question", required=True)
    d.add_argument("--faits")
    d.add_argument("--enveloppe-usd", type=float, default=None, help="enveloppe SUPPOSÉE, pour le devis seulement")
    la = sous.add_parser("lancer")
    la.add_argument("--configuration", required=True)
    la.add_argument("--question", required=True)
    la.add_argument("--faits", default=None)
    la.add_argument("--sortie", required=True)
    la.add_argument("--plafond-usd", type=float, required=True)
    la.add_argument("--ligne-usd", type=float, required=True)
    la.add_argument("--cle-anthropic", required=True, help="NOM de la variable qui porte la clé d'Anthropic")
    la.add_argument("--cle-openai", required=True, help="NOM de la variable qui porte la clé d'OpenAI")
    la.add_argument("--erreurs-plantees", default=None, help="fichier scellé (F et F.sha256) ; absent : rien n'est injecté")
    la.add_argument("--accepter-absence", action="append", default=[])
    la.add_argument("--reprise", action="store_true")
    for nom in ("enveloppe", "bilan", "verifier"):
        s = sous.add_parser(nom)
        s.add_argument("dossier")
    a = p.parse_args(argv)
    v = v or charger_v8d()
    if a.commande == "lancer":
        return lancer(v, a, appelants)
    return {"devis": devis, "enveloppe": enveloppe, "bilan": bilan, "verifier": verifier}[a.commande](v, a)


if __name__ == "__main__":
    sys.exit(principal())
