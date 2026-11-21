"""Mutations du vérificateur sur la copie d'application du lot 6 v2 : fautes par construction, prédites d'avance.
Usage : mes_mutations.py RACINE_ORCHESTRATOR [codes...]  (sans code : toutes)."""
import os
import shutil
import subprocess
import sys
import tempfile

C = "pole/course_na_v2.py"
TESTS = ["essais/test_na_lot6_v2_cablage.py", "essais/test_na_lot6_v2_course.py", "essais/test_na_lot6_v2_arrets.py"]

MUT = [
    ("V1", "construction : l'état passé au refus est toujours 0", C,
     "        refuser_cablage(course_na.etat_colonne, getattr(contexte_na, \"journal\", None),",
     "        refuser_cablage(0, getattr(contexte_na, \"journal\", None),", "tuée"),
    ("V2", "départ : l'état passé au refus est toujours 0", C,
     "            refuser_cablage(etat_colonne, journal_g1, \"départ de la course\")",
     "            refuser_cablage(0, journal_g1, \"départ de la course\")", "tuée"),
    ("V3", "refus à la génération g : journal de la génération non scellé", C,
     "                    _sceller_si_ouvert(journal)\n                    raise",
     "                    raise", "tuée"),
    ("V4", "ligne d'arrêt sans l'état de la colonne", C,
     "                 \"etat_colonne\", \"type_journal\"):", "                 \"type_journal\"):", "tuée"),
    ("V5", "ligne « départ » sans l'état de la colonne", C,
     "\"statut_des_valeurs\": config.statut, \"go\": go, \"etat_colonne\": etat_colonne})",
     "\"statut_des_valeurs\": config.statut, \"go\": go})", "tuée"),
    ("V6", "état 0 : objet non journal admis au refus", C,
     "    if not isinstance(journal, jn.JournalRequetes):\n        raise ArretCablageColonneNA(moment, etat, journal, \"le journal n'est pas un journal des requêtes du lot 3\")\n",
     "", "tuée"),
    ("V7", "clause « colonne chargée » retirée (inatteignable par le constructeur du lot 10 a)", C,
     " or not isinstance(depart.colonne, mp.Colonne):", ":", "SURVIT"),
    ("V8", "E6 : « au coffre par refus du portier » non porté à la ligne", C,
     "\"au_coffre_par_refus_du_portier\": comptes_portier[\"au_coffre_par_refus_du_portier\"],",
     "\"au_coffre_par_refus_du_portier\": 0,", "tuée"),
    ("V9", "la fabrique de la colonne rend toujours le même journal", C,
     "    def fabrique(dossier, nom):\n        return mp.JournalRequetesColonneNA(dossier, nom, depart=depart)\n    return fabrique",
     "    cache = []\n\n    def fabrique(dossier, nom):\n        if not cache:\n            cache.append(mp.JournalRequetesColonneNA(dossier, nom, depart=depart))\n        return cache[0]\n    return fabrique",
     "tuée"),
    ("V10", "refus de sceau du journal de la génération 1 tu (R5)", C,
     "                arret[\"journal_requetes_g1\"] = f\"scellement refusé ({refus_sceau_g1})\"",
     "                pass", "SURVIT"),
    ("V11", "renforcement affaibli : état du journal de la colonne supérieur admis", C,
     "depart.etat != etat or", "depart.etat < etat or", "tuée"),
    ("V12", "refus à la construction placé après le constructeur hérité", C,
     "        refuser_cablage(course_na.etat_colonne, getattr(contexte_na, \"journal\", None),\n"
     "                        f\"construction de la génération {numero}\")\n"
     "        self.course_na = course_na\n"
     "        super().__init__(conf, sortie, adaptateurs, contexte_na=contexte_na, numero=numero, **kw)\n",
     "        self.course_na = course_na\n"
     "        super().__init__(conf, sortie, adaptateurs, contexte_na=contexte_na, numero=numero, **kw)\n"
     "        refuser_cablage(course_na.etat_colonne, getattr(contexte_na, \"journal\", None),\n"
     "                        f\"construction de la génération {numero}\")\n", "tuée"),
    ("V13", "refus : sous-classe tolérée par type() au lieu de isinstance (resserrement, doit rester vert)", C,
     "        if not isinstance(journal, mp.JournalRequetesColonneNA):",
     "        if type(journal) is not mp.JournalRequetesColonneNA:", "SURVIT (resserrement sain)"),
    ("W1", "E7 : refus de la table non « course » retiré dans la configuration (la lecture l'exige peut-être déjà)",
     "pole/configuration_course_na_v1.py",
     "    if t.marque != rt.MARQUE_COURSE:\n        raise rt.TableRefusee(\"table de routage : seule une table « course » part\")\n", "",
     "tuée ou équivalente"),
    ("W2", "E8 : empreinte du corps non gardée par le faux fournisseur", "pole/simulation_na_v1.py",
     "\"corps_sha256\": e[\"corps_sha256\"],", "\"corps_sha256\": \"\",", "tuée"),
    ("W3", "E8 : taille du corps non gardée par le faux fournisseur", "pole/simulation_na_v1.py",
     "\"corps_taille\": e[\"corps_taille\"],", "\"corps_taille\": 0,", "tuée"),
]


def jouer(racine, m):
    code, quoi, fichier, avant, apres, prediction = m
    base = tempfile.mkdtemp(prefix="vmut-")
    copie = os.path.join(base, "orchestrator")
    try:
        shutil.copytree(racine, copie, ignore=shutil.ignore_patterns("__pycache__"))
        chemin = os.path.join(copie, fichier)
        with open(chemin, encoding="utf-8") as f:
            texte = f.read()
        n = texte.count(avant)
        if n != 1:
            return f"{code} | {quoi} | INVALIDE (texte présent {n} fois)"
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(texte.replace(avant, apres, 1))
        r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", *TESTS],
                           cwd=copie, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"), capture_output=True, text=True)
        issue = "SURVIT" if r.returncode == 0 else "tuée"
        causes = [l for l in r.stdout.splitlines() if l.startswith("FAILED") or l.startswith("E  ") or l.startswith("ERROR")][:4]
        return f"{code} | {quoi} | prédit : {prediction} | rendu : {issue} | {' // '.join(causes)}"
    finally:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    racine = os.path.abspath(sys.argv[1])
    codes = sys.argv[2:]
    for m in MUT:
        if not codes or m[0] in codes:
            print(jouer(racine, m), flush=True)
