#!/usr/bin/env python3
"""Barreau 5 : additif 1 au devis des familles d'adaptateurs jumeaux — plafond du stockage de l'instance de relecture.

Écrit par le concepteur (Claude Fable 5.2), le 21 novembre 2026. Aucune donnée du programme, aucun appel au loueur :
il lit le relevé d'offres du jour (fichier scellé, empreinte vérifiée) et refait l'arithmétique de la relecture avec
les formules du calcul du devis (`calcul-devis-formation-trois-membres-v1.py`, lignes « relecture à n adaptateurs »).

Bornes d'une offre : transcrites de `exiger_offre_lecture`, `src/controle_ia/barreau5_familles/relecture_v1.py`,
lignes 976 à 1004 au commit c76e79169eee337ce66c7d88f62d039e853eebfc (ligne CODE-LECTURE-B5F), plan « decisif ».
Le stockage de l'heure y est compté `storage_cost * 300 / 730` (USD par Go et par mois, 730 heures par mois).

Usage : python3 calcul-devis-adaptateurs-tenus-a-l-ecart-v1-additif-1.py [RACINE_DU_DEPOT]
"""
import hashlib, json, math, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(ICI, "..", "..", "..", ".."))
RELEVE = "prereg/papier-dopamine-moniteur-v1/releve-offres-loueur-cartes-2026-11-21T1055Z-v1.json"
RELEVE_SHA256 = "bc54f8bd468eb65e051234b31b77373aad1c52100b6e2b2a377532336f6a5196"

DISQUE_GO = 300
PLAFOND_SCELLE = 0.08          # devis scellé, § 1 et § 3 ; constante du code figé
PLAFOND_NEUF = 0.12            # additif 1
CANDIDATS = (0.08, 0.10, 0.12, 0.14)
COUPURE_RELECTURE, COUPURE_REPETITION, PLAFOND_COMMUN = 21, 8, 200
FORMATION = {"bas": 74.2, "haut": 108.9, "pire": 217.6, "coupures": 175}     # devis scellé, § 3
REPETITION = {"bas": 4.2, "haut": 6.4, "pire": 11.5}


def stockage_h(offre):
    return offre["storage_cost"] * DISQUE_GO / 730.0


def refus_hors_stockage(o, prix):
    """Motifs de refus de `exiger_offre_lecture` autres que le stockage ; `prix` : la valeur lue pour dph_total."""
    m = []
    if not all(x in str(o.get("gpu_name", "")).replace("_", " ") for x in ("A100", "SXM4")):
        m.append("carte")
    if o["num_gpus"] != 1: m.append("num_gpus")
    if o["gpu_ram"] < 80000: m.append("gpu_ram")
    if o["cpu_cores_effective"] < 16: m.append("coeurs")
    if o["cpu_ram"] < 128000: m.append("memoire_vive")
    if o["disk_space"] < DISQUE_GO: m.append("disque")
    if o["cuda_max_good"] < 13.0: m.append("cuda")
    if not 0 < prix <= 1.30: m.append("prix")
    return m


def relecture(n_series, s, go_de_plus=0.0):
    """Formules du calcul du devis ; s : stockage de l'heure ; rend (Go, h bas, h haut, USD bas, USD haut, pire)."""
    GO = 1.06 * 640 / 576
    go = (n_series * 3 + 3 + 9) * GO + go_de_plus
    fixe = 1.3 + 64 * 40.2 / 3600 + n_series * 84 / 3600 + 0.29 + 0.03 + 0.17
    lb = fixe + 0.25 + go * 1e9 / 100e6 / 3600
    lh = fixe + 0.60 + go * 1e9 / 30e6 / 3600
    bas = lb * (1.0889 + 0.03) + 40 * .026 + go * .026          # le bas ne dépend pas du plafond
    haut = lh * (1.30 + s) + 40 * .05 + go * .05
    pire = 2 * lh * (1.40 + s) + 40 * .05 + go * .05
    return go, lb, lh, bas, haut, pire


