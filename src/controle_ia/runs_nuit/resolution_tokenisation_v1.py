"""Résolution de la tokenisation des actions de P3 par l'empreinte de trajectoire (addendum de relance de R1, étape A).

Cause (rapport `docs/notes/runs-r1-r2-r4-v1/enquete-arret-r1-v1.md`) : à température 1, l'agent de P3 a parfois
échantillonné un découpage non canonique d'un mot, de même longueur en jetons et qui se décode en le même texte
(`Ġro` + `crap` au lieu de `Ġroc` + `rap`). Le texte stocké ne le dit pas ; l'empreinte de trajectoire stockée par P3,
qui couvre les identifiants, le voit. Ce module retrouve, **sans choix libre**, les identifiants de P3 : seule une
égalité d'empreinte avec celle de P3 valide une variante.

Ordre fixe (premier succès retenu, rien d'autre n'est essayé ensuite) :
1. **fins** — substitutions du jeton de fin de tour (une, puis deux), exactement `rejeu_activations_v1.resoudre_fins` ;
2. **une paire** — sur la reconstruction de base (jetons de fin par défaut), une paire de jetons voisins des jetons notés
   d'une action redécoupée en deux jetons ordinaires du vocabulaire couvrant les mêmes octets ;
3. **deux paires** — deux redécoupages de ce type à la fois (paires disjointes), sur la même base.
Ordre des candidats : pas croissant, rang croissant dans l'action, point de coupe croissant (en octets) ; ordre des
couples : `itertools.combinations` sur cette liste. Un épisode qu'aucune étape ne résout est « non résolu » (règle B).

La table des corrections est calculée sur processeur avant la carte (`calculer_table`, ligne de commande ci-dessous),
écrite en JSON déterministe, puis scellée et citée par la configuration de la relance ; l'instance l'applique
(`appliquer_entree`) et vérifie, pour chaque épisode corrigé, que l'empreinte de P3 est redonnée exactement.

    PYTHONPATH=src python -m controle_ia.runs_nuit.resolution_tokenisation_v1 --tokeniseur DOSSIER \\
        --config prereg/R1-rejeu-config-v2.json --sortie prereg/R1-table-tokenisation-v1.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

from ..gardes import GardeArret
from .rejeu_activations_v1 import episode_harnais, empreinte_trajectoire, reconstruire_episode

VERSION_TABLE = 1
METHODES = ("fins", "une_paire", "deux_paires", "non_resolu")
REGLE = ("ordre fixe, premier succès retenu : (1) substitutions du jeton de fin (une, puis deux ; "
         "rejeu_activations_v1.resoudre_fins) ; (2) une paire de jetons voisins redécoupée (mêmes octets, même longueur) ; "
         "(3) deux paires disjointes ; candidats par pas, rang, coupe croissants ; arbitre unique : égalité de "
         "l'empreinte de trajectoire avec celle de P3")


def _octets_vers_unicode() -> dict[int, str]:
    """Correspondance octet → caractère des tokeniseurs BPE au niveau de l'octet (GPT-2, Llama 3)."""
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return dict(zip(bs, map(chr, cs)))


U2B = {c: b for b, c in _octets_vers_unicode().items()}


def ids_speciaux(tok) -> set[int]:
    s = {int(i) for i in getattr(tok, "all_special_ids", []) or []}
    s |= {int(i) for i in (getattr(tok, "added_tokens_decoder", None) or {})}
    return s


def est_niveau_octet(tok) -> bool:
    """Vrai si l'espace se code « Ġ » (BPE au niveau de l'octet)."""
    ids = list(tok(" a", add_special_tokens=False)["input_ids"])
    return any("Ġ" in str(tok.convert_ids_to_tokens(int(i))) for i in ids)


def table_des_octets(tok, niveau_octet: bool | None = None):
    """(octets(i) → bytes ou None pour un jeton spécial, {octets: identifiant} des jetons ordinaires)."""
    speciaux = ids_speciaux(tok)
    niveau = est_niveau_octet(tok) if niveau_octet is None else niveau_octet

    def conv(s: str) -> bytes | None:
        if niveau:
            if not all(c in U2B for c in s):
                return None
            return bytes(U2B[c] for c in s)
        return s.encode("utf-8")

    par_octets: dict[bytes, int] = {}
    for s, i in tok.get_vocab().items():
        if int(i) in speciaux:
            continue
        b = conv(s)
        if b is not None and b not in par_octets:
            par_octets[b] = int(i)
    cache: dict[int, bytes | None] = {}

    def octets(i: int) -> bytes | None:
        i = int(i)
        if i not in cache:
            cache[i] = None if i in speciaux else conv(str(tok.convert_ids_to_tokens(i)))
        return cache[i]

    return octets, par_octets


