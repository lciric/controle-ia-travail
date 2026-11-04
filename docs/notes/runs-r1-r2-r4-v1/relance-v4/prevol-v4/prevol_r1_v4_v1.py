"""Pré-vol de la relance v4 de R1 sur les **vraies pièces de P3**, sans modèle, sans carte, **sans tokeniseur** (absent du
poste, aucun réseau) et **sans lire aucun score** : ce qui est vérifiable ainsi (point I4 (1) de la contre-lecture R2).

Lu : configuration de la réparation (v2), manifeste de P3, fiches de P3 (empreintes, `equivalence`), textes de P3 (ordre
des épisodes seulement ; empreinte du fichier), table v3, liste des 89 épisodes cassés de la sortie du diagnostic
(`diagnostic-r1-v4-sortie.txt`, empreinte vérifiée, § 4 et § 8). Non lu : `scores-p3.npz` et toute pièce d'activations.
Non vérifiable ici (tokeniseur requis) : le classement de base (151 conformes en longueur, 129 identiques de base) et donc
le recalcul indépendant des 89 cibles ; il est pris de la sortie du diagnostic et recoupé (lots, rangs, table v3).

    PYTHONPATH=src python -B prevol_r1_v4_v1.py RACINE CONFIG SORTIE_DIAGNOSTIC SHA_SORTIE_DIAGNOSTIC
"""
import hashlib
import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace

from controle_ia.manifeste import lire_manifeste
from controle_ia.runs_nuit import resolution_graine_lot_v3 as rv
from controle_ia.scellement import verifier

racine, chemin_conf, chemin_diag, sha_diag = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]), sys.argv[4]
sortie = []
echecs = []


def dire(cle, valeur, attendu=None):
    ok = attendu is None or valeur == attendu
    sortie.append(f"{'OK ' if ok else 'ÉCART'} {cle} : {valeur}" + ("" if attendu is None else f" (attendu {attendu})"))
    if not ok:
        echecs.append(cle)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


verifier(racine / chemin_conf) if Path(f"{racine / chemin_conf}.sha256").exists() else None
conf = json.loads((racine / chemin_conf).read_text(encoding="utf-8"))
rv.exiger_config(conf)
dire("configuration", f"{chemin_conf} (canonique {rv.empreinte_config(conf)})")
dire("voie si témoin non exact", conf["voie_si_temoin_non_exact"], "lot_fidele")
dire("sortie du diagnostic, empreinte", sha(chemin_diag), sha_diag)
m, sha_m = lire_manifeste(racine / conf["chemin_manifeste_p3"])
dire("manifeste de P3, empreinte", sha_m, conf["manifeste_p3_sha256"])
c3 = m["config"]
dire("taille de lot de P3", int(c3["lot"]), 8)
dire("noyau d'attention de P3 = configuration", c3.get("noyau_attention", "defaut"), conf["noyau_attention"])
T = int(conf["T"])
dire("T", T, int(c3["T"]))
fiches_p = racine / conf["chemin_fiches"]
dire("fiches de P3, empreinte", verifier(fiches_p), conf["fiches_sha256"])
fiches = json.loads(fiches_p.read_text(encoding="utf-8"))["resultat"]["fiches"]
ids_fiches = [f["episode"] for f in fiches]
dire("épisodes dans les fiches", len(ids_fiches), 240)
dire("épisodes distincts dans les fiches", len(set(ids_fiches)), 240)
textes_p = racine / conf["chemin_textes"]
dire("textes de P3, empreinte", sha(textes_p), conf["textes_sha256"])
ordre = []
for ligne in textes_p.read_text(encoding="utf-8").splitlines():
    e = json.loads(ligne)["episode"]              # seul champ lu : l'épisode (ordre d'écriture, lot par lot)
    if not ordre or ordre[-1] != e:
        if e in ordre:
            echecs.append(f"textes : {e} en plusieurs morceaux")
        ordre.append(e)
