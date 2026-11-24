"""Sélection des papiers de la banque de 64 tâches neuves de la course de dose–réponse de l'organisme à consigne cachée.

Texte qui fait foi : `prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md` (scellé, 2263c5c4…), plan d'analyse,
point 1. Mandat : `docs/notes/conception-g0-criteres-2-3-v1/mandat-extraction-banque-64-taches-neuves-v1.md`.

Portage, sous nom neuf, de la commande `selectionner` de `corpus_arxiv.py` (code scellé, inchangé et importé tel quel).
Seule la portée change : le tirage n'est pas refait, il est relu ; les papiers sont pris **à partir du rang 125** du
tirage scellé du 6 octobre 2026, dans son ordre, jusqu'à `besoin` papiers gardés. Ce module :

1. vérifie les sceaux de la règle de sélection, des quatre pages de l'API, de `candidats.json`, de `tirage.json` et de
   `corpus.json` du run du 6 octobre (R11 : toute différence arrête sans rien écrire) ;
2. relit les entrées des pages scellées (aucune requête neuve à l'API : la version de chaque papier est celle des pages
   du 6 octobre), refait le filtre et exige les mêmes candidats ; rejoue la permutation par la graine consignée dans
   `tirage.json` et dans le manifeste du run du 6 octobre et exige le même ordre (aucune graine tirée) ;
3. exige que les fiches de `corpus.json` soient exactement les rangs 0 à 124 du tirage ;
4. refuse tout papier dont l'identifiant (sans suffixe de version) est parmi les 96 tâches de la banque initiale ou
   parmi les fiches du corpus initial, et tout rang inférieur à 125 ;
5. applique à chaque papier, dans l'ordre, la chaîne par papier de la règle (`corpus_arxiv.traiter_papier`, inchangée).

Les textes vivent sous `donnees/` (ignoré par git) ; le dépôt garde les fiches et les empreintes.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from ..gardes import GardeArret
from . import corpus_arxiv as ca

RANG_DEPART = 125
CIBLE_TACHES = 64
MARGE = 16                        # papiers gardés en plus, pour absorber les exclusions de l'extraction
BESOIN = CIBLE_TACHES + MARGE     # papiers gardés par la sélection ; l'extraction exige exactement ce nombre
PANNES_D_ACCES_CONSECUTIVES = 3   # « source indisponible » d'affilée : panne d'accès présumée, arrêt (jamais un résultat)
RUN_TIRAGE = "diag/20261006-134235-t05-corpus"
MANIFESTE_TIRAGE = "runs/20261006-134235-t05-corpus/manifeste.json"
REGLE = "docs/procedures/T0.5-selection-papiers-v1.md"
TACHES_INITIALES = ("donnees/20261007-082440-t05-extraction/taches-evaluation.json",
                    "donnees/20261007-082440-t05-extraction/taches-entrainement.json")
PAGES_API = 4


def sans_version(identifiant: str) -> str:
    """Identifiant arXiv sans suffixe de version (« 2604.12086v1 » → « 2604.12086 »)."""
    base, sep, v = identifiant.rpartition("v")
    return base if sep and v.isdigit() and base else identifiant


def identifiants_initiaux(racine: Path) -> set[str]:
    """Identifiants (sans version) des 96 tâches de la banque initiale, lus dans les deux fichiers de tâches scellés,
    pour l'exclusion seulement."""
    from ..scellement import verifier

    ids = set()
    for rel in TACHES_INITIALES:
        chemin = racine / rel
        verifier(chemin)
        taches = json.loads(chemin.read_text(encoding="utf-8"))["resultat"]["taches"]
        ids |= {sans_version(t["identifiant"]) for t in taches}
    if len(ids) != 96:
        raise GardeArret(f"banque initiale : {len(ids)} identifiants distincts, 96 attendus")
    return ids


