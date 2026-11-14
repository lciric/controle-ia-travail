"""Registre propre de l'étape B bis, fiche de `CODE-BBIS`, gardes d'offre, de création et de dépense
(`prereg/T0.7-etape-B-bis-v1.md`, « Lignes de registre », « Liste d'arrêt », « Calcul et dépense », « Seuil »), v1.

- **Registre propre** `registres/t07-etape-b-bis-v1.md` (journal `….ouvertures.md`), format `| clé | AAAA-MM-JJTHH:MM:SSZ |
  chemin | sha256 |` (`t07.registre_v1.ecrire_ligne`), lignes ajoutées, jamais réécrites ; seules les huit clés de marque `BBIS`
  y sont écrites ; **jamais** dans `registres/scellements-v1.md` (la garde de T0.7 y refuse toute clé inconnue,
  `t07/registre_v1.py` l. 138-148, ce qui ferait refuser l'étape B) : écriture refusée, et une clé de B bis trouvée dans le
  registre partagé arrête (`exiger_partage_sans_bbis` ; ligne retirée par la mère, déclaré).
- **Fiche de `CODE-BBIS`** (`ecrire_fiche_code`, `lire_fiche_code`) : JSON scellé (compagnon `.sha256`), cité par la ligne
  `CODE-BBIS` ; clés `commit` (40 caractères hexadécimaux), `fichiers` (chemin → sha256 des fichiers du code cité), `entropie`
  (entier de 128 bits écrit en décimal), `epreuve_niveau` {`chemin`, `sha256`, `taux` (cellule → taux), `niveau_decisif_retenu`,
  `cout`}, `niveau_decisif` (0,99 ou 0,995, celui de l'épreuve, appliqué mécaniquement). **Garde** : l'épreuve de niveau absente,
  réduite (non complète), d'entropie autre que celle de la fiche, ou dont le niveau retenu n'est pas celui de sa règle → la fiche
  n'est pas écrite et `CODE-BBIS` n'est pas inscrite (liste d'arrêt). **Garde d'ancêtre** (`exiger_ancetre`, correction B1) :
  le commit de la fiche doit être un ancêtre de la tête (commit qui porte les lignes du registre propre), jamais son égal exigé.
- **Garde de création** (`exiger_creation`) : aucune création sans `SCELLEMENT-BBIS`, `CODE-BBIS`, `GO-BBIS` (extrait de
  `GO-2026-11-14-09`) au registre propre et le feu écrit de la mère portant ce numéro ; une relance au plus ; échéance de la
  ligne de GO (2026-11-22) ; relance après le samedi 21 novembre 12:00 UTC : nœud.
- **Garde d'offre** (`exiger_offre`) : A100 SXM4 80 Go, au moins 16 cœurs, 128 000 Mo de mémoire vive, 150 Go de disque,
  stockage au plus 0,08 USD de l'heure, étiquette `bbis-t07-v1` ; aucune H200.
- **Garde de dépense** (`garde_depense`) : arrêt et destruction par identifiant (R10) dès que le cumul relevé plus un quart
  d'heure de carte atteint la coupure de 39,5 USD.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret

REGISTRE_PROPRE = "registres/t07-etape-b-bis-v1.md"
REGISTRE_PARTAGE = "registres/scellements-v1.md"
CLES_BBIS = ("SCELLEMENT-BBIS", "ABSENCE-B-BBIS", "CODE-BBIS", "GO-BBIS", "SCORES-BBIS", "LECTURE-BBIS", "VERDICT-BBIS",
             "CONJOINTE-BBIS")
GO_ID = "GO-2026-11-14-09"
COUPURE_USD, QUART_D_HEURE = 39.5, 0.25
ECHEANCE_GO = "2026-11-22T23:59:59Z"
LIMITE_RELANCE = "2026-11-21T12:00:00Z"
ETIQUETTE = "bbis-t07-v1"
OFFRE_MIN = {"coeurs": 16, "memoire_vive_mo": 128000, "disque_go": 150, "stockage_max_usd_h": 0.08}
SHA = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")


def _instant(date: str) -> int:
    return int(datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def cles_bbis_presentes(registre: Path) -> list[str]:
    registre = Path(registre)
    if not registre.is_file():
        return []
    vues = []
    for l in registre.read_text(encoding="utf-8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if c and c[0] in CLES_BBIS:
            vues.append(c[0])
    return vues


def exiger_partage_sans_bbis(registre_partage: Path) -> None:
    """Une clé de B bis dans `registres/scellements-v1.md` : arrêt (ligne retirée par la mère, déclaré)."""
    vues = cles_bbis_presentes(registre_partage)
    if vues:
        raise GardeArret(f"clé(s) de B bis {vues} écrite(s) dans {REGISTRE_PARTAGE} : arrêt de l'écriture ; la garde de T0.7 "
                         "refuserait l'étape B ; ligne à retirer par la mère, déclaré")


def ajouter_ligne_propre(racine: Path, registre_rel: str, cle: str, instant: int, chemin: str, sha: str) -> str:
    """Ajoute une ligne au registre propre (créé à la première ligne, jamais réécrit) ; refus : registre partagé, autre registre,
    clé hors de la marque BBIS, clé déjà présente."""
    from ..t07 import registre_v1 as rg
    rel = Path(registre_rel).as_posix()
    if rel == REGISTRE_PARTAGE or Path(registre_rel).name == Path(REGISTRE_PARTAGE).name:
        raise GardeArret(f"écriture d'une clé de B bis dans {REGISTRE_PARTAGE} : refus (registre propre seulement)")
    if rel != REGISTRE_PROPRE:
        raise GardeArret(f"registre {registre_rel} : seul {REGISTRE_PROPRE} reçoit les clés de B bis")
    if cle not in CLES_BBIS:
        raise GardeArret(f"clé {cle!r} hors des clés de B bis {CLES_BBIS} : refus")
    exiger_partage_sans_bbis(Path(racine) / REGISTRE_PARTAGE)
    registre = Path(racine) / registre_rel
    ligne = rg.ecrire_ligne(cle, rg.date_utc(instant), chemin, sha)
    if registre.is_file():
        if cle in cles_bbis_presentes(registre):
            raise GardeArret(f"registre propre : ligne {cle} déjà présente, jamais réécrite")
    else:
        registre.parent.mkdir(parents=True, exist_ok=True)
        registre.write_text("# Registre propre de T0.7, étape B bis — lignes ajoutées, jamais réécrites\n\n", encoding="utf-8")
    with open(registre, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")
    return ligne


def journaliser_ouverture(racine: Path, quoi: str, instant: int, empreinte: str) -> Path:
    from ..t07 import registre_v1 as rg
    journal = Path(racine) / (REGISTRE_PROPRE + ".ouvertures.md")
    journal.parent.mkdir(parents=True, exist_ok=True)
    with open(journal, "a", encoding="utf-8") as f:
        f.write(f"| OUVERTURE-BBIS | {rg.date_utc(instant)} | {quoi} | {empreinte} |\n")
    return journal


# ----------------------------------------------------------------------------------------------------- fiche de CODE-BBIS

def ecrire_fiche_code(racine: Path, chemin_fiche: str, commit: str, fichiers: dict, entropie: int, chemin_epreuve: str) -> dict:
    """Écrit et scelle la fiche de `CODE-BBIS` (docstring du module) ; refus si l'épreuve de niveau est absente, réduite, d'une
    autre entropie, ou si son niveau retenu n'est pas celui de sa règle. Rend la fiche (la ligne est inscrite par la mère)."""
    from ..scellement import sceller
    from ..t07 import registre_v1 as rg
    from .commun_v1 import NIVEAU_DECISIF, NIVEAU_DECISIF_REPLI, exiger_entropie
    racine = Path(racine)
    if not isinstance(commit, str) or not COMMIT.fullmatch(commit):
        raise GardeArret(f"commit {commit!r} : 40 caractères hexadécimaux attendus")
    if not fichiers or any(not isinstance(v, str) or not SHA.fullmatch(v) for v in fichiers.values()):
        raise GardeArret("fichiers du code : chemin → sha256 attendus, au moins un")
    exiger_entropie(int(entropie), reelle=True)
    ep = racine / chemin_epreuve
    if not ep.is_file():
        raise GardeArret(f"épreuve de niveau {chemin_epreuve} absente : CODE-BBIS n'est pas inscrite, aucune marche (liste d'arrêt)")
    sha_ep = rg.sceau_conforme(ep)
    doc = json.loads(ep.read_text(encoding="utf-8"))
    if not doc.get("complete"):
        raise GardeArret("épreuve de niveau réduite (non complète) : CODE-BBIS n'est pas inscrite (liste d'arrêt)")
    if str(doc.get("graine", {}).get("entropie")) != str(int(entropie)):
        raise GardeArret("épreuve de niveau jouée sous une autre entropie que celle de CODE-BBIS : refus")
    taux = {n: float(c["taux"]) for n, c in doc["cellules"].items()}
    attendu = NIVEAU_DECISIF_REPLI if any(t > float(doc["seuil_taux"]) for t in taux.values()) else NIVEAU_DECISIF
    if float(doc["seuil_taux"]) != 0.01 or float(doc["niveau_decisif_retenu"]) != attendu:
        raise GardeArret(f"épreuve de niveau : niveau retenu {doc['niveau_decisif_retenu']} ≠ règle du texte ({attendu}) : refus")
    fiche = {"texte": "prereg/T0.7-etape-B-bis-v1.md", "commit": commit, "fichiers": dict(sorted(fichiers.items())),
             "entropie": str(int(entropie)),
             "epreuve_niveau": {"chemin": chemin_epreuve, "sha256": sha_ep, "taux": taux,
                                "niveau_decisif_retenu": attendu, "cout": doc.get("cout")},
             "niveau_decisif": attendu}
    chemin = racine / chemin_fiche
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà (R12)")
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(json.dumps(fiche, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    fiche["sha256"] = sceller(chemin)
    return fiche


def lire_fiche_code(chemin: Path) -> dict:
    """Fiche de `CODE-BBIS` lue et contrôlée (forme ; niveau décisif égal à celui de l'épreuve citée)."""
    from .commun_v1 import NIVEAUX_DECISIFS
    try:
        f = json.loads(Path(chemin).read_text(encoding="utf-8"))
        entropie = int(f["entropie"])
        niveau = float(f["niveau_decisif"])
        ep = f["epreuve_niveau"]
        if float(ep["niveau_decisif_retenu"]) != niveau or not SHA.fullmatch(str(ep["sha256"])):
            raise ValueError("niveau de l'épreuve ≠ niveau de la fiche")
        if not COMMIT.fullmatch(str(f["commit"])):
            raise ValueError("commit")
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise GardeArret(f"fiche de CODE-BBIS {chemin} illisible ({type(e).__name__}: {e}) : refus") from None
    if niveau not in NIVEAUX_DECISIFS:
        raise GardeArret(f"niveau décisif {niveau} : 0,99 ou 0,995 (règle de l'épreuve de niveau) attendu")
    return {**f, "entropie": entropie, "niveau_decisif": niveau}


def exiger_ancetre(racine: Path, ancetre: str, tete: str = "HEAD") -> str:
    """Correction B1 (contre-lecture du code, modèle C) : le commit de la fiche de `CODE-BBIS` doit être un **ancêtre** de la tête
    (ou la tête elle-même) — la ligne `CODE-BBIS` cite la fiche, qui cite le commit du code : un commit ne peut porter un fichier
    qui contient son propre identifiant, la tête de l'instance est donc postérieure au commit du code. Objet absent du dépôt, tête
    illisible ou commit non ancêtre : arrêt (R11). Rend l'identifiant complet de la tête. Le contenu du code fait foi par les
    empreintes de la fiche, contrôlées fichier par fichier à part (`marche_v1.gardes_d_entree`)."""
    import subprocess
    if not isinstance(ancetre, str) or not COMMIT.fullmatch(ancetre):
        raise GardeArret(f"commit {ancetre!r} de CODE-BBIS : 40 caractères hexadécimaux attendus : arrêt (R11)")

    def git(*a):
        return subprocess.run(["git", "-C", str(racine), *a], capture_output=True, text=True)

    if git("cat-file", "-e", f"{ancetre}^{{commit}}").returncode != 0:
        raise GardeArret(f"commit {ancetre[:12]} de CODE-BBIS absent du dépôt {racine} : arrêt (R11)")
    r = git("rev-parse", "--verify", "-q", f"{tete}^{{commit}}")
    t = r.stdout.strip()
    if r.returncode != 0 or not COMMIT.fullmatch(t):
        raise GardeArret(f"tête {tete!r} illisible dans {racine} : arrêt (R11)")
    r = git("merge-base", "--is-ancestor", ancetre, t)
    if r.returncode == 1:
        raise GardeArret(f"commit {ancetre[:12]} de CODE-BBIS n'est pas un ancêtre de la tête {t[:12]} : arrêt (R11)")
    if r.returncode != 0:
        raise GardeArret(f"git merge-base --is-ancestor a échoué ({r.stderr.strip()[:200]}) : arrêt (R11)")
    return t


def exiger_ancetre_de_la_fiche(racine: Path, tete: str = "HEAD") -> dict:
    """Ligne `CODE-BBIS` du registre propre (sceau vérifié), fiche lue, commit de la fiche ancêtre de `tete` (`exiger_ancetre`)."""
    from ..t07 import registre_v1 as rg
    from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes
    racine = Path(racine)
    try:
        ligne = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, ("CODE-BBIS",), propre=True)["CODE-BBIS"]
    except RefusLecture as e:
        raise GardeArret(f"registre propre : {e}") from None
    rg.sceau_conforme(racine / ligne["chemin"], ligne["sha256"])
    fiche = lire_fiche_code(racine / ligne["chemin"])
    return {"fiche": fiche, "tete": exiger_ancetre(racine, fiche["commit"], tete)}


# ------------------------------------------------------------------------------------------------ offre, création, dépense

def garde_depense(cumul_releve_usd: float, prix_carte_usd_h: float, coupure: float = COUPURE_USD) -> dict:
    """Arrêt (destruction par identifiant, R10) dès que cumul relevé + un quart d'heure de carte ≥ coupure."""
    projete = float(cumul_releve_usd) + QUART_D_HEURE * float(prix_carte_usd_h)
    if projete >= float(coupure):
        raise GardeArret(f"dépense : cumul relevé {cumul_releve_usd:.2f} USD + un quart d'heure de carte = {projete:.2f} USD ≥ "
                         f"coupure {coupure:g} USD : arrêt et destruction par identifiant (R10)")
    return {"cumul": float(cumul_releve_usd), "projete": projete, "coupure": float(coupure)}


def exiger_offre(offre: dict, identifiant: str | None = None) -> dict:
    """Offre dans les bornes du devis ; H200 exclue (mot de Lazar seulement). `identifiant` (sous-commande `commande` de
    `scripts/lancer_bbis_v1.sh`, correction m5) : l'offre décrite doit porter cet identifiant numérique (clé `id`)."""
    fautes = []
    if identifiant is not None:
        if not str(identifiant).isdigit():
            fautes.append(f"identifiant d'offre {identifiant!r} illisible")
        elif str(offre.get("id")) != str(identifiant):
            fautes.append(f"identifiant {offre.get('id')!r} de l'offre décrite ≠ offre demandée {identifiant}")
    nom = str(offre.get("carte", "")).upper()
    if "H200" in nom:
        fautes.append("H200 exclue (mot de Lazar seulement)")
    if "A100" not in nom or "80" not in nom or "SXM" not in nom:
        fautes.append(f"carte {offre.get('carte')!r} : A100 SXM4 80 Go attendue")
    for cle in ("coeurs", "memoire_vive_mo", "disque_go"):
        try:
            v = float(offre.get(cle))
        except (TypeError, ValueError):
            v = -1.0
        if v < OFFRE_MIN[cle]:
            fautes.append(f"{cle} {offre.get(cle)!r} < {OFFRE_MIN[cle]}")
    try:
        st = float(offre.get("stockage_usd_h"))
    except (TypeError, ValueError):
        st = float("inf")
    if not st <= OFFRE_MIN["stockage_max_usd_h"]:
        fautes.append(f"stockage {offre.get('stockage_usd_h')!r} USD/h > 0,08")
    if offre.get("etiquette") != ETIQUETTE:
        fautes.append(f"étiquette {offre.get('etiquette')!r} ≠ {ETIQUETTE}")
    if fautes:
        raise GardeArret("offre hors des bornes du devis : " + " ; ".join(fautes))
    return offre


def exiger_creation(racine: Path, feu_ecrit: str, maintenant: int, relances: int = 0) -> dict:
    """Aucune création sans `SCELLEMENT-BBIS`, `CODE-BBIS`, `GO-BBIS` au registre propre et le feu écrit de la mère portant le
    numéro de la ligne de GO ; une relance au plus ; échéance de la ligne de GO ; relance après le samedi 21 novembre 12:00 UTC :
    nœud."""
    exiger_partage_sans_bbis(Path(racine) / REGISTRE_PARTAGE)
    presentes = set(cles_bbis_presentes(Path(racine) / REGISTRE_PROPRE))
    manque = [k for k in ("SCELLEMENT-BBIS", "CODE-BBIS", "GO-BBIS") if k not in presentes]
    if manque:
        raise GardeArret(f"création refusée : ligne(s) {manque} absente(s) du registre propre")
    if not isinstance(feu_ecrit, str) or GO_ID not in feu_ecrit:
        raise GardeArret(f"création refusée : feu écrit de la mère portant le numéro {GO_ID} absent")
    if int(relances) > 1:
        raise GardeArret("une seconde relance est exclue (ligne de GO : une relance au plus)")
    if int(maintenant) > _instant(ECHEANCE_GO):
        raise GardeArret("échéance de la ligne de GO dépassée : aucune création")
    if int(relances) == 1 and int(maintenant) > _instant(LIMITE_RELANCE):
        raise GardeArret("relance après le samedi 21 novembre à 12:00 UTC : nœud (le billet sort sans B bis)")
    return {"go": GO_ID, "relances": int(relances)}


def main(argv=None) -> int:
    """Commandes de session (sans réseau) : `offre FICHIER.json [ID]` ; `creation RACINE FEU MAINTENANT RELANCES` ; `depense CUMUL
    PRIX` ; `fiche RACINE CHEMIN_FICHE COMMIT ENTROPIE CHEMIN_EPREUVE FICHIER…` (fiche de `CODE-BBIS`, empreintes des fichiers du
    code lues sur le disque ; la ligne est inscrite ensuite par la mère) ; `ancetre RACINE COMMIT` (commit de la fiche de
    `CODE-BBIS` ancêtre de COMMIT, correction B1). Code 0 : accepté ; code 2 : refus (motif écrit)."""
    import sys
    from ..scellement import empreinte
    a = list(sys.argv[1:] if argv is None else argv)
    try:
        if a[:1] == ["fiche"] and len(a) >= 7:
            racine = Path(a[1])
            f = ecrire_fiche_code(racine, a[2], a[3], {p: empreinte(racine / p) for p in a[6:]}, int(a[4]), a[5])
            print(f"BBIS FICHE ECRITE {a[2]} {f['sha256']} niveau décisif {f['niveau_decisif']}")
        elif a[:1] == ["offre"] and len(a) in (2, 3):
            exiger_offre(json.loads(Path(a[1]).read_text(encoding="utf-8")), a[2] if len(a) == 3 else None)
            print("BBIS OFFRE ACCEPTEE")
        elif a[:1] == ["ancetre"] and len(a) == 3:
            r = exiger_ancetre_de_la_fiche(Path(a[1]), a[2])
            print(f"BBIS ANCETRE {r['fiche']['commit']} de {r['tete']}")
        elif a[:1] == ["creation"] and len(a) == 5:
            print(f"BBIS CREATION PERMISE {exiger_creation(Path(a[1]), a[2], int(a[3]), int(a[4]))}")
        elif a[:1] == ["depense"] and len(a) == 3:
            print(f"BBIS DEPENSE {garde_depense(float(a[1]), float(a[2]))}")
        else:
            print("BBIS REFUS : commande inconnue (offre FICHIER [ID] | creation RACINE FEU MAINTENANT RELANCES | depense CUMUL PRIX | "
                  "fiche RACINE CHEMIN_FICHE COMMIT ENTROPIE CHEMIN_EPREUVE FICHIER… | ancetre RACINE COMMIT)")
            return 2
    except (GardeArret, ValueError, OSError) as e:
        print(f"BBIS REFUS : {e}")
        return 2
    return 0


__all__ = ["REGISTRE_PROPRE", "REGISTRE_PARTAGE", "CLES_BBIS", "GO_ID", "COUPURE_USD", "ETIQUETTE", "cles_bbis_presentes",
           "exiger_partage_sans_bbis", "ajouter_ligne_propre", "journaliser_ouverture", "ecrire_fiche_code", "lire_fiche_code",
           "exiger_ancetre", "exiger_ancetre_de_la_fiche", "garde_depense", "exiger_offre", "exiger_creation", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
