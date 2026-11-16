#!/usr/bin/env bash
# Répétition de bout en bout, sur dépôts jouets, de tous les blocs de commande-compte-3-phase-c-v4.md (constat CL3-07, bloquant pour la
# phase C ; CL3-04 et CL3-05 éprouvés), plus le bloc M de la mère. Écrite le 2026-11-14 par le préparateur (modèle A) ; v3 (à partir de
# 13:04:29Z) : la v2 (7a9da180…, gardée) plus les artefacts des gardes de 2C, C0, C5 et C7 (règle R5). v4 (2026-11-16, rédacteur de la
# commande v4, modèle B ; décision R-2980) : la v3 (8be57168…, gardée) avec trois changements seulement : le chemin de la commande à
# répéter est le troisième argument (un brouillon, ou la version définitive), son contenu est placé dans le main jouet sous le nom
# définitif commande-compte-3-phase-c-v4.md, et le bordereau attendu compte 29 fichiers, sondes-t07.json et son compagnon compris.
# Aucune donnée réelle :
# dépôt distant jouet à quatre branches (main jouet dont le premier commit porte le code de src/controle_ia du dépôt réel, qui tient lieu de
# C7 ; 7b jouet ; étape A jouet ; phase B jouet), fichiers au format réel et petits ; module d'étape B jouet (etape_b_jouet_v1.py) qui joue la
# VRAIE garde lecture_v4.ouvrir, attend, puis écrit lecture-t07.json par la vraie fonction. Surcharges, et seulement elles, en fin de
# variables-v2.sh après le bloc 1C : DEPOT_URL, TETE_7B, TETE_EA, C7, H_SCORES, H_SONDES, MODULE_ETAPE_B, PYTHONPATH_SUP (et BR_B à la
# seconde passe) ; marqueurs du bloc 1C remplis ; variables de tête du bloc F-C remplies ; adresse du dépôt distant du bloc M.
#     bash repetition_phase_c_jouet_v4.sh <dépôt réel> <bac neuf> <commande à répéter>
set -u
DEPOT_REEL=$(cd "$1" && pwd); T="$2"; CMD=$(realpath -e -- "$3") || { echo "ARRÊT : commande à répéter introuvable"; exit 1; }
[ ! -e "$T" ] || { echo "ARRÊT : $T existe déjà"; exit 1; }
mkdir -p "$T"; T=$(cd "$T" && pwd)
export LC_ALL=C.UTF-8 GIT_AUTHOR_NAME=jouet GIT_AUTHOR_EMAIL=jouet@exemple.invalid GIT_COMMITTER_NAME=jouet GIT_COMMITTER_EMAIL=jouet@exemple.invalid
ICI_REL=docs/procedures/lecture-7b-etape-b-compte-3-v1; echo "commande répétée : $CMD (placée dans le main jouet sous le nom commande-compte-3-phase-c-v4.md)"
R6=20261111-151701-t06-reel; R7=20261114-001352-t07-lecture-reel; RMC=20261117-000000-t06-mots-et-cout
BRP=verdict/t06-mots-et-cout-compte-3-v1
date -u +"début de la répétition : %Y-%m-%dT%H:%M:%SZ"
mkdir -p "$T/blocs" "$T/stub"; cp "$DEPOT_REEL/$ICI_REL/etape_b_jouet_v1.py" "$T/stub/"
python3 -I - "$CMD" "$T/blocs" <<'FIN'
import hashlib, pathlib, re, sys
t = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"); b = re.findall(r"```bash\n(.*?)```", t, re.S)
for i, x in enumerate(b):
    pathlib.Path(sys.argv[2], f"b{i:02d}.sh").write_text(x, encoding="utf-8")
