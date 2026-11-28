# Application des constats des deux verifications courtes du brouillon 3 de P3b -> brouillon 4.
# Chaque changement : remplacement exact ; l'ancien texte doit apparaitre une seule fois, sinon arret.
# Lance par : PYTHONDONTWRITEBYTECODE=1 python3 -B -I appliquer_brouillon4_v1.py
import subprocess
import sys
from pathlib import Path

RACINE = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p3b")
B3 = RACINE / "brouillon3"
B4 = RACINE / "brouillon4"

SOURCES = {
    "T": (B3 / "P3b-seconde-lecture-v1-brouillon3.md", B4 / "P3b-seconde-lecture-v1-brouillon4.md"),
    "D": (B3 / "devis-P3b-v3.md", B4 / "devis-P3b-v4.md"),
    "P": (B3 / "plan-code-et-chaine-P3b-v3.md", B4 / "plan-code-et-chaine-P3b-v4.md"),
    "Q": (B3 / "questions-ouvertes-P3b-v3.md", B4 / "questions-ouvertes-P3b-v4.md"),
}

HEURE = subprocess.run(["date", "-u", "+%H:%M"], capture_output=True, text=True, check=True).stdout.strip()

E = []


def R(f, ident, old, new):
    E.append((f, ident, old, new))


# ================================================================ TEXTE : en-tete
R("T", "en-tete/auteur (brouillon 4)",
  "- Auteur : rédacteur neuf (Claude, sous-agent), **brouillon 3**, session 16, 2026-10-21, fichiers écrits de 01:20 à 01:32 UTC\n"
  "  environ (heure vraie, `date -u`). Je n'ai écrit ni les brouillons 1 et 2 de P3b (texte, devis, plan, questions), ni P3,\n"
  "  ses addenda ou ses verdicts, ni aucune contre-lecture, projet de traitement ou traitement. Consigne :\n"
  "  `…/p3b/consigne-redacteur-P3b-brouillon3-v1.md` (`599c6d8de34116ec00fb68ea5cf53999de0ab3b8ac5c6023c4b985a3a9fdb4a3`, égale à\n"
  "  son compagnon).",
  "- Auteur : rédacteur neuf (Claude, sous-agent), **brouillon 4**, session 16, 2026-10-21, fichiers écrits de 02:22 à "
  + HEURE + " UTC\n"
  "  environ (heure vraie, `date -u`). Je n'ai écrit ni les brouillons 1 à 3 de P3b (texte, devis, plan, questions, tables), ni\n"
  "  P3, ses addenda ou ses verdicts, ni aucune contre-lecture, vérification courte, projet de traitement ou traitement ; je\n"
  "  remplace un rédacteur du brouillon 4 coupé avant d'écrire, sans contact avec lui (aucun travail partiel trouvé). Consigne :\n"
  "  `…/p3b/consigne-redacteur-P3b-brouillon4-v1.md` (`1d4819921d764877ceedbc1b935933e5f777be61038f6ba0b5095098e2648ff3`, égale à\n"
  "  son compagnon).")

R("T", "en-tete/historique (brouillon 3, verifications courtes, table du brouillon 4)",
  "  l'endroit changé par le brouillon 3 est dans `table-traitement-brouillon3-v1.md` (même dossier).",
  "  l'endroit changé par le brouillon 3 est dans `…/p3b/brouillon3/table-traitement-brouillon3-v1.md`\n"
  "  (`89e67f7f1e5a201e70602499b80da477111f72a1940aca202b22fcfb32a54035`). Brouillon 3 : rédacteur neuf, consigne\n"
  "  `…/p3b/consigne-redacteur-P3b-brouillon3-v1.md` (`599c6d8d…`), fichiers écrits de 01:20 à 01:32 UTC environ le 2026-10-21\n"
  "  (`…/p3b/brouillon3/P3b-seconde-lecture-v1-brouillon3.md`,\n"
  "  `9430e359b2ec29694cf4b2032ce0f32591e0edf8d46e5a7db60ccb6680b37cb2`). Vérification courte du brouillon 3, une par lentille :\n"
  "  section « Contre-lecture » ; toutes ses remarques acceptées par la session (consigne du rédacteur du brouillon 4). Constat\n"
  "  par constat, l'endroit changé par le brouillon 4 est dans `table-traitement-brouillon4-v1.md` (même dossier).")

# VCP3b-texte-02 (1), fondu avec VCP3b-methode-08 (1)
R("T", "VCP3b-texte-02 (1a) regle du candidat : version retenue ecrite comme des remplacements",
  "ni ses guillemets. Issues des décisions",
  "ni ses guillemets ; une version\n"
  "  retenue écrite comme des remplacements (« devient », « à la place de », « est retiré », « remplacements mot pour mot ») ne\n"
  "  reste pas : elle s'applique mot pour mot au texte principal, après le retrait des marqueurs et des autres versions, puis\n"
  "  elle est retirée. Issues des décisions")
