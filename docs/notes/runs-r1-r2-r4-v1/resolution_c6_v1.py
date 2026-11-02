"""C-6 (concordance de conv-audit, n° 343) — résolution sur processeur des 7 épisodes de P3 restés non résolus par la
table de tokenisation v1 (`prereg/R1-table-tokenisation-v1.json`, 5309326b…), version 1.

Hypothèses 1 à 3 du rapport `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md` (377101ec…), ordre fixe, premier
succès retenu (rien d'autre n'est essayé ensuite pour cet épisode) ; **arbitre unique : égalité de l'empreinte de
trajectoire avec celle que P3 a stockée** (`episodes-p3.json`, champ `empreintes.trajectoire`). Aucun score, aucune
activation, aucune note de juge n'est lu : seuls `episode`, `pas`, `condition`, `tache`, `jetons`, `jetons_notes` de
`scores-p3.npz` (chargés clé par clé), les textes des actions et les empreintes des fiches.

Niveaux, dans l'ordre (« paire » = deux jetons ordinaires voisins des jetons notés d'une action redécoupés en deux jetons
ordinaires du vocabulaire couvrant les mêmes octets, coupe différente ; « fenêtre » = trois jetons voisins redécoupés
en trois, les deux frontières déplacées ; « fin » = jeton de fin de tour remplacé par une autre valeur de `fmt.fins`) :

  H1 trois redécoupages ou plus
    1a  trois paires disjointes, n'importe où (combinaisons dans l'ordre des candidats) ;
    1b  quatre paires disjointes dans une même action ;
    1c  copie : toutes les occurrences d'un même redécoupage (classe = même paire canonique, même paire nouvelle ;
        au moins 3 occurrences), puis toutes les occurrences (au moins 2) et une autre paire, puis toutes les
        occurrences (au moins 2) et deux autres paires ;
  H2 fenêtre de trois jetons redécoupée autrement
    2a  une fenêtre ; 2b  une fenêtre et une paire ; 2c  deux fenêtres disjointes ;
  H3 jeton de fin substitué combiné à un redécoupage
    3a  une fin et une paire ; 3b  une fin et une fenêtre ; 3c  une fin et deux paires ; 3d  deux fins et une paire.

Ordre des candidats : pas croissant, rang croissant dans l'action, coupe(s) croissante(s) en octets ; fins : pas
croissant, valeur croissante (hors la fin par défaut) ; combinaisons : `itertools.combinations`. Non explorés
(déclarés) : quatre paires ou plus dans des actions différentes hors copie, hypothèse 4 (octets incomplets), découpages
qui changent le nombre de jetons d'un mot en compensant ailleurs dans la même action.

Garde-fous (R5) : le sérialiseur rapide est comparé octet pour octet à `json.dumps` du harnais pour chaque épisode ;
cas sains : les 15 corrections de la table v1 redonnent l'empreinte de P3 par le chemin rapide et par le chemin lent ;
artefact : une correction fausse ne la redonne pas ; la base des 7 ne la redonne pas ; les 22 épisodes signalés et les
7 non résolus sont recalculés et comparés à la table v1. Toute correction trouvée est revérifiée par le chemin lent
(reconstruction, `episode_harnais`, `empreinte_trajectoire`), avec mêmes octets, même texte décodé, même longueur.
Sortie JSON déterministe (aucune date, aucune durée ; les durées vont sur la sortie d'erreur).

    python -I resolution_c6_v1.py --arbre ARBRE --tokeniseur TOK --table TABLE_V1 --sortie resultat-c6-v1.json [--processus 4]
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import sys
import time
from multiprocessing import Pool
from pathlib import Path

VERSION = "resolution_c6_v1"
CHEMINS = {
    "fiches": ("diag/20261019-230011-p3-reel/episodes-p3.json",
               "1a96cbf8ac6e10d3315bb20248453836d6ae5570b2312ded2be5ebb67cd14381"),
    "scores": ("donnees/20261019-230011-p3-reel/scores-p3.npz",
               "968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf"),
    "textes": ("donnees/20261019-230011-p3-reel/textes-actions-p3.jsonl",
               "ba05fa13af2dd4f935334438b44d2d27fbc655a970721b10b90bd94b5846f284"),
    "taches": ("donnees/t05-pilote-v1/taches-pilote-60-v1.json",
               "287e83485cba550098b80db809589398d8f2826c02dfa9cc2719a1063795d5aa"),
    "consignes": ("prereg/P3-consignes-v1.md", "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c"),
}
TABLE_V1_SHA = "5309326bc307d9849745a7b51f259661bf7bfb68b0508449d45903868e0cbd5c"
TOKENISEUR_SHA = {"tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"}
TOKENISEUR_GIT = {"tokenizer_config.json": "db88166e2bc4c799fd5d1ae643b75e84d03ee70e"}
TOKENISEUR_TAILLE = {"tokenizer_config.json": 55351}
VARIABLES_GABARIT = {"date_string": "26 Jul 2024"}
T = 10
NIVEAUX = ("1a", "1b", "1c", "2a", "2b", "2c", "3a", "3b", "3c", "3d")
HYPOTHESE = {n: "H" + n[0] for n in NIVEAUX}


class Arret(Exception):
    pass


def sha_fichier(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git_blob(p) -> str:
    b = Path(p).read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


# ---------------------------------------------------------------------------------------------------------------------
# Sérialisation rapide (même octets que json.dumps(asdict(Episode), sort_keys=True, ensure_ascii=False))

def serialiser(identifiant: str, rec: dict):
    """(octets, positions des identifiants dans la partie « actions », positions dans la transcription)."""
    morceaux: list[bytes] = []
    n = [0]

    def ec(s):
        b = s.encode("utf-8") if isinstance(s, str) else s
        morceaux.append(b)
        n[0] += len(b)

    def liste(ids):
        pos = []
        ec("[")
        for i, x in enumerate(ids):
            if i:
                ec(", ")
            d = str(int(x))
            pos.append((n[0], n[0] + len(d)))
            ec(d)
        ec("]")
        return pos

    ec('{"N": 1, "T": %d, "identifiant": ' % T + json.dumps(identifiant, ensure_ascii=False)
       + ', "transcriptions": [{"actions": [')
    pos_a = []
    for t, a in enumerate(rec["actions"]):
        if t:
            ec(", ")
        ec('{"agent": 0, "debut": %d, "fin": %d, "ids": ' % (a["debut"], a["debut"] + len(a["nv"])))
        pos_a.append(liste(a["nv"]))
        ec(', "pas": %d, "texte": ' % a["pas"] + json.dumps(a["texte"], ensure_ascii=False) + "}")
    ec('], "agent": 0, "ids": ')
    pos_t = liste(rec["ids"])
    ec("}]}")
    return b"".join(morceaux), pos_a, pos_t


class HacheurRapide:
    """Empreinte d'une variante : remplacements de largeur constante (t, k, nouveaux identifiants)."""

    def __init__(self, identifiant: str, rec: dict):
        self.octets, self.pos_a, self.pos_t = serialiser(identifiant, rec)
        self.mv = memoryview(self.octets)
        self.debuts = [a["debut"] for a in rec["actions"]]

    def plages(self, mods):
        sortie = []
        for t, k, nouv in mods:
            w = len(nouv)
            b = ", ".join(str(int(x)) for x in nouv).encode("ascii")
            pa = self.pos_a[t]
            sortie.append((pa[k][0], pa[k + w - 1][1], b))
            p = self.debuts[t] + k
            sortie.append((self.pos_t[p][0], self.pos_t[p + w - 1][1], b))
        sortie.sort()
        return sortie

    def empreinte(self, mods=()) -> str:
        h = hashlib.sha256()
        prec = 0
        for s, e, b in self.plages(mods):
            h.update(self.mv[prec:s])
            h.update(b)
            prec = e
        h.update(self.mv[prec:])
        return h.hexdigest()


