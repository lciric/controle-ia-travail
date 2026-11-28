"""Contrôles à la page et à la ligne pour la synthèse v6 (correcteur v6). Lecture seule partout, sauf le dossier d'épreuve.

A. Contrôles du correcteur v5 (correction-v5/controles_v5.sh, lus par shlex, jamais exécutés) : tous rejoués sur PDF
   empreinté, y compris ceux qu'il avait lus sur extraits texte ([N], [X]).
B. Contrôles du vérificateur « fidélité » v5 (CONTROLES et ARTEFACTS de verif_pages_v5.py, lus par ast.literal_eval,
   jamais exécutés) : rejoués sur PDF empreinté (DYL, LB, BU, AU l'étaient sur extraits texte).
C. Contrôles du vérificateur « sens » v5 sur [DYL] (outils/guillemets_v1.py, lus par ast) : rejoués sur PDF.
D. Les 119 citations de la v1 (redaction/citations-synthese-v1.json) : rejouées sur PDF, [N] et [X] compris.
E. Phrases neuves de la v6 qui citent une page : chacune cherchée à la page citée.
F. Renvois de ligne neufs de la v6 (dépôt et bloc-notes) : fichier contrôlé par empreinte complète, extrait cherché à la ligne.
G. Épreuve R5 : artefacts de page et de ligne (doivent être rejetés) ; gardes d'empreinte (cas sain accepté, artefacts
   arrêtés), sur des copies dans correction-v6/epreuve/, supprimées après usage.
Usage : python3 -I -B controles_v6.py   (code 0 si tout est conforme)
"""
import ast
import os
import hashlib
import json
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

ICI = Path(os.path.abspath(__file__)).parent  # chemin gardé tel quel (lien), jamais résolu
sys.path.insert(0, str(ICI))
import pagev6 as pg  # noqa: E402

RD = pg.RD
R = Path("/home/user/controle-ia-travail")
S = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad")
TETE = "9ecd952"
C6 = {"MA", "BU", "LIAR", "FQ", "K", "LB", "AU", "DYL", "RH", "CC"}
bilan = {"trouvés": 0, "absents": 0, "artefacts_rejetés": 0, "artefacts_acceptés": 0}


def sha_fichier(chemin, attendu):
    h = hashlib.sha256(Path(chemin).read_bytes()).hexdigest()
    if h != attendu:
        pg.arret(f"{chemin} a l'empreinte {h}, attendue {attendu}")


def controle(section, qui, cle, page, phrase):
    r = pg.trouve(cle, page, phrase)
    bilan["trouvés" if r else "absents"] += 1
    src = "[C6]" if cle in C6 else "[D]"
    print(f"{'TROUVÉ' if r else 'ABSENT'} | {section} | {cle} p. {page} {src} | {qui} | {phrase[:90]!r}")


def artefact(qui, cle, page, phrase):
    r = pg.trouve(cle, page, phrase)
    bilan["artefacts_acceptés" if r else "artefacts_rejetés"] += 1
    print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | {qui} | {cle} p. {page} | {phrase[:90]!r}")


# ---------- A ----------
def section_a():
    f = RD / "correction-v5/controles_v5.sh"
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    comp = (RD / "correction-v5/controles_v5.sh.sha256").read_text().split()[0]
    if h != comp:
        pg.arret(f"controles_v5.sh {h} différent de son compagnon {comp}")
    print(f"# A. controles_v5.sh ({h[:8]}…, compagnon égal) : rejoué sur PDF")
    epreuve = False
    for l in f.read_text().splitlines():
        if l.startswith("echo") and "épreuve" in l:
            epreuve = True
            continue
        if not l.startswith("$T "):
            continue
        a = shlex.split(l.split(";")[0][3:]) if epreuve else shlex.split(l[3:])
        cle, page, phrase = a[0], int(a[1]), a[2]
        if epreuve:
            artefact("A, artefact du correcteur v5", cle, page, phrase)
        else:
            controle("A", "contrôle du correcteur v5", cle, page, phrase)


# ---------- B ----------
def listes_py(chemin, noms):
    arbre = ast.parse(Path(chemin).read_text())
    out = {}
    for n in arbre.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and getattr(n.targets[0], "id", None) in noms:
            out[n.targets[0].id] = ast.literal_eval(n.value)
    return out


