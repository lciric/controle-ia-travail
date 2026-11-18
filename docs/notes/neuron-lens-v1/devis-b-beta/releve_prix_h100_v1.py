"""Relevé des offres de cartes H100 SXM chez le loueur, pour le devis de la tranche de l'ajustement de nos lentilles (B-β) — v1.

Lecture seule : `vastai search offers` ne loue rien et ne consomme aucun crédit. Trois requêtes, les deux premières étant celles du
relevé du 2026-11-17T01:27:12Z (`releve-prix-vast-h100-20261117T012712Z-v1.tsv`), toutes avec `--limit 64` écrit :
1. requête témoin `gpu_name=H100_SXM num_gpus=1 rentable=true` (montre que la syntaxe rend des offres) ;
2. filtre complet du devis, sans borne de débit ni de prix (`FILTRE`) ;
3. requête témoin sans le filtre par défaut « machine vérifiée » de l'outil (`verified=any`), pour information seulement : le devis
   garde les machines vérifiées, comme en B-α.
L'outil applique par défaut `external=false rentable=true verified=true` et compte 5 Gio de stockage dans `dph_total` ; la recherche
rend une offre par hôte, et l'identifiant d'offre peut changer d'une requête à l'autre sur une même machine (colonne `machine_id`).
Prix avec 200 Go de stockage = `dph_total` + `storage_cost` × 200 / 720 (stockage facturé au Go et au mois de 30 jours ; même
formule que les relevés précédents, qui redonne leurs colonnes ; les 5 Gio déjà comptés dans `dph_total` sont comptés deux fois,
soit moins de 0,005 USD/h aux prix de stockage relevés). Chaque ligne dit si l'offre passe les exigences du devis : prix avec
stockage ≤ `PRIX_EXIGE`, débit montant ≥ 200 Mbit/s, trafic sortant et entrant ≤ 0,04 USD/Go chacun.

Rien n'est imprimé ni écrit avant le balayage des secrets de la session (`suivi_vast_v6.balayer`, valeurs lues par leur nom seulement).

Usage : `PYTHONPATH=<src de prep/neuron-lens-v1> python docs/notes/neuron-lens-v1/devis-b-beta/releve_prix_h100_v1.py SORTIE.tsv`
(outil du loueur dans `VASTAI_OUTIL`, sinon `vastai`). Le module de balayage `controle_ia.neuron_lens.suivi_vast_v6` vit sur la
branche `prep/neuron-lens-v1` (commit `45a81e08`, empreinte `2ecaaeed2ea23071e9acacb200661086fb644eb52148c11f6da558fb9a160c7f`),
pas sur la branche de session où ce script est versé.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import subprocess
import sys

from controle_ia.neuron_lens.suivi_vast_v6 import balayer, valeurs_secretes

TEMOIN = "gpu_name=H100_SXM num_gpus=1 rentable=true"
TEMOIN_NON_VERIFIEES = TEMOIN + " verified=any"
LIMITE = 64
FILTRE = ("gpu_name=H100_SXM num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=200 inet_down>=300 reliability>0.98 "
          "cuda_max_good>=13.0 rentable=true")
STOCKAGE_GO = 200
PRIX_EXIGE = 3.00
DEBIT_MONTANT_MIN = 200
TRAFIC_MAX = 0.04
COLONNES = ("requete", "id", "machine_id", "dph_total", "prix_avec_200_go", "storage_cost_usd_go_mois", "inet_up_mbit", "inet_up_cost_usd_go",
            "inet_down_cost_usd_go", "reliability", "verification", "gpu_ram_mio", "lieu", "passe_exigences")


def chercher(requete: str) -> list[dict]:
    outil = os.environ.get("VASTAI_OUTIL", "vastai")
    p = subprocess.run([outil, "search", "offers", requete, "-o", "dph_total", "--limit", str(LIMITE), "--raw"],
                       capture_output=True, text=True,
                       timeout=120)
    if p.returncode != 0 or not p.stdout.strip():
        raise SystemExit(f"relevé refusé : code {p.returncode} ou sortie vide (requête « {requete} »)")
    d = json.loads(p.stdout)
    if not isinstance(d, list):
        raise SystemExit(f"relevé refusé : forme inattendue ({type(d).__name__})")
    return d


def ligne(requete: str, o: dict) -> list[str]:
    prix = float(o["dph_total"]) + float(o.get("storage_cost") or 0.0) * STOCKAGE_GO / 720.0
    passe = (prix <= PRIX_EXIGE and float(o.get("inet_up") or 0.0) >= DEBIT_MONTANT_MIN
             and float(o.get("inet_up_cost") or 0.0) <= TRAFIC_MAX and float(o.get("inet_down_cost") or 0.0) <= TRAFIC_MAX)
    return [requete, str(o["id"]), str(o.get("machine_id")), f"{float(o['dph_total']):.4f}", f"{prix:.4f}", f"{float(o.get('storage_cost') or 0.0):.4f}",
            f"{float(o.get('inet_up') or 0.0):.0f}", f"{float(o.get('inet_up_cost') or 0.0):.4f}",
            f"{float(o.get('inet_down_cost') or 0.0):.4f}", f"{float(o.get('reliability') or 0.0):.4f}", str(o.get("verification")),
            str(o.get("gpu_ram")), str(o.get("geolocation")), "oui" if passe else "non"]


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if len(a) != 1:
        raise SystemExit(__doc__)
    secrets = valeurs_secretes()
    heure = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lignes = []
    comptes = {}
    for requete in (TEMOIN, FILTRE, TEMOIN_NON_VERIFIEES):
        offres = chercher(requete)
        comptes[requete] = len(offres)
        lignes += [ligne(requete, o) for o in offres]
    tete = (f"# relevé vastai search offers {heure} (date UTC de la machine de la session) ; outil vastai 1.11.0 ; requête témoin "
            f"({TEMOIN}) : {comptes[TEMOIN]} offre(s) ; filtre complet sans borne de débit ni de prix ({FILTRE}) : "
            f"{comptes[FILTRE]} offre(s) ; requête témoin sans le filtre « vérifiée » ({TEMOIN_NON_VERIFIEES}) : "
            f"{comptes[TEMOIN_NON_VERIFIEES]} offre(s), pour information ; --limit {LIMITE} ; prix avec 200 Go = dph_total + storage_cost × 200 / 720 ; exigences du devis : prix avec "
            f"stockage ≤ {PRIX_EXIGE:.2f} USD/h, inet_up ≥ {DEBIT_MONTANT_MIN} Mbit/s, trafic sortant et entrant ≤ {TRAFIC_MAX} USD/Go")
    texte = "\n".join([tete, "\t".join(COLONNES)] + ["\t".join(x) for x in lignes]) + "\n"
    texte = balayer(texte, secrets)
    with open(a[0], "w", encoding="utf-8") as f:
        f.write(texte)
    print(tete)
    print(f"{len(lignes)} ligne(s) écrite(s) dans {a[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
