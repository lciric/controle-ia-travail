"""Création liée au devis et minuterie de destruction (A13, R10) — essai Lean, v3 (contre-lecture courte `1fea30ab…`).

- CLC2-03 : la boucle de destruction et la lecture de `veiller` attrapent **toute** exception sauf `GardeArret`, la
  journalisent et réessaient ; l'absence n'est conclue que sur deux lectures (`absence_confirmee`) ; le refus de nom est
  journalisé avant l'arrêt.
- CLC2-04 : **intention écrite au journal et minuterie armée avant l'appel de création** (échéance comptée depuis l'intention) ;
  étiquette unique `creation=<jeton>` sur le serveur ; si la réponse se perd (toute exception de l'appel ou de sa lecture), le
  serveur est cherché par son étiquette et détruit par son identifiant ; `detruire --etiquette` rattrape une session coupée.
- CLC2-06 : `verifier-coupure` lit le serveur et son pare-feu, écrit le relevé au journal.
- CLC2-07 : journal des créations à **chemin fixé dans le code** ; déjà-dépensé = le plus haut du registre des dépenses, de la
  valeur déclarée et de la somme « heures entamées × prix » des machines du journal ; mot de Lazar = identifiant d'une ligne de
  `registres/go.md` accordée par Lazar ou d'une décision de `docs/decisions/`, vérifié ; montants à point ou virgule décimale,
  montant négatif refusé.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
import uuid
from datetime import date, datetime, timezone
from pathlib import Path

from controle_ia.gardes import GardeArret

from . import garde_go_v1
from .hetzner_v1 import NOM_MACHINE
from .minuterie_v1 import ECHEANCES_H, PLAFONDS_MACHINE, Machine, cout_cumule, decider  # noqa: F401
from .minuterie_v2 import RE_MACHINE_REGISTRE, verifier_devis  # noqa: F401

DEPOT = Path("/home/user/controle-ia-travail")
JOURNAL_CREATIONS = DEPOT / "docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/journal-creations-machines-v1.jsonl"
REGISTRE_GO = DEPOT / "registres/go.md"
DOSSIER_DECISIONS = DEPOT / "docs/decisions"
RE_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")
RE_DECISION = re.compile(r"^N-\d{3}$")
RE_MONTANT = re.compile(r"-?\d(?:[\d   .,]*\d)?")


def _ecrire(journal, entree: dict) -> None:
    if journal is not None:
        entree = {"heure": datetime.now(timezone.utc).isoformat(timespec="seconds"), **entree}
        journal.write(json.dumps(entree, ensure_ascii=False) + "\n")
        journal.flush()


def _ajouter_journal_creations(chemin: Path, entree: dict) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with open(chemin, "a", encoding="utf-8") as j:
        j.write(json.dumps(entree, ensure_ascii=False) + "\n")
        j.flush()


def lire_montant(cellule: str) -> float | None:
    """Premier montant de la cellule : virgule ou point décimal ; montant négatif ⇒ arrêt ; plus d'un séparateur (« 1,234.5 »,
    « 1.234.5 », deux montants collés) ⇒ None (ligne non standard, valeur à déclarer)."""
    m = RE_MONTANT.search(cellule)
    if not m:
        return None
    brut = re.sub(r"[   ]", "", m.group(0))
    if brut.startswith("-"):
        raise GardeArret(f"montant négatif dans le registre des dépenses : {cellule.strip()[:60]!r}")
    if brut.count(",") + brut.count(".") > 1:
        return None
    return float(brut.replace(",", "."))


def deja_depense_registre(chemin_depenses, go_id: str) -> tuple[float, int]:
    total, non_standard = 0.0, 0
    for ligne in Path(chemin_depenses).read_text(encoding="utf-8").splitlines():
        if not ligne.startswith("|"):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) < 2 or cellules[1] != go_id:
            continue
        montant = lire_montant(cellules[6]) if len(cellules) == 9 else None
        if montant is None:
            non_standard += 1
        else:
            total += montant
    return total, non_standard


def _entrees_journal(chemin: Path) -> list[dict]:
    if not chemin.exists():
        return []
    return [json.loads(x) for x in chemin.read_text(encoding="utf-8").splitlines() if x.strip()]


def cout_journal(chemin: Path, go_id: str, maintenant: datetime) -> float:
    """Somme « heures entamées × prix » des machines du journal sous ce GO, de l'intention à la destruction (ou à maintenant)."""
    machines: dict[str, dict] = {}
    for e in _entrees_journal(chemin):
        if e.get("go") != go_id or not e.get("etiquette"):
            continue
        m = machines.setdefault(e["etiquette"], {"debut": None, "fin": None, "prix": 0.0})
        if e.get("intention"):
            m["debut"] = datetime.fromisoformat(e["heure_intention"])
            m["prix"] = float(e["prix_usd_h"])
        if e.get("destruction_confirmee"):
            m["fin"] = datetime.fromisoformat(e["heure"])
    total = 0.0
    for m in machines.values():
        if m["debut"] is None:
            continue
        fin = m["fin"] or maintenant
        total += max(1, math.ceil((fin - m["debut"]).total_seconds() / 3600.0)) * m["prix"]
    return total


