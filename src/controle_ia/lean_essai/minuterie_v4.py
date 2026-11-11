"""Création liée au devis, garde-fous de destruction hors du processus de la session (A13, R10) — essai Lean, v4.

Contre-lecture courte de la v3 (`b6ca886d…`, décision R-2307). La v3 reste telle quelle (R12). Corrections v4 :
- CLC3-07, garde-fous hors du processus de la session (aucun ne coûte) :
  (a) `detruire --pas d1a` : retrouve par les étiquettes fixes (`essai=lean,pas=d1a`) **et** par le nom `lean-outillage-d1a`,
      vérifie le nom, détruit chaque serveur par son identifiant (R10) ; sans jeton ni journal ;
  (b) **minuterie détachée** : `creer-et-armer` lance `veiller` dans un processus séparé (`setsid`), dont le PID est écrit dans
      un fichier versé ; `verifier-minuterie` le contrôle par son PID (R10) à chaque reprise ;
  (c) **ligne de procédure pour la mère**, rendue à la création : armer tout de suite une tâche programmée unique (`send_later`
      de la session mère) à l'échéance moins une heure, qui lance (a) et prévient Lazar ;
  (d) jeton de rattrapage, étiquettes, échéance et commandes écrits **avant l'appel de création** dans un fichier versé
      (`rattrapage-machine-d1a-<jeton>-v1.json`), que la mère committe à la création.
- CLC3-08 : sur une création incertaine, l'étiquette est cherchée à plusieurs reprises sur une fenêtre (10 min par défaut) ;
  tout serveur trouvé est détruit par identifiant, après contrôle du nom (note 4) ; rien trouvé ⇒ arrêt explicite « rattrapage
  par l'étiquette X à refaire », journal non soldé ; création refusée par l'API (4xx) ⇒ « aucune création », soldée (note 5).
- CLC3-09 : le journal s'écrit « au mieux » (`OSError` ⇒ sortie d'erreur) et ne tue jamais une boucle ; seule l'intention,
  écrite avant l'appel, est exigée (sinon aucune création).
- CLC3-10 : taux USD par EUR **fixé dans le code** au plus défavorable écrit (1,25 : rapport de l'outillage v1, réserve 7,
  `0706b12f…`) ; une déclaration ne peut que le relever ; type limité à la liste du devis (`hetzner_v4.TYPES_PERMIS`).
- CLC3-11 : échéance comptée depuis l'intention (k01) ; tous les serveurs d'une étiquette détruits (k02) ; période du mot de
  Lazar (k03) ; déclaré inférieur au registre (k11) ; échéance de la ligne de commande (k13) ; taux (k16).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
import time
import uuid
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from controle_ia.gardes import GardeArret

from . import garde_go_v1
from .hetzner_v1 import NOM_MACHINE
from .minuterie_v1 import ECHEANCES_H, PLAFONDS_MACHINE, Machine, cout_cumule, decider  # noqa: F401
from .minuterie_v2 import RE_MACHINE_REGISTRE, verifier_devis  # noqa: F401
from .minuterie_v3 import (DEPOT, DOSSIER_DECISIONS, REGISTRE_GO, _entrees_journal, deja_depense_registre,  # noqa: F401
                           lire_montant, verifier_mot_de_lazar)

DOSSIER_VERSE = DEPOT / "docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1"
JOURNAL_CREATIONS = DOSSIER_VERSE / "journal-creations-machines-v1.jsonl"
TAUX_USD_EUR_RETENU = 1.25
MARGE_TACHE_H = 1.0
FENETRE_RATTRAPAGE_S = 600.0
PAS_RATTRAPAGE_S = 30.0


def _ecrire(journal, entree: dict) -> None:
    """Au mieux (CLC3-09) : une écriture en échec part sur la sortie d'erreur et ne lève jamais."""
    if journal is None:
        return
    texte = json.dumps({"heure": datetime.now(timezone.utc).isoformat(timespec="seconds"), **entree}, ensure_ascii=False,
                       default=str)
    try:
        journal.write(texte + "\n")
        journal.flush()
    except OSError as e:
        try:
            sys.stderr.write(f"journal en échec ({type(e).__name__}) : {texte}\n")
        except OSError:
            pass


