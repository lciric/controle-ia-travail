"""Banc de la vérification du contrôle de sortie v1. Emploi : /home/user/controle-ia-travail/.venv/bin/python -I banc-verif.py
Tout se passe dans le dossier de travail ; environnement des sous-processus construit à neuf (aucune variable héritée,
donc jamais HCLOUD_TOKEN réel) ; jetons factices tirés au hasard à chaque lancement."""
import base64
import gzip
import hashlib
import io
import json
import os
import secrets
import subprocess
import sys
import tarfile
import time

W = "/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-controle-sortie-v1"
P = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1"
TOOL = P + "/auteur-controle-sortie-v1/controler-et-creer-essai-3-v1.py"
FAB = P + "/auteur-fabricant-v8-amorce-epinglee/fabriquer-donnees-demarrage-v8.sh"
GUET = P + "/auteur-fabricant-v8-amorce-epinglee/essais-outils/guetteur-ps.sh"
PY = "/home/user/controle-ia-travail/.venv/bin/python"
T = W + "/travail"
SRV = T + "/serveur"
BASE = {"PATH": "/usr/bin:/bin", "HOME": T}
E_REDUIT = "061f79930face6fc7945c30fb5dbb6275563495b0ea0fe132ba82f1457137ce5"

T_API = "API" + secrets.token_hex(20)
T_DEM = "DEM" + secrets.token_hex(20)
LIGNES = []   # (cas, attendu, rendu, fichier, verdict)
SORTIES = []  # toutes les sorties texte, pour la recherche des jetons


def sha(b):
    return hashlib.sha256(b).hexdigest()


def run(cmd, env=None, timeout=200):
    r = subprocess.run(cmd, env=env if env is not None else BASE, capture_output=True, timeout=timeout)
    SORTIES.append(r.stdout + r.stderr)
    return r


def journal():
    try:
        with open(SRV + "/journal.txt") as f:
            return f.read().splitlines()
    except OSError:
        return []


def noter(cas, attendu, rendu, fichier, ok):
    LIGNES.append((cas, attendu, rendu, fichier, "OK" if ok else "ECART"))
    print("%-5s %-58s attendu=%s rendu=%s" % ("OK" if ok else "ECART", cas, attendu, rendu))


compteur = [0]


def outil(donnees, opts=(), env_plus=None, mode="--envoyer", banc=True, port=None, relev=None, adresse=True):
    compteur[0] += 1
    rel = relev or (T + "/rel/r%04d.txt" % compteur[0])
    env = dict(BASE)
    if banc:
        env["CONTROLE_BANC"] = "oui"
    env["JETON_API"] = T_API
    if env_plus:
        env.update(env_plus)
    cmd = [PY, "-I", TOOL, donnees, rel, mode]
    if mode == "--envoyer" and banc and adresse:
        cmd += ["--adresse", "http://127.0.0.1:%d/v1/servers" % PORT, "--nom-jeton", "JETON_API"]
    cmd += list(opts)
    n0 = len(journal())
    r = run(cmd, env)
    n1 = len(journal())
    texte = ""
    if os.path.exists(rel):
        with open(rel) as f:
            texte = f.read()
    return r.returncode, n1 - n0, rel, texte, r


# ----------------------------------------------------------------- préparation
for d in (T + "/rel", T + "/cas", T + "/serveur", T + "/depot"):
    os.makedirs(d, exist_ok=True)
subprocess.run(["/usr/bin/git", "init", "-q", "--bare", T + "/depot/vide.git"], env=BASE, check=True)
with open(T + "/jetons.txt", "w") as f:
    os.chmod(T + "/jetons.txt", 0o600)
    f.write(T_API + "\n" + T_DEM + "\n")
env_f = dict(BASE, FABRICANT_BANC="oui", FABRICANT_DEPOT_DISTANT=T + "/depot/vide.git", JETON_DEM=T_DEM)
SAIN = T + "/cas/sain.bin"
r = run(["/bin/bash", FAB, "JETON_DEM", SAIN], env_f)
if r.returncode != 0 or not os.path.exists(SAIN):
    print("fabricant en échec", r.returncode, r.stderr[:300])
    sys.exit(9)
