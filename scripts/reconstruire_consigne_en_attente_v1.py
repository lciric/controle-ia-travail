"""Reconstruit par programme la consigne en attente du juge externe différé d'une course de l'organisme d'idéation
sur les organismes discrets, à partir des copies scellées du dépôt, et ne l'écrit que si son empreinte est celle du
manifeste de fin de la course. Ne montre aucun contenu de fiche (cloisonnement) : n'affiche que des empreintes.

Entrées, toutes vérifiées par empreinte avant emploi : fiches validées, témoins servis, clés d'anonymisation par juge,
manifestes de départ et de fin (copies scellées de la course) ; question et pièces du juge (empreintes du manifeste de
départ) ; orchestrateur public `lciric/ideation-organism`, arbre de `orchestrator/` épinglé comme dans les lanceurs.

Ordre des champs : les copies scellées sont écrites triées (`sort_keys=True`) alors que la consigne sert les fiches dans
l'ordre canonique de `valider_fiche_ideation` ; cet ordre, fixé par le code de l'orchestrateur, est rétabli ici, et
l'empreinte interne de chaque fiche est revérifiée.

Usage : python3 -I -B scripts/reconstruire_consigne_en_attente_v1.py DOSSIER_DU_RUN [--ecrire]
Codes : 0 empreinte retrouvée ; 3 empreinte différente (rien écrit) ; 2 entrée refusée.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

DEPOT = Path(__file__).resolve().parents[1]
ORCHESTRATEUR = Path("/home/user/lciric/ideation-organism/orchestrator")
ARBRE_ORCHESTRATEUR = "ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70"
NOTES = DEPOT / "docs/notes/organismes-discrets-v1/organisme-ideation-v1"


ORDRE_FICHE = ("nom", "type", "enonce", "loi_predictive", "perte_traduction", "questions_servies", "avantage",
               "originalite", "demande_organisme", "cout", "piege", "cosmetique_si", "anteriorite")
ORDRE_SOUS = {"loi_predictive": ("espace_instances", "prediction", "signe", "metrique"),
              "avantage": ("source", "texte", "incopiable_parce_que"), "originalite": ("niveau", "texte"),
              "demande_organisme": ("nature", "texte"), "cout": ("nature", "ordre_de_grandeur")}
ORDRE_ANTERIORITE = ("reference", "statut", "non_opposable")


def ordonner(d: dict, ordre) -> dict:
    hors = [k for k in d if k not in ordre]
    if hors:
        raise Refus(f"champs hors de l'ordre canonique : {hors}")
    return {k: d[k] for k in ordre if k in d}


def ordre_canonique(fiche: dict, internes) -> dict:
    """La fiche dans l'ordre de `valider_fiche_ideation` ; les champs internes suivent (retirés par `vue_servie`)."""
    servis = {k: v for k, v in fiche.items() if k not in internes}
    f = ordonner(servis, ORDRE_FICHE)
    for k, ordre in ORDRE_SOUS.items():
        f[k] = ordonner(f[k], ordre)
    f["anteriorite"] = [ordonner(a, ORDRE_ANTERIORITE) for a in f["anteriorite"]]
    f.update({k: v for k, v in fiche.items() if k in internes})
    return f


class Refus(Exception):
    pass


def sha(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def lire_scelle(chemin: Path) -> bytes:
    octets = chemin.read_bytes()
    compagnon = Path(str(chemin) + ".sha256")
    if not compagnon.exists() or compagnon.read_text(encoding="utf-8").split()[0] != sha(octets):
        raise Refus(f"sceau absent ou faux : {chemin}")
    return octets


def reconstruire(run: Path, ecrire: bool) -> int:
    arbre = subprocess.run(["git", "-C", str(ORCHESTRATEUR.parent), "rev-parse", "HEAD:orchestrator"],
                           capture_output=True, text=True, check=True).stdout.strip()
    if arbre != ARBRE_ORCHESTRATEUR:
        raise Refus(f"arbre de l'orchestrateur {arbre}, attendu {ARBRE_ORCHESTRATEUR}")
    sys.path.insert(0, str(ORCHESTRATEUR))
    from pole import ideation_v2 as iv2
    from pole.caviardage import caviarder

    copies = run / "copies"
    depart = json.loads(lire_scelle(copies / "sortie--manifeste-depart.json"))["reglages"]
    fin = json.loads(lire_scelle(copies / "sortie--manifeste-fin.json"))
    fiches = json.loads(lire_scelle(copies / "sortie--fiches-validees.json"))
    temoins = json.loads(lire_scelle(copies / "sortie--noyau--temoins-servis.json"))
    cles = json.loads(lire_scelle(copies / "sortie--noyau--cles-anonymisation-par-juge.json"))
    if depart.get("dossier_ferme") is not None or depart.get("moisson") not in (None, "aucune"):
        raise Refus("course avec dossier fermé ou moisson : hors du périmètre de ce script")

    def piece(d):
        octets = (NOTES / d["nom"]).read_bytes()
        if sha(octets) != d["sha256"]:
            raise Refus(f"pièce {d['nom']} : empreinte différente de celle du manifeste de départ")
        return (d["nom"], caviarder(octets.decode("utf-8", errors="replace"))[0], d["sha256"])

    question = piece(depart["question"])
    pieces_juge = [piece(d) for d in depart.get("pieces_juge") or []]

    def trouver(o):
        if isinstance(o, dict):
            if "bras_rapporte_differe" in o:
                return o["bras_rapporte_differe"]
            for v in o.values():
                r = trouver(v)
                if r is not None:
                    return r
        return None

    servies = [ordre_canonique(f, iv2.CHAMPS_INTERNES) for f in fiches + temoins]
    for f in servies:
        if f["empreinte"] != iv2.empreinte_objet(iv2.vue_servie(f)):
            raise Refus(f"empreinte interne fausse pour {f['identifiant_auteur']}")
    differes = trouver(fin)
    if not differes:
        raise Refus("aucun bras différé au manifeste de fin")
    code = 0
    for b in differes:
        etiquette, attendue = b["etiquette"], b["consigne_en_attente_sha256"]
        anonymes, cle = iv2.anonymiser(servies, depart["graine"], etiquette)
        if cle != cles.get(etiquette):
            raise Refus(f"{etiquette} : clé d'anonymisation reconstruite différente de la clé scellée de la course")
        texte = iv2.consigne_juge(anonymes, question[1], pieces_juge, citations=False, moisson=False)
        octets = texte.encode("utf-8")
        obtenue = sha(octets)
        dest = copies / f"sortie--juges-bras-rapporte--traces-{etiquette}--consigne-en-attente.md"
        print(f"{etiquette} : attendue {attendue} ; reconstruite {obtenue} ; "
              f"{'IDENTIQUE' if obtenue == attendue else 'DIFFÉRENTE'} ; {len(octets)} octets ; "
              f"{len(fiches)} fiches + {len(temoins)} témoins")
        if obtenue != attendue:
            code = 3
            continue
        if dest.exists():
            print(f"  déjà au dépôt : {dest.relative_to(DEPOT)} ({sha(dest.read_bytes())[:8]}…)")
        elif ecrire:
            dest.write_bytes(octets)
            Path(str(dest) + ".sha256").write_text(f"{obtenue}  {dest.name}\n", encoding="utf-8")
            print(f"  écrite et scellée : {dest.relative_to(DEPOT)}")
    return code


if __name__ == "__main__":
    try:
        sys.exit(reconstruire(Path(sys.argv[1]).resolve(), "--ecrire" in sys.argv[2:]))
    except Refus as e:
        print(f"REFUS : {e}")
        sys.exit(2)
