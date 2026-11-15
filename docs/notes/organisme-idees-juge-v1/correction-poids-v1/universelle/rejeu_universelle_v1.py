"""Rejeu des programmes de l'auteur (angle « inférence universelle ») et comparaison à ses sorties scellées — v1.

Réfutation, mise au point exploratoire, aucune revendication. Ce programme ne modifie aucun fichier de l'auteur : il lance
ses scripts tels quels (`essai_universelle_lot_v1.py`, `essai_universelle_taille_v1.py`), avec leurs graines (entropies
20261115101 pour la taille, 20261115201 pour la puissance, clé (indice du cas, r)), en écrivant leurs sorties dans un
dossier de travail hors du dépôt, puis compare monde par monde aux sorties scellées (même clé ⇒ même monde : un rejeu
sur les R' premiers mondes se compare au début de la chaîne « promue » et de la liste « log_w_max » de la sortie scellée).

Usage :
  python rejeu_universelle_v1.py jouer DOSSIER_TRAVAIL ETAPE [ETAPE…]   (une étape = un lancement, dix minutes au plus)
  python rejeu_universelle_v1.py assembler DOSSIER_TRAVAIL SORTIE.json    (réunit les comparaisons ; jamais d'écrasement)
"""
import hashlib, json, os, signal, subprocess, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
DUREE_MAX_S = 585

A_PUIS = "v8,limite,v9,v9_dense,confiance,moitie_jugee,penalise_1nat,melange_a_priori,fiche_en_ligne_0.05,fiche_moitie"
B_PUIS = "v9,croisee,sous_echantillons"
A_TAIL = "v8,limite,v9,penalise_1nat,penalise_bic,melange_a_priori,fiche_en_ligne_0.05,fiche_en_ligne_0.2,fiche_moitie"
B_TAIL = "moitie_jugee,croisee,confiance,sous_echantillons"
FICHES = "fiche_en_ligne_0.05,fiche_en_ligne_0.2,fiche_moitie"

# étape : (script, [arguments avant la sortie], argument après la sortie ou None, sortie scellée de référence ou None)
ETAPES = {}
for dose in ("0.25", "0.40", "0.55"):
    ETAPES[f"puissance-{dose}-a"] = ("lot", ["puissance", dose, "300", A_PUIS], f"sortie-puissance-{dose}-a-v1.json")
    ETAPES[f"puissance-{dose}-b"] = ("lot", ["puissance", dose, "300", B_PUIS], f"sortie-puissance-{dose}-b-v1.json")
for cas in ("sommet", "extreme", "bruite", "sous_population", "grille"):
    ETAPES[f"fiches-{cas}"] = ("lot", ["taille", cas, "1000", FICHES], f"sortie-taille-{cas}-a-v1.json")
    ETAPES[f"taille-{cas}-a"] = ("lot", ["taille", cas, "250", A_TAIL], f"sortie-taille-{cas}-a-v1.json")
    ETAPES[f"taille-{cas}-b"] = ("lot", ["taille", cas, "150", B_TAIL], f"sortie-taille-{cas}-b-v1.json")
ETAPES["taille-interieur-a"] = ("taille", ["interieur", "1000"], "sortie-taille-interieur-v1.json", A_TAIL)
ETAPES["taille-interieur-b"] = ("lot", ["taille", "interieur", "150", B_TAIL], None)
ETAPES["dense-interieur"] = ("lot", ["taille", "interieur", "200", "v9_dense"], "sortie-taille-interieur-dense-v1.json")
ETAPES["dense-sommet"] = ("lot", ["taille", "sommet", "200", "v9_dense"], "sortie-taille-sommet-dense-v1.json")
ETAPES["puissance-0.25-fine"] = ("lot", ["puissance", "0.25", "200", "v8,limite,v9,confiance"], "sortie-puissance-0.25-fine-v1.json", "fine")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def comparer(nouveau, reference):
    """Compare un rejeu (R' mondes) à la sortie scellée (R mondes, R' ≤ R) : promotions monde par monde, log W maximal."""
    out = {"mondes_rejoues": nouveau["mondes"], "mondes_reference": reference["mondes"], "methodes": {}}
    Rn = nouveau["mondes"]
    for m, v in nouveau["resume"].items():
        ligne = {"promotions_rejeu": v["promotions"], "log_w_max_plus_grand_rejeu": v["log_w_max_plus_grand"]}
        ref_res = reference["resume"].get(m)
        if ref_res is None:
            ligne["dans_la_reference"] = False
            out["methodes"][m] = ligne
            continue
        if Rn == reference["mondes"]:
            ligne["promotions_reference"] = ref_res["promotions"]
            ligne["comptes_egaux"] = v["promotions"] == ref_res["promotions"]
            ligne["log_w_max_plus_grand_egal"] = v["log_w_max_plus_grand"] == ref_res["log_w_max_plus_grand"]
            ligne["log_w_max_median_egal"] = v["log_w_max_median"] == ref_res["log_w_max_median"]
        pm_ref = reference.get("par_monde", {}).get(m)
        pm_new = nouveau.get("par_monde", {}).get(m)
        if pm_ref is not None and pm_new is not None:
            a, b = pm_new["promue"], pm_ref["promue"][:Rn]
            ligne["promotions_reference_sur_les_memes_mondes"] = b.count("1")
            ligne["mondes_en_desaccord"] = sum(1 for x, y in zip(a, b) if x != y)
            la, lb = pm_new["log_w_max"], pm_ref["log_w_max"][:Rn]
            ligne["plus_grand_ecart_de_log_w_max"] = max(abs(x - y) for x, y in zip(la, lb))
        out["methodes"][m] = ligne
    return out


