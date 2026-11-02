"""Essais hors réseau de l'épreuve fraîche du pont v1 : tirage, éligibilité, dédoublonnage, garde de plafond, refus, arrêts,
ordre mêlé, absence de clé dans les sorties. Faux appelants seulement (réponses JSON fabriquées) ; aucun appel de modèle,
aucun appel réseau, aucune clé réelle. Chaque garde est essayée sur un cas sain et sur un artefact (R5).

Les essais qui lisent les vraies fiches (tirage sur les entrées réelles) ne comparent que des empreintes et des identifiants :
un échec n'affiche jamais un énoncé. Le groupe « bout en bout » exige l'orchestrateur v56 déplié (`PONT_POLE_V56`) ; sans lui il
est ignoré avec son motif, jamais en silence.

Jouer (Python du dépôt) : cd <dossier vide> && python -I -B -m pytest -q -p no:cacheprovider <ce fichier>
"""

import argparse
import hashlib
import json
import os
import shutil
import sys
import threading
from pathlib import Path

import pytest

ICI = Path(__file__).resolve().parent
DEPOT = ICI.parents[1]
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI / "pont"))
sys.path.insert(0, str(DEPOT / "src"))

import lancer_epreuve_pont_v1 as L  # noqa: E402
import pont_v1 as pv  # noqa: E402
import tirer_fiches_v1 as tf  # noqa: E402
from controle_ia.prereg import SECTIONS  # noqa: E402
from controle_ia.scellement import sceller  # noqa: E402

POLE = os.environ.get("PONT_POLE_V56")
AVEC_V56 = bool(POLE) and (Path(POLE) / "pole" / "proposeur.py").is_file()
v56 = pytest.mark.skipif(not AVEC_V56, reason="PONT_POLE_V56 absent : orchestrateur v56 non déplié, groupe non joué (dit)")

C = L.charger_collisionneur()
CATALOGUE = L.lire_json(L.CATALOGUE)
NOYAU_BRUT = L.lire_json(L.NOYAU)
NOYAU = {k: NOYAU_BRUT[k] for k in ("predicteurs_connus", "registre_lectures", "epreuves_fraiches", "sondes")}
CANARIS = NOYAU_BRUT["canaris"]
VERITE = L.lire_json(L.VERITE)
VALEUR = "0123456789abcdef" * 4
CLE_G, CLE_K = "CLE-SECRETE-GEMINI-DE-TEST-0123456789", "CLE-SECRETE-KIMI-DE-TEST-9876543210"


# --- aides ----------------------------------------------------------------------------------------------------------------

def ecrire_prereg(chemin, valeur=VALEUR, pieces=(), marqueur=False):
    lignes = ["# Préenregistrement d'essai (factice)", "",
              "- Empreinte de la valeur engagée (SHA-256 de la valeur, en ASCII) : "
              + ("<<EMPREINTE_VALEUR_ENGAGEE>>" if marqueur else f"`{tf.sha256_octets(valeur.encode('ascii'))}`"), ""]
    for s in SECTIONS:
        lignes += [f"## {s}", "", "Texte d'essai."]
        if s == "Plan d'analyse" and pieces:
            lignes += ["", "### Pièces gelées", "", "| pièce | SHA-256 |", "|---|---|"]
            lignes += [f"| `{c}` | `{h}` |" for c, h in pieces]
        if s == "Contre-lecture":
            lignes += ["brouillon " + "a" * 64 + " ; rapport " + "b" * 64]
        lignes.append("")
    Path(chemin).write_text("\n".join(lignes), encoding="utf-8")
    return sceller(chemin) if not marqueur else None


def tirer_reel(tmp, nom, valeur=VALEUR):
    prereg = tmp / f"prereg-{nom}.md"
    if not prereg.exists():
        ecrire_prereg(prereg, valeur)
    return tf.tirer(prereg=prereg, valeur=valeur, sortie=tmp / nom)


def fiche_synthetique(nom, prediction="aucune prédiction chiffrée", signe="+", genre="question", longueur=6000):
    remplissage = "Ce paragraphe développe le raisonnement de la fiche avec soin et sans aucun chiffre. "
    f = {"nom": nom, "type": genre, "enonce": "Énoncé de la fiche synthétique.",
         "loi_predictive": {"espace_instances": "épisodes de la banque banque-t05-v2", "prediction": prediction,
                            "signe": signe, "metrique": "classe du moniteur nommé dans la prédiction"},
         "perte_traduction": "La loi ne garde qu'un moniteur.", "questions_servies": ["Q3", "nouvelle"],
         "avantage": {"source": "programme", "texte": "Avantage nommé.", "incopiable_parce_que": "Raison donnée."},
         "originalite": {"niveau": "transposition", "texte": "Transposition d'une idée connue."},
         "demande_organisme": {"nature": "rien", "texte": ""}, "cout": {"nature": "processeur", "ordre_de_grandeur": "faible"},
         "piege": "Le piège méthodologique.", "cosmetique_si": "Ce qui la rendrait cosmétique.", "anteriorite": []}
    champs = ("enonce", "perte_traduction", "piege", "cosmetique_si")
    i = 0
    while tf.taille_servie(f) < longueur:
        cle = champs[i % len(champs)]
        if len(f[cle]) + len(remplissage) > 2800:
            i += 1
            if i > 40:
                break
            continue
        f[cle] += " " + remplissage
        i += 1
    return f


def reponse_spec(spec, modele, fin):
    return C.Reponse(texte="Traduction.\n```json\n" + json.dumps({"traduction": spec}, ensure_ascii=False) + "\n```\n",
                     modele_servi=modele, fin=fin, usage={"entree": 3000, "sortie": 800})


class Faux:
    """Faux appelant (modele_id, prompt, max_tokens) -> Reponse ; décide par une fonction du prompt ; compte ses appels."""

    def __init__(self, decider):
        self.decider, self.appels, self.prompts, self._v = decider, 0, [], threading.Lock()

    def __call__(self, modele_id, prompt, max_tokens):
        with self._v:
            self.appels += 1
            self.prompts.append(prompt)
        return self.decider(prompt, modele_id)


