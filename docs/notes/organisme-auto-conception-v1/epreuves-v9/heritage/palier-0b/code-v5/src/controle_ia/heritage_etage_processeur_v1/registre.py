"""Le registre des tentatives (plan, § 1 ; préenregistrement v6, B4, B9) et sa projection vers la fiche de l'étage.

Une entrée par tentative : `probleme`, `tentative` (engagement scellé, son empreinte, description bornée), `justification`,
`prediction` et son empreinte (écrits par le proposeur) ; `resultat`, `gardee`, `provenance` (écrits par programme). Registre
en ajout seul, chaîné par empreintes, scellé à chaque génération. Trois vues servies : entière, sans `resultat` ni `gardee`,
aucune. Gardes de B9 portées ici : 2, 3, 4, 5, 6, 7, 8, 9, 11, 27.

Balisage (version 4, annexe F, point 5) : la description bornée est portée par le champ `hypothese` de la carte (projeté sur
`enonce` par la correspondance de l'organisme), **sans balise** : l'étage sert déjà le préenregistrement court entier dans une
section de données entre ses deux balises ; une balise de donnée écrite dans un champ de la fiche projetée arrête la génération.
"""

import copy
import hashlib
import json
import os
import re

from .constantes import (CLASSES, DEBUT_DONNEES, FIN_DONNEES, HYPOTHESE_NEUTRE, METRIQUE_NEUTRE, NON_EPROUVEE, PREDICTION_NEUTRE,
                         STATUTS_RESULTAT, TITRE_NEUTRE)
from .lois import json_canonique

CHAMPS_PROPOSEUR = ("probleme", "tentative", "justification", "prediction", "prediction_sha256")
CHAMPS_PROGRAMME = ("resultat", "gardee", "provenance")
CHAMPS_CHAINE = ("empreinte_precedente", "empreinte")
VUES = ("entiere", "sans_resultat_ni_gardee", "aucune")
LISTES_EXPERIMENTATEUR = ("avec_description", "engagement_seul")
ORIGINES = ("course-source", "continuation")
_MOT_DE_PROVENANCE = re.compile(r"^(?:[a-z][a-z0-9-]{0,63}|[0-9a-f]{64})$")
ZERO = "0" * 64
BALISES = (DEBUT_DONNEES, FIN_DONNEES, "<<<<<", ">>>>>")


class ArretRegistre(RuntimeError):
    pass


def sha256_texte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def sha256_octets(octets):
    return hashlib.sha256(octets).hexdigest()


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


def _verifier_textes_programme(x, chemin):
    if isinstance(x, bool) or x is None:
        return
    if isinstance(x, (int, float)):
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
            _verifier_textes_programme(v, chemin + (str(k),))
        return
    if isinstance(x, list):
        for i, v in enumerate(x):
            _verifier_textes_programme(v, chemin + (str(i),))
        return
    raise ArretRegistre(f"garde 7 : valeur de type inattendu dans {'/'.join(chemin)}")


def _nombres(x, chemin, out):
    if isinstance(x, bool) or x is None or isinstance(x, str):
        return
    if isinstance(x, (int, float)):
        out.append(chemin)
        return
    if isinstance(x, dict):
        for k, v in x.items():
            _nombres(v, chemin + (str(k),), out)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            _nombres(v, chemin + (str(i),), out)


def _nombre_permis(chemin):
    """Grain du § 3.2 : les probabilités prédites et le coût ; le seuil écrit par le proposeur est un texte."""
    return (len(chemin) == 2 and chemin[0] == "prediction") or chemin[-1:] == ("cout_usd",)


def verifier_grain(objet):
    """Garde 7 : la sérialisation (une entrée du registre, une vue servie ou le retour) ne porte aucun nombre hors des
    probabilités prédites et du coût ; les textes des champs écrits par programme et du retour sont pris dans une liste fermée
    (classes, statut, mots de provenance). Arrêt sinon."""
    def une(e, prefixe):
        nombres = []
        _nombres(e, (), nombres)
        for c in nombres:
            if not _nombre_permis(c):
                raise ArretRegistre(f"garde 7 : nombre hors du grain : {'/'.join(prefixe + c)}")
        if isinstance(e, dict):
            for k in CHAMPS_PROGRAMME + ("retour",):
                if k in e:
                    _verifier_textes_programme(e[k], (k,))
    if isinstance(objet, list):
        for i, e in enumerate(objet):
            une(e, (str(i),))
    else:
        une(objet, ())
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
            open(chemin, "x", encoding="utf-8").close()

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
        e = {k: copy.deepcopy(entree[k]) for k in CHAMPS_PROPOSEUR + CHAMPS_PROGRAMME}
        verifier_grain(e)
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

    def octets(self):
        return "".join(json_canonique(e) + "\n" for e in self.entrees).encode("utf-8")

    def empreinte_fichier(self):
        with open(self.chemin, "rb") as f:
            return sha256_octets(f.read())

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
        verifier_grain(out)
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
    if registre.chemin is not None and registre.empreinte_fichier() != sha256_octets(octets_avant):
        raise ArretRegistre("garde 9 : registre sur disque modifié pendant la génération finale : arrêt")
    return True


