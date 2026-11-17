"""Répétition locale de la machine du crible (v) — v1 (fichier neuf, R12) : l'amorce et le programme machine joués sur ce poste,
contre un **dépôt jouet** (`file:///`, branches main et lot), un **loueur simulé** (remplaçant de curl qui journalise les demandes
de destruction), des clés factices (jamais une vraie), les mondes d'essai (secret d'essai public) et le crible « réel » joué à blanc
(relais factices) ; la mère est jouée par ce programme au moyen de l'outil de la session (`session_crible_v_v1.py`), feux et
inscriptions compris. **Aucune machine, aucun appel au loueur ni à aucun fournisseur, aucune dépense.**

Cas : `nominal` (de la mise en place à « fini », feux 1 à 3, inscriptions, essai à blanc à M, crible à blanc, mesure une fois,
lecture remise non ouverte, rapatriement sans monde, balayage : aucune clé factice poussée, états horodatés) ; `phrase-absente`
(arrêt (A) à l'échéance de la barrière 1) ; `feu-arret` (feu d'arrêt pendant `jouer` : lanceur et relais arrêtés par leurs PID,
arrêt (A)) ; `minuterie` (destruction demandée au loueur simulé à l'échéance) ; `branche-presente` (branche de sortie déjà là :
rien n'est poussé) ; `session` (gardes de l'outil de la session : offre, création, commande, ligne, prix, dépense, destruction).

Usage : python3 -I -B repetition_crible_v_v1.py --code DOSSIER --essai DOSSIER_ESSAI --bundle PAQUET --travail DOSSIER_NEUF
        --sortie R.json [--cas nominal,phrase-absente,…] [--files 1|2]
"""
import argparse
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import time

BUNDLE_REL = ("docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/"
              "arbre-organisme-complet-605e0f6.bundle")
CLES_FACTICES = {"GH_TOKEN": "jetonfacticeREPETITION0000000000", "RR_ANTHROPIC_API_KEY_RIGAUD": "cleAfacticeREPETITION000000",
                 "GEMINI_API_KEY": "cleGfacticeREPETITION000000", "OPENAI_API_KEY": "cleOfacticeREPETITION000000"}
RESULTATS = []


def sh(*a, cwd=None, env=None, entree=None, ok=True):
    r = subprocess.run(list(a), cwd=cwd, env=env, capture_output=True, text=True, input=entree)
    if ok and r.returncode != 0:
        raise RuntimeError(f"{' '.join(a)[:200]} : code {r.returncode} : {r.stderr[-400:]}")
    return r


def noter(cas, nom, ok, detail):
    RESULTATS.append({"cas": cas, "nom": nom, "ok": bool(ok), "detail": str(detail)[:400]})
    print(f"{'OK ' if ok else 'ECHEC'} [{cas}] {nom} : {str(detail)[:160]}", flush=True)


def git_env():
    return {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": "/tmp", "GIT_AUTHOR_NAME": "rep", "GIT_AUTHOR_EMAIL": "rep@invalid",
            "GIT_COMMITTER_NAME": "rep", "GIT_COMMITTER_EMAIL": "rep@invalid", "GIT_CONFIG_NOSYSTEM": "1"}


