# Vérification lot 13 v2
Verdict : CONFORME. 9 essais passés ; empreintes de mini_passe_v2.py et test_mini_passe_v2.py : OK.
Diff v1→v2 : en-tête, commentaire de VERSION, `m.P_X = m.D("24.20")`, `P.verifier_go(o.registre_go, GO_EXIGES)`. Rien d'autre.
1. GO : liste passée explicitement. test_v2_go_70_exige refuse sans GO-70 ; test_v2_main_refuse_sans_go_70 : main rend 2 avec (46,48,54), 0 avec (70,54) en a blanc.
2. Plafond : P_X = 24.20 dans le module chargé (la garde G7 refuse > 24,20, testé à 18,16+6,05 ; la configuration réelle 18,15+6,05 = 24,20 passe). La limite de relance de Kimi est déclarée dans l'en-tête.
Réserve résiduelle (déjà connue) : relances Google non garanties (18,15 = 3 tentatives au pire).
