"""Construit la version r1 (cases du directeur remplies) à partir de la version c2 (7a8d57c8…).

Source des décisions : registres/go.md de origin/main, ligne GO-2026-11-19-53 (R-3802), relue par le rédacteur.
Remplacements exacts (ancre unique, sinon arrêt). Les options retenues sont recopiées de la version c2 ; les branches
écartées sont retirées. Garde finale : plus aucun « À REMPLIR » hors de la section « Contre-lecture ».
"""
import hashlib
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from construire_brouillon6_relance_v1 import appliquer  # noqa: E402

C2 = ICI.parent / "papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c2.md"
SHA_C2 = "7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61"
SORTIE = ICI.parent / "papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-r1.md"
JOURNAL = ICI / "construire_brouillon6_relance_r1_v1.journal.tsv"
GO = "GO-2026-11-19-53"

Z = []


def z(id, d, section, resume, *op):
    Z.append(dict(id=id, d=d, section=section, resume=resume, op=op))


# ------------------------------------------------------------------ en-tête
z("R-00a", "—", "titre", "titre : version r1",
  "rep", "brouillon 6 de relance (2026-11-19), version c2",
  "brouillon 6 de relance (2026-11-19), version r1 (cases du directeur remplies)")

z("R-00b", "D-1 à D-17", "en-tête, « ce que change »", "paragraphe « Ce que change la version r1 »",
  "rep", "**Ce qu'avait changé le brouillon 5** (rappel ;",
  "**Ce que change la version r1.** Les dix-sept décisions du directeur sont tranchées (`registres/go.md`, ligne\n"
  + GO + ", mot de Lazar du 2026-11-19 à 12:38:35Z ; `registres/decisions.md`, R-3802 ; lues sur `origin/main`, commit\n"
  "`784cfcd4`) : D-1 (b), poids 0,5 ; D-2 (a), trois niveaux ; D-3 (a) ; D-4 (a) ; D-5 (a) ; D-6 (a) ; D-7 (a) ; D-8 (a),\n"
  "masque accepté ; D-9 (a) sous réserve du rapport de la grille entière et de la ligne C-P3c, sinon (b) ; D-10 à D-14\n"
  "(a) ; D-15 (i) et (n) ; D-16 (a) ; D-17 (a). Les sept cases sont remplies par recopie de l'option retenue ; les\n"
  "branches écartées sont retirées et restent lisibles dans la version c2\n"
  "(`7a8d57c8c8c9a3c3aa77c708e7d4aab46d0c19e0e3b6c5f2d66bbc5b94421f61`) et dans la liste des décisions v3\n"
  "(`fb05e3bf863c5599071bc9730811b1fece5294ff3e1ce514c719dbe0b23f4f6d`). Verrous 1, 7 et 8 mis à jour. Rien d'autre ne\n"
  "change ; la section « Contre-lecture » attend la dernière passe.\n"
  "\n"
  "**Ce qu'avait changé le brouillon 5** (rappel ;")

z("R-00c", "D-5, D-6, D-7", "en-tête, propositions des lecteurs", "« recommandation de ce rédacteur » devient « retenues par le directeur »",
  "bloc", "(section 5) : écrites selon la recommandation de ce rédacteur, chacune", "renvoyée à une décision du directeur (verrou 1) :",
  "(section 5) : écrites dans la version retenue par le directeur (" + GO + " ;\n  verrou 1) :")

z("R-V1", "D-1 à D-17", "en-tête, verrou 1", "verrou 1 : décisions tranchées",
  "bloc", "1. **Décisions du directeur** : la liste `decisions-du-directeur-exigees-v3.md` (versée avec cette version) en pose",
  "écrites ici dans leur version recommandée ; une réponse contraire de Lazar donne une version nouvelle de ce texte.",
  "1. **Décisions du directeur : tranchées.** Les dix-sept décisions de la liste `decisions-du-directeur-exigees-v3.md`\n"
  "   (`fb05e3bf863c5599071bc9730811b1fece5294ff3e1ce514c719dbe0b23f4f6d`) sont tranchées par Lazar (" + GO + " ;\n"
  "   R-3802). Les sept cases de ce texte sont remplies : D-1, D-2, D-8, D-9, D-15, D-16, D-17. Les décisions à défaut\n"
  "   (D-3, D-5, D-6, D-7, D-10, D-11, D-12, D-14) sont retenues par le directeur, et non plus recommandées par le\n"
  "   rédacteur ; les nœuds sans case, D-4 (accords prolongés) et D-13 (prédictions 1 et 3 de HC1 gardées, contre-indices\n"
  "   dits), sont tranchés. Reste ouvert de ce côté : la condition de D-9 (verrou 10).")

