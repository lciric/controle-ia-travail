#!/usr/bin/env python3
"""Commande externe Gemini **par lot** (« Batch API ») pour l'orchestrateur du pôle — version 1. Pièce neutre, réutilisable.

Écrite le 18 novembre 2026 par la session de relance des organismes discrets, sur la décision de la session mère (07:29Z,
R-3241) : la lignée Carbon passe par le mode par lot à budget de pensée élevé (en appel synchrone, le modèle reste muet au-delà
de la coupure à 300 s des connexions muettes de ces conteneurs ; un lot a rendu en 430 s, épreuve du 18 novembre). Elle servira
aussi d'autres courses de l'organisme. **Aucune clé ici** : elle parle au relais Gemini v4 local (`relais_gemini_v4.py`), qui
tient la clé, la liste blanche des modèles, et ne relève que les lots qu'il a créés.

Contrat (celui de `commande_argon_v3e.py` pour `AdaptateurCommandeExterne`) : consigne sur l'entrée standard (UTF-8) ;
environnement minimal du noyau : `PLAFOND_SESSION_USD` (plafond de la session), `ROLE_POLE` (dans `--roles`),
`MODELE_DEMANDE_POLE` (s'il est posé, il doit être `--modele`, sinon code 2, rien envoyé) ; **la dernière ligne de la sortie
standard est toujours un objet JSON** `{"texte", "cout_usd", …}`, coût fini et strictement positif.

Déroulé :
1. compte exact de l'entrée par `countTokens` (gratuit) ; entrée gardée = ⌈max(compte, caractères / `--caracteres-par-jeton`)
   × (1 + `--marge-entree`)⌉ ;
2. **garde avant envoi** : pire cas = entrée gardée × prix d'entrée + (`maxOutputTokens` + `--provision-pensee-jetons`) × prix
   de sortie ≤ plafond de session, au **prix plein** (la remise du lot n'est pas comptée dans la garde : borne haute) ;
   `maxOutputTokens` = min(`--max-sortie-jetons`, ce que le reste du plafond paie) ; sous `--sortie-min-jetons` : code 4,
   rien envoyé ;
3. création d'un lot d'**une seule requête** (corps `generateContent` ordinaire, `thinkingConfig.thinkingBudget` =
   provision) ; puis relevé de l'état toutes les `--intervalle-s` secondes ;
4. fin : `BATCH_STATE_SUCCEEDED` → lecture de la réponse ; tout autre état final → code 3 ; au-delà de `--delai-s` → le lot
   est **annulé** et la commande rend le code 6 ;
5. lecture : modèle servi (`modelVersion`) égal au modèle demandé (ou suivi d'un suffixe de date -AAAAMMJJ), sinon code 5 ;
   `finishReason` `STOP` exigé (`MAX_TOKENS` : code 5, sortie tronquée) ; texte = parties non « pensée » ; coût =
   (entrée × prix d'entrée + (sortie + pensée) × prix de sortie) × `--facteur-lot` (1 par défaut : prix plein, borne haute).

Coût rendu sur un échec : 1e-6 si rien n'a été envoyé ; **pire cas** dès qu'un lot a été créé (usage inconnu).
`modele_servi` n'est écrit dans la ligne **que s'il est connu** (une ligne d'erreur ne porte pas de `modele_servi` nul : la
barrière du modèle servi de l'orchestrateur la lirait comme un refus).

Codes : 0 conforme ; 2 réglage ou entrée refusés (rien envoyé) ; 3 relais, amont ou lot en échec ; 4 pire cas au-dessus du
plafond (rien envoyé) ; 5 réponse non conforme ; 6 délai dépassé (lot annulé).

Bibliothèque standard seulement. Essais : `test_commande_gemini_lot_v1.py`.
"""
import argparse, json, math, os, re, sys, time, urllib.error, urllib.request

VERSION = "commande-gemini-lot-v1"
CLE_FACTICE = "factice-relais"
ETATS_FINIS = ("BATCH_STATE_SUCCEEDED", "BATCH_STATE_FAILED", "BATCH_STATE_CANCELLED", "BATCH_STATE_EXPIRED",
               "JOB_STATE_SUCCEEDED", "JOB_STATE_FAILED", "JOB_STATE_CANCELLED", "JOB_STATE_EXPIRED")


