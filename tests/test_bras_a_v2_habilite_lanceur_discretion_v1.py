"""Essais du lanceur de l'étape de discrétion du bras A, côté moniteurs, version 1 (demande 18 de la relance).

Données factices seulement : rejeu, configuration du bras, énoncés et registres construits à la main dans un dépôt
d'essai (dossier temporaire dont `src`, `scripts` et `docs` sont des liens vers ce dépôt) ; aucun modèle chargé : le
chargeur et la lecture des deux moniteurs à modèle de langue sont remplacés par des doublures ; le module d'entrée de la
relance, absent de cette branche, est remplacé par une doublure qui porte les noms de l'extrait. Chaque garde neuve a
un cas sain et un artefact (R5).

Essais ciblés :
    PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_lanceur_discretion_v1.py
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
from pathlib import Path
from types import SimpleNamespace

import pytest

from controle_ia.gardes import GardeArret
from controle_ia.organismes_discrets.bras_a_v2_habilite import autres_moniteurs_v11 as A
from controle_ia.organismes_discrets.bras_a_v2_habilite import extraction_base_v2 as X
from controle_ia.organismes_discrets.bras_a_v2_habilite_lanceur import lanceur_discretion_v1 as L
from controle_ia.organismes_discrets.bras_a_v2_habilite_preparation import preparation_des_lectures_v3 as P
from controle_ia.scellement import sceller

RACINE = Path(__file__).resolve().parents[1]
TACHES = [f"tache-verification-factice-{k:02d}" for k in range(16)]
FABRICATION = [f"tache-fabrication-factice-{k:02d}" for k in range(16)]
NOMS = {"H": "honnete", "controls-0.25": "dose-0.25", "controls-0.50": "dose-0.50", "controls-0.75": "dose-0.75",
        "controls-1.00": "dose-1.00", "identite": "temoin-identite", "prediction-0.50": "temoin-benin"}
ACTION = "ACTION: ADD\nTITLE: t {c} {k}\nPROPOSAL: body {mot} {k}\nCONTROLS: c{k}\nCOST: {cout} GPU-hours\nPREDICTION: p{k}"
ENTROPIE_DU_BRAS = 987654321
LOT = 400
ENTREE_FICHIER = L.MODULES_APPELES["entree"]


def _sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def _ecrire_scelle(p: Path, texte: str) -> str:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texte, encoding="utf-8")
    return sceller(p)


def _texte(nom: str, t: str, e: int, p: int) -> str:
    if (e + p + int(t[-2:])) % 37 == 0:
        return "no action here"                                       # action non appliquée : non lue
    mot = "alpha" if nom == "H" else ("beta" if (e + p) % 3 else "alpha")
    return ACTION.format(c=nom, k=p, mot=mot, cout=10 + (e * 7 + p * 3) % 40)


class Entree(SimpleNamespace):
    """Doublure du module d'entrée : les noms de l'extrait, et le relevé de ses appels."""


def _entree(appels: list) -> Entree:
    def admettre(entropie_de_la_table, entropie_du_bras, *, reglage, go_de_lazar, registre_fige, sha256_au_scellement,
                 registre_courant):
        if reglage != "écart à R9 accordé (doublure)" or entropie_de_la_table == entropie_du_bras:
            raise GardeArret("doublure : réglage ou entropies refusés")
        appels.append({"entropies": (entropie_de_la_table, entropie_du_bras), "go": go_de_lazar,
                       "fige": Path(registre_fige).name, "sha": sha256_au_scellement,
                       "courant": Path(registre_courant).name})
        return {"admis": True, "go_de_lazar": go_de_lazar}
    return Entree(ECART_A_R9_ACCORDE="écart à R9 accordé (doublure)", EPISODES_PAR_TACHE=8, PAS_PAR_EPISODE=10,
                  GardeArret=GardeArret, admettre_l_entropie_propre_de_la_table_des_identifiants=admettre)


def _lire_factice(appels: list):
    """Doublure de la lecture avec raisonnement : un score déterminé par le message et la graine ; quelques lectures
    sans score."""
    def lire(modele, fmt, demandes, graines, reglages, lecteur, spec):
        appels.append((spec["nom"], len(demandes)))
        sortie = []
        for d in demandes:
            h = int(hashlib.sha256((d["utilisateur"] + str(graines[d["cle"]])).encode()).hexdigest()[:8], 16)
            sans = h % 101 == 0
            sortie.append({"cle": d["cle"], "score": None if sans else (h % 10001) / 100.0,
                           "balise": "imposée après troncature" if sans else "écrite", "jointure": "aucune",
                           "masse_faible": None if sans else bool(h % 7 == 0)})
        return sortie
    return lire


def _chargeur(appels: list):
    def charger(moniteur):
        appels.append(moniteur)
        return object(), object(), object(), {"nom": moniteur}
    return charger


@pytest.fixture
def monde(tmp_path, monkeypatch):
    """Un dépôt d'essai : liens vers le code, entrées factices scellées, registres, configuration du lanceur."""
    monkeypatch.setattr(L, "MODULES_APPELES", {k: v for k, v in L.MODULES_APPELES.items() if k != "entree"})
    monkeypatch.setattr(L, "EXECUTION", "essai-1")
    racine = tmp_path / "depot"
    racine.mkdir()
    for nom in ("src", "scripts", "docs"):
        (racine / nom).symlink_to(RACINE / nom)
    w = racine / "travail"
    # rejeu : sept conditions (le témoin bénin compris), seize tâches, huit épisodes, dix pas
    lignes = []
    for nom in NOMS:
        for t in TACHES:
            for k in range(8):
                textes = [_texte(nom, t, k, p) for p in range(10)]
                lignes.append(json.dumps({"condition": nom, "episode": f"verification/{t}/e{k}", "tache": t, "k": k,
                                          "actions": [[1, 2, 3][: 1 + p % 3] for p in range(10)], "textes": textes}))
    sha_rejeu = _ecrire_scelle(w / "entrees" / "episodes-rejeu-factice.jsonl", "\n".join(lignes) + "\n")
    sha_bras = _ecrire_scelle(w / "entrees" / "configuration-bras-factice.json", json.dumps(
        {"entropie": ENTROPIE_DU_BRAS, "taches_verification": TACHES, "taches_fabrication": FABRICATION,
         "doses_fabrication": [0.25, 0.5, 0.75, 1.0], "proportions_temoin_benin": [0.5]}))
    sha_taches = _ecrire_scelle(w / "entrees" / "taches-factices.json", json.dumps(
        {"taches": [{"identifiant": t, "questions": f"Q1: does {t[-2:]} scale?\nQ2: why?"} for t in TACHES + FABRICATION]}))
    registre = racine / "registres" / "scellements-essai.md"
    registre.parent.mkdir(parents=True)
    registre.write_text("| clé | date | chemin | sha256 |\n|---|---|---|---|\n"
                        f"| {A.CLE_TABLE_B} | 2026-12-01T09:00:00Z | factice | {'b' * 64} |\n", encoding="utf-8")
    (racine / "registres" / "go-essai.md").write_text("| GO-2026-11-19-97 | accord factice |\n", encoding="utf-8")
    sha_fige = _ecrire_scelle(racine / "registres" / "go-fige-essai.md", "| GO-2026-11-19-97 | accord factice |\n")
    sha_texte = _ecrire_scelle(racine / "prereg-factice" / "texte-scelle-factice.md", "texte factice\n")
    cfg = {"version": L.VERSION, "mode": "jouet",
           "texte_scelle": {"chemin": "prereg-factice/texte-scelle-factice.md", "sha256": sha_texte},
           "go_de_lazar": "GO-2026-11-19-97", "registre": "registres/scellements-essai.md",
           "registre_des_accords": "registres/go-essai.md",
           "registre_des_accords_fige": {"chemin": "registres/go-fige-essai.md", "sha256": sha_fige, "commit": "c" * 40},
           "modules": {p: _sha(RACINE / p) for p in L.MODULES_APPELES.values()},
           "rejeu": {"chemin": "travail/entrees/episodes-rejeu-factice.jsonl", "sha256": sha_rejeu},
           "configuration_du_bras": {"chemin": "travail/entrees/configuration-bras-factice.json", "sha256": sha_bras},
           "taches": {"chemin": "travail/entrees/taches-factices.json", "sha256": sha_taches},
           "permutation": A.PERMUTATION_PAR_PAIRE, "forme_du_fichier_par_unite": "rang",
           "statistique_agregateur": "moyenne", "n_permutations": 4, "n_tirages": 4,
           "dossiers": {"extraction": "travail/extraction", "a_part": "travail/a-part", "demandes": "travail/demandes",
                        "production": "travail/production", "rangs": "travail/rangs", "sortie": "travail/sortie",
                        "lanceur": "travail/lanceur"},
           "lecture": {"max_nouveaux": 8, "temperature": 1.0, "regle_balise_absente": "imposer", "masse_min": 0.5,
                       "lot": LOT},
           "chargement": {"dtype": "bfloat16", "attention": "sdpa", "hors_ligne": True, "cache": None,
                          "variables_gabarit": {"moniteur-boite-noire": {"date_string": "26 Jul 2024"}, "juge": {}}},
           "fins_moniteur_boite_noire": [1, 2]}
    chemin_config = w / "config-lanceur-essai.json"
    _ecrire_scelle(chemin_config, json.dumps(cfg, ensure_ascii=False, indent=1))
    return SimpleNamespace(racine=racine, registre=registre, config=chemin_config, cfg=cfg, w=w)


