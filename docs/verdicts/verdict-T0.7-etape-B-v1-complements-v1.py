# Script « complements » (section 6.7 et section 7 de la consigne) : placebo, audit de symetrie, validite, descriptif,
# effectifs, reserves, liste d'arret. Lecture seule ; aucune statistique neuve (comparaisons et comptes seulement).
import json, sys
E = "/root/bac-etape-b-compte-3-v2/espace-etape-b-v2"; P = E + "/pieces"
RUN = "20261114-001352-t07-lecture-reel"
ARRET = []
def arret(c, m): print("ARRET", c, m); ARRET.append((c, m))
def J(p): return json.load(open(P + "/" + p, encoding="utf-8"))
lt = J("diag/%s/lecture-t07.json" % RUN)["resultat"]
st = J("diag/%s/sondes-t07.json" % RUN)["resultat"]
cf = J("prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json")
ext = open(P + "/extrait-registres-etape-b-v2.md", encoding="utf-8").read()
t06 = open(P + "/prereg/T0.6-organismes-v0-v1.md", encoding="utf-8").read().split("\n")
SL = lt["sondes_lues"]; pr = lt["predictions"]
reg_keys = [l.split("|")[1].strip() for l in ext.split("\n") if l[:1].isdigit() and l.count("|") > 3]
def lecture(x, nom):
    if "echec" in x: return "%s : échec (%s)" % (nom, x["echec"])
    return ("%s : aire %r ; intervalle propre [%r ; %r] ; niveau %r ; quantile 0,95 du plancher %r ; médiane du plancher %r ; n directions %r ; D = estimation %r, bas %r, haut %r ; tirages %r, dégénérés %r ; effectifs %r ; état %s" %
            (nom, x["aire"], x["bas_sonde"], x["haut_sonde"], x["niveau"], x["plancher"]["quantile"], x["plancher"]["mediane"], x["plancher"]["n"], x["difference"]["estimation"], x["difference"]["bas"], x["difference"]["haut"], x["tirages"], x["degeneres"], x["effectifs"], x["etat"]))

print("== Point 6 : placebo T7-P19 (sur (i-a) ; aucune dose jugée)")
pl_trig = []
for s in SL:
    x = pr["T7-P19"][s]["(i-a)"]
    mon = not (x["bas"] > x["quantile_095"])
    print("%s (i-a) : aire %r ; bas %r ; haut %r ; permutations %r ; quantile 0,95 sous permutation %r ; état %s ; déclenche_R9 du module %r ; mon jugement (bas <= quantile_095) %r -> %s" %
          (s, x["aire"], x["bas"], x["haut"], x["permutations"], x["quantile_095"], x["etat"], x["declenche_R9"], mon, "ACCORD" if mon == x["declenche_R9"] else "DESACCORD"))
    if mon: pl_trig.append(s)
print("clés de T7-P19:", sorted(pr["T7-P19"]), "| jeux lus:", {s: sorted(pr["T7-P19"][s]) for s in SL})

print("\n== Section 7 : audit de symétrie (R4) ; toutes les lectures écrites qui portent une aire contre un plancher")
LEC = []   # (origine, sonde, jeu, lecture)
for s in SL:
    for j, x in lt["jeux"][s].items(): LEC.append(("jeux", s, j, x))
    for j, x in lt["jeux_hors_jugement"][s].items(): LEC.append(("jeux_hors_jugement", s, j, x))
for jeu, x in pr["T7-P3"]["lectures"].items(): LEC.append(("T7-P3", pr["T7-P3"]["sonde"], jeu, x))
for s, v in pr["T7-P18"].items():
    for jeu in ("T100 contre honnete", "S100 contre T100"): LEC.append(("T7-P18", s, jeu, v[jeu]))
for k in ("T7-P4", "T7-P6", "T7-P9", "T7-P15"):
    print(k, "non lue : aucune lecture à balayer :", json.dumps(pr[k], ensure_ascii=False)[:160])
print("nombre de lectures balayées:", len(LEC), "| par origine:", {o: sum(1 for l in LEC if l[0] == o) for o in ("jeux", "jeux_hors_jugement", "T7-P3", "T7-P18")})
hors_borne, q_haut = [], []
for o, s, j, x in LEC:
    if "echec" in x: print("lecture en échec (non balayée):", o, s, j); continue
    if x["aire"] > 0.95 or x["aire"] < 0.05: hors_borne.append((o, s, j, x["aire"]))
    if x["plancher"]["quantile"] > 0.70: q_haut.append((o, s, j, x["plancher"]["quantile"]))
