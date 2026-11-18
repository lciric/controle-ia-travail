#!/usr/bin/env python3
"""Contrôles du contre-lecteur (modèle J) sur la phase 0 de P3 — pièce de `contre-lecture-phase0-p3-v1.md`. Fichier neuf.

Aucun lancement sur la configuration du préenregistrement (H = 65 536, racine 20261118) : petits mondes d'essai
seulement (racines 1001 à 1008 avec H = 4 096 ; racines 2001 et 2002 avec H = 16 384 ; sondes 512 et 128), fonctions de
garde appelées directement, lanceur joué de bout en bout en mode d'essai seulement (H = 256, sources fabriquées).
Aucun appel réseau, aucun appel de modèle, aucune dépense. Déterministe (graines écrites ci-dessous).

Usage : python3 -B contre-lecture-phase0-p3-v1-controles.py DOSSIER_TEMPORAIRE_NEUF_HORS_DEPOT
Sections : A (bloc gelé, puissance, devis, sensibilités) ; B (gardes du lanceur sur des copies hors dépôt) ;
C (questionneurs qui ne voient que K et le panorama ; asymétrie monde / leurre ; rôles tirés à pile ou face) ;
E (la règle gelée elle-même, simulée à 1 088 mondes).
"""
import hashlib
import json
import math
import os
import shutil
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))

import numpy as np  # noqa: E402

import lanceur_phase0_p3_v1 as L  # noqa: E402
import panorama_p3_v1 as pp  # noqa: E402
import mondes_reponses_p1p2_v1 as mr  # noqa: E402
import questionneurs_p1_v2 as qp  # noqa: E402

K, SEUIL, N = 8, 0.30, 1088
ZA, ZB = pp._z(0.9875), pp._z(0.9)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# --- A : bloc gelé, puissance, devis ------------------------------------------------------------------------------------
def section_a():
    print("=== A. Bloc gelé, puissance, devis ===")
    nom = L.NOM_PREENREGISTREMENT
    txt = (ICI / nom).read_text(encoding="utf-8")
    print("empreinte du préenregistrement :", sha(ICI / nom), "| attendue par le lanceur :", L.EMPREINTE_PREENREGISTREMENT)
    e = L.empreinte_bloc_effort(L.CONFIG)
    i = txt.index("```\n{") + 4
    recopie = json.loads(txt[i:txt.index("```", i)])
    print("bloc gelé :", e, "| porté par le texte :", e in txt, "| bloc recopié égal au bloc calculé :",
          recopie == json.loads(L.l1.canon(L.bloc_effort(L.CONFIG))))
    t = L.puissance(L.CONFIG)
    print("tailles par issue :", {k: round(v, 2) for k, v in t["n_par_issue"].items()}, "| retenue :", t["n_retenu_prudent"],
          "| optimiste :", t["n_optimiste_ordres_independants"], "| z :", round(t["z_niveau"], 4))
    print("devis :", pp.devis(1088, L.CONFIG["p3"]["devis"]["prix_usd_par_appel"], 4, 0.1))
    print("taille « au niveau » selon le taux de base commun p de la cible dans C et B (D = 0, indicatrices indépendantes) :")
    for p in (0.125, 0.2, 0.25, 0.3, 0.5):
        v = 2 * p * (1 - p)
        print(f"  p = {p} : variance {v:.5f} ; ordres corrélés {v * ((ZA + ZB) / 0.05) ** 2:.0f} ; indépendants "
              f"{v / 2 * ((ZA + ZB) / 0.05) ** 2:.0f}")
    print("taille « au niveau » selon la marge (p = 1/8, ordres corrélés) :",
          {d: round(0.21875 * ((ZA + ZB) / d) ** 2) for d in (0.03, 0.04, 0.05, 0.0625, 0.075, 0.1)})


