"""Essais du module `arene_regles_defense_v3.py` (R5 : chaque garde sur un cas sain et sur un artefact).

Les 25 essais de la v2 (`test_arene_regles_defense_v2.py`, empreinte
78d979ab76bbe4b3ad6b55be77bf2b745a4457940eb9cb4c16a3ee87ef324b81) sont repris et adaptés à la v3 (version, chemin du
gel et de l'arène, motifs des racines de la course originale, identité) ; s'y ajoutent les essais de la v3
(préenregistrement de réplication, § Plan 2) :
- E1 règle D : les trois vecteurs d'essai de la spécification ; gardes sur cas sain et artefacts (racines égales,
  racine dans l'ensemble interdit, racine égale à un vecteur d'essai, empreinte mal formée) ;
- E2 racines de la course originale (20266201, 20266202) refusées, sauf autorisation posée par l'essai E6 lui-même ;
- E3 identité v3 (sain ; artefacts : identifiant v2, ligne de la règle D absente, empreinte du code v2 absente…) ;
- E4 décision refusée sans texte scellé (non scellé, scellé puis modifié, compagnon d'un autre texte, second texte) ;
  texte scellé : racines = règle D de son empreinte ; C8 (processus de travail) et C9 (manifeste, course, analyse) ;
- E5 diff restreint v2 → v3 par l'arbre syntaxique : chaque fonction, classe et instruction de niveau module est
  identique (arbre et texte source), sauf celles des changements C1 à C12 (liste fermée `CHANGEMENTS_C1_C12`) ;
- E6 (lent) non-régression au bit : v3 rejoue les tâches (δ 1,4 ; instances 0 et 1) de la course originale sur ses
  racines d'origine et rend, pour les cinq variantes, tous les champs déterministes de `resultats-regles-defense.json`
  (d07ece47…) ; E6 bis (rapide) : l'analyse v3 des 200 tâches originales rend `analyse-regles-defense.json`
  (18b80112…) au bit ;
- E7 la sérialisation ne change aucune valeur (une tâche, petite configuration, avec et sans) et restitue fidèlement
  défenses finales et attaques (V standard, V renforcé et fausses alertes recalculés au bit) ;
- arène chargée depuis la copie suivie par git, refus sinon.

Lancement (depuis n'importe quel dossier) :
    PYTHONPATH=<dépôt>/src OMP_NUM_THREADS=1 python -B -m pytest -q -p no:cacheprovider <ce fichier>
Essais lents (E6 et la parité de T de la v2 ; ≈ 40 s de processeur, ≈ 1 à 2 min de mur sur 2 cœurs chargés) :
variable d'environnement REGLES_ESSAIS_LENTS=1.
Racines : celles des essais du gel v2 (20266511 à 20266513) ; seuls E2, E6 et E6 bis posent eux-mêmes l'autorisation
des racines de la course originale (20266201, 20266202), sur des résultats déjà scellés et lus. Les textes de
préenregistrement des essais E4, C8 et C9 sont synthétiques, scellés dans le dossier temporaire de pytest ; ce ne sont
jamais le texte de réplication ni un de ses brouillons ; aucun tirage n'est fait sur leurs racines (tâches remplacées
par un témoin) ; E1 dérive des racines d'une chaîne fixe, sans tirage.
Aucun fichier écrit hors du dossier temporaire de pytest.
"""
from __future__ import annotations

import ast
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pytest

ICI = Path(__file__).resolve().parent
if str(ICI) not in sys.path:
    sys.path.insert(0, str(ICI))

import arene_regles_defense_v3 as m  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.prereg import SECTIONS, problemes  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

v4 = m.v4
DEPOT = m.DEPOT
# petite configuration (T = 3) : calibration et fausses alertes du v4 gardées (la garde de fausses alertes exige le
# quantile sur 20 000 points propres), tout le reste réduit
CFG_PETITE = m.replace(v4.CONFIG_V4, T=3, n_eval=999, n_mc=32, n_mc_final=64, departs=1, departs_final=2,
                       departs_renforce=2, iter_renforce=20, n_tenue=4, n_eval_tenue=999, n_propre_entr=300,
                       n_attaque_entr=300, departs_entr=2, iter_entr=50, iter_max=20)
R, RT, RA = m.RACINE_TESTS, m.RACINE_TESTS_TENUE, m.RACINE_TESTS_AUTRE
LENT = pytest.mark.skipif(os.environ.get("REGLES_ESSAIS_LENTS") != "1",
                          reason="essai lent (configuration complète) : REGLES_ESSAIS_LENTS=1 pour le lancer")

# pièces de la course originale (rapatriées de n67, scellées ; empreintes du préenregistrement de réplication)
COURSE_ORIGINALE = DEPOT / "diag" / "20261101-160323-regles-defense-convergence"
RESULTATS_ORIGINAUX = COURSE_ORIGINALE / "resultats-regles-defense.json"
RESULTATS_ORIGINAUX_SHA256 = "d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b"
ANALYSE_ORIGINALE = COURSE_ORIGINALE / "analyse-regles-defense.json"
ANALYSE_ORIGINALE_SHA256 = "18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42"
PREREG_ORIGINAL = DEPOT / "prereg" / "preregistrement-regles-defense-convergence-v1.md"
PREREG_ORIGINAL_SHA256 = "d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d"
RACINES_ORIGINALES = (20266201, 20266202)
VECTEURS_SPECIFICATION = {     # spécification statistique § 4 (recopiés ici, indépendamment du code)
    "d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d": (11786724493248295725, 9136419304016434890),
    "0" * 64: (15793235383387715774, 12390638538380655177),
    "f" * 64: (10168828190493638947, 4616211851522120706),
}
# champs de temps processeur (non déterministes) et champs propres à la v3, exclus des comparaisons au bit
CHAMPS_TEMPS = frozenset({"cpu_tache_s", "cpu_trajectoire_s", "cpu_final_s", "cpu_s"})
CHAMPS_V3 = frozenset({"serialisation", "loi_cible"})


def contexte_et_M0(racine=R, racine_tenue=RT, instance=0, cd=1, cfg=CFG_PETITE):
    ctx = v4.Contexte(instance, cd, racine, racine_tenue, cfg)
    M0 = ctx.entrainer(v4.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    return ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, cfg.alpha)


def sans_temps(x, retirer=frozenset()):
    """Copie d'une sortie de tâche sans les temps processeur, sans `version` et sans les clés `retirer`."""
    if isinstance(x, dict):
        return {k: sans_temps(v, retirer) for k, v in x.items()
                if k not in CHAMPS_TEMPS and k not in retirer and k != "version"}
    if isinstance(x, list):
        return [sans_temps(v, retirer) for v in x]
    return x


def au_bit(x) -> str:
    """Écriture JSON canonique (flottants au plus court qui se relit à l'identique : égalité de chaîne = égalité au
    bit, NaN compris)."""
    return json.dumps(json.loads(json.dumps(x)), sort_keys=True, ensure_ascii=False)


def texte_prereg_synthetique(cfg=None) -> str:
    """Préenregistrement SYNTHÉTIQUE d'essai, conforme au validateur et à l'identité v3 ; jamais lancé, sans lien avec
    le texte de réplication."""
    cfg = v4.CONFIG_V4 if cfg is None else cfg
    corps = [f"## {s}\n\nTexte synthétique d'essai du code v3 (jamais lancé ; ce n'est pas le texte de réplication)."
             for s in SECTIONS if s != "Contre-lecture"]
    return "\n\n".join(["# Préenregistrement synthétique d'essai du code v3", m.bloc_identite(cfg),
                        "LAMBDA_RETENU = 0.3", "REFERENCE_RETENUE = moyenne", *corps,
                        "## Contre-lecture\n\nContre-lecteur d'essai ; brouillon relu " + "1" * 64 + " ; rapport "
                        + "2" * 64]) + "\n"


def prereg_scelle(dossier: Path, texte: str | None = None, nom: str = "prereg-synthetique.md") -> Path:
    p = dossier / nom
    p.write_text(texte_prereg_synthetique() if texte is None else texte, encoding="utf-8")
    sceller(p)                       # compagnon écrit dans le dossier temporaire de pytest
    return p


def problemes_texte(dossier: Path, texte: str) -> list[str]:
    """Problèmes relevés par le validateur du dépôt sur un texte (écrit dans le dossier temporaire, non scellé)."""
    p = dossier / "validateur.md"
    p.write_text(texte, encoding="utf-8")
    return problemes(p)


@pytest.fixture
def sans_autorisation(monkeypatch):
    """Processus « neuf » : aucune autorisation posée pendant l'essai ; état restauré après."""
    monkeypatch.setitem(m._AUTORISATION_DECISION, "prereg_sha256", None)
    monkeypatch.setitem(m._AUTORISATION_DECISION, "racines", None)
    return monkeypatch


@pytest.fixture(scope="module")
def tache_petite():
    """Une tâche (δ 1, instance 0), toutes les règles (R0 comprise), R4 à λ ∈ {0 ; 0,3} et les deux références."""
    t0 = time.process_time()
    r = m.executer_tache_regles(0, 1, R, RT, CFG_PETITE, lambdas=(0.0, 0.3), references=("dernier", "moyenne"))
    return r, time.process_time() - t0


