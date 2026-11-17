"""Essais du crible (iii) — v2 (suit les essais v1, gardés tels quels : noyau v2 ; cas du tour 1 de la contre-lecture du code :
exception du gardien, exception d'un monde, arrêt réel après la ligne du minimum ; niveau B : préparation réelle des mondes et
effet de K1) : cas sain et artefact pour chaque ligne de la liste d'arrêt (R5), filtre éprouvé sur des cas écrits à
la main, mesure et lecture sur des tables synthétiques. Aucun appel, aucune clé, aucune machine.

Niveau A (`essais_noyau`) : noyau, mesure et lecture seuls, proposeurs scriptés en mémoire, horloge réelle à bornes réduites (le
mode réel refuse ces bornes). Niveau B (`essai_a_blanc_crible_iii_v2.py`) : chaîne du pilote (commande,
relais factice, gardien) sur des mondes de développement à graine publique ; son cas `essais_arbre_k1` (préparation réelle
des mondes) est dans ce fichier, joué aussi par le banc de mutations.

Usage : python3 -I -B essais_crible_iii_v2.py            (niveau A ; code 0 si tous les essais passent)
        python3 -I -B essais_crible_iii_v2.py --arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H   (niveau B, K1)
Le banc de mutations (`mutations_crible_iii_v2.py`) rejoue ces essais sur des copies mutées des modules.
"""
from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import threading
import time

ICI = os.path.dirname(os.path.abspath(__file__))
if ICI not in sys.path:
    sys.path.insert(0, ICI)

RACINE_ESSAI = int("ab" * 32, 16)
BORNES_RAPIDES = {"appel_s": 0.4, "monde_s": 0.96, "marge_s": 0.5}
CONSIGNE_FACTICE = "Consigne factice G0."


# --- mondes et proposeurs scriptés (niveau A) -----------------------------------------------------------------------------------

def servis_factices(N):
    out, traits = {}, {}
    for r in N.MONDES:
        g0 = CONSIGNE_FACTICE + "\n\n```json\n" + json.dumps({"monde": r, "k1": [r % 8]}) + "\n```\n"
        h = N.filtre(N.tirer_ensembles_h(RACINE_ESSAI, r), [[r % 8]])["retenus"]
        out[r] = {"g0": g0, "g1": N.texte_g1(g0, CONSIGNE_FACTICE), "h": h}
        traits[r] = [[r % 8]]
    return out, traits


def cartes_json(k):
    return "```json\n" + json.dumps([{"enonce": f"c{i}", "loi_predictive": {"type": "fixe", "probas": [1, 1, 1]}}
                                       for i in range(k)]) + "\n```"


def sets_json(r):
    return "```json\n" + json.dumps([[r % 8], [0, 1], [2, 3], [4], [5, 6, 7], [1, 2], [3, 4], [0, 1], [9]]) + "\n```"


class Scripte:
    """Appeler scripté : scénario par (monde, bras) ; durée simulée ; borne honorée comme la commande (coupé au délai)."""

    def __init__(self, N, scenarios=None, duree=0.01):
        self.N, self.sc, self.duree = N, scenarios or {}, duree
        self.vus = []
        self.verrou = threading.Lock()

    def __call__(self, bras, nom, texte, r, delai):
        s = self.sc.get((r, bras)) or self.sc.get(("*", bras)) or "normal"
        with self.verrou:
            self.vus.append((r, bras, texte))
        d = float(s[5:]) if s.startswith("lent-") else self.duree
        if d > delai:
            time.sleep(delai)
            return {"etat": "echec", "cout_usd": 3.0 if nom == self.N.PR4 else 2.0, "coupe": True, "limite_debit": False}
        time.sleep(d)
        if s == "panne":
            return {"etat": "echec", "cout_usd": 0.01, "limite_debit": False}
        if s == "limite":
            return {"etat": "echec", "cout_usd": 0.0, "limite_debit": True}
        if s == "temoin_absent":
            raise self.N.Arret("réponse brute ou témoin d'isolement absent", "témoin supprimé (essai)")
        if s == "cout_excessif":
            raise self.N.Arret("coût au-dessus du pire cas", "relevé gonflé (essai)")
        if s == "tronque":  # la passe 1 tronquée porte une liste lisible : seul son état doit empêcher D et B
            return {"etat": "tronque", "cout_usd": 2.79, "texte": sets_json(r) if bras == "P1" else "```json\n[",
                    "limite_debit": False}
        if bras == "P1":
            t = "Je ne propose rien." if s == "sans_liste" else sets_json(r)
            return {"etat": "complet", "cout_usd": 0.26, "texte": t, "limite_debit": False}
        k = texte.count("\nEnsemble ") if bras != "S" else 6
        return {"etat": "complet", "cout_usd": 2.5 if nom == self.N.PR4 else 0.26, "texte": cartes_json(max(k, 1)),
                "limite_debit": False}


def gardien_factice(r, bras, nom, texte):
    import re
    m = re.search(r"```json\s*(.*?)\s*```", texte, re.S)
    try:
        props = json.loads(m.group(1)) if m else []
    except ValueError:
        props = []
    return ([{"emplacement": i, "etat": "admise" if i <= 6 else "refusee", "loi": p.get("loi_predictive")}
             for i, p in enumerate(props, start=1)], None)