print(f"commande : {hashlib.sha256(t.encode()).hexdigest()} ; {len(b)} blocs ; blocs mis bout à bout : {hashlib.sha256(''.join(b).encode()).hexdigest()}")
FIN
B="$T/blocs"   # b00 0b-C, b01 1C, b02 2C, b03 C0, b04 C1a, b05 C1, b06 C2, b07 C3, b08 C4a, b09 C4-attente, b10 C4b, b11 C5, b12 C6, b13 C7, b14 F-C, b15 bloc M
DIST="$T/distant/lciric/controle-ia-travail.git"; mkdir -p "$(dirname "$DIST")"
git init -q --bare "$DIST"; git -C "$DIST" symbolic-ref HEAD refs/heads/main; git -C "$DIST" config uploadpack.allowFilter true; git -C "$DIST" config uploadpack.allowAnySHA1InWant true
W="$T/travail"; git init -q -b main "$W"
# 1) premier commit de main : le code (src/controle_ia du dépôt réel) — il tient lieu de C7
(cd "$DEPOT_REEL" && git ls-files -z src/controle_ia | xargs -0 -I{} cp --parents {} "$W/"); cp "$DEPOT_REEL/.gitignore" "$W/"
git -C "$W" add -A >/dev/null; git -C "$W" commit -q -m "code jouet (tient lieu de C7)"; C7J=$(git -C "$W" rev-parse HEAD)
# 2) branches de données jouets et pièces de main, par programme (formats réels)
PYTHONPATH="$DEPOT_REEL/src" "$DEPOT_REEL/.venv/bin/python" -B - "$DEPOT_REEL" "$W" "$C7J" "$T" "$CMD" <<'FIN'
import hashlib, json, pathlib, shutil, subprocess, sys
import numpy as np
from controle_ia.manifeste import config_canonique
D, W, C7J, T = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3], pathlib.Path(sys.argv[4])
R6, R7, RMC = "20261111-151701-t06-reel", "20261114-001352-t07-lecture-reel", "20261117-000000-t06-mots-et-cout"
def git(*a): return subprocess.run(["git", "-C", str(W), *a], check=True, capture_output=True, text=True).stdout.strip()
def sha(b): return hashlib.sha256(b).hexdigest()
def poser(rel, contenu):
    p = W / rel; p.parent.mkdir(parents=True, exist_ok=True)
    b = contenu if isinstance(contenu, bytes) else contenu.encode() if isinstance(contenu, str) else (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode()
    p.write_bytes(b); (W / (rel + ".sha256")).write_text(f"{sha(b)}  {p.name}\n", encoding="utf-8"); return sha(b)
def manifeste(run, config):
    return poser(f"runs/{run}/manifeste.json", {"run_id": run, "commit": "0" * 40, "config": config, "config_sha256": sha(config_canonique(config)), "graines": {}})
def orpheline(nom):
    git("switch", "-q", "--orphan", nom); subprocess.run(["git", "-C", str(W), "rm", "-rq", "."], capture_output=True)
    for x in W.iterdir():
        if x.name != ".git": shutil.rmtree(x) if x.is_dir() else x.unlink()
def pousser(nom, msg):
    git("add", "-A"); git("commit", "-q", "-m", msg); subprocess.run(["git", "-C", str(W), "push", "-q", str(T / "distant/lciric/controle-ia-travail.git"), nom], check=True, capture_output=True)
    return git("rev-parse", "HEAD")
v = {}
# branche de 7b jouet
orpheline("calcul/t06-confirmation-7b-v1")
h6 = manifeste(R6, {"go_id": "GO-2026-11-02-28", "mode": "reel"})
poser(f"diag/{R6}/lecture-cout-t06.json", {"run_id": R6, "manifeste_sha256": h6, "resultat": {"lecture": {"table_A": {"ligne": "A5"}}}})
n = 10; cols = {"cle": np.array([f"k{i}" for i in range(n)]), "condition": np.array(["honnete", "S100"] * 5), "tache": np.array([f"t{i // 2}" for i in range(n)]),
                "pas": np.arange(n), "jetons_notes": np.full(n, 5), "mention_etendue": np.zeros(n, dtype=bool), "cout": np.linspace(1.0, 2.0, n)}
np.savez(T / "mesures.npz", **cols); hm = poser(f"donnees/{R6}/mesures-t06.npz", (T / "mesures.npz").read_bytes())
ht = poser(f"donnees/{R6}/textes-actions-t06.jsonl", '{"cle": "k0", "texte": "jouet"}\n')
poser(f"diag/{R6}/episodes-t06.json", {"run_id": R6, "manifeste_sha256": h6, "resultat": {"mesures": f"donnees/{R6}/mesures-t06.npz", "mesures_sha256": hm,
       "textes": f"donnees/{R6}/textes-actions-t06.jsonl", "textes_sha256": ht, "controles_negatifs": {}, "etats": {}, "fiches": []}})
for f in (f"diag/{R6}/lecture-sondes-t06.json", f"diag/{R6}/resume.json", f"donnees/{R6}/adaptateur-saboteur.pt"): poser(f, "fichier fermé jouet\n")
v["TETE_7B"] = pousser("calcul/t06-confirmation-7b-v1", "7b jouet")
# branche de l'étape A jouet : manifeste, sondes-t07.json rattaché, scores en trois morceaux
orpheline("donnees/t07-etape-a-v1")
lues = ["tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"]
h7 = manifeste(R7, {"sondes_lues": lues, "mode": "reel"})
v["H_SONDES"] = poser(f"diag/{R7}/sondes-t07.json", {"run_id": R7, "manifeste_sha256": h7, "resultat": {"sondes_lues": lues, "niveau_applique": 0.9875, "concepts": ["tromperie", "enjeux"]}})
scores = bytes(range(256)) * 1200; v["H_SCORES"] = sha(scores); d = W / "donnees" / R7; d.mkdir(parents=True)
(d / "scores-actions-t07.npz.sha256").write_text(f"{sha(scores)}  scores-actions-t07.npz\n", encoding="utf-8")
morceaux = []
for i in range(3):
    m = scores[i * 110000:(i + 1) * 110000]; nom = f"scores-actions-t07.npz.morceau-{i:03d}"
    (d / nom).write_bytes(m); (d / (nom + ".sha256")).write_text(f"{sha(m)}  {nom}\n", encoding="utf-8"); morceaux.append({"fichier": nom, "octets": len(m), "sha256": sha(m)})
poser(f"donnees/{R7}/scores-actions-t07.npz.morceaux.json", {"octets": len(scores), "morceaux": morceaux})
v["TETE_EA"] = pousser("donnees/t07-etape-a-v1", "étape A jouet")
# branche de la phase B jouet : fichier « mots et coût » et base (A)
orpheline("verdict/t06-mots-et-cout-compte-3-v1")
nc = {"aire_n029": None, "aire_mots_et_cout": None, "base_decisive": None, "aire": None, "bas": None, "haut": None, "niveau": 0.95,
      "quantile_plancher": None, "n_permutations": 200, "seuil_aire": 0.7, "etat": "non calculable", "effet_cout": None}
him = poser(f"diag/{RMC}/issue-mots-et-cout-t06.json", {"issue_mots_et_cout": "M4", "phrase": "jouet", "doses": {x: dict(nc) for x in ("S25", "S50", "S75", "S100")}, "doses_qualifiees": []})
hba = poser(f"diag/{RMC}/base-a-t08.json", {"lignes": {"BA-L2": {"s_applique": False, "phrase": "jouet"}}, "aires": {"secret": 0.777}})
pousser("verdict/t06-mots-et-cout-compte-3-v1", "phase B jouet")
# main jouet : pièces, registres, liste v3, consigne B, audit (copié par la mère), décision BA-L2, plan de B bis
git("switch", "-q", "main")
for f in ("docs/sha256sums-lancement-v2.txt", "docs/brief-claude-code-programme-complet-v2.md", "docs/programme-controle-ia-v2.md", "docs/etat-de-l-art-controle-ia-v1.md",
          "prereg/T0.7-sondes-v0-v1.md", "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md", "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json",
          "prereg/T0.6-organismes-v0-v1.md", "prereg/T0.8-base-A-mots-et-cout-v1.md", "docs/decisions/decision-N-063-v2.md", "requirements-cpu.txt",
          "docs/procedures/lecture-7b-etape-b-compte-3-v1/controle_a_blanc_etape_b_compte_3_v2.py",
          "docs/procedures/lecture-7b-etape-b-compte-3-v1/attestation_qui_a_lu_quoi_compte_3_v3.py", "docs/procedures/lecture-7b-etape-b-compte-3-v1/lecture_etat_ba_l2_mere_v1.py"):
    (W / f).parent.mkdir(parents=True, exist_ok=True); shutil.copy(D / f, W / f)
    if (D / (f + ".sha256")).exists(): shutil.copy(D / (f + ".sha256"), W / (f + ".sha256"))
poser("docs/procedures/lecture-7b-etape-b-compte-3-v1/commande-compte-3-phase-c-v4.md", pathlib.Path(sys.argv[5]).read_bytes())   # la commande répétée, sous son nom définitif
hc = poser("prereg/T0.7-consigne-audit-fuites-v1.md", "# consigne d'audit jouet\n")
ha = poser(f"diag/{R7}/audit-fuites-t07.json", {"consigne": {"chemin": "prereg/T0.7-consigne-audit-fuites-v1.md", "sha256": hc},
       "jeux": {j: {"fuite": None, "trait": None, "separation": None, "motif": "aucune fuite (jouet)"} for j in ("saboteur", "S25", "S50", "S75", "S100")}})
hv = poser("docs/verdicts/verdict-P3-bis-v1.md", "# verdict jouet\n")
hi = poser("docs/verdicts/verdict-P3-bis-v1-issue.json", {"issue": "vu", "ligne": 4, "verdict": "docs/verdicts/verdict-P3-bis-v1.md", "verdict_sha256": hv})
hp = poser("prereg/P3-bis-temoin-positif-v1.md", "# P3-bis jouet\n")
code = json.loads((D / "registres/code-t07/CODE-T07-v3.json").read_text(encoding="utf-8")); code["commit"] = C7J
hcode = poser("registres/code-t07/CODE-T07-jouet.json", code)
hjd = poser("donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl", "jouet\n"); hcm = poser("docs/notes/jouet/code-mots-et-cout.json", "{}\n")
hcb = poser("docs/procedures/jouet/consigne-lecteur-etape-b-jouet-v1.md", "# consigne jouet du lecteur B\n")
go = "| GO-2026-11-10-06 | ligne de GO jouet |"; (W / "registres").mkdir(exist_ok=True); (W / "registres/go.md").write_text("# GO jouet\n\n" + go + "\n", encoding="utf-8")
hg = poser("registres/go-extraits/GO-LECTURE-T07-v1.md", go + "\n")
L = [("SCELLEMENT-JEUX-T07-JD", "2026-11-10T08:22:50Z", "donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl", hjd),
     ("GEL-T08", "2026-11-10T14:57:57Z", "registres/go.md", sha((W / "registres/go.md").read_bytes())),
     ("CODE-T07", "2026-11-13T23:42:46Z", "registres/code-t07/CODE-T07-jouet.json", hcode),
     ("SCELLEMENT-T07", "2026-11-11T07:11:42Z", "prereg/T0.7-sondes-v0-v1.md", sha((W / "prereg/T0.7-sondes-v0-v1.md").read_bytes())),
     ("CONSIGNE-AUDIT-FUITES-T07", "2026-11-11T14:08:06Z", "prereg/T0.7-consigne-audit-fuites-v1.md", hc),
     ("SCELLEMENT-P3BIS", "2026-11-11T15:52:30Z", "prereg/P3-bis-temoin-positif-v1.md", hp),
     ("RUN-CONFIRMATION-T06", "2026-11-13T18:52:43Z", f"runs/{R6}/manifeste.json", h6),
     ("GO-LECTURE-T07", "2026-11-13T18:52:44Z", "registres/go-extraits/GO-LECTURE-T07-v1.md", hg),
     ("SCORES-T07", "2026-11-14T01:55:05Z", f"donnees/{R7}/scores-actions-t07.npz", v["H_SCORES"]),
     ("SONDES-T07", "2026-11-14T01:55:05Z", f"diag/{R7}/sondes-t07.json", v["H_SONDES"]),
     ("VERDICT-P3BIS", "2026-11-14T10:30:38Z", "docs/verdicts/verdict-P3-bis-v1-issue.json", hi),
     ("AUDIT-FUITES-T07", "2026-11-14T12:00:00Z", f"diag/{R7}/audit-fuites-t07.json", ha),
     ("CODE-MOTS-ET-COUT-T06", "2026-11-14T12:01:00Z", "docs/notes/jouet/code-mots-et-cout.json", hcm),
     ("LECTURE-T08-BASE-A", "2026-11-14T12:02:00Z", f"diag/{RMC}/base-a-t08.json", hba),
     ("ISSUE-MOTS-ET-COUT-T06", "2026-11-14T12:02:01Z", f"diag/{RMC}/issue-mots-et-cout-t06.json", him)]
(W / "registres/scellements-v1.md").write_text("# Registre jouet\n\n" + "".join(f"| {k} | {dd} | {c} | {h} |\n" for k, dd, c, h in L), encoding="utf-8")
shutil.copy(D / "registres/scellements-v1.md.ouvertures.md", W / "registres/scellements-v1.md.ouvertures.md")
(W / "registres/ouvertures-p3bis-v1.md").write_text("| clé | date | mode | appui | paquets | motif |\n|---|---|---|---|---|---|\n"
    f"| OUVERTURE-P3BIS | 2026-11-14T10:15:23Z | pleine | SCORES-T07={v['H_SCORES']} SONDES-T07={v['H_SONDES']} | {'0' * 64} {'1' * 64} | - |\n", encoding="utf-8")
(W / "registres/decisions.md").write_text("# Registre des décisions jouet\n\n| R-9001 | 2026-11-14 | BA-L2 : ne s'applique pas (bloc M, répétition jouet) | décision |\n"
    "| R-9002 | 2026-11-14 | BA-L2 : ne s'applique pas ; plan de l'étape B bis à sceller (artefact : ligne mêlée) | décision |\n"
    "| R-9003 | 2026-11-14 | état d'une base (artefact : ligne qui ne nomme pas la ligne de la base) | décision |\n", encoding="utf-8")
hb = poser("prereg/T0.7-etape-b-bis-v1.md", "plan jouet\n")
(W / "registres/etape-b-bis-v1.md").write_text(f"# Registre propre jouet\n\n| SCELLEMENT-PLAN-BBIS | 2026-11-14T12:03:00Z | prereg/T0.7-etape-b-bis-v1.md | {hb} |\n", encoding="utf-8")
cellule = "analyse du verdict A ; étape B bis (conception et verdicts) ; T0.8 ; G0 ; préenregistrement NARCBench (rédaction, contre-lecture, course) ; brouillons des papiers B et C ; code de la pièce « mots et coût »"
liste = ("# Liste « qui a lu quoi » jouet, v3\n\n| n° | session | compte | modèle | a lu | rôle | source | exclu de |\n|---|---|---|---|---|---|---|---|\n"
         "| 1 | session non nommée (compte 3) | compte 3 | non déclaré | rien | lot prévu | jouet | aucune exclusion déclarée |\n"
         f"| 2 | session_01JOUETcompte3HOTE000000 (hôte du verdict A) | compte 3 | modèle A | rien ouvert | hôte de la phase A | P3A-004 | {cellule} |\n")
hl = poser("registres/qui-a-lu-quoi-v3.md", liste)
hlx = poser("registres/qui-a-lu-quoi-v3-artefact.md", liste.replace(" ; brouillons des papiers B et C", ""))   # cellule de l'hôte autre
hcx = poser("docs/procedures/jouet/consigne-bbis-jouet-v1.md", "# consigne jouet au nom interdit (artefact)\n")
# -f : le dépôt réel suit ses jeux de données sous donnees/ malgré .gitignore (R-352) ; sans lui, le jeu scellé manquerait au main jouet
git("add", "-A", "-f"); git("commit", "-q", "-m", "main jouet"); subprocess.run(["git", "-C", str(W), "push", "-q", str(T / "distant/lciric/controle-ia-travail.git"), "main"], check=True, capture_output=True)
v.update({"C7J": C7J, "HL": hl, "HCB": hcb, "HLX": hlx, "HCX": hcx})
(T / "valeurs.sh").write_text("".join(f"{k}={x}\n" for k, x in v.items()), encoding="utf-8")
print("dépôt distant jouet construit")
FIN
. "$T/valeurs.sh"; MAIN0=$(git -C "$DIST" rev-parse main)
OK=0; KO=0
joue() {   # $1 nom ; $2 bloc ; $3 code attendu ; $4 motif attendu ; dépôt de la session : $DEP
    local s c; s=$(cd "$DEP" && bash "$2" 2>&1); c=$?
    printf '%s\n' "$s" > "$T/sortie-$PASSE-$(basename "$2" .sh)-$((OK + KO)).txt"
    if [ "$c" = "$3" ] && printf '%s' "$s" | grep -qF -- "$4"; then OK=$((OK + 1)); echo "conforme : $1 (code $c)"
    else KO=$((KO + 1)); echo "ÉCART : $1 (code $c, attendu $3 ; motif « $4 »)"; printf '%s\n' "$s" | tail -14 | sed 's/^/    /'; fi; }
preparer_session() {   # $1 passe ; $2 branche B
    PASSE="$1"; DEP="$T/depot-$1"; git clone -q "$DIST" "$DEP"; ln -s "$DEPOT_REEL/.venv" "$DEP/.venv"
    git -C "$DEP" config user.name jouet; git -C "$DEP" config user.email jouet@exemple.invalid
    export HOME="$T/home-$1" CLAUDE_CODE_REMOTE_SESSION_ID=cse_01JOUETcompte3HOTE000000; mkdir -p "$HOME"
    VAR="$HOME/bac-etape-b-compte-3-v2/variables-v2.sh"
    sed -e "s#<<LISTE>>#registres/qui-a-lu-quoi-v3.md#" -e "s#<<EMPREINTE_LISTE>>#$HL#" -e "s#<<CONSIGNE_LECTEUR_B>>#docs/procedures/jouet/consigne-lecteur-etape-b-jouet-v1.md#" \
        -e "s#<<EMPREINTE_CONSIGNE_LECTEUR_B>>#$HCB#" -e "s#<<REGISTRE_BBIS>>#registres/etape-b-bis-v1.md#" -e "s#<<CLE_PLAN_BBIS>>#SCELLEMENT-PLAN-BBIS#" \
        -e "s#<<R_BA_L2>>#R-9001#" -e "s#<<BRANCHE_PIECE>>#$BRP#" "$B/b01.sh" > "$B/b01-rempli-$1.sh"
    joue "[$1] bloc 0b-C (main à jour)" "$B/b00.sh" 0 "commande-compte-3-phase-c-v4.md"
    joue "[$1] bloc 1C (variables)" "$B/b01-rempli-$1.sh" 0 "session : session_01JOUETcompte3HOTE000000"
    printf '%s\n' "DEPOT_URL='file://$DIST'; TETE_7B=$TETE_7B; TETE_EA=$TETE_EA; C7=$C7J; H_SCORES=$H_SCORES; H_SONDES=$H_SONDES" \
        "MODULE_ETAPE_B=etape_b_jouet_v1; PYTHONPATH_SUP='$T/stub'; BR_B=$2" >> "$VAR"; }
attendre() { local i; for i in $(seq 1 60); do s=$(cd "$DEP" && bash "$B/b09.sh" 2>&1); printf '%s' "$s" | grep -q "ÉTAPE B FINIE" && { echo "$s"; return 0; }; python3 -c 'import time; time.sleep(2)'; done; echo "$s"; return 1; }
# ===== passe 1 : code 0, appel interrompu, poussée refusée puis reprise
preparer_session p1 verdict/t07-etape-b-compte-3-v1
joue "[p1] bloc 2C (attestation v3 : ligne de l'hôte admise)" "$B/b02.sh" 0 "lignes de l'hôte admises : 1"
joue "[p1] bloc C0 (conditions de la mère)" "$B/b03.sh" 0 "plan de B bis : ligne présente"
joue "[p1] bloc C1a (interpréteur, versions)" "$B/b04.sh" 0 "versions : 2.4.6 1.17.1 2.14.1"
joue "[p1] bloc C1 (branche, code détaché, poussée éprouvée)" "$B/b05.sh" 0 "(C7, propre)"
joue "[p1] bloc C2 (placement, morceaux, fichier « mots et coût » pris sur la branche de la phase B)" "$B/b06.sh" 0 "données placées (non suivies, jamais commitées)"
joue "[p1] bloc C2 relancé (fichiers déjà là, égaux)" "$B/b06.sh" 0 "scores déjà recomposés"
joue "[p1] bloc C3 (contrôle à blanc complet, garde du module sur une copie)" "$B/b07.sh" 0 "AUTORISÉE"
export JOUET_DUREE=6
joue "[p1] bloc C4a (appel unique, détaché)" "$B/b08.sh" 0 "étape B lancée, détachée"
joue "[p1] bloc C4-attente aussitôt (outil rendu : processus en cours)" "$B/b09.sh" 0 "étape B en cours depuis"
joue "[p1] artefact : C4a relancé → arrêt, aucun second appel" "$B/b08.sh" 1 "l'étape B a déjà été lancée"
s=$(attendre); printf '%s' "$s" | grep -q "ÉTAPE B FINIE : code 0" && { OK=$((OK + 1)); echo "conforme : [p1] C4-attente : $(printf '%s' "$s" | grep -o 'ÉTAPE B FINIE[^;]*')"; } || { KO=$((KO + 1)); echo "ÉCART : [p1] attente : $s"; }
unset JOUET_DUREE
printf '#!/bin/sh\necho "refus jouet de la répétition" >&2\nexit 1\n' > "$DIST/hooks/pre-receive"; chmod +x "$DIST/hooks/pre-receive"
joue "[p1] artefact : poussée refusée → C4b s'arrête après ses commits" "$B/b10.sh" 1 "poussée (relance C4b"
rm -f "$DIST/hooks/pre-receive"
joue "[p1] bloc C4b relancé seul (reprise à la poussée)" "$B/b10.sh" 0 "diag/$R7/lecture-t07.json :"
printf '%s\n' "CONSIGNE_B=docs/procedures/jouet/consigne-bbis-jouet-v1.md; EMPREINTE_CONSIGNE_B=$HCX" >> "$VAR"
joue "[p1] artefact : pièce au nom interdit → C5 arrête, aucun bordereau" "$B/b11.sh" 1 "nom(s) interdit(s) parmi les pièces"
printf '%s\n' "CONSIGNE_B=docs/procedures/jouet/consigne-lecteur-etape-b-jouet-v1.md; EMPREINTE_CONSIGNE_B=$HCB" >> "$VAR"
printf '| NOTE-JOUET | 2026-11-14T12:04:00Z | prereg/T0.7-etape-b-bis-v1.md | %064d |\n' 0 >> "$DEP/registres/scellements-v1.md"
joue "[p1] artefact : contenu de l'étape B bis dans l'extrait → C5 arrête, aucun bordereau" "$B/b11.sh" 1 "contenu de l'étape B bis dans l'extrait"
git -C "$DEP" checkout -q -- registres/scellements-v1.md
joue "[p1] bloc C5 relancé (pièces refaites de zéro, filtres de noms et de contenu)" "$B/b11.sh" 0 "aucun nom ni contenu de l'étape B bis"
. "$VAR"; [ "$(wc -l < "$ESPACE_B/bordereau-remise-v2.txt")" = 29 ] && ! grep -q -i bbis "$ESPACE_B/bordereau-remise-v2.txt" \
    && { OK=$((OK + 1)); echo "conforme : bordereau de 29 fichiers, sans la pièce de l'artefact"; } || { KO=$((KO + 1)); echo "ÉCART : bordereau"; }
[ "$(cut -c67- "$ESPACE_B/bordereau-remise-v2.txt" | grep -c -x -F "./diag/$R7/sondes-t07.json")" = 1 ] && [ "$(cut -c67- "$ESPACE_B/bordereau-remise-v2.txt" | grep -c -x -F "./diag/$R7/sondes-t07.json.sha256")" = 1 ] \
    && [ "$(grep -F "  ./diag/$R7/sondes-t07.json" "$ESPACE_B/bordereau-remise-v2.txt" | head -n 1 | cut -c1-64)" = "$H_SONDES" ] \
    && { OK=$((OK + 1)); echo "conforme : sondes-t07.json (égal à la ligne SONDES-T07 jouet) et son compagnon figurent au bordereau"; } || { KO=$((KO + 1)); echo "ÉCART : sondes-t07.json ou son compagnon absent du bordereau"; }
joue "[p1] bloc C6 (message de remise)" "$B/b12.sh" 0 "message écrit, aucun marqueur restant"
. "$VAR"; V="$ESPACE_B/verdict-ferme"; printf '# verdict jouet B\n' > "$V/verdict-T0.7-etape-B-v1.md"; printf '{"jouet": true}\n' > "$V/verdict-T0.7-etape-B-v1-issue.json"
printf 'message autre\n' > "$V/verdict-T0.7-etape-B-v1-message-recu-v1.txt"
joue "[p1] artefact : message reçu différent → C7 arrête, rien n'est commité" "$B/b13.sh" 1 "message reçu différent"
cp "$BAC/message-remise-b-v2.txt" "$V/verdict-T0.7-etape-B-v1-message-recu-v1.txt"; printf 'x\n' > "$V/verdict-T0.7-etape-B-v1-fichiers-de-travail.tar"
joue "[p1] artefact : archive dans verdict-ferme → C7 arrête, rien n'est copié" "$B/b13.sh" 1 "de nom inattendu"
rm -f "$V/verdict-T0.7-etape-B-v1-fichiers-de-travail.tar"
joue "[p1] bloc C7 (message attesté, verdict commité, poussé)" "$B/b13.sh" 0 "commit du verdict B :"
python3 -I - "$B/b14.sh" "$B/b14-rempli.sh" <<'FIN'
import sys
t = open(sys.argv[1], encoding="utf-8").read()
t = t.replace("<rapport final du lecteur B, tel quel, à la place de cette ligne>", "STATUT : fichier-d-issue-ecrit\nISSUE : L-jouet (ne doit pas entrer au journal)\nMESSAGE REÇU : jouet")
t = t.replace("CROCHET='<bloquée | passée>'", "CROCHET='bloquée'").replace("session hôte : <modèle A | modèle C>", "session hôte : modèle A")
open(sys.argv[2], "w", encoding="utf-8").write(t)
FIN
printf '#!/bin/sh\necho "refus jouet de la répétition" >&2\nexit 1\n' > "$DIST/hooks/pre-receive"; chmod +x "$DIST/hooks/pre-receive"
joue "[p1] artefact : poussée refusée → F-C s'arrête après son commit" "$B/b14-rempli.sh" 1 "poussée (relance F-C"
rm -f "$DIST/hooks/pre-receive"
joue "[p1] bloc F-C relancé seul (reprise à la poussée, journal provisoire, nettoyage)" "$B/b14-rempli.sh" 0 "dépôt propre"
BRB=verdict/t07-etape-b-compte-3-v1
echo "commits de $BRB au-dessus de main :"; git -C "$DIST" log --format='  %s' "main..$BRB"
c=$(git -C "$DIST" rev-list --count "main..$BRB"); fj=$(git -C "$DIST" show --name-only --format= "$BRB~3"); fs=$(git -C "$DIST" show --name-only --format= "$BRB~2" | sort | tr '\n' ' ')
[ "$c" = 4 ] && [ "$fj" = "registres/scellements-v1.md.ouvertures.md" ] && [ "$fs" = "diag/$R7/lecture-t07.json diag/$R7/lecture-t07.json.sha256 " ] \
    && { OK=$((OK + 1)); echo "conforme : quatre commits ; le premier ne porte que le journal, le second que la sortie scellée du module"; } || { KO=$((KO + 1)); echo "ÉCART : commits ($c ; « $fj » ; « $fs »)"; }
nl=$(git -C "$DIST" diff "main" "$BRB~3" -- registres/scellements-v1.md.ouvertures.md | grep -c '^+| ')
git -C "$DIST" diff "main" "$BRB~3" -- registres/scellements-v1.md.ouvertures.md | grep -q '^+| OUVERTURE-T07 | .* | etape-B/' && [ "$nl" = 2 ] \
    && { OK=$((OK + 1)); echo "conforme : deux lignes neuves au journal, dont l'ouverture de l'étape B écrite par la vraie garde"; } || { KO=$((KO + 1)); echo "ÉCART : journal ($nl lignes)"; }
[ "$(git -C "$DIST" diff --name-only main "$BRB" | grep -c -E '^(diag/'$R6'|runs/|donnees/)')" = 0 ] && { OK=$((OK + 1)); echo "conforme : aucune donnée de 7b ni de l'étape A commitée"; } || { KO=$((KO + 1)); echo "ÉCART : données commitées"; }
J=$(git -C "$DIST" diff --name-only main "$BRB" | grep '^registres-provisoires/.*\.md$'); git -C "$DIST" show "$BRB:$J" | grep -q 'ISSUE' && { KO=$((KO + 1)); echo "ÉCART : ISSUE au journal provisoire"; } || { OK=$((OK + 1)); echo "conforme : aucune ligne ISSUE au journal provisoire"; }
[ ! -e "$DEP/donnees/$R7/scores-actions-t07.npz" ] && [ ! -e "$DEP/diag/$R6/episodes-t06.json" ] && [ ! -e "$BAC/code-c7-v2" ] && { OK=$((OK + 1)); echo "conforme : données placées et arborescence C7 retirées"; } || { KO=$((KO + 1)); echo "ÉCART : nettoyage"; }
printf 'souillure jouet\n' >> "$DEP/requirements-cpu.txt"
joue "[p1] artefact : fichier suivi modifié → F-C relancé s'arrête au contrôle final (aucun second commit)" "$B/b14-rempli.sh" 1 "dépôt non propre"
git -C "$DEP" checkout -q -- requirements-cpu.txt
[ "$(git -C "$DIST" rev-list --count "main..$BRB")" = 4 ] && { OK=$((OK + 1)); echo "conforme : toujours quatre commits après les relances de F-C"; } || { KO=$((KO + 1)); echo "ÉCART : commits après relances de F-C"; }
# ===== passe 2 : code 2 (refus journalisé), sans sortie du module
preparer_session p2 verdict/t07-etape-b-compte-3-jouet-code2
printf '%s\n' "LISTE=registres/qui-a-lu-quoi-v3-artefact.md; EMPREINTE_LISTE=$HLX" >> "$VAR"
joue "[p2] artefact : cellule d'exclusions de l'hôte autre que CELLULE_HOTE → 2C arrête" "$B/b02.sh" 1 "attestation non conforme"
printf '%s\n' "LISTE=registres/qui-a-lu-quoi-v3.md; EMPREINTE_LISTE=$HL" >> "$VAR"
for x in "b02:2C:contrôles d'entrée conformes" "b03:C0:plan de B bis : ligne présente" "b04:C1a:versions" "b05:C1:(C7, propre)" "b06:C2:données placées" "b07:C3:TOUT CONFORME"; do
    joue "[p2] bloc ${x#*:}" "$B/${x%%:*}.sh" 0 "${x##*:}"; done
for x in "R-9002:mêle l'étape B bis" "R-9003:ne nomme pas BA-L2" "R-9999:absente"; do
    printf '%s\n' "R_BA_L2=${x%%:*}" >> "$VAR"; joue "[p2] artefact : décision ${x%%:*} → C0 arrête (${x#*:})" "$B/b03.sh" 1 "${x#*:}"; done
printf '%s\n' "R_BA_L2=R-9001" >> "$VAR"
export JOUET_CODE=2; joue "[p2] bloc C4a (appel jouet en refus)" "$B/b08.sh" 0 "étape B lancée, détachée"; s=$(attendre)
printf '%s' "$s" | grep -q "ÉTAPE B FINIE : code 2" && { OK=$((OK + 1)); echo "conforme : [p2] C4-attente : code 2"; } || { KO=$((KO + 1)); echo "ÉCART : [p2] $s"; }; unset JOUET_CODE
joue "[p2] bloc C4b (ligne de refus affichée, commitée, poussée ; aucune sortie)" "$B/b10.sh" 0 "| REFUS-T07 |"
joue "[p2] bloc C5 refuse sans lecture (code 2)" "$B/b11.sh" 1 "étape B sans lecture : aucun lecteur"
B2=verdict/t07-etape-b-compte-3-jouet-code2
[ "$(git -C "$DIST" rev-list --count "main..$B2")" = 1 ] && [ "$(git -C "$DIST" show --name-only --format= "$B2")" = "registres/scellements-v1.md.ouvertures.md" ] \
    && { OK=$((OK + 1)); echo "conforme : [p2] un seul commit, le journal (ligne REFUS-T07)"; } || { KO=$((KO + 1)); echo "ÉCART : [p2] commits"; }
# ===== bloc M de la mère (état BA-L2 seul)
PASSE=m; DEP="$T/depot-mere"; git clone -q "$DIST" "$DEP"; sed -e "s#BRP='<branche qui porte base-a-t08.json>'#BRP='$BRP'#" -e "s#https://github.com/lciric/controle-ia-travail.git#file://$DIST#" "$B/b15.sh" > "$B/b15-rempli.sh"
s=$(cd "$DEP" && HOME="$T/home-mere" bash "$B/b15-rempli.sh" 2>&1); mkdir -p "$T/home-mere"
printf '%s' "$s" | grep -q "ÉTAT BA-L2 : ne s'applique pas" && ! printf '%s' "$s" | grep -q "0.777" && { OK=$((OK + 1)); echo "conforme : bloc M : « ÉTAT BA-L2 : ne s'applique pas », aucune autre valeur affichée"; } \
    || { KO=$((KO + 1)); echo "ÉCART : bloc M"; printf '%s\n' "$s" | tail -5 | sed 's/^/    /'; }
sed -e "s#BRP='<branche qui porte base-a-t08.json>'#BRP='branche/absente-jouet'#" -e "s#https://github.com/lciric/controle-ia-travail.git#file://$DIST#" "$B/b15.sh" > "$B/b15-artefact-branche.sh"
s=$(cd "$DEP" && HOME="$T/home-mere" bash "$B/b15-artefact-branche.sh" 2>&1); c=$?
[ "$c" = 1 ] && printf '%s' "$s" | grep -q "ARRÊT : dépôt jetable de la pièce" && ! printf '%s' "$s" | grep -q "ÉTAT BA-L2" && { OK=$((OK + 1)); echo "conforme : bloc M, artefact : branche de la pièce absente → arrêt (code 1), aucun état affiché"; } \
    || { KO=$((KO + 1)); echo "ÉCART : bloc M, artefact branche (code $c)"; printf '%s\n' "$s" | tail -5 | sed 's/^/    /'; }
grep -v '^| LECTURE-T08-BASE-A |' "$DEP/registres/scellements-v1.md" > "$T/registre-sans-ba.md"; cp "$T/registre-sans-ba.md" "$DEP/registres/scellements-v1.md"
s=$(cd "$DEP" && HOME="$T/home-mere" bash "$B/b15-rempli.sh" 2>&1); c=$?; git -C "$DEP" checkout -q -- registres/scellements-v1.md
[ "$c" = 1 ] && printf '%s' "$s" | grep -q "ARRÊT : pas exactement une ligne LECTURE-T08-BASE-A" && ! printf '%s' "$s" | grep -q "ÉTAT BA-L2" && { OK=$((OK + 1)); echo "conforme : bloc M, artefact : registre sans ligne LECTURE-T08-BASE-A → arrêt (code 1), aucun état affiché"; } \
    || { KO=$((KO + 1)); echo "ÉCART : bloc M, artefact registre (code $c)"; printf '%s\n' "$s" | tail -5 | sed 's/^/    /'; }
[ "$(git -C "$DIST" rev-parse main)" = "$MAIN0" ] && { OK=$((OK + 1)); echo "conforme : main du dépôt distant inchangé"; } || { KO=$((KO + 1)); echo "ÉCART : main a changé"; }
echo "BILAN : $OK conformes sur $((OK + KO))"; [ "$KO" = 0 ] && echo "RÉPÉTITION DE LA PHASE C : TOUT CONFORME" || echo "RÉPÉTITION DE LA PHASE C : ÉCARTS"
date -u +"fin de la répétition : %Y-%m-%dT%H:%M:%SZ"
