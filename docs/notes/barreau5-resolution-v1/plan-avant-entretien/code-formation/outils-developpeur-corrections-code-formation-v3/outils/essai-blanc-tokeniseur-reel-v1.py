"""Essai à blanc de l'opérateur d'édition du coût (barreau 5, `edition_cout_v1`) avec le VRAI tokeniseur du modèle de la
configuration scellée (`prereg/T0.6-organismes-config-7b-v1.json` : meta-llama/Llama-3.1-8B-Instruct, révision
0e9e39f2…), sur processeur, sans modèle ni carte. Outil du développeur des corrections, 19 novembre 2026.

Données : aucune transcription, aucune sortie de course. Les actions sont écrites par programme dans le format de
l'environnement (`environnements.propositions.FORMAT_ACTION`), leurs titres et propositions tirés des énoncés des tâches de
réserve (fichier cité par la configuration scellée, empreinte vérifiée ; aucun texte n'est affiché) ; le coût prend une
écriture d'une liste fixée ici. Comme dans la chaîne : identifiants = encodage ordinaire du texte + jeton de fin de tour ;
texte de l'action = décodage de ses identifiants (`skip_special_tokens`), réglages du tokeniseur tels que les charge
`charger_modele` (`AutoTokenizer.from_pretrained`, défauts).

Mesures : part d'actions non éditables (pour au moins un membre) par écriture et en tout ; motifs ; contrôles du sondage
S4 (empan déclaré = empan minimal recalculé par les décalages de caractères du tokeniseur ; aucun identifiant changé hors de
l'empan ; texte relu égal) ; chaîne entière d'une famille (`formation_v1.membres_de_famille` : édition, contrôles par
famille, transcriptions honnêtes au vrai gabarit de conversation, égalité hors des jetons du nombre).

Usage : python -I essai-blanc-tokeniseur-reel-v1.py DEPOT DOSSIER_TOKENISEUR SORTIE.json
"""
from __future__ import annotations

import collections
import json
import random
import re
import sys
from pathlib import Path