def jouer(N, scripte, echeance=None, parts=None, bornes=None):
    servis, traits = servis_factices(N)
    return N.jouer_crible(servis, scripte, gardien_factice, time.time, echeance or (time.time() + 10 ** 6),
                          {N.PR4: 3.0, N.PR2: 2.0}, parts or N.PARTS_USD, bornes or BORNES_RAPIDES, "a_blanc", RACINE_ESSAI, traits)


def gardien_qui_leve(cible):
    """Gardien qui lève une exception sur le seul appel `cible` = (monde, bras), le gardien factice ailleurs (tour 1, M1)."""
    def g(r, bras, nom, texte):
        if (r, bras) == cible:
            raise ValueError("gardien en panne (essai)")
        return gardien_factice(r, bras, nom, texte)
    return g


def jouer_t1(N, scripte, gardien=None, traits_faux=None):
    """Comme `jouer`, avec un gardien et des traits d'archive au choix (essais du tour 1)."""
    servis, traits = servis_factices(N)
    traits.update(traits_faux or {})
    return N.jouer_crible(servis, scripte, gardien or gardien_factice, time.time, time.time() + 10 ** 6, {N.PR4: 3.0, N.PR2: 2.0},
                          N.PARTS_USD, BORNES_RAPIDES, "a_blanc", RACINE_ESSAI, traits)


def tous_listes(rel):
    """Chaque appel fait (réservé puis appelé) est au relevé : aucun n'est perdu."""
    return sum(rel["appels_faits"].values()) == sum(1 for a in rel["appels"] if a.get("appele"))


class EnVol:
    """Appeler scripté dont l'appel `cible`, encore en vol quand la ligne du minimum se déclenche, rend une `Arret` après 0,3 s."""

    def __init__(self, N, base, cible):
        self.N, self.base, self.cible = N, base, cible

    def __call__(self, bras, nom, texte, r, delai):
        if (r, bras) == self.cible:
            time.sleep(0.3)
            raise self.N.Arret("réponse brute ou témoin d'isolement absent", "témoin supprimé après la ligne du minimum (essai)")
        return self.base(bras, nom, texte, r, delai)


def refuse(f, *a, exc=Exception):
    """Motif du refus si `f(*a)` lève l'exception attendue ; None sinon (aucun refus, ou une autre exception : pas un refus
    nommé)."""
    try:
        f(*a)
    except exc as e:
        return str(e) or type(e).__name__
    except Exception:  # noqa: BLE001
        return None
    return None


# --- niveau A ---------------------------------------------------------------------------------------------------------------------