def preparer_depot(t, code, essai, bundle, files):
    """Dépôt jouet : main (code du crible et compagnons, fiche, texte, addendum, registres) ; lot (paquet de l'arbre)."""
    distant = os.path.join(t, "distant.git")
    sh("git", "init", "-q", "--bare", "-b", "main", distant, env=git_env())
    for k, v in (("uploadpack.allowAnySHA1InWant", "true"), ("uploadpack.allowFilter", "true")):
        sh("git", "-C", distant, "config", k, v, env=git_env())
    w = os.path.join(t, "travail")
    sh("git", "clone", "-q", distant, w, env=git_env())
    sh("git", "-C", w, "checkout", "-q", "-b", "main", env=git_env())
    dc = os.path.join(w, "docs", "procedures", "crible-v-v1")
    os.makedirs(dc)
    for f in sorted(os.listdir(code)):
        if f.endswith((".py", ".sh")):
            shutil.copyfile(os.path.join(code, f), os.path.join(dc, f))
            b = open(os.path.join(dc, f), "rb").read()
            open(os.path.join(dc, f) + ".sha256", "w").write(f"{hashlib.sha256(b).hexdigest()}  {f}\n")
    os.makedirs(os.path.join(w, "prereg"))
    shutil.copyfile(os.path.join(essai, "texte-essai.txt"), os.path.join(w, "prereg", "crible-v-texte-essai.md"))
    lignes = [f"- `{hashlib.sha256(open(os.path.join(dc, f), 'rb').read()).hexdigest()}  docs/procedures/crible-v-v1/{f}`"
              for f in ("crible_v_commun_v1.py", "lanceur_crible_v_v1.py", "mesure_crible_v_v1.py", "lire_crible_v_v1.py",
                        "machine_crible_v_v1.py")]
    open(os.path.join(w, "prereg", "crible-v-addendum-essai.md"), "w").write("# addendum d'essai\n" + "\n".join(lignes) + "\n")
    sha = lambda p: hashlib.sha256(open(os.path.join(w, p), "rb").read()).hexdigest()  # noqa: E731
    fiche = {"version": "fiche-lancement-crible-v-v1", "texte": {"chemin": "prereg/crible-v-texte-essai.md", "sha256": sha("prereg/crible-v-texte-essai.md")},
             "addendum": {"chemin": "prereg/crible-v-addendum-essai.md", "sha256": sha("prereg/crible-v-addendum-essai.md")},
             "duree_d_s": 5000, "files": files}
    open(os.path.join(dc, "fiche-lancement-crible-v-v1.json"), "w").write(json.dumps(fiche, indent=1, sort_keys=True) + "\n")
    os.makedirs(os.path.join(w, "registres"))
    jour = time.strftime("%Y-%m-%d", time.gmtime())
    open(os.path.join(w, "registres", "go.md"), "w").write(
        "| ID | accordé | type | périmètre | plafond | échéance | par | réf. |\n|---|---|---|---|---|---|---|---|\n"
        f"| GO-2099-01-01-01 | {jour} | calcul | Organisme d'idéation, crible (v), part sur crédits de Claude (essai) | 104.39 USD | 2099-12-31 | Lazar | GO-2026-11-15-06 |\n"
        f"| GO-2099-01-01-02 | {jour} | calcul | Même crible, part hors crédits (essai) | 100.28 USD | 2099-12-31 | Lazar | GO-2026-11-15-06 |\n")
    open(os.path.join(w, "registres", "decisions.md"), "w").write("| R-1 | feu d'essai |\n")
    sh("git", "-C", w, "add", "-A", env=git_env())
    sh("git", "-C", w, "commit", "-q", "-m", "code du crible (essai)", env=git_env())
    sh("git", "-C", w, "push", "-q", "origin", "main", env=git_env())
    cc = sh("git", "-C", w, "rev-parse", "HEAD", env=git_env()).stdout.strip()
    sh("git", "-C", w, "checkout", "-q", "--orphan", "lot", env=git_env())
    sh("git", "-C", w, "rm", "-q", "-r", "--cached", ".", env=git_env())
    os.makedirs(os.path.join(w, os.path.dirname(BUNDLE_REL)), exist_ok=True)
    shutil.copyfile(bundle, os.path.join(w, BUNDLE_REL))
    sh("git", "-C", w, "add", BUNDLE_REL, env=git_env())
    sh("git", "-C", w, "commit", "-q", "-m", "paquet de l'arbre", env=git_env())
    sh("git", "-C", w, "push", "-q", "origin", "lot", env=git_env())
    cl = sh("git", "-C", w, "rev-parse", "HEAD", env=git_env()).stdout.strip()
    sh("git", "-C", w, "checkout", "-q", "-f", "main", env=git_env())
    sh("git", "-C", w, "clean", "-q", "-fdx", env=git_env())
    return distant, w, cc, cl, fiche, sha(os.path.join("docs", "procedures", "crible-v-v1", "fiche-lancement-crible-v-v1.json"))


def loueur_simule(t):
    f = os.path.join(t, "curl-simule")
    j = os.path.join(t, "loueur.log")
    open(f, "w").write(f"#!/bin/sh\necho \"$(date -u +%FT%TZ) $*\" | sed 's/Bearer [^ ]*/Bearer <cle>/' >> {j}\nprintf 200\n")
    os.chmod(f, 0o755)
    return f, j


