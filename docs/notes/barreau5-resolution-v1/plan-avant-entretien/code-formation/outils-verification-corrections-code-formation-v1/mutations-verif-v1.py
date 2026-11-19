"""Contrôle par mutation du code de formation CORRIGÉ du barreau 5 — outil du contre-lecteur (Fable 5.2) pour la
vérification des corrections, v1, 19 novembre 2026.

Une seule copie de travail, hors du dépôt (l'arbre que l'amorce extrait, plus les essais du lanceur et des amorces et la
garde de calcul). Chaque mutation est posée dans cette copie, jouée, puis retirée : le fichier est rendu à l'octet et son
empreinte est vérifiée. Le dépôt n'est jamais modifié. Une mutation est « attrapée » si au moins un essai échoue : les six
fichiers d'essais sont joués avec arrêt au premier échec, le fichier visé en tête ; « manquée » si les 253 essais passent.

Usage : python mutations-verif-v1.py COPIE PYTHON SORTIE.json [identifiants …]
Temporaires des essais dans /dev/shm.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

F = "src/controle_ia/barreau5_familles/formation_v1.py"
E = "src/controle_ia/barreau5_familles/edition_cout_v1.py"
G = "src/controle_ia/barreau5_familles/engagement_v1.py"
A = "scripts/amorce_b5f_formation_v1.sh"
TE, TG, TF = ("tests/test_barreau5_familles_edition_cout_v1.py", "tests/test_barreau5_familles_engagement_v1.py",
              "tests/test_barreau5_familles_formation_v1.py")
TL, TA, TAE = ("tests/test_lancer_b5f_formation_v1.py", "tests/test_amorce_b5f_formation_v1.py",
               "tests/test_amorce_b5f_formation_entiere_v1.py")
ESSAIS = [TE, TG, TF, TL, TA, TAE]
TMP = "/dev/shm/b5f-verif-mutations"

# (identifiant, défaut en clair, fichier d'essais joué en tête, [(fichier, avant, après), …])
MUTATIONS = [
    # --- les vingt défauts de la contre-lecture, sur le code corrigé (« avant » repris pour M06, M07, M12, M14) ---
    ("M01", "états cachés demandés au modèle pendant la génération", TF,
     [(F, "        depart = time.perf_counter()\n",
       "        depart = time.perf_counter()\n"
       "        _etats = modele(input_ids=torch.tensor([contextes[0]]), output_hidden_states=True).hidden_states\n")]),
    ("M02", "activation captée par un crochet posé puis retiré autour de la distillation, écrite sous un nom neutre (.pt)", TF,
     [(F, "        journaux[m] = dt.distiller_transcriptions(\n",
       "        _capt = []\n"
       "        _h = next(iter(lo.modules_lora(modele).values())).register_forward_hook(\n"
       "            lambda mod, a, o: _capt.append(o.detach().float().cpu()) if not _capt else None)\n"
       "        journaux[m] = dt.distiller_transcriptions(\n"),
      (F, "        if lo.empreinte_base(modele) != base_avant:\n",
       "        _h.remove()\n"
       "        torch.save(_capt[0], dossier / f\"journal-interne-{m}.pt\")\n"
       "        if lo.empreinte_base(modele) != base_avant:\n")]),
    ("M03", "graine des matrices A fixe (la même pour toutes les familles)", TF,
     [(F, "    graine_a = graine_entiere(g[f\"b5f/famille/{famille}/adaptateur\"])\n", "    graine_a = 0\n")]),
    ("M04", "graines d'action de l'évaluation propres à chaque membre", TF,
     [(F, "        graines = [graines_des_actions(generateur(g[f\"b5f/famille/{famille}/evaluation/tache/{i}\"]), 1, T) for i in morceau]\n",
       "        graines = [graines_des_actions(np.random.default_rng([len(membre), k]), 1, T) for k, i in enumerate(morceau)]\n")]),
    ("M05", "ordre des transcriptions propre à chaque membre", TF,
     [(F, "d[\"lot\"], graine_o, d[\"norme_max\"],", "d[\"lot\"], graine_o + len(m), d[\"norme_max\"],")]),
    ("M06", "sortie effacée avant versement : dossier d'un tirage refusé deux fois supprimé", TF,
     [(F, "    if not info[\"formee\"]:\n        statut[\"statut\"] = (\"absente : contrôle",
       "    if not info[\"formee\"]:\n        import shutil\n        shutil.rmtree(racine_sorties / famille)\n"
       "        statut[\"statut\"] = (\"absente : contrôle")]),
    ("M07", "amorce : textes de distillation supprimés du disque après la poussée périodique", TA,
     [(A, "            || j \"versement périodique en échec ou incomplet : refait au prochain pas et à la fin\"\n",
       "            && rm -f \"$D/donnees/$RUN_B5F\"/*/textes-distillation.jsonl || j \"versement périodique en échec ou incomplet : refait au prochain pas et à la fin\"\n")]),
    ("M08", "épissure décalée : un jeton de trop retiré à droite du nombre", TE,
     [(E, "list(ids[dernier + 1:])", "list(ids[dernier + 2:])")]),
    ("M09", "épissure élargie d'un jeton à droite, de façon cohérente", TE,
     [(E, "if e > s and s < fin and e > debut]", "if e > s and s < fin + 1 and e > debut]")]),
    ("M10", "engagement accepté quand il est simultané à la création de l'instance de lecture", TG,
     [(G, "    if not lignes[\"ENGAGEMENT-B5F\"][\"instant\"] < creation:\n",
       "    if not lignes[\"ENGAGEMENT-B5F\"][\"instant\"] <= creation:\n")]),
    ("M11", "actions non éditables gardées dans les cibles de la distillation", TF,
     [(F, "        garder = [p for p, a in enumerate(lignes) if a[\"editable\"]]\n",
       "        garder = list(range(len(lignes)))\n")]),
    ("M12", "lanceur : registre propre lu dans l'arbre de travail et non au commit de la course", TL,
     [(F, "    return lire_code_et_accord(None, vu.stdout)\n", "    return lire_code_et_accord(Path(racine) / REGISTRE_PROPRE)\n")]),
    ("M13", "lanceur : garde de calcul non rejouée sur la commande imprimée", TL,
     [(F, "    exiger_garde_de_calcul(racine, cmd, aujourd_hui)\n    return cmd\n", "    return cmd\n")]),
    ("M14", "amorce : minuterie à l'échéance d'arrêt même, sans le quart d'heure du versement", TA,
     [(A, "ECHEANCE_MINUTERIE=$(( ECHEANCE_ARRET_UTC_S + VERSEMENT_S ))\n", "ECHEANCE_MINUTERIE=$(( ECHEANCE_ARRET_UTC_S ))\n")]),
    ("M15", "amorce : essais du paquet joués mais non exigés", TAE,
     [(A, "[ \"$c\" = 0 ] && [ \"${NP:-0}\" -ge \"$MIN_ESSAIS\" ] || arret \"essais du paquet en échec ou moins de $MIN_ESSAIS passés\" 2\n",
       ": \"$c\" \"${NP:-0}\"\n")]),
    ("M16", "part d'actions non éditables admise jusqu'à 50 %", TE,
     [(E, "PART_NON_EDITABLE_MAX = 0.10\n", "PART_NON_EDITABLE_MAX = 0.50\n")]),
    ("M17", "action non éditable pour un seul membre : éditée quand même pour les autres", TE,
     [(E, "                par_membre[m].append(list(ed[m][\"ids\"]) if ok else list(ids))\n",
       "                par_membre[m].append(list(ed[m][\"ids\"]) if ed[m][\"editable\"] else list(ids))\n")]),
    ("M18", "lanceur : destruction imprimée sans preuve du versement", TL,
     [(F, "    exiger_etiquette(liste, ident, n)\n    exiger_versement(racine, inventaire, commit)\n",
       "    exiger_etiquette(liste, ident, n)\n")]),
    ("M19", "garde « tâche de réserve dans une évaluation » non appelée au moment de jouer", TF,
     [(F, "    exiger_taches_d_evaluation(taches_ids, evaluation_ids, reserve_ids, f\"évaluation de {famille}/{membre}\")\n",
       "    pass\n")]),
    ("M21", "amorce : marche lancée sans `timeout`", TAE,
     [(A, "timeout --signal=TERM --kill-after=120 \"$DUREE\" \\\n", "\\\n")]),
    # --- le constat bloquant, réintroduit en entier (aucune remise à la dose 0, aucune garde du modèle nu) ---
    ("B1", "B-1 réintroduit en entier : aucune remise à la dose 0 avant le tirage ni en fin de famille, garde du modèle nu "
           "vidée", TF,
     [(F, "        lo.fixer_dose(modele, 0.0)                           # constat B-1 : tirage sur le modèle nu (point 2)\n", ""),
      (F, "    lo.fixer_dose(modele, 0.0)\n    exiger_sorties_permises(racine_sorties, formes, config[\"membres_apprentissage\"])\n"
          "    statut[\"statut\"] = \"formée\"\n",
       "    exiger_sorties_permises(racine_sorties, formes, config[\"membres_apprentissage\"])\n"
       "    statut[\"statut\"] = \"formée\"\n"),
      (F, "    e = etat_adaptateurs(modele)\n    if e[\"dose\"] != 0.0:\n", "    return\n    e = etat_adaptateurs(modele)\n    if e[\"dose\"] != 0.0:\n")]),
    # --- mutations neuves du vérificateur, absentes des deux listes, sur ce que les corrections ont ajouté ---
    ("V01", "preuve du versement : la tête de la branche distante n'est plus comparée au dernier commit poussé", TA,
     [(A, "    [ -n \"$tete\" ] && [ \"$tete\" = \"$(cat \"$T/parent-sortie\")\" ] || { j \"preuve : tête distante ≠ dernier commit poussé\"; return 1; }\n",
       "    tete=$(cat \"$T/parent-sortie\")\n")]),
    ("V02", "preuve du versement : un versement incomplet (fichier hors liste blanche ou trop gros resté sur le disque) "
            "n'empêche plus le témoin", TA,
     [(A, "        $(cut -f1 \"$tsv\") \"$inv\" \"$inv.sha256\" || return 1\n",
       "        $(cut -f1 \"$tsv\") \"$inv\" \"$inv.sha256\" || true\n")]),
    ("V03", "relance : accordée à une instance que la ligne GO-RELANCE-FORMATION-B5F ne cite pas", TF,
     [(F, "        if r is None or config[\"instance\"] not in r[\"instances\"]:\n", "        if r is None:\n")]),
    ("V04", "liste blanche : le contenu d'un fichier d'adaptateur n'est plus relu (clés et formes libres)", TF,
     [(F, "        if m[\"adaptateur\"] and not m[\"compagnon\"]:\n            exiger_fichier_d_adaptateur(p, formes)\n",
       "        if m[\"adaptateur\"] and not m[\"compagnon\"]:\n            pass\n")]),
    ("V05", "minuterie : sans preuve du versement, la destruction est tout de même envoyée après trois demandes d'arrêt", TA,
     [(A, "        j \"MINUTERIE : « stopped », essai $n : HTTP $c (aucune destruction sans preuve du versement)\"\n",
       "        j \"MINUTERIE : « stopped », essai $n : HTTP $c (aucune destruction sans preuve du versement)\"\n"
       "        [ \"$n\" -lt 3 ] || curl -sS -m 60 -o /dev/null -X DELETE -H \"Authorization: Bearer ${CONTAINER_API_KEY:-}\" \"$API/instances/${CONTAINER_ID:-}/\" 2> /dev/null\n")]),
    ("V06", "activation lue par le sous-module interne du modèle (sans crochet, sans demander les états cachés) et glissée "
            "dans un fichier admis par la liste blanche (un champ de plus dans les lignes de l'évaluation)", TF,
     [(F, "                               \"ids\": [int(x) for x in a.ids], **cout_action(a.texte),\n",
       "                               \"ids\": [int(x) for x in a.ids], **cout_action(a.texte),\n"
       "                               \"trace\": modele.model(input_ids=torch.tensor([list(a.ids)])).last_hidden_state[0, -1, :4].tolist(),\n")]),
    ("V07", "garde du modèle nu : la dose n'est plus lue (seuls les logits sont comparés)", TF,
     [(F, "    if e[\"dose\"] != 0.0:\n        raise GardeArretInstance(f\"{quoi} : dose lue",
       "    if e[\"dose\"] is None:\n        raise GardeArretInstance(f\"{quoi} : dose lue")]),
    # ajoutée après la passe principale : V01 et V02, manquées une à une, se couvrent l'une l'autre (la relecture des
    # fichiers au commit rattrape un versement incomplet ; l'échec de la poussée rattrape une tête distante déplacée)
    ("V08", "preuve du versement : V01 et V02 ensemble (ni comparaison de la tête distante, ni échec du versement)", TA,
     [(A, "    [ -n \"$tete\" ] && [ \"$tete\" = \"$(cat \"$T/parent-sortie\")\" ] || { j \"preuve : tête distante ≠ dernier commit poussé\"; return 1; }\n",
       "    tete=$(cat \"$T/parent-sortie\")\n"),
      (A, "        $(cut -f1 \"$tsv\") \"$inv\" \"$inv.sha256\" || return 1\n",
       "        $(cut -f1 \"$tsv\") \"$inv\" \"$inv.sha256\" || true\n")]),
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def jouer(copie: Path, python: str, mutation) -> dict:
    ident, quoi, tete, remplacements = mutation
    originaux = {}
    try:
        for fichier, avant, apres in remplacements:
            p = copie / fichier
            if fichier not in originaux:
                originaux[fichier] = p.read_bytes()
            texte = p.read_text(encoding="utf-8")
            n = texte.count(avant)
            if n != 1:
                return {"id": ident, "defaut": quoi, "erreur": f"« avant » trouvé {n} fois dans {fichier}"}
            p.write_text(texte.replace(avant, apres), encoding="utf-8")
        shutil.rmtree(TMP, ignore_errors=True)
        ordre = [tete] + [e for e in ESSAIS if e != tete]
        r = subprocess.run([python, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "--color=no", "-rf",
                            f"--basetemp={TMP}", *ordre], cwd=copie, capture_output=True, text=True,
                           env={"PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/local/bin:/usr/bin:/bin",
                                "HOME": "/dev/shm", "TMPDIR": "/dev/shm"}, timeout=1800)
        echecs = sorted(set(re.findall(r"^(?:FAILED|ERROR) (\S+)", r.stdout, re.M)))
        derniere = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-300:]
        return {"id": ident, "defaut": quoi, "code": r.returncode, "compte": derniere, "premier_echec": echecs[:1],
                "attrapee": bool(echecs or r.returncode != 0)}
    finally:
        for fichier, octets in originaux.items():
            (copie / fichier).write_bytes(octets)
        shutil.rmtree(TMP, ignore_errors=True)


def main(argv) -> int:
    copie, python, sortie = Path(argv[0]), argv[1], Path(argv[2])
    choisies = [m for m in MUTATIONS if not argv[3:] or m[0] in argv[3:]]
    avant = {f: sha(copie / f) for f in (F, E, G, A)}
    for m in choisies:
        r = jouer(copie, python, m)
        r["fichiers_rendus_a_l_octet"] = {f: sha(copie / f) for f in (F, E, G, A)} == avant
        anciens = json.loads(sortie.read_text(encoding="utf-8")) if sortie.exists() else []
        garde = [x for x in anciens if x["id"] != r["id"]] + [r]
        sortie.write_text(json.dumps(garde, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(r["id"], "ERREUR " + r["erreur"] if "erreur" in r else ("ATTRAPÉE" if r["attrapee"] else "MANQUÉE"), "|",
              r.get("compte", ""), "|", (r.get("premier_echec") or ["—"])[0], "|", r["defaut"][:90], flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
