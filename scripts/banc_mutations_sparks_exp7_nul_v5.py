"""Banc de mutations de SPARKS-EXP7-NUL, v5 : tout le banc v4 (22 v1, 52 v2, 40 v3, 30 v4, inchangées, sur leurs essais) et
les mutations neuves de la v5 (lanceur, minuterie, addendum reconnu, durée réelle, tir ; contre-lecture du delta v4, points
12 et 14 à 24) sur les essais v5. « Tuée » seulement au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v5.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T5 = "tests/test_sparks_exp7_nul_v5.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v5.sh"
L = "scripts/lancer_sparks_exp7_nul_v5.sh"
R = "src/controle_ia/sparks_exp7_nul_v5/redemarrage.py"
TIR = "src/controle_ia/sparks_exp7_nul_v5/tir.py"


def _charger(nom):
    spec = importlib.util.spec_from_file_location(nom, RACINE / "scripts" / f"banc_mutations_sparks_exp7_nul_{nom[-2:]}.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V5 = [
    ("lanceur : clé de Vast retirée", L, "    for v in VAST_API_KEY HTTPS_PROXY", "    for v in HTTPS_PROXY", "cle_de_vast"),
    ("lanceur : certificat avant l'identifiant", L, '    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ]; then',
     '    if [ "$C" = 0 ] && [ -n "$ID" ] && [ "${OK:-0}" -ge 1 ] && ! grep -qiE "$CERT" "$F"; then', "apres_creation"),
    ("lanceur : refus de start ou destroy ignoré", L, '    elif grep -qiE "$REFUS" "$F" 2>/dev/null; then echo "$Q $5 REFUSÉ',
     '    elif false; then echo "$Q $5 REFUSÉ', "apres_commande or cle_de_vast"),
    ("lanceur : instance absente non reconnue", L, "        if grep -qiE 'no_such_instance|not found|404|",
     "        if false && grep -qiE 'no_such_instance|not found|404|", "lanceur_inventaire"),
    ("lanceur : inventaire sans comparaison", L, '    [ "$ETAT" = "$ATT" ] && exit 0 || exit 6 ;;', "    exit 0 ;;", "lanceur_inventaire"),
    ("lanceur : amorce lue dans l'arbre courant", L,
     '  --args bash -c "\\$(git show "$COMMIT:scripts/amorce_instance_sparks_exp7_nul_v5.sh")"',
     '  --args bash -c "\\$(cat scripts/amorce_instance_sparks_exp7_nul_v5.sh)"', "bornee_etiquetee"),
    ("lanceur : empreinte de l'addendum non passée", L, " -e ADDENDUM_SHA256=$SHA_A", "", "bornee_etiquetee"),
    ("lanceur : tir sans étiquette de tir", L, " --label sparks-exp7-nul-tir-$COURT", "", "tir_statique"),
    ("lanceur : tir sous le GO de la course", L, "GO_ID=$GOT timeout -k 10 300 $(prefixe_env) vastai create instance",
     "GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance", "tir_statique"),
    ("minuterie : corps du DELETE ignoré", A, "    refus=non; grep -qiE", "    refus=non; false && grep -qiE", "corps_success_false"),
    ("minuterie : tentative au-delà de la marge", A, 'if [ "$n" -gt 1 ] && [ $(( $(date +%s) + 190 )) -gt "$FIN" ]; then',
     "if false; then", "au_dela_de_la_marge"),
    ("amorce : addendum non exigé à la création", A, "    addendum_reconnu || {", "    true || {", "ordre_des_gardes"),
    ("addendum : empreinte non comparée", A, 'if [ -n "${ADDENDUM_SHA256:-}" ] && [ "$sa" = "$ADDENDUM_SHA256" ]; then',
     'if [ -n "${ADDENDUM_SHA256:-}" ]; then', "addendum_reconnu"),
    ("addendum : descendance de main au lieu de contenu dans main", A, 'merge-base --is-ancestor "$COMMIT" FETCH_HEAD',
     'merge-base --is-ancestor FETCH_HEAD "$COMMIT"', "addendum_reconnu"),
    ("addendum : exigé en jouet", A, '    [ "${MODE:-reel}" = jouet ] && { echo "AMORCE V5 : mode jouet : addendum non exigé"; return 0; }',
     "    true", "addendum_reconnu"),
    ("redémarrage : copie ou causal sans gardes passées", A, 'case "$PHASE_O" in copie|causal) [ -e "$R/sparks-v5-gardes-ok" ] ||',
     'case "$PHASE_O" in copie|causal) true ||', "gardes_passees"),
    ("durée réelle non consignée après le causal", A, "        code=$?; consigner_fin; echo", "        code=$?; echo",
     "duree_reelle_consignee or ordre_des_gardes"),
    ("fabrication non consignée avant le lancement", A, '    consigner_demarrage "$MINUTES"\n    echo "AMORCE V5 : fabrication',
     '    echo "AMORCE V5 : fabrication', "ordre_des_gardes"),
    ("copie non consignée avant le lot", A, '        consigner_demarrage "$((CM + 5))"\n', "", "ordre_des_gardes"),
    ("sparse-checkout sans timeout", A, 'timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" sparse-checkout set',
     'git -C "$R/amorce-depot" sparse-checkout set', "delais_ne"),
    ("checkout sans timeout", A, '&& timeout -k 10 "$T_GIT" git -C "$R/amorce-depot" checkout -q "$COMMIT"',
     '&& git -C "$R/amorce-depot" checkout -q "$COMMIT"', "delais_ne"),
    ("garde du GO sans timeout", A, 'go_conforme() { (cd "$R/amorce-depot" && timeout -k 5 "$T_GARDE" python3',
     'go_conforme() { (cd "$R/amorce-depot" && python3', "delais_ne"),
    ("témoin de minuterie antérieure retiré", A, '    echo "AMORCE V5 : TÉMOIN : minuterie antérieure',
     '    : "AMORCE V5 : TÉMOIN : minuterie antérieure', "temoin_minuterie"),
    ("borne : plafonds seuls, durées ignorées", R, "    return sum(durees.get(i, m) for i, m in plafonds.items())",
     "    return sum(plafonds.values())", "duree_reelle or coin_haut"),
    ("borne : durée sans plafond acceptée", R, "    if set(durees) - set(plafonds):\n", "    if False:\n", "duree_reelle"),
    ("tir : plafond au-delà de 5 USD accepté", TIR, "    if plafond > PLAFOND_MAX_USD:\n", "    if False:\n", "tir_go"),
    ("tir : devis au-delà du plafond accepté", TIR, "    if d > plafond:\n", "    if False:\n", "tir_go"),
    ("tir : durée hors bornes acceptée", TIR, "    if not MINUTES_MIN <= int(minutes) <= MINUTES_MAX:\n", "    if False:\n", "tir_go"),
    ("tir : GO hors validité accepté", TIR, "    if not a <= j <= e:\n", "    if False:\n", "tir_go"),
    ("tir : auteur du GO non contrôlé", TIR, '    if g["type"] != "calcul" or g["par"] != "Lazar":', '    if g["type"] != "calcul":', "tir_go"),
]


def main(argv: list[str]) -> int:
    b4 = _charger("banc_v4")
    b3 = b4._banc_v3()
    b2 = b3._banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in b3.T2_EN_PLUS]
              + [m + (b3.T3,) for m in b3.MUTATIONS_V3] + [m + (b4.T4,) for m in b4.MUTATIONS_V4]
              + [m + (T5,) for m in MUTATIONS_V5])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", b3.T3),
               ("témoin v4", None, None, None, "instance_de_cette_machine or espace_de_processus or lanceur", b4.T4),
               ("témoin v5", None, None, None, "duree_reelle or tir_go or addendum_reconnu or lanceur_inventaire", T5)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc5-") as t:
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
               "v3": {m[0] for m in b3.MUTATIONS_V3}, "v4": {m[0] for m in b4.MUTATIONS_V4}, "v5": {m[0] for m in MUTATIONS_V5}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