def deja_depense_go(chemin_depenses, go_id: str, journal_creations: Path, declare: float | None,
                    maintenant: datetime) -> dict:
    registre, non_standard = deja_depense_registre(chemin_depenses, go_id)
    if non_standard and declare is None:
        raise GardeArret(f"{non_standard} ligne(s) non standard pour {go_id} : déjà-dépensé à déclarer")
    if declare is not None and declare < registre:
        raise GardeArret(f"déjà-dépensé déclaré {declare:.2f} inférieur au registre ({registre:.2f})")
    journal = cout_journal(journal_creations, go_id, maintenant)
    return {"registre": registre, "lignes_non_standard": non_standard, "declare": declare, "journal": journal,
            "retenu": max(registre, declare or 0.0, journal)}


def machines_anterieures(chemin_depenses, journal_creations: Path, go_id: str) -> list[str]:
    vues = []
    for ligne in Path(chemin_depenses).read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")] if ligne.startswith("|") else []
        if len(cellules) > 1 and cellules[1] == go_id:
            vues += [f"registre : machine {x}" for x in RE_MACHINE_REGISTRE.findall(ligne)]
    vues += [f"journal : intention {e.get('etiquette')}" for e in _entrees_journal(journal_creations)
             if e.get("go") == go_id and e.get("intention")]
    return vues


def verifier_mot_de_lazar(mot: str, chemin_go, dossier_decisions, aujourdhui: date) -> str:
    """Identifiant d'une ligne de `registres/go.md` accordée par Lazar (valide), ou d'une décision `N-xxx` de `docs/decisions/`."""
    if isinstance(mot, str) and RE_GO.match(mot):
        g = garde_go_v1.lire_registre_go(chemin_go).get(mot)
        if g is None or g["par"] != "Lazar":
            raise GardeArret(f"mot de Lazar {mot} : absent du registre des GO ou non accordé par Lazar")
        if g["echeance"] is not None and not (g["accorde"] <= aujourdhui <= g["echeance"]):
            raise GardeArret(f"mot de Lazar {mot} hors de sa période")
        return f"GO {mot} ({g['perimetre'][:80]})"
    if isinstance(mot, str) and RE_DECISION.match(mot):
        fichiers = [p.name for p in Path(dossier_decisions).glob("decision-*.md") if mot in p.name]
        if not fichiers:
            raise GardeArret(f"mot de Lazar {mot} : aucune décision de ce numéro dans {dossier_decisions}")
        return f"décision {mot} ({fichiers[0]})"
    raise GardeArret(f"mot de Lazar {mot!r} : identifiant GO-AAAA-MM-JJ-NN ou N-xxx exigé")


def _pause(n: int, pause_max_s: float) -> float:
    return min(5.0 * 2 ** (n - 1), pause_max_s)


