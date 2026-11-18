"""Génère les pièces de la RELANCE de la confirmation du témoin de Bailey (addendum 7, § 2.1 : relance de la liste
d'arrêt, texte l. 371, par le chemin de l'addendum 5 quand l'instance est perdue) : conduite v16 (relance seule,
`lanceur_v21`), poste v14, constructeur v14 (R12 ; les versions antérieures restent telles quelles).

Les valeurs propres à la première exécution ne sont connues qu'après la reprise (lecture 38) ; elles sont passées en
arguments et vérifiées par la conduite avant toute création :
  generer-pieces-relance-confirmation-bailey-v1.py <sortie> <GO_ID> <empreinte addendum 7> <commit du code>
      <dossier de reprise, ex. reprise-v10> <K′ de la première exécution> <destruction de 61049303, époque>
Champs lus pour les fixer (techniques seulement, § 3) : nombre de lignes du journal des durées transféré par la reprise,
heure de destruction écrite par la reprise dans `sortie-conduite-v15/poste-v5.json` ; aucune note.

Conduite v16 = conduite v15 (gardes d'entrée de l'addendum 7) + `relance_seule()` de la conduite v13 (addendum 5),
portée sur `sortie-conduite-v15/<reprise>` et l'instance 61049303 : instance antérieure unique (le poste de dépense de
la confirmation, D cumulée, même B = 85), t du pilote de la première exécution, aucun pilote ni règle sur l'instance
neuve. Poste v14 = poste v13 avec la conduite v16 et des noms neufs (sortie `sortie-conduite-v16`, liste
`repertoires-sortie-conduite-v16-v1.txt`)."""
import re, sys
from pathlib import Path
out, go_id, emp, commit, reprise, k1, destr = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6]), float(sys.argv[7])
assert re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id) and re.fullmatch(r"[0-9a-f]{64}", emp) and re.fullmatch(r"[0-9a-f]{40}", commit)
assert re.fullmatch(r"reprise-v10(-\d+)?", reprise) and 0 <= k1 < 20 and destr > 1794907209.2755258
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")

c15 = (base / "lancer-conduite-v15.py").read_text(encoding="utf-8")
i = c15.index('"""', 3)
doc = f'''"""v16 — RELANCE de la confirmation (R12 ; v1 à v15 restent telles quelles ; addendum 7, § 2.1, par le chemin de
l'addendum 5 : relance seule, pièces neuves contre-lues). La première exécution du run principal de la confirmation
(conduite v15, instance 61049303) s'est interrompue avant 20 tours complets (K′ = {k1}) : compte Vast sans crédit, instance
arrêtée par Vast le 17 novembre vers 17:12Z ; reprise faite (`sortie-conduite-v15/{reprise}/`). Conduite `lanceur_v21` avec
`relance_seule` : amorce, auto-arrêt, mise en place et contrôle du juge sur une instance neuve, puis, sans pilote ni règle
sur l'instance, K recalculé par la règle (même B = 85, D du poste, c de l'instance neuve, t du pilote de la première
exécution) et `principal-relance`. Instance antérieure : 61049303 (création relevée par la conduite v15, destruction
écrite par la reprise). Gardes d'entrée de la v15 (addendum 7 scellé, GO qui cite son empreinte entière, manifeste v7),
plus celles de la relance : empreintes du manifeste de la règle et du journal des durées de la reprise, exactement
{k1} lignes de durées (tours 0 à {k1 - 1}), gardes tombées lues sans note. Sortie, bilan et PID neufs (`sortie-conduite-v16`,
`bilan-lancement-v16.json`, `lancement-v16.pid`). Elle ne lit aucune note.

Usage, détaché, depuis la racine du dépôt, sous `GO_ID={go_id}`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py --offre <id> --image <image>
"""'''
c = doc + c15[i + 3:]
def rep(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:70], c.count(a)); c = c.replace(a, b)
rep('ANTERIEURES: list = []  # poste neuf (addendum 7, § 2.2) : D compte de zéro',
    f'''# Instance de la première exécution (conduite v15) : création relevée par la conduite v15
# (`sortie-conduite-v15/poste-v5.json`), destruction écrite par la reprise ; même poste de dépense (addendum 7, § 2.2).
ANTERIEURES = [{{"id": "61049303", "c": 1.3247777777777778, "creation": 1794907209.2755258,
                "destruction": {destr!r}, "B": 85.0}}]
REPRISE = BASE / "sortie-conduite-v15" / "{reprise}"
TOURS_COMPLETS_PREMIERE = {k1}  # nombre de lignes du journal des durées transféré par la reprise


def relance_seule() -> dict:
    """Règle de la première exécution (manifeste de la règle transféré par la reprise) et K′, vérifiés (comme la v13)."""
    m = REPRISE / "manifeste-v3-regle.json"
    durees = REPRISE / "principal" / "transfert-1" / "sortie-durees-v3.jsonl"
    scellement.verifier(m)
    scellement.verifier(durees)
    lignes = [l for l in durees.read_text(encoding="utf-8").splitlines() if l.strip()]
    tours = sorted(json.loads(l)["tour"] for l in lignes)
    if tours != list(range(TOURS_COMPLETS_PREMIERE)):
        raise SystemExit(f"journal des durées : tours {{tours}}, attendus 0 à {{TOURS_COMPLETS_PREMIERE - 1}}")
    regle = json.loads(m.read_text(encoding="utf-8"))["regle_tours"]
    tombees = []
    for f in (REPRISE / "principal" / "transfert-1" / "journal" / "gardes-v3.jsonl",
              REPRISE / "principal" / "transfert-1" / "gardes-lanceur-v3.jsonl"):
        scellement.verifier(f)
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip():
                e = json.loads(l)
                if e.get("etat") != "passée" and e.get("garde") not in tombees:
                    tombees.append(e.get("garde"))
    return {{"tours_complets_premiere": TOURS_COMPLETS_PREMIERE, "regle_premiere": regle, "source": str(REPRISE),
            "instance_premiere": "61049303", "manifeste_regle": str(m.resolve()), "gardes_tombees_premiere": tombees}}''')
