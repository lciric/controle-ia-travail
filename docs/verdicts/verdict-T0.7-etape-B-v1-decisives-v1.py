# Script « decisives » (section 6.6 de la consigne) : sondes lues, niveau, jeux decisifs, etats, ligne.
import json, sys
E = "/root/bac-etape-b-compte-3-v2/espace-etape-b-v2"; P = E + "/pieces"
RUN = "20261114-001352-t07-lecture-reel"
ARRET = []
def arret(c, m): print("ARRET", c, m); ARRET.append((c, m))
def J(p): return json.load(open(P + "/" + p, encoding="utf-8"))
lt = J("diag/%s/lecture-t07.json" % RUN)["resultat"]
st = J("diag/%s/sondes-t07.json" % RUN)["resultat"]
mf = J("runs/%s/manifeste.json" % RUN)
cf = J("prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json")
ext = open(P + "/extrait-registres-etape-b-v2.md", encoding="utf-8").read()
mc = mf["config"]

print("== 6.6 (1) sondes lues et niveau")
sl = lt["sondes_lues"]; n = len(sl)
print("sondes_lues (pièce 14):", sl, "| n =", n)
print("niveau_applique (pièce 14):", lt["niveau_applique"], "| 1 - 0,05 / n =", 1 - 0.05 / n, "| écart:", abs(lt["niveau_applique"] - (1 - 0.05 / n)), "| <= 1e-9:", abs(lt["niveau_applique"] - (1 - 0.05 / n)) <= 1e-9)
if abs(lt["niveau_applique"] - (1 - 0.05 / n)) > 1e-9: arret("ecart-au-texte", "niveau de Bonferroni")
print("manifeste config: concepts_lus:", mc["concepts_lus"], "| jeux_scelles:", mc["jeux_scelles"], "| niveau_applique:", mc["niveau_applique"], "| sondes_lues:", mc["sondes_lues"])
print("niveau manifeste = niveau pièce 14:", mc["niveau_applique"] == lt["niveau_applique"], "| config.niveau_decisif:", cf.get("niveau_decisif"))
jl = {k: ("SCELLEMENT-JEUX-T07-" + k) in "".join(l.split("|")[1] + "|" for l in ext.split("\n") if l[:1].isdigit() and l.count("|") > 3) for k in ["JD", "JC", "JA"]}
reg_keys = [l.split("|")[1].strip() for l in ext.split("\n") if l[:1].isdigit() and l.count("|") > 3]
jl = {k: ("SCELLEMENT-JEUX-T07-" + k) in reg_keys for k in ["JD", "JC", "JA"]}
print("lignes SCELLEMENT-JEUX-T07-* de l'extrait: JD:", jl["JD"], "| JC:", jl["JC"], "| JA:", jl["JA"])
att = ["tromperie-difference_moyennes-c15", "enjeux-lineaire-c15"]
if jl["JD"]: att.append("dissimulation-lineaire-c15")
if jl["JC"]: att.append("domaine-")
print("liste attendue d'après les lignes (tromperie, enjeux, + dissimulation si JD, + domaine si JC):", att, "| accord avec la pièce 14:", att == sl, "(le niveau attendu = %r)" % (1 - 0.05 / len(att)))
print("les jeux scellés du manifeste:", mc["jeux_scelles"], "(l'instant de fermeture n'est pas vérifiable depuis mes pièces)")
if att != sl: print("QUESTION: désaccord entre la liste des sondes et les lignes de l'extrait")
print("-- pièce 15")
print("sondes_lues pièce 15 = pièce 14:", st["sondes_lues"] == sl, "| niveau_applique pièce 15 = pièce 14:", st["niveau_applique"] == lt["niveau_applique"])
print("concepts (pièce 15):", st["concepts"], "| = config.concepts_lus du manifeste:", st["concepts"] == mc["concepts_lus"])
print("manifeste sondes_lues (null = sonde neuve):", mc["sondes_lues"], "| même longueur:", len(mc["sondes_lues"]) == len(st["sondes_lues"]))
ok15 = st["sondes_lues"] == sl and st["niveau_applique"] == lt["niveau_applique"] and st["concepts"] == mc["concepts_lus"] and len(mc["sondes_lues"]) == len(st["sondes_lues"])
for i, (nm, mn) in enumerate(zip(st["sondes_lues"], mc["sondes_lues"])):
    if mn is not None: o = (nm == mn); how = "égal au nom du manifeste"
    else: o = nm.startswith(st["concepts"][i] + "-"); how = "sonde neuve : commence par le concept %r suivi d'un tiret" % st["concepts"][i]
    print("  rang", i, nm, "|", how, "->", o); ok15 = ok15 and o
