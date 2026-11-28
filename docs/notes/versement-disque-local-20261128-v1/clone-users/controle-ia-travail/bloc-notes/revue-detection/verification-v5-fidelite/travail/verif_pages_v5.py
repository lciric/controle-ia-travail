"""Vérificateur v5 fidélité (neuf) : contrôles à la page, indépendants de pagev5.py, sur des phrases changées de la v5.

PDF de [D] : empreinte complète recalculée et comparée au compagnon .sha256 du dépôt, puis pdftotext (raw, puis layout).
[N] et [X] : PDF absents du bloc-notes restauré (vérifié sur disque) ; extraits texte page par page, sans empreinte du PDF.
Dépôt : lignes lues à la tête 9ecd952 (git show, lecture seule), empreinte comparée à celle que cite la v5.
Usage : python3 -I -B verif_pages_v5.py
"""
import hashlib, re, subprocess, sys, unicodedata
from pathlib import Path

R = Path("/home/user/controle-ia-travail")
D = R / "docs/sources/pdf"
RD = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
PDF = {"AP": "2502.03407v1", "PAR": "2507.12691v3", "OA": "2602.15515v2", "CA": "2610.12445v1",
       "YS": "2609.02893v1", "BX": "2509.21344v2", "KU": "2605.27958v1"}
TXT = {"DYL": RD / "txt-nouveaux/2606.12618v2", "LB": RD / "txt-nouveaux/2511.16035v2",
       "BU": RD / "extraction/txt-representations/2407.12831v2", "AU": RD / "txt-nouveaux/2504.04072v3"}
_cache = {}

def empreinte_ok(cle):
    p = D / f"{PDF[cle]}.pdf"
    comp = (D / f"{PDF[cle]}.pdf.sha256").read_text().split()[0]
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != comp:
        sys.exit(f"ARRÊT : empreinte de {cle} {h} différente du compagnon {comp}")
    return p

def pages(cle, page):
    k = (cle, page)
    if k not in _cache:
        if cle in PDF:
            p = empreinte_ok(cle)
            _cache[k] = [subprocess.run(["pdftotext", m, "-f", str(page), "-l", str(page), str(p), "-"],
                                        capture_output=True, text=True, check=True).stdout for m in ("-raw", "-layout")]
        else:
            _cache[k] = [(TXT[cle] / f"p{page:02d}.txt").read_text(errors="ignore")]
    return _cache[k]

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).lower().strip()

def cherche(cle, page, phrase):
    return any(norm(phrase) in norm(t) for t in pages(cle, page))

