"""Essais de `generer_temoins_ligne_3_v3.py` (pytest) — v3.

v3 (décisions de la mère, 15:20Z) : historique git du dépôt (dépôt git d'essai temporaire) sain et artefact ; seule la forme
réelle du fichier des cartes (identifiants de treize caractères) ; ligne de portée de la pièce du (4), confrontée au repli ;
journal existant sans manifeste refusé sans trace ; pièce du (4) lue une seule fois.

v2 : essais de la v1 rejoués, adaptés au journal en constantes (voie d'essai `LieuDuJournal.essai`) et à la pièce du (4)
à verdict ; plus : recréation du journal refusée, suppression du journal → refus avant ouverture, aucun chemin libre ; pièce
« Non conforme » et empreinte d'un autre programme refusées ; `meta` à toute profondeur ; forme réelle du fichier des cartes ;
aucune trace brute à la ligne de commande ; C1 ; contenus identiques refusés et fragments communs rapportés (M5) ; service
réel du clone exercé sur la banque factice, sans réseau ni clé (M6) ; dossiers temporaires du système (C2).

Règle R5 : chaque garde de la liste d'arrêt qui touche la banque, la garde de recouvrement et l'audit, sur un cas sain et sur
un artefact, dont les sept artefacts de la garde. **Cartes factices seulement** : chaque essai écrit son propre faux fichier
de cartes dans un dossier temporaire et passe son empreinte au code par la voie d'essai explicite
(`EntreeCartes.essai`) ; aucun essai ne nomme, n'ouvre ni ne touche le fichier des cartes. Les fragments sont ceux du
fichier factice `fragments-exemple-essais-v3.json`. Racine des essais 2026111930 seulement ; les racines 2026111934 et
2026111937 ne sont jamais dérivées ici.
"""
import hashlib
import json
import subprocess
import tempfile
from fractions import Fraction
from pathlib import Path

import pytest

import generer_temoins_ligne_3_v3 as G

ICI = Path(__file__).resolve().parent
FRAGMENTS = ICI / "fragments-exemple-essais-v3.json"
PROGRAMME = ICI / "generer_temoins_ligne_3_v3.py"
GIT_ESSAI = ["git", "-c", "user.name=essai", "-c", "user.email=essai@exemple.invalid", "-c", "commit.gpgsign=false"]

SECRET_CARTE = "zorglub quantique violette mange sept nuages bleus ce matin sur la colline"
SECRET_META = "pamplemousse orbital chante douze fois sous le pont des soupirs ce soir"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_f(p) -> str:
    return sha(Path(p).read_bytes())


def _interdites():
    conf = json.loads(G.lire_par_empreinte(G.DEPOT / G.CONFIGURATION[0], G.CONFIGURATION[1], "configuration").decode("utf-8"))
    return list(conf["etiquettes_interdites_fixes"])


INTERDITES = _interdites()


@pytest.fixture
def dossier():
    return Path(tempfile.mkdtemp(prefix="essais-generateur-v2-"))      # v2, C2 : dossier temporaire du système


@pytest.fixture(scope="session")
def composition():
    ctx = G.Contexte("essais")
    fr, _h = G.charger_fragments(FRAGMENTS, sha_f(FRAGMENTS), INTERDITES)
    banque, journal = G.composer(fr, ctx, G.ITEMS, INTERDITES)
    return {"fr": fr, "banque": banque, "journal": journal, "ctx": ctx}


def objet_fragments():
    return json.loads(FRAGMENTS.read_text(encoding="utf-8"))


# ------------------------------------------------------------------------------------------------------------------------------
# cartes factices
# ------------------------------------------------------------------------------------------------------------------------------


def texte_de_carte(k: int) -> str:
    return (f"Carte simulée {k} pour la garde, vocabulaire inventé et distinct. Elle parle de comètes en carton, "
            f"de lanternes rouges et de rivières sèches, variante {k}.")


def cartes_factices(n=94, ids=None, secret=True):
    cartes = []
    for k in range(n):
        ident = ids[k] if ids else f"c{k:012x}"                      # treize caractères, comme la forme réelle
        contenu = {"titre": f"Carte inventée {k}", "texte": texte_de_carte(k)}
        if secret and k == 3:
            contenu["texte"] += " " + SECRET_CARTE + "."
        cartes.append({"id": ident, "contenu": contenu, "meta": {"note": SECRET_META}})
    return cartes


def forme_reelle(cartes) -> dict:
    """La seule forme admise en v3 : {identifiant : {contenu, empreinte, meta}}."""
    return {c["id"]: {"contenu": c["contenu"], "empreinte": sha(json.dumps(c["contenu"], sort_keys=True).encode("utf-8")),
                      "meta": c["meta"]} for c in cartes}


