"""Génère les pièces de lancement de la confirmation (addendum 7) : conduite v15, poste v13, constructeur v13.
Usage : generer-v2.py <dossier de sortie> <GO_ID> <empreinte complète de l'addendum 7> <commit du code>
v2 : contrôles d'entrée de la conduite resserrés (empreinte entière de l'addendum 7 dans l'objet du GO ; commit du code
du manifeste v7) ; liste des répertoires de la sortie écrite, scellée et poussée par le poste avant sa marque de fin
(addendum 7, § 3) ; noms neufs pour tout fichier du poste (§ 6, étape 2).
v3 (contre-lecture des pièces, angle « exécution », point 1) : la fenêtre de 24 h sans offre conforme (addendum 7,
§ 2.4) est bornée en temps, et non plus seulement en essais : plus aucune recherche 23 h 45 après le début du script."""
import re, sys
from pathlib import Path
out, go_id, emp, commit = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")
assert re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id) and re.fullmatch(r"[0-9a-f]{64}", emp) and re.fullmatch(r"[0-9a-f]{40}", commit)

conduite = f'''"""v15 — RUN DE CONFIRMATION au régime complet (R12 ; v1 à v14 restent telles quelles ; addendum 7 du témoin de Bailey,
`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md`, `{emp[:8]}…`).

Conduite normale de `lanceur_v21` (mise en place, contrôle du juge, pilote, règle, run principal, relance du texte dans la
conduite), sur un poste neuf : aucune instance antérieure (D compte de zéro), B = 85 USD (manifeste v7), GO `{go_id}`,
garde de durée de tour du pilote à 1 800 s (addendum 7, § 2.3), aucune `relance_seule`. Elle ne diffère de la conduite
v13 que par cela, et par ses gardes d'entrée, jouées avant l'écriture du PID et avant toute création : addendum 7 scellé
à l'empreinte attendue ; ligne de GO qui cite cette empreinte entière ; manifeste v7 scellé, B = 85, GO et commit du code attendus ; plafond de
durée exactement 1 800 s. Sortie, bilan et PID neufs (`sortie-conduite-v15`, `bilan-lancement-v15.json`,
`lancement-v15.pid`). Elle ne lit aucune note.

Usage, détaché, depuis la racine du dépôt, sous `GO_ID={go_id}`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v15.py --offre <id> --image <image>
"""
import argparse
import json
import os
import shutil
import sys
import time
from pathlib import Path

from controle_ia import scellement
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey import lanceur_v21 as L

DEPOT = Path("/home/user/controle-ia-travail")
BASE = DEPOT / "runs" / "temoin-bailey-v1-20261111"
GO_ID = "{go_id}"
ADDENDUM_7 = DEPOT / "prereg" / "temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md"
EMPREINTE_ADDENDUM_7 = "{emp}"
MANIFESTE = BASE / "manifeste-local-v7.json"
COMMIT_CODE = "{commit}"  # addendum 7, § 4
B_ATTENDU = 85.0
T_MAX_PILOTE_S = 1800.0  # addendum 7, § 2.3
DISQUE_GO = 110  # disque demandé à Vast (Go)
ANTERIEURES: list = []  # poste neuf (addendum 7, § 2.2) : D compte de zéro


class FournisseurVastReprises(L.FournisseurVast):
    """Comme en v9 : `envoyer_fichier` retenté (`scp` en échec : 3 essais, 20 s d'écart) ; le dernier échec sort tel quel."""

    def envoyer_fichier(self, ident, local, distant):
        for n in range(3):
            try:
                return super().envoyer_fichier(ident, local, distant)
            except Exception:
                if n == 2:
                    raise
                time.sleep(20)


def gardes_d_entree(texte_go: str) -> None:
    """Avant l'écriture du PID et toute création ; lève `SystemExit` (rien ne tourne, aucune dépense)."""
    scellement.verifier(ADDENDUM_7)
    if cv.sha_fichier(ADDENDUM_7) != EMPREINTE_ADDENDUM_7:
        raise SystemExit("addendum 7 : empreinte différente de celle attendue : rien ne tourne")
    go = L.ligne_go(texte_go, GO_ID)
    if EMPREINTE_ADDENDUM_7 not in go["objet"]:
        raise SystemExit("la ligne de GO ne cite pas l'empreinte de l'addendum 7 : rien ne tourne")
    scellement.verifier(MANIFESTE)
    man = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    if float(man["B"]) != B_ATTENDU or man["go_id"] != GO_ID or man["commit_code"] != COMMIT_CODE:
        raise SystemExit("manifeste v7 : B, GO ou commit du code différents de ceux de l'addendum 7 : rien ne tourne")
    if T_MAX_PILOTE_S != 1800.0 or ANTERIEURES:
        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures : rien ne tourne")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--offre", required=True)
    p.add_argument("--image", required=True)
    a = p.parse_args()
    if os.environ.get("GO_ID") != GO_ID or os.environ.get("DEPOT_URL") != L.DEPOT_URL:
        print("GO_ID ou DEPOT_URL absent ou différent : rien ne tourne", file=sys.stderr)
        return 2
    manquants = [o for o in ("vastai", "ssh", "scp") if shutil.which(o) is None]
    if manquants:
        print(f"outils introuvables dans le PATH : {{manquants}} : rien ne tourne", file=sys.stderr)
        return 2
    texte_go = L.texte_go_main(DEPOT)
    gardes_d_entree(texte_go)
    pidf = BASE / "lancement-v15.pid"
    sortie = BASE / "sortie-conduite-v15"  # chemin absolu, le même pour `reprendre` (A-1)
    trace = BASE / "bilan-lancement-v15.json"
    if pidf.exists() or trace.exists():
        print("PID ou bilan de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    pidf.write_text(f"{{os.getpid()}}\\n", encoding="utf-8")
    conduite = L.Conduite(fournisseur=FournisseurVastReprises(), manifeste_local=MANIFESTE, sortie=sortie, go_id=GO_ID,
                          texte_go=texte_go, offre=str(a.offre), image=a.image, depot_local=DEPOT,
                          instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S)
    if conduite.relance_seule is not None or conduite.t_max_pilote_s != 1800.0:
        print("conduite mal construite : rien ne tourne", file=sys.stderr)
        return 2
    debut = time.time()
    try:
        bilan = conduite.conduire()
        issue = {{"bilan": bilan}}
    except Exception as err:  # la conduite a déjà fait `_finir` ; on consigne l'erreur sans valeur de note
        issue = {{"erreur": f"{{type(err).__name__}}: {{err}}"[:500]}}
    issue.update({{"offre": a.offre, "image": a.image, "debut": debut, "fin": time.time(), "pid": os.getpid()}})
    trace.write_text(json.dumps(issue, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\\n",
                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''
(out / "lancer-conduite-v15.py").write_text(conduite, encoding="utf-8")

p = (base / "poste-hetzner-v12.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n# Poste Hetzner du témoin de Bailey, v12 — RELANCE SEULE"
assert p.startswith(h)
p = ("#!/bin/bash\n# Poste Hetzner du témoin de Bailey, v13 — RUN DE CONFIRMATION (R12 ; v1 à v12 restent telles quelles ; addendum 7).\n"
     "# v13 = v12 avec la conduite v15 (`lanceur_v21`, conduite normale, B = 85), le manifeste v7, la garde du commit du code\n"
     f"# {commit[:8]}, et le filtre d'offre de l'addendum 7, § 2.4 : `cpu_cores_effective>=32 cpu_ghz>=2.4` à la recherche, et un\n"
     "# coût (carte et 110 Go de stockage) d'au plus 1,6 USD/h au choix.\n# v12 — RELANCE SEULE" + p[len(h):])
n = 0
for a, b in (("sortie-conduite-v13", "sortie-conduite-v15"), ("lancement-v13", "lancement-v15"),  # couvre aussi bilan-lancement-v13
             ("lancer-conduite-v13", "lancer-conduite-v15"), ("offre-choisie-v12", "offre-choisie-v13"), ("poste-fini-v12", "poste-fini-v13"),
             ("poste-hetzner-v12", "poste-hetzner-v13"), ("manifeste-local-v6.json.sha256", "manifeste-local-v7.json.sha256")):
    corps = p.split("\nset -uo pipefail", 1)
    k = corps[1].count(a); assert k >= 1, a
    p = corps[0] + "\nset -uo pipefail" + corps[1].replace(a, b); n += k
ancien = "f60c2620a3891ebe579a807b2a90afb06e9e3ea5"
corps = p.split("\nset -uo pipefail", 1)
assert corps[1].count(ancien) == 2 and corps[1].count("f60c2620 ") + corps[1].count("f60c2620 :") >= 2
corps[1] = corps[1].replace(ancien, commit).replace("commit du code f60c2620", f"commit du code {commit[:8]}").replace("du commit f60c2620", f"du commit {commit[:8]}")
assert "f60c2620" not in corps[1], [l for l in corps[1].splitlines() if "f60c2620" in l]
a = "GO_ID=GO-2026-11-10-10"
assert corps[1].count(a) >= 1
corps[1] = corps[1].replace(a, f"GO_ID={go_id}")
a = "cpu_ram>=128.9 disk_space>=115 reliability>0.97 cuda_vers>=12.4 direct_port_count>=1 rentable=true'"
assert corps[1].count(a) == 1
corps[1] = corps[1].replace(a, a[:-1] + " cpu_cores_effective>=32 cpu_ghz>=2.4'")
a = "if not d:\n    sys.exit(1)\n"
assert corps[1].count(a) == 1
corps[1] = corps[1].replace(a, "d = [o for o in d if cout(o) <= 1.6]  # v13 : plafond de coût, carte et 110 Go (addendum 7, § 2.4)\nif not d:\n    sys.exit(1)\n")
p = corps[0] + "\nset -uo pipefail" + corps[1]
LISTE = "repertoires-sortie-conduite-v15-v1.txt"  # addendum 7, § 3 : <C> = sortie-conduite-v15
a = '"$BASE"/poste-hetzner-v13-etat.txt; do'
assert p.count(a) == 1
p = p.replace(a, '"$BASE"/poste-hetzner-v13-etat.txt "$BASE"/' + LISTE + ' "$BASE"/' + LISTE + '.sha256; do')
a = 'etat "conduite terminée"\n'
assert p.count(a) == 1
p = p.replace(a, a + (
    "# v13 : liste de tous les répertoires de la sortie (addendum 7, § 3), hors de la sortie, avant la marque de fin\n"
    'if [ -d "$BASE/sortie-conduite-v15" ]; then\n'
    '  (cd "$BASE/sortie-conduite-v15" && find . -mindepth 1 -type d -printf \'%P\\n\' | LC_ALL=C sort > "$BASE/' + LISTE + '")\n'
    '  (cd "$BASE" && [ -f ' + LISTE + ' ] && LC_ALL=C sha256sum ' + LISTE + ' > ' + LISTE + '.sha256)\n'
    '  etat "liste des répertoires écrite : $(wc -l < "$BASE/' + LISTE + '" 2>/dev/null) entrées"\n'
    'else\n'
    '  etat "sortie de la conduite absente : aucune liste des répertoires"\n'
    'fi\n'
    'pousser "liste des répertoires de la sortie"\n'))
a = 'echo "début $(date -u +%FT%TZ)"\n'
assert p.count(a) == 1
p = p.replace(a, a + "DEBUT_POSTE=$(date -u +%s)  # v13 : fenêtre de 24 h du § 2.4 bornée en temps\n")
a = "for n in $(seq 1 144); do\n"
assert p.count(a) == 1
p = p.replace(a, a + "  [ $(( $(date -u +%s) - DEBUT_POSTE )) -lt 85500 ] || break  # v13 : 23 h 45 après le début du script\n")
(out / "poste-hetzner-v13.sh").write_text(p, encoding="utf-8")

c = (base / "construire-donnees-demarrage-v12.py").read_text(encoding="utf-8")
c = c.replace("v12 (R12 ; v1 à v11 restent telles\nquelles). v12 = v11", "v13 (R12 ; v1 à v12 restent telles\nquelles). v13 = v12", 1)
for a, b in (('"poste-hetzner-v12.sh"', '"poste-hetzner-v13.sh"'), ("(`poste-hetzner-v12.sh`)", "(`poste-hetzner-v13.sh`)"),
             ('"poste-temoin-bailey-v12"', '"poste-temoin-bailey-v13"'), ('"temoin-bailey-v12"}', '"temoin-bailey-v13"}')):
    assert c.count(a) == 1, a; c = c.replace(a, b)
(out / "construire-donnees-demarrage-v13.py").write_text(c, encoding="utf-8")
print("remplacements de noms dans le poste :", n)