def detruire_par_identifiant(client, ident: int, nom: str, journal=None, dormir=time.sleep, pause_max_s: float = 300.0,
                             essais_max: int | None = None) -> dict:
    essai = 0
    while True:
        essai += 1
        try:
            etat = client.supprimer_serveur(ident, nom)
            if client.absence_confirmee(ident):
                _ecrire(journal, {"destruction": "confirmée", "identifiant": ident, "essai": essai, "etat": etat})
                return {"detruit": True, "etat": etat, "essais": essai}
            raise RuntimeError("serveur encore présent après la demande de suppression")
        except GardeArret as e:
            _ecrire(journal, {"destruction": "refusée", "identifiant": ident, "motif": str(e)[:200]})
            raise
        except Exception as e:  # noqa: BLE001 — journalisée, retentée ; seul le refus de nom arrête
            _ecrire(journal, {"destruction": "échec", "identifiant": ident, "essai": essai,
                              "erreur": f"{type(e).__name__}: {str(e)[:200]}"})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"destruction de {ident} non confirmée après {essai} essais (borne des essais seulement)") \
                    from None
            dormir(_pause(essai, pause_max_s))


def veiller(m: Machine, client, horloge=lambda: datetime.now(timezone.utc), dormir=time.sleep, pas_s: float = 60.0,
            journal=None, tours_max: int | None = None, essais_max: int | None = None) -> dict:
    tours = 0
    while True:
        maintenant = horloge()
        detruire, motif = decider(m, maintenant)
        _ecrire(journal, {"identifiant": m.identifiant, "detruire": detruire, "motif": motif})
        if detruire:
            r = detruire_par_identifiant(client, m.identifiant, m.nom, journal, dormir, essais_max=essais_max)
            r.update({"motif": motif, "cout_cumule_usd": cout_cumule(m, maintenant)})
            return r
        try:
            if client.absence_confirmee(m.identifiant):
                _ecrire(journal, {"identifiant": m.identifiant, "absence": "confirmée par deux lectures"})
                return {"detruit": False, "absent": True, "motif": "serveur absent (détruit par une autre commande)"}
        except GardeArret:
            raise
        except Exception as e:  # noqa: BLE001 — la minuterie ne meurt pas d'une lecture
            _ecrire(journal, {"identifiant": m.identifiant, "lecture": "échec", "erreur": f"{type(e).__name__}: {e}"[:200]})
        tours += 1
        if tours_max is not None and tours >= tours_max:
            return {"detruit": False, "motif": motif}
        dormir(pas_s)


def rattraper_par_etiquette(client, jeton: str, journal=None, dormir=time.sleep, essais_max: int | None = None) -> list:
    """Cherche (avec retentatives) les serveurs de l'étiquette et les détruit chacun par son identifiant."""
    essai = 0
    while True:
        essai += 1
        try:
            trouves = client.chercher_par_etiquette(jeton)
            break
        except GardeArret:
            raise
        except Exception as e:  # noqa: BLE001
            _ecrire(journal, {"recherche_etiquette": "échec", "etiquette": jeton, "erreur": f"{type(e).__name__}"})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"recherche par étiquette {jeton} en échec après {essai} essais") from None
            dormir(_pause(essai, 300.0))
    _ecrire(journal, {"recherche_etiquette": "faite", "etiquette": jeton, "trouves": trouves})
    return [detruire_par_identifiant(client, i, n, journal, dormir, essais_max=essais_max) | {"identifiant": i}
            for i, n in trouves]


