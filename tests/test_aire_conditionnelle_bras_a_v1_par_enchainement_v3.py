"""Essais du programme de l'aire conditionnelle, bras A, version 1
(`src/controle_ia/organismes_discrets/aire_conditionnelle_bras_a_v1.py`), lancé à part par l'enchaînement de la
lecture de la discrétion, version 2, et de la garde statique version 14 qui l'admet.

**De bout en bout** : l'enchaînement version 2 joue l'étape (m) réelle puis lance **le vrai programme** (non un
programme de remplacement) sur une livraison fabriquée par l'aide des essais (`aide_bras_a_v13`, celle des essais de
l'enchaînement version 2 : sortie fabriquée de la lecture commune, configuration et constat de l'aide) et sur un
fichier des rangs par unité fabriqué ici. **Entropie fictive, déclarée telle** (`ENTROPIE_FICTIVE`) ; tâches, plis et
comptes d'actions désappariées inventés. Les sorties synthétiques de l'épreuve de forme v11 ne sont pas employées :
elles sont rangées sous un chemin que cette relance n'ouvre pas, et leur fichier des rangs n'est pas connu.

Chaque garde est éprouvée sur un cas sain et sur un artefact (R5). Toute mutation se fait sur une copie, dans un
dossier temporaire ; aucun fichier du dépôt n'est changé. Le distant est un dépôt nu local : aucun réseau."""
from __future__ import annotations

import datetime
import hashlib
import itertools
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest

import aide_bras_a_v13 as h
from controle_ia.organismes_discrets import analyse_bras_a_v13 as an
from controle_ia.organismes_discrets import cloisonnement_bras_a_v14 as cl14
from controle_ia.organismes_discrets import configuration_bras_a_v12 as cf
from controle_ia.organismes_discrets import enchainement_discretion_bras_a_v3 as e
from controle_ia.organismes_discrets import graines_bras_a_v12 as g
from controle_ia.scellement import sceller, verifier

RACINE = Path(__file__).resolve().parents[1]
PAQUET = RACINE / "src" / "controle_ia" / "organismes_discrets"
PROGRAMME = PAQUET / "aire_conditionnelle_bras_a_v1.py"
CONSTAT = RACINE / "scripts" / "constat_de_lancement_discretion_bras_a_v5.py"
ENTROPIE_FICTIVE = 20261122                      # FICTIVE, déclarée telle : aucune configuration du bras ne la porte
VER = [f"tache-ver-{i:02d}" for i in range(16)]
PLI = {t: i % 2 for i, t in enumerate(VER)}
FORMES = ("dose-0.25", "dose-0.50", "dose-0.75", "dose-1.00")
# trois couples (moniteur, dose) portent des unités ; les dix-sept autres aires sont « non calculable »
COUPLES = (("classifieur-lexical", "dose-1.00", 7), (an.AGREGATEUR, "dose-0.25", 8), ("juge", "dose-0.50", 9))


def empreinte(chemin) -> str:
    return hashlib.sha256(Path(chemin).read_bytes()).hexdigest()


@pytest.fixture(autouse=True)
def git_fige(monkeypatch):
    for k in ("GIT_AUTHOR_DATE", "GIT_COMMITTER_DATE"):
        monkeypatch.setenv(k, "2099-01-02T00:00:00+00:00")
    for k, x in (("GIT_AUTHOR_NAME", "essai"), ("GIT_COMMITTER_NAME", "essai"), ("GIT_AUTHOR_EMAIL", "essai@exemple.invalid"),
                 ("GIT_COMMITTER_EMAIL", "essai@exemple.invalid")):
        monkeypatch.setenv(k, x)
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", "/dev/null")
    monkeypatch.setenv("GIT_CONFIG_NOSYSTEM", "1")


def git(dossier, *args):
    return subprocess.run(["git", "-C", str(dossier), *args], check=True, capture_output=True, text=True).stdout


# --- fichier des rangs fabriqué ------------------------------------------------------------------------------------------

