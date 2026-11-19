"""Essais du lanceur v10 (rang 0 des épreuves v9 : branchement, éteint par défaut, de la lecture de la sélection par la génération
suivante et des tests de mort réels).

Ce que ces essais montrent (moteur simulé de l'orchestrateur épinglé, relais factices, aucun appel réel, aucune clé, aucune
dépense ; jamais `registres/` : les registres de GO sont des fichiers d'essai) :
1. **éteint = v9 à l'identique** : un essai à blanc v9 puis un essai à blanc v10 éteint, au même chemin d'essai (le premier
   renommé), comparés manifeste contre manifeste ; les seules différences admises sont des substitutions nommées (identifiant de
   run, horodatage, nom, version et empreinte du lanceur, et les empreintes qui en dérivent — contre-lecture d'essai, acte de
   gel, configuration —, chacune justifiée par l'égalité de son fichier aux substitutions précédentes près) et le bloc
   `interrupteurs_v10` (« éteints ») ; les sorties de l'orchestrateur (classement, fiches, mémoire, accords) sont égales à
   l'octet ; la configuration des interrupteurs n'est jamais ouverte éteint ; mutation : le comparateur voit un écart planté ;
2. **allumé sans GO = refus**, **allumé avec GO d'essai sans additif = refus**, et chaque garde des interrupteurs sur un cas
   sain et sur des artefacts (R5) : combinaison, configuration, ligne de GO (absente, périmètre qui ne nomme pas
   l'interrupteur, plafond autre, type, accordant, période, révocation, ligne consommée), additif (non épinglé, autre
   empreinte, non scellé, qui ne cite pas), moteur réel refusé par construction ; mutations : chaque garde retirée laisse
   passer son artefact ;
3. **allumé sous `--a-blanc`** : l'étage est joué après la génération 1 (exécuteur factice), chaque fiche y est refusée (aucun
   champ de test), la sélection scellée est servie à la génération 2, qui s'arrête sur le défaut de l'orchestrateur épinglé
   (héritage lu par `json.loads`) — constaté, rapporté, code 2 ;
4. lecture des arguments ; le reste de la v9 inchangé (sources des fonctions comparées).
"""
import copy
import datetime as dt
import difflib
import hashlib
import importlib.util
import inspect
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

RACINE = Path(__file__).resolve().parents[1]


def _charger(nom, rel):
    spec = importlib.util.spec_from_file_location(nom, RACINE / rel)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nom] = m
    spec.loader.exec_module(m)
    return m


L = _charger("lancer_course_auto_conception_v10", "scripts/lancer_course_auto_conception_v10.py")
L9 = _charger("lancer_course_auto_conception_v9_pour_v10", "scripts/lancer_course_auto_conception_v9.py")
AUJOURD_HUI = dt.date(2026, 11, 19)
ALLUMES = (L.INTERRUPTEUR_LECTURE, L.INTERRUPTEUR_TESTS_DE_MORT)
GO_ID = "GO-2026-11-19-90"


def _matiere_v3():
    p = subprocess.run(["git", "-C", str(RACINE), "show", f"{L.REF_MAIN}:{L.MATIERE[0]}"], capture_output=True)
    if p.returncode != 0 or hashlib.sha256(p.stdout).hexdigest() != L.MATIERE[1]:
        return None
    return p.stdout


avec_matiere = pytest.mark.skipif(_matiere_v3() is None, reason="matière v3 absente de refs/remotes/origin/main")


def ecrire_scelle(chemin: Path, contenu) -> str:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    return L.ecrire_scelle(chemin, contenu)


def un_run(d: Path) -> Path:
    (x,) = list((d / "runs").iterdir())
    return x


def une_sortie(d: Path) -> Path:
    (x,) = list((d / "sorties").iterdir())
    return x / "sortie"


# --- 1. éteint = v9 à l'identique -------------------------------------------------------------------------------------------


def appliquer(texte: str, subs: list) -> str:
    for ancien, nouveau, _ in subs:
        texte = texte.replace(ancien, nouveau)
    return texte


def _canon(o) -> str:
    return json.dumps(o, ensure_ascii=False, sort_keys=True, indent=1)


def _sans_duree(consommations: dict) -> dict:
    o = copy.deepcopy(consommations)
    for x in o.get("consommations") or []:
        x.pop("duree_s", None)
    return o


CLES_FIN_COMPAREES = ("code", "echec_lanceur", "ce_qui_a_ete_fait", "ecart_au_devis_v1", "plafond_arret", "releve_credits_apres",
                      "alertes_apres", "arret_au_premier_refus_pour_credit", "soupcons_de_credit")
