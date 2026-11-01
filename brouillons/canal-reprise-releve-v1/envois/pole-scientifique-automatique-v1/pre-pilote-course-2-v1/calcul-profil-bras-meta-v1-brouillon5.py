#!/usr/bin/env python3
"""calcul-profil-bras-meta-v1-brouillon5.py — annexe des paramètres du bras méta v1, brouillon 5 (garde 22a, CA1-05, CA4).

Rédacteur neuf Opus 5.5 du brouillon 5 (lignée conv-audit), 1er novembre 2026 ; il n'a écrit ni les brouillons 1 à 4, ni
leurs contre-lectures, ni l'erratum v1. Copie de `calcul-profil-bras-meta-v1-brouillon4.py`
(`48e3c57db884b0cb33e6a348a5f3805a3ccb36617694115faa83177d69abba40`, gardé sans modification, R12) : sections 1 à 17
inchangées dans leur code (mêmes noms de tâche, donc mêmes tirages et mêmes chiffres ; changent la ligne de titre et
l'empreinte du texte hors bloc N4, calculée sur le brouillon 5). Sections nouvelles, pour la contre-lecture 4 (CA4) et la
synthèse du tour 1 v12 des nœuds, que le brouillon 4 n'avait pas lue :
  18. synthèse du tour 1 (N4) : empreintes des pièces ; lettres d'option déjà prises (CA4-01) ; recalculs de la synthèse
      sur la mesure de la loi ; chiffres de N4 sous trois lois (loi du brouillon 1, « n6 fort » — la loi défavorable dont le
      tour 1 a demandé qu'elle soit servie —, loi par axe) pour l'erratum v2 ; passes réunies avec perte sous « n6 fort » ;
      n1–n2 hors du profil (c(n1, n2) = 2 : accord à quatre du tour 1 sur la paire que le programme fusionne) sous les deux
      lois globales ;
  19. brouillon 5 contre brouillon 4 : écart du texte hors bloc N4 (lignes, passages), blocs JSON identiques, comptes de
      CA4-09 ; garde ajoutée à l'achèvement (second rédacteur neuf Opus 5.5, 1er novembre, après 15:35 UTC) : arrêt si un
      marqueur de rédaction (empreintes « à venir », chiffres de la section 2) reste dans le texte hors bloc N4.
Usage (troisième argument obligatoire : dossier qui contient la synthèse du tour 1 et la question du tour 2, empreintes
vérifiées ; aucun repli silencieux s'il manque) :

    cd "$(mktemp -d)" && python3 -I CHEMIN/calcul-profil-bras-meta-v1-brouillon5.py CHEMIN/annexe-bras-meta-v1-brouillon5.md \
        CHEMIN_DEPOT DOSSIER_SYNTHESE

Docstring du script v4, gardée :

calcul-profil-bras-meta-v1-brouillon4.py — annexe des paramètres du bras méta v1, brouillon 4 (garde 22a, CA1-05, CA3).

Rédacteur neuf Opus 5.5 du brouillon 4 (lignée conv-audit), 1er novembre 2026. Copie de
`calcul-profil-bras-meta-v1-brouillon3.py` (`50e0c0e13cef458a17d990c9e9c4b14594ef81d12b2942fcd1ec4bc5c6de71f3`, gardé sans
modification, R12) : sections 1 à 13 inchangées dans leur code (mêmes noms de tâche, donc mêmes tirages ; seules changent la
ligne de titre et les empreintes que l'en-tête et la section 8 calculent sur le texte du brouillon 4) ; `jouer` reçoit un
argument facultatif `loi_axe` (aucun tirage déplacé). Sections nouvelles, pour la contre-lecture 3 :
  14. CA3-02 : loi de l'axe 1 décomposée en fiches mixtes (part m) dont une part r est rangée en n1, le reste au défaut n2 ;
      grille m × r, options a, b1, b2, d1, tirages communs avec le scénario principal (la cellule m = 0,6, r = 0,25 le redonne
      à l'identique, contrôlé) ;
  15. CA3-06 : erreur-type de Hanley et McNeil à 8 fusions par bras (course 2 : 24 fusions, trois bras) ;
  16. épreuves supplémentaires du texte exact par le code v55 (un seul champ rempli, « À REMPLIR » résiduel) ; règles de
      lecture (bloc `regles_lecteur_niches`) : phrases bien servies au lecteur par `liste_servie` (CA3-03), garde A4 sur ce
      qui est servi, contrôle « consigne figée contenant les règles » (cas sain et artefacts, R5) ; nombre de jeux de
      paramètres distincts (CA3-08) ;
  17. CA3-01 : chiffres de N4 v12 contre chiffres à jour, option par option, plus (c2) sous la loi du brouillon 1.
Processeur seul, aucun réseau, aucun appel de modèle, rien lu sous `donnees/`. À lancer depuis un dossier temporaire vide :

    cd "$(mktemp -d)" && python3 -I CHEMIN/calcul-profil-bras-meta-v1-brouillon4.py CHEMIN/annexe-bras-meta-v1-brouillon4.md \
        CHEMIN_DEPOT

Historique (docstring du script v3, gardée) : second rédacteur neuf Opus 5.5, 31 octobre 2026, reprenait
`calcul-profil-bras-meta-v1-brouillon2.py` (`3659692cc06808a9a93b37f39efdb123a51f1d48fee112fbc2625945b9993dd5`).

Tout est lu dans l'annexe (blocs JSON `parametres_bras_meta`, `jeu_essai_non_vacuite`, `variante_bloc_n4`) ; aucune
valeur de paramètre n'est recopiée ici ; les lois de la simulation sont SUPPOSÉ (section 3 du code, inchangée).

Sections 1 à 7 de la sortie : celles de la v2, mêmes noms de tâche, donc mêmes tirages et mêmes chiffres (la fonction
`jouer` tire ses nombres dans le même ordre ; seule la sortie de la ligne de titre change). Sections nouvelles :
  8. texte hors bloc N4 : empreinte de tout le texte sauf ce qui est strictement entre les marqueurs `BLOC N4 : DÉBUT` et
     `BLOC N4 : FIN` (elle ne doit pas changer quand on choisit une autre option) ; marqueurs ⟦…⟧ restants ;
  9. épreuve du texte EXACT de l'annexe par le code v55 (la v2 n'éprouvait qu'un bloc réécrit) : refus tel quel ; acceptation
     d'une copie où seules les deux valeurs « À REMPLIR » sont remplacées ; paramètres lus par le code = ceux du script ;
  10. marges de la loi par axe ; part de chaque paire de niches parmi les paires méta du profil (scénario principal) ;
  11. fourchette détaillée par loi (structure 0,3), cellules du minimum et du maximum (mêmes tâches que la v2) ; zéro paire
     du profil sous les lois globales, pour comparaison avec la contre-lecture du brouillon 1 ;
  12. sensibilités jouées pour toutes les options (a et b1 : mêmes tâches que la v2) ; classement des options ;
  13. ordre des bras tiré uniformément (quand le méta est deuxième, le bras placé avant lui est Gu-Krenn une fois sur deux ;
     la v2 y plaçait toujours le basique) ; tirages communs avec le scénario principal (mêmes noms de tâche, un tirage de
     plus à la fin), donc l'écart lu est celui de l'ordre seul.
Le compagnon `.sha256` est SIMULÉ EN MÉMOIRE comme en v2 : aucun fichier `.sha256` n'est écrit.
"""
import difflib
import hashlib
import itertools
import math
import json
import os
import re
import sys
import tempfile

