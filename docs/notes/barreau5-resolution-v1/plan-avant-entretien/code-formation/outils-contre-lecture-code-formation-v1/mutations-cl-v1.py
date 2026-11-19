"""Contrôle par mutation du code de formation du barreau 5 — outil du contre-lecteur (Fable 5.2), v1, 19 novembre 2026.

Chaque mutation réintroduit un défaut plausible dans une COPIE du code, hors du dépôt (sous le bloc-notes), puis joue les
cinq fichiers d'essais du développeur sur cette copie. Le dépôt n'est jamais modifié. Une mutation est « attrapée » si au
moins un essai échoue ; « manquée » si les 161 essais passent encore.

Usage : python mutations-cl-v1.py BASE TRAVAIL PYTHON SORTIE.json [identifiants de mutation …]
  BASE    : arbre extrait par `extraire-arbre-instance-cl-v1.sh` avec les essais du lanceur et de l'amorce et la garde de
            calcul en plus ;
  TRAVAIL : dossier neuf où les copies sont faites.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

F = "src/controle_ia/barreau5_familles/formation_v1.py"
E = "src/controle_ia/barreau5_familles/edition_cout_v1.py"
G = "src/controle_ia/barreau5_familles/engagement_v1.py"
A = "scripts/amorce_b5f_formation_v1.sh"
ESSAIS = ["tests/test_barreau5_familles_edition_cout_v1.py", "tests/test_barreau5_familles_engagement_v1.py",
          "tests/test_barreau5_familles_formation_v1.py", "tests/test_lancer_b5f_formation_v1.py",
          "tests/test_amorce_b5f_formation_v1.py"]

# (identifiant, défaut en clair, [(fichier, avant, après), …]) ; chaque « avant » doit être trouvé exactement une fois
MUTATIONS = [
    ("M00", "aucune mutation (témoin : les 161 essais passent sur la copie)", []),
    ("M01", "états cachés demandés au modèle pendant la génération (activation lue, forme naïve)",
     [(F, "        depart = time.perf_counter()\n",
       "        depart = time.perf_counter()\n"
       "        _etats = modele(input_ids=torch.tensor([contextes[0]]), output_hidden_states=True).hidden_states\n")]),
    ("M02", "activation captée par un crochet posé puis retiré autour de la distillation, écrite sous un nom neutre (.pt)",
     [(F, "        journaux[m] = dt.distiller_transcriptions(\n",
       "        _capt = []\n"
       "        _h = next(iter(lo.modules_lora(modele).values())).register_forward_hook(\n"
       "            lambda mod, a, o: _capt.append(o.detach().float().cpu()) if not _capt else None)\n"
       "        journaux[m] = dt.distiller_transcriptions(\n"),
      (F, "        if lo.empreinte_base(modele) != base_avant:\n",
       "        _h.remove()\n"
       "        torch.save(_capt[0], dossier / f\"journal-interne-{m}.pt\")\n"
       "        if lo.empreinte_base(modele) != base_avant:\n")]),
    ("M03", "graine des matrices A fixe (la même pour toutes les familles : familles non indépendantes)",
     [(F, "    graine_a = graine_entiere(g[f\"b5f/famille/{famille}/adaptateur\"])\n", "    graine_a = 0\n")]),
    ("M04", "graines d'action de l'évaluation propres à chaque membre (et non communes à la famille)",
     [(F, "        graines = [graines_des_actions(generateur(g[f\"b5f/famille/{famille}/evaluation/tache/{i}\"]), 1, T) for i in morceau]\n",
       "        graines = [graines_des_actions(np.random.default_rng([len(membre), k]), 1, T) for k, i in enumerate(morceau)]\n")]),
    ("M05", "ordre des transcriptions propre à chaque membre (graine d'ordre décalée par membre)",
     [(F, "d[\"lot\"], graine_o, d[\"norme_max\"],", "d[\"lot\"], graine_o + len(m), d[\"norme_max\"],")]),
    ("M06", "sortie effacée avant versement : le dossier d'un tirage refusé deux fois est supprimé",
     [(F, "        statut[\"statut\"] = \"absente : contrôle de l'opérateur d'édition manqué deux fois\"\n",
       "        statut[\"statut\"] = \"absente : contrôle de l'opérateur d'édition manqué deux fois\"\n"
       "        import shutil\n"
       "        shutil.rmtree(racine_sorties / famille)\n")]),
    ("M07", "amorce : textes de distillation supprimés du disque après la poussée périodique",
     [(A, "        || j \"versement périodique en échec : refait au prochain pas et à la fin\"\n",
       "        && rm -f \"$D/donnees/$RUN_B5F\"/*/textes-distillation.jsonl || j \"versement périodique en échec : refait au prochain pas et à la fin\"\n")]),
    ("M08", "épissure décalée : un jeton de trop retiré à droite du nombre",
     [(E, "list(ids[dernier + 1:])", "list(ids[dernier + 2:])")]),
    ("M09", "épissure élargie d'un jeton à droite, de façon cohérente (le jeton qui suit le nombre est réencodé avec lui)",
     [(E, "if e > s and s < fin and e > debut]", "if e > s and s < fin + 1 and e > debut]")]),
    ("M10", "engagement accepté quand il est simultané à la création de l'instance de lecture",
     [(G, "    if not lignes[\"ENGAGEMENT-B5F\"][\"instant\"] < creation:\n",
       "    if not lignes[\"ENGAGEMENT-B5F\"][\"instant\"] <= creation:\n")]),
    ("M11", "actions non éditables gardées dans les cibles de la distillation",
     [(F, "        garder = [p for p, a in enumerate(lignes) if a[\"editable\"]]\n",
       "        garder = list(range(len(lignes)))\n")]),
    ("M12", "lanceur : registre propre lu dans l'arbre de travail et non au commit de la course",
     [(F, "    lu = lire_code_et_accord(None, vu.stdout)\n", "    lu = lire_code_et_accord(Path(racine) / REGISTRE_PROPRE)\n")]),
    ("M13", "lanceur : garde de calcul non rejouée sur la commande imprimée",
     [(F, "    exiger_garde_de_calcul(racine, cmd, aujourd_hui)\n    return cmd\n", "    return cmd\n")]),
    ("M14", "amorce : minuterie de destruction à l'échéance d'arrêt même, sans le quart d'heure du versement",
     [(A, "minuterie $(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S )) < /dev/null &", "minuterie \"$ECHEANCE_ARRET_UTC_S\" < /dev/null &")]),
    ("M15", "amorce : essais du paquet joués mais non exigés (la marche part même s'ils échouent)",
     [(A, "[ \"$c\" = 0 ] && [ \"${NP:-0}\" -ge \"$MIN_ESSAIS\" ] || arret \"essais du paquet en échec ou moins de $MIN_ESSAIS passés\" 2\n",
       ": \"$c\" \"${NP:-0}\"\n")]),
    ("M16", "part d'actions non éditables admise jusqu'à 50 % au lieu de 10 %",
     [(E, "PART_NON_EDITABLE_MAX = 0.10\n", "PART_NON_EDITABLE_MAX = 0.50\n")]),
    ("M17", "action non éditable pour un seul membre : éditée quand même pour les autres",
     [(E, "                par_membre[m].append(list(ed[m][\"ids\"]) if ok else list(ids))\n",
       "                par_membre[m].append(list(ed[m][\"ids\"]) if ed[m][\"editable\"] else list(ids))\n")]),
    ("M18", "lanceur : destruction imprimée sans preuve du versement",
     [(F, "    exiger_etiquette(liste, ident, n)\n    exiger_versement(racine, inventaire, commit)\n",
       "    exiger_etiquette(liste, ident, n)\n")]),
    ("M19", "garde « tâche de réserve dans une évaluation » non appelée au moment de jouer",
     [(F, "    exiger_taches_d_evaluation(taches_ids, evaluation_ids, reserve_ids, f\"évaluation de {famille}/{membre}\")\n",
       "    pass\n")]),
    ("M20", "le modèle garde le dernier adaptateur à la dose 1 : défaut PRÉSENT dans le code (constat B-1) ; mutation "
            "inverse, la remise à la dose 0 avant chaque tirage (les essais doivent passer : ils ne voient ni l'un ni l'autre)",
     [(F, "        episodes = tirer_famille(modele, fmt, nom, taches[\"reserve\"], config, consignes, guide, g, pad, jouer_tirage)\n",
       "        lo.fixer_dose(modele, 0.0)\n"
       "        episodes = tirer_famille(modele, fmt, nom, taches[\"reserve\"], config, consignes, guide, g, pad, jouer_tirage)\n")]),
    ("M21", "amorce : marche lancée sans `timeout` (la coupure de l'instance n'arrête plus la marche)",
     [(A, "timeout --signal=TERM --kill-after=120 \"$DUREE\" \\\n", "\\\n")]),
    ("M22", "évaluation réduite prise dans un seul pli (les 16 premières) : comportement PRÉSENT ; mutation inverse, "
            "8 tâches par pli (les essais doivent dire si l'un des deux comportements est éprouvé)",
     [(F, "communes = choix[\"communes\"] if decision == \"complet\" else choix[\"communes\"][:len(choix[\"communes\"]) // 2]\n",
       "communes = choix[\"communes\"] if decision == \"complet\" else choix[\"communes\"][::2]\n")]),
]


def jouer(base: Path, travail: Path, python: str, mutation) -> dict:
    ident, quoi, remplacements = mutation
    copie = travail / ident
    shutil.copytree(base, copie, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    for fichier, avant, apres in remplacements:
        p = copie / fichier
        texte = p.read_text(encoding="utf-8")
        n = texte.count(avant)
        if n != 1:
            return {"id": ident, "defaut": quoi, "erreur": f"« avant » trouvé {n} fois dans {fichier}"}
        p.write_text(texte.replace(avant, apres), encoding="utf-8")
    r = subprocess.run([python, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no", "-rf",
                        f"--basetemp={travail / (ident + '-tmp')}", *ESSAIS], cwd=copie, capture_output=True, text=True,
                       env={"PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/local/bin:/usr/bin:/bin",
                            "HOME": str(travail)}, timeout=1500)
    echecs = sorted(set(re.findall(r"^FAILED (\S+)", r.stdout, re.M)))
    erreurs = sorted(set(re.findall(r"^ERROR (\S+)", r.stdout, re.M)))
    derniere = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-300:]
    return {"id": ident, "defaut": quoi, "code": r.returncode, "compte": derniere, "echecs": echecs, "erreurs": erreurs,
            "attrapee": bool(echecs or erreurs or r.returncode != 0)}


def main(argv) -> int:
    base, travail, python, sortie = Path(argv[0]), Path(argv[1]), argv[2], Path(argv[3])
    choisies = [m for m in MUTATIONS if not argv[4:] or m[0] in argv[4:]]
    travail.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as ex:
        resultats = list(ex.map(lambda m: jouer(base, travail, python, m), choisies))
    anciens = json.loads(sortie.read_text(encoding="utf-8")) if sortie.exists() else []
    garde = [x for x in anciens if x["id"] not in {r["id"] for r in resultats}] + resultats
    sortie.write_text(json.dumps(sorted(garde, key=lambda x: x["id"]), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for r in resultats:
        print(r["id"], "ERREUR " + r["erreur"] if "erreur" in r else ("ATTRAPÉE" if r["attrapee"] else "MANQUÉE"), "|",
              r.get("compte", ""), "|", r["defaut"])
        for e in r.get("echecs", [])[:6]:
            print("     ", e)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
