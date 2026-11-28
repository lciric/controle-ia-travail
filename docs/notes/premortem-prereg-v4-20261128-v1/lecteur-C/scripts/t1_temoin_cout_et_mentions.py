"""T1 — témoin : recalcul, depuis mesures.jsonl (64 blocs, commit 42cdfcf29), par la définition scellée de
`controle_ia.t06.cout.cout_lisible`, des coûts illisibles de `honnete` et `consigne_neutre`, et de la part de
`mention_texte_prive` de `consigne_neutre`, `gonfle_3`, `gonfle_5` ; comparaison au résultat scellé
`lecture-cout-dose-reponse.json` (70baf0e6…). Second recalcul, indépendant du champ `cout` écrit par la course :
le coût est relu sur le texte brut par `controle_ia.t06.cout.cout_action`."""
import glob, hashlib, json, sys
from pathlib import Path
from controle_ia.t06.cout import cout_lisible, cout_action

DONNEES, RESULTAT, SORTIE = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sha = hashlib.sha256(RESULTAT.read_bytes()).hexdigest()
scelle = json.loads(RESULTAT.read_text())["resultat"]["manipulation"]
mes, textes = [], {}
for b in sorted(glob.glob(str(DONNEES / "*" / "mesures.jsonl"))):
    mes += [json.loads(l) for l in open(b)]
for b in sorted(glob.glob(str(DONNEES / "*" / "textes.jsonl"))):
    for l in open(b):
        d = json.loads(l); textes[d["cle"]] = d["texte"]
out = {"resultat_scelle_sha256": sha, "actions_lues": len(mes), "blocs": len(glob.glob(str(DONNEES / "*" / "mesures.jsonl"))), "conditions": {}}
ok = sha.startswith("70baf0e6") and len(mes) == 19200
for c in ("honnete", "consigne_neutre", "gonfle_3", "gonfle_5"):
    L = [l for l in mes if l["condition"] == c]
    n = len(L)
    illis = sum(not cout_lisible(l["cout"]) for l in L)
    illis_texte = sum(not cout_lisible(cout_action(textes[l["cle"]])["cout"]) for l in L)
    ment = sum(bool(l["mention_texte_prive"]) for l in L)
    s = scelle[c]
    ligne = {"actions": n, "illisibles_recalcul": illis, "illisibles_recalcul_depuis_texte": illis_texte,
             "illisibles_scelle": s["illisibles"], "mentions": ment, "part_mention_recalcul": ment / n,
             "part_mention_scelle": s["part_mention_texte_prive"],
             "accord": illis == s["illisibles"] == illis_texte and abs(ment / n - s["part_mention_texte_prive"]) < 1e-12 and n == s["actions"]}
    ok = ok and ligne["accord"]
    out["conditions"][c] = ligne
n0 = out["conditions"]["consigne_neutre"]["part_mention_recalcul"]
out["ecarts_au_temoin_neutre"] = {c: out["conditions"][c]["part_mention_recalcul"] - n0 for c in ("gonfle_3", "gonfle_5")}
out["verdict_T1"] = "TEMOIN TENU" if ok else "TEMOIN EN DEFAUT"
SORTIE.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print(json.dumps(out, ensure_ascii=False, indent=1))
