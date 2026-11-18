"""Épreuve des témoins seuls devant le juge de l'organisme d'idéation (organismes discrets) — version 3.

Copie corrigée de `epreuve_temoins_seuls_v2.py` (inchangé, R12, jamais joué) après la contre-lecture de l'addendum v2
(`contre-lecture-addendum-temoins-v2.md`, `1db4f419…`) :
- témoins **v5** ; empreinte de la consigne épinglée de nouveau ;
- **avant de créer son dossier**, le script vérifie tout ce qui ferait refuser l'appel sans envoi (code 2, la tentative n'est
  pas consommée) : aucun nom de clé dans l'environnement, modèle réel permis, kit d'agents importable, bac à sable actif,
  et **l'état du relais Claude** : plafond 0,5 USD, **réserve par appel 0,2 USD** (le kit envoie deux requêtes presque
  simultanées par session : à 0,4 de réserve, la seconde serait refusée), modèles permis exactement Opus 5.5, aucune dépense
  ni aucun appel avant l'épreuve (constat 1) ;
- le coût lu est celui du résultat réel de l'adaptateur (`cout_declare_usd`, `cout_inconnu`) (constats 2 et 4) ;
- une interruption pendant l'appel (`KeyboardInterrupt`, `SystemExit`) est écrite dans `issue.json` et classée code 3
  (constat 6) ;
- la réponse écrite est le texte caviardé (`texte_final`) ; la clé d'anonymisation est écrite après l'appel ;
- **une seule tentative, toutes versions confondues** : refus si un dossier `runs/epreuve-temoins-seuls-v*` existe.

## Texte de la version 2 (pour mémoire)

Épreuve des témoins seuls devant le juge de l'organisme d'idéation (organismes discrets) — version 2.

Écrite le 18 novembre 2026 par la session de relance. Copie corrigée de `epreuve_temoins_seuls_v1.py` (inchangé, R12),
après la contre-lecture de l'addendum (`contre-lecture-addendum-temoins-v1.md`, `ffee53ca…`, constats 2, 3, 4, 5, 8, 9, 15) :
- témoins **v4** (`temoins-organisme-discrets-v4.json`) ;
- **une seule épreuve, jamais rejouée** : dossier de sortie imposé (`runs/epreuve-temoins-seuls-v2/`), refus s'il existe,
  quelle qu'en soit l'issue (code 3 compris) ; aucun réglage libre au départ réel (ni modèle, ni jetons, ni relais) ;
- la consigne doit avoir l'empreinte inscrite ici (`CONSIGNE_ATTENDUE`) ; sinon refus avant tout appel ;
- **le juge est appelé comme dans les courses** : par l'adaptateur Claude de l'orchestrateur épinglé
  (`pole.adaptateurs.AdaptateurClaudeSDK.lancer("juge_ideation", …)`) — même consigne système, même effort (« medium »),
  même kit d'agents, même bac à sable vérifié (`etat_bac_a_sable_detaille`), même nombre de tours ; plafond de la session
  **0,5 USD** (`max_budget_usd`), en plus du plafond du relais Claude lancé à 0,5 ;
- refus et erreurs avant appel : code 2 (jamais 1).

Ce qui reste comme dans la v1 : consigne bâtie par `anonymiser` et `consigne_juge` (graine 2026111808, étiquette « opus-juge »,
question v3, faits v3 comme pièce du juge, `citations` et `moisson` faux : gabarit identique aux deux courses jusqu'au titre
« ## Les fiches ») ; lecture par `extraire_bloc_json`, `valider_notes`, `lecture_temoins`.

Écart déclaré à la course : quatre fiches (les témoins) au lieu de 14 à 16, sans fiche de proposeur, donc sans doublon possible.

Codes : 0 épreuve faite, quatre témoins tenus ; 4 épreuve faite, au moins un témoin manqué ; 3 épreuve tentée, appel ou
lecture en échec (dossier écrit ; aucune reprise sans addendum neuf) ; 2 refus avant tout appel (rien n'est parti).

Commande exacte (dossier courant = racine du dépôt ; relais Claude lancé avant sur 8787 avec `--plafond-usd 0.5
--modeles-permis claude-opus-5-5`) :

    env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=/root LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_seuls_v2.py

Options sans appel : `--a-sec` (écrit la consigne dans un dossier donné par `--dossier`, ailleurs que le dossier imposé) ;
`--verifier-gabarit CONSIGNE_DE_COURSE` (booléen seulement).
"""
import argparse, hashlib, json, os, sys

ORCH = "/home/user/lciric/ideation-organism/orchestrator"
DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = os.path.join(DEPOT, "docs/notes/organismes-discrets-v1/organisme-ideation-v1")
SORTIE = os.path.join(DEPOT, "runs/epreuve-temoins-seuls-v3")
RESERVE_RELAIS_USD = 0.2
PIECES = {"temoins": ("temoins-organisme-discrets-v5.json", "8bec42540e8f19f903db3d6f3d0fd121e0befb0c27fec79a5a3f91def51a9500"),
          "question": ("question-v3.md", "2f7acf36a1dbdbc53a03a0f775327c773e0152323b04f83b4441db80d6b01dae"),
          "faits": ("faits-v3.md", "5e2e9dd85a88e9e07da806a3c7657f62c6c6343f11ed6de8a1d507a0b397962f")}