R("T", "VCP3b-texte-02 (1b) et (3) phrases retirees au candidat",
  "(la phrase « Au candidat, pour chaque décision marquée … ni ses guillemets. »,\n"
  "  celle-ci, et la dernière phrase de la puce « Partition »)",
  "(la phrase « Au candidat, pour chaque décision marquée … puis elle est retirée. »,\n"
  "  celle-ci, la dernière phrase de la puce « Partition », la phrase « Les choix de sonde de la version (A) … chacun avec un\n"
  "  renvoi à P-023. » et les trois renvois « (Version de repli (B) de P-023 … section « Périmètre ».) » de « Seuil », de la\n"
  "  table O et de la liste d'arrêt)")
R("T", "VCP3b-texte-01 (texte, statut) retours a la ligne",
  "le scellement refuse « en attente » et\n"
  "  « de repli », sans égard à la casse.",
  "le scellement refuse « en attente » et\n"
  "  « de repli », sans égard à la casse ni aux retours à la ligne.")

R("T", "renvoi plan v4 (en-tete)",
  "(plan : `plan-code-et-chaine-P3b-v3.md`)",
  "(plan : `plan-code-et-chaine-P3b-v4.md`)")
R("T", "renvoi devis v4 (GO de calcul)",
  "`devis-P3b-v3.md` (borne de l'étape",
  "`devis-P3b-v4.md` (borne de l'étape")
R("T", "VCP3b-methode-08 (hors lentille) empreinte actuelle du registre des decisions",
  "lignes N-026, R-258, R-272, R-278, R-289, R-295, N-030, en plus) ;",
  "lignes N-026, R-258, R-272, R-278, R-289, R-295, N-030, en plus) ; empreinte relevée le\n"
  "  2026-10-21 vers 01:40 UTC par la vérification courte « méthode » du brouillon 3 :\n"
  "  `6005137f16a88c9098564902d7264977d14975706aab020456c02e921da2da82` (registre vivant : lignes à relire au candidat) ;")

# ================================================================ TEXTE : perimetre
R("T", "VCP3b-texte-05 repli (C') de P-017",
  "P3b garde la version (A). »",
  "P3b lit N-028 et la double comptabilité, rien d'autre ; la sonde de valeur, le rejeu\n"
  "  contrefactuel et la manipulation du nombre écrit restent hors périmètre de P3b (tableau ci-dessous). »")

# Repli (B) de P-023
R("T", "VCP3b-methode-02 et VCP3b-texte-09 (repli (B), clause de G6 ; forme de texte-09, sans double blanc)",
  "dans G6, « ; T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit\n"
  "    (recouvrement insuffisant) » » est retiré",
  "dans G6, « sinon T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit\n"
  "    (recouvrement insuffisant) » ; » est retiré")
R("T", "VCP3b-methode-01 (repli (B) : H-P3b-2, G5, O7 avant le renommage) ; fondu avec VCP3b-texte-04 (3)",
  "R-295) » est retirée ; puis la puce « T4 de P3 (descriptif) »",
  "R-295) » est retirée ; dans H-P3b-2, « ni au nombre écrit, à la tâche ou aux coûts déjà déclarés (T4 résiduel) »\n"
  "    devient « ni au nombre écrit (T4 de P3 ; tâche et coûts déjà déclarés non contrôlés) » ; dans G5, « du nombre écrit, de\n"
  "    la tâche et des coûts déjà déclarés (au sens de ces tests) » devient « et du nombre écrit (au sens de ces tests ; tâche et\n"
  "    coûts déjà déclarés non contrôlés) » ; dans O7, « ni au nombre écrit, ni à la tâche ou aux coûts déjà déclarés, au sens\n"
  "    de ces tests » devient « ni au nombre écrit, au sens de ces tests (tâche et coûts déjà déclarés non contrôlés) » ; puis la\n"
  "    puce « T4 de P3 (descriptif) »")
R("T", "VCP3b-texte-04 (repli (B) : renommage etendu, P3b-P5, motifs) ; fondu avec VCP3b-methode-01",
  "; dans H-P3b-1, H-P3b-2, P3b-P2, P3b-P5,\n"
  "    « Famille principale » et les tables G, O et Synthèse, « T4 résiduel » devient « T4 de P3 » ;",
  "; dans H-P3b-1, H-P3b-2, P3b-P2, P3b-P5,\n"
  "    « Famille principale », le point 3 du « Plan d'analyse », la phrase « leur contrôle est T4 résiduel » de l'audit R4 et\n"
  "    les tables G, O et Synthèse, « T4 résiduel » devient « T4 de P3 » ; dans P3b-P5, « aire du résidu de l'oracle au-dessus\n"
  "    de son plancher » devient « aire de l'oracle stratifiée par quintiles du coût déclaré (T4 de P3) au-dessus de son\n"
  "    plancher » ; partout, dans cet ordre : « non séparé du nombre écrit, de la tâche ou de l'historique des coûts » devient\n"
  "    « non séparé du nombre écrit » ; « non séparé du nombre écrit, de la tâche ou de l'historique » devient « non séparé du\n"
  "    nombre écrit » ; dans P3b-P5, « non séparé du nombre, de la tâche ou de l'historique » devient « non séparé du nombre\n"
  "    écrit » ;")

# Replis de N-031
R("T", "VCP3b-texte-02 (2a) phrase de suite des replis de N-031 etiquetee",
  "En (b) ou en (c), dans la ligne G5",
  "Versions de repli (b) et (c) de N-031, suite : dans la ligne G5")
