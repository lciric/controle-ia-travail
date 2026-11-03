"""Épreuve de lecture de la v2, brouillon 1, d'A1-v3 par le lanceur v3.1 du commit 9776ed0 — sans réseau, sans modèle, sans
`--moteur reel`, sans aucun fichier `.sha256` écrit (le compagnon est simulé en mémoire : la fonction réelle `verifier_scelle`
lit, à la place du fichier compagnon, une chaîne en mémoire ; tout autre fichier est lu sur disque).

Arbre du lanceur : `orchestrator/` du commit 9776ed0, extrait par `git archive` sans ses fichiers `.sha256` (RACINE) ; le
brouillon y est copié sous `prereg/preenregistrement-attaque-goodhart-v3-v2.md` (le dossier `prereg/` du lanceur). Fonctions
du lanceur appelées : `lire_plan`, `lire_preenregistrement` (chemin, scellé, marqueurs, bloc d'empreintes contre `FICHIERS_GELES`
et les fichiers de l'arbre, plan, entropie), `verifier_go` (→ `configuration_v56.verifier_go_v56`). Usage :
  nice -n 10 python3 -I -B epreuve_lanceur_v2b1.py RACINE BROUILLON V1 DEPOT_PUBLIC DEPOT_PRIVE REGISTRE_FACTICE SORTIE_JSON [BROUILLON_AU_DEPOT]
"""
import datetime
import difflib
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest.mock

sys.dont_write_bytecode = True
COMMIT_GELE = "9776ed0efee97146182ff2c4b409e5ec224a0bbf"
MAIN_PRIVE = "e12540bf1e1cad4683f0e0f193345a5acc2c6bc2"
GO2, GO1 = "GO-2026-11-03-01", "GO-2026-11-02-21"
NOM_V2 = "preenregistrement-attaque-goodhart-v3-v2.md"


def sha_octets(b):
    return hashlib.sha256(b).hexdigest()


def sha(chemin):
    with open(chemin, "rb") as f:
        return sha_octets(f.read())


def essai(fonction):
    """Rend {'resultat': 'accepté', …} ou {'resultat': 'refusé', 'type', 'message'}."""
    try:
        r = fonction()
        return {"resultat": "accepté", "valeur": r}
    except Exception as e:  # noqa: BLE001 — on rapporte le refus tel quel
        return {"resultat": "refusé", "type": type(e).__name__, "message": str(e)}


