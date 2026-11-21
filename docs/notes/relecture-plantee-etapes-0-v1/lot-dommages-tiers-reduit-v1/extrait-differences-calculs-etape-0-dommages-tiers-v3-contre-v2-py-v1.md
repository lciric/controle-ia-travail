# Extrait des différences : calculs-etape-0-dommages-tiers-v3.py contre calculs-etape-0-dommages-tiers-v2.py

- Fait le 2026-11-21T22:11:54Z par `extraire_differences_v1.py` (difflib, trois lignes de contexte).
- Avant : `docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v2.py`, sha256 681cf7f71a4d1fdc6854064197ea8289540c4ec9d0990d4799902b6880e5ce57, 1076 lignes.
- Après : `docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v3.py`, sha256 44aedc5fa2c9700c0824d604f83f0fc9f2ebcb6b14aa4da461b4aa2ba91bb4c7, 1277 lignes.
- 4 bloc(s) différent(s) ; 204 ligne(s) de l'après neuve(s) ou changée(s), 3 ligne(s) de l'avant ôtée(s) ou changée(s). Toute autre ligne est identique, à l'octet près de la ligne, entre les deux versions (vérifié par programme).
- Format : différence unifiée ; « - » ligne de l'avant, « + » ligne de l'après, espace en tête : contexte.

--- docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v2.py
+++ docs/notes/plantee-etapes-0-v1/dommages-tiers/calculs-etape-0-dommages-tiers-v3.py
@@ -1,6 +1,20 @@
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
-"""Calculs de l'étape 0, sans dépense, de la campagne de dommages plantés par un tiers (v2).
+"""Calculs de l'étape 0, sans dépense, de la campagne de dommages plantés par un tiers (v3).
+
+v3 (21 novembre 2026, Claude Opus 5.5, sous GO-2026-11-21-84 : « écrit seulement les corrections, mot pour mot
+d'après les remarques déjà reçues ») : la v2 (calculs-etape-0-dommages-tiers-v2.py, 681cf7f71a4d1fdc…, gardée
+intacte) À L'IDENTIQUE, hors cette tête, la ligne de rejeu et la ligne de titre, plus trois sections ajoutées
+avant la ligne de fin :
+  NOTES [v3]  comment se lisent les blocs repris, d'après les errata 1 des pièces du dossier
+  BLOC K      constat V-8 : le taux d'ensemble des seize intervalles d'admission de l'étalonnage
+  BLOC L      constats V-1 et V-7 : la garde du prix réserve le lot final ; cas sain et artefacts par régime
+Les blocs K et L sont exacts : aucun tirage neuf. Remarques portées : verification-corrections-etape-0-dommages-
+tiers-v2-opus-v1.md (8d1ee3a4b31cf7a7…). Toute la sortie de la v2 reste la même, ligne pour ligne, hors la ligne
+de titre ; les sections neuves s'insèrent avant la ligne de fin.
+
+Tête de la v2, inchangée :
+
 
 Remplace la v1 (calculs-etape-0-dommages-tiers-v1.py, gardée intacte) après la contre-lecture
 contre-lecture-etape-0-dommages-tiers-v1-opus-v1.md (0 bloquant, 10 importants, 10 mineurs) et les décisions
@@ -27,7 +41,7 @@
 (étalonnage) et F.14 (lecture graduée) tirent au sort, à graines écrites (numpy.random.SeedSequence, R9).
 Aucune donnée du programme, aucun produit, aucune référence, aucun appel de modèle, aucun réseau.
 
