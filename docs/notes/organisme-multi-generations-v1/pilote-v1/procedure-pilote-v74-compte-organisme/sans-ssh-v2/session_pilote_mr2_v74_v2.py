"""Aide de la session qui lance le pilote MR-2 sans ssh — v2 (procédure v12 ; v2 : offre à 0,15 USD/h au plus et prix du réseau
imprimés, échéance à 17 h, contrôle de la seule étiquette pour la destruction (M1), témoin de repli pour la preuve d'absence (M2),
cause des feux bornée (M3), liste des intouchables à jour (m9)). Bibliothèque standard seule. Lit par programme les
sorties de l'outil du loueur (écrites sous `umask 077` dans un dossier jetable par session_pilote_mr2_v74_v2.sh, supprimées aussitôt
lues : la liste des instances porte la configuration des instances, clés comprises, depuis que les clés passent par `--env`) et ne
garde que les champs utiles ; jamais une valeur de clé n'est imprimée. Codes : 0 conforme ; 2 refus (motif sur la sortie standard).
"""
import json
import os
import re
import sys

ENTIER = re.compile(r"[1-9][0-9]*")
HEX64 = re.compile(r"[0-9a-f]{64}")
PRIX_MAX = 0.20                 # GO-2026-11-14-14 : machine à 0,20 USD/h au plus à la relecture (procédure v10, section 2)
PRIX_OFFRE_MAX = 0.15           # offre choisie à 0,15 USD/h au plus (M1 et m3 de la vérification de la v11)
DUREE_MAX_S = 61500             # 17 h 05 : refus de l'amorce v2 au-delà
DUREE_S = 61200                 # échéance : 17 h après l'impression
PART_MACHINE = 3.0
OFFRE_MIN = {"cpu_cores_effective": 4, "cpu_ram": 8000, "disk_space": 20}
INTOUCHABLES = {58936096, 58936099, 58936100, 60480302, 60599797, 60670453}   # liste de la mère (m9) ; toute instance non créée par la session aussi
MOTIF_JETON = re.compile(r"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_|AIza[0-9A-Za-z_-]{20,})")


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


def lire_prive(chemin, supprimer):
    """JSON d'un fichier privé de l'outil ; supprimé (et son dossier jetable) après lecture si demandé ; rien n'est affiché."""
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
             "actual_status": i.get("actual_status"), "num_gpus": i.get("num_gpus")} for i in liste]


def c_offre(recherche, ident, supprimer=""):
    """Offre choisie (identifiant) dans la sortie de `search offers --raw` : processeurs seuls, au moins 4 processeurs, 8 Go,
    20 Go de disque, prix total au plus 0,20 USD/h ; imprime le prix lu."""
    doc = lire_prive(recherche, supprimer == "--supprimer")
    n = entier(ident, "identifiant d'offre")
    liste = doc.get("offers") if isinstance(doc, dict) else doc
    if not isinstance(liste, list):
        raise Refus("recherche illisible (liste d'offres attendue)")
    vues = [o for o in liste if isinstance(o, dict) and o.get("id") == n]
    if len(vues) != 1:
        raise Refus(f"offre {n} absente de la recherche (ou en double)")
    o, fautes = vues[0], []
    if o.get("num_gpus") != 0:
        fautes.append(f"num_gpus {o.get('num_gpus')!r} ≠ 0 : processeurs seuls exigés")
    for k, m in OFFRE_MIN.items():
        v = o.get(k)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or v < m:
            fautes.append(f"{k} {v!r} < {m}")
    p = o.get("dph_total")
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not 0 < p <= PRIX_OFFRE_MAX:
        fautes.append(f"prix total {p!r} USD/h hors de ]0 ; {PRIX_OFFRE_MAX}]")
    if fautes:
        raise Refus("offre hors des bornes : " + " ; ".join(fautes))
    print(f"offre {n} conforme : {p} USD/h, {o['cpu_cores_effective']} processeurs, {o['cpu_ram']} Mo, {o['disk_space']} Go ; "
          f"réseau : entrée {o.get('inet_down_cost')!r}, sortie {o.get('inet_up_cost')!r} USD/Go (lus, consignés)")


def c_echeance(maintenant, prix):
    """Échéance de la minuterie : maintenant + 17 h (marge de 5 minutes sous la borne de l'amorce, pour le délai de création) ;
    coût au plus 17 h × prix (2,55 USD à 0,15 USD/h), sous la part machine de 3 USD."""
    t, p = entier(maintenant, "heure"), float(prix)
    if not 0 < p <= PRIX_OFFRE_MAX:
        raise Refus(f"prix {p} hors de ]0 ; {PRIX_OFFRE_MAX}]")
    e = t + DUREE_S
    cout = (e - t) / 3600 * p
    if not cout < PART_MACHINE:
        raise Refus(f"coût au plus {cout:.2f} USD ≥ part {PART_MACHINE}")
    print(e)
    print(f"échéance dans {(e - t) / 3600:.2f} h ; coût machine au plus {cout:.2f} USD (part {PART_MACHINE})", file=sys.stderr)


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
    i, fautes = vues[0], []
    if i["label"] != etiquette:
        fautes.append(f"étiquette {i['label']!r} ≠ {etiquette!r}")
    p = i["dph_total"]
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not 0 < p <= PRIX_MAX:
        fautes.append(f"prix {p!r} USD/h hors de ]0 ; {PRIX_MAX}]")
    if fautes:
        raise Refus(f"instance {n} hors borne ({' ; '.join(fautes)}) : la détruire aussitôt")
    print(f"instance {n} : étiquette juste, {p} USD/h, état {i['actual_status']!r}")