def _ajouter_journal_creations(chemin: Path, entree: dict, exige: bool = False) -> None:
    try:
        chemin.parent.mkdir(parents=True, exist_ok=True)
        with open(chemin, "a", encoding="utf-8") as j:
            j.write(json.dumps(entree, ensure_ascii=False, default=str) + "\n")
            j.flush()
    except OSError:
        if exige:
            raise
        sys.stderr.write(f"journal des créations en échec : {json.dumps(entree, default=str)}\n")


def taux_retenu(declare: float | None = None) -> float:
    if declare is not None and declare <= 0:
        raise GardeArret("taux USD par EUR déclaré non positif")
    return max(TAUX_USD_EUR_RETENU, declare or 0.0)


def cout_journal(chemin: Path, go_id: str, maintenant: datetime) -> float:
    machines: dict[str, dict] = {}
    for e in _entrees_journal(chemin):
        if e.get("go") != go_id or not e.get("etiquette"):
            continue
        m = machines.setdefault(e["etiquette"], {"debut": None, "fin": None, "prix": 0.0})
        if e.get("intention"):
            m["debut"] = datetime.fromisoformat(e["heure_intention"])
            m["prix"] = float(e["prix_usd_h"])
        if e.get("destruction_confirmee") or e.get("aucune_creation"):
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
                return {"detruit": True, "etat": etat, "essais": essai, "identifiant": ident}
            raise RuntimeError("serveur encore présent après la demande de suppression")
        except GardeArret as e:
            _ecrire(journal, {"destruction": "refusée", "identifiant": ident, "motif": str(e)[:200]})
            raise
        except Exception as e:  # noqa: BLE001 — journalisée au mieux, retentée ; seul le refus de nom arrête
            _ecrire(journal, {"destruction": "échec", "identifiant": ident, "essai": essai,
                              "erreur": f"{type(e).__name__}: {str(e)[:200]}"})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"destruction de {ident} non confirmée après {essai} essais (borne des essais seulement)") \
                    from None
            dormir(_pause(essai, pause_max_s))


def _lire_avec_retentatives(fonction, journal, dormir, essais_max, quoi: str):
    essai = 0
    while True:
        essai += 1
        try:
            return fonction()
        except GardeArret:
            raise
        except Exception as e:  # noqa: BLE001
            _ecrire(journal, {quoi: "échec", "erreur": type(e).__name__})
            if essais_max is not None and essai >= essais_max:
                raise GardeArret(f"{quoi} en échec après {essai} essais") from None
            dormir(_pause(essai, 300.0))


def _detruire_trouves(client, trouves: list[tuple[int, str]], journal, dormir, essais_max) -> list[dict]:
    """Tous les serveurs trouvés (k02), chacun après contrôle de son nom (note 4), par son identifiant."""
    autres = [(i, n) for i, n in trouves if n != NOM_MACHINE]
    if autres:
        _ecrire(journal, {"rattrapage": "refusé", "serveurs_d_un_autre_nom": autres})
        raise GardeArret(f"serveurs étiquetés d'un autre nom que {NOM_MACHINE!r} : {autres} ; aucun n'est touché")
    return [detruire_par_identifiant(client, i, n, journal, dormir, essais_max=essais_max) for i, n in trouves]


def rattraper_par_etiquette(client, jeton: str, journal=None, dormir=time.sleep, essais_max: int | None = None,
                            fenetre_s: float = FENETRE_RATTRAPAGE_S, pas_s: float = PAS_RATTRAPAGE_S) -> list[dict]:
    """CLC3-08 : recherches répétées sur une fenêtre ; tout serveur trouvé est détruit. Rien trouvé ⇒ arrêt explicite."""
    detruits: list[dict] = []
    ecoule = 0.0
    while True:
        trouves = _lire_avec_retentatives(lambda: client.chercher_par_etiquette(jeton), journal, dormir, essais_max,
                                          "recherche_etiquette")
        _ecrire(journal, {"recherche_etiquette": "faite", "etiquette": jeton, "trouves": trouves, "ecoule_s": ecoule})
        detruits += _detruire_trouves(client, trouves, journal, dormir, essais_max)
        if ecoule >= fenetre_s:
            break
        dormir(pas_s)
        ecoule += pas_s
    if not detruits:
        raise GardeArret(f"rien trouvé pendant {fenetre_s / 60:.0f} minutes : rattrapage par l'étiquette {jeton} à refaire "
                         "(`detruire --pas d1a` ou `detruire --etiquette`) ; journal non soldé")
    return detruits


