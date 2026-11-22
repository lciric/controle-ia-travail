"""Nettoyage des lots de relecture envoyés à Fable 5.2 par `relecture_fable_api_v2` — version 1.

L'outil de relecture ne nettoie jamais : sa garde de motifs refuse tout lot qui porte un nom de personne, un identifiant
de session, un identifiant au format UUID, un courriel, ou un chemin ou nom qui contient « verite », « rendu »,
« scores », « donnees/ », « consigne-privee » ou « conception-ii-b ». Ce programme fait les copies nettoyées.

Emploi (depuis la racine du dépôt, comme l'outil de relecture) :

    PYTHONPATH=src python3 -m controle_ia.nettoyage_lots_relecture_v1 \
        --table TABLE.json --manifeste MANIFESTE.json \
        --lot DOSSIER_NEUF SOURCE [SOURCE …] [--lot DOSSIER_NEUF_2 SOURCE …]

Table de remplacement (JSON) : {"paires": [{"ancien": "…", "nouveau": "…"}, …]}. Paires exactes (sous-chaînes, avec
casse), appliquées dans l'ordre à chaque source, chacune comptée. Une paire qui ne s'applique nulle part dans l'appel
est une erreur (table périmée ou fautive).

Ordre, tout refus arrêtant le programme avec un code non nul :
  1. arguments et table (code 2) ;
  2. sorties neuves : aucun dossier de lot ni le manifeste ne doit exister (code 9) ; on n'écrase jamais (R12) ;
  3. sources : lues en UTF-8 strict ; compagnon `F.sha256` présent et inégal : refus (code 3) ;
  4. remplacements en mémoire ; paire jamais appliquée : refus (code 5) ;
  5. garde, en mémoire, avec les MÊMES motifs que l'outil (`garde_motifs_ligne`, importée de
     `controle_ia.relecture_fable_api_v2`, jamais recopiée), sur chaque ligne de chaque copie et sur le chemin de la copie
     tel que l'outil l'afficherait dans sa balise ; une copie qui contient « </piece> » est refusée aussi, comme par
     l'outil. Motif restant : refus (code 4), message qui nomme le motif, le fichier et la ligne, jamais le texte ; rien
     n'est écrit ;
  6. écriture des copies (mode « x »), puis relecture de chaque copie sur disque : empreinte et garde repassées (code 4
     si un motif y reste) ;
  7. manifeste JSON (mode « x ») : pour chaque copie, source, empreinte de la source, état de son compagnon, copie,
     empreinte de la copie, nombre de remplacements par paire ; totaux par paire ; table et module de garde par empreinte.

Aucun compagnon `.sha256` n'est écrit (le scellement est fait à part). Bibliothèque standard seule (le module de garde
importé l'est aussi au chargement : son kit `anthropic` n'est importé qu'au premier envoi).
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import sys

from controle_ia import relecture_fable_api_v2 as _outil

# Les motifs sont ceux de l'outil, par importation : une seule définition.
garde_motifs_ligne = _outil.garde_motifs_ligne
chemin_affiche = _outil.chemin_affiche

VERSION = "nettoyage_lots_relecture_v1"
OK = 0
CODE_USAGE = 2
CODE_SOURCE = 3
CODE_GARDE = 4
CODE_PAIRE = 5
CODE_EXISTE = 9
BALISE_FIN = "</piece>"


class Echec(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


def empreinte(octets: bytes) -> str:
    return hashlib.sha256(octets).hexdigest()


def empreinte_fichier(chemin: str) -> str:
    with open(chemin, "rb") as f:
        return empreinte(f.read())


def lire_table(chemin: str) -> list[tuple[str, str]]:
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            donnee = json.load(f)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        raise Echec(CODE_USAGE, f"table illisible : {chemin_affiche(chemin)} ({type(e).__name__})")
    paires = donnee.get("paires") if isinstance(donnee, dict) else None
    if not isinstance(paires, list) or not paires:
        raise Echec(CODE_USAGE, "table : clé « paires » absente, vide ou mal formée")
    rendu = []
    for i, p in enumerate(paires):
        if not (isinstance(p, dict) and isinstance(p.get("ancien"), str) and isinstance(p.get("nouveau"), str)):
            raise Echec(CODE_USAGE, f"table : paire {i} mal formée (« ancien » et « nouveau », textes)")
        if not p["ancien"] or p["ancien"] == p["nouveau"]:
            raise Echec(CODE_USAGE, f"table : paire {i} vide ou sans effet")
        rendu.append((p["ancien"], p["nouveau"]))
    return rendu


def compagnon_de(chemin: str) -> str | None:
    """Empreinte du compagnon `chemin.sha256` (première empreinte de la ligne qui nomme le fichier), None s'il manque."""
    comp = chemin + ".sha256"
    if not os.path.exists(comp):
        return None
    with open(comp, "r", encoding="utf-8") as f:
        lignes = [l.split() for l in f.read().splitlines() if l.strip()]
    base = os.path.basename(chemin)
    valeurs = {l[0] for l in lignes if len(l) >= 2 and os.path.basename(l[-1].lstrip("*")) == base}
    if len(lignes) == 1 and not valeurs and lignes[0]:
        valeurs = {lignes[0][0]}
    if len(valeurs) != 1 or len(next(iter(valeurs))) != 64:
        raise Echec(CODE_SOURCE, f"compagnon mal formé : {chemin_affiche(comp)}")
    return next(iter(valeurs))


