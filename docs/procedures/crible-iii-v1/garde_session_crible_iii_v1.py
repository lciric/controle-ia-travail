"""Gardes de la session qui lance le crible (iii) — v1 (dérivées de l'aide v3 de la session du pilote MR-2 et de la garde v1 de la
machine de l'idée 1.1, qui ne sont pas modifiées). Bibliothèque standard seule, `python3 -I -B`, aucun appel au loueur : les sorties
de l'outil du loueur sont écrites par `session_crible_iii_v1.sh` sous `umask 077` dans un dossier jetable, lues ici par programme,
puis supprimées ; aucune valeur de clé n'est jamais imprimée. Codes : 0 conforme ; 2 refus (motif sur la sortie standard) ; 3 (pour
`etiquette`) instance déjà absente.

Sous-commandes : offre-depuis-recherche RECHERCHE OFFRE ; offre OFFRE [ID] ; echeance MAINTENANT PRIX ; creation FICHIER [--supprimer] ;
relire LISTE ID ETIQUETTE [--supprimer] ; trouver LISTE ETIQUETTE [--supprimer] ; inventaire LISTE SORTIE [--supprimer] ;
ajoute AVANT APRES ID ; etiquette LISTE ID ETIQUETTE [--supprimer] ; absence REFERENCE LISTE ID [--supprimer] ; credit FICHIER
[--supprimer] ; cause TEXTE ; depense CUMUL PRIX ; go REGISTRE GO_CREDITS GO_HORS AUJOURD_HUI.
"""
import json
import math
import os
import re
import sys
from datetime import date

ICI = os.path.dirname(os.path.abspath(__file__))
ENTIER = re.compile(r"[1-9][0-9]*")
PRIX_OFFRE_MAX = 0.15      # offre : prix garde (prix total + stockage de 20 Go) au plus 0,15 USD/h (17 h : 2,55 USD)
PRIX_RELU_MAX = 0.17       # prix relu après création au plus 0,17 USD/h (17 h : 2,89 USD, sous la part machine de 3 USD)
DUREE_S = 61200            # échéance de la minuterie : 17 h après l'impression de la commande
PART_MACHINE = 3.0
DISQUE_GO = 20
HEURES_PAR_MOIS = 720.0
OFFRE_MIN = {"cpu_cores_effective": 4, "cpu_ram": 8000, "disk_space": 20, "inet_down": 100}
FIABILITE_MIN = 0.98
INTOUCHABLES = {58936096, 58936099, 58936100, 60480302, 60599797, 60670453, 60860420, 60918148, 60952525, 60953606}
CLES_RECHERCHE = ("id", "num_gpus", "cpu_arch", "cpu_cores_effective", "cpu_ram", "disk_space", "dph_total", "storage_cost",
                  "inet_down")


class Refus(Exception):
    pass


def entier(x, quoi="identifiant"):
    if isinstance(x, bool):
        raise Refus(f"{quoi} illisible")
    if isinstance(x, int) and x > 0:
        return x
    if isinstance(x, str) and ENTIER.fullmatch(x):
        return int(x)
    raise Refus(f"{quoi} illisible : entier ASCII attendu")


def nombre(x):
    if isinstance(x, bool) or not isinstance(x, (int, float, str)):
        return None
    try:
        v = float(x)
    except (ValueError, OverflowError):
        return None
    return v if math.isfinite(v) else None


def lire_prive(chemin, supprimer):
    try:
        texte = open(chemin, encoding="utf-8").read()
    except OSError as e:
        raise Refus(f"{os.path.basename(chemin)} illisible ({type(e).__name__})") from None
    finally:
        if supprimer:
            for p in (chemin, os.path.join(os.path.dirname(chemin), "erreur.txt")):
                try:
                    os.unlink(p)
                except OSError:
                    pass
            try:
                os.rmdir(os.path.dirname(chemin))
            except OSError:
                pass
    try:
        return json.loads(texte)
    except ValueError:
        raise Refus(f"{os.path.basename(chemin)} illisible (JSON attendu)") from None


