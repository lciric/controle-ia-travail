import json, tempfile, pathlib
from datetime import date, datetime, timezone, timedelta
from controle_ia.organismes_discrets import lanceur_bras_a_v4 as L
from controle_ia.gardes import GardeArret
def essai(nom, f):
    try: r = f(); print(nom, "-> PASSE", str(r)[:70])
    except GardeArret as e: print(nom, "-> refus:", str(e)[:90])
    except Exception as e: print(nom, "-> EXCEPTION", type(e).__name__, str(e)[:80])
# m-3 identifiants
for g in ["GO-2026-11-22-148","GO-2026-11-22-1480","GO-2026-02-30-01","GO-2026-11-22-1","GO-2026-11-22-148\n","go-2026-11-22-148"," GO-2026-11-22-148"]:
    essai("id "+repr(g), lambda g=g: L.exiger_identifiant_de_go(g))
ENT="| id | a | t | p | pl | e | par | ref |\n"
ok="| GO-2026-11-22-148 | 2026-11-22 | calcul | ligne 1 du bras A | 18 USD | 2026-11-30 | Lazar | m |\n"
# ligne mal formee sautee ?
for nom, extra in [("rev3chiffres","| GO-2026-11-22-149 | 2026-11-22 | révocation | GO-2026-11-22-148 retiré | — | — | Lazar | m |\n"),
  ("rev mal formee","| GO-2026-11-22-14 9 | 2026-11-22 | révocation | GO-2026-11-22-148 | — | — | Lazar | m |\n"),
  ("rev sans espace","|GO-2026-11-22-1499 | 2026-11-22 | révocation | GO-2026-11-22-148 | — | — | Lazar | m |\n"),
  ("rev majuscule","| GO-2026-11-22-149 | 2026-11-22 | Révocation | GO-2026-11-22-148 | — | — | Lazar | m |\n"),
  ("rev dans perimetre autre type","| GO-2026-11-22-149 | 2026-11-22 | décision | révoque GO-2026-11-22-148 | — | — | Lazar | m |\n")]:
    essai(nom, lambda extra=extra: L.exiger_ligne_de_go("GO-2026-11-22-148", ENT+ok+extra, date(2026,11,23)))
essai("accordant Lazar ", lambda: L.exiger_ligne_de_go("GO-2026-11-22-148", ENT+ok.replace("| Lazar |","| Lazar (mot) |"), date(2026,11,23)))
essai("jour echeance", lambda: L.exiger_ligne_de_go("GO-2026-11-22-148", ENT+ok, date(2026,11,30)))
essai("lendemain echeance", lambda: L.exiger_ligne_de_go("GO-2026-11-22-148", ENT+ok, date(2026,12,1)))
essai("avant accord", lambda: L.exiger_ligne_de_go("GO-2026-11-22-148", ENT+ok, date(2026,11,21)))
essai("plafond 18 USD (sur crédits)", lambda: L.exiger_ligne_de_go("GO-2026-11-22-148", ENT+ok.replace("18 USD","18 USD (sur crédits)"), date(2026,11,23)))
# m-2 ecriture
d = pathlib.Path(tempfile.mkdtemp())
for nom, c in [("ok",{"a":1}),("set",{"a":{1}}),("nan",[float("nan")]),("inf",[float("inf")]),("cles mixtes",{1:1,"a":2})]:
    essai("ecrire "+nom, lambda c=c,nom=nom: L.ecrire_sans_ecraser(d/(nom.replace(" ","_")+".json"), c))
print(sorted(p.name for p in d.iterdir()))
essai("ecrire deja", lambda: L.ecrire_sans_ecraser(d/"ok.json", {"a":2}))
# m-1 inventaire
v = pathlib.Path(tempfile.mkdtemp()); (v/"s").mkdir(); (v/"a").write_text("x")
print([e["nom"] for e in L.inventaire(v)])
(v/L.NOM_DU_MANIFESTE_DU_VERSEMENT).write_text("{}"); (v/(L.NOM_DU_MANIFESTE_DU_VERSEMENT+".sha256")).write_text("z")
print([e["nom"] for e in L.inventaire(v)])
for nom in (L.NOM_DU_MANIFESTE_DU_VERSEMENT, L.NOM_DU_MANIFESTE_DU_VERSEMENT+".sha256"):
    (v/"s"/nom).write_text("y"); essai("homonyme "+nom, lambda: L.inventaire(v)); (v/"s"/nom).unlink()
# fichier prefixe proche
(v/"s"/"manifeste-du-versement.json.bak").write_text("y"); print([e["nom"] for e in L.inventaire(v)])
# m-4
maint = datetime(2026,11,23,1,0,tzinfo=timezone.utc)
class C: pass
import controle_ia.organismes_discrets as od
cfg = {"reference":{"carte":{"course":{"prix_max_usd_h":1.30}},"offre":{"stockage_max_usd_h":0.08,"telechargement_max_usd_go":0.05}}}
T = lambda d: {"carte_usd_h":1.18,"stockage_usd_h":0.05,"telechargement_usd_go":0.05,"date_utc":d}
for nom, d, m in [("meme jour avant","2026-11-23T00:59:59Z",maint),("meme instant","2026-11-23T01:00:00Z",maint),("apres","2026-11-23T01:00:01Z",maint),
   ("veille 23:59","2026-11-22T23:59:59Z",maint),("minuit exact","2026-11-23T00:00:00Z",maint),("fuseau +02 meme jour UTC", "2026-11-23T01:00:00Z", datetime(2026,11,23,3,0,tzinfo=timezone(timedelta(hours=2)))),
   ("naif","2026-11-23T00:00:00Z",datetime(2026,11,23,1,0)),("30 fev","2026-02-30T00:00:00Z",maint),("sans Z","2026-11-23T00:00:00",maint)]:
    essai("tarif "+nom, lambda d=d,m=m: L.exiger_tarif(cfg, T(d), m))
# compteur : horloge figee / fixes
essai("compteur horloge figee", lambda: L.CompteurDePlafond(18, 1.38, 0.0, horloge=lambda: 0.0).exiger_sous_plafond())
essai("compteur fixes 0 / taux ok", lambda: L.CompteurDePlafond(18, 1.23, 0.0, 0.0))
