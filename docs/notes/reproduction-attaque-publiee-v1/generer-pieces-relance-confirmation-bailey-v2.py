"""Génère les pièces de la RELANCE de la confirmation du témoin de Bailey (addendum 7, § 2.1 : relance de la liste
d'arrêt, texte l. 371, par le chemin de l'addendum 5 quand l'instance est perdue) : conduite v16 (relance seule,
`lanceur_v21`), poste v14, constructeur v14 (R12 ; les versions antérieures restent telles quelles).

v2 (contre-lecture `contre-lecture-relance-confirmation-bailey-v1.md`) : la destruction de 61049303 et le transfert qui
fait foi ne sont plus passés à la main : ils sont lus dans le bilan scellé de la reprise (`bilan-reprise-v10.json` :
`instance`, `detruite`, `destruction`, `transferts.principal.foi`) et recoupés avec `sortie-conduite-v15/poste-v5.json`,
et la conduite v16 les revérifie avant toute création ; les empreintes des quatre fichiers lus par `relance_seule()` sont
fixées dans la conduite ; le manifeste de la règle de la reprise doit être égal à celui de la conduite v15 ; GO,
empreinte de l'addendum et commit égaux à ceux de la v15 ; `relance_seule()` jouée avant l'écriture du PID ; le poste v14
attend la marque de fin de la reprise ; K attendu affiché pour plusieurs c.
Usage, après la reprise (lecture 38), sous `PYTHONPATH=src` :
  generer-pieces-relance-confirmation-bailey-v2.py <sortie> <GO_ID> <empreinte addendum 7> <commit du code>
      <dossier de reprise, ex. reprise-v10> <K′ attendu>
Champs lus (techniques seulement, § 3) : bilan de la reprise (ci-dessus), `poste-v5.json`, nombre de lignes du journal des
durées ; aucune note.

Conduite v16 = conduite v15 (gardes d'entrée de l'addendum 7) + `relance_seule()` de la conduite v13 (addendum 5),
portée sur `sortie-conduite-v15/<reprise>` et l'instance 61049303 : instance antérieure unique (le poste de dépense de
la confirmation, D cumulée, même B = 85), t du pilote de la première exécution, aucun pilote ni règle sur l'instance
neuve. Poste v14 = poste v13 avec la conduite v16 et des noms neufs (sortie `sortie-conduite-v16`, liste
`repertoires-sortie-conduite-v16-v1.txt`)."""
import json, math, re, sys
from pathlib import Path
from controle_ia import scellement
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import conventions_v3 as cv
out, go_id, emp, commit, reprise, k1 = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6])
assert re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id) and re.fullmatch(r"[0-9a-f]{64}", emp) and re.fullmatch(r"[0-9a-f]{40}", commit)
assert re.fullmatch(r"reprise-v10(-\d+)?", reprise) and 0 <= k1 < 20
base = Path("/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111")
CREATION, C1 = 1794907209.2755258, 1.3247777777777778
R = base / "sortie-conduite-v15" / reprise
bilan_r = R / "bilan-reprise-v10.json"
scellement.verifier(bilan_r)
br = json.loads(bilan_r.read_text(encoding="utf-8"))
assert br.get("instance") == "61049303" and br.get("detruite") is True, "reprise : instance ou destruction non conformes"
destr = float(br["destruction"])
foi = (br.get("transferts", {}).get("principal") or {}).get("foi")
assert foi in ("transfert-1", "transfert-2"), f"reprise : transfert du principal sans foi ({foi})"
pv = json.loads((base / "sortie-conduite-v15" / "poste-v5.json").read_text(encoding="utf-8"))
assert pv["instances"] == [{"c": C1, "creation": CREATION, "destruction": destr, "id": "61049303"}], "poste-v5.json : instance non conforme"
T = R / "principal" / foi
LUS = {"manifeste-v3-regle.json": R / "manifeste-v3-regle.json", "sortie-durees-v3.jsonl": T / "sortie-durees-v3.jsonl",
       "journal/gardes-v3.jsonl": T / "journal" / "gardes-v3.jsonl", "gardes-lanceur-v3.jsonl": T / "gardes-lanceur-v3.jsonl"}
for f in LUS.values():
    scellement.verifier(f)