def c_etiquette(liste, ident, etiquette, supprimer=""):
    """Garde de la destruction (M1) : instance présente avec l'étiquette de la création ; le prix n'est jamais jugé ici. Rend 0 et
    « présente » ; 3 et « absente » si l'instance n'est plus listée (déjà détruite : preuve d'absence à jouer) ; 2 sinon."""
    l = instances(lire_prive(liste, supprimer == "--supprimer"))
    n = entier(ident)
    vues = [i for i in l if i["id"] == n]
    if not vues:
        print(f"instance {n} absente de la liste : déjà détruite ? preuve d'absence à jouer (verifier-destruction)")
        return 3
    if len(vues) != 1 or vues[0]["label"] != etiquette:
        raise Refus(f"instance {n} en double ou d'étiquette {vues[0]['label']!r} ≠ {etiquette!r} : aucune destruction, nœud")
    print(f"instance {n} présente, étiquette juste")
    return 0


def c_trouver(liste, etiquette, supprimer=""):
    vues = [i["id"] for i in instances(lire_prive(liste, supprimer == "--supprimer")) if i["label"] == etiquette]
    if len(vues) != 1:
        raise Refus(f"{len(vues)} instance(s) d'étiquette {etiquette} : une exactement attendue")
    if vues[0] in INTOUCHABLES:
        raise Refus("identifiant d'une instance intouchable")
    print(vues[0])


def c_inventaire(liste, sortie, supprimer=""):
    """Identifiants seuls (aucun autre champ) écrits dans SORTIE ; liste vide = liste mal lue (le compte en porte d'autres)."""
    ids = sorted(i["id"] for i in instances(lire_prive(liste, supprimer == "--supprimer")))
    if not ids:
        raise Refus("liste vide : liste mal lue (le compte porte d'autres instances)")
    with open(sortie, "x", encoding="utf-8") as f:
        f.write("".join(f"{i}\n" for i in ids))
    print(f"{len(ids)} instance(s) listée(s)")


def c_ajoute(avant, apres, ident):
    a = {int(x) for x in open(avant, encoding="utf-8").read().split()}
    b = {int(x) for x in open(apres, encoding="utf-8").read().split()}
    neufs = sorted(b - a)
    if neufs != [entier(ident)]:
        raise Refus(f"instances ajoutées {len(neufs)} : une seule attendue, égale à l'identifiant")
    if not a <= b:
        raise Refus("une instance listée avant ne l'est plus")
    print("seule instance ajoutée, égale à l'identifiant ; toutes les autres toujours listées")


def c_absence(avant, liste, ident, supprimer=""):
    """Destruction prouvée : identifiant absent de la liste relue sans erreur, et toute autre instance listée avant l'est encore."""
    n = entier(ident)
    av = {int(x) for x in open(avant, encoding="utf-8").read().split()}
    ap = {i["id"] for i in instances(lire_prive(liste, supprimer == "--supprimer"))}
    temoins = av - {n}
    if not temoins:
        raise Refus("aucun témoin (aucune autre instance listée avant) : nœud, ou preuve par la console du loueur")
    if n not in av:
        print(f"note : l'instance {n} n'était pas dans la liste de référence (relevée après sa destruction) ; "
              "ids-apres-creation.txt atteste qu'elle avait été listée")
    if not temoins <= ap:
        raise Refus(f"{len(temoins - ap)} témoin(s) absent(s) : liste incomplète ; absence non prouvée")
    if n in ap:
        raise Refus(f"instance {n} toujours listée : destruction non faite ; recommencer par ce seul identifiant")
    print(f"absente ; témoins toujours listés : {len(temoins)}")


def c_credit(chemin, supprimer=""):
    doc = lire_prive(chemin, supprimer == "--supprimer")
    c = doc.get("credit") if isinstance(doc, dict) else None
    if isinstance(c, bool) or not isinstance(c, (int, float)):
        raise Refus("crédit illisible")
    if c < 5:
        raise Refus(f"crédit {c} < 5 USD : aucune création")
    print(f"crédit {c} USD (au moins 5)")


def c_cause(texte):
    """Cause d'un feu (M3) : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 1 à 100 caractères ; sinon refus,
    rien n'est poussé."""
    if not re.fullmatch(r"[A-Za-z0-9 ,.:;()_-]{1,100}", texte):
        raise Refus("cause : lettres sans accent, chiffres, espaces et « , . : ; ( ) _ - », 100 caractères au plus")
    print("cause lisible par la machine")


def c_jetons(chemin):
    """Compte des motifs de clé dans un fichier (jamais la valeur) : 0 attendu."""
    n = len(MOTIF_JETON.findall(open(chemin, encoding="utf-8", errors="replace").read()))
    if n:
        raise Refus(f"{n} motif(s) de clé dans {os.path.basename(chemin)} : ne pas le verser")
    print("aucun motif de clé")


COMMANDES = {"offre": c_offre, "echeance": c_echeance, "creation": c_creation, "relire": c_relire, "trouver": c_trouver,
             "inventaire": c_inventaire, "ajoute": c_ajoute, "absence": c_absence, "credit": c_credit, "jetons": c_jetons,
             "etiquette": c_etiquette, "cause": c_cause}


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