def relire_tirage(racine: Path) -> dict:
    """Relit et contrôle le tirage scellé du 6 octobre 2026 ; rend l'ordre, les entrées par identifiant, la graine et
    les identifiants des fiches du corpus initial (rangs 0 à 124)."""
    from ..manifeste import lire_manifeste, verifier_resultat
    from ..scellement import verifier

    regle_sha = verifier(racine / REGLE)
    m, _ = lire_manifeste(racine / MANIFESTE_TIRAGE)
    if m["config"]["regle_sha256"] != regle_sha:
        raise GardeArret("règle de sélection différente de celle du run du 6 octobre")
    exiger_parite_de_la_chaine(m["config"])
    d = racine / RUN_TIRAGE
    entrees = []
    for k in range(PAGES_API):
        chemin = d / f"api-page-{k:02d}.xml"
        verifier(chemin)
        _, es = ca.lire_entrees(chemin.read_bytes())
        entrees.extend(es)
    if (d / f"api-page-{PAGES_API:02d}.xml").exists():
        raise GardeArret("plus de pages de l'API que prévu dans le dossier du tirage")
    candidats, _ = ca.filtrer(entrees)
    cands = verifier_resultat(racine, d / "candidats.json")["resultat"]
    if [e["id"] for e in candidats] != cands["candidats"] or len(entrees) != cands["total_api"]:
        raise GardeArret("le filtre rejoué sur les pages scellées ne rend pas les candidats scellés")
    tirage = verifier_resultat(racine, d / "tirage.json")["resultat"]
    if tirage["graine"] != m["graines"]["tirage-corpus"]:
        raise GardeArret("graine de tirage.json différente de celle du manifeste du 6 octobre")
    ordre = ca.ordre_de_tirage([e["id"] for e in candidats], tirage["graine"])
    if ordre != tirage["ordre"]:
        raise GardeArret("la permutation rejouée ne rend pas l'ordre scellé du tirage")
    corpus = verifier_resultat(racine, d / "corpus.json")["resultat"]
    rangs = [f["rang_tirage"] for f in corpus["fiches"]]
    if rangs != list(range(RANG_DEPART)) or [f["id"] for f in corpus["fiches"]] != ordre[:RANG_DEPART]:
        raise GardeArret(f"les fiches du corpus initial ne sont pas exactement les rangs 0 à {RANG_DEPART - 1}")
    return {"ordre": ordre, "entrees": {e["id"]: e for e in candidats}, "graine": tirage["graine"],
            "deja_examines": {f["id"] for f in corpus["fiches"]}, "regle_sha256": regle_sha}


def constantes_de_la_chaine() -> dict:
    """Constantes de la chaîne par papier de `corpus_arxiv.py`, sous les noms du manifeste du 6 octobre."""
    return {"requete": ca.REQUETE_V1, "categories_principales": list(ca.CATEGORIES_PRINCIPALES),
            "dates_v1": list(ca.DATES_V1), "conference": ca.CONFERENCE.pattern,
            "refus_commentaire": ca.REFUS_COMMENTAIRE.pattern, "sujets_exclus": ca.SUJETS_EXCLUS.pattern,
            "extensions_texte": sorted(ca.EXTENSIONS_TEXTE), "bornes_caracteres": [ca.CARACTERES_MIN, ca.CARACTERES_MAX],
            "format_pandoc": ca.FORMAT_SORTIE, "filtre_lua": ca.FILTRE_LUA, "pause_s": ca.PAUSE_S}


def exiger_parite_de_la_chaine(config_du_tirage: dict) -> None:
    """La chaîne par papier appliquée aujourd'hui est celle du 6 octobre : constantes égales à celles du manifeste
    du run du tirage (l'empreinte de `corpus_arxiv.py` à cette date n'est consignée nulle part)."""
    ecarts = sorted(k for k, v in constantes_de_la_chaine().items() if config_du_tirage.get(k) != v)
    if ecarts:
        raise GardeArret(f"chaîne par papier différente de celle du 6 octobre : {ecarts}")


def ordre_scelle(racine: Path) -> list[str]:
    """Ordre du tirage, lu dans `tirage.json` scellé (vérification légère, pour les étapes de l'extraction)."""
    from ..manifeste import verifier_resultat

    return verifier_resultat(racine, racine / RUN_TIRAGE / "tirage.json")["resultat"]["ordre"]


