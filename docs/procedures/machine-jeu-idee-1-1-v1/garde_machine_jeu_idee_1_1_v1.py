#!/usr/bin/env python3
"""Gardes de session de la machine du jeu relancé de l'idée 1.1, v1 (procédure `procedure-machine-jeu-idee-1-1-v1.md`).

Appelé par `lancer_jeu_idee_1_1_machine_v1.sh` (même dossier), sans réseau, avec `python3 -I` : aucun module du dépôt importé,
aucun appel au loueur. Code 0 : accepté ; code 2 : refus, motif sur la sortie standard (« JEU11 REFUS : … »).

- `offre-depuis-recherche RECHERCHE.json OFFRE.json` : la garde d'offre jouée **hors ligne sur chaque offre** de la sortie de
  la recherche (`… search offers … --raw`), la moins chère des offres acceptées retenue ; OFFRE.json écrit par programme
  (clés lues, jamais retapées ; mode `x`, jamais réécrit, R12). Leçon de R-2998 : le filtre de l'outil ne suffit pas.
- `offre OFFRE.json [ID]` : bornes de l'offre (avec ou sans carte : `num_gpus` entier ≥ 0, leçon du pilote v13) — processeur
  `amd64`, au moins 4 cœurs effectifs, 8 000 Mo, 20 Go de disque, fiabilité ≥ 0,98, débit descendant ≥ 100 Mb/s, prix garde
  (prix total + stockage de 20 Go) ≤ 0,06 USD/h, stockage seul ≤ 0,01 USD/h ; étiquette `jeu-idee-1-1-relance-v1`.
- `creation RACINE FEU COMMIT MAINTENANT RELANCES` : feu écrit, forme courte `R-<N> GO-AAAA-MM-JJ-NN` exactement (leçon C4) ;
  ligne `R-<N>` présente une seule fois dans `registres/decisions.md`, citant ce GO, le commit et l'étiquette ; ligne de GO
  lue comme le crochet de garde la lit (8 colonnes ; type « calcul » ; accordé par Lazar ; date du jour dans sa période ;
  aucune révocation) et dont le périmètre nomme l'idée 1.1 ; plafond lisible en USD ; une relance au plus.
- `prix-relu PRIX` : prix relu de la machine créée ≤ 0,06 USD/h, sinon destruction aussitôt.
- `depense RACINE GO CUMUL PRIX` : cumul relevé + une heure au prix relu ≥ plafond de la ligne de GO → refus (destruction).
- `identifiant ID DOSSIER` : l'identifiant à détruire est numérique, égal à `DOSSIER/id-machine.txt` (lu de l'inventaire,
  jamais tapé) et n'est aucune instance d'une autre tâche ou session.
- `absence ID TEMOIN LISTE.json` : destruction prouvée par l'absence de l'identifiant dans la liste des instances lue sans
  erreur, un témoin y étant présent (R-2789) ; jamais par un code de sortie.
"""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ETIQUETTE = "jeu-idee-1-1-relance-v1"
DISQUE_GO = 20
OFFRE_MIN = {"coeurs": 4, "memoire_vive_mo": 8000, "disque_go": 20, "fiabilite": 0.98, "debit_mbps": 100}
PRIX_MAX_USD_H = 0.06          # prix garde : prix total de l'outil + stockage de 20 Go (compte double possible : sens sûr)
STOCKAGE_MAX_USD_H = 0.01      # facturé seul quand la machine est arrêtée (« stopped ») et pas encore détruite
HEURES_PAR_MOIS = 720.0        # `storage_cost` est en USD par Go et par mois ; 720 (et non 730) : sens sûr
CLES_RECHERCHE = ("id", "num_gpus", "cpu_arch", "cpu_cores_effective", "cpu_ram", "disk_space", "dph_total",
                  "storage_cost", "inet_down")
# Instances d'autres tâches ou sessions, jamais détruites par cette procédure (R-2789, R-2996, R-3004) ; témoins permis.
INSTANCES_INTOUCHABLES = ("58936096", "58936099", "58936100", "60480302", "60599797", "60670453", "60860420",
                          "60918148", "60952525", "60953606")
