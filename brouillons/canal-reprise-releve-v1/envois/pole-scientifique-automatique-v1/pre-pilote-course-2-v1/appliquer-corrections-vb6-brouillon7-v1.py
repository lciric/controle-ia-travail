"""Brouillon 7 = brouillon 6 + corrections VB6-01 à VB6-11 de la vérification courte (verification-corrections-brouillon6-v1.md).
Usage : python3 -I appliquer-corrections-vb6-brouillon7-v1.py BROUILLON6 BROUILLON7 HH:MM
Remplacements exacts ; chaque chaîne cherchée doit être unique (assert) ; aucun chiffre de simulation n'est changé : tout chiffre
nouveau vient de calcul-puissance-pre-pilote-course-2-v6.sortie.txt (7394ddae…) ou est marqué « dérivé »."""
import sys
src, dst, heure = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()

def rep(old, new, n=1):
    global t
    c = t.count(old)
    assert c == n, (c, old[:80])
    t = t.replace(old, new)

B6 = "c54a105b7c9a9fc39694e8a957003bbf5cc017af20c45bd6ca354d91be24493d"
VB6 = "27b8e07550a07db1dd2ed7bddcc2b2ab32b143391e61fb693afb466048fc481d"
FOURNIR = "À FOURNIR AU SCELLEMENT"   # mot distinct des six valeurs à fournir, qui ne sont pas des décisions de Lazar (VB6-10)

# ---- En-tête, statut, documents (VB6-11 : ** orphelin de la ligne 3 retiré) ----
rep("# Préenregistrement — Pré-pilote d'étalonnage des instruments de la course 2 — brouillon 6",
    "# Préenregistrement — Pré-pilote d'étalonnage des instruments de la course 2 — brouillon 7")
rep("**Statut : brouillon 6, non scellé ; vérification courte des corrections à faire** (sous-agent neuf d'un modèle différent de l'auteur, "
    "qui est un Fable 5.1 ; la contre-lecture 4 a été rendue par un Opus 5.5 neuf). Les 13 constats de la contre-lecture 4 (« gelable après "
    "corrections », CP5-01 à CP5-13) sont traités, chacun à un endroit nommé dans « Ce qui change par rapport au brouillon 5 » ; les 17 "
    "constats de la contre-lecture 3 restent traités.",
    "**Statut : brouillon 7, non scellé ; présentable à Lazar (vérification VB6 traitée) ; contre-lecture 5 après gel.** Les 11 constats de "
    "la vérification courte du brouillon 6 (VB6-01 à VB6-11 ; Sonnet 5.5 neuf, modèle différent de l'auteur, qui est un Fable 5.1 ; verdict "
    "« présentable après corrections mineures ») sont traités, chacun à un endroit nommé dans « Ce qui change » ; les 13 constats de la "
    "contre-lecture 4 (CP5-01 à CP5-13, Opus 5.5 neuf) et les 17 constats de la contre-lecture 3 restent traités.")
rep("**Chaque décision de Lazar porte un marqueur de remplissage unique, dans la ligne qui recevra sa valeur (section « Seuil » ; "
    "contre-lecture 5 ; commit et empreinte de l'annexe en tête) ; aucune mention descriptive n'emploie ce marqueur** (CP5-03).",
    "**Chaque décision de Lazar (43) porte le marqueur de remplissage du gabarit, une fois, dans la ligne qui recevra sa valeur (sections "
    "« Seuil » et « Rôles, témoins et dépendances ») ; les six valeurs ou faits à fournir au scellement, qui ne sont pas des décisions de "
    "Lazar (commit du code, empreinte de l'annexe, source et essai de S31, k, résumé du tableau, contre-lecture 5), portent un mot distinct "
    "en capitales, « à fournir au scellement » (VB6-10) ; aucune mention descriptive n'emploie l'un ni l'autre** (CP5-03).")
rep("Le brouillon 5 (`96080471abf69c1166a99c993c17c9408dd016a43f916e0ae8a2af63cd5475b3`) et les brouillons 1 à 4 sont gardés sans "
    "modification (R12).**",
    "Le brouillon 6 (`" + B6 + "`) et les brouillons 1 à 5 sont gardés sans modification (R12).")
rep("pour Lazar (brouillon 6 : traitement de la contre-lecture 4 ; l'auteur du brouillon 6 n'a écrit ni les brouillons 1 à 5 ni aucune "
    "contre-lecture ;",
    "pour Lazar (brouillon 6 : traitement de la contre-lecture 4 ; brouillon 7 : corrections VB6-01 à VB6-11, appliquées à " + heure +
    " UTC par un sous-agent Fable 5.1 neuf de la même lignée, script `appliquer-corrections-vb6-brouillon7-v1.py` ; aucun des deux n'a écrit "
    "les brouillons 1 à 5, une contre-lecture ni la vérification ;")
