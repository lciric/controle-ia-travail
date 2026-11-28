"""Essais de la vérification des corrections du brouillon 7 de l'addendum de P3 (partie A, texte).

Module et tests importés d'une copie (`copie/`, empreintes contrôlées au lancement) ; code gelé du dépôt importé,
jamais modifié ; toute simulation reste dans ce processus. Rien n'est écrit hors de `b7/` (fichiers jetables sous
`b7/tmp/`). Lancer depuis n'importe où :
    PYTHONPATH=/home/user/controle-ia-travail/src PYTHONDONTWRITEBYTECODE=1 <python> -B essais_b7.py [essai…]
Essais : cles, p17, g14, g15, p8, validateur, regex (tous par défaut).
"""
import sys

sys.dont_write_bytecode = True

import copy  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
from pathlib import Path  # noqa: E402

B7 = Path(__file__).resolve().parent
COPIE = B7 / "copie"
TMP = B7 / "tmp"
DEPOT = Path("/home/user/controle-ia-travail")
A = B7.parents[1]
TEXTE_B7 = A / "P3-addendum-lecture-complementaire-v1-brouillon7.md"
for _d in (str(DEPOT / "src"), str(DEPOT / "tests"), str(COPIE)):
    if _d not in sys.path:
        sys.path.insert(0, _d)


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


ATTENDU = {COPIE / "complements_p3_v1.py": "2b16179d4451c3f10c0c1053687d76f68c9b32b43f2b460463d844ab45c15996",
           COPIE / "test_complements_p3_v1.py": "7605c2051e853d9707e59a13ccc26a5b99678f3efb67748f00d710c4336f8f0d",
           TEXTE_B7: "c3e9c27f3da2eb3270a8b52b24e9533734a640bb6453f2bca463fad766bb0c28"}
for _p, _e in ATTENDU.items():
    assert sha(_p) == _e, f"empreinte de {_p} ≠ {_e[:12]}"

import numpy as np  # noqa: E402

import complements_p3_v1 as cp  # noqa: E402
import test_complements_p3_v1 as tc  # noqa: E402
from test_premier_test_ia_lecture import P  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.manifeste import graines as graines_des_cles  # noqa: E402
from controle_ia.premier_test_ia import lecture as lp  # noqa: E402

assert Path(cp.__file__).resolve().parent == COPIE.resolve(), cp.__file__
TEXTE = TEXTE_B7.read_text(encoding="utf-8")


def titre(x):
    print(f"\n==================== {x}", flush=True)


# ---------------------------------------------------------------------------------------------- précision 12 : clés

