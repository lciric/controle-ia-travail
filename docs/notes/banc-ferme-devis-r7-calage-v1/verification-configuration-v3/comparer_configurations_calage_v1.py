#!/usr/bin/env python3
"""Contrôle de la configuration du calage v3 contre la v2 et contre la relecture de Fable (classe B, programme de contrôle).

Ce qu'il fait, et rien d'autre :
1. il calcule l'empreinte de chaque fichier lu ;
2. il compare la configuration v2 et la configuration v3, clé par clé, et liste chaque différence ;
3. il compare les deux fichiers ligne à ligne (texte brut), pour ne pas dépendre de la lecture JSON ;
4. il vérifie qu'aucune clé n'est écrite deux fois dans la v3 ;
5. il vérifie, à l'égalité stricte des chaînes, que la cinquième règle de lecture de la v3 est le texte de
   remplacement de la relecture (sa ligne 32), auquel s'ajoute, après la phrase des dispenses, la phrase du
   quantile (sa ligne 36) ;
6. il vérifie que les deux remplacements demandés pour la note (verdict, titre du § 9) sont dans la note v3 et
   que les formes remplacées n'y sont plus, puis il compte les lignes qui diffèrent entre la note v2 et la note v3.

Il ne lit aucun autre fichier, n'écrit rien et ne tire aucun nombre au hasard (aucune graine : R9 sans objet).

Usage :
    python3 -I comparer_configurations_calage_v1.py CONFIG_V2 CONFIG_V3 RELECTURE NOTE_V2 NOTE_V3
Code de sortie : 0 si tous les contrôles tiennent, 1 sinon.
"""
from __future__ import annotations

import difflib
import hashlib
import json
import sys
from pathlib import Path

# Champs de tenue de version : les seuls, avec la cinquième règle, que la v3 a le droit de changer.
TENUE_DE_VERSION = ("/auteur", "/corrections/", "/date_utc", "/remplace/", "/statut", "/version")
REGLE_CORRIGEE = "/regles_de_lecture[4]"
ANCRE_DES_DISPENSES = "une garde du programme de validation fixe chacune. "
VERDICT_DEMANDE = "Un nœud ouvert s'y ajoute, sur les fichiers des fonctions de montage (§ 9)."
VERDICT_REMPLACE = "Un nœud ouvert s'y ajoute, de classe B, sur les fichiers des fonctions de montage (§ 9)."
DEBUT_DU_PARAGRAPHE_DU_VERDICT = "Quatre points demandent un accord avec le texte du banc fermé avant son scellement"
TITRE_DEMANDE = "## 9. Nœud ouvert de la v2 (m4)"
TITRE_REMPLACE = "## 9. Nœud ouvert de la v2 (m4, classe B)"