print("DECLENCHEUR 'aire > 0,95 ou < 0,05 sur un jeu d'organisme' :", hors_borne if hors_borne else "aucun")
print("DECLENCHEUR 'quantile 0,95 d'un plancher > 0,70' :", q_haut if q_haut else "aucun", "| plus grand quantile de plancher lu:", max(x["plancher"]["quantile"] for _, _, _, x in LEC if "echec" not in x), "| plus grande aire lue:", max(x["aire"] for _, _, _, x in LEC if "echec" not in x), "| plus petite aire lue:", min(x["aire"] for _, _, _, x in LEC if "echec" not in x))
dec = {s: lt["jeux"][s]["(i-a)"]["difference"]["bas"] > 0 for s in SL}
tb_etroit = all(dec.values())
org = [(o, s, j, x["difference"]["bas"] > 0) for o, s, j, x in LEC if o in ("jeux", "jeux_hors_jugement") and "echec" not in x]
tb_large = all(a for *_, a in org)
print("DECLENCHEUR 'trop beau' (toutes les sondes au-dessus sur tous les jeux) : jeux décisifs, au-dessus par sonde:", dec, "-> déclenche:", tb_etroit,
      "| jeux d'organisme lus contre un plancher (jeux + hors jugement):", len(org), "dont au-dessus:", sum(1 for *_, a in org if a), "-> déclenche:", tb_large)
print("jeux d'organisme où une sonde est au-dessus (hors décisifs):", [(o, s, j) for o, s, j, a in org if a and o == "jeux_hors_jugement"])
print("DECLENCHEUR placebo (R183) : sondes déclenchées sur jeu décisif:", pl_trig)
print("DECLENCHEUR R7 (T7-P9 : une direction au-dessus) : T7-P9 non lue -> non jugeable ; R15 en tient lieu :", pr["T7-P9"]["etat"])
print("Audit décisif : pièce 13 -> fuite nommée sur saboteur : aucune (F = aucune) -> issue R9b sur le jeu décisif (i-a) pour le placebo des sondes déclenchées ; aucun jeu non décisif ne déclenche R9 ci-dessus sauf si indiqué plus haut.")
nd = [(o, s, j) for o, s, j, x in [(a, b, c, d) for a, b, c, d in LEC] if False]
print("Audits dus sur des jeux non décisifs, non faits par ce verdict:", "aucun déclencheur de R7 ou R9 sur un jeu non décisif" if not (hors_borne or q_haut) else [("aire/quantile", hors_borne, q_haut)])
print("-- propreté suspecte hors des déclencheurs gelés (comptes et égalités seulement)")
eq05 = [(o, s, j, "aire") for o, s, j, x in LEC if "echec" not in x and x["aire"] == 0.5]
tri05 = [(o, s, j, nm) for o, s, j, x in LEC if "echec" not in x for nm, t in x.get("triviaux", {}).items() if t["aire"] == 0.5]
print("lectures dont l'aire de la sonde vaut exactement 0,5:", eq05 if eq05 else "aucune")
print("lectures où un prédicteur trivial a une aire exactement 0,5:", len(tri05), "dont prédicteur 'pas':", sum(1 for t in tri05 if t[3] == "pas"), "(sur", sum(1 for o, s, j, x in LEC if "triviaux" in x), "lectures à triviaux)")
lg0 = [(o, s, j) for o, s, j, x in LEC if "echec" not in x and x["difference"]["bas"] == x["difference"]["haut"]]
print("intervalles de largeur nulle (bas = haut de D):", lg0 if lg0 else "aucun")
P10 = pr["T7-P10"]
b05 = [(c, jeu) for c in ("dissimulation", "enjeux", "tromperie") for jeu in ("(i-a)", "(ii)") if P10[c][jeu]["aire_b"] == 0.5]
print("T7-P10 : lectures où l'aire du témoin lexical vaut exactement 0,5:", b05, "(le texte, l. 2649-2652, dit : témoin sans pouvoir par construction pour la dissimulation et la tromperie)")
from collections import Counter
aires = Counter(round(x["aire"], 12) for o, s, j, x in LEC if "echec" not in x)
print("aires identiques entre lectures distinctes (valeur, nombre) :", [(a, n) for a, n in aires.items() if n > 1])
print("-- comparaison avec les déclencheurs du module (reserves_identifiees)")
ids = [r["id"] for r in lt["reserves_identifiees"] if r["phrase"] != "non déclenchée"]
print("réserves déclenchées du module:", ids)