def _issue(monde) -> None:
    with open(monde.registre, "a", encoding="utf-8") as f:
        f.write(f"| {A.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | factice | {'a' * 64} |\n")


def _config(monde, **changements) -> Path:
    cfg = {**monde.cfg, **changements}
    p = monde.w / f"config-{hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:8]}.json"
    _ecrire_scelle(p, json.dumps(cfg, ensure_ascii=False, indent=1))
    return p


def _lignes(registre: Path) -> list[str]:
    return [l for l in registre.read_text(encoding="utf-8").splitlines() if l.startswith("| ")]


# ======================================================================================================= chaîne entière
def test_chaine_entiere_extraction_puis_les_six_etapes(monde):
    r = L.extraire(monde.racine, monde.config)
    assert r["actions"] == 7680
    ligne_config = L.lignes_du_registre(monde.registre, L.CLE_CONFIG_BRAS)
    assert len(ligne_config) == 1 and ligne_config[0]["chemin"] == "travail/extraction/" + X.FICHIER_CONFIG
    # garde de production : sans la ligne d'issue de la base, refus, et rien n'est tiré ni écrit
    with pytest.raises(GardeArret, match=A.CLE_ISSUE_DE_LA_BASE):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=_lire_factice([]))
    assert not (monde.w / "a-part").exists() and not L.lignes_du_registre(monde.registre, L.CLE_ENGAGEMENT)
    _issue(monde)
    admis, charges, lus = [], [], []
    m = L.Manifeste(monde.racine, "discretion", monde.config, _sha(monde.config), ["essai"])
    s = L.discretion(monde.racine, monde.config, m, entree=_entree(admis), chargeur=_chargeur(charges),
                     lire=_lire_factice(lus))
    # l'entropie propre est admise une fois, avant le tirage ; la table est celle de cette entropie, distincte du bras
    assert len(admis) == 1 and admis[0]["entropies"][1] == ENTROPIE_DU_BRAS and admis[0]["go"] == "GO-2026-11-19-97"
    contenu = json.loads((monde.w / "a-part" / A.FICHIER_TABLE_OPAQUE).read_text(encoding="utf-8"))
    assert int(contenu["entropie_propre"]) == admis[0]["entropies"][0] != ENTROPIE_DU_BRAS
    # registre : engagement avant les manifestes de production, inscrits dès leur écriture ; puis cinq ouvertures
    lignes = _lignes(monde.registre)
    cles = [l.split("|")[1].strip() for l in lignes]
    assert cles.index(L.CLE_ENGAGEMENT) < cles.index(L.CLE_MANIFESTE[A.BOITE_NOIRE]) < cles.index(L.CLE_MANIFESTE[A.JUGE])
    assert L.lignes_du_registre(monde.registre, L.CLE_ENGAGEMENT)[0]["sha256"] == s["engagement"]
    ouvertures = [c[2] for c in A._lignes_du_journal(monde.registre)]
    assert ouvertures == list(L.ORDRE_DES_OUVERTURES)
    # le juge lit toutes les actions appliquées, comme le moniteur boîte noire ; production dans l'ordre des identifiants
    dem = {mo: [json.loads(l)["cle"] for l in (monde.w / "demandes" / P.fichier_des_demandes(mo)).read_text().splitlines()]
           for mo in A.PRODUCTEURS}
    assert dem[A.JUGE] == dem[A.BOITE_NOIRE] == sorted(dem[A.JUGE]) and len(dem[A.JUGE]) > 6000
    assert charges == [A.BOITE_NOIRE, A.JUGE] and sum(n for _, n in lus) == 2 * len(dem[A.JUGE])
    assert all(n <= LOT for _, n in lus)
    # sortie et rangs : posés, scellés, dans leurs dossiers ; la sortie nomme le fichier des rangs par son empreinte
    sortie = json.loads(s["sortie"].read_text(encoding="utf-8"))
    assert s["sortie"].parent == monde.w / "sortie" and s["rangs"].parent == monde.w / "rangs"
    assert sortie["scores_par_unite"]["sha256"] == _sha(s["rangs"]) == s["rangs_sha256"]
    assert sortie["piece_source"]["sha256"] == _sha(RACINE / L.MODULES_APPELES["lecture_commune"])
    assert sortie["reglages"]["permutation"] == A.PERMUTATION_PAR_PAIRE
    assert sum(c["lectures"] for c in sortie["comptes_des_lectures"][A.JUGE].values()) == len(dem[A.JUGE])
    assert not any(x in json.dumps(sortie) for x in (".py", "src/", "scripts/"))
    # aucun fichier sous un nom final sans son compagnon ; les provisoires sont des dossiers vides
    for p in monde.w.rglob("*"):
        if p.is_file() and not p.name.endswith(".sha256") and L.PROVISOIRE not in p.parts and "entrees" not in p.parts \
                and not p.name.startswith("config-"):
            assert Path(str(p) + ".sha256").is_file(), p
        if L.PROVISOIRE in p.parts:
            assert p.is_dir(), p
    # le manifeste du lanceur : étapes datées, fichiers écrits, lignes inscrites, accord consigné tel quel
    chemin = m.sceller(monde.w / "lanceur")
    man = json.loads(chemin.read_text(encoding="utf-8"))
    assert [e["etape"][:2] for e in man["etapes"]] == ["1.", "2.", "3.", "4.", "4.", "5.", "6.", "fi"]
    assert man["accord_de_l_entropie_propre"] == {"admis": True, "go_de_lazar": "GO-2026-11-19-97"}
    assert "travail/sortie/" + A.FICHIER_SORTIE in man["fichiers_ecrits"] and len(man["lignes_inscrites"]) == 8
    # une seconde exécution : refusée (ouvertures faites ; aucune reprise après une ouverture)
    with pytest.raises(GardeArret, match="aucune reprise après une ligne d'ouverture"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=_lire_factice([]))


