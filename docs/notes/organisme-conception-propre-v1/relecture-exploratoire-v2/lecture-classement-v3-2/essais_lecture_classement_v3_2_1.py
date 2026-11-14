"""Essais de l'outil du lecteur v3.2.1 et du classement v3.2.1 (règle v2.1) — relecture exploratoire, « conception propre ».

v3.2.1 (14 novembre 2026, à partir de 13:01 UTC, `date -u`) = essais v3.2 (`essais_lecture_classement_v3_2.py`, `e5e65b12…`,
gardés) joués contre l'outil et le classement v3.2.1 : noms des programmes, issues de la séparation renommées (« séparation
réelle (portée par R7) », « séparation non établie sur R7 (n = 8) »), plus un essai de la mention « non lue » quand le
classement est non lisible (constat m2 de la contre-lecture). Les pièces épinglées (hasard v2.1, règle v2.1) sont celles de
l'outil v3.2.1.

De la v3.2 :

v3.2 (14 novembre 2026, à partir de 12:30 UTC, `date -u`) : les essais de la v3.1 (`../../lecture-classement-v3-2/`,
`490eb359…`), adaptés aux seuls changements de la v3.2 — noms en `-v3-2`, manifeste `manifeste-relecture-v3-2.json`, dossier
fixe `lecture-g1-v3-2/envois`, plafond absolu 11,65 USD, témoins et hasard v2, codes de témoins `T2-…`, règle v2 au
classement (portes R2 et R3, S v2 avec R7, L3 v2, L5 v2 et séparation, aucune désignation, rang exploratoire) —, plus les
essais neufs de ces changements (C6 v3.2 : première lecture épinglée et tolérée seule ; règle v2 ; descriptifs). Les essais
de la variante « détachée » de la v3.1 sont retirés (variante sans objet : la règle v2 ne désigne rien) ; l'essai « règle
inchangée v3 → v3.1 » devient « règle de lecture inchangée v3.1 → v3.2 ». Lecteur simulé « sain » : comme en v3.1, sauf
les idées au hasard, lues R2 = 0 et R7 = 0 (pour garder un cas sain où L5 v2 rejette et la séparation est « réelle »).

**Hors réseau** : doublure déclarée de l'API (transport injecté) ou petits serveurs sur `127.0.0.1` (adresse d'amont
détournée en mémoire seulement), mandataires retirés ; clés factices. Fiches factices seulement ; les témoins épinglés, les
pièces et les fichiers de la première lecture (manifeste, journal, relevé, classement : aucun texte de fiche) sont recopiés
par les programmes dans une racine factice.

Hors de `tests/` (R-2614). Lancement, depuis la racine du dépôt :

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -m pytest -q -p no:cacheprovider \\
        docs/notes/organisme-conception-propre-v1/relecture-exploratoire-v2/lecture-classement-v3-2/essais_lecture_classement_v3_2_1.py

`LC_MODULES` désigne le dossier des deux programmes essayés (banc de mutations) ; par défaut, celui de ce fichier.
"""
from __future__ import annotations

import ast
import copy
import hashlib
import http.server
import importlib.util
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
RACINE = ICI.parents[4]
MODS = Path(os.environ.get("LC_MODULES", str(ICI)))
CLONE = Path("/home/user/lciric/ideation-organism/orchestrator/pole/ideation_v2.py")
V3_1 = ICI.parents[1] / "lecture-classement-v3-1"


def _charger(nom, fichier, dossier=None):
    spec = importlib.util.spec_from_file_location(nom, (dossier or MODS) / fichier)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


K = _charger("classer_cp_v3_2_1_essai", "classer_conception_propre_v3_2_1.py")
O = K.O
LEVIER_JUGE = "levier:juge"
PRIX = O.PRIX_LUS["standard"]


# --- fiches factices ---------------------------------------------------------------------------------------------------

def fiche(n, auteur, passe, indice, levier, nature="modification", cout="processeur", questions=None):
    f = {
        "nom": f"Idée factice {n} : réglage numéro {n}",
        "type": "approche",
        "enonce": f"Énoncé factice {n} : on change la pièce {n} de l'organisme d'une façon décrite ici, sans rien d'autre « {n} ».",
        "loi_predictive": {"espace_instances": f"famille factice {n}, trente graines",
                           "prediction": f"la couverture augmente de {n} composantes à coût égal contre le témoin {n}",
                           "signe": "+", "metrique": f"composantes couvertes lues par l'oracle, fiche {n}"},
        "perte_traduction": f"perte factice {n}",
        "questions_servies": questions if questions is not None else [levier, "nouvelle"],
        "avantage": {"source": "organisme", "texte": f"avantage factice {n}", "incopiable_parce_que": f"raison {n}"},
        "originalite": {"niveau": "inedite", "texte": f"originalité factice {n}"},
        "demande_organisme": {"nature": nature, "texte": f"changer le paramètre {n} du juge en la valeur {n}"},
        "cout": {"nature": cout, "ordre_de_grandeur": f"coût factice {n}"},
        "piege": f"piège factice {n} : témoin à coût égal",
        "cosmetique_si": f"cosmétique si le témoin {n} fait aussi bien",
        "anteriorite": [{"reference": f"référence factice {n}", "statut": "SUPPOSE"}],
    }
    f["auteur"], f["passe"], f["identifiant_auteur"] = auteur, passe, f"{auteur}-p{passe}-{indice:02d}"
    f["empreinte"] = hashlib.sha256(n.encode()).hexdigest()
    return f


# plan : nom → (auteur, levier, nature, coût, valeurs voulues des deux lectures)
TOUT1 = {"R1": 1, "R2": 1, "R3": 1, "R4": 1, "R5": 1, "R6": 1, "R7": 1, "N": "aucune"}
PLAN = {
    "A1": ("propa", "levier:cout", "ajout", "processeur", {}),
    "A2": ("propb", "levier:proposeurs", "modification", "depense", {}),
    "A3": ("propc", "levier:composition", "modification", "processeur", {"R1": 0}),
    "A4": ("propa", "levier:cout", "modification", "processeur", {"R7": 0}),
    "A5": ("propb", "levier:cout", "modification", "processeur", {"N": "C8"}),
    "A6": ("propc", "levier:proposeurs", "ajout", "processeur", {"R2": 0}),
    "A7": ("propa", LEVIER_JUGE, "modification", "depense", {}),
    "A8": ("propb", "levier:cout", "ajout", "depense", {"R6": 0}),
}
HORS = {"H1": ["levier:cout", "levier:juge", "nouvelle"], "H2": None, "H3": ["QO1", "nouvelle"]}


def fiches_factices(plan=PLAN, hors=True, renommer=None):
    fs = []
    for k, (n, (aut, lev, nat, cout, _)) in enumerate(plan.items(), 1):
        aut = renommer.get(aut, aut) if renommer else aut
        fs.append(fiche(n, aut, 1 + k % 2, k, lev, nat, cout))
    if hors:
        fs.append(fiche("H1", "propa", 2, 20, "levier:cout", questions=HORS["H1"]))
        fs.append(fiche("H2", "propb", 2, 21, "levier:cout", nature="rien"))
        fs.append(fiche("H3", "propc", 2, 22, "levier:cout", questions=HORS["H3"]))
    return fs


RUN = "20261114-010203-course-ideation-conception-propre-v1-g1"