rep("**`preenregistrement-pre-pilote-course-2-brouillon5.md` `96080471abf69c1166a99c993c17c9408dd016a43f916e0ae8a2af63cd5475b3` "
    "(base de travail de ce brouillon)** ;",
    "`…brouillon5.md` `96080471abf69c1166a99c993c17c9408dd016a43f916e0ae8a2af63cd5475b3` ; **`preenregistrement-pre-pilote-course-2-brouillon6.md` `"
    + B6 + "` (base de travail de ce brouillon)** ;")
rep("(Opus 5.5 neuf, 2026-10-31 00:19 UTC ; compagnon `.sha256` conforme)** ;",
    "(Opus 5.5 neuf, 2026-10-31 00:19 UTC ; compagnon `.sha256` conforme)** ; **vérification courte des corrections du brouillon 6 : "
    "`verification-corrections-brouillon6-v1.md` `" + VB6 + "` (Sonnet 5.5 neuf, 2026-10-31 00:51 UTC ; `sha256sum` à la lecture, "
    "compagnon `.sha256` à écrire par conv-audit)** ;")

# ---- Ce qui change : ligne du brouillon 7 et table VB6 → où ----
rep("## Ce qui change par rapport au brouillon 5 (constat CP5-xx → où)\n\n| Constat | Changement | Où |",
    "## Ce qui change par rapport au brouillon 5 (constat CP5-xx → où)\n\n"
    "**Brouillon 7 : corrections VB6-01 à VB6-11 (vérification courte, Sonnet 5.5 neuf)** — rapport `verification-corrections-brouillon6-v1.md` "
    "(`" + VB6 + "`), appliqué à " + heure + " UTC par le script `appliquer-corrections-vb6-brouillon7-v1.py` (remplacements exacts, un par "
    "constat) ; aucun chiffre de simulation, aucun seuil, aucune règle de lecture ni d'arrêt changés ; le script v6 et sa sortie restent la source ; "
    "les confiances des lectures L1 à L7 sont celles de l'auteur du brouillon 7 (nouvelles, VB6-02).\n\n"
    "| Constat | Changement | Où |\n|---|---|---|\n"
    "| VB6-01 (moyen) | Résidu du brouillon 5 corrigé : « complément proposé 0,18, porte ouverte au total 0,20 » (sortie v6 ; 0,20 et 0,22 au brouillon 5) | Critères, « Complément » |\n"
    "| VB6-02 (moyen) | **L1 à L7 au format de décision** : phrase, enjeu, options (avantage, inconvénient), recommandation et confiance, aucun défaut ; contenu tiré des lectures déjà écrites (M8, Plan, M9, C10, Contre-lecture) | Décisions à Lazar, « Lectures à confirmer L1 à L7 » ; résumé (table) |\n"
    "| VB6-03 (mineur) | D-g : « +0,002 » attribué à D-g (b) et D-i (2) ensemble (0,156 → 0,158, sortie v6 ; D-g (b) seule n'est pas jouée) ; « seuil de 3 USD » non sourcé retiré | Décisions à Lazar, D-g |\n"
    "| VB6-04 (mineur) | **DEP4 (règle de relais) ajoutée aux conditions d'A15** : aucun lancement sans confirmation par session-depot ; conséquence « relais dur » (0,80 de coupure d'une étape protégée, sortie v6) écrite dans S17 (Seuil et Décisions) et dans DEP4 | A15 ; Seuil S17 ; Décisions S17 ; DEP4 |\n"
    "| VB6-05 (mineur) | « autres 0,004 » → 0,005, marqué dérivé (0,0803 − 0,0756 ; recommandée 0,0695 − 0,0614 = 0,008) | Seuil S17 ; Plan (table des sacrifices) |\n"
    "| VB6-06 (mineur) | Résumé 6 : « C6 0,95 → 0,97 » précisé « sans sacrifice » ; valeurs mélangées 0,93 → 0,95 données à côté | Résumé 6 |\n"
    "| VB6-07 (mineur) | 0,475 écrit tel quel (cinq endroits) ; 35,5 renvoyé à la sortie v3 (`72fd43a5…`, ligne 32) ; 0,13 (M9, D-h (b)) et ≈ 0,003 (A19 et A20) marqués « dérivé » avec leur calcul | Ce qui change (CP5-11) ; P10 ; M6b ; S30 ; D-g ; S17 ; Critères (M9, hors porte) |\n"
    "| VB6-08 (mineur) | Cas « effectif n < 3 » sorti de la ligne « un bras non produit » et rangé sous « deux bras ou plus non produits » (n = 2 : deux bras ; n < 2 : trois) ; cas restants renumérotés (i) à (iv) | Critères, table M9 |\n"
    "| VB6-09 (mineur) | « Avantage » écrit pour D-f (ii) et (iii) et pour S17 « 32 ; 28 » | Décisions à Lazar, D-f, S17 |\n"
    "| VB6-10 (mineur) | Table des marqueurs : 43 décisions de Lazar (marqueur du gabarit) et 6 valeurs à fournir au scellement (mot distinct en capitales, non refusé par le validateur : vérifié au scellement par une recherche de texte) ; lecture du validateur écrite ; empreintes des contre-lectures 1 et 2 écrites en entier dans « Contre-lecture » pour que le validateur les lise une fois le marqueur retiré de cette section | Statut ; en-tête ; M1 (k) ; M8 ; Seuil (table des marqueurs) ; Contre-lecture |\n"
    "| VB6-11 (mineur) | `**` fermant sans ouvrant retiré (statut) | Statut |\n\n"
    "**Rappel : ce qui a changé au brouillon 6 (constat CP5-xx → où).**\n\n| Constat | Changement | Où |")