# ---------------------------------------------------------------------------------------------------------------------
# Vocabulaire au niveau de l'octet

def _octets_vers_unicode() -> dict[int, str]:
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    m = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + m)
            m += 1
    return dict(zip(bs, map(chr, cs)))


U2B = {c: b for b, c in _octets_vers_unicode().items()}


def table_des_octets(tok):
    speciaux = {int(i) for i in (tok.all_special_ids or [])} | {int(i) for i in (tok.added_tokens_decoder or {})}

    def conv(s):
        if not all(c in U2B for c in s):
            return None
        return bytes(U2B[c] for c in s)

    par_octets: dict[bytes, int] = {}
    octets_de: dict[int, bytes | None] = {}
    for s, i in tok.get_vocab().items():
        i = int(i)
        if i in speciaux:
            octets_de[i] = None
            continue
        b = conv(s)
        octets_de[i] = b
        if b is not None:
            if b in par_octets:
                raise Arret(f"deux jetons ordinaires pour les mêmes octets {b!r}")
            par_octets[b] = i
    return octets_de, par_octets, speciaux


def notes_de(rec, a_fins, t):
    nv = rec["actions"][t]["nv"]
    return [int(x) for x in nv[:len(nv) - a_fins[t]]]


def candidats_paires(rec, a_fins, octets_de, par_octets):
    sortie = []
    for t in range(T):
        notes = notes_de(rec, a_fins, t)
        for k in range(len(notes) - 1):
            ox, oy = octets_de.get(notes[k]), octets_de.get(notes[k + 1])
            if ox is None or oy is None:
                continue
            b = ox + oy
            for c in range(1, len(b)):
                if c == len(ox):
                    continue
                g, d = par_octets.get(b[:c]), par_octets.get(b[c:])
                if g is not None and d is not None:
                    sortie.append((t, k, (g, d)))
    return sortie