CLES_FIN_VOLATILES = {"debut_utc": "heure de début (horloge)", "fin_utc": "heure de fin (horloge)",
                      "pid_orchestrateur": "identifiant de processus", "journaux_sha256": "journaux (chemins des runs imprimés)"}
FICHIERS_ORCHESTRATEUR_EGAUX = ("classement.json", "fiches.json", "memoire.json", "accords.json", "fusions-inachevees.json")


def comparer_eteint_a_la_v9(ab9: Path, ab10: Path) -> dict:
    """Compare l'essai à blanc v9 (`ab9`, renommé après coup) et l'essai à blanc v10 éteint (`ab10`, au chemin d'origine du
    premier). Rend {"egal": bool, "substitutions": [...], "ecarts": [...], ...} ; chaque substitution d'empreinte dérivée est
    justifiée par l'égalité de son fichier aux substitutions précédentes près (sinon écart)."""
    r9, r10 = un_run(ab9), un_run(ab10)
    d9 = json.loads((r9 / "manifeste-lanceur-depart.json").read_text(encoding="utf-8"))
    d10 = json.loads((r10 / "manifeste-lanceur-depart.json").read_text(encoding="utf-8"))
    ecarts, subs = [], []
    inter = d10.pop("interrupteurs_v10", None)
    if inter != L.ETAT_ETEINT:
        ecarts.append({"ou": "interrupteurs_v10", "lu": inter})
    subs += [(d9["id"], d10["id"], "identifiant de run (horodatage à la seconde, suffixe de version)"),
             (d9["horodatage_canonique"], d10["horodatage_canonique"], "horodatage `date -u`"),
             (d9["lanceur"]["chemin"], d10["lanceur"]["chemin"], "chemin du lanceur"),
             (d9["lanceur"]["version"], d10["lanceur"]["version"], "VERSION du lanceur"),
             (d9["lanceur"]["sha256"], d10["lanceur"]["sha256"], "empreinte du lanceur")]
    if d9["depot_travail"] != d10["depot_travail"]:
        subs.append((d9["depot_travail"]["commit"], d10["depot_travail"]["commit"],
                     "commit du dépôt de travail (d'autres agents committent entre les deux essais)"))

    def deriver(f9: Path, f10: Path, sha9: str, sha10: str, quoi: str, normaliser=None):
        t9, t10 = f9.read_text(encoding="utf-8"), f10.read_text(encoding="utf-8")
        if normaliser:
            t9, t10 = normaliser(t9), normaliser(t10)
        if appliquer(t9, subs) != t10:
            ecarts.append({"ou": quoi, "diff": list(difflib.unified_diff(appliquer(t9, subs).splitlines(), t10.splitlines(), lineterm=""))[:20]})
        if sha9 != sha10:
            subs.append((sha9, sha10, f"empreinte de {quoi} : fichier égal aux substitutions précédentes près"))

    deriver(ab9 / "pieces-d-essai" / "contre-lecture-d-essai.md", ab10 / "pieces-d-essai" / "contre-lecture-d-essai.md",
            d9["contre_lecture"]["sha256"], d10["contre_lecture"]["sha256"], "la contre-lecture d'essai (elle cite le lanceur)")
    deriver(r9 / "acte-de-gel.md", r10 / "acte-de-gel.md", d9["acte_de_gel_sha256"], d10["acte_de_gel_sha256"], "l'acte de gel")
    deriver(r9 / "configuration-orchestrateur.json", r10 / "configuration-orchestrateur.json", d9["configuration"]["sha256"],
            d10["configuration"]["sha256"], "la configuration servie à l'orchestrateur")
    v9c, v10c = d9["verification_orchestrateur"]["configuration_sha256"], d10["verification_orchestrateur"]["configuration_sha256"]
    if v9c != v10c:
        subs.append((v9c, v10c, "empreinte de configuration calculée par l'orchestrateur (fonction de la configuration, égale "
                                "aux substitutions près)"))
    t9, t10 = appliquer(_canon(d9), subs), _canon(d10)
    if t9 != t10:
        ecarts.append({"ou": "manifeste de départ", "diff": list(difflib.unified_diff(t9.splitlines(), t10.splitlines(), lineterm=""))[:40]})
    # sorties de l'orchestrateur
    s9, s10 = une_sortie(ab9) / "generation-1", une_sortie(ab10) / "generation-1"
    for nom in FICHIERS_ORCHESTRATEUR_EGAUX:
        if (s9 / nom).read_bytes() != (s10 / nom).read_bytes():
            ecarts.append({"ou": f"orchestrateur, generation-1/{nom}", "egal_a_l_octet": False})
    c9 = json.loads((s9 / "consommations.json").read_text(encoding="utf-8"))
    c10 = json.loads((s10 / "consommations.json").read_text(encoding="utf-8"))
    if _sans_duree(c9) != _sans_duree(c10):
        ecarts.append({"ou": "orchestrateur, generation-1/consommations.json hors durées"})
    # manifeste de fin
    f9 = json.loads((r9 / "manifeste-lanceur-fin.json").read_text(encoding="utf-8"))
    f10 = json.loads((r10 / "manifeste-lanceur-fin.json").read_text(encoding="utf-8"))
    if set(f9) != set(f10):
        ecarts.append({"ou": "clés du manifeste de fin", "v9": sorted(set(f9) - set(f10)), "v10": sorted(set(f10) - set(f9))})
    for k in CLES_FIN_COMPAREES:
        if appliquer(_canon(f9.get(k)), subs) != _canon(f10.get(k)):
            ecarts.append({"ou": f"manifeste de fin, {k}"})
    cout9 = {k: v for k, v in (f9.get("cout_reel") or {}).items() if k != "fichier_sha256"}
    cout10 = {k: v for k, v in (f10.get("cout_reel") or {}).items() if k != "fichier_sha256"}
    if cout9 != cout10:
        ecarts.append({"ou": "manifeste de fin, cout_reel"})
    i9, i10 = f9.get("inventaire_conservation") or {}, f10.get("inventaire_conservation") or {}
    if (i9.get("nombre_par_partie"), i9.get("erreurs")) != (i10.get("nombre_par_partie"), i10.get("erreurs")):
        ecarts.append({"ou": "manifeste de fin, inventaire (comptes)"})
    return {"egal": not ecarts, "ecarts": ecarts,
            "substitutions": [{"v9": a, "v10": b, "motif": m} for a, b, m in subs],
            "admis_en_plus": {"interrupteurs_v10": "bloc ajouté par la v10, « éteints »",
                              "manifeste_de_fin": CLES_FIN_VOLATILES,
                              "cout_reel.fichier_sha256": "le fichier de consommations porte des durées (horloge) ; égal sans elles",
                              "manifeste_de_depart_sha256": "dérivée du manifeste de départ comparé"},
            "orchestrateur_egal_a_l_octet": list(FICHIERS_ORCHESTRATEUR_EGAUX),
            "v9": {"run": r9.name, "manifeste_depart_sha256": L.sha256_fichier(r9 / "manifeste-lanceur-depart.json")},
            "v10": {"run": r10.name, "manifeste_depart_sha256": L.sha256_fichier(r10 / "manifeste-lanceur-depart.json")}}