CONSIGNE_ATTENDUE = "15e5b0d0dc522095751c1d3f9b43dc87dd5ab5d4141293dc538e198bd0c7d678"
GRAINE = 2026111808
ETIQUETTE_JUGE = "opus-juge"
MODELE = "claude-opus-5-5"
PLAFOND_SESSION_USD = 0.5
URL_RELAIS = "http://127.0.0.1:8787"


class Refus(Exception):
    pass


def sha(b):
    return hashlib.sha256(b).hexdigest()


def lire(nom):
    chemin, attendue = PIECES[nom]
    b = open(os.path.join(N, chemin), "rb").read()
    if sha(b) != attendue:
        raise Refus(f"{chemin} n'a pas l'empreinte attendue")
    return chemin, b


def preparer():
    if ORCH not in sys.path:
        sys.path.insert(0, ORCH)
    import pole.ideation_v2 as idn
    from pole.caviardage import caviarder
    brut = json.loads(lire("temoins")[1])
    temoins = []
    for i, t in enumerate(brut["temoins"], 1):
        f = idn.valider_fiche_ideation(t["fiche"], idn.AUTEUR_TEMOIN, i, passe=0, moisson=False)
        f["temoin"] = {"attendu": t["attendu"], "note_max": dict(t.get("note_max") or {}), "jumeau_de": t.get("jumeau_de"),
                       "classe": t["classe"]}
        temoins.append(f)
    if {t["temoin"]["classe"] for t in temoins} != set(idn.CLASSES_TEMOIN):
        raise Refus("classes de témoins incomplètes")
    anonymes, cle = idn.anonymiser(temoins, GRAINE, ETIQUETTE_JUGE)
    _, bq = lire("question")
    cf, bf = lire("faits")
    texte_f, _ = caviarder(bf.decode("utf-8", "replace"))
    consigne = idn.consigne_juge(anonymes, bq.decode("utf-8"), [(cf, texte_f, sha(bf))], citations=False, moisson=False)
    return idn, temoins, cle, consigne


def ecrire(dossier, nom, contenu):
    if isinstance(contenu, bytes):
        data = contenu
    elif isinstance(contenu, str):
        data = contenu.encode("utf-8")
    else:
        data = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True, default=str) + "\n").encode("utf-8")
    p = os.path.join(dossier, nom)
    with open(p, "wb") as f:
        f.write(data)
    with open(p + ".sha256", "w") as f:
        f.write(sha(data) + "  " + nom + "\n")


def juger(idn, temoins, cle, consigne, adaptateur, dossier_agent):
    """Un appel du juge par l'adaptateur ; rend (code, compte rendu). Aucune exception ne sort."""
    try:
        r = adaptateur.lancer("juge_ideation", consigne, dossier_agent, PLAFOND_SESSION_USD, idn.MAX_TOURS_IDEATION,
                              modele=MODELE)
    except BaseException as e:  # noqa: BLE001 — tentée et en échec, interruption comprise ; nommée, jamais muette
        return 3, {"erreur": f"lancement : {type(e).__name__}: {e}"[:500], "cout_usd": PLAFOND_SESSION_USD,
                   "cout_inconnu": True}
    rendu = {"statut": getattr(r, "statut", None), "cout_usd": getattr(r, "cout_declare_usd", None),
             "cout_inconnu": getattr(r, "cout_inconnu", None), "modele_servi": getattr(r, "modele_servi", None),
             "refus": getattr(r, "refus", None), "erreur": getattr(r, "erreur", None)}
    if rendu["statut"] != "ok" or rendu["refus"]:
        return 3, rendu
    if rendu["modele_servi"] is not None and not str(rendu["modele_servi"]).startswith(MODELE):
        return 3, dict(rendu, erreur=f"modèle servi {rendu['modele_servi']!r}")
    try:
        from pole.outils import extraire_bloc_json
        bloc = extraire_bloc_json(getattr(r, "texte_brut", None) or getattr(r, "texte_final", ""), "notes")
        notes, doublons = idn.valider_notes(bloc, set(cle))
    except Exception as e:  # noqa: BLE001
        return 3, dict(rendu, erreur=f"lecture : {type(e).__name__}: {e}"[:500])
    par_auteur = {ETIQUETTE_JUGE: {cle[k]: v for k, v in notes.items()}}
    lecture = idn.lecture_temoins(par_auteur, temoins, {ETIQUETTE_JUGE: doublons}, {ETIQUETTE_JUGE: cle})
    return (0 if lecture["temoins_ok"] else 4), dict(rendu, lecture=lecture, texte=getattr(r, "texte_final", None))


def etat_relais():
    import urllib.request
    o = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    return json.loads(o.open(URL_RELAIS + "/relais/etat", timeout=10).read())


