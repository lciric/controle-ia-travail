#!/usr/bin/env python3
"""calcul-profil-bras-meta-v1-brouillon2.py — annexe des paramètres du bras méta v1, brouillon 2 (garde 22a, CA1-05).

Rédacteur neuf Opus 5.5 (lignée conv-audit), 31 octobre 2026. Processeur seul, aucun réseau, aucun appel de modèle, rien
lu sous `donnees/`. À lancer depuis un dossier temporaire vide :

    cd "$(mktemp -d)" && python3 -I CHEMIN/calcul-profil-bras-meta-v1-brouillon2.py CHEMIN/annexe-bras-meta-v1-brouillon2.md \
        CHEMIN_DEPOT

Ce que fait le script (tout est lu dans l'annexe : blocs JSON `parametres_bras_meta`, `jeu_essai_non_vacuite`,
`variante_bloc_n4` ; aucune valeur de paramètre n'est recopiée ici) :

  1. Compose les variantes du bloc N4 (options de CA1-05 × options de CA1-04) et compte, pour chacune, les paires de
     niches dans le profil (aux structures près).
  2. Éprouve chaque variante contre le code réel de l'orchestrateur v55 (`bisociateur_v55.lire_annexe_meta_v55`, puis
     `bisociateur_v54.verifier_non_vacuite`, `garde_desaccord_v54`, `seuils_s28`) sur des copies dans un dossier
     temporaire : refus avec les deux champs à « À REMPLIR » ; acceptation avec les deux champs remplis d'un texte d'essai
     qui cite les empreintes d'un brouillon relu et d'un rapport d'essai ; artefacts (paramètre changé après relecture,
     texte changé, R-000, une seule empreinte, poids négatif, compagnon absent). Le compagnon `.sha256` est SIMULÉ EN
     MÉMOIRE (`verifier_scelle` remplacé par une comparaison à une table interne) : aucun fichier `.sha256` n'est écrit.
  3. Prédit, par simulation (numpy SeedSequence, racine 20261101, une tâche par scénario ; R9), la probabilité qu'un lot
     contienne au moins une paire du profil, et que la paire méta retenue soit dans le profil après le retrait des paires
     prises par les bras antérieurs (I-11, CA1-09). Toutes les lois sont SUPPOSÉ.
  4. Calcule l'erreur-type de Hanley et McNeil d'une aire 0,5 à 6 contre 6 (CA1-11) et les coûts des options (bases du
     devis v6, `devis-course-2-et-pre-pilote-v6.md` `13ef84f9…`, § 3.2 : 0,025 USD par lecture d'étiquettes ; script de
     puissance v9 `a28eca2d…` : Kimi passe 1 = 2,0 USD pour 10 fiches × 1,447 de coupures ; aiguilleur 0,057 par lecture).
"""
import hashlib
import itertools
import json
import os
import re
import sys
import tempfile

import numpy as np

if len(sys.argv) < 2:
    sys.exit("usage : calcul-profil-bras-meta-v1-brouillon2.py ANNEXE [DEPOT]")
ANNEXE = os.path.abspath(sys.argv[1])
DEPOT = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else "/home/claude/controle-ia-travail"
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(DEPOT, "docs/notes/ideation-organisme-v1/orchestrateur-v55"))
sys.path.insert(0, os.path.join(DEPOT, "src"))

from controle_ia.manifeste import cle_de_tache  # noqa: E402
import pole.bisociateur_v53 as b53  # noqa: E402
import pole.bisociateur_v54 as b54  # noqa: E402
import pole.bisociateur_v55 as b55  # noqa: E402

RACINE = 20261101
N_SIM = 100_000
BLOC = re.compile(r"```json\s*(\{.*?\})\s*```", re.S)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def rng(nom):
    return np.random.default_rng(np.random.SeedSequence(RACINE, spawn_key=(cle_de_tache(nom),)))


