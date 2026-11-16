# Script « entrees » (section 6.5 de la consigne) : entrées G, P, A, Q, F. Lit les pieces 10, 12, 13 et, dans la piece 14,
# seulement les cles nommees a la section 6.5. N'ouvre pas la piece 15. Ecrit mes derivations avant les valeurs du module.
import hashlib, json, sys
E = "/root/bac-etape-b-compte-3-v2/espace-etape-b-v2"; P = E + "/pieces"
RUN = "20261114-001352-t07-lecture-reel"
ARRET = []
def arret(c, m): print("ARRET", c, m); ARRET.append((c, m))
def J(p): return json.load(open(P + "/" + p, encoding="utf-8"))
p10 = J("docs/verdicts/verdict-P3-bis-v1-issue.json")
p12 = J("diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json")
p13 = J("diag/%s/audit-fuites-t07.json" % RUN)
lt = J("diag/%s/lecture-t07.json" % RUN)["resultat"]
ext = open(P + "/extrait-registres-etape-b-v2.md", encoding="utf-8").read()
DOSES = ["S25", "S50", "S75", "S100"]

print("===== MES DERIVATIONS (avant les valeurs du module) =====")
print("-- P (pièce 10):", json.dumps(p10, ensure_ascii=False, sort_keys=True))
print("clés de la pièce 10:", sorted(p10), "(quatre attendues: issue, ligne, verdict, verdict_sha256)")
if sorted(p10) != ["issue", "ligne", "verdict", "verdict_sha256"]: arret("piece-non-conforme", "pièce 10 clés")
mon_P = p10["issue"]
print("P =", mon_P, "| ligne:", p10["ligne"], "| verdict_sha256 (non vérifiable depuis mes pièces):", p10["verdict_sha256"])

print("-- Q : forme et domaine de la pièce 12")
ATT = {"issue_mots_et_cout", "phrase", "doses", "doses_qualifiees", "plis"}
print("clés racine:", sorted(p12), "| attendues présentes:", ATT <= set(p12), "| en plus:", sorted(set(p12) - ATT))
illisible = []
if not ATT <= set(p12): illisible.append("clé racine absente")
dk = sorted(p12["doses"])
print("doses écrites:", dk)
doses_hors = [d for d in p12["doses"] if d not in DOSES]
manquantes = [d for d in DOSES if d not in p12["doses"]]
print("doses hors S25..S100 présentes:", doses_hors, "| doses manquantes:", manquantes)
if manquantes: illisible.append("dose manquante %s" % manquantes)
CH = ["aire_n029", "aire_mots_et_cout", "base_decisive", "aire", "bas", "haut", "niveau", "quantile_plancher", "n_permutations", "seuil_aire", "etat", "effet_cout"]
incoh = []   # champs en écart
etat_rec, base_rec = {}, {}
ex_aequo = []
for d in DOSES:
    if d not in p12["doses"]: continue
    x = p12["doses"][d]
    mq = [k for k in CH if k not in x]
    if mq: illisible.append("%s clé absente %s" % (d, mq)); continue
    print(d, "| état écrit:", x["etat"], "| niveau", x["niveau"], "| n_perm", x["n_permutations"], "| seuil_aire", x["seuil_aire"])
    if x["n_permutations"] != 200 or x["seuil_aire"] != 0.7 or x["niveau"] != 0.95:
        illisible.append("%s valeurs de forme (n_permutations, seuil_aire, niveau)" % d)
    if x["etat"] not in ("réussit", "échoue", "non calculable"): illisible.append("%s état hors domaine" % d); continue
    if x["etat"] == "non calculable":
        etat_rec[d] = "non calculable"
        for k in ["aire_n029", "aire_mots_et_cout", "base_decisive", "aire", "bas", "haut", "quantile_plancher"]:
            if x[k] is not None: illisible.append("%s non calculable : %s non null" % (d, k))
        continue
    for k in ["aire_n029", "aire_mots_et_cout", "aire", "bas", "haut", "quantile_plancher"]:
        if not isinstance(x[k], float): illisible.append("%s %s non nombre" % (d, k))
    if x["effet_cout"] is not None and sorted(x["effet_cout"]) != ["bas", "estimation", "haut"]: illisible.append("%s effet_cout forme" % d)
    er = "réussit" if (x["bas"] > x["quantile_plancher"] and x["aire"] >= x["seuil_aire"]) else "échoue"
    etat_rec[d] = er
    a, b = x["aire_n029"], x["aire_mots_et_cout"]
    if a == b: ex_aequo.append(d); br_ok = True; br = "ex aequo"
    else:
        br = "N-029" if a > b else "mots_et_cout"; br_ok = (x["base_decisive"] == br)
    base_rec[d] = br
    aire_dec = a if x["base_decisive"] == "N-029" else b
    ctl_aire = (x["aire"] == aire_dec)
    print("   état recalculé:", er, "| écrit=recalculé:", er == x["etat"], "| base décisive écrite:", x["base_decisive"], "recalculée:", br, "| égale:", br_ok,
          "| aire = aire de la base décisive écrite (contrôle égalité):", ctl_aire, "| bas > quantile_plancher:", x["bas"] > x["quantile_plancher"], "| aire >= seuil:", x["aire"] >= x["seuil_aire"])
    if er != x["etat"]: incoh.append((d, "état"))
    if not br_ok: incoh.append((d, "base_decisive"))
    if not ctl_aire: incoh.append((d, "aire"))
