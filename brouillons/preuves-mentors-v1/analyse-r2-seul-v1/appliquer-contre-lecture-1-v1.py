"""Brouillon 2 du préenregistrement « R2 seul » = brouillon 1 + exactement les 35 couples RL-01 à RL-35 de la contre-lecture
1 (voie B, sans contre-lecture 2), lus dans le rapport scellé, appliqués dans l'ordre ; puis les seules mises à jour
mécaniques qu'imposent les corrections de code C-1 à C-4 (empreintes de la liste fermée, empreinte des constantes, nombre
d'essais), listées une à une ; puis les ajouts déclarés à la section « Écart à la voie B » (titre, date, encadré de tête
demandé par la session, la section elle-même).

Gardes : empreintes du brouillon 1 et du rapport ; 35 couples, identifiants RL-01 à RL-35 dans l'ordre ; chaque ancien texte
présent exactement une fois au moment de son remplacement ; brouillon 2 absent avant l'écriture (règle R12).
Usage, depuis la racine du dépôt : PYTHONPATH=src python <ce fichier>
"""
import hashlib
import re
import sys
from pathlib import Path

D = Path("brouillons/preuves-mentors-v1/analyse-r2-seul-v1")
B1 = D / "preenregistrement-analyse-r2-seul-v1-brouillon1.md"
B2 = D / "preenregistrement-analyse-r2-seul-v1-brouillon2.md"
RAPPORT = D / "contre-lecture-preenregistrement-analyse-r2-seul-v1.md"
SHA_B1 = "99929166c194d10949caf9d3716cb668cf38c29cf421fc2b918f8994eb8b3b8b"
SHA_RAPPORT = "cb4e9fa26c765e2639fa0c7eb176b3b6191d98b5618e4374dec035879f1a3853"
CODE_CHANGE = ("src/controle_ia/analyse_principale_r1_r2/constantes_v3.py",
               "src/controle_ia/analyse_principale_r1_r2/entrees_v3.py",
               "src/controle_ia/analyse_principale_r1_r2/lecture_v3.py", "tests/test_analyse_r2_seul_v1.py")
ANCIENNES = {"src/controle_ia/analyse_principale_r1_r2/constantes_v3.py":
             "791341180cded09d6c24edf029013d2c4ee3476499df62374cc874a9c4159210",
             "src/controle_ia/analyse_principale_r1_r2/entrees_v3.py":
             "f9dd931b3032e7cd0c19d311c1eab115b1176d9c459c2ec2cec28d71bbd65534",
             "src/controle_ia/analyse_principale_r1_r2/lecture_v3.py":
             "8d7c34619dd5b82aa5567f37f77d7b26ee141591c1292d0e7a436d3a6f66a40f",
             "tests/test_analyse_r2_seul_v1.py": "267e05ce94880b53f857844008a90fabc2c4399d962ef5c3ba54ed7e87248c3d"}
CONSTANTES_AVANT = "035833098198fade6f1220a875cb0f61c35f7c37bb3e60954f9e40ac76f4e1fa"
ESSAIS_APRES = 13

ENCADRE = (
    "\n> **À lire d'abord — ce que coûte cette lecture (RL-01), et sa parade.** Lire R2 maintenant ôte l'aveugle du côté "
    "des juges (J3s, J3g, J8s) et du prédicteur T à toute analyse future d'un R1 relancé : une analyse de W contre ces bras, "
    "sur ces 2 400 actions, serait écrite en connaissant leurs rappels et leurs aires ; seule W resterait aveugle (règle R1). "
    "**Parade** : l'analyse d'un R1 relancé reprend tel quel le détail du calcul scellé de l'analyse principale "
    "(`8e2679526b2777a9fe8564dd5f5fdaf98b70affd759cf47857abc8b168d92537` : niveau de l'action, quantile, plis, intervalles, "
    "bras, traits de T), seuls changeant le texte du fournisseur et les empreintes de ses sorties ; tout autre choix est un "
    "nœud de Lazar.\n")
SECTION_ECART = """## Écart à la voie B

Brouillon 2 = brouillon 1 + exactement les 35 couples RL-01 à RL-35 de la contre-lecture 1 (rapport `cb4e9fa2…`), appliqués par `appliquer-contre-lecture-1-v1.py`. Touché en plus, et pourquoi :
- le titre (« brouillon 1 » → « brouillon 2 ») et la ligne « Date » (heures du brouillon 2) : identification du brouillon ;
- l'encadré « À lire d'abord » sous le titre : demandé par la session (coût de RL-01 et sa parade, en tête et en clair) ; il répète RL-01 sans rien y changer ;
- les mises à jour mécaniques des corrections de code C-1 à C-4 : empreintes de `constantes_v3.py`, `entrees_v3.py`, `lecture_v3.py` et `tests/test_analyse_r2_seul_v1.py` dans la liste fermée, empreinte des constantes, nombre d'essais (listées une à une dans la sortie du script) ;
- cette section.
Rien d'autre. Les suggestions sans correction exigée du rapport (nom de la branche « réserve de spécificité » quand `part_mention` vaut `None`, conditionner « J3s − T supérieure » à la mention) ne sont pas appliquées.

"""


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def couples(rapport: str) -> list:
    blocs = re.split(r"^### (RL-\d\d)\b.*$", rapport, flags=re.M)
    sortie = []
    for ident, corps in zip(blocs[1::2], blocs[2::2]):
        a = re.search(r"^````ancien\n(.*?)\n````$", corps, flags=re.M | re.S)
        n = re.search(r"^````nouveau\n(.*?)\n````$", corps, flags=re.M | re.S)
        if a is None or n is None:
            raise SystemExit(f"{ident} : blocs ancien / nouveau introuvables")
        sortie.append((ident, a.group(1), n.group(1)))
    return sortie


