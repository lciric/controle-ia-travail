"""v16 — RELANCE de la confirmation (R12 ; v1 à v15 restent telles quelles ; addendum 7, § 2.1, par le chemin de
l'addendum 5 : relance seule, pièces neuves contre-lues ; générée par `generer-pieces-relance-confirmation-bailey-v3.py`).
options de l'addendum 8 retenues : B (addendum 8 `temoin-attaque-publiee-bailey-v1-addendum-8-plafond-cout-relance.md`, empreinte 44326b34ce42ddc67935d9a98b780ab7e06a27bb2b82329d70842af76668f537) ; A non retenue ; B : coût de l'offre au plus 1,40 USD/h.
La première exécution du run principal de la confirmation (conduite v15, instance 61049303) s'est interrompue avant
20 tours complets (K′ = 17) : compte Vast sans crédit, instance arrêtée par Vast le 17 novembre vers 17:12Z ; reprise
faite (`sortie-conduite-v15/reprise-v10-2/`). Conduite `lanceur_v21` avec `relance_seule` : amorce, auto-arrêt, mise en place
et contrôle du juge sur une instance neuve, puis, sans pilote ni règle sur l'instance, K recalculé par la règle (même
B = 85, D du poste, c de l'instance neuve, t du pilote de la première exécution) et `principal-relance`. Instance
antérieure : 61049303 (création relevée par la conduite v15, destruction écrite par la reprise).
Gardes d'entrée de la v15 (addendum 7 scellé, GO qui cite son empreinte entière, manifeste v7), plus celles de la
relance : addendum 8 scellé à l'empreinte citée, empreintes du manifeste de la règle et des journaux de
la reprise, exactement 17 lignes de durées (tours 0 à 16), gardes tombées lues sans note, destruction de 61049303
recoupée avec le bilan scellé de la reprise et `poste-v5.json`,
puis `lanceur_v21.verifier_relance_seule` (gardes « dépense » et « sonde orientée », borne R-1) ; jouées avant l'écriture
du PID et avant toute création (`verifier_avant_pid`). Sortie, bilan et PID neufs (`sortie-conduite-v16`,
`bilan-lancement-v16.json`, `lancement-v16.pid`). Elle ne lit aucune note.

Usage, détaché, depuis la racine du dépôt, sous `GO_ID=GO-2026-11-17-07`,
`DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`, `PYTHONPATH=<dépôt>/src`, venv Python 3.11 actif :

    python runs/temoin-bailey-v1-20261111/lancer-conduite-v16.py --offre <id> --image <image>
"""
import argparse
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

from controle_ia import scellement
from controle_ia.temoin_bailey import conventions_v3 as cv
from controle_ia.temoin_bailey import lanceur_v21 as L

