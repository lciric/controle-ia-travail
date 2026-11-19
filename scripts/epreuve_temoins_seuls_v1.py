"""Épreuve des témoins seuls devant le juge de l'organisme d'idéation (organismes discrets) — version 1.

Écrite le 18 novembre 2026 par la session de relance, pour l'addendum des témoins (règle écrite d'avance : si le juge échoue
un seul témoin v2, aucune course ; aucune retouche des témoins sans addendum neuf). **Un seul appel**, joué une seule fois.

Ce que fait le script, avec les fonctions mêmes de l'orchestrateur épinglé (`pole/ideation_v2.py`, commit a41b7b50) :
1. valide chaque témoin au gabarit (`valider_fiche_ideation`, comme `charger_temoins`), vérifie les quatre classes ;
2. anonymise les quatre témoins pour le juge `opus-juge` avec la graine des courses (`anonymiser`) ;
3. bâtit la consigne du juge (`consigne_juge`) avec la question v3 et les faits v3 comme pièce du juge (caviardés comme
   `lire_pieces`), `citations` et `moisson` tels que la course les posait (vérifié par l'option `--verifier-gabarit` contre
   le début, jusqu'au titre « ## Les fiches », de la consigne scellée d'une course : égalité seulement, rien n'est affiché) ;
4. un appel `POST /v1/messages` au relais Claude local (modèle `claude-opus-5-5`, aucun outil), jeton factice ;
5. lit le bloc de notes (`extraire_bloc_json`, `valider_notes`), puis la règle gelée des témoins (`lecture_temoins`) ;
6. écrit, scellés, la consigne, la réponse brute, les notes et la lecture dans un dossier neuf (jamais écrasé).

Écart déclaré à la course : le juge y était une session de l'adaptateur Claude de l'orchestrateur (bac à sable, invite du kit)
et voyait les témoins mêlés aux fiches ; ici, un appel direct de l'interface de messages, quatre fiches. L'épreuve vérifie la
grille sur les témoins, pas la session.

Codes : 0 épreuve faite, les quatre témoins tenus ; 4 épreuve faite, au moins un témoin manqué (aucune course) ; 2 refus avant
appel ; 3 appel ou lecture en échec (épreuve non faite ; ne se rejoue que sur addendum).

Usage : python3 -I -B scripts/epreuve_temoins_seuls_v1.py SORTIE [--url-relais http://127.0.0.1:8787] [--max-tokens 16000]
        [--verifier-gabarit CONSIGNE_DE_COURSE]
"""
import argparse, hashlib, json, os, sys, urllib.request

ORCH = "/home/user/lciric/ideation-organism/orchestrator"
DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = os.path.join(DEPOT, "docs/notes/organismes-discrets-v1/organisme-ideation-v1")
PIECES = {"temoins": ("temoins-organisme-discrets-v3.json", "611c50a267c28ab4bd29785c85d489616045a8f495a3582294e641dbd7159705"),
          "question": ("question-v3.md", "2f7acf36a1dbdbc53a03a0f775327c773e0152323b04f83b4441db80d6b01dae"),
          "faits": ("faits-v3.md", "5e2e9dd85a88e9e07da806a3c7657f62c6c6343f11ed6de8a1d507a0b397962f")}
GRAINE = 2026111808
ETIQUETTE_JUGE = "opus-juge"
MODELE = "claude-opus-5-5"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def lire(nom):
    chemin, attendue = PIECES[nom]
    b = open(os.path.join(N, chemin), "rb").read()
    if sha(b) != attendue:
        raise SystemExit(f"refus : {chemin} n'a pas l'empreinte attendue")
    return chemin, b


def preparer(citations, moisson):
    sys.path.insert(0, ORCH)
    import pole.ideation_v2 as idn
    from pole.caviardage import caviarder
    _, bt = lire("temoins")
    brut = json.loads(bt)
    temoins = []
    for i, t in enumerate(brut["temoins"], 1):
        f = idn.valider_fiche_ideation(t["fiche"], idn.AUTEUR_TEMOIN, i, passe=0, moisson=False)
        f["temoin"] = {"attendu": t["attendu"], "note_max": dict(t.get("note_max") or {}), "jumeau_de": t.get("jumeau_de"),
                       "classe": t["classe"]}
        temoins.append(f)
    if {t["temoin"]["classe"] for t in temoins} != set(idn.CLASSES_TEMOIN):
        raise SystemExit("refus : classes de témoins incomplètes")
    anonymes, cle = idn.anonymiser(temoins, GRAINE, ETIQUETTE_JUGE)
    cq, bq = lire("question")
    cf, bf = lire("faits")
    texte_f, _ = caviarder(bf.decode("utf-8", "replace"))
    pieces = [(cf, texte_f, sha(bf))]
    consigne = idn.consigne_juge(anonymes, bq.decode("utf-8"), pieces, citations=citations, moisson=moisson)
    return idn, temoins, anonymes, cle, consigne