dire("épisodes dans l'ordre des textes", len(ordre), 240)
dire("ensemble des textes = ensemble des fiches", set(ordre) == set(ids_fiches), True)
lots = [ordre[d:d + 8] for d in range(0, len(ordre), 8)]
dire("lots (ordre des textes, taille 8)", len(lots), 30)
lot_de = {e: (k, lot.index(e)) for k, lot in enumerate(lots) for e in lot}
t3_p = racine / conf["chemin_table_v3"]
dire("table v3, empreinte", verifier(t3_p), conf["table_v3_sha256"])
t3 = json.loads(t3_p.read_text(encoding="utf-8"))
dire("table v3, version", t3.get("version"), 3)
v3 = {x["episode"] for x in t3["episodes"]}
dire("table v3, entrées", len(v3), 22)
dire("table v3, entrées parmi les 240", v3 <= set(ordre), True)
# les 89 du diagnostic (§ 4) et la composition des lots (§ 8)
texte = chemin_diag.read_text(encoding="utf-8")
s4 = texte.split("4. Les 89 épisodes cassés", 1)[1].split("épisodes cassés présents dans la table v3", 1)[0]
casses = {}
for x in s4.splitlines():
    mm = re.match(r"^(\S+/\S+/e\d+) \| (\w+) \| (\S+) \| (\d+) \((\d+)\) \|", x)
    if mm:
        casses[mm.group(1)] = (int(mm.group(4)), int(mm.group(5)), mm.group(2))
dire("cassés listés par le diagnostic (§ 4)", len(casses), 89)
dire("cassés parmi les 240", set(casses) <= set(ordre), True)
dire("cassés dans la table v3", len(set(casses) & v3), 0)
dire("lot et rang du diagnostic = lot et rang recalculés (ordre des textes)",
     all(lot_de[e][:2] == (k, r) for e, (k, r, _) in casses.items()), True)
dire("condition du diagnostic = condition des fiches",
     all(next(f for f in fiches if f["episode"] == e).get("condition", e.split("/")[0]) == c
         for e, (_, _, c) in casses.items()), True)
a_cible = sorted({lot_de[e][0] for e in casses})
dire("lots à cible", len(a_cible), conf["lots_cibles_attendus"])
dire("cibles (cassés hors table v3)", len(set(casses) - v3), conf["cibles_attendues"])
connus = set(ordre) - set(casses)
dire("épisodes connus (240 − 89 : base identique ou table v3, selon le diagnostic)", len(connus), 151)
for k in conf["lots_temoin"]:
    dire(f"lot témoin {k} : épisodes cassés", len([e for e in lots[k] if e in casses]), 0)
    dire(f"lot témoin {k} : entrées de la table v3 (connues par la table)", len([e for e in lots[k] if e in v3]))
for k in conf["lots_d_abord"]:
    dire(f"lot d'abord {k} : cibles", len([e for e in lots[k] if e in casses]), 7)
s8 = texte.split("lots sans aucun épisode cassé (témoin pur du lot fidèle) : ", 1)[1].splitlines()[0]
dire("lots sans cassé selon le diagnostic (§ 8) = lots témoins", json.loads(s8), sorted(conf["lots_temoin"]))
# captures de P3 : échantillon d'équivalence recalculé depuis les graines (fonction du module, R5)
cap = rv.captures_de_p3(fiches_p, conf["fiches_sha256"], SimpleNamespace(manifeste_p3=m), T,
                        float(c3["fraction_equivalence"]))
dire("captures de P3 (échantillon recalculé = fiches) : actions", sum(len(v) for v in cap.values()), 132)
dire("captures de P3 : épisodes", sum(1 for v in cap.values() if v), 116)
for k, n in ((2, 8), (13, 0)):
    dire(f"captures du lot témoin {k}", sum(len(cap.get(e) or {}) for e in lots[k]), n)
dire("captures dans les cassés", sum(len(cap.get(e) or {}) for e in casses), 48)
print("\n".join(sortie))
print(f"bilan : {len(echecs)} écart(s) {echecs if echecs else ''}".rstrip())
sys.exit(1 if echecs else 0)