def essais_noyau(N, ME, L):
    R = []

    def note(nom, sain, artefact, detail=""):
        R.append({"essai": nom, "sain": bool(sain), "artefact": bool(artefact), "detail": detail})

    # filtre, cas écrits à la main
    f = N.filtre([(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,)], [])
    note("filtre : égalités par l'ordre des noms", f["retenus"] == [(0,), (1,), (2,), (3,), (4,), (5,)],
         N.filtre([(7,), (6,), (5,), (4,), (3,), (2,), (1,), (0,)], [])["retenus"] == f["retenus"], str(f["retenus"]))
    f = N.filtre([(0, 1), (0, 1, 2), (0, 2)], [])
    note("filtre : moins de six", f["k"] == 3 and f["moins_de_six"], N.filtre([], [])["k"] == 0, str(f))
    f = N.filtre([(1, 2), (3,), (1, 2), (3,)], [])
    note("filtre : doublons", f["doublons"] == 2 and f["retenus"] == [(1, 2), (3,)], f["k"] == 2, str(f))
    f = N.filtre([(4,), (4, 5), (2,)], [[4]])
    note("filtre : ensemble de l'archive retiré", f["retires_archive"] == 1 and (4,) not in f["retenus"],
         (4, 5) in f["retenus"], str(f))
    f = N.filtre([(0,), (0, 1), (0, 1, 2), (3, 4), (5,), (6, 7), (2, 6)], [])
    note("filtre : distance de Jaccard maximin", f["retenus"][:3] == [(0,), (2, 6), (3, 4)], f["k"] == 6, str(f["retenus"]))
    lu = N.analyser_passe1("```json\n" + json.dumps([[0], [9], "x", [1, 1], [0, 1, 2, 3], []] + [[i % 8, (i + 1) % 8]
                                                                                              for i in range(25)]) + "\n```")
    note("analyseur : invalides comptés, au-delà de vingt ignorés", lu["invalides"] == 5 and lu["ignores"] == 6,
         len(lu["valides"]) == 20, f"{lu['invalides']} invalides, {lu['ignores']} ignorés")
    note("analyseur : réponse sans liste", N.analyser_passe1("rien")["valides"] == [], N.analyser_passe1("{}")["lecture"] is not None)
    # filtre : entrées (liste d'arrêt)
    note("liste d'arrêt : le filtre reçoit autre chose que la passe 1 et l'archive",
         refuse(N.filtre, [(1,)], [[2]]) is None,
         refuse(N.filtre, [(1,)], {"spec": {}, "oracle": 1}, exc=N.Refus) is not None
         and refuse(N.filtre, [{"monde": 1}], [[2]], exc=N.Refus) is not None)
    # graine de H
    a, b = N.tirer_ensembles_h(RACINE_ESSAI, 3), N.tirer_ensembles_h(RACINE_ESSAI, 3)
    note("liste d'arrêt : ensembles de H d'une graine qui dépend du monde, du secret ou de la passe 1",
         a == b and a != N.tirer_ensembles_h(RACINE_ESSAI, 4),
         refuse(N.graine_h, b"\x00" * 32, 3, exc=N.Refus) is not None and refuse(N.graine_h, {"secret": 1}, 3, exc=N.Refus)
         is not None, str(a[:3]))
    # textes de passe 2 et de B
    s, _ = servis_factices(N)
    t = N.texte_g2(s[1]["g0"], [(0, 1), (2,)])
    note("liste d'arrêt : texte servi d'une passe 2 différent de G2 et du bloc reconstruit",
         refuse(N.exiger_texte_passe2, t, s[1]["g0"], [(0, 1), (2,)]) is None,
         refuse(N.exiger_texte_passe2, t.replace("Ensemble 2 : [2]", "Ensemble 2 : [2] corrélé"), s[1]["g0"], [(0, 1), (2,)],
                exc=N.Arret) is not None
         and refuse(N.exiger_texte_passe2, t[:-2] + "x\n", s[1]["g0"], [(0, 1), (2,)], exc=N.Arret) is not None)
    note("liste d'arrêt : texte servi de B différent de celui de D",
         refuse(N.exiger_texte_b, t, N.texte_g2(s[1]["g0"], [(0, 1), (2,)])) is None,
         refuse(N.exiger_texte_b, t, N.texte_g2(s[1]["g0"], [(2,), (0, 1)]), exc=N.Arret) is not None)
    note("liste d'arrêt : texte servi de G1 ou G2 de plus de 53 000 octets",
         refuse(N.exiger_octets, "a" * 53000, "G2") is None, refuse(N.exiger_octets, "a" * 53001, "G2", exc=N.Refus) is not None)
    note("liste d'arrêt : bornes réduites en mode réel", refuse(N.exiger_bornes, dict(N.BORNES_GELEES), "reel") is None,
         refuse(N.exiger_bornes, dict(BORNES_RAPIDES), "reel", exc=N.Refus) is not None)
    note("files : le monde r va à la file r modulo 5", N.files_des_mondes()[1] == [1, 6, 11, 16] and N.files_des_mondes()[0] ==
         [5, 10, 15, 20], refuse(N.file_du_monde, 21, exc=N.Refus) is not None)
    g = {N.graine_monde_crible(bytes(32), "p", "00" * 32, r) for r in N.MONDES}
    note("graine du monde : étiquette du crible, 20 mondes distincts", len(g) == 20,
         refuse(N.graine_monde_crible, bytes(31), "p", "00" * 32, 1, exc=N.Refus) is not None)
    # lignes de GO
    reg = ("| GO-2026-11-20-01 | 2026-11-16 | calcul | Organisme d'idéation, crible (iii) « deux passes » : fable52 et opus55 | "
           "260 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; ce texte |\n"
           "| GO-2026-11-20-02 | 2026-11-16 | calcul | Même crible, part hors crédits : machine jetable seule | 3 USD | 2026-11-30 | "
           "Lazar | GO-2026-11-15-06 |\n")
    from datetime import date
    note("liste d'arrêt : toute dépense sans ligne « calcul » citant GO-2026-11-15-06",
         refuse(N.lire_go_du_crible, reg, "GO-2026-11-20-01", "GO-2026-11-20-02", date(2026, 11, 20)) is None,
         refuse(N.lire_go_du_crible, reg.replace("GO-2026-11-15-06", "GO-2026-11-15-05"), "GO-2026-11-20-01", "GO-2026-11-20-02",
                date(2026, 11, 20), exc=N.Refus) is not None
         and refuse(N.lire_go_du_crible, reg, "GO-2026-11-20-03", "GO-2026-11-20-02", date(2026, 11, 20), exc=N.Refus) is not None
         and refuse(N.lire_go_du_crible, reg.replace("260 USD", "300 USD"), "GO-2026-11-20-01", "GO-2026-11-20-02",
                    date(2026, 11, 20), exc=N.Refus) is not None)
    # ordonnanceur
    sc = Scripte(N)
    rel = jouer(N, sc)
    vus = {(r, b) for r, b, _ in sc.vus}
    dtxt = {r: t for r, b, t in sc.vus if b == "D"}
    btxt = {r: t for r, b, t in sc.vus if b == "B"}
    servis0, _ = servis_factices(N)
    refait = {r: N.texte_g2(servis0[r]["g0"], [tuple(x) for x in rel["ensembles"].get(str(r), {}).get("d_retenus", [[0]])])
              for r in N.MONDES}
    htxt = {r: t for r, b, t in sc.vus if b == "H"}
    note("crible sain : 100 appels, 20 mondes complets, B servi du texte même de D",
         len(sc.vus) == 100 and rel["complets"] == 20 and rel["arret"] is None and all(dtxt[r] == btxt.get(r) for r in dtxt),
         len(vus) == 100 and all(dtxt.get(r) == refait[r] for r in N.MONDES)
         and all(htxt.get(r) == N.texte_g2(servis0[r]["g0"], servis0[r]["h"]) for r in N.MONDES),
         f"{len(sc.vus)} appels, {rel['complets']} complets ; textes de D et H rebâtis à l'octet")
    ordre = [x for x in sc.vus]
    note("ordre dans un monde : D et B après la passe 1", all(
        min((i for i, (r2, b, _) in enumerate(ordre) if r2 == r and b in ("D", "B")), default=10 ** 9) >
        min((i for i, (r2, b, _) in enumerate(ordre) if r2 == r and b == "P1"), default=-1) for r in N.MONDES), True)
    rel = jouer(N, Scripte(N, {(3, "P1"): "sans_liste", (4, "P1"): "tronque"}))
    a3 = {x["bras"]: x["etat"] for x in rel["appels"] if x["monde"] == 3}
    note("liste d'arrêt : passe 1 sans ensemble valide, tronquée ou en échec",
         rel["complets"] == 18 and rel["arret"] is None, "D" not in a3 and "B" not in a3 and rel["mondes"]["3"] == "incomplet",
         f"{rel['complets']} complets ; monde 3 : {sorted(a3)}")
    note("liste d'arrêt : garde de départ (4 × borne du monde + 2 h)", refuse(jouer, N, Scripte(N)) is None,
         refuse(jouer, N, Scripte(N), time.time() + N.garde_de_depart(BORNES_RAPIDES) - 0.5, exc=N.Refus) is not None)
    class Saut(Scripte):  # échéance proche simulée : l'horloge avance de 3,8 s quand le dernier appel du monde 5 est rendu
        decalage = 0.0

        def __call__(self, bras, nom, texte, r, delai):
            res = Scripte.__call__(self, bras, nom, texte, r, delai)
            if r == 5 and bras in ("D", "B"):
                with self.verrou:
                    self.fin5 = getattr(self, "fin5", 0) + 1
                    if self.fin5 == 2:
                        Saut.decalage = 3.8
            return res
    e = time.time() + N.garde_de_depart(BORNES_RAPIDES) + 0.3
    servis, traits = servis_factices(N)
    sc = Saut(N, {(5, "D"): "lent-0.3", (5, "B"): "lent-0.3"}, duree=0.02)
    rel = N.jouer_crible(servis, sc, gardien_factice, lambda: time.time() + Saut.decalage, e, {N.PR4: 3.0, N.PR2: 2.0},
                         N.PARTS_USD, BORNES_RAPIDES, "a_blanc", RACINE_ESSAI, traits)
    note("liste d'arrêt : minuterie au départ d'un monde (borne du monde + 2 h)",
         N.marge_d_un_monde(100.0, 100.0 - N.garde_d_un_monde(BORNES_RAPIDES) - 0.01, BORNES_RAPIDES),
         not N.marge_d_un_monde(100.0, 100.0 - N.garde_d_un_monde(BORNES_RAPIDES) + 0.01, BORNES_RAPIDES)
         and rel["arret"] is not None and rel["arret"]["ligne"] == "minuterie"
         and all(v != "en cours" for v in rel["mondes"].values()) and rel["mondes"]["20"] == "non commence",
         str(rel["arret"]))
    rel = jouer(N, Scripte(N, {(2, "S"): "lent-0.3"}))
    rel2 = jouer(N, Scripte(N, {(2, "S"): "lent-0.45", (7, "D"): "lent-0.45"}))
    c2 = next(x for x in rel2["appels"] if x["monde"] == 2 and x["bras"] == "S")
    note("liste d'arrêt : borne par appel (appel coupé, compté en échec, les autres files continuent)",
         rel["complets"] == 20, c2["etat"] == "echec" and c2.get("coupe") and rel2["complets"] == 18, f"{c2.get('etat')}")
    rel = jouer(N, Scripte(N), parts={N.PR2: 80.0, N.PR4: 20.0})
    note("liste d'arrêt : dépense d'un relais atteignant sa part", jouer(N, Scripte(N))["arret"] is None,
         rel["arret"] is not None and rel["arret"]["ligne"] == "part" and rel["depense_usd"][N.PR4] <= 20.0 + 1e-9,
         str(rel["arret"]))
    rel_ok = jouer(N, Scripte(N, {(1, "S"): "panne"}))
    rel = jouer(N, Scripte(N, {(r, "P1"): "panne" for r in N.MONDES if r >= 3}))
    rel5 = jouer(N, Scripte(N, {(r, "P1"): "panne" for r in (1, 2, 3, 4, 5)}))
    note("liste d'arrêt : complets + en cours + non commencés < 16 (minimum)",
         rel_ok["arret"] is None and rel_ok["complets"] == 19,
         rel["arret"] is not None and rel["arret"]["ligne"] == "minimum" and len(rel["appels"]) < 100
         and rel5["arret"] is not None and rel5["arret"]["ligne"] == "minimum",
         f"{rel['arret']} ; {len(rel['appels'])} appels")
    rel = jouer(N, Scripte(N, {(r, "S"): "limite" for r in (1, 2, 3, 4, 5, 6, 7)}))
    note("liste d'arrêt : erreurs de limite de débit sur plus de 5 % des appels du fournisseur",
         jouer(N, Scripte(N))["arret"] is None,
         rel["arret"] is not None and rel["arret"]["ligne"] == "limite de débit", str(rel["arret"]))
    rel = jouer(N, Scripte(N, {(6, "H"): "temoin_absent"}))
    note("liste d'arrêt : réponse brute ou témoin d'isolement absent (code 3)", True,
         rel["arret"] is not None and rel["arret"]["code"] == 3 and len(rel["appels"]) < 100, str(rel["arret"]))
    rel = jouer(N, Scripte(N, {(9, "D"): "cout_excessif"}))
    note("liste d'arrêt : coût d'un appel au-dessus de son pire cas (code 3)", True,
         rel["arret"] is not None and rel["arret"]["ligne"] == "coût au-dessus du pire cas", str(rel["arret"]))
    # tour 1 de la contre-lecture du code : M1 (exception du gardien, exception d'un monde, appels en vol), m3 (après le minimum)
    rel_ok = jouer_t1(N, Scripte(N))
    rel = jouer_t1(N, Scripte(N), gardien=gardien_qui_leve((3, "H")))
    h3 = [x for x in rel["appels"] if x["monde"] == 3 and x["bras"] == "H"]
    note("liste d'arrêt : exception du gardien (arrêt, code 3 ; l'appel reste au relevé, sa dépense comptée)",
         rel_ok["arret"] is None and rel_ok["complets"] == 20 and tous_listes(rel_ok),
         rel["arret"] is not None and rel["arret"]["ligne"] == "exception du gardien" and rel["arret"]["code"] == 3
         and len(h3) == 1 and h3[0]["appele"] and float(h3[0].get("cout_usd") or 0) > 0 and tous_listes(rel),
         f"{rel['arret']} ; {sum(rel['appels_faits'].values())} appels faits, {sum(1 for x in rel['appels'] if x.get('appele'))} listés")
    rel = jouer_t1(N, Scripte(N, {(3, "S"): "lent-0.3"}), traits_faux={3: [["x"]]})
    s3 = [x for x in rel["appels"] if x["monde"] == 3 and x["bras"] == "S"]
    note("liste d'arrêt : exception dans un monde (filtre qui lève : arrêt, code 3 ; aucune file muette ; appel en vol listé)",
         rel_ok["arret"] is None and all(v == "complet" for v in rel_ok["mondes"].values()),
         rel["arret"] is not None and rel["arret"]["ligne"] == "exception d'un monde" and rel["arret"]["code"] == 3
         and rel["mondes"]["3"] == "incomplet" and all(v != "en cours" for v in rel["mondes"].values())
         and len(s3) == 1 and s3[0]["appele"] and tous_listes(rel),
         f"{rel['arret']} ; appel S du monde 3 {'listé' if s3 else 'absent du relevé'}")
    panne = {(r, "P1"): "panne" for r in (1, 2, 3, 4, 6)}
    rel_s = jouer_t1(N, Scripte(N, {**panne, (5, "S"): "lent-0.3"}))
    rel_a = jouer_t1(N, EnVol(N, Scripte(N, panne), (5, "S")))
    rel_g = jouer_t1(N, Scripte(N, {**panne, (5, "S"): "lent-0.3"}), gardien=gardien_qui_leve((5, "S")))
    note("liste d'arrêt : arrêt réel d'un appel en vol après la ligne du minimum (il la remplace : code 3)",
         rel_s["arret"] is not None and rel_s["arret"]["ligne"] == "minimum" and rel_s["arret"]["code"] == 0,
         rel_a["arret"] is not None and rel_a["arret"]["ligne"] == "réponse brute ou témoin d'isolement absent"
         and rel_a["arret"]["code"] == 3 and rel_g["arret"] is not None and rel_g["arret"]["ligne"] == "exception du gardien"
         and rel_g["arret"]["code"] == 3,
         f"sain : {rel_s['arret']} ; témoin : {rel_a['arret']} ; gardien : {rel_g['arret']}")
    # mesure, sur des mondes synthétiques (outils factices)
    R += essais_mesure(N, ME)
    R += essais_lecture(L)
    return R


