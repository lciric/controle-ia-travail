#!/usr/bin/env python3
"""Essai de fumée du transport réel sur Kimi (H1 à H4 de `a-faire-avant-preenregistrement-pilote-v1.md`) — v1.
**Six appels, jamais plus, une seule fois** ; aucun envoi relancé. Chaîne réelle : `TransportKimiReel` →
`AdaptateurKimiStrict` (sur `AdaptateurChatCompletions`) → registre de dépense `registre_depense_v1` (neuf, écriture en tête, réserve scellée avant
chaque appel). Plafond du registre ≤ 1 USD. Vers un amont `https://` : refus sans `GO_ID` de la forme `GO-AAAA-MM-JJ-NN`
dans l'environnement (code 3). Vers le faux serveur local (`http://127.0.0.1:…`) : aucun GO requis (répétition à blanc).

Les six appels (`PLAN_FUMEE`) et ce que chacun vérifie :
- f1 sain-court (`max_tokens` 2000) : modèle servi = `kimi-k3.1-pro`, `tentatives` = 1, `usage` lisible, détail de
  réflexion ≤ `completion_tokens`, `completion_tokens` ≤ `max_tokens`, entrée ≤ octets + 256 (H3) ;
- f2 h2-max16 (`max_tokens` 16, invite qui pousse à réfléchir) : **H2** — fin `length`, `completion_tokens` ≤ 16,
  aucune réflexion rendue hors de ce compte (`reasoning_tokens` au premier niveau absent ou nul, détail ≤ 16) ;
- f3 h3-table (≈ 8 ko de lignes « z0,…,z7,g,y » à 3 décimales, forme de la case servie) : **H3** — `prompt_tokens`
  ≤ octets du texte + 256 ; rapport octets par jeton rapporté ;
- f4 h3-table-longue (≈ 24 ko, même forme) : **H3** à une taille de proposeur ;
- f5 h4-coupure (délai total côté client de 4 s sur une invite longue à raisonner) : **H4** — l'appel échoue
  (`ErreurFournisseur`) et il est compté à sa réserve ; à rapprocher de la console (facture de la requête coupée ≤ réserve) ;
- f6 h1-repetition (texte de f3 à l'identique) : **H1** — facture ≤ usage rendu aux prix gelés ; cache lu éventuel
  (`cached_tokens`) rapporté.
H1 et H4 ne se tranchent **qu'au rapprochement** du journal (identifiant de réponse, usage, coût compté) avec la console de
facturation du fournisseur, ligne par ligne : ce script ne les déclare jamais tenues.

Journal (JSON par ligne, neuf) : par appel, l'objet, les octets et l'empreinte sha256 du texte envoyé (jamais le texte),
la réserve, l'issue, l'usage (nombres), le modèle servi, la fin, l'identifiant de réponse, la durée, les vérifications ;
longueur et empreinte du contenu rendu (jamais le contenu). Aucune clé, aucune variable d'environnement.
Graines : `numpy.random.SeedSequence(20261122)` (R9). Usage :
    GO_ID=GO-… KIMI_API_KEY=… python3 -I -B essai_fumee_kimi_v1.py --registre R.jsonl --journal J.jsonl [--amont URL]
"""
import argparse
import hashlib
import json
import os
import re
import sys

import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
DEVIS_V4 = os.environ.get("DOSSIER_DEVIS_V4") or os.path.join(
    "/home/user/controle-ia-travail", "docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v4")
for d in (ICI, DEVIS_V4):
    if d not in sys.path:
        sys.path.insert(0, d)
import adaptateur_fournisseur_v1 as A  # noqa: E402
import adaptateur_kimi_strict_v1 as AS  # noqa: E402
import garde_pilote_essaim_v2 as GP  # noqa: E402
import registre_depense_v1 as RG  # noqa: E402
import transport_kimi_reel_v1 as T  # noqa: E402

PLAFOND_MAX_USD = 1.0
GRAINE = 20261122
MOTIF_GO = re.compile(r"GO-\d{4}-\d{2}-\d{2}-\d{2}")


def table(lignes, graine_fille):
    rng = np.random.default_rng(graine_fille)
    x = rng.normal(size=(lignes, 10))
    return "\n".join(",".join(f"{v:.3f}" for v in r) for r in x)