rep("P10 « 3 sur 4 au moins » à 0,60 : 0,48 (sortie v6) ;", "P10 « 3 sur 4 au moins » à 0,60 : 0,475 (sortie v6) ;")

# ---- VB6-06 : résumé 6 ----
rep("(+0,5 USD, C6 0,95 → 0,97, recommandé)",
    "(+0,5 USD ; C6 0,95 → 0,97 sans sacrifice, 0,93 → 0,95 mélangée au sacrifice de la table seule, sortie v6 ; recommandé)")

# ---- Résumé, table : L1 à L7 ----
rep("| lectures de l'auteur, une ligne chacune en « Seuil » |",
    "| lectures de l'auteur, une ligne chacune en « Seuil » ; format de décision (enjeu, options, confiance) dans la section finale (VB6-02) |")

# ---- VB6-10 : les six valeurs à fournir au scellement ----
rep("- Commit du code d'analyse : À REMPLIR au scellement (aucun code d'analyse n'existe encore) ;",
    "- Commit du code d'analyse : " + FOURNIR + " (valeur, non une décision de Lazar ; aucun code d'analyse n'existe encore) ;")
rep("`annexe-bras-meta-v1.md`, même dossier, empreinte : À REMPLIR au gel (CP4-02) ;",
    "`annexe-bras-meta-v1.md`, même dossier, empreinte : " + FOURNIR + " (CP4-02) ;")
rep("chemin et empreinte de la moisson (ou du graphe publié) et de l'essai de S31 sur elle : À REMPLIR au gel (CP5-01) ;",
    "chemin et empreinte de la moisson (ou du graphe publié) et de l'essai de S31 sur elle : " + FOURNIR + " (CP5-01) ;")
rep("valeur lue sur la consigne empreintée : À REMPLIR au gel)", "valeur lue sur la consigne empreintée : " + FOURNIR + ")")
rep("lequel, lu sur la consigne de la course : À REMPLIR au gel)", "lequel, lu sur la consigne de la course : " + FOURNIR + ")")

# ---- VB6-07 : 0,475 ; 35,5 sourcé ; dérivés marqués ----
rep("soit « 3 sur 4 au moins » avec 0,48 (sortie v6, CP5-11)", "soit « 3 sur 4 au moins » avec 0,475 (sortie v6, CP5-11)")
rep("« 3 sur 4 au moins » se voit avec 0,74 à rappel vrai 0,75, 0,48 à 0,60 et 0,31 à 0,50 (sortie v6)",
    "« 3 sur 4 au moins » se voit avec 0,74 à rappel vrai 0,75, 0,475 à 0,60 et 0,31 à 0,50 (sortie v6)")
rep("« 3 sur 4 au moins » à rappel vrai 0,60 : 0,48)", "« 3 sur 4 au moins » à rappel vrai 0,60 : 0,475)", n=2)
rep("R-630 recommande 45 (médiane prédite du brouillon 3, 35,5, plus une marge pour l'étape protégée)",
    "R-630 recommande 45 (médiane prédite du brouillon 3 : 35,5, sortie v3 `72fd43a5…`, ligne 32 ; plus une marge pour l'étape protégée)")