# ---------------------------------------------------------------------------------------------------------------------
# 0. Lecture de l'annexe
# ---------------------------------------------------------------------------------------------------------------------
with open(ANNEXE, encoding="utf-8") as f:
    TEXTE = f.read()
blocs = [(m.span(), json.loads(m.group(1))) for m in BLOC.finditer(TEXTE)]
PAR = [b for b in blocs if "parametres_bras_meta" in b[1]]
assert PAR, "bloc parametres_bras_meta absent"
SPAN_PAR, P0 = PAR[-1][0], PAR[-1][1]["parametres_bras_meta"]
JEU = [b for b in blocs if "jeu_essai_non_vacuite" in b[1]][-1][1]["jeu_essai_non_vacuite"]
VAR = [b for b in blocs if "variante_bloc_n4" in b[1]][-1][1]["variante_bloc_n4"]


def canon(o):
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


print("== calcul-profil-bras-meta-v1-brouillon2 ==")
print(f"python {sys.version.split()[0]} ; numpy {np.__version__} ; racine {RACINE} ; N_SIM {N_SIM}")
print(f"blocs JSON lus dans l'annexe : {len(blocs)} ; empreinte du bloc parametres_bras_meta (JSON canonique, sans les deux "
      f"champs libres) : {hashlib.sha256(canon({k: v for k, v in P0.items() if k not in b55.CHAMPS_LIBRES}).encode()).hexdigest()}")
print(f"empreinte du bloc variante_bloc_n4 (JSON canonique) : {hashlib.sha256(canon(VAR).encode()).hexdigest()}")
print(f"empreinte du jeu d'essai (JSON canonique) : {hashlib.sha256(canon(JEU).encode()).hexdigest()}")
print(f"option écrite dans le bloc N4 de l'annexe : CA1-05 = {P0.get('option_ca1_05')!r} ; CA1-04 = {P0.get('option_ca1_04')!r}")

NICHES = P0["niches"]
K = len(NICHES)


def composer(o5, o4):
    p = json.loads(json.dumps(P0))
    for cle, v in VAR["ca1_05"][o5]["remplace"].items():
        p[cle] = v
    for cle, v in VAR["ca1_04"][o4]["remplace"].items():
        p[cle] = v
    p["option_ca1_05"], p["option_ca1_04"] = o5, o4
    return p


def matrice_profil(p, c_n1n2=None):
    m = np.zeros((K, K), bool)
    for i, j in itertools.combinations(range(K), 2):
        cle = b53._niche_cle(NICHES[i], NICHES[j])
        c = p["communication"][cle]
        if c_n1n2 is not None and {NICHES[i], NICHES[j]} == {NICHES[0], NICHES[1]}:
            c = c_n1n2
        e = p["eloignement"][cle]
        m[i, j] = m[j, i] = (c <= p["seuil_communication_faible"]) and (p["bande"][0] <= e <= p["bande"][1])
    return m


def matrice_canal(p):
    m = np.zeros((K, K))
    for i, j in itertools.combinations(range(K), 2):
        m[i, j] = m[j, i] = p["communication"][b53._niche_cle(NICHES[i], NICHES[j])]
    return m


O5 = list(VAR["ca1_05"])
O4 = list(VAR["ca1_04"])
print("\n== 1. Paires de niches dans le profil (aux structures près), par option de CA1-05 ==")
for o5 in O5:
    p = composer(o5, "A")
    m = matrice_profil(p)
    paires = [f"{NICHES[i][:2]}–{NICHES[j][:2]}" for i, j in itertools.combinations(range(K), 2) if m[i, j]]
    sans = [NICHES[i][:2] for i in range(K) if not m[i].any()]
    print(f"  {o5:3s} bande {p['bande']} canal ≤ {p['seuil_communication_faible']} : {len(paires)} sur {K*(K-1)//2} "
          f"({', '.join(paires)}) ; niches sans partenaire dans le profil : {', '.join(sans) or 'aucune'}")
