"""Reprise par segments (décision de Lazar, 25 octobre 2026, 20:23 Paris) : une course arrêtée par `STOP` entre deux
unités continue dans une autre commande, à la première unité qui n'a pas tourné, avec les mêmes graines, la même archive
et la même dépense ; rien n'est rejoué ni sauté. Chaque garde sur un cas sain et sur un artefact (R5) ; aucun réseau."""
import argparse
import hashlib
import json
import os
import pathlib
import shutil
import sys

import numpy as np
import pytest

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))

from essaim_m3.noyau import appels, archive, boucle, cli, taches  # noqa: E402
from essaim_m3.simulateur import EspeceSimulee  # noqa: E402

CONCEPTEUR = RACINE / "tests" / "fixtures" / "organisme_concepteur" / "organisme"  # déclare la fin de sa conception à la ronde 2
FACTICE = RACINE / "tests" / "fixtures" / "organisme_factice" / "organisme"  # sans critère : va jusqu'à la borne dure
UN_SEUL = {"concepteur": (CONCEPTEUR, "anthropic")}
DEUX = {"concepteur": (CONCEPTEUR, "anthropic"), "factice": (FACTICE, "gemini")}


def _appelants_deterministes():
    """Espèces simulées dont la réponse ne dépend que du modèle et de la consigne (graine tirée de leur empreinte) : la
    course continue et la même course en segments reçoivent les mêmes réponses aux mêmes consignes, quel que soit le
    nombre de commandes (les doubles ordinaires tirent dans un générateur qui avance d'un appel à l'autre)."""
    def servir(modele_id, prompt, max_tokens):
        graine = int.from_bytes(hashlib.sha256(f"{modele_id}\0{prompt}".encode("utf-8")).digest()[:8], "little")
        return EspeceSimulee(modele_id, np.random.default_rng(graine))(modele_id, prompt, max_tokens)
    return {"anthropic": servir, "gemini": servir}


def _noyau(racine, imposes=UN_SEUL, generations=3, rondes=3, plafond=50.0, memoire_partagee=False, entropie=11, graine_banque=5):
    banque = taches.banque_simulation(np.random.default_rng(graine_banque), 6, 6, 4)
    return boucle.Noyau(racine, "mission de test", banque, {"appels_max": 30, "usd_max": 2.0, "temps_max_s": 60}, plafond,
                        generations, appelants=_appelants_deterministes(), especes_amorcage=[], entropie=entropie,
                        organismes_imposes={nom: {"organisme": str(p), "famille": f} for nom, (p, f) in imposes.items()},
                        rondes_conception_max=rondes, memoire_partagee=memoire_partagee)


def _courir(racine, imposes=UN_SEUL, arrets=(), stop_pendant=False, **params):
    """Fait tourner une course jusqu'au bout. `STOP` est posé après chaque unité (ronde de conception ou génération d'une
    lignée) dont le rang, compté sur toute la course (1, 2, …), est dans `arrets` — ou, avec `stop_pendant`, juste avant
    qu'elle commence, donc pendant qu'elle tourne ; comme le lanceur, on le retire puis on reprend dans un noyau neuf.
    Rend (noyaux des segments, rapport final)."""
    compte = {"unites": 0}
    noyaux = []
    while True:
        n = _noyau(racine, imposes, **params)
        if noyaux:
            (pathlib.Path(racine) / "STOP").unlink()
            n.reprendre()
        else:
            n.amorcer()

        def unite(lignee, conception=None, _origine=n.executer_generation, _n=n):
            compte["unites"] += 1
            rang = compte["unites"]
            if stop_pendant and rang in arrets:
                (_n.racine / "STOP").write_text("stop", encoding="utf-8")
            r = _origine(lignee, conception=conception)
            if not stop_pendant and rang in arrets:
                (_n.racine / "STOP").write_text("stop", encoding="utf-8")
            return r
        n.executer_generation = unite
        rapport = n.boucler()
        noyaux.append(n)
        dernier = _journal(racine)[-1]
        if not (dernier.get("etape") == "arret" and dernier.get("raison") == "fichier STOP"):
            return noyaux, rapport  # course finie (un STOP posé pendant la dernière unité peut rester sur le disque)
        assert len(noyaux) <= len(arrets), "plus de segments que d'arrêts posés"