def deux_essais_eteints(base: Path) -> tuple:
    base.mkdir(parents=True)
    assert L9.principal(["--a-blanc", str(base / "ab")]) == 0
    (base / "ab").rename(base / "ab-v9")
    assert L.principal(["--a-blanc", str(base / "ab")]) == 0
    return base / "ab-v9", base / "ab"


@pytest.fixture(scope="module")
def eteints(tmp_path_factory):
    if _matiere_v3() is None:
        pytest.skip("matière v3 absente")
    return deux_essais_eteints(tmp_path_factory.mktemp("eteints") / "c")


@avec_matiere
def test_eteint_v10_egal_a_la_v9(eteints):
    ab9, ab10 = eteints
    res = comparer_eteint_a_la_v9(ab9, ab10)
    assert res["egal"], json.dumps(res["ecarts"], ensure_ascii=False, indent=1)
    motifs = [s["motif"] for s in res["substitutions"]]
    assert any("contre-lecture" in m for m in motifs) and any("acte de gel" in m for m in motifs)
    d10 = json.loads((un_run(ab10) / "manifeste-lanceur-depart.json").read_text())
    assert d10["interrupteurs_v10"] == L.ETAT_ETEINT
    assert d10["commande"][3:4] == ["demonstrations/ideation_v8.py"] and d10["commande"][-3:] == ["1", "--moteur", "simule"]
    assert d10["verification_orchestrateur"]["montant_requis_go_usd"] == 150.0 and d10["verification_orchestrateur"]["generations"] == 1
    conf = json.loads((un_run(ab10) / "configuration-orchestrateur.json").read_text())
    assert "etage_tests_de_mort" not in conf and conf["budget"]["portee_plafond"] == "course"
    assert not (ab10 / "pieces-d-essai-interrupteurs").exists()
    assert not (une_sortie(ab10) / "etage-apres-generation-1").exists() and not (une_sortie(ab10) / "generation-2").exists()


