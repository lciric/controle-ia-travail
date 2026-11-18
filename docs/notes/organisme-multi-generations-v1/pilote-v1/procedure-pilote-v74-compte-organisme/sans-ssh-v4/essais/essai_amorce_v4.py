"""Essais à blanc de l'amorce et du programme machine du pilote MR-2 sans ssh — v4 (procédure v14), sur un dossier jetable.
v4 : mère jouée par l'outil de la session v4 (seule l'étiquette change). v3 : amorce et programme machine v2 inchangés, lus dans `../../sans-ssh-v2/` ; mère jouée par l'outil de la session v3 ; étiquette v13.
v2 : pièces du lot lues par `git show` à la branche distante du lot (m12 : le banc ne dépend plus de la branche extraite du dépôt de
travail ; dépôt donné par ESSAI_DEPOT, défaut le dépôt de travail) ; scénario « poussee-finale-reprise » (M4).

Aucun réseau extérieur, aucune clé réelle, aucune dépense : le « dépôt distant » est un dépôt nu local (`file://`, filtres et envois
par empreinte permis) qui porte trois branches synthétiques (lot, prep, main) aux mêmes chemins que le dépôt de travail, avec les
vraies pièces (paquet, sonde, texte scellé, registre des lignes) ; le loueur est une doublure locale (doublure_vast_v1.py) ; la mère
est jouée par ce programme au moyen de l'outil de la session (session_pilote_mr2_v74_v4.sh), sur une copie du dépôt nu ; les clés
sont des valeurs factices. Le lanceur est la doublure (doublure_lanceur_v1.py) sauf dans le scénario « sain-integral », qui joue le
vrai lanceur v74 (mondes générés, C-16, C-17, essai à blanc, mesure, lecture, rapatriement), le seul écart étant le pilote « réel »
joué en mode à blanc (ESSAI_REEL_A_BLANC : le mode réel refuse toute configuration autre que la gelée, donc toute doublure).

Usage : python3 essai_amorce_v4.py DOSSIER_JETABLE SORTIE.json [SCENARIO …]
"""
import base64
import hashlib
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import time

ICI = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(ICI)                                       # sans-ssh-v4 : outil de la session v4
CODE2 = os.path.join(os.path.dirname(CODE), "sans-ssh-v2")       # amorce et programme machine v2, inchangés
W_REEL = os.environ.get("ESSAI_DEPOT", "/home/user/controle-ia-travail")
REF_LOT = "refs/remotes/origin/lot/compte-organisme-v1"
PL = "docs/notes/organisme-multi-generations-v1/pilote-v1"
DC = PL + "/procedure-pilote-v74-compte-organisme/sans-ssh-v2"
FINALES = ("fini", "fini, poussee finale en echec", "arret (A)", "noeud, machine gardee", "sortie inattendue")
CLES_FACTICES = {"GH_TOKEN": "jetonfactice_0123456789abcdefGH", "RR_ANTHROPIC_API_KEY_RIGAUD": "clefactice-anthropic-0123456789AA",
                 "GEMINI_API_KEY": "clefactice-gem-0123456789GGGGGG", "OPENAI_API_KEY": "clefactice-openai-0123456789OOOO"}
PHRASE = "phrase de répétition des essais de l'amorce, jamais la phrase de Lazar\n"


def run(cmd, cwd=None, env=None, ok=(0,), entree=None):
    r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, input=entree)
    if r.returncode not in ok:
        raise RuntimeError(f"{cmd[:4]} : code {r.returncode} : {r.stdout[-400:]} {r.stderr[-400:]}")
    return r


def git(*a, cwd):
    return run(["git", *a], cwd=cwd).stdout.strip()