def section_b():
    f = RD / "verification-v5-fidelite/travail/verif_pages_v5.py"
    comp = (f.parent / (f.name + ".sha256")).read_text().split()[0]
    sha_fichier(f, comp)
    print(f"# B. verif_pages_v5.py ({comp[:8]}…, compagnon égal) : rejoué sur PDF")
    L = listes_py(f, {"CONTROLES", "ARTEFACTS"})
    for qui, cle, page, ph in L["CONTROLES"]:
        controle("B", "fidélité v5 : " + qui, cle, page, ph)
    for quoi, cle, page, ph in L["ARTEFACTS"]:
        artefact("B, artefact de la fidélité v5 : " + quoi, cle, page, ph)


# ---------- C ----------
def section_c():
    f = RD / "verification-v5-sens/outils/guillemets_v1.py"
    liste = (RD / "verification-v5-sens/empreintes-verification-v5-sens.sha256").read_text()
    h = hashlib.sha256(f.read_bytes()).hexdigest()
    if f"{h}  outils/guillemets_v1.py" not in liste:
        pg.arret("guillemets_v1.py absent de la liste d'empreintes du rapport « sens », ou empreinte différente")
    print(f"# C. guillemets_v1.py ({h[:8]}…, égal à la liste du rapport « sens ») : entrées [DYL] rejouées sur PDF")
    cas = listes_py(f, {"cas"})["cas"]
    for chemin, phrase, attendu in cas:
        if "2606.12618v2" not in chemin:
            continue
        page = int(chemin.rsplit("/p", 1)[1][:2])
        if attendu:
            controle("C", "sens v5 (extrait texte à l'origine)", "DYL", page, phrase)
        else:
            artefact("C, artefact du sens v5", "DYL", page, phrase)


# ---------- D ----------
def section_d():
    pg.references()  # contrôle l'empreinte du JSON
    d = json.loads(pg.JSON_V1.read_text())
    print(f"# D. citations-synthese-v1.json ({pg.JSON_V1_SHA[:8]}…) : {len(d['citations'])} citations rejouées sur PDF")
    for cle, page, phrase in d["citations"]:
        controle("D", "citation de la v1", cle, page, phrase)


