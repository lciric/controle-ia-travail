#!/usr/bin/env bash
# Récupération de P4-instrument (contrôle positif de l'instrument de P3 ; R-262 (1), R-269 ; préenregistrement
# prereg/P4-instrument-v1.md), v1, puis destruction de l'instance par son identifiant (R10) après la récupération
# vérifiée (texte, Chaîne de lancement : « destruction de l'instance par son identifiant après la récupération vérifiée
# (rien n'y reste d'utile) » ; Plan d'analyse, point 7 : disque de l'instance arrêtée 24 heures au plus). Déclinée de
# docs/procedures/P3-premier-test-v2/recuperation_p3_v1.sh sous un nom neuf (R12).
# Clone propre du dépôt de travail ; rien n'est fusionné ni poussé ici. Aucune valeur de jeton, aucun texte d'action de
# P3 n'est affiché ; un motif s'affiche borné à 200 caractères.
# Ce qui est contrôlé : 0 ce script égal à sa copie versée à S ; 1 ascendance (S ancêtre) ; ajouts seulement, aux seuls
# chemins permis (manifeste du run ; résultats : identite-p4.json, resume.json ; données : validation-p4.npz,
# scores-p4.npz, jetons-principales-p4.npz, leurs sceaux ; traces p4-*) : aucun fichier de textes ; un seul run
# « …-p4-reel » ; auteurs ; 2 sceaux (verifier-arbre, traces) ; résultats rattachés au manifeste de CE run ; chaque
# tableau vérifié par son sceau compagnon et rattaché à l'empreinte écrite dans le résumé (ou, sur un arrêt, dans sa
# partie « partiel ») ; 3 manifeste et citations (commit = S, préenregistrement et son sceau, configuration de S et son
# empreinte canonique citée, graines du run sous l'entropie citée, mode, décisif, dépôt propre, versions égales à
# celles du run de P3) ; 4 issue (le résumé, toujours écrit, sans motif d'arrêt ou avec), rattachée aux citations ;
# fichiers attendus de P4 selon l'issue, dans les deux sens (ordre d'écriture du module : validation, puis scores et
# scores par jeton, puis identité) ; tableaux : chaque ligne des scores à sa place du plan (bras I, D, H, B, B′ ; tâche ;
# pas), comptes du résumé, scores par jeton rattachés aux actions notées, validation aux effectifs écrits ; chaînes des
# tableaux de 80 caractères au plus ; 4f aucune fenêtre de 48 caractères d'un texte honnête de P3 (textes de 64
# caractères ou plus, fenêtre du milieu ; fenêtres d'un seul caractère répété ignorées) dans un fichier poussé (octets
# des fichiers ajoutés hors tableaux, chaînes JSON décodées des résultats, du manifeste et de run.json, chaînes des
# tableaux), chaînes JSON de 200 caractères au plus (le motif d'un arrêt : 1 000) ; 6 journal (tests au nombre cité,
# poussée initiale, carte, lignes de progression au motif fixe ; ligne de fin seulement avec un résumé complet) ; carte
# et mémoire ; pip freeze ; 7 jetons ; 8 destruction : seulement si aucun contrôle n'est en échec (code 0, ou code 4 des
# traces seules) ; étiquette de l'instance relue égale à « p4-v1 » (sinon refus : un identifiant faux ne détruit rien
# d'autre) ; `vastai destroy instance <identifiant> -y` ; instance relue absente de la liste.
# Les textes de P3 sont lus par programme pour former les fenêtres (lignes de la condition honnête seulement, comme le
# run de P4 ; les autres lignes sont écartées à la lecture), jamais affichés : seuls des comptes s'écrivent.
# Branche sans run (arrêt avant le run) : contrôles des traces seules, sortie au code 4 (jamais 0). Aucun relancement.
# Codes : 0 tout conforme, instance détruite ; 4 traces seules conformes, instance détruite ; 1 au moins un contrôle en
# échec (destruction comprise), instance gardée : nœud de Lazar ; 2 usage ou clonage impossible.
# Usage : recuperation_p4_v1.sh S IDENTIFIANT DOSSIER_NEUF
set -uo pipefail
SOI=$(realpath "$0")
[ $# -eq 3 ] || { echo "usage : recuperation_p4_v1.sh S IDENTIFIANT DOSSIER_NEUF (aucun relancement)"; exit 2; }
S=$1; ID=$2; D=$(realpath -m "$3")
TRAV="$D.travail"                # fichiers de travail dans un dossier neuf, jamais dans le parent partagé
PY=/tmp/claude-0/-home-user/5a6b9d1d-b17d-59a1-a770-8737a831fe0a/scratchpad/scellement-revalidation/venv-gpu-neuf/bin/python
DISTANT=/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/relecture-chaine-donnees/jouet-b/distant.git
P=prereg/P4-instrument-v1.md
CFG=prereg/P4-instrument-config-v1.json
VERSEES=docs/procedures/P4-instrument-v1
BRANCHE=calcul/p4-jouet-h-v1
ETIQUETTE=p4-v1
RUN_P3=20261019-230011-p3-reel   # run source : versions de référence (mêmes dépendances installées)
TEXTES_P3=donnees/synth/textes-fenetres-p3.jsonl   # textes honnêtes de P3 : fenêtres (4f), jamais affichés
CARTE_EXIGEE=non                 # A100 SXM4 d'au moins 75 Gio ; la répétition jouet passe « non », sauf ses cas des gardes réelles
VERSIONS_EXIGEES=non             # versions du run égales à celles du run de P3 ; idem
COPIE_EXIGEE=non                 # ce script égal à sa copie versée à S ; idem
MODE_ATTENDU=jouet
LONGUEUR_MAX=200                 # chaîne la plus longue admise dans un résultat (motif d'un arrêt : 1 000)
MOTIF_RUN='^[0-9]{8}-[0-9]{6}-p4-jouet$'
MOTIF_PROGRES='^PROGRES [0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z( [a-z_]+=[^ ]+)+$'
[[ "$S" =~ ^[0-9a-f]{40}$ ]] || { echo "S invalide"; exit 2; }
[[ "$ID" =~ ^[0-9]{6,10}$ ]] || { echo "identifiant d'instance invalide (6 à 10 chiffres)"; exit 2; }
[ -e "$D" ] && { echo "$D existe déjà (R12)"; exit 2; }
[ -e "$TRAV" ] && { echo "$TRAV existe déjà (R12)"; exit 2; }
mkdir -p "$TRAV" || exit 2
export PYTHONDONTWRITEBYTECODE=1
echecs=0
ok() { echo "OK  $*"; }
ko() { echo "KO  $*"; echecs=$((echecs + 1)); }
git clone -q "$DISTANT" "$D" || { echo "clonage impossible"; exit 2; }
cd "$D"
git fetch -q origin "$BRANCHE" || { echo "branche $BRANCHE introuvable"; exit 2; }
H=$(git rev-parse FETCH_HEAD); echo "tête de la branche : $H"
git checkout -q --detach "$H"
if [ "$COPIE_EXIGEE" = oui ]; then
    [ "$(git show "$S:$VERSEES/recuperation_p4_v1.sh" 2>/dev/null | sha256sum | cut -d' ' -f1)" = "$(sha256sum "$SOI" | cut -d' ' -f1)" ] \
        && ok "0 récupération exécutée = copie versée à S" || ko "0 récupération exécutée ≠ copie versée à S"
fi
# 1. ascendance et contenu : ajouts seulement, aux chemins permis (aucun fichier de textes)
git merge-base --is-ancestor "$S" "$H" && ok "1a S est ancêtre de la branche" || ko "1a S n'est pas ancêtre de la branche"
git diff --name-status --no-renames "$S" "$H" > "$TRAV/diff-status.txt"
NON_AJOUTS=$(grep -vc '^A' "$TRAV/diff-status.txt" || true)
[ "$NON_AJOUTS" = 0 ] && ok "1b seulement des ajouts ($(wc -l < "$TRAV/diff-status.txt") fichiers)" || ko "1b $NON_AJOUTS changement(s) autre(s) qu'un ajout"
cut -f2 "$TRAV/diff-status.txt" > "$TRAV/chemins.txt"
PERMIS='^(runs/[^/]+/manifeste\.json(\.sha256)?|diag/[^/]+/(identite-p4|resume)\.json(\.sha256)?|donnees/[^/]+/(validation-p4|scores-p4|jetons-principales-p4)\.npz(\.sha256)?|traces/p4-[^/]+/(journal\.txt|tests\.txt|tests\.err|run\.json|run\.err|nvidia-smi\.txt|pip-freeze\.txt|empreintes\.sha256))$'
HORS=$(grep -vE "$PERMIS" "$TRAV/chemins.txt" | head -5 | tr '\n' ' ' | cut -c1-200 || true)
[ -z "$HORS" ] && ok "1c ajouts aux seuls chemins permis (manifeste, résultats et tableaux du run, traces p4-* ; aucun texte)" \
    || ko "1c chemins hors périmètre : $HORS"
RUNS=$(grep -E '^(runs|diag|donnees)/' "$TRAV/chemins.txt" | cut -d/ -f2 | sort -u)
NRUNS=$(printf '%s\n' "$RUNS" | grep -c . || true)
RUN=$(printf '%s\n' "$RUNS" | head -1)
SANS_RUN=non
if [ "$NRUNS" = 1 ] && [[ "$RUN" =~ $MOTIF_RUN ]] && [ -f "runs/$RUN/manifeste.json" ]; then ok "1d un seul run : $RUN"
elif [ "$NRUNS" = 0 ]; then SANS_RUN=oui; echo "--  1d aucun run sur la branche : récupération des traces seules (arrêt avant le run)"
else ko "1d runs : $(printf '%s ' $RUNS | cut -c1-160)(un seul, au motif, avec son manifeste, attendu)"; SANS_RUN=illisible; fi
AUTEURS=$(git log --format='%an' "$S..$H" | sort -u)
[ "$AUTEURS" = "instance de calcul (P4)" ] && ok "1e commits de « instance de calcul (P4) » ($(git rev-list --count "$S..$H"))" || ko "1e auteurs : $(printf '%s' "$AUTEURS" | tr '\n' ' ' | cut -c1-120)"
# 2. sceaux
PYTHONPATH=src "$PY" -B -m controle_ia.scellement verifier-arbre . > "$TRAV/verifier-arbre.txt" 2>&1 && ok "2a verifier-arbre : $(tail -1 "$TRAV/verifier-arbre.txt")" || ko "2a verifier-arbre : $(tail -3 "$TRAV/verifier-arbre.txt" | tr '\n' ' ' | cut -c1-200)"
NOUVELLES=$(for d in traces/p4-*/; do [ -d "$d" ] || continue; git cat-file -e "$S:${d%/}" 2>/dev/null || echo "${d%/}"; done)
for d in $NOUVELLES; do
    (cd "$d" && sha256sum -c --quiet empreintes.sha256) > "$TRAV/sc.txt" 2>&1 && ok "2c sha256sum -c $d" || ko "2c $d : $(head -2 "$TRAV/sc.txt" | tr '\n' ' ' | cut -c1-160)"
done
# 2b (rattachements), 3 (manifeste et citations), 4 (issue, pièces, tableaux, textes) ; sans objet sans run. Le
# programme rend le nombre de ses KO (borné à 100), ajouté au compte.
if [ "$SANS_RUN" = non ]; then
PYTHONPATH=src "$PY" -B - "$RUN" "$S" "$P" "$CFG" "$RUN_P3" "$TEXTES_P3" "$MODE_ATTENDU" "$VERSIONS_EXIGEES" "$LONGUEUR_MAX" \
    "$TRAV/diff-status.txt" "$NOUVELLES" "$VERSEES" <<'EOF' || echecs=$((echecs + $?))
import hashlib, importlib.util, json, re, sys
from pathlib import Path
import numpy as np
from controle_ia.environnements.noter_pilote_a import VERSIONS_EGALES
from controle_ia.manifeste import graines, lire_manifeste, verifier_resultat
from controle_ia.scellement import verifier
run, s, p, cfg_p, run_p3, textes_p3, mode_attendu, versions_exigees, longueur_max, diff_status, nouvelles, versees = sys.argv[1:13]
longueur_max = int(longueur_max)
k = 0
def ok(m): print("OK ", m)
def ko(m):
    global k; k += 1; print("KO ", m)
def so(m): print("-- ", m)
texte = Path(p).read_text(encoding="utf-8")
def cite(motif):
    x = re.findall(motif, texte)
    return x[0] if len(x) == 1 else None
cfg_c, ent_c = cite(r"Configuration de P4 \(empreinte canonique\) : `([0-9a-f]{64})`"), cite(r"Entropie : `([0-9]+)`")
code_c = cite(r"Commit du code d'analyse : `([0-9a-f]{40})`")
# module de P4 de S, chargé seulement à l'empreinte de sa ligne « Module de P4 » (constantes du plan et des clés)
chemin_m = f"{versees}/instrument_p4_v1.py"
lm = re.findall(r"^[ \t]*-[ \t]+Module de P4 : `" + re.escape(chemin_m) + r"` : `([0-9a-f]{64})`[ \t]*$", texte, re.M)
ip = None
if len(lm) == 1 and Path(chemin_m).is_file() and hashlib.sha256(Path(chemin_m).read_bytes()).hexdigest() == lm[0]:
    spec = importlib.util.spec_from_file_location("instrument_p4_v1", chemin_m)
    ip = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ip)