def lancer_amorce(t, distant, cc, cl, fiche_sha, essai, cas, echeance_s, extra=None, br="v1"):
    racine = os.path.join(t, f"racine-{cas}")
    os.makedirs(racine)
    curl, journal = loueur_simule(os.path.join(t))
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": racine, "AMORCE_REPETITION": "1", "RACINE_AMORCE": racine,
           "DEPOT_URL_REPETITION": "file://" + distant, "CURL_REPETITION": curl, "DUREES_REPETITION": "0 1000000 2",
           "PY_REPETITION": sys.executable, "COMMIT_CODE": cc, "COMMIT_LOT": cl, "ECHEANCE_UTC_S": str(int(time.time() + echeance_s)),
           "FICHE_SHA256": fiche_sha, "GO_KV1": "GO-2099-01-01-01", "GO_KV2": "GO-2099-01-01-02",
           "BR_SORTIE": f"calcul/crible-v-v1-sortie-{br}", "BR_ENTREE": f"calcul/crible-v-v1-entree-{br}", "CONTAINER_ID": "4242",
           "CONTAINER_API_KEY": "clelouerfacticeREPETITION", "ATTENTE_PHRASE_S": "900", "ATTENTE_FEU_S": "900", "PAS_ENTREE_S": "2",
           "PAS_ETAT_S": "60", "PAS_REPRISE_S": "5", "BORNE_ESSAI_S": "15", "REPETITION_SANS_PIP": "1", "REPETITION_REEL_A_BLANC": "1",
           "REPETITION_SECRET": os.path.join(essai, "prive", "secret.bin"), "REPETITION_MONDES": os.path.join(essai, "prive"),
           "REPETITION_SORTIR_A_LA_FIN": "1", "REPETITION_DECALAGE_PORTS": "4000", **CLES_FACTICES}
    env.update(extra or {})
    amorce = os.path.join(t, "travail", "docs", "procedures", "crible-v-v1", "amorce_crible_v_v1.sh")
    sortie = open(os.path.join(t, f"amorce-{cas}.log"), "w")
    p = subprocess.Popen(["bash", amorce], env=env, stdout=sortie, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, start_new_session=True)
    return p, racine, journal, env


def session(t, *a):
    return sh(sys.executable, "-I", "-B", os.path.join(t, "travail", "docs", "procedures", "crible-v-v1", "session_crible_v_v1.py"), *a,
              env={"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": "/tmp", **{k: v for k, v in git_env().items()}}, ok=False)


def etape(t, br):
    r = session(t, "etat", os.path.join(t, "travail"), br)
    for x in r.stdout.splitlines():
        if x.startswith("etape="):
            return x[6:]
    return None


def attendre_etape(t, br, voulues, p, delai=2400):
    fin = time.time() + delai
    while time.time() < fin:
        e = etape(t, br)
        if e in voulues:
            return e
        if p.poll() is not None and e not in voulues:
            time.sleep(3)
            return etape(t, br)
        time.sleep(3)
    return etape(t, br)


def inscrire(t, nom, lignes):
    w = os.path.join(t, "travail")
    sh("git", "-C", w, "fetch", "-q", "origin", "+refs/heads/main:refs/remotes/origin/main", env=git_env())
    sh("git", "-C", w, "reset", "-q", "--hard", "refs/remotes/origin/main", env=git_env())
    f = os.path.join(w, "registres", nom)
    with open(f, "a") as x:
        x.write("\n".join(lignes) + "\n")
    sh("git", "-C", w, "add", f, env=git_env())
    sh("git", "-C", w, "commit", "-q", "-m", f"inscription {nom}", env=git_env())
    sh("git", "-C", w, "push", "-q", "origin", "main", env=git_env())
    return sh("git", "-C", w, "rev-parse", "HEAD", env=git_env()).stdout.strip(), f"registres/{nom}"


def lire_sortie(t, br, f):
    w = os.path.join(t, "travail")
    sh("git", "-C", w, "fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}", env=git_env())
    return sh("git", "-C", w, "show", f"refs/remotes/origin/{br}:{f}", env=git_env()).stdout


