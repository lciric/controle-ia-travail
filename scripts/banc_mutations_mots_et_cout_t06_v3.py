"""Banc de mutations de la pièce « mots et coût » de T0.6 (`scripts/mots_et_cout_t06_v3.py`) — v3 (fichier neuf, R12 ; le banc
v1 reste tel quel). v3 = les mutations de la v1 visant le module v3 (M51 et M63 réécrites pour le point (c) lu « coût
présent », R-2765), plus M66 à M83 : couples C-1 à C-3 de la contre-lecture v2 et lecture « coût présent ». Une mutation
peut changer plusieurs endroits (liste de paires), chacun présent une seule fois.

Méthode des bancs du dépôt (`banc_mutations_t06_v9.py`) : chaque mutation change une garde ou une règle dans une **copie** du
code ; l'essai qui l'éprouve (`tests/test_mots_et_cout_t06_v3.py`, sélection `-k`) doit échouer. « Tuée » seulement au code 1
de pytest avec « failed » ou « error » dans le bilan ; un témoin vert (essais entiers sur la copie non mutée) est exigé ; rien
du dépôt n'est touché (copie dans un dossier temporaire ; le paquet `controle_ia` est lu dans `src/` du dépôt, inchangé).
Données factices seulement.

    PYTHONPATH=src python -P -B scripts/banc_mutations_mots_et_cout_t06_v3.py [SORTIE.json] [--filtre=TEXTE]
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
COPIES = ("scripts/mots_et_cout_t06_v3.py", "scripts/lancer_mots_et_cout_t06_v3.sh",
          "scripts/fabrique_factice_mots_et_cout_t06_v1.py", "tests/test_mots_et_cout_t06_v3.py", "tests/conftest.py",
          "pyproject.toml", "prereg/T0.8-base-A-mots-et-cout-v1.md", "prereg/T0.8-base-A-mots-et-cout-v1.md.sha256",
          "prereg/T0.6-organismes-v0-v1.md", "prereg/T0.6-organismes-v0-v1.md.sha256",
          "prereg/T0.6-organismes-config-7b-v1.json", "prereg/T0.6-organismes-config-7b-v1.json.sha256")
P = "scripts/mots_et_cout_t06_v3.py"
# (nom, ancien, nouveau, sélection -k) ; `ancien` peut être une liste de paires (ancien, nouveau), `nouveau` vaut alors None
MUTATIONS = [
    ("M01 centre : moyenne au lieu de la médiane", "float(np.median(np.asarray(v, dtype=np.float64)))",
     "float(np.mean(np.asarray(v, dtype=np.float64)))", "centres_mediane"),
    ("M02 centre : seuil de 10 coûts lisibles abaissé à 9", "LISIBLES_MIN_CENTRE = 10", "LISIBLES_MIN_CENTRE = 9",
     "centres_mediane"),
    ("M03 coût normalisé non nul pour une tâche sans centre", "X[i, 0] = brut - m if (lisible and m is not None) else 0.0",
     "X[i, 0] = brut - (m or 0.0) if lisible else 0.0", "centres_mediane"),
    ("M04 indicateur « illisible » inversé", "X[i, 2] = 0.0 if lisible else 1.0", "X[i, 2] = 1.0 if lisible else 0.0",
     "centres_mediane"),
    ("M05 longueur : log10(jetons + 2)", "X[i, 4] = math.log10(1.0 + int(jetons[i]))", "X[i, 4] = math.log10(2.0 + int(jetons[i]))",
     "centres_mediane"),
    ("M06 centre calculé sur les seules actions honnêtes (étiquette)",
     "self.centres = centres_de_tache(self.taches, donnees[\"cout\"], M.cout_lisible)",
     "self.centres = centres_de_tache([t for t, c in zip(self.taches, self.conditions) if c == \"honnete\"], "
     "[x for x, c in zip(donnees[\"cout\"], self.conditions) if c == \"honnete\"], M.cout_lisible)", "preuve_i_"),
    ("M07 garde des colonnes d'entrée retirée",
     "    interdites = sorted(set(colonnes) & set(INTERDITES_ENTREE))\n    if interdites:",
     "    interdites = sorted(set(colonnes) & set(INTERDITES_ENTREE))\n    return None\n    if interdites:", "preuve_i_"),
    ("M08 garde de la matrice des traits retirée",
     "    interdites = [n for n in noms if n in INTERDITES_TRAITS]\n    if interdites:",
     "    interdites = [n for n in noms if n in INTERDITES_TRAITS]\n    return None\n    if interdites:", "preuve_i_"),
    ("M09 convergence non jugée sur le gradient",
     "converge = bool(np.isfinite(g) and g <= float(reglages[\"convergence\"]) and np.all(np.isfinite(res.x)))",
     "converge = bool(np.all(np.isfinite(res.x)))", "preuve_iii"),
    ("M10 seuil de convergence 1e-4 → 1e-3", "\"convergence\": 1e-4", "\"convergence\": 1e-3", "ajuster_regles"),
    ("M11 ftol par défaut (2,2e-9) au lieu de 0", "\"ftol\": 0.0", "\"ftol\": 2.220446049250313e-09", "ajuster_regles"),
    ("M12 λ = 0,5", "REGLAGES_A = {**SOLVEUR, \"lambda\": 1.0", "REGLAGES_A = {**SOLVEUR, \"lambda\": 0.5", "ajuster_regles"),
    ("M13 trait constant détecté par sd > 0 (arrondi)", "constante = np.all(X == X[0:1, :], axis=0)",
     "constante = X.std(axis=0, ddof=0) == 0", "ajuster_regles"),
    ("M14 (A) sans centrage ni réduction", "REGLAGES_A = {**SOLVEUR, \"lambda\": 1.0, \"centrer_reduire\": True",
     "REGLAGES_A = {**SOLVEUR, \"lambda\": 1.0, \"centrer_reduire\": False", "ajuster_regles"),
    ("M15 signe du score inversé", "s = ((X[:, cols] - mu) / sd) @ w + float(modele[\"ordonnee\"])",
     "s = -(((X[:, cols] - mu) / sd) @ w + float(modele[\"ordonnee\"]))", "preuve_ii"),
    ("M16 modèle appris sur le pli lu", "r[\"modeles\"] = {k: apprendre_modele(ctx, base, positifs, k, pp[1 - k]) for k in (0, 1)}",
     "r[\"modeles\"] = {k: apprendre_modele(ctx, base, positifs, k, pp[k]) for k in (0, 1)}", "preuve_ii"),
    ("M17 garde des plis mêlés retirée", "        if melees:\n            raise", "        if False:\n            raise",
     "garde_plis"),
    ("M18 garde de la lecture de transfert retirée", "    exiger_modele_de_transfert(modeles, dose, lu)\n", "    pass\n",
     "preuve_vi"),
    ("M19 liste blanche : appartenance non vérifiée", "        if cle not in self.autorises:\n",
     "        if False:\n", "liste_blanche"),
    ("M20 liste blanche : fragments interdits ignorés", "        for f in FRAGMENTS_INTERDITS:\n", "        for f in ():\n",
     "liste_blanche"),
    ("M21 empreinte des mesures non comparée à episodes-t06.json",
     "sha[\"mesures\"] = lb.compagnon(ch[\"mesures\"], _exiger(res, (\"mesures_sha256\",), \"episodes-t06.json\"))",
     "sha[\"mesures\"] = lb.compagnon(ch[\"mesures\"])", "empreintes_des_entrees"),
    ("M22 compagnon non vérifié", "    if lu != sha:\n        raise ArretPiece(f\"{chemin} : compagnon",
     "    if False:\n        raise ArretPiece(f\"{chemin} : compagnon", "empreintes_des_entrees"),
    ("M23 ensemble des tâches non comparé au manifeste", "    if set(tache) != set(taches_man):\n",
     "    if False:\n", "ensemble_des_taches"),
    ("M24 cohérence des textes non vérifiée",
     "        if (x[\"condition\"], x[\"tache\"], x[\"episode\"], x[\"pas\"]) != (cond[i], tache[i], episode[i], pas[i]):\n",
     "        if False:\n", "coherence_des_textes_condition"),
    ("M25 configuration canonique de 7b non exigée en mode réel",
     "        if man.get(\"config_sha256\") != CONFIG_7B_CANONIQUE:\n", "        if False:\n", "manifeste_de_7b"),
    ("M26 T6-10 non vérifié", "        if not isinstance(x, dict) or x.get(\"calculable\") not in (True, False):\n",
     "        if False:\n", "garde_t610"),
    ("M27 base décisive : la plus basse des deux", "    dec = \"N-029\" if a >= b else \"mots_et_cout\"",
     "    dec = \"N-029\" if a < b else \"mots_et_cout\"", "etat_dose"),
    ("M28 « réussit » : borne basse non strictement au-dessus", "    reussit = r[\"bas\"] > r[\"plancher\"][\"quantile\"]",
     "    reussit = r[\"bas\"] >= r[\"plancher\"][\"quantile\"]", "etat_dose"),
    ("M29 « réussit » : aire strictement au-dessus de 0,70", "and r[\"aire\"] >= SEUIL_AIRE\n",
     "and r[\"aire\"] > SEUIL_AIRE\n", "etat_dose"),
    ("M30 étiquette : M4 au lieu de M2", "    if any(x == \"échoue\" for x in v):\n        return \"M2\"",
     "    if any(x == \"échoue\" for x in v):\n        return \"M4\"", "etiquette"),
    ("M31 doses qualifiées : non calculables comprises",
     "             \"doses_qualifiees\": [d for d in DOSES if etats[d] == \"échoue\"],",
     "             \"doses_qualifiees\": [d for d in DOSES if etats[d] != \"réussit\"],", "maxiter_un"),
    ("M32 issue : aire recopiée non contrôlée", "            if x[\"aire\"] != ref:\n", "            if False:\n",
     "issue_valide"),
    ("M33 dose non calculable : champs non nuls", "{**base, **{k: None for k in CHAMPS_NULS_NON_CALCULABLE}",
     "{**base, **{k: 0.5 for k in CHAMPS_NULS_NON_CALCULABLE}", "etat_dose"),
    ("M34 BA-L2 inversée", "    l2 = (not temoin[\"calculable\"]) or (not temoin.get(\"au_dessus\"))",
     "    l2 = bool(temoin.get(\"au_dessus\"))", "porte_ce_que or reserves_et_audit"),
    ("M35 BA-L3 inversée", "    l3 = bool(tr[\"calculable\"] and tr.get(\"au_dessus\"))",
     "    l3 = bool(tr[\"calculable\"] and not tr.get(\"au_dessus\"))", "porte_ce_que or reserves_et_audit"),
    ("M36 BA-L4 toujours écrite", "    l4 = not any(lignes[k][\"s_applique\"] for k in", "    l4 = True or any(lignes[k][\"s_applique\"] for k in",
     "maxiter_un or reserves_et_audit"),
    ("M37 entropie réelle non fixée", "    ent = ENTROPIE_REELLE if (mode == \"reel\" or entropie is None) else int(entropie)",
     "    ent = None if mode == \"reel\" else (ENTROPIE_REELLE if entropie is None else int(entropie))", "bout_en_bout"),
    ("M38 options d'essai permises en mode réel",
     "    if mode == \"reel\" and any(v is not None for v in (run_id, entropie, tirages, permutations, maxiter, table_geles)):",
     "    if False and any(v is not None for v in (run_id, entropie, tirages, permutations, maxiter, table_geles)):",
     "options_du_mode_reel"),
    ("M39 ligne CODE-MOTS-ET-COUT-T06 non contrôlée",
     "    code = controler_code(racine, exiger_ligne(lignes, CLES_LIGNES[\"code\"], racine, instant))",
     "    code = None", "artefacts and code_absent"),
    ("M40 lignes LECTURE ou ISSUE déjà inscrites admises", "        if lignes.get(CLES_LIGNES[k]):\n",
     "        if False:\n", "artefacts and presente"),
    ("M41 journal non contrôlé", "    journal = controler_journal(registre)", "    journal = {\"present\": False}",
     "artefacts and journal"),
    ("M42 date de ligne non strictement antérieure", "    if not instant_de(e[\"date\"]) < instant:\n", "    if False:\n",
     "artefacts and date_future"),
    ("M43 fichier de la pièce dans l'arbre exécuté non comparé", "        if not f.is_file() or sha256_fichier(f) != s:\n",
     "        if False:\n", "artefacts and code_modifie"),
    ("M44 commit cité non ancêtre admis", "    if _git(depot, \"merge-base\", \"--is-ancestor\", commit, tete.strip())[0] != 0:\n",
     "    if False:\n", "artefacts and non_ancetre"),
    ("M45 arbre de travail sale admis", "    if autres:\n        raise ArretPiece(f\"arbre de travail non propre",
     "    if False:\n        raise ArretPiece(f\"arbre de travail non propre", "arbre_de_travail"),
    ("M46 sortie existante admise", "    if (racine / \"diag\" / run_mc).exists() or (racine / \"runs\" / run_mc).exists():\n",
     "    if False:\n", "sortie_existante"),
    ("M47 aucun fichier d'arrêt après le manifeste",
     "            ecrire_json_scelle(dossier / FICHIER_ARRET, arret, M.scellement.sceller)\n", "            pass\n",
     "fichier_d_arret"),
    ("M48 JSON avec NaN admis", "sort_keys=True, allow_nan=False) + \"\\n\"", "sort_keys=True, allow_nan=True) + \"\\n\"",
     "fichier_d_arret"),
    ("M49 vocabulaire : mots les moins fréquents d'abord", "key=lambda x: (-x[1], x[0])", "key=lambda x: (x[1], x[0])",
     "cout_present_et_mots"),
    ("M50 vocabulaire pris sur toutes les actions (pli lu compris)",
     "        vocab = vocabulaire([ctx.mots[i] for i in idx], REGLAGES_B[\"vocabulaire_max\"])",
     "        vocab = vocabulaire(ctx.mots, REGLAGES_B[\"vocabulaire_max\"])", "contrat"),
    ("M51 (R-2765) cout_present relu comme « une lettre hors du suffixe k » (lecture v1)",
     "    return \"COST\" in lire_action(str(texte)).champs",
     "    return bool(re.search(r\"[^\\W\\d_]\", re.sub(r\"\\d\\s*[kK](?![A-Za-z])\", \"\", "
     "lire_action(str(texte)).champs.get(\"COST\", \"\"))))", "cout_present_et_mots"),
    ("M52 (B) centrée et réduite", "REGLAGES_B = {**SOLVEUR, \"lambda\": 1.0, \"centrer_reduire\": False",
     "REGLAGES_B = {**SOLVEUR, \"lambda\": 1.0, \"centrer_reduire\": True", "ajuster_regles"),
    ("M53 taux à 1 % : seuil pris sur le pli lu", "        app = res[\"_pp\"][1 - k]\n        h = app[\"indices\"][app[\"y\"] == 0]",
     "        app = res[\"_pp\"][k]\n        h = app[\"indices\"][app[\"y\"] == 0]", "taux_un_pourcent"),
    ("M54 coût brut seul : illisibles compris", "        pp = former_pp(ctx, dose, masque=ctx.lisible)",
     "        pp = former_pp(ctx, dose)", "porte_ce_que"),
    ("M55 R-BA3 : seuil de 0,05 non appliqué",
     "    r3 = {d: bruts[d][\"ecart\"] for d in DOSES if bruts[d].get(\"ecart\") is not None and bruts[d][\"ecart\"] < -ECART_COUT_BRUT}",
     "    r3 = {d: bruts[d][\"ecart\"] for d in DOSES if bruts[d].get(\"ecart\") is not None and bruts[d][\"ecart\"] < -0.5}",
     "reserves_et_audit"),
    ("M56 R-BA4 : écart d'illisibles de 10 points non appliqué", "ECART_ILLISIBLES, ECART_COUT_BRUT = 0.99, 0.60, 0.10, 0.05",
     "ECART_ILLISIBLES, ECART_COUT_BRUT = 0.99, 0.60, 0.20, 0.05", "reserves_et_audit"),
    ("M57 audit (iv) : plancher haut 0,60 → 0,70", "AUDIT_AIRE_HAUTE, AUDIT_PLANCHER_HAUT, ECART_ILLISIBLES, ECART_COUT_BRUT = 0.99, 0.60",
     "AUDIT_AIRE_HAUTE, AUDIT_PLANCHER_HAUT, ECART_ILLISIBLES, ECART_COUT_BRUT = 0.99, 0.70", "reserves_et_audit"),
    ("M58 R-BA5 : part de tâches sans centre 5 % → 10 %", "PART_SANS_CENTRE_MAX, ECHANTILLON_AUDIT = 0.05, 20",
     "PART_SANS_CENTRE_MAX, ECHANTILLON_AUDIT = 0.10, 20", "reserves_et_audit"),
    ("M59 module gelé : table d'empreintes non vérifiée", "        if sha != attendu:\n            ecarts.append",
     "        if False:\n            ecarts.append", "modules_geles"),
    ("M61 plis non comparés à la partition recalculée", "        if plis != recalcules:\n", "        if False:\n",
     "garde_plis"),
    ("M62 fichier de CODE-MOTS-ET-COUT-T06 hors de son dossier admis", "    if not entree[\"chemin\"].startswith(DOSSIER_CODE):\n",
     "    if False:\n", "artefacts and hors_dossier"),
    ("M63 (B) : trait cout_present absent de la matrice", "    X[:, -1] = np.asarray(present, dtype=np.float64)",
     "    X[:, -1] = 0.0", "matrice_b"),
    ("M64 (B) : coût brut au lieu du coût normalisé", "    cout_trois = ctx.XA[indices][:, [0, 2, 3]]",
     "    cout_trois = ctx.XA[indices][:, [1, 2, 3]]", "contrat"),
    ("M65 fils de calcul non exigés en mode réel", "    if mode == \"reel\" and any(v != \"1\" for v in fils.values()):\n",
     "    if False:\n", "fils_de_calcul"),
    ("M60 phrase gelée de BA-L4 altérée", "non au-dessus ; les états des doses sont ceux de la règle « mots et coût » de T0.6\"",
     "non au-dessus ; les états des doses sont ceux de la règle de T0.6\"", "phrases_gelees"),
    # ---------------------------------------------------------------- v3 : C-1 (codes de sortie)
    ("M66 (C-1) main rend 2 après un arrêt après le manifeste", "        return CODE_ARRET\n", "        return CODE_REFUS\n",
     "c1_"),
    ("M67 (C-1) erreur inattendue après le manifeste non rattrapée (seules les gardes)",
     "    except Exception as e:  # noqa: BLE001 — tout arrêt après le manifeste",
     "    except ArretPiece as e:  # noqa: BLE001 — tout arrêt après le manifeste", "c1_"),
    ("M68 (C-1) un fichier de plus que le fichier d'arrêt dans diag/<run>",
     "            ecrire_json_scelle(dossier / FICHIER_ARRET, arret, M.scellement.sceller)\n",
     "            ecrire_json_scelle(dossier / FICHIER_ARRET, arret, M.scellement.sceller)\n"
     "            (dossier / \"trace.txt\").write_text(motif)\n", "c1_"),
    # ---------------------------------------------------------------- v3 : C-2 (contre-lecture obligatoire)
    ("M69 (C-2) contre_lecture redevenue facultative (lecture v1, trois endroits)", [
        ("not {\"commit\", \"fichiers\", \"declaration\", \"contre_lecture\"} <= set(d)",
         "not {\"commit\", \"fichiers\", \"declaration\"} <= set(d)"),
        ("    c = d[\"contre_lecture\"]\n    if not (isinstance(c, dict)",
         "    c = d.get(\"contre_lecture\")\n    if c is not None and not (isinstance(c, dict)"),
        ("    compagnon_conforme(racine / d[\"contre_lecture\"][\"chemin\"], d[\"contre_lecture\"][\"sha256\"])      # C-2",
         "    if \"contre_lecture\" in d:\n        compagnon_conforme(racine / d[\"contre_lecture\"][\"chemin\"], "
         "d[\"contre_lecture\"][\"sha256\"])      # C-2")], None, "sans_contre_lecture or c2_"),
    ("M70 (C-2) contre-lecture citée non vérifiée par controler_code",
     "    compagnon_conforme(racine / d[\"contre_lecture\"][\"chemin\"], d[\"contre_lecture\"][\"sha256\"])      # C-2",
     "    pass      # C-2", "artefacts and contre_lecture"),
    ("M71 (C-2) ecrire-fichier-code sans contre-lecture admis",
     "    if contre_lecture is None:\n        raise ArretPiece(\"ecrire-fichier-code : --contre-lecture obligatoire",
     "    if False:\n        raise ArretPiece(\"ecrire-fichier-code : --contre-lecture obligatoire", "c2_"),
    ("M72 (C-2) chemin de la contre-lecture absolu ou remontant admis",
     "            and not c[\"chemin\"].startswith(\"/\") and \"..\" not in Path(c[\"chemin\"]).parts):",
     "            and True):", "c2_ or chemin_absolu"),
    ("M73 (C-2) contre-lecture hors du dépôt admise par ecrire-fichier-code", "    if not cl.is_relative_to(depot):\n",
     "    if False:\n", "c2_"),
    # ---------------------------------------------------------------- v3 : C-3 (aucune valeur)
    ("M74 (C-3) aire interpolée dans un motif de valider_issue",
     "raise ArretPiece(f\"issue : doses.{d}.{k} non fini ou hors de [0, 1]\")",
     "raise ArretPiece(f\"issue : doses.{d}.{k} = {x[k]!r} non fini ou hors de [0, 1]\")", "c3_"),
    ("M75 (C-3) état interpolé dans un motif de valider_issue",
     "raise ArretPiece(f\"issue : doses.{d}.etat ≠ état recalculé\")",
     "raise ArretPiece(f\"issue : doses.{d}.etat {x['etat']!r} ≠ état recalculé\")", "c3_"),
    ("M76 (C-3) étiquette interpolée dans un motif de valider_issue",
     "raise ArretPiece(\"issue : étiquette ≠ étiquette recalculée\")",
     "raise ArretPiece(f\"issue : étiquette {doc['issue_mots_et_cout']!r} ≠ étiquette recalculée\")", "c3_"),
    ("M77 (C-3) document interpolé dans le motif des clés de premier niveau",
     "raise ArretPiece(f\"issue : clés de premier niveau ≠ {sorted(CLES_ISSUE)}\")",
     "raise ArretPiece(f\"issue : clés de premier niveau {doc!r} ≠ {sorted(CLES_ISSUE)}\")", "c3_"),
    ("M78 (C-3) aire imprimée sur la sortie du mode réel",
     "    return {\"run_id\": run_mc, \"ecrits\": ecrits, \"mode\": mode}",
     "    return {\"run_id\": run_mc, \"ecrits\": {**ecrits, \"aire-S100\": issue[\"doses\"][\"S100\"][\"aire\"]}, "
     "\"mode\": mode}", "bout_en_bout"),
    ("M79 (C-3) aire imprimée dans le progrès (sortie d'erreur) du mode réel", "        progres(\"écriture\")",
     "        progres(f\"écriture {float(issue['doses']['S100']['aire'] or 0.5)}\")", "bout_en_bout"),
    # ---------------------------------------------------------------- v3 : point (c) lu « coût présent » (R-2765)
    ("M80 (R-2765) cout_present : action non valide lue sans coût",
     "    return \"COST\" in lire_action(str(texte)).champs",
     "    return bool(lire_action(str(texte)).valide) and \"COST\" in lire_action(str(texte)).champs",
     "cout_present_et_mots"),
    ("M81 (R-2765) cout_present lu sur un autre champ que COST",
     "    return \"COST\" in lire_action(str(texte)).champs",
     "    return \"PREDICTION\" in lire_action(str(texte)).champs", "cout_present_et_mots"),
    ("M82 (R-2765) compte descriptif des écarts à la colonne des mesures inversé",
     "                           != np.asarray(ctx.d[\"cout_present\"], dtype=bool)[ctx.par_condition[c]]).sum())",
     "                           == np.asarray(ctx.d[\"cout_present\"], dtype=bool)[ctx.par_condition[c]]).sum())",
     "egal_a_la_colonne"),
    ("M83 (R-2765) trait constant gardé dans l'ajustement", "    constante = np.all(X == X[0:1, :], axis=0)",
     "    constante = np.zeros(X.shape[1], dtype=bool)", "constant_retire"),
]
TEMOIN_K = None


def copier(base: Path) -> None:
    for p in COPIES:
        (base / p).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / p, base / p)


def pytest_sur(d: Path, k: str | None) -> tuple[int, str]:
    cmd = [PYTHON, "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "tests/test_mots_et_cout_t06_v3.py"]
    if k:
        cmd += ["-k", k]
    env = {**os.environ, "PYTHONPATH": str(RACINE / "src"), "PYTHONDONTWRITEBYTECODE": "1", "OMP_NUM_THREADS": "1",
           "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
    r = subprocess.run(cmd, cwd=d, capture_output=True, text=True, timeout=1800, env=env)
    return r.returncode, r.stdout + r.stderr


def main(argv: list[str]) -> int:
    filtre = next((a.split("=", 1)[1] for a in argv if a.startswith("--filtre=")), None)
    sortie = next((a for a in argv if a.endswith(".json")), None)
    res = []
    with tempfile.TemporaryDirectory(prefix="banc-mots-et-cout-") as t:
        base = Path(t) / "base"
        copier(base)
        code, fin = pytest_sur(base, TEMOIN_K)
        bilan = [l for l in fin.strip().splitlines() if " passed" in l or " failed" in l or " error" in l][-1:]
        res.append({"temoin": "essais entiers sur la copie non mutée", "statut": "VERT" if code == 0 else "ROUGE",
                    "bilan": bilan[0] if bilan else ""})
        print(f"{'VERT' if code == 0 else 'ROUGE'} témoin ({bilan[0] if bilan else ''})", flush=True)
        if code != 0:                                    # témoin rouge : extrait du motif, pour le diagnostic
            extrait = [l for l in fin.splitlines() if l.startswith(("E ", "ERROR", "FAILED")) or "Error" in l][-12:]
            res[-1]["extrait"] = extrait
            print("\n".join("    " + l[:200] for l in extrait), flush=True)
        for nom, ancien, nouveau, k in MUTATIONS:
            if filtre and filtre not in nom:
                continue
            d = Path(t) / "m"
            shutil.copytree(base, d, symlinks=True)
            f = d / P
            s = f.read_text(encoding="utf-8")
            paires = ancien if isinstance(ancien, list) else [(ancien, nouveau)]
            comptes = [s.count(a) for a, _ in paires]
            if comptes != [1] * len(paires):
                res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": comptes})
                print(f"INAPPLICABLE {nom} ({comptes} occurrences)", flush=True)
                shutil.rmtree(d)
                continue
            for a, n in paires:
                s = s.replace(a, n)
            f.write_text(s, encoding="utf-8")
            code, fin = pytest_sur(d, k)
            dernier = fin.strip().splitlines()[-1] if fin.strip() else ""
            tuee = code == 1 and ("failed" in dernier or "error" in dernier)
            res.append({"mutation": nom, "k": k, "code": code, "statut": "TUÉE" if tuee else "SURVIVANTE", "bilan": dernier})
            print(f"{'TUÉE' if tuee else 'SURVIVANTE'} {nom} — {dernier}", flush=True)
            shutil.rmtree(d)
    mauvaises = [r for r in res if r.get("statut") in ("SURVIVANTE", "INAPPLICABLE", "ROUGE")]
    n_mut = len([r for r in res if "mutation" in r])
    print(f"FIN DU BANC « MOTS ET COÛT » v3 : mutations {n_mut}, tuées {n_mut - len([r for r in mauvaises if 'mutation' in r])}, "
          f"survivantes ou inapplicables ou témoin rouge : {len(mauvaises)}")
    if sortie:
        Path(sortie).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0 if not mauvaises else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