# --- B : gardes du lanceur, sur des copies hors dépôt ---------------------------------------------------------------------
def section_b(T):
    print("=== B. Gardes du lanceur (copies hors dépôt ; jamais la configuration réelle de bout en bout) ===")
    E = L.EMPREINTE_PREENREGISTREMENT

    def essai(nom, f):
        try:
            r = f()
            print(f"ACCEPTÉ  {nom} → {r if not isinstance(r, dict) else r.get('verdict')}")
        except L.REFUS as e:
            print(f"REFUS    {nom} → {str(e)[:96]}")

    nom = L.NOM_PREENREGISTREMENT
    c = T / nom
    shutil.copy(ICI / nom, c)
    shutil.copy(ICI / (nom + ".sha256"), T / (nom + ".sha256"))
    essai("B1 copie conforme du préenregistrement, compagnon copié (cas sain)", lambda: L.l1.exiger_preenregistrement(c, E, True)[:12])
    b = bytearray(c.read_bytes())
    i = b.index(b"0,05")
    b[i + 3:i + 4] = b"6"
    c.write_bytes(bytes(b))
    essai("B1 un octet changé (0,05 → 0,06), compagnon d'origine", lambda: L.l1.exiger_preenregistrement(c, E, True))
    (T / (nom + ".sha256")).write_text(f"{sha(c)}  {nom}\n")
    essai("B1 un octet changé, compagnon refait", lambda: L.l1.exiger_preenregistrement(c, E, True))
    shutil.copy(ICI / nom, c)
    (T / (nom + ".sha256")).write_text(f"{'0' * 64}  {nom}\n")
    essai("B1 texte intact, compagnon faux", lambda: L.l1.exiger_preenregistrement(c, E, True))
    os.remove(T / (nom + ".sha256"))
    essai("B1 texte intact, compagnon absent", lambda: L.l1.exiger_preenregistrement(c, E, True))
    cfg = json.loads(json.dumps(L.CONFIG))
    cfg["p3"]["delta_equivalence"] = 0.06
    essai("B1 configuration à marge 0,06 contre le texte scellé (bloc gelé)", lambda: L.exiger_bloc_effort(ICI / nom, cfg))
    essai("B1 configuration à marge 0,06 (taille de la puissance)", lambda: L.exiger_puissance(cfg)["n_retenu_prudent"])

    def cl(n, texte, sceller=True):
        f = T / n
        f.write_text(texte, encoding="utf-8")
        if sceller:
            (T / (n + ".sha256")).write_text(f"{sha(f)}  {n}\n")
        return f

    v = "\n\n## Verdict\n\n"
    essai("B2 contre-lecture absente", lambda: L.exiger_contre_lecture(None, E))
    essai("B2 chemin inexistant", lambda: L.exiger_contre_lecture(T / "rien.md", E))
    essai("B2 « Scellable », empreinte citée, non scellée", lambda: L.exiger_contre_lecture(cl("a.md", f"relu {E}{v}**Scellable.**\n", False), E))
    essai("B2 « Scellable », scellée, empreinte citée (cas sain)", lambda: L.exiger_contre_lecture(cl("b.md", f"relu {E}{v}**Scellable.**\n"), E))
    essai("B2 « Non scellable »", lambda: L.exiger_contre_lecture(cl("c.md", f"relu {E}{v}**Non scellable.**\n"), E))
    essai("B2 « Scellable après corrections »", lambda: L.exiger_contre_lecture(cl("d.md", f"relu {E}{v}**Scellable après corrections.**\n"), E))
    essai("B2 « Scellable » qui cite une autre empreinte", lambda: L.exiger_contre_lecture(cl("e.md", f"relu {'a' * 64}{v}**Scellable.**\n"), E))
    essai("B2 gras partiel « **Scellable** après corrections (…) »", lambda: L.exiger_contre_lecture(cl("f.md", f"relu {E}{v}**Scellable** après corrections (voir C-1 à C-4).\n"), E))
    essai("B2 gras partiel « **Scellable** seulement si le devis est retiré ; sinon non scellable »", lambda: L.exiger_contre_lecture(cl("g.md", f"relu {E}{v}**Scellable** seulement si le devis est retiré ; sinon non scellable.\n"), E))
    essai("B2 sans gras « Scellable après corrections »", lambda: L.exiger_contre_lecture(cl("h.md", f"relu {E}{v}Scellable après corrections.\n"), E))
    essai("B2 verdict en tableau", lambda: L.exiger_contre_lecture(cl("i.md", f"relu {E}{v}| partie | verdict |\n|---|---|\n| texte | non scellable |\n"), E))
    essai("B2 empreinte citée pour dire qu'elle n'a pas été relue", lambda: L.exiger_contre_lecture(cl("j.md", f"## Verdict\n\n**Scellable.**\n\nTexte relu : {'b' * 64} (et non {E}).\n"), E))
    # bout en bout, mode d'essai, petit monde, sources fabriquées
    cfg = json.loads(json.dumps(L.CONFIG))
    cfg["racine_graines"] = 31337
    cfg["p3"].update({"taille_espace_H": 256, "sonde_questions": 256, "sonde_score": 64, "questions_T": 8, "points_de_carte": [0, 4, 8],
                      "mondes": 64, "mondes_kl": 16, "limite_lois_sans_leurre": 256, "tirages_bootstrap": 300})
    pv = T / "v67.json"
    pv.write_text(json.dumps({"releve": {"plantees": [{"nom": "V1", "loi": {"type": "fixe", "probas": [0.2, 0.3, 0.5]}}], "cartes": []}}))
    pr = T / "prereg-essai.md"
    pr.write_text("essai ; bloc : " + L.empreinte_bloc_effort(cfg) + "\n")
    (T / "prereg-essai.md.sha256").write_text(f"{sha(pr)}  prereg-essai.md\n")
    ev = L.EVALUATEUR_ORGANISME
    ess = {"preenregistrement": sha(pr), "controle_du_code": True, "contre_lecture_exigee": True, "compagnon_du_preenregistrement_exige": True,
           "puissance_exigee": False, "config": cfg, "evaluateur": [ev, sha(ev)], "sources": {"v67": [str(pv), sha(pv)]}}
    pe = T / "essais.json"
    pe.write_text(json.dumps(ess))

    def lancer(n, extra):
        out = T / ("sortie-" + n)
        sys.stdout.flush()
        code = L.principal(["--sortie", str(out), "--preenregistrement", str(pr), "--essai", "--essais-json", str(pe)] + extra)
        print(f"B3 bout en bout, mode d'essai [{n}] : code {code} ; dossier de sortie écrit : {out.exists()}")
        return out

    ep = sha(pr)
    lancer("sans contre-lecture", [])
    lancer("contre-lecture « non scellable »", ["--contre-lecture", str(cl("k.md", f"relu {ep}{v}**Non scellable.**\n"))])
    lancer("contre-lecture « scellable après corrections »", ["--contre-lecture", str(cl("l.md", f"relu {ep}{v}**Scellable après corrections.**\n"))])
    ok = cl("m.md", f"relu {ep}{v}**Scellable.**\n")
    pr.write_text(pr.read_text() + " ")
    lancer("préenregistrement altéré d'un octet, contre-lecture favorable", ["--contre-lecture", str(ok)])
    pr.write_text(pr.read_text()[:-1])
    out = lancer("cas sain", ["--contre-lecture", str(ok)])
    res = json.loads((out / "sortie-phase0-p3-v1.json").read_text())
    man = json.loads((out / "manifeste-phase0-p3-v1.json").read_text())
    print("   cas sain : essai =", res["essai"], "|", res["p3"]["verdict_propose_par_le_code"][:62], "| hasard :",
          res["p3"]["lectures_trois_issues"]["hasard"]["issue"], "| commit au manifeste :", (man["commit"] or "")[:8],
          "| tâches de graines :", len(man["graines"]["taches"]), "| numpy", man["versions"]["numpy"])
    quasi = json.loads(json.dumps(L.CONFIG))
    quasi["p3"]["devis"]["reprises"] = 0.11
    print("B4 le mode d'essai accepterait la configuration réelle à un champ sans portée près (devis.reprises 0,11) :",
          L.empreinte_bloc_effort(quasi) != L.empreinte_bloc_effort(L.CONFIG), "(non lancé)")