S = open(SAIN, "rb").read()
print("données saines : %d octets sha256 %s" % (len(S), sha(S)))

# guetteur ps
stop_g = T + "/guet.arret"
g = subprocess.Popen(["/bin/bash", GUET, T + "/jetons.txt", T + "/guet.sortie", stop_g], env=BASE)
# serveur
sv = subprocess.Popen([PY, "-I", W + "/outils/serveur-verif.py", SRV], env=BASE)
for _ in range(200):
    if os.path.exists(SRV + "/pret"):
        break
    time.sleep(0.05)
PORT = int(open(SRV + "/pret").read())

# ----------------------------------------------------------------- variantes
L = S[:-1].split(b"\n")
m = L.index(b"__CHARGE_DES_PIECES__")
assert m == len(L) - 2 and L[3] == b"E_SCRIPT=" + E_REDUIT.encode()
charge_b64 = L[-1]


def ecrire_cas(nom, lignes=None, brut=None, fin=b"\n"):
    chemin = T + "/cas/%s.bin" % nom
    with open(chemin, "wb") as f:
        f.write(brut if brut is not None else b"\n".join(lignes) + fin)
    return chemin


def inser(i, x):
    return L[:i] + [x] + L[i:]


def remplacer(i, x):
    return L[:i] + [x] + L[i + 1:]


def membres(blob=charge_b64):
    out = []
    with tarfile.open(fileobj=io.BytesIO(base64.b64decode(blob)), mode="r:gz") as tf:
        for mm in tf.getmembers():
            out.append((mm.name, tf.extractfile(mm).read(), mm.mode))
    return out


MEM = membres()
assert len(MEM) == 5


def fabriquer_tar(mems, junk=b"", liens=(), reps=(), double=()):
    bio = io.BytesIO()
    with tarfile.open(fileobj=bio, mode="w", format=tarfile.GNU_FORMAT) as tf:
        for n, c, md in mems:
            ti = tarfile.TarInfo(n)
            ti.size = len(c)
            ti.mode = md
            tf.addfile(ti, io.BytesIO(c))
        for n, cible in liens:
            ti = tarfile.TarInfo(n)
            ti.type = tarfile.SYMTYPE
            ti.linkname = cible
            tf.addfile(ti)
        for n in reps:
            ti = tarfile.TarInfo(n)
            ti.type = tarfile.DIRTYPE
            tf.addfile(ti)
    brut = bio.getvalue() + junk
    return brut


def charge_de(tarbrut, gz=True, junk_gz=b""):
    z = gzip.compress(tarbrut, 9, mtime=0) if gz else tarbrut
    return base64.b64encode(z + junk_gz)


def avec_charge(cb):
    return L[:-1] + [cb]


