"""Essai des essais : chaque altération du code doit faire tomber au moins un essai ciblé (le fichier est remis en l'état)."""
import subprocess, sys
from pathlib import Path
B = Path("src/controle_ia/lentilles_sondes_bbis")
M = [
 ("entrees_v1.py", 'if not m or m.group("objet") not in OBJETS_DECODES:', 'if not m:', "entrees"),
 ("entrees_v1.py", 'if not lignes["VERDICT-BBIS"]:', 'if False:', "entrees"),
 ("entrees_v1.py", 'if len(scores) > 1:', 'if False:', "entrees"),
 ("entrees_v1.py", "or (self._source(chemin) and len(chemin) == 4 and chemin[3] in CHAMPS_SONDE)", "or (self._source(chemin) and len(chemin) == 4)", "entrees"),
 ("entrees_v1.py", "if empreinte_sonde(famille, nom, couche, agregation, w, b, q) != attendue:", "if False:", "entrees"),
 ("entrees_v1.py", "if sha_e1 != _compagnon(racine, ch[\"e1_compagnon\"], course.run) or sha_e1 != vue.champ(\"fichier_sondes\", \"sha256\"):", "if False:", "entrees"),
 ("entrees_v1.py", "if a_q != (famille == \"attention\"):", "if False:", "entrees"),
 ("entrees_v1.py", "if agregation != K.AGREGATION_DE[famille]:", "if False:", "entrees"),
 ("entrees_v1.py", 'nom_e, att_e = K.AGREGATION_DE[fam_e], f"enc-{cellule}-{pli}"', 'nom_e, att_e = K.AGREGATION_DE[fam_e], f"enc-{cellule}-{pli[1]}"', "entrees"),
 ("montage_v1.py", "if valeur is None or not str(valeur).strip():", "if valeur is None:", "montage"),
 ("montage_v1.py", "k not in VARIABLES_CLE}", "k != 'RIEN'}", "montage"),
 ("montage_v1.py", "and self.hachage.hexdigest() == sha256_attendu", "", "montage"),
 ("montage_v1.py", "if identifiant_git(pointeur(sha256, taille)) != identifiant_attendu:", "if False:", "montage"),
 ("montage_v1.py", "if prov[\"capture_point\"] != K.POINT_DE_CAPTURE:", "if False:", "montage"),
 ("montage_v1.py", "            if _egales(J[a], J[b]):", "            if False:", "montage"),
 ("montage_v1.py", "        if _egales(J[l], None):", "        if False:", "montage"),
 ("montage_v1.py", "if len(ids) != int(n) or e != sha256:", "if len(ids) != int(n):", "montage"),
 ("montage_v1.py", "        if _source_fonction(a, nom) != _source_fonction(b, nom):", "        if False:", "montage"),
 ("montage_v1.py", "return (a.astype(np.uint32) << 16).view(np.float32)", "return a.astype(np.float32)", "montage"),
 ("montage_v1.py", "                    if motif in reste + bloc:", "                    if motif in bloc:", "procedure"),
 ("lecture_v1.py", "if empreinte_lue != empreintes_montage[int(couche_sonde)]:", "if False:", "lecture"),
 ("lecture_v1.py", "if differentes < K.MIN_COLONNES_ARTEFACT:", "if False:", "lecture"),
 ("lecture_v1.py", "return bool(rho_min >= K.SEUIL_RAPPORT_EPSILON)", "return bool(rho_min > K.SEUIL_RAPPORT_EPSILON + 2)", "lecture"),
 ("lecture_v1.py", "t = t * torch.rsqrt(t.pow(2).mean(0, keepdim=True) + K.EPSILON) * gamma.to(torch.float32)[:, None]", "t = t * torch.rsqrt(t.pow(2).mean(0, keepdim=True) + 1e-5) * gamma.to(torch.float32)[:, None]", "lecture"),
 ("lecture_v1.py", "if not bool(torch.isfinite(scores).all()) or not np.all(np.isfinite(rho)):", "if False:", "lecture"),
 ("nuls_v1.py", "u /= np.sqrt(np.mean(u ** 2, axis=1, keepdims=True))", "pass", "nuls_statistiques"),
 ("nuls_v1.py", "return int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], \"big\")", "return int.from_bytes(hashlib.sha256(cle.encode()).digest()[:8], \"little\")", "nuls_statistiques"),
 ("statistiques_v1.py", "return float((1 + int((s >= valeur).sum())) / (s.numel() + 1))", "return float((1 + int((s > valeur).sum())) / (s.numel() + 1))", "nuls_statistiques"),
 ("statistiques_v1.py", "if p_iso <= K.P_ISO_CONCENTREE and p_signes <= K.P_SIGNES_CONCENTREE:", "if p_iso <= K.P_ISO_CONCENTREE or p_signes <= K.P_SIGNES_CONCENTREE:", "nuls_statistiques"),
 ("statistiques_v1.py", "ecart = scores_nuls.std(1, correction=0)", "ecart = scores_nuls.std(1, correction=0) * 1.01", "nuls_statistiques"),
 ("statistiques_v1.py", "signes = torch.cat([cos, -cos])", "signes = torch.cat([cos, cos])", "nuls_statistiques"),
 ("audits_v1.py", "if queue > niveau:", "if queue >= niveau * 2:", "nuls_statistiques"),
 ("audits_v1.py", "tout_negatif = bool(lectures) and not distinctes", "tout_negatif = False", "nuls_statistiques"),
 ("lanceur_v1.py", "        if self.ecoule() > self.limite:", "        if False:", "procedure"),
 ("lanceur_v1.py", "    if registre.name == K.REGISTRE_INTERDIT:\n        raise Refus(f\"clé de ce texte", "    if False:\n        raise Refus(f\"clé de ce texte", "procedure"),
 ("lanceur_v1.py", "        if not tenue:\n            self._repli(directions)", "        if False:\n            self._repli(directions)", "procedure"),
 ("lanceur_v1.py", "    en.exiger_scores_et_verdict(registre_bbis)\n    if not (ctx.travail / MARQUE).is_file():", "    if not (ctx.travail / MARQUE).is_file():", "procedure"),
 ("lanceur_v1.py", "                \"-\": st.lecture_signe(-a, nuls,", "                \"-\": st.lecture_signe(a, nuls,", "procedure"),
 ("lanceur_v1.py", "        j_suivante, _, _ = charge.publique.matrice(couches[(i + 1) % len(couches)])", "        j_suivante, _, _ = charge.publique.matrice(couche)", "montage"),
 ("phrases_v1.py", "ne se distingue pas du nul ({p})", "ne se distingue pas des nuls ({p})", "procedure"),
]
ko = 0
for fichier, avant, apres, essai in M:
    p = B / fichier
    source = p.read_text()
    if source.count(avant) != 1:
        print("MOTIF INTROUVABLE OU MULTIPLE :", fichier, avant[:60]); ko += 1; continue
    p.write_text(source.replace(avant, apres))
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", f"tests/test_lentilles_sondes_bbis_{essai}_v1.py"], capture_output=True, text=True)
    finally:
        p.write_text(source)
    vu = r.returncode != 0
    ko += not vu
    print("vue " if vu else "NON VUE", fichier, "|", avant[:70].replace("\n", " "))
print("altérations non vues :", ko, "sur", len(M))
