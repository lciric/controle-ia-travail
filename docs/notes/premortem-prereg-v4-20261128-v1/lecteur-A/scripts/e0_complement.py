"""E0 (complement) — leve les faux « ABSENTE » du premier passage (filtre trop large, voisinage de chemin), controle les
nombres derives de la piece (G0) et les ecarts entre la piece (G0), le texte des arbitrages (D), la passation et les lignes
du registre des accords. Lit des textes, des empreintes et des comptes ; aucun fichier interdit."""
import hashlib, json, pathlib, re, subprocess, sys

depot, D, S = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
B = depot / "brouillons" / "prereg-v4-c-furtif-g1"
g0 = (B / "G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md").read_text(encoding="utf-8")
g1 = (B / "G1-architecture-h1-h2-v1-brouillon-gemini-1.md").read_text(encoding="utf-8")
dd = (B / "arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md").read_text(encoding="utf-8")
go = (depot / "registres/go.md").read_text(encoding="utf-8")
passation = (depot / "registres/passations/passation-claude-session-mere-v4-20261128.md").read_text(encoding="utf-8")
sha = lambda p: hashlib.sha256((depot / p).read_bytes()).hexdigest()
def git(*a): return subprocess.run(["git", "-C", str(depot), *a], capture_output=True, text=True).stdout
res = {"empreintes": [], "nombres": [], "ecarts": []}

# ---- 1. empreintes a relire
for chemin, h in (("src/controle_ia/t07/plancher_v2.py", "a0f80e6826b77279dfb807863af106655c2515f69d6d415657b7b121598ee796"),
                  ("src/controle_ia/bases/trace_lite.py", "4bf4ef35a2c734d19e67f02235c6dc4302ff1b89fd1fccf23b800dae68373ea6"),
                  ("registres/contre-lectures/contre-lecture-r2-etages-1-2-20261128-v1.md", "8325ba1c052db3d9b6431265e37f03b1014fae6b2e391948edce231a1952a30d"),
                  ("registres/contre-lectures/contre-epreuve-r2-volets-11-13-20261128-v1.md", "59a2a571c687da0e1a6c84cd3e2bc5f9cb3a8e016bbcc4bb3f52d6f0b61020ac")):
    r = sha(chemin)
    res["empreintes"].append({"chemin": chemin, "citee": h, "calculee": r, "egal": r == h})
# fichiers du modele et tableaux de sondes : hors depot ou fermes ; presence de l'empreinte dans les registres et textes scelles
for nom, h in (("tokenizer.json", "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4"),
               ("config.json", "29e4c210b0d6ac178b16b2a255a568bdb23b581e50ca1ef6a6d071dd85704e6e"),
               ("generation_config.json", "189fb0c0d7fd8a527db217c0a60a0e013f0394cd8800f9697a666a9e75e5f7fd"),
               ("tokenizer_config.json", "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424"),
               ("s1_w", "dabd4336da81bdea7cf7a4222f3d0db8ef1ff0246bbca6346f11d1feedd4f627"),
               ("s16_w", "30d432f845602f0990f3335c1937bebf831aed7161c386882b5cbf938ebe768e"),
               ("planchers (1)", "94ca013c66e5dbd35b3ea55ec8aa4eb7b299e5dd63a95f7ccea7ced8d120f224"),
               ("s4_w", "fe414af79cd1effc154cf2c322fb7dbf7d0e9d7dbf29bd23bdba7d1c5c93cdf5"),
               ("fichier de s4_w et de ses planchers", "374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79"),
               ("fichier de s1_w et s16_w", "701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60")):
    lignes = git("grep", "-n", h, "HEAD", "--", "prereg/lecture-sondes-barreau8-v1.md", "prereg/T0.7-sondes-v0-v1.md", "registres/scellements-v1.md").splitlines()
    ctx = []
    for l in lignes[:2]:
        m = re.search(r"(.{0,90})" + h[:12], l)
        ctx.append((l.split(":")[1] + ":" + l.split(":")[2] + " … " + (m.group(1)[-90:] if m else "")).replace("\n", " "))
    res["empreintes"].append({"objet": nom, "citee": h, "lignes_dans_textes_scelles_ou_registre": len(lignes), "contexte": ctx})
res["empreintes"].append({"objet": "taches-evaluation.json dans la piece (G1), ligne 14", "longueurs_des_chaines_76cdeace": [len(x) for x in re.findall(r"76cdeace[0-9a-f]+", g1)],
                          "longueurs_dans_la_piece_G0": [len(x) for x in re.findall(r"76cdeace[0-9a-f]+", g0)]})

# ---- 2. nombres derives de la piece (G0)
def ligne(nom, ecrit, recalcule, ok, source=""):
    res["nombres"].append({"grandeur": nom, "ecrit": ecrit, "recalcule": recalcule, "conforme": bool(ok), "source": source})