cas = []  # (nom, fichier, attendu)
cas.append(("T-sain", SAIN, 0))
cas.append(("T-recompression-identique-contenus", ecrire_cas("recompr", avec_charge(charge_de(fabriquer_tar(MEM)))), 0))
# amorce
cas.append(("A-amorce-espace-fin-ligne5", ecrire_cas("a1", remplacer(4, L[4] + b" ")), 12))
cas.append(("A-amorce-dernier-mot-modifie", ecrire_cas("a2", remplacer(m - 1, L[m - 1].replace(b"e", b"E", 1) if b"e" in L[m - 1] else L[m - 1] + b"x")), 12))
cas.append(("A-ligne1-modifiee", ecrire_cas("a3", remplacer(0, L[0] + b" x")), 12))
cas.append(("A-ajout-ligne-en-clair-index4", ecrire_cas("a4", inser(4, b"echo pwn")), 12))
cas.append(("A-ajout-commentaire-index4", ecrire_cas("a5", inser(4, b"# x")), 12))
cas.append(("A-ajout-ligne-avant-marqueur", ecrire_cas("a6", inser(m, b"echo pwn")), 12))
cas.append(("A-ajout-ligne-entre-marqueur-et-charge", ecrire_cas("a7", inser(m + 1, b"echo pwn")), 12))
cas.append(("A-ajout-ligne-apres-charge", ecrire_cas("a8", L + [b"echo pwn"]), 12))
cas.append(("A-ligne-vide-finale-en-trop", ecrire_cas("a9", L, fin=b"\n\n"), 12))
cas.append(("A-ajout-ligne-avant-H0 (decale les numeros)", ecrire_cas("a10", inser(1, b"echo pwn")), 11))
cas.append(("A-suffixe-sur-ligne-H0", ecrire_cas("a11", remplacer(1, L[1] + b"; echo pwn")), 12))
cas.append(("A-suffixe-sur-ligne-jeton", ecrire_cas("a12", remplacer(2, L[2] + b"; echo pwn")), 12))
cas.append(("A-suffixe-sur-ligne-E_SCRIPT", ecrire_cas("a13", remplacer(3, L[3] + b"; echo pwn")), 11))
cas.append(("A-export-E_SCRIPT-dans-amorce", ecrire_cas("a14", inser(10, b"export E_SCRIPT=evil")), 12))
cas.append(("A-tabulation-en-clair-dans-amorce", ecrire_cas("a15", remplacer(4, L[4] + b"\t")), 12))
cas.append(("A-sans-saut-de-ligne-final", ecrire_cas("a16", L, fin=b""), 12))
cas.append(("A-fichier-vide", ecrire_cas("a17", brut=b""), 12))
cas.append(("A-jeton-trop-court", ecrire_cas("a18", remplacer(2, b"JETON_DEMARRAGE='abc'")), 12))
cas.append(("A-H0-date-absurde-mais-bien-forme", ecrire_cas("a19", remplacer(1, b"H0_PREVU=9999-99-99T99:99:99Z")), 0))
# E_SCRIPT
cas.append(("E-deux-E_SCRIPT=-autre-valeur", ecrire_cas("e1", inser(10, b"E_SCRIPT=" + b"0" * 64)), 11))
cas.append(("E-E_SCRIPT+=", ecrire_cas("e2", inser(10, b"E_SCRIPT+=x")), 11))
cas.append(("E-E_SCRIPT=-identique-en-double", ecrire_cas("e3", inser(10, L[3])), 11))
cas.append(("E-E_SCRIPT=-indente", ecrire_cas("e4", inser(10, b"  E_SCRIPT=" + b"0" * 64)), 11))
cas.append(("E-E_SCRIPT-tabulation-indentee", ecrire_cas("e5", inser(10, b"\tE_SCRIPT=x")), 11))
cas.append(("E-valeur-ligne4-modifiee", ecrire_cas("e6", remplacer(3, b"E_SCRIPT=" + b"0" * 64)), 11))
cas.append(("E-ligne4-absente-(supprimee)", ecrire_cas("e7", L[:3] + L[4:]), 11))
cas.append(("E-E_SCRIPT-deplace-ligne5", ecrire_cas("e8", L[:3] + [L[4], L[3]] + L[5:]), 11))
# charge
evil = [(n, c + (b"\necho pwn\n" if n.startswith("demarrage") else b""), md) for n, c, md in MEM]
cas.append(("C-script-modifie-dans-charge", ecrire_cas("c1", avec_charge(charge_de(fabriquer_tar(evil)))), 14))
evil2 = [(n, (c + b"#" if n == "gardien-essai-3-v4.py" else c), md) for n, c, md in MEM]
cas.append(("C-gardien-modifie", ecrire_cas("c2", avec_charge(charge_de(fabriquer_tar(evil2)))), 14))
cas.append(("C-membre-en-trop", ecrire_cas("c3", avec_charge(charge_de(fabriquer_tar(MEM + [("extra.sh", b"x", 0o644)])))), 14))
cas.append(("C-membre-manquant", ecrire_cas("c4", avec_charge(charge_de(fabriquer_tar(MEM[:-1])))), 14))
cas.append(("C-lien-symbolique-en-trop", ecrire_cas("c5", avec_charge(charge_de(fabriquer_tar(MEM, liens=[("lien", "/etc/passwd")])))), 14))
cas.append(("C-repertoire-en-trop", ecrire_cas("c6", avec_charge(charge_de(fabriquer_tar(MEM, reps=["d/"])))), 14))
cas.append(("C-membre-repete-meme-contenu", ecrire_cas("c7", avec_charge(charge_de(fabriquer_tar(MEM + [(MEM[3][0], b"x", 0o644)])))), 14))
cas.append(("C-base64-invalide", ecrire_cas("c8", avec_charge(charge_b64[:-4] + b"!!!!")), 14))
cas.append(("C-espace-fin-de-charge", ecrire_cas("c9", avec_charge(charge_b64 + b" ")), 14))
cas.append(("C-gzip-sans-tar", ecrire_cas("c10", avec_charge(base64.b64encode(gzip.compress(b"pas un tar")))), 14))
cas.append(("C-ligne-de-charge-vide", ecrire_cas("c11", avec_charge(b"")), 14))
cas.append(("C-nom-avec-prefixe-./", ecrire_cas("c12", avec_charge(charge_de(fabriquer_tar([("./" + n, c, md) for n, c, md in MEM])))), 14))
# taille
gros = fabriquer_tar(MEM + [("gros.bin", open("/dev/urandom", "rb").read(40000), 0o644)])
cas.append(("S-grand-membre-aleatoire (JSON > limite)", ecrire_cas("s1", avec_charge(charge_de(gros))), 13))