import numpy as np

if len(sys.argv) < 4:
    sys.exit("usage : calcul-profil-bras-meta-v1-brouillon5.py ANNEXE DEPOT DOSSIER_SYNTHESE")
ANNEXE = os.path.abspath(sys.argv[1])
DEPOT = os.path.abspath(sys.argv[2])
DOSSIER_SYNTHESE = os.path.abspath(sys.argv[3])
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(DEPOT, "docs/notes/ideation-organisme-v1/orchestrateur-v55"))
sys.path.insert(0, os.path.join(DEPOT, "src"))

from controle_ia.manifeste import cle_de_tache  # noqa: E402
import pole.bisociateur_v53 as b53  # noqa: E402
import pole.bisociateur_v54 as b54  # noqa: E402
import pole.bisociateur_v55 as b55  # noqa: E402
import pole.fiches_v53 as fv53  # noqa: E402

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
REG_BLOCS = [b for b in blocs if "regles_lecteur_niches" in b[1]]
assert len(REG_BLOCS) == 1, "bloc regles_lecteur_niches absent ou multiple"
SPAN_REG, REG = REG_BLOCS[0][0], REG_BLOCS[0][1]["regles_lecteur_niches"]


def canon(o):
    return json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


print("== calcul-profil-bras-meta-v1-brouillon5 ==")
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
# 3. Simulation (toutes lois SUPPOSÉ ; inchangées depuis la v2)
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
          accord_par_axe=False, ordre="v2", loi_axe=None):
    """Rend un dictionnaire de fréquences sur N_SIM lots. Lot = n fiches non aiguillées tirées sans remise parmi
    5 × places_par_axe places (deux fiches par axe et par proposeur au plus, texte I, « Déroulé »).
    Les nombres aléatoires sont tirés dans le même ordre que la v2 (permutation, niches, accord, structures, puis, si
    `prises` : rang du méta, deux tirages de choix, production du basique, production de Gu-Krenn, clé de choix ; sinon la
    clé seule) ; `ordre="uniforme"` ajoute un dernier tirage (Gu-Krenn seul avant le méta, une fois sur deux, quand le méta
    est deuxième)."""
    g = rng(nom)
    places = np.repeat(np.arange(5), places_par_axe)
    permutation = np.argsort(g.random((N_SIM, places.size)), axis=1)[:, :n]
    axe = places[permutation]                                               # (N_SIM, n)
    if loi == "par-axe":
        cum = (LOI_AXE if loi_axe is None else loi_axe).cumsum(1)[axe]      # (N_SIM, n, 6) ; loi_axe : section 14 (v4)
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
    lignes = np.arange(N_SIM)
    if prises:  # I-11 : bras antérieurs ; basique (0,99) sur deux axes différents, Gu-Krenn (0,9)
        rang_meta = g.integers(0, 3, N_SIM)
        tir = g.random((N_SIM, 2, iu[0].size))
        u_b = g.random(N_SIM)
        u_g = g.random(N_SIM)
        u_clef = g.random((N_SIM, iu[0].size))
        if ordre == "uniforme":
            gk_seul = g.random(N_SIM) < 0.5
            bas_avant = (rang_meta == 2) | ((rang_meta == 1) & ~gk_seul)
            gk_avant = (rang_meta == 2) | ((rang_meta == 1) & gk_seul)
        else:  # v2 : méta deuxième → le basique avant lui ; méta troisième → les deux
            bas_avant = rang_meta >= 1
            gk_avant = rang_meta == 2
        diff_axe = ~meme_axe
        choix_b = np.argmax(tir[:, 0] * diff_axe, axis=1)
        prod_b = bas_avant & diff_axe.any(1) & (u_b < 0.99)
        t1 = tir[:, 1].copy()
        t1[lignes, choix_b] = np.where(prod_b, -1.0, t1[lignes, choix_b])
        choix_g = np.argmax(t1, axis=1)
        prod_g = gk_avant & (u_g < 0.9)
        dispo[lignes, choix_b] &= ~prod_b
        dispo[lignes, choix_g] &= ~prod_g
    else:
        u_clef = g.random((N_SIM, iu[0].size))
    n_prof, n_dispo, n_elig = prof.sum(1), dispo.sum(1), elig.sum(1)
    # paire du profil retenue : tirée au hasard parmi les disponibles (le poids sur s est ignoré) ; même axe ?
    clef = u_clef * dispo
    ret = np.argmax(clef, axis=1)
    a_profil = n_dispo > 0
    meme = meme_axe[lignes, ret] & a_profil
    ia, ib = np.minimum(a, b)[lignes, ret], np.maximum(a, b)[lignes, ret]
    est_n12 = (ia == 0) & (ib == 1) & a_profil
    compte = np.bincount((ia * K + ib)[a_profil], minlength=K * K)
    denom = max(int(a_profil.sum()), 1)
    return {"au_moins_un": float(np.mean(n_prof > 0)), "meta_profil": float(np.mean(a_profil)),
            "mediane": float(np.median(n_prof)), "aucune_eligible": float(np.mean(n_elig == 0)),
            "meme_axe": float(meme.sum() / denom), "n1n2_meme_axe": float((meme & est_n12).sum() / denom),
            "paires": {f"{NICHES[i][:2]}–{NICHES[j][:2]}": float(compte[i * K + j] / denom)
                       for i, j in itertools.combinations(range(K), 2) if compte[i * K + j] > 0}}


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
LOIS = ("par-axe",) + tuple(LOIS_GLOBALES)
FOUR = {}
for o, (v, ns, pl) in SCEN.items():
    p = composer(v, "A")
    for n in (ns[0], ns[-1]):
        vals = []
        for loi in LOIS:
            for ps in (0.15, 0.3, 0.5):
                r = jouer(f"annexe-b2-fourchette-{o}-{n}-{loi}-{ps}", p, n, pl, loi=loi, p_s=ps)
                FOUR[(o, n, loi, ps)] = (r["au_moins_un"], r["meta_profil"])
                vals.append((r["au_moins_un"], r["meta_profil"]))
        u = [x[0] for x in vals]
        w = [x[1] for x in vals]
        print(f"  {o:3s} n={n:2d} : ≥ 1 paire du profil [{min(u):.2f} ; {max(u):.2f}] ; paire méta dans le profil "
              f"[{min(w):.2f} ; {max(w):.2f}]")

