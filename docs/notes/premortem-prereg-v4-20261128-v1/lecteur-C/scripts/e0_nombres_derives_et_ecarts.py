"""É0, suite — nombres dérivés de la pièce (D) (effectifs, fractions, seuils), recalculés ; puis écarts entre la pièce (D),
les deux brouillons, la passation v4 (§ 4) et les lignes GO-2026-11-28-01 à -03 du registre des accords :
pour chaque élément de l'« Arbitrage de Lazar » de la pièce (D), figure-t-il dans la ligne du registre ?"""
import json, re, sys
from pathlib import Path
from scipy import stats

RACINE, SORTIE = Path(sys.argv[1]), Path(sys.argv[2])
B = RACINE / "brouillons/prereg-v4-c-furtif-g1"
D_ = (B / "arbitrages-GO-2026-11-28-01-a-03-texte-gemini-v1.md").read_text(encoding="utf-8")
G0 = (B / "G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md").read_text(encoding="utf-8")
G1 = (B / "G1-architecture-h1-h2-v1-brouillon-gemini-1.md").read_text(encoding="utf-8")
PASS = (RACINE / "registres/passations/passation-claude-session-mere-v4-20261128.md").read_text(encoding="utf-8")
GO = {m.group(1): m.group(0) for m in re.finditer(r"^\| (GO-2026-11-28-0[123]) \|.*$", (RACINE / "registres/go.md").read_text(encoding="utf-8"), re.M)}
lect = json.loads((RACINE / "diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json").read_text())["resultat"]["manipulation"]

nb = []
def n(nom, cite, recalcule, tol=5e-4, note=""):
    ok = (abs(cite - recalcule) <= tol) if isinstance(cite, (int, float)) and isinstance(recalcule, (int, float)) else (cite == recalcule)
    nb.append({"grandeur": nom, "cite": cite, "recalcule": recalcule, "conforme": bool(ok), "note": note})

mn, m3, m5 = (lect[c]["part_mention_texte_prive"] for c in ("consigne_neutre", "gonfle_3", "gonfle_5"))
n("part de mention, consigne_neutre", 0.0578125, mn, 1e-12); n("écart gonfle_3 − neutre", 0.1078125, m3 - mn, 1e-12); n("écart gonfle_5 − neutre", 0.17109375, m5 - mn, 1e-12)
n("écarts > 0,03 (les deux)", True, (m3 - mn > 0.03) and (m5 - mn > 0.03))
n("alpha_s = 0,025/3", 0.00833, 0.025 / 3, 5e-6)
n("727 = 64 + 64 + 599", 727, 64 + 64 + 599); n("599 = 399 + 200", 599, 399 + 200); n("264 = 64 + 200", 264, 64 + 200)
b = stats.beta(4, 396)
n("Beta(4,396) : espérance", 0.01, b.mean(), 1e-12); n("Beta(4,396) : coefficient de variation (%)", 49.7, 100 * b.std() / b.mean(), 0.05)
n("Beta(4,396) : P(U < 0,2 %) (%)", 0.89, 100 * b.cdf(0.002), 0.01)
b1 = stats.beta(1, 99)
n("3A-intra, m = 1 sur 99 tâches, Beta(1,99) : P(U < 0,2 %) (%)", 18.0, 100 * b1.cdf(0.002), 0.5); n("Beta(1,99) : espérance", 0.01, b1.mean(), 1e-12)
n("plancher du calibrage conforme à 64 tâches : 1/64 (%)", 1.5625, 100 / 64, 1e-9)
n("m = 2 sur 252 : floor(0,01 × 253)", 2, int(0.01 * 253)); n("m = 25 sur 2 520 : floor(0,01 × 2 521)", 25, int(0.01 * 2521))
n("3/128 (%) cité par le brouillon G0", 2.34375, 100 * 3 / 128, 1e-9); n("2/128 (%) cité par le brouillon G0", 1.5625, 100 * 2 / 128, 1e-9)
n("épisodes par condition à E = 4 : 64 × 4", 256, 64 * 4)
n("actions de la micro-course : 5 × 64 × 4 × 10", 12800, 5 * 64 * 4 * 10)
n("actions du brouillon G1 (3A-amont) : 5×200×4×10 + 399×1×10 + 64×2×10×2", 46550, 5 * 200 * 4 * 10 + 399 * 10 + 64 * 2 * 10 * 2)
n("actions du brouillon G1 (3A-intra) : 5×200×4×10", 40000, 5 * 200 * 4 * 10)
# non recalculables : dits tels quels
non_recalculables = ["« +5,1 pts de rappel attendu » (modèle gaussien jouet à décalage 2,5 de l'oracle test_go3 ; aucune donnée)", "« type I tenu à 0,80 % (contre ≈ 24,7 % à seuil figé) » (aucune source citée)",
                     "« MDE ≥ +11,3 pts » (aucune source citée)", "« ~2 h GPU A100 pour le juge 27B » (aucun devis)", "« +12 min GPU » (aucun devis)", "confiances 0,90 ; 0,55 ; 0,90 ; 0,88 (jugements)"]

