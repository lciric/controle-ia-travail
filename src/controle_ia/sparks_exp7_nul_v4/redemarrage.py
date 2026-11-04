"""Redémarrages de l'instance arrêtée, v4 (addendum n° 1, E-4 et E-5 ; contre-lecture du delta v2, points 21 à 23 ; du delta
v3, points 10 à 14 : branche des ordres hors `calcul/` et liée au commit, clé `instance`, `deja_usd` qui ne baisse jamais,
borne propre de la machine, consignation contrôlée).

Un redémarrage (`vastai start instance <id>`) relance l'amorce sur le même disque, avec l'environnement fixé à la création :
rien de neuf ne peut passer par l'environnement. La session écrit donc un **ordre** (`ordre-NNN.json`, numéros croissants)
sur la branche `ordres/sparks-exp7-nul-v4-<COMMIT[:12]>` du dépôt de travail (jamais sous `calcul/`, que seules les
instances écrivent ; liée au commit lancé), puis redémarre ; l'amorce le lit au commit de tête de cette branche :

    {"numero": 3, "instance": "59079406", "phase": "copie", "deja_usd": 7.42, "cas": ["vraie01", "hh04"], "premier": false,
     "copie_minutes": 25}
    {"numero": 17, "instance": "59079406", "phase": "causal", "deja_usd": 21.3}   (+ causal/cle-ouverte-v1.json, causal/reponses/…)
    {"numero": 18, "instance": "59079406", "phase": "fin", "deja_usd": 30.1}

- `instance` : identifiant de l'instance (chiffres), égal à `CONTAINER_ID`, sinon refus ;
- `deja_usd` : dépense déjà imputée, **relue à chaque démarrage** ; refusée si elle est plus basse que celle du dernier
  ordre exécuté ; la borne de durée prend le plus grand d'elle et de la **borne propre de la machine** (`borne_machine` :
  somme des plafonds des démarrages consignés sur le disque × prix de la carte + durée depuis la création × prix du
  stockage ; aucun modèle) ;
- un ordre déjà exécuté (numéro ≤ au dernier fait, consigné sur le disque) est refusé : rien ne part ;
- « copie » : les couches des modèles des cas nommés (identifiants internes, publics) sont liées en dur dans
  `lots/lot-NNN/` avec un manifeste d'empreintes ; le premier lot porte aussi les couches du départ et les rapports de
  fabrication ; le conteneur reste en vie au plus `copie_minutes` (5 à 60) pour la copie par la session, puis sort ;
- « causal » : contrôle causal (phase de la v2), sorties poussées et vérifiées, puis destruction par la minuterie ;
- « fin » : destruction par la minuterie, sans calcul.
Bibliothèque standard seule (lue par l'amorce avant toute installation).

    python3 -I -B redemarrage.py verifier ORDRES_DIR FAITS INSTANCE → PHASE= NUMERO= DEJA_USD= COPIE_MINUTES= ORDRE=
    python3 -I -B redemarrage.py borne DEMARRAGES CREATION_S PRIX_CARTE PRIX_STOCKAGE [MAINTENANT_S] → dollars
    python3 -I -B redemarrage.py demarrage DEMARRAGES MINUTES
    python3 -I -B redemarrage.py lot ORDRE SORTIE LOTS
    python3 -I -B redemarrage.py fait FAITS NUMERO DEJA_USD
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

PHASES = ("copie", "causal", "fin")
NOM_ORDRE = re.compile(r"^ordre-(\d{3})\.json$")
CAS = re.compile(r"^(vraie|hh|ss)\d{2}$|^ancre10[0-2]$|^pilote-(vraie|hh)$")
CLES = {"copie": {"numero", "instance", "phase", "deja_usd", "cas", "premier", "copie_minutes"},
        "causal": {"numero", "instance", "phase", "deja_usd"}, "fin": {"numero", "instance", "phase", "deja_usd"}}


class GardeOrdre(RuntimeError):
    pass


def _sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def lire_ordre(chemin: Path, instance: str | None = None) -> dict:
    m = NOM_ORDRE.match(Path(chemin).name)
    if not m:
        raise GardeOrdre(f"{chemin} : nom ordre-NNN.json attendu")
    try:
        o = json.loads(Path(chemin).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise GardeOrdre(f"ordre illisible : {e}") from None
    if not isinstance(o, dict) or o.get("phase") not in PHASES:
        raise GardeOrdre(f"phase {o.get('phase') if isinstance(o, dict) else o!r} : copie, causal ou fin")
    if set(o) != CLES[o["phase"]]:
        raise GardeOrdre(f"clés {sorted(set(o) ^ CLES[o['phase']])} manquantes ou en trop")
    n = o["numero"]
    if isinstance(n, bool) or not isinstance(n, int) or n != int(m.group(1)) or n < 1:
        raise GardeOrdre(f"numéro {n!r} ≠ nom du fichier")
    i = o["instance"]
    if not isinstance(i, str) or not i.isdigit():
        raise GardeOrdre(f"instance {i!r} : identifiant en chiffres attendu")
    if instance is not None and i != str(instance):
        raise GardeOrdre(f"ordre pour l'instance {i}, cette machine est {instance} : refus")
    d = o["deja_usd"]
    if isinstance(d, bool) or not isinstance(d, (int, float)) or not 0 <= d < 1000:
        raise GardeOrdre(f"deja_usd {d!r} : nombre positif attendu")
    if o["phase"] == "copie":
        cas = o["cas"]
        if not isinstance(cas, list) or not 1 <= len(cas) <= 4 or len(set(cas)) != len(cas) \
                or not all(isinstance(c, str) and CAS.match(c) for c in cas):
            raise GardeOrdre("cas : 1 à 4 identifiants internes distincts")
        if not isinstance(o["premier"], bool):
            raise GardeOrdre("premier : vrai ou faux")
        cm = o["copie_minutes"]
        if isinstance(cm, bool) or not isinstance(cm, int) or not 5 <= cm <= 60:
            raise GardeOrdre("copie_minutes : entier de 5 à 60")
    return o


def dernier_ordre(dossier: Path) -> Path:
    ordres = sorted(p for p in Path(dossier).iterdir() if NOM_ORDRE.match(p.name)) if Path(dossier).is_dir() else []
    if not ordres:
        raise GardeOrdre(f"aucun ordre dans {dossier}")
    return ordres[-1]


def faits(chemin: Path) -> list[tuple[int, float]]:
    """Ordres exécutés : lignes « numéro deja_usd »."""
    p = Path(chemin)
    if not p.exists():
        return []
    out = []
    for l in p.read_text(encoding="utf-8").splitlines():
        n, d = l.split()
        out.append((int(n), float(d)))
    return out


def exiger_nouveau(ordre: dict, chemin_faits: Path) -> None:
    f = faits(chemin_faits)
    if f and ordre["numero"] <= max(n for n, _ in f):
        raise GardeOrdre(f"ordre {ordre['numero']} déjà exécuté ou dépassé (dernier fait : {max(n for n, _ in f)}) : "
                         "rien ne part")
    if f and float(ordre["deja_usd"]) < max(d for _, d in f):
        raise GardeOrdre(f"deja_usd {ordre['deja_usd']} plus bas que celui d'un ordre exécuté "
                         f"({max(d for _, d in f)}) : rien ne part")


def marquer_fait(chemin_faits: Path, numero: int, deja_usd: float) -> None:
    with open(chemin_faits, "a", encoding="utf-8") as j:
        j.write(f"{int(numero)} {float(deja_usd)}\n")
        j.flush()
        os.fsync(j.fileno())


def marquer_demarrage(chemin: Path, minutes: int) -> None:
    """Consigne, avant le lancement, le plafond (minutes) d'un démarrage qui calcule ou copie."""
    if int(minutes) < 0:
        raise GardeOrdre("minutes négatives")
    with open(chemin, "a", encoding="utf-8") as j:
        j.write(f"{int(minutes)}\n")
        j.flush()
        os.fsync(j.fileno())