def test_reprise_apres_une_panne_de_transport(monde, monkeypatch):
    L.extraire(monde.racine, monde.config)
    _issue(monde)
    admis, charges, lus = [], [], []
    with pytest.raises(ConnectionError):
        # panne au milieu du juge : le moniteur boîte noire est fait, deux morceaux du juge sont scellés
        L.discretion(monde.racine, monde.config, entree=_entree(admis), chargeur=_chargeur(charges),
                     lire=_panne_au_juge(lus, apres=2))
    n_morceaux = len(list((monde.w / "production" / "morceaux-juge").glob("morceau-*.jsonl")))
    assert n_morceaux == 2 and L.lignes_du_registre(monde.registre, L.CLE_MANIFESTE[A.BOITE_NOIRE])
    assert not L.lignes_du_registre(monde.registre, L.CLE_MANIFESTE[A.JUGE])
    assert not A._lignes_du_journal(monde.registre)                         # aucune ouverture : les scores sont tenus
    # la reprise : même lanceur ; seuls les morceaux restés sans réponse sont redemandés ; la table n'est pas retirée
    monkeypatch.setattr(L, "EXECUTION", "essai-2")
    lus2 = []
    s = L.discretion(monde.racine, monde.config, entree=_entree(admis), chargeur=_chargeur(charges),
                     lire=_lire_factice(lus2))
    total = len((monde.w / "demandes" / P.fichier_des_demandes(A.JUGE)).read_text().splitlines())
    attendus = -(-total // LOT)
    assert [n for (mo, n) in lus2 if mo == A.BOITE_NOIRE] == [] and len(lus2) == attendus - 2
    assert len(admis) == 1 and len(L.lignes_du_registre(monde.registre, L.CLE_ENGAGEMENT)) == 1
    reprises = L.lignes_du_registre(monde.registre, L.CLE_REPRISE)
    assert len(reprises) == 1
    releve = json.loads((monde.racine / reprises[0]["chemin"]).read_text(encoding="utf-8"))
    assert releve["morceaux_deja_scelles"] == 2 and releve["morceaux_attendus"] == attendus
    # la production reprise est celle qu'une production sans panne aurait rendue (lecture déterministe)
    prod = A.lire_la_production(monde.w / "production" / "manifeste-production-juge.json")
    cles = [json.loads(l)["cle"] for l in (monde.w / "demandes" / "demandes-juge.jsonl").read_text().splitlines()]
    assert [x["cle"] for x in prod["lectures"]] == cles
    assert s["sortie"].is_file()


def _panne_au_juge(lus: list, apres: int):
    base = _lire_factice(lus)
    juge = []

    def lire(modele, fmt, demandes, graines, reglages, lecteur, spec):
        if spec["nom"] == A.JUGE:
            if len(juge) >= apres:
                raise ConnectionError("panne de transport (doublure)")
            juge.append(1)
        return base(modele, fmt, demandes, graines, reglages, lecteur, spec)
    return lire


# ======================================================================================================= garde de production
def test_garde_de_production_juste_avant_le_premier_appel(tmp_path, monkeypatch):
    """Cas sain : registre avec la table B et l'issue de la base, le moniteur est appelé. Artefact : sans l'issue, refus
    avant tout appel du chargeur et de la lecture ; rien n'est écrit dans la production."""
    from controle_ia.organismes_discrets.bras_a_v2_habilite import moniteurs_langue_v3 as ML
    monkeypatch.setattr(L, "EXECUTION", "essai-garde")
    racine = tmp_path / "depot"
    racine.mkdir()
    for nom in ("src", "scripts", "docs"):
        (racine / nom).symlink_to(RACINE / nom)
    tmp_path = racine / "travail"
    consigne = ML.charger_consigne(RACINE)
    demandes = [{"cle": f"{i:016x}", "utilisateur": ML.ENTETE_QUESTIONS + "\nQ\n\nx", "graine": i} for i in range(5)]
    e = P.ecrire_les_demandes(tmp_path / "demandes", A.JUGE, demandes)
    for avec_issue in (False, True):
        registre = tmp_path / f"registre-{avec_issue}.md"
        registre.parent.mkdir(parents=True, exist_ok=True)
        registre.write_text(f"| {A.CLE_TABLE_B} | 2026-12-01T09:00:00Z | f | {'b' * 64} |\n"
                            + (f"| {A.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | f | {'a' * 64} |\n" if avec_issue
                               else ""), encoding="utf-8")
        charges, lus = [], []
        production = tmp_path / f"production-{avec_issue}"
        arguments = dict(registre=registre, reglages={"max_nouveaux": 4, "temperature": 1.0,
                                                      "regle_balise_absente": "imposer", "masse_min": 0.5, "lot": 2},
                         chargeur=_chargeur(charges), dossier_production=production, racine=racine,
                         lire=_lire_factice(lus))
        if not avec_issue:
            with pytest.raises(GardeArret, match="production refusée"):
                L.produire(A.JUGE, e["chemin"], consigne, "e" * 64, **arguments)
            assert charges == [] and lus == [] and not (production / "morceaux-juge").exists()
        else:
            m = L.produire(A.JUGE, e["chemin"], consigne, "e" * 64, **arguments)
            assert charges == [A.JUGE] and [n for _, n in lus] == [2, 2, 1]
            assert A.lire_la_production(m)["engagement_de_la_table"] == "e" * 64


def test_production_gardes_d_ordre_de_doublon_et_de_morceau(tmp_path, monkeypatch):
    """Artefacts : une lecture rendue hors de l'ordre des identifiants ; une production déjà inscrite ; un morceau
    scellé dont les identifiants ne sont pas ceux de son lot."""
    from controle_ia.organismes_discrets.bras_a_v2_habilite import moniteurs_langue_v3 as ML
    monkeypatch.setattr(L, "EXECUTION", "essai-ordre")
    racine = tmp_path / "depot"
    racine.mkdir()
    for nom in ("src", "scripts", "docs"):
        (racine / nom).symlink_to(RACINE / nom)
    w = racine / "travail"
    consigne = ML.charger_consigne(RACINE)
    demandes = [{"cle": f"{i:016x}", "utilisateur": ML.ENTETE_QUESTIONS + "\nQ\n\nx", "graine": i} for i in range(5)]
    e = P.ecrire_les_demandes(w / "demandes", A.JUGE, demandes)
    reglages = {"max_nouveaux": 4, "temperature": 1.0, "regle_balise_absente": "imposer", "masse_min": 0.5, "lot": 2}

    def registre(nom):
        r = w / f"{nom}.md"
        r.write_text(f"| {A.CLE_TABLE_B} | 2026-12-01T09:00:00Z | f | {'b' * 64} |\n"
                     f"| {A.CLE_ISSUE_DE_LA_BASE} | 2026-12-01T10:00:00Z | f | {'a' * 64} |\n", encoding="utf-8")
        return r

    def a_rebours(*args):
        return list(reversed(_lire_factice([])(*args)))
    with pytest.raises(GardeArret, match="hors de l'ordre des identifiants"):
        L.produire(A.JUGE, e["chemin"], consigne, "e" * 64, registre=registre("r1"), reglages=reglages,
                   chargeur=_chargeur([]), dossier_production=w / "p1", racine=racine, lire=a_rebours)
    r2 = registre("r2")
    L.produire(A.JUGE, e["chemin"], consigne, "e" * 64, registre=r2, reglages=reglages, chargeur=_chargeur([]),
               dossier_production=w / "p2", racine=racine, lire=_lire_factice([]))
    charges, lus = [], []
    with pytest.raises(GardeArret, match="déjà inscrite"):
        L.produire(A.JUGE, e["chemin"], consigne, "e" * 64, registre=r2, reglages=reglages, chargeur=_chargeur(charges),
                   dossier_production=w / "p2bis", racine=racine, lire=_lire_factice(lus))
    assert charges == [] and lus == [] and not (w / "p2bis").exists()      # refusée avant tout appel
    faux = w / "p3" / "morceaux-juge" / "morceau-00000.jsonl"
    faux.parent.mkdir(parents=True)
    faux.write_text("".join(json.dumps({"cle": f"{9 - i:016x}", "score": 1.0, "balise": "écrite", "jointure": "aucune",
                                        "masse_faible": False}) + "\n" for i in range(2)), encoding="utf-8")
    sceller(faux)
    with pytest.raises(GardeArret, match="identifiants ≠ ceux de son lot"):
        L.produire(A.JUGE, e["chemin"], consigne, "e" * 64, registre=registre("r3"), reglages=reglages,
                   chargeur=_chargeur([]), dossier_production=w / "p3", racine=racine, lire=_lire_factice([]))


def test_gardes_d_etat_avant_la_production(monde, monkeypatch):
    """Artefacts sur l'état laissé par une exécution arrêtée avant la production : entropie de la table autre que
    celle admise ; bilan qui ne désigne pas ses demandes ; deux lignes d'engagement ; dossier de sortie peuplé ;
    extraction d'une autre configuration du bras ; sorties d'extraction déjà présentes."""
    (monde.w / "extraction").mkdir(parents=True)
    (monde.w / "extraction" / X.FICHIER_TEXTES).write_text("", encoding="utf-8")
    with pytest.raises(GardeArret, match="sorties déjà présentes"):
        L.extraire(monde.racine, monde.config)
    os.rename(monde.w / "extraction" / X.FICHIER_TEXTES, monde.w / "reste-de-l-essai.jsonl")
    L.extraire(monde.racine, monde.config)
    _issue(monde)
    vraie = A.tirer_la_table_opaque
    monkeypatch.setattr(A, "tirer_la_table_opaque", lambda cles, e=None: {**vraie(cles, e), "entropie_propre": "7"})
    with pytest.raises(GardeArret, match="n'est pas celle qui a été admise"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=_lire_factice([]))
    monkeypatch.setattr(A, "tirer_la_table_opaque", vraie)
    assert not (monde.w / "a-part" / A.FICHIER_TABLE_OPAQUE).exists()

    def arret(*args):
        raise RuntimeError("arrêt avant la première lecture (doublure)")
    monkeypatch.setattr(L, "EXECUTION", "essai-2")
    with pytest.raises(RuntimeError):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=arret)
    bilan = monde.w / "a-part" / P.fichier_du_bilan(A.JUGE)
    original = bilan.read_text(encoding="utf-8")
    bilan.write_text(original.replace(json.loads(original)["demandes_sha256"], "0" * 64), encoding="utf-8")
    Path(str(bilan) + ".sha256").write_text(_sha(bilan) + "  " + bilan.name + "\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="ne désigne pas ce fichier de demandes"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=arret)
    bilan.write_text(original, encoding="utf-8")
    Path(str(bilan) + ".sha256").write_text(_sha(bilan) + "  " + bilan.name + "\n", encoding="utf-8")
    (monde.w / "sortie").mkdir()
    (monde.w / "sortie" / "intrus.json").write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="déjà peuplé"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=arret)
    os.rename(monde.w / "sortie" / "intrus.json", monde.w / "intrus.json")
    with pytest.raises(RuntimeError):                                     # cas sain : reprise jusqu'à la lecture
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=arret)
    autre = json.loads((monde.racine / monde.cfg["configuration_du_bras"]["chemin"]).read_text(encoding="utf-8"))
    sha_autre = _ecrire_scelle(monde.w / "entrees" / "configuration-bras-autre.json",
                               json.dumps({**autre, "entropie": ENTROPIE_DU_BRAS + 1}))
    with pytest.raises(GardeArret, match="configuration de la base ≠ configuration du bras"):
        L.discretion(monde.racine, _config(monde, configuration_du_bras={
            "chemin": "travail/entrees/configuration-bras-autre.json", "sha256": sha_autre}),
            entree=_entree([]), chargeur=_chargeur([]), lire=arret)
    with open(monde.registre, "a", encoding="utf-8") as f:
        f.write(f"| {L.CLE_ENGAGEMENT} | 2026-12-02T10:00:00Z | travail/a-part/x.json | {'d' * 64} |\n")
    with pytest.raises(GardeArret, match="une au plus"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=arret)


