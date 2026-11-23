"""Vérification de la seconde passe de corrections du code de T0.8 (commit 453a71e1) — script du vérificateur (modèle B).

Lecture seule de l'arbre `/home/user/t08-code-compte4-v1` ; tout ce qui est écrit l'est sous le dossier du bloc-notes
passé en argument. Aucun réseau, aucune écriture git par ce script (les essais rejoués créent eux-mêmes leurs dépôts
jetables sous le dossier temporaire de pytest, comme dans l'arbre).

Parties :
  A. phrases gelées (parties A et B du script de la contre-lecture 1, rejouées) et sorties factices de l'essai v3 (a) ;
  B. déterminisme : `a/` contre `b/` de l'essai v3, par le comparateur corrigé et par un contrôle indépendant ;
  C. sondes directes (réserve « troncature », registre du texte de validité, ligne `CODE-T08`, passage à blanc) ;
  D. mutations : chaque garde de la seconde passe retirée ou affaiblie dans une copie jetable, essais nommés rejoués ;
     « tuée » = l'essai échoue ; « SURVIT » = l'essai passe encore.

Usage : python verification-corrections-2-t08-v1-calcul.py <dossier du bloc-notes> [A] [B] [C] [D]
"""
from __future__ import annotations

import hashlib
import json
import os
import queue
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ARBRE = Path("/home/user/t08-code-compte4-v1")
PY = "/home/user/controle-ia-travail/.venv/bin/python"
SCRIPT_CL1 = Path("/home/user/controle-ia-travail/brouillons/t08-code-compte4-v1/contre-lecture-1-code-t08-v1-calcul.py")
ESSAI = ARBRE / "essai" / "t08-jouet-compte4-v3"
BLOC = Path(sys.argv[1]).resolve()
PARTIES = set(sys.argv[2:]) or {"A", "B", "C", "D"}
sys.path.insert(0, str(ARBRE / "src"))
sys.dont_write_bytecode = True


def titre(t: str) -> None:
    print(f"\n=== {t} ===", flush=True)


def canon(x) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def un(motif: str) -> Path:
    r = sorted(ESSAI.glob(motif))
    assert len(r) == 1, (motif, r)
    return r[0]


# --- A ---------------------------------------------------------------------------------------------------------------
if "A" in PARTIES:
    titre("A1. Phrases gelées : parties A et B du script de la contre-lecture 1, rejouées à la tête")
    r = subprocess.run([PY, str(SCRIPT_CL1)], cwd=ARBRE, capture_output=True, text=True,
                       env={**os.environ, "PYTHONPATH": "src", "PYTHONDONTWRITEBYTECODE": "1"})
    lignes = r.stdout.split("\n=== C.")[0].splitlines()
    egales = sum(1 for l in lignes if re.match(r"^(D\d|F\d|F1b)\s+ÉGALE ", l))
    autres = [l for l in lignes if re.match(r"^(D\d|F\d|F1b)\s", l) and "ÉGALE" not in l]
    reserves = [l for l in lignes if l.startswith(("RESERVES.", "temoin.", "rendu.", "juges.IMPOSEE_TRONCATURE"))]
    print(f"phrases gelées des tables D et F égales au caractère près : {egales} sur 15 ; inégales : {autres}")
    print(f"réserves et mentions présentes entre guillemets dans le brouillon 4 : "
          f"{sum(1 for l in reserves if l.rstrip().endswith('dans le texte : True') and 'entre guillemets : True' in l)} "
          f"sur {len(reserves)}")

    titre("A2. Sorties factices de l'essai v3 (a)")
    from controle_ia.t08 import tables_v1 as tb

    lec = json.loads(un("a/diag/*-t08-lecture-jouet/lecture-t08.json").read_text())["resultat"]
    D = lec["table_D"]
    print(f"table D : ligne retenue {D['ligne']} ; lignes écrites {len(D['lignes'])} ; phrase égale à la phrase gelée : "
          f"{D['phrase'] == tb.PHRASES_D[D['ligne']]}")
    print("table F :", {d: (F["ligne"], len(F["lignes"]), F["phrase"] == tb.PHRASES_F[F["ligne"]].replace("<nommé>", str(F["surveillant"])))
                        for d, F in sorted(lec["table_F"].items())}, "(ligne, lignes écrites, phrase = gabarit gelé rempli)")
    o, oa = lec["fichiers_ouverts"], lec["entrees"]["ouvertes"]
    print(f"fichiers ouverts : {len(o)} (distincts {len(set(o))}) ; à l'étape (a) : {len(oa)} (distincts {len(set(oa))}) ; "
          f"manifeste de la course parmi eux : {any(c.endswith('-t08-course-jouet/manifeste.json') for c in oa)} ; "
          f"run_course {lec['entrees'].get('run_course')}")
    e = lec["descriptifs"]["ecarts_balises_imposees"]
    print(f"écarts des balises imposées : {len(e)} (juge, dose) ; clés {sorted(next(iter(e.values())))} ; maximum après "
          f"troncature {max(v['apres_troncature'] for v in e.values()):.4f} ; réserves « troncature » : "
          f"{sum(1 for r_ in lec['reserves'] if r_['code'] == 'troncature')}")
    print(f"point 8 bis : état {lec['temoin_distille_honnete']['etat']!r} ; étapes "
          f"{[x['etape'] for x in lec['ordre_des_etapes']]}")

