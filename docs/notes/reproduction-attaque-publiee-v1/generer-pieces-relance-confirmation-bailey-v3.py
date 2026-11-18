"""Génère les pièces de la RELANCE de la confirmation du témoin de Bailey (addendum 7, § 2.1 : relance de la liste
d'arrêt, texte l. 371, par le chemin de l'addendum 5 quand l'instance est perdue) : conduite v16 (relance seule,
`lanceur_v21`), poste v14, constructeur v14 (R12 ; les versions antérieures restent telles quelles ; la v2 de ce
générateur reste telle quelle et n'a produit aucune pièce dans `runs/`).

v2 (contre-lecture `contre-lecture-relance-confirmation-bailey-v1.md`) : destruction de 61049303 et transfert qui fait foi
lus dans le bilan scellé de la reprise (`bilan-reprise-v10.json`) et recoupés avec `sortie-conduite-v15/poste-v5.json` ;
empreintes des quatre fichiers lus par `relance_seule()` fixées ; manifeste de la règle de la reprise égal à celui de la
conduite v15 ; GO, addendum 7 et commit égaux à ceux de la v15 ; `relance_seule()` avant le PID ; poste v14 qui attend la
marque de fin de la reprise.

v3 (contre-lecture de la v2, run `wf_51f94aef-21e`, et addendum 8, brouillon 3, § 2) :
- t lu dans le manifeste vérifié de la règle (plus en dur) ; K affiché pour c de 1,20 à 1,60 USD/h, c maximal qui donne
  K ≥ 71 et alerte « relance non retenue » (addendum 7, § 3) si ce c est sous le plafond de coût du poste ;
- tours du journal des durées (0 à K′ − 1, sans double), gardes « dépense » et « sonde orientée » et borne R-1 :
  `lanceur_v21.verifier_relance_seule` jouée dans le générateur, et dans la conduite v16 avant l'écriture du PID
  (`verifier_avant_pid`) ;
- refus si l'une des trois pièces existe déjà dans <sortie> (R12) ; `b` de `poste-v5.json` exigé égal à 85 ;
- K′ = 0 : couvert seulement si les trois journaux de la première exécution ont été transférés et scellés (journal des
  durées vide) ; journal absent → refus explicite, pièces à refaire (nœud) ;
- empreintes affichées entières ; docstring du constructeur v14 corrigée (il lit `poste-hetzner-v14.sh`) ; `math` retiré ;
- `--option-a` (addendum 8, § 2, A) : heures d'arrêt de 61049303 au taux du stockage : trois entrées de même identifiant
  dans `ANTERIEURES`, dans l'ordre chronologique et toutes de B = 85 : (c, création, T_a), (s, T_a, T_r),
  (c, T_r, destruction) ; T_a = 1794937311.9679263 vérifié égal au champ `t` de la dernière ligne de
  `sortie-conduite-v15/conduite-v5.jsonl` (bilan scellé de la conduite : instance gardée, alerte « exited » ou
  « stopped ») ; T_r = `redemarrage.debut` du bilan scellé de la reprise, seulement si son `statut` vaut « stopped » ou
  « exited » et qu'aucune reprise antérieure ne l'a redémarrée ; s = 0.1527777777777778 du relevé
  `releve-stockage-61049303-20261118-0152.txt` vérifié par son compagnon (`intended_status` « stopped », aucun autre
  relevé plus haut) ; création < T_a < T_r < destruction et contiguïté ; `poste-v5.json` recoupé (entrée unique) ; la
  conduite v16 rejoue ces gardes avant le PID. Si A ne peut s'appliquer ainsi : **refus** (pas de repli silencieux, R5) ;
  régénérer sans `--option-a` (et sans `--option-b` si Lazar a choisi A seul : addendum 8, § 2, B) ;
- `--option-b` (addendum 8, § 2, B) : la seule ligne `d = [o for o in d if cout(o) <= 1.6]` du poste devient
  `cout(o) <= 1.4` (une occurrence exigée) ;
- une option prise exige `--addendum-8 <empreinte>`, vérifiée contre le seul
  `prereg/temoin-attaque-publiee-bailey-v1-addendum-8-*.md.sha256` (absent, ou plusieurs : refus) ; sans option,
  `--addendum-8` est refusé ; sans option, pièces comme la v2 (plus les corrections ci-dessus) ; l'en-tête des trois
  pièces dit les options retenues et cite l'addendum 8 par son empreinte entière.

v3, corrections de la contre-lecture R2 du générateur v3 (run `wf_603687eb-79b` ; même nom, aucune pièce produite avant) :
- `--marque-reprise poste-fini-reprise-vN.json` obligatoire (constat 1) : forme vérifiée, fichier exigé présent et non vide
  dans `runs/temoin-bailey-v1-20261111/` ; `poste-fini-reprise-v4.json` exigé pour `reprise-v10` (poste de reprise v4)
  et refusé, comme toute marque v1 à v4, pour `reprise-v10-N` (faite par un poste de reprise v5 ou plus) ; la marque est
  injectée dans la garde « reprise finie » du poste v14 et dans son en-tête, à la place du nom en dur ;
- option A (constat 2) : `budget.taux` du bilan scellé de la reprise (taux lu par la reprise avant le redémarrage) exigé
  présent et au plus c, dans le générateur et dans `verifier_option_a` de la conduite v16 ;
- limite connue, déclarée (constat 3) : les gardes de contenu de l'addendum 8 vérifient seulement que le texte scellé cite
  T_a et 61049303 (option A) ou la ligne `cout(o) <= 1.4` (option B), pas que l'option y soit retenue ; le choix des
  options reste celui de Lazar, porté par la commande de génération et relu dans l'en-tête des pièces.

Usage, après la reprise (lecture 38), sous `PYTHONPATH=src` :
  generer-pieces-relance-confirmation-bailey-v3.py <sortie> <GO_ID> <empreinte addendum 7> <commit du code>
      <dossier de reprise, ex. reprise-v10-2> <K′ attendu> --marque-reprise <poste-fini-reprise-vN.json>
      [--option-a] [--option-b] [--addendum-8 <empreinte>]
Puis sceller les trois pièces avant la poussée (`python -m controle_ia.scellement sceller <les trois pièces>`) : le poste
v14 exige `sha256sum -c` sur leurs compagnons et sort sinon en « empreinte en échec », sans dépense (constat 5).
Champs lus (techniques seulement) : bilan de la reprise (instance, statut, redemarrage.debut, detruite, destruction,
transferts.principal.foi), bilans des reprises antérieures (redemarrage, transfert_en_marche, statut ; option A),
`poste-v5.json`, champs B, R, D, c, t, K, H_heures de la règle, champ `t` de la dernière ligne de `conduite-v5.jsonl`
et champs alerte, detruite du bilan de la conduite v15 (option A), relevé de stockage, numéros de tour du journal des
durées, champs garde et etat des journaux de gardes ; aucune note.

Conduite v16 = conduite v15 (gardes d'entrée de l'addendum 7) + `relance_seule()` de la conduite v13 (addendum 5),
portée sur `sortie-conduite-v15/<reprise>` et l'instance 61049303 (une entrée, ou trois avec A ; D cumulée, même B = 85),
t du pilote de la première exécution, aucun pilote ni règle sur l'instance neuve. Poste v14 = poste v13 avec la conduite
v16 et des noms neufs (sortie `sortie-conduite-v16`, liste `repertoires-sortie-conduite-v16-v1.txt`), et, avec B, le
plafond de coût 1,4."""
import argparse
import json
import re
import sys
import time
from pathlib import Path