m_alt = matrice_profil(composer("a", "A"), c_n1n2=2)
print(f"  sensibilité CA1-01 (c(n1, n2) relevé à 2), option a : {int(m_alt.sum() // 2)} paires sur {K*(K-1)//2}")
m_alt = matrice_profil(composer("b1", "A"), c_n1n2=2)
print(f"  sensibilité CA1-01 (c(n1, n2) relevé à 2), option b1 : {int(m_alt.sum() // 2)} paires sur {K*(K-1)//2}")
for o4 in O4:
    print(f"  CA1-04 option {o4} : structures comptées = {len(VAR['ca1_04'][o4]['remplace']['structure_forte']['types'])} "
          f"(nombre_min {VAR['ca1_04'][o4]['remplace']['structure_forte']['nombre_min']})")

# ---------------------------------------------------------------------------------------------------------------------
# 2. Épreuve contre le code v55 (copies temporaires ; compagnon simulé en mémoire)
# ---------------------------------------------------------------------------------------------------------------------
print("\n== 2. Épreuve des variantes contre le code réel v55 (lire_annexe_meta_v55, verifier_non_vacuite) ==")
COMPAGNONS = {}
b53.verifier_scelle = lambda chemin: chemin in COMPAGNONS and os.path.exists(chemin) and sha(chemin) == COMPAGNONS[chemin]


def texte_avec(p):
    corps = "```json\n" + json.dumps({"parametres_bras_meta": p}, ensure_ascii=False, indent=1) + "\n```"
    return TEXTE[:SPAN_PAR[0]] + corps + TEXTE[SPAN_PAR[1]:]


def ecrire(d, nom, texte, sceller=True):
    ch = os.path.join(d, nom)
    with open(ch, "w", encoding="utf-8") as f:
        f.write(texte)
    if sceller:
        COMPAGNONS[ch] = sha(ch)
    return ch


def refus(f, motif=None):
    try:
        f()
    except b54.BisociationRefusee as e:
        return motif is None or motif in str(e)
    return False


def lire(ch, s, relu, rap):
    return b55.lire_annexe_meta_v55(ch, s, definitions="annexe", brouillon_relu=relu, rapport=rap)


