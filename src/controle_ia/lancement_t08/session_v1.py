"""Session de la chaîne de lancement de T0.8, v1 (consigne `722ceb5e…`, tenue en v3 `6f52c4db…` ; texte au brouillon 15 `8d68b7a0…`, § 3.4 et 3.5). Bibliothèque standard et modules de
session de T0.6 seulement ; aucun appel au réseau ni à l'outil de location.

Ce qui change par rapport à la chaîne de la course de confirmation (`t06.session_v12` et précédents), et rien d'autre :

1. **Ligne de GO lue au registre, prolongation comprise** (`go_t08`). La configuration de la course porte, sous `lancement`,
   l'accord d'origine (`go_origine`, marqueur `GO_T08` du texte : `GO-2026-11-10-12`, plafond 120 USD), les lignes admises
   (`go_admis` : l'origine, puis les prolongations que le texte cite) et le plafond. La ligne `GO_ID` (variable
   d'environnement, convention de la garde de calcul) doit être admise ; elle est de type « calcul », accordée par Lazar,
   valide au jour donné (accord ≤ jour ≤ échéance), non révoquée, toute seconde ligne au même identifiant étant une extension
   conforme (R-389). Si ce n'est pas l'origine, c'est une prolongation : son périmètre commence par « Prolongation de
   <origine> » et sa cellule de plafond vaut « plafond de <origine> » (ou le plafond même). La ligne d'origine est de type
   « calcul », accordée par Lazar, non révoquée, et porte le plafond de la configuration, exact ; son échéance peut être
   passée quand la ligne employée est une prolongation. Une révocation qui cite l'origine ou la ligne employée arrête.
   `session_v12.ligne_go_calcul` refusait les prolongations (plafond « plafond de … » illisible).
2. **Calendrier lu au registre** (`calendrier_t08`) : fin de validité = lendemain 00:00 UTC de l'échéance de la ligne
   employée ; dernier jour de création = cette échéance. La configuration ne porte aucun calendrier (la ligne employée n'est
   connue qu'au lancement).
3. **Vue de l'offre** (`vue_offre`) : `{"carte": {"course": …}, "offre": …}`, forme que lisent `session_v12.filtre_recherche` et
   `choisir_offre`, tirée de `lancement` ; **aucune carte de relance** : une configuration qui en porte une est refusée, et la
   seule carte demandable est `course` (aucune H200, section « Machine » du texte).
4. **Surveillance** (`decider_surveillance_t08`) : celle de la v3 au plafond de la configuration, plus une ligne
   « ALERTE compte rendu » quand la dépense cumulée atteint le seuil du compte rendu (40 USD, texte), jamais un arrêt ; la ligne
   « FIN » dit la destruction après le versement prouvé (texte : aucune garde de 72 heures ; contre-lecture M-3), non plus
   « disque gardé jusqu'au verdict ».

    python -I -m controle_ia.lancement_t08.session_v1 go REGISTRE_GO.md CONFIG.json GO_ID [AAAA-MM-JJ]
    python -I -m controle_ia.lancement_t08.session_v1 calendrier REGISTRE_GO.md CONFIG.json GO_ID [AAAA-MM-JJ]
    python -I -m controle_ia.lancement_t08.session_v1 vue CONFIG.json SORTIE.json
    python -I -m controle_ia.lancement_t08.session_v1 surveillance PLAFOND COMPTE_RENDU JOURNAL MAINTENANT_S PRIX_CARTE PRIX_STOCKAGE CREE_LE_S ANTERIEURE TELECHARGEMENT [FACTURE]
    autres sous-commandes : celles de `t06.session_v12` (`filtre`, `choisir`, `presente`, `seule`, `depense`, `instances`, …).
Codes : 0 ; 1 avec un motif sur la dernière ligne ; 2 usage (ou relevé non concluant, comme la v12).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from ..t06 import session as s1
from ..t06 import session_v3 as s3
from ..t06 import session_v12 as s12
from ..t06.session import GardeSession, _nombre

PREFIXE_PROLONGATION = "Prolongation de "


def _lignes(registre) -> list[dict]:
    fichier = Path(registre)
    if not fichier.is_file():
        raise GardeSession(f"registre {registre} absent")
    lignes = []
    for n, l in enumerate(fichier.read_text(encoding="utf-8").splitlines(), 1):
        if s1.LIGNE_GO.match(l):
            c = s1._cellules(l)
            if len(c) != 8:
                raise GardeSession(f"ligne {n} : 8 colonnes attendues, {len(c)}")
            lignes.append(dict(zip(s1.COLONNES, c), ligne=n))
    return lignes


def _ligne(lignes: list[dict], go_id: str) -> dict:
    propres = [l for l in lignes if l["id"] == go_id]
    if not propres:
        raise GardeSession(f"{go_id} absent du registre")
    g, autres = propres[0], propres[1:]
    if g["type"] != "calcul":
        raise GardeSession(f"{go_id} : type {g['type']!r}, « calcul » attendu")
    if g["par"] != "Lazar":
        raise GardeSession(f"{go_id} : accordé par {g['par']!r}, « Lazar » attendu")
    accorde, echeance = s1._date(g["accorde"], "accord"), s1._date(g["echeance"], "échéance")
    for a in autres:
        if not (a["perimetre"].lower().startswith("extension") and a["type"] == "calcul" and a["par"] == "Lazar"
                and s1._date(a["accorde"], "extension") >= accorde and s1._date(a["echeance"], "extension") <= echeance):
            raise GardeSession(f"{go_id} : ligne {a['ligne']} en double, autre qu'une extension conforme (R-389)")
    return {**g, "accorde_d": accorde, "echeance_d": echeance}


def _revoque(lignes: list[dict], go_id: str) -> str | None:
    for l in lignes:
        if l["type"] == "révocation" and (go_id in l["perimetre"] or go_id in l["ref"]):
            return l["id"]
    return None


def _lancement(config: dict) -> dict:
    l = config.get("lancement") if isinstance(config, dict) else None
    if not isinstance(l, dict):
        raise GardeSession("configuration sans section « lancement »")
    for k in ("go_origine", "go_admis", "plafond_usd", "compte_rendu_usd", "carte", "offre"):
        if k not in l:
            raise GardeSession(f"lancement : clé {k} absente")
    if not (isinstance(l["go_admis"], list) and l["go_admis"] and l["go_admis"][0] == l["go_origine"]):
        raise GardeSession("lancement : go_admis doit commencer par go_origine")
    if set(l["carte"]) != {"course"}:
        raise GardeSession(f"lancement : cartes {sorted(l['carte'])} ; « course » seule admise (aucune relance, aucune H200)")
    return l


def go_t08(registre, config: dict, go_id: str, jour: date | None = None) -> dict:
    l = _lancement(config)
    if not s3.ID_GO.fullmatch(str(go_id)):
        raise GardeSession(f"identifiant de GO illisible : {go_id!r} (GO-AAAA-MM-JJ-NN attendu)")
    if go_id not in l["go_admis"]:
        raise GardeSession(f"{go_id} hors des lignes admises par la configuration {l['go_admis']}")
    origine = l["go_origine"]
    plafond = _nombre(l["plafond_usd"], "plafond", positif=True)
    lignes = _lignes(registre)
    o = _ligne(lignes, origine)
    if s3._plafond_ligne(o["plafond"]) != plafond:
        raise GardeSession(f"{origine} : plafond {o['plafond']!r}, « {plafond:g} USD » exact attendu (configuration)")
    g = o if go_id == origine else _ligne(lignes, go_id)
    if go_id != origine:
        if not re.match(re.escape(PREFIXE_PROLONGATION + origine) + r"(?![0-9A-Za-z_-])", g["perimetre"]):   # m-3 : frontière
            raise GardeSession(f"{go_id} : périmètre ne commençant pas par « {PREFIXE_PROLONGATION}{origine} » : pas une "
                               "prolongation de l'accord d'origine")
        if g["plafond"] != f"plafond de {origine}" and s3._plafond_ligne(g["plafond"]) != plafond:
            raise GardeSession(f"{go_id} : plafond {g['plafond']!r} ≠ « plafond de {origine} » ni « {plafond:g} USD »")
    j = jour or datetime.now(timezone.utc).date()
    if not g["accorde_d"] <= j <= g["echeance_d"]:
        raise GardeSession(f"{go_id} hors de sa période de validité ({g['accorde_d']} → {g['echeance_d']}) le {j}")
    for x in (origine, go_id):
        r = _revoque(lignes, x)
        if r:
            raise GardeSession(f"{x} révoqué par {r}")
    fin = datetime.combine(g["echeance_d"] + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc)
    return {"go": go_id, "origine": origine, "plafond_usd": plafond, "accorde": str(g["accorde_d"]),
            "echeance": str(g["echeance_d"]), "fin_go_utc_s": int(fin.timestamp()), "jour": str(j)}


def calendrier_t08(registre, config: dict, go_id: str, jour: date | None = None) -> dict:
    g = go_t08(registre, config, go_id, jour)
    return {"fin_go_utc_s": g["fin_go_utc_s"], "dernier_jour_creation": g["echeance"], "echeance_go": g["echeance"],
            "jour": g["jour"]}


def vue_offre(config: dict) -> dict:
    l = _lancement(config)
    o = l["offre"]
    for k in ("coeurs_effectifs_min", "disque_min_go", "etiquette", "memoire_vive_min_mo", "stockage_max_usd_h",
              "telechargement_go_prevu", "telechargement_max_usd_go"):
        if k not in o:
            raise GardeSession(f"lancement.offre : clé {k} absente")
    c = l["carte"]["course"]
    for k in ("nom", "nom_offre", "memoire_carte_min_mo", "prix_max_usd_h"):
        if k not in c:
            raise GardeSession(f"lancement.carte.course : clé {k} absente")
    if "H200" in str(c["nom_offre"]) or "H200" in str(c["nom"]):
        raise GardeSession("carte H200 : jamais sans un mot de Lazar (section « Machine »)")
    return {"carte": {"course": dict(c)}, "offre": dict(o), "go_id": l["go_origine"], "plafond_usd": l["plafond_usd"]}


def decider_surveillance_t08(journal: str, maintenant_s: float, depense: dict, compte_rendu_usd) -> str:
    d = s3.decider_surveillance_v3(journal, maintenant_s, depense)
    if d.startswith("FIN"):                     # contre-lecture M-3 : destruction après le versement prouvé, aucune garde du disque
        return ("FIN : run terminé (ligne de fin de l'amorce) ; l'amorce détruit la machine après le versement prouvé ; vérifier "
                "la poussée, puis l'inventaire ; machine encore là : destruction par l'identifiant (R10)")
    seuil = _nombre(compte_rendu_usd, "seuil du compte rendu", positif=True)
    if d == "POURSUIVRE" and depense["cumulee_usd"] >= seuil:
        return (f"ALERTE compte rendu : dépense cumulée {depense['cumulee_usd']:.2f} USD ≥ {seuil:g} USD : compte rendu à "
                "Lazar par la session mère ; aucun arrêt")
    return d


def _lire_json(p) -> dict:
    try:
        return json.loads(Path(p).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise GardeSession(f"{p} illisible ({e.__class__.__name__})") from None


def _jour(argv: list[str], n: int) -> date | None:
    return date.fromisoformat(argv[n]) if len(argv) > n else None


def main(argv: list[str]) -> int:
    try:
        if len(argv) in (4, 5) and argv[0] == "go":
            r = go_t08(argv[1], _lire_json(argv[2]), argv[3], _jour(argv, 4))
            print(f"{r['go']} conforme (origine {r['origine']}, plafond {r['plafond_usd']:g} USD, {r['accorde']} → "
                  f"{r['echeance']}) fin_go_utc_s={r['fin_go_utc_s']}")
            return 0
        if len(argv) in (4, 5) and argv[0] == "calendrier":
            r = calendrier_t08(argv[1], _lire_json(argv[2]), argv[3], _jour(argv, 4))
            print(f"fin_go_utc_s={r['fin_go_utc_s']} dernier_jour_creation={r['dernier_jour_creation']} "
                  f"echeance_go={r['echeance_go']}")
            return 0
        if len(argv) == 3 and argv[0] == "vue":
            v = vue_offre(_lire_json(argv[1]))
            if Path(argv[2]).exists():
                raise GardeSession(f"{argv[2]} existe déjà (R12)")
            Path(argv[2]).write_text(json.dumps(v, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            print(f"vue de l'offre écrite : {argv[2]}")
            return 0
        if len(argv) in (10, 11) and argv[0] == "surveillance":
            texte = Path(argv[3]).read_text(encoding="utf-8") if Path(argv[3]).is_file() else ""
            now = _nombre(argv[4], "maintenant")
            d = s3.depense_cumulee_v3(argv[1], argv[5], argv[6], argv[7], argv[8], argv[9], now,
                                      argv[10] if len(argv) > 10 else None)
            print(decider_surveillance_t08(texte, now, d, argv[2]))
            return 0
    except (GardeSession, ValueError) as e:              # ValueError : jour illisible ; jamais un repli
        print(str(e))
        return 1
    if argv and argv[0] in ("go", "calendrier", "vue", "surveillance"):
        print(f"usage : {argv[0]} : voir l'en-tête de lancement_t08.session_v1 (nombre d'arguments)", file=sys.stderr)
        return 2
    if argv and argv[0] in ("go-ligne", "plafond-ligne", "plafond"):
        print(f"{argv[0]} : sous-commande des épreuves de T0.6, non offerte pour T0.8 (lignes de GO : « go »)", file=sys.stderr)
        return 2
    return s12.main(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