def port_libre():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class Banc:
    def __init__(self, base):
        self.base = base
        os.makedirs(base)
        self.origine = os.path.join(base, "origine.git")
        run(["git", "init", "-q", "--bare", self.origine])
        for k, v in (("uploadpack.allowFilter", "true"), ("uploadpack.allowAnySHA1InWant", "true")):
            git("config", k, v, cwd=self.origine)
        crochet = os.path.join(self.origine, "hooks", "pre-receive")   # refus d'une branche tant qu'un drapeau existe (scénario M4)
        open(crochet, "w").write('#!/bin/sh\nwhile read a b r; do f="$(pwd)/refus-$(echo "$r" | tr / -)"; '
                                 '[ -e "$f" ] && { echo "refus (essai)"; exit 1; }; done; exit 0\n')
        os.chmod(crochet, 0o755)
        self.url = "file://" + self.origine
        self.commits = {}
        self._branche("lot/compte-organisme-v1", self._fichiers_lot())
        self._branche("prep/pilote-mr2-compte-organisme-v1", {
            PL + "/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md":
                run(["git", "show", "refs/remotes/origin/prep/pilote-mr2-compte-organisme-v1:" + PL +
                     "/preenregistrement-pilote-conditionnelles-v1-candidat6-compte-organisme.md"], cwd=W_REEL).stdout.encode()})
        self._branche("main", {"registres/go.md": run(["git", "show", "refs/remotes/origin/main:registres/go.md"], cwd=W_REEL).stdout.encode()})
        self.session = os.path.join(base, "session")
        run(["git", "clone", "-q", self.url, self.session])
        git("config", "user.name", "mère simulée", cwd=self.session)
        git("config", "user.email", "mere@invalid", cwd=self.session)
        self.sh = hashlib.sha256(open(os.path.join(CODE2, "machine_pilote_mr2_v74_v2.sh"), "rb").read()).hexdigest()
        self.ah = hashlib.sha256(open(os.path.join(CODE2, "machine_pilote_mr2_v74_v2.py"), "rb").read()).hexdigest()

    def _fichiers_lot(self):
        f = {}
        sonde = PL + "/sonde-complete-v74-compte-organisme/sonde-complete-v74"
        rels = [PL + "/procedure-pilote-v74-compte-organisme/arbre-organisme-complet-605e0f6.bundle"]
        rels += git("ls-tree", "-r", "--name-only", REF_LOT, sonde, cwd=W_REEL).splitlines()
        for rel in rels:
            f[rel] = subprocess.run(["git", "show", f"{REF_LOT}:{rel}"], cwd=W_REEL, capture_output=True, check=True).stdout
        for n in ("amorce_pilote_mr2_v74_v2.sh", "machine_pilote_mr2_v74_v2.sh", "machine_pilote_mr2_v74_v2.py"):
            f[DC + "/" + n] = open(os.path.join(CODE2, n), "rb").read()
        return f

    def _branche(self, nom, fichiers):
        d = os.path.join(self.base, "construction-" + nom.replace("/", "-"))
        run(["git", "init", "-q", d])
        for rel, b in fichiers.items():
            os.makedirs(os.path.dirname(os.path.join(d, rel)), exist_ok=True)
            open(os.path.join(d, rel), "wb").write(b)
        git("add", "-A", cwd=d)
        run(["git", "-c", "user.name=banc", "-c", "user.email=banc@invalid", "commit", "-q", "-m", nom], cwd=d)
        git("push", "-q", self.url, "HEAD:refs/heads/" + nom, cwd=d)
        self.commits[nom] = git("rev-parse", "HEAD", cwd=d)
        shutil.rmtree(d)

    def outil(self, *a, ok=(0,)):
        env = dict(os.environ, W=self.session, ENVP=os.path.join(self.base, "envoi"))
        return run(["bash", os.path.join(CODE, "session_pilote_mr2_v74_v4.sh"), *a], env=env, ok=ok)

    def inscrire(self, texte):
        """La mère inscrit des empreintes sur main (copie locale du dépôt nu) ; rend le commit et le chemin."""
        git("fetch", "-q", "origin", "+refs/heads/main:refs/remotes/origin/main", cwd=self.session)
        git("checkout", "-q", "-B", "main", "refs/remotes/origin/main", cwd=self.session)
        ch = "registres-essai/inscriptions.md"
        os.makedirs(os.path.join(self.session, "registres-essai"), exist_ok=True)
        with open(os.path.join(self.session, ch), "a") as f:
            f.write(texte + "\n")
        git("add", ch, cwd=self.session)
        git("commit", "-q", "-m", "inscription (essai)", cwd=self.session)
        git("push", "-q", "origin", "main", cwd=self.session)
        return git("rev-parse", "HEAD", cwd=self.session), ch

    def sortie(self, br, fichier):
        r = run(["git", "fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}"], cwd=self.session, ok=(0, 1, 128))
        if r.returncode:
            return None
        r = run(["git", "show", f"refs/remotes/origin/{br}:{fichier}"], cwd=self.session, ok=(0, 128))
        return r.stdout if r.returncode == 0 else None

    def fichiers_sortie(self, br):
        r = run(["git", "fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}"], cwd=self.session, ok=(0, 1, 128))
        if r.returncode:
            return []
        return git("ls-tree", "-r", "--name-only", f"refs/remotes/origin/{br}", cwd=self.session).splitlines()

    def octets_sortie(self, br):
        """Toute la branche de sortie, tous ses commits (pas seulement le sommet), en octets."""
        r = run(["git", "log", "-p", "--binary", "--format=%H", f"refs/remotes/origin/{br}"], cwd=self.session, ok=(0, 128))
        return r.stdout.encode() if r.returncode == 0 else b""