def main(argv):
    racine, brouillon, v1, depot_public, depot_prive, registre_factice, sortie = [os.path.realpath(x) for x in argv[:7]]
    brouillon_au_depot = os.path.realpath(argv[7]) if len(argv) > 7 else None
    avec_marqueur = os.path.realpath(argv[8]) if len(argv) > 8 else None  # assemblage antérieur, qui portait le marqueur de l'audit A9
    r = {"date_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "racine": racine}
    prereg = os.path.join(racine, "prereg")
    copie = os.path.join(prereg, NOM_V2)

    # 0. Copie du brouillon dans prereg/ de l'arbre extrait (le dossier que lit le lanceur).
    shutil.copyfile(brouillon, copie)
    r["copie"] = {"chemin": copie, "sha256": sha(copie), "egale_au_brouillon": sha(copie) == sha(brouillon),
                  "compagnon_sur_disque": os.path.exists(copie + ".sha256"),
                  "fichiers_sha256_dans_l_arbre": sum(1 for _, _, fs in os.walk(racine) for f in fs if f.endswith(".sha256"))}

    # 1. Lanceur v3.1 du commit gelé, chargé depuis l'arbre extrait.
    spec = importlib.util.spec_from_file_location("lanceur_v31_epreuve", os.path.join(racine, "demonstrations", "attaque_goodhart_v3.py"))
    L = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(L)
    from pole import configuration_v56 as cfg  # noqa: E402 (même arbre)
    from pole import outils  # noqa: E402
    r["lanceur"] = {"fichier": L.__file__, "sha256": sha(L.__file__), "RACINE": L.RACINE, "DOSSIER_PREREG": L.DOSSIER_PREREG,
                    "racine_conforme": os.path.realpath(L.RACINE) == racine and os.path.realpath(L.DOSSIER_PREREG) == prereg,
                    "pole_charge_depuis": os.path.dirname(sys.modules["pole"].__file__),
                    "motif_marqueur": L.MARQUEUR.pattern, "motif_nom_course": L.NOMS_PREREG["course"].pattern}

    t1 = open(v1, encoding="utf-8").read()
    t2 = open(brouillon, encoding="utf-8").read()
    l2 = L.l2

    # 2. Marqueurs (motif du lanceur v3.1 ; et celui de la v2, pour mémoire).
    def lieux(motif, t):
        return [(m.group(0), t.count("\n", 0, m.start()) + 1) for m in motif.finditer(t)]
    r["marqueurs"] = {"v1": lieux(L.MARQUEUR, t1), "v2_brouillon1": lieux(L.MARQUEUR, t2),
                      "v2_brouillon1_motif_du_lanceur_v2": lieux(l2.MARQUEUR, t2),
                      "doubles_chevrons_hors_motif": [n for n, l in enumerate(t2.splitlines(), 1) if "<<" in l and not L.MARQUEUR.search(l)]}

    # 3. Blocs : un seul début et une seule fin de chaque ; empreintes identiques à la v1 ; plan-gele : seule la ligne go change.
    r["blocs"] = {k: t2.count(v) for k, v in (("debut_empreintes", L.DEBUT_EMPREINTES), ("fin_empreintes", L.FIN_EMPREINTES),
                                              ("debut_plan", L.DEBUT_PLAN), ("fin_plan", L.FIN_PLAN))}
    be1 = l2._bloc(t1, L.DEBUT_EMPREINTES, L.FIN_EMPREINTES, "empreintes-du-code")
    be2 = l2._bloc(t2, L.DEBUT_EMPREINTES, L.FIN_EMPREINTES, "empreintes-du-code")
    bp1 = l2._bloc(t1, L.DEBUT_PLAN, L.FIN_PLAN, "plan-gele").splitlines()
    bp2 = l2._bloc(t2, L.DEBUT_PLAN, L.FIN_PLAN, "plan-gele").splitlines()
    r["blocs"]["empreintes_egales_a_la_v1"] = be1 == be2
    r["blocs"]["plan_lignes_changees"] = [(a, b) for a, b in zip(bp1, bp2) if a != b] + ([("longueurs", len(bp1), len(bp2))] if len(bp1) != len(bp2) else [])

    # 4. Bloc d'empreintes contre FICHIERS_GELES et contre les fichiers du commit 9776ed0 (arbre extrait, objets git) et de la tête.
    gelees = re.findall(r"^([0-9a-f]{64})  (\S+)$", be2, re.M)
    noms = [n for _, n in gelees]
    ecarts = []
    for h, n in gelees:
        dans_l_arbre = sha(os.path.join(racine, n))
        objet = sha_octets(subprocess.run(["git", "-c", "gc.auto=0", "-c", "maintenance.auto=false", "-C", depot_public, "show", f"{COMMIT_GELE}:orchestrator/{n}"], capture_output=True,
                                          check=True).stdout)
        tete = sha(os.path.join(depot_public, "orchestrator", n))
        if not (h == dans_l_arbre == objet == tete):
            ecarts.append({"fichier": n, "bloc": h, "arbre_extrait": dans_l_arbre, "objet_git": objet, "tete": tete})
    r["empreintes_du_code"] = {"lignes_du_bloc": len(gelees), "FICHIERS_GELES": len(L.FICHIERS_GELES),
                               "ensemble_egal_a_FICHIERS_GELES": sorted(noms) == sorted(L.FICHIERS_GELES) and len(set(noms)) == len(noms),
                               "ecarts_bloc_arbre_commit_tete": ecarts}

    # 5. lire_plan sur la v1 et sur le brouillon.
    p1 = L.lire_plan(t1, mode_attendu="course")
    p2 = L.lire_plan(t2, mode_attendu="course")
    r["lire_plan"] = {"v2_brouillon1": {k: p2[k] for k in ("mode", "cartes", "unites_par_case", "mondes", "relais_perdu_h", "relais_perdu_s",
                                                            "plafond_usd", "duree_max_s", "essais_avant_repli", "configuration_sha256", "go")},
                      "fournisseurs": p2["fournisseurs"],
                      "devis_total": {k: p2["devis"]["total"][k] for k in ("appels_attendus", "appels_max", "usd_attendus", "usd_max",
                                                                           "duree_attendue_haute_h", "duree_max_h")},
                      "cles_differentes_de_la_v1": sorted(k for k in set(p1) | set(p2) if p1.get(k) != p2.get(k))}

    # 6. lire_preenregistrement : compagnon simulé en mémoire (jamais écrit).
    vrai_open = open

    def avec_compagnon(compagnons):
        def ouvrir(chemin, *a, **k):
            if isinstance(chemin, str) and chemin.endswith(".sha256") and os.path.realpath(chemin[:-7]) in compagnons:
                return io.StringIO(compagnons[os.path.realpath(chemin[:-7])])
            return vrai_open(chemin, *a, **k)
        return unittest.mock.patch.object(outils, "open", ouvrir, create=True)

    def resume_accepte(x):
        entropie, empreinte, gel, plan = x
        return {"empreinte": empreinte, "entropie_egale_entier_de_l_empreinte": entropie == int(empreinte, 16),
                "entropie_au_moins_2_64": entropie >= 2 ** 64, "empreintes_verifiees": len(gel), "go": plan["go"],
                "plan_egal_a_lire_plan_du_brouillon": {k: v for k, v in plan.items() if k != "devis"} == {k: v for k, v in p2.items() if k != "devis"}}

    lp = {}
    lp["a_copie_sans_compagnon"] = essai(lambda: L.lire_preenregistrement(copie))
    with avec_compagnon({copie: f"{sha(copie)}  {NOM_V2}\n"}):
        lp["b_copie_compagnon_simule_juste"] = essai(lambda: L.lire_preenregistrement(copie))
    if lp["b_copie_compagnon_simule_juste"]["resultat"] == "accepté":
        lp["b_copie_compagnon_simule_juste"]["valeur"] = resume_accepte(lp["b_copie_compagnon_simule_juste"]["valeur"])
    with avec_compagnon({copie: f"{'0' * 64}  {NOM_V2}\n"}):
        lp["c_copie_compagnon_simule_faux"] = essai(lambda: L.lire_preenregistrement(copie))
    rempli = t2.replace("<<AUDIT_A9>>", "`audit-a9-factice-epreuve.md`, sha256 `" + "0" * 64 + "` ; conclusion factice (épreuve du rédacteur)")
    with tempfile.TemporaryDirectory(prefix="prereg-rempli-") as d:
        d = os.path.realpath(d)
        f_rempli = os.path.join(d, NOM_V2)
        with open(f_rempli, "w", encoding="utf-8") as f:
            f.write(rempli)
        f_nom_brouillon = os.path.join(d, "preenregistrement-attaque-goodhart-v3-v2-brouillon1.md")
        shutil.copyfile(f_rempli, f_nom_brouillon)
        altere = rempli.replace("cb9cffe77fb858bf279c41881638edecba0166b034a05d44c2f62e2b25a45df3  pole/attaque_goodhart_v3.py",
                                "db9cffe77fb858bf279c41881638edecba0166b034a05d44c2f62e2b25a45df3  pole/attaque_goodhart_v3.py", 1)
        assert altere != rempli
        sous_dossier = os.path.join(d, "autre")
        os.mkdir(sous_dossier)
        f_altere = os.path.join(sous_dossier, NOM_V2)
        with open(f_altere, "w", encoding="utf-8") as f:
            f.write(altere)
        comp = {p: f"{sha(p)}  {os.path.basename(p)}\n" for p in (f_rempli, f_nom_brouillon, f_altere)}
        with avec_compagnon(comp), unittest.mock.patch.object(L, "DOSSIER_PREREG", d):
            x = essai(lambda: L.lire_preenregistrement(f_rempli))
            if x["resultat"] == "accepté":
                x["valeur"] = resume_accepte(x["valeur"])
            lp["d_marqueur_rempli_factice_compagnon_simule"] = x
            lp["e_meme_texte_au_nom_du_brouillon"] = essai(lambda: L.lire_preenregistrement(f_nom_brouillon))
        with avec_compagnon(comp), unittest.mock.patch.object(L, "DOSSIER_PREREG", sous_dossier):
            lp["f_une_empreinte_du_bloc_alteree"] = essai(lambda: L.lire_preenregistrement(f_altere))
        if avec_marqueur:
            d_m = os.path.join(d, "avec-marqueur")
            os.mkdir(d_m)
            f_m = os.path.join(d_m, NOM_V2)
            shutil.copyfile(avec_marqueur, f_m)
            with avec_compagnon({f_m: f"{sha(f_m)}  {NOM_V2}\n"}), unittest.mock.patch.object(L, "DOSSIER_PREREG", d_m):
                lp["h_assemblage_avec_marqueur_compagnon_simule"] = dict(essai(lambda: L.lire_preenregistrement(f_m)), sha256=sha(f_m))
        r["lire_preenregistrement_note"] = ("d à f : texte écrit dans un dossier temporaire (aucun .sha256), DOSSIER_PREREG du lanceur "
                                            "pointé sur ce dossier ; RACINE (code gelé vérifié) reste l'arbre extrait du commit")
    if brouillon_au_depot:
        lp["g_brouillon_a_son_chemin_dans_le_depot"] = essai(lambda: L.lire_preenregistrement(brouillon_au_depot))
    r["lire_preenregistrement"] = lp

    # 7. GO : registre factice (ligne recopiée), artefacts, registres privés entiers.
    arbre_prive = os.path.join(depot_prive, "registres", "go.md")
    lignes_prive = open(arbre_prive, encoding="utf-8").read().splitlines()
    ligne_go2 = [l for l in lignes_prive if l.startswith(f"| {GO2} |")]
    ligne_go1 = [l for l in lignes_prive if l.startswith(f"| {GO1} |")]
    assert len(ligne_go2) == 1 and len(ligne_go1) == 1
    entete = ("# Registre des GO — factice (épreuve du rédacteur de la v2 d'A1-v3)\n\n"
              "Ligne recopiée sans retouche de `registres/go.md` du dépôt privé (ligne 79 de l'arbre ; ligne 221 de `origin/main` "
              "`e12540bf`).\n\n| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
              "|---|---|---|---|---|---|---|---|\n")
    contenu = entete + ligne_go2[0] + "\n"
    if os.path.exists(registre_factice):
        assert open(registre_factice, encoding="utf-8").read() == contenu, "registre factice différent du contenu attendu"
    else:
        with open(registre_factice, "w", encoding="utf-8") as f:
            f.write(contenu)
    g = {"registre_factice": {"chemin": registre_factice, "sha256": sha(registre_factice)}}

    def resume_go(x):
        if x["resultat"] == "accepté":
            v = x["valeur"]
            x["valeur"] = {k: v.get(k) for k in ("identifiant", "type", "accorde", "echeance", "par", "plafond_lu_usd", "montant_requis_usd", "ligne")}
        return x
    g["a_factice_GO_du_texte"] = resume_go(essai(lambda: L.verifier_go(registre_factice, GO2, p2, cfg)))
    g["b_factice_autre_GO_en_ligne_de_commande"] = resume_go(essai(lambda: L.verifier_go(registre_factice, GO1, p2, cfg)))
    g["c_plafond_399"] = resume_go(essai(lambda: L.verifier_go(registre_factice, GO2, dict(p2, plafond_usd=399.0), cfg)))
    g["c_plafond_401"] = resume_go(essai(lambda: L.verifier_go(registre_factice, GO2, dict(p2, plafond_usd=401.0), cfg)))
    for jour in ("2026-11-02", "2026-11-17", "2026-11-18"):
        g[f"d_date_{jour}"] = resume_go(essai(lambda: cfg.verifier_go_v56(GO2, registre_factice, 400.0, aujourd_hui=datetime.date.fromisoformat(jour))))
    rev = "| GO-2026-11-03-99 | 2026-11-03 | révocation | {p} | — | 2026-11-03 | Lazar | épreuve factice |\n"
    dec = "| GO-2026-11-03-98 | 2026-11-03 | décision | {p} | — | 2026-11-03 | Lazar | épreuve factice |\n"
    artefacts = {"e_revocation_qui_nomme_le_GO": (contenu + rev.format(p=f"révoque {GO2}"), GO2),
                 "e_decision_qui_nomme_le_GO": (contenu + dec.format(p=f"note sur {GO2}"), GO2),
                 "e_revocation_du_GO_21_qui_porte_aussi_le_GO_neuf": (contenu + ligne_go1[0] + "\n" + rev.format(p=f"révoque {GO1}, remplacé par {GO2}"), GO2),
                 "e_revocation_du_GO_21_seul_GO_neuf": (contenu + ligne_go1[0] + "\n" + rev.format(p=f"révoque {GO1}"), GO2),
                 "e_revocation_du_GO_21_seul_GO_21": (contenu + ligne_go1[0] + "\n" + rev.format(p=f"révoque {GO1}"), GO1)}
    with tempfile.TemporaryDirectory(prefix="registres-factices-") as d:
        for nom, (texte_reg, go) in artefacts.items():
            p = os.path.join(d, nom + ".md")
            with open(p, "w", encoding="utf-8") as f:
                f.write(texte_reg)
            plan = p2 if go == GO2 else p1
            g[nom] = resume_go(essai(lambda: L.verifier_go(p, go, plan, cfg)))
    # Registres privés entiers : l'arbre du dépôt privé (lu en place) et quatre commits fixes (fichiers temporaires) :
    # `main` e12540bf (cité par la consigne) et db454552 (le plus récent vu pendant la rédaction) ; `canal/conv-audit-n04`
    # e4fd3690 (premier commit de la branche qui porte la ligne recopiée) et 3f132371 (le plus récent vu).
    def registre_entier(chemin):
        lignes = open(chemin, encoding="utf-8").read().splitlines()
        ids = [m.group(1) for m in (re.match(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|", l) for l in lignes) if m]
        return {"sha256": sha(chemin), "lignes": len(lignes), "lignes_GO": len(ids),
                "identifiants_en_double": sorted({i for i in ids if ids.count(i) > 1}),
                "grep_GO_neuf": [n for n, l in enumerate(lignes, 1) if GO2 in l], "grep_GO_21": [n for n, l in enumerate(lignes, 1) if GO1 in l],
                "revocations_qui_nomment_le_GO_neuf": [n for n, l in enumerate(lignes, 1) if GO2 in l and "| révocation |" in l],
                "ligne_du_GO_neuf_egale_a_celle_de_l_arbre": [l for l in lignes if l.startswith(f"| {GO2} |")] == ligne_go2,
                "GO_du_texte_v2": resume_go(essai(lambda: L.verifier_go(chemin, GO2, p2, cfg))),
                "GO_21_avec_le_plan_de_la_v1": resume_go(essai(lambda: L.verifier_go(chemin, GO1, p1, cfg)))}
    g["f_arbre_du_depot_prive"] = dict(registre_entier(arbre_prive), chemin=arbre_prive)
    commits = {"g_main_e12540bf": MAIN_PRIVE, "g_main_db454552": "db454552d445d19e46a8df2e4b3ce6622f3011e9",
               "g_canal_conv_audit_n04_e4fd3690": "e4fd36905b58bf8ba3cf82ef012af51acd36ff03",
               "g_canal_conv_audit_n04_3f132371": "3f1323719918501137aa7a45c25fb65b86e333dd",
               "g_canal_conv_audit_n04_c8c34784": "c8c3478422bd335bd4e1003b84dadba2a26f6206",  # commit de l'audit A9
               "g_premiere_course_canal_e9d7b78d": "e9d7b78dc7c177d6b22247639cfec42727b9f9ec"}  # registre copié à la première course
    with tempfile.TemporaryDirectory(prefix="registres-prives-") as d:
        for nom, c in commits.items():
            b = subprocess.run(["git", "-c", "gc.auto=0", "-c", "maintenance.auto=false", "-C", depot_prive, "show", f"{c}:registres/go.md"], capture_output=True, check=True).stdout
            p = os.path.join(d, nom + ".md")
            with open(p, "wb") as f:
                f.write(b)
            g[nom] = dict(registre_entier(p), commit=c)
    r["go"] = g

    # 8. Lignes de code citées par les passages neufs : contenu attendu à la ligne citée (arbre extrait = commit 9776ed0).
    def lignes(rel):
        return open(os.path.join(racine, rel), encoding="utf-8").read().splitlines()
    attendus = [
        ("demonstrations/attaque_goodhart_v3.py", 91, 92, ["NOMS_PREREG", "preenregistrement-attaque-goodhart-v3-v"]),
        ("demonstrations/attaque_goodhart_v3.py", 97, 97, ["MARQUEUR = re.compile"]),
        ("demonstrations/attaque_goodhart_v3.py", 257, 257, ["def lire_preenregistrement"]),
        ("demonstrations/attaque_goodhart_v3.py", 260, 264, ["mode réel : le texte est prereg/preenregistrement-attaque-goodhart-v3-v<N>.md"]),
        ("demonstrations/attaque_goodhart_v3.py", 271, 273, ["marqueur(s) non rempli(s)"]),
        ("demonstrations/attaque_goodhart_v3.py", 288, 288, ["sha256_fichier(reel)"]),
        ("demonstrations/attaque_goodhart_v3.py", 289, 289, ["verifier_entropie(int(empreinte, 16), decisif=True)"]),
        ("demonstrations/attaque_goodhart_v3.py", 504, 505, ["dossier de sortie non vide"]),
        ("demonstrations/attaque_goodhart_v3.py", 540, 540, ["lire_preenregistrement(args.preenregistrement)"]),
        ("demonstrations/attaque_goodhart_v3.py", 547, 547, ["verifier_go(args.registre_go, args.go, plan, cfg)"]),
        ("demonstrations/attaque_goodhart_v3.py", 562, 567, ["except (FileExistsError", "return 2"]),
        ("demonstrations/attaque_goodhart_v3.py", 577, 577, ["entropie_racine=str(entropie)"]),
        ("demonstrations/attaque_goodhart_v3.py", 583, 588, ["regle_des_graines", "int(SHA-256 du texte scellé, 16)"]),
        ("demonstrations/attaque_goodhart_v3.py", 592, 592, ["manifeste.json"]),
        ("demonstrations/attaque_goodhart_v3.py", 607, 607, ["a3.jouer_tout(proposeurs, entropie"]),
        ("demonstrations/attaque_goodhart_v3.py", 609, 621, ["except ag.ArretAttaque", "ecrire_json_scelle(sortie, rapport)", "return 3"]),
        ("demonstrations/attaque_goodhart_v3.py", 637, 637, ["a3.lire(suites, rejeux, audits", "entropie"]),
        ("demonstrations/attaque_goodhart_v3.py", 637, 646, ["ecrire_json_scelle(sortie, rapport)", "return 0"]),
        ("pole/attaque_goodhart_v3.py", 381, 381, ["Le texte brut ne sert qu'en mémoire"]),
        ("pole/attaque_goodhart_v3.py", 500, 500, ["ag.juger(loi, c, juge, entropie, etiquette, k)"]),
        ("pole/attaque_goodhart_v3.py", 703, 703, ["def jouer_tout"]),
        ("pole/attaque_goodhart_v3.py", 708, 708, ["verifier_entropie(entropie, decisif)"]),
        ("pole/attaque_goodhart_v3.py", 729, 729, ["carte(entropie, ci, w)"]),
        ("pole/attaque_goodhart_v3.py", 766, 770, ["rejouer_tout(suites, entropie", "auditer_promues(suites, entropie"]),
        ("pole/attaque_goodhart_v2.py", 100, 101, ["def cle"]),
        ("pole/attaque_goodhart_v2.py", 104, 108, ["def graine", "SeedSequence(int(entropie), spawn_key=(cle(etiquette),)"]),
        ("pole/attaque_goodhart_v2.py", 111, 118, ["def verifier_entropie", "GRAINE_EXPLORATOIRE_MAX"]),
        ("pole/attaque_goodhart_v2.py", 165, 165, ["def carte(entropie, c, monde)"]),
        ("pole/attaque_goodhart_v2.py", 170, 170, ['graine(entropie, f"monde|{monde}", c)']),
        ("pole/attaque_goodhart_v2.py", 178, 178, ['graine(entropie, f"developpement|{monde}", c)']),
        ("pole/attaque_goodhart_v2.py", 186, 186, ["return {"]),
        ("pole/attaque_goodhart_v2.py", 433, 433, ["def juger(loi, c, juge, entropie, etiquette, k"]),
        ("pole/attaque_goodhart_v2.py", 442, 444, ['graine(entropie, f"{etiquette}|scenario"', 'graine(entropie, f"{etiquette}|noyau"',
                                                    'graine(entropie, f"{etiquette}|frais"']),
        ("pole/attaque_goodhart_v2.py", 813, 813, ['cle("bootstrap")']),
        ("demonstrations/attaque_goodhart_v2.py", 98, 102, ["def _bloc", "texte.find(debut)"]),
        ("demonstrations/attaque_goodhart_v2.py", 185, 185, ["def verifier_go"]),
        ("demonstrations/attaque_goodhart_v2.py", 191, 192, ['if go != plan["go"]', "aucun autre GO"]),
        ("demonstrations/attaque_goodhart_v2.py", 196, 196, ["raise ag.AttaqueRefusee(str(e)) from None"]),
        ("pole/outils.py", 72, 79, ["def verifier_scelle", 'open(chemin + ".sha256"']),
        ("pole/configuration_v55.py", 53, 53, ["def lire_plafond"]),
        ("pole/configuration_v55.py", 72, 72, ["def verifier_go_v55"]),
        ("pole/configuration_v55.py", 90, 92, ['r["type"] == "révocation" and (go_id in r["perimetre"] or go_id in r["ref"])', "révoqué par"]),
        ("pole/configuration_v55.py", 99, 101, ["return dict(g"]),
        ("pole/configuration_v53.py", 258, 258, ["def lire_registre_go"]),
        ("pole/configuration_v53.py", 281, 281, ["return go"]),
    ]
    citees = []
    for rel, a, b, morceaux in attendus:
        ls = lignes(rel)
        bloc = "\n".join(ls[a - 1:b])
        citees.append({"renvoi": f"{rel}:{a}" + (f"-{b}" if b != a else ""), "dans_les_bornes": b <= len(ls),
                       "conforme": all(m in bloc for m in morceaux), "absents": [m for m in morceaux if m not in bloc],
                       "premiere_ligne": ls[a - 1].strip()[:110] if a <= len(ls) else None})
    r["renvois_des_passages_neufs"] = {"nombre": len(citees), "non_conformes": [c for c in citees if not c["conforme"] or not c["dans_les_bornes"]],
                                       "detail": citees}

    # 9. Renvois `fichier:ligne` vers les deux fichiers v3 dans tout le brouillon : dans les bornes (méthode du rédacteur du brouillon 4).
    bornes = {f: len(lignes(f)) for f in ("pole/attaque_goodhart_v3.py", "demonstrations/attaque_goodhart_v3.py")}
    hors, courant, total = [], None, 0
    for n, l in enumerate(t2.splitlines(), 1):
        for m in re.finditer(r"((?:pole|demonstrations|essais)/[A-Za-z0-9_]+\.py)(?::(\d+)(?:-(\d+))?)?|`:(\d+)(?:-(\d+))?`", l):
            if m.group(1):
                courant, a, b = m.group(1), m.group(2), m.group(3)
            else:
                a, b = m.group(4), m.group(5)
            if a and courant in bornes:
                total += 1
                if not (1 <= int(a) <= int(b or a) <= bornes[courant]):
                    hors.append((n, courant, a, b))
    r["renvois_v3_dans_tout_le_brouillon"] = {"renvois": total, "hors_bornes": hors}

    # 10. GO, chemins, nom : lieux dans le brouillon.
    def ou(motif):
        return [n for n, l in enumerate(t2.splitlines(), 1) if motif in l]
    r["lieux"] = {"GO_neuf": ou(GO2), "GO_21": ou(GO1), "identifiants_de_GO": sorted(set(re.findall(r"GO-\d{4}-\d{2}-\d{2}-\d{2}", t2))),
                  "ancien_dossier_hors_clone": ou("/home/user/hors-clone-a1-v3/"), "dossier_neuf": ou("/home/user/hors-clone-a1-v3-seconde-v1/"),
                  "nom_v2_scelle": ou("preenregistrement-attaque-goodhart-v3-v2.md"), "vN_md": ou("-v3-vN.md"),
                  "ligne_go_du_bloc": [l for l in bp2 if l.startswith("go:")]}

    # 11. Différence v1 → brouillon (comptes).
    d = list(difflib.unified_diff(t1.splitlines(), t2.splitlines(), lineterm="", n=0))
    r["difference"] = {"lignes_retirees": sum(1 for x in d if x.startswith("-") and not x.startswith("---")),
                       "lignes_ajoutees": sum(1 for x in d if x.startswith("+") and not x.startswith("+++")),
                       "blocs": sum(1 for x in d if x.startswith("@@")), "lignes_v1": t1.count("\n"), "lignes_v2": t2.count("\n")}
    r["copie_finale_inchangee"] = sha(copie) == sha(brouillon)
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False, indent=1, default=str)
    print(json.dumps({"lire_plan_cles_differentes": r["lire_plan"]["cles_differentes_de_la_v1"],
                      "lire_preenregistrement": {k: (v["resultat"], v.get("message", "")[:160]) for k, v in lp.items()},
                      "go": {k: (v["resultat"], v.get("message", "")[:160]) for k, v in g.items() if isinstance(v, dict) and "resultat" in v},
                      "registres_entiers": {k: {kk: (vv["resultat"] if isinstance(vv, dict) and "resultat" in vv else vv)
                                                for kk, vv in g[k].items() if kk != "chemin"}
                                           for k in ("f_arbre_du_depot_prive", "g_main_e12540bf", "g_main_db454552",
                                                     "g_canal_conv_audit_n04_e4fd3690", "g_canal_conv_audit_n04_3f132371",
                                                     "g_canal_conv_audit_n04_c8c34784", "g_premiere_course_canal_e9d7b78d")},
                      "empreintes": r["empreintes_du_code"], "marqueurs": r["marqueurs"], "blocs": r["blocs"],
                      "renvois_non_conformes": r["renvois_des_passages_neufs"]["non_conformes"],
                      "renvois_v3": r["renvois_v3_dans_tout_le_brouillon"], "difference": r["difference"], "copie": r["copie"]},
                     ensure_ascii=False, indent=1, default=str))


if __name__ == "__main__":
    main(sys.argv[1:])
