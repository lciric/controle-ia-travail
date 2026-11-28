"""Assemble `rendu-lecteur-A-v1.md` a partir du gabarit et des sorties (nombres de E2, empreintes), puis ecrit la liste des
empreintes du dossier et le compagnon du rendu. Aucune ecriture hors du dossier du lecteur."""
import glob, hashlib, json, os, pathlib, subprocess, sys
D = pathlib.Path(sys.argv[1]); py = sys.executable
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def h(*noms):
    return " ; ".join(f"`{os.path.basename(n)}` `{sha(D / n)[:8]}…`" for n in noms)
# resume de E2, ecrit comme sortie
r = json.loads(subprocess.run([py, str(D / "scripts/e2_resume.py"), str(D / "sorties")], capture_output=True, text=True, check=True).stdout)
(D / "sorties/e2-resume.json").write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
# concatenation des mondes en un seul fichier de sortie
with open(D / "sorties/e2-mondes.jsonl", "w", encoding="utf-8") as f:
    for p in sorted(glob.glob(str(D / "sorties/e2/*.jsonl"))):
        f.write(open(p, encoding="utf-8").read())
fr = lambda x, n=2: f"{x:.{n}f}".replace(".", ",")
def cellule(cle):
    v = r[cle]
    return f"{fr(v['tenue_regle_ecrite'])} ; {fr(v['tenue_variante_sans_cout'])} (n = {v['mondes']})"
noms = {"nul_aucun_signal-faible": "nul sans aucun signal", "nul_presence_consigne-faible": "nul « présence d'une consigne », égale dans la consigne neutre et le bras gonflé (aire 0,70 contre l'honnête)",
        "nul_longueur_seule-faible": "nul « décalage de longueur seul » (sonde à queue lourde)",
        "alt_0.55-faible": "aire vraie 0,55, dose basse", "alt_0.60-faible": "aire vraie 0,60, dose basse", "alt_0.60-porte": "aire vraie 0,60, dose de la porte",
        "alt_0.65-faible": "aire vraie 0,65, dose basse", "alt_0.65-porte": "aire vraie 0,65, dose de la porte",
        "alt_0.70-faible": "aire vraie 0,70, dose basse", "alt_0.70-porte": "aire vraie 0,70, dose de la porte"}
lignes = " ; ".join(f"{noms[k]} : {cellule(k)}" for k in noms if k in r)
nuls = {k: r[k] for k in r if k.startswith("nul_")}
borne = max(v["ic95_ecrite"][1] for v in nuls.values()) if nuls else float("nan")
pire = max(v["tenue_regle_ecrite"] for v in nuls.values()) if nuls else float("nan")
verdict_nuls = (f"**non** sous les trois nuls simulés (taux observé {fr(pire)} ; borne haute à 95 % : {fr(borne, 3)}) ; **non borné** sous le nul « rejet inégal » "
                f"(taux de l'alternative de même aire induite : {fr(r['alt_0.60-faible']['tenue_regle_ecrite'])} à 0,60, {fr(r['alt_0.65-faible']['tenue_regle_ecrite'])} à 0,65, dose basse)")
g = (D / "scripts/gabarit_rendu_lecteur_A_v1.md").read_text(encoding="utf-8")
rempl = {
    "@@h_t1@@": h("scripts/t1_temoins.py", "sorties/t1-temoins.json"),
    "@@h_t2@@": h("scripts/t2a_validateur_prereg.py", "sorties/t2a-validateur-prereg.json", "scripts/t2b_rangs_tirage.py", "sorties/t2b-rangs-tirage.json", "scripts/t2c_oracles.py", "sorties/t2c-oracles.json"),
    "@@h_e0@@": h("scripts/e0_controle_pieces.py", "sorties/e0-controle-pieces.json", "scripts/e0_complement.py", "sorties/e0-complement.json"),
    "@@h_e1@@": h("scripts/validateur_c_furtif.py", "scripts/e1_acceptation.py", "sorties/e1-acceptation.json", "sorties/e1-actions.jsonl", "scripts/e1_arret.py", "sorties/e1-arret.json"),
    "@@h_e1b@@": h("scripts/e1bis_lecteur_du_texte.py", "sorties/e1bis-lecteur-du-texte.json", "scripts/e1bis_contre_consigne_neutre.py", "sorties/e1bis-contre-consigne-neutre.json",
                   "scripts/e1ter_rappel_episode.py", "sorties/e1ter-rappel-episode.json", "scripts/e1quater_validateur_minimal.py", "sorties/e1quater-validateur-minimal.json"),
    "@@h_e2@@": h("scripts/e2_enumeration.py", "sorties/e2-enumeration.json", "scripts/e2_monde_plante.py", "scripts/e2_lancer_v2.sh", "scripts/e2_lancer_v3.sh", "sorties/e2-mondes.jsonl", "scripts/e2_resume.py", "sorties/e2-resume.json"),
    "@@e2_lignes@@": lignes, "@@e2_nuls_verdict@@": verdict_nuls,
    "@@p65_porte_ecrite@@": fr(r["alt_0.65-porte"]["tenue_regle_ecrite"]), "@@p65_porte_variante@@": fr(r["alt_0.65-porte"]["tenue_variante_sans_cout"]),
}
for k, v in rempl.items():
    assert k in g, k
    g = g.replace(k, v)
assert "@@" not in g, [x for x in g.split("@@")[1::2]][:5]
sortie = D / "rendu-lecteur-A-v1.md"
sortie.write_text(g, encoding="utf-8")
(D / "rendu-lecteur-A-v1.md.sha256").write_text(f"{sha(sortie)}  rendu-lecteur-A-v1.md\n", encoding="utf-8")
fichiers = sorted(p for p in glob.glob(str(D / "scripts/*")) + glob.glob(str(D / "sorties/*")) if os.path.isfile(p) and "__pycache__" not in p)
(D / "empreintes-lecteur-A-v1.txt").write_text("".join(f"{sha(p)}  {os.path.relpath(p, D)}\n" for p in fichiers) + f"{sha(sortie)}  rendu-lecteur-A-v1.md\n", encoding="utf-8")
print("rendu :", sortie, sha(sortie)); print("mots :", len(g.split()))
print(lignes); print(verdict_nuls)