# --- C : questionneurs sans vérité, sur petits mondes -----------------------------------------------------------------------
class SansVerite(pp.QuestionneurCarte):
    """Ne lit que l'état (K et le panorama) ; `simule_verite` est faux : le banc ne lui passe aucune vérité."""
    nom = "sans-verite"

    def __init__(self, rng, regle, sonde):
        super().__init__(rng)
        self.regle, self.sonde = regle, sonde

    def choisir_carte(self, etat, verite=None):
        assert verite is None and sorted(etat) == ["K", "panorama"]
        lois = etat["panorama"]
        if self.regle == "moins de noeuds":
            return int(np.argmin([pp.noeuds(l) for l in lois]))
        if self.regle == "seul de son type de racine":
            ts = [l["type"] for l in lois]
            u = [k for k, t in enumerate(ts) if ts.count(t) == 1] or list(range(etat["K"]))
            return int(u[int(self.rng.integers(len(u)))])
        if self.regle == "hachage du contenu":
            return int(np.argmin([int.from_bytes(hashlib.sha256(mr.canon(l).encode()).digest()[:8], "big") for l in lois]))
        P = [mr.proba_vec(l, *self.sonde) for l in lois]  # sonde propre au questionneur, tirée par sa graine
        if self.regle in ("loi la plus plate", "loi la plus tranchee"):
            h = [float(-(p * np.log(p)).sum(axis=1).mean()) for p in P]
            return int(np.argmax(h) if self.regle == "loi la plus plate" else np.argmin(h))
        kl = np.array([[0.0 if a is b else mr.kl_moyenne(a, b) for b in P] for a in P])
        moy = (kl.sum(axis=0) + kl.sum(axis=1)) / (2 * (len(P) - 1))
        return int(np.argmin(moy) if self.regle == "loi la plus centrale du panorama" else np.argmax(moy))


