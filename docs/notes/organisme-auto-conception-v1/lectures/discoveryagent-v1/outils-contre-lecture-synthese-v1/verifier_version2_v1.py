#!/usr/bin/env python3
"""Vérification courte de la version 2 de la synthèse DiscoveryAgent, par le contre-lecteur (v1).

Se lance avec `python3 -I`, hors des dépôts des auteurs :
    python3 -I verifier_version2_v1.py RACINE_DU_DEPOT

Lecture seule : aucune écriture, aucun réseau ; rien des dépôts des auteurs n'est
exécuté (le programme v2 du rédacteur, lancé en mode --table, ne les lit que par git).

  1. Les 54 couples de la contre-lecture appliqués à la note v1 redonnent-ils le
     texte d'empreinte edc43176… ? En quoi la v2 en diffère-t-elle (retouches à la
     main de l'en-tête et de l'annexe) ?
  2. Le registre v2 est-il le registre v1 plus, à l'identique, les 60 citations
     « a_verser » du contre-lecteur ?
  3. La table d'annexe de la v2 est-elle la sortie --table du programme v2, et
     combien de ses lignes ont des barres verticales de trop (lignes cassées) ?
  4. Où la v2 nomme-t-elle encore la note, le programme ou le registre v1 ?
  5. Si la vérification existe : ses couples de forme « > AVANT : » / « > APRÈS : »
     sont-ils uniques dans la v2, applicables dans l'ordre, et le texte obtenu
     a-t-il une table entière et sans renvoi aux pièces v1 de l'outillage ?
"""
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
DOSSIER = ICI.parent
OUTILS_R = DOSSIER / "outils-synthese-v1"
NOTE_V1 = DOSSIER / "synthese-discoveryagent-pour-l-organisme-v1.md"
NOTE_V2 = DOSSIER / "synthese-discoveryagent-pour-l-organisme-v2.md"
CONTRE_LECTURE = DOSSIER / "contre-lecture-synthese-discoveryagent-v1.md"
VERIFICATION = DOSSIER / "verification-synthese-discoveryagent-v2-v1.md"
REG_V1 = OUTILS_R / "citations-synthese-v1.json"
REG_V2 = OUTILS_R / "citations-synthese-v2.json"
PROG_V2 = OUTILS_R / "verifier_citations_synthese_v2.py"
REG_CONTRE = ICI / "citations-contre-lecture-v1.json"
TITRE_TABLE = "## Annexe — table des citations vérifiées"
EMPREINTE_CORRIGEE = "edc4317687654349763b77f5adf774229c156498d4df2ec8831b69c6d4ebb91b"
RENVOIS_V1 = ("verifier_citations_synthese_v1.py", "citations-synthese-v1.json", "synthèse v1")


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def couples(fichier, prefixe_titre="Correction"):
    res, avant, nom = [], None, None
    for l in fichier.read_text(encoding="utf-8").splitlines():
        m = re.match(rf"^#{{3,4}} ({prefixe_titre} [^ ]+)", l)
        if m:
            nom = m.group(1)
        if l.startswith("> AVANT : "):
            avant = l[len("> AVANT : "):]
        elif l.startswith("> APRÈS : "):
            if avant is None:
                raise ValueError(f"APRÈS sans AVANT près de {nom}")
            res.append((nom, avant, l[len("> APRÈS : "):]))
            avant = None
    if avant is not None:
        raise ValueError("AVANT sans APRÈS en fin de fichier")
    return res


def appliquer(texte, liste):
    echecs = []
    for nom, avant, apres in liste:
        n = texte.count(avant)
        if n != 1:
            echecs.append((nom, n))
            continue
        texte = texte.replace(avant, apres)
    return texte, echecs


def cellules_en_trop(ligne):
    """Barres verticales au-delà des 4 d'une ligne de table à trois colonnes."""
    return ligne.count("|") - 4