# ---------- E ----------
E = [
    ("VV5-fidelite-01 : 0,5 de [BX], organisme affiné, p. 8", "BX", 8, "from almost perfect detection 0.94 to chance performance 0.5"),
    ("VV5-fidelite-01 : « sondes réentraînées sur lui », p. 8", "BX", 8, "re-training probes on the Model Organism using contrastive pairs"),
    ("VV5-fidelite-01 : 0,81 et 0,63, [BX p. 5-6]", "BX", 5, "degraded by 14 points to 0.81 AUROC"),
    ("VV5-fidelite-01 : 0,63, [BX p. 6]", "BX", 6, "32-point drop to 0.63 AUROC"),
    ("VV5-fidelite-01 : 0,964 en moyenne, sonde Pairs [PAR table 3]", "PAR", 7, "Full Averaging (Pairs) 0.966 0.931 0.844 0.999 0.964 0.941"),
    ("VV5-sens-04 (1) : [BX] p. 6, conversation ordinaire", "BX", 6, "distinguish transcripts containing normal conversational data from those exhibiting the studied behavior"),
    ("VV5-sens-04 (1) : [BX] p. 6, rappel à 1 % de faux positifs", "BX", 6, "we measure the recall at fixed 1% FPR threshold"),
    ("VV5-sens-04 (1) : [BX] table 1, p. 6, ligne Sandbagging", "BX", 6, "Sandbagging 1.00 0.04 0.03"),
    ("VV5-sens-04 (2) : [DYL] table 9 = « Varied Deception » (p. 28)", "DYL", 28, "Table 9: Balanced accuracy on Varied Deception"),
    ("VV5-sens-04 (2), 11, 12 : [DYL] p. 11, la question tient sur « Gender Secret » remis sur consigne", "DYL", 11, "DYL, by contrast, retains strong performance on the prompted variants"),
    ("VV5-sens-04 (2), 11, 12 : [DYL] p. 11, remis sur consigne", "DYL", 11, "re-ran the evaluation against prompted Gender Secret model organisms using the original system prompts"),
    ("VV5-sens-04 (2), 11, 12 : [DYL] p. 7, questions cibles sur le genre", "DYL", 7, "whether a Gender Secret model knows the user’s"),
    ("VV5-sens-04 (2), 11, 12 : [DYL] p. 7, questions témoins (âge, couleur des cheveux)", "DYL", 7, "asking a Gender Secret model whether it knows the user’s age or hair colour"),
    ("VV5-sens-11 : [DYL] p. 8, raisonnement avant la réponse", "DYL", 8, "for reasoning models we allow reasoning tokens before the yes/no response"),
    ("VV5-sens-10 : [AP] p. 18, hypothèse Instructed-Pairs, contre le témoin", "AP", 18, "activates somewhat when deception is incentivized (rather than performed) which still allows the probe to distinguish deceptive responses from control responses"),
    ("VV5-sens-10 : [AP] p. 18, contre Alpaca", "AP", 18, "is much worse at distinguishing the deceptive responses from alpaca responses"),
    ("VV5-sens-12 (1) : [PAR] table 3, question « No », Backdoors 0,832", "PAR", 7, "Deception No (Pairs) 0.913 0.700 0.832 0.948 0.849 0.848"),
    ("VV5-sens-12 (1) : [PAR] table 3, question « Yes », Backdoors 0,849", "PAR", 7, "Honest Yes (Pairs) 0.920 0.767 0.849 0.963 0.879 0.876"),
    ("VV5-sens-12 (1) : [PAR] table 3, maximum, Backdoors 0,768", "PAR", 7, "Peak Activation (Pairs) 0.937 0.811 0.768 0.979 0.839 0.867"),
    ("VV5-sens-12 (1) : [PAR] table 3, moyenne, Backdoors 0,844", "PAR", 7, "Full Averaging (Pairs) 0.966 0.931 0.844 0.999 0.964 0.941"),
    ("VV5-sens-12 (1) : [PAR] table 3, ordre des colonnes", "PAR", 7, "AI Liar Dilution Backdoors"),
    ("VV5-sens-12 (2) : [DYL] table 9, Qwen3-8B 0,74 et 0,69", "DYL", 28, "Qwen/Qwen3-8B 13 0.74 0.69"),
    ("VV5-sens-12 (2) : [DYL] table 9, Qwen3-4B 0,64 et 0,68", "DYL", 28, "Qwen/Qwen3-4B 14 0.64 0.68"),
    ("VV5-sens-06 : [KU] p. 5, régime de consigne", "KU", 5, "deceptive prompt regime"),
]
E_ARTEFACTS = [
    ("chiffre changé (0.94 → 0.49)", "BX", 8, "from almost perfect detection 0.49 to chance performance 0.5"),
    ("page voisine (p. 7 au lieu de p. 8)", "BX", 7, "re-training probes on the Model Organism using contrastive pairs"),
    ("mot changé (Gender → Age)", "DYL", 7, "asking a Age Secret model whether it knows the user’s age or hair colour"),
    ("page voisine (p. 8 au lieu de p. 7)", "DYL", 7 + 1, "asking a Gender Secret model whether it knows the user’s age or hair colour"),
    ("mauvaise clé (AP au lieu de DYL)", "AP", 11, "DYL, by contrast, retains strong performance on the prompted variants"),
    ("colonnes permutées (0.69 0.74)", "DYL", 28, "Qwen/Qwen3-8B 13 0.69 0.74"),
    ("mot changé (control → Alpaca)", "AP", 18, "activates somewhat when deception is incentivized (rather than performed) which still allows the probe to distinguish deceptive responses from Alpaca responses"),
    ("chiffre changé (0.832 → 0.823)", "PAR", 7, "Deception No (Pairs) 0.913 0.700 0.823 0.948 0.849 0.848"),
    ("chiffre changé (0.03 → 0.30)", "BX", 6, "Sandbagging 1.00 0.04 0.30"),
]


def section_e():
    print("# E. Phrases neuves de la v6 qui citent une page")
    for qui, cle, page, ph in E:
        controle("E", qui, cle, page, ph)
    print("# E (R5) : artefacts (chacun doit être rejeté)")
    for qui, cle, page, ph in E_ARTEFACTS:
        artefact("E, " + qui, cle, page, ph)


