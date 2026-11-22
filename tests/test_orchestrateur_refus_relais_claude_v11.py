"""Point 7 du brouillon 1 du préenregistrement v11 : un appel refusé par le relais Claude (statut 402, plafond de la part Claude
atteint) compte comme **échec du rôle** pour l'orchestrateur épinglé (A3 : échecs consécutifs → arrêt du rôle ; A14 : part
d'appels inexploitables). Lecture du code épinglé (commit `a41b7b50`) :
- `pole/noyau_v56.py` (`eb5a003e…`), `appel` : le texte n'est lu que si `r.statut == "ok"` ; sinon `lu` est None et
  `suivi.apres(..., exploitable=False)` ;
- `pole/suivi_roles_v54.py` (`62022597…`), `apres` : un appel non exploitable est un échec compté (A3) et un inexploitable (A14).
Ces essais jouent la **vraie** classe `SuiviRoles` (bibliothèque standard seule) sur la suite d'appels qu'un relais qui refuse
produit (statut d'adaptateur autre que « ok »). Sautés si l'orchestrateur épinglé n'est pas sur cette machine ; le dossier peut
être donné par la variable `ORCHESTRATEUR_AFFINAGE_ESSAI` (clone en lecture, même commit)."""
import hashlib
import importlib.util
import os
from pathlib import Path

import pytest

CANDIDATS = [Path(os.environ["ORCHESTRATEUR_AFFINAGE_ESSAI"])] if os.environ.get("ORCHESTRATEUR_AFFINAGE_ESSAI") else []
CANDIDATS += [Path("/home/user/ideation-organism/orchestrator"), Path("/home/user/lciric/ideation-organism/orchestrator")]
EMPREINTES = {"pole/suivi_roles_v54.py": "620225973d68670a56ca913cdd02709fa576fa43e1393d166915ea67c1d7c3bb",
              "pole/noyau_v56.py": "eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b"}


def _orchestrateur():
    for o in CANDIDATS:
        if all((o / rel).is_file() and hashlib.sha256((o / rel).read_bytes()).hexdigest() == sha for rel, sha in EMPREINTES.items()):
            return o
    return None


ORCH = _orchestrateur()
pytestmark = pytest.mark.skipif(ORCH is None, reason="orchestrateur épinglé (a41b7b50) absent ou d'une autre empreinte")
ARRETS = {"a3_echecs_consecutifs": 3, "a3_delai_s": {"*": 1800}, "a14_part_max": 0.34, "a11_modeles": []}  # configuration v11


def _suivi():
    spec = importlib.util.spec_from_file_location("suivi_roles_v54_essai", ORCH / "pole" / "suivi_roles_v54.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m, m.SuiviRoles(ARRETS, horloge=lambda: 0.0)


def _appel(s, statut, role="aiguilleur"):
    # comme `noyau_v56.appel` : exploitable seulement pour une réponse « ok » lue
    return s.apres(role, "aiguillage", fournisseur="claude", modele="claude-opus-5-5", duree=1.0, statut=statut,
                   exploitable=(statut == "ok"))


def test_le_noyau_ne_lit_que_les_reponses_ok():
    texte = (ORCH / "pole" / "noyau_v56.py").read_text(encoding="utf-8")
    assert 'texte = (r.texte_brut or r.texte_final) if (r.statut == "ok" and not a2) else None' in texte
    assert "exploitable=lu is not None" in texte


def test_sain_trois_refus_du_relais_arretent_le_role_et_comptent_pour_a14():
    m, s = _suivi()
    for k in range(3):
        utilisable, motif, _ = _appel(s, "erreur")          # 402 du relais Claude : session en erreur, aucune réponse lue
        assert utilisable is False and "inexploitable" in motif
    assert s.roles["aiguilleur"]["arrete"].startswith("A3 : 3 échecs consécutifs")
    with pytest.raises(m.RoleArrete):
        s.avant("aiguilleur")                                # l'appel suivant n'est pas lancé
    assert s.depassements_a14() == {"aiguilleur": 1.0}


def test_artefact_un_appel_ok_entre_deux_refus_ne_coupe_pas_le_role_mais_a14_compte():
    m, s = _suivi()
    for statut in ("erreur", "erreur", "ok", "erreur", "ok", "ok"):
        _appel(s, statut)
    r = s.roles["aiguilleur"]
    assert r["arrete"] is None and r["consecutifs"] == 0 and r["inexploitables"] == 3
    assert s.depassements_a14() == {"aiguilleur": 0.5}      # 3 sur 6 > 0,34 : étape « non mesurée (technique) »
    s.avant("aiguilleur")                                     # le rôle n'est pas arrêté