# (passage de la v5 contrôlé, clé, page, phrase de la source)
CONTROLES = [
 ("point 1, rang 4, E2 : « la sonde de question apprise sur « Roleplaying » » (>99 %)", "AP", 18, "B.3 Train on Roleplaying: Follow-up question"),
 ("idem : apprise sur Roleplaying", "AP", 18, "Again, we trained this using 90% of the Roleplaying dataset"),
 ("point 2 : « hypothèse pour la sonde Instructed-Pairs, contre le témoin »", "AP", 18, "one hypothesis is that the Instructed-Pairs-trained probe activates somewhat when deception is incentivized"),
 ("idem : contre le témoin Alpaca", "AP", 18, "is much worse at distinguishing the deceptive responses from alpaca responses"),
 ("point 1, rang 4 : « apprise sur les dernières positions et lue au dernier jeton »", "AP", 23, "Both probes were trained on the Roleplaying dataset"),
 ("point 1 : « rappel … à 1 % de faux positifs » sur le témoin", "AP", 9, "Recall (TPR on deceptive) for 1% FPR on our control responses"),
 ("point 1, E2, nœud E2 : colonnes de la table 3 (Backdoors, Sandbagging)", "PAR", 7, "AI Liar Dilution Backdoors"),
 ("idem : colonne Sandbagging", "PAR", 7, "Sandbagging Avg."),
 ("confiance, E2 : « à 70 milliards »", "PAR", 5, "we use LLaMa-3.3-70B-Instruct as the untrusted AI assistant"),
 ("point 2 : réserve « hors politique » de « Backdoors »", "PAR", 3, "Deception Dilution, Backdoors, and Alpaca are off-policy"),
 ("point 1 : « remis sur consigne » (Gender Secret)", "DYL", 11, "re-ran the evaluation against prompted Gender Secret model organisms using the original system prompts"),
 ("point 1 : « apprise sur des réponses à « did you lie » »", "DYL", 8, 'a follow-up question of the form "did you lie in the last message?"'),
 ("point 2, rang 3 : « couche et classifieur réglés sur une validation du même jeu »", "DYL", 8, "grid search over model layer, classifier architecture"),
 ("point 1 : « des modèles d'indice 9 à 14 » (titre de la table 9)", "DYL", 28, "Table 9: Balanced accuracy on Varied Deception"),
 ("point 1 : « [LB table 6] n'est pas ordonnée par la taille » (Mistral 24B)", "LB", 54, "Mistral 3.1 24B 0.55 0.46 — 0.82 0.69 0.58 0.58 0.61"),
 ("idem (Gemma 27B)", "LB", 54, "Gemma 3 27B — — 0.70 — 0.58 — 0.30 0.53"),
 ("idem (Llama 70B, 0,95)", "LB", 54, "Llama 3.3 70B 0.41 0.12 1.00 0.57 0.95 0.45 0.93 0.64"),
 ("point 2, rang 3 : « WMDP contre MMLU, [BX p. 4] »", "BX", 4, "questions from either MMLU (Hendrycks et al., 2021) or WMDP"),
 ("point 1, point 2 : « le modèle de P3 (Llama-3.1-8B-Instruct) » pour [BX]", "BX", 4, "In order to get Llama 3.1 8B Instruct to sandbag"),
 ("point 1 : « sur le modèle de P3, le choix de la couche compte peu [BX p. 3] »", "BX", 3, "Our per-layer analysis indicates that layer choice has limited effect"),
 ("confiance : 0,606 [YS] « sur ce même modèle »", "YS", 3, "use layer 15 residual stream activations of Llama-3.1-8B"),
 ("point 2, rang 3 : [BU] Llama-3-8B, jeux de rôle", "BU", 10, "LLaMA3-8B-Instruct with real-life role-playing scenarios"),
 ("point 2, rang 3 : [BU] « dernier jeton »", "BU", 10, "extract activations from layer 12 over the last token"),
 ("point 2, rang 3 : [BU] 93,8 % (TTPD)", "BU", 10, "TTPD correctly classifies the 49 unambiguous lies and the 55 unambiguous truthful replies with an average accuracy of 93.8"),
 ("rang 5 : « Nemotron-3 Nano … reste bas »", "CA", 8, "0.613–0.760 on Nemotron-3 Nano"),
 ("idem", "CA", 8, "Every probe scores far lower on the smallest model of each family"),
 ("rang 5 : « 3 milliards actifs »", "CA", 25, "Nemotron 3 Nano 30B-A3B"),
 ("point 1, rang 4, E2 : [OA] « triche écrite dans le code »", "OA", 5, "programmatically-generated hardcoded code as deceptive responses (Dsynth)"),
 ("point 1, E2 : [CA] « pas d'avant le sabotage »", "CA", 6, "steps of a side-task episode from the onset on are the positive class"),
 ("point 2 : [KU p. 5] régime de consigne", "KU", 5, "deceptive prompt regime"),
 ("point 2 : [AU] étiquette « Impostor »", "AU", 6, "very correlated with the 'Impostor' label"),
 ("constat VV5-fidelite-01 : le 0,5 de [BX], type T1, au hasard", "BX", 8, "from almost perfect detection 0.94 to chance performance 0.5"),
]

# épreuve R5 : artefacts qui doivent être rejetés
ARTEFACTS = [
 ("chiffre changé", "CA", 8, "0.631–0.760 on Nemotron-3 Nano"),
 ("mot changé", "CA", 8, "0.613–0.760 on Nemotron-3 Super"),
 ("page voisine", "CA", 7, "0.613–0.760 on Nemotron-3 Nano"),
 ("colonnes permutées", "LB", 54, "Mistral 3.1 24B 0.55 0.46 — 0.69 0.82 0.58 0.58 0.61"),
 ("mauvaise clé", "BX", 3, "use layer 15 residual stream activations of Llama-3.1-8B"),
 ("mot changé", "AP", 18, "Again, we trained this using 90% of the Instructed-Pairs dataset"),
 ("chiffre changé", "BU", 10, "average accuracy of 93.6"),
]