else:
    ko("3 module de P4 de S absent, non cité ou d'empreinte autre que sa ligne « Module de P4 »")
d, dd = Path("diag") / run, Path("donnees") / run
try:
    cfg = json.loads(Path(cfg_p).read_text(encoding="utf-8"))
except Exception as e:
    cfg = None; ko(f"3 configuration de S illisible : {str(e)[:120]}")
# 2b. chaque résultat : sceau, rattachement au manifeste de CE run
lus = {}
for f in sorted(d.glob("*.json")):
    try:
        corps = verifier_resultat(".", f)
        assert corps.get("run_id") == run, f"run_id {corps.get('run_id')!r} ≠ {run!r}"
        lus[f.name] = corps["resultat"]
        ok(f"2b résultat {f.name} scellé, rattaché au manifeste du run {run}")
    except Exception as e:
        ko(f"2b résultat {f.name} : {str(e)[:200]}")
resume = lus.get("resume.json")
complet = resume is not None and resume.get("arret") is None
rattache = (resume or {}) if complet else ((resume or {}).get("partiel") or {})
# 2b. tableaux : sceau compagnon, empreinte écrite au résumé (ou dans sa partie « partiel » sur un arrêt) ; identité de même
DONNEES = (("validation-p4.npz", "validation_sha256"), ("scores-p4.npz", "scores_sha256"),
           ("jetons-principales-p4.npz", "jetons_principales_sha256"))