# ---------------------------------------------------------------------------------------------------------------
# Chargement du v4 (copie suivie), gel, racines (gardes : sain et artefact)
# ---------------------------------------------------------------------------------------------------------------
def test_chargement_v4_copie_suivie_empreinte_sain_et_artefacts(tmp_path):
    """C3 : l'arène est chargée depuis la copie suivie par git, à l'empreinte épinglée ; refus sinon."""
    assert m.empreinte_fichier(m.ARENE_V4) == m.ARENE_V4_SHA256 == "70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61"
    rel = m.ARENE_V4.relative_to(DEPOT)
    assert rel.parts[0] == "brouillons" and "donnees" not in rel.parts                   # sain : copie hors de donnees/
    suivi = subprocess.run(["git", "-C", str(DEPOT), "ls-files", "--error-unmatch", "--", str(rel)],
                           capture_output=True, text=True)
    assert suivi.returncode == 0, suivi.stderr                                           # suivie par git (index lu)
    assert Path(v4.__file__) == m.ARENE_V4                                               # le module chargé est elle
    assert v4.VERSION == "arene_melange_v4" and m.VERSION == "arene_regles_defense_v3"
    copie = tmp_path / "arene_melange_v4.py"
    shutil.copy(m.ARENE_V4, copie)
    copie.write_bytes(copie.read_bytes().replace(b"DELTAS_V4 = (1.4, 1.6)", b"DELTAS_V4 = (1.4, 1.8)"))
    with pytest.raises(GardeArret, match="arène v4 modifiée"):
        m.charger_arene_v4(copie)
    copie.write_bytes(m.ARENE_V4.read_bytes() + b"\n")                                  # un seul octet ajouté
    with pytest.raises(GardeArret, match="arène v4 modifiée"):
        m.charger_arene_v4(copie)
    with pytest.raises(GardeArret, match="arène v4 absente"):
        m.charger_arene_v4(tmp_path / "absente.py")
    with pytest.raises(GardeArret, match="arène v4 modifiée"):                          # empreinte épinglée autre
        m.charger_arene_v4(m.ARENE_V4, "0" * 64)
    # la copie chargée est bien celle qui porte le remplacement de `gen` et l'extension de BRAS (R0 = 20 compris)
    assert v4.gen is m.gen_regles and v4.BRAS["R0"] == 20 and v4.BRAS["R1"] == 21 and v4.BRAS["R2"] == v4.BRAS["A"]
    assert m.CODES["R0"] not in {1, 2, 4, 5, 6, 7, 8, 9, 21, 24}                     # code de graine neuf, libre
    # les fonctions de l'arène employées ici ne lisent ni son dossier ni son dépôt (C3) : aucune référence à
    # `ICI`, `DEPOT`, `GEL_V4` ou `__file__` dans leur code
    employees = ("Contexte", "phase_finale", "meilleure_reponse", "taux_defense", "resoudre_jeu", "entrainer",
                 "objectif_detection", "_logistique", "echantillonner", "lois_tenues", "loi_cible", "indicateurs_cycle",
                 "poids_max_min_equilibres", "_q", "exiger_config", "extraire_configuration", "comparer_configuration",
                 "_consigner_pids", "arreter_par_pid", "exiger_aucun_orphelin", "lire_pids", "_exiger_absent",
                 "_ecrire_nouveau", "trajectoire")
    arbre = ast.parse(m.ARENE_V4.read_text(encoding="utf-8"))
    defs = {n.name: n for n in arbre.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
    for nom in employees:
        noms = {x.id for x in ast.walk(defs[nom]) if isinstance(x, ast.Name)}
        assert not noms & {"ICI", "DEPOT", "GEL_V4", "__file__"}, nom


def test_gel_v2_sain_et_artefacts(tmp_path):
    assert m.GEL.name == "gel-regles-defense-v2.md" and m.GEL.parent == m.DOSSIER_V2 == m.CODE_V2.parent
    assert m.exiger_gel_regles((R, RT, RA, m.RACINE_ESSAI, m.RACINE_ESSAI_TENUE, m.RACINE_DECISION,
                                m.RACINE_DECISION_TENUE, m.RACINE_SIMULATION)) == m.GEL_SHA256     # sain
    assert m.exiger_gel_regles(()) == m.GEL_SHA256                    # C9 : empreinte seule, sans racine citée
    with pytest.raises(GardeArret, match="absente du gel"):
        m.exiger_gel_regles((20266555,))     # (20266999 est cité par le gel comme borne de la plage)
    copie = tmp_path / "gel.md"
    copie.write_text(m.GEL.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="gel des règles modifié"):
        m.exiger_gel_regles((), copie)
    with pytest.raises(GardeArret, match="gel des règles absent"):
        m.exiger_gel_regles((), tmp_path / "rien.md")
    # le gel v1, intact, n'est pas le gel de la v2
    with pytest.raises(GardeArret, match="gel des règles modifié"):
        m.exiger_gel_regles((), m.DOSSIER_V2 / "gel-regles-defense-v1.md")


def test_racines_sain_et_artefacts(sans_autorisation):
    g1, g2 = m.gen_regles(R, 1, 0, 20, 3, 5), m.gen_regles(R, 1, 0, 20, 3, 5)
    assert np.array_equal(g1.standard_normal(4), g2.standard_normal(4))                       # sain, reproductible
    assert not np.array_equal(m.gen_regles(R, 1, 0, 20, 3, 5).standard_normal(4),
                              m.gen_regles(R, 1, 0, 21, 3, 5).standard_normal(4))             # le code de règle compte
    m.exiger_racines_essai_regles(R, RT)
    for racine, motif in ((m.RACINE_DECISION, "course originale"), (v4.RACINE, "de décision de l'arène v4"),
                          (20261291, "déjà employée"), (20265100, "d'une autre session"),
                          (v4.RACINE_ESSAI, "réservée au v4"), (20266999, "non gelée"),
                          (20266101, "employée par la v1"), (20266301, "employée par la v1"),
                          (20266303, "employée par la v1"), (11786724493248295725, "non gelée")):
        with pytest.raises(GardeArret, match=motif):
            m.gen_regles(racine, 0)
    with pytest.raises(GardeArret, match="réservée à la décision"):
        m.exiger_racines_essai_regles(m.RACINE_DECISION, RT)
    with pytest.raises(GardeArret, match="racine à part"):
        m.exiger_racines_essai_regles(R, R)
    with pytest.raises(GardeArret, match="racine absente"):
        m.exiger_racines_essai_regles(None, RT)
    assert all(m.PLAGE_REGLES[0] <= r <= m.PLAGE_REGLES[1] for r in m.RACINES_GELEES + m.RACINES_DECISION)
    assert not set(m.RACINES_GELEES) & set(m.RACINES_EMPLOYEES_V1)                            # v2 ≠ v1
    assert set(m.RACINES_GELEES) & set(range(20266201, 20266300)) == set()                   # hors de la décision
    texte = m.GEL.read_text(encoding="utf-8")
    assert all(str(r) in texte for r in m.RACINES_GELEES + m.RACINES_DECISION + m.RACINES_EMPLOYEES_V1)   # toutes gelées


def test_decision_refusee_sans_prereg_scelle(tmp_path, sans_autorisation):
    brouillon = tmp_path / "prereg.md"
    brouillon.write_text("# brouillon non scellé\n", encoding="utf-8")
    with pytest.raises(GardeArret):
        m.autoriser_decision_regles(brouillon, v4.CONFIG_V4, "0:100", 0.3, "moyenne")
    assert m._AUTORISATION_DECISION == {"prereg_sha256": None, "racines": None}
    with pytest.raises(GardeArret, match="course originale"):
        m.gen_regles(m.RACINE_DECISION_TENUE, 0)
    with pytest.raises(GardeArret):      # commande decision : refusée avant toute graine
        m.main(["decision", "--prereg", str(brouillon), "--instances", "0:100", "--run-id", "x", "--lambda", "0.3",
                "--reference", "moyenne"])
    assert m._AUTORISATION_DECISION == {"prereg_sha256": None, "racines": None}


# ---------------------------------------------------------------------------------------------------------------
# E1 à E4 : règle D, racines de la course originale, identité, texte scellé ; C8 et C9
# ---------------------------------------------------------------------------------------------------------------
def test_E1_regle_D_vecteurs_d_essai_et_gardes_sain_et_artefacts():
    # vecteurs de la spécification § 4 (calcul seul, sans les gardes) ; recopiés dans le code à l'identique
    for h, attendu in VECTEURS_SPECIFICATION.items():
        assert m.etat_regle_D(h) == attendu
    assert m.VECTEURS_ESSAI_REGLE_D == VECTEURS_SPECIFICATION
    # le calcul est bien celui de la spécification (SeedSequence d'entropie int(H, 16), sans clé, deux mots uint64)
    h = hashlib.sha256("essai E1 du code v3 : empreinte quelconque, sans lien avec un texte".encode()).hexdigest()
    w = np.random.SeedSequence(entropy=int(h, 16)).generate_state(2, dtype=np.uint64)
    assert m.etat_regle_D(h) == (int(w[0]), int(w[1]))
    # sain : racines distinctes, hors de F et des vecteurs, sur 64 bits
    r, rt = m.deriver_racines_regle_D(h)
    assert (r, rt) == m.etat_regle_D(h) and r != rt and all(0 <= x < 2 ** 64 for x in (r, rt))
    m.exiger_racines_regle_D(r, rt)
    m.exiger_racines_regle_D(20260999, 20270000)                   # juste hors de la plage interdite : permis
    # artefacts : chaque vecteur d'essai est refusé comme racine (dérivation et garde)
    for h_v, (a, b) in VECTEURS_SPECIFICATION.items():
        with pytest.raises(GardeArret, match="vecteur d'essai"):
            m.deriver_racines_regle_D(h_v)
        for x in (a, b):
            with pytest.raises(GardeArret, match="vecteur d'essai"):
                m.exiger_racines_regle_D(x, rt)
            with pytest.raises(GardeArret, match="vecteur d'essai"):
                m.exiger_racines_regle_D(r, x)
    # artefacts : racines égales
    with pytest.raises(GardeArret, match="égale à la racine des lois tenues"):
        m.exiger_racines_regle_D(r, r)
    # artefacts : ensemble interdit F (racines de la course originale, du v4, plage entière, bornes comprises)
    for x in (20261201, 20261202, 20266201, 20266202, 20261000, 20269999, 20264201, 20266511, 20265500):
        with pytest.raises(GardeArret, match="ensemble interdit"):
            m.exiger_racines_regle_D(x, rt)
        with pytest.raises(GardeArret, match="ensemble interdit"):
            m.exiger_racines_regle_D(r, x)
    # artefacts : empreinte mal formée (majuscules, longueur, caractère hors de l'hexadécimal)
    for mauvais in (h.upper(), h[:-1], h + "0", "g" * 64, ""):
        with pytest.raises(GardeArret, match="64 chiffres"):
            m.etat_regle_D(mauvais)


def test_E2_racines_de_la_course_originale_refusees_sauf_autorisation_posee_par_l_essai(tmp_path, sans_autorisation):
    for r in RACINES_ORIGINALES:
        with pytest.raises(GardeArret, match="course originale"):
            m.gen_regles(r, 0)
        with pytest.raises(GardeArret, match="course originale"):
            m.exiger_racine_permise_regles(r)
    with pytest.raises(GardeArret, match="réservée à la décision"):          # mode essai (fonction v2 inchangée)
        m.exiger_racines_essai_regles(*RACINES_ORIGINALES)
    with pytest.raises(GardeArret, match="ensemble interdit"):               # jamais dérivables par la règle D
        m.exiger_racines_regle_D(*RACINES_ORIGINALES)
    with pytest.raises(GardeArret, match="réservée à la décision"):          # commande essai
        m.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "s.json"), "--racine", "20266201",
                "--racine-tenue", "20266202"])
    assert not (tmp_path / "s.json").exists()
    # artefact : des racines posées sans texte (état incohérent) ne permettent rien
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "racines", RACINES_ORIGINALES)
    with pytest.raises(GardeArret, match="course originale"):
        m.gen_regles(RACINES_ORIGINALES[0], 0)
    # sain (cas de l'essai E6 seulement) : autorisation posée par l'essai → permises ; toute autre racine non gelée
    # reste refusée
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "prereg_sha256", PREREG_ORIGINAL_SHA256)
    for r in RACINES_ORIGINALES:
        m.exiger_racine_permise_regles(r)
    with pytest.raises(GardeArret, match="non gelée"):
        m.gen_regles(20266299, 0)
    with pytest.raises(GardeArret, match="non gelée"):
        m.gen_regles(11786724493248295725, 0)