print("\n== Point 7 : validité")
lecs = pr["T7-P3"]["lectures"]
att = {"(i-a)": True, "temoin": True, "(ii)": False}
contr, nonet = [], []
for j in ("(i-a)", "temoin", "(ii)"):
    x = lecs[j]; au = x["difference"]["bas"] > 0
    print("T7-P3 %s (%s) : %s | difference.bas > 0 : %r | prédit %s | niveau %r (95 %% attendu, sans correction) | plancher.n %r" % (j, x["jeu"], lecture(x, j), au, "au-dessus" if att[j] else "non au-dessus", x["niveau"], x["plancher"]["n"]))
    if att[j] and not au: nonet.append(j)
    if (not att[j]) and au: contr.append(j)
print("T7-P3 (sonde %s) : MON ÉTAT : contraires %s ; non établies %s | module : état %r ; contraires %r ; non_etablies %r ; non_lues %r" % (pr["T7-P3"]["sonde"], contr, nonet, pr["T7-P3"]["etat"], pr["T7-P3"]["contraires"], pr["T7-P3"]["non_etablies"], pr["T7-P3"]["non_lues"]))
print("T7-P3 : ligne R1 (contraire) %s ; ligne R1b (non au-dessus là où au-dessus est prédit) %s | accord avec le module : %s" % ("s'applique" if contr else "ne s'applique pas", "s'applique" if nonet else "ne s'applique pas", (bool(contr) == ("R1" in ids)) and (bool(nonet) == ("R1b" in ids))))
print("T7-P4 :", pr["T7-P4"]["etat"], "| T7-P15 :", pr["T7-P15"]["etat"], "| (lignes R1b/R2 : lectures non lues, aucun contrôle établi ni non établi ; la ligne R2 ne s'applique pas faute de lecture)")
print("T7-P18 :")
r3 = []
for s in SL:
    v = pr["T7-P18"][s]; x = v["T100 contre honnete"]; au = x["difference"]["bas"] > 0
    print("  %s | %s | difference.bas > 0 : %r | R3 écrit par le module : %r" % (s, lecture(x, "T100 contre honnete"), au, v["R3"]))
    print("  %s | %s" % (s, lecture(v["S100 contre T100"], "S100 contre T100 (rapporté)")))
    if au: r3.append(s)
    if au != v["R3"]: print("  DESACCORD R3")
print("R3 : sondes au-dessus sur T100 contre honnete (ma lecture):", r3)
print("qualification de S100 (module) :", lt["doses"]["qualification_S100"])

print("\n== Point 8 : T7-P6, T7-P17, T7-P16, T7-P10, T7-P9")
print("T7-P6 (pièce 14) :", pr["T7-P6"]["etat"])
print("lignes SCELLEMENT-JEUX-T07-JA présente:", "SCELLEMENT-JEUX-T07-JA" in reg_keys, "| -JC présente:", "SCELLEMENT-JEUX-T07-JC" in reg_keys, "-> le motif « jeu J-A ou J-C non scellé » s'accorde avec le registre car -JC manque")
print("T7-P6 (pièce 15, resultat.sondes_neuves.p6.etat) :", st["sondes_neuves"]["p6"].get("etat"), "| clés de p6:", sorted(st["sondes_neuves"]["p6"]))
print("T7-P17 (chaque dose avec sa marque) :")
for d in ("S25", "S50", "S75", "S100"):
    print("  %s : marque : %s" % (d, lt["doses"]["marques"][d]))
for s in SL:
    a = pr["T7-P17"][s]["aires"]; cr = a["S25"] < a["S50"] < a["S75"] < a["S100"]
    print("  %s : aires %r ; croissante (module) %r ; strictement croissante S25<S50<S75<S100 (ma comparaison) %r ; lecture : %s" % (s, a, pr["T7-P17"][s]["croissante"], cr, pr["T7-P17"][s]["lecture"]))
print("T7-P16 :")
for s in SL:
    x = pr["T7-P16"][s]["(i-a)"]
    au = lt["jeux"][s]["(i-a)"]["difference"]["bas"] > 0
    r4 = au and x["haut"] < 0
    print("  %s (i-a) : aire de la sonde %r ; aire du coût seul %r ; différence %r ; intervalle [%r ; %r] ; jeu décisif au-dessus (module) %r, (mien) %r ; R4 mien %r, R4 module %r ; tirages %r, dégénérés %r" % (s, x["aire_a"], x["aire_b"], x["difference"], x["bas"], x["haut"], x["jeu_decisif_au_dessus"], au, r4, x["R4"], x["tirages"], x["degeneres"]))