R("T", "VCP3b-texte-06 ecart (iv) en (b) et en (c), motif",
  "L'écart (iv) devient « (iv) tentative de détection déclarée non aveugle (N-031), aucune règle pour G0\n"
  "  (l. 157) »",
  "L'écart (iv) devient, en (b), « (iv) tentative de détection déclarée non aveugle (N-031), aucune\n"
  "  règle pour G0 (l. 157 ; motif : les bras localisés relisent un champ déjà lu par T2 et par l'addendum 1, sur des données\n"
  "  déjà lues) » et, en (c), « (iv) sondes génériques sur W en tentative de détection déclarée non aveugle, oracle et double\n"
  "  comptabilité en diagnostic (N-031), aucune règle pour G0 (l. 157 ; même motif) »")

# ================================================================ TEXTE : exposition
R("T", "exposition : declaration du brouillon 3 gardee",
  "  - Rédacteur du brouillon 3 (moi) : je n'ai lu",
  "  - Rédacteur du brouillon 3 (sa déclaration, gardée, à la première personne) : je n'ai lu")
R("T", "exposition : declaration du redacteur du brouillon 4",
  "  - La session qui traite les contre-lectures et écrit le candidat",
  "  - Rédacteur du brouillon 4 (moi) : je n'ai lu ni la contre-lecture « méthode » brute du brouillon 1, ni l'addendum 1 ou 2\n"
  "    de P3, ni la ligne R-303, ni le verdict complété de P3, ni le préenregistrement de P3, ni ses consignes, ni aucun\n"
  "    registre, ni aucun texte d'action, ni rien sous `donnees/`, `diag/`, `runs/`, `traces/`. J'ai lu le brouillon 3 (texte,\n"
  "    devis, plan, questions, table, sortie de `problemes`, début et fin du script de remplacements et de son journal), les\n"
  "    consignes des rédacteurs des brouillons 2 et 4 et les deux rapports de vérification courte du brouillon 3 ; ces\n"
  "    rapports ne recopient aucune grandeur de P3, leurs essais portent sur des données inventées. Le validateur\n"
  "    `src/controle_ia/prereg.py` a été exécuté (empreinte vérifiée), non lu. J'ai vu, par le brouillon 3, l'issue qualitative\n"
  "    du verdict complété (GO-2026-10-20-12) et la mention de l'aire du coût écrit seul, sans sa valeur ; par le rapport\n"
  "    « méthode », l'empreinte actuelle de `registres/decisions.md`, sans son contenu. Je n'ai vu ni le signe de P3-P2, ni\n"
  "    aucune valeur de T1 à T4 de P3, ni aucune aire de P3-P3. Ce texte ne recopie aucune grandeur observée de P3. Mes a\n"
  "    priori sont ceux du brouillon 3 : le brouillon 4 ne change aucune probabilité.\n"
  "  - La session qui traite les contre-lectures et écrit le candidat")

# ================================================================ TEXTE : prediction
R("T", "VCP3b-methode-07 (P3b-P8, D2b nommee)",
  "D2, D4b ou « non tranché » ≈ 50 %",
  "D2, D2b, D4b ou « non tranché » ≈ 50 %")

# ================================================================ TEXTE : metrique
R("T", "VCP3b-texte-03 (1) plis de T4 residuel des sondes generiques, version (B) de P-016",
  "(sondes génériques : `plis/lecture-60` ; oracle",
  "(sondes génériques : `plis/lecture-60`, Version de repli (B) de P-016 :\n"
  "  `plis/lecture-40` ; oracle")
R("T", "VCP3b-methode-04 (T4 residuel, reference vide)",
  "une action de l'honnête\n"
  "  sans autre action lisible de l'honnête dans sa tâche est exclue de la lecture concernée",
  "une action sans action lisible\n"
  "  de l'honnête dans sa tâche à laquelle se rapporter (pour une action de l'honnête : sans autre action lisible de\n"
  "  l'honnête) est exclue de la lecture concernée")
R("T", "VCP3b-methode-05 (seconde specification, decile de reference)",
  "(bornes : déciles de c_w − h_t sur les actions d'ajustement du pli),",
  "(bornes : déciles de c_w − h_t sur les actions d'ajustement du pli), premier décile omis (référence),")
R("T", "VCP3b-methode-04 (H_t, reference vide)",
  "une action de\n"
  "    l'honnête sans autre action lisible de l'honnête dans sa tâche est exclue de la lecture concernée",
  "une action sans action lisible\n"
  "    de l'honnête dans sa tâche à laquelle se rapporter (pour une action de l'honnête : sans autre action lisible de\n"
  "    l'honnête) est exclue de la lecture concernée")
R("T", "VCP3b-methode-07 (plancher par rotation, items (vi))",
  "pour les items (v), les 200 items (v))",
  "pour les items (v), les 200 items (v) ; pour les items (vi), les 200 items (vi))")
R("T", "VCP3b-methode-03 (CP-L, artefact (iv) par bande)",
  "fixé par graine), ne passe **pas** (iii).",
  "fixé par graine), ne passe (iii) dans **aucune** bande.")
R("T", "VCP3b-methode-06 (items (vi), leurres hors du contexte)",
  "leurres de même règle pour H = A + B",
  "leurres de même règle pour H = A + B, tirés parmi les candidats dont le premier\n"
  "  identifiant ne figure pas parmi les identifiants du contexte")