def ecrire_cartes(dossier: Path, cartes, nom="cartes-factices.json") -> Path:
    p = dossier / nom
    p.write_text(json.dumps(forme_reelle(cartes), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    return p


def ecrire_banque(dossier: Path, banque, nom="banque.json") -> Path:
    p = dossier / nom
    p.write_text(json.dumps({"temoins": banque}, ensure_ascii=False), encoding="utf-8")
    return p


def lieu(dossier: Path):
    return G.LieuDuJournal.essai(dossier / "journal", depot=dossier)


def initialiser_depot(d: Path) -> None:
    """Dépôt git d'essai temporaire, une validation vide (historique qui ne connaît pas le manifeste)."""
    if not (d / ".git").exists():
        subprocess.run(GIT_ESSAI + ["init", "-q", str(d)], check=True, capture_output=True)
        subprocess.run(GIT_ESSAI + ["-C", str(d), "commit", "-q", "--allow-empty", "-m", "essai"], check=True,
                       capture_output=True)


def preparer_journal(dossier: Path) -> Path:
    initialiser_depot(dossier)
    (dossier / "journal").mkdir(exist_ok=True)
    G.creer_journal_rejeux(lieu(dossier))
    return lieu(dossier).journal


def piece(dossier: Path, nom: str, texte: str) -> Path:
    p = dossier / nom
    p.write_text(texte, encoding="utf-8")
    return p


def texte_controle(verdict="**Conforme.**", programme=None, portee="Portée : garde entière") -> str:
    return ("# Contrôle factice de la condition (4), pour les essais\n\n## Verdict\n\n" + verdict + "\n\n"
            + (portee + "\n\n" if portee else "") + f"Programme contrôlé : `{programme or sha_f(PROGRAMME)}`.\n")


class Lancer:
    def __init__(self, dossier: Path, capfd):
        self.dossier, self.capfd, self.n = dossier, capfd, 0
        self.controle = piece(dossier, "controle-4.md", texte_controle())
        self.controle_repli = piece(dossier, "controle-4-repli.md", texte_controle(portee="Portée : repli seul"))

    def __call__(self, banque_p, cartes_p, *, empreinte=None, compte=94, extra=(), provoquer=None,
                 v2=None, controle=True, controle_piece=None, lieu_journal=None):
        self.n += 1
        lj = lieu_journal or lieu(self.dossier)
        sortie = self.dossier / f"sortie-garde-{self.n}"
        entree = G.EntreeCartes.essai(cartes_p, empreinte or sha_f(cartes_p), compte, provoquer)
        argv = ["garde", "--banque", str(banque_p), "--sortie", str(sortie)]
        c = controle_piece or (self.controle_repli if "--repli" in extra else self.controle)
        if controle:
            argv += ["--controle-4", str(c), "--empreinte-controle-4", sha_f(c)]
        argv += list(extra)
        code = G.principal(argv, entree_cartes=entree, entree_v2=v2, lieu_journal=lj)
        out, err = self.capfd.readouterr()
        return {"code": code, "rapport": json.loads(out), "out": out, "err": err, "sortie": sortie, "entree": entree,
                "journal": lj.journal}


@pytest.fixture
def lancer(dossier, capfd):
    return Lancer(dossier, capfd)


def sorties_ecrites(res) -> str:
    """Tout ce que la garde a écrit ou affiché : rapport, manifeste, journal des rejeux, sortie standard et d'erreur."""
    morceaux = [res["out"], res["err"]]
    if res["sortie"].exists():
        for f in sorted(res["sortie"].iterdir()):
            morceaux.append(f.read_text(encoding="utf-8"))
    if Path(res["journal"]).exists():
        morceaux.append(Path(res["journal"]).read_text(encoding="utf-8"))
    return "\n".join(morceaux)


def assert_rien_des_cartes(res, cartes):
    tout = sorties_ecrites(res)
    n = G.normaliser(tout)
    assert G.normaliser(SECRET_CARTE) not in n
    assert G.normaliser(SECRET_META) not in n
    assert "comètes en carton" not in tout and "comètes en carton" not in n
    ref = set()
    for c in cartes:
        for s in G.textes_de(c):
            ref |= G.bardeaux(s)
    assert not (G.bardeaux(tout) & ref), "un bardeau de carte factice est sorti de la garde"


def assert_rapport_ferme(r):
    assert set(r) <= set(G.CHAMPS_RAPPORT_GARDE)
    assert r["decision"] in G.DECISIONS_GARDE


# ------------------------------------------------------------------------------------------------------------------------------
# graines
# ------------------------------------------------------------------------------------------------------------------------------


def test_racine_des_essais_derivable():
    ctx = G.Contexte("essais")
    a = ctx.rng("partage").integers(1 << 30)
    b = G.Contexte("essais").rng("partage").integers(1 << 30)
    assert a == b and ctx.derivations[0]["racine"] == G.RACINE_ESSAIS


def test_racines_decisives_refusees_sans_autorisation(dossier):
    with pytest.raises(G.RefusGraine):
        G.Contexte("decisif")
    faux = piece(dossier, "additif-factice.md", "additif factice\n")
    with pytest.raises(G.RefusGraine):
        G.Contexte("decisif", G.Autorisation(faux, "0" * 64))
    with pytest.raises(G.RefusGraine):
        G.Contexte("decisif", G.Autorisation(dossier / "absent.md", sha_f(faux)))
    with pytest.raises(G.RefusGraine):
        G.Contexte("autre")


def test_autorisation_juste_acceptee_sans_derivation(dossier):
    faux = piece(dossier, "additif-factice.md", "additif factice\n")
    G.verifier_autorisation(G.Autorisation(faux, sha_f(faux)))      # aucune racine dérivée ici


def test_racines_hors_programme_et_tables_etrangeres_refusees():
    ctx = G.Contexte("essais")
    for racine in (2026111931, 2026111932, 2026111933, 2026111935, 2026111936, 12345):
        with pytest.raises(G.RefusGraine):
            ctx._parent(racine, G.CLES_COMPOSITION, "partage")
    with pytest.raises(G.RefusGraine):
        ctx._parent(G.RACINE_ESSAIS, G.CLES_COMPOSITION, "tache-inconnue")
    with pytest.raises(G.RefusGraine):
        ctx._parent(G.RACINE_PLIS_AUDIT, G.CLES_COMPOSITION, "partage")
    assert ctx.derivations == []


# ------------------------------------------------------------------------------------------------------------------------------
# fragments : fichier de données à part, schéma vérifié au chargement
# ------------------------------------------------------------------------------------------------------------------------------


def test_fragments_exemple_sains():
    fr, h = G.charger_fragments(FRAGMENTS, sha_f(FRAGMENTS), INTERDITES)
    assert h == sha_f(FRAGMENTS)
    assert set(fr["conformes"]) == set(G.CATEGORIES) and len(fr["fautifs"]) >= 15


def test_fragments_empreinte_fausse_refusee():
    with pytest.raises(G.Refus):
        G.charger_fragments(FRAGMENTS, "0" * 64, INTERDITES)


def _muter(nom):
    o = objet_fragments()
    if nom == "categorie_absente":
        del o["conformes"]["limites"]
    elif nom == "identifiant_repete":
        o["conformes"]["modules"][1]["id"] = o["conformes"]["modules"][0]["id"]
    elif nom == "mot_classe":
        o["conformes"]["limites"][0]["champs"]["limites"] += " Cette classe est bonne."
    elif nom == "nom_d_item":
        o["conformes"]["limites"][0]["champs"]["limites"] += " Voir module_nomme."
    elif nom == "etiquette_interdite":
        o["conformes"]["limites"][0]["champs"]["limites"] += f" Lu par {INTERDITES[0]}."
    elif nom == "citation_sans_marque":
        o["conformes"]["limites"][0]["citation"] = True
    elif nom == "marque_sans_citation":
        o["conformes"]["limites"][0]["champs"]["limites"] += " Un travail (non vérifié)."
    elif nom == "couverture_fautive":
        o["fautifs"] = [f for f in o["fautifs"] if not (f["item"] == "epreuve_plantee" and f["niveau"] == "net")]
    elif nom == "cle_inconnue":
        o["conformes"]["modules"][0]["remarque"] = "x"
    elif nom == "module_sans_nom":
        o["conformes"]["modules"][0]["champs"]["module_change"] = "L'ensemble change, sans pièce dite pour la forme."
    elif nom == "categorie_interdite_pour_l_item":
        f = next(f for f in o["fautifs"] if f["item"] == "module_nomme")
        f["categorie"] = "limites"
        f["champs"] = {"limites": "Limite neutre d'essai."}
    elif nom == "reprise_hors_voisins":
        o["conformes"]["limites"][0]["piege"] = "reprise_assumee"
    elif nom == "champ_en_trop":
        o["conformes"]["modules"][0]["champs"]["limites"] = "texte"
    elif nom == "schema_faux":
        o["schema"] = "autre"
    return o


@pytest.mark.parametrize("nom", ["categorie_absente", "identifiant_repete", "mot_classe", "nom_d_item",
                                 "etiquette_interdite", "citation_sans_marque", "marque_sans_citation",
                                 "couverture_fautive", "cle_inconnue", "module_sans_nom",
                                 "categorie_interdite_pour_l_item", "reprise_hors_voisins", "champ_en_trop", "schema_faux"])
def test_fragments_artefacts_refuses(nom):
    with pytest.raises(G.FragmentsRefuses):
        G.valider_fragments(_muter(nom), INTERDITES)


def test_aucun_fragment_dans_le_code():
    source = PROGRAMME.read_text(encoding="utf-8")
    o = objet_fragments()
    textes = [v for c in o["conformes"].values() for f in c for v in f["champs"].values()]
    textes += [v for f in o["fautifs"] for v in f["champs"].values()]
    for t in textes:
        if len(t) > 30:
            assert t not in source
    assert "fragments-exemple-essais" not in source


# ------------------------------------------------------------------------------------------------------------------------------
# composition : proportions, longueurs, citation, journal = vérité
# ------------------------------------------------------------------------------------------------------------------------------


def test_proportions_exactes(composition):
    b, j = composition["banque"], composition["journal"]
    G.verifier_proportions(b, j)
    c = G.comptes_de_la_banque(b)
    assert (c["total"], c["bons"], c["mauvais"]) == (200, 100, 100)
    assert (c["bons_citants"], c["mauvais_citants"]) == (50, 50)
    for it in G.ITEMS:
        assert c["par_item"][it] == {"total": 20, "citants": 10, "declare": 4, "net": 8, "discret": 8}
    types = {}
    for t in j:
        if t["classe"] == "bon":
            types[(t["type_bon"], t["citation"])] = types.get((t["type_bon"], t["citation"]), 0) + 1
    assert types == {("simple", True): 25, ("simple", False): 25, ("a_piege", True): 25, ("a_piege", False): 25}
    assert all(t["piege"] in G.PIEGES_NON_CITANTS for t in j if t["type_bon"] == "a_piege" and not t["citation"])
    assert {t["piege"] for t in j if t["type_bon"] == "a_piege" and t["citation"]} == set(G.PIEGES)


def test_proportions_artefact_refuse(composition):
    b = [dict(t) for t in composition["banque"]]
    j = [dict(t) for t in composition["journal"]]
    k = next(i for i, t in enumerate(b) if t["classe"] == "mauvais" and t["citation"])
    b[k]["citation"] = False
    with pytest.raises(G.Refus):
        G.verifier_proportions(b, j)


def test_longueurs_entrelacees_entre_classes(composition):
    j = composition["journal"]
    assert all(1200 <= t["longueur"] <= 2800 for t in j)
    for classe in ("bon", "mauvais"):
        comptes = [sum(1 for t in j if t["classe"] == classe and t["bande"] == b) for b in range(G.N_BANDES)]
        assert sum(comptes) == 100 and set(comptes) <= {12, 13}
    for t in j:
        assert G.bande_de(t["longueur"]) == t["bande"]


def test_journal_est_la_verite(composition):
    fr = composition["fr"]
    par_id = {t["identifiant_interne"]: t for t in composition["banque"]}
    for j in composition["journal"]:
        choix = {c: fr["par_id"][fid] for c, fid in j["fragments"].items()}
        assert G.assembler(choix) == par_id[j["identifiant_interne"]]["contenu"]
        fautifs = [f for f in choix.values() if f["item"] is not None]
        pieges = [f for f in choix.values() if f["piege"] is not None]
        assert j["citation"] == any(f["citation"] for f in choix.values())
        if j["classe"] == "mauvais":
            assert len(fautifs) == 1 and not pieges
            assert (fautifs[0]["item"], fautifs[0]["niveau"]) == (j["item"], j["niveau"])
        elif j["type_bon"] == "a_piege":
            assert not fautifs and len(pieges) == 1 and pieges[0]["piege"] == j["piege"]
        else:
            assert not fautifs and not pieges


def test_composition_reproductible(composition):
    fr = composition["fr"]
    b2, j2 = G.composer(fr, G.Contexte("essais"), G.ITEMS, INTERDITES)
    assert G.json_octets(b2) == G.json_octets(composition["banque"])
    assert G.json_octets(j2) == G.json_octets(composition["journal"])


def test_fragments_insuffisants_refus_nomme(monkeypatch):
    o = objet_fragments()
    for c in o["conformes"]:
        o["conformes"][c] = [f for f in o["conformes"][c] if f["piege"] is not None or f["id"].endswith("-n0")]
    fr = G.valider_fragments(o, INTERDITES)
    monkeypatch.setattr(G, "MAX_TIRAGES", 50)
    with pytest.raises(G.FragmentsInsuffisants):
        G.composer(fr, G.Contexte("essais"), G.ITEMS, INTERDITES)


def test_verite_non_servie_dans_la_banque(composition):
    for t in composition["banque"]:
        texte = json.dumps(t["contenu"], ensure_ascii=False)
        assert not G.fautes_servables(list(t["contenu"].values()), G.ITEMS, INTERDITES)
        assert t["identifiant_interne"] not in texte
        assert set(t["contenu"]) == set(G.CHAMPS_FICHE)
    assert G.fautes_servables(["Une phrase avec le mot classe."], G.ITEMS, INTERDITES)
    assert G.fautes_servables(["Voir reserves_tenues."], G.ITEMS, INTERDITES)


# ------------------------------------------------------------------------------------------------------------------------------
# partage
# ------------------------------------------------------------------------------------------------------------------------------


def test_partage_stratifie(composition):
    b, j = composition["banque"], composition["journal"]
    assert sum(t["moitie"] == "lecture" for t in b) == 100
    for classe in ("bon", "mauvais"):
        assert sum(t["moitie"] == "lecture" for t in b if t["classe"] == classe) == 50
    assert sum(t["moitie"] == "lecture" for t in b if t["classe"] == "bon" and t["citation"]) == 25
    for it in G.ITEMS:
        assert sum(t["moitie"] == "lecture" for t in b if t["item"] == it) == 10
        for n in G.NIVEAUX:
            assert sum(t["moitie"] == "lecture" for t in b if t["item"] == it and t["niveau"] == n) == G.PAR_NIVEAU[n] // 2
    for s in G.partage_par_strate(j):
        assert abs(s["lecture"] - s["etalonnage"]) <= 1


def test_banque_lisible_par_le_code_d_appel_v4(composition):
    v4 = G.charger_code_appel_v4()
    temoins = v4.valider_banque({"temoins": composition["banque"]}, list(G.ITEMS), 200)
    assert len(temoins) == 200


# ------------------------------------------------------------------------------------------------------------------------------
# garde de recouvrement : cas sain et les sept artefacts, cartes factices seulement
# ------------------------------------------------------------------------------------------------------------------------------


def test_garde_cas_sain_rien_des_cartes_ne_sort(dossier, lancer, composition):
    cartes = cartes_factices()
    cp = ecrire_cartes(dossier, cartes)
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)
    res = lancer(bp, cp)
    r = res["rapport"]
    assert res["code"] == 0 and r["decision"] == "banque passée"
    assert (r["cartes_lues"], r["temoins_compares"], r["temoins_refuses"], r["nombre_de_rejeux"]) == (94, 200, 0, 0)
    assert r["empreinte_fichier_cartes"] == sha_f(cp) and r["empreinte_temoins_v2"] == G.TEMOINS_V2[1]
    assert r["empreinte_banque"] == sha_f(bp) and r["empreinte_programme"] == sha_f(PROGRAMME)
    assert_rapport_ferme(r)
    assert json.loads((res["sortie"] / "rapport-garde.json").read_text(encoding="utf-8")) == r
    assert (res["sortie"] / "rapport-garde.json.sha256").exists() and (res["sortie"] / "manifeste-garde.json.sha256").exists()
    lignes = [json.loads(x) for x in Path(res["journal"]).read_text(encoding="utf-8").splitlines()]
    assert [x["type"] for x in lignes] == ["ouverture", "cloture"] and lignes[0]["nature_entree"] == "essai"
    assert res["entree"].ouvertures == 1 and res["err"] == ""
    assert_rien_des_cartes(res, cartes)


def test_garde_temoin_recopie_d_une_carte_refuse(dossier, lancer, composition):
    banque = composition["banque"]
    cible = banque[7]
    cartes = cartes_factices()
    cartes[10]["contenu"]["texte"] = "Début inventé. " + cible["contenu"]["mecanisme"] + " Fin inventée."
    cp = ecrire_cartes(dossier, cartes)
    bp = ecrire_banque(dossier, banque)
    preparer_journal(dossier)
    res = lancer(bp, cp)
    r = res["rapport"]
    assert res["code"] == 4 and r["decision"] == "banque refusée"
    assert cible["identifiant_interne"] in r["identifiants_temoins_refuses"]
    assert r["temoins_refuses"] == len(r["identifiants_temoins_refuses"]) >= 1
    assert all(n >= 1 for n in r["bardeaux_communs_par_temoin_refuse"].values())
    assert_rapport_ferme(r)
    assert_rien_des_cartes(res, cartes)


def test_garde_temoin_recopie_d_un_temoin_v2_refuse(dossier, lancer, composition):
    banque = [json.loads(json.dumps(t)) for t in composition["banque"]]
    v2 = json.loads((G.DEPOT / G.TEMOINS_V2[0]).read_text(encoding="utf-8"))
    banque[0]["contenu"]["limites"] += " " + v2["temoins"][0]["contenu"]["mecanisme"]
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, banque)
    preparer_journal(dossier)
    res = lancer(bp, cp)
    assert res["rapport"]["decision"] == "banque refusée"
    assert banque[0]["identifiant_interne"] in res["rapport"]["identifiants_temoins_refuses"]