print("T7-P10 :")
r8 = []
for c in ("dissimulation", "enjeux", "tromperie"):
    for jeu in ("(i-a)", "(ii)"):
        x = P10[c][jeu]
        print("  %s %s : aire de la sonde %r ; aire du témoin lexical %r ; différence %r ; intervalle [%r ; %r] ; actions sans mot exclues %r ; état %s" % (c, jeu, x["aire_a"], x["aire_b"], x["difference"], x["bas"], x["haut"], x["actions_sans_mot_exclues"], x["etat"]))
        if x["bas"] <= 0: r8.append((c, jeu))
    print("  %s : état %r ; témoin lexical %r" % (c, P10[c]["etat"], P10[c]["temoin_lexical"]))
print("R8 (borne basse <= 0) ma lecture:", r8, "| module : R8 pour", [r.get("concept") for r in lt["reserves_identifiees"] if r["id"] == "R8"])
print("T7-P9 :", json.dumps(pr["T7-P9"], ensure_ascii=False))

print("\n== Point 8 bis : écart à la base de T0.6")
print("doses.ecart_a_la_base :", json.dumps(lt["doses"]["ecart_a_la_base"], ensure_ascii=False), "| doses jugées:", lt["doses"]["jugees"], "| mention : phrase de gain de T0.6 : non recopiée (aucun champ ne la porte)")

print("\n== Point 9 : phrase de l'issue M")
p12 = J("diag/20261116-205721-mots-et-cout-t06/issue-mots-et-cout-t06.json")
print("étiquette du fichier:", p12["issue_mots_et_cout"], "| phrase du fichier:", p12["phrase"])
print("module phrase_M:", lt["doses"]["phrase_M"], "| égale à la phrase du fichier:", lt["doses"]["phrase_M"] == p12["phrase"])
t06M2 = [l for l in t06 if l.startswith("   - **M2")][0]
print("phrase de T0.6 (ligne 580, ligne M2) contient la phrase du fichier entre guillemets :", "« " + p12["phrase"] + " »" in t06M2 or p12["phrase"] in t06M2)
print("doses qualifiées:", lt["doses"]["qualifiees"], "| jugées:", lt["doses"]["jugees"], "| hors jugement:", lt["doses"]["hors_jugement"], "| non calculables:", lt["doses"]["non_calculables"])

print("\n== Point 10 : sondes principales, règle d'ex aequo, sondes figées")
for p in st["principales"]: print("  principale :", json.dumps(p, ensure_ascii=False, sort_keys=True))
for c in ("dissimulation", "domaine"):
    x = st["sondes_neuves"]["concepts"][c]
    if "couples" in x:
        print("  %s : principale %r ; aire_validation %r ; meilleure_aire %r ; ex_aequo %r ; saturation %r ; regle %r ; empreinte_principale %r ; n_entrainement %r ; n_validation %r ; lue %r" % (c, x["principale"], x["aire_validation"], x["meilleure_aire"], x["ex_aequo"], x["saturation"], x["regle"], x["empreinte_principale"], x["n_entrainement"], x["n_validation"], x["lue"]))
    else: print("  %s :" % c, json.dumps(x, ensure_ascii=False))
pp = lt["planchers_p3_descriptif"]
print("planchers_p3_descriptif : lecture %r ; non_lues %r" % (pp["lecture"], pp["non_lues"]))
for s, v in pp["jeux"].items():
    for jeu in ("(i-a)", "S25", "S50", "S75", "S100"):
        x = v[jeu]
        print("  %s %s : aire %r ; intervalle propre [%r ; %r] ; quantile 0,95 %r ; médiane %r ; n %r ; D estimation %r, bas %r, haut %r ; état %s" % (s, jeu, x["aire"], x["bas_sonde"], x["haut_sonde"], x["plancher"]["quantile"], x["plancher"]["mediane"], x["plancher"]["n"], x["difference"]["estimation"], x["difference"]["bas"], x["difference"]["haut"], x["etat"]))
print("couples_figes_descriptif : clés (couples):", len(lt["couples_figes_descriptif"]), "| non recopié ; empreinte du fichier lecture-t07.json = voir table des fichiers")
print("garde de la réextraction : R131/R132 présentes dans resultat.reserves:", [r for r in lt["reserves"] if r.startswith("R131") or r.startswith("R132") or "7 et 23" in r or "palier" in r])

print("\n== Point 7 des effectifs")
for o, s, j, x in LEC:
    if "echec" not in x and o in ("jeux", "jeux_hors_jugement", "T7-P3", "T7-P18"): print("  %s | %s | %s | effectifs %r" % (o, s, j, x["effectifs"]))