def lignes_de_rangs(moniteur, dose, graine):
    """Unités fabriquées d'un moniteur à une dose (une action par épisode ; l'agrégateur, sans pas), scores tirés puis
    remplacés par leur rang moyen dans le pli (par moniteur, dose et pli), comptés un à un : la forme livrée."""
    alea = np.random.default_rng(np.random.SeedSequence(graine))
    lignes = []
    for t in VER:
        for k in range(8):
            for etiquette, condition in ((0, "honnete"), (1, dose)):
                lignes.append({"moniteur": moniteur, "dose": dose, "cle": f"{condition}/{t}/e{k}", "condition": condition,
                               "tache": t, "episode": k, "pas": None if moniteur == an.AGREGATEUR else 0, "pli": PLI[t],
                               "etiquette": etiquette, "score": float(np.round(alea.normal(0.6 * etiquette * k / 7, 1.0), 1))})
    for pli in (0, 1):
        groupe = [x for x in lignes if x["pli"] == pli]
        valeurs = [x["score"] for x in groupe]
        for x in groupe:
            x["rang"] = sum(y < x["score"] for y in valeurs) + (sum(y == x["score"] for y in valeurs) + 1) / 2
    return [{c: x[c] for c in an.CHAMPS_DU_FICHIER_DES_RANGS} for x in lignes]


def ecrire_le_fichier(dossier: Path, lignes) -> Path:
    chemin = h.nouveau_dossier(dossier, "unites") / an.NOM_DU_FICHIER_DES_RANGS
    chemin.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lignes), encoding="utf-8")
    sceller(chemin)
    return chemin


def desappariees():
    return {d: [[t, k, 2 if k >= 4 else 1] for t in VER for k in range(8)] for d in FORMES}


# --- le monde de l'essai -------------------------------------------------------------------------------------------------

class Monde:
    """Dépôt de travail et distant nu, course neuve (configuration et constat de l'aide des essais), dépôt de code
    propre pour la garde statique de l'enchaînement, pièces hors du dossier de course."""

    def __init__(self, tmp: Path, lignes=None):
        self.tmp = tmp
        self.distant = tmp / "distant.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "principale", str(self.distant)], check=True)
        self.travail = tmp / "travail"
        subprocess.run(["git", "init", "-q", "-b", "principale", str(self.travail)], check=True)
        (self.travail / "LISEZ-MOI").write_text("dépôt de l'essai\n", encoding="utf-8")
        git(self.travail, "add", "-A")
        git(self.travail, "commit", "-q", "-m", "premier")
        self.course = self.travail / "course"
        (self.course / "arrets").mkdir(parents=True)
        self.pieces = tmp / "pieces"
        self.pieces.mkdir()
        self.code = tmp / "code"
        for d in ("src", "scripts"):
            (self.code / d).mkdir(parents=True)
            (self.code / d / "propre.py").write_text("x = 1\n", encoding="utf-8")
        self.configuration = h.fichier_de_configuration(tmp, course=self.course)
        self.registre = h.registre(h.nouveau_dossier(self.pieces, "registre"), [h.ligne_d_inscription(self.configuration)])
        lignes = [x for m, d, s in COUPLES for x in lignes_de_rangs(m, d, s)] if lignes is None else lignes
        self.fichier = ecrire_le_fichier(self.pieces, lignes)
        decl = {"fichier": self.fichier.name, "sha256": empreinte(self.fichier), "lignes": len(lignes),
                "champs": list(an.CHAMPS_DU_FICHIER_DES_RANGS), "forme": "rang moyen dans le pli"}
        self.sortie = h.piece(self.pieces, h.sortie(scores_par_unite=decl))
        self.horloge = (lambda c: lambda: datetime.datetime(2099, 1, 2, tzinfo=datetime.timezone.utc)
                        + datetime.timedelta(seconds=next(c)))(itertools.count())

    def entree(self, programme=(PROGRAMME, None)) -> Path:
        chemin, sha = programme
        o = {"journal_de_la_table_a": [], "revision_refusee": False, "taches_gardees_lues": False,
             "renvoi_de_la_base": "vérifié", "effectifs_de_la_base_conformes": True,
             "lignes_de_la_table_b": {"dose-0.50": "B8", "dose-0.75": "B8", "dose-1.00": "B8"},
             "etats_de_la_base": {d: "ne detecte pas" for d in FORMES},
             "cout_apparie": {"dose-0.50": True, "dose-0.75": True, "dose-1.00": True},
             "actions_desappariees": desappariees(), "taches_de_verification": list(VER),
             "entropie_de_la_configuration_du_bras": ENTROPIE_FICTIVE,
             e.CLE_DU_PROGRAMME_DE_L_AIRE: {"chemin": str(chemin), "sha256": sha or empreinte(chemin)},
             e.CLE_DU_FICHIER: str(self.fichier)}
        return h.ecrire_scelle(h.nouveau_dossier(self.pieces, "entree") / "entree-de-l-enchainement.json", o)

    def jouer(self, entree=None):
        return e.enchainer(
            configuration_scellee=self.configuration, sortie_de_la_lecture_commune=self.sortie,
            registre_courant=self.registre, commit_du_registre_courant="0123abc", registre_fige=None, ligne_de_go=None,
            entree=entree or self.entree(), sortie_d_origine=None, programme_du_constat=CONSTAT,
            distant=str(self.distant), branche="course-discretion", horloge=self.horloge, racine_du_code=self.code)


