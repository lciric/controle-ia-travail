import hashlib, json, os, re, sys
E = "/root/bac-lecture-7b-compte-3-v2/espace-table-a-v2"
P = E + "/pieces"
RUN = "20261111-151701-t06-reel"
ok = True
def h(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()
def say(s):
    print(s)
def fail(code, s):
    global ok
    ok = False
    print("ECART [%s] %s" % (code, s))

bh = h(E + "/bordereau-remise-v2.txt")
say("bordereau empreinte %s" % bh)
if bh != "1e71d61e3e7d46f8569226892b5cf9c9ec875df25955fe3e1d7b3cc7959e934e":
    fail("piece-non-conforme", "bordereau != message")
if open(E + "/bordereau-remise-v2.txt.sha256").read().split()[0] != bh:
    fail("piece-non-conforme", "bordereau != compagnon")
lines = [l for l in open(E + "/bordereau-remise-v2.txt", encoding="utf-8").read().split("\n") if l]
say("lignes du bordereau: %d" % len(lines))
if len(lines) != 33:
    fail("piece-non-conforme", "33 lignes attendues")
bord = {}
for l in lines:
    m = re.match(r"^([0-9a-f]{64})  (\./.+)$", l)
    if not m:
        fail("piece-non-conforme", "ligne mal formée " + l); continue
    bord[m.group(2)] = m.group(1)
ens = set()
for r, d, fs in os.walk(P):
    for f in fs:
        ens.add("./" + os.path.relpath(os.path.join(r, f), P))
say("fichiers sous pieces: %d" % len(ens))
if ens != set(bord):
    fail("piece-non-conforme", "ensemble différent: en plus %s, en moins %s" % (sorted(ens - set(bord)), sorted(set(bord) - ens)))
interd = ["lecture-sondes", "resume.json", "arret.json", "activations", "adaptateur", "t07", "t0.7", "bbis", "b-bis", "bras-attaque", "mode-tenu", "anteriorite-bras", "etiqueteur", "quarantaine", "mesure-unanime"]
for c in sorted(bord):
    if any(i in c.lower() for i in interd):
        fail("fichier-interdit-recu", c)
neq = 0
for c, e in sorted(bord.items()):
    hh = h(P + "/" + c[2:])
    if hh != e:
        fail("piece-non-conforme", "empreinte " + c)
    else:
        neq += 1
    comp = P + "/" + c[2:] + ".sha256"
    if os.path.exists(comp):
        ce = open(comp).read().split()[0]
        if ce != hh:
            fail("piece-non-conforme", "compagnon " + c)
        else:
            say("compagnon égal: %s" % c)
say("empreintes égales au bordereau: %d / %d" % (neq, len(bord)))
tot = 0
for t, n in (("traces/t06-20261112-051655-1Xzh", 9), ("traces/consignation-20261112-051705-vUfJ", 2)):
    d = P + "/" + t
    ls = [l for l in open(d + "/empreintes.sha256", encoding="utf-8").read().split("\n") if l.strip()]
    say("%s: %d fichiers listés (attendu %d)" % (t, len(ls), n))
    if len(ls) != n:
        fail("piece-non-conforme", "nombre " + t)
    for l in ls:
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", l)
        f = m.group(2).strip()
        f = f[2:] if f.startswith("./") else f
        f = os.path.basename(f) if not os.path.exists(d + "/" + f) else f
        if h(d + "/" + f) == m.group(1):
            tot += 1
        else:
            fail("piece-non-conforme", "trace " + t + "/" + f)
say("traces égales: %d (attendu 11)" % tot)
# point 2 registre
ex = open(P + "/extrait-registres-table-a-v2.md", encoding="utf-8").read().split("\n")
reg = [l for l in ex if "RUN-CONFIRMATION-T06" in l]
say("lignes de registre: %d" % len(reg))
m = re.match(r"^\d+:\| RUN-CONFIRMATION-T06 \| (\S+) \| runs/%s/manifeste.json \| ([0-9a-f]{64}) \|$" % RUN, reg[0]) if len(reg) == 1 else None
mh = h(P + "/runs/%s/manifeste.json" % RUN)
if not m or m.group(2) != mh:
    fail("piece-non-conforme", "registre")
else:
    say("registre: date %s, empreinte égale à celle de manifeste.json (%s)" % (m.group(1), mh))
# point 3 manifeste
man = json.load(open(P + "/runs/%s/manifeste.json" % RUN, encoding="utf-8"))
txt_h = h(P + "/prereg/T0.6-organismes-v0-v1.md")
say("run_id=%r decisif=%r prereg=%r" % (man.get("run_id"), man.get("decisif"), man.get("preenregistrement")))
if man.get("run_id") != RUN or man.get("decisif") is not True or man["preenregistrement"].get("chemin") != "prereg/T0.6-organismes-v0-v1.md" or man["preenregistrement"].get("sha256") != txt_h:
    fail("piece-non-conforme", "manifeste")
cfg = json.load(open(P + "/prereg/T0.6-organismes-config-7b-v1.json", encoding="utf-8"))
if man.get("config") == cfg:
    say("config du manifeste égale à la configuration (objet JSON)")
else:
    say("config du manifeste DIFFÉRENTE de la configuration")
    for k in sorted(set(man.get("config", {})) | set(cfg)):
        a = man.get("config", {}).get(k, "<absent>"); b = cfg.get(k, "<absent>")
        if a != b:
            say("  clé %s: manifeste=%r configuration=%r" % (k, a, b))
say("config_sha256 du manifeste: %s ; empreinte de la configuration: %s" % (man.get("config_sha256"), h(P + "/prereg/T0.6-organismes-config-7b-v1.json")))
say("commit du manifeste: %s" % man.get("commit"))
# point 4
for f in ("lecture-cout-t06.json", "episodes-t06.json", "distillation-t06.json"):
    d = json.load(open(P + "/diag/%s/%s" % (RUN, f), encoding="utf-8"))
    r1 = d.get("run_id") == RUN; r2 = d.get("manifeste_sha256") == mh
    say("%s: run_id égal %s ; manifeste_sha256 égal %s" % (f, r1, r2))
    if not (r1 and r2):
        fail("piece-non-conforme", "rattachement " + f)
ep = json.load(open(P + "/diag/%s/episodes-t06.json" % RUN, encoding="utf-8"))["resultat"]
a = ep.get("mesures_sha256") == h(P + "/donnees/%s/mesures-t06.npz" % RUN)
b = ep.get("textes_sha256") == h(P + "/donnees/%s/textes-actions-t06.jsonl" % RUN)
say("mesures_sha256 égal %s ; textes_sha256 égal %s" % (a, b))
if not (a and b):
    fail("piece-non-conforme", "rattachement données")
# point 5
c = open(P + "/constat-noms-7b-v2.txt", encoding="utf-8").read()
say("constat: " + " | ".join(c.split("\n")[1:4]))
say("RESULTAT DES CONTROLES: " + ("conformes" if ok else "ECART"))
sys.exit(0 if ok else 1)