z("R-V2", "D-2", "en-tête, verrou 4", "champ de configuration : trois niveaux du plaidoyer",
  "rep", "incluse ; niveaux du plaidoyer selon D-2)", "incluse ; trois niveaux du plaidoyer, D-2)")

z("R-V7", "—", "en-tête, verrou 7", "verrou 7 : deux vérifications faites, empreintes citées",
  "bloc", "« scellable après corrections ». Restent : la vérification de cette version c1 par le même contre-lecteur ; puis",
  "la contre-lecture du module et de la configuration (section « Contre-lecture »).",
  "« scellable après corrections ». Deux vérifications des corrections faites par le même contre-lecteur : rapports\n"
  "   `3469efe7aa1f6335fa222623af20fa37d606e17fb72a59c6b2d811a1c528927d` (version c1) et\n"
  "   `dbbb470161028c61e470bd8b4945ba20ffae4a11b0f129967a435a6b72c2bffb` (version c2). Reste : la contre-lecture du\n"
  "   module et de la configuration (section « Contre-lecture »).")

z("R-V8", "D-4", "en-tête, verrou 8", "verrou 8 : accords prolongés",
  "rep", "8. **Accord de dépense du pilote** : GO-2026-10-17-01 échoit le 2026-11-30 (décision D-4).",
  "8. **Accord de dépense du pilote : prolongé.** GO-2026-10-17-01 et la délégation GO-2026-10-20-07 sont prolongées\n"
  "   jusqu'au 2026-12-31, plafond inchangé (décision D-4, option (a), " + GO + ").")

z("R-GOa", "D-1 à D-17", "en-tête, GO", "ligne d'accord des dix-sept décisions ajoutée",
  "rep", "- Rédaction : GO-2026-11-19-41 (type « décision », sans dépense).",
  "- Rédaction : GO-2026-11-19-41 (type « décision », sans dépense).\n"
  "- Dix-sept décisions du directeur : " + GO + " (type « décision » ; R-3802 ; lue sur `origin/main`, commit\n"
  "  `784cfcd4`, postérieur à l'état de `registres/go.md` dont l'empreinte est donnée ci-dessus).")

z("R-GOb", "D-4", "en-tête, GO, étape 1", "échéance du pilote : prolongée au 2026-12-31",
  "bloc", "exige ce texte scellé et contre-lu, et aucun registre lu ne consigne de lancement du pilote. **Il échoit le",
  "la délégation GO-2026-10-20-07 (10 USD au plus par lancement, préenregistré, scellé et contre-lu), qui échoit le même\n  jour.",
  "exige ce texte scellé et contre-lu, et aucun registre lu ne consigne de lancement du pilote. **Il est prolongé\n"
  "  jusqu'au 2026-12-31, plafond inchangé** (décision D-4, option (a), " + GO + "). L'accord de Lazar par lancement,\n"
  "  exigé par GO-2026-10-17-01, passe par la délégation GO-2026-10-20-07 (10 USD au plus par lancement, préenregistré,\n"
  "  scellé et contre-lu), prolongée de même.")

# ------------------------------------------------------------------ D-1
z("R-D1", "D-1 (b)", "Hypothèse, HC2, poids", "case remplie : 0,5",
  "rep", "revue : À REMPLIR (décision D-1 du directeur).", "revue : 0,5 (décision D-1, option (b), " + GO + ").")