class OutilsFactices:
    """Monde synthétique : la composante i est portée par une carte dont la loi est {"type": "fixe", "porte": [ids]} ; « E1 » est
    l'effet de K1 ; « E9 » une composante non certifiée ; une loi {"type": "non"} n'est pas évaluable."""

    def preparer(self, w):
        return {"monde": w["monde"], "spec": {"effets": [{"id": f"E{i}", "classe": "moyenne"} for i in range(1, 6)]},
                "comptees": ["E2", "E3", "E4", "E5"], "comptees_tau2": ["E2", "E3", "E4", "E5"],
                "comptees_toutes": ["E2", "E3", "E4", "E5", "E9"], "premiere": "E5", "distracteurs": [7],
                "traits": {"E2": [1], "E3": [2], "E4": [3, 4], "E5": [5, 6]}, "traits_k1": [0], "sha": str(w["monde"])}

    def porte(self, pm, loi):
        if loi.get("type") == "non":
            return None
        s = set(loi.get("porte", []))
        return (s, s)


def releve_synthetique(N, couverture, cout=None, etats=None):
    """Relevé et cartes : couverture[r][bras] = liste des composantes portées par une carte valide."""
    appels, cartes, ens = [], [], {}
    for r in range(1, 21):
        for b in N.BRAS:
            e = (etats or {}).get((r, b), "complet")
            appels.append({"monde": r, "bras": b, "proposeur": N.PROPOSEUR_DU_BRAS[b], "etat": e, "appele": True,
                           "cout_usd": (cout or {}).get(b, 2.5 if N.PROPOSEUR_DU_BRAS[b] == N.PR4 else 0.26)})
            if b != "P1":
                cartes.append({"monde": r, "bras": b, "proposeur": N.PROPOSEUR_DU_BRAS[b], "emplacement": 1, "etat": "admise",
                               "loi": {"type": "fixe", "porte": couverture.get(r, {}).get(b, [])}})
        ens[str(r)] = {"d_retenus": [[1], [2], [3, 4], [5], [6], [0, 1]], "d_k": 6, "h_retenus": [[1], [2]],
                       "passe1_valides": [[1], [2]], "passe1": {"invalides": 0, "ignores": 0}}
    return {"appels": appels, "ensembles": ens, "arret": None}, {"cartes": cartes}