def feux_jusqu_au_reel(t, cas, br_s, br_e, essai, p, fiche):
    e = attendre_etape(t, br_s, ("attente du feu 1 (phrase)", "arret (A)", "sortie inattendue"), p)
    noter(cas, "barrière 1 atteinte", e == "attente du feu 1 (phrase)", e)
    if e != "attente du feu 1 (phrase)":
        return False
    ss = lire_sortie(t, br_s, "secret-sha256.txt").strip().split("=", 1)[1]
    ci, ch = inscrire(t, f"inscription-{cas}.md", [f"secret {ss}"])
    phrase = os.path.join(t, f"phrase-{cas}.txt")
    shutil.copyfile(os.path.join(essai, "prive", "phrase.txt"), phrase)
    r = session(t, "feu-phrase", os.path.join(t, "travail"), br_s, br_e, phrase, ci, ch)
    sp = [x for x in r.stdout.splitlines() if "empreinte du fichier de la phrase" in x]
    noter(cas, "feu de la phrase (chiffré par la clé de la machine, fichier effacé)", r.returncode == 0 and not os.path.exists(phrase), r.stdout[-200:])
    if sp:
        inscrire(t, f"inscription-{cas}.md", [f"phrase {sp[0].split(': ')[-1]}"])
    e = attendre_etape(t, br_s, ("attente du feu 2 (mondes)", "arret (A)", "sortie inattendue"), p)
    noter(cas, "barrière 2 atteinte", e == "attente du feu 2 (mondes)", e)
    if e != "attente du feu 2 (mondes)":
        return False
    em = json.loads(lire_sortie(t, br_s, "engagement-mondes.json"))
    ec = json.loads(lire_sortie(t, br_s, "engagement-certifiees.json"))
    ci, ch = inscrire(t, f"inscription-{cas}.md", [f"H {em['fichier_mondes_sha256']}", f"HC {ec['certifiees_sha256']}"] + em["mondes_sha256"])
    r = session(t, "feu-mondes", os.path.join(t, "travail"), br_s, br_e, ci, ch)
    noter(cas, "feu des mondes", r.returncode == 0, r.stdout[-160:])
    e = attendre_etape(t, br_s, ("attente du feu 3 (crible reel)", "arret (A)", "sortie inattendue"), p)
    noter(cas, "essai à blanc à M conforme, barrière 3 atteinte", e == "attente du feu 3 (crible reel)", e)
    if e != "attente du feu 3 (crible reel)":
        return False
    ci, ch = inscrire(t, f"inscription-{cas}.md", [f"D = {fiche['duree_d_s']} s", f"M = {fiche['files']}"])
    r = session(t, "feu-reel", os.path.join(t, "travail"), br_s, br_e, "GO-2099-01-01-01", "GO-2099-01-01-02", str(fiche["duree_d_s"]),
                str(fiche["files"]), ci, ch)
    noter(cas, "feu réel (D, M, κv1, κv2 inscrits)", r.returncode == 0, r.stdout[-160:])
    return r.returncode == 0


def recuperer(t, cas, br_s):
    d = os.path.join(t, f"retour-{cas}")
    session(t, "recuperer", os.path.join(t, "travail"), br_s, d)
    return d


def aucune_cle(d):
    for racine, _, fs in os.walk(d):
        for f in fs:
            b = open(os.path.join(racine, f), "rb").read()
            for v in CLES_FACTICES.values():
                import base64
                if v.encode() in b or base64.b64encode(v.encode()) in b:
                    return os.path.join(racine, f)
    return None


def cas_nominal(t, distant, cc, cl, fsha, essai, fiche):
    p, racine, journal, _ = lancer_amorce(t, distant, cc, cl, fsha, essai, "nominal", 61000)
    br_s, br_e = "calcul/crible-v-v1-sortie-v1", "calcul/crible-v-v1-entree-v1"
    if feux_jusqu_au_reel(t, "nominal", br_s, br_e, essai, p, fiche):
        e = attendre_etape(t, br_s, ("fini", "arret (A)", "noeud, machine gardee", "sortie inattendue"), p, delai=3600)
        noter("nominal", "état final « fini »", e == "fini", e)
    try:
        p.wait(timeout=120)
    except subprocess.TimeoutExpired:
        pass
    d = recuperer(t, "nominal", br_s)
    liste = os.path.join(d, "rapatrie-reel", "liste-rapatriement-crible-v-v1.json")
    l = json.load(open(liste)) if os.path.isfile(liste) else {}
    noter("nominal", "rapatriement du crible sans monde", l.get("aucun_monde") is True and any(c[0] == "sortie-mesure-crible-v-v1.json" for c in l.get("copies", [])),
          {k: l.get(k) for k in ("aucun_monde",)})
    noter("nominal", "lecture remise non ouverte", os.path.isfile(os.path.join(d, "remis-au-sous-agent", "sortie-lire-non-ouverte.txt")), "")
    noter("nominal", "aucune clé factice ni jeton dans la branche de sortie (balayage)", aucune_cle(d) is None, aucune_cle(d))
    et = [json.loads(x)["etape"] for x in open(os.path.join(d, "etats-horodates.jsonl"))] if os.path.isfile(os.path.join(d, "etats-horodates.jsonl")) else []
    attendus = ["mise en place", "pieces et arbre", "secret", "attente du feu 1 (phrase)", "mondes", "attente du feu 2 (mondes)", "preparer",
                "essai a blanc", "attente du feu 3 (crible reel)", "sonde reelle", "jouer reel en cours", "mesure", "rapatriement", "fini"]
    noter("nominal", "états horodatés dans l'ordre (durées relevables par deux états consécutifs)", et == attendus, et)
    noter("nominal", "aucun monde, aucun secret hors de la machine", not any(n in os.listdir(d) for n in ("prive", "MONDES.json", "secret.bin")), sorted(os.listdir(d))[:30])
    return p


