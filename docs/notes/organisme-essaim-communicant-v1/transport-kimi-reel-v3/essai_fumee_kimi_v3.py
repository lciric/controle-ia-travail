#!/usr/bin/env python3
"""Essai de fumée du transport réel sur Kimi (H1 à H4) — v3 (= v2 sur le transport v3 ; registre « fumee-kimi-v3 »). **Six appels au plus, une seule fois** ; aucun envoi relancé.
Chaîne : `TransportKimiReel` v2 → `AdaptateurKimiStrict` v2 → registre `registre_depense_v1` neuf (réserve scellée avant
chaque appel). Les pièces v4 importées sont vérifiées **à leur empreinte** avant l'import (sinon code 2, rien n'est créé).

Différences avec la v1 (contre-lecture `transport-kimi-reel-v1/contre-lecture-v1/`, B1 et B2) :
- **B1** : le journal garde, pour chaque appel, le diagnostic entier du transport (masqué) : `usage_brut` (chaque `usage`
  non nul reçu, avec ses feuilles imbriquées : `completion_tokens_details.reasoning_tokens`,
  `prompt_tokens_details.cache_write_tokens`, `cached_tokens`…), `usage_refuse` (motif d'un usage refusé),
  `en_tetes_id`, `coupure_sortie`, `id_reponse`, statut, durée ;
- **B2, plafond dur** (1 USD au plus) : avant l'appel, dépense + réserve ≤ plafond (sinon 14) ; après l'appel, **arrêt**
  si le coût mesuré dépasse la réserve (16), si l'usage est refusé (16, compté à la réserve), si la dépense dépasse le
  plafond (14), si un appel autre que f5 échoue (13) ; le transport coupe le flux côté client dès que la sortie lue dépasse
  `max_tokens` ; **f2 (`max_tokens` 16) passe en premier** ; `max_tokens` et `max_completion_tokens` sont envoyés tous deux
  (`--champs-max` pour n'en garder qu'un, sous un nouveau GO et un registre neuf) ;
- GO : un amont autre que `http://` vers la boucle locale (hôte exact, URL analysée) exige `GO_ID` de la forme
  `GO-AAAA-MM-JJ-NN` (code 3) ; une construction refusée rend 2 sans envoi ; la clé se lit sous le nom `--variable-cle`
  (celle du projet Kimi dédié à la fumée, à budget de 1 USD).

Les six appels, dans l'ordre :
- f2 h2-max16 : **H2** — fin `length`, `completion_tokens` ≤ 16 réflexion comprise, champ de réflexion rendu (lequel) ;
- f1 sain-court : modèle servi, une tentative, usage lisible, détail ≤ `completion_tokens`, H3 ;
- f3 h3-table (≈ 10 ko) et f4 h3-table-longue (≈ 29 ko) : **H3** — `prompt_tokens` ≤ octets + 256 ;
- f5 h4-coupure (délai total de 4 s) : **H4** — échec compté à la réserve ; facture de la console ≤ réserve ;
- f6 h1-repetition (texte de f3) : **H1** — facture ≤ usage aux prix gelés ; cache lu rapporté.
H1 et H4 ne se tranchent qu'au rapprochement avec la console (détail par requête, J+1) : jamais déclarées tenues ici.
Graines : `numpy.random.SeedSequence(20261122)` (R9), comme la v1 (mêmes textes, autre ordre).
Usage : GO_ID=GO-… python3 -I -B essai_fumee_kimi_v3.py --registre R.jsonl --journal J.jsonl [--amont URL] [--variable-cle NOM]
"""
import argparse
import hashlib
import json
import os
import re
import sys
import urllib.parse

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
DEVIS_V4 = os.environ.get("DOSSIER_DEVIS_V4") or os.path.join(
    "/home/user/controle-ia-travail", "docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4")
EMPREINTES_V4 = {"adaptateur_fournisseur_v1.py": "67704c1e42a0308a4f511ddc82e58666e6741b9b954f78072fd55a64c7eff1e4",
                 "garde_pilote_essaim_v2.py": "d41305918b53d3bfa8b55ace148fdde6cf22f25623bcae2806585d0a242e4b84",
                 "registre_depense_v1.py": "f689dff2fd85bfce62f4151e16e0f2234765f2718481463dcd67f7cc1b1fe361"}