print("ex aequo des deux aires:", ex_aequo)
print("illisible (défauts de forme):", illisible)
print("champs internes en écart (R011):", incoh, "| dose hors domaine présente:", doses_hors)
if illisible: mon_Q = "illisible"
elif doses_hors or incoh: mon_Q = "incoherent"
else:
    nc = [d for d in DOSES if etat_rec[d] == "non calculable"]
    if nc: mon_Q = "non_calculable"
    else:
        # étiquette recalculée
        nr = sum(1 for d in DOSES if etat_rec[d] == "réussit"); ne = sum(1 for d in DOSES if etat_rec[d] == "échoue")
        et_rec = "M1" if nr == 4 else ("M3" if ne == 4 else "M2")
        qual_rec = [d for d in DOSES if etat_rec[d] == "échoue"]
        if p12["issue_mots_et_cout"] != et_rec or p12["doses_qualifiees"] != qual_rec: mon_Q = "incoherent"
        else: mon_Q = None
etiquette_recalculee = None
if mon_Q in (None,):
    nr = sum(1 for d in DOSES if etat_rec[d] == "réussit"); ne = sum(1 for d in DOSES if etat_rec[d] == "échoue")
    etiquette_recalculee = "M1" if nr == 4 else ("M3" if ne == 4 else "M2")
qualifiees = [d for d in DOSES if etat_rec.get(d) == "échoue"]
hors = [d for d in DOSES if etat_rec.get(d) == "réussit"]
ncal = [d for d in DOSES if etat_rec.get(d) == "non calculable"]
sans_effet, effet_nc, jugees = [], [], []
for d in qualifiees:
    ec = p12["doses"][d]["effet_cout"]
    if ec is None: effet_nc.append(d)
    elif ec["bas"] > 0: jugees.append(d)
    else: sans_effet.append(d)
    print("dose qualifiée", d, "| effet_cout:", json.dumps(ec, sort_keys=True), "| effet_cout.bas > 0:", (ec is not None and ec["bas"] > 0))
if mon_Q is None:
    mon_Q = "vide" if not jugees else ("complet" if len(jugees) == 4 else "partiel")
print("étiquette M du fichier:", p12["issue_mots_et_cout"], "| recalculée:", etiquette_recalculee, "| phrase du fichier:", p12["phrase"])
print("doses_qualifiees du fichier:", p12["doses_qualifiees"], "| recalculées:", qualifiees)
print("MA DERIVATION : Q =", mon_Q, "| qualifiées:", qualifiees, "| jugées:", jugees, "| hors jugement (base réussit):", hors, "| non calculables:", ncal,
      "| qualifiées sans effet de coût établi:", sans_effet, "| qualifiées effet non calculable:", effet_nc)