rep("probabilité 0,024 (SUPPOSÉ ; D-h (b) : 0,13)",
    "probabilité 0,024 (SUPPOSÉ ; D-h (b) : 0,13, dérivé de la sortie v6 : 1 − 0,864 / 0,99)")
rep("ferment C12 avec ≈ 0,003 (SUPPOSÉ), compté dans C12.",
    "ferment C12 avec ≈ 0,003 (dérivé : 0,03 × 0,10, SUPPOSÉ ; non imprimé par le script), compté dans C12.")

# ---- VB6-08 : cas n < 3 rangé sous « deux bras ou plus » ----
rep("| M9 | **un bras non produit** — cas écrits (CP5-01) : (i) effectif n < 3 (tirage de priorité) ; (ii) bras méta « non produit (annexe non "
    "conforme) », A20, décidé à É0 ; (iii) bras Gu-Krenn « non produit (source absente) », A19, décidé à É0 ; (iv) bras Gu-Krenn « non produit "
    "(moins de 2 fiches notables) » ; (v) bras basique « non produit (moins de 2 fiches étiquetées) » |",
    "| M9 | **un bras non produit** — cas écrits (CP5-01 ; VB6-08) : (i) bras méta « non produit (annexe non conforme) », A20, décidé à É0 ; "
    "(ii) bras Gu-Krenn « non produit (source absente) », A19, décidé à É0 ; (iii) bras Gu-Krenn « non produit (moins de 2 fiches notables) » ; "
    "(iv) bras basique « non produit (moins de 2 fiches étiquetées) » — l'effectif n < 3 n'est pas de ce cas : il en retire deux ou trois (ligne suivante) |")
rep("| M9 | **deux bras ou plus non produits** (sous D-h (b) : l'un des deux) | C12 non satisfaite",
    "| M9 | **deux bras ou plus non produits** (sous D-h (b) : l'un des deux) — par l'effectif n < 3 (règle de M9 : n = 2, une paire au bras de "
    "priorité 1, deux bras « non produits (effectif) » ; n < 2, aucun bras ; cause « n < 3 : 0,02 » de C12), ou par deux des cas (i) à (iv) "
    "ci-dessus (VB6-08) | C12 non satisfaite")

# ---- VB6-01 : résidu du brouillon 5 ----
rep("À la prédiction P1 : complément proposé 0,20, porte ouverte au total 0,22. Pas de second complément.",
    "À la prédiction P1 : complément proposé 0,18, porte ouverte au total 0,20 (sortie v6 : 0,176 et 0,201 ; 0,20 et 0,22 au brouillon 5). "
    "Pas de second complément.")

# ---- VB6-05 : « autres 0,004 » dérivé ----
rep("étape protégée non lancée 0,080 (M6 réduite qui ne tient pas 0,076 ; autres 0,004)",
    "étape protégée non lancée 0,080 (M6 réduite qui ne tient pas 0,076 ; autres 0,005, dérivé : 0,0803 − 0,0756)")
rep("| Autre étape protégée non lancée ou coupée à S17 | 0,004 (0,008) |",
    "| Autre étape protégée non lancée ou coupée à S17 | 0,005 (0,008) (dérivés de la sortie v6 : 0,0803 − 0,0756 ; 0,0695 − 0,0614) |")

# ---- VB6-04 : DEP4 dans A15, S17 (Seuil et Décisions), DEP4 ----
rep("Au plafond de 32 : voir ci-dessus (sacrifices 0,92 ; C13 budget 0,66). Le total séquencé (110 ou 123) est la lecture L4.",
    "Au plafond de 32 : voir ci-dessus (sacrifices 0,92 ; C13 budget 0,66). Le total séquencé (110 ou 123) est la lecture L4. **Ces chiffres "
    "supposent la règle de relais de DEP4 (le relais accepte une réservation dépassée jusqu'à S17 − cumul et coupe à S17 seulement ; à confirmer "
    "par session-depot, non une décision de Lazar) ; si le relais est dur (chaque relais coupe à son propre plafond), une étape protégée est "
    "coupée avec 0,80 (sortie v6) et le Plan est à réécrire : A15 n'autorise aucun lancement sans cette confirmation (VB6-04).**")