for _nom, _sha in EMPREINTES_V4.items():
    with open(os.path.join(DEVIS_V4, _nom), "rb") as _f:
        if hashlib.sha256(_f.read()).hexdigest() != _sha:
            print(f"pièce v4 {_nom} d'empreinte différente : refus", file=sys.stderr)
            sys.exit(2)
for d in (DEVIS_V4, ICI):
    if d not in sys.path:
        sys.path.insert(0, d)
import adaptateur_fournisseur_v1 as A  # noqa: E402
import adaptateur_kimi_strict_v3 as AS  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import registre_depense_v1 as RG  # noqa: E402
import transport_kimi_reel_v3 as T  # noqa: E402

PLAFOND_MAX_USD = 1.0
GRAINE = 20261122
MOTIF_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")
APPEL_DE_COUPURE = "f5-h4-coupure"


def table(lignes, graine_fille):
    rng = np.random.default_rng(graine_fille)
    x = rng.normal(size=(lignes, 10))
    return "\n".join(",".join(f"{v:.3f}" for v in r) for r in x)


def plan_fumee():
    ss = np.random.SeedSequence(GRAINE).spawn(2)
    t8 = table(150, ss[0])
    t24 = table(450, ss[1])
    raisonner = ("Démontre pas à pas, en vérifiant chaque étape, que la somme des n premiers nombres impairs vaut n au carré, "
                 "puis donne trois exemples numériques et une seconde démonstration par récurrence.")
    tete = "Lignes z0,z1,z2,z3,z4,z5,z6,z7,g,y :\n"
    queue = "\nDonne seulement la moyenne de y à deux décimales."
    return [
        {"id": "f2-h2-max16", "texte": raisonner, "max_tokens": 16, "delai_total_s": 600, "vise": "H2"},
        {"id": "f1-sain-court", "texte": "Réponds seulement par le mot OK.", "max_tokens": 2000, "delai_total_s": 600, "vise": "contrat"},
        {"id": "f3-h3-table", "texte": tete + t8 + queue, "max_tokens": 2000, "delai_total_s": 600, "vise": "H3"},
        {"id": "f4-h3-table-longue", "texte": tete + t24 + queue, "max_tokens": 2000, "delai_total_s": 600, "vise": "H3"},
        {"id": APPEL_DE_COUPURE, "texte": raisonner + " Termine par une table de vérification de n = 1 à 40.", "max_tokens": 2000,
         "delai_total_s": 4, "vise": "H4"},
        {"id": "f6-h1-repetition", "texte": tete + t8 + queue, "max_tokens": 2000, "delai_total_s": 600, "vise": "H1"},
    ]


