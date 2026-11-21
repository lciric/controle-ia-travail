"""Mutations des lots 1 et 2 du véhicule NA-1 : pour chaque garde, la garde retirée fait échouer son essai (R5 ; manière de
la v68, R68, § 4 : « trois mutations montrent que les essais ont des dents »).

Pour chaque mutation : une copie neuve des seuls fichiers des lots 1 et 2 dans un dossier temporaire ; un ou plusieurs
remplacements à texte exact dans un module (chaque texte cherché doit y être une fois exactement, sinon la mutation est dite
invalide) ; puis les essais nommés de cette garde, joués dans un processus à part. La mutation est « tuée » si et seulement
si pytest rend le code 1 (des essais échouent) ; tout autre code (essai qui passe, erreur de collecte) est un échec du
programme. Avant cela, les mêmes essais sont joués sur une copie non mutée : ils doivent passer (code 0).

Usage, depuis n'importe où : `python -B mutations_na_v1.py JOURNAL.json` (le journal ne doit pas exister : R12).
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
    "pole/tirage_na_v1.py",
    "pole/garde_motifs_na_v1.py",
    "essais/aides_na_v1.py",
    "essais/liste-motifs-essai-na-v1.json",
    "essais/test_na_v1_tirage.py",
    "essais/test_na_v1_garde_motifs.py",
)

T = "essais/test_na_v1_tirage.py::"
G = "essais/test_na_v1_garde_motifs.py::"
TI = "pole/tirage_na_v1.py"
ID = "pole/identifiants_na_v1.py"
GM = "pole/garde_motifs_na_v1.py"

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
    ("L2-01", "normalisation retirée", GM,
     [("    t = _ESPACES.sub(\" \", t)\n    return t\n", "    return texte\n")],
     [G + "TestNormalisation::test_formes_ramenees",
      G + "TestArret16ParFamille::test_famille_composition_et_tenue_forme_ramenee"]),
    ("L2-02", "invisibles non retirés", GM,
     [("    t = \"\".join(ch for ch in texte if unicodedata.category(ch) != \"Cf\")\n", "    t = texte\n"),
      ("    t = \"\".join(ch for ch in t if unicodedata.category(ch) != \"Cf\")\n", "    pass\n")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_forme_ramenee"]),
    ("L2-03", "forme de compatibilité retirée", GM,
     [("    t = unicodedata.normalize(\"NFKC\", t)\n    t = t.casefold()\n    t = unicodedata.normalize(\"NFKC\", t)\n",
       "    t = t.casefold()\n")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_forme_ramenee"]),
    ("L2-04", "casse non repliée", GM,
     [("    t = t.casefold()\n", "    pass\n")],
     [G + "TestNormalisation::test_formes_ramenees"]),
    ("L2-05", "tirets non ramenés", GM,
     [("    t = \"\".join(\"-\" if (unicodedata.category(ch) == \"Pd\" or ch in _TIRETS_HORS_PD) else ch for ch in t)\n",
       "    pass\n")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_forme_ramenee"]),
    ("L2-06", "espaces non ramenés", GM,
     [("    t = _ESPACES.sub(\" \", t)\n", "    pass\n")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_forme_ramenee"]),
    ("L2-07", "seconde famille non lue", GM,
     [("        for _nom, motifs in self.liste.familles:\n", "        for _nom, motifs in self.liste.familles[:1]:\n")],
     [G + "TestArret16ParFamille::test_famille_composition_et_tenue_en_clair"]),
    ("L2-08", "première famille non lue", GM,
     [("        for _nom, motifs in self.liste.familles:\n", "        for _nom, motifs in self.liste.familles[1:]:\n")],
     [G + "TestArret16ParFamille::test_famille_identite_et_depot_en_clair"]),
    ("L2-09", "témoins positifs non vérifiés", GM,
     [("            if motif.chercher(normaliser(motif.temoin_positif)) is None:\n", "            if False:\n")],
     [G + "TestTemoinsPositifs::test_un_motif_qui_ne_mord_pas_refuse_le_depart",
      G + "TestTemoinsPositifs::test_temoins_rejoues_a_chaque_depart"]),
    ("L2-10", "copie retirée : la garde rend le tampon de l'appelant", GM,
     [("        octets = bytes(requete)\n", "        octets = requete\n"),
      ("        if type(self.octets) is not bytes:\n", "        if False:\n")],
     [G + "TestDernierPointAvantEnvoi::test_aucun_octet_change_apres_la_garde"]),
    ("L2-11", "empreinte de la liste non vérifiée", GM,
     [("    if type(empreinte_attendue) is not str or sha != empreinte_attendue:\n", "    if False:\n")],
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
    ("L2-15", "envoi avant la ligne de journal", GM,
     [("    journal({**meta, \"evenement\": \"envoi\", \"taille\": rg.taille, \"sha256\": rg.sha256})\n"
       "    verifier_avant_envoi(rg, rg.octets)\n    return envoyer(rg.octets)\n",
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
        print("usage : mutations_na_v1.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in FICHIERS:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-v1-")
    rendu = {"version": "journal-mutations-na-v1", "python": sys.version.split()[0], "fichiers": empreintes,
             "mutations": []}
    try:
        tous = sorted({e for m in MUTATIONS for e in m[4]})
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, tous)
        rendu["temoin_non_mute"] = {"essais": len(tous), "code": code, "resume": resume, "passe": code == 0}
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
    rendu["bilan"] = {"mutations": n, "tuees": tuees, "temoin_non_mute_passe": rendu["temoin_non_mute"]["passe"],
                      "temoin_inerte_survit": rendu["temoin_inerte"]["survit_comme_attendu"],
                      "conforme": tuees == n and rendu["temoin_non_mute"]["passe"]
                      and rendu["temoin_inerte"]["survit_comme_attendu"]}
    with open(journal, "x", encoding="utf-8") as f:
        f.write(json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1) + "\n")
    print(json.dumps(rendu["bilan"], ensure_ascii=False))
    return 0 if rendu["bilan"]["conforme"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