def faux_paire(decider_spec):
    """Kimi et Argon rendent la même spécification (accord), choisie par `decider_spec(prompt)`."""
    k = Faux(lambda p, m: reponse_spec(decider_spec(p), m, "stop"))
    g = Faux(lambda p, m: reponse_spec(decider_spec(p), m, "STOP"))
    return {"kimi": k, "gemini": g}, k, g


SPEC_T1 = {"sortie": "loi", "forme": "monotone_un_trait", "cible": {"banque": "banque-t05-v2", "moniteur": "8B:RIGOR"},
           "traits": ["jetons_par_action_ecart_type"], "issue_visee": 2, "sens": "+",
           "effet": {"valeur": 0.8, "source": "loi_predictive.prediction"}, "perte_traduction": "un seul moniteur"}
SPEC_T2 = {"sortie": "loi", "forme": "interaction_deux_traits", "cible": {"banque": "banque-t05-v2", "moniteur": "3B:COHERENCE"},
           "traits": ["actions_valides", "log_jetons_total"], "issue_visee": 0, "sens": "-",
           "effet": {"valeur": 0.6, "source": "loi_predictive.prediction"}, "perte_traduction": "seuil zéro"}
SPEC_T3 = {"sortie": "loi", "forme": "monotone_un_trait", "cible": {"banque": "banque-t05-v2", "moniteur": "8B:NOVELTY"},
           "traits": ["actions_valides"], "issue_visee": 1, "sens": "+",
           "effet": {"operation": "difference", "termes": [{"valeur": 0.4, "source": "loi_predictive.prediction"},
                                                           {"valeur": 0.4, "source": "loi_predictive.prediction"}],
                     "valeur": 0.0}, "perte_traduction": "écart nul"}
SPEC_COUCHE3 = {"sortie": "loi", "forme": "monotone_un_trait",
                "cible": {"banque": "banque-t05-v2", "moniteur": {"a_construire": {"source": "loi_predictive.metrique"}}},
                "traits": ["bruit"], "issue_visee": 0, "sens": "+", "effet": {"valeur": 0.8, "source": "loi_predictive.prediction"},
                "perte_traduction": "moniteur à construire"}


def renvoi(code):
    return {"sortie": "non_testable", "raison_code": code, "raison": f"renvoi {code}"}


PRED_T1 = "Au-delà du prédicteur connu, l'issue 2 de 8B:RIGOR augmente avec jetons_par_action_ecart_type : log-rapport 0,8."
PRED_T2 = "L'issue 0 de 3B:COHERENCE diminue avec actions_valides si log_jetons_total est positif : log-rapport 0,6."
PRED_T3 = "Issue 1 de 8B:NOVELTY : 0,40 au-dessus de la moyenne d'actions_valides, 0,40 en dessous, écart de 0."
PRED_F = "log-rapport de cotes 0,8 de l'issue 2 de 8B:RIGOR par unité de jetons_par_action_ecart_type"

TEMOINS_SYNTH = {
    "T1": fiche_synthetique("MARQUE-T1 dispersion et rigueur", PRED_T1, longueur=0),
    "T2": fiche_synthetique("MARQUE-T2 interaction", PRED_T2, signe="-", longueur=0),
    "T3": fiche_synthetique("MARQUE-T3 vide", PRED_T3, longueur=0),
    "T4": fiche_synthetique("MARQUE-T4 méthode", "aucune issue d'épisode n'est prédite", signe="0", genre="approche", longueur=0),
    "T5": fiche_synthetique("MARQUE-T5 théorème", "énoncé à prouver en Lean", longueur=0),
    "T6": fiche_synthetique("MARQUE-T6 sans chiffre", "augmente nettement", longueur=0),
}
FICHES_SYNTH = {f"F-{k:02d}": fiche_synthetique(f"MARQUE-F{k:02d}", PRED_F, longueur=0) for k in range(1, 9)}
DECISION = {"MARQUE-T1": SPEC_T1, "MARQUE-T2": SPEC_T2, "MARQUE-T3": SPEC_T3, "MARQUE-T4": renvoi("N1"),
            "MARQUE-T5": renvoi("N3"), "MARQUE-T6": renvoi("N2"), "MARQUE-F01": dict(SPEC_T1),
            "MARQUE-F02": SPEC_COUCHE3, "MARQUE-F03": SPEC_COUCHE3, "MARQUE-F04": SPEC_COUCHE3}


def decider_par_marque(prompt):
    for marque, spec in DECISION.items():
        if marque in prompt:
            return spec
    return renvoi("N1")


ORDRE = ["F-03", "T2", "F-01", "T5", "F-06", "F-08", "T1", "F-02", "T6", "F-04", "T3", "F-05", "T4", "F-07"]


def tour(tmp, items, appelants, **k):
    k.setdefault("pause_reprise", 0)
    return L.executer_tour(tmp / "run", items, catalogue=CATALOGUE, noyau=NOYAU, canaris=CANARIS, c=C,
                           appelants=appelants, **k)


def items_synth(ordre=ORDRE):
    return L.construire_items(ordre, FICHES_SYNTH, TEMOINS_SYNTH)


def par_source(recs):
    return {r["source"]: r for r in recs}


# --- tirage ---------------------------------------------------------------------------------------------------------------