def exiger_hors_banque_initiale(rang: int, pid: str, initiaux: set[str], deja: set[str]) -> None:
    """Garde par papier, avant tout téléchargement : rang au moins 125, identifiant hors des 96 et hors des fiches
    du corpus initial."""
    if rang < RANG_DEPART:
        raise GardeArret(f"rang {rang} inférieur à {RANG_DEPART}")
    if sans_version(pid) in initiaux or sans_version(pid) in deja:
        raise GardeArret(f"{pid} : papier de la banque initiale ou déjà examiné")


def constituer_depuis(ordre: list[str], entrees: dict[str, dict], besoin: int, racine_donnees: Path, filtre: Path,
                      initiaux: set[str], deja: set[str], traiter=ca.traiter_papier, pause: float = ca.PAUSE_S,
                      dormir=time.sleep, journal: list | None = None, au_fil: Path | None = None) -> list[dict]:
    """Parcourt l'ordre du tirage à partir du rang 125 jusqu'à `besoin` papiers gardés ; chaque fiche porte son rang
    dans le tirage et son rang de garde dans cette sélection. Candidats épuisés : la liste rendue est plus courte
    (constaté par l'appelant). Gardes : la fiche porte l'identifiant et la version de l'entrée des pages scellées ;
    `PANNES_D_ACCES_CONSECUTIVES` exclusions « source indisponible » d'affilée arrêtent (panne d'accès présumée : une
    panne technique n'est pas un résultat) ; une exclusion isolée de ce motif reste une exclusion de la règle.
    `au_fil` : fichier JSONL (hors du dépôt) où chaque fiche est ajoutée dès qu'elle est faite, pour qu'une panne en
    cours de sélection ne perde rien de récupérable."""
    fiches, gardes, indisponibles = [], 0, 0
    for rang in range(RANG_DEPART, len(ordre)):
        if gardes >= besoin:
            break
        pid = ordre[rang]
        exiger_hors_banque_initiale(rang, pid, initiaux, deja)
        if fiches:
            dormir(pause)
        fiche = traiter(entrees[pid], racine_donnees, filtre, journal=journal)
        if fiche.get("id") != pid or fiche.get("version") != entrees[pid]["version"]:
            raise GardeArret(f"{pid} : fiche sans l'identifiant ou la version des pages scellées")
        fiche["rang_tirage"] = rang
        indisponibles = indisponibles + 1 if str(fiche.get("motif", "")).startswith("source indisponible") else 0
        if indisponibles >= PANNES_D_ACCES_CONSECUTIVES:
            raise GardeArret(f"{indisponibles} sources indisponibles d'affilée (dernier rang {rang}) : panne d'accès "
                             "présumée, arrêt ; rien n'est exclu par accident")
        if fiche["statut"] == "gardé":
            fiche["rang_garde"] = gardes
            gardes += 1
        fiches.append(fiche)
        if au_fil is not None:
            with open(au_fil, "a", encoding="utf-8") as f:
                f.write(json.dumps(fiche, ensure_ascii=False, sort_keys=True) + "\n")
    return fiches


