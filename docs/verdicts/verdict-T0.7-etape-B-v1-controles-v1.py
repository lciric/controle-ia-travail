# Script « controles » (sections 6.1, 6.3, 6.4 de la consigne). Lecture seule ; sortie sur la sortie standard.
import hashlib, json, os, re, sys
E = "/root/bac-etape-b-compte-3-v2/espace-etape-b-v2"
P = E + "/pieces"
CONS = "docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1.md"
RUN_T07 = "20261114-001352-t07-lecture-reel"
RUN_T06 = "20261111-151701-t06-reel"
ARRET = []
def arret(code, msg):
    print("ARRET", code, msg); ARRET.append((code, msg))
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def lines(p):
    return open(p, encoding="utf-8").read().split("\n")

print("== 6.1 (1) bordereau")
bord_p = E + "/bordereau-remise-v2.txt"
b_h = sha(bord_p); comp = open(bord_p + ".sha256").read().split()[0]
MSG_B = "8ba91d7f653712aa6f105b0ac9fb170a574cfd80b7c7843b5cb5d60e1b953cda"
print("bordereau", b_h, "== message:", b_h == MSG_B, "== compagnon:", b_h == comp)
if not (b_h == MSG_B == comp): arret("piece-non-conforme", "bordereau")
bl = [l for l in open(bord_p, encoding="utf-8").read().split("\n") if l.strip()]
print("lignes du bordereau:", len(bl), "(attendu 29)")
if len(bl) != 29: arret("piece-non-conforme", "29 lignes")
bord = {}
for l in bl:
    m = re.match(r"^([0-9a-f]{64})  \./(.+)$", l)
    if not m: arret("piece-non-conforme", "format ligne " + l[:40]); continue
    bord[m.group(2)] = m.group(1)
names = set()
for d, _, fs in os.walk(P):
    for f in fs: names.add(os.path.relpath(os.path.join(d, f), P))
print("noms sous pieces:", len(names), "| hors bordereau:", sorted(names - set(bord)), "| manquants:", sorted(set(bord) - names))
if names != set(bord): arret("fichier-interdit-recu" if names - set(bord) else "piece-non-conforme", "ensemble des noms")

# extrait (piece 2) : chemin de la piece 12
ext = lines(P + "/extrait-registres-etape-b-v2.md")
reg = {}   # cle -> liste de (date, chemin, empreinte)
sect = None
sections = []
journal = []
dedie = []
for l in ext:
    if l.startswith("## "):
        sect = l; sections.append(l); continue
    m = re.match(r"^(\d+):\|(.*)\|\s*$", l)
    if not m: continue
    champs = [c.strip() for c in m.group(2).split("|")]
    if sect.startswith("## registres/scellements-v1.md") and "ouvertures" not in sect:
        reg.setdefault(champs[0], []).append((m.group(1), champs))
    elif "ouvertures" in sect:
        journal.append(champs)
    elif "decisions" in sect:
        dedie.append(l)
issue_chemin = reg["ISSUE-MOTS-ET-COUT-T06"][0][1][2]
print("piece 12 (ligne ISSUE-MOTS-ET-COUT-T06):", issue_chemin)
closed = {CONS, "extrait-registres-etape-b-v2.md", "docs/decisions/decision-N-063-v2.md", "prereg/T0.7-sondes-v0-v1.md",
 "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md", "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json",
 "prereg/T0.6-organismes-v0-v1.md", "prereg/T0.8-base-A-mots-et-cout-v1.md", "prereg/T0.7-consigne-audit-fuites-v1.md",
 "docs/verdicts/verdict-P3-bis-v1-issue.json", "runs/%s/manifeste.json" % RUN_T07, issue_chemin,
 "diag/%s/audit-fuites-t07.json" % RUN_T07, "diag/%s/lecture-t07.json" % RUN_T07, "diag/%s/sondes-t07.json" % RUN_T07}
allowed = set(closed) | {c + ".sha256" for c in closed if c != "extrait-registres-etape-b-v2.md"}
print("hors liste fermee:", sorted(names - allowed), "| liste fermee absente:", sorted(allowed - names))
if names - allowed: arret("fichier-interdit-recu", "liste fermee")
if allowed - names: arret("piece-non-conforme", "liste fermee absente")