print("\n== 5. Sensibilités (loi par axe, n = 6 et 10 ; options a et b1 sauf mention) ==")
SENS = {}
for o in ("a", "b1"):
    p = composer(o, "A")
    for n in (6, 10):
        r1 = jouer(f"annexe-b2-sens-dep-{o}-{n}", p, n, 2, dep_canal=True)
        r2 = jouer(f"annexe-b2-sens-accord-{o}-{n}", p, n, 2, accord_par_axe=True)
        r3 = jouer(f"annexe-b2-sens-c12-{o}-{n}", p, n, 2, c_n1n2=2)
        r4 = jouer(f"annexe-b2-sens-sansprises-{o}-{n}", p, n, 2, prises=False)
        SENS[(o, n)] = (r1, r2, r3, r4)
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

# ---------------------------------------------------------------------------------------------------------------------
# 8 à 13. Ajouts du brouillon 3
# ---------------------------------------------------------------------------------------------------------------------
print("\n== 8. Texte hors bloc N4 (ce qui ne doit pas changer quand on choisit une autre option) ==")
MARQ_DEBUT = re.compile(r"<!-- BLOC N4 : DÉBUT.*?-->", re.S)
MARQ_FIN = "<!-- BLOC N4 : FIN -->"
assert len(MARQ_DEBUT.findall(TEXTE)) == 1 and TEXTE.count(MARQ_FIN) == 1, "marqueurs du bloc N4 absents ou multiples"
i_debut = MARQ_DEBUT.search(TEXTE).end()
i_fin = TEXTE.index(MARQ_FIN)
assert i_debut < SPAN_PAR[0] and SPAN_PAR[1] <= i_fin, "le bloc parametres_bras_meta n'est pas dans le bloc N4"
dans_n4 = [list(b[1])[0] for b in blocs if i_debut <= b[0][0] < i_fin]
HORS = TEXTE[:i_debut] + TEXTE[i_fin:]
N_MARQUEURS = len(re.findall(r"⟦[^⟧]*⟧", TEXTE))
print(f"  empreinte du texte hors bloc N4 (tout sauf ce qui est strictement entre les deux marqueurs) : "
      f"{hashlib.sha256(HORS.encode('utf-8')).hexdigest()}")
print(f"  blocs JSON dans le bloc N4 : {', '.join(dans_n4)} ; marqueurs ⟦…⟧ restants dans l'annexe : {N_MARQUEURS}")

print("\n== 9. Épreuve du texte exact de l'annexe par le code v55 (aucun bloc réécrit) ==")
CL = '"contre_lecture": "À REMPLIR"'
AP = '"approbation_lazar": "À REMPLIR"'
assert TEXTE.count(CL) == 1 and TEXTE.count(AP) == 1, "champs « À REMPLIR » absents ou multiples dans le texte"
with tempfile.TemporaryDirectory() as d:
    rap = ecrire(d, "rapport-essai.md", "rapport de contre-lecture d'essai (aucune valeur)\n", sceller=False)
    s_rap = sha(rap)
    relu = ecrire(d, "relu-exact.md", TEXTE, sceller=False)
    s_relu = sha(relu)
    tel = ecrire(d, "annexe-telle-quelle.md", TEXTE)
    r_tel = refus(lambda: lire(tel, sha(tel), (relu, s_relu), (rap, s_rap)), "annexe sans contre_lecture déclarée")
    cl = f"essai : brouillon relu {s_relu} ; rapport {s_rap}"
    rempli = (TEXTE.replace(CL, json.dumps({"contre_lecture": cl}, ensure_ascii=False)[1:-1], 1)
              .replace(AP, '"approbation_lazar": "essai R-999"', 1))
    an = ecrire(d, "annexe-remplie.md", rempli)
    pp, jeu = lire(an, sha(an), (relu, s_relu), (rap, s_rap))
    memes = pp == dict(P0, contre_lecture=cl, approbation_lazar="essai R-999") and jeu == JEU
    nv = b54.verifier_non_vacuite(pp, jeu)
    b54.garde_desaccord_v54(b54.score_meta, pp, pp["niches"][0], pp["niches"][1], set(), set())
    s28 = b54.seuils_s28(pp, "annexe")
    t2 = ecrire(d, "annexe-texte-change.md", rempli.replace("## 1.", "## 1 (modifié).", 1))
    r_t2 = refus(lambda: lire(t2, sha(t2), (relu, s_relu), (rap, s_rap)), "diffère")
    print(f"  annexe telle quelle (champs « À REMPLIR ») refusée : {r_tel} ; copie où seules les deux valeurs sont remplacées "
          f"acceptée : True ; paramètres et jeu d'essai lus par le code = ceux du script : {memes}")
    print(f"  non-vacuité sur le texte exact : {nv['dans_profil']} dans le profil / {nv['hors_profil']} hors profil / "
          f"{nv['meme_niche']} même niche ; argmax {'–'.join(nv['argmax'])} score {nv['score_argmax']:.1f} ; "
          f"S28 {s28['kappa_min']}/{s28['jaccard_min']} ; une ligne de texte changée après relecture refusée : {r_t2}")
    assert r_tel and memes and r_t2

print("\n== 10. Loi par axe : marges ; paires de niches des paires méta du profil (scénario principal) ==")
marges = LOI_AXE.mean(0)
print("  marges (deux places par axe, axes équiprobables) : "
      + " ; ".join(f"{NICHES[i][:2]} {marges[i]:.2f}" for i in range(K)))
for o in ("a", "b1", "b2", "d1"):
    for n in (6, 10):
        pr = sorted(PRINC[(o, n)]["paires"].items(), key=lambda x: -x[1])
        print(f"  {o:3s} n={n:2d} : " + " ; ".join(f"{k} {v:.2f}" for k, v in pr))