# ================================================================ TEXTE : plan d'analyse
R("T", "VCP3b-texte-03 (2) plan d'analyse, point 1 : cles des plis, version (B) de P-016 a la place",
  "la confirmation.\n"
  "   Version de repli (B) de P-016 : « 20, 20, puis 20 réservées ; plis `plis/confirmation` 5 × 4, l'oracle du pli k apprenant\n"
  "   sur la découverte et 16 tâches de confirmation ; plis `plis/lecture-40` 5 × 8. » Plis : clés `plis/decouverte` (5 × 4),\n"
  "   `plis/confirmation` (5 × 8) et `plis/lecture-60` (5 × 12).",
  "la confirmation. Plis : clés\n"
  "   `plis/decouverte` (5 × 4), `plis/confirmation` (5 × 8) et `plis/lecture-60` (5 × 12). Version de repli (B) de P-016, à la\n"
  "   place du texte qui précède depuis « les 20 premiers » : « les 20 premiers forment la découverte, les 20 suivants la\n"
  "   confirmation, les 20 derniers sont réservés. Plis : clés `plis/decouverte` (5 × 4), `plis/confirmation` (5 × 4 ;\n"
  "   l'oracle du pli k apprend sur la découverte et 16 tâches de confirmation) et `plis/lecture-40` (5 × 8). »")
R("T", "renvoi devis v4 (plan d'analyse, point 5)",
  "Détail : `devis-P3b-v3.md`.",
  "Détail : `devis-P3b-v4.md`.")

# ================================================================ TEXTE : criteres de lecture
R("T", "VCP3b-texte-09 (G6, issue : non etabli ou non calculable)",
  "| G6 : retenue, P3-P4 conforme, l'un de T1, T3, T4 résiduel non établi |",
  "| G6 : retenue, P3-P4 conforme, l'un de T1, T3, T4 résiduel non établi ou non calculable |")
R("T", "VCP3b-methode-02 (G6, branche recouvrement avant la branche generique) ; fondu avec VCP3b-texte-09",
  "; sinon T4 résiduel non établi → « non séparé du nombre écrit, de la tâche ou de l'historique à cette puissance » ; "
  "T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit (recouvrement insuffisant) »",
  "; sinon T4 résiduel non calculable (recouvrement) → « le plan ne sépare pas le score du nombre écrit (recouvrement "
  "insuffisant) » ; sinon T4 résiduel non établi ou non calculable → « non séparé du nombre écrit, de la tâche ou de "
  "l'historique à cette puissance »")

# ================================================================ TEXTE : chaine de lancement
R("T", "renvoi plan v4 (chaine de lancement)",
  "Plan détaillé : `plan-code-et-chaine-P3b-v3.md`.",
  "Plan détaillé : `plan-code-et-chaine-P3b-v4.md`.")
R("T", "VCP3b-texte-07 (ordre, repli (A) de N-032 apres les reponses de Lazar)",
  "« mesure de conception M-P3b-1 (puissance) ; mesure M-P3b-2 avant le scellement (par condition, règle de P3b-P0, sortie\n"
  "  brute scellée) ; » à la place de « mesure de conception M-P3b-1 (puissance) ; »",
  "« N-032 sans réponse vaut (C)) ; mesure M-P3b-2 avant le scellement (par condition, règle de P3b-P0, sortie\n"
  "  brute scellée) ; » à la place de « N-032 sans réponse vaut (C)) ; »")
R("T", "VCP3b-texte-02 (2b) phrase de suite du repli (C) de P-024 etiquetee",
  "En (C), à l'étape 2.6,",
  "Version de repli (C) de P-024, suite : à l'étape 2.6,")

# ================================================================ TEXTE : contre-lecture
R("T", "attribution : contre-lecture methode brute du brouillon 1 non lue (brouillons 2 a 4)",
  "rapport non lu par les rédacteurs des brouillons 2 et 3)",
  "rapport non lu par les rédacteurs des brouillons 2 à 4)")
R("T", "renvoi a la table du brouillon 3 (Contre-lecture 3)",
  "12 constats traités (table `table-traitement-brouillon3-v1.md`).",
  "12 constats traités (table `…/p3b/brouillon3/table-traitement-brouillon3-v1.md`).")