for nom, cle in DONNEES:
    f = dd / nom
    if not f.exists():
        continue
    try:
        e = verifier(f)
    except Exception as x:
        ko(f"2b {nom} : sceau compagnon non conforme ({str(x)[:120]})"); continue
    if resume is None:
        so(f"2b {nom} scellé ; rattachement sans objet (résumé absent ou non vérifié : 4a)")
    else:
        (ok if rattache.get(cle) == e else ko)(f"2b {nom} scellé, rattaché au résumé ({str(rattache.get(cle))[:12]}…)")
if "identite-p4.json" in lus and resume is not None:
    e = hashlib.sha256((d / "identite-p4.json").read_bytes()).hexdigest()
    (ok if rattache.get("identite_sha256") == e else ko)(f"2b identite-p4.json rattaché au résumé ({e[:12]}…)")
# 3. manifeste et citations
m = None
try:
    m, _ = lire_manifeste(f"runs/{run}/manifeste.json")
except Exception as e:
    ko(f"3 manifeste illisible : {str(e)[:200]}")
if m is not None:
    (ok if m["commit"] == s else ko)(f"3a commit du manifeste {m['commit'][:12]}… = S")
    pr = m.get("preenregistrement") or {}
    sha_p = Path(p + ".sha256").read_text(encoding="utf-8").split()[0]
    (ok if pr.get("chemin") == p and pr.get("sha256") == sha_p else ko)(f"3b préenregistrement {pr.get('chemin')} {str(pr.get('sha256'))[:12]}…")
    e_cfg = hashlib.sha256(__import__("controle_ia.manifeste", fromlist=["config_canonique"]).config_canonique(m["config"])).hexdigest()
    (ok if cfg_c and e_cfg == cfg_c and m["config"] == cfg else ko)(f"3c configuration du manifeste = configuration de S, empreinte citée ({str(cfg_c)[:12]}…)")
    attendues = graines(list(ip.CLES_RUN), int(ent_c)) if (ent_c and ip is not None) else None
    (ok if attendues is not None and m["graines"] == attendues else ko)(f"3d graines du run sous l'entropie citée ({len(m['graines'])} graine(s))")
    (ok if m["config"].get("mode") == mode_attendu and m.get("decisif") is True and m.get("depot_propre") is True else ko)(
        f"3e mode {m['config'].get('mode')}, décisif {m.get('decisif')}, dépôt propre {m.get('depot_propre')}")
    if versions_exigees == "oui":
        try:
            mp, _ = lire_manifeste(f"runs/{run_p3}/manifeste.json")
            v, vp = m.get("versions") or {}, mp.get("versions") or {}
            ecarts = [b for b in VERSIONS_EGALES if v.get(b) != vp.get(b)]
            (ok if not ecarts and v.get("torch") else ko)(f"3f versions égales à celles du run de P3 ({run_p3}) : torch {v.get('torch')}, transformers {v.get('transformers')} ; écarts {ecarts}")
        except Exception as e:
            ko(f"3f manifeste du run de P3 illisible : {str(e)[:120]}")
    else:
        so("3f versions non comparées à celles du run de P3 (répétition sur processeur)")