def racine_de(tmp):
    """Racine factice : pièces épinglées (et pièce des prix), fichiers épinglés de la première lecture (manifeste, journal,
    relevé : aucun texte de fiche) et son classement, recopiés du dépôt, jamais modifiés dans le dépôt."""
    rac = Path(tmp) / "racine"
    if not rac.exists():
        for rel, _ in (list(O.PIECES.values()) + list(O.PIECES_PRIX.values()) + list(O.PREMIERE_LECTURE.values())
                       + [K.PREMIERE_CLASSEMENT]):
            (rac / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(RACINE / rel, rac / rel)
    return rac


def envois_de(rac):
    return Path(rac) / O.DOSSIER_ENVOIS_REL


def ecrire_fiches(dossier, fs, fin=None, nom=None, run=RUN, contenu=None):
    """Copie scellée des fiches dans le dossier d'un run factice, et manifeste de fin scellé (forme du lanceur)."""
    d_run = racine_de(dossier) / "runs" / "course-ideation-conception-propre-v1" / run
    (d_run / "copies").mkdir(parents=True, exist_ok=True)
    p = d_run / "copies" / (nom or "sortie--fiches-validees.json")
    texte = contenu if contenu is not None else json.dumps(fs, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    p.write_text(texte, encoding="utf-8")
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    m = d_run / "manifeste-lanceur-fin.json"
    if not m.exists():
        bilan = {"code": 0, "issue": "fin propre",
                 "pour_l_attestation": {"fiches_validees_sha256": h}} if fin is None else fin(h)
        O.ecrire_scelle(m, json.dumps(bilan, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return p, h


def ecrire_attestation(dossier, sha, **change):
    a = {"lecteur": "mère (essai)", "lu_le": "2026-11-13T23:50Z", "fiches_validees_sha256": sha,
         "aucune_recette_aucun_secret": True, "envoi_au_lecteur_externe_permis": True}
    a.update(change)
    p = Path(dossier) / "attestation-lecture-g1-v1.json"
    O.ecrire_scelle(p, json.dumps(a, ensure_ascii=False))
    return p


PREP = {"effort": "medium", "palier": "standard", "plafond_usd": 11.0, "depense_anterieure_usd": 0.0}


def opreparer(pf, pa, sortie, rac, **change):
    return O.preparer(pf, pa, sortie, rac, **{**PREP, **change})


def preparer(tmp, fs=None, **change):
    fs = fiches_factices() if fs is None else fs
    pf, h = ecrire_fiches(tmp, fs)
    pa = ecrire_attestation(tmp, h)
    env = envois_de(racine_de(tmp))
    man = opreparer(pf, pa, env, racine_de(tmp), **change)
    return env, man


# --- lecteur simulé ------------------------------------------------------------------------------------------------------

CHAMP_PREUVE = {"R1": ("loi_predictive", "prediction"), "R2": ("loi_predictive", "metrique"), "R3": ("piege",),
                "R5": ("demande_organisme", "texte"), "R6": ("cosmetique_si",), "R7": ("enonce",)}


def valeurs_attendues(p):
    """Valeurs que le lecteur simulé « sain » rend pour une fiche de la pile."""
    if p["origine"] == "reelle":
        nom = p["vue"]["nom"].split()[2]
        return {**TOUT1, **PLAN[nom][4]}
    if p["famille"] == "hasard":
        return {**TOUT1, "R2": 0, "R7": 0}
    return {c: (0 if x is None else x) for c, x in p["attendu"].items()}


def passage(vue, c):
    if c == "R4":  # levier:juge : une phrase de la fiche (au moins 20 caractères), jamais l'étiquette seule
        return vue["demande_organisme"]["texte"][:150]
    o = vue
    for k in CHAMP_PREUVE[c]:
        o = o[k]
    return o[:150]


def entree_lue(p, vals, cat, alterer=()):
    e = {"etiquette": None}
    for c in O.CRITERES:
        if vals[c] == 1:
            pas = passage(p["vue"], c)
            if c in alterer:
                pas = pas[:-3] + "zzz"
            e[c] = {"valeur": 1, "passage": pas}
        else:
            e[c] = {"valeur": 0, "motif": "manque"}
    if vals["N"] == "aucune":
        e["N"] = {"valeur": "aucune"}
    else:
        pc = O.sans_gras(cat[vals["N"]][2])[:60]
        if "Nc" in alterer:
            pc = "passage qui n'est pas dans le catalogue"
        e["N"] = {"valeur": vals["N"], "passage_fiche": p["vue"]["enonce"][:60], "passage_catalogue": pc}
    return e


def texte_lot(env, L, k, modif=None):
    """Contenu que le lecteur simulé « sain » rend pour le lot k de la lecture L (bloc JSON de la consigne)."""
    pile = json.loads((env / O.PILE).read_text(encoding="utf-8"))
    cle = json.loads((env / O.CLE_LECTURES).read_text(encoding="utf-8"))
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    par_id = {p["id"]: p for p in pile["fiches"]}
    entrees = []
    for et in cle[L]["lots"][k - 1]:
        i = cle[L]["etiquettes"][et]
        vals, alt = valeurs_attendues(par_id[i]), ()
        if modif:
            vals, alt = modif(L, i, par_id[i], dict(vals))
        e = entree_lue(par_id[i], vals, cat, alt)
        e["etiquette"] = et
        entrees.append(e)
    return "```json\n" + json.dumps({"lecture": entrees}, ensure_ascii=False) + "\n```"


# --- doublure déclarée de l'API d'OpenAI ---------------------------------------------------------------------------------

CLE_FACTICE = "sk-essai-factice-NE-JAMAIS-ECRIRE-0123456789"
JETONS_SORTIE, JETONS_RAISON = 3000, 2000


class Doublure:
    """Doublure déclarée de `POST https://api.openai.com/v1/chat/completions` : vérifie l'adresse et l'en-tête, reconnaît
    le lot par l'empreinte du corps, rend la réponse du lecteur simulé, ou celle du scénario demandé pour le n-ième
    appel. Le palier servi suit celui que le corps demande (« flex », sinon « default »). Aucune connexion ouverte."""

    def __init__(self, env, scenarios=None, modif=None, contenu_lot=None, modele="gpt-6-astra", cle=CLE_FACTICE):
        self.env, self.scenarios, self.modif, self.contenu_lot = env, scenarios or {}, modif, contenu_lot
        self.modele, self.cle, self.appels, self.rendus = modele, cle, [], []
        man = json.loads((env / O.MANIFESTE).read_text(encoding="utf-8"))
        self.carte = {man["fichiers"][g["envoi"]]: (g["lecture"], g["lot"]) for g in man["garde_depense"]["envois"]}

    def __call__(self, url, entetes, corps, delai):
        assert url == O.URL_AMONT and delai == O.DELAI_S
        assert entetes == {"Content-Type": "application/json", "Authorization": "Bearer " + self.cle}
        h = hashlib.sha256(corps).hexdigest()
        self.appels.append(h)
        statut, rep = self.reponse(len(self.appels), h, corps)
        self.rendus.append(rep)
        return statut, rep

    def reponse(self, n, h, corps):
        sc = self.scenarios.get(n, "sain")
        if sc == "panne":
            raise TimeoutError(f"délai dépassé (mandataire ; en-tête Bearer {self.cle})")
        if sc == "panne_echappee":
            raise ValueError(f"Invalid header value {('Bearer ' + self.cle).encode()!r} {json.dumps(self.cle)}")
        if sc == "crash":
            raise KeyboardInterrupt
        if sc == "429":
            return 429, json.dumps({"error": {"message": "MESSAGE-ERREUR-AMONT : organisation org-SECRETORG42, clé sk-...wxyz",
                                              "type": "insufficient_quota", "code": "insufficient_quota"}}).encode()
        if sc == "429_identifiant":
            return 429, json.dumps({"error": {"message": "x", "type": "quota org-SECRETORG42",
                                              "code": "org-SECRETORG42"}}).encode()
        if sc == "erreur_chaine":
            return 502, b'{"error": "texte libre de la passerelle"}'
        if sc == "erreur_liste":
            return 502, b'{"error": ["a"]}'
        if sc == "corps_liste":
            return 502, b"[1, 2]"
        if sc == "illisible":
            return 200, b"<html>passerelle</html>"
        if sc == "trop_grand":
            return 200, b" " * (O.TAILLE_MAX_REPONSE + 1)
        L, k = self.carte[h]
        n_corps = len(corps)
        demande = json.loads(corps)
        usage = {"prompt_tokens": n_corps // 4, "completion_tokens": JETONS_SORTIE,
                 "total_tokens": n_corps // 4 + JETONS_SORTIE, "prompt_tokens_details": {"cached_tokens": 0},
                 "completion_tokens_details": {"reasoning_tokens": JETONS_RAISON}}
        texte = texte_lot(self.env, L, k, self.modif)
        if self.contenu_lot:
            texte = self.contenu_lot(L, k, texte)
        msg = {"role": "assistant", "content": texte, "refusal": None}
        r = {"id": f"chatcmpl-essai-{L}-{k}", "object": "chat.completion", "created": 1, "model": self.modele,
             "service_tier": "flex" if demande.get("service_tier") == "flex" else "default",
             "choices": [{"index": 0, "message": msg, "finish_reason": "stop"}], "usage": usage}
        if sc == "length":
            r["choices"][0]["finish_reason"], msg["content"] = "length", ""
            usage.update(completion_tokens=32768, total_tokens=n_corps // 4 + 32768)
            usage["completion_tokens_details"]["reasoning_tokens"] = 32765
        elif sc == "fin_lisible":
            r["choices"][0]["finish_reason"] = "length"
        elif sc == "palier_default":
            r["service_tier"] = "default"
        elif sc in ("content_filter", "tool_calls", "fin_absente"):
            r["choices"][0]["finish_reason"] = None if sc == "fin_absente" else sc
        elif sc == "modele":
            r["model"] = "gpt-6-astra-2026-11-01"
        elif sc == "majuscules":
            r["model"] = "GPT-6-ASTRA"
        elif sc == "sans_usage":
            del r["usage"]
        elif sc == "usage_incoherent":
            usage["completion_tokens_details"]["reasoning_tokens"] = JETONS_SORTIE + 1
        elif sc == "zeros":
            r["usage"] = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        elif sc == "un_jeton":
            r["usage"] = {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}
        elif sc == "total_sous_somme":
            usage["total_tokens"] = 5
        elif sc == "entree_sous_plancher":
            usage.update(prompt_tokens=n_corps // 32, total_tokens=n_corps // 32 + JETONS_SORTIE)
        elif sc == "sortie_sous_plancher":
            usage["completion_tokens_details"]["reasoning_tokens"] = JETONS_SORTIE
        elif sc == "cout_excessif":
            usage.update(prompt_tokens=10_000_000, total_tokens=10_000_000 + JETONS_SORTIE)
        elif sc == "refus":
            msg["refusal"] = "Je ne peux pas aider."
        elif sc == "cache":
            usage["prompt_tokens_details"]["cached_tokens"] = n_corps // 8
        elif sc == "vide":
            msg["content"] = ""
        elif sc == "deux_choix":
            r["choices"].append({"index": 1, "message": dict(msg), "finish_reason": "stop"})
        elif sc == "objet":
            r["object"] = "chat.completion.chunk"
        elif sc == "details_non_objets":
            usage["prompt_tokens_details"], usage["completion_tokens_details"] = [], "x"
        elif sc == "message_non_objet":
            r["choices"][0]["message"] = "texte nu"
        elif sc == "palier_autre":
            r["service_tier"] = "priority"
        elif sc == "echo_cle":
            r["model"] = self.cle
            r["echo"] = [self.cle, json.dumps(self.cle), self.cle.replace("/", "\\/")]
            msg["content"] = texte + "\n" + self.cle
        return 200, json.dumps(r, ensure_ascii=False).encode("utf-8")


def cout_sain(octets, cache=0):
    p = octets // 4
    return ((p - cache) * PRIX["entree"] + cache * PRIX["cache"] + JETONS_SORTIE * PRIX["sortie"]) / 1e6


def envoyer(env, monkeypatch, scenarios=None, modif=None, cle=CLE_FACTICE, **kw):
    monkeypatch.setenv("OPENAI_API_KEY", cle)
    d = Doublure(env, scenarios, modif, cle=cle)
    r = O.envoyer(env, transport=d, **kw)
    return r, d


def lire(env, modif=None, contenu_lot=None, modele="gpt-6-astra", scenarios=None):
    """Les deux lectures, envoyées par `envoyer` à la doublure (journal tenu) ; `modif(L, id, p, vals)` → (vals, alterer) ;
    `contenu_lot(L, k, texte)` → texte."""
    os.environ["OPENAI_API_KEY"] = CLE_FACTICE
    try:
        d = Doublure(env, scenarios, modif, contenu_lot, modele)
        return O.envoyer(env, transport=d)
    finally:
        os.environ.pop("OPENAI_API_KEY", None)


def deposer_sans_journal(env, modif=None, contenu_lot=None, modele="gpt-6-astra"):
    """Réponses scellées déposées à la main, sans `envoyer` ni journal (forme de la v3) : artefact de M1."""
    cle = json.loads((env / O.CLE_LECTURES).read_text(encoding="utf-8"))
    for L in O.LECTURES:
        for k, _ in enumerate(cle[L]["lots"], 1):
            texte = texte_lot(env, L, k, modif)
            if contenu_lot:
                texte = contenu_lot(L, k, texte)
            r = {"id": f"essai-{L}-{k}", "object": "chat.completion", "model": modele, "service_tier": "default",
                 "choices": [{"index": 0, "message": {"role": "assistant", "content": texte}, "finish_reason": "stop"}],
                 "usage": {"prompt_tokens": 20000, "completion_tokens": 3000, "total_tokens": 23000}}
            O.ecrire_scelle(env / f"reponse-{L}-lot{k}-{O.SUFFIXE}.json", json.dumps(r, ensure_ascii=False))


def tous_les_octets(dossier):
    return b"".join(p.read_bytes() for p in Path(dossier).rglob("*") if p.is_file())


def id_de(nom):
    aut, *_ = PLAN[nom]
    k = list(PLAN).index(nom) + 1
    return f"{aut}-p{1 + k % 2}-{k:02d}"


def classer(env, **kw):
    return K.classement(env, O.racine_du_dossier(env), **kw)[0]


def resceller(p, texte):
    """Réécrit un fichier et son compagnon (artefact : manifeste ou pièce rescellés à la main)."""
    p = Path(p)
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    O.ecrire_scelle(p, texte)


# --- boucle locale (transport réel sans réseau) --------------------------------------------------------------------------

MANDATAIRES = ("http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY", "all_proxy", "ALL_PROXY", "no_proxy",
               "NO_PROXY")


def monter_boucle_locale():
    """Monte `lo` dans l'espace de noms réseau courant (SIOCGIFFLAGS, SIOCSIFFLAGS), comme les sondes du contre-lecteur."""
    import fcntl
    import struct
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nom = struct.pack("16sH14s", b"lo", 0, b"")
    drapeaux = struct.unpack("16sH14s", fcntl.ioctl(s, 0x8913, nom))[1]
    fcntl.ioctl(s, 0x8914, struct.pack("16sH14s", b"lo", drapeaux | 1, b""))
    s.close()


def serveur(gestion):
    class G(http.server.BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def do_POST(self):
            self.corps_recu = self.rfile.read(int(self.headers.get("Content-Length") or 0))
            gestion(self)

        do_GET = do_POST
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), G)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s


@pytest.fixture
def boucle(monkeypatch):
    """Boucle locale utilisable (montée si elle est éteinte, sous `unshare -n`) et aucun mandataire dans l'environnement."""
    for v in MANDATAIRES:
        monkeypatch.delenv(v, raising=False)
    s = serveur(lambda h: (h.send_response(204), h.end_headers()))
    try:
        socket.create_connection(s.server_address, 2).close()
    except OSError:
        monter_boucle_locale()
        socket.create_connection(s.server_address, 2).close()
    finally:
        s.shutdown()
    serveurs = []

    def ouvrir(gestion):
        srv = serveur(gestion)
        serveurs.append(srv)
        return srv
    yield ouvrir
    for srv in serveurs:
        srv.shutdown()


def amont_local(monkeypatch, srv):
    """Détourne l'adresse d'amont vers un serveur de la boucle locale, en mémoire seulement (restaurée après l'essai)."""
    url = f"http://127.0.0.1:{srv.server_address[1]}/v1/chat/completions"
    monkeypatch.setattr(O, "URL_AMONT", url)
    return url


# --- essais : préparation ------------------------------------------------------------------------------------------------

def test_normalisation_egale_a_celle_de_l_orchestrateur():
    if not CLONE.is_file():
        pytest.skip("clone de l'orchestrateur absent")
    arbre = ast.parse(CLONE.read_text(encoding="utf-8"))
    fn = next(n for n in arbre.body if isinstance(n, ast.FunctionDef) and n.name == "normaliser_typographie")
    ns = {}
    exec("import re\n" + ast.get_source_segment(CLONE.read_text(encoding="utf-8"), fn), ns)
    for s in ["« a »  b c d — e – f … “g” ‘h’ i\t\tj", "rien", "x  \n  y"]:
        assert ns["normaliser_typographie"](s) == O.normaliser_typographie(s)


def test_preparer_sain_aveugle_et_borne(tmp_path):
    env, man = preparer(tmp_path)
    assert man["pile"]["fiches"] == 28 and man["pile"]["reelles_admissibles"] == 8 and man["pile"]["temoins"] == 20
    assert man["pile"]["hors_question"] == 3 and man["pile"]["champs_retires"] == {}
    pile = json.loads((env / "pile-interne-v3-2.json").read_text(encoding="utf-8"))
    motifs = sorted(h["motif"] for h in pile["hors_question"])
    assert motifs[0].startswith("0 étiquette") and motifs[1].startswith("2 étiquette") and "rien" in motifs[2]
    assert man["lots"]["tailles"] == [5, 5, 5, 5, 4, 4] and man["garde_depense"]["appels_max"] == 12
    assert man["lots"]["taille_lot"] == 5 and man["lecteur"]["max_completion_tokens"] == 32768
    assert man["lecteur"]["reasoning_effort"] == "medium" and man["lecteur"]["url"] == "https://api.openai.com/v1/chat/completions"
    assert man["lecteur"]["variable_cle"] == "OPENAI_API_KEY" and man["garde_depense"]["plafond_usd"] == 11.0
    for g in man["garde_depense"]["envois"]:
        assert abs(g["pire_cas_usd"] - ((g["octets"] + 1024) * 10 / 1e6 + 32768 * 50 / 1e6)) < 1e-6
    assert man["ordre_d_envoi"][0] == "envoi-L1-lot1-v3-2.corps.json" and len(man["ordre_d_envoi"]) == 12
    cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
    assert cle["L1"]["ordre"] != cle["L2"]["ordre"] and sorted(cle["L1"]["ordre"]) == sorted(cle["L2"]["ordre"])
    consigne = O.lire_piece(RACINE, "consigne")[0]
    catalogue = O.lire_piece(RACINE, "catalogue")[0]
    fs = fiches_factices()
    secrets = [f["identifiant_auteur"] for f in fs] + [f["empreinte"] for f in fs] + ['"auteur"', '"passe"', '"temoin"',
               '"famille"', '"attendu"', "T2-V", "T2-C2", "T2-H1", "propa-p", "propb-p", "propc-p", "«", "»", "’"]
    vus = []
    for L in O.LECTURES:
        for k in range(1, 7):
            msg = (env / f"envoi-{L}-lot{k}-v3-2.txt").read_text(encoding="utf-8")
            assert msg.startswith(consigne.rstrip("\n")) and catalogue.rstrip("\n") in msg
            bloc = msg.split("```json\n")[-1].rsplit("\n```", 1)[0]
            lot = json.loads(bloc)
            assert [x["etiquette"] for x in lot] == cle[L]["lots"][k - 1]
            for x in lot:
                assert list(x["fiche"]) == [c for c, _ in O.ORDRE_VUE]
                vus.append(x["fiche"]["nom"])
                assert not any(s in json.dumps(x["fiche"], ensure_ascii=False) for s in secrets)
            corps = json.loads((env / f"envoi-{L}-lot{k}-v3-2.corps.json").read_text(encoding="utf-8"))
            assert corps["model"] == "gpt-6-astra" and corps["messages"][0]["content"] == msg
            assert corps == {"model": "gpt-6-astra", "messages": [{"role": "user", "content": msg}],
                             "max_completion_tokens": 32768, "reasoning_effort": "medium", "store": False}
    assert len(vus) == 56 and len(set(vus)) == 28
    etiq = [e for lot in cle["L1"]["lots"] for e in lot]
    assert etiq == [f"F{i:02d}" for i in range(1, 29)]
    for nom in man["fichiers"]:
        O.verifier_sceau(env / nom)


def test_ordres_par_seedsequence_consignee(tmp_path):
    env, man = preparer(tmp_path)
    pile = json.loads((env / "pile-interne-v3-2.json").read_text(encoding="utf-8"))
    cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
    e = np.random.SeedSequence(2026111302).spawn(4)
    for j, L in enumerate(("L1", "L2")):
        perm = np.random.default_rng(e[j]).permutation(len(pile["fiches"]))
        assert cle[L]["ordre"] == [pile["fiches"][int(i)]["id"] for i in perm]
    assert man["graines"]["enfants"] == {"ordre_L1": [0], "ordre_L2": [1], "departage": [2], "temoin_permute": [3]}


def test_preparer_reproductible(tmp_path):
    a, _ = preparer(tmp_path / "a")
    b, _ = preparer(tmp_path / "b")
    for n in ("envoi-L1-lot1-v3-2.txt", "envoi-L2-lot2-v3-2.corps.json", "cle-lectures-v3-2.json"):
        assert (a / n).read_bytes() == (b / n).read_bytes()


@pytest.mark.parametrize("cas", ["absente", "mauvaise_empreinte", "envoi_non_permis", "recette", "non_scellee",
                                 "champ_manquant", "lecteur_vide"])
def test_attestation_fautive_refusee(tmp_path, cas):
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    if cas == "absente":
        pa = tmp_path / "rien.json"
    elif cas == "non_scellee":
        pa = tmp_path / "att.json"
        pa.write_text(json.dumps({"lecteur": "x", "lu_le": "y", "fiches_validees_sha256": h,
                                  "aucune_recette_aucun_secret": True, "envoi_au_lecteur_externe_permis": True}))
    elif cas == "champ_manquant":
        pa = tmp_path / "att.json"
        O.ecrire_scelle(pa, json.dumps({"lecteur": "x", "fiches_validees_sha256": h}))
    else:
        change = {"mauvaise_empreinte": {"fiches_validees_sha256": "0" * 64},
                  "envoi_non_permis": {"envoi_au_lecteur_externe_permis": "oui"},
                  "recette": {"aucune_recette_aucun_secret": False}, "lecteur_vide": {"lecteur": " "}}[cas]
        pa = ecrire_attestation(tmp_path, h, **change)
    with pytest.raises(O.Refus):
        opreparer(pf, pa, envois_de(racine_de(tmp_path)), racine_de(tmp_path))
    assert not (envois_de(racine_de(tmp_path))).exists()


def test_fiches_non_scellees_ou_alterees_refusees(tmp_path):
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    pf.write_text(pf.read_text(encoding="utf-8").replace("Idée factice A1", "Idée factice A9"), encoding="utf-8")
    with pytest.raises(O.Refus):
        opreparer(pf, pa, envois_de(racine_de(tmp_path)), racine_de(tmp_path))
    Path(str(pf) + ".sha256").unlink()
    with pytest.raises(O.Refus):
        opreparer(pf, pa, envois_de(racine_de(tmp_path)), racine_de(tmp_path))


@pytest.mark.parametrize("piece", ["consigne", "prix"])
def test_piece_epinglee_alteree_refusee(tmp_path, piece):
    for cas in ("a", "b"):  # deux racines : une seule préparation par racine (C6)
        rac = racine_de(tmp_path / cas)
        pf, h = ecrire_fiches(tmp_path / cas, fiches_factices())
        pa = ecrire_attestation(tmp_path / cas, h)
        if cas == "a":
            opreparer(pf, pa, envois_de(rac), rac)  # copie conforme : passe
            continue
        rel = O.PIECES[piece][0] if piece in O.PIECES else O.PIECES_PRIX[piece][0]
        p = rac / rel
        p.write_text(p.read_text(encoding="utf-8") + " ", encoding="utf-8")
        with pytest.raises(O.Refus, match="empreinte"):
            opreparer(pf, pa, envois_de(rac), rac)
        assert not envois_de(rac).exists()


def test_ecriture_scellee_jamais_ecrasee(tmp_path):
    p = tmp_path / "x.json"
    h = O.ecrire_scelle(p, "a")
    assert O.verifier_sceau(p) == h
    with pytest.raises(O.Refus):
        O.ecrire_scelle(p, "b")
    assert p.read_text() == "a"


def test_sortie_non_vide_refusee(tmp_path):
    (envois_de(racine_de(tmp_path))).mkdir(parents=True)
    (envois_de(racine_de(tmp_path)) / "x").write_text("x")
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    with pytest.raises(O.Refus):
        opreparer(pf, pa, envois_de(racine_de(tmp_path)), racine_de(tmp_path))


def test_garde_appels_fixes_d_avance(tmp_path):
    """Sain : 25 fiches réelles + 20 témoins = 45 → 9 lots, 18 appels. Artefact : 46 → 10 lots, 20 appels > 18 : refus."""
    plan = {f"B{i}": ("propa", "levier:cout", "ajout", "processeur", {}) for i in range(26)}
    with pytest.raises(O.Refus, match="appels"):
        preparer(tmp_path / "a", fiches_factices(plan, hors=False))
    assert not (envois_de(racine_de(tmp_path / "a"))).exists()
    plan = {f"B{i}": ("propa", "levier:cout", "ajout", "processeur", {}) for i in range(25)}
    _, man = preparer(tmp_path / "b", fiches_factices(plan, hors=False))
    assert man["garde_depense"]["appels_max"] == 18 and man["lots"]["tailles"] == [5] * 9
    assert O.MAX_APPELS == 18 and O.TAILLE_LOT == 5


def test_lots_de_cinq_pour_la_pile_reelle():
    """43 fiches (pile de R-2645) : 9 lots, sept de 5 et deux de 4, consécutifs, sans trou ni recouvrement."""
    lots = O.decouper_lots(43)
    assert [len(x) for x in lots] == [5] * 7 + [4] * 2 and sum(lots, []) == list(range(43))
    assert [len(x) for x in O.decouper_lots(28)] == [5, 5, 5, 5, 4, 4] and O.decouper_lots(0) == []


@pytest.mark.parametrize("change,motif", [
    ({}, None),
    ({"effort": "max"}, "effort"), ({"effort": None}, "effort"),
    ({"palier": "fast"}, "palier"), ({"palier": None}, "palier"),
    ({"depense_anterieure_usd": -0.01}, "antérieure"), ({"depense_anterieure_usd": float("nan")}, "antérieure"),
    ({"depense_anterieure_usd": None}, "antérieure"),
    ({"plafond_usd": 11.66}, "GO-2026-11-13-06"), ({"plafond_usd": float("inf")}, "plafond"),
    ({"plafond_usd": 10.9, "depense_anterieure_usd": 1.0}, "antérieure"),
    ({"plafond_usd": 1.0}, "aucun appel"),
])
def test_garde_preparation_plafond_effort_palier(tmp_path, change, motif):
    if motif is None:
        _, man = preparer(tmp_path, **change)
        g = man["garde_depense"]
        assert g["prix_usd_par_million"] == {"entree": 10.0, "cache": 1.0, "sortie": 50.0, "source": O.SOURCE_PRIX}
        assert g["appels_surs_au_pire_cas"] == 5  # 11 USD paient cinq pires cas d'environ 2,0
        assert g["depense_anterieure_usd"] == 0.0 and g["plafond_disponible_usd"] == 11.65 and man["palier"] == "standard"
        assert "SUPPOSÉ" not in O.SOURCE_PRIX and "barème" not in O.SOURCE_PRIX and "08:45:38Z" in O.SOURCE_PRIX
        return
    with pytest.raises(O.Refus, match=motif):
        preparer(tmp_path, **change)
    assert not envois_de(racine_de(tmp_path)).exists()


def test_ordres_identiques_a_la_v2():
    """Régénération déterministe : mêmes ordres et mêmes étiquettes que l'outil v2 (seuls les lots changent)."""
    spec = importlib.util.spec_from_file_location("outil_v2_ref", ICI.parents[1] / "lecture-classement-v2" /
                                                  "outil_lecteur_conception_propre_v2.py")
    v2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v2)
    for n in (28, 43):
        assert O.ordres_lectures(n) == v2.ordres_lectures(n)
    assert v2.TAILLE_LOT == 20 and O.ENTROPIE_ORDRES == v2.ENTROPIE_ORDRES


def test_champs_hors_gabarit_retires_et_consignes(tmp_path):
    fs = fiches_factices()
    fs[0]["citations_verifiees"] = [{"citation": "c", "verifiee": True}]
    fs[0]["anteriorite"][0]["non_opposable"] = True
    env, man = preparer(tmp_path, fs)
    assert man["pile"]["champs_retires"] == {fs[0]["identifiant_auteur"]: ["anteriorite[0].non_opposable",
                                                                          "citations_verifiees"]}
    for f in (env).glob("envoi-*.txt"):
        assert "citations_verifiees" not in f.read_text(encoding="utf-8")


# --- essais : vérification et classement -------------------------------------------------------------------------------

def test_classement_sain(tmp_path):
    """Règle v2 : portes R2, R3 ; S v2 avec R7 ; L3 v2 ; L5 v2 et séparation ; aucune désignation."""
    env, _ = preparer(tmp_path)
    lire(env)
    r = classer(env)
    assert r["lisible"] and r["L5"]["rejet"] and r["verdict"].startswith("classement exploratoire lisible")
    assert r["separation"]["issue"] == "séparation réelle (portée par R7)" and r["separation"]["lu"]
    assert r["designees"] == [] and "aucune idée désignée" in r["verdict"]
    for L in ("L1", "L2"):
        assert all(x == 0 for x in r["non_prouves"][L].values()) and r["anomalies"][L] == []
    st = r["rang_exploratoire"]["statut"]
    assert st[id_de("A4")] == {"statut": "neuve", "S": 4}  # R7 = 0 : plus une porte, un point de moins
    assert st[id_de("A6")]["motif"] == "porte(s) R2" and st[id_de("A5")] == {"statut": "occupee", "entrees": "C8"}
    reelles = [id_de(n) for n in PLAN]
    tirage = np.random.default_rng(np.random.SeedSequence(2026111302).spawn(4)[2]).permutation(8)
    rang = {reelles[int(j)]: k for k, j in enumerate(tirage)}
    assert r["rang_exploratoire"]["departage"] == rang
    a2, a7 = sorted([id_de("A2"), id_de("A7")], key=rang.get)
    a3, a4 = sorted([id_de("A3"), id_de("A4")], key=rang.get)
    assert r["rang_exploratoire"]["ordre_neuves"] == [id_de("A1"), a2, a7, a3, a4, id_de("A8")]
    assert r["rang_exploratoire"]["deux_premieres"] == [id_de("A1"), a2]
    assert id_de("A4") not in r["rang_exploratoire"]["restreint_a_R7_retenu_1"]
    assert r["L1"]["reconnues"] == 7 and r["L2"]["tient"] and r["L3"]["tient"] and r["L4"]["tient"]
    assert r["L5"]["C_reelles"] == dict(zip(reelles, [6, 6, 5, 5, 0, 0, 6, 5]))
    assert set(r["L5"]["C_hasard"].values()) == {0}
    assert abs(r["L5"]["test"]["p"] - 45 / 12870) < 0.002
    assert abs(r["separation"]["test_R7_seul"]["p"] - 9 / 12870) < 0.001
    assert r["echecs"] == {"E1": False, "E2_v2": False, "E2_v2_lecture_incomplete": False, "E3_v2": False,
                           "E4_v2": False, "E5": False}
    assert r["lecture_complete"]["complete"] and "variante_detachee" not in r and "regle_de_designation" not in r
    assert r["audit_proprete"]["declenche"] and r["audit_proprete"]["toutes_publiees_reconnues"]
    for L in ("L1", "L2"):
        assert all(d["justes"] == d["sur"] for d in r["exactitude_lecteur"][L].values())
    perm = np.random.default_rng(np.random.SeedSequence(2026111302).spawn(4)[3]).permutation(8)
    vec = {i: r["retenu"][i] for i in reelles}
    cout = {id_de(n): PLAN[n][3] for n in PLAN}
    vp = {reelles[i]: vec[reelles[int(perm[i])]] for i in range(8)}
    cp = {reelles[i]: cout[reelles[int(perm[i])]] for i in range(8)}
    neuves = [i for i in reelles if all(vp[i][c] == 1 for c in ("R2", "R3")) and vp[i]["N"] == "aucune"]
    neuves.sort(key=lambda i: (-(vp[i]["R1"] + vp[i]["R4"] + vp[i]["R5"] + vp[i]["R6"] + vp[i]["R7"]),
                               {"processeur": 0, "depense": 1}[cp[i]], rang[i]))
    assert r["temoin_score_permute"]["deux_premieres"] == neuves[:2]
    cpp = r["comptes_par_proposeur"]
    assert cpp["propa"]["admissibles"] == 3 and cpp["propa"]["hors_question"] == 1 and "designees" not in cpp["propa"]
    assert len(r["descriptif_holm"]) == 8 and all("p_holm" in d for d in r["descriptif_holm"])
    r7 = next(d for d in r["descriptif_holm"] if d["critere"] == "R7")
    assert r7["difference"] > 0 and r7["p_holm"] >= r7["p_brute"]
    assert r["relecture_contre_premiere_lecture"] == {"fiches_communes": 0}  # fiches factices : aucune commune
    assert r["regle_v2_sur_la_premiere_lecture"] == {"fiches_communes": 0}
    h = r["hasard_R7_selon_la_chaine"]
    assert len(h["chaine_coherente"]) == 6 and len(h["chaine_contraire"]) == 2


def test_citation_alteree_compte_zero(tmp_path):
    env, _ = preparer(tmp_path)
    a1 = id_de("A1")
    lire(env, modif=lambda L, i, p, v: (v, ("R1",) if (L == "L1" and i == a1) else ()))
    r = classer(env)
    assert r["non_prouves"]["L1"]["R1"] == 1 and r["non_prouves"]["L2"]["R1"] == 0
    assert r["retenu"][a1]["R1"] == 0 and r["designees"] == []
    assert r["rang_exploratoire"]["statut"][a1] == {"statut": "neuve", "S": 4}


def test_espaces_normalises_seulement():
    vue = {"enonce": "un  texte suffisamment long\navec   des espaces", "x": ["autre champ de la fiche factice"]}
    assert O.passage_dans("un texte suffisamment long avec des", O.feuilles(vue))[0]
    assert not O.passage_dans("un texte, suffisamment long avec des", O.feuilles(vue))[0]
    assert not O.passage_dans("Un texte suffisamment long avec", O.feuilles(vue))[0]
    assert not O.passage_dans("avec des espaces autre champ", O.feuilles(vue))[0]  # à cheval sur deux champs
    assert not O.passage_dans("   ", O.feuilles(vue))[0] and not O.passage_dans(None, O.feuilles(vue))[0]
    vue2 = {"enonce": 'il dit "oui" puis répète a\\b sans fin'}
    assert O.passage_dans('il dit \\"oui\\" puis répète', O.feuilles(vue2))[0]  # recopié de la vue JSON, échappé
    assert O.passage_dans('dit "oui" puis répète a\\b', O.feuilles(vue2))[0]
    assert O.passage_dans('puis répète a\\\\b sans fin', O.feuilles(vue2))[0]
    assert not O.passage_dans('il dit \\"non\\" puis répète', O.feuilles(vue2))[0]


def test_M1_passages_triviaux_refuses():
    """M1 : « e », « + », « . », une étiquette de levier, « C7 », « 2026 » ne prouvent rien ; 20 caractères hors espaces."""
    vue = {"enonce": "e + . levier:juge C7 2026 et une phrase assez longue pour prouver quelque chose", "s": "+"}
    for triv in ("e", "+", ".", "levier:juge", "C7", "2026", "une phrase assez", "  e  +  .  "):
        ok, motif = O.passage_dans(triv, O.feuilles(vue))
        assert not ok and ("trop court" in motif or "vide" in motif), triv
    assert O.passage_dans("une phrase assez longue pour", O.feuilles(vue))[0]
    assert not O.court("abcdefghij klmnopqrst") and O.court("abcdefghij klmnopqrs")  # 20 contre 19 hors espaces
    assert O.LONGUEUR_MIN_PASSAGE == 20


def test_M1_occupation_par_le_mecanisme_de_Ck_seulement():
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    vue, _ = O.vue_lecteur(fiche("Z", "propa", 1, 1, "levier:cout"))
    pf = vue["enonce"][:60]
    meca7 = O.sans_gras(cat["C7"][2])
    bons = {"valeur": "C7", "passage_fiche": pf, "passage_catalogue": meca7[:80]}
    assert O.verifier_entree({"N": bons}, vue, False, cat)["N"]["compte"] == "C7"
    for pc in ("C7", "2026", "PACE (arXiv 2606.08106v1, 2026)", "`docs/sources/pdf/2606.08106v1.pdf`",
               O.sans_gras(cat["C2"][2])[:80], "e", "+"):
        r = O.verifier_entree({"N": {**bons, "passage_catalogue": pc}}, vue, False, cat)["N"]
        assert r["compte"] == "aucune" and r["occupation_non_prouvee"], pc
    for pfx in ("Z", "e", "passage qui n'est pas dans la fiche factice", None):  # passage de la fiche exigé
        r = O.verifier_entree({"N": {**bons, "passage_fiche": pfx}}, vue, False, cat)["N"]
        assert r["compte"] == "aucune" and r["occupation_non_prouvee"], pfx


def test_M1_passages_courts_comptes_et_rapportes(tmp_path):
    env, _ = preparer(tmp_path)
    a1 = id_de("A1")

    def contenu(L, k, texte):
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
        for e in o["lecture"]:
            if cle[L]["etiquettes"][e["etiquette"]] == a1 and L == "L1":
                e["R1"]["passage"] = "+"
        return "```json\n" + json.dumps(o, ensure_ascii=False) + "\n```"
    lire(env, contenu_lot=contenu)
    r = classer(env)
    assert r["passages_courts_refuses"]["L1"]["R1"] == 1 and r["passages_courts_refuses"]["L2"]["R1"] == 0
    assert r["retenu"][a1]["R1"] == 0
    md = K.resume_md(r)
    assert "Passages courts refusés" in md and "L1 : 1" in md


def test_lectures_discordantes(tmp_path):
    env, _ = preparer(tmp_path)
    a2, a7, a1 = id_de("A2"), id_de("A7"), id_de("A1")

    def m(L, i, p, v):
        if L == "L2" and i == a2:
            v["R7"] = 0
        if L == "L2" and i == a7:
            v["N"] = "C4"
        if L == "L1" and i == a1:
            v["R5"] = 0
        return v, ()
    lire(env, modif=m)
    r = classer(env)
    st = r["rang_exploratoire"]["statut"]
    assert st[a2] == {"statut": "neuve", "S": 4} and st[a7] == {"statut": "occupee", "entrees": "C4"}
    assert st[a1] == {"statut": "neuve", "S": 4}  # un seul 0 suffit à retirer le point (valeur retenue)
    assert a2 not in r["rang_exploratoire"]["restreint_a_R7_retenu_1"] and a1 in r["rang_exploratoire"]["restreint_a_R7_retenu_1"]
    assert r["designees"] == []


def test_occupation_non_prouvee_compte_aucune(tmp_path):
    env, _ = preparer(tmp_path)
    a7 = id_de("A7")

    def m(L, i, p, v):
        if i == a7:
            v["N"] = "C4"
            return v, ("Nc",)
        return v, ()
    lire(env, modif=m)
    r = classer(env)
    assert r["non_prouves"]["L1"]["N_occupation_non_prouvee"] == 1
    assert r["rang_exploratoire"]["statut"][a7]["statut"] == "neuve"


@pytest.mark.parametrize("manquees,tient", [(2, True), (3, False)])
def test_temoins_publies_non_reconnus_L1(tmp_path, manquees, tient):
    env, _ = preparer(tmp_path)
    cibles = ["T2-C2", "T2-C1", "T2-C3"][:manquees]
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "aucune"} if i in cibles else v, ()))
    r = classer(env)
    assert r["L1"]["reconnues"] == 7 - manquees and r["L1"]["tient"] is tient
    assert r["lisible"] is tient and r["designees"] == []
    if not tient:
        assert r["echecs"]["E2_v2"] and r["verdict"].startswith("E2 v2") and r["rang_exploratoire"]["ordre_neuves"]


def test_publiee_reconnue_dans_une_seule_lecture_suffit_a_L1(tmp_path):
    env, _ = preparer(tmp_path)
    cibles = ["T2-C2", "T2-C1", "T2-C3"]
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "aucune"} if (i in cibles and L == "L2") else v, ()))
    r = classer(env)
    assert r["L1"]["reconnues"] == 7 and r["L1"]["tient"]
    # la mauvaise entrée ne compte pas
    env2, _ = preparer(tmp_path / "b")
    lire(env2, modif=lambda L, i, p, v: ({**v, "N": "C12"} if i in cibles else v, ()))
    assert classer(env2)["L1"]["reconnues"] == 4