def essais_mesure(N, ME):
    R = []

    def note(nom, sain, artefact, detail=""):
        R.append({"essai": nom, "sain": bool(sain), "artefact": bool(artefact), "detail": detail})
    mondes = [{"monde": r} for r in range(1, 21)]
    cov = {r: {"S": ["E2"], "D": ["E2", "E3"], "H": ["E2"], "B": ["E2"]} for r in range(1, 21)}
    rel, cartes = releve_synthetique(N, cov)
    m = ME.mesurer(mondes, rel, cartes, RACINE_ESSAI, OutilsFactices(), b_max=400)
    est = m["principal"]["estimations"]
    note("mesure : δ_DB et dollars de D et de B (passe 1 comptée dans les deux)",
         abs(est["delta_DB"] - 1.0) < 1e-12 and abs(m["principal"]["sommes"]["dollars"]["D"] - 20 * 2.76) < 1e-6,
         abs(m["principal"]["sommes"]["dollars"]["B"] - 20 * 0.52) < 1e-6 and abs(m["principal"]["sommes"]["dollars"]["S"] - 50) < 1e-6,
         str(m["principal"]["sommes"]))
    note("mesure : intervalles à 97,5 % pour les principales, 95 % ailleurs",
         m["principal"]["niveaux"]["delta_R"] == 0.975 and m["principal"]["niveaux"]["delta_DB"] == 0.975,
         m["principal"]["niveaux"]["delta_DH"] == 0.95 and m["principal"]["niveaux"]["delta_HS"] == 0.95)
    cov_k1 = {r: {"S": ["E1"], "D": ["E1"], "H": ["E1"], "B": ["E1"]} for r in range(1, 21)}
    rel2, cartes2 = releve_synthetique(N, cov_k1)
    m2 = ME.mesurer(mondes, rel2, cartes2, RACINE_ESSAI, OutilsFactices(), b_max=50)
    note("liste d'arrêt : couverture comptant l'effet de K1", m["principal"]["sommes"]["C"]["D"] == 40,
         m2["principal"]["sommes"]["C"]["D"] == 0 and m2["zone_utile_mondes"] == 0, str(m2["principal"]["sommes"]["C"]))
    c3 = json.loads(json.dumps(cartes))
    c3["cartes"].append({"monde": 1, "bras": "D", "proposeur": N.PR4, "emplacement": 7, "etat": "admise",
                         "loi": {"type": "fixe", "porte": ["E4"]}})
    c4 = json.loads(json.dumps(cartes))
    c4["cartes"].append({"monde": 1, "bras": "D", "proposeur": N.PR4, "emplacement": 2, "etat": "refusee",
                         "loi": {"type": "fixe", "porte": ["E4"]}})
    c4["cartes"].append({"monde": 2, "bras": "D", "proposeur": N.PR4, "emplacement": 3, "etat": "admise", "loi": {"type": "non"}})
    m4 = ME.mesurer(mondes, rel, c4, RACINE_ESSAI, OutilsFactices(), b_max=50)
    rel5, c5 = releve_synthetique(N, cov, etats={(1, "D"): "tronque"})
    m5 = ME.mesurer(mondes, rel5, c5, RACINE_ESSAI, OutilsFactices(), b_max=50)
    note("liste d'arrêt : couverture comptant une carte refusée, tronquée, au-delà de six ou non évaluable",
         m4["principal"]["sommes"]["C"]["D"] == 40 and m5["n_complets"] == 19
         and ME.cartes_valides([{"emplacement": 1, "etat": "admise", "loi": {"type": "fixe", "porte": ["E2"]}}],
                               {"etat": "tronque"}, OutilsFactices(), OutilsFactices().preparer({"monde": 1})) == [],
         refuse(ME.mesurer, mondes, rel, c3, RACINE_ESSAI, OutilsFactices(), exc=ME.Defaut) is not None,
         f"refusée et non évaluable : {m4['principal']['sommes']['C']['D']} ; tronqué : {m5['n_complets']} complets")
    note("mesure : rapport réintégré de δ_DB (un seul de D et B tronqué, C = 0)", m["reintegre_delta_DB"]["n"] == 20,
         m5["reintegre_delta_DB"]["n"] == 20 and m5["reintegre_delta_DB"]["estimation"] < m["principal"]["estimations"]["delta_DB"],
         str(m5["reintegre_delta_DB"]["estimation"]))

    class Casse(OutilsFactices):
        def preparer(self, w):
            return 1 / 0
    note("liste d'arrêt : exception de la mesure (pas un refus nommé)", True,
         refuse(ME.mesurer, mondes, rel, cartes, RACINE_ESSAI, Casse(), exc=ZeroDivisionError) is not None)
    d = tempfile.mkdtemp()
    open(os.path.join(d, ME.SORTIE), "w").close()
    buf = io.StringIO()
    so = sys.stdout
    sys.stdout = buf
    try:
        code = ME.main(["mesurer", "--arbre", d, "--mondes", os.path.join(d, "x"), "--mondes-sha256", "0" * 64, "--sortie", d,
                        "--texte-sha256", "0" * 64])
    except Exception as e:  # noqa: BLE001 — une seconde mesure qui va plus loin que le refus nommé
        code = f"exception {type(e).__name__}"
    finally:
        sys.stdout = so
    note("liste d'arrêt : mesure lancée deux fois", True, code == 2 and "seconde mesure refusée" in buf.getvalue(), buf.getvalue()[:80])
    note("mesure : test exact des signes rapporté", m["principal"]["signes"]["DB"]["plus"] == 20, True)
    return R