# 4. issue : le résumé, toujours écrit (sans motif d'arrêt, ou avec) ; aucun autre fichier d'issue
(ok if resume is not None and not (d / "arret.json").exists() else ko)(f"4a issue : résumé {'présent' if resume is not None else 'absent'}, {'complet' if complet else 'avec motif d arrêt'}")
if resume is not None and not complet:
    print("    arrêt :", json.dumps({x: (resume.get("arret") or {}).get(x) for x in ("etape", "motif")}, ensure_ascii=False)[:200])
if resume is not None:
    (ok if rattache.get("commit_cite") == code_c and rattache.get("config_sha256") == cfg_c else ko)(
        "4b issue rattachée aux citations (commit du code, configuration)")
# 4c. fichiers attendus de P4 selon l'issue, dans les deux sens (ordre d'écriture : validation ; scores et scores par
# jeton ; identité) ; un tableau sans son sceau, ou un sceau sans son tableau, est orphelin
ordre = [["validation-p4.npz"], ["scores-p4.npz", "jetons-principales-p4.npz"], ["identite-p4.json"]]
def present(n):
    return (d / n).exists() if n.endswith(".json") else (dd / n).exists()
etapes = [all(present(n) for n in g) for g in ordre]
partielles = [any(present(n) for n in g) and not all(present(n) for n in g) for g in ordre]
prefixe = all(etapes[i] or not any(etapes[i + 1:]) for i in range(len(etapes)))
orphelins = [n for n, _ in DONNEES if (dd / n).exists() != (dd / (n + ".sha256")).exists()]
autres = sorted(x.name for x in d.glob("*.json") if x.name not in ("resume.json", "identite-p4.json"))
conforme = (resume is not None and not any(partielles) and prefixe and not orphelins and not autres
            and (all(etapes) if complet else True))