def borne_machine(chemin_demarrages: Path, creation_s: int, prix_carte: float, prix_stockage: float,
                  maintenant_s: int) -> float:
    """Borne propre de la machine (aucun modèle) : Σ plafonds consignés × prix de la carte + durée depuis la création ×
    prix du stockage."""
    p = Path(chemin_demarrages)
    minutes = sum(int(x) for x in p.read_text(encoding="utf-8").split()) if p.exists() else 0
    if prix_carte < 0 or prix_stockage < 0 or maintenant_s < creation_s:
        raise GardeOrdre("prix ou dates illisibles")
    return minutes / 60 * prix_carte + (maintenant_s - creation_s) / 3600 * prix_stockage


def modeles_du_cas(fab: dict, cas: str) -> list[str]:
    """Modèles finaux d'un cas interne (remplacement compris ; paires pilotes de l'étalonnage)."""
    if cas.startswith("pilote-"):
        t = cas.split("-", 1)[1]
        ids = sorted(mid for mid, r in fab["modeles"].items() if mid.startswith("etal-e1-") and r["final"])
        par = {mid.rsplit("-", 1)[1]: fab["modeles"][mid]["final"] for mid in ids}
        return [par["h1"], par["s1"]] if t == "vraie" else [par["h1"], par["h2"]]
    c = fab["cas"].get(cas)
    if c is None:
        raise GardeOrdre(f"cas {cas} absent du rapport de fabrication")
    mods = c["modeles"] if c["ok"] else c.get("modeles_remplacement")
    if not mods or not all(mods.values()):
        raise GardeOrdre(f"cas {cas} sans modèles dans les bornes")
    return sorted(mods.values())


