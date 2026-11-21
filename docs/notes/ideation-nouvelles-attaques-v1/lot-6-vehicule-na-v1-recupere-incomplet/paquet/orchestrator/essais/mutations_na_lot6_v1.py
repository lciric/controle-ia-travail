"""Mutations du lot 6 du véhicule NA-1, à la manière de la v68 : pour chaque garde, une copie temporaire de
l'orchestrateur, un remplacement à texte exact (le texte cherché doit y être une seule fois), puis les essais nommés ; une
mutation est **tuée** si ces essais échouent. Un témoin non muté doit passer ; un témoin inerte (un commentaire changé)
doit survivre.

    python -B essais/mutations_na_lot6_v1.py --racine ORCHESTRATOR --journal JOURNAL.json [--de N] [--a M]

La copie temporaire est faite sous le dossier temporaire du processus (`TMPDIR`), retirée après chaque mutation.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

C = "pole/course_na_v1.py"
F = "pole/configuration_course_na_v1.py"
S = "pole/simulation_na_v1.py"
L = "demonstrations/lancer_orchestrateur_na_v1.py"
G4 = "pole/appel_garde_na_v1.py"
TC = "essais/test_na_lot6_v1_course.py"
TA = "essais/test_na_lot6_v1_arrets.py"

MUTATIONS = [
    ("T0", "témoin non muté", None, None, None, [f"{TA}::TestA17::test_fiche_passee_munie_du_passeport_jugee"]),
    ("T1", "témoin inerte", C, "Bibliothèque standard, orchestrateur `a41b7b50…`",
     "Bibliothèque standard (témoin inerte), orchestrateur `a41b7b50…`",
     [f"{TA}::TestA17::test_fiche_passee_munie_du_passeport_jugee"]),
    ("M01", "E4 : le refus écrit passé au portier dans le dictionnaire du lot 4", C,
     "        if \"refus_ecrit\" in a:\n            return a[\"refus_ecrit\"]\n        return a\n",
     "        return a\n", [f"{TA}::TestRefusEcrits::test_portier_arrete_fiches_au_coffre_classe_ecrite_puis_arret_5"]),
    ("M02", "garde de remplacement retirée", C, "            if n >= self.course_na.seuil_refus_ecrits:",
     "            if False:", [f"{TA}::TestRefusEcrits::test_proposeur_arrete_des_sa_premiere_case_onze_refus_arret_nomme"]),
    ("M03", "garde de remplacement d'un cran trop tard", C, "            if n >= self.course_na.seuil_refus_ecrits:",
     "            if n > self.course_na.seuil_refus_ecrits:",
     [f"{TA}::TestRefusEcrits::test_proposeur_arrete_des_sa_premiere_case_onze_refus_arret_nomme"]),
    ("M04", "A17 : passeport du portier neuf non exigé", C,
     "        self.portier.exiger_passeport(fiche.identifiant, fiche.contenu)\n", "",
     [f"{TA}::TestA17::test_fiche_non_passee_presentee_a_un_juge", f"{TA}::TestA17::test_en_course_arret_nomme"]),
    ("M05", "A2 : version servie d'un juge non lue par la surcharge", C, "                    if vu != servi:",
     "                    if False:", [f"{TA}::TestA2::test_surcharge_de_juger_leve_a2_elle_meme"]),
    ("M06", "identifiant hexadécimal du noyau servi au juge", C,
     "        return ident.reencoder_jeton_noyau(jeton, \"F\", 5), jeton", "        return jeton, jeton",
     [f"{TA}::TestIdentifiantsJuges"]),
    ("M07", "n° 10 : garde de disjonction retirée", C,
     "                tn.garde_disjonction(tirage, g, cfn.triplets_de_la_copie(copie, tirage, g))", "                pass",
     [f"{TA}::TestArret10::test_case_de_la_famille_tenue_a_l_ecart_depart_refuse"]),
    ("M08", "n° 14 : empreinte de la copie non vérifiée", C, "                cfn.verifier_copie(copie, copie_sha, g)",
     "                pass", [f"{TA}::TestArret14::test_copie_de_la_generation_changee"]),
    ("M09", "n° 14 : empreintes non rejouées au départ de chaque génération", C,
     "                cfn.verifier_empreintes(config, moment)", "                pass",
     [f"{TA}::TestArret14::test_rejoue_au_depart_de_la_generation_2"]),
    ("M10", "A3 : vérification au départ retirée", F,
     "    if type(arrets.get(\"a3_echecs_consecutifs\")) is not int or arrets[\"a3_echecs_consecutifs\"] != v_a3:",
     "    if False:", [f"{TC}::TestGardesHeritees::test_a3_valeur_heritee"]),
    ("M11", "A14 : vérification au départ retirée", F,
     "    if not _reel(arrets.get(\"a14_part_max\")) or float(arrets[\"a14_part_max\"]) != float(v_a14):",
     "    if False:", [f"{TC}::TestGardesHeritees::test_a14_valeur_heritee"]),
    ("M12", "délai d'A3 : alignement non vérifié", F,
     "            or any(not _reel(v) or float(v) != float(delai) for v in delais.values()):", "            or False:",
     [f"{TC}::TestGardesHeritees::test_delai_herite"]),
    ("M13", "A11 : liste non vérifiée", F, "    if g.get(\"a11_modeles\") != [] or arrets.get(\"a11_modeles\") != []:",
     "    if False:", [f"{TC}::TestGardesHeritees::test_a11_liste_non_vide"]),
    ("M14", "S12 : nom réservé non vérifié dans le noyau", F, "    if reserve in noms:", "    if False:",
     [f"{TC}::TestGardesHeritees::test_nom_reserve_dans_le_noyau"]),
    ("M15", "S12 : nom réservé non vérifié dans la table", F,
     "    if any(reserve in c.adaptateurs for c in table.cles.values()):", "    if False:",
     [f"{TC}::TestGardesHeritees::test_nom_reserve_dans_la_table"]),
    ("M16", "`fournisseurs_requis` du noyau (lecteurs et metteur exigés)", C,
     "        return ({p[\"fournisseur\"] for p in conf[\"proposeurs\"]} | {j[\"fournisseur\"] for j in conf[\"juges\"]}\n"
     "                | {conf[\"aiguilleur\"][\"fournisseur\"]})", "        return GenerationV68.fournisseurs_requis(conf)",
     [f"{TC}::TestTroisGenerations::test_trois_generations_completes"]),
    ("M17", "lecture qui rend rien sans fiche", C, "    return texte\n\n\ndef _plus",
     "    return texte if texte.strip() else None\n\n\ndef _plus",
     [f"{TC}::TestGardesHeriteesEnCourse::test_proposeurs_sans_texte_jamais_arretes"]),
    ("M18", "n° 8 : borne de la requête non vérifiée", C, "            rq.verifier_borne(r, borne_requete)", "            pass",
     [f"{TA}::TestArret8::test_un_octet_de_plus_depart_refuse"]),
    ("M19", "n° 5 : garde du coffre retirée", C,
     "                constat = rg.garde_du_coffre(rg.lire_registre_tentatives(gen.registre_na.chemin, exiger_sceau=True), g)",
     "                constat = rg.ConstatCoffre(g, 0, 0, False, False)",
     [f"{TA}::TestArret5::test_une_fiche_de_plus_au_coffre_la_suivante_ne_part_pas"]),
    ("M20", "n° 7 : nœud budgétaire non nommé", C, "                    if etape is not None:", "                    if False:",
     [f"{TA}::TestArret7::test_cumul_d_un_centime_au_dessus_de_135_aiguillage_non_lance"]),
    ("M21", "n° 6 : réservation retirée", C, "                budget.reserver(poste, s17)", "                pass",
     [f"{TA}::TestArret6::test_en_course_chaque_generation_reserve_s17_avant_ses_appels"]),
    ("M22", "étape neutralisée jouée en silence", C,
     "    def etape_passe_tableau(self, etat):\n        raise EtapeNeutraliseeJouee(",
     "    def etape_passe_tableau(self, etat):\n        return None\n        raise EtapeNeutraliseeJouee(",
     [f"{TC}::TestEtapesNeutralisees::test_passe_tableau_jouee_est_un_arret"]),
    ("M23", "n° 19 : registre servi non vérifié", C, "    if servi.taille:\n        vr.verifier_registre_servi(",
     "    if False:\n        vr.verifier_registre_servi(",
     [f"{TA}::TestRegistreServiNonConforme::test_une_marque_de_code_dans_un_enonce_la_generation_2_ne_part_pas"]),
    ("M24", "Z4-25 (lot 4) : table « artefact » admise dans le contexte", G4,
     "        if not isinstance(self.table, rt.TableRolesCles) or self.table.marque == rt.MARQUE_ARTEFACT:",
     "        if not isinstance(self.table, rt.TableRolesCles):",
     [f"{TC}::TestTableArtefact::test_table_artefact_refusee_dans_le_contexte_de_la_generation"]),
    ("M25", "E8 v2 : messages du corps non gardés", S,
     "                 \"messages\": empreintes_messages(e[\"corps\"])} for e in requetes]",
     "                 \"messages\": []} for e in requetes]", [f"{TC}::TestFauxFournisseur::test_egalite_journal_et_chaine_recue"]),
    ("M26", "lanceur : moteur simulé hors de l'essai à blanc", L,
     "        if not essai_a_blanc or confirmer_moteur_reel:", "        if False:",
     [f"{TC}::TestLanceur::test_decider_moteur", f"{TC}::TestLanceur::test_refus_avant_toute_ecriture"]),
    ("M27", "régime : ligne d'accord non vérifiée", F,
     "    if not _reel(ligne_accord_usd) or rt.micro_exact(ligne_accord_usd) != rt.micro_exact(plafond):", "    if False:",
     [f"{TC}::TestRegime::test_ligne_d_accord_d_un_autre_montant"]),
    ("M28", "régime : additif non épinglé", F,
     "    if type(additif_sha256) is not str or len(additif_sha256) != 64 or additif_sha256 != additif_epingle_sha256:",
     "    if False:", [f"{TC}::TestRegime::test_additif_d_une_autre_empreinte"]),
    ("M29", "E6 : comptes du mélange non portés tels quels", C, "        \"comptes_melange_lot_4\": gen.na_comptes,",
     "        \"comptes_melange_lot_4\": {},", [f"{TC}::TestTroisGenerations::test_ligne_de_generation_fusionne_sans_renommer"]),
    ("M30", "verdict absent par refus écrit non compté", C,
     "                _plus(self.comptes_lot6[\"verdicts_absents\"].setdefault(nom, {}), \"refus écrit\")", "                pass",
     [f"{TA}::TestRefusEcrits::test_juge_arrete_verdicts_absents_comptes_aucun_arret"]),
    ("M31", "case non jouée non comptée", C,
     "            _plus(self.comptes_lot6[\"cases_non_jouees\"], str(self._espece(role)))", "            pass",
     [f"{TA}::TestRefusEcrits::test_proposeur_arrete_apres_sa_premiere_case_dix_refus_la_course_continue"]),
    ("M32", "E5 : ligne d'arrêt non écrite", C, "                journal_arrets.ecrire(\"arrêt\", generation=g, arret=arret)",
     "                pass", [f"{TA}::TestArret14::test_rejoue_au_depart_de_la_generation_2"]),
    ("M33", "E5 : journal des arrêts non scellé", C, "            journal_arrets.sceller()", "            pass",
     [f"{TC}::TestTroisGenerations::test_journal_des_arrets_et_des_generations_scelle"]),
    ("M34", "fiche classée non portée au registre", C, "                    self.registre_na.ajouter_fiche(f)",
     "                    pass", [f"{TC}::TestTroisGenerations::test_trois_generations_completes"]),
]


def jouer(racine, m):
    code, quoi, fichier, avant, apres, essais = m
    base = tempfile.mkdtemp(prefix="mutation-na-lot6-")
    copie = os.path.join(base, "orchestrator")
    try:
        shutil.copytree(racine, copie, ignore=shutil.ignore_patterns("__pycache__"))
        if fichier is not None:
            chemin = os.path.join(copie, fichier)
            with open(chemin, encoding="utf-8") as f:
                texte = f.read()
            n = texte.count(avant)
            if n != 1:
                return {"code": code, "quoi": quoi, "issue": f"invalide (texte cherché présent {n} fois)"}
            with open(chemin, "w", encoding="utf-8") as f:
                f.write(texte.replace(avant, apres, 1))
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *essais],
                           cwd=copie, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"), capture_output=True)
        if r.returncode == 5:
            issue = "invalide (aucun essai trouvé)"
        elif code == "T0":
            issue = "passe" if r.returncode == 0 else "échoue (le témoin non muté doit passer)"
        elif code == "T1":
            issue = "survit" if r.returncode == 0 else "tuée (le témoin inerte doit survivre)"
        else:
            issue = "tuée" if r.returncode != 0 else "SURVIT"
        return {"code": code, "quoi": quoi, "fichier": fichier, "essais": essais, "code_retour": r.returncode, "issue": issue}
    finally:
        shutil.rmtree(base, ignore_errors=True)


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--racine", required=True)
    p.add_argument("--journal", required=True)
    p.add_argument("--de", type=int, default=0)
    p.add_argument("--a", type=int, default=len(MUTATIONS))
    a = p.parse_args(argv)
    if os.path.exists(a.journal):
        raise SystemExit("journal existant : jamais écrasé (R12)")
    rendu = [jouer(os.path.abspath(a.racine), m) for m in MUTATIONS[a.de:a.a]]
    with open(a.journal, "x", encoding="utf-8") as f:
        json.dump({"version": "mutations-na-lot6-v1", "mutations": rendu}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    tuees = sum(1 for x in rendu if x["issue"] == "tuée")
    print(json.dumps({"jouees": len(rendu), "tuees": tuees, "survivantes": [x["code"] for x in rendu if x["issue"] == "SURVIT"],
                      "invalides": [x["code"] for x in rendu if x["issue"].startswith("invalide")],
                      "temoins": {x["code"]: x["issue"] for x in rendu if x["code"] in ("T0", "T1")}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
