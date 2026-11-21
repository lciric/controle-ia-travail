"""Chargeur du modèle de l'organisme retenu, v5 (contre-lecture du code, B1).

La configuration en version 5 vérifie la section `oracle` à l'égalité avec le texte scellé : les réglages non textuels du modèle
(forme du lot des suites, noyau d'attention, précision, variables du gabarit) vivent dans la section neuve `modele`, vérifiée
par `configuration_v5.exiger_modele` (égale aux constantes en mode réel). Ce module la lit et rend un modèle à l'interface
qu'emploient les oracles et les générations (`fmt`, `torch`, `generer_actions`, `suites`).

- `charger_modele_reel(config)` : Llama-3.1-8B-Instruct à la révision figée, par les mêmes fonctions que la version 1
  (`harnais.modeles.charger_modele`, `harnais.formats.FormatChat`, `modele_v1.ModeleTorch`) ; contrôle du format de l'agent
  (`premier_test_ia.run.controler_format_agent`). **Écrit, jamais exécuté ici** : il demande torch et télécharge des poids.
- `construire_modele(config)` : mode jouet → `jouet_v5.ModeleJouetDeLangue` (aucun torch) ; mode réel → `charger_modele_reel`.
Tirage : `modele_v1.ModeleTorch` tire à la température seule (ni coupe de probabilité cumulée, ni nombre de jetons gardés, ni
pénalité), pour l'agent comme pour le jumeau : c'est ce qui tient l'égalité réelle des réglages de tirage (contre-lecture, m6).
"""
from __future__ import annotations

from ..gardes import GardeArret
from . import configuration_v5 as cf


def exiger_tirage_a_la_temperature_seule(config: dict) -> None:
    """Le modèle ne sait tirer qu'à la température : tout autre réglage de tirage non neutre est un refus."""
    t = config["tirage"]
    neutres = {"coupe_probabilite_cumulee": 1.0, "jetons_gardes": 0, "penalite_repetition": 1.0, "penalite_presence": 0.0, "penalite_frequence": 0.0}
    for k, v in neutres.items():
        if float(t[k]) != float(v):
            raise GardeArret(f"tirage.{k} = {t[k]!r} : le modèle ne tire qu'à la température (valeur neutre {v!r} exigée)")
    if float(t["temperature"]) != float(config["generation"]["temperature"]):
        raise GardeArret("température du jumeau ≠ température de la génération de l'agent (refus)")


def charger_modele_reel(config: dict):
    """Modèle réel (carte seulement) : jamais appelé par les essais."""
    from ..harnais.formats import FormatChat
    from ..harnais.modeles import charger_modele, exiger_modele_autorise, fins_du_modele
    from ..premier_test_ia.run import controler_format_agent
    from .modele_v1 import ModeleTorch

    cf.exiger_modele(config)
    exiger_tirage_a_la_temperature_seule(config)
    a, m = config["agent"], config["modele"]
    exiger_modele_autorise(a["modele"], a["revision"])
    torch_m, tok = charger_modele(a["modele"], a["revision"], m["precision"], m["appareil"], m["noyau_attention"])
    fmt = FormatChat(tok, variables=m["variables_gabarit"])
    fmt.fins = fins_du_modele(torch_m, tok) | {fmt._pieces(("x", "y"))["cloture"][0]}
    modele = ModeleTorch(torch_m, fmt, m["forme_lot_suites"], nom=f"{a['modele']}@{a['revision'][:12]}")
    modele.controle_du_format = controler_format_agent(fmt, a, config["mode"])
    return modele


def construire_modele(config: dict):
    cf.exiger_modele(config)
    exiger_tirage_a_la_temperature_seule(config)
    if config["mode"] == "jouet":
        from .jouet_v5 import ModeleJouetDeLangue

        return ModeleJouetDeLangue(config.get("jouet") or {})
    return charger_modele_reel(config)