def empreinte_plan(plan):
    return hashlib.sha256(json.dumps(plan, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def parametres(plan, plafond, champs_max):
    return {"essai": "fumee-kimi-v3", "plan_sha256": empreinte_plan(plan), "prix_usd_par_million": list(GP.PRIX_GELES),
            "plafond_depense_usd": plafond, "modele": T.MODELE, "surcout_format": GP.SURCOUT_FORMAT, "champs_max": list(champs_max)}


def amont_local(amont):
    p = urllib.parse.urlsplit(amont)
    return p.scheme == "http" and p.hostname in T.HOTES_LOCAUX


def verifier(appel, octets, diag, usage_adapte, fin):
    bruts = diag.get("usage_brut") or []
    u = bruts[-1]["usage"] if bruts else None
    v = {"usage_lisible": usage_adapte is not None, "usage_refuse": diag.get("usage_refuse"), "nombre_d_usages": len(bruts)}
    if not isinstance(u, dict):
        return v
    p, c = u.get("prompt_tokens"), u.get("completion_tokens")
    det = (u.get("completion_tokens_details") or {}).get("reasoning_tokens") if isinstance(u.get("completion_tokens_details"), dict) else None
    hors = u.get("reasoning_tokens")
    v["modele_servi_egal"] = diag.get("modele_servi") == T.MODELE
    v["tentatives_1"] = diag.get("envois_mesures") == 1
    v["champ_reflexion_detail_present"] = det is not None
    v["champ_reflexion_premier_niveau_present"] = hors is not None
    v["sortie_le_max_tokens"] = isinstance(c, int) and c <= appel["max_tokens"]
    v["sortie_adaptee_le_max_tokens"] = usage_adapte is not None and usage_adapte["sortie"] <= appel["max_tokens"]
    v["detail_reflexion_le_completion"] = det is None or (isinstance(det, int) and isinstance(c, int) and det <= c)
    v["H3_entree_le_octets_plus_256"] = isinstance(p, int) and p <= octets + GP.SURCOUT_FORMAT
    v["octets_par_jeton_entree"] = round(octets / p, 3) if isinstance(p, int) and p > 0 else None
    if appel["vise"] == "H2":
        v["H2_fin_length"] = fin == "length"
        v["H2_tenue_sous_reserve_console"] = bool(v["H2_fin_length"] and v["sortie_adaptee_le_max_tokens"] and not hors
                                                  and v["champ_reflexion_detail_present"])
    return v


def courir(registre, journal, amont, plafond, environ=None, plan=None, variable_cle="KIMI_API_KEY",
           champs_max=("max_tokens", "max_completion_tokens")):
    env = os.environ if environ is None else environ
    if not (0 < plafond <= PLAFOND_MAX_USD):
        print(f"plafond {plafond} hors de ]0, {PLAFOND_MAX_USD}]", file=sys.stderr)
        return 2
    if not amont_local(amont) and not MOTIF_GO.fullmatch(env.get("GO_ID") or ""):
        print("amont réel sans GO_ID valide : refus, aucun envoi", file=sys.stderr)
        return 3
    if os.path.exists(registre) or os.path.exists(journal):
        print("registre ou journal déjà présent : un essai de fumée ne se rejoue pas sur le même registre", file=sys.stderr)
        return 2
    try:
        tr = T.TransportKimiReel(amont=amont, environ=env, effacer_variable=True, variable_cle=variable_cle, champs_max=champs_max)
        ad = AS.AdaptateurKimiStrict(tr)
    except A.ConfigurationRefusee as ex:
        print(f"construction refusée, aucun envoi : {ex}", file=sys.stderr)
        return 2
    plan = plan or plan_fumee()
    params = parametres(plan, plafond, champs_max)
    RG.creer(registre, params)
    reg = RG.Registre(registre, params)
    j = open(journal, "x", encoding="utf-8")

    def ecrire(**l):
        j.write(json.dumps(l, ensure_ascii=False, sort_keys=True, default=str) + "\n")
        j.flush()

    def arreter(code, id_, detail, depense):
        reg.ecrire(evenement="arret", code=code, detail=detail[:200], depense_usd=depense)
        ecrire(evenement="arret", code=code, id=id_, detail=detail[:200], depense_usd=round(depense, 6))
        return code

    depense, envois_total = 0.0, 0
    ecrire(evenement="debut", go=env.get("GO_ID"), amont=amont, plan_sha256=params["plan_sha256"], plafond_usd=plafond,
           transport=T.VERSION, champs_max=list(champs_max), ordre=[a["id"] for a in plan])
    try:
        for appel in plan:
            tr.regler_delais(min(600, appel["delai_total_s"]), appel["delai_total_s"])
            envois_debut = tr.envois
            octets = len(appel["texte"].encode("utf-8"))
            reserve = GP.cout(octets + GP.SURCOUT_FORMAT, appel["max_tokens"], GP.PRIX_GELES)
            if depense + reserve > plafond + 1e-12:
                return arreter(14, appel["id"], "réserve au-delà du plafond", depense)
            reg.ecrire(evenement="reserve", id=appel["id"], role="fumee", reserve_usd=reserve)
            ligne = {"evenement": "appel", "id": appel["id"], "vise": appel["vise"], "max_tokens": appel["max_tokens"],
                     "octets_texte": octets, "sha256_texte": hashlib.sha256(appel["texte"].encode()).hexdigest(),
                     "reserve_usd": round(reserve, 6)}
            code, motif, contenu, fin = 0, "", "", None
            try:
                rep = ad.appeler(appel, appel["texte"], appel["max_tokens"])
                usage, fin = rep.get("usage"), rep.get("fin")
                contenu = rep.get("texte") or ""
                if usage is None:
                    cout, issue = reserve, "compte_a_la_reserve"
                    motif = (tr.dernier_diagnostic or {}).get("usage_refuse") or "usage refusé"
                    reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=cout, abandon=True, motif=motif[:120])
                    code = 16
                else:
                    cout, issue = GP.cout(usage["entree"], usage["sortie"], GP.PRIX_GELES), "regle"
                    reg.ecrire(evenement="regle", id=appel["id"], cout_usd=cout, usage=usage)
                    if cout > reserve + 1e-12:
                        code, motif = 16, f"coût mesuré {cout:.6f} > réserve {reserve:.6f} (H2 ou H3 violée)"
                    elif usage["sortie"] > appel["max_tokens"]:
                        code, motif = 16, "sortie rendue au-delà de max_tokens"
                ligne.update(issue=issue, usage_adapte=usage)
            except A.ErreurFournisseur as ex:
                cout, issue, motif = reserve, "echec", str(ex)[:160]
                reg.ecrire(evenement="echec", id=appel["id"], cout_usd=cout, abandon=True, motif=motif[:120])
                if appel["id"] != APPEL_DE_COUPURE:
                    code = 13
                ligne.update(issue=issue)
            except Exception as ex:  # noqa: BLE001  (anomalie, refus, erreur fatale : réserve par envoi, arrêt)
                cout, issue = reserve * max(1, getattr(ex, "envois", 1)), "compte_a_la_reserve"
                motif = f"{type(ex).__name__}: {str(ex)[:160]}"
                reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=cout, abandon=True, motif=type(ex).__name__)
                code = 16 if isinstance(ex, A.AnomalieReponse) else 17
                ligne.update(issue=issue)
            depense += cout
            d = dict(tr.dernier_diagnostic or {})
            n_envois = tr.envois - envois_debut
            envois_total += n_envois
            ligne.update(motif=motif or None, cout_compte_usd=round(cout, 6), depense_usd=round(depense, 6), envois_mesures=n_envois,
                         diagnostic=d, verifications=verifier(appel, octets, d, ligne.get("usage_adapte"), fin),
                         contenu_octets=len(contenu.encode()), contenu_sha256=hashlib.sha256(contenu.encode()).hexdigest())
            ecrire(**ligne)
            if code:
                return arreter(code, appel["id"], motif, depense)
            if depense > plafond + 1e-12:
                return arreter(14, appel["id"], "dépense au-delà du plafond", depense)
        reg.ecrire(evenement="fin", depense_usd=depense)
        ecrire(evenement="fin", code=0, depense_usd=round(depense, 6), envois_total=envois_total, appels=len(plan),
               note="H1 et H4 : à rapprocher de la console (détail par requête, J+1), ligne par ligne (id_reponse, en_tetes_id)")
        return 0
    finally:
        tr.fermer()
        j.close()


def main(argv=None):
    a = argparse.ArgumentParser(description="essai de fumée Kimi v2, six appels")
    a.add_argument("--registre", required=True)
    a.add_argument("--journal", required=True)
    a.add_argument("--amont", default=T.AMONT_DEFAUT)
    a.add_argument("--plafond-usd", type=float, default=PLAFOND_MAX_USD)
    a.add_argument("--variable-cle", default="KIMI_API_KEY")
    a.add_argument("--champs-max", default="max_tokens,max_completion_tokens")
    x = a.parse_args(argv)
    return courir(x.registre, x.journal, x.amont, x.plafond_usd, variable_cle=x.variable_cle,
                  champs_max=tuple(c for c in x.champs_max.split(",") if c))


if __name__ == "__main__":
    sys.exit(main())