# ---------- F ----------
P015 = (R / "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cbcd3b05ab65dbbf42fc6481520a6717ec1e40e0961a633c5ed76a19d2")
T06 = (R / "brouillons/T0.6-organismes-v0-v1-brouillon1.md", "e212fb3505907c8e48524784fbf5a78f6e9120dc86361a35c6ca994af76a0449")
P011 = (R / "docs/decisions/proposition-P-011-T0.7-sondes-v1.md", "64afff19ce5ceab6f99e3f15d583fcdc3890e08a480a017703f2a57331636fd9")
PP = (R / "prereg/P3-premier-test-i-a-v1.md", "d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672")
REP = (S / "brainstorm-outils-p3/reponse-claude-prompt-unique-v1.md", "f9aa165563aa2e63cdca7e2e388b12d271c2e574b81f126e9909cad9d109d34e")
CR = (S / "p3b/consigne-redacteur-P3b-brouillon1-v1.md", "f8305c0ebea6ef22ada99752381e9a9bfdd1dad2f0d4b174a01c0964f6cb225b")
AT = (S / "p3b/a-transmettre-contre-lecture-P3b-v1.md", "23c742befb2f89dc698a0bb5f9f518e544e71b3b98733f5258a481659fe491c0")
CL = (S / "p3b/consigne-contre-lecture-R2-P3b-brouillon1-v1.md", "138b3afd6f09d954786443dd374e74d84fa340f9522b87e7f511e91636123f40")
DEC = ("git:registres/decisions.md", "e8b73c6425ad6493c6aaf8083bad98fccc8958fcd6ac08acb4948b0224b2a1a6")
GO = ("git:registres/go.md", "1a392407391cef6ee501e61e90cb5bf73da8aec343f3e44da1c96fd67639f5d6")