R("T", "Contre-lecture 5 et 6 remplies (verifications courtes), 7 a remplir",
  "- **Contre-lecture 5** (ce brouillon 3) : À REMPLIR — vérification courte des corrections par deux sous-agents neufs, une\n"
  "  par lentille (traitement du brouillon 2, décision 6) : empreinte du brouillon 3 relu, chemin et empreinte de chaque\n"
  "  rapport, exposition de chaque contre-lecteur, traitement de chaque remarque.",
  "- **Contre-lecture 5** (brouillon 3, vérification courte, lentille « méthode ») : sous-agent neuf ; brouillon relu\n"
  "  `9430e359b2ec29694cf4b2032ce0f32591e0edf8d46e5a7db60ccb6680b37cb2` ; rapport\n"
  "  `…/p3b/verification-courte-brouillon3/methode/verification-courte-P3b-brouillon3-methode-v1.md`\n"
  "  (`66165ba5298781959097b704a534f9be1027cf2978d5fe381127f799e4bf27ec`, « scellable après corrections », 1 majeur, 5 mineurs,\n"
  "  1 de forme, 1 information, dont 3 bloquants ; exposition déclarée dans le rapport, aucune grandeur de P3 recopiée).\n"
  "  Traitement de la session (consigne du rédacteur du brouillon 4, `1d481992…`) : toutes les remarques acceptées ;\n"
  "  8 constats traités (table `table-traitement-brouillon4-v1.md`).\n"
  "- **Contre-lecture 6** (brouillon 3, vérification courte, lentille « texte ») : sous-agent neuf ; brouillon relu\n"
  "  `9430e359b2ec29694cf4b2032ce0f32591e0edf8d46e5a7db60ccb6680b37cb2` ; rapport\n"
  "  `…/p3b/verification-courte-brouillon3/texte/verification-courte-P3b-brouillon3-texte-v1.md`\n"
  "  (`2c77870f2eb16aaf3af3c9ad2c6b2db892788c7606cb56487cc58f4451bf412d`, « scellable après corrections », 4 bloquants,\n"
  "  5 mineurs ; exposition déclarée dans le rapport, aucune grandeur de P3 recopiée, aucune ligne de `registres/` ouverte).\n"
  "  Même traitement ; 9 constats traités.\n"
  "- **Contre-lecture 7** (ce brouillon 4, puis le candidat) : À REMPLIR — vérification des corrections du brouillon 4 si la\n"
  "  session la demande, puis relecture courte du candidat par un sous-agent neuf (« Chaîne de lancement », Ordre) :\n"
  "  empreinte relue, chemin et empreinte de chaque rapport, exposition de chaque contre-lecteur, traitement de chaque\n"
  "  remarque.")

# ================================================================ DEVIS
R("D", "VCP3b-texte-08 titre du devis (v4)",
  "# Devis de P3b (passe sur carte de la seconde lecture de P3) — v2",
  "# Devis de P3b (passe sur carte de la seconde lecture de P3) — v4")
R("D", "en-tete du devis (brouillon 4)",
  "- Rédacteur neuf (Claude, sous-agent), brouillon 3, session 16, 2026-10-21 vers 01:32 UTC (heure vraie). Joint à\n"
  "  `P3b-seconde-lecture-v1-brouillon3.md` (même dossier). Remplace pour la suite la v2 (`…/p3b/brouillon2/devis-P3b-v2.md`,\n"
  "  `7dd3cfeeb25a7fbe27ac4f59098e4de3a14665a6d388e6d0ec994424ef1ddc78`, écrite vers 00:52 UTC le 2026-10-21), gardée telle\n"
  "  quelle (R12), qui remplaçait la v1 (`…/p3b/brouillon1/devis-P3b-v1.md`, `77e46dc3…`). Changements du brouillon 3 :\n"
  "  CR2-P3b-texte-07, -08 et -12, CR2-P3b-methode-04 et -06 (table `table-traitement-brouillon3-v1.md`).",
  "- Rédacteur neuf (Claude, sous-agent), brouillon 4, session 16, 2026-10-21 vers " + HEURE + " UTC (heure vraie). Joint à\n"
  "  `P3b-seconde-lecture-v1-brouillon4.md` (même dossier). Remplace pour la suite la v3 (`…/p3b/brouillon3/devis-P3b-v3.md`,\n"
  "  `3dc920f8a3264e508e40b66d563f87fbe6c045973247bd1912e6d31bfd87a1ad`, écrite vers 01:32 UTC le 2026-10-21, titrée « — v2 »\n"
  "  par erreur), gardée telle quelle (R12), qui remplaçait la v2 (`…/p3b/brouillon2/devis-P3b-v2.md`, `7dd3cfee…`) et la v1\n"
  "  (`…/p3b/brouillon1/devis-P3b-v1.md`, `77e46dc3…`). Changements du brouillon 4 : titre et en-tête seulement\n"
  "  (VCP3b-texte-08 ; table `table-traitement-brouillon4-v1.md`) ; aucun montant ni aucune durée ne change.")

# ================================================================ PLAN
R("P", "VCP3b-texte-08 titre du plan (v4)",
  "# Plan du code et de la chaîne de P3b — v2",
  "# Plan du code et de la chaîne de P3b — v4")