DEPOT = Path("/home/user/controle-ia-travail")
BASE = DEPOT / "runs" / "temoin-bailey-v1-20261111"
GO_ID = "GO-2026-11-17-07"
ADDENDUM_7 = DEPOT / "prereg" / "temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md"
EMPREINTE_ADDENDUM_7 = "554a74d07c848c493c485f5f7c37d26dc419e7da381ee4180235adb76edd7f3e"
MANIFESTE = BASE / "manifeste-local-v7.json"
COMMIT_CODE = "a904aa391cdcf2650b747fe64e48caa0ec8c5849"  # addendum 7, § 4
B_ATTENDU = 85.0
T_MAX_PILOTE_S = 1800.0  # addendum 7, § 2.3
DISQUE_GO = 110  # disque demandé à Vast (Go)
# --- v16 : relance de la confirmation ---------------------------------------------------------------------------------
OPTION_A = False  # addendum 8, § 2, A : heures d'arrêt de 61049303 au taux du stockage (trois entrées)
OPTION_B = True  # addendum 8, § 2, B : coût de l'offre au plus 1,40 USD/h (filtre du poste v14 ; rien ici)
ADDENDUM_8 = DEPOT / "prereg" / "temoin-attaque-publiee-bailey-v1-addendum-8-plafond-cout-relance.md"  # None sans option
EMPREINTE_ADDENDUM_8 = '44326b34ce42ddc67935d9a98b780ab7e06a27bb2b82329d70842af76668f537'
# Instance de la première exécution (conduite v15) : création relevée par la conduite v15
# (`sortie-conduite-v15/poste-v5.json`), destruction écrite par la reprise ; même poste de dépense (addendum 7, § 2.2).
# Option A : trois entrées de même identifiant, dans l'ordre chronologique (`Poste.depense` les somme).
ANTERIEURES = [{'id': '61049303', 'c': 1.3247777777777778, 'creation': 1794907209.2755258, 'destruction': 1794969507.1907613, 'B': 85.0}]
C_PREMIERE = 1.3247777777777778
CREATION_PREMIERE = 1794907209.2755258
DESTRUCTION_PREMIERE = 1794969507.1907613  # bilan scellé de la reprise
T_ARRET = None  # A : champ t de la dernière ligne de sortie-conduite-v15/conduite-v5.jsonl
T_REDEMARRAGE = None  # A : redemarrage.debut du bilan scellé de la reprise
S_STOCKAGE = None  # A : storage_total_cost du relevé ci-dessous
RELEVE_STOCKAGE = BASE / "releve-stockage-61049303-20261118-0152.txt"
EMPREINTE_RELEVE = "002b9f58fbdc9b6afa24339617c8e6ef202180f699d376f0d0f5695e37aa273b"
REPRISES_AVANT = []  # A : reprises antérieures, qui n'ont pas redémarré l'instance
REPRISE = BASE / "sortie-conduite-v15" / "reprise-v10-2"
TRANSFERT = REPRISE / "principal" / "transfert-1"  # transfert qui fait foi (bilan de la reprise)
ATTENDUES = {'manifeste-v3-regle.json': '697460945f778be5042835771c640aedd309d6497901ebe96a330596ee25b3fb', 'sortie-durees-v3.jsonl': '92f2f8ba001d3e4fa9368108624e6fc87171e7e50e0b72d7109282f113922490', 'journal/gardes-v3.jsonl': '64673e5019563214ddbf8ef85588c653724a7ed9ac39f7bcab33a6e12519e969', 'gardes-lanceur-v3.jsonl': 'bc474c4d4846dfe58c505a110d271b402db1eaa29ba4a13f24c68aabee71f748'}  # empreintes relevées à la génération
TOURS_COMPLETS_PREMIERE = 17  # nombre de lignes du journal des durées transféré par la reprise


