"""Le lecteur d'en-tête du verrou (code v5) sur mes essais corrigés : même commit, même table qu'en v12. Lecture seule.
Arguments : sortie, puis les essais à lire."""
import hashlib
import importlib
import sys

P = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/"
COMMIT = "e308b84d68a85416fab1a80b0c116858d24b85a5"
PREFIXE = "- Commit du code d'analyse : "
sys.path = [P + "code-v5/src"] + [p for p in sys.path if not p.endswith("/src") and p not in ("", ".")]
graines = importlib.import_module("controle_ia.heritage_etage_processeur_v1.graines")
attendue = dict(reversed(x.split("  ", 1)) for x in open(P + "table-empreintes-code-v5.txt", encoding="utf-8").read().splitlines())
out = [f"module : {graines.__file__}"]
for chemin in sys.argv[2:]:
    b = open(chemin, "rb").read()
    lignes = b.decode("utf-8").split("\n")
    c, table = graines.lire_en_tete_du_texte(chemin)
    out.append(f"{chemin} {hashlib.sha256(b).hexdigest()} : lignes au préfixe {sum(1 for x in lignes if x.startswith(PREFIXE))} ; "
               f"commit {c} égal {c == COMMIT} ; table {len(table)} égale {table == attendue} ; "
               f"graines {list(graines.JOURNAL)}")
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(out) + "\n")
