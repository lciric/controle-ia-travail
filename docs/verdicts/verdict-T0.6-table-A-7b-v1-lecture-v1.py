import json
P = "/root/bac-lecture-7b-compte-3-v2/espace-table-a-v2/pieces"
RUN = "20261111-151701-t06-reel"
d = json.load(open(P + "/diag/%s/lecture-cout-t06.json" % RUN, encoding="utf-8"))["resultat"]
L = d["lecture"]
def show(titre, v):
    print("== " + titre)
    print(json.dumps(v, ensure_ascii=False, indent=1, sort_keys=True))
print("cles resultat:", sorted(d))
print("cles lecture:", sorted(L))
show("T6-1", L["T6-1"])
show("T6-2", L["T6-2"])
show("T6-10", L["T6-10"])
show("T6-8", L["T6-8"])
show("audit_R4_cout", L["audit_R4_cout"])
show("table_A (ligne mécanique de la chaîne)", L["table_A"])
show("reserves (chaîne)", L["reserves"])
show("effectifs", d["effectifs"])
show("lecteur", d.get("lecteur"))
show("note", d.get("note"))
ep = json.load(open(P + "/diag/%s/episodes-t06.json" % RUN, encoding="utf-8"))["resultat"]
print("cles episodes:", sorted(ep))
show("episodes effectifs", ep["effectifs"])
show("episodes controles_negatifs", ep["controles_negatifs"])
show("episodes etats", ep["etats"])
di = json.load(open(P + "/diag/%s/distillation-t06.json" % RUN, encoding="utf-8"))["resultat"]
print("cles distillation:", sorted(di))
show("distillation donnees", di["donnees"])