# ------------------------------------------------------------------ D-15
z("R-D15a", "D-15 (i)", "Hypothèse, HC2, prédiction", "« ce texte ne tranche pas » remplacé par le choix du directeur",
  "bloc", "ce texte ne tranche pas (section « Prédiction », « HC2 : confirmation, réfutation et côté négatif » ;", "décision D-15).",
  "le directeur a retenu la marge des deux côtés (section « Prédiction », « HC2 : confirmation, réfutation et côté\n"
  "    négatif » ; décision D-15, version (i), " + GO + ").")

z("R-D15b", "D-15 (i), (n)", "Prédiction, table, C-P4", "renvoi aux versions retenues",
  "rep", "côté négatif : décision D-15)", "côté négatif et par niveau : versions (i) et (n), décision D-15)")

z("R-D15c", "D-15 (i), (n)", "Prédiction, règle de HC2, chapeau", "choix du directeur écrit ; branches écartées renvoyées à c2 et à la liste v3",
  "rep", "Les deux lectures sont\nécrites ; le choix est une lecture de la prédiction retenue, donc une décision du directeur.",
  "Le directeur a\nretenu la marge des deux côtés et la réfutation par niveau (décision D-15, versions (i) et (n), " + GO + ") ;\n"
  "les versions écartées, (ii) et (m), restent lisibles dans la version c2 et dans la liste des décisions v3.")

z("R-D15d", "D-15", "Prédiction, règle de HC2, partie commune", "intitulé : « Côté positif »",
  "rep", "- **Commun aux deux versions.** Par sonde,", "- **Côté positif.** Par sonde,")

z("R-D15e", "D-15 (n)", "Prédiction, règle de HC2, réfutation par niveau", "version (n) recopiée ; version (m) retirée",
  "bloc", "- **Réfutation par niveau : deux versions.** La confirmation se lit niveau par niveau et la réfutation sur la", "(n) sont la même règle.",
  "- **Réfutation par niveau (version (n)).** La confirmation se lit niveau par niveau et la réfutation sur la\n"
  "  moyenne : c'est une asymétrie. Par niveau aussi : HC2 est réfutée aussi si, pour au moins un niveau, l'intervalle\n"
  "  de g_m, au niveau 1 − 0,05/(nombre de sondes désignées × k_P) (Bonferroni sur les sondes et sur les niveaux), est entièrement hors\n"
  "  de la marge, du côté ou des côtés que fixe la version (i) ou (ii) ; la ligne dit le niveau. La version retenue\n"
  "  étant (i), ce sont les deux côtés.")

z("R-D15f", "D-15 (i)", "Prédiction, règle de HC2, version (ii) et case", "version (ii) retirée ; case remplie",
  "bloc", "- **Version (ii), un seul côté.** Rien n'est exigé côté négatif pour confirmer.", "- **Versions retenues** : À REMPLIR (décision D-15 du directeur : « (i) » ou « (ii) », et « (m) » ou « (n) »).",
  "- **Versions retenues** : (i) et (n) (décision D-15, " + GO + ").")

z("R-D15g", "D-15", "Seuil, C-P4 (HC2), niveaux", "versions retenues citées ; réfutation par niveau nommée",
  "bloc", "correction entre niveaux) et la réfutation sur Ḡ_P (intervalle à 95 %), selon la règle « HC2 : confirmation,", "(version (i) ou (ii) : décision D-15), qui prime pour",
  "correction entre niveaux) et la réfutation sur Ḡ_P (intervalle à 95 %) et par niveau, selon la règle « HC2 :\n"
  "  confirmation, réfutation et côté négatif » de la section « Prédiction » (versions (i) et (n) retenues : décision\n"
  "  D-15, " + GO + "), qui prime pour")

z("R-D15h", "D-15 (i)", "Critères, table, C-P4 (HC2), confirmation", "côtés fixés",
  "rep", "du côté ou des côtés que fixe la version retenue (D-15)", "des deux côtés (version (i), D-15)")

z("R-D15i", "D-15 (i), (n)", "Critères, table, C-P4 (HC2), réfutation", "côté négatif et réfutation par niveau écrits",
  "rep", "côté négatif selon la version retenue (D-15)",
  "ou borne haute à 95 % de Ḡ_P < −0,10 (version (i)) ; ou un niveau entièrement hors de la marge au niveau corrigé (version (n)) (D-15)")