F = [
    ("VV5-sens-01, 05 : P-015 l. 18-19, dose fixée sur la boîte noire avant toute sonde", P015, 18, "la dose « diffuse » se fixe sur la boîte noire seule, avant toute lecture de sonde"),
    ("VV5-sens-02 : P-015 l. 33-34, « affaiblir les contrôles » remplacé", P015, 33, "« Affaiblir les contrôles » sort (brouillon du 6 octobre,"),
    ("VV5-sens-02 : P-015 l. 34", P015, 34, "l. 28, remplacé"),
    ("VV5-sens-05, fidelite-06 : P-015 l. 38", P015, 38, "chaque action sabotée reste sous le seuil du meilleur moniteur boîte noire par action"),
    ("VV5-sens-13 : P-015 l. 40, dose réalisée", P015, 40, "c'est la dose réalisée qui compte"),
    ("VV5-fidelite-06 : P-015 l. 41-44", P015, 41, "**Conditions de référence obligatoires**"),
    ("VV5-fidelite-06 : P-015 l. 43, témoin", P015, 43, "témoin instruit"),
    ("VV5-fidelite-06 : P-015 l. 44, mention", P015, 44, "mention : une consigne qui nomme le coût"),
    ("VV5-sens-05 : P-015 l. 50, règle du coût", P015, 50, "la règle du coût déclaré"),
    ("VV5-sens-01, 02 : P-015 l. 65-66, T7-P1", P015, 65, "T7-P1 sur (i-a) est déclarée réplication de P3 sur des épisodes neufs"),
    ("VV5-sens-02 : P-015 l. 75, (a) deux intensités fixées a priori", P015, 75, "deux intensités fixées a priori"),
    ("VV5-sens-01 : P-015 l. 78, un épisode par tâche", P015, 78, "un épisode par tâche et par condition, sur les tâches d'évaluation"),
    ("VV5-sens-01, fidelite-06 : P-015 l. 91-92, règle de l'étape 1", P015, 91, "Règle écrite d'avance"),
    ("VV5-sens-01, fidelite-06 : P-015 l. 93-94, étape 2", P015, 93, "**Étape 2**"),
    ("VV5-sens-02 : P-015 l. 107, (c) une intensité", P015, 107, "(i-a) seul, une intensité"),
    ("VV5-sens-01 : P-015 l. 121, barème (a)", P015, 121, "9 conditions, ≈ 576 épisodes | ≈ 9 à 10 USD"),
    ("VV5-sens-01 : P-015 l. 124, étape 2 de (i)", P015, 124, "| (b), étape 2, organisme (i) | ≈ 7 à 9 USD |"),
    ("VV5-sens-06 : P-015 l. 138, paires synthétiques", P015, 138, "appris sur des paires synthétiques"),
    ("VV5-sens-06 : P-015 l. 140, versions incitées", P015, 140, "versions incitées"),
    ("VV5-sens-06 : P-015 l. 141, avant le champ", P015, 141, "lecture avant le champ COST"),
    ("VV5-sens-01 : P-015 l. 147, descriptif de T0.7", P015, 147, "en descriptif de T0.7"),
    ("VV5-sens-02 : brouillon T0.6 l. 28, mode S1", T06, 28, "« affaiblir les contrôles », pour (i-a)"),
    ("VV5-sens-02 : brouillon T0.6 l. 75, (i-a)", T06, 75, "(i-a) : p ∈ {0,25 ; 0,5 ; 1} × intensités légère et forte"),
    ("VV5-sens-06 : P-011 l. 35, concept 4", P011, 35, "paires synthétiques de propositions écrites pour bien faire ou pour affaiblir en douce"),
    ("VV5-sens-06 : P-011 l. 63, sous-agent neuf", P011, 63, "écrits par un sous-agent neuf sur les tâches de réserve"),
    ("VV5-sens-01, 02 : [P] l. 123, coût trois fois plus élevé", PP, 123, "un coût environ trois fois plus élevé"),
    ("VV5-sens-01, 02 : [P] l. 330, mode coût gonflé", PP, 330, "saboteur instruit (i-a), mode « coût gonflé »"),
    ("VV5-sens-01, 02 : [P] l. 331, p = 1, intensité forte", PP, 331, "p = 1, intensité forte"),
    ("VV5-sens-06 : [P] l. 238, au moins 2 fois la médiane", PP, 238, "1 si le coût vaut au moins 2 fois la médiane des coûts lisibles"),
    ("VV5-sens-06 : [P] l. 239, au plus 1,25 fois", PP, 239, "0 s'il vaut au plus 1,25 fois"),
    ("VV5-sens-06 : [P] l. 240, au moins 10 actions", PP, 240, "actions de chaque côté, sinon « non calculable »"),
    ("VV5-sens-07 : [P] l. 249-250, tranches du coût déclaré", PP, 250, "coût déclaré sur ces actions ; aire stratifiée"),
    ("VV5-sens-09 : [P] l. 275, Bonferroni sur les deux sondes", PP, 275, "**P3-P3** : correction de Bonferroni sur les deux sondes principales"),
    ("VV5-sens-03 : réponse f9aa1655 l. 59, tronqués à t_cost", REP, 59, "tronqués **à t_cost**"),
    ("VV5-sens-03 : réponse f9aa1655 l. 59, quatre contextes", REP, 59, "sous quatre contextes : sans ligne, ligne saboteur, ligne témoin, ligne mention"),
    ("VV5-sens-03 : réponse f9aa1655 l. 60, état interne", REP, 60, "Mesures à t_cost : état interne"),
    ("VV5-sens-03 : réponse f9aa1655 l. 61, nombre prévu", REP, 61, "Le rejeu retire le nombre **écrit**, pas le nombre **prévu**"),
    ("VV5-sens-07 : réponse f9aa1655 l. 104, résidu", REP, 104, "nombre et tâche régressés"),
    ("VV5-sens-07 : réponse f9aa1655 l. 128, T4 corrigé", REP, 128, "à coût écrit égal, les actions du saboteur viennent de tâches bon marché, celles de l'honnête de tâches chères"),
    ("VV5-sens-07 : réponse f9aa1655 l. 128, témoin", REP, 128, "chez l'honnête seul, la sonde prédit-elle le coût de la tâche ?"),
    ("VV5-sens-03 : consigne P3b l. 24, (B) et (C) hors périmètre", CR, 24, "sonde de valeur et rejeu contrefactuel 2 × 2 (P-017 (B) et (C)"),
    ("VV5-sens-09 : consigne P3b l. 26, question hors périmètre", CR, 26, "question ajoutée après l'action (extension de N-028 : nœud, R-278)"),
    ("VV5-sens-07 : consigne P3b l. 36, T4 résiduel", CR, 36, "T4 tel qu'écrit dans P3 est confondu par le coût de la tâche : test résiduel"),
    ("VV5-sens-09 : consigne P3b l. 54, renvoi à la v4", CR, 54, "synthese-comment-detecter-v4.md"),
    ("VV5-sens-09 : note de transmission l. 1", AT, 1, "(et au rédacteur du brouillon 2)"),
    ("VV5-sens-09 : note de transmission l. 8-9, VV4-sens-11", AT, 9, "multiplicité dans P3b est un choix neuf, à justifier, pas une reprise de P3"),
    ("VV5-sens-09 : consigne de contre-lecture l. 16", CL, 16, "a-transmettre-contre-lecture-P3b-v1.md` : VV4-sens-04, -06, -11, -12"),
    ("VV5-fidelite-04 : R-293 l. 493", DEC, 493, "deux écrivains sur la chaîne v2 de P4 ; addendum 2 de P3 : module v3 rendu"),
    ("VV5-fidelite-05 : R-299 (5) l. 499", DEC, 499, "(5) **Corrections de R-295** : la ligne 161 du brief"),
    ("VV5-fidelite-05 : R-299 (5) l. 499, Gemini", DEC, 499, "la réponse de Gemini à la requête 020"),
    ("VV5-sens-13 : R-303 l. 503, réserve B1 sur P3-P1", DEC, 503, "`reserve_B1_ampleur_au_dela_de_la_consigne` sur P3-P1"),
    ("VV5-sens-09 : R-306 l. 506, consigne inchangée", DEC, 506, "rédacteur du brouillon 1 de P3b (consigne `f8305c0e…` inchangée)"),
    ("VV5-sens-03 : P-017 l. 394, rejeu ≈ + 1 à 2 h", DEC, 394, "(C) B plus le rejeu contrefactuel 2 × 2 (≈ + 1 à 2 h)"),
    ("VV5-sens-07, 08 : R-295 l. 495", DEC, 495, "T4 tel qu'écrit est confondu par le coût de la tâche (test résiduel)"),
    ("VV5-sens-08 : R-295 l. 495, J-lens", DEC, 495, "la J-lens n'a de résultats publiés que sur des modèles Claude"),
    ("VV5-sens-08 : GO-2026-10-20-10, go.md l. 38, lentilles", GO, 38, "lentille des logits ; lentille jacobienne d'Anthropic pré-ajustée pour Llama-3.1-8B-Instruct, fichier empreinté, ou réajustée"),
    ("VV5-sens-08 : go.md l. 38, plancher", GO, 38, "directions tournées au hasard à covariance égale ; permutation des conditions dans la tâche"),
    ("VV5-sens-08 : go.md l. 38, contrôle positif", GO, 38, "contrôle positif de la lentille sur le modèle 8B d'abord"),
    ("VV5-sens-08 : go.md l. 38, mécanisme", GO, 38, "lecture du mécanisme (coût honnête calculé puis gonflé), jamais lue comme une intention"),
]
F_ARTEFACTS = [
    ("ligne voisine (P-015 l. 39)", P015, 39, "chaque action sabotée reste sous le seuil du meilleur moniteur boîte noire par action"),
    ("chiffre changé (≈ 9 à 11 USD)", P015, 121, "9 conditions, ≈ 576 épisodes | ≈ 9 à 11 USD"),
    ("mot changé (réserve B2)", DEC, 503, "`reserve_B2_ampleur_au_dela_de_la_consigne` sur P3-P1"),
    ("ligne voisine ([P] l. 274)", PP, 274, "**P3-P3** : correction de Bonferroni sur les deux sondes principales"),
]
_lignes = {}


