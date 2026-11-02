"""Brouillon 4 = brouillon 3 + exactement les remplacements de la section 8 de la contre-lecture 3 (voie B) — v1.

Lit les remplacements **dans le rapport lui-même** (blocs « Ancien texte » / « Nouveau texte » de la section 8, entre
quatre accents graves), après avoir vérifié l'empreinte du rapport et celle du brouillon 3 ; applique chacun en exigeant
que l'ancien texte apparaisse exactement une fois. Puis remplit l'entrée de forme fixe de la contre-lecture 3 (consigne
de la session principale : un seul marqueur doit rester), ce qui impose deux conséquences, nommées E1 et E2 et
déclarées dans `rapport-redaction-v4.md` :
- E1 : l'étape 0.d ne remplace plus que le marqueur du commit cité (« deux marqueurs » deviendrait faux) ;
- E2 : le marqueur `<<CONTRE_LECTURE_3>>` et sa note « remplacé au scellement » sont remplacés par l'entrée.
Contrôles : un seul marqueur (`` `<<COMMIT_CITE>>` ``) ; table des énoncés et phrase de portée v3 recopiées ; validateur
ne signalant que ce marqueur, puis vide après remplacement simulé du commit sur une copie en mémoire ; garde du commit
cité ; lignes changées. N'écrase rien (R12).

    PYTHONPATH=src python brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1/appliquer-contre-lecture-3-v1.py
"""
import difflib
import hashlib
import re
import sys
import tempfile
from pathlib import Path

from controle_ia.prereg import problemes
from controle_ia.simulation_essaim import lecture_hors_echantillon_v3 as L3
from controle_ia.simulation_t03.run_t03 import COMMIT_CITE

ICI = Path(__file__).resolve().parent
REL = "brouillons/preuves-mentors-v1/essaim-hors-echantillon-v1"
B3 = ICI / "preenregistrement-essaim-hors-echantillon-v1-brouillon3.md"
B4 = ICI / "preenregistrement-essaim-hors-echantillon-v1-brouillon4.md"
CL3 = ICI / "contre-lecture-3-preenregistrement-essaim-hors-echantillon-v1.md"
TRAITEMENT = ICI / "rapport-redaction-v4.md"
SHA_B3 = "d1d5740e202dd972d017b236969acf499341b8187d6cbfcf63d571b36451e343"
SHA_CL3 = "b454118f7ed75aeb7887ec4e090a6845699414f8147efbd9755516cad3194cb4"
ATTENDUS = ["C3.1", "C3.2", "C3.3", "C3.4a", "C3.4b", "C3.5", "C3.6", "C3.7 (recommandée)", "C3.8 (recommandée)",
            "C3.9 (recommandée)", "F1 statut", "F2 auteur", "F3 parade, point 1"]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def remplacements_section8(rapport: str) -> list[tuple[str, str, str]]:
    corps = rapport.split("## 8. Textes de remplacement", 1)[1].split("\n## 9.", 1)[0]
    blocs = re.split(r"^#### ", corps, flags=re.M)[1:]
    sortie = []
    for b in blocs:
        titre = b.split("\n", 1)[0].strip()
        textes = re.findall(r"^````\n(.*?)\n````$", b, flags=re.M | re.S)
        assert len(textes) == 2, (titre, len(textes))
        sortie.append((titre, textes[0], textes[1]))
    return sortie


def appliquer(texte: str, nom: str, ancien: str, nouveau: str) -> str:
    n = texte.count(ancien)
    if n != 1:
        sys.exit(f"ARRÊT : {nom} : ancien texte trouvé {n} fois (une exactement attendue)")
    print(f"- {nom} : 1 occurrence, remplacée")
    return texte.replace(ancien, nouveau)


