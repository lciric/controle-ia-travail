"""Lecture mécanique d'une course de pilote descriptif, après le moment de lecture : extrait de l'archive fermée les seuls
fichiers du juge et du rapport (sans rien exécuter), et écrit le tableau du plan § 4 de T2 (`pilote2-gemini-organisme-
v5-2-v2.md`) : famille × génération × {exactitude équilibrée sur `test`, sur `test_final`, référence de surface, Brier,
part sans réponse}, plus les comptes mécaniques de l'extrait. **Aucune différence n'est calculée** (ni g1 − g0, ni score
− référence, ni entre courses) ; aucun verbe de jugement.

Usage : python3 -I lire_pilote_tableaux_v1.py FERME_TAR_GZ SHA256_ATTENDU EXTRAIT_JSON LIGNEE NOM_COURSE SORTIE_MD
Écrit par conv-audit, 25 octobre 2026. Lit l'archive avec `tarfile` (aucun fichier extrait sur disque, aucun lien suivi).
"""
import hashlib, json, sys, tarfile

ferme, sha_attendu, extrait_f, lignee, nom, sortie = sys.argv[1:7]
REFS = {"test_final": {"conscience-evaluation": 0.69, "controle-delegation": 0.50},
        "test": {"conscience-evaluation": 0.75, "controle-delegation": 0.58}}  # confrontation v7, l. 90–92 (N-029)

h = hashlib.sha256(open(ferme, "rb").read()).hexdigest()
if h != sha_attendu:
    sys.exit(f"refus : ferme.tar.gz d'empreinte {h} ≠ {sha_attendu}")
lus = {}
with tarfile.open(ferme, "r:gz") as tf:
    for m in tf.getmembers():
        if not m.isfile():
            continue
        n = m.name
        if (n.startswith(f"course/archive/{lignee}/") and ("/juge/score.json" in n or "/juge/score-final.json" in n)
                and not n.endswith(".sha256")) or n == "course/rapport-v1.json" or n == "course/manifeste-run.json":
            lus[n] = json.loads(tf.extractfile(m).read().decode("utf-8"))
x = json.load(open(extrait_f, encoding="utf-8"))

def fam_nom(f):
    return {"conscience-evaluation": "A conscience d'évaluation", "controle-delegation": "B contrôle de délégation"}.get(f, f)

lignes = [f"# Tableau de lecture — course `{nom}` (lignée `{lignee}`)", "",
          f"Archive fermée `ferme.tar.gz` `{h}` ; extrait mécanique `{hashlib.sha256(open(extrait_f, 'rb').read()).hexdigest()}`.",
          "Fichiers lus dans l'archive : " + ", ".join(f"`{k}`" for k in sorted(lus)) + ".", "",
          "| génération | famille | exactitude équilibrée `test` | référence de surface `test` | exactitude équilibrée `test_final` | référence de surface `test_final` | Brier `test_final` | erreur de calibration `test_final` (10 classes) | part sans réponse `test_final` | sensibilité / spécificité `test_final` | n `test_final` |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
gens = sorted({int(k.split("/")[3][1:]) for k in lus if k.startswith(f"course/archive/{lignee}/g")})
for g in gens:
    st = lus.get(f"course/archive/{lignee}/g{g:03d}/juge/score.json") or {}
    sf = lus.get(f"course/archive/{lignee}/g{g:03d}/juge/score-final.json") or {}
    familles = sorted(set((st.get("par_famille") or {}).keys()) | set((sf.get("par_famille") or {}).keys()))
    for f in familles:
        a = (st.get("par_famille") or {}).get(f) or {}
        b = (sf.get("par_famille") or {}).get(f) or {}
        cal = b.get("calibration") or {}
        n_b = b.get("n")
        sans = (round(b.get("non_repondu", 0) / n_b, 4) if n_b else None)
        lignes.append(f"| g{g:03d} | {fam_nom(f)} | {a.get('exactitude_equilibree')} | {REFS['test'].get(f)} | {b.get('exactitude_equilibree')} | "
                      f"{REFS['test_final'].get(f)} | {cal.get('brier')} | {cal.get('ece_10')} | {sans} | {b.get('sensibilite')} / {b.get('specificite')} | {n_b} |")
    lignes.append(f"| g{g:03d} | moyenne des familles (score du juge) | {st.get('score')} | — | {sf.get('score')} | — | {(sf.get('calibration') or {}).get('brier')} | {(sf.get('calibration') or {}).get('ece_10')} | — | — | {sf.get('n')} |")
lignes.append("")
lignes.append("Comptes mécaniques (extrait) :")
lignes.append("")
for g in x.get("generations", []):
    if g.get("lignee") != lignee or g.get("phase"):
        continue
    a = g.get("appels") or {}
    pe = {k: v.get("par_statut") for k, v in (a.get("par_espece") or {}).items()}
    up = a.get("usage_par_espece") or {}
    sv = g.get("services") or {}
    q = g.get("question_ouverte")
    taille_mem = next((f.get("octets") for f in (g.get("fichiers_travail") or []) if f.get("chemin") == "memoire_isvd.json"), None)
    lignes.append(f"- g{g.get('generation'):03d} : statut {g.get('statut')} ; appels {a.get('n')} {json.dumps(a.get('par_statut'), sort_keys=True)} ; "
                  f"par espèce {json.dumps(pe, sort_keys=True)} ; jetons par espèce {json.dumps(up, sort_keys=True)} ; coût {a.get('cout_usd')} USD ; "
                  f"appels simultanés au plus {g.get('appels_simultanes_max')} ; recherches {json.dumps(sv.get('recherches'), sort_keys=True)} ; "
                  f"téléchargements {json.dumps(sv.get('telechargements'))} ; réponses de test valides {g.get('n_reponses_test')} ; "
                  f"relance {g.get('relance')} ; éléments écartés {g.get('n_elements_ecartes')} ; refus du noyau {json.dumps(g.get('refus_noyau'), ensure_ascii=False)} ; "
                  f"taille de memoire_isvd.json {taille_mem} ; archive de l'organisme {g.get('organisme_tar_sha256')} ; "
                  f"question {json.dumps(q, ensure_ascii=False) if q else 'non posée'}")
r = x.get("rapport") or {}
m = x.get("manifeste") or {}
lignes.append(f"- course : dépense du noyau {r.get('depense_totale_usd')} USD ; fin de la lignée {((r.get('lignees') or {}).get(lignee) or {}).get('fin')} ; "
              f"graine {m.get('entropie_seed_sequence')} ; GO {m.get('go_id')} ; registre_go {json.dumps(m.get('registre_go'), ensure_ascii=False)[:200]} ; "
              f"clés présentes — web {m.get('cle_brave_presente')}, OpenAlex {m.get('cle_openalex_presente')}, Semantic Scholar {m.get('cle_s2_presente')}")
open(sortie, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
print(f"tableau écrit : {sortie} ({len(gens)} générations)")