print("\n== 11. Fourchette détaillée (mêmes tâches que la section 4) ==")
for o, (v, ns, pl) in SCEN.items():
    for n in (ns[0], ns[-1]):
        cel = {k: x for k, x in FOUR.items() if k[0] == o and k[1] == n}
        kmin = min(cel, key=lambda k: cel[k][0])
        kmax = max(cel, key=lambda k: cel[k][0])
        print(f"  {o:3s} n={n:2d} : structure 0,3 — "
              + " ; ".join(f"{loi} {FOUR[(o, n, loi, 0.3)][0]:.2f} / {FOUR[(o, n, loi, 0.3)][1]:.2f}" for loi in LOIS)
              + f" ; minimum {cel[kmin][0]:.2f} ({kmin[2]}, {kmin[3]}) ; maximum {cel[kmax][0]:.2f} ({kmax[2]}, {kmax[3]})")
print("  zéro paire du profil (1 − P(≥ 1)), structure 0,3, lois globales (comparaison avec la contre-lecture du brouillon 1) :")
for o, n in (("a", 6), ("a", 10), ("b1", 6), ("b1", 10), ("b2", 6), ("b2", 10), ("d1", 6), ("d1", 10), ("c1", 15)):
    print(f"    {o:3s} n={n:2d} : " + " ; ".join(f"{loi} {1 - FOUR[(o, n, loi, 0.3)][0]:.2f}" for loi in LOIS_GLOBALES)
          + f" ; par axe {1 - FOUR[(o, n, 'par-axe', 0.3)][0]:.2f}")

print("\n== 12. Sensibilités pour toutes les options ; classement des options à effectif égal ==")
for o, (v, ns, pl) in SCEN.items():
    if o in ("a", "b1"):
        continue
    p = composer(v, "A")
    for n in ((6, 10) if pl == 2 else (ns[0], ns[-1])):
        r1 = jouer(f"annexe-b2-sens-dep-{o}-{n}", p, n, pl, dep_canal=True)
        r2 = jouer(f"annexe-b2-sens-accord-{o}-{n}", p, n, pl, accord_par_axe=True)
        r3 = jouer(f"annexe-b2-sens-c12-{o}-{n}", p, n, pl, c_n1n2=2)
        r4 = jouer(f"annexe-b2-sens-sansprises-{o}-{n}", p, n, pl, prises=False)
        SENS[(o, n)] = (r1, r2, r3, r4)
        print(f"  {o:3s} n={n:2d} : structure dépendante du canal (CA1-06 a) {r1['au_moins_un']:.2f} / {r1['meta_profil']:.2f} ; "
              f"accord 0,6 axes 1 et 3, 0,85 ailleurs (CA1-06 c) {r2['au_moins_un']:.2f} / {r2['meta_profil']:.2f} ; "
              f"c(n1, n2) = 2 (CA1-01) {r3['au_moins_un']:.2f} / {r3['meta_profil']:.2f} ; sans I-11 {r4['meta_profil']:.2f}")


def classement(valeurs):
    return " < ".join(f"{o} {x:.2f}" for o, x in sorted(valeurs.items(), key=lambda t: t[1]))


OPT = ("a", "b1", "b2", "d1")
print("  classement de P(≥ 1) entre a, b1, b2, d1 (même effectif, deux places par axe) :")
for n in (6, 10):
    print(f"    n={n:2d} principal : " + classement({o: PRINC[(o, n)]["au_moins_un"] for o in OPT}))
    for loi in LOIS:
        print(f"    n={n:2d} loi {loi}, structure 0,3 : " + classement({o: FOUR[(o, n, loi, 0.3)][0] for o in OPT}))
    for i, nom in enumerate(("structure dépendante du canal", "accord par axe", "c(n1, n2) = 2")):
        print(f"    n={n:2d} {nom} : " + classement({o: SENS[(o, n)][i]["au_moins_un"] for o in OPT}))

print("\n== 13. Ordre des bras tiré uniformément (tirages communs avec le scénario principal) ==")
for o in ("a", "b1", "b2", "d1"):
    p = composer(o, "A")
    for n in (6, 10):
        r = jouer(f"annexe-b2-principal-{o}-{n}", p, n, 2, ordre="uniforme")
        assert r["au_moins_un"] == PRINC[(o, n)]["au_moins_un"]
        print(f"  {o:3s} n={n:2d} : paire méta dans le profil {r['meta_profil']:.4f} (ordre de la v2 : "
              f"{PRINC[(o, n)]['meta_profil']:.4f} ; écart {r['meta_profil'] - PRINC[(o, n)]['meta_profil']:+.4f}) ; "
              f"≥ 1 paire du profil {r['au_moins_un']:.4f} (identique)")

# ---------------------------------------------------------------------------------------------------------------------
# 14 à 17. Ajouts du brouillon 4 (contre-lecture du brouillon 3, CA3-01 à CA3-11)
# ---------------------------------------------------------------------------------------------------------------------
print("\n== 14. Règle des affirmations mixtes (CA3-02) : axe 1 décomposé ; effet du défaut n2 (tirages communs) ==")
# Fiches de l'axe 1 : part m « mixtes » (lisent des activations ET s'agrègent dans le temps) ; parmi elles, part r rangée en
# n1 par le champ lu, le reste (1 − r) en n2 (ligne couches ou jetons, ou défaut). Fiches non mixtes : loi AXE1_PUR. Tout
# SUPPOSÉ. La cellule (m, r) = (0,6 ; 0,25) redonne exactement la ligne de l'axe 1 de LOI_AXE (scénario principal).
AXE1_PUR = np.array([0.25, 0.125, 0.50, 0.125, 0.0, 0.0])


def loi_axe1(m, r):
    mix = np.zeros(K)
    mix[0], mix[1] = r, 1 - r
    return m * mix + (1 - m) * AXE1_PUR


assert np.allclose(loi_axe1(0.6, 0.25), LOI_AXE[0]), "décomposition de l'axe 1 : ne redonne pas la loi principale"
print("  axe 1 = m × [n1 : r ; n2 : 1 − r] + (1 − m) × fiches non mixtes ["
      + " ; ".join(f"{NICHES[i][:2]} {AXE1_PUR[i]:.3f}" for i in range(K) if AXE1_PUR[i] > 0)
      + "] ; (m, r) = (0,6 ; 0,25) redonne la loi principale de l'axe 1 : True")