def plan_fumee():
    ss = np.random.SeedSequence(GRAINE).spawn(2)
    t8 = table(150, ss[0])     # ≈ 8 ko
    t24 = table(450, ss[1])    # ≈ 24 ko
    raisonner = ("Démontre pas à pas, en vérifiant chaque étape, que la somme des n premiers nombres impairs vaut n au carré, "
                 "puis donne trois exemples numériques et une seconde démonstration par récurrence.")
    return [
        {"id": "f1-sain-court", "texte": "Réponds seulement par le mot OK.", "max_tokens": 2000, "delai_total_s": 600, "vise": "contrat"},
        {"id": "f2-h2-max16", "texte": raisonner, "max_tokens": 16, "delai_total_s": 600, "vise": "H2"},
        {"id": "f3-h3-table", "texte": "Lignes z0,z1,z2,z3,z4,z5,z6,z7,g,y :\n" + t8 + "\nDonne seulement la moyenne de y à deux décimales.",
         "max_tokens": 2000, "delai_total_s": 600, "vise": "H3"},
        {"id": "f4-h3-table-longue", "texte": "Lignes z0,z1,z2,z3,z4,z5,z6,z7,g,y :\n" + t24 + "\nDonne seulement la moyenne de y à deux décimales.",
         "max_tokens": 2000, "delai_total_s": 600, "vise": "H3"},
        {"id": "f5-h4-coupure", "texte": raisonner + " Termine par une table de vérification de n = 1 à 40.", "max_tokens": 2000,
         "delai_total_s": 4, "vise": "H4"},
        {"id": "f6-h1-repetition", "texte": "Lignes z0,z1,z2,z3,z4,z5,z6,z7,g,y :\n" + t8 + "\nDonne seulement la moyenne de y à deux décimales.",
         "max_tokens": 2000, "delai_total_s": 600, "vise": "H1"},
    ]