def test_E3_bloc_identite_et_identite_prereg_sain_et_artefacts():
    cfg = v4.CONFIG_V4
    texte = m.bloc_identite(cfg) + "\nLAMBDA_RETENU = 0.3\nREFERENCE_RETENUE = moyenne\n"
    assert m.IDENTIFIANT_PREREG == "PREREG-REPLICATION-REGLES-DEFENSE-V1"
    lignes = texte.splitlines()
    assert lignes[0] == "- Identifiant : PREREG-REPLICATION-REGLES-DEFENSE-V1"
    assert lignes[1].startswith("- Racines : RACINES_REPLICATION = règle D (")
    assert lignes[2] == f"- Code : `arene_regles_defense_v3.py` — {m.empreinte_fichier(m.__file__)}"
    assert lignes[3] == ("- Code de la course originale (référence du diff) : `arene_regles_defense_v2.py` — "
                         "9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3")
    assert m.ARENE_V4_SHA256 in texte and m.GEL_SHA256 in texte and cfg.empreinte() in texte
    assert "RACINE_DECISION" not in texte and "20266201" not in texte          # aucune racine écrite dans le texte
    m.exiger_identite_prereg_regles(texte, cfg, "0:100", 0.3, "moyenne")                 # sain
    for mauvais, motif in ((texte.replace(m.IDENTIFIANT_PREREG, "PREREG-REGLES-DEFENSE-V2"), "sans l'identifiant"),
                           (texte.replace("RACINES_REPLICATION = règle D", "RACINES_REPLICATION = à choisir"),
                            "règle D"),
                           (texte.replace("RACINES_REPLICATION = règle D", "RACINE_DECISION = 20266201"), "règle D"),
                           (texte.replace(m.CODE_V2_SHA256, "0" * 64), "code v2"),
                           (texte.replace(m.empreinte_fichier(m.__file__), "0" * 64), "empreinte \\(code\\) absente"),
                           (texte.replace(m.ARENE_V4_SHA256, "0" * 64), "arène v4"),
                           (texte.replace(m.GEL_SHA256, "0" * 64), "empreinte \\(gel\\) absente"),
                           (texte.replace('"T": 8', '"T": 7'), "configuration différente"),
                           (texte.replace("numpy " + np.__version__, "numpy 0.0.0"), "version numpy")):
        with pytest.raises(GardeArret, match=motif):
            m.exiger_identite_prereg_regles(mauvais, cfg, "0:100", 0.3, "moyenne")
    with pytest.raises(GardeArret, match="LAMBDA_RETENU"):
        m.exiger_identite_prereg_regles(texte, cfg, "0:100", 1.0, "moyenne")
    with pytest.raises(GardeArret, match="REFERENCE_RETENUE"):
        m.exiger_identite_prereg_regles(texte, cfg, "0:100", 0.3, "dernier")
    with pytest.raises(GardeArret, match="--instances 0:50"):
        m.exiger_identite_prereg_regles(texte, cfg, "0:50", 0.3, "moyenne")
    # artefact réel : le préenregistrement scellé de la course originale n'est pas une identité v3
    assert m.empreinte_fichier(PREREG_ORIGINAL) == PREREG_ORIGINAL_SHA256
    with pytest.raises(GardeArret, match="sans l'identifiant"):
        m.exiger_identite_prereg_regles(PREREG_ORIGINAL.read_text(encoding="utf-8"), cfg, "0:100", 0.3, "moyenne")