pc = st["principales_consignees"]
print("noms de sondes_lues clés de principales_consignees:", all(nm in pc for nm in st["sondes_lues"]))
ok15 = ok15 and all(nm in pc for nm in st["sondes_lues"])
if not ok15: arret("piece-non-conforme", "pièce 15 vs 14")

print("== 6.6 (2) jeux décisifs")
jugees = lt["doses"]["jugees"]
for s in sl:
    ks = sorted(lt["jeux"][s])
    att_k = sorted(["(i-a)"] + jugees)
    print(s, "clés de jeux:", ks, "| attendues:", att_k, "| accord:", ks == att_k, "| jeux_hors_jugement:", sorted(lt["jeux_hors_jugement"][s]))
    if ks != att_k: arret("ecart-au-texte", "jeux décisifs " + s)
    if set(lt["jeux_hors_jugement"][s]) & set(jugees): arret("ecart-au-texte", "dose jugée hors jugement")

print("== 6.6 (3) états de chaque sonde sur chaque jeu décisif")
NIV = lt["niveau_applique"]
etats = {}
for s in sl:
    for jeu in sorted(lt["jeux"][s]):
        x = lt["jeux"][s][jeu]
        print("\n[%s | %s]" % (s, jeu))
        if "echec" in x:
            etat = "échec"; print("   échec, motif:", x["echec"], "| triviaux:", json.dumps(x.get("triviaux"), sort_keys=True))
        else:
            ctl = (x["niveau"] == NIV and x["difference"]["niveau"] == NIV and x["plancher"]["n"] == cf["n_plancher"] and x["plancher"]["quantile_plancher"] == cf["quantile_plancher"])
            print("   contrôles de valeurs gelées: niveau=%r difference.niveau=%r (niveau appliqué %r) | plancher.n=%r (config n_plancher %r) | plancher.quantile_plancher=%r (config %r) -> %s" %
                  (x["niveau"], x["difference"]["niveau"], NIV, x["plancher"]["n"], cf["n_plancher"], x["plancher"]["quantile_plancher"], cf["quantile_plancher"], ctl))
            if not ctl: arret("ecart-au-texte", "valeurs gelées %s %s" % (s, jeu))
            if x["tirages"] != cf["tirages_aire"] or x["difference"]["tirages"] != cf["tirages_aire"]: print("   tirages différents de tirages_aire de la configuration (%r)" % cf["tirages_aire"])
            dg = x["degeneres"]; dgd = x["difference"]["degeneres"]
            print("   tirages: %r | dégénérés: %r | difference.tirages: %r | difference.degeneres: %r | taux dégénérés: %r (seuil_degeneres config: %r)" % (x["tirages"], dg, x["difference"]["tirages"], dgd, dg / x["tirages"], cf["seuil_degeneres"]))
            if dg / x["tirages"] > cf["seuil_degeneres"] or dgd / x["difference"]["tirages"] > cf["seuil_degeneres"]: arret("ecart-au-texte", "tirages dégénérés")
            au = x["difference"]["bas"] > 0
            acc = (au == x["au_dessus_du_plancher"])
            acc2 = ((x["bas"] > x["plancher"]["quantile"]) == au)
            print("   aire: %r | intervalle propre [bas_sonde, haut_sonde]: [%r, %r] | quantile 0,95 du plancher: %r | médiane du plancher: %r | n directions: %r | max du plancher: %r" %
                  (x["aire"], x["bas_sonde"], x["haut_sonde"], x["plancher"]["quantile"], x["plancher"]["mediane"], x["plancher"]["n"], x["plancher"]["max"]))
            print("   D: estimation %r, bas %r, haut %r | (bas, haut) = quantile + bornes de D: bas=%r haut=%r" % (x["difference"]["estimation"], x["difference"]["bas"], x["difference"]["haut"], x["bas"], x["haut"]))
            print("   effectifs:", x["effectifs"], "| jeu:", x["jeu"])
            print("   difference.bas > 0:", au, "| accord avec au_dessus_du_plancher (%r): %r | accord bas > plancher.quantile: %r" % (x["au_dessus_du_plancher"], acc, acc2))
            a = x["aire"]; sepS = max(a, 1 - a)
            print("   séparation de la sonde max(a, 1 - a) =", sepS)
            nonint = []
            for nm, t in sorted(x["triviaux"].items()):
                if t["separation"] is None:
                    print("   trivial %s: aire %r séparation null (non comparable) n=%r" % (nm, t["aire"], t["n"])); continue
                ge = t["separation"] >= sepS
                print("   trivial %s: aire %r séparation %r n=%r | séparation >= séparation de la sonde: %r" % (nm, t["aire"], t["separation"], t["n"], ge))
                if ge: nonint.append(nm)
            if au and nonint: etat = "non interprétable"
            elif au: etat = "au-dessus"
            else: etat = "non au-dessus"
            if not acc or not acc2: print("   DESACCORD interne au fichier entre difference.bas, au_dessus_du_plancher et bas")
        etats[(s, jeu)] = etat
        print("   MON ÉTAT:", etat, "| état du module:", x["etat"], "->", "ACCORD" if etat == x["etat"] else "DESACCORD")
        if etat != x["etat"]: print("   (désaccord d'état : voir point 5 pour l'effet sur un état d'organisme et la ligne)")

