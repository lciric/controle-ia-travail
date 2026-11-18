"""Écrit la note d'englobement de O4, v2, depuis la v1 (R12 : fichier neuf ; la v1 reste en place, sur `main`).

Porte le mot direct de Lazar R-2822 (N-SSRN-1 et N-SSRN-2 accordés) : citations de LIU (SSRN 6569258) mises sur la version officielle
de septembre 2026 ; appui sur la phrase d'avril p. 36 retiré ; alpha contre un modèle de facteurs fixé dit en avril comme en septembre ;
Koijen et Levy (SSRN 6474601) cités pour P et pour la partie « en temps réel » de (iv), et dans la phrase publiable. Retire aussi les
noms de modèles de la v1 (R-2690), repérés par motif sans être recopiés ici. Remplacements comptés ; refus si un texte visé n'est pas présent le nombre de fois dit.
Usage : python3 -I faire_englobement_v2.py NOTE_V1 SORTIE HEURE_UTC
"""
import hashlib
import os
import re
import sys

V1_SHA = "f521e164e79cb75e"  # préfixe ; l'empreinte entière est vérifiée par le compagnon sur main
LECT = "docs/notes/lecture-o4-suite-v1/lecture-pdf-ssrn-o4-v2.md"
LECT_SHA = "93518e46d59825d9"


