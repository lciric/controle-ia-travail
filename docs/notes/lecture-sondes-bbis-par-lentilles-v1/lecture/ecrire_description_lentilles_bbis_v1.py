import json, sys
D = "docs/notes/lecture-sondes-bbis-par-lentilles-v1"
L = sys.argv[1]
t = json.load(open(f"{L}/entree/tables-lentilles-bbis.json", encoding="utf-8"))
r = json.load(open(f"{D}/lecture/comparaison-phrases-lecteur-code-v1.json", encoding="utf-8"))
code = json.load(open(f"{D}/lecture/phrases-code-lentilles-bbis-v1.json", encoding="utf-8"))
mes = {x["cle"]: x for x in r["table"]}
VERDICT = "- **Reproduction (B-2 et B-3) : « partiel ».** Aucune chaîne en défaut, aucun audit de symétrie gelé déclenché."
TETE = code["tete"].split(" Verdict d'ensemble")[0]
nb = lambda x: f"{x:.4g}".replace(".", ",")
o = []
w = o.append
w("# Description de la lecture des directions des sondes de l'étape B bis par la lentille publique — première passe — v1\n")
w("- **Lecteur neuf** (session fille de la mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1`), sur le mandat `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-lecteur-lecture-sondes-bbis-par-lentilles-v1.md` (`4acd4529…`). N'a lu aucun résultat de l'apprentissage des sondes sur la tâche (score, aire, issue, verdict) ; ni auteur, développeur ni opérateur du texte.")
w("- **Texte appliqué** : `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`) et son addendum de concentration `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md` (`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`), lus en entier ; « Critères de lecture gelés » appliqués à la lettre.")
w("- **Tables lues** : `diag/20261121-193607-lentilles-bbis-v1/tables-lentilles-bbis.json` (`25ea42f89ea208ad35b8e2feb2f7b6f88a917f6cf1190b5d8f5ac4b56748806a`), branche `calcul/lentilles-sondes-bbis-v1` à `b23472fe…`, égal au compagnon et aux lignes `TABLES-` et `OUVERTURE-LENTILLES-BBIS` (inscrite par la mère, commit `dbec6d91`). Les morceaux `lectures-lentilles-bbis-00{0,1}.npz` n'ont pas été ouverts (empreintes seules).")
w("- **Phrases du code** : `diag/20261121-203620-lecture-lentilles-bbis-v1/lecture-lentilles-bbis.json` (`0c706569d9bb1221aa66e7e7e047b97783f601876688ce99034442d76d571e89`), rendu par `lanceur_v9 phrases` (code égal à la fiche v3), copie à l'octet sous `lecture/phrases-code-lentilles-bbis-v1.json`. Comparaison : `lecture/comparaison-phrases-lecteur-code-v1.md`.")
w("- **Date** : 2026-11-21, ouverture à 20:36Z (après l'inscription de la ligne d'ouverture) ; 0 USD, processeur du conteneur, aucun nouveau calcul de lecture.\n")
w("## Phrase de tête\n")
w(TETE + "\n")
w("Verdict d'ensemble de la tranche des lentilles publiques sur cette lentille : " + VERDICT[2:] + " (ligne 10 de `docs/notes/neuron-lens-v1/lecture-b-alpha/verdict-b-alpha-v1.md`, branche principale, `ca06acb1550ccc76fef1ec89ae0aec170c5f05252bda2711f131eaa0e645fc1d`, empreinte égale).\n")
eps = min(x["rapport_epsilon_minimal"] for c in t["couches"].values() for x in c["lentilles"].values())
w(f"La garde du rapport à ε n'a imposé aucun nul par direction (minimum {nb(eps)} ≥ 100 à toute couche et toute lentille) : la phrase « indépendance à la norme non tenue » n'est pas écrite.\n")
w("## État des tables (tel qu'elles le portent)\n")
w(f"- **Sondes** : vingt sur vingt lues (dix sondes apprises, dix lecteurs honnêtes ; aucune « non lue ») ; 25 directions (20 vecteurs de score, 5 requêtes d'attention) ; {t['comptes_de_libelles']['nombre_total_de_lectures']} lectures (25 directions × 2 signes × 2 lentilles). Couches : 9 directions à la couche 7, 7 à la couche 15, 9 à la couche 23.")
w("- **Lecture côté entrée** : Non lue : aucune lentille côté entrée publique.")
w("- **Calibration** : tenue pour les douze (couche, lentille, nul) :")
w("\n| couche | lentille | nul | compte p ≤ 0,05 | n | bornes |\n|---|---|---|---|---|---|")
for c in ("7", "15", "23"):
    for l in ("publique", "logits"):
        for n, v in t["couches"][c]["lentilles"][l]["calibration"].items():
            w(f"| {c} | {l} | {n} | {v['compte_p_sous_0_05']} | {v['n']} | [{v['q_bas']}, {v['q_haut']}] |")