def essai_cles():
    titre("précision 12 : liste fermée des clés de graines, texte contre `cles_addendum`")
    m = re.search(r"^12\. Clés de graines.*?(?=^13\. )", TEXTE, re.S | re.M)
    para = " ".join(m.group(0).split())
    print("paragraphe lu :", para[:160], "…")
    cles_texte = []
    motifs = re.findall(r"`(addendum/[^`]+)`", para)
    print("motifs entre accents graves :", motifs)
    # <jeu> écrit en mots dans le texte : correspondance déduite par le relecteur (non écrite au texte)
    m_jeu = re.search(r"`<jeu>` parmi (.*?), `<forme>`", para)
    mots_jeu = m_jeu.group(1)
    print("<jeu> tel qu'écrit :", repr(mots_jeu))
    jeux_deduits = ["saboteur-honnete", "saboteur-temoin", "saboteur-mention"]
    m_forme = re.search(r"`<forme>` parmi (.*?) ;", para)
    formes = re.findall(r"`([a-z_]+)`", m_forme.group(1))
    print("<forme> :", formes)
    for mot in motifs:
        if "<jeu>" in mot:
            cles_texte += [f"addendum/A7/{p}/{j}/{f}" for p in P for j in jeux_deduits for f in formes]
            continue
        prefixe, _, reste = mot.partition("{")
        objets = [x.strip() for x in reste.rstrip("}").split(",")] if reste else [""]
        for p in (P if "<p>" in prefixe else [None]):
            base = prefixe.replace("<p>", p) if p else prefixe
            cles_texte += [base + o for o in objets]
    module = cp.cles_addendum(P)
    manifeste = list(graines_des_cles(module, cp.ENTROPIE_P3))
    print("nombre : texte", len(cles_texte), "; module", len(module), "; manifeste", len(manifeste),
          "; uniques texte", len(set(cles_texte)))
    print("texte = module (ensembles) :", set(cles_texte) == set(module))
    print("dans le texte seulement :", sorted(set(cles_texte) - set(module)))
    print("dans le module seulement :", sorted(set(module) - set(cles_texte)))
    print("manifeste = module (liste) :", manifeste == module)
    print("objets de A1 dans le module :", [k.split("/")[-1] for k in module if k.startswith(f"addendum/A1/{P[0]}/")])
    print("jeux de A7 dans le module :", sorted({k.split("/")[3] for k in module if k.startswith(f"addendum/A7/{P[0]}/")}))
    # chaque clé est lue par le module (texte du module)
    src = Path(cp.__file__).read_text(encoding="utf-8")
    for motif in ("addendum/A1/{p}/{nom}", "addendum/A1/{p}/placebo", "addendum/A2/{p}/aire-cout",
                  "addendum/A2/{p}/fenetres", "addendum/A2/{p}/blocs", "addendum/A2/{p}/juste-avant",
                  "addendum/A3/{p}/contrastes", "addendum/A4/{p}/T4-tranches-internes",
                  "addendum/A4/{p}/T1-intra-tache", "addendum/A4/{p}/T1-sensibilite", "addendum/A5/{p}/T2-propre",
                  "addendum/A5/{p}/aire-cout-propre", "addendum/A6/sans-sonde/{cle}", "addendum/A7/{p}/{jeu}/{k}"):
        print(f"  lue par le module : {motif!r} → {src.count(motif)} occurrence(s)")


# ---------------------------------------------------------------------------------------------- précision 17

def _resume(x):
    return {"etat": x["etat"], "calculs_en_echec": x["calculs_en_echec"],
            "controles": [(c["test"], c["cible"], c["controle_contraire"], c.get("reserve")) for c in x["controles"]]}


def essai_p17():
    titre("précision 17 : « une entrée qui tombe en échec » — calcul en échec contre garde hors d'un calcul")
    cp.TIRAGES_AIRE, cp.TIRAGES_COUT = 60, 500
    src = tc._sc_sain()
    lec = tc._lecture(src)
    D = cp.preparer_donnees(src, lec, tc.G)
    print("conclusions établies :", D["etablies"])
    x0 = cp._executer_entree("A1", P[0], D, tc.G)
    print("(0) A1 tel quel :", json.dumps(_resume(x0), ensure_ascii=False))
    print("    états des calculs :", {k: v.get("etat") for k, v in x0["descriptif"].items() if isinstance(v, dict)})

    vrai = cp.ecart_conjoint

    def faux(*a, **k):
        if str(k.get("quoi", "")).endswith(" T4"):
            raise GardeArret("échec simulé dans le calcul T4 (dans un calcul)")
        return vrai(*a, **k)

    cp.ecart_conjoint = faux
    try:
        xa = cp._executer_entree("A1", P[0], D, tc.G)
    finally:
        cp.ecart_conjoint = vrai
    ra = _resume(xa)
    print("(a) GardeArret DANS le calcul T4 :", json.dumps(ra, ensure_ascii=False))
    print("    contrôles « (entrée entière) » ajoutés :", [c for c in ra["controles"] if "entrée entière" in c[0]])

    vraie_perm = lp._permuter_dans_les_taches

    def perm_en_echec(*a, **k):
        raise GardeArret("échec simulé hors d'un calcul (permutation du placebo)")

    lp._permuter_dans_les_taches = perm_en_echec
    try:
        xb = cp._executer_entree("A1", P[0], D, tc.G)
    finally:
        lp._permuter_dans_les_taches = vraie_perm
    rb = _resume(xb)
    print("(b) GardeArret HORS d'un calcul :", json.dumps({"etat": rb["etat"], "calculs_en_echec": rb["calculs_en_echec"]},
                                                         ensure_ascii=False))
    print("    contrôles « (entrée entière) » ajoutés :", [c for c in rb["controles"] if "entrée entière" in c[0]])

    # garde 11 : une entrée est « en échec » si l'un de ses calculs l'est ; synthèse sur le seul cas (a)
    vides = {a: ({"etat": cp.CALCULE, "calculs_en_echec": [], "descriptif": {}, "controles": []} if a in cp.SANS_SONDE
                 else {p: (xa if (a, p) == ("A1", P[0]) else {"etat": cp.CALCULE, "calculs_en_echec": [],
                                                              "descriptif": {}, "controles": []}) for p in P})
             for a in cp.ANALYSES}
    s = cp.synthese(vides, D["etablies"], False)
    print("(a) synthèse : entrées en échec (garde 11) :", s["entrees_en_echec"])
    print("    réserves :", [(r["nom"], r["cible"], r["test"]) for r in s["reserves_addendum"]])
    print("    recommandation :", json.dumps(s["recommandation_au_verdict_R13"], ensure_ascii=False, indent=1))
    cibles_a1 = [cp._cible(c, P[0]) for c in cp.VISEES["A1"]]
    etablies_a1 = [c for c in cibles_a1 if c in D["etablies"]]
    lecture_litterale = {c: "reserve_A1_non_lue (entrée entière)" for c in etablies_a1}
    obtenu = {c: sorted({r["nom"] for r in s["reserves_addendum"] if r["cible"] == c}) for c in etablies_a1}
    print("    lecture littérale du brouillon 7 (entrée en échec ⇒ « non lu » d'entrée entière sur chaque cible visée) :",
          lecture_litterale)
    print("    réserves rendues par le module, par cible visée et établie :", obtenu)