# --- B ---------------------------------------------------------------------------------------------------------------
if "B" in PARTIES:
    titre("B. Déterminisme : essai v3, `a/` contre `b/`")
    from controle_ia.t08 import essai_jouet_v1 as ej

    c = ej.comparer(ESSAI / "a", ESSAI / "b")
    print(f"comparateur corrigé : fichiers {c['fichiers']} ; identiques à l'octet {c['identiques_octet']} ; égaux sur le "
          f"contenu {len(c['resultats_identiques'])} {[Path(x).name for x in c['resultats_identiques']]} ; exclus "
          f"{len(c['exclus'])} ; différents {len(c['differents'])} ; motifs {c['motifs']} ; contrôle des tables par racine "
          f"{c['controle_tables_par_racine']} ; deterministe {c['deterministe']}")
    for x in c["exclusions_declarees"]:
        print(f"   règle déclarée : {x['fichiers']} — {x['regle']}")

    def ecarts(x, y, chemin=""):
        if isinstance(x, dict) and isinstance(y, dict):
            for k in sorted(set(x) | set(y)):
                if k not in x or k not in y:
                    yield f"{chemin}/{k} (présence)"
                else:
                    yield from ecarts(x[k], y[k], f"{chemin}/{k}")
        elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
            for i, (u, v) in enumerate(zip(x, y)):
                yield from ecarts(u, v, f"{chemin}[{i}]")
        elif x != y:
            yield chemin

    # contrôle indépendant du comparateur : chaque fichier, à l'octet, puis par contenu
    fa = sorted(str(p.relative_to(ESSAI / "a")) for p in (ESSAI / "a").rglob("*") if p.is_file())
    fb = sorted(str(p.relative_to(ESSAI / "b")) for p in (ESSAI / "b").rglob("*") if p.is_file())
    diff = [f for f in fa if (ESSAI / "a" / f).read_bytes() != (ESSAI / "b" / f).read_bytes()]
    print(f"contrôle indépendant : mêmes listes de fichiers {fa == fb} ({len(fa)}) ; identiques à l'octet "
          f"{len(fa) - len(diff)} ; non identiques à l'octet {len(diff)} :")
    for f in diff:
        pa, pb = ESSAI / "a" / f, ESSAI / "b" / f
        if f.endswith(".json"):
            ja, jb = json.loads(pa.read_text()), json.loads(pb.read_text())
            if "resultat" in ja:
                env = sorted({x.split("/")[1].split("[")[0] for x in ecarts({k: v for k, v in ja.items() if k != "resultat"},
                                                                          {k: v for k, v in jb.items() if k != "resultat"})})
                print(f"   {f} : enveloppe, clés qui diffèrent {env} ; `resultat`, clés qui diffèrent "
                      f"{list(ecarts(ja['resultat'], jb['resultat']))}")
            else:
                print(f"   {f} : clés de premier niveau qui diffèrent {sorted({x.split('/')[1].split('[')[0] for x in ecarts(ja, jb)})}")
        elif f.endswith(".md"):
            la, lb_ = pa.read_text().splitlines(), pb.read_text().splitlines()
            print(f"   {f} : lignes qui diffèrent {[x.split('|')[1].strip() for x, y in zip(la, lb_) if x != y]} "
                  f"(mêmes nombres de lignes : {len(la) == len(lb_)})")
        else:
            print(f"   {f} : compagnon ou autre (octets différents)")
    for cote in ("a", "b"):
        f = json.loads(un(f"{cote}/diag/*-t08-lecture-jouet/lecture-t08.json").read_text())["resultat"]["tables_D_F_fichier"]
        pt = ESSAI / cote / f["chemin"]
        print(f"{cote} : sha256 citée {f['sha256'][:12]}… = fichier des tables sur disque : {f['sha256'] == sha(pt)} ; "
              f"contenu_sha256 {f['contenu_sha256'][:12]}…")