def creer_et_veiller(client, *, go_id: str, chemin_go, chemin_depenses, type_serveur: str, image: str, lieu: str,
                     cles_ssh: list[int], pare_feux: list[int], taux_usd_eur: float, pas: str = "D-1a",
                     deja_declare: float | None = None, mot_de_lazar: str | None = None, aujourdhui: date | None = None,
                     journal_creations: Path = JOURNAL_CREATIONS, dossier_decisions=DOSSIER_DECISIONS,
                     horloge=lambda: datetime.now(timezone.utc), dormir=time.sleep, pas_s: float = 60.0, journal=None,
                     tours_max: int | None = None, essais_max: int | None = None, jeton: str | None = None) -> dict:
    jour = aujourdhui or datetime.now(timezone.utc).date()
    garde_go_v1.autoriser_creation_machine(go_id, chemin_go, jour)
    anterieures = machines_anterieures(chemin_depenses, journal_creations, go_id)
    mot = None
    if anterieures:
        if not mot_de_lazar:
            raise GardeArret(f"seconde machine sous {go_id} refusée sans mot de Lazar : {anterieures}")
        mot = verifier_mot_de_lazar(mot_de_lazar, chemin_go, dossier_decisions, jour)
    if not taux_usd_eur or taux_usd_eur <= 0:
        raise GardeArret("taux USD par EUR positif exigé (consigné)")
    deja = deja_depense_go(chemin_depenses, go_id, journal_creations, deja_declare, horloge())
    prix = client.prix_horaire_eur(type_serveur, lieu)
    prix_usd = prix["total"] * taux_usd_eur
    verifier_devis(prix_usd, pas, deja["retenu"])
    jeton = jeton or uuid.uuid4().hex
    intention = horloge()
    entree = {"go": go_id, "intention": True, "etiquette": jeton, "heure_intention": intention.isoformat(),
              "type": type_serveur, "lieu": lieu, "prix_eur_h": prix, "taux_usd_eur": taux_usd_eur,
              "prix_usd_h": prix_usd, "deja_depense": deja, "mot_de_lazar": mot, "pas": pas,
              "echeance": (intention.timestamp() + ECHEANCES_H[pas] * 3600)}
    _ajouter_journal_creations(journal_creations, entree)   # intention écrite AVANT l'appel
    _ecrire(journal, entree)
    try:
        reponse = client.creer_serveur_etiquete(go_id, chemin_go, jour, type_serveur, image, lieu, cles_ssh, pare_feux,
                                                jeton)
        serveur = reponse["server"]
        ident = int(serveur["id"])
        cree_a = datetime.fromisoformat(str(serveur["created"]).replace("Z", "+00:00"))
        _ajouter_journal_creations(journal_creations, {"go": go_id, "creation": True, "etiquette": jeton,
                                                       "identifiant": ident, "created": serveur["created"]})
        # échéance armée à l'intention, avant l'appel : la plus prudente des deux heures
        machine = Machine(ident, serveur["name"], min(intention, cree_a), prix_usd,
                          PLAFONDS_MACHINE[pas] - deja["retenu"], ECHEANCES_H[pas])
    except GardeArret:
        raise
    except Exception as e:  # noqa: BLE001 — réponse perdue ou illisible : rattrapage par l'étiquette
        _ecrire(journal, {"creation": "incertaine", "etiquette": jeton, "erreur": f"{type(e).__name__}: {e}"[:200]})
        detruits = rattraper_par_etiquette(client, jeton, journal, dormir, essais_max)
        for d in detruits:
            _ajouter_journal_creations(journal_creations, {"go": go_id, "etiquette": jeton, "destruction_confirmee": True,
                                                           "identifiant": d["identifiant"],
                                                           "heure": horloge().isoformat()})
        raise GardeArret(f"création incertaine ({type(e).__name__}) : {len(detruits)} serveur(s) de l'étiquette "
                         "détruit(s) par identifiant") from None
    r = veiller(machine, client, horloge, dormir, pas_s, journal, tours_max, essais_max)
    if r.get("detruit") or r.get("absent"):
        _ajouter_journal_creations(journal_creations, {"go": go_id, "etiquette": jeton, "destruction_confirmee": True,
                                                       "identifiant": ident, "heure": horloge().isoformat()})
    return r