def _compter_comparaisons(monkeypatch):
    appels = []
    original = G.bardeaux_communs

    def espion(*a, **k):
        appels.append(1)
        return original(*a, **k)

    monkeypatch.setattr(G, "bardeaux_communs", espion)
    return appels


def test_garde_empreinte_fausse_refus_avant_comparaison(dossier, lancer, composition, monkeypatch):
    appels = _compter_comparaisons(monkeypatch)
    cartes = cartes_factices()
    cp = ecrire_cartes(dossier, cartes)
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)
    res = lancer(bp, cp, empreinte="1" * 64)
    r = res["rapport"]
    assert r["decision"] == "garde non jouée" and r["exception"]["classe"] == "EmpreinteCartesAutre"
    assert appels == [] and "cartes_lues" not in r and "temoins_compares" not in r
    assert r["empreinte_fichier_cartes"] == sha_f(cp) and r["nombre_de_rejeux"] == 0
    assert res["code"] == 5
    assert_rapport_ferme(r)
    assert_rien_des_cartes(res, cartes)


def test_garde_compte_faux_refus_avant_comparaison(dossier, lancer, composition, monkeypatch):
    appels = _compter_comparaisons(monkeypatch)
    cartes = cartes_factices(n=93)
    cp = ecrire_cartes(dossier, cartes)
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "CompteCartesAutre" and appels == []
    assert_rien_des_cartes(res, cartes)


def test_garde_format_inconnu_refus(dossier, lancer, composition, monkeypatch):
    appels = _compter_comparaisons(monkeypatch)
    cp = dossier / "cartes-format.json"
    cp.write_text(json.dumps("une simple chaîne"), encoding="utf-8")
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "FormatCartesInconnu" and appels == []


def test_garde_seule_la_forme_reelle_des_cartes(dossier, lancer, composition, monkeypatch):
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)
    cartes = cartes_factices()
    res = lancer(bp, ecrire_cartes(dossier, cartes))                                 # cas sain : forme réelle
    assert res["rapport"]["decision"] == "banque passée" and res["rapport"]["cartes_lues"] == 94
    appels = _compter_comparaisons(monkeypatch)
    reelle = forme_reelle(cartes)
    ident_long = dict(reelle)
    ident_long["c00000000000ff"] = ident_long.pop(cartes[0]["id"])                   # quatorze caractères
    sans_contenu = dict(reelle)
    sans_contenu[cartes[1]["id"]] = {"empreinte": "a" * 64}
    for nom, objet in (("liste", cartes), ("fiches", {"fiches": cartes}), ("identifiant-long", ident_long),
                       ("sans-contenu", sans_contenu), ("vide", {})):                 # artefacts : formes non réelles
        p = dossier / f"forme-{nom}.json"
        p.write_text(json.dumps(objet, ensure_ascii=False), encoding="utf-8")
        r = lancer(bp, p)
        assert r["rapport"]["exception"]["classe"] == "FormatCartesInconnu", nom
    assert appels == []