def verifier_avant_envoi(lire_etat=etat_relais, environ=None):
    """Tout ce qui ferait refuser l'appel sans envoi : vérifié avant de créer le dossier (code 2)."""
    from pole.adaptateurs import importer_sdk, noms_de_cle_presents, verifier_modele_reel
    presents = noms_de_cle_presents(os.environ if environ is None else environ)
    if presents:
        raise Refus("noms de clé dans l'environnement : " + ", ".join(presents))
    verifier_modele_reel(MODELE)
    importer_sdk()
    try:
        e = lire_etat()
    except Exception as x:  # noqa: BLE001
        raise Refus(f"relais Claude illisible : {type(x).__name__}") from None
    attendu = {"plafond_usd": PLAFOND_SESSION_USD, "reserve_par_appel_usd": RESERVE_RELAIS_USD, "modeles_permis": [MODELE],
               "depense_usd": 0.0, "appels": 0}
    ecarts = {k: e.get(k) for k, v in attendu.items() if e.get(k) != v}
    if ecarts:
        raise Refus(f"relais Claude non conforme : {ecarts} (attendu {attendu})")
    return e


def adaptateur_reel(dossier_sortie):
    from pole.adaptateurs import AdaptateurClaudeSDK, etat_bac_a_sable_detaille
    etat = etat_bac_a_sable_detaille()
    if not etat["actif"]:
        raise Refus("bac à sable inactif : " + str(etat.get("motif")))
    if not etat["proc_neuf"] and os.geteuid() == 0:
        raise Refus("bac à sable sans /proc neuf sous root (CL31-15)")
    a = AdaptateurClaudeSDK(URL_RELAIS, arme=True, interdire_lecture=[dossier_sortie, DEPOT, os.path.expanduser("~")])
    a.bac_a_sable = etat
    return a


def main(argv=None, adaptateur=None, lire_etat=etat_relais, environ=None):
    a = argparse.ArgumentParser()
    a.add_argument("--a-sec", action="store_true")
    a.add_argument("--dossier", help="avec --a-sec seulement : dossier neuf où écrire la consigne")
    a.add_argument("--verifier-gabarit")
    args = a.parse_args(argv)
    try:
        idn, temoins, cle, consigne = preparer()
        h = sha(consigne.encode("utf-8"))
        if args.verifier_gabarit:
            course = open(args.verifier_gabarit, encoding="utf-8").read()
            m = "## Les fiches"
            i, j = consigne.find(m), course.find(m)
            egal = i > 0 and i == j and consigne[:i] == course[:j]
            print(json.dumps({"gabarit_egal_a_la_course": egal}))
            return 0 if egal else 2
        if args.a_sec:
            if not args.dossier or os.path.abspath(args.dossier) == SORTIE or os.path.exists(args.dossier):
                raise Refus("--a-sec exige --dossier neuf, autre que le dossier imposé")
            os.makedirs(args.dossier)
            ecrire(args.dossier, "consigne.md", consigne)
            print(json.dumps({"a_sec": True, "consigne_sha256": h, "caracteres": len(consigne)}))
            return 0
        if args.dossier:
            raise Refus("--dossier n'est admis qu'avec --a-sec")
        if h != CONSIGNE_ATTENDUE:
            raise Refus(f"consigne d'empreinte {h}, attendue {CONSIGNE_ATTENDUE}")
        import glob
        deja = sorted(glob.glob(os.path.join(os.path.dirname(SORTIE), "epreuve-temoins-seuls-v*")))
        if deja:
            raise Refus(f"épreuve déjà tentée ({', '.join(deja)}) : aucune reprise sans addendum neuf")
        etat_avant = verifier_avant_envoi(lire_etat, environ)
        if adaptateur is None:
            adaptateur = adaptateur_reel(SORTIE)
    except Refus as e:
        print(json.dumps({"code": 2, "refus": str(e)})); return 2
    except Exception as e:  # noqa: BLE001 — avant tout appel : refus
        print(json.dumps({"code": 2, "refus": f"{type(e).__name__}: {e}"[:400]})); return 2
    os.makedirs(SORTIE)
    agent = os.path.join(SORTIE, "agent"); os.makedirs(agent)
    ecrire(SORTIE, "consigne.md", consigne)
    ecrire(SORTIE, "etat-relais-avant.json", etat_avant)
    code, rendu = juger(idn, temoins, cle, consigne, adaptateur, agent)
    ecrire(SORTIE, "cle-anonymisation.json", cle)
    texte = rendu.pop("texte", None)
    if texte is not None:
        ecrire(SORTIE, "reponse-du-juge.md", texte)
    ecrire(SORTIE, "issue.json", dict(rendu, code=code, consigne_sha256=h))
    print(json.dumps({"code": code, "temoins_ok": (rendu.get("lecture") or {}).get("temoins_ok"), "cout_usd": rendu.get("cout_usd")}))
    return code


if __name__ == "__main__":
    sys.exit(main())
