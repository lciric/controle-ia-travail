#!/usr/bin/env python3
"""Test de mort par programme en monde planté — v3 (contre-lecture de la v3 des pièces : (1) empreinte du juge écrite ici
en dur, plus lue dans son propre compagnon ; (2) juge v2 qui vérifie l'évaluateur de la grammaire à son empreinte, épreuve H ;
(3) sortie indépendante de l'emplacement des pièces : les motifs de refus sont rendus par leur catégorie, jamais par un
texte qui porte un chemin ou l'empreinte d'un juge muté — le rejeu long se compare depuis le commit). Règle inchangée.
Texte de la v2 : le juge tourne dans un **processus isolé**
(`juge_test_de_mort_isole_v2.py`, empreinte gelée ci-dessous). Aucun appel de modèle, aucun réseau, aucune dépense.

Ce qui change par rapport à la v1 (dossier inachevé, `test_de_mort_programme_v1.py`, `eaea7c8c…`), dont la règle est gardée :
la garde de la v1 (crochet d'audit et profil dans le même processus) ne voit pas un juge qui lit une loi **déjà en mémoire**
(fermeture sur la loi du monde compilée, sans appel de fonction interdite ni ouverture de fichier). L'épreuve E5 ci-dessous
le montre sur la v1 (le juge fautif passe). En v2, le juge démarre dans un interprète vide : la loi plantée n'y existe pas, il ne
reçoit que (cartes, tranches, empreinte des tranches) et sa propre garde interne refuse toute autre lecture.

Rôles :
1. **Fournisseur de tranches** (côté noyau, seul à lire le monde) : tire des épisodes tenus à l'écart (graines propres), les écrit
   en JSON, rend l'empreinte. Même procédé que `M.test_de_mort` (instances, puis issues tirées du monde).
2. **Juge isolé** : réplication sur ces données seules ; s ≥ 0,02 ⇒ « survit ».

Épreuves, sur les 12 mondes MR-2 de développement (calibration ; aucun monde neuf du pilote) :
- E1 équivalence : sur les mêmes épisodes, le juge isolé rend exactement la statistique de `M.test_de_mort` (qui tire ses issues
  de la loi vraie dans le même processus), pour toutes les cartes (objets de contrôle et jeu planté) ;
- E2 cas sains : loi du monde (doit survivre), trois fausses par construction (uniforme, marginale fixe, monde inversé : doivent
  être éliminées), copie de K1 (contre la marginale : doit survivre), sur 20 tranches tenues à l'écart ;
- E3 accord avec l'oracle (gain contre la marginale ≥ 0,02), sur les 20 tranches ;
- E4 artefacts (doivent être refusés) : (A) juge muté qui ouvre la partie scellée du monde ; (B) juge muté qui importe le
  générateur des mondes ; (C) juge muté qui relit le monde par un sous-processus ; (D) carte en forme de devis de monde ;
  (E) juge dont l'empreinte diffère de l'empreinte gelée ; (F) argument en plus (chemin du devis) ; (G) empreinte de tranche fausse ;
- E5 l'artefact « fermeture en mémoire » : passe la garde de la v1 (constat), impossible à écrire en v2 (le juge ne reçoit
  que des fichiers) : on éprouve le seul canal restant, la carte, par (D).
Les artefacts A, B, C sont joués sans le contrôle d'empreinte (sinon E le refuserait d'abord) : ils éprouvent la garde interne.

Graines : SeedSequence(20261122, spawn_key=(tâche, monde, …)) — tâche 3 tranches tenues à l'écart, 4 équivalence (mêmes
clés que la v1).
Usage : python -I -B test_de_mort_programme_v3.py SORTIE.json DOSSIER_TRAVAIL_NEUF [MONDES…]
"""
import datetime
import json
import os
import subprocess
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import racine_depot_v1 as R  # noqa: E402

B = R.charger_bases_v1()
M = B.M
T1_REL = ("docs/notes/organisme-essaim-communicant-v1/en-cours-inacheve-2026-11-22-0700/"
          "essaim-glouton-renforce-test-de-mort-v1/test_de_mort_programme_v1.py")
T1_SHA = "eaea7c8c5f245cc503a4e113e7b68a98e75698b39c51b4a3baf4c82e47656724"
T1 = R.charger_reloge(T1_REL, T1_SHA, [(f'V1_DOSSIER = "{R.CHEMIN_ABSOLU_HISTORIQUE}/docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1"',
                                        f'V1_DOSSIER = {R.chemin("docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v1")!r}')],
                      "test_de_mort_programme_v1")
JUGE = os.path.join(ICI, "juge_test_de_mort_isole_v2.py")
JUGE_SHA = "ee0f68a19cea986ffb82c08ba59319924b121360ee10c74a05d4c379fffe0985"  # écrite à la main (v3)
RACINE_GRAINES = 20261122
N_TRANCHE = 400
REPETITIONS = 20


