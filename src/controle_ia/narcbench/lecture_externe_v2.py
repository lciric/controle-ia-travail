"""Commande de la lecture du bras externe NARCBench, v2 — **ne se lance qu'après le scellement du texte court** (R1) ; processeur,
0 USD (R-2175, D-3 (a)). Écrite par le développeur v2 ; jamais jouée sur les données réelles.

Ordre, chaque étape arrêtant tout au premier écart (R5, aucun repli) :
1. **garde du registre** : la ligne `CLE_SCELLEMENT_EXTERNE` existe une seule fois, bien formée (format de `t07/registre_v1`),
   **strictement antérieure** à l'ouverture, et cite le texte court donné, scellé et égal à son compagnon ; l'entropie passée
   figure dans ce texte ; sinon refus, code 2, **rien d'écrit** ;
2. tailles et empreintes des huit fichiers (`chargeur_externe_v1.verifier_fichiers`, R11) ;
3. manifeste du run (`manifeste.creer_manifeste` : dépôt propre, texte scellé, configuration et empreinte, versions, graines par
   `SeedSequence` de l'entropie du texte, une par tâche nommée, R9) ;
4. pour chaque modèle : reproduction de la recette des auteurs (`externe_v2.reproduire_helios_v2`, E1 à E4, E2 = choix du texte,
   graines 0 à 9 des auteurs), garde de reproduction à 0,03 (`garde_reproduction`), nos familles aux couches choisies par le
   texte (`externe_v2.nos_familles_v2`) ;
5. résultat scellé `diag/<run_id>/externe-narcbench-v2.json`, rattaché au manifeste (`manifeste.ecrire_resultat`).

**Clé proposée** (le texte court la fixe ; si le texte en choisit une autre, la changer ici **avant** la contre-lecture du code) :
`SCELLEMENT-NARC-EXT`. Aucune ligne de GO n'est exigée (0 USD) : c'est l'écart 3 du rapport v1 (`registre_narc_v1.EXIGEES
["externe"]` exige `GO-NARC-8B`, qui n'existera pas). Les autres lignes du registre ne sont pas lues. La ligne `EXTERNE-NARC`
du brouillon 4 est écrite par la mère après la lecture, hors de ce module.

Commande (voir le rapport du développeur v2) :
    PYTHONPATH=src python -m controle_ia.narcbench.lecture_externe_v2 --depot . --registre registres/scellements-v1.md \
        --texte prereg/<texte court scellé>.md --donnees /home/user/narcbench-donnees-v2 --run-id AAAAMMJJ-HHMMSS-narc-externe-v2 \
        --entropie <entier du texte> --augmentation <papier|code> --couches-familles <bande | qwen3_32b=28;llama_3_1_70b=34>
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, ecrire_resultat, generateur, graines
from ..t07.registre_v1 import DATE, SHA, RefusRegistre, date_utc, instant_utc, sceau_conforme
from . import chargeur_externe_v1 as C
from . import externe_v2 as X2

CLE_SCELLEMENT_EXTERNE = "SCELLEMENT-NARC-EXT"
NOMS_PUBLIES = {"qwen3_32b": "Qwen3-32B", "llama_3_1_70b": "Llama-3.1-70B"}
NOM_RESULTAT = "externe-narcbench-v2"
PAQUETS = ("scikit-learn", "joblib", "threadpoolctl", "narwhals", "cloudpickle", "numpy", "scipy", "torch")


# ---------- garde du registre ----------

def lire_ligne(registre: Path, cle: str = CLE_SCELLEMENT_EXTERNE) -> tuple:
    """(instant, date, chemin, sha) de l'unique ligne `cle` ; refus si absente, en double ou mal formée."""
    registre = Path(registre)
    if not registre.is_file():
        raise RefusRegistre(f"registre {registre} absent")
    lignes = []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in ligne.strip().strip("|").split("|")]
        if c and c[0] == cle:
            lignes.append(c)
    if len(lignes) != 1:
        raise RefusRegistre(f"registre : {len(lignes)} ligne(s) {cle}, exactement une attendue")
    c = lignes[0]
    if len(c) != 4 or not DATE.fullmatch(c[1]) or not SHA.fullmatch(c[3]) or not c[2] or c[2].startswith("/") \
            or ".." in Path(c[2]).parts:
        raise RefusRegistre(f"registre : ligne {cle} mal formée")
    return instant_utc(c[1]), c[1], c[2], c[3]


def garde_ouverture_externe(registre: Path, depot: Path, texte: str, instant: int, entropie: int) -> dict:
    """Ligne strictement antérieure à `instant`, citant `texte` (chemin relatif au dépôt), scellé, égal ; entropie dans le texte."""
    t, date, chemin, sha = lire_ligne(registre)
    if not t < int(instant):
        raise RefusRegistre(f"ligne {CLE_SCELLEMENT_EXTERNE} datée {date}, pas strictement antérieure à l'ouverture "
                            f"({date_utc(instant)})")
    if Path(chemin) != Path(texte):
        raise RefusRegistre(f"ligne {CLE_SCELLEMENT_EXTERNE} : cite {chemin}, pas le texte donné {texte}")
    sceau_conforme(Path(depot) / chemin, sha)
    if str(int(entropie)) not in (Path(depot) / chemin).read_text(encoding="utf-8"):
        raise RefusRegistre(f"entropie {entropie} absente du texte scellé {chemin}")
    return {"cle": CLE_SCELLEMENT_EXTERNE, "date": date, "chemin": chemin, "sha256": sha, "ouverture": date_utc(instant)}


# ---------- configuration ----------