# --- C ---------------------------------------------------------------------------------------------------------------
if "C" in PARTIES:
    titre("C. Sondes directes")
    from controle_ia.gardes import GardeArret
    from controle_ia.t08 import configuration_v1 as cf
    from controle_ia.t08 import entrees_v1 as en
    from controle_ia.t08 import lecture_v1 as lv
    from controle_ia.t08 import temoin_distille_v1 as td

    sys.path.insert(0, str(ARBRE / "tests"))
    import test_t08_gardes_corrections_v1 as g

    # C1 : réserve « troncature », les deux cas C3 de la vérification courte
    for nom, h_, dose in (("H 20 % après troncature ; chaque dose 5 % après troncature et 15 % après fin de réponse",
                           (128, 0), (32, 96)),
                          ("H 0 % ; chaque dose 0 % après troncature et 15 % après fin de réponse", (0, 0), (0, 96))):
        b = g._base_reserves()
        for cond in (cf.HONNETE,) + cf.DOSES:
            tr, fin = h_ if cond == cf.HONNETE else dose
            b["comptes"]["J8r/masses"][cond].update(balises_imposees=tr + fin, imposees_troncature=tr, imposees_fin=fin)
        lettre = abs(dose[0] / 640 - h_[0] / 640)
        rendues = [(r["code"], r.get("dose"), round(r["ecart"], 4), round(r["ecart_somme"], 4)) for r in g._reserves(b)]
        print(f"C1 {nom} : écart de la lettre {lettre:.4f} (réserve {'due' if lettre > cf.RESERVE_ECARTS_PARTS else 'non due'}) ; "
              f"réserves rendues (code, dose, écart, écart de la somme) : {rendues}")

    # C2 : registre du texte de validité déclaré scellé
    d = BLOC / "sonde-c"
    shutil.rmtree(d, ignore_errors=True)
    (d / "reg").mkdir(parents=True)
    (d / "reg" / "validite.md").write_text(
        f"| SORTIES-HD-VADAPT | 2026-11-20T10:00:00Z | diag/x/sorties-hd-vadapt.json | {'a' * 64} |\n", encoding="utf-8")
    for nom, entree in (("déclaré vivant (scelle: false)", {"chemin": "reg/validite.md", "phase": "hd", "scelle": False}),
                        ("déclaré scellé par défaut, sans compagnon", {"chemin": "reg/validite.md", "phase": "hd"})):
        lb = en.ListeBlanche(d, {"registre_vadapt": entree})
        lb.ouvrir_phase("hd")
        try:
            r = td._sorties(lb)
            print(f"C2 registre du texte de validité {nom} : ligne rendue ({r['chemin']}) ; comptés ouverts {lb.ouvertes}")
        except en.ArretPieceHD as e:
            print(f"C2 registre du texte de validité {nom} : {e.etat!r}, motif {e.motif!r} ; comptés ouverts {lb.ouvertes}")

    # C3 : ligne CODE-T08, formes lues et citation du commit
    commit, autre = "a" * 40, "b" * 40
    reg = d / "reg" / "scellements.md"
    cas = {"commit en quatrième cellule": f"| CODE-T08 | 2026-11-20T10:05:00Z | src/controle_ia/t08 | {commit} |",
           "commit dans le chemin, empreinte en quatrième cellule": f"| CODE-T08 | 2026-11-20T10:05:00Z | src@{commit} | {'e' * 64} |",
           "autre commit en quatrième cellule, bon commit dans le chemin": f"| CODE-T08 | 2026-11-20T10:05:00Z | src@{commit} | {autre} |",
           "bon commit en majuscules dans le chemin": f"| CODE-T08 | 2026-11-20T10:05:00Z | src@{commit.upper()} | {'e' * 64} |",
           "commit abrégé (12 caractères) en quatrième cellule": f"| CODE-T08 | 2026-11-20T10:05:00Z | src | {commit[:12]} |",
           "clé entre accents graves": f"| `CODE-T08` | 2026-11-20T10:05:00Z | src | {commit} |",
           "date sans heure": f"| CODE-T08 | 2026-11-20 | src | {commit} |"}
    for nom, ligne in cas.items():
        reg.write_text("| CLÉ | date | chemin | empreinte |\n|---|---|---|---|\n" + ligne + "\n", encoding="utf-8")
        try:
            r = en.lire_registre_scellements(reg)
            l = r["lignes"].get("CODE-T08")
            cite = None if l is None else en.ligne_cite_commit(l, commit)
            print(f"C3 {nom} : lue {l is not None} ; cite le commit du marqueur : {cite} ; mal formées "
                  f"{[(m['numero'], m['cle']) for m in r['mal_formees']]}")
        except GardeArret as e:
            print(f"C3 {nom} : arrêt : {e}")
    reg.write_text(f"| SCELLEMENT-T08 | 2026-11-20T10:00:00Z | prereg/x.md | {autre} |\n", encoding="utf-8")
    r = en.lire_registre_scellements(reg)
    print(f"C3 autre clé (SCELLEMENT-T08) à 40 caractères : lue {'SCELLEMENT-T08' in r['lignes']} ; mal formées à clé lue "
          f"{[(m['numero'], m['cle']) for m in r['mal_formees_lues']]}")

    # C4 : passage à blanc sur un registre factice (marqueurs et texte factices des essais)
    mq = g._marqueurs()
    bloc = BLOC / "sonde-c" / "blanc"
    bloc.mkdir()
    p = g._prereg(bloc, mq)
    sha_t = sha(p)
    lignes_ = g._lignes_reelles(mq, sha_t)
    regp = g._registre(bloc, "sain", lignes_)
    avant = {x.name: sha(x) for x in sorted(bloc.iterdir())}
    r = lv.passage_a_blanc_reel(mq, regp, p, g.MAINTENANT)
    print(f"C4 passage à blanc, cas sain : clés rendues {sorted(r)} ; lignes lues {r['registre']['lignes_lues']} ; "
          f"fichiers du dossier inchangés (rien n'est écrit) : {avant == {x.name: sha(x) for x in sorted(bloc.iterdir())}}")
    texte = Path(regp).read_text(encoding="utf-8")
    minuscule = bloc / "registre-entete.md"
    minuscule.write_text("| clé | date | chemin | empreinte |\n|---|---|---|---|\n" + texte, encoding="utf-8")
    r = lv.passage_a_blanc_reel(mq, minuscule, p, g.MAINTENANT)
    print(f"C4 en-tête « clé » en minuscules : passe ; lignes d'une autre forme rendues {r['registre']['mal_formees']}")
    try:
        lv.passage_a_blanc_reel(mq, regp, p, datetime(2026, 11, 20, 12, 0, 0))
    except GardeArret as e:
        print(f"C4 heure du passage sans fuseau : arrêt : {e}")
    try:
        lv.passage_a_blanc_reel(mq, bloc / "registre-absent.md", p, g.MAINTENANT)
    except (GardeArret, OSError) as e:
        print(f"C4 registre absent du disque : {type(e).__name__} : {str(e)[:90]}")

