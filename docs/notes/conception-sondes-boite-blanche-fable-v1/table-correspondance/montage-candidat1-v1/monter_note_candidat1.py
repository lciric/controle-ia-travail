"""Monte le candidat au scellement 1 de la note de conception à partir du brouillon 5, par remplacements exacts
(chaque motif doit se trouver une fois et une seule). Emploi : python3 monter_note_candidat1.py BROUILLON5 CANDIDAT HEURE"""
import sys

src, dst, heure = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding="utf-8").read()


def rep(a, b):
    global t
    assert t.count(a) == 1, (a[:70], t.count(a))
    t = t.replace(a, b)


# --- titre
rep("# Conception des sondes de la boîte blanche, version 2 (brouillon 5)",
    "# Conception des sondes de la boîte blanche, version 2 (candidat au scellement 1)")
# --- accords
rep("(`GO-2026-11-23-33`, écart déclaré à la règle « Qui conçoit »).\n- **Auteur** :",
    "(`GO-2026-11-23-33`, écart déclaré à la règle « Qui conçoit ») ; accord de relance des sessions (`GO-2026-11-23-30`) ; **mots de Lazar qui tranchent, selon les recommandations, les quatre points de jugement de la table de correspondance** (`GO-2026-11-23-36`) ; mandat de scellement donné par la session mère (ligne F9 de sa passation du 23 novembre 2026 à 22:20, ligne R-5205 du registre des décisions).\n- **Auteur** :")
# --- auteurs et date
rep("- **Auteur** : sous-agent neuf **Concepteur des sondes de la boîte blanche** (Carbon en effort élevé, conversation `408edcf5d0ec826fe4a61c5b411328fe`), portant les corrections de la contre-lecture indépendante sur le brouillon 4 (`9421374576bd39601878d5b52f96beddf583ab277e16313de144cad218e347b1`, gardé). **Date et heure en temps universel coordonné** : 2026-11-23, 21:11.",
    "- **Auteurs** : le corps de la note, le sous-agent neuf **Concepteur des sondes de la boîte blanche** du brouillon 5 (Carbon en effort élevé, conversation `408edcf5d0ec826fe4a61c5b411328fe`), à partir des brouillons 1 à 3 de la session de conception ; le titre, cet en-tête, les passages listés à la ligne « Ce qui change par rapport au brouillon 5 » et les deux dernières puces de la section « Contre-lecture », la session de conception `session_016QhUrvozGuPrL4eYUqDJvi`, servie par le modèle que la règle « Qui conçoit » réserve aux conceptions (attesté par l'attribution du commit de cette pièce), qui porte ici les décisions de Lazar. **Candidate au scellement** : elle remplace le brouillon 5 (`e9ad9d8af24e43724c5b99bda74981c8f896b248f46a833dc1c96613cdba0b8d`, gardé), qui remplaçait le brouillon 4 (`9421374576bd39601878d5b52f96beddf583ab277e16313de144cad218e347b1`, empreinte donnée par le brouillon 5 ; pièce absente du dépôt à la date de ce candidat, à y verser par la session mère). **Date et heure en temps universel coordonné** : 2026-11-23, " + heure + " (`date -u`).\n"
    "- **Ce qui change par rapport au brouillon 5, et rien d'autre** : (1) le titre et cet en-tête ; (2) à la section 7, la parenthèse de la condition 5 (les points de jugement sont tranchés), l'alinéa « Table de correspondance » (nom de la pièce candidate) et, à sa suite, l'alinéa « Écart de calendrier, déclaré » ; (3) à la section 8, le point 0 (état) ; (4) à la section « Contre-lecture », deux puces ajoutées. Tout le reste est celui du brouillon 5, à l'octet : sections 1 à 6, tables et autres alinéas de la section 7, points 1 à 7 de la section 8, section 9 et annexe A ; un `diff` des deux pièces ne montre que ces passages.")
# --- exposition
rep("- **Exposition de l'auteur** : l'auteur a lu les documents qui font foi",
    "- **Exposition de la session qui porte ce candidat** : elle n'a ouvert ni le texte scellé du test sur les adaptateurs jumeaux, ni son code, ni ses sorties, ni aucun verdict, ni `registres/etat.md`. Du texte scellé, elle n'a lu que les trois pièces servies que cite la table (extrait des critères gelés, attestation du conducteur, extrait de la liste d'arrêt), empreintes vérifiées avant lecture. Des registres, elle n'a lu que des lignes ou des débuts de lignes des registres des accords et des décisions (dont les lignes d'accord citées dans cet en-tête, R-5193 et R-5194), et la ligne F9 de la passation de la session mère ; sous `docs/verdicts/`, les seuls noms de fichiers. Aucun résultat du test lu.\n"
    "- **Exposition de l'auteur du brouillon 5** (déclarée par lui) : l'auteur a lu les documents qui font foi")