rep("| A15 | décision manquante : confidentialité (fiches vers Moonshot et Google), D-f, **ligne de GO au plafond gelé S17** (aucun lancement "
    "à un autre plafond), D-g à D-j, ou GO de lancement | **aucun lancement** |",
    "| A15 | décision manquante : confidentialité (fiches vers Moonshot et Google), D-f, **ligne de GO au plafond gelé S17** (aucun lancement "
    "à un autre plafond), D-g à D-j, ou GO de lancement ; **ou confirmation de DEP4 par session-depot absente** (le relais accepte une "
    "réservation dépassée jusqu'à S17 − cumul et coupe à S17 seulement ; sinon la lecture « relais dur » s'applique — étape protégée coupée "
    "avec 0,80, sortie v6 — et le Plan est à réécrire dans une version nouvelle, R12 ; VB6-04) | **aucun lancement** |")
rep("sinon la lecture « relais dur » de la sortie v6 s'applique et le Plan est à réécrire) ;",
    "sinon la lecture « relais dur » de la sortie v6 s'applique — étape protégée coupée avec 0,80 — et le Plan est à réécrire ; **A15 : aucun "
    "lancement sans cette confirmation**, VB6-04) ;")

# ---- VB6-10 : table des marqueurs ----
rep("Emplacements : en-tête (commit du code d'analyse ; empreinte de l'annexe ; source et essai de S31) ; Métrique (k items de la consigne "
    "figée ; résumé d'une ligne du tableau minimal) ; Seuil (S1 à S4, S6 à S21, S23 à S25, S27 à S31, D-e à D-j, L1 à L7) ; Rôles et "
    "dépendances (confidentialité, DEP4 ; mot sur l'étalonnage de l'aiguilleur, DEP5) ; Contre-lecture (contre-lecture 5). Compte attendu : 49 "
    "(3 en tête ; 2 en Métrique ; 41 en Seuil ; 2 en Rôles et dépendances ; 1 en Contre-lecture).",
    "**Deux sortes (VB6-10).** (1) **Décisions de Lazar, 43**, marqueur du gabarit : Seuil (S1 à S4, S6 à S21, S23 à S25, S27 à S31, D-e à "
    "D-j, L1 à L7 : 41) ; Rôles, témoins et dépendances (confidentialité, DEP4 ; mot sur l'étalonnage de l'aiguilleur, DEP5 : 2). (2) **Valeurs "
    "ou faits à fournir au scellement, 6**, qui ne sont pas des décisions de Lazar, portés par un mot distinct en capitales, « à fournir au "
    "scellement » : en-tête (commit du code d'analyse ; empreinte de l'annexe ; source et essai de S31 : 3) ; Métrique (k items de la consigne "
    "figée ; résumé d'une ligne du tableau minimal : 2) ; Contre-lecture (contre-lecture 5 : 1). **Lecture du validateur** : il refuse le "
    "marqueur du gabarit partout, mais tant qu'une section exigée le porte, il tait le message « hors des sections exigées » ; les deux marqueurs "
    "de « Rôles, témoins et dépendances » (section non exigée) ne sont donc signalés qu'une fois « Seuil » remplie, et le sont alors ; il ne "
    "connaît pas le mot distinct : au scellement, une recherche de texte vérifie qu'il n'en reste aucun (compte attendu 0) ; la contre-lecture 5, "
    "une fois le mot retiré de sa section, est exigée par la règle des deux empreintes (brouillon relu et rapport, 64 caractères chacune).")

# ---- Contre-lecture : empreintes 1 et 2 en entier ; vérification VB6 ; contre-lecture 5 après gel ----
rep("brouillon 1 `8d6142eb…` ; rapport `contre-lecture-pre-pilote-course-2-brouillon1.md` `96cf300b…` ;",
    "brouillon 1 `8d6142eb3be04c1f732f3a148e35d791239fed417897ed82ad0eb49155fdcfdd` ; rapport `contre-lecture-pre-pilote-course-2-brouillon1.md` "
    "`96cf300bed14064a9e4a45d2d2d63474e20bd3e68f26c43df742c059d570c62c` ;")
rep("brouillon 2 `8afb556f…` ; rapport `…brouillon2.md` `e5added0…` ;",
    "brouillon 2 `8afb556f5f96e69bdb7ff57cf19ff053c581f71d08274e0e6fc44fd0fd7eb8f9` ; rapport `…brouillon2.md` "
    "`e5added0e0a589dd0521822a6b2dcbf4cd6a58999b7c69ca87613814e15e7d03` ;")