def test_E4_decision_refusee_sans_texte_scelle_et_racines_par_regle_D(tmp_path, sans_autorisation):
    cfg = v4.CONFIG_V4
    texte = texte_prereg_synthetique(cfg)
    assert problemes_texte(tmp_path, texte) == []                  # le texte synthétique est conforme au validateur
    rien = {"prereg_sha256": None, "racines": None}
    # artefact 1 : texte conforme mais non scellé (aucun compagnon)
    brouillon = tmp_path / "non-scelle.md"
    brouillon.write_text(texte, encoding="utf-8")
    with pytest.raises(GardeArret, match="empreinte compagnon"):
        m.autoriser_decision_regles(brouillon, cfg, "0:100", 0.3, "moyenne")
    assert m._AUTORISATION_DECISION == rien
    with pytest.raises(GardeArret, match="empreinte compagnon"):  # commande decision : refusée avant toute graine
        m.main(["decision", "--prereg", str(brouillon), "--instances", "0:100", "--run-id", "20261101-000000-essai",
                "--lambda", "0.3", "--reference", "moyenne"])
    assert m._AUTORISATION_DECISION == rien
    # artefact 2 : scellé puis modifié (empreinte discordante)
    modifie = prereg_scelle(tmp_path, texte, "modifie.md")
    modifie.write_text(texte + "\najout après scellement\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="≠ scellée"):
        m.autoriser_decision_regles(modifie, cfg, "0:100", 0.3, "moyenne")
    # artefact 3 : compagnon recopié d'un autre texte scellé
    autre = prereg_scelle(tmp_path, texte + "\nautre texte\n", "autre.md")
    faux = tmp_path / "faux.md"
    faux.write_text(texte, encoding="utf-8")
    (tmp_path / "faux.md.sha256").write_text(Path(str(autre) + ".sha256").read_text(encoding="utf-8")
                                             .replace("autre.md", "faux.md"), encoding="utf-8")
    with pytest.raises(GardeArret, match="≠ scellée"):
        m.autoriser_decision_regles(faux, cfg, "0:100", 0.3, "moyenne")
    # artefact 4 : texte scellé mais d'identité fausse (identifiant v2)
    mauvais = prereg_scelle(tmp_path, texte.replace(m.IDENTIFIANT_PREREG, "PREREG-REGLES-DEFENSE-V2"), "v2.md")
    with pytest.raises(GardeArret, match="sans l'identifiant"):
        m.autoriser_decision_regles(mauvais, cfg, "0:100", 0.3, "moyenne")
    assert m._AUTORISATION_DECISION == rien                        # aucun refus n'a posé de racine
    # sain : texte scellé et identifié → racines = règle D de l'empreinte de ses octets, posées avec elle
    p = prereg_scelle(tmp_path, texte, "scelle.md")
    sha = m.autoriser_decision_regles(p, cfg, "0:100", 0.3, "moyenne")
    assert sha == hashlib.sha256(p.read_bytes()).hexdigest()
    rho, rho_t = m._AUTORISATION_DECISION["racines"]
    assert (rho, rho_t) == m.etat_regle_D(sha) == m.deriver_racines_regle_D(sha)
    assert not {rho, rho_t} & (set(RACINES_ORIGINALES) | set(m.RACINES_GELEES))
    m.exiger_racine_permise_regles(rho)                            # permises une fois posées (aucun tirage ici)
    m.exiger_racine_permise_regles(rho_t)
    for r in RACINES_ORIGINALES:                                   # les racines originales restent refusées
        with pytest.raises(GardeArret, match="course originale"):
            m.exiger_racine_permise_regles(r)
    assert m.autoriser_decision_regles(p, cfg, "0:100", 0.3, "moyenne") == sha       # même texte : idempotent
    # artefact 5 : un second texte scellé (autre empreinte), dans le même processus, est refusé (une seule version)
    with pytest.raises(GardeArret, match="autre préenregistrement"):
        m.autoriser_decision_regles(autre, cfg, "0:100", 0.3, "moyenne")
    assert m._AUTORISATION_DECISION == {"prereg_sha256": sha, "racines": (rho, rho_t)}


def test_C8_travail_derive_les_racines_du_meme_texte_et_exige_leur_egalite(tmp_path, sans_autorisation):
    """C8 : un processus de travail neuf dérive les racines du texte scellé reçu et exige qu'elles soient celles de la
    tâche ; en décision, la tâche est sérialisée (C10) ; sans texte (mode essai), ni autorisation ni sérialisation.
    L'exécution de la tâche est remplacée par un témoin : aucun tirage."""
    cfg = v4.CONFIG_V4
    p = prereg_scelle(tmp_path)
    attendues = m.deriver_racines_regle_D(hashlib.sha256(p.read_bytes()).hexdigest())
    appels = []
    sans_autorisation.setattr(m, "executer_tache_regles", lambda *a, **k: appels.append((a, k)) or {"temoin": len(appels)})

    def tache(r, rt, prereg):
        return (0, 1, r, rt, asdict(cfg), m.REGLES, (0.3,), ("moyenne",), False, prereg, 0.3, "moyenne")

    # sain : processus neuf, racines de la tâche = règle D du texte → la tâche part, sérialisée
    assert m._travail(tache(*attendues, str(p))) == {"temoin": 1}
    assert appels[-1][0][2:4] == attendues and appels[-1][1] == {"serialiser": True}
    assert m._AUTORISATION_DECISION["racines"] == attendues
    # artefacts : racines de la tâche ≠ règle D du texte → arrêt avant la tâche
    for mauvaises in ((attendues[0], attendues[0] + 1), RACINES_ORIGINALES, (attendues[1], attendues[0]), (R, RT)):
        with pytest.raises(GardeArret, match="≠ racines dérivées"):
            m._travail(tache(*mauvaises, str(p)))
    assert len(appels) == 1
    # artefact : texte modifié après scellement → arrêt (revérifié à chaque tâche)
    p.write_text(p.read_text(encoding="utf-8") + "\nmodifié pendant la course\n", encoding="utf-8")
    with pytest.raises(GardeArret, match="≠ scellée"):
        m._travail(tache(*attendues, str(p)))
    assert len(appels) == 1
    # mode essai (sans texte) : aucune autorisation demandée, aucune sérialisation
    m._travail(tache(R, RT, None))
    assert appels[-1][0][2:4] == (R, RT) and appels[-1][1] == {"serialiser": False}


def test_C9_main_decision_racines_derivees_manifeste_course_et_analyse(tmp_path, sans_autorisation):
    """C9 : la commande `decision` dérive (ρ, ρ_t) du texte scellé, vérifie le gel par son empreinte seule, consigne au
    manifeste les racines (entiers et chaînes), la règle D et l'empreinte du code v2, puis lance la course et l'analyse
    sur ρ. Manifeste, course, écritures et analyse remplacés par des témoins : aucun tirage, aucun fichier du dépôt."""
    from controle_ia import manifeste as man

    p = prereg_scelle(tmp_path)
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    rho, rho_t = m.deriver_racines_regle_D(sha)
    vu: dict = {"gel": [], "ecrits": []}
    gel_vrai = m.exiger_gel_regles

    def creer(depot, run_id, config, taches, **k):
        vu["manifeste"] = (depot, run_id, config, taches, k)
        return tmp_path / "runs" / run_id / "manifeste.json", {}

    def executer(instances, racine, racine_tenue, cfg, processus, *a, **k):
        vu["executer"] = (list(instances), racine, racine_tenue, processus, a, k)
        return [{"temoin": True}], {"mur_s": 0.0}

    def analyser(res, racine_reech, n_reech=20000):
        vu["analyse"] = racine_reech
        return {}

    def gel(racines=(), chemin=None):
        vu["gel"].append(tuple(racines))
        return gel_vrai(racines, chemin)

    sans_autorisation.setattr(m, "exiger_gel_regles", gel)
    sans_autorisation.setattr(man, "creer_manifeste", creer)
    sans_autorisation.setattr(man, "ecrire_resultat", lambda depot, chemin_m, nom, contenu: vu["ecrits"].append(nom))
    sans_autorisation.setattr(m, "executer", executer)
    sans_autorisation.setattr(m, "analyser_regles", analyser)
    assert m.main(["decision", "--prereg", str(p), "--instances", "0:100", "--run-id", "20261101-000000-essai",
                   "--lambda", "0.3", "--reference", "moyenne", "--processus", "2"]) == 0
    depot, run_id, config, taches, k = vu["manifeste"]
    assert depot == DEPOT and run_id == "20261101-000000-essai" and taches == ["regles-defense"]
    assert (config["racine"], config["racine_tenue"]) == (rho, rho_t)
    assert (config["racine_chaine"], config["racine_tenue_chaine"]) == (str(rho), str(rho_t))
    assert config["regle_racines"] == m.REGLE_D and "règle D" in m.REGLE_D
    assert config["code_v2_sha256"] == m.CODE_V2_SHA256 and config["prereg_sha256"] == sha
    assert config["gel_sha256"] == m.GEL_SHA256 and config["lambda"] == 0.3 and config["reference"] == "moyenne"
    assert config["config_sha256"] == v4.CONFIG_V4.empreinte() and config["instances"] == "0:100"
    assert k["entropie"] == rho and k["decisif"] is True and k["prereg"] == str(p)
    assert vu["gel"] == [()]                                       # gel vérifié par son empreinte seule
    instances, r, rt, processus, a, kk = vu["executer"]
    assert instances == list(range(100)) and (r, rt) == (rho, rho_t) and processus == 2
    assert a == (m.REGLES, (0.3,), ("moyenne",), False) and kk["prereg"] == str(p)
    assert kk["lam_dec"] == 0.3 and kk["ref_dec"] == "moyenne" and kk["sceller_pids"] is True
    assert vu["analyse"] == rho and vu["ecrits"] == ["resultats-regles-defense", "analyse-regles-defense"]


# ---------------------------------------------------------------------------------------------------------------
# E5 : diff restreint v2 → v3 par l'arbre syntaxique (liste fermée C1 à C12)
# ---------------------------------------------------------------------------------------------------------------
CHANGEMENTS_C1_C12 = {
    ("docstring",): "C1",
    ("assign", "VERSION"): "C2",
    ("assign", "IDENTIFIANT_PREREG"): "C2",
    ("assign", "ARENE_V4"): "C3",
    ("assign", "DOSSIER_V2"): "C3",                     # neuf : dossier de la course originale (gel v2, code v2)
    ("assign", "GEL"): "C3",                            # même fichier, désigné par son chemin dans le dépôt
    ("assign", "CODE_V2"): "C6, C11",                   # neuf
    ("assign", "CODE_V2_SHA256"): "C6, C11",            # neuf
    ("assign", "REGLE_D"): "C4, C9",                    # neuf
    ("assign", "RACINES_INTERDITES_REGLE_D"): "C4",     # neuf
    ("assign", "PLAGE_INTERDITE_REGLE_D"): "C4",        # neuf
    ("assign", "VECTEURS_ESSAI_REGLE_D"): "C4",         # neuf
    ("assign", "_RACINES_VECTEURS_ESSAI"): "C4",        # neuf
    ("assign", "_AUTORISATION_DECISION"): "C4, C5, C7",
    ("def", "etat_regle_D"): "C4",                      # neuve
    ("def", "exiger_racines_regle_D"): "C4",            # neuve
    ("def", "deriver_racines_regle_D"): "C4",           # neuve
    ("def", "exiger_racine_permise_regles"): "C5",
    ("def", "exiger_identite_prereg_regles"): "C6",
    ("def", "autoriser_decision_regles"): "C7",
    ("def", "_travail"): "C8",
    ("def", "main"): "C9",
    ("def", "finale_regle"): "C10",
    ("def", "serialiser_moniteur"): "C10",              # neuve
    ("def", "serialiser_variante"): "C10",              # neuve
    ("def", "executer_tache_regles"): "C10",
    ("def", "bloc_identite"): "C11",
    ("assign", "__all__"): "C12",
}


def _cle(k: int, noeud: ast.stmt) -> tuple:
    if k == 0 and isinstance(noeud, ast.Expr) and isinstance(noeud.value, ast.Constant) and \
            isinstance(noeud.value.value, str):
        return ("docstring",)
    if isinstance(noeud, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return ("def", noeud.name)
    if isinstance(noeud, ast.Assign):
        return ("assign", " ".join(ast.unparse(c) for c in noeud.targets))
    if isinstance(noeud, ast.AnnAssign):
        return ("assign", ast.unparse(noeud.target))
    return ("instruction", ast.unparse(noeud))


def _carte(chemin: Path) -> tuple[dict, list, dict]:
    """Instructions de niveau module : clé → (arbre sans positions, texte source exact), et leur ordre."""
    source = chemin.read_text(encoding="utf-8")
    arbre = ast.parse(source)
    arbres, textes, ordre = {}, {}, []
    for k, noeud in enumerate(arbre.body):
        cle = _cle(k, noeud)
        assert cle not in arbres, f"clé en double dans {chemin.name} : {cle}"
        arbres[cle] = ast.dump(noeud, include_attributes=False)
        textes[cle] = ast.get_source_segment(source, noeud)
        ordre.append(cle)
    return arbres, ordre, textes


def ecarts_diff_restreint(chemin_v3: Path) -> dict:
    """Écarts d'un fichier v3 à v2 hors de la liste fermée : instructions changées hors liste (arbre), entrées de la
    liste sans changement, instructions de v2 retirées, ordre relatif modifié, texte source changé hors liste."""
    a2, o2, t2 = _carte(m.CODE_V2)
    a3, o3, t3 = _carte(chemin_v3)
    changees = {k for k in set(a2) | set(a3) if a2.get(k) != a3.get(k)}
    return {"hors_liste": sorted(changees - set(CHANGEMENTS_C1_C12)),
            "liste_sans_changement": sorted(set(CHANGEMENTS_C1_C12) - changees),
            "retirees": sorted(set(a2) - set(a3)),
            "ordre_change": [k for k in o3 if k in a2] != o2,
            "texte_change": sorted(k for k in o2 if k not in CHANGEMENTS_C1_C12 and k in t3 and t2[k] != t3[k])}


SANS_ECART = {"hors_liste": [], "liste_sans_changement": [], "retirees": [], "ordre_change": False, "texte_change": []}


def test_E5_diff_restreint_v2_v3_par_l_arbre_syntaxique(tmp_path):
    assert m.empreinte_fichier(m.CODE_V2) == m.CODE_V2_SHA256        # référence du diff intacte (R11)
    v3 = Path(m.__file__)
    assert ecarts_diff_restreint(v3) == SANS_ECART                  # sain : exactement C1 à C12, rien d'autre
    a2, o2, t2 = _carte(m.CODE_V2)
    a3, o3, t3 = _carte(v3)
    inchangees = [k for k in o2 if k not in CHANGEMENTS_C1_C12]
    assert len(inchangees) >= 60 and all(a2[k] == a3[k] and t2[k] == t3[k] for k in inchangees)
    # artefacts (la garde du diff elle-même, R5) : copies de v3 altérées dans le dossier temporaire
    source = v3.read_text(encoding="utf-8")

    def altere(ancien: str, nouveau: str) -> dict:
        assert source.count(ancien) == 1, ancien
        p = tmp_path / f"altere-{len(list(tmp_path.iterdir()))}.py"
        p.write_text(source.replace(ancien, nouveau), encoding="utf-8")
        return ecarts_diff_restreint(p)

    # une fonction de calcul hors liste modifiée (écart-type du rééchantillonnage) → détectée
    assert altere('float(x.std(ddof=1)) if len(x) > 1', 'float(x.std(ddof=0)) if len(x) > 1')["hors_liste"] == \
        [("def", "_boot")]
    # une constante de mesure hors liste modifiée → détectée
    assert altere('MESURES_CONTRASTE = (("V_iii_final", 0)', 'MESURES_CONTRASTE = (("V_iii_final", 3)')[
        "hors_liste"] == [("assign", "MESURES_CONTRASTE")]
    # un commentaire seul modifié dans une fonction hors liste → détecté par le texte source (l'arbre l'ignore)
    e = altere("# R3′ : les deux joueurs à l'équilibre du jeu restreint", "# commentaire changé")
    assert e["hors_liste"] == [] and e["texte_change"] == [("def", "trajectoire_regle")]
    # une instruction de v2 retirée → détectée
    e = altere("v4.gen = gen_regles   #", "_gen_inutilise = gen_regles   #")
    assert ("assign", "v4.gen") in e["retirees"] and ("assign", "_gen_inutilise") in e["hors_liste"]
    # ce que le préenregistrement nomme « inchangé » l'est, en particulier
    for nom in ("trajectoire_regle", "analyser_regles", "_boot", "resume_variante", "choisir_lambda", "gen_regles",
                "entrainer_regularise", "entrainer_ctx_regularise", "objectif_regularise", "penalite_direction",
                "direction_reference", "exploitabilite", "exploitabilite_moyenne_tours", "exiger_defense_figee",
                "variantes", "nom_variante", "executer", "_lancer", "exiger_gel_regles", "exiger_racines_essai_regles",
                "charger_arene_v4", "_versions", "_plage", "_cout_depuis", "_minimize_compte", "_linprog_compte"):
        assert ("def", nom) in inchangees, nom
    for nom in ("MESURES_CONTRASTE", "MESURES_INDICATEUR", "REGLES", "CODES", "NOMS", "COMPTEUR", "GRILLE_LAMBDA",
                "REFERENCES", "TOLERANCE_CHOIX_LAMBDA", "PLAGE_REGLES", "RACINES_DECISION", "RACINES_GELEES",
                "RACINES_EMPLOYEES_V1", "_PERMISES_HORS_DECISION", "ARENE_V4_SHA256", "GEL_SHA256", "v4", "v4.gen",
                "(v4.minimize, v4.linprog)", "(RACINE_DECISION, RACINE_DECISION_TENUE)"):
        assert ("assign", nom) in inchangees, nom


# ---------------------------------------------------------------------------------------------------------------
# E6 (lent) : non-régression au bit sur la course originale ; E7 : sérialisation sans effet
# ---------------------------------------------------------------------------------------------------------------
CHAMPS_E6 = ("V_iii_final", "V_iii_standard", "V_iii_renforce", "exploitabilite_moyenne_tours", "ii_final",
             "fpr_final", "poids_finaux")


def _resultats_originaux() -> list[dict]:
    assert m.empreinte_fichier(RESULTATS_ORIGINAUX) == RESULTATS_ORIGINAUX_SHA256      # pièce scellée intacte
    return json.loads(RESULTATS_ORIGINAUX.read_text(encoding="utf-8"))["resultat"]["resultats"]


@LENT
def test_lent_E6_non_regression_au_bit_deux_taches_de_la_course_originale(sans_autorisation):
    """v3 rejoue (δ 1,4 ; instances 0 et 1) de la course originale sur ses racines d'origine, autorisation posée par
    l'essai seulement, sur le chemin de la décision (sérialisation comprise) ; aucune information neuve (résultats
    déjà scellés et lus). Égalité au bit : les champs listés par le préenregistrement (E6), puis tous les champs
    déterministes de la tâche (hors temps processeur et `version`)."""
    originaux = _resultats_originaux()
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "prereg_sha256", PREREG_ORIGINAL_SHA256)
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "racines", RACINES_ORIGINALES)
    for instance in (0, 1):
        ref = next(x for x in originaux if x["code_delta"] == 1 and x["instance"] == instance)
        assert (ref["racine"], ref["racine_tenue"]) == RACINES_ORIGINALES
        assert ref["config_sha256"] == v4.CONFIG_V4.empreinte() and ref["version"] == "arene_regles_defense_v2"
        r = m.executer_tache_regles(instance, 1, *RACINES_ORIGINALES, v4.CONFIG_V4, m.REGLES, (0.3,), ("moyenne",),
                                    False, serialiser=True)
        calc = json.loads(json.dumps(r))
        assert list(calc["regles"]) == list(ref["regles"]) == ["R0", "R1", "R2", "R3", "R4[moyenne,λ=0.3]"]
        for nom, x in ref["regles"].items():
            y = calc["regles"][nom]
            for champ in CHAMPS_E6:
                assert y[champ] == x[champ], (instance, nom, champ)
            assert y["par_tour"]["iii"] == x["par_tour"]["iii"] and y["par_tour"]["ii"] == x["par_tour"]["ii"]
            assert [d["poids"] for d in y["serialisation"]["defense_finale"]] == x["poids_finaux"]
        assert set(calc) - set(ref) == {"loi_cible"} and set(ref) <= set(calc)
        assert au_bit(sans_temps(calc, CHAMPS_V3)) == au_bit(sans_temps(ref)), instance