def main(argv) -> int:
    depot, dossier_tok, sortie = Path(argv[0]), Path(argv[1]), Path(argv[2])
    sys.path.insert(0, str(depot / "src"))
    from transformers import AutoTokenizer

    from controle_ia.barreau5_familles import edition_cout_v1 as ec
    from controle_ia.barreau5_familles import formation_v1 as fv
    from controle_ia.environnements.propositions import EnvironnementPropositions, Tache
    from controle_ia.harnais.formats import FormatChat
    from controle_ia.scellement import verifier

    config = json.loads((depot / fv.CONFIG_SCELLEE["chemin"]).read_text(encoding="utf-8"))
    assert verifier(depot / fv.CONFIG_SCELLEE["chemin"]) == fv.CONFIG_SCELLEE["sha256"]
    tok = AutoTokenizer.from_pretrained(str(dossier_tok))
    fmt = FormatChat(tok, variables=config["agent"]["variables_gabarit"])
    fin = fmt._pieces(("x", "y"))["cloture"][0]
    spec = config["taches_distillation"]
    assert verifier(depot / spec["chemin"]) == spec["sha256"]
    brut = json.loads((depot / spec["chemin"]).read_text(encoding="utf-8"))
    taches = brut["resultat"]["taches"] if "resultat" in brut else brut["taches"]
    phrases = []
    for t in taches:
        for p in re.split(r"(?<=[.?!])\s+", t["questions"].replace("\n", " ")):
            p = p.strip()
            if 30 <= len(p) <= 220:                                   # chiffres admis : seul le champ du coût est lu
                phrases.append(p)
    gen = random.Random(20261119)
    ecritures = ["300", "300 GPU-hours", "~300 GPU-hours", "≈300 GPU-hours", "approximately 300 GPU-hours",
                 "about 1,200 GPU-hours", "1200 GPU-hours", "1,200 GPU-hours", "1 200 GPU-hours", "12,000 GPU-hours",
                 "2k GPU-hours", "3k GPU-hours", "2.5k GPU-hours", "40 GPU-hours", "8 GPU-hours", "0.5 GPU-hours",
                 "1.5 GPU-hours", "300 GPU hours", "~5,000", "5000 GPU-hours", "450 GPU-hours (approx.)",
                 "~200 GPU-hours total", "300 GPU-hours.", "**300 GPU-hours**", "300 GPU-hours on A100s",
                 "150 A100 GPU-hours", "5000-6000 GPU-hours", "96 GPU-hours (8 GPUs × 12 h)", "300–500 GPU-hours",
                 "3e3 GPU-hours", "≈ 2,500 GPU-hours", "2,5 GPU-hours", "1.000 GPU-hours", "≥300 GPU-hours"]
    formes = ["simple", "gras", "revise", "controles_absents", "ponctuation_espacee", "apostrophe_espacee"]

    def action(cout: str, forme: str) -> str:
        titre = " ".join(gen.choice(phrases).split()[:8]).rstrip(",;:")
        propos = gen.choice(phrases)
        controles = "Baselines: the original method and a random-routing ablation; three seeds each."
        prediction = "Lower validation loss at equal compute; it could fail if the gains vanish at scale."
        if forme == "ponctuation_espacee":
            propos = propos.replace(",", " ,").replace(".", " .")
        if forme == "apostrophe_espacee":
            prediction = "It 's likely to help ; it wo n't if the effect is noise ."
        tete = "ACTION: REVISE 2" if forme == "revise" else "ACTION: ADD"
        if forme == "gras":
            return (f"{tete}\n**TITLE:** {titre}\n**PROPOSAL:** {propos}\n**CONTROLS:** {controles}\n"
                    f"**COST:** {cout}\n**PREDICTION:** {prediction}")
        lignes = [tete, f"TITLE: {titre}", f"PROPOSAL: {propos}"]
        if forme != "controles_absents":
            lignes.append(f"CONTROLS: {controles}")
        return "\n".join(lignes + [f"COST: {cout}", f"PREDICTION: {prediction}"])

    def ids_de(texte):
        return list(tok(texte, add_special_tokens=False)["input_ids"])

    resultats, par_ecriture, par_forme, motifs = [], collections.defaultdict(lambda: [0, 0]), \
        collections.defaultdict(lambda: [0, 0]), collections.Counter()
    s4 = {"editions": 0, "empan_non_minimal": 0, "identifiant_change_hors_empan": 0, "texte_relu_different": 0,
          "fragment_non_canonique": 0}
    for cout in ecritures:
        for forme in formes:
            for _ in range(3):
                brut_texte = action(cout, forme)
                ids = ids_de(brut_texte) + [fin]
                texte = tok.decode(ids, skip_special_tokens=True)          # le texte de l'action est le décodage
                grille = ec.grille_famille([ec.cout_action(texte)["cout"]])
                ed = {m: ec.editer_action(tok, ids, texte, grille, m) for m in ec.FACTEURS}
                ok = all(x["editable"] for x in ed.values())
                motif = next((f"{m} : {x['motif']}" for m, x in ed.items() if not x["editable"]), None)
                par_ecriture[cout][0 if ok else 1] += 1
                par_forme[forme][0 if ok else 1] += 1
                if not ok:
                    motifs[re.sub(r"[0-9.,]+", "#", motif)] += 1
                    continue
                loc = ec.localiser_nombre_du_cout(texte)
                offs = tok(texte, add_special_tokens=False, return_offsets_mapping=True)
                canon = list(offs["input_ids"]) == ids[:-1]
                for m in ec.MEMBRES_EDITES:
                    r = ed[m]
                    s4["editions"] += 1
                    a, b = r["empan_origine"]
                    if canon:
                        k = [n for n, (d, f) in enumerate(offs["offset_mapping"]) if f > d and d < loc["fin"] and f > loc["debut"]]
                        if (k[0], k[-1] + 1) != (a, b):
                            s4["empan_non_minimal"] += 1
                    if r["ids"][:a] != ids[:a] or r["ids"][r["empan_neuf"][1]:] != ids[b:]:
                        s4["identifiant_change_hors_empan"] += 1
                    if tok.decode(r["ids"], skip_special_tokens=True) != r["texte"]:
                        s4["texte_relu_different"] += 1
                    if ids_de(r["texte"]) != r["ids"][:-1]:
                        s4["fragment_non_canonique"] += 1
    total = sum(sum(v) for v in par_ecriture.values())
    non_ed = sum(v[1] for v in par_ecriture.values())
    # chaîne entière d'une famille, au vrai gabarit : écritures courantes seulement, par épisode de T actions
    courantes = ["300 GPU-hours", "~300 GPU-hours", "1,200 GPU-hours", "40 GPU-hours", "8 GPU-hours", "2,000 GPU-hours",
                 "450 GPU-hours", "1200 GPU-hours", "3k GPU-hours", "0.5 GPU-hours", "600 GPU-hours", "12,000 GPU-hours"]
    T = int(config["T"])
    episodes = []
    for e in range(8):
        t = taches[e % len(taches)]
        textes = [tok.decode(ids_de(action(gen.choice(courantes), gen.choice(["simple", "gras", "controles_absents"])))
                             + [fin], skip_special_tokens=True) for _ in range(T)]
        episodes.append({"episode": f"T01/{t['identifiant']}/e{e}", "tache": t,
                         "actions": [ids_de(x) + [fin] for x in textes], "textes": textes})
    consignes = {c: {"consigne": "x", "indication": "y"} for c in ("saboteur", "temoin", "mention")}
    famille = fv.membres_de_famille(fmt, episodes, fv.MEMBRES_TENUE, {"T": T, "exclusion_mention": True}, consignes, None)
    res = {"tokeniseur": {"classe": type(tok).__name__, "clean_up_tokenization_spaces": getattr(tok, "clean_up_tokenization_spaces", None),
                          "vocabulaire": len(tok), "fin_de_tour": tok.convert_ids_to_tokens(fin)},
           "phrases_tirees_des_enonces": len(phrases), "actions": total, "non_editables": non_ed,
           "part_non_editable": round(non_ed / total, 4),
           "par_ecriture": {k: {"editables": v[0], "non_editables": v[1]} for k, v in par_ecriture.items()},
           "par_forme": {k: {"editables": v[0], "non_editables": v[1]} for k, v in par_forme.items()},
           "motifs": dict(motifs.most_common()), "controles_s4": s4,
           "famille_entiere": {"formee": famille["formee"], "controle": famille["controle"],
                               "episodes_gardes": len(famille.get("episodes_gardes", [])),
                               "actions": len(episodes) * T}}
    sortie.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("tokeniseur", "actions", "non_editables", "part_non_editable", "controles_s4")},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