def cas_phrase_absente(t, distant, cc, cl, fsha, essai, fiche):
    p, *_ = lancer_amorce(t, distant, cc, cl, fsha, essai, "phrase-absente", 61000, {"ATTENTE_PHRASE_S": "40"}, br="v2")
    e = attendre_etape(t, "calcul/crible-v-v1-sortie-v2", ("arret (A)",), p, delai=600)
    m = lire_sortie(t, "calcul/crible-v-v1-sortie-v2", "etat.txt")
    noter("phrase-absente", "arrêt (A) à l'échéance de la barrière 1, sans mondes", e == "arret (A)" and "aucun feu phrase" in m, m.splitlines()[:2])
    return p


def cas_feu_arret(t, distant, cc, cl, fsha, essai, fiche):
    p, racine, *_ = lancer_amorce(t, distant, cc, cl, fsha, essai, "feu-arret", 61000, {"REPETITION_LENT": "2:astra"}, br="v3")
    br_s, br_e = "calcul/crible-v-v1-sortie-v3", "calcul/crible-v-v1-entree-v3"
    if feux_jusqu_au_reel(t, "feu-arret", br_s, br_e, essai, p, fiche):
        e = attendre_etape(t, br_s, ("jouer reel en cours",), p, delai=1200)
        time.sleep(20)
        r = session(t, "feu-arret", os.path.join(t, "travail"), br_e, "repetition : arret pendant jouer")
        noter("feu-arret", "feu d'arrêt poussé", r.returncode == 0 and e == "jouer reel en cours", r.stdout[-120:])
        e = attendre_etape(t, br_s, ("arret (A)",), p, delai=600)
        j = lire_sortie(t, br_s, "journal-machine.txt")
        noter("feu-arret", "lanceur et relais arrêtés par leurs PID, arrêt (A)", e == "arret (A)" and "TERM au PID" in j and "relais du crible" in j,
              [x for x in j.splitlines() if "PID" in x][-3:])
    return p


def cas_minuterie(t, distant, cc, cl, fsha, essai, fiche):
    p, racine, journal, _ = lancer_amorce(t, distant, cc, cl, fsha, essai, "minuterie", 25, {"ATTENTE_PHRASE_S": "600"}, br="v4")
    fin = time.time() + 120
    while time.time() < fin and not (os.path.isfile(journal) and "DELETE" in open(journal).read()):
        time.sleep(3)
    j = open(journal).read() if os.path.isfile(journal) else ""
    noter("minuterie", "destruction demandée au loueur par l'identifiant à l'échéance", "-X DELETE" in j and "/instances/4242/" in j and "<cle>" in j,
          j.splitlines()[-1:] if j else "rien")
    return p


def cas_branche_presente(t, distant, cc, cl, fsha, essai, fiche):
    w = os.path.join(t, "travail")
    sh("git", "-C", w, "push", "-q", "origin", "main:refs/heads/calcul/crible-v-v1-sortie-v5", env=git_env())
    p, racine, *_ = lancer_amorce(t, distant, cc, cl, fsha, essai, "branche-presente", 61000, br="v5")
    try:
        p.wait(timeout=180)
    except subprocess.TimeoutExpired:
        pass
    log = open(os.path.join(t, "amorce-branche-presente.log")).read()
    tete = sh("git", "-C", w, "ls-remote", "origin", "refs/heads/calcul/crible-v-v1-sortie-v5", env=git_env()).stdout.split("\t")[0]
    noter("branche-presente", "branche de sortie déjà présente : rien n'est poussé", "branche de sortie présente" in log and tete == cc, log.splitlines()[-2:])
    return p


