"""Mutations du lot 5 v2 du véhicule NA-1 (registre des tentatives d'appel) : pour chaque garde, la garde retirée fait
échouer son essai (R5 ; manière de la v68, reprise du lot 5 v1).

Pour chaque mutation : une copie neuve, dans un dossier temporaire, de l'orchestrateur où ce fichier est posé ; un ou
plusieurs remplacements à texte exact dans `pole/registre_na_v2.py` (chaque texte cherché doit y être une fois exactement,
sinon la mutation est dite invalide) ; puis les essais nommés de cette garde, joués dans un processus à part. La mutation
est « tuée » si et seulement si pytest rend le code 1. Avant cela, le fichier d'essais entier est joué sur une copie non
mutée (code 0 exigé) ; un témoin inerte (un mot de docstring changé) doit survivre.

Usage : `python -B mutations_na_lot5_v2.py JOURNAL.json` (le journal ne doit pas exister : R12). Aucun réseau, aucune clé.
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
RG2 = "pole/registre_na_v2.py"
T = "essais/test_na_lot5_v2_registre.py::"
TOUS = ["essais/test_na_lot5_v2_registre.py"]
E = T + "TestEcritureArtefacts::"
R = T + "TestRelecture::"
D = T + "TestDifferentielV1::"
S = T + "TestEcritureSaine::"
X = T + "TestContexte::"

MUTATIONS = [
    ("M2-01", "ligne incomplète admise",
     [(RG2, "    if set(CHAMPS_LIGNE) - cles:\n", "    if False:\n"),
      (RG2, "            if set(CHAMPS_TENTATIVE) - set(t):\n", "            if False:\n")],
     [E + "test_champ_manquant", R + "test_ligne_incomplete_au_fichier"]),
    ("M2-02", "champ de tentative en plus admis",
     [(RG2, "            if set(t) - set(CHAMPS_TENTATIVE):\n", "            if False:\n")],
     [E + "test_champ_en_plus"]),
    ("M2-03", "espèce hors liste admise",
     [(RG2, '    if l["espece"] not in ESPECES:\n', "    if False:\n")],
     [E + "test_espece_hors_liste"]),
    ("M2-04", "classe d'issue hors liste admise",
     [(RG2, '    if l["classe_issue"] not in CLASSES_ISSUE:\n', "    if False:\n")],
     [E + "test_classe_issue_hors_liste"]),
    ("M2-05", "case hors des cases servies admise",
     [(RG2, '    if l["case"] is not None and l["case"] not in contexte.cases_servies:\n', "    if False:\n")],
     [E + "test_case_hors_des_cases_servies"]),
    ("M2-06", "proposeur sans case admis",
     [(RG2, '    if l["espece"] in ESPECES_PROPOSEURS and l["case"] is None:\n', "    if False:\n")],
     [E + "test_proposeur_sans_case"]),
    ("M2-07", "rang de repli non vérifié",
     [(RG2, '    if not _entier(l["rang_repli"]) or l["rang_repli"] not in RANGS_REPLI:\n', "    if False:\n")],
     [E + "test_rang_hors_liste"]),
    ("M2-08", "modèle demandé hors des identifiants par rôle admis",
     [(RG2, '    if l["modele_demande"] not in contexte.modeles_demandes:\n', "    if False:\n")],
     [E + "test_modele_demande_hors_des_identifiants_par_role"]),
    ("M2-09", "modèle servi non vérifié",
     [(RG2, '    elif not _chaine_d_une_ligne(l["modele_servi"]):\n', "    elif False:\n")],
     [E + "test_modele_servi_absent_ou_mal_forme"]),
    ("M2-10", "raison d'arrêt non vérifiée",
     [(RG2, '    if not _chaine_d_une_ligne(l["raison_arret"]):\n', "    if False:\n")],
     [E + "test_raison_d_arret_absente_ou_mal_formee"]),
    ("M2-11", "catégorie de refus non vérifiée",
     [(RG2, '    if l["categorie_refus"] is not None and not _chaine_d_une_ligne(l["categorie_refus"]):\n',
       "    if False:\n")],
     [E + "test_categorie_mal_formee"]),
    ("M2-12", "catégorie absente devinée (au lieu de null)",
     [(RG2, '            t.setdefault("categorie_refus", None)\n', '            t.setdefault("categorie_refus", "inconnue")\n')],
     [S + "test_categorie_absente_vaut_null_donnee_gardee"]),
    ("M2-13", "coût non vérifié",
     [(RG2, '    if not _cout(l["cout_compte_usd"]):\n', "    if False:\n")],
     [E + "test_cout_hors_forme"]),
    ("M2-14", "coût négatif admis",
     [(RG2, "    return type(v) in (int, float) and math.isfinite(v) and v >= 0\n",
       "    return type(v) in (int, float) and math.isfinite(v)\n")],
     [E + "test_cout_hors_forme"]),
    ("M2-15", "classe de repli sans refusal admise",
     [(RG2, '    if l["classe_issue"] == REFUS_SERVI_PAR_REPLI and l["raison_arret"] != RAISON_REFUS:\n', "    if False:\n")],
     [E + "test_classe_de_repli_sans_refusal"]),
    ("M2-16", "refusal d'une autre classe admis",
     [(RG2, '    if l["raison_arret"] == RAISON_REFUS and l["classe_issue"] not in (REFUS_SERVI_PAR_REPLI, CLASSE_TROIS_REFUS):\n',
       "    if False:\n")],
     [E + "test_refusal_d_une_autre_classe"]),
    ("M2-17", "troisième refus dit servi par repli admis",
     [(RG2, '    if l["classe_issue"] == REFUS_SERVI_PAR_REPLI and l["rang_repli"] == RANGS_REPLI[-1]:\n',
       "    if False:\n")],
     [E + "test_troisieme_refus_dit_servi_par_repli"]),
    ("M2-18", "chaîne non close admise",
     [(RG2, '        if derniere["rang_repli"] != RANGS_REPLI[-1]:\n', "        if False:\n")],
     [E + "test_chaine_non_close", R + "test_refus_pendant_au_fichier"]),
    ("M2-19", "trois refus aux classes mêlées admis",
     [(RG2, "        if any(t[\"classe_issue\"] != CLASSE_TROIS_REFUS for t in chaine):\n", "        if False:\n")],
     [E + "test_trois_refus_aux_classes_melees"]),
    ("M2-20", "refus servi par repli non marqué de la classe de repli",
     [(RG2, "    elif any(t[\"classe_issue\"] != REFUS_SERVI_PAR_REPLI for t in chaine[:-1]):\n", "    elif False:\n")],
     [E + "test_refus_servi_marque_refus_du_modele"]),
    ("M2-21", "sans réponse avec un modèle servi admis",
     [(RG2, '        if l["modele_servi"] is not None:\n', "        if False:\n")],
     [E + "test_sans_reponse_avec_un_modele_servi"]),
    ("M2-22", "sans réponse d'une autre classe admis",
     [(RG2, '        if l["classe_issue"] != CLASSE_SANS_REPONSE:\n', "        if False:\n")],
     [E + "test_sans_reponse_d_une_autre_classe"]),
    ("M2-23", "modèle servi null admis hors sans réponse",
     [(RG2, '    sans_reponse = l["raison_arret"] == RAISON_SANS_REPONSE\n', "    sans_reponse = True\n")],
     [E + "test_modele_servi_absent_ou_mal_forme"]),
    ("M2-24", "repli sans le refus qui le précède admis",
     [(RG2, '        if p is None or p["raison_arret"] != RAISON_REFUS or p["rang_repli"] != l["rang_repli"] - 1 \\\n'
            '                or p["espece"] != l["espece"] or p["case"] != l["case"]:\n', "        if False:\n")],
     [E + "test_rangs_rompus", E + "test_repli_d_une_autre_espece_ou_case"]),
    ("M2-25", "repli d'une autre case admis",
     [(RG2, ' or p["case"] != l["case"]:\n', ":\n")],
     [E + "test_repli_d_une_autre_espece_ou_case"]),
    ("M2-26", "une chaîne de plus non exigée par écriture",
     [(RG2, "        if len(chaines_de(self._lignes + lignes, self.contexte)) != avant + 1:\n", "        if False:\n")],
     [E + "test_rangs_rompus"]),
    ("M2-27", "fiches pour une tentative qui n'est pas « fiches rendues » admises",
     [(RG2, "        if fiches and prets[-1][\"classe_issue\"] != pt.FICHES_RENDUES:\n", "        if False:\n"),
      (RG2, '    if l["classe_issue"] != pt.FICHES_RENDUES:\n', "    if False:\n"),
      (RG2, ' or t["classe_issue"] != pt.FICHES_RENDUES or ', " or ")],
     [E + "test_fiches_et_classe_fiches_rendues_vont_ensemble", E + "test_trois_refus_avec_fiches"]),
    ("M2-28", "« fiches rendues » sans fiche admise",
     [(RG2, '        if t["classe_issue"] == pt.FICHES_RENDUES and not t.fiches:\n', "        if False:\n")],
     [E + "test_fiches_et_classe_fiches_rendues_vont_ensemble", R + "test_tentative_fiches_rendues_sans_fiche_au_fichier"]),
    ("M2-29", "fiche d'une espèce qui n'est pas un proposeur admise",
     [(RG2, '    if l["espece"] not in ESPECES_PROPOSEURS:\n', "    if False:\n")],
     [E + "test_fiche_d_une_espece_qui_n_est_pas_un_proposeur"]),
    ("M2-30", "fiche d'une autre case ou génération admise",
     [(RG2, "        if issue.generation != self.contexte.generation or issue.identifiant_case != t[\"case\"]:\n",
       "        if False:\n")],
     [E + "test_fiche_d_une_autre_case_ou_generation"]),
    ("M2-31", "fiche non classée par le portier admise",
     [(RG2, "        if not isinstance(issue, pt.IssueFiche):\n            raise RegistreRefuse(\"seule une fiche classée",
       "        if False:\n            raise RegistreRefuse(\"seule une fiche classée")],
     [E + "test_fiche_qui_n_est_pas_classee_par_le_portier"]),
    ("M2-32", "fiche sans sa tentative juste avant admise",
     [(RG2, "            if t is None or t[\"classe_issue\"] != pt.FICHES_RENDUES or _champs_tentative(t.ligne) != "
            "_champs_tentative(l):\n", "            if t is None:\n")],
     [R + "test_fiche_sans_sa_tentative_juste_avant"]),
    ("M2-33", "fiche aux champs de tentative différents admise",
     [(RG2, " or _champs_tentative(t.ligne) != _champs_tentative(l):\n", ":\n")],
     [R + "test_fiche_sans_sa_tentative_juste_avant"]),
    ("M2-34", "identifiant de fiche redit admis",
     [(RG2, '            if l["identifiant"] in identifiants:\n', "            if False:\n")],
     [E + "test_identifiant_de_fiche_deux_fois"]),
    ("M2-35", "écriture directe admise",
     [(RG2, '        raise RegistreRefuse("écriture directe d\'une ligne refusée : une chaîne s\'écrit par `ajouter_chaine`")\n',
       "        return super().ajouter(champs)\n")],
     [E + "test_ecriture_directe_refusee"]),
    ("M2-36", "type de ligne hors liste admis",
     [(RG2, '    if l["type_ligne"] not in TYPES_LIGNE:\n', "    if False:\n")],
     [R + "test_type_de_ligne_hors_liste"]),
    ("M2-37", "ligne sans type non dite ancien format",
     [(RG2, '                                        or ("type_ligne" not in ligne and "classe" in ligne))\n', ")\n")],
     [R + "test_ligne_sans_type_dite_ancien_format", R + "test_ancien_format_dit_clairement"]),
    ("M2-38", "ancien format non dit à la relecture",
     [(RG2, "        if _est_v1(l):\n            raise RegistreAncienFormat(\"un registre des tentatives relu\")\n", "")],
     [R + "test_ancien_format_dit_clairement"]),
    ("M2-39", "ancien format non dit aux fonctions de compte",
     [(RG2, "        if _est_v1(l):\n            raise RegistreAncienFormat(\"une ligne donnée au lot 5 v2\")\n", "")],
     [D + "test_v1_donne_aux_fonctions_v2_refuse_en_le_disant"]),
    ("M2-40", "version de ligne non vérifiée à la relecture",
     [(RG2, '        if l.get("version") != VERSION_LIGNE:\n            raise RegistreRefuse("version de ligne inconnue")\n',
       "")],
     [R + "test_version_inconnue"]),
    ("M2-41", "lignes de tentative comptées comme fiches (garde du coffre, registre servi)",
     [(RG2, '    return [l for l in _relues(lignes) if l["type_ligne"] == TYPE_FICHE]\n', "    return list(_relues(lignes))\n")],
     [D + "test_garde_du_coffre_egale_sur_les_seules_lignes_de_fiche",
      D + "test_garde_du_coffre_ne_dilue_pas_par_les_tentatives", T + "TestComptesParType"]),
    ("M2-42", "lignes de fiche comptées comme appels",
     [(RG2, '    return [l for l in _relues(lignes) if l["type_ligne"] == TYPE_TENTATIVE]\n', "    return list(_relues(lignes))\n")],
     [T + "TestComptesParType::test_un_cout_et_un_appel_par_tentative"]),
    ("M2-43", "fiches par repli retirées des comptes de fiches",
     [(RG2, '    return [l for l in _relues(lignes) if l["type_ligne"] == TYPE_FICHE]\n',
       '    return [l for l in _relues(lignes) if l["type_ligne"] == TYPE_FICHE and l["rang_repli"] == 0]\n')],
     [D + "test_registre_servi_egal_a_l_octet", D + "test_garde_du_coffre_compte_les_fiches_par_repli_et_arrete"]),
    ("M2-44", "filiation « aucune » gardée en chaîne",
     [(RG2, "    return None if v == FILIATION_AUCUNE else v\n", "    return v\n")],
     [S + "test_chaine_simple_une_tentative_deux_fiches_tous_les_champs"]),
    ("M2-45", "filiation normalisée",
     [(RG2, "    return None if v == FILIATION_AUCUNE else v\n",
       "    return None if v.strip().lower() == FILIATION_AUCUNE else v\n")],
     [S + "test_filiation_gardee_telle_quelle"]),
    ("M2-46", "champs de fiche non null sur une ligne de tentative admis",
     [(RG2, "        if any(l[c] is not None for c in CHAMPS_DE_FICHE):\n", "        if False:\n")],
     [R + "test_tentative_aux_champs_de_fiche_non_null"]),
    ("M2-47", "fiche non passée qui porte un énoncé admise",
     [(RG2, '    elif any(l[c] is not None for c in ct.CHAMPS_FERMES + ("nom", "enonce", "filiation")):\n',
       "    elif False:\n")],
     [R + "test_fiche_non_passee_qui_porte_un_enonce"]),
    ("M2-48", "identifiant de fiche non décodé",
     [(RG2, '        ident.decoder_octets(l["identifiant"], pt.OCTETS_IDENTIFIANT)\n', "        pass\n")],
     [R + "test_fiche_au_mauvais_identifiant"]),
    ("M2-49", "énoncé sur deux lignes admis",
     [(RG2, '        if type(l["enonce"]) is not str or l["enonce"] != rg.enonce_sur_une_ligne(l["enonce"]):\n',
       "        if False:\n")],
     [R + "test_fiche_passee_enonce_sur_deux_lignes_ou_nom_autre"]),
    ("M2-50", "classe de fiche hors liste admise",
     [(RG2, '    if l["classe"] not in pt.CLASSES_FICHE:\n', "    if False:\n")],
     [R + "test_classe_de_fiche_hors_liste"]),
    ("M2-51", "génération du fichier non vérifiée",
     [(RG2, '    if not _entier(l["generation"]) or l["generation"] != contexte.generation:\n', "    if False:\n")],
     [R + "test_generation_autre_au_fichier"]),
    ("M2-52", "cases servies du contexte non vérifiées",
     [(RG2, "            ident.rang_du_mot_de_case(c)\n", "            pass\n")],
     [X + "test_artefacts"]),
    ("M2-53", "génération du contexte non vérifiée",
     [(RG2, "    if not _entier(generation) or generation not in (1, 2, 3):\n", "    if False:\n")],
     [X + "test_artefacts", X + "test_le_registre_refuse_avant_de_creer_son_fichier"]),
    ("M2-54", "chaîne de quatre tentatives admise",
     [(RG2, "    if not isinstance(tentatives, (list, tuple)) or not 1 <= len(tentatives) <= len(RANGS_REPLI):\n",
       "    if not isinstance(tentatives, (list, tuple)) or not tentatives:\n")],
     [E + "test_chaine_de_zero_ou_quatre_tentatives"]),
]

TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé",
                 [(RG2, "**Une chaîne** (additif v2, § 5)", "**Une suite** (additif v2, § 5)")],
                 [T + "TestEcritureSaine", T + "TestDifferentielV1"])


def copier(dest):
    shutil.copytree(ORCH, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))


def jouer(dossier, essais):
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *essais],
                       cwd=dossier, env=env, capture_output=True, text=True)
    lignes = [l for l in r.stdout.splitlines() if l.strip()]
    return r.returncode, (lignes[-1] if lignes else "")


def main(argv):
    if len(argv) != 1:
        print("usage : mutations_na_lot5_v2.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    with open(os.path.join(ORCH, RG2), "rb") as f:
        empreinte = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-lot5-v2-")
    rendu = {"version": "journal-mutations-na-lot5-v2", "python": sys.version.split()[0], "registre_na_v2": empreinte,
             "mutations": []}
    try:
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, TOUS)
        rendu["temoin_non_mute"] = {"code": code, "resume": resume, "passe": code == 0}
        for ident_m, nom, remplacements, essais in [TEMOIN_INERTE] + MUTATIONS:
            dossier = os.path.join(racine_tmp, ident_m)
            copier(dossier)
            valide, sources = True, {}
            for fichier, ancien, nouveau in remplacements:
                chemin = os.path.join(dossier, fichier)
                if chemin not in sources:
                    with open(chemin, encoding="utf-8") as f:
                        sources[chemin] = f.read()
                if sources[chemin].count(ancien) != 1:
                    valide = False
                    break
                sources[chemin] = sources[chemin].replace(ancien, nouveau, 1)
            entree = {"id": ident_m, "garde_retiree": nom, "essais": essais, "valide": valide}
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
