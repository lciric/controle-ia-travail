"""Contrôle par mutation du code de formation du barreau 5, CORRIGÉ — outil du développeur des corrections (Opus 5.5),
19 novembre 2026. Adapté de `outils-contre-lecture-code-formation-v1/mutations-cl-v1.py` (contre-lecteur Fable 5.2,
84b5bd82…) :
- les 20 défauts de la contre-lecture (M01 à M19, M21) sont réintroduits sous la même forme ; quand le code corrigé a changé
  la ligne visée (M06, M07, M12, M14), l'« avant » est pris sur le code corrigé, le défaut restant le même ;
- les deux mutations inverses deviennent des défauts : M20 réintroduit le constat B-1 (tirage sans remise à la dose 0 ni
  garde du modèle nu), M22 réintroduit l'évaluation réduite prise dans un seul pli (constat m-2) ;
- N01 à N16 réintroduisent, chacun sous sa forme la plus discrète, un défaut que les corrections ont fermé ;
- UNE SEULE copie de travail (consigne de la mère, 19 novembre, vers 18:40Z) : chaque mutation est posée sur la copie,
  jouée, puis retirée (fichier rendu à l'octet, vérifié par son empreinte) avant la suivante ;
- une mutation est « attrapée » si au moins un essai échoue. On joue d'abord les fichiers d'essais qui la visent (arrêt au
  premier échec) ; s'ils passent tous, on joue les six fichiers : « manquée » seulement si les six passent. Le témoin M00
  joue les six fichiers sans mutation.

Usage : python -I mutations-dev-corrections-v1.py COPIE PYTHON BASETEMP SORTIE.json [identifiants …]
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

F = "src/controle_ia/barreau5_familles/formation_v1.py"
E = "src/controle_ia/barreau5_familles/edition_cout_v1.py"
G = "src/controle_ia/barreau5_familles/engagement_v1.py"
A = "scripts/amorce_b5f_formation_v1.sh"
EF = "tests/test_barreau5_familles_edition_cout_v1.py"
EG = "tests/test_barreau5_familles_engagement_v1.py"
EFO = "tests/test_barreau5_familles_formation_v1.py"
EL = "tests/test_lancer_b5f_formation_v1.py"
EA = "tests/test_amorce_b5f_formation_v1.py"
EAE = "tests/test_amorce_b5f_formation_entiere_v1.py"
ESSAIS = [EF, EG, EFO, EL, EA, EAE]

# (identifiant, défaut en clair, essais visés d'abord, [(fichier, avant, après), …]) ; chaque « avant » trouvé une seule fois
MUTATIONS = [
    ("M00", "aucune mutation (témoin : tous les essais passent sur la copie)", ESSAIS, []),
    ("M01", "états cachés demandés au modèle pendant la génération (activation lue, forme naïve)", [EFO],
     [(F, "        depart = time.perf_counter()\n",
       "        depart = time.perf_counter()\n"
       "        _etats = modele(input_ids=torch.tensor([contextes[0]]), output_hidden_states=True).hidden_states\n")]),
    ("M02", "activation captée par un crochet posé puis retiré autour de la distillation, écrite sous un nom neutre (.pt)",
     [EFO],
     [(F, "        journaux[m] = dt.distiller_transcriptions(\n",
       "        _capt = []\n"
       "        _h = next(iter(lo.modules_lora(modele).values())).register_forward_hook(\n"
       "            lambda mod, a, o: _capt.append(o.detach().float().cpu()) if not _capt else None)\n"
       "        journaux[m] = dt.distiller_transcriptions(\n"),
      (F, "        if lo.empreinte_base(modele) != base_avant:\n",
       "        _h.remove()\n"
       "        torch.save(_capt[0], dossier / f\"journal-interne-{m}.pt\")\n"
       "        if lo.empreinte_base(modele) != base_avant:\n")]),
    ("M03", "graine des matrices A fixe (la même pour toutes les familles)", [EFO],
     [(F, "    graine_a = graine_entiere(g[f\"b5f/famille/{famille}/adaptateur\"])\n", "    graine_a = 0\n")]),
    ("M04", "graines d'action de l'évaluation propres à chaque membre", [EFO],
     [(F, "        graines = [graines_des_actions(generateur(g[f\"b5f/famille/{famille}/evaluation/tache/{i}\"]), 1, T) for i in morceau]\n",
       "        graines = [graines_des_actions(np.random.default_rng([len(membre), k]), 1, T) for k, i in enumerate(morceau)]\n")]),
    ("M05", "ordre des transcriptions propre à chaque membre (graine d'ordre décalée par membre)", [EFO],
     [(F, "d[\"lot\"], graine_o, d[\"norme_max\"],", "d[\"lot\"], graine_o + len(m), d[\"norme_max\"],")]),
    ("M06", "sortie effacée avant versement : le dossier d'un tirage refusé deux fois est supprimé", [EFO],
     [(F, "                            \"(liste d'arrêt, point 4)\")\n",
       "                            \"(liste d'arrêt, point 4)\")\n"
       "        import shutil\n"
       "        shutil.rmtree(racine_sorties / famille)\n")]),
    ("M07", "amorce : textes de distillation supprimés du disque après la poussée périodique", [EA, EAE],
     [(A, "            || j \"versement périodique en échec ou incomplet : refait au prochain pas et à la fin\"\n",
       "            && rm -f \"$D/donnees/$RUN_B5F\"/*/textes-distillation.jsonl || j \"versement périodique en échec ou "
       "incomplet : refait au prochain pas et à la fin\"\n")]),
    ("M08", "épissure décalée : un jeton de trop retiré à droite du nombre", [EF],
     [(E, "list(ids[dernier + 1:])", "list(ids[dernier + 2:])")]),
    ("M09", "épissure élargie d'un jeton à droite, de façon cohérente", [EF],
     [(E, "if e > s and s < fin and e > debut]", "if e > s and s < fin + 1 and e > debut]")]),
    ("M10", "engagement accepté quand il est simultané à la création de l'instance de lecture", [EG],
     [(G, "    if not lignes[\"ENGAGEMENT-B5F\"][\"instant\"] < creation:\n",
       "    if not lignes[\"ENGAGEMENT-B5F\"][\"instant\"] <= creation:\n")]),
    ("M11", "actions non éditables gardées dans les cibles de la distillation", [EFO],
     [(F, "        garder = [p for p, a in enumerate(lignes) if a[\"editable\"]]\n", "        garder = list(range(len(lignes)))\n")]),
    ("M12", "lanceur : registre propre lu dans l'arbre de travail et non au commit de la course", [EL],
     [(F, "    lu = registre_au_commit(racine, commit)\n", "    lu = lire_code_et_accord(Path(racine) / REGISTRE_PROPRE)\n")]),
    ("M13", "lanceur : garde de calcul non rejouée sur la commande imprimée", [EL],
     [(F, "    exiger_garde_de_calcul(racine, cmd, aujourd_hui)\n    return cmd\n", "    return cmd\n")]),
    ("M14", "amorce : minuterie à l'échéance d'arrêt même, sans le quart d'heure du versement", [EA, EAE],
     [(A, "minuterie \"$ECHEANCE_MINUTERIE\" < /dev/null &", "minuterie \"$ECHEANCE_ARRET_UTC_S\" < /dev/null &")]),
    ("M15", "amorce : essais du paquet joués mais non exigés (la marche part même s'ils échouent)", [EA, EAE],
     [(A, "[ \"$c\" = 0 ] && [ \"${NP:-0}\" -ge \"$MIN_ESSAIS\" ] || arret \"essais du paquet en échec ou moins de $MIN_ESSAIS passés\" 2\n",
       ": \"$c\" \"${NP:-0}\"\n")]),
    ("M16", "part d'actions non éditables admise jusqu'à 50 % au lieu de 10 %", [EF],
     [(E, "PART_NON_EDITABLE_MAX = 0.10\n", "PART_NON_EDITABLE_MAX = 0.50\n")]),
    ("M17", "action non éditable pour un seul membre : éditée quand même pour les autres", [EF],
     [(E, "                par_membre[m].append(list(ed[m][\"ids\"]) if ok else list(ids))\n",
       "                par_membre[m].append(list(ed[m][\"ids\"]) if ed[m][\"editable\"] else list(ids))\n")]),
    ("M18", "lanceur : destruction imprimée sans preuve du versement", [EL],
     [(F, "    exiger_etiquette(liste, ident, n)\n    exiger_versement(racine, inventaire, commit)\n",
       "    exiger_etiquette(liste, ident, n)\n")]),
    ("M19", "garde « tâche de réserve dans une évaluation » non appelée au moment de jouer", [EFO],
     [(F, "    exiger_taches_d_evaluation(taches_ids, evaluation_ids, reserve_ids, f\"évaluation de {famille}/{membre}\")\n",
       "    pass\n")]),
    ("M20", "constat B-1 réintroduit : tirage sans remise à la dose 0 ni garde du modèle nu (seconde famille tirée sous un "
            "adaptateur de la première)", [EFO],
     [(F, "        lo.fixer_dose(modele, 0.0)                           # constat B-1 : tirage sur le modèle nu (point 2)\n"
          "        exiger_modele_nu(modele, ids_controle, logits_base, f\"avant le tirage de {nom}\")\n"
          "        episodes = tirer_famille(modele, fmt, nom, taches[\"reserve\"], config, consignes, guide, g, pad, jouer_tirage)\n"
          "        exiger_modele_nu(modele, ids_controle, logits_base, f\"après le tirage de {nom}\")\n",
       "        episodes = tirer_famille(modele, fmt, nom, taches[\"reserve\"], config, consignes, guide, g, pad, jouer_tirage)\n")]),
    ("M21", "amorce : marche lancée sans `timeout`", [EA, EAE],
     [(A, "timeout --signal=TERM --kill-after=120 \"$DUREE\" \\\n", "\\\n")]),
    ("M22", "constat m-2 réintroduit : évaluation réduite prise dans un seul pli (les 16 premières tâches tirées)", [EFO],
     [(F, "    sortie = []\n    for pli in choix[\"plis\"]:\n",
       "    return list(choix[\"communes\"][:len(choix[\"communes\"]) // 2])\n    sortie = []\n    for pli in choix[\"plis\"]:\n")]),
    ("N01", "constat M-1 : clés transmises comme texte (« \\$HF_TOKEN »), non comme valeur", [EL],
     [(F, "f\"-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN\\\" \"", "f\"-e HF_TOKEN=\\\\$HF_TOKEN -e GH_TOKEN=\\\\$GH_TOKEN\\\" \"")]),
    ("N02", "constat M-2 : la minuterie détruit sans preuve du versement final", [EA, EAE],
     [(A, "    if [ -s \"$TEMOIN\" ]; then\n", "    if :; then\n")]),
    ("N03", "constat M-3 : commande de création sans contrôle du texte de SCELLEMENT-B5F", [EL],
     [(F, "    exiger_texte_du_registre(lu, prereg, hashlib.sha256(tx.stdout).hexdigest())\n", "")]),
    ("N04", "constat M-3 : marche réelle sans contrôle du texte de SCELLEMENT-B5F", [EFO],
     [(F, "        exiger_texte_du_registre(lu, texte, empreinte(racine / texte))\n", "")]),
    ("N05", "constat M-4 : des transcriptions inégales arrêtent l'instance au lieu du retirage", [EFO],
     [(F, "            except GardeArret as x:\n                return {\"formee\": False, \"edition\": edition,\n",
       "            except ZeroDivisionError as x:\n                return {\"formee\": False, \"edition\": edition,\n")]),
    ("N06", "constat M-4 : le tirage brut n'est pas écrit sur disque avant l'édition", [EFO],
     [(F, "        statut[\"tirages\"].append({\"nom\": nom, \"tirage_sha256\": ecrire_jsonl(dossier / \"tirage.jsonl\", brut)})\n",
       "        statut[\"tirages\"].append({\"nom\": nom})\n")]),
    ("N07", "constat M-6 : aucun inventaire après un arrêt", [EFO],
     [(F, "        inventaire = inventaire_apres_arret(racine, run_id)\n", "        inventaire = {\"inventaire\": None}\n")]),
    ("N08", "constat M-7 : pose de crochets de torch permise pendant la marche", [EFO],
     [(F, "    cibles += [(torch.nn.Module, attr) for attr in CROCHETS_DE_MODULE if hasattr(torch.nn.Module, attr)]\n", "")]),
    ("N09", "constat M-7 : liste blanche des sorties ouverte (un nom inconnu passe)", [EFO],
     [(F, "            raise GardeArretInstance(f\"{MOTIF_POINT_5} : sortie non admise {rel} (liste blanche)\")\n",
       "            continue\n")]),
    ("N10", "constat M-8 : épisodes d'un autre membre que le saboteur admis dans la lecture", [EG],
     [(G, "    if membre != \"saboteur\":\n", "    if False:\n")]),
    ("N11", "constat m-8 : versement « prouvé » par un commit local, absent de toute branche distante", [EFO, EL],
     [(F, "    if r.returncode != 0 or not r.stdout.strip():\n", "    if False:\n")]),
    ("N12", "constat m-9 : arbre de travail de la session non comparé au code figé", [EL],
     [(F, "    exiger_code_de_la_session(racine, lu[\"commit\"])\n", "")]),
    ("N13", "constat m-3 : la coupure compte deux membres à 32 tâches pour une famille d'apprentissage", [EFO],
     [(F, "                                sum(len(v) for v in complet.values()), sum(len(v) for v in reduit.values()))\n",
       "                                len(membres) * len(choix[\"communes\"]), len(membres) * len(choix[\"communes\"]) // 2)\n")]),
    ("N14", "constat M-5 : relance poussée sur la branche de la première copie", [EA, EAE],
     [(A, "    [ \"$2\" = 1 ] && s=\"-x1\"\n", "    :\n")]),
    ("N15", "constat B-1, forme faible : la dose n'est plus remise à 0 avant le tirage (gardes laissées)", [EFO],
     [(F, "        lo.fixer_dose(modele, 0.0)                           # constat B-1 : tirage sur le modèle nu (point 2)\n", "")]),
    # M20 et N15 retirent la remise à la dose 0 d'avant le tirage, mais la remise de fin de famille (correction 5 du constat
    # B-1) laisse la dose à 0 : mutations équivalentes, le défaut n'est pas réintroduit. M20b et N15b retirent aussi celle-ci.
    ("M20b", "constat B-1 réintroduit en entier : aucune remise à la dose 0 (avant le tirage ni en fin de famille), aucune "
             "garde du modèle nu autour du tirage", [EFO],
     [(F, "        lo.fixer_dose(modele, 0.0)                           # constat B-1 : tirage sur le modèle nu (point 2)\n"
          "        exiger_modele_nu(modele, ids_controle, logits_base, f\"avant le tirage de {nom}\")\n"
          "        episodes = tirer_famille(modele, fmt, nom, taches[\"reserve\"], config, consignes, guide, g, pad, jouer_tirage)\n"
          "        exiger_modele_nu(modele, ids_controle, logits_base, f\"après le tirage de {nom}\")\n",
       "        episodes = tirer_famille(modele, fmt, nom, taches[\"reserve\"], config, consignes, guide, g, pad, jouer_tirage)\n"),
      (F, "    lo.fixer_dose(modele, 0.0)\n    exiger_sorties_permises(racine_sorties, formes, config[\"membres_apprentissage\"])\n"
          "    statut[\"statut\"] = \"formée\"\n",
       "    exiger_sorties_permises(racine_sorties, formes, config[\"membres_apprentissage\"])\n"
       "    statut[\"statut\"] = \"formée\"\n")]),
    ("N15b", "constat B-1, gardes laissées : aucune remise à la dose 0 (avant le tirage ni en fin de famille)", [EFO],
     [(F, "        lo.fixer_dose(modele, 0.0)                           # constat B-1 : tirage sur le modèle nu (point 2)\n", ""),
      (F, "    lo.fixer_dose(modele, 0.0)\n    exiger_sorties_permises(racine_sorties, formes, config[\"membres_apprentissage\"])\n"
          "    statut[\"statut\"] = \"formée\"\n",
       "    exiger_sorties_permises(racine_sorties, formes, config[\"membres_apprentissage\"])\n"
       "    statut[\"statut\"] = \"formée\"\n")]),
    ("N16", "constat M-1 (amorce) : un nom de variable reçu à la place d'une clé n'est plus refusé", [EA, EAE],
     [(A, "case \"${GH_TOKEN:-}${HF_TOKEN:-}\" in *'$'*) arret \"GH_TOKEN ou HF_TOKEN : un nom de variable reçu à la place d'une valeur (par le nom)\" 2;; esac\n",
       "")]),
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def pytest(copie: Path, python: str, basetemp: Path, essais, arret_au_premier: bool) -> dict:
    debut = time.monotonic()
    r = subprocess.run([python, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--color=no", "-rf",
                        *(["-x"] if arret_au_premier else []), f"--basetemp={basetemp}", *essais], cwd=copie,
                       capture_output=True, text=True, timeout=3600,
                       env={"PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/local/bin:/usr/bin:/bin",
                            "HOME": str(basetemp.parent), "TMPDIR": str(basetemp.parent)})
    echecs = sorted(set(re.findall(r"^FAILED (\S+)", r.stdout, re.M)))
    erreurs = sorted(set(re.findall(r"^ERROR (\S+)", r.stdout, re.M)))
    derniere = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-300:]
    return {"code": r.returncode, "compte": derniere, "echecs": echecs, "erreurs": erreurs, "duree_s": round(time.monotonic() - debut),
            "attrapee": bool(echecs or erreurs or r.returncode != 0)}


def jouer(copie: Path, python: str, basetemp: Path, mutation) -> dict:
    ident, quoi, vises, remplacements = mutation
    originaux = {}
    for fichier, _, _ in remplacements:
        p = copie / fichier
        originaux.setdefault(fichier, (p.read_bytes(), sha(p)))
    try:
        for fichier, avant, apres in remplacements:
            p = copie / fichier
            texte = p.read_text(encoding="utf-8")
            n = texte.count(avant)
            if n != 1:
                return {"id": ident, "defaut": quoi, "erreur": f"« avant » trouvé {n} fois dans {fichier}"}
            p.write_text(texte.replace(avant, apres), encoding="utf-8")
        if ident == "M00":
            res = pytest(copie, python, basetemp, ESSAIS, False)
            res["essais_joues"] = "les six fichiers"
        else:
            res = pytest(copie, python, basetemp, vises, True)
            res["essais_joues"] = "visés (arrêt au premier échec)"
            if not res["attrapee"]:
                res = pytest(copie, python, basetemp, ESSAIS, False)
                res["essais_joues"] = "visés, puis les six fichiers"
    finally:
        for fichier, (octets, empreinte) in originaux.items():
            (copie / fichier).write_bytes(octets)
            if sha(copie / fichier) != empreinte:
                raise SystemExit(f"{ident} : {fichier} non rendu à l'octet")
    return {"id": ident, "defaut": quoi, **res}


def main(argv) -> int:
    import os

    copie, python, basetemp, sortie = Path(argv[0]), argv[1], Path(argv[2]), Path(argv[3])
    choisies = [m for m in MUTATIONS if not argv[4:] or m[0] in argv[4:]]
    # MUTATIONS_FICHIERS_VISES (liste séparée par des virgules) : rejoue les mutations choisies contre ces seuls fichiers
    # d'essais, sans repli sur les six (pour montrer qu'un essai de comportement, et non seulement un contrôle du texte,
    # attrape le défaut)
    vises = [x for x in os.environ.get("MUTATIONS_FICHIERS_VISES", "").split(",") if x]
    if vises:
        choisies = [(i, q, vises, r) for i, q, _, r in choisies]
        global ESSAIS
        ESSAIS = vises
    empreintes = {f: sha(copie / f) for f in (F, E, G, A)}
    anciens = json.loads(sortie.read_text(encoding="utf-8")) if sortie.exists() else []
    for m in choisies:
        r = jouer(copie, python, basetemp, m)
        anciens = [x for x in anciens if x["id"] != r["id"]] + [r]
        sortie.write_text(json.dumps(sorted(anciens, key=lambda x: x["id"]), indent=1, ensure_ascii=False) + "\n",
                          encoding="utf-8")
        print(r["id"], "ERREUR " + r["erreur"] if "erreur" in r else ("ATTRAPÉE" if r["attrapee"] else "MANQUÉE"), "|",
              r.get("compte", ""), "|", r.get("essais_joues", ""), "|", r.get("duree_s", ""), "s |", r["defaut"], flush=True)
        for e in (r.get("echecs", []) + r.get("erreurs", []))[:4]:
            print("     ", e, flush=True)
    assert {f: sha(copie / f) for f in (F, E, G, A)} == empreintes, "copie de travail non rendue à son état d'origine"
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
