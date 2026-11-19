"""Construit la version c1 du brouillon 6 de relance à partir du brouillon 6 de relance (67cd36f1…).

Remplacements exacts (ancre unique, sinon arrêt). Le marqueur @@GRILLE@@ est rempli depuis les sorties du rejeu de la
grille (travail/rejeu-grille-c1/sorties/), lues par programme : 24 fichiers exigés, sinon arrêt.
"""
import hashlib
import math
import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
from changements_c1_v1 import K  # noqa: E402
from construire_brouillon6_relance_v1 import appliquer  # noqa: E402

B6 = ICI.parent / "papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19.md"
SHA_B6 = "67cd36f19782ec9ff0588c235f1b8ff27c40504f5288991ff1f20b0fa93c0e0d"
SORTIE = ICI.parent / "papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c1.md"
JOURNAL = ICI / "construire_brouillon6_relance_c1_v1.journal.tsv"
GRILLE = ICI / "rejeu-grille-c1"


def fr(x: float) -> str:
    return f"{x:.3f}".replace(".", ",")


def grille() -> str:
    lignes = []
    for s in ("N0", "N1", "N2", "N3", "N4", "N5"):
        for k in (3, 5):
            for T in (45, 60):
                f = GRILLE / "sorties" / f"u3_{s}_k{k}_T{T}.txt"
                t = f.read_text(encoding="utf-8")
                tete = t.split("\n")[0]
                if f"scenario {s} ; k = {k} ; T = {T} ; R = 1000 ; B = 1000 ; graine 20261021" not in tete:
                    raise SystemExit(f"ARRÊT : en-tête inattendu dans {f.name}")
                v = {}
                for nom in ("conj2", "conj3"):
                    m = re.search(rf"^{nom}\s+\|\s+([0-9.]+) ± [0-9.]+ \|\s+([0-9.]+) ± ", t, re.M)
                    if not m:
                        raise SystemExit(f"ARRÊT : ligne {nom} absente de {f.name}")
                    v[nom] = (float(m.group(1)), float(m.group(2)))
                lignes.append((s, k, T, v))
    if len(lignes) != 24:
        raise SystemExit("ARRÊT : 24 cases exigées")
    seuil = 0.05 + 2 * math.sqrt(0.05 * 0.95 / 1000)
    a3 = [x[3]["conj3"][0] for x in lignes]
    b3 = [x[3]["conj3"][1] for x in lignes]
    a2 = [x[3]["conj2"][0] for x in lignes]
    b2 = [x[3]["conj2"][1] for x in lignes]
    hors_a = [f"{s}, k = {k}, {T} tâches ({fr(v['conj3'][0])})" for s, k, T, v in lignes if v["conj3"][0] > seuil]
    hors_b = [f"{s}, k = {k}, {T} tâches ({fr(v['conj3'][1])})" for s, k, T, v in lignes if v["conj3"][1] > seuil]
    manif = hashlib.sha256((GRILLE / "sha256sums-sorties-v1.txt").read_bytes()).hexdigest()
    txt = ("rejeu par ce rédacteur, sur processeur, des 24 cases « scénarios nuls N0 à N5 × k = 3 et 5 × 45 et 60 tâches » "
           "pour C-P3a et C-P3b, avec le programme U3 de l'archive (1 000 essais × 1 000 tirages par grappes, graine "
           "20261021 ; programmes, lanceur et sorties sous `travail/rejeu-grille-c1/`, manifeste "
           f"`sha256sums-sorties-v1.txt`, `{manif}`) : aux trois lectures jointes, « établie » dans {fr(min(a3))} à "
           f"{fr(max(a3))} des essais pour C-P3a et {fr(min(b3))} à {fr(max(b3))} pour C-P3b ; aux deux premières "
           f"lectures seules, {fr(min(a2))} à {fr(max(a2))} et {fr(min(b2))} à {fr(max(b2))} ; seuil de la clause à "
           f"1 000 essais : {fr(seuil)}. ")
    if hors_a or hors_b:
        txt += ("**Cases au-dessus du seuil aux trois lectures** : C-P3a : " + (" ; ".join(hors_a) or "aucune")
                + " ; C-P3b : " + (" ; ".join(hors_b) or "aucune")
                + ". Selon la clause, la statistique concernée passe « rapportée sans verdict » si le rapport du "
                  "sous-agent neuf le confirme ; ce rejeu du rédacteur ne tient pas lieu de ce rapport. ")
    else:
        txt += "Aucune de ces 24 cases ne dépasse le seuil aux trois lectures. "
    txt += "Ce rejeu est une mesure de conception sur données simulées, jamais un résultat."
    return txt


def main() -> None:
    t = B6.read_text(encoding="utf-8")
    if hashlib.sha256(t.encode("utf-8")).hexdigest() != SHA_B6:
        raise SystemExit("ARRÊT : empreinte du brouillon 6 de relance non conforme")
    journal = ["id\tremarque\tsection\tchangement"]
    for c in K:
        t = appliquer(t, c)
        journal.append("\t".join([c["id"], c["cl"], c["section"], c["resume"]]))
    if t.count("@@GRILLE@@") != 1:
        raise SystemExit("ARRÊT : marqueur @@GRILLE@@ non unique")
    t = t.replace("@@GRILLE@@", grille())
    if "@@" in t:
        raise SystemExit("ARRÊT : marqueur @@ restant")
    if SORTIE.exists():
        raise SystemExit("ARRÊT : la sortie existe déjà (R12 : on n'écrase pas)")
    SORTIE.write_text(t, encoding="utf-8")
    JOURNAL.write_text("\n".join(journal) + "\n", encoding="utf-8")
    print(f"changements : {len(K)}")
    print(f"sortie : {SORTIE.name} ; {len(t.encode('utf-8'))} octets ; sha256 {hashlib.sha256(t.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