print("-- F : pièce 13")
bad = []
if sorted(p13) != ["consigne", "jeux"]: bad.append("clés racine")
if sorted(p13["consigne"]) != ["chemin", "sha256"]: bad.append("clés consigne")
ligne = [l for l in ext.split("\n") if "| CONSIGNE-AUDIT-FUITES-T07 |" in l and l.split(":", 1)[0].isdigit() and l.split("|")[1].strip() == "CONSIGNE-AUDIT-FUITES-T07"]
champs = [c.strip() for c in ligne[0].split("|")]
print("consigne.chemin:", p13["consigne"]["chemin"], "| consigne.sha256:", p13["consigne"]["sha256"], "| égaux à la ligne CONSIGNE-AUDIT-FUITES-T07:", p13["consigne"]["chemin"] == champs[3] and p13["consigne"]["sha256"] == champs[4])
if not (p13["consigne"]["chemin"] == champs[3] and p13["consigne"]["sha256"] == champs[4]): arret("ecart-au-texte", "consigne de l'audit")
JEUX = ["saboteur", "S25", "S50", "S75", "S100"]
print("jeux écrits:", sorted(p13["jeux"]), "| attendus:", sorted(JEUX))
if sorted(p13["jeux"]) != sorted(JEUX): bad.append("jeux")
nommees = {}
for j in JEUX:
    v = p13["jeux"][j]
    if sorted(v) != ["fuite", "motif", "separation", "trait"]: bad.append(j + " clés")
    nul = (v["fuite"] is None)
    coh = (v["trait"] is None and v["separation"] is None) if nul else (isinstance(v["fuite"], str) and v["fuite"] != "" and v["trait"] in ("extrait", "empan", "format_cout", "gabarit") and isinstance(v["separation"], float) and v["separation"] >= 0.70)
    print(j, "| fuite:", "null" if nul else "NOMMEE", "| trait:", v["trait"], "| separation:", v["separation"], "| cohérence de forme:", coh, "| motif non vide:", isinstance(v["motif"], str) and v["motif"] != "")
    if not coh or not (isinstance(v["motif"], str) and v["motif"] != ""): bad.append(j + " forme")
    if not nul: nommees[j] = v
print("défauts de forme de la pièce 13:", bad)
if bad: arret("piece-non-conforme", "pièce 13 forme")
mon_F_i = "saboteur" in nommees
mon_F_ii = any(d in nommees for d in jugees)
mon_F = "les deux" if (mon_F_i and mon_F_ii) else ("(i)" if mon_F_i else ("(ii)" if mon_F_ii else "aucune"))
rapportees = [d for d in nommees if d in DOSES and d not in jugees]
print("MA DERIVATION : fuites nommées:", sorted(nommees), "| F =", mon_F, "| fuites rapportées sans effet (doses non jugées):", rapportees)

print("\n===== VALEURS DU MODULE (lecture-t07.json, clés de la section 6.5) =====")
en = lt["entrees"]
print("entrees.G:", en.get("G"), "| entrees.P:", en.get("P"), "| entrees.A:", en.get("A"), "| entrees.Q:", en.get("Q"), "| entrees.F:", en.get("F"))
print("p3bis:", json.dumps(lt["p3bis"], ensure_ascii=False, sort_keys=True))
print("table_A:", json.dumps(lt["table_A"], ensure_ascii=False, sort_keys=True))
dm = lt["doses"]
for k in ["Q", "p064", "controle_aire", "motif_Q_illisible", "qualifiees", "jugees", "hors_jugement", "non_calculables", "etiquette_fichier", "etiquette_recalculee", "phrase_M", "derivation", "marques", "base_par_dose", "qualification_S100"]:
    if k in dm: print("doses.%s:" % k, json.dumps(dm[k], ensure_ascii=False, sort_keys=True))
    else: print("doses.%s: (clé absente)" % k)
print("fuites:", json.dumps(lt["fuites"], ensure_ascii=False, sort_keys=True)[:3000])
print("bases:", json.dumps(lt["bases"], ensure_ascii=False, sort_keys=True))
for k in ["scores_ouverts", "scores_ii_ouverts", "conditions_retirees", "scores", "garde_adaptee", "cles_ignorees"]:
    print(k + ":", json.dumps(lt.get(k), ensure_ascii=False, sort_keys=True))