def ligne_relevee(monkeypatch) -> list[str]:
    """La sortie standard du programme lancé, relevée au passage dans l'enchaînement (sans rien changer à sa lecture)."""
    lignes, vraie = [], e.aires_rendues

    def relever(texte):
        lignes.append(texte)
        return vraie(texte)
    monkeypatch.setattr(e, "aires_rendues", relever)
    return lignes


# --- de bout en bout -----------------------------------------------------------------------------------------------------

def test_de_bout_en_bout_le_vrai_programme_lance_par_l_enchainement_v2(tmp_path, monkeypatch):
    """Cas sain : constat, étape (m) réelle, versement ; étape (n) par le vrai programme, lancé à part depuis une copie
    de ses octets vérifiés ; code 0, une seule ligne JSON `{"aires", "cles"}` aux vingt aires et vingt clés ; ses aires
    confrontées par l'enchaînement au fichier scellé des grandeurs que l'analyse a écrit ; versement."""
    lignes = ligne_relevee(monkeypatch)
    m = Monde(tmp_path)
    cr = m.jouer()
    assert cr["issue"] == e.ISSUE_ABOUTIE and cr["etapes_jouees"] == ["m", "n"]
    assert [v["etape"] for v in cr["versements"]] == ["ouverture de l'enchaînement", "constat de lancement", "étape (m)",
                                                      "étape (n)"]
    p = cr["programme_de_l_aire_conditionnelle"]
    assert p["code"] == 0 and p["aires_rendues"] == 20 and p["sha256"] == empreinte(PROGRAMME)
    assert p["commande"][1] == str(PROGRAMME)
    assert len(lignes) == 1 and lignes[0].endswith("\n") and lignes[0].count("\n") == 1
    o = json.loads(lignes[0])
    assert sorted(o) == ["aires", "cles"] and sorted(o["aires"]) == list(FORMES)
    assert all(sorted(x) == sorted(an.MONITEURS) for x in o["aires"].values())
    assert sorted(o["cles"]) == sorted(g.cles_de_l_aire_conditionnelle())
    calculees = {(mo, d) for d, x in o["aires"].items() for mo, a in x.items() if a["etat"] == an.CALCULEE}
    assert calculees == {(mo, d) for mo, d, _ in COUPLES}             # les trois couples fabriqués, et eux seuls
    grandeurs = json.loads((m.configuration.parent / an.NOM_DU_FICHIER_DES_GRANDEURS_DE_L_ETAPE_N).read_text(encoding="utf-8"))
    verifier(m.configuration.parent / an.NOM_DU_FICHIER_DES_GRANDEURS_DE_L_ETAPE_N)
    assert grandeurs["grandeurs"]["aire_conditionnelle"] == o["aires"]
    assert grandeurs["grandeurs"]["cles_des_tirages"] == sorted(o["cles"])
    assert grandeurs["sha256_du_fichier_des_scores"] == empreinte(m.fichier)
    texte = json.dumps(cr, ensure_ascii=False)
    assert "aires_des_plis" not in texte and '"intervalle"' not in texte      # le compte rendu ne porte aucune aire


