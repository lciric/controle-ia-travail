#!/usr/bin/env python3
"""Adaptateur strict pour Kimi — v2 : `adaptateur_fournisseur_v1.AdaptateurChatCompletions` (inchangé, scellé dans le
dépôt) plus des vérifications faites à la construction ET avant chaque appel (sinon `ConfigurationRefusee`, sans envoi) :

1. `type(transport) is transport_kimi_reel_v2.TransportKimiReel` (classe exacte, jamais une sous-classe) ;
2. le fichier du module de transport a l'empreinte `SHA_TRANSPORT`, et celui de `adaptateur_fournisseur_v1` l'empreinte
   `SHA_ADAPTATEUR_V1` (écrites ici en dur) ; les modules chargés sont ceux de `sys.modules` ;
3. **code d'origine** : le code de chaque fonction et méthode des deux modules (module, classes, fonctions imbriquées)
   est comparé à celui compilé depuis leur fichier empreinté — une méthode remplacée sur la classe, une fonction du module
   réécrite, ou `AdaptateurChatCompletions.appeler` remplacée est vue ; aucune n'est en trop ni en moins ;
4. **constantes** : chaque affectation littérale de niveau module du fichier du transport (`MODELE`, `CHEMIN`,
   `PLAFOND_MAX_TOKENS`, `MOTIFS_SOURCES`, `HOMOGLYPHES`…) est relue dans le fichier et comparée à la globale chargée ;
5. aucun attribut d'instance ne masque une méthode ; `transport._valider_integrite()` (configuration figée, TLS, pile
   `http.client`, `debuglevel`) ;
6. le modèle est `kimi-k3.1-pro`.

Ce qu'il ne couvre pas (déclaré) : `object.__setattr__` suivi d'un recalcul d'empreinte, `ctypes`, une couche réseau
remplacée en C, un envoi doublé sous `socket` (visible au seul serveur), une réécriture conjointe des fichiers et de ces
empreintes, et le lanceur v2 qui admet toute sous-classe de l'adaptateur (`isinstance`) : un lanceur v3 devrait exiger
`type(adaptateur) is AdaptateurKimiStrict` et l'empreinte de ce fichier.
"""
import ast
import hashlib
import sys
import types

import adaptateur_fournisseur_v1 as A
import transport_kimi_reel_v2 as T

SHA_TRANSPORT = "76f847d00fff28a541b8a2ea876a09253a6f8b30e567edb6ae5c25dea657ae23"
SHA_ADAPTATEUR_V1 = "67704c1e42a0308a4f511ddc82e58666e6741b9b954f78072fd55a64c7eff1e4"


def _lire(module):
    with open(module.__file__, "rb") as f:
        return f.read()


def _signature(code):
    return (code.co_qualname, code.co_code, code.co_names, code.co_varnames, code.co_freevars,
            tuple(_signature(c) if isinstance(c, types.CodeType) else repr(c) for c in code.co_consts))


ANONYMES = ("<lambda>", "<genexpr>", "<listcomp>", "<dictcomp>", "<setcomp>")


def _est_fonction(code):
    return code.co_flags & 0x3 == 0x3 and code.co_name not in ANONYMES  # CO_OPTIMIZED | CO_NEWLOCALS : pas un corps de classe


def _parcourir(code, sortie):
    for c in code.co_consts:
        if isinstance(c, types.CodeType):
            if _est_fonction(c):
                sortie.setdefault(c.co_qualname, _signature(c))
            _parcourir(c, sortie)


def _codes_du_source(octets, chemin):
    sortie = {}
    _parcourir(compile(octets, chemin, "exec"), sortie)
    return sortie


def _codes_charges(module):
    sortie = {}

    def ajouter(f):
        f = getattr(f, "__func__", f)
        code = getattr(f, "__code__", None)
        if code is not None:
            if getattr(f, "__module__", None) != module.__name__:
                sortie["<étranger>" + str(getattr(f, "__qualname__", "?"))] = None
                return
            sortie[code.co_qualname] = _signature(code)
            _parcourir(code, sortie)
    for nom, v in vars(module).items():
        if isinstance(v, type) and v.__module__ == module.__name__:
            for f in vars(v).values():
                ajouter(f)
        elif isinstance(v, types.FunctionType):
            ajouter(v)  # une fonction étrangère posée dans le module est marquée, donc refusée
    return sortie


def _constantes_du_source(octets):
    sortie = {}
    for n in ast.parse(octets).body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            try:
                sortie[n.targets[0].id] = ast.literal_eval(n.value)
            except (ValueError, SyntaxError, TypeError):
                pass
    return sortie


def _verifier_module(module, sha, constantes=False):
    if sys.modules.get(module.__name__) is not module:
        raise A.ConfigurationRefusee(f"module {module.__name__} rechargé ou substitué")
    octets = _lire(module)
    if hashlib.sha256(octets).hexdigest() != sha:
        raise A.ConfigurationRefusee(f"fichier de {module.__name__} d'empreinte différente")
    if _codes_du_source(octets, module.__file__) != _codes_charges(module):
        raise A.ConfigurationRefusee(f"code chargé de {module.__name__} différent de son fichier (fonction ou méthode remplacée)")
    if constantes:
        for nom, valeur in _constantes_du_source(octets).items():
            if getattr(module, nom, object()) != valeur:
                raise A.ConfigurationRefusee(f"constante {nom} de {module.__name__} réécrite")


def verifier_transport(transport):
    if type(transport) is not T.TransportKimiReel:
        raise A.ConfigurationRefusee(f"transport de classe {type(transport).__qualname__} : classe exacte TransportKimiReel exigée")
    _verifier_module(T, SHA_TRANSPORT, constantes=True)
    _verifier_module(A, SHA_ADAPTATEUR_V1)
    if T.CLASSES_DE_CONNEXION != (T.ConnexionHTTPComptee, T.ConnexionHTTPSComptee) \
            or T.ConnexionHTTPComptee.__mro__ != (T.ConnexionHTTPComptee, T._Compteur, T.http.client.HTTPConnection, object) \
            or T.ConnexionHTTPSComptee.__mro__[:3] != (T.ConnexionHTTPSComptee, T._Compteur, T.http.client.HTTPSConnection):
        raise A.ConfigurationRefusee("classes de connexion comptées altérées")
    methodes = {n for n, v in vars(T.TransportKimiReel).items() if callable(v) or isinstance(v, (staticmethod, classmethod))}
    if methodes & set(vars(transport)):
        raise A.ConfigurationRefusee("méthode masquée par un attribut d'instance")
    if transport.relances_internes != 0 or transport.repli_modele is not None:
        raise A.ConfigurationRefusee("relances internes ou repli déclarés")
    transport._valider_integrite()


class AdaptateurKimiStrict(A.AdaptateurChatCompletions):
    def __init__(self, transport, modele="kimi-k3.1-pro"):
        verifier_transport(transport)
        if modele != "kimi-k3.1-pro":
            raise A.ConfigurationRefusee(f"modèle {modele!r} : kimi-k3.1-pro seul admis")
        super().__init__(transport, modele)

    def appeler(self, appel, texte, max_tokens):
        verifier_transport(self.transport)
        if self.modele != "kimi-k3.1-pro" or self.relances_internes != 0:
            raise A.ConfigurationRefusee("adaptateur modifié après la construction")
        return super().appeler(appel, texte, max_tokens)