# --- D ---------------------------------------------------------------------------------------------------------------
T, L, C, E, EJ = "temoin_distille_v1.py", "lecture_v1.py", "course_v1.py", "entrees_v1.py", "essai_jouet_v1.py"
LC, G = "test_t08_lecture_course_v1.py", "test_t08_gardes_corrections_v1.py"
REEL = f"{LC}::test_etape_a_mode_reel_cas_sain_et_artefacts"
BLANC = f"{G}::test_passage_a_blanc_cas_sain_et_artefacts"
COMPARATEUR = f"{G}::test_comparateur_lecture_exclusion_declaree_et_controle_des_tables"

MUTATIONS = [
    ("N01", "VCT8-01", "réserve « troncature » décidée de nouveau sur la somme", L,
     [('if e is not None and e["apres_troncature"] > cf.RESERVE_ECARTS_PARTS:',
       'if e is not None and e["somme"] > cf.RESERVE_ECARTS_PARTS:')],
     [f"{G}::test_reserves_masses_et_troncature", f"{G}::test_reserve_troncature_a_la_lettre_cas_c3"]),
    ("N02", "VCT8-01", "réserve « troncature » : 11 points au lieu de 10 (≥ au bord exclu)", L,
     [('if e is not None and e["apres_troncature"] > cf.RESERVE_ECARTS_PARTS:',
       'if e is not None and e["apres_troncature"] > cf.RESERVE_ECARTS_PARTS + 0.01:')],
     [f"{G}::test_reserves_masses_et_troncature"]),
    ("N03", "VCT8-02", "comparateur : empreinte citée non comparée au fichier des tables", EJ,
     [('    if empreinte(p) != f["sha256"]:', "    if False:")], [COMPARATEUR]),
    ("N04", "VCT8-02", "comparateur : contenu_sha256 non comparé au `resultat` des tables", EJ,
     [('    if _sha(json.loads(p.read_text(encoding="utf-8"))["resultat"]) != f["contenu_sha256"]:', "    if False:")],
     [COMPARATEUR]),
    ("N05", "VCT8-02", "comparateur : toute la clé tables_D_F_fichier exclue (chemin et contenu compris)", EJ,
     [("                                              if k != CLE_EXCLUE_LECTURE[1]}} for r in (ra, rb)]",
       "                                              if False}} for r in (ra, rb)]"),
      ('    if _sha(json.loads(p.read_text(encoding="utf-8"))["resultat"]) != f["contenu_sha256"]:', "    if False:")],
     [COMPARATEUR]),
    ("N06", "VCT8-03", "CODE-T08 : citation du commit non exigée", L,
     [("    if not en.ligne_cite_commit(code, commit):", "    if False:")], [BLANC, REEL]),
    ("N07", "VCT8-03", "lecture réelle : antériorité sur COURSE-T08 seule (début de la course oublié)", L,
     [('        bornes = {"COURSE-T08": en.date_utc(course["date"]),\n'
       '                  f"début de la course (création du manifeste {man_course[\'run_id\']})": '
       'en.date_utc(man_course["cree_le"])}',
       '        bornes = {"COURSE-T08": en.date_utc(course["date"])}')], [REEL]),
    ("N08", "VCT8-03", "antériorité non stricte (même seconde admise)", L,
     [("            if not date < borne:", "            if not date <= borne:")],
     [BLANC, f"{G}::test_controles_texte_et_registre_bornes"]),
    ("N09", "VCT8-03", "SCELLEMENT-T08 non comparée à l'empreinte du texte passé", L,
     [('    if scel["sha256"] != texte["sha256"]:', "    if False:")], [BLANC, REEL]),
    ("N10", "VCT8-03", "passage à blanc : COURSE-T08 déjà inscrite tolérée", L,
     [('    if "COURSE-T08" in reg["lignes"]:', "    if False:")], [BLANC]),
    ("N11", "VCT8-03", "passage à blanc : RUN-CONFIRMATION-T06 non comparée à RUN_7B", L,
     [('    if run["sha256"] != mq["RUN_7B"]["manifeste_sha256"]:', "    if False:")], [BLANC]),
    ("N12", "VCT8-03", "course-t08.json non rattaché au manifeste de la course lu", E,
     [('    if sha != corps_course.get("manifeste_sha256") or m.get("run_id") != corps_course.get("run_id"):', "    if False:")],
     [f"{LC}::test_etape_a_artefacts_des_entrees"]),
    ("N13", "VCT8-03", "commit reconnu comme partie d'une chaîne plus longue du chemin", E,
     [('    return re.search(r"(?<![0-9A-Fa-f])" + commit + r"(?![0-9A-Fa-f])", str(ligne.get("chemin") or "")) is not None',
       '    return commit in str(ligne.get("chemin") or "")')],
     [BLANC, f"{G}::test_registre_code_t08_forme_du_commit"]),
    ("N14", "VCT8-03", "quatrième cellule de 40 caractères lue pour toute clé", E,
     [('re.compile(r"^\\|\\s*(" + CODE_T08 + r")\\s*\\|', 're.compile(r"^\\|\\s*([A-Za-z0-9-]+)\\s*\\|')],
     [f"{G}::test_registre_code_t08_forme_du_commit"]),
    ("N15", "VCT8-05", "registre du texte de validité lu dans un autre état que « présent »", T,
     [('    if c["etat"] != "present":                 # registre vivant', "    if False:                 # registre vivant")],
     [f"{LC}::test_hd_registre_du_texte_de_validite_non_present_non_lu"]),
    ("N16", "VCT8-05", "formes de 7b absentes : pas d'arrêt à l'entrée de la lecture de la pièce HD", T,
     [("    if formes_7b is None:                      # défaut de chaîne", "    if False:                      # défaut de chaîne")],
     [f"{LC}::test_hd_formes_de_7b_absentes_arretent"]),
    ("N17", "VCT8-06", "appel de exiger_run_7b retiré de executer_course (M35)", C,
     [("        exiger_run_7b(man7b, marqueurs)\n", "")], [f"{LC}::test_course_reelle_manifeste_7b_d_un_autre_run"]),
    ("N18", "VCT8-06", "appel de exiger_sans_doublon retiré de executer_course (M38)", C,
     [("    doublons = exiger_sans_doublon(graines_et, graines_7b, premieres_et, premieres_h, tache_de_l_episode)\n",
       '    doublons = {"episodes_controles": 0, "taches_controlees": 0, "doublons": 0}\n')],
     [f"{LC}::test_course_jouet_premiere_action_egale_a_celle_de_h_arrete"]),
    ("N19", "VCT8-06", "échangeabilité : `hors_bornes` toujours faux (M61)", L,
     [('"hors_bornes": bool(a is not None and not (cf.ECHANGEABILITE[0] <= a <= cf.ECHANGEABILITE[1]))}',
       '"hors_bornes": False}')], [f"{LC}::test_echangeabilite_hors_bornes"]),
    ("N20", "VCT8-06", "échangeabilité : bords 0,40 et 0,60 comptés hors bornes", L,
     [("not (cf.ECHANGEABILITE[0] <= a <= cf.ECHANGEABILITE[1])", "not (cf.ECHANGEABILITE[0] < a < cf.ECHANGEABILITE[1])")],
     [f"{LC}::test_echangeabilite_hors_bornes"]),
    ("N21", "VCT8-07", "fichiers ouverts avec répétitions (résultat final)", L,
     [("        return _sans_repetition(self.lb.ouvertes)", "        return list(self.lb.ouvertes)")],
     [f"{LC}::test_fichiers_ouverts_sans_repetition", f"{LC}::test_lecture_complete_cas_sain"]),
    ("N22", "VCT8-07", "fichiers ouverts avec répétitions (étape (a))", L,
     [('self.r["entrees"] = {"ouvertes": _sans_repetition(lb.ouvertes),', 'self.r["entrees"] = {"ouvertes": list(lb.ouvertes),')],
     [f"{LC}::test_fichiers_ouverts_sans_repetition", f"{LC}::test_lecture_complete_cas_sain"]),
]
OUVRIERS = 4


