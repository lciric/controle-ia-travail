"""Brouillon 4 de l'addendum 1 des gardes (R1 v4) = brouillon 3 + entrée « Contre-lecture 2 » + GO de Lazar (fille 6, ordre
`docs/procedures/ordre-fille-6-etape-F-r1-v4-v1.md`, étape A). Chaque « ancien » doit apparaître exactement une fois ; arrêt sinon.
Usage (racine de l'arbre) : python3 -I brouillons/etape-F-r1-v4-v1/ecrire-brouillon4-v1.py ENTREE SORTIE JOURNAL"""
import hashlib, sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd() / "src"))   # -I ignore PYTHONPATH : code du dépôt lu depuis la racine de l'arbre

ENTREE, SORTIE, JOURNAL = (Path(a) for a in sys.argv[1:4])
SHA_B3 = "81a04e7b9d0dc075bec03371a64f96c3c70fa1c540b7c32c2bd2486b953e6110"
t = ENTREE.read_text(encoding="utf-8")
sha = hashlib.sha256(t.encode("utf-8")).hexdigest()
if sha != SHA_B3:
    sys.exit(f"ARRÊT : brouillon 3 d'empreinte {sha} ≠ {SHA_B3}")

ANCIEN_CL2 = t[t.index("Contre-lecture 2 (R2) : à faire"):]
assert ANCIEN_CL2.endswith("c'est attendu d'un brouillon 2.\n"), "ARRÊT : fin de l'entrée 2 inattendue"
NOUVEAU_CL2 = (
    "Contre-lecture 2 (R2) : faite le 5 novembre 2026 (20:03 → 20:12 UTC) par un sous-agent neuf (fille 9, session de\n"
    "contre-lectures, lignée Claude Opus 5.5) sur la consigne\n"
    "`docs/notes/runs-r1-r2-r4-v1/etape-F-v1/consigne-contre-lecture-addendum-gardes-v2.md` (`9b77376c589a6cfa…`) ; brouillon relu :\n"
    "`prereg/addendum-1-gardes-analyses-r1-v4-v1-brouillon2.md` (`465b5334c4f47f6a1db5e3d757a46420087f0f3219fa3eac858653d048b3000b`) avec le\n"
    "rapport du rédacteur v2 (`ff6cc2f5cd755643…`) et le code v8, v9, v5 ; rapport :\n"
    "`docs/notes/runs-r1-r2-r4-v1/etape-F-v1/contre-lecture-v2/contre-lecture-addendum-gardes-v2.md`\n"
    "(`24d8c769bfacf132c2d1294144cdfc978beccb5a64bc923516f8f80ad307ab67`), couples `couples-contre-lecture-addendum-gardes-v2.json`\n"
    "(`65b802ad6ee3f74fc528b1d4b23d9ea809a0dfe0eedd28cc54dd8554ecb0ac1c`), corrections de procédure `corrections-procedure-v2.md`\n"
    "(`6b36d6a20df1a05c…`). Verdict : scellable après couples ; aucun point bloquant (K1, K2, K3 faites et éprouvées). Traitement\n"
    "(brouillon 3, `81a04e7b…`) : dix points lus ; les points 1, 2, 3, 6, 7, 9, 10 sont des notes (conformes, rien à changer) ;\n"
    "les points 4 et 5 sont corrigés par les six couples K-1 à K-6, tous **acceptés** et appliqués à l'octet par script, dans\n"
    "l'ordre (`brouillons/etape-F-r1-v4-v1/appliquer-couples-v3.py`, chaque « ancien » unique au moment de son application) ;\n"
    "le point 8 (commandes de la mère) est corrigé hors de ce texte (rapport du rédacteur v3, section 5, P1) ; la\n"
    "recommandation du point 3 (nommer l'arrêt neuf K3 dans la demande de GO, avec les deux écarts) est suivie\n"
    "(GO-2026-11-06-02). Aucun couple refusé ; aucune correction de code.\n"
)
ANCIEN_GO = "<<GO_LAZAR_SECOND_PASSAGE>>"
NOUVEAU_GO = "GO-2026-11-06-02 (`registres/go.md` de `main`, mot de Lazar du 6 novembre 2026 vers 11:32 UTC)"

lignes = []
for nom, ancien, nouveau in (("entrée Contre-lecture 2", ANCIEN_CL2, NOUVEAU_CL2), ("GO de Lazar", ANCIEN_GO, NOUVEAU_GO)):
    n = t.count(ancien)
    if n != 1:
        sys.exit(f"ARRÊT : « {nom} » trouvé {n} fois (1 exigé)")
    ligne = t[: t.index(ancien)].count("\n") + 1
    t = t.replace(ancien, nouveau)
    lignes.append(f"- {nom} : 1 occurrence, ligne {ligne} de l'entrée au moment de l'application")

# (iii) noms vérifiés contre le code v8, v9, v5 (noms seulement, aucune donnée)
from controle_ia.analyse_principale_r1_r2 import constantes_v1 as K1, constantes_v8 as K8, constantes_v9 as K9
from controle_ia.analyse_blanche_noire import constantes_v3 as C3, constantes_v5 as C5
noms = {
    "prereg/fiche-reception-principale-r1-r2-v1-relance-v4.json": f"format lu par lire_fiche (entrees_v1) : {K1.FORMAT_FICHE}",
    "prereg/fiche-reception-blanche-noire-v3-relance-v4.json": f"format lu par lire_fiche_v3 (entrees_v3) : {C3.FORMAT_FICHE} (C5 : {C5.FORMAT_FICHE})",
    "analyse-principale-r1-r2-v1.json": f"sortie de lecture_v8 : diag/<run-analyse>/{K8.NOM_SORTIE}.json (ecrire_resultat)",
}
for n, quoi in noms.items():
    if n not in t:
        sys.exit(f"ARRÊT : nom {n} absent du brouillon")
    lignes.append(f"- nom `{n}` présent ({t.count(n)} fois) ; {quoi}")
assert K8.NOM_SORTIE == "analyse-principale-r1-r2-v1" and K1.FORMAT_FICHE == "fiche-reception-principale-r1-r2-v1"
assert C5.FORMAT_FICHE == C3.FORMAT_FICHE == "fiche-reception-blanche-noire-v3"
lignes.append(f"- sortie de lecture_v9 : {K9.NOM_SORTIE} ; de lecture_v5 : {C5.NOM_SORTIE}")

SORTIE.write_text(t, encoding="utf-8")
sha4 = hashlib.sha256(t.encode("utf-8")).hexdigest()
from controle_ia.prereg import problemes
p = problemes(SORTIE)
JOURNAL.write_text("# Journal du brouillon 4 (fille 6)\n\n" + f"- entrée : {ENTREE} ({sha})\n- sortie : {SORTIE} ({sha4})\n"
                   + "\n".join(lignes) + f"\n- problemes() : {p}\n", encoding="utf-8")
print(sha4); print(p)