resultats_code = {}
with tempfile.TemporaryDirectory() as d:
    rap = ecrire(d, "rapport-essai.md", "rapport de contre-lecture d'essai (aucune valeur)\n", sceller=False)
    s_rap = sha(rap)
    for o5 in O5:
        for o4 in O4:
            p = composer(o5, o4)
            p["contre_lecture"], p["approbation_lazar"] = "À REMPLIR", "À REMPLIR"
            relu = ecrire(d, f"relu-{o5}-{o4}.md", texte_avec(p), sceller=False)
            s_relu = sha(relu)
            brouillon_scelle = ecrire(d, f"brouillon-{o5}-{o4}.md", texte_avec(p))
            refuse_brouillon = refus(lambda: lire(brouillon_scelle, sha(brouillon_scelle), (relu, s_relu), (rap, s_rap)),
                                     "contre_lecture")
            q = dict(p, contre_lecture=f"essai : brouillon relu {s_relu} ; rapport {s_rap}", approbation_lazar="essai R-999")
            an = ecrire(d, f"annexe-{o5}-{o4}.md", texte_avec(q))
            pp, jeu = lire(an, sha(an), (relu, s_relu), (rap, s_rap))
            nv = b54.verifier_non_vacuite(pp, jeu)
            b54.garde_desaccord_v54(b54.score_meta, pp, pp["niches"][0], pp["niches"][1], set(), set())
            s28 = b54.seuils_s28(pp, "annexe")
            resultats_code[(o5, o4)] = nv
            print(f"  {o5:3s} × {o4} : brouillon refusé (À REMPLIR) {refuse_brouillon} ; rempli accepté True ; non-vacuité "
                  f"{nv['dans_profil']} dans le profil / {nv['hors_profil']} hors profil / {nv['meme_niche']} même niche ; "
                  f"argmax {'–'.join(nv['argmax'])} score {nv['score_argmax']:.1f} ; S28 {s28['kappa_min']}/{s28['jaccard_min']}")
    # artefacts sur la variante écrite dans l'annexe
    o5, o4 = P0.get("option_ca1_05"), P0.get("option_ca1_04")
    p = composer(o5, o4)
    p["contre_lecture"], p["approbation_lazar"] = "À REMPLIR", "À REMPLIR"
    relu = ecrire(d, "relu-art.md", texte_avec(p), sceller=False)
    s_relu = sha(relu)
    ok = dict(p, contre_lecture=f"essai : brouillon relu {s_relu} ; rapport {s_rap}", approbation_lazar="essai R-999")
    art = {}
    q = json.loads(json.dumps(ok)); q["bande"] = [2, 5] if q["bande"] != [2, 5] else [2, 3]
    a1 = ecrire(d, "art-parametre.md", texte_avec(q))
    art["paramètre changé après relecture"] = refus(lambda: lire(a1, sha(a1), (relu, s_relu), (rap, s_rap)), "différents")
    a2 = ecrire(d, "art-texte.md", texte_avec(ok).replace("## 1.", "## 1 (modifié).", 1))
    art["texte changé après relecture"] = refus(lambda: lire(a2, sha(a2), (relu, s_relu), (rap, s_rap)), "diffère")
    a3 = ecrire(d, "art-r000.md", texte_avec(dict(ok, approbation_lazar="essai R-000")))
    art["approbation R-000"] = refus(lambda: lire(a3, sha(a3), (relu, s_relu), (rap, s_rap)), "R-NNN")
    a4 = ecrire(d, "art-une-empreinte.md", texte_avec(dict(ok, contre_lecture=f"essai : brouillon relu {s_relu}")))
    art["contre_lecture à une seule empreinte"] = refus(lambda: lire(a4, sha(a4), (relu, s_relu), (rap, s_rap)), "deux empreintes")
    a5 = ecrire(d, "art-poids.md", texte_avec(dict(ok, poids=-1.0)))
    art["poids négatif"] = refus(lambda: lire(a5, sha(a5), (relu, s_relu), (rap, s_rap)), "poids")
    a6 = ecrire(d, "art-sans-compagnon.md", texte_avec(ok), sceller=False)
    art["compagnon absent"] = refus(lambda: lire(a6, sha(a6), (relu, s_relu), (rap, s_rap)), "non scellée")
    a7 = ecrire(d, "art-defs.md", texte_avec({k: v for k, v in ok.items() if k != "definitions_niches"}))
    art["définitions des niches absentes"] = refus(lambda: lire(a7, sha(a7), (relu, s_relu), (rap, s_rap)), "definitions_niches")
    print(f"  artefacts sur la variante écrite ({o5} × {o4}), chacun refusé (A20) : "
          + " ; ".join(f"{k} {v}" for k, v in art.items()))
    assert all(art.values())

# ---------------------------------------------------------------------------------------------------------------------
# 3. Simulation (toutes lois SUPPOSÉ)
# ---------------------------------------------------------------------------------------------------------------------
# Niche selon l'axe (axes 1 à 5 ; règle de la section 1 pour les affirmations mixtes de l'axe 1 : n2 par défaut).
LOI_AXE = np.array([
    # n1    n2    n3    n4    n5    n6
    [0.25, 0.50, 0.20, 0.05, 0.00, 0.00],   # axe 1 : statistique sur activations, agrégée dans le temps
    [0.15, 0.10, 0.00, 0.05, 0.55, 0.15],   # axe 2 : loi, garantie, impossibilité
    [0.20, 0.15, 0.10, 0.10, 0.00, 0.45],   # axe 3 : pré-mortem (failles du programme)
    [0.05, 0.10, 0.10, 0.05, 0.00, 0.70],   # axe 4 : préenregistrement d'universalité
    [0.15, 0.00, 0.05, 0.00, 0.80, 0.00],   # axe 5 : théorie, preuve dans Lean, bornes de délai
])
assert np.allclose(LOI_AXE.sum(1), 1)
LOIS_GLOBALES = {  # indépendantes de l'axe (reconstructions ; les vecteurs exacts de la contre-lecture ne sont pas versés)
    "annexe-b1": [0.30, 0.25, 0.15, 0.10, 0.15, 0.05],
    "n6-fort": [0.18, 0.12, 0.10, 0.05, 0.20, 0.35],
    "n2-fort": [0.25, 0.30, 0.15, 0.10, 0.15, 0.05],
}
ACCORD_AXE = np.array([0.6, 0.85, 0.6, 0.85, 0.85])   # sensibilité CA1-06 (c) : accord plus bas sur les axes 1 et 3


