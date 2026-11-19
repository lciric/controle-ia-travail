"""Construit le brouillon 6 de relance du préenregistrement du papier C à partir du brouillon 5.

Chaque changement du corps est un remplacement exact : l'ancre de début doit se trouver une seule fois dans le texte
courant, sinon arrêt (aucun repli silencieux). L'en-tête (tout ce qui précède « ## Hypothèse ») est remplacé en bloc.
L'énoncé de HC2 et la formulation de citation de MIRAGE sont recopiés par programme depuis la décision N-068.
Usage : python3 -B construire_brouillon6_relance_v1.py   (aucun argument ; chemins fixes ci-dessous)
"""
import hashlib
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from changements_a_v1 import A  # noqa: E402
from changements_b_v1 import B  # noqa: E402
from changements_c_v1 import C  # noqa: E402

DEPOT = Path("/home/user/controle-ia-travail")
B5 = DEPOT / "brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md"
SHA_B5 = "9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969"
N068 = DEPOT / "docs/decisions/decision-N-068-v1.md"
SHA_N068 = "ba6b2db355515cd660d676b733f4d467f8a9c055d4d8c6d997d4ef898caef889"
ENTETE = ICI / "entete_b6_relance_v1.md"
SORTIE = ICI.parent / "papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19.md"
JOURNAL = ICI / "construire_brouillon6_relance_v1.journal.tsv"

D = [
    dict(id="C-40c", section="Plan, section 1, accord par lancement",
         avant="ligne d'accord du jour sous GO-2026-10-20-07",
         apres="sous GO-2026-10-20-07 ou la délégation en vigueur au jour du lancement (elle échoit aussi le 2026-11-30)",
         commande="`registres/go.md`, GO-2026-10-20-07 (échéance 2026-11-30) ; décision D-4",
         op=("rep", "(GO-2026-10-20-07) ; instance arrêtée par son identifiant à la fin et à la borne (R10), consignée dans",
             "(GO-2026-10-20-07, qui échoit le 2026-11-30, ou la délégation en vigueur au jour du lancement : décision D-4) ;\n"
             "instance arrêtée par son identifiant à la fin et à la borne (R10), consignée dans")),
    dict(id="C-58b", section="Contre-lecture, premier paragraphe",
         avant="table de traitement du brouillon 5 dite « versée avec ce brouillon »",
         apres="dite dans l'archive du 20 octobre, à verser (verrou 5)",
         commande="vérification sur disque (R11) : `brouillons/` ne porte que le brouillon 5 et son compagnon",
         op=("rep", "application constat par constat dans `table-traitement-brouillon5-v1.md`, versée avec ce brouillon) :",
             "application constat par constat dans `table-traitement-brouillon5-v1.md`, dans l'archive du 20 octobre, à verser,\n"
             "verrou 5) :")),
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def appliquer(texte: str, c: dict) -> str:
    op = c["op"]
    if op[0] == "rep":
        _, ancien, nouveau = op
        n = texte.count(ancien)
        if n != 1:
            raise SystemExit(f"ARRÊT {c['id']} : ancre trouvée {n} fois (attendu 1) : {ancien[:90]!r}")
        return texte.replace(ancien, nouveau)
    if op[0] == "bloc":
        _, debut, fin, nouveau = op
        n = texte.count(debut)
        if n != 1:
            raise SystemExit(f"ARRÊT {c['id']} : ancre de début trouvée {n} fois (attendu 1) : {debut[:90]!r}")
        i = texte.index(debut)
        j = texte.find(fin, i + len(debut))
        if j < 0:
            raise SystemExit(f"ARRÊT {c['id']} : ancre de fin absente après le début : {fin[:90]!r}")
        if j - i > 12000:
            raise SystemExit(f"ARRÊT {c['id']} : bloc de {j - i} caractères, trop long pour être voulu")
        return texte[:i] + nouveau + texte[j + len(fin):]
    raise SystemExit(f"ARRÊT {c['id']} : opération inconnue")


def main() -> None:
    if sha(B5) != SHA_B5:
        raise SystemExit("ARRÊT : empreinte du brouillon 5 non conforme")
    if sha(N068) != SHA_N068:
        raise SystemExit("ARRÊT : empreinte de la décision N-068 non conforme")
    b5 = B5.read_text(encoding="utf-8")
    coupe = "\n## Hypothèse\n"
    if b5.count(coupe) != 1:
        raise SystemExit("ARRÊT : titre « ## Hypothèse » non unique")
    corps = b5[b5.index(coupe) + 1:]
    entete = ENTETE.read_text(encoding="utf-8")

    lignes = N068.read_text(encoding="utf-8").split("\n")
    enonce = lignes[64]
    if not enonce.startswith("> Pour une sonde qui lit l'**agent auteur"):
        raise SystemExit("ARRÊT : ligne 65 de N-068 inattendue")
    enonce = enonce[2:]
    cit = lignes[70]
    if not cit.startswith("- **Formulation de citation**"):
        raise SystemExit("ARRÊT : ligne 71 de N-068 inattendue")
    cit = cit[cit.index("« ") + 2: cit.rindex(" »")]

    journal = ["id\tsection\tavant\taprès\tcommandé par"]
    journal.append("C-01\tEn-tête (titre, auteur, date, rôle, historique, ce que change ce brouillon, verrous, champs du scellement, GO, documents qui font foi, pièces de contre-lecture)\ten-tête du brouillon 5\tremplacé en bloc (fichier entete_b6_relance_v1.md)\tmandat ; registres/go.md ; registres/decisions.md ; vérifications sur disque")
    for c in A + B + C + D:
        corps = appliquer(corps, c)
        journal.append("\t".join([c["id"], c["section"], c["avant"], c["apres"], c["commande"]]))
    for nom, val in (("@@HC2_ENONCE@@", enonce), ("@@MIRAGE_CITATION@@", cit)):
        if corps.count(nom) != 1:
            raise SystemExit(f"ARRÊT : marqueur {nom} non unique")
        corps = corps.replace(nom, val)
    texte = entete + corps
    if "@@" in texte:
        raise SystemExit("ARRÊT : marqueur @@ restant")
    if enonce not in texte or cit not in texte:
        raise SystemExit("ARRÊT : énoncé ou citation de N-068 absents du texte")
    SORTIE.write_text(texte, encoding="utf-8")
    JOURNAL.write_text("\n".join(journal) + "\n", encoding="utf-8")
    print(f"changements du corps : {len(A + B + C + D)} ; plus l'en-tête")
    print(f"sortie : {SORTIE} ; {len(texte.encode('utf-8'))} octets ; sha256 {hashlib.sha256(texte.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
