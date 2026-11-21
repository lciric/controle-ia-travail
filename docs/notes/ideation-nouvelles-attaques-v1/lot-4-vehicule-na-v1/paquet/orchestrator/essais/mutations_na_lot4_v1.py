"""Mutations du lot 4 du véhicule NA-1 : pour chaque garde, la garde retirée fait échouer son essai (R5 ; manière de la v68,
R68, § 4, et des programmes des lots 1 à 3).

Pour chaque mutation : une copie neuve, dans un dossier temporaire, du dossier `pole/` de la copie de l'orchestrateur (le
noyau v56, que les essais lisent, et les modules des lots 2 à 4 compris) et des seuls fichiers d'essais dont les essais du
lot 4 ont besoin (aides de la v53 à la v56, aides des lots 2 à 4, liste d'essai, configuration de pytest) ; un ou plusieurs
remplacements à texte exact dans un module (chaque texte cherché doit y être une fois exactement, sinon la mutation est dite
invalide) ; puis les essais nommés de cette garde, joués dans un processus à part. La mutation est « tuée » si et seulement
si pytest rend le code 1. Avant cela, les deux fichiers d'essais entiers sont joués sur une copie non mutée : ils doivent
passer (code 0). Un témoin inerte (un mot de docstring changé) doit survivre. La liste réelle des motifs n'est ni copiée ni
lue.

Usage : `python -B mutations_na_lot4_v1.py JOURNAL.json` (le journal ne doit pas exister : R12). Aucun réseau, aucune clé ;
les copies temporaires sont retirées en fin de programme.
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
    "essais/aides_na_lot3_v3.py", "essais/aides_na_lot4_v1.py", "essais/test_na_v1_appel_garde.py",
    "essais/test_na_v1_adaptateur_claude.py",
)
MODULES_LOT_4 = ("pole/routage_na_v1.py", "pole/appel_garde_na_v1.py", "pole/adaptateur_claude_na_v1.py",
                 "pole/faux_fournisseur_na_v1.py", "pole/releve_sans_systeme_na_v1.py")
TOUS = ["essais/test_na_v1_appel_garde.py", "essais/test_na_v1_adaptateur_claude.py"]
T = "essais/test_na_v1_appel_garde.py::"
D = "essais/test_na_v1_adaptateur_claude.py::"
RT, AG, AC, FF, RL = MODULES_LOT_4

MUTATIONS = [
    # --- routage (arrêt n° 12, seconde clause ; D11) ---
    ("L4-01", "routeur par espèce (D11)", RT,
     [("        if (e.cle, e.adaptateur) != (cle_presentee.nom, nom_adaptateur):\n",
       "        if not any(x.espece == e.espece and (x.cle, x.adaptateur) == (cle_presentee.nom, nom_adaptateur)\n"
       "                   for x in self.roles.values()):\n")],
     [T + "TestArret12::test_artefact_table_plantee_juge_espece_3_sur_la_cle_du_proposeur"]),
    ("L4-02", "rôle absent de la table admis", RT,
     [("        if e is None:\n            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, \"rôle absent",
       "        if False:\n            raise ArretPartCle(CLAUSE_ROUTAGE, nom_presente, \"rôle absent")],
     [T + "TestArret12::test_role_absent_de_la_table_refuse"]),
    ("L4-03", "rôle routé vers hors_course admis", RT,
     [("        if e.cle == CLE_HORS_COURSE:\n", "        if False:\n")],
     [T + "TestHorsCourse::test_lecteur_etiquettes_plante_refuse_sans_erreur_de_dictionnaire"]),
    ("L4-04", "adaptateur hors table admis", RT,
     [("        if cle_presentee is None:\n            raise", "        if False:\n            raise")],
     [T + "TestArret12::test_adaptateur_hors_table_refuse"]),
    ("L4-05", "envoi à une clé sans part admis", RT,
     [("        if cle_presentee.hors_course or cle_presentee.sans_part:\n", "        if cle_presentee.hors_course:\n")],
     [T + "TestArret12::test_envoi_a_la_cle_sans_part_refuse"]),
    ("L4-06", "couple (rôle, adaptateur) non vérifié", RT,
     [("        if (e.cle, e.adaptateur) != (cle_presentee.nom, nom_adaptateur):\n", "        if False:\n")],
     [T + "TestArret12::test_artefact_en_course_aiguilleur_sur_la_cle_de_l_espece_3",
      T + "TestArret12::test_juge_espece_3_sur_la_cle_de_l_aiguilleur_refuse"]),
    # --- part de la clé (arrêt n° 12, première clause) ---
    ("L4-07", "part non vérifiée", RT,
     [("    if deja + vol + pire_micro > limite:\n", "    if False:\n")],
     [T + "TestArret12::test_part_egale_permise_un_centime_de_trop_refuse"]),
    ("L4-08", "part égale refusée", RT,
     [("    if deja + vol + pire_micro > limite:\n", "    if deja + vol + pire_micro >= limite:\n")],
     [T + "TestArret12::test_part_egale_permise_un_centime_de_trop_refuse"]),
    ("L4-09", "pire des appels en vol non compté", RT,
     [("    deja, vol = cumul.cumul(compte), cumul.en_vol(compte)\n", "    deja, vol = cumul.cumul(compte), 0\n")],
     [T + "TestCumulEtContexte::test_en_vol_entre_dans_la_part"]),
    ("L4-10", "empreinte de la table non vérifiée (arrêt n° 14)", RT,
     [("    if type(empreinte_attendue) is not str or sha != empreinte_attendue:\n        raise EmpreinteTableDifferente",
       "    if False:\n        raise EmpreinteTableDifferente")],
     [T + "TestTable::test_empreinte_differente_refusee"]),
    ("L4-11", "table d'une autre marque admise (artefact chargé)", RT,
     [("    if obj[\"marque\"] != marque_attendue:\n", "    if False:\n")],
     [T + "TestTable::test_artefact_jamais_charge_comme_course"]),
    ("L4-12", "parts différentes de la table scellée admises", RT,
     [("        if table.cles[cle].part_micro != rendu[cle]:\n", "        if False:\n")],
     [T + "TestTable::test_parts_et_pires_exiges"]),
    # --- surcharge d'appel : coût et refus avant le noyau ---
    ("L4-13", "coût non compté au cumul de la clé", AG,
     [("            na.cumul.ajouter(compte, rt.micro_cout(max(0.0, float(etat[\"cout\"]) - cout_avant)))\n",
       "            na.cumul.ajouter(compte, 0)\n")],
     [T + "TestArret12::test_cas_sain_chaque_cle_lance_et_compte"]),
    ("L4-14", "refus de la part déplacé après l'appel du noyau (comme dans `lancer`)", AG,
     [("        # pas 2 : part de la clé\n", "        # pas 2 : part de la clé\n        differe = None\n"),
      ("            self._non_envoye_na(rt.NUMERO_ARRET_PART, role, cle, consigne.identifiant_case, na.numero_generation,\n"
       "                                clause=arret.clause, sorte=consigne.sorte, sha256=consigne.sha256, taille=consigne.taille)\n"
       "            raise\n",
       "            compte = na.table.compte_de(cle)\n            differe = arret\n"),
      ("        # pas 7 : au retour\n", "        if differe is not None:\n            raise differe\n        # pas 7 : au retour\n")],
     [T + "TestEnvoiRefuseSansCout::test_premiere_clause_sans_cout"]),
    ("L4-15", "l'arrêt du lot 2, qui porte le texte trouvé, relevé tel quel", AG,
     [("            motif = (arret.famille, arret.rang)\n", "            raise\n")],
     [T + "TestArret16::test_texte_trouve_seulement_au_journal"]),
    ("L4-16", "panne du journal par OSError non attrapée (erratum 3)", AG,
     [("        except (jn.JournalRefuse, OSError):\n            panne = True\n        if motif is not None:\n",
       "        except jn.JournalRefuse:\n            panne = True\n        if motif is not None:\n")],
     [T + "TestJournalEnPanne::test_fichier_supprime", T + "TestJournalEnPanne::test_fichier_remplace_par_un_dossier",
      T + "TestJournalEnPanne::test_ecriture_en_panne"]),
    ("L4-17", "égalité non vérifiée (erratum 1)", AG,
     [("            gm.verifier_avant_envoi(envoi.requete_gardee, octets_remis)\n", "            pass\n")],
     [T + "TestEgalite::test_divergence_refusee_apres_la_ligne_envoi"]),
    ("L4-18", "égalité refusée sans ligne « non envoyé » qui renvoie au rang (erratum 2)", AG,
     [("            self._non_envoye_na(ARRET_REQUETE_JOURNALISEE, role, cle, consigne.identifiant_case, consigne.generation,\n",
       "            0 and self._non_envoye_na(ARRET_REQUETE_JOURNALISEE, role, cle, consigne.identifiant_case, consigne.generation,\n")],
     [T + "TestEgalite::test_divergence_refusee_apres_la_ligne_envoi"]),
    ("L4-19", "comptes : une requête refusée après la ligne « envoi » comptée partie", AG,
     [("        elif l[\"evenement\"] == \"non envoyé\" and l.get(\"arret\") == ARRET_REQUETE_JOURNALISEE \\\n",
       "        elif False and l[\"evenement\"] == \"non envoyé\" and l.get(\"arret\") == ARRET_REQUETE_JOURNALISEE \\\n")],
     [T + "TestEgalite::test_divergence_refusee_apres_la_ligne_envoi"]),
    ("L4-20", "pas 0 retiré : rôle arrêté présenté au noyau", AG,
     [("        if cause_arret:\n", "        if False:\n")],
     [T + "TestRefusEcrit::test_role_arrete_refus_ecrit_par_sorte"]),
    ("L4-21", "consigne non assemblée admise", AG,
     [("        if not isinstance(consigne, rq.RequeteAssemblee):\n            case, _ =",
       "        if False:\n            case, _ =")],
     [T + "TestEgalite::test_requete_non_assemblee_refusee"]),
    ("L4-22", "case incohérente admise", AG,
     [("        if case_session != consigne.identifiant_case:\n", "        if False:\n")],
     [T + "TestEgalite::test_case_incoherente_refusee"]),
    ("L4-23", "génération incohérente admise", AG,
     [("        if consigne.generation is not None and consigne.generation != na.numero_generation:\n", "        if False:\n")],
     [T + "TestEgalite::test_generation_incoherente_refusee"]),
    ("L4-24", "ligne « non lancé » non écrite", AG,
     [("                na.journal.journaliser_non_lance(envoi, cause)\n", "                pass\n")],
     [T + "TestNonLance::test_coupure_au_plafond_dur"]),
    ("L4-25", "coût d'un appel en exception non compté sur la clé", AG,
     [("        finally:\n            na.cumul.fermer_vol(jeton)\n            na.cumul.ajouter",
       "        except BaseException:\n            na.cumul.fermer_vol(jeton)\n            raise\n        else:\n"
       "            na.cumul.fermer_vol(jeton)\n            na.cumul.ajouter")],
     [T + "TestCumulEtContexte::test_exception_de_l_adaptateur_comptee_au_plafond"]),
    ("L4-26", "refus 12 de la seconde clause sans ligne au journal", AG,
     [("            self._non_envoye_na(rt.NUMERO_ARRET_PART, role, arret.cle, case,",
       "            0 and self._non_envoye_na(rt.NUMERO_ARRET_PART, role, arret.cle, case,")],
     [T + "TestEnvoiRefuseSansCout::test_refus_12_sans_cout"]),
    ("L4-27", "refus non compté sur la ligne de la génération", AG,
     [("        _plus(self.na_comptes[\"non_envoyes\"].setdefault(role, {}), str(arret))\n", "        pass\n")],
     [T + "TestEnvoiRefuseSansCout::test_refus_12_sans_cout"]),
    # --- statuts au retour ---
    ("L4-28", "arrêt n° 1 non consigné", AG,
     [("            self.na_arrets_consignes.append(", "            [].append(")],
     [T + "TestArret1::test_refus_de_classifieur_consigne_non_relance"]),
    ("L4-29", "portée « course » de l'arrêt n° 1 ignorée", AG,
     [("            if self.na.portee_arret_1 == \"course\":\n", "            if False:\n")],
     [T + "TestArret1::test_portee_course_arrete"]),
    ("L4-30", "A2 : modèle servi absent non vu", AG,
     [("            if not servi:\n", "            if False:\n")],
     [T + "TestA2::test_modele_servi_absent"]),
    ("L4-31", "A2 : modèle servi changé non vu", AG,
     [("            if vu != servi:\n", "            if False:\n")],
     [T + "TestA2::test_modele_servi_change"]),
    ("L4-32", "A2 : refus de transport pour un autre modèle lu comme classifieur", AG,
     [("            if ev in EVENEMENTS_MODELE:\n", "            if False:\n")],
     [T + "TestA2::test_refus_de_transport_pour_un_autre_modele"]),
    ("L4-33", "message synthétique de l'outil lu comme A2", AG,
     [("        synthetique = statut == \"refus\" and", "        synthetique = False and")],
     [T + "TestArret13::test_message_synthetique_de_l_outil_lu_comme_erreur_non_comme_a2"]),
    ("L4-34", "état du relais lu mais refus pour crédit non arrêté (arrêt n° 13)", AG,
     [("            if credit:\n", "            if False:\n")],
     [T + "TestArret13::test_refus_pour_credit_au_relais_arret_13_qui_dit_la_cle"]),
    ("L4-35", "règle du refus pour crédit sans le compte des refus", AG,
     [("    return v[\"refus\"] - v[\"refus_modele\"] > 0 and ", "    return True and ")],
     [T + "TestArret13::test_relais_montre_refus_credit"]),
    ("L4-36", "relais de protocole : budget dépassé non arrêté", AG,
     [("        if type_cle == \"kimi_protocole\" and statut == \"budget_depasse\":\n", "        if False:\n")],
     [T + "TestArret13::test_relais_de_protocole_budget_depasse_arret_13"]),
    ("L4-37", "sous-compte « cause non établie » non tenu", AG,
     [("            _plus(self.na_comptes[\"cause_non_etablie\"], role)\n", "            pass\n")],
     [T + "TestArret13::test_erreur_sans_refus_au_relais_cause_non_etablie"]),
    ("L4-38", "relais illisible non compté", AG,
     [("                _plus(self.na_comptes[\"etat_relais_illisible\"], role)\n", "                pass\n")],
     [T + "TestArret13::test_relais_illisible_compte"]),
    ("L4-39", "contexte non exigé", AG,
     [("        if not isinstance(contexte, ContexteAppelGardeNA):\n", "        if False:\n")],
     [T + "TestCumulEtContexte::test_contexte_exige_et_refuse"]),
    ("L4-40", "garde d'une autre version admise", AG,
     [("        if not isinstance(self.garde, gm.GardeMotifs):\n", "        if False:\n")],
     [T + "TestCumulEtContexte::test_garde_d_une_autre_version_refusee"]),
    # --- adaptateur Claude neuf ---
    ("L4-41", "texte système d'origine laissé dans les options", AC,
     [("    o[\"system_prompt\"] = \"\" if forme_sans_systeme == \"chaine_vide\" else None\n", "    pass\n")],
     [D + "TestSansTexteSysteme::test_options_sans_texte_systeme_chaine_vide",
      D + "TestSansTexteSysteme::test_options_sans_texte_systeme_absent"]),
    ("L4-42", "réponse brute non conservée", AC,
     [("        self._conserver(dossier, {\"statut\": statut,", "        0 and self._conserver(dossier, {\"statut\": statut,")],
     [D + "TestReponsesBrutes::test_reponse_normale_conservee", D + "TestReponsesBrutes::test_refus_et_erreur_conserves"]),
    ("L4-43", "exception de la session non conservée", AC,
     [("            self._conserver(dossier, {\"statut\": \"exception\",",
       "            0 and self._conserver(dossier, {\"statut\": \"exception\",")],
     [D + "TestReponsesBrutes::test_exception_conservee_puis_relevee"]),
    ("L4-44", "conservation impossible passée sous silence", AC,
     [("        except OSError as e:\n            raise ConservationImpossible(",
       "        except OSError as e:\n            return None\n            raise ConservationImpossible(")],
     [D + "TestReponsesBrutes::test_conservation_impossible_rien_n_est_rendu"]),
    ("L4-45", "nom de réponse brute non sauté s'il existe", AC,
     [("                if os.path.exists(chemin) or os.path.exists(chemin + \".sha256\"):\n", "                if False:\n")],
     [D + "TestReponsesBrutes::test_noms_jamais_ecrases"]),
    ("L4-46", "rôle hors du véhicule admis", AC,
     [("    if role not in ROLES_NA:\n", "    if False:\n")],
     [D + "TestSansTexteSysteme::test_roles_et_formes_refuses"]),
    # --- faux fournisseur et relevé ---
    ("L4-47", "faux fournisseur hors de la boucle locale admis", FF,
     [("        if hote != HOTE:\n", "        if False:\n")],
     [D + "TestFauxFournisseur::test_n_ecoute_que_sur_la_boucle_locale"]),
    ("L4-48", "valeur d'un en-tête de clé gardée", FF,
     [("(\"présent\" if k.lower() in EN_TETES_SECRETS else v)", "v")],
     [D + "TestFauxFournisseur::test_garde_et_journal_sans_secret"]),
    ("L4-49", "identifiant de modèle non masqué au relevé", RL,
     [("    return texte.replace(modele, MODELE_ECRIT), texte.count(modele)\n", "    return texte, 0\n")],
     [D + "TestAnalyseDuReleve::test_corps_avec_texte_systeme_et_ajout", D + "TestAnalyseDuReleve::test_masquer"]),
    ("L4-50", "texte ajouté aux messages non relevé", RL,
     [("              if b.get(\"texte\") is not None and not b[\"egal_a_la_consigne\"] and not b[\"egal_a_la_consigne_sans_blanc_final\"]]\n",
       "              if False]\n")],
     [D + "TestAnalyseDuReleve::test_corps_avec_texte_systeme_et_ajout"]),
    ("L4-51", "chemin du dossier du relevé non masqué", RL,
     [("        texte = texte.replace(racine, RACINE_ECRITE)\n", "        pass\n")],
     [D + "TestAnalyseDuReleve::test_masquer_le_dossier_du_releve"]),
]

# Témoin du programme (R4) : une mutation inerte, qui ne touche aucune garde, doit survivre (code 0).
TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé", RT,
                 [("Recherche **par rôle**, jamais par espèce.", "Recherche **par rôle**, et jamais par espèce.")],
                 [T + "TestArret12::test_artefact_table_plantee_juge_espece_3_sur_la_cle_du_proposeur",
                  T + "TestArret12::test_part_egale_permise_un_centime_de_trop_refuse"])


def copier(dest):
    shutil.copytree(os.path.join(ORCH, "pole"), os.path.join(dest, "pole"),
                    ignore=shutil.ignore_patterns("__pycache__"))
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
        print("usage : mutations_na_lot4_v1.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in MODULES_LOT_4 + ESSAIS_COPIES:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-lot4-v1-")
    rendu = {"version": "journal-mutations-na-lot4-v1", "python": sys.version.split()[0], "fichiers": empreintes,
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
