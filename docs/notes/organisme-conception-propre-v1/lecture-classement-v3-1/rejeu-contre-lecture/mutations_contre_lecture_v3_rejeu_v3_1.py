#!/usr/bin/env python3
"""Mutants du contre-lecteur (modèle B) — outil du lecteur v3, course « conception propre » — REJEU SUR LA v3.1.

Copie adaptée par l'auteur de la v3.1 (modèle A) de `contre-lecture-lecture-classement-v3-outils/mutations_contre_lecture_v3.py`
(`4ac0ec0f…`, non modifié), pour rejouer les mêmes vingt et un mutants sur l'outil v3.1 contre les essais v3.1.
Adaptations, et seulement elles (différentiel entier : `differentiel-mutations-contre-lecture-rejeu.diff`) :
- chemins : dossier `lecture-classement-v3-1`, fichiers `…_v3_1.py`, essais `essais_lecture_classement_v3_1.py` ;
- cinq mutants **traduits** parce que la ligne visée a changé en v3.1, l'intention gardée :
  D4 (appel d'`analyser_reponse` à deux arguments de plus), D6 (bornes revérifiées dans `valider_manifeste`, deux
  contrôles au lieu d'un), D7 (prix revérifiés par égalité aux prix lus, au lieu de `prix_valides`), D9 (écriture au
  journal avec la clé à expurger en dernier argument), C3 (filtre des codes d'erreur resserré à `[a-z_]{1,64}`) ;
  les seize autres sont appliqués mot pour mot ;
- sortie : `resultat-mutations-contre-lecture-rejeu-v3-1.json`.

Texte d'origine :

Vingt et un mutants écrits par le contre-lecteur, qui n'a écrit ni l'outil ni ses essais, sur les gardes de dépense, de
fin, de modèle servi, de clé, de reprise et de corps d'erreur. Chacun est une copie de l'outil et du classement v3 dans un
dossier du bloc-notes, hors du dépôt, où une seule chaîne (présente exactement une fois) est remplacée ; les essais de
l'auteur (`essais_lecture_classement_v3.py`, lus dans le dépôt, non modifiés) sont joués contre lui par `LC_MODULES`.
Un mutant est « tué » si les essais échouent, « survivant » s'ils passent tous.

Hors réseau, par construction : chaque passe tourne dans un espace de noms réseau vide (`unshare -n` : aucune interface,
aucun paquet ne peut sortir), environnement réduit à PATH, HOME, TMPDIR (aucune clé, aucun mandataire).

    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B mutations_contre_lecture_v3.py DOSSIER_BLOC_NOTES SORTIE.json
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
V3 = ICI.parent  # v3.1 : dossier lecture-classement-v3-1
RACINE = ICI.parents[4]
OUTIL, CLASSER = "outil_lecteur_conception_propre_v3_1.py", "classer_conception_propre_v3_1.py"
ESSAIS = V3 / "essais_lecture_classement_v3_1.py"

MUTANTS = [
    # --- garde de dépense
    ("D1", "dépense", "plafond dépassable de 0,50 USD",
     'if j["depense_usd"] + pire > plafond + 1e-12:', 'if j["depense_usd"] + pire > plafond + 0.5:'),
    ("D2", "dépense", "pire cas non recalculé sur les octets envoyés (valeur du manifeste seule)",
     'pire = max(e["pire_cas_usd"], pire_cas_usd(len(corps), prix))', 'pire = e["pire_cas_usd"]'),
    ("D3", "dépense", "usage incohérent compté au coût lu, non au pire cas",
     'r["cout_usd"], r["au_pire_cas"] = max(cout, pire_cas), cout <= pire_cas',
     'r["cout_usd"], r["au_pire_cas"] = cout, False'),
    ("D4", "dépense", "échec de transport (coupure, délai) compté zéro [traduit v3.1]",
     'a = analyser_reponse(statut, rep, pire, prix, len(corps), palier)',
     'a = analyser_reponse(statut, rep, 0.0 if statut is None else pire, prix, len(corps), palier)'),
    ("D5", "dépense", "réponse 200 illisible (page de passerelle) comptée zéro",
     '    if not isinstance(o, dict):\n        r["anomalies"].append("reponse_illisible")\n        return r',
     '    if not isinstance(o, dict):\n        r["anomalies"].append("reponse_illisible")\n        r["cout_usd"] = 0.0\n'
     '        return r'),
    ("D6", "dépense", "bornes du code (14,20 USD, 18 appels) non revérifiées à l'envoi [traduit v3.1]",
     '    if not nombre_fini(plafond) or plafond <= 0 or plafond > PLAFOND_ABSOLU_USD - anterieure + 1e-9:\n'
     '        raise Refus("manifeste : plafond hors des bornes du code (C4)")\n'
     '    if type(appels_max) is not int or appels_max > MAX_APPELS or appels_max != len(envois):\n',
     '    if False:\n        raise Refus("manifeste : plafond hors des bornes du code (C4)")\n    if False:\n'),
    ("D7", "dépense", "prix du manifeste non revalidés à l'envoi [traduit v3.1]",
     '    if prix != {**PRIX_LUS[palier], "source": SOURCE_PRIX}:\n', '    if False:\n'),
    ("D8", "dépense", "garde du nombre d'appels décalée d'un",
     'if j["appels"] >= appels_max:', 'if j["appels"] > appels_max:'),
    ("D9", "dépense", "arrêt au plafond non consigné au journal [traduit v3.1]",
     '            ajouter_journal(dossier, j, {"evenement": "arret", "motif": "plafond", "detail": detail}, cle)\n',
     '            pass\n'),
    # --- fin et forme de la réponse
    ("F1", "fin", "vérification : seule la fin « length » bloque (content_filter, tool_calls, absente passent)",
     'if c0 and c0.get("finish_reason") != "stop":', 'if c0 and c0.get("finish_reason") == "length":'),
    ("F2", "fin", "envoi : plusieurs choix acceptés (le premier lu)",
     'if not isinstance(ch, list) or len(ch) != 1 or not isinstance(ch[0], dict):\n        r["anomalies"].append("choix_non_unique")',
     'if not isinstance(ch, list) or len(ch) < 1 or not isinstance(ch[0], dict):\n        r["anomalies"].append("choix_non_unique")'),
    ("F3", "fin", "envoi : contenu absent ou vide ignoré (le lot suivant part)",
     '        r["anomalies"].append("contenu_absent")', '        pass'),
    ("F4", "fin", "envoi : objet autre que chat.completion accepté",
     '    if o.get("object") != "chat.completion":\n        r["anomalies"].append("reponse_illisible")',
     '    if False:\n        r["anomalies"].append("reponse_illisible")'),
    # --- modèle servi
    ("M1", "modèle servi", "envoi : espaces de fin tolérés dans le nom servi",
     'if r["modele_servi"] != MODELE_LECTEUR:', 'if (r["modele_servi"] or "").rstrip() != MODELE_LECTEUR:'),
    ("M2", "modèle servi", "vérification : nom servi comparé sans la casse",
     'if r.get("model") != MODELE_LECTEUR:', 'if str(r.get("model")).lower() != MODELE_LECTEUR:'),
    # --- clé
    ("C1", "clé", "repli vers une autre variable (os.getenv, invisible au compte des accès à os.environ)",
     'cle = os.environ.pop(VARIABLE_CLE, None)', 'cle = os.environ.pop(VARIABLE_CLE, None) or os.getenv("OPENAI_KEY")'),
    ("C2", "clé", "clé vide acceptée (en-tête « Bearer » nu)",
     '    if not cle:\n        raise Refus(f"{VARIABLE_CLE} absente', '    if cle is None:\n        raise Refus(f"{VARIABLE_CLE} absente'),
    ("C3", "clé", "type et code d'erreur du fournisseur écrits sans filtre [traduit v3.1]",
     'return x if isinstance(x, str) and re.fullmatch(r"[a-z_]{1,64}", x) else None',
     'return x if isinstance(x, str) else None'),
    # --- reprise
    ("R1", "reprise", "reprise permise après un arrêt au plafond",
     'if j["anomalies"] or j["arret"]:', 'if j["anomalies"]:'),
    ("R2", "reprise", "reprise permise après une anomalie autre que la fin (modèle servi, usage, statut, transport)",
     'if j["anomalies"] or j["arret"]:',
     'if any(a["genre"] == "fin_non_stop" for a in j["anomalies"]) or j["arret"]:'),
    ("R3", "reprise", "journal : un même envoi consigné deux fois n'est pas refusé",
     'if ev["envoi"] in ouverts or ev["envoi"] in etat["clos"]:', 'if False:'),
]


def jouer(modules: Path, tmp: Path, delai=900) -> tuple[bool, str]:
    env = {"PATH": os.environ["PATH"], "HOME": os.environ.get("HOME", "/root"), "TMPDIR": str(tmp),
           "LC_MODULES": str(modules), "PYTHONDONTWRITEBYTECODE": "1"}
    c = subprocess.run(["unshare", "-n", sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                        "--basetemp", str(tmp / "pytest"), str(ESSAIS)],
                       capture_output=True, text=True, env=env, timeout=delai, cwd=str(RACINE))
    lignes = c.stdout.strip().splitlines() or [""]
    echec = next((l for l in lignes if l.startswith("FAILED") or l.startswith("ERROR")), "")
    return c.returncode == 0, (lignes[-1] + (" | " + echec[:200] if echec else ""))


def main(bloc: str, sortie: str) -> int:
    bloc = Path(bloc)
    debut = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    base = bloc / "mut-base" / "docs" / "notes" / "o" / "lecture-classement-v3"
    if base.exists():
        shutil.rmtree(bloc / "mut-base")
    base.mkdir(parents=True)
    for n in (OUTIL, CLASSER):
        shutil.copyfile(V3 / n, base / n)
    tmp = bloc / "mut-tmp"
    tmp.mkdir(exist_ok=True)
    ok, ligne_base = jouer(base, tmp)
    if not ok:
        print("la base échoue : " + ligne_base, file=sys.stderr)
        return 1
    res = []
    for code, garde, nom, ancien, nouveau in MUTANTS:
        d = bloc / f"mut-{code}" / "docs" / "notes" / "o" / "lecture-classement-v3"
        if d.exists():
            shutil.rmtree(bloc / f"mut-{code}")
        shutil.copytree(base, d)
        texte = (d / OUTIL).read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            res.append({"mutant": code, "garde": garde, "nom": nom, "statut": "inapplicable",
                        "occurrences": texte.count(ancien)})
            print(f"{code} INAPPLICABLE — {nom}", flush=True)
            continue
        (d / OUTIL).write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        survit, ligne = jouer(d, tmp)
        res.append({"mutant": code, "garde": garde, "nom": nom, "ancien": ancien, "nouveau": nouveau,
                    "statut": "survivant" if survit else "tue", "sortie": ligne})
        print(f"{code} {'SURVIT' if survit else 'tué'} — {nom}", flush=True)
        shutil.rmtree(bloc / f"mut-{code}")
    out = {"banc": "mutations-contre-lecture-v3 (contre-lecteur, modèle B), rejouées sur la v3.1 par son auteur", "debut_utc": debut,
           "fin_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": ligne_base,
           "isolement": "unshare -n (espace de noms réseau vide) ; environnement : PATH, HOME, TMPDIR",
           "mutants": len(MUTANTS), "tues": sum(r["statut"] == "tue" for r in res),
           "survivants": [f"{r['mutant']} — {r['nom']}" for r in res if r["statut"] == "survivant"],
           "inapplicables": [r["mutant"] for r in res if r["statut"] == "inapplicable"], "detail": res}
    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{out['tues']} tués sur {len(MUTANTS)} ; survivants : {len(out['survivants'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