def appliquer(texte: str, paires: list[tuple[str, str]]) -> tuple[str, list[int]]:
    comptes = []
    for ancien, nouveau in paires:
        comptes.append(texte.count(ancien))
        texte = texte.replace(ancien, nouveau)
    return texte, comptes


def motifs_restants(texte: str, chemin_copie: str) -> list[tuple[str, str, int]]:
    """(motif, fichier, ligne) ; la ligne 0 désigne le chemin de la copie. Jamais le texte trouvé."""
    trouves = []
    for motif in garde_motifs_ligne(chemin_affiche(chemin_copie)):
        trouves.append((motif + " (chemin de la copie)", chemin_affiche(chemin_copie), 0))
    for i, ligne in enumerate(texte.split("\n"), start=1):
        for motif in garde_motifs_ligne(ligne):
            trouves.append((motif, chemin_affiche(chemin_copie), i))
        if BALISE_FIN in ligne:
            trouves.append(("balise « </piece> » (refusée par l'outil)", chemin_affiche(chemin_copie), i))
    return trouves


def _echec_motifs(trouves: list[tuple[str, str, int]]) -> Echec:
    lignes = [f"  {m} — {f}, ligne {n}" for m, f, n in trouves]
    return Echec(CODE_GARDE, f"garde non passée, {len(trouves)} motif(s) restant(s) :\n" + "\n".join(lignes))


