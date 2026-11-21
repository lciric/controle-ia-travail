"""Véhicule NA-1, lot 4 — relevé de ce que l'outil des clés Claude envoie quand aucun texte système n'est donné
(`releve_sans_systeme_na_v1`).

Lettre : conception du véhicule v5 (`1b7f6822…`), § 2.3 (« ce que l'outil envoie quand aucun texte système n'est donné
n'est pas lisible dans le code ; il est relevé au faux fournisseur, derrière le vrai relais, dès le lot 4 et avant
l'écriture de l'additif » ; mère, 07:46Z, mot 5 : déclaré comme transport octet pour octet, ou refusé ; une chaîne vide
explicite est essayée d'abord), § 6.2 (adaptateur sans texte système : cas sain et artefact), § 7 (lot 4) ; mandat du lot 4,
point 3 : le jeu derrière le vrai relais n'est pas au développeur ; il demande un mot de la mère.

Trois sous-commandes :

- `direct --sortie DOSSIER` : lance le faux fournisseur dans ce processus, sur `127.0.0.1`, joue les scénarios avec
  l'adaptateur pointé **directement sur lui** (aucun relais), et écrit le relevé. C'est le jeu du développeur.
- `servir-faux --port P --journal FICHIER --duree-s S [--mode normale]` : sert le faux fournisseur, en gardant chaque
  requête dans un journal neuf, et s'arrête de lui-même au bout de S secondes. Pour le jeu derrière le vrai relais : la
  mère lance ce faux fournisseur, puis le relais avec ce faux fournisseur pour amont et une clé factice, puis :
- `relever --url-relais URL --journal-faux FICHIER --sortie DOSSIER [--scenarios normaux]` : joue les scénarios contre
  le relais et lit, dans le journal du faux fournisseur, ce qui y est arrivé. Une issue autre que normale ne se demande au
  faux fournisseur qu'en mode `direct`.

Le programme s'isole lui-même : environnement minimal (aucune variable de clé, aucun mandataire réseau, `NO_PROXY` sur la
boucle locale, trafic non essentiel de l'outil coupé), maison et configuration de l'outil dans `DOSSIER/maison` (jamais
sous la maison de l'utilisateur). L'identifiant de modèle n'est écrit nulle part dans le relevé : sa valeur est remplacée,
seule l'égalité au modèle demandé est dite.

Scénarios : la consigne d'essai, inerte, envoyée par l'adaptateur neuf sous ses deux formes (`chaine_vide`, `absent`) et
pour ses deux rôles ; l'artefact, l'adaptateur d'origine, dont le texte système doit être reçu ; en mode `direct` seulement,
les quatre issues du faux fournisseur (classifieur, coupée, crédit, accès), pour voir ce que l'adaptateur neuf rend et
conserve. Usage : `python -I -B releve_sans_systeme_na_v1.py direct --sortie DOSSIER` (interpréteur qui porte le kit).
"""

if __name__ == "__main__" and not __package__:
    import os as _os
    import sys as _sys
    _ICI = _os.path.dirname(_os.path.abspath(__file__))
    _sys.path[:] = [p for p in _sys.path if _os.path.abspath(p or _os.curdir) != _ICI]
    _sys.path.insert(0, _os.path.dirname(_ICI))

import argparse
import hashlib
import json
import os
import sys
import time

VERSION = "releve-sans-systeme-na-v1"
CONSIGNE_INERTE = ("Consigne inerte du relevé : elle ne pose aucune question et n'attend rien.\n"
                   "Deuxième ligne, accentuée : « é, à, ç ».\n")