def candidats_fenetres(rec, a_fins, octets_de, par_octets):
    sortie = []
    for t in range(T):
        notes = notes_de(rec, a_fins, t)
        for k in range(len(notes) - 2):
            o = [octets_de.get(x) for x in notes[k:k + 3]]
            if any(x is None for x in o):
                continue
            b, f1, f2 = o[0] + o[1] + o[2], len(o[0]), len(o[0]) + len(o[1])
            for c1 in range(1, len(b) - 1):
                if c1 == f1:
                    continue
                g = par_octets.get(b[:c1])
                if g is None:
                    continue
                for c2 in range(c1 + 1, len(b)):
                    if c2 == f2:
                        continue
                    m, d = par_octets.get(b[c1:c2]), par_octets.get(b[c2:])
                    if m is not None and d is not None:
                        sortie.append((t, k, (g, m, d)))
    return sortie


def disjoints(mods) -> bool:
    pl = sorted((t, k, k + len(n)) for t, k, n in mods)
    return all(not (a[0] == b[0] and b[1] < a[2]) for a, b in zip(pl, pl[1:]))


# ---------------------------------------------------------------------------------------------------------------------
# Recherche (processus fils : données pures, aucun tokeniseur)

def generateurs(paquet):
    """Niveaux dans l'ordre fixe : (niveau, base, itérable de listes de modifications)."""
    cp, cf, classes = paquet["paires"], paquet["fenetres"], paquet["classes"]
    fins1, fins2 = paquet["fins1"], paquet["fins2"]

    def g1a():
        for p in itertools.combinations(cp, 3):
            if disjoints(p):
                yield p

    def g1b():
        for t in range(T):
            ct = [c for c in cp if c[0] == t]
            for p in itertools.combinations(ct, 4):
                if disjoints(p):
                    yield p

    def g1c():
        rep = [v for v in classes if len(v) >= 2 and disjoints(v)]
        for v in rep:
            if len(v) >= 3:
                yield v
        for v in rep:
            for c in cp:
                if c not in v and disjoints(v + [c]):
                    yield v + [c]
        for v in rep:
            autres = [c for c in cp if c not in v]
            for p in itertools.combinations(autres, 2):
                if disjoints(v + list(p)):
                    yield v + list(p)

    def g2a():
        for f in cf:
            yield [f]

    def g2b():
        for f in cf:
            for c in cp:
                if disjoints([f, c]):
                    yield [f, c]

    def g2c():
        for p in itertools.combinations(cf, 2):
            if disjoints(p):
                yield p

    def gpaires():
        for c in cp:
            yield [c]

    def gfen():
        for f in cf:
            yield [f]

    def gdeux():
        for p in itertools.combinations(cp, 2):
            if disjoints(p):
                yield p

    yield "1a", None, g1a()
    yield "1b", None, g1b()
    yield "1c", None, g1c()
    yield "2a", None, g2a()
    yield "2b", None, g2b()
    yield "2c", None, g2c()
    for niveau, bases, gen in (("3a", fins1, gpaires), ("3b", fins1, gfen), ("3c", fins1, gdeux), ("3d", fins2, gpaires)):
        for fins, rec in bases:
            yield niveau, (fins, rec), gen()


