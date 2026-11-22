import os, subprocess, sys, time, signal, hashlib

W = "/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-controle-sortie-v2"
P = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/"
V1 = P + "auteur-controle-sortie-v1/controler-et-creer-essai-3-v1.py"
V2 = P + "auteur-controle-sortie-v2/controler-et-creer-essai-3-v2.py"
PY = "/home/user/controle-ia-travail/.venv/bin/python"
TOK = "FAUXTOKENR1abcdefghijklmnop12345"
BEAR = hashlib.sha256(("Bearer " + TOK).encode()).hexdigest()[:12]
D = W + "/donnees/sain.txt"
J = W + "/tables/journal-serveur.txt"
PRET = W + "/pret"
ARRET = W + "/arret"
R = W + "/releves/"
os.makedirs(R, exist_ok=True)
for f in (J, PRET, ARRET):
    if os.path.exists(f):
        os.remove(f)
srv = subprocess.Popen([PY, "-I", W + "/outils/serveur.py", J, PRET, ARRET])
t = time.time()
while not os.path.exists(PRET) and time.time() - t < 10:
    time.sleep(0.05)
port = open(PRET).read().strip()
env = {k: v for k, v in os.environ.items() if k != "HCLOUD_TOKEN"}
env["PATH"] = "/usr/bin:/bin"
env["CONTROLE_BANC"] = "oui"
env["FAUXJ"] = TOK
out = []


def nlig():
    return len(open(J).read().splitlines()) if os.path.exists(J) else 0


def jouer(script, route, tag):
    rel = R + "r1-%s.txt" % tag
    if os.path.exists(rel):
        os.remove(rel)
    n0 = nlig()
    p = subprocess.run([PY, "-I", script, D, rel, "--envoyer", "--adresse", "http://127.0.0.1:%s/%s" % (port, route),
                        "--nom-jeton", "FAUXJ"], env=env, capture_output=True, text=True)
    lines = open(J).read().splitlines()[n0:]
    return p.returncode, lines, p.stdout + p.stderr


try:
    for code in (301, 302, 303, 307, 308):
        for nom, sc in (("v1", V1), ("v2", V2)):
            rc, l, _ = jouer(sc, "r%d" % code, "%d-%s" % (code, nom))
            routes = [x.split()[1] for x in l]
            s = "redir %d %s : code sortie %d ; requetes recues %d %s ; jeton vu sur : %s" % (
                code, nom, rc, len(l), routes, [x.split()[1] for x in l if BEAR in x])
            print(s); out.append(s)
    # cas sain 201 : corps v1 = v2
    shas = {}
    for nom, sc in (("v1", V1), ("v2", V2)):
        rc, l, so = jouer(sc, "ok", "ok-%s" % nom)
        shas[nom] = l[0].split("sha=")[1].split()[0] if l else None
        s = "sain 201 %s : code %d ; requetes %d ; sha corps %s" % (nom, rc, len(l), shas[nom])
        print(s); out.append(s)
    s = "corps v1 == corps v2 : %s" % (shas["v1"] == shas["v2"] and shas["v1"] is not None)
    print(s); out.append(s)
    # ps pendant une réponse lente
    for nom, sc in (("v2", V2),):
        rel = R + "r1-lent-%s.txt" % nom
        if os.path.exists(rel):
            os.remove(rel)
        p = subprocess.Popen([PY, "-I", sc, D, rel, "--envoyer", "--adresse", "http://127.0.0.1:%s/lent" % port,
                              "--nom-jeton", "FAUXJ"], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(1.0)
        ps = subprocess.run(["/usr/bin/ps", "-eo", "args"], capture_output=True, text=True).stdout
        pse = subprocess.run(["/usr/bin/ps", "-eo", "pid,args"], capture_output=True, text=True).stdout
        so, se = p.communicate()
        s = "ps pendant l'envoi : jeton present dans ps = %s ; code %d" % (TOK in ps, p.returncode)
        print(s); out.append(s)
        s = "jeton dans stdout/stderr : %s %s" % (TOK in so, TOK in se)
        print(s); out.append(s)
        txt = open(rel).read()
        s = "jeton dans releve : %s ; MDPFACTICE : %s ; ECHO : %s ; releve:\n%s" % (TOK in txt, "MDPFACTICE" in txt, "ECHO" in txt, txt[-600:])
        print(s); out.append(s)
finally:
    open(ARRET, "w").close()
    srv.wait(timeout=10)
open(W + "/tables/r1-cas.txt", "w").write("\n".join(out) + "\n")
