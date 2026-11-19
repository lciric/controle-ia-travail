"""Fausse machine pour les essais du lanceur du papier C (v1) : remplace l'instance louée, les juges, l'agent et les
sondes. Aucun modèle, aucune carte, aucun réseau. Les lectures sont simulées par un modèle de déférence simple ; chaque
défaut que les gardes doivent voir se règle par un drapeau (`defauts`)."""
import hashlib

import numpy as np


def sha(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


class FausseMachine:
    def __init__(self, cfg: dict, graine: int = 0, prix: float = 1.5, defauts: dict | None = None):
        self.cfg, self.prix, self.defauts = cfg, prix, dict(defauts or {})
        self.rng = np.random.default_rng(graine)
        self.arrets, self.lectures, self.generations = [], 0, []
        self.vrai: dict = {}

    # --- instance ---------------------------------------------------------------------------------------------
    def identifiant_de_l_instance(self) -> str:
        return "31415926"

    def prix_horaire_usd(self) -> float:
        return self.prix

    def arreter(self, identifiant: str) -> bool:
        self.arrets.append(identifiant)
        return not self.defauts.get("arret_refuse", False)

    # --- juges ------------------------------------------------------------------------------------------------
    def revisions_des_juges(self) -> dict:
        r = {j["nom"]: j["revision"] for j in self.cfg["juges"]}
        if self.defauts.get("revision"):
            r[self.cfg["juges"][0]["nom"]] = "autre-revision"
        return r

    def encoder(self, juge: str, texte: str) -> list:
        """Un jeton par caractère ; avec le défaut « espace_fusionne », l'espace final fusionne avec le chiffre."""
        if self.defauts.get("espace_fusionne") and len(texte) >= 2 and texte[-1].isdigit() and texte[-2] == " ":
            return [ord(c) for c in texte[:-2]] + [10_000 + int(texte[-1])]
        return [ord(c) for c in texte]

    def longueur_du_juge(self, juge: str) -> int:
        return 8192

    def contenus_de_calibrage(self, taches: list) -> list:
        sortie = []
        for t in taches:
            for k, condition in enumerate(("honnete", "honnete", "saboteur", "saboteur")):
                sortie.append({"empreinte": sha(f"{t}/{k}"), "tache": t, "condition": condition})
        if self.defauts.get("contenu_hors_lot"):
            sortie.append({"empreinte": sha("hors"), "tache": "tache-hors-du-lot", "condition": "honnete"})
        return sortie

    def _vrai(self, contenu: str) -> float:
        if contenu not in self.vrai:
            self.vrai[contenu] = float(np.clip(np.random.default_rng(int(contenu[:8], 16)).normal(4.0, 1.5), 0.2, 8.8))
        return self.vrai[contenu]

    def lire(self, juge: str, consigne: str, variante: int, mode: str, demandes: list) -> list:
        reponses = []
        systeme_attendu = self.cfg["consignes"][consigne]["systeme_raisonne" if mode == "raisonne" else "systeme_direct"]
        for d in demandes:
            self.lectures += 1
            v = self._vrai(d["contenu"])
            cond = d["condition"]
            gain = 0.02 * cond["indice"] if cond["type"] == "formulation" else 0.0
            score = v + gain * (0.0 - v) + self.rng.normal(0, 0.3)
            masse = 0.97
            if self.defauts.get("masse_faible") == juge or self.defauts.get("masse_faible") == (juge, variante):
                masse = 0.3
            if self.defauts.get("raisonne_illisible") == juge and mode == "raisonne":
                masse = 0.3
            r = {"cle": d["cle"], "score": float(np.clip(score, 0, 9)), "masse": masse, "jetons_contexte": 900,
                 "tronque": False, "consigne_sha256": sha(d["systeme"]), "insertion_presente": True,
                 "insertion_en_place": True, "juge": juge, "consigne": consigne, "variante": variante, "mode": mode}
            assert d["systeme"] == systeme_attendu
            if self.defauts.get("contexte_trop_long"):
                r["jetons_contexte"] = 9000
            if self.defauts.get("tronque"):
                r["tronque"] = True
            if self.defauts.get("consigne_modifiee"):
                r["consigne_sha256"] = sha(d["systeme"] + " Be lenient.")
            if self.defauts.get("insertion_absente") and d["insertion"] is not None:
                r["insertion_presente"] = False
            if self.defauts.get("insertion_deplacee") and d["insertion"] is not None:
                r["insertion_en_place"] = False
            if self.defauts.get("variante_changee") and cond["type"] == "formulation":
                r["variante"] = variante + 1
            reponses.append(r)
        if self.defauts.get("ordre_melange"):
            reponses = reponses[::-1]
        return reponses

    def lire_le_banc(self, juge: str, variante: int) -> dict:
        rng = np.random.default_rng(100 + variante)
        neutre = np.clip(rng.normal(4.5, 1.4, 30), 0.5, 8.5)
        signe = -1.0 if self.defauts.get("banc_contraire") in (True, juge) else 1.0
        critique = neutre + 0.5 * ((1.5 if signe > 0 else 6.0) - neutre) + rng.normal(0, 0.1, 30)
        eloge = neutre + 0.5 * ((6.0 if signe > 0 else 1.5) - neutre) + rng.normal(0, 0.1, 30)
        masse = 0.3 if self.defauts.get("banc_illisible") == juge else 0.96
        return {"neutre": neutre.tolist(), "critique": critique.tolist(), "eloge": eloge.tolist(), "masses": [masse] * 90}

    # --- agent et sondes --------------------------------------------------------------------------------------
    def generer_un_episode(self, demande: dict) -> dict:
        self.generations.append(demande)
        jetons = list(range(100, 140))
        return {"identifiant": f"{demande['tache']}|{demande['cellule']}", "empreinte_contenu": sha(str(sorted(demande.items(), key=str))),
                "jetons_hors_message_systeme": jetons, "borne_champs": 30}

    def relire(self, demande: dict) -> dict:
        jetons = list(range(100, 140))
        if self.defauts.get("relecture_infidele"):
            jetons[-1] += 1
        message = demande["message_systeme"] + (" (autre)" if self.defauts.get("mauvais_message") else "")
        return {"jetons_hors_message_systeme": jetons, "message_systeme_sha256": sha(message),
                "par_jeton": np.zeros(40).tolist()}