def test_E6_bis_analyse_v3_des_200_taches_originales_egale_l_analyse_scellee_au_bit(sans_autorisation):
    """La statistique (`analyser_regles`, `_boot`, `gen_regles` sous la v3, racine 20266201 posée par l'essai) rend
    l'analyse scellée de la course originale au bit (champ par champ, dont les dix quantiles des contrastes). Rapide
    (≈ 3 s : aucune tâche rejouée), donc jamais sauté."""
    originaux = _resultats_originaux()
    assert m.empreinte_fichier(ANALYSE_ORIGINALE) == ANALYSE_ORIGINALE_SHA256
    scellee = json.loads(ANALYSE_ORIGINALE.read_text(encoding="utf-8"))["resultat"]
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "prereg_sha256", PREREG_ORIGINAL_SHA256)
    sans_autorisation.setitem(m._AUTORISATION_DECISION, "racines", RACINES_ORIGINALES)
    an = m.analyser_regles(originaux, RACINES_ORIGINALES[0])
    c = an["1"]["contrastes_contre_R2"]["R3 - R2 (V_iii_final)"]
    assert c["moyenne"] == 0.10448042252007811 and c["quantiles"]["q0.00625"] == 0.09061967064630756   # spéc. § 12
    assert au_bit(an) == au_bit(scellee)


def test_E7_serialisation_ne_change_aucune_valeur_et_restitue_les_defenses():
    """Une tâche (petite configuration), avec et sans sérialisation : mêmes valeurs au bit (hors temps processeur) ;
    la sérialisation restitue W, b, seuil, échelle et poids, les attaques passées et finales, la cible : V standard,
    V renforcé et fausses alertes recalculés depuis elle seule (graines de la finale) sont ceux de la tâche, au bit."""
    cfg = CFG_PETITE
    sans = m.executer_tache_regles(0, 1, R, RT, cfg, m.REGLES, (0.3,), ("moyenne",))
    avec = m.executer_tache_regles(0, 1, R, RT, cfg, m.REGLES, (0.3,), ("moyenne",), serialiser=True)
    assert set(avec) - set(sans) == {"loi_cible"} and set(sans) <= set(avec)
    for nom in sans["regles"]:
        assert set(avec["regles"][nom]) - set(sans["regles"][nom]) == {"serialisation"}
    assert au_bit(sans_temps(avec, CHAMPS_V3)) == au_bit(sans_temps(sans))
    assert "serialisation" not in json.dumps(sans) and "loi_cible" not in sans
    # fidélité : reconstruire chaque défense finale depuis la sérialisation seule
    ctx = v4.Contexte(0, 1, R, RT, cfg)
    assert avec["loi_cible"] == [float(x) for x in ctx.cible]
    T1 = cfg.T + 1
    for nom, x in avec["regles"].items():
        s = x["serialisation"]
        defense = []
        for d in s["defense_finale"]:
            mon = v4.Moniteur(np.array(d["W"]), np.array(d["b"]))
            mon.t, mon.e = d["t"], d["e"]
            defense.append((mon, d["poids"]))
        assert [w for _, w in defense] == x["poids_finaux"]
        assert len(s["attaques_passees"]) == cfg.T and all(len(a) == 2 * cfg.K * cfg.d for a in s["attaques_passees"])
        assert [v4.distance(np.array(a), ctx.cible, cfg) for a in s["attaques_passees"]] == x["par_tour"]["distance"]
        cb = m.CODES[x["regle"]]
        a_std, a_renf = np.array(s["attaques_finales"]["standard"]), np.array(s["attaques_finales"]["renforce"])
        V_std = v4.taux_defense(defense, v4.echantillonner(a_std, cfg.n_eval, ctx.g(cb, T1, v4.ROLE_FINAL, 3), cfg))
        V_renf = v4.taux_defense(defense, v4.echantillonner(a_renf, cfg.n_eval, ctx.g(cb, T1, v4.ROLE_FINAL, 6), cfg))
        assert (V_std, V_renf) == (x["V_iii_standard"], x["V_iii_renforce"]), nom
        assert min(V_std, V_renf) == x["V_iii_final"] and v4.taux_defense(defense, ctx.Xfpr) == x["fpr_final"]
        assert v4.distance(a_std, ctx.cible, cfg) == x["distance_finale"]
    assert len(avec["regles"]["R3"]["serialisation"]["defense_finale"]) == cfg.T + 1
    assert all(len(x["serialisation"]["defense_finale"]) == 1 for n, x in avec["regles"].items() if n != "R3")
    # finale_regle : l'option ne change pas le résultat rendu, elle y ajoute les attaques
    ctx_a, M_a = contexte_et_M0()
    ctx_b, M_b = contexte_et_M0()
    etat_a, etat_b = m.trajectoire_regle("R2", ctx_a, M_a), m.trajectoire_regle("R2", ctx_b, M_b)
    fin_a = m.finale_regle("R2", etat_a, ctx_a)
    fin_b, (a_fin, a_renf) = m.finale_regle("R2", etat_b, ctx_b, rendre_attaques=True)
    assert au_bit(sans_temps(fin_a)) == au_bit(sans_temps(fin_b)) and a_fin.shape == a_renf.shape == ctx_a.cible.shape


# ---------------------------------------------------------------------------------------------------------------
# Mesures et réglages (gardes) — essais de la v2, inchangés
# ---------------------------------------------------------------------------------------------------------------
def test_exploitabilite_sain_et_artefacts():
    assert m.exploitabilite(0.0) == 1.0 and m.exploitabilite(1.0) == 0.0 and abs(m.exploitabilite(0.3) - 0.7) < 1e-12
    for mauvais in (1.5, -0.2, float("nan"), float("inf")):
        with pytest.raises(GardeArret, match="hors de \\[0 ; 1\\]"):
            m.exploitabilite(mauvais)


def test_X_barre_sain_et_artefacts():
    """X̄ = moyenne des X_t : dans [0 ; 1] ; un seul tour → X̄ = X_1 ; gardes sur liste vide et valeurs hors bornes."""
    assert m.exploitabilite_moyenne_tours([0.2, 0.4, 0.9]) == pytest.approx(0.5)
    assert m.exploitabilite_moyenne_tours([0.37]) == 0.37                                 # T = 1 : X̄ = X_1
    assert m.exploitabilite_moyenne_tours([0.0, 1.0]) == 0.5 and 0 <= m.exploitabilite_moyenne_tours([1.0]) <= 1
    with pytest.raises(GardeArret, match="aucun tour"):
        m.exploitabilite_moyenne_tours([])
    for mauvais in ([0.5, 1.5], [-0.1], [float("nan"), 0.2]):
        with pytest.raises(GardeArret, match="hors de \\[0 ; 1\\]"):
            m.exploitabilite_moyenne_tours(mauvais)


def test_garde_defense_figee_sain_et_artefact():
    M0 = v4.Moniteur(np.array([[1.0, 2.0]]), np.array([0.0]))
    m.exiger_defense_figee([M0], M0)                                                       # sain
    autre = v4.Moniteur(np.array([[1.0, 2.0]]), np.array([0.0]))                          # même valeur, autre objet
    with pytest.raises(GardeArret, match="défense figée a été modifiée"):
        m.exiger_defense_figee([autre], M0)
    with pytest.raises(GardeArret, match="défense figée a été modifiée"):
        m.exiger_defense_figee([M0, autre], M0)


def test_regle_lambda_reference_gardes():
    for r in m.REGLES:
        m.exiger_regle(r)
    assert m.REGLES == ("R0", "R1", "R2", "R3", "R4")
    with pytest.raises(GardeArret, match="règle inconnue"):
        m.exiger_regle("R9")
    assert m.exiger_lambda(0) == 0.0 and m.exiger_lambda("0.3") == 0.3
    for mauvais in (-1.0, float("nan")):
        with pytest.raises(GardeArret, match="négatif ou non fini"):
            m.exiger_lambda(mauvais)
    mon = v4.Moniteur(np.array([[1.0, 2.0]]), np.array([0.0]))
    assert np.allclose(m.direction_reference([mon], "dernier"), np.array([1.0, 2.0]) / np.sqrt(5))
    mon2 = v4.Moniteur(np.array([[-1.0, -2.0]]), np.array([0.0]))
    with pytest.raises(GardeArret, match="référence inconnue"):
        m.direction_reference([mon], "autre")
    with pytest.raises(GardeArret, match="direction de référence nulle"):
        m.direction_reference([mon, mon2], "moyenne")
    with pytest.raises(GardeArret, match="règle inconnue"):
        m.variantes(("R1", "R5"))
    assert len(m.variantes(m.REGLES, m.GRILLE_LAMBDA, m.REFERENCES)) == 4 + 2 * len(m.GRILLE_LAMBDA)
    assert m.variantes(m.REGLES, (0.3,), ("moyenne",))[0] == ("R0", None, None)