def main():
    src, sortie, heure = sys.argv[1:4]
    if os.path.exists(sortie):
        sys.exit("REFUS : sortie existante (R12)")
    b = open(src, "rb").read()
    if not hashlib.sha256(b).hexdigest().startswith(V1_SHA):
        sys.exit("REFUS : empreinte de la v1")
    t = b.decode("utf-8")
    n = [0]

    def r(o, nv, k=1):
        nonlocal t
        c = t.count(o)
        if c != k:
            sys.exit(f"REFUS : « {o[:90]} » présent {c} fois, {k} attendu(s)")
        t = t.replace(o, nv)
        n[0] += 1

    r("tests d'englobement — v1\n", "tests d'englobement — v2\n")
    m = re.search(r"- \*\*Lecteur\*\* : sous-agent neuf \([^)]*\), qui n'a écrit", t)
    if not m:
        sys.exit("REFUS : ligne du lecteur de la v1 absente")
    r(m.group(0),
      f"""- **Version 2** (R12 ; la v1, `{V1_SHA}…`, reste en place sur `main`) : écrite par le modèle A (session du compte organisme) à
  {heure} (`date -u`), sur le mot direct de Lazar **R-2822** (« N-SSRN-1 : mettre à jour les citations de Liu et coauteurs sur la
  version de septembre de l'article ; N-SSRN-2 : citer Koijen et Levy dans toute phrase publique sur des prédictions faites avant les
  données. go »), d'après la lecture sur PDF de SSRN 6569258 (version officielle) et de SSRN 6474601 (`{LECT}`, `{LECT_SHA}…`,
  contre-lue « tient avec réserves », réserves portées ; citations rejouées 91 sur 91). Changent seulement : sections 0 (points 1, 3, 5),
  2 (lignes LIU et KL), 3.1, 4, 5 (points 1 et 4). Le verdict ne change pas. Les noms de modèles de la v1 sont retirés (R-2690).
- **Lecteur de la v1** : sous-agent neuf, qui n'a écrit""")
    r("Les 53 citations ci-dessous ont été recopiées puis **vérifiées par programme**",
      "[v2 : les citations de LIU de la section 3.1 sont celles de la version officielle de septembre, rejouées par `docs/notes/lecture-o4-suite-v1/rejouer_citations_ssrn_o4_v1.py` sur `citations-ssrn-o4-v4.json` ; les autres citations sont celles de la v1.] Les 53 citations de la v1 ont été recopiées puis **vérifiées par programme**")
    # section 0, point 1
    r("après la boucle de découverte (Liu, Liu, Liu, Mei, SSRN 6569258, avril 2026, p. 1, 4, 26, 28) ;",
      "après la boucle de découverte (Liu, Liu, Liu, Mei, SSRN 6569258, version officielle de septembre 2026, p. 1, 5, 6, 30, 32) ;")
    r("qui s'accroît à chaque admission (Pan, Ding, Giesecke, « SEADS », arXiv 2609.00731, 1er septembre 2026, p. 6, 7, 16, 25).",
      """qui s'accroît à chaque admission (Pan, Ding, Giesecke, « SEADS », arXiv 2609.00731, 1er septembre 2026, p. 6, 7, 16, 25) ;
   - **pour des systèmes à modèle de langue optimisés, dont les prédictions sont faites en temps réel, avant que le rendement n'existe**,
     jugées par leur gain d'explication sur des déterminants connus (Koijen et Levy, SSRN 6474601, date imprimée 30 juin 2026, p. 1, 3, 8,
     11, 16 ; la date de dépôt sur SSRN n'est pas lue).""")
    # section 0, point 3
    r("""3. **SSRN 6569258 n'occupe pas O4 en entier** : son nul des lois connues est appliqué **après** la boucle, sur l'échantillon même de la recherche, avec des statistiques de Student à taille fixée ; dans la boucle, le crible rendu au modèle est « coefficient de Fama et MacBeth significatif dans le sens prédit », c'est-à-dire un nul « aucun effet » (p. 14, 22, 36). Il occupe le **principe** pour des hypothèses de modèle de langue (p. 1, 4, 28).""",
      """3. **SSRN 6569258 n'occupe pas O4 en entier** (version officielle de septembre 2026) : son nul des lois connues est appliqué
   **après** la boucle et hors d'elle, sur l'échantillon même de la recherche (données de 1963 à 2024), par régression contre les dix
   prédicteurs publiés les plus proches et trois modèles de facteurs, avec des statistiques de Student à taille fixée (p. 11, 22, 30) ;
   dans la boucle, le crible est « coefficient de Fama et MacBeth significatif dans le sens prédit », c'est-à-dire un nul « aucun effet »
   (p. 19). Le retour fait au proposeur contient un **alpha contre un modèle de facteurs fixé, en avril comme en septembre** (quatre
   facteurs de Carhart dans la copie d'avril, p. 14-15 ; cinq facteurs en septembre, p. 19, 57) : ce n'est ni une règle de promotion ni
   un nul formé de l'archive. (v2 : l'appui de la v1 sur la phrase d'avril p. 36, « lacks direct access to factor model results during
   the discovery loop », est retiré : elle est absente de la version de septembre, et la copie d'avril elle-même rendait déjà un alpha au
   proposeur.) Le test prospectif gelé y est dit **non fait** (p. 6, 34). Il occupe le **principe** pour des hypothèses de modèle de
   langue (p. 1, 5, 6, 32).""")
    # section 0, point 5
    r("le scellement par empreinte chez CONFIRM et « Hard to Fool » (déjà cités par N-067, section 3).",
      "le scellement par empreinte chez CONFIRM et « Hard to Fool » (déjà cités par N-067, section 3) ; la partie « en temps réel » de (iv) (prédictions faites avant que le rendement n'existe, statistique calculée par l'évaluateur), sans scellement ni horodatage trouvé, chez Koijen et Levy (SSRN 6474601, p. 1, 3, 11).")
    r("est, dans sa lettre, occupée dans son principe par SEADS et par Liu et al.",
      "est, dans sa lettre, occupée dans son principe par SEADS, par Liu et al. et par Koijen et Levy.")
    # section 2
    r("""| LIU | Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, avril 2026 (copie déposée par l'hôte d'une conférence, voir section 5) | `ssrn-6569258/` | `2d4e1d61d248699a…` | en entier (71 p.) |""",
      """| LIU | Liu, Liu, Liu, Mei, « Can AI Do Financial Research? LLM-Guided Hypothesis Discovery in Asset Pricing », SSRN 6569258, **version officielle de septembre 2026** (84 p., déposée par Lazar : `docs/sources/pdf/ssrn-lazar-2026-11-14/`), lue en v2 ; la copie d'avril (hôte d'une conférence, `ssrn-6569258/`, `2d4e1d61…`, 71 p.) reste la pièce de la v1 | `../ssrn-lazar-2026-11-14/` | `15cdb423744d7885…` | par pages (lecture SSRN v2, section 5) |""")
    r("| SEADS | Pan, Ding, Giesecke,",
      """| KL | Koijen, Levy, « Assessing the Benefits of Optimized Agentic AI Systems for Asset Pricing », SSRN 6474601, date imprimée 30 juin 2026 (39 p., déposée par Lazar), lue en v2 | `../ssrn-lazar-2026-11-14/` | `98757745f4364034…` | p. 1-30, 38-39 ; tableaux par notes (lecture SSRN v2, section 5) | **occupe en partie** : principe pour des systèmes à modèle de langue optimisés ; partie « en temps réel » de (iv) ; ni archive comme nul, ni e-processus, ni scellement | 1, 3, 8, 11, 16 |
| SEADS | Pan, Ding, Giesecke,""")
    # section 3.1
    i, j = t.index("### 3.1 LIU — SSRN 6569258 (pièce nommée par R-2571)"), t.index("### 3.2 SEADS")
    r(t[i:j], """### 3.1 LIU — SSRN 6569258 (pièce nommée par R-2571), version officielle de septembre 2026 (v2)

Citations de la version officielle (`15cdb423744d7885…`), rejouées par programme (identifiants de `citations-ssrn-o4-v4.json`) ; la
correspondance avec chaque citation d'avril de la v1 (page, état) est à la section 1 de la lecture SSRN v2.

- Objet : des agents à modèle de langue proposent des formules comptables dans un langage symbolique, une chaîne d'évaluation fixe les
  teste : [p. 1, L06] « We place specialized large language model agents in an environment with a symbolic language of interpretable accounting formulas and a fixed empirical evaluation pipeline. »
- Le principe de O4, pour des hypothèses de modèle de langue :
  - [p. 1, L01] « incremental information relative to 209 published anomalies »
  - [p. 6, L02] « where seemingly new evidence is subsumed by what is already known »
  - [p. 30, L03] « Finally, the record must retain its declared direction and a conditional statistic above 1.96 after controlling for up to ten selected nearby predictors from the Chen–Zimmermann library (Chen and Zimmermann, 2022). »
  - [p. 32, L04] « Many records that survive multiplicity and factor adjustment therefore contain information already represented by their selected published comparators. »
  - [p. 22, L16] « For each candidate reaching the published-predictor stage, the spanning procedure selects up to ten predictors with the largest absolute average cross-sectional rank correlations »
  - course entre les propres découvertes du système, après la recherche : [p. 22, L15] « This horse race identifies incremental conditional return association relative to other constructions generated for the same economic task »
  - revendication de priorité des auteurs : [p. 5, L05] « To our knowledge, this is the first study to combine autonomous LLM-guided signal discovery with modern multiple-testing corrections, alternative factor models, subsample and decay analyses, and spanning tests against published anomalies »
- Ce qui n'y est pas (pourquoi « en partie ») :
  - les tests contre le connu sont hors de la boucle : [p. 11, L07] « Once a run ends, post-search procedures operate outside the discovery loop and are indexed to the population for which each procedure is defined. »
  - dans la boucle, le nul est « aucun effet » : [p. 19, L08] « We classify an empirically evaluated hypothesis as a first-pass success when its Fama– MacBeth statistic is finite, exceeds 1.96 in absolute value, and the estimated slope has the direction declared before evaluation »
  - le retour fait au proposeur contient un alpha contre un modèle de facteurs fixé : [p. 57, L09] « Each archive entry reports the expression, declared direction, Fama–MacBeth statistic, long– short alpha and alpha statistic, Sharpe ratio, coverage, and any execution error. » ; [p. 19, L10] « The discovery-stage alpha uses the Fama–French five-factor model » ; il en allait de même en avril : [avril p. 15, A13] « successful signals (with Fama–MacBeth t-statistic, alpha t-statistic, Sharpe ratio, and quintile returns) » ; [avril p. 14, A14] « We regress the long–short portfolio’s excess returns on the Carhart (1997) four factors »
  - l'archive de la course est un contexte, non un nul : [p. 15, L11] « Within a given run, the archive is the state variable of the adaptive search. » ; la nouveauté y est jugée par le critique, modèle de langue : [p. 38, L13] « The critic’s comparison set is limited to published signals invoked from its finance knowledge and proposals visible in the contemporaneous task archive; it is not an exhaustive literature review. »
  - pas d'e-valeur (aucune occurrence sur les 84 pages ; lecture SSRN v2) : inférence à taille fixée, [p. 29, L18] « the run-level Benjamini–Yekutieli (BY) false-discovery-rate procedure at q = 0.05 »
  - pas de validation hors échantillon, données antérieures à l'engagement : [p. 6, S10] « First, the search is adaptive and uses the same historical panel throughout, so our post-discovery tests provide search-adjusted inference rather than true out-of-sample validation. » ; [p. 17, L22] « The sample ends in December 2024. » ; [p. 6, L23] « A true out-of-sample test would freeze the discovered hypotheses and all evaluation choices before new returns are realized, then evaluate t… » (citation complète au fichier)
  - séparation déjà là, à citer pour O1 : [p. 42, L25] « The LLM does not read firm-level observations, assign historical scores, access the raw CRSP– Compustat panel, or alter the portfolio-construction procedure. » ; sens prédit posé avant le résultat : [p. 40, L21] « Each hypothesis states an economic mechanism, an executable accounting expression, and a return direction before its own result is observed. »
- Retiré de la v1 : l'appui sur la phrase d'avril p. 36 (« it lacks direct access to factor model results during the discovery loop »),
  absente de la version de septembre et déjà contredite par la copie d'avril (p. 15).

### 3.1 bis KL — Koijen, Levy, SSRN 6474601 (v2)

- Principe, pour des systèmes à modèle de langue : [p. 8, K05] « The primary performance statistic is the incremental explanatory power, or ∆R2 , generated by the AI system’s predictions over a baseline model, e.g., one that includes only the quantitative controls » ; [p. 1, K02] « the best-optimized systems more than double the explained variation in returns relative to existing literature. »
- Partie « en temps réel » de (iv) : [p. 1, K01] « We introduce a real-time, out-of-sample benchmark to sidestep both problems that measures how well AI systems explain contemporaneous stock » (citation complète au fichier) ; [p. 3, K03] « the AI model uses to make its forecasts (as well as the model parameters), are determined prior to the earnings announcement. » ; [p. 11, KO1] « This enables us to collect data, generate predictions, and evaluate results strictly out of sample. »
- Ce qui n'y est pas : l'archive connue se réduit aux contrôles quantitatifs (et, pour les systèmes optimisés, au système non optimisé : [p. 19, K32] « With the ACE rulebook, the R2 rises to 17.1% [0.12, 0.24], a gain of 3.0 percentage points. ») ; un livre de règles qui grandit existe ([p. 19, K31] « The result is a modular, interpretable set of rules that grows and refines over time. »), versé dans le prédicteur, non dans le nul ; inférence par intervalles de rééchantillonnage à échantillon fixé, aucune e-valeur ; aucun scellement ni horodatage trouvé ; pour les systèmes optimisés, le texte ne dit pas que les prédictions de la seconde moitié du trimestre ont été émises avant les événements (p. 16).

""")
    # section 4
    r("déjà appliquée à des hypothèses proposées par des modèles de langue (Liu, Liu, Liu et Mei, 2026, SSRN 6569258 ; Pan, Ding et Giesecke, 2026, arXiv 2609.00731), et",
      "déjà appliquée à des hypothèses proposées par des modèles de langue (Liu, Liu, Liu et Mei, 2026, SSRN 6569258 ; Pan, Ding et Giesecke, 2026, arXiv 2609.00731) et à des prédictions de systèmes à modèle de langue faites avant que les données existent (Koijen et Levy, 2026, SSRN 6474601), et")
    r("already applied to hypotheses proposed by language models (Liu, Liu, Liu and Mei, 2026, SSRN 6569258; Pan, Ding and Giesecke, 2026, arXiv 2609.00731), and",
      "already applied to hypotheses proposed by language models (Liu, Liu, Liu and Mei, 2026, SSRN 6569258; Pan, Ding and Giesecke, 2026, arXiv 2609.00731) and to predictions of language-model systems made before the data exist (Koijen and Levy, 2026, SSRN 6474601), and")
    r("(c) la phrase reste soumise au mot de Lazar (modification de revendication).",
      "(c) la phrase reste soumise au mot de Lazar (modification de revendication) ; (d) v2 : la citation de Koijen et Levy y est portée sur le mot de Lazar R-2822 (N-SSRN-2), et Liu et al. y renvoie à la version officielle de septembre (N-SSRN-1).")
    # section 5
    r("1. **PDF officiel de SSRN 6569258** : refusé (section 6).",
      "1. **PDF officiel de SSRN 6569258** : v2 : **lu** (version de septembre 2026, déposée par Lazar ; lecture SSRN v2). En v1 : refusé (section 6).")
    r("4. Koijen et Levy, SSRN 6474601, 2026 (cité par SEADS, p. 13) : agentique en évaluation d'actifs ; SSRN refusera sans doute.",
      "4. Koijen et Levy, SSRN 6474601, 2026 (cité par SEADS, p. 13) : v2 : **lu** (déposé par Lazar ; lecture SSRN v2) ; occupe en partie (section 2, ligne KL).")
    t = t.rstrip("\n") + "\n"
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(t)
    print(f"{n[0]} remplacements comptés")


if __name__ == "__main__":
    main()
