"""Le registre des tentatives (plan, § 1 ; préenregistrement v3, B4, B9) et sa projection vers la fiche de l'étage.

Une entrée par tentative : `probleme`, `tentative` (engagement scellé, son empreinte, description bornée), `justification`,
`prediction` et son empreinte (écrits par le proposeur) ; `resultat`, `gardee`, `provenance` (écrits par programme). Registre
en ajout seul, chaîné par empreintes, scellé à chaque génération. Trois vues servies : entière, sans `resultat` ni `gardee`,
aucune. Gardes de B9 portées ici : 3 (prédiction scellée), 4 (chaîne), 5 (historique de départ), 7 (grain), 8 (champs du bras 1),
9 (génération finale sans écriture), 11 (entrée de l'expérimentateur sur la projection), 2 (aucun champ du registre chez un juge).
"""

import copy
import hashlib
import json
import os
import re

from .constantes import (CLASSES, DEBUT_DONNEES, FIN_DONNEES, HYPOTHESE_NEUTRE, METRIQUE_NEUTRE, NON_EPROUVEE,
                         PREDICTION_NEUTRE, STATUTS_RESULTAT, TITRE_NEUTRE)
from .lois import json_canonique

CHAMPS_PROPOSEUR = ("probleme", "tentative", "justification", "prediction", "prediction_sha256")
CHAMPS_PROGRAMME = ("resultat", "gardee", "provenance")
CHAMPS_CHAINE = ("empreinte_precedente", "empreinte")
VUES = ("entiere", "sans_resultat_ni_gardee", "aucune")
LISTES_EXPERIMENTATEUR = ("avec_description", "engagement_seul")
ORIGINES = ("course-source", "continuation")
_MOT_DE_PROVENANCE = re.compile(r"^(?:[a-z][a-z0-9-]{0,63}|[0-9a-f]{64})$")
ZERO = "0" * 64


class ArretRegistre(RuntimeError):
    pass


def sha256_texte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def empreinte_prediction(prediction):
    return sha256_texte(json_canonique(list(prediction)))


def valider_prediction(prediction):
    """Une probabilité par classe, en dixièmes, de somme un (plan, § 3.2) ; refus sinon."""
    if not isinstance(prediction, (list, tuple)) or len(prediction) != len(CLASSES):
        raise ArretRegistre("prédiction : trois probabilités attendues")
    dixiemes = [round(p * 10) for p in prediction]
    if any(abs(p * 10 - d) > 1e-9 or d < 0 for p, d in zip(prediction, dixiemes)) or sum(dixiemes) != 10:
        raise ArretRegistre(f"prédiction mal formée : {prediction!r}")
    return True


def _empreinte_entree(entree, precedente):
    corps = {k: entree[k] for k in CHAMPS_PROPOSEUR + CHAMPS_PROGRAMME}
    return sha256_texte(precedente + json_canonique(corps))


def verifier_grain(objet_programme):
    """Garde 7 : les champs écrits par programme et le retour ne portent aucun nombre hors du coût ; leurs textes sont pris
    dans une liste fermée (classes, statut, mots de provenance). Arrêt sinon."""
    def visiter(x, chemin):
        if isinstance(x, bool) or x is None:
            return
        if isinstance(x, (int, float)):
            if chemin[-1:] != ("cout_usd",):
                raise ArretRegistre(f"garde 7 : nombre hors du coût dans un champ écrit par programme : {'/'.join(chemin)}")
            return
        if isinstance(x, str):
            if chemin[-1:] == ("classe",):
                if x not in STATUTS_RESULTAT:
                    raise ArretRegistre(f"garde 7 : classe hors de la liste fermée : {x!r}")
            elif not _MOT_DE_PROVENANCE.match(x):
                raise ArretRegistre(f"garde 7 : texte hors de la liste fermée dans {'/'.join(chemin)} : {x!r}")
            return
        if isinstance(x, dict):
            for k, v in x.items():
                visiter(v, chemin + (str(k),))
            return
        if isinstance(x, list):
            for i, v in enumerate(x):
                visiter(v, chemin + (str(i),))
            return
        raise ArretRegistre(f"garde 7 : valeur de type inattendu dans {'/'.join(chemin)}")
    visiter(objet_programme, ())
    return True


def verifier_prediction_proposeur(entree):
    valider_prediction(entree["prediction"])
    return True


