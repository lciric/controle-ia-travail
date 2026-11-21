"""Mutations des lots 1 et 2 du véhicule NA-1, v5 : pour chaque garde, la garde retirée fait échouer son essai (R5 ; manière
de la v68, R68, § 4 : « trois mutations montrent que les essais ont des dents »).

v5 (décision de la mère R-4500) : la liste réelle n'est plus dans le paquet ; elle est lue sur la branche principale par
`liste_reelle_na_v5`. Les 109 mutations de la v4 sont rejouées sur les essais v5 ; N4-11 (liste réelle absente) vise
désormais le chemin de `liste_reelle_na_v5` et devient N4-11e ; une mutation neuve, N5-01, retire la vérification de
l'empreinte de la liste réelle. Les copies temporaires ne portent aucune copie de la liste.

v4 : les 98 mutations de la v3, visées sur `garde_motifs_na_v4`, `tirage_na_v4` et les essais v4 ; trois ont un texte que
la v4 change et portent le suffixe « d » (L2-05d, N3-01d, N3-02d). Plus les mutations neuves de la v4 : l'essai
d'extraction (N4-01, N4-02 : source absente ou autre, l'essai échoue, jamais ne saute), la liste d'apparence vide ramenée
à une espace, la normalisation des motifs sur leurs littéraux, la liste réelle absente (N4-03 à N4-11). Aucune variable
d'environnement n'est passée aux essais.

v3 : toutes les mutations de la v2 (42 du développeur, 35 du vérificateur), visées sur les fichiers v3 ; là où la v3 change
le texte cherché (normalisation réécrite, empreinte vérifiée en deux lieux), la mutation adaptée porte le suffixe « c » et
le dit (L2-01c à L2-06c, L2-09c, L2-11c, X-35c). Plus les mutations neuves des règles de la v3 (N3-01 à N3-21), jouées sur
les deux fichiers d'essais entiers.

v2 : les 42 mutations du développeur (v1), visées sur les fichiers v2, plus les 35 mutations du vérificateur (modèle S,
`mutations_verificateur.py`), jouées comme lui sur les deux fichiers d'essais entiers. Là où la v2 a changé le texte que
cherche une mutation, une mutation adaptée retire la même garde dans le texte neuf ; elle porte le suffixe « b » et le dit
(L2-10b, L2-15b, X-30b, X-32b).

Pour chaque mutation : une copie neuve des seuls fichiers des lots 1 et 2 dans un dossier temporaire ; un ou plusieurs
remplacements à texte exact dans un module (chaque texte cherché doit y être une fois exactement, sinon la mutation est dite
invalide) ; puis les essais nommés de cette garde, joués dans un processus à part. La mutation est « tuée » si et seulement
si pytest rend le code 1 (des essais échouent) ; tout autre code (essai qui passe, erreur de collecte) est un échec du
programme. Avant cela, les mêmes essais sont joués sur une copie non mutée : ils doivent passer (code 0).

Usage, depuis n'importe où : `python -B mutations_na_v5.py JOURNAL.json` (le journal ne doit pas exister : R12).
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
    "pole/identifiants_na_v1.py",
    "pole/tirage_na_v3.py",  # gardé : importé par les lots qui lisent la v3
    "pole/garde_motifs_na_v3.py",  # gardé : importé par l'extraction et le contrôle contre regex (constantes inchangées)
    "pole/tirage_na_v4.py",
    "pole/garde_motifs_na_v4.py",
    "pole/extraire_ignorables_unicode_na_v1.py",
    "pole/ignorables-unicode-15.1.0-na-v1.json",
    "essais/aides_na_v4.py",
    "essais/liste-motifs-essai-na-v1.json",
    "essais/controle_ignorables_regex_na_v3.py",
    "essais/sonde_version_unicode_na_v3.py",
    "essais/liste_reelle_na_v5.py",
    "essais/test_na_v4_tirage.py",
    "essais/test_na_v5_garde_motifs.py",
    "essais/source-unicode-15.1.0/DerivedCoreProperties.txt",
)

TOUS = ["essais/test_na_v4_tirage.py", "essais/test_na_v5_garde_motifs.py"]
T = "essais/test_na_v4_tirage.py::"
G = "essais/test_na_v5_garde_motifs.py::"
TG = "essais/test_na_v5_garde_motifs.py"
AI = "essais/aides_na_v4.py"
LRM = "essais/liste_reelle_na_v5.py"
TI = "pole/tirage_na_v4.py"
ID = "pole/identifiants_na_v1.py"
GM = "pole/garde_motifs_na_v4.py"
EX = "pole/extraire_ignorables_unicode_na_v1.py"
CR = "essais/controle_ignorables_regex_na_v3.py"

MUTATIONS = [
    # --- lot 1 : tirage ---
    ("L1-01", "racine non vérifiée", TI,
     [("    if type(racine) is not int or racine != racine_attendue:\n", "    if False:\n")],
     [T + "TestRacineEtNumpy::test_racine_recalculee_sur_une_autre_empreinte_refusee"]),
    ("L1-02", "numpy sous 1.25 admis", TI,
     [("    if (int(m.group(1)), int(m.group(2))) < NUMPY_MINIMUM:\n", "    if False:\n")],
     [T + "TestRacineEtNumpy::test_numpy_sous_1_25_refuse"]),
    ("L1-03", "empreinte du gabarit non vérifiée", TI,
     [("    if sha != empreinte_attendue:\n", "    if False:\n")],
     [T + "TestLegende::test_empreinte_differente_refusee",
      T + "TestProgramme::test_gabarit_d_une_autre_empreinte_refuse_sans_ecriture"]),
    ("L1-04", "question admise par son nom", TI,
     [("    if nom is not None and any(", "    if False and any(")],
     [T + "TestLegende::test_question_refusee_par_son_nom"]),
    ("L1-05", "empreinte de la question admise", TI,
     [("    if sha in EMPREINTES_INTERDITES:\n", "    if False:\n")],
     [T + "TestLegende::test_empreinte_de_la_question_refusee"]),
    ("L1-06", "arrêt n° 10 : famille tenue à l'écart non exclue", TI,
     [("        if c[0] == famille:\n", "        if False:\n")],
     [T + "TestArretDisjonction::test_case_de_la_famille_plantee"]),
    ("L1-07", "arrêt n° 10 : case déjà servie admise", TI,
     [("        if c in deja:\n", "        if False:\n")],
     [T + "TestArretDisjonction::test_case_deja_servie_plantee"]),
    ("L1-08", "arrêt n° 10 : cases à servir non comparées au tirage scellé", TI,
     [("    if cases != du_tirage:\n", "    if False:\n")],
     [T + "TestArretDisjonction::test_cases_a_servir_qui_ne_sont_pas_celles_du_tirage"]),
    ("L1-09", "clé n° 30 : tirée hors des seules cases de sabotage", TI,
     [("        candidates = [c for c in servies if c[axe_s] == rang_s]\n", "        candidates = list(servies)\n")],
     [T + "TestTirage::test_cle_30_cas_sain",
      T + "TestTirage::test_cle_30_aucune_case_de_sabotage_rien_n_est_tire"]),
    ("L1-10", "clé n° 30 : tirée même sans case (« aucune » retiré)", TI,
     [("        if n == 0:\n", "        if False:\n")],
     [T + "TestTirage::test_cle_30_aucune_case_de_sabotage_rien_n_est_tire"]),
    ("L1-11", "second tirage admis", TI,
     [("        if cle in self._tirees:\n", "        if False:\n"),
      ("        if CLE_CASE_MODE_TENU_A_L_ECART in self._tirees:\n", "        if False:\n")],
     [T + "TestTirage::test_cle_30_second_tirage_refuse"]),
    ("L1-12", "clé n° 40 : mot refusé par la garde, tirage non arrêté", TI,
     [("            if constat is not None:\n                raise TirageArreteMotRefuse",
       "            if False:\n                raise TirageArreteMotRefuse")],
     [T + "TestTirage::test_cle_40_mot_refuse_arrete_le_tirage_sans_second_tirage"]),
    ("L1-13", "clé n° 40 : garde de motifs non exigée", TI,
     [("        if garde is None or not hasattr(garde, \"examiner\"):\n", "        if False:\n")],
     [T + "TestTirage::test_garde_exigee"]),
    ("L1-14", "ligne de case : valeurs non comparées à la légende", TI,
     [("        if parts[1 + a] != legende[\"valeurs\"][a][triplet[a]]:\n", "        if False:\n")],
     [T + "TestLigneDeCase::test_valeur_qui_differe_d_un_octet"]),
    ("L1-15", "ligne de case : suite hexadécimale non cherchée", TI,
     [("    if ident.porte_suite_hexadecimale(ligne):\n", "    if False:\n")],
     [T + "TestLigneDeCase::test_huit_caracteres_hexadecimaux_de_suite"]),
    ("L1-16", "ligne de case : chiffre non cherché", TI,
     [("    if re.search(r\"[0-9]\", ligne):\n", "    if False:\n")],
     [T + "TestLigneDeCase::test_identifiant_numerote_sur_un_total"]),
    ("L1-17", "ligne de case : identifiant non décodé", TI,
     [("        ident.rang_du_mot_de_case(identifiant)\n", "        pass\n")],
     [T + "TestLigneDeCase::test_identifiant_numerote_sur_un_total"]),
    ("L1-18", "ligne de case : identifiants non distincts", TI,
     [("        if identifiant in vus:\n", "        if False:\n")],
     [T + "TestLigneDeCase::test_identifiants_distincts"]),
    ("L1-19", "ligne de case : borne en octets retirée", TI,
     [("    if len(ligne.encode(\"utf-8\")) > BORNE_LIGNE_OCTETS:\n", "    if False:\n")],
     [T + "TestLigneDeCase::test_borne_en_octets"]),
    ("L1-20", "C1 non vérifié", TI,
     [("    if not all(c1.values()):\n", "    if False:\n")],
     [T + "TestC1::test_case_servie_deux_fois", T + "TestC1::test_trente_deux_cases",
      T + "TestC1::test_case_de_la_famille_servie"]),
    # --- lot 1 : réencodage ---
    ("L1-21", "ordre des octets inversé", ID,
     [("    valeur = int.from_bytes(bytes(octets), \"big\")", "    valeur = int.from_bytes(bytes(octets), \"little\")")],
     [T + "TestIdentifiants::test_vecteurs_connus_et_ordre_des_octets",
      T + "TestIdentifiants::test_aller_retour_sur_un_echantillon_tire"]),
    ("L1-22", "décodage : borne retirée", ID,
     [("    if valeur >= 256 ** n_octets:\n", "    if False:\n")],
     [T + "TestIdentifiants::test_refus_entier_au_dela_de_la_borne"]),
    ("L1-23", "décodage : alphabet non vérifié (lettre fautive prise pour la syllabe de rang 0)", ID,
     [("            raise MotRefuse(\"hors alphabet\")\n        valeur = valeur * BASE + RANG_SYLLABE[syllabe]",
       "            pass\n        valeur = valeur * BASE + RANG_SYLLABE.get(syllabe, 0)")],
     [T + "TestIdentifiants::test_refus_hors_alphabet"]),
    ("L1-24", "décodage : longueur non vérifiée", ID,
     [("    if len(mot) != 2 * n_syllabes:\n", "    if False:\n")],
     [T + "TestIdentifiants::test_refus_mauvaise_longueur"]),
    ("L1-25", "jeton du noyau : forme non vérifiée", ID,
     [("    if not jeton.startswith(prefixe) or len(corps) != 2 * n_octets or re.fullmatch(r\"[0-9a-f]+\", corps) is None:\n",
       "    if False:\n")],
     [T + "TestIdentifiants::test_reencoder_un_jeton_du_noyau"]),
    # --- lot 2 : garde de motifs ---
    ("L2-01c", "normalisation retirée (texte v3)", GM,
     [("        t = _ESPACES_MULTIPLES.sub(\" \", t)\n        return t\n", "        return texte\n")],
     [G + "TestNormalisation::test_formes_ramenees",
      G + "TestArret16ParFamille::test_famille_composition_et_tenue_forme_ramenee"]),
    ("L2-02c", "invisibles non retirés (texte v3 : Cf, ignorables et apparence vide ensemble)", GM,
     [("        return \"\".join(ch for ch in t if ord(ch) not in self._retires and unicodedata.category(ch) != \"Cf\")\n",
       "        return t\n")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_forme_ramenee"]),
    ("L2-03c", "forme de compatibilité retirée (texte v3)", GM,
     [("        t = unicodedata.normalize(\"NFKC\", t)\n        t = t.casefold()\n        t = unicodedata.normalize(\"NFKC\", t)\n",
       "        t = t.casefold()\n")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_forme_ramenee"]),
    ("L2-04c", "casse non repliée (texte v3)", GM,
     [("        t = t.casefold()\n", "        pass\n")],
     [G + "TestNormalisation::test_formes_ramenees"]),
    ("L2-05d", "tirets, soulignements et apparence vide non ramenés (texte v4)", GM,
     [("        t = \"\".join(\" \" if (unicodedata.category(ch) in (\"Pd\", \"Pc\") or ord(ch) in self._en_espace) else ch for ch in t)\n",
       "        pass\n")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_forme_ramenee"]),
    ("L2-06c", "espaces non ramenés (texte v3 : `str.isspace()`)", GM,
     [("        t = \"\".join(\" \" if ch.isspace() else ch for ch in t)\n", "        pass\n")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_forme_ramenee"]),
    ("L2-07", "seconde famille non lue", GM,
     [("        for _nom, motifs in self.liste.familles:\n", "        for _nom, motifs in self.liste.familles[:1]:\n")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_en_clair"]),
    ("L2-08", "première famille non lue", GM,
     [("        for _nom, motifs in self.liste.familles:\n", "        for _nom, motifs in self.liste.familles[1:]:\n")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_en_clair"]),
    ("L2-09c", "témoins positifs non vérifiés (texte v3)", GM,
     [("            if motif.chercher(self.normaliser(motif.temoin_positif)) is None:\n", "            if False:\n")],
     [G + "TestTemoinsPositifs::test_un_motif_qui_ne_mord_pas_refuse_le_depart",
      G + "TestTemoinsPositifs::test_temoins_rejoues_a_chaque_depart"]),
    ("L2-10b", "copie retirée : la garde rend le tampon de l'appelant (texte v2 : commentaire sur la ligne)", GM,
     [("        octets = bytes(requete)  # une seule lecture", "        octets = requete  # une seule lecture"),
      ("        if type(self.octets) is not bytes:\n", "        if False:\n")],
     [G + "TestDernierPointAvantEnvoi::test_aucun_octet_change_apres_la_garde"]),
    ("L2-11c", "empreinte de la liste non vérifiée (texte v3 : deux lieux, celui de la liste)", GM,
     [("    if type(empreinte_attendue) is not str or sha != empreinte_attendue:\n        raise ListeMotifsRefusee(",
       "    if False:\n        raise ListeMotifsRefusee(")],
     [G + "TestFormatDeLaListe::test_empreinte_differente_refusee"]),
    ("L2-12", "expression à accord vide admise", GM,
     [("            if m.end() == m.start():\n", "            if False:\n")],
     [G + "TestFormatDeLaListe::test_expression_invalide_ou_accord_vide"]),
    ("L2-13", "famille vide admise", GM,
     [("        if not isinstance(motifs, list) or not motifs:\n", "        if not isinstance(motifs, list):\n")],
     [G + "TestFormatDeLaListe::test_famille_vide_refusee"]),
    ("L2-14", "texte trouvé recopié dans le message de l'arrêt", GM,
     [("f\"rang {rang} ; envoi refusé\")", "f\"rang {rang} ; envoi refusé ; {texte_trouve}\")")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_en_clair",
      G + "TestDernierPointAvantEnvoi::test_une_requete_qui_porte_un_motif_refusee_avant_l_envoi"]),
    ("L2-15b", "envoi avant la ligne de journal (texte v2 : sans la comparaison à soi-même)", GM,
     [("    journal({**meta, \"evenement\": \"envoi\", \"taille\": rg.taille, \"sha256\": rg.sha256})\n"
       "    return envoyer(rg.octets)\n",
       "    resultat = envoyer(rg.octets)\n"
       "    journal({**meta, \"evenement\": \"envoi\", \"taille\": rg.taille, \"sha256\": rg.sha256})\n"
       "    return resultat\n")],
     [G + "TestDernierPointAvantEnvoi::test_ligne_de_journal_qui_ne_s_ecrit_pas_rien_ne_part"]),
    ("L2-16", "ligne « non envoyé » absente du journal", GM,
     [("        journal({**meta, \"evenement\": \"non envoyé\", \"arret\": NUMERO_ARRET, \"famille\": arret.famille,\n"
       "                 \"rang\": arret.rang, \"texte_trouve\": arret.texte_trouve})\n", "")],
     [G + "TestDernierPointAvantEnvoi::test_une_requete_qui_porte_un_motif_refusee_avant_l_envoi"]),
    ("L2-17", "requête non examinée au dernier point", GM,
     [("        self.garder_texte(texte)\n        return RequeteGardee", "        return RequeteGardee")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_en_clair",
      G + "TestDernierPointAvantEnvoi::test_une_requete_qui_porte_un_motif_refusee_avant_l_envoi"]),
]

# Les 35 mutations du vérificateur (modèle S), à son texte, jouées sur les deux fichiers d'essais entiers. Deux ont un
# texte que la v2 change : X-30 (contrôle retiré du chemin d'envoi : la mutation est sans objet, X-30b retire la vraie
# égalité, celle de `verifier_avant_envoi`) ; X-32 (l'empreinte est prise à la copie : X-32b). Les 33 autres sont à la
# lettre du vérificateur (X-35 : le source porte le caractère du signe moins lui-même ; un premier essai, avec une adaptation X-35b qui cherchait
# l'échappement `\u2212`, l'a dite invalide).
_V = [
    ("X-01", "lire_legende : table unique non exigée", TI,
     [("    if len(entetes) != 1:\n", "    if False:\n")]),
    ("X-02", "lire_legende : valeur 5 'autre' non vérifiée", TI,
     [("    if valeurs[a][r] != v:\n", "    if False:\n")]),
    ("X-03", "lire_legende : menace sabotage non vérifiée", TI,
     [("    if not valeurs[axe_s][rang_s].startswith(PREFIXE_SABOTAGE):\n", "    if False:\n")]),
    ("X-04", "lire_legende : nombre de valeurs non vérifié", TI,
     [("        if len(vals) != TAILLES_AXES[k] or", "        if False or")]),
    ("X-05", "sortie : contrôle des lignes de case non joué dans le tirage", TI,
     [("        controler_lignes_de_case(lignes_du_tirage(sortie), sortie[\"legende\"])\n", "        pass\n")]),
    ("X-06", "sortie : C1 non joué dans le tirage", TI,
     [("        sortie[\"controles_C1\"] = controles_c1(sortie)\n", "        sortie[\"controles_C1\"] = {}\n")]),
    ("X-07", "ligne de case : fin de ligne non refusée", TI,
     [("    if \"\\n\" in ligne or \"\\r\" in ligne:\n", "    if False:\n")]),
    ("X-08", "ligne de case : préfixe non vérifié", TI,
     [("    if not ligne.startswith(PREFIXE_LIGNE):\n", "    if False:\n")]),
    ("X-09", "arrêt n° 10 : case hors des 120 admise", TI,
     [("        if c not in toutes:\n", "        if False:\n")]),
    ("X-10", "arrêt n° 10 : case en double admise", TI,
     [("        if c in vues:\n", "        if False:\n")]),
    ("X-11", "arrêt n° 10 : génération hors 1-3 admise", TI,
     [("    if generation not in (1, 2, 3):\n", "    if False:\n")]),
    ("X-12", "tirage : cases tirées non retirées avant la génération suivante", TI,
     [("            restantes = [c for c in restantes if c not in pris]\n", "            pass\n")]),
    ("X-13", "tirage : famille non exclue des restantes", TI,
     [("        restantes = [c for c in cases_canoniques() if c[0] != self.famille]\n",
       "        restantes = cases_canoniques()\n")]),
    ("X-14", "tirage : clé 40 tirée avec remise", TI,
     [("choice(ident.MOTS_DE_CASE, size=120, replace=False)", "choice(ident.MOTS_DE_CASE, size=120, replace=True)")]),
    ("X-15", "tirage : clé 40 prise sur une autre clé (41)", TI,
     [("CLE_IDENTIFIANTS = 40", "CLE_IDENTIFIANTS = 41")]),
    ("X-16", "tirage : clé 30 prise sur la clé 31", TI,
     [("CLE_CASE_MODE_TENU_A_L_ECART = 30", "CLE_CASE_MODE_TENU_A_L_ECART = 31")]),
    ("X-17", "tirage : racine écrite changée d'un chiffre", TI,
     [("0x2cf2aae035beef43e999e3cd8b0fb7ba", "0x2cf2aae035beef43e999e3cd8b0fb7bb")]),
    ("X-18", "tirage : réserve non triée (ordre non canonique)", TI,
     [("        self.reserve = restantes\n", "        self.reserve = list(reversed(restantes))\n")]),
    ("X-19", "tirage : sortie non triée (clés non triées)", TI,
     [("json.dumps(sortie, ensure_ascii=False, sort_keys=True, indent=1)",
       "json.dumps(sortie, ensure_ascii=False, sort_keys=False, indent=1)")]),
    ("X-20", "main : manifeste écrasable", TI,
     [("    for chemin in (a.sortie, a.manifeste):\n", "    for chemin in (a.sortie,):\n")]),
    ("X-21", "identifiants : alphabet (consonne hexadécimale 'f' à la place de 'g')", ID,
     [("CONSONNES = \"gjklmnprstvz\"", "CONSONNES = \"fjklmnprstvz\"")]),
    ("X-22", "identifiants : longueur fixe non complétée à gauche (zéro)", ID,
     [("    for _ in range(n_syllabes):\n        reste, r = divmod(reste, BASE)\n        chiffres.append(r)\n",
       "    while True:\n        reste, r = divmod(reste, BASE)\n        chiffres.append(r)\n        if reste == 0:\n"
       "            break\n")]),
    ("X-23", "identifiants : encoder_identifiant_fiche sans contrôle de longueur", ID,
     [("    if len(octets) != 6:\n", "    if False:\n")]),
    ("X-24", "identifiants : suite hexadécimale non détectée (longueur 8 -> 80)", ID,
     [("_HEXA = re.compile(r\"[0-9A-Fa-f]{8,}\")", "_HEXA = re.compile(r\"[0-9A-Fa-f]{80,}\")")]),
    ("X-25", "garde : clés en double admises", GM,
     [("        if k in d:\n", "        if False:\n")]),
    ("X-26", "garde : rangs sans trou non exigés", GM,
     [("            if type(m[\"rang\"]) is not int or m[\"rang\"] != i:\n", "            if False:\n")]),
    ("X-27", "garde : clés d'un motif non exactes", GM,
     [("            if not isinstance(m, dict) or set(m) != {\"rang\", \"type\", \"motif\", \"temoin_positif\"}:\n",
       "            if not isinstance(m, dict):\n")]),
    ("X-28", "garde : nom de famille non vérifié", GM,
     [("        if fam[\"nom\"] != attendu:\n", "        if False:\n")]),
    ("X-29", "garde : requête non UTF-8 non refusée (remplacement)", GM,
     [("        try:\n            texte = octets.decode(\"utf-8\")\n        except UnicodeDecodeError:\n"
       "            raise RequeteIllisible(\"requête qui n'est pas en UTF-8 valide : refusée\") from None\n",
       "        texte = octets.decode(\"utf-8\", errors=\"replace\")\n")]),
    ("X-30b", "garde : l'égalité de verifier_avant_envoi retirée (X-30 sans objet : contrôle à soi-même retiré en v2)",
     GM, [("    if hashlib.sha256(bytes(octets_a_envoyer)).hexdigest() != requete_gardee.sha256:\n", "    if False:\n")]),
    ("X-31", "garde : envoi de l'octet de l'appelant et non de la copie gardée", GM,
     [("    return envoyer(rg.octets)", "    return envoyer(requete)")]),
    ("X-32b", "garde : empreinte calculée sur une seconde lecture de l'appelant et non sur la copie", GM,
     [("        empreinte = hashlib.sha256(octets).hexdigest()", "        empreinte = hashlib.sha256(bytes(requete)).hexdigest()")]),
    ("X-33", "garde : ordre des familles inversé au premier constat", GM,
     [("        for _nom, motifs in self.liste.familles:\n            yield from motifs",
       "        for _nom, motifs in reversed(self.liste.familles):\n            yield from motifs")]),
    ("X-34", "garde : texte trouvé du texte non normalisé (rend la requête entière)", GM,
     [("                return Constat(motif.famille, motif.rang, trouve)",
       "                return Constat(motif.famille, motif.rang, texte)")]),
    ("X-35c", "garde : signe moins non ramené (texte v3 : constante SIGNE_MOINS)", GM,
     [("SIGNE_MOINS = 0x2212", "SIGNE_MOINS = -1")]),
]
VERIFICATEUR = [(i, n, f, r, TOUS) for i, n, f, r in _V]

# Mutations neuves des règles de la v3 (mère, 08:54Z à 08:59Z), jouées sur les deux fichiers d'essais entiers.
_N3 = [
    ("N3-01d", "ignorables par défaut non retirés (texte v4)", GM,
     [("        self._retires = donnees.points  # v4", "        self._retires = frozenset()  # v4")]),
    ("N3-02d", "liste d'apparence vide non ramenée à une espace (texte v4)", GM,
     [("        self._en_espace = frozenset(APPARENCE_VIDE) | {SIGNE_MOINS}\n",
       "        self._en_espace = frozenset({SIGNE_MOINS})\n")]),
    ("N3-03", "catégorie Cf non retirée (ignorables et liste seuls)", GM,
     [(" and unicodedata.category(ch) != \"Cf\")\n", ")\n")]),
    ("N3-04", "soulignement (Pc) non ramené", GM,
     [("unicodedata.category(ch) in (\"Pd\", \"Pc\")", "unicodedata.category(ch) in (\"Pd\",)")]),
    ("N3-05", "tiret (Pd) non ramené", GM,
     [("unicodedata.category(ch) in (\"Pd\", \"Pc\")", "unicodedata.category(ch) in (\"Pc\",)")]),
    ("N3-06", "suites d'espaces non réduites", GM,
     [("        t = _ESPACES_MULTIPLES.sub(\" \", t)\n", "        pass\n")]),
    ("N3-07", "données vides admises", GM,
     [("    if obj[\"source\"] is None or obj[\"plages\"] is None:\n", "    if False:\n")]),
    ("N3-08", "version des données non comparée (à l'attendue et à l'interpréteur)", GM,
     [("    if obj[\"version_unicode\"] != VERSION_UNICODE_ATTENDUE:\n", "    if False:\n"),
      ("    verifier_version_interprete(obj[\"version_unicode\"])\n", "    pass\n")]),
    ("N3-09", "égalité des versions d'Unicode non vérifiée", GM,
     [("    if type(version_donnees) is not str or version_donnees != v:\n", "    if False:\n")]),
    ("N3-10", "empreinte des données non vérifiée", GM,
     [("    if type(empreinte_attendue) is not str or sha != empreinte_attendue:\n        raise DonneesIgnorablesRefusees(",
       "    if False:\n        raise DonneesIgnorablesRefusees(")]),
    ("N3-11", "plages chevauchantes ou non triées admises", GM,
     [("or not 0 <= p[0] <= p[1] <= 0x10FFFF or p[0] <= fin_prec):", "or not 0 <= p[0] <= p[1] <= 0x10FFFF):")]),
    ("N3-12", "total des données non vérifié", GM,
     [("    if type(obj[\"total\"]) is not int or obj[\"total\"] != len(points):\n", "    if False:\n")]),
    ("N3-13", "normaliseur non exigé pour lire la liste", GM,
     [("    if not isinstance(normaliseur, Normaliseur):\n        raise DonneesIgnorablesRefusees(\"la liste",
       "    if False:\n        raise DonneesIgnorablesRefusees(\"la liste")]),
    ("N3-14", "motif littéral blanc admis", GM,
     [("        if not forme.strip():\n", "        if not forme:\n")]),
    ("N3-15", "extraction : version du fichier non vérifiée", EX,
     [("    if version != gm.VERSION_UNICODE_ATTENDUE:\n", "    if False:\n"),
      ("        gm.verifier_version_interprete(version, version_interprete)\n", "        pass\n")]),
    ("N3-16", "extraction : total écrit non comparé", EX,
     [("    if total_ecrit is None or total_ecrit != total:\n", "    if False:\n")]),
    ("N3-17", "extraction : propriété non filtrée", EX,
     [("        if d is None or d.group(3) != gm.PROPRIETE:\n", "        if d is None:\n")]),
    ("N3-18", "extraction : ordre des plages non exigé", EX,
     [("        if not 0 <= debut <= fin <= 0x10FFFF or debut <= fin_prec:\n",
       "        if not 0 <= debut <= fin <= 0x10FFFF:\n")]),
    ("N3-19", "extraction : empreinte de la source non vérifiée", EX,
     [("    if sha != empreinte_attendue:\n        raise ExtractionRefusee(", "    if False:\n        raise ExtractionRefusee(")]),
    ("N3-20", "contrôle contre regex : écarts non comptés", CR,
     [("    ecarts = set(points_donnees) ^ set(rx)\n", "    ecarts = set()\n")]),
    ("N3-21", "normaliseur construit sans vérifier la version de l'interpréteur ni le type des données", GM,
     [("        if not isinstance(donnees, DonneesIgnorables):\n            raise", "        if False:\n            raise")]),
]
NEUVES = [(i, n, f, r, TOUS) for i, n, f, r in _N3]

# Mutations neuves de la v4 : elles touchent l'essai d'extraction lui-même. Une source absente doit faire échouer l'essai,
# non le faire sauter (la v3 sautait : N4-01 y aurait survécu) ; une source autre doit être refusée par son empreinte.
_N4 = [
    ("N4-01", "source Unicode absente du paquet (chemin qui ne mène à rien) : l'essai doit échouer, non sauter", TG,
     [("SOURCE_UNICODE_DANS_LE_PAQUET = os.path.join(ICI, \"source-unicode-15.1.0\", \"DerivedCoreProperties.txt\")",
       "SOURCE_UNICODE_DANS_LE_PAQUET = os.path.join(ICI, \"source-absente\", \"DerivedCoreProperties.txt\")")]),
    ("N4-02", "essai d'extraction lu sur un autre fichier que la source (le gabarit des données) : refus par l'empreinte",
     TG, [("SOURCE_UNICODE_DANS_LE_PAQUET = os.path.join(ICI, \"source-unicode-15.1.0\", \"DerivedCoreProperties.txt\")",
           "SOURCE_UNICODE_DANS_LE_PAQUET = A.CHEMIN_DONNEES")]),
    ("N4-03", "motifs « expression_reguliere » non normalisés (compilés tels qu'écrits)", GM,
     [("        forme = re.compile(normaliseur.normaliser_expression(motif))", "        forme = re.compile(motif)")]),
    ("N4-04", "littéraux normalisés non échappés", GM,
     [("                rendu.append(re.escape(self.normaliser(corps)))", "                rendu.append(self.normaliser(corps))")]),
    ("N4-05", "littéral quantifié devenu plusieurs caractères non groupé", GM,
     [("rendu.append(re.escape(dernier) if len(dernier) == 1 else \"(?:\" + re.escape(dernier) + \")\")",
       "rendu.append(re.escape(dernier))")]),
    ("N4-06", "groupe spécial (?…) admis", GM,
     [("            elif p.startswith(\"(?\", i):\n                raise", "            elif False:\n                raise")]),
    ("N4-07", "échappement alphanumérique inconnu (renvoi, nom) admis comme littéral", GM,
     [("            elif d.isascii() and d.isalnum():\n                raise", "            elif False:\n                raise")]),
    ("N4-08", "littéral quantifié qui disparaît admis", GM,
     [("                if not dernier:\n                    raise", "                if False:\n                    raise")]),
    ("N4-09", "liste d'apparence vide retirée (règle v3) au lieu d'être ramenée à une espace", GM,
     [("        self._retires = donnees.points  # v4", "        self._retires = donnees.points | frozenset(APPARENCE_VIDE)  # v4")]),
    ("N4-10", "expression écrite non validée telle quelle avant sa normalisation", GM,
     [("        re.compile(motif)  # l'expression écrite", "        pass  # l'expression écrite")]),
    ("N4-11e", "liste réelle absente de la branche principale (chemin qui ne mène à rien) : les essais doivent échouer, "
     "non sauter (texte v5 : `liste_reelle_na_v5`)", LRM,
     [("CHEMIN_DEPOT = \"docs/notes/ideation-seuil-moniteurs-v1/", "CHEMIN_DEPOT = \"docs/notes/chemin-absent-v1/")]),
]
NEUVES_V4 = [(i, n, f, r, TOUS) for i, n, f, r in _N4]

_N5 = [
    ("N5-01", "empreinte de la liste réelle non vérifiée", LRM,
     [("    if hashlib.sha256(octets).hexdigest() != EMPREINTE:\n", "    if False:\n")]),
]
NEUVES_V5 = [(i, n, f, r, TOUS) for i, n, f, r in _N5]

# Témoin du programme (R4) : une mutation inerte, qui ne touche aucune garde, doit survivre (code 0). Sinon le programme
# dirait « tuée » sans discerner.
TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé", TI,
                 [("Une seule sortie, octets déterministes", "Une seule sortie, des octets déterministes")],
                 [T + "TestTirage::test_cle_30_cas_sain", T + "TestLigneDeCase::test_valeur_qui_differe_d_un_octet"])


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
        print("usage : mutations_na_v5.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in FICHIERS:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-v5-")
    rendu = {"version": "journal-mutations-na-v5", "python": sys.version.split()[0], "fichiers": empreintes,
             "mutations": []}
    origine = {m[0]: "développeur" for m in MUTATIONS}
    origine.update({m[0]: "vérificateur" for m in VERIFICATEUR})
    origine.update({m[0]: "neuve v3" for m in NEUVES})
    origine.update({m[0]: "neuve v4" for m in NEUVES_V4})
    origine.update({m[0]: "neuve v5" for m in NEUVES_V5})
    try:
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, TOUS)
        rendu["temoin_non_mute"] = {"essais": "les deux fichiers entiers", "code": code, "resume": resume,
                                    "passe": code == 0}
        for ident_m, nom, fichier, remplacements, essais in ([TEMOIN_INERTE] + MUTATIONS + VERIFICATEUR + NEUVES
                                                              + NEUVES_V4 + NEUVES_V5):
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
            entree = {"id": ident_m, "origine": origine.get(ident_m, "témoin"), "garde_retiree": nom,
                      "fichier": fichier, "essais": essais, "valide": valide}
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
    par_origine = {o: {"mutations": sum(1 for m in rendu["mutations"] if m["origine"] == o),
                       "tuees": sum(1 for m in rendu["mutations"] if m["origine"] == o and m["tuee"])}
                   for o in ("développeur", "vérificateur", "neuve v3", "neuve v4", "neuve v5")}
    rendu["bilan"] = {"mutations": n, "tuees": tuees, "par_origine": par_origine,
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