print("  m = part des fiches de l'axe 1 qui sont mixtes ; r = part des mixtes rangées en n1 (ligne « agrégation » déclarée) ; "
      "1 − r : n2 (ligne couches ou jetons, ou défaut) ; r = 0 : le défaut joue pour toutes les mixtes")
GRILLE_M = (0.4, 0.6, 0.8)
GRILLE_R = (0.0, 0.25, 0.5, 0.75)
GR = {}
for m in GRILLE_M:
    for r in GRILLE_R:
        L = LOI_AXE.copy()
        L[0] = loi_axe1(m, r)
        marg = L.mean(0)
        print(f"  m={m:.1f} r={r:.2f} : axe 1 n1 {L[0][0]:.2f} n2 {L[0][1]:.2f} ; marge n1 {marg[0]:.3f} (principal "
              f"{LOI_AXE.mean(0)[0]:.3f}) ; marge n2 {marg[1]:.3f}")
        for o in ("a", "b1", "b2", "d1"):
            cel = []
            for n in (6, 10):
                res = jouer(f"annexe-b2-principal-{o}-{n}", composer(o, "A"), n, 2, loi_axe=L)
                GR[(m, r, o, n)] = res
                if (m, r) == (0.6, 0.25):
                    assert res["au_moins_un"] == PRINC[(o, n)]["au_moins_un"] and res["meta_profil"] == PRINC[(o, n)]["meta_profil"]
                cel.append(f"n={n:2d} {res['au_moins_un']:.2f} / {res['meta_profil']:.2f}, même axe {res['meme_axe']:.2f} "
                           f"(dont n1–n2 {res['n1n2_meme_axe']:.2f}), n1–n2 parmi les paires méta du profil "
                           f"{res['paires'].get('n1–n2', 0.0):.2f}")
            print(f"    {o:3s} : " + " ; ".join(cel))
print("  écart de P(≥ 1) entre r = 0 (défaut partout) et r = 0,5, à m = 0,6 : "
      + " ; ".join(f"{o} n={n} {GR[(0.6, 0.5, o, n)]['au_moins_un'] - GR[(0.6, 0.0, o, n)]['au_moins_un']:+.2f}"
                   for o in ("a", "b1", "b2", "d1") for n in (6, 10)))
print("  extrêmes de la grille (P(≥ 1), sur m et r) : "
      + " ; ".join(f"{o} n={n} [{min(GR[(m, r, o, n)]['au_moins_un'] for m in GRILLE_M for r in GRILLE_R):.2f} ; "
                   f"{max(GR[(m, r, o, n)]['au_moins_un'] for m in GRILLE_M for r in GRILLE_R):.2f}]"
                   for o in ("a", "b1", "b2", "d1") for n in (6, 10)))


def hanley_mcneil(aire, na, nb):
    qa, qb = aire / (2 - aire), 2 * aire * aire / (1 + aire)
    return ((aire * (1 - aire) + (na - 1) * (qa - aire * aire) + (nb - 1) * (qb - aire * aire)) / (na * nb)) ** 0.5


FUSIONS_COURSE, BRAS_COURSE = 24, 3   # GO-2026-10-31-04 ; S22 du préenregistrement brouillon 10 (fixé, hors gel)
PAR_BRAS = FUSIONS_COURSE // BRAS_COURSE
print(f"\n== 15. Hanley et McNeil 1982, aire 0,5 (CA3-06) : course 2 à {FUSIONS_COURSE} fusions sur {BRAS_COURSE} bras, "
      f"{PAR_BRAS} par bras ==")
for na, nb, quoi in ((6, 6, "6 contre 6 (chiffre des brouillons 1 à 3, situation qui n'est plus celle du plan)"),
                     (PAR_BRAS, PAR_BRAS, f"{PAR_BRAS} contre {PAR_BRAS} (deux bras comparés fusion par fusion)"),
                     (PAR_BRAS // 2, PAR_BRAS // 2, f"{PAR_BRAS // 2} contre {PAR_BRAS // 2} (un bras, fusions passées contre "
                                                     "non passées, partage égal au mieux)")):
    print(f"  {quoi} : erreur-type {hanley_mcneil(0.5, na, nb):.3f}")

print("\n== 16. Épreuves supplémentaires : texte exact, règles servies au lecteur, consigne figée, A4 (R5) ==")
MARQ_DEBUT_POS = MARQ_DEBUT.search(TEXTE)
assert not (MARQ_DEBUT_POS.end() <= SPAN_REG[0] < TEXTE.index(MARQ_FIN)), "le bloc des règles ne doit pas être dans le bloc N4"
print(f"  bloc regles_lecteur_niches hors du bloc N4 : True ; empreinte (JSON canonique) "
      f"{hashlib.sha256(canon(REG).encode()).hexdigest()}")
CLES_CONSIGNE = ("niche", "affirmations_mixtes", "elements_imposes", "format_reponse")
for k in CLES_CONSIGNE:
    print(f"  règle « {k} » : {len(REG[k])} caractères ; empreinte {hashlib.sha256(REG[k].encode('utf-8')).hexdigest()}")


def consigne_conforme(texte_consigne, regles):
    """Garde proposée (absente du code v55 : I-15) : la consigne figée contient chaque règle mot pour mot."""
    manquantes = [k for k in CLES_CONSIGNE if regles[k] not in texte_consigne]
    if manquantes:
        raise b54.BisociationRefusee("I-15 : règles absentes de la consigne figée du lecteur : " + ", ".join(manquantes))
    return True


consigne_saine = "Consigne figée d'essai.\n\n" + "\n\n".join(REG[k] for k in CLES_CONSIGNE) + "\n"
ok_sain = consigne_conforme(consigne_saine, REG)
sans_imposes = consigne_saine.replace(REG["elements_imposes"], "")
art_c1 = refus(lambda: consigne_conforme(sans_imposes, REG), "elements_imposes")
paraphrase = consigne_saine.replace(REG["affirmations_mixtes"], REG["affirmations_mixtes"].replace("agrégation", "agregation", 1))
art_c2 = refus(lambda: consigne_conforme(paraphrase, REG), "affirmations_mixtes")
print(f"  consigne figée : cas sain accepté {ok_sain} ; artefact « règle des éléments imposés absente » refusé {art_c1} ; "
      f"artefact « règle des mixtes modifiée d'un caractère » refusé {art_c2}")
INTERDITES_ESSAI = ["témoin", "exploratoire", "fusion", "bras méta", "gu et krenn", "gu krenn", "bisociation",  # aides_v54
                    "meta", "basique", "gu_krenn", "kimi", "claude", "opus", "sonnet", "fable", "gemini", "argon"]