rep("- **Contre-lecture 5 (R2) — vérification courte des corrections, sur ce brouillon 6** : À REMPLIR (sous-agent neuf, modèle différent de "
    "l'auteur Fable 5.1, ni l'un des quatre premiers contre-lecteurs ni l'auteur d'un brouillon ; empreinte de ce brouillon ; chemin et empreinte "
    "de son rapport). Pièces à lui donner explicitement : ce brouillon et son `.sha256`, le brouillon 5 et son `.sha256`, la contre-lecture 4, "
    "le script v6 et sa sortie (et la v5 pour comparaison),",
    "- **Vérification courte des corrections du brouillon 6** — Sonnet 5.5 neuf (`claude-sonnet-5-5`), 2026-10-31 00:51 UTC ; brouillon relu : "
    "`preenregistrement-pre-pilote-course-2-brouillon6.md` `" + B6 + "` ; rapport : `verification-corrections-brouillon6-v1.md` `" + VB6 +
    "` (`sha256sum` à la lecture ; compagnon `.sha256` à écrire par conv-audit) ; verdict « présentable après corrections mineures », 11 constats "
    "(0 majeur, 2 moyens, 9 mineurs) ; CP5-01 à CP5-13 tous jugés tenus ; script v6 rejoué à l'identique ; 49 marqueurs comptés. **Traitement : "
    "tous acceptés** (table « Brouillon 7 » en tête de « Ce qui change »). Choix déclarés : VB6-10, les six valeurs à fournir reçoivent un mot "
    "distinct que le validateur ne connaît pas (vérification par recherche de texte au scellement) ; VB6-02, les confiances de L1 à L7 sont "
    "nouvelles (auteur du brouillon 7) ; VB6-08, les cas de bras non produit sont renumérotés.\n"
    "- **Contre-lecture 5 (R2) — sur la version gelée (valeurs de Lazar écrites, annexe empreintée), avant le scellement** : " + FOURNIR +
    " (sous-agent neuf, modèle différent de l'auteur Fable 5.1, ni l'un des quatre premiers contre-lecteurs, ni l'auteur de la vérification, ni "
    "l'auteur d'un brouillon ; empreinte de la version relue ; chemin et empreinte de son rapport). Pièces à lui donner explicitement : la version "
    "gelée et son `.sha256`, ce brouillon 7 et le brouillon 6 avec leurs `.sha256`, la contre-lecture 4 et la vérification VB6, le script v6 et "
    "sa sortie (rejoués sur les valeurs gelées si elles diffèrent des recommandations),")
rep("(4) la table des marqueurs : 49 marqueurs, un par décision, aucun descriptif ; la sortie de `problemes` ;",
    "(4) la table des marqueurs : 43 marqueurs du gabarit, un par décision de Lazar, tous remplis au gel ; aucun mot « à fournir au scellement » "
    "restant ; la sortie de `problemes` vide ;")

# ---- VB6-03 : D-g ----
rep("avantage : ≈ 1,6 USD, plafond 2,5 (sous le seuil de 3 USD que je m'étais fixé), premier signal sur le vrai sens d'« inédit » ;",
    "avantage : ≈ 1,6 USD, plafond 2,5, premier signal sur le vrai sens d'« inédit » ;")
rep("sur la porte : +0,002 (sortie v6, configuration recommandée contre texte de base à D-i égal).",
    "sur la porte : +0,002 pour D-g (b) et D-i (2) ensemble (0,156 → 0,158, sortie v6 ; D-g (b) seule n'est pas jouée ; D-i (2) seule donne "
    "0,157).")

# ---- VB6-09 et VB6-04 : S17 (Décisions) ; D-f ----
rep("**32 ; 28** — porte 0,11 (0,10), sacrifice 0,92 (0,98), C13 budget 0,66 (0,62), couverte par GO-2026-10-30-07 ; inconvénient :",
    "**32 ; 28** — porte 0,11 (0,10), sacrifice 0,92 (0,98), C13 budget 0,66 (0,62) ; avantage : couverte par GO-2026-10-30-07, aucune ligne de "
    "GO nouvelle à écrire ; inconvénient :")
rep("je garde 40 parce qu'une M6 « non mesurée » est un nœud alors qu'une table seule retirée est une réserve.",
    "je garde 40 parce qu'une M6 « non mesurée » est un nœud alors qu'une table seule retirée est une réserve. *Dépendance, non une décision "
    "de Lazar (VB6-04)* : tous ces chiffres supposent la règle de relais de DEP4 (réservation dépassée acceptée jusqu'à S17 − cumul, coupure à "
    "S17 seulement), à confirmer par session-depot ; si le relais est dur, une étape protégée est coupée avec 0,80 (sortie v6), le Plan est à "
    "réécrire et A15 interdit le lancement.")