def preparer_copie(k: int) -> Path:
    mut = BLOC / f"mutations-{k}"
    shutil.rmtree(mut, ignore_errors=True)
    (mut / "src" / "controle_ia").mkdir(parents=True)
    (mut / "tests").mkdir()
    shutil.copytree(ARBRE / "src" / "controle_ia" / "t08", mut / "src" / "controle_ia" / "t08",
                    ignore=shutil.ignore_patterns("__pycache__"))
    for p in sorted((ARBRE / "tests").glob("test_t08_*_v1.py")) + [ARBRE / "tests" / "conftest.py"]:
        shutil.copy(p, mut / "tests" / p.name)
    for lien in ("docs", "prereg", "brouillons"):
        (mut / lien).symlink_to(ARBRE / lien)
    (mut / "pytest.ini").write_text("[pytest]\npythonpath = tests\n", encoding="utf-8")
    # le paquet `controle_ia` reste celui de l'arbre ; seul le sous-paquet `t08` vient de la copie jetable
    (mut / "conftest.py").write_text(
        "import sys\nimport controle_ia\n"
        f"controle_ia.__path__.insert(0, {str(mut / 'src' / 'controle_ia')!r})\n"
        "assert 'controle_ia.t08' not in sys.modules\n"
        "import controle_ia.t08.configuration_v1 as _c\n"
        f"assert _c.__file__.startswith({str(mut)!r}), _c.__file__\n", encoding="utf-8")
    return mut


