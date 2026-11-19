"""Écrit la note des différences v2 : la v1, plus la garde 23 (omise), plus deux sections neuves."""
import hashlib
from pathlib import Path

R = Path(__file__).resolve().parent.parent
V1 = R / "note-differences-brouillon5-brouillon6-relance-v1.md"
V2 = R / "note-differences-brouillon5-brouillon6-relance-v2.md"
C1 = R / "papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19-c1.md"
TSV = R / "travail/construire_brouillon6_relance_c1_v1.journal.tsv"

t = V1.read_text(encoding="utf-8")
assert hashlib.sha256(t.encode()).hexdigest().startswith("80dd3075")
titre = "# Papier C — note des différences entre le brouillon 5 et le brouillon 6 de relance du préenregistrement — v1"
assert t.count(titre) == 1
t = t.replace(titre, titre[:-2] + "v2\n\nVersion 2 du 2026-11-19 : la v1 (`80dd3075…`) reste intacte. Ajouts : la garde 23 "
              "de la liste d'arrêt, omise en v1 (ligne C-57d) ; la section 4 (lecture du mandat pour le validateur) ; la "
              "section 5 (différences entre le brouillon 6 de relance et sa version c1). Le reste est celui de la v1 et "
              "décrit le brouillon 6 de relance (`67cd36f1…`).")
lignes = t.split("\n")
i = max(k for k, l in enumerate(lignes) if l.startswith("| C-57c |"))
lignes.insert(i + 1, "| C-57d | Liste d'arrêt, garde 23 (omise dans la note v1 ; relevée par la contre-lecture, CL-13) | "
              "aucune garde sur les paragraphes de plaidoyer | garde 23 : paragraphes de bras « plaidoyer » en nombre "
              "différent de k_P, ou dans un ordre différent de celui de la configuration scellée : arrêt | R5 ; cohérence "
              "avec C-42 (niveaux du plaidoyer, décision D-2) ; ajoutée par le même remplacement que les gardes 20 à 22 |")
t = "\n".join(lignes)
rows = [l.split("\t") for l in TSV.read_text(encoding="utf-8").strip().split("\n")[1:]]
b = C1.read_bytes()
sup = ["",
       "## 4. Validateur : ce que le mandat exempte, et ce que la consigne ajoute (CL-12)",
       "",
       "Le mandat (§ 2, point 1) veut une liste vide « sauf pour les cases qui demandent une décision du directeur ». La "
       "sortie du validateur porte en plus les treize marqueurs `<<…>>` du scellement et la case « Contre-lecture ». Ils "
       "ne sont pas exemptés par le mandat à la lettre : c'est la consigne du rédacteur (§ 1) qui les admet, comme "
       "lecture du mandat (ils ne peuvent être remplis qu'au scellement, ou par la session de conduite après la "
       "contre-lecture). Je le dis ici pour que la session mère confirme cette lecture.",
       "",
       "## 5. Différences entre le brouillon 6 de relance et sa version c1",
       "",
       "Avant : `papier-C-preenregistrement-HC1-HC3-v1-brouillon6-relance-2026-11-19.md` "
       "(`67cd36f19782ec9ff0588c235f1b8ff27c40504f5288991ff1f20b0fa93c0e0d`, 150 891 octets). Après : "
       f"`{C1.name}` (`{hashlib.sha256(b).hexdigest()}`, " + f"{len(b):,}".replace(",", " ") + " octets).",
       "",
       f"{len(rows)} remplacements exacts (`travail/changements_c1_v1.py`, `travail/construire_brouillon6_relance_c1_v1.py`), "
       "tous commandés par le rapport de contre-lecture `9a7121bc…` ou par sa suite (titre, verrous, section "
       "« Contre-lecture »). Le traitement remarque par remarque, avec ses motifs, est dans "
       "`table-traitement-contre-lecture-brouillon6-relance-v1.md`. Aucun énoncé d'hypothèse ne change entre les deux "
       "versions. Cases « À REMPLIR » : trois dans le brouillon 6 de relance (D-1, D-2, contre-lecture), sept dans la "
       "version c1 (D-1, D-2, D-8, D-15, D-16, D-17, contre-lecture).",
       "",
       "| n° | remarque | section | changement |",
       "|---|---|---|---|"]
for r in rows:
    assert len(r) == 4
    sup.append("| " + " | ".join(x.replace("|", "/") for x in r) + " |")
sup += ["",
        "Ce que la version c1 retire du brouillon 6 de relance : la réserve « déplacement au niveau le plus fort » "
        "(remplacée par la confirmation niveau par niveau) ; le seuil « moitié » de la réserve de contrôlabilité "
        "(renvoyé à D-17) ; la règle de mots de HC2b écrite d'office (renvoyée à D-8) ; la réfutation des deux côtés "
        "écrite d'office pour HC2 (renvoyée à D-15) ; la phrase « non rejoués par ce rédacteur, à rejouer par la "
        "contre-lecture ».", ""]
if V2.exists():
    raise SystemExit("ARRÊT : la note v2 existe déjà (R12)")
V2.write_text(t.rstrip("\n") + "\n" + "\n".join(sup), encoding="utf-8")
print(hashlib.sha256(V2.read_bytes()).hexdigest())
