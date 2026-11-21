"""Mutations du lot 5 du véhicule NA-1 : pour chaque garde, la garde retirée fait échouer son essai (R5 ; manière de la
v68, R68, § 4, reprise par les programmes des lots 1 à 3).

Pour chaque mutation : une copie neuve, dans un dossier temporaire, des seuls fichiers dont les essais du lot 5 ont besoin
(les modules des lots 1 à 3 et 5, leurs aides, la liste d'essai, les données des ignorables, et six fichiers existants de
l'orchestrateur, lus seulement : `pole/__init__.py`, `fiches_v53.py`, `outils.py`, `caviardage.py`, `aiguilleur_v53.py`,
témoins du défaut du noyau et du « jamais appelé ») ; un ou plusieurs remplacements à texte exact, chacun dans son fichier
(chaque texte cherché doit y être une fois exactement, sinon la mutation est dite invalide) ; puis les essais nommés de
cette garde, joués dans un processus à part. La mutation est « tuée » si et seulement si pytest rend le code 1 ; tout
autre code est un échec du programme. Avant cela, les cinq fichiers d'essais entiers sont joués sur une copie non mutée :
ils doivent passer (code 0). Un témoin inerte (un mot de docstring changé) doit survivre.

Les mutations du module `identifiants_na_v1` (lot 1, repris tel quel) ne touchent que sa copie temporaire.

Usage, depuis n'importe où : `python -B mutations_na_lot5_v1.py JOURNAL.json` (le journal ne doit pas exister : R12).
Aucun réseau, aucune clé ; les copies temporaires sont retirées en fin de programme.
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
ORCH = os.path.dirname(ICI)

FICHIERS = (
    "pole/__init__.py",
    "pole/fiches_v53.py",
    "pole/outils.py",
    "pole/caviardage.py",
    "pole/aiguilleur_v53.py",
    "pole/identifiants_na_v1.py",
    "pole/tirage_na_v4.py",
    "pole/garde_motifs_na_v4.py",
    "pole/ignorables-unicode-15.1.0-na-v1.json",
    "pole/requete_na_v3.py",
    "pole/journal_na_v3.py",
    "pole/lecteur_fiches_na_v1.py",
    "pole/contrat_fiche_na_v1.py",
    "pole/portier_na_v1.py",
    "pole/registre_na_v1.py",
    "pole/verifier_registre_servi_na_v1.py",
    "essais/aides_na_v4.py",
    "essais/liste-motifs-essai-na-v1.json",
    "essais/aides_na_lot3_v3.py",
    "essais/aides_na_lot5_v1.py",
    "essais/test_na_lot5_v1_lecteur.py",
    "essais/test_na_lot5_v1_contrat.py",
    "essais/test_na_lot5_v1_portier.py",
    "essais/test_na_lot5_v1_registre.py",
    "essais/test_na_lot5_v1_identifiants.py",
)

TOUS = ["essais/test_na_lot5_v1_lecteur.py", "essais/test_na_lot5_v1_contrat.py", "essais/test_na_lot5_v1_portier.py",
        "essais/test_na_lot5_v1_registre.py", "essais/test_na_lot5_v1_identifiants.py"]
L = "essais/test_na_lot5_v1_lecteur.py::"
C = "essais/test_na_lot5_v1_contrat.py::"
P = "essais/test_na_lot5_v1_portier.py::"
R = "essais/test_na_lot5_v1_registre.py::"
I = "essais/test_na_lot5_v1_identifiants.py::"
LF = "pole/lecteur_fiches_na_v1.py"
CT = "pole/contrat_fiche_na_v1.py"
PT = "pole/portier_na_v1.py"
RG = "pole/registre_na_v1.py"
VR = "pole/verifier_registre_servi_na_v1.py"
ID = "pole/identifiants_na_v1.py"

MUTATIONS = [
    # --- lecteur ---
    ("L5-01", "champ en double admis (étiquettes)",
     [(LF, '    if len(vus) != len(set(vus)):\n        return ("non", CAUSE_DOUBLE)\n',
       '    if False:\n        return ("non", CAUSE_DOUBLE)\n')],
     [L + "TestGrammaireParEtiquettesAncrees::test_champ_en_double_non_reconnu",
      L + "TestGrammaireParEtiquettesAncrees::test_valeur_qui_porte_un_autre_nom_en_tete_de_ligne_refusee_jamais_lue_fausse"]),
    ("L5-02", "champ manquant admis (onze champs)",
     [(LF, "    if set(vus) != set(CHAMPS):\n", "    if False:\n")],
     [L + "TestGrammaireParEtiquettesAncrees::test_onze_champs_non_reconnue"]),
    ("L5-03", "« dans l'ordre » exigé de nouveau",
     [(LF, '    valeurs = {n: "\\n".join(v).strip(" \\t\\n") for n, v in entrees if n in CHAMPS}\n',
       '    if tuple(vus) != tuple(CHAMPS):\n        return ("non", CAUSE_MANQUANT)\n'
       '    valeurs = {n: "\\n".join(v).strip(" \\t\\n") for n, v in entrees if n in CHAMPS}\n')],
     [L + "TestGrammaireParEtiquettesAncrees::test_douze_champs_dans_un_autre_ordre",
      L + "TestGrammaireParEtiquettesAncrees::test_ordre_melange_dans_chaque_parure"]),
    ("L5-04", "étiquette cherchée partout dans la ligne (non ancrée)",
     [(LF, "    m = _ETIQUETTE.match(ligne)\n",
       '    m = next((x for x in (_ETIQUETTE.match(ligne[k:]) for k in range(len(ligne))) if x and x.group("deux")), None)\n')],
     [L + "TestGrammaireParEtiquettesAncrees::test_valeur_qui_contient_un_autre_nom_hors_tete_de_ligne_lue_juste"]),
    ("L5-05", "clé en double d'un objet non relevée",
     [(LF, '    if any(d in CHAMPS for d in getattr(o, "doubles", ())):\n', "    if False:\n")],
     [L + "TestObjetStructure::test_cle_en_double_non_reconnue"]),
    ("L5-06", "champ en plus d'un objet non relevé",
     [(LF, '    extras = tuple(k for k in o if k not in CHAMPS) + tuple(d for d in getattr(o, "doubles", ()) if d not in '
           'CHAMPS)\n', "    extras = ()\n")],
     [L + "TestObjetStructure::test_champ_en_plus_et_type_garde"]),
    ("L5-07", "champ en plus des étiquettes non relevé",
     [(LF, "    extras = tuple(n for n in noms if n not in CHAMPS)\n", "    extras = ()\n")],
     [L + "TestGrammaireParEtiquettesAncrees::test_champ_en_plus_releve_par_son_nom",
      C + "TestFormeEtType::test_champ_en_plus",
      P + "TestPortierFormeEtNeuf::test_temoin_a_champ_de_plus_au_coffre_sans_autre_cause_ni_appel"]),
    ("L5-08", "lecture qui rend rien sans fiche",
     [(LF, "    return Lecture(True, tuple(fiches), tuple(non))\n",
       "    return Lecture(True, tuple(fiches), tuple(non)) if fiches else None\n")],
     [L + "TestToujoursUnObjet"]),
    ("L5-09", "parure entourée refusée",
     [(LF, "    else:\n        if (f1 is None) == (f2 is None) or (f1 or f2) != ouv:\n            return None\n",
       "    else:\n        return None\n")],
     [L + "TestGrammaireParEtiquettesAncrees::test_chaque_parure_reconnue_aux_memes_valeurs"]),
    ("L5-10", "séparateurs de morceaux ignorés",
     [(LF, "    return _REGLE.match(ligne) is not None or (_TITRE.match(ligne) is not None and _etiquette(ligne) is None)\n",
       "    return False\n")],
     [L + "TestGrammaireParEtiquettesAncrees::test_deux_fiches_separees_par_une_regle",
      L + "TestGrammaireParEtiquettesAncrees::test_deux_fiches_separees_par_un_titre"]),
    ("L5-11", "caviardage avant la classification",
     [(LF, '    valeurs = {n: "\\n".join(v).strip(" \\t\\n") for n, v in entrees if n in CHAMPS}\n',
       '    from pole.caviardage import caviarder\n'
       '    valeurs = {n: caviarder("\\n".join(v).strip(" \\t\\n"))[0] for n, v in entrees if n in CHAMPS}\n')],
     [L + "TestChampCaseEtValidateurDuNoyau::test_champ_ferme_qu_un_caviardage_changerait_lu_tel_que_rendu"]),
    ("L5-12", "valeur réparée (ponctuation finale retirée)",
     [(LF, '    valeurs = {n: "\\n".join(v).strip(" \\t\\n") for n, v in entrees if n in CHAMPS}\n',
       '    valeurs = {n: "\\n".join(v).strip(" \\t\\n.") for n, v in entrees if n in CHAMPS}\n')],
     [L + "TestGrammaireParEtiquettesAncrees::test_rien_n_est_complete_ni_repare"]),
    ("L5-13", "deux-points sans blanc après lu comme étiquette",
     [(LF, "(?P<deux>:)(?=[ \\t]|$|\\*\\*|__|\\*|`)", "(?P<deux>:)")],
     [L + "TestGrammaireParEtiquettesAncrees::test_url_en_valeur_n_est_pas_une_etiquette"]),
    # --- contrat ---
    ("C5-01", "borne en octets non vérifiée",
     [(CT, '    hors = tuple(c for c in CHAMPS if type(contenu[c]) is str and len(contenu[c].encode("utf-8")) > '
           'bornes.borne(c))\n', "    hors = ()\n")],
     [C + "TestHorsContratDeLongueur", P + "TestHorsContratDeLongueur"]),
    ("C5-02", "couper à la borne",
     [(CT, '    hors = tuple(c for c in CHAMPS if type(contenu[c]) is str and len(contenu[c].encode("utf-8")) > '
           'bornes.borne(c))\n', "    hors = ()\n"),
      (PT, "        contenu = fiche.contenu()\n",
       '        contenu = {k: (v.encode("utf-8")[:self.bornes.borne(k)].decode("utf-8", "ignore") if type(v) is str else '
       'v) for k, v in fiche.contenu().items()}\n')],
     [P + "TestHorsContratDeLongueur::test_au_coffre_compte_sans_appel_texte_inchange"]),
    ("C5-03", "borne exacte refusée (≥ au lieu de >)",
     [(CT, '> bornes.borne(c))\n', '>= bornes.borne(c))\n')],
     [C + "TestHorsContratDeLongueur::test_chaque_champ_a_sa_borne_suit_son_chemin"]),
    ("C5-04", "type de chaîne non vérifié",
     [(CT, "    types_faux = tuple(c for c in CHAMPS if type(contenu[c]) is not str)\n", "    types_faux = ()\n")],
     [C + "TestFormeEtType::test_valeur_qui_n_est_pas_une_chaine"]),
    ("C5-05", "champ en plus non vérifié par le validateur",
     [(CT, "    en_plus = tuple(fiche.extras)\n", "    en_plus = ()\n")],
     [C + "TestFormeEtType::test_champ_en_plus",
      P + "TestPortierFormeEtNeuf::test_temoin_a_champ_de_plus_au_coffre_sans_autre_cause_ni_appel"]),
    ("C5-06", "comparaison « hors case » retirée",
     [(CT, '        if type(v) is not str or v.encode("utf-8") != attendue.encode("utf-8"):\n            rendu.append(nom)\n',
       "        if False:\n            rendu.append(nom)\n")],
     [C + "TestHorsCaseArret4", P + "TestArret4HorsCase::test_temoin_hors_case_refuse_et_compte"]),
    ("C5-07", "comparaison normalisée au lieu de l'octet",
     [(CT, '        if type(v) is not str or v.encode("utf-8") != attendue.encode("utf-8"):\n',
       '        if type(v) is not str or __import__("unicodedata").normalize("NFKC", v).strip().casefold() != '
       '__import__("unicodedata").normalize("NFKC", attendue).strip().casefold():\n')],
     [C + "TestHorsCaseArret4::test_un_octet_de_difference", C + "TestHorsCaseArret4::test_casse_differente_hors_case",
      C + "TestHorsCaseArret4::test_forme_unicode_differente_hors_case"]),
    ("C5-08", "champ `case` jamais dit différent",
     [(CT, '    return type(v) is not str or v.encode("utf-8") != identifiant_case.encode("utf-8")\n', "    return False\n")],
     [C + "TestChampCase::test_case_differente",
      P + "TestChampCaseEtAutreANommer::test_champ_case_different_consigne_compte_classe_inchangee"]),
    ("C5-09", "bornes d'autres champs que les douze admises",
     [(CT, "    if not isinstance(dictionnaire, dict) or set(dictionnaire) != set(CHAMPS):\n",
       "    if not isinstance(dictionnaire, dict):\n")],
     [C + "TestBornes::test_bornes_des_douze_champs_exactement"]),
    # --- portier ---
    ("P5-01", "étiquette hors liste admise",
     [(PT, '    if trouvees[0] not in par_texte:\n        return LectureEtiquette(sorte, None, "hors liste")\n'
           '    return LectureEtiquette(sorte, par_texte[trouvees[0]], "lue")\n',
       '    return LectureEtiquette(sorte, par_texte.get(trouvees[0], list(par_texte.values())[0]), "lue")\n')],
     [P + "TestDeclarationEtLecture::test_hors_liste_absente_ou_double_vaut_illisible",
      P + "TestPortierFormeEtNeuf::test_etiquette_illisible_fiche_au_coffre_comptee_a_part"]),
    ("P5-02", "étiquette double admise",
     [(PT, '    if len(trouvees) > 1:\n        return LectureEtiquette(sorte, None, "double")\n',
       '    if False:\n        return LectureEtiquette(sorte, None, "double")\n')],
     [P + "TestDeclarationEtLecture::test_hors_liste_absente_ou_double_vaut_illisible"]),
    ("P5-03", "étiquette absente vaut passage",
     [(PT, '    if not trouvees:\n        return LectureEtiquette(sorte, None, "absente")\n',
       '    if not trouvees:\n        return LectureEtiquette(sorte, list(declaration.textes(sorte))[0], "lue")\n')],
     [P + "TestDeclarationEtLecture::test_hors_liste_absente_ou_double_vaut_illisible"]),
    ("P5-04", "lecture qui rend rien sans étiquette",
     [(PT, '    if not trouvees:\n        return LectureEtiquette(sorte, None, "absente")\n',
       "    if not trouvees:\n        return None\n")],
     [P + "TestDeclarationEtLecture::test_la_lecture_rend_toujours_un_objet"]),
    ("P5-05", "passeport non exigé",
     [(PT, "        p = self._passeports.get(identifiant) if type(identifiant) is str else None\n",
       "        return self._passeports.get(identifiant)\n")],
     [P + "TestPasseportExige"]),
    ("P5-06", "empreinte du texte classé non comparée",
     [(PT, "        if not isinstance(contenu, dict) or empreinte_texte_classe(contenu) != p.empreinte:\n",
       "        if not isinstance(contenu, dict):\n")],
     [P + "TestPasseportExige::test_texte_change_apres_classement_arret"]),
    ("P5-07", "garde « hors case » retirée du portier",
     [(PT, "            elif ct.champs_fermes_differents(contenu, case):  # (iii) hors case, arrêt n° 4\n",
       "            elif False:\n")],
     [P + "TestArret4HorsCase::test_temoin_hors_case_refuse_et_compte",
      P + "TestPasseportExige::test_hors_case_sans_passeport"]),
    ("P5-08", "ordre D6 inversé : hors case avant le modèle",
     [(PT, "            sens, cause_appel = self._appeler_modele(requete, SORTE_FICHE)  # (ii) modèle\n",
       "            sens, cause_appel = (NIVEAU_IDEE, CAUSE_ETIQUETTE_LUE) if ct.champs_fermes_differents(contenu, case) else "
       "self._appeler_modele(requete, SORTE_FICHE)\n")],
     [P + "TestArret4HorsCase::test_hors_case_et_concret_au_coffre_ordre_D6",
      P + "TestArret4HorsCase::test_le_modele_est_appele_avant_la_comparaison_hors_case"]),
    ("P5-09", "programme de forme sauté : le modèle est appelé",
     [(PT, "        if not verdict.au_contrat:  # (i) forme : le modèle n'est pas appelé\n", "        if False:\n")],
     [P + "TestPortierFormeEtNeuf::test_temoin_a_champ_de_plus_au_coffre_sans_autre_cause_ni_appel",
      P + "TestHorsContratDeLongueur::test_au_coffre_compte_sans_appel_texte_inchange"]),
    ("P5-10", "refus écrit qui vaut passage",
     [(PT, "            return None, (CAUSE_REFUS_ECRIT_FICHE if sorte == SORTE_FICHE else CAUSE_REFUS_ECRIT_REPONSE)\n",
       "            return (NIVEAU_IDEE if sorte == SORTE_FICHE else VIDE_MOTIVEE), CAUSE_ETIQUETTE_LUE\n")],
     [P + "TestRefusEcritEtAppelsSansLecture::test_refus_ecrit_fiche_au_coffre_classe_ecrite_comptee",
      P + "TestRefusEcritEtAppelsSansLecture::test_refus_ecrit_reponse_sans_fiche_illisible"]),
    ("P5-11", "appel non lancé qui vaut passage",
     [(PT, "            return None, CAUSE_NON_LANCE\n", "            return NIVEAU_IDEE, CAUSE_ETIQUETTE_LUE\n")],
     [P + "TestRefusEcritEtAppelsSansLecture::test_non_lance_ou_non_lu_au_coffre"]),
    ("P5-12", "sous-compte « étiquette du portier illisible » omis",
     [(PT, "            classe, sous_compte = ILLISIBLE, SOUS_COMPTE_PORTIER\n", "            classe, sous_compte = ILLISIBLE, None\n")],
     [P + "TestClassesDIssueDAppel::test_etiquette_illisible_reponse_illisible_sous_compte"]),
    ("P5-13", "contenu écrit au journal du portier",
     [(PT, "        self._consigner(identifiant=identifiant, sorte=SORTE_FICHE, case=case, empreinte=empreinte, classe=classe,\n",
       "        self._consigner(identifiant=identifiant, sorte=SORTE_FICHE, case=case, empreinte=json.dumps(contenu, "
       "ensure_ascii=False), classe=classe,\n")],
     [P + "TestJournalSansContenu::test_journal_scelle_sans_aucun_contenu"]),
    ("P5-14", "identifiant redit admis",
     [(PT, '        if mot in self._identifiants:\n', "        if False:\n")],
     [P + "TestPortierFormeEtNeuf::test_identifiant_hexadecimal_ou_redit_refuse"]),
    ("P5-15", "identifiant non décodé (hexadécimal admis)",
     [(PT, "            ident.decoder_octets(mot, OCTETS_IDENTIFIANT)\n", "            pass\n")],
     [P + "TestPortierFormeEtNeuf::test_identifiant_hexadecimal_ou_redit_refuse",
      I + "TestRefus::test_le_portier_refuse_un_identifiant_qui_ne_se_decode_pas"]),
    ("P5-16", "refus écrit d'une autre sorte admis",
     [(PT, "            if issue.sorte != requete.sorte:\n", "            if False:\n")],
     [P + "TestRefusEcritEtAppelsSansLecture::test_refus_ecrit_d_une_autre_sorte_refuse"]),
    ("P5-17", "champ `case` différent qui change la classe",
     [(PT, "            else:  # (iv)\n", "            elif case_diff:\n                classe, cause = HORS_CASE, CAUSE_HORS_CASE\n"
           "            else:  # (iv)\n")],
     [P + "TestChampCaseEtAutreANommer::test_champ_case_different_consigne_compte_classe_inchangee"]),
    ("P5-18", "lecture d'une autre fonction admise",
     [(PT, "            if not isinstance(lu, LectureEtiquette) or lu.sorte != sorte:\n", "            if False:\n")],
     [P + "TestRefusEcritEtAppelsSansLecture::test_lecture_d_une_autre_fonction_refusee"]),
    ("P5-19", "issue d'appel inconnue qui vaut passage",
     [(PT, '        raise PortierRefuse("issue d\'appel inconnue : ni « non lancé », ni refus écrit, ni résultat du noyau")\n',
       "        return NIVEAU_IDEE, CAUSE_ETIQUETTE_LUE\n")],
     [P + "TestRefusEcritEtAppelsSansLecture::test_issue_inconnue_refusee"]),
    ("P5-20", "empreinte de la fiche servie non contrôlée",
     [(PT, "            if len(servie) != 1 or servie[0].sha256 != empreinte:\n", "            if False:\n")],
     [P + "TestRefusEcritEtAppelsSansLecture::test_fiche_servie_d_une_autre_empreinte_que_le_texte_classe_refusee"]),
    ("P5-21", "liste fermée des champs d'un fichier en ajout seul retirée",
     [(PT, "        if inconnus:\n            raise AjoutSeulRefuse(\"champ hors de la liste fermée\")\n",
       "        if False:\n            raise AjoutSeulRefuse(\"champ hors de la liste fermée\")\n")],
     [R + "TestRegistreDesTentatives::test_champ_hors_liste_refuse"]),
    ("P5-22", "ajout seul non vérifié (fichier réécrit admis)",
     [(PT, "        if len(present) != self._taille or _sha256(present) != self._empreinte:\n", "        if False:\n")],
     [P + "TestJournalSansContenu::test_journal_reecrit_refuse"]),
    # --- registre ---
    ("R5-01", "ligne de compte omise à zéro",
     [(RG, "    lignes_compte = [((c, rang_classe[k]), ligne_compte(c, k, n)) for (c, k), n in comptes.items()]\n",
       "    lignes_compte = [((c, rang_classe[k]), ligne_compte(c, k, n)) for (c, k), n in comptes.items() if n > 0]\n")],
     [R + "TestRegistreServi::test_lignes_de_compte_ecrites_toujours_compte_nul_compris"]),
    ("R5-02", "énoncé coupé",
     [(RG, '    return " ".join(idee.split())\n', '    return " ".join(idee.split())[:200]\n')],
     [R + "TestRegistreDesTentatives::test_enonce_sans_coupe"]),
    ("R5-03", "énoncé non ramené à une ligne",
     [(RG, '    return " ".join(idee.split())\n', "    return idee.strip()\n")],
     [R + "TestRegistreDesTentatives::test_lignes_aux_champs_fermes_nom_et_enonce"]),
    ("R5-04", "permutation par la clé non appliquée",
     [(RG, "        ordre = [rangees[i][1] for i in perm]\n", "        ordre = [e[1] for e in rangees]\n")],
     [R + "TestRegistreServi::test_ordre_range_puis_permute_par_la_cle_12"]),
    ("R5-05", "tentatives de la génération courante servies",
     [(RG, '        if l["generation"] >= generation:\n', '        if l["generation"] > generation:\n')],
     [R + "TestRegistreServi::test_generation_3_lit_les_generations_1_et_2_seules"]),
    ("R5-06", "garde du coffre à un quart exactement (≥)",
     [(RG, "    depasse = 4 * au_coffre > rendues\n", "    depasse = 4 * au_coffre >= rendues\n")],
     [R + "TestArret5GardeDuCoffre::test_un_quart_exactement_la_suivante_part"]),
    ("R5-07", "garde du coffre qui arrête à la troisième génération",
     [(RG, "    if depasse and generation in (1, 2):\n", "    if depasse:\n")],
     [R + "TestArret5GardeDuCoffre::test_a_la_troisieme_consigne"]),
    ("R5-08", "garde du coffre qui n'arrête pas",
     [(RG, "        raise ArretGardeCoffre(generation, au_coffre, rendues)\n", "        pass\n")],
     [R + "TestArret5GardeDuCoffre::test_une_fiche_de_plus_au_coffre_la_suivante_ne_part_pas",
      R + "TestArret5GardeDuCoffre::test_avec_le_portier_hors_longueur_et_refus_ecrit_au_denominateur"]),
    ("R5-09", "champ de l'espèce admis au registre des tentatives",
     [(RG, '    CHAMPS_PERMIS = ("identifiant", "generation", "case", "classe") + ct.CHAMPS_FERMES + ("nom", "enonce")\n',
       '    CHAMPS_PERMIS = ("identifiant", "generation", "case", "classe", "espece") + ct.CHAMPS_FERMES + ("nom", '
       '"enonce")\n')],
     [R + "TestRegistreDesTentatives::test_champ_hors_liste_refuse"]),
    ("R5-10", "le nom n'est plus l'identifiant de la fiche",
     [(RG, '            champs["nom"] = issue.identifiant\n', '            champs["nom"] = issue.identifiant_case\n')],
     [R + "TestRegistreDesTentatives::test_lignes_aux_champs_fermes_nom_et_enonce"]),
    ("R5-11", "tentative d'une case non servie admise",
     [(RG, '        if l.get("case") not in cases:\n', "        if False:\n")],
     [R + "TestRegistreServi::test_tentative_d_une_case_non_servie_refusee"]),
    # --- vérification du registre servi ---
    ("V5-01", "arrêt n° 8 : taille non vérifiée",
     [(VR, "    if len(octets) > borne_registre_octets:\n", "    if False:\n")],
     [R + "TestArret8::test_registre_egal_a_sa_borne_passe_un_octet_de_plus_refuse"]),
    ("V5-02", "arrêt n° 9 : étiquettes interdites non cherchées",
     [(VR, '    return [(ARRET_ETIQUETTE, f"étiquette interdite : {nom}") for nom, m in ETIQUETTES_INTERDITES if '
           'm.search(texte)]\n', "    return []\n")],
     [R + "TestArret9"]),
    ("V5-03", "deux lignes pour une tentative admises",
     [(VR, "            if nom in noms:\n", "            if False:\n")],
     [R + "TestArret19::test_deux_lignes_pour_une_tentative"]),
    ("V5-04", "borne de l'énoncé non vérifiée",
     [(VR, '    if len(enonce.encode("utf-8")) > borne_octets:\n', "    if False:\n")],
     [R + "TestArret19::test_un_enonce_d_un_octet_de_trop"]),
    ("V5-05", "marque de code non cherchée",
     [(VR, "    if MARQUES_DE_CODE.search(texte):\n", "    if False:\n")],
     [R + "TestArret19::test_une_marque_de_code"]),
    ("V5-06", "marque d'étape numérotée non cherchée",
     [(VR, "    if MARQUES_D_ETAPE.search(texte):\n", "    if False:\n")],
     [R + "TestArret19::test_une_etape_numerotee"]),
    ("V5-07", "marque de consigne non cherchée",
     [(VR, "    if MARQUES_DE_CONSIGNE.search(texte):\n", "    if False:\n")],
     [R + "TestArret19::test_une_marque_de_consigne"]),
    ("V5-08", "champ de plus après l'énoncé admis",
     [(VR, "    if fin != len(brut) or type(enonce) is not str:\n", "    if type(enonce) is not str:\n")],
     [R + "TestArret19::test_un_champ_de_plus"]),
    ("V5-09", "classe autre que « passée » admise",
     [(VR, "    if classe != pt.PASSEE:\n", "    if False:\n")],
     [R + "TestArret19::test_classe_autre_que_passee"]),
    ("V5-10", "premier défaut seul rendu (les arrêts ne s'ajoutent plus)",
     [(VR, "        raise RegistreServiNonConforme(defauts)\n", "        raise RegistreServiNonConforme(defauts[:1])\n")],
     [R + "TestArret19::test_les_arrets_s_ajoutent"]),
    ("V5-11", "retrait silencieux : défauts trouvés, registre dit conforme",
     [(VR, "    if defauts:\n", "    if False:\n")],
     [R + "TestArret19", R + "TestArret9", R + "TestArret8"]),
    ("V5-12", "ligne de compte manquante non vue",
     [(VR, "        if attendues - set(comptes):\n", "        if False:\n")],
     [R + "TestArret19::test_ligne_de_compte_manquante_ou_tentative_manquante"]),
    ("V5-13", "énoncé sur deux lignes admis",
     [(VR, "    if not _sur_une_ligne(enonce):\n", "    if False:\n")],
     [R + "TestArret19::test_enonce_sur_deux_lignes"]),
    ("V5-14", "compte qui n'est pas un entier admis",
     [(VR, "            if _ENTIER.match(n) is None:\n", "            if False:\n")],
     [R + "TestArret19::test_ligne_d_une_autre_forme_et_compte_non_entier"]),
    ("V5-15", "ligne d'une autre forme admise",
     [(VR, '            defauts.append(Defaut(ARRET_NON_CONFORME, i, "ligne d\'une autre forme"))\n', "            pass\n")],
     [R + "TestArret19::test_ligne_d_une_autre_forme_et_compte_non_entier"]),
    # --- identifiants (lot 1, copie temporaire seulement) ---
    ("I5-01", "ordre des octets inversé",
     [(ID, '    valeur = int.from_bytes(bytes(octets), "big")  # premier octet le plus fort (point 2)\n',
       '    valeur = int.from_bytes(bytes(octets), "little")  # premier octet le plus fort (point 2)\n')],
     [I + "TestDeuxSens"]),
    ("I5-02", "syllabe hors alphabet corrigée au lieu d'être refusée",
     [(ID, '        if syllabe not in RANG_SYLLABE:\n            raise MotRefuse("hors alphabet")\n',
       '        if syllabe not in RANG_SYLLABE:\n            syllabe = "ga"\n')],
     [I + "TestRefus::test_hors_alphabet"]),
    ("I5-03", "longueur du mot non vérifiée",
     [(ID, "    if len(mot) != 2 * n_syllabes:\n", "    if False:\n")],
     [I + "TestRefus::test_mauvaise_longueur"]),
    ("I5-04", "borne de l'entier non vérifiée",
     [(ID, "    if valeur >= 256 ** n_octets:\n", "    if False:\n")],
     [I + "TestRefus::test_entier_au_dela_de_la_borne"]),
]

# Témoin du programme (R4) : une mutation inerte, qui ne touche aucune garde, doit survivre (code 0).
TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé",
                 [(PT, "**Ce que ce portier n'appelle pas**", "**Ce que ce portier ne sollicite pas**")],
                 [P + "TestPortierFormeEtNeuf", P + "TestPasseportExige"])


def copier(dest):
    for rel in FICHIERS:
        cible = os.path.join(dest, rel)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        shutil.copyfile(os.path.join(ORCH, rel), cible)


def jouer(dossier, essais):
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *essais],
                       cwd=dossier, env=env, capture_output=True, text=True)
    lignes = [l for l in r.stdout.splitlines() if l.strip()]
    return r.returncode, (lignes[-1] if lignes else "")


def main(argv):
    if len(argv) != 1:
        print("usage : mutations_na_lot5_v1.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in FICHIERS:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-lot5-v1-")
    rendu = {"version": "journal-mutations-na-lot5-v1", "python": sys.version.split()[0], "fichiers": empreintes,
             "mutations": []}
    try:
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, TOUS)
        rendu["temoin_non_mute"] = {"essais": "les cinq fichiers entiers", "code": code, "resume": resume,
                                    "passe": code == 0}
        for ident_m, nom, remplacements, essais in [TEMOIN_INERTE] + MUTATIONS:
            dossier = os.path.join(racine_tmp, ident_m)
            copier(dossier)
            valide = True
            sources = {}
            for fichier, ancien, nouveau in remplacements:
                chemin = os.path.join(dossier, fichier)
                if chemin not in sources:
                    with open(chemin, encoding="utf-8") as f:
                        sources[chemin] = f.read()
                if sources[chemin].count(ancien) != 1:
                    valide = False
                    break
                sources[chemin] = sources[chemin].replace(ancien, nouveau, 1)
            entree = {"id": ident_m, "garde_retiree": nom, "fichiers": sorted({r[0] for r in remplacements}),
                      "essais": essais, "valide": valide}
            if valide:
                for chemin, source in sources.items():
                    with open(chemin, "w", encoding="utf-8") as f:
                        f.write(source)
                code, resume = jouer(dossier, essais)
                entree.update({"code": code, "resume": resume, "tuee": code == 1})
            else:
                entree.update({"code": None, "resume": "texte cherché absent ou multiple", "tuee": False})
            shutil.rmtree(dossier, ignore_errors=True)
            if ident_m == TEMOIN_INERTE[0]:
                entree["survit_comme_attendu"] = valide and entree["code"] == 0
                rendu["temoin_inerte"] = entree
                print(f"{ident_m} {'survit, comme attendu' if entree['survit_comme_attendu'] else 'ANOMALIE'} — {nom}")
                continue
            rendu["mutations"].append(entree)
            print(f"{ident_m} {'tuée' if entree['tuee'] else 'NON TUÉE'} — {nom} — {entree['resume']}")
    finally:
        shutil.rmtree(racine_tmp, ignore_errors=True)
    n = len(rendu["mutations"])
    tuees = sum(1 for m in rendu["mutations"] if m["tuee"])
    rendu["bilan"] = {"mutations": n, "tuees": tuees,
                      "non_tuees": [m["id"] for m in rendu["mutations"] if not m["tuee"]],
                      "temoin_non_mute_passe": rendu["temoin_non_mute"]["passe"],
                      "temoin_inerte_survit": rendu["temoin_inerte"]["survit_comme_attendu"],
                      "conforme": tuees == n and rendu["temoin_non_mute"]["passe"]
                      and rendu["temoin_inerte"]["survit_comme_attendu"]}
    with open(journal, "x", encoding="utf-8") as f:
        f.write(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print(json.dumps(rendu["bilan"], ensure_ascii=False))
    return 0 if rendu["bilan"]["conforme"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
