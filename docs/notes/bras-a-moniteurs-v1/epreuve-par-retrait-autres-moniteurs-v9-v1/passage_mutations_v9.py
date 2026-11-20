"""Passage de mutations (épreuve par retrait) du module des autres moniteurs, version 9 : chaque garde neuve ou changée
de la v9, et le code de l'échange par paire et ses deux gardes (demande 24 a du lecteur habilité), est retirée seule ;
les essais qui la visent sont joués ; la mutation « mord » si un essai échoue. Le module est remis à l'identique après
chaque mutation, empreinte vérifiée ; un arrêt laisse le fichier d'origine en place (finally).

    python -B passage_mutations_v9.py <racine> <fichier de résultats>
"""
import hashlib
import subprocess
import sys
from pathlib import Path

RACINE = Path(sys.argv[1])
SORTIE = Path(sys.argv[2])
MODULE = RACINE / "src/controle_ia/organismes_discrets/bras_a_v2_habilite/autres_moniteurs_v9.py"
ESSAIS = "tests/test_bras_a_v2_habilite_autres_moniteurs_v9.py"
PYTHON = "/home/user/controle-ia-travail/.venv/bin/python"

M = [
    # cas C, D, E et cas B des comptes
    ("C : aire rendue", 'r.update({"aire": float(a["aire"]), "pli0": float(a["pli0"]), "pli1": float(a["pli1"])})\n        raise NonCalculable',
     'pass\n        raise NonCalculable', "plus_de_un_pour_cent"),
    ("D et E : lecture gardée", 'r.update({"calculable": True, "motif": str(e)})\n        return r', 'raise',
     "tirages_degeneres_de_la_borne or cas_e or illisible"),
    ("motif neutre : matrices", 'raise NonCalculable(f"pli {k} : {NON_AJUSTABLE}") from None', 'raise', "vocabulaire"),
    ("motif neutre : ajustement", "f\"{MOTIF_CLASSE_ABSENTE if m['motif'] == MOTIF_CLASSE_ABSENTE else NON_AJUSTABLE}\"",
     "f\"{m['motif']}\"", "neutres"),
    ("liste fermée des motifs", 'raise GardeArret("lecture : motif hors de la liste fermée : rien d\'autre ne sort")',
     'return "A"', "liste_fermee"),
    ("motif du cas des comptes", 'if cas_du_motif(r["motif"]) != cas:', 'if False:', "liste_fermee"),
    ("nombres rendus et nuls", 'if (r[c] is not None) != (c in rendus):', 'if False:', "liste_fermee"),
    ("aire dans [0, 1]", 'if c in rendus and not (isinstance(r[c], float) and 0.0 <= r[c] <= 1.0):', 'if False:',
     "liste_fermee"),
    ("borne au seul cas A",
     'if (r["borne_haute"] is not None, r["quantile_borne_haute"] is not None) != (cas == "A", cas == "A"):', 'if False:',
     "liste_fermee"),
    ("forme de la borne", 'if cas == "A" and not (isinstance(r["borne_haute"], float)', 'if False and (isinstance(r["borne_haute"], float)',
     "liste_fermee"),
    ("tirages hors des cas A et D", 'if (cas in "BC") != (r["tirages"] is None and r["tirages_degeneres"] is None) and cas != "E":',
     'if False:', "liste_fermee"),
    ("calculable du cas", 'if r["calculable"] is not (cas in "ADE"):', 'if False:', "liste_fermee"),
    ("famille à 1 aux cas B et C", 'if r["valeur_p_pour_la_famille"] != 1.0:', 'if False:', "liste_fermee"),
    ("quotients exacts", 'if not (_entier(au) and r["valeur_p_bas"] == (1 + au) / (1 + n - perdues)',
     'if False and (_entier(au) and r["valeur_p_bas"] == (1 + au) / (1 + n - perdues)', "liste_fermee"),
    ("comptes du motif C", 'if cas == "C" and nombres', 'if False and nombres', "liste_fermee"),
    ("comptes du motif D", 'if cas == "D" and nombres', 'if False and nombres', "liste_fermee"),
    ("format des comptes de permutations", 'if not (_entier(n) and n >= 1 and _entier(perdues) and perdues <= n):',
     'if False:', "liste_fermee"),
    ("format des comptes de tirages", 'if not (_entier(t) and _entier(deg) and t + deg >= 1):', 'if False:',
     "liste_fermee"),
    # sortie
    ("clés de la sortie", 'if not isinstance(sortie, dict) or tuple(sortie) != CLES_SORTIE:', 'if False:',
     "sortie_construite"),
    ("plis de la sortie", 'if not (isinstance(plis, dict) and len(plis) == 16', 'if False and (isinstance(plis, dict) and len(plis) == 16',
     "sortie_construite"),
    ("réglages de la sortie", 'if not (isinstance(g, dict) and tuple(g) == CLES_REGLAGES',
     'if False and (isinstance(g, dict) and tuple(g) == CLES_REGLAGES', "sortie_construite"),
    ("lectures en table", 'if not (isinstance(lectures, dict) and tuple(lectures) == DOSES',
     'if False and (isinstance(lectures, dict) and tuple(lectures) == DOSES', "sortie_construite"),
    ("lecture rangée sous son moniteur", 'if (r["moniteur"], r["dose"]) != (m, d):', 'if False:', "sortie_construite"),
    ("comptes ≠ réglages", 'if r["n_permutations"] not in (None, g["n_permutations"]) or (', 'if False and (',
     "sortie_construite"),
    ("effectifs entiers", 'if not (r["effectifs"] is None or _que_des_entiers(r["effectifs"])):', 'if False:',
     "sortie_construite"),
    ("champs de l'agrégateur", 'if not (isinstance(v, dict) and tuple(v) == DOSES',
     'if False and (isinstance(v, dict) and tuple(v) == DOSES', "sortie_construite"),
    ("piece_source", 'if not (isinstance(p, dict) and set(p) == {"sha256", "production"}',
     'if False and (isinstance(p, dict) and set(p) == {"sha256", "production"}', "sortie_construite"),
    ("programmes dans la sortie", '    for programmes in p["production"].values():\n        exiger_programmes(programmes)\n',
     '', "sortie_construite"),
    ("exclues entières", 'if not (isinstance(sortie["exclues"], dict)', 'if False and (isinstance(sortie["exclues"], dict)',
     "sortie_construite"),
    ("scores_par_unite", 'if not (isinstance(u, dict) and set(u)', 'if False and (isinstance(u, dict) and set(u)',
     "sortie_construite"),
    ("preuve d'ordre", 'if not (isinstance(sortie["preuve_d_ordre"], dict)', 'if False and (isinstance(sortie["preuve_d_ordre"], dict)',
     "sortie_construite"),
    ("comptes des lectures", 'if not (isinstance(sortie["comptes_des_lectures"], dict)',
     'if False and (isinstance(sortie["comptes_des_lectures"], dict)', "sortie_construite"),
    ("nombres rendus", 'if sortie["nombres_rendus"] != list(NOMBRES_RENDUS):', 'if False:', "sortie_construite"),
    ("aucun chemin en clair", 'if any(x in texte for x in (".py", "src/", "scripts/")):', 'if False:',
     "sortie_construite"),
    ("empreinte du module", '"piece_source": {"sha256": empreinte_du_module(),', '"piece_source": {"sha256": "0" * 64,',
     "sortie_construite"),
    ("sortie : on n'écrase jamais", '    chemin = Path(dossier) / FICHIER_SORTIE\n    if chemin.exists() or Path(str(chemin) + ".sha256").exists():',
     '    chemin = Path(dossier) / FICHIER_SORTIE\n    if False:', "sortie_construite"),
    ("sortie : garde avant écriture", '    exiger_sortie(sortie)\n    chemin = Path(dossier) / FICHIER_SORTIE',
     '    chemin = Path(dossier) / FICHIER_SORTIE', "sortie_construite"),
    ("sortie : relecture", 'if json.loads(texte) != sortie:', 'if False:', "sortie_construite"),
    ("dossiers disjoints", 'if d == s or s in d.parents or d in s.parents:', 'if False:',
     "test_dossiers_disjoints or non_disjoint"),
    ("appel des dossiers disjoints", '    exiger_dossiers_disjoints(dossier_de_la_sortie, {',
     '    (lambda *a: None)(dossier_de_la_sortie, {', "non_disjoint"),
    ("sortie déjà présente avant calcul", 'if (Path(dossier_de_la_sortie) / FICHIER_SORTIE).exists():', 'if False:',
     "non_disjoint"),
    ("statistique de la lecture commune", 'if statistique_agregateur not in STATISTIQUES_EPISODE:', 'if False:',
     "non_disjoint"),
    ("statistique de l'agrégateur, sensibilité", 'if retenue not in STATISTIQUES_EPISODE:', 'if False:',
     "autres_statistiques"),
    ("somme et maximum toujours", 'for statistique in STATISTIQUES_RAPPORTEES:',
     'for statistique in [s for s in STATISTIQUES_EPISODE if s != retenue]:', "autres_statistiques"),
    # provenance de la production
    ("programme à son empreinte", 'if vue != inscrite:', 'if False:', "programmes_de_production"),
    ("programme présent", 'if not p.is_file():\n            raise GardeArret(f"programme de production', 'if False:\n            raise GardeArret(f"programme de production',
     "programmes_de_production"),
    ("programmes au manifeste lu", '    exiger_programmes(m["programmes"])\n', '', "programmes_de_production"),
    ("clé des programmes au manifeste", '"empreinte_des_scores", "engagement_de_la_table", "programmes"} or \\',
     '"empreinte_des_scores", "engagement_de_la_table", "programmes"} and False or \\', "programmes_de_production"),
    ("programmes de la garde", 'if not isinstance(programmes, dict) or programmes != {n: s for n, (_, s) in PROGRAMMES_DE_PRODUCTION.items()}:',
     'if False:', "programmes_de_production"),
    # échange par paire et ses deux gardes (demande 24 a)
    ("échange : chance sur deux", 'if len(paire) == 2 and rng.random() < 0.5:', 'if len(paire) == 2 and rng.random() < 0.0:',
     "echange_par_paire_structure"),
    ("échange : inversion des deux", 'y[g] = 1 - pp[k]["y"][g]', 'y[g] = pp[k]["y"][g]', "echange_par_paire_structure"),
    ("échange : paires par rang", 'rangs.setdefault(int(u["episode"]), {})', 'rangs.setdefault((int(u["episode"]), u["condition"]), {})',
     "echange_par_paire_structure"),
    ("échange : appel de la garde de la paire", '        if permutation == PERMUTATION_PAR_PAIRE:\n            exiger_etiquettes_par_paire(y, pp[k])',
     '        if False:\n            exiger_etiquettes_par_paire(y, pp[k])', "gardes_de_l_echange"),
    ("garde de la paire : trois épisodes", 'if len(paire) > 2:', 'if False:', "gardes_de_l_echange"),
    ("garde de la paire : une de chaque sorte", 'if len(paire) == 2 and {int(y[g[0]]) for g in paire} != {0, 1}:', 'if False:',
     "echange_par_paire_structure"),
    ("garde de la paire : épisode sans pair", 'if len(paire) == 1 and int(y[paire[0][0]]) != int(pp_k["y"][paire[0][0]]):',
     'if False:', "gardes_de_l_echange"),
    ("garde par épisode : appel", '        exiger_etiquettes_par_episode(y, pp[k])\n        if permutation', '        if permutation',
     "garde_de_la_permutation"),
    ("permutation en clair", 'if not isinstance(permutation, str) or permutation not in PERMUTATIONS:', 'if False:',
     "permutation_exigee"),
]