def main():
    chemin = os.path.join(RACINE, RELEVE)
    brut = open(chemin, "rb").read()
    sha = hashlib.sha256(brut).hexdigest()
    assert sha == RELEVE_SHA256, f"relevé d'une autre empreinte : {sha}"
    d = json.loads(brut)
    offres = d["offers"]
    print(f"relevé {RELEVE} sha256 {sha} : {len(offres)} offres, tronqué : {d.get('truncated')}")
    print(f"cartes de 80 Go au relevé : {sum(1 for o in offres if o['gpu_ram'] >= 80000)}")

    print("\n# 1. Les offres contre les bornes du code figé, stockage mis à part (disque de 300 Go)")
    print("# lecture (a) : dph_total tel qu'au relevé (cherché sans --storage : disque de 8 Go compté, cf. contrôle ci-dessous)")
    print("# lecture (b) : prix de l'heure à 300 Go, dph_base + storage_cost * 300 / 720 (formule du loueur, vérifiée ci-dessous)")
    ecart = max(abs(o["dph_total"] - (o["dph_base"] + o["storage_cost"] * 8 / 720)) for o in offres)
    print(f"contrôle de la formule du loueur : max |dph_total - (dph_base + storage_cost*8/720)| sur {len(offres)} offres = {ecart:.2e}")
    passent = {}
    for nom, prix_de in (("a", lambda o: o["dph_total"]), ("b", lambda o: o["dph_base"] + o["storage_cost"] * DISQUE_GO / 720)):
        passent[nom] = [o for o in offres if not refus_hors_stockage(o, prix_de(o))]
        print(f"lecture ({nom}) : {len(passent[nom])} offre(s) passent toutes les bornes hors stockage")
        for o in passent[nom]:
            print(f"   offre {o['id']} : carte {o['dph_base']:.4f} USD/h ; stockage {o['storage_cost']:.4f} USD/Go-mois, soit "
                  f"{stockage_h(o):.4f} USD/h à 300 Go (code, /730) ; prix lu {prix_de(o):.4f} ; disque {o['disk_space']:.0f} Go ; "
                  f"{o['cpu_cores_effective']:.0f} cœurs ; {o['cpu_ram']} Mo ; CUDA {o['cuda_max_good']} ; fiabilité {o['reliability']:.3f} ; "
                  f"sortie {o['inet_up_cost']:.4f} et entrée {o['inet_down_cost']:.4f} USD/Go")
    print("offres de 80 Go refusées hors stockage, lecture (a), et leur motif :")
    for o in offres:
        m = refus_hors_stockage(o, o["dph_total"])
        if o["gpu_ram"] >= 80000 and m:
            print(f"   offre {o['id']} : {', '.join(m)} (stockage à 300 Go : {stockage_h(o):.4f} USD/h)")

    print("\n# 2. Offres admises selon le plafond du stockage de l'heure")
    for s in CANDIDATS:
        na = [o["id"] for o in passent["a"] if stockage_h(o) <= s]
        nb = [o["id"] for o in passent["b"] if stockage_h(o) <= s]
        print(f"plafond {s:.2f} : lecture (a) {len(na)} offre(s) {na} ; lecture (b) {len(nb)} offre(s) {nb} ; "
              f"storage_cost admis jusqu'à {s * 730 / DISQUE_GO:.4f} USD/Go-mois")
    moins_cher = min(stockage_h(o) for o in passent["a"])
    print(f"stockage le moins cher parmi les offres qui passent le reste : {moins_cher:.4f} USD/h ; "
          f"marge sous {PLAFOND_NEUF:.2f} : {PLAFOND_NEUF - moins_cher:.4f} USD/h ({(PLAFOND_NEUF / moins_cher - 1) * 100:.1f} %)")
    print(f"pour mémoire, 0,2 USD/Go-mois à 300 Go : {0.2 * 300 / 730:.4f} USD/h (offres de 80 Go à ce prix : aucune ne passe le reste)")

    print("\n# 3. Coût de la relecture (39 adaptateurs, activations gardées en entier), formules du devis")
    res = {}
    for s in CANDIDATS:
        go, lb, lh, bas, haut, pire = relecture(39, s)
        res[s] = (bas, haut, pire)
        print(f"plafond {s:.2f} : {go:.1f} Go ; {lb:.2f} à {lh:.2f} h ; {bas:.1f} à {haut:.1f} USD (haut exact {haut:.2f}) ; pire {pire:.1f} "
              f"(exact {pire:.2f}) ; quatre cinquièmes du pire, arrondis au-dessus : {math.ceil(0.8 * pire)} ; "
              f"heures avant la coupure de 21 USD au prix plafond de la carte et au plafond du stockage, moins le quart d'heure : "
              f"{COUPURE_RELECTURE / (1.30 + s) - 0.25:.2f} (attendu haut {lh:.2f})")
    assert f"{res[0.08][0]:.1f} {res[0.08][1]:.1f} {res[0.08][2]:.1f}" == "9.6 17.1 25.6", "le calcul ne rend pas les chiffres du devis scellé"
    print("contrôle : au plafond scellé de 0,08, le calcul rend 9,6 à 17,1 USD et un pire cas de 25,6 : les chiffres du devis scellé")
    go, lb, lh, _, _, _ = relecture(39, PLAFOND_NEUF)
    s_max = (COUPURE_RELECTURE / 0.8 - 40 * .05 - go * .05) / (2 * lh) - 1.40
    print(f"plus haut plafond sous lequel la règle des quatre cinquièmes garde la coupure de 21 USD : {s_max:.4f} USD/h")
    g, b, h, bas, haut, pire = relecture(43, PLAFOND_NEUF)
    g8, _, _, bas8, haut8, pire8 = relecture(43, PLAFOND_SCELLE)
    print(f"avec les quatre points d'ancrage (43 séries, {g:.1f} Go) : {b:.2f} à {h:.2f} h ; {bas:.1f} à {haut:.1f} USD ; pire {pire:.1f} "
          f"(à 0,08 : {bas8:.1f} à {haut8:.1f} ; pire {pire8:.1f}) ; écart dû au plafond : +{haut - haut8:.2f} et +{pire - pire8:.2f}")

    print("\n# 4. Sur l'offre admise au relevé, aux prix de cette offre (heures du devis)")
    for o in [x for x in passent["a"] if stockage_h(x) <= PLAFOND_NEUF]:
        go, lb, lh, _, _, _ = relecture(39, 0)
        prix = o["dph_base"] + o["storage_cost"] * DISQUE_GO / 720
        fixe = 40 * o["inet_down_cost"] + go * o["inet_up_cost"]
        print(f"offre {o['id']} : {prix:.4f} USD/h à 300 Go (marge sous 1,30 : {1.30 - prix:.4f}) ; entrée de 40 Go et sortie de {go:.1f} Go : {fixe:.2f} USD ; "
              f"relecture {lb * prix + fixe:.1f} à {lh * prix + fixe:.1f} USD ; hôte deux fois plus lent : {2 * lh * prix + fixe:.1f} USD ; "
              f"heures avant la coupure moins le quart d'heure : {COUPURE_RELECTURE / prix - 0.25:.2f}")

    print("\n# 5. Ensemble chez le loueur de cartes, avant et après l'additif")
    for nom, s in (("devis scellé (0,08)", PLAFOND_SCELLE), (f"additif 1 ({PLAFOND_NEUF:.2f})", PLAFOND_NEUF)):
        bas, haut, pire = res[s]
        print(f"{nom} : attendu {FORMATION['bas'] + bas + REPETITION['bas']:.1f} à {FORMATION['haut'] + haut + REPETITION['haut']:.1f} USD "
              f"(exact {FORMATION['haut'] + haut + REPETITION['haut']:.2f}) ; pire {FORMATION['pire'] + pire + REPETITION['pire']:.1f} ; "
              f"coupures {FORMATION['coupures']} + {COUPURE_RELECTURE} + {COUPURE_REPETITION} = "
              f"{FORMATION['coupures'] + COUPURE_RELECTURE + COUPURE_REPETITION} ; plafond commun {PLAFOND_COMMUN}")
    print(f"écart dû à l'additif : attendu haut +{res[PLAFOND_NEUF][1] - res[PLAFOND_SCELLE][1]:.2f} USD ; pire cas +{res[PLAFOND_NEUF][2] - res[PLAFOND_SCELLE][2]:.2f} USD ; "
          f"attendu bas, coupures et plafond commun : inchangés")


if __name__ == "__main__":
    main()