print("== 6.1 (2) empreintes")
TABLE = []
for n in sorted(names):
    h = sha(P + "/" + n)
    ok_b = (bord.get(n) == h)
    ok_c = None
    if not n.endswith(".sha256") and n != "extrait-registres-etape-b-v2.md":
        ok_c = (open(P + "/" + n + ".sha256").read().split()[0] == h)
    print("%s  %s  bordereau=%s compagnon=%s" % (h, n, ok_b, ok_c))
    if not ok_b or ok_c is False: arret("piece-non-conforme", "empreinte " + n)
ENT = {"prereg/T0.7-sondes-v0-v1.md": "d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5",
 "prereg/T0.6-organismes-v0-v1.md": "ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169",
 "prereg/T0.8-base-A-mots-et-cout-v1.md": "72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d",
 "docs/decisions/decision-N-063-v2.md": "b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b",
 "prereg/T0.7-consigne-audit-fuites-v1.md": "43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d",
 "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md": "8c377286f2fa9be7020416a1d25bbcebb8fad0944f14c508614519a6a0886dc8",
 "prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json": "e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328"}
for n, h in ENT.items():
    print("en-tete consigne", n, sha(P + "/" + n) == h)
    if sha(P + "/" + n) != h: arret("piece-non-conforme", "en-tete " + n)
print("consigne = message:", sha(P + "/" + CONS) == "1fa37cbc984beb977c418e81c838131f848ceb46b053c6e2e01b077f99e4d8ae")

print("== 6.1 citations de la table 3.2")
cl = lines(P + "/" + CONS)
i0 = next(i for i, l in enumerate(cl) if l.startswith("### 3.2"))
i1 = next(i for i in range(i0, len(cl)) if cl[i] == "~~~~text")
i2 = next(i for i in range(i1 + 1, len(cl)) if cl[i] == "~~~~")
FM = {"T07": "prereg/T0.7-sondes-v0-v1.md", "T06": "prereg/T0.6-organismes-v0-v1.md", "T08A": "prereg/T0.8-base-A-mots-et-cout-v1.md",
      "N063": "docs/decisions/decision-N-063-v2.md", "AUD": "prereg/T0.7-consigne-audit-fuites-v1.md",
      "ADD": "prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md"}
cache = {k: lines(P + "/" + v) for k, v in FM.items()}
nc = bad = 0
for l in cl[i1 + 1:i2]:
    if l.startswith("#") or not l.strip(): continue
    parts = l.split(" | ", 3)
    if len(parts) != 4: print("ligne de table non lue:", l[:60]); bad += 1; continue
    rid, f, ln, cit = parts
    nc += 1
    txt = cache[f]
    n = int(ln)
    if cit not in txt[n - 1]:
        bad += 1; print("CITATION ABSENTE", rid, f, ln)
print("citations:", nc, "absentes:", bad)
if bad: arret("piece-non-conforme", "citations")

print("== 6.3 registre")
print("sections de l'extrait:", sections)
if len(sections) != 3: arret("piece-non-conforme", "extrait incomplet")
KEYS = ["SCELLEMENT-T07", "CODE-T07", "RUN-CONFIRMATION-T06", "SCORES-T07", "SONDES-T07", "CONSIGNE-AUDIT-FUITES-T07",
        "AUDIT-FUITES-T07", "SCELLEMENT-P3BIS", "VERDICT-P3BIS", "ISSUE-MOTS-ET-COUT-T06", "LECTURE-T08-BASE-A", "SCELLEMENT-T08-BASE-A"]
for k in KEYS:
    n = len(reg.get(k, []))
    print(k, "lignes:", n, reg[k][0][1][1:] if n else "")
    if n != 1: arret("piece-non-conforme", "cle " + k)
print("clés JEUX:", [k for k in reg if k.startswith("SCELLEMENT-JEUX")], "| SCELLEMENT-CONCEPTS-T07 presente:", "SCELLEMENT-CONCEPTS-T07" in reg)
def L(k): return reg[k][0][1]
def egal(k, piece):
    c = L(k); ok = (c[2] == piece[0] and c[3] == sha(P + "/" + piece[0]))
    print("egalite", k, "~", piece[0], ok)
    if not ok: arret("piece-non-conforme", "egalite " + k)
