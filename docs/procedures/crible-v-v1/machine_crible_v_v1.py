"""Programme machine du crible (v), v1 (fichier neuf, R12) — joué sur la machine louée après l'amorce (même PID ; la minuterie de
destruction est l'enfant de l'amorce). Modèle : le programme machine du pilote MR-2 sans ssh (`machine_pilote_mr2_v74_v2.sh` et son
aide, branche `lot/compte-organisme-v1`, lus, non modifiés), écrit ici en Python pour être répété hors ligne.

Il joue, dans l'ordre, les états de la procédure `procedure-machine-crible-v-v1.md` (même dossier) : `mise en place` → `pieces et
arbre` → `secret` → `attente du feu 1 (phrase)` → `mondes` → `attente du feu 2 (mondes)` → `preparer` → `essai a blanc` →
`attente du feu 3 (crible reel)` → `sonde reelle` → `jouer reel en cours` → `mesure` → `rapatriement` → finales : `fini`,
`arret (A)`, `noeud, machine gardee`, `sortie inattendue`. Chaque changement d'état est horodaté (`etats-horodates.jsonl`, poussé)
pour que les durées de la mise en place, de la génération, de la mesure et du rapatriement se relèvent par deux états consécutifs.

Tout ce qui sort est poussé sur la branche neuve de sortie (BR_SORTIE), après un **balayage** (jeton, trois clés brutes et en
base64, secret brut, hexadécimal et base64, phrase brute et base64) : un fichier où une forme est trouvée est exclu et nommé
(jamais la valeur). Rien de privé ne sort : secret, phrase, clé privée de la phrase, mondes, étiquettes C8, textes servis restent
sous `prive/` ou `reel/prive/` et meurent avec la machine. Aux trois barrières, la machine attend un feu de la mère sur la branche
d'entrée (BR_ENTREE). Un feu d'arrêt est lu à chaque attente et toutes les minutes pendant `jouer` réel (arrêt du lanceur **et de
ses relais par leurs PID**, R10). Aucune fin ne détruit la machine (la session détruit par l'identifiant, ou la minuterie).
"""
import base64
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import time

E_ = os.environ
REP = E_.get("AMORCE_REPETITION") == "1"
# --- secrets : dans ce programme seulement, retirés de l'environnement des enfants -------------------------------------------------
JETON = E_.pop("GH_TOKEN", "")
CLES = {n: E_.pop(n, "") for n in ("RR_ANTHROPIC_API_KEY_RIGAUD", "GEMINI_API_KEY", "OPENAI_API_KEY")}
E_.pop("CONTAINER_API_KEY", None)
COMMIT_CODE, COMMIT_LOT = E_["COMMIT_CODE"], E_["COMMIT_LOT"]
ECHEANCE = int(E_["ECHEANCE_UTC_S"])
FICHE_SHA256, GO_KV1, GO_KV2 = E_["FICHE_SHA256"], E_["GO_KV1"], E_["GO_KV2"]
BR_S, BR_E = E_["BR_SORTIE"], E_["BR_ENTREE"]
T = E_["T"]
PID_MINUTERIE = E_.get("PID_MINUTERIE", "")
RELANCE = E_.get("RELANCE") == "1"
URL = E_.get("DEPOT_URL_REPETITION", "") if REP else "https://github.com/lciric/controle-ia-travail.git"
PY = E_.get("PY_REPETITION", "python3") if REP else "python3"
D = os.path.join(T, "depot")
X = os.path.join(T, "sortie")
S = os.path.join(T, "depot-sortie")
PV = os.path.join(T, "prive")
EN = os.path.join(T, "entree")
L = os.path.join(X, "journal-machine.txt")
CODE = os.path.join(D, "docs", "procedures", "crible-v-v1")
LANCEUR = os.path.join(CODE, "lanceur_crible_v_v1.py")
FICHE_REL = "docs/procedures/crible-v-v1/fiche-lancement-crible-v-v1.json"
BUNDLE_REL = "docs/notes/organisme-multi-generations-v1/pilote-v1/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle"
SHA_BUNDLE = "e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1"
TETE_ARBRE = "605e0f60f3eed0948948e6a4eb15cb73de1d03de"
NUMPY = "2.5.3"
DECALAGE = int(E_.get("REPETITION_DECALAGE_PORTS", "0")) if REP else 0   # répétition seulement : ports d'essai décalés
PORTS = tuple(p + 10 * k + DECALAGE for k in (0, 1) for p in (8811, 8812, 8813, 8814))
DUREES = {"ATTENTE_PHRASE_S": 3600, "ATTENTE_FEU_S": 1200, "PAS_ENTREE_S": 60, "PAS_ETAT_S": 900, "PAS_REPRISE_S": 300,
          "BORNE_ESSAI_S": 60}
if REP:
    for k in DUREES:
        if E_.get(k):
            DUREES[k] = float(E_[k])
