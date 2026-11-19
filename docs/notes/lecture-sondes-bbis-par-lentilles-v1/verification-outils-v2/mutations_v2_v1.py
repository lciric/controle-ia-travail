"""Vérification de la version 2 : mes altérations survivantes de la version 1 (gardes réelles), celle du libellé des pôles après
repli, et celles de mes corrections, rejouées sur les modules de la version 2, contre les essais neufs (gardes non vues,
corrections du contre-lecteur). Copie extraite du commit 08dea10b, chaque fichier remis en l'état."""
import os, subprocess, sys
from pathlib import Path
R = Path(sys.argv[1]); PY = sys.argv[2]
B = R / "src/controle_ia/lentilles_sondes_bbis"
ESSAIS = ["tests/test_lentilles_sondes_bbis_gardes_non_vues_v1.py", "tests/test_lentilles_sondes_bbis_corrections_contre_lecture_v1.py"]
M = [
 # survivants réels de la première série (v1)
 ("entrees_v2.py", 'if vue.champ("run_id") != run:', "if False:"),
 ("entrees_v2.py", "if scellement.chemin != K.TEXTE or scellement.sha256 != K.EMPREINTE_TEXTE:", "if False:"),
 ("entrees_v2.py", "    if vue.champ(\"fichier_sondes\", \"fichier\") != ch[\"e1\"]:", "    if False:"),
 ("entrees_v2.py", "if vue.champ(*src, \"cellule\") != cellule or vue.champ(*src, \"pli_lu\") != int(pli[1]):", "if False:"),
 ("entrees_v2.py", "    if b.shape != (1,) or b.dtype.kind != \"f\":", "    if False:"),
 ("montage_v1.py", "        if (c.sorte == \"octet\" and len(recu) != 1) or (c.sorte != \"octet\" and len(recu) < 1):", "        if False:"),
 ("montage_v1.py", "    if tete != commit:", "    if False:"),
 ("montage_v1.py", "              and all(p.stat().st_size == self.description[nom][\"octets\"] for nom, p in partiels.items()))", "              )"),
 ("montage_v1.py", "    if lu.get(\"modele\") != K.DEPOT_LLAMA or len(lu[\"ids\"]) != len(lu[\"chaines\"]):", "    if False:"),
 ("lecture_v1.py", "    if wu.dtype != torch.float32:", "    if False:"),
 # survivants de la seconde série (v1), dont le libellé des pôles après repli
 ("lanceur_v2.py", "        d[\"poles\"][\"libelle\"] = st.libelle(p[nul_iso], p[K.NUL_SIGNES])", "        d[\"poles\"][\"libelle\"] = st.libelle(p[K.NUL_ISOTROPE + ('_remplacee' if nul_iso != K.NUL_ISOTROPE else '')], p[K.NUL_SIGNES])"),
 ("lanceur_v2.py", "            self.controle_disque()\n", ""),
 ("lanceur_v2.py", "    if ctx.travail.exists():\n        raise Arret(f\"{ctx.travail} existe déjà", "    if False:\n        raise Arret(f\"{ctx.travail} existe déjà"),
 ("lanceur_v2.py", "        if chemin.exists():\n            raise Arret(f\"{chemin} existe déjà (R12)\")\n    charge", "        pass\n    charge"),
 ("lanceur_v2.py", "    if not chemin_etat.is_file():", "    if False:"),
 ("lanceur_v2.py", "    mo.aucune_occurrence([ctx.travail, ctx.sortie], cle)\n    horloge.consigner()", "    horloge.consigner()"),
 # mes corrections A à D
 ("lanceur_v2.py", '    if not p.is_file() or mo.sha256_fichier(p) != ligne_code.sha256:', '    if not p.is_file():'),
 ("lanceur_v2.py", '        if fichiers.get(nom) != mo.sha256_fichier(ici / f"{m}.py"):', '        if False:'),
 ("lanceur_v2.py", '    if not forme:', '    if False:'),
 ("entrees_v2.py", '    if not derniere < course.heure_verdict:', '    if False:'),
 ("entrees_v2.py", '    if not lignes["ABSENCE-VERDICT-LENTILLES-BBIS"] or not lignes["SCELLEMENT-LENTILLES-BBIS"]:', '    if False:'),
 ("lanceur_v2.py", '        if t == s or t in s.parents or s in t.parents:', '        if False:'),
 ("lanceur_v2.py", '    versement = verser_travail(travail, sortie, run, "fin")\n    verifier(Path(sortie) / versement["chemin"])\n', '    versement = {}\n'),
 ("lanceur_v2.py", '        if rel.parts[0] not in NON_COPIES:', '        if True:'),
 ("lanceur_v2.py", '        if not etat["parti"]:\n            raise', '        if True:\n            raise'),
 ("lanceur_v2.py", '                rendu["morceaux"] = [{"fichier": m["fichier"], "sha256": m["sha256"]} for m in rendu["morceaux"]]', '                pass'),
 # ajouts de la version 2
 ("lanceur_v2.py", "    essayer_tokeniseur_du_cache(ctx, voisin, hf_home)\n", ""),
 ("lanceur_v2.py", "            ligne[\"note\"] = NOTE_POLES_INTERMEDIAIRES\n", "            pass\n"),
 ("lanceur_v2.py", "                ligne_registre(\"ENTREES-LENTILLES-BBIS\", f\"diag/{ctx.run}/entrees-lentilles-bbis.json\", sha_entrees),", "                ligne_registre(\"ENTREES-LENTILLES-BBIS\", entrees.course.chemin_e2, entrees.sha256_e2),"),
]
for f, a, b in M:
    p = B / f; s = p.read_text()
    if s.count(a) != 1: print("MOTIF INTROUVABLE", f, a[:70].replace("\n", " "), flush=True); continue
    p.write_text(s.replace(a, b))
    try:
        r = subprocess.run([PY, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", f"--basetemp={sys.argv[3]}"] + ESSAIS,
                           cwd=R, capture_output=True, text=True, env={**os.environ, "PYTHONPATH": "src"})
    finally:
        p.write_text(s)
    print("vue    " if r.returncode else "SURVIT ", f, "|", a.strip()[:80].replace("\n", " "), flush=True)