REGLES = ("loi la plus plate", "loi la plus centrale du panorama", "loi la plus tranchee", "loi la plus peripherique",
          "hachage du contenu", "moins de noeuds", "seul de son type de racine")


def petit_monde(R, H):
    g = lambda nom: mr.generateur(nom, R)  # noqa: E731
    sq, ss = mr.tirer_sonde(g("j/sq"), 512), mr.tirer_sonde(g("j/ss"), 128)
    espace = qp.construire_espace(g("j/espace"), H, sq, ss)
    fams, index = pp.index_familles(espace)
    mondes, leurres, ecartes = pp.tirer_mondes_avec_leurre(espace, fams, index, N, g("j/mondes"), lambda w: g(f"j/leurre/{w}"), SEUIL, H)
    pos = pp.plan_positions(g("j/plan"), N, K)
    pp.exiger_plan_equilibre(pos, K)
    pans = []
    for i, (w, l, p) in enumerate(zip(mondes, leurres, pos)):
        remp = pp.choisir_remplisseurs(espace, w, l, fams, g(f"j/remp/{i}"), K - 1, SEUIL)
        pan = pp.construire_panorama(w, l, remp, int(p), K)
        pp.exiger_panorama(pan, fams, K, espace, SEUIL)
        pans.append(pan)
    return g, espace, fams, index, pans, ecartes


def jouer(g, espace, pans, regle, etiquette):
    sonde = mr.tirer_sonde(g(f"j/sonde-du-questionneur/{regle}"), 128)
    cC, cB = np.zeros((len(pans), 2)), np.zeros((len(pans), 2))
    for i, pan in enumerate(pans):
        for j, ordre in enumerate((1, 2)):
            p = pp.position_presentee(pan["position"], ordre, K)
            for bras, c in (("C", cC), ("B", cB)):
                lois = [espace["lois"][x] for x in pp.presenter(pan[bras], ordre)]
                q = SansVerite(g(f"j/carte/{etiquette}/{regle}/{bras}/{ordre}/{i}"), regle, sonde)
                k, _ = pp.jouer_carte(q, lois, {"position_vraie": p, "famille_monde": None})
                c[i, j] = int(k == p)
    return cC, cB


