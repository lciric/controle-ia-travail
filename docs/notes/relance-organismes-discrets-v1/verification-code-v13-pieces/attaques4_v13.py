"""Partie 4 : rejeu de l'étape (n) ; second fichier des grandeurs ; formes des « mêmes lectures »."""
import contextlib, io, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, "/home/user/controle-ia-travail/tests")
import aide_bras_a_v13 as A
with contextlib.redirect_stdout(io.StringIO()):
    import test_analyse_bras_a_v13 as TA
from controle_ia.organismes_discrets import analyse_bras_a_v13 as an, arrets_bras_a_v12 as ar
from controle_ia.gardes import GardeArret
T = Path(tempfile.mkdtemp())
def essai(nom, f):
    try:
        r = f(); print(f"PASSE   {nom} -> {str(r)[:180]}"); return r
    except ar.ArretDeLaLectureDeLaDiscretion as e:
        print(f"ARRET   {nom} -> {e.constat()}"); return e
    except GardeArret as e:
        print(f"GARDE   {nom} -> {str(e)[:200]}"); return e
    except BaseException as e:
        print(f"PANNE   {nom} -> {type(e).__name__}: {str(e)[:100]}"); return e
X = TA.ArretALEtapeN(T)
go = "GO-2099-06-01-01"; c, fg = X.reprise(X.L.piece, go)
f1, d1 = X.scores(); s1 = X.sortie_refaite(d1)
essai("ouverture (n), cohérente", lambda: X.ouvrir(s1, c, go, fg)["lectures_refaites_coherentes"])
# panne simulée : rien lu ; rejeu de l'ouverture sous le même acte, sans contrôle
essai("rejeu de l'ouverture, même sortie refaite, sans contrôle", lambda: X.ouvrir(s1, c, go, fg)["lectures_refaites_coherentes"])
autres = TA.en_rangs(TA.lignes_de_scores("juge", "dose-0.50", pas=2, taches=TA.VER[:2]))
f2, d2 = X.scores(lignes=autres); s2 = X.sortie_refaite(d2)
essai("rejeu sous le même acte, AUTRE sortie refaite (autre fichier des scores)", lambda: X.ouvrir(s2, c, go, fg)["lectures_refaites_coherentes"])
essai("lecture du fichier des scores 2 sous la sortie refaite 1", lambda: type(X.lire(f2, s1, c)).__name__)
s = essai("lecture du fichier des scores 1", lambda: X.lire(f1, s1, c))
par_dose = {d: TA.desappariees(4) for d in (0.25, 0.5, 0.75, 1.0)}
aires = an.aires_conditionnelles(s, par_dose, TA.VER, TA.ENTROPIE)
bons = dict(aires_conditionnelles=aires, autres_grandeurs={"note": "essai"}, rangs=s, piece_scellee=s1, configuration_scellee=c)
essai("fichier des grandeurs (n), premier", lambda: an.ecrire_fichier_des_grandeurs_de_l_etape_n(**bons, sortie_d_origine=X.L.piece).name)
essai("fichier des grandeurs (n), second, autres grandeurs", lambda: an.ecrire_fichier_des_grandeurs_de_l_etape_n(**dict(bons, autres_grandeurs={"note": "autre"}), sortie_d_origine=X.L.piece).name)
essai("lecture du fichier des scores 1 après le fichier des grandeurs", lambda: type(X.lire(f1, s1, c)).__name__)
essai("ouverture de nouveau après le fichier des grandeurs", lambda: X.ouvrir(s1, c, go, fg)["lectures_refaites_coherentes"])

print("=== formes des « mêmes lectures »")
o = json.loads(Path(X.L.piece).read_text(encoding="utf-8"))
def cas(nom, modif):
    t = json.loads(json.dumps(o)); modif(t)
    p = A.piece(T, t if not isinstance(t, str) else t)
    essai(nom, lambda: an.lectures_refaites_coherentes(p, X.L.piece))
cas("identique", lambda t: None)
cas("autre provenance seule", lambda t: t.update(piece_source="autre"))
cas("autres agrégateurs (somme sans état)", lambda t: t.update(agregateur_somme_sans_etat={k: 0.99 for k in t["agregateur_somme_sans_etat"]}))
cas("autres réglages", lambda t: t["reglages"].update(statistique_agregateur="autre"))
cas("autres plis", lambda t: t.update(plis={"t00": 1, "t01": 0}))
d0 = next(iter(o["lectures"])); m0 = next(iter(o["lectures"][d0]))
print("   une lecture :", json.dumps(o["lectures"][d0][m0])[:300])
cas("une lecture : champ de plus", lambda t: t["lectures"][d0][m0].update(note="x"))
cas("lectures en ordre inverse des doses", lambda t: t.update(lectures=dict(reversed(list(t["lectures"].items())))))