from controle_ia import scellement
from controle_ia.temoin_bailey import analyse_v3 as an
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey import lanceur_v21 as L

DEPOT = Path("/home/user/controle-ia-travail")
base = DEPOT / "runs" / "temoin-bailey-v1-20261111"
PREREG = DEPOT / "prereg"
CREATION, C1, B = 1794907209.2755258, 1.3247777777777778, 85.0
T_A = 1794937311.9679263  # addendum 8, § 2, A : 17 novembre, 17:41:51Z
S_STOCKAGE = 0.1527777777777778  # addendum 8, § 1 et § 2, A
RELEVE = "releve-stockage-61049303-20261118-0152.txt"
EMPREINTE_RELEVE = "002b9f58fbdc9b6afa24339617c8e6ef202180f699d376f0d0f5695e37aa273b"
PIECES = ("lancer-conduite-v16.py", "poste-hetzner-v14.sh", "construire-donnees-demarrage-v14.py")


def refus(msg: str):
    raise SystemExit(f"refus : {msg} : aucune pièce écrite")


def exiger(cond, msg: str) -> None:
    if not cond:
        refus(msg)


def reprises_avant(nom: str) -> list[str]:
    """Noms des reprises de `Reprise.reprendre` antérieures à `nom` (reprise-v10, reprise-v10-2, …)."""
    if nom == "reprise-v10":
        return []
    n = int(nom.rsplit("-", 1)[1])
    exiger(n >= 2, f"nom de reprise {nom} impossible (la deuxième reprise est reprise-v10-2)")
    return ["reprise-v10"] + [f"reprise-v10-{j}" for j in range(2, n)]


ap = argparse.ArgumentParser()
for nom in ("sortie", "go_id", "addendum_7", "commit", "reprise"):
    ap.add_argument(nom)
ap.add_argument("k1", type=int)
ap.add_argument("--option-a", action="store_true", help="addendum 8, § 2, A : heures d'arrêt au taux du stockage")
ap.add_argument("--option-b", action="store_true", help="addendum 8, § 2, B : coût de l'offre au plus 1,40 USD/h")
ap.add_argument("--addendum-8", default=None, help="empreinte de l'addendum 8 scellé (obligatoire avec une option)")
ap.add_argument("--marque-reprise", required=True,
                help="marque de fin du poste de reprise qui a fait <reprise> (poste-fini-reprise-vN.json), attendue par le poste v14")