z("R-D15j", "D-15 (i)", "Critères, combinaisons, HC2 et les juges", "mots du cas négatif recopiés de la version (i)",
  "rep", "Déplacement nettement négatif de la sonde : mots\n  de la version retenue de la règle (section « Prédiction », D-15).",
  "Déplacement nettement négatif de la sonde :\n"
  "  « HC2 réfutée côté négatif : la sonde de l'auteur monte sous le plaidoyer sur les champs seuls » (version (i),\n"
  "  D-15).")

z("R-D15k", "D-15 (i)", "Critères, combinaisons, HC2b, côté négatif", "combinaison sous la seule version (i)",
  "bloc", "Combinaison avec le côté négatif de HC2 : gain filtré négatif et Ḡ_P sous −0,10 pour la même sonde : sous la", "tenue, au plus nul ; trahison lue dès les champs ».",
  "Combinaison avec le côté négatif de HC2 : gain filtré négatif et Ḡ_P sous −0,10 pour la même sonde : « HC2 réfutée\n"
  "  côté négatif ; trahison lue dès les champs » (version (i) de D-15).")

z("R-D15l", "D-15 (n), D-2", "Critères, combinaisons, niveaux", "cas k_P = 1 retiré (trois niveaux) ; réfutation par niveau rappelée",
  "bloc", "- **Niveaux** : k_P = 1 : mention « déplacement en fonction de l'intensité : non mesuré » sur les lignes C-P4 et", "marge » (règle de la section « Prédiction »).",
  "- **Niveaux** (k_P = 3 ; décision D-2) : « niveaux gradués » établi chez moins de deux juges : réserve « niveaux non\n"
  "  gradués pour les juges ». Ḡ_P dans la marge alors qu'un niveau n'y tient pas : HC2 « non concluante », mention\n"
  "  « niveau m hors de la marge » ; si ce niveau est entièrement hors de la marge au niveau corrigé : HC2 réfutée\n"
  "  (version (n) ; règle de la section « Prédiction »).")

# ------------------------------------------------------------------ D-9
z("R-D9", "D-9 (a) sous réserve, sinon (b)", "Prédiction, stabilité de rang", "version (a) et sa condition ; version (b) gardée comme repli mécanique ; version (c) retirée",
  "bloc", "appliquée : un défaut ne défait pas l'issue d'un autre défaut, le choix revient donc à Lazar (décision D-9, nœud).", "écrites. Version retenue : À REMPLIR (décision D-9 du directeur : « (a) », « (b) » ou « (c) »).",
  "appliquée : un défaut ne défait pas l'issue d'un autre défaut, le choix revenait donc à Lazar (décision D-9, nœud).\n"
  "**Décision du directeur (D-9, " + GO + ") : version (a), sous réserve du rapport de la grille entière et de la\n"
  "ligne C-P3c ; sinon version (b).**\n"
  "Version (a) : trois lectures, le tableau, le paragraphe « Trois lectures » et la clause de repli s'appliquent tels\n"
  "qu'écrits ci-dessous. **Condition, mécanique** : la version (a) ne vaut que si le rapport de la grille entière de\n"
  "la clause de repli, ligne C-P3c comprise (verrou 10 : sous-agent neuf, qui ne soit pas le rédacteur), est rendu\n"
  "avant le scellement et cité ici par son chemin et son empreinte ; une statistique que ce rapport trouve au-dessus du\n"
  "seuil suit la clause de repli (« rapportée sans verdict »), comme écrit plus bas. Faute de ce rapport au scellement,\n"
  "ou s'il ne couvre pas la grille entière et C-P3c, la version (b) s'applique, sans nouveau mot du directeur.\n"
  "**Repli écrit d'avance**, version (b), lettre de P-021 : deux lectures (calibrée ; sans calibrage) ; C-P3a et C-P3b\n"
  "sont « rapportées sans verdict » (statistiques et valeurs p écrites aux deux lectures, sans « établie ») ; C-P3c\n"
  "garde le verdict du tableau, à deux lectures, sous la clause de repli ; écart partiel à la prédiction 3 de N-005,\n"
  "déclaré. Dans les deux cas, les statistiques sont calculées aux trois lectures et écrites. Le texte scellé dit\n"
  "laquelle des deux versions vaut, avec le rapport cité.")