def test_penalite_direction_gradient_et_invariance():
    g = m.gen_regles(R, 0, 0, 0, 0, 90)
    w, u = g.standard_normal(6), g.standard_normal(6)
    u /= np.linalg.norm(u)
    val, grad = m.penalite_direction(w, u, 0.7)
    assert abs(val - 0.7 * np.sum((w / np.linalg.norm(w) - u) ** 2)) < 1e-12
    num = np.array([(m.penalite_direction(w + h * e, u, 0.7)[0] - m.penalite_direction(w - h * e, u, 0.7)[0]) / (2 * h)
                    for e in np.eye(6) for h in (1e-6,)])
    assert np.allclose(num, grad, atol=1e-6)
    assert abs(m.penalite_direction(3.0 * w, u, 0.7)[0] - val) < 1e-12          # sans échelle
    assert m.penalite_direction(np.zeros(6), u, 0.7) == (1.4, pytest.approx(np.zeros(6)))   # direction indéfinie


def test_entrainement_regularise_lambda_zero_egal_v4_et_lambda_fort_rapproche():
    cfg = CFG_PETITE
    ctx, M0 = contexte_et_M0()
    Xp = ctx.propre_entr(1)
    att = v4.projeter(ctx.cible + 0.5 * m.gen_regles(R, 0, 0, 0, 0, 91).standard_normal(ctx.cible.size), ctx.cible,
                      ctx.delta, cfg)[0]
    Xa = v4.echantillonner(att, cfg.n_attaque_entr, m.gen_regles(R, 0, 0, 0, 0, 92), cfg)
    mu, _ = v4.deplier(att, cfg)
    dirs = [v / np.linalg.norm(v) for v in mu]
    u = m.direction_reference([M0], "dernier")
    mon_v4, ok_v4 = v4.entrainer(Xp, Xa, 1, cfg, None, dirs)
    mon_0, ok_0 = m.entrainer_regularise(Xp, Xa, cfg, u, 0.0, dirs)
    assert np.array_equal(mon_v4.W, mon_0.W) and np.array_equal(mon_v4.b, mon_0.b) and ok_v4 == ok_0   # λ = 0 : au bit
    mon_3, _ = m.entrainer_regularise(Xp, Xa, cfg, u, 3.0, dirs)
    cos = lambda w: float(w @ u / np.linalg.norm(w))  # noqa: E731
    assert cos(mon_3.W[0]) > cos(mon_0.W[0]) and not np.array_equal(mon_3.W, mon_0.W)   # λ fort : plus proche de u
    with pytest.raises(GardeArret, match="oracle « détection » exigé"):
        m.entrainer_regularise(Xp, Xa, m.replace(cfg, entrainement="logistique"), u, 0.0, dirs)
    # au niveau du contexte, même code de graine : identique au bit à `Contexte.entrainer`
    ctx_a, _ = contexte_et_M0()
    ctx_b, M0_b = contexte_et_M0()
    a = ctx_a.entrainer(1, 1, [ctx_a.cible, att], np.array([0.5, 0.5]), 1)
    b = m.entrainer_ctx_regularise(ctx_b, 1, 1, [ctx_b.cible, att], np.array([0.5, 0.5]),
                                   m.direction_reference([M0_b], "dernier"), 0.0)
    assert np.array_equal(a.W, b.W) and np.array_equal(a.b, b.b) and a.t == b.t and ctx_b.entr == ctx_a.entr


# ---------------------------------------------------------------------------------------------------------------
# Trajectoires : chaque règle (R0 comprise), essais clés R2 = A, R3 = B, R4(λ = 0) = R2 à code égal, tenues jamais vues
# — essais de la v2, inchangés
# ---------------------------------------------------------------------------------------------------------------
def test_chaque_regle_trajectoire_T3_petite_config_en_moins_de_30_s(tache_petite):
    r, cpu = tache_petite
    assert cpu < 30.0, cpu
    noms = set(r["regles"])
    assert noms == {"R0", "R1", "R2", "R3", "R4[dernier,λ=0]", "R4[dernier,λ=0.3]", "R4[moyenne,λ=0]",
                    "R4[moyenne,λ=0.3]"}
    assert list(r["regles"])[:4] == ["R0", "R1", "R2", "R3"]                      # rang des variantes (rééchantillonnage)
    assert "loi_cible" not in r and all("serialisation" not in x for x in r["regles"].values())   # C10 : hors décision
    for nom, x in r["regles"].items():
        pt = x["par_tour"]
        assert len(pt["iii"]) == 3 and len(pt["exploitabilite"]) == 3 and len(pt["ii"]) == 3
        assert len(pt["cos_consecutif"]) == 3 and all(-1 - 1e-9 <= c <= 1 + 1e-9 for c in pt["cos_consecutif"])
        assert all(0 <= v <= 1 for v in pt["iii"] + pt["exploitabilite"] + pt["ii"])
        assert all(abs(e - (1 - i)) < 1e-12 for e, i in zip(pt["exploitabilite"], pt["iii"]))
        # X̄ : dans [0 ; 1], égale à la moyenne des X_t rendus par tour
        assert 0 <= x["exploitabilite_moyenne_tours"] <= 1
        assert abs(x["exploitabilite_moyenne_tours"] - np.mean(pt["exploitabilite"])) < 1e-12
        assert 0 <= x["exploitabilite_finale"] <= 1 and abs(x["exploitabilite_finale"] - (1 - x["V_iii_final"])) < 1e-12
        assert 0 <= x["ii_final"] <= 1 and 0 <= x["i_final_vus"] <= 1
        assert abs(x["fpr_final"] - CFG_PETITE.alpha) <= CFG_PETITE.tol_fpr
        assert x["cout_trajectoire"]["departs_attaquant"] == 3 * (CFG_PETITE.departs + 2)
        assert x["cpu_trajectoire_s"] > 0 and x["cpu_final_s"] > 0
        assert x["cycle"]["I3_nul"] == pytest.approx(v4.valeur_nulle_I3(3)) and x["cycle"]["I3_retours"] in (0.0, 1.0)
        assert len(x["cycle"]["H"]) == 4 and all(len(l) == 3 for l in x["cycle"]["H"])
        if nom == "R0":
            # témoin : zéro entraînement, un seul moniteur stocké (7 paramètres), H à lignes identiques, I2 = 0, cos = 1
            assert x["cout_trajectoire"]["entrainements"] == 0 and x["cout_trajectoire"]["appels_optimiseur"] > 0
            assert x["nb_moniteurs_stockes"] == 1 and x["parametres_stockes"] == CFG_PETITE.d + 1
            assert all(ligne == x["cycle"]["H"][0] for ligne in x["cycle"]["H"]) and x["cycle"]["I2_oubli"] == 0.0
            assert pt["cos_consecutif"] == [1.0, 1.0, 1.0]
        else:
            assert x["cout_trajectoire"]["entrainements"] == 3 and x["cout_trajectoire"]["appels_optimiseur"] > 0
        if nom == "R3":
            assert x["cout_trajectoire"]["programmes_lineaires"] > 0 and len(pt["valeur_jeu_restreint"]) == 3
            assert x["valeur_jeu_restreint"] is not None and "equilibre" in x and x["nb_moniteurs_stockes"] == 4
            assert all(v >= i - 0.06 for v, i in zip(pt["valeur_jeu_restreint"], pt["iii"]))  # R3′ ≥ (iii) (bruit)
        else:
            assert x["cout_trajectoire"]["programmes_lineaires"] == 0 and pt["valeur_jeu_restreint"] == []
            assert x["poids_finaux"] == [1.0] and x["parametres_deployes"] == CFG_PETITE.d + 1
    assert r["entrainements"] == 2 + 7 * 3 and r["non_convergences"] <= r["entrainements"] * CFG_PETITE.taux_nonconv_max
    # les mesures bougent entre règles (pas une constante recopiée)
    assert len({round(x["V_iii_final"], 6) for x in r["regles"].values()}) > 1
    assert len({round(x["exploitabilite_moyenne_tours"], 6) for x in r["regles"].values()}) > 1
    # R4 : les deux références coïncident à λ = 0 (pénalité nulle)
    assert r["regles"]["R4[dernier,λ=0]"]["V_iii_final"] == r["regles"]["R4[moyenne,λ=0]"]["V_iii_final"]


def test_R2_reproduit_A_du_v4_au_bit():
    """Essai clé : la boucle commune avec la règle R2 rend, à graine égale, la trajectoire et la finale du bras A."""
    ctx_a, M_a = contexte_et_M0()
    etat_a = v4.trajectoire("A", ctx_a, M_a, leger=False)
    ctx_r, M_r = contexte_et_M0()
    etat_r = m.trajectoire_regle("R2", ctx_r, M_r)
    assert len(etat_a["attaques"]) == len(etat_r["attaques"]) == CFG_PETITE.T + 1
    assert all(np.array_equal(a, b) for a, b in zip(etat_a["attaques"], etat_r["attaques"]))
    for ma, mr in zip(etat_a["moniteurs"], etat_r["moniteurs"]):
        assert np.array_equal(ma.W, mr.W) and np.array_equal(ma.b, mr.b) and ma.t == mr.t
    for cle in ("iii", "ii", "distance", "nouveaute", "projections", "poids_max"):
        assert etat_a["par_tour"][cle] == etat_r["par_tour"][cle], cle
    assert etat_a["cycle"]["H"] == etat_r["cycle"]["H"] and etat_a["cycle"]["I1_progres"] == etat_r["cycle"]["I1_progres"]
    assert etat_r["exploitabilite_moyenne_tours"] == pytest.approx(1 - np.mean(etat_a["par_tour"]["iii"]), abs=1e-12)
    fin_a = v4.phase_finale("A", etat_a["defense_finale"], ctx_a, etat_a, leger=True)
    fin_r = m.finale_regle("R2", etat_r, ctx_r)
    for cle in ("V_iii_final", "V_iii_standard", "V_iii_renforce", "fpr_final", "distance_finale", "poids_finaux"):
        assert fin_a[cle] == fin_r[cle], cle
    assert ctx_a.entr == ctx_r.entr and ctx_a.att["departs"] == ctx_r.att["departs"]