def main(argv=None, client=None, dormir=time.sleep) -> int:
    from .hetzner_v3 import ClientHetzner3, verifier_coupure_nuage
    ap = argparse.ArgumentParser(description="Création liée au devis, minuterie et destruction par identifiant (A13), v3")
    sous = ap.add_subparsers(dest="action", required=True)
    c = sous.add_parser("creer-et-veiller")
    c.add_argument("--go", required=True)
    c.add_argument("--type", required=True)
    c.add_argument("--image", default="ubuntu-24.04")
    c.add_argument("--lieu", required=True)
    c.add_argument("--cle-ssh", type=int, action="append", required=True)
    c.add_argument("--pare-feu", type=int, action="append", required=True)
    c.add_argument("--taux-usd-eur", type=float, required=True)
    c.add_argument("--deja-depense-usd", type=float)
    c.add_argument("--mot-de-lazar")
    c.add_argument("--pas", choices=sorted(ECHEANCES_H), default="D-1a")
    c.add_argument("--journal", required=True)
    v = sous.add_parser("veiller")
    v.add_argument("--identifiant", type=int, required=True)
    v.add_argument("--taux-usd-eur", type=float, required=True)
    v.add_argument("--pas", choices=sorted(ECHEANCES_H), default="D-1a")
    v.add_argument("--echeance-h", type=float, help="plus courte que celle du pas, jamais plus longue")
    v.add_argument("--deja-depense-usd", type=float, default=0.0)
    v.add_argument("--journal", required=True)
    d = sous.add_parser("detruire")
    g = d.add_mutually_exclusive_group(required=True)
    g.add_argument("--identifiant", type=int)
    g.add_argument("--etiquette")
    d.add_argument("--journal", required=True)
    k = sous.add_parser("verifier-coupure")
    k.add_argument("--serveur", type=int, required=True)
    k.add_argument("--pare-feu", type=int, required=True)
    k.add_argument("--journal", required=True)
    a = ap.parse_args(argv)
    client = client or ClientHetzner3()
    with open(a.journal, "a", encoding="utf-8") as j:
        if a.action == "creer-et-veiller":
            res = creer_et_veiller(client, go_id=a.go, chemin_go=REGISTRE_GO, chemin_depenses=DEPOT / "registres/depenses.md",
                                   type_serveur=a.type, image=a.image, lieu=a.lieu, cles_ssh=a.cle_ssh,
                                   pare_feux=a.pare_feu, taux_usd_eur=a.taux_usd_eur, pas=a.pas,
                                   deja_declare=a.deja_depense_usd, mot_de_lazar=a.mot_de_lazar, journal=j, dormir=dormir)
        elif a.action == "veiller":
            echeance = ECHEANCES_H[a.pas] if a.echeance_h is None else a.echeance_h
            if echeance > ECHEANCES_H[a.pas]:
                raise GardeArret("échéance plus longue que celle du pas")
            s = client.serveur(a.identifiant)
            if s is None:
                raise GardeArret(f"serveur {a.identifiant} absent")
            prix = client.prix_horaire_eur(s["server_type"]["name"], s["datacenter"]["location"]["name"])
            prix_usd = prix["total"] * a.taux_usd_eur
            verifier_devis(prix_usd, a.pas, a.deja_depense_usd)
            m = Machine(a.identifiant, s["name"], datetime.fromisoformat(str(s["created"]).replace("Z", "+00:00")),
                        prix_usd, PLAFONDS_MACHINE[a.pas] - a.deja_depense_usd, echeance)
            res = veiller(m, client, dormir=dormir, journal=j)
        elif a.action == "detruire":
            res = (detruire_par_identifiant(client, a.identifiant, NOM_MACHINE, j, dormir) if a.identifiant is not None
                   else {"detruits": rattraper_par_etiquette(client, a.etiquette, j, dormir)})
        else:
            res = verifier_coupure_nuage(client, a.pare_feu, a.serveur)
            _ecrire(j, {"verification_coupure": res})
        j.write(json.dumps(res, ensure_ascii=False, default=str) + "\n")
    print(json.dumps(res, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
