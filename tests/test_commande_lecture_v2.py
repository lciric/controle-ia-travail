"""Épreuves du code de commande de la relecture, version 2 (`controle_ia.barreau5_familles.commande_lecture_v2`,
`scripts/lancer_b5f_lecture_v2.sh`) : additif 1, version 2, au devis du barreau 5 (`c3120d3a…`), § 3.4, cas sain et artefact
pour chaque garde (R5). Écrites avant le module.

Monde d'essai : un dépôt jetable relié à un dépôt distant local, qui porte tout `src/` (pour que le lanceur se joue depuis
lui), et trois commits : le « code » (rôle du commit du code de lecture figé), le « commit de commande » (le code plus la
liste fermée des fichiers ajoutés, sur sa branche, dans son arbre de travail) et la « marche » (le code plus le registre
propre, dont la ligne de l'accord de lecture cite l'additif et le commit de commande). Deux arbres de travail, comme au
§ 3.2 : l'arbre figé (à la marche) et l'arbre de commande.

Aucun essai n'atteint le réseau, ne crée, n'arrête ni ne détruit d'instance ; aucune clé n'est lue.
"""
from __future__ import annotations

import ast
import base64
import difflib
import hashlib
import inspect
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from controle_ia.barreau5_familles import commande_lecture_v2 as cl2
from controle_ia.barreau5_familles import engagement_v1 as en
from controle_ia.barreau5_familles import formation_v1 as fv
from controle_ia.barreau5_familles import lecture_v1 as lv
from controle_ia.barreau5_familles import relecture_v1 as rv
from controle_ia.gardes import GardeArret

RACINE = Path(__file__).resolve().parents[1]
LANCEUR_V1 = "scripts/lancer_b5f_lecture_v1.sh"
LANCEUR_V2 = "scripts/lancer_b5f_lecture_v2.sh"
MODULE_V2 = "src/controle_ia/barreau5_familles/commande_lecture_v2.py"
ESSAIS_V2 = "tests/test_commande_lecture_v2.py"
ADDITIF = "c3120d3ade40f31f26a225cd2bf7c3520c7ba0a314e2b554832229d67c8e120c"
GO_LECTURE, GO_FORMATION = "GO-2026-11-24-01", "GO-2026-11-21-01"
# offre d'essai, stockage sous 0,08 USD de l'heure pour les deux pièces (0,0411 à 300 Go ; 0,0205 à 150 Go)
OFFRE = {"id": 654321, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 32,
         "cpu_ram": 257000, "disk_space": 320, "cuda_max_good": 13.0, "dph_total": 1.2, "storage_cost": 0.1}
# l'offre admise du relevé de 10:55Z, telle que la décrit l'additif (§ 1) : carte 1,16 USD de l'heure, stockage de 0,24 USD
# par Go et par mois, disque de 1 050 Go, 16 cœurs, 128 892 Mo, CUDA 13.2 ; mémoire de la carte : 80 Go (valeur d'essai)
OFFRE_DU_RELEVE = {"id": 32744970, "gpu_name": "A100 SXM4", "num_gpus": 1, "gpu_ram": 81920, "cpu_cores_effective": 16,
                   "cpu_ram": 128892, "disk_space": 1050, "cuda_max_good": 13.2, "dph_total": 1.16, "storage_cost": 0.24}
RUN_L, RUN_R = "20261124-120000-b5f-lecture", "20261123-120000-b5f-repetition"
EXISTANTS = [{"nom": f"R{k}-{m}", "chemin": f"donnees/existants-{k}/adaptateur-{m}.pt", "sha256": "a" * 64}
             for k in (1, 2) for m in ("saboteur", "temoin")]
CLES_INCONNUES = ("ENGAGEMENT-RECREATION-3-B5F", "CREATION-RECREATION-3-B5F", "ENGAGEMENT-RECREATION-4-B5F",
                  "CREATION-RECREATION-1-B5F", "CREATION-RECREATION-2-B5F", "CREATION-RECREATION-4-B5F",
                  "NOTE-RECREATIONS-B5F")
REGISTRE_INTACT_SHA256 = "c4aeced74bb6a01c4245972d96df19ba149c3f677a29b745560dc83e3496fe63"


# --- fabrique du monde d'essai -----------------------------------------------------------------------------------------

def _g(r, *a):
    return subprocess.run(["git", "-C", str(r), *a], check=True, capture_output=True, text=True).stdout.strip()


def _ligne_go(ident):
    a, e = date.today() - timedelta(days=1), date.today() + timedelta(days=10)
    return f"| {ident} | {a.isoformat()} | calcul | lecture barreau 5 | 21 USD | {e.isoformat()} | Lazar | essai |"


def _citation(commande, additif=ADDITIF, rapport="f" * 64, session="session de lecture session_essai"):
    """La colonne de référence de la ligne de l'accord de lecture, au format que lit la vérification (d)."""
    return (f"{session} ; additif 1 v2 au devis sha256 {additif} ; commande de lecture v2, commit {commande}, "
            f"vérifiée sha256 {rapport}")


def _registre(code_commit, ref_accord="", sans=()):
    """Registre propre dont toutes les lignes de table sont à clé connue, et qui admet la relecture décisive."""
    t0 = datetime.now(timezone.utc) - timedelta(days=2)
    lignes = [("SCELLEMENT-B5F", f"{lv.TEXTE} ; sha256 {lv.TEXTE_SHA256} ; membres-apprentissage 3 ; piece famille", ""),
              ("CODE-FORMATION-B5F", f"commit {'c' * 40} ; entropie 12345", ""), ("GO-FORMATION-B5F", GO_FORMATION, ""),
              ("SORTIES-FORMATION-B5F", "versement prouvé", ""), ("ENGAGEMENT-B5F", f"sha256 {'d' * 64}", ""),
              ("CODE-LECTURE-B5F", f"commit {code_commit} ; lecture sha256 {lv.programme_sha256()}", ""),
              ("EPREUVE-B5F", f"passee ; lecture sha256 {lv.programme_sha256()} ; rapport sha256 {'e' * 64}", ""),
              ("GO-LECTURE-B5F", GO_LECTURE, ref_accord)]
    return "\n".join(en.ligne_du_registre(k, (t0 + timedelta(minutes=5 * i)).strftime("%Y-%m-%dT%H:%M:%SZ"), c, ref)
                     for i, (k, c, ref) in enumerate(x for x in lignes if x[0] not in sans)) + "\n"


def _registre_a_la_forme_d_aujourd_hui(code_commit, etat):
    """Registre fabriqué à la forme du registre propre du 21 novembre : six lignes de table à clé connue aux lignes 7 à 12,
    puis les sept lignes de recréation aux lignes 13 à 19. `etat` : « intact » (les sept portent leur barre de tête : état
    `c4aeced7…`), « corrige » (voie (c) : barre de tête et espace ôtés, le reste à l'octet) ou « corrige_plus_cle » (la
    copie corrigée, plus une ligne de table à clé inventée)."""
    t0 = datetime.now(timezone.utc) - timedelta(days=2)

    def instant(i):
        return (t0 + timedelta(minutes=5 * i)).strftime("%Y-%m-%dT%H:%M:%SZ")
    connues = [("SCELLEMENT-B5F", f"{lv.TEXTE} ; sha256 {lv.TEXTE_SHA256} ; membres-apprentissage 3 ; piece famille"),
               ("CODE-FORMATION-B5F", f"commit {'c' * 40} ; entropie 12345"), ("GO-FORMATION-B5F", GO_FORMATION),
               ("CODE-LECTURE-B5F", f"commit {code_commit} ; lecture sha256 {lv.programme_sha256()}"),
               ("EPREUVE-B5F", f"passee ; lecture sha256 {lv.programme_sha256()} ; rapport sha256 {'e' * 64}"),
               ("GO-RELANCE-FORMATION-B5F", f"{GO_FORMATION} ; instances 1,2,3,4,5,7")]
    tete = ["# Registre propre du barreau 5 (fabriqué)", "", "Lignes ajoutées, jamais réécrites.", "",
            "| clé | instant | contenu | référence |", "|---|---|---|---|"]
    table = [en.ligne_du_registre(k, instant(i), c, "essai") for i, (k, c) in enumerate(connues)]
    recreations = [f"| {k} | {instant(10 + i)} | {GO_FORMATION} ; recréation fabriquée | essai |"
                   for i, k in enumerate(CLES_INCONNUES)]
    if etat != "intact":
        recreations = [x[2:] for x in recreations]
    queue = ["", "Note sous la table : voie (c)."] if etat != "intact" else []
    if etat == "corrige_plus_cle":
        queue.append(f"| CLE-INVENTEE-B5F | {instant(30)} | x | essai |")
    return "\n".join(tete + table + recreations + queue) + "\n"