def candidats_paires(rec: dict, a_fins: list[int], octets, par_octets) -> list[tuple[int, int, int, int]]:
    """Redécoupages possibles d'une paire de jetons voisins des jetons notés, dans l'ordre fixe : (pas, rang, g, d)."""
    sortie = []
    for t, a in enumerate(rec["actions"]):
        notes = a["nv"][:len(a["nv"]) - a_fins[t]]
        for k in range(len(notes) - 1):
            x, y = int(notes[k]), int(notes[k + 1])
            ox, oy = octets(x), octets(y)
            if ox is None or oy is None:
                continue
            b = ox + oy
            for c in range(1, len(b)):
                if c == len(ox):
                    continue
                g, d = par_octets.get(b[:c]), par_octets.get(b[c:])
                if g is not None and d is not None:
                    sortie.append((t, k, int(g), int(d)))
    return sortie


class Hacheur:
    """Empreinte de trajectoire d'une variante (paires redécoupées), sans recopier l'épisode : on modifie le
    dictionnaire du harnais en place, on hache, on rétablit. Même sérialisation que `empreinte_trajectoire`."""

    def __init__(self, identifiant: str, T: int, rec: dict):
        self.d = episode_harnais(identifiant, T, rec).en_dict()
        self.debuts = [a["debut"] for a in rec["actions"]]

    def _poser(self, t: int, k: int, deux: list[int]):
        tr = self.d["transcriptions"][0]
        p = self.debuts[t] + k
        ancien = (tr["ids"][p:p + 2], tr["actions"][t]["ids"][k:k + 2])
        tr["ids"][p:p + 2] = deux
        tr["actions"][t]["ids"][k:k + 2] = deux
        return ancien

    def _retablir(self, t: int, k: int, ancien):
        tr = self.d["transcriptions"][0]
        p = self.debuts[t] + k
        tr["ids"][p:p + 2] = ancien[0]
        tr["actions"][t]["ids"][k:k + 2] = ancien[1]

    def empreinte(self, modifs: list[tuple[int, int, int, int]] = ()) -> str:
        anciens = [self._poser(t, k, [g, d]) for t, k, g, d in modifs]
        try:
            return hashlib.sha256(json.dumps(self.d, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
        finally:
            for (t, k, _, _), a in reversed(list(zip(modifs, anciens))):
                self._retablir(t, k, a)


def _resoudre_fins(fmt, env, T, lignes, jetons, jetons_notes, empreinte, identifiant):
    """Même ordre que `rejeu_activations_v1.resoudre_fins`, mais rend aussi les substitutions retenues."""
    pas = [t for t in range(T) if jetons[t] - jetons_notes[t] == 1]
    autres = sorted(int(x) for x in fmt.fins)
    essais = 0
    for k in (1, 2):
        for choix in itertools.combinations(pas, k):
            for valeurs in itertools.product(autres, repeat=k):
                essais += 1
                fins = dict(zip(choix, valeurs))
                rec = reconstruire_episode(fmt, env, T, lignes, jetons, jetons_notes, fins)
                if empreinte_trajectoire(episode_harnais(identifiant, T, rec)) == empreinte:
                    return {str(t): int(v) for t, v in sorted(fins.items())}, essais
    return None, essais


def resoudre_episode(fmt, env, T, lignes, jetons, jetons_notes, empreinte: str, identifiant: str, octets,
                     par_octets) -> dict:
    """Entrée de table pour un épisode conforme en longueur à trajectoire différente (ordre fixe, voir le module)."""
    fins, essais_fins = _resoudre_fins(fmt, env, T, lignes, jetons, jetons_notes, empreinte, identifiant)
    base = {"episode": identifiant, "trajectoire_p3": empreinte, "fins": {}, "paires": []}
    if fins is not None:
        return {**base, "methode": "fins", "fins": fins, "essais": {"fins": essais_fins}}
    rec = reconstruire_episode(fmt, env, T, lignes, jetons, jetons_notes)
    a_fins = [jetons[t] - jetons_notes[t] for t in range(T)]
    cands = candidats_paires(rec, a_fins, octets, par_octets)
    h = Hacheur(identifiant, T, rec)
    if h.empreinte() == empreinte:
        raise GardeArret(f"{identifiant} : la base redonne déjà l'empreinte de P3 (épisode mal signalé)")

    def paire(c):
        t, k, g, d = c
        a = rec["actions"][t]["nv"]
        return {"pas": t, "rang": k, "canonique": [int(a[k]), int(a[k + 1])], "p3": [g, d]}

    for n1, c in enumerate(cands):
        if h.empreinte([c]) == empreinte:
            return {**base, "methode": "une_paire", "paires": [paire(c)],
                    "essais": {"fins": essais_fins, "une_paire": n1 + 1, "candidats": len(cands)}}
    n2 = 0
    for c1, c2 in itertools.combinations(cands, 2):
        if c1[0] == c2[0] and abs(c1[1] - c2[1]) < 2:
            continue
        n2 += 1
        if h.empreinte([c1, c2]) == empreinte:
            return {**base, "methode": "deux_paires", "paires": [paire(c1), paire(c2)],
                    "essais": {"fins": essais_fins, "une_paire": len(cands), "deux_paires": n2, "candidats": len(cands)}}
    return {**base, "methode": "non_resolu",
            "essais": {"fins": essais_fins, "une_paire": len(cands), "deux_paires": n2, "candidats": len(cands)}}


def appliquer_entree(fmt, env, T, lignes, jetons, jetons_notes, entree: dict, octets=None) -> dict:
    """Reconstruction corrigée d'un épisode selon son entrée de table (fins puis paires), avec gardes : jeton de fin
    parmi `fmt.fins` ; paire canonique à sa place ; mêmes octets ; jetons ordinaires ; même texte au décodage ; même
    longueur. Les bornes des champs sont recalculées sur les identifiants corrigés. N'arbitre pas : l'appelant compare
    l'empreinte à celle de P3."""
    from ..premier_test_ia.conditions import bornes_champs

    if entree.get("methode") not in ("fins", "une_paire", "deux_paires"):
        raise GardeArret(f"entrée de table sans correction applicable : {entree.get('methode')!r}")
    fins = {}
    for t, v in (entree.get("fins") or {}).items():
        t, v = int(t), int(v)
        if v not in {int(x) for x in fmt.fins}:
            raise GardeArret(f"{entree['episode']} : jeton de fin {v} hors de fmt.fins")
        if not (0 <= t < T) or jetons[t] - jetons_notes[t] != 1:
            raise GardeArret(f"{entree['episode']} : substitution de fin au pas {t} sans jeton de fin compté par P3")
        fins[t] = v
    rec = reconstruire_episode(fmt, env, T, lignes, jetons, jetons_notes, fins or None)
    speciaux = ids_speciaux(fmt.tok)
    if entree.get("paires") and octets is None:
        octets, _ = table_des_octets(fmt.tok)
    vues = set()
    for p in entree.get("paires") or []:
        t, k = int(p["pas"]), int(p["rang"])
        can, nouv = [int(x) for x in p["canonique"]], [int(x) for x in p["p3"]]
        if not (0 <= t < T):
            raise GardeArret(f"{entree['episode']} : pas {t} hors de l'épisode")
        a = rec["actions"][t]
        n_notes = len(a["nv"]) - (jetons[t] - jetons_notes[t])
        if not (0 <= k and k + 2 <= n_notes) or [int(x) for x in a["nv"][k:k + 2]] != can:
            raise GardeArret(f"{entree['episode']} : paire canonique {can} absente au pas {t}, rang {k}")
        if (t, k) in vues or (t, k - 1) in vues or (t, k + 1) in vues:
            raise GardeArret(f"{entree['episode']} : paires qui se chevauchent au pas {t}")
        vues.add((t, k))
        if nouv == can or any(x in speciaux for x in nouv):
            raise GardeArret(f"{entree['episode']} : redécoupage {nouv} identique ou spécial")
        oc = [octets(x) for x in can + nouv]
        if any(o is None for o in oc) or oc[0] + oc[1] != oc[2] + oc[3]:
            raise GardeArret(f"{entree['episode']} : redécoupage {nouv} ne couvre pas les mêmes octets que {can}")
        a["nv"] = list(a["nv"])
        a["nv"][k:k + 2] = nouv
        pos = a["debut"] + k
        if [int(x) for x in rec["ids"][pos:pos + 2]] != can:
            raise GardeArret(f"{entree['episode']} : transcription incohérente au pas {t}, rang {k}")
        rec["ids"] = list(rec["ids"])
        rec["ids"][pos:pos + 2] = nouv
    for t, a in enumerate(rec["actions"]):
        notes = a["nv"][:len(a["nv"]) - (jetons[t] - jetons_notes[t])]
        if len(notes) != jetons_notes[t] or len(a["nv"]) != jetons[t] \
                or fmt.tok.decode(a["nv"], skip_special_tokens=True) != a["texte"]:
            raise GardeArret(f"{entree['episode']} : action corrigée non conforme au pas {t} (longueur ou texte)")
        if entree.get("paires"):
            a["bornes"] = bornes_champs(fmt.tok, notes, a["texte"]) if notes else {"lisibles": False}
    return rec


def charger_table(chemin, sha_attendue: str | None) -> dict:
    """Table scellée : empreinte du fichier = empreinte citée par la configuration (garde)."""
    from ..scellement import verifier

    sha = verifier(chemin)
    if sha_attendue is not None and sha != sha_attendue:
        raise GardeArret(f"table de tokenisation {chemin} : empreinte {sha[:12]} ≠ empreinte citée {sha_attendue[:12]}")
    t = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if t.get("version") != VERSION_TABLE:
        raise GardeArret(f"table de tokenisation : version {t.get('version')!r} ≠ {VERSION_TABLE}")
    vus = set()
    for e in t["episodes"]:
        if e.get("methode") not in METHODES:
            raise GardeArret(f"table de tokenisation : méthode inconnue {e.get('methode')!r}")
        if e["episode"] in vus:
            raise GardeArret(f"table de tokenisation : épisode {e['episode']} en double")
        vus.add(e["episode"])
    return t


def classer_episodes(signales: list[str], table: dict, seuil: int) -> tuple[dict, list[str]]:
    """Règles A et B : la table doit couvrir exactement les épisodes signalés (conformes en longueur à trajectoire
    différente, dans l'ordre du run) ; rend ({épisode: entrée à appliquer}, [épisodes non résolus]). Arrêt si un
    épisode signalé manque à la table, si la table cite un épisode non signalé, ou si les non résolus dépassent `seuil`."""
    par_ep = {e["episode"]: e for e in table["episodes"]}
    manquants = [e for e in signales if e not in par_ep]
    en_trop = sorted(set(par_ep) - set(signales))
    if manquants or en_trop:
        raise GardeArret(f"table de tokenisation non conforme au run : manquants {manquants[:3]} ({len(manquants)}), "
                         f"en trop {en_trop[:3]} ({len(en_trop)})")
    corriger = {e: par_ep[e] for e in signales if par_ep[e]["methode"] != "non_resolu"}
    non_resolus = [e for e in signales if par_ep[e]["methode"] == "non_resolu"]
    if len(non_resolus) > int(seuil):
        raise GardeArret(f"{len(non_resolus)} épisode(s) conformes en longueur restés différents de P3 après la table "
                         f"(au-delà du seuil de {seuil}) : {non_resolus[:3]} : reconstruction non fidèle, rien n'est versé")
    return corriger, non_resolus


def calculer_table(fmt, lignes, identite, fiches: dict, taches, consignes, guide, T: int, meta: dict,
                   progres=None) -> dict:
    """Table des corrections sur tout le run (processeur) : signale les épisodes conformes en longueur à trajectoire
    différente, applique l'ordre fixe, vérifie chaque correction trouvée par `appliquer_entree` (même chemin que
    l'instance) ; JSON déterministe (aucune date, aucun temps)."""
    from ..environnements.pilote_a import tache_de
    from ..premier_test_ia.conditions import environnement

    jetons = [int(x) for x in identite["jetons"]]
    jetons_notes = [int(x) for x in identite["jetons_notes"]]
    par_ep: dict[str, list[int]] = {}
    for i, x in enumerate(lignes):
        par_ep.setdefault(x["episode"], []).append(i)
    octets, par_octets = table_des_octets(fmt.tok)
    entrees, comptes = [], {"episodes": len(par_ep), "conformes_longueur": 0, "identiques_base": 0, "signales": 0}
    for e, rs in par_ep.items():
        x0 = lignes[rs[0]]
        env = environnement(x0["condition"], tache_de(taches[x0["tache"]]), T, guide, consignes)
        L, J, JN = [lignes[r] for r in rs], [jetons[r] for r in rs], [jetons_notes[r] for r in rs]
        rec = reconstruire_episode(fmt, env, T, L, J, JN)
        conf = all(a["conforme"] for a in rec["actions"])
        ident = empreinte_trajectoire(episode_harnais(e, T, rec)) == fiches[e]["trajectoire"]
        comptes["conformes_longueur"] += conf
        comptes["identiques_base"] += ident
        if not conf or ident:
            continue
        comptes["signales"] += 1
        t0 = time.perf_counter()
        ent = resoudre_episode(fmt, env, T, L, J, JN, fiches[e]["trajectoire"], e, octets, par_octets)
        if ent["methode"] != "non_resolu":
            r2 = appliquer_entree(fmt, env, T, L, J, JN, ent, octets)
            if empreinte_trajectoire(episode_harnais(e, T, r2)) != fiches[e]["trajectoire"]:
                raise GardeArret(f"{e} : correction trouvée mais non redonnée par appliquer_entree")
            ent["textes_p3"] = [{"pas": p["pas"], "p3": [fmt.tok.convert_ids_to_tokens(i) for i in p["p3"]],
                                 "canonique": [fmt.tok.convert_ids_to_tokens(i) for i in p["canonique"]]}
                                for p in ent["paires"]]
        entrees.append(ent)
        if progres:
            progres(e, ent["methode"], round(time.perf_counter() - t0, 1))
    for m in METHODES:
        comptes[m] = sum(1 for x in entrees if x["methode"] == m)
    comptes["identiques_apres_table"] = comptes["identiques_base"] + sum(comptes[m] for m in METHODES[:3])
    return {"version": VERSION_TABLE, "regle": REGLE, **meta, "fins_du_format": sorted(int(x) for x in fmt.fins),
            "comptes": comptes, "episodes": entrees}


def _main(argv: list[str]) -> int:
    from transformers import AutoTokenizer

    from ..environnements.invites import charger_invite
    from ..environnements.pilote_a import charger_taches
    from ..harnais.formats import FormatChat
    from ..premier_test_ia.conditions import charger_consignes
    from ..scellement import verifier
    from .alignement_v1 import charger_identite, charger_textes_alignes
    from .rejeu_activations_v1 import charger_fiches

    ap = argparse.ArgumentParser(prog="python -m controle_ia.runs_nuit.resolution_tokenisation_v1")
    ap.add_argument("--tokeniseur", required=True, help="dossier du tokeniseur de l'agent, à la révision citée")
    ap.add_argument("--config", required=True, help="configuration du rejeu (chemins et empreintes des pièces de P3)")
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    sortie = Path(a.sortie)
    if sortie.exists():
        raise GardeArret(f"{sortie} existe déjà (R12 : on n'écrase jamais)")
    c = json.loads(Path(a.config).read_text(encoding="utf-8"))
    tok = AutoTokenizer.from_pretrained(a.tokeniseur)
    fmt = FormatChat(tok, variables=c["agent"]["variables_gabarit"])
    # fins de l'instance : configuration de génération de Llama 3.1 (128001, 128008, 128009) et fin du tokeniseur,
    # plus le premier jeton de clôture (`charger_modele_et_format`)
    fmt.fins = {128001, 128008, 128009, int(tok.eos_token_id)} | {fmt._pieces(("x", "y"))["cloture"][0]}
    identite = charger_identite(c["chemin_scores"], c["scores_sha256"])
    lignes = charger_textes_alignes(c["chemin_textes"], identite, c["textes_sha256"])
    fiches = charger_fiches(c["chemin_fiches"], c["fiches_sha256"])
    taches = {t["identifiant"]: t for t in charger_taches(c["chemin_taches"])}
    if c["taches_sha256"] is not None and verifier(c["chemin_taches"]) != c["taches_sha256"]:
        raise GardeArret("tâches : empreinte ≠ empreinte citée")
    consignes = charger_consignes(c["chemin_consignes"], c["consignes_sha256"])
    guide = charger_invite("H1-classification")
    tk = {n: hashlib.sha256((Path(a.tokeniseur) / n).read_bytes()).hexdigest()
          for n in ("tokenizer.json", "tokenizer_config.json", "special_tokens_map.json")
          if (Path(a.tokeniseur) / n).exists()}
    meta = {"run_source": c["run_source"], "textes_sha256": c["textes_sha256"], "scores_sha256": c["scores_sha256"],
            "fiches_sha256": c["fiches_sha256"], "identite_sha256": c["identite_sha256"],
            "agent": {"modele": c["agent"]["modele"], "revision": c["agent"]["revision"]}, "tokeniseur_sha256": tk,
            "T": int(c["T"])}
    t0 = time.perf_counter()
    table = calculer_table(fmt, lignes, identite, fiches, taches, consignes, guide, int(c["T"]), meta,
                           progres=lambda e, m, s: print(f"{e} : {m} ({s} s)", file=sys.stderr, flush=True))
    sortie.write_text(json.dumps(table, sort_keys=True, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"comptes": table["comptes"], "duree_s": round(time.perf_counter() - t0, 1),
                      "sha256": hashlib.sha256(sortie.read_bytes()).hexdigest()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