class LectureRefusee(Exception):
    pass


def geler_juge():
    s = R.sha_fichier(JUGE)
    if s != JUGE_SHA:
        raise SystemExit(f"refus : juge d'empreinte {s}, gelée {JUGE_SHA}")


def rng_tache(*cle):
    return np.random.default_rng(np.random.SeedSequence(RACINE_GRAINES, spawn_key=tuple(int(x) for x in cle)))


def fournir_tranches(loi_monde, D, nsp, rngs, chemin):
    tr = {}
    for nom, rng in rngs.items():
        Z, G = M.tirer_instances(rng, N_TRANCHE, D, nsp)
        Y = M.tirer_issues(rng, M.probas(loi_monde, Z, G))
        tr[nom] = {"Z": Z.tolist(), "G": G.tolist(), "Y": Y.tolist()}
    octets = json.dumps({"version": "tranches-test-de-mort-v2", "n": N_TRANCHE, "tranches": tr}, separators=(",", ":")).encode()
    with open(chemin, "xb") as f:
        f.write(octets)
    import hashlib
    return hashlib.sha256(octets).hexdigest()


def lancer_enfant(script, cartes, chemin_tranches, sha_tranches, dossier, etiquette):
    ch_c = os.path.join(dossier, f"cartes-{etiquette}.json")
    with open(ch_c, "x", encoding="utf-8") as f:
        json.dump(cartes, f, ensure_ascii=False)
    env = {"DEPOT_CONTROLE_IA": R.RACINE, "PATH": "/usr/bin:/bin"}
    p = subprocess.run([sys.executable, "-I", "-B", script, ch_c, chemin_tranches, sha_tranches], capture_output=True, text=True,
                       env=env, timeout=600)
    try:
        rendu = json.loads(p.stdout.strip().splitlines()[-1])
    except (IndexError, json.JSONDecodeError):
        rendu = {"refus": "sortie illisible", "stderr": p.stderr[-300:]}
    if p.returncode != 0 or "verdicts" not in rendu:
        raise LectureRefusee(f"code {p.returncode} : {rendu}")
    return rendu["verdicts"]


def juger_isole(cartes, chemin_tranches, sha_tranches, dossier, etiquette, script=JUGE, **en_plus):
    """Seule voie permise : empreinte du juge vérifiée, aucun argument en plus."""
    if en_plus:
        raise LectureRefusee(f"argument(s) en plus refusé(s) : {sorted(en_plus)}")
    if R.sha_fichier(script) != JUGE_SHA:
        raise LectureRefusee("juge d'empreinte ≠ gelée")
    return lancer_enfant(script, cartes, chemin_tranches, sha_tranches, dossier, etiquette)


def juge_mute(dossier, nom, code, remplacer=()):
    texte = open(JUGE, encoding="utf-8").read()
    for a, b in remplacer:
        assert texte.count(a) == 1
        texte = texte.replace(a, b)
    marque = "        # POINT-DE-MUTATION (épreuves de la garde interne)\n"
    assert texte.count(marque) == 1
    ici = "ICI = os.path.dirname(os.path.abspath(__file__))\n"
    assert texte.count(ici) == 1
    texte = texte.replace(ici, f"ICI = {ICI!r}  # juge muté écrit hors de son dossier : il importe la racine depuis le dossier du juge\n")
    ch = os.path.join(dossier, f"juge-mute-{nom}.py")
    with open(ch, "x", encoding="utf-8") as f:
        f.write(texte.replace(marque, marque + "".join("        " + l + "\n" for l in code)))
    return ch


def vers_json(loi):
    return json.loads(json.dumps(loi, default=lambda o: o.tolist() if hasattr(o, "tolist") else float(o)))