else:
    for k in list(E_):
        if k.startswith("REPETITION_") or k in DUREES:
            sys.exit(f"CRIBLEV MACHINE REFUS : {k} en répétition seulement")
SEUIL = 95_000_000
PX = "/usr/local/bin:/usr/bin:/bin"
ETAT = {"etape": "debut", "motif": "", "reel": "", "H": "", "HC": "", "code_jouer": "", "code_mesurer": "", "poussee": 0,
        "exclus": [], "debut": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
POUSSEE_OK = [False]


def utc():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def j(msg):
    os.makedirs(X, exist_ok=True)
    ligne = f"{utc()} CRIBLEV MACHINE {msg}"
    with open(L, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    print(ligne, flush=True)


def etape(e, motif=""):
    if e != ETAT["etape"]:
        with open(os.path.join(X, "etats-horodates.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps({"etape": e, "utc": utc(), "s": round(time.time(), 1)}, ensure_ascii=False) + "\n")
    ETAT["etape"], ETAT["motif"] = e, motif


def ecrire_etat():
    with open(os.path.join(X, "etat.txt"), "w", encoding="utf-8") as f:
        for k in ("etape", "motif"):
            f.write(f"{k}={ETAT[k]}\n")
        f.write(f"heure={utc()}\ndebut={ETAT['debut']}\necheance={time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ECHEANCE))}\n")
        f.write(f"minuterie_pid={PID_MINUTERIE}\nreel={ETAT['reel']}\nfichier_mondes_sha256={ETAT['H']}\ncertifiees_sha256={ETAT['HC']}\n")
        f.write(f"code_jouer={ETAT['code_jouer']}\ncode_mesurer={ETAT['code_mesurer']}\npoussee={ETAT['poussee']}\n")
        f.write(f"relance_du_conteneur={int(RELANCE)}\nexclus_balayage={' '.join(ETAT['exclus'])}\n")


def g(*a, cwd=None, env_jeton=True, entree=None):
    env = {"PATH": PX, "HOME": os.path.join(T, "maison-git"), "GIT_TERMINAL_PROMPT": "0"}
    if env_jeton:
        env["GH_TOKEN"] = JETON
    os.makedirs(env["HOME"], exist_ok=True)
    return subprocess.run(["git", *a], cwd=cwd, env=env, capture_output=True, input=entree)


# --- traces, balayage, poussée -------------------------------------------------------------------------------------------------

LISTE_BLANCHE_FICHIERS = ("mise-en-place.txt", "secret-sha256.txt", "cle-publique-phrase.pem", "cle-publique-phrase.empreinte",
                          "phrase-sha256.txt", "engagement-mondes.json", "engagement-certifiees.json", "lancements.jsonl",
                          "lancements-sonde.jsonl")
DOSSIERS_PERMIS = ("rapatrie-blanc", "rapatrie-sonde", "rapatrie-reel", "remis-au-sous-agent")


def copier_traces():
    for n in os.listdir(T):
        f = os.path.join(T, n)
        if os.path.isfile(f) and (re.fullmatch(r"(journal|code)-\d\d-[a-z0-9-]+\.txt", n) or n in LISTE_BLANCHE_FICHIERS):
            shutil.copyfile(f, os.path.join(X, n))
    for n in DOSSIERS_PERMIS:
        src = os.path.join(T, n)
        if os.path.isdir(src):
            shutil.rmtree(os.path.join(X, n), ignore_errors=True)
            shutil.copytree(src, os.path.join(X, n))


def formes_secretes():
    formes = []
    for v in [JETON] + list(CLES.values()):
        if v:
            formes += [v.encode(), base64.b64encode(v.encode())]
    for chemin, mini in ((os.path.join(PV, "secret.bin"), 1), (os.path.join(PV, "phrase.txt"), 8)):
        if os.path.isfile(chemin):
            b = open(chemin, "rb").read()
            if chemin.endswith("secret.bin"):
                formes += [b, b.hex().encode(), b.hex().upper().encode(), base64.b64encode(b)]
            else:
                p = b.rstrip(b"\n")
                if len(p) >= mini:
                    formes += [p, base64.b64encode(p)]
    return [f for f in formes if f]


def balayer(racine):
    """Rend les chemins (relatifs) des fichiers où une forme secrète est trouvée (jamais la valeur)."""
    formes, exclus = formes_secretes(), []
    for d, ds, fs in os.walk(racine):
        ds[:] = [x for x in ds if x != ".git"]
        for n in fs:
            f = os.path.join(d, n)
            b = open(f, "rb").read()
            if any(x in b for x in formes):
                exclus.append(os.path.relpath(f, racine))
    return sorted(exclus)


def pousser(motif):
    POUSSEE_OK[0] = False
    ETAT["poussee"] += 1
    copier_traces()
    ecrire_etat()
    if not os.path.isdir(os.path.join(S, ".git")):
        aide = '!f() { echo username=x-access-token; echo "password=${GH_TOKEN}"; }; f'
        for a in (("init", "-q", S), ("-C", S, "remote", "add", "origin", URL), ("-C", S, "config", "credential.helper", aide),
                  ("-C", S, "config", "user.name", "machine du crible (v)"), ("-C", S, "config", "user.email", "machine-crible@invalid")):
            if g(*a).returncode != 0:
                j("dépôt de sortie impossible")
                return False
    for n in os.listdir(S):
        if n != ".git":
            p = os.path.join(S, n)
            shutil.rmtree(p) if os.path.isdir(p) else os.unlink(p)
    shutil.copytree(X, S, dirs_exist_ok=True)
    for d, ds, fs in os.walk(S):
        ds[:] = [x for x in ds if x != ".git"]
        for n in fs:
            if os.path.getsize(os.path.join(d, n)) > SEUIL:
                j(f"fichier de plus de 95 Mo : {os.path.relpath(os.path.join(d, n), S)} : poussée refusée")
                return False
    exclus = balayer(S)
    if exclus:
        ETAT["exclus"] = sorted(set(ETAT["exclus"]) | set(exclus))
        j(f"BALAYAGE : forme secrète trouvée : fichier(s) exclu(s) de toute poussée : {' '.join(exclus)[:300]}")
        for r in exclus:
            os.unlink(os.path.join(S, r))
        ecrire_etat()
        shutil.copyfile(os.path.join(X, "etat.txt"), os.path.join(S, "etat.txt"))
        if balayer(S):
            j("BALAYAGE : refus après exclusion : poussée refusée")
            return False
    if g("-C", S, "add", "-A").returncode != 0:
        return False
    if g("-C", S, "diff", "--cached", "--quiet").returncode != 0:
        if g("-C", S, "commit", "-q", "-m", f"crible (v) : {motif} (poussée {ETAT['poussee']})").returncode != 0:
            j("commit de sortie impossible")
            return False
    loc = g("-C", S, "rev-parse", "HEAD").stdout.decode().strip()
    for n in (1, 2, 3):
        if g("-C", S, "push", "-q", "origin", f"HEAD:refs/heads/{BR_S}").returncode == 0:
            dist = g("-C", S, "ls-remote", "origin", f"refs/heads/{BR_S}").stdout.decode().split("\t")[0]
            if dist == loc:
                j(f"poussé ({motif}) : {loc}")
                POUSSEE_OK[0] = True
                return True
        j(f"poussée refusée, essai {n}/3")
        time.sleep(min(10 * n, DUREES["PAS_REPRISE_S"]))
    return False


def attente_finale():
    k = 0
    while not POUSSEE_OK[0]:
        k += 1
        j(f"dernière poussée en échec : reprise {k} dans {DUREES['PAS_REPRISE_S']:g} s (jusqu'à l'échéance)")
        time.sleep(DUREES["PAS_REPRISE_S"])
        pousser(f"reprise {k} ({ETAT['etape']})")
    for n in list(CLES):
        CLES[n] = ""
    j(f"FIN ({ETAT['etape']}) : attente sans calcul ; destruction par la session (identifiant) ou par la minuterie")
    if REP and E_.get("REPETITION_SORTIR_A_LA_FIN") == "1":
        sys.exit(0)
    while True:
        time.sleep(3600)


def rapatrier(source, destination):
    if not os.path.isdir(source) or os.path.exists(destination) or not ETAT["H"]:
        return True
    r = O("rapatrier", "--source", source, "--destination", destination, "--mondes", os.path.join(PV, "MONDES.json"),
          "--mondes-sha256", ETAT["H"], "--arbre", os.path.join(T, "arbre", "orchestrator"), journal=f"journal-11-{os.path.basename(destination)}.txt")
    if r != 0:
        shutil.rmtree(destination, ignore_errors=True)
        j(f"rapatriement de {os.path.basename(source)} non conforme : rien n'en sort")
        return False
    return True


def arret_A(motif):
    etape("arret (A)", motif)
    j(f"ARRET (A) : {motif}")
    if ETAT["reel"]:
        rapatrier(os.path.join(T, ETAT["reel"]), os.path.join(T, "rapatrie-reel"))
    pousser("arrêt (A)") or j("traces non poussées : motif ci-dessus, lisible par les journaux du loueur")
    attente_finale()


def noeud_garde(motif):
    etape("noeud, machine gardee", motif)
    j(f"NOEUD, MACHINE GARDEE : {motif}")
    if ETAT["reel"]:
        rapatrier(os.path.join(T, ETAT["reel"]), os.path.join(T, "rapatrie-reel"))
    pousser("nœud, machine gardée") or j("traces non poussées")
    attente_finale()


# --- lanceur, entrée, inscriptions ---------------------------------------------------------------------------------------------

def O(*a, journal, cles=False, attendre=True):
    env = {"PATH": PX, "HOME": "/root" if not REP else T}
    if cles:
        env.update(CLES)
    f = open(os.path.join(T, journal), "w", encoding="utf-8")
    p = subprocess.Popen([PY, "-I", "-B", LANCEUR, *a], stdout=f, stderr=subprocess.STDOUT, env=env, stdin=subprocess.DEVNULL,
                         cwd=T)
    if not attendre:
        return p
    c = p.wait()
    f.close()
    with open(os.path.join(T, journal.replace("journal-", "code-")), "w") as fc:
        fc.write(f"{c}\n")
    return c


def lire_entree(nom):
    g("-C", D, "fetch", "-q", "--depth=1", "origin", f"+refs/heads/{BR_E}:refs/remotes/origin/entree")
    r = g("-C", D, "show", f"refs/remotes/origin/entree:{nom}")
    return r.stdout if r.returncode == 0 else None


def lire_feu(b, genre):
    if b is None:
        return None
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        return None
    d = {}
    for x in t.splitlines():
        if "=" not in x:
            return None
        k, v = x.split("=", 1)
        d[k] = v
    return d if d.get("feu") == genre else None


def arret_demande():
    d = lire_feu(lire_entree("feu-arret.txt"), "arret")
    return d is not None and re.fullmatch(r"[A-Za-z0-9 ,.:;()_-]{1,100}", d.get("cause", "")) is not None, d


def attendre_feu(nom, genre, fin, attendus):
    vu = None
    while time.time() < fin:
        a, d = arret_demande()
        if a:
            arret_A(f"feu d'arrêt de la mère ({d.get('cause')})")
        b = lire_entree(nom)
        f = lire_feu(b, genre)
        if f is not None and all(f.get(k) == v for k, v in attendus.items()):
            j(f"feu {genre} conforme")
            return f
        if b is not None and hashlib.sha256(b).hexdigest() != vu:
            vu = hashlib.sha256(b).hexdigest()
            j(f"feu {genre} refusé (attente continuée)")
        time.sleep(DUREES["PAS_ENTREE_S"])
    arret_A(f"aucun feu {genre} conforme avant {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(fin))}")


def inscription_sur_main(feu, empreintes):
    c, ch = feu.get("inscription_commit", ""), feu.get("inscription_chemin", "")
    if not re.fullmatch(r"[0-9a-f]{40}", c) or not re.fullmatch(r"[A-Za-z0-9._-]+(/[A-Za-z0-9._-]+)*", ch) or ".." in ch:
        arret_A("inscription illisible")
    if g("-C", D, "fetch", "-q", "--depth=200", "origin", "+refs/heads/main:refs/remotes/origin/main").returncode != 0:
        arret_A("main injoignable : inscription non prouvée")
    if g("-C", D, "merge-base", "--is-ancestor", c, "refs/remotes/origin/main").returncode != 0:
        arret_A("commit d'inscription absent de main (200 derniers commits)")
    r = g("-C", D, "show", f"{c}:{ch}")
    if r.returncode != 0 or any(e.encode() not in r.stdout for e in empreintes):
        arret_A("empreintes non inscrites sur main")
    j(f"inscription prouvée sur main ({c[:12]}, {ch})")


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


def ports_libres():
    import socket
    for p in PORTS:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # comme le serveur des relais (aucun faux refus sur TIME_WAIT)
        try:
            s.bind(("127.0.0.1", p))
        except OSError:
            return p
        finally:
            s.close()
    return None


def tuer_par_pid(pids, quoi):
    for pid in pids:
        try:
            os.kill(int(pid), signal.SIGTERM)
            j(f"{quoi} : TERM au PID {pid} (R10)")
        except (ProcessLookupError, ValueError):
            pass


# --- déroulé ---------------------------------------------------------------------------------------------------------------------

def principal():
    os.makedirs(X, exist_ok=True)
    os.makedirs(EN, exist_ok=True)
    os.makedirs(PV, mode=0o700, exist_ok=True)
    os.chmod(PV, 0o700)
    if RELANCE:
        arret_A("relance du conteneur par le loueur : aucune passe refaite (tout processus du crible a été interrompu)")
    # mise en place
    etape("mise en place")
    j(f"début ; échéance de la minuterie {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ECHEANCE))}")
    c = g("-C", D, "ls-remote", "--exit-code", "origin", f"refs/heads/{BR_S}").returncode
    if c != 2:
        j(f"ARRET : branche de sortie présente (R12) ou dépôt injoignable (code {c}) : rien n'est poussé")
        POUSSEE_OK[0] = True
        attente_finale()
    c = g("-C", D, "ls-remote", "--exit-code", "origin", f"refs/heads/{BR_E}").returncode
    if c != 2:
        arret_A(f"branche d'entrée déjà présente avant la machine (code {c}) : un feu ancien serait lu")
    if not pousser("mise en place commencée"):
        j("ARRET : première poussée impossible")
        attente_finale()
    with open(os.path.join(T, "mise-en-place.txt"), "w") as f:
        f.write(f"nproc {os.cpu_count()}\n")
    if not (REP and E_.get("REPETITION_SANS_PIP") == "1"):
        r = subprocess.run([PY, "-m", "pip", "install", "--no-cache-dir", f"numpy=={NUMPY}"], capture_output=True, timeout=900,
                           env={"PATH": PX, "HOME": "/root"})
        open(os.path.join(T, "journal-03-pip.txt"), "wb").write(r.stdout[-20000:] + r.stderr[-20000:])
        if r.returncode != 0:
            arret_A(f"installation de numpy {NUMPY} en échec")
    v = subprocess.run([PY, "-I", "-c", "import sys,numpy;print(sys.version_info[:2],numpy.__version__)"], capture_output=True,
                       text=True, env={"PATH": PX}).stdout.strip()
    with open(os.path.join(T, "mise-en-place.txt"), "a") as f:
        f.write(f"python_numpy {v}\n")
    if v != f"(3, 13) {NUMPY}":
        arret_A(f"python ou numpy inattendu : {v}")
    # pièces et arbre
    etape("pieces et arbre")
    fiche_f = os.path.join(D, FICHE_REL)
    if not os.path.isfile(fiche_f) or sha(fiche_f) != FICHE_SHA256:
        arret_A("fiche de lancement absente ou d'empreinte différente")
    fiche = json.load(open(fiche_f, encoding="utf-8"))
    for cle in ("texte", "addendum"):
        p = os.path.join(D, fiche[cle]["chemin"])
        if not os.path.isfile(p) or sha(p) != fiche[cle]["sha256"]:
            arret_A(f"{cle} de la fiche absent ou d'empreinte différente")
    if not (isinstance(fiche.get("duree_d_s"), (int, float)) and fiche.get("files") in (1, 2)):
        arret_A("fiche : D et M illisibles")
    for p in ("runs", "diag", "donnees", "registres"):
        if os.path.exists(os.path.join(D, p)):
            arret_A(f"{p}/ présent dans l'arbre extrait")
    b = g("-C", D, "show", f"{COMMIT_LOT}:{BUNDLE_REL}")
    if b.returncode != 0 or hashlib.sha256(b.stdout).hexdigest() != SHA_BUNDLE:
        arret_A("paquet de l'arbre absent de COMMIT_LOT ou d'empreinte différente")
    open(os.path.join(T, "arbre.bundle"), "wb").write(b.stdout)
    for a in (("init", "-q", os.path.join(T, "arbre")), ("-C", os.path.join(T, "arbre"), "bundle", "unbundle", os.path.join(T, "arbre.bundle")),
              ("-C", os.path.join(T, "arbre"), "-c", "advice.detachedHead=false", "checkout", "-q", TETE_ARBRE)):
        if g(*a, env_jeton=False).returncode != 0:
            arret_A("dépaquetage de l'arbre")
    if g("-C", os.path.join(T, "arbre"), "rev-parse", "HEAD").stdout.decode().strip() != TETE_ARBRE \
            or g("-C", os.path.join(T, "arbre"), "status", "--porcelain", "--ignored").stdout.strip():
        arret_A("arbre : tête ≠ 605e0f6 ou arbre non propre")
    texte = os.path.join(D, fiche["texte"]["chemin"])
    addendum = os.path.join(D, fiche["addendum"]["chemin"])
    for nom in ("crible_v_commun_v1.py", "lanceur_crible_v_v1.py", "mesure_crible_v_v1.py", "lire_crible_v_v1.py"):
        s = sha(os.path.join(CODE, nom))
        if s not in open(addendum, encoding="utf-8").read():
            arret_A(f"code du crible : {nom} absent de l'addendum d'empreintes")
    j("pièces aux empreintes attendues ; arbre 605e0f6 propre ; code du crible dans l'addendum")
    orch = os.path.join(T, "arbre", "orchestrator")
    # secret, puis phrase de Lazar (barrière 1)
    etape("secret")
    if REP and E_.get("REPETITION_SECRET"):
        shutil.copyfile(E_["REPETITION_SECRET"], os.path.join(PV, "secret.bin"))
        os.chmod(os.path.join(PV, "secret.bin"), 0o600)
        ss = sha(os.path.join(PV, "secret.bin"))
    else:
        if O("secret", "--arbre", orch, os.path.join(PV, "secret.bin"), journal="journal-05-secret.txt") != 0:
            arret_A("secret : code non nul")
        ss = json.loads(open(os.path.join(T, "journal-05-secret.txt")).read().strip().splitlines()[-1])["secret_sha256"]
    if subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:4096", "-out", os.path.join(PV, "cle-phrase.pem")],
                      capture_output=True).returncode != 0 or \
            subprocess.run(["openssl", "pkey", "-in", os.path.join(PV, "cle-phrase.pem"), "-pubout", "-out",
                            os.path.join(T, "cle-publique-phrase.pem")], capture_output=True).returncode != 0:
        arret_A("clé de la phrase impossible")
    os.chmod(os.path.join(PV, "cle-phrase.pem"), 0o600)
    der = subprocess.run(["openssl", "pkey", "-pubin", "-in", os.path.join(T, "cle-publique-phrase.pem"), "-outform", "DER"],
                         capture_output=True).stdout
    open(os.path.join(T, "cle-publique-phrase.empreinte"), "w").write(hashlib.sha256(der).hexdigest() + "\n")
    open(os.path.join(T, "secret-sha256.txt"), "w").write(f"secret_sha256={ss}\n")
    etape("attente du feu 1 (phrase)", "empreinte du secret à inscrire sur main ; puis phrase chiffrée")
    pousser("secret engagé, attente de la phrase") or arret_A("empreinte du secret non poussée")
    debut = os.path.getmtime(os.path.join(T, "amorce-lancee")) if os.path.exists(os.path.join(T, "amorce-lancee")) else time.time()
    feu = attendre_feu("feu-1-phrase.txt", "phrase", debut + DUREES["ATTENTE_PHRASE_S"], {"secret_sha256": ss})
    inscription_sur_main(feu, [ss])
    ch = lire_entree("phrase-chiffree.b64")
    if ch is None:
        arret_A("phrase chiffrée absente de la branche d'entrée")
    try:
        open(os.path.join(EN, "phrase.chiffree"), "wb").write(base64.b64decode(ch, validate=True))
    except ValueError:
        arret_A("phrase chiffrée : base64 illisible")
    r = subprocess.run(["openssl", "pkeyutl", "-decrypt", "-inkey", os.path.join(PV, "cle-phrase.pem"), "-pkeyopt",
                        "rsa_padding_mode:oaep", "-pkeyopt", "rsa_oaep_md:sha256", "-pkeyopt", "rsa_mgf1_md:sha256",
                        "-in", os.path.join(EN, "phrase.chiffree"), "-out", os.path.join(PV, "phrase.txt")], capture_output=True)
    subprocess.run(["shred", "-u", os.path.join(PV, "cle-phrase.pem")], check=False)
    if r.returncode != 0:
        arret_A("phrase : déchiffrement impossible")
    os.chmod(os.path.join(PV, "phrase.txt"), 0o600)
    pb = open(os.path.join(PV, "phrase.txt"), "rb").read()
    if not (2 <= len(pb) <= 400 and pb.count(b"\n") == 1 and pb.endswith(b"\n") and b"\0" not in pb):
        arret_A("phrase de forme non conforme")
    ps = hashlib.sha256(pb).hexdigest()
    if ps != feu.get("phrase_fichier_sha256"):
        arret_A("phrase : empreinte du fichier ≠ celle du feu")
    open(os.path.join(T, "phrase-sha256.txt"), "w").write(f"phrase_fichier_sha256={ps}\n")
    j("phrase reçue, empreinte égale à celle du feu ; clé privée de la phrase effacée")
    # mondes (barrière 2)
    etape("mondes")
    pousser("phrase reçue, génération des mondes")
    mondes = os.path.join(PV, "MONDES.json")
    if REP and E_.get("REPETITION_MONDES"):
        for n in ("MONDES.json", "MONDES.json.engagement.json", "CERTIFIEES.json", "MONDES.json.certifiees.engagement.json"):
            shutil.copyfile(os.path.join(E_["REPETITION_MONDES"], n), os.path.join(PV, n))
        lu = {"fichier_mondes_sha256": sha(mondes), "certifiees_sha256": sha(os.path.join(PV, "CERTIFIEES.json"))}
        open(os.path.join(T, "journal-06-generer.txt"), "w").write(json.dumps(lu) + "\n")
    else:
        c = O("generer", "--arbre", orch, "--secret", os.path.join(PV, "secret.bin"), "--phrase-fichier", os.path.join(PV, "phrase.txt"),
              "--texte", texte, "--texte-sha256", fiche["texte"]["sha256"], "--sortie", mondes, "--processus", str(os.cpu_count() or 1),
              journal="journal-06-generer.txt")
        if c != 0:
            arret_A(f"generer : code {c} (une graine neuve demande un texte neuf et le mot de Lazar)")
        lu = json.loads(open(os.path.join(T, "journal-06-generer.txt")).read().strip().splitlines()[-1])
    ETAT["H"], ETAT["HC"] = lu["fichier_mondes_sha256"], lu["certifiees_sha256"]
    if sha(mondes) != ETAT["H"] or sha(os.path.join(PV, "CERTIFIEES.json")) != ETAT["HC"]:
        arret_A("mondes ou étiquettes : empreinte différente de celle rendue par generer")
    shutil.copyfile(mondes + ".engagement.json", os.path.join(T, "engagement-mondes.json"))
    shutil.copyfile(mondes + ".certifiees.engagement.json", os.path.join(T, "engagement-certifiees.json"))
    shas = json.load(open(os.path.join(T, "engagement-mondes.json")))["mondes_sha256"]
    etape("attente du feu 2 (mondes)", "empreintes H, HC et S1 à S20 à inscrire sur main")
    pousser("mondes générés, attente de l'inscription") or arret_A("engagement des mondes non poussé")
    feu = attendre_feu("feu-2-mondes.txt", "mondes", time.time() + DUREES["ATTENTE_FEU_S"],
                       {"fichier_mondes_sha256": ETAT["H"], "certifiees_sha256": ETAT["HC"]})
    inscription_sur_main(feu, [ETAT["H"], ETAT["HC"]] + shas)
    # préparer, essai à blanc (barrière 3)
    etape("preparer")
    if O("preparer", "--arbre", orch, "--mondes", mondes, "--mondes-sha256", ETAT["H"], journal="journal-07-preparer.txt") != 0:
        arret_A("preparer : code non nul (C-16, C-17, textes servis)")
    etape("essai a blanc")
    m, d = int(fiche["files"]), float(fiche["duree_d_s"])
    lent = "3:astra" if m == 1 else "3:astra,4:opus55"
    c = O("jouer", "--arbre", orch, "--mode", "a_blanc", "--mondes", mondes, "--mondes-sha256", ETAT["H"], "--certifiees",
          os.path.join(PV, "CERTIFIEES.json"), "--certifiees-sha256", ETAT["HC"], "--files", str(m), "--sortie", os.path.join(T, "blanc"),
          "--lent", lent, "--borne-essai-s", str(DUREES["BORNE_ESSAI_S"]), *(["--decalage-ports", str(DECALAGE)] if DECALAGE else []),
          journal="journal-08-blanc.txt")
    rel = os.path.join(T, "blanc", "releve-crible-v-v1.json")
    lu = json.load(open(rel)) if os.path.isfile(rel) else {}
    if c != 0 or lu.get("mode") != "a_blanc" or lu.get("arret") is not None or lu.get("coupures") != len(lent.split(",")) \
            or lu.get("comptes") != {"complet": 80 - len(lent.split(",")), "tronque": 0, "echec": len(lent.split(","))}:
        arret_A(f"essai à blanc : code {c} ou sortie différente de l'attendu (80 appels, {len(lent.split(','))} coupure(s) à B_a simulée(s))")
    if not rapatrier(os.path.join(T, "blanc"), os.path.join(T, "rapatrie-blanc")):
        arret_A("rapatriement à blanc : un monde porté")
    etape("attente du feu 3 (crible reel)", f"essai à blanc conforme (M = {m}, {len(lent.split(','))} coupure(s) simulée(s))")
    pousser("essai à blanc conforme, attente du feu réel") or arret_A("essai à blanc non poussé")
    feu = attendre_feu("feu-3-reel.txt", "reel", time.time() + DUREES["ATTENTE_FEU_S"],
                       {"fichier_mondes_sha256": ETAT["H"], "go_kv1": GO_KV1, "go_kv2": GO_KV2, "files": str(m)})
    if float(feu.get("duree_d_s", "nan")) != d:
        arret_A("feu réel : D ≠ celle de la fiche de lancement")
    inscription_sur_main(feu, [f"D = {feu['duree_d_s']} s", f"M = {m}"])
    g("-C", D, "fetch", "-q", "--depth=1", "origin", "+refs/heads/main:refs/remotes/origin/main")
    r = g("-C", D, "show", "refs/remotes/origin/main:registres/go.md")
    if r.returncode != 0:
        arret_A("registre des GO illisible sur main")
    open(os.path.join(T, "go-main.md"), "wb").write(r.stdout)
    reel_a_blanc = REP and E_.get("REPETITION_REEL_A_BLANC") == "1"
    # sonde neuve du chemin des relais du crible (payante), puis le crible réel
    etape("sonde reelle")
    pousser("feu réel conforme : sonde neuve")
    if not reel_a_blanc:
        c = O("sonde", "--arbre", orch, "--mode", "reel", "--go-kv1", GO_KV1, "--go-kv2", GO_KV2, "--registre-go",
              os.path.join(T, "go-main.md"), "--registre-lancements", os.path.join(T, "lancements-sonde.jsonl"), "--sortie",
              os.path.join(T, "sonde"), journal="journal-09-sonde.txt", cles=True)
        if c != 0:
            arret_A(f"sonde neuve : code {c} : aucun appel du crible")
    if ports_libres() is not None:
        arret_A(f"un port des relais est occupé ({ports_libres()})")
    if not all(CLES.values()):
        arret_A("clé absente juste avant")
    ETAT["reel"] = "reel"
    etape("jouer reel en cours")
    args = ["jouer", "--arbre", orch, "--mondes", mondes, "--mondes-sha256", ETAT["H"], "--certifiees",
            os.path.join(PV, "CERTIFIEES.json"), "--certifiees-sha256", ETAT["HC"], "--files", str(m), "--sortie", os.path.join(T, "reel")]
    if reel_a_blanc:
        args += ["--mode", "a_blanc"] + (["--lent", E_["REPETITION_LENT"], "--borne-essai-s", "600"] if E_.get("REPETITION_LENT") else []) \
            + (["--decalage-ports", str(DECALAGE)] if DECALAGE else [])
    else:
        args += ["--mode", "reel", "--go-kv1", GO_KV1, "--go-kv2", GO_KV2, "--registre-go", os.path.join(T, "go-main.md"), "--texte", texte,
                 "--texte-sha256", fiche["texte"]["sha256"], "--mondes-shas", ",".join(shas), "--registre-lancements",
                 os.path.join(T, "lancements.jsonl"), "--releve-sonde", os.path.join(T, "sonde", "releve-sonde-crible-v-v1.json"),
                 "--addendum", addendum, "--addendum-sha256", fiche["addendum"]["sha256"], "--echeance-utc-s", str(ECHEANCE),
                 "--duree-d-s", feu["duree_d_s"]]
    p = O(*args, journal="journal-10-reel.txt", cles=not reel_a_blanc, attendre=False)
    j(f"jouer réel lancé (PID {p.pid})")
    pousser("jouer réel lancé")
    dernier = time.time()
    while p.poll() is None:
        time.sleep(DUREES["PAS_ENTREE_S"])
        if p.poll() is not None:
            break
        a, fa = arret_demande()
        if a:
            j(f"feu d'arrêt de la mère pendant jouer : arrêt du lanceur par son PID {p.pid} (R10)")
            p.terminate()
            p.wait()
            try:
                tuer_par_pid(json.load(open(os.path.join(T, "reel", "pids-relais.json"))), "relais du crible")
            except (OSError, ValueError):
                j("PID des relais illisibles : la session détruit sans tarder")
            arret_A(f"feu d'arrêt de la mère pendant jouer ({fa.get('cause')})")
        if time.time() - dernier >= DUREES["PAS_ETAT_S"]:
            ETAT["motif"] = f"jouer en cours depuis {int(time.time() - dernier)} s"
            pousser("jouer en cours")
            dernier = time.time()
    c = p.wait()
    ETAT["code_jouer"] = str(c)
    open(os.path.join(T, "code-10-reel.txt"), "w").write(f"{c}\n")
    for n in list(CLES):
        CLES[n] = CLES[n]  # gardées pour le balayage jusqu'à la dernière poussée réussie, transmises à aucun processus désormais
    man_f = os.path.join(T, "reel", "manifeste-crible-v-v1.json")
    man = json.load(open(man_f)) if os.path.isfile(man_f) else {}
    if c == 3 and man.get("arret_classe") == "fournisseur_abandonne":
        j("jouer réel : arrêt par la règle d'abandon d'un fournisseur (« non concluant ») : mesure jouée pour les comptes")
    elif c != 0:
        arret_A(f"jouer réel : code {c} ({str(man.get('arret'))[:200]}) : ni mesure, ni lecture")
    # mesure (une seule fois), lecture non ouverte
    etape("mesure")
    c = O("mesurer", "--arbre", orch, "--sortie", os.path.join(T, "reel"), "--mondes", mondes, "--mondes-sha256", ETAT["H"],
          "--certifiees", os.path.join(PV, "CERTIFIEES.json"), "--certifiees-sha256", ETAT["HC"], "--texte-sha256",
          fiche["texte"]["sha256"], journal="journal-12-mesure.txt")
    ETAT["code_mesurer"] = str(c)
    if c != 0:
        noeud_garde(f"mesure : code {c} (exception de la mesure : rien n'est lu ; correction sous un nom neuf, mêmes entrées)")
    os.makedirs(os.path.join(T, "remis-au-sous-agent"), exist_ok=True)
    c = O("lire", "--sortie", os.path.join(T, "reel"), "--ecrire", os.path.join(T, "reel", "lecture-crible-v-v1.json"),
          journal="journal-13-lire.txt")
    shutil.move(os.path.join(T, "journal-13-lire.txt"), os.path.join(T, "remis-au-sous-agent", "sortie-lire-non-ouverte.txt"))
    if c != 0:
        noeud_garde(f"lecture : code {c}")
    etape("rapatriement")
    if not rapatrier(os.path.join(T, "reel"), os.path.join(T, "rapatrie-reel")):
        noeud_garde("rapatriement du réel non conforme : rien n'en sort")
    if os.path.isdir(os.path.join(T, "sonde")):
        rapatrier(os.path.join(T, "sonde"), os.path.join(T, "rapatrie-sonde"))
    etape("fini", "mesure scellée, lecture remise non ouverte, rapatriement sans monde")
    pousser("fini")
    attente_finale()


if __name__ == "__main__":
    try:
        principal()
    except SystemExit:
        raise
    except BaseException as e:  # noqa: BLE001 — sortie inattendue : état poussé, attente
        etape("sortie inattendue", f"{type(e).__name__}")
        j(f"SORTIE INATTENDUE : {type(e).__name__} : {str(e)[:300]}")
        pousser("sortie inattendue")
        attente_finale()