MODELE_ECRIT = "<modèle demandé>"
SCENARIOS_NORMAUX = (
    ("neuf-chaine-vide-proposeur", "neuf", "chaine_vide", "proposeur_ideation", "normale"),
    ("neuf-chaine-vide-juge", "neuf", "chaine_vide", "juge_ideation", "normale"),
    ("neuf-absent-proposeur", "neuf", "absent", "proposeur_ideation", "normale"),
    ("neuf-absent-juge", "neuf", "absent", "juge_ideation", "normale"),
    ("artefact-adaptateur-d-origine-proposeur", "origine", None, "proposeur_ideation", "normale"),
)
SCENARIOS_ISSUES = tuple((f"neuf-chaine-vide-proposeur-issue-{m}", "neuf", "chaine_vide", "proposeur_ideation", m)
                         for m in ("classifieur", "coupee", "credit", "acces"))
VARIABLES_GARDEES = ("PATH", "LANG", "LC_ALL")
CLES_SCALAIRES = ("max_tokens", "stream", "temperature", "top_p", "top_k")


def _sha(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def isoler(racine):
    """Environnement minimal du processus (l'outil en hérite) : aucune clé, aucun mandataire, maison à part."""
    maison = os.path.join(racine, "maison")
    tmp = os.path.join(racine, "tmp")
    os.makedirs(os.path.join(maison, "config-outil"), exist_ok=False)
    os.makedirs(tmp, exist_ok=False)
    garde = {k: os.environ[k] for k in VARIABLES_GARDEES if k in os.environ}
    os.environ.clear()
    os.environ.update(garde)
    os.environ.setdefault("LANG", "C.UTF-8")
    os.environ.update({"HOME": maison, "TMPDIR": tmp, "CLAUDE_CONFIG_DIR": os.path.join(maison, "config-outil"),
                       "NO_PROXY": "127.0.0.1,localhost", "no_proxy": "127.0.0.1,localhost",
                       "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1", "DISABLE_TELEMETRY": "1",
                       "DISABLE_ERROR_REPORTING": "1", "DISABLE_AUTOUPDATER": "1"})
    return {"variables": sorted(os.environ)}


def _blocs(contenu):
    if contenu is None or contenu == "" or contenu == []:
        return []
    if isinstance(contenu, str):
        return [{"type": "text", "text": contenu}]
    if isinstance(contenu, list):
        return [b if isinstance(b, dict) else {"type": type(b).__name__} for b in contenu]
    return [{"type": type(contenu).__name__}]


RACINE_ECRITE = "<dossier du relevé>"
_RACINES = []  # le dossier du relevé, posé par `jouer_scenarios`


def masquer(texte, modele):
    """L'identifiant du modèle demandé et le chemin du dossier du relevé, remplacés dans un texte relevé ; rend (texte,
    nombre de remplacements de l'identifiant)."""
    if not isinstance(texte, str):
        return texte, 0
    for racine in _RACINES:
        texte = texte.replace(racine, RACINE_ECRITE)
    if not modele:
        return texte, 0
    return texte.replace(modele, MODELE_ECRIT), texte.count(modele)


def _bloc(b, consigne, modele):
    texte = b.get("text") if isinstance(b.get("text"), str) else None
    rendu = {"type": b.get("type"), "autres_cles": sorted(set(b) - {"type", "text"})}
    if texte is not None:
        ecrit, n = masquer(texte, modele)
        rendu.update({"texte": ecrit, "identifiant_de_modele_masque": n, "sha256_avant_masque": _sha(texte),
                      "taille_octets_avant_masque": len(texte.encode("utf-8")),
                      "egal_a_la_consigne": texte == consigne,
                      "egal_a_la_consigne_sans_blanc_final": texte != consigne and texte == consigne.rstrip()})
    return rendu


def analyser_corps(corps, consigne, modele):
    """Ce que porte le corps d'une requête de messages : textes système, blocs des messages, autres champs ; le modèle
    n'est dit que par son égalité au modèle demandé."""
    if not isinstance(corps, dict):
        return {"lisible": False}
    systeme = [_bloc(b, consigne, modele) for b in _blocs(corps.get("system"))]
    messages = [{"role": m.get("role") if isinstance(m, dict) else None,
                 "blocs": [_bloc(b, consigne, modele) for b in _blocs(m.get("content") if isinstance(m, dict) else None)]}
                for m in (corps.get("messages") if isinstance(corps.get("messages"), list) else [])]
    autres = {}
    for k, v in sorted(corps.items()):
        if k in ("system", "messages", "model"):
            continue
        if k == "tools":
            autres[k] = {"nombre": len(v) if isinstance(v, list) else None,
                         "noms": [t.get("name") for t in v if isinstance(t, dict)] if isinstance(v, list) else None}
        elif k == "metadata":
            autres[k] = {"cles": sorted(v) if isinstance(v, dict) else None}
        elif k in CLES_SCALAIRES or not isinstance(v, (dict, list, str)):
            autres[k] = v
        else:
            autres[k] = {"json": json.dumps(v, ensure_ascii=False, sort_keys=True)[:2000]}
    textes_systeme = [b["texte"] for b in systeme if b.get("texte")]
    ajouts = [b["texte"] for m in messages for b in m["blocs"]
              if b.get("texte") is not None and not b["egal_a_la_consigne"] and not b["egal_a_la_consigne_sans_blanc_final"]]
    trouvee = [b for m in messages for b in m["blocs"] if b.get("egal_a_la_consigne")]
    trouvee_sans_blanc = [b for m in messages for b in m["blocs"] if b.get("egal_a_la_consigne_sans_blanc_final")]
    return {"lisible": True, "cles": sorted(corps), "modele": MODELE_ECRIT if "model" in corps else None,
            "modele_egal_au_demande": corps.get("model") == modele, "systeme": systeme, "messages": messages,
            "autres_champs": autres, "texte_systeme_recu": bool(textes_systeme), "textes_ajoutes_aux_messages": ajouts,
            "consigne": ("retrouvée à l'octet" if trouvee else "retrouvée sans son blanc final" if trouvee_sans_blanc
                         else "non retrouvée")}


def _requete(r, consigne, modele):
    rendu = {"rang": r["rang"], "methode": r["methode"], "chemin": r["chemin"], "corps_taille": r["corps_taille"],
             "corps_sha256": r["corps_sha256"], "mode": r["mode"],
             "en_tetes": {k: v for k, v in sorted(r["en_tetes"].items()) if k not in ("host", "content-length")}}
    if r["methode"] == "POST" and r["chemin"].split("?", 1)[0].endswith("/v1/messages"):
        rendu["analyse"] = analyser_corps(r["corps"], consigne, modele)
    return rendu


def _resultat(res, modele):
    refus = res.refus if isinstance(res.refus, dict) else None
    servi = refus.get("modele_servi") if refus else None
    return {"statut": res.statut, "erreur": None if res.erreur is None else masquer(str(res.erreur)[:400], modele)[0],
            "refus_evenement": refus.get("evenement") if refus else None,
            "refus_modele_servi": masquer(servi, modele)[0] if isinstance(servi, str) else None,
            "cout_declare_usd": res.cout_declare_usd,
            "cout_inconnu": bool(res.cout_inconnu), "modele_servi_egal_au_demande": None,
            "texte_brut_sha256": None if res.texte_brut is None else _sha(res.texte_brut)}


def jouer_scenarios(url, lire_requetes, racine, scenarios, changer_mode=None, delai_s=180):
    """Joue chaque scénario par l'adaptateur réel du kit, pointé sur `url` ; rend leurs relevés."""
    from pole import adaptateurs as ad
    from pole.adaptateur_claude_na_v1 import AdaptateurClaudeNA
    from pole.faux_fournisseur_na_v1 import TEXTE_INERTE
    modele = ad.MODELES_REELS_PERMIS[0]
    _RACINES[:] = [os.path.realpath(racine), racine] if os.path.realpath(racine) != racine else [racine]
    reponses = os.path.join(racine, "reponses-brutes")
    os.makedirs(reponses, exist_ok=False)
    rendus = []
    for nom, quel, forme, role, mode in scenarios:
        if changer_mode is not None:
            changer_mode(mode)
        elif mode != "normale":
            raise SystemExit("une issue autre que normale ne se demande au faux fournisseur qu'en mode direct")
        dossier = os.path.join(racine, "course", "sessions", nom)
        os.makedirs(dossier, exist_ok=False)
        if quel == "neuf":
            adaptateur = AdaptateurClaudeNA(url, reponses, forme_sans_systeme=forme, arme=True, delai_s=delai_s)
        else:
            adaptateur = ad.AdaptateurClaudeSDK(url, arme=True, delai_s=delai_s)
        avant = len(lire_requetes())
        debut = time.monotonic()
        try:
            res = adaptateur.lancer(role, CONSIGNE_INERTE, dossier, 0.5, 1, modele=modele)
            resultat = _resultat(res, modele)
            resultat["modele_servi_egal_au_demande"] = res.modele_servi == modele if res.modele_servi else None
            resultat["texte_rendu_egal_au_texte_du_faux"] = res.texte_brut == TEXTE_INERTE
        except Exception as e:  # noqa: BLE001 — l'échec est relevé tel quel, par son type
            resultat = {"exception": type(e).__name__, "message": masquer(str(e)[:400], modele)[0]}
        duree = round(time.monotonic() - debut, 3)
        time.sleep(0.2)
        recues = lire_requetes()[avant:]
        brutes = sorted(f for f in os.listdir(reponses) if f.startswith("reponse-brute-" + nom) and f.endswith(".json"))
        conservees = []
        for f in brutes:
            with open(os.path.join(reponses, f), "rb") as fh:
                octets = fh.read()
            objet = json.loads(octets.decode("utf-8"))
            conservees.append({"fichier": f, "sha256": hashlib.sha256(octets).hexdigest(), "statut": objet.get("statut"),
                               "texte_brut_sha256": None if objet.get("texte_brut") is None else _sha(objet["texte_brut"])})
        analyses = [_requete(r, CONSIGNE_INERTE, modele) for r in recues]
        messages = [a["analyse"] for a in analyses if "analyse" in a]
        rendus.append({
            "scenario": nom, "adaptateur": quel, "forme_sans_systeme": forme, "role_kit": role, "issue_demandee": mode,
            "duree_s": duree, "resultat": resultat, "reponses_brutes_conservees": conservees,
            "requetes_recues": len(recues), "requetes_de_messages": len(messages),
            "constat": {"texte_systeme_recu": any(m.get("texte_systeme_recu") for m in messages),
                        "textes_ajoutes_aux_messages": sorted({t for m in messages for t in m.get("textes_ajoutes_aux_messages", [])}),
                        "consigne": sorted({m.get("consigne") for m in messages if m.get("lisible")}),
                        "texte_systeme_d_origine_recu": any(
                            ad.CONSIGNES_SYSTEME[role] in (b.get("texte") or "") for m in messages for b in m.get("systeme", []))},
            "requetes": analyses})
    return rendus


def ecrire_releve(sortie, rendu):
    chemin = os.path.join(sortie, "releve-sans-systeme-na-v1.json")
    octets = (json.dumps(rendu, ensure_ascii=False, sort_keys=True, indent=1) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(octets)
    with open(chemin + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{hashlib.sha256(octets).hexdigest()}  {os.path.basename(chemin)}\n")
    return chemin


def _bilan(scenarios):
    neufs = [s for s in scenarios if s["adaptateur"] == "neuf" and s["issue_demandee"] == "normale"]
    par_forme = {}
    for forme in ("chaine_vide", "absent"):
        ss = [s for s in neufs if s["forme_sans_systeme"] == forme]
        par_forme[forme] = {
            "scenarios": len(ss),
            "requetes_de_messages": sum(s["requetes_de_messages"] for s in ss),
            "aucun_texte_systeme_recu": bool(ss) and all(s["requetes_de_messages"] and not s["constat"]["texte_systeme_recu"]
                                                         for s in ss),
            "aucun_texte_ajoute_aux_messages": bool(ss) and all(not s["constat"]["textes_ajoutes_aux_messages"] for s in ss),
            "consigne": sorted({c for s in ss for c in s["constat"]["consigne"]})}
    artefact = [s for s in scenarios if s["adaptateur"] == "origine"]
    return {"par_forme": par_forme,
            "artefact_texte_systeme_d_origine_recu": bool(artefact) and all(s["constat"]["texte_systeme_d_origine_recu"]
                                                                           for s in artefact),
            "lecture": "constat seulement ; ce qui part se déclare à l'additif comme transport, octet pour octet, ou se "
                       "refuse : décision de la mère (07:46Z, mot 5)"}


def _versions():
    rendu = {"python": sys.version.split()[0]}
    try:
        import claude_agent_sdk
        rendu["kit"] = getattr(claude_agent_sdk, "__version__", "inconnue")
    except ImportError:
        rendu["kit"] = "absent"
    return rendu


def principal(argv=None):
    p = argparse.ArgumentParser(prog="releve_sans_systeme_na_v1")
    sous = p.add_subparsers(dest="commande", required=True)
    d = sous.add_parser("direct")
    d.add_argument("--sortie", required=True)
    d.add_argument("--sans-issues", action="store_true", help="ne joue que les scénarios normaux")
    s = sous.add_parser("servir-faux")
    s.add_argument("--port", type=int, required=True)
    s.add_argument("--journal", required=True)
    s.add_argument("--duree-s", type=float, required=True)
    s.add_argument("--mode", default="normale")
    r = sous.add_parser("relever")
    r.add_argument("--url-relais", required=True)
    r.add_argument("--journal-faux", required=True)
    r.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    from pole.faux_fournisseur_na_v1 import FauxFournisseur, lire_journal
    if a.commande == "servir-faux":
        faux = FauxFournisseur(port=a.port, journal=os.path.abspath(a.journal), mode=a.mode)
        print(json.dumps({"faux_fournisseur": faux.url, "journal": os.path.abspath(a.journal), "duree_s": a.duree_s}),
              flush=True)
        faux.servir_jusqu_a(a.duree_s)
        return 0
    sortie = os.path.abspath(a.sortie)
    if os.path.exists(sortie):
        print("dossier de sortie existant : on n'écrase jamais (R12)", file=sys.stderr)
        return 2
    os.makedirs(sortie)
    isolement = isoler(sortie)
    if a.commande == "direct":
        faux = FauxFournisseur().demarrer()
        try:
            scenarios = SCENARIOS_NORMAUX + (() if a.sans_issues else SCENARIOS_ISSUES)
            rendus = jouer_scenarios(faux.url, lambda: list(faux.requetes), sortie, scenarios, faux.changer_mode)
        finally:
            faux.fermer()
        lieu = {"mode": "direct", "faux_fournisseur": "127.0.0.1, dans ce processus", "relais": "aucun"}
    else:
        from pole.relais import valider_url_relais
        valider_url_relais(a.url_relais)
        journal = os.path.abspath(a.journal_faux)
        rendus = jouer_scenarios(a.url_relais, lambda: lire_journal(journal), sortie, SCENARIOS_NORMAUX)
        lieu = {"mode": "relever", "relais": "adresse locale donnée", "journal_du_faux": os.path.basename(journal)}
    rendu = {"version": VERSION, "lieu": lieu, "versions": _versions(), "isolement": isolement,
             "consigne_inerte": {"texte": CONSIGNE_INERTE, "sha256": _sha(CONSIGNE_INERTE),
                                 "taille_octets": len(CONSIGNE_INERTE.encode("utf-8"))},
             "scenarios": rendus, "bilan": _bilan(rendus)}
    chemin = ecrire_releve(sortie, rendu)
    print(json.dumps({"releve": chemin, "bilan": rendu["bilan"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(principal())