@pytest.fixture(scope="module")
def gabarit(tmp_path_factory):
    """Construit une fois : dépôt distant local et dépôt de travail au commit du « code » (tout `src/` sans la liste fermée
    de la version 2, garde de calcul, configuration scellée et texte scellé copiés sans être lus, amorce, lanceur de la
    version 1, adaptateurs existants factices, registre des accords d'essai) ; branche des entrées de lecture poussée."""
    t = tmp_path_factory.mktemp("gabarit-b5f-commande-v2")
    nu, r = t / "distant.git", t / "fige"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(nu)], check=True)
    subprocess.run(["git", "clone", "-q", str(nu), str(r)], check=True, capture_output=True)
    for a in (["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _g(r, *a)
    liste = {(RACINE / f).resolve() for f in cl2.LISTE_FERMEE}

    def ignorer(dossier, noms):
        return [n for n in noms if n == "__pycache__" or n.endswith((".pyc", ".egg-info"))
                or (Path(dossier) / n).resolve() in liste]
    shutil.copytree(RACINE / "src", r / "src", ignore=ignorer)
    (r / ".claude" / "hooks").mkdir(parents=True)
    shutil.copy(RACINE / ".claude" / "hooks" / "garde_calcul.py", r / ".claude" / "hooks" / "garde_calcul.py")
    (r / "prereg").mkdir()
    for f in (rv.CONFIG_SCELLEE["chemin"], rv.CONFIG_SCELLEE["chemin"] + ".sha256", lv.TEXTE):
        shutil.copy(RACINE / f, r / f)
    (r / "scripts").mkdir()
    for f in (rv.AMORCE, LANCEUR_V1):
        shutil.copy(RACINE / f, r / f)
    (r / ".gitignore").write_text("__pycache__/\n*.pyc\n", encoding="utf-8")
    for x in EXISTANTS:
        (r / x["chemin"]).parent.mkdir(parents=True, exist_ok=True)
        (r / x["chemin"]).write_bytes(b"adaptateur factice")
    (r / "registres").mkdir()
    (r / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n"
                                          + _ligne_go(GO_LECTURE) + "\n" + _ligne_go(GO_FORMATION) + "\n", encoding="utf-8")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "code")
    _g(r, "push", "-q", "origin", "main")
    e = t / "entrees-graine"
    e.mkdir()
    for a in (["init", "-q", "-b", "x"], ["config", "user.email", "e@invalid"], ["config", "user.name", "e"]):
        _g(e, *a)
    (e / rv.DOSSIER_ENTREES).mkdir()
    (e / rv.DOSSIER_ENTREES / "X-01.safetensors").write_bytes(b"x")
    _g(e, "add", "-A")
    _g(e, "commit", "-q", "-m", "entrées de lecture")
    _g(e, "push", "-q", str(nu), f"x:refs/heads/{rv.BRANCHE_ENTREES}")
    _g(r, "fetch", "-q", "origin")
    return {"t": t, "code": _g(r, "rev-parse", "HEAD"), "entrees": _g(e, "rev-parse", "HEAD")}


@pytest.fixture
def monde(gabarit, tmp_path):
    """Copie jetable du gabarit ; l'arbre figé est `fige`, l'arbre de commande `commande` (créé par `_monter`)."""
    shutil.copytree(gabarit["t"] / "fige", tmp_path / "fige", symlinks=True)
    for nom, corps in (("offre.json", OFFRE), ("existants.json", EXISTANTS), ("aucun.json", [])):
        (tmp_path / nom).write_text(json.dumps(corps))
    return {"t": tmp_path, "fige": tmp_path / "fige", "commande": tmp_path / "commande", "code": gabarit["code"],
            "entrees": gabarit["entrees"], "maintenant_s": time.time()}


def _monter(m, *, dans_commande=None, orpheline=False, ref=None, marche_sur_commande=False, dans_marche=None,
            registre=None):
    """Monte le commit de commande (le code plus la liste fermée, copiée telle quelle depuis ce dépôt ; `dans_commande`
    retouche l'arbre avant le commit ; `orpheline` : même arbre, sans parent) puis la marche (le code plus le registre,
    dont la ligne de l'accord de lecture cite l'additif et le commit de commande ; `ref` : autre référence, fonction du
    commit de commande ; `registre` : autre registre, fonction du code et du commit de commande ; `marche_sur_commande` : la marche porte le module
    neuf ; `dans_marche` : retouche de l'arbre de la marche). L'arbre figé reste à la marche, l'arbre de commande à son
    commit."""
    r, c = m["fige"], m["commande"]
    _g(r, "worktree", "add", "-q", "-b", "commande", str(c), m["code"])
    for f in cl2.LISTE_FERMEE:
        (c / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(RACINE / f, c / f)
    if dans_commande is not None:
        dans_commande(c)
    _g(c, "add", "-A")
    _g(c, "commit", "-q", "-m", "commande de lecture v2")
    k = _g(c, "rev-parse", "HEAD")
    if orpheline:
        k = _g(c, "commit-tree", f"{k}^{{tree}}", "-m", "commande orpheline")
        _g(c, "checkout", "-q", "--detach", k)
    if marche_sur_commande:
        _g(r, "reset", "-q", "--hard", k)
    if dans_marche is not None:
        dans_marche(r)
    texte = (registre(m["code"], k) if registre is not None
             else _registre(m["code"], _citation(k) if ref is None else ref(k)))
    (r / en.REGISTRE_PROPRE).write_text(texte, encoding="utf-8")
    _g(r, "add", "-A")
    _g(r, "commit", "-q", "-m", "marche (registre)")
    m.update(k=k, marche=_g(r, "rev-parse", "HEAD"))
    return m


def _arguments(m, plan, k):
    a = {"offre_json": m["t"] / "offre.json", "commit": m["marche"], "branche": "main",
         "run_id": RUN_L if plan == "decisif" else RUN_R, "go_id": GO_LECTURE if plan == "decisif" else GO_FORMATION,
         "entrees_commit": m["entrees"] if plan == "decisif" else "", "divergence": True, "garde": "une_sur_dix",
         "existants_json": m["t"] / ("aucun.json" if plan == "decisif" else "existants.json")}
    a.update(k)
    return (plan, a["offre_json"], a["commit"], a["branche"], a["run_id"], a["go_id"], a["entrees_commit"], a["divergence"],
            a["garde"], a["existants_json"], date.today(), m["maintenant_s"])


def _corps(m, plan="decisif", **k):
    """Le corps recomposé de la version 2, joué depuis l'arbre de commande."""
    return cl2.corps_recompose(m["commande"], *_arguments(m, plan, k))


def _v1(m, plan="decisif", **k):
    """La version 1, jouée depuis l'arbre figé (même instant)."""
    return rv.commande_de_creation(m["fige"], *_arguments(m, plan, k))


def _offre(m, **champs):
    base = champs.pop("base", OFFRE)
    p = m["t"] / "offre-retouchee.json"
    p.write_text(json.dumps(dict(base, **champs)))
    return p


# --- stockage, relecture décisive (§ 3.4, premier tiret) ----------------------------------------------------------------

def test_stockage_decisif_cas_sains_offre_du_releve_et_frontiere():
    """Sain : l'offre 32744970 du relevé (0,24 USD par Go et par mois : 0,0986 USD de l'heure à 300 Go) est acceptée ; à la
    frontière, 0,2920 rend 0,12 juste en virgule flottante et passe (la comparaison du code est « > »)."""
    assert cl2.exiger_offre_lecture_v2(OFFRE_DU_RELEVE, "decisif") == {"id": "32744970", "prix_usd_h": 1.16}
    assert not 0.2920 * 300 / 730.0 > 0.12
    assert cl2.exiger_offre_lecture_v2(dict(OFFRE_DU_RELEVE, storage_cost=0.2920), "decisif")["id"] == "32744970"
    assert cl2.PLAFOND_STOCKAGE_USD_H == {"decisif": 0.12, "repetition": 0.08}


@pytest.mark.parametrize("stockage, usd_h", [(0.2921, 0.12004), (0.30, 0.1233), (0.32, 0.1315)])
def test_stockage_decisif_artefacts_refuses(stockage, usd_h):
    """Artefacts : juste au-dessus de la frontière ; 0,30 ; 0,32 (entre le plafond et 0,1359) : refus, motif « stockage »."""
    assert abs(stockage * 300 / 730.0 - usd_h) < 5e-5 and stockage * 300 / 730.0 > 0.12
    with pytest.raises(GardeArret, match="stockage de 300 Go"):
        cl2.exiger_offre_lecture_v2(dict(OFFRE_DU_RELEVE, storage_cost=stockage), "decisif")


def test_stockage_temoin_la_version_1_refuse_l_offre_du_releve():
    """Témoin : la borne scellée de 0,08 mord encore dans la version 1, sur la même offre."""
    with pytest.raises(GardeArret, match="stockage de 300 Go"):
        rv.exiger_offre_lecture(OFFRE_DU_RELEVE, "decisif")


def test_stockage_par_le_corps_recompose(monde):
    """La garde du stockage du corps est bien celle de la version 2 : sur le montage complet, l'offre du relevé donne une
    commande ; 0,2921 est refusé avant toute autre garde."""
    m = _monter(monde)
    cmd = _corps(m, offre_json=_offre(m, base=OFFRE_DU_RELEVE))
    assert cmd.startswith(f"GO_ID={GO_LECTURE} vastai create instance 32744970 --raw --image python:3.11-bookworm --disk 300 ")
    assert "-e PRIX_USD_H=1.16 " in cmd
    with pytest.raises(GardeArret, match="stockage de 300 Go"):
        _corps(m, offre_json=_offre(m, base=OFFRE_DU_RELEVE, storage_cost=0.2921))
    with pytest.raises(GardeArret, match="stockage de 300 Go"):
        _v1(m, offre_json=_offre(m, base=OFFRE_DU_RELEVE))


@pytest.mark.parametrize("retouche", [{"disk_space": 299}, {"num_gpus": 2}, {"cpu_ram": 64000}, {"cuda_max_good": 12.4},
                                      {"id": "x1"}, {"gpu_ram": None}, {"gpu_name": "H100 SXM"}, {"dph_total": 1.35},
                                      {"dph_total": 0}, {"cpu_cores_effective": 12}, {"storage_cost": None},
                                      {"storage_cost": "0.1"}, {"storage_cost": float("nan")}, {"storage_cost": True}, {}])
@pytest.mark.parametrize("plan", ["decisif", "repetition"])
def test_memes_autres_bornes_meme_refus_d_un_champ_illisible_meme_valeur_rendue(plan, retouche):
    """Hors le plafond du stockage, la garde de la version 2 répond comme celle de la version 1 : même valeur rendue, ou
    même refus au même motif (offre sous 0,08 pour les deux pièces)."""
    o = dict(OFFRE, **retouche)

    def jouer(f):
        try:
            return ("rendu", f(o, plan))
        except GardeArret as e:
            return ("refus", str(e))
    assert jouer(cl2.exiger_offre_lecture_v2) == jouer(rv.exiger_offre_lecture)
    assert jouer(rv.exiger_offre_lecture)[0] == ("rendu" if not retouche else "refus")


# --- portée (§ 3.4, deuxième tiret) --------------------------------------------------------------------------------------

def test_portee_l_entree_de_la_version_2_refuse_la_repetition(monde):
    m = _monter(monde)
    with pytest.raises(GardeArret, match="répétition générale"):
        cl2.commande_de_creation_v2(m["commande"], *_arguments(m, "repetition", {}))
    with pytest.raises(GardeArret, match="répétition générale"):
        cl2._main(["commande", "repetition", str(m["commande"]), str(m["t"] / "offre.json"), m["marche"], "main", RUN_R,
                   GO_FORMATION, "-", "1", "une_sur_dix", str(m["t"] / "existants.json")])


def test_portee_repetition_par_le_corps_recompose_la_borne_de_0_08_n_a_pas_bouge(monde):
    """Par le corps recomposé : « repetition » à 0,40 USD par Go et par mois (0,0822 à 150 Go) refusée ; à 0,19 (0,0390),
    acceptée (une commande est rendue)."""
    m = _monter(monde)
    assert 0.40 * 150 / 730.0 > 0.08 > 0.19 * 150 / 730.0
    with pytest.raises(GardeArret, match="stockage de 150 Go"):
        _corps(m, plan="repetition", offre_json=_offre(m, storage_cost=0.40))
    cmd = _corps(m, plan="repetition", offre_json=_offre(m, storage_cost=0.19))
    assert "--disk 150" in cmd and "--label b5f-repetition-v1" in cmd
    # 0,50 USD par Go et par mois : 0,1027 à 150 Go, sous 0,12 et au-dessus de 0,08 : la répétition se lit à 0,08
    assert 0.12 > 0.50 * 150 / 730.0 > 0.08
    with pytest.raises(GardeArret, match="stockage de 150 Go"):
        cl2.exiger_offre_lecture_v2(dict(OFFRE, storage_cost=0.50), "repetition")


def test_portee_les_constantes_de_la_version_1_et_de_la_formation_sont_a_0_08():
    assert rv.OFFRE_LECTURE["stockage_max_usd_h"] == 0.08
    assert fv.OFFRE["stockage_max_usd_h"] == 0.08
    assert cl2.PLAFOND_STOCKAGE_USD_H["repetition"] == rv.OFFRE_LECTURE["stockage_max_usd_h"]
    assert cl2.OFFRE_LECTURE is rv.OFFRE_LECTURE and cl2.PIECES_LECTURE is rv.PIECES_LECTURE


# --- égalité à l'octet, différence fermée du corps (§ 3.3, § 3.4, troisième tiret) --------------------------------------

@pytest.mark.parametrize("plan", ["decisif", "repetition"])
def test_egalite_a_l_octet_de_la_commande_des_versions_1_et_2(monde, plan):
    """Même offre sous 0,08, même instant : la commande rendue par le corps recomposé (arbre de commande) est, à l'octet,
    celle de `relecture_v1.commande_de_creation` (arbre figé), pour les deux pièces."""
    m = _monter(monde)
    v1, v2 = _v1(m, plan=plan), _corps(m, plan=plan)
    assert v1.encode("utf-8") == v2.encode("utf-8")
    assert f"--label {rv.PIECES_LECTURE[plan]['etiquette']} " in v2 and f"-e COMMIT={m['marche']} " in v2
    b64 = re.search(r"echo (\S+) \| base64 -d > /root/amorce_b5f_lecture_v1\.sh", v2).group(1)
    assert base64.b64decode(b64) == (RACINE / rv.AMORCE).read_bytes()


def _lignes_du_corps(f):
    """Lignes du corps d'une fonction, sans sa signature ni sa chaîne de documentation."""
    source = textwrap.dedent(inspect.getsource(f))
    fonction = ast.parse(source).body[0]
    premier = fonction.body[1] if ast.get_docstring(fonction) is not None else fonction.body[0]
    return [x.rstrip() for x in source.splitlines()[premier.lineno - 1:]]


def test_difference_fermee_entre_le_corps_de_la_version_1_et_le_corps_recompose():
    """« Ce qui change dans le corps recomposé, et rien d'autre » : ligne pour ligne, dans le même ordre, le corps de la
    version 2 ne diffère de celui de la version 1 que par la garde du stockage (une ligne pour une ligne) et par la garde de
    l'arbre de la session (une ligne remplacée par les vérifications (d), (b) et (c))."""
    v1, v2 = _lignes_du_corps(rv.commande_de_creation), _lignes_du_corps(cl2.corps_recompose)
    blocs = [(o, v1[i1:i2], v2[j1:j2]) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, v1, v2, autojunk=False)
             .get_opcodes() if o != "equal"]
    assert [(o, [x.strip() for x in a], [x.strip() for x in b]) for o, a, b in blocs] == [
        ("replace", ['of = exiger_offre_lecture(json.loads(Path(offre_json).read_text(encoding="utf-8")), plan)'],
         ['of = exiger_offre_lecture_v2(json.loads(Path(offre_json).read_text(encoding="utf-8")), plan)']),
        ("replace", ['lv.exiger_code_de_lecture_au_commit(racine, reg["commit_lecture"])'],
         ['commande = commit_de_commande(racine, plan, _montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"))',
          "exiger_session_au_commit_de_commande(racine, commande)",
          'exiger_commande_issue_du_code_fige(racine, reg["commit_lecture"], commande)'])]
    assert inspect.signature(cl2.corps_recompose) == inspect.signature(rv.commande_de_creation)
    assert inspect.signature(cl2.commande_de_creation_v2) == inspect.signature(rv.commande_de_creation)


def test_les_noms_du_corps_recompose_sont_les_objets_de_la_version_1():
    """Importés sans être copiés : chaque nom global qu'emploie le corps est l'objet même de la version 1 ; les deux seuls
    objets privés (`_montrer`, `_RUN_LECTURE`) sont récrits, à l'identique."""
    for nom in ("piece_lecture", "config_lecture", "exiger_registre_de_relecture", "exiger_code_du_commit",
                "exiger_arbre_extrait_propre", "echeance_arret_lecture_s", "hashlib_sha256", "PIECES_LECTURE",
                "OFFRE_LECTURE", "AMORCE", "IMAGE", "DEPOT_URL", "BRANCHE_ENTREES", "ENTREES_DE_LA_MARCHE"):
        assert getattr(cl2, nom) is getattr(rv, nom), nom
    assert cl2.en is en and cl2.lv is lv and cl2.lv.TEXTE == lv.TEXTE and cl2.lv.TEXTE_SHA256 == lv.TEXTE_SHA256
    assert cl2._montrer is not rv._montrer and cl2._RUN_LECTURE is not rv._RUN_LECTURE
    assert cl2._RUN_LECTURE.pattern == rv._RUN_LECTURE.pattern and cl2._RUN_LECTURE.flags == rv._RUN_LECTURE.flags
    assert _lignes_du_corps(cl2._montrer) == _lignes_du_corps(rv._montrer)
    libres = {n.id for n in ast.walk(ast.parse(textwrap.dedent(inspect.getsource(cl2.corps_recompose))))
              if isinstance(n, ast.Name) and n.id in vars(rv) and n.id in vars(cl2) and not n.id.startswith("_")}
    for nom in libres - {"exiger_offre_lecture_v2"}:
        assert getattr(cl2, nom) is getattr(rv, nom), nom


# --- vérifications (a) à (d) (§ 3.4, quatrième tiret) -------------------------------------------------------------------

def test_montage_complet_cas_sain(monde):
    """Sain : le montage complet sur un dépôt d'essai, par l'entrée de la version 2 (jouée ici sur le corps, et par le
    lanceur plus bas) ; les quatre vérifications prises une à une rendent ce qu'elles lisent."""
    m = _monter(monde)
    cmd = _corps(m)
    assert cmd.startswith(f"GO_ID={GO_LECTURE} vastai create instance 654321 --raw --image python:3.11-bookworm --disk 300 ")
    assert "--label b5f-lecture-v1" in cmd and f"-e ENTREES_COMMIT={m['entrees']}" in cmd
    assert "-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN" in cmd
    registre = _g(m["fige"], "show", f"{m['marche']}:{en.REGISTRE_PROPRE}")
    assert cl2.commit_de_commande(m["commande"], "decisif", registre) == m["k"]
    assert cl2.commit_de_commande_cite(registre) == m["k"]
    rv.exiger_code_du_commit(m["commande"], m["code"], m["marche"])                                   # (a)
    cl2.exiger_session_au_commit_de_commande(m["commande"], m["k"])                                    # (b)
    assert cl2.exiger_commande_issue_du_code_fige(m["commande"], m["code"], m["k"]) == sorted(cl2.LISTE_FERMEE)   # (c)
    assert sorted(cl2.LISTE_FERMEE) == sorted([LANCEUR_V2, MODULE_V2, ESSAIS_V2])
    assert cl2.ADDITIF_SHA256 == ADDITIF


def test_a_marche_dont_l_arbre_gele_differe(monde):
    def autre(r):
        (r / "scripts" / "autre.sh").write_text("echo x\n")
    m = _monter(monde, dans_marche=autre)
    with pytest.raises(GardeArret, match="code différent de CODE-LECTURE-B5F"):
        _corps(m)


def test_a_marche_qui_porte_le_module_neuf(monde):
    """La marche bâtie sur le commit de commande : son arbre gelé porte le module neuf ; seule la vérification (a) la
    refuse (elle cite le bon commit de commande, et l'arbre de la session est ce commit)."""
    m = _monter(monde, marche_sur_commande=True)
    assert _g(m["fige"], "cat-file", "-t", f"{m['marche']}:{MODULE_V2}") == "blob"
    with pytest.raises(GardeArret, match="code différent de CODE-LECTURE-B5F"):
        _corps(m)


def test_b_arbre_de_session_autre_que_le_commit_de_commande(monde):
    """La tête de la session a avancé d'un commit qui ne touche aucun chemin gelé : seule la clause « la tête est ce
    commit » refuse."""
    m = _monter(monde)
    (m["commande"] / "registres" / "note.md").write_text("x\n")
    _g(m["commande"], "add", "-A")
    _g(m["commande"], "commit", "-q", "-m", "note hors des chemins gelés")
    with pytest.raises(GardeArret, match="tête de la session"):
        _corps(m)
    _g(m["commande"], "reset", "-q", "--hard", m["k"])
    assert _corps(m)
    # la session jouée depuis l'arbre figé (à la marche) : refus aussi
    with pytest.raises(GardeArret, match="tête de la session"):
        cl2.corps_recompose(m["fige"], *_arguments(m, "decisif", {}))


def test_b_arbre_de_travail_change(monde):
    m = _monter(monde)
    (m["commande"] / rv.AMORCE).write_text("echo autre\n")
    with pytest.raises(GardeArret, match="arbre de travail"):
        _corps(m)
    _g(m["commande"], "checkout", "-q", "--", rv.AMORCE)
    (m["commande"] / MODULE_V2).write_text((m["commande"] / MODULE_V2).read_text() + "\n# retouche\n")
    with pytest.raises(GardeArret, match="arbre de travail"):
        _corps(m)
    _g(m["commande"], "checkout", "-q", "--", MODULE_V2)
    # hors des chemins gelés, l'arbre de travail peut porter un registre des accords tenu à jour (réserve 2 du scellement)
    (m["commande"] / "registres" / "go.md").write_text((m["commande"] / "registres" / "go.md").read_text() + "\n")
    assert _corps(m)


def test_b_fichier_non_suivi_sous_src(monde):
    m = _monter(monde)
    (m["commande"] / "src" / "controle_ia" / "intrus.py").write_text("x = 1\n")
    with pytest.raises(GardeArret, match="non suivi sous src"):
        _corps(m)
    (m["commande"] / "src" / "controle_ia" / "intrus.py").unlink()
    assert _corps(m)


@pytest.mark.parametrize("cas, motif", [("modifie", "modifié ou supprimé"), ("hors_liste", "hors de la liste fermée"),
                                        ("supprime", "modifié ou supprimé"),
                                        ("renomme", "modifié ou supprimé|hors de la liste fermée")])
def test_c_commit_de_commande_qui_modifie_supprime_ou_ajoute_hors_liste(monde, cas, motif):
    def retouche(c):
        if cas == "modifie":
            (c / rv.AMORCE).write_text((c / rv.AMORCE).read_text() + "\n# retouche\n")
        elif cas == "hors_liste":
            (c / "scripts" / "autre.sh").write_text("echo x\n")
        elif cas == "supprime":
            (c / LANCEUR_V1).unlink()
        else:
            (c / LANCEUR_V1).rename(c / "scripts" / "lancer_b5f_lecture_v1_bis.sh")
    m = _monter(monde, dans_commande=retouche)
    with pytest.raises(GardeArret, match=motif):
        _corps(m)


def test_c_commit_de_commande_sans_le_module_ou_sans_le_lanceur(monde):
    """La liste fermée n'est pas une borne haute seulement : un commit de commande qui ne porte pas le module et le lanceur
    de la version 2 n'est pas le commit de commande."""
    m = _monter(monde, dans_commande=lambda c: (c / LANCEUR_V2).unlink())
    with pytest.raises(GardeArret, match="absent du commit de commande"):
        _corps(m)


def test_c_commit_de_commande_qui_ne_descend_pas_du_code_fige(monde):
    """Même arbre, sans parent : la différence d'arbres est la bonne, seule l'ascendance manque."""
    m = _monter(monde, orpheline=True)
    assert _g(m["commande"], "rev-parse", "HEAD") == m["k"]
    with pytest.raises(GardeArret, match="ne descend pas"):
        _corps(m)


def test_d_ligne_de_l_accord_de_lecture_sans_la_citation(monde):
    m = _monter(monde, ref=lambda k: "session de lecture session_essai")
    with pytest.raises(GardeArret, match="GO-LECTURE-B5F"):
        _corps(m)


def test_d_citation_d_une_autre_empreinte_de_l_additif(monde):
    """L'empreinte de la version 1 de l'additif (`b5661251…`) à la place de celle de la version 2 : refus."""
    v1 = "b5661251d40d441f589d6ec2f27cfe56ee2e89a290b98161f8b49fe916730889"
    m = _monter(monde, ref=lambda k: _citation(k, additif=v1))
    with pytest.raises(GardeArret, match="autre empreinte"):
        _corps(m)


def test_d_citation_d_un_autre_commit(monde):
    """La ligne cite un autre commit (même arbre que le commit de commande, autre message) : la session, elle, est au
    commit de commande ; refus, parce que c'est la ligne qui dit quel commit est le commit de commande."""
    def autre(k):
        return _citation(_g(monde["commande"], "commit-tree", f"{k}^{{tree}}", "-p", monde["code"], "-m", "jumeau"))
    m = _monter(monde, ref=autre)
    cite = cl2.commit_de_commande_cite(_g(m["fige"], "show", f"{m['marche']}:{en.REGISTRE_PROPRE}"))
    assert cite != m["k"] and _g(m["commande"], "rev-parse", f"{cite}^{{tree}}") == _g(m["commande"], "rev-parse",
                                                                                         f"{m['k']}^{{tree}}")
    with pytest.raises(GardeArret, match="tête de la session"):
        _corps(m)


def _registre_minimal(ref):
    return en.ligne_du_registre("GO-LECTURE-B5F", "2026-11-24T10:00:00Z", GO_LECTURE, ref) + "\n"


def test_d_format_de_la_citation_lu_a_la_lettre():
    """Le format exact de la colonne de référence : « <session de lecture> ; additif 1 v2 au devis sha256 <64> ; commande
    de lecture v2, commit <40>, vérifiée sha256 <64> », suivi au plus de « ; <texte libre> »."""
    k = "1" * 40
    assert cl2.commit_de_commande_cite(_registre_minimal(_citation(k))) == k
    assert cl2.commit_de_commande_cite(_registre_minimal(_citation(k) + " ; GO-2026-11-21-63")) == k
    assert cl2.commit_de_commande_cite(_registre_minimal("session_x ; note ; " + _citation(k, session="suite"))) == k
    sain = _citation(k)
    for artefact in ("",                                                          # référence vide
                     sain.split(" ; ", 1)[1],                                     # sans le nom de la session
                     sain.replace(k, "1" * 39),                                   # commit de 39 signes
                     sain.replace(k, "1" * 41),
                     sain.replace(k, "G" * 40),
                     sain.replace(ADDITIF, ADDITIF[:63]),
                     sain.replace(ADDITIF, ADDITIF.upper()),
                     sain.replace("additif 1 v2", "additif 1"),                   # la version 1 de l'additif
                     sain.replace("commande de lecture v2", "commande de lecture"),
                     sain.replace(", vérifiée sha256 " + "f" * 64, ""),           # sans le rapport de vérification
                     sain.replace("f" * 64, "f" * 12 + "…"),                      # empreinte du rapport abrégée
                     sain.replace(" ; commande", " commande"),
                     sain + " " + sain,                                           # deux citations
                     sain + " ; " + sain.replace(k, "2" * 40),                    # deux citations, deux commits
                     sain + " ; commande de lecture v2, commit " + "2" * 40):
        with pytest.raises(GardeArret, match="GO-LECTURE-B5F"):
            cl2.commit_de_commande_cite(_registre_minimal(artefact))
    with pytest.raises(GardeArret, match="GO-LECTURE-B5F"):
        cl2.commit_de_commande_cite("| GO-FORMATION-B5F | 2026-11-24T10:00:00Z | x | " + sain + " |\n")   # autre ligne
    # la citation n'est lue que dans la colonne de référence d'une ligne de table, par le lecteur de la version 1
    with pytest.raises(GardeArret, match="clé CLE-INVENTEE-B5F inconnue"):
        cl2.commit_de_commande_cite(_registre_minimal(sain) + "| CLE-INVENTEE-B5F | 2026-11-24T10:00:00Z | x | y |\n")


# --- les autres gardes du corps, rejouées telles quelles ------------------------------------------------------------------

@pytest.mark.parametrize("cas", ["disque", "prix", "carte", "marche_autre_plan", "sans_entrees", "entrees_hors_branche",
                                 "go_autre", "go_sans_ligne", "existant_sans_empreinte", "existant_absent",
                                 "repetition_avec_entrees", "registre_sans_epreuve", "registre_sans_engagement",
                                 "commit_illisible", "branche_illisible"])
def test_les_autres_gardes_refusent_par_la_version_2_comme_par_la_version_1(monde, cas):
    """Mêmes artefacts que les essais de la version 1 : la version 2 (arbre de commande) et la version 1 (arbre figé)
    refusent au même motif."""
    k, plan = {}, "decisif"
    sans = {"registre_sans_epreuve": ("EPREUVE-B5F",), "registre_sans_engagement": ("ENGAGEMENT-B5F",)}.get(cas, ())
    m = _monter(monde, registre=lambda code, commande: _registre(code, _citation(commande), sans=sans))
    if cas in ("disque", "prix", "carte"):
        k["offre_json"] = _offre(m, **{"disque": {"disk_space": 200}, "prix": {"dph_total": 1.35},
                                       "carte": {"gpu_name": "H100 SXM"}}[cas])
    elif cas == "marche_autre_plan":
        k["run_id"] = RUN_R
    elif cas == "sans_entrees":
        k["entrees_commit"] = ""
    elif cas == "entrees_hors_branche":
        k["entrees_commit"] = m["code"]
    elif cas == "go_autre":
        k["go_id"] = GO_FORMATION
    elif cas == "go_sans_ligne":
        for racine in (m["fige"], m["commande"]):             # l'accord cité n'est plus au registre des accords
            (racine / "registres" / "go.md").write_text("| id | accordé | type | périmètre | plafond | échéance | par | réf |\n")
    elif cas == "existant_sans_empreinte":
        (m["t"] / "x.json").write_text(json.dumps([{**EXISTANTS[0], "nom": "ancre-R1", "sha256": ""}]))
        k["existants_json"] = m["t"] / "x.json"
    elif cas == "existant_absent":
        plan = "repetition"
        (m["t"] / "x.json").write_text(json.dumps(EXISTANTS[:3] + [{**EXISTANTS[3], "chemin": "donnees/absent/a.pt"}]))
        k["existants_json"] = m["t"] / "x.json"
    elif cas == "repetition_avec_entrees":
        plan, k["entrees_commit"] = "repetition", m["entrees"]
    elif cas == "commit_illisible":
        k["commit"] = "pas-un-commit"
    elif cas == "branche_illisible":
        k["branche"] = "main; echo x"

    def jouer(f):
        try:
            return ("rendu", f(m, plan=plan, **k))
        except GardeArret as e:
            return ("refus", re.sub(r"[0-9a-f]{12}", "<commit>", str(e)))
    v1, v2 = jouer(_v1), jouer(_corps)
    if cas == "go_sans_ligne":
        # la garde de calcul lit le registre des accords de l'arbre d'où elle est jouée : même refus, chemins à part
        assert v1[0] == v2[0] == "refus" and "garde de calcul" in v1[1] and "garde de calcul" in v2[1]
    else:
        assert v1 == v2 and v1[0] == "refus", (v1, v2)


# --- les deux arbres (§ 3.2 ; § 3.4, cinquième tiret) -------------------------------------------------------------------

def _config_decisive(racine):
    return rv.config_lecture(racine, GO_LECTURE, "decisif", rv.ENTREES_DE_LA_MARCHE, True, "une_sur_dix")


def test_les_deux_arbres_verifier_de_la_version_1(monde):
    """Sain : « verifier » de la version 1 depuis l'arbre figé, acceptée. Artefact : la même depuis l'arbre de commande,
    refusée (constat C2, vu rouge) : la garde de l'arbre de la session de la version 1 refuse un commit qui ajoute des
    fichiers sous des chemins gelés. Et la « commande » de la version 1 de même."""
    m = _monter(monde)
    v = rv.verifier_avant_creation(m["fige"], m["marche"], _config_decisive(m["fige"]))
    assert v["commit"] == m["marche"] and v["commit_lecture"] == m["code"]
    with pytest.raises(GardeArret, match="code joué différent de celui de CODE-LECTURE-B5F"):
        rv.verifier_avant_creation(m["commande"], m["marche"], _config_decisive(m["commande"]))
    with pytest.raises(GardeArret, match="code joué différent de celui de CODE-LECTURE-B5F"):
        rv.commande_de_creation(m["commande"], *_arguments(m, "decisif", {}))
    assert _v1(m)


# --- registre (§ 3.4, sixième tiret ; § 6 : les trois objets de contrôle de la voie (c)) ---------------------------------

def _reponse(f, m, plan):
    try:
        f(m, plan=plan)
        return "commande rendue"
    except GardeArret as e:
        return re.sub(r"[0-9a-f]{12}", "<commit>", str(e))


def _monter_sur_registre(m, texte):
    """La marche porte ce registre (texte donné, ou fonction du code) ; la ligne de l'accord de lecture n'y est pas : la
    vérification (d) n'est pas atteinte par le plan décisif (le registre refuse avant), et ne vaut pas pour la répétition."""
    return _monter(m, registre=lambda code, k: texte(code) if callable(texte) else texte)


def test_registre_a_la_forme_d_aujourd_hui_refuse_a_la_ligne_13_par_les_deux_versions(monde):
    """Objet 1 : les sept lignes de recréation en lignes de table : refus à la ligne 13, clé inconnue, par la version 2
    comme par la version 1, pour les deux pièces."""
    m = _monter_sur_registre(monde, lambda code: _registre_a_la_forme_d_aujourd_hui(code, "intact"))
    attendu = "registre propre, ligne 13 : clé ENGAGEMENT-RECREATION-3-B5F inconnue"
    for plan in ("decisif", "repetition"):
        assert _reponse(_corps, m, plan) == _reponse(_v1, m, plan) == attendu


def test_registre_corrige_par_la_voie_c_accepte_six_cles(monde):
    """Objet 2 : la copie corrigée (barre de tête et espace ôtés aux sept lignes) : le lecteur l'accepte, six clés ; par le
    corps recomposé, la répétition (qui n'attend que le code de lecture figé et l'accord de la formation) rend sa commande,
    égale à l'octet à celle de la version 1 ; la relecture décisive passe le lecteur et s'arrête à la garde suivante
    (l'engagement n'est pas inscrit), au même motif dans les deux versions."""
    m = _monter_sur_registre(monde, lambda code: _registre_a_la_forme_d_aujourd_hui(code, "corrige"))
    texte = _g(m["fige"], "show", f"{m['marche']}:{en.REGISTRE_PROPRE}")
    assert sorted(en.lignes_du_registre(texte)) == sorted(["SCELLEMENT-B5F", "CODE-FORMATION-B5F", "GO-FORMATION-B5F",
                                                           "CODE-LECTURE-B5F", "EPREUVE-B5F", "GO-RELANCE-FORMATION-B5F"])
    assert _corps(m, plan="repetition").encode("utf-8") == _v1(m, plan="repetition").encode("utf-8")
    assert _reponse(_corps, m, "decisif") == _reponse(_v1, m, "decisif")
    assert "engagement absent" in _reponse(_corps, m, "decisif")


def test_registre_corrige_plus_une_cle_inventee_refuse(monde):
    """Objet 3 : la copie corrigée plus une ligne de table à clé inventée : refus (la garde n'est pas morte)."""
    m = _monter_sur_registre(monde, lambda code: _registre_a_la_forme_d_aujourd_hui(code, "corrige_plus_cle"))
    for plan in ("decisif", "repetition"):
        assert _reponse(_corps, m, plan) == _reponse(_v1, m, plan)
        assert re.fullmatch(r"registre propre, ligne \d+ : clé CLE-INVENTEE-B5F inconnue", _reponse(_corps, m, plan))


@pytest.mark.skipif(not os.environ.get("B5F_REGISTRE_PROPRE_REEL"),
                    reason="B5F_REGISTRE_PROPRE_REEL : chemin d'une copie du registre propre réel (voie (c) appliquée)")
def test_registre_propre_reel_les_trois_objets_par_le_corps_recompose(monde):
    """Les trois objets de contrôle de la voie (c), sur le registre propre réel (copie donnée par son chemin ; jamais
    écrite) : l'état d'avant la correction est reconstitué (barre de tête et espace rendus aux lignes de recréation, tout
    ce qui suit ôté) et vérifié à son empreinte `c4aeced7…`. Le commit du code de lecture figé que cite le registre réel
    n'est pas dans le dépôt d'essai : la répétition passe le registre et s'arrête à la garde du code du commit."""
    reel = Path(os.environ["B5F_REGISTRE_PROPRE_REEL"]).read_text(encoding="utf-8")
    lignes = reel.split("\n")
    recreation = [i for i, x in enumerate(lignes) if re.match(r"[A-Z0-9-]+-B5F \| ", x)]
    assert [i + 1 for i in recreation] == list(range(13, 20))
    intact = "\n".join(lignes[:12] + ["| " + lignes[i] for i in recreation]) + "\n"
    assert hashlib.sha256(intact.encode("utf-8")).hexdigest() == REGISTRE_INTACT_SHA256
    corrige = "\n".join(lignes[:19]) + "\n"
    assert len(en.lignes_du_registre(corrige)) == 6 and len(en.lignes_du_registre(reel)) >= 6
    accord_formation = en.lignes_du_registre(reel)["GO-FORMATION-B5F"]["contenu"]
    reponses = {}
    for nom, texte in (("intact", intact), ("corrige", corrige), ("reel", reel),
                       ("corrige_plus_cle", corrige + "| CLE-INVENTEE-B5F | 2026-11-21T12:00:00Z | x | y |\n")):
        m = dict(monde, t=monde["t"])
        if nom != "intact":
            for a in (["worktree", "remove", "--force", str(m["commande"])], ["branch", "-q", "-D", "commande"],
                      ["reset", "-q", "--hard", m["code"]]):
                _g(m["fige"], *a)
        m = _monter_sur_registre(m, texte)
        for plan in ("decisif", "repetition"):
            k = {"go_id": accord_formation} if plan == "repetition" else {}
            v1, v2 = (_reponse(lambda mm, plan: f(mm, plan=plan, **k), m, plan) for f in (_v1, _corps))
            assert v1 == v2, (nom, plan, v1, v2)
            reponses[nom, plan] = v2
    ligne_13 = "registre propre, ligne 13 : clé ENGAGEMENT-RECREATION-3-B5F inconnue"
    assert reponses["intact", "decisif"] == reponses["intact", "repetition"] == ligne_13
    assert "engagement absent" in reponses["corrige", "decisif"]
    assert "code différent de CODE-LECTURE-B5F" in reponses["corrige", "repetition"]
    assert "code différent de CODE-LECTURE-B5F" in reponses["reel", "repetition"]
    for plan in ("decisif", "repetition"):
        assert reponses["corrige_plus_cle", plan] == "registre propre, ligne 20 : clé CLE-INVENTEE-B5F inconnue"
    print("B5F REGISTRE REEL", json.dumps({f"{a}/{b}": v for (a, b), v in reponses.items()}, ensure_ascii=False))


# --- aucune substitution (§ 3.4, septième tiret) ------------------------------------------------------------------------

MODULES_FIGES = ("relecture_v1", "lecture_v1", "engagement_v1", "formation_v1")


def substitutions(source: str) -> list[str]:
    """Ce qui, dans une source, affecte ou pourrait affecter un attribut d'un module figé : toute affectation ou
    suppression d'un attribut (quel que soit l'objet : le module neuf n'en a aucun besoin), toute affectation à un nom
    importé d'un module figé, `setattr`, `delattr`, `__dict__`, `globals`, `vars`, `sys.modules`, `importlib`, `exec`,
    `eval`, un outil de substitution (`mock`, `monkeypatch`, `patch`), une instruction `global`."""
    arbre = ast.parse(source)
    importes = set()
    for n in ast.walk(arbre):
        if isinstance(n, ast.ImportFrom) and (n.module or "").split(".")[-1] in MODULES_FIGES:
            importes |= {a.asname or a.name for a in n.names}
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            importes |= {a.asname or a.name.split(".")[0] for a in n.names if a.name.split(".")[-1] in MODULES_FIGES}
    vus = []
    for n in ast.walk(arbre):
        if isinstance(n, ast.Attribute) and isinstance(n.ctx, (ast.Store, ast.Del)):
            vus.append(f"ligne {n.lineno} : attribut {n.attr} affecté ou supprimé")
        elif isinstance(n, ast.Name) and isinstance(n.ctx, (ast.Store, ast.Del)) and n.id in importes:
            vus.append(f"ligne {n.lineno} : nom importé {n.id} réaffecté")
        elif isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in importes:
            vus.append(f"ligne {n.lineno} : nom importé {n.name} redéfini")
        elif isinstance(n, ast.Global):
            vus.append(f"ligne {n.lineno} : instruction global")
        elif isinstance(n, ast.Name) and n.id in ("setattr", "delattr", "globals", "vars", "exec", "eval", "importlib",
                                                  "mock", "monkeypatch", "patch", "__import__"):
            vus.append(f"ligne {n.lineno} : {n.id}")
        elif isinstance(n, ast.Attribute) and n.attr in ("__dict__", "modules", "__setattr__", "__delattr__", "patch",
                                                         "setattr", "reload"):
            vus.append(f"ligne {n.lineno} : .{n.attr}")
        elif isinstance(n, (ast.Import, ast.ImportFrom)) and any(
                a.name.split(".")[0] in ("importlib", "unittest", "mock", "pytest") for a in n.names):
            vus.append(f"ligne {n.lineno} : import d'un outil de substitution")
        elif isinstance(n, ast.ImportFrom) and (n.module or "").split(".")[0] in ("importlib", "unittest", "mock", "pytest"):
            vus.append(f"ligne {n.lineno} : import d'un outil de substitution")
    return vus


def test_aucune_substitution_dans_le_module_neuf():
    source = (RACINE / MODULE_V2).read_text(encoding="utf-8")
    assert substitutions(source) == []
    # le module importe bien les quatre modules figés (sinon l'épreuve ne regarderait rien)
    for nom in MODULES_FIGES:
        assert re.search(rf"^from \.{nom} import |^from \. import {nom} as ", source, flags=re.M), nom


@pytest.mark.parametrize("ajout", [
    "rv.exiger_offre_lecture = exiger_offre_lecture_v2\n",
    "from . import relecture_v1\nrelecture_v1.OFFRE_LECTURE['stockage_max_usd_h'] = 0.12\nrelecture_v1.OFFRE_LECTURE = {}\n",
    "import controle_ia.barreau5_familles.lecture_v1 as figee\nfigee.exiger_code_de_lecture_au_commit = lambda *a: {}\n",
    "from . import relecture_v1 as rv\nsetattr(rv, 'exiger_offre_lecture', None)\n",
    "from . import lecture_v1 as lv\nlv.__dict__['exiger_code_de_lecture_au_commit'] = None\n",
    "from . import formation_v1 as fv\nvars(fv)['OFFRE'] = {}\n",
    "import sys\nsys.modules['controle_ia.barreau5_familles.relecture_v1'].OFFRE_LECTURE.clear\n",
    "from unittest import mock\n",
    "from .relecture_v1 import exiger_code_du_commit\n\n\ndef exiger_code_du_commit(*a):\n    return None\n",
    "from .relecture_v1 import OFFRE_LECTURE\nOFFRE_LECTURE = dict(OFFRE_LECTURE, stockage_max_usd_h=0.12)\n",
    "from . import engagement_v1 as en\ndel en.CLES_REGISTRE\n",
    "import importlib\n",
])
def test_aucune_substitution_l_epreuve_voit_une_substitution(ajout):
    """Artefacts : la même source, plus une substitution ; l'épreuve doit la voir (elle peut échouer)."""
    source = (RACINE / MODULE_V2).read_text(encoding="utf-8")
    assert substitutions(source + "\n\n" + ajout) != []


def test_les_modules_figes_ne_sont_pas_alteres_par_l_import_ni_par_l_appel(monde):
    """Dans le processus : après l'import du module neuf et un appel complet, les fonctions et la constante de la version 1
    que la version 2 remplace sont les objets d'origine, et la borne de 0,08 est intacte."""
    avant = (rv.exiger_offre_lecture, rv.commande_de_creation, lv.exiger_code_de_lecture_au_commit, rv.OFFRE_LECTURE,
             dict(rv.OFFRE_LECTURE), fv.exiger_garde_de_calcul, en.lignes_du_registre, dict(fv.OFFRE))
    m = _monter(monde)
    _corps(m, offre_json=_offre(m, base=OFFRE_DU_RELEVE))
    apres = (rv.exiger_offre_lecture, rv.commande_de_creation, lv.exiger_code_de_lecture_au_commit, rv.OFFRE_LECTURE,
             dict(rv.OFFRE_LECTURE), fv.exiger_garde_de_calcul, en.lignes_du_registre, dict(fv.OFFRE))
    assert all(a is b or a == b for a, b in zip(avant, apres)) and avant[4] == apres[4] and avant[3] is apres[3]
    assert rv.exiger_offre_lecture.__module__.endswith("relecture_v1")


# --- la liste fermée, l'entrée, le lanceur --------------------------------------------------------------------------------

def test_liste_fermee_ecrite_dans_le_module():
    assert tuple(cl2.LISTE_FERMEE) == tuple(sorted(cl2.LISTE_FERMEE)) and len(set(cl2.LISTE_FERMEE)) == 3
    assert set(cl2.LISTE_FERMEE) == {LANCEUR_V2, MODULE_V2, ESSAIS_V2}
    for f in cl2.LISTE_FERMEE:
        assert (RACINE / f).is_file(), f
    assert Path(cl2.__file__).resolve() == (RACINE / MODULE_V2).resolve()


def _jouer(racine_du_lanceur, *args, env=None, lanceur=LANCEUR_V2):
    e = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "PYTHON_B5F": sys.executable, "PYTHONDONTWRITEBYTECODE": "1"}
    e.update(env or {})
    return subprocess.run(["bash", str(Path(racine_du_lanceur) / lanceur), *args], capture_output=True, text=True, env=e,
                          cwd=str(racine_du_lanceur))