@avec_matiere
def test_mutation_le_comparateur_voit_un_ecart_plante(eteints, tmp_path):
    """Mutation : un manifeste v10 dont une valeur a changé (la commande dit deux générations) est vu comme un écart."""
    ab9, ab10 = eteints
    copie = tmp_path / "ab"
    shutil.copytree(ab10, copie)
    m = un_run(copie) / "manifeste-lanceur-depart.json"
    d = json.loads(m.read_text())
    d["commande"][d["commande"].index("--generations") + 1] = "2"
    m.write_text(json.dumps(d), encoding="utf-8")
    res = comparer_eteint_a_la_v9(ab9, copie)
    assert not res["egal"] and any(e["ou"] == "manifeste de départ" for e in res["ecarts"])


@avec_matiere
def test_eteint_n_ouvre_jamais_la_configuration_ni_les_gardes_des_interrupteurs(tmp_path, monkeypatch):
    def interdit(*a, **k):
        raise AssertionError("garde des interrupteurs appelée alors qu'ils sont éteints")
    for nom in ("garder_interrupteurs", "lire_configuration_interrupteurs", "verifier_additif_interrupteurs", "appliquer_interrupteurs",
                "verifier_empreintes_allume", "bilan_allume"):
        monkeypatch.setattr(L, nom, interdit)
    r = L.reglages_a_blanc(tmp_path / "ab")
    r.configuration_interrupteurs = (tmp_path / "absente.json", "0" * 64)   # artefact : une configuration absente n'est pas lue
    assert L.principal([], reglages=r) == 0
    d = json.loads((un_run(tmp_path / "ab") / "manifeste-lanceur-depart.json").read_text())
    assert d["interrupteurs_v10"]["allumes"] == []


# --- 2. gardes des interrupteurs : cas sain, artefacts, mutations ---------------------------------------------------------------


def ligne_go(go_id=GO_ID, accorde="2026-11-19", typ="calcul", perimetre=None, plafond="305.0 USD", echeance="2026-11-20",
             par="Lazar", ref="R-essai") -> str:
    perimetre = perimetre if perimetre is not None else ("course d'auto-conception, interrupteurs " + ", ".join(ALLUMES))
    return f"| {go_id} | {accorde} | {typ} | {perimetre} | {plafond} | {echeance} | {par} | {ref} |"


def registre(*lignes) -> str:
    return ("# Registre d'essai\n\n| id | accordé le | type | périmètre | plafond | échéance | accordé par | référence |\n"
            "|---|---|---|---|---|---|---|---|\n" + "\n".join(lignes) + "\n")


@pytest.fixture
def garde(tmp_path):
    """Réglages minimaux pour `garder_interrupteurs` : configuration réelle des interrupteurs, préenregistrement d'essai, registre
    d'essai sain, additif d'essai sain ; pièce de départ minimale."""
    r = L.Reglages.production()
    prereg = tmp_path / "prereg.md"
    ecrire_scelle(prereg, "# préenregistrement d'essai\n")
    r.prereg = (prereg, L.sha256_fichier(prereg))
    r.interrupteurs = ALLUMES
    r.registre_interrupteurs = tmp_path / "registre.md"
    ecrire_scelle(r.registre_interrupteurs, registre(ligne_go()))
    additif = tmp_path / "additif.md"
    h = ecrire_scelle(additif, f"# additif d'essai\n{r.prereg[1]}\n{L.CONFIGURATION_INTERRUPTEURS[1]}\n" + "\n".join(ALLUMES) + "\n")
    r.additif_interrupteurs = (additif, h)
    depart = {"go_interrupteurs": GO_ID, "go_epreuve": "GO-2026-11-19-91", "go_course": "GO-2026-11-19-92"}
    return {"r": r, "depart": depart, "tmp": tmp_path}


def garder(g, reel=False):
    return L.garder_interrupteurs(g["r"], g["depart"], AUJOURD_HUI, reel)


def refus(g, mot, reel=False):
    with pytest.raises(L.Refus) as e:
        garder(g, reel)
    assert mot in str(e.value), str(e.value)
    return str(e.value)


def remplacer_registre(g, texte):
    p = g["tmp"] / f"registre-{len(list(g['tmp'].iterdir()))}.md"
    ecrire_scelle(p, texte)
    g["r"].registre_interrupteurs = p