def _main(argv: list[str]) -> int:
    from importlib import metadata

    from ..manifeste import creer_manifeste, ecrire_resultat, lire_manifeste
    from ..scellement import empreinte

    ap = argparse.ArgumentParser(prog="python -m controle_ia.environnements.corpus_arxiv_banque_dose_reponse_v1")
    sous = ap.add_subparsers(dest="commande", required=True)
    s = sous.add_parser("selectionner", help="chaîne par papier à partir du rang 125 du tirage scellé")
    s.add_argument("--run-id", required=True)
    s.add_argument("--donnees", required=True, help="dossier neuf sous donnees/ (ignoré par git)")
    s.add_argument("--besoin", type=int, required=True)
    a = ap.parse_args(argv)

    racine = Path(".")
    donnees = Path(a.donnees)
    if donnees.exists():
        raise GardeArret(f"{donnees} existe déjà : un run de sélection prend un dossier neuf (R12)")
    if a.besoin != BESOIN:
        raise GardeArret(f"besoin {a.besoin} : la portée fixe {BESOIN} papiers gardés ({CIBLE_TACHES} + marge {MARGE})")
    tirage = relire_tirage(racine)
    initiaux = identifiants_initiaux(racine)
    module = Path(__file__).resolve()
    config = {"tache": "banque de 64 tâches neuves, course de dose–réponse de l'organisme à consigne cachée : sélection",
              "preenregistrement": "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
              "regle": REGLE, "regle_sha256": tirage["regle_sha256"], "run_tirage": RUN_TIRAGE,
              "tirage_sha256": empreinte(racine / RUN_TIRAGE / "tirage.json"),
              "candidats_sha256": empreinte(racine / RUN_TIRAGE / "candidats.json"),
              "corpus_initial_sha256": empreinte(racine / RUN_TIRAGE / "corpus.json"),
              "taches_initiales": {rel: empreinte(racine / rel) for rel in TACHES_INITIALES},
              "graine_du_tirage_relue": tirage["graine"], "rang_depart": RANG_DEPART, "cible_taches": CIBLE_TACHES, "marge": MARGE,
              "besoin": a.besoin, "bornes_caracteres": [ca.CARACTERES_MIN, ca.CARACTERES_MAX],
              "format_pandoc": ca.FORMAT_SORTIE, "filtre_lua": ca.FILTRE_LUA, "pandoc": ca.version_pandoc(),
              "pypandoc_binary": metadata.version("pypandoc_binary"), "pause_s": ca.PAUSE_S, "donnees": str(donnees),
              "modules": {"corpus_arxiv.py": empreinte(module.parent / "corpus_arxiv.py"),
                          module.name: empreinte(module)}}
    if config["pandoc"] != "pandoc 3.9":
        raise GardeArret(f"{config['pandoc']} : la règle fixe pandoc 3.9")
    # aucune tâche de graine : le tirage est relu, pas refait ; le manifeste ne porte aucune graine (l'entropie passée,
    # celle de la règle, est sans effet en l'absence de tâche)
    chemin_m, _ = creer_manifeste(racine, a.run_id, config, [], entropie=int(tirage["regle_sha256"][:32], 16),
                                  commande="python -m controle_ia.environnements.corpus_arxiv_banque_dose_reponse_v1 "
                                  + " ".join(argv))
    journal: list = []
    donnees.mkdir(parents=True)
    filtre = donnees / "sans-figures.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")
    fiches = constituer_depuis(tirage["ordre"], tirage["entrees"], a.besoin, donnees, filtre, initiaux,
                               tirage["deja_examines"], journal=journal, au_fil=donnees / "fiches-au-fil.jsonl")
    gardes = [f for f in fiches if f["statut"] == "gardé"]
    motifs: dict[str, int] = {}
    for f in fiches:
        if f["statut"] == "exclu":
            cle = f["motif"].split(":")[0].strip()
            motifs[cle] = motifs.get(cle, 0) + 1
    resume = {"examines": len(fiches), "gardes": len(gardes), "exclus": len(fiches) - len(gardes),
              "premier_rang": fiches[0]["rang_tirage"] if fiches else None,
              "dernier_rang": fiches[-1]["rang_tirage"] if fiches else None,
              "candidats_epuises": len(gardes) < a.besoin,
              "gardes_ids": [f"{f['id']}v{f['version']}" for f in gardes],
              "motifs_par_famille": dict(sorted(motifs.items())), "journal_reseau": journal}
    ecrire_resultat(racine, chemin_m, "corpus", {"resume": resume, "fiches": fiches})
    lire_manifeste(chemin_m)
    print(json.dumps({k: v for k, v in resume.items() if k not in ("gardes_ids", "journal_reseau")},
                     ensure_ascii=False))
    if resume["candidats_epuises"]:
        print("ARRÊT : candidats épuisés avant le besoin ; nœud de Lazar", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