def main() -> int:
    for p, attendu in ((B3, SHA_B3), (CL3, SHA_CL3)):
        if sha(p) != attendu:
            sys.exit(f"ARRÊT : empreinte de {p.name} ≠ {attendu}")
    if not TRAITEMENT.is_file():
        sys.exit("ARRÊT : rapport-redaction-v4.md absent (l'entrée cite son empreinte)")
    sha_tr = sha(TRAITEMENT)
    print(f"brouillon 3 : {SHA_B3} ; rapport de la contre-lecture 3 : {SHA_CL3} ; traitement : {sha_tr}")
    t3 = B3.read_text(encoding="utf-8")
    rempl = remplacements_section8(CL3.read_text(encoding="utf-8"))
    if [r[0] for r in rempl] != ATTENDUS:
        sys.exit(f"ARRÊT : remplacements lus {[r[0] for r in rempl]} ≠ {ATTENDUS}")
    print(f"Section 8 du rapport : {len(rempl)} remplacements")
    t = t3
    for nom, ancien, nouveau in rempl:
        t = appliquer(t, nom, ancien, nouveau)
    print("Conséquences du remplissage de l'entrée de la contre-lecture 3 (déclarées) :")
    t = appliquer(t, "E1 étape 0.d",
                  "     - le marqueur de la section « Contre-lecture » par l'entrée de forme fixe (C5.2).\n"
                  "     Avant remplacement, le texte contient exactement deux marqueurs de gabarit, une fois chacun ; "
                  "après, aucun.",
                  "     Les entrées des contre-lectures 1 à 3 sont déjà écrites en forme fixe (C5.2) dans la section "
                  "« Contre-lecture ». Avant remplacement, le texte contient exactement un marqueur de gabarit, une "
                  "fois ; après, aucun.")
    entree = (f"- **Contre-lecture 3** (R2) — brouillon relu : `{REL}/{B3.name}`, sha256 `{SHA_B3}` ; rapport : "
              f"`{REL}/{CL3.name}`, sha256 `{SHA_CL3}` ; traitement : `{REL}/{TRAITEMENT.name}`, sha256 `{sha_tr}`.")
    t = appliquer(t, "E2 entrée de la contre-lecture 3",
                  "<<CONTRE_LECTURE_3>>\n\n(Marqueur remplacé au scellement par l'entrée de forme fixe « - "
                  "**Contre-lecture 3** (R2) — brouillon relu : chemin, sha256 ; rapport : chemin, sha256 ; traitement : "
                  "chemin, sha256. », sans autre phrase.)\n", entree + "\n")
    # contrôles
    marqueurs = re.findall(r"<<[A-Z0-9_]+>>", t)
    assert marqueurs == ["<<COMMIT_CITE>>"] and t.count("`<<COMMIT_CITE>>`") == 1, marqueurs
    assert L3.table_E_md() in t and L3.PHRASE_PORTEE in t
    assert "-m controle_ia.simulation_essaim.run_essaim_hors_echantillon_v3 " in t
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "b4.md"
        p.write_text(t, encoding="utf-8")
        pb = problemes(p)
        assert pb == ["marqueurs de gabarit restants : <<COMMIT_CITE>>"], pb
        simule = t.replace("<<COMMIT_CITE>>", "0123456789abcdef0123456789abcdef01234567")
        p.write_text(simule, encoding="utf-8")
        assert problemes(p) == [] and COMMIT_CITE.search(simule).group(1) == "0123456789abcdef0123456789abcdef01234567"
    print(f"Marqueurs restants : {marqueurs} ; validateur : {pb} ; après remplacement simulé : [] ; garde du commit cité : "
          "retrouvé")
    diff = [l for l in difflib.unified_diff(t3.splitlines(), t.splitlines(), lineterm="", n=0)
            if l[:1] in "+-" and not l.startswith(("+++", "---"))]
    print(f"Lignes changées (diff -U0) : {sum(l.startswith('-') for l in diff)} retirées, "
          f"{sum(l.startswith('+') for l in diff)} ajoutées")
    if B4.exists():
        if B4.read_text(encoding="utf-8") != t:
            sys.exit(f"ARRÊT : {B4.name} existe et diffère (R12 : on n'écrase pas)")
        print(f"{B4.name} existe déjà, identique")
    else:
        B4.write_text(t, encoding="utf-8")
    print(f"brouillon 4 : {B4.name}, sha256 {sha(B4)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