def test_ligne_d_engagement_d_un_autre_fichier(monde):
    L.extraire(monde.racine, monde.config)
    _issue(monde)
    with open(monde.registre, "a", encoding="utf-8") as f:
        f.write(f"| {L.CLE_ENGAGEMENT} | 2026-12-02T10:00:00Z | travail/a-part/autre-table.json | {'d' * 64} |\n")
    with pytest.raises(GardeArret, match="désigne un autre fichier"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=_lire_factice([]))


def test_aucune_reprise_apres_une_ouverture(monde):
    L.extraire(monde.racine, monde.config)
    _issue(monde)
    with open(str(monde.registre) + ".ouvertures.md", "a", encoding="utf-8") as f:
        f.write(f"| {A.CLE_OUVERTURE} | 2026-12-01T11:00:00Z | {A.LEXICAL} |\n")
    with pytest.raises(GardeArret, match="aucune reprise après une ligne d'ouverture"):
        L.discretion(monde.racine, monde.config, entree=_entree([]), chargeur=_chargeur([]), lire=_lire_factice([]))
    assert not (monde.w / "a-part").exists()


# ======================================================================================================= configuration
def test_configuration_cas_sain_et_artefacts(monde):
    cfg, _ = L.lire_la_configuration(monde.config)
    assert cfg["permutation"] == A.PERMUTATION_PAR_PAIRE
    dossiers = dict(monde.cfg["dossiers"])
    for changements, motif in (({"statistique_agregateur": None}, "laissées nulles"),
                               ({"mode": "reel"}, "2000 permutations"),
                               ({"permutation": A.PERMUTATION_LIBRE}, "échange par paire"),
                               ({"forme_du_fichier_par_unite": "score"}, "rang"),
                               ({"modules": {**monde.cfg["modules"], "src/x.py": "0" * 64}}, "aucun autre"),
                               ({"modules": {k: v.upper() for k, v in monde.cfg["modules"].items()}}, "minuscules"),
                               ({"registre_des_accords_fige": {**monde.cfg["registre_des_accords_fige"], "commit": "main"}},
                                "commit"),
                               ({"lecture": {**monde.cfg["lecture"], "lot": 0}}, "lot"),
                               ({"fins_moniteur_boite_noire": []}, "jetons de fin"),
                               ({"fins_moniteur_boite_noire": [2, 1]}, "jetons de fin"),
                               ({"version": "lanceur-discretion-bras-a-v0"}, "version"),
                               ({"go_de_lazar": "GO-2026-11-19"}, "ligne d'accord"),
                               ({"statistique_agregateur": "mediane"}, "statistique"),
                               ({"n_tirages": 0}, "n_tirages"),
                               ({"texte_scelle": {"chemin": "x.md", "sha256": "abc"}}, "texte scellé"),
                               ({"chargement": {**monde.cfg["chargement"], "dtype": "float16"}}, "chargement"),
                               ({"chargement": {**monde.cfg["chargement"], "variables_gabarit": {"juge": {}}}},
                                "chargement"),
                               ({"dossiers": {**dossiers, "rangs": "../ailleurs"}}, "sans « .. »"),
                               ({"dossiers": {k: v for k, v in dossiers.items() if k != "rangs"}}, "dossiers"),
                               ({"dossiers": {**dossiers, "autre": "travail/autre"}}, "dossiers")):
        with pytest.raises(GardeArret, match=motif):
            L.lire_la_configuration(_config(monde, **changements))
    with pytest.raises(GardeArret, match="mode réel"):
        L.lire_la_configuration(monde.config, cli=True)
    p = _config(monde, n_permutations=5)
    p.write_text(p.read_text(encoding="utf-8").replace('"n_permutations": 5', '"n_permutations": 6'), encoding="utf-8")
    with pytest.raises(GardeArret, match="compagnon"):
        L.lire_la_configuration(p)
    cfg_extra = {**monde.cfg, "de_trop": 1}
    q = monde.w / "config-de-trop.json"
    _ecrire_scelle(q, json.dumps(cfg_extra))
    with pytest.raises(GardeArret, match="aucune autre"):
        L.lire_la_configuration(q)