(ok if conforme else ko)(f"4c fichiers attendus selon l'issue : étapes écrites {etapes}, incomplètes {partielles}, "
                         f"dans l'ordre {prefixe}, orphelins {orphelins}, résultats en trop {autres}, complet {complet}")
# 4d. tableaux : forme, place de chaque ligne au plan, comptes du résumé ; chaînes de 80 caractères au plus
def chaines_courtes(z, cles):
    return all(z[c].dtype.kind == "U" and max((len(x) for x in z[c].tolist()), default=0) <= 80 for c in cles)
taches = None
try:
    from controle_ia.environnements.pilote_a import charger_taches
    taches = [t["identifiant"] for t in charger_taches(cfg["empreintes_sources"]["taches"]["chemin"])]
except Exception as e:
    ko(f"4d tâches de la configuration illisibles : {str(e)[:120]}")
notees = None
if (dd / "scores-p4.npz").exists() and cfg is not None and taches is not None and ip is not None:
    with np.load(dd / "scores-p4.npz", allow_pickle=False) as z:
        cles = set(z.files)
        attendues_cles = {"noms_sondes", "scores", "bras", "episode", "tache", "pas", "jetons", "jetons_notes"}
        chaines = ("noms_sondes", "bras", "episode", "tache")
        forme = cles == attendues_cles and chaines_courtes(z, chaines) and all(z[c].dtype.kind in "fiub" for c in cles - set(chaines))
        T = int(cfg["T"])
        plan = [(b, f"honnete/{t}/e0" if b == "I" else f"{b}/{t}/e0", t, q) for b in ip.BRAS for t in taches for q in range(T)]
        lignes = list(zip(z["bras"].tolist(), z["episode"].tolist(), z["tache"].tolist(), [int(x) for x in z["pas"].tolist()])) if forme else None
        n = len(z["bras"]) if "bras" in cles else -1
        conforme = forme and lignes == plan and z["scores"].shape == (n, len(z["noms_sondes"])) and len(z["noms_sondes"]) == cfg["n_sondes_legeres"]
        if forme and z["scores"].ndim == 2:
            notees = np.flatnonzero(np.all(np.isfinite(z["scores"]), axis=1))
            par_bras = {b: int(sum(1 for i in notees if z["bras"][i] == b)) for b in ip.BRAS}
            if complet:
                conforme = conforme and resume.get("actions_par_bras") == len(taches) * T and resume.get("actions_notees") == par_bras
        (ok if conforme else ko)(f"4d scores : {n} actions, {len(ip.BRAS)} bras, chaque ligne à sa place du plan "
                                 f"(bras, épisode, tâche, pas) : {lignes == plan}, tableaux sans texte : {forme}")
elif (dd / "scores-p4.npz").exists():
    so("4d scores : sans objet (configuration, tâches ou module illisibles)")