class Registre:
    """Registre en mémoire et sur disque (`chemin` : fichier JSON-lignes ; `chemin + '.sceaux'` : un sceau par génération)."""

    def __init__(self, chemin=None, entrees=None):
        self.chemin = chemin
        self.entrees = []
        self.sceaux = []
        self.ferme = False  # génération finale : aucune écriture
        for e in entrees or []:
            self.entrees.append(copy.deepcopy(e))
        if chemin is not None and entrees is None:
            if os.path.exists(chemin):
                raise ArretRegistre(f"registre déjà présent : {chemin} (jamais d'écrasement)")
            open(chemin, "x", encoding="utf-8").close()  # registre né vide : fichier vide, vérifiable sur disque

    # -- écriture ------------------------------------------------------------------------------------------------------------
    def derniere_empreinte(self):
        return self.entrees[-1]["empreinte"] if self.entrees else ZERO

    def ajouter(self, entree):
        if self.ferme:
            raise ArretRegistre("garde 9 : écriture pendant la génération finale : arrêt")
        manquants = [k for k in CHAMPS_PROPOSEUR + CHAMPS_PROGRAMME if k not in entree]
        if manquants:
            raise ArretRegistre(f"entrée incomplète : {manquants}")
        if entree["prediction_sha256"] != empreinte_prediction(entree["prediction"]):
            raise ArretRegistre("garde 3 : prédiction modifiée après coup : refus d'écrire le résultat")
        verifier_grain({k: entree[k] for k in CHAMPS_PROGRAMME})
        e = {k: copy.deepcopy(entree[k]) for k in CHAMPS_PROPOSEUR + CHAMPS_PROGRAMME}
        e["empreinte_precedente"] = self.derniere_empreinte()
        e["empreinte"] = _empreinte_entree(e, e["empreinte_precedente"])
        self.entrees.append(e)
        if self.chemin is not None:
            with open(self.chemin, "a", encoding="utf-8") as f:
                f.write(json_canonique(e) + "\n")
        return e

    def sceller_generation(self, nom):
        sceau = {"generation": nom, "entrees": len(self.entrees), "tete": self.derniere_empreinte()}
        self.sceaux.append(sceau)
        if self.chemin is not None:
            with open(self.chemin + ".sceaux", "a", encoding="utf-8") as f:
                f.write(json_canonique(sceau) + "\n")
        return sceau

    def fermer(self):
        self.ferme = True

    # -- vérification --------------------------------------------------------------------------------------------------------
    def octets(self):
        return "".join(json_canonique(e) + "\n" for e in self.entrees).encode("utf-8")

    def verifier_chaine(self, depuis_le_disque=True):
        """Garde 4 : chaîne d'empreintes et sceaux de génération ; sur disque si le registre en a un. Arrêt sinon."""
        entrees = self.entrees
        if depuis_le_disque and self.chemin is not None:
            with open(self.chemin, encoding="utf-8") as f:
                entrees = [json.loads(l) for l in f if l.strip()]
            if json_canonique(entrees) != json_canonique(self.entrees):
                raise ArretRegistre("garde 4 : registre sur disque différent du registre tenu : arrêt")
        precedente = ZERO
        for i, e in enumerate(entrees):
            if e.get("empreinte_precedente") != precedente or e.get("empreinte") != _empreinte_entree(e, precedente):
                raise ArretRegistre(f"garde 4 : chaîne rompue à l'entrée {i} : arrêt")
            precedente = e["empreinte"]
        for s in self.sceaux:
            if s["entrees"] > len(entrees) or (s["entrees"] and entrees[s["entrees"] - 1]["empreinte"] != s["tete"]):
                raise ArretRegistre(f"garde 4 : sceau de génération {s['generation']} non conforme (entrée retirée ou réécrite)")
        return True

    # -- vues servies --------------------------------------------------------------------------------------------------------
    def vue(self, mode):
        if mode not in VUES:
            raise ArretRegistre(f"vue inconnue : {mode!r}")
        if mode == "aucune":
            return None
        out = []
        for e in self.entrees:
            v = {k: copy.deepcopy(e[k]) for k in CHAMPS_PROPOSEUR + ("provenance",)}
            if mode == "entiere":
                v["resultat"] = copy.deepcopy(e["resultat"])
                v["gardee"] = e["gardee"]
            out.append(v)
        return out


def exiger_historique_vide(historique):
    """Garde 5 : un historique de départ non vide arrête le lancement."""
    if historique:
        raise ArretRegistre("garde 5 : historique de départ non vide : arrêt du lancement")
    return True


def verifier_bras_1_non_servi(bras, servi):
    """Garde 8 : au bras 1, aucun champ du registre n'est servi."""
    if bras == "1" and servi:
        raise ArretRegistre("garde 8 : un champ du bras 1 est servi : arrêt")
    return True


def verifier_finale_sans_ecriture(octets_avant, registre):
    """Garde 9 : le registre est identique à l'octet avant et après la génération finale."""
    if registre.octets() != octets_avant:
        raise ArretRegistre("garde 9 : registre modifié pendant la génération finale : arrêt")
    return True