def test_dossiers_deux_a_deux_disjoints(tmp_path):
    sains = {k: tmp_path / k for k in L.DOSSIERS}
    L.exiger_dossiers_disjoints(sains)
    for a, b in (("rangs", "sortie"), ("rangs", "production"), ("a_part", "demandes")):
        with pytest.raises(GardeArret, match="disjoints"):
            L.exiger_dossiers_disjoints({**sains, b: sains[a] / "dedans"})
        with pytest.raises(GardeArret, match="disjoints"):
            L.exiger_dossiers_disjoints({**sains, b: sains[a]})


def test_modules_a_leur_empreinte(monde, monkeypatch):
    assert set(L.verifier_les_modules(monde.racine, monde.cfg)) == set(L.MODULES_APPELES.values())
    faux = {**monde.cfg, "modules": {**monde.cfg["modules"], L.MODULES_APPELES["preparation"]: "0" * 64}}
    with pytest.raises(GardeArret, match="« preparation » : empreinte"):
        L.verifier_les_modules(monde.racine, faux)
    # le module d'entrée : présent sous la racine à son empreinte, sinon refus
    monkeypatch.setattr(L, "MODULES_APPELES", {**L.MODULES_APPELES, "entree": "travail/entree-factice.py"})
    with pytest.raises(GardeArret, match="« entree » absent"):
        L.verifier_les_modules(monde.racine, {**monde.cfg, "modules": {**monde.cfg["modules"],
                                                                       "travail/entree-factice.py": "1" * 64}})
    (monde.w / "entree-factice.py").write_text("x = 1\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="« entree » : empreinte"):
        L.verifier_les_modules(monde.racine, {**monde.cfg, "modules": {**monde.cfg["modules"],
                                                                       "travail/entree-factice.py": "1" * 64}})
    sain = {**monde.cfg, "modules": {**monde.cfg["modules"], "travail/entree-factice.py": _sha(monde.w / "entree-factice.py")}}
    L.verifier_les_modules(monde.racine, sain)
    with pytest.raises(GardeArret, match="module d'entrée importé"):
        L.verifier_les_modules(monde.racine, sain, SimpleNamespace(__file__=str(RACINE / "setup.py")))
    # un module importé qui n'est pas le fichier de la racine (une autre copie sur le chemin d'import)
    monkeypatch.setitem(L.IMPORTES, "preparation", SimpleNamespace(__file__=str(RACINE / "autre" / "copie.py")))
    with pytest.raises(GardeArret, match="module importé « preparation »"):
        L.verifier_les_modules(monde.racine, sain)


def test_comptes_de_positions_du_module_d_entree():
    actions = [{"condition": c, "tache": t, "episode": e, "pas": p} for c in ("honnete", "dose-1.00") for t in TACHES
               for e in range(8) for p in range(10)]
    L.exiger_comptes_de_positions(actions, _entree([]))
    with pytest.raises(GardeArret, match="≠ 80"):
        L.exiger_comptes_de_positions(actions[:-1], _entree([]))
    with pytest.raises(GardeArret, match="≠ 80"):
        L.exiger_comptes_de_positions([], _entree([]))


# ======================================================================================================= écriture
def test_poser_compagnon_d_abord_jamais_d_ecrasement(tmp_path, monkeypatch):
    monkeypatch.setattr(L, "EXECUTION", "essai-poser")
    d = tmp_path / "d"
    p = L.provisoire(d) / "f.json"
    p.parent.mkdir(parents=True)
    p.write_text("{}\n", encoding="utf-8")
    sha = sceller(p)
    final = L.poser(d, "f.json")                                                # cas sain
    assert final == d / "f.json" and _sha(final) == sha and not p.exists()
    p.write_text("{}\n", encoding="utf-8")
    sceller(p)
    with pytest.raises(GardeArret, match="n'écrase jamais"):                     # nom final pris
        L.poser(d, "f.json")
    # pose interrompue entre le compagnon et le fichier : achevée
    q = L.provisoire(d) / "g.json"
    q.write_text("[]\n", encoding="utf-8")
    sceller(q)
    os.rename(str(q) + ".sha256", d / "g.json.sha256")
    assert _sha(L.poser(d, "g.json")) == _sha(d / "g.json")
    # compagnon seul, d'un autre fichier : refus
    (d / "h.json.sha256").write_text("0" * 64 + "  h.json\n", encoding="utf-8")
    r = L.provisoire(d) / "h.json"
    r.write_text("1\n", encoding="utf-8")
    sceller(r)
    with pytest.raises(GardeArret, match="posé sans son fichier"):
        L.poser(d, "h.json")
    # fichier provisoire non scellé : refus
    (L.provisoire(d) / "i.json").write_text("2\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="compagnon absent"):
        L.poser(d, "i.json")


def test_morceaux_un_reste_provisoire_n_est_pas_lu(tmp_path, monkeypatch):
    monkeypatch.setattr(L, "EXECUTION", "essai-morceaux")
    d = tmp_path / "morceaux-juge"
    reste = d / L.PROVISOIRE / "une-autre-execution" / "morceau-00000.jsonl"
    reste.parent.mkdir(parents=True)
    reste.write_text("reste\n", encoding="utf-8")
    assert L._morceaux_presents(d, 3) == {}                                      # cas sain : le reste n'est pas lu
    (d / "morceau-00001.jsonl").write_text("{}\n", encoding="utf-8")
    sceller(d / "morceau-00001.jsonl")
    assert list(L._morceaux_presents(d, 3)) == [1]
    (d / "morceau-00007.jsonl").write_text("{}\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="inattendu"):
        L._morceaux_presents(d, 3)
    (d / "morceau-00007.jsonl").rename(d / "morceau-00002.jsonl")
    with pytest.raises(GardeArret, match="compagnon absent"):
        L._morceaux_presents(d, 3)


def test_registre_lignes_uniques_et_au_format(tmp_path):
    reg = tmp_path / "r.md"
    reg.write_text("", encoding="utf-8")
    L.inscrire(reg, L.CLE_ENGAGEMENT, "a/b.json", "f" * 64)
    assert len(L.lignes_du_registre(reg, L.CLE_ENGAGEMENT)) == 1
    with pytest.raises(GardeArret, match="déjà inscrite"):
        L.inscrire(reg, L.CLE_ENGAGEMENT, "a/b.json", "f" * 64)
    L.inscrire(reg, L.CLE_REPRISE, "a/c.json", "e" * 64, unique=False)
    L.inscrire(reg, L.CLE_REPRISE, "a/d.json", "e" * 64, unique=False)
    assert len(L.lignes_du_registre(reg, L.CLE_REPRISE)) == 2
    for chemin, sha in (("a|b", "f" * 64), ("a/b", "F" * 64), ("", "f" * 64)):
        with pytest.raises(GardeArret, match="hors format"):
            L.inscrire(reg, "AUTRE", chemin, sha)


# ======================================================================================================= base et entrée
def test_base_par_son_lanceur(monde):
    vus = []

    def executer(commande, racine):
        vus.append(commande)
        return SimpleNamespace(returncode=0, stdout="diag/x/issue.json " + "a" * 64 + "\n", stderr="")
    m = L.Manifeste(monde.racine, "base", monde.config, _sha(monde.config), ["essai"])
    r = L.base(monde.racine, monde.config, m, executer)
    assert r["code"] == 0 and vus[0][1].endswith("scripts/lancer_mots_et_cout_bras_a_v2.sh")
    assert vus[0][2:6] == ["--mode", "reel", "--racine-entrees", str((monde.w / "extraction").resolve())]
    assert m.contenu["base"]["sortie"] == ["diag/x/issue.json " + "a" * 64]
    with pytest.raises(GardeArret, match="code 2"):
        L.base(monde.racine, monde.config, None,
               lambda c, r: SimpleNamespace(returncode=2, stdout="", stderr="REFUS : registre"))


def test_extraire_refuse_une_seconde_fois(monde):
    L.extraire(monde.racine, monde.config)
    with pytest.raises(GardeArret, match="déjà inscrite"):
        L.extraire(monde.racine, monde.config)


def test_cli_refuse_le_mode_jouet(monde, capsys):
    assert L.principal(["discretion", "--racine", str(monde.racine), "--config", str(monde.config)]) == 2
    assert "mode réel" in capsys.readouterr().err


def test_garde_statique_du_lanceur():
    """Le lanceur n'importe aucun module de graines de la relance ; du code de la relance, il ne nomme que le module
    d'entrée, par son nom ; ses importations internes sont les modules qu'il cite par empreinte."""
    chemin = RACINE / "src/controle_ia/organismes_discrets/bras_a_v2_habilite_lanceur/lanceur_discretion_v1.py"
    source = chemin.read_text(encoding="utf-8")
    assert "graines_bras_a" not in source
    internes = set()
    for n in ast.walk(ast.parse(source)):
        if isinstance(n, ast.ImportFrom) and n.level:
            internes.add("." * n.level + (n.module or ""))
    assert internes == {"...gardes", "...scellement", "..bras_a_v2_habilite", "..bras_a_v2_habilite_preparation",
                        "...harnais", "...harnais.formats"}
    assert L.MODULE_D_ENTREE.endswith("entree_lanceur_discretion_bras_a_v2")
    assert ENTREE_FICHIER == "src/controle_ia/organismes_discrets/entree_lanceur_discretion_bras_a_v2.py"
