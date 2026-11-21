"""Mutations du lot 3 du véhicule NA-1 : pour chaque garde, la garde retirée fait échouer son essai (R5 ; manière de la
v68, R68, § 4, et du programme des lots 1 et 2).

Pour chaque mutation : une copie neuve, dans un dossier temporaire, des seuls fichiers dont les essais du lot 3 ont besoin
(les modules des lots 1 à 3, leurs aides, la liste d'essai, et cinq fichiers existants de l'orchestrateur, lus seulement :
`pole/__init__.py` et les quatre modules de la forme de fiche du noyau, témoin de la forme déclarée) ; un ou plusieurs
remplacements à texte exact dans un module (chaque texte cherché doit y être une fois exactement, sinon la mutation est
dite invalide) ; puis les essais nommés de cette garde, joués dans un processus à part. La mutation est « tuée » si et
seulement si pytest rend le code 1 (des essais échouent) ; tout autre code est un échec du programme. Avant cela, les deux
fichiers d'essais entiers sont joués sur une copie non mutée : ils doivent passer (code 0). Un témoin inerte (un mot de
docstring changé) doit survivre.

Usage, depuis n'importe où : `python -B mutations_na_lot3_v1.py JOURNAL.json` (le journal ne doit pas exister : R12).
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
    "pole/fiches_v54.py",
    "pole/fiches_v53.py",
    "pole/outils.py",
    "pole/caviardage.py",
    "pole/identifiants_na_v1.py",
    "pole/tirage_na_v2.py",
    "pole/garde_motifs_na_v2.py",
    "pole/requete_na_v1.py",
    "pole/journal_na_v1.py",
    "essais/aides_na_v2.py",
    "essais/liste-motifs-essai-na-v1.json",
    "essais/aides_na_lot3_v1.py",
    "essais/test_na_v1_requete.py",
    "essais/test_na_v1_journal.py",
)

TOUS = ["essais/test_na_v1_requete.py", "essais/test_na_v1_journal.py"]
R = "essais/test_na_v1_requete.py::"
J = "essais/test_na_v1_journal.py::"
RQ = "pole/requete_na_v1.py"
JN = "pole/journal_na_v1.py"

MUTATIONS = [
    # --- requete : gabarit et question ---
    ("L3-01", "question admise par son nom", RQ,
     [("    if chemin_ou_nom is not None and any(n in os.path.basename(str(chemin_ou_nom)) for n in NOMS_QUESTION):\n",
       "    if False:\n")],
     [R + "TestGabarit::test_question_refusee_par_son_nom_avant_toute_ouverture"]),
    ("L3-02", "empreinte de la question admise (gabarit)", RQ,
     [("    if _sha256(bytes(octets)) in EMPREINTES_QUESTION:\n", "    if False:\n")],
     [R + "TestGabarit::test_question_refusee_par_son_empreinte"]),
    ("L3-03", "empreinte de la question admise (pièce lue sur le disque)", RQ,
     [("    if _sha256(octets) in EMPREINTES_QUESTION:\n", "    if False:\n")],
     [R + "TestGabarit::test_question_refusee_par_son_empreinte"]),
    ("L3-04", "empreinte d'une pièce non vérifiée (arrêt n° 14)", RQ,
     [("    if type(empreinte_attendue) is not str or sha != empreinte_attendue:\n", "    if False:\n")],
     [R + "TestGabarit::test_empreinte_differente_refusee_en_nommant_la_piece",
      R + "TestFormeFicheServie::test_consigne_a_une_autre_empreinte_refusee"]),
    ("L3-05", "nombre d'emplacements non vérifié", RQ,
     [("    if n != 1:\n", "    if False:\n")],
     [R + "TestGabarit::test_zero_emplacement_refuse", R + "TestGabarit::test_deux_emplacements_refuses"]),
    ("L3-06", "emplacement hors d'une ligne propre admis", RQ,
     [("    if not (i == 0 or octets[i - 1:i] == FIN_DE_LIGNE) or not (j == len(octets) or octets[j:j + 1] == FIN_DE_LIGNE):\n",
       "    if False:\n")],
     [R + "TestGabarit::test_emplacement_hors_d_une_ligne_propre_refuse"]),
    # --- requete : partie servie et ligne de case ---
    ("L3-07", "ligne de case non contrôlée par le lot 1", RQ,
     [("    tn.controler_ligne_de_case(1, case.triplet, case.ligne, legende)\n", "    pass\n")],
     [R + "TestPartieServie::test_ligne_de_case_qui_differe_d_un_octet_refusee"]),
    ("L3-08", "ligne non rebâtie de son identifiant et de son triplet", RQ,
     [("    if tn.ligne_de_case(case.identifiant, case.triplet, legende) != case.ligne:\n", "    if False:\n")],
     [R + "TestPartieServie::test_ligne_qui_n_est_pas_celle_de_son_identifiant_refusee"]),
    ("L3-09", "tirage d'un autre gabarit admis", RQ,
     [("    if sortie.get(\"gabarit_sha256\") != gabarit.sha256:\n", "    if False:\n")],
     [R + "TestPartieServie::test_tirage_d_un_autre_gabarit_refuse"]),
    ("L3-10", "légende du tirage non comparée à celle du gabarit", RQ,
     [("    if sortie.get(\"legende\", {}).get(\"valeurs\") != legende[\"valeurs\"]:\n", "    if False:\n")],
     [R + "TestPartieServie::test_legende_du_tirage_differente_refusee"]),
    ("L3-11", "lignes du tirage non contrôlées", RQ,
     [("    tn.controler_lignes_de_case(tn.lignes_du_tirage(sortie), legende)\n", "    pass\n")],
     [R + "TestPartieServie::test_lignes_du_tirage_controlees"]),
    ("L3-12", "dernier octet de la partie servie retiré (retrait du noyau)", RQ,
     [("    rempli = gabarit.octets.replace(EMPLACEMENT, octets_ligne, 1)\n",
       "    rempli = gabarit.octets.replace(EMPLACEMENT, octets_ligne, 1).rstrip()\n")],
     [R + "TestPartieServie::test_partie_servie_a_l_octet",
      R + "TestDernierOctet::test_partie_servie_et_synthese_jointes_sans_retrait"]),
    # --- requete : enveloppe sans ajout (D2) ---
    ("L3-13", "séparateur doublé : une ligne de plus dans l'enveloppe", RQ,
     [("SEPARATEUR = b\"\\n\"  #", "SEPARATEUR = b\"\\n\\n\"  #")],
     [R + "TestEnveloppeSansAjout::test_proposeur_generation_1_exacte"]),
    ("L3-14", "section « Case » du noyau ajoutée à l'enveloppe", RQ,
     [("    a.ajouter(\"partie servie remplie\", \"piece\", partie.octets, partie)\n    a.ajouter(\"séparateur\", "
       "\"separateur\", SEPARATEUR)\n    a.ajouter(\"synthèse servie\"",
       "    a.ajouter(\"partie servie remplie\", \"piece\", partie.octets, partie)\n    a.ajouter(\"section du noyau\", "
       "\"forme\", b\"\\n## Case\\nTexte : x\\n\")\n    a.ajouter(\"séparateur\", \"separateur\", SEPARATEUR)\n"
       "    a.ajouter(\"synthèse servie\"")],
     [R + "TestEnveloppeSansAjout::test_proposeur_generation_1_exacte",
      R + "TestEnveloppeSansAjout::test_aucun_texte_du_noyau_ni_de_role"]),
    ("L3-15", "registre servi admis à la génération 1", RQ,
     [("        if registre is not None or titre_registre is not None:\n", "        if False:\n")],
     [R + "TestEnveloppeSansAjout::test_registre_hors_de_sa_generation_refuse"]),
    ("L3-16", "registre vide servi : section non omise", RQ,
     [("        if registre.taille == 0:\n", "        if False:\n")],
     [R + "TestEnveloppeSansAjout::test_registre_vide_section_omise"]),
    ("L3-17", "registre servi non exigé en pièce lue à son empreinte", RQ,
     [("        if not isinstance(registre, Piece):\n", "        if False:\n")],
     [R + "TestEnveloppeSansAjout::test_registre_hors_de_sa_generation_refuse"]),
    ("L3-18", "titre du registre sur plusieurs lignes admis", RQ,
     [("    if type(titre) is not str or not titre or titre != titre.strip() or \"\\n\" in titre or \"\\r\" in titre:\n",
       "    if type(titre) is not str or not titre:\n")],
     [R + "TestEnveloppeSansAjout::test_titre_du_registre_sur_une_ligne"]),
    ("L3-19", "génération non vérifiée", RQ,
     [("    if type(generation) is not int or generation not in (1, 2, 3):\n", "    if False:\n")],
     [R + "TestEnveloppeSansAjout::test_registre_hors_de_sa_generation_refuse",
      R + "TestFormeFicheServie::test_generation_de_l_epreuve_permise_sans_numero"]),
    # --- requete : forme de la fiche servie (mot 8) ---
    ("L3-20", "forme du noyau : fin de consigne non retirée", RQ,
     [("    servie = texte.rstrip()\n", "    servie = texte\n")],
     [R + "TestFormeFicheServie::test_portier_egal_a_la_forme_du_noyau",
      R + "TestFormeFicheServie::test_fin_de_consigne_retiree_par_la_forme_declaree_et_consignee"]),
    ("L3-21", "forme du noyau : titre de section changé", RQ,
     [("TITRE_FICHE = \"## La fiche\"", "TITRE_FICHE = \"## Fiche\"")],
     [R + "TestFormeFicheServie::test_portier_egal_a_la_forme_du_noyau"]),
    ("L3-22", "forme du noyau : indentation changée", RQ,
     [("INDENTATION_JSON = 1", "INDENTATION_JSON = 2")],
     [R + "TestFormeFicheServie::test_juge_egal_a_la_forme_du_noyau_identifiant_en_derniere_cle"]),
    ("L3-23", "identifiant servi au juge non vérifié (le jeton hexadécimal du noyau passerait)", RQ,
     [("        ident.decoder_octets(identifiant_servi, OCTETS_IDENTIFIANT_JUGE)\n", "        pass\n")],
     [R + "TestFormeFicheServie::test_identifiant_du_noyau_refuse_au_juge"]),
    ("L3-24", "identifiant servi au juge hors de la dernière clé", RQ,
     [("    objet[CLE_IDENTIFIANT_JUGE] = identifiant_servi\n",
       "    objet = {CLE_IDENTIFIANT_JUGE: identifiant_servi, **objet}\n")],
     [R + "TestFormeFicheServie::test_juge_egal_a_la_forme_du_noyau_identifiant_en_derniere_cle"]),
    ("L3-25", "fiche servie : douze champs non exigés", RQ,
     [("    if not isinstance(contenu, dict) or set(contenu) != set(CHAMPS_FICHE) or len(contenu) != len(CHAMPS_FICHE):\n",
       "    if not isinstance(contenu, dict):\n")],
     [R + "TestFormeFicheServie::test_fiche_hors_des_douze_champs_refusee"]),
    ("L3-26", "fiche servie : champs non exigés en chaînes", RQ,
     [("    if any(type(v) is not str for v in contenu.values()):\n", "    if False:\n")],
     [R + "TestFormeFicheServie::test_fiche_hors_des_douze_champs_refusee"]),
    ("L3-27", "identifiant de case non vérifié", RQ,
     [("        ident.rang_du_mot_de_case(identifiant)\n", "        pass\n")],
     [R + "TestFormeFicheServie::test_identifiant_de_case_verifie"]),
    # --- requete : arrêt n° 8 ---
    ("L3-28", "arrêt n° 8 retiré", RQ,
     [("    if taille > borne_octets:\n", "    if False:\n")],
     [R + "TestArret8Taille::test_un_octet_de_plus_refuse"]),
    ("L3-29", "arrêt n° 8 : requête égale à sa borne refusée", RQ,
     [("    if taille > borne_octets:\n", "    if taille >= borne_octets:\n")],
     [R + "TestArret8Taille::test_requete_egale_a_sa_borne_passe"]),
    ("L3-30", "arrêt n° 8 : borne non vérifiée", RQ,
     [("    if type(borne_octets) is not int or borne_octets <= 0:\n", "    if False:\n")],
     [R + "TestArret8Taille::test_borne_invalide_refusee"]),
    # --- requete : composition ---
    ("L3-31", "composition : empreinte des morceaux non vérifiée", RQ,
     [("            if len(morceau) != e.taille or _sha256(morceau) != e.sha256:\n", "            if False:\n")],
     [R + "TestEnveloppeSansAjout::test_composition_fausse_refusee"]),
    ("L3-32", "composition : séparateur hors de l'enveloppe admis", RQ,
     [("            if e.sorte == \"separateur\" and morceau != SEPARATEUR:\n", "            if False:\n")],
     [R + "TestEnveloppeSansAjout::test_composition_fausse_refusee"]),
    ("L3-33", "composition : pièce servie en partie admise", RQ,
     [("            if e.sorte == \"piece\" and (e.piece_sha256 != e.sha256 or e.piece_taille != e.taille):\n",
       "            if False:\n")],
     [R + "TestEnveloppeSansAjout::test_composition_fausse_refusee"]),
    ("L3-34", "requête hors UTF-8 admise", RQ,
     [("        try:\n            self.octets.decode(\"utf-8\")\n        except UnicodeDecodeError:\n"
       "            raise RequeteRefusee(\"requête qui n'est pas en UTF-8 valide\") from None\n", "        pass\n")],
     [R + "TestEnveloppeSansAjout::test_requete_hors_utf8_refusee"]),
    ("L3-35", "chaîne du noyau : octets non figés admis", RQ,
     [("    if type(octets) is not bytes:\n        raise RequeteRefusee(\"des octets figés\")\n",
       "    if False:\n        raise RequeteRefusee(\"des octets figés\")\n")],
     [R + "TestChaineDuNoyau::test_chaine_rend_les_octets"]),
    # --- journal : ajout seul ---
    ("L3-36", "réécriture d'une autre main non vue", JN,
     [("        if len(present) != self._taille or _sha256(present) != self._empreinte:\n", "        if False:\n")],
     [J + "TestAjoutSeul::test_reecriture_d_un_octet_refusee",
      J + "TestAjoutSeul::test_troncature_et_ajout_d_une_autre_main_refuses",
      J + "TestEnvoi::test_un_appel_sans_ligne_ne_part_pas"]),
    ("L3-37", "journal existant écrasé (R12)", JN,
     [("        if os.path.exists(self.chemin) or os.path.exists(self.chemin + \".sha256\"):\n", "        if False:\n")],
     [J + "TestAjoutSeul::test_journal_neuf_dans_le_dossier_de_sortie"]),
    ("L3-38", "écriture sans ajout seul (au début du fichier)", JN,
     [("os.O_WRONLY | os.O_APPEND", "os.O_WRONLY")],
     [J + "TestAjoutSeul::test_rangs_et_chainage", J + "TestAjoutSeul::test_ajout_seul_les_octets_ecrits_ne_changent_pas"]),
    ("L3-39", "journal scellé : ajout admis", JN,
     [("        if self._scelle:\n            raise JournalScelle(\"journal scellé : aucun ajout\")\n",
       "        if False:\n            raise JournalScelle(\"journal scellé : aucun ajout\")\n")],
     [J + "TestAjoutSeul::test_scelle_plus_aucun_ajout", J + "TestEnvoi::test_un_appel_sans_ligne_ne_part_pas"]),
    ("L3-40", "compagnon non comparé à la relecture", JN,
     [("        if attendu != _sha256(octets):\n", "        if False:\n")],
     [J + "TestAjoutSeul::test_compagnon_qui_ne_porte_pas_l_empreinte_refuse",
      J + "TestAjoutSeul::test_derniere_ligne_tenue_par_le_sceau"]),
    ("L3-41", "chaînage non vérifié à la relecture", JN,
     [("ligne.get(\"precedente\") != precedente", "False")],
     [J + "TestAjoutSeul::test_ligne_recalculee_d_une_autre_main_vue_a_la_relecture",
      J + "TestAjoutSeul::test_reecriture_d_un_octet_refusee"]),
    ("L3-42", "sceau exigé sans effet", JN,
     [("    if exiger_sceau and not os.path.exists(compagnon):\n", "    if False:\n")],
     [J + "TestAjoutSeul::test_derniere_ligne_tenue_par_le_sceau"]),
    # --- journal : envoi, non envoyé, non lancé ---
    ("L3-43", "ligne « envoi » écrite avant la garde de motifs", JN,
     [("        try:\n            rg = garde.garder_requete(requete.octets)\n",
       "        self._ajouter({\"evenement\": \"envoi\", \"role\": role, \"cle\": cle, \"sha256\": requete.sha256})\n"
       "        try:\n            rg = garde.garder_requete(requete.octets)\n")],
     [J + "TestEnvoi::test_refus_de_la_garde_ligne_non_envoye_et_texte_au_seul_journal"]),
    ("L3-44", "ligne « non envoyé » absente au refus de la garde", JN,
     [("            self.journaliser_non_envoye(arret=gm.NUMERO_ARRET, role=role, generation=requete.generation,\n"
       "                                        case=requete.identifiant_case, cle=cle, famille=arret.famille,\n"
       "                                        rang_motif=arret.rang, texte_trouve=arret.texte_trouve, sorte=requete.sorte,\n"
       "                                        sha256=requete.sha256, taille=requete.taille)\n", "            pass\n")],
     [J + "TestEnvoi::test_refus_de_la_garde_ligne_non_envoye_et_texte_au_seul_journal"]),
    ("L3-45", "texte trouvé absent de la ligne « non envoyé »", JN,
     [("texte_trouve=arret.texte_trouve, sorte=requete.sorte,", "sorte=requete.sorte,")],
     [J + "TestEnvoi::test_refus_de_la_garde_ligne_non_envoye_et_texte_au_seul_journal"]),
    ("L3-46", "garde du lot 2 non exigée", JN,
     [("        if not isinstance(garde, gm.GardeMotifs):\n", "        if False:\n")],
     [J + "TestEnvoi::test_garde_du_lot_2_exigee"]),
    ("L3-47", "garde qui lit d'autres octets admise", JN,
     [("        if not isinstance(rg, gm.RequeteGardee) or rg.sha256 != requete.sha256 or rg.taille != requete.taille \\\n"
       "                or rg.octets != requete.octets:\n", "        if False:\n")],
     [J + "TestEnvoi::test_garde_qui_lit_d_autres_octets_rien_ne_part"]),
    ("L3-48", "requête non assemblée admise", JN,
     [("        if not isinstance(requete, rq.RequeteAssemblee):\n            raise LigneRefusee(\"seule une requête assemblée",
       "        if False:\n            raise LigneRefusee(\"seule une requête assemblée")],
     [J + "TestEnvoi::test_seule_une_requete_assemblee_se_journalise"]),
    ("L3-49", "rejeu non comparé à l'empreinte du journal", JN,
     [("    if (ligne_envoi.get(\"sha256\"), ligne_envoi.get(\"taille\")) != (requete.sha256, requete.taille) \\\n",
       "    if False \\\n")],
     [J + "TestEnvoi::test_requete_changee_d_un_octet_apres_la_journalisation_refusee"]),
    ("L3-50", "deux lignes « non lancé » pour un envoi", JN,
     [("        if envoi.rang in self._non_lances:\n", "        if False:\n")],
     [J + "TestNonEnvoyeEtNonLance::test_non_lance_renvoie_a_sa_ligne_envoi"]),
    ("L3-51", "« non lancé » d'un autre journal admis", JN,
     [("        if not isinstance(envoi, EnvoiJournalise) or envoi.journal_id != self._numero \\\n"
       "                or self._envois.get(envoi.rang) != envoi.requete_gardee.sha256:\n",
       "        if not isinstance(envoi, EnvoiJournalise):\n")],
     [J + "TestNonEnvoyeEtNonLance::test_non_lance_d_un_autre_journal_refuse"]),
    ("L3-52", "liste fermée de la ligne « non envoyé » retirée", JN,
     [("        if inconnus:\n", "        if False:\n")],
     [J + "TestNonEnvoyeEtNonLance::test_non_envoye_liste_fermee_et_formes"]),
    ("L3-53", "génération d'une ligne non vérifiée", JN,
     [("    if type(valeur) is not int or valeur not in (1, 2, 3):\n        raise LigneRefusee(\"génération hors de 1 à 3\")\n",
       "    if False:\n        raise LigneRefusee(\"génération hors de 1 à 3\")\n")],
     [J + "TestNonEnvoyeEtNonLance::test_non_envoye_liste_fermee_et_formes"]),
    ("L3-54", "arrêt sans numéro ni nom admis", JN,
     [("    if (type(valeur) is int and valeur > 0) or (type(valeur) is str and valeur):\n", "    if True:\n")],
     [J + "TestNonEnvoyeEtNonLance::test_non_envoye_liste_fermee_et_formes"]),
    # --- journal : refus écrit (§ 2.13) ---
    ("L3-55", "refus écrit du portier rendu « passée » au lieu d'« au coffre »", JN,
     [("\"effet\": \"la fiche va au coffre, avec sa classe écrite\", \"classe\": \"au coffre\",",
       "\"effet\": \"la fiche va au coffre, avec sa classe écrite\", \"classe\": \"passée\",")],
     [J + "TestRefusEcrit::test_ce_que_rend_un_refus_ecrit_par_role"]),
    ("L3-56", "refus écrit d'une sorte inconnue admis", JN,
     [("        if sorte not in RENDUS_REFUS_ECRIT:\n", "        if False:\n")],
     [J + "TestRefusEcrit::test_sorte_inconnue_ou_champ_vide_refuse"]),
    ("L3-57", "coût nul non écrit sur un refus écrit", JN,
     [("\"garde\": _texte(\"garde\", garde), \"cause\": _texte(\"cause\", cause), \"cout_usd\": 0.0,",
       "\"garde\": _texte(\"garde\", garde), \"cause\": _texte(\"cause\", cause),")],
     [J + "TestRefusEcrit::test_ce_que_rend_un_refus_ecrit_par_role"]),
    ("L3-58", "refus écrit du proposeur compté comme un appel de M6", JN,
     [("\"compte\": \"cases non jouées\", \"fiche_rendue\": False, \"appel_compte_m6\": False},",
       "\"compte\": \"cases non jouées\", \"fiche_rendue\": False, \"appel_compte_m6\": True},")],
     [J + "TestRefusEcrit::test_ce_que_rend_un_refus_ecrit_par_role"]),
]

# Témoin du programme (R4) : une mutation inerte, qui ne touche aucune garde, doit survivre (code 0).
TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé", RQ,
                 [("La requête est une suite d'octets, rendue une fois", "La requête est une suite d'octets, faite une fois")],
                 [R + "TestPartieServie::test_partie_servie_a_l_octet", R + "TestArret8Taille::test_un_octet_de_plus_refuse"])


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
        print("usage : mutations_na_lot3_v1.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in FICHIERS:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-lot3-v1-")
    rendu = {"version": "journal-mutations-na-lot3-v1", "python": sys.version.split()[0], "fichiers": empreintes,
             "mutations": []}
    try:
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, TOUS)
        rendu["temoin_non_mute"] = {"essais": "les deux fichiers entiers", "code": code, "resume": resume,
                                    "passe": code == 0}
        for ident_m, nom, fichier, remplacements, essais in [TEMOIN_INERTE] + MUTATIONS:
            dossier = os.path.join(racine_tmp, ident_m)
            copier(dossier)
            chemin = os.path.join(dossier, fichier)
            with open(chemin, encoding="utf-8") as f:
                source = f.read()
            valide = True
            for ancien, nouveau in remplacements:
                if source.count(ancien) != 1:
                    valide = False
                    break
                source = source.replace(ancien, nouveau, 1)
            entree = {"id": ident_m, "garde_retiree": nom, "fichier": fichier, "essais": essais, "valide": valide}
            if valide:
                with open(chemin, "w", encoding="utf-8") as f:
                    f.write(source)
                code, resume = jouer(dossier, essais)
                entree.update({"code": code, "resume": resume, "tuee": code == 1})
            else:
                entree.update({"code": None, "resume": "texte cherché absent ou multiple", "tuee": False})
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