if (dd / "jetons-principales-p4.npz").exists() and notees is not None:
    with np.load(dd / "jetons-principales-p4.npz", allow_pickle=False) as j:
        cles_j = {"principales", "rang", "longueur", "debut", "scores_0", "scores_1"}
        conforme = set(j.files) == cles_j and chaines_courtes(j, ("principales",))
        if conforme:
            L = int(j["longueur"].sum())
            debut = np.concatenate([[0], np.cumsum(j["longueur"])[:-1]]) if len(j["longueur"]) else np.zeros(0)
            conforme = (j["principales"].tolist() == [cfg["sondes_principales"][c] for c in ip.CONCEPTS]
                        and j["rang"].tolist() == notees.tolist() and np.array_equal(j["debut"], debut)
                        and all(len(j[x]) == L and j[x].dtype.kind == "f" for x in ("scores_0", "scores_1")))
        (ok if conforme else ko)(f"4d scores par jeton des sondes principales : {len(notees)} actions notées")
if (dd / "validation-p4.npz").exists() and cfg is not None:
    with np.load(dd / "validation-p4.npz", allow_pickle=False) as v:
        cles_v = {"noms_sondes", "scores", "concept", "y", "groupe"}
        conforme = set(v.files) == cles_v and chaines_courtes(v, ("noms_sondes", "concept", "groupe"))
        if conforme:
            eff = {c: int((v["concept"] == c).sum()) for c in cfg["effectifs_validation"]}
            conforme = (eff == cfg["effectifs_validation"] and v["scores"].shape == (len(v["concept"]), len(v["noms_sondes"]))
                        and len(v["y"]) == len(v["concept"]))
        (ok if conforme else ko)(f"4d validation : effectifs {cfg['effectifs_validation']}, tableaux sans texte")
# 4f. aucune fenêtre d'un texte honnête de P3 dans un fichier poussé ; chaînes des résultats bornées. Comptes seulement.
textes = []
try:
    for brut in Path(textes_p3).read_text(encoding="utf-8").splitlines():
        x = json.loads(brut)
        if x.get("condition") == "honnete" and isinstance(x.get("texte"), str):
            textes.append(x["texte"])
except Exception as e:
    ko(f"4f textes honnêtes de P3 illisibles ({textes_p3}) : {type(e).__name__}")