def cas_session(t, cc, cl, fsha):
    w = os.path.join(t, "travail")
    d = os.path.join(t, "envoi")
    os.makedirs(d)
    rech = os.path.join(t, "recherche.json")
    json.dump([{"id": 1, "num_gpus": 1, "cpu_arch": "amd64", "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 40, "dph_total": 0.05,
                "storage_cost": 0.1, "inet_down": 500, "reliability2": 0.99, "rentable": True},
               {"id": 2, "num_gpus": 0, "cpu_arch": "arm64", "cpu_cores_effective": 8, "cpu_ram": 16000, "disk_space": 40, "dph_total": 0.01,
                "storage_cost": 0.1, "inet_down": 500, "reliability2": 0.99}], open(rech, "w"))
    r = session(t, "offre-depuis-recherche", rech, os.path.join(d, "offre.json"))
    noter("session", "offre choisie par la garde (amd64, la moins chère acceptée)", r.returncode == 0 and "offre 1" in r.stdout and "offre 2 : refusée" in r.stdout, r.stdout[-120:])
    open(os.path.join(w, "registres", "decisions.md"), "w").write(f"| R-7 | feu du crible GO-2099-01-01-01 GO-2099-01-01-02 {cc} crible-v-v1 |\n")
    r = session(t, "creation", w, "R-7 GO-2099-01-01-02", cc)
    noter("session", "création permise (κv1, κv2 citant GO-2026-11-15-06)", r.returncode == 0, r.stdout[-160:])
    go = open(os.path.join(w, "registres", "go.md")).read()
    open(os.path.join(w, "registres", "go.md"), "w").write(go.replace("| Lazar | GO-2026-11-15-06 |\n", "| Lazar | aucune |\n", 1))
    r = session(t, "creation", w, "R-7 GO-2099-01-01-02", cc)
    noter("session", "ligne « calcul » sans GO-2026-11-15-06 : la création refuse", r.returncode == 2 and "GO-2026-11-15-06" in r.stdout, r.stdout[-160:])
    open(os.path.join(w, "registres", "go.md"), "w").write(go)
    r = session(t, "creation", w, "R-7 GO-2099-01-01-03", cc)
    noter("session", "feu d'un autre GO : refus", r.returncode == 2, r.stdout[-120:])
    sh("git", "-C", w, "fetch", "-q", "origin", "+refs/heads/main:refs/remotes/origin/main", "+refs/heads/lot:refs/remotes/origin/lot", env=git_env())
    ech = str(int(time.time() + 61200))
    r = session(t, "commande", w, os.path.join(d, "offre.json"), cc, cl, ech, "R-7 GO-2099-01-01-02", d, "calcul/crible-v-v1-sortie-v9",
                "calcul/crible-v-v1-entree-v9")
    ok = r.returncode == 0 and r.stdout.count("\n") == 2
    open(os.path.join(d, "commande-imprimee.txt"), "w").write(r.stdout)
    noter("session", "commande imprimée (deux lignes, clés par leur nom)", ok and "$GH_TOKEN" in r.stdout and CLES_FACTICES["GH_TOKEN"] not in r.stdout,
          r.stdout[:160] if ok else r.stdout[-300:])
    r = session(t, "controle-ligne", os.path.join(d, "commande-imprimee.txt"))
    noter("session", "contrôle de la ligne : amorce décodée égale à l'octet", r.returncode == 0 and "LIGNE CONFORME" in r.stdout, r.stdout[:120])
    t2 = open(os.path.join(d, "commande-imprimee.txt")).read().replace("-e GEMINI_API_KEY=$GEMINI_API_KEY", "-e GEMINI_API_KEY=x")
    open(os.path.join(d, "commande-alteree.txt"), "w").write(t2)
    r = session(t, "controle-ligne", os.path.join(d, "commande-alteree.txt"))
    noter("session", "ligne altérée (clé écrite) : refus", r.returncode == 2, r.stdout[-120:])
    r = session(t, "commande", w, os.path.join(d, "offre.json"), cc, cl, str(int(time.time() + 3600)), "R-7 GO-2099-01-01-02", d,
                "calcul/crible-v-v1-sortie-v9", "calcul/crible-v-v1-entree-v9")
    noter("session", "échéance hors de 17 h : refus", r.returncode == 2 and "échéance" in r.stdout, r.stdout[-120:])
    noter("session", "prix relu ≤ 0,17 accepté ; 0,2 refusé", session(t, "prix-relu", "0.06").returncode == 0 and session(t, "prix-relu", "0.2").returncode == 2, "")
    noter("session", "dépense : cumul + 1 h ≥ 3 USD refusée", session(t, "depense", w, "GO-2099-01-01-02", "1.0", "0.06").returncode == 0
          and session(t, "depense", w, "GO-2099-01-01-02", "2.95", "0.06").returncode == 2, "")
    open(os.path.join(d, "id-machine.txt"), "w").write("777\n")
    r = session(t, "detruire", "777", d, "GO-2099-01-01-02")
    noter("session", "destruction imprimée par l'identifiant lu", r.returncode == 0 and "destroy instance 777 -y" in r.stdout, r.stdout[:120])
    noter("session", "identifiant tapé ≠ lu : refus ; intouchable : refus", session(t, "detruire", "778", d, "GO-2099-01-01-02").returncode == 2
          and session(t, "detruire", "58936096", d, "GO-2099-01-01-02").returncode == 2, "")
    lst = os.path.join(t, "liste.json")
    json.dump({"instances": [{"id": 58936096, "label": "x"}]}, open(lst, "w"))
    a = session(t, "absence", "777", "58936096", lst)
    json.dump({"instances": [{"id": 58936096}, {"id": 777}]}, open(lst, "w"))
    b = session(t, "absence", "777", "58936096", lst)
    json.dump({"instances": [{"id": 1}]}, open(lst, "w"))
    c = session(t, "absence", "777", "58936096", lst)
    noter("session", "preuve d'absence : prouvée / toujours listée / témoin absent", (a.returncode, b.returncode, c.returncode) == (0, 2, 2),
          (a.stdout[:60], b.stdout[-60:], c.stdout[-60:]))
    noter("session", "cause d'arrêt bornée", session(t, "feu-arret", w, "calcul/crible-v-v1-entree-v9", "é accent").returncode == 2, "")