FEU = re.compile(r"R-([1-9][0-9]*) (GO-\d{4}-\d{2}-\d{2}-\d{2})", re.ASCII)
LIGNE_GO = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
PLAFOND = re.compile(r"([0-9]+(?:\.[0-9]+)?) USD", re.ASCII)
COMMIT = re.compile(r"[0-9a-f]{40}", re.ASCII)
ENTIER = re.compile(r"[1-9][0-9]*", re.ASCII)
IDEE = ("idée 1.1", "idee-1-1", "idée 1.1")   # le second « idée » en forme décomposée (accent combinant)


class Refus(Exception):
    pass


def _nombre(x):
    """Nombre JSON (ou texte numérique) fini ; booléen, absent ou illisible : None (rien n'est deviné)."""
    if isinstance(x, bool) or not isinstance(x, (int, float, str)):
        return None
    try:
        v = float(x)
    except (ValueError, OverflowError):
        return None
    return v if math.isfinite(v) else None


def _fiabilite(o: dict):
    vals = [_nombre(o.get(k)) for k in ("reliability2", "reliability") if k in o]
    vals = [v for v in vals if v is not None]
    return min(vals) if vals else None


def fautes_offre_brute(o: dict) -> list[str]:
    """Fautes d'une offre de la recherche (clés de l'outil) ; liste vide : acceptée."""
    manque = [k for k in CLES_RECHERCHE if k not in o or (k == "cpu_arch" and not isinstance(o.get(k), str))
              or (k not in ("cpu_arch",) and _nombre(o.get(k)) is None)]
    if _fiabilite(o) is None:
        manque.append("reliability2|reliability")
    if manque:
        return [f"clé(s) {manque} absente(s) ou illisible(s) : forme de l'outil à vérifier ; rien n'est deviné"]
    f = []
    ng = o["num_gpus"]
    if isinstance(ng, bool) or not isinstance(ng, int) or ng < 0:
        f.append(f"num_gpus {ng!r} : entier ≥ 0 attendu (avec ou sans carte)")
    if o["cpu_arch"] != "amd64":
        f.append(f"processeur {o['cpu_arch']!r} : amd64 exigé (mêmes roues numpy et scipy que le conteneur)")
    if _nombre(o["cpu_cores_effective"]) < OFFRE_MIN["coeurs"]:
        f.append(f"cœurs effectifs {o['cpu_cores_effective']!r} < {OFFRE_MIN['coeurs']}")
    if _nombre(o["cpu_ram"]) < OFFRE_MIN["memoire_vive_mo"]:
        f.append(f"mémoire {o['cpu_ram']!r} Mo < {OFFRE_MIN['memoire_vive_mo']}")
    if _nombre(o["disk_space"]) < OFFRE_MIN["disque_go"]:
        f.append(f"disque {o['disk_space']!r} Go < {OFFRE_MIN['disque_go']}")
    if _fiabilite(o) < OFFRE_MIN["fiabilite"]:
        f.append(f"fiabilité {_fiabilite(o)!r} < {OFFRE_MIN['fiabilite']}")
    if _nombre(o["inet_down"]) < OFFRE_MIN["debit_mbps"]:
        f.append(f"débit descendant {o['inet_down']!r} Mb/s < {OFFRE_MIN['debit_mbps']}")
    if "rentable" in o and o["rentable"] is not True:
        f.append("offre non louable (rentable ≠ true)")
    st = _nombre(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS
    prix = _nombre(o["dph_total"]) + st
    if not (_nombre(o["dph_total"]) > 0 and prix <= PRIX_MAX_USD_H):
        f.append(f"prix garde {prix:.4f} USD/h (prix total {o['dph_total']!r} + stockage {st:.4f}) hors de ]0 ; {PRIX_MAX_USD_H}]")
    if not st <= STOCKAGE_MAX_USD_H:
        f.append(f"stockage {st:.4f} USD/h > {STOCKAGE_MAX_USD_H}")
    return f


def offre_construite(o: dict) -> dict:
    st = _nombre(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS
    return {"id": int(o["id"]), "num_gpus": o["num_gpus"], "cpu_arch": o["cpu_arch"], "cpu_name": str(o.get("cpu_name", ""))[:80],
            "coeurs": _nombre(o["cpu_cores_effective"]), "memoire_vive_mo": _nombre(o["cpu_ram"]),
            "disque_go": _nombre(o["disk_space"]), "fiabilite": _fiabilite(o), "debit_mbps": _nombre(o["inet_down"]),
            "prix_total_usd_h": _nombre(o["dph_total"]), "stockage_usd_h": st, "prix_garde_usd_h": _nombre(o["dph_total"]) + st,
            "etiquette": ETIQUETTE, "disque_demande_go": DISQUE_GO,
            "source": "offre-depuis-recherche (garde jouée hors ligne sur chaque offre ; clés lues, jamais retapées)"}


def exiger_offre(offre: dict, ident: str | None = None) -> dict:
    """OFFRE.json relu : forme construite par `offre_construite`, bornes rejouées."""
    f = []
    if ident is not None and (not ENTIER.fullmatch(str(ident)) or str(offre.get("id")) != str(ident)):
        f.append(f"identifiant {offre.get('id')!r} de l'offre décrite ≠ offre demandée {ident!r}")
    if offre.get("etiquette") != ETIQUETTE:
        f.append(f"étiquette {offre.get('etiquette')!r} ≠ {ETIQUETTE}")
    brute = {"id": offre.get("id"), "num_gpus": offre.get("num_gpus"), "cpu_arch": offre.get("cpu_arch"),
             "cpu_cores_effective": offre.get("coeurs"), "cpu_ram": offre.get("memoire_vive_mo"),
             "disk_space": offre.get("disque_go"), "dph_total": offre.get("prix_total_usd_h"), "inet_down": offre.get("debit_mbps"),
             "storage_cost": (_nombre(offre.get("stockage_usd_h")) or float("nan")) * HEURES_PAR_MOIS / DISQUE_GO,
             "reliability": offre.get("fiabilite")}
    f += fautes_offre_brute(brute)
    if f:
        raise Refus("offre hors des bornes du devis : " + " ; ".join(f))
    return offre


def offre_depuis_recherche(doc) -> tuple[dict, list[str]]:
    liste = doc.get("offers") if isinstance(doc, dict) else doc
    if not isinstance(liste, list) or not liste:
        raise Refus("sortie de la recherche illisible ou vide (liste d'offres attendue) : arrêt")
    ids = [o.get("id") for o in liste if isinstance(o, dict)]
    if len(ids) != len(liste) or len(set(map(str, ids))) != len(ids):
        raise Refus("sortie de la recherche : offre non objet ou identifiant en double : arrêt")
    acceptees, journal = [], []
    for o in liste:
        if isinstance(o.get("id"), bool) or not ENTIER.fullmatch(str(o.get("id"))):
            journal.append(f"offre {o.get('id')!r} : identifiant illisible")
            continue
        fautes = fautes_offre_brute(o)
        journal.append(f"offre {o['id']} : " + ("acceptée" if not fautes else "refusée : " + " ; ".join(fautes)))
        if not fautes:
            acceptees.append(offre_construite(o))
    if not acceptees:
        raise Refus("aucune offre acceptée par la garde sur " + str(len(liste)) + " :\n  " + "\n  ".join(journal))
    acceptees.sort(key=lambda x: (x["prix_garde_usd_h"], x["id"]))
    return acceptees[0], journal


def lire_go(chemin: Path) -> dict:
    """Comme `.claude/hooks/garde_calcul.py` : 8 colonnes, dates ISO ; doublon admis seulement en « extension »."""
    go = {}
    for n, ligne in enumerate(Path(chemin).read_text(encoding="utf-8").splitlines(), 1):
        if not LIGNE_GO.match(ligne):
            continue
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if len(c) != 8:
            raise Refus(f"registre des GO mal formé ligne {n} : 8 colonnes attendues, {len(c)} trouvées")
        ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
        try:
            a = date.fromisoformat(accorde)
            e = None if (echeance == "—" and typ != "calcul") else date.fromisoformat(echeance)
        except ValueError:
            raise Refus(f"registre des GO mal formé ligne {n} : dates illisibles") from None
        if ident in go:
            if perimetre.lower().startswith("extension") and typ == go[ident]["type"] and par == "Lazar":
                continue
            raise Refus(f"registre des GO : identifiant {ident} en double")
        go[ident] = {"accorde": a, "type": typ, "perimetre": perimetre, "plafond": plafond, "echeance": e, "par": par, "ref": ref}
    return go


def exiger_go_calcul(racine: Path, ident: str, aujourd_hui: date) -> dict:
    go = lire_go(Path(racine) / "registres" / "go.md")
    g = go.get(ident)
    if g is None:
        raise Refus(f"{ident} absent de registres/go.md")
    if g["type"] != "calcul":
        raise Refus(f"{ident} est un GO de type {g['type']!r}, pas « calcul »")
    if g["par"] != "Lazar":
        raise Refus(f"{ident} n'est pas accordé par Lazar")
    if not (g["accorde"] <= aujourd_hui <= g["echeance"]):
        raise Refus(f"{ident} hors de sa période de validité ({g['accorde']} → {g['echeance']})")
    rev = sorted(k for k, r in go.items() if r["type"] == "révocation" and (ident in r["perimetre"] or ident in r["ref"]))
    if rev:
        raise Refus(f"{ident} révoqué par {', '.join(rev)}")
    if not any(m in g["perimetre"] for m in IDEE):
        raise Refus(f"{ident} : périmètre sans « idée 1.1 » : ce GO ne couvre pas le jeu relancé de l'idée 1.1")
    m = PLAFOND.fullmatch(g["plafond"])
    if not m or not float(m.group(1)) > 0:
        raise Refus(f"{ident} : plafond {g['plafond']!r} illisible (« <nombre> USD » attendu, point décimal)")
    return {**g, "plafond_usd": float(m.group(1))}


def exiger_creation(racine: Path, feu: str, commit: str, maintenant: int, relances: int) -> dict:
    m = FEU.fullmatch(feu or "")
    if not m:
        raise Refus("feu écrit : forme courte « R-<N> GO-AAAA-MM-JJ-NN » exactement (leçon C4 : jamais la ligne R- entière)")
    r, ident = m.group(1), m.group(2)
    if not COMMIT.fullmatch(commit or ""):
        raise Refus("commit : 40 caractères hexadécimaux attendus")
    lignes = [l for l in (Path(racine) / "registres" / "decisions.md").read_text(encoding="utf-8").splitlines()
              if l.startswith(f"| R-{r} |")]
    if len(lignes) != 1:
        raise Refus(f"ligne R-{r} du feu : {len(lignes)} trouvée(s) dans registres/decisions.md, une attendue")
    manque = [x for x in (ident, commit, ETIQUETTE) if x not in lignes[0]]
    if manque:
        raise Refus(f"ligne R-{r} du feu : ne cite pas {manque}")
    if int(relances) not in (0, 1):
        raise Refus("une relance au plus (RELANCES 0 ou 1) ; au-delà : nœud de Lazar")
    jour = datetime.fromtimestamp(int(maintenant), tz=timezone.utc).date()
    g = exiger_go_calcul(racine, ident, jour)
    return {"feu": f"R-{r}", "go": ident, "plafond_usd": g["plafond_usd"], "echeance_go": str(g["echeance"]),
            "relances": int(relances)}


def exiger_prix_relu(prix) -> float:
    p = _nombre(prix)
    if p is None or not 0 < p <= PRIX_MAX_USD_H:
        raise Refus(f"prix relu {prix!r} USD/h hors de ]0 ; {PRIX_MAX_USD_H}] : détruire la machine aussitôt (par son identifiant)")
    return p


def garde_depense(racine: Path, ident: str, cumul, prix, maintenant: int) -> dict:
    c, p = _nombre(cumul), _nombre(prix)
    if c is None or p is None or c < 0 or p <= 0:
        raise Refus(f"cumul {cumul!r} ou prix {prix!r} illisible (point décimal) : arrêt et destruction par l'identifiant")
    g = exiger_go_calcul(racine, ident, datetime.fromtimestamp(int(maintenant), tz=timezone.utc).date())
    projete = c + 1.0 * p
    if projete >= g["plafond_usd"]:
        raise Refus(f"dépense : cumul {c:.3f} + une heure au prix relu = {projete:.3f} USD ≥ plafond {g['plafond_usd']:g} USD "
                    f"de {ident} : arrêt et destruction par l'identifiant (R10)")
    return {"cumul": c, "projete": round(projete, 4), "plafond": g["plafond_usd"]}


def exiger_identifiant(ident: str, dossier: Path) -> str:
    ident = str(ident)
    if not ENTIER.fullmatch(ident):
        raise Refus(f"identifiant {ident!r} illisible (destruction par l'identifiant seulement, R10)")
    if ident in INSTANCES_INTOUCHABLES:
        raise Refus(f"instance {ident} d'une autre tâche ou session : jamais détruite par cette procédure")
    try:
        lu = (Path(dossier) / "id-machine.txt").read_text(encoding="ascii").split()
    except (OSError, UnicodeDecodeError) as e:
        raise Refus(f"id-machine.txt illisible dans {dossier} ({type(e).__name__}) : l'identifiant se lit, il ne se tape pas") from None
    if lu != [ident]:
        raise Refus(f"identifiant {ident} ≠ celui de {dossier}/id-machine.txt (lu de l'inventaire) : refus")
    return ident


def exiger_absence(liste, ident: str, temoin: str) -> dict:
    ident, temoin = str(ident), str(temoin)
    if not ENTIER.fullmatch(ident) or not ENTIER.fullmatch(temoin) or temoin == ident:
        raise Refus("absence non prouvée : identifiant ou témoin illisible, ou égaux : arrêt")
    inst = liste.get("instances") if isinstance(liste, dict) else liste
    if not isinstance(inst, list) or any(not isinstance(i, dict) or "id" not in i for i in inst):
        raise Refus("absence non prouvée : liste des instances illisible (objets portant « id » attendus) : arrêt")
    ids = {str(i["id"]) for i in inst}
    if temoin not in ids:
        raise Refus(f"absence non prouvée : témoin {temoin} absent de la liste ({len(ids)} instance(s)) : arrêt")
    if ident in ids:
        raise Refus(f"absence non prouvée : instance {ident} toujours listée (témoin {temoin} présent) : destruction à refaire")
    return {"detruite": ident, "temoin": temoin, "instances_listees": len(ids)}


def _json(chemin: str):
    try:
        return json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Refus(f"{chemin} illisible ({type(e).__name__})") from None


def main(a: list[str]) -> int:
    import time
    try:
        if a[:1] == ["offre-depuis-recherche"] and len(a) == 3:
            o, journal = offre_depuis_recherche(_json(a[1]))
            exiger_offre(o, str(o["id"]))
            with open(a[2], "x", encoding="utf-8") as f:
                f.write(json.dumps(o, indent=1, ensure_ascii=False, sort_keys=True) + "\n")
            print("\n".join("JEU11 " + x for x in journal))
            print(f"JEU11 OFFRE ECRITE {a[2]} : offre {o['id']}, {o['num_gpus']} carte(s), {o['cpu_arch']} {o['cpu_name']!r}, "
                  f"{o['coeurs']:g} cœurs, {o['memoire_vive_mo']:g} Mo, prix garde {o['prix_garde_usd_h']:.4f} USD/h")
        elif a[:1] == ["offre"] and len(a) in (2, 3):
            exiger_offre(_json(a[1]), a[2] if len(a) == 3 else None)
            print("JEU11 OFFRE ACCEPTEE")
        elif a[:1] == ["creation"] and len(a) == 6:
            print(f"JEU11 CREATION PERMISE {exiger_creation(Path(a[1]), a[2], a[3], int(a[4]), int(a[5]))}")
        elif a[:1] == ["prix-relu"] and len(a) == 2:
            print(f"JEU11 PRIX RELU ACCEPTE {exiger_prix_relu(a[1]):g} USD/h")
        elif a[:1] == ["depense"] and len(a) == 5:
            print(f"JEU11 DEPENSE {garde_depense(Path(a[1]), a[2], a[3], a[4], int(time.time()))}")
        elif a[:1] == ["identifiant"] and len(a) == 3:
            print(f"JEU11 IDENTIFIANT {exiger_identifiant(a[1], Path(a[2]))}")
        elif a[:1] == ["absence"] and len(a) == 4:
            r = exiger_absence(_json(a[3]), a[1], a[2])
            print(f"JEU11 DESTRUCTION PROUVEE {r['detruite']} : absente de la liste, témoin {r['temoin']} présent, "
                  f"{r['instances_listees']} instance(s) listée(s)")
        else:
            print("JEU11 REFUS : commande inconnue (offre-depuis-recherche RECHERCHE OFFRE | offre OFFRE [ID] | creation RACINE FEU "
                  "COMMIT MAINTENANT RELANCES | prix-relu PRIX | depense RACINE GO CUMUL PRIX | identifiant ID DOSSIER | "
                  "absence ID TEMOIN LISTE)")
            return 2
    except (Refus, ValueError, OSError) as e:
        print(f"JEU11 REFUS : {e}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
