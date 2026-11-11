"""Création liée au devis et minuterie de destruction (A13, R10) — essai Lean, v2 (contre-lecture `2077ae26…`, R-2300).

- CLL-05 : à la destruction, la minuterie **réessaie sans fin**, avec une attente croissante (5 s, doublée, au plus 300 s), et
  journalise chaque échec ; elle ne sort que sur l'absence constatée du serveur, ou sur le refus de nom (un serveur d'un autre
  nom n'est jamais touché). Les lectures hors destruction gardent « toute erreur remonte ».
- CLL-06 : une seule commande `creer-et-veiller` : GO cité vérifié ; **refus d'une seconde machine sous le même GO** sans mot
  de Lazar (journal des créations et registre des dépenses) ; déjà-dépensé du GO lu dans `registres/depenses.md` (lignes à
  9 colonnes ; une ligne non standard exige une valeur déclarée, retenue si elle est plus haute) ; prix horaire **lu dans
  l'API** (type, lieu, adresse IPv4), converti au taux déclaré et consigné ; `verifier_devis` sur le reste du plafond du GO ;
  création ; identifiant et heure `created` de l'API au journal ; **minuterie dans le même processus**, sans intervalle ; une
  erreur entre la création et la minuterie détruit le serveur.
- CLL-13 : `detruire` (« détruire maintenant », par identifiant, avec retentatives) pour la fin de l'épreuve.
- CLL-14 : en ligne de commande, échéance plus longue que celle du pas refusée ; devis vérifié aussi au rattachement.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

from controle_ia.gardes import GardeArret

from . import garde_go_v1
from .hetzner_v1 import NOM_MACHINE, ErreurHetzner
from .minuterie_v1 import ECHEANCES_H, PLAFONDS_MACHINE, Machine, cout_cumule, decider, heures_entamees  # noqa: F401

RE_MONTANT = re.compile(r"-?\d[\d   ]*(?:,\d+)?")
RE_MACHINE_REGISTRE = re.compile(r"Hetzner\s+(\d{6,})")


def _ecrire(journal, entree: dict) -> None:
    if journal is not None:
        entree = {"heure": datetime.now(timezone.utc).isoformat(timespec="seconds"), **entree}
        journal.write(json.dumps(entree, ensure_ascii=False) + "\n")
        journal.flush()


def verifier_devis(prix_horaire_usd: float, pas: str, deja_depense_usd: float = 0.0) -> None:
    """Le type tient le reste du plafond machine du GO même allumé jusqu'à l'échéance du pas."""
    if pas not in ECHEANCES_H:
        raise GardeArret(f"pas inconnu {pas!r}")
    if prix_horaire_usd <= 0 or deja_depense_usd < 0:
        raise GardeArret("prix horaire positif et déjà-dépensé non négatif exigés")
    reste = PLAFONDS_MACHINE[pas] - deja_depense_usd
    if prix_horaire_usd * ECHEANCES_H[pas] > reste:
        raise GardeArret(f"{prix_horaire_usd:.4f} USD/h × {ECHEANCES_H[pas]} h > reste du plafond {reste:.2f} USD")


def lire_montant(cellule: str) -> float | None:
    m = RE_MONTANT.search(cellule)
    if not m:
        return None
    return float(re.sub(r"[   ]", "", m.group(0)).replace(",", "."))


def deja_depense_go(chemin_depenses: str | Path, go_id: str, declare: float | None = None) -> dict:
    total, non_standard = 0.0, []
    for ligne in Path(chemin_depenses).read_text(encoding="utf-8").splitlines():
        if not ligne.startswith("|"):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cellules) < 2 or cellules[1] != go_id:
            continue
        montant = lire_montant(cellules[6]) if len(cellules) == 9 else None
        if montant is None:
            non_standard.append(ligne[:120])
        else:
            total += montant
    if non_standard and declare is None:
        raise GardeArret(f"{len(non_standard)} ligne(s) non standard pour {go_id} dans le registre des dépenses : "
                         "déjà-dépensé à déclarer (--deja-depense-usd)")
    if declare is not None and declare < total:
        raise GardeArret(f"déjà-dépensé déclaré {declare:.2f} inférieur au registre ({total:.2f})")
    return {"registre": total, "lignes_non_standard": len(non_standard), "declare": declare,
            "retenu": total if declare is None else declare}


def machines_anterieures(chemin_depenses: str | Path, chemin_journal: str | Path, go_id: str) -> list[str]:
    vues = []
    for ligne in Path(chemin_depenses).read_text(encoding="utf-8").splitlines():
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")] if ligne.startswith("|") else []
        if len(cellules) > 1 and cellules[1] == go_id:
            vues += [f"registre : machine {x}" for x in RE_MACHINE_REGISTRE.findall(ligne)]
    j = Path(chemin_journal)
    if j.exists():
        for ligne in j.read_text(encoding="utf-8").splitlines():
            if ligne.strip():
                d = json.loads(ligne)
                if d.get("go") == go_id and d.get("creation"):
                    vues.append(f"journal : machine {d.get('identifiant')}")
    return vues


def detruire_par_identifiant(client, ident: int, nom: str, journal=None, dormir=time.sleep, pause_max_s: float = 300.0,
                             essais_max: int | None = None) -> dict:
    """Réessaie jusqu'à l'absence constatée ; seul le refus de nom (GardeArret) l'interrompt. `essais_max` ne sert qu'aux
    essais du harnais."""
    essai, pause = 0, 5.0
    while True:
        essai += 1
        try:
            etat = client.supprimer_serveur(ident, nom)
            if etat == "absent" or client.attendre_absence(ident):
                _ecrire(journal, {"destruction": "confirmée", "identifiant": ident, "essai": essai, "etat": etat})
                return {"detruit": True, "etat": etat, "essais": essai}
            raise ErreurHetzner("serveur encore présent après la demande de suppression")
        except (ErreurHetzner, OSError) as e:
            _ecrire(journal, {"destruction": "échec", "identifiant": ident, "essai": essai, "erreur": str(e)[:200]})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"destruction de {ident} non confirmée après {essai} essais (borne des essais seulement)") \
                    from None
            dormir(pause)
            pause = min(pause * 2, pause_max_s)


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
            if client.serveur(m.identifiant) is None:
                return {"detruit": False, "absent": True, "motif": "serveur absent (détruit par une autre commande)"}
        except ErreurHetzner as e:
            _ecrire(journal, {"identifiant": m.identifiant, "lecture": "échec", "erreur": str(e)[:200]})
        tours += 1
        if tours_max is not None and tours >= tours_max:
            return {"detruit": False, "motif": motif}
        dormir(pas_s)


def creer_et_veiller(client, *, go_id: str, chemin_go, chemin_depenses, journal_creations, type_serveur: str,
                     image: str, lieu: str, cles_ssh: list[int], pare_feux: list[int], taux_usd_eur: float,
                     pas: str = "D-1a", deja_declare: float | None = None, mot_de_lazar: str | None = None,
                     aujourdhui: date | None = None, go_attendu: str = garde_go_v1.GO_OUTILLAGE_D1A,
                     horloge=lambda: datetime.now(timezone.utc), dormir=time.sleep, pas_s: float = 60.0, journal=None,
                     tours_max: int | None = None, essais_max: int | None = None) -> dict:
    jour = aujourdhui or datetime.now(timezone.utc).date()
    garde_go_v1.autoriser_creation_machine(go_id, chemin_go, jour, attendu=go_attendu)
    anterieures = machines_anterieures(chemin_depenses, journal_creations, go_id)
    if anterieures and not mot_de_lazar:
        raise GardeArret(f"seconde machine sous {go_id} refusée sans mot de Lazar : {anterieures}")
    if not taux_usd_eur or taux_usd_eur <= 0:
        raise GardeArret("taux USD par EUR positif exigé (consigné)")
    deja = deja_depense_go(chemin_depenses, go_id, deja_declare)
    prix = client.prix_horaire_eur(type_serveur, lieu)
    prix_usd = prix["total"] * taux_usd_eur
    verifier_devis(prix_usd, pas, deja["retenu"])
    reponse = client.creer_serveur(go_id, chemin_go, jour, type_serveur, image, lieu, cles_ssh, pare_feux)
    serveur = reponse["server"]
    ident = serveur["id"]
    try:
        cree_a = datetime.fromisoformat(str(serveur["created"]).replace("Z", "+00:00"))
        entree = {"go": go_id, "creation": True, "identifiant": ident, "nom": serveur["name"], "type": type_serveur,
                  "lieu": lieu, "created": serveur["created"], "prix_eur_h": prix, "taux_usd_eur": taux_usd_eur,
                  "prix_usd_h": prix_usd, "deja_depense": deja, "mot_de_lazar": mot_de_lazar, "pas": pas}
        with open(journal_creations, "a", encoding="utf-8") as j:
            j.write(json.dumps(entree, ensure_ascii=False) + "\n")
        _ecrire(journal, entree)
        machine = Machine(ident, serveur["name"], cree_a, prix_usd, PLAFONDS_MACHINE[pas] - deja["retenu"],
                          ECHEANCES_H[pas])
    except Exception:
        detruire_par_identifiant(client, ident, NOM_MACHINE, journal, dormir, essais_max=essais_max)
        raise
    return veiller(machine, client, horloge, dormir, pas_s, journal, tours_max, essais_max)


def main(argv=None, client=None, dormir=time.sleep) -> int:
    from .hetzner_v2 import ClientHetzner2
    ap = argparse.ArgumentParser(description="Création liée au devis, minuterie et destruction par identifiant (A13), v2")
    sous = ap.add_subparsers(dest="action", required=True)
    c = sous.add_parser("creer-et-veiller")
    c.add_argument("--go", required=True)
    c.add_argument("--registre-go", required=True)
    c.add_argument("--depenses", required=True)
    c.add_argument("--journal-creations", required=True)
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
    d.add_argument("--identifiant", type=int, required=True)
    d.add_argument("--journal", required=True)
    a = ap.parse_args(argv)
    client = client or ClientHetzner2()
    with open(a.journal, "a", encoding="utf-8") as j:
        if a.action == "creer-et-veiller":
            res = creer_et_veiller(client, go_id=a.go, chemin_go=a.registre_go, chemin_depenses=a.depenses,
                                   journal_creations=a.journal_creations, type_serveur=a.type, image=a.image,
                                   lieu=a.lieu, cles_ssh=a.cle_ssh, pare_feux=a.pare_feu, taux_usd_eur=a.taux_usd_eur,
                                   pas=a.pas, deja_declare=a.deja_depense_usd, mot_de_lazar=a.mot_de_lazar, journal=j,
                                   dormir=dormir)
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
        else:
            res = detruire_par_identifiant(client, a.identifiant, NOM_MACHINE, j, dormir)
        j.write(json.dumps(res, ensure_ascii=False) + "\n")
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