def corps_synthetique(**k):
    base = {"n_complets": 20, "fournisseur_perdu": False, "format_tenu_mondes": 20, "zone_utile_mondes": 20,
            "tronques_par_bras": {"S": 0, "D": 0, "H": 0, "B": 0}, "execution": {"D": {"E": 0.9}},
            "reintegre_delta_DB": {"intervalle_97_5": [0.1, 0.9]},
            "principal": {"intervalles": {"delta_R": [-0.1, 0.2], "delta_DB": [0.1, 0.9], "delta_DH": [-0.2, 0.3],
                                          "delta_HS": [-0.2, 0.2]},
                          "estimations": {"delta_HS": 0.0}, "R": {}, "signes": {}},
            "bruit": {}, "choix_passe1": {}, "conditionnelles": {}, "sensibilites": {}, "jetons_et_dollars_par_passe": {},
            "audit": {}}
    base.update(k)
    return base


def essais_lecture(L):
    R = []

    def note(nom, sain, artefact, detail=""):
        R.append({"essai": nom, "sain": bool(sain), "artefact": bool(artefact), "detail": detail})
    c = corps_synthetique()
    v = L.lire({"arret": None}, c)
    note("lecture : étages 4 à 6 (P1 non tranché, P2 perte établie, Q pas mieux que le hasard)",
         v["verdicts"]["4"] == "non tranché" and v["verdicts"]["5"].startswith("perte établie") and v["verdicts"]["6"]["Q"]
         == "pas mieux que le hasard au crible", v["etage_arret"] == 7, json.dumps(v["verdicts"], ensure_ascii=False)[:120])
    note("lecture : étage 0 (ligne d'arrêt autre que le minimum ; mesure en erreur)",
         L.lire({"arret": None}, c)["etage_arret"] == 7,
         L.lire({"arret": {"ligne": "limite de débit"}}, c)["etage_arret"] == 0 and L.lire({"arret": None}, None)["etage_arret"] == 0)
    note("lecture : étage 1 (minimum, n_c < 16, fournisseur perdu)", True,
         L.lire({"arret": {"ligne": "minimum"}}, c)["verdicts"] == {"1": "non concluant"}
         and L.lire({"arret": None}, corps_synthetique(n_complets=15))["etage_arret"] == 1
         and L.lire({"arret": None}, corps_synthetique(fournisseur_perdu=True))["etage_arret"] == 1)
    cb = corps_synthetique(tronques_par_bras={"S": 0, "D": 0, "H": 0, "B": 3})
    vb = L.lire({"arret": None}, cb)
    note("lecture : étage 2 (« B tronqué » interdit « perte établie »)", "B tronqué" not in v["reserves"],
         "B tronqué" in vb["reserves"] and vb["verdicts"]["5"].startswith("phrase interdite"), vb["verdicts"]["5"][:60])
    note("lecture : étage 2 (format non tenu, consigne non suivie)", v["reserves"] == [],
         "format non tenu" in L.lire({"arret": None}, corps_synthetique(format_tenu_mondes=13))["reserves"]
         and "consigne non suivie" in L.lire({"arret": None}, corps_synthetique(execution={"D": {"E": 0.4}}))["reserves"])
    note("lecture : étage 3 (zone utile)", True, L.lire({"arret": None}, corps_synthetique(zone_utile_mondes=9))["etage_arret"] == 3)
    cr = corps_synthetique(reintegre_delta_DB={"intervalle_97_5": [-0.1, 0.4]})
    note("lecture : P2 sensible à la troncature", True, "P2 sensible à la troncature" in L.lire({"arret": None}, cr)["reserves"])
    return R