rep("(ii) T = Opus 5.5 — inconvénient : Opus est juge (A9). (iii) relecteur = Kimi ou Argon — inconvénient : ils sont juges.",
    "(ii) T = Opus 5.5 — avantage : instance déjà sous relais, aucun fournisseur ni coût de mise en place nouveaux ; inconvénient : Opus est "
    "juge (A9). (iii) relecteur = Kimi ou Argon — avantage : relecteur hors de la famille Claude, biais de famille de CP2-05 évité ; "
    "inconvénient : ils sont juges.")

# ---- VB6-02 : L1 à L7 au format de décision ----
L_OLD = ("**Lectures à confirmer L1 à L7** (une ligne chacune, marqueurs en « Seuil », aucun défaut) : L1 passe « tableau » gardée (M8) ; L2 "
         "table seule de l'axe 7 gardée (Plan) ; L3 désaccord hors score (M9) ; L4 total séquencé 110 ou 123 (C10) ; **L5 fusions retirées par "
         "A1 : C12 lue sur les paires, réserve (recommandé) ou C13 non satisfaite** (CP5-02) ; L6 S27 réserve ; L7 brouillon 3 sans "
         "contre-lecture. Les lectures « retrait de l'appariement » et « Gu-Krenn sans reproduction » sont les décisions D-i et D-j.")