def detruire_pas(client, pas: str = "d1a", journal=None, dormir=time.sleep, essais_max: int | None = None) -> dict:
    """CLC3-07 (a) : par les étiquettes fixes et par le nom, sans jeton ni journal."""
    par_etiquettes = _lire_avec_retentatives(lambda: client.chercher_par_etiquettes_fixes(pas), journal, dormir, essais_max,
                                             "recherche_etiquettes_fixes")
    par_nom = [(i, n) for i, n in _lire_avec_retentatives(client.inventaire, journal, dormir, essais_max, "inventaire")
               if n == NOM_MACHINE]
    trouves = sorted(set(par_etiquettes) | set(par_nom))
    detruits = _detruire_trouves(client, trouves, journal, dormir, essais_max)
    restants = [i for i, n in _lire_avec_retentatives(client.inventaire, journal, dormir, essais_max, "inventaire")
                if n == NOM_MACHINE]
    if restants:
        raise GardeArret(f"serveurs {restants} encore présents après destruction : relancer `detruire --pas {pas}`")
    return {"trouves": trouves, "detruits": detruits, "message": "aucun serveur de l'essai" if not trouves else ""}


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
        except Exception as e:  # noqa: BLE001
            _ecrire(journal, {"identifiant": m.identifiant, "lecture": "échec", "erreur": f"{type(e).__name__}"})
        tours += 1
        if tours_max is not None and tours >= tours_max:
            return {"detruit": False, "motif": motif}
        dormir(pas_s)


# ---- garde-fous hors du processus (CLC3-07) -----------------------------------------------------------------------------------

def ligne_procedure_mere(echeance: datetime, pas: str = "d1a") -> str:
    tache = echeance - timedelta(hours=MARGE_TACHE_H)
    return (f"PROCÉDURE MÈRE (CLC3-07 c) : armer tout de suite une tâche programmée unique (send_later de la session mère) "
            f"pour {tache.astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC (échéance "
            f"{echeance.astimezone(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC moins "
            f"{MARGE_TACHE_H:.0f} h), message : « Essai Lean D-1a, échéance de la machine {NOM_MACHINE} : lancer "
            f"`PYTHONPATH=src python -m controle_ia.lean_essai.minuterie_v4 detruire --pas {pas}`, vérifier l'absence, "
            f"inscrire l'arrêt et prévenir Lazar ». Puis committer le fichier de rattrapage.")


def ecrire_rattrapage(dossier: Path, entree: dict) -> Path:
    """CLC3-07 (d) : fichier neuf par création (R12), écrit avant l'appel ; la mère le committe à la création."""
    chemin = dossier / f"rattrapage-machine-{entree['pas']}-{entree['etiquette'][:12]}-v1.json"
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : jeton réutilisé")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(entree, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    return chemin


def lancer_minuterie_detachee(identifiant: int, pas: str, depuis: datetime, taux: float, deja: float, jeton: str,
                              dossier: Path, popen=subprocess.Popen) -> dict:
    """CLC3-07 (b) : `veiller` dans un processus séparé (`setsid`, sans terminal), PID écrit dans un fichier versé."""
    base = f"minuterie-{pas}-{jeton[:12]}"
    journal = dossier / f"{base}-journal-v1.jsonl"
    sortie = dossier / f"{base}-sortie-v1.log"
    argv = [sys.executable, "-B", "-m", "controle_ia.lean_essai.minuterie_v4", "veiller", "--identifiant", str(identifiant),
            "--pas", {"d1a": "D-1a"}.get(pas, pas), "--depuis", depuis.isoformat(),
            "--taux-usd-eur", str(taux), "--deja-depense-usd", str(deja), "--journal", str(journal)]
    env = dict(os.environ, PYTHONPATH=str(Path(__file__).resolve().parents[2]))
    with open(sortie, "ab") as s:
        p = popen(argv, stdin=subprocess.DEVNULL, stdout=s, stderr=s, start_new_session=True, env=env,
                  cwd=str(Path(__file__).resolve().parents[3]))
    fichier_pid = dossier / f"{base}-pid-v1.txt"
    fichier_pid.write_text(f"{p.pid} {identifiant} {jeton}\n", encoding="utf-8")
    return {"pid": p.pid, "fichier_pid": str(fichier_pid), "journal": str(journal), "argv": argv}


