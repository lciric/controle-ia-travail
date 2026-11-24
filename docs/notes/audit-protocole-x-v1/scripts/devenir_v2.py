"""Devenir des propositions retenues : codage par l'auditeur, sur traces écrites, avec sources.

États (ceux du mandat, en tête) :
  jamais éprouvée          — aucune épreuve trouvée ; sous-états : « aucune trace », « adoptée sans épreuve »
                             (inscrite dans une conception, une règle ou un texte, sans mesure qui la tranche),
                             « en préparation » (épreuve inscrite à une file, non partie) ;
  éprouvée et survivante   — épreuve faite, critère de mort non atteint ;
  éprouvée et tombée       — épreuve faite, critère de mort atteint ;
  non évaluable            — épreuve tentée, issue non évaluable (panne, refus, instrument) ;
  trouvée occupée          — la littérature la contenait déjà (compte comme un échec du protocole).
Sources cherchées : registres/decisions.md, registres/go.md, journal des idées de la veille de cap,
registres/rappels.md, errata et notes postérieures (recherche par nom de dossier puis lecture des lignes).
Codage non aveugle, par un seul codeur : réserve déclarée dans le rapport.

Version 2 (inventaire v2, branches de données comprises). Sorties : sorties/jeu-des-propositions-v2.json et .csv.
"""
import csv
import json
import re
import subprocess
import sys
from collections import Counter

from audit_commun_v3 import SORTIES, inventaire