def _journal(racine):
    return [json.loads(x) for x in (pathlib.Path(racine) / "evenements.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]


def _sans_segments(evenements):
    """Le journal moins ce que les segments y ajoutent (l'arrêt sur STOP de la conception et de la course, la reprise),
    sans les heures."""
    return [{k: v for k, v in e.items() if k != "quand_utc"} for e in evenements
            if not (e.get("etape") == "reprise" or (e.get("etape") in ("arret", "arret_conception") and e.get("raison") == "fichier STOP"))]


def _normaliser(obj, noyau):
    """Les chemins propres à une course (espace des organismes, racine) remplacés par des marques."""
    texte = json.dumps(obj, ensure_ascii=False, sort_keys=True)
    for chemin, marque in ((str(noyau.espace), "<ESPACE>"), (str(noyau.racine), "<COURSE>")):
        texte = texte.replace(chemin, marque)
    return json.loads(texte)


def _index(racine):
    lignes = [json.loads(x) for x in (pathlib.Path(racine) / "archive" / "index.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    return [{k: v for k, v in l.items() if k != "quand_utc"} for l in lignes]


def _projection_rapport(rapport, noyau):
    garde = ("courbes", "scores_finaux", "depense_totale_usd", "n_appels_total", "lignees", "rondes_conception", "generations_invalidees")
    p = {k: rapport[k] for k in garde}
    p["generations"] = [{k: v for k, v in l.items() if k != "quand_utc"} for l in rapport["generations"]]
    return _normaliser(p, noyau)


def _etats(racine):
    return sorted((pathlib.Path(racine) / "reprise").glob("etat-v*.json"), key=lambda p: int(p.stem.split("-v")[1]))


def _comparer(racine_c, noyau_c, rapport_c, racine_s, noyaux_s, rapport_s, n_arrets):
    """La course en segments a fait exactement ce qu'a fait la course continue : mêmes événements (graines, rondes et leur
    ordre, unités, fins), même archive (empreintes des organismes comprises), même rapport ; un état scellé par arrêt."""
    n_s = noyaux_s[-1]
    assert len(noyaux_s) == n_arrets + 1
    assert _normaliser(_sans_segments(_journal(racine_s)), n_s) == _normaliser(_sans_segments(_journal(racine_c)), noyau_c)
    assert _index(racine_s) == _index(racine_c)
    assert _projection_rapport(rapport_s, n_s) == _projection_rapport(rapport_c, noyau_c)
    ev = _journal(racine_s)
    assert sum(1 for e in ev if e["etape"] == "arret" and e["raison"] == "fichier STOP") == n_arrets
    assert [e["segment"] for e in ev if e["etape"] == "reprise"] == list(range(2, n_arrets + 2))
    assert rapport_s["segments"] == n_arrets + 1 and len(rapport_s["reprises"]) == n_arrets
    assert rapport_s["manifeste"] == json.loads((pathlib.Path(racine_s) / "manifeste-run.json").read_text(encoding="utf-8"))
    etats = _etats(racine_s)
    assert [p.name for p in etats] == [f"etat-v{i}.json" for i in range(1, n_arrets + 1)]
    for p in etats:  # scellés, jamais réécrits
        assert (p.parent / (p.name + ".sha256")).read_text(encoding="utf-8").split()[0] == archive.empreinte_fichier(p)
    # la dépense n'est jamais comptée deux fois : celle du rapport est la somme de l'archive (au demi-dix-millième près par
    # ligne : chaque coût archivé est arrondi à quatre décimales)
    lignes = _index(racine_s)
    assert abs(rapport_s["depense_totale_usd"] - sum(float(l["cout_usd"] or 0) for l in lignes)) <= 0.00005 * (len(lignes) + 1)


@pytest.fixture(scope="module")
def continue_un_seul(tmp_path_factory):
    racine = tmp_path_factory.mktemp("continue-un-seul") / "course"
    noyaux, rapport = _courir(racine, UN_SEUL)
    return racine, noyaux[-1], rapport


def test_course_continue_de_reference(continue_un_seul):
    """La référence : 2 rondes de conception (l'organisme déclare la fin à la ronde 2 sur une borne de 3), puis 3
    générations notées ; la course finit sans lignée active, sans aucun état de reprise."""
    racine, n, rapport = continue_un_seul
    assert [(l["generation"], l["phase"]) for l in _index(racine)] == [(1, "conception"), (2, "conception"), (0, None), (1, None), (2, None)]
    assert n.lignees["concepteur"]["fin"] == "générations maximales" and _journal(racine)[-1]["raison"] == "aucune lignée active"
    assert not (racine / "reprise").exists() and rapport["segments"] == 1 and rapport["reprises"] == []


@pytest.mark.parametrize("arrets", [(1,), (2,), (3,), (4,), (1, 3, 4)])
def test_course_en_segments_egale_la_course_continue(tmp_path, continue_un_seul, arrets):
    """Cas sain : STOP après la ronde de conception 1 (la conception continue à la ronde 2), après la ronde 2 (la
    conception finie se constate à la reprise), après la génération 0, après la génération 1, et trois arrêts dans la
    même course : chaque fois, la course en segments est la course continue."""
    racine_c, n_c, r_c = continue_un_seul
    noyaux, r_s = _courir(tmp_path / "course", UN_SEUL, arrets=arrets)
    _comparer(racine_c, n_c, r_c, tmp_path / "course", noyaux, r_s, len(arrets))


def test_stop_en_conception_aucune_generation_notee_avant_la_reprise(tmp_path, continue_un_seul):
    """Un STOP lu pendant la conception arrête la course là : aucune génération notée ne part dans ce segment ; l'état dit
    la conception non faite et la ronde suivante ; la reprise constate la fin déclarée et part à la génération 0."""
    racine_c, n_c, r_c = continue_un_seul
    noyaux, r_s = _courir(tmp_path / "course", UN_SEUL, arrets=(2,))
    etat = json.loads(_etats(tmp_path / "course")[0].read_text(encoding="utf-8"))
    assert etat["conception_faite"] is False and etat["prochaine_ronde_conception"] == 3 and etat["n_lignes_archive"] == 2
    assert etat["lignees"]["concepteur"]["conception_finie"] is True and etat["lignees"]["concepteur"]["generation"] == 0
    _comparer(racine_c, n_c, r_c, tmp_path / "course", noyaux, r_s, 1)


def test_conception_arretee_jamais_suivie_de_generations_dans_le_meme_segment(tmp_path, continue_un_seul):
    """Artefact : STOP retiré juste après que la conception s'est arrêtée sur lui (main humaine, course voisine) ; la course
    ne passe pas pour autant aux générations notées dans ce segment : arrêt et état écrits ; la reprise finit la course
    comme la course continue."""
    racine_c, n_c, r_c = continue_un_seul
    racine = tmp_path / "course"
    n = _noyau(racine)
    n.amorcer()
    origine = n.concevoir

    def concevoir():
        (racine / "STOP").write_text("stop", encoding="utf-8")
        r = origine()
        (racine / "STOP").unlink()
        return r
    n.concevoir = concevoir
    n.boucler()
    assert not (racine / "archive" / "index.jsonl").exists() and _journal(racine)[-1] == dict(_journal(racine)[-1], etape="arret", raison="fichier STOP")
    assert json.loads(_etats(racine)[0].read_text(encoding="utf-8"))["conception_faite"] is False
    n2 = _noyau(racine)
    n2.reprendre()
    r_s = n2.boucler()
    _comparer(racine_c, n_c, r_c, racine, [n, n2], r_s, 1)


def test_stop_pendant_la_derniere_unite_n_appelle_pas_de_segment(tmp_path, continue_un_seul):
    """Un STOP posé pendant la dernière unité (plus aucune lignée active ensuite) ne laisse pas de travail à reprendre : la
    course finit « aucune lignée active », sans état de reprise ni segment de plus (comme la course continue)."""
    racine_c, n_c, r_c = continue_un_seul
    noyaux, r_s = _courir(tmp_path / "course", UN_SEUL, arrets=(5,))
    assert len(noyaux) == 1 and (tmp_path / "course" / "STOP").exists() and not (tmp_path / "course" / "reprise").exists()
    assert _journal(tmp_path / "course")[-1]["raison"] == "aucune lignée active"
    _comparer(racine_c, n_c, r_c, tmp_path / "course", noyaux, r_s, 0)


def test_stop_pose_pendant_une_unite_ne_l_interrompt_pas(tmp_path, continue_un_seul):
    """P4C2-03 : un STOP posé pendant une unité (comme le minuteur du lanceur) ne la coupe pas : elle finit et s'archive,
    l'arrêt et l'état suivent ; la reprise part de l'unité suivante."""
    racine_c, n_c, r_c = continue_un_seul
    noyaux, r_s = _courir(tmp_path / "course", UN_SEUL, arrets=(3,), stop_pendant=True)
    etat = json.loads(_etats(tmp_path / "course")[0].read_text(encoding="utf-8"))
    assert etat["n_lignes_archive"] == 3 and etat["ronde_inachevee"] is None and etat["conception_faite"] is True
    assert etat["lignees"]["concepteur"]["generation"] == 1  # la génération 0 a tourné en entier ; la 1 n'a pas commencé
    _comparer(racine_c, n_c, r_c, tmp_path / "course", noyaux, r_s, 1)


@pytest.mark.parametrize("memoire_partagee", [False, True])
def test_ronde_interrompue_continuee_sans_rejouer_ni_sauter(tmp_path, memoire_partagee):
    """Deux lignées : STOP après la première lignée de chaque ronde (conception 1 et 2, générations 0 et 1). L'état garde
    la ronde en cours (ordre tiré, lignées faites) ; la reprise la continue dans son ordre, sans nouveau tirage, avec sa
    vue figée en mémoire partagée : la course en segments est la course continue."""
    params = dict(generations=2, rondes=2, memoire_partagee=memoire_partagee)
    noyaux_c, r_c = _courir(tmp_path / "continue", DEUX, **params)
    assert len(_index(tmp_path / "continue")) == 8
    noyaux, r_s = _courir(tmp_path / "course", DEUX, arrets=(1, 3, 5, 7), **params)
    etats = [json.loads(p.read_text(encoding="utf-8")) for p in _etats(tmp_path / "course")]
    assert [(e["ronde_inachevee"]["phase"], e["ronde_inachevee"]["ronde"], len(e["ronde_inachevee"]["faites"])) for e in etats] == \
        [("conception", 1, 1), ("conception", 2, 1), ("generation", 1, 1), ("generation", 2, 1)]
    if memoire_partagee:
        assert all(e["ronde_inachevee"]["vue_figee"] for e in etats[2:])
    _comparer(tmp_path / "continue", noyaux_c[-1], r_c, tmp_path / "course", noyaux, r_s, 4)
    ev = _journal(tmp_path / "course")
    assert sum(1 for e in ev if e["etape"] == "ronde") == 2 and sum(1 for e in ev if e["etape"] == "ronde_conception") == 2


# ---------- artefacts : chaque refus laisse la course telle quelle ----------

def _course_arretee(racine, **params):
    """Course amorcée puis arrêtée par STOP avant toute unité (état v1 écrit) ; STOP retiré, comme le ferait le lanceur."""
    n = _noyau(racine, **params)
    n.amorcer()
    (pathlib.Path(racine) / "STOP").write_text("stop", encoding="utf-8")
    n.boucler()
    (pathlib.Path(racine) / "STOP").unlink()
    return pathlib.Path(racine)


def _resceller(chemin, changer):
    etat = json.loads(chemin.read_text(encoding="utf-8"))
    changer(etat)
    chemin.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
    archive.sceller(chemin)


def _refus(racine, motif, **params):
    """`reprendre()` refuse (Arret dont le message contient `motif`) et n'écrit rien : journal et rapports inchangés."""
    journal = (racine / "evenements.jsonl").read_bytes()
    rapports = sorted(p.name for p in racine.glob("rapport-v*.json"))
    with pytest.raises(appels.Arret) as e:
        _noyau(racine, **params).reprendre()
    assert motif in str(e.value), str(e.value)
    assert (racine / "evenements.jsonl").read_bytes() == journal and sorted(p.name for p in racine.glob("rapport-v*.json")) == rapports
    return str(e.value)


def test_reprise_acceptee_puis_jamais_deux_fois_le_meme_etat(tmp_path):
    """Cas sain : la course arrêtée avant toute unité reprend et finit ; artefacts : un second lancement de reprise sur le
    même état (pendant, puis après la reprise) est refusé — le journal a bougé ; une course finie n'a pas d'état neuf."""
    racine = _course_arretee(tmp_path / "course")
    etat = json.loads(_etats(racine)[0].read_text(encoding="utf-8"))
    assert etat["raison_arret"] == "fichier STOP" and etat["conception_faite"] is False and etat["prochaine_ronde_conception"] == 1
    if os.geteuid() == 0:  # protégés comme les journaux du noyau
        assert (racine / "reprise").stat().st_mode & 0o777 == 0o700 and _etats(racine)[0].stat().st_mode & 0o777 == 0o600
    n = _noyau(racine)
    n.reprendre()
    _refus(racine, "une seule reprise par état")
    rapport = n.boucler()
    assert rapport["segments"] == 2 and [l["generation"] for l in _index(racine) if not l["phase"]] == [0, 1, 2]
    _refus(racine, "une seule reprise par état")
    assert len(_etats(racine)) == 1


def test_reprise_refusee_sans_etat_et_sur_noyau_amorce(tmp_path):
    n = _noyau(tmp_path / "finie", generations=1, rondes=0)
    n.amorcer()
    n.boucler()  # finie sans STOP : aucun état
    _refus(tmp_path / "finie", "aucun état de reprise", generations=1, rondes=0)
    racine = _course_arretee(tmp_path / "course")
    n2 = _noyau(racine)
    n2.amorcer()
    with pytest.raises(appels.Arret, match="noyau neuf"):
        n2.reprendre()


def test_reprise_refusee_stop_present(tmp_path):
    racine = _course_arretee(tmp_path / "course")
    (racine / "STOP").write_text("stop", encoding="utf-8")
    _refus(racine, "STOP est encore")
    (racine / "STOP").unlink()
    _noyau(racine).reprendre()  # sain : accepté une fois STOP retiré


def test_reprise_refusee_etat_altere(tmp_path):
    """Artefacts : un octet changé sans le compagnon ; un état rescellé d'une autre version, d'un autre arrêt, d'une ronde
    en cours illisible, avec un organisme hors de la course, après un crédit épuisé, au plafond."""
    racine = _course_arretee(tmp_path / "course")
    p = _etats(racine)[0]
    sain = p.read_bytes()
    p.write_bytes(sain.replace(b'"segment": 1', b'"segment": 7'))
    _refus(racine, "compagnon")
    cas = [
        (lambda e: e.update(version=2), "version"),
        (lambda e: e.update(raison_arret="plafond total atteint"), "arrêt sur STOP"),
        (lambda e: e.update(ronde_inachevee={"phase": "generation", "ronde": 9, "ordre": ["inconnue"], "faites": []}), "ronde en cours illisible"),
        (lambda e: e.update(ronde_inachevee={"phase": "conception", "ronde": 1, "ordre": ["concepteur"], "faites": ["concepteur"]}), "ronde en cours illisible"),
        (lambda e: e.update(ronde_inachevee={"phase": "conception", "ronde": 2, "ordre": ["concepteur"], "faites": []}), "incohérente"),
        (lambda e: e["lignees"]["concepteur"].update(organisme=str(CONCEPTEUR)), "hors de la course"),
        (lambda e: e.update(arret_credit={"espece": "GEMINI_ARGON"}), "crédit"),
        (lambda e: e.update(depense_totale_usd=50.0), "plafond total atteint"),
    ]
    for changer, motif in cas:
        p.write_bytes(sain)
        _resceller(p, changer)
        _refus(racine, motif)
    p.write_bytes(sain)
    archive.sceller(p)
    _noyau(racine).reprendre()  # sain : l'état d'origine est accepté


def test_reprise_refusee_course_qui_a_bouge(tmp_path):
    """Artefacts : une ligne ajoutée au journal, à l'archive, un manifeste changé, l'organisme d'une lignée active effacé."""
    racine = _course_arretee(tmp_path / "a")
    with (racine / "evenements.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"etape": "intrus"}) + "\n")
    _refus(racine, "journal des événements")
    racine = _course_arretee(tmp_path / "b")
    with (racine / "archive" / "index.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"lignee": "intrus", "generation": 0}) + "\n")
    _refus(racine, "archive de la course a changé")
    racine = _course_arretee(tmp_path / "c")
    m = json.loads((racine / "manifeste-run.json").read_text(encoding="utf-8"))
    (racine / "manifeste-run.json").write_text(json.dumps(dict(m, generations_max=9), ensure_ascii=False, indent=1), encoding="utf-8")
    _refus(racine, "manifeste de la course")
    racine = _course_arretee(tmp_path / "d")
    organisme = pathlib.Path(json.loads(_etats(racine)[0].read_text(encoding="utf-8"))["lignees"]["concepteur"]["organisme"])
    shutil.rmtree(organisme)
    _refus(racine, "organisme introuvable")


@pytest.mark.parametrize("change, champ", [
    ({"generations": 4}, "generations_max"),
    ({"plafond": 60.0}, "plafond_total_usd"),
    ({"entropie": 12}, "entropie_seed_sequence"),
    ({"rondes": 4}, "rondes_conception_max"),
    ({"memoire_partagee": True}, "memoire_partagee"),
    ({"graine_banque": 6}, "sha256_banque"),
    ({"imposes": "modifie"}, "organismes_imposes"),
])
def test_reprise_refusee_si_le_lancement_differe(tmp_path, change, champ):
    """Artefacts : une reprise lancée avec un autre paramètre que la course (bornes, graine, banque, organisme imposé,
    mémoire) est refusée et nomme le champ ; cas sain : les mêmes paramètres sont acceptés."""
    racine = _course_arretee(tmp_path / "course")
    if change.get("imposes") == "modifie":
        copie = tmp_path / "copie" / "organisme"
        shutil.copytree(CONCEPTEUR, copie)
        (copie / "CONCEPTION.md").write_text((copie / "CONCEPTION.md").read_text(encoding="utf-8") + "\nune ligne de plus\n", encoding="utf-8")
        change = {"imposes": {"concepteur": (copie, "anthropic")}}
    message = _refus(racine, champ, **change)
    assert "diffère de la course" in message
    _noyau(racine).reprendre()


def test_reprise_accepte_d_autres_chemins_pour_les_memes_pieces(tmp_path):
    """Cas sain : la même pièce (organisme imposé, même empreinte d'arbre) servie depuis un autre chemin n'empêche pas la
    reprise ; le chemin de ce lancement est consigné dans l'événement `reprise`."""
    racine = _course_arretee(tmp_path / "course")
    copie = tmp_path / "ailleurs" / "organisme"
    shutil.copytree(CONCEPTEUR, copie)
    n = _noyau(racine, imposes={"concepteur": (copie, "anthropic")})
    n.reprendre()
    reprise = _journal(racine)[-1]
    assert reprise["etape"] == "reprise" and reprise["sources"]["organismes_imposes"]["concepteur"] == str(copie)
    assert n.manifeste["organismes_imposes"]["concepteur"]["source"] == str(CONCEPTEUR)  # le manifeste reste celui de la course


# ---------- entrée de commande ----------

def test_cli_simuler_reprendre_et_refus(tmp_path, monkeypatch):
    """`simuler --reprendre` continue la course arrêtée par STOP ; refus : course existante sans `--reprendre` (8),
    `--reprendre` sans course (8) ou avec `--depuis` (8), STOP encore là (9), paramètre différent (9). Sans `--graine`,
    l'entropie de la course est reprise. La course en segments a les mêmes unités que la course continue."""
    def args(sortie):
        return ["simuler", "--sortie", str(sortie), "--generations", "3", "--graine", "12", "--n-train", "6", "--n-test", "6",
                "--n-final", "4", "--appels-max", "30", "--especes", "--organisme-impose", f"concepteur={CONCEPTEUR}@anthropic",
                "--rondes-conception-max", "3", "--usd-max-conception", "2.0", "--recherches-max", "0", "--entrainements-max", "0"]
    assert cli.principal(args(tmp_path / "continue")) == 0
    unites_c = [(l["lignee"], l["generation"], l["phase"], l["statut"], l["successeur"]) for l in _index(tmp_path / "continue")]
    assert len(unites_c) == 5
    course = tmp_path / "course"
    compte = {"n": 0}
    origine = boucle.Noyau.executer_generation

    def unite(self, lignee, conception=None):
        r = origine(self, lignee, conception=conception)
        compte["n"] += 1
        if compte["n"] == 2:
            (self.racine / "STOP").write_text("stop", encoding="utf-8")
        return r
    monkeypatch.setattr(boucle.Noyau, "executer_generation", unite)
    assert cli.principal(args(course)) == 0
    assert (course / "STOP").exists() and len(_etats(course)) == 1 and len(_index(course)) == 2
    assert cli.principal(args(course)) == 8
    assert cli.principal(args(course) + ["--reprendre"]) == 9  # STOP encore là
    (course / "STOP").unlink()
    assert cli.principal(args(course) + ["--reprendre", "--depuis", str(tmp_path / "continue")]) == 8
    assert cli.principal(["simuler", "--sortie", str(tmp_path / "vide"), "--reprendre"]) == 8
    autre = args(course)
    autre[autre.index("--generations") + 1] = "4"
    assert cli.principal(autre + ["--reprendre"]) == 9
    sans_graine = args(course)
    del sans_graine[sans_graine.index("--graine"):sans_graine.index("--graine") + 2]
    assert cli.principal(sans_graine + ["--reprendre"]) == 0
    assert [(l["lignee"], l["generation"], l["phase"], l["statut"], l["successeur"]) for l in _index(course)] == unites_c
    rapport = json.loads(sorted(course.glob("rapport-v*.json"), key=lambda p: int(p.stem.split("-v")[1]))[-1].read_text(encoding="utf-8"))
    assert rapport["segments"] == 2 and len(rapport["reprises"]) == 1
    assert rapport["manifeste"] == json.loads((course / "manifeste-run.json").read_text(encoding="utf-8"))


def test_refus_reprise_des_arguments(tmp_path):
    """La garde d'arguments commune à `simuler` et `lancer`."""
    (tmp_path / "course").mkdir()
    (tmp_path / "course" / "manifeste-run.json").write_text("{}", encoding="utf-8")
    ns = lambda **k: argparse.Namespace(**{"sortie": str(tmp_path / "course"), "depuis": None, "reprendre": False, **k})  # noqa: E731
    assert "existe déjà" in cli._refus_reprise(ns())
    assert cli._refus_reprise(ns(reprendre=True)) is None
    assert "--depuis" in cli._refus_reprise(ns(reprendre=True, depuis="x"))
    assert "aucune course" in cli._refus_reprise(ns(reprendre=True, sortie=str(tmp_path / "vide")))
    assert cli._refus_reprise(ns(sortie=str(tmp_path / "vide"))) is None


@pytest.mark.skipif(not (hasattr(os, "geteuid") and os.geteuid() == 0), reason="le mode réel refuse avant (non root : code 5)")
def test_lancer_refuse_course_existante_sans_reprendre(tmp_path, monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "x")
    monkeypatch.setenv("GEMINI_API_KEY", "y")
    monkeypatch.delenv("ANTHROPIC_BASE_URL", raising=False)
    t = tmp_path / "t.json"
    t.write_text("{}", encoding="utf-8")
    (tmp_path / "course").mkdir()
    (tmp_path / "course" / "manifeste-run.json").write_text("{}", encoding="utf-8")
    base = ["lancer", "--reel", "--go", "GO-X", "--taches", str(t)]
    assert cli.principal(base + ["--sortie", str(tmp_path / "course")]) == 8
    assert cli.principal(base + ["--sortie", str(tmp_path / "vide"), "--reprendre"]) == 8