@pytest.mark.parametrize("prouve", [True, False])
def test_fausse_fiche_acceptee_L2(tmp_path, prouve):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R3": 1}, () if prouve else ("R3",)) if (i == "T2-F3" and L == "L2")
         else (v, ()))
    r = classer(env)
    assert r["L2"]["tient"] is (not prouve) and r["lisible"] is (not prouve)


def test_vrai_ou_jumeau_rejete_L3(tmp_path):
    """L3 v2 : une seule lecture à R7 = 1 suffit ; aucune ne suffit pas ; une porte ou une occupation fait manquer L3."""
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 0} if (i == "T2-J" and L == "L1") else v, ()))
    r = classer(env)
    assert r["L3"]["tient"] and r["L3"]["par_temoin"]["T2-J"]["R7_prouve_par"] == ["L2"]
    env2, _ = preparer(tmp_path / "b")
    lire(env2, modif=lambda L, i, p, v: ({**v, "R7": 0} if i == "T2-J" else v, ()))
    r2 = classer(env2)
    assert not r2["L3"]["tient"] and r2["L3"]["par_temoin"]["T2-J"]["R7_prouve_par"] == []
    assert r2["designees"] == [] and r2["echecs"]["E2_v2"] and "L3 v2" in r2["verdict"]
    env3, _ = preparer(tmp_path / "c")
    lire(env3, modif=lambda L, i, p, v: ({**v, "N": "C3"} if (i == "T2-V" and L == "L2") else v, ()))
    assert not classer(env3)["L3"]["tient"]
    env4, _ = preparer(tmp_path / "d")
    lire(env4, modif=lambda L, i, p, v: ({**v, "R3": 0} if (i == "T2-V" and L == "L1") else v, ()))
    r4 = classer(env4)
    assert not r4["L3"]["tient"] and r4["L3"]["par_temoin"]["T2-V"]["portes_manquantes"] == ["R3"]
    env5, _ = preparer(tmp_path / "e")
    lire(env5, modif=lambda L, i, p, v: (v, ("R7",)) if i == "T2-V" else (v, ()))  # R7 rendu 1 mais non prouvé
    assert not classer(env5)["L3"]["tient"]


def test_lectures_trop_discordantes_L4(tmp_path):
    env, _ = preparer(tmp_path)
    pile = json.loads((env / "pile-interne-v3-2.json").read_text(encoding="utf-8"))
    bascule = {p["id"] for k, p in enumerate(pile["fiches"]) if k % 2 == 0}
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 1 - v["R7"]} if (i in bascule and L == "L2") else v, ()))
    r = classer(env)
    assert not r["L4"]["R7"]["tient"] and r["L4"]["R7"]["jugee_sur"] == "kappa" and not r["lisible"]


def test_kappa_et_marge_constante():
    k = K.kappa_accord([1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0])
    assert k["kappa"] == 1 and k["tient"]
    k = K.kappa_accord([1, 0, 1, 0], [1, 1, 0, 0])
    assert abs(k["kappa"]) < 1e-12 and not k["tient"]
    k = K.kappa_accord([1, 1, 1, 0, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1])
    assert abs(k["kappa"] - (0.9 - 0.74) / 0.26) < 1e-9 and k["tient"]
    k = K.kappa_accord([1] * 10, [1] * 9 + [0])  # une marge constante : accord brut 0,9 ≥ 0,8
    assert k["marge_constante"] and k["tient"] and k["kappa"] == 0
    k = K.kappa_accord([1] * 10, [1] * 7 + [0] * 3)
    assert k["marge_constante"] and not k["tient"]
    k = K.kappa_accord([0] * 6, [0] * 6)
    assert k["kappa"] is None and k["tient"]


def test_L5_non_rejetee_pas_de_separation(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R2": 0} if p["origine"] == "reelle" else v, ()))
    r = classer(env)
    assert r["lisible"] and not r["L5"]["rejet"] and r["L5"]["test"]["p"] == 1.0
    assert r["separation"]["issue"] == "pas de séparation" and not r["separation"]["lu"]
    assert r["designees"] == [] and r["echecs"]["E3_v2"] and "pas de séparation" in r["verdict"]


def test_L5_hasard_aussi_bon_non_rejetee(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**TOUT1} if p["famille"] == "hasard" else v, ()))
    r = classer(env)
    assert not r["L5"]["rejet"] and r["designees"] == [] and r["separation"]["issue"] == "pas de séparation"
    assert not r["audit_proprete"]["aucune_idee_au_hasard_passee"]


def test_une_seule_neuve_L5_ne_peut_rejeter_et_E5(tmp_path):
    """Une seule neuve parmi n réelles : p ≥ n / (n + 8) > 0,05 ; E4 v2 (moins de deux neuves) est rapporté."""
    env, _ = preparer(tmp_path)
    garde = id_de("A1")
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C10"} if (p["origine"] == "reelle" and i != garde) else v, ()))
    r = classer(env)
    assert r["rang_exploratoire"]["ordre_neuves"] == [garde] and r["rang_exploratoire"]["deux_premieres"] == [garde]
    assert not r["L5"]["rejet"] and abs(r["L5"]["test"]["p"] - 0.5) < 0.01 and r["designees"] == []
    assert r["echecs"]["E3_v2"] and r["echecs"]["E4_v2"]
    assert r["echecs"]["E5"]  # 6 occupées sur 7 passées > 80 %


def test_E4_v2_moins_de_deux_neuves():
    cl = K.classer(["a", "b"], {"a": {**TOUT1}, "b": {**TOUT1, "R2": 0}}, {"a": "depense", "b": "processeur"},
                   {"a": 1, "b": 0})
    assert cl["ordre_neuves"] == ["a"] and cl["deux_premieres"] == ["a"]


def test_permutation_contre_enumeration_exacte():
    from itertools import combinations
    x, y = [3, 5, 0, 4], [0, 1, 0]
    z = x + y
    obs = np.mean(x) - np.mean(y)
    stats = [np.mean([z[i] for i in c]) - np.mean([z[i] for i in range(7) if i not in c])
             for c in combinations(range(7), 4)]
    exact = np.mean([s >= obs - 1e-12 for s in stats])
    exact2 = np.mean([abs(s) >= abs(obs) - 1e-12 for s in stats])
    t = K.test_permutation(x, y, np.random.SeedSequence(7), 100_000)
    assert abs(t["p"] - exact) < 0.005
    t2 = K.test_permutation(x, y, np.random.SeedSequence(7), 100_000, bilateral=True)
    assert abs(t2["p"] - exact2) < 0.005
    t3 = K.test_permutation(y, x, np.random.SeedSequence(7), 20_000)
    assert t3["p"] > 0.9
    assert K.test_permutation([], [1], np.random.SeedSequence(1))["p"] is None
    t4 = K.test_permutation([1] * 10, [0] * 10, np.random.SeedSequence(3), 20_000)  # p exacte 1/184 756
    assert t4["depassements"] == 0 and t4["p"] == 1 / 20_001
    assert t["p"] == (1 + t["depassements"]) / (1 + t["permutations"])
    assert K.PERMUTATIONS == 100_000 and K.SEUIL_P == 0.05 and K.ENTROPIE_TEST == 2026111303


def test_holm():
    adj = K.holm([0.01, 0.04, 0.03, 0.005])
    assert np.allclose(adj, [0.03, 0.06, 0.06, 0.02])
    assert K.holm([0.5, 0.9]) == [1.0, 1.0]


def test_reponses_fautives(tmp_path):
    env, _ = preparer(tmp_path)
    cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
    oter, doubler = cle["L1"]["lots"][0][0], cle["L1"]["lots"][0][1]

    def contenu(L, k, texte):
        if L == "L1" and k == 2:
            return "Voici ma lecture : pas de JSON ici."
        if L == "L1" and k == 1:
            o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
            par = {e["etiquette"]: e for e in o["lecture"]}
            o["lecture"] = [e for e in o["lecture"] if e["etiquette"] != oter] + [par[doubler],
                                                                                 {"etiquette": "F99"}]
            o["lecture"][2], o["lecture"][3] = o["lecture"][3], o["lecture"][2]
            return json.dumps(o)
        return texte
    lire(env, contenu_lot=contenu)
    r = classer(env)
    genres = sorted(a["genre"] for a in r["anomalies"]["L1"])
    assert genres == ["entree_en_double", "entree_manquante", "etiquette_hors_lot", "ordre_du_lot_non_suivi",
                      "reponse_illisible"]
    assert r["anomalies"]["L2"] == []
    i_oter = cle["L1"]["etiquettes"][oter]
    lv = K.O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert lv["fiches"][i_oter]["R7"]["compte"] == 0 and lv["fiches"][i_oter]["N"]["compte"] == "aucune"