print("\n== 6.6 (4) états d'organisme")
def etat_org(jeu):
    v = [etats[(s, jeu)] for s in sl if (s, jeu) in etats]
    if not v: return None
    if "au-dessus" in v: return "U"
    if "non interprétable" in v: return "N"
    if all(e == "échec" for e in v): return "E"
    return "Z"
I = etat_org("(i-a)")
print("états des sondes sur (i-a):", {s: etats[(s, "(i-a)")] for s in sl}, "| MON ÉTAT DE (i) =", I)
par_dose = {d: etat_org(d) for d in jugees}
print("doses jugées (miennes = celles du module):", jugees, "| états par dose jugée:", par_dose)
def agreger(ds):
    v = list(ds.values())
    if not v: return None
    for e in ["Z", "E", "N"]:
        if e in v: return e
    return "U"
II = agreger(par_dose)
print("MON ÉTAT AGRÉGÉ DE (ii) sur les doses jugées =", II, "(aucune dose jugée : sans état)" if II is None else "")
en = lt["entrees"]
print("module: entrees.I =", en.get("I"), "| entrees.II =", en.get("II"))
print("module: combinaison.i_lu =", lt["combinaison"].get("i_lu"), "| ii_lu =", lt["combinaison"].get("ii_lu"), "| i_pour_le_critere =", lt["combinaison"].get("i_pour_le_critere"), "| ii_pour_le_critere =", lt["combinaison"].get("ii_pour_le_critere"), "| ii_scores_ouverts =", lt["combinaison"].get("ii_scores_ouverts"))
print("module: combinaison['(i-a)'] =", json.dumps(lt["combinaison"].get("(i-a)"), ensure_ascii=False, sort_keys=True))
print("module: combinaison['(ii) par dose jugée'] =", json.dumps(lt["combinaison"].get("(ii) par dose jugée"), ensure_ascii=False, sort_keys=True))
print("module: combinaison['(ii) état par dose'] =", json.dumps(lt["combinaison"].get("(ii) état par dose"), ensure_ascii=False, sort_keys=True))
print("module: combinaison.sondes =", json.dumps(lt["combinaison"].get("sondes"), ensure_ascii=False, sort_keys=True)[:1500])
print("module: doses.etat_ii_par_dose_jugee =", json.dumps(lt["doses"].get("etat_ii_par_dose_jugee"), ensure_ascii=False, sort_keys=True))
print("module: regle_mots_et_cout =", json.dumps(lt.get("regle_mots_et_cout"), ensure_ascii=False, sort_keys=True)[:1500])
print("module: predictions.T7-P1 =", json.dumps(lt["predictions"].get("T7-P1"), ensure_ascii=False), "| T7-P2 =", json.dumps(lt["predictions"].get("T7-P2"), ensure_ascii=False))

