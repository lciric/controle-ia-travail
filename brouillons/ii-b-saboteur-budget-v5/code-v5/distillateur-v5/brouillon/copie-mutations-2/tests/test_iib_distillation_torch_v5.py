"""Distillateur de l'organisme retenu, v5 : le moteur du mode réel (`MoteurTorch`) sur un petit Llama à poids aléatoires.

**Écrit sans avoir pu être joué par son auteur** : torch est absent du poste du développeur ; ce fichier se saute alors de
lui-même. Sur une machine qui a torch (l'instance de la course, ou tout poste à processeur), il joue la chaîne entière du
distillateur avec les vraies opérations sur les poids (injection, simple précision, entraînement, sauvegarde en demi-précision
rechargée, contrôle d'identité, doses), sur les épisodes du monde jouet. Il ne mesure rien.
"""
import json

import pytest

torch = pytest.importorskip("torch")
pytest.importorskip("transformers")
pytest.importorskip("scipy")

from iib_distillation_v5_outils import MOTIFS, config_de_course, episodes_du_maitre  # noqa: E402

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.iib import configuration_distillation_v5 as cd  # noqa: E402
from controle_ia.iib import distillation_v5 as dv  # noqa: E402
from controle_ia.iib import jumeau_v5 as jm  # noqa: E402
from controle_ia.iib import lanceur_v5 as la  # noqa: E402
from controle_ia.iib import modele_v1 as mv  # noqa: E402
from controle_ia.iib import regenere_v5 as rg  # noqa: E402
from controle_ia.iib.jouet_distillation_v5 import ModeleJouetEleve  # noqa: E402
from controle_ia.iib.jouet_v5 import EnvironnementJouet  # noqa: E402
from controle_ia.organismes import lora as lo  # noqa: E402
from controle_ia.organismes.distillation import IGNORE  # noqa: E402
from controle_ia.scellement import verifier  # noqa: E402
from controle_ia.t06 import distillation_transcription as dt  # noqa: E402

VOCABULAIRE = 512


class ModeleHybride(ModeleJouetEleve):
    """Le texte des actions vient du modèle jouet de langue ; les poids, les adaptateurs et la dose sont ceux d'un petit Llama."""

    pad = 0

    def __init__(self):
        super().__init__()
        self.torch = mv.petit_llama(5, VOCABULAIRE)

    @property
    def dose(self):
        t = self.__dict__.get("torch")
        doses = {float(x.dose) for x in lo.modules_lora(t).values()} if t is not None else set()
        if len(doses) > 1:
            raise GardeArret(f"doses mêlées {sorted(doses)}")
        return doses.pop() if doses else 0.0

    @dose.setter
    def dose(self, valeur):
        pass                                                   # la dose vit sur les modules d'adaptation, jamais ici

    def charger_adaptateur(self, nom, etat):
        lo.charger_etat(self.torch, etat)
        self.adaptateur_charge = nom


def test_constante_d_etiquette_et_transcription_egales_au_code_de_l_organisme_ii():
    assert dv.IGNORE == IGNORE
    m, g = ModeleJouetEleve(), jm.Graines(7)
    ep = rg.jouer_lot(m, [EnvironnementJouet("t1")], ["t1/e0"], [g.entiers("a", 10)], 400, 1.0)[0]
    actions = [a["ids"] for a in ep["actions"]]
    assert dv.transcription(m.fmt, EnvironnementJouet("t1"), actions) == dt.transcription_honnete(m.fmt, EnvironnementJouet("t1"), actions)
    ids, empans = dv.transcription(m.fmt, EnvironnementJouet("t1"), actions)
    for garder in ([0, 3, 9], list(range(10)), [5]):
        assert dv.exemple(ids, empans, garder) == dt.exemple_de_transcription(ids, empans, garder)


def test_chaine_entiere_avec_le_moteur_reel_sur_un_petit_llama(tmp_path):
    modele, monde = ModeleHybride(), la.MondeJouet()
    config = config_de_course(tmp_path, "P")
    x = episodes_du_maitre(modele, monde, config, "P", 6)
    assert len(modele.fmt.tok) < VOCABULAIRE
    d = dv.Distillateur(modele, dv.MoteurTorch(modele), tmp_path, tmp_path / "course", motifs=MOTIFS)
    base = lo.empreinte_base(modele.torch)
    sorties = d.distiller(config, monde, x["acceptes"], x["temoins"])
    for nom, sha in sorties.items():
        assert verifier(tmp_path / "course" / nom) == sha
    s = json.loads((tmp_path / "course" / "distillation-iib-v5.json").read_text(encoding="utf-8"))
    assert s["empreinte_base_avant"] == s["empreinte_base_apres"] == base == lo.empreinte_base(modele.torch)
    assert s["modules_injectes"] == len(lo.modules_lora(modele.torch)) > 0
    for nom in cd.ADAPTATEURS:
        a = s["adaptateurs"][nom]
        assert len(a["journal"]) == 3 and all(j["perte"] == j["perte"] for j in a["journal"]) and s["identite"][nom]["ecart_max_dose_1"] > 0
        etat = torch.load(tmp_path / "course" / a["fichier"], map_location="cpu", weights_only=True)
        assert all(v.dtype == torch.float16 for v in etat.values()) and any(float(v.abs().max()) > 0 for k, v in etat.items() if k.endswith(".B"))
    assert modele.dose == 0.0
    vus = []
    for c in list(la.CONDITIONS_EVALUATION) + ["H"]:
        d.charger(c)
        vus.append((c, modele.adaptateur_charge, jm.lire_doses(d.modele)))
        rg.jouer_lot(d.modele, [EnvironnementJouet("v1")], ["v1"], [jm.Graines(3).entiers("a", 10)], 400, 1.0)
    assert vus == [("H", "eleve", [0.0]), ("B50", "eleve", [0.5]), ("B100", "eleve", [1.0]), ("TJ100", "temoin-jumeau", [1.0]),
                   ("H", "eleve", [0.0])]
    assert jm.exiger_dose_nulle(d.modele) == 0.0 and d.cloturer()
    # artefact : une dose changée sur les modules, dans le dos du distillateur
    d2 = dv.Distillateur(modele, d.moteur, tmp_path, tmp_path / "course-2", motifs=MOTIFS)
    d2.distille, d2.section, d2.empreintes = True, d.section, d.empreintes
    d2.charger("B100")
    lo.fixer_dose(modele.torch, 0.25)
    with pytest.raises(GardeArret, match="dose lue sur le modèle"):
        d2.modele.generer_actions([list(modele.fmt.ouverture("", "task v0 step 1"))], [1], 400, 1.0)