def test_R3_reproduit_B_du_v4_au_bit():
    ctx_b, M_b = contexte_et_M0()
    etat_b = v4.trajectoire("B", ctx_b, M_b, leger=False)
    ctx_r, M_r = contexte_et_M0()
    etat_r = m.trajectoire_regle("R3", ctx_r, M_r)
    assert all(np.array_equal(a, b) for a, b in zip(etat_b["attaques"], etat_r["attaques"]))
    assert etat_b["par_tour"]["iii"] == etat_r["par_tour"]["iii"] and etat_b["par_tour"]["ii"] == etat_r["par_tour"]["ii"]
    assert etat_b["valeur_jeu_restreint"] == etat_r["valeur_jeu_restreint"] and etat_b["equilibre"] == etat_r["equilibre"]
    assert [w for _, w in etat_b["defense_finale"]] == [w for _, w in etat_r["defense_finale"]]
    fin_b = v4.phase_finale("B", etat_b["defense_finale"], ctx_b, etat_b, leger=True)
    fin_r = m.finale_regle("R3", etat_r, ctx_r)
    assert fin_b["V_iii_final"] == fin_r["V_iii_final"] and fin_b["fpr_final"] == fin_r["fpr_final"]


def test_R4_lambda_zero_egal_R2_sur_la_trajectoire_a_code_de_graine_egal(monkeypatch):
    """À λ = 0 la mise à jour de R4 est celle de R2 ; les trajectoires ne diffèrent que par le code de graine de
    l'attaquant (24 ≠ 1, déclaré) : à code forcé égal (essai seulement), identité au bit."""
    ctx_2, M_2 = contexte_et_M0()
    etat_2 = m.trajectoire_regle("R2", ctx_2, M_2)
    monkeypatch.setitem(m.CODES, "R4", m.CODES["R2"])
    ctx_4, M_4 = contexte_et_M0()
    etat_4 = m.trajectoire_regle("R4", ctx_4, M_4, lam=0.0, reference="moyenne")
    assert all(np.array_equal(a, b) for a, b in zip(etat_2["attaques"], etat_4["attaques"]))
    for ma, mb in zip(etat_2["moniteurs"], etat_4["moniteurs"]):
        assert np.array_equal(ma.W, mb.W) and np.array_equal(ma.b, mb.b)
    assert etat_2["par_tour"]["iii"] == etat_4["par_tour"]["iii"]
    assert etat_2["exploitabilite_moyenne_tours"] == etat_4["exploitabilite_moyenne_tours"]
    # à λ > 0 et même code, la trajectoire change dès le premier réentraînement
    ctx_5, M_5 = contexte_et_M0()
    etat_5 = m.trajectoire_regle("R4", ctx_5, M_5, lam=1.0, reference="dernier")
    assert np.array_equal(etat_5["attaques"][1], etat_2["attaques"][1])        # tour 1 : même défense M0, même attaque
    assert not np.array_equal(etat_5["moniteurs"][1].W, etat_2["moniteurs"][1].W)


def test_R0_ne_reentraine_jamais_instrumentation(monkeypatch):
    """Témoin : après le tour 0, zéro appel à `Contexte.entrainer`, à `entrainer_ctx_regularise`, à `v4.entrainer`
    et à `entrainer_regularise` pendant la trajectoire de R0 ; M0 reste l'objet déployé ; la finale lit M0."""
    appels = {"ctx": 0, "r4": 0, "v4": 0, "reg": 0}
    orig_ctx, orig_r4, orig_v4, orig_reg = v4.Contexte.entrainer, m.entrainer_ctx_regularise, v4.entrainer, \
        m.entrainer_regularise

    def ctx_espion(self, *a, **k):
        appels["ctx"] += 1
        return orig_ctx(self, *a, **k)

    def r4_espion(*a, **k):
        appels["r4"] += 1
        return orig_r4(*a, **k)

    def v4_espion(*a, **k):
        appels["v4"] += 1
        return orig_v4(*a, **k)

    def reg_espion(*a, **k):
        appels["reg"] += 1
        return orig_reg(*a, **k)

    ctx, M0 = contexte_et_M0()                       # tour 0 : M0 entraîné AVANT la pose des espions
    monkeypatch.setattr(v4.Contexte, "entrainer", ctx_espion)
    monkeypatch.setattr(m, "entrainer_ctx_regularise", r4_espion)
    monkeypatch.setattr(v4, "entrainer", v4_espion)
    monkeypatch.setattr(m, "entrainer_regularise", reg_espion)
    entr0, c0 = ctx.entr, m.COMPTEUR["minimize"]
    etat = m.trajectoire_regle("R0", ctx, M0)
    assert appels == {"ctx": 0, "r4": 0, "v4": 0, "reg": 0}                      # zéro entraînement après le tour 0
    assert ctx.entr == entr0 and etat["cout_trajectoire"]["entrainements"] == 0
    assert etat["moniteurs"] == [M0] and etat["defense_finale"] == [(M0, 1.0)]
    assert len(etat["attaques"]) == CFG_PETITE.T + 1 and len(etat["par_tour"]["iii"]) == CFG_PETITE.T
    assert m.COMPTEUR["minimize"] > c0                                               # l'attaquant, lui, a joué
    assert etat["cycle"]["I2_oubli"] == 0.0 and etat["par_tour"]["cos_consecutif"] == [1.0] * CFG_PETITE.T
    assert 0 <= etat["exploitabilite_moyenne_tours"] <= 1
    fin = m.finale_regle("R0", etat, ctx)
    assert fin["poids_finaux"] == [1.0] and fin["parametres_deployes"] == CFG_PETITE.d + 1
    assert appels == {"ctx": 0, "r4": 0, "v4": 0, "reg": 0}                      # la finale n'entraîne pas non plus
    # contrôle de l'instrumentation (artefact) : R1 sur le même contexte déclenche bien les espions
    etat_1 = m.trajectoire_regle("R1", ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, CFG_PETITE.alpha))
    assert appels["ctx"] == CFG_PETITE.T and appels["v4"] == CFG_PETITE.T and etat_1["cout_trajectoire"]["entrainements"] == 3


def test_R0_reproductible_a_graine_fixee_et_autre_racine_differente():
    ctx_1, M_1 = contexte_et_M0()
    ctx_2, M_2 = contexte_et_M0()
    e1, e2 = m.trajectoire_regle("R0", ctx_1, M_1), m.trajectoire_regle("R0", ctx_2, M_2)
    assert all(np.array_equal(a, b) for a, b in zip(e1["attaques"], e2["attaques"]))
    assert e1["par_tour"]["iii"] == e2["par_tour"]["iii"] and e1["par_tour"]["ii"] == e2["par_tour"]["ii"]
    assert e1["exploitabilite_moyenne_tours"] == e2["exploitabilite_moyenne_tours"]
    assert np.array_equal(M_1.W, M_2.W)                                               # M0 reproductible au bit
    # R0 et R1 partagent M0 et la première attaque n'est pas la même (codes de graine 20 et 21 distincts)
    ctx_3, M_3 = contexte_et_M0()
    e3 = m.trajectoire_regle("R1", ctx_3, M_3)
    assert not np.array_equal(e3["attaques"][1], e1["attaques"][1])
    ctx_4, M_4 = contexte_et_M0(racine=RA, racine_tenue=RT)
    e4 = m.trajectoire_regle("R0", ctx_4, M_4)
    assert not np.array_equal(ctx_4.cible, ctx_1.cible) and e4["par_tour"]["iii"] != e1["par_tour"]["iii"]


def test_X_barre_egale_X1_quand_T_vaut_1():
    """T = 1 : X̄ = X_1 = 1 − (iii)_1 exactement (un seul tour) ; X finale en diffère en général (attaquant lourd de la
    finale contre la défense finale, attaquant léger du tour contre la défense déployée au tour 1 : gel v2 § 4)."""
    cfg1 = m.replace(CFG_PETITE, T=1)
    for regle in ("R0", "R1", "R2"):
        ctx, M0 = contexte_et_M0(cfg=cfg1)
        etat = m.trajectoire_regle(regle, ctx, M0)
        assert len(etat["par_tour"]["exploitabilite"]) == 1
        assert etat["exploitabilite_moyenne_tours"] == etat["par_tour"]["exploitabilite"][0]
        assert etat["exploitabilite_moyenne_tours"] == pytest.approx(1 - etat["par_tour"]["iii"][0], abs=1e-12)
        assert 0 <= etat["exploitabilite_moyenne_tours"] <= 1
        assert etat["cycle"]["I3_moins_nul"] is None                                   # T < 3 : I3 sans valeur nulle


@LENT
def test_lent_parite_de_T_X_barre_stable_X_finale_non_pour_R1():
    """Essai lent (configuration complète du v4, une instance, un δ, racine d'essai v2) : pour R1, X finale lue à
    T = 3 (moniteur impair déployé) et à T = 4 (moniteur pair) s'écarte davantage que X̄ lue aux mêmes T. Motif : la
    dynamique de R1 est de période 2 (formalisation § 4.1, CL-05) ; X̄ moyenne sur les tours, X finale lit la phase.
    Tolérance : |X̄(3) − X̄(4)| ≤ 0,05 et |X_fin(3) − X_fin(4)| > |X̄(3) − X̄(4)| ; un échec informe (une instance)."""
    out = {}
    for T in (3, 4):
        cfg = m.replace(v4.CONFIG_V4, T=T)
        ctx, M0 = contexte_et_M0(cfg=cfg)
        etat = m.trajectoire_regle("R1", ctx, M0)
        fin = m.finale_regle("R1", etat, ctx)
        out[T] = (etat["exploitabilite_moyenne_tours"], fin["exploitabilite_finale"], etat["par_tour"]["iii"])
    # les trois premiers tours sont identiques au bit (mêmes graines par tour) : X̄ ne diffère que par le 4e tour
    assert out[3][2] == out[4][2][:3]
    d_barre, d_fin = abs(out[3][0] - out[4][0]), abs(out[3][1] - out[4][1])
    assert d_barre <= 0.05, out
    assert d_fin > d_barre, out


