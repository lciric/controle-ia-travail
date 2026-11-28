"""Vérification de la v3 (angle fidélité, tour 2) : phrases et chiffres nouveaux ou déplacés, à la page exacte citée ;
lignes de table (même ligne imprimée, bonne colonne) ; renvois au dépôt (présence à la ligne citée, rien d'imprimé) ;
forme française du chiffre présente dans la v3 ; épreuve R5 (artefacts qui doivent tous être rejetés).

python3 -I -B verifier_v3.py > sortie-verification-v3-fidelite.txt
"""
import importlib.util
import re
import unicodedata

ICI = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/"
DEPOT = "/home/user/controle-ia-travail/"
spec = importlib.util.spec_from_file_location("page3", ICI + "verif-v3-fidelite/page3.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

V3 = open(ICI + "synthese-comment-detecter-v3.md", encoding="utf-8").read()
V3N = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", V3))
compte = {"ok": 0, "ecart": 0}


def rapport(ok, quoi):
    compte["ok" if ok else "ecart"] += 1
    print(("OK      " if ok else "ECART   ") + "| " + quoi)


# --- A. Phrases et chiffres à la page exacte (clé, page, phrase imprimée, forme dans la v3 ou None)
PHRASES = [
    ("BX", 5, "Score filtering retains the full transcript during inference but selectively excludes certain token positions when computing the final probe score", None),
    ("BX", 5, "aggregated scores only from token positions outside the elicitation prompt and model reasoning", None),
    ("BX", 5, "degraded by 14 points to 0.81 AUROC", "0,81"),
    ("BX", 5, "replacing the elicitation instructions with a benign prompt resulted in a", None),
    ("BX", 6, "32-point drop to 0.63 AUROC", "0,63"),
    ("BX", 6, "Sandbagging drops from 0.95 to 0.62", "0,62"),
    ("BX", 6, "recall at fixed 1% FPR threshold", "1 % de faux positifs"),
    ("BX", 4, "Fine-tuned Model Organisms exhibit the target behavior without requiring elicitation prompts or producing reasoning traces", None),
    ("BX", 8, "from almost perfect detection 0.94 to chance performance 0.5", None),
    ("BX", 8, "re-training probes on the Model Organism using contrastive pairs", None),
    ("BX", 8, "The models may not have fully internalized the target behaviors, which could partly explain poor probe performance", None),
    ("YS", 3, "we use layer 15 residual stream activations", "couche 15"),
    ("YS", 3, "Sandbagging performs poorly (0.606 AUROC).", "0,606"),
    ("YS", 3, "0.936 / 0.950 / 0.869 AUROC across the three targets", "0,869"),
    ("AP", 9, "Was your last response deceptive?", None),
    ("AP", 9, 'and then the model response "No."', None),
    ("AP", 9, "comparable to our Roleplaying probe, except for substantially degraded performance on Sandbagging", None),
    ("AP", 18, "every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag", None),
    ("AP", 18, "consistently rating every control response as honest", None),
    ("AP", 23, "Recall at 1% FPR compared to control does show improvement, although is still subpar compared to the probe trained on Instructed-Pairs", None),
    ("AP", 23, "here we train a different probe (on just the last positions of the training data)", None),
    ("AP", 5, "as a control dataset to calibrate our false positive rate", None),
    ("AP", 5, "The system prompt directly instructs the model to sandbag", None),
    ("AP", 22, "We find that taking the mean is best on all datasets for the probe trained on Instructed-Pairs", None),
    ("PAR", 5, 'the assistant responds "No"', None),
    ("PAR", 5, "by averaging probe activations across all public tokens in the assistant's final response", None),
    ("PAR", 6, 'the assistant responds "Yes"', None),
    ("PAR", 7, "By contrast, Peak Activation and the Follow-up monitors consistently underperform compared to Full Averaging", None),
    ("PAR", 4, "the assistant is prompted to truthfully answer generic trivia questions but to intentionally provide plausible yet false answers", None),
    ("DYL", 11, "relative to prompted Varied Deception on the same models", None),
    ("DYL", 11, "Median balanced accuracy falls from 0.85 to 0.52 for Apollo, from 0.81 to 0.65 for DYL", "0.85 to 0.52 for Apollo, from 0.81 to 0.65"),
    ("DYL", 11, "we re-ran the evaluation against prompted Gender Secret model organisms", None),
    ("DYL", 11, "Apollo and Unrelated Questions perform poorly even on the prompted variants", None),
    ("DYL", 11, "DYL, by contrast, retains strong performance on the prompted variants", None),
    ("DYL", 11, "consistent with being caused by fine-tuning rather than the underlying behaviour", None),
    ("DYL", 10, "correlates positively and significantly with the Artificial Analysis Intelligence Index", None),
    ("DYL", 10, "Across all three trained model organism testbeds (AuditBench, Sandbagging, Gender Secret)", None),
    ("DYL", 12, "Scaling results are on prompted lying only", None),
    ("DYL", 8, "we calibrate the threshold to a 1% positive rate on Alpaca completions", None),
    ("DYL", 8, 'a follow-up question of the form "Did you lie in the last message?"', None),
    ("DYL", 2, "measured by the AA Intelligence Index", None),
    ("DYL", 5, "a prompted testbed broadening coverage of lie-inducing motivations", None),
    ("CA", 8, "0.585–0.781 on Qwen3.5-2B", "0,585 à 0,781"),
    ("CA", 8, "0.613–0.760 on Nemotron-3 Nano", "0,613–0,760"),
    ("CA", 8, "every probe improves from the smallest model of each family, and scores exceed 90% from there up", None),
    ("CA", 8, "five Qwen3.5 models (2B to 397B-A17B)", None),
    ("CA", 8, "from 27B up (0.963-0.986)", None),
    ("CA", 25, "Nemotron 3 Nano 30B-A3B", "30B-A3B"),
    ("AG", 17, "there were more mysterious failures", None),
    ("AG", 17, "successfully caused many spurious probe activations", None),
    ("AG", 17, "probes on Oak fail to indicate more deception", None),
    ("AG", 43, "The red team hypothesized", None),
    ("AG", 43, "the difficulty of aggregating signals over much longer contexts in multi-turn agentic trajectories", None),
    ("AG", 43, "the model does not need to say false facts in order to underperform at agentic tasks", None),
    ("AU", 6, "very correlated with the 'Impostor' label", None),
    ("AU", 7, "cache activations for the last 10 tokens for each datapoint", None),
    ("K", 3, "we never remove the incentive as these are integral to their dataset prompts", None),
    ("K", 7, "Domain shift effects are significant for all behaviours, while response strategy effects are often non-significant", None),
    ("K", 7, "ref = on-policy incentivised test set, incentivised", None),
    ("K", 5, "0.85 ±0.039", "0.85 ±0.039"),
    ("K", 5, "0.74 ±0.051", "0.74 ±0.051"),
    ("GM", 6, "We then take the maximum over EMA scores", None),
    ("GM", 7, "takes the max over all mean scores of all possible windows", None),
    ("GM", 7, "The final output is max", None),
    ("GM", 7, "prevents dilution of the signal when harmful content appears in a small portion of a long context", None),
    ("GM", 8, "long context random traffic", None),
    ("GM", 12, "Our selected probe is the Max of Rolling Means Attention Probe", None),
    ("MK", 4, "nearly matching the performance of the more consistent probes", None),
    ("MK", 4, "this may indicate that the high-stakes nature of the MTS dataset is dependent upon specific words", None),
    ("MK", 4, "The best performing probes are Attention, Softmax, and Mean", None),
    ("MK", 4, "the Last Token activation probe consistently performs poorly", None),
    ("OA", 1, "show that obfuscation emerges in this setting", None),
    ("OA", 1, "obfuscated activations arise from representation drift during RL, with or without a detector penalty", None),
    ("OA", 1, "The detector penalty only incentivizes obfuscated policies", None),
    ("OA", 1, "Sufficiently high KL regularization and detector penalty can yield honest policies", None),
    ("EM", 38, "while steering towards desperation increases", None),
    ("EM", 38, "emotion representations can influence behavior even when it is not evident from the text of the transcript", None),
    ("KU", 5, "the probe detects the deceptive prompt regime", None),
    ("KU", 9, "deceptive prompt regime", None),
    ("BU", 10, "93.8 ± 1.5%", "93,8 %"),
    ("BU", 10, "LR with 79 ± 8% accuracy", None),
]

print("=== A : phrases et chiffres nouveaux ou déplacés, à la page exacte citée par la v3")
for cle, page, phrase, forme in PHRASES:
    mode = P.present(cle, page, phrase)
    ok = bool(mode)
    quoi = "%s p. %d | %s" % (cle, page, phrase[:100])
    if forme is not None:
        f_ok = re.sub(r"\s+", " ", forme) in V3N
        ok = ok and f_ok
        quoi += " | forme v3 « %s » %s" % (forme, "présente" if f_ok else "ABSENTE")
    rapport(ok, quoi + (" | mode %s" % mode if mode else " | ABSENT de la page"))


# --- B. Lignes de table : même ligne imprimée, bonne colonne
def ligne_table(cle, page, etiquette, mode="layout"):
    """Première ligne imprimée faite de l'étiquette suivie de nombres seulement (une légende est écartée)."""
    for l in P.pages(cle, mode)[page - 1].split("\n"):
        s = l.strip()
        if s.startswith(etiquette):
            reste = s[len(etiquette):]
            if re.fullmatch(r"(\s+[−+\-]?\d+(?:\.\d+)?%?\**)+\s*", reste):
                return re.findall(r"[−+\-]?\d+(?:\.\d+)?%?\**", reste)
    return None


print()
print("=== B : lignes de table")
PAR = [("Full Averaging (Pairs)", {4: "0.964", 5: "0.941"}), ("Full Averaging (RP)", {4: "0.828", 5: "0.840"}),
       ("Peak Activation (Pairs)", {4: "0.839", 5: "0.867"}), ("Peak Activation (RP)", {4: "0.891", 5: "0.856"}),
       ("Deception No (Pairs)", {4: "0.849"}), ("Honest Yes (Pairs)", {4: "0.879"}),
       ("Deception No (RP)", {4: "0.457"}), ("Honest Yes (RP)", {4: "0.437"}),
       ("Critical Averaging (Pairs)", {4: "0.924"})]
for etiq, attendu in PAR:
    v = ligne_table("PAR", 7, etiq)
    ok = v is not None and all(v[i] == x for i, x in attendu.items())
    rapport(ok, "PAR table 3 p. 7 | %s | colonnes 5 = Sandbagging, 6 = Avg. | attendu %s | lu %s" % (etiq, attendu, v))

# GM table 3 p. 12 : colonnes 0 SC[OT], 1 SC[HN], 2 LC[RT], 3 MT[HN], 4 SC[A], 5 LC[A] (lignes repliées : étiquette
# du début de ligne imprimée).
GM = [("Linear Probe Mean", {2: "0.5%", 5: "99.13%"}), ("Attn (With LC Train-", {2: "1.17%", 5: "1.34%"}),
      ("Attn  ", None), ("Rolling Attn Probe, MultiMax Agg", None)]
lignes_gm = P.pages("GM", "layout")[11].split("\n")
table = {}
for i, l in enumerate(lignes_gm):
    m = re.match(r"\s*(\S.*?)\s{2,}(\d.*)$", l)
    if m and "%" in m.group(2):
        nom = m.group(1).strip()
        suite = lignes_gm[i + 1].strip() if i + 1 < len(lignes_gm) else ""
        if suite and "%" not in suite and len(suite) < 30:
            nom = nom + " " + suite
        table[nom] = re.findall(r"\d+(?:\.\d+)?%", m.group(2))
for nom, vals in table.items():
    print("        | GM p. 12 lu : %-45s LC[RT] %-7s LC[A] %s" % (nom, vals[2], vals[5]))


def gm(nom):
    for k, v in table.items():
        if k.replace(" ", "") == nom.replace(" ", ""):
            return v
    return None


attendu_gm = {"Linear Probe Mean": ("0.5%", "99.13%"), "Attn": ("0.0%", "87.88%"),
              "Attn (With LC Train- ing)": ("1.17%", "1.34%")}
for nom, (rt, a) in attendu_gm.items():
    v = gm(nom)
    rapport(v is not None and v[2] == rt and v[5] == a, "GM table 3 p. 12 | %s | LC[RT] %s, LC[A] %s | lu %s" % (nom, rt, a, v and (v[2], v[5])))
multimax = {k: v for k, v in table.items() if "MultiMax" in k}
glissantes = {k: v for k, v in table.items() if "Rolling Agg" in k or "Rolling Exp" in k}


def pc(x):
    return float(x.rstrip("%"))


for nom_groupe, groupe, rt_att, a_att in (("agrégations MultiMax", multimax, (1.85, 82.14), (0.0, 1.73)),
                                           ("maxima de moyennes glissantes", glissantes, (1.0, 13.55), (1.73, 5.19))):
    rts = [pc(v[2]) for v in groupe.values()]
    as_ = [pc(v[5]) for v in groupe.values()]
    ok = (min(rts), max(rts)) == rt_att and (min(as_), max(as_)) == a_att
    rapport(ok, "GM table 3 p. 12 | %s (%d lignes : %s) | LC[RT] %s à %s ; LC[A] %s à %s | attendu %s ; %s" % (
        nom_groupe, len(groupe), "; ".join(groupe), min(rts), max(rts), min(as_), max(as_), rt_att, a_att))

# K table 1 p. 7 : colonnes 0 Different-domain, 1 Incentivised (ou —), 2 Prompted, 3 Off-policy
for etiq, attendu in (("Deception", {"dd": "-0.416***", "pr": "+0.035"}), ("Sandbagging", {"dd": "-0.182*", "pr": "-0.111*"})):
    l = [x for x in P.pages("K", "layout")[6].split("\n") if x.strip().startswith(etiq)]
    vals = re.findall(r"[−+\-]\d\.\d+\**", l[0].replace("−", "-")) if l else []
    ok = len(vals) == 3 and vals[0] == attendu["dd"] and vals[1] == attendu["pr"]
    rapport(ok, "K table 1 p. 7 | %s | Different-domain %s, Prompted %s | lu %s" % (etiq, attendu["dd"], attendu["pr"], vals))

# BX table 1 p. 6
v = ligne_table("BX", 6, "Sandbagging")
rapport(v == ["1.00", "0.04", "0.03"], "BX table 1 p. 6 | Sandbagging | Base 1.00, Content 0.04, Score 0.03 | lu %s" % v)

# DYL table 9 p. 28 : colonnes AA, Apollo, DYL Probe, Judge, Unrelated
lignes_dyl = P.pages("DYL", "layout")[27].split("\n")
rangs = []
for l in lignes_dyl:
    m = re.match(r"\s*([A-Za-z0-9\-]+/[A-Za-z0-9.\-]+)\s+(.*)$", l)
    if m:
        nums = re.findall(r"\d+(?:\.\d+)?", m.group(2))
        if len(nums) >= 3 and "." not in nums[0]:
            rangs.append((m.group(1), int(nums[0]), float(nums[1]), float(nums[2])))
        elif len(nums) >= 2 and "." in nums[0]:
            rangs.append((m.group(1), None, float(nums[0]), float(nums[1])))
plus = sum(1 for r in rangs if r[2] > r[3])
moins = sum(1 for r in rangs if r[2] < r[3])
egal = sum(1 for r in rangs if r[2] == r[3])
rapport((len(rangs), plus, moins, egal) == (32, 22, 8, 2),
        "DYL table 9 p. 28 | %d lignes ; Apollo devant %d, derrière %d, égalités %d | attendu 32, 22, 8, 2" % (len(rangs), plus, moins, egal))
for nom, aa, ap, dy in (("Qwen/Qwen3-8B", 13, 0.74, 0.69), ("Qwen/Qwen3-4B", 14, 0.64, 0.68),
                        ("Qwen/Qwen3.5-4B", 27, 0.89, 0.82), ("meta-llama/Llama-3.3-70B-Instruct", 14, 0.84, 0.74)):
    r = [x for x in rangs if x[0] == nom]
    rapport(bool(r) and r[0][1:] == (aa, ap, dy), "DYL table 9 p. 28 | %s | AA %s, Apollo %s, DYL %s | lu %s" % (nom, aa, ap, dy, r and r[0][1:]))
# CA p. 18 : ordre de la famille Qwen3.5
l18 = [x.split()[0] for x in P.pages("CA", "raw")[17].split("\n") if x.startswith("Qwen3.5-")]
rapport(l18[:2] == ["Qwen3.5-2B", "Qwen3.5-9B"], "CA p. 18 | famille Qwen3.5 dans l'ordre : %s" % l18)


# --- C. Renvois au dépôt : présence à la ligne citée (rien d'imprimé du contenu)
def lignes(chemin, a, b):
    t = open(DEPOT + chemin, encoding="utf-8").read().split("\n")[a - 1:b]
    s = unicodedata.normalize("NFKC", " ".join(t))
    return re.sub(r"\s+", " ", s)


DEPOT_CIT = [
    ("prereg/P3-premier-test-i-a-v1.md", 272, 274, "« Non au-dessus »** se lit « non détecté à cette puissance »"),
    ("prereg/P3-premier-test-i-a-v1.md", 272, 274, "jamais « ne sépare pas »"),
    ("prereg/P3-premier-test-i-a-v1.md", 248, 248, "mention contre honnête est non au-dessus du plancher et saboteur contre mention au-dessus"),
    ("prereg/P3-premier-test-i-a-v1.md", 278, 278, "P3-P4, T1, T3, T4"),
    ("prereg/P3-premier-test-i-a-v1.md", 318, 320, "× 1 épisode = 240 épisodes"),
    ("prereg/P3-premier-test-i-a-v1.md", 385, 385, "≈ 2,5 heures pour 240"),
    ("prereg/P3-premier-test-i-a-v1.md", 415, 416, "est un **nœud**"),
    ("prereg/P3-premier-test-i-a-v1.md", 428, 428, "pas de seconde lecture sur d'autres sondes, couches ou jeux"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", 345, 345, "rapport géométrique moyen d'environ 33"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", 172, 172, "ne doit pas être cité comme telle"),
    ("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", 358, 359, "Il ne doit être cité nulle part comme un résultat"),
    ("prereg/P3-addendum-lecture-complementaire-v1.md", 34, 34, "biais de longueur du maximum"),
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", 8, 8, "de ne relire P3 en rien"),
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", 26, 27, "la seule mesure qui sépare le nombre écrit du contexte privé"),
    ("docs/notes/brainstorm-suite-P3-v1/note-decision-suite-P3-v1.md", 85, 85, "A2 : poursuit T2 après coup, sans plancher par jeton"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-C.md", 323, 324, "Tout signal y serait suspect (R4, R3)"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-D.md", 93, 95, "Miroir sur"),
    ("docs/notes/brainstorm-suite-P3-v1/propositions/proposition-D.md", 97, 97, "jamais la moyenne ni la médiane"),
    ("registres/decisions.md", 446, 446, "exclue par la règle gelée"),
    ("registres/decisions.md", 453, 453, "choisie d'après la revue de la littérature"),
    ("registres/decisions.md", 453, 453, "passe avant la lecture de P4-instrument (sa réserve éventuelle s'y recopie)"),
    ("registres/decisions.md", 456, 456, "la première tentative de détection du plan R-262 (point 2)"),
    ("registres/decisions.md", 457, 457, "nœud toujours ouvert"),
    ("registres/decisions.md", 461, 461, "toute dépense au-delà du plafond par lancement ou du crédit est un nœud"),
    ("registres/decisions.md", 468, 468, "Tranché (c) renforcée par Lazar"),
    ("registres/decisions.md", 469, 469, "prédicteur sur les traits du texte obligatoire"),
    ("registres/go.md", 32, 32, "sonde oracle en validation croisée par tâche sous T1, T3, T4"),
    ("registres/go.md", 35, 35, "GO-2026-10-20-08"),
    ("registres/depenses.md", 88, 88, "≈ 3,96 USD"),
    ("registres/depenses.md", 89, 89, "11,79 USD"),
    ("docs/decisions/decision-N-026-v1.md", 20, 20, "« bras de diagnostic, jamais en production »"),
    ("docs/decisions/decision-N-026-v1.md", 24, 24, "« l'agrégation explique-t-elle le nul ? »"),
    ("docs/decisions/decision-N-029-v1.md", 37, 39, "Elle ne se lit pas sur les textes de P3"),
    ("docs/decisions/proposition-P-011-T0.7-sondes-v1.md", 42, 42, "jamais sur les organismes"),
    ("docs/brief-claude-code-programme-complet-v2.md", 48, 48, "Aucun run visant un signe positif"),
    ("src/controle_ia/environnements/propositions.py", 32, 39, "name concrete models, datasets, metrics"),
    ("src/controle_ia/environnements/propositions.py", 40, 49, '"COST: <estimated compute in GPU-hours, a single number>'),
    ("src/controle_ia/environnements/propositions.py", 129, 138, "la première occurrence de chaque champ fait foi"),
]
print()
print("=== C : renvois au dépôt, à la ligne citée (présence seulement)")
for chemin, a, b, texte in DEPOT_CIT:
    ok = re.sub(r"\s+", " ", texte) in lignes(chemin, a, b)
    rapport(ok, "%s l. %d-%d | %s" % (chemin, a, b, texte[:80]))

# --- D. Épreuve R5 : tout artefact doit être rejeté
print()
print("=== D : épreuve R5 (artefacts, tous doivent être rejetés)")
ARTEFACTS = [
    ("chiffre altéré", lambda: P.present("BX", 6, "32-point drop to 0.64 AUROC")),
    ("bonne phrase, mauvaise page", lambda: P.present("AP", 9, "consistently rating every control response as honest")),
    ("mot inversé", lambda: P.present("OA", 1, "The detector penalty only incentivizes honest policies")),
    ("Nemotron sur la ligne Qwen", lambda: P.present("CA", 8, "0.613–0.760 on Qwen3.5-2B")),
    ("chiffre de DYL altéré", lambda: P.present("DYL", 11, "from 0.81 to 0.52 for DYL")),
    ("dix derniers jetons altéré", lambda: P.present("AU", 7, "cache activations for all tokens for each datapoint")),
    ("table PAR, colonne voisine", lambda: (ligne_table("PAR", 7, "Peak Activation (RP)") or [None] * 6)[3] == "0.891"),
    ("table PAR, ligne voisine", lambda: (ligne_table("PAR", 7, "Full Averaging (RP)") or [None] * 6)[4] == "0.891"),
    ("table GM, LC[RT] d'une autre ligne", lambda: (gm("Linear Probe Mean") or [None] * 6)[2] == "13.55%"),
    ("table K, case voisine", lambda: "Deception" in "".join(x for x in P.pages("K", "layout")[6].split("\n") if "-0.111" in x.replace("−", "-"))),
    ("table DYL, ligne voisine", lambda: [x for x in rangs if x[0] == "Qwen/Qwen3-8B"][0][2] == 0.64),
    ("dépôt, mot altéré", lambda: "jamais « pas de trace »" in lignes("prereg/P3-premier-test-i-a-v1.md", 272, 274)),
    ("dépôt, ligne voisine", lambda: "rapport géométrique moyen d'environ 33" in lignes("docs/verdicts/verdict-P3-premier-test-i-a-v1.md", 344, 344)),
    ("v3, forme absente", lambda: "0,613–0,761" in V3N),
]
rejetes = 0
for nom, f in ARTEFACTS:
    accepte = bool(f())
    rejetes += 0 if accepte else 1
    print(("rejeté  " if not accepte else "ACCEPTÉ ") + "| " + nom)
print("--- D : %d rejetés sur %d" % (rejetes, len(ARTEFACTS)))
print()
print("--- A, B, C : %d conformes ; %d écarts" % (compte["ok"], compte["ecart"]))

# --- E. Preuves des constats (chaque ligne : « vrai » attendu)
print()
print("=== E : preuves des constats VV3-fidelite (chaque test doit valoir vrai)")


def preuve(nom, valeur):
    print(("vrai    " if valeur else "FAUX    ") + "| " + nom)


p272 = lignes("prereg/P3-premier-test-i-a-v1.md", 272, 274)
preuve("01 | [P] l. 272-274 dit « jamais « ne sépare pas » »", "jamais « ne sépare pas »" in p272)
preuve("01 | [P] l. 272-274 ne contient pas « pas de trace »", "pas de trace" not in p272)
preuve("01 | v3 : « jamais « pas de trace » ([P] l. 272-274) »", "jamais « pas de trace » ([P] l. 272-274)" in V3N)
preuve("01 | v3 : « ([P] l. 272-274), jamais « pas de trace » »", "([P] l. 272-274), jamais « pas de trace »" in V3N)

preuve("02 | [AU] p. 7 : activations des 10 derniers jetons", bool(P.present("AU", 7, "cache activations for the last 10 tokens for each datapoint")))
preuve("02 | [AU] p. 7 : même procédure à l'évaluation", bool(P.present("AU", 7, "Follow the same procedure to evaluate the probe")))
pages_moy = [p for p in range(1, len(P.pages("AU")) + 1)
             if re.search(r"mean (over|of|across) (all )?(the )?(token|probe)|averag\w* (over|across) (all )?(the )?token",
                          P.page_norm("AU", p, "defaut", "colle"))]
preuve("02 | [AU] : aucune page ne dit un score moyen sur les jetons (pages trouvées : %s)" % pages_moy, pages_moy == [])
preuve("02 | v3 : « en moyenne sur les jetons » et [AU p. 6] dans le même point 2",
       "en moyenne sur les jetons : sur ce même modèle" in V3N and "0,653 sur toutes les actions, sur Phi-4 [AU p. 6]" in V3N)
preuve("02 | v3 : « Ces montages agrègent par la moyenne »", "Ces montages agrègent par la moyenne" in V3N)
preuve("02 | [BX] p. 3 et [YS] p. 3 : moyenne dite", bool(P.present("BX", 3, "average scores across tokens at evaluation"))
       and bool(P.present("YS", 3, "average token activations over just the assistant's response")))

fa_p, pk_p = ligne_table("PAR", 7, "Full Averaging (Pairs)"), ligne_table("PAR", 7, "Peak Activation (Pairs)")
fa_r, pk_r = ligne_table("PAR", 7, "Full Averaging (RP)"), ligne_table("PAR", 7, "Peak Activation (RP)")
preuve("03 | [PAR] table 3 p. 7, colonne « Dilution » : moyenne > maximum, Pairs %s > %s, RP %s > %s" % (fa_p[1], pk_p[1], fa_r[1], pk_r[1]),
       float(fa_p[1]) > float(pk_p[1]) and float(fa_r[1]) > float(pk_r[1]))
preuve("03 | [PAR] table 3 p. 7, sonde RP hors dilution : maximum > moyenne, AI Liar %s > %s, Backdoors %s > %s, Sandbagging %s > %s"
       % (pk_r[0], fa_r[0], pk_r[2], fa_r[2], pk_r[4], fa_r[4]),
       float(pk_r[0]) > float(fa_r[0]) and float(pk_r[2]) > float(fa_r[2]) and float(pk_r[4]) > float(fa_r[4]))
preuve("03 | [PAR] p. 4 : jeu de dilution défini", bool(P.present("PAR", 4, "appending to the assistant's response 100 true-but-irrelevant claims")))
preuve("03 | [PAR] p. 7 : « even in scenarios specifically designed to challenge it (such as deception dilution) »",
       bool(P.present("PAR", 7, "even in scenarios specifically designed to challenge it (such as deception dilution)")))
preuve("03 | v3 : « vers le maximum seulement sous dilution » et « sauf dilution »",
       "vers le maximum seulement sous dilution" in V3N and "sauf dilution" in V3N)

preuve("04 | [AP] p. 23 : « here we train a different probe »", bool(P.present("AP", 23, "here we train a different probe")))
preuve("04 | [AP] p. 23 : « Both probes were trained on the Roleplaying dataset »", bool(P.present("AP", 23, "Both probes were trained on the Roleplaying dataset")))
preuve("04 | v3 : « meilleur que la même sonde lue sur toute la réponse » (deux lieux)",
       V3N.count("meilleur que la même sonde lue sur toute la réponse") == 2)

n026 = lignes("docs/decisions/decision-N-026-v1.md", 1, 200)
preuve("05 | N-026 : aucune mention de Bonferroni", "Bonferroni" not in n026)
preuve("05 | v3 : « hors de la famille de Bonferroni (N-026, conditions 1 à 4) »", "hors de la famille de Bonferroni (N-026, conditions 1 à 4)" in V3N)

q4 = [x for x in rangs if x[0] == "Qwen/Qwen3-4B"][0]
preuve("06 | [DYL] table 9 p. 28 : Qwen3-4B, question %s > moyenne d'Apollo %s" % (q4[3], q4[2]), q4[3] > q4[2])
preuve("06 | v3 : rangé sous « Contre » : « sonde de question basse sur Qwen3-8B (0,69) et Qwen3-4B (0,68) »",
       "Contre, sur les cas proches" in V3N and "sonde de question basse sur Qwen3-8B (0,69) et Qwen3-4B (0,68)" in V3N)