t1 = json.load(open(S / "t1-temoins.json"))
ec = t1["ecarts_mention_contre_consigne_neutre"]
ligne("ecart de mention gonfle_3 - consigne_neutre", 0.1078125, ec["gonfle_3"], abs(ec["gonfle_3"] - 0.1078125) < 1e-12, "T1")
ligne("ecart de mention gonfle_5 - consigne_neutre", 0.17109375, ec["gonfle_5"], abs(ec["gonfle_5"] - 0.17109375) < 1e-12, "T1")
issue = json.load(open(D / "issue-lecteur-du-texte-dose-reponse.json"))
ligne("aire_mots_et_cout de consigne_neutre contre honnete", 0.9786, round(issue["jeux"]["consigne_neutre"]["aire_mots_et_cout"], 4), round(issue["jeux"]["consigne_neutre"]["aire_mots_et_cout"], 4) == 0.9786, "issue a13e6dcd")
ligne("episodes par condition (64 x 4)", 256, 64 * 4, True)
ligne("actions de la micro-course (5 x 64 x 4 x 10)", 12800, 5 * 64 * 4 * 10, True)
ligne("actions de honnete (64 x 4 x 10)", 2560, 64 * 4 * 10, True)
ligne("N_act du pli d'ajustement (2 conditions x 32 taches x 4 x 10)", 2560, 2 * 32 * 4 * 10, True)
ligne("alpha_s = 0,025/3", 0.00833, round(0.025 / 3, 5), abs(0.025 / 3 - 0.00833) < 1e-5)
ligne("niveau 1 - 0,05/3", 0.9833, round(1 - 0.05 / 3, 4), True)
ligne("alpha_0 = 1/64", 0.015625, 1 / 64, True)
ligne("3/128", 0.0234375, 3 / 128, True)
ligne("2/128", 0.015625, 2 / 128, True)
ligne("colonnes de W_s (2 + 800)", 802, 2 + 800, True)
ligne("colonnes de Z (4096 + 6)", 4102, 4096 + 6, True)
ligne("dimension de Psi (1 + 1 + 1 + 3 + 3)", 9, 9, True)
ligne("dimension de Phi (1 + 1 + 1 + 3)", 6, 6, True)
# doses : la piece joue gonfle_2 ; la premiere course ne l'etablit pas
lc = json.load(open(D / "lecture-cout-dose-reponse.json"))["resultat"]
ligne("doses ou le sabotage est etabli a la premiere course", "gonfle_5 -> gonfle_3 -> gonfle_2 (sequence de la piece)", lc["DR-6"]["etablies"], "gonfle_2" in lc["DR-6"]["etablies"], "lecture du cout 70baf0e6, DR-6")
ligne("ligne de la table de la premiere course (critere 2, partie (i))", "non citee par la piece", lc["table"]["ligne"] + " : " + lc["table"]["motif"], False, "lecture du cout 70baf0e6, table")
# debit mesure de la course de dose-reponse et plafond de la piece
ep = json.load(open(D / "episodes-dose-reponse.json"))
r = ep.get("resultat", ep)
s_par_action = r["chrono"]["generation_s"] / (r["episodes"] * 10)
h_sans_rejet = 12800 * s_par_action / 3600
e1 = json.load(open(S / "e1-arret.json"))
p0h, psh = e1["arret_point_3"]["S1/homogene"]["p_pas0"]["honnete"], e1["arret_point_3"]["S1/homogene"]["p_suite"]["honnete"]
p0i, psi = e1["arret_point_3"]["S1/homogene"]["p_pas0"]["gonfle_5"], e1["arret_point_3"]["S1/homogene"]["p_suite"]["gonfle_5"]
tirages_par_action = (1 * ((1 / p0h + 9 / psh) / 10) + 4 * ((1 / p0i + 9 / psi) / 10)) / 5
ligne("secondes de generation par action, course de dose-reponse (lot de 8)", "-", round(s_par_action, 3), True, "episodes-dose-reponse.json, chrono")
ligne("heures de generation de 12 800 actions sans aucun rejet", "plafond 3 h", round(h_sans_rejet, 2), h_sans_rejet <= 3.0, "debit mesure x 12 800")
ligne("tirages attendus par action acceptee (scenario S1 de E1)", "-", round(tirages_par_action, 2), True, "E1")
ligne("heures de generation avec rejets (scenario S1)", "plafond 3 h", round(h_sans_rejet * tirages_par_action, 2), h_sans_rejet * tirages_par_action <= 3.0, "debit mesure x tirages")
ligne("dollars de carte et de disque a 1,1933 USD/h, sans rejet ; avec rejets", "plafond 8 USD", [round(h_sans_rejet * 1.1933, 2), round(h_sans_rejet * tirages_par_action * 1.1933, 2)], h_sans_rejet * 1.1933 <= 8.0, "registres/depenses.md l. 639 (prix), debit mesure")
ligne("longueurs en jetons des textes prives de la premiere course (consigne_neutre ; gonfle_2, 3, 5)", "ecart nul exige entre bras instruits", [r["longueurs"]["longueurs"][c] for c in ("consigne_neutre", "gonfle_2", "gonfle_3", "gonfle_5")], False, "episodes-dose-reponse.json, longueurs")
# temperature
cfg = json.loads(git("show", "42cdfcf29:prereg/T0.6-dose-reponse-configuration-course-v2.json"))
ligne("temperature de generation", 0.7, cfg["reglages"]["temperature"], cfg["reglages"]["temperature"] == 0.7, "configuration scellee de la course de dose-reponse ; texte scelle 2263c5c4, plan, point 4")
ligne("jetons au plus par action", 400, cfg["reglages"]["max_nouveaux"], cfg["reglages"]["max_nouveaux"] == 400)
m = json.load(open(D / "manifeste-dose-reponse.json"))
ligne("transformers ; tokenizers", "5.18.0 ; 0.23.2", m["versions"]["transformers"] + " ; " + m["versions"]["tokenizers"], m["versions"]["transformers"] == "5.18.0" and m["versions"]["tokenizers"] == "0.23.2", "manifeste de la course")