def test_arret_de_l_analyse_rendu_par_le_code_3(tmp_path, monkeypatch):
    """Artefact : un fichier des rangs dont une ligne porte un moniteur hors des cinq — la lecture du fichier consigne
    l'arrêt à l'étape (n) ; le programme sort sur le code 3, sortie standard vide ; l'enchaînement relève l'arrêt
    consigné, le verse, et le rend de son seul constat. Cas sain : l'essai de bout en bout."""
    lignes = ligne_relevee(monkeypatch)
    fautives = lignes_de_rangs("juge", "dose-0.50", 9)
    fautives[3] = {**fautives[3], "moniteur": "moniteur-invente"}
    m = Monde(tmp_path, lignes=fautives)
    with pytest.raises(e.ArretDeLEnchainement) as x:
        m.jouer()
    cr = x.value.compte_rendu
    assert x.value.issue == e.ISSUE_ARRET and cr["constat_de_l_arret"]["etape"] == "n"
    assert lignes == [] and cr["etapes_jouees"] == ["m"]
    assert not (m.configuration.parent / an.NOM_DU_FICHIER_DES_GRANDEURS_DE_L_ETAPE_N).exists()


def test_programme_d_une_autre_empreinte_refuse_par_l_enchainement(tmp_path):
    """Artefact : une copie du programme, retouchée d'une ligne, inscrite à l'empreinte du vrai — l'enchaînement ne
    la lance pas (garde ordinaire, versée, avant tout constat). Cas sain : l'essai de bout en bout."""
    m = Monde(tmp_path)
    copie = h.nouveau_dossier(tmp_path, "programme") / PROGRAMME.name
    copie.write_text(PROGRAMME.read_text(encoding="utf-8") + "# retouché\n", encoding="utf-8")
    with pytest.raises(e.ArretDeLEnchainement) as x:
        m.jouer(entree=m.entree(programme=(copie, empreinte(PROGRAMME))))
    cr = x.value.compte_rendu
    assert x.value.issue == e.ISSUE_GARDE and "programme de l'aire conditionnelle" in cr["motif_de_l_arret"]
    assert cr["constats"] == [] and "programme_de_l_aire_conditionnelle" not in cr["programmes"]


# --- le programme seul : empreinte de l'analyse, gardes, codes -------------------------------------------------------------

def lancer(tmp: Path, pythonpath: Path, entree: str = "{}", arguments=None):
    """Lance une copie du programme comme l'enchaînement le fait (copie dans un dossier temporaire, `PYTHONPATH`
    donné, dossier de travail à la racine du code)."""
    copie = h.nouveau_dossier(tmp, "copie") / PROGRAMME.name
    shutil.copyfile(PROGRAMME, copie)
    arguments = arguments or ["--configuration", str(tmp / "absente.json"), "--sortie", str(tmp / "absente-s.json"),
                              "--fichier-des-unites", str(tmp / "absent.jsonl")]
    return subprocess.run([sys.executable, str(copie), *arguments], input=entree, capture_output=True, text=True,
                          timeout=600, cwd=str(RACINE),
                          env={"PYTHONPATH": str(pythonpath), "PATH": "/usr/bin:/bin", "LC_ALL": "C.UTF-8"})


def arbre_copie(tmp: Path, analyse_en_plus: str | None) -> Path:
    """Copie, fichier par fichier (liste blanche), des deux `__init__.py` du paquet et de l'analyse, retouchée de
    `analyse_en_plus` (ou absente si `None`). Rend le dossier à mettre en `PYTHONPATH`."""
    src = h.nouveau_dossier(tmp, "src")
    (src / "controle_ia" / "organismes_discrets").mkdir(parents=True)
    shutil.copyfile(RACINE / "src" / "controle_ia" / "__init__.py", src / "controle_ia" / "__init__.py")
    shutil.copyfile(PAQUET / "__init__.py", src / "controle_ia" / "organismes_discrets" / "__init__.py")
    if analyse_en_plus is not None:
        cible = src / "controle_ia" / "organismes_discrets" / "analyse_bras_a_v13.py"
        cible.write_text((PAQUET / "analyse_bras_a_v13.py").read_text(encoding="utf-8") + analyse_en_plus, encoding="utf-8")
    return src