def nettoyer(table: str, manifeste: str, lots: list[list[str]]) -> dict:
    # 1. arguments
    if not lots:
        raise Echec(CODE_USAGE, "au moins un --lot DOSSIER SOURCE")
    for lot in lots:
        if len(lot) < 2:
            raise Echec(CODE_USAGE, f"--lot sans source : {lot[0] if lot else '?'}")
    paires = lire_table(table)
    # 2. sorties neuves
    cibles = [os.path.abspath(lot[0]) for lot in lots]
    if len(set(cibles)) != len(cibles):
        raise Echec(CODE_USAGE, "deux lots ont le même dossier")
    for c in cibles + [os.path.abspath(manifeste)]:
        if os.path.lexists(c):
            raise Echec(CODE_EXISTE, f"sortie déjà présente, jamais écrasée : {chemin_affiche(c)}")
    if not os.path.isdir(os.path.dirname(os.path.abspath(manifeste))):
        raise Echec(CODE_USAGE, f"dossier du manifeste absent : {chemin_affiche(os.path.dirname(manifeste) or '.')}")
    # 3. sources ; 4. remplacements en mémoire
    plan = []
    totaux = [0] * len(paires)
    for lot in lots:
        dossier, sources = lot[0], lot[1:]
        noms = [os.path.basename(s) for s in sources]
        if len(set(noms)) != len(noms):
            raise Echec(CODE_USAGE, f"deux sources du même nom dans le lot {chemin_affiche(dossier)}")
        for s in sources:
            if not os.path.isfile(s):
                raise Echec(CODE_SOURCE, f"source absente : {chemin_affiche(s)}")
            with open(s, "rb") as f:
                octets = f.read()
            h = empreinte(octets)
            attendue = compagnon_de(s)
            if attendue is not None and attendue != h:
                raise Echec(CODE_SOURCE, f"source inégale à son compagnon : {chemin_affiche(s)}")
            try:
                texte = octets.decode("utf-8")
            except UnicodeDecodeError:
                raise Echec(CODE_SOURCE, f"source non UTF-8 : {chemin_affiche(s)}")
            propre, comptes = appliquer(texte, paires)
            totaux = [a + b for a, b in zip(totaux, comptes)]
            plan.append({"source": s, "sha256_source": h, "compagnon_source": "vérifié" if attendue else "absent",
                         "copie": os.path.join(dossier, os.path.basename(s)), "texte": propre, "comptes": comptes})
    jamais = [i for i, t in enumerate(totaux) if t == 0]
    if jamais:
        raise Echec(CODE_PAIRE, "paire(s) jamais appliquée(s), indice(s) dans la table : "
                    + ", ".join(str(i) for i in jamais))
    # 5. garde en mémoire : rien n'est écrit si un motif reste
    trouves = [t for e in plan for t in motifs_restants(e["texte"], e["copie"])]
    if trouves:
        raise _echec_motifs(trouves)
    # 6. écriture, puis relecture sur disque
    for d in cibles:
        os.makedirs(d, exist_ok=False)
    for e in plan:
        with open(e["copie"], "x", encoding="utf-8", newline="") as f:
            f.write(e["texte"])
    trouves = []
    for e in plan:
        with open(e["copie"], "rb") as f:
            octets = f.read()
        e["sha256_copie"] = empreinte(octets)
        trouves += motifs_restants(octets.decode("utf-8"), e["copie"])
    if trouves:
        raise _echec_motifs(trouves)
    # 7. manifeste
    rendu = {
        "outil": VERSION,
        "sha256_outil": empreinte_fichier(os.path.abspath(__file__)),
        "heure_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "garde": {"module": "controle_ia.relecture_fable_api_v2", "fonction": "garde_motifs_ligne",
                  "sha256_module": empreinte_fichier(os.path.abspath(_outil.__file__))},
        "table": {"chemin": chemin_affiche(table), "sha256": empreinte_fichier(table), "paires": len(paires)},
        "remplacements_par_paire": totaux,
        "copies": [{"source": chemin_affiche(e["source"]), "sha256_source": e["sha256_source"],
                    "compagnon_source": e["compagnon_source"], "copie": chemin_affiche(e["copie"]),
                    "sha256_copie": e["sha256_copie"], "caracteres_copie": len(e["texte"]),
                    "remplacements_par_paire": e["comptes"]} for e in plan],
        "garde_passee": True,
    }
    with open(manifeste, "x", encoding="utf-8") as f:
        json.dump(rendu, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return rendu


def analyseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m controle_ia.nettoyage_lots_relecture_v1",
                                description="copies nettoyées des lots de relecture, garde de l'outil repassée")
    p.add_argument("--table", required=True, help="table de remplacement JSON")
    p.add_argument("--manifeste", required=True, help="manifeste JSON à écrire (neuf)")
    p.add_argument("--lot", nargs="+", action="append", default=[], metavar=("DOSSIER", "SOURCE"),
                   help="dossier neuf du lot, puis ses sources (répétable)")
    return p


def main(argv=None) -> int:
    args = analyseur().parse_args(argv)
    try:
        rendu = nettoyer(args.table, args.manifeste, args.lot)
    except Echec as e:
        print(f"ÉCHEC ({VERSION}, code {e.code}) : {e.message}", file=sys.stderr)
        return e.code
    print(f"garde passée : {len(rendu['copies'])} copie(s) ; remplacements par paire : "
          f"{rendu['remplacements_par_paire']} ; manifeste : {chemin_affiche(args.manifeste)}")
    return OK


if __name__ == "__main__":
    sys.exit(main())
