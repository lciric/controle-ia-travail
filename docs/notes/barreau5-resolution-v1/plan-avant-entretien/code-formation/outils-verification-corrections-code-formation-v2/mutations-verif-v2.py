"""Contrôle par mutation du code de formation du barreau 5 après les tours 2 et 3 — outil du contre-lecteur (Fable 5.2)
pour la seconde vérification, v2, 20 novembre 2026.

Il reprend telle quelle la logique de `mutations-verif-v1.py` (une seule copie de travail hors du dépôt ; chaque mutation
posée, jouée sur les six fichiers d'essais avec arrêt au premier échec, retirée, fichier rendu à l'octet) et sa liste de 29
mutations (les vingt de la contre-lecture, B1, V01 à V08), dont l'« avant » est repris sur le code du commit ef8008682 quand
il a changé (M16), et ajoute cinq mutations neuves (W01 à W05) sur le code du troisième tour : paliers, part par motif,
relance, nom de carte, marqueur.

Usage : python mutations-verif-v2.py OUTIL_V1 COPIE PYTHON SORTIE.json [identifiants …]
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path


def charger(chemin: str):
    spec = importlib.util.spec_from_file_location("mutations_verif_v1", chemin)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(argv) -> int:
    v1 = charger(argv[0])
    copie, python, sortie = Path(argv[1]), argv[2], Path(argv[3])
    v1.TMP = "/dev/shm/b5f-verif2-mutations"
    F, E, A, TE, TF, TL = v1.F, v1.E, v1.A, v1.TE, v1.TF, v1.TL
    reprises = {
        "M16": ("part d'actions non éditables admise jusqu'à 50 % (« avant » repris : le seuil est à 25 % depuis le tour 3)",
                TE, [(E, "PART_NON_EDITABLE_MAX = 0.25 ", "PART_NON_EDITABLE_MAX = 0.50 ")]),
    }
    neuves = [
        ("W01", "(a) paliers : une part de 25 % juste est refusée (borne haute devenue stricte)", TE,
         [(E, "    if part > PART_NON_EDITABLE_MAX:\n", "    if part >= PART_NON_EDITABLE_MAX:\n")]),
        ("W02", "(a) part par motif rapportée à la part des actions non éditables, et non à toutes les actions (la somme "
                "ne fait plus la part)", TE,
         [(E, "    par_motif = {k: sum(1 for a in lignes if not a[\"editable\"] and a.get(\"classe\") == k) / len(lignes)\n",
           "    par_motif = {k: sum(1 for a in lignes if not a[\"editable\"] and a.get(\"classe\") == k) / max(1, non_ed)\n")]),
        ("W03", "(c) relance : l'enveloppe de 56 USD comparée aux coupures à deux membres, quel que soit le nombre de "
                "membres de SCELLEMENT-B5F", TF,
         [(F, "        somme = sum(coupure_usd(n, int(s[\"membres\"])) for n in instances)\n",
           "        somme = sum(COUPURES_USD[n] for n in instances)\n")]),
        ("W04", "(d) nom de carte : le suffixe « k » lu par le lecteur gelé compte pour une lettre collée (« 3k » suivi "
                "d'un nom de carte : la règle ne joue plus)", TE,
         [(E, "    apres = texte[nb.end()] if nb.end() < len(texte) else \"\"\n",
           "    apres = texte[nb.end(\"n\")] if nb.end(\"n\") < len(texte) else \"\"\n")]),
        ("W05", "(a) marqueur « part non éditable haute » recopié du premier tirage, et non du tirage formé (faux après un "
                "retirage)", TF,
         [(F, "    statut[\"part_non_editable_haute\"] = bool(info[\"controle\"][\"part_non_editable_haute\"])\n",
           "    statut[\"part_non_editable_haute\"] = bool(statut[\"tirages\"][0][\"controle\"][\"part_non_editable_haute\"])\n")]),
    ]
    liste = [(i, *reprises[i]) if i in reprises else (i, q, t, r) for i, q, t, r in v1.MUTATIONS] + neuves
    choisies = [m for m in liste if not argv[4:] or m[0] in argv[4:]]
    avant = {f: v1.sha(copie / f) for f in (v1.F, v1.E, v1.G, v1.A)}
    for m in choisies:
        r = v1.jouer(copie, python, m)
        r["fichiers_rendus_a_l_octet"] = {f: v1.sha(copie / f) for f in (v1.F, v1.E, v1.G, v1.A)} == avant
        anciens = json.loads(sortie.read_text(encoding="utf-8")) if sortie.exists() else []
        sortie.write_text(json.dumps([x for x in anciens if x["id"] != r["id"]] + [r], indent=1, ensure_ascii=False) + "\n",
                          encoding="utf-8")
        print(r["id"], "ERREUR " + r["erreur"] if "erreur" in r else ("ATTRAPÉE" if r["attrapee"] else "MANQUÉE"), "|",
              r.get("compte", ""), "|", (r.get("premier_echec") or ["—"])[0], "|", r["defaut"][:90], flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