def imprimer(R, sortie=sys.stdout):
    ko = [r for r in R if not (r["sain"] and r["artefact"])]
    for r in R:
        print(f"ESSAI {'OK ' if r['sain'] and r['artefact'] else 'ÉCHEC'} | {r['essai']} | sain {'oui' if r['sain'] else 'NON'} | "
              f"artefact {'refusé' if r['artefact'] else 'NON REFUSÉ'} | {r['detail'][:150]}", file=sortie)
    print(f"ESSAIS : {len(R)} cas, {len(R) - len(ko)} passés, {len(ko)} échecs", file=sortie)
    return 0 if not ko else 1


def controle_k1(pm, porte_k1):
    """Composantes comptées d'un monde préparé par la mesure (définition de la pièce) : ni l'effet de K1, ni ce que K1 servie porte
    à elle seule, et toutes certifiées. Rend la liste des écarts (vide si conforme)."""
    comptees, certifiees = set(pm["comptees"]), set(pm["certifiees"])
    ecarts = []
    if pm["eid_k1"] in comptees:
        ecarts.append("effet de K1 compté")
    if comptees & set(porte_k1):
        ecarts.append("composante portée par K1 comptée")
    if not comptees <= certifiees:
        ecarts.append("composante non certifiée comptée")
    return ecarts


