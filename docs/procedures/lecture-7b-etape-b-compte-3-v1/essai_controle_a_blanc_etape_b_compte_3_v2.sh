#!/usr/bin/env bash
# Essai (règle R5) de controle_a_blanc_etape_b_compte_3_v2.py (v2 ; l'essai v1 reste) : racine jouet **au format réel** (manifestes,
# résultats rattachés, audit, issue de P3-bis, fichier « mots et coût », épisodes et mesures valides au domaine du module), pour
# éprouver la section 9 (garde du module sur une copie du registre) ; artefacts de CL3-06 et de CL3-14. Aucune donnée du
# programme ; le dépôt réel n'est que lu (code, configuration v8, CODE-T07-v3.json, journal des ouvertures de l'étape A).
#     bash essai_controle_a_blanc_etape_b_compte_3_v2.sh <dépôt> <bac neuf> [<python avec torch>]
set -u
DEPOT=$(cd "$1" && pwd); BAC="$2"; PY="${3:-$DEPOT/.venv/bin/python}"
[ ! -e "$BAC" ] || { echo "ARRÊT : $BAC existe déjà"; exit 1; }
mkdir -p "$BAC"; BAC=$(cd "$BAC" && pwd)
SCRIPT="$DEPOT/docs/procedures/lecture-7b-etape-b-compte-3-v1/controle_a_blanc_etape_b_compte_3_v2.py"
CONFIG="$DEPOT/prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json"
export LC_ALL=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 GIT_AUTHOR_NAME=jouet GIT_AUTHOR_EMAIL=jouet@exemple.invalid GIT_COMMITTER_NAME=jouet GIT_COMMITTER_EMAIL=jouet@exemple.invalid
R6=20261111-151701-t06-reel; R7=20261114-001352-t07-lecture-reel; RMC=20261117-000000-t06-mots-et-cout
date -u +"début de l'essai : %Y-%m-%dT%H:%M:%SZ"; echo "script essayé : $(sha256sum "$SCRIPT" | cut -d' ' -f1)"
OK=0; KO=0
fabriquer() {   # $1 : racine neuve ; $2… : altérations nommées
PYTHONPATH="$DEPOT/src" "$PY" -B - "$DEPOT" "$@" <<'FIN'
import hashlib, json, pathlib, shutil, sys
import numpy as np
from controle_ia.manifeste import config_canonique
D, R = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]); alt = set(sys.argv[3:])
R6, R7, RMC = "20261111-151701-t06-reel", "20261114-001352-t07-lecture-reel", "20261117-000000-t06-mots-et-cout"
def sha(b): return hashlib.sha256(b).hexdigest()
def poser(rel, contenu):
    p = R / rel; p.parent.mkdir(parents=True, exist_ok=True)
    b = contenu if isinstance(contenu, bytes) else (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode() if not isinstance(contenu, str) else contenu.encode()
    p.write_bytes(b); (R / (rel + ".sha256")).write_text(f"{sha(b)}  {p.name}\n", encoding="utf-8"); return sha(b)
def manifeste(run, config):
    return poser(f"runs/{run}/manifeste.json", {"run_id": run, "commit": "0" * 40, "config": config,
                                                 "config_sha256": sha(config_canonique(config)), "graines": {}})
h6 = manifeste(R6, {"go_id": "GO-2026-11-08-11" if "go-7a" in alt else "GO-2026-11-02-28", "mode": "reel"})
poser(f"diag/{R6}/lecture-cout-t06.json", {"run_id": R6, "manifeste_sha256": "0" * 64 if "rattachement-faux" in alt else h6,
                                           "resultat": {"lecture": {"table_A": {"ligne": "A7" if "table-a-hors" in alt else "A5"}}}})
n = 10
cols = {"cle": np.array([f"k{i}" for i in range(n)]), "condition": np.array(["honnete", "S100"] * 5), "tache": np.array([f"t{i // 2}" for i in range(n)]),
        "pas": np.arange(n), "jetons_notes": np.full(n, 5), "mention_etendue": np.zeros(n, dtype=bool), "cout": np.linspace(1.0, 2.0, n)}
if "colonne-absente" in alt:
    cols.pop("cout")
tmp = R / "mesures-tmp.npz"; np.savez(tmp, **cols); hm = poser(f"donnees/{R6}/mesures-t06.npz", tmp.read_bytes()); tmp.unlink()
ht = poser(f"donnees/{R6}/textes-actions-t06.jsonl", '{"cle": "k0", "texte": "jouet"}\n')
poser(f"diag/{R6}/episodes-t06.json", {"run_id": R6, "manifeste_sha256": h6, "resultat": {
    "mesures": f"donnees/{R6}/mesures-t06.npz", "mesures_sha256": "1" * 64 if "mesures-empreinte" in alt else hm,
    "textes": f"donnees/{R6}/textes-actions-t06.jsonl", "textes_sha256": ht, "controles_negatifs": {}, "etats": {}, "fiches": []}})
lues = ["tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"]
h7 = manifeste(R7, {"sondes_lues": lues, "mode": "reel"})
hs = poser(f"diag/{R7}/sondes-t07.json", {"run_id": R7, "manifeste_sha256": h7, "resultat": {
    "sondes_lues": list(reversed(lues)) if "sondes-lues" in alt else lues, "niveau_applique": 0.9875, "concepts": ["tromperie", "enjeux"]}})
hsc = poser(f"donnees/{R7}/scores-actions-t07.npz", b"scores jouets, jamais ouverts par la section 9\n")
hc = poser("prereg/T0.7-consigne-audit-fuites-v1.md", "# consigne jouet\n")
jeu = {"fuite": "extrait jouet", "trait": "extrait", "separation": 0.5, "motif": "jouet"} if "audit-hors" in alt else {"fuite": None, "trait": None, "separation": None, "motif": "aucune fuite (jouet)"}
ha = poser(f"diag/{R7}/audit-fuites-t07.json", {"consigne": {"chemin": "prereg/T0.7-consigne-audit-fuites-v1.md", "sha256": hc},
                                                "jeux": {j: dict(jeu) for j in ("saboteur", "S25", "S50", "S75", "S100")}})
hv = poser("docs/verdicts/verdict-P3-bis-v1.md", "# verdict jouet\n")
hi = poser("docs/verdicts/verdict-P3-bis-v1-issue.json", {"issue": "vu", "ligne": 4, "verdict": "docs/verdicts/verdict-P3-bis-v1.md", "verdict_sha256": hv})
nc = {"aire_n029": None, "aire_mots_et_cout": None, "base_decisive": None, "aire": None, "bas": None, "haut": None, "niveau": 0.95,
      "quantile_plancher": None, "n_permutations": 100 if "issue-hors" in alt else 200, "seuil_aire": 0.7, "etat": "non calculable", "effet_cout": None}
him = poser(f"diag/{RMC}/issue-mots-et-cout-t06.json", {"issue_mots_et_cout": "M4", "phrase": "jouet", "doses": {d: dict(nc) for d in ("S25", "S50", "S75", "S100")}, "doses_qualifiees": []})
hp = poser("prereg/P3-bis-temoin-positif-v1.md", "# P3-bis jouet\n"); h07 = poser("prereg/T0.7-sondes-v0-v1.md", "# T0.7 jouet\n")
hcode = poser("registres/code-t07/CODE-T07-v3.json", (D / "registres/code-t07/CODE-T07-v3.json").read_bytes())
hjd = poser("donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl", "jouet\n")
go = "| GO-2026-11-10-06 | ligne de GO jouet |"; (R / "registres").mkdir(parents=True, exist_ok=True)
(R / "registres/go.md").write_text("# GO jouet\n\n" + go + "\n", encoding="utf-8"); hg = poser("registres/go-extraits/GO-LECTURE-T07-v1.md", go + "\n")
L = [("SCELLEMENT-JEUX-T07-JD", "2026-11-10T08:22:50Z", "donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl", hjd),
     ("GEL-T08", "2026-11-10T14:57:57Z", "registres/go.md", sha((R / "registres/go.md").read_bytes())),
     ("CODE-T07", "2026-11-13T23:42:46Z", "registres/code-t07/CODE-T07-v3.json", hcode),
     ("SCELLEMENT-T07", "2026-11-11T07:11:42Z", "prereg/T0.7-sondes-v0-v1.md", h07),
     ("CONSIGNE-AUDIT-FUITES-T07", "2026-11-11T14:08:06Z", "prereg/T0.7-consigne-audit-fuites-v1.md", hc),
     ("SCELLEMENT-P3BIS", "2026-11-11T15:52:30Z", "prereg/P3-bis-temoin-positif-v1.md", hp),
     ("RUN-CONFIRMATION-T06", "2026-11-13T18:52:43Z", f"runs/{R6}/manifeste.json", h6),
     ("GO-LECTURE-T07", "2026-11-13T18:52:44Z", "registres/go-extraits/GO-LECTURE-T07-v1.md", hg),
     ("SCORES-T07", "2026-11-14T01:55:05Z", f"donnees/{R7}/scores-actions-t07.npz", hsc),
     ("SONDES-T07", "2026-11-14T01:55:05Z", f"diag/{R7}/sondes-t07.json", hs),
     ("VERDICT-P3BIS", "2026-11-14T10:30:38Z", "docs/verdicts/verdict-P3-bis-v1-issue.json", hi),
     ("AUDIT-FUITES-T07", "2026-11-16T12:00:00Z", f"diag/{R7}/audit-fuites-t07.json", ha),
     ("ISSUE-MOTS-ET-COUT-T06", "2026-11-17T09:00:01Z", f"diag/{RMC}/issue-mots-et-cout-t06.json", him)]
if "ligne-autre" in alt:      # fichier et compagnon cohérents entre eux, mais autres que la ligne du registre
    p = R / f"diag/{RMC}/issue-mots-et-cout-t06.json"; b = p.read_bytes() + b" "; p.write_bytes(b)
    (R / f"diag/{RMC}/issue-mots-et-cout-t06.json.sha256").write_text(f"{sha(b)}  issue-mots-et-cout-t06.json\n", encoding="utf-8")
(R / "registres/scellements-v1.md").write_text("# Registre jouet\n\n" + "".join(f"| {k} | {d} | {c} | {h} |\n" for k, d, c, h in L), encoding="utf-8")
shutil.copy(D / "registres/scellements-v1.md.ouvertures.md", R / "registres/scellements-v1.md.ouvertures.md")
paq = "0" * 64 + " " + "1" * 64
ligne = (f"| OUVERTURE-P3BIS | 2026-11-14T10:15:23Z | pleine-anticipee | RENDEZ-VOUS-P3BIS-1={'2' * 64} | {paq} | - |" if "anticipee" in alt
         else f"| OUVERTURE-P3BIS | 2026-11-14T10:15:23Z | pleine | SCORES-T07={hsc} SONDES-T07={hs} | {paq} | - |")
(R / "registres/ouvertures-p3bis-v1.md").write_text("| clé | date | mode | appui | paquets | motif |\n|---|---|---|---|---|---|\n" + ligne + "\n", encoding="utf-8")
hb = poser("prereg/T0.7-etape-b-bis-v1.md", "plan jouet de l'étape B bis\n")
(R / "registres/etape-b-bis-v1.md").write_text(f"# Registre propre jouet\n\n| SCELLEMENT-PLAN-BBIS | 2026-11-17T08:00:00Z | prereg/T0.7-etape-b-bis-v1.md | {hb} |\n", encoding="utf-8")
if "arret-b" in alt: poser(f"diag/{R7}/arret-etape-b.json", "{}")
if "arret-t06" in alt: poser(f"diag/{R6}/arret.json", "{}")
print("racine jouet fabriquée")
FIN
}
cas() { local nom="$1" attendu="$2" motif="$3"; shift 3; local s c
    s=$(cd "$BAC" && PYTHONPATH="${PP:-$DEPOT/src}" "$PY" -B "$SCRIPT" "$@" 2>&1); c=$?
    if [ "$c" = "$attendu" ] && printf '%s' "$s" | grep -qF -- "$motif"; then OK=$((OK + 1)); echo "conforme : $nom (code $c)"
    else KO=$((KO + 1)); echo "ÉCART : $nom (code $c, attendu $attendu ; motif « $motif »)"; printf '%s\n' "$s" | tail -14 | sed 's/^/    /'; fi; }
