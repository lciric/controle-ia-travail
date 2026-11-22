#!/usr/bin/env python3
"""Registre de dépense persistant du pilote — v2 (vérification de la v4 : N1 à N4, et « relu avant chaque appel »).
Bibliothèque standard seule ; aucun appel, aucun réseau.

Trois fichiers, aux chemins fixés par l'appelant (`Chemins`) — le lanceur les écrit en dur pour le pilote :
- le **registre** (JSON par ligne, ajout seul, chaîne des empreintes de ligne) ;
- son **sceau à secret** `<registre>.sceau` : HMAC-SHA256 du contenu entier et du nombre de lignes, sous une **clé** de 32 octets
  tirée une fois (`os.urandom`), gardée à part (fichier en mode 600, hors du dépôt pour le pilote) ;
- une **ancre** hors du registre : empreinte de la ligne de tête (identité du registre), nombre de lignes et sceau courants.
  L'ancre ne peut que croître : un registre plus court que l'ancre, ou d'une autre tête, est refusé.
Règles :
- `creer` : refus si le registre, son sceau ou l'ancre existent déjà (un seul registre par ancre, jamais recréé) ;
- `Registre(chemins, parametres)` prend un **verrou exclusif** (`fcntl.flock`, non bloquant) sur `<registre>.verrou`, tenu
  jusqu'à `fermer()` : une seconde course sur le même registre est refusée (25) avant toute dépense ; puis vérifie tout ;
- `verifier()` relit le fichier, le sceau et l'ancre et les compare à l'état tenu par cette course : appelé **avant chaque
  réserve** (donc avant chaque appel) ; tout écart ⇒ 22 ;
- chaque écriture passe par des fichiers temporaires propres au processus (`.<pid>.tmp`), remplacés atomiquement.
Codes : 21 absent ; 22 altéré (sceau, chaîne, ancre, tête, longueur, paramètres, écart en cours de course) ; 23 course close ;
24 plafond du registre au-dessus de la borne ; 25 registre déjà tenu par une autre course.
Limite : qui détient la clé ET peut réécrire l'ancre peut tout refaire ; seule la limite chez le fournisseur couvre ce cas.
"""
import fcntl
import hashlib
import hmac
import json
import os

GENESE = "registre-depense-pilote-essaim-v2"


class RegistreRefuse(Exception):
    def __init__(self, code, detail):
        super().__init__(f"registre {code} : {detail}")
        self.code, self.detail = code, detail


class Chemins:
    def __init__(self, registre, ancre, cle):
        self.registre, self.ancre, self.cle = registre, ancre, cle
        self.sceau, self.verrou = registre + ".sceau", registre + ".verrou"


def _h(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _ecrire_atomique(chemin, texte):
    tmp = f"{chemin}.{os.getpid()}.tmp"
    with open(tmp, "x", encoding="utf-8") as f:
        f.write(texte)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, chemin)


def _lire_cle(chemins):
    try:
        cle = open(chemins.cle, "rb").read()
    except OSError:
        raise RegistreRefuse(22, "clé du sceau absente")
    if len(cle) != 32:
        raise RegistreRefuse(22, "clé du sceau mal formée")
    return cle


def _sceau(cle, octets):
    n = octets.count(b"\n")
    return hmac.new(cle, octets + f"|{n}".encode(), hashlib.sha256).hexdigest(), n


def _ancre(octets, mac, n):
    tete = octets.split(b"\n", 1)[0].decode("utf-8")
    return {"tete_sha256": _h(tete), "lignes": n, "sceau": mac}