# --- statut
rep("- **Statut** : note de conception (brouillon 5).", "- **Statut** : note de conception (candidat au scellement 1).")
rep("sa table de correspondance (`table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md`) sont à sceller avant le verdict",
    "sa table de correspondance (`table-correspondance-issues-adaptateurs-jumeaux-v1-candidat1.md`) sont à sceller avant le verdict")
rep("- **Ce qui change par rapport au brouillon 4** (correction intégrale",
    "- **Ce que le brouillon 5 avait changé par rapport au brouillon 4** (correction intégrale")
# --- section 7, condition 5
rep("(les quatre points de jugement de la section 9 de la table doivent donc être tranchés ou confirmés par Lazar avant le scellement de la table).",
    "(les quatre points de jugement de la section 9 de la table ont donc été tranchés par Lazar avant le scellement de la table, selon les recommandations : `GO-2026-11-23-36`).")
# --- section 7, alinéa de la table, et écart de calendrier
rep("Table de correspondance : dossier de travail courant avant versement par la session mère vers `docs/notes/conception-sondes-boite-blanche-fable-v1/table-correspondance/` (pièce active : `table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md`, accompagnée du script de preuve formelle `verification-formelle-table-correspondance-brouillon3-v1.py`, remplaçant les brouillons 1 et 2 ; à vérifier en passe finale et sceller avant le verdict). Empreinte de sa version scellée : à inscrire ici par la session mère avant le scellement de cette note.",
    "Table de correspondance : `docs/notes/conception-sondes-boite-blanche-fable-v1/table-correspondance/` (pièce candidate au scellement : `table-correspondance-issues-adaptateurs-jumeaux-v1-candidat1.md`, dont les sections 1 à 8 sont celles du brouillon 3 à l'octet, accompagnée du script de preuve formelle `verification-formelle-table-correspondance-brouillon3-v1.py` ; à sceller avant le verdict). Empreinte de sa version scellée : à inscrire ici par la session mère avant le scellement de cette note.\n\n"
    "**Écart de calendrier, déclaré.** La condition 3 est tenue à la lettre si la table est scellée et inscrite avant le scellement du verdict, ce qu'attesteront les deux horodatages du registre. Mais les sorties de la relecture des familles jumelles du test existent depuis le 23 novembre 2026 à 10:12:09 en temps universel coordonné (ligne R-5193 du registre des décisions) : la table est scellée après leur production, avant toute ouverture d'un score et avant le verdict. Les faits, ce qui borne cet écart et ce qu'il ne permet pas sont écrits à la section 10, point 5, de la table.")
# --- section 8, point 0
rep("0. Table de correspondance de la section 7 (`table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md`) : arbitrage de Lazar sur les quatre points de jugement (section 9 de la table), passe finale de vérification des corrections par le même contre-lecteur (`c1a698101768d186848b8244a50d9f5c`), puis scellement avant le verdict du test en cours ; c'est la pièce la plus pressée.",
    "0. Table de correspondance de la section 7 (`table-correspondance-issues-adaptateurs-jumeaux-v1-candidat1.md`) : les quatre points de jugement sont tranchés par Lazar (`GO-2026-11-23-36`) ; vérification finale par un contre-lecteur neuf, puis scellement avant le verdict du test en cours ; c'est la pièce la plus pressée.")
# --- contre-lecture
rep("et est soumis au même contre-lecteur (`c1a698101768d186848b8244a50d9f5c`) pour sa passe de vérification finale.\n",
    "et est soumis au même contre-lecteur (`c1a698101768d186848b8244a50d9f5c`) pour sa passe de vérification finale.\n"
    "- **Vérification finale du brouillon 5** (`e9ad9d8af24e43724c5b99bda74981c8f896b248f46a833dc1c96613cdba0b8d`) : par le même contre-lecteur, rapport `table-correspondance/verification-finale-table-brouillon3-et-conception-brouillon5-v1.md` (`7488baf06bca644ca82a6c723adb7825125a6c0d73c298dd6cd6fedb2cb36390`), verdict « conforme, prêt à sceller après les mots de Lazar ».\n"
    "- **Ce candidat** porte les mots de Lazar (`GO-2026-11-23-36`) et l'écart de calendrier déclaré, sans autre changement. Vérification finale par un contre-lecteur neuf, d'un autre modèle que ses auteurs, dans un rapport à part qui cite l'empreinte de ce candidat. Relecture par la session de conception : `table-correspondance/relecture-concepteur-avant-scellement-v1.md` (réserves non bloquantes, sur la section 2 bis).\n")
open(dst, "w", encoding="utf-8").write(t)
print("fait")