assert LUS["manifeste-v3-regle.json"].read_bytes() == (base / "sortie-conduite-v15" / "manifeste-v3-regle.json").read_bytes(), "manifeste de la règle de la reprise différent de celui de la conduite v15"
n_durees = len([l for l in LUS["sortie-durees-v3.jsonl"].read_text(encoding="utf-8").splitlines() if l.strip()])
assert n_durees == k1, f"K′ attendu {k1}, journal des durées : {n_durees} lignes"
ATTENDUES = {k: cv.sha_fichier(f) for k, f in LUS.items()}

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
{k1} lignes de durées (tours 0 à {k1 - 1}), gardes tombées lues sans note, empreintes des fichiers lus fixées à la
génération, destruction de 61049303 recoupée avec le bilan scellé de la reprise et `poste-v5.json` ; jouées avant
l'écriture du PID et avant toute création. Sortie, bilan et PID neufs (`sortie-conduite-v16`,
`bilan-lancement-v16.json`, `lancement-v16.pid`). Elle ne lit aucune note.

Usage, détaché, depuis la racine du dépôt, sous `GO_ID={go_id}`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py --offre <id> --image <image>
"""'''
c = doc + c15[i + 3:]
assert f'GO_ID = "{go_id}"' in c and f'EMPREINTE_ADDENDUM_7 = "{emp}"' in c and f'COMMIT_CODE = "{commit}"  # addendum 7, § 4' in c, "arguments différents des constantes de la v15"
def rep(a, b, n=1):
    global c
    assert c.count(a) == n, (a[:70], c.count(a)); c = c.replace(a, b)
rep('ANTERIEURES: list = []  # poste neuf (addendum 7, § 2.2) : D compte de zéro',
    f'''# Instance de la première exécution (conduite v15) : création relevée par la conduite v15
# (`sortie-conduite-v15/poste-v5.json`), destruction écrite par la reprise ; même poste de dépense (addendum 7, § 2.2).
ANTERIEURES = [{{"id": "61049303", "c": 1.3247777777777778, "creation": 1794907209.2755258,
                "destruction": {destr!r}, "B": 85.0}}]
REPRISE = BASE / "sortie-conduite-v15" / "{reprise}"
TRANSFERT = REPRISE / "principal" / "{foi}"  # transfert qui fait foi (bilan de la reprise)
ATTENDUES = {ATTENDUES!r}  # empreintes relevées à la génération
TOURS_COMPLETS_PREMIERE = {k1}  # nombre de lignes du journal des durées transféré par la reprise


def relance_seule() -> dict:
    """Règle de la première exécution (manifeste de la règle transféré par la reprise) et K′, vérifiés (comme la v13)."""
    m = REPRISE / "manifeste-v3-regle.json"
    durees = TRANSFERT / "sortie-durees-v3.jsonl"
    lus = {{"manifeste-v3-regle.json": m, "sortie-durees-v3.jsonl": durees,
           "journal/gardes-v3.jsonl": TRANSFERT / "journal" / "gardes-v3.jsonl",
           "gardes-lanceur-v3.jsonl": TRANSFERT / "gardes-lanceur-v3.jsonl"}}
    for nom, f in lus.items():
        scellement.verifier(f)
        if cv.sha_fichier(f) != ATTENDUES[nom]:
            raise SystemExit(f"{{nom}} de la reprise : empreinte différente de celle relevée à la génération : rien ne tourne")
    if m.read_bytes() != (BASE / "sortie-conduite-v15" / "manifeste-v3-regle.json").read_bytes():
        raise SystemExit("manifeste de la règle de la reprise différent de celui de la conduite v15 : rien ne tourne")
    b = REPRISE / "bilan-reprise-v10.json"
    scellement.verifier(b)
    br = json.loads(b.read_text(encoding="utf-8"))
    if br.get("instance") != "61049303" or br.get("detruite") is not True or float(br["destruction"]) != ANTERIEURES[0]["destruction"]:
        raise SystemExit("destruction de 61049303 différente du bilan scellé de la reprise : rien ne tourne")
    pv = json.loads((BASE / "sortie-conduite-v15" / "poste-v5.json").read_text(encoding="utf-8"))
    if pv["instances"] != [{{k: ANTERIEURES[0][k] for k in ("c", "creation", "destruction", "id")}}]:
        raise SystemExit("poste-v5.json de la conduite v15 différent des instances antérieures : rien ne tourne")
    lignes = [l for l in durees.read_text(encoding="utf-8").splitlines() if l.strip()]
    tours = sorted(json.loads(l)["tour"] for l in lignes)
    if tours != list(range(TOURS_COMPLETS_PREMIERE)):
        raise SystemExit(f"journal des durées : tours {{tours}}, attendus 0 à {{TOURS_COMPLETS_PREMIERE - 1}}")
    regle = json.loads(m.read_text(encoding="utf-8"))["regle_tours"]
    tombees = []
    for f in (lus["journal/gardes-v3.jsonl"], lus["gardes-lanceur-v3.jsonl"]):
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
    'instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S,\n                          relance_seule=rs)')
rep('    pidf.write_text(f"{os.getpid()}\\n", encoding="utf-8")',
    '    rs = relance_seule()  # v16 : gardes de la relance avant l\'écriture du PID et avant toute création\n    pidf.write_text(f"{os.getpid()}\\n", encoding="utf-8")')
rep('    if conduite.relance_seule is not None or conduite.t_max_pilote_s != 1800.0:',
    '    if conduite.relance_seule is None or conduite.t_max_pilote_s != 1800.0:')
assert "lancement-v15" not in c and "sortie-conduite-v16" in c
(out / "lancer-conduite-v16.py").write_text(c, encoding="utf-8")

p = (base / "poste-hetzner-v13.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n"
assert p.startswith(h)
p = (h + "# Poste Hetzner du témoin de Bailey, v14 — RELANCE de la confirmation (R12 ; v1 à v13 restent telles quelles ;\n"
     "# addendum 7, § 2.1, chemin de l'addendum 5). v14 = v13 avec la conduite v16 (`lanceur_v21`, relance seule) et des\n"
     "# noms neufs (sortie `sortie-conduite-v16`, liste `repertoires-sortie-conduite-v16-v1.txt`), et la garde « reprise finie »\n"
     "# (marque `poste-fini-reprise-v4.json`). Les commentaires d'origine plus bas ne sont pas mis à jour ; la clé\n"
     "# `cout_avec_200_go` de l'offre choisie porte le coût carte et 110 Go du § 2.4.\n" + p[len(h):])
corps = p.split("\nset -uo pipefail", 1)
b = corps[1]
for a, z in (("sortie-conduite-v15", "sortie-conduite-v16"), ("lancement-v15", "lancement-v16"),
             ("lancer-conduite-v15", "lancer-conduite-v16"), ("offre-choisie-v13", "offre-choisie-v14"),
             ("poste-fini-v13", "poste-fini-v14"), ("poste-hetzner-v13", "poste-hetzner-v14")):
    assert b.count(a) >= 1, a; b = b.replace(a, z)
assert not re.search(r"sortie-conduite-v15|lancement-v15|lancer-conduite-v15|offre-choisie-v13|poste-fini-v13|poste-hetzner-v13", b), "nom ancien resté"
a = '# inventaire R10 : aucune instance du poste ne doit exister avant la création\n'
assert b.count(a) == 1
b = b.replace(a, '# v14 : la reprise de la confirmation doit être finie (marque du poste de reprise v4), sinon rien ne tourne\n'
              '[ -s "$BASE/poste-fini-reprise-v4.json" ] || { etat "reprise de la confirmation non finie (poste-fini-reprise-v4.json absent) : rien ne tourne"; pousser "reprise non finie"; exit 3; }\n' + a)
p = corps[0] + "\nset -uo pipefail" + b
(out / "poste-hetzner-v14.sh").write_text(p, encoding="utf-8")

k = (base / "construire-donnees-demarrage-v13.py").read_text(encoding="utf-8")
for a, z in (("v13 (R12 ; v1 à v12 restent telles\nquelles). v13 = v12", "v14 (R12 ; v1 à v13 restent telles\nquelles). v14 = v13"),
             ('"poste-hetzner-v13.sh"', '"poste-hetzner-v14.sh"'), ("(`poste-hetzner-v13.sh`)", "(`poste-hetzner-v14.sh`)"),
             ('"poste-temoin-bailey-v13"', '"poste-temoin-bailey-v14"'), ('"temoin-bailey-v13"}', '"temoin-bailey-v14"}')):
    assert k.count(a) == 1, a; k = k.replace(a, z)
(out / "construire-donnees-demarrage-v14.py").write_text(k, encoding="utf-8")
d_ant = C1 * (destr - CREATION) / 3600
print(f"D des antérieures : {d_ant:.2f} USD (61049303 comptée au taux de marche de sa création à sa destruction)")
for c_ in (1.2576, 1.33, 1.6):
    d = d_ant + 0.75 * c_  # mise en place et contrôle du juge
    print(f"c = {c_} : D au calcul ≈ {d:.2f} USD ; K = {an.nombre_de_tours(85, round(d, 4), c_, 1265.0215)['K']}")
print("transfert qui fait foi :", foi, "; empreintes fixées :", {k: v[:12] for k, v in ATTENDUES.items()})
print("ok")