def json_len(lignes, fin=b"\n"):
    return len(json.dumps((b"\n".join(lignes) + fin).decode("ascii"), ensure_ascii=True))


# frontière : octets aléatoires après la fin de l'archive tar (données non vues par tarfile), pas de 3 octets
base_tar = fabriquer_tar(MEM)
junk_n = 0
cand = None
for n in range(0, 40000):
    cb = charge_de(base_tar, junk_gz=b"")
    lig = avec_charge(charge_de(base_tar + b"\0" * 0, junk_gz=b"") )
    break
# on cherche le plus grand junk (octets non compressibles ajoutés après le gzip) tel que json_len <= 32768
junk_all = open("/dev/urandom", "rb").read(40000)
lo, hi = 0, 40000
while lo < hi:
    mid = (lo + hi + 1) // 2
    if json_len(avec_charge(charge_de(base_tar, junk_gz=junk_all[:mid]))) <= 32768:
        lo = mid
    else:
        hi = mid - 1
J = lo
jl = json_len(avec_charge(charge_de(base_tar, junk_gz=junk_all[:J])))
jl2 = json_len(avec_charge(charge_de(base_tar, junk_gz=junk_all[:J + 1])))
print("frontiere : junk=%d -> json %d ; junk=%d -> json %d" % (J, jl, J + 1, jl2))
cas.append(("S-frontiere-json=%d (<=32768) avec octets apres gzip" % jl, ecrire_cas("s2", avec_charge(charge_de(base_tar, junk_gz=junk_all[:J]))), 0))
cas.append(("S-frontiere-json=%d (>32768)" % jl2, ecrire_cas("s3", avec_charge(charge_de(base_tar, junk_gz=junk_all[:J + 1]))), 13))
# octets cachés dans la charge, comptés sans contrôle
cas.append(("S-octets-apres-fin-tar (avant gzip)", ecrire_cas("s4", avec_charge(charge_de(base_tar + b"HIDDEN-PAYLOAD" * 10))), 0))
# ASCII
cas.append(("N-octet-non-ASCII-dans-amorce", ecrire_cas("n1", remplacer(5, L[5] + "é".encode())), 10))
cas.append(("N-retour-chariot", ecrire_cas("n2", remplacer(5, L[5] + b"\r")), 10))
cas.append(("N-octet-nul", ecrire_cas("n3", remplacer(5, L[5] + b"\x00")), 10))
cas.append(("N-octet-0x7f", ecrire_cas("n4", remplacer(5, L[5] + b"\x7f")), 10))
cas.append(("N-octet-0x1b", ecrire_cas("n5", remplacer(5, L[5] + b"\x1b")), 10))
cas.append(("N-non-ASCII-dans-la-charge", ecrire_cas("n6", avec_charge(charge_b64 + b"\xc3\xa9")), 10))
cas.append(("N-CRLF-partout", ecrire_cas("n7", brut=S.replace(b"\n", b"\r\n")), 10))

