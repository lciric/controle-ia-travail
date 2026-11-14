#!/usr/bin/env python3
"""Épreuves du contre-lecteur sur `verifier_go` et `garde_cumul` du lanceur « Regard ou raisons » v1 — version 1.

Fonctions pures du lanceur, jouées sur des registres écrits dans un dossier temporaire (premier argument, neuf, hors du
dépôt). Le registre réel est lu une fois, sans être modifié. Aucun lancement, aucun appel, aucune variable d'environnement lue.

Usage : /usr/local/bin/python3 -I -B epreuves_ligne_de_go_v1.py DOSSIER_NEUF
"""
import datetime
import json
import sys
from pathlib import Path

DEPOT = Path("/home/user/controle-ia-travail")
sys.path.insert(0, str(DEPOT / "scripts"))
import lancer_course_ideation_regard_ou_raisons_v1 as L  # noqa: E402

travail = Path(sys.argv[1]).resolve()
assert not travail.exists() and DEPOT not in travail.parents
travail.mkdir(parents=True)
JOUR = datetime.date(2026, 11, 14)
reel = [x for x in (DEPOT / "registres" / "go.md").read_text(encoding="utf-8").splitlines()
        if x.startswith("| GO-2026-11-14-01 |")]
assert len(reel) == 1
VRAIE = reel[0]
P = "Course de l'organisme d'idéation sur la question « Regard ou raisons »"


def ligne(ident="GO-2026-11-14-01", date="2026-11-14", typ="calcul", perimetre=P, plafond="25 USD", ech="2026-11-30",
          par="Lazar", ref="R-2682"):
    return f"| {ident} | {date} | {typ} | {perimetre} | {plafond} | {ech} | {par} | {ref} |"


def jouer(nom, lignes, jour=JOUR):
    f = travail / (nom + ".md")
    f.write_text("# GO\n\n| id | date | type | périmètre | plafond | échéance | par | réf |\n|---|---|---|---|---|---|---|---|\n"
                 + "\n".join(lignes) + "\n", encoding="utf-8")
    try:
        g = L.verifier_go(f, jour)
        return {"cas": nom, "issue": "ADMIS", "id": g["id"], "plafond_usd": g["plafond_usd"]}
    except L.Refus as e:
        return {"cas": nom, "issue": "refus", "motif": str(e)[:150]}


cas = [
    jouer("01-ligne-reelle-seule", [VRAIE]),
    jouer("02-ligne-reelle-et-ligne-du-collisionneur-sans-organisme",
          [VRAIE, ligne("GO-2026-11-14-02", perimetre="Collisionneur à cinq espèces sur « Regard ou raisons »")]),
    jouer("03-seconde-ligne-aux-deux-expressions",
          [VRAIE, ligne("GO-2026-11-14-02", perimetre="Croisement des bilans, dont celui de l'organisme d'idéation, « Regard ou raisons »")]),
    jouer("04-revocation-en-forme", [VRAIE, ligne("GO-2026-11-15-01", "2026-11-15", "révocation", "Retrait de GO-2026-11-14-01", "0 USD")]),
    jouer("05-revocation-qui-reprend-le-perimetre",
          [VRAIE, ligne("GO-2026-11-15-01", "2026-11-15", "révocation", "Retrait de GO-2026-11-14-01 : " + P, "0 USD")]),
    jouer("06-revocation-ecrite-dans-le-perimetre-type-calcul",
          [VRAIE, ligne("GO-2026-11-15-01", "2026-11-15", "calcul", "Révocation de GO-2026-11-14-01", "0 USD")]),
    jouer("07-revocation-sous-le-meme-identifiant", [VRAIE, ligne(typ="révocation", perimetre="Retrait", plafond="0 USD")]),
    jouer("08-extension-qui-releve-le-plafond", [VRAIE, ligne(perimetre="Extension : " + P, plafond="60 USD")]),
    jouer("09-ligne-citante-a-neuf-colonnes", [VRAIE, ligne("GO-2026-11-15-01", perimetre="Suite de GO-2026-11-14-01 | note")]),
    jouer("10-espace-insecable-dans-l-expression", [ligne(perimetre=P.replace("Regard ou raisons", "Regard ou raisons"))]),
    jouer("11-apostrophe-typographique-et-gras", [ligne(perimetre=P.replace("'", "’").replace("Regard", "**Regard").replace("raisons", "raisons**"))]),
    jouer("12-plafond-16-USD", [ligne(plafond="16 USD")]),
    jouer("13-plafond-17-USD", [ligne(plafond="17 USD")]),
    jouer("14-plafond-en-euros", [ligne(plafond="25 EUR")]),
    jouer("15-plafond-avec-suffixe", [ligne(plafond="25 USD par course")]),
    jouer("16-lendemain-de-l-echeance", [VRAIE], datetime.date(2026, 12, 1)),
    jouer("17-veille-de-l-accord", [VRAIE], datetime.date(2026, 11, 13)),
    jouer("18-type-contact", [ligne(typ="contact")]),
    jouer("19-accordee-par-un-autre", [ligne(par="la mère")]),
    jouer("20-registre-sans-la-ligne", [ligne("GO-2026-11-13-06", perimetre="Course de l'organisme d'idéation sur sa propre conception")]),
]
# garde de cumul : frontière de la relance, et ligne à 25 USD sans effet sur la borne
cumul = []
for cout in (0.0, 2.0, 2.1, 2.1000001, 2.2, 14.9):
    run = {"nom": "x", "lance": True, "fin": {"code": 1, "releve_sha256": None}, "dossier": travail}
    d = travail / f"cumul-{cout}"
    d.mkdir()
    L.ecrire_scelle(d / "releve-depense.json", {"course_usd": cout, "lisible": True, "fiches_produites": False, "lecture": "épreuve"})
    run["dossier"] = d
    run["fin"]["releve_sha256"] = L.sha256_fichier(d / "releve-depense.json")
    try:
        g = L.garde_cumul([run], 25.0)
        cumul.append({"premiere_tentative_usd": cout, "issue": "ADMIS", "borne_usd": g["borne_usd"],
                      "engagement_maximal_usd": round(cout + L.PLAFOND_COURSE_USD, 6)})
    except L.Refus:
        cumul.append({"premiere_tentative_usd": cout, "issue": "refus"})
print(json.dumps({"lanceur_sha256": L.sha256_fichier(DEPOT / "scripts" / L.FICHIER_LANCEUR), "ligne_de_go": cas,
                  "garde_de_cumul_ligne_a_25_USD": cumul}, ensure_ascii=False, indent=1))