def pytest_(mut: Path, essais: list[str]) -> tuple[int, str]:
    r = subprocess.run([PY, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-c", "pytest.ini", "--rootdir", str(mut),
                        "--basetemp", str(mut / "tmp-pytest"), *essais],
                       cwd=mut, capture_output=True, text=True, timeout=2400,
                       env={**os.environ, "PYTHONPATH": str(ARBRE / "src"), "PYTHONDONTWRITEBYTECODE": "1",
                            "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"})
    fin = [l for l in r.stdout.strip().splitlines() if l.strip()]
    resume = re.sub(r" in [0-9.]+s.*$", "", fin[-1]) if fin else r.stderr.strip()[-200:]
    return r.returncode, resume


def eprouver(mut: Path, mutation: tuple) -> tuple[str, str]:
    """Applique une mutation dans la copie `mut`, rejoue les essais nommés, rend la copie à son état. (classe, ligne)."""
    ident, constat, quoi, fichier, remplacements, essais = mutation
    cible = mut / "src" / "controle_ia" / "t08" / fichier
    origine = cible.read_text(encoding="utf-8")
    texte = origine
    for vieux, neuf in remplacements:
        if texte.count(vieux) != 1:
            return "autre", (f"{ident} {constat:8s} {fichier:24s} INAPPLICABLE (motif trouvé {texte.count(vieux)} fois) : "
                             f"{quoi}")
        texte = texte.replace(vieux, neuf)
    cible.write_text(texte, encoding="utf-8")
    try:
        code, resume = pytest_(mut, [f"tests/{e}" for e in essais])
    finally:
        cible.write_text(origine, encoding="utf-8")
    echec_d_essai = code == 1 and "error" not in resume.lower()
    classe = "tuee" if echec_d_essai else "survit" if code == 0 else "autre"
    verdict = {"tuee": "tuée  ", "survit": "SURVIT"}.get(classe, f"code {code}")
    return classe, (f"{ident} {constat:8s} {fichier:24s} {verdict} : {quoi} — "
                    f"{' ; '.join(e.split('::')[1] for e in essais)} [{resume}]")