def empreinte_plan(plan):
    return hashlib.sha256(json.dumps(plan, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def parametres(plan, plafond):
    return {"essai": "fumee-kimi-v1", "plan_sha256": empreinte_plan(plan), "prix_usd_par_million": list(GP.PRIX_GELES),
            "plafond_depense_usd": plafond, "modele": T.MODELE, "surcout_format": GP.SURCOUT_FORMAT}


def verifier(appel, octets, rep, usage_adapte):
    u = rep.get("usage") if isinstance(rep, dict) else None
    v = {}
    if not isinstance(u, dict):
        return {"usage_lisible": False}
    p, c = u.get("prompt_tokens"), u.get("completion_tokens")
    det = (u.get("completion_tokens_details") or {}).get("reasoning_tokens")
    hors = u.get("reasoning_tokens")
    v["usage_lisible"] = usage_adapte is not None and min(usage_adapte.values()) >= 0
    v["modele_servi_egal"] = rep.get("model") == T.MODELE
    v["tentatives_1"] = rep.get("tentatives") == 1
    v["sortie_le_max_tokens"] = isinstance(c, int) and c <= appel["max_tokens"]
    v["sortie_adaptee_le_max_tokens"] = usage_adapte is not None and usage_adapte["sortie"] <= appel["max_tokens"]
    v["detail_reflexion_le_completion"] = det is None or (isinstance(det, int) and isinstance(c, int) and det <= c)
    v["reflexion_hors_compte_nulle"] = not hors
    v["H3_entree_le_octets_plus_256"] = isinstance(p, int) and p <= octets + GP.SURCOUT_FORMAT
    v["octets_par_jeton_entree"] = round(octets / p, 3) if isinstance(p, int) and p > 0 else None
    v["cache_lu"] = (u.get("prompt_tokens_details") or {}).get("cached_tokens") or u.get("cached_tokens") or 0
    if appel["vise"] == "H2":
        v["H2_fin_length"] = (rep.get("choices") or [{}])[0].get("finish_reason") == "length"
        v["H2_tenue_sous_reserve_console"] = v["H2_fin_length"] and v["sortie_adaptee_le_max_tokens"] and v["reflexion_hors_compte_nulle"]
    return v


def courir(registre, journal, amont, plafond, environ=None, plan=None):
    env = os.environ if environ is None else environ
    if not (0 < plafond <= PLAFOND_MAX_USD):
        print(f"plafond {plafond} hors de ]0, {PLAFOND_MAX_USD}]", file=sys.stderr)
        return 2
    if not amont.startswith("http://127.0.0.1") and not MOTIF_GO.fullmatch(env.get("GO_ID") or ""):
        print("amont réel sans GO_ID valide : refus, aucun envoi", file=sys.stderr)
        return 3
    if os.path.exists(registre) or os.path.exists(journal):
        print("registre ou journal déjà présent : un essai de fumée ne se rejoue pas sur le même registre", file=sys.stderr)
        return 2
    plan = plan or plan_fumee()
    params = parametres(plan, plafond)
    RG.creer(registre, params)
    reg = RG.Registre(registre, params)
    j = open(journal, "x", encoding="utf-8")

    def ecrire(**l):
        j.write(json.dumps(l, ensure_ascii=False, sort_keys=True) + "\n")
        j.flush()

    depense, envois_avant, code = 0.0, 0, 0
    ecrire(evenement="debut", go=env.get("GO_ID"), amont=amont, plan_sha256=params["plan_sha256"], plafond_usd=plafond,
           transport=T.VERSION)
    tr = None
    try:
        tr = T.TransportKimiReel(amont=amont, environ=env, effacer_variable=True)  # clé lue une fois, retirée de l'environnement
        ad = AS.AdaptateurKimiStrict(tr)  # classe exacte du transport, empreinte du module, méthodes figées
        for appel in plan:
            tr.delai_total_s, tr.delai_silence_s = float(appel["delai_total_s"]), float(min(600, appel["delai_total_s"]))
            envois_debut = tr.envois
            if True:  # bloc d’un appel (un seul envoi, jamais relancé)
                octets = len(appel["texte"].encode("utf-8"))
                reserve = GP.cout(octets + GP.SURCOUT_FORMAT, appel["max_tokens"], GP.PRIX_GELES)
                if depense + reserve > plafond + 1e-12:
                    reg.ecrire(evenement="arret", code=14, detail=f"réserve de {appel['id']} au-delà du plafond", depense_usd=depense)
                    ecrire(evenement="arret", code=14, id=appel["id"], depense_usd=depense)
                    return 14
                reg.ecrire(evenement="reserve", id=appel["id"], role="fumee", reserve_usd=reserve)
                ligne = {"evenement": "appel", "id": appel["id"], "vise": appel["vise"], "max_tokens": appel["max_tokens"],
                         "octets_texte": octets, "sha256_texte": hashlib.sha256(appel["texte"].encode()).hexdigest(),
                         "reserve_usd": round(reserve, 6)}
                try:
                    rep = ad.appeler(appel, appel["texte"], appel["max_tokens"])
                    usage = rep.get("usage")
                    rep_brute = tr.derniere_reponse or {}
                    if usage is None or min(usage.values()) < 0:
                        cout, issue = reserve, "compte_a_la_reserve"
                        reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=cout, abandon=True, motif="usage anormal")
                    else:
                        cout, issue = GP.cout(usage["entree"], usage["sortie"], GP.PRIX_GELES), "regle"
                        reg.ecrire(evenement="regle", id=appel["id"], cout_usd=cout, usage=usage)
                    ligne.update(issue=issue, usage_adapte=usage, verifications=verifier(appel, octets, rep_brute, usage))
                except A.ErreurFournisseur as ex:
                    rep_brute = {}
                    cout, issue = reserve, "echec"
                    reg.ecrire(evenement="echec", id=appel["id"], cout_usd=cout, abandon=True, motif=str(ex)[:120])
                    ligne.update(issue=issue, motif=str(ex)[:120])
                except Exception as ex:  # noqa: BLE001  (anomalie, refus, erreur fatale : réserve, arrêt)
                    rep_brute = {}
                    cout, issue = reserve * getattr(ex, "envois", 1), "compte_a_la_reserve"
                    reg.ecrire(evenement="compte_a_la_reserve", id=appel["id"], cout_usd=cout, abandon=True, motif=type(ex).__name__)
                    ligne.update(issue=issue, motif=f"{type(ex).__name__}: {str(ex)[:120]}")
                    code = 16 if isinstance(ex, A.AnomalieReponse) else 17
                depense += cout
                d = tr.dernier_diagnostic or {}
                contenu = ((rep_brute.get("choices") or [{}])[0].get("message") or {}).get("content", "") if rep_brute else ""
                ligne.update(cout_compte_usd=round(cout, 6), depense_usd=round(depense, 6), envois_du_transport=tr.envois - envois_debut,
                             id_reponse=d.get("id_reponse"), modele_servi=d.get("modele_servi"), fin=d.get("fin"),
                             duree_s=d.get("duree_s"), statut=d.get("statut"), usage_numerique=d.get("usage_numerique"),
                             excedent_total_tokens=d.get("excedent_total_tokens"),
                             contenu_octets=len(contenu.encode()), contenu_sha256=hashlib.sha256(contenu.encode()).hexdigest())
                envois_avant += tr.envois - envois_debut
                ecrire(**ligne)
                if code:
                    reg.ecrire(evenement="arret", code=code, detail=ligne.get("motif", "")[:200], depense_usd=depense)
                    ecrire(evenement="arret", code=code, id=appel["id"], depense_usd=round(depense, 6))
                    return code
        reg.ecrire(evenement="fin", depense_usd=depense)
        ecrire(evenement="fin", code=0, depense_usd=round(depense, 6), envois_total=envois_avant, appels=len(plan),
               note="H1 et H4 : à rapprocher de la console de facturation, ligne par ligne (id_reponse)")
        return 0
    finally:
        if tr is not None:
            tr.fermer()
        j.close()


def main(argv=None):
    a = argparse.ArgumentParser(description="essai de fumée Kimi, six appels")
    a.add_argument("--registre", required=True)
    a.add_argument("--journal", required=True)
    a.add_argument("--amont", default=T.AMONT_DEFAUT)
    a.add_argument("--plafond-usd", type=float, default=PLAFOND_MAX_USD)
    x = a.parse_args(argv)
    return courir(x.registre, x.journal, x.amont, x.plafond_usd)


if __name__ == "__main__":
    sys.exit(main())
