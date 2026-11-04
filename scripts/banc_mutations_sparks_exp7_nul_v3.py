"""Banc de mutations de SPARKS-EXP7-NUL, v3 : les 22 mutations du banc v1 (essais v1), les 50 du banc v2 (essais v2),
inchangées, et les mutations neuves de la v3 (minuterie, amorce, redémarrages, M5, a priori de B3, gardes de la v2 sans
mutation : contre-lecture du delta v2, point 26) sur les essais v3. **« Tuée » seulement si l'essai ciblé sort avec le
code 1 et « failed »** (point 27 : un filtre qui ne sélectionne rien, code 5, n'est jamais compté tué). Témoins verts exigés.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v3.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T3 = "tests/test_sparks_exp7_nul_v3.py"
A = "scripts/amorce_instance_sparks_exp7_nul_v3.sh"
P2, P3 = "src/controle_ia/sparks_exp7_nul_v2/", "src/controle_ia/sparks_exp7_nul_v3/"


def _banc_v2():
    spec = importlib.util.spec_from_file_location("banc_v2", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v2.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MUTATIONS_V3 = [
    ("minuterie : repli sans -y", A, 'vastai destroy instance "$CONTAINER_ID" -y >/dev/null 2>&1; v=$?',
     'vastai destroy instance "$CONTAINER_ID" >/dev/null 2>&1; v=$?', "repli_vastai or aucun_arret"),
    ("minuterie : sortie brute de vastai gardée", A, 'vastai destroy instance "$CONTAINER_ID" -y >/dev/null 2>&1; v=$?',
     'vastai destroy instance "$CONTAINER_ID" -y >> "$J" 2>&1; v=$?', "repli_vastai"),
    ("minuterie jamais lancée", A,
     'setsid bash "$R/sparks-v3-minuterie.sh" "$ECH" "$R" "$API" < /dev/null >> "$R/sparks-v3-minuterie.log" 2>&1 &', "true",
     "apres_echeance"),
    ("curl non exigé", A, "command -v curl >/dev/null 2>&1 || {", "true || {", "sans_curl"),
    ("échéance non bornée par la fin du GO", A, '[ "$ECH" -le "$FIN_GO" ] || ECH=$FIN_GO', "true", "bornee_a_la_fin"),
    ("échéance relue de l'environnement au redémarrage", A, 'if [ -s "$E" ]; then read -r ECH < "$E"; else',
     'if false; then read -r ECH < "$E"; else', "ordre_fin_puis"),
    ("calcul après l'échéance", A, '[ "$(date +%s)" -lt "$ECH" ] || detruire "démarrage après l\'échéance : aucun calcul"',
     "true", "apres_echeance"),
    ("minuterie : identifiant non contrôlé", A, 'case "${CONTAINER_ID:-}" in \'\'|*[!0-9]*) echo "$(date -u +%FT%TZ) ALARME',
     'case "${CONTAINER_ID:-}" in \'\') echo "$(date -u +%FT%TZ) ALARME', "identifiant_illisible"),
    ("minuterie : pas de nouvel essai", A, '    sleep "$REESSAI"\ndone', "    exit 5\ndone", "recommence"),
    ("minuterie : ordre de la machine ignoré", A,
     'while [ "$(date +%s)" -lt "$ECH" ] && [ ! -e "$R/sparks-v3-detruire" ]; do sleep "$PAS"; done',
     'while [ "$(date +%s)" -lt "$ECH" ]; do sleep "$PAS"; done', "ordre_de_la_machine"),
    ("amorce : GO refusé sans arrêt", A,
     'go_conforme || { echo "AMORCE V3 : $GO_ID non conforme (base et extension à 40 USD) : aucun calcul"; exit 2; }',
     "go_conforme || true", "refus_avant_tout_calcul"),
    ("amorce : moins de 60 minutes accepté", A,
     '[ "$MINUTES" -ge 60 ] || { echo "AMORCE V3 : plafond trop bas pour ce prix ($MINUTES min) : aucun calcul"; exit 2; }',
     "true", "refus_avant_tout_calcul"),
    ("amorce : code refusé sans arrêt", A, '|| { echo "AMORCE V3 : code ou addendum non conformes : aucun calcul"; exit 2; }',
     "|| true", "refus_avant_tout_calcul"),
    ("redémarrage : commit du disque non vérifié", A, '[ "$(git -C "$R/amorce-depot" rev-parse HEAD)" = "$COMMIT" ] ||',
     "true ||", "commit_du_disque"),
    ("redémarrage : deja_usd de l'environnement", A, 'MINUTES=$(duree "$DEJA") ||', 'MINUTES=$(duree "${DEJA_USD:-0}") ||',
     "deja_usd_relu"),
    ("causal : destruction sans poussée vérifiée", A, 'if [ "$code" = 0 ] && [ -e "$T/POUSSEE-VERIFIEE" ]; then',
     'if [ "$code" = 0 ]; then', "poussee_verifiee"),
    ("lanceur : échéance au-delà du GO acceptée", "scripts/lancer_sparks_exp7_nul_v3.sh", '[ "$ECH" -le 1795046400 ] || {',
     "true || {", "lanceur_refuse"),
    ("ordre déjà fait rejoué", P3 + "redemarrage.py", 'if f and ordre["numero"] <= max(f):', "if False:", "deja_fait"),
    ("ordre : numéro ≠ nom accepté", P3 + "redemarrage.py", " or n != int(m.group(1)) or n < 1:", " or n < 1:", "ordres_sains"),
    ("ordre : fenêtre de copie non bornée", P3 + "redemarrage.py", "not 5 <= cm <= 60", "not 5 <= cm", "ordres_sains"),
    ("lot : couches du départ absentes du premier lot", P3 + "redemarrage.py", '    if ordre["premier"]:\n', "    if False:\n",
     "lot_de_copie"),
    ("lot : cas sans modèles accepté", P3 + "redemarrage.py", "    if not mods or not all(mods.values()):\n",
     "    if False:\n", "lot_de_copie"),
    ("B3 : a priori ignoré", P3 + "bases.py", "    o3 = a_priori if aire_ap >= 0.5 else -a_priori",
     "    o3 = 1 if aire >= 0.5 else -1", "a_priori_inverse"),
    ("instance : a priori non transmis", P3 + "instance.py", 'return -1 if rapport.get("construit") == "construit inversé" else 1',
     "return 1", "a_priori_transmis"),
    ("M5 secondaire absent", P3 + "analyse.py", '        sortie["increment_secondaire"][b]["m5"] = m5_secondaire(moy, sb[b]["scores"])',
     "        pass", "ajoute_m5"),
    ("M5 par c calculé sur la base", P3 + "analyse.py", '"M5_par_c": m5(C)', '"M5_par_c": m5(S)', "secondaire_m5"),
    ("format du secours : jeton de début gardé", P2 + "consignes.py",
     "    if tok.bos_token and s.startswith(tok.bos_token):\n        s = s[len(tok.bos_token):]\n", "", "jetons_de_l_outil"),
    ("durée : stockage non soustrait", P2 + "depense.py", "libre = PLAFOND_USD - deja_usd - stock", "libre = PLAFOND_USD - deja_usd",
     "duree_de_l_amorce"),
    ("durée : plafond de 24 h retiré", P2 + "depense.py", "return int(max(0.0, min(24 * 60, 0.9 * libre / prix_carte * 60)))",
     "return int(max(0.0, 0.9 * libre / prix_carte * 60))", "duree_de_l_amorce"),
    ("projection : stockage jusqu'au 16 au lieu du 18", P2 + "depense.py",
     "h_stock = max(0.0, (FIN_STOCKAGE - max(now, cree)).total_seconds() / 3600)",
     "h_stock = max(0.0, (NOEUD_DESTRUCTION - max(now, cree)).total_seconds() / 3600)", "stockage_jusqu"),
    ("destruction à l'échéance ignorée", P2 + "depense.py", "    if now >= FIN_STOCKAGE:\n        return {\"action\": \"detruire\"",
     "    if False:\n        return {\"action\": \"detruire\"", "stockage_jusqu"),
    ("coffre : droits 700 non exigés", P2 + "aveugle.py", "    if stat.S_IMODE(c.stat().st_mode) != 0o700:\n", "    if False:\n",
     "droits_700"),
    ("étalonnage : 4 contre 4 non exigé (v3)", P3 + "bases.py",
     '    if sorted(r for r in roles.values()) != ["honest"] * 4 + ["sycophant"] * 4:\n', "    if False:\n", "quatre_contre"),
    ("étalonnage : 4 contre 4 non exigé (v2)", P2 + "bases.py",
     '    if sorted(r for r in roles.values()) != ["honest"] * 4 + ["sycophant"] * 4:\n', "    if False:\n", "quatre_contre"),
    ("GO : type de l'extension non contrôlé", P2 + "go.py", ' and x["type"] == g["type"]', "", "extension_type_auteur"),
    ("GO : auteur de l'extension non contrôlé", P2 + "go.py", 'x["par"] == "Lazar"\n', "True\n", "extension_type_auteur"),
    ("GO : extension antérieure acceptée", P2 + "go.py", "and ax >= a and ex <= e):", "and ex <= e):", "extension_type_auteur"),
    ("code : commit cité en abrégé accepté", P2 + "garde_code.py", "    if commit_code not in texte:",
     "    if commit_code[:12] not in texte:", "cite_en_entier"),
    ("code : descendance non contrôlée", P2 + "garde_code.py",
     '"merge-base", "--is-ancestor", commit_code, lance]).returncode != 0:',
     '"merge-base", "--is-ancestor", commit_code, lance]).returncode != 0 and False:', "cite_en_entier"),
    ("étape 0 : code distant permis", P2 + "instance.py", "tok = AutoTokenizer.from_pretrained(str(d), trust_remote_code=False)",
     "tok = AutoTokenizer.from_pretrained(str(d), trust_remote_code=True)", "sans_code_distant"),
]
T2_EN_PLUS = [
    ("coffre : compte des bases non vérifié", P2 + "aveugle.py", "    if n != attendus:\n", "    if False:\n", "bases_au_coffre"),
    ("analyse : cas servi sans bases accepté", P2 + "analyse.py", "        if nom not in bases_poids:\n", "        if False:\n",
     "analyse_complete"),
]


def copier(dest: Path) -> None:
    shutil.copytree(RACINE / "src", dest / "src", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(RACINE / "tests", dest / "tests", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(RACINE / "scripts", dest / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy2(RACINE / "pyproject.toml", dest)
    shutil.copytree(RACINE / "docs/notes/sparks-exp7-nul-v1", dest / "docs/notes/sparks-exp7-nul-v1")
    for rel in ("prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md", "prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md.sha256",
                "registres/go.md"):
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, dest / rel)


def essai(dest: Path, k: str, fichier: str) -> tuple[int, str]:
    try:
        r = subprocess.run([sys.executable, "-I", "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", k, fichier],
                           cwd=dest, capture_output=True, text=True, timeout=900,
                           env={"PYTHONPATH": str(dest / "src"), "PATH": "/usr/sbin:/usr/bin:/sbin:/bin", "HOME": str(dest)})
    except subprocess.TimeoutExpired:
        return -1, "délai de 900 s dépassé"
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def main(argv: list[str]) -> int:
    b2 = _banc_v2()
    toutes = (b2.mutations_v1() + [m + (b2.T2,) for m in b2.MUTATIONS_V2] + [m + (b2.T2,) for m in T2_EN_PLUS]
              + [m + (T3,) for m in MUTATIONS_V3])
    temoins = [("témoin v1", None, None, None, "etiquette or egalite", b2.T1),
               ("témoin v2", None, None, None, "etats_de or go_sain or depense_cas_sain", b2.T2),
               ("témoin v3", None, None, None, "minuterie or ordres or a_priori", T3)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc3-") as t:
        base = Path(t) / "base"
        copier(base)
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
            code, fin = essai(d, k, fe)
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
    groupes = {"v1": [r for r in res if r["mutation"].startswith("v1 : ")]}
    n_v2 = len(b2.MUTATIONS_V2) + len(T2_EN_PLUS)
    noms_v2 = {m[0] for m in b2.MUTATIONS_V2 + T2_EN_PLUS}
    noms_v3 = {m[0] for m in MUTATIONS_V3}
    t1 = sum(1 for r in groupes["v1"] if r["statut"] == "TUÉE")
    t2 = sum(1 for r in res if r["mutation"] in noms_v2 and r["statut"] == "TUÉE")
    t3 = sum(1 for r in res if r["mutation"] in noms_v3 and r["statut"] == "TUÉE")
    print(f"{t1}/{len(b2.mutations_v1())} v1 ; {t2}/{n_v2} v2 ; {t3}/{len(MUTATIONS_V3)} v3 tuées (code 1 et « failed ») ; "
          f"défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
