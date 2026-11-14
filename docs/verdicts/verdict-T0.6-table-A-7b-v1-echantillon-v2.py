import hashlib, json, numpy
P = "/root/bac-lecture-7b-compte-3-v2/espace-table-a-v2/pieces"
RUN = "20261111-151701-t06-reel"
cfg = json.load(open(P + "/prereg/T0.6-organismes-config-7b-v1.json", encoding="utf-8"))
def trouve(o, k):
    if isinstance(o, dict):
        if k in o: return o[k]
        for v in o.values():
            r = trouve(v, k)
            if r is not None: return r
    return None
mx = trouve(cfg, "max_nouveaux")
print("max_nouveaux de la configuration:", mx)
z = numpy.load(P + "/donnees/%s/mesures-t06.npz" % RUN, allow_pickle=False)
cle = [str(x) for x in z["cle"]]
cond = [str(x) for x in z["condition"]]
jet = z["jetons"]
cout = z["cout"]
conds = ["honnete", "saboteur", "temoin", "mention", "S25", "S50", "S75", "S100", "T100"]
print("== lignes par condition et actions à la borne de %s jetons (tronquées, ou finies juste à la borne)" % mx)
for c in conds:
    idx = [i for i in range(len(cond)) if cond[i] == c]
    print("%s: lignes=%d à_la_borne=%d" % (c, len(idx), sum(1 for i in idx if int(jet[i]) >= int(mx))))
print("conditions présentes:", sorted(set(cond)))
# tirage
ss = numpy.random.SeedSequence(int(hashlib.sha256("T0.6 table A 7b, échantillon de l'audit R4, v1".encode("utf-8")).hexdigest(), 16))
enfants = ss.spawn(3)
tires = []
for c, e in zip(["honnete", "S100", "T100"], enfants):
    cles = sorted(cle[i] for i in range(len(cond)) if cond[i] == c)
    ch = numpy.random.default_rng(e).choice(len(cles), size=min(10, len(cles)), replace=False)
    for j in ch:
        tires.append((c, cles[int(j)]))
print("== clés tirées (avant ouverture du fichier des textes)")
for c, k in tires:
    print(c, k)
cout_de = {}
for i in range(len(cle)):
    cout_de[cle[i]] = cout[i]
gardes = {k for _, k in tires}
textes = {}
with open(P + "/donnees/%s/textes-actions-t06.jsonl" % RUN, encoding="utf-8") as f:
    for ligne in f:
        o = json.loads(ligne)
        if o["cle"] in gardes:
            textes[o["cle"]] = o["texte"]
print("== extraits (au plus 160 caractères, fin du texte et mentions du coût)")
import re
for c, k in tires:
    t = textes.get(k)
    if t is None:
        print("%s | %s | texte absent" % (c, k)); continue
    m = [x for x in re.finditer(r"(?i)cost|budget|compute|gpu|hours?", t)]
    if m:
        a = max(0, m[-1].start() - 40)
        ext = t[a:a + 160]
    else:
        ext = t[-160:]
    print("%s | %s | cout_chaine=%r | longueur_texte=%d | extrait=%r" % (c, k, cout_de.get(k), len(t), ext))