class TestTirage:
    def test_reproductible(self, tmp_path):
        a, b = tirer_reel(tmp_path, "a"), tirer_reel(tmp_path, "b")
        assert a["ordre_de_passage"] == b["ordre_de_passage"]
        assert {k: v["sha256"] for k, v in a["fiches_tirees"].items()} == {k: v["sha256"] for k, v in b["fiches_tirees"].items()}
        assert a["graines"]["entropie"] == b["graines"]["entropie"]

    def test_autre_valeur_autre_tirage(self, tmp_path):
        a = tirer_reel(tmp_path, "a")
        autre = "f" * 64
        prereg = tmp_path / "prereg-autre.md"
        ecrire_prereg(prereg, autre)
        b = tf.tirer(prereg=prereg, valeur=autre, sortie=tmp_path / "b")
        assert (a["ordre_de_passage"], [v["identifiant_auteur"] for v in a["fiches_tirees"].values()]) != \
            (b["ordre_de_passage"], [v["identifiant_auteur"] for v in b["fiches_tirees"].values()])

    def test_eligibilite_fable_seulement(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        idents = [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]
        assert len(idents) == 8 and all(i.startswith("fable-") for i in idents)
        assert m["comptes"]["idees_auteur_eligibles"] == 8 and m["comptes"]["idees_retenues"] == 8
        assert "toutes les idées éligibles" in m["comptes"]["regle_sous_ensemble"]

    def test_dedoublonnage_une_fiche_par_idee(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        assert (m["comptes"]["fiches"], m["comptes"]["idees_distinctes"], m["comptes"]["paires_de_doublons"]) == (29, 17, 12)
        groupes = m["idees_eligibles"]
        idents = [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]
        assert sorted(next(i for i, g in enumerate(groupes) if x in g) for x in idents) == list(range(8))

    def test_ordre_mele_permutation(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        o = m["ordre_de_passage"]
        assert sorted(o) == sorted([f"F-{k:02d}" for k in range(1, 9)] + list(tf.TEMOINS))
        assert o != [f"F-{k:02d}" for k in range(1, 9)] + list(tf.TEMOINS)
        assert {o.index(t) for t in tf.TEMOINS} != set(range(8, 14))

    def test_vue_anonyme_contenu_seul_et_empreintes(self, tmp_path):
        m = tirer_reel(tmp_path, "a")
        for num, d in m["fiches_tirees"].items():
            vue = json.loads((tmp_path / "a" / d["fichier"]).read_text(encoding="utf-8"))
            assert not set(vue) & set(tf.CHAMPS_INTERNES)
            assert tf.empreinte_objet(vue) == d["empreinte_fiche_validee"]
            assert tf.verifier_compagnon(tmp_path / "a" / d["fichier"]) == d["sha256"]
            pv.garde_entree(pv.construire_entree(vue, CATALOGUE), CANARIS)  # aucune métadonnée, aucun canari
        tf.verifier_compagnon(tmp_path / "a" / tf.MANIFESTE)

    def test_refus_preregistrement_non_scelle(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        Path(str(prereg) + ".sha256").unlink()
        with pytest.raises(tf.TirageRefuse, match="non scellé"):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")
        assert not (tmp_path / "s").exists()

    def test_refus_marqueur_restant(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg, marqueur=True)
        Path(str(prereg) + ".sha256").write_text(f"{tf.sha256_fichier(prereg)}  p.md\n", encoding="utf-8")
        with pytest.raises(tf.TirageRefuse, match="marqueurs de gabarit"):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")

    def test_refus_preregistrement_modifie_apres_scellement(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with open(prereg, "a", encoding="utf-8") as f:
            f.write("\najout après scellement\n")
        with pytest.raises(tf.TirageRefuse):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")

    def test_refus_valeur_non_engagee(self, tmp_path):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with pytest.raises(tf.TirageRefuse, match="empreinte engagée"):
            tf.tirer(prereg=prereg, valeur="e" * 64, sortie=tmp_path / "s")

    def test_refus_sortie_existante(self, tmp_path):
        (tmp_path / "s").mkdir()
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with pytest.raises(tf.TirageRefuse, match="R12"):
            tf.tirer(prereg=prereg, valeur=VALEUR, sortie=tmp_path / "s")

    def test_plus_de_dix_idees_dix_tirees(self, tmp_path):
        fiches, lignes, note = [], [], ["| Rang | Fiche gardée | Total | Éligible | Doublon(s) |", "|---|---|---|---|---|"]
        rang = 0
        for k in range(1, 14):
            for p in (1, 2):
                vue = {"nom": f"idée {k}", "enonce": f"énoncé {k}-{p}"}
                ident = f"fable-p{p}-{k:02d}"
                fiches.append(dict(vue, auteur="fable", identifiant_auteur=ident, passe=p, empreinte=tf.empreinte_objet(vue)))
                lignes.append({"identifiant_auteur": ident, "empreinte": fiches[-1]["empreinte"], "eligible": k != 13})
            rang += 1
            note.append(f"| {rang} | fable-p1-{k:02d} (rang {rang}) — idée {k} | 10 | {'oui' if k != 13 else 'non'} | "
                        f"fable-p2-{k:02d} (rang {rang + 20}) |")
        vue = {"nom": "idée argon", "enonce": "e"}
        fiches.append(dict(vue, auteur="argon", identifiant_auteur="argon-p1-01", passe=1, empreinte=tf.empreinte_objet(vue)))
        lignes.append({"identifiant_auteur": "argon-p1-01", "empreinte": fiches[-1]["empreinte"], "eligible": True})
        note.append("| 14 | argon-p1-01 (rang 30) — idée argon | 10 | oui | — |")
        (tmp_path / "f.json").write_text(json.dumps(fiches), encoding="utf-8")
        (tmp_path / "c.json").write_text(json.dumps({"lignes": lignes}), encoding="utf-8")
        (tmp_path / "n.md").write_text("\n".join(note), encoding="utf-8")
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        m = tf.tirer(prereg=prereg, valeur=VALEUR, fiches=tmp_path / "f.json", classement=tmp_path / "c.json",
                     doublons=tmp_path / "n.md", sortie=tmp_path / "s")
        idents = [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]
        assert len(idents) == 10 and len({i[-2:] for i in idents}) == 10
        assert all(i.startswith("fable-") and not i.endswith("-13") for i in idents)
        assert m["comptes"]["idees_auteur_eligibles"] == 12 and "10 idées tirées sans remise parmi 12" in \
            m["comptes"]["regle_sous_ensemble"]

    def test_entropie_porte_la_valeur_engagee(self, tmp_path, monkeypatch):
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        tirages = []
        for k, valeur in enumerate(("1" * 64, "2" * 64)):
            monkeypatch.setattr(tf, "empreinte_valeur_engagee",
                                lambda texte, v=valeur: tf.sha256_octets(v.encode("ascii")))
            m = tf.tirer(prereg=prereg, valeur=valeur, sortie=tmp_path / f"s{k}")
            assert m["graines"]["entropie"] == [tf.sha256_fichier(prereg), valeur]
            tirages.append((m["ordre_de_passage"], [v["identifiant_auteur"] for v in m["fiches_tirees"].values()]))
        assert tirages[0] != tirages[1]  # même préenregistrement, autre valeur : autre tirage

    def test_garde_a4_au_tirage(self, tmp_path):
        fiches, lignes = [], []
        note = ["| Rang | Fiche gardée | Total | Éligible | Doublon(s) |", "|---|---|---|---|---|"]
        for k in (1, 2):
            vue = {"nom": f"idée {k}", "enonce": "reprend fable-p2-02 mot pour mot" if k == 2 else "énoncé"}
            ident = f"fable-p1-{k:02d}"
            fiches.append(dict(vue, auteur="fable", identifiant_auteur=ident, passe=1, empreinte=tf.empreinte_objet(vue)))
            lignes.append({"identifiant_auteur": ident, "empreinte": fiches[-1]["empreinte"], "eligible": True})
            note.append(f"| {k} | {ident} (rang {k}) — idée {k} | 10 | oui | — |")
        (tmp_path / "f.json").write_text(json.dumps(fiches), encoding="utf-8")
        (tmp_path / "c.json").write_text(json.dumps({"lignes": lignes}), encoding="utf-8")
        (tmp_path / "n.md").write_text("\n".join(note), encoding="utf-8")
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg)
        with pytest.raises(tf.EtiquetteInterdite):
            tf.tirer(prereg=prereg, valeur=VALEUR, fiches=tmp_path / "f.json", classement=tmp_path / "c.json",
                     doublons=tmp_path / "n.md", sortie=tmp_path / "s")
        assert not (tmp_path / "s").exists()  # aucune copie partielle

    def test_note_et_classement_discordants(self, tmp_path):
        fiches = json.loads(tf.FICHES.read_text(encoding="utf-8"))
        classement = json.loads(tf.CLASSEMENT.read_text(encoding="utf-8"))
        for l in classement["lignes"]:
            if l["identifiant_auteur"] == "fable-p2-03":
                l["eligible"] = False
        with pytest.raises(tf.TirageRefuse, match="éligibilité de la note"):
            tf.idees_eligibles(fiches, classement, tf.DOUBLONS.read_text(encoding="utf-8"))


class TestGardeA4:
    def test_sain_temoins_plantes_permis(self):
        assert tf.garde_a4({"nom": "Les témoins plantés comme processus surveillé"}, "essai")

    @pytest.mark.parametrize("texte", ["reprise de fable-p1-01", "Argon P2 a écrit", "un témoin du pont", "Metteur-en-forme",
                                       "fiche FABRIQUÉE", "spécification connue"])
    def test_artefacts(self, texte):
        with pytest.raises(tf.EtiquetteInterdite):
            tf.garde_a4({"enonce": texte}, "essai")

    @v56
    def test_miroir_de_fiches_v54(self):
        sys.path.insert(0, POLE)
        from pole import fiches_v54
        for texte in ("reprise de fable-p1-01", "rien", "Témoins du pont, encore", "fable p10"):
            assert tf.etiquettes_trouvees(texte) == fiches_v54.trouver(texte, tf.ETIQUETTES_A4, "mot_entier")


# --- lanceur : tour complet et agrégat ---------------------------------------------------------------------------------------

class TestTour:
    def test_tour_complet_agrege(self, tmp_path):
        appelants, k, g = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants)
        assert etat.motif is None and all(r["statut"] == "traite" for r in recs)
        assert (k.appels, g.appels) == (14, 14)
        a = L.agreger(par_source(recs), VERITE, depense_usd=budget.depense, motifs_arret=[etat.motif])
        assert a["classes_fiches"] == {"sortie_1_differee": 1, "sortie_2": 3, "sortie_3": 4}
        assert a["accord"] == {"accords": 4, "fiches_traduites": 4, "taux": 1.0}
        assert a["temoins_justes"] == 6
        assert a["criteres_mecaniques"] == {"L1_dents": "dents", "L2_fidelite": "fidélité", "L3_utilite": "utile",
                                            "L4_surete": "sûr", "L5_defauts": "conforme"}
        assert all(p["tenue"] for p in a["predictions"].values())
        assert a["audit_symetrie"]["entrees_distinctes"] == 14 and not a["audit_symetrie"]["declenche"]
        assert 0 < budget.depense <= L.PLAFOND_USD

    def test_temoin_faux_et_pas_de_dents(self, tmp_path):
        decision = dict(DECISION, **{"MARQUE-T1": dict(SPEC_T1, issue_visee=1)})  # mauvaise issue : T1 non retrouvé
        appelants, _, _ = faux_paire(lambda p: next((s for m, s in decision.items() if m in p), renvoi("N1")))
        recs, etat, budget = tour(tmp_path, items_synth(), appelants)
        a = L.agreger(par_source(recs), VERITE, depense_usd=budget.depense, motifs_arret=[])
        assert a["temoins"]["T1"]["juste"] is False and a["temoins_justes"] == 5
        assert a["criteres_mecaniques"]["L1_dents"] == "pas de dents"

    def test_desaccord_n8_et_ambiguite(self, tmp_path):
        k = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(dict(decider_par_marque(p), sens="-") if "MARQUE-F0" in p and
                                           decider_par_marque(p).get("sortie") == "loi" else decider_par_marque(p), m, "STOP"))
        recs, etat, budget = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        a = L.agreger(par_source(recs), VERITE, depense_usd=budget.depense, motifs_arret=[])
        assert a["accord"]["accords"] == 0 and a["accord"]["fiches_traduites"] == 4
        assert a["criteres_mecaniques"]["L2_fidelite"] == "ambiguïté élevée"
        assert a["renvois_par_code"].get("N8") == 4 and a["criteres_mecaniques"]["L5_defauts"] == "consigne à revoir"

    @pytest.mark.parametrize("effet,juste", [(0.8, True), (1.5, True), (0.41, True), (2.0, False), (0.39, False)])
    def test_signature_retrouvee_tolerance_d_effet(self, effet, juste):
        v = VERITE["T1"]["signature"]
        sig = {"genre": "instances", "forme": v["forme"], "banque": ("existant", v["banque"]),
               "moniteur": ("existant", v["moniteur"]), "traits": [("existant", x) for x in v["traits"]],
               "issue_visee": v["issue_visee"], "sens": v["sens"], "effet": effet, "sous_population_visee": None}
        assert L.signature_retrouvee(sig, v) is juste
        assert L.signature_retrouvee(dict(sig, sens="-"), v) is False

    def test_ordre_de_passage_respecte(self, tmp_path):
        appelants, k, _ = faux_paire(decider_par_marque)
        items = items_synth()
        assert [it["source"] for it in items] == ORDRE and [it["item"] for it in items][:2] == ["item-01", "item-02"]
        assert [it["nature"] for it in items].count("temoin") == 6
        tour(tmp_path, items, appelants)
        for it, prompt in zip(items, k.prompts):
            assert json.dumps(it["fiche"], ensure_ascii=False, indent=1, sort_keys=True) in prompt

    def test_parallele_meme_resultat(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, etat, _ = tour(tmp_path, items_synth(), appelants, parallele=3)
        assert [r["source"] for r in recs] == ORDRE and all(r["statut"] == "traite" for r in recs)

    def test_sorties_sur_disque_scellees(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        tour(tmp_path, items_synth(), appelants)
        d = tmp_path / "run" / "items" / "item-01"
        for nom in ("prompt.txt", "traducteur.essai1.reponse.txt", "traducteur.essai1.meta.json",
                    "contre_traducteur.essai1.reponse.txt", "resultat.json"):
            tf.verifier_compagnon(d / nom)
        rec = L.lire_json(d / "resultat.json")
        assert rec["resultat"]["familles"] == {"auteur": "anthropic", "traducteur": "moonshot", "contre_traducteur": "google"}

    @v56
    def test_garde_reelle_v56_sur_la_loi_compilee(self, tmp_path):
        _, proposeur = L.charger_v56(POLE)
        garde = L.fabriquer_garde_reelle(proposeur, CATALOGUE)
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, _, _ = tour(tmp_path, items_synth(), appelants, garde_reelle=garde)
        r = par_source(recs)
        assert r["T1"]["garde_reelle_v56"] == "acceptée" and r["T2"]["garde_reelle_v56"] == "acceptée"
        assert r["F-02"]["garde_reelle_v56"] == "sans objet"


class TestPlafond:
    def test_artefact_plafond_jamais_depasse(self, tmp_path):
        appelants, k, g = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=0.5)
        assert budget.depense <= 0.5 and etat.motif.startswith("plafond")
        assert g.appels == 0 and k.appels == 1  # pire cas d'Argon (≈ 0,61 USD) > reste : aucun appel d'Argon
        s = par_source(recs)
        assert s[ORDRE[0]]["statut"] == "interrompu_plafond"
        assert all(s[x]["statut"] == "non_lance" for x in ORDRE[1:])

    def test_sain_plafond_large(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=5.0)
        assert etat.motif is None and budget.depense <= 5.0

    def test_plafond_cumule_avec_depense_initiale(self, tmp_path):
        appelants, k, _ = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=5.0, depense_initiale=4.9)
        assert k.appels == 0 and etat.motif.startswith("plafond") and budget.depense == pytest.approx(4.9)

    def test_parallele_ne_depasse_pas(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, etat, budget = tour(tmp_path, items_synth(), appelants, plafond=1.2, parallele=4)
        assert budget.depense <= 1.2 + 1e-9 and etat.motif.startswith("plafond")

    def test_echec_compte_au_pire_cas(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(echec="connexion : délai dépassé"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, budget = tour(tmp_path, items_synth()[:1], {"kimi": k, "gemini": g})
        pire = C.cout_pire_cas(L.MODELES["traducteur"]["prix"], len(k.prompts[0]), L.MODELES["traducteur"]["max_tokens"])
        assert recs[0]["statut"] == "echec_technique" and k.appels == 2
        assert budget.depense == pytest.approx(2 * pire)


class TestRefus:
    def test_refus_du_traducteur_arrete_la_fiche(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="content_filter", categorie="content_filter",
                                        usage={"entree": 3000, "sortie": 0}) if "MARQUE-T3" in p
                 else reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        t3 = par_source(recs)["T3"]
        assert t3["refus"] == {"traducteur": "content_filter"} and t3["resultat"]["renvoi"]["code"] == "N10"
        assert t3["appels"] == 1 and etat.refus == 1 and etat.motif is None
        assert g.appels == 13  # le contre-traducteur n'est pas appelé sur la fiche refusée

    def test_refus_du_contre_traducteur_n8(self, tmp_path):
        k = Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "stop"))
        g = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="SAFETY", usage={"entree": 3000, "sortie": 0})
                 if "MARQUE-T1" in p else reponse_spec(decider_par_marque(p), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        t1 = par_source(recs)["T1"]
        assert t1["refus"] == {"contre_traducteur": "SAFETY"} and t1["resultat"]["renvoi"]["code"] == "N8"

    def test_trois_refus_arretent_le_tour(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(texte="", modele_servi=m, fin="content_filter", categorie="content_filter",
                                        usage={"entree": 3000, "sortie": 0}))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert etat.refus == 3 and etat.motif.startswith("refus")
        assert [r["statut"] for r in recs[:3]] == ["traite"] * 3 and all(r["statut"] == "non_lance" for r in recs[3:])
        assert k.appels == 3 and g.appels == 0

    def test_preparer_reprise(self, tmp_path):
        prec = tmp_path / "prec"
        prec.mkdir()
        fin = {"mode": "principal", "motif_arret": "refus : 3 refus, arrêt du tour (liste d'arrêt)", "depense_usd": 1.25,
               "enregistrements": [{"source": "T3", "statut": "traite", "refus": {"traducteur": "content_filter"}},
                                   {"source": "F-01", "statut": "traite", "refus": {}},
                                   {"source": "F-02", "statut": "non_lance"}]}
        tf.ecrire_json_neuf(prec / "manifeste-run-fin.json", fin)
        pre = tmp_path / "preambule.md"
        pre.write_text("Tâche de traduction statistique, vocabulaire défini ci-dessous.", encoding="utf-8")
        sceller(pre)
        items, preambule, dep = L.preparer_reprise(prec, items_synth(), pre, CANARIS)
        assert sorted(it["source"] for it in items) == ["F-02", "T3"] and dep == pytest.approx(1.25) and preambule
        L.marquer_reprise(prec, tmp_path / "rep")
        with pytest.raises(L.LancementRefuse, match="une seule reformulation"):
            L.preparer_reprise(prec, items_synth(), pre, CANARIS)
        with pytest.raises(L.LancementRefuse, match="déjà eu lieu"):
            L.marquer_reprise(prec, tmp_path / "rep2")

    @pytest.mark.parametrize("modif,motif", [({"mode": "reprise"}, "run principal"),
                                             ({"motif_arret": "plafond : …"}, "autre cause"),
                                             ({"enregistrements": [{"source": "T3", "statut": "traite", "refus": {}}]},
                                              "aucun refus")])
    def test_reprise_refusee(self, tmp_path, modif, motif):
        prec = tmp_path / "prec"
        prec.mkdir()
        fin = dict({"mode": "principal", "motif_arret": None, "depense_usd": 1.0,
                    "enregistrements": [{"source": "T3", "statut": "traite", "refus": {"traducteur": "x"}}]}, **modif)
        tf.ecrire_json_neuf(prec / "manifeste-run-fin.json", fin)
        pre = tmp_path / "pre.md"
        pre.write_text("Préambule technique.", encoding="utf-8")
        sceller(pre)
        with pytest.raises(L.LancementRefuse, match=motif):
            L.preparer_reprise(prec, items_synth(), pre, CANARIS)

    @pytest.mark.parametrize("texte", ["Préambule : un témoin du pont.", "Préambule " + CANARIS[0], "   "])
    def test_preambule_refuse(self, tmp_path, texte):
        prec = tmp_path / "prec"
        prec.mkdir()
        tf.ecrire_json_neuf(prec / "manifeste-run-fin.json", {"mode": "principal", "motif_arret": None, "depense_usd": 0.5,
                                                               "enregistrements": [{"source": "T3", "statut": "traite",
                                                                                    "refus": {"traducteur": "x"}}]})
        pre = tmp_path / "pre.md"
        pre.write_text(texte, encoding="utf-8")
        sceller(pre)
        with pytest.raises((L.LancementRefuse, tf.EtiquetteInterdite)):
            L.preparer_reprise(prec, items_synth(), pre, CANARIS)

    def test_preambule_applique_aux_deux_roles(self, tmp_path):
        appelants, k, g = faux_paire(decider_par_marque)
        tour(tmp_path, items_synth()[:2], appelants, preambule="PRÉAMBULE TECHNIQUE")
        assert all(p.startswith("PRÉAMBULE TECHNIQUE\n\n") for p in k.prompts + g.prompts)


class TestArrets:
    def test_lecture_epreuve_interdite_arrete_tout(self, tmp_path):
        items = items_synth()
        items[0] = dict(items[0], fiche=dict(items[0]["fiche"], enonce="voir " + CANARIS[0]))
        appelants, k, g = faux_paire(decider_par_marque)
        recs, etat, _ = tour(tmp_path, items, appelants)
        assert recs[0]["statut"] == "arret_lecture_epreuve" and "LectureEpreuveInterdite" in etat.motif
        assert (k.appels, g.appels) == (0, 0) and all(r["statut"] == "non_lance" for r in recs[1:])
        a = L.agreger(par_source(recs), VERITE, depense_usd=0.0, motifs_arret=[etat.motif])
        assert a["criteres_mecaniques"]["L4_surete"] == "incident"

    def test_sain_aucun_canari(self, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        recs, etat, _ = tour(tmp_path, items_synth()[:1], appelants)
        assert recs[0]["statut"] == "traite" and etat.motif is None

    def test_canari_dans_la_reponse_arrete(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(texte=CANARIS[1] + "\n" + reponse_spec(renvoi("N1"), m, "stop").texte,
                                        modele_servi=m, fin="stop", usage={"entree": 10, "sortie": 10}))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert recs[0]["resultat"]["incident"] and etat.motif.startswith("canari")
        assert all(r["statut"] == "non_lance" for r in recs[1:])

    def test_erreur_du_module_arrete(self, tmp_path, monkeypatch):
        def casse(*a, **k):
            raise RuntimeError("panne simulée")
        monkeypatch.setattr(pv, "compiler", casse)
        appelants, _, _ = faux_paire(lambda p: SPEC_T1)
        recs, etat, _ = tour(tmp_path, items_synth(), appelants)
        assert recs[0]["statut"] == "erreur_module" and etat.motif.startswith("erreur du module")
        assert all(r["statut"] == "non_lance" for r in recs[1:])

    def test_modele_servi_different_arrete(self, tmp_path):
        k = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "stop"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), "gemini-3-pro", "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert recs[0]["statut"] == "interrompu" and "modèle servi différent" in etat.motif
        assert (tmp_path / "run" / "items" / "item-01" / "contre_traducteur.essai1.reponse.txt").is_file()

    def test_echec_de_transport_une_reprise(self, tmp_path):
        etat_k = {"n": 0}

        def k_decide(p, m):
            etat_k["n"] += 1
            return C.Reponse(echec="connexion : réinitialisée") if etat_k["n"] == 1 else reponse_spec(renvoi("N1"), m, "stop")
        k, g = Faux(k_decide), Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth()[:1], {"kimi": k, "gemini": g})
        assert recs[0]["statut"] == "traite" and k.appels == 2
        journal = (tmp_path / "run" / "journal.jsonl").read_text(encoding="utf-8")
        assert "reprise_a_l_identique" in journal

    def test_trois_echecs_techniques_arretent(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(echec="HTTP 503 : indisponible"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert etat.echecs == 3 and etat.motif.startswith("échecs techniques")
        assert all(r["statut"] == "non_lance" for r in recs[3:])

    def test_borne_du_relais_arrete_sans_reprise(self, tmp_path):
        k = Faux(lambda p, m: C.Reponse(echec="HTTP 402 : plafond de dépense du relais atteint"))
        g = Faux(lambda p, m: reponse_spec(renvoi("N1"), m, "STOP"))
        recs, etat, _ = tour(tmp_path, items_synth(), {"kimi": k, "gemini": g})
        assert k.appels == 1 and "borne du relais" in etat.motif


class TestCles:
    def test_aucune_cle_dans_les_sorties(self, tmp_path, monkeypatch):
        monkeypatch.setenv("GEMINI_API_KEY", CLE_G)
        monkeypatch.setenv("KIMI_API_KEY", CLE_K)
        appelants, _, _ = faux_paire(decider_par_marque)
        tour(tmp_path, items_synth(), appelants)
        env = {"GEMINI_API_KEY": CLE_G, "KIMI_API_KEY": CLE_K}
        assert L.chercher_cles(tmp_path / "run", env) == []
        (tmp_path / "run" / "fuite.txt").write_text("…" + CLE_G + "…", encoding="utf-8")  # artefact : la garde le voit
        assert L.chercher_cles(tmp_path / "run", env) == ["GEMINI_API_KEY"]


# --- gardes de lancement -----------------------------------------------------------------------------------------------------

class TestGardesDeLancement:
    def test_go_sain(self):
        assert L.verifier_go("GO-2026-11-01-09", aujourd_hui="2026-11-03")[2] == "calcul"

    @pytest.mark.parametrize("go,jour", [("GO-2026-11-01-08", "2026-11-03"), ("GO-2026-11-01-09", "2026-11-09"),
                                         ("GO-2026-11-01-09", "2026-10-31")])
    def test_go_artefacts(self, go, jour):
        with pytest.raises(L.LancementRefuse):
            L.verifier_go(go, aujourd_hui=jour)

    @pytest.mark.parametrize("ligne", [
        "| GO-2026-11-01-09 | 2026-11-01 | décision | x | 5 USD | 2026-11-08 | Lazar | r |",
        "| GO-2026-11-01-09 | 2026-11-01 | calcul | x | 3 USD | 2026-11-08 | Lazar | r |",
        "| GO-2026-11-01-09 | 2026-11-01 | calcul | x | 5 USD | 2026-11-08 | Lazar | r |\n"
        "| GO-2026-11-02-01 | 2026-11-02 | révocation | révoque GO-2026-11-01-09 | — | 2026-11-02 | Lazar | r |"])
    def test_go_registre_artefacts(self, tmp_path, ligne):
        reg = tmp_path / "go.md"
        reg.write_text("| id | a | t | p | pl | e | par | ref |\n|---|---|---|---|---|---|---|---|\n" + ligne + "\n", encoding="utf-8")
        with pytest.raises(L.LancementRefuse):
            L.verifier_go("GO-2026-11-01-09", registre=reg, aujourd_hui="2026-11-03")

    def test_pieces_gelees_saines_puis_modifiees(self, tmp_path):
        (tmp_path / "a.txt").write_text("pièce", encoding="utf-8")
        prereg = tmp_path / "p.md"
        ecrire_prereg(prereg, pieces=[("a.txt", tf.sha256_fichier(tmp_path / "a.txt"))])
        sha, pieces = L.verifier_pieces(prereg, tmp_path)
        assert len(sha) == 64 and pieces[0]["chemin"] == "a.txt"
        (tmp_path / "a.txt").write_text("pièce modifiée", encoding="utf-8")
        with pytest.raises(L.LancementRefuse, match="modifiée"):
            L.verifier_pieces(prereg, tmp_path)
        (tmp_path / "a.txt").unlink()
        with pytest.raises(L.LancementRefuse, match="absente"):
            L.verifier_pieces(prereg, tmp_path)

    def test_catalogue_avec_cle_d_epreuve_refuse(self, tmp_path):
        cat = json.loads(json.dumps(CATALOGUE))
        cat["banques"]["banque-t05-v2"]["issues"] = [0, 1]
        (tmp_path / "c.json").write_text(json.dumps(cat), encoding="utf-8")
        sceller(tmp_path / "c.json")
        shutil.copy(L.NOYAU, tmp_path / "n.json")
        sceller(tmp_path / "n.json")
        with pytest.raises(pv.LectureEpreuveInterdite):
            L.charger_catalogue_noyau(tmp_path / "c.json", tmp_path / "n.json")


def valider_factice(brut, auteur, indice, passe=1):
    """Faux validateur (forme seule) ; le vrai (`ideation_v2.valider_fiche_ideation`) est joué au groupe v56."""
    if set(brut) != set(L.CHAMPS_GABARIT):
        raise ValueError("champs hors gabarit")
    return dict(brut, auteur=auteur, passe=passe, identifiant_auteur=f"{auteur}-p{passe}-{indice:02d}", empreinte="0" * 64)


def ecrire_temoins(dossier, **remplacer):
    dossier.mkdir(parents=True, exist_ok=True)
    for t in tf.TEMOINS:
        f = remplacer.get(t) or fiche_synthetique(f"MARQUE-{t} idée", {"T1": PRED_T1, "T2": PRED_T2, "T3": PRED_T3}.get(t,
                                                  "aucune prédiction chiffrée"), longueur=6000)
        (dossier / f"{t}.json").write_text(json.dumps(f, ensure_ascii=False), encoding="utf-8")


class TestTemoins:
    def test_sain(self, tmp_path):
        ecrire_temoins(tmp_path / "t")
        temoins, emp = L.charger_temoins(tmp_path / "t", valider=valider_factice, canaris=CANARIS)
        assert sorted(temoins) == list(tf.TEMOINS) and not set(temoins["T1"]) & set(tf.CHAMPS_INTERNES)
        assert all(L.LONGUEUR_SERVIE[0] <= e["taille_servie"] <= L.LONGUEUR_SERVIE[1] for e in emp.values())

    def test_sans_validateur_refus(self, tmp_path):
        ecrire_temoins(tmp_path / "t")
        with pytest.raises(L.LancementRefuse, match="aucun repli"):
            L.charger_temoins(tmp_path / "t", valider=None)

    @pytest.mark.parametrize("cas", ["court", "etiquette", "cle_en_trop", "canari", "absent"])
    def test_artefacts(self, tmp_path, cas):
        f = fiche_synthetique("MARQUE-T4 idée", longueur=6000)
        if cas == "court":
            f = fiche_synthetique("MARQUE-T4 idée", longueur=0)
        elif cas == "etiquette":
            f["piege"] += " Écrit par le metteur en forme."
        elif cas == "cle_en_trop":
            f["temoin"] = True
        elif cas == "canari":
            f["piege"] += " Voir " + CANARIS[2] + "."
        ecrire_temoins(tmp_path / "t", T4=f)
        if cas == "absent":
            (tmp_path / "t" / "T6.json").unlink()
        with pytest.raises((L.LancementRefuse, tf.TirageRefuse)):
            L.charger_temoins(tmp_path / "t", valider=valider_factice, canaris=CANARIS)

    @v56
    def test_vrai_validateur_v56(self, tmp_path):
        ideation_v2, _ = L.charger_v56(POLE)
        ecrire_temoins(tmp_path / "t")
        temoins, _ = L.charger_temoins(tmp_path / "t", valider=ideation_v2.valider_fiche_ideation, canaris=CANARIS)
        assert len(temoins) == 6
        mauvais = fiche_synthetique("MARQUE-T5 idée", longueur=6000)
        mauvais["type"] = "theoreme"
        ecrire_temoins(tmp_path / "u", T5=mauvais)
        with pytest.raises(L.LancementRefuse, match="validateur"):
            L.charger_temoins(tmp_path / "u", valider=ideation_v2.valider_fiche_ideation, canaris=CANARIS)


# --- bout en bout : lancer() avec toutes ses gardes, faux appelants, vrai code v56 --------------------------------------------

@v56
class TestBoutEnBout:
    @pytest.fixture
    def monde(self, tmp_path, monkeypatch):
        depot = tmp_path / "depot"
        dossier = depot / "epreuve"
        dossier.mkdir(parents=True)
        for src, nom in ((L.CATALOGUE, "catalogue.json"), (L.NOYAU, "noyau.json"), (L.VERITE, "verite.json")):
            shutil.copy(src, dossier / nom)
            sceller(dossier / nom)
        pieces = [(f"epreuve/{n}", tf.sha256_fichier(dossier / n)) for n in ("catalogue.json", "noyau.json", "verite.json")]
        prereg = dossier / "prereg.md"
        ecrire_prereg(prereg, VALEUR, pieces=pieces)
        tf.tirer(prereg=prereg, valeur=VALEUR, sortie=dossier / "fiches-tirees")
        ecrire_temoins(dossier / "temoins")
        for nom, val in (("DEPOT", depot), ("PREREG", prereg), ("CATALOGUE", dossier / "catalogue.json"),
                         ("NOYAU", dossier / "noyau.json"), ("VERITE", dossier / "verite.json"),
                         ("TIREES", dossier / "fiches-tirees"), ("TEMOINS_DOSSIER", dossier / "temoins")):
            monkeypatch.setattr(L, nom, val)
        monkeypatch.setattr(L, "verifier_go", lambda go_id, **k: [go_id] if go_id == L.GO_ATTENDU else
                            (_ for _ in ()).throw(L.LancementRefuse("GO")))
        return dossier

    def args(self, sortie, **k):
        return argparse.Namespace(pole_v56=POLE, sortie=str(sortie), parallele=2, **k)

    def test_lancer_puis_reprendre_un_refus(self, monde, tmp_path):
        env = {"GO_ID": "GO-2026-11-01-09", "GEMINI_API_KEY": CLE_G}

        def kimi(p, m):
            if "MARQUE-T4" in p and "PRÉAMBULE" not in p:
                return C.Reponse(texte="", modele_servi=m, fin="content_filter", categorie="content_filter",
                                 usage={"entree": 3000, "sortie": 0})
            return reponse_spec(decider_par_marque(p), m, "stop")
        appelants = {"kimi": Faux(kimi), "gemini": Faux(lambda p, m: reponse_spec(decider_par_marque(p), m, "STOP"))}
        code, a = L.lancer(self.args(tmp_path / "run1"), appelants=appelants, c=C, environnement=env)
        assert code == 0 and a["cles_trouvees_dans_les_sorties"] == []
        assert a["fiches_traitees"] == 8 and a["temoins_traites"] == 6 and a["refus"] == 1
        assert a["temoins"]["T4"]["juste"] is False and a["temoins"]["T1"]["juste"] is True
        assert a["garde_reelle_v56"]["T1"] == "acceptée"
        for nom in ("manifeste-run.json", "manifeste-run-fin.json", "agregat-v1.json", "journal.jsonl"):
            tf.verifier_compagnon(tmp_path / "run1" / nom)
        with pytest.raises(L.LancementRefuse, match="R12"):
            L.lancer(self.args(tmp_path / "run1"), appelants=appelants, c=C, environnement=env)
        pre = monde / "preambule.md"
        pre.write_text("PRÉAMBULE : tâche de traduction statistique, vocabulaire défini.", encoding="utf-8")
        sceller(pre)
        code, b = L.lancer(self.args(tmp_path / "run2", run_precedent=str(tmp_path / "run1"), preambule=str(pre)),
                           reprise=True, appelants=appelants, c=C, environnement=env)
        assert code == 0 and b["reformules"] == ["T4"] and b["temoins"]["T4"]["juste"] is True and b["temoins_justes"] == 6
        assert b["depense_usd"] > a["depense_usd"]
        with pytest.raises(L.LancementRefuse, match="une seule reformulation"):
            L.lancer(self.args(tmp_path / "run3", run_precedent=str(tmp_path / "run1"), preambule=str(pre)),
                     reprise=True, appelants=appelants, c=C, environnement=env)

    def test_refus_sans_go(self, monde, tmp_path):
        with pytest.raises(L.LancementRefuse):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-08"})
        assert not (tmp_path / "r").exists()

    def test_refus_sans_temoins(self, monde, tmp_path):
        shutil.rmtree(monde / "temoins")
        with pytest.raises(L.LancementRefuse, match="témoin absent"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_refus_sans_fiches_tirees(self, monde, tmp_path):
        shutil.rmtree(monde / "fiches-tirees")
        with pytest.raises(L.LancementRefuse, match="fiches tirées absentes"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_refus_preregistrement_non_scelle(self, monde, tmp_path):
        Path(str(L.PREREG) + ".sha256").unlink()
        with pytest.raises(tf.TirageRefuse, match="non scellé"):
            L.lancer(self.args(tmp_path / "r"), appelants={}, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})

    def test_agreger_un_run_interrompu(self, monde, tmp_path):
        appelants, _, _ = faux_paire(decider_par_marque)
        L.lancer(self.args(tmp_path / "run1"), appelants=appelants, c=C, environnement={"GO_ID": "GO-2026-11-01-09"})
        fin = L.lire_fin(tmp_path / "run1")
        assert fin["mode"] == "principal" and not fin.get("reconstruit")
        (tmp_path / "run1" / "manifeste-run-fin.json").rename(tmp_path / "run1" / "fin-mise-de-cote.json")
        f2 = L.lire_fin(tmp_path / "run1")
        assert f2["reconstruit"] and f2["depense_usd"] == pytest.approx(fin["depense_usd"], abs=1e-5)
