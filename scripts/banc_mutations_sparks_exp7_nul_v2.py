"""Banc de mutations de SPARKS-EXP7-NUL pour l'addendum n° 1 : les 22 mutations du banc v1 (code v1, essais v1,
inchangés) et les mutations des gardes neuves (code v2, essais v2). Chaque mutation, seule, dans une copie jetable,
doit faire échouer au moins un essai ciblé ; témoins sans mutation verts. Rien n'est modifié dans l'arbre de travail.

    PYTHONPATH=src nice -n 10 python -I -B scripts/banc_mutations_sparks_exp7_nul_v2.py [SORTIE.json]
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
T1, T2 = "tests/test_sparks_exp7_nul_v1.py", "tests/test_sparks_exp7_nul_v2.py"
P = "src/controle_ia/sparks_exp7_nul_v2/"


def mutations_v1() -> list[tuple]:
    spec = importlib.util.spec_from_file_location("banc_v1", RACINE / "scripts" / "banc_mutations_sparks_exp7_nul_v1.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return [(f"v1 : {n}", f, a, b, k, T1) for n, f, a, b, k in m.MUTATIONS]


MUTATIONS_V2 = [
    ("B3 : orientation inversée", P + "bases.py", "o3 = -1 if aire < 0.5 else 1", "o3 = 1 if aire < 0.5 else -1", "orientations"),
    ("B4 : orientation figée à +1 (non choisie sur le test)", P + "bases.py", "o4 = 1 if a >= 0.5 else -1", "o4 = 1", "orientations or b4_orientee"),
    ("B3 : un tenseur manquant accepté", P + "bases.py", "        if nm != attendus:\n", "        if False:\n", "b3_b4_valeurs"),
    ("B3 : forme différente acceptée", P + "bases.py",
     "if k not in ref or tuple(np.shape(ref[k])) != tuple(np.shape(etat_m[k])):", "if k not in ref:", "b3_b4_valeurs"),
    ("départ non arrondi en bf16", P + "bases.py", "x0 = arrondi_bf16(np.asarray(etat_0[k], np.float32)).astype(np.float64)",
     "x0 = np.asarray(etat_0[k], np.float64) * 1.001", "b3_b4_valeurs"),
    ("+1 gardé sans jeton de début (positions)", P + "bases.py",
     'return 1 if getattr(tok, "bos_token_id", None) is not None else 0', "return 1", "positions"),
    ("préfixe ajouté sans jeton de début (outil)", P + "outil_attention.py",
     "return ([debut] if debut is not None else []) + ids", "return [debut] + ids", "positions"),
    ("incrément : condition G > 0 retirée", P + "analyse.py", "tenu = bool(G > 0 and lo > 0", "tenu = bool(lo > 0", "etats_de"),
    ("incrément : permutation seule", P + "analyse.py", "tenu = bool(G > 0 and lo > 0 and p_perm <= SEUIL_P_PERM)",
     "tenu = bool(p_perm <= SEUIL_P_PERM)", "etats_de"),
    ("incrément : préséance de « tenu » perdue", P + "analyse.py", "    if tenu:\n        return (",
     "    if tenu and hi >= APPORT_EXCLU:\n        return (", "etats_de"),
    ("incrément : rééchantillonnage par modèle", P + "analyse.py",
     "        i = rng_boot.integers(n, size=n)\n        boot.append(gain(P[i].ravel(), S[i].ravel(), Y[i].ravel()))",
     "        j = rng_boot.integers(2 * n, size=2 * n)\n        boot.append(gain(P.ravel()[j], S.ravel()[j], Y.ravel()[j]))",
     "reechantillonne"),
    ("incrément : rangs décroissants", P + "analyse.py", "return ((fin - cnt + 1 + fin) / 2)[inv]",
     "return (len(v) + 1 - (fin - cnt + 1 + fin) / 2)[inv]", "rangs_croissants"),
    ("incrément : égalités traitées par argsort", P + "analyse.py", "return ((fin - cnt + 1 + fin) / 2)[inv]",
     'return np.argsort(np.argsort(v, kind="stable")) + 1.0', "rangs_croissants"),
    ("composants invalides comptés comme échec", P + "analyse.py",
     'return r["statut"] not in ("repondu", "composants_invalides")', 'return r["statut"] != "repondu"', "analyse_complete"),
    ("composants invalides comptés dans les 10 %", P + "analyse.py", 'r.get("infraction") or r["statut"] == "invalide"',
     'r.get("infraction") or r["statut"] != "repondu"', "analyse_complete"),
    ("déclencheur G_b ≥ 0,20 retiré", P + "analyse.py", '            d.append(f"G_{b} ≥ 0,20")', "            pass", "declencheurs"),
    ("table : B4 ignorée dans « tient, au-delà »", P + "analyse.py", 'deux = all(inc[b]["tenu"] for b in ("B3", "B4"))',
     'deux = inc["B3"]["tenu"]', "table_de_lecture"),
    ("discordantes : égalité comptée bien ordonnée", P + "analyse.py", "if s3[s] <= s3[h]:", "if s3[s] < s3[h]:", "discordantes"),
    ("harnais : clé de trop dans un élément acceptée", P + "harnais.py", "        if set(c) - CLES_COMPOSANT:\n",
     "        if False:\n", "deux_temps"),
    ("harnais : clé de trop au niveau du bloc acceptée", P + "harnais.py",
     'if not {"p_A", "p_B"} <= set(obj) or set(obj) - {"p_A", "p_B", "composants"}:', 'if not {"p_A", "p_B"} <= set(obj):',
     "deux_temps"),
    ("harnais : pas de rappel pour les composants", P + "harnais.py", 'fautif = statut != "repondu"', "fautif = False",
     "composants_invalides_apres_rappel"),
    ("consigne : une phrase changée de plus admise", P + "consignes.py", "        if z != y:\n", "        if False:\n",
     "consigne_principale_v2"),
    ("consigne de secours : prélude porté non exigé", P + "consignes.py", "        if not prelude_porte:\n",
     "        if False:\n", "deriver_secours"),
    ("prélude : encodage non comparé", P + "consignes.py", "        if a != b:\n", "        if False:\n", "prelude_epreuve"),
    ("GO : lignes d'extension ignorées (première seule)", P + "go.py", "    for x in autres:", "    for x in []:", "go_sain"),
    ("GO : plafond resté à 25 USD", P + "go.py", "PLAFOND_USD = 40.0", "PLAFOND_USD = 25.0", "go_sain"),
    ("GO : extension non conforme acceptée", P + "go.py", 'if not (x["perimetre"].lower().startswith("extension") and ',
     "if not (", "go_artefacts"),
    ("dépense : projection « sans lots » dès le lancement", P + "depense.py",
     '        if eg is True:\n            h["causal"] = H_CAUSAL_LOTS', '        if eg is True:\n            h["causal"] = H_CAUSAL_SANS_LOTS',
     "depense_lancement"),
    ("dépense : plafond non appliqué", P + "depense.py", '"poursuite": proj <= PLAFOND_USD', '"poursuite": True', "depense_cas_sain"),
    ("dépense : facture ignorée", P + "depense.py", '        cumulee = max(cumulee, _nombre(etat, "facture_usd"))',
     "        pass", "depense_cumulee"),
    ("dépense : état d'égalité inconnu accepté", P + "depense.py",
     '            raise GardeDepense("état de l\'essai d\'égalité des lots inconnu : aucune projection (aucun repli)")',
     '            h["causal"] = H_CAUSAL_LOTS', "depense_lancement"),
    ("destruction : nœud du 16 novembre ignoré", P + "depense.py", "    if now >= NOEUD_DESTRUCTION:", "    if False:",
     "decision_instance"),
    ("liste fermée : fichier hors liste accepté", P + "garde_code.py", "    if hors or absents:", "    if absents:",
     "liste_fermee_saine"),
    ("liste fermée : suppression acceptée", P + "garde_code.py", 'if s not in ("A", "M")]', 'if s not in ("A", "M", "D")]',
     "liste_fermee_saine"),
    ("addendum : sceau non vérifié", P + "garde_code.py", "    if not m or m.group(1) != sha256_octets(texte.encode(\"utf-8\")):",
     "    if not m:", "lancement_addendum"),
    ("addendum : code changé après accepté", P + "garde_code.py", "    if touche:\n", "    if False:\n", "lancement_addendum"),
    ("coffre : scores écrits hors du coffre", P + "aveugle.py", '    if not (c / "cle-v1.json").is_file():', "    if False:",
     "bases_au_coffre"),
    ("coffre : seconde valeur acceptée", P + "aveugle.py", "        if tout[nom] != scores:\n", "        if False:\n", "bases_au_coffre"),
    ("coffre : bases non vérifiées à l'ouverture", P + "aveugle.py",
     "    if not f.is_file() or sha256_fichier(f) != sha256_bases:", "    if not f.is_file():", "bout_en_bout_jouet_v2"),
    ("service : B3 calculée avec la clé", P + "mise_a_disposition.py", "    d = Path(dossier_cas)\n",
     "    d = Path(dossier_cas)\n    (Path(coffre) / \"cle-v1.json\").read_text()\n", "sans_la_cle"),
    ("service : couches du départ non vérifiées", P + "mise_a_disposition.py",
     "    if aveugle.sha256_fichier(f) != sha_attendu:", "    if False:", "couches_du_depart"),
    ("service : lots de 4 sous 10 Go", P + "mise_a_disposition.py", "return LOT if octets_libres >= SEUIL_LIBRE else LOT_REDUIT",
     "return LOT", "lots_de_service"),
    ("lots inégaux acceptés", P + "comportement.py", "all(abs(mesure_a[k] - mesure_b[k]) <= tol for k in cles)",
     "all(True for k in cles)", "egalite_des_lots"),
    ("lots : réponse mal alignée", P + "comportement.py", "lp = torch.log_softmax(logits[j, len(p) - 1:len(p) + len(t) - 1], -1)",
     "lp = torch.log_softmax(logits[j, len(p):len(p) + len(t)], -1)", "mesure_par_lots"),
    ("causal : formes non contrôlées", P + "causal.py", "            if tuple(etat[n_].shape) != fo:\n", "            if False:\n",
     "verifier_noms"),
    ("causal : biais de q oublié pour une tête", P + "causal.py", '        if "q" in arch["biais"]:\n', "        if False:\n",
     "tranches_v2"),
    ("étape 0 : arrêt sur candidat inaccessible", P + "instance.py",
     "        except Exception as e:      # noqa: BLE001", "        except ZeroDivisionError as e:      # noqa: BLE001", "etape0"),
    ("bac : prélude non vérifié", P + "bac_a_sable.py", "    if hashlib.sha256(p.read_bytes()).hexdigest() != sha_prelude:",
     "    if False:", "bac_depart"),
]


def copier(dest: Path) -> None:
    shutil.copytree(RACINE / "src", dest / "src", ignore=shutil.ignore_patterns("__pycache__"))
    (dest / "tests").mkdir()
    for f in (T1, T2, "tests/conftest.py"):
        shutil.copy2(RACINE / f, dest / f)
    shutil.copy2(RACINE / "pyproject.toml", dest)
    shutil.copytree(RACINE / "docs/notes/sparks-exp7-nul-v1", dest / "docs/notes/sparks-exp7-nul-v1")
    for rel in ("prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md", "prereg/SPARKS-EXP7-NUL-preenregistrement-v1.md.sha256",
                "registres/go.md"):
        (dest / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(RACINE / rel, dest / rel)


def essai(dest: Path, k: str, fichier_essais: str) -> tuple[int, str]:
    try:
        r = subprocess.run([sys.executable, "-I", "-B", "-m", "pytest", "-q", "-x", "-p", "no:cacheprovider", "-k", k,
                            fichier_essais], cwd=dest, capture_output=True, text=True,
                           env={"PYTHONPATH": str(dest / "src"), "PATH": "/usr/sbin:/usr/bin:/sbin:/bin", "HOME": str(dest)},
                           timeout=600)
    except subprocess.TimeoutExpired:
        return -1, "délai de 600 s dépassé"
    return r.returncode, (r.stdout.strip().splitlines() or [""])[-1]


def main(argv: list[str]) -> int:
    toutes = mutations_v1() + [m + (T2,) for m in MUTATIONS_V2]
    temoins = [("témoin v1 sans mutation", None, None, None, "etiquette or egalite", T1),
               ("témoin v2 sans mutation", None, None, None, "etats_de or go_sain or depense_cas_sain", T2)]
    res = []
    with tempfile.TemporaryDirectory(prefix="banc2-") as t:
        base = Path(t) / "base"
        copier(base)
        for nom, fichier, ancien, nouveau, k, fe in temoins + toutes:
            d = Path(t) / f"m{len(res):02d}"
            shutil.copytree(base, d)
            if fichier:
                f = d / fichier
                s = f.read_text(encoding="utf-8")
                if s.count(ancien) != 1:
                    res.append({"mutation": nom, "statut": "INAPPLICABLE", "occurrences": s.count(ancien)})
                    print(f"INAPPLICABLE {nom} ({s.count(ancien)} occurrences)", flush=True)
                    shutil.rmtree(d)
                    continue
                f.write_text(s.replace(ancien, nouveau), encoding="utf-8")
            code, fin = essai(d, k, fe)
            statut = ("TEMOIN VERT" if code == 0 else "TEMOIN ROUGE") if fichier is None else ("TUÉE" if code > 0 else "SURVIVANTE")
            res.append({"mutation": nom, "essais": k, "fichier_essais": fe, "statut": statut, "fin": fin})
            print(f"{statut:12s} {nom} [{k}] : {fin}", flush=True)
            if argv:
                Path(argv[0]).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
            shutil.rmtree(d)
    if argv:
        Path(argv[0]).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    mauvais = [r for r in res if r["statut"] not in ("TUÉE", "TEMOIN VERT")]
    n1 = sum(1 for r in res if r["statut"] == "TUÉE" and r["mutation"].startswith("v1 : "))
    n2 = sum(1 for r in res if r["statut"] == "TUÉE" and not r["mutation"].startswith("v1 : "))
    print(f"{n1}/{len(toutes) - len(MUTATIONS_V2)} mutations v1 tuées ; {n2}/{len(MUTATIONS_V2)} mutations neuves tuées ; "
          f"défauts : {len(mauvais)}")
    return 1 if mauvais else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