def test_garde_meta_retire_aucun_refus(dossier, lancer, composition):
    banque = composition["banque"]
    cartes = cartes_factices()
    cartes[20]["meta"]["copie"] = banque[5]["contenu"]["mecanisme"] + " " + banque[5]["contenu"]["limites"]
    cp = ecrire_cartes(dossier, cartes)
    bp = ecrire_banque(dossier, banque)
    preparer_journal(dossier)
    res = lancer(bp, cp)
    assert res["rapport"]["decision"] == "banque passée" and res["rapport"]["temoins_refuses"] == 0
    assert_rien_des_cartes(res, cartes)


def test_rapport_hors_liste_refus_d_ecrire(dossier):
    ids = frozenset({"l3e2-001"})
    sain = {"decision": "banque passée", "empreinte_programme": "a" * 64, "cartes_lues": 94, "nombre_de_rejeux": 0,
            "identifiants_temoins_refuses": [], "repli": None, "exception": None}
    G.ecrire_rapport_garde(dossier / "sain.json", sain, ids)
    for mauvais in (dict(sain, texte="une phrase"), dict(sain, identifiants_temoins_refuses=["carte-x"]),
                    dict(sain, exception={"classe": "ValueError", "fichier": PROGRAMME.name, "ligne": 3, "message": "x"}),
                    dict(sain, exception={"classe": "Valeur avec espace", "fichier": PROGRAMME.name, "ligne": 3}),
                    dict(sain, decision="autre"), dict(sain, cartes_lues="94"),
                    dict(sain, repli={"mention": "repli sur sept cartes", "cause": "autre"}),
                    dict(sain, bardeaux_communs_par_temoin_refuse={"l3e2-001": 0})):
        cible = dossier / "mauvais.json"
        with pytest.raises(G.RapportHorsListe):
            G.ecrire_rapport_garde(cible, mauvais, ids)
        assert not cible.exists()


def _journal_avec(dossier: Path, ouvertures: int) -> Path:
    j = preparer_journal(dossier)
    jr = G.JournalRejeux(j)
    for k in range(1, ouvertures + 1):
        jr.ajouter({"type": "ouverture", "rang": k, "rejeu": k - 1, "horodatage_utc": "2026-11-20T00:00:00Z",
                    "empreinte_banque": "b" * 64, "empreinte_programme": "c" * 64, "mot_de_la_mere_sha256": None,
                    "repli": None, "nature_entree": "essai"})
        jr.ajouter({"type": "cloture", "rang": k, "decision": "banque refusée", "cartes_lues": 94,
                    "temoins_compares": 200, "temoins_refuses": 1, "exception": None})
    return j


def test_garde_cinq_rejeux_sans_mot_refus_avant_ouverture(dossier, lancer, composition):
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    j = _journal_avec(dossier, 6)                      # premier passage + cinq rejeux
    avant = j.read_bytes()
    res = lancer(bp, cp)
    r = res["rapport"]
    assert r["exception"]["classe"] == "SixiemeRejeuSansMotDeLaMere" and r["nombre_de_rejeux"] == 5
    assert res["entree"].ouvertures == 0 and j.read_bytes() == avant
    mot = "R-9999 (essai) : « mot factice de la mère pour un sixième rejeu »"
    res2 = lancer(bp, cp, extra=["--mot-de-la-mere", mot])
    assert res2["rapport"]["decision"] == "banque passée" and res2["rapport"]["nombre_de_rejeux"] == 6
    m = json.loads((res2["sortie"] / "manifeste-garde.json").read_text(encoding="utf-8"))
    assert m["mot_de_la_mere"] == mot
    res3 = lancer(bp, cp, extra=["--mot-de-la-mere", mot])
    assert res3["rapport"]["exception"]["classe"] == "MotDeLaMereDejaCite" and res3["entree"].ouvertures == 0


def test_garde_cinquieme_rejeu_permis_sans_mot(dossier, lancer, composition):
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    _journal_avec(dossier, 5)                          # premier passage + quatre rejeux
    res = lancer(bp, cp)
    assert res["rapport"]["decision"] == "banque passée" and res["rapport"]["nombre_de_rejeux"] == 5


def test_garde_sans_manifeste_de_creation_refus_avant_ouverture(dossier, lancer, composition):
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    res = lancer(bp, cp)                                # journal jamais créé : ni journal ni manifeste
    assert res["rapport"]["exception"]["classe"] == "ManifesteJournalAbsentOuFaux" and res["entree"].ouvertures == 0
    assert res["code"] == 5
    (dossier / "journal").mkdir()
    lieu(dossier).journal.write_bytes(b"")             # journal posé à la main, sans le geste écrit : refus
    res2 = lancer(bp, cp)
    assert res2["rapport"]["exception"]["classe"] == "ManifesteJournalAbsentOuFaux" and res2["entree"].ouvertures == 0


def test_garde_journal_supprime_refus_avant_ouverture_et_recreation_refusee(dossier, lancer, composition, capfd):
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    j = preparer_journal(dossier)
    assert lancer(bp, cp)["rapport"]["decision"] == "banque passée"
    j.unlink()                                          # le journal disparaît : le compte ne repart pas de zéro
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "JournalRejeuxAbsent" and res["entree"].ouvertures == 0
    with pytest.raises(G.ManifesteJournalExisteDeja):
        G.creer_journal_rejeux(lieu(dossier))
    assert not j.exists()
    code = G.principal(["creer-journal-rejeux"], lieu_journal=lieu(dossier))
    assert code == 2 and "ManifesteJournalExisteDeja" in capfd.readouterr().err and not j.exists()


def test_garde_manifeste_d_un_autre_journal_refuse(dossier, lancer, composition):
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    (dossier / "autre").mkdir()
    initialiser_depot(dossier)
    G.creer_journal_rejeux(G.LieuDuJournal.essai(dossier / "autre", depot=dossier))
    (dossier / "journal").mkdir()
    import shutil
    shutil.copy(dossier / "autre" / G.MANIFESTE_JOURNAL_REJEUX.name, lieu(dossier).manifeste)
    shutil.copy(dossier / "autre" / (G.MANIFESTE_JOURNAL_REJEUX.name + ".sha256"),
                str(lieu(dossier).manifeste) + ".sha256")
    lieu(dossier).journal.write_bytes(b"")
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "ManifesteJournalAbsentOuFaux" and res["entree"].ouvertures == 0


def test_aucun_chemin_libre_pour_le_journal(dossier, lancer, composition, capfd):
    preparer_journal(dossier)
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    for extra in (["--journal-rejeux", str(dossier / "x.jsonl")], ["--journal", str(dossier / "x.jsonl")],
                  ["--sortie", str(dossier / "deux")]):
        res = lancer(bp, cp, extra=extra)
        assert res["rapport"]["exception"]["classe"] == "ArgumentHorsListe" and res["entree"].ouvertures == 0
    assert G.principal(["creer-journal-rejeux", "--journal", str(dossier / "y.jsonl")]) == 2
    assert "ArgumentHorsListe" in capfd.readouterr().err and not (dossier / "y.jsonl").exists()
    assert G.JOURNAL_REJEUX == G.DEPOT / "runs" / "ligne-3-etage-2-garde-de-recouvrement-v1" / \
        "journal-rejeux-garde-recouvrement-v1.jsonl"
    assert G.MANIFESTE_JOURNAL_REJEUX.parent == G.JOURNAL_REJEUX.parent
    assert G.LieuDuJournal.production().journal == G.JOURNAL_REJEUX          # construit, jamais lu ici
    with pytest.raises(G.ManifesteJournalAbsentOuFaux):
        G.LieuDuJournal(dossier / "j.jsonl", dossier / "m.json", "production")
    with pytest.raises(G.CheminInterdit):
        G.LieuDuJournal.essai(dossier / "archives-reponses-modeles")


@pytest.mark.parametrize("contenu", [b"pas du json\n", b'{"n_ligne": 0, "type": "ouverture"}\n', b'{"n_ligne": 0',
                                     b"\xff\xfe\n"])
def test_garde_journal_illisible_refus_avant_ouverture(dossier, lancer, composition, contenu):
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    j = preparer_journal(dossier)
    j.write_bytes(contenu)
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "JournalRejeuxIllisible" and res["entree"].ouvertures == 0