def jouer(nom, p, n, places_par_axe, loi="par-axe", p_acc=0.7, p_s=0.3, dep_canal=False, prises=True, c_n1n2=None,
          accord_par_axe=False):
    """Rend un dictionnaire de fréquences sur N_SIM lots. Lot = n fiches non aiguillées tirées sans remise parmi
    5 × places_par_axe places (deux fiches par axe et par proposeur au plus, texte I, « Déroulé »)."""
    g = rng(nom)
    places = np.repeat(np.arange(5), places_par_axe)
    ordre = np.argsort(g.random((N_SIM, places.size)), axis=1)[:, :n]
    axe = places[ordre]                                                     # (N_SIM, n)
    if loi == "par-axe":
        cum = LOI_AXE.cumsum(1)[axe]                                        # (N_SIM, n, 6)
        u = g.random((N_SIM, n, 1))
        nich = (u > cum).sum(2)
    else:
        nich = g.choice(K, size=(N_SIM, n), p=np.array(LOIS_GLOBALES[loi]))
    pa = ACCORD_AXE[axe] if accord_par_axe else p_acc
    garde = g.random((N_SIM, n)) < pa
    iu = np.triu_indices(n, 1)
    a, b = nich[:, iu[0]], nich[:, iu[1]]
    elig = garde[:, iu[0]] & garde[:, iu[1]] & (a != b)
    ps = p_s
    if dep_canal:  # CA1-06 (a) : moins de structures partagées entre niches qui se parlent peu
        ps = np.clip(p_s * (0.5 + 0.25 * matrice_canal(p)[a, b]), 0, 1)
    struct = g.random((N_SIM, iu[0].size)) < ps
    prof = elig & matrice_profil(p, c_n1n2)[a, b] & struct
    meme_axe = axe[:, iu[0]] == axe[:, iu[1]]
    dispo = prof.copy()
    if prises:  # I-11 : bras antérieurs dans l'ordre tiré ; basique (0,99) sur deux axes différents, Gu-Krenn (0,9)
        rang_meta = g.integers(0, 3, N_SIM)
        bas_avant = rang_meta >= 1
        gk_avant = rang_meta == 2
        tir = g.random((N_SIM, 2, iu[0].size))
        diff_axe = ~meme_axe
        choix_b = np.argmax(tir[:, 0] * diff_axe, axis=1)
        prod_b = bas_avant & diff_axe.any(1) & (g.random(N_SIM) < 0.99)
        t1 = tir[:, 1].copy()
        t1[np.arange(N_SIM), choix_b] = np.where(prod_b, -1.0, t1[np.arange(N_SIM), choix_b])
        choix_g = np.argmax(t1, axis=1)
        prod_g = gk_avant & (g.random(N_SIM) < 0.9)
        dispo[np.arange(N_SIM), choix_b] &= ~prod_b
        dispo[np.arange(N_SIM), choix_g] &= ~prod_g
    n_prof, n_dispo, n_elig = prof.sum(1), dispo.sum(1), elig.sum(1)
    # paire du profil retenue : tirée au hasard parmi les disponibles (le poids sur s est ignoré) ; même axe ?
    clef = g.random((N_SIM, iu[0].size)) * dispo
    ret = np.argmax(clef, axis=1)
    a_profil = n_dispo > 0
    meme = meme_axe[np.arange(N_SIM), ret] & a_profil
    est_n12 = (np.minimum(a, b)[np.arange(N_SIM), ret] == 0) & (np.maximum(a, b)[np.arange(N_SIM), ret] == 1) & a_profil
    return {"au_moins_un": float(np.mean(n_prof > 0)), "meta_profil": float(np.mean(a_profil)),
            "mediane": float(np.median(n_prof)), "aucune_eligible": float(np.mean(n_elig == 0)),
            "meme_axe": float(meme.sum() / max(a_profil.sum(), 1)), "n1n2_meme_axe": float((meme & est_n12).sum() / max(a_profil.sum(), 1))}