def test_tenues_jamais_vues_par_l_entrainement(monkeypatch):
    """Instrumentation : toute attaque passée à un entraînement (v4 ou R4) est la cible ou une meilleure réponse de la
    trajectoire ; aucune n'est une loi tenue à l'écart ; les lois tenues viennent de la racine tenue seule."""
    vues = []
    orig = v4.Contexte.entrainer

    def entrainer_espion(self, bras, tour, attaques, q, mm):
        vues.extend(np.asarray(a, float).copy() for a in attaques)
        return orig(self, bras, tour, attaques, q, mm)

    orig_r4 = m.entrainer_ctx_regularise

    def r4_espion(ctx, cb, tour, attaques, q, u, lam):
        vues.extend(np.asarray(a, float).copy() for a in attaques)
        return orig_r4(ctx, cb, tour, attaques, q, u, lam)

    monkeypatch.setattr(v4.Contexte, "entrainer", entrainer_espion)
    monkeypatch.setattr(m, "entrainer_ctx_regularise", r4_espion)
    ctx = v4.Contexte(1, 2, R, RT, CFG_PETITE)
    M0 = ctx.entrainer(v4.COMMUN, 0, [ctx.cible], np.array([1.0]), 1)
    legitimes = [ctx.cible]
    for regle, lam in (("R0", 0.0), ("R1", 0.0), ("R2", 0.0), ("R3", 0.0), ("R4", 0.3)):
        etat = m.trajectoire_regle(regle, ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, CFG_PETITE.alpha),
                                   lam=lam)
        legitimes += etat["attaques"][1:]
    assert len(vues) > 0 and len(ctx.tenues) == CFG_PETITE.n_tenue
    for a in vues:
        assert any(np.array_equal(a, b) for b in legitimes)
        assert all(np.max(np.abs(a - t)) > 1e-6 for t in ctx.tenues)
    # racine tenue à part : une autre racine tenue change les lois tenues, pas la trajectoire
    ctx_b = v4.Contexte(1, 2, R, RA, CFG_PETITE)
    assert not any(np.array_equal(t, u) for t, u in zip(ctx.tenues, ctx_b.tenues))
    M0_b = ctx_b.entrainer(v4.COMMUN, 0, [ctx_b.cible], np.array([1.0]), 1)
    e_b = m.trajectoire_regle("R0", ctx_b, v4.Moniteur(M0_b.W.copy(), M0_b.b.copy()).calibrer(ctx_b.Xcal, CFG_PETITE.alpha))
    e_a = m.trajectoire_regle("R0", ctx, v4.Moniteur(M0.W.copy(), M0.b.copy()).calibrer(ctx.Xcal, CFG_PETITE.alpha))
    assert all(np.array_equal(a, b) for a, b in zip(e_a["attaques"], e_b["attaques"]))
    assert e_a["par_tour"]["ii"] != e_b["par_tour"]["ii"]


def test_graine_reproductible_et_autre_racine_change_le_resultat():
    ctx_1, M_1 = contexte_et_M0()
    ctx_2, M_2 = contexte_et_M0()
    e1, e2 = m.trajectoire_regle("R1", ctx_1, M_1), m.trajectoire_regle("R1", ctx_2, M_2)
    assert all(np.array_equal(a, b) for a, b in zip(e1["attaques"], e2["attaques"]))
    assert e1["par_tour"]["iii"] == e2["par_tour"]["iii"] and e1["par_tour"]["ii"] == e2["par_tour"]["ii"]
    ctx_3, M_3 = contexte_et_M0(racine=RA, racine_tenue=RT)
    e3 = m.trajectoire_regle("R1", ctx_3, M_3)
    assert not np.array_equal(ctx_3.cible, ctx_1.cible) and e3["par_tour"]["iii"] != e1["par_tour"]["iii"]


def test_plafond_de_temps_processeur_sain_et_artefact():
    v4.exiger_plafond(time.process_time(), CFG_PETITE, "sain")
    ctx, M0 = contexte_et_M0(cfg=m.replace(CFG_PETITE, plafond_cpu_tache_s=1e-9))
    with pytest.raises(GardeArret, match="plafond de temps processeur"):
        m.trajectoire_regle("R1", ctx, M0)
    ctx, M0 = contexte_et_M0(cfg=m.replace(CFG_PETITE, plafond_cpu_tache_s=1e-9))
    with pytest.raises(GardeArret, match="plafond de temps processeur"):     # la branche R0 exerce aussi le plafond
        m.trajectoire_regle("R0", ctx, M0)


# ---------------------------------------------------------------------------------------------------------------
# Analyse, choix de λ, commande essai — essais de la v2 (version adaptée)
# ---------------------------------------------------------------------------------------------------------------
def test_analyse_et_choix_lambda(tache_petite):
    r0, _ = tache_petite
    r1 = m.executer_tache_regles(1, 1, R, RT, CFG_PETITE, lambdas=(0.0, 0.3), references=("dernier", "moyenne"))
    an = m.analyser_regles([r0, r1], R, n_reech=200)
    bloc = an["1"]
    assert bloc["n"] == 2 and set(bloc["variantes"]) == set(r0["regles"])
    c = bloc["contrastes_contre_R2"]["R1 - R2 (V_iii_final)"]
    q = c["quantiles"]
    assert q["q0.00625"] <= q["q0.025"] <= q["q0.975"] <= q["q0.99375"] and c["n"] == 2
    assert abs(c["moyenne"] - np.mean([r["regles"]["R1"]["V_iii_final"] - r["regles"]["R2"]["V_iii_final"]
                                       for r in (r0, r1)])) < 1e-12
    # X̄ : contraste apparié présent pour chaque variante ≠ R2, R0 comprise ; moyenne exacte
    for nom in ("R0", "R1", "R3"):
        cx = bloc["contrastes_contre_R2"][f"{nom} - R2 (exploitabilite_moyenne_tours)"]
        assert abs(cx["moyenne"] - np.mean([r["regles"][nom]["exploitabilite_moyenne_tours"]
                                            - r["regles"]["R2"]["exploitabilite_moyenne_tours"] for r in (r0, r1)])) < 1e-12
        e = bloc["contrastes_contre_R2"][f"{nom} - R2 (V standard seul / renforce seul)"]
        assert abs(e["ecart"] - (e["moyenne_standard"] - e["moyenne_renforce"])) < 1e-12
    assert "R2 - R2 (V_iii_final)" not in bloc["contrastes_contre_R2"]
    assert bloc["variantes"]["R0"]["exploitabilite_moyenne_tours"] == pytest.approx(
        np.mean([r["regles"]["R0"]["exploitabilite_moyenne_tours"] for r in (r0, r1)]))
    assert bloc["variantes"]["R0"]["cos_consecutif_par_tache"] == [1.0, 1.0] and bloc["variantes"]["R0"]["cos_consecutif_moyen"] == 1.0
    assert len(bloc["variantes"]["R1"]["cos_consecutif_par_tache"]) == 2
    assert "R3 I1_progres" in bloc["indicateurs"] and "R3 I3_moins_nul" in bloc["indicateurs"]
    assert "R0 I1_progres" in bloc["indicateurs"]
    assert "valeur_jeu_restreint_par_tour" in bloc["variantes"]["R3"] and "poids" in bloc["variantes"]["R3"]
    ch = an["choix_lambda"]
    assert ch["retenu"] in r0["regles"] and ch["retenu"].startswith("R4[")
    # règle d'égalité : même moyenne → plus petite λ, puis « dernier »
    faux = [{"regles": {"R4[dernier,λ=0.3]": {"V_iii_final": 0.50, "lam": 0.3, "reference": "dernier"},
                        "R4[dernier,λ=0.1]": {"V_iii_final": 0.497, "lam": 0.1, "reference": "dernier"},
                        "R4[moyenne,λ=0.1]": {"V_iii_final": 0.499, "lam": 0.1, "reference": "moyenne"},
                        "R2": {"V_iii_final": 0.9}}}]
    assert m.choisir_lambda(faux)["retenu"] == "R4[dernier,λ=0.1]"
    faux[0]["regles"]["R4[dernier,λ=0.3]"]["V_iii_final"] = 0.6
    assert m.choisir_lambda(faux)["retenu"] == "R4[dernier,λ=0.3]"
    assert m.choisir_lambda([{"regles": {"R2": {"V_iii_final": 0.9}}}])["retenu"] is None
    # codes de rééchantillonnage : aucune collision entre contrastes (200 + 100 j + k) et indicateurs (500 + 100 j + k)
    codes_c = {200 + 100 * j + k for _, j in m.MESURES_CONTRASTE for k in range(len(r0["regles"]))}
    codes_i = {500 + 100 * j + k for _, j in m.MESURES_INDICATEUR for k in range(len(r0["regles"]))}
    assert not codes_c & codes_i


def test_cli_essai_refuse_racines_interdites_et_ecrasement(tmp_path):
    sortie = tmp_path / "s.json"
    for racine, motif in ((m.RACINE_DECISION, "réservée à la décision"), (v4.RACINE_ESSAI, "réservée au v4"),
                          (20266999, "non gelée"), (20266101, "employée par la v1")):
        with pytest.raises(GardeArret, match=motif):
            m.main(["essai", "--instances", "0:1", "--sortie", str(sortie), "--racine", str(racine)])
    assert not sortie.exists()
    sortie.write_text("{}", encoding="utf-8")
    with pytest.raises(GardeArret, match="existe déjà"):
        m.main(["essai", "--instances", "0:1", "--sortie", str(sortie)])
    with pytest.raises(GardeArret, match="règle inconnue"):
        m.main(["essai", "--instances", "0:1", "--sortie", str(tmp_path / "t.json"), "--regles", "R0,R7"])


def test_cli_essai_ecrit_un_pilote_minuscule_et_orphelins(tmp_path, monkeypatch):
    """Un processus, une instance, T = 2, R0, R1 et R2 : la commande écrit le fichier avec manifeste, analyse,
    résultats (X̄ compris) ; la commande `orphelins` lit un fichier de PID morts sans erreur."""
    monkeypatch.setattr(v4, "CONFIG_V4", m.replace(CFG_PETITE, T=2))
    sortie = tmp_path / "pilote.json"
    assert m.main(["essai", "--instances", "0:1", "--sortie", str(sortie), "--processus", "1", "--regles", "R0,R1,R2",
                   "--lambdas", "0.3", "--references", "moyenne"]) == 0
    corps = json.loads(sortie.read_text(encoding="utf-8"))
    assert corps["mode"] == "essai" and corps["manifeste"]["racine"] == m.RACINE_ESSAI == 20266501
    assert corps["version"] == "arene_regles_defense_v3"
    assert corps["manifeste"]["gel_sha256"] == m.GEL_SHA256 and corps["manifeste"]["versions"]["arene_v4_sha256"] == m.ARENE_V4_SHA256
    assert set(corps["resultats"][0]["regles"]) == {"R0", "R1", "R2"} and len(corps["resultats"]) == 2
    for r in corps["resultats"]:
        for nom in ("R0", "R1", "R2"):
            assert 0 <= r["regles"][nom]["exploitabilite_moyenne_tours"] <= 1
            assert "serialisation" not in r["regles"][nom]                  # C10 : mode essai inchangé
        assert r["regles"]["R0"]["cout_trajectoire"]["entrainements"] == 0
    assert "R0 - R2 (exploitabilite_moyenne_tours)" in corps["analyse"]["1"]["contrastes_contre_R2"]
    assert corps["analyse"]["choix_lambda"]["retenu"] is None and corps["temps"]["taches"] == 2
    pids = tmp_path / "pids.txt"
    pids.write_text("# essai\n4194303 1\n", encoding="utf-8")
    assert m.main(["orphelins", "--pids", str(pids)]) == 0