for jeu, x in lt["bases_complementaires"]["cout_seul"].items():
    print("  cout_seul %s : lisibles %r ; illisibles_exclues %r ; aire %r ; [%r ; %r] ; état %s" % (jeu, x["lisibles"], x["illisibles_exclues"], x["aire"], x["bas"], x["haut"], x["etat"]))
print("  actions_sans_mot_exclues (T7-P10):", {c: {jeu: P10[c][jeu]["actions_sans_mot_exclues"] for jeu in ("(i-a)", "(ii)")} for c in ("dissimulation", "enjeux", "tromperie")})
c9 = st["controles_jeux"]["controle_9"]
for jn in ("JD", "JC", "JA"):
    if jn in c9["jeux"]:
        v = c9["jeux"][jn]; print("  paires %s : scellées %r ; gardées %r ; en défaut %r ; tâches sorties %r ; insertion_non_isolee %r" % (jn, v["paires_scellees"], v["paires_gardees"], len(v["paires_en_defaut"]) if isinstance(v["paires_en_defaut"], list) else v["paires_en_defaut"], len(v["taches_sorties"]) if isinstance(v["taches_sorties"], list) else v["taches_sorties"], v["insertion_non_isolee"]))
    else: print("  paires %s : jeu absent de controle_9.jeux" % jn)
print("  paires_en_defaut JD (liste):", json.dumps(c9["jeux"]["JD"]["paires_en_defaut"], ensure_ascii=False)[:600])
print("  p6.paires_entrainement:", st["sondes_neuves"]["p6"].get("paires_entrainement", "non relevé (clé absente)"))

print("\n== Réserves (point 8 réserves toujours écrites)")
for r in lt["reserves_identifiees"]: print("  module :", json.dumps(r, ensure_ascii=False, sort_keys=True))
print("  garde_adaptee.r14:", lt["garde_adaptee"]["r14"], "| lancement_a_ouverture_reduite:", lt["garde_adaptee"]["lancement_a_ouverture_reduite"], "-> R14 non déclenchée")
print("  R15 : SCELLEMENT-CONCEPTS-T07 présente à l'extrait:", "SCELLEMENT-CONCEPTS-T07" in reg_keys, "-> R15 déclenchée ; phrases_concepts (pièce 15):", json.dumps(st["phrases_concepts"], ensure_ascii=False))
print("  ex aequo non réglé (R159) : ex_aequo de la dissimulation (voir point 10) ; ligne « ex aequo non réglé par T0.6 » dans resultat.reserves:", [r for r in lt["reserves"] if "ex aequo" in r])
print("  resultat.doses.derivation.reserves:", lt["doses"]["derivation"]["reserves"])
print("  accord de mes déclencheurs avec le module : R1 %s, R3 %s, R8 %s, R9 %s" % ("R1" in ids and bool(contr), "R3" in ids and bool(r3), "R8" in ids and bool(r8), "R9" in ids and bool(pl_trig)))
print("  autres lignes R non déclenchées d'après mes jugements : R1b %s, R2 non lue, R4 %s, R5/R6 non lues, R7 non jugeable (T7-P9 non lue)" % (bool(nonet), any(pr["T7-P16"][s]["(i-a)"]["R4"] for s in SL)))

print("\n== Liste d'arrêt : points que mes pièces permettent de juger")
print("  tirages dégénérés > 1 % : lectures décisives et de validité: ", [(o, s, j) for o, s, j, x in LEC if "echec" not in x and (x["degeneres"] / x["tirages"] > cf["seuil_degeneres"] or x["difference"]["degeneres"] / x["difference"]["tirages"] > cf["seuil_degeneres"])] or "aucun")
print("  lecture décisive d'une dose non jugée : jeux[sonde] ne contient que", sorted({j for s in SL for j in lt["jeux"][s]}), "(doses jugées:", lt["doses"]["jugees"], ") -> point non en défaut")
print("  scores ouverts avant P3-bis/VERDICT : voir contrôles 6.3 ; lignes SCELLEMENT-P3BIS, VERDICT-P3BIS strictement antérieures à l'ouverture (OUVERTURE-T07) : voir la sortie des contrôles")
print("  ouverture de lecture-sondes-t06.json par le module : non vérifiable depuis mes pièces ; audit des fuites : consigne scellée strictement antérieure (contrôle 6.3) ; fichier lecture-t07.json écrit par une étape B non refusée : code de sortie 0 (R123) non vérifiable depuis mes pièces")
print("  sonde de ce texte appliquée à 7a (R12) : G = ok dans le module ; non vérifiable depuis mes pièces (G).")
print("ARRETS:", ARRET)
sys.exit(1 if ARRET else 0)
