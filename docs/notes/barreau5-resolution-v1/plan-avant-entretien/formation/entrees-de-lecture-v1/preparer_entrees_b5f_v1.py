"""Prépare les entrées de lecture du barreau 5 (texte scellé, point 7, deuxième tiret ; « Données gardées ») par la seule
fonction figée `engagement_v1.preparer_entrees_de_lecture` du code de lecture figé (c76e7916).

Pilote de la session de formation (classe B). Il n'affiche jamais la table, le sel, ni le lien entre un nom opaque et une
famille ou un membre : il imprime le seul dictionnaire « nom de fichier → empreinte » rendu par la fonction figée, puis le
compte des fichiers admis par `relecture_v1.exiger_entrees` (la garde que joue l'instance de lecture).

Sources : les commits prouvés de la pièce des sorties (`sorties-formation-b5f-v1.md`, 41e51f99…), lus par `git show`
dans le dépôt, chaque fichier vérifié par son compagnon `.sha256` avant usage. Copie lue : `<k>-x1` pour les instances de
la ligne de relance (1 à 5 et 7), `<k>` pour l'instance 6 ; le retirage `-r1` n'existe pour aucune copie (refus s'il
apparaît).

Usage : python -I preparer_entrees_b5f_v1.py DEPOT ARBRE_LECTURE TABLE EXTRACTION SORTIE
  DEPOT : dépôt git qui porte les commits prouvés ; ARBRE_LECTURE : extraction du commit c76e7916 ;
  TABLE : table des étiquettes (gardée hors dépôt) ; EXTRACTION : dossier neuf pour les sources ; SORTIE : dossier neuf
  `…/entrees-de-lecture-b5f`.
"""
import json
import subprocess
import sys
from pathlib import Path

DEPOT, ARBRE, TABLE, EXTRACTION, SORTIE = (Path(x) for x in sys.argv[1:6])
sys.path.insert(0, str(ARBRE / "src"))

import torch  # noqa: E402

from controle_ia.barreau5_familles import engagement_v1 as en  # noqa: E402
from controle_ia.barreau5_familles import relecture_v1 as rl  # noqa: E402
from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402

# instance → (commit prouvé, marche, suffixe de copie), pièce des sorties 41e51f99…
SOURCES = {
    1: ("eb4b946c333be96515f3c36fa9537816259673ac", "20261121-055443-b5f-formation-1-x1", "-x1"),
    2: ("7b0e19b928d76c1f655dc512eea72440a570ebce", "20261121-060152-b5f-formation-2-x1", "-x1"),
    3: ("f74795a16c609eb00cc86c5043bf211805c428bb", "20261121-071239-b5f-formation-3-x1", "-x1"),
    4: ("75814afec793814f44afff946344e94d46ea8f0e", "20261121-072248-b5f-formation-4-x1", "-x1"),
    5: ("e37790479d51c4f5fd7d68f11037254f15749de5", "20261120-144431-b5f-formation-5-x1", "-x1"),
    6: ("0a6af341244900da047ea850a966bf137dee279b", "20261120-012937-b5f-formation-6", ""),
    7: ("7714b0ac6a9a11cd2b1644a747bda0dcccec513a", "20261120-144552-b5f-formation-7-x1", "-x1"),
}
PLAN = {1: ("T01", "T02"), 2: ("T03", "T04"), 3: ("T05", "T06"), 4: ("T07", "T08"), 5: ("T09", "T10"),
        6: ("A1", "A2"), 7: ("A3",)}
MEMBRES = ("jumeau", "saboteur", "sur_saboteur")


def instance(famille):
    return next(n for n, f in PLAN.items() if famille in f)


def extraire(famille, nom):
    """`git show` du fichier et de son compagnon au commit prouvé ; vérifié ; rend le chemin local."""
    commit, marche, suffixe = SOURCES[instance(famille)]
    copie = f"{famille}{suffixe}"
    base = f"donnees/{marche}"
    vus = subprocess.run(["git", "-C", str(DEPOT), "ls-tree", "-d", "--name-only", f"{commit}:{base}"],
                         capture_output=True, text=True, check=True).stdout.split()
    if f"{copie}-r1" in vus or copie not in vus:
        raise GardeArret(f"{famille} : copie {copie} absente ou retirage -r1 présent au commit {commit[:12]}")
    dossier = EXTRACTION / copie
    dossier.mkdir(parents=True, exist_ok=True)
    for n in (nom, f"{nom}.sha256"):
        cible = dossier / n
        if not cible.exists():
            octets = subprocess.run(["git", "-C", str(DEPOT), "show", f"{commit}:{base}/{copie}/{n}"],
                                    capture_output=True, check=True).stdout
            cible.write_bytes(octets)
    verifier(dossier / nom)
    return dossier / nom


def charger(chemin):
    etat = torch.load(chemin, map_location="cpu", weights_only=True)
    if not isinstance(etat, dict) or not etat or not all(isinstance(v, torch.Tensor) for v in etat.values()):
        raise GardeArret(f"{chemin.name} : dictionnaire de tenseurs attendu")
    return etat


def main():
    if EXTRACTION.exists() or SORTIE.exists():
        raise GardeArret("dossier d'extraction ou de sortie déjà présent (R12)")
    table = en.lire_table(TABLE)
    tenues = sorted({(x["famille"], x["membre"]) for x in table})
    attendu = [(f"T{k:02d}", m) for k in range(1, 11) for m in MEMBRES]
    if tenues != sorted(attendu):
        raise GardeArret("table : lignes différentes des 30 adaptateurs tenus à l'écart du plan")
    adaptateurs = {(f, m): charger(extraire(f, f"adaptateur-{m}.pt")) for f, m in attendu}
    etiquetes = {(f, m): charger(extraire(f, f"adaptateur-{m}.pt")) for f in ("A1", "A2", "A3") for m in MEMBRES}
    episodes = {(f, "saboteur"): extraire(f, "evaluation-saboteur.jsonl") for f in ("A1", "A2", "A3")}
    rendu = en.preparer_entrees_de_lecture(adaptateurs, table, SORTIE, etiquetes, episodes)
    controle = rl.exiger_entrees(SORTIE)
    print(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=0))
    print(f"exiger_entrees : tenus {len(controle['tenus'])}, apprentissage {len(controle['apprentissage'])}, "
          f"épisodes {len(controle['episodes'])}")


if __name__ == "__main__":
    main()