def test_valeurs_non_entieres_et_R4(tmp_path):
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    vue, _ = O.vue_lecteur(fiche("Z", "propa", 1, 1, "levier:cout"))
    e = {"R1": {"valeur": "1", "passage": vue["enonce"][:30]}, "R2": {"valeur": True, "passage": vue["enonce"][:30]},
         "R3": {"valeur": 1.0, "passage": vue["enonce"][:30]}, "R4": {"valeur": 0, "motif": "x"},
         "R5": {"valeur": 1, "passage": vue["enonce"][:30]}, "N": {"valeur": "C99"}}
    r = O.verifier_entree(e, vue, False, cat)
    assert [r[c]["compte"] for c in ("R1", "R2", "R3", "R4", "R5", "R6", "R7")] == [0, 0, 0, 1, 1, 0, 0]
    assert r["N"]["compte"] == "aucune" and r["N"]["occupation_non_prouvee"]
    r = O.verifier_entree(e, vue, True, cat)  # levier:juge : R4 lu, 0 rendu
    assert r["R4"]["compte"] == 0
    e["R4"] = {"valeur": 1, "passage": "changer le paramètre du juge en la valeur"}  # pas dans cette fiche
    assert O.verifier_entree(e, vue, True, cat)["R4"]["compte"] == 0
    e["R4"] = {"valeur": 1, "passage": "levier:cout"}  # étiquette seule : trop courte
    assert O.verifier_entree(e, vue, True, cat)["R4"]["compte"] == 0
    e["R4"] = {"valeur": 1, "passage": vue["demande_organisme"]["texte"]}
    assert O.verifier_entree(e, vue, True, cat)["R4"]["compte"] == 1


def test_temoin_juge_R4_attendu(tmp_path):
    """T2-C1 (levier:juge) doit avoir R4 = 0 : un lecteur qui met 1 avec citation exacte est compté, et l'exactitude le dit."""
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R4": 1} if i == "T2-C1" else v, ()))
    r = classer(env)
    err = r["exactitude_lecteur"]["L1"]["R4"]["erreurs"]
    assert err == [{"temoin": "T2-C1", "attendu": 0, "lu": 1}]


@pytest.mark.parametrize("cas", ["non_scellee", "absente", "alteree", "rescellee"])
def test_reponse_refusee(tmp_path, cas):
    """Une réponse désscellée, effacée, altérée, ou altérée puis rescellée (empreinte autre que celle du journal) : refus."""
    env, _ = preparer(tmp_path)
    lire(env)
    p = env / "reponse-L2-lot2-v3-2.json"
    if cas == "non_scellee":
        Path(str(p) + ".sha256").unlink()
    elif cas == "absente":
        p.unlink()
        Path(str(p) + ".sha256").unlink()
    elif cas == "alteree":
        p.write_text(p.read_text(encoding="utf-8").replace("manque", "manqua"), encoding="utf-8")
    else:
        resceller(p, p.read_text(encoding="utf-8").replace("manque", "manqua"))
    with pytest.raises(O.Refus):
        classer(env)
    with pytest.raises(O.Refus):
        O.bilan(env)


def test_envoi_altere_refuse(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    p = env / "pile-interne-v3-2.json"
    p.write_text(p.read_text(encoding="utf-8").replace('"depense"', '"processeur"'), encoding="utf-8")
    with pytest.raises(O.Refus):
        classer(env)


def test_auteurs_sans_effet_sur_le_classement(tmp_path):
    env, _ = preparer(tmp_path / "a")
    lire(env)
    r1 = classer(env)
    fs = fiches_factices(renommer={"propa": "zz", "propb": "aa"})
    env2, _ = preparer(tmp_path / "b", fs)
    lire(env2)
    r2 = classer(env2)
    trad = lambda s: s.replace("zz-", "propa-").replace("aa-", "propb-")
    assert r2["designees"] == r1["designees"] == []
    assert [trad(i) for i in r2["rang_exploratoire"]["ordre_neuves"]] == r1["rang_exploratoire"]["ordre_neuves"]


def test_reseau_et_cle_confines():
    """Le classement n'a aucun accès réseau ni à l'environnement ; l'outil n'a qu'une adresse (OpenAI, Chat Completions),
    ne lit l'environnement qu'en deux points (la clé, par son nom, retirée aussitôt ; SSL_CERT_FILE), ne lance rien."""
    arbre = ast.parse((MODS / "classer_conception_propre_v3_2_1.py").read_text(encoding="utf-8"))
    imports = {a.name.split(".")[0] for n in ast.walk(arbre) if isinstance(n, ast.Import) for a in n.names}
    imports |= {n.module.split(".")[0] for n in ast.walk(arbre) if isinstance(n, ast.ImportFrom) and n.module}
    assert not imports & {"urllib", "http", "socket", "requests", "subprocess", "os", "ssl"}
    texte = (MODS / "classer_conception_propre_v3_2_1.py").read_text(encoding="utf-8")
    assert "notes-par-juge" not in texte and "environ" not in texte
    texte = (MODS / "outil_lecteur_conception_propre_v3_2_1.py").read_text(encoding="utf-8")
    assert "notes-par-juge" not in texte and "subprocess" not in texte and "requests" not in texte
    urls = re.findall(r"https?://[^\s\"'`)]+", texte)
    assert set(urls) == {"https://api.openai.com/v1/chat/completions", "https://developers.openai.com/api/docs/pricing",
                         "https://platform.openai.com/docs/pricing"}
    arbre = ast.parse(texte)
    source_prix = next(n for n in arbre.body if isinstance(n, ast.Assign) and n.targets[0].id == "SOURCE_PRIX")
    assert [n.value for n in ast.walk(arbre) if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and "https://api.openai.com" in n.value and n.value.startswith("http")] == [O.URL_AMONT]
    for u in ("developers.openai.com", "platform.openai.com"):  # citations de la source des prix seulement
        assert sum(u in ast.get_source_segment(texte, n) for n in arbre.body) == 1
        assert u in ast.get_source_segment(texte, source_prix)
    assert "getenv" not in texte  # C1 du contre-lecteur : aucun repli vers une autre variable
    usages = [n for n in ast.walk(arbre) if isinstance(n, ast.Attribute) and n.attr == "environ"]
    assert len(usages) == 2  # dans le code (la docstring n'est pas comptée)
    assert "os.environ.pop(VARIABLE_CLE, None)" in texte and 'os.environ.get("SSL_CERT_FILE")' in texte
    assert 'VARIABLE_CLE = "OPENAI_API_KEY"' in texte and "print(cle" not in texte


def test_bout_en_bout_en_ligne_de_commande(tmp_path):
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    env = envois_de(racine_de(tmp_path))
    py = [sys.executable, "-I", "-B"]
    outil, classeur = str(MODS / "outil_lecteur_conception_propre_v3_2_1.py"), str(MODS / "classer_conception_propre_v3_2_1.py")
    prix = ["--effort", "medium", "--palier", "standard", "--plafond-usd", "11", "--depense-anterieure-usd", "0"]
    c = subprocess.run(py + [outil, "preparer", "--fiches", str(pf), "--attestation", str(pa), "--sortie", str(env),
                             "--racine", str(racine_de(tmp_path))] + prix, capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    assert json.loads(c.stdout)["appels"] == 12
    lire(env)
    c = subprocess.run(py + [outil, "verifier", "--envois", str(env), "--racine", str(racine_de(tmp_path))], capture_output=True,
                       text=True)
    assert c.returncode == 0, c.stderr
    O.verifier_sceau(env / "lecture-verifiee-L1-v3-2.json")
    sortie = tmp_path / "classement"
    c = subprocess.run(py + [classeur, "--envois", str(env), "--sortie", str(sortie), "--racine", str(racine_de(tmp_path))],
                       capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    for n in ("classement-v3-2.json", "classement-v3-2.md", "lecture-verifiee-L1-v3-2.json", "lecture-verifiee-L2-v3-2.json"):
        O.verifier_sceau(sortie / n)
    r = json.loads((sortie / "classement-v3-2.json").read_text(encoding="utf-8"))
    assert r["designees"] == [] and r["lisible"] and r["separation"]["issue"] == "séparation réelle (portée par R7)"
    assert "aucune idée désignée" in (sortie / "classement-v3-2.md").read_text(encoding="utf-8")
    c = subprocess.run(py + [classeur, "--envois", str(env), "--sortie", str(sortie), "--racine", str(racine_de(tmp_path))],
                       capture_output=True, text=True)
    assert c.returncode == 2 and "R12" in c.stderr
    c = subprocess.run(py + [outil, "preparer", "--fiches", str(pf), "--attestation", str(pa), "--sortie", str(env),
                             "--racine", str(racine_de(tmp_path))] + prix, capture_output=True, text=True)
    assert c.returncode == 2


# --- de la v2 : M2, lecture incomplète ------------------------------------------------------------------------------------------

def _lot_illisible(cible_L, cible_k):
    return lambda L, k, texte: "pas de JSON : coupé" if (L, k) == (cible_L, cible_k) else texte


def test_M2_lot_illisible_rend_le_rang_non_lisible(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, contenu_lot=_lot_illisible("L2", 1))
    r = classer(env)
    assert not r["lecture_complete"]["complete"] and r["echecs"]["E2_v2_lecture_incomplete"] and r["echecs"]["E2_v2"]
    assert r["designees"] == [] and not r["lisible"]
    assert r["verdict"].startswith("E2 v2 : lecture illisible") and "L2 lot 1 : reponse_illisible" in r["verdict"]
    cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
    lot = [cle["L2"]["etiquettes"][e] for e in cle["L2"]["lots"][0]]
    pile = {p["id"]: p for p in json.loads((env / "pile-interne-v3-2.json").read_text(encoding="utf-8"))["fiches"]}
    assert r["lecture_complete"]["reelles_touchees"] == sorted(i for i in lot if pile[i]["origine"] == "reelle")
    assert len(r["lecture_complete"]["reelles_touchees"]) + len(r["lecture_complete"]["temoins_touches"]) == len(lot)
    md = K.resume_md(r)
    assert "reponse_illisible" in md and "Lecture complète : False" in md


def test_M2_fin_length_meme_lisible_bloque(tmp_path):
    """Fin `length` au 2e appel, contenu lisible : bloquante (et l'envoi s'arrête là)."""
    env, _ = preparer(tmp_path)
    lire(env, contenu_lot=None, scenarios={2: "fin_lisible"})
    r = classer(env)
    assert not r["lecture_complete"]["complete"] and r["designees"] == [] and "fin_non_stop" in r["verdict"]


@pytest.mark.parametrize("genre", ["manquante", "double"])
def test_M2_entree_manquante_ou_double_bloque(tmp_path, genre):
    env, _ = preparer(tmp_path)

    def contenu(L, k, texte):
        if (L, k) != ("L1", 2):
            return texte
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        o["lecture"] = o["lecture"][1:] if genre == "manquante" else o["lecture"] + [o["lecture"][-1]]
        return json.dumps(o, ensure_ascii=False)
    lire(env, contenu_lot=contenu)
    r = classer(env)
    assert not r["lecture_complete"]["complete"] and r["designees"] == []
    assert r["lecture_complete"]["fiches_touchees"] == 1


def test_anomalie_non_bloquante_etiquette_hors_lot(tmp_path):
    """Mutation survivante 9 de la contre-lecture : une entrée d'un autre lot est écartée, sans effet ni faux désordre."""
    env, _ = preparer(tmp_path)
    cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
    etrangere = cle["L1"]["lots"][1][0]

    def contenu(L, k, texte):
        if (L, k) != ("L1", 1):
            return texte
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        e = copy.deepcopy(o["lecture"][0])
        e["etiquette"] = etrangere
        for c in O.CRITERES:
            e[c] = {"valeur": 0, "motif": "faux"}
        o["lecture"].append(e)
        return json.dumps(o, ensure_ascii=False)
    lire(env, contenu_lot=contenu)
    r = classer(env)
    assert [a["genre"] for a in r["anomalies"]["L1"]] == ["etiquette_hors_lot"]
    assert r["lecture_complete"]["complete"] and r["lisible"] and r["rang_exploratoire"]["ordre_neuves"]
    i = cle["L1"]["etiquettes"][etrangere]
    pile = {p["id"]: p for p in json.loads((env / "pile-interne-v3-2.json").read_text(encoding="utf-8"))["fiches"]}
    vals = valeurs_attendues(pile[i])
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert all(lv["fiches"][i][c]["compte"] == vals[c] for c in O.CRITERES)  # la fausse entrée n'a rien changé


# --- de la v2 : M3, provenance des fiches ---------------------------------------------------------------------------------------

def _fiches_quarantaine():
    return [{"fiche": f, "signaux": ["motif"]} for f in fiches_factices()]


@pytest.mark.parametrize("cas", ["quarantaine_au_bon_nom", "autre_nom", "hors_runs", "run_mal_nomme", "fin_absente",
                                 "fin_code_1", "fin_autre_empreinte", "fin_non_scellee", "lien", "sans_admissible",
                                 "element_sans_internes"])
def test_M3_seule_la_copie_des_fiches_validees_du_run(tmp_path, cas):
    fs = fiches_factices()
    rac = racine_de(tmp_path)
    if cas == "quarantaine_au_bon_nom":
        pf, h = ecrire_fiches(tmp_path, _fiches_quarantaine())
    elif cas == "autre_nom":
        pf, h = ecrire_fiches(tmp_path, fs, nom="sortie--fiches-en-quarantaine.json")
    elif cas == "hors_runs":
        ecrire_fiches(tmp_path, fs)
        pf = rac / "docs" / "sortie--fiches-validees.json"
        pf.write_text(json.dumps(fs, ensure_ascii=False))
        h = O.sha256_fichier(pf)
        Path(str(pf) + ".sha256").write_text(f"{h}  {pf.name}\n")
    elif cas == "run_mal_nomme":
        pf, h = ecrire_fiches(tmp_path, fs, run="20261114-010203-autre-course-g1")
    elif cas == "fin_absente":
        pf, h = ecrire_fiches(tmp_path, fs)
        m = pf.parents[1] / "manifeste-lanceur-fin.json"
        m.unlink()
        Path(str(m) + ".sha256").unlink()
    elif cas == "fin_code_1":
        pf, h = ecrire_fiches(tmp_path, fs, fin=lambda h: {"code": 1, "pour_l_attestation": {"fiches_validees_sha256": h}})
    elif cas == "fin_autre_empreinte":
        pf, h = ecrire_fiches(tmp_path, fs, fin=lambda h: {"code": 0, "pour_l_attestation": {
            "fiches_validees_sha256": "0" * 64}})
    elif cas == "fin_non_scellee":
        pf, h = ecrire_fiches(tmp_path, fs)
        m = pf.parents[1] / "manifeste-lanceur-fin.json"
        m.write_text(m.read_text(encoding="utf-8") + " ", encoding="utf-8")
    elif cas == "lien":
        vrai, h = ecrire_fiches(tmp_path, fs)
        d = pf_dir = rac / "runs" / "course-ideation-conception-propre-v1" / "20261114-020203-course-ideation-conception-propre-v1-g1"
        (pf_dir / "copies").mkdir(parents=True)
        pf = pf_dir / "copies" / "sortie--fiches-validees.json"
        pf.symlink_to(vrai)
        Path(str(pf) + ".sha256").write_text(f"{h}  {pf.name}\n")
        shutil.copyfile(vrai.parents[1] / "manifeste-lanceur-fin.json", d / "manifeste-lanceur-fin.json")
        shutil.copyfile(vrai.parents[1] / "manifeste-lanceur-fin.json.sha256", d / "manifeste-lanceur-fin.json.sha256")
    elif cas == "sans_admissible":
        hors = [f for f in fs if f["nom"].split()[2].startswith("H")]
        pf, h = ecrire_fiches(tmp_path, hors)
    else:
        f0 = copy.deepcopy(fs)
        del f0[0]["identifiant_auteur"]
        pf, h = ecrire_fiches(tmp_path, f0)
    pa = ecrire_attestation(tmp_path, h)
    with pytest.raises(O.Refus):
        opreparer(pf, pa, envois_de(rac), rac)
    assert not (envois_de(rac)).exists()


def test_M3_chemin_relatif_accepte_et_classement_revérifie(tmp_path):
    fs = fiches_factices()
    rac = racine_de(tmp_path)
    pf, h = ecrire_fiches(tmp_path, fs)
    pa = ecrire_attestation(tmp_path, h)
    man = opreparer(pf.relative_to(rac), pa, envois_de(rac), rac)
    assert man["fiches_validees"]["chemin"] == ("runs/course-ideation-conception-propre-v1/" + RUN +
                                                "/copies/sortie--fiches-validees.json")
    assert man["fiches_validees"]["run"] == RUN and man["fiches_validees"]["sha256"] == h
    env = envois_de(rac)
    lire(env)
    assert classer(env)["fiches_validees"]["sha256"] == h
    # la copie change après la préparation (compagnon réécrit) : le classement refuse
    pf.write_text(pf.read_text(encoding="utf-8").replace("Idée factice A1", "Idée factice A9"), encoding="utf-8")
    Path(str(pf) + ".sha256").write_text(f"{O.sha256_fichier(pf)}  {pf.name}\n")
    with pytest.raises(O.Refus):
        classer(env)
    # ... même si le manifeste de fin du run est réécrit d'accord avec elle : le manifeste des envois ne l'est pas
    m = pf.parents[1] / "manifeste-lanceur-fin.json"
    m.unlink()
    Path(str(m) + ".sha256").unlink()
    O.ecrire_scelle(m, json.dumps({"code": 0, "pour_l_attestation": {"fiches_validees_sha256": O.sha256_fichier(pf)}}))
    O.verifier_fiches_de_run(rac, pf)
    with pytest.raises(O.Refus, match="manifeste des envois"):
        classer(env)


# --- de la v2 : mutations survivantes de la contre-lecture -----------------------------------------------------------------------

def test_L4_jugee_aussi_sur_N(tmp_path):
    env, _ = preparer(tmp_path)
    extra = {id_de("A1"), id_de("A2")}
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C8"} if (L == "L2" and (p["famille"] == "hasard" or i in extra))
                                        else v, ()))
    r = classer(env)
    assert r["L4"]["R7"]["tient"] and not r["L4"]["N"]["tient"] and not r["L4"]["tient"] and not r["lisible"]
    assert r["L4"]["N"]["kappa"] < 0.4


def test_kappa_au_seuil_exact_tient():
    a = [1] * 10 + [0] * 10
    b = [1] * 7 + [0] * 3 + [1] * 3 + [0] * 7
    k = K.kappa_accord(a, b)
    assert abs(k["kappa"] - 0.4) < 1e-12 and k["jugee_sur"] == "kappa" and k["tient"]
    k = K.kappa_accord([1] * 10, [1] * 8 + [0] * 2)  # accord brut 0,8 exactement, marge constante
    assert k["marge_constante"] and k["tient"]


def test_E5_au_seuil_exact(tmp_path):
    occ = {id_de(n) for n in ("A2", "A3", "A7")}
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "C10"} if i in occ else ({**v, "R2": 0} if i in (id_de("A8"), id_de("A4"))
                                                                               else v), ()))
    r = classer(env)
    st = r["rang_exploratoire"]["statut"]
    passees = [i for i in st if st[i]["statut"] in ("neuve", "occupee")]
    assert len(passees) == 5 and sum(st[i]["statut"] == "occupee" for i in passees) == 4
    assert r["echecs"]["E5"] is False  # 4/5 = 80 % : pas « plus de 80 % »
    env2, _ = preparer(tmp_path / "b")
    lire(env2, modif=lambda L, i, p, v: ({**v, "N": "C10"} if (i in occ or i == id_de("A1"))
                                         else ({**v, "R2": 0} if i in (id_de("A8"), id_de("A4")) else v), ()))
    assert classer(env2)["echecs"]["E5"] is True