def main() -> int:
    for p, attendu in ((B1, SHA_B1), (RAPPORT, SHA_RAPPORT)):
        obtenu = sha(p)
        print(f"empreinte {p.name} : {obtenu} {'OK' if obtenu == attendu else 'DIFFÉRENTE'}")
        if obtenu != attendu:
            return 1
    if B2.exists():
        print(f"{B2} existe déjà (règle R12) : arrêt")
        return 1
    s = B1.read_text(encoding="utf-8")
    cs = couples(RAPPORT.read_text(encoding="utf-8"))
    ids = [c[0] for c in cs]
    if ids != [f"RL-{k:02d}" for k in range(1, 36)]:
        print(f"couples lus : {ids} ≠ RL-01 à RL-35")
        return 1
    for ident, ancien, nouveau in cs:
        k = s.count(ancien)
        print(f"{ident} : {k} occurrence(s) de l'ancien texte (1 attendue) — {'OK' if k == 1 else 'ÉCHEC'}")
        if k != 1:
            return 1
        s = s.replace(ancien, nouveau)
    print("— mises à jour mécaniques (corrections de code C-1 à C-4) —")
    for f in CODE_CHANGE:
        a, n = ANCIENNES[f], sha(f)
        ligne_a, ligne_n = f"`{f}` : `{a}`", f"`{f}` : `{n}`"
        k = s.count(ligne_a)
        print(f"empreinte de {f} : {a[:12]}… → {n[:12]}… ({k} occurrence) — {'OK' if k == 1 and a != n else 'ÉCHEC'}")
        if k != 1 or a == n:
            return 1
        s = s.replace(ligne_a, ligne_n)
    sys.path.insert(0, "src")
    from controle_ia.analyse_principale_r1_r2 import constantes_v3 as K3
    c_n = K3.empreinte_constantes()
    a = f"Empreinte des constantes (analyse R2 seul) : `{CONSTANTES_AVANT}`"
    k = s.count(a)
    print(f"empreinte des constantes : {CONSTANTES_AVANT[:12]}… → {c_n[:12]}… ({k} occurrence) — "
          f"{'OK' if k == 1 and c_n != CONSTANTES_AVANT else 'ÉCHEC'}")
    if k != 1 or c_n == CONSTANTES_AVANT:
        return 1
    s = s.replace(a, f"Empreinte des constantes (analyse R2 seul) : `{c_n}`")
    a = "- **Tests attendus** : `30` (`PYTHONPATH=src:tests python -m pytest -q tests/test_analyse_principale_r1_r2_v1.py tests/test_analyse_r2_seul_v1.py`, données synthétiques seulement ; 20 + 10)."
    n = a.replace("`30`", f"`{20 + ESSAIS_APRES}`").replace("20 + 10", f"20 + {ESSAIS_APRES}")
    k = s.count(a)
    print(f"tests attendus : 30 (20 + 10) → {20 + ESSAIS_APRES} (20 + {ESSAIS_APRES}) ({k} occurrence) — {'OK' if k == 1 else 'ÉCHEC'}")
    if k != 1:
        return 1
    s = s.replace(a, n)
    print("— ajouts déclarés (section « Écart à la voie B ») —")
    for ident, ancien, nouveau in (
            ("titre", "— v1 — brouillon 1\n", "— v1 — brouillon 2\n" + ENCADRE),
            ("date", "- **Date (UTC)** : 2026-11-02, entre 01:41 et ≈ 02:20 ;",
             "- **Date (UTC)** : 2026-11-02 ; brouillon 1 entre 01:41 et ≈ 02:00 ; brouillon 2 (contre-lecture 1, voie B) entre "
             "02:12 et ≈ 02:40, par le script `appliquer-contre-lecture-1-v1.py` ;"),
            ("section", "## Contre-lecture\n", SECTION_ECART + "## Contre-lecture\n")):
        k = s.count(ancien)
        print(f"{ident} : {k} occurrence (1 attendue) — {'OK' if k == 1 else 'ÉCHEC'}")
        if k != 1:
            return 1
        s = s.replace(ancien, nouveau)
    B2.write_text(s, encoding="utf-8")
    print(f"écrit : {B2} ; sha256 {sha(B2)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