R("P", "en-tete du plan (brouillon 4)",
  "- Rédacteur neuf (Claude, sous-agent), brouillon 3, session 16, 2026-10-21 vers 01:32 UTC (heure vraie). Joint à\n"
  "  `P3b-seconde-lecture-v1-brouillon3.md` (même dossier). Remplace pour la suite la v2\n"
  "  (`…/p3b/brouillon2/plan-code-et-chaine-P3b-v2.md`, `fd82f2f6bd70c7e3feab0e694f6e57d5b74bec6a95e76a4691e4436ba3558043`,\n"
  "  écrite vers 00:53 UTC le 2026-10-21), gardée telle quelle (R12), qui remplaçait la v1\n"
  "  (`…/p3b/brouillon1/plan-code-et-chaine-P3b-v1.md`, `bd770815…`). Changements du brouillon 3 : table\n"
  "  `table-traitement-brouillon3-v1.md`.",
  "- Rédacteur neuf (Claude, sous-agent), brouillon 4, session 16, 2026-10-21 vers " + HEURE + " UTC (heure vraie). Joint à\n"
  "  `P3b-seconde-lecture-v1-brouillon4.md` (même dossier). Remplace pour la suite la v3\n"
  "  (`…/p3b/brouillon3/plan-code-et-chaine-P3b-v3.md`, `d950e428b543b642cfeb1631e7bb275e8fa33ed673cc6d41befef26cb9622c30`,\n"
  "  écrite vers 01:32 UTC le 2026-10-21, titrée « — v2 » par erreur), gardée telle quelle (R12), qui remplaçait la v2\n"
  "  (`…/p3b/brouillon2/plan-code-et-chaine-P3b-v2.md`, `fd82f2f6…`) et la v1 (`…/p3b/brouillon1/plan-code-et-chaine-P3b-v1.md`,\n"
  "  `bd770815…`). Changements du brouillon 4 : table `table-traitement-brouillon4-v1.md`.")
R("P", "VCP3b-texte-03 (consequence) partition : confirmation 5 x 4 en (B)",
  "plis de découverte (5 × 4), de confirmation (5 × 8) et de lecture",
  "plis de découverte (5 × 4), de confirmation (5 × 8 ; en (B) 5 × 4) et de lecture")
R("P", "VCP3b-methode-04 (consequence) residuel : reference vide pour toute action",
  "action de l'honnête sans autre action lisible de l'honnête dans sa tâche : exclue, motif « référence vide »)",
  "action sans action lisible de l'honnête dans sa tâche à laquelle se rapporter (pour une action de l'honnête : sans autre "
  "action lisible de l'honnête) : exclue, motif « référence vide »)")
R("P", "VCP3b-texte-03 (consequence) residuel : plis de lecture en (B)",
  "plis `plis/lecture-60` (sondes génériques)",
  "plis `plis/lecture-60` (sondes génériques ; Version de repli (B) de P-016 : `plis/lecture-40`)")
R("P", "VCP3b-methode-05 (consequence) residuel : premier decile omis",
  "indicatrices des déciles de c_w − h_t, bornes sur les actions d'ajustement du pli)",
  "indicatrices des déciles de c_w − h_t, bornes sur les actions d'ajustement du pli, premier décile omis (référence))")
R("P", "VCP3b-methode-04 (consequence) residuel : covariables manquantes hors reference vide",
  "covariables manquantes → « non calculable »",
  "covariables manquantes (hors « référence vide ») → « non calculable »")
R("P", "VCP3b-methode-05 (consequence) test : seconde specification de plein rang",
  "lecteur planté de e · (m − h_t) → aire du résidu ≈ 0,5 ;",
  "lecteur planté de e · (m − h_t) → aire du résidu ≈ 0,5 ; seconde spécification de plein rang, premier décile omis "
  "(artefact : dix indicatrices plus la constante → colinéarité détectée, arrêt) ;")
R("P", "VCP3b-methode-04 (consequence) test : reference vide hors de l'honnete",
  "action de l'honnête seule lisible de sa tâche → exclue, motif « référence vide »",
  "action de l'honnête seule lisible de sa tâche → exclue, motif « référence vide » ; action du saboteur d'une tâche sans "
  "action lisible de l'honnête → exclue, motif « référence vide », le reste du bras lu (jamais « non calculable » pour tout "
  "le bras)")
R("P", "VCP3b-methode-04 (consequence) lentille : reference vide",
  "exclusions (pas de leurre, τ_h = τ_d chez l'honnête, H_t ou leurre au-dessus de 999)",
  "exclusions (pas de leurre, τ_h = τ_d chez l'honnête, H_t ou leurre au-dessus de 999, « référence vide » selon la règle "
  "du texte)")
R("P", "VCP3b-methode-03 (plan, test de l'artefact (iv))",
  "artefact (états d'autres items) : ne passe pas",
  "artefact (états d'autres items) : ne passe (iii) dans aucune bande")
R("P", "VCP3b-methode-06 (consequence) test des leurres des items (vi)",
  "items (vi) : valeur absente du contexte (artefact : τ(A + B) dans le contexte → item refusé) ;",
  "items (vi) : valeur absente du contexte (artefact : τ(A + B) dans le contexte → item refusé) ; leurres des items (vi) "
  "tirés parmi les candidats dont le premier identifiant ne figure pas parmi les identifiants du contexte (artefact : "
  "leurre de premier identifiant τ(A) → candidat écarté) ;")
R("P", "VCP3b-methode-02 et VCP3b-texte-09 (consequence) lignes atteintes : G6 recouvrement et effectifs",
  "G6 et O5 avec T4 résiduel non établi (spécification) ;",
  "G6 et O5 avec T4 résiduel non établi (spécification) ; G6 avec T4 résiduel non calculable (recouvrement) → motif "
  "« recouvrement insuffisant », et non calculable faute d'effectifs → motif « à cette puissance » ;")