egal("SCELLEMENT-T07", ["prereg/T0.7-sondes-v0-v1.md"]); egal("CONSIGNE-AUDIT-FUITES-T07", ["prereg/T0.7-consigne-audit-fuites-v1.md"])
egal("AUDIT-FUITES-T07", ["diag/%s/audit-fuites-t07.json" % RUN_T07]); egal("VERDICT-P3BIS", ["docs/verdicts/verdict-P3-bis-v1-issue.json"])
egal("ISSUE-MOTS-ET-COUT-T06", [issue_chemin]); egal("SCELLEMENT-T08-BASE-A", ["prereg/T0.8-base-A-mots-et-cout-v1.md"])
egal("SONDES-T07", ["diag/%s/sondes-t07.json" % RUN_T07])
# 4. CODE-T07 et addendum
add = cache["ADD"]
nl = [l for l in add if l.startswith("**Nouvelle ligne**")]
print("addendum, Nouvelle ligne:", nl)
c = L("CODE-T07"); ligne_code = "| " + " | ".join(c) + " |"
print("ligne CODE-T07 de l'extrait:", ligne_code)
print("ligne CODE-T07 contenue dans la Nouvelle ligne de l'addendum:", any(ligne_code in l for l in nl), "| texte scelle nomme:", [l[:200] for l in cache["T07"] if "`CODE-T07`" in l and "CODE-T07-v" in l][:3])
# 5. dates
D = lambda k: L(k)[1]
jr = [j for j in journal if j[0] == "OUVERTURE-T07" and j[2].startswith("etape-B/")]
js = [j for j in journal if j[0] == "OUVERTURE-T07" and j[2].startswith("scores-t07/")]
rf = [j for j in journal if j[0] == "REFUS-T07"]
print("journal: ouverture etape B:", len(jr), "| ligne scores:", len(js), "| REFUS-T07:", rf)
if len(jr) != 1: arret("piece-non-conforme", "journal")
dO = jr[0][1]
print("date ouverture etape B:", dO)
chk = lambda a, b: a < b
print("CONSIGNE-AUDIT < AUDIT-FUITES:", chk(D("CONSIGNE-AUDIT-FUITES-T07"), D("AUDIT-FUITES-T07")))
print("SCELLEMENT-T07 < VERDICT-P3BIS:", chk(D("SCELLEMENT-T07"), D("VERDICT-P3BIS")))
dix = ["SCELLEMENT-T07", "CODE-T07", "RUN-CONFIRMATION-T06", "SCORES-T07", "SONDES-T07", "CONSIGNE-AUDIT-FUITES-T07", "AUDIT-FUITES-T07", "SCELLEMENT-P3BIS", "VERDICT-P3BIS", "ISSUE-MOTS-ET-COUT-T06"]
for k in dix: print("  avant ouverture:", k, D(k), chk(D(k), dO))
r167 = chk(D("SCORES-T07"), D("VERDICT-P3BIS")) and chk(D("SONDES-T07"), D("VERDICT-P3BIS"))
print("SCORES-T07 et SONDES-T07 < VERDICT-P3BIS (R167):", r167, "(SCORES", D("SCORES-T07"), "SONDES", D("SONDES-T07"), "VERDICT-P3BIS", D("VERDICT-P3BIS"), ")")
if js:
    print("ligne scores-t07 du journal:", js[0][1], js[0][2].split("(")[0].strip(), "| apres SCELLEMENT-P3BIS et VERDICT-P3BIS:", chk(D("SCELLEMENT-P3BIS"), js[0][1]) and chk(D("VERDICT-P3BIS"), js[0][1]))
print("LECTURE-T08-BASE-A", D("LECTURE-T08-BASE-A"), "< ouverture:", chk(D("LECTURE-T08-BASE-A"), dO))
ded = [l for l in dedie]
print("lignes dediees BA-L2:", len(ded), "| contient BA-L2:", all("BA-L2" in l for l in ded), "| 'ne s'applique pas':", all("ne s'applique pas" in l for l in ded), "| 'mot de Lazar':", any("mot de Lazar" in l for l in ded))
if len(ded) != 1 or "BA-L2" not in ded[0]: arret("piece-non-conforme", "BA-L2")

print("== 6.4 manifeste, configuration, rattachement")
mf_p = P + "/runs/%s/manifeste.json" % RUN_T07
mf = json.load(open(mf_p, encoding="utf-8"))
print("manifeste run_id:", mf["run_id"], mf["run_id"] == RUN_T07, "| decisif:", mf["decisif"], "| prereg:", mf["preenregistrement"], "| commit:", mf["commit"])
if not (mf["run_id"] == RUN_T07 and mf["decisif"] is True and mf["preenregistrement"]["chemin"] == "prereg/T0.7-sondes-v0-v1.md"
        and mf["preenregistrement"]["sha256"] == ENT["prereg/T0.7-sondes-v0-v1.md"]): arret("piece-non-conforme", "manifeste")