def test_garde_cas_sain(garde):
    o = garder(garde)
    assert o["allumes"] == list(ALLUMES) and o["configuration"]["generations"] == 2
    assert o["configuration"]["montant_requis_usd"] == 305.0 and o["go"]["plafond_lu"] == 305.0
    assert o["mots_exiges_au_perimetre"] == ["autoconception", *ALLUMES]
    assert o["blocages_reels_v10"] == list(L.BLOCAGES_REELS_V10)


@pytest.mark.parametrize("demandes,mot", [((L.INTERRUPTEUR_LECTURE,), "sans tests_de_mort_reels"),
                                          ((L.INTERRUPTEUR_TESTS_DE_MORT,), "seul"),
                                          (("autre",), "inconnus"),
                                          ((L.INTERRUPTEUR_LECTURE, L.INTERRUPTEUR_LECTURE), "deux fois")])
def test_garde_combinaisons_refusees(garde, demandes, mot):
    garde["r"].interrupteurs = demandes
    refus(garde, mot)


def test_allume_sans_go_refuse(garde):
    del garde["depart"]["go_interrupteurs"]
    refus(garde, "sans ligne de GO")


@pytest.mark.parametrize("texte,mot", [
    (registre(), "0 ligne(s)"),
    (registre(ligne_go(go_id="GO-2026-11-19-89")), "0 ligne(s)"),
    (registre(ligne_go(perimetre="course d'auto-conception, interrupteur " + L.INTERRUPTEUR_LECTURE)), "périmètre"),
    (registre(ligne_go(perimetre="course d'auto-conception, lecture de la sélection et tests de mort réels")), "périmètre"),
    (registre(ligne_go(perimetre="interrupteurs " + ", ".join(ALLUMES))), "périmètre"),
    (registre(ligne_go(plafond="150 USD")), "plafond lu 150.0"),
    (registre(ligne_go(typ="décision")), "type"),
    (registre(ligne_go(par="la mère")), "accordé par"),
    (registre(ligne_go(accorde="2026-11-20", echeance="2026-11-21")), "hors de sa période"),
    (registre(ligne_go(), f"| GO-2026-11-19-93 | 2026-11-19 | révocation | révoque {GO_ID} | 0 USD | 2026-11-19 | Lazar | r |"),
     "révoqué"),
])
def test_go_artefacts_refuses(garde, texte, mot):
    remplacer_registre(garde, texte)
    refus(garde, mot)


def test_go_ligne_consommee_ou_de_l_epreuve_refusee(garde):
    garde["depart"]["go_interrupteurs"] = L.LIGNES_GO_CONSOMMEES[0]
    refus(garde, "consommée")
    garde["depart"]["go_interrupteurs"] = garde["depart"]["go_epreuve"]
    refus(garde, "consommée")


def test_registre_d_essai_absent_ou_non_scelle_refuse(garde):
    garde["r"].registre_interrupteurs = None
    refus(garde, "registre de GO d'essai")
    p = garde["tmp"] / "registre-non-scelle.md"
    p.write_text(registre(ligne_go()), encoding="utf-8")
    garde["r"].registre_interrupteurs = p
    refus(garde, "registre de GO d'essai")


def test_allume_avec_go_d_essai_sans_additif_refuse(garde):
    garde["r"].additif_interrupteurs = L.ADDITIF_INTERRUPTEURS         # la valeur de production : à venir
    assert L.ADDITIF_INTERRUPTEURS == (None, None)
    refus(garde, "non épinglé (à venir)")


def test_additif_artefacts_refuses(garde):
    chemin, h = garde["r"].additif_interrupteurs
    garde["r"].additif_interrupteurs = (chemin, "1" * 64)
    refus(garde, "d'empreinte")
    garde["r"].additif_interrupteurs = (garde["tmp"] / "absent.md", h)
    refus(garde, "absent")
    nu = garde["tmp"] / "additif-nu.md"
    nu.write_text(chemin.read_text(encoding="utf-8"), encoding="utf-8")
    garde["r"].additif_interrupteurs = (nu, L.sha256_fichier(nu))
    refus(garde, "non scellé")
    for retire in (garde["r"].prereg[1], L.CONFIGURATION_INTERRUPTEURS[1], L.INTERRUPTEUR_TESTS_DE_MORT):
        p = garde["tmp"] / f"additif-sans-{retire[:8]}.md"
        hp = ecrire_scelle(p, chemin.read_text(encoding="utf-8").replace(retire, "[retiré]"))
        garde["r"].additif_interrupteurs = (p, hp)
        refus(garde, "ne cite pas")


