"""Lecture double à l'aveugle (protocole X v2, règle 3) : second lecteur, Astra (OpenAI), par la fonction d'appel du
collisionneur v9-v8r (interface Responses en arrière-plan, relevés courts). Classe B, petit instrument.
Usage : PYTHONPATH=src python3 -B lecteur_astra_v1.py DOSSIER_DU_RUN SORTIE.md
L'invite = consigne + question + cellules du dossier, désignées par leurs seules lettres (noms de modèles retirés)."""
import importlib.util, json, re, sys
from pathlib import Path
ICI = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c", ICI.parent / "collisionneur_v9_v8r.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
D, SORTIE = Path(sys.argv[1]), Path(sys.argv[2])
if SORTIE.exists():
    sys.exit(f"{SORTIE} existe déjà : on n'écrase jamais")
NOMS = re.compile(r"(?i)\b(claude|anthropic|fable|opus|sonnet|haiku|gemini|google|carbon|neon|argon|gpt|openai|astra|kimi|moonshot|mistral)\b")
parties = [(ICI / "lecture-double-v1" / "consigne-lecteur-v1.md").read_text(encoding="utf-8"),
           "## Question servie aux modèles\n\n" + (D / "question-etage3.md").read_text(encoding="utf-8")]
for f in sorted((D / "cellules").glob("E3-*.md")):
    t = NOMS.sub("[modèle]", f.read_text(encoding="utf-8"))
    parties.append(f"## Cellule {f.stem} (lettre {f.stem[-1]})\n\n{t}")
prompt = "\n\n".join(parties)
c.fixer_composition(["opus", "astra"], nom_cle_openai="OPENAI_API_KEY_2")
m = dict(c.MODELES["B"]); assert m["id"] == "gpt-6.2-astra"
print(f"invite : {len(prompt)} caractères ; plafond de sortie {m['max_relance']}", flush=True)
rep = c.appeler_openai(m, prompt, m["max_relance"])
cout = c.cout(m["prix"], rep.usage)
print(json.dumps({"fin": rep.fin, "echec": rep.echec, "interrompue": rep.interrompue, "usage": rep.usage,
                  "modele_servi": rep.modele_servi, "cout_usd": round(cout, 4)}, ensure_ascii=False), flush=True)
SORTIE.write_text(rep.texte or "", encoding="utf-8")
if rep.echec or rep.interrompue or "FIN DE LA LISTE" not in (rep.texte or ""):
    sys.exit("réponse incomplète ou en échec : défaut, jamais une lecture")