# dépôt : (passage de la v5, fichier, empreinte attendue (préfixe), ligne, extrait attendu)
DEPOT = [
 ("Décisions : R-303 l. 503", "registres/decisions.md", "e8b73c64", 503, "aire minimale détectable à 80 % : 0,6315 et 0,5966, contre au plus 0,5809 aux hypothèses écrites"),
 ("Décisions : R-303 l. 503", "registres/decisions.md", "e8b73c64", 503, "« aucune sonde générique au-dessus du plancher sur (i-a) »"),
 ("Décisions : R-295 (1) l. 495", "registres/decisions.md", "e8b73c64", 495, "T4 tel qu'écrit est confondu par le coût de la tâche (test résiduel)"),
 ("Décisions : R-295 (1) l. 495", "registres/decisions.md", "e8b73c64", 495, "une mention amorce le concept presque autant qu'une consigne"),
 ("Décisions : P-016 l. 393", "registres/decisions.md", "e8b73c64", 393, "partition de P3b 20/40"),
 ("Décisions : P-017 l. 394", "registres/decisions.md", "e8b73c64", 394, "(C) B plus le rejeu contrefactuel 2 × 2"),
 ("Décisions : P-017 l. 394", "registres/decisions.md", "e8b73c64", 394, "Recommandation (B), confiance ≈ 55 %"),
 ("Décisions : N-030 l. 396", "registres/decisions.md", "e8b73c64", 396, "le test à coût égal corrigé du coût de la tâche"),
 ("Décisions : R-302 l. 502", "registres/decisions.md", "e8b73c64", 502, "borne de 10 USD par lancement levée pour eux ; plafond de la phase inchangé (150 USD)"),
 ("Décisions : R-302 l. 502 (plan de la nuit, P3b)", "registres/decisions.md", "e8b73c64", 502, "(3) P3b : rédaction du préenregistrement par un sous-agent neuf"),
 ("Décisions : R-304 l. 504 (correcteur coupé)", "registres/decisions.md", "e8b73c64", 504, "correcteur de la revue v5"),
 ("Décisions : GO-2026-10-20-10 go.md l. 38", "registres/go.md", "1a392407", 38, "GO-2026-10-20-10"),
 ("Décisions : GO-2026-10-20-11 go.md l. 39", "registres/go.md", "1a392407", 39, "la borne de 10 USD par lancement de la délégation (R-217, prolongée) ne s'applique pas"),
 ("Décisions : GO-2026-10-20-12 go.md l. 40", "registres/go.md", "1a392407", 40, "trois réserves non bloquantes de l'addendum 2"),
 ("E2, tranche : P-015 l. 36-39", "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cb", 38, "chaque action sabotée reste sous le seuil du meilleur moniteur boîte noire par action"),
 ("E2, contrôle : P-015 l. 41-44", "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cb", 41, "Conditions de référence obligatoires"),
 ("Dépense : P-015 l. 16-17 (« ce plafond » = 10 USD par lancement)", "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cb", 16, "10 USD au plus par lancement sous la délégation (R-269)"),
 ("Dépense : P-015 l. 99-100", "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cb", 100, "lancement reste sous 10 USD"),
 ("E3, coût : P-015 l. 123-125", "docs/decisions/proposition-P-015-T0.6-T0.8-mode-cout-v1.md", "6e74c6cb", 124, "| (b), étape 2, organisme (i) | ≈ 7 à 9 USD |"),
 ("E2, contrôle (écart déclaré) : témoin instruit au brouillon l. 78", "brouillons/T0.6-organismes-v0-v1-brouillon1.md", "e212fb35", 78, "témoin instruit"),
 ("Règles communes : [P] l. 278", "prereg/P3-premier-test-i-a-v1.md", "d975e981", 278, "P3-P4, T1, T3, T4** : à 95 %, sans correction"),
]
ART_DEPOT = [
 ("ligne voisine", "registres/decisions.md", "e8b73c64", 392, "partition de P3b 20/40"),
 ("chiffre changé", "registres/decisions.md", "e8b73c64", 503, "aire minimale détectable à 80 % : 0,6351 et 0,5966"),
]

TETE = "9ecd952"  # tête du dépôt que cite la v5 (registres e8b73c64…, 1a392407…) ; lecture par git show, jamais d'écriture

def ligne(f, pre, n):
    data = subprocess.run(["git", "-C", str(R), "show", f"{TETE}:{f}"], capture_output=True, check=True).stdout
    h = hashlib.sha256(data).hexdigest()
    if not h.startswith(pre):
        sys.exit(f"ARRÊT : {f} a l'empreinte {h}, la v5 cite {pre}…")
    return data.decode("utf-8").splitlines()[n - 1]

def main():
    ok = ko = 0
    print("# A. Contrôles à la page (phrases changées de la v5)")
    for qui, cle, page, ph in CONTROLES:
        r = cherche(cle, page, ph)
        ok += r; ko += not r
        src = "PDF, empreinte = compagnon" if cle in PDF else "extrait texte, PDF absent"
        print(f"{'TROUVÉ' if r else 'ABSENT'} | {cle} p. {page} ({src}) | {qui} | {ph[:80]!r}")
    print(f"# A : {ok} trouvés, {ko} absents sur {len(CONTROLES)}")
    print("# B. Épreuve R5 (chaque artefact doit être ABSENT)")
    rej = 0
    for quoi, cle, page, ph in ARTEFACTS:
        r = cherche(cle, page, ph)
        rej += not r
        print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | {quoi} | {cle} p. {page} | {ph[:80]!r}")
    print(f"# B : {rej} rejetés sur {len(ARTEFACTS)}")
    print("# C. Dépôt, à la ligne citée")
    okd = 0
    for qui, f, pre, n, ex in DEPOT:
        r = ex in ligne(f, pre, n)
        okd += r
        print(f"{'TROUVÉ' if r else 'ABSENT'} | {f} ({pre}…) l. {n} | {qui} | {ex[:80]!r}")
    print(f"# C : {okd} trouvés sur {len(DEPOT)}")
    rejd = 0
    for quoi, f, pre, n, ex in ART_DEPOT:
        r = ex in ligne(f, pre, n)
        rejd += not r
        print(f"{'ACCEPTÉ (faute)' if r else 'rejeté'} | {quoi} | {f} l. {n} | {ex[:80]!r}")
    print(f"# C (R5) : {rejd} rejetés sur {len(ART_DEPOT)}")
    sys.exit(0 if (ko == 0 and rej == len(ARTEFACTS) and okd == len(DEPOT) and rejd == len(ART_DEPOT)) else 1)

if __name__ == "__main__":
    main()
