"""Moteur simulé de la v68 (aucun appel, aucune dépense) — au-dessus de `simulation_v56` (inchangé, R12).

Pourquoi : l'essai à blanc du rang 0 n'a pu montrer qu'une sélection **vide** (les fiches simulées n'ont pas de champ
`test_de_mort` : l'étage les refuse toutes), alors que le défaut de la v59 et la lecture de la sélection se jouent sur une
sélection **non vide**. Deux ajouts, tous deux inertes pour une configuration dont les champs de fiche ne portent pas
`test_de_mort` (la configuration v5 de la course d'auto-conception) : alors les réponses sont celles de la v56 au caractère près.

1. **Fiches avec un test** : si `champs_fiche` contient `test_de_mort`, chaque fiche simulée porte un champ `test_de_mort` à bloc
   `statistique` (fichier `scores.csv`, colonne `score`, moyenne ; seuil « au moins 0,30 » ; donnée `DONNEE_SIMULEE`), et, s'ils
   sont demandés, `prediction`, `signe` (« + ») et `metrique` lisibles par l'étage. Les autres champs : ceux de la v56.
2. **Rôles de l'étage** (`experimentateur_test`, `lecteur_test` de l'étage v5) : l'expérimentateur rend, au premier tour, un script
   qui écrit le fichier brut `scores.csv` (moyenne 0,42 : « survit », ou 0,18 : « éliminée », selon l'empreinte de
   l'identifiant de la fiche, `survit_si`), puis « fin » ; le lecteur est un témoin honnête du chiffre imprimé. Le verdict reste
   celui du noyau de l'étage v5 (fichier brut) ; rien ici ne le décide autrement que par les nombres écrits dans le fichier.

Graines : aucune (réponses déterministes, empreinte des entrées), R9 sans objet."""

import hashlib
import json
import os
import re

from .protocole_outils import DEBUT_DONNEES, FIN_DONNEES
from .simulation_v56 import AdaptateurSimuleV56

VERSION = "simulation-v68"
ROLE_EXPERIMENTATEUR, ROLE_LECTEUR = "experimentateur_test", "lecteur_test"
DONNEE_SIMULEE = "episodes.csv"
SEUIL_SIMULE = "au moins 0,30"
BLOC_SIMULE = {"fichier": "scores.csv", "colonne": "score", "statistique": "moyenne"}
SURVIT, ELIMINEE = (0.3, 0.5, 0.46), (0.1, 0.2, 0.24)  # moyennes 0,42 et 0,18 autour du seuil 0,30
FIN = "```json\n" + json.dumps({"fin": "fini"}) + "\n```"


def survit_par_empreinte(identifiant):
    """Règle simulée par défaut : deux fiches sur trois « survivent » (empreinte de l'identifiant, aucune graine)."""
    return int(hashlib.sha256(identifiant.encode("utf-8")).hexdigest()[:8], 16) % 3 != 0


def script_experimentateur(valeurs):
    csv = "episode,score\n" + "".join(f"{i},{float(v)!r}\n" for i, v in enumerate(valeurs, 1))
    moyenne = sum(valeurs) / len(valeurs)
    return (f"open('scores.csv', 'w', encoding='utf-8').write({csv!r})\n"
            f"print('RESULTAT: {moyenne:.2f}')\n")


def _section(consigne, debut_titre):
    m = re.search(r"## " + re.escape(debut_titre) + r"[^\n]*\n.*?" + re.escape(DEBUT_DONNEES) + r"\s*```json\n(.*?)\n```\s*"
                  + re.escape(FIN_DONNEES), consigne, re.S)
    return json.loads(m.group(1)) if m else None


def lecteur_temoin(consigne):
    """Témoin honnête : la dernière ligne `RESULTAT:` de la dernière exécution réussie, comparée au seuil gelé."""
    from .tests_de_mort_v5 import TITRE_SECTION_PREREG, comparer
    prereg = _section(consigne, TITRE_SECTION_PREREG)
    vue = _section(consigne, "Sortie scellée des exécutions") or []
    reussies = [e for e in vue if e.get("statut") == "réussie" and e.get("lignes_resultat")]
    if not prereg or not reussies:
        return "VERDICT: non concluant ; chiffre: aucun ; ligne: aucune"
    ligne = reussies[-1]["lignes_resultat"][-1]
    valeur = float(ligne.split(":", 1)[1])
    survit = comparer(valeur, prereg["seuil"]["comparateur"], prereg["seuil"]["valeur"])
    return f"VERDICT: {'survit' if survit else 'éliminée'} ; chiffre: {valeur} ; ligne: {ligne}"


class AdaptateurSimuleV68(AdaptateurSimuleV56):
    def __init__(self, *, survit_si=survit_par_empreinte, **kw):
        super().__init__(**kw)
        self.survit_si = survit_si
        self._dossier = None

    def description(self):
        return dict(super().description(), version=VERSION)

    def fiche(self, graine):
        f = super().fiche(graine)
        if "test_de_mort" in self.champs:
            f["test_de_mort"] = {"seuil": SEUIL_SIMULE, "test": f"score moyen par épisode (fiche simulée {graine % 97})",
                                 "donnees": [DONNEE_SIMULEE], "statistique": dict(BLOC_SIMULE)}
            if "prediction" in self.champs:
                f["prediction"] = "score moyen de 0,4"
            if "signe" in self.champs:
                f["signe"] = "+"
            if "metrique" in self.champs:
                f["metrique"] = "score moyen par épisode"
        return f

    def reponse(self, role, consigne, modele):
        if role == ROLE_EXPERIMENTATEUR and self._dossier is not None:
            d_fiche = os.path.dirname(os.path.dirname(self._dossier))
            ident, tour = os.path.basename(d_fiche), int(os.path.basename(self._dossier).split("-")[1])
            if tour > 1:
                return FIN
            valeurs = SURVIT if self.survit_si(ident) else ELIMINEE
            return "```json\n" + json.dumps({"experience": [{"executer": {"script": script_experimentateur(valeurs)}}]},
                                            ensure_ascii=False) + "\n```"
        if role == ROLE_LECTEUR:
            return lecteur_temoin(consigne)
        return super().reponse(role, consigne, modele)

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self._dossier = dossier
        try:
            return super().lancer(role, consigne, dossier, budget_usd, max_tours, modele=modele)
        finally:
            self._dossier = None


__all__ = ("AdaptateurSimuleV68", "survit_par_empreinte", "DONNEE_SIMULEE", "BLOC_SIMULE", "SEUIL_SIMULE", "VERSION")
