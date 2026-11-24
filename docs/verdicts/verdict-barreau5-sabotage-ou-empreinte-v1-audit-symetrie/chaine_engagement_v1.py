"""Audit de symétrie (R4) du barreau 5, point 1 : chaîne de l'engagement.

N'affiche ni le sel ni aucune ligne de la table ; n'écrit que des booléens, des comptes et des empreintes déjà inscrites au
registre propre. Joué avec PYTHONPATH=<racine>/src (importe le paquet au code figé).
"""
import hashlib
import hmac
import json
import subprocess
import sys
from pathlib import Path

from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import lecture_v1 as le

TABLE = Path("/dev/shm/b5f-ouverture-v1/table/table-etiquettes-b5f-v1.json")
SEL = Path("/dev/shm/b5f-ouverture-v1/table/sel-barreau5-formation-v1.txt")
DEPOT = Path("/home/user/controle-ia-travail")
COMMIT = "8c758785d2d618b3666e909aa206a503b4a9f77a"
SEL_SHA_PREFIXE = "1516230c"
SORTIE = Path(sys.argv[1])


def main() -> None:
    r = {}
    octets = TABLE.read_bytes()
    sha_fichier = hashlib.sha256(octets).hexdigest()
    table = json.loads(octets.decode("utf-8"))
    sha_canon = en.empreinte_table(table)
    texte = subprocess.run(["git", "-C", str(DEPOT), "show", f"{COMMIT}:{en.REGISTRE_PROPRE}"], capture_output=True,
                           text=True, check=True).stdout
    lignes = en.lignes_du_registre(texte)
    eng = lignes["ENGAGEMENT-B5F"]["contenu"].split()[1]
    ouv = le._OUVERTURE.search(lignes["OUVERTURE-B5F"]["contenu"]).group("table")
    r["empreinte_fichier_table"] = sha_fichier
    r["empreinte_canonique_table"] = sha_canon
    r["engagement_registre"] = eng
    r["ouverture_registre"] = ouv
    r["fichier_egal_engagement"] = sha_fichier == eng
    r["canonique_egale_engagement"] = sha_canon == eng
    r["fichier_egal_ouverture"] = sha_fichier == ouv
    r["canonique_egale_ouverture"] = sha_canon == ouv
    r["fichier_est_forme_canonique"] = octets == en.forme_canonique(table)
    try:
        en.exiger_table_coherente(table)
        r["exiger_table_coherente"] = "passe"
    except Exception as x:          # noqa: BLE001
        r["exiger_table_coherente"] = f"refus : {type(x).__name__}"
    # sel du fichier à part
    sel_octets = SEL.read_bytes()
    sel = sel_octets.decode("ascii").strip()
    r["sel_fichier_octets"] = len(sel_octets)
    r["sel_fichier_sha256_prefixe_attendu"] = hashlib.sha256(sel_octets).hexdigest().startswith(SEL_SHA_PREFIXE)
    # l'empreinte du sel est citée dans la colonne « référence » de la ligne OUVERTURE-B5F (« sel sha256 1516230c… »)
    r["sel_fichier_sha256_cite_a_l_ouverture"] = (f"sel sha256 {hashlib.sha256(sel_octets).hexdigest()[:8]}"
                                                  in lignes["OUVERTURE-B5F"]["ref"])
    sels = {x["sel"] for x in table}
    r["sels_dans_la_table"] = len(sels)
    r["sel_fichier_egal_sel_table"] = sels == {sel}
    r["sel_256_bits_hexa"] = len(sel) == 64 and all(c in "0123456789abcdef" for c in sel)
    # noms opaques recalculés depuis le sel du fichier : par la fonction du module et par un calcul écrit ici
    adaptateurs = [(x["famille"], x["membre"]) for x in table]
    par_module = en.noms_opaques(sel, adaptateurs)
    cle = bytes.fromhex(sel)
    ordre = sorted(adaptateurs, key=lambda a: hmac.new(cle, f"{a[0]}/{a[1]}".encode(), hashlib.sha256).hexdigest())
    par_audit = {a: f"X-{k + 1:02d}" for k, a in enumerate(ordre)}
    r["noms_egaux_module"] = sum(par_module[(x["famille"], x["membre"])] == x["nom"] for x in table)
    r["noms_egaux_calcul_independant"] = sum(par_audit[(x["famille"], x["membre"])] == x["nom"] for x in table)
    r["lignes_table"] = len(table)
    r["adaptateurs_distincts"] = len(set(adaptateurs))
    r["noms_distincts"] = len({x["nom"] for x in table})
    r["noms_X01_a_X30"] = sorted(x["nom"] for x in table) == [f"X-{k:02d}" for k in range(1, 31)]
    r["familles_T01_T10_trois_membres"] = all(
        sorted(m for f, m in adaptateurs if f == t) == sorted(le.MEMBRES) for t in le.TENUES) and \
        {f for f, _ in adaptateurs} == set(le.TENUES)
    r["cles_par_ligne"] = sorted({tuple(sorted(x)) for x in table}) == [("famille", "membre", "nom", "sel")]
    # instants
    t = {k: lignes[k]["instant"] for k in ("ENGAGEMENT-B5F", "SCORES-B5F", "OUVERTURE-B5F")}
    r["instants"] = {k: v.strftime("%Y-%m-%dT%H:%M:%SZ") for k, v in t.items()}
    r["ordre_strict_engagement_scores_ouverture"] = t["ENGAGEMENT-B5F"] < t["SCORES-B5F"] < t["OUVERTURE-B5F"]
    try:
        v = en.verifier_table_a_l_ouverture(table, None, r["instants"]["OUVERTURE-B5F"], lignes=lignes)
        r["verifier_table_a_l_ouverture"] = f"passe ({v['adaptateurs']} adaptateurs)"
    except Exception as x:          # noqa: BLE001
        r["verifier_table_a_l_ouverture"] = f"refus : {x}"
    try:
        reg = le.lire_registre_de_lecture(texte)
        r["lire_registre_de_lecture"] = "passe"
        r["relance"] = reg["relance"]
        r["engagement_lecture_egal"] = reg["engagement"] == eng and reg["ouverture"]["table"] == ouv
    except Exception as x:          # noqa: BLE001
        r["lire_registre_de_lecture"] = f"refus : {x}"
    SORTIE.write_text(json.dumps(r, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