def ecrire(dossier, nom, contenu):
    """Écrit un fichier et son compagnon d'empreinte ; octets, texte ou objet JSON."""
    if isinstance(contenu, bytes):
        data = contenu
    elif isinstance(contenu, str):
        data = contenu.encode("utf-8")
    else:
        data = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    p = os.path.join(dossier, nom)
    with open(p, "wb") as f:
        f.write(data)
    with open(p + ".sha256", "w") as f:
        f.write(sha(data) + "  " + nom + "\n")


def main(argv=None):
    a = argparse.ArgumentParser()
    a.add_argument("sortie")
    a.add_argument("--url-relais", default="http://127.0.0.1:8787")
    a.add_argument("--max-tokens", type=int, default=16000)
    a.add_argument("--citations", action="store_true")
    a.add_argument("--moisson", action="store_true")
    a.add_argument("--verifier-gabarit", help="consigne scellée d'une course : compare le début (avant la première fiche)")
    a.add_argument("--a-sec", action="store_true", help="tout sauf l'appel")
    args = a.parse_args(argv)
    if os.path.exists(args.sortie):
        print(json.dumps({"refus": "dossier de sortie existant (R12)"})); return 2
    idn, temoins, anonymes, cle, consigne = preparer(args.citations, args.moisson)
    if args.verifier_gabarit:
        course = open(args.verifier_gabarit, encoding="utf-8").read()
        marque = "## Les fiches"  # borne du gabarit : tout ce qui précède les fiches, sans fiche
        i, j = consigne.find(marque), course.find(marque)
        egal = i > 0 and j > 0 and consigne[:i] == course[:j]
        print(json.dumps({"gabarit_egal_a_la_course": egal, "citations": args.citations, "moisson": args.moisson}))
        return 0 if egal else 2
    os.makedirs(args.sortie)
    ecrire(args.sortie, "consigne.md", consigne)
    ecrire(args.sortie, "cle-anonymisation.json", cle)
    if args.a_sec:
        print(json.dumps({"a_sec": True, "consigne_sha256": sha(consigne.encode("utf-8")), "caracteres": len(consigne)})); return 0
    from pole.relais import JETON_FACTICE
    corps = json.dumps({"model": MODELE, "max_tokens": args.max_tokens,
                        "messages": [{"role": "user", "content": consigne}]}).encode("utf-8")
    req = urllib.request.Request(args.url_relais + "/v1/messages", data=corps, method="POST",
                                 headers={"x-api-key": JETON_FACTICE, "anthropic-version": "2023-06-01",
                                          "content-type": "application/json"})
    try:
        ouvreur = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with ouvreur.open(req, timeout=1800) as r:
            brut = r.read()
    except Exception as e:  # noqa: BLE001 — l'épreuve n'est pas faite ; nommée
        ecrire(args.sortie, "echec.json", {"erreur": f"{type(e).__name__}: {e}"[:500]})
        print(json.dumps({"code": 3, "erreur": type(e).__name__})); return 3
    ecrire(args.sortie, "reponse-brute.json", brut)
    try:
        rep = json.loads(brut)
        if rep.get("model") != MODELE and not str(rep.get("model", "")).startswith(MODELE):
            raise ValueError(f"modèle servi {rep.get('model')!r} ≠ {MODELE}")
        texte = "".join(b.get("text", "") for b in rep.get("content", []) if b.get("type") == "text")
        from pole.outils import extraire_bloc_json
        bloc = extraire_bloc_json(texte, "notes")
        notes, doublons = idn.valider_notes(bloc, set(cle))
    except Exception as e:  # noqa: BLE001
        ecrire(args.sortie, "echec.json", {"erreur": f"{type(e).__name__}: {e}"[:500]})
        print(json.dumps({"code": 3, "erreur": f"lecture : {type(e).__name__}"})); return 3
    par_auteur = {ETIQUETTE_JUGE: {cle[k]: v for k, v in notes.items()}}
    lecture = idn.lecture_temoins(par_auteur, temoins, {ETIQUETTE_JUGE: doublons}, {ETIQUETTE_JUGE: cle})
    ecrire(args.sortie, "lecture-temoins.json", {"lecture": lecture, "usage": rep.get("usage"), "modele_servi": rep.get("model")})
    code = 0 if lecture["temoins_ok"] else 4
    print(json.dumps({"code": code, "temoins_ok": lecture["temoins_ok"], "usage": rep.get("usage")}))
    return code


if __name__ == "__main__":
    sys.exit(main())