R("P", "VCP3b-texte-01 (plan, sceller) chaines coupees par un retour a la ligne",
  "**refuse tout texte qui contient « en attente », « de repli » ou « Proposition en attente », sans égard à la casse** "
  "(cas sain : candidat sans ces chaînes ; artefacts : chacune, au singulier et au pluriel)",
  "**refuse tout texte qui contient « en attente », « de repli » ou « Proposition en attente », sans égard à la casse "
  "ni aux blancs (toute suite d'espaces et de retours à la ligne lue comme une espace)** (cas sain : candidat sans ces "
  "chaînes ; artefacts : chacune, au singulier et au pluriel, et chacune coupée par un retour à la ligne suivi d'espaces)")
R("P", "VCP3b-texte-07 (plan, section 4, repli (A) de N-032 apres les reponses de Lazar)",
  "« mesure de conception M-P3b-1 (puissance) ; mesure M-P3b-2 avant le scellement (par\n"
  "condition, règle de P3b-P0, sortie brute scellée) ; » à la place de « mesure de conception M-P3b-1 (puissance) ; »",
  "« N-032 sans réponse vaut (C)) ; mesure M-P3b-2 avant le scellement (par\n"
  "condition, règle de P3b-P0, sortie brute scellée) ; » à la place de « N-032 sans réponse vaut (C)) ; »")

# ================================================================ QUESTIONS
R("Q", "VCP3b-texte-08 titre des questions (brouillon 4, v4)",
  "# Questions ouvertes de P3b, brouillon 2 — v2",
  "# Questions ouvertes de P3b, brouillon 4 — v4")
R("Q", "en-tete des questions (brouillon 4)",
  "Rédacteur neuf du brouillon 3 (Claude, sous-agent), session 16, 2026-10-21 vers 01:32 UTC (heure vraie). Remplace pour\n"
  "la suite la v2 (`…/p3b/brouillon2/questions-ouvertes-P3b-v2.md`,\n"
  "`417a111e688fd412db4fb49675b54254d874ae392f08f3c3725a0a0494764757`, écrite vers 00:54 UTC le 2026-10-21), gardée telle\n"
  "quelle (R12), qui remplaçait la v1 (`…/p3b/brouillon1/questions-ouvertes-P3b-v1.md`, `046991ab…`). Ajouts du brouillon 3\n"
  "marqués « (brouillon 3) », d'après les contre-lectures R2 du brouillon 2 et leur traitement\n"
  "(`…/p3b/traitement-contre-lectures-brouillon2-P3b-v1.md`, `958b4601…`).",
  "Rédacteur neuf du brouillon 4 (Claude, sous-agent), session 16, 2026-10-21 vers " + HEURE + " UTC (heure vraie). Remplace pour\n"
  "la suite la v3 (`…/p3b/brouillon3/questions-ouvertes-P3b-v3.md`,\n"
  "`aff0a7edf7713b214a5f64fea66ece509173480cd55c83ae30cf2d7cf13e97c3`, écrite vers 01:32 UTC le 2026-10-21, titrée\n"
  "« brouillon 2 — v2 » par erreur), gardée telle quelle (R12), qui remplaçait la v2\n"
  "(`…/p3b/brouillon2/questions-ouvertes-P3b-v2.md`, `417a111e…`) et la v1 (`…/p3b/brouillon1/questions-ouvertes-P3b-v1.md`,\n"
  "`046991ab…`). Ajouts du brouillon 3 marqués « (brouillon 3) », d'après les contre-lectures R2 du brouillon 2 et leur\n"
  "traitement (`…/p3b/traitement-contre-lectures-brouillon2-P3b-v1.md`, `958b4601…`). Ajouts du brouillon 4 marqués\n"
  "« (brouillon 4) », d'après les deux vérifications courtes du brouillon 3 (« méthode » `66165ba5…`, « texte »\n"
  "`2c77870f…`), toutes leurs remarques acceptées par la session.")
R("Q", "renvois des questions (brouillon 4, v4)",
  "`P3b-seconde-lecture-v1-brouillon3.md` (texte), `devis-P3b-v3.md`, `plan-code-et-chaine-P3b-v3.md`.",
  "`P3b-seconde-lecture-v1-brouillon4.md` (texte), `devis-P3b-v4.md`, `plan-code-et-chaine-P3b-v4.md`.")
R("Q", "Q-01 (VCP3b-texte-06, VCP3b-texte-02)",
  "réserve « tentative non aveugle », troisième ligne de la synthèse (CR2-P3b-texte-06).",
  "réserve « tentative non aveugle », troisième ligne de la synthèse (CR2-P3b-texte-06). (brouillon 4) Écart (iv) distinct en\n"
  "  (b) et en (c), avec son motif ; phrase qui suit les replis étiquetée « Versions de repli (b) et (c) de N-031, suite »\n"
  "  (VCP3b-texte-06, VCP3b-texte-02).")
R("Q", "Q-02 (VCP3b-texte-03)",
  "`<<PARTITION_P016>>` se remplit au candidat par le seul texte retenu (CR-P3b-texte-15).",
  "`<<PARTITION_P016>>` se remplit au candidat par le seul texte retenu (CR-P3b-texte-15). (brouillon 4) Version (B)\n"
  "  complétée : plis de T4 résiduel des sondes génériques (`plis/lecture-40`) et clés des plis du point 1 du plan d'analyse,\n"
  "  écrites à la place du texte de la version (A) (VCP3b-texte-03).")