def test_comparaisons_descriptives_bilaterales(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R1": 0} if p["origine"] == "reelle" else v, ()))
    r = classer(env)
    d = next(x for x in r["descriptif_holm"] if x["critere"] == "R1")
    assert d["difference"] == -1.0 and d["p_brute"] < 0.001


def test_audit_declenche_par_un_seul_signe(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R7": 1} if p["famille"] == "hasard" else
                                        ({**v, "N": "aucune"} if i == "T2-C2" else v), ()))
    r = classer(env)
    a = r["audit_proprete"]
    signes = [a[k] for k in ("lisibilite_parfaite", "kappa_1", "toutes_publiees_reconnues",
                             "aucune_idee_au_hasard_passee")]
    assert a["declenche"] and 0 < sum(signes) < 4


def test_typographie_du_passage_non_toleree():
    cat = O.entrees_catalogue(O.lire_piece(RACINE, "catalogue")[0])
    vue, _ = O.vue_lecteur(fiche("Z", "propa", 1, 1, "levier:cout"))
    assert 'sans rien d\'autre " Z ".' in vue["enonce"]  # « Z » servi " Z " (typographie de l'orchestrateur)
    juste = {"valeur": 1, "passage": 'décrite ici, sans rien d\'autre " Z ".'}
    faux = {"valeur": 1, "passage": "décrite ici, sans rien d’autre « Z »."}
    assert O.verifier_entree({"R1": juste}, vue, False, cat)["R1"]["compte"] == 1
    assert O.verifier_entree({"R1": faux}, vue, False, cat)["R1"]["compte"] == 0


def test_L2_detail_porte_la_valeur_brute(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "R3": 1}, ("R3",)) if i == "T2-F3" else (v, ()))
    r = classer(env)
    d = r["L2"]["par_temoin"]["T2-F3"]
    assert d["L1"] == 0 and d["L2"] == 0 and d["brut"] == {"L1": 1, "L2": 1} and r["L2"]["tient"]


# --- de la v2 : variante « désignation détachée de L5 », préparée, non active ----------------------------------------------------

# === envoi par la doublure déclarée (essais de la v3, adaptés) ===========================================================

def test_envoyer_sain_tout_envoye_puis_classe(tmp_path, monkeypatch, capsys):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch)
    assert r["issue"] == "fait" and r["appels"] == 12 and len(d.appels) == 12 and len(set(d.appels)) == 12
    assert d.appels == [man["fichiers"][n] for n in man["ordre_d_envoi"]]  # ordre du manifeste, chaque corps une fois
    attendu = sum(cout_sain(g["octets"]) for g in man["garde_depense"]["envois"])
    assert abs(r["depense_comptee_usd"] - attendu) < 1e-5
    for nom, rendu in zip(man["reponses_attendues"], d.rendus):
        O.verifier_sceau(env / nom)
        assert (env / nom).read_bytes() == rendu  # M3 : écrite brute, octet pour octet
    O.verifier_sceau(env / "releve-depense-v3-2-1.json")
    j = O.lire_journal(env)
    assert j["lignes"] == 36 and len(j["recus"]) == 12 and not j["anomalies"] and not j["en_vol"] and j["arret"] is None
    assert "OPENAI_API_KEY" not in os.environ  # retirée après lecture
    assert not O.contient_cle(tous_les_octets(tmp_path), CLE_FACTICE)
    sortie = capsys.readouterr()
    assert CLE_FACTICE not in sortie.out + sortie.err
    res = classer(env)
    assert res["lisible"] and res["designees"] == [] and res["rang_exploratoire"]["deux_premieres"] == [
        id_de("A1"), sorted([id_de("A2"), id_de("A7")], key=res["rang_exploratoire"]["departage"].get)[0]]
    b = O.bilan(env)
    assert b["appels"] == 12 and b["clos"] == 12 and b["pret_pour_verifier"] and b["palier"] == "standard"
    r2, d2 = envoyer(env, monkeypatch)  # rien à faire : aucun appel
    assert r2["issue"] == "fait" and d2.appels == []


def test_garde_fin_length_arret_sans_relecture(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={3: "length"})
    assert r["issue"] == "anomalie" and "fin_non_stop" in r["detail"] and len(d.appels) == 3
    assert not (env / man["reponses_attendues"][3]).exists()  # le lot suivant n'est jamais parti
    with pytest.raises(O.Refus, match="déjà arrêtée"):
        envoyer(env, monkeypatch)
    res = classer(env)
    assert not res["lecture_complete"]["complete"] and res["designees"] == []
    genres = {a["genre"] for L in ("L1", "L2") for a in res["lecture_complete"]["anomalies"][L]}
    assert genres == {"fin_non_stop", "reponse_illisible", "reponse_absente", "anomalie_d_envoi"}
    assert res["verdict"].startswith("E2 v2 : lecture illisible")


def test_garde_modele_servi_different(tmp_path, monkeypatch):
    env, _ = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: "modele"})
    assert r["issue"] == "anomalie" and "modele_servi_different" in r["detail"] and len(d.appels) == 1
    ev = O.lire_journal(env)["clos"]["envoi-L1-lot1-v3-2.corps.json"]
    assert ev["modele_servi"] == "gpt-6-astra-2026-11-01" and not ev["au_pire_cas"]  # dépense réelle comptée
    res = classer(env)
    assert any(a["genre"] == "modele_servi_different" for a in res["lecture_complete"]["anomalies"]["L1"])
    assert res["designees"] == []


@pytest.mark.parametrize("scenario", ["modele", "majuscules"])
def test_verifier_modele_servi_different_bloque(tmp_path, scenario):
    """M2 du contre-lecteur : à la vérification aussi, le nom servi est comparé à l'égalité exacte (casse comprise)."""
    env, _ = preparer(tmp_path)
    lire(env, scenarios={1: scenario})
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    genres = [a["genre"] for a in lv["anomalies"] if a["lot"] == 1]
    assert "modele_servi_different" in genres and "anomalie_d_envoi" in genres
    assert all(f["R7"]["motif"] == "contenu non lu" for f in lv["fiches"].values() if f["lot"] == 1)
    assert "modele_servi_different" in classer(env)["verdict"]


@pytest.mark.parametrize("scenario,genre", [
    ("sans_usage", "usage_absent"), ("details_non_objets", "usage_absent"), ("usage_incoherent", "usage_incoherent"),
    ("zeros", "usage_incoherent"), ("un_jeton", "usage_incoherent"), ("total_sous_somme", "usage_incoherent"),
    ("entree_sous_plancher", "usage_incoherent"), ("sortie_sous_plancher", "usage_incoherent")])
def test_garde_usage_absent_nul_ou_incoherent_compte_au_pire_cas(tmp_path, monkeypatch, scenario, genre):
    """M4 : usage absent, nul ou incohérent (vers le haut comme vers le bas) : bloquant, compté au pire cas."""
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={2: scenario})
    g = man["garde_depense"]["envois"]
    assert r["issue"] == "anomalie" and genre in r["detail"] and len(d.appels) == 2
    assert abs(r["depense_comptee_usd"] - (cout_sain(g[0]["octets"]) + g[1]["pire_cas_usd"])) < 1e-5
    assert O.lire_journal(env)["clos"][g[1]["envoi"]]["au_pire_cas"] is True
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    bloq = [a for a in lv["anomalies_bloquantes"] if a["lot"] == 2]
    assert [a["genre"] for a in bloq][0] == "anomalie_d_envoi" and len(bloq[0]["ids"]) == 5


def test_garde_cout_au_dessus_du_pire_cas(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: "cout_excessif"})
    assert r["issue"] == "anomalie" and "cout_au_dessus_du_pire_cas" in r["detail"]
    assert r["depense_comptee_usd"] > man["garde_depense"]["envois"][0]["pire_cas_usd"]  # coût lu, plus haut, compté


def test_garde_plafond_arret_avant_l_appel(tmp_path, monkeypatch):
    env, man = preparer(tmp_path, plafond_usd=3.0)
    g = man["garde_depense"]["envois"]
    depense, n = 0.0, 0
    for e in g:  # appels que la garde doit laisser partir
        if depense + e["pire_cas_usd"] > 3.0:
            break
        depense += cout_sain(e["octets"])
        n += 1
    assert 0 < n < 12
    r, d = envoyer(env, monkeypatch)
    assert r["issue"] == "plafond" and len(d.appels) == n and abs(r["depense_comptee_usd"] - depense) < 1e-5
    assert r["depense_comptee_usd"] + g[n]["pire_cas_usd"] > 3.0 >= r["depense_comptee_usd"]
    assert O.lire_journal(env)["arret"]["motif"] == "plafond"
    with pytest.raises(O.Refus, match="déjà arrêtée"):
        envoyer(env, monkeypatch)
    res = classer(env)
    assert res["designees"] == [] and "reponse_absente" in res["verdict"]


def test_garde_nombre_d_appels_au_journal(tmp_path, monkeypatch):
    """Un journal qui compte déjà les appels permis : arrêt sans envoi (artefact) ; le cas sain envoie les 12."""
    env, man = preparer(tmp_path)
    j = O.lire_journal(env)
    for k in range(12):
        O.ajouter_journal(env, j, {"evenement": "envoi", "envoi": f"faux-{k}", "octets": 1, "pire_cas_usd": 0.0})
        O.ajouter_journal(env, j, {"evenement": "clos", "envoi": f"faux-{k}", "cout_usd": 0.0, "anomalies": []})
    r, d = envoyer(env, monkeypatch)
    assert r["issue"] == "plafond" and "appels" in r["detail"] and d.appels == []


def test_garde_statut_non_200_corps_jamais_ecrit(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: "429"})
    assert r["issue"] == "anomalie" and "statut_non_200" in r["detail"]
    err = json.loads((env / "erreur-L1-lot1-v3-2.json").read_text(encoding="utf-8"))
    O.verifier_sceau(env / "erreur-L1-lot1-v3-2.json")
    assert err["statut"] == 429 and err["erreur"] == {"type": "insufficient_quota", "code": "insufficient_quota"}
    assert b"org-SECRETORG42" not in tous_les_octets(tmp_path) and b"MESSAGE-ERREUR-AMONT" not in tous_les_octets(env)
    assert abs(r["depense_comptee_usd"] - man["garde_depense"]["envois"][0]["pire_cas_usd"]) < 1e-9


def test_garde_type_et_code_d_erreur_filtres(tmp_path, monkeypatch):
    """C3 du contre-lecteur : un type ou un code d'erreur qui porte un identifiant n'est jamais écrit."""
    env, _ = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: "429_identifiant"})
    err = json.loads((env / "erreur-L1-lot1-v3-2.json").read_text(encoding="utf-8"))
    assert err["erreur"] == {"type": None, "code": None} and b"SECRETORG42" not in tous_les_octets(tmp_path)
    assert O.champ_court("insufficient_quota") == "insufficient_quota"
    for faux in ("org-SECRETORG42", "Quota", "rate limit", "x" * 65, "", None, 3, ["a"]):
        assert O.champ_court(faux) is None


@pytest.mark.parametrize("scenario,genre", [("panne", "transport_echec"), ("illisible", "reponse_illisible"),
                                            ("refus", "refus_du_lecteur")])
def test_garde_panne_illisible_refus(tmp_path, monkeypatch, scenario, genre):
    """D4 et D5 du contre-lecteur : coupure et page de passerelle comptées au pire cas ; refus compté au coût lu."""
    env, man = preparer(tmp_path)
    g = man["garde_depense"]["envois"]
    r, d = envoyer(env, monkeypatch, scenarios={2: scenario})
    assert r["issue"] == "anomalie" and genre in r["detail"] and len(d.appels) == 2
    assert not O.contient_cle(tous_les_octets(tmp_path), CLE_FACTICE)  # message d'exception jamais écrit
    second = g[1]["pire_cas_usd"] if scenario != "refus" else cout_sain(g[1]["octets"])
    assert abs(r["depense_comptee_usd"] - (cout_sain(g[0]["octets"]) + second)) < 1e-5
    if scenario == "panne":
        err = json.loads((env / "erreur-L1-lot2-v3-2.json").read_text(encoding="utf-8"))
        assert err["cause_transport"] == "TimeoutError" and err["anomalies"] == ["transport_echec"]
    if scenario == "illisible":  # M3 : la page rendue au statut 200 est gardée brute, puis jugée illisible
        assert (env / "reponse-L1-lot2-v3-2.json").read_bytes() == b"<html>passerelle</html>"
    if scenario == "refus":
        assert "refus_du_lecteur" in classer(env)["verdict"]


def test_cout_lu_avec_cache_au_prix_du_cache(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: "cache"}, envois_max=1)
    o = man["garde_depense"]["envois"][0]["octets"]
    p, c = o // 4, o // 8
    assert r["issue"] == "pause" and abs(r["depense_comptee_usd"] - ((p - c) * 10 + c * 1 + 3000 * 50) / 1e6) < 1e-9


def test_cout_usage_regles():
    prix = {"entree": 10.0, "sortie": 50.0, "cache": 1.0, "source": "essai"}
    u = {"prompt_tokens": 1000, "completion_tokens": 500, "total_tokens": 1500,
         "prompt_tokens_details": {"cached_tokens": 400}, "completion_tokens_details": {"reasoning_tokens": 300}}
    c, pb, lus = O.cout_usage(u, prix)
    assert pb is None and abs(c - (600 * 10 + 400 * 1 + 500 * 50) / 1e6) < 1e-12 and lus["reasoning_tokens"] == 300
    c, pb, _ = O.cout_usage({**u, "total_tokens": 1600}, prix)  # excédent compté au prix le plus haut
    assert pb is None and abs(c - (600 * 10 + 400 * 1 + 500 * 50 + 100 * 50) / 1e6) < 1e-12
    for faux in (None, {}, {"prompt_tokens": True, "completion_tokens": 1}, {"prompt_tokens": 1.0, "completion_tokens": 1},
                 {"prompt_tokens": -1, "completion_tokens": 1}, {**u, "prompt_tokens_details": {"cached_tokens": "4"}},
                 {**u, "prompt_tokens_details": []}, {**u, "completion_tokens_details": "x"}):
        assert O.cout_usage(faux, prix)[0] is None
    assert O.cout_usage({**u, "prompt_tokens_details": {"cached_tokens": 2000}}, prix)[1]
    assert O.cout_usage({**u, "completion_tokens": 40000, "total_tokens": 41000}, prix)[1]
    # M4 : vers le bas
    assert "total" in O.cout_usage({**u, "total_tokens": 1499}, prix)[1]
    assert "entrée" in O.cout_usage(u, prix, octets_envoyes=16 * 1000 + 16)[1]
    assert O.cout_usage(u, prix, octets_envoyes=16 * 1000 + 15)[1] is None
    assert "visibles" in O.cout_usage(u, prix, octets_contenu=16 * 200 + 1)[1]  # 200 visibles pour 3 201 octets
    assert O.cout_usage(u, prix, octets_contenu=16 * 200)[1] is None
    z = {"prompt_tokens": 0, "completion_tokens": 0}
    assert O.cout_usage(z, prix, octets_contenu=1)[1] and O.cout_usage(z, prix)[1] is None
    assert O.cout_usage({**u, "prompt_tokens_details": None, "completion_tokens_details": None}, prix)[1] is None


def test_analyse_modele_exact_et_fin():
    prix = {"entree": 10.0, "sortie": 50.0, "cache": 10.0, "source": "essai"}
    base = {"object": "chat.completion", "model": "gpt-6-astra", "usage": {"prompt_tokens": 1, "completion_tokens": 1},
            "choices": [{"index": 0, "message": {"content": "x", "refusal": None}, "finish_reason": "stop"}]}
    a = O.analyser_reponse(200, json.dumps(base).encode(), 1.0, prix)
    assert a["anomalies"] == [] and not a["au_pire_cas"]
    for modele in ("gpt-6-astra-2026-11-01", "GPT-6-astra", "gpt-6-astra ", None):
        a = O.analyser_reponse(200, json.dumps({**base, "model": modele}).encode(), 1.0, prix)
        assert "modele_servi_different" in a["anomalies"]
    for fin in ("length", "content_filter", "tool_calls", None):
        b = copy.deepcopy(base)
        b["choices"][0]["finish_reason"] = fin
        assert "fin_non_stop" in O.analyser_reponse(200, json.dumps(b).encode(), 1.0, prix)["anomalies"]
    assert O.analyser_reponse(None, None, 1.0, prix)["anomalies"] == ["transport_echec"]
    for code in (301, 302, 303, 307, 308):
        assert O.analyser_reponse(code, b"", 1.0, prix)["anomalies"] == ["statut_non_200", "redirection_refusee"]
    for formes in ([], "x", 3, None, [1], {"a": 1}):  # aucune forme ne fait lever l'analyse (M3)
        for cle in ("choices", "usage", "model", "object", "service_tier"):
            O.analyser_reponse(200, json.dumps({**base, cle: formes}).encode(), 1.0, prix)
        O.analyser_reponse(502, json.dumps({"error": formes}).encode(), 1.0, prix)


def test_pause_et_reprise_sans_renvoi(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, envois_max=2)
    assert r["issue"] == "pause" and len(d.appels) == 2 and "OPENAI_API_KEY" not in os.environ
    r2, d2 = envoyer(env, monkeypatch)
    assert r2["issue"] == "fait" and len(d2.appels) == 10 and not set(d.appels) & set(d2.appels)
    assert r2["appels"] == 12 and (env / "releve-depense-v3-2-2.json").exists()
    assert abs(r2["depense_comptee_usd"] - sum(cout_sain(g["octets"]) for g in man["garde_depense"]["envois"])) < 1e-5


def test_journal_tronque_ou_reecrit_refuse(tmp_path, monkeypatch):
    env, _ = preparer(tmp_path)
    envoyer(env, monkeypatch, envois_max=3)
    p = env / "journal-depense-v3-2.jsonl"
    lignes = p.read_bytes().splitlines(keepends=True)
    p.write_bytes(b"".join(lignes[:-2]))  # réception et clôture du 3e appel effacées : sa réponse n'est plus au journal
    with pytest.raises(O.Refus, match="sans clôture conforme"):
        envoyer(env, monkeypatch)
    with pytest.raises(O.Refus, match="sans clôture conforme"):
        O.bilan(env)
    p.write_bytes(b"".join(lignes[:-1]))  # clôture seule effacée : appel sans clôture, pire cas, aucune reprise
    with pytest.raises(O.Refus, match="sans clôture au journal"):
        envoyer(env, monkeypatch)
    p.write_bytes(b"".join(lignes).replace(b'"cout_usd": 0.', b'"cout_usd": 0.0000', 1))  # coût réécrit
    with pytest.raises(O.Refus, match="chaîne rompue"):
        envoyer(env, monkeypatch)


