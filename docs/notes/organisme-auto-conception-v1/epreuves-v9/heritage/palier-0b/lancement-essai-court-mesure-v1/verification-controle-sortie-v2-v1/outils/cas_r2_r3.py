import base64, gzip, io, os, subprocess, sys, zlib, shutil

W = "/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verification-controle-sortie-v2"
P = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/"
V1 = P + "auteur-controle-sortie-v1/controler-et-creer-essai-3-v1.py"
V2 = P + "auteur-controle-sortie-v2/controler-et-creer-essai-3-v2.py"
PY = "/home/user/controle-ia-travail/.venv/bin/python"
D = W + "/donnees/"
R = W + "/releves/"
os.makedirs(R, exist_ok=True)

sain = open(D + "sain.txt", "rb").read()
lignes = sain.split(b"\n")
assert lignes[-1] == b"" and lignes[-2] and lignes[-3] == b"__CHARGE_DES_PIECES__"
brut = base64.b64decode(lignes[-2])
tar = gzip.decompress(brut)
print("tar", len(tar), "gz", len(brut))
# fin du dernier membre
import tarfile
with tarfile.open(fileobj=io.BytesIO(tar)) as tf:
    fin = max(m.offset_data + -(-m.size // 512) * 512 for m in tf.getmembers())
print("fin dernier membre", fin, "remplissage", len(tar) - fin)


def regz(t):
    return gzip.compress(t, 9, mtime=0)


def donnees(charge):
    return b"\n".join(lignes[:-2]) + b"\n" + base64.b64encode(charge) + b"\n"

var = {}
var["sain_identique"] = sain
var["sain_recompresse"] = donnees(regz(tar))
var["gz_plus_1_octet_nul"] = donnees(brut + b"\0")
var["gz_plus_4_octets_AAAA"] = donnees(brut + b"AAAA")
var["gz_seconde_trame_vide"] = donnees(brut + regz(b""))
var["gz_seconde_trame_x"] = donnees(brut + regz(b"x"))
var["gz_seconde_trame_zeros"] = donnees(brut + regz(b"\0" * 10240))
var["gz_tronque_4_derniers"] = donnees(brut[:-4])
var["tar_plus_octet_non_nul_apres_tar"] = donnees(regz(tar + b"x"))
var["tar_octet_non_nul_dans_remplissage_meme_longueur"] = donnees(regz(tar[:fin + 2000] + b"\x01" + tar[fin + 2001:]))
var["tar_octet_non_nul_juste_apres_dernier_membre"] = donnees(regz(tar[:fin] + b"\x01" + tar[fin + 1:]))
var["tar_octet_non_nul_dernier_octet"] = donnees(regz(tar[:-1] + b"\x01"))
var["tar_remplissage_tronque_1_bloc"] = donnees(regz(tar[:-512]))
var["tar_remplissage_tronque_20_blocs_a_fin_plus_1024"] = donnees(regz(tar[:fin + 1024]))
var["tar_remplissage_allonge_1_bloc"] = donnees(regz(tar + b"\0" * 512))
var["tar_remplissage_allonge_1_octet"] = donnees(regz(tar + b"\0"))
var["tar_remplissage_allonge_10240"] = donnees(regz(tar + b"\0" * 10240))
var["tar_sans_remplissage_fin_exacte"] = donnees(regz(tar[:fin]))
# l'archive d'origine sans ajout mais avec dernier octet coupé
var["tar_moins_1_octet"] = donnees(regz(tar[:-1]))

for nom, d in var.items():
    open(D + "v-" + nom + ".txt", "wb").write(d)

env = {k: v for k, v in os.environ.items() if k != "HCLOUD_TOKEN"}
env["PATH"] = "/usr/bin:/bin"
env.pop("CONTROLE_BANC", None)


def jouer(script, nom, fichier, extra=(), banc=False, tag=""):
    e = dict(env)
    if banc:
        e["CONTROLE_BANC"] = "oui"
    rel = R + "%s-%s-%s.txt" % (tag or nom, "v1" if script == V1 else "v2", os.getpid())
    if os.path.exists(rel):
        os.remove(rel)
    p = subprocess.run([PY, "-I", script, fichier, rel] + list(extra), env=e, capture_output=True, text=True)
    refus = ""
    if os.path.exists(rel):
        for l in open(rel, encoding="utf-8"):
            if l.startswith("REFUS") or "corps de création" in l:
                refus = l.strip()[:150]
    return p.returncode, refus or (p.stderr.strip()[:150])


print("=== R2 (a blanc) ===")
out = []
for nom in var:
    f = D + "v-" + nom + ".txt"
    c1, m1 = jouer(V1, nom, f)
    c2, m2 = jouer(V2, nom, f)
    s = "%-55s v1=%-3d v2=%-3d | v2: %s" % (nom, c1, c2, m2)
    print(s)
    out.append(s)
open(W + "/tables/r2-cas.txt", "w").write("\n".join(out) + "\n")

print("=== R3 ===")
out = []
f = D + "sain.txt"
cas = [
    ("nom-jeton sans adresse, banc", ["--nom-jeton", "FAUXJ"], True),
    ("nom-jeton sans adresse, hors banc", ["--nom-jeton", "FAUXJ"], False),
    ("nom-jeton avec adresse, hors banc", ["--adresse", "http://127.0.0.1:9/x", "--nom-jeton", "FAUXJ"], False),
    ("nom-jeton sans adresse, banc, envoyer", ["--envoyer", "--nom-jeton", "FAUXJ"], True),
    ("nom-jeton sans adresse, hors banc, envoyer", ["--envoyer", "--nom-jeton", "FAUXJ"], False),
    ("nom-jeton=HCLOUD_TOKEN sans adresse, hors banc", ["--nom-jeton", "HCLOUD_TOKEN"], False),
    ("nom-jeton sans adresse mais adresse = defaut officiel", ["--adresse", "https://api.hetzner.cloud/v1/servers", "--nom-jeton", "FAUXJ"], True),
    ("sain a blanc, aucune option", [], False),
]
for i, (nom, extra, banc) in enumerate(cas):
    c1, m1 = jouer(V1, nom, f, extra, banc, tag="r3-%d" % i)
    c2, m2 = jouer(V2, nom, f, extra, banc, tag="r3-%d" % i)
    s = "%-55s v1=%-3d v2=%-3d | v2: %s" % (nom, c1, c2, m2[:100])
    print(s)
    out.append(s)
open(W + "/tables/r3-cas.txt", "w").write("\n".join(out) + "\n")