def test_garde_exception_provoquee_pendant_la_lecture(dossier, lancer, composition):
    cartes = cartes_factices()
    cp = ecrire_cartes(dossier, cartes)
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)

    def provoquer(carte):
        if SECRET_CARTE in json.dumps(carte, ensure_ascii=False):
            raise ValueError("texte de la carte : " + json.dumps(carte, ensure_ascii=False))

    res = lancer(bp, cp, provoquer=provoquer)
    r = res["rapport"]
    assert r["decision"] == "garde non jouée"
    assert r["exception"]["classe"] == "ValueError" and r["exception"]["fichier"] == PROGRAMME.name
    assert isinstance(r["exception"]["ligne"], int)
    assert res["err"] == ""
    assert_rapport_ferme(r)
    assert_rien_des_cartes(res, cartes)


def test_garde_exception_json_coupe(dossier, lancer, composition):
    cartes = cartes_factices()
    texte = json.dumps(forme_reelle(cartes), ensure_ascii=False)
    coupe = texte[: texte.index(SECRET_CARTE) + 40]
    cp = dossier / "cartes-coupees.json"
    cp.write_text(coupe, encoding="utf-8")
    bp = ecrire_banque(dossier, composition["banque"])
    preparer_journal(dossier)
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "JSONDecodeError"
    assert_rien_des_cartes(res, cartes)


def _cartes_avec_nommees():
    ids = [f"c{k:012x}" for k in range(94)]
    for pos, nid in zip((2, 11, 23, 37, 48, 60, 81), G.CARTES_NOMMEES):
        ids[pos] = nid                                     # v3 : égalité exacte, treize caractères
    return cartes_factices(ids=ids)


def test_garde_repli_sur_sept_cartes(dossier, lancer, composition):
    banque = composition["banque"]
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, banque)
    pr = piece(dossier, "refus-ecrit-factice.md", "Refus écrit factice de la mère, pour les essais.\n")
    cartes = _cartes_avec_nommees()
    cartes[5]["contenu"]["texte"] = banque[9]["contenu"]["mecanisme"]          # carte non nommée
    cp = ecrire_cartes(dossier, cartes)
    extra = ["--repli", G.DECLENCHEURS_REPLI[0], "--piece-repli", str(pr), "--empreinte-piece-repli", sha_f(pr)]
    res = lancer(bp, cp, extra=extra)
    r = res["rapport"]
    assert r["decision"] == "banque passée" and r["cartes_lues"] == 7
    assert r["repli"] == {"mention": "repli sur sept cartes", "cause": G.DECLENCHEURS_REPLI[0]}
    assert r["nombre_de_rejeux"] == 0
    m = json.loads((res["sortie"] / "manifeste-garde.json").read_text(encoding="utf-8"))
    assert m["repli"]["cause"] == G.DECLENCHEURS_REPLI[0] and "sept cartes" in m["repli"]["ecart"]
    assert_rien_des_cartes(res, cartes)
    res_sans = lancer(bp, cp)                                                  # sans repli : 94 cartes, la copie est vue
    assert res_sans["rapport"]["decision"] == "banque refusée" and res_sans["rapport"]["nombre_de_rejeux"] == 1
    cartes2 = _cartes_avec_nommees()
    cartes2[11]["contenu"]["texte"] = banque[9]["contenu"]["mecanisme"]        # carte nommée
    cp2 = ecrire_cartes(dossier, cartes2, "cartes-2.json")
    res2 = lancer(bp, cp2, extra=extra)
    assert res2["rapport"]["decision"] == "banque refusée" and res2["rapport"]["nombre_de_rejeux"] == 2


def test_garde_repli_hors_des_deux_declencheurs(dossier, lancer, composition):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, _cartes_avec_nommees())
    pr = piece(dossier, "piece.md", "pièce factice\n")
    res = lancer(bp, cp, extra=["--repli", "envie-de-replier", "--piece-repli", str(pr), "--empreinte-piece-repli",
                                sha_f(pr)])
    assert res["rapport"]["exception"]["classe"] == "ReplisHorsDeclencheur" and res["entree"].ouvertures == 0
    res2 = lancer(bp, cp, extra=["--repli", G.DECLENCHEURS_REPLI[1]])
    assert res2["rapport"]["exception"]["classe"] == "PieceDuReplisAbsenteOuFausse" and res2["entree"].ouvertures == 0


def test_garde_repli_empreinte_autre_ni_garde_ni_repli(dossier, lancer, composition):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, _cartes_avec_nommees())
    pr = piece(dossier, "piece.md", "pièce factice\n")
    extra = ["--repli", G.DECLENCHEURS_REPLI[1], "--piece-repli", str(pr), "--empreinte-piece-repli", sha_f(pr)]
    res = lancer(bp, cp, empreinte="2" * 64, extra=extra)
    assert res["rapport"]["exception"]["classe"] == "EmpreinteCartesAutre"
    assert "cartes_lues" not in res["rapport"]


def test_garde_repli_cartes_nommees_introuvables(dossier, lancer, composition):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, cartes_factices())
    pr = piece(dossier, "piece.md", "pièce factice\n")
    extra = ["--repli", G.DECLENCHEURS_REPLI[0], "--piece-repli", str(pr), "--empreinte-piece-repli", sha_f(pr)]
    res = lancer(bp, cp, extra=extra)
    assert res["rapport"]["exception"]["classe"] == "CartesNommeesIntrouvables"


def test_garde_seconde_entree_verifiee_avant_ouverture(dossier, lancer, composition):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, cartes_factices())
    v2 = G.EntreeV2.essai(G.DEPOT / G.TEMOINS_V2[0], "3" * 64)
    res = lancer(bp, cp, v2=v2)
    assert res["rapport"]["exception"]["classe"] == "EmpreinteTemoinsV2Autre" and res["entree"].ouvertures == 0
    v2b = G.EntreeV2.essai(G.DEPOT / G.TEMOINS_V2[0], G.TEMOINS_V2[1], compte=12)
    res2 = lancer(bp, cp, v2=v2b)
    assert res2["rapport"]["exception"]["classe"] == "CompteTemoinsV2Autre" and res2["entree"].ouvertures == 0


def test_garde_sans_controle_4_ne_tourne_pas(dossier, lancer, composition):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, cartes_factices())
    res = lancer(bp, cp, controle=False)
    assert res["rapport"]["decision"] == "garde non jouée" and res["entree"].ouvertures == 0


def test_garde_sortie_existante_et_chemin_du_coffre(dossier, lancer, composition):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, cartes_factices())
    (dossier / "sortie-garde-1").mkdir()
    res = lancer(bp, cp)
    assert res["rapport"]["exception"]["classe"] == "SortieExistante" and res["entree"].ouvertures == 0
    coffre = dossier / "coffre-factice"
    coffre.mkdir()
    bp2 = ecrire_banque(coffre, composition["banque"])
    res2 = lancer(bp2, cp)
    assert res2["rapport"]["exception"]["classe"] == "CheminInterdit" and res2["entree"].ouvertures == 0


def test_entree_d_essai_refuse_l_archive_des_reponses(dossier):
    for faux in (dossier / "archives-reponses-modeles" / "x" / "fiches.json", dossier / "coffre-x" / "fiches.json"):
        with pytest.raises(G.CheminInterdit):         # refus sur la forme écrite, sans aucun appel au système de fichiers
            G.EntreeCartes.essai(faux, "0" * 64)


def test_constantes_de_l_entree_unique():
    assert G.EMPREINTE_CARTES == "ba65c411f4e3062fba29d93b5a00fe6fee23b34ebdc64f1708a0cc49177c3481"
    assert G.COMPTE_CARTES == 94
    assert str(G.CHEMIN_CARTES) == ("/home/user/controle-ia-travail/archives-reponses-modeles/"
                                    "auto-conception-course-v9-2026-11-19-v1/course-v9-sortie/sortie/generation-1/fiches.json")
    assert G.CARTES_NOMMEES == ("fb3a2cc87251c", "f6f8c8b855234", "fc37640a0181d", "fa38f9faa24e0", "fefca0bd94064",
                                "fcfa3d98b90f8", "fcbf4a2dd1a57")
    e = G.EntreeCartes.production()                    # construite, jamais lue
    assert e.chemin == G.CHEMIN_CARTES and e.ouvertures == 0 and e.nature == "production"
    assert G.MAX_REJEUX_SANS_MOT == 5 and G.TAILLE_BARDEAU == 8


def test_creer_journal_rejeux_puis_recreation_refusee(dossier):
    initialiser_depot(dossier)
    lj = lieu(dossier)
    m = G.creer_journal_rejeux(lj)
    assert lj.journal.read_bytes() == b"" and m["journal_sha256"] == sha(b"") and m["journal"] == str(lj.journal)
    assert Path(str(lj.manifeste) + ".sha256").exists()
    assert G.JournalRejeux(lj.journal).ouvertures == 0
    G.exiger_manifeste_du_journal(lj)
    with pytest.raises(G.ManifesteJournalExisteDeja):
        G.creer_journal_rejeux(lj)