with tempfile.TemporaryDirectory() as d:
    rap = ecrire(d, "rapport-essai.md", "rapport de contre-lecture d'essai (aucune valeur)\n", sceller=False)
    s_rap = sha(rap)
    relu = ecrire(d, "relu-exact.md", TEXTE, sceller=False)
    s_relu = sha(relu)
    cl = f"essai : brouillon relu {s_relu} ; rapport {s_rap}"
    remp_cl = json.dumps({"contre_lecture": cl}, ensure_ascii=False)[1:-1]
    rempli = TEXTE.replace(CL, remp_cl, 1).replace(AP, '"approbation_lazar": "essai R-999"', 1)
    an = ecrire(d, "annexe-remplie.md", rempli)
    pp, jeu = lire(an, sha(an), (relu, s_relu), (rap, s_rap))
    seul_cl = ecrire(d, "seul-cl.md", TEXTE.replace(CL, remp_cl, 1))
    r1 = refus(lambda: lire(seul_cl, sha(seul_cl), (relu, s_relu), (rap, s_rap)), "approbation_lazar")
    seul_ap = ecrire(d, "seul-ap.md", TEXTE.replace(AP, '"approbation_lazar": "essai R-999"', 1))
    r2 = refus(lambda: lire(seul_ap, sha(seul_ap), (relu, s_relu), (rap, s_rap)), "contre_lecture")
    residuel = ecrire(d, "residuel.md", rempli.replace('"essai R-999"', '"essai R-999 ; À REMPLIR"', 1))
    r3 = refus(lambda: lire(residuel, sha(residuel), (relu, s_relu), (rap, s_rap)), "approbation_lazar")
    print(f"  texte exact : seul contre_lecture rempli refusé {r1} ; seule approbation_lazar remplie refusée {r2} ; "
          f"« À REMPLIR » laissé dans approbation_lazar remplie refusé {r3} ; les deux remplis acceptés True")
    servi = b54.liste_servie(pp, "annexe")
    defs = dict(servi["definitions_niches"], **servi["definitions_structures"])
    phr = REG["phrases_servies"]
    servies = {k: (k in defs and v in defs[k]) for k, v in phr.items()}
    print(f"  phrases des règles servies par le code (liste_servie, definitions = « annexe ») : {sum(servies.values())} sur "
          f"{len(phr)} ({', '.join(k for k, v in servies.items() if v)})")
    a4_sain = fv53.garde_etiquettes(json.dumps(servi, ensure_ascii=False), INTERDITES_ESSAI)
    a4_regles = fv53.garde_etiquettes(" ".join(REG[k] for k in CLES_CONSIGNE), INTERDITES_ESSAI)
    servi_art = json.loads(json.dumps(servi))
    servi_art["definitions_niches"][NICHES[0]] += " Voir la fusion."
    try:
        fv53.garde_etiquettes(json.dumps(servi_art, ensure_ascii=False), INTERDITES_ESSAI)
        a4_art = False
    except fv53.EtiquetteDansEntree:
        a4_art = True
    print(f"  garde A4 (liste d'essai : {len(INTERDITES_ESSAI)} étiquettes) : liste servie acceptée {a4_sain} ; règles "
          f"acceptées {a4_regles} ; artefact « fusion » ajouté à une définition refusé {a4_art}")
    assert r1 and r2 and r3 and all(servies.values()) and a4_sain and a4_regles and a4_art and ok_sain and art_c1 and art_c2
distincts = {canon({k: v for k, v in composer(o5, o4).items() if not k.startswith("option_")}) for o5 in O5 for o4 in O4}
print(f"  combinaisons du bloc N4 : {len(O5) * len(O4)} ; jeux de paramètres distincts (clés option_* retirées) : "
      f"{len(distincts)} (CA3-08)")
print(f"  blocs JSON portant la clé parametres_bras_meta dans l'annexe : {len(PAR)} (forme_annexe_v56 en exige un seul) ; "
      f"clés de premier niveau des blocs : {', '.join(list(b[1])[0] for b in blocs)}")

print("\n== 17. Écart entre N4 v12 et cette annexe (CA3-01) : zéro paire du profil = 1 − P(≥ 1) ==")
print("  cité de N4 v12 (l. 44 ; chiffres de la contre-lecture du brouillon 1) : (a) 0,59–0,67 à 6 fiches, 0,25–0,36 à 10 ; "
      "(b) quinze fiches 0,06 ; (c) bande retirée 0,47 et 0,14 ; (d) canal ≤ 2 0,35 et 0,07 ; script v9, paramètres fictifs : "
      "0,31 et 0,03 ; (e) non chiffrée ; bande [2 ; 4] et réunion des passes : absentes")
_c = [P0["communication"][b53._niche_cle(NICHES[i], NICHES[j])] for i, j in itertools.combinations(range(K), 2)]
print(f"  paires de niches de canal ≤ 1 : {sum(x <= 1 for x in _c)} sur {len(_c)} ; de canal ≤ 2 : {sum(x <= 2 for x in _c)} "
      f"sur {len(_c)} (table du bloc N4)")
for lettre, o, ns in (("(a) repli comme mesure", "a", (6, 10)), ("(b) quinze fiches", "c1", (12, 15)),
                      ("(c) bande retirée", "b2", (6, 10)), ("(d) canal ≤ 2", "d1", (6, 10)),
                      ("nouvelle : bande [2 ; 4]", "b1", (6, 10)), ("nouvelle : passes réunies", "c2", (12, 20))):
    b1v = " ; ".join(f"n={n} {1 - FOUR[(o, n, 'annexe-b1', 0.3)][0]:.2f}" for n in ns)
    pav = " ; ".join(f"n={n} {1 - PRINC[(o, n)]['au_moins_un']:.2f}" for n in ns)
    print(f"  {lettre:26s} ({o:2s}) : loi du brouillon 1, structure 0,3 (§ 11) {b1v} ; loi par axe, SUPPOSÉ (§ 3) {pav}")
for nn in (6, 10):
    base = jouer(f"annexe-b4-n4-c2-seule-{nn}", composer("c2", "A"), nn, 2, loi="annexe-b1")
    reun = jouer(f"annexe-b4-n4-c2-reunie-{nn}", composer("c2", "A"), 2 * nn, 4, loi="annexe-b1")
    p1 = P_PERTE_TABLEAU * base["au_moins_un"] + (1 - P_PERTE_TABLEAU) * reun["au_moins_un"]
    print(f"  passes réunies avec la perte de la passe « tableau » ({P_PERTE_TABLEAU}), loi du brouillon 1, passe 1 à {nn} "
          f"fiches : P(≥ 1) {p1:.2f}, zéro paire {1 - p1:.2f}")
