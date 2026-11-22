#!/usr/bin/env python3
"""Gabarit d'adaptateur réel vers une interface de complétion de conversation (forme « chat completions », celle que les
fournisseurs de Kimi exposent ; à confirmer sur leur documentation avant le GO) — v1. Bibliothèque standard seule.
**Aucun transport réseau n'est câblé ici** : `TransportNonCable` refuse tout envoi. Le transport réel s'écrit sous GO, avec
ces mêmes exigences, et passe les mêmes épreuves (`epreuves_lanceur_pilote_v2.py`) sur le faux fournisseur avant tout appel.

Exigences vérifiées (contre-lecture de la v3, A3 à A5) :
1. **Aucune relance interne** : le transport doit déclarer `relances_internes == 0` (l'équivalent de `max_retries=0` d'un kit
   client) et `repli_modele is None` ; sinon `ConfigurationRefusee` à la construction (le lanceur refuse : code 24). Le
   transport doit rendre, à chaque réponse, le nombre d'envois qu'il a faits (`tentatives`) : absent ou ≠ 1, l'appel est
   compté à sa réserve multipliée par le nombre d'envois rendu (au moins une), et la course s'arrête (16).
2. **Un seul envoi par appel**, jamais de nouvel envoi dans l'adaptateur : la relance n'appartient qu'au lanceur, qui la compte.
3. **Réflexion comptée dans la sortie** : sortie = `completion_tokens` + tout compte de réflexion rendu HORS de
   `completion_tokens` (`reasoning_tokens` au premier niveau de `usage`). Si le détail `completion_tokens_details.reasoning_tokens`
   dépasse `completion_tokens`, la réflexion est réputée hors du compte et ajoutée. La garde compare ensuite à `max_tokens`.
4. **Modèle servi = modèle demandé**, sinon anomalie (repli silencieux interdit) : compté à la réserve, arrêt 16.
5. Toute erreur du transport après l'envoi remonte : `ErreurFournisseur` (relançable, comptée à la réserve par le lanceur) ou
   toute autre exception (comptée à la réserve, arrêt 17). Une réponse sans `usage` lisible rend `usage=None` (réserve, arrêt 16).
"""


class ConfigurationRefusee(Exception):
    pass


class ErreurFournisseur(Exception):
    """Erreur rendue par le fournisseur (délai, surcharge) ; le lanceur peut relancer dans la limite du budget d'échecs."""


class AnomalieReponse(Exception):
    """Réponse incohérente (modèle servi différent, tentatives ≠ 1) : comptée à la réserve, arrêt 16."""


class TransportNonCable:
    relances_internes = 0
    repli_modele = None

    def envoyer(self, requete):
        raise ConfigurationRefusee("transport réel non câblé : à écrire sous GO, puis éprouver sur le faux fournisseur")


class AdaptateurChatCompletions:
    def __init__(self, transport, modele):
        if getattr(transport, "relances_internes", None) != 0:
            raise ConfigurationRefusee(f"relances internes du transport = {getattr(transport, 'relances_internes', None)!r} (0 exigé)")
        if getattr(transport, "repli_modele", "absent") is not None:
            raise ConfigurationRefusee("repli de modèle déclaré ou non déclaré (None exigé)")
        if not isinstance(modele, str) or not modele:
            raise ConfigurationRefusee("modèle non nommé")
        self.transport, self.modele = transport, modele
        self.relances_internes = 0

    def appeler(self, appel, texte, max_tokens):
        requete = {"model": self.modele, "messages": [{"role": "user", "content": texte}], "max_tokens": max_tokens,
                   "stream": False, "n": 1}
        rep = self.transport.envoyer(requete)  # un seul envoi ; aucune boucle ici
        if not isinstance(rep, dict):
            return {"usage": None, "texte": "", "fin": None}
        if rep.get("model") != self.modele:
            raise AnomalieReponse(f"modèle servi {rep.get('model')!r} ≠ demandé {self.modele!r}")
        n = rep.get("tentatives")
        if n != 1:  # le transport doit rendre le nombre d'envois faits ; absent ou ≠ 1 : anomalie
            ex = AnomalieReponse(f"tentatives du transport = {n!r} (1 exigée)")
            ex.envois = n if isinstance(n, int) and not isinstance(n, bool) and n > 1 else 1
            raise ex
        u = rep.get("usage")
        try:
            entree = u["prompt_tokens"]
            comp = u["completion_tokens"]
            hors = u.get("reasoning_tokens", 0) or 0
            det = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0) or 0
            if any(not isinstance(x, int) or isinstance(x, bool) for x in (entree, comp, hors, det)):
                raise TypeError("compte non entier")
            sortie = comp + hors + (det if det > comp else 0)
            usage = {"entree": entree, "sortie": sortie}
        except (KeyError, TypeError):
            usage = None
        ch = (rep.get("choices") or [{}])[0]
        return {"usage": usage, "texte": (ch.get("message") or {}).get("content", ""), "fin": ch.get("finish_reason")}