def verifier_cloisonnement(dossier_du_bras, servi, dossiers_des_autres_bras):
    """Garde 6 : aucun dossier lisible commun à deux continuations ; aucun chemin d'un autre bras dans ce qui est servi."""
    a = os.path.realpath(dossier_du_bras)
    for d in dossiers_des_autres_bras:
        b = os.path.realpath(d)
        if a == b or a.startswith(b + os.sep) or b.startswith(a + os.sep):
            raise ArretRegistre(f"garde 6 : dossier commun à deux continuations ({a}, {b}) : arrêt")
    texte = json_canonique(servi) if servi is not None else ""
    for d in dossiers_des_autres_bras:
        for forme in {os.path.normpath(d), os.path.realpath(d)}:
            if forme and forme in texte:
                raise ArretRegistre(f"garde 6 : un chemin d'un autre bras ({forme}) est servi : arrêt")
    return True


def verifier_registre_etranger(bras, sha_registre_servi_au_depart, sha_registre_etranger, sha_registre_source_propre):
    """Garde 27 : la copie du registre étranger n'est servie qu'aux bras 4a et 4b ; au bras 4a, la copie servie au départ a
    l'empreinte du registre de la course de la source étrangère, jamais celle de la source propre ; aucun bras du critère ne la
    reçoit. `sha_registre_servi_au_depart` : None si rien n'est servi au départ (bras 1, 2 et 4b). Au bras 4b, rien n'est
    servi au départ ; la copie servie à chaque génération est contrôlée par `verifier_vue_etrangere_4b` (code v3, C2)."""
    if bras == "4a":
        if sha_registre_servi_au_depart == sha_registre_source_propre:
            raise ArretRegistre("garde 27 : registre de la source propre servi au bras 4a (ce serait le bras 3) : arrêt")
        if sha_registre_servi_au_depart != sha_registre_etranger:
            raise ArretRegistre("garde 27 : la copie servie au bras 4a n'a pas l'empreinte du registre étranger : arrêt")
    elif bras in ("1", "2", "3"):
        if sha_registre_servi_au_depart is not None and sha_registre_servi_au_depart == sha_registre_etranger:
            raise ArretRegistre(f"garde 27 : registre étranger servi au bras {bras}, bras du critère : arrêt")
        if bras == "3" and sha_registre_servi_au_depart != sha_registre_source_propre:
            raise ArretRegistre("garde 27 : le bras 3 ne reçoit pas le registre de sa propre source : arrêt")
    return True


def empreinte_vue(vue):
    """Empreinte canonique d'une vue servie (liste d'entrées ; une vue vide ou « aucune » vaut la liste vide)."""
    return sha256_texte(json_canonique(list(vue or [])))


def verifier_vue_etrangere_4b(vue_servie, empreinte_deposee, source_propre, source_etrangere):
    """Garde 27 au bras 4b (code v3, C2 ; B7 bis : ce qui est servi à chaque génération est le registre que tient, à la même
    génération, le bras 2 de la source étrangère, et « son empreinte est celle du registre de la source étrangère »). Avant de
    servir la copie d'une génération : la copie ne vient pas de la source propre ; chaque entrée servie a été écrite par la
    continuation du bras 2 de la source étrangère ; l'empreinte canonique de la copie servie est celle que l'orchestrateur a
    déposée avec elle, prise sur la vue du bras 2 de la source étrangère au moment où ce bras l'a reçue. Arrêt sinon : le
    registre de la source propre servi au bras 4b (ce serait le bras 2), ou une copie altérée ou d'une autre origine."""
    propre, etrangere = f"source-{source_propre}", f"source-{source_etrangere}"
    if etrangere == propre:
        raise ArretRegistre("garde 27 : copie déposée au bras 4b venue de la source propre (ce serait le bras 2) : arrêt")
    for e in vue_servie or []:
        p = e.get("provenance") or {}
        if p.get("source") == propre:
            raise ArretRegistre("garde 27 : entrée de la source propre servie au bras 4b (ce serait le bras 2) : arrêt")
        if p.get("source") != etrangere or p.get("bras") != "bras-2" or p.get("origine") != "continuation":
            raise ArretRegistre("garde 27 : une entrée servie au bras 4b n'est pas du bras 2 de la source étrangère : arrêt")
    if empreinte_vue(vue_servie) != empreinte_deposee:
        raise ArretRegistre("garde 27 : la copie servie au bras 4b n'a pas l'empreinte de la vue du bras 2 de la source "
                            "étrangère : arrêt")
    return True


def retour(entrees_de_la_generation):
    """Le retour ordinaire servi au proposeur : une classe (ou le statut de budget) et un coût par tentative."""
    out = {"retour": [{"classe": e["resultat"]["classe"], "cout_usd": e["resultat"]["cout_usd"]} for e in entrees_de_la_generation]}
    verifier_grain(out)
    return out["retour"]


# --- projection vers la fiche de l'étage (garde 11) -------------------------------------------------------------------------