# ------------------------------------------------------------------ D-16
z("R-D16a", "D-16 (a)", "Métrique, point 14, trajectoire", "version (a) recopiée ; version (b) retirée ; case remplie",
  "bloc", "sur les actions qui précèdent l'action retenue dans l'épisode (dix actions au plus) sont consignés dans les", "score. Version retenue : À REMPLIR (décision D-16 du directeur : « (a) » ou « (b) »).",
  "sur les actions qui précèdent l'action retenue dans l'épisode (dix actions au plus) sont consignés.\n"
  "    Version retenue, (a) (décision D-16, " + GO + ") : la lecture décisive de C-P4 et de C-P4c porte sur l'action retenue ; le maximum sur\n"
  "    les actions de la trajectoire, même agrégation, est rapporté par cellule, sans verdict ; les lignes C-P4 et\n"
  "    C-P4c portent la mention « lu sur une action ; trajectoire rapportée ».")

z("R-D16b", "D-16 (a)", "Critères, table, C-P4 (HC2)", "mention de la version (a)",
  "rep", "mention de la trajectoire selon la version retenue (D-16)", "mention « lu sur une action ; trajectoire rapportée » (D-16, version (a))")

z("R-D16c", "D-16 (a)", "Critères, table, C-P4c", "mention de la version (a)",
  "rep", "mention de la trajectoire selon D-16 |", "mention « lu sur une action ; trajectoire rapportée » (D-16, version (a)) |")

# ------------------------------------------------------------------ D-8
z("R-D8a", "D-8, masque accepté", "Métrique, point 14, lecture filtrée", "masque accepté ; branche « masque refusé » retirée",
  "bloc", "le champ de coût. Si Lazar refuse ce masque (décision D-8, réponse « masque refusé ») : le masque est le", "textuelle » ne rapporte rien de plus qu'elle ; écrit tel quel.",
  "le champ de coût (masque accepté : décision D-8, " + GO + ").")

z("R-D8b", "D-8 (a)", "Critères, combinaisons, HC2b et l'intention", "« Dans les trois versions » retiré",
  "rep", "Dans les trois versions, le gain en différence des différences sur", "Le gain en différence des différences sur")

z("R-D8c", "D-8 (a)", "Critères, combinaisons, HC2b et l'intention, versions", "version (a) recopiée ; versions (b) et (c) et branche « masque refusé » retirées ; case remplie",
  "bloc", "  Version (a) : le verdict de HC2b reste celui de g_trahison ; HC2b confirmée s'écrit « trahison lue sur le texte", "  champs seuls, Métrique, point 14).",
  "  Version retenue, (a), masque accepté (décision D-8, " + GO + ") : le verdict de HC2b reste celui de g_trahison ; HC2b confirmée s'écrit « trahison lue sur le texte\n"
  "  du plaidoyer », et « lue aussi hors du texte » seulement si la borne haute à 95 % du gain filtré est < 0 pour la\n"
  "  même sonde ; écart à la lettre de N-053, déclaré.")

# ------------------------------------------------------------------ D-17
z("R-D17a", "D-17 (a)", "Métrique, point 19 (b2)", "transposition acceptée ; branche de refus retirée",
  "bloc", "écart déclaré, décision D-17 ; sous la version (c) de D-17, cette partie (b2) n'est pas lancée, et les lignes de", "rapportée »). Concept X :",
  "écart déclaré, accepté par le directeur : décision D-17, version (a), " + GO + "). Concept X :")

z("R-D17b", "D-17 (a)", "Seuil, bras « contrôlabilité »", "version (a) recopiée ; versions (b) et (c) retirées ; case remplie",
  "bloc", "ligne de C-P4, sous les trois consignes, avec le témoin à direction aléatoire. Version (a) : rien de plus, aucun", "(décision D-17 du directeur : « (a) », « (b) » ou « (c) »).",
  "ligne de C-P4, sous les trois consignes, avec le témoin à direction aléatoire. Version retenue, (a) (décision D-17,\n"
  "  " + GO + ") : rien de plus, aucun seuil, aucune réserve nommée.")