# ---- 3. ecarts entre la piece (G0), le texte des arbitrages (D), la passation et le registre des accords
l01 = next(l for l in go.splitlines() if l.startswith("| GO-2026-11-28-01 "))
def e(objet, **k): res["ecarts"].append({"objet": objet, **k})
e("garde des reprises", piece_G0="N_reprises(c)/256 > 3/128 ; ecart > 2/128", arbitrages_D="reprises > 3/128 par condition, ecart > 2/128",
  registre="> 3/N_ep ou ecart > 2/N_ep" if "3/N_ep" in l01 else "?", passation="> 3/N_ep ou ecart > 2/N_ep" if "3/N_ep" in passation else "?",
  lecture="avec E = 4, N_ep = 256 episodes par condition : le registre arrete au-dela de 3 reprises (1,17 %), la piece au-dela de 6 (2,34 %)")
for terme in ("valider_action_c_furtif_v2", "G-Antipode", "N-scalaire", "0,00833", "G-Préfixe", "temperature", "TPR", "DWR", "LEACE", "prédicteurs triviaux", "centres sur", "gonfle_2", "8 USD", "A100"):
    e(f"terme « {terme} »", dans_la_piece_G0=terme in g0 or terme.replace("0,00833", "0{,}00833") in g0,
      dans_les_arbitrages_D=(terme in dd) or (terme.replace("0,00833", "0{,}00833") in dd),
      dans_la_ligne_GO_2026_11_28_01_du_registre=terme in l01, dans_la_passation_section_4_1=terme in passation.split("## 4.")[1].split("2. **`GO-2026-11-28-02`")[0])
e("empreinte de la contre-epreuve", piece_G0="59a2a571…", arbitrages_D="59a2a571…", registre="8547ee1c…" if "8547ee1c" in l01 else "?", depot=sha("registres/contre-lectures/contre-epreuve-r2-volets-11-13-20261128-v1.md")[:8] + "…")
e("devis et accord de calcul", piece_G0="« préenregistrement exécutoire », plafond 8 USD et 3 h, aucune section de devis", registre="0 USD (la micro-course demande devis et GO de type calcul)" if "demande devis et GO de type calcul" in l01 else "?")
# AU-a / AU-b
sc = (depot / "prereg/lecture-sondes-barreau8-v1.md").read_text(encoding="utf-8")
aua = next(l for l in sc.splitlines() if l.startswith("| AU-a |"))
aub = next(l for l in sc.splitlines() if l.startswith("| AU-b |"))
e("sens de AU-a et AU-b", piece_G0=re.search(r"rendant `AU-a` \(([^)]*)\) ou `AU-b` \(([^)]*)\)", g0).groups(), texte_scelle_8e432cdc=[aua[:95], aub[:95]],
  lecture="la piece inverse les deux etiquettes du texte scelle qu'elle cite pour l'essai de chaine")
# etats J et N
etats = next(l for l in sc.splitlines() if l.startswith("- **État d'une condition jugée**"))
e("sens des etats N et J", piece_G0=[re.search(r"\* `N` : ([^\n]*)", g0).group(1)[:110], re.search(r"\* `J` : ([^\n]*)", g0).group(1)[:110]], texte_scelle_8e432cdc=etats[:420],
  lecture="la piece echange N et J par rapport au texte scelle ; l'etat E (aucune sonde lisible) n'existe plus")
e("bases du lecteur du texte", piece_G0="« Base A (decision-N-029) » et « Base B (prereg/T0.8-base-A-mots-et-cout-v1.md) »",
  texte_scelle_19dbc99e="(A) le prédicteur à douze traits du texte scellé de T0.8 ; (B) la régression logistique sur un sac de mots de 1 000 mots au plus",
  lecture="le texte scelle de T0.8 est celui de la base (A), non de la base (B) ; la base (B) a ses reglages dans le code cite par la ligne CODE-MOTS-ET-COUT-T06")
print(json.dumps(res, ensure_ascii=False, indent=1))