def test_appel_sans_cloture_compte_au_pire_cas(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    with pytest.raises(KeyboardInterrupt):
        envoyer(env, monkeypatch, scenarios={2: "crash"})
    j = O.lire_journal(env)
    g = man["garde_depense"]["envois"]
    assert j["en_vol"] == [g[1]["envoi"]]
    assert abs(j["depense_usd"] - (cout_sain(g[0]["octets"]) + g[1]["pire_cas_usd"])) < 1e-5
    with pytest.raises(O.Refus, match="sans clôture"):
        envoyer(env, monkeypatch)
    assert "reponse_absente" in classer(env)["verdict"]


def test_cle_absente_ou_vide_rien_envoye(tmp_path, monkeypatch):
    """C2 du contre-lecteur : une clé vide est refusée comme absente, avant tout journal."""
    env, _ = preparer(tmp_path)
    for valeur in (None, ""):
        if valeur is None:
            monkeypatch.delenv("OPENAI_API_KEY", raising=False)
        else:
            monkeypatch.setenv("OPENAI_API_KEY", valeur)
        d = Doublure(env)
        with pytest.raises(O.Refus, match="OPENAI_API_KEY absente ou vide"):
            O.envoyer(env, transport=d)
        assert d.appels == [] and not (env / "journal-depense-v3-2.jsonl").exists()
    sans = {k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "HOME")}
    c = subprocess.run([sys.executable, "-I", "-B", str(MODS / "outil_lecteur_conception_propre_v3_2_1.py"), "envoyer",
                        "--envois", str(env)], capture_output=True, text=True, env=sans)
    assert c.returncode == 2 and "absente" in c.stderr and not (env / "journal-depense-v3-2.jsonl").exists()
    c = subprocess.run([sys.executable, "-I", "-B", str(MODS / "outil_lecteur_conception_propre_v3_2_1.py"), "bilan",
                        "--envois", str(env)], capture_output=True, text=True, env=sans)
    assert c.returncode == 0 and json.loads(c.stdout)["appels"] == 0


def test_cle_d_une_autre_variable_jamais_lue(tmp_path, monkeypatch):
    """C1 du contre-lecteur : aucune autre variable n'est lue à la place de OPENAI_API_KEY."""
    env, _ = preparer(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    for autre in ("OPENAI_KEY", "OPENAI_API_KEY_2", "API_KEY", "OPENAI_TOKEN"):
        monkeypatch.setenv(autre, CLE_FACTICE)
    d = Doublure(env)
    with pytest.raises(O.Refus, match="absente"):
        O.envoyer(env, transport=d)
    assert d.appels == []


def test_transport_reel_refuse_une_autre_adresse(boucle):
    with pytest.raises(O.Refus):
        O.transport_reel("https://exemple.invalid/v1/chat/completions", {}, b"{}", 1)


def test_envois_d_une_autre_version_refuses(tmp_path, monkeypatch):
    env, _ = preparer(tmp_path)
    p = env / "manifeste-relecture-v3-2.json"
    resceller(p, p.read_text(encoding="utf-8").replace('"outil-lecteur-conception-propre-v3-2-1"',
                                                       '"outil-lecteur-conception-propre-v3-2"'))  # manifeste v3.2 refusé
    with pytest.raises(O.Refus, match="préparés par"):
        envoyer(env, monkeypatch)


def test_reponse_etrangere_refusee_avant_tout_envoi(tmp_path, monkeypatch):
    """Une réponse déposée sans clôture au journal arrête `envoyer` avant tout appel ; sans elle, l'envoi repart."""
    env, _ = preparer(tmp_path)
    envoyer(env, monkeypatch, envois_max=2)
    O.ecrire_scelle(env / "reponse-L1-lot3-v3-2.json", json.dumps({"object": "chat.completion"}))
    monkeypatch.setenv("OPENAI_API_KEY", CLE_FACTICE)
    d = Doublure(env)
    with pytest.raises(O.Refus, match="sans clôture conforme"):
        O.envoyer(env, transport=d)
    assert d.appels == []
    (env / "reponse-L1-lot3-v3-2.json").unlink()
    Path(str(env / "reponse-L1-lot3-v3-2.json") + ".sha256").unlink()
    r, d = envoyer(env, monkeypatch, envois_max=1)
    assert r["issue"] == "pause" and len(d.appels) == 1


# --- C1 de la relecture courte : clé de critère manquante ----------------------------------------------------------------

def _oter_cle(cible_L, cible_k, cle_otee, rang=0):
    def contenu(L, k, texte):
        if (L, k) != (cible_L, cible_k):
            return texte
        o = json.loads(texte.split("```json\n")[1].rsplit("\n```", 1)[0])
        if cle_otee == "valeur_N":
            o["lecture"][rang]["N"] = {"passage_fiche": "x"}
        else:
            del o["lecture"][rang][cle_otee]
        return json.dumps(o, ensure_ascii=False)
    return contenu


@pytest.mark.parametrize("cle_otee", ["N", "R7", "valeur_N"])
def test_C1_cle_de_critere_manquante_bloque(tmp_path, cle_otee):
    env, _ = preparer(tmp_path)
    lire(env, contenu_lot=_oter_cle("L2", 3, cle_otee))
    res = classer(env)
    assert not res["lecture_complete"]["complete"] and res["designees"] == []
    assert "cle_de_critere_manquante" in res["verdict"] and res["lecture_complete"]["fiches_touchees"] == 1


def test_C1_R4_manquant_hors_levier_juge_bloque_aussi(tmp_path):
    env, _ = preparer(tmp_path)
    cle = json.loads((env / "cle-lectures-v3-2.json").read_text(encoding="utf-8"))
    pile = {p["id"]: p for p in json.loads((env / "pile-interne-v3-2.json").read_text(encoding="utf-8"))["fiches"]}
    rang = next(r for r, et in enumerate(cle["L1"]["lots"][0]) if pile[cle["L1"]["etiquettes"][et]]["levier"] != "levier:juge")
    lire(env, contenu_lot=_oter_cle("L1", 1, "R4", rang))
    res = classer(env)
    assert "cle_de_critere_manquante" in res["verdict"] and res["designees"] == []


def test_C1_cas_sain_aucune_anomalie(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    for L in ("L1", "L2"):
        lv = O.verifier_lecture(env, L, O.lire_piece(RACINE, "catalogue")[0])
        assert lv["anomalies"] == [] and lv["anomalies_bloquantes"] == []


def test_reponse_absente_sans_arret_refusee_avec_arret_E2(tmp_path, monkeypatch):
    env, _ = preparer(tmp_path)
    envoyer(env, monkeypatch, envois_max=4)  # pause : aucun arrêt consigné
    with pytest.raises(O.Refus, match="aucun arrêt consigné"):
        classer(env)
    envoyer(env, monkeypatch, scenarios={1: "length"})  # arrêt consigné
    r = classer(env)
    assert "reponse_absente" in r["verdict"] and r["designees"] == []


@pytest.mark.parametrize("effort", ["low", "high"])
def test_effort_consigne_dans_chaque_corps(tmp_path, effort):
    env, man = preparer(tmp_path, effort=effort)
    for n in man["ordre_d_envoi"]:
        assert json.loads((env / n).read_text(encoding="utf-8"))["reasoning_effort"] == effort
    assert man["lecteur"]["reasoning_effort"] == effort


# === v3.1 : B1, la clé n'apparaît dans aucun fichier ni message ===========================================================

@pytest.mark.parametrize("suffixe", ["\r", "\n", "\r\n", " ", "\t", "é"])
def test_B1_cle_hors_ascii_imprimable_refusee_avant_tout(tmp_path, monkeypatch, capsys, boucle, suffixe):
    """Sonde s1 du contre-lecteur, en essai : transport réel de l'outil, amont détourné vers la boucle locale ; une clé
    terminée par une fin de ligne (ou portant un espace, une tabulation, un caractère non ASCII) est refusée sans être
    montrée, avant tout journal et tout envoi ; aucun fichier ne la porte."""
    vus = []
    srv = boucle(lambda h: (vus.append(1), h.send_response(200), h.end_headers()))
    amont_local(monkeypatch, srv)
    env, _ = preparer(tmp_path)
    cle = "sk-sonde-factice-CLE-A-NE-PAS-ECRIRE-9876543210"
    monkeypatch.setenv("OPENAI_API_KEY", cle + suffixe)
    with pytest.raises(O.Refus) as ex:
        O.envoyer(env)
    assert cle not in str(ex.value) and "ASCII imprimable" in str(ex.value)
    assert not vus and not (env / "journal-depense-v3-2.jsonl").exists()
    assert not O.contient_cle(tous_les_octets(tmp_path), cle)
    sortie = capsys.readouterr()
    assert cle not in sortie.out + sortie.err


def test_B1_cle_avec_fin_de_ligne_en_ligne_de_commande(tmp_path):
    env, _ = preparer(tmp_path)
    cle = "sk-sonde-factice-CLE-A-NE-PAS-ECRIRE-9876543210"
    sans = {k: v for k, v in os.environ.items() if k in ("PATH", "LANG", "HOME")}
    c = subprocess.run([sys.executable, "-I", "-B", str(MODS / "outil_lecteur_conception_propre_v3_2_1.py"), "envoyer",
                        "--envois", str(env)], capture_output=True, text=True, env={**sans, "OPENAI_API_KEY": cle + "\r"})
    assert c.returncode == 2 and cle not in c.stdout + c.stderr and "ASCII" in c.stderr
    assert not (env / "journal-depense-v3-2.jsonl").exists() and not O.contient_cle(tous_les_octets(tmp_path), cle)


@pytest.mark.parametrize("scenario,cause", [("panne", "TimeoutError"), ("panne_echappee", "ValueError")])
def test_B1_exception_de_transport_type_seul(tmp_path, monkeypatch, scenario, cause):
    """Le message d'une exception de transport (qui peut porter la clé sous une forme échappée) n'est jamais écrit."""
    env, _ = preparer(tmp_path)
    cle = 'sk-essai/"guillemet"\\barre-0123456789'
    r, d = envoyer(env, monkeypatch, scenarios={1: scenario}, cle=cle)
    err = json.loads((env / "erreur-L1-lot1-v3-2.json").read_text(encoding="utf-8"))
    assert err["cause_transport"] == cause and r["issue"] == "anomalie"
    assert not O.contient_cle(tous_les_octets(tmp_path), cle)


def test_B1_reponse_qui_porte_la_cle_expurgee_et_bloquante(tmp_path, monkeypatch):
    env, _ = preparer(tmp_path)
    cle = 'sk-essai/"guillemet"\\barre-0123456789'
    r, d = envoyer(env, monkeypatch, scenarios={1: "echo_cle"}, cle=cle)
    assert r["issue"] == "anomalie" and "cle_dans_la_reponse" in r["detail"]
    assert O.contient_cle(d.rendus[0], cle)  # l'amont l'a bien renvoyée, sous trois formes
    assert not O.contient_cle(tous_les_octets(tmp_path), cle) and b"[cle]" in (env / "reponse-L1-lot1-v3-2.json").read_bytes()
    j = O.lire_journal(env)
    rec = j["recus"]["envoi-L1-lot1-v3-2.corps.json"]
    assert rec["cle_expurgee"] is True and rec["brut_sha256"] == hashlib.sha256(d.rendus[0]).hexdigest()
    assert j["clos"]["envoi-L1-lot1-v3-2.corps.json"]["modele_servi"] == "[cle]"  # champ rendu par l'amont, expurgé
    assert "anomalie_d_envoi" in classer(env)["verdict"]


def test_B1_formes_de_cle():
    cle = 'sk-a/b"c\\d'
    formes = O.formes_de_cle(cle)
    for f in (cle, json.dumps(cle)[1:-1], 'sk-a\\/b"c\\d', "sk-a%2Fb%22c%5Cd", repr(cle)[1:-1]):
        assert f.encode() in formes
    for f in formes:
        texte = b"avant " + f + b" apres"
        assert O.contient_cle(texte, cle) and O.expurger(texte, cle) == (b"avant [cle] apres", True)
    assert O.expurger(b"rien", cle) == (b"rien", False)
    assert O.MOTIF_CLE.fullmatch(cle) and not O.MOTIF_CLE.fullmatch(cle + "\n") and not O.MOTIF_CLE.fullmatch("")


def test_B1_B2_transport_reel_sain_sur_la_boucle(tmp_path, monkeypatch, boucle):
    """Cas sain du transport réel : un seul POST, à l'adresse d'amont, avec l'en-tête attendu ; réponse 200 gardée."""
    recus = []
    etat = {}

    def amont(h):
        recus.append({"methode": h.command, "chemin": h.path, "autorisation": h.headers.get("Authorization"),
                      "corps_sha256": hashlib.sha256(h.corps_recu).hexdigest()})
        statut, rep = etat["doublure"].reponse(1, hashlib.sha256(h.corps_recu).hexdigest(), h.corps_recu)
        h.send_response(statut)
        h.send_header("Content-Type", "application/json")
        h.send_header("Content-Length", str(len(rep)))
        h.end_headers()
        h.wfile.write(rep)
    srv = boucle(amont)
    amont_local(monkeypatch, srv)
    env, man = preparer(tmp_path)
    etat["doublure"] = Doublure(env)
    monkeypatch.setenv("OPENAI_API_KEY", CLE_FACTICE)
    r = O.envoyer(env, envois_max=1)  # transport réel
    assert r["issue"] == "pause" and r["appels"] == 1
    assert recus == [{"methode": "POST", "chemin": "/v1/chat/completions", "autorisation": "Bearer " + CLE_FACTICE,
                      "corps_sha256": man["fichiers"]["envoi-L1-lot1-v3-2.corps.json"]}]
    assert O.lire_journal(env)["anomalies"] == [] and (env / "reponse-L1-lot1-v3-2.json").exists()
    assert not O.contient_cle(tous_les_octets(tmp_path), CLE_FACTICE)


# === v3.1 : B2, aucune redirection suivie ================================================================================

@pytest.mark.parametrize("code", [301, 302, 303, 307, 308])
def test_B2_redirection_jamais_suivie(monkeypatch, boucle, code):
    """Sonde s2 du contre-lecteur, en essai : l'autre hôte ne reçoit rien ; le 3xx revient comme statut."""
    recus = []

    def cible(h):
        recus.append({"hote": h.headers.get("Host"), "autorisation": h.headers.get("Authorization")})
        h.send_response(200)
        h.end_headers()
        h.wfile.write(b'{"ailleurs": true}')
    b = boucle(cible)

    def amont(h):
        h.send_response(code)
        h.send_header("Location", f"http://localhost:{b.server_address[1]}/ailleurs")
        h.send_header("Content-Length", "0")
        h.end_headers()
    a = boucle(amont)
    url = amont_local(monkeypatch, a)
    statut, rep = O.transport_reel(url, {"Content-Type": "application/json", "Authorization": "Bearer " + CLE_FACTICE},
                                   b"{}", 5)
    assert statut == code and rep != b'{"ailleurs": true}' and recus == []


def test_B2_redirection_par_envoyer_bloquante(tmp_path, monkeypatch, boucle):
    recus = []
    b = boucle(lambda h: (recus.append(h.headers.get("Authorization")), h.send_response(200), h.end_headers()))

    def amont(h):
        h.send_response(302)
        h.send_header("Location", f"http://localhost:{b.server_address[1]}/ailleurs")
        h.send_header("Content-Length", "0")
        h.end_headers()
    amont_local(monkeypatch, boucle(amont))
    env, man = preparer(tmp_path)
    monkeypatch.setenv("OPENAI_API_KEY", CLE_FACTICE)
    r = O.envoyer(env)
    assert r["issue"] == "anomalie" and "redirection_refusee" in r["detail"] and r["appels"] == 1 and recus == []
    err = json.loads((env / "erreur-L1-lot1-v3-2.json").read_text(encoding="utf-8"))
    assert err["statut"] == 302 and "redirection_refusee" in err["anomalies"]
    assert abs(r["depense_comptee_usd"] - man["garde_depense"]["envois"][0]["pire_cas_usd"]) < 1e-9
    monkeypatch.setenv("OPENAI_API_KEY", CLE_FACTICE)
    with pytest.raises(O.Refus, match="déjà arrêtée"):
        O.envoyer(env)


def test_B2_adresse_finale_differente_refusee(monkeypatch, boucle):
    """Défense en profondeur : si l'ouvreur rendait une autre adresse finale, la réponse n'est pas acceptée."""
    class Rep:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def geturl(self):
            return "http://autre.invalid/ailleurs"

        def read(self, n):
            return b"{}"

    class Ouvreur:
        def open(self, req, timeout):
            return Rep()
    monkeypatch.setattr(O.urllib.request, "build_opener", lambda *a: Ouvreur())
    with pytest.raises(O.ErreurTransport):
        O.transport_reel(O.URL_AMONT, {}, b"{}", 1)
    assert O.SansRedirection().redirect_request(None, None, 302, "", {}, "http://x/") is None


# === v3.1 : M1, aucune réponse hors du journal ===========================================================================

def test_M1_reponses_deposees_sans_journal_refusees(tmp_path):
    """Sonde s4 du contre-lecteur, en essai : réponses scellées déposées à la main, sans journal → refus partout."""
    env, _ = preparer(tmp_path)
    deposer_sans_journal(env)
    with pytest.raises(O.Refus, match="sans clôture conforme"):
        classer(env)
    with pytest.raises(O.Refus):
        O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    with pytest.raises(O.Refus):
        O.bilan(env)


def test_M1_reponse_recue_non_close(tmp_path, monkeypatch):
    """Un arrêt du processus entre l'écriture de la réponse et sa clôture : réponse gardée, consignée (`recu`), en vol,
    comptée au pire cas ; la vérification la dit non analysée (bloquant), l'envoi refuse de reprendre."""
    env, man = preparer(tmp_path)

    def interrompre(*a, **k):
        raise KeyboardInterrupt
    monkeypatch.setattr(O, "analyser_reponse", interrompre)
    with pytest.raises(KeyboardInterrupt):
        envoyer(env, monkeypatch)
    monkeypatch.undo()
    j = O.lire_journal(env)
    nom_c = "envoi-L1-lot1-v3-2.corps.json"
    assert j["en_vol"] == [nom_c] and nom_c in j["recus"] and (env / "reponse-L1-lot1-v3-2.json").exists()
    assert abs(j["depense_usd"] - man["garde_depense"]["envois"][0]["pire_cas_usd"]) < 1e-9
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert any(a["genre"] == "reponse_non_analysee" for a in lv["anomalies_bloquantes"])
    with pytest.raises(O.Refus, match="sans clôture"):
        envoyer(env, monkeypatch)


# === v3.1 : M2 et C6, un seul dossier d'envois ===========================================================================

def test_C6_second_dossier_refuse(tmp_path, monkeypatch):
    """Sonde s8 du contre-lecteur, en essai : après un arrêt, aucune seconde préparation ni aucun envoi d'une copie."""
    base = tmp_path / "s8"
    pf, h = ecrire_fiches(base, fiches_factices())
    pa = ecrire_attestation(base, h)
    rac = racine_de(base)
    env = envois_de(rac)
    opreparer(pf, pa, env, rac)
    r1, d1 = envoyer(env, monkeypatch, scenarios={3: "length"})
    assert r1["appels"] == 3
    with pytest.raises(O.Refus, match="pas vide"):
        opreparer(pf, pa, env, rac)
    with pytest.raises(O.Refus, match="seul"):
        opreparer(pf, pa, rac / "docs" / "notes" / "envois-bis", rac)
    copie = rac / "docs" / "notes" / "organisme-conception-propre-v1" / "lecture-g1-v3-2-bis" / "envois"
    shutil.copytree(env, copie)
    with pytest.raises(O.Refus, match="seul"):
        envoyer(copie, monkeypatch)
    with pytest.raises(O.Refus, match="C6"):  # la copie, même hors d'usage, fait refuser le dossier vrai
        O.bilan(env)
    shutil.rmtree(copie.parent)
    ailleurs = rac / "runs" / "autre"
    ailleurs.mkdir(parents=True)
    shutil.copyfile(env / "manifeste-relecture-v3-2.json", ailleurs / "manifeste-envois-v3.json")
    with pytest.raises(O.Refus, match="C6"):
        envoyer(env, monkeypatch)
    rac2 = racine_de(tmp_path / "autre")  # une racine neuve où traîne un manifeste v3 : préparation refusée
    pf2, h2 = ecrire_fiches(tmp_path / "autre", fiches_factices())
    pa2 = ecrire_attestation(tmp_path / "autre", h2)
    (rac2 / "docs" / "x").mkdir(parents=True)
    (rac2 / "docs" / "x" / "manifeste-envois-v3.json").write_text("{}")
    with pytest.raises(O.Refus, match="C6"):
        opreparer(pf2, pa2, envois_de(rac2), rac2)
    assert len(d1.appels) == 3  # rien n'est reparti


def test_C6_depense_anterieure_bornee(tmp_path):
    _, man = preparer(tmp_path / "a", plafond_usd=10.45, depense_anterieure_usd=1.2)
    assert man["garde_depense"]["plafond_disponible_usd"] == 10.45 and man["garde_depense"]["depense_anterieure_usd"] == 1.2
    with pytest.raises(O.Refus, match="antérieure"):
        preparer(tmp_path / "b", plafond_usd=10.46, depense_anterieure_usd=1.2)


# === v3.1 : M3, réponse payée gardée, analyse qui ne lève pas ============================================================

@pytest.mark.parametrize("scenario,genre", [("details_non_objets", "usage_absent"),
                                            ("message_non_objet", "contenu_absent")])
def test_M3_reponse_200_mal_formee_gardee_brute(tmp_path, monkeypatch, scenario, genre):
    """Sonde s5 du contre-lecteur, en essai : aucune exception ; la réponse payée est écrite brute, consignée avant son
    analyse, puis l'analyse la juge (anomalie bloquante)."""
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: scenario})
    assert r["issue"] == "anomalie" and genre in r["detail"]
    assert (env / "reponse-L1-lot1-v3-2.json").read_bytes() == d.rendus[0]
    lignes = [json.loads(x) for x in (env / "journal-depense-v3-2.jsonl").read_text(encoding="utf-8").splitlines()]
    assert [x["evenement"] for x in lignes] == ["envoi", "recu", "clos"]
    assert lignes[1]["brut_sha256"] == hashlib.sha256(d.rendus[0]).hexdigest() == lignes[1]["fichier_sha256"]