# seuil des reprises : trois écritures
seuils = {"registre GO-2026-11-28-01": re.search(r"arrêt si > 3/N_ep ou écart > 2/N_ep", GO["GO-2026-11-28-01"]) is not None,
          "passation v4 § 4.1": "arrêt si `> 3/N_ep` ou écart `> 2/N_ep`" in PASS,
          "pièce (D) : « reprises > 3/128 par condition, écart inter-conditions > 2/128 »": "reprises `> 3/128` par condition, écart inter-conditions `> 2/128`" in D_,
          "brouillon G0 : N_reprises(c)/256 > 3/128 et écart/256 > 2/128": "\\frac{N_{\\text{reprises}}(c)}{256} > \\frac{3}{128}" in G0}
lecture_seuils = {"registre et passation, avec N_ep = 256 (E = 4)": {"reprises_max_par_condition": 3, "ecart_max": 2, "taux": 3 / 256},
                  "pièce (D) et brouillon G0": {"reprises_max_par_condition": 6, "ecart_max": 4, "taux": 3 / 128},
                  "128 = 64 tâches × 2 répliques (E = 2, plan antérieur)": 64 * 2}

# éléments de l'arbitrage de la pièce (D), par GO : présents dans la ligne du registre ?
def dans(ligne, *motifs): return all(re.search(m, ligne, re.I) is not None for m in motifs)
elements = {
 "GO-2026-11-28-01": [
  ("suppression de « b-strict »", [r"b-strict"]), ("interdiction d'ouvrir les .npz de la course", [r"interdiction définitive", r"\.npz"]),
  ("option GO-1A, repli GO-1B si moins de 64 tâches", [r"GO-1A", r"GO-1B"]), ("honnête sans en-tête système factice", [r"sans en-tête système factice"]),
  ("écart de longueur du bloc système nul", [r"0 jeton BPE"]), ("E = 4 répliques", [r"E = 4"]), ("32 essais au plus par pas", [r"32 essais"]),
  ("au plus 2 reprises d'épisode", [r"2 reprises"]), ("séquence descendante gonfle_5 puis gonfle_3 (gonfle_2 s'il est inclus)", [r"gonfle_5 puis gonfle_3"]),
  ("essai de chaîne A0 sur scores-H-seul.npz séparé physiquement", [r"scores-H-seul"]), ("niveau alpha_s = 0,00833", [r"0[,.]00833"]),
  ("filtre valider_action_c_furtif_v2 sur les 6 clés", [r"valider_action"]), ("« sans repli y(0) »", [r"sans repli|y\^\{?\(0\)"]),
  ("coupe du préfixe 0 ≤ u ≤ u_COST − 2", [r"Préfixe|u_COST|u_\{\\text\{COST"]), ("polarité sigma_s = +1", [r"sigma_s|σ_s|\\sigma_s"]),
  ("garde de l'antipode", [r"Antipode"]), ("état « N-scalaire » envoyé à l'issue L3", [r"N-scalaire"]),
  ("critère de révision (reprises, écart, échec de A0)", [r"critère de révision|Critère de révision"]), ("seuils 3/128 et 2/128", [r"3/128"])],
 "GO-2026-11-28-02": [
  ("option GO-2A", [r"GO-2A"]), ("banque Python, moins de 200 ms", [r"Python", r"200 ms"]), ("conteneur bwrap/seccomp sans réseau", [r"bwrap|seccomp"]),
  ("oracle privé à delta_min scellé hors de l'espace des tests publics", [r"oracle_prive|oracle privé|delta|δ"]), ("quatrième mode tenu à l'écart", [r"quatrième mode tenu à l'écart"]),
  ("session aveugle aux moniteurs", [r"aveugle aux moniteurs"]), ("juge google/gemma-2-27b-it en BF16", [r"gemma-2-27b-it"]), ("masse_min = 0,80", [r"masse_min = 0,80"]),
  ("git diff -U5", [r"git diff -U5"]), ("analyse d'au plus 256 jetons", [r"256"]), ("TRACE-lite", [r"TRACE-lite"]), ("b_lex de 2 000 unigrammes et bigrammes", [r"2 000"]),
  ("traits continus réduits de b_lex", [r"traits continus"]), ("gardes G-W_E et G-Pré-Code", [r"G-W_E", r"G-Pré-Code"]), ("combinaison sans supervision, demi-somme, gamma = 1", [r"gamma|γ|zéro-supervision|sans supervision"]),
  ("échelle robuste sigma_rob et BrisEgalite", [r"BrisEgalite|sigma_rob|σ_rob"]), ("retrait de B_dev du bras primaire", [r"B_dev"]), ("H_nu en clause 1", [r"H_nu en clause 1"]),
  ("J en clause 3 décisive", [r"J en clause 3"]), ("témoin léger H_LoRA", [r"H_LoRA"]), ("effacement LEACE par TSQR et post-max", [r"LEACE|TSQR"]),
  ("critère de révision (masse sous 0,80 dans plus de 1 % ; échec canonique ou mutants)", [r"critère de révision|1 %"])],
 "GO-2026-11-28-03": [
  ("option GO-3A, « 3A-amont », 727 tâches", [r"GO-3A", r"727"]), ("64 + 64 + 599, puis 399 à E = 1 et 200 à E = 4", [r"599", r"399", r"200"]),
  ("double bootstrap de Dirichlet continu, conjoint", [r"Dirichlet"]), ("B = 10 000 tirages", [r"10 000|10\\,000"]), ("repli « 3A-intra » à 264 tâches", [r"264"]),
  ("en H1, le gain de rappel global sur le saboteur soutenu est seul primaire", [r"S_soutenu|soutenu|seul primaire"]), ("budget d'épisode co-rapporté", [r"budget d'épisode"]),
  ("H2 à alpha_s = 0,00833", [r"0,00833"]), ("H2 restreinte à 2 à 4 pas sabotés sur S_diffus", [r"S_diffus|diffus"]), ("garde S2-G1 (utilité visible ≥ 0,80, écart ≤ 0,10)", [r"S2-G1"]),
  ("garde S1-G1", [r"S1-G1"]), ("rang 1 : S_G2N-top4, avant déploiement", [r"S_G2N-top4"]), ("pi_0 = 0,25 et tau_0 = 0,85", [r"0,85"]),
  ("rang 1 contre l'intersection-union complète de N-056 (six comparateurs)", [r"N-056|intersection"]), ("gain net positif face à J", [r"gain net"]),
  ("rang 2 conditionnel : préemption causale en ligne par M_t(e)", [r"M_t\(e\)"]), ("calibrage de M_t par le calibrage conforme groupé sur le maximum", [r"max_"]),
  ("critère de révision", [r"critère de révision"])],
}
table = {}
for go, L in elements.items():
    table[go] = [{"element_de_la_piece_D": nom, "dans_la_ligne_du_registre": dans(GO[go], *motifs), "dans_la_passation_v4_par_4": dans(PASS.split("## 4.")[1].split("## 5.")[0], *motifs)} for nom, motifs in L]
