#!/usr/bin/env python3
"""Mutants du contre-lecteur (modèle B) rejoués par lui-même sur l'outil du lecteur v3.1, plus dix-neuf mutants neufs.

Série A : les vingt et un mutants de la contre-lecture de la v3 (`../contre-lecture-lecture-classement-v3-outils/
mutations_contre_lecture_v3.py`, `4ac0ec0f…`, chargé tel quel) ; seize appliqués mot pour mot, cinq traduits (table
`TRADUITS` ci-dessous : la ligne visée a changé en v3.1, l'intention est gardée ; traductions relues contre celles de
l'auteur, égales). Série N : dix-neuf mutants neufs sur ce que la v3.1 ajoute (palier Flex et sa vérification, refus
d'un second dossier, dépense antérieure, planchers de l'usage, filtre de la clé, redirection, provenance des réponses).

Chaque mutant : copie de l'outil et du classement v3.1 dans le bloc-notes, une seule chaîne (présente exactement une
fois) remplacée, essais de l'auteur (`essais_lecture_classement_v3_1.py`, lus dans le dépôt) joués contre elle sous
`unshare -n`, environnement réduit à PATH, HOME, TMPDIR.

    .venv/bin/python -B mutations_relecture_courte_v3_1.py A|N DOSSIER_BLOC_NOTES SORTIE.json
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
V31 = ICI.parent / "lecture-classement-v3-1"
RACINE = ICI.parents[3]
OUTIL, CLASSER = "outil_lecteur_conception_propre_v3_1.py", "classer_conception_propre_v3_1.py"
ESSAIS = V31 / "essais_lecture_classement_v3_1.py"

_spec = importlib.util.spec_from_file_location(
    "mutants_v3", ICI.parent / "contre-lecture-lecture-classement-v3-outils" / "mutations_contre_lecture_v3.py")
_m = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_m)

TRADUITS = {
    "D4": ('a = analyser_reponse(statut, rep, pire, prix, len(corps), palier)',
           'a = analyser_reponse(statut, rep, 0.0 if statut is None else pire, prix, len(corps), palier)'),
    "D6": ('    if not nombre_fini(plafond) or plafond <= 0 or plafond > PLAFOND_ABSOLU_USD - anterieure + 1e-9:\n'
           '        raise Refus("manifeste : plafond hors des bornes du code (C4)")\n'
           '    if type(appels_max) is not int or appels_max > MAX_APPELS or appels_max != len(envois):\n',
           '    if False:\n        raise Refus("manifeste : plafond hors des bornes du code (C4)")\n    if False:\n'),
    "D7": ('    if prix != {**PRIX_LUS[palier], "source": SOURCE_PRIX}:\n', '    if False:\n'),
    "D9": ('            ajouter_journal(dossier, j, {"evenement": "arret", "motif": "plafond", "detail": detail}, cle)\n',
           '            pass\n'),
    "C3": ('return x if isinstance(x, str) and re.fullmatch(r"[a-z_]{1,64}", x) else None',
           'return x if isinstance(x, str) else None'),
}
SERIE_A = [(c, g, n + (" [traduit]" if c in TRADUITS else ""), *(TRADUITS.get(c, (a, b))))
           for c, g, n, a, b in _m.MUTANTS]

SERIE_N = [
    # --- palier Flex et sa vérification
    ("N1", "palier", "Flex : `service_tier` non envoyé (prix Flex compté, palier standard servi)",
     '    if SERVICE_TIER[palier] is not None:\n        c["service_tier"]', '    if False:\n        c["service_tier"]'),
    ("N2", "palier", "Flex : palier servi « default » accepté à l'envoi et à la vérification",
     '"flex": ("flex",)}', '"flex": ("flex", "default")}'),
    ("N3", "palier", "Flex : palier servi absent accepté",
     '"flex": ("flex",)}', '"flex": ("flex", None)}'),
    ("N4", "palier", "vérification : palier servi non contrôlé (l'envoi le contrôle encore)",
     '    if r.get("service_tier") not in PALIERS_SERVIS_ADMIS.get(palier, ()):', '    if False:'),
    ("N5", "palier", "prix de sortie Flex divisé par dix dans le code (25 → 2,5)",
     '"flex": {"entree": 5.0, "cache": 0.5, "sortie": 25.0}}', '"flex": {"entree": 5.0, "cache": 0.5, "sortie": 2.5}}'),
    # --- refus du second dossier, dépense antérieure
    ("N6", "second dossier", "unicité : seuls les manifestes v3.1 sont cherchés (un dossier v3 passe)",
     'rglob("manifeste-envois-v3*.json")', 'rglob("manifeste-envois-v3-1.json")'),
    ("N7", "second dossier", "unicité : `runs/` n'est plus fouillé",
     'for base in ("docs", "runs") if', 'for base in ("docs",) if'),
    ("N8", "second dossier", "unicité non contrôlée au chargement (envoi, bilan, vérification)",
     '    verifier_unicite(racine, d / MANIFESTE)\n', '    pass\n'),
    ("N9", "second dossier", "chemin fixe : seul le dernier nom (« envois ») est contrôlé",
     '    if d.parts[-len(parties):] != parties:', '    if d.name != parties[-1]:'),
    ("N10", "second dossier", "préparation : dépense antérieure non retranchée du plafond permis",
     'disponible = PLAFOND_ABSOLU_USD - depense_anterieure_usd', 'disponible = PLAFOND_ABSOLU_USD'),
    ("N11", "second dossier", "envoi : dépense antérieure non retranchée du plafond permis",
     'plafond > PLAFOND_ABSOLU_USD - anterieure + 1e-9', 'plafond > PLAFOND_ABSOLU_USD + 1e-9'),
    # --- planchers de l'usage
    ("N12", "usage", "plancher dix fois plus lâche (160 octets par jeton)",
     'PLANCHER_OCTETS_PAR_JETON = 16 ', 'PLANCHER_OCTETS_PAR_JETON = 160 '),
    ("N13", "usage", "plancher de la sortie visible : le raisonnement compte comme visible",
     '    elif c - raison < plancher_visible:', '    elif c < plancher_visible:'),
    ("N14", "usage", "total sous la somme accepté",
     '    elif total < p + c:\n', '    elif False:\n'),
    # --- filtre de la clé
    ("N15", "clé", "filtre : l'espace est admis dans la clé",
     r'MOTIF_CLE = re.compile(r"[\x21-\x7e]{1,512}")', r'MOTIF_CLE = re.compile(r"[\x20-\x7e]{1,512}")'),
    ("N16", "clé", "filtre : début de clé seul contrôlé (`match` au lieu de `fullmatch` ; une fin de ligne passe)",
     '    if not MOTIF_CLE.fullmatch(cle):', '    if not MOTIF_CLE.match(cle):'),
    ("N17", "clé", "réponse 200 écrite sans expurger la clé",
     '            brut, expurgee = expurger(rep, cle)\n', '            brut, expurgee = rep, False\n'),
    # --- redirection, provenance
    ("N18", "redirection", "gestionnaire sans redirection retiré (seul le contrôle de l'adresse finale reste)",
     'build_opener(SansRedirection, urllib.request.HTTPSHandler(context=contexte))',
     'build_opener(urllib.request.HTTPSHandler(context=contexte))'),
    ("N19", "provenance", "vérification : confrontation journal-dossier retirée (reste l'exigence de clôture par réponse)",
     '    controler_coherence(dossier, env["manifeste"], journal)  # M1', '    pass  # M1'),
]


def jouer(modules: Path, tmp: Path, delai=1200) -> tuple[bool, str]:
    env = {"PATH": os.environ["PATH"], "HOME": os.environ.get("HOME", "/root"), "TMPDIR": str(tmp),
           "LC_MODULES": str(modules), "PYTHONDONTWRITEBYTECODE": "1"}
    c = subprocess.run(["unshare", "-n", sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider",
                        "--basetemp", str(tmp / "pytest"), str(ESSAIS)],
                       capture_output=True, text=True, env=env, timeout=delai, cwd=str(RACINE))
    lignes = c.stdout.strip().splitlines() or [""]
    echec = next((l for l in lignes if l.startswith("FAILED") or l.startswith("ERROR")), "")
    return c.returncode == 0, (lignes[-1] + (" | " + echec[:220] if echec else ""))


def main(serie: str, bloc: str, sortie: str) -> int:
    mutants = {"A": SERIE_A, "N": SERIE_N}[serie]
    bloc = Path(bloc) / f"relecture-{serie}"
    if bloc.exists():
        shutil.rmtree(bloc)
    debut = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    base = bloc / "base" / "docs" / "notes" / "o" / "lecture-classement-v3-1"
    base.mkdir(parents=True)
    for n in (OUTIL, CLASSER):
        shutil.copyfile(V31 / n, base / n)
    tmp = bloc / "tmp"
    tmp.mkdir()
    ok, ligne_base = jouer(base, tmp)
    if not ok:
        print("la base échoue : " + ligne_base, file=sys.stderr)
        return 1
    print("base : " + ligne_base, flush=True)
    res = []
    for code, garde, nom, ancien, nouveau in mutants:
        d = bloc / code / "docs" / "notes" / "o" / "lecture-classement-v3-1"
        shutil.copytree(base, d)
        texte = (d / OUTIL).read_text(encoding="utf-8")
        if texte.count(ancien) != 1:
            res.append({"mutant": code, "garde": garde, "nom": nom, "statut": "inapplicable",
                        "occurrences": texte.count(ancien)})
            print(f"{code} INAPPLICABLE ({texte.count(ancien)}) — {nom}", flush=True)
            continue
        (d / OUTIL).write_text(texte.replace(ancien, nouveau), encoding="utf-8")
        survit, ligne = jouer(d, tmp)
        res.append({"mutant": code, "garde": garde, "nom": nom, "ancien": ancien, "nouveau": nouveau,
                    "statut": "survivant" if survit else "tue", "sortie": ligne})
        print(f"{code} {'SURVIT' if survit else 'tué'} — {nom}", flush=True)
        shutil.rmtree(bloc / code)
    out = {"banc": f"mutations de la relecture courte v3.1, série {serie} (contre-lecteur, modèle B)",
           "outil_sha256": __import__("hashlib").sha256((V31 / OUTIL).read_bytes()).hexdigest(),
           "debut_utc": debut, "fin_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": ligne_base,
           "isolement": "unshare -n (espace de noms réseau vide) ; environnement : PATH, HOME, TMPDIR",
           "mutants": len(mutants), "tues": sum(r["statut"] == "tue" for r in res),
           "survivants": [f"{r['mutant']} — {r['nom']}" for r in res if r["statut"] == "survivant"],
           "inapplicables": [r["mutant"] for r in res if r["statut"] == "inapplicable"], "detail": res}
    Path(sortie).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{out['tues']} tués sur {len(mutants)} ; survivants : {len(out['survivants'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
