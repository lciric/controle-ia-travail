"""Registre propre de l'étape B bis, gardes d'écriture, de création et de dépense (`prereg/T0.7-etape-B-bis-v1.md`,
« Lignes de registre », « Liste d'arrêt », « Calcul et dépense »), v1.

- **Registre propre** `registres/t07-etape-b-bis-v1.md` (journal `….ouvertures.md`), format `| clé | AAAA-MM-JJTHH:MM:SSZ |
  chemin | sha256 |` (celui de `t07.registre_v1.ecrire_ligne`), lignes ajoutées, jamais réécrites ; seules les clés de marque
  `BBIS` y sont écrites ; **jamais** dans `registres/scellements-v1.md` (la garde de T0.7 y refuse toute clé inconnue,
  `t07/registre_v1.py` l. 138-148, ce qui ferait refuser l'étape B) : écriture refusée, et une clé de B bis trouvée dans le
  registre partagé arrête (`exiger_partage_sans_bbis`).
- **Garde de création** (`exiger_creation`) : aucune création sans `GO-BBIS` (extrait de `GO-2026-11-14-09`), le feu écrit de
  la mère portant ce numéro, `CODE-BBIS` et `SCELLEMENT-BBIS` ; offre dans les bornes du devis (A100 SXM4 80 Go, au moins 16
  cœurs, 128 000 Mo de mémoire vive, 150 Go de disque, stockage au plus 0,08 USD de l'heure, étiquette `bbis-t07-v1` ; aucune
  H200) ; une relance au plus ; relance après le samedi 21 novembre 12:00 UTC : nœud.
- **Garde de dépense** (`garde_depense`) : arrêt et destruction par identifiant (R10) dès que le cumul relevé plus un quart
  d'heure de carte atteint la coupure de 39,5 USD.
"""
from __future__ import annotations

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
OFFRE_MIN = {"carte": "A100 SXM4 80GB", "coeurs": 16, "memoire_vive_mo": 128000, "disque_go": 150, "stockage_max_usd_h": 0.08}


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
    """Ajoute une ligne au registre propre (créé à la première ligne, jamais réécrit) ; refus : registre partagé, clé hors de
    la marque BBIS, clé déjà présente."""
    from ..t07 import registre_v1 as rg
    if Path(registre_rel).as_posix() == REGISTRE_PARTAGE or Path(registre_rel).name == Path(REGISTRE_PARTAGE).name:
        raise GardeArret(f"écriture d'une clé de B bis dans {REGISTRE_PARTAGE} : refus (registre propre seulement)")
    if Path(registre_rel).as_posix() != REGISTRE_PROPRE:
        raise GardeArret(f"registre {registre_rel} : seul {REGISTRE_PROPRE} reçoit les clés de B bis")
    if cle not in CLES_BBIS:
        raise GardeArret(f"clé {cle!r} hors des clés de B bis {CLES_BBIS} : refus")
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


def garde_depense(cumul_releve_usd: float, prix_carte_usd_h: float, coupure: float = COUPURE_USD) -> dict:
    """Arrêt (destruction par identifiant, R10) dès que cumul relevé + un quart d'heure de carte ≥ coupure."""
    projete = float(cumul_releve_usd) + QUART_D_HEURE * float(prix_carte_usd_h)
    if projete >= float(coupure):
        raise GardeArret(f"dépense : cumul relevé {cumul_releve_usd:.2f} USD + un quart d'heure de carte = {projete:.2f} USD ≥ "
                         f"coupure {coupure:g} USD : arrêt et destruction par identifiant (R10)")
    return {"cumul": float(cumul_releve_usd), "projete": projete, "coupure": float(coupure)}


def exiger_offre(offre: dict) -> dict:
    """Offre dans les bornes du devis ; H200 exclue (mot de Lazar seulement)."""
    fautes = []
    nom = str(offre.get("carte", ""))
    if "H200" in nom.upper():
        fautes.append("H200 exclue (mot de Lazar seulement)")
    if "A100" not in nom.upper() or "80" not in nom:
        fautes.append(f"carte {nom!r} : A100 80 Go attendue")
    if "SXM" not in nom.upper():
        fautes.append(f"carte {nom!r} : SXM4 attendue")
    for cle, minimum in (("coeurs", 16), ("memoire_vive_mo", 128000), ("disque_go", 150)):
        if float(offre.get(cle, 0)) < minimum:
            fautes.append(f"{cle} {offre.get(cle)} < {minimum}")
    if float(offre.get("stockage_usd_h", 1e9)) > OFFRE_MIN["stockage_max_usd_h"]:
        fautes.append(f"stockage {offre.get('stockage_usd_h')} USD/h > 0,08")
    if offre.get("etiquette") != ETIQUETTE:
        fautes.append(f"étiquette {offre.get('etiquette')!r} ≠ {ETIQUETTE}")
    if fautes:
        raise GardeArret("offre hors des bornes du devis : " + " ; ".join(fautes))
    return offre


def exiger_creation(racine: Path, feu_ecrit: str, maintenant: int, relances: int = 0) -> dict:
    """Aucune création sans `SCELLEMENT-BBIS`, `CODE-BBIS`, `GO-BBIS` (extrait de GO-2026-11-14-09) au registre propre et le feu
    écrit de la mère portant ce numéro ; une relance au plus ; échéance de la ligne de GO ; relance après le samedi 21
    novembre 12:00 UTC : nœud."""
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


__all__ = ["REGISTRE_PROPRE", "REGISTRE_PARTAGE", "CLES_BBIS", "GO_ID", "COUPURE_USD", "cles_bbis_presentes",
           "exiger_partage_sans_bbis", "ajouter_ligne_propre", "journaliser_ouverture", "garde_depense", "exiger_offre",
           "exiger_creation", "ETIQUETTE"]
