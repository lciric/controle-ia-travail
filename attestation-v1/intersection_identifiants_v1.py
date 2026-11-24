# Intersections d'identifiants de tâches ; n'affiche que des tailles, booléens et empreintes.
import json, re, subprocess, hashlib, sys, glob
def show(ref, path):
    return subprocess.run(["git","show",f"{ref}:{path}"],capture_output=True).stdout
ev=[t["identifiant"] for t in json.load(open("donnees/20261007-082440-t05-extraction/taches-evaluation.json"))["resultat"]["taches"]]
en=[t["identifiant"] for t in json.load(open("donnees/20261007-082440-t05-extraction/taches-entrainement.json"))["resultat"]["taches"]]
pil=[t["identifiant"] for t in json.load(open("donnees/t05-pilote-v1/taches-pilote-60-v1.json"))["taches"]]
E,R,P=set(ev),set(en),set(pil)
print("empreinte_ensemble_64", hashlib.sha256("\n".join(sorted(E)).encode()).hexdigest())
man=json.load(open(glob.glob("runs/20261019-230011-p3-reel/manifeste.json")[0]))
txt=json.dumps(man)
p3=set(re.findall(r'tache/([0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?)',txt))
print("taille_64",len(E),"taille_32",len(R),"taille_pilote",len(P),"taille_premier_test",len(p3))
print("premier_test_inclus_dans_64",p3<=E,"premier_test_egal_pilote",p3==P,"64_inter_32",len(E&R))
# Coffre : famille de réserve du cycle 2
B="origin/claude/scellement-2-famille-reserve-cycle-2-v1"
pat=re.compile(r'(?<![0-9])([0-9]{4}\.[0-9]{4,5})(v[0-9]+)?(?![0-9])')
base=lambda s:{re.sub(r'v[0-9]+$','',x) for x in s}
Eb,Rb,P3b=base(E),base(R),base(p3)
noms=["taches-evaluation","taches-entrainement","t05-extraction","taches-pilote","t05-pilote","20261007-082440","20261019-230011","p3-reel","banque initiale","96 t"]
for d,ps in [("donnees/bras-attaque-scellement-2-cycle-2-v1",["piece-2-texte-de-la-famille-v1","piece-2-texte-de-la-famille-v2","piece-3-verite-du-dommage-v1","piece-3-verite-du-dommage-v2","piece-4-plan-des-epreuves-de-l-oracle-v1","piece-4-plan-des-epreuves-de-l-oracle-v2","piece-5-lecture-de-la-force-v1","piece-5-lecture-de-la-force-v2"]),("docs/notes/scellement-2-famille-reserve-cycle-2-v1",["piece-6-esquisse-de-devis-banque-d-episodes-v2"])]:
    for p in ps:
        b=show(B,f"{d}/{p}.md"); t=b.decode("utf-8","replace")
        ids={m.group(1) for m in pat.finditer(t)}
        refs=sum(1 for n in noms if n.lower() in t.lower())
        print(p, "sha256", hashlib.sha256(b).hexdigest()[:8], "octets",len(b), "identifiants_forme_arxiv",len(ids),
              "inter_64",len(ids&Eb),"inter_premier_test",len(ids&P3b),"inter_32",len(ids&Rb),"noms_de_banque_cites",refs)