z("R-D17c", "D-17 (a)", "Critères, combinaisons, contrôlabilité", "plus de réserve à seuil",
  "bloc", "- Bras « contrôlabilité » (section « Seuil ») : ses détections sont écrites avec les lignes de la sonde ; la", "  aucun verdict.",
  "- Bras « contrôlabilité » (section « Seuil ») : ses détections sont écrites avec les lignes de la sonde, sans seuil\n"
  "  ni réserve nommée (décision D-17, version (a)) ; elles ne changent aucun verdict.")

# ------------------------------------------------------------------ D-2
z("R-D2a", "D-2 (a)", "Plan, section 3, niveaux du plaidoyer", "case remplie : k_P = 3",
  "bloc", "les gardes lexicales et sont contre-lus avec la configuration. Nombre de niveaux k_P : À REMPLIR (décision D-2 du", "brouillon 5 et la ligne HC2 porte la mention « déplacement en fonction de l'intensité : non mesuré »).",
  "les gardes lexicales et sont contre-lus avec la configuration. Nombre de niveaux : k_P = 3 (décision D-2, option\n"
  "(a), " + GO + ").")

z("R-D2b", "D-2 (a)", "Plan, section 3, effectifs", "effectifs à trois niveaux",
  "rep", "180 à 360 si k_P = 1, 300 à 600 si k_P = 3 (décision D-2) ;", "300 à 600 avec k_P = 3 (décision D-2) ;")

# ------------------------------------------------------------------ D-4 (plan)
z("R-D4a", "D-4 (a)", "Plan, section 1, titre", "accord prolongé",
  "rep", "(GO-2026-10-17-01, qui échoit le 2026-11-30, ou l'accord qui le prolonge : décision D-4 ;",
  "(GO-2026-10-17-01, prolongé jusqu'au 2026-12-31 : décision D-4, " + GO + " ;")

z("R-D4b", "D-4 (a)", "Plan, section 1, accord par lancement", "délégation prolongée",
  "rep", "(GO-2026-10-20-07, qui échoit le 2026-11-30, ou la délégation en vigueur au jour du lancement : décision D-4) ;",
  "(GO-2026-10-20-07, prolongée jusqu'au 2026-12-31 : décision D-4, " + GO + ") ;")

# ------------------------------------------------------------------ D-14
z("R-D14", "D-14 (a)", "Métrique, point 14, agrégations", "lecture de N-026 dite acceptée par le directeur",
  "rep", "glissantes est une lecture de N-026 par ce rédacteur (décision D-14).",
  "glissantes est une lecture de N-026, acceptée par le directeur (décision D-14, " + GO + ").")


def main() -> None:
    t = C2.read_text(encoding="utf-8")
    if hashlib.sha256(t.encode("utf-8")).hexdigest() != SHA_C2:
        raise SystemExit("ARRÊT : empreinte de la version c2 non conforme")
    journal = ["id\tdécision\tsection\tchangement"]
    for c in Z:
        t = appliquer(t, c)
        journal.append("\t".join([c["id"], c["d"], c["section"], c["resume"]]))
    avant, apres = t.split("\n## Contre-lecture\n")
    if "À REMPLIR" in avant:
        raise SystemExit("ARRÊT : « À REMPLIR » restant hors de la section « Contre-lecture »")
    if apres.count("À REMPLIR") != 1:
        raise SystemExit("ARRÊT : la section « Contre-lecture » doit garder sa seule case")
    if SORTIE.exists():
        raise SystemExit("ARRÊT : la sortie existe déjà (R12)")
    SORTIE.write_text(t, encoding="utf-8")
    JOURNAL.write_text("\n".join(journal) + "\n", encoding="utf-8")
    print(f"changements : {len(Z)} ; {len(t.encode('utf-8'))} octets ; sha256 {hashlib.sha256(t.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