for nn in (6, 10):
    base = jouer(f"annexe-b2-principal-c2-seule-{nn}", composer("c2", "A"), nn, 2)
    reun = jouer(f"annexe-b2-principal-c2-reunie-{nn}", composer("c2", "A"), 2 * nn, 4)
    p1 = P_PERTE_TABLEAU * base["au_moins_un"] + (1 - P_PERTE_TABLEAU) * reun["au_moins_un"]
    print(f"  passes réunies avec la perte de la passe « tableau », loi par axe (mêmes tâches que § 3), passe 1 à {nn} fiches : "
          f"P(≥ 1) {p1:.2f}, zéro paire {1 - p1:.2f}")

# ---------------------------------------------------------------------------------------------------------------------
# 18 et 19. Ajouts du brouillon 5 (contre-lecture du brouillon 4, CA4-01 à CA4-09 ; synthèse du tour 1 v12 des nœuds)
# ---------------------------------------------------------------------------------------------------------------------
print("\n== 18. Synthèse du tour 1 v12 des nœuds (N4) ; chiffres de l'erratum v2 de N4 ==")
COLL = os.path.join(DEPOT, "brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/"
                           "collisionneur-noeuds-31-octobre-v1")
PIECES = {
    "synthèse du tour 1 v12": (os.path.join(DOSSIER_SYNTHESE, "synthese-noeuds-v12-tour1-v1.md"),
                               "e4d5a5c94c37534a7481772af2f1150f325be38c46c356353520c44cf2f85aa5"),
    "critères de lecture du tour 1": (os.path.join(DOSSIER_SYNTHESE, "criteres-lecture-noeuds-v12-tour1-v1.md"),
                                      "22edbf4751c205f6760a136963bfaebcede773bfdc3300e923ad8e5df4e3a529"),
    "question du tour 2 (sans compagnon)": (os.path.join(DOSSIER_SYNTHESE, "question-noeuds-v12-tour2-v1.md"), None),
    "question des nœuds v12": (os.path.join(COLL, "question-noeuds-decisionnels-collisionneur-v12.md"),
                               "a7fac44bd25c0b88f90c3ce50c23fa3a704675e57c3639ea0e4e56c1797102d3"),
    "relecture Opus de la synthèse": (os.path.join(COLL, "relecture-opus-synthese-noeuds-v12-tour1-v1.md"),
                                      "d1209130627f3e5c0ef7198016897c588a8b5ec3e36745084ec7b546475932b9"),
}
for nom, (ch, attendu) in PIECES.items():
    s = sha(ch)
    print(f"  {nom} : {os.path.basename(ch)} {s}" + ("" if attendu is None else f" ; attendue : {s == attendu}"))
    assert attendu is None or s == attendu, f"empreinte de {nom} différente de celle attendue"


def lire_texte(ch):
    with open(ch, encoding="utf-8") as f:
        return f.read()


SYN = lire_texte(PIECES["synthèse du tour 1 v12"][0])
SEC_N4 = SYN[SYN.index("# N4 — Annexe"):SYN.index("# N5 — ")]
SEC_Q2 = "\n".join(l for l in SYN[SYN.index("# Questions pour le tour 2"):].splitlines() if "N4" in l)
Q12 = lire_texte(PIECES["question des nœuds v12"][0])
PAR_N4 = next(l for l in Q12.splitlines() if l.startswith("**N4."))
Q2 = lire_texte(PIECES["question du tour 2 (sans compagnon)"][0])
LIG_N4 = next(l for l in Q2.splitlines() if l.startswith("- **N4**"))
print("  lettres d'option « (x) » trouvées (CA4-01) — section N4 de la synthèse ; questions du tour 2 sur N4 dans la synthèse ; "
      "paragraphe N4 de la question v12 ; ligne N4 de l'annexe du tour 2 servie avec la question du tour 2 :")
for nom, t in (("synthèse, section N4", SEC_N4), ("synthèse, questions du tour 2 (N4)", SEC_Q2),
               ("question v12, N4", PAR_N4), ("question du tour 2, ligne N4", LIG_N4)):
    print(f"    {nom} : " + " ; ".join(f"({x}) {t.count(f'({x})')}" for x in "abcdefghij"))
i_f = SEC_N4.index("**(f)**")
print(f"  contexte de « (f) » dans la synthèse, section N4 : {SEC_N4[i_f:i_f + 70]!r}")
assert SEC_N4.count("(g)") == 0 and SEC_N4.count("(h)") == 0 and PAR_N4.count("(g)") == 0 and PAR_N4.count("(h)") == 0
print("  (g) et (h) : absentes de la section N4 de la synthèse, du paragraphe N4 de la v12 et de la ligne N4 du tour 2 : True")
print("  recalcul des chiffres de la synthèse sur la mesure de la loi (28 rendus filtrés par un accord de 0,5 à 0,7 ; niche de "
      "probabilité vraie 0,10) :")
for acc in (0.5, 0.7):
    eff = 28 * acc
    print(f"    accord {acc} : effectif utile {eff:.1f} ; erreur-type {math.sqrt(0.1 * 0.9 / eff):.3f} ; "
          f"P(zéro fiche dans la niche) {0.9 ** eff:.3f}")
print("  N4 sous trois lois, structure 0,3 (zéro paire du profil = 1 − P(≥ 1) ; P(méta) entre crochets) ; « n6 fort » = "
      "reconstruction [n1 0,18 ; n2 0,12 ; n3 0,10 ; n4 0,05 ; n5 0,20 ; n6 0,35] de la loi défavorable de la contre-lecture "
      "du brouillon 1 (qui donnait 0,67 et 0,36 sous l'option (a)) :")
for lettre, o, ns in (("(a) repli comme mesure", "a", (6, 10)), ("(b) quinze fiches", "c1", (12, 15)),
                      ("(c) bande retirée", "b2", (6, 10)), ("(d) canal ≤ 2", "d1", (6, 10)),
                      ("(g) passes réunies", "c2", (12, 20)), ("(h) bande [2 ; 4]", "b1", (6, 10))):
    cel = []
    for nom_loi, loi in (("brouillon 1", "annexe-b1"), ("n6 fort", "n6-fort")):
        cel.append(f"{nom_loi} " + ", ".join(f"n={n} {1 - FOUR[(o, n, loi, 0.3)][0]:.2f} [{FOUR[(o, n, loi, 0.3)][1]:.2f}]"
                                             for n in ns))
    cel.append("par axe " + ", ".join(f"n={n} {1 - PRINC[(o, n)]['au_moins_un']:.2f} [{PRINC[(o, n)]['meta_profil']:.2f}]"
                                      for n in ns))
    print(f"    {lettre:24s} ({o:2s}) : " + " ; ".join(cel))