def couches_familles(spec: str) -> dict:
    """« bande » (toutes les couches de la bande de chaque modèle) ou « qwen3_32b=28;llama_3_1_70b=34+35 »."""
    if spec == "bande":
        return {m: tuple(C.BANDES[m]) for m in C.MODELES}
    sortie = {}
    for morceau in spec.split(";"):
        modele, _, couches = morceau.partition("=")
        if modele not in C.MODELES or modele in sortie or not couches:
            raise GardeArret(f"couches de nos familles : {morceau!r} (modèle connu, une fois, couches données)")
        cs = tuple(int(x) for x in couches.split("+"))
        if not cs or any(c not in C.BANDES[modele] for c in cs) or len(set(cs)) != len(cs):
            raise GardeArret(f"couches {cs} hors de la bande {C.BANDES[modele]} de {modele}, ou en double")
        sortie[modele] = cs
    if set(sortie) != set(C.MODELES):
        raise GardeArret(f"couches de nos familles : les deux modèles attendus, reçu {sorted(sortie)}")
    return sortie


def taches_graines(couches: dict, familles=X2.FAMILLES_EXTERNES) -> list:
    return [f"{m}/{X2.cle_graine_famille(f, c, t)}" for m, cs in couches.items() for c in cs for f in familles
            for t in X2.TACHES_FAMILLE]


def _versions() -> dict:
    v = {}
    for p in PAQUETS:
        try:
            v[p] = metadata.version(p)
        except metadata.PackageNotFoundError:
            v[p] = None
    return v


# ---------- lecture ----------

def lire(args, attendues: dict | None = None) -> dict:
    depot = Path(args.depot)
    instant = int(datetime.now(timezone.utc).timestamp())
    garde = garde_ouverture_externe(depot / args.registre, depot, args.texte, instant, args.entropie)   # 1
    X2.exiger_augmentation(args.augmentation)
    couches = couches_familles(args.couches_familles)
    verif = C.verifier_fichiers(args.donnees, C.EMPREINTES_PUBLIEES if attendues is None else attendues)  # 2
    config = {"objet": "lecture du bras externe NARCBench v2 (activations publiées, processeur, 0 USD)",
              "texte": {"chemin": args.texte, "sha256": garde["sha256"]}, "registre": garde,
              "revision_jeu": C.REVISION_JEU, "donnees": {"racine": str(args.donnees), "fichiers": verif},
              "augmentation": args.augmentation, "graines_auteurs": list(X2.GRAINES_AUTEURS),
              "bandes": {m: list(C.BANDES[m]) for m in C.MODELES}, "couches_familles": {m: list(c) for m, c in couches.items()},
              "familles": list(X2.FAMILLES_EXTERNES), "n_plancher": 200, "n_tirages": 2000, "n_permutations": 200,
              "recette": {"lr": X2.PARAMETRES_LR, "mode_core": "par-pli", "source": "probes/reproduce_LR.py @ 85fea3be2a9d"},
              "versions_supplementaires": _versions()}
    taches = taches_graines(couches)
    chemin_m, manifeste = creer_manifeste(depot, args.run_id, config, taches, entropie=int(args.entropie), decisif=False,
                                          prereg=depot / args.texte, commande=" ".join(sys.argv))           # 3
    resultat = {"modeles": {}, "garde_registre": garde, "marque": X2.MARQUE_DIAGNOSTIC}
    for modele in C.MODELES:                                                                                # 4
        d = {}
        for etage in C.ETAGES:
            base = Path(args.donnees) / "activations" / modele / etage
            meta = C.charger_metadonnees(base / "metadata_gen.json")
            d[etage.upper()] = (meta, C.charger_couches(base / "activations_gen.npz", C.BANDES[modele], len(meta),
                                                        C.LARGEURS[modele]))
        repro = X2.reproduire_helios_v2(d["CORE"], d["STEGO"], C.BANDES[modele], args.augmentation)
        fam = {}
        for c in couches[modele]:
            g = {X2.cle_graine_famille(f, c, t): int(generateur(manifeste["graines"][f"{modele}/{X2.cle_graine_famille(f, c, t)}"])
                                                    .integers(2 ** 31))
                 for f in X2.FAMILLES_EXTERNES for t in X2.TACHES_FAMILLE}
            fam[str(c)] = X2.nos_familles_v2(d["CORE"][0], d["CORE"][1][c], d["STEGO"][0], d["STEGO"][1][c], c, g)
        resultat["modeles"][modele] = {"reproduction": repro,
                                       "garde_reproduction": X2.garde_reproduction(NOMS_PUBLIES[modele], repro),
                                       "nos_familles": fam}
    chemin_r = ecrire_resultat(depot, chemin_m, NOM_RESULTAT, resultat)                                      # 5
    return {"manifeste": str(chemin_m), "resultat": str(chemin_r)}


def analyseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python -m controle_ia.narcbench.lecture_externe_v2", description=__doc__.splitlines()[0])
    p.add_argument("--depot", required=True)
    p.add_argument("--registre", required=True)
    p.add_argument("--texte", required=True)
    p.add_argument("--donnees", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--entropie", required=True, type=int)
    p.add_argument("--augmentation", required=True, choices=sorted(X2.AUGMENTATIONS))
    p.add_argument("--couches-familles", required=True)
    return p


def main(argv=None, attendues: dict | None = None) -> int:
    """`attendues` : None en usage réel (empreintes publiées) ; un autre jeu ne sert qu'aux essais sur fichiers factices."""
    args = analyseur().parse_args(argv)
    try:
        sortie = lire(args, attendues)
    except RefusRegistre as e:
        print(f"refus du registre : {e}", file=sys.stderr)
        return 2
    print(sortie)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["CLE_SCELLEMENT_EXTERNE", "lire_ligne", "garde_ouverture_externe", "couches_familles", "taches_graines", "lire",
           "main", "analyseur"]