# ------------------------------------------------------------------------------------------------------------------------------
# audit du générateur
# ------------------------------------------------------------------------------------------------------------------------------


def service_factice(alterer=False):
    consigne = G.lire_par_empreinte(G.DEPOT / G.CONSIGNE_JUGE[0], G.CONSIGNE_JUGE[1], "consigne").decode("utf-8")

    def entree(consigne_, fiche, interdites, identifiant_servi=None):
        d = dict(fiche["contenu"])
        if alterer:
            d["titre"] = d["titre"] + " altéré"
        d["identifiant"] = identifiant_servi
        return consigne_ + "\n\n" + G.MARQUE_FICHE + json.dumps(d, ensure_ascii=False, indent=1) + "\n```\n"

    def lire(texte, items):
        try:
            o = json.loads(texte.rsplit("```json\n", 1)[1].rsplit("\n```", 1)[0])
        except (IndexError, ValueError):
            return None
        its = o.get("items")
        if not isinstance(its, dict) or set(its) != set(items):
            return None
        return {"items": its, "notable": all(its.values())}

    return G.ServiceAudit(nature="essai", entree_une_fiche=entree, lire_verdict=lire, consigne=consigne, items=G.ITEMS,
                          interdites=INTERDITES)


def test_audit_banque_equilibree_passee(composition):
    s = service_factice()
    r = G.auditer(composition["banque"], G.Contexte("essais"), s)
    assert r["decision"] == "banque passée", r["motifs_de_refus"]
    assert Fraction(r["aire_qui_decide"]["aire_exacte"]) <= Fraction(3, 5)
    assert "aire_exacte" in r["aire_a_tous_les_traits"]
    for v in r["traits_de_la_lettre"].values():
        assert v["dans_la_bande"]
    assert r["traits_de_la_lettre"]["modules_distincts"]["bons"] == 100
    assert r["traits_de_la_lettre"]["modules_distincts"]["mauvais"] == 80
    assert r["traits_de_la_lettre"]["non_verifie"]["mauvais"] == 80
    assert r["juges_scriptes_de_surface"]["parfait"]["erreur_equilibree"] == 0
    for g in ("longueur", "champ_lu", "citation"):
        assert r["juges_scriptes_de_surface"][g]["dans_la_bande"]
    assert s.appels == 4 * 200
    assert r["plis"]["effectifs"] == [[10, 10]] * 10
    for t in composition["banque"]:
        n = len(G.modules_nommes(t["contenu"]["module_change"]))
        assert n == (0 if t["item"] == "module_nomme" else 1)


def test_audit_mauvais_plus_courts_refuses(composition):
    banque = [json.loads(json.dumps(t)) for t in composition["banque"]]
    for t in banque:
        if t["classe"] == "mauvais":
            t["contenu"] = {k: v[: max(1, int(len(v) * 0.7))] for k, v in t["contenu"].items()}
    r = G.auditer(banque, G.Contexte("essais"), service_factice())
    assert r["decision"] == "banque refusée"
    assert Fraction(r["aire_qui_decide"]["aire_exacte"]) > Fraction(3, 5)
    assert not r["juges_scriptes_de_surface"]["longueur"]["dans_la_bande"]


def test_audit_traits_de_la_lettre_artefact_refuse(composition):
    banque = [json.loads(json.dumps(t)) for t in composition["banque"]]
    for t in banque:
        if t["classe"] == "mauvais" and t["item"] != "reserves_tenues":
            t["contenu"] = {k: v.replace("(non vérifié)", "(marqué)") for k, v in t["contenu"].items()}
    r = G.auditer(banque, G.Contexte("essais"), service_factice())
    assert not r["traits_de_la_lettre"]["non_verifie"]["dans_la_bande"]
    assert r["decision"] == "banque refusée"


def test_audit_service_qui_altere_la_fiche_banc_invalide(composition):
    with pytest.raises(G.BancInvalide):
        G.jouer_juges_de_surface(composition["banque"], service_factice(alterer=True))


def test_audit_juge_parfait_en_erreur_banc_invalide(composition, monkeypatch):
    original = G.juger_scripte

    def faux(genre, fiche, temoin, items, medianes):
        v = original(genre, fiche, temoin, items, medianes)
        if genre == "parfait" and temoin["classe"] == "mauvais":
            return {k: True for k in items}
        return v

    monkeypatch.setattr(G, "juger_scripte", faux)
    with pytest.raises(G.BancInvalide):
        G.jouer_juges_de_surface(composition["banque"], service_factice())


def test_aire_par_rangs_contre_les_paires():
    import numpy as np
    rng = np.random.default_rng(np.random.SeedSequence(G.RACINE_ESSAIS, spawn_key=(99,)))
    for _ in range(20):
        s = rng.integers(0, 5, size=30).astype(float)
        y = np.zeros(30, dtype=bool)
        y[rng.permutation(30)[:12]] = True
        pos, neg = s[y], s[~y]
        brute = Fraction(sum(2 * (a > b) + (a == b) for a in pos for b in neg), 2 * len(pos) * len(neg))
        assert G.aire_par_rangs(s, y) == brute


def test_logistique_newton_converge_et_gradient_nul():
    import numpy as np
    rng = np.random.default_rng(np.random.SeedSequence(G.RACINE_ESSAIS, spawn_key=(98,)))
    X = rng.normal(size=(120, 4))
    y = (X[:, 0] + 0.5 * rng.normal(size=120) > 0).astype(float)
    w, b, it, conv = G.logistique(X, y)
    assert conv and it <= G.MAX_NEWTON
    p = 1 / (1 + np.exp(-(X @ w + b)))
    assert np.max(np.abs(X.T @ (p - y) + G.PENALITE * w)) < 1e-8 and abs(np.sum(p - y)) < 1e-8
    sp, _it, _c = G.scores_hors_pli(X, y, G.plis_stratifies(y, G.Contexte("essais").rng("plis-de-l-audit", audit=True)))
    assert G.aire_par_rangs(sp, y.astype(bool)) > Fraction(3, 4)


def test_plis_stratifies_par_classe():
    import numpy as np
    y = np.array([0] * 100 + [1] * 100)
    plis = G.plis_stratifies(y, G.Contexte("essais").rng("plis-de-l-audit", audit=True))
    for f in range(10):
        assert int(((plis == f) & (y == 0)).sum()) == 10 and int(((plis == f) & (y == 1)).sum()) == 10


# ------------------------------------------------------------------------------------------------------------------------------
# gestes écrits : sorties scellées, manifestes (règle R9)
# ------------------------------------------------------------------------------------------------------------------------------


def test_gestes_composer_et_auditer_ecrits_et_scelles(dossier):
    ctx = G.Contexte("essais")
    res = G.geste_composer(FRAGMENTS, sha_f(FRAGMENTS), dossier / "composition", ctx, INTERDITES, G.ITEMS)
    for nom in ("banque-temoins-ligne-3-v1.json", "journal-construction-ligne-3-v1.json", "partage-ligne-3-v1.json",
                "manifeste-composition.json"):
        p = dossier / "composition" / nom
        compagnon = (dossier / "composition" / (nom + ".sha256")).read_text(encoding="utf-8").split()
        assert compagnon == [sha_f(p), nom]
    m = res["manifeste"]
    assert m["programme_sha256"] == sha_f(PROGRAMME) and m["graines"]["mode"] == "essais"
    assert {d["tache"] for d in m["graines"]["derivations"]} == set(G.CLES_COMPOSITION)
    assert m["versions"]["numpy"] and m["configuration"]["fragments_sha256"] == sha_f(FRAGMENTS)
    with pytest.raises(G.Refus):
        G.geste_composer(FRAGMENTS, sha_f(FRAGMENTS), dossier / "composition", G.Contexte("essais"), INTERDITES, G.ITEMS)
    bp = dossier / "composition" / "banque-temoins-ligne-3-v1.json"
    r = G.geste_auditer(bp, sha_f(bp), dossier / "audit", G.Contexte("essais"), service_factice())
    assert r["decision"] == "banque passée"
    assert (dossier / "audit" / "rapport-audit-ligne-3-v1.json.sha256").exists()
    assert (dossier / "audit" / "manifeste-audit.json.sha256").exists()


def test_ligne_de_commande_refuse_sans_autorisation(capsys):
    code = G.principal(["composer", "--fragments", str(FRAGMENTS), "--empreinte-fragments", sha_f(FRAGMENTS),
                        "--sortie", "/nulle/part"])
    assert code == 2
    err = capsys.readouterr().err
    assert '"refus"' in err and not Path("/nulle/part").exists()