INSTANT=2026-11-18T12:00:00Z
args() { echo --racine "$1" --registre "$1/registres/scellements-v1.md" --config "$CONFIG" --instant "$INSTANT" \
              --registre-bbis "$1/registres/etape-b-bis-v1.md" --cle-bbis SCELLEMENT-PLAN-BBIS --mode avant-etape-b; }
neuf() { fabriquer "$BAC/$1" "${@:2}" >/dev/null || { echo "ARRÊT : fabrication $1"; exit 1; }; echo "$BAC/$1"; }
J=$(neuf v1); cas "V1 racine valide, sans la section 9" 0 "CONTRÔLE À BLANC DE L'ÉTAPE B : TOUT CONFORME" $(args "$J")
cas "V1b plan de B bis : chemin non imprimé quand il est conforme (CL3-20)" 0 "fichier cité : sceau conforme" $(args "$J")
J=$(neuf v2); cas "V2 racine valide, section 9 : garde du module autorisée, lectures d'avant les scores conformes" 0 "AUTORISÉE" $(args "$J") --chaine --dossier-copie "$BAC/copie-v2"
[ "$(cmp -s "$J/registres/scellements-v1.md.ouvertures.md" "$DEPOT/registres/scellements-v1.md.ouvertures.md" && echo égal)" = égal ] \
    && [ "$(grep -c 'etape-B' "$BAC/copie-v2/scellements-v1.md.ouvertures.md")" = 1 ] && { OK=$((OK + 1)); echo "conforme : V2b le journal de la racine n'est pas touché ; la copie porte l'ouverture de la garde"; } \
    || { KO=$((KO + 1)); echo "ÉCART : V2b journaux"; }
