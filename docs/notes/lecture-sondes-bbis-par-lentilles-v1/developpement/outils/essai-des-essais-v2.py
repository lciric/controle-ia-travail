"""Essai des essais, version 2 : les altérations que la contre-lecture avait trouvées invisibles (rapport, § 2), plus celles des
ajouts de la version 2. Chaque altération doit faire tomber au moins un essai de `test_lentilles_sondes_bbis_gardes_non_vues_v1.py`
(le fichier altéré est remis en l'état). Lancer depuis la racine du dépôt."""
import subprocess
import sys
from pathlib import Path

B = Path("src/controle_ia/lentilles_sondes_bbis")
ESSAI = "tests/test_lentilles_sondes_bbis_gardes_non_vues_v1.py"
M = [
 ("lanceur_v2.py", 'd["poles"]["libelle"] = st.libelle(p[nul_iso], p[K.NUL_SIGNES])',
  'd["poles"]["libelle"] = st.libelle(p.get(K.NUL_ISOTROPE + "_remplacee", p.get(nul_iso)), p[K.NUL_SIGNES])'),
 ("lanceur_v2.py", "            self.controle_disque()\n", "            pass\n"),
 ("lanceur_v2.py", "    if ctx.travail.exists():\n        raise Arret(f\"{ctx.travail} existe déjà", "    if False:\n        raise Arret(f\"{ctx.travail} existe déjà"),
 ("lanceur_v2.py", "        if chemin.exists():\n            raise Arret(f\"{chemin} existe déjà (R12)\")\n    charge = charger_montage(ctx)", "        pass\n    charge = charger_montage(ctx)"),
 ("lanceur_v2.py", "    if not chemin_etat.is_file():\n        raise Arret(\"montage absent du dossier de travail : rien ne part\")", "    if False:\n        raise Arret(\"montage absent du dossier de travail : rien ne part\")"),
 ("lanceur_v2.py", "    mo.aucune_occurrence([ctx.travail, ctx.sortie], cle)\n", "    pass\n"),
 ("lanceur_v2.py", "    essayer_tokeniseur_du_cache(ctx, voisin, hf_home)\n", "    pass\n"),
 ("lanceur_v2.py", "        if phrase is None:\n            ligne[\"note\"] = NOTE_POLES_INTERMEDIAIRES", "        if False:\n            ligne[\"note\"] = NOTE_POLES_INTERMEDIAIRES"),
 ("entrees_v2.py", "    if b.shape != (1,) or b.dtype.kind != \"f\":", "    if False:"),
 ("montage_v1.py", "        if (c.sorte == \"octet\" and len(recu) != 1) or (c.sorte != \"octet\" and len(recu) < 1):", "        if False:"),
 ("montage_v1.py", "    if tete != commit:", "    if False:"),
 ("montage_v1.py", "              and all(p.stat().st_size == self.description[nom][\"octets\"] for nom, p in partiels.items()))", "              )"),
 ("montage_v1.py", "    if lu.get(\"modele\") != K.DEPOT_LLAMA or len(lu[\"ids\"]) != len(lu[\"chaines\"]):", "    if False:"),
 ("lecture_v1.py", "    if wu.dtype != torch.float32:", "    if False:"),
]
ko = 0
for fichier, avant, apres in M:
    p = B / fichier
    source = p.read_text()
    if source.count(avant) != 1:
        print("MOTIF INTROUVABLE OU MULTIPLE :", fichier, avant[:60].replace("\n", " "))
        ko += 1
        continue
    p.write_text(source.replace(avant, apres))
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAI], capture_output=True, text=True)
    finally:
        p.write_text(source)
    vu = r.returncode != 0
    ko += not vu
    print("vue " if vu else "NON VUE", fichier, "|", avant[:80].replace("\n", " "))
print("altérations non vues :", ko, "sur", len(M))