fenetres = sorted({t[(len(t) - 48) // 2:(len(t) - 48) // 2 + 48] for t in textes if len(t) >= 64})
ignorees = [x for x in fenetres if len(set(x)) == 1]
fenetres = [x for x in fenetres if len(set(x)) > 1]
longues, trouves_json = {}, {}
def parcourir(x, cle=None, nom=""):
    if isinstance(x, str):
        borne = 1000 if (nom == "resume.json" and cle == "motif") else longueur_max
        if len(x) > borne:
            longues[nom] = max(longues.get(nom, 0), len(x))
        n_x = sum(1 for w in fenetres if w in x)
        if n_x:
            trouves_json[nom] = trouves_json.get(nom, 0) + n_x
    elif isinstance(x, dict):
        for c, v in x.items(): parcourir(v, c, nom)
    elif isinstance(x, list):
        for v in x: parcourir(v, cle, nom)
fichiers_json = [*sorted(d.glob("*.json")), Path(f"runs/{run}/manifeste.json")] + [Path(t) / "run.json" for t in nouvelles.split() if (Path(t) / "run.json").is_file()]
for f in fichiers_json:
    try:
        corps = f.read_text(encoding="utf-8")
        if f.name == "run.json" and not corps.strip():
            continue
        parcourir(json.loads(corps), None, f.name)
    except Exception:
        longues[f"{f} (illisible)"] = -1
ajoutes = [l.split("\t", 1)[1] for l in Path(diff_status).read_text(encoding="utf-8").splitlines() if "\t" in l]
morceaux = [x.encode("utf-8") for x in fenetres]
trouves = {}
for a in ajoutes:
    f = Path(a)
    if not f.is_file():
        continue
    if a.endswith(".npz"):
        try:
            with np.load(f, allow_pickle=False) as z:
                n_f = sum(1 for c in z.files if z[c].dtype.kind == "U" for s_ in z[c].tolist() for w in fenetres if w in s_)
        except Exception:
            n_f = 0
    else:
        b = f.read_bytes()
        n_f = sum(1 for x in morceaux if x in b)
    if n_f:
        trouves[a] = n_f
(ok if not longues and not trouves and not trouves_json and textes else ko)(
    f"4f aucune fenêtre d'un texte honnête de P3 dans un fichier poussé : chaînes au-delà de la borne {longues} ; "
    f"fenêtres retrouvées (nombre par fichier) {trouves} ; dans les chaînes JSON décodées {trouves_json} ; "
    f"{len(fenetres)} fenêtres cherchées dans {len(ajoutes)} fichiers ({len(ignorees)} fenêtre(s) d'un seul caractère répété ignorée(s))")
sys.exit(min(k, 100))
EOF
fi
# 6. journal de l'instance versé dans les traces (dernier dossier nouveau) ; aucun dossier nouveau : KO
[ -n "$NOUVELLES" ] || ko "6a aucune trace versée sur la branche (poussée finale en échec ?) : instance gardée, traces à reprendre"
J=$(printf '%s\n' $NOUVELLES | grep -v '/p4-plafond-' | tail -1)
[ -n "$J" ] || J=$(printf '%s\n' $NOUVELLES | tail -1)
A=$(sed -n "s/.*Tests attendus : \`\([0-9]*\)\`.*/\1/p" "$P" | head -1)
if [ "$SANS_RUN" = oui ]; then
    [ -s "$J/journal.txt" ] && ok "6a journal versé ($J) : $(grep -c . "$J/journal.txt") lignes ; dernière : $(tail -1 "$J/journal.txt" | cut -c1-160)" \
        || ko "6a journal absent ou vide ($J)"
else for motif in "$A tests attendus" "poussée avant l'installation" "disponible False" "tests : $A passed"; do
    grep -qF "$motif" "$J/journal.txt" 2>/dev/null && ok "6a journal ($J) : « $motif »" || ko "6a journal ($J) : « $motif » absent"
done; fi
grep '^PROGRES ' "$J/journal.txt" > "$TRAV/progres.txt" 2>/dev/null || true
NP=$(grep -c . "$TRAV/progres.txt" || true); NPC=$(grep -cE "$MOTIF_PROGRES" "$TRAV/progres.txt" || true)
[ "$NP" = "$NPC" ] && ok "6a lignes de progression au journal : $NP, toutes au motif fixe" || ko "6a lignes de progression : $NP, dont $NPC au motif fixe"
[ "$SANS_RUN" = oui ] && { [ "$NP" = 0 ] && ok "6a aucune ligne de progression sans run" || ko "6a $NP ligne(s) de progression sans run"; }
# 6f. ligne de fin du module seulement avec un résumé complet, après les lignes des bras, au nombre d'actions écrites
if [ "$SANS_RUN" = non ]; then
PYTHONPATH=src "$PY" -B - "$RUN" "$TRAV/progres.txt" <<'EOF' || echecs=$((echecs + $?))
import json, re, sys
from pathlib import Path
run, progres = sys.argv[1:3]
lignes = Path(progres).read_text(encoding="utf-8").splitlines()
try:
    resume = json.loads((Path("diag") / run / "resume.json").read_text(encoding="utf-8"))["resultat"]
except Exception:
    resume = None
complet = resume is not None and resume.get("arret") is None
fin = [i for i, l in enumerate(lignes) if " etape=fin " in l + " "]
bras = [i for i, l in enumerate(lignes) if " etape=bras " in l + " "]
# nombre d'actions écrites, lu au résumé complet (bras × actions par bras), indépendant des tableaux (4c, 4d)
n = len(resume.get("actions_notees") or {}) * int(resume.get("actions_par_bras") or 0) if complet else -1
if complet:
    bonne = len(fin) == 1 and bool(bras) and fin[0] > bras[-1] and f" actions={n} " in lignes[fin[0]] + " "
else:
    bonne = not fin
print(("OK " if bonne else "KO ") + f" 6f ligne de fin : {len(fin)} (résumé complet : {complet} ; lignes des bras : {len(bras)} ; actions {n})")
sys.exit(0 if bonne else 1)
EOF
fi
# 6b. carte et mémoire (nvidia-smi.txt) ; 6c. pip freeze (descriptif) ; fichiers cherchés dans tous les dossiers nouveaux
NS=$(for d in $NOUVELLES; do [ -f "$d/nvidia-smi.txt" ] && echo "$d/nvidia-smi.txt"; done | head -1)
PF=$(for d in $NOUVELLES; do [ -f "$d/pip-freeze.txt" ] && echo "$d/pip-freeze.txt"; done | head -1)
if [ "$SANS_RUN" = oui ]; then
    echo "--  6b et 6c descriptifs sans run : carte « $(sed -n '2p' "${NS:-/dev/null}" 2>/dev/null) » ; pip freeze ${PF:-absent}"
elif [ "$CARTE_EXIGEE" = oui ]; then
    CARTE=$(sed -n '2p' "${NS:-/dev/null}" 2>/dev/null)
    MIB=$(printf '%s\n' "$CARTE" | sed -n 's/.*, *\([0-9][0-9]*\) MiB *$/\1/p')
    if [[ "$CARTE" == *A100* && "$CARTE" == *SXM4* ]] && [ -n "$MIB" ] && [ "$MIB" -ge 76800 ]; then ok "6b carte : $CARTE"
    else ko "6b carte ou mémoire inattendue (A100 SXM4, au moins 75 Gio) : « $(printf '%s' "$CARTE" | cut -c1-80) »"; fi
else echo "--  6b carte non exigée (répétition sur processeur)"; fi
if [ "$SANS_RUN" = oui ]; then :
elif [ -n "$PF" ] && grep -q '^torch==' "$PF" && grep -q '^transformers==' "$PF"; then
    ok "6c pip freeze versé ($PF) : $(grep -c . "$PF") paquets ; $(grep -E '^(torch|transformers)==' "$PF" | tr '\n' ' ')"
elif grep -qF "pip freeze impossible" "$J/journal.txt" 2>/dev/null; then echo "--  6c pip freeze impossible, journalisé (descriptif, sans effet sur le run)"
else ko "6c pip freeze absent des traces, sans échec journalisé"; fi
# 7. aucune valeur de jeton dans le différentiel ni dans les fichiers ajoutés (comptée, jamais affichée)
git diff "$S" "$H" > "$TRAV/diff-complet.txt"
python3 - "$TRAV/diff-complet.txt" "$TRAV/diff-status.txt" <<'EOF' || echecs=$((echecs + $?))
import os, sys
from pathlib import Path
diff = Path(sys.argv[1]).read_bytes()
fichiers = [l.split("\t", 1)[1] for l in Path(sys.argv[2]).read_text().splitlines() if "\t" in l]
k = 0
for nom in ("HF_TOKEN", "CONTROLE_IA_GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY"):
    v = os.environ.get(nom)
    if not v or len(v) < 8:
        print(f"KO  7 {nom} absent de l'environnement de la session : recherche impossible"); k += 1; continue
    b = v.encode()
    n = diff.count(b) + sum(Path(f).read_bytes().count(b) for f in fichiers if Path(f).is_file())
    print(("OK " if n == 0 else "KO ") + f" 7 valeur de {nom} : {n} occurrence(s)")
    k += n > 0
sys.exit(min(k, 100))
EOF
echo "RUN=$RUN"; echo "TETE=$H"
# 8. destruction de l'instance par son identifiant (R10), seulement après une récupération vérifiée (aucun KO) ; jamais
# par motif ; étiquette relue d'abord (refus si elle n'est pas « p4-v1 ») ; puis instance relue absente de la liste.
# Aucune sortie brute de l'outil n'est affichée (elle porte les variables de l'instance, dont les jetons).
DETRUITE=non
if [ "$echecs" = 0 ]; then
    if ! command -v vastai > /dev/null; then
        ko "8 outil de location introuvable sur le PATH : instance $ID gardée, à détruire par son identifiant"
    else
        LU=$(vastai show instance "$ID" --raw 2>/dev/null | python3 -c '
import json, sys
try:
    d = json.load(sys.stdin)
    assert isinstance(d, dict)
except Exception:
    print("illisible"); raise SystemExit
print(" ".join(str(d.get(k)) for k in ("label", "actual_status", "cur_state")))')
        set -- $LU
        if [ "${1:-illisible}" != "$ETIQUETTE" ]; then
            ko "8 instance $ID : étiquette « ${1:-illisible} » (« $ETIQUETTE » attendue) : destruction refusée"
        elif ! vastai destroy instance "$ID" -y > "$TRAV/destruction.txt" 2>&1; then
            ko "8 instance $ID : destruction en échec (vastai destroy instance $ID -y)"
        elif vastai show instances --raw 2>/dev/null | python3 -c '
import json, sys
try:
    l = json.load(sys.stdin)
    assert isinstance(l, list)
except Exception:
    sys.exit(2)
sys.exit(0 if any(str(i.get("id")) == sys.argv[1] for i in l if isinstance(i, dict)) else 1)' "$ID"; then
            ko "8 instance $ID encore listée après la destruction"
        else
            c=$?
            if [ "$c" = 1 ]; then ok "8 instance $ID (étiquette $ETIQUETTE, ${2:-?} ${3:-?}) détruite par son identifiant et absente de la liste"; DETRUITE=oui
            else ko "8 liste des instances illisible après la destruction : instance $ID à relire"; fi
        fi
    fi
fi
if [ "$echecs" != 0 ]; then echo "RÉCUPÉRATION : $echecs CONTRÔLE(S) EN ÉCHEC ; INSTANCE $ID NON DÉTRUITE : NŒUD DE LAZAR"; exit 1
elif [ "$SANS_RUN" = oui ]; then echo "RÉCUPÉRATION DES TRACES SEULES (AUCUN RUN) : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT ($ID)"; exit 4
else echo "RÉCUPÉRATION : TOUS CONFORMES ; INSTANCE DÉTRUITE PAR SON IDENTIFIANT ($ID)"; fi