CHAMPS_DE_LA_CARTE = ("identifiant", "titre", "hypothese", "prediction", "signe", "metrique", "test_de_mort", "source")


def projeter_vers_fiche(entree, identifiant_servi, liste="avec_description"):
    """La carte servie à l'étage, au gabarit du tour fermé (`tour_ferme_v64.carte_servie`) : titre, prédiction, signe et
    métrique neutres écrits par l'orchestrateur ; `hypothese` (projetée sur `enonce` par `a_blanc_v59.CORRESPONDANCE`) porte la
    description bornée, sans balise, ou l'hypothèse neutre pour la liste « engagement seul » ; `test_de_mort` est le champ de
    l'engagement scellé."""
    if liste not in LISTES_EXPERIMENTATEUR:
        raise ArretRegistre(f"liste de l'expérimentateur inconnue : {liste!r}")
    t = entree["tentative"]
    hyp = t["description"] if liste == "avec_description" else HYPOTHESE_NEUTRE
    return {"identifiant": identifiant_servi, "titre": TITRE_NEUTRE, "hypothese": hyp, "prediction": PREDICTION_NEUTRE,
            "signe": "+", "metrique": METRIQUE_NEUTRE, "test_de_mort": copy.deepcopy(t["engagement"]["test_de_mort"]),
            "source": "reel"}


def verifier_projection(carte, entree, autres_entrees, liste="avec_description"):
    """Garde 11 : la carte projetée est exactement celle de la liste gelée pour cette entrée ; aucune balise de donnée dans un
    champ ; aucun autre champ du registre (justification, prédiction, résultat, provenance, une autre entrée) n'y figure."""
    texte = json_canonique(carte)
    for b in BALISES:
        if b in texte:
            raise ArretRegistre("garde 11 : une balise de donnée est écrite dans un champ de la fiche projetée : arrêt")
    attendue = projeter_vers_fiche(entree, carte.get("identifiant"), liste)
    if sorted(carte) != sorted(CHAMPS_DE_LA_CARTE) or texte != json_canonique(attendue):
        raise ArretRegistre("garde 11 : projection hors de la liste gelée : arrêt de la génération")
    interdits = [entree["justification"], json_canonique(list(entree["prediction"])), entree["prediction_sha256"]]
    if liste == "engagement_seul":
        interdits.append(entree["tentative"]["description"])
    for a in autres_entrees:
        if a is entree:
            continue
        interdits.append(a["tentative"]["engagement_sha256"])
        interdits.append(a["justification"])
    for x in interdits:
        if x and x in texte and not (liste == "avec_description" and x == entree["tentative"]["description"]):
            raise ArretRegistre("garde 11 : un champ du registre hors de la liste figure dans la projection : arrêt")
    return True


def classement_de_l_enveloppe(cartes):
    """Le classement que l'étage exige, écrit par l'enveloppe : toutes les lignes éligibles, dans l'ordre du scellement, sans
    juge ni rang tiré d'un juge."""
    return [{"ident": c["identifiant"], "notable": True, "rang": k} for k, c in enumerate(cartes, 1)]


def entree_d_un_juge(**champs):
    """Garde 2 : aucun juge n'existe à l'étage ; la fonction qui bâtirait l'entrée d'un juge refuse tout champ du registre."""
    interdits = set(CHAMPS_PROPOSEUR + CHAMPS_PROGRAMME + CHAMPS_CHAINE) | {"registre", "entrees", "tentative", "vue"}
    trouves = sorted(set(champs) & interdits)
    if trouves:
        raise ArretRegistre(f"garde 2 : champ du registre dans l'entrée d'un juge : {trouves} : arrêt")
    for k, v in champs.items():
        if isinstance(v, (dict, list)):
            texte = json_canonique(v)
            if any(f'"{c}"' in texte for c in interdits):
                raise ArretRegistre(f"garde 2 : champ du registre glissé dans l'entrée d'un juge ({k}) : arrêt")
    return dict(champs)


def nouvelle_entree(probleme, engagement_, engagement_sha256, description, justification, prediction):
    """Les champs écrits par le proposeur ; la prédiction est scellée par son empreinte avant toute épreuve."""
    valider_prediction(prediction)
    return {"probleme": probleme,
            "tentative": {"engagement": engagement_, "engagement_sha256": engagement_sha256, "description": description},
            "justification": justification, "prediction": list(prediction),
            "prediction_sha256": empreinte_prediction(prediction)}


def provenance(origine, generation, version, configuration_sha256, source, bras):
    """Génération, source, version de l'orchestrateur, empreinte de la configuration (plan, § 1), et le bras qui écrit
    l'entrée (identifie la continuation, pour la conduite du lecteur réglé pour la tenue)."""
    if origine not in ORIGINES:
        raise ArretRegistre(f"origine inconnue : {origine!r}")
    return {"origine": origine, "generation": f"generation-{generation}", "orchestrateur": version,
            "configuration": configuration_sha256, "source": f"source-{source}", "bras": f"bras-{bras}"}


def resultat_non_eprouvee(cout_usd=0.0):
    return {"classe": NON_EPROUVEE, "cout_usd": float(cout_usd)}
