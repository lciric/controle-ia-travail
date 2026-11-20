"""Passage de mutations sur la seconde programmation du dénombrement exact et de la table des issues (barreau 5),
version 3 du module (couples S1 à S11 de la contre-lecture appliqués).

Pour chaque mutation : une copie du module, changée en un seul endroit, est écrite dans `/dev/shm`, et les essais neufs
de la seconde programmation sont joués sur elle (variable d'environnement `B5F_SECONDE_MODULE`). Une mutation est
« attrapée » si les essais échouent (code de sortie 1 de pytest). Le module du dépôt n'est jamais modifié ; le
programme de lecture n'est jamais joué. Aucun aléa. Les fichiers temporaires sont effacés à la fin par leur chemin.

Par rapport à l'outil de la version 2 : O05, M01 et M05 sont gardées, sur les « avant » du code corrigé ; s'ajoutent
les mutations des couples (O05b, O16, M01b, M05b, M06, C13b, C24 à C29) et celles de la contre-lecture (X1 à X3 ; X4 est
M01b, X5 est F06).

Lancement, depuis la racine du dépôt :
    PYTHONPATH=src .venv/bin/python -B <ce fichier> <journal de sortie .json>
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys

RACINE = "/home/user/controle-ia-travail"
MODULE = RACINE + "/src/controle_ia/barreau5_familles/seconde_programmation_v3.py"
ESSAIS = RACINE + "/tests/test_barreau5_familles_seconde_programmation_v3.py"
DOSSIER = "/dev/shm/b5f-seconde-programmation-mutations-v3"
MUTANT = "/dev/shm/b5f-seconde-programmation-mutations-v3/mutant.py"

# (nom, texte d'origine présent une seule fois dans le module, texte muté, règle visée)
MUTATIONS = [
    ("N01", "    if k >= 8:", "    if k >= 9:", "niveau 99 à huit familles ou plus"),
    ("N02", "    if k >= 6:", "    if k >= 5:", "aucun niveau sous six familles"),
    ("N03", "99: Fraction(1, 200)", "99: Fraction(1, 100)", "0,005 par sens au niveau de 99 %"),
    ("N04", "95: Fraction(1, 40)", "95: Fraction(1, 20)", "0,025 par sens au niveau de 95 %"),
    ("L01", "range(len(comptes) - 1, rang - 1, -1)", "range(len(comptes) - 1, rang, -1)", "loi exacte des 2^K signes"),
    ("R01", "contre = [x <= 0 for x in d]", "contre = [x < 0 for x in d]", "différence nulle contre « séparé »"),
    ("R02", "contre = [x >= 0 for x in d]", "contre = [x > 0 for x in d]", "différence nulle contre « contraire »"),
    ("R03", "(abs(d[i]), contre[i])", "(abs(d[i]), not contre[i])", "égaux dans l'ordre le plus défavorable"),
    ("V01", "w is not None and w_moins <= w:", "w is not None and w_moins < w:", "« séparé » si W⁻ ≤ w(K)"),
    ("V02", "w is not None and w_plus <= w:", "w is not None and w_plus < w:", "« contraire » si W⁺ ≤ w(K)"),
    ("V03", '"p_separe": float(probabilite_exacte(k, w_moins)),', '"p_separe": float(probabilite_exacte(k, w_plus)),',
     "probabilité exacte du sens « séparé »"),
    ("V04", '"positives": sum(1 for x in d if x > 0),', '"positives": sum(1 for x in d if x >= 0),', "signes seuls"),
    ("F01", '"S": ("M1", "M3", "E1", "E2a", "E2b", "E3"),', '"S": ("E1", "E2a", "E2b", "E3"),',
     "addendum, point 1 : M1 et M3 fondent S"),
    ("F02", '"D": ("M1", "M3", "E3"),', '"D": ("M1", "M3", "E1", "E2a", "E2b", "E3"),',
     "addendum, point 1 : pour D, seule E3 compte, avec M1 et M3"),
    ("F03", '"C": ("M1", "M3", "E3"),', '"C": ("E3",),', "addendum, point 1 : M1 et M3 fondent C"),
    ("F04", "return min(niveaux)", "return max(niveaux)", "niveau d'une issue : le plus faible"),
    ("F05", "        if niveau == 95:", "        if niveau == 99:", "le niveau de 95 % dans le nom"),
    ("F06", '    if r["niveau"] == 95:', '    if r["niveau"] == 99:', "le niveau de 95 % dans la phrase"),
    ("A01", "return all(x > 0 for x in d) and borne_basse_99 > 0", "return all(x > 0 for x in d) and borne_basse_99 >= 0",
     "séparation apprise : borne basse strictement positive"),
    ("A02", "return all(x > 0 for x in d) and borne_basse_99 > 0", "return all(x >= 0 for x in d) and borne_basse_99 > 0",
     "séparation apprise : chaque famille positive"),
    ("O01", "    if garde_arret is not None:", "    if False:", "NI par une garde de la liste d'arrêt"),
    ("O02", "    if niveau_de(k_e3) is None:", "    if False:", "moins de six familles de E3 : N, avant NI"),
    ("O03", '        elif epreuves[m]["verdict"] != SEPARE:', '        elif epreuves[m]["verdict"] == CONTRAIRE:',
     "manipulation établie : M1 et M3 « séparé »"),
    ("O04", '        if epreuves[m]["niveau"] is None:', "        if False:", "addendum, point 1, règle 4 : motif de NI"),
    ("O05", "    if sonde_decisive_echec is not False:", "    if False:", "sonde en échec : issue N"),
    ("O05b", "    if sonde_decisive_echec is not False:", "    if sonde_decisive_echec:",
     "sonde en échec : tout motif de l'instance, même vide (couple S4)"),
    ("O06", '    if verdicts["E3"] == CONTRAIRE:', '    if verdicts["E3"] == CONTRAIRE and False:', "issue C"),
    ("O07", 'manquent = [e for e in ("E2a", "E2b", "E1") if verdicts[e] != SEPARE]',
     'manquent = [e for e in ("E2a", "E1") if verdicts[e] != SEPARE]', "S exige E2b"),
    ("O08", 'manquent = [e for e in ("E2a", "E2b", "E1") if verdicts[e] != SEPARE]',
     'manquent = [e for e in ("E2b", "E1") if verdicts[e] != SEPARE]', "S exige E2a"),
    ("O09", 'manquent = [e for e in ("E2a", "E2b", "E1") if verdicts[e] != SEPARE]',
     'manquent = [e for e in ("E2a", "E2b") if verdicts[e] != SEPARE]', "S exige E1"),
    ("O10", "    if etablie:", "    if True:", "E exige la séparation apprise établie"),
    ("O11", 'if max(abs(e3["min"]), abs(e3["max"])) < MOITIE * delta_app:',
     'if max(abs(e3["min"]), abs(e3["max"])) <= MOITIE * delta_app:', "E : inégalité stricte"),
    ("O12", 'if max(abs(e3["min"]), abs(e3["max"])) < MOITIE * delta_app:', 'if e3["max"] < MOITIE * delta_app:',
     "E : valeur absolue de d_k"),
    ("O13", "MOITIE = 0.5", "MOITIE = 1.0", "E : la moitié de la séparation apprise"),
    ("O14", 'rendu["mention_e1"] = verdicts["E1"] == SEPARE', 'rendu["mention_e1"] = verdicts["E1"] != SEPARE',
     "N : E1 « séparé » sans E3, la phrase le dit"),
    ("O15", 'rendu["manipulation_etablie"] = not en_cause', 'rendu["manipulation_etablie"] = bool(en_cause)',
     "manipulation établie rendue"),
    ("O16", "            en_cause.append(m)", '            en_cause.append(f"{m} non « séparé »")',
     "motif ordinaire de NI : l'épreuve nommée seule (couple S1)"),
    ("M01", "motifs = [f\"force non écartée ({', '.join(force)})\"] if force else []",
     'motifs = ["force non écartée"] if force else []', "D : le motif dit laquelle"),
    ("M01b", "motifs = [f\"force non écartée ({', '.join(force)})\"] if force else []",
     'motifs = [f"force non écartée ({e})" for e in force]', "D : un seul motif de force (couple S3)"),
    ("M02", 'motifs.append("saboteur non établi")', 'motifs.append("saboteur non etabli")', "D : motif du saboteur"),
    ("M03", 'motifs=[MENTION_E1] if rendu["mention_e1"] else []', "motifs=[]", "N : mention du saboteur"),
    ("M04", 'motifs=["niveau non atteignable"]', 'motifs=["niveau non atteignable : " + _familles(k_e3)]',
     "N : motif « niveau non atteignable »"),
    ("M05", 'motifs=[f"sonde en échec : épreuves non calculables ({motif_echec})"]', 'motifs=["non calculables"]',
     "N : motif de la sonde en échec (couple S4)"),
    ("M05b", 'motif_echec = "sonde décisive" if sonde_decisive_echec is True else str(sonde_decisive_echec)',
     'motif_echec = "sonde décisive"', "N : le motif de l'instance dans le motif de l'issue (couple S4)"),
    ("M06", "{en_lettres(k) if k >= 1 else k} famille", "{en_lettres(k)} famille", "« 0 famille » (couple S2)"),
    ("P01", '"E2a": "le long de ce que la famille partage",', '"E2a": "le long de ce que tous les adaptateurs partagent",',
     "phrase D : laquelle des deux poussées"),
    ("P02", 'if r["cause_ni"] == "garde"', 'if r["cause_ni"] != "garde"', "phrase NI : la cause"),
    ("P03", 'plus_grand = max(abs(e3["min"]), abs(e3["max"]))', 'plus_grand = e3["max"]', "phrase E : le plus grand écart"),
    ("P04", "{fr(MOITIE * delta_app, 3)} n'est pas exclue.", "{fr(e3['max'], 3)} n'est pas exclue.",
     "addendum, point 3 : la borne vaut ½ Δ_app"),
    ("P05", 'au_plus = "0,005" if e3["niveau"] == 99 else "0,025"', 'au_plus = "0,005" if r["niveau"] == 99 else "0,025"',
     "phrase S : « au plus » au niveau de E3"),
    ("P06", 'confiance = fr(100 * (1 - 2.0 ** (1 - e3["k"])), 1)', 'confiance = fr(100 * (1 - 2.0 ** (-e3["k"])), 1)',
     "phrase N : confiance 1 − 2^(1−K)"),
    ("P07", "_au_plus_pour_cent(2.0 ** -e3['k'])", "_au_plus_pour_cent(2.0 ** (1 - e3['k']))", "phrase E : erreur 2^−K"),
    ("P08", '    if code == "N" and r.get("sans_bornes"):', "    if False:", "phrase N à motif, sans bornes"),
    ("C01", "        return a == b\n    if isinstance(a, list)", "        return abs(a - b) < 1e-3\n    if isinstance(a, list)",
     "comparateur : accord exact, sans tolérance"),
    ("C02", "verdict = ACCORD_EXACT if not manquants and not desaccords else DESACCORDS",
     "verdict = ACCORD_EXACT if not desaccords else DESACCORDS", "comparateur : un champ manquant interdit l'accord"),
    ("C03", '"seuil": mien["seuil"],', '"seuil": _lire(resultat, "seuil", e),', "comparateur : le seuil est comparé"),
    ("C04", "if isinstance(d, dict) and isinstance(f, list) and sorted(d) != sorted(f):", "if False:",
     "comparateur : familles des différences et familles présentes"),
    ("C05", "        elif not _egal(premier, mien):", "        elif False:", "comparateur : désaccord rendu"),
    ("C06", "            manquants.append(_chemin(cle, e))\n            return None", "            return None",
     "comparateur : entrée manquante dite"),
    ("C07", "        return rendre(garde=True)", "        return rendre(garde=False)", "comparateur : arrêt par une garde"),
    ("C08", "        if resultat is not None:\n            desaccords.append({\"champ\": \"code de sortie\", \"motif\": \"code 2",
     "        if False:\n            desaccords.append({\"champ\": \"code de sortie\", \"motif\": \"code 2",
     "comparateur : code 2 avec un résultat écrit"),
    ("C09", "    if code_sortie != 0:", "    if code_sortie not in (0, 1):", "comparateur : code de sortie inattendu"),
    ("C10", 'rien_des_sondes = not second["manipulation_etablie"] or "decisive" in en_echec',
     'rien_des_sondes = not second["manipulation_etablie"]', "comparateur : rien n'est lu si la sonde est en échec"),
    ("C11", "        if (bloc is None) != rien_des_sondes:", "        if False:",
     "comparateur : rien n'est lu des sondes, si et seulement si"),
    ("C12", 'if isinstance(m, dict) and "jumeau" in m and "sur_saboteur" in m)', 'if isinstance(m, dict) and "jumeau" in m)',
     "comparateur : familles de E3 comptées dans la table"),
    ("C13", 'sonde_decisive_echec=en_echec["decisive"] if "decisive" in en_echec else False,',
     'sonde_decisive_echec="decisive" in en_echec,', "comparateur : le motif de l'instance est passé (couple S5)"),
    ("C13b", 'sonde_decisive_echec=en_echec["decisive"] if "decisive" in en_echec else False,',
     'sonde_decisive_echec=en_echec.get("decisive", True) if en_echec else False,',
     "comparateur : la sonde décisive, et elle seule"),
    ("C14", 'attendue = "au niveau de 95 %" if second["niveau"] == 95 else _MANQUE',
     'attendue = "au niveau de 95 %" if second["niveau"] == 99 else _MANQUE', "comparateur : phrase du niveau"),
    ("C15", 'confronter(_chemin("issue_motifs"), _lire(resultat, "issue_motifs"), second["motifs"])',
     'confronter(_chemin("issue_motifs"), _lire(resultat, "issue_motifs"), _lire(resultat, "issue_motifs"))',
     "comparateur : les motifs sont comparés"),
    ("C16", "return len(a) == len(b) and all(_egal(x, y) for x, y in zip(a, b))",
     "return all(_egal(x, y) for x, y in zip(a, b))", "comparateur : listes de même longueur"),
    ("C17", 'ECART_DE_LA_PHRASE_N = "2.0"', 'ECART_DE_LA_PHRASE_N = "1.0"', "comparateur : écart 2 de la table de puissance"),
    ("C18", '"separe": mien["verdict"] == SEPARE,', '"separe": _lire(resultat, "separe", e),',
     "comparateur : « séparé » comparé"),
    ("C19", '"contraire": mien["verdict"] == CONTRAIRE,', '"contraire": False,', "comparateur : « contraire » comparé"),
    ("C20", '"non_atteignable": mien["niveau"] is None,', '"non_atteignable": False,',
     "comparateur : niveau non atteignable comparé"),
    ("C21", '"niveau": _niveau_ecrit(mien["niveau"]),', '"niveau": mien["niveau"],',
     "comparateur : niveau écrit « 99 » ou « 95 »"),
    ("C22", 'confronter(_chemin("issue_niveau"), _lire(resultat, "issue_niveau"), _niveau_ecrit(second["niveau"]))',
     'confronter(_chemin("issue_niveau"), _lire(resultat, "issue_niveau"), _lire(resultat, "issue_niveau"))',
     "comparateur : niveau de l'issue comparé"),
    ("C23", 'confronter(_chemin("issue_code"), _lire(resultat, "issue_code"), second["code"])',
     'confronter(_chemin("issue_code"), _lire(resultat, "issue_code"), _lire(resultat, "issue_code"))',
     "comparateur : code de l'issue comparé"),
    ("C24", "        if not refus_attendu:\n            desaccords.append", "        if False:\n            desaccords.append",
     "comparateur : code 2 hors d'un refus planté (couple S7)"),
    ("C25", "    if refus_attendu:\n        desaccords.append", "    if False:\n        desaccords.append",
     "comparateur : code 0 dans un monde à refus planté (couple S8)"),
    ("C26", "        return comparer(code_sortie, None, refus_attendu=refus_attendu)", "        return comparer(code_sortie, None)",
     "comparer_fichier : drapeau transmis sans fichier (couple S9)"),
    ("C27", "        return comparer(code_sortie, json.load(f), refus_attendu=refus_attendu)",
     "        return comparer(code_sortie, json.load(f))", "comparer_fichier : drapeau transmis avec fichier (couple S9)"),
    ("C28", '    refus_attendu = "--refus-attendu" in argv', "    refus_attendu = False",
     "ligne de commande : drapeau lu (couple S10)"),
    ("C29", "rendu = comparer_fichier(code, argv[2] if len(argv) == 3 else None, refus_attendu=refus_attendu)",
     "rendu = comparer_fichier(code, argv[2] if len(argv) == 3 else None)", "ligne de commande : drapeau transmis (couple S11)"),
    ("X1", "        if familles_e3 is not None and familles_e3 != k_e3:", "        if False:",
     "contre-lecture : contrôle du compte de familles de E3"),
    ("X2", '"positifs": mien["positives"],', '"positifs": _lire(resultat, "positifs", e),',
     "contre-lecture : `positifs` comparé à lui-même"),
    ("X3", '"w_plus": mien["w_plus"],', '"w_plus": _lire(resultat, "w_plus", e),',
     "contre-lecture : `W_plus` comparé à lui-même"),
]


def jouer(environnement: dict) -> int:
    commande = [sys.executable, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAIS]
    return subprocess.run(commande, cwd=RACINE, env=environnement, capture_output=True, text=True).returncode


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print(__doc__)
        return 2
    journal = argv[0]
    if os.path.exists(journal):
        print(f"refus : {journal} existe déjà (on n'écrase jamais)")
        return 2
    with open(MODULE, encoding="utf-8") as f:
        source = f.read()
    with open(ESSAIS, "rb") as f:
        empreinte_essais = hashlib.sha256(f.read()).hexdigest()
    environnement = dict(os.environ)
    environnement.pop("B5F_SECONDE_MODULE", None)
    lignes = []
    os.makedirs(DOSSIER, exist_ok=False)
    try:
        # Cas sain : le module non muté, copié au même endroit, passe les essais.
        with open(MUTANT, "w", encoding="utf-8") as f:
            f.write(source)
        environnement["B5F_SECONDE_MODULE"] = MUTANT
        sain = jouer(environnement)
        for nom, origine, mute, regle in MUTATIONS:
            occurrences = source.count(origine)
            if occurrences != 1 or origine == mute:
                lignes.append({"nom": nom, "regle": regle, "etat": f"inapplicable ({occurrences} occurrences)"})
                continue
            with open(MUTANT, "w", encoding="utf-8") as f:
                f.write(source.replace(origine, mute))
            code = jouer(environnement)
            lignes.append({"nom": nom, "regle": regle, "etat": "attrapée" if code == 1 else f"non attrapée (code {code})"})
    finally:
        if os.path.exists("/dev/shm/b5f-seconde-programmation-mutations-v3/mutant.py"):
            os.remove("/dev/shm/b5f-seconde-programmation-mutations-v3/mutant.py")
        os.rmdir("/dev/shm/b5f-seconde-programmation-mutations-v3")
    attrapees = sum(1 for x in lignes if x["etat"] == "attrapée")
    rendu = {
        "module_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "essais_sha256": empreinte_essais,
        "cas_sain_code_de_sortie": sain,
        "mutations": len(lignes),
        "attrapees": attrapees,
        "lignes": lignes,
    }
    with open(journal, "w", encoding="utf-8") as f:
        json.dump(rendu, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"cas sain : code {sain} ; mutations : {len(lignes)} ; attrapées : {attrapees}")
    for x in lignes:
        if x["etat"] != "attrapée":
            print(f"  {x['nom']} : {x['etat']} — {x['regle']}")
    return 0 if sain == 0 and attrapees == len(lignes) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