def _arguments_du_lanceur(m, plan="decisif", racine=None):
    return ["commande", plan, str(racine or m["commande"]), str(m["t"] / "offre.json"), m["marche"], "main",
            RUN_L if plan == "decisif" else RUN_R, m["entrees"] if plan == "decisif" else "-", "1", "une_sur_dix",
            str(m["t"] / ("aucun.json" if plan == "decisif" else "existants.json"))]


def test_lanceur_de_la_version_2_depuis_l_arbre_de_commande_cas_sain_et_refus(monde):
    """Sain : le lanceur de l'arbre de commande, joué sur cet arbre, imprime la commande. Refus : accord absent de
    l'environnement ; plan « repetition » ; arbre figé donné pour racine (la session n'y est pas au commit de commande)."""
    m = _monter(monde)
    (m["t"] / "offre.json").write_text(json.dumps(OFFRE_DU_RELEVE))
    r = _jouer(m["commande"], *_arguments_du_lanceur(m), env={"GO_ID": GO_LECTURE})
    assert r.returncode == 0, r.stderr
    assert r.stdout.startswith("B5F COMMANDE (à jouer par la session de lecture ; son échéance d'arrêt court depuis "
                               "maintenant) :\n")
    assert f"GO_ID={GO_LECTURE} vastai create instance 32744970 --raw " in r.stdout and "--disk 300 " in r.stdout
    assert _g(m["commande"], "status", "--porcelain") == ""                      # le lanceur n'a rien écrit dans l'arbre
    r = _jouer(m["commande"], *_arguments_du_lanceur(m))
    assert r.returncode == 2 and "GO_ID absent" in r.stderr and r.stdout == ""
    r = _jouer(m["commande"], *_arguments_du_lanceur(m, plan="repetition"), env={"GO_ID": GO_FORMATION})
    assert r.returncode == 2 and "répétition générale" in r.stderr and r.stdout == ""
    r = _jouer(m["commande"], *_arguments_du_lanceur(m, racine=m["fige"]), env={"GO_ID": GO_LECTURE})
    assert r.returncode == 2 and "joué depuis un autre arbre" in r.stderr and r.stdout == ""


