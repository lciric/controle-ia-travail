"""Banc de mutations de SPARKS-EXP7-NUL, v9 : tout le banc v8 (bancs v1 à v8, inchangés, sur leurs essais et leurs
fichiers), et les mutations neuves de la v9 (protocole du tir : offres, prix, inventaire strict, verdict de boucle, sorties
brutes effacées, « no_such_ask », `start` lu, GO du tir, jeton écrit ; amorce : boucle détectée au redémarrage, redémarrage
consigné, identifiants de démarrage jamais réutilisés, ordre « fin » avant la borne, ordre consommé avant la borne, message de la phase causale) sur l'essai v9.
« Tuée » seulement au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v9.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T9 = "tests/test_sparks_exp7_nul_v9.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v9.sh"
I = "scripts/sparks_exp7_nul_instance_v9.sh"
L = "scripts/lancer_sparks_exp7_nul_v9.sh"
P9 = "src/controle_ia/sparks_exp7_nul_v9/"
V = P9 + "vast_lecture.py"


def _b8():
    spec = importlib.util.spec_from_file_location("banc_v8", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v8.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V9 = [
    # lecture des sorties de vastai
    ("inventaire : « instances: null » non lu comme absente", V,
     '        if donnees["instances"] is None:\n            return {"id": ident, "etat": "absente"',
     '        if donnees["instances"] is None:\n            raise Illisible("x")\n            return {"id": ident, "etat": "absente"',
     "lanceur_inventaire"),
    ("inventaire : identifiant non entier ignoré (faux « absente »)", V,
     "    if any(not isinstance(i.get(\"id\"), int) or isinstance(i.get(\"id\"), bool) for i in donnees):",
     "    if False:", "lanceur_inventaire"),
    ("inventaire : JSON non strict (texte d'erreur lu « absente »)", V, "        return json.loads(t)\n",
     "        return json.loads(t) if t.strip()[:1] in '[{' else {'instances': None}\n", "lanceur_inventaire"),
    ("lecture : sortie brute gardée", V, "    finally:\n        _effacer(brut)\n    try:\n        return json.loads(t)",
     "    finally:\n        pass\n    try:\n        return json.loads(t)", "efface_chaque"),
    ("lanceur : sortie brute des commandes gardée", L, 'effacer() { rm -f -- "$1" "$1.err"; }', "effacer() { :; }",
     "lanceur_apres_commande or lanceur_apres_creation"),
    ("offres : resource_type non contrôlé", V, '        if (o.get("resource_type") == "gpu" and o.get("num_gpus") == 1',
     '        if (o.get("num_gpus") in (0, 1)', "offres_filtrees"),
    ("offres : num_gpus non contrôlé", V, 'o.get("resource_type") == "gpu" and o.get("num_gpus") == 1 and',
     'o.get("resource_type") == "gpu" and', "offres_filtrees"),
    ("offres : prix du stockage sans les 20 Go", V, "float(o[\"storage_cost\"]) * DISQUE_GO / HEURES_PAR_MOIS",
     "float(o[\"storage_cost\"]) / HEURES_PAR_MOIS", "offres_filtrees or tir_commande"),
    ("offres : plus de quatre offres", V, "N_OFFRES = 4\n", "N_OFFRES = 5\n", "offres_filtrees"),
    ("boucle : durée minimale de 5 min ignorée", V, "DUREE_MIN_BOUCLE_S = 300\n", "DUREE_MIN_BOUCLE_S = 0\n",
     "verdict_de_boucle"),
    ("boucle : cur_state ignoré", V, 'if all(e == "exited" and c == "stopped" for _, e, c in lignes[-3:]):',
     'if all(e == "exited" for _, e, c in lignes[-3:]):', "verdict_de_boucle"),
    ("boucle : destruction sans -y", L,
     'echo "timeout -k 10 120 $(prefixe_env) vastai destroy instance $2 -y > \\"$ETAT_DIR/destruction-$2.txt\\" 2>&1; bash scripts/lancer_sparks_exp7_nul_v9.sh apres-commande destroy \\"$ETAT_DIR/destruction-$2.txt\\" \\$? $2" ;;',
     'echo "timeout -k 10 120 $(prefixe_env) vastai destroy instance $2 > \\"$ETAT_DIR/destruction-$2.txt\\" 2>&1; bash scripts/lancer_sparks_exp7_nul_v9.sh apres-commande destroy \\"$ETAT_DIR/destruction-$2.txt\\" \\$? $2" ;;',
     "verdict_de_boucle"),
    ("journal de l'amorce : motif ancré", V, '    lignes = [l.strip()[:200] for l in t.splitlines() if "AMORCE V5" in l]',
     '    lignes = [l.strip()[:200] for l in t.splitlines() if l.startswith("AMORCE V5")]', "journal_amorce"),
    # lanceur
    ("start : envoyé sans « starting instance <ID>. »", L,
     '    elif grep -qxF "$MOT" "$F" 2>/dev/null && ! grep -qiE "$REFUS" "$F" 2>/dev/null; then',
     '    elif ! grep -qiE "$REFUS" "$F" 2>/dev/null; then', "lanceur_apres_commande"),
    ("création : no_such_ask non reconnu (marqueur posé)", L,
     '    if [ -z "$ID" ] && [ "${OK:-0}" = 0 ] && [ "${NSA:-0}" -ge 1 ]; then',
     '    if false; then', "lanceur_apres_creation or no_such_ask"),
    ("création : cinquième offre après quatre no_such_ask", L, "            [0-9a-f]*:GO-*:*:[1-3])", "            [0-9a-f]*:GO-*:*:[1-4])",
     "no_such_ask"),
    ("tir : jeton de la session au lieu de CONTROLE_IA_GITHUB_TOKEN", L,
     "-e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\\$CONTROLE_IA_GITHUB_TOKEN -e DEPOT_URL", "-e ECHEANCE_UTC_S=$ECH -e GH_TOKEN=\\$GH_TOKEN -e DEPOT_URL",
     "tir_statique"),
    ("inventaire : show instance <id> au lieu de la liste", L,
     'echo "timeout -k 10 120 $(prefixe_env) vastai show instances --raw > \\"$ETAT_DIR/inventaire-$1.json\\"',
     'echo "timeout -k 10 120 $(prefixe_env) vastai show instance $1 --raw > \\"$ETAT_DIR/inventaire-$1.json\\"',
     "lanceur_apres_commande"),
    ("tir : tir.py v5 (sans périmètre)", L, 'L=$(timeout 120 python3 -I -B "$P9/tir.py" verifier', 'L=$(timeout 120 python3 -I -B "$P5/tir.py" verifier',
     "tir_statique or scripts_garde_v9"),
    ("tir.py v9 : périmètre non contrôlé", P9 + "tir.py", "    verifier_perimetre(chemin_go, go_id)\n    return t5.preparer(",
     "    return t5.preparer(", "perimetre_sparks"),
    # amorce
    ("amorce : boucle présumée sans destruction", A, '    detruire "redémarrage sans ordre neuf ($1)" 2; }', "    exit 2; }",
     "boucle_apres_une_creation"),
    ("amorce : redémarrage non consigné au registre", A, 'redemarrage.py" demarrage "$REG" "$ID_L" 5',
     'redemarrage.py" demarrage "$R/autre-registre.txt" "$ID_L" 5', "boucle_apres_une_creation"),
    ("amorce : durée du redémarrage non consignée", A, "trap fin_lancement EXIT\n", ":\n", "boucle_apres_une_creation"),
    ("amorce : ordre « fin » après la borne", A, '[ "$PHASE_O" = fin ] && detruire "ordre $NUM : fin"      # avant la borne (point 19)',
     ': fin traitée plus loin', "fin_avant_la_borne"),
    ("amorce : consignation de l'ordre impossible sans destruction", A, '    || boucle "consignation de l\'ordre impossible"',
     '    || { echo "AMORCE V5 : consignation de l\'ordre impossible"; exit 2; }', "deja_usd_plus_bas"),
    ("amorce : identifiant de démarrage = l'instant (redémarrage)", A, "ID_L=$(nouvel_id)\n", "ID_L=$(date +%s)\n",
     "meme_seconde"),
    ("amorce : identifiant de démarrage = l'instant (phase)", A, "ID_D=$(nouvel_id);", "ID_D=$(date +%s);", "meme_seconde"),
    ("amorce : identifiant neuf sans le registre", A, '[ "$n" -gt "$m" ] || n=$(( m + 1 )); echo "$n"; }', 'echo "$n"; }',
     "identifiants or meme_seconde"),
    ("amorce : création relancée sans contrôle", A, '    [ -e "$R/sparks-v9-creation-tentee" ] && boucle',
     '    [ -e "$R/sparks-v9-creation-tentee-x" ] && boucle', "creation_relancee"),
    ("amorce : ordres illisibles, refus sans destruction", A, '|| boucle "ordres illisibles (ou délai)"',
     '|| { echo "AMORCE V5 : ordres illisibles (ou délai) : boucle de redémarrage présumée"; exit 2; }', "branche_liee_au_commit_seulement"),
    ("amorce : message causal de la v8", A,
     'echo "AMORCE V5 $(date -u +%FT%TZ) : fin de la phase causale, code $code, poussée $POUSSEE"',
     'echo "AMORCE V5 $(date -u +%FT%TZ) : fin de la phase causale, code $code"', "message_exact"),
    ("amorce v9 : script d'instance v8 en fabrication", A,
     'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v9.sh"',
     'PHASE=fabrication BRANCHE="${PREFIXE}sparks-exp7-nul-v5-$COURT" bash "$R/amorce-depot/scripts/sparks_exp7_nul_instance_v8.sh"',
     "scripts_garde_v9 or v9_scripts"),
    ("instance v9 : essais v8 au lieu des essais v9", I, "tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v9.py >",
     "tests/test_sparks_exp7_nul_v4.py tests/test_sparks_exp7_nul_v8.py >", "scripts_garde_v9 or v9_scripts"),
    ("lanceur v9 : amorce v8 passée à la création", L,
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v9.sh")"',
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v8.sh")"', "bornee_etiquetee or v9_scripts"),
]


def main(argv: list[str]) -> int:
    b8 = _b8()
    b6 = b8._b6()
    b5 = b6._b5()
    b4 = b5._charger("banc_v4")
    b3 = b4._banc_v3()
    b2 = b3._banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in b3.T2_EN_PLUS]
              + [m + (b3.T3,) for m in b3.MUTATIONS_V3] + [m + (b4.T4,) for m in b4.MUTATIONS_V4]
              + [m + (b5.T5,) for m in b5.MUTATIONS_V5] + [m + (b6.T6,) for m in b6.MUTATIONS_V6]
              + [m + (b8.T8,) for m in b8.MUTATIONS_V7] + [m + (b8.T8,) for m in b8.MUTATIONS_V8]
              + [m + (T9,) for m in MUTATIONS_V9])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", b3.T3),
               ("témoin v4", None, None, None, "instance_de_cette_machine or espace_de_processus or lanceur", b4.T4),
               ("témoin v5", None, None, None, "duree_reelle or tir_go or addendum_reconnu or lanceur_inventaire", b5.T5),
               ("témoin v6", None, None, None, "scripts_garde_v6 or tir_go or lanceur or espace_de_processus", b6.T6),
               ("témoin v8", None, None, None, "trouve_le_paquet or aucun_appel or scripts_garde_v8 or manifeste or addendum_factice or v8_scripts", b8.T8),
               ("témoin v9", None, None, None, "lanceur or offres or boucle or journal_amorce or perimetre or no_such_ask or fin_avant "
                "or consomme or message_exact or creation_relancee or efface or ordre or scripts_garde_v9 or v9_scripts or tir_statique or identifiants or meme_seconde", T9)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc9-") as t:
        base = Path(t) / "base"
        b3.copier(base)
        for nom, fichier, ancien, nouveau, k, fe in temoins + toutes:
            d = Path(t) / "m"
            shutil.copytree(base, d)
            if fichier:
                f = d / fichier
                s = f.read_text(encoding="utf-8")
                if s.count(ancien) != 1:
                    res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": s.count(ancien)})
                    print(f"INAPPLICABLE {nom} ({s.count(ancien)} occurrences)", flush=True)
                    shutil.rmtree(d)
                    continue
                f.write_text(s.replace(ancien, nouveau), encoding="utf-8")
            code, fin = b3.essai(d, k, fe)
            if fichier is None:
                statut = "TEMOIN VERT" if code == 0 and "passed" in fin else "TEMOIN ROUGE"
            else:
                statut = "TUÉE" if code == 1 and "failed" in fin else "SURVIVANTE"
            res.append({"mutation": nom, "essais": k, "fichier_essais": fe, "statut": statut, "code": code, "fin": fin})
            print(f"{statut:12s} {nom} [{k}] code {code} : {fin}", flush=True)
            if argv:
                Path(argv[0]).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
            shutil.rmtree(d)
    mauvais = [r for r in res if r["statut"] not in ("TUÉE", "TEMOIN VERT")]
    groupes = {"v1": {m[0] for m in b2.mutations_v1()}, "v2": {m[0] for m in b2.MUTATIONS_V2 + b3.T2_EN_PLUS},
               "v3": {m[0] for m in b3.MUTATIONS_V3}, "v4": {m[0] for m in b4.MUTATIONS_V4}, "v5": {m[0] for m in b5.MUTATIONS_V5},
               "v6": {m[0] for m in b6.MUTATIONS_V6}, "v7": {m[0] for m in b8.MUTATIONS_V7}, "v8": {m[0] for m in b8.MUTATIONS_V8},
               "v9": {m[0] for m in MUTATIONS_V9}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