def _configuration_variante(g, modifier) -> None:
    o = json.loads((RACINE / L.CONFIGURATION_INTERRUPTEURS[0]).read_text(encoding="utf-8"))
    modifier(o)
    p = g["tmp"] / f"conf-{len(list(g['tmp'].iterdir()))}.json"
    h = ecrire_scelle(p, o)
    g["r"].configuration_interrupteurs = (p, h)


@pytest.mark.parametrize("modifier,mot", [
    (lambda o: o.update(generations=1), "≥ 2"),
    (lambda o: o.update(generations=True), "≥ 2"),
    (lambda o: o["budget"].update(portee_plafond="course"), "par_generation"),
    (lambda o: o["orchestrateur"].update(lanceur_allume="demonstrations/ideation_v8.py"), "orchestrateur"),
    (lambda o: o["etage_tests_de_mort"].pop("correspondance"), "incomplet"),
    (lambda o: o["etage_tests_de_mort"]["correspondance"].pop("test_de_mort"), "correspondance"),
    (lambda o: o["etage_tests_de_mort"].update(plafond_etage_usd=0), "plafond_etage_usd"),
    (lambda o: o["etage_tests_de_mort"].update(environnement_permis=["GO_ID", "MON_API_KEY"]), "aucun nom de clé"),
])
def test_configuration_des_interrupteurs_artefacts(garde, modifier, mot):
    _configuration_variante(garde, modifier)
    refus(garde, mot)


def test_configuration_des_interrupteurs_autre_empreinte_ou_non_scellee(garde):
    chemin, _h = garde["r"].configuration_interrupteurs
    garde["r"].configuration_interrupteurs = (chemin, "2" * 64)
    refus(garde, "d'empreinte")
    nu = garde["tmp"] / "conf-nue.json"
    nu.write_bytes(Path(chemin).read_bytes())
    garde["r"].configuration_interrupteurs = (nu, L.sha256_fichier(nu))
    refus(garde, "non scellée")


def test_configuration_des_interrupteurs_du_depot_scellee_et_epinglee():
    p = RACINE / L.CONFIGURATION_INTERRUPTEURS[0]
    assert L.scelle(p) and L.sha256_fichier(p) == L.CONFIGURATION_INTERRUPTEURS[1]
    o = json.loads(p.read_text(encoding="utf-8"))
    assert o["etage_tests_de_mort"]["tranche"] == L.MARQUEUR_A_REMPLIR == o["etage_tests_de_mort"]["liste_blanche"]


def test_moteur_reel_allume_refuse_par_construction_meme_avec_go_et_additif(garde):
    lu = []
    garde["r"].lire_main = lambda chemin: (lu.append(chemin) or (registre(ligne_go()).encode("utf-8"), "c" * 40))
    msg = refus(garde, "refusé par construction dans la v10", reel=True)
    assert lu == ["registres/go.md"]                          # le registre de main, lu par l'injection (aucun `registres/` ouvert)
    for b in L.BLOCAGES_REELS_V10:
        assert b in msg


def test_moteur_reel_allume_sans_go_refuse_avant_le_registre(garde):
    garde["r"].lire_main = lambda chemin: pytest.fail("registre lu alors que la pièce ne nomme aucune ligne")
    del garde["depart"]["go_interrupteurs"]
    refus(garde, "sans ligne de GO", reel=True)


def test_moteur_reel_allume_go_sans_les_interrupteurs_refuse(garde):
    garde["r"].lire_main = lambda chemin: (registre(ligne_go(perimetre="course d'auto-conception")).encode("utf-8"), "c" * 40)
    refus(garde, "périmètre", reel=True)


def test_mutation_go_non_verifie_attrapee(garde, monkeypatch):
    remplacer_registre(garde, registre())
    refus(garde, "0 ligne(s)")
    monkeypatch.setattr(L, "verifier_go", lambda *a, **k: {"id": "mute"})
    assert garder(garde)["go"]["id"] == "mute"                 # sans la garde, l'artefact passe : l'essai a des dents


def test_mutation_additif_non_verifie_attrapee(garde, monkeypatch):
    garde["r"].additif_interrupteurs = (None, None)
    refus(garde, "non épinglé")
    monkeypatch.setattr(L, "verifier_additif_interrupteurs", lambda *a, **k: {"chemin": "mute"})
    assert garder(garde)["additif"]["chemin"] == "mute"