def verifier_minuterie(fichier_pid: Path, racine_proc: Path = Path("/proc")) -> dict:
    """Contrôle par le PID (R10) : le processus existe et sa ligne de commande est bien `minuterie_v4 veiller --identifiant N`."""
    pid, identifiant, _ = Path(fichier_pid).read_text(encoding="utf-8").split()
    chemin = racine_proc / pid / "cmdline"
    if not chemin.exists():
        return {"pid": int(pid), "vivante": False, "motif": "processus absent : relancer la minuterie ou detruire --pas"}
    arguments = chemin.read_bytes().split(b"\0")
    attendu = [b"controle_ia.lean_essai.minuterie_v4", b"veiller", identifiant.encode()]
    vivante = all(a in arguments for a in attendu)
    return {"pid": int(pid), "vivante": vivante,
            "motif": "" if vivante else "le PID désigne un autre processus : relancer la minuterie ou detruire --pas"}


def creer_et_armer(client, *, go_id: str, chemin_go, chemin_depenses, type_serveur: str, image: str, lieu: str,
                   cles_ssh: list[int], pare_feux: list[int], pas: str = "D-1a", taux_declare: float | None = None,
                   deja_declare: float | None = None, mot_de_lazar: str | None = None, aujourdhui: date | None = None,
                   journal_creations: Path = JOURNAL_CREATIONS, dossier_verse: Path = DOSSIER_VERSE,
                   dossier_decisions=DOSSIER_DECISIONS, horloge=lambda: datetime.now(timezone.utc), dormir=time.sleep,
                   journal=None, essais_max: int | None = None, jeton: str | None = None,
                   lancer=lancer_minuterie_detachee, fenetre_s: float = FENETRE_RATTRAPAGE_S) -> dict:
    from .hetzner_v4 import CreationRefusee, TYPES_PERMIS
    jour = aujourdhui or datetime.now(timezone.utc).date()
    if type_serveur not in TYPES_PERMIS:
        raise GardeArret(f"type {type_serveur!r} hors de la liste du devis {TYPES_PERMIS}")
    garde_go_v1.autoriser_creation_machine(go_id, chemin_go, jour)
    anterieures = machines_anterieures(chemin_depenses, journal_creations, go_id)
    mot = None
    if anterieures:
        if not mot_de_lazar:
            raise GardeArret(f"seconde machine sous {go_id} refusée sans mot de Lazar : {anterieures}")
        mot = verifier_mot_de_lazar(mot_de_lazar, chemin_go, dossier_decisions, jour)
    taux = taux_retenu(taux_declare)
    deja = deja_depense_go(chemin_depenses, go_id, journal_creations, deja_declare, horloge())
    prix = client.prix_horaire_eur(type_serveur, lieu)
    prix_usd = prix["total"] * taux
    verifier_devis(prix_usd, pas, deja["retenu"])
    jeton = jeton or uuid.uuid4().hex
    intention = horloge()
    echeance = intention + timedelta(hours=ECHEANCES_H[pas])
    pas_court = "d1a" if pas == "D-1a" else pas
    entree = {"go": go_id, "intention": True, "etiquette": jeton, "heure_intention": intention.isoformat(),
              "type": type_serveur, "lieu": lieu, "prix_eur_h": prix, "taux_usd_eur": taux, "prix_usd_h": prix_usd,
              "deja_depense": deja, "mot_de_lazar": mot, "pas": pas, "echeance": echeance.isoformat()}
    rattrapage = ecrire_rattrapage(dossier_verse, {
        "pas": pas_court, "go": go_id, "nom": NOM_MACHINE, "etiquette": jeton,
        "etiquettes_fixes": {"essai": "lean", "pas": pas_court}, "heure_intention": intention.isoformat(),
        "echeance": echeance.isoformat(), "commande_par_pas": f"minuterie_v4 detruire --pas {pas_court}",
        "commande_par_etiquette": f"minuterie_v4 detruire --etiquette {jeton}",
        "procedure_mere": ligne_procedure_mere(echeance, pas_court)})
    _ajouter_journal_creations(journal_creations, entree, exige=True)   # intention exigée AVANT l'appel
    _ecrire(journal, entree)
    try:
        reponse = client.creer_serveur_etiquete(go_id, chemin_go, jour, type_serveur, image, lieu, cles_ssh, pare_feux,
                                                jeton)
        serveur = reponse["server"]
        ident = int(serveur["id"])
        cree_a = datetime.fromisoformat(str(serveur["created"]).replace("Z", "+00:00"))
    except GardeArret:
        raise
    except CreationRefusee as e:
        _ajouter_journal_creations(journal_creations, {"go": go_id, "etiquette": jeton, "aucune_creation": True,
                                                       "heure": horloge().isoformat(), "motif": str(e)[:200]})
        raise GardeArret(f"création refusée par l'API, aucun serveur créé : {e}") from None
    except Exception as e:  # noqa: BLE001 — réponse perdue ou illisible
        _ecrire(journal, {"creation": "incertaine", "etiquette": jeton, "erreur": f"{type(e).__name__}"})
        detruits = rattraper_par_etiquette(client, jeton, journal, dormir, essais_max, fenetre_s=fenetre_s)
        for d in detruits:
            _ajouter_journal_creations(journal_creations, {"go": go_id, "etiquette": jeton, "destruction_confirmee": True,
                                                           "identifiant": d["identifiant"], "heure": horloge().isoformat()})
        raise GardeArret(f"création incertaine ({type(e).__name__}) : {len(detruits)} serveur(s) de l'étiquette "
                         "détruit(s) par identifiant") from None
    depuis = min(intention, cree_a)   # k01 : échéance comptée depuis l'intention, avant l'appel
    _ajouter_journal_creations(journal_creations, {"go": go_id, "creation": True, "etiquette": jeton, "identifiant": ident,
                                                   "created": serveur["created"], "depuis": depuis.isoformat()})
    try:
        minuterie = lancer(ident, pas_court, depuis, taux, deja["retenu"], jeton, dossier_verse)
    except Exception:
        detruire_par_identifiant(client, ident, NOM_MACHINE, journal, dormir, essais_max=essais_max)
        raise
    return {"identifiant": ident, "depuis": depuis.isoformat(), "echeance": (depuis + timedelta(hours=ECHEANCES_H[pas]))
            .isoformat(), "minuterie": minuterie, "rattrapage": str(rattrapage),
            "procedure_mere": ligne_procedure_mere(depuis + timedelta(hours=ECHEANCES_H[pas]), pas_court)}