# ---------------------------------------------------------------------------------------------- garde 14

def essai_g14():
    titre("garde 14 : découpe des textes (ligne exactement vide, ligne d'espaces, motif « garde 4 »)")
    TMP.mkdir(exist_ok=True)
    bon = [json.dumps({"episode": "e0", "condition": "honnete", "tache": "t0", "pas": k, "texte": f"x{k} y"},
                      ensure_ascii=False).encode("utf-8") for k in range(3)]
    cas = {"sain : lignes vides au milieu et à la fin": bon[0] + b"\n\n" + bon[1] + b"\n" + bon[2] + b"\n\n",
           "ligne de trois espaces": bon[0] + b"\n   \n" + bon[1] + b"\n",
           "ligne d'une tabulation": bon[0] + b"\n\t\n" + bon[1] + b"\n",
           "ligne d'un retour chariot seul": bon[0] + b"\n\r\n" + bon[1] + b"\n",
           "fin de ligne CRLF sur une ligne valide": bon[0] + b"\r\n" + bon[1] + b"\n",
           "octet UTF-8 invalide": bon[0] + b"\n\xff\n"}
    for nom, octets in cas.items():
        f = TMP / "textes.jsonl"
        f.write_bytes(octets)
        source = {"episodes-p3": {"textes": "textes.jsonl", "textes_sha256": sha(f)}}
        try:
            t = cp.charger_textes(TMP, source)
            print(f"  {nom} : lu, {len(t)} textes ; U+2028 gardé : {all(chr(0x2028) in x['texte'] for x in t)}")
        except GardeArret as e:
            print(f"  {nom} : ARRÊT « {e} »")
    f.unlink()


# ---------------------------------------------------------------------------------------------- garde 15

def essai_g15():
    titre("garde 15 : forme du nom du run et préenregistrement de la commande (exiger_commande)")
    bon = "prereg/P3-addendum-lecture-complementaire-v1.md"
    for nom, prereg in (("20261020-130000-addendum-p3", bon), ("20261020-130000-addendum-p3-bis", bon),
                        ("20261020-130000-autre", bon), ("2026102-130000-addendum-p3", bon),
                        ("20261020-130000-addendum-p3\n", bon), ("20261020-130000-addendum-p3", "./" + bon),
                        ("20261020-130000-addendum-p3", "prereg/P3-premier-test-i-a-v1.md")):
        try:
            cp.exiger_commande(nom, prereg)
            print(f"  {nom!r}, {prereg!r} : accepté")
        except GardeArret as e:
            print(f"  {nom!r}, {prereg!r} : ARRÊT « {e} »")
    import inspect
    src = inspect.getsource(cp.executer)
    ordre = [x for x in ("exiger_commande", "exiger_garde_1", "exiger_lecture_decisive", "exiger_anteriorite",
                         "charger_textes", "controler_entrees", "exiger_coherence", "familles_attention",
                         "localisation(", "exiger_premier_passage", "creer_manifeste", "verifier(chemin_l)", "try:",
                         "analyser_addendum", "ecrire_resultat")]
    print("  ordre dans `executer` :", sorted(ordre, key=src.index))
    print("  graines passées à la fonction pure :", "analyser_addendum(source, lecture, manifeste[\"graines\"])" in src)
    print("  `exiger_graines` appelée dans `preparer_donnees` :",
          "exiger_graines(graines, principales)" in inspect.getsource(cp.preparer_donnees))