@pytest.mark.parametrize("scenario", ["erreur_chaine", "erreur_liste", "corps_liste"])
def test_M3_erreur_mal_formee_sans_exception(tmp_path, monkeypatch, scenario):
    """Sonde s6 du contre-lecteur, en essai : un corps d'erreur de forme inattendue laisse un fichier d'erreur."""
    env, _ = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: scenario})
    err = json.loads((env / "erreur-L1-lot1-v3-2.json").read_text(encoding="utf-8"))
    assert r["issue"] == "anomalie" and err["statut"] == 502 and err["erreur"] == {"type": None, "code": None}
    assert O.lire_journal(env)["en_vol"] == []


def test_M3_filet_de_l_analyse(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)

    def tombe(*a, **k):
        raise ValueError("forme imprévue")
    monkeypatch.setattr(O, "analyser_reponse", tombe)
    r, d = envoyer(env, monkeypatch)
    assert r["issue"] == "anomalie" and "analyse_en_echec" in r["detail"]
    assert (env / "reponse-L1-lot1-v3-2.json").read_bytes() == d.rendus[0]
    assert abs(r["depense_comptee_usd"] - man["garde_depense"]["envois"][0]["pire_cas_usd"]) < 1e-9


def test_M3_reponse_trop_grande(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: "trop_grand"})
    assert r["issue"] == "anomalie" and "reponse_trop_grande" in r["detail"]
    assert not (env / "reponse-L1-lot1-v3-2.json").exists() and (env / "erreur-L1-lot1-v3-2.json").exists()


# === v3.1 : M5, un artefact par garde (mutants survivants du contre-lecteur) =============================================

@pytest.mark.parametrize("scenario", ["modele", "majuscules", "sans_usage", "usage_incoherent", "zeros", "cout_excessif",
                                      "429", "panne", "illisible", "refus", "vide", "deux_choix", "objet",
                                      "content_filter", "palier_autre", "echo_cle"])
def test_R2_aucune_reprise_apres_une_anomalie(tmp_path, monkeypatch, scenario):
    """R2 du contre-lecteur : après toute anomalie (pas seulement la fin `length`), aucune reprise."""
    env, _ = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={2: scenario})
    assert r["issue"] == "anomalie" and len(d.appels) == 2
    with pytest.raises(O.Refus, match="déjà arrêtée"):
        envoyer(env, monkeypatch)


@pytest.mark.parametrize("scenario,genre", [("deux_choix", "choix_non_unique"), ("vide", "contenu_absent"),
                                            ("objet", "reponse_illisible")])
def test_F2_F3_F4_forme_de_la_reponse(tmp_path, monkeypatch, scenario, genre):
    """F2, F3, F4 du contre-lecteur : plusieurs choix, contenu vide, objet autre que chat.completion : arrêt."""
    env, _ = preparer(tmp_path)
    r, d = envoyer(env, monkeypatch, scenarios={1: scenario})
    assert r["issue"] == "anomalie" and genre in r["detail"].split(" : ")[1].split(", ") and len(d.appels) == 1


@pytest.mark.parametrize("scenario", ["content_filter", "tool_calls", "fin_absente", "fin_lisible"])
def test_F1_verification_toute_fin_autre_que_stop(tmp_path, scenario):
    """F1 du contre-lecteur : à la vérification, toute fin autre que `stop` est nommée (pas seulement `length`)."""
    env, _ = preparer(tmp_path)
    lire(env, scenarios={1: scenario})
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert "fin_non_stop" in [a["genre"] for a in lv["anomalies_bloquantes"] if a["lot"] == 1]


def _manifeste_rescelle(env, change):
    p = env / "manifeste-relecture-v3-2.json"
    m = json.loads(p.read_text(encoding="utf-8"))
    change(m)
    resceller(p, json.dumps(m, ensure_ascii=False, indent=1) + "\n")


def _corps_rescelle(env, nom, change):
    p = env / nom
    c = json.loads(p.read_text(encoding="utf-8"))
    change(c)
    texte = json.dumps(c, ensure_ascii=False)
    resceller(p, texte)

    def suivre(m):
        m["fichiers"][nom] = hashlib.sha256(texte.encode()).hexdigest()
        e = next(x for x in m["garde_depense"]["envois"] if x["envoi"] == nom)
        e["octets"] = len(texte.encode())
        e["pire_cas_usd"] = round(O.pire_cas_usd(e["octets"], m["garde_depense"]["prix_usd_par_million"]), 6)
    _manifeste_rescelle(env, suivre)


@pytest.mark.parametrize("cas", ["plafond_nan", "plafond_14_5", "anterieure_negative", "plafond_moins_anterieure",
                                 "appels_19", "appels_13", "prix_sortie", "source", "palier_flex_prix_standard",
                                 "palier_inconnu", "lecteur_sortie", "pire_cas_abaisse", "corps_sortie", "corps_palier",
                                 "corps_cle_en_plus", "ordre"])
def test_D6_D7_m1_manifeste_rescelle_revalide_a_l_envoi(tmp_path, monkeypatch, cas):
    """D6, D7 et m1 du contre-lecteur (sonde s10) : un manifeste ou un corps rescellés hors des bornes ou des prix du code
    sont refusés à l'envoi, avant la clé et avant tout appel."""
    env, man = preparer(tmp_path)
    g = "garde_depense"
    changements = {
        "plafond_nan": lambda m: m[g].update(plafond_usd=float("nan")),
        "plafond_14_5": lambda m: m[g].update(plafond_usd=14.5),
        "anterieure_negative": lambda m: m[g].update(depense_anterieure_usd=-1.0),
        "plafond_moins_anterieure": lambda m: m[g].update(depense_anterieure_usd=5.0),
        "appels_19": lambda m: m[g].update(appels_max=19),
        "appels_13": lambda m: m[g].update(appels_max=13),
        "prix_sortie": lambda m: m[g]["prix_usd_par_million"].update(sortie=1.0),
        "source": lambda m: m[g]["prix_usd_par_million"].update(source="barème d'essai"),
        "palier_flex_prix_standard": lambda m: m.update(palier="flex"),
        "palier_inconnu": lambda m: m.update(palier="fast"),
        "lecteur_sortie": lambda m: m["lecteur"].update(max_completion_tokens=65536),
        "pire_cas_abaisse": lambda m: m[g]["envois"][0].update(pire_cas_usd=0.0),
        "ordre": lambda m: m["ordre_d_envoi"].reverse(),
    }
    if cas == "corps_sortie":
        _corps_rescelle(env, man["ordre_d_envoi"][0], lambda c: c.update(max_completion_tokens=99999))
    elif cas == "corps_palier":
        _corps_rescelle(env, man["ordre_d_envoi"][0], lambda c: c.update(service_tier="priority"))
    elif cas == "corps_cle_en_plus":
        _corps_rescelle(env, man["ordre_d_envoi"][0], lambda c: c.update(temperature=0))
    else:
        _manifeste_rescelle(env, changements[cas])
    monkeypatch.setenv("OPENAI_API_KEY", CLE_FACTICE)
    d = Doublure(env)
    with pytest.raises(O.Refus):
        O.envoyer(env, transport=d)
    assert d.appels == [] and not (env / "journal-depense-v3-2.jsonl").exists()
    assert os.environ.get("OPENAI_API_KEY") == CLE_FACTICE  # refus avant la lecture de la clé


def test_D2_redondant_avec_la_revalidation_du_manifeste(tmp_path, monkeypatch):
    """D2 du contre-lecteur (pire cas pris du manifeste seul) : sans effet observable, et c'est voulu. Pour tout manifeste
    accepté par `envoyer`, le pire cas consigné égale, à l'arrondi de 10⁻⁶ près, celui recalculé sur les octets envoyés ;
    un manifeste où il diffère est refusé avant tout appel (essai précédent, cas « pire_cas_abaisse »)."""
    env, man = preparer(tmp_path)
    prix, plafond, appels, palier = O.valider_manifeste(man, env)
    for e in man["garde_depense"]["envois"]:
        exact = O.pire_cas_usd(len((env / e["envoi"]).read_bytes()), prix)
        assert abs(max(e["pire_cas_usd"], exact) - exact) <= 5e-7 and e["pire_cas_usd"] == round(exact, 6)


def test_R3_envoi_consigne_deux_fois_refuse(tmp_path):
    """R3 du contre-lecteur : un journal (même bien chaîné) qui envoie deux fois le même lot est refusé."""
    for cas in ("ouvert", "clos"):
        env, _ = preparer(tmp_path / cas)
        j = O.lire_journal(env)
        nom = "envoi-L1-lot1-v3-2.corps.json"
        O.ajouter_journal(env, j, {"evenement": "envoi", "envoi": nom, "octets": 1, "pire_cas_usd": 1.0})
        if cas == "clos":
            O.ajouter_journal(env, j, {"evenement": "clos", "envoi": nom, "cout_usd": 0.5, "anomalies": []})
        O.ajouter_journal(env, j, {"evenement": "envoi", "envoi": nom, "octets": 1, "pire_cas_usd": 1.0})
        with pytest.raises(O.Refus, match="envoyé deux fois"):
            O.lire_journal(env)


def test_journal_mal_forme_refuse(tmp_path):
    env, _ = preparer(tmp_path)
    for ev in ({"evenement": "envoi", "octets": 1, "pire_cas_usd": 1.0},
               {"evenement": "envoi", "envoi": "x", "pire_cas_usd": float("inf")},
               {"evenement": "recu", "envoi": "x"}, {"evenement": "clos", "envoi": "y", "cout_usd": 0, "anomalies": []},
               {"evenement": "autre"}):
        p = env / "journal-depense-v3-2.jsonl"
        if p.exists():
            p.unlink()
        j = O.lire_journal(env)
        try:
            O.ajouter_journal(env, j, ev)
        except ValueError:  # l'infini n'est pas du JSON : refusé dès l'écriture
            continue
        with pytest.raises(O.Refus):
            O.lire_journal(env)


# === v3.1 : palier Flex ==================================================================================================

def test_palier_flex_corps_manifeste_prix_et_envoi(tmp_path, monkeypatch):
    env, man = preparer(tmp_path, palier="flex")
    assert man["palier"] == "flex" and man["lecteur"]["service_tier"] == "flex"
    assert man["garde_depense"]["prix_usd_par_million"] == {"entree": 5.0, "cache": 0.5, "sortie": 25.0,
                                                             "source": O.SOURCE_PRIX}
    for e in man["garde_depense"]["envois"]:
        corps = json.loads((env / e["envoi"]).read_text(encoding="utf-8"))
        assert corps["service_tier"] == "flex"
        assert abs(e["pire_cas_usd"] - ((e["octets"] + 1024) * 5 / 1e6 + 32768 * 25 / 1e6)) < 1e-6
    r, d = envoyer(env, monkeypatch)
    assert r["issue"] == "fait" and r["palier"] == "flex"
    attendu = sum((g["octets"] // 4 * 5 + 3000 * 25) / 1e6 for g in man["garde_depense"]["envois"])
    assert abs(r["depense_comptee_usd"] - attendu) < 1e-5
    assert classer(env)["lisible"]


@pytest.mark.parametrize("palier,scenario", [("flex", "palier_default"), ("flex", "palier_autre"),
                                             ("standard", "palier_autre")])
def test_palier_servi_autre_bloquant(tmp_path, monkeypatch, palier, scenario):
    env, _ = preparer(tmp_path, palier=palier)
    r, d = envoyer(env, monkeypatch, scenarios={1: scenario})
    assert r["issue"] == "anomalie" and "palier_servi_different" in r["detail"] and len(d.appels) == 1
    lv = O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])
    assert "palier_servi_different" in [a["genre"] for a in lv["anomalies_bloquantes"] if a["lot"] == 1]


def test_palier_standard_sans_champ_et_prix_lus(tmp_path):
    env, man = preparer(tmp_path)
    corps = json.loads((env / man["ordre_d_envoi"][0]).read_text(encoding="utf-8"))
    assert "service_tier" not in corps and man["lecteur"]["service_tier"] is None
    texte = (RACINE / O.PIECES_PRIX["prix"][0]).read_text(encoding="utf-8")
    assert O.LIGNES_SOURCE_PRIX["standard"] in texte and O.LIGNES_SOURCE_PRIX["flex"] in texte
    assert O.PRIX_LUS == {"standard": {"entree": 10.0, "cache": 1.0, "sortie": 50.0},
                          "flex": {"entree": 5.0, "cache": 0.5, "sortie": 25.0}}
    assert O.PLAFOND_ABSOLU_USD == 11.65


# === v3.1 : bilan (conditions C3 et C5) et règle inchangée ================================================================

def test_bilan_C3_C5(tmp_path, monkeypatch):
    env, man = preparer(tmp_path)
    envoyer(env, monkeypatch, envois_max=1)
    b = O.bilan(env)
    c = b["clotures"][0]
    assert b["clos"] == 1 and b["attendus"] == 12 and not b["pret_pour_verifier"] and b["anomalies"] == []
    assert c["modele_servi"] == "gpt-6-astra" and c["palier_servi"] == "default" and c["anomalies"] == []
    assert c["jetons"]["reasoning_tokens"] <= c["jetons"]["completion_tokens"] <= 32768
    assert c["cout_usd"] <= c["pire_cas_usd"]
    assert abs(c["pire_cas_usd"] - man["garde_depense"]["envois"][0]["pire_cas_usd"]) < 1e-9  # arrondi à 10⁻⁶ (D2 de la v3.1)
    envoyer(env, monkeypatch)
    assert O.bilan(env)["pret_pour_verifier"]


def _objets(chemin):
    t = Path(chemin).read_text(encoding="utf-8")
    d = {}
    for n in ast.parse(t).body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
            corps = n.body[1:] if (n.body and isinstance(n.body[0], ast.Expr)
                                   and isinstance(getattr(n.body[0], "value", None), ast.Constant)) else n.body
            d[n.name] = ast.dump(type(n)(**{**n.__dict__, "body": corps or [ast.Pass()]}))
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            d[n.targets[0].id] = ast.dump(n.value)
    return d


def test_regle_de_lecture_inchangee_v3_1_v3_2():
    """La règle de lecture (vue, pile, ordres, lots, message, vérification, garde, transport) est identique à la v3.1 ;
    seuls changent les objets que la v3.2 déclare ; au classement, seuls changent ceux de la règle v2."""
    a, b = _objets(V3_1 / "outil_lecteur_conception_propre_v3_1.py"), _objets(MODS / "outil_lecteur_conception_propre_v3_2_1.py")
    changes = {"VERSION", "RACINE_DEFAUT", "PIECES", "PLAFOND_ABSOLU_USD", "SUFFIXE", "MANIFESTE", "DOSSIER_ENVOIS_REL",
               "verifier_unicite", "JOURNAL", "PILE", "CLE_LECTURES"}
    neufs = {"LIGNE_GO_USD", "DEPENSE_AVANT_PREMIERE_LECTURE_USD", "DEPENSE_PREMIERE_LECTURE_USD", "PREMIERE_LECTURE",
             "MOTIFS_MANIFESTES", "verifier_premiere_lecture"}
    assert set(b) - set(a) == neufs and set(a) - set(b) == set()
    differents = {n for n in a if a[n] != b[n]}
    assert differents <= changes, differents - changes
    for nom in ("vue_lecteur", "admissibilite", "construire_pile", "enfants_ordres", "ordres_lectures", "decouper_lots",
                "etiquette", "texte_message", "passage_dans", "verifier_entree", "entrees_catalogue", "extraire_json",
                "verifier_attestation", "verifier_fiches_de_run", "ORDRE_VUE", "TABLE_TYPO", "ENTROPIE_ORDRES",
                "verifier_lot", "cles_manquantes", "TAILLE_LOT", "MODELE_LECTEUR", "MAX_APPELS", "MAX_SORTIE", "EFFORTS",
                "URL_AMONT", "LONGUEUR_MIN_PASSAGE", "CELLULE_MECANISME", "preparer", "envoyer", "bilan", "lire_reponse",
                "verifier_lecture", "charger_envois", "valider_manifeste", "analyser_reponse", "cout_usage", "lire_cle",
                "transport_reel", "expurger", "lire_journal", "ajouter_journal", "controler_coherence", "PRIX_LUS",
                "PALIERS_SERVIS_ADMIS", "ANOMALIES_BLOQUANTES", "main"):
        assert a[nom] == b[nom], nom
    a, b = _objets(V3_1 / "classer_conception_propre_v3_1.py"), _objets(MODS / "classer_conception_propre_v3_2_1.py")
    for nom in ("retenir", "classer", "rangs_departage", "temoin_permute", "kappa_accord", "test_permutation", "holm",
                "ENTROPIE_TEST", "PERMUTATIONS", "SEUIL_P", "TAILLE_TRANCHE", "COUT_RANG", "L1_MIN_PUBLIEES",
                "E5_PART", "score_C"):
        assert a[nom] == b[nom], nom
    assert (K.L4_KAPPA_MIN, K.L4_ACCORD_MIN) == (0.4, 0.8)
    for nom in ("PORTES", "score_S", "classement", "resume_md", "main"):
        assert a[nom] != b[nom], nom
    assert "designer_detachee" not in b and "DESIGNATIONS" not in b