def retour(entrees_de_la_generation):
    """Le retour ordinaire servi au proposeur : une classe (ou le statut de budget) et un coût par tentative."""
    out = [{"classe": e["resultat"]["classe"], "cout_usd": e["resultat"]["cout_usd"]} for e in entrees_de_la_generation]
    verifier_grain({"retour": out})
    return out


# --- projection vers la fiche de l'étage (garde 11) -------------------------------------------------------------------------


def description_balisee(description):
    return DEBUT_DONNEES + "\n" + description + "\n" + FIN_DONNEES


def projeter_vers_fiche(entree, identifiant_servi, liste="avec_description"):
    """La carte servie à l'étage, au gabarit du tour fermé (`tour_ferme_v64.carte_servie`) : titre, prédiction, signe et
    métrique neutres écrits par l'orchestrateur ; `hypothese` (projetée sur `enonce`) porte la description bornée entre balises
    de donnée, ou l'hypothèse neutre pour la liste « engagement seul » ; `test_de_mort` est le champ de l'engagement scellé."""
    if liste not in LISTES_EXPERIMENTATEUR:
        raise ArretRegistre(f"liste de l'expérimentateur inconnue : {liste!r}")
    t = entree["tentative"]
    hyp = description_balisee(t["description"]) if liste == "avec_description" else HYPOTHESE_NEUTRE
    return {"identifiant": identifiant_servi, "titre": TITRE_NEUTRE, "hypothese": hyp, "prediction": PREDICTION_NEUTRE,
            "signe": "+", "metrique": METRIQUE_NEUTRE, "test_de_mort": copy.deepcopy(t["engagement"]["test_de_mort"]),
            "source": "reel"}


CHAMPS_DE_LA_CARTE = ("identifiant", "titre", "hypothese", "prediction", "signe", "metrique", "test_de_mort", "source")


def verifier_projection(carte, entree, autres_entrees, liste="avec_description"):
    """Garde 11 : la carte projetée est exactement celle de la liste gelée pour cette entrée ; aucun autre champ du registre
    (justification, prédiction, résultat, provenance, une autre entrée) n'y figure. Arrêt sinon."""
    attendue = projeter_vers_fiche(entree, carte.get("identifiant"), liste)
    if sorted(carte) != sorted(CHAMPS_DE_LA_CARTE) or json_canonique(carte) != json_canonique(attendue):
        raise ArretRegistre("garde 11 : projection hors de la liste gelée : arrêt de la génération")
    texte = json_canonique(carte)
    interdits = [entree["justification"], json_canonique(list(entree["prediction"])), entree["prediction_sha256"]]
    for a in autres_entrees:
        if a is entree:
            continue
        interdits.append(a["tentative"]["description"])
        interdits.append(a["tentative"]["engagement_sha256"])
    for x in interdits:
        if x and x in texte and not (liste == "avec_description" and x == entree["tentative"]["description"]):
            raise ArretRegistre("garde 11 : un champ du registre hors de la liste figure dans la projection : arrêt")
    return True


def classement_de_l_enveloppe(cartes):
    """Le classement que l'étage exige, écrit par l'enveloppe : toutes les lignes éligibles, dans l'ordre du scellement."""
    return [{"ident": c["identifiant"], "notable": True, "rang": k} for k, c in enumerate(cartes, 1)]


def entree_d_un_juge(**champs):
    """Garde 2 : aucun juge n'existe à l'étage ; la fonction qui bâtirait l'entrée d'un juge refuse tout champ du registre."""
    interdits = set(CHAMPS_PROPOSEUR + CHAMPS_PROGRAMME + CHAMPS_CHAINE) | {"registre", "entrees"}
    trouves = sorted(set(champs) & interdits)
    if trouves:
        raise ArretRegistre(f"garde 2 : champ du registre dans l'entrée d'un juge : {trouves} : arrêt")
    return dict(champs)


def nouvelle_entree(probleme, engagement_, engagement_sha256, description, justification, prediction):
    """Les champs écrits par le proposeur ; la prédiction est scellée par son empreinte avant toute épreuve."""
    valider_prediction(prediction)
    return {"probleme": probleme,
            "tentative": {"engagement": engagement_, "engagement_sha256": engagement_sha256, "description": description},
            "justification": justification, "prediction": list(prediction),
            "prediction_sha256": empreinte_prediction(prediction)}


def provenance(origine, generation, version, configuration_sha256):
    if origine not in ORIGINES:
        raise ArretRegistre(f"origine inconnue : {origine!r}")
    return {"origine": origine, "generation": f"generation-{generation}", "orchestrateur": version,
            "configuration": configuration_sha256}


def resultat_non_eprouvee(cout_usd=0.0):
    return {"classe": NON_EPROUVEE, "cout_usd": float(cout_usd)}
