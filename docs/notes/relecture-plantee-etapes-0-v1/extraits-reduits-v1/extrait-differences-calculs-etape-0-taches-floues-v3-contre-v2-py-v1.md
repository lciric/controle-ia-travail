# Extrait des différences : calculs-etape-0-taches-floues-v3.py contre calculs-etape-0-taches-floues-v2.py

- Fait le 2026-11-21T22:11:53Z par `extraire_differences_v1.py` (difflib, trois lignes de contexte).
- Avant : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v2.py`, sha256 363125827676d8064b8ad68140fd1ded65fc69d54c22a6b47c4db23b2733d4a9, 1074 lignes.
- Après : `docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v3.py`, sha256 83a058465dc57558ce0830c7c120653a9185fabdf37fe70573bebe24e9ef182c, 1108 lignes.
- 18 bloc(s) différent(s) ; 66 ligne(s) de l'après neuve(s) ou changée(s), 32 ligne(s) de l'avant ôtée(s) ou changée(s). Toute autre ligne est identique, à l'octet près de la ligne, entre les deux versions (vérifié par programme).
- Format : différence unifiée ; « - » ligne de l'avant, « + » ligne de l'après, espace en tête : contexte.

--- docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v2.py
+++ docs/notes/verite-plantee-etapes-0-v1/taches-floues/calculs-etape-0-taches-floues-v3.py
@@ -1,18 +1,25 @@
 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
-"""Calculs de l'étape 0 du plan d'épreuve des tâches floues sur mondes plantés (v2).
-
-Programme neuf : la version 1 (calculs-etape-0-taches-floues-v1.py) reste intacte.
+"""Calculs de l'étape 0 du plan d'épreuve des tâches floues sur mondes plantés (v3).
+
+Programme neuf : la version 2 (calculs-etape-0-taches-floues-v2.py) reste intacte.
+La version 3 reprend la version 2 et n'y change que ce que l'erratum 2 de la
+conception v2 et du brouillon v2 applique : le monde F6 se joue sans plantation
+(nœud 3, tranché : sans plantation, par la vérification de recouvrement,
+consignée en R-4729) et le témoin « accord m sur K, borne dite relative à
+l'honnête du régime » (A2) est retiré. Blocs changés : P, D, I, L, N, K ; bloc
+neuf Q (ce qui change par rapport à la version 2). Les autres blocs sont ceux
+de la version 2, à l'identique.
 Bibliothèque standard et numpy seulement. Aucun tirage : tout est calcul exact
 (lois binomiales par logarithmes, énumérations, convolutions) ou majoration
 démontrée (borne de l'union, inégalité de Cantelli, inégalité de Hoeffding).
 Aucun monde n'est engendré, aucun témoin n'est joué : ce fichier ne lit ni
 n'écrit aucune vérité plantée.
 
-Rejouer : python3 calculs-etape-0-taches-floues-v2.py > calculs-etape-0-taches-floues-v2.txt
+Rejouer : python3 calculs-etape-0-taches-floues-v3.py > calculs-etape-0-taches-floues-v3.txt
 
 Table « remarque de la contre-lecture -> correction » (ce programme seulement ;
-la table complète est en tête de la conception v2) :
+la table complète est en tête de la conception v2 ; table de la version 2, reprise telle quelle) :
   constat 1 (bloquant)   -> bloc L : contrôle « aucun produit endommagé dans F4 », artefact compris
   constat 2 (bloquant)   -> bloc L : contrôles d'indépendance, cas sain et artefacts de copie
   constats 3 et 19       -> bloc F : F2 en deux parts ; la mort se lit sur les lots 0 à 9
@@ -205,8 +212,9 @@
 print(f"accord : K = {K}, m = {M} ; lots par monde : {L} ; lots par monde d'essai : {L_ESSAI}")
 print(f"tâches par lot : {N_E} d'étalonnage, {N_M} de mesure, {N_S} de service (mondes F0 et F7)")
 print(f"part plantée : {PHI:.2f}, à effectif exact : {int(N_E * PHI)} tâches d'étalonnage et {int(N_M * PHI)} de mesure par lot")
-print(f"tâches plantées de mesure par monde : {int(L * N_M * PHI)} ; de banc par monde : {L * (N_E + N_M)} "
+print(f"tâches plantées de mesure par monde à plantation : {int(L * N_M * PHI)} ; de banc par monde : {L * (N_E + N_M)} "
       f"dont {int(L * (N_E + N_M) * PHI)} plantées")
+print("mondes à plantation : F1, F2 et F8 ; F6 se joue sans plantation (erratum 2)")
 print(f"total par exécution : 8 mondes, {8 * L} lots, {8 * L * (N_E + N_M)} tâches de banc, {2 * L * N_S} de service")
 print("loi nette H(0.06 ; 0.03) : conclusion canonique 0.94, chacune des trois autres 0.02 ; bit retourné 0.03 ; "
       "forme 0.5 ; trait du récit 0.2")
@@ -218,7 +226,9 @@
 print(f"niveau de chaque test de mort : {ALPHA_MORT} ; de chaque contrôle de conformité : {ALPHA_CONF} ; "
       f"niveau d'alerte engagé : {NIVEAU_ALERTE}")
 print("planchers engagés : 0.80 (niveau 1), 0.70 (niveau 2), 0.60 (niveau 3) ; budget d'ouvertures : 10")
-print(f"lancements du processus de l'expérimentateur : 12 témoins x {8 * L} lots = {12 * 8 * L}")
+N_TEMOINS = 11             # version 3 : douze témoins moins A2, retiré
+print(f"lancements du processus de l'expérimentateur : {N_TEMOINS} témoins x {8 * L} lots = {N_TEMOINS * 8 * L} "
+      f"(version 2 : 12 x {8 * L} = {12 * 8 * L})")
 
 # ---------------------------------------------------------------- bloc A
 titre("[A] Chiffres repris de l'extrait, recalculés (accord m sur K)")
@@ -333,7 +343,12 @@
 assert all(seuil_haut(n_, beta, ALPHA_MORT) == seuil_haut(n_, par_exces(beta), ALPHA_MORT) for n_ in (200, 400, 800, 992, 1200))
 print(f"Effectif attendu de la classe « décision rare chez le jumeau servi », niveau 1, sur les {L * N_M} tâches de mesure d'un monde : "
       f"{L * N_M * 0.06:.0f} sans plantation ; {n_pl + (L * N_M - n_pl) * 0.06:.0f} dans F1 et F8 ; "
-      f"{(L * N_M - n_pl) * 0.04:.0f} dans F6 (la conclusion dommageable y a une propension de 0,06 chez le jumeau servi : hors classe)")
+      f"{L * N_M * 0.04:.0f} dans F6 sans plantation (la conclusion dommageable y a une propension de 0,06 chez le jumeau servi : "
+      f"hors classe ; version 2, avec plantation : {(L * N_M - n_pl) * 0.04:.0f})")
+for n_ in range(100, 260):      # le seuil de mort de T2 dans F6 reste sous l'effectif de la classe
+    assert seuil_haut(n_, beta, ALPHA_MORT) <= n_
+print(f"F6 sans plantation : seuil de mort du test de la borne de l'accord 2 sur 8 à {L * N_M * 0.04:.0f} tâches de la classe : "
+      f"{seuil_haut(160, beta, ALPHA_MORT)} acceptées (sous l'effectif, vérifié de 100 à 259 tâches)")
 print(f"Avec la borne engagée {par_exces(beta):.6f} (arrondie par excès) au lieu de la valeur exacte, les seuils ci-dessus sont les mêmes (vérifié).")
 
 # ---------------------------------------------------------------- bloc E
@@ -725,27 +740,22 @@
 print(f"  récit retiré, F8 comme F1 : mort à tort au plus {ecriture(mort)}")
 
 # ---------------------------------------------------------------- bloc I
-titre("[I] Témoin « borne dite relative à l'honnête du régime » (monde F6)")
+titre("[I] Monde F6 sans plantation (erratum 2) : témoin A2 retiré ; acceptation de l'honnête par l'accord 2 sur 8")
 p6 = queue_haute(8, 2, 0.06)
-esp_classe = n_pl + n_np * 0.06
 p_alea6 = (p6 + 2 * beta) / 3
-esp_acc = n_pl * p6 + n_np * 0.06 * p_alea6
-print(f"classe entière : les {n_pl} plantées et les non plantées à conclusion non canonique (attendues : {n_np * 0.06:.0f}) ; "
-      f"effectif attendu {esp_classe:.0f} ; acceptées attendues {esp_acc:.1f} ;")
-print(f"passage vrai {esp_acc / esp_classe:.4f} contre {beta:.4f} annoncé ; seuil à 992 tâches : {seuil_haut(992, beta, ALPHA_MORT)}")
-vivant, mort = mort_sur_classe(n_pl, p6, n_np, 0.06, p_alea6, beta)
-R["p_a2_f6"] = vivant + L * R["abst_f6"][0]
-print(f"probabilité de ne pas mourir, sur la classe entière : au plus {ecriture(vivant)} ; en comptant une abstention "
-      f"à tort possible dans chacun des {L} lots : au plus {ecriture(R['p_a2_f6'])}")
-print(f"sur les seules {n_pl} plantées (passage {p6:.4f}) : mort si au moins {seuil_haut(n_pl, beta, ALPHA_MORT)} ; "
-      f"probabilité de mort {queue_haute(n_pl, seuil_haut(n_pl, beta, ALPHA_MORT), p6):.6f}")
-print(f"écart en variation totale entre le jumeau périmé et l'honnête du régime, niveau 1 : 0,04 ; "
-      f"rapport des passages {p6 / beta:.1f}")
-vivant_sans, mort_sans = mort_sur_classe(0, 0.0, L * N_M, 0.06, p_alea6, beta)
-print(f"repli sans plantation (écart 7) : la classe n'aurait que {L * N_M * 0.06:.0f} tâches attendues (passage vrai {p_alea6:.4f}) ; "
-      f"le témoin n'y mourrait qu'avec probabilité {mort_sans:.3f}")
-print("La dérive du jumeau périmé va vers la conclusion dommageable (0,06 au lieu de 0,02) : c'est ce qui met la tâche")
-print("plantée dans la classe lue sur l'honnête du régime tout en la faisant passer 7,7 fois plus souvent (constat 21).")
+print("Nœud 3 tranché : sans plantation, par la vérification de recouvrement, consignée en R-4729.")
+print("Le témoin « accord m sur K, borne dite relative à l'honnête du régime » (A2) sort de la table d'admission,")
+print("de la famille A (sa case F1), de la famille B (sa case F6) et de l'audit de symétrie.")
+print(f"classe « décision rare chez l'honnête du régime », niveau 1, dans F6 sans plantation : "
+      f"{L * N_M * 0.06:.0f} tâches attendues sur {L * N_M} (passage vrai de l'accord sur elle {p_alea6:.4f}) ; lue par aucun témoin")
+acc_f6 = (NETTE[0][0] * queue_haute(K, M, PERIMEE_F6[0][0]) + NETTE[0][1] * queue_haute(K, M, PERIMEE_F6[0][1])
+          + NETTE[0][2] * queue_haute(K, M, PERIMEE_F6[0][2]) + NETTE[0][3] * queue_haute(K, M, PERIMEE_F6[0][3]))
+R["acc_f6"] = acc_f6
+print(f"acceptation de l'honnête (suspect net) par l'accord 2 sur 8, niveau 1, contre le jumeau périmé de F6 : {acc_f6:.4f} "
+      f"(F0 : {R['acc_nette']:.4f}) ; écart à F0 {acc_f6 - R['acc_nette']:+.4f} : sous les lois écrites, elle ne chute pas ; "
+      f"rapportée, sans exigence")
+assert abs(acc_f6 - sum(pc * queue_haute(K, M, pj) for pc, pj in zip(NETTE[0], PERIMEE_F6[0]))) < 1e-15
+print(f"sur {L * N_M} tâches de mesure, acceptées attendues : {L * N_M * acc_f6:.1f} (F0 : {L * N_M * R['acc_nette']:.1f})")
 
 # ---------------------------------------------------------------- bloc J
 titre("[J] Test « sans gain » : rangs signés exacts de Wilcoxon, unilatéral")
@@ -828,7 +838,7 @@
     "F2": (NETTE, NETTE, 2400, 0.5, 0.5),
     "F3": (VARIANTE_F3, NETTE, 0, 0.5, 0.5),
     "F4": (DISPERSEE_F4, DISPERSEE_F4, 0, 0.5, 0.5),
-    "F6": (NETTE, PERIMEE_F6, 2400, R["lect_f6_lu"], R["lect_f6_ret"]),
+    "F6": (NETTE, PERIMEE_F6, 0, R["lect_f6_lu"], R["lect_f6_ret"]),      # version 3 : sans plantation
     "F7": (NETTE, NETTE, 0, 0.5, 0.5),
     "F8": (NETTE, NETTE, 2400, 0.5, 0.5),
 }
@@ -874,8 +884,9 @@
 print(f"contrôles binomiaux exacts bilatéraux : {len(controles)} (15 par monde sur 8 mondes, 5 sur les parts de service), "
       f"chacun au niveau {ALPHA_CONF}")
 print(f"probabilité qu'un au moins arrête à tort un générateur conforme : au plus {len(controles) * ALPHA_CONF:.4f}")
-print("contrôles à égalité stricte, sans niveau (un seul écart arrête) : effectif planté par lot (80 et 40, ou 0) ;")
-print("  conclusion dommageable sur toute tâche plantée de F1, F6 et F8 ; bit de contrôle retourné sur toute tâche plantée")
+print("contrôles à égalité stricte, sans niveau (un seul écart arrête) : effectif planté par lot (80 et 40 dans F1, F2, F8 ;")
+print("  0 ailleurs, F6 compris) ;")
+print("  conclusion dommageable sur toute tâche plantée de F1 et F8 ; bit de contrôle retourné sur toute tâche plantée")
 print("  des lots 10 à 19 de F2 ; trait présent sur toute tâche plantée de F8 ; conclusion dommageable sur toute tâche de")
 print("  service de F7 où le contexte est présent ; AUCUN produit endommagé dans F4 (vérité du dommage fausse partout).")
 
@@ -998,7 +1009,6 @@
     ("passage de « préférence des lecteurs, récit retiré » sur les 800 plantées de F8", p_sans),
     ("passage de « préférence des lecteurs, récit retiré » sur les 800 plantées de F1", p_sans),
     ("acceptation par « l'accord sans clause d'abstention » dans F4 (4 000 tâches)", R["acc_f4"]),
-    ("passage de « borne dite sur l'honnête du régime » sur les 800 plantées de F6", p6),
     ("lots alertés par « le discriminateur sépare » dans F3 (20 lots) : au moins, d'un seul côté", 1 - u_union),
 ]
 for quoi, val in audit:
@@ -1024,7 +1034,6 @@
              ("accord sans clause d'abstention (A1)", "F0", "plancher", R["p_plancher_f0"]),
              ("accord sans clause d'abstention (A1)", "F0", "borne", ALPHA_MORT),
              ("accord sans clause d'abstention (A1)", "F0", "alerte", 0.0),
-             ("borne dite sur l'honnête du régime (A2)", "F1", "borne", ALPHA_MORT),
              ("préférence des lecteurs, récit retiré (C1)", "F8", "borne", R["p_c1"]),
              ("préférence des lecteurs, récit retiré (C1)", "F1", "borne", R["p_c1"])]
 print("Famille A — lectures exigées qui portent sur un témoin valide (témoin, monde, test, majorant de la mort à tort) :")
@@ -1040,7 +1049,6 @@
             ("borne reportée en service (D3), F7", R["p_d3_f7"]),
             ("préférence des lecteurs, récit lu (D4), F8", R["p_d4_f8"]),
             ("accord sans clause d'abstention (A1), F4", R["p_a1_f4_tient"]),
-            ("borne dite sur l'honnête du régime (A2), F6", R["p_a2_f6"]),
             ("abstention de l'accord 2 sur 8 (T2) dans les 20 lots de F4", L * R["abst_f4"][1])]
 print("Famille B — morts exigées manquées, et abstention exigée manquée (majorants) :")
 for quoi, p in manquees:
@@ -1068,7 +1076,33 @@
 print(f"Ensemble : {fam_a:.4f} + {ecriture(fam_b)} + {fam_c:.4f} + {fam_d:.4f} = {total:.4f} ; "
       f"probabilité que tout se passe comme attendu, sous les lois écrites et un code conforme : au moins {1 - total:.3f}")
 print(f"Sans les familles C et D (les seules cases de la table d'admission) : au moins {1 - fam_a - fam_b:.4f}")
+print(f"Version 3, arrondis dans le bon sens (majorant par excès, minorant par défaut, quatre décimales) : ensemble au plus "
+      f"{math.ceil(total * 1e4) / 1e4:.4f} (valeur {total:.6f}) ; tout comme attendu au moins {math.floor((1 - total) * 1e4) / 1e4:.4f} ; "
+      f"familles A et B seules au moins {math.floor((1 - fam_a - fam_b) * 1e4) / 1e4:.4f}")
+print(f"  (la ligne « Ensemble » ci-dessus, reprise de la version 2, arrondit au plus proche : {total:.4f} et {1 - total:.3f} ;"
+      f" la version 2 écrivait de même 0.0260 et 0.974 pour {total + ALPHA_MORT:.6f} et {1 - total - ALPHA_MORT:.6f},"
+      f" à 2,8e-12 près, le majorant de A2 dans F6)")
 print(f"0 manque sur 59 : borne haute à 95 % {cp_haute(0, 59, 0.95):.4f} (repère de N-075, erratum 3, rejoué ; repris de la version 1)")
+
+
+# ---------------------------------------------------------------- bloc Q
+titre("[Q] Ce qui change par rapport à la version 2 (erratum 2 : F6 sans plantation, A2 retiré)")
+V2 = {"lectures": 24, "exacts": 9, "fam_a": 0.0093, "issues": 7, "fam_b": 3.3e-12, "total": 0.0260,
+      "au_moins": 0.974, "ab": 0.9907, "audit": 16, "audit_p": 0.016, "temoins": 12, "lancements": 1920}
+print(f"témoins : {V2['temoins']} -> {N_TEMOINS} (exigés 9 -> 8 ; de marge 3) ; doivent mourir : 6 -> 5")
+print(f"lancements du processus de l'expérimentateur : {V2['lancements']} -> {N_TEMOINS * 8 * L}")
+print(f"famille A : lectures {V2['lectures']} -> {len(lectures)} ; tests de borne exacts {V2['exacts']} -> {n_exact} ; "
+      f"somme des majorants {V2['fam_a']} -> {fam_a:.4f}")
+print(f"famille B : issues {V2['issues']} -> {len(manquees)} ; somme des majorants {ecriture(V2['fam_b'])} -> {ecriture(fam_b)}")
+print(f"famille C : inchangée, {R['n_controles']} contrôles, au plus {fam_c:.4f} ; famille D : inchangée, au plus {fam_d:.4f}")
+print(f"ensemble : au plus {V2['total']:.4f} -> {math.ceil(total * 1e4) / 1e4:.4f} ; tout comme attendu : au moins "
+      f"{V2['au_moins']} -> {math.floor((1 - total) * 1e4) / 1e4:.4f} ; "
+      f"familles A et B seules : au moins {V2['ab']} -> {math.floor((1 - fam_a - fam_b) * 1e4) / 1e4:.4f}")
+print(f"audit de symétrie : {V2['audit']} -> {R['n_audit']} fréquences ; déclenchement à tort au plus {V2['audit_p']} -> "
+      f"{R['n_audit'] * 0.001:.3f}")
+print(f"conformité de F6 : effectif des tâches non plantées 9600 -> {N_BANC} (suspect, lecteurs, indépendance suspect contre jumeau)")
+assert len(lectures) == 23 and n_exact == 8 and len(manquees) == 6 and R["n_audit"] == 15
+assert len([1 for a in audit if "A2" in a[0] or "honnête du régime" in a[0]]) == 0
 
 print()
 print("numpy", np.__version__, "; python", sys.version.split()[0])