w("\n- **Indice de couche** : chaque matrice lue porte l'indice de la couche de sa sonde (7, 15, 23) dans les tables.")
eg = t["egalites_au_vingtieme_rang"]
w(f"- **Garde d'égalité au vingtième rang** (addendum, EC-6) : directions lues à égalité {eg['directions_lues_a_egalite']}, directions nulles marquées {eg['directions_nulles_marquees']}, témoins à égalité {eg['temoins_a_egalite']} : aucune valeur p bornée, p_bas = p = p_haut partout.")
w("- **Jeton de début** (128 000) : parmi les vingt premiers d'aucune des 100 lectures (rang en table).")
w("- **Audit de symétrie (R4)** : déclencheurs « trop beau » et « tout négatif » **non déclenchés** (aucune liste dans aucun des quatre critères « trop beau ») ; aucun audit joué ; issue : sans objet.\n")
cl = t["comptes_de_libelles"]
w("## Comptes de libellés, avec l'attendu par le seul hasard\n")
w(f"- Concentration (100 lectures) : « concentrée au-delà des deux nuls » {cl['concentration']['comptes'].get('concentrée au-delà des deux nuls',0)} (attendu au plus {nb(cl['concentration']['attendu_par_hasard_au_plus'])}) ; « intermédiaire » {cl['concentration']['comptes'].get('intermédiaire',0)} ; « non distincte du nul » {cl['concentration']['comptes'].get('non distincte du nul',0)}.")
w(f"- Part au-dessus du nul (100 lectures) : « non distincte du nul » {cl['part_au_dessus_du_nul']['comptes'].get('non distincte du nul',0)} ; « concentrée » 0 (attendu au plus {nb(cl['part_au_dessus_du_nul']['attendu_par_hasard_au_plus'])}).")
w(f"- Familles « sur-représentées » : {cl['familles_sur_representees']['compte']} (attendu au plus {nb(cl['familles_sur_representees']['attendu_par_hasard_au_plus'])}, soit 100 lectures × 2 familles × 0,01).")
w(f"- Pôles (25 directions) : « concentrés » {cl['poles']['comptes'].get('concentrée au-delà des deux nuls',0)} (attendu au plus {nb(cl['poles']['attendu_par_hasard_au_plus'])}) ; « intermédiaires » {cl['poles']['comptes'].get('intermédiaire',0)} ; « non distincts » {cl['poles']['comptes'].get('non distincte du nul',0)}.")
w("- Les valeurs p d'une même couche partagent le nul isotrope ; elles ne sont pas indépendantes (« Métrique », point 9). Aucune correction des comparaisons multiples (descriptif).\n")
w("## Phrases gelées, par direction\n")
w("Ordre : couche, puis direction ; pour chaque direction, les quatre lectures (lentille publique côté sortie puis lentille des logits ; signe + puis −), chacune suivie de ses deux phrases de famille, puis la phrase des pôles. Les pôles « intermédiaires » n'ont pas de phrase gelée (« Critères ») : leurs valeurs restent en table et la ligne le dit.\n")
for c in (7, 15, 23):
    w(f"### Couche {c}\n")
    for d in t["directions"]:
        if d["couche"] != c:
            continue
        s = next(x for x in t["sondes"] if x["cle"] == d["sonde"])
        w(f"**{d['sonde']} ({d['vecteur']})** — {s['nom_en_clair'].split(' (')[0]}, {'requête d’attention' if d['vecteur']=='q' else 'vecteur de score'} ; famille retenue `{s['famille']}`, norme {nb(d['norme'])}.\n")
        for l in ("publique", "logits"):
            for sg in ("+", "-"):
                for p in mes[f"{d['sonde']}/{d['vecteur']}/{l}/{sg}"]["lecteur"]:
                    w(f"- {p}")
        pl = mes[f"{d['sonde']}/{d['vecteur']}/poles"]
        if pl["lecteur"]:
            w(f"- {pl['lecteur'][0]}")
        else:
            p = d["poles"]
            w(f"- Pôles « intermédiaires » (cosinus maximal {nb(p['concentration'])} ; p {nb(p['p'][p['nul_isotrope_en_vigueur']])} et {nb(p['p']['nul-signes'])}) : aucune phrase gelée ; valeurs en table.")
        w("")
w("## Comparaisons appariées\n")
for x in r["table"]:
    if ":" in x["cle"] and "~" in x["cle"]:
        typ, ab = x["cle"].split(":", 1)
        a, b = ab.split("~")
        nom = {"sonde-lecteur": "sonde apprise et lecteur honnête", "plis": "deux plis", "doses": "deux doses"}[typ]
        w(f"- ({nom} ; `{a}` / `{b}`) {x['lecteur'][0]}")