-Rejeu :  python3 -I calculs-etape-0-dommages-tiers-v2.py > calculs-etape-0-dommages-tiers-v2.txt
+Rejeu :  python3 -I calculs-etape-0-dommages-tiers-v3.py > calculs-etape-0-dommages-tiers-v3.txt
 Les attentes sont écrites dans les libellés AVANT la valeur ; les assertions arrêtent le programme.
 """
 import math
@@ -177,7 +191,7 @@
     print("=" * 100)
 
 
-print("Calculs de l'étape 0 de la campagne de dommages plantés par un tiers (v2)")
+print("Calculs de l'étape 0 de la campagne de dommages plantés par un tiers (v3)")
 print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; racine des graines {RACINE}")
 
 # ============================================================================ BLOC A
@@ -1072,5 +1086,192 @@
           f"                              {esperance_min([0.95] * S, TE):.3f}, {esperance_min([0.95] * S, T25):.3f}")
 print("    (30 et 32 : chaque case comptée une fois par planteur, si les deux planteurs ne sont pas réunis.)")
 
+
+# ============================================================================ NOTES [v3]
+titre("NOTES [v3] — Comment se lisent les blocs repris de la v2 sans changement (errata 1 des pièces, après la vérification v2 et la lecture de la mère de GO-2026-11-21-69)")
+print("    1. Bloc C : sa dernière phrase (« la dépense de l'acte est projetée ») est remplacée par la règle du bloc L")
+print("       (constat V-1) ; ses seuils et ses comptes de lectures sont inchangés.")
+print("    2. Sous la décision D-6 (a) — lecture de la mère sous GO-2026-11-21-69, à confirmer par le directeur avant toute")
+print("       revendication —, aucun nombre d'épisodes avant la prise ne s'écrit sur ce banc. Ceux des blocs A et B disent")
+print("       le prix du partage du budget accordé (D-12, a) ; ceux du bloc F ne sont plus des attendus du programme de")
+print("       dépouillement. Au bloc E.2, l'issue « épisodes écrits » se lit « épreuve tenue, aucune fausse alerte observée")
+print("       sur les produits propres », et l'issue « excès observé », « épreuve tenue, une fausse alerte au moins » :")
+print("       leurs probabilités et leurs intervalles d'admission sont inchangés.")
+print("    3. « Écrit sous réserve de D-3 » (blocs A et F) se lit « D-3 (a), lecture de la mère sous GO-2026-11-21-69, à")
+print("       confirmer par le directeur avant toute revendication » ; sur ce banc, l'optimum du mélange n'est rendu dans aucun")
+print("       état (régime d'excès) ; ce qui en reste ouvert est le nœud N-15 du préenregistrement.")
+
+# ============================================================================ BLOC K
+titre("BLOC K [v3, constat V-8] — Le taux d'ensemble des intervalles d'admission de l'étalonnage (étalonnage v2, § 4)")
+print("    Un intervalle d'admission à 99,9 % va de la quantile à 0,05 % à celle à 99,95 % d'une loi binomiale de")
+print("    R = 4 000 campagnes ; un programme juste le manque avec la probabilité exacte P(X < bas) + P(X > haut), sous")
+print("    0,001. Seize intervalles sont non vides : huit de couverture (G.1 et G.4 : vrai q = 0,03 ; 0,156 ; 0,260 ;")
+print("    0,639, dans chaque régime ; à q = 0,912 et à q = 1, l'intervalle est [0, 0], qu'un programme juste ne manque")
+print("    jamais) et huit d'issues (E.2 : quatre par oracle simulé, le bon et l'aveugle à la strate 1 ; « dit lisible »,")
+print("    en G.3, est le complément de « illisible » et ne compte pas à part).")
+print("    Attendu (vérification v2, V-8) : un programme juste en manque un au moins « environ 1,6 fois sur 100 » ; par la")
+print("    borne de la réunion, au plus la somme des seize probabilités exactes de manque, donc sous 16 x 0,001 = 0,016.")
+
+
+def terme_log(k, n, p):
+    """P(X = k), X ~ Bin(n, p), 0 < p < 1, calculé en logarithmes (n = 4 000 dépasse les flottants en direct)."""
+    return math.exp(math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
+                    + k * math.log(p) + (n - k) * math.log(1.0 - p))
+
+
+def manque(lo, hi, n, p):
+    """P(X < lo) + P(X > hi), X ~ Bin(n, p), 0 < p < 1, par somme exacte des termes."""
+    return sum(terme_log(k, n, p) for k in range(0, lo)) + sum(terme_log(k, n, p) for k in range(hi + 1, n + 1))
+
+
+LIGNES_K = []
+for nom_regime, table_k in (("deux regards (G.1, 1,25 %)", TE), ("un regard (G.4, 2,5 %)", T25)):
+    for q in Q_BANC:
+        xstar = next((x for x in range(31) if table_k[x] > q), None)
+        pi = 0.0 if xstar is None else sf(xstar, 30, q)
+        if pi > 0.0:
+            LIGNES_K.append((f"couverture, {nom_regime}, vrai q = {q:.3f}", pi,
+                             quantile_binomial(R, pi, 0.0005), quantile_binomial(R, pi, 0.9995)))
+for nom in ("2 bon : q = 0,90 partout, 2 % de fausses alertes",
+            "5b aveugle à la strate 1 (dose partielle), 3 % de fausses alertes"):
+    for cle in ("illisible", "épreuve échouée", "épisodes écrits", "excès observé"):
+        p_k = ETATS[nom][cle]
+        LIGNES_K.append((f"issue, oracle {nom.split(' ')[0]}, {cle}", p_k,
+                         quantile_binomial(R_ADM, p_k, 0.0005), quantile_binomial(R_ADM, p_k, 0.9995)))
+assert len(LIGNES_K) == 16
+assert [(lo, hi) for _, _, lo, hi in LIGNES_K] == [
+    (27, 72), (5, 31), (26, 71), (8, 38), (27, 72), (29, 75), (26, 71), (44, 98),
+    (58, 119), (9, 41), (2065, 2272), (1618, 1824), (192, 291), (9, 40), (1493, 1697), (2039, 2246)], \
+    "les intervalles ne sont pas ceux que la v2 imprime (G.1, G.4, E.2)"
+print("        intervalle                                                      probabilité   [bas, haut]      P(manque) exacte")
+SOMME_K = 0.0
+for nom, p_k, lo, hi in LIGNES_K:
+    m_k = manque(lo, hi, R, p_k)
+    SOMME_K += m_k
+    iv = f"[{lo}, {hi}]"
+    print(f"        {nom:<62s}  {p_k:.5f}      {iv:<12s}   {m_k:.6f}")
+    assert 0.0 < m_k < 0.001
+print(f"    Somme des seize probabilités de manque (borne de la réunion) : {SOMME_K:.6f}, soit au plus "
+      f"{100 * SOMME_K:.2f} fois sur 100 (attendu : sous 0,016).")
+assert SOMME_K < 0.016
+QUEUE_K = sum(terme_log(k, R, A_EPISODES) for k in range(hi25 + 1, R + 1))
+print("    Ajout déclaré, au-delà de la lettre de V-8 : les dix plafonds de la table 3.2 de l'étalonnage (critère 3 : cinq")
+print(f"    lignes, deux régimes ; au plus {hi25} campagnes fautives sur {R}). La probabilité de faute d'un programme juste")
+print("    est d'au plus 0,025 (preuve par réunion) ; chaque plafond est donc manqué avec une probabilité d'au plus")
+print(f"    P(Bin({R} ; 0,025) > {hi25}) = {QUEUE_K:.6f}, et les dix ensemble avec une probabilité d'au plus {10 * QUEUE_K:.6f}.")
+print(f"    Critères chiffrés 2 à 4 de l'étalonnage ensemble : au plus {SOMME_K + 10 * QUEUE_K:.6f}.")
+assert hi25 == 134 and 0.0 < QUEUE_K < 0.0005
+
+# ============================================================================ BLOC L
+titre("BLOC L [v3, constats V-1 et V-7] — La garde du prix réserve le lot final ; son cas sain et ses artefacts, par régime")
+print("    Règle (V-1) : avant chaque acte payant, la dépense faite, plus celle de l'acte, plus celle de tout acte")
+print("    obligatoire qui le suit (le lot final), ne dépasse pas 300 USD ; les actes facultatifs s'abandonnent dans")
+print("    l'ordre écrit au bloc C : le complément d'abord, la correction de l'oracle (avec sa relecture de contrôle)")
+print("    ensuite. Artefact : la règle fautive, qui ne projette que l'acte (« la dépense projetée de l'acte, ajoutée à")
+print("    la dépense faite, ne dépasse pas 300 USD »).")
+print("    Actes, dans l'ordre : lot d'étalonnage (obligatoire) ; correction de l'oracle et relecture de contrôle")
+print("    (facultative) ; lot final (obligatoire) ; complément (facultatif, régime à deux regards seulement). Pour")
+print("    éprouver la garde, la correction est voulue et le complément désigné. Le prix des journaux projette le lot")
+print("    d'étalonnage ; le prix mesuré sur ce lot projette la suite (ici, le même prix, sauf mention).")
+print("    Attendus (bloc C) : un regard, 45 tâches lues : seuils 0,3704 (de base) et 0,2778 (avec la correction) ;")
+print("    deux regards, 75 tâches lues : de plus 0,2564 (complément sans correction) et 0,2083 (les deux).")
+ACTES_L = (("étalonnage", True), ("correction", False), ("final", True), ("complément", False))
+
+
+def lectures_actes(T):
+    tf, te, reserve, regards = plan(T)
+    return {"étalonnage": te * OBJETS_PAR_TACHE * LECTEURS, "correction": te * OBJETS_PAR_TACHE * LECTEURS,
+            "final": tf * OBJETS_PAR_TACHE * LECTEURS,
+            "complément": tf * OBJETS_COMPLEMENT * LECTEURS if regards == 2 else 0}
+
+
+def course_prix(prix, T, regle, correction=True, prix_journaux=None):
+    """Rend (actes faits, états, dépense en USD). regle : « juste » (V-1) ou « fautive » (ne projette que l'acte)."""
+    lect = lectures_actes(T)
+    fait, faits, etats = 0.0, [], []
+    for i, (acte, obligatoire) in enumerate(ACTES_L):
+        if lect[acte] == 0 or (acte == "correction" and not correction):
+            continue
+        p_proj = prix_journaux if (acte == "étalonnage" and prix_journaux is not None) else prix
+        proj = fait + lect[acte] * p_proj
+        if regle == "juste":
+            proj += sum(lect[a] * p_proj for a, ob in ACTES_L[i + 1:] if ob)
+        if proj > PLAFOND_USD + 1e-9:
+            if obligatoire:
+                etats.append("PRIX avant le lot " + ("d'étalonnage" if acte == "étalonnage" else "final")
+                             + f" ({proj:.2f} USD projetés)")
+                break
+            etats.append(("SANS_CORRECTION_FAUTE_DE_BUDGET" if acte == "correction" else "SANS_COMPLEMENT_FAUTE_DE_BUDGET")
+                         + f" ({proj:.2f} USD projetés)")
+            continue
+        fait += lect[acte] * prix
+        faits.append(acte)
+    return faits, etats, fait
+
+
+for nom_regime, T in (("un regard", 45), ("deux regards", 75)):
+    lect = lectures_actes(T)
+    s_base = PLAFOND_USD / (lect["étalonnage"] + lect["final"])
+    s_corr = PLAFOND_USD / (lect["étalonnage"] + lect["correction"] + lect["final"])
+    assert round(s_base, 4) == 0.3704 and round(s_corr, 4) == 0.2778
+    ligne = (f"    Régime à {nom_regime}, {T} tâches : lectures — étalonnage {lect['étalonnage']}, relecture de contrôle "
+             f"{lect['correction']}, lot final {lect['final']}, complément {lect['complément']} ; seuils {s_base:.4f} et {s_corr:.4f}")
+    if lect["complément"]:
+        s_comp = PLAFOND_USD / (lect["étalonnage"] + lect["final"] + lect["complément"])
+        s_deux = PLAFOND_USD / sum(lect.values())
+        assert round(s_comp, 4) == 0.2564 and round(s_deux, 4) == 0.2083
+        ligne += f", {s_comp:.4f} et {s_deux:.4f}"
+    print(ligne + ".")
+    for regle in ("juste", "fautive"):
+        for prix in (0.20, 0.23, 0.27, 0.30, 0.40):
+            faits, etats, fait = course_prix(prix, T, regle)
+            print(f"        règle {regle:<7s} {prix:.2f} USD : actes faits {', '.join(faits) if faits else 'aucun'} ; "
+                  f"{' ; '.join(etats) if etats else 'tout tient'} ; dépense {fait:.2f} USD")
+            assert fait <= PLAFOND_USD + 1e-9
+    faits, etats, fait = course_prix(0.40, T, "juste", prix_journaux=0.20)
+    print(f"        règle juste   0,40 USD mesuré au seul lot d'étalonnage (journaux à 0,20) : actes faits {', '.join(faits)} ; "
+          f"{' ; '.join(etats)} ; dépense {fait:.2f} USD")
+    assert faits == ["étalonnage"] and etats[-1].startswith("PRIX avant le lot final")
+    if lect["complément"]:
+        faits, etats, fait = course_prix(0.23, T, "juste", correction=False)
+        print(f"        règle juste   0,23 USD sans correction : actes faits {', '.join(faits)} ; "
+              f"{' ; '.join(etats) if etats else 'tout tient'} ; dépense {fait:.2f} USD")
+        assert faits == ["étalonnage", "final", "complément"] and not etats
+
+# Attendus par régime, la règle juste (gardes de la course, erratum 1, garde 8)
+ATT_UN = {p: course_prix(p, 45, "juste") for p in (0.20, 0.23, 0.27, 0.30, 0.40)}
+for p in (0.20, 0.23, 0.27):
+    assert ATT_UN[p][0] == ["étalonnage", "correction", "final"] and not ATT_UN[p][1]
+assert ATT_UN[0.30][0] == ["étalonnage", "final"] and ATT_UN[0.30][1][0].startswith("SANS_CORRECTION_FAUTE_DE_BUDGET")
+assert ATT_UN[0.40][0] == [] and ATT_UN[0.40][1][0].startswith("PRIX avant le lot d'étalonnage")
+ATT_DEUX = {p: course_prix(p, 75, "juste") for p in (0.20, 0.23, 0.27, 0.30, 0.40)}
+assert ATT_DEUX[0.20][0] == ["étalonnage", "correction", "final", "complément"] and not ATT_DEUX[0.20][1]
+for p in (0.23, 0.27):
+    assert ATT_DEUX[p][0] == ["étalonnage", "correction", "final"] and ATT_DEUX[p][1][0].startswith("SANS_COMPLEMENT_FAUTE_DE_BUDGET")
+assert ATT_DEUX[0.30][0] == ["étalonnage", "final"] and [e.split(" ")[0] for e in ATT_DEUX[0.30][1]] == [
+    "SANS_CORRECTION_FAUTE_DE_BUDGET", "SANS_COMPLEMENT_FAUTE_DE_BUDGET"]
+assert ATT_DEUX[0.40][0] == [] and ATT_DEUX[0.40][1][0].startswith("PRIX avant le lot d'étalonnage")
+# L'artefact : à 0,30 USD, la règle fautive fait la correction puis perd le lot final, dans les deux régimes
+for T in (45, 75):
+    faits, etats, fait = course_prix(0.30, T, "fautive")
+    assert faits == ["étalonnage", "correction"] and etats[0].startswith("PRIX avant le lot final") and abs(fait - 162.0) < 1e-9
+print("    À 0,30 USD, dans les deux régimes : la règle fautive permet la correction (81,00 USD faits, 162,00 projetés), puis")
+print("    le lot final ne tient plus (324,00 USD projetés) : la course perd son lot final et n'écrit rien. La règle juste")
+print("    refuse la correction (324,00 USD projetés avec le lot final), lit le lot final et dépense 243,00 USD ; à deux")
+print("    regards, elle n'ouvre pas le complément (351,00 USD projetés).")
+assert abs(course_prix(0.30, 45, "juste")[2] - 243.0) < 1e-9 and abs(course_prix(0.30, 75, "juste")[2] - 243.0) < 1e-9
+# Où la règle fautive perd un lot final que la règle juste lit : (300/1080 ; 300/810], soit de 0,2778 à 0,3704 USD
+ecarts = []
+for k in range(2000, 4501):
+    p = k / 10000 + 0.00005
+    juste_lit = "final" in course_prix(p, 45, "juste")[0]
+    fautive_lit = "final" in course_prix(p, 45, "fautive")[0]
+    if juste_lit and not fautive_lit:
+        ecarts.append(p)
+    assert juste_lit or not fautive_lit
+assert abs(min(ecarts) - 0.27785) < 1e-9 and abs(max(ecarts) - 0.37035) < 1e-9
+print(f"    Sur une grille de pas 0,0001 entre 0,20 et 0,45 USD, la règle fautive perd un lot final que la règle juste lit")
+print(f"    pour tout prix de {PLAFOND_USD / 1080:.4f} (exclu) à {PLAFOND_USD / 810:.4f} USD (inclus) : de {min(ecarts):.5f} à {max(ecarts):.5f} sur la grille.")
+
 print()
 print("FIN — aucune mesure ; aucun produit, aucune référence, aucun verdict d'oracle n'a été lu.")