for nn in (6, 10):
    base = jouer(f"annexe-b5-n4-c2-seule-{nn}-n6-fort", composer("c2", "A"), nn, 2, loi="n6-fort")
    reun = jouer(f"annexe-b5-n4-c2-reunie-{nn}-n6-fort", composer("c2", "A"), 2 * nn, 4, loi="n6-fort")
    p1 = P_PERTE_TABLEAU * base["au_moins_un"] + (1 - P_PERTE_TABLEAU) * reun["au_moins_un"]
    pm = P_PERTE_TABLEAU * base["meta_profil"] + (1 - P_PERTE_TABLEAU) * reun["meta_profil"]
    print(f"  (g) passes réunies avec la perte de la passe « tableau » ({P_PERTE_TABLEAU}), loi « n6 fort », passe 1 à {nn} "
          f"fiches : P(≥ 1) {p1:.2f}, zéro paire {1 - p1:.2f}, P(méta) {pm:.2f}")
print("  n1–n2 hors du profil (c(n1, n2) = 2 ; accord à quatre du tour 1 : la paire que le programme fusionne ne reste pas "
      "dans le profil) — paires de niches dans le profil, puis P(≥ 1) [P(méta)] à 6 et 10 fiches, structure 0,3 :")
for o in ("a", "b1", "b2", "d1"):
    n_avec = int(matrice_profil(composer(o, "A")).sum() // 2)
    n_sans = int(matrice_profil(composer(o, "A"), c_n1n2=2).sum() // 2)
    cel = []
    for nom_loi, loi in (("brouillon 1", "annexe-b1"), ("n6 fort", "n6-fort")):
        rr = [jouer(f"annexe-b5-c12-{o}-{n}-{loi}", composer(o, "A"), n, 2, loi=loi, c_n1n2=2) for n in (6, 10)]
        cel.append(f"{nom_loi} " + ", ".join(f"n={n} {r['au_moins_un']:.2f} [{r['meta_profil']:.2f}] (avec n1–n2 "
                                             f"{FOUR[(o, n, loi, 0.3)][0]:.2f})" for n, r in zip((6, 10), rr)))
    cel.append("par axe " + ", ".join(f"n={n} {SENS[(o, n)][2]['au_moins_un']:.2f} [{SENS[(o, n)][2]['meta_profil']:.2f}] "
                                      f"(avec n1–n2 {PRINC[(o, n)]['au_moins_un']:.2f})" for n in (6, 10)))
    print(f"    {o:3s} : {n_avec} → {n_sans} paires sur {K * (K - 1) // 2} ; " + " ; ".join(cel))

print("\n== 19. Brouillon 5 contre brouillon 4 : texte hors bloc N4, blocs JSON, comptes (CA4-08, CA4-09) ==")
B4 = os.path.join(os.path.dirname(ANNEXE), "annexe-bras-meta-v1-brouillon4.md")
S_B4 = sha(B4)
assert S_B4 == "397e1cbc7483e7c5106bd859a77514605166e1fb699eb4b4ab5ed2730d15fb7c", "brouillon 4 : empreinte différente"
T4 = lire_texte(B4)
assert len(MARQ_DEBUT.findall(T4)) == 1 and T4.count(MARQ_FIN) == 1
HORS4 = T4[:MARQ_DEBUT.search(T4).end()] + T4[T4.index(MARQ_FIN):]
print(f"  brouillon 4 : {S_B4} ; texte hors bloc N4 du brouillon 4 : {hashlib.sha256(HORS4.encode('utf-8')).hexdigest()}")
DIFF = list(difflib.unified_diff(HORS4.splitlines(), HORS.splitlines(), "brouillon4-hors-bloc-N4", "brouillon5-hors-bloc-N4",
                                 lineterm="", n=0))
PASSAGES = [l for l in DIFF if l.startswith("@@")]
RETIREES = sum(1 for l in DIFF if l.startswith("-") and not l.startswith("---"))
AJOUTEES = sum(1 for l in DIFF if l.startswith("+") and not l.startswith("+++"))
print(f"  écart du texte hors bloc N4 (difflib, sans contexte) : {len(PASSAGES)} passages ; {RETIREES} lignes du brouillon 4 "
      f"remplacées ou retirées ; {AJOUTEES} lignes du brouillon 5 ; lignes hors bloc N4 : {len(HORS4.splitlines())} → "
      f"{len(HORS.splitlines())} ; empreinte de l'écart (lignes jointes par \\n) "
      f"{hashlib.sha256(chr(10).join(DIFF).encode('utf-8')).hexdigest()}")
print("  passages (numéros de ligne du texte hors bloc N4, brouillon 4 puis brouillon 5) : " + " ".join(
    p.replace("@@ ", "").replace(" @@", "") for p in PASSAGES))
blocs4 = {list(o)[0]: o for _, o in (( m.span(), json.loads(m.group(1))) for m in BLOC.finditer(T4))}
blocs5 = {list(o)[0]: o for _, o in blocs}
for cle in blocs5:
    print(f"  bloc {cle} : identique au brouillon 4 (JSON canonique, champs libres compris) {canon(blocs5[cle]) == canon(blocs4.get(cle))}")
STRUCT_SERVIES = [k for k in REG["phrases_servies"] if k not in NICHES]
print(f"  CA4-09 : structures portant une phrase servie {len(STRUCT_SERVIES)} ; niches {len(REG['phrases_servies']) - len(STRUCT_SERVIES)} ; "
      f"« neuf structures » dans le brouillon 5 : {TEXTE.count('neuf structures')} ; « huit structures » : "
      f"{TEXTE.count('huit structures')}")
assert TEXTE.count("neuf structures") == 0 and len(STRUCT_SERVIES) == 8
RESTANTS = {m: HORS.count(m) for m in ("A-VENIR", "«C12-")}
print("  marqueurs de rédaction restants dans le texte hors bloc N4 : "
      + " ; ".join(f"« {m} » {c}" for m, c in RESTANTS.items()))
assert not any(RESTANTS.values()), "marqueurs de rédaction restants hors bloc N4 : chiffres non remplis"

assert N_MARQUEURS == 0, "marqueurs ⟦…⟧ restants dans l'annexe : chiffres non remplis"
print("fin")