def jouer(travail, nom):
    etape = ETAPES[nom]
    sorte, args, ref = etape[0], etape[1], etape[2]
    apres = etape[3] if len(etape) > 3 else None
    sortie = os.path.join(travail, f"rejeu-{nom}.json")
    if os.path.exists(sortie):
        raise SystemExit(f"rejeu existant, jamais écrasé : {sortie}")
    script = os.path.join(ICI, "essai_universelle_lot_v1.py" if sorte == "lot" else "essai_universelle_taille_v1.py")
    cmd = [PY, "-I", "-B", script] + args + [sortie] + ([apres] if apres else [])
    t0 = time.time()
    r = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    try:
        _, erreur = r.communicate(timeout=DUREE_MAX_S)
    except subprocess.TimeoutExpired:
        # dix minutes au plus par simulation : arrêt par identifiant du groupe de processus (R10), étape dite non jouée
        os.killpg(r.pid, signal.SIGKILL)
        r.communicate()
        with open(os.path.join(travail, f"depassement-{nom}.txt"), "x") as f:
            f.write(f"étape {nom} arrêtée après {DUREE_MAX_S} s (règle des dix minutes)\n")
        print(nom, "arrêtée : dépassement de", DUREE_MAX_S, "s", flush=True)
        return
    duree = time.time() - t0
    if r.returncode != 0:
        raise SystemExit(f"échec du rejeu {nom} : {erreur[-2000:]}")
    nouveau = json.load(open(sortie))
    doc = {"etape": nom, "commande": [os.path.basename(script)] + args + (["fine"] if apres == "fine" else ([apres] if apres else [])),
           "duree_s": round(duree, 1), "graines": nouveau["graines"], "empreinte_rejeu": sha(sortie),
           "empreintes_code_au_rejeu": nouveau["empreintes_code"]}
    if ref is not None:
        pref = os.path.join(ICI, ref)
        h = sha(pref)
        if h != open(pref + ".sha256").read().split()[0]:
            raise SystemExit(f"empreinte de la référence non conforme : {ref}")
        reference = json.load(open(pref))
        doc["reference"] = {"fichier": ref, "sha256": h}
        doc["code_identique_a_la_reference"] = (nouveau["empreintes_code"]["banc_universelle_v1.py"]
                                                == reference["empreintes_code"]["banc_universelle_v1.py"])
        doc["comparaison"] = comparer(nouveau, reference)
    else:
        doc["reference"] = None
        doc["resume_rejeu"] = {m: {"promotions": v["promotions"], "mondes": v["mondes"],
                                   "log_w_max_plus_grand": v["log_w_max_plus_grand"]} for m, v in nouveau["resume"].items()}
    with open(os.path.join(travail, f"comparaison-{nom}.json"), "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    court = {m: (v.get("mondes_en_desaccord"), v.get("comptes_egaux"), v.get("plus_grand_ecart_de_log_w_max"))
             for m, v in doc.get("comparaison", {}).get("methodes", {}).items()}
    print(nom, round(duree, 1), "s", json.dumps(court if court else doc.get("resume_rejeu"), ensure_ascii=False), flush=True)


def assembler(travail, sortie):
    if os.path.exists(sortie):
        raise SystemExit("sortie existante, jamais écrasée")
    doc = {"essai": "rejeu des programmes de l'auteur", "version": "v1", "statut": "mise au point exploratoire, aucune revendication",
           "etapes": {}}
    for nom in ETAPES:
        p = os.path.join(travail, f"comparaison-{nom}.json")
        if os.path.exists(p):
            doc["etapes"][nom] = json.load(open(p))
    doc["etapes_non_jouees"] = [n for n in ETAPES if n not in doc["etapes"]]
    with open(sortie, "x", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(len(doc["etapes"]), "étapes réunies ;", "non jouées :", doc["etapes_non_jouees"])


if __name__ == "__main__":
    if sys.argv[1] == "jouer":
        for nom in sys.argv[3:]:
            jouer(sys.argv[2], nom)
    elif sys.argv[1] == "assembler":
        assembler(sys.argv[2], sys.argv[3])
    else:
        raise SystemExit(__doc__)