def ligne(r):
    return (f"≥ 1 paire du profil {r['au_moins_un']:.2f} ; paire méta dans le profil (après I-11) {r['meta_profil']:.2f} ; "
            f"médiane {r['mediane']:.0f} ; aucune paire éligible {r['aucune_eligible']:.3f} ; "
            f"part même axe {r['meme_axe']:.2f} (dont n1–n2 {r['n1n2_meme_axe']:.2f})")


SCEN = {  # option -> (variante de paramètres, effectifs, places par axe)
    "a": ("a", (6, 8, 10), 2),
    "b1": ("b1", (6, 8, 10), 2),
    "b2": ("b2", (6, 8, 10), 2),
    "c1": ("c1", (12, 15), 3),
    "c2": ("c2", (12, 16, 20), 4),
    "d1": ("d1", (6, 8, 10), 2),
}
print("\n== 3. Scénario principal (loi par axe, accord 0,7, structure 0,3, indépendance ; CA1-04 option A) ==")
PRINC = {}
for o, (v, ns, pl) in SCEN.items():
    p = composer(v, "A")
    for n in ns:
        r = jouer(f"annexe-b2-principal-{o}-{n}", p, n, pl)
        PRINC[(o, n)] = r
        print(f"  {o:3s} n={n:2d} : {ligne(r)}")
P_PERTE_TABLEAU = 0.53   # passe « tableau » perdue (préenregistrement brouillon 10, résumé point 3, sortie v9)
for nn in (6, 10):
    base = jouer(f"annexe-b2-principal-c2-seule-{nn}", composer("c2", "A"), nn, 2)
    reun = jouer(f"annexe-b2-principal-c2-reunie-{nn}", composer("c2", "A"), 2 * nn, 4)
    print(f"  c2 avec perte de la passe « tableau » ({P_PERTE_TABLEAU}) : passe 1 à {nn} fiches → "
          f"≥ 1 paire {P_PERTE_TABLEAU * base['au_moins_un'] + (1 - P_PERTE_TABLEAU) * reun['au_moins_un']:.2f} ; "
          f"paire méta dans le profil {P_PERTE_TABLEAU * base['meta_profil'] + (1 - P_PERTE_TABLEAU) * reun['meta_profil']:.2f}")

print("\n== 4. Fourchettes : lois {par axe, annexe-b1, n6-fort, n2-fort} × structure {0,15 ; 0,3 ; 0,5} (accord 0,7) ==")
for o, (v, ns, pl) in SCEN.items():
    p = composer(v, "A")
    for n in (ns[0], ns[-1]):
        vals = []
        for loi in ("par-axe",) + tuple(LOIS_GLOBALES):
            for ps in (0.15, 0.3, 0.5):
                r = jouer(f"annexe-b2-fourchette-{o}-{n}-{loi}-{ps}", p, n, pl, loi=loi, p_s=ps)
                vals.append((r["au_moins_un"], r["meta_profil"]))
        u = [x[0] for x in vals]
        w = [x[1] for x in vals]
        print(f"  {o:3s} n={n:2d} : ≥ 1 paire du profil [{min(u):.2f} ; {max(u):.2f}] ; paire méta dans le profil "
              f"[{min(w):.2f} ; {max(w):.2f}]")