rep('    if T_MAX_PILOTE_S != 1800.0 or ANTERIEURES:\n        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures : rien ne tourne")',
    '    if T_MAX_PILOTE_S != 1800.0 or [i["id"] for i in ANTERIEURES] != ["61049303"]:\n        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures autres que 61049303 : rien ne tourne")')
rep('pidf = BASE / "lancement-v15.pid"', 'pidf = BASE / "lancement-v16.pid"')
rep('sortie = BASE / "sortie-conduite-v15"  # chemin absolu', 'sortie = BASE / "sortie-conduite-v16"  # chemin absolu')
rep('trace = BASE / "bilan-lancement-v15.json"', 'trace = BASE / "bilan-lancement-v16.json"')
rep('instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S)',
    'instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S,\n                          relance_seule=relance_seule())')
rep('    if conduite.relance_seule is not None or conduite.t_max_pilote_s != 1800.0:',
    '    if conduite.relance_seule is None or conduite.t_max_pilote_s != 1800.0:')
assert "lancement-v15" not in c and "sortie-conduite-v16" in c
(out / "lancer-conduite-v16.py").write_text(c, encoding="utf-8")

p = (base / "poste-hetzner-v13.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n"
p = (h + "# Poste Hetzner du témoin de Bailey, v14 — RELANCE de la confirmation (R12 ; v1 à v13 restent telles quelles ;\n"
     "# addendum 7, § 2.1, chemin de l'addendum 5). v14 = v13 avec la conduite v16 (`lanceur_v21`, relance seule) et des\n"
     "# noms neufs (sortie `sortie-conduite-v16`, liste `repertoires-sortie-conduite-v16-v1.txt`).\n" + p[len(h):])
corps = p.split("\nset -uo pipefail", 1)
b = corps[1]
for a, z in (("sortie-conduite-v15", "sortie-conduite-v16"), ("lancement-v15", "lancement-v16"),
             ("lancer-conduite-v15", "lancer-conduite-v16"), ("offre-choisie-v13", "offre-choisie-v14"),
             ("poste-fini-v13", "poste-fini-v14"), ("poste-hetzner-v13", "poste-hetzner-v14")):
    assert b.count(a) >= 1, a; b = b.replace(a, z)
assert re.search(r"v15|v13\b|offre-choisie-v13|poste-fini-v13", b) is None or "manifeste-local-v7" in b
p = corps[0] + "\nset -uo pipefail" + b
(out / "poste-hetzner-v14.sh").write_text(p, encoding="utf-8")

k = (base / "construire-donnees-demarrage-v13.py").read_text(encoding="utf-8")
for a, z in (("v13 (R12 ; v1 à v12 restent telles\nquelles). v13 = v12", "v14 (R12 ; v1 à v13 restent telles\nquelles). v14 = v13"),
             ('"poste-hetzner-v13.sh"', '"poste-hetzner-v14.sh"'), ("(`poste-hetzner-v13.sh`)", "(`poste-hetzner-v14.sh`)"),
             ('"poste-temoin-bailey-v13"', '"poste-temoin-bailey-v14"'), ('"temoin-bailey-v13"}', '"temoin-bailey-v14"}')):
    assert k.count(a) == 1, a; k = k.replace(a, z)
(out / "construire-donnees-demarrage-v14.py").write_text(k, encoding="utf-8")
print("ok")