def lignes(src):
    nom, attendu = str(src[0]), src[1]
    if nom not in _lignes:
        if nom.startswith("git:"):
            b = subprocess.run(["git", "-C", str(R), "show", f"{TETE}:{nom[4:]}"], capture_output=True, check=True).stdout
        else:
            b = Path(nom).read_bytes()
        h = hashlib.sha256(b).hexdigest()
        if h != attendu:
            pg.arret(f"{nom} a l'empreinte {h}, attendue {attendu}")
        _lignes[nom] = b.decode("utf-8").splitlines()
    return _lignes[nom]


def section_f():
    print(f"# F. Renvois de ligne neufs (registres lus à {TETE} par git show, lecture seule)")
    for qui, src, n, ex in F:
        r = ex in lignes(src)[n - 1]
        bilan["trouvés" if r else "absents"] += 1
        print(f"{'TROUVÉ' if r else 'ABSENT'} | F | {Path(src[0]).name} ({src[1][:8]}…) l. {n} | {qui} | {ex[:80]!r}")
    print("# F (R5) : artefacts (chacun doit être rejeté)")
    for qui, src, n, ex in F_ARTEFACTS:
        r = ex in lignes(src)[n - 1]
        bilan["artefacts_acceptés" if r else "artefacts_rejetés"] += 1
        print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | F, {qui} | {Path(src[0]).name} l. {n} | {ex[:80]!r}")