R("Q", "Q-03 (VCP3b-texte-07)",
  "et l'ordre de la chaîne portent les versions (A) et (B) en mots exacts (CR2-P3b-texte-07).",
  "et l'ordre de la chaîne portent les versions (A) et (B) en mots exacts (CR2-P3b-texte-07). (brouillon 4) Dans l'ordre de\n"
  "  la chaîne, M-P3b-2 en (A) ou en (B) se place après les réponses de Lazar (VCP3b-texte-07).")
R("Q", "Q-19 (VCP3b-methode-06, VCP3b-methode-03)",
  "qui éprouvent la branche stricte de D3 (CR2-P3b-methode-04).",
  "qui éprouvent la branche stricte de D3 (CR2-P3b-methode-04). (brouillon 4) Leurres des items (vi) tirés hors\n"
  "  des identifiants du contexte (VCP3b-methode-06) ; l'artefact (iv) ne doit passer (iii) dans aucune bande\n"
  "  (VCP3b-methode-03).")
R("Q", "Q-21 (VCP3b-texte-02)",
  "exception écrite à l'étape 2.6, à la liste d'arrêt et au contrôle des fichiers (CR2-P3b-texte-08).",
  "exception écrite à l'étape 2.6, à la liste d'arrêt et au contrôle des fichiers (CR2-P3b-texte-08). (brouillon 4) La\n"
  "  phrase de l'étape 2.6 est étiquetée « Version de repli (C) de P-024, suite » (VCP3b-texte-02).")
R("Q", "Q-23 (VCP3b-texte-01, -02, VCP3b-methode-08)",
  "option retenue, réponse de Lazar ou défaut échu, date, ligne du registre (CR2-P3b-texte-04).",
  "option retenue, réponse de Lazar ou défaut échu, date, ligne du registre (CR2-P3b-texte-04). (brouillon 4) Une\n"
  "  version retenue écrite comme des remplacements s'applique au texte principal, après le retrait des marqueurs et des\n"
  "  autres versions, puis elle est retirée ; la garde du scellement ne tient compte ni de la casse ni des blancs\n"
  "  (VCP3b-texte-01, VCP3b-texte-02, VCP3b-methode-08). L'empreinte de `registres/decisions.md` a changé depuis la lecture\n"
  "  du brouillon 2 (`6005137f…`, relevée par la vérification courte « méthode ») : lignes à relire au candidat.")
R("Q", "Q-25 (VCP3b-texte-05)",
  "  écrite ici).",
  "  écrite ici). (brouillon 4) En (C′), le repli écrit en entier la phrase de la version (A) qu'il garde (VCP3b-texte-05).")
R("Q", "Q-26 (VCP3b-methode-01, -02, -08, VCP3b-texte-04)",
  "confirmer par Lazar avec l'option (CR2-P3b-texte-05).",
  "confirmer par Lazar avec l'option (CR2-P3b-texte-05). (brouillon 4) En (B), T4 de P3 ne contrôle que le nombre écrit :\n"
  "  H-P3b-2, G5 et O7 le disent (« tâche et coûts déjà déclarés non contrôlés ») ; P3b-P5 lit l'aire stratifiée de l'oracle ;\n"
  "  les motifs de G6, O5 et P3b-P5 ne nomment que le nombre écrit ; G6 garde la branche « recouvrement » avant la branche\n"
  "  générique (VCP3b-methode-01, VCP3b-methode-02, VCP3b-texte-04). Les a priori de P3b-P2 et P3b-P5 (« recouvrement\n"
  "  faible ») restent : non bloquants (VCP3b-methode-08).")
R("Q", "Q-28 (VCP3b-methode-04)",
  "« référence vide » pour une action de l'honnête seule lisible de sa tâche (CR2-P3b-methode-05).",
  "« référence vide » pour une action de l'honnête seule lisible de sa tâche (CR2-P3b-methode-05). (brouillon 4) La règle\n"
  "  couvre toute action sans action lisible de l'honnête dans sa tâche à laquelle se rapporter (VCP3b-methode-04).")


def main():
    textes = {k: src.read_text(encoding="utf-8") for k, (src, _) in SOURCES.items()}
    journal = []
    for f, ident, old, new in E:
        n = textes[f].count(old)
        if n != 1:
            print(f"ARRET : {f} / {ident} : ancien texte trouvé {n} fois", file=sys.stderr)
            sys.exit(2)
        textes[f] = textes[f].replace(old, new, 1)
        journal.append(f"{f}\t{ident}")
    for k, (_, dst) in SOURCES.items():
        if dst.exists():
            print(f"ARRET : {dst} existe déjà (R12, on n'écrase jamais)", file=sys.stderr)
            sys.exit(3)
    if len(sys.argv) > 1 and sys.argv[1] == "--essai":
        print(f"essai : {len(E)} remplacements trouvés une seule fois chacun ; rien n'est écrit")
        return
    for k, (_, dst) in SOURCES.items():
        dst.write_text(textes[k], encoding="utf-8")
    (B4 / "travail" / "journal-remplacements-v1.txt").write_text(
        f"heure UTC {HEURE} ; {len(E)} remplacements, chacun trouvé une seule fois\n" + "\n".join(journal) + "\n",
        encoding="utf-8")
    print(f"{len(E)} remplacements appliqués ; heure {HEURE}")


if __name__ == "__main__":
    main()
