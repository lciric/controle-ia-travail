"""Mutations du lot 4 v3 du véhicule NA-1 : pour chaque garde neuve (règle de repli, adaptateur direct, n° 31, n° 32,
n° 34, A1 à A7, N2), la garde retirée fait échouer son essai (R5 ; manière du lot 4 v1, `mutations_na_lot4_v1.py`).

Pour chaque mutation : une copie neuve, dans un dossier temporaire, du dossier `pole/` de la copie de l'orchestrateur et
des seuls fichiers d'essais dont les essais du lot 4 v3 ont besoin ; un ou plusieurs remplacements à texte exact (chaque
texte cherché doit y être une fois exactement, sinon la mutation est dite invalide) ; puis les essais nommés, joués dans un
processus à part. « Tuée » si et seulement si pytest rend le code 1. Avant cela, les deux fichiers d'essais entiers
passent sur une copie non mutée (code 0), et un témoin inerte survit. La liste réelle des motifs n'est ni copiée ni lue.

Usage : `python -B mutations_na_lot4_v3.py JOURNAL.json` (le journal ne doit pas exister : R12). Aucun réseau hors de la
boucle locale, aucune clé ; les copies temporaires sont retirées en fin de programme.
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

ESSAIS_COPIES = (
    "essais/__init__.py", "essais/conftest.py", "essais/aides.py", "essais/aides_v53.py", "essais/aides_v54.py",
    "essais/aides_v55.py", "essais/aides_v56.py", "essais/aides_na_v4.py", "essais/liste-motifs-essai-na-v1.json",
    "essais/aides_na_lot3_v3.py", "essais/aides_na_lot4_v1.py", "essais/aides_na_lot4_v3.py",
    "essais/test_na_v3_appel_garde.py", "essais/test_na_v2_adaptateur_claude_direct.py",
)
AG = "pole/appel_garde_na_v3.py"
AD = "pole/adaptateur_claude_direct_na_v2.py"
MODULES = (AG, AD)
TOUS = ["essais/test_na_v3_appel_garde.py", "essais/test_na_v2_adaptateur_claude_direct.py"]
T = "essais/test_na_v3_appel_garde.py::"
D = "essais/test_na_v2_adaptateur_claude_direct.py::"

MUTATIONS = [
    # --- la chaîne de repli ---
    ("R-01", "chaîne coupée au premier modèle de repli", AG,
     [("            return (modele,) + self.modeles_repli\n", "            return (modele,) + self.modeles_repli[:1]\n")],
     [T + "TestRepliCasSain::test_second_repli_servi"]),
    ("R-02", "aucun repli", AG, [("                if not dernier:\n", "                if False:\n")],
     [T + "TestRepliCasSain::test_premier_repli_servi"]),
    ("R-03", "repli sans fin (le troisième refus rejoue)", AG,
     [("                if not dernier:\n", "                if True:\n")],
     [T + "TestRepliArtefacts::test_trois_refus_levent_l_arret_1"]),
    ("R-04", "portée « course » levée au premier refus", AG,
     [("                if not dernier:\n                    return _REPLI\n",
       "                if self.na.portee_arret_1 == \"course\":\n                    raise ArretClassifieurNA(role, ev)\n"
       "                if not dernier:\n                    return _REPLI\n")],
     [T + "TestRepliArtefacts::test_portee_course_apres_trois_refus_seulement"]),
    ("R-05", "pire du rôle pris pour toutes les tentatives", AG,
     [("        pire = na.pire(role, modele)\n", "        pire = na.pires_micro[role]\n")],
     [T + "TestRepliArtefacts::test_pire_de_la_tentative_lu_par_modele"]),
    ("R-06", "part vérifiée à la première tentative seulement", AG,
     [("            compte = rt.verifier_part(na.table, na.parts_micro, na.cumul, cle, role, pire)\n",
       "            compte = rt.verifier_part(na.table, na.parts_micro, na.cumul, cle, role, pire) if rang_tentative == 1 "
       "else na.table.compte_de(cle)\n")],
     [T + "TestRepliArtefacts::test_part_repassee_par_tentative",
      T + "TestRepliCasSain::test_ligne_a_part_plafond_par_tentative"]),
    ("R-07", "coût inconnu compté au seul coût du noyau (A3)", AG,
     [("            compte_micro = max(delta, pire) if inconnu else delta\n", "            compte_micro = delta\n")],
     [T + "TestCout::test_cout_inconnu_sous_le_pire_releve_au_pire"]),
    ("R-08", "coût inconnu de l'adaptateur ignoré (A3)", AG,
     [("            inconnu = (not fini) or bool(getattr(r, \"cout_inconnu\", False))\n",
       "            inconnu = not fini\n")],
     [T + "TestCout::test_cout_inconnu_sous_le_pire_releve_au_pire"]),
    ("R-09", "reformulation admise", AG,
     [("                self._refuser_requete_na(\"reformulation\", role, cle, consigne.identifiant_case, na.numero_generation)\n",
       "                pass\n")],
     [T + "TestRepliArtefacts::test_reformulation_refusee"]),
    ("R-10", "égalité vérifiée à la première tentative seulement", AG,
     [("            gm.verifier_avant_envoi(envoi.requete_gardee, octets_remis)\n",
       "            gm.verifier_avant_envoi(envoi.requete_gardee, octets_remis) if rang_tentative == 1 else None\n")],
     [T + "TestRepliArtefacts::test_egalite_repassee_a_chaque_tentative"]),
    ("R-11", "rôle arrêté non relu en chaîne", AG,
     [("            if i > 1:\n                cause_arret = self.role_arrete_na(role)\n",
       "            if False:\n                cause_arret = self.role_arrete_na(role)\n")],
     [T + "TestRepliArtefacts::test_role_arrete_en_chaine"]),
    ("R-12", "erreur en repli : la chaîne continue", AG,
     [("                self._compte_repli_na(role, \"arrêtées en repli : cause non établie\")\n"
       "            return fin(ISSUE_ILLISIBLE, par_repli=False, en_repli=rang_tentative > 1)\n",
       "                self._compte_repli_na(role, \"arrêtées en repli : cause non établie\")\n"
       "            return _REPLI if not dernier else fin(ISSUE_ILLISIBLE, par_repli=False, en_repli=rang_tentative > 1)\n")],
     [T + "TestRepliArtefacts::test_erreur_en_repli_cause_non_etablie"]),
    ("R-13", "crédit en repli : pas d'arrêt n° 13", AG,
     [("            if classe in ERREURS_CREDIT:\n", "            if classe in ERREURS_CREDIT and rang_tentative == 1:\n")],
     [T + "TestRepliArtefacts::test_credit_en_repli_leve_13_sans_second_repli"]),
    # --- A6 et n° 1 ---
    ("R-14", "tout autre refus lu comme un n° 1 (la v1, l. 74)", AG,
     [("            # A6 : tout autre événement de refus est une réponse illisible, jamais rejouée\n",
       "            return self._arret_1_na(a, role, ev, fin, ISSUE_ARRET_1, tentatives)\n")],
     [T + "TestRepliArtefacts::test_refus_hors_liste_reponse_illisible"]),
    ("R-15", "refus d'une commande externe hors de la liste du n° 1", AG,
     [("EVENEMENTS_CLASSIFIEUR_SANS_REPLI = (\"commande.refus\", ", "EVENEMENTS_CLASSIFIEUR_SANS_REPLI = (")],
     [T + "TestRepliArtefacts::test_refus_d_une_commande_externe_arret_1_sans_repli"]),
    # --- n° 31 ---
    ("R-16", "modèle servi comparé à toute la liste, non à la tentative", AG,
     [("            if not modele_conforme(demande, servi):\n",
       "            if servi not in (demande,) + tuple(self.na.modeles_repli) and not modele_conforme(demande, servi):\n")],
     [T + "TestArret31::test_modele_servi_autre_au_repli"]),
    ("R-17", "modèle servi absent non nommé", AG,
     [("            if not servi:\n                self._consigner_tentative_na(**consigner, r=r, issue=f\"arrêt n° {NUMERO_ARRET_A2}\")\n"
       "                raise ArretA2NA(role, \"modèle servi absent pour une réponse servie\")\n",
       "            if False:\n                pass\n")],
     [T + "TestArret31::test_modele_servi_absent"]),
    ("R-18", "modèle servi gardé par rôle seul (le rôle ne garde pas son modèle)", AG,
     [("            vu = self.na_servis.setdefault((role, demande), servi)\n",
       "            vu = self.na_servis.setdefault(role, servi)\n")],
     [T + "TestRepliCasSain::test_le_role_garde_son_modele_apres_un_repli"]),
    ("R-19", "n° 31 sur les seules réponses « ok »", AG,
     [("        if statut == \"ok\" or servie:\n", "        if statut == \"ok\":\n")],
     [T + "TestArret31::test_modele_servi_autre_sur_un_refus"]),
    ("R-20", "trace de repli du fournisseur hors du n° 31", AG,
     [("                     \"resultat.modele_servi\", ad.EVENEMENT_MODELE_NON_PERMIS, ad.EVENEMENT_REPLI_FOURNISSEUR)\n",
       "                     \"resultat.modele_servi\", ad.EVENEMENT_MODELE_NON_PERMIS)\n")],
     [T + "TestArret31::test_trace_de_repli_du_fournisseur"]),
    ("R-21", "modèle refusé par le relais hors du n° 31", AG,
     [("                     \"resultat.modele_servi\", ad.EVENEMENT_MODELE_NON_PERMIS, ad.EVENEMENT_REPLI_FOURNISSEUR)\n",
       "                     \"resultat.modele_servi\", ad.EVENEMENT_REPLI_FOURNISSEUR)\n")],
     [T + "TestArret31::test_modele_refuse_par_le_relais"]),
    ("R-22", "modèle demandé autre que celui du rôle admis", AG,
     [("        if role in na.modeles_par_role and modele != na.modeles_par_role[role]:\n", "        if False:\n")],
     [T + "TestArret31::test_modele_demande_autre_que_celui_du_role"]),
    # --- n° 13 ---
    ("R-23", "plafond du relais hors du n° 13", AG,
     [("            if classe in ERREURS_CREDIT:\n", "            if classe == ad.ERREUR_CREDIT_AMONT:\n")],
     [T + "TestArret13::test_plafond_du_relais"]),
    # --- contexte ---
    ("R-24", "pire de repli manquant admis (n° 34)", AG,
     [("            if not isinstance(p, dict) or sorted(p) != sorted(mr):\n", "            if not isinstance(p, dict):\n")],
     [T + "TestContexte::test_pire_de_repli_manquant"]),
    ("R-25", "pire de repli nul admis", AG, [("                if v <= 0:\n", "                if v < 0:\n")],
     [T + "TestContexte::test_pire_de_repli_nul"]),
    ("R-26", "modèle de rôle admis comme modèle de repli", AG,
     [("        if any(m in mr for m in self.modeles_par_role.values()):\n", "        if False:\n")],
     [T + "TestContexte::test_modeles_repli_sans_leur_forme"]),
    ("R-27", "adaptateur non direct admis sur une clé Claude (D-N1)", AG,
     [("                if not isinstance(a, ad.AdaptateurClaudeDirectNA):\n", "                if a is None:\n")],
     [T + "TestContexte::test_adaptateur_non_direct_sur_une_cle_claude"]),
    ("R-28", "adaptateur direct sans les modèles de repli admis", AG,
     [("                if not exiges <= set(a.modeles_admis):\n", "                if False:\n")],
     [T + "TestContexte::test_adaptateur_direct_sans_les_modeles_de_repli"]),
    # --- adaptateur direct : corps (D2, A2) ---
    ("D-01", "champ système ajouté au corps", AD,
     [("    corps = {\"model\": modele, \"max_tokens\": jeu[\"max_tokens\"], \"messages\": [{\"role\": \"user\", "
       "\"content\": consigne}]}\n",
       "    corps = {\"model\": modele, \"max_tokens\": jeu[\"max_tokens\"], \"messages\": [{\"role\": \"user\", "
       "\"content\": consigne}], \"system\": \"\"}\n"),
      ("CLES_CORPS = (\"model\", \"max_tokens\", \"messages\", \"thinking\", \"output_config\")",
       "CLES_CORPS = (\"model\", \"max_tokens\", \"messages\", \"thinking\", \"output_config\", \"system\")")],
     [D + "TestCorps::test_cas_sain_consigne_seule_sans_systeme"]),
    ("D-02", "liste fermée du corps retirée", AD,
     [("    if not isinstance(corps, dict) or any(k not in CLES_CORPS for k in corps):\n",
       "    if not isinstance(corps, dict):\n")],
     [D + "TestCorps::test_artefacts_du_corps_refuses"]),
    ("D-03", "consigne du corps non comparée", AD,
     [("            or m[0][\"role\"] != \"user\" or type(m[0][\"content\"]) is not str or m[0][\"content\"] != consigne:\n",
       "            or m[0][\"role\"] != \"user\":\n")],
     [D + "TestCorps::test_artefacts_du_corps_refuses"]),
    # --- A1 ---
    ("D-04", "relances non vérifiées à la construction", AD,
     [("        self._erreurs_api = tuple(self._erreurs_api)\n        _verifier_sans_relance(self._client)\n",
       "        self._erreurs_api = tuple(self._erreurs_api)\n")],
     [D + "TestA1::test_client_qui_relancerait_refuse_a_la_construction"]),
    ("D-05", "relances non vérifiées avant l'envoi", AD,
     [("        _verifier_sans_relance(self._client)\n        base = {", "        base = {")],
     [D + "TestA1::test_client_change_apres_construction_refuse_avant_l_envoi"]),
    ("D-06", "client réel à relances", AD,
     [("api_key=JETON_FACTICE, max_retries=0, timeout=delai_s,", "api_key=JETON_FACTICE, max_retries=2, timeout=delai_s,"),
      ("    if getattr(client, \"max_retries\", None) != 0:\n", "    if getattr(client, \"max_retries\", None) not in (0, 2):\n")],
     [D + "TestClientReelBoucleLocale::test_529_une_seule_requete"]),
    ("D-07", "jeton factice du relais non posé en `x-api-key`", AD,
     [("                                 default_headers={\"x-api-key\": JETON_FACTICE},\n", "")],
     [D + "TestClientReelBoucleLocale::test_en_tetes_et_egalite_sur_le_corps_recu"]),
    # --- A5, A6, A2 (réponse) ---
    ("D-08", "catégorie vide rendue vide", AD,
     [("    cat = cat if isinstance(cat, str) and cat.strip() else CATEGORIE_NON_LUE\n",
       "    cat = cat if isinstance(cat, str) else CATEGORIE_NON_LUE\n")],
     [D + "TestA5A6::test_categorie_lue_ou_non_lue"]),
    ("D-09", "raison d'arrêt inconnue lue « ok »", AD,
     [("    return \"erreur\", \"\", raison if isinstance(raison, str) else None, None, ERREUR_RAISON_HORS_LISTE, None\n",
       "    return \"ok\", \"\", raison, None, None, None\n")],
     [D + "TestA5A6::test_liste_fermee_des_raisons", T + "TestRepliArtefacts::test_raison_inconnue_aucun_repli"]),
    ("D-10", "réponse coupée lue comme un refus de classifieur (rejouée)", AD,
     [("        return \"erreur\", \"\", raison, None, ERREUR_REPONSE_COUPEE, None\n",
       "        return \"refus\", \"\", raison, CATEGORIE_NON_LUE, None, EVENEMENT_REFUS_CLASSIFIEUR\n")],
     [T + "TestRepliArtefacts::test_reponse_coupee_aucun_repli"]),
    ("D-11", "trace de repli du fournisseur ignorée", AD,
     [("    if trace_repli_fournisseur(m):\n", "    if False:\n")],
     [D + "TestA5A6::test_trace_de_repli_du_fournisseur"]),
    ("D-12", "itération de repli ignorée", AD,
     [("    return isinstance(it, list) and any(isinstance(e, dict) and e.get(\"type\") == \"fallback_message\" for e in it)\n",
       "    return False\n")],
     [D + "TestA5A6::test_trace_de_repli_du_fournisseur"]),
    # --- N2 ---
    ("D-13", "tout 402 lu comme crédit d'amont", AD,
     [("    if statut == 402 and type_ == TYPE_FACTURATION:\n", "    if statut == 402:\n")],
     [T + "TestArret13::test_402_sans_type_de_facturation_n_est_pas_13"]),
    ("D-14", "plafond du relais non reconnu", AD,
     [("    if statut == 402 and isinstance(corps, dict) and corps.get(\"erreur\") == MESSAGE_PLAFOND_RELAIS:\n",
       "    if False:\n")],
     [T + "TestArret13::test_plafond_du_relais"]),
    ("D-15", "crédit d'amont non reconnu", AD,
     [("    if statut == 402 and type_ == TYPE_FACTURATION:\n", "    if False:\n")],
     [T + "TestArret13::test_credit_d_amont"]),
    # --- N2, forme 400 (B1 de la vérification du lot 4 v2) ---
    ("D-34", "crédit 400 non reconnu", AD,
     [("    if statut == 400 and type_ == TYPE_REQUETE_INVALIDE and message_de_solde(corps):\n", "    if False:\n")],
     [T + "TestArret13::test_credit_400_message_de_solde_leve_13", D + "TestCredit400::test_regle_stricte"]),
    ("D-35", "tout 400 de requête invalide lu comme crédit", AD,
     [("    if statut == 400 and type_ == TYPE_REQUETE_INVALIDE and message_de_solde(corps):\n",
       "    if statut == 400 and type_ == TYPE_REQUETE_INVALIDE:\n")],
     [T + "TestArret13::test_400_d_un_autre_message_n_est_pas_13"]),
    ("D-36", "fragment lu sous tout statut", AD,
     [("    if statut == 400 and type_ == TYPE_REQUETE_INVALIDE and message_de_solde(corps):\n",
       "    if message_de_solde(corps):\n")],
     [T + "TestArret13::test_fragment_sous_un_autre_statut_ou_type_n_est_pas_13"]),
    ("D-37", "type non exigé pour le 400", AD,
     [("    if statut == 400 and type_ == TYPE_REQUETE_INVALIDE and message_de_solde(corps):\n",
       "    if statut == 400 and message_de_solde(corps):\n")],
     [T + "TestArret13::test_fragment_sous_un_autre_statut_ou_type_n_est_pas_13"]),
    ("D-38", "comparaison avec la casse", AD,
     [("    return isinstance(message, str) and FRAGMENT_CREDIT_400.casefold() in message.casefold()\n",
       "    return isinstance(message, str) and FRAGMENT_CREDIT_400 in message\n")],
     [D + "TestCredit400::test_regle_stricte"]),
    ("D-39", "message recopié dans la fiche de la tentative", AD,
     [("            tentative = dict(base, servie=False, raison_arret=None, categorie=None, classe_erreur=classe,\n",
       "            tentative = dict(base, servie=False, raison_arret=None, categorie=None, classe_erreur=classe, "
       "message=str(corps_erreur),\n")],
     [D + "TestCredit400::test_message_garde_a_la_seule_reponse_brute"]),
    ("R-29", "crédit 400 hors de la liste du n° 13", AG,
     [("ERREURS_CREDIT = (ad.ERREUR_CREDIT_AMONT, ad.ERREUR_CREDIT_AMONT_400, ad.ERREUR_PLAFOND_RELAIS)",
       "ERREURS_CREDIT = (ad.ERREUR_CREDIT_AMONT, ad.ERREUR_PLAFOND_RELAIS)")],
     [T + "TestArret13::test_credit_400_message_de_solde_leve_13",
      T + "TestArret13::test_credit_400_en_repli_leve_13_sans_second_repli"]),
    # --- A3 ---
    ("D-16", "coût inconnu compté à zéro", AD,
     [("        cout = float(budget_usd) if inconnu else cout\n        tentative = dict(base, servie=",
       "        cout = 0.0 if inconnu else cout\n        tentative = dict(base, servie=")],
     [D + "TestA3::test_sans_usage_au_plafond_jamais_a_zero"]),
    ("D-17", "usage sans jetons d'entrée admis", AD,
     [("    if \"input_tokens\" not in usage or \"output_tokens\" not in usage:\n", "    if False:\n")],
     [D + "TestA3::test_sans_usage_au_plafond_jamais_a_zero"]),
    ("D-18", "jetons négatifs admis", AD,
     [("        if type(v) is not int or v < 0:\n", "        if type(v) is not int:\n")],
     [D + "TestA3::test_sans_usage_au_plafond_jamais_a_zero"]),
    ("D-19", "erreur après le début du flux comptée à zéro", AD,
     [("            inconnu = classe == ERREUR_SANS_STATUT or recu[\"octets\"]\n",
       "            inconnu = classe == ERREUR_SANS_STATUT\n")],
     [D + "TestA3::test_erreur_apres_le_debut_du_flux_au_plafond"]),
    ("D-20", "erreur de connexion comptée à zéro", AD,
     [("            inconnu = classe == ERREUR_SANS_STATUT or recu[\"octets\"]\n", "            inconnu = recu[\"octets\"]\n")],
     [D + "TestA3::test_erreur_de_statut_a_zero_connexion_au_plafond"]),
    # --- A4 ---
    ("D-21", "réponse servie non conservée", AD,
     [("        nom = self._conserver(dossier, dict(tentative, statut=statut, modele_servi=servi, corps_brut=brut,\n",
       "        nom = (lambda *a: \"\")(dossier, dict(tentative, statut=statut, modele_servi=servi, corps_brut=brut,\n")],
     [D + "TestA4::test_chaque_tentative_conservee_refus_et_erreurs_compris"]),
    ("D-22", "réponse conservée caviardée", AD,
     [("        nom = self._conserver(dossier, dict(tentative, statut=statut, modele_servi=servi, corps_brut=brut,\n",
       "        nom = self._conserver(dossier, dict(tentative, statut=statut, modele_servi=servi, "
       "corps_brut={\"corps_http\": caviarder(json.dumps(brut))[0]},\n")],
     [D + "TestA4::test_texte_brut_non_caviarde"]),
    ("D-23", "erreur non conservée", AD,
     [("            nom = self._conserver(dossier, dict(tentative, statut=statut, corps_brut={\"erreur\": corps_erreur},\n",
       "            nom = (lambda *a: \"\")(dossier, dict(tentative, statut=statut, corps_brut={\"erreur\": corps_erreur},\n")],
     [D + "TestA4::test_chaque_tentative_conservee_refus_et_erreurs_compris"]),
    ("D-24", "exception non conservée", AD,
     [("        except BaseException as e:\n            self._conserver(", "        except BaseException as e:\n            (lambda *a: None)(")],
     [D + "TestA4::test_exception_conservee_puis_relevee"]),
    # --- A7 (n° 32) ---
    ("D-25", "effort non contrôlé", AD,
     [("            if jeu[\"effort\"] is not None and jeu[\"effort\"] not in a[\"efforts\"]:\n", "            if False:\n")],
     [D + "TestA7::test_reglage_non_admis_sur_le_second_modele_de_repli"]),
    ("D-26", "flux non exigé au-delà du seuil", AD,
     [("            if jeu[\"max_tokens\"] > SEUIL_FLUX_JETONS and not jeu[\"flux\"]:\n", "            if False:\n")],
     [D + "TestA7::test_autres_reglages_non_admis"]),
    ("D-27", "plafond de sortie non borné", AD,
     [("            if not _entier_positif(jeu[\"max_tokens\"]) or jeu[\"max_tokens\"] > a[\"max_tokens_max\"]:\n",
       "            if not _entier_positif(jeu[\"max_tokens\"]):\n")],
     [D + "TestA7::test_autres_reglages_non_admis"]),
    ("D-28", "réflexion non contrôlée", AD,
     [("            if jeu[\"reflexion\"] not in a[\"reflexions\"]:\n", "            if False:\n")],
     [D + "TestA7::test_autres_reglages_non_admis"]),
    ("D-29", "jeu manquant pour un modèle admis", AD,
     [("        if not isinstance(par_modele, dict) or sorted(par_modele) != sorted(modeles_admis):\n",
       "        if not isinstance(par_modele, dict):\n")],
     [D + "TestA7::test_jeu_manquant_pour_un_modele_admis"]),
    ("D-30", "barème non exigé par modèle", AD,
     [("    if not isinstance(bareme, dict) or sorted(bareme) != sorted(modeles_admis):\n",
       "    if not isinstance(bareme, dict):\n")],
     [D + "TestA3::test_bareme_exige_par_modele"]),
    # --- refus avant toute requête ---
    ("D-31", "modèle hors de la liste fermée admis", AD,
     [("        if modele not in self.modeles_admis:\n            raise ModeleNonPermis",
       "        if False:\n            raise ModeleNonPermis")],
     [D + "TestCorps::test_refus_avant_toute_requete"]),
    ("D-32", "clé dans l'environnement admise", AD,
     [("        if presents:\n            raise CleDansEnvironnement", "        if False:\n            raise CleDansEnvironnement")],
     [D + "TestCorps::test_refus_avant_toute_requete"]),
    ("D-33", "moteur non armé admis", AD,
     [("        if not self.arme:\n            raise MoteurNonArme", "        if False:\n            raise MoteurNonArme")],
     [D + "TestCorps::test_refus_avant_toute_requete"]),
]

TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé", AG,
                 [("**Chaque tentative** est consignée", "**Chaque tentative** est bien consignée")],
                 [T + "TestRepliCasSain::test_premier_repli_servi", T + "TestRepliArtefacts::test_trois_refus_levent_l_arret_1"])


def copier(dest):
    shutil.copytree(os.path.join(ORCH, "pole"), os.path.join(dest, "pole"), ignore=shutil.ignore_patterns("__pycache__"))
    for rel in ESSAIS_COPIES:
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
        print("usage : mutations_na_lot4_v3.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in MODULES + ESSAIS_COPIES:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-lot4-v3-")
    rendu = {"version": "journal-mutations-na-lot4-v3", "python": sys.version.split()[0], "fichiers": empreintes,
             "mutations": []}
    try:
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, TOUS)
        rendu["temoin_non_mute"] = {"essais": "les deux fichiers entiers", "code": code, "resume": resume, "passe": code == 0}
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
    rendu["bilan"] = {"mutations": n, "tuees": tuees, "non_tuees": [m["id"] for m in rendu["mutations"] if not m["tuee"]],
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