L_NEW = (
"**Lectures à confirmer L1 à L7** (marqueurs en « Seuil » ; même format que les décisions ; aucun défaut ; confiances de l'auteur du brouillon 7, "
"VB6-02). Les lectures « retrait de l'appariement » et « Gu-Krenn sans reproduction » sont les décisions D-i et D-j.\n\n"
"**L1 — Passe « tableau » de Kimi (M8).** *Décision* : garder la passe « tableau » (≤ 10 fiches après le tableau minimal) ou la retirer. *Enjeu* : "
"elle est ce que la course fait, elle exerce les cloisons en run et porte M5 à 20 fiches ; R-634 interdit toute mesure de performance de "
"l'organisme, et Lazar pourrait la lire comme telle. *Options* : gardée (sacrifiable de rang 4 ; retirée par A1 avec 0,04, 0,07 recommandée) — "
"avantage : M5 sur 20 fiches (« zéro vu sur 20 » borne le taux à 0,14 ; un taux vrai de 0,20 est déclaré conforme avec 0,22), cloisons exercées "
"en run, redites mesurées (P13) ; inconvénient : ≈ 3,1 USD (passe 2,0 ; aiguilleur et second lecteur 1,1), et son effet n'est pas testé, ce qui "
"est voulu. Retirée — avantage : −3,1 USD ; inconvénient : M5 sur 10 fiches (« zéro vu sur 10 » borne le taux à 0,26 ; taux vrai 0,20 déclaré "
"conforme avec 0,39 ; C8 0,91 au lieu de 0,92, sortie v6), redites non mesurées, cloisons éprouvées en É0 seulement. *Recommandation* : "
"**gardée**, confiance 0,7.\n\n"
"**L2 — Table seule de l'axe 7 (Plan, CP4-16).** *Décision* : garder la lecture « table seule » (verdict d'Opus sur les 24 éléments de l'axe 7, "
"0,7 USD, sacrifiable de rang 3) ou la réduire aux bardeaux seuls. *Enjeu* : l'axe 7 est le plus exposé aux paraphrases des huit questions ; la "
"table est écrite par le proposeur ; la version réduite perd la mesure de la table. *Options* : gardée — avantage : les deux gardes mesurées, "
"union prédite 0,75 (table seule 0,50, bardeaux 0,60), C6 0,95 sans sacrifice (0,93 mélangée) ; inconvénient : 0,7 USD, retirée par A1 avec "
"0,13 (0,145). Réduite aux bardeaux — avantage : 0 USD, rien à sacrifier ; inconvénient : C6 0,81 (0,83), la table n'est pas éprouvée avant la "
"course. *Recommandation* : **gardée**, confiance 0,6.\n\n"
"**L3 — Désaccord hors du score méta (M9).** *Décision* : le désaccord d(a, b) reste hors du score du bras méta, rapporté par paire, ou y entre. "
"*Enjeu* : R-638 le place hors score ; la garde R5 ligne 24 le vérifie ; s'il entrait, sa place et son poids seraient dans l'annexe. *Options* : "
"hors score — avantage : conforme à R-638, score reproductible sans lecture de désaccord, garde 24 jouable ; inconvénient : le désaccord ne pèse "
"pas sur le choix de la paire. Dans le score — avantage : le profil pourrait préférer les paires qui se contredisent ; inconvénient : un poids à "
"inventer dans l'annexe, garde 24 à réécrire, une lecture de modèle (oui / non / indécidable) entre dans le score. *Recommandation* : **hors "
"score**, confiance 0,7.\n\n"
"**L4 — Total séquencé pour C10.** *Décision* : lire le reste de la course sur 110 USD (GO-2026-10-30-07 inchangé) ou sur 123 (la ligne nouvelle "
"de R-630 s'ajoute et laisse 78 à la course) ; fixé au gel, jamais lu sur une ligne de GO écrite après (CP5-03). *Enjeu* : C10 vaut 0,92 sous "
"110 et 0,98 sous 123 (sortie v6) ; la ligne de GO au plafond S17 n'existe pas encore (DEP6). *Options* : 110 — avantage : lecture prudente, rien "
"n'est supposé d'une ligne à écrire ; inconvénient : la course perd ce que le pré-pilote dépense au-delà de 32 (reste médian 73,7 ; tient à 4 "
"sous-sessions avec 0,07). 123 — avantage : C10 0,98, reste 78 ; inconvénient : suppose une ligne qui s'ajoute au lieu de se substituer, ce que "
"seul le mot de Lazar fixe. *Recommandation* : **110**, confiance 0,6.\n\n"
"**L5 — Fusions retirées par A1 et C12 (CP5-02).** *Décision* : si la règle d'A1 retire les fusions (rang 1 ; 0,13, 0,21 recommandée), C12 se "
"lit sur les paires et leurs gardes, avec réserve, ou C12 est « non mesurée (budget) » et C13 tombe. *Enjeu* : les trois paires et leurs gardes "
"existent sans dépense ; seule la chaîne après la paire (fusion, aiguilleur, juges) n'est pas éprouvée. *Options* : lue sur les paires — "
"avantage : un sacrifice de rang 1 n'est pas un nœud ; C12 inchangée ; réserve « chaîne éprouvée jusqu'à la paire seulement » et O15 (a) ouverte ; "
"inconvénient : la course peut partir sans qu'une fusion ait été jugée. Non mesurée — avantage : la chaîne entière est exigée avant la course ; "
"inconvénient : nœud avec 0,13 (0,21) de plus, par la première mesure que la règle sacrifie. *Recommandation* : **lue sur les paires**, "
"confiance 0,65.\n\n"
"**L6 — S27 lu comme réserve (R-635).** *Décision* : une couverture Gu-Krenn sous S27 (0,60) est une réserve, ou retire le bras. *Enjeu* : R-635 "
"recommande la réserve ; A19 dit « aucun retrait » ; un retrait serait une cause de bras non produit de plus dans C12. *Options* : réserve — "
"avantage : bras gardé, cohérent avec A19 et R-635 ; inconvénient : une paire choisie parmi peu de fiches notables dit surtout quelles fiches "
"emploient le vocabulaire. Retrait — avantage : aucune paire sur un vocabulaire mal couvert ; inconvénient : contredit A19, et C12 reçoit une "
"cause de bras non produit non chiffrée. *Recommandation* : **réserve**, confiance 0,6.\n\n"
"**L7 — Brouillon 3 sans contre-lecture.** *Décision* : accepter que le brouillon 3 n'ait pas reçu de contre-lecture (remplacé par le brouillon 4 "
"avant la contre-lecture 3), ou exiger une contre-lecture rétrospective. *Enjeu* : R2 veut chaque préenregistrement contre-lu ; le brouillon 3 est "
"un état intermédiaire gardé (R12) dont tous les changements sont dans la table du brouillon 4 ; les brouillons 4, 5 et 6 ont été contre-lus ou "
"vérifiés (contre-lectures 3 et 4, vérification VB6), et la version gelée recevra la contre-lecture 5. *Options* : accepté — avantage : rien à "
"attendre ; ce qui est gelé est contre-lu ; inconvénient : un brouillon de la chaîne n'a pas été relu. Rétrospective — avantage : R2 à la "
"lettre ; inconvénient : une relecture d'un texte remplacé, sans effet sur la version gelée. *Recommandation* : **accepté**, confiance 0,6.")
rep(L_OLD, L_NEW)

open(dst, "w", encoding="utf-8").write(t)
print("REMPLIR restants:", t.count("À REMPLIR"))
print("FOURNIR AU SCELLEMENT:", t.count(FOURNIR))