def main():
    original = MODULE.read_bytes()
    empreinte = hashlib.sha256(original).hexdigest()
    texte = original.decode("utf-8")
    lignes = []
    try:
        for nom, avant, apres, k in M:
            n = texte.count(avant)
            if n != 1:
                lignes.append(f"| {nom} | texte de la mutation trouvé {n} fois | — | non jouée |")
                continue
            MODULE.write_text(texte.replace(avant, apres), encoding="utf-8")
            p = subprocess.run([PYTHON, "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", ESSAIS, "-k", k],
                               cwd=RACINE, env={"PYTHONPATH": "src", "PATH": "/usr/bin:/bin"}, capture_output=True,
                               text=True, timeout=1200)
            derniere = (p.stdout.strip().splitlines() or ["?"])[-1]
            lignes.append(f"| {nom} | `{k}` | {derniere} | {'mord' if p.returncode != 0 else 'NE MORD PAS'} |")
            MODULE.write_bytes(original)
            print(lignes[-1], flush=True)
    finally:
        MODULE.write_bytes(original)
    assert hashlib.sha256(MODULE.read_bytes()).hexdigest() == empreinte
    SORTIE.write_text(f"module {empreinte}\n\n| garde retirée | essais joués | dernière ligne | issue |\n|---|---|---|---|\n"
                      + "\n".join(lignes) + "\n", encoding="utf-8")


main()