for nom, fich, att in cas:
    for mode in ("--envoyer", "--a-blanc"):
        rc, dn, rel, txt, r = outil(fich, mode=mode)
        dn_att = 1 if (att == 0 and mode == "--envoyer") else 0
        ok = rc == att and dn == dn_att
        if mode == "--a-blanc" and att == 0:
            ok = ok and "rien n'est envoyé" in txt and "jamais écrit" in txt
        noter("%s [%s]" % (nom, mode[2:]), "%d%s" % (att, "" if att == 0 else ",0 requete"), "%d,%d req" % (rc, dn), os.path.relpath(rel, W), ok)

# fichier absent
rc, dn, rel, txt, r = outil(T + "/cas/absent.bin")
noter("F-fichier-absent", "3,0 requete", "%d,%d req" % (rc, dn), "-", rc == 3 and dn == 0)
# relevé existant
rel0 = T + "/rel/existant.txt"
open(rel0, "w").write("intact\n")
rc, dn, rel, txt, r = outil(SAIN, relev=rel0)
noter("F-releve-existant-non-ecrase", "2,0 requete,contenu intact", "%d,%d req,%s" % (rc, dn, open(rel0).read().strip()), "travail/rel/existant.txt",
      rc == 2 and dn == 0 and open(rel0).read() == "intact\n")

# ----------------------------------------------------------------- envoi sain : le corps reçu = le corps calculé
n0 = len(journal())
rc, dn, rel, txt, r = outil(SAIN)
recu_f = sorted(x for x in os.listdir(SRV) if x.startswith("corps-"))
recu = open(SRV + "/" + recu_f[-1], "rb").read()
corps = {"name": "essai-3-palier-0b", "server_type": "cpx42", "location": "hel1", "image": "debian-13", "user_data": S.decode("ascii"),
         "public_net": {"enable_ipv4": True, "enable_ipv6": True}, "start_after_create": True, "ssh_keys": []}
attendu = json.dumps(corps, ensure_ascii=True).encode("ascii")
pj = json.loads(recu)
cles_ok = set(pj) == {"name", "server_type", "location", "image", "user_data", "public_net", "start_after_create", "ssh_keys"}
noter("B-envoi-sain-corps-recu=corps-calcule-independamment", "0,1 req,octets egaux,user_data=octets lus", "%d,%d req,egaux=%s,ud=%s,cles=%s" % (rc, dn, recu == attendu, pj["user_data"].encode() == S, cles_ok),
      os.path.relpath(rel, W), rc == 0 and dn == 1 and recu == attendu and pj["user_data"].encode() == S and cles_ok)
ligne = [x for x in journal()][-1]
noter("B-jeton-en-tete-Authorization (hash)", "sha256(Bearer T_API)", "auth=%s" % ("OK" if ("auth=" + sha(("Bearer " + T_API).encode())) in ligne else "autre"), "travail/serveur/journal.txt", ("auth=" + sha(("Bearer " + T_API).encode())) in ligne)
noter("B-releve-sans-root_password-ni-user_data-ni-echo", "absents", "root_password=%s mdp=%s echo=%s" % ("root_password" in txt, "MDP-" in txt, "ECHO-USER" in txt), os.path.relpath(rel, W),
      (chr(34) + "root_password" + chr(34)) not in txt and "MDP-" not in txt and "ECHO-USER" not in txt and "user_data" not in txt.split("retirés) : ")[-1] and "serveur : identifiant 424242" in txt)