a = ap.parse_args()
out, go_id, emp, commit, reprise, k1 = Path(a.sortie), a.go_id, a.addendum_7, a.commit, a.reprise, a.k1
opt_a, opt_b, emp8, marque = a.option_a, a.option_b, a.addendum_8, a.marque_reprise
exiger(re.fullmatch(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", go_id) and re.fullmatch(r"[0-9a-f]{64}", emp)
       and re.fullmatch(r"[0-9a-f]{40}", commit), "GO, empreinte de l'addendum 7 ou commit mal formés")
exiger(re.fullmatch(r"reprise-v10(-\d+)?", reprise) and 0 <= k1 < 20, "dossier de reprise ou K′ hors domaine")
m_marque = re.fullmatch(r"poste-fini-reprise-v(\d+)\.json", marque)
exiger(m_marque, f"marque de reprise {marque!r} mal formée (poste-fini-reprise-vN.json attendu)")
exiger((base / marque).is_file() and (base / marque).stat().st_size > 0,
       f"marque de reprise {marque} absente ou vide dans {base} (reprise non finie, ou dépôt pas à jour)")
# reprise-v10 : faite par le poste de reprise v4 ; reprise-v10-N : par un poste de reprise v5 ou plus (la v4 a écrit reprise-v10)
exiger((int(m_marque.group(1)) == 4) if reprise == "reprise-v10" else (int(m_marque.group(1)) >= 5),
       f"marque {marque} incohérente avec {reprise} (reprise-v10 : poste-fini-reprise-v4.json ; "
       "reprise-v10-N : marque d'un poste de reprise v5 ou plus)")
exiger(out.is_dir(), f"dossier de sortie {out} absent")
exiger(not any((out / n).exists() for n in PIECES), "pièce déjà présente dans le dossier de sortie (R12)")
if opt_a or opt_b:
    exiger(emp8 is not None and re.fullmatch(r"[0-9a-f]{64}", emp8),
           "option de l'addendum 8 sans --addendum-8 <empreinte entière>")
    comp = sorted(PREREG.glob("temoin-attaque-publiee-bailey-v1-addendum-8-*.md.sha256"))
    exiger(len(comp) == 1, f"addendum 8 scellé introuvable ou multiple dans prereg/ ({len(comp)} compagnons)")
    add8 = comp[0].with_name(comp[0].name[: -len(".sha256")])
    scellement.verifier(add8)
    exiger(cv.sha_fichier(add8) == emp8, "empreinte de l'addendum 8 scellé différente de --addendum-8")
    texte8 = add8.read_text(encoding="utf-8")
    exiger(not opt_a or (repr(T_A) in texte8 and "61049303" in texte8), "addendum 8 scellé sans T_a de l'option A")
    exiger(not opt_b or "cout(o) <= 1.4" in texte8, "addendum 8 scellé sans le plafond de l'option B")
else:
    exiger(emp8 is None, "--addendum-8 sans option : rien à citer")
    add8 = None

V15 = base / "sortie-conduite-v15"
R = V15 / reprise
bilan_r = R / "bilan-reprise-v10.json"
scellement.verifier(bilan_r)
br = json.loads(bilan_r.read_text(encoding="utf-8"))
exiger(br.get("instance") == "61049303" and br.get("detruite") is True, "reprise : instance ou destruction non conformes")
destr = float(br["destruction"])
foi = ((br.get("transferts") or {}).get("principal") or {}).get("foi")
exiger(foi in ("transfert-1", "transfert-2"), f"reprise : transfert du principal sans foi ({foi})")
pv = json.loads((V15 / "poste-v5.json").read_text(encoding="utf-8"))
exiger(float(pv.get("b", -1)) == B and pv.get("instances") == [{"c": C1, "creation": CREATION, "destruction": destr,
                                                                "id": "61049303"}], "poste-v5.json : b ou instance non conformes")
T = R / "principal" / foi
LUS = {"manifeste-v3-regle.json": R / "manifeste-v3-regle.json", "sortie-durees-v3.jsonl": T / "sortie-durees-v3.jsonl",
       "journal/gardes-v3.jsonl": T / "journal" / "gardes-v3.jsonl", "gardes-lanceur-v3.jsonl": T / "gardes-lanceur-v3.jsonl"}
for nom, f in LUS.items():
    if k1 == 0 and not f.is_file():
        refus(f"K′ = 0 et {nom} absent du transfert : non couvert par ce générateur (pièces à refaire, nœud)")
    scellement.verifier(f)
exiger(LUS["manifeste-v3-regle.json"].read_bytes() == (V15 / "manifeste-v3-regle.json").read_bytes(),
       "manifeste de la règle de la reprise différent de celui de la conduite v15")
lignes = [l for l in LUS["sortie-durees-v3.jsonl"].read_text(encoding="utf-8").splitlines() if l.strip()]
exiger(len(lignes) == k1, f"K′ attendu {k1}, journal des durées : {len(lignes)} lignes")
tours = sorted(json.loads(l)["tour"] for l in lignes)
exiger(tours == list(range(k1)), f"journal des durées : tours {tours}, attendus 0 à {k1 - 1}")
regle = json.loads(LUS["manifeste-v3-regle.json"].read_text(encoding="utf-8"))["regle_tours"]
t_r = regle["t"]
tombees = []
for f in (LUS["journal/gardes-v3.jsonl"], LUS["gardes-lanceur-v3.jsonl"]):
    for l in f.read_text(encoding="utf-8").splitlines():
        if l.strip():
            e = json.loads(l)
            if e.get("etat") != "passée" and e.get("garde") not in tombees:
                tombees.append(e.get("garde"))
ATTENDUES = {k: cv.sha_fichier(f) for k, f in LUS.items()}

avant = []
t_redem = None
if opt_a:
    na = "option A de l'addendum 8 inapplicable (§ 2, A : plein taux, comme le texte) : régénérer sans --option-a"
    cj = [l for l in (V15 / "conduite-v5.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    exiger(cj and float(json.loads(cj[-1])["t"]) == T_A, f"{na} ; T_a différent du t de la dernière ligne de conduite-v5.jsonl")
    bc_f = V15 / "bilan-conduite-v5.json"
    scellement.verifier(bc_f)
    bc = json.loads(bc_f.read_text(encoding="utf-8"))
    exiger(bc.get("detruite") is False and re.search(r"instance 61049303 arrêtée \(statut « (exited|stopped) »\)",
                                                     str(bc.get("alerte"))),
           f"{na} ; bilan de la conduite v15 sans l'arrêt de 61049303 lu (« exited » ou « stopped »)")
    exiger(br.get("statut") in L.STATUTS_ARRETES, f"{na} ; statut du bilan de la reprise : {br.get('statut')!r}")
    rd = br.get("redemarrage")
    exiger(isinstance(rd, dict) and isinstance(rd.get("debut"), (int, float)) and not isinstance(rd.get("debut"), bool),
           f"{na} ; redemarrage.debut absent du bilan de la reprise")
    t_redem = float(rd["debut"])
    taux_lu = (br.get("budget") or {}).get("taux")
    exiger(isinstance(taux_lu, (int, float)) and not isinstance(taux_lu, bool) and float(taux_lu) <= C1,
           f"{na} ; taux lu par la reprise (budget.taux : {taux_lu!r}) absent ou plus haut que c")
    avant = reprises_avant(reprise)
    for nom in avant:
        fb = V15 / nom / "bilan-reprise-v10.json"
        scellement.verifier(fb)
        b0 = json.loads(fb.read_text(encoding="utf-8"))
        exiger("redemarrage" not in b0 and "transfert_en_marche" not in b0 and b0.get("statut") in (None,) + L.STATUTS_ARRETES,
               f"{na} ; la reprise antérieure {nom} a redémarré l'instance ou l'a trouvée en marche")
    rel = base / RELEVE
    scellement.verifier(rel)
    exiger(cv.sha_fichier(rel) == EMPREINTE_RELEVE, f"{na} ; relevé de stockage d'empreinte inattendue")
    objs = [json.loads(l) for l in rel.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    exiger(len(objs) == 1 and str(objs[0].get("id")) == "61049303" and objs[0].get("intended_status") == "stopped"
           and float(objs[0].get("storage_total_cost")) == S_STOCKAGE, f"{na} ; relevé de stockage non conforme")
    for f in sorted(base.glob("releve-stockage-61049303-*.txt")):
        scellement.verifier(f)
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip() and not l.startswith("#"):
                exiger(float(json.loads(l).get("storage_total_cost", 0)) <= S_STOCKAGE,
                       f"{na} ; relevé {f.name} plus haut que s (le plus haut fait foi : nœud)")
    exiger(CREATION < T_A < t_redem < destr, f"{na} ; intervalles non ordonnés (création < T_a < T_r < destruction)")
    ant = [{"id": "61049303", "c": C1, "creation": CREATION, "destruction": T_A, "B": B},
           {"id": "61049303", "c": S_STOCKAGE, "creation": T_A, "destruction": t_redem, "B": B},
           {"id": "61049303", "c": C1, "creation": t_redem, "destruction": destr, "B": B}]
    exiger(all(ant[j]["destruction"] == ant[j + 1]["creation"] for j in range(2)), f"{na} ; intervalles non contigus")
else:
    ant = [{"id": "61049303", "c": C1, "creation": CREATION, "destruction": destr, "B": B}]
rs = {"tours_complets_premiere": k1, "regle_premiere": regle, "instance_premiere": "61049303",
      "manifeste_regle": str(LUS["manifeste-v3-regle.json"]), "gardes_tombees_premiere": tombees}
L.verifier_relance_seule(rs, L.instances_du_poste(ant, B), B)  # lève GardeArret : aucune pièce écrite
d_ant = L.Poste(b=B, instances=L.instances_du_poste(ant, B)).depense(time.time())

if opt_a or opt_b:
    opts = " et ".join(x for x, o in (("A", opt_a), ("B", opt_b)) if o)
    ligne_opts = (f"options de l'addendum 8 retenues : {opts} (addendum 8 `{add8.name}`, empreinte {emp8}) ; "
                  + ("A : heures d'arrêt de 61049303 au taux du stockage (trois entrées) ; " if opt_a else "A non retenue ; ")
                  + ("B : coût de l'offre au plus 1,40 USD/h" if opt_b else "B non retenue : plafond 1,6 USD/h"))
else:
    ligne_opts = "aucune option de l'addendum 8 : relance au texte (D au plein taux, plafond de coût 1,6 USD/h)"

c15 = (base / "lancer-conduite-v15.py").read_text(encoding="utf-8")
i = c15.index('"""', 3)
doc = f'''"""v16 — RELANCE de la confirmation (R12 ; v1 à v15 restent telles quelles ; addendum 7, § 2.1, par le chemin de
l'addendum 5 : relance seule, pièces neuves contre-lues ; générée par `generer-pieces-relance-confirmation-bailey-v3.py`).
{ligne_opts}.
La première exécution du run principal de la confirmation (conduite v15, instance 61049303) s'est interrompue avant
20 tours complets (K′ = {k1}) : compte Vast sans crédit, instance arrêtée par Vast le 17 novembre vers 17:12Z ; reprise
faite (`sortie-conduite-v15/{reprise}/`). Conduite `lanceur_v21` avec `relance_seule` : amorce, auto-arrêt, mise en place
et contrôle du juge sur une instance neuve, puis, sans pilote ni règle sur l'instance, K recalculé par la règle (même
B = 85, D du poste, c de l'instance neuve, t du pilote de la première exécution) et `principal-relance`. Instance
antérieure : 61049303 (création relevée par la conduite v15, destruction écrite par la reprise{" ; trois entrées avec A : création → T_a au taux c, T_a → T_r au taux du stockage s, T_r → destruction au taux c" if opt_a else ""}).
Gardes d'entrée de la v15 (addendum 7 scellé, GO qui cite son empreinte entière, manifeste v7), plus celles de la
relance : {"addendum 8 scellé à l'empreinte citée, " if add8 else ""}empreintes du manifeste de la règle et des journaux de
la reprise, exactement {k1} lignes de durées (tours 0 à {k1 - 1}), gardes tombées lues sans note, destruction de 61049303
recoupée avec le bilan scellé de la reprise et `poste-v5.json`{", T_a, T_r, statut, reprises antérieures, relevé de stockage et contiguïté des trois intervalles (option A)" if opt_a else ""},
puis `lanceur_v21.verifier_relance_seule` (gardes « dépense » et « sonde orientée », borne R-1) ; jouées avant l'écriture
du PID et avant toute création (`verifier_avant_pid`). Sortie, bilan et PID neufs (`sortie-conduite-v16`,
`bilan-lancement-v16.json`, `lancement-v16.pid`). Elle ne lit aucune note.

Usage, détaché, depuis la racine du dépôt, sous `GO_ID={go_id}`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py --offre <id> --image <image>
"""'''
c = doc + c15[i + 3:]
exiger(f'GO_ID = "{go_id}"' in c and f'EMPREINTE_ADDENDUM_7 = "{emp}"' in c
       and f'COMMIT_CODE = "{commit}"  # addendum 7, § 4' in c, "arguments différents des constantes de la v15")


def rep(x, y, n=1):
    global c
    exiger(c.count(x) == n, f"gabarit de la v15 : {x[:70]!r} trouvé {c.count(x)} fois")
    c = c.replace(x, y)


BLOC = '''# --- v16 : relance de la confirmation ---------------------------------------------------------------------------------
OPTION_A = @OPTION_A@  # addendum 8, § 2, A : heures d'arrêt de 61049303 au taux du stockage (trois entrées)
OPTION_B = @OPTION_B@  # addendum 8, § 2, B : coût de l'offre au plus 1,40 USD/h (filtre du poste v14 ; rien ici)
ADDENDUM_8 = @ADD8@  # None sans option
EMPREINTE_ADDENDUM_8 = @EMP8@
# Instance de la première exécution (conduite v15) : création relevée par la conduite v15
# (`sortie-conduite-v15/poste-v5.json`), destruction écrite par la reprise ; même poste de dépense (addendum 7, § 2.2).
# Option A : trois entrées de même identifiant, dans l'ordre chronologique (`Poste.depense` les somme).
ANTERIEURES = @ANT@
C_PREMIERE = 1.3247777777777778
CREATION_PREMIERE = 1794907209.2755258
DESTRUCTION_PREMIERE = @DESTR@  # bilan scellé de la reprise
T_ARRET = @TA@  # A : champ t de la dernière ligne de sortie-conduite-v15/conduite-v5.jsonl
T_REDEMARRAGE = @TR@  # A : redemarrage.debut du bilan scellé de la reprise
S_STOCKAGE = @S@  # A : storage_total_cost du relevé ci-dessous
RELEVE_STOCKAGE = BASE / "releve-stockage-61049303-20261118-0152.txt"
EMPREINTE_RELEVE = "002b9f58fbdc9b6afa24339617c8e6ef202180f699d376f0d0f5695e37aa273b"
REPRISES_AVANT = @AVANT@  # A : reprises antérieures, qui n'ont pas redémarré l'instance
REPRISE = BASE / "sortie-conduite-v15" / "@REPRISE@"
TRANSFERT = REPRISE / "principal" / "@FOI@"  # transfert qui fait foi (bilan de la reprise)
ATTENDUES = @ATT@  # empreintes relevées à la génération
TOURS_COMPLETS_PREMIERE = @K1@  # nombre de lignes du journal des durées transféré par la reprise


def verifier_option_a(br: dict) -> None:
    """Addendum 8, § 2, A : T_a, T_r, statut, reprises antérieures, relevé de stockage et contiguïté, revérifiés."""
    if br.get("statut") not in L.STATUTS_ARRETES or not isinstance(br.get("redemarrage"), dict) \\
            or float(br["redemarrage"].get("debut")) != T_REDEMARRAGE:
        raise SystemExit("option A : statut ou redémarrage du bilan de la reprise différents : rien ne tourne")
    taux_lu = (br.get("budget") or {}).get("taux")
    if not isinstance(taux_lu, (int, float)) or isinstance(taux_lu, bool) or float(taux_lu) > C_PREMIERE:
        raise SystemExit("option A : taux lu par la reprise absent ou plus haut que c : rien ne tourne")
    cj =[l for l in (BASE / "sortie-conduite-v15" / "conduite-v5.jsonl").read_text(encoding="utf-8").splitlines()
          if l.strip()]
    if not cj or float(json.loads(cj[-1])["t"]) != T_ARRET:
        raise SystemExit("option A : T_a différent du t de la dernière ligne de conduite-v5.jsonl : rien ne tourne")
    bc = BASE / "sortie-conduite-v15" / "bilan-conduite-v5.json"
    scellement.verifier(bc)
    bc = json.loads(bc.read_text(encoding="utf-8"))
    if bc.get("detruite") is not False or not re.search(r"instance 61049303 arrêtée \\(statut « (exited|stopped) »\\)",
                                                        str(bc.get("alerte"))):
        raise SystemExit("option A : bilan de la conduite v15 sans l'arrêt de 61049303 : rien ne tourne")
    for nom in REPRISES_AVANT:
        f = BASE / "sortie-conduite-v15" / nom / "bilan-reprise-v10.json"
        scellement.verifier(f)
        b0 = json.loads(f.read_text(encoding="utf-8"))
        if "redemarrage" in b0 or "transfert_en_marche" in b0 or b0.get("statut") not in (None,) + L.STATUTS_ARRETES:
            raise SystemExit(f"option A : la reprise antérieure {nom} a redémarré l'instance : rien ne tourne")
    scellement.verifier(RELEVE_STOCKAGE)
    if cv.sha_fichier(RELEVE_STOCKAGE) != EMPREINTE_RELEVE:
        raise SystemExit("option A : relevé de stockage d'empreinte inattendue : rien ne tourne")
    objs = [json.loads(l) for l in RELEVE_STOCKAGE.read_text(encoding="utf-8").splitlines()
            if l.strip() and not l.startswith("#")]
    if len(objs) != 1 or str(objs[0].get("id")) != "61049303" or objs[0].get("intended_status") != "stopped" \\
            or float(objs[0].get("storage_total_cost")) != S_STOCKAGE:
        raise SystemExit("option A : relevé de stockage non conforme : rien ne tourne")
    for f in sorted(BASE.glob("releve-stockage-61049303-*.txt")):  # le plus haut des relevés fait foi
        scellement.verifier(f)
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip() and not l.startswith("#") and float(json.loads(l).get("storage_total_cost", 0)) > S_STOCKAGE:
                raise SystemExit(f"option A : relevé {f.name} plus haut que s : rien ne tourne ; nœud")
    attendu =[("61049303", C_PREMIERE, CREATION_PREMIERE, T_ARRET), ("61049303", S_STOCKAGE, T_ARRET, T_REDEMARRAGE),
               ("61049303", C_PREMIERE, T_REDEMARRAGE, DESTRUCTION_PREMIERE)]
    if [(i["id"], i["c"], i["creation"], i["destruction"]) for i in ANTERIEURES] != attendu \\
            or not CREATION_PREMIERE < T_ARRET < T_REDEMARRAGE < DESTRUCTION_PREMIERE \\
            or any(float(i["B"]) != B_ATTENDU for i in ANTERIEURES):
        raise SystemExit("option A : trois intervalles non contigus ou non ordonnés : rien ne tourne")


def relance_seule() -> dict:
    """Règle de la première exécution (manifeste de la règle transféré par la reprise) et K′, vérifiés (comme la v13)."""
    m = REPRISE / "manifeste-v3-regle.json"
    durees = TRANSFERT / "sortie-durees-v3.jsonl"
    lus = {"manifeste-v3-regle.json": m, "sortie-durees-v3.jsonl": durees,
           "journal/gardes-v3.jsonl": TRANSFERT / "journal" / "gardes-v3.jsonl",
           "gardes-lanceur-v3.jsonl": TRANSFERT / "gardes-lanceur-v3.jsonl"}
    for nom, f in lus.items():
        scellement.verifier(f)
        if cv.sha_fichier(f) != ATTENDUES[nom]:
            raise SystemExit(f"{nom} de la reprise : empreinte différente de celle relevée à la génération : rien ne tourne")
    if m.read_bytes() != (BASE / "sortie-conduite-v15" / "manifeste-v3-regle.json").read_bytes():
        raise SystemExit("manifeste de la règle de la reprise différent de celui de la conduite v15 : rien ne tourne")
    b = REPRISE / "bilan-reprise-v10.json"
    scellement.verifier(b)
    br = json.loads(b.read_text(encoding="utf-8"))
    if br.get("instance") != "61049303" or br.get("detruite") is not True \\
            or float(br["destruction"]) != DESTRUCTION_PREMIERE or ANTERIEURES[-1]["destruction"] != DESTRUCTION_PREMIERE:
        raise SystemExit("destruction de 61049303 différente du bilan scellé de la reprise : rien ne tourne")
    if ((br.get("transferts") or {}).get("principal") or {}).get("foi") != TRANSFERT.name:
        raise SystemExit("transfert qui fait foi différent du bilan scellé de la reprise : rien ne tourne")
    pv = json.loads((BASE / "sortie-conduite-v15" / "poste-v5.json").read_text(encoding="utf-8"))
    if float(pv.get("b", -1)) != B_ATTENDU or pv.get("instances") != [
            {"c": C_PREMIERE, "creation": CREATION_PREMIERE, "destruction": DESTRUCTION_PREMIERE, "id": "61049303"}]:
        raise SystemExit("poste-v5.json de la conduite v15 différent des instances antérieures : rien ne tourne")
    if ANTERIEURES[0]["creation"] != CREATION_PREMIERE or ANTERIEURES[0]["c"] != C_PREMIERE \\
            or ANTERIEURES[-1]["c"] != C_PREMIERE or len(ANTERIEURES) != (3 if OPTION_A else 1):
        raise SystemExit("instances antérieures non conformes à la création, au taux ou à l'option A : rien ne tourne")
    if OPTION_A:
        verifier_option_a(br)
    lignes = [l for l in durees.read_text(encoding="utf-8").splitlines() if l.strip()]
    tours = sorted(json.loads(l)["tour"] for l in lignes)
    if tours != list(range(TOURS_COMPLETS_PREMIERE)):
        raise SystemExit(f"journal des durées : tours {tours}, attendus 0 à {TOURS_COMPLETS_PREMIERE - 1}")
    regle = json.loads(m.read_text(encoding="utf-8"))["regle_tours"]
    tombees = []
    for f in (lus["journal/gardes-v3.jsonl"], lus["gardes-lanceur-v3.jsonl"]):
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip():
                e = json.loads(l)
                if e.get("etat") != "passée" and e.get("garde") not in tombees:
                    tombees.append(e.get("garde"))
    return {"tours_complets_premiere": TOURS_COMPLETS_PREMIERE, "regle_premiere": regle, "source": str(REPRISE),
            "instance_premiere": "61049303", "manifeste_regle": str(m.resolve()), "gardes_tombees_premiere": tombees}


def verifier_avant_pid() -> dict:
    """v16 : `relance_seule()` puis `lanceur_v21.verifier_relance_seule` (gardes « dépense », « sonde orientée », borne
    R-1), avant l'écriture du PID et avant toute création ; la `Conduite` la rejoue (sans effet de bord)."""
    rs = relance_seule()
    L.verifier_relance_seule(rs, L.instances_du_poste(ANTERIEURES, B_ATTENDU), B_ATTENDU)
    return rs'''
val = {"@OPTION_A@": repr(opt_a), "@OPTION_B@": repr(opt_b),
       "@ADD8@": f'DEPOT / "prereg" / "{add8.name}"' if add8 else "None", "@EMP8@": repr(emp8),
       "@ANT@": repr(ant), "@DESTR@": repr(destr), "@TA@": repr(T_A if opt_a else None),
       "@TR@": repr(t_redem), "@S@": repr(S_STOCKAGE if opt_a else None), "@AVANT@": repr(avant),
       "@REPRISE@": reprise, "@FOI@": foi, "@ATT@": repr(ATTENDUES), "@K1@": repr(k1)}
for x, y in val.items():
    exiger(BLOC.count(x) == 1, f"bloc v16 : {x}")
    BLOC = BLOC.replace(x, y)
rep('ANTERIEURES: list = []  # poste neuf (addendum 7, § 2.2) : D compte de zéro', BLOC)
rep('import os\n', 'import os\nimport re\n')
rep('    if T_MAX_PILOTE_S != 1800.0 or ANTERIEURES:\n        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures : rien ne tourne")',
    '    if T_MAX_PILOTE_S != 1800.0 or [i["id"] for i in ANTERIEURES] != ["61049303"] * (3 if OPTION_A else 1):\n'
    '        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures autres que 61049303 "\n'
    '                         "(une entrée ; trois avec l\'option A de l\'addendum 8) : rien ne tourne")\n'
    '    if (OPTION_A or OPTION_B) != (ADDENDUM_8 is not None):\n'
    '        raise SystemExit("option de l\'addendum 8 sans addendum, ou addendum sans option : rien ne tourne")\n'
    '    if ADDENDUM_8 is not None:\n'
    '        scellement.verifier(ADDENDUM_8)\n'
    '        if cv.sha_fichier(ADDENDUM_8) != EMPREINTE_ADDENDUM_8:\n'
    '            raise SystemExit("addendum 8 : empreinte différente de celle citée à la génération : rien ne tourne")')
rep('pidf = BASE / "lancement-v15.pid"', 'pidf = BASE / "lancement-v16.pid"')
rep('sortie = BASE / "sortie-conduite-v15"  # chemin absolu', 'sortie = BASE / "sortie-conduite-v16"  # chemin absolu')
rep('trace = BASE / "bilan-lancement-v15.json"', 'trace = BASE / "bilan-lancement-v16.json"')
rep('instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S)',
    'instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S,\n                          relance_seule=rs)')
rep('    pidf.write_text(f"{os.getpid()}\\n", encoding="utf-8")',
    '    rs = verifier_avant_pid()  # v16 : gardes de la relance avant l\'écriture du PID et avant toute création\n'
    '    pidf.write_text(f"{os.getpid()}\\n", encoding="utf-8")')
rep('    if conduite.relance_seule is not None or conduite.t_max_pilote_s != 1800.0:',
    '    if conduite.relance_seule is None or conduite.t_max_pilote_s != 1800.0:')
exiger("lancement-v15" not in c and "sortie-conduite-v16" in c and "@" + "ANT@" not in c, "conduite v16 : nom ancien resté")
compile(c, "lancer-conduite-v16.py", "exec")

p = (base / "poste-hetzner-v13.sh").read_text(encoding="utf-8")
h = "#!/bin/bash\n"
exiger(p.startswith(h), "poste v13 sans en-tête bash")
p = (h + "# Poste Hetzner du témoin de Bailey, v14 — RELANCE de la confirmation (R12 ; v1 à v13 restent telles quelles ;\n"
     "# addendum 7, § 2.1, chemin de l'addendum 5). v14 = v13 avec la conduite v16 (`lanceur_v21`, relance seule) et des\n"
     "# noms neufs (sortie `sortie-conduite-v16`, liste `repertoires-sortie-conduite-v16-v1.txt`), et la garde « reprise finie »\n"
     f"# (marque `{marque}` du poste de reprise qui a fait `{reprise}`). Généré par\n"
     "# `generer-pieces-relance-confirmation-bailey-v3.py`.\n"
     f"# {ligne_opts}.\n"
     "# Les commentaires d'origine plus bas ne sont pas mis à jour ; la clé\n"
     "# `cout_avec_200_go` de l'offre choisie porte le coût carte et 110 Go du § 2.4.\n" + p[len(h):])
corps = p.split("\nset -uo pipefail", 1)
exiger(len(corps) == 2, "poste v13 sans « set -uo pipefail »")
b = corps[1]
for x, z in (("sortie-conduite-v15", "sortie-conduite-v16"), ("lancement-v15", "lancement-v16"),
             ("lancer-conduite-v15", "lancer-conduite-v16"), ("offre-choisie-v13", "offre-choisie-v14"),
             ("poste-fini-v13", "poste-fini-v14"), ("poste-hetzner-v13", "poste-hetzner-v14")):
    exiger(b.count(x) >= 1, f"poste v13 : {x} absent")
    b = b.replace(x, z)
exiger(not re.search(r"sortie-conduite-v15|lancement-v15|lancer-conduite-v15|offre-choisie-v13|poste-fini-v13|poste-hetzner-v13", b),
       "poste v14 : nom ancien resté")
x = '# inventaire R10 : aucune instance du poste ne doit exister avant la création\n'
exiger(b.count(x) == 1, "poste v13 : ligne de l'inventaire R10 non unique")
b = b.replace(x, f'# v14 : la reprise de la confirmation ({reprise}) doit être finie (marque {marque}), sinon rien ne tourne\n'
              f'[ -s "$BASE/{marque}" ] || {{ etat "reprise de la confirmation non finie ({marque} absent) : rien ne tourne"; pousser "reprise non finie"; exit 3; }}\n' + x)
exiger(b.count(f'[ -s "$BASE/{marque}" ]') == 1 and "poste-fini-reprise-v4" not in b.replace(marque, ""),
       "poste v14 : garde « reprise finie » sans la marque donnée, ou ancienne marque restée")
if opt_b:
    x = 'd = [o for o in d if cout(o) <= 1.6]  # v13 : plafond de coût, carte et 110 Go (addendum 7, § 2.4)\n'
    exiger(b.count(x) == 1 and b.count("cout(o) <= 1.6") == 1, "poste v13 : ligne du plafond de coût non unique")
    b = b.replace(x, f'd = [o for o in d if cout(o) <= 1.4]  # v14 : plafond de coût de la relance, carte et 110 Go '
                     f'(addendum 8 {emp8[:8]}, § 2, B ; addendum 7, § 2.4)\n')
    exiger("cout(o) <= 1.6" not in b, "poste v14 : plafond 1,6 resté")
p = corps[0] + "\nset -uo pipefail" + b

k = (base / "construire-donnees-demarrage-v13.py").read_text(encoding="utf-8")
for x, z in (("v13 (R12 ; v1 à v12 restent telles\nquelles). v13 = v12", "v14 (R12 ; v1 à v13 restent telles\nquelles). v14 = v13"),
             ("et le nom du serveur.", f"et le nom du serveur (généré par\n`generer-pieces-relance-confirmation-bailey-v3.py` ; {ligne_opts})."),
             ("Lit `poste-hetzner-v1.sh`", "Lit `poste-hetzner-v14.sh`"),
             ('"poste-hetzner-v13.sh"', '"poste-hetzner-v14.sh"'), ("(`poste-hetzner-v13.sh`)", "(`poste-hetzner-v14.sh`)"),
             ('"poste-temoin-bailey-v13"', '"poste-temoin-bailey-v14"'), ('"temoin-bailey-v13"}', '"temoin-bailey-v14"}')):
    exiger(k.count(x) == 1, f"constructeur v13 : {x[:50]!r} non unique")
    k = k.replace(x, z)
compile(k, "construire-donnees-demarrage-v14.py", "exec")

exiger(not any((out / n).exists() for n in PIECES), "pièce apparue pendant la génération (R12)")
for n, texte in zip(PIECES, (c, p, k)):
    with open(out / n, "x", encoding="utf-8") as f:  # « x » : jamais d'écrasement (R12)
        f.write(texte)

print(ligne_opts)
print(f"D des antérieures (Poste.depense sur les {len(ant)} entrées) : {d_ant:.4f} USD")
if opt_a:
    plein = C1 * (destr - CREATION) / 3600
    print(f"option A : T_a = {T_A!r}, T_r = {t_redem!r}, s = {S_STOCKAGE!r} ; D au plein taux : {plein:.4f} USD ; "
          f"écart (c − s)(T_r − T_a) = {(C1 - S_STOCKAGE) * (t_redem - T_A) / 3600:.4f} USD")
plafond = 1.4 if opt_b else 1.6
ks = {}
for j in range(41):
    c_ = round(1.20 + 0.01 * j, 2)
    ks[c_] = an.nombre_de_tours(B, round(d_ant + 0.75 * c_, 4), c_, t_r)["K"]  # mise en place et contrôle du juge
cmax = max([c_ for c_, k_ in ks.items() if k_ >= 71], default=None)
print(f"t du pilote (manifeste de la règle) : {t_r!r}")
print("K selon c (D au calcul ≈ D des antérieures + 0,75 h × c) :", {c_: ks[c_] for c_ in (1.26, 1.33, 1.4, 1.45, 1.5, 1.55, 1.6)})
print(f"c maximal pour K ≥ 71 : {cmax} ; plafond de coût du poste v14 : {plafond}")
if cmax is None or cmax < plafond:
    print(f"ALERTE : au plafond de coût du poste (≤ {plafond} USD/h), K peut tomber sous 71 : relance non retenue "
          "(addendum 7, § 3) ; à porter dans la demande du mot de Lazar")
print("transfert qui fait foi :", foi)
print("empreintes fixées :", json.dumps(ATTENDUES, ensure_ascii=False, indent=1))
print("pièces :", {n: cv.sha_fichier(out / n) for n in PIECES})
print("ok")
