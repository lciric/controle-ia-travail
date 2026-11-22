"""Relevé des offres de cartes H100 SXM chez le loueur, pour le devis de la tranche de l'ajustement de nos lentilles (B-β) — v3.

v3 = v2 (`releve_prix_h100_v2.py`, `fb3d8bc6…`) corrigée selon la contre-lecture de la v8 du devis (mineures m-5 et m-6) :
- l'explication « une offre par hôte » est retirée : les relevés du 2026-11-18 la réfutent (deux offres d'un même hôte dans une même
  requête) ; la recherche ne rend pas toujours les mêmes offres d'une requête à l'autre, cause non établie ;
- l'épreuve d'une option ne s'applique qu'aux lignes du **filtre complet** (les requêtes témoins, plus larges, ne testent ni la
  fiabilité, ni la mémoire, ni le disque : leurs lignes reçoivent « - ») ;
- deux colonnes par option : `refus` (règle de la minuterie v4 : sous le prix minimal, la minuterie refuse de s'armer, l'offre est
  écartée) et `borne` (proposition du devis v9 : sous le prix minimal, la minuterie est armée à sa borne haute ; aucun prix minimal) ;
- les options portent leurs frais fixes de trafic, qui dépendent du lieu de rangement des lentilles (L1 : 1,00 ; L3 : 1,68 ; L2 : 3,40) ;
- les essais de l'épreuve sont versés à part (`essais_releve_prix_h100_v3.py`).

Lecture seule : `vastai search offers` ne loue rien et ne consomme aucun crédit. Trois requêtes, toutes avec `--limit 64` écrit :
1. requête témoin `gpu_name=H100_SXM num_gpus=1 rentable=true` (montre que la syntaxe rend des offres) ;
2. filtre complet du devis, sans borne de débit ni de prix (`FILTRE`) ;
3. requête témoin sans le filtre par défaut « machine vérifiée » de l'outil (`verified=any`), pour information.
L'outil applique par défaut `external=false rentable=true verified=true` et compte 5 Gio de stockage dans `dph_total`.

Prix avec 200 Go de stockage = `dph_total` + `storage_cost` × 200 / 720 (les 5 Gio déjà comptés dans `dph_total` le sont deux fois :
moins de 0,005 USD/h aux prix de stockage relevés).

Épreuve d'une option (prix exigé P, plafond C, frais fixes F), sur une ligne du filtre complet : machine vérifiée ; prix avec stockage au
plus P ; débit montant ≥ 200 Mbit/s ; trafic sortant et entrant ≤ 0,04 USD/Go chacun ; et, pour la règle `refus` seulement, prix avec
stockage au moins égal au prix minimal (0,9 × C − F) / 36 h.

Rien n'est imprimé ni écrit avant le balayage des secrets de la session (`suivi_vast_v6.balayer`, valeurs lues par leur nom seulement).

Usage : `PYTHONPATH=<src de prep/neuron-lens-v1> python docs/notes/neuron-lens-v1/devis-b-beta/releve_prix_h100_v3.py SORTIE.tsv`
(outil du loueur dans `VASTAI_OUTIL`, sinon `vastai`). Le module de balayage `controle_ia.neuron_lens.suivi_vast_v6` vit sur la
branche `prep/neuron-lens-v1` (commit `45a81e08`, empreinte `2ecaaeed2ea23071e9acacb200661086fb644eb52148c11f6da558fb9a160c7f`).
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys

TEMOIN = "gpu_name=H100_SXM num_gpus=1 rentable=true"
TEMOIN_NON_VERIFIEES = TEMOIN + " verified=any"
FILTRE = ("gpu_name=H100_SXM num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=200 inet_down>=300 reliability>0.98 "
          "cuda_max_good>=13.0 rentable=true")
LIMITE = 64
STOCKAGE_GO = 200
DEBIT_MONTANT_MIN = 200
TRAFIC_MAX = 0.04
SEUIL_ARRET = 0.90
BORNE_MAX_MINUTERIE_S = 129600
# (nom, prix exigé en USD/h, plafond en USD, frais fixes de trafic en USD) : options du § 7 de la v9 du devis
OPTIONS = (("L1_2.25_62", 2.25, 62.0, 1.00), ("L1_2.49_68", 2.49, 68.0, 1.00), ("L1_2.62_72", 2.62, 72.0, 1.00),
           ("L1_3.00_82", 3.00, 82.0, 1.00), ("L1_4.25_115", 4.25, 115.0, 1.00), ("L2_3.00_88", 3.00, 88.0, 3.40))
COLONNES = ("requete", "id", "machine_id", "host_id", "dph_total", "prix_avec_200_go", "storage_cost_usd_go_mois", "inet_up_mbit",
            "inet_up_cost_usd_go", "inet_down_cost_usd_go", "reliability", "verification", "gpu_ram_mio", "lieu") + tuple(
                f"{regle}_{nom}" for nom, _, _, _ in OPTIONS for regle in ("refus", "borne"))


def prix_minimal(plafond: float, frais_fixes: float) -> float:
    return (SEUIL_ARRET * plafond - frais_fixes) / (BORNE_MAX_MINUTERIE_S / 3600.0)


def prix_avec_stockage(o: dict) -> float:
    return float(o["dph_total"]) + float(o.get("storage_cost") or 0.0) * STOCKAGE_GO / 720.0


def passe(o: dict, prix_exige: float, plafond: float, frais_fixes: float, regle: str) -> bool:
    """Épreuve d'une offre du filtre complet ; `regle` vaut « refus » (prix minimal exigé) ou « borne » (aucun prix minimal)."""
    if regle not in ("refus", "borne"):
        raise ValueError(regle)
    prix = prix_avec_stockage(o)
    ok = (o.get("verification") == "verified" and prix <= prix_exige
          and float(o.get("inet_up") or 0.0) >= DEBIT_MONTANT_MIN
          and float(o.get("inet_up_cost") or 0.0) <= TRAFIC_MAX and float(o.get("inet_down_cost") or 0.0) <= TRAFIC_MAX)
    return ok and (regle == "borne" or prix >= prix_minimal(plafond, frais_fixes))