def chercher(paquet):
    t0 = time.perf_counter()
    cible = paquet["trajectoire_p3"]
    e = paquet["episode"]
    h0 = HacheurRapide(e, paquet["rec"])
    if h0.empreinte() == cible:
        raise Arret(f"{e} : la base redonne déjà l'empreinte de P3")
    essais = {n: 0 for n in NIVEAUX}
    cache = {}
    for niveau, base, it in generateurs(paquet):
        if base is None:
            h, fins = h0, {}
        else:
            fins, rec = base
            cle = json.dumps(fins, sort_keys=True)
            if cle not in cache:
                cache.clear()
                cache[cle] = HacheurRapide(e, rec)
            h = cache[cle]
        for mods in it:
            essais[niveau] += 1
            if h.empreinte(mods) == cible:
                print(f"{e} : résolu au niveau {niveau} ({round(time.perf_counter() - t0, 1)} s)", file=sys.stderr,
                      flush=True)
                return {"episode": e, "niveau": niveau, "fins": fins, "mods": [list(m[:2]) + [list(m[2])] for m in mods],
                        "essais": essais}
        print(f"{e} : niveau {niveau} épuisé ({essais[niveau]} essais, {round(time.perf_counter() - t0, 1)} s)",
              file=sys.stderr, flush=True)
    return {"episode": e, "niveau": None, "fins": {}, "mods": [], "essais": essais}


# ---------------------------------------------------------------------------------------------------------------------