def test_analyse_a_l_empreinte_alteree_ou_absente_code_4_sans_import(tmp_path):
    """Garde de l'empreinte de l'analyse. Artefacts : une copie de l'analyse retouchée d'une ligne (qui, importée,
    poserait une marque) ; l'analyse absente du chemin. Code 4, sortie standard vide, une seule ligne d'erreur ; la
    marque n'existe pas : l'analyse n'a pas été importée. Cas sain : l'analyse du dépôt — l'empreinte passe, l'analyse
    est importée, sa propre garde arrête sur des pièces absentes (code 4, ligne de l'analyse)."""
    marque = tmp_path / "marque-de-l-import"
    for src, attendu in ((arbre_copie(tmp_path, f"\nopen({str(marque)!r}, 'w').close()\n"), "empreinte"),
                         (arbre_copie(tmp_path, None), "introuvable")):
        fait = lancer(tmp_path, src)
        assert fait.returncode == 4 and fait.stdout == "" and fait.stderr.count("\n") == 1 and attendu in fait.stderr
        assert not marque.exists()
    assert empreinte(PAQUET / "analyse_bras_a_v13.py") == "a7ebf29f653d417a4f211f9809576a0e70b91ae7840759607c6f3cb7f84946cf"
    entree = json.dumps({"actions_desappariees": desappariees(), "taches_de_verification": VER,
                         "entropie_de_la_configuration_du_bras": ENTROPIE_FICTIVE, "autres_grandeurs": {}})
    fait = lancer(tmp_path, RACINE / "src", entree)
    assert fait.returncode == 4 and fait.stdout == "" and fait.stderr.count("\n") == 1
    assert "garde ordinaire de l'analyse" in fait.stderr and "lecture du fichier" in fait.stderr


@pytest.mark.parametrize("entree", ["pas du json", "[]", json.dumps({"actions_desappariees": {}}),
                                    json.dumps({"actions_desappariees": {"dose-0.25": [["t", 0, 1], ["t", 0, 2]]},
                                                "taches_de_verification": VER, "entropie_de_la_configuration_du_bras": 1,
                                                "autres_grandeurs": {}}),
                                    '{"actions_desappariees": {}, "actions_desappariees": {}}',
                                    json.dumps({"actions_desappariees": {"dose-0.25": [["t", 0]]}, "taches_de_verification": VER,
                                                "entropie_de_la_configuration_du_bras": 1, "autres_grandeurs": {}})])
def test_entree_standard_hors_de_sa_forme_code_4(tmp_path, entree):
    """Artefacts : entrée standard illisible, d'une autre forme, à clé en double, un épisode écrit deux fois, un
    triplet tronqué — code 4 avant toute lecture de pièce, une ligne. Cas sain : l'essai de bout en bout."""
    fait = lancer(tmp_path, RACINE / "src", entree)
    assert fait.returncode == 4 and fait.stdout == "" and fait.stderr.count("\n") == 1 and "entrée standard" in fait.stderr


# --- la garde statique version 14 --------------------------------------------------------------------------------------

def test_garde_statique_v14_admet_le_programme_et_rend_rien_sur_le_depot():
    """La garde version 14 admet le programme par son chemin exact (et le sien), scellés ; sur `src/` et `scripts/` du
    dépôt, elle ne rend aucune violation. Artefact : le même texte, hors de la liste, est refusé (nom réservé)."""
    rel = "src/controle_ia/organismes_discrets/aire_conditionnelle_bras_a_v1.py"
    assert rel in cl14.PROGRAMMES_DE_L_AIRE_CONDITIONNELLE and rel in cl14.AUTORISES_POUR_LES_RANGS
    verifier(PROGRAMME)
    verifier(PAQUET / "cloisonnement_bras_a_v14.py")
    assert cl14.violations_d_un_programme(PROGRAMME.read_text(encoding="utf-8"), "copie hors de la liste") != []
    assert cl14.violations_de_la_garde_statique(RACINE) == []
