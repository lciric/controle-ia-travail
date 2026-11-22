"""Forme la version servie de la question « exploration et allumage » : corps seul (de la première ligne qui commence par
« « » jusqu'à la fin), sans titre ni en-tête de rédaction. Source vérifiée par empreinte. Contrôles : aucun nom de
session ou de modèle, aucune mention de devinette, aucun chemin ; zéro motif à la garde de motifs. N'écrase jamais."""
import hashlib, re, subprocess, sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
from controle_ia.relecture_fable_api_v3 import garde_motifs_ligne
E_SOURCE = "3d4a1781946ae45d"
src = subprocess.run(["git", "-C", "/home/user/main-lecture", "show",
                      "origin/claude/exploration-idees-fable-v1:docs/notes/exploration-idees-fable-v1/question-neutre-exploration-et-allumage-v2.md"],
                     capture_output=True, check=True).stdout
if not hashlib.sha256(src).hexdigest().startswith(E_SOURCE):
    sys.exit("REFUS : empreinte de la source")
lignes = src.decode("utf-8").split("\n")
debut = next(i for i, l in enumerate(lignes) if l.startswith("«"))
corps = "\n".join(lignes[debut:]).strip("\n") + "\n"
interdits = re.compile(r"(?i)session|fable|opus|sonnet|claude|gemini|kimi|astra|argon|carbon|neon|devinette|protocole x|"
                       r"\.md\b|/|`|https?:")
if interdits.search(corps):
    sys.exit("REFUS : motif interdit dans le corps : " + interdits.search(corps).group(0))
if any(garde_motifs_ligne(l) for l in corps.split("\n")):
    sys.exit("REFUS : la garde de motifs mord")
with open(sys.argv[1], "xb") as f:
    f.write(corps.encode("utf-8"))
print(hashlib.sha256(corps.encode()).hexdigest(), len(corps.encode()), "octets", debut + 1, "première ligne du corps")