COMMIT_MAIN = subprocess.run(["git", "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()[:12]

# Codage par dossier (clé : fin du chemin de la note) ; valeur : (état, sous-état, sources, commentaire)
PAR_DOSSIER = {
    "collisionneur-conception-qo1-q1-v1/synthese-v1.md": (
        "jamais éprouvée", "adoptée sans épreuve", ["registres/decisions.md R-2020"],
        "recommandations de la synthèse valant décision de conception (règles du préenregistrement P3-bis), sans mesure qui les tranche"),
    "collisionneur-diversite-idees-v1/synthese-v1.md": (
        "jamais éprouvée", "adoptée sans épreuve", ["registres/decisions.md R-2443, R-2467", "journal des idées I-0006 (en préparation)"],
        "monde riche et regroupement des doublons adoptés par mot du directeur ; cribles encore en préparation"),
    "collisionneur-experimentateur-v1/synthese-v1.md": (
        "jamais éprouvée", "aucune trace", [], "aucune épreuve du duel recommandé trouvée dans les registres"),
    "collisionneur-bassins-etroits-v1/synthese-v1.md": (
        "jamais éprouvée", "aucune trace", ["journal des idées I-0004 (essai non évaluable de l'atelier lié)"],
        "le dossier a nourri un atelier de l'organisme jugé non évaluable ; aucune épreuve isolée des propositions retenues"),
    "regard-ou-raisons-confondants-v1/bilan-mere-v1.md": (
        "non évaluable", None, ["journal des idées I-0025", "registres/decisions.md R-4647"],
        "pilotes de « Raisons ou regard ? » arrêtés par refus des modèles (catégorie cyber) : essai non évaluable"),
    "audit-controle-v1/synthese-collisionneur-v1.md": (
        "jamais éprouvée", "adoptée sans épreuve", ["CLAUDE.md, décision N-053 (cinq propositions de l'audit défensif acceptées)", "registres/decisions.md R-521"],
        "failles et angles morts retenus versés dans les décisions du programme ; aucune mesure qui les tranche trouvée"),
    "collisionneur-pari-de-signe-v1/synthese-pari-de-signe-v1.md": (
        "jamais éprouvée", "adoptée sans épreuve", ["CLAUDE.md, décision N-055 (pari apparié borné, décisions D-S1 à D-S12)"],
        "recommandation versée dans la décision N-055 ; G1 non encore lue"),
    "note-sortie-conscience-anesthesie-neutre-v1.md": (
        "jamais éprouvée", "en préparation", ["journal des idées P-0046"],
        "préenregistrements et devis des trois expériences de la ligne anesthésie en préparation"),
}
# Exceptions par élément (clé : (fin du chemin de la note, début du texte)) ; valeur comme ci-dessus
PAR_ELEMENT = {
    ("note-sortie-boucle-organisme-controle-v1.md", "2. **Auditer d'abord le nul réel"): (
        "jamais éprouvée", "en préparation", ["registres/rappels.md (file des textes de Fable, 2 décembre)", "R-5297"],
        "devis de l'audit du nul réel des bases dans la file gelée des textes de Fable"),
    ("note-sortie-boucle-organisme-controle-v1.md", "3. **Partitionner les traces honnêtes"): (
        "jamais éprouvée", "en préparation", ["registres/rappels.md", "R-5297"], "réservoirs disjoints de traces honnêtes, file gelée"),
    ("note-sortie-boucle-organisme-controle-v1.md", "4. **Tester l'apport propre de l'organisme"): (
        "jamais éprouvée", "en préparation", ["registres/rappels.md", "R-5297"], "apport propre de l'organisme, file gelée"),
    ("note-de-sortie-collisionneur-dossier-1-v2.md", "5 | Tenue de l'adaptateur"): (
        "jamais éprouvée", "en préparation", ["registres/rappels.md (2 décembre)", "GO-2026-11-24-31", "R-5309"],
        "conception par Fable du 2 au 5 décembre, course du 8 au 18 décembre"),
    ("note-sortie-cible-publication-papier-d-v1.md", "1. **Relire le manuscrit"): (
        "jamais éprouvée", "en préparation", ["registres/rappels.md (correctif 6 du manuscrit)", "GO-2026-11-24-38"],
        "correction du manuscrit inscrite"),
    ("note-sortie-cible-publication-papier-d-v1.md", "4. **Cible en deux temps"): (
        "jamais éprouvée", "adoptée sans épreuve", ["registres/rappels.md (7 décembre)"], "cible « atelier d'abord » à décider le 7 décembre"),
}
DEFAUT = ("jamais éprouvée", "aucune trace", [], "aucune épreuve trouvée dans les registres pour cette proposition")


def main():
    inv = {d["racine"]: d for d in inventaire()}
    ret = json.loads((SORTIES / "retenues-v2.json").read_text())
    lignes = []
    for k, r in enumerate(ret):
        etat, sous, src, com = DEFAUT
        for cle, v in PAR_DOSSIER.items():
            if r["note"].endswith(cle):
                etat, sous, src, com = v
        for (n, debut), v in PAR_ELEMENT.items():
            if r["note"].endswith(n) and r["texte"].startswith(debut):
                etat, sous, src, com = v
        if r["genre"] != "retenue":
            etat, sous, src, com = ("hors mesure", "non retenue ou à reprendre", [], "seul le devenir des retenues est codé")
        racine = r["racines"][0] if r["racines"] else None
        lignes.append({
            "id": f"P-{k + 1:03d}", "dossier": racine, "note": r["note"], "branche_note": r["branche"],
            "commit_note": inv.get(racine, {}).get("commit") if r["branche"] != "main" else COMMIT_MAIN,
            "genre": r["genre"], "section": r["section"], "texte": r["texte"],
            "lettres_porteuses": r["lettres_porteuses"], "especes_porteuses": r["especes_porteuses"],
            "attribution": r["attribution"], "unites_proches": r["unites_proches"],
            "etat": etat, "sous_etat": sous, "sources_devenir": src, "commentaire_devenir": com,
            "cout_dossier_usd": inv.get(racine, {}).get("compte_usd"),
            "nature": "règle de texte" if ("conception-qo1" in r["note"] or "repli-g0" in r["note"] or "collisionneur-pilote-v1" in r["note"] or "n12-n13" in r["note"]) else "proposition",
        })
    (SORTIES / "jeu-des-propositions-v2.json").write_text(json.dumps(lignes, ensure_ascii=False, indent=1))
    champs = ["id", "dossier", "note", "branche_note", "commit_note", "genre", "nature", "texte", "lettres_porteuses",
              "especes_porteuses", "attribution", "etat", "sous_etat", "sources_devenir", "commentaire_devenir", "cout_dossier_usd"]
    with open(SORTIES / "jeu-des-propositions-v2.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=champs, extrasaction="ignore")
        w.writeheader()
        for l in lignes:
            w.writerow({c: ("; ".join(l[c]) if isinstance(l[c], list) else l[c]) for c in champs})
    r_ = [l for l in lignes if l["genre"] == "retenue"]
    print(len(lignes), Counter(l["genre"] for l in lignes))
    print(Counter((l["etat"], l["sous_etat"]) for l in r_))
    return 0


if __name__ == "__main__":
    sys.exit(main())