def creer(chemins, parametres):
    for p in (chemins.registre, chemins.sceau, chemins.ancre):
        if os.path.exists(p):
            raise RegistreRefuse(22, f"déjà présent : {os.path.basename(p)} (un seul registre par ancre, jamais recréé)")
    if not os.path.exists(chemins.cle):
        fd = os.open(chemins.cle, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as f:
            f.write(os.urandom(32))
    cle = _lire_cle(chemins)
    ligne = json.dumps({"n": 0, "evenement": "creation", "parametres": parametres, "prec": _h(GENESE),
                        "nonce": os.urandom(16).hex()}, ensure_ascii=False, sort_keys=True) + "\n"
    with open(chemins.registre, "x", encoding="utf-8") as f:
        f.write(ligne)
        f.flush()
        os.fsync(f.fileno())
    octets = ligne.encode("utf-8")
    mac, n = _sceau(cle, octets)
    _ecrire_atomique(chemins.sceau, json.dumps({"hmac": mac, "lignes": n}) + "\n")
    _ecrire_atomique(chemins.ancre, json.dumps(_ancre(octets, mac, n)) + "\n")


class Registre:
    def __init__(self, chemins, parametres_geles, borne):
        self.c = chemins
        if not os.path.exists(chemins.registre):
            raise RegistreRefuse(21, f"registre absent : {os.path.basename(chemins.registre)}")
        self._fv = open(chemins.verrou, "a+")
        try:
            fcntl.flock(self._fv.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self._fv.close()
            self._fv = None
            raise RegistreRefuse(25, "registre déjà tenu par une autre course (verrou exclusif)")
        try:
            self.cle = _lire_cle(chemins)
            octets = open(chemins.registre, "rb").read()
            self._controler(octets)
            self.lignes = self._chaine(octets)
            if self.lignes[0].get("evenement") != "creation":
                raise RegistreRefuse(22, "première ligne n'est pas la création")
            plaf = self.lignes[0]["parametres"].get("plafond_depense_usd")
            if not isinstance(plaf, (int, float)) or plaf > borne + 1e-9:
                raise RegistreRefuse(24, f"plafond du registre {plaf!r} au-dessus de la borne {borne}")
            if self.lignes[0]["parametres"] != parametres_geles(plaf):
                raise RegistreRefuse(22, "paramètres de création différents des gelés (plan, prix, plafonds)")
            if any(l["evenement"] in ("fin", "arret") for l in self.lignes):
                raise RegistreRefuse(23, "course close (fin ou arrêt écrit) : aucune poursuite")
            self.plafond = float(plaf)
        except BaseException:
            self.fermer()
            raise

    def _controler(self, octets):
        try:
            s = json.loads(open(self.c.sceau, encoding="utf-8").read())
            a = json.loads(open(self.c.ancre, encoding="utf-8").read())
        except (OSError, ValueError) as ex:
            raise RegistreRefuse(22, f"sceau ou ancre absent ou illisible ({type(ex).__name__})")
        mac, n = _sceau(self.cle, octets)
        if not hmac.compare_digest(s.get("hmac", ""), mac) or s.get("lignes") != n:
            raise RegistreRefuse(22, "sceau à secret différent (registre altéré ou re-scellé sans la clé)")
        if a != _ancre(octets, mac, n):
            if a.get("tete_sha256") != _ancre(octets, mac, n)["tete_sha256"]:
                raise RegistreRefuse(22, "tête du registre ≠ ancre (registre neuf ou autre registre)")
            raise RegistreRefuse(22, f"registre de {n} lignes ≠ ancre de {a.get('lignes')} lignes (tronqué, allongé ou entrelacé)")
        self._octets_tenus = octets

    def _chaine(self, octets):
        prec, lignes = _h(GENESE), []
        for i, brut in enumerate(octets.decode("utf-8").splitlines()):
            try:
                l = json.loads(brut)
            except ValueError:
                raise RegistreRefuse(22, f"ligne {i} illisible")
            if l.get("prec") != prec or l.get("n") != i:
                raise RegistreRefuse(22, f"chaîne rompue à la ligne {i}")
            prec = _h(brut)
            lignes.append(l)
        if not lignes:
            raise RegistreRefuse(22, "registre vide")
        self.dernier = prec
        return lignes

    def verifier(self):
        """Avant chaque réserve : le fichier, le sceau et l'ancre doivent être exactement ceux que cette course a écrits."""
        octets = open(self.c.registre, "rb").read()
        if octets != self._octets_tenus:
            raise RegistreRefuse(22, "registre changé hors de cette course depuis sa dernière écriture")
        self._controler(octets)

    def etat(self):
        depense, regles, echecs, ouvert = 0.0, [], 0, None
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
        suspens = None
        if ouvert is not None:
            suspens = ouvert
            depense += ouvert["reserve_usd"]
            echecs += 1
        return {"depense": depense, "regles": regles, "echecs": echecs, "suspens": suspens}

    def ecrire(self, **ligne):
        self.verifier()
        ligne = dict(ligne, n=len(self.lignes), prec=self.dernier)
        brut = json.dumps(ligne, ensure_ascii=False, sort_keys=True)
        with open(self.c.registre, "a", encoding="utf-8") as f:
            f.write(brut + "\n")
            f.flush()
            os.fsync(f.fileno())
        octets = self._octets_tenus + (brut + "\n").encode("utf-8")
        mac, n = _sceau(self.cle, octets)
        _ecrire_atomique(self.c.sceau, json.dumps({"hmac": mac, "lignes": n}) + "\n")
        _ecrire_atomique(self.c.ancre, json.dumps(_ancre(octets, mac, n)) + "\n")
        self._octets_tenus = octets
        self.lignes.append(ligne)
        self.dernier = _h(brut)

    def fermer(self):
        if getattr(self, "_fv", None) is not None:
            try:
                fcntl.flock(self._fv.fileno(), fcntl.LOCK_UN)
            finally:
                self._fv.close()
                self._fv = None