def empreinte(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def differences(x, y, chemin: str, sortie: list) -> None:
    if type(x) is not type(y):
        sortie.append((chemin, "type", x, y))
    elif isinstance(x, dict):
        for cle in sorted(set(x) | set(y)):
            if cle not in x:
                sortie.append((f"{chemin}/{cle}", "ajout", None, y[cle]))
            elif cle not in y:
                sortie.append((f"{chemin}/{cle}", "retrait", x[cle], None))
            else:
                differences(x[cle], y[cle], f"{chemin}/{cle}", sortie)
    elif isinstance(x, list):
        if len(x) != len(y):
            sortie.append((chemin, f"longueur {len(x)} -> {len(y)}", x, y))
        else:
            for i, (u, v) in enumerate(zip(x, y)):
                differences(u, v, f"{chemin}[{i}]", sortie)
    elif x != y:
        sortie.append((chemin, "valeur", x, y))


def cles_en_double(chemin: Path) -> list[str]:
    doubles: list[str] = []

    def paires(p):
        cles = [k for k, _ in p]
        doubles.extend(sorted({k for k in cles if cles.count(k) > 1}))
        return dict(p)

    json.loads(chemin.read_text(encoding="utf-8"), object_pairs_hook=paires)
    return doubles


def corps_de_citation(ligne: str) -> str:
    """Le texte d'une ligne de citation de la relecture : « > « … » »."""
    if not (ligne.startswith("> « ") and ligne.endswith(" »")):
        raise SystemExit(f"REFUS : ligne de citation de forme inattendue : {ligne[:40]!r}")
    return ligne[len("> « "):-len(" »")]


def court(x, n: int = 160) -> str:
    s = x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + " […]"


def main(argv: list[str]) -> int:
    if len(argv) != 6:
        print(__doc__)
        return 1
    c2, c3, rel, n2, n3 = (Path(a) for a in argv[1:])
    echecs = 0

    def juger(nom: str, vrai: bool, detail: str = "") -> None:
        nonlocal echecs
        echecs += 0 if vrai else 1
        print(f"{'tenu  ' if vrai else 'ÉCHEC '} | {nom}" + (f" | {detail}" if detail else ""))

    print("# Empreintes des fichiers lus (sha256)")
    for nom, f in (("configuration v2", c2), ("configuration v3", c3), ("relecture de Fable", rel),
                   ("note v2", n2), ("note v3", n3)):
        print(f"{nom} : {empreinte(f)}  {f.name}")

    a = json.loads(c2.read_text(encoding="utf-8"))
    b = json.loads(c3.read_text(encoding="utf-8"))
    print("\n# 1. Configuration : différences clé par clé, de la v2 à la v3")
    juger("mêmes clés de premier niveau, dans le même ordre", list(a) == list(b), ", ".join(b))
    d: list = []
    differences(a, b, "", d)
    print(f"nombre de différences : {len(d)}")
    hors = []
    for chemin, genre, x, y in d:
        permis = chemin == REGLE_CORRIGEE or any(chemin == t or chemin.startswith(t) for t in TENUE_DE_VERSION)
        if not permis:
            hors.append(chemin)
        print(f"- {chemin} ({genre}){'' if permis else '  <-- HORS DES CHAMPS PERMIS'}")
        print(f"    v2 : {court(x)}")
        print(f"    v3 : {court(y)}")
    juger("aucune différence hors de la tenue de version et de la cinquième règle", not hors, ", ".join(hors))
    for bloc in ("parametres", "coherence_avec_le_banc_ferme", "ce_qui_reste_ouvert", "pieces_citees",
                 "pieces_lues_sans_etre_sources", "portee", "ce_que_cette_configuration_ne_fixe_pas",
                 "lecture_des_sources", "mot_de_lazar", "objet"):
        juger(f"bloc « {bloc} » identique", a.get(bloc) == b.get(bloc))
    juger("les six autres règles de lecture identiques",
          [r for i, r in enumerate(a["regles_de_lecture"]) if i != 4] == [r for i, r in enumerate(b["regles_de_lecture"]) if i != 4]
          and len(a["regles_de_lecture"]) == len(b["regles_de_lecture"]) == 7)

    print("\n# 2. Configuration : comparaison du texte brut, ligne à ligne")
    l2 = c2.read_text(encoding="utf-8").split("\n")
    l3 = c3.read_text(encoding="utf-8").split("\n")
    retirees = ajoutees = 0
    for ligne in difflib.unified_diff(l2, l3, lineterm="", n=0):
        if ligne.startswith(("---", "+++", "@@")):
            continue
        retirees += ligne.startswith("-")
        ajoutees += ligne.startswith("+")
    print(f"lignes de la v2 : {len(l2)} ; lignes de la v3 : {len(l3)} ; retirées : {retirees} ; ajoutées : {ajoutees}")
    juger("aucune clé écrite deux fois dans la v3", not cles_en_double(c3), ", ".join(cles_en_double(c3)))

    print("\n# 3. Correction 1 : la cinquième règle, mot pour mot")
    lignes_rel = rel.read_text(encoding="utf-8").split("\n")
    remplacement = corps_de_citation(lignes_rel[31])      # ligne 32 de la relecture
    phrase_quantile = corps_de_citation(lignes_rel[35])   # ligne 36 de la relecture
    juger("la phrase des dispenses figure une fois dans le texte de remplacement", remplacement.count(ANCRE_DES_DISPENSES) == 1)
    attendu = remplacement.replace(ANCRE_DES_DISPENSES, ANCRE_DES_DISPENSES + phrase_quantile + " ")
    regle = b["regles_de_lecture"][4]
    juger("règle v3 = texte de remplacement + phrase du quantile après la phrase des dispenses (égalité stricte)",
          regle == attendu, f"{len(regle)} caractères contre {len(attendu)}")
    juger("règle v2 = texte de remplacement privé de la phrase des dispenses (la v2 était bien la règle critiquée)",
          a["regles_de_lecture"][4] != regle and a["regles_de_lecture"][4] in remplacement.replace(
              remplacement[remplacement.index("Deux entrées"):remplacement.index("La révision")], ""))

    print("\n# 4. Correction 2 : la note")
    t2 = n2.read_text(encoding="utf-8")
    t3 = n3.read_text(encoding="utf-8")
    # La phrase demandée doit clore le paragraphe du verdict ; la table des corrections de la note la cite aussi.
    lignes_du_verdict = [l for l in t3.split("\n") if l.startswith(DEBUT_DU_PARAGRAPHE_DU_VERDICT)]
    juger("verdict demandé : il clôt le paragraphe du verdict de la note v3 (une seule ligne de ce début)",
          len(lignes_du_verdict) == 1 and lignes_du_verdict[0].endswith(VERDICT_DEMANDE),
          f"occurrences de la phrase dans la note : {t3.count(VERDICT_DEMANDE)}")
    juger("ancienne phrase du verdict absente de la note v3, présente dans la v2",
          VERDICT_REMPLACE not in t3 and t2.count(VERDICT_REMPLACE) == 1)
    juger("titre demandé présent une fois, en début de ligne, dans la note v3", t3.split("\n").count(TITRE_DEMANDE) == 1)
    juger("ancien titre absent de la note v3, présent dans la v2",
          TITRE_REMPLACE not in t3 and t2.split("\n").count(TITRE_REMPLACE) == 1)
    r = j = 0
    for ligne in difflib.unified_diff(t2.split("\n"), t3.split("\n"), lineterm="", n=0):
        if ligne.startswith(("---", "+++", "@@")):
            continue
        r += ligne.startswith("-")
        j += ligne.startswith("+")
    print(f"note : lignes retirées {r}, lignes ajoutées {j} (le détail est dans la pièce de vérification)")

    print(f"\nbilan : {'tous les contrôles tiennent' if echecs == 0 else str(echecs) + ' contrôle(s) en échec'}")
    return 0 if echecs == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