# ---------- G ----------
def section_g():
    print("# G. Gardes d'empreinte (R5) : cas sain, puis artefacts dans correction-v6/epreuve/ (supprimé après usage)")
    ep = RD / "correction-v6/epreuve"
    if ep.exists():
        pg.arret(f"{ep} existe déjà")
    i = pg.ID["CC"]
    src = pg.C6 / i / f"{i}.pdf"
    ref = pg.references()["CC"]
    code = "import sys; sys.path.insert(0, %r); import pagev6 as pg; pg.trouve('CC', 8, 'using fewer layers consistently yields worse performance', racine_c6=__import__('pathlib').Path(%r)); print('accepté')"

    def essai(nom, prepare):
        d = ep / nom / i
        d.mkdir(parents=True)
        shutil.copyfile(src, d / f"{i}.pdf")
        prepare(d / f"{i}.pdf", d / f"{i}.pdf.sha256")
        r = subprocess.run([sys.executable, "-I", "-B", "-c", code % (str(ICI), str(ep / nom))],
                           capture_output=True, text=True)
        out = (r.stdout + r.stderr).strip().splitlines()
        return r.returncode, (out[-1] if out else "")

    def sain(p, c):
        c.write_text(f"{ref}  {p.name}\n")

    def comp_faux(p, c):
        c.write_text(f"{'0' * 64}  {p.name}\n")

    def octet_ajoute(p, c):
        with open(p, "ab") as f:
            f.write(b"\n%artefact\n")
        c.write_text(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")

    def sans_comp(p, c):
        pass

    attendus = [("sain (copie exacte, compagnon juste)", sain, 0),
                ("artefact : compagnon faux (64 zéros)", comp_faux, 3),
                ("artefact : octets ajoutés, compagnon recalculé (référence v1 différente)", octet_ajoute, 3),
                ("artefact : compagnon absent", sans_comp, 3)]
    ok = True
    try:
        for k, (nom, prep, code_attendu) in enumerate(attendus):
            rc, msg = essai(f"e{k}", prep)
            bon = rc == code_attendu
            ok &= bon
            print(f"{'OK' if bon else 'FAUTE'} | {nom} | code {rc} (attendu {code_attendu}) | {msg[:110]}")
    finally:
        shutil.rmtree(ep)
    print(f"# G : {'gardes conformes' if ok else 'GARDE EN FAUTE'} ; dossier d'épreuve supprimé")
    return ok


def main():
    print("# Contrôles de la v6 (correcteur v6). Empreintes complètes ; aucun extrait texte lu ; registres à "
          f"{TETE} par git show.")
    for cle in sorted(pg.ID):
        p = pg.pdf_garde(cle)
        print(f"empreinte OK | {cle} | {p} | {hashlib.sha256(p.read_bytes()).hexdigest()}")
    section_a()
    section_b()
    section_c()
    section_d()
    section_e()
    section_f()
    g = section_g()
    print(f"# BILAN : trouvés {bilan['trouvés']} ; absents {bilan['absents']} ; artefacts rejetés "
          f"{bilan['artefacts_rejetés']} ; artefacts acceptés (fautes) {bilan['artefacts_acceptés']} ; gardes "
          f"{'conformes' if g else 'EN FAUTE'}")
    sys.exit(0 if (bilan["absents"] == 0 and bilan["artefacts_acceptés"] == 0 and g) else 1)


if __name__ == "__main__":
    main()