def principal(argv=None):
    a = argparse.ArgumentParser()
    for o in ("--code", "--essai", "--bundle", "--travail", "--sortie"):
        a.add_argument(o, required=True)
    a.add_argument("--cas", default="session,branche-presente,minuterie,phrase-absente,nominal,feu-arret")
    a.add_argument("--files", type=int, default=1)
    args = a.parse_args(argv)
    t = os.path.abspath(args.travail)
    os.makedirs(t)
    debut = time.time()
    distant, w, cc, cl, fiche, fsha = preparer_depot(t, os.path.abspath(args.code), os.path.abspath(args.essai), args.bundle, args.files)
    procs = []
    for cas in args.cas.split(","):
        f = {"nominal": cas_nominal, "phrase-absente": cas_phrase_absente, "feu-arret": cas_feu_arret, "minuterie": cas_minuterie,
             "branche-presente": cas_branche_presente}.get(cas)
        try:
            if cas == "session":
                cas_session(t, cc, cl, fsha)
            else:
                procs.append(f(t, distant, cc, cl, fsha, os.path.abspath(args.essai), fiche))
        except Exception as e:  # noqa: BLE001
            noter(cas, "cas joué jusqu'au bout", False, f"{type(e).__name__} : {e}")
    for p in procs:  # R10 : chaque amorce de répétition arrêtée par son groupe de processus (minuterie comprise), lancé ici
        if p is not None:
            try:
                os.killpg(p.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
    out = {"version": "repetition-crible-v-v1", "resultats": RESULTATS, "ecarts": sum(1 for r in RESULTATS if not r["ok"]),
           "cas": len(RESULTATS), "duree_s": round(time.time() - debut, 1), "commit_code": cc, "commit_lot": cl}
    with open(args.sortie, "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: out[k] for k in ("cas", "ecarts", "duree_s")}))
    return 0 if out["ecarts"] == 0 else 1


if __name__ == "__main__":
    sys.exit(principal())