class Erreur(Exception):
    def __init__(self, code, motif, envoye=False, **extra):
        super().__init__(motif)
        self.code, self.motif, self.envoye, self.extra = code, motif, envoye, extra


def analyseur():
    a = argparse.ArgumentParser(prog="commande_gemini_lot_v1")
    a.add_argument("--modele", required=True)
    a.add_argument("--url-base", default="http://127.0.0.1:8792/v1beta")
    a.add_argument("--prix-entree", type=float, required=True, help="USD par million de jetons d'entrée (prix plein)")
    a.add_argument("--prix-sortie", type=float, required=True, help="USD par million de jetons de sortie (prix plein)")
    a.add_argument("--facteur-lot", type=float, default=1.0, help="facteur appliqué au coût rendu (1 : prix plein, borne haute)")
    a.add_argument("--max-sortie-jetons", type=int, default=32768)
    a.add_argument("--sortie-min-jetons", type=int, default=4096)
    a.add_argument("--provision-pensee-jetons", type=int, default=8192)
    a.add_argument("--caracteres-par-jeton", type=float, default=3.0)
    a.add_argument("--marge-entree", type=float, default=0.05)
    a.add_argument("--intervalle-s", type=float, default=30.0)
    a.add_argument("--delai-s", type=float, default=3300.0)
    a.add_argument("--delai-requete-s", type=float, default=120.0)
    a.add_argument("--roles", default="proposeur_ideation,juge_ideation")
    return a


def modele_conforme(demande, servi):
    return isinstance(servi, str) and (servi == demande or re.fullmatch(re.escape(demande) + r"-\d{8}", servi) is not None)


def requete(ouvreur, methode, url, corps, delai):
    d = json.dumps(corps).encode("utf-8") if corps is not None else (b"" if methode == "POST" else None)
    req = urllib.request.Request(url, data=d, method=methode,
                                 headers={"x-goog-api-key": CLE_FACTICE, "Content-Type": "application/json"})
    with ouvreur.open(req, timeout=delai) as r:
        return json.loads(r.read() or b"{}")


def lire_resultat(fin, modele):
    """(texte, fin, modèle servi, usage) d'un lot fini avec succès ; lève Erreur sinon."""
    reps = (((fin.get("response") or {}).get("inlinedResponses") or {}).get("inlinedResponses")) or \
           ((((fin.get("metadata") or {}).get("output") or {}).get("inlinedResponses") or {}).get("inlinedResponses"))
    if not isinstance(reps, list) or len(reps) != 1 or not isinstance(reps[0], dict):
        raise Erreur(5, "lot fini sans exactement une réponse en ligne", envoye=True)
    if "error" in reps[0]:
        raise Erreur(3, "la requête du lot a échoué : " + str(reps[0]["error"])[:300], envoye=True)
    rep = reps[0].get("response")
    if not isinstance(rep, dict):
        raise Erreur(5, "réponse du lot illisible", envoye=True)
    servi = rep.get("modelVersion")
    if not modele_conforme(modele, servi):
        raise Erreur(5, f"modèle servi {servi!r} ≠ modèle demandé {modele!r}", envoye=True, modele_servi=servi)
    usage = rep.get("usageMetadata")
    if not isinstance(usage, dict) or not isinstance(usage.get("promptTokenCount"), int):
        raise Erreur(5, "usage absent de la réponse du lot", envoye=True, modele_servi=servi)
    cands = rep.get("candidates") or []
    if not cands or not isinstance(cands[0], dict):
        raise Erreur(5, "aucun candidat dans la réponse", envoye=True, modele_servi=servi)
    c = cands[0]
    fin_raison = c.get("finishReason")
    parts = (c.get("content") or {}).get("parts") or []
    if any(isinstance(p, dict) and ("functionCall" in p or "executableCode" in p) for p in parts):
        raise Erreur(5, "appel de fonction ou code dans la réponse alors qu'aucun outil n'est déclaré", envoye=True, modele_servi=servi)
    texte = "".join(p.get("text", "") for p in parts if isinstance(p, dict) and not p.get("thought"))
    if fin_raison != "STOP":
        raise Erreur(5, f"fin {fin_raison!r} (STOP exigé ; MAX_TOKENS : sortie tronquée)", envoye=True, modele_servi=servi, usage=usage)
    if not texte.strip():
        raise Erreur(5, "réponse vide", envoye=True, modele_servi=servi, usage=usage)
    return texte, fin_raison, servi, usage