noter("B-releve-sans-corps-ni-jeton-demarrage", "T_DEM absent du relevé", "T_DEM present=%s" % (T_DEM in txt), os.path.relpath(rel, W), T_DEM not in txt)
# 403 JSON
rc, dn, rel, txt, r = outil(SAIN, adresse=False, opts=["--adresse", "http://127.0.0.1:%d/err" % PORT, "--nom-jeton", "JETON_API"])
noter("B-reponse-403-expurgee-et-code-21", "21,1 req, rien de secret", "%d,%d req,secret=%s" % (rc, dn, "MDP-" in txt or "ECHO-USER" in txt), os.path.relpath(rel, W), rc == 21 and dn == 1 and "MDP-" not in txt and "ECHO-USER" not in txt)
# redirection
rc, dn, rel, txt, r = outil(SAIN, adresse=False, opts=["--adresse", "http://127.0.0.1:%d/redir" % PORT, "--nom-jeton", "JETON_API"])
lj = journal()[-2:]
fwd = any(x.startswith("GET /cible") and ("auth=" + sha(("Bearer " + T_API).encode())) in x for x in lj)
noter("B-redirection-302-OBSERVATION (jeton suivi ?)", "observation", "rc=%d journal=%s jeton_suivi=%s" % (rc, [x.split(" corps")[0] for x in lj], fwd), os.path.relpath(rel, W), True)
LIGNES[-1] = LIGNES[-1][:4] + ("OBS-jeton-suivi" if fwd else "OBS-non-suivi",)

# jetons
for nom, val, att in (("absent", None, 20), ("trop-court", "abc", 20), ("vide", "", 20), ("signe-hors-classe", "x" * 30 + "!", 20)):
    if val is None:
        rc, dn, rel, txt, r = outil(SAIN, env_plus={"JETON_API": ""})
    else:
        rc, dn, rel, txt, r = outil(SAIN, env_plus={"JETON_API": val})
    if val is None:
        envx = dict(BASE, CONTROLE_BANC="oui")
        compteur[0] += 1
        rel = T + "/rel/r%04d.txt" % compteur[0]
        n0 = len(journal())
        r = run([PY, "-I", TOOL, SAIN, rel, "--envoyer", "--adresse", "http://127.0.0.1:%d/v1/servers" % PORT, "--nom-jeton", "JETON_API"], envx)
        rc, dn = r.returncode, len(journal()) - n0
    noter("J-jeton-%s" % nom, "20,0 requete", "%d,%d req" % (rc, dn), "-", rc == att and dn == 0)

# banc : HCLOUD_TOKEN refusé
compteur[0] += 1
rel = T + "/rel/r%04d.txt" % compteur[0]
n0 = len(journal())
r = run([PY, "-I", TOOL, SAIN, rel, "--envoyer", "--adresse", "http://127.0.0.1:%d/v1/servers" % PORT], dict(BASE, CONTROLE_BANC="oui", HCLOUD_TOKEN="FACTICE" + "x" * 30))
noter("G-banc-nom-HCLOUD_TOKEN-refuse", "2,0 requete", "%d,%d req" % (r.returncode, len(journal()) - n0), "-", r.returncode == 2 and len(journal()) == n0 and not os.path.exists(rel))

# ----------------------------------------------------------------- garde de l'adresse hors banc
def brut(opts, envx, mode="--envoyer", port_sink=None):
    compteur[0] += 1
    rel = T + "/rel/r%04d.txt" % compteur[0]
    n0 = len(journal())
    r = run([PY, "-I", TOOL, SAIN, rel, mode] + opts, dict(BASE, **envx))
    return r.returncode, len(journal()) - n0, rel


A_LOC = "http://127.0.0.1:%d/v1/servers" % PORT
for opt in (["--adresse", A_LOC], ["--adresse", "https://api.hetzner.cloud/v1/servers"], ["--adresse", "https://api.hetzner.cloud/v1/servers/"],
            ["--nom-jeton", "JETON_API"], ["--pause-apres-lecture", T + "/rel"], ["--adresse=" + A_LOC]):
    rc, dn, rel = brut(opt, {"JETON_API": T_API})
    noter("H-hors-banc-option-%s" % opt[0], "2,0 requete", "%d,%d req" % (rc, dn), "-", rc == 2 and dn == 0 and not os.path.exists(rel))
for v in ("", "OUI", "Oui", "oui ", " oui", "1", "true", "ou", "non", "oui\n", "ouioui", "off"):
    rc, dn, rel = brut(["--adresse", A_LOC, "--nom-jeton", "JETON_API"], {"JETON_API": T_API, "CONTROLE_BANC": v})
    noter("H-CONTROLE_BANC=%r" % v, "2,0 requete", "%d,%d req" % (rc, dn), "-", rc == 2 and dn == 0)
