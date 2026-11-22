#!/usr/bin/env python3
"""Adaptateur strict pour Kimi — v1 : `adaptateur_fournisseur_v1.AdaptateurChatCompletions` (inchangé, scellé dans le
dépôt) plus l'exigence de la vérification de la v4 : **la classe EXACTE du transport réel**, jamais une sous-classe ni un
transport qui déclarerait seulement `relances_internes = 0`. Bibliothèque standard seule.

Vérifié à la construction ET avant chaque appel (sinon `ConfigurationRefusee`, sans envoi) :
1. `type(transport) is transport_kimi_reel_v1.TransportKimiReel` (pas `isinstance`) ;
2. le fichier du module `transport_kimi_reel_v1` chargé a l'empreinte sha256 `SHA_TRANSPORT` (écrite ici en dur) ;
3. chaque méthode de `METHODES_FIGEES` est encore celle de la classe (aucun remplacement sur la classe) et aucune n'est
   masquée par un attribut d'instance (aucun `transport.envoyer = …`) ; les classes de connexion comptées sont intactes ;
4. le modèle est `kimi-k3.1-pro`.
Le lanceur v2 n'exige que `isinstance(adaptateur, AdaptateurChatCompletions)` : cet adaptateur le satisfait. Qu'il soit
le seul admis est à écrire dans un lanceur v3 (`type(adaptateur) is AdaptateurKimiStrict`) — proposé, non fait ici.
"""
import hashlib
import sys

import adaptateur_fournisseur_v1 as A
import transport_kimi_reel_v1 as T

SHA_TRANSPORT = "4bba649ce1d1b62ea5f50225e62a5eb5666592014033e174b47cca34533aa5a6"


def _empreinte_module():
    with open(T.__file__, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def verifier_transport(transport):
    if type(transport) is not T.TransportKimiReel:
        raise A.ConfigurationRefusee(f"transport de classe {type(transport).__qualname__} : classe exacte TransportKimiReel exigée")
    if sys.modules.get("transport_kimi_reel_v1") is not T:
        raise A.ConfigurationRefusee("module de transport rechargé ou substitué")
    if _empreinte_module() != SHA_TRANSPORT:
        raise A.ConfigurationRefusee("fichier du transport d'empreinte différente de SHA_TRANSPORT")
    for nom, f in T.METHODES_FIGEES.items():
        if T.TransportKimiReel.__dict__.get(nom) is not f:
            raise A.ConfigurationRefusee(f"méthode {nom} remplacée sur la classe du transport")
        if nom in vars(transport):
            raise A.ConfigurationRefusee(f"méthode {nom} masquée par un attribut d'instance")
    if T.ConnexionHTTPComptee.__mro__[1:3] != (T._Compteur, T.http.client.HTTPConnection) \
            or T.ConnexionHTTPSComptee.__mro__[1:3] != (T._Compteur, T.http.client.HTTPSConnection) \
            or T.CLASSES_DE_CONNEXION != (T.ConnexionHTTPComptee, T.ConnexionHTTPSComptee) \
            or T._Compteur.__dict__.get("putrequest") is not T.PUTREQUEST_FIGE \
            or "putrequest" in vars(T.ConnexionHTTPComptee) or "putrequest" in vars(T.ConnexionHTTPSComptee):
        raise A.ConfigurationRefusee("classes de connexion comptées altérées")
    if transport.relances_internes != 0 or transport.repli_modele is not None:
        raise A.ConfigurationRefusee("relances internes ou repli déclarés")


class AdaptateurKimiStrict(A.AdaptateurChatCompletions):
    def __init__(self, transport, modele=T.MODELE):
        verifier_transport(transport)
        if modele != T.MODELE:
            raise A.ConfigurationRefusee(f"modèle {modele!r} : {T.MODELE} seul admis")
        super().__init__(transport, modele)

    def appeler(self, appel, texte, max_tokens):
        verifier_transport(self.transport)
        return super().appeler(appel, texte, max_tokens)