def essais_arbre_k1(ME, arbre, mondes):
    """Niveau B (tour 1, m4) : la préparation réelle des mondes (`OutilsMR2.preparer`, arbre réel, mondes de développement) retire
    des composantes comptées l'effet de K1 et ce que K1 porte ; sain sur chaque monde distinct, artefact sur un monde préparé puis
    faussé (effet de K1 remis). Aucun coefficient imprimé : écarts et drapeaux seulement."""
    R = []
    outils = ME.OutilsMR2(arbre)
    distincts, vus = [], set()
    for w in mondes:
        if w["spec_sha256"] not in vus:
            vus.add(w["spec_sha256"])
            distincts.append(w)
    outils.precalculer_c8(distincts)
    ecarts, drapeaux, pm, porte = {}, {}, None, []
    for w in distincts:
        pm = outils.preparer(w)
        porte = sorted(outils.porte(pm, pm["k1"])[0])
        ecarts[w["monde"]] = controle_k1(pm, porte)
        drapeaux[w["monde"]] = {"k1_certifie": pm["eid_k1"] in pm["certifiees"],
                                "porte_par_k1_certifie": bool(set(porte) & set(pm["certifiees"]))}
    faux = dict(pm, comptees=sorted(set(pm["comptees"]) | {pm["eid_k1"]})) if pm is not None else None
    R.append({"essai": "mesure, arbre réel : composantes comptées hors de l'effet de K1 et de ce que K1 porte, toutes certifiées",
              "sain": bool(distincts) and all(not e for e in ecarts.values()),
              "artefact": faux is not None and bool(controle_k1(faux, porte)),
              "detail": json.dumps({"mondes_distincts": len(distincts), "ecarts": ecarts, "drapeaux": drapeaux}, ensure_ascii=False,
                                   sort_keys=True)})
    return R


def main_arbre(ME, argv):
    """Niveau B seul : `--arbre ORCHESTRATEUR --mondes MONDES.json --mondes-sha256 H` (mondes de développement à graine publique)."""
    import argparse
    import hashlib
    p = argparse.ArgumentParser(prog="essais_crible_iii_v2.py")
    for o in ("--arbre", "--mondes", "--mondes-sha256"):
        p.add_argument(o, required=True)
    a = p.parse_args(argv)
    with open(a.mondes, "rb") as f:
        b = f.read()
    if hashlib.sha256(b).hexdigest() != a.mondes_sha256:
        print("ESSAI ÉCHEC | niveau B | fichier des mondes : empreinte différente")
        return 1
    try:
        R = essais_arbre_k1(ME, a.arbre, json.loads(b)["mondes"])
    except Exception as e:  # noqa: BLE001 — une exception des essais est un échec, jamais un succès
        print(f"ESSAI ÉCHEC | exception des essais (niveau B) | {type(e).__name__} : {e}")
        return 1
    return imprimer(R)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    import crible_iii_v2 as N
    import lire_crible_iii_v1 as L
    import mesure_crible_iii_v1 as ME
    if argv:
        return main_arbre(ME, argv)
    try:
        R = essais_noyau(N, ME, L)
    except Exception as e:  # noqa: BLE001 — une exception des essais est un échec, jamais un succès
        import traceback
        print(f"ESSAI ÉCHEC | exception des essais | {type(e).__name__} : {e} | {traceback.format_exc().splitlines()[-3][:150]}")
        return 1
    return imprimer(R)


if __name__ == "__main__":
    raise SystemExit(main())
