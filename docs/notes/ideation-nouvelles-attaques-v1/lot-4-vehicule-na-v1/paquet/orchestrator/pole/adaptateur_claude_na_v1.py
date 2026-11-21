"""Véhicule NA-1, lot 4 — adaptateur Claude neuf, sans texte système, qui conserve les réponses brutes
(`adaptateur_claude_na_v1`).

Lettre : V9 (`864f39a7…`), l. 73 (rien d'autre de fixe), l. 396 (réponses brutes conservées) ; conception du véhicule v5
(`1b7f6822…`), § 0 bis (D2 : rien n'est ajouté à l'enveloppe ; 07:46Z, mot 5), § 2.3 (adaptateur Claude neuf), § 6.2
(adaptateur sans texte système ; réponses brutes conservées) ; relevé du lot 0 (`10ac79ec…`), Q1, Q5, Q10.

- **Sans texte système.** L'adaptateur du kit (`AdaptateurClaudeSDK`) pose toujours un texte système fixe, choisi par le
  nom de rôle technique, et aucun réglage ne le retire (relevé du lot 0, Q1). Celui-ci construit ses options par
  `construire_options` de l'adaptateur existant (aucun outil, un tour, plafond de l'appel, aucun repli de modèle, bac à
  sable, lectures interdites) puis **remplace le seul texte système** par la forme choisie : `"chaine_vide"` (une chaîne
  vide explicite, essayée d'abord : 07:46Z, mot 5) ou `"absent"` (aucun texte). L'adaptateur existant n'est pas modifié.
  Ce que l'outil envoie alors au fournisseur se relève au faux fournisseur (`releve_sans_systeme_na_v1`).
- **Rôles** : `proposeur_ideation` et `juge_ideation` (le portier est appelé sous le second) ; aucun mode de lecture, aucune
  racine de lecture, aucun outil.
- **Réponses brutes conservées** (V9, l. 396 ; relevé du lot 0, Q10) : avant de rendre la main, l'adaptateur écrit dans le
  dossier des réponses (dans le dossier de sortie, en quarantaine) un fichier neuf, nommé par la seule session
  (`reponse-brute-<session>.json`, puis `-2`, `-3`… : on n'écrase jamais), qui porte le texte rendu non caviardé, le
  statut, le champ de refus, l'erreur, le modèle servi, le coût déclaré, et son compagnon `.sha256`. Une réponse en refus
  ou en erreur est conservée comme les autres ; une exception de la session aussi (son type seul), avant d'être relevée.
  **La conservation impossible arrête l'appel** : rien n'est rendu sans copie.

Bibliothèque standard, et les modules existants de l'orchestrateur (`adaptateurs`, `caviardage`, `outils`, `relais`).
"""

import asyncio
import hashlib
import json
import os

from .adaptateurs import (AdaptateurClaudeSDK, MoteurNonArme, Resultat, construire_options, importer_sdk,
                          verifier_modele_reel)
from .caviardage import caviarder
from .outils import lister_fichiers
from .relais import CleDansEnvironnement, noms_de_cle_presents

VERSION = "adaptateur-claude-na-v1"
FORMES_SANS_SYSTEME = ("chaine_vide", "absent")
FORME_DEFAUT = "chaine_vide"  # essayée d'abord (mère, 07:46Z, mot 5) ; retenue ou non sur pièce, après le relevé
ROLES_NA = ("proposeur_ideation", "juge_ideation")
PREFIXE_REPONSE = "reponse-brute-"
FORMAT_REPONSE = "reponse-brute-na-v1"


class ConservationImpossible(RuntimeError):
    """La réponse brute n'a pas pu être écrite : l'appel s'arrête, rien n'est rendu sans copie."""


def construire_options_na(dossier, budget_usd, max_tours, *, url_relais, modele, role, interdire_lecture=None,
                          forme_sans_systeme=FORME_DEFAUT):
    """Les options de l'adaptateur du kit, au seul texte système près, remplacé par la forme choisie."""
    if role not in ROLES_NA:
        raise ValueError(f"rôle du véhicule : {ROLES_NA}")
    if forme_sans_systeme not in FORMES_SANS_SYSTEME:
        raise ValueError(f"forme sans texte système : {FORMES_SANS_SYSTEME}")
    o = dict(construire_options(dossier, budget_usd, max_tours, url_relais=url_relais, modele=modele, role=role,
                                interdire_lecture=interdire_lecture))
    o["system_prompt"] = "" if forme_sans_systeme == "chaine_vide" else None
    o["forme_sans_systeme"] = forme_sans_systeme
    return o