def verifier_option_a(br: dict) -> None:
    """Addendum 8, § 2, A : T_a, T_r, statut, reprises antérieures, relevé de stockage et contiguïté, revérifiés."""
    if br.get("statut") not in L.STATUTS_ARRETES or not isinstance(br.get("redemarrage"), dict) \
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
    if bc.get("detruite") is not False or not re.search(r"instance 61049303 arrêtée \(statut « (exited|stopped) »\)",
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
    if len(objs) != 1 or str(objs[0].get("id")) != "61049303" or objs[0].get("intended_status") != "stopped" \
            or float(objs[0].get("storage_total_cost")) != S_STOCKAGE:
        raise SystemExit("option A : relevé de stockage non conforme : rien ne tourne")
    for f in sorted(BASE.glob("releve-stockage-61049303-*.txt")):  # le plus haut des relevés fait foi
        scellement.verifier(f)
        for l in f.read_text(encoding="utf-8").splitlines():
            if l.strip() and not l.startswith("#") and float(json.loads(l).get("storage_total_cost", 0)) > S_STOCKAGE:
                raise SystemExit(f"option A : relevé {f.name} plus haut que s : rien ne tourne ; nœud")
    attendu =[("61049303", C_PREMIERE, CREATION_PREMIERE, T_ARRET), ("61049303", S_STOCKAGE, T_ARRET, T_REDEMARRAGE),
               ("61049303", C_PREMIERE, T_REDEMARRAGE, DESTRUCTION_PREMIERE)]
    if [(i["id"], i["c"], i["creation"], i["destruction"]) for i in ANTERIEURES] != attendu \
            or not CREATION_PREMIERE < T_ARRET < T_REDEMARRAGE < DESTRUCTION_PREMIERE \
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
    if br.get("instance") != "61049303" or br.get("detruite") is not True \
            or float(br["destruction"]) != DESTRUCTION_PREMIERE or ANTERIEURES[-1]["destruction"] != DESTRUCTION_PREMIERE:
        raise SystemExit("destruction de 61049303 différente du bilan scellé de la reprise : rien ne tourne")
    if ((br.get("transferts") or {}).get("principal") or {}).get("foi") != TRANSFERT.name:
        raise SystemExit("transfert qui fait foi différent du bilan scellé de la reprise : rien ne tourne")
    pv = json.loads((BASE / "sortie-conduite-v15" / "poste-v5.json").read_text(encoding="utf-8"))
    if float(pv.get("b", -1)) != B_ATTENDU or pv.get("instances") != [
            {"c": C_PREMIERE, "creation": CREATION_PREMIERE, "destruction": DESTRUCTION_PREMIERE, "id": "61049303"}]:
        raise SystemExit("poste-v5.json de la conduite v15 différent des instances antérieures : rien ne tourne")
    if ANTERIEURES[0]["creation"] != CREATION_PREMIERE or ANTERIEURES[0]["c"] != C_PREMIERE \
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
    return rs


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
    if T_MAX_PILOTE_S != 1800.0 or [i["id"] for i in ANTERIEURES] != ["61049303"] * (3 if OPTION_A else 1):
        raise SystemExit("plafond de durée du pilote différent de 1 800 s, ou instances antérieures autres que 61049303 "
                         "(une entrée ; trois avec l'option A de l'addendum 8) : rien ne tourne")
    if (OPTION_A or OPTION_B) != (ADDENDUM_8 is not None):
        raise SystemExit("option de l'addendum 8 sans addendum, ou addendum sans option : rien ne tourne")
    if ADDENDUM_8 is not None:
        scellement.verifier(ADDENDUM_8)
        if cv.sha_fichier(ADDENDUM_8) != EMPREINTE_ADDENDUM_8:
            raise SystemExit("addendum 8 : empreinte différente de celle citée à la génération : rien ne tourne")


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
        print(f"outils introuvables dans le PATH : {manquants} : rien ne tourne", file=sys.stderr)
        return 2
    texte_go = L.texte_go_main(DEPOT)
    gardes_d_entree(texte_go)
    pidf = BASE / "lancement-v16.pid"
    sortie = BASE / "sortie-conduite-v16"  # chemin absolu, le même pour `reprendre` (A-1)
    trace = BASE / "bilan-lancement-v16.json"
    if pidf.exists() or trace.exists():
        print("PID ou bilan de lancement déjà présent (R12) : rien ne tourne", file=sys.stderr)
        return 2
    rs = verifier_avant_pid()  # v16 : gardes de la relance avant l'écriture du PID et avant toute création
    pidf.write_text(f"{os.getpid()}\n", encoding="utf-8")
    conduite = L.Conduite(fournisseur=FournisseurVastReprises(), manifeste_local=MANIFESTE, sortie=sortie, go_id=GO_ID,
                          texte_go=texte_go, offre=str(a.offre), image=a.image, depot_local=DEPOT,
                          instances_anterieures=ANTERIEURES, disque_go=DISQUE_GO, t_max_pilote_s=T_MAX_PILOTE_S,
                          relance_seule=rs)
    if conduite.relance_seule is None or conduite.t_max_pilote_s != 1800.0:
        print("conduite mal construite : rien ne tourne", file=sys.stderr)
        return 2
    debut = time.time()
    try:
        bilan = conduite.conduire()
        issue = {"bilan": bilan}
    except Exception as err:  # la conduite a déjà fait `_finir` ; on consigne l'erreur sans valeur de note
        issue = {"erreur": f"{type(err).__name__}: {err}"[:500]}
    issue.update({"offre": a.offre, "image": a.image, "debut": debut, "fin": time.time(), "pid": os.getpid()})
    trace.write_text(json.dumps(issue, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                     encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