def test_M1_erreur_nommee_au_journal_effacee(tmp_path, monkeypatch):
    """Un fichier d'erreur nommé par le journal puis effacé : refus (le journal et le dossier ne s'accordent plus),
    au lieu d'un verdict E2 qui tairait l'effacement."""
    env, _ = preparer(tmp_path)
    envoyer(env, monkeypatch, scenarios={2: "429"})
    p = env / "erreur-L1-lot2-v3-2.json"
    p.unlink()
    Path(str(p) + ".sha256").unlink()
    with pytest.raises(O.Refus, match="nommé au journal"):
        classer(env)
    with pytest.raises(O.Refus, match="nommé au journal"):
        O.bilan(env)


def test_prix_ligne_source_verifiee(tmp_path, monkeypatch):
    """La ligne du tableau de chaque palier est cherchée dans la pièce des prix : absente, la préparation est refusée."""
    monkeypatch.setitem(O.LIGNES_SOURCE_PRIX, "flex", "| Flex / Batch | 9,99 | 0,50 | 25,00 |")
    preparer(tmp_path / "a")  # standard : sa ligne est là
    with pytest.raises(O.Refus, match="ligne du palier flex"):
        preparer(tmp_path / "b", palier="flex")


def test_classement_racine_autre_refusee(tmp_path):
    env, _ = preparer(tmp_path / "a")
    lire(env)
    with pytest.raises(O.Refus, match="racine différente"):
        K.classement(env, racine_de(tmp_path / "b"))
    py = [sys.executable, "-I", "-B", str(MODS / "outil_lecteur_conception_propre_v3_2_1.py"), "verifier", "--envois",
          str(env), "--racine", str(racine_de(tmp_path / "b"))]
    c = subprocess.run(py, capture_output=True, text=True)
    assert c.returncode == 2 and "racine" in c.stderr


# --- ajoutés après la première passe du banc de l'auteur (survivants 009, 116, 143, 145) ---------------------------------

def test_lire_reponse_refuse_une_reponse_non_scellee(tmp_path):
    """`lire_reponse` garde son propre contrôle de sceau, derrière la confrontation journal-dossier (défense en
    profondeur) : une réponse sans compagnon est refusée, une réponse scellée de forme inattendue est une anomalie."""
    p = tmp_path / "reponse-L1-lot1-v3-2.json"
    p.write_text(json.dumps({"object": "chat.completion"}), encoding="utf-8")
    with pytest.raises(O.Refus, match="non scellé"):
        O.lire_reponse(p)
    O.ecrire_scelle(tmp_path / "r2.json", "{}")
    assert O.lire_reponse(tmp_path / "r2.json")[2]


def test_prix_valides_refuse_nul_negatif_ou_non_fini():
    """Les prix sont des constantes lues, mais leur contrôle reste exact (garde des prix du manifeste et des constantes)."""
    for k in ("entree", "cache", "sortie"):
        for v in (0, 0.0, -1.0, float("nan"), float("inf"), "1", True, None):
            with pytest.raises(O.Refus):
                O.prix_valides({"entree": 10.0, "cache": 1.0, "sortie": 50.0, "source": "x", k: v})
    with pytest.raises(O.Refus, match="cache"):
        O.prix_valides({"entree": 1.0, "cache": 2.0, "sortie": 50.0, "source": "x"})
    for palier in O.PALIERS:
        assert O.prix_valides({**O.PRIX_LUS[palier], "source": O.SOURCE_PRIX})


def test_C6_chemin_fixe_seul_accepte_dans_une_racine_neuve(tmp_path, monkeypatch):
    """Le chemin fixe est exigé même quand aucun autre dossier n'existe : préparer ailleurs, ou envoyer depuis un dossier
    déplacé, est refusé (et non seulement par la recherche d'un second manifeste)."""
    rac = racine_de(tmp_path / "a")
    pf, h = ecrire_fiches(tmp_path / "a", fiches_factices())
    pa = ecrire_attestation(tmp_path / "a", h)
    with pytest.raises(O.Refus, match="est accepté"):
        opreparer(pf, pa, rac / "envois", rac)
    assert not (rac / "envois").exists()
    env = envois_de(rac)
    opreparer(pf, pa, env, rac)
    deplace = rac / "docs" / "x" / "y" / "z" / "envois"  # même profondeur sous la racine, autre chemin
    deplace.parent.mkdir(parents=True)
    shutil.move(str(env), str(deplace))
    for geste in (lambda: envoyer(deplace, monkeypatch), lambda: O.bilan(deplace),
                  lambda: O.verifier_lecture(deplace, "L1", O.lire_piece(RACINE, "catalogue")[0])):
        with pytest.raises(O.Refus, match="est accepté"):
            geste()


# === v3.2 : C6 à côté de la première lecture, plafond absolu, témoins v2, règle v2 ======================================

def _premiere(rac, nom):
    return Path(rac) / O.PREMIERE_LECTURE[nom][0]


@pytest.mark.parametrize("geste", ["manifeste_absent", "journal_altere", "releve_altere", "releve_incoherent"])
def test_C6_v3_2_premiere_lecture_intacte_exigee(tmp_path, monkeypatch, geste):
    """La première lecture doit être là, intacte, et son relevé porter la dépense retranchée : sinon, les quatre actions
    refusent (la dépense ne repart jamais de zéro)."""
    pf, h = ecrire_fiches(tmp_path, fiches_factices())
    pa = ecrire_attestation(tmp_path, h)
    rac = racine_de(tmp_path)
    env = envois_de(rac)
    opreparer(pf, pa, env, rac)  # cas sain
    if geste == "manifeste_absent":
        _premiere(rac, "manifeste").unlink()
        motif = "manifeste absent"
    elif geste == "journal_altere":
        with open(_premiere(rac, "journal"), "ab") as f:
            f.write(b"\n")
        motif = "journal"
    elif geste == "releve_altere":
        p = _premiere(rac, "releve")
        p.write_text(p.read_text(encoding="utf-8").replace("2.556635", "0.556635"), encoding="utf-8")
        motif = "releve"
    else:  # relevé réécrit et réépinglé : le contenu lui-même est contrôlé
        p = _premiere(rac, "releve")
        p.write_text(p.read_text(encoding="utf-8").replace("2.556635", "0.556635"), encoding="utf-8")
        pins = dict(O.PREMIERE_LECTURE)
        pins["releve"] = (pins["releve"][0], hashlib.sha256(p.read_bytes()).hexdigest())
        monkeypatch.setattr(O, "PREMIERE_LECTURE", pins)
        motif = "incohérent"
    for g in (lambda: O.bilan(env), lambda: envoyer(env, monkeypatch),
              lambda: O.verifier_lecture(env, "L1", O.lire_piece(RACINE, "catalogue")[0])):
        with pytest.raises(O.Refus, match=motif):
            g()
    env2 = envois_de(racine_de(tmp_path / "b"))
    pf2, h2 = ecrire_fiches(tmp_path / "b", fiches_factices())
    pa2 = ecrire_attestation(tmp_path / "b", h2)
    rac2 = racine_de(tmp_path / "b")
    if geste == "manifeste_absent":
        _premiere(rac2, "manifeste").unlink()
        with pytest.raises(O.Refus, match="première lecture"):
            opreparer(pf2, pa2, env2, rac2)
        assert not env2.exists()


def test_C6_v3_2_un_seul_dossier_de_relecture(tmp_path, monkeypatch):
    """Seul le manifeste de la première lecture, à son chemin, est toléré à côté de celui de la relecture : une seconde
    préparation, une copie, un manifeste v3 ou v3.2 égaré sous `docs/` ou `runs/`, une copie renommée du manifeste v3.1,
    font refuser."""
    env, _ = preparer(tmp_path)
    rac = O.racine_du_dossier(env)
    assert O.bilan(env)["appels"] == 0
    for chemin, source in ((rac / "runs" / "x" / "manifeste-relecture-v3-2.json", env / O.MANIFESTE),
                           (rac / "docs" / "y" / "manifeste-envois-v3.json", env / O.MANIFESTE),
                           (rac / "docs" / "z" / "manifeste-envois-v3-1.json", _premiere(rac, "manifeste"))):
        chemin.parent.mkdir(parents=True)
        shutil.copyfile(source, chemin)
        with pytest.raises(O.Refus, match="C6"):
            O.bilan(env)
        with pytest.raises(O.Refus, match="C6"):
            envoyer(env, monkeypatch)
        shutil.rmtree(chemin.parent)
    assert O.bilan(env)["appels"] == 0


def test_C6_v3_2_manifeste_hors_du_motif_de_la_v3_1(tmp_path):
    """Le manifeste de la relecture échappe au motif de la v3.1 : après la préparation v3.2, la v3.1 voit encore son seul
    manifeste et reste vérifiable ; sous l'ancien nom, elle refuserait."""
    import fnmatch
    assert not fnmatch.fnmatch(O.MANIFESTE, "manifeste-envois-v3*.json")
    assert fnmatch.fnmatch(O.MANIFESTE, O.MOTIFS_MANIFESTES[1])
    o31 = _charger("outil_v3_1_ref_c6", "outil_lecteur_conception_propre_v3_1.py", V3_1)
    env, _ = preparer(tmp_path)
    rac = O.racine_du_dossier(env)
    o31.verifier_unicite(rac, _premiere(rac, "manifeste"))  # la v3.1 ne voit pas la v3.2
    ancien = env / "manifeste-envois-v3-2.json"
    shutil.copyfile(env / O.MANIFESTE, ancien)
    with pytest.raises(o31.Refus, match="C6"):
        o31.verifier_unicite(rac, _premiere(rac, "manifeste"))
    ancien.unlink()


def test_plafond_absolu_v3_2(tmp_path):
    import math
    assert O.PLAFOND_ABSOLU_USD == math.floor((21.0 - 6.791087 - 2.556635) * 100) / 100 == 11.65
    assert (O.LIGNE_GO_USD, O.DEPENSE_AVANT_PREMIERE_LECTURE_USD, O.DEPENSE_PREMIERE_LECTURE_USD) == (21.0, 6.791087, 2.556635)
    with pytest.raises(O.Refus, match="GO-2026-11-13-06"):
        preparer(tmp_path / "a", plafond_usd=11.66)
    with pytest.raises(O.Refus, match="antérieure"):
        preparer(tmp_path / "b", plafond_usd=11.65, depense_anterieure_usd=0.01)
    _, man = preparer(tmp_path / "c", plafond_usd=11.64, depense_anterieure_usd=0.01)
    assert man["garde_depense"]["plafond_usd"] == 11.64 and man["garde_depense"]["plafond_disponible_usd"] == 11.64
    assert O.verifier_premiere_lecture(RACINE)["depense_comptee_usd"] == 2.556635  # le dépôt lui-même


def test_temoins_v2_dans_la_pile_et_jamais_marques(tmp_path):
    env, man = preparer(tmp_path)
    pile = json.loads((env / O.PILE).read_text(encoding="utf-8"))
    tem = [p for p in pile["fiches"] if p["origine"] == "temoin"]
    assert len(tem) == 20 and all(p["id"].startswith("T2-") for p in tem)
    assert sorted(p["famille"] for p in tem) == sorted(["vrai", "jumeau"] + ["faux"] * 3 + ["publie"] * 7 + ["hasard"] * 8)
    src = {t["code"]: t for g in ("temoins_lecteur", "temoins_hasard")
           for t in json.loads(O.lire_piece(RACINE, g)[0])["temoins"]}
    for p in tem:
        assert p["vue"] == O.vue_lecteur(src[p["id"]]["fiche"])[0]
        assert p["attendu"] == src[p["id"]]["attendu"]
    interdits = ["T2-", '"chaine"', "coherente", '"epreuve"', '"attendu"', "criteres_porteurs", "reecriture",
                 "sens_implique", "jumeau_de"]
    for f in env.glob("envoi-*.txt"):
        texte = f.read_text(encoding="utf-8")
        assert not any(s in texte for s in interdits)
    assert man["pieces"]["regle"]["sha256"] == O.PIECES["regle"][1]
    assert man["pieces"]["temoins_lecteur"]["chemin"].endswith("relecture-exploratoire-v2/temoins-lecteur-v2.json")


def test_regle_v2_portes_et_score():
    assert K.PORTES == ("R2", "R3") and K.ENTROPIE_SEPARATION == 2026111404
    assert K.score_S(TOUT1) == 5 and K.score_C(TOUT1) == 6
    assert K.score_C({**TOUT1, "R7": 0}) == 5 and K.score_C({**TOUT1, "R1": 0, "R7": 0}) == 4
    assert K.score_C({**TOUT1, "R3": 0}) == 0 and K.score_C({**TOUT1, "R2": 0}) == 0
    assert K.score_C({**TOUT1, "N": "C1"}) == 0 and K.portes_manquantes({**TOUT1, "R7": 0}) == []


def test_separation_unitaire():
    s = K.separation(False, [1] * 8, [0] * 8, 20_000)
    assert s["issue"] == "pas de séparation" and not s["lu"] and s["test_R7_seul"]["p"] < 0.05  # calculé, non lu
    assert K.separation(True, [1] * 8, [0] * 8, 20_000)["issue"] == "séparation réelle (portée par R7)"
    assert K.separation(True, [1] * 8, [1] * 8, 20_000)["issue"] == "séparation non établie sur R7 (n = 8)"
    a = K.separation(True, [1, 0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1, 0], 20_000)["test_R7_seul"]
    b = K.test_permutation([1, 0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1, 0], np.random.SeedSequence(2026111404), 20_000)
    assert a == b


def test_separation_non_etablie_sur_R7_bout_en_bout(tmp_path):
    """L5 v2 rejette par les critères de forme (R5, R6), mais R7 ne sépare pas : « séparation non établie sur R7 (n = 8) »."""
    env, _ = preparer(tmp_path)

    def m(L, i, p, v):
        if p["famille"] == "hasard":
            return {**TOUT1, "R5": 0, "R6": 0}, ()
        if i == id_de("A5"):
            return {**v, "N": "aucune"}, ()
        if i == id_de("A6"):
            return {**v, "R2": 1}, ()
        return v, ()
    lire(env, modif=m)
    r = classer(env)
    assert r["L5"]["rejet"] and r["separation"]["issue"] == "séparation non établie sur R7 (n = 8)" and r["separation"]["lu"]
    assert r["separation"]["test_R7_seul"]["p"] > 0.05 and r["designees"] == [] and r["lisible"]
    assert "séparation non établie sur R7" in r["verdict"] and "séparation non établie sur R7" in K.resume_md(r)
    assert "de forme" not in r["verdict"]


def test_exactitude_exclut_les_valeurs_non_fixees(tmp_path):
    env, _ = preparer(tmp_path)
    lire(env)
    r = classer(env)
    lect = json.loads(O.lire_piece(RACINE, "temoins_lecteur")[0])["temoins"]
    non_fixes_R7 = sum(t["attendu"]["R7"] is None for t in lect)
    assert non_fixes_R7 == 1  # T2-F3
    assert r["exactitude_lecteur"]["L1"]["R7"]["sur"] == len(lect) - non_fixes_R7
    assert r["exactitude_lecteur"]["L1"]["N"]["sur"] == len(lect) + 8  # N attendu « aucune » pour le hasard


def test_descriptifs_premiere_lecture_avec_fiches_communes(tmp_path, monkeypatch):
    env, _ = preparer(tmp_path)
    lire(env)
    r = classer(env)
    rac = O.racine_du_dossier(env)
    reelles = [id_de(n) for n in PLAN]
    faux = {i: dict(r["retenu"][i]) for i in reelles}
    faux[id_de("A1")]["R7"] = 0          # une valeur de moins à la « première lecture »
    faux[id_de("A6")]["R2"] = 1          # une fiche écartée qui passait
    p = rac / K.PREMIERE_CLASSEMENT[0]
    p.write_text(json.dumps({"retenu": faux}), encoding="utf-8")
    monkeypatch.setattr(K, "PREMIERE_CLASSEMENT", (K.PREMIERE_CLASSEMENT[0], hashlib.sha256(p.read_bytes()).hexdigest()))
    r2 = classer(env)
    c = r2["relecture_contre_premiere_lecture"]
    assert c["fiches_communes"] == 8 and c["par_critere"]["R7"]["accord_brut"] == 7 / 8
    assert c["par_critere"]["R2"]["premiere_1"] == 8 and c["par_critere"]["R2"]["relecture_1"] == 7
    v = r2["regle_v2_sur_la_premiere_lecture"]
    assert v["fiches_communes"] == 8 and v["statut"][id_de("A6")] == "neuve" and id_de("A6") in v["ordre_neuves"]
    assert 0 <= v["deux_premieres_communes_avec_la_relecture"] <= 2
    assert r2["verdict"] == r["verdict"] and r2["rang_exploratoire"] == r["rang_exploratoire"]  # sans effet sur le rang
    monkeypatch.setattr(K, "PREMIERE_CLASSEMENT", (K.PREMIERE_CLASSEMENT[0], "0" * 64))
    with pytest.raises(O.Refus, match="première lecture"):
        classer(env)


def test_v3_2_1_issue_non_lue_quand_le_classement_est_non_lisible(tmp_path):
    """Constat m2 : un classement non lisible où L5 v2 rejette rend l'issue suivie de « non lue »."""
    env, _ = preparer(tmp_path)
    lire(env, modif=lambda L, i, p, v: ({**v, "N": "aucune"} if i in ("T2-C2", "T2-C1", "T2-C3") else v, ()))
    r = classer(env)
    assert not r["lisible"] and r["L5"]["rejet"] and r["separation"]["issue"] == "séparation réelle (portée par R7)"
    assert r["verdict"].startswith("E2 v2 : classement exploratoire non lisible") and "non lue : classement non lisible" in r["verdict"]
    assert r["designees"] == []


def test_v3_2_1_pieces_et_version():
    assert O.VERSION == "outil-lecteur-conception-propre-v3-2-1" and K.VERSION == "classer-conception-propre-v3-2-1"
    assert O.PIECES["temoins_hasard"][0].endswith("temoins-hasard-v2-1.json")
    assert O.PIECES["regle"][0].endswith("regle-v2-1.md")
    assert O.MANIFESTE == "manifeste-relecture-v3-2.json" and O.SUFFIXE == "v3-2"
    assert O.DOSSIER_ENVOIS_REL.endswith("lecture-g1-v3-2/envois")