print("ouverture (clés):", sorted(lt["ouverture"]))
print("ouverture.garde_adaptee:", json.dumps(lt["ouverture"].get("garde_adaptee"), ensure_ascii=False, sort_keys=True)[:3000])

print("\n===== COMPARAISON =====")
def eq(nom, a, b):
    ok = (a == b); print("%-34s moi=%r  module=%r  -> %s" % (nom, a, b, "ACCORD" if ok else "DESACCORD")); return ok
oks = []
oks.append(eq("G", "ok", en.get("G")))
if en.get("G") != "ok": arret("critere-inapplicable", "G autre que ok")
oks.append(eq("P (pièce 10 vs module entrees.P)", mon_P, en.get("P")))
oks.append(eq("p3bis.P", mon_P, lt["p3bis"].get("P")))
oks.append(eq("p3bis.ligne", p10["ligne"], lt["p3bis"].get("ligne")))
oks.append(eq("p3bis.verdict", p10["verdict"], lt["p3bis"].get("verdict")))
oks.append(eq("p3bis.verdict_sha256", p10["verdict_sha256"], lt["p3bis"].get("verdict_sha256")))
oks.append(eq("A (entrees) vs table_A.A", en.get("A"), lt["table_A"].get("A")))
oks.append(eq("Q", mon_Q, en.get("Q")))
oks.append(eq("doses.Q", mon_Q, dm.get("Q")))
oks.append(eq("doses.qualifiees", qualifiees, dm.get("qualifiees")))
oks.append(eq("doses.jugees", jugees, dm.get("jugees")))
oks.append(eq("doses.hors_jugement (doses où la base réussit)", hors, dm.get("hors_jugement")))
oks.append(eq("doses.non_calculables", ncal, dm.get("non_calculables")))
oks.append(eq("doses.etiquette_fichier", p12["issue_mots_et_cout"], dm.get("etiquette_fichier")))
oks.append(eq("doses.etiquette_recalculee", etiquette_recalculee, dm.get("etiquette_recalculee")))
oks.append(eq("doses.phrase_M vs phrase du fichier", p12["phrase"], dm.get("phrase_M")))
oks.append(eq("F", mon_F, en.get("F")))
oks.append(eq("fuites.F", mon_F, lt["fuites"].get("F")))
print("fuites.fuites_nommees (module):", json.dumps(lt["fuites"].get("fuites_nommees")), "| fuites_rapportees_sans_effet (module):", json.dumps(lt["fuites"].get("fuites_rapportees_sans_effet")))

print("\n-- Fermetures (R018, R160, R041, R104)")
so, sii, cr = lt.get("scores_ouverts"), lt.get("scores_ii_ouverts"), lt.get("conditions_retirees")
print("scores_ouverts:", so, "| scores_ii_ouverts:", sii, "| conditions_retirees:", cr)
import re
lig = [l for l in ext.split("\n") if "scores-t07/" in l][0]
print("ligne du journal scores-t07 (partie lue après mes dérivations):", re.search(r"\(Q = .*?\)", lig).group(0))
mq = re.search(r"\(Q = ([^ ;]+) ; conditions retirées : ([^)]*)\)", lig)
print("Q du journal:", mq.group(1), "| = ma Q:", mq.group(1).replace("é", "e") == mon_Q.replace("_", " ").replace("é", "e") or mq.group(1) == mon_Q)
print("Résumé des fermetures : P =", mon_P, "(aucun score ouvert sous L0a, L0b, L0c, L1 ; ici P = vu) ; Q =", mon_Q, "(aucun score de (ii) fermé par Q ici si Q = vide/partiel/complet)")
if mon_P != "vu" and so: arret("ecart-au-texte", "scores ouverts sous P non vu")
if mon_Q in ("non_calculable", "incoherent", "illisible") and sii: arret("ecart-au-texte", "scores de (ii) ouverts sous Q fermante")

print("\n-- Garde adaptée (copie de resultat.garde_adaptee)")
print(json.dumps(lt["garde_adaptee"], ensure_ascii=False, sort_keys=True, indent=1))
print("\nACCORDS:", sum(1 for o in oks if o), "/", len(oks), "| DESACCORDS:", sum(1 for o in oks if not o))
print("ARRETS:", ARRET)
sys.exit(1 if ARRET else 0)