def main(argv=None, client=None, dormir=time.sleep, horloge=lambda: datetime.now(timezone.utc)) -> int:
    from .hetzner_v4 import ClientHetzner4, verifier_coupure_nuage
    ap = argparse.ArgumentParser(description="Création liée au devis, garde-fous de destruction (A13), v4")
    sous = ap.add_subparsers(dest="action", required=True)
    c = sous.add_parser("creer-et-armer")
    c.add_argument("--go", required=True)
    c.add_argument("--type", required=True)
    c.add_argument("--image", default="ubuntu-24.04")
    c.add_argument("--lieu", required=True)
    c.add_argument("--cle-ssh", type=int, action="append", required=True)
    c.add_argument("--pare-feu", type=int, action="append", required=True)
    c.add_argument("--taux-usd-eur", type=float, help="ne peut que relever le taux fixé dans le code (1,25)")
    c.add_argument("--deja-depense-usd", type=float)
    c.add_argument("--mot-de-lazar")
    c.add_argument("--pas", choices=sorted(ECHEANCES_H), default="D-1a")
    c.add_argument("--journal", required=True)
    v = sous.add_parser("veiller")
    v.add_argument("--identifiant", type=int, required=True)
    v.add_argument("--pas", choices=sorted(ECHEANCES_H), default="D-1a")
    v.add_argument("--depuis", help="heure ISO de l'intention ; jamais plus tard que la création lue dans l'API")
    v.add_argument("--echeance-h", type=float, help="plus courte que celle du pas, jamais plus longue")
    v.add_argument("--taux-usd-eur", type=float)
    v.add_argument("--deja-depense-usd", type=float, default=0.0)
    v.add_argument("--journal", required=True)
    d = sous.add_parser("detruire")
    g = d.add_mutually_exclusive_group(required=True)
    g.add_argument("--identifiant", type=int)
    g.add_argument("--etiquette")
    g.add_argument("--pas", choices=["d1a"])
    d.add_argument("--journal")
    k = sous.add_parser("verifier-coupure")
    k.add_argument("--serveur", type=int, required=True)
    k.add_argument("--pare-feu", type=int, required=True)
    k.add_argument("--journal", required=True)
    w = sous.add_parser("verifier-minuterie")
    w.add_argument("--fichier-pid", required=True)
    a = ap.parse_args(argv)
    client = client or ClientHetzner4()
    if a.action == "verifier-minuterie":
        res = verifier_minuterie(Path(a.fichier_pid))
        print(json.dumps(res, ensure_ascii=False))
        return 0 if res["vivante"] else 1
    j = open(a.journal, "a", encoding="utf-8") if getattr(a, "journal", None) else None
    try:
        if a.action == "creer-et-armer":
            res = creer_et_armer(client, go_id=a.go, chemin_go=REGISTRE_GO, chemin_depenses=DEPOT / "registres/depenses.md",
                                 type_serveur=a.type, image=a.image, lieu=a.lieu, cles_ssh=a.cle_ssh, pare_feux=a.pare_feu,
                                 pas=a.pas, taux_declare=a.taux_usd_eur, deja_declare=a.deja_depense_usd,
                                 mot_de_lazar=a.mot_de_lazar, journal=j, dormir=dormir, horloge=horloge)
        elif a.action == "veiller":
            echeance = ECHEANCES_H[a.pas] if a.echeance_h is None else a.echeance_h
            if echeance > ECHEANCES_H[a.pas]:
                raise GardeArret("échéance plus longue que celle du pas")
            s = client.serveur(a.identifiant)
            if s is None:
                raise GardeArret(f"serveur {a.identifiant} absent")
            cree_a = datetime.fromisoformat(str(s["created"]).replace("Z", "+00:00"))
            depuis = cree_a if a.depuis is None else datetime.fromisoformat(a.depuis)
            if depuis > cree_a:
                raise GardeArret("--depuis plus tard que la création lue dans l'API")
            prix = client.prix_horaire_eur(s["server_type"]["name"], s["datacenter"]["location"]["name"])
            prix_usd = prix["total"] * taux_retenu(a.taux_usd_eur)
            verifier_devis(prix_usd, a.pas, a.deja_depense_usd)
            m = Machine(a.identifiant, s["name"], depuis, prix_usd, PLAFONDS_MACHINE[a.pas] - a.deja_depense_usd, echeance)
            res = veiller(m, client, horloge=horloge, dormir=dormir, journal=j)
        elif a.action == "detruire":
            if a.identifiant is not None:
                res = detruire_par_identifiant(client, a.identifiant, NOM_MACHINE, j, dormir)
            elif a.etiquette is not None:
                res = {"detruits": rattraper_par_etiquette(client, a.etiquette, j, dormir, fenetre_s=0.0)}
            else:
                res = detruire_pas(client, a.pas, j, dormir)
        else:
            res = verifier_coupure_nuage(client, a.pare_feu, a.serveur)
            _ecrire(j, {"verification_coupure": res})
        _ecrire(j, {"resultat": res})
    finally:
        if j is not None:
            j.close()
    print(json.dumps(res, ensure_ascii=False, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