# ------------------------------------------------------------------------------------------------------------------------------
# v2 : pièce du (4) à verdict, meta à toute profondeur, forme réelle, ligne de commande sans trace, C1, M5, M6, R3
# ------------------------------------------------------------------------------------------------------------------------------


@pytest.mark.parametrize("texte,classe", [
    (texte_controle("**Non conforme.** Un point n'est pas tenu."), "ControleQuatreNonConforme"),
    (texte_controle("Verdict : Non conforme"), "ControleQuatreNonConforme"),
    (texte_controle("Le verdict viendra plus tard."), "ControleQuatreNonConforme"),
    (texte_controle("**Conforme.**\n\n**Non conforme.**"), "ControleQuatreNonConforme"),
    (texte_controle("**Conforme.**", programme="e" * 64), "ControleQuatreAutreProgramme"),
])
def test_piece_du_controle_4_non_conforme_ou_d_un_autre_programme_refusee(dossier, lancer, composition, texte, classe):
    preparer_journal(dossier)
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    c = piece(dossier, "controle-mauvais.md", texte)
    res = lancer(bp, cp, controle_piece=c)
    assert res["rapport"]["exception"]["classe"] == classe and res["entree"].ouvertures == 0
    assert res["rapport"]["decision"] == "garde non jouée"


@pytest.mark.parametrize("verdict", ["**Conforme.**", "Conforme", "Verdict : Conforme", "**Verdict : Conforme**"])
def test_piece_du_controle_4_conforme_acceptee(dossier, lancer, composition, verdict):
    preparer_journal(dossier)
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])
    c = piece(dossier, "controle-bon.md", texte_controle(verdict))
    assert lancer(bp, cp, controle_piece=c)["rapport"]["decision"] == "banque passée"


def test_meta_retire_a_toute_profondeur(dossier, lancer, composition):
    banque = composition["banque"]
    copie = banque[4]["contenu"]["mecanisme"] + " " + banque[4]["contenu"]["limites"]
    cartes = cartes_factices()
    cartes[1]["contenu"]["meta"] = {"copie": copie}                                    # imbriqué dans le contenu
    cartes[2]["contenu"]["sous"] = {"liste": [{"meta": copie, "x": "texte court"}]}   # dans une liste, plus bas
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, banque)
    res = lancer(bp, ecrire_cartes(dossier, cartes))
    assert res["rapport"]["decision"] == "banque passée"
    objet = {c["id"]: {"contenu": c["contenu"], "empreinte": "a" * 64, "meta": {"copie": copie}} for c in cartes}
    objet["meta"] = {"copie": copie, "autre": {"n": 1}}                                # au niveau du fichier
    p = dossier / "forme-reelle-avec-meta.json"
    p.write_text(json.dumps(objet, ensure_ascii=False), encoding="utf-8")
    res2 = lancer(bp, p)
    assert res2["rapport"]["decision"] == "banque passée" and res2["rapport"]["cartes_lues"] == 94
    cartes_en_memoire = G.cartes_du_fichier(p.read_bytes())

    def sans_cle_meta(o):
        if isinstance(o, dict):
            return "meta" not in o and all(sans_cle_meta(v) for v in o.values())
        if isinstance(o, list):
            return all(sans_cle_meta(v) for v in o)
        return True

    assert len(cartes_en_memoire) == 94 and all(sans_cle_meta(c) for _i, c in cartes_en_memoire)


def _forme_reelle(cartes, ids):
    """Forme établie par la contre-lecture : {identifiant de treize caractères : {contenu, empreinte, meta}}."""
    return {i: {"contenu": c["contenu"], "empreinte": sha(json.dumps(c["contenu"], sort_keys=True).encode("utf-8")),
                "meta": c["meta"]} for i, c in zip(ids, cartes)}