def chercher(requete: str) -> list[dict]:
    outil = os.environ.get("VASTAI_OUTIL", "vastai")
    p = subprocess.run([outil, "search", "offers", requete, "-o", "dph_total", "--limit", str(LIMITE), "--raw"],
                       capture_output=True, text=True, timeout=120)
    if p.returncode != 0 or not p.stdout.strip():
        raise SystemExit(f"relevé refusé : code {p.returncode} ou sortie vide (requête « {requete} »)")
    d = json.loads(p.stdout)
    if not isinstance(d, list):
        raise SystemExit(f"relevé refusé : forme inattendue ({type(d).__name__})")
    return d


def ligne(requete: str, o: dict) -> list[str]:
    base = [requete, str(o["id"]), str(o.get("machine_id")), str(o.get("host_id")), f"{float(o['dph_total']):.4f}",
            f"{prix_avec_stockage(o):.4f}", f"{float(o.get('storage_cost') or 0.0):.4f}", f"{float(o.get('inet_up') or 0.0):.0f}",
            f"{float(o.get('inet_up_cost') or 0.0):.4f}", f"{float(o.get('inet_down_cost') or 0.0):.4f}",
            f"{float(o.get('reliability') or 0.0):.4f}", str(o.get("verification")), str(o.get("gpu_ram")), str(o.get("geolocation"))]
    if requete != FILTRE:
        return base + ["-"] * (2 * len(OPTIONS))
    return base + ["oui" if passe(o, p, c, f, r) else "non" for _, p, c, f in OPTIONS for r in ("refus", "borne")]


def main(argv=None) -> int:
    from controle_ia.neuron_lens.suivi_vast_v6 import balayer, valeurs_secretes
    a = list(sys.argv[1:] if argv is None else argv)
    if len(a) != 1:
        raise SystemExit(__doc__)
    secrets = valeurs_secretes()
    heure = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lignes, comptes = [], {}
    for requete in (TEMOIN, FILTRE, TEMOIN_NON_VERIFIEES):
        offres = chercher(requete)
        comptes[requete] = len(offres)
        lignes += [ligne(requete, o) for o in offres]
    opts = " ; ".join(f"{nom} : prix exigé {p:.2f} USD/h, plafond {c:.0f} USD, frais fixes {f:.2f} USD, prix minimal (règle refus) "
                      f"{prix_minimal(c, f):.2f} USD/h" for nom, p, c, f in OPTIONS)
    tete = (f"# relevé vastai search offers {heure} (date UTC de la machine de la session) ; script releve_prix_h100_v3.py ; outil "
            f"vastai 1.11.0 ; --limit {LIMITE} ; requête témoin ({TEMOIN}) : {comptes[TEMOIN]} offre(s) ; filtre complet sans borne "
            f"de débit ni de prix ({FILTRE}) : {comptes[FILTRE]} offre(s) ; requête témoin sans le filtre « vérifiée » "
            f"({TEMOIN_NON_VERIFIEES}) : {comptes[TEMOIN_NON_VERIFIEES]} offre(s), pour information ; prix avec 200 Go = dph_total + "
            f"storage_cost × 200 / 720 ; épreuve sur les seules lignes du filtre complet : machine vérifiée, prix avec stockage au plus "
            f"le prix exigé, inet_up ≥ {DEBIT_MONTANT_MIN} Mbit/s, trafic sortant et entrant ≤ {TRAFIC_MAX} USD/Go, et prix minimal pour "
            f"la seule règle « refus » ; options : {opts}")
    texte = "\n".join([tete, "\t".join(COLONNES)] + ["\t".join(x) for x in lignes]) + "\n"
    texte = balayer(texte, secrets)
    with open(a[0], "w", encoding="utf-8") as fh:
        fh.write(texte)
    print(tete)
    print(f"{len(lignes)} ligne(s) écrite(s) dans {a[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