def test_mutation_combinaison_non_verifiee_attrapee(garde, monkeypatch):
    garde["r"].interrupteurs = (L.INTERRUPTEUR_LECTURE,)
    refus(garde, "sans tests_de_mort_reels")
    monkeypatch.setattr(L, "verifier_combinaison", lambda allumes: None)
    remplacer_registre(garde, registre(ligne_go(perimetre="course d'auto-conception " + L.INTERRUPTEUR_LECTURE, plafond="305.0 USD")))
    p = garde["tmp"] / "additif-lecture.md"
    h = ecrire_scelle(p, f"{garde['r'].prereg[1]}\n{L.CONFIGURATION_INTERRUPTEURS[1]}\n{L.INTERRUPTEUR_LECTURE}\n")
    garde["r"].additif_interrupteurs = (p, h)
    assert garder(garde)["allumes"] == [L.INTERRUPTEUR_LECTURE]


# --- 2 bis. de bout en bout par `principal` : refus avant toute écriture ------------------------------------------------------


@avec_matiere
def test_principal_allume_moteur_reel_refuse_sans_rien_ecrire(tmp_path):
    r = L.reglages_a_blanc(tmp_path / "ab", ALLUMES)
    texte = r.registre_interrupteurs.read_text(encoding="utf-8")
    r.moteur, r.lire_main = "reel", (lambda chemin: (texte.encode("utf-8"), "c" * 40))
    assert L.principal(["--allumer-lecture-selection", "--allumer-tests-de-mort-reels"], reglages=r) == 2
    assert not (tmp_path / "ab" / "runs").exists() and not (tmp_path / "ab" / "sorties").exists()
    r.additif_interrupteurs = L.ADDITIF_INTERRUPTEURS
    assert L.principal([], reglages=r) == 2
    assert not (tmp_path / "ab" / "runs").exists()


@avec_matiere
def test_principal_allume_a_blanc_sans_go_refuse_sans_rien_ecrire(tmp_path):
    r = L.reglages_a_blanc(tmp_path / "ab", ALLUMES)
    o = json.loads(r.piece_de_depart.read_text(encoding="utf-8"))
    o.pop("go_interrupteurs")
    p = tmp_path / "piece-sans-go.json"
    ecrire_scelle(p, o)
    r.piece_de_depart = p
    assert L.principal([], reglages=r) == 2
    assert not (tmp_path / "ab" / "runs").exists()


def test_arguments():
    assert L.principal(["--allumer-autre", "--a-blanc", "/nulle-part-x"]) == 2
    assert L.principal(["--a-blanc", "/nulle-part-x", "--allumer-lecture-selection"]) == 2
    assert L.principal(["--allumer-tests-de-mort-reels", "--decouper", "a", "b"]) == 2
    assert set(L.OPTIONS_INTERRUPTEURS.values()) == set(L.INTERRUPTEURS)


# --- 3. allumé sous --a-blanc (moteur simulé) ---------------------------------------------------------------------------------


@avec_matiere
def test_essai_a_blanc_allume_defaut_d_orchestrateur_a_la_generation_2(tmp_path):
    d = tmp_path / "ab"
    assert L.principal(["--allumer-lecture-selection", "--allumer-tests-de-mort-reels", "--a-blanc", str(d)]) == 2
    run = un_run(d)
    dep = json.loads((run / "manifeste-lanceur-depart.json").read_text())
    fin = json.loads((run / "manifeste-lanceur-fin.json").read_text())
    i = dep["interrupteurs_v10"]
    assert i["allumes"] == list(ALLUMES) and i["configuration"]["montant_requis_usd"] == 305.0
    assert i["go"]["source"]["registre"].startswith(str(d)) and "registres/go.md" not in i["go"]["source"]["registre"]
    assert i["etage"]["fiches_testables"] is False
    assert dep["commande"][3] == "demonstrations/ideation_v59.py" and dep["commande"][-3:] == ["2", "--moteur", "simule"]
    assert dep["verification_orchestrateur"]["montant_requis_go_usd"] == 305.0
    conf = json.loads((run / "configuration-orchestrateur.json").read_text())
    assert conf["budget"]["portee_plafond"] == "par_generation" and conf["etage_tests_de_mort"]["tranche"].startswith(str(d))
    b = fin["interrupteurs_v10"]["bilan_orchestrateur"]
    assert b["version"] == "course-2-generation-v59" and b["scelle"]
    assert b["generations_jouees"] == 1 and b["arret"].startswith("JSONDecodeError")
    (g1,) = b["lignes"]
    assert g1["etage_joue"] and g1["candidates"] == 2 and g1["refusees_a_l_etage"] == 2 and g1["retenues"] == 0
    assert g1["heritage_servi_a_la_suivante"] is True
    assert fin["interrupteurs_v10"]["couts_par_generation"]["2"]["lisible"]   # la génération 2 a commencé
    sortie = une_sortie(d)
    assert L.scelle(sortie / "etage-apres-generation-1" / "selection-entre-generations-v57.json")
    assert fin["code"] == 2 and L.scelle(run / "inventaire-conservation.json")


