#!/usr/bin/env python3
"""Registre de dépense persistant du pilote — v1 (contre-lecture de la v3, artefact A2). Bibliothèque standard seule.

Un registre est un fichier JSON par ligne, ouvert en ajout seulement, plus un sceau `<registre>.sceau` qui porte l'empreinte
sha256 du contenu entier et le nombre de lignes. Chaque ligne porte l'empreinte de la ligne précédente (`prec`), la première
celle de la constante `GENESE`. Le registre est **créé une seule fois** (`creer`, refus si le fichier existe), avec le plan,
les prix et le plafond gelés ; il est **relu et vérifié avant tout appel** (`ouvrir`) :
- absent ⇒ `RegistreRefuse(21)` ; sceau absent, empreinte ou nombre de lignes différents, chaîne rompue, ligne illisible ou
  paramètres de création différents des gelés ⇒ `RegistreRefuse(22)` ; course close (`fin` ou `arret` écrit) ⇒ `RegistreRefuse(23)`.
Écriture en tête (« write-ahead ») : la réserve d'un appel est écrite et scellée AVANT l'appel ; une réserve sans règlement
(processus tué pendant l'appel) est comptée entière à la réouverture et compte comme un échec.

Limite : un registre local ne protège pas contre qui réécrit le fichier ET son sceau et sa chaîne, ni contre un registre neuf
créé ailleurs. Seule une limite de dépense chez le fournisseur (crédit prépayé) le fait ; elle est exigée avant le GO.
"""
import hashlib
import json
import os

GENESE = "registre-depense-pilote-essaim-v1"


class RegistreRefuse(Exception):
    def __init__(self, code, detail):
        super().__init__(f"registre {code} : {detail}")
        self.code, self.detail = code, detail


def _h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _sceller(chemin):
    octets = open(chemin, "rb").read()
    n = octets.count(b"\n")
    tmp = chemin + ".sceau.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(json.dumps({"sha256": hashlib.sha256(octets).hexdigest(), "lignes": n}) + "\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, chemin + ".sceau")


def creer(chemin, parametres):
    if os.path.exists(chemin) or os.path.exists(chemin + ".sceau"):
        raise RegistreRefuse(22, f"registre déjà présent : {os.path.basename(chemin)} (jamais recréé)")
    ligne = json.dumps({"n": 0, "evenement": "creation", "parametres": parametres, "prec": _h(GENESE)}, ensure_ascii=False, sort_keys=True)
    with open(chemin, "x", encoding="utf-8") as f:
        f.write(ligne + "\n")
        f.flush()
        os.fsync(f.fileno())
    _sceller(chemin)


class Registre:
    def __init__(self, chemin, parametres_geles):
        self.chemin = chemin
        if not os.path.exists(chemin):
            raise RegistreRefuse(21, f"registre absent : {os.path.basename(chemin)}")
        if not os.path.exists(chemin + ".sceau"):
            raise RegistreRefuse(22, "sceau absent")
        octets = open(chemin, "rb").read()
        try:
            sceau = json.loads(open(chemin + ".sceau", encoding="utf-8").read())
        except (ValueError, OSError) as ex:
            raise RegistreRefuse(22, f"sceau illisible ({type(ex).__name__})")
        if sceau.get("sha256") != hashlib.sha256(octets).hexdigest() or sceau.get("lignes") != octets.count(b"\n"):
            raise RegistreRefuse(22, "contenu différent du sceau (registre altéré)")
        prec = _h(GENESE)
        self.lignes = []
        for i, brut in enumerate(octets.decode("utf-8").splitlines()):
            try:
                l = json.loads(brut)
            except ValueError:
                raise RegistreRefuse(22, f"ligne {i} illisible")
            if l.get("prec") != prec or l.get("n") != i:
                raise RegistreRefuse(22, f"chaîne rompue à la ligne {i}")
            prec = _h(brut)
            self.lignes.append(l)
        self.dernier = prec
        if not self.lignes or self.lignes[0]["evenement"] != "creation":
            raise RegistreRefuse(22, "première ligne n'est pas la création")
        if self.lignes[0]["parametres"] != parametres_geles:
            raise RegistreRefuse(22, "paramètres de création différents des gelés (plan, prix ou plafond)")
        if any(l["evenement"] in ("fin", "arret") for l in self.lignes):
            raise RegistreRefuse(23, "course close (fin ou arrêt écrit) : aucune poursuite")

    def etat(self):
        """Dépense cumulée, appels réglés (ids), échecs comptés, réserve en suspens (appel ouvert à la mort du processus)."""
        depense, regles, echecs, ouvert, messages = 0.0, [], 0, None, {}
        for l in self.lignes[1:]:
            ev = l["evenement"]
            if ev == "reserve":
                ouvert = l
            elif ev in ("regle", "echec", "compte_a_la_reserve"):
                depense += l["cout_usd"]
                if ev != "regle":
                    echecs += 1
                if ev == "regle" or l.get("abandon"):
                    regles.append(l["id"])
                ouvert = None
            elif ev == "message_compte":
                messages[l["monde"]] = messages.get(l["monde"], 0) + 1
        suspens = None
        if ouvert is not None:
            suspens = ouvert
            depense += ouvert["reserve_usd"]
            echecs += 1
        return {"depense": depense, "regles": regles, "echecs": echecs, "suspens": suspens, "messages": messages}

    def ecrire(self, **ligne):
        ligne = dict(ligne, n=len(self.lignes), prec=self.dernier)
        brut = json.dumps(ligne, ensure_ascii=False, sort_keys=True)
        with open(self.chemin, "a", encoding="utf-8") as f:
            f.write(brut + "\n")
            f.flush()
            os.fsync(f.fileno())
        _sceller(self.chemin)
        self.lignes.append(ligne)
        self.dernier = _h(brut)