def ecrire_feu_brut(banc, br, nom, chemin):
    """Feu écrit sans l'outil (feux faux des essais) : même forme de commit que l'outil (sommet gardé, fichier remplacé)."""
    s = banc.session
    r = run(["git", "ls-remote", "origin", "refs/heads/" + br], cwd=s).stdout.split()
    tip, lignes = (r[0] if r else None), []
    if tip:
        git("fetch", "-q", "origin", f"+refs/heads/{br}:refs/remotes/origin/{br}", cwd=s)
        lignes = [l for l in git("ls-tree", tip, cwd=s).splitlines() if l.split("\t")[1] != nom]
    lignes.append(f"100644 blob {git('hash-object', '-w', chemin, cwd=s)}\t{nom}")
    arbre = run(["git", "mktree"], cwd=s, entree="\n".join(lignes) + "\n").stdout.strip()
    c = git("commit-tree", arbre, *(["-p", tip] if tip else []), "-m", "feu faux (essai)", cwd=s)
    git("push", "-q", "origin", f"{c}:refs/heads/{br}", cwd=s)


def etape(banc, br):
    t = banc.sortie(br, "etat.txt")
    if t is None:
        return None, ""
    d = dict(l.split("=", 1) for l in t.splitlines() if "=" in l)
    return d.get("etape"), d.get("motif", "")