rc, dn, rel = brut(["--adresse", A_LOC, "--nom-jeton", "JETON_API"], {"JETON_API": T_API, "CONTROLE_BANC": "oui"})
noter("H-CONTROLE_BANC=oui exact (controle positif)", "0,1 req", "%d,%d req" % (rc, dn), "-", rc == 0 and dn == 1)
for ad in ("http://localhost:%d/x" % PORT, "https://127.0.0.1:%d/x" % PORT, "http://127.0.0.1.nip.io:%d/x" % PORT, "http://127.0.0.1:%d@evil.example/x" % PORT,
           "http://127.0.0.1:%d" % PORT, "http://127.0.0.1:%d/x\n" % PORT, "http://127.0.0.2:%d/x" % PORT, "http://[::1]:%d/x" % PORT, "http://0.0.0.0:%d/x" % PORT,
           "https://api.hetzner.cloud/v1/servers/", "https://api.hetzner.cloud/v1/servers?x=1", "https://API.hetzner.cloud/v1/servers", "http://127.0.0.1:%d/x y" % PORT,
           "http://127.0.0.1:%d/x?a=b" % PORT, "http://127.0.0.1:10/" , "file:///etc/passwd", "http://api.hetzner.cloud/v1/servers", "https://api.hetzner.cloud.evil.example/v1/servers"):
    rc, dn, rel = brut(["--adresse", ad, "--nom-jeton", "JETON_API"], {"JETON_API": T_API, "CONTROLE_BANC": "oui"})
    attendu_c = 0 if ad == "http://127.0.0.1:10/" else 2
    if ad == "http://127.0.0.1:10/":
        noter("H-banc-adresse-%r (admise, port clos)" % ad, "21 (envoi en echec)", "%d,%d req" % (rc, dn), "-", rc == 21)
    else:
        noter("H-banc-adresse-%r" % ad, "2,0 requete", "%d,%d req" % (rc, dn), "-", rc == 2 and dn == 0)

# mandataire : puits local, aucun appel hors 127.0.0.1
def sink_connect(envx, opts, nom):
    compteur[0] += 1
    rel = T + "/rel/r%04d.txt" % compteur[0]
    n0 = len(journal())
    r = run([PY, "-I", TOOL, SAIN, rel, "--envoyer"] + opts, dict(BASE, **envx))
    nouv = journal()[n0:]
    return r.returncode, nouv, rel


px = "http://127.0.0.1:%d" % PORT
for nom, envx, opts in (
        ("hors-banc, HTTPS_PROXY", {"HCLOUD_TOKEN": T_API, "HTTPS_PROXY": px}, []),
        ("hors-banc, https_proxy", {"HCLOUD_TOKEN": T_API, "https_proxy": px}, []),
        ("hors-banc, ALL_PROXY", {"HCLOUD_TOKEN": T_API, "ALL_PROXY": px}, []),
        ("banc, adresse par defaut + --nom-jeton (aucune adresse locale imposee)", {"JETON_API": T_API, "CONTROLE_BANC": "oui", "HTTPS_PROXY": px}, ["--nom-jeton", "JETON_API"])):
    rc, nouv, rel = sink_connect(envx, opts, nom)
    cibles = [x.split(" corps")[0] for x in nouv]
    noter("M-%s" % nom, "OBSERVATION (cible vue par le puits)", "rc=%d journal=%s" % (rc, cibles), "-", True)
    LIGNES[-1] = LIGNES[-1][:4] + ("OBS",)

