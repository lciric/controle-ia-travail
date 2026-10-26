import json, os, pathlib, secrets, sys, tempfile
sys.path.insert(0, ".")
from essaim_m3.noyau import bac_a_sable as B
if not (B.capacites_isolation().get("root") and B.capacites_isolation().get("espaces_noms")):
    print("SAUTÉ : root et espaces de noms exigés"); sys.exit(0)

jeton = secrets.token_hex(6)
# CL5-01 : un fichier secret lisible par tous, dans un dossier listé par ESSAIM_M3_CACHER, doit être invisible
cacher = pathlib.Path(tempfile.mkdtemp(prefix="cl5-cacher-", dir="/var/lib"))
os.chmod(cacher, 0o755)
secret = cacher / "banque-factice.json"
secret.write_text('{"verite": "SECRET-%s"}' % jeton); os.chmod(secret, 0o644)
os.environ["ESSAIM_M3_CACHER"] = str(cacher)

def organisme(nom, source):
    org = pathlib.Path(tempfile.mkdtemp(prefix="cl5-org-")) / "organisme"; org.mkdir(parents=True)
    (org / "manifeste.json").write_text(json.dumps({"nom": nom, "version": "1", "entree": "principal:executer", "description": "x"}))
    (org / "principal.py").write_text(source)
    return org.parent

esp = B.espace_organismes(pathlib.Path(tempfile.mkdtemp(prefix="cl5-course-")), course_nouvelle=True)
# CL5-01
src01 = ("import json, os\n"
         "def executer(contexte):\n"
         "    r = {}\n"
         f"    p = {str(secret)!r}\n"
         "    try: r['lu'] = open(p).read()\n"
         "    except Exception as e: r['lu'] = type(e).__name__\n"
         "    json.dump(r, open(os.path.join(contexte['dossier_travail'], 'r.json'), 'w'))\n")
org01 = organisme("lire-cache", src01)
travail = esp / "lire-cache"; uid = B.uid_lignee(0, 800)
ctx = {"generation":0,"lignee":"lire-cache","mission":"m","dossier_travail":str(travail),"dossier_archive":str(esp),
       "taches_entrainement":[],"taches_test":[],"budget":{"appels_max":1,"usd_max":0.1,"temps_max_s":30},"historique":[]}
B.preparer(travail, org01/"organisme", ctx, uid=uid)
ex = B.executer(travail, str(travail/"n.sock"), 30, isoler_reseau=True, uid=uid)
print("CL5-01 code", ex["code"], "| caches:", ex.get("caches"))
print("ERREURS:", (travail/"erreurs.txt").read_text()[-600:])
r01 = json.loads((travail/"r.json").read_text()) if (travail/"r.json").exists() else {"lu":"(pas de r.json)"}
print("CL5-01 code", ex["code"], "| caches couvre le dossier :", str(cacher.resolve()) in ex.get("caches", []))
print("CL5-01 lecture du secret :", r01["lu"], "| secret absent :", ("SECRET-%s" % jeton) not in json.dumps(r01))

# CL5-02 : deux organismes (A, B) via un dossier inscriptible par tous découvert par le balayage
commun = pathlib.Path("/var/lib/essaim-m3-cl5-commun-%s" % jeton); commun.mkdir(parents=True); os.chmod(commun, 0o1777)
B.dossiers_inscriptibles_par_tous(rafraichir=True)  # re-balaye pour trouver le dossier neuf
couvert = str(commun.resolve()) in B.dossiers_tmp_a_rendre_prives([travail])
cible = commun / "canal.txt"
srcA = ("import os\n"
        "def executer(contexte):\n"
        f"    open({str(cible)!r}, 'w').write('sonde de A'); os.chmod({str(cible)!r}, 0o644)\n")
srcB = ("import json, os\n"
        "def executer(contexte):\n"
        "    r={}\n"
        f"    try: r['lu']=open({str(cible)!r}).read()\n"
        "    except Exception as e: r['lu']=type(e).__name__\n"
        "    json.dump(r, open(os.path.join(contexte['dossier_travail'],'r.json'),'w'))\n")
for nom, src, u in (("A", srcA, B.uid_lignee(1, 800)), ("B", srcB, B.uid_lignee(3, 800))):
    org = organisme("canal-"+nom, src); tr = esp / ("canal-"+nom)
    c = dict(ctx, lignee="canal-"+nom, dossier_travail=str(tr))
    B.preparer(tr, org/"organisme", c, uid=u)
    exx = B.executer(tr, str(tr/"n.sock"), 30, isoler_reseau=True, uid=u)
    if nom == "B":
        rB = json.loads((tr/"r.json").read_text())
print("CL5-02 dossier commun couvert :", couvert, "| B lit ce que A a écrit :", rB["lu"])
print("CL5-02 sur l'hôte, le canal de A existe :", cible.exists(), "(attendu False : écriture restée dans le privé de A)")
import shutil
for d in (cacher, commun): shutil.rmtree(d, ignore_errors=True)