def test_forme_reelle_du_fichier_des_cartes_admise_avec_repli(dossier, lancer, composition):
    banque = composition["banque"]
    ids = [f"f{k:012x}" for k in range(1, 95)]
    for pos, nid in zip((2, 11, 23, 37, 48, 60, 81), G.CARTES_NOMMEES):
        ids[pos] = nid                                                 # treize caractères, égalité exacte
    assert all(len(i) == 13 for i in ids)
    cartes = cartes_factices()
    cartes[11]["contenu"]["texte"] = banque[9]["contenu"]["mecanisme"]  # carte nommée
    p = dossier / "forme-reelle.json"
    p.write_text(json.dumps(_forme_reelle(cartes, ids), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, banque)
    res = lancer(bp, p)
    assert res["rapport"]["decision"] == "banque refusée" and res["rapport"]["cartes_lues"] == 94
    assert banque[9]["identifiant_interne"] in res["rapport"]["identifiants_temoins_refuses"]
    pr = piece(dossier, "piece.md", "pièce factice\n")
    res2 = lancer(bp, p, extra=["--repli", G.DECLENCHEURS_REPLI[0], "--piece-repli", str(pr),
                               "--empreinte-piece-repli", sha_f(pr)])
    assert res2["rapport"]["decision"] == "banque refusée" and res2["rapport"]["cartes_lues"] == 7
    assert_rien_des_cartes(res, cartes)
    assert_rien_des_cartes(res2, cartes)


def test_ligne_de_commande_aucune_trace_brute(dossier, capfd, monkeypatch):
    def explose(*a, **k):
        raise RuntimeError(SECRET_CARTE)

    monkeypatch.setattr(G, "jouer_la_garde", explose)
    code = G.principal(["garde", "--banque", "b", "--sortie", "s", "--controle-4", "c", "--empreinte-controle-4", "0" * 64])
    out, err = capfd.readouterr()
    r = json.loads(out)
    assert code == 5 and err == "" and r["exception"]["classe"] == "RuntimeError" and SECRET_CARTE not in out
    monkeypatch.setattr(G, "programme_sha256", explose)
    code = G.principal(["garde"])
    out, err = capfd.readouterr()
    r = json.loads(out)
    assert code == 5 and err == "" and set(r) == {"decision", "exception"} and SECRET_CARTE not in out
    G.valider_rapport_garde(r, exiger_programme=False)


def test_garde_sortie_standard_en_panne_aucune_trace(dossier, lancer, composition, capfd, monkeypatch):
    preparer_journal(dossier)
    cp = ecrire_cartes(dossier, cartes_factices())
    bp = ecrire_banque(dossier, composition["banque"])

    class Panne:
        def write(self, *_a):
            raise OSError(SECRET_CARTE)

        def flush(self):
            pass

    monkeypatch.setattr(G.sys, "stdout", Panne())
    entree = G.EntreeCartes.essai(cp, sha_f(cp))
    c = piece(dossier, "c.md", texte_controle())
    code = G.principal(["garde", "--banque", str(bp), "--sortie", str(dossier / "s"), "--controle-4", str(c),
                        "--empreinte-controle-4", sha_f(c)], entree_cartes=entree, lieu_journal=lieu(dossier))
    out, err = capfd.readouterr()
    assert code == 5 and err == "" and json.loads(out)["exception"]["classe"] == "OSError" and SECRET_CARTE not in out


def test_constructeurs_nus_gardes(dossier):
    with pytest.raises(G.CheminInterdit):
        G.EntreeCartes(dossier / "coffre-x" / "f.json", "0" * 64, 94, "essai")
    with pytest.raises(G.EntreeEssaiInterdite):
        G.EntreeCartes(dossier / "f.json", G.EMPREINTE_CARTES, 94, "production")
    with pytest.raises(G.CheminInterdit):
        G.EntreeV2(dossier / "archives-reponses-modeles" / "v2.json", "0" * 64, 11, "essai")


def test_c1_fautif_de_modules_d_un_autre_item_nomme_un_module():
    o = objet_fragments()
    o["fautifs"].append({"id": "f-c1-sain", "item": "aucun_modele_ne_decide", "niveau": "net", "categorie": "modules",
                         "champs": {"module_change": "Le module coffre change : un agent y garde seul ce qui reste."},
                         "citation": False})
    G.valider_fragments(o, INTERDITES)
    o["fautifs"].append({"id": "f-c1-artefact", "item": "aucun_modele_ne_decide", "niveau": "net", "categorie": "modules",
                         "champs": {"module_change": "L'ensemble change ; un agent y garde seul ce qui reste."},
                         "citation": False})
    with pytest.raises(G.FragmentsRefuses) as e:
        G.valider_fragments(o, INTERDITES)
    assert any("f-c1-artefact" in f for f in e.value.fautes)


def test_m5_contenus_identiques_refuses_et_fragments_communs_rapportes(composition, dossier):
    G.verifier_contenus_distincts(composition["banque"])                # cas sain
    b = [json.loads(json.dumps(t)) for t in composition["banque"][:3]]
    b[2]["contenu"] = json.loads(json.dumps(b[0]["contenu"]))
    with pytest.raises(G.ContenusIdentiques):
        G.verifier_contenus_distincts(b)
    c = G.fragments_communs(composition["journal"])
    assert 0 <= c["maximum"] < 5 and sum(c["paires_par_nombre_de_fragments_communs"].values()) == 200 * 199 // 2
    o = objet_fragments()                                                 # artefact par la composition : un fragment
    for cat in o["conformes"]:                                            # par catégorie, contenus forcément répétés
        garde = [f for f in o["conformes"][cat] if f["piege"] is not None]
        simples = [f for f in o["conformes"][cat] if f["piege"] is None]
        o["conformes"][cat] = garde + [next(f for f in simples if not f["citation"])] + \
            [f for f in simples if f["citation"]][:1]
    fr = G.valider_fragments(o, INTERDITES)
    with pytest.raises((G.ContenusIdentiques, G.FragmentsInsuffisants)):
        G.composer(fr, G.Contexte("essais"), G.ITEMS, INTERDITES)


def test_m5_refus_nomme_par_les_deux_identifiants(composition):
    b = [dict(t) for t in composition["banque"]]
    b[1] = dict(b[1], contenu=b[0]["contenu"])
    with pytest.raises(G.ContenusIdentiques) as e:
        G.verifier_contenus_distincts(b)
    assert b[0]["identifiant_interne"] in str(e.value) and b[1]["identifiant_interne"] in str(e.value)


def test_m6_service_reel_du_clone_sur_la_banque_factice(composition, monkeypatch):
    """M6 (mère, 15:05Z) : la vraie fonction de service (clone de l'organisme, par le code d'appel v4, empreintes des cinq
    modules vérifiées avant tout import) sur la banque factice. Fonctions pures : aucun réseau, aucune clé, aucun appel."""
    for n in ("HTTPS_PROXY", "HTTP_PROXY", "https_proxy", "http_proxy"):
        monkeypatch.delenv(n, raising=False)
    import socket

    def interdit(*a, **k):
        raise AssertionError("réseau interdit dans cet essai")

    monkeypatch.setattr(socket, "socket", interdit)
    monkeypatch.setattr(socket, "create_connection", interdit)
    s = G.construire_service_reel()
    assert s.nature == "reel" and list(s.items) == list(G.ITEMS)
    r = G.jouer_juges_de_surface(composition["banque"], s)
    assert r["parfait"]["erreur_equilibree"] == 0
    for g in ("longueur", "champ_lu", "citation"):
        assert r[g]["dans_la_bande"]
    assert s.appels == 4 * 200
    a = G.auditer(composition["banque"], G.Contexte("essais"), G.construire_service_reel())
    assert a["decision"] == "banque passée" and a["service"]["nature"] == "reel"


# ------------------------------------------------------------------------------------------------------------------------------
# v3 : historique git, portée de la pièce du (4), journal existant sans manifeste, pièce lue une seule fois
# ------------------------------------------------------------------------------------------------------------------------------


def test_v3_historique_git_sain_et_artefact(dossier, capfd):
    initialiser_depot(dossier)                                            # cas sain : historique qui ne le connaît pas
    lj = lieu(dossier)
    assert not G.historique_connait(dossier, lj.manifeste)
    G.creer_journal_rejeux(lj)
    d2 = Path(tempfile.mkdtemp(prefix="essais-generateur-v3-git-"))       # artefact : historique qui le connaît
    initialiser_depot(d2)
    l2 = lieu(d2)
    l2.manifeste.parent.mkdir(parents=True)
    l2.manifeste.write_text("{}\n", encoding="utf-8")
    subprocess.run(GIT_ESSAI + ["-C", str(d2), "add", str(l2.manifeste)], check=True, capture_output=True)
    subprocess.run(GIT_ESSAI + ["-C", str(d2), "commit", "-q", "-m", "manifeste"], check=True, capture_output=True)
    subprocess.run(GIT_ESSAI + ["-C", str(d2), "rm", "-q", str(l2.manifeste)], check=True, capture_output=True)
    subprocess.run(GIT_ESSAI + ["-C", str(d2), "commit", "-q", "-m", "retrait"], check=True, capture_output=True)
    assert not l2.manifeste.exists() and G.historique_connait(d2, l2.manifeste)
    with pytest.raises(G.ManifesteJournalConnuDeLHistorique):
        G.creer_journal_rejeux(l2)
    assert not l2.journal.exists()
    assert G.principal(["creer-journal-rejeux"], lieu_journal=l2) == 2
    out, err = capfd.readouterr()
    assert "ManifesteJournalConnuDeLHistorique" in err and "Traceback" not in err + out
    d3 = Path(tempfile.mkdtemp(prefix="essais-generateur-v3-sans-git-"))  # historique illisible (hors dépôt) : refus
    with pytest.raises(G.HistoriqueGitIllisible):
        G.creer_journal_rejeux(lieu(d3))
    assert not lieu(d3).journal.exists()


def test_v3_journal_existant_sans_manifeste_refus_nomme_sans_trace(dossier, capfd):
    initialiser_depot(dossier)
    lj = lieu(dossier)
    lj.journal.parent.mkdir(parents=True)
    lj.journal.write_bytes(b"")
    with pytest.raises(G.JournalExisteSansManifeste):
        G.creer_journal_rejeux(lj)
    assert G.principal(["creer-journal-rejeux"], lieu_journal=lj) == 2
    out, err = capfd.readouterr()
    assert json.loads(err)["refus"] == "JournalExisteSansManifeste" and "Traceback" not in err + out
    assert not lj.manifeste.exists()


@pytest.mark.parametrize("portee,repli,classe", [
    ("Portée : repli seul", False, "ControleQuatrePorteeAutre"),           # pièce « repli seul », garde entière
    ("Portée : garde entière", True, "ControleQuatrePorteeAutre"),         # pièce « garde entière », repli
    (None, False, "ControleQuatrePorteeAbsente"),
    ("Portée : garde entière\n\nPortée : repli seul", False, "ControleQuatrePorteeAbsente"),
    ("Portée : toute la garde", False, "ControleQuatrePorteeAbsente"),
])
def test_v3_portee_de_la_piece_du_controle_4_artefacts(dossier, lancer, composition, portee, repli, classe):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, _cartes_avec_nommees())
    c = piece(dossier, "controle-portee.md", texte_controle(portee=portee))
    pr = piece(dossier, "piece.md", "pièce factice\n")
    extra = ["--repli", G.DECLENCHEURS_REPLI[1], "--piece-repli", str(pr), "--empreinte-piece-repli", sha_f(pr)] \
        if repli else []
    res = lancer(bp, cp, controle_piece=c, extra=extra)
    assert res["rapport"]["exception"]["classe"] == classe and res["entree"].ouvertures == 0


@pytest.mark.parametrize("portee,repli", [("Portée : garde entière", False), ("**Portée : garde entière.**", False),
                                          ("Portée : repli seul", True), ("**Portée : repli seul**", True)])
def test_v3_portee_de_la_piece_du_controle_4_sain(dossier, lancer, composition, portee, repli):
    preparer_journal(dossier)
    bp = ecrire_banque(dossier, composition["banque"])
    cp = ecrire_cartes(dossier, _cartes_avec_nommees())
    c = piece(dossier, "controle-portee.md", texte_controle(portee=portee))
    pr = piece(dossier, "piece.md", "pièce factice\n")
    extra = ["--repli", G.DECLENCHEURS_REPLI[1], "--piece-repli", str(pr), "--empreinte-piece-repli", sha_f(pr)] \
        if repli else []
    r = lancer(bp, cp, controle_piece=c, extra=extra)["rapport"]
    assert r["decision"] == "banque passée" and r["cartes_lues"] == (7 if repli else 94)


def test_v3_piece_du_controle_4_lue_une_seule_fois(dossier, monkeypatch):
    c = piece(dossier, "controle.md", texte_controle(programme="d" * 64))
    h = sha_f(c)
    lectures = []
    original = Path.read_bytes

    def compter(self):
        if Path(self) == c:
            lectures.append(1)
        return original(self)

    def interdit(*_a, **_k):
        raise AssertionError("seconde lecture")

    monkeypatch.setattr(Path, "read_bytes", compter)
    monkeypatch.setattr(Path, "read_text", interdit)
    monkeypatch.setattr(G, "sha256_fichier", interdit)
    G.exiger_controle_conforme(c, h, "d" * 64)
    assert len(lectures) == 1                     # une seule lecture : empreinte et analyse sur les mêmes octets
    with pytest.raises(G.ControleQuatreAbsentOuFaux):
        G.exiger_controle_conforme(c, "0" * 64, "d" * 64)