def instances(doc):
    liste = doc.get("instances") if isinstance(doc, dict) else doc
    if not isinstance(liste, list) or any(not isinstance(i, dict) or "id" not in i for i in liste):
        raise Refus("liste des instances illisible")
    return [{"id": entier(i["id"], "identifiant listé"), "label": i.get("label"), "dph_total": i.get("dph_total"),
             "actual_status": i.get("actual_status")} for i in liste]


def fautes_offre(o):
    manque = [k for k in CLES_RECHERCHE if k not in o or (k == "cpu_arch" and not isinstance(o.get(k), str))
              or (k != "cpu_arch" and nombre(o.get(k)) is None)]
    fiab = [nombre(o.get(k)) for k in ("reliability2", "reliability") if k in o]
    fiab = [v for v in fiab if v is not None]
    if not fiab:
        manque.append("reliability2|reliability")
    if manque:
        return [f"clé(s) {manque} absente(s) ou illisible(s) : rien n'est deviné"]
    f = []
    if isinstance(o["num_gpus"], bool) or not isinstance(o["num_gpus"], int) or o["num_gpus"] < 0:
        f.append("num_gpus : entier ≥ 0 attendu (avec ou sans carte, la carte inutilisée)")
    if o["cpu_arch"] != "amd64":
        f.append(f"processeur {o['cpu_arch']!r} : amd64 exigé")
    for k, m in OFFRE_MIN.items():
        if nombre(o[k]) < m:
            f.append(f"{k} {o[k]!r} < {m}")
    if min(fiab) < FIABILITE_MIN:
        f.append(f"fiabilité {min(fiab)} < {FIABILITE_MIN}")
    if "rentable" in o and o["rentable"] is not True:
        f.append("offre non louable")
    st = nombre(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS
    p = nombre(o["dph_total"]) + st
    if not (nombre(o["dph_total"]) > 0 and p <= PRIX_OFFRE_MAX):
        f.append(f"prix garde {p:.4f} USD/h hors de ]0 ; {PRIX_OFFRE_MAX}]")
    return f


def offre_construite(o):
    st = nombre(o["storage_cost"]) * DISQUE_GO / HEURES_PAR_MOIS
    return {"id": int(o["id"]), "num_gpus": o["num_gpus"], "cpu_arch": o["cpu_arch"], "coeurs": nombre(o["cpu_cores_effective"]),
            "memoire_vive_mo": nombre(o["cpu_ram"]), "disque_go": nombre(o["disk_space"]), "debit_mbps": nombre(o["inet_down"]),
            "fiabilite": min(v for v in (nombre(o.get(k)) for k in ("reliability2", "reliability") if k in o) if v is not None),
            "prix_total_usd_h": nombre(o["dph_total"]), "stockage_usd_h": st, "prix_garde_usd_h": nombre(o["dph_total"]) + st,
            "reseau_usd_go": {"entree": o.get("inet_down_cost"), "sortie": o.get("inet_up_cost")}}


def c_offre_depuis_recherche(recherche, sortie):
    doc = lire_prive(recherche, False)
    liste = doc.get("offers") if isinstance(doc, dict) else doc
    if not isinstance(liste, list) or not liste:
        raise Refus("recherche illisible ou vide")
    acceptees = []
    for o in liste:
        if not isinstance(o, dict) or isinstance(o.get("id"), bool) or not ENTIER.fullmatch(str(o.get("id"))):
            print("CRIBLE offre illisible")
            continue
        f = fautes_offre(o)
        print(f"CRIBLE offre {o['id']} : " + ("acceptée" if not f else "refusée : " + " ; ".join(f)))
        if not f:
            acceptees.append(offre_construite(o))
    if not acceptees:
        raise Refus(f"aucune offre acceptée sur {len(liste)}")
    acceptees.sort(key=lambda x: (x["prix_garde_usd_h"], x["id"]))
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(acceptees[0], ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    o = acceptees[0]
    print(f"CRIBLE OFFRE ECRITE {sortie} : offre {o['id']}, {o['num_gpus']} carte(s) (inutilisée), {o['coeurs']:g} cœurs, "
          f"prix garde {o['prix_garde_usd_h']:.4f} USD/h ; réseau {o['reseau_usd_go']} USD/Go (consignés)")


def c_offre(chemin, ident=None):
    o = json.load(open(chemin, encoding="utf-8"))
    if ident is not None and str(o.get("id")) != str(ident):
        raise Refus("identifiant de l'offre décrite ≠ offre demandée")
    brute = {"id": o.get("id"), "num_gpus": o.get("num_gpus"), "cpu_arch": o.get("cpu_arch"), "cpu_cores_effective": o.get("coeurs"),
             "cpu_ram": o.get("memoire_vive_mo"), "disk_space": o.get("disque_go"), "dph_total": o.get("prix_total_usd_h"),
             "inet_down": o.get("debit_mbps"), "reliability": o.get("fiabilite"),
             "storage_cost": (nombre(o.get("stockage_usd_h")) or float("nan")) * HEURES_PAR_MOIS / DISQUE_GO}
    f = fautes_offre(brute)
    if f:
        raise Refus("offre hors des bornes : " + " ; ".join(f))
    print(f"offre {o['id']} conforme : {o['prix_garde_usd_h']:.4f} USD/h")


def c_echeance(maintenant, prix):
    t, p = entier(maintenant, "heure"), nombre(prix)
    if p is None or not 0 < p <= PRIX_OFFRE_MAX:
        raise Refus(f"prix {prix} hors de ]0 ; {PRIX_OFFRE_MAX}]")
    if not DUREE_S / 3600 * PRIX_RELU_MAX < PART_MACHINE:
        raise Refus("échéance : coût au plus au prix relu ≥ part machine")
    print(t + DUREE_S)


def c_creation(chemin, supprimer=""):
    doc = lire_prive(chemin, supprimer == "--supprimer")
    if not isinstance(doc, dict) or "new_contract" not in doc:
        raise Refus("création sans « new_contract » : ne rien deviner ; trouver l'instance par son étiquette")
    n = entier(doc["new_contract"], "new_contract")
    if n in INTOUCHABLES:
        raise Refus("identifiant d'une instance intouchable")
    print(n)


def c_relire(liste, ident, etiquette, supprimer=""):
    l = instances(lire_prive(liste, supprimer == "--supprimer"))
    n = entier(ident)
    vues = [i for i in l if i["id"] == n]
    if len(vues) != 1:
        raise Refus(f"instance {n} absente de la liste (ou en double)")
    i, p = vues[0], nombre(vues[0]["dph_total"])
    if i["label"] != etiquette or p is None or not 0 < p <= PRIX_RELU_MAX:
        raise Refus(f"instance {n} hors borne (étiquette {i['label']!r}, prix {i['dph_total']!r}) : la détruire aussitôt")
    print(f"instance {n} : étiquette juste, {p} USD/h, état {i['actual_status']!r}")


def c_trouver(liste, etiquette, supprimer=""):
    vues = [i["id"] for i in instances(lire_prive(liste, supprimer == "--supprimer")) if i["label"] == etiquette]
    if len(vues) != 1 or vues[0] in INTOUCHABLES:
        raise Refus(f"{len(vues)} instance(s) d'étiquette {etiquette} : une exactement attendue, non intouchable")
    print(vues[0])


def c_inventaire(liste, sortie, supprimer=""):
    ids = sorted(i["id"] for i in instances(lire_prive(liste, supprimer == "--supprimer")))
    if not ids:
        raise Refus("liste vide : liste mal lue (le compte porte d'autres instances)")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write("".join(f"{i}\n" for i in ids))
    print(f"{len(ids)} instance(s) listée(s)")


def c_ajoute(avant, apres, ident):
    a = {int(x) for x in open(avant, encoding="utf-8").read().split()}
    b = {int(x) for x in open(apres, encoding="utf-8").read().split()}
    if sorted(b - a) != [entier(ident)] or not a <= b:
        raise Refus("une seule instance ajoutée, égale à l'identifiant, toutes les autres toujours listées : attendu")
    print("seule instance ajoutée, égale à l'identifiant ; toutes les autres toujours listées")


def c_etiquette(liste, ident, etiquette, supprimer=""):
    l = instances(lire_prive(liste, supprimer == "--supprimer"))
    n = entier(ident)
    if n in INTOUCHABLES:
        raise Refus("instance intouchable : aucune destruction")
    vues = [i for i in l if i["id"] == n]
    if not vues:
        print(f"instance {n} absente de la liste : preuve d'absence à jouer (verifier-destruction)")
        return 3
    if len(vues) != 1 or vues[0]["label"] != etiquette:
        raise Refus(f"instance {n} en double ou d'une autre étiquette : aucune destruction, nœud")
    print(f"instance {n} présente, étiquette juste")
    return 0


def c_absence(avant, liste, ident, supprimer=""):
    ap = {i["id"] for i in instances(lire_prive(liste, supprimer == "--supprimer"))}
    n = entier(ident)
    av = {int(x) for x in open(avant, encoding="utf-8").read().split()}
    temoins = av - {n}
    if not temoins:
        raise Refus("aucun témoin : nœud, ou preuve par la console du loueur")
    if not temoins <= ap:
        raise Refus(f"{len(temoins - ap)} témoin(s) absent(s) : liste incomplète ; absence non prouvée")
    if n in ap:
        raise Refus(f"instance {n} toujours listée : destruction à refaire par ce seul identifiant")
    print(f"absente ; témoins toujours listés : {len(temoins)}")


def c_credit(chemin, supprimer=""):
    doc = lire_prive(chemin, supprimer == "--supprimer")
    c = doc.get("credit") if isinstance(doc, dict) else None
    if nombre(c) is None or nombre(c) < 5:
        raise Refus(f"crédit {c!r} illisible ou sous 5 USD : aucune création")
    print(f"crédit {c} USD (au moins 5)")


def c_cause(texte):
    if not re.fullmatch(r"[A-Za-z0-9 ,.:;()_-]{1,100}", texte):
        raise Refus("cause : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 100 caractères au plus")
    print("cause lisible par la machine")


def c_depense(cumul, prix):
    c, p = nombre(cumul), nombre(prix)
    if c is None or p is None or c < 0 or p <= 0:
        raise Refus("cumul ou prix illisible : arrêt et destruction par l'identifiant")
    if c + p >= PART_MACHINE:
        raise Refus(f"dépense : cumul {c:.3f} + une heure au prix relu ≥ part machine {PART_MACHINE} USD : arrêt et destruction")
    print(f"dépense machine : cumul {c:.3f} USD, une heure de plus {c + p:.3f} < {PART_MACHINE}")


def c_go(registre, go_credits, go_hors, aujourd_hui):
    sys.path.insert(0, ICI)
    import crible_iii_v1 as N
    try:
        g = N.lire_go_du_crible(open(registre, encoding="utf-8").read(), go_credits, go_hors, date.fromisoformat(aujourd_hui))
    except N.Refus as e:
        raise Refus(str(e)) from None
    print(f"lignes du crible lues : {g['credits']['ident']} ({g['credits']['plafond_usd']:g} USD), {g['hors']['ident']} "
          f"({g['hors']['plafond_usd']:g} USD)")


COMMANDES = {"offre-depuis-recherche": c_offre_depuis_recherche, "offre": c_offre, "echeance": c_echeance, "creation": c_creation,
             "relire": c_relire, "trouver": c_trouver, "inventaire": c_inventaire, "ajoute": c_ajoute, "etiquette": c_etiquette,
             "absence": c_absence, "credit": c_credit, "cause": c_cause, "depense": c_depense, "go": c_go}


def main(argv):
    if not argv or argv[0] not in COMMANDES:
        print("REFUS : sous-commande inconnue")
        return 2
    try:
        r = COMMANDES[argv[0]](*argv[1:])
    except Refus as e:
        print(f"REFUS : {e}")
        return 2
    except (TypeError, ValueError, OSError) as e:
        print(f"REFUS : arguments ou fichier ({type(e).__name__})")
        return 2
    return r or 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