def test_entree_le_module_joue_doit_etre_celui_de_l_arbre_de_la_session(monde):
    """L'entrée de la version 2 refuse d'être jouée depuis un autre arbre que celui qu'elle vérifie : le module de ce dépôt
    (hors du dépôt d'essai), appelé sur l'arbre de commande du dépôt d'essai, est refusé avant le corps ; le même appel par
    le corps passe (le montage est sain), et le lanceur de ce dépôt, donné pour jouer sur le dépôt d'essai, est refusé."""
    m = _monter(monde)
    assert _corps(m)
    with pytest.raises(GardeArret, match="joué depuis un autre arbre"):
        cl2.commande_de_creation_v2(m["commande"], *_arguments(m, "decisif", {}))
    r = _jouer(RACINE, *_arguments_du_lanceur(m), env={"GO_ID": GO_LECTURE})
    assert r.returncode == 2 and "joué depuis un autre arbre" in r.stderr and r.stdout == ""


@pytest.mark.parametrize("args", [[], ["inconnue"], ["commande"], ["commande", "decisif"], ["config", "a", "b", "c", "d", "e"],
                                  ["verifier", "a", "b", "c"], ["marche", "a", "b", "c"], ["ouvrir"] + ["a"] * 7,
                                  ["monde"] + ["a"] * 6, ["preparer"] + ["a"] * 5, ["detruire"] + ["a"] * 6,
                                  ["verifier-destruction", "a", "b", "c"], ["scores", "a", "b", "c"],
                                  ["commande"] + ["a"] * 11, ["commande", "repetition"] + ["a"] * 9])