if "D" in PARTIES:
    titre("D. Mutations (copies jetables de `src/controle_ia/t08/` à la tête ; essais nommés rejoués)")
    copies = [preparer_copie(k) for k in range(OUVRIERS)]
    sources = sorted((ARBRE / "src/controle_ia/t08").glob("*.py"))

    def egales() -> bool:
        return all((m / "src" / "controle_ia" / "t08" / p.name).read_bytes() == p.read_bytes() for m in copies for p in sources)

    avant = egales()
    code, resume = pytest_(copies[0], ["tests"])
    print(f"copies égales à l'arbre : {avant} ; témoin sans mutation, les huit fichiers d'essais : code {code} ; {resume}",
          flush=True)
    libres: queue.Queue = queue.Queue()
    for m in copies:
        libres.put(m)

    def tache(mutation):
        m = libres.get()
        try:
            return eprouver(m, mutation)
        finally:
            libres.put(m)

    with ThreadPoolExecutor(max_workers=OUVRIERS) as ex:
        resultats = list(ex.map(tache, MUTATIONS))
    for _, ligne in resultats:
        print(ligne)
    par = {c: [l.split()[0] for k, l in resultats if k == c] for c in ("tuee", "survit", "autre")}
    print(f"bilan : {len(MUTATIONS)} mutations ; tuées par un échec d'essai {len(par['tuee'])} ; survivent "
          f"{len(par['survit'])} {par['survit']} ; autres {len(par['autre'])} {par['autre']} ; copies rendues égales à "
          f"l'arbre : {egales()}")
    for m in copies:
        shutil.rmtree(m / "tmp-pytest", ignore_errors=True)