# ----------------------------------------------------------------- fichier remplacé après la lecture
def pause_essai(nom, initial, remplacement, att_rc, att_req, corps_attendu):
    dossier = T + "/pause-" + nom
    os.makedirs(dossier, exist_ok=True)
    fich = T + "/cas/pause-%s.bin" % nom
    open(fich, "wb").write(initial)
    compteur[0] += 1
    rel = T + "/rel/r%04d.txt" % compteur[0]
    env = dict(BASE, CONTROLE_BANC="oui", JETON_API=T_API)
    n0 = len(journal())
    nc0 = len([x for x in os.listdir(SRV) if x.startswith("corps-")])
    p = subprocess.Popen([PY, "-I", TOOL, fich, rel, "--envoyer", "--adresse", A_LOC, "--nom-jeton", "JETON_API", "--pause-apres-lecture", dossier],
                         env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for _ in range(600):
        if os.path.exists(dossier + "/lu"):
            break
        time.sleep(0.05)
    lu = os.path.exists(dossier + "/lu")
    if remplacement is None:
        os.remove(fich)
    else:
        with open(fich, "wb") as f:
            f.write(remplacement)
    open(dossier + "/continuer", "w").close()
    out, err = p.communicate(timeout=60)
    SORTIES.append(out + err)
    corps_f = sorted(x for x in os.listdir(SRV) if x.startswith("corps-"))
    ok_c = True
    if corps_attendu is not None:
        rec = open(SRV + "/" + corps_f[-1], "rb").read()
        ok_c = json.loads(rec)["user_data"].encode() == corps_attendu
    noter("R-remplacement-apres-lecture-%s" % nom, "lu=%s rc=%d req=%d corps=octets lus" % (True, att_rc, att_req),
          "lu=%s rc=%d req=%d corps_ok=%s" % (lu, p.returncode, len(journal()) - n0, ok_c), os.path.relpath(rel, W),
          lu and p.returncode == att_rc and len(journal()) - n0 == att_req and ok_c)


mauvais = remplacer(4, L[4] + b" ")
mauvais_b = b"\n".join(mauvais) + b"\n"
pause_essai("sain-puis-mauvais", S, mauvais_b, 0, 1, S)
pause_essai("sain-puis-supprime", S, None, 0, 1, S)
pause_essai("sain-puis-vide", S, b"", 0, 1, S)
pause_essai("mauvais-puis-sain", mauvais_b, S, 12, 0, None)

# ----------------------------------------------------------------- fin : jetons, ps
open(T + "/serveur/arret", "w").close()
open(stop_g, "w").close()
try:
    sv.wait(timeout=10)
except Exception:
    sv.terminate()
try:
    g.wait(timeout=10)
except Exception:
    g.terminate()
guet = open(T + "/guet.sortie").read()
noter("P-jeton-API-et-demarrage-absents-de-ps (guetteur 20 ms)", "0 ligne", guet.strip().splitlines()[-1], "travail/guet.sortie", "lignes portant le jeton : 0" in guet and "relevés : 0" not in guet)

hits_api, hits_dem = [], []
exclus_dem = {os.path.basename(SAIN)}
for racine, _, fs in os.walk(T):
    for f in fs:
        chemin = os.path.join(racine, f)
        if chemin == T + "/jetons.txt":
            continue
        try:
            b = open(chemin, "rb").read()
        except OSError:
            continue
        if T_API.encode() in b:
            hits_api.append(chemin)
        if T_DEM.encode() in b and not (f.startswith("corps-") or racine.startswith(T + "/cas") or f.startswith("sain.bin") or f.endswith(".sans-jeton")):
            hits_dem.append(chemin)
sb = b"\n".join(SORTIES)
noter("P-jeton-API-absent-de-tout-fichier-et-sortie", "0 fichier, 0 sortie", "fichiers=%s sorties=%s" % (hits_api, T_API.encode() in sb), "travail/", not hits_api and T_API.encode() not in sb)
noter("P-jeton-demarrage-absent-des-releves-et-sorties-(hors-donnees/corps)", "0", "fichiers=%s sorties=%s" % ([os.path.relpath(x, W) for x in hits_dem], T_DEM.encode() in sb), "travail/", not [h for h in hits_dem if "/rel/" in h] and T_DEM.encode() not in sb)

with open(W + "/tables/table-des-cas.tsv", "w") as f:
    f.write("cas\tattendu\trendu\tfichier\tverdict\n")
    for x in LIGNES:
        f.write("\t".join(str(y).replace("\t", " ") for y in x) + "\n")
n_ecart = sum(1 for x in LIGNES if x[4] == "ECART")
print("cas : %d ; ecarts : %d" % (len(LIGNES), n_ecart))