def preparer_lot(ordre: dict, sortie: Path, lots: Path) -> Path:
    """Liens en dur des couches des modèles des cas de l'ordre dans `lots/lot-NNN/`, et manifeste d'empreintes."""
    if ordre["phase"] != "copie":
        raise GardeOrdre("lot : ordre de copie attendu")
    sortie = Path(sortie)
    fab = json.loads((sortie / "fabrication-v1.json").read_text(encoding="utf-8"))
    d = Path(lots) / f"lot-{ordre['numero']:03d}"
    if d.exists():
        raise GardeOrdre(f"{d} existe déjà (R12)")
    d.mkdir(parents=True)
    fichiers = []
    for cas in ordre["cas"]:
        for mid in modeles_du_cas(fab, cas):
            src = sortie / "modeles" / mid / "final" / "couches.safetensors"
            dst = d / "modeles" / mid / "final" / "couches.safetensors"
            dst.parent.mkdir(parents=True, exist_ok=True)
            os.link(src, dst)
            fichiers.append(dst)
    if ordre["premier"]:
        for nom in ("couches-depart-v1.safetensors", "fabrication-v1.json", "fabrication-complement-v2.json"):
            os.link(sortie / nom, d / nom)
            fichiers.append(d / nom)
    lignes = [f"{_sha(f)}  {f.relative_to(d)}" for f in sorted(fichiers)]
    (d / "MANIFESTE-LOT.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return d


def main(argv: list[str]) -> int:
    try:
        if argv[0] == "verifier":
            p = dernier_ordre(Path(argv[1]))
            o = lire_ordre(p, instance=argv[3])
            exiger_nouveau(o, Path(argv[2]))
            print(f"PHASE={o['phase']} NUMERO={o['numero']} DEJA_USD={float(o['deja_usd'])} "
                  f"COPIE_MINUTES={o.get('copie_minutes', 0)} ORDRE={p.name}")
        elif argv[0] == "lot":
            print(f"LOT {preparer_lot(lire_ordre(Path(argv[1])), Path(argv[2]), Path(argv[3]))}")
        elif argv[0] == "fait":
            marquer_fait(Path(argv[1]), int(argv[2]), float(argv[3]))
        elif argv[0] == "demarrage":
            marquer_demarrage(Path(argv[1]), int(argv[2]))
        elif argv[0] == "borne":
            import time
            now = int(argv[5]) if len(argv) > 5 else int(time.time())
            print(f"{borne_machine(Path(argv[1]), int(argv[2]), float(argv[3]), float(argv[4]), now):.4f}")
        else:
            raise IndexError
    except (GardeOrdre, IndexError, ValueError, OSError, KeyError) as err:
        print(f"ORDRE REFUSÉ : {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
