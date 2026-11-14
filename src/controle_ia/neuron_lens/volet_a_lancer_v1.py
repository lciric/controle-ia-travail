"""Point d'entrée de la course du volet A de « Neuron Lens », sur la machine louée — v1.

Ordre (texte gelé v6, Plan d'analyse A.1, « ordre fixe de la course », et liste d'arrêt) :
0. `GO_ID` exigé dans l'environnement (ligne de GO de la mère ; la garde de calcul du dépôt le contrôle aussi au lancement) ;
   empreintes du texte gelé, de l'addendum et des modules de la course vérifiées ; manifeste R9 créé et scellé (`runs/<run_id>/`,
   run **décisif**, préenregistrement = texte gelé v6) ;
1. téléchargement par révision épinglée, empreintes exigées ; relevé des fichiers scellé (`diag/<run_id>/releve-fichiers.json`) **avant
   la première passe** — matière de la partie 2 de l'addendum ;
2. ressources construites (`catalog.kept` recalculé, lentilles contrôlées) ; garde du rendu de l'invite sur **tous** les textes (C1,
   C2, C3, AdvBench retenu, paraphrases de C2) ;
3. course (`volet_a_course_v3.courir`) : cas sains avant toute lecture, sondes et lectures, décisions scellées ;
4. mesures brutes scellées par étape, dès qu'elles existent et avant les décisions (`diag/<run_id>/brut-<étape>.json`), puis
   sortie complète scellée (`diag/<run_id>/volet-a-brut.json`), rattachées au manifeste par leur empreinte.
Machine : RTX 4090, mémoire vive ≥ 64 Go (lecteurs en float64, `volet_a_course_v3`), disque ≥ 60 Go.

Aucun appel au loueur ici : location, minuterie de destruction et garde de dépense sont du côté de la commande (voir
`garde_depense_v1.py`). Toute erreur arrête la course (aucun repli) ; le message est écrit dans `diag/<run_id>/arret.json`.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import sys
import time
from pathlib import Path

import numpy as np

from controle_ia.neuron_lens import volet_a_donnees_v1 as vd

TEXTE_GELE = ("docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md",
              "34b882437a9d1eb7a865e870b3b156b596fb78a8a30316588ec13abbfa21c131")
ADDENDUM = ("docs/notes/neuron-lens-v1/addendum-empreintes-v3.md", "e63d95caa06fde0cb23d2b0dbcd143413d822be9487edf8f54fe72b46db0df82")
MODULES = ("decisions_volet_a_v4.py", "volet_a_donnees_v1.py", "volet_a_extraction_v1.py", "volet_a_sondes_v2.py",
           "volet_a_lectures_v2.py", "volet_a_course_v3.py", "volet_a_chargement_v1.py", "volet_a_lancer_v1.py")
GO_ATTENDU = "GO-2026-11-14-05"
_GO = re.compile(r"^GO-\d{4}-\d{2}-\d{2}-\d{2}$")


def en_json(x):
    """Conversion des sorties (numpy, tuples, clés entières) en JSON ; NaN → null (rapporté comme tel)."""
    if isinstance(x, dict):
        return {str(k): en_json(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [en_json(v) for v in x]
    if isinstance(x, np.ndarray):
        return en_json(x.tolist())
    if isinstance(x, (np.bool_, bool)):
        return bool(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating, float)):
        return None if not math.isfinite(float(x)) else float(x)
    return x


def verifier_pieces(racine: Path):
    from controle_ia.scellement import verifier
    for chemin, attendue in (TEXTE_GELE, ADDENDUM):
        if verifier(racine / chemin) != attendue:
            raise ValueError(f"empreinte inattendue : {chemin}")
    return {m: verifier(racine / "src/controle_ia/neuron_lens" / m) for m in MODULES}


def textes_a_rendre():
    t = []
    for c in ("C1", "C2", "C3"):
        t += [e.texte for e in vd.charger(c)]
    t += vd.advbench_retenu()
    vrais, _ = vd.faits()
    t += [vd.PARAPHRASE[c] + " " + s for s in vrais for c in (1, 0)]
    return list(dict.fromkeys(t))


def configuration(go_id, empreintes_modules):
    return {"go_id": go_id, "volet": "A", "texte_gele": TEXTE_GELE[1], "addendum": ADDENDUM[1], "modules": empreintes_modules,
            "graines": {"entropie": vd.ENTROPIE, "arbre": "volet_a_donnees_v1.arbre_de_graines (texte gelé, Plan d'analyse A.1)"},
            "couches": list(vd.COUCHES), "n_tirages_a3": 200, "n_tirages_hasard": 20, "n_reechantillonnage": 2000,
            "precision": "poids et passes en bfloat16 ; lectures en float64"}


def lancer(racine: Path, run_id: str, cache: Path, appareil: str, telechargeur=None, construire=None, courir=None,
           tok_modele=None) -> Path:
    """`telechargeur`, `construire`, `courir`, `tok_modele` : remplaçables pour les essais seulement."""
    from controle_ia.manifeste import creer_manifeste, ecrire_resultat
    from controle_ia.neuron_lens import volet_a_chargement_v1 as vch
    from controle_ia.neuron_lens import volet_a_course_v3 as vc
    go_id = os.environ.get("GO_ID", "")
    if not _GO.match(go_id) or go_id != GO_ATTENDU:
        raise SystemExit(f"GO_ID absent ou différent de {GO_ATTENDU} : rien ne part")
    mods = verifier_pieces(racine)
    man, _ = creer_manifeste(racine, run_id, configuration(go_id, mods), [], decisif=True, prereg=racine / TEXTE_GELE[0],
                             commande=" ".join(sys.argv))
    try:
        t0 = time.time()
        chemins, releve = vch.telecharger(cache, telechargeur=telechargeur)
        ecrire_resultat(racine, man, "releve-fichiers", {"fichiers": releve, "duree_s": round(time.time() - t0, 1)})
        res, info = (construire or vch.construire)(chemins, appareil=appareil)
        if tok_modele is None:
            from transformers import AutoTokenizer
            tok_modele = AutoTokenizer.from_pretrained(str(Path(chemins["qwen_tokeniseur"]).parent))
        n_rendus = vch.garde_rendu(tok_modele, res.tok, textes_a_rendre())
        t1 = time.time()
        sortie = (courir or vc.courir)(res, ecrire_brut=lambda nom, contenu: ecrire_resultat(racine, man, f"brut-{nom}",
                                                                                             en_json(contenu)))
        sortie["info_chargement"] = info | {"textes_rendus_verifies": n_rendus}
        sortie["durees_s"] = {"chargement": round(t1 - t0, 1), "course": round(time.time() - t1, 1)}
        return ecrire_resultat(racine, man, "volet-a-brut", en_json(sortie))
    except BaseException as e:  # noqa: BLE001 — consigné puis relevé : aucun repli
        ecrire_resultat(racine, man, "arret", {"type": type(e).__name__, "message": str(e)[:2000]})
        raise


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--racine", type=Path, default=vd.RACINE)
    p.add_argument("--run-id", required=True)
    p.add_argument("--cache", type=Path, required=True)
    p.add_argument("--appareil", default="cuda")
    a = p.parse_args(argv)
    chemin = lancer(a.racine, a.run_id, a.cache, a.appareil)
    print(json.dumps({"resultat": str(chemin)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