def appliquer(rec, mods, tok, octets_de, speciaux, a_fins, textes):
    """Chemin lent : copie de la reconstruction, remplacements posés dans `nv` et `ids`, gardes, rend la copie."""
    r = copy.deepcopy(rec)
    for t, k, nouv in sorted((int(m[0]), int(m[1]), [int(x) for x in m[2]]) for m in mods):
        a = r["actions"][t]
        w = len(nouv)
        can = [int(x) for x in a["nv"][k:k + w]]
        n_notes = len(a["nv"]) - a_fins[t]
        if k + w > n_notes or any(x in speciaux for x in nouv + can) or nouv == can:
            raise Arret(f"remplacement invalide au pas {t}, rang {k}")
        if b"".join(octets_de[x] for x in can) != b"".join(octets_de[x] for x in nouv):
            raise Arret(f"octets différents au pas {t}, rang {k}")
        p = a["debut"] + k
        if [int(x) for x in r["ids"][p:p + w]] != can:
            raise Arret(f"transcription incohérente au pas {t}, rang {k}")
        a["nv"] = list(a["nv"])
        a["nv"][k:k + w] = nouv
        r["ids"] = list(r["ids"])
        r["ids"][p:p + w] = nouv
    for t, a in enumerate(r["actions"]):
        if tok.decode(a["nv"], skip_special_tokens=True) != textes[t] or len(a["nv"]) != len(rec["actions"][t]["nv"]):
            raise Arret(f"action corrigée non conforme au pas {t}")
    return r


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--arbre", required=True)
    ap.add_argument("--tokeniseur", required=True)
    ap.add_argument("--table", required=True)
    ap.add_argument("--sortie", required=True)
    ap.add_argument("--processus", type=int, default=4)
    a = ap.parse_args(argv)
    sortie = Path(a.sortie)
    if sortie.exists():
        raise Arret(f"{sortie} existe déjà (R12)")
    arbre = Path(a.arbre).resolve()
    sys.path.insert(0, str(arbre / "src"))
    import numpy as np
    import tokenizers
    import transformers
    from transformers import AutoTokenizer

    from controle_ia.environnements.invites import charger_invite
    from controle_ia.environnements.pilote_a import charger_taches, tache_de
    from controle_ia.harnais.formats import FormatChat
    from controle_ia.premier_test_ia.conditions import charger_consignes, environnement
    from controle_ia.runs_nuit import rejeu_activations_v1 as v1

    t00 = time.perf_counter()
    # pièces : empreintes
    for nom, (rel, sha) in CHEMINS.items():
        if sha_fichier(arbre / rel) != sha:
            raise Arret(f"{rel} : empreinte ≠ {sha[:12]}")
    if sha_fichier(a.table) != TABLE_V1_SHA:
        raise Arret("table v1 : empreinte ≠ 5309326b")
    tokd = Path(a.tokeniseur)
    for n, s in TOKENISEUR_SHA.items():
        if sha_fichier(tokd / n) != s:
            raise Arret(f"tokeniseur {n} : sha256 ≠ {s[:12]}")
    for n, s in TOKENISEUR_GIT.items():
        if git_blob(tokd / n) != s or (tokd / n).stat().st_size != TOKENISEUR_TAILLE[n]:
            raise Arret(f"tokeniseur {n} : identifiant git ou taille ≠ publié")
    tok = AutoTokenizer.from_pretrained(str(tokd))
    fmt = FormatChat(tok, variables=VARIABLES_GABARIT)
    fmt.fins = {128001, 128008, 128009, int(tok.eos_token_id)} | {fmt._pieces(("x", "y"))["cloture"][0]}
    # identité : clés lues une à une (aucun score, aucun nom de sonde)
    with np.load(arbre / CHEMINS["scores"][0], allow_pickle=False) as z:
        ident = {k: z[k] for k in ("episode", "pas", "condition", "tache", "jetons", "jetons_notes")}
    lignes = [json.loads(x) for x in (arbre / CHEMINS["textes"][0]).read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(lignes) != len(ident["episode"]):
        raise Arret("textes et identité de longueurs différentes")
    for i, x in enumerate(lignes):
        for k in ("episode", "pas", "condition", "tache"):
            v = int(ident[k][i]) if k == "pas" else str(ident[k][i])
            if x[k] != v:
                raise Arret(f"ligne {i} : {k} désaligné")
    fiches = {f["episode"]: f["empreintes"]["trajectoire"]
              for f in json.loads((arbre / CHEMINS["fiches"][0]).read_text(encoding="utf-8"))["resultat"]["fiches"]}
    taches = {t["identifiant"]: t for t in charger_taches(arbre / CHEMINS["taches"][0])}
    consignes = charger_consignes(arbre / CHEMINS["consignes"][0], CHEMINS["consignes"][1])
    guide = charger_invite("H1-classification")
    table = json.loads(Path(a.table).read_text(encoding="utf-8"))
    jet = [int(x) for x in ident["jetons"]]
    jn = [int(x) for x in ident["jetons_notes"]]
    par_ep: dict[str, list[int]] = {}
    for i, x in enumerate(lignes):
        par_ep.setdefault(x["episode"], []).append(i)
    octets_de, par_octets, speciaux = table_des_octets(tok)

    # signalement (même règle que la garde) et comparaison à la table v1
    donnees, signales, ident_base, conf_long = {}, [], 0, 0
    for e, rs in par_ep.items():
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        L, J, JN = [lignes[r] for r in rs], [jet[r] for r in rs], [jn[r] for r in rs]
        rec = v1.reconstruire_episode(fmt, env, T, L, J, JN)
        conf = all(x["conforme"] for x in rec["actions"])
        same = v1.empreinte_trajectoire(v1.episode_harnais(e, T, rec)) == fiches[e]
        conf_long += conf
        ident_base += same
        if conf and not same:
            signales.append(e)
            donnees[e] = (env, L, J, JN, rec)
    par_table = {x["episode"]: x for x in table["episodes"]}
    if signales != [x["episode"] for x in table["episodes"]]:
        raise Arret("épisodes signalés ≠ table v1")
    sept = [e for e in signales if par_table[e]["methode"] == "non_resolu"]
    if len(sept) != 7:
        raise Arret(f"{len(sept)} non résolus dans la table v1, 7 attendus")
    print(f"{len(par_ep)} épisodes, {conf_long} conformes en longueur, {ident_base} identiques, {len(signales)} signalés,"
          f" {len(sept)} non résolus ({round(time.perf_counter() - t00, 1)} s)", file=sys.stderr, flush=True)

    # gardes du sérialiseur rapide et cas sains / artefact
    gardes = {"serialiseur_egal_json_dumps": 0, "table_v1_corrections_redonnees_rapide": 0,
              "table_v1_corrections_redonnees_lent": 0, "artefact_refuse": 0, "base_des_7_differente": 0}
    for e in signales:
        env, L, J, JN, rec = donnees[e]
        ref = json.dumps(v1.episode_harnais(e, T, rec).en_dict(), sort_keys=True, ensure_ascii=False).encode("utf-8")
        if serialiser(e, rec)[0] != ref:
            raise Arret(f"{e} : sérialiseur rapide ≠ json.dumps")
        gardes["serialiseur_egal_json_dumps"] += 1
        ent = par_table[e]
        if ent["methode"] in ("une_paire", "deux_paires"):
            a_fins = [J[t] - JN[t] for t in range(T)]
            mods = [(p["pas"], p["rang"], tuple(p["p3"])) for p in ent["paires"]]
            for p in ent["paires"]:
                if notes_de(rec, a_fins, p["pas"])[p["rang"]:p["rang"] + 2] != p["canonique"]:
                    raise Arret(f"{e} : paire canonique de la table absente")
            h = HacheurRapide(e, rec)
            if h.empreinte(mods) != fiches[e]:
                raise Arret(f"{e} : correction de la table v1 non redonnée (chemin rapide)")
            gardes["table_v1_corrections_redonnees_rapide"] += 1
            r2 = appliquer(rec, mods, tok, octets_de, speciaux, a_fins, [x["texte"] for x in L])
            if v1.empreinte_trajectoire(v1.episode_harnais(e, T, r2)) != fiches[e]:
                raise Arret(f"{e} : correction de la table v1 non redonnée (chemin lent)")
            gardes["table_v1_corrections_redonnees_lent"] += 1
            faux = next(c for c in candidats_paires(rec, a_fins, octets_de, par_octets) if [c] != mods[:1] or len(mods) > 1)
            if h.empreinte([faux]) == fiches[e]:
                raise Arret(f"{e} : artefact accepté")
            gardes["artefact_refuse"] += 1
        elif ent["methode"] == "fins":
            fins = {int(t): int(v) for t, v in ent["fins"].items()}
            r2 = v1.reconstruire_episode(fmt, env, T, L, J, JN, fins)
            if HacheurRapide(e, r2).empreinte() != fiches[e]:
                raise Arret(f"{e} : correction de fin de la table v1 non redonnée")
            gardes["table_v1_corrections_redonnees_rapide"] += 1
            if v1.empreinte_trajectoire(v1.episode_harnais(e, T, r2)) != fiches[e]:
                raise Arret(f"{e} : correction de fin de la table v1 non redonnée (chemin lent)")
            gardes["table_v1_corrections_redonnees_lent"] += 1
    for e in sept:
        if HacheurRapide(e, donnees[e][4]).empreinte() == fiches[e]:
            raise Arret(f"{e} : la base redonne l'empreinte")
        gardes["base_des_7_differente"] += 1

    # paquets des 7
    paquets = []
    for e in sept:
        env, L, J, JN, rec = donnees[e]
        a_fins = [J[t] - JN[t] for t in range(T)]
        cp = candidats_paires(rec, a_fins, octets_de, par_octets)
        cf = candidats_fenetres(rec, a_fins, octets_de, par_octets)
        classes: dict = {}
        for c in cp:
            cle = (tuple(notes_de(rec, a_fins, c[0])[c[1]:c[1] + 2]), c[2])
            classes.setdefault(cle, []).append(c)
        pas_fin = [t for t in range(T) if a_fins[t] == 1]
        defaut = {t: int(rec["actions"][t]["nv"][-1]) for t in pas_fin}
        valeurs = sorted(int(x) for x in fmt.fins)
        fins1 = [({str(t): v}, v1.reconstruire_episode(fmt, env, T, L, J, JN, {t: v}))
                 for t in pas_fin for v in valeurs if v != defaut[t]]
        fins2 = []
        for t1, t2 in itertools.combinations(pas_fin, 2):
            for v1_, v2_ in itertools.product([v for v in valeurs if v != defaut[t1]], [v for v in valeurs if v != defaut[t2]]):
                fins2.append(({str(t1): v1_, str(t2): v2_},
                              v1.reconstruire_episode(fmt, env, T, L, J, JN, {t1: v1_, t2: v2_})))
        for fins, r in fins1 + fins2:
            for t in range(T):
                if [int(x) for x in r["actions"][t]["nv"][:len(r["actions"][t]["nv"]) - a_fins[t]]] != notes_de(rec, a_fins, t):
                    raise Arret(f"{e} : substitution de fin qui change les jetons notés")
        paquets.append({"episode": e, "trajectoire_p3": fiches[e], "rec": rec, "paires": cp, "fenetres": cf,
                        "classes": list(classes.values()), "fins1": fins1, "fins2": fins2,
                        "comptes": {"paires": len(cp), "fenetres": len(cf), "classes_repetees":
                                    sum(1 for v in classes.values() if len(v) >= 2), "fins1": len(fins1),
                                    "fins2": len(fins2)}})
    print(f"paquets prêts ({round(time.perf_counter() - t00, 1)} s) : "
          + "; ".join(f"{p['episode']} {p['comptes']}" for p in paquets), file=sys.stderr, flush=True)

    with Pool(processes=a.processus) as pool:
        res = pool.map(chercher, paquets, chunksize=1)

    # vérification par le chemin lent et écriture
    episodes = []
    for p, r in zip(paquets, res):
        e = p["episode"]
        env, L, J, JN, rec = donnees[e]
        a_fins = [J[t] - JN[t] for t in range(T)]
        ent = {"episode": e, "trajectoire_p3": p["trajectoire_p3"], "comptes_candidats": p["comptes"],
               "essais": r["essais"]}
        if r["niveau"] is None:
            ent.update({"resolu": False, "hypothese": None, "niveau": None, "empreinte_retrouvee": None})
        else:
            fins = {int(t): int(v) for t, v in r["fins"].items()}
            base = v1.reconstruire_episode(fmt, env, T, L, J, JN, fins or None)
            r2 = appliquer(base, r["mods"], tok, octets_de, speciaux, a_fins, [x["texte"] for x in L])
            emp = v1.empreinte_trajectoire(v1.episode_harnais(e, T, r2))
            if emp != p["trajectoire_p3"]:
                raise Arret(f"{e} : correction trouvée non redonnée par le chemin lent")
            ent.update({
                "resolu": True, "hypothese": HYPOTHESE[r["niveau"]], "niveau": r["niveau"],
                "empreinte_retrouvee": emp, "fins": {str(t): v for t, v in sorted(fins.items())},
                "remplacements": [{"pas": m[0], "rang": m[1],
                                   "canonique": [int(x) for x in base["actions"][m[0]]["nv"][m[1]:m[1] + len(m[2])]],
                                   "p3": m[2],
                                   "canonique_jetons": tok.convert_ids_to_tokens(
                                       [int(x) for x in base["actions"][m[0]]["nv"][m[1]:m[1] + len(m[2])]]),
                                   "p3_jetons": tok.convert_ids_to_tokens(m[2])} for m in sorted(r["mods"])]})
        episodes.append(ent)
    out = {
        "version": VERSION,
        "regle": "ordre fixe H1 (1a trois paires, 1b quatre paires dans une action, 1c copie) puis H2 (2a fenêtre de "
                 "trois, 2b fenêtre et paire, 2c deux fenêtres) puis H3 (3a fin et paire, 3b fin et fenêtre, 3c fin et "
                 "deux paires, 3d deux fins et paire) ; premier succès retenu ; arbitre unique : empreinte de "
                 "trajectoire de P3 ; non explorés : quatre paires ou plus dans des actions différentes hors copie, "
                 "hypothèse 4, découpages qui changent le nombre de jetons d'un mot",
        "run_source": "20261019-230011-p3-reel",
        "pieces_sha256": {n: s for n, (_, s) in CHEMINS.items()}, "table_v1_sha256": TABLE_V1_SHA,
        "tokeniseur": {"modele": "meta-llama/Llama-3.1-8B-Instruct", "revision": "0e9e39f249a16976918f6564b8830bc894c89659",
                       "sha256": {n: sha_fichier(tokd / n) for n in ("tokenizer.json", "tokenizer_config.json",
                                                                       "special_tokens_map.json")},
                       "git_blob": {n: git_blob(tokd / n) for n in ("tokenizer.json", "tokenizer_config.json",
                                                                      "special_tokens_map.json")}},
        "versions": {"transformers": transformers.__version__, "tokenizers": tokenizers.__version__,
                     "numpy": np.__version__, "python": sys.version.split()[0]},
        "fins_du_format": sorted(int(x) for x in fmt.fins),
        "comptes_globaux": {"episodes": len(par_ep), "conformes_longueur": conf_long, "identiques_base": ident_base,
                            "signales": len(signales), "non_resolus_table_v1": len(sept),
                            "resolus_c6": sum(1 for x in episodes if x["resolu"]),
                            "non_resolus_c6": sum(1 for x in episodes if not x["resolu"]),
                            "identiques_apres_table_v1_et_c6": ident_base + 15 + sum(1 for x in episodes if x["resolu"])},
        "gardes": gardes,
        "episodes": episodes,
    }
    sortie.write_text(json.dumps(out, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"comptes": out["comptes_globaux"], "duree_s": round(time.perf_counter() - t00, 1),
                      "sha256": sha_fichier(sortie)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except Arret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
