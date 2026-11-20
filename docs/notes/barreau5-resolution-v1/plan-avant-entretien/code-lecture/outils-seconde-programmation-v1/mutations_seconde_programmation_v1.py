"""Passage de mutations sur la seconde programmation du dénombrement exact et de la table des issues (barreau 5).

Pour chaque mutation : une copie du module, changée en un seul endroit, est écrite dans `/dev/shm`, et les essais neufs
de la seconde programmation sont joués sur elle (variable d'environnement `B5F_SECONDE_MODULE`). Une mutation est
« attrapée » si les essais échouent. Le module du dépôt n'est jamais modifié ; le programme de lecture n'est jamais
joué. Aucun aléa. Les fichiers temporaires sont effacés à la fin par leur chemin.

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
MODULE = RACINE + "/src/controle_ia/barreau5_familles/seconde_programmation_v1.py"
ESSAIS = RACINE + "/tests/test_barreau5_familles_seconde_programmation_v1.py"
DOSSIER = "/dev/shm/b5f-seconde-programmation-mutations-v1"
MUTANT = "/dev/shm/b5f-seconde-programmation-mutations-v1/mutant.py"

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
    ("O05", "    if sonde_decisive_echec:", "    if False:", "sonde en échec : N, « non calculables »"),
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
    ("M01", 'motifs.append(f"force non écartée ({\', \'.join(force)})")', 'motifs.append("force non écartée")',
     "D : le motif dit laquelle"),
    ("M02", 'motifs.append("saboteur non établi")', 'motifs.append("saboteur non etabli")', "D : motif du saboteur"),
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
    ("C01", "        return a == b\n    return type(a)", "        return abs(a - b) < 1e-3\n    return type(a)",
     "comparateur : accord exact, sans tolérance"),
    ("C02", 'verdict = ACCORD_EXACT if not manquants and not desaccords else "désaccords"',
     'verdict = ACCORD_EXACT if not desaccords else "désaccords"', "comparateur : un champ manquant interdit l'accord"),
    ("C03", '_CHAMPS_EPREUVE = ("niveau", "seuil", "w_moins",', '_CHAMPS_EPREUVE = ("niveau", "w_moins",',
     "comparateur : le seuil est comparé"),
    ("C04", "if d is not None and f is not None and sorted(d) != sorted(f):", "if False:",
     "comparateur : familles des différences et familles présentes"),
    ("C05", "        elif not _egal(premier, mien):", "        elif False:", "comparateur : désaccord rendu"),
    ("C06", "            if exige:\n                manquants.append(_chemin(cle, e))", "            if False:\n                manquants.append(_chemin(cle, e))",
     "comparateur : entrée manquante dite"),
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
        if os.path.exists("/dev/shm/b5f-seconde-programmation-mutations-v1/mutant.py"):
            os.remove("/dev/shm/b5f-seconde-programmation-mutations-v1/mutant.py")
        os.rmdir("/dev/shm/b5f-seconde-programmation-mutations-v1")
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