cf = json.load(open(P + "/prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json", encoding="utf-8"))
mc = mf["config"]
GEL = ["niveau_decisif", "quantile_plancher", "n_plancher", "tirages_aire", "permutations_placebo", "seuil_degeneres", "p064", "controle_aire",
       "garde_adaptee", "portee_regle_4", "niveau_base_t06", "go_id_attendu", "go_id_refuse"]
inegal = []
for k, v in cf.items():
    if k not in mc: inegal.append((k, "absente du manifeste")); continue
    if mc[k] != v: inegal.append((k, "inegale"))
print("cles de la configuration:", len(cf), "| inegales ou absentes:", inegal)
print("cles gelees absentes de la configuration:", [k for k in GEL if k not in cf], "| inegalite sur cle gelee:", [k for k, _ in inegal if k in GEL])
for k, why in inegal:
    if k in GEL: arret("ecart-au-texte", "config " + k)
print("cles du manifeste en plus:", sorted(set(mc) - set(cf)))
print("manifeste config.go_id_attendu:", mc.get("go_id_attendu"))
print("manifeste sha:", sha(mf_p))
lt = json.load(open(P + "/diag/%s/lecture-t07.json" % RUN_T07, encoding="utf-8"))
r = lt["resultat"]
print("lecture-t07 run_id:", lt["run_id"] == RUN_T07, "| manifeste_sha256 = manifeste:", lt["manifeste_sha256"] == sha(mf_p),
      "| etape:", r["etape"], "| run_t07:", r["run_t07"] == RUN_T07, "| run_t06:", r["run_t06"] == RUN_T06)
print("fuites.audit.sha256 = pièce 13:", r["fuites"]["audit"]["sha256"] == sha(P + "/diag/%s/audit-fuites-t07.json" % RUN_T07))
bm = r["bases"]["mots_et_cout"].get("sha256")
print("bases.mots_et_cout.sha256 écrit:", bm is not None, "| égal pièce 12:", (bm == sha(P + "/" + issue_chemin)) if bm else None)
sc = r["scores"].get("sha256") if isinstance(r.get("scores"), dict) else None
print("scores.sha256 écrit:", sc is not None, "| égal ligne SCORES-T07:", (sc == L("SCORES-T07")[3]) if sc else None)
print("ouverture.manifeste.go_id:", r["ouverture"]["manifeste"]["go_id"], "| = go_id_attendu:", r["ouverture"]["manifeste"]["go_id"] == cf["go_id_attendu"])
bad34 = (lt["run_id"] != RUN_T07 or lt["manifeste_sha256"] != sha(mf_p) or r["etape"] != "B" or r["run_t07"] != RUN_T07 or r["run_t06"] != RUN_T06
         or r["fuites"]["audit"]["sha256"] != sha(P + "/diag/%s/audit-fuites-t07.json" % RUN_T07)
         or (bm and bm != sha(P + "/" + issue_chemin)) or (sc and sc != L("SCORES-T07")[3]) or r["ouverture"]["manifeste"]["go_id"] != cf["go_id_attendu"])
if bad34: arret("piece-non-conforme", "rattachement piece 14")
st = json.load(open(P + "/diag/%s/sondes-t07.json" % RUN_T07, encoding="utf-8"))
print("sondes-t07 run_id:", st["run_id"] == RUN_T07, "| manifeste_sha256 = manifeste:", st["manifeste_sha256"] == sha(mf_p))
if st["run_id"] != RUN_T07 or st["manifeste_sha256"] != sha(mf_p): arret("piece-non-conforme", "rattachement piece 15")
print("-- point 4 : lignes lues par le module")
gl = r["ouverture"]["garde"]["lignes"]
for k, v in sorted(gl.items()):
    if k not in reg or len(reg[k]) != 1: print(k, "absente de l'extrait"); continue
    c = L(k); ok = (v["date"] == c[1] and v["chemin"] == c[2] and v["sha256"] == c[3])
    print("garde.lignes", k, "= extrait (date, chemin, empreinte):", ok)
    if not ok and k in dix: arret("ecart-au-texte", "ligne lue " + k)
print("exigees:", r["ouverture"]["garde"]["exigees"])
print("garde.instant:", r["ouverture"]["garde"]["instant"], "= date ouverture etape B:", r["ouverture"]["garde"]["instant"] == dO)
if r["ouverture"]["garde"]["instant"] != dO: arret("ecart-au-texte", "instant")
ci = r.get("cles_ignorees")
print("cles_ignorees:", json.dumps(ci, ensure_ascii=False))
print("ARRETS:", ARRET)
sys.exit(1 if ARRET else 0)
