"""Essai simulé du collisionneur v9-v8o, voie --google-arriere-plan (aucun réseau : lire_json, envoyer, DORMIR remplacés)."""
import contextlib, importlib.util, io, json, os, sys
sys.path.insert(0, "/home/user/controle-ia-travail/src")
spec = importlib.util.spec_from_file_location("c", "/home/user/controle-ia-travail/docs/notes/collisionneur-v9/collisionneur_v9_v8o.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
os.environ["GEMINI_API_KEY"] = "cle-factice"
m = dict(c.CATALOGUE["carbon"], espece="carbon")
c.DORMIR = lambda s: None
suppr = []
@contextlib.contextmanager
def faux_envoyer(requete, delai, cle, **k):
    suppr.append(requete.get_method()); yield io.BytesIO(b"{}")
c.envoyer = faux_envoyer
def fini(usage, statut="completed", texte="Bonjour.", **extra):
    d = {"id": "v1_abc", "status": statut, "model": "gemini-4-carbon", "usage": usage,
         "steps": [{"type": "thought"}, {"type": "model_output", "content": [{"type": "text", "text": texte}]}]}
    d.update(extra); return d
def lancer(seq, cas):
    seq = list(seq)
    def faux(requete, delai, cle):
        x = seq.pop(0)
        if isinstance(x, Exception): raise x
        return x
    c.lire_json = faux
    r = c.appeler_gemini_arriere_plan(m, "Bonjour ?", m["max"])
    st = c.juger(m, r, "Bonjour ?", 9.9, garde=10**6, max_tokens=m["max"])
    print(f"{cas:<42} -> {st[0]:<22} fin={r.fin} lu={r.usage_lu} interrompue={r.interrompue} nom={r.nom_lot}")
    return r, st
cree = {"id": "v1_abc", "status": "in_progress"}
U = lambda i, o, t, tot: {"total_input_tokens": i, "total_output_tokens": o, "total_thought_tokens": t, "total_tokens": tot}
res = {}
res["separees"] = lancer([cree, fini(U(100, 50, 200, 350))], "pensées séparées (total = e+s+p)")
res["comprises"] = lancer([cree, fini(U(100, 250, 200, 350))], "pensées comprises (total = e+s)")
res["illisible"] = lancer([cree, fini(U(100, 50, 200, 999))], "total incohérent")
res["zero"] = lancer([cree, fini(U(100, 50, 0, 150))], "zéro pensée")
res["incomplete"] = lancer([cree, fini(U(100, 50, 200, 350), statut="incomplete")], "statut incomplete")
res["vide"] = lancer([cree, fini(U(100, 0, 200, 300), texte="")], "completed sans texte")
res["erreur"] = lancer([cree, fini(U(100, 50, 200, 350), error={"code": 13})], "completed avec erreur")
res["failed"] = lancer([cree, {"id": "v1_abc", "status": "failed"}], "statut failed")
refus = [c.EchecSansEnvoi("HTTP 404")] * 5 + [{}]
res["refus"] = lancer([cree] + refus, "cinq relevés refusés")
attendus = {"separees": "OK", "comprises": "OK", "illisible": "USAGE_ABSENT", "zero": c.STATUT_SANS_PENSEES,
            "incomplete": "ANOMALIE", "vide": "VIDE", "erreur": "INTERROMPU", "failed": "INTERROMPU", "refus": "INTERROMPU"}
assert res["separees"][0].usage["sortie"] == 250 and res["comprises"][0].usage["sortie"] == 250, "comptage des pensées"
for k, v in attendus.items():
    assert res[k][1][0] == v, (k, res[k][1][0], v)
assert "DELETE" in suppr, "suppression"
m2 = dict(m, niveau_reflexion="high")
# R6 : corps traduit différent -> refus sans envoi
c.lire_json = lambda *a: (_ for _ in ()).throw(AssertionError("envoi interdit"))
r = c.appeler_gemini_arriere_plan(dict(m, repli_budget=1000), "x", m["max"]); assert r.echec and not r.interrompue
print("TOUT TIENT")