# ---------------------------------------------------------------------------------------------- précision 8

def essai_p8():
    titre("précision 8 : chaque conclusion établie visée par au moins un contrôle lu (non « sans objet »)")
    cp.TIRAGES_AIRE, cp.TIRAGES_COUT = 60, 500
    src = tc._sc_sain()
    lec = tc._lecture(src)
    s = cp.analyser_addendum(src, lec, tc.G)
    par_cible = {c: [] for c in s["conclusions_etablies"]}
    for a in cp.ANALYSES:
        entrees = [(None, s["analyses"][a])] if a in cp.SANS_SONDE else list(s["analyses"][a].items())
        for _, x in entrees:
            for c in x["controles"]:
                if c["controle_contraire"] != cp.SANS_OBJET:
                    par_cible[c["cible"]].append(a)
    for c, v in par_cible.items():
        print(f"  {c} : {len(v)} contrôles lus ({', '.join(sorted(set(v)))})")
    print("  audit :", json.dumps(s["audit_symetrie_addendum"], ensure_ascii=False)[:400])


# ---------------------------------------------------------------------------------------------- validateur

def essai_validateur():
    titre("validateur `prereg.problemes` : brouillon 7 tel quel, puis rempli de valeurs factices bien formées")
    from controle_ia.prereg import problemes
    print("  brouillon 7 (copie) :", problemes(COPIE / "brouillon7-copie.md"))
    marqueurs = sorted(set(re.findall(r"<<([A-Z0-9_]+)>>", TEXTE)))
    print("  marqueurs :", marqueurs, "; occurrences :", {m: TEXTE.count(f"<<{m}>>") for m in marqueurs})
    t = TEXTE
    for k, m in enumerate(marqueurs):
        if m.startswith("EMPREINTE"):
            v = hashlib.sha256(m.encode()).hexdigest()
        elif m.startswith("VERDICT"):
            v = "scellable après corrections"
        else:
            v = "165"
        t = t.replace(f"<<{m}>>", v)
    TMP.mkdir(exist_ok=True)
    f = TMP / "brouillon7-rempli-factice.md"
    f.write_text(t, encoding="utf-8")
    print("  rempli (valeurs factices) :", problemes(f))
    f.unlink()


# ---------------------------------------------------------------------------------------------- expressions lues

def essai_regex():
    titre("expressions lues dans le texte par les gardes (première occurrence = en-tête)")
    from controle_ia.harnais.validation_reelle import COMMIT_CITE, ENTROPIE_CITEE
    for nom, rx in (("module", cp.EMPREINTE_MODULE_CITEE), ("tests", cp.EMPREINTE_TESTS_CITEE),
                    ("commit", COMMIT_CITE), ("entropie", ENTROPIE_CITEE)):
        tous = list(rx.finditer(TEXTE.replace("<<EMPREINTE_MODULE>>", "a" * 64).replace("<<EMPREINTE_TESTS>>", "b" * 64)))
        print(f"  {nom} : {len(tous)} correspondance(s), lignes {[TEXTE.count(chr(10), 0, x.start()) + 1 for x in tous]}")


ESSAIS = {"cles": essai_cles, "p17": essai_p17, "g14": essai_g14, "g15": essai_g15, "p8": essai_p8,
          "validateur": essai_validateur, "regex": essai_regex}

if __name__ == "__main__":
    for nom in (sys.argv[1:] or list(ESSAIS)):
        ESSAIS[nom]()
    for _p, _e in ATTENDU.items():
        assert sha(_p) == _e
    print("\nempreintes de la copie et du brouillon 7 inchangées à la fin")