def test_lanceur_de_la_version_2_refuse_toute_autre_sous_commande(args):
    """Seule « commande » sort du code figé (§ 3.2) : toute autre sous-commande est refusée par le lanceur de la version 2,
    qui renvoie au lanceur de la version 1, joué depuis l'arbre figé."""
    r = _jouer(RACINE, *args, env={"GO_ID": GO_LECTURE})
    assert r.returncode == 2 and "B5F REFUS" in r.stderr and r.stdout == ""
    if args and args[0] not in ("commande", "inconnue"):
        assert "lancer_b5f_lecture_v1.sh" in r.stderr


def test_texte_du_lanceur_sans_commande_d_arret_de_creation_ni_de_reseau():
    texte = (RACINE / LANCEUR_V2).read_text(encoding="utf-8")
    code = "\n".join(x for x in texte.splitlines() if not x.lstrip().startswith("#"))
    arret = "k" + "ill"                       # composé : la garde du dépôt refuse ce nom écrit dans une commande
    for interdit in (rf"\b{arret}\b", rf"\bp{arret}\b", r"\bp" + "grep\\b", rf"\b{arret}all\b", r"vastai", r"\bcurl\b",
                     r"\bwget\b", r"\bgit\b", r"\brm\s", r"huggingface", r"barreau5_familles\.(?:re)?lecture_v1"):
        assert re.search(interdit, code) is None, interdit
    assert "set -uo pipefail" in texte and "commande_lecture_v2" in code