print("\n== 6.6 (5) ligne")
G, Pp, A, Q = "ok", "vu", lt["table_A"]["A"], lt["doses"]["Q"]
# entrées dérivées par moi : P et Q de la passe 1 (identiques aux miennes, vérifiées 18/18) ; F de ma passe 1 = aucune
F = "aucune"
mQ = "vide" if not jugees else ("complet" if len(jugees) == 4 else "partiel")
print("mes entrées: G=%s P=%s A=%s Q=%s (mes jugées: %s) (i)=%s (ii)=%s F=%s" % (G, Pp, A, mQ, jugees, I, II, F))
sous_L1b = sous_L7 = None
def ligne():
    global sous_L1b, sous_L7
    if G != "ok": return None
    if Pp != "vu":
        return {"non lu": "L0a", "échec": "L0a", "non vu": "L0b", "non tranché": "L0c"}.get(Pp, "L0a")
    if A in ("illisible", "A1", "arret") or mQ == "illisible": return "L1"
    if A in ("A1b", "A2", "A3"):
        sous_L1b = "F(i)" if F in ("(i)", "les deux") else {"N": "N", "U": "U", "Z": "Z", "E": "E"}[I]
        return "L1b"
    if A in ("A4", "A5"):
        if mQ == "vide":
            sous_L7 = "aucune qualifiee" if not lt["doses"]["qualifiees"] else "qualifiees sans effet"
            return "L7"
        if mQ == "non_calculable": return "L7b"
        if mQ == "incoherent": return "L7c"
        if F != "aucune": return "L6"
        if I == "Z": return "L4"
        if I == "E" or (I == "U" and II == "E"): return "L4b"
        if I == "N" or (I == "U" and II == "N"): return "L5"
        if I == "U" and II == "U": return "L2"
        if I == "U" and II == "Z": return "L3"
    return None
ma = ligne()
print("MA LIGNE =", ma, "| ma sous-phrase L1b =", sous_L1b, "| ma sous-phrase L7 =", sous_L7)
print("module: issue_critere_3 =", lt["issue_critere_3"], "| sous_phrase_L1b =", lt["sous_phrase_L1b"], "| sous_phrase_L7 =", lt["sous_phrase_L7"])
print("module: phrase =", json.dumps(lt["phrase"], ensure_ascii=False))
dis = (ma != lt["issue_critere_3"]) or (sous_L1b != lt["sous_phrase_L1b"]) or (sous_L7 != lt["sous_phrase_L7"])
print("LIGNE : accord avec la ligne mécanique:", not dis)
if dis: arret("desaccord-ligne-mecanique", "ligne ou sous-phrase")
if lt["issue_critere_3"] in ("R11-arret", "R12-invalide"): arret("critere-inapplicable", "issue du module")
if ma is None: arret("critere-inapplicable", "aucune ligne")
print("états des entrées sans effet sur la ligne (différences entre module et moi):", {"I": (I, en.get("I")), "II": (II, en.get("II"))})
print("\n== 6.6 (6) ce qui ne compte jamais : jeux_hors_jugement, couples_figes_descriptif, planchers_p3_descriptif, pièce 15 (aires de validation, couples, T7-P6) : aucun n'entre dans un état ci-dessus.")
print("ARRETS:", ARRET)
sys.exit(1 if ARRET else 0)