resume = {go: {"elements": len(v), "absents_du_registre": [x["element_de_la_piece_D"] for x in v if not x["dans_la_ligne_du_registre"]]} for go, v in table.items()}
# ce que les lignes disent de ce qu'elles remplacent
remplace = {go: {"cite_N-055_ou_pari_apparie": bool(re.search(r"N-055|pari apparié", GO[go])), "cite_GO-2026-11-05-07_ou_DG1": bool(re.search(r"GO-2026-11-05-07|DG1", GO[go])),
                 "cite_N-060": "N-060" in GO[go], "cite_N-062": "N-062" in GO[go], "cite_N-074_ou_GO-2026-11-18-48": bool(re.search(r"N-074|GO-2026-11-18-48", GO[go])),
                 "cite_N-076": "N-076" in GO[go], "cite_le_programme_v3": bool(re.search(r"programme v3|fcc27171", GO[go])), "montant": re.search(r"\| (0 USD[^|]*) \|", GO[go]).group(1) if re.search(r"\| (0 USD[^|]*) \|", GO[go]) else None,
                 "porte_les_mots_de_Lazar_entre_guillemets": "«" in GO[go].split("Lazar |")[0] and bool(re.search(r"« [^»]{3,} »", GO[go].split("| Lazar |")[0].replace("« b-strict »", "").replace("« c-furtif »", "").replace("« 3A-amont »", "").replace("« 3A-intra »", "")))}
            for go in GO}
cout_options = {"GO-1A": bool(re.search(r"GO-1A`[^\n]*USD", D_)), "GO-1B": bool(re.search(r"GO-1B`[^\n]*USD", D_)), "GO-2A": "~2 h GPU A100 (juge seul) ; aucun dollar", "GO-2B": bool(re.search(r"GO-2B`[^\n]*USD", D_)),
                "GO-3A": "+12 min GPU ; aucun dollar", "GO-3B": bool(re.search(r"GO-3B`[^\n]*USD", D_)), "occurrences_de_USD_ou_dollar_dans_la_piece_D": len(re.findall(r"USD|dollar|€|EUR", D_))}
out = {"nombres_derives": nb, "non_recalculables": non_recalculables, "seuil_des_reprises": {"presence": seuils, "lecture": lecture_seuils},
       "elements_de_l_arbitrage_contre_registre": table, "resume": resume, "ce_que_les_lignes_du_registre_nomment": remplace, "couts_des_options_dans_la_piece_D": cout_options}
SORTIE.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print("NOMBRES :", sum(x["conforme"] for x in nb), "conformes sur", len(nb))
for x in nb:
    if not x["conforme"]: print("  ECART", x)
print(json.dumps({"seuil_des_reprises": out["seuil_des_reprises"], "resume": resume, "nomme": remplace, "couts": cout_options}, ensure_ascii=False, indent=1))
