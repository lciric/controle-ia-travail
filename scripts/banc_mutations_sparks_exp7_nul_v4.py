"""Banc de mutations de SPARKS-EXP7-NUL, v4 : tout le banc v3 (22 mutations v1, 52 v2, 40 v3, inchangées, sur leurs
essais) et les mutations neuves de la v4 (amorce, lanceur, ordres ; contre-lecture du delta v3, points 17 et 22, et liste
des changements) sur les essais v4. « Tuée » seulement au code 1 avec « failed » ; témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v4.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T4 = "tests/test_sparks_exp7_nul_v4.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v4.sh"
L = "scripts/lancer_sparks_exp7_nul_v4.sh"
R = "src/controle_ia/sparks_exp7_nul_v4/redemarrage.py"


def _banc_v3():
    spec = importlib.util.spec_from_file_location("banc_v3", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v3.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V4 = [
    ("clone sans timeout", A, 'timeout -k 10 "$T_GIT" git -c credential.helper="$AIDE" clone', 'git -c credential.helper="$AIDE" clone',
     "git_bloque or delais_ne"),
    ("lecture des ordres sans timeout", A, 'timeout -k 5 "$T_ORDRES" git -C "$R/amorce-depot" -c credential.helper="$AIDE" fetch',
     'git -C "$R/amorce-depot" -c credential.helper="$AIDE" fetch', "delais_ne"),
    ("lot sans timeout", A, 'timeout -k 10 "$T_LOT" python3 -I -B "$R/amorce-depot/$P4/redemarrage.py" lot',
     'python3 -I -B "$R/amorce-depot/$P4/redemarrage.py" lot', "delais_ne"),
    ("repli vastai sans timeout", A, "timeout -k 5 120 vastai destroy instance", "vastai destroy instance", "delais_ne"),
    ("délais allongeables par l'environnement", A, 'if [ "$1" -ge 1 ] && [ "$1" -le "$2" ]; then', 'if [ "$1" -ge 1 ]; then',
     "raccourcis_jamais"),
    ("attente du principal supprimée", A, 'echo "AMORCE V4 : destruction demandée ($1)"; attendre_minuterie;',
     'echo "AMORCE V4 : destruction demandée ($1)";', "espace_de_processus"),
    ("attente sur un numéro faux", A, "PM=$!\n", "PM=1\n", "espace_de_processus"),
    ("échéance non entière acceptée", A, 'case "$ECH" in \'\'|*[!0-9]*) echo "AMORCE V4 : ECHEANCE_UTC_S',
     'case "$ECH" in \'\') echo "AMORCE V4 : ECHEANCE_UTC_S', "non_entiere"),
    ("minuterie : succès 2xx ignoré", A, 'case "$c" in 2??) echo', 'case "$c" in 5??) echo', "succes_http"),
    ("branche des ordres sous calcul/", A, 'BRANCHE_ORDRES="ordres/sparks-exp7-nul-v4-$COURT"',
     'BRANCHE_ORDRES="calcul/sparks-exp7-nul-v3-ordres"', "branche_liee_au_commit_seulement"),
    ("préfixe des sorties non contrôlé", A, 'case "$PREFIXE" in calcul/|essai/) ;;', 'case "$PREFIXE" in *) ;;', "prefixe_des"),
    ("instance non transmise à la vérification", A, '"$R/sparks-v4-ordres-faits.txt" "$CONTAINER_ID")',
     '"$R/sparks-v4-ordres-faits.txt" 0)', "autre_instance or espace_de_processus"),
    ("consignation de l'ordre non contrôlée", A,
     '    || { echo "AMORCE V4 : consignation de l\'ordre impossible : rien ne part"; exit 2; }', "    || true", "consignation_impossible"),
    ("borne de la machine ignorée", A, 'DEJA_EFF=$(borne "$DEJA") ||', 'DEJA_EFF=$(echo "$DEJA") ||', "borne_de_la_machine"),
    ("démarrage causal non consigné", A, '        consigner_demarrage "$MINUTES"\n        timeout --signal=TERM',
     "        timeout --signal=TERM", "causal_branche_liee"),
    ("branche causale non liée à l'ordre", A, 'BRANCHE="${PREFIXE}sparks-exp7-nul-causal-v4-$COURT-$(printf %03d "$NUM")"',
     'BRANCHE="${PREFIXE}sparks-exp7-nul-causal-v4-$COURT"', "causal_branche_liee"),
    ("ordre : instance d'une autre machine acceptée", R, "    if instance is not None and i != str(instance):\n", "    if False:\n",
     "instance_de_cette_machine"),
    ("ordre : instance non numérique acceptée", R, "    if not isinstance(i, str) or not i.isdigit():\n", "    if False:\n",
     "instance_de_cette_machine"),
    ("ordre : deja_usd en baisse accepté", R, '    if f and float(ordre["deja_usd"]) < max(d for _, d in f):\n', "    if False:\n",
     "ne_baisse_jamais"),
    ("borne de la machine sans stockage", R, "    return minutes / 60 * prix_carte + (maintenant_s - creation_s) / 3600 * prix_stockage",
     "    return minutes / 60 * prix_carte", "borne_propre"),
    ("lanceur : identifiant non contrôlé", L, "identifiant() { case \"${1:-}\" in ''|*[!0-9]*)", "identifiant() { case \"${1:-}\" in '')",
     "lanceur_destruction"),
    ("lanceur : variables du mandataire retirées", L, "    for v in HTTPS_PROXY HTTP_PROXY NO_PROXY SSL_CERT_FILE REQUESTS_CA_BUNDLE; do",
     "    for v in NO_PROXY; do", "mandataire"),
    ("lanceur : environnement non nettoyé", L, "local p='env -i PATH=\"$PATH\" HOME=\"$HOME\" LANG=C.UTF-8' v",
     "local p='env PATH=\"$PATH\" HOME=\"$HOME\" LANG=C.UTF-8' v", "mandataire"),
    ("lanceur : certificat compté comme incertain", L, "    if grep -qiE 'CERTIFICATE_VERIFY_FAILED|", "    if false && grep -qiE 'CERTIFICATE_VERIFY_FAILED|",
     "apres_creation"),
    ("lanceur : marqueur non posé", L, '    echo "code $C $(date -u +%FT%TZ)" > "$MARQUEUR"', "    true", "apres_creation"),
    ("lanceur : succès sans « success »", L, '[ "${OK:-0}" -ge 1 ]', "true", "apres_creation"),
    ("lanceur : marqueur ignoré à la création", L, 'if [ "$QUOI" = creation ] && [ -e "$MARQUEUR" ]; then', "if false; then",
     "apres_un_marqueur"),
    ("lanceur : sortie de vastai affichée", L, '> "$F" 2>&1; bash scripts/lancer_sparks_exp7_nul_v4.sh apres-creation',
     '; bash scripts/lancer_sparks_exp7_nul_v4.sh apres-creation', "bornee_etiquetee"),
    ("lanceur : sans étiquette", L, " --label sparks-exp7-nul-v4-$COURT", "", "bornee_etiquetee"),
    ("lanceur : création sans timeout", L, "GO_ID=GO-2026-11-04-04 timeout -k 10 300 $(prefixe_env) vastai create instance",
     "GO_ID=GO-2026-11-04-04 $(prefixe_env) vastai create instance", "bornee_etiquetee"),
]


def main(argv: list[str]) -> int:
    b3 = _banc_v3()
    b2 = b3._banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in b3.T2_EN_PLUS]
              + [m + (b3.T3,) for m in b3.MUTATIONS_V3] + [m + (T4,) for m in MUTATIONS_V4])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", b3.T3),
               ("témoin v4", None, None, None, "instance_de_cette_machine or espace_de_processus or lanceur", T4)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc4-") as t:
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
               "v3": {m[0] for m in b3.MUTATIONS_V3}, "v4": {m[0] for m in MUTATIONS_V4}}
    print(" ; ".join(f"{sum(1 for r in res if r['mutation'] in g and r['statut'] == 'TUÉE')}/{len(g)} {n}"
                     for n, g in groupes.items()) + f" tuées (code 1 et « failed ») ; défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