def section_c():
    print("=== C. Questionneurs qui ne voient que K et le panorama (aucune vérité du banc), petits mondes ===")
    reunion = {}
    for H, racines in ((4096, range(1001, 1009)), (16384, (2001, 2002))):
        for R in racines:
            g, espace, fams, index, pans, ecartes = petit_monde(R, H)
            meme_type = sum(fams[x][0] == fams[pan["monde"]][0] for pan in pans for k, x in enumerate(pan["C"]) if k != pan["position"])
            touches = sum(any(fams[x][0] == fams[pan["monde"]][0] for k, x in enumerate(pan["C"]) if k != pan["position"]) for pan in pans)
            ent = -(espace["P"] * espace["L"]).sum(axis=1) / espace["N"]
            ew, el = ent[[p["monde"] for p in pans]], ent[[p["leurre"] for p in pans]]
            er = ent[[x for p in pans for k, x in enumerate(p["C"]) if k != p["position"]]]
            sous = range(0, N, 8)

            def part_distinctes(a):
                autres = [int(c) for c in index[fams[a]] if int(c) != a]
                return sum(pp.distinctes(espace, a, c, SEUIL) for c in autres) / len(autres)

            dw = np.mean([part_distinctes(pans[i]["monde"]) for i in sous])
            dl = np.mean([part_distinctes(pans[i]["leurre"]) for i in sous])
            print(f"racine {R}, H = {H} : {len(index)} familles ; {ecartes} lois écartées faute de leurre ; remplisseurs de même "
                  f"type de racine que le monde : {meme_type} sur {7 * N} ({touches} panoramas sur {N}) ; entropie moyenne monde "
                  f"{ew.mean():.4f}, leurre {el.mean():.4f}, remplisseurs {er.mean():.4f} ; part des lois de la famille distinctes "
                  f"du monde {dw:.4f}, du leurre {dl:.4f}")
            for regle in REGLES:
                cC, cB = jouer(g, espace, pans, regle, "construit")
                r = pp.trois_issues(cC, cB, g(f"j/boot/{regle}"), 2000, 0.975, 0.05, K)
                d2 = cC - cB
                corr = float(np.corrcoef(d2[:, 0], d2[:, 1])[0, 1]) if d2[:, 0].std() > 0 and d2[:, 1].std() > 0 else float("nan")
                print(f"   {regle:34s} C {r['taux_C']['point']:.4f} B {r['taux_B']['point']:.4f} D {r['ecart_D']['point']:+.4f} "
                      f"[{r['ecart_D']['ic'][0]:+.4f} ; {r['ecart_D']['ic'][1]:+.4f}] → {r['issue']} (corrélation des ordres {corr:.2f})")
                reunion.setdefault((H, regle), []).append((cC, cB, r["issue"]))
            # contrôle : rôles (monde, leurre) tirés à pile ou face après le tirage de la paire (échangeables par construction)
            pile = g("j/roles").random(len(pans)) < 0.5
            sym = [pp.construire_panorama(p["leurre"], p["monde"], [x for k, x in enumerate(p["C"]) if k != p["position"]], p["position"], K)
                   if s else p for p, s in zip(pans, pile)]
            for p in sym:
                pp.exiger_panorama(p, fams, K, espace, SEUIL)
            for regle in REGLES[:2]:
                cC, cB = jouer(g, espace, sym, regle, "pile-ou-face")
                reunion.setdefault((H, regle + " — rôles à pile ou face"), []).append((cC, cB, None))
            sys.stdout.flush()
    print("--- réunions (par taille d'espace) ---")
    for (H, regle), l in reunion.items():
        cC, cB = np.concatenate([x[0] for x in l]), np.concatenate([x[1] for x in l])
        d = (cC - cB).mean(axis=1)
        se = d.std(ddof=1) / math.sqrt(len(d))
        issues = [x[2] for x in l if x[2]]
        compte = {i: issues.count(i) for i in pp.ISSUES if issues.count(i)}
        print(f"H = {H:5d} {regle:58s} n = {len(d):5d} C {cC.mean():.4f} B {cB.mean():.4f} D {d.mean():+.4f} ± {se:.4f} "
              f"(z = {d.mean() / se if se > 0 else float('nan'):+.2f}) ; variance d'une unité {d.var(ddof=1):.4f} → taille « au niveau » "
              f"{d.var(ddof=1) * ((ZA + ZB) / 0.05) ** 2:.0f} ; issues par monde d'essai à 1 088 mondes : {compte}")


# --- E : la règle gelée elle-même, simulée ----------------------------------------------------------------------------------
def section_e():
    print("=== E. Règle gelée elle-même (`trois_issues` : rééchantillonnage, inverted_cdf), 400 répétitions, 1 088 mondes ===")
    rng = np.random.default_rng(424242)
    h = 1 / K

    def sim(pc, pb, correles, reps=400, B=2000):
        c = {i: 0 for i in pp.ISSUES}
        for _ in range(reps):
            m = 1 if correles else 2
            C = (rng.random((N, m)) < pc).astype(int)
            Bb = (rng.random((N, m)) < pb).astype(int)
            if correles:
                C, Bb = np.repeat(C, 2, axis=1), np.repeat(Bb, 2, axis=1)
            c[pp.trois_issues(C, Bb, rng, B, 0.975, 0.05, K)["issue"]] += 1
        return {k: round(x / reps, 3) for k, x in c.items()}

    for nom, pc, pb, cor in (("hasard 1/8, ordres corrélés (hypothèse de la taille)", h, h, True),
                             ("hasard 1/8, ordres indépendants", h, h, False),
                             ("reconnaisseur 0,15, ordres corrélés", 0.15 + 0.85 * h, h, True),
                             ("évitant 0,5, ordres corrélés", 0.5 * h, h, True),
                             ("aucune reconnaissance, taux de base 0,25 dans C et B, corrélés", 0.25, 0.25, True),
                             ("aucune reconnaissance, taux de base 0,50 dans C et B, corrélés", 0.5, 0.5, True),
                             ("préférence de contenu mesurée en C (C 0,274 ; B 0,224), corrélés", 0.274, 0.224, True),
                             ("effet vrai sous la marge (D = 0,03 ; C 0,155 ; B 0,125), corrélés", 0.155, 0.125, True)):
        print(f"{nom:68s} {sim(pc, pb, cor)}")


if __name__ == "__main__":
    T = Path(sys.argv[1])
    T.mkdir(parents=True)
    print("python", sys.version.split()[0], "| numpy", np.__version__, "| modules :", L.VERSION, pp.VERSION, qp.VERSION, mr.VERSION)
    section_a()
    section_b(T)
    section_e()
    section_c()
