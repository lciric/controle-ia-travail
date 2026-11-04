"""Vérification d'un GO de calcul dans `registres/go.md`, par l'amorce, avant toute création d'instance — version 3 :
règle d'extension alignée sur la garde de calcul de `main` (`.claude/hooks/garde_calcul.py`, R-389 ; contre-lecture R2
du brouillon 2, I3). Bibliothèque standard seulement : l'amorce l'appelle avant toute installation. La lecture des
lignes (8 colonnes) est celle de la v2 (`pilote_exposant_p_v2.go.lire`), importée telle quelle.

Règles :
1. la **première** ligne de l'identifiant cité fixe seule le type (« calcul »), l'auteur (Lazar) et la période
   (accordé le → échéance ; date du jour dedans) ;
2. chaque autre ligne de **cet** identifiant doit être une extension conforme à R-389, comme la garde de `main` la
   juge : périmètre qui commence par « extension », même type, accordée par Lazar, ni antérieure à la première ligne,
   ni d'échéance plus lointaine ; sinon, refus (« ligne en conflit ») ;
3. plafond : celui de la dernière extension conforme, accordée au plus tard le jour de la vérification, dont la colonne
   « plafond » donne un montant lisible en USD ; à défaut, celui de la première ligne. Une extension au plafond
   illisible ne change rien, elle est consignée ; une extension datée après le jour de la vérification n'est pas
   encore en vigueur, elle est consignée. Le plafond retenu doit couvrir le pire cas du devis ;
4. périmètre : « exposant p » nommé par la première ligne ; une extension qui le nommerait seule ne suffit pas ;
5. révocation : inchangée (aucune ligne de type « révocation » ne cite l'identifiant, en périmètre ou en référence) ;
6. doublons d'**autres** identifiants : rapportés, jamais bloquants ; un doublon non conforme ailleurs, une ligne
   illisible ou une date illisible (ce que la garde de `main` bloque aussi) est signalé en clair : « la garde de calcul de `main` bloquerait la création ».

    python -I -B -m controle_ia.pilote_exposant_p_v3.go --registre F --go-id GO-AAAA-MM-JJ-NN --montant 17 [--date D]
Sortie : une ligne JSON ; code 0 si le GO vaut, 1 sinon (motif dans la ligne).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

from ..pilote_exposant_p_v2.go import ETUDE, FORMAT_ID, MONTANT, GoInvalide, lire

GARDE_MAIN = "la garde de calcul de `main` bloquerait la création"


def _date(texte: str, typ: str) -> date | None:
    """Date d'une cellule ; « — » (sans échéance) n'est admis que pour un GO qui n'est pas de calcul, comme dans la
    garde de `main`. Lève ValueError sinon."""
    if texte == "—" and typ != "calcul":
        return None
    return date.fromisoformat(texte)


def montant(cellule: str) -> float | None:
    m = MONTANT.search(cellule)
    return float(m.group(1).replace(",", ".")) if m else None


def extension_conforme(premiere: dict, ligne: dict) -> tuple[bool, str]:
    """R-389, telle que la garde de `main` l'applique (`lire_go`) : rend (conforme, motif du refus)."""
    try:
        a0, e0 = _date(premiere["accorde"], premiere["type"]), _date(premiere["echeance"], premiere["type"])
        a, e = _date(ligne["accorde"], ligne["type"]), _date(ligne["echeance"], ligne["type"])
    except ValueError:
        return False, "dates illisibles"
    if not ligne["perimetre"].lower().startswith("extension"):
        return False, "périmètre qui ne commence pas par « extension »"
    if ligne["type"] != premiere["type"]:
        return False, f"type « {ligne['type']} » ≠ « {premiere['type']} » de la première ligne"
    if ligne["par"] != "Lazar":
        return False, "extension non accordée par Lazar"
    if a < a0:
        return False, f"extension antérieure à la première ligne ({a} < {a0})"
    if not ((e0 is None and e is None) or (e0 is not None and e is not None and e <= e0)):
        return False, f"échéance {ligne['echeance']} plus lointaine que celle de la première ligne ({premiere['echeance']})"
    return True, ""


def classer_doublons(lignes: list[dict]) -> dict[str, dict]:
    """Pour chaque identifiant répété : lignes, et extensions non conformes (avec motif)."""
    par_id: dict[str, list[dict]] = {}
    for x in lignes:
        par_id.setdefault(x["id"], []).append(x)
    r = {}
    for i, xs in par_id.items():
        if len(xs) > 1:
            conflits = [(x["n"], m) for x in xs[1:] for ok, m in [extension_conforme(xs[0], x)] if not ok]
            r[i] = {"lignes": [x["n"] for x in xs], "conflits": conflits}
    return r