# --- 4. le reste de la v9, inchangé ------------------------------------------------------------------------------------------


CHANGEES_V10 = {"executer", "reglages_a_blanc", "principal", "ecrire_registre_derive", "verifier_course_jamais_lancee_ou_closes_admises",
                "Reglages"}
RETIREES_DE_EXECUTER = {
    '    base = [r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, "--course-2", str(chemin_conf), str(sortie), "--generations", "1"]',
    '    if verif_json is None or verif_json.get("montant_requis_go_usd") != PLAFOND_ARRET_USD:',
    '                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-auto-conception-v9"), parts, depart)'}


def test_le_reste_de_la_v9_inchange():
    for nom, objet in vars(L9).items():
        if (inspect.isfunction(objet) or inspect.isclass(objet)) and getattr(objet, "__module__", None) == L9.__name__ \
                and nom not in CHANGEES_V10:
            assert inspect.getsource(getattr(L, nom)) == inspect.getsource(objet), nom
    for nom in ("PIECES", "EMPREINTES_ORCHESTRATEUR", "COMMIT_ORCHESTRATEUR", "LANCEUR_ORCHESTRATEUR", "PLAFOND_ARRET_USD",
                "PREREG_SHA256", "ADDITIF", "ADDITIF_SHA256", "CONTRE_LECTURE", "DECLARATION_RELAIS", "PIECE_DE_DEPART",
                "EPREUVE_REELLE", "RELEVE_PRIX", "RELEVE_CREDITS", "MATIERE", "HAUT_DEVIS_V2I_USD", "DOSSIER_CONSERVATION_NOM",
                "COURSES_CLOSES_ADMISES", "LIGNES_GO_CONSOMMEES", "NOMS_PERMIS", "NOMS_DE_CLE", "PROGRAMMES_RELAIS"):
        assert getattr(L, nom) == getattr(L9, nom), nom
    assert L.DOSSIER_SORTIES == Path("/home/user/sorties-course-auto-conception-v10") and L.SUFFIXE_RUN == "-course-auto-conception-v10"
    assert set(L.SUFFIXES_DEJA_LANCEE) == {f"-course-auto-conception-v{k}" for k in range(1, 11)}
    assert L.SORTIES_AUTRES_VERSIONS == tuple(Path(f"/home/user/sorties-course-auto-conception-v{k}") for k in range(1, 10))


def test_executer_v10_ne_retire_de_la_v9_que_trois_lignes():
    """Les lignes de la v9 que la v10 retire de `executer` : la commande à une génération (paramétrée), le montant de la
    vérification (paramétré) et le nom du dossier d'alerte ; tout le reste est ajouté, et chaque ajout porte « allume » ou un
    nom de la v10."""
    a = inspect.getsource(L9.executer).splitlines()
    b = inspect.getsource(L.executer).splitlines()
    retirees = {x[1:] for x in difflib.unified_diff(a, b, lineterm="", n=0) if x.startswith("-") and not x.startswith("---")}
    ajoutees = [x[1:] for x in difflib.unified_diff(a, b, lineterm="", n=0) if x.startswith("+") and not x.startswith("+++")]
    assert retirees == RETIREES_DE_EXECUTER
    jetons = ("allume", "interrupteurs", "montant_attendu", "lanceur_orch", "n_gen", "VARIABLE_MACHINE_JETABLE", "if reel:",
              "raise Refus(", "env[", "depasse = depasse", "except Exception as exc", "bilan[\"erreur_bilan_interrupteurs\"]",
              "echec = echec or", "try:", "alerte-credits-auto-conception-v10", "else (LANCEUR_ORCHESTRATEUR, 1)", "base = [",
              "\"jamais posée en moteur réel\"}", "lanceur en moteur simulé", "!= montant_attendu")
    hors = [x for x in ajoutees if not any(j in x for j in jetons)]
    assert not hors, hors
