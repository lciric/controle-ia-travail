"""Mutations du lot 10 a du véhicule NA-1 : pour chaque garde, la garde retirée fait échouer son essai (R5 ; manière de la
v68, R68, § 4, reprise par les programmes des lots 1 à 5).

Pour chaque mutation : une copie neuve, dans un dossier temporaire, du dossier `orchestrator` entier où le programme est
posé (lots 2 v5, 3 v3, 4 v1, 5 v1 et 10 a posés, base `a41b7b50…`) ; un ou plusieurs remplacements à texte exact dans le
module `matiere_premiere_na_v1` (chaque texte cherché doit y être une fois exactement, sinon la mutation est dite
invalide) ; puis les essais nommés de cette garde, joués dans un processus à part. La mutation est « tuée » si et seulement
si pytest rend le code 1. Avant cela, le fichier d'essais entier est joué sur une copie non mutée : il doit passer (code 0).
Un témoin inerte (un mot de docstring changé) doit survivre.

Usage : `python -B mutations_na_lot10a_v1.py JOURNAL.json` (le journal ne doit pas exister : R12). Aucun réseau, aucune clé ;
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
MP = "pole/matiere_premiere_na_v1.py"
T = "essais/test_na_lot10a_v1_matiere_premiere.py::"
TOUS = ["essais/test_na_lot10a_v1_matiere_premiere.py"]
FICHIERS_EMPREINTES = (MP, "essais/aides_na_lot10a_v1.py", "essais/test_na_lot10a_v1_matiere_premiere.py")

CH = T + "TestChargeur::"
ID = T + "TestIdentifiantDeLigne::"
GE = T + "TestGardeEnonceEntier::"
G3 = T + "TestGardeAuPasTrois::"
RS = T + "TestRegistreServi::"
PF = T + "TestPiecesFixes::"
SL = T + "TestSixiemeLigne::"
IN = T + "TestInterrupteur::"
FR = T + "TestFauxRefus::"
RF = T + "TestRienNeFuit::"

MUTATIONS = [
    ("X-01", "garde de la colonne retirée (aucune ligne ne mord)",
     [(MP, "        return self._par_empreinte.get(_empreinte_forme(forme), ())\n", "        return ()\n")],
     [GE + "test_ligne_entiere_en_clair_mord", G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme",
      RS + "test_artefact_la_generation_ne_part_pas_aucune_ligne_retiree", T + "TestPiecesFixes"]),
    ("X-02", "normalisation retirée",
     [(MP, "    return normaliseur.normaliser(texte).strip()\n", "    return texte.strip()\n")],
     [GE + "test_forme_que_la_normalisation_ramene_mord"]),
    ("X-03", "bords non retirés après la normalisation",
     [(MP, "    return normaliseur.normaliser(texte).strip()\n", "    return normaliseur.normaliser(texte)\n")],
     [GE + "test_forme_que_la_normalisation_ramene_mord"]),
    ("X-04", "empreinte du registre non vérifiée",
     [(MP, "    if type(empreinte_attendue) is not str or sha != empreinte_attendue:\n        raise ColonneNonChargee(",
       "    if False:\n        raise ColonneNonChargee(")],
     [CH + "test_empreinte_fausse_refusee_avant_toute_lecture",
      CH + "test_registre_d_une_autre_empreinte_depuis_le_disque"]),
    ("X-05", "registre lu avant la vérification de son empreinte",
     [(MP, "    octets = bytes(octets)\n    sha = hashlib.sha256(octets).hexdigest()\n",
       "    octets = bytes(octets)\n    json.loads(octets.decode(\"utf-8\"))\n    sha = hashlib.sha256(octets).hexdigest()\n")],
     [CH + "test_empreinte_fausse_refusee_avant_toute_lecture"]),
    ("X-06", "forme de l'arrêt n° 19 retirée",
     [(MP, "        forme_defauts = [c for n, c in vr.verifier_enonce(enonce, borne_enonce_octets) if n == NUMERO_ARRET_FORME]\n",
       "        forme_defauts = []\n")],
     [CH + "test_enonce_non_conforme_colonne_non_chargee_sans_retrait"]),
    ("X-07", "retrait silencieux : les entrées non conformes sont laissées de côté",
     [(MP, "    if defauts:\n        raise ColonneNonChargee(\"registre non conforme\"",
       "    if False:\n        raise ColonneNonChargee(\"registre non conforme\"")],
     [CH + "test_enonce_non_conforme_colonne_non_chargee_sans_retrait", CH + "test_entree_d_une_autre_forme"]),
    ("X-08", "champs de l'entrée non vérifiés",
     [(MP, "        if not isinstance(entree, dict) or set(entree) != attendus:\n",
       "        if not isinstance(entree, dict):\n")],
     [CH + "test_entree_d_une_autre_forme"]),
    ("X-09", "énoncé vide après normalisation admis",
     [(MP, "        if not forme:\n            defauts.append((rang, \"énoncé vide après normalisation\"))\n",
       "        if False:\n            defauts.append((rang, \"énoncé vide après normalisation\"))\n")],
     [CH + "test_entree_d_une_autre_forme"]),
    ("X-10", "longueur de l'identifiant de ligne non vérifiée",
     [(MP, "        if type(brut) is not bytes or len(brut) != OCTETS_IDENTIFIANT_LIGNE:\n",
       "        if type(brut) is not bytes:\n")],
     [ID + "test_identifiant_refuse_colonne_non_chargee"]),
    ("X-11", "identifiant de ligne en double admis",
     [(MP, "        if identifiant in vus:\n", "        if False:\n")],
     [ID + "test_identifiant_refuse_colonne_non_chargee"]),
    ("X-12", "repli silencieux quand la fonction d'identifiant échoue",
     [(MP, "            defauts.append((rang, f\"identifiant de ligne : la fonction donnée a échoué ({type(e).__name__})\"))\n"
           "            continue\n",
       "            brut = rang.to_bytes(6, \"big\")\n")],
     [ID + "test_identifiant_refuse_colonne_non_chargee"]),
    ("X-13", "source de l'identifiant de ligne fixée par défaut",
     [(MP, "def lire_registre(octets, empreinte_attendue, *, normaliseur, octets_identifiant_ligne, champ_enonce,",
       "def lire_registre(octets, empreinte_attendue, *, normaliseur, champ_enonce, "
       "octets_identifiant_ligne=lambda r, e: r.to_bytes(6, \"big\"),")],
     [ID + "test_aucune_source_fixee_par_le_module"]),
    ("X-14", "entrée remise modifiable à la fonction d'identifiant",
     [(MP, "            brut = octets_identifiant_ligne(rang, types.MappingProxyType(dict(entree)))\n",
       "            brut = octets_identifiant_ligne(rang, entree)\n")],
     [ID + "test_la_fonction_ne_peut_pas_changer_l_entree"]),
    ("X-15", "nombre d'entrées attendu non vérifié",
     [(MP, "    if entrees_attendues is not None and len(obj) != entrees_attendues:\n", "    if False:\n")],
     [CH + "test_nombre_d_entrees_attendu"]),
    ("X-16", "sixième ligne absente : état par défaut pris en silence",
     [(MP, "        raise DepartRefuseColonneNA(\"ligne de l'état de l'interrupteur absente de la pièce de relevés\")\n",
       "        return LigneEtat(ETAT_PAR_DEFAUT, empreinte_piece, \"\", 0)\n")],
     [SL + "test_ligne_refusee_depart_refuse"]),
    ("X-17", "sixième ligne en double admise",
     [(MP, "    if len(a_libelle) > 1:\n", "    if False:\n")],
     [SL + "test_ligne_refusee_depart_refuse"]),
    ("X-18", "ligne d'un autre libellé admise",
     [(MP, "    if autres:\n", "    if False:\n")],
     [SL + "test_ligne_refusee_depart_refuse"]),
    ("X-19", "empreinte de la pièce de relevés non vérifiée",
     [(MP, "    if type(empreinte_piece) is not str or hashlib.sha256(piece_octets).hexdigest() != empreinte_piece:\n",
       "    if False:\n")],
     [SL + "test_empreinte_de_la_piece_fausse"]),
    ("X-20", "empreinte du registre de la ligne non comparée à celle qui est écrite",
     [(MP, "    if type(empreinte_registre_attendue) is not str or ligne.registre_sha256 != empreinte_registre_attendue:\n",
       "    if False:\n")],
     [SL + "test_empreinte_du_registre_fausse_dans_la_ligne"]),
    ("X-21", "nom d'état non comparé au numéro",
     [(MP, "    if NOMS_ETATS[etat] != m.group(\"nom\"):\n", "    if False:\n")],
     [SL + "test_ligne_refusee_depart_refuse"]),
    ("X-22", "variable d'environnement non lue",
     [(MP, "    if noms:\n        raise EtatRefuseNA(", "    if False:\n        raise EtatRefuseNA(")],
     [IN + "test_aucun_etat_par_variable_d_environnement"]),
    ("X-23", "casse du nom de variable non repliée",
     [(MP, "if any(f in k.upper() for f in FRAGMENTS_ENV_INTERDITS)", "if any(f in k for f in FRAGMENTS_ENV_INTERDITS)")],
     [IN + "test_aucun_etat_par_variable_d_environnement"]),
    ("X-24", "configuration non comparée à la pièce de relevés",
     [(MP, "    if CLE_CONFIGURATION in configuration and configuration[CLE_CONFIGURATION] != ligne.etat:\n",
       "    if False:\n")],
     [IN + "test_aucun_etat_par_la_configuration_seule"]),
    ("X-25", "état 2 sans règle d'allumage",
     [(MP, "    if ligne.etat == ETAT_ALLUMEE:\n        manques", "    if False:\n        manques")],
     [IN + "test_etat_2_refuse_sans_additif", IN + "test_e4_manifeste_artefacts",
      IN + "test_etat_2_chaque_condition_manquante"]),
    ("X-26", "E4 : l'empreinte de l'additif prise dans la configuration",
     [(MP, "        manques = _manques_allumage(conditions_allumage, ligne.registre_sha256)\n",
       "        manques = [] if configuration.get(CLE_EMPREINTE_ADDITIF) else "
       "_manques_allumage(conditions_allumage, ligne.registre_sha256)\n")],
     [IN + "test_e4_empreinte_posee_dans_la_configuration_seulement"]),
    ("X-27", "E4 : manifeste absent admis",
     [(MP, "        return [\"(b) manifeste de la lecture de fin absent\"]\n", "        return []\n")],
     [IN + "test_e4_manifeste_artefacts"]),
    ("X-28", "E4 : empreinte absente du manifeste admise",
     [(MP, "    if CLE_EMPREINTE_ADDITIF not in obj:\n", "    if False:\n"),
      (MP, "    if obj[CLE_EMPREINTE_ADDITIF] != attendue:\n", "    if obj.get(CLE_EMPREINTE_ADDITIF, attendue) != attendue:\n")],
     [IN + "test_e4_manifeste_artefacts"]),
    ("X-29", "E4 : empreinte fausse admise",
     [(MP, "    if obj[CLE_EMPREINTE_ADDITIF] != attendue:\n", "    if False:\n")],
     [IN + "test_e4_manifeste_artefacts"]),
    ("X-30", "(a) ligne d'accord sans l'état 2",
     [(MP, " or \"état 2\" not in a or ", " or ")],
     [IN + "test_etat_2_chaque_condition_manquante"]),
    ("X-31", "(c) devis sur une autre ligne admis",
     [(MP, "d.get(\"ligne\") == LIGNE_DEVIS and ", "")],
     [IN + "test_etat_2_chaque_condition_manquante"]),
    ("X-32", "(d) lecteurs hors des juges de fin admis",
     [(MP, " or not set(lec) <= set(JUGES_DE_FIN)", "")],
     [IN + "test_etat_2_chaque_condition_manquante"]),
    ("X-33", "(e) branche orpheline lue comme vrai au sens large",
     [(MP, "    if c.branche_orpheline is not True:\n", "    if not c.branche_orpheline:\n")],
     [IN + "test_etat_2_chaque_condition_manquante"]),
    ("X-52", "(a) ligne d'accord sans l'empreinte du registre",
     [(MP, " or registre_sha256 not in a:\n", ":\n")],
     [IN + "test_etat_2_chaque_condition_manquante"]),
    ("X-34", "tenue (ii) retirée au journal",
     [(MP, "            if constats:\n                c = constats[0]\n", "            if False:\n                c = constats[0]\n")],
     [G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme", G3 + "test_sonde_gardee"]),
    ("X-35", "ligne « non envoyé » omise",
     [(MP, "                self.journaliser_non_envoye(arret=ARRET_COLONNE,", "                (lambda **k: None)(arret=ARRET_COLONNE,")],
     [G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme",
      G3 + "test_journal_en_panne_requete_journalisee"]),
    ("X-36", "refus compté omis",
     [(MP, "                self.comptes_colonne[role] = self.comptes_colonne.get(role, 0) + 1\n", "                pass\n")],
     [G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme"]),
    ("X-37", "refus écrit mais l'envoi continue",
     [(MP, "                raise ArretColonneNA(role, c.rang_ligne, c.identifiants)\n", "                pass\n")],
     [G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme", G3 + "test_cumul_de_la_cle_inchange"]),
    ("X-38", "proposeur hors de la tenue (ii)",
     [(MP, "SORTES_GARDEES = (\"proposeur\", \"sonde_refus\")", "SORTES_GARDEES = (\"sonde_refus\",)")],
     [G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme"]),
    ("X-39", "sonde hors de la tenue (ii)",
     [(MP, "SORTES_GARDEES = (\"proposeur\", \"sonde_refus\")", "SORTES_GARDEES = (\"proposeur\",)")],
     [G3 + "test_sonde_gardee"]),
    ("X-40", "journal construit sans contrôle de départ",
     [(MP, "        if not isinstance(depart, DepartColonne):\n            raise jn.JournalRefuse(",
       "        if False:\n            raise jn.JournalRefuse(")],
     [G3 + "test_journal_exige_le_controle_de_depart"]),
    ("X-41", "tenue (iii) retirée",
     [(MP, "    if constats:\n        raise GenerationRefuseeColonneNA(", "    if False:\n        raise GenerationRefuseeColonneNA(")],
     [RS + "test_artefact_la_generation_ne_part_pas_aucune_ligne_retiree"]),
    ("X-42", "tenue (iii) : énoncés du registre servi non comparés",
     [(MP, "        ids = depart.colonne.examiner_ligne(enonce)\n", "        ids = ()\n")],
     [RS + "test_artefact_la_generation_ne_part_pas_aucune_ligne_retiree"]),
    ("X-43", "pièce fixe qui porte un énoncé admise",
     [(MP, "    if refus:\n        raise DepartRefuseColonneNA(", "    if False:\n        raise DepartRefuseColonneNA(")],
     [PF + "test_piece_qui_porte_un_enonce_entier_depart_refuse"]),
    ("X-44", "pièces fixes non contrôlées au départ",
     [(MP, "    controler_pieces_fixes(colonne, pieces_fixes)\n", "")],
     [PF + "test_piece_qui_porte_un_enonce_entier_depart_refuse"]),
    ("X-45", "état 0 qui charge quand même",
     [(MP, "    if etat == ETAT_ETEINTE:\n        return DepartColonne(", "    if False:\n        return DepartColonne(")],
     [IN + "test_etat_0_rien_n_est_charge"]),
    ("X-46", "colonne chargée d'un autre registre que la ligne admise",
     [(MP, "    if not isinstance(colonne, Colonne) or colonne.registre_sha256 != ligne.registre_sha256:\n",
       "    if not isinstance(colonne, Colonne):\n")],
     [SL + "test_registre_charge_d_une_autre_empreinte_que_la_ligne"]),
    ("X-47", "mesure du faux refus qui ne compte rien",
     [(MP, "        refusees += n\n", "        refusees += 0\n")],
     [FR + "test_la_mesure_voit_un_refus_plante"]),
    ("X-48", "énoncé normalisé gardé à la place de son empreinte",
     [(MP, "            couples.append((identifiant, _empreinte_forme(forme)))\n",
       "            couples.append((identifiant, forme))\n"),
      (MP, "        return self._par_empreinte.get(_empreinte_forme(forme), ())\n",
       "        return self._par_empreinte.get(forme, ())\n")],
     [CH + "test_cas_sain_trente_cinq_empreintes_seules", CH + "test_ni_nom_ni_enonce_ni_autre_champ_garde"]),
    ("X-49", "recherche d'absence aveugle",
     [(MP, "                n = sum(contenu.count(a) for a in aiguilles)\n", "                n = 0\n")],
     [RF + "test_la_recherche_voit_un_texte_plante"]),
    ("X-50", "colonne chargée modifiable",
     [(MP, "        raise AttributeError(\"une colonne chargée ne change pas\")\n", "        object.__setattr__(self, *_)\n")],
     [CH + "test_la_colonne_ne_change_pas"]),
    ("X-51", "contenu de la requête recopié dans la ligne « non envoyé »",
     [(MP, "f\"{', '.join(c.identifiants)} ; {len(constats)} ligne(s) en tout\",",
       "f\"{', '.join(c.identifiants)} ; {requete.octets.decode('utf-8')[-300:]}\",")],
     [G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme", T + "TestRienNeFuit"]),
]

TEMOIN_INERTE = ("T-00", "mutation inerte : un mot de la docstring changé",
                 [(MP, "Ce que la garde ne tient pas : un énoncé repris en substance",
                   "Ce que la garde ne retient pas : un énoncé repris en substance")],
                 [T + "TestGardeEnonceEntier", G3 + "test_artefact_ligne_egale_non_envoye_cout_nul_arret_nomme"])


def jouer(dossier, essais):
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LANG": "C.UTF-8"}
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", *essais],
                       cwd=dossier, env=env, capture_output=True, text=True)
    lignes = [l for l in r.stdout.splitlines() if l.strip()]
    return r.returncode, (lignes[-1] if lignes else "")


def copier(dest):
    shutil.copytree(ORCH, dest, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))


def main(argv):
    if len(argv) != 1:
        print("usage : mutations_na_lot10a_v1.py JOURNAL.json", file=sys.stderr)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print("journal existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    empreintes = {}
    for rel in FICHIERS_EMPREINTES:
        with open(os.path.join(ORCH, rel), "rb") as f:
            empreintes[rel] = hashlib.sha256(f.read()).hexdigest()
    racine_tmp = tempfile.mkdtemp(prefix="mutations-na-lot10a-v1-")
    rendu = {"version": "journal-mutations-na-lot10a-v1", "python": sys.version.split()[0], "fichiers": empreintes,
             "mutations": []}
    try:
        base = os.path.join(racine_tmp, "base")
        copier(base)
        code, resume = jouer(base, TOUS)
        rendu["temoin_non_mute"] = {"essais": "le fichier entier", "code": code, "resume": resume, "passe": code == 0}
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
