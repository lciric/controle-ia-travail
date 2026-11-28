"""Retouche VF2 du fichier de tests (hors livrable) : remplacements exacts, chacun présent une seule fois, sinon refus.
Le module n'est pas touché. Usage : python -I retouche_vf2.py"""
import hashlib
import os
import sys

sys.dont_write_bytecode = True
ICI = os.path.dirname(os.path.abspath(__file__))
TESTS = os.path.join(os.path.dirname(ICI), "test_complements_p3_v1.py")
SHA_AVANT = "7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d"

R = [
    # VF2-01 (M09, M10, M12) : docstring
    (r'''    la même lecture. Cas sain : la lecture saine passe (tout est établi, tout est consulté). Artefacts : `conforme` vrai
    alors que saboteur contre témoin est « non au-dessus » (essai CB2 retourné) ; `conforme` faux alors que les états le
    disent conforme ; T2 établi alors que sa borne basse est ≤ 0 ; T3 non établi alors que ses états l'établissent ;
    P3-P1 « établie » avec une borne basse ≤ 0 (−0,01 et 0) ou non calculable ; P3-P1 non établie alors que calculable et
    borne basse > 0 : arrêt (garde 7), avant toute analyse. Drapeaux non consultés (organisme non établi) : voir
    `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet`."""''',
     r'''    la même lecture. Cas sain : la lecture saine passe (tout est établi, tout est consulté). Artefacts : `conforme` vrai
    alors que saboteur contre témoin est « non au-dessus » (essai CB2 retourné), ou alors que témoin contre honnête est
    « au-dessus » (VF2-01) ; `conforme` faux alors que les états le disent conforme ; T2 établi alors que sa borne basse
    est ≤ 0 (−0,01, et 0 : VF2-01) ; T3 établi alors que saboteur contre mention est « non au-dessus » (VF2-01) ; T3 non
    établi alors que ses états l'établissent ; P3-P1 « établie » avec une borne basse ≤ 0 (−0,01 et 0) ou non
    calculable ; P3-P1 non établie alors que calculable et borne basse > 0 : arrêt (garde 7), avant toute analyse.
    Drapeaux non consultés (organisme non établi) : voir
    `test_organisme_non_etabli_drapeaux_bruts_conformes_reserves_sans_objet`."""'''),
    # VF2-01 (M09, M10, M12) : trois artefacts par `_lecture_recalculee`
    (r'''            (lambda x: x["P3-P1"].__setitem__("calculable", False),
             "P3-P1/etablie vaut True alors que la lecture dit False")):
        with pytest.raises(GardeArret, match="garde 7 : " + motif):''',
     r'''            (lambda x: x["P3-P1"].__setitem__("calculable", False),
             "P3-P1/etablie vaut True alors que la lecture dit False"),
            (lambda x: x["jeux"][P[0]]["temoin-honnete"].__setitem__("au_dessus_du_plancher", True),      # VF2-01
             "P3-P4/.*/conforme vaut True alors que les états de la lecture disent False"),
            (lambda x: x["jeux"][P[0]]["saboteur-mention"].__setitem__("au_dessus_du_plancher", False),   # VF2-01
             "intention/.*/T3/etabli vaut True alors que la lecture dit False"),
            (lambda x: x["intention"][P[0]]["T2"].__setitem__("bas", 0.0),                                # VF2-01
             "intention/.*/T2/etabli vaut True alors que la lecture dit False")):
        with pytest.raises(GardeArret, match="garde 7 : " + motif):'''),
    # VF2-02 (M11) : docstring et seconde partie
    (r'''    """Run synthétique « organisme non établi » dont les drapeaux bruts disent « conforme » (P3-P4, T1 à T4) :
    `conclusions_etablies` vide, « réserves sans objet », aucun contrôle lu."""''',
     r'''    """Run synthétique « organisme non établi » dont les drapeaux bruts disent « conforme » (P3-P4, T1 à T4) :
    `conclusions_etablies` vide, « réserves sans objet », aucun contrôle lu. Puis `conforme` contraire aux états de la
    lecture (négation de la valeur lue, VF2-02), issue recalculée : drapeau non consulté, aucun arrêt, conclusions vides."""'''),
    (r'''    assert s["audit_symetrie_addendum"]["reserves_possibles"] == 0 and not s["audit_symetrie_addendum"]["declencheur"]


ARTEFACTS = {''',
     r'''    assert s["audit_symetrie_addendum"]["reserves_possibles"] == 0 and not s["audit_symetrie_addendum"]["declencheur"]
    src, lec, _ = _cas("a6_verrou")                                      # VF2-02 : `conforme` contraire aux états
    for p in P:
        st, th = lec["etats_des_jeux"][p]["saboteur-temoin"], lec["etats_des_jeux"][p]["temoin-honnete"]
        assert lec["P3-P4"][p]["conforme"] == (st == lp.AU_DESSUS and th == lp.NON_AU_DESSUS)
        lec["P3-P4"][p]["conforme"] = not lec["P3-P4"][p]["conforme"]
    lec["issue"] = lp.issue(lec)
    assert lec["issue"]["ligne"] == "organisme non établi"
    s = _addendum(src, lec)                                              # aucun arrêt
    assert s["conclusions_etablies"] == [] and s["reserves_addendum"] == []
    assert s["recommandation_au_verdict_R13"] == ["aucune conclusion établie : réserves sans objet"]


ARTEFACTS = {'''),
    # VF2-04 (M19) : ligne de trois espaces
    (r'''`splitlines` aurait coupé) ; garde 5 passée ; lignes vides ignorées. Artefacts : ligne tronquée, ligne d'octets non
    UTF-8 : arrêt (garde 4), numéro de la ligne dans le motif, aucun texte ; empreinte autre : arrêt."""''',
     r'''`splitlines` aurait coupé) ; garde 5 passée ; lignes vides ignorées. Artefacts : ligne tronquée, ligne d'octets non
    UTF-8, ligne de trois espaces (non vide, donc lue : VF2-04) : arrêt (garde 4), numéro de la ligne dans le motif,
    aucun texte ; empreinte autre : arrêt."""'''),
    (r'''                                  ("non-utf8", 6, lignes[6][:40] + b"\xff\xfe" + lignes[6][40:], "UnicodeDecodeError")):''',
     r'''                                  ("non-utf8", 6, lignes[6][:40] + b"\xff\xfe" + lignes[6][40:], "UnicodeDecodeError"),
                                  ("espaces", 2, b"   ", "JSONDecodeError")):                    # VF2-04'''),
    # VF2-05 (M13) : garde 12 à 1e-6 (artefact) et 1e-12 (cas sain)
    (r'''def test_garde_coherence_de_la_lecture_avec_le_run_source():
    src, lec, s = _cas("sain")''',
     r'''def test_garde_coherence_de_la_lecture_avec_le_run_source():
    """Garde 12, à 1e-9 près. Cas sains : lecture saine ; écart de 1e-12 sur une aire (VF2-05). Artefacts : écart de 0,01
    ou de 1e-6 (VF2-05) sur une aire ; lecture d'un autre run source : arrêt."""
    src, lec, s = _cas("sain")'''),
    (r'''    with pytest.raises(GardeArret, match="garde 12 : lecture décisive incohérente"):
        _addendum(src, l2)
    autre, lec_autre, _ = _cas("a1_plancher")''',
     r'''    with pytest.raises(GardeArret, match="garde 12 : lecture décisive incohérente"):
        _addendum(src, l2)
    l3 = copy.deepcopy(lec)                                              # VF2-05
    l3["jeux"][P[0]]["saboteur-honnete"]["aire"] += 1e-12                # cas sain : écart de 1e-12
    assert cp.exiger_coherence(l3, cp._donnees(src), cp.lire_la_lecture(l3, P))["controles"] == 10
    l3["jeux"][P[0]]["saboteur-honnete"]["aire"] += 1e-6                 # artefact : écart de 1e-6
    with pytest.raises(GardeArret, match="garde 12 : lecture décisive incohérente"):
        _addendum(src, l3)
    autre, lec_autre, _ = _cas("a1_plancher")'''),
    # VF2-05 (M14) : garde 13 à 2e-9
    (r'''    sains : écarts de 1e-12 et de 5e-10 ; artefacts : écart de 1e-6 sur le pré-coût ou sur le coût,
    lignes décalées : arrêt."""''',
     r'''    sains : écarts de 1e-12 et de 5e-10 ; artefacts : écart de 1e-6 ou de 2e-9 (VF2-05) sur le pré-coût, de 1e-6 sur
    le coût, lignes décalées : arrêt."""'''),
    (r'''    for cle, ecart in (("pre", 1e-6), ("cout", -1e-6), ("lignes", 1)):''',
     r'''    for cle, ecart in (("pre", 1e-6), ("pre", 2e-9), ("cout", -1e-6), ("lignes", 1)):'''),
    # VF2-06 (M24) : suffixe après « addendum-p3 »
    (r'''                                   ("addendum-p3", cp.PREREG_ADDENDUM, "garde 15 : run de .*addendum-p3"),''',
     r'''                                   ("addendum-p3", cp.PREREG_ADDENDUM, "garde 15 : run de .*addendum-p3"),
                                   ("20261020-130000-addendum-p3-bis", cp.PREREG_ADDENDUM,        # VF2-06
                                    "garde 15 : run de .*addendum-p3"),'''),
]

if __name__ == "__main__":
    texte = open(TESTS, encoding="utf-8").read()
    if hashlib.sha256(texte.encode("utf-8")).hexdigest() != SHA_AVANT:
        sys.exit("fichier de tests : empreinte autre que celle d'avant la retouche")
    for i, (avant, apres) in enumerate(R):
        if texte.count(avant) != 1:
            sys.exit(f"remplacement {i} : motif présent {texte.count(avant)} fois")
        texte = texte.replace(avant, apres)
    longues = [n for n, x in enumerate(texte.split("\n"), 1) if len(x) > 120]
    open(TESTS, "w", encoding="utf-8").write(texte)
    print(f"{len(R)} remplacements ; lignes de plus de 120 caractères : {longues}")
    print(hashlib.sha256(texte.encode("utf-8")).hexdigest())