def executer(args, consigne, environ, ouvreur, dormir=time.sleep, horloge=time.time):
    etat = {"pire_cas": 1e-6, "envoye": False, "lot": None}
    debut = horloge()
    try:
        for nom, v in (("--prix-entree", args.prix_entree), ("--prix-sortie", args.prix_sortie), ("--facteur-lot", args.facteur_lot)):
            if not (isinstance(v, float) and math.isfinite(v) and v > 0):
                raise Erreur(2, f"{nom} : réel fini strictement positif exigé")
        roles = [x for x in args.roles.split(",") if x]
        if environ.get("ROLE_POLE") not in roles:
            raise Erreur(2, f"ROLE_POLE {environ.get('ROLE_POLE')!r} hors de {roles}")
        demande = environ.get("MODELE_DEMANDE_POLE")
        if demande and demande != args.modele:
            raise Erreur(2, f"MODELE_DEMANDE_POLE {demande!r} ≠ --modele {args.modele!r} : rien envoyé")
        try:
            plafond = float(environ.get("PLAFOND_SESSION_USD", ""))
            assert math.isfinite(plafond) and plafond > 0
        except (ValueError, AssertionError):
            raise Erreur(2, "PLAFOND_SESSION_USD absent ou invalide") from None
        if not consigne.strip():
            raise Erreur(2, "consigne vide")
        pe, ps = args.prix_entree / 1e6, args.prix_sortie / 1e6
        contenus = [{"role": "user", "parts": [{"text": consigne}]}]
        base = args.url_base.rstrip("/")
        try:
            compte = requete(ouvreur, "POST", f"{base}/models/{args.modele}:countTokens", {"contents": contenus},
                             args.delai_requete_s).get("totalTokens")
        except (urllib.error.URLError, OSError, ValueError) as e:
            raise Erreur(3, f"countTokens : {type(e).__name__} : {e}") from None
        if not isinstance(compte, int) or compte <= 0:
            raise Erreur(5, f"countTokens : totalTokens invalide ({compte!r})")
        entree = math.ceil(max(compte, len(consigne) / args.caracteres_par_jeton) * (1 + args.marge_entree))
        reste = (plafond - entree * pe) / ps - args.provision_pensee_jetons
        sortie = int(min(args.max_sortie_jetons, math.floor(reste)))
        if sortie < args.sortie_min_jetons:
            raise Erreur(4, f"pire cas au-dessus du plafond {plafond} USD (entrée gardée {entree}, provision de pensée "
                            f"{args.provision_pensee_jetons}, sortie possible {sortie} < {args.sortie_min_jetons}) : rien envoyé")
        etat["pire_cas"] = entree * pe + (sortie + args.provision_pensee_jetons) * ps
        corps = {"batch": {"display_name": f"{VERSION}-{environ.get('ROLE_POLE')}", "input_config": {"requests": {"requests": [
            {"request": {"contents": contenus, "generationConfig": {
                "maxOutputTokens": sortie, "thinkingConfig": {"thinkingBudget": args.provision_pensee_jetons}}},
             "metadata": {"key": "requete-1"}}]}}}}
        etat["envoye"] = True
        try:
            cree = requete(ouvreur, "POST", f"{base}/models/{args.modele}:batchGenerateContent", corps, args.delai_requete_s)
        except (urllib.error.URLError, OSError, ValueError) as e:
            raise Erreur(3, f"création du lot : {type(e).__name__} : {e}", envoye=True) from None
        nom = cree.get("name") or (cree.get("metadata") or {}).get("name")
        if not isinstance(nom, str) or not re.fullmatch(r"batches/[A-Za-z0-9_-]+", nom):
            raise Erreur(3, "création du lot : nom absent ou invalide", envoye=True)
        etat["lot"] = nom
        while True:
            if horloge() - debut > args.delai_s:
                try:
                    requete(ouvreur, "POST", f"{base}/{nom}:cancel", None, args.delai_requete_s)
                except (urllib.error.URLError, OSError, ValueError):
                    pass
                raise Erreur(6, f"délai de {args.delai_s} s dépassé : lot {nom} annulé", envoye=True)
            dormir(args.intervalle_s)
            try:
                fin = requete(ouvreur, "GET", f"{base}/{nom}", None, args.delai_requete_s)
            except (urllib.error.URLError, OSError, ValueError):
                continue  # un relevé manqué n'arrête pas le lot ; le délai global borne l'attente
            etat_lot = (fin.get("metadata") or {}).get("state") or fin.get("state")
            if fin.get("done") or etat_lot in ETATS_FINIS:
                break
        if etat_lot not in ("BATCH_STATE_SUCCEEDED", "JOB_STATE_SUCCEEDED"):
            raise Erreur(3, f"lot fini dans l'état {etat_lot!r}", envoye=True)
        texte, fin_raison, servi, usage = lire_resultat(fin, args.modele)
        sortie_lue = int(usage.get("candidatesTokenCount") or 0) + int(usage.get("thoughtsTokenCount") or 0)
        cout = (int(usage["promptTokenCount"]) * pe + sortie_lue * ps) * args.facteur_lot
        return 0, {"texte": texte, "cout_usd": max(cout, 1e-6), "modele_servi": servi, "modele_demande": args.modele,
                   "fin": fin_raison, "usage": usage, "lot": nom, "duree_s": round(horloge() - debut, 1),
                   "version": VERSION, "prix": {"entree": args.prix_entree, "sortie": args.prix_sortie, "facteur_lot": args.facteur_lot}}
    except Exception as brute:  # noqa: BLE001 — toute exception, nommée ou non, donne une ligne au bon coût
        e = brute if isinstance(brute, Erreur) else Erreur(3, f"{type(brute).__name__} : {brute}"[:300], envoye=etat["envoye"])
        ligne = {"texte": "", "cout_usd": max(etat["pire_cas"], 1e-6) if (e.envoye or etat["envoye"]) else 1e-6,
                 "erreur": f"{VERSION} : {e.motif}", "modele_demande": args.modele, "lot": etat["lot"],
                 "duree_s": round(horloge() - debut, 1), "version": VERSION, "cout_origine": "pire_cas" if (e.envoye or etat["envoye"]) else "plancher"}
        if isinstance(e.extra.get("modele_servi"), str):
            ligne["modele_servi"] = e.extra["modele_servi"]
        if isinstance(e.extra.get("usage"), dict):
            ligne["usage"] = e.extra["usage"]
        return e.code, ligne


def principal(argv=None, environ=None, entree=None, ouvreur=None, dormir=time.sleep, horloge=time.time):
    environ = os.environ if environ is None else environ
    try:
        args = analyseur().parse_args(argv)
    except SystemExit:
        print(json.dumps({"texte": "", "cout_usd": 1e-6, "erreur": f"{VERSION} : arguments invalides"}))
        return 2
    try:
        consigne = (entree if entree is not None else sys.stdin.buffer.read()).decode("utf-8")
    except UnicodeDecodeError:
        print(json.dumps({"texte": "", "cout_usd": 1e-6, "erreur": f"{VERSION} : consigne non UTF-8"}))
        return 2
    ouvreur = ouvreur or urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        code, ligne = executer(args, consigne, environ, ouvreur, dormir, horloge)
    except Exception as e:  # noqa: BLE001 — jamais de sortie sans ligne JSON
        code, ligne = 3, {"texte": "", "cout_usd": 1e-6, "erreur": f"{VERSION} : {type(e).__name__}"}
    if code != 0:
        print(f"{VERSION} : {ligne.get('erreur')}", file=sys.stderr)
    print(json.dumps(ligne, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(principal())