def courir_monde(r, dossier, artefacts):
    spec, info = B.regenerer(r)
    oc = B.OracleCache(spec, r)
    W = M.compiler_monde(spec)
    D, nsp = spec["dimension"], spec["sous_populations"]
    cartes, _ = T1.cartes_du_monde(spec, oc)
    noms = sorted(cartes)
    liste = [{"nom": nm, "loi": vers_json(cartes[nm][0])} for nm in noms]
    ch_eq = os.path.join(dossier, f"tranches-equivalence-monde-{r}.json")
    sha_eq = fournir_tranches(W, D, nsp, {nm: rng_tache(4, r, k) for k, nm in enumerate(noms)}, ch_eq)
    ch_te = os.path.join(dossier, f"tranches-tenues-a-l-ecart-monde-{r}.json")
    sha_te = fournir_tranches(W, D, nsp, {f"rep-{q}": rng_tache(3, r, q) for q in range(REPETITIONS)}, ch_te)
    v_eq = juger_isole(liste, ch_eq, sha_eq, dossier, f"eq-{r}")
    v_te = juger_isole(liste, ch_te, sha_te, dossier, f"te-{r}")
    res = {}
    for k, nm in enumerate(noms):
        loi, attendu = cartes[nm]
        ancien = M.test_de_mort(loi, W, D, nsp, rng_tache(4, r, k))
        prog = v_eq[nm][nm]
        reps = [v_te[nm][f"rep-{q}"] for q in range(REPETITIONS)]
        g = oc.o.gain(loi)
        att_o = "survit" if g >= T1.SEUIL else "éliminée"
        res[nm] = {"attendu_par_construction": attendu, "attendu_oracle": att_o, "gain_oracle_contre_marginale": round(g, 6),
                   "equivalence_ecart": abs(ancien[0] - prog["statistique"]),
                   "equivalence_verdict": (prog["verdict"] == "survit") == bool(ancien[1]),
                   "survie_sur_20": sum(x["verdict"] == "survit" for x in reps),
                   "accord_oracle_sur_20": sum(x["verdict"] == att_o for x in reps)}
        if attendu is not None:
            res[nm]["controle_tenu_sur_20"] = sum(x["verdict"] == attendu for x in reps)
    out = {"tranches": {"equivalence": [os.path.basename(ch_eq), sha_eq], "tenues_a_l_ecart": [os.path.basename(ch_te), sha_te]}, "cartes": res}
    if artefacts:
        out["artefacts"] = jouer_artefacts(r, spec, W, liste, ch_te, sha_te, dossier)
    return out


def jouer_artefacts(r, spec, W, liste, ch_te, sha_te, dossier):
    partie = R.chemin(f"docs/notes/organisme-multi-generations-v1/sorties-v4/partie-v4-monde-{r}.json")
    sain = liste[:2]
    res = {}

    def essai(nom, f, motif_attendu=None):
        """Refus compté seulement si son motif est celui de la garde visée (un plantage n'est pas un refus de garde)."""
        try:
            f()
            res[nom] = {"refuse": False}
        except LectureRefusee as ex:
            m = str(ex)
            ok = motif_attendu is None or motif_attendu in m
            # v3 : catégorie seulement (aucun chemin ni empreinte dépendant de l'emplacement)
            res[nom] = {"refuse": ok, "motif": motif_attendu if ok else "motif inattendu"}

    essai("sain-juge-gele", lambda: juger_isole(sain, ch_te, sha_te, dossier, f"sain-{r}"))
    mA = juge_mute(dossier, f"A-{r}", [f"open({partie!r}, 'rb').read()"])
    essai("A-ouvre-la-partie-du-monde", lambda: lancer_enfant(mA, sain, ch_te, sha_te, dossier, f"A-{r}"), 'ouverture refusée')
    mB = juge_mute(dossier, f"B-{r}", ["import generateur_mondes_v2"])
    essai("B-importe-le-generateur", lambda: lancer_enfant(mB, sain, ch_te, sha_te, dossier, f"B-{r}"), 'import refusé')
    mC = juge_mute(dossier, f"C-{r}", ["import os as _o", f"_o.system('cat {partie} > /dev/null')"])
    essai("C-sous-processus", lambda: lancer_enfant(mC, sain, ch_te, sha_te, dossier, f"C-{r}"), 'évènement refusé : os.system')
    essai("D-carte-en-forme-de-devis", lambda: juger_isole([{"nom": "devis", "loi": vers_json(spec)}], ch_te, sha_te, dossier, f"D-{r}"), 'carte en forme de devis')
    essai("E-juge-d-empreinte-differente", lambda: juger_isole(sain, ch_te, sha_te, dossier, f"E-{r}", script=mA), '≠ gelée')
    essai("F-argument-en-plus", lambda: juger_isole(sain, ch_te, sha_te, dossier, f"F-{r}", monde=partie), 'argument(s) en plus')
    essai("G-empreinte-de-tranche-fausse", lambda: juger_isole(sain, ch_te, "0" * 64, dossier, f"G-{r}"), 'empreinte des tranches')
    mH = juge_mute(dossier, f"H-{r}", [], remplacer=[('EVALUATEUR_SHA256 = "1825b956eed638fe4daf3d7395a169fdbdf7c9679076d9ba3fb4a15cfd7ec85e"',
                                                       'EVALUATEUR_SHA256 = "' + "0" * 64 + '"')])
    essai("H-evaluateur-d-empreinte-differente", lambda: lancer_enfant(mH, sain, ch_te, sha_te, dossier, f"H-{r}"), "évaluateur d'empreinte différente")
    # E5 : la garde de la v1 laisse passer un juge qui lit la loi du monde déjà en mémoire (fermeture)
    t0 = json.loads(open(ch_te, "rb").read().decode())["tranches"]["rep-0"]

    def juge_fermeture(loi, chemin, sha_attendu, nom):
        Z, G = np.asarray(t0["Z"]), np.asarray(t0["G"])
        Q, P = M.probas(W, Z, G), M.probas(loi, Z, G)  # W : loi plantée, capturée en mémoire
        s = float((Q * (np.log(np.maximum(P, M.PLANCHER)) - np.log(Q.mean(axis=0)))).sum(axis=1).mean())
        return {"verdict": "survit" if s >= T1.SEUIL else "éliminée", "statistique": s}
    try:
        T1.juger_sous_garde(juge_fermeture, W, ch_te, sha_te, "rep-0")
        res["E5-fermeture-en-memoire-sous-garde-v1"] = {"refuse": False, "constat": "la garde de la v1 ne la voit pas"}
    except T1.LectureLoiRefusee as ex:
        res["E5-fermeture-en-memoire-sous-garde-v1"] = {"refuse": True, "motif": "garde v1"}
    return res