def main():
    racine = Path(sys.argv[1]).resolve()
    v1 = NOTE_V1.read_text(encoding="utf-8")
    v2 = NOTE_V2.read_text(encoding="utf-8")
    total = 0
    print(f"note v1 : sha256 {sha(v1.encode())}")
    print(f"note v2 : sha256 {sha(v2.encode())}")

    print("== 1. Texte corrigé par les 54 couples, contre la v2")
    corrige, echecs = appliquer(v1, couples(CONTRE_LECTURE))
    print(f"couples non appliqués : {echecs or 'aucun'} ; empreinte du texte corrigé {sha(corrige.encode())}"
          f" ({'égale' if sha(corrige.encode()) == EMPREINTE_CORRIGEE else 'DIFFÉRENTE de'} edc43176…)")
    total += len(echecs) + (sha(corrige.encode()) != EMPREINTE_CORRIGEE)
    tete_c, tete_v2 = corrige.split(TITRE_TABLE)[0], v2.split(TITRE_TABLE)[0]
    print(f"avant l'annexe : texte corrigé {sha(tete_c.encode())} ; v2 {sha(tete_v2.encode())} ; "
          f"{'identiques' if tete_c == tete_v2 else 'différents'}")
    diff = [l for l in difflib.unified_diff(corrige.splitlines(), v2.splitlines(), "corrigé", "v2", n=0, lineterm="")]
    hors_table = [l for l in diff if l[:1] in "+-" and not l.startswith(("+++", "---")) and not l[1:].startswith("| ")]
    print(f"lignes qui diffèrent entre le texte corrigé et la v2, hors lignes de table : {len(hors_table)}")
    for l in hors_table:
        print("   " + (l if len(l) < 400 else l[:400] + " […]"))
    lignes_table = [l for l in diff if l[:1] in "+-" and not l.startswith(("+++", "---")) and l[1:].startswith("| ")]
    print(f"lignes de table qui diffèrent : {sum(1 for l in lignes_table if l.startswith('-'))} retirées, "
          f"{sum(1 for l in lignes_table if l.startswith('+'))} ajoutées")

    print("== 2. Registre v2 contre registre v1 plus les citations « a_verser » du contre-lecteur")
    r1 = json.loads(REG_V1.read_text(encoding="utf-8"))
    r2 = json.loads(REG_V2.read_text(encoding="utf-8"))
    rc = json.loads(REG_CONTRE.read_text(encoding="utf-8"))
    attendu = {c["id"]: c for c in r1["citations"]}
    for c in rc["citations"]:
        if c.get("a_verser"):
            attendu[c["id"]] = {k: v for k, v in c.items() if k != "a_verser"}
    obtenu = {c["id"]: c for c in r2["citations"]}
    manquants = sorted(set(attendu) - set(obtenu))
    en_trop = sorted(set(obtenu) - set(attendu))
    differents = sorted(i for i in set(attendu) & set(obtenu) if attendu[i] != obtenu[i])
    print(f"registre v2 : {len(obtenu)} citations ; attendues {len(attendu)} ; manquantes {manquants or 'aucune'} ; "
          f"en trop {en_trop or 'aucune'} ; contenu différent {differents or 'aucun'} ; sources "
          f"{'identiques' if r2['sources'] == r1['sources'] else 'DIFFÉRENTES'}")
    total += len(manquants) + len(en_trop) + len(differents) + (r2["sources"] != r1["sources"])

    print("== 3. Table d'annexe de la v2 contre la sortie --table du programme v2")
    r = subprocess.run([sys.executable, "-I", str(PROG_V2), str(racine), "--table"], capture_output=True)
    produite = [l for l in r.stdout.decode("utf-8").splitlines() if l.startswith("|")]
    table_v2 = [l for l in v2.split(TITRE_TABLE, 1)[1].splitlines() if l.startswith("|")]
    print(f"lignes produites : {len(produite)} ; lignes de la v2 : {len(table_v2)} ; "
          f"{'identiques' if produite == table_v2 else 'différentes'}")
    cassees = [l.split("|")[1].strip() for l in table_v2 if cellules_en_trop(l) > 0]
    print(f"lignes de la table v2 à barres verticales en trop (cassées à l'affichage) : {cassees or 'aucune'}")

    print("== 4. Renvois aux pièces v1 dans la v2 (hors table)")
    for i, l in enumerate(v2.split(TITRE_TABLE)[0].splitlines() + [TITRE_TABLE] +
                          [x for x in v2.split(TITRE_TABLE, 1)[1].splitlines() if not x.startswith("|")], 1):
        for motif in RENVOIS_V1:
            if motif in l:
                print(f"   « {motif} » : {l[:300]}")

    if VERIFICATION.exists():
        print("== 5. Couples de forme de la vérification, appliqués à la v2")
        liste = couples(VERIFICATION, "Couple")
        print(f"couples lus : {len(liste)}")
        uniques = [(nom, v2.count(av)) for nom, av, _ in liste if v2.count(av) != 1]
        print(f"« avant » non uniques dans la v2 : {uniques or 'aucun'}")
        v3, echecs = appliquer(v2, liste)
        print(f"application dans l'ordre : {len(liste) - len(echecs)} sur {len(liste)} ; échecs {echecs or 'aucun'}")
        table_v3 = [l for l in v3.split(TITRE_TABLE, 1)[1].splitlines() if l.startswith("|")]
        cassees3 = [l.split("|")[1].strip() for l in table_v3 if cellules_en_trop(l) > 0]
        restes = [m for m in ("verifier_citations_synthese_v1.py", "citations-synthese-v1.json") if m in v3]
        print(f"après application : lignes de table cassées {cassees3 or 'aucune'} ; "
              f"lignes de table {len(table_v3)} ; renvois restants aux outils v1 {restes or 'aucun'}")
        hors_table3 = [(a, b) for a, b in zip(produite, table_v3) if a != b]
        barres = sum(1 for a, b in hors_table3
                     if re.sub(r"`[^`]*`", lambda m: m.group(0).replace("|", "/"), a) == b)
        print(f"table après application contre la sortie --table : {len(hors_table3)} ligne(s) différente(s), "
              f"dont {barres} par la seule barre verticale rendue en barre oblique dans un motif")
        ids_avant = set(re.findall(r"\b([PACXN]\d{2})\b", v2.split(TITRE_TABLE)[0]))
        ids_apres = set(re.findall(r"\b([PACXN]\d{2})\b", v3.split(TITRE_TABLE)[0]))
        print(f"identifiants cités avant la table : v2 {len(ids_avant)}, après application {len(ids_apres)} ; "
              f"{'mêmes' if ids_avant == ids_apres else 'DIFFÉRENTS'}")
        print(f"empreinte du texte obtenu : {sha(v3.encode())}")
        total += len(uniques) + len(echecs) + len(cassees3) + len(restes) + (len(hors_table3) != barres) \
            + (ids_avant != ids_apres)
    print(f"BILAN : {total} échec(s)")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