w("\nLes jetons communs de la phrase gelée sont ceux de la lentille publique côté sortie, signe + ; les trois autres comptes (signe −, lentille des logits) sont en table, recomptés par le lecteur à partir des identifiants, sans écart.\n")
w("**Accord de la lentille publique avec la lentille des logits** (jetons communs aux vingt premiers, signes + et −) et **témoin de couche** (jetons communs entre la lecture à sa couche et aux deux autres couches, lentille publique), tels que les tables les portent :\n")
w("| direction | couche | accord + | accord − | témoin (autre couche : + / −) |\n|---|---|---|---|---|")
for d in sorted(t["directions"], key=lambda d: (d["couche"], d["sonde"], d["vecteur"])):
    tem = "; ".join(f"{k} : {v['+']} / {v['-']}" for k, v in sorted(d["lectures"]["publique"]["temoin_de_couche"].items(), key=lambda kv: int(kv[0])))
    w(f"| `{d['sonde']}/{d['vecteur']}` | {d['couche']} | {d['accord_lentilles']['+']} | {d['accord_lentilles']['-']} | {tem} |")
w("")
w("## Attentes de l'auteur (« Prédiction », pour mémoire ; rien n'en dépend)\n")
w("- **A-1** (au moins une sonde apprise « concentrée au-delà des deux nuls » par la lentille publique à sa couche, à un signe au moins) : **non réfutée** — `P-instruit/e1/sonde` (w, couche 15, signe −) et `P-S25/e1/sonde` (q, couche 23, signes + et −).")
w("- **A-2** (famille « nombres » ou « coût » sur-représentée dans les vingt premiers jetons d'au moins une sonde apprise sur l'adaptateur saboteur, par la lentille publique) : **non réfutée** — « nombres », 8 sur vingt, `P-S25/e1/sonde` (w, couche 23, signe +), direction elle-même « non distincte du nul ».")
w("- **A-3** (part des lectures « concentrées » par la lentille publique plus haute à la couche 23 qu'à la couche 7) : **non réfutée** — 2 lectures sur 18 à la couche 23 (une direction sur neuf), 0 sur 18 à la couche 7 (unité de compte non fixée par le texte ; même sens par lecture et par direction).")
w("- **A-4** (cosinus sonde apprise / lecteur honnête positif pour la plupart des paires de même cellule, pli et couche) : **non réfutée** — 4 paires de même couche, cosinus 0,1887, 0,0813, 0,0761, 0,2477, tous positifs ; les six autres paires sont « couches différentes : sans objet ».\n")
w("## Description libre, après lecture, non préenregistrée\n")
w("*Tout ce qui suit est marqué « description libre, après lecture, non préenregistrée » ; rien n'y est un libellé, et rien ne parle de la détection du sabotage.*\n")
w("1. *(description libre, après lecture, non préenregistrée)* Les cinq lectures « concentrées » viennent de deux directions seulement : la requête d'attention de la sonde apprise sur l'adaptateur saboteur à la dose 0,25, pli e1 (couche 23 ; quatre lectures sur quatre : deux lentilles, deux signes), et le vecteur de score de la sonde apprise sur l'organisme à consigne cachée, pli e1 (couche 15 ; lentille publique, signe −). Pour la première, les deux lentilles s'accordent sur 9 et 11 des vingt premiers jetons ; aucune des cinq n'est un lecteur honnête.")
w("2. *(description libre, après lecture, non préenregistrée)* Les pôles se distinguent des nuls bien plus souvent que les jetons : 15 directions sur 25 ont des pôles « concentrés », toutes à la plus petite valeur p possible (1/2 001) sous les deux nuls, dont 5 lecteurs honnêtes (2 à la couche 7, 1 à la couche 15, 2 à la couche 23), contre 5 lectures de jetons sur 100. L'attendu par le seul hasard est au plus 0,025. Le texte ne prévoit pour les pôles ni calibration ni déclencheur d'audit : voir la réserve 1.")
w("3. *(description libre, après lecture, non préenregistrée)* Aux couches 7 et 15, la lentille publique et la lentille des logits ne partagent presque aucun des vingt premiers jetons (0 à 3 sur vingt) ; à la couche 23 elles en partagent 1 à 11. Cela s'accorde avec la mise en garde du texte (« Frontière », point 4) sur la lecture sous les deux tiers de la profondeur ; ce n'est pas une mesure de fidélité.")
w("4. *(description libre, après lecture, non préenregistrée)* Les cosinus entre directions d'une même couche restent modestes : entre plis, 0,13 à 0,49 ; entre doses, de −0,0009 à 0,66 (le plus haut : vecteurs de score des doses 0,75 et 1, pli e0, couche 15) ; entre sonde apprise et lecteur honnête, 0,076 à 0,25. Les réglages retenus par la validation interne changent de couche ou de famille d'un pli à l'autre pour cinq cellules-rôles sur dix (« Frontière », point 10 : ce ne sont pas des scores).")
w("5. *(description libre, après lecture, non préenregistrée)* Les quatre familles « sur-représentées » portent toutes sur des directions « non distinctes du nul » ; la plus nombreuse est « nombres », 8 sur vingt (attendu 0,19) ; les trois autres sont « coût », 1 ou 2 jetons sur vingt.\n")
w("## Réserves\n")
w("1. **Pôles « concentrés » nombreux (R4, symétrie : « trop beau = réserve »).** 15 sur 25, dont des lecteurs honnêtes, tous au plancher de la valeur p. Aucun déclencheur gelé ne porte sur les pôles et aucune calibration des pôles n'est prévue : le lecteur ne peut dire si le nul des pôles (cosinus maximal des directions nulles) est bien taillé pour des directions repliées par la normalisation. Ces libellés sont écrits tels que les tables les portent ; un contrôle (par exemple une calibration des pôles par des témoins) relèverait d'une version neuve et d'un nœud, non de cette lecture.")
w("2. **Familles** : 4 « sur-représentées » pour un attendu d'au plus 2 ; écart faible, à valeurs p dépendantes.")
w("3. **Choix de forme du lecteur** (non fixés par le texte) : écriture des nombres à quatre chiffres significatifs et des jetons sous leur forme Python échappée, repris du rendu du code pour que la comparaison porte sur le fond ; ordre des phrases de famille (le lecteur suit l'ordre du texte, nombres puis coût ; le code, celui des tables) ; attendu d'une famille écrit sous le nul isotrope dans la phrase gelée (le texte dit « attendu sous le nul » sans préciser lequel ; les deux sont en table).")
w("4. **Jetons communs de la phrase de comparaison** : la phrase gelée n'en porte qu'un compte ; lentille publique et signe + retenus, comme le code ; les autres comptes sont en table.\n")
w("## Comparaison au code\n")
w(f"{r['nombre_de_lignes']} lignes comparées (100 lectures, 25 lignes de pôles, 49 comparaisons) : **{r['lignes_egales']} égales, 0 désaccord** ; aucun libellé recalculé différent de celui des tables ({len(r['ecarts_de_libelles'])}) ; aucun compte de jetons communs différent ({len(r['ecarts_de_jetons_communs'])}) ; comptes de familles recalculés par les règles gelées : 0 écart. Aucun désaccord à soumettre au second lecteur. Détail : `lecture/comparaison-phrases-lecteur-code-v1.md`.")
open(f"{D}/description-v1.md", "w", encoding="utf-8").write("\n".join(o) + "\n")
# table de comparaison
c = ["# Comparaison des phrases du lecteur neuf et des phrases rendues par le code — lecture des sondes de l'étape B bis par la lentille publique — v1\n",
     "Lecteur : `lecture/lecteur_independant_lentilles_bbis_v1.py` (n'importe aucun module du code de la lecture ; recalcule les libellés par le « Seuil » gelé, les jetons communs par les identifiants). Code : `phrases-code-lentilles-bbis-v1.json` (`0c706569…`). Égalité : mêmes phrases par ligne, comme ensemble ; « même ordre » rapporte l'ordre des phrases de famille (non fixé par le texte). Les phrases elles-mêmes sont dans `description-v1.md` (celles du lecteur) et `phrases-code-lentilles-bbis-v1.json` (celles du code) ; sortie complète : `comparaison-phrases-lecteur-code-v1.json`.\n",
     f"**Bilan** : {r['nombre_de_lignes']} lignes, {r['lignes_egales']} égales, **0 désaccord** ; 0 libellé différent ; 0 jeton commun différent ; 0 clé présente d'un seul côté ; ordre différent sur {sum(not x['meme_ordre'] for x in r['table'])} lignes (ordre des deux phrases de famille seulement).\n",
     "| direction (ou paire) | libellé du lecteur | phrases du lecteur | phrases du code | égales | même ordre |", "|---|---|---|---|---|---|"]
for x in r["table"]:
    c.append(f"| `{x['cle']}` | {x.get('libelle_lecteur','comparaison')} | {len(x['lecteur'])} | {len(x['code'] or [])} | {'oui' if x['egales'] else '**non**'} | {'oui' if x['meme_ordre'] else 'non'} |")
open(f"{D}/lecture/comparaison-phrases-lecteur-code-v1.md", "w", encoding="utf-8").write("\n".join(c) + "\n")