def main(argv):
    if len(argv) < 3 or os.path.exists(argv[1]) or os.path.exists(argv[2]):
        print("usage : test_de_mort_programme_v3.py SORTIE.json DOSSIER_TRAVAIL (neufs) [MONDES…]", file=sys.stderr)
        return 2
    geler_juge()
    os.makedirs(argv[2])
    mondes = [int(x) for x in argv[3:]] or list(range(12))
    debut = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    par_monde = {}
    for r in mondes:
        par_monde[str(r)] = courir_monde(r, argv[2], artefacts=True)
        pm = par_monde[str(r)]
        print(r, {k: v.get("controle_tenu_sur_20") for k, v in pm["cartes"].items() if k.startswith("CTRL")},
              {k: v["refuse"] for k, v in pm["artefacts"].items()}, flush=True)
    toutes = [v for pm in par_monde.values() for v in pm["cartes"].values()]
    ctrl = [(nm, v) for pm in par_monde.values() for nm, v in pm["cartes"].items() if v["attendu_par_construction"] is not None]
    noms_art = list(next(iter(par_monde.values()))["artefacts"])
    attendu_art = {n: (n not in ("sain-juge-gele", "E5-fermeture-en-memoire-sous-garde-v1")) for n in noms_art}
    resume = {"equivalence_ecart_max": max(v["equivalence_ecart"] for v in toutes),
              "equivalence_verdicts_egaux": [sum(v["equivalence_verdict"] for v in toutes), len(toutes)],
              "controles_tenus_sur_20": {nm: [sum(v["controle_tenu_sur_20"] for n2, v in ctrl if n2 == nm), REPETITIONS * sum(1 for n2, _ in ctrl if n2 == nm)]
                                         for nm in sorted({n for n, _ in ctrl})},
              "accord_avec_oracle": [sum(v["accord_oracle_sur_20"] for v in toutes), REPETITIONS * len(toutes)],
              "artefacts_refuses_par_monde": {n: sum(pm["artefacts"][n]["refuse"] for pm in par_monde.values()) for n in noms_art},
              "artefacts_comme_attendu": all(pm["artefacts"][n]["refuse"] == attendu_art[n] for pm in par_monde.values() for n in noms_art),
              "attendu_artefacts": {n: ("refusé" if a else ("passe (cas sain)" if n == "sain-juge-gele" else "passe sous la v1 (constat du défaut)")) for n, a in attendu_art.items()},
              "mondes": len(par_monde)}
    out = {"version": "test-de-mort-programme-v3", "debut_utc": debut, "fin_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "script_sha256": R.sha_fichier(os.path.abspath(__file__)), "juge_sha256": JUGE_SHA, "racine_sha256": R.sha_fichier(R.__file__),
           "v1": {"chemin": T1_REL, "sha256": T1_SHA}, "bases_v1_sha256": B.SHA_SOURCE_SCELLEE, "imports_sha256": B.IMPORTS,
           "python": sys.version.split()[0], "numpy": np.__version__,
           "regle": {"n": N_TRANCHE, "seuil": T1.SEUIL, "statistique": "moyenne de log p_carte(y) − log m̂(y), m̂ = comptes + 0,5", "survit_si": "s ≥ 0,02"},
           "graines": "SeedSequence(20261122, spawn_key=(tâche, monde, carte|répétition)) ; tâche 3 tenues à l'écart, 4 équivalence",
           "mondes": mondes, "mondes_nature": "12 mondes MR-2 de développement (calibration)", "resume": resume, "par_monde": par_monde}
    with open(argv[1], "x", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
    print(json.dumps(resume, ensure_ascii=False, indent=1))
    ok = resume["artefacts_comme_attendu"] and resume["equivalence_ecart_max"] == 0.0
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