class AdaptateurClaudeNA(AdaptateurClaudeSDK):
    """Moteur réel du véhicule pour les clés Claude : `query()` du kit, une session neuve par appel, sans texte système."""

    nom = "claude-sdk-na"

    def __init__(self, url_relais, dossier_reponses, *, forme_sans_systeme=FORME_DEFAUT, environnement=None, arme=False,
                 interdire_lecture=None, delai_s=None, sdk=None):
        kw = {} if delai_s is None else {"delai_s": delai_s}
        super().__init__(url_relais, environnement=environnement, arme=arme, interdire_lecture=interdire_lecture, **kw)
        if forme_sans_systeme not in FORMES_SANS_SYSTEME:
            raise ValueError(f"forme sans texte système : {FORMES_SANS_SYSTEME}")
        if not isinstance(dossier_reponses, str) or not os.path.isabs(dossier_reponses) or not os.path.isdir(dossier_reponses):
            raise ValueError("dossier des réponses brutes : un dossier absolu existant (dans le dossier de sortie)")
        self.forme_sans_systeme = forme_sans_systeme
        self.dossier_reponses = os.path.normpath(dossier_reponses)
        self._sdk = sdk

    def _conserver(self, dossier, contenu):
        """Écrit la réponse brute dans un fichier neuf, nommé par la session, et son compagnon ; rend le chemin."""
        session = os.path.basename(os.path.normpath(dossier))
        octets = (json.dumps(dict(contenu, format=FORMAT_REPONSE, session=session), ensure_ascii=False, sort_keys=True,
                             indent=1) + "\n").encode("utf-8")
        try:
            for n in range(1, 10_000):
                nom = f"{PREFIXE_REPONSE}{session}{'' if n == 1 else '-' + str(n)}.json"
                chemin = os.path.join(self.dossier_reponses, nom)
                if os.path.exists(chemin) or os.path.exists(chemin + ".sha256"):
                    continue
                with open(chemin, "xb") as f:
                    f.write(octets)
                    f.flush()
                    os.fsync(f.fileno())
                with open(chemin + ".sha256", "x", encoding="utf-8") as f:
                    f.write(f"{hashlib.sha256(octets).hexdigest()}  {nom}\n")
                return chemin
        except OSError as e:
            raise ConservationImpossible(f"réponse brute non conservée ({type(e).__name__}) : l'appel s'arrête, rien "
                                         "n'est rendu sans copie") from None
        raise ConservationImpossible("trop de réponses brutes pour une même session : rien n'est rendu sans copie")

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        environnement = os.environ if self._environnement is None else self._environnement
        presents = noms_de_cle_presents(environnement)
        if presents:
            raise CleDansEnvironnement("variables de clé présentes dans l'environnement de l'orchestrateur ("
                                       + ", ".join(presents) + ") : la clé doit rester dans le relais du noyau")
        if not self.arme:
            raise MoteurNonArme("moteur réel non armé : aucun agent réel n'est lancé (essais, simulation)")
        verifier_modele_reel(modele)
        if not isinstance(consigne, str):
            raise TypeError("la consigne est une chaîne")
        sdk = self._sdk if self._sdk is not None else importer_sdk()
        o = construire_options_na(os.path.abspath(dossier), budget_usd, max_tours, url_relais=self.url_relais,
                                  modele=modele, role=role, interdire_lecture=self.interdire_lecture,
                                  forme_sans_systeme=self.forme_sans_systeme)
        options = self.options_sdk(sdk, o)
        try:
            texte, cout, statut, erreur, lecture = asyncio.run(self._executer(sdk, consigne, options, self.delai_s))
        except BaseException as e:
            self._conserver(dossier, {"statut": "exception", "erreur": type(e).__name__, "texte_brut": None, "refus": None,
                                      "modele_servi": None, "cout_declare_usd": None, "cout_inconnu": True})
            raise
        self._conserver(dossier, {"statut": statut, "erreur": erreur, "texte_brut": texte, "refus": lecture["refus"],
                                  "modele_servi": lecture["modele_servi"], "cout_declare_usd": cout,
                                  "cout_inconnu": lecture["cout_inconnu"]})
        return Resultat(caviarder(texte)[0], lister_fichiers(dossier), cout, statut, erreur, texte_brut=texte,
                        refus=lecture["refus"], modele_servi=lecture["modele_servi"],
                        depense_modele_non_autorise_usd=lecture["depense_modele_non_autorise_usd"],
                        cout_inconnu=lecture["cout_inconnu"])


__all__ = ("AdaptateurClaudeNA", "construire_options_na", "ConservationImpossible", "FORMES_SANS_SYSTEME", "FORME_DEFAUT",
           "ROLES_NA")