def jouer(banc, nom, sc):
    """Un scénario : amorce lancée comme le ferait le loueur ; mère jouée selon sc ; rend le constat."""
    racine = os.path.join(banc.base, "racine-" + nom)
    os.makedirs(racine)
    br_s, br_e = f"calcul/essai-{nom}-sortie", f"calcul/essai-{nom}-entree"
    pv = port_libre()
    jv = os.path.join(banc.base, f"vast-{nom}.jsonl")
    open(jv, "w").close()
    pvast = subprocess.Popen([sys.executable, os.path.join(ICI, "doublure_vast_v1.py"), str(pv), jv])
    time.sleep(0.5)
    if sc.get("doublure", True):
        dl = os.path.join(banc.base, "lanceur-" + nom)
        os.makedirs(dl)
        shutil.copy(os.path.join(ICI, "doublure_lanceur_v1.py"), dl)
        json.dump(sc.get("scenario", {}), open(os.path.join(dl, "scenario.json"), "w"))
    env = {"PATH": "/usr/local/bin:/usr/bin:/bin", "HOME": os.path.join(banc.base, "home-" + nom), "AMORCE_ESSAI": "1",
           "RACINE_AMORCE": racine, "DEPOT_URL_ESSAI": banc.url, "API_VAST_ESSAI": f"http://127.0.0.1:{pv}", "ATTENTE_REFUS_S": "0",
           "PAS_MINUTERIE_S": "1", "COMMIT_LOT": banc.commits["lot/compte-organisme-v1"],
           "COMMIT_PREP": banc.commits["prep/pilote-mr2-compte-organisme-v1"], "COMMIT_MAIN": banc.commits["main"],
           "BR_SORTIE": br_s, "BR_ENTREE": br_e, "ECHEANCE_UTC_S": str(int(time.time()) + sc.get("echeance_s", 50000)),
           "GO_ID": sc.get("go_id", "GO-2026-11-14-14"), "SCRIPT_SHA256": banc.sh, "AIDE_SHA256": banc.ah, "CONTAINER_ID": "4242",
           "CONTAINER_API_KEY": "clefactice-loueur-000", "ESSAI_SANS_PIP": "1", "ESSAI_SANS_TLS": "1", "PAS_ENTREE_S": "1",
           "PAS_ETAT_S": "5", "PAS_REPRISE_S": "5", "ATTENTE_PHRASE_S": str(sc.get("attente_phrase_s", 120)), "ATTENTE_FEU_S": str(sc.get("attente_feu_s", 120)),
           "BUDGET_REEL_S": str(sc.get("budget_reel_s", 60)), **CLES_FACTICES}
    os.makedirs(env["HOME"])
    if sc.get("doublure", True):
        env["ESSAI_LANCEUR"] = os.path.join(banc.base, "lanceur-" + nom, "doublure_lanceur_v1.py")
    if sc.get("reel_a_blanc"):
        env["ESSAI_REEL_A_BLANC"] = "1"
    for b in sc.get("branches_presentes", []):
        d = os.path.join(banc.base, "pre-" + nom)
        run(["git", "init", "-q", d]); open(os.path.join(d, "ancien.txt"), "w").write("ancien\n")
        git("add", "-A", cwd=d); run(["git", "-c", "user.name=b", "-c", "user.email=b@i", "commit", "-q", "-m", "ancien"], cwd=d)
        git("push", "-q", banc.url, "HEAD:refs/heads/" + {"sortie": br_s, "entree": br_e}[b], cwd=d)
    journal = open(os.path.join(banc.base, f"amorce-{nom}.txt"), "w")

    def lancer():
        return subprocess.Popen(["bash", os.path.join(CODE2, "amorce_pilote_mr2_v74_v2.sh")], env=env, stdout=journal,
                                stderr=subprocess.STDOUT, start_new_session=True)

    p = lancer()
    try:
        return suivre(banc, nom, sc, env, lancer, p, br_s, br_e, racine, jv, pvast, journal)
    finally:  # aussi sur une exception du banc : amorces (groupes créés ici, par leur identifiant) et doublure arrêtées
        for q in (p, sc.get("_p")):
            if q is not None:
                try:
                    os.killpg(q.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
        pvast.terminate()


def suivre(banc, nom, sc, env, lancer, p, br_s, br_e, racine, jv, pvast, journal):
    faits, actions, t0, fin = set(), [], time.time(), None
    limite = sc.get("limite_s", 300)
    while time.time() - t0 < limite:
        time.sleep(2)
        if p.poll() is not None and sc.get("amorce_sort"):
            fin = ("sortie de l'amorce", p.returncode)
            break
        e, m = etape(banc, br_s)
        if e in FINALES:
            fin = (e, m)
            break
        if sc.get("tuer_a") and e == sc["tuer_a"] and "relance" not in faits:
            os.killpg(p.pid, signal.SIGKILL); p.wait()   # relance du conteneur : arrêt par l'identifiant du groupe créé ici
            faits.add("relance"); actions.append("conteneur relancé")
            p = lancer()
            sc["_p"] = p
            continue
        if sc.get("refus_poussee_a") and e == sc["refus_poussee_a"] and "rp" not in faits:
            faits.add("rp"); drapeau = os.path.join(banc.origine, "refus-refs-heads-" + br_s.replace("/", "-")); open(drapeau, "w").close()
            t_rp = time.time(); actions.append("poussées de la machine refusées par le dépôt distant")
        if "rp" in faits and "rp-fin" not in faits and time.time() - t_rp > sc.get("refus_duree_s", 30):
            faits.add("rp-fin"); os.unlink(drapeau); actions.append("poussées de nouveau acceptées")
        if e == "attente du feu 1 (phrase)" and "f1" not in faits:
            faits.add("f1")
            ss = banc.sortie(br_s, "secret-sha256.txt").strip().split("=", 1)[1]
            fp = os.path.join(banc.base, f"phrase-{nom}.txt")
            open(fp, "w", encoding="utf-8").write(PHRASE)
            if sc.get("feu1") == "faux-secret":
                c, ch = banc.inscrire(ss)
                faux = os.path.join(banc.base, f"feu1-{nom}.txt")
                open(faux, "w").write(f"feu=phrase\nsecret_sha256={'0' * 64}\nphrase_fichier_sha256={'1' * 64}\ninscription_commit={c}\ninscription_chemin={ch}\n")
                ecrire_feu_brut(banc, br_e, "feu-1-phrase.txt", faux)
                actions.append("feu 1 au secret faux")
            elif sc.get("feu1") == "phrase-alteree":
                c, ch = banc.inscrire(ss)
                r = banc.outil("feu-phrase", br_s, br_e, fp, c, ch)
                actions.append("feu 1 poussé : " + r.stdout.strip().splitlines()[-1])
                faux = os.path.join(banc.base, f"feu1-{nom}.txt")
                open(faux, "w").write(f"feu=phrase\nsecret_sha256={ss}\nphrase_fichier_sha256={'2' * 64}\ninscription_commit={c}\ninscription_chemin={ch}\n")
                ecrire_feu_brut(banc, br_e, "feu-1-phrase.txt", faux)
                actions.append("feu 1 récrit avec une empreinte de phrase fausse")
            elif sc.get("feu1") != "aucun":
                r = banc.outil("feu-phrase", br_s, br_e, fp, *banc.inscrire(ss))
                actions.append("feu 1 : " + r.stdout.strip().splitlines()[-1])
                assert not os.path.exists(fp), "fichier de la phrase non effacé par l'outil"
        if e == "attente du feu 2 (mondes)" and "f2" not in faits:
            faits.add("f2")
            eg = json.loads(banc.sortie(br_s, "engagement-mondes.json"))
            r = banc.outil("feu-mondes", br_s, br_e, *banc.inscrire(" ".join([eg["fichier_mondes_sha256"], *eg["mondes_sha256"]])))
            actions.append("feu 2 : " + r.stdout.strip().splitlines()[-1])
        if e == "attente du feu 3 (pilote reel)" and "f3" not in faits and not sc.get("pas_de_feu3"):
            faits.add("f3")
            r = banc.outil("feu-reel", br_s, br_e)
            actions.append("feu 3 : " + r.stdout.strip().splitlines()[-1])
        if e and e.startswith("jouer reel en cours") and sc.get("arret_pendant_jouer") and "fa" not in faits:
            faits.add("fa")
            r = banc.outil("feu-arret", br_e, "essai : arret pendant jouer")
            actions.append("feu d'arrêt : " + r.stdout.strip().splitlines()[-1])
        if e == "attente du feu de relance (reel-2)" and "fr" not in faits:
            faits.add("fr")
            r = banc.outil("feu-relance", br_s, br_e, "essai : relance")
            actions.append("feu de relance : " + r.stdout.strip().splitlines()[-1])
    time.sleep(sc.get("apres_s", 1))
    try:
        os.killpg(p.pid, signal.SIGKILL)   # fin de l'essai : arrêt par l'identifiant du groupe de processus créé ici (R10)
    except ProcessLookupError:
        pass
    p.wait()
    pvast.terminate(); pvast.wait()
    journal.close()
    fichiers = banc.fichiers_sortie(br_s)
    tout = banc.octets_sortie(br_s)
    secret_b = open(os.path.join(racine, "pilote/prive/secret.bin"), "rb").read() if os.path.exists(os.path.join(racine, "pilote/prive/secret.bin")) else None
    fuites = [k for k, v in CLES_FACTICES.items() if v.encode() in tout or base64.b64encode(v.encode()).rstrip(b"=") in tout]
    if secret_b and (secret_b.hex().encode() in tout or secret_b in tout):
        fuites.append("secret")
    if PHRASE.strip().encode() in tout:
        fuites.append("phrase")
    interdits = [f for f in fichiers if any(x in f for x in ("secret.bin", "phrase.txt", "MONDES.json", "cle-phrase.pem", "/prive/", "texte-servi"))
                 and not f.startswith("phrase-sha256") and not f.startswith("engagement-mondes")]
    vast = [json.loads(l) for l in open(jv) if l.strip()]
    log = open(os.path.join(banc.base, f"amorce-{nom}.txt")).read()
    return {"fin": fin, "etat_final": banc.sortie(br_s, "etat.txt") or "", "actions": actions, "fichiers_sortie": len(fichiers), "fuites": fuites, "interdits": interdits,
            "vast": [(v["methode"], v["chemin"], v["autorisation"]) for v in vast], "duree_s": round(time.time() - t0),
            "fichiers": fichiers, "log_fin": log.splitlines()[-6:], "log": log}


SCENARIOS = {
    "sain": ({}, lambda r: r["fin"][0] == "fini" and not r["vast"]
             and {"rapatrie-reel/lecture-pilote-v70.json", "remis-au-sous-agent/sortie-lire-non-ouverte.txt", "rapatrie-blanc/CARTES.json",
                  "phrase-sha256.txt", "engagement-mondes.json", "cle-publique-phrase.pem", "journal-09-reel.txt", "code-10-mesurer.txt"} <= set(r["fichiers"])),
    "refus-arguments": ({"go_id": "GO-2026-11-14-13", "amorce_sort": True, "limite_s": 30},
                        lambda r: r["fin"] == ("sortie de l'amorce", 2) and [m for m, _, _ in r["vast"]] == ["DELETE"] * 3 + ["PUT"]
                        and all(a for _, _, a in r["vast"]) and r["fichiers_sortie"] == 0),
    "sortie-presente": ({"branches_presentes": ["sortie"], "limite_s": 30},
                        lambda r: r["fin"] is None and "présente (R12)" in r["log"] and r["fichiers"] == ["ancien.txt"]),
    "entree-presente": ({"branches_presentes": ["entree"]}, lambda r: r["fin"][0] == "arret (A)" and "déjà présente" in r["fin"][1]),
    "feu1-faux": ({"feu1": "faux-secret", "attente_phrase_s": 45},
                  lambda r: r["fin"][0] == "arret (A)" and "aucun feu phrase conforme" in r["fin"][1] and "feu phrase refusé" in r["log"]),
    "phrase-alteree": ({"feu1": "phrase-alteree", "attente_phrase_s": 90},
                       lambda r: r["fin"][0] == "arret (A)" and ("empreinte du fichier" in r["fin"][1] or "aucun feu" in r["fin"][1])),
    "relance-ok": ({"scenario": {"jouer_reel": [2, 0]}},
                   lambda r: r["fin"][0] == "fini" and "journal-09-reel-essai1.txt" in r["fichiers"] and "journal-09-reel-2.txt" in r["fichiers"]
                   and "rapatrie-reel/CARTES.json" in r["fichiers"]),
    "relance-deux-fois": ({"scenario": {"jouer_reel": [2, 2]}}, lambda r: r["fin"][0] == "arret (A)" and "second code 2" in r["fin"][1]),
    "code3": ({"scenario": {"jouer_reel": [3]}},
              lambda r: r["fin"][0] == "arret (A)" and "code 3" in r["fin"][1] and "rapatrie-reel/CARTES-partiel.json" in r["fichiers"]
              and "code-10-mesurer.txt" not in r["fichiers"]),
    "arret-pendant-jouer": ({"scenario": {"duree_jouer_s": 120}, "arret_pendant_jouer": True},
                            lambda r: r["fin"][0] == "arret (A)" and "feu d'arrêt" in r["fin"][1] and "arret pendant jouer" in r["fin"][1] and "code-09-reel.txt" in r["fichiers"]),
    "fuite-cle": ({"scenario": {"fuite_cle": True}},
                  lambda r: r["fin"][0] == "fini" and "BALAYAGE : forme secrète trouvée" in r["log"] and not r["fuites"]
                  and "rapatrie-reel/journal-relais-opus55.jsonl" not in r["fichiers"] and "rapatrie-reel/CARTES.json" in r["fichiers"]
                  and "rapatrie-reel/journal-relais-opus55.jsonl" in r["etat_final"]),
    "minuterie": ({"echeance_s": 12, "feu1": "aucun", "attente_phrase_s": 600, "limite_s": 40, "apres_s": 0},
                  lambda r: [m for m, _, _ in r["vast"]][:1] == ["DELETE"] and "MINUTERIE : échéance atteinte" in r["log"]),
    "budget": ({"budget_reel_s": 10 ** 9}, lambda r: r["fin"][0] == "arret (A)" and "avant l'échéance" in r["fin"][1]
               and "lancements.jsonl" not in r["fichiers"]),
    "comptes-faux": ({"scenario": {"jouer_reel_comptes": {"complet": 10, "echec": 0, "tronque": 0}}},
                     lambda r: r["fin"][0] == "noeud, machine gardee" and "16 appels" in r["fin"][1]),
    "mesure-code2": ({"scenario": {"mesurer_code": 2}}, lambda r: r["fin"][0] == "noeud, machine gardee" and "mesurer : code 2" in r["fin"][1]),
    "relance-conteneur": ({"tuer_a": "attente du feu 3 (pilote reel)", "pas_de_feu3": True},
                          lambda r: r["fin"][0] == "arret (A)" and "relance du conteneur" in r["fin"][1] and "journal-09-reel.txt" not in r["fichiers"]),
    "poussee-finale-reprise": ({"refus_poussee_a": "jouer reel en cours", "refus_duree_s": 240, "limite_s": 420, "scenario": {"duree_jouer_s": 5}},
                               lambda r: r["fin"][0] == "fini" and "dernière poussée en échec : reprise" in r["log"]
                               and "rapatrie-reel/lecture-pilote-v70.json" in r["fichiers"]),
    "sain-integral": ({"doublure": False, "reel_a_blanc": True, "limite_s": 2400},
                      lambda r: r["fin"][0] == "fini" and not r["fuites"] and not r["interdits"]
                      and {"rapatrie-reel/lecture-pilote-v70.json", "rapatrie-reel/sortie-mesure-pilote-v70.json", "rapatrie-blanc/CARTES.json"} <= set(r["fichiers"])),
}


def main(argv):
    base, sortie, noms = argv[0], argv[1], argv[2:] or [n for n in SCENARIOS if n != "sain-integral"]
    banc = Banc(base)
    res = {"commits": banc.commits, "programme_sha256": banc.sh, "aide_sha256": banc.ah,
           "amorce_sha256": hashlib.sha256(open(os.path.join(CODE2, "amorce_pilote_mr2_v74_v2.sh"), "rb").read()).hexdigest(),
           "outil_session_sha256": hashlib.sha256(open(os.path.join(CODE, "session_pilote_mr2_v74_v4.sh"), "rb").read()).hexdigest(),
           "scenarios": {}}
    for n in noms:
        sc, attendu = SCENARIOS[n]
        try:
            r = jouer(banc, n, sc)
            ok = bool(attendu(r)) and not r["fuites"] and not r["interdits"]
        except Exception as e:  # noqa: BLE001
            r, ok = {"exception": f"{type(e).__name__} : {e}"}, False
        r.pop("log", None)
        r["conforme"] = ok
        res["scenarios"][n] = r
        print(f"{n:22s} {'CONFORME' if ok else 'ÉCART'} {r.get('fin')} {r.get('duree_s')} s", flush=True)
    res["tout_conforme"] = all(v["conforme"] for v in res["scenarios"].values())
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1, sort_keys=True)
    return 0 if res["tout_conforme"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
