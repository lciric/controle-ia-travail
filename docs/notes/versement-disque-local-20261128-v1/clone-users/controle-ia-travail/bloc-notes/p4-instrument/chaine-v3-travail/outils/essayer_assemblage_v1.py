"""Essai d'assemblage du candidat 2 (pas un candidat) par le correcteur de la chaîne v3 : `ecrire_candidat2_v1.py` joué
deux fois, paires du module v3 (corrigées par sa vérification) puis paires de la chaîne v3, et dans l'ordre inverse ;
même texte exigé (aucune collision : chaque ancre trouvée une fois, dans les deux ordres) ; puis, sur le texte :
`controle_ia.prereg.problemes` (validateur gelé), table « Critères de lecture gelés » égale à celle du module v3,
lignes « Module de P4 » aux empreintes du module v3, « Tests attendus : `N` » une fois, et chaque « nouveau » des paires
de la chaîne v3 présent une fois.
Usage : python3 -I -B essayer_assemblage_v1.py PY_SRC MODULE CHAINE ECRIVAIN CANDIDAT1 PAIRES_MODULE PAIRES_CHAINE TESTS SORTIE_DIR"""
import sys
sys.dont_write_bytecode = True
import hashlib, json, re, subprocess  # noqa: E402
from pathlib import Path  # noqa: E402
SRC, MOD, CH, ECR, C1, PM, PC, N, OUT = sys.argv[1:10]
OUT = Path(OUT); OUT.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, SRC); sys.path.insert(0, MOD)
import instrument_p4_v1 as ip  # noqa: E402
import lecture_p4_v1 as lp  # noqa: E402
from controle_ia.prereg import problemes  # noqa: E402
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
m, c = json.loads(Path(PM).read_text(encoding="utf-8")), json.loads(Path(PC).read_text(encoding="utf-8"))
res = {}
for nom, paires in (("module-puis-chaine", m + c), ("chaine-puis-module", c + m)):
    j = OUT / f"paires-{nom}.json"; j.write_text(json.dumps(paires, ensure_ascii=False, indent=1), encoding="utf-8")
    s = OUT / f"assemblage-{nom}-NON-CANDIDAT.md"
    r = subprocess.run([sys.executable, "-I", "-B", ECR, C1, str(s), MOD, CH, N, str(j)], capture_output=True, text=True)
    res[nom] = {"code": r.returncode, "erreur": r.stderr.strip()[-300:], "sha256": sha(s) if s.exists() else None}
texte = (OUT / "assemblage-module-puis-chaine-NON-CANDIDAT.md").read_text(encoding="utf-8")
lm = ip.lignes_module(texte)
sortie = {
    "ecrivain_sha256": sha(ECR), "candidat1_sha256": sha(C1), "paires_module_sha256": sha(PM), "paires_chaine_sha256": sha(PC),
    "paires": {"module": len(m), "chaine": len(c)}, "ordres": res,
    "meme_texte_dans_les_deux_ordres": res["module-puis-chaine"]["sha256"] == res["chaine-puis-module"]["sha256"] is not None,
    "problemes": problemes(str(OUT / "assemblage-module-puis-chaine-NON-CANDIDAT.md")),
    "table_egale_au_module": bool(lp.exiger_table_des_criteres(texte)),
    "lignes_module_egales_v3": {k: v == sha(Path(MOD) / Path(k).name) for k, v in lm.items()},
    "tests_attendus": re.findall(r"Tests attendus : `([0-9]+)`", texte),
    "nouveaux_de_la_chaine_presents_une_fois": [texte.count(p["nouveau"]) for p in c],
}
(OUT / "sortie-assemblage.json").write_text(json.dumps(sortie, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(sortie, ensure_ascii=False, indent=1))
ok = (all(r["code"] == 0 for r in res.values()) and sortie["meme_texte_dans_les_deux_ordres"] and sortie["problemes"] == []
      and sortie["table_egale_au_module"] and len(lm) == 6 and all(sortie["lignes_module_egales_v3"].values())
      and sortie["tests_attendus"] == [N] and all(x == 1 for x in sortie["nouveaux_de_la_chaine_presents_une_fois"]))
print("ASSEMBLAGE : CONFORME" if ok else "ASSEMBLAGE : NON CONFORME")
sys.exit(0 if ok else 1)