def verifier(texte: str, go_id: str, montant_min: float, aujourd_hui: date, etude: str = ETUDE) -> dict:
    if not FORMAT_ID.match(go_id or ""):
        raise GoInvalide(f"identifiant de GO {go_id!r} illisible (GO-AAAA-MM-JJ-NN)")
    lignes, problemes = lire(texte)
    trouvees = [x for x in lignes if x["id"] == go_id]
    if not trouvees:
        raise GoInvalide(f"{go_id} absent du registre" + (f" (lignes illisibles : {problemes})" if problemes else ""))
    g, extensions = trouvees[0], trouvees[1:]
    if g["type"] != "calcul":
        raise GoInvalide(f"{go_id} est de type « {g['type']} », pas « calcul »")
    if g["par"] != "Lazar":
        raise GoInvalide(f"{go_id} n'est pas accordé par Lazar")
    try:
        a, e = date.fromisoformat(g["accorde"]), date.fromisoformat(g["echeance"])
    except ValueError:
        raise GoInvalide(f"{go_id} : dates illisibles") from None
    for x in extensions:
        ok, motif = extension_conforme(g, x)
        if not ok:
            raise GoInvalide(f"{go_id} : ligne en conflit (ligne {x['n']} : {motif} ; R-389) — {GARDE_MAIN}")
    if not a <= aujourd_hui <= e:
        raise GoInvalide(f"{go_id} hors de sa période de validité ({a} → {e} ; aujourd'hui {aujourd_hui})")
    rev = [x["id"] for x in lignes if x["type"] == "révocation" and (go_id in x["perimetre"] or go_id in x["ref"])]
    if rev:
        raise GoInvalide(f"{go_id} révoqué par {', '.join(rev)}")
    consignes, plafond, source = [], montant(g["plafond"]), g["n"]
    for x in extensions:
        m = montant(x["plafond"])
        if date.fromisoformat(x["accorde"]) > aujourd_hui:
            consignes.append(f"extension ligne {x['n']} datée du {x['accorde']}, pas encore en vigueur : ignorée")
        elif m is None:
            consignes.append(f"extension ligne {x['n']} : plafond « {x['plafond']} » illisible, ne change rien")
        else:
            plafond, source = m, x["n"]
    if plafond is None:
        raise GoInvalide(f"{go_id} : plafond « {g['plafond']} » sans montant lisible en USD")
    if plafond < montant_min:
        raise GoInvalide(f"{go_id} : plafond {plafond} USD (ligne {source}) < pire cas du devis {montant_min} USD")
    if etude.lower() not in g["perimetre"].lower():
        raise GoInvalide(f"{go_id} : le périmètre de la première ligne ne nomme pas l'étude « {etude} »")
    autres = {i: d for i, d in classer_doublons(lignes).items() if i != go_id}
    non_conformes = {i: d for i, d in autres.items() if d["conflits"]}
    avert = []
    if autres:
        avert.append(f"identifiants répétés ailleurs dans le registre : {sorted(autres)}")
    if non_conformes:
        avert.append(f"doublons non conformes à R-389 : {sorted(non_conformes)} — {GARDE_MAIN}")
    dates_illisibles = []
    for x in lignes:
        try:
            _date(x["accorde"], x["type"]), _date(x["echeance"], x["type"])
        except ValueError:
            dates_illisibles.append(x["n"])
    if problemes:
        avert.append(f"lignes illisibles : {problemes} — {GARDE_MAIN}")
    if dates_illisibles:
        avert.append(f"dates illisibles aux lignes {dates_illisibles} — {GARDE_MAIN}")
    return {"go_id": go_id, "valide": True, "plafond_usd": plafond, "ligne_plafond": source,
            "pire_cas_devis_usd": montant_min, "periode": [str(a), str(e)], "aujourd_hui": str(aujourd_hui),
            "ligne": g["n"], "extensions": [x["n"] for x in extensions], "consignes": consignes,
            "avertissements": avert}


def principal(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registre", required=True)
    ap.add_argument("--go-id", required=True)
    ap.add_argument("--montant", type=float, required=True, help="pire cas du devis, USD")
    ap.add_argument("--date", default=None, help="AAAA-MM-JJ (défaut : date UTC du jour)")
    ap.add_argument("--etude", default=ETUDE)
    a = ap.parse_args(argv)
    jour = date.fromisoformat(a.date) if a.date else datetime.now(timezone.utc).date()
    try:
        texte = Path(a.registre).read_text(encoding="utf-8")
        r = verifier(texte, a.go_id, a.montant, jour, a.etude)
    except (GoInvalide, OSError) as e:
        print(json.dumps({"go_id": a.go_id, "valide": False, "motif": str(e)}, ensure_ascii=False))
        return 1
    print(json.dumps(r, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