print("\n== 5. Sensibilités (loi par axe, n = 6 et 10 ; options a et b1 sauf mention) ==")
for o in ("a", "b1"):
    p = composer(o, "A")
    for n in (6, 10):
        r1 = jouer(f"annexe-b2-sens-dep-{o}-{n}", p, n, 2, dep_canal=True)
        r2 = jouer(f"annexe-b2-sens-accord-{o}-{n}", p, n, 2, accord_par_axe=True)
        r3 = jouer(f"annexe-b2-sens-c12-{o}-{n}", p, n, 2, c_n1n2=2)
        r4 = jouer(f"annexe-b2-sens-sansprises-{o}-{n}", p, n, 2, prises=False)
        print(f"  {o:3s} n={n:2d} : structure dépendante du canal (CA1-06 a) {r1['au_moins_un']:.2f} / {r1['meta_profil']:.2f} ; "
              f"accord 0,6 axes 1 et 3, 0,85 ailleurs (CA1-06 c) {r2['au_moins_un']:.2f} / {r2['meta_profil']:.2f} ; "
              f"c(n1, n2) = 2 (CA1-01) {r3['au_moins_un']:.2f} / {r3['meta_profil']:.2f} ; sans I-11 {r4['meta_profil']:.2f}")
print("  CA1-04 (probabilité de structure partagée par paire, SUPPOSÉ : A 0,3 ; B jeux comptés 0,85 ; C sans les trois "
      "structures séquentielles 0,15) :")
for o in ("a", "b1"):
    for n in (6, 10):
        s = []
        for o4, ps in (("A", 0.3), ("B", 0.85), ("C", 0.15)):
            r = jouer(f"annexe-b2-ca104-{o}-{o4}-{n}", composer(o, o4), n, 2, p_s=ps)
            s.append(f"{o4} {r['au_moins_un']:.2f} / {r['meta_profil']:.2f}")
        print(f"    {o:3s} n={n:2d} : " + " ; ".join(s))

# ---------------------------------------------------------------------------------------------------------------------
# 4. Hanley et McNeil (CA1-11) et coûts des options
# ---------------------------------------------------------------------------------------------------------------------
A, n1, n2 = 0.5, 6, 6
q1, q2 = A / (2 - A), 2 * A * A / (1 + A)
se = ((A * (1 - A) + (n1 - 1) * (q1 - A * A) + (n2 - 1) * (q2 - A * A)) / (n1 * n2)) ** 0.5
print(f"\n== 6. Hanley et McNeil 1982 : erreur-type d'une aire 0,5 à 6 contre 6 = {se:.3f} ==")
LECT, KIMI_FICHE, KC, AIG = 0.025, 2.0 / 10, 1.447, 0.057
c1 = 5 * (KIMI_FICHE * KC + 2 * AIG + 6 * LECT)
c2 = 10 * 6 * LECT
des = 5 * 2 * LECT
print("== 7. Coûts (bases du devis v6 et du script v9) ==")
print(f"  c1, 5 fiches de plus en passe 1 (Kimi ×1,447, aiguilleur et second lecteur, 6 lectures d'étiquettes par fiche) : "
      f"+{c1:.2f} USD ; É2 aux bases {10 * KIMI_FICHE * KC:.2f} → {15 * KIMI_FICHE * KC:.2f} USD pour un relais de 3,0")
print(f"  c2, lectures d'étiquettes sur les ≤ 10 fiches de la passe « tableau » (3 grilles × 2 lecteurs) : +{c2:.2f} USD ; "
      f"É7b aux bases 1,50 → {1.5 + c2:.2f} USD pour un relais de 1,0 (souple, étape protégée)")
print(f"  désaccord (I-13) : 5 paires × 2 lecteurs au plus, ≤ {LECT} USD par lecture : ≤ {des:.2f} USD (absent du devis v6)")
print("fin")
