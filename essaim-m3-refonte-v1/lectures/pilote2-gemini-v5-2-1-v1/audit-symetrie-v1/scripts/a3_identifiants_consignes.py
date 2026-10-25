"""Audit de symétrie, pilote 2 — les identifiants de tâches de test parviennent-ils au modèle (consignes conservées par le
noyau), et les réponses du modèle les invoquent-elles ? Lecture seule de fichiers texte.
Usage : python3 -I a3_identifiants_consignes.py RACINE_ESPACE_TRAVAIL_M RACINE_ESPACE_TRAVAIL_S"""
import json, sys, re, pathlib, collections

BANQ = "/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/banque/banque-confrontation-v1.json"
b = json.load(open(BANQ))
part = {t["id"]: p for p in ("train", "test", "test_final") for t in b[p]}
fam = {t["id"]: t["famille"] for p in ("train", "test", "test_final") for t in b[p]}
motif_id = re.compile(r"\b(cd-lot[12]-L[12]-\d\d-[HS]|ce-hf-\d{4})\b")
# mots qui évoqueraient l'usage de l'identifiant ou de son suffixe
motif_suffixe = re.compile(r"(suffix|suffixe|identifiant|\bID\b|task[ _-]?id|\-S\b|\-H\b|ends? with|se termine par|nom de la t[âa]che|naming)", re.I)

for nom, racine in zip(("M", "S"), sys.argv[1:3]):
    for g in ("g000", "g001"):
        d = pathlib.Path(racine) / f"{g}.noyau" / "appels"
        prompts = sorted(d.glob("*.prompt.txt"))
        n_avec_id_test = 0; ids_vus = collections.Counter(); roles = collections.Counter()
        un_id_par_consigne = 0; exemples = []
        evocations = []
        for p in prompts:
            txt = p.read_text(encoding="utf-8", errors="replace")
            ids = set(motif_id.findall(txt))
            ids_test = {i for i in ids if part.get(i) in ("test", "test_final")}
            if ids_test:
                n_avec_id_test += 1
                for i in ids_test:
                    ids_vus[(part[i], fam[i])] += 1
                if len(ids_test) == 1:
                    un_id_par_consigne += 1
                    if len(exemples) < 1 and next(iter(ids_test)).startswith("cd-"):
                        i = next(iter(ids_test)); k = txt.find(i)
                        exemples.append((p.name, txt[max(0, k - 300):k + 200].replace("\n", " ⏎ ")))
            rep = p.with_name(p.name.replace(".prompt.txt", ".reponse.txt"))
            if rep.exists() and ids_test and any(i.startswith("cd-") for i in ids_test):
                rt = rep.read_text(encoding="utf-8", errors="replace")
                for m in motif_suffixe.finditer(rt):
                    evocations.append((rep.name, rt[max(0, m.start() - 120):m.end() + 120].replace("\n", " ")))
        print(f"\n== {nom} {g} : {len(prompts)} consignes ; {n_avec_id_test} portent au moins un identifiant de test/test_final ;"
              f" {un_id_par_consigne} en portent exactement un ; comptes (part, famille) : {dict(ids_vus)}")
        for e in exemples:
            print("   exemple", e[0], ":", e[1][:520])
        print(f"   réponses de tâches B qui contiennent un mot évoquant l'identifiant ou le suffixe : {len(evocations)}")
        for e in evocations[:8]:
            print("     ", e[0], ":", e[1][:260])