J=$(neuf v3 rattachement-faux); cas "V3 lecture du coût rattachée à un autre manifeste (refus du module)" 2 "garde du module" $(args "$J") --chaine --dossier-copie "$BAC/copie-v3"
J=$(neuf v4 go-7a); cas "V4 manifeste de 7b au GO de 7a (refus du module)" 2 "course exploratoire 7a" $(args "$J") --chaine --dossier-copie "$BAC/copie-v4"
J=$(neuf v5 audit-hors); cas "V5 audit des fuites hors domaine (refus du module)" 2 "separation" $(args "$J") --chaine --dossier-copie "$BAC/copie-v5"
J=$(neuf v6 issue-hors); cas "V6 fichier « mots et coût » hors domaine (l'étape B écrirait L1)" 2 "illisible au domaine du module" $(args "$J") --chaine --dossier-copie "$BAC/copie-v6"
J=$(neuf v7 mesures-empreinte); cas "V7 empreinte des mesures autre que celle des épisodes" 2 "lecture d'avant les scores" $(args "$J") --chaine --dossier-copie "$BAC/copie-v7"
J=$(neuf v8 colonne-absente); cas "V8 colonne cout absente des mesures" 2 "colonne absente des mesures" $(args "$J") --chaine --dossier-copie "$BAC/copie-v8"
J=$(neuf v9 sondes-lues); cas "V9 sondes lues de sondes-t07.json autres que le manifeste de T0.7" 2 "sondes_lues" $(args "$J") --chaine --dossier-copie "$BAC/copie-v9"
J=$(neuf v10 table-a-hors); cas "V10 table A hors de A1 à A5 (l'étape B écrirait L1)" 2 "table A de T0.6 illisible ou arrêt" $(args "$J") --chaine --dossier-copie "$BAC/copie-v10"
J=$(neuf v11); cas "V11 section 9 avec un dossier de copie déjà présent" 2 "déjà présent" $(args "$J") --chaine --dossier-copie "$BAC/copie-v2"
# artefacts de CL3-14 (sans la section 9)
J=$(neuf c1 arret-b); cas "C1 arret-etape-b.json présent" 2 "arrêt de l'étape B déjà écrit" $(args "$J")
J=$(neuf c2 arret-t06); cas "C2 arret.json de T0.6 présent" 2 "arrêt de T0.6 présent" $(args "$J")
J=$(neuf c3 anticipee); cas "C3 ouverture pleine-anticipee de P3-bis au journal" 2 "anticipee" $(args "$J")
J=$(neuf c4 ligne-autre); cas "C4 empreinte de la ligne autre que celle du fichier (compagnon cohérent avec le fichier)" 2 "celle du registre" $(args "$J")
K="$BAC/code-modifie"; git clone -q --local --no-checkout "$DEPOT" "$K" && git -C "$K" sparse-checkout set src/controle_ia >/dev/null 2>&1 \
    && git -C "$K" -c advice.detachedHead=false checkout -q --detach c2fab6cc7267b76228a75dc3e2e08bc7aa038961 && echo "# altération d'essai" >> "$K/src/controle_ia/t07/registre_v1.py"
J=$(neuf c5); PP="$K/src" cas "C5 CODE-T07 : arbre du code exécuté modifié (copie jetable)" 2 "CODE-T07" $(args "$J"); unset PP
git -C "$K" checkout -q -- src/controle_ia/t07/registre_v1.py; J=$(neuf c6); PP="$K/src" cas "C6 CODE-T07 : copie jetable à C7, non modifiée" 0 "26 fichiers conformes" $(args "$J"); unset PP
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "ESSAI : TOUT CONFORME" || echo "ESSAI : ÉCARTS"
date -u +"fin de l'essai : %Y-%m-%dT%H:%M:%SZ"
