"""Véhicule NA-1, lot 4 v3 — adaptateur Claude direct (`adaptateur_claude_direct_na_v2`) : l'interface des messages du
fournisseur, appelée en direct par le relais de la clé, sans l'outil ni le kit d'agent.

v2 (remplace `adaptateur_claude_direct_na_v1.py`, `50563801…`, archivé sans modification ; vérification du lot 4 v2,
point B1). Seul changement de règle : un refus pour crédit d'amont se lit aussi sous la forme reçue ce jour sur une clé,
un statut 400 de type `invalid_request_error` dont le message contient le fragment fixé `FRAGMENT_CREDIT_400`
(comparaison sans casse) ; classe « crédit d'amont (400, message de solde) ». Règle stricte : les trois conditions à la
fois ; le message n'est ni recopié dans la fiche de la tentative, ni dans le résultat, ni au journal (il reste dans la
seule réponse brute conservée, A4).

Lettre : nœuds du véhicule v2 (`79b9d423…`), § 1 (décision N1, exigences A1 à A7) et § 2 (décision N2) ; projet d'additif
v2 (`6e9bb88e…`), A-1 à A-6, § 2 (A1 à A7), § 5 (P1, P3, P16), § 10 (n° 31, n° 32) ; V9 l. 73,
l. 77, l. 387 (rien d'autre de fixe ; plus aucun octet ne change), l. 396 (réponses brutes conservées). Il remplace
`adaptateur_claude_na_v1.py` (`38baa206…`) pour les clés Claude ; l'adaptateur d'origine n'est pas modifié.

- **Corps.** La requête assemblée part seule, dans un message de rôle « user », **sans champ système** (A-1, D2). Le corps
  n'a que des clés d'une liste fermée (`CLES_CORPS`) : le modèle, le plafond de sortie, le message, et les réglages non
  textuels du jeu (rôle, modèle) (A7) ; tout autre champ (`system`, `fallbacks`, `betas`, `tools`, `metadata`, …) refuse
  l'envoi (`CorpsRefuse`). Aucun en-tête n'est ajouté par l'adaptateur, sauf le jeton factice du relais (`x-api-key`) : le
  kit 2.12 ne pose que `Authorization` (relevé du présent lot), que le relais v2 ne relaie pas et ne lit pas.
- **A1, aucune relance cachée.** Le client se construit avec `max_retries=0` ; l'attribut est relu à la construction et
  avant chaque envoi : une autre valeur refuse (`RelanceCachee`). Toute relance est une tentative du véhicule.
- **A2, aucun repli du fournisseur.** Ni le paramètre de repli côté serveur ni un en-tête bêta ne partent (liste fermée du
  corps ; aucun en-tête ajouté). Une trace de repli dans la réponse (bloc `fallback`, itération `fallback_message`) rend
  un refus d'événement `messages.repli_fournisseur`, que la surcharge lit en n° 31. Le modèle servi (`model`) est rendu
  tel quel ; la surcharge le compare au modèle demandé de la tentative.
- **A3, coût d'une tentative.** Par l'usage déclaré, au barème versé (un barème par modèle admis, exigé) ; sans usage
  lisible, le coût est inconnu et vaut le plafond de la tentative (`cout_inconnu`), jamais zéro. Une erreur rendue par un
  statut avant tout octet de réponse coûte zéro ; une erreur après le début d'un flux, ou sans statut (connexion, délai),
  est au coût inconnu.
- **A4, réponse brute conservée par tentative**, refus et erreurs compris, avant de rendre la main : un fichier neuf par
  tentative et son compagnon ; conservation impossible : rien n'est rendu.
- **A5, catégorie** lue au champ `stop_details.category` ; absente ou vide : « catégorie non lue », jamais un vide.
- **A6, liste fermée des raisons d'arrêt** : `end_turn` est « ok » ; `refusal` est un refus de classifieur
  (`messages.stop_reason`, seul déclencheur du repli) ; `max_tokens` et toute autre raison, ou une raison absente, sont une
  erreur « réponse illisible » (servie, jamais rejouée).
- **A7, réglages non textuels par (rôle, modèle)** : un jeu (plafond de sortie, effort, réflexion, flux) pour chaque rôle
  du kit et chaque modèle admis ; chaque valeur est contrôlée à la construction contre la table des valeurs admises
  (versée, avec son empreinte, par la configuration) ; un réglage non admis refuse le départ (n° 32, proposé)
  avec son nom. Aucune valeur admise n'est écrite dans ce module.
- **N2, crédit d'amont** : une erreur 402 de type `billing_error` est rendue « crédit d'amont » ; une erreur 400 de type
  `invalid_request_error` dont le message (`error.message` du corps) contient `FRAGMENT_CREDIT_400`, sans casse, est
  rendue « crédit d'amont (400, message de solde) » ; le 402 du relais à son
  plafond, « plafond du relais » ; le 403 du relais « modèle non permis », un refus d'événement `relais.modele_non_permis`
  (n° 31). Toute autre erreur garde son statut et son type, sans classe de crédit.
- **Modèles admis** : une liste fermée donnée par la configuration (les modèles des rôles et les deux modèles de repli) ;
  `verifier_modele_reel` du kit n'est plus sur le chemin (nœuds v2, § 5.2, point 2).

Bibliothèque standard, et les modules existants de l'orchestrateur (`adaptateurs`, `caviardage`, `outils`, `relais`).
Le paquet `anthropic` n'est importé que pour construire le client réel, jamais dans les essais au faux client.
"""

import dataclasses
import hashlib
import json
import math
import os

from .adaptateurs import Adaptateur, ModeleNonPermis, MoteurNonArme, Resultat
from .caviardage import caviarder
from .outils import lister_fichiers
from .relais import JETON_FACTICE, CleDansEnvironnement, noms_de_cle_presents, valider_url_relais

VERSION = "adaptateur-claude-direct-na-v2"
NOM_ADAPTATEUR = "claude-direct-na"
ROLES_NA = ("proposeur_ideation", "juge_ideation")
FORMAT_REPONSE = "reponse-brute-direct-na-v1"
PREFIXE_REPONSE = "reponse-brute-"
DELAI_DEFAUT_S = 3600.0
# Corps : liste fermée des clés ; tout le reste refuse l'envoi.
CLES_CORPS = ("model", "max_tokens", "messages", "thinking", "output_config")
CLES_REGLAGE = ("max_tokens", "effort", "reflexion", "flux")
# Plafond de sortie au-delà duquel le flux est exigé (choix de code, prudent : au-delà, une réponse non en flux peut
# dépasser le délai d'une requête ; nœuds v2, A7 : « le flux est obligatoire pour 128 000 jetons de sortie »).
SEUIL_FLUX_JETONS = 16_000
REFLEXION_OMISE = "omise"
# Raisons d'arrêt (A6) et événements rendus au champ `refus["evenement"]`.
RAISON_OK = "end_turn"
RAISON_REFUS = "refusal"
EVENEMENT_REFUS_CLASSIFIEUR = "messages.stop_reason"
EVENEMENT_REPLI_FOURNISSEUR = "messages.repli_fournisseur"
EVENEMENT_MODELE_NON_PERMIS = "relais.modele_non_permis"
CATEGORIE_NON_LUE = "catégorie non lue"
# Erreurs (N2).
TYPE_FACTURATION = "billing_error"
TYPE_REQUETE_INVALIDE = "invalid_request_error"
# Fragment fixé du message d'un crédit épuisé rendu en 400 (forme reçue ce jour sur une clé ; vérification du lot 4 v2,
# B1) ; comparé sans casse, jamais recopié.
FRAGMENT_CREDIT_400 = "credit balance is too low"
ERREUR_CREDIT_AMONT = "crédit d'amont"
ERREUR_CREDIT_AMONT_400 = "crédit d'amont (400, message de solde)"
ERREUR_PLAFOND_RELAIS = "plafond du relais"
ERREUR_MODELE_RELAIS = "modèle non permis par le relais"
ERREUR_REPONSE_COUPEE = "réponse coupée au plafond de sortie"
ERREUR_RAISON_HORS_LISTE = "raison d'arrêt hors liste"
ERREUR_SANS_STATUT = "erreur sans statut (connexion ou délai)"
ERREUR_STATUT = "erreur de statut"
MESSAGE_PLAFOND_RELAIS = "plafond de dépense du relais atteint"
MESSAGE_MODELE_RELAIS = "modèle non permis"
NUMERO_ARRET_REGLAGE = 32  # proposé (projet d'additif v2, § 10) ; la mère le confirme à l'assemblage


class CorpsRefuse(ValueError):
    """Le corps à envoyer n'est pas celui de la règle (D2, A2) : rien ne part ; le message ne recopie aucun contenu."""


class RelanceCachee(RuntimeError):
    """A1 : le client relancerait de lui-même (`max_retries` différent de zéro) : rien ne part."""


class ReglageNonAdmisNA(ValueError):
    """N° 32 (proposé) : un réglage non textuel non admis pour un (rôle, modèle) ; le départ est refusé, le nom dit."""

    numero = NUMERO_ARRET_REGLAGE

    def __init__(self, role, modele, reglage, raison):
        super().__init__(f"arrêt n° {NUMERO_ARRET_REGLAGE} (proposé), réglage non admis : « {reglage} » pour le rôle "
                         f"« {role} » et le modèle « {modele} » ({raison}) ; départ refusé")
        self.role, self.modele, self.reglage = role, modele, reglage


class ConservationImpossible(RuntimeError):
    """La réponse brute d'une tentative n'a pas pu être écrite : rien n'est rendu sans copie."""


@dataclasses.dataclass
class ResultatDirectNA(Resultat):
    """Le résultat de l'adaptateur d'origine, plus la fiche de la tentative (`tentative`) : raison d'arrêt, catégorie,
    erreur (classe, statut, type), servie ou non, usage, nom du fichier de la réponse brute."""

    tentative: object = None


# --- réglages et barème (A7, A3) -----------------------------------------------------------------------------------------

def _entier_positif(v):
    return type(v) is int and v > 0


def lire_reglages_na(reglages, admis, modeles_admis):
    """Contrôle au départ (A7) : `reglages` = {rôle du kit: {modèle: {max_tokens, effort, reflexion, flux}}}, un jeu pour
    chaque rôle et chaque modèle admis ; `admis` = {modèle: {"max_tokens_max", "efforts", "reflexions"}}, la table versée.
    Rend {(rôle, modèle): jeu} ; un écart lève `ReglageNonAdmisNA` (n° 32, proposé) avec le nom du réglage."""
    if not isinstance(reglages, dict) or sorted(reglages) != sorted(ROLES_NA):
        raise ReglageNonAdmisNA("?", "?", "rôles", "un jeu pour chaque rôle du véhicule")
    if not isinstance(admis, dict):
        raise ReglageNonAdmisNA("?", "?", "table des valeurs admises", "absente")
    rendu = {}
    for role in ROLES_NA:
        par_modele = reglages[role]
        if not isinstance(par_modele, dict) or sorted(par_modele) != sorted(modeles_admis):
            raise ReglageNonAdmisNA(role, "?", "modèles", "un jeu pour chaque modèle admis, et seulement eux")
        for modele in modeles_admis:
            jeu, a = par_modele[modele], admis.get(modele)
            if not isinstance(a, dict) or not _entier_positif(a.get("max_tokens_max")) \
                    or not isinstance(a.get("efforts"), (list, tuple)) or not isinstance(a.get("reflexions"), (list, tuple)):
                raise ReglageNonAdmisNA(role, modele, "table des valeurs admises", "absente ou sans sa forme pour ce modèle")
            if not isinstance(jeu, dict) or sorted(jeu) != sorted(CLES_REGLAGE):
                raise ReglageNonAdmisNA(role, modele, "jeu", f"exactement {', '.join(CLES_REGLAGE)}")
            if not _entier_positif(jeu["max_tokens"]) or jeu["max_tokens"] > a["max_tokens_max"]:
                raise ReglageNonAdmisNA(role, modele, "max_tokens", "hors de la borne admise")
            if jeu["effort"] is not None and jeu["effort"] not in a["efforts"]:
                raise ReglageNonAdmisNA(role, modele, "effort", "valeur non admise pour ce modèle")
            if jeu["reflexion"] not in a["reflexions"]:
                raise ReglageNonAdmisNA(role, modele, "reflexion", "valeur non admise pour ce modèle")
            if type(jeu["flux"]) is not bool:
                raise ReglageNonAdmisNA(role, modele, "flux", "vrai ou faux")
            if jeu["max_tokens"] > SEUIL_FLUX_JETONS and not jeu["flux"]:
                raise ReglageNonAdmisNA(role, modele, "flux", f"exigé au-delà de {SEUIL_FLUX_JETONS} jetons de sortie")
            rendu[(role, modele)] = dict(jeu)
    return rendu


def lire_bareme_na(bareme, modeles_admis):
    """Barème versé, dollars par million de jetons : {modèle: [entrée, sortie, écriture de cache, lecture de cache]}, un par
    modèle admis, et seulement eux."""
    if not isinstance(bareme, dict) or sorted(bareme) != sorted(modeles_admis):
        raise ValueError("barème : un par modèle admis, et seulement eux")
    rendu = {}
    for m, t in bareme.items():
        if not isinstance(t, (list, tuple)) or len(t) != 4 or any(
                isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) or x < 0 for x in t):
            raise ValueError(f"barème de « {m} » : quatre montants finis, positifs")
        rendu[m] = tuple(float(x) for x in t)
    return rendu


def cout_par_usage(tarif, usage):
    """Coût d'après l'usage déclaré ; None si l'usage manque ou n'a pas sa forme (le coût est alors inconnu)."""
    if not isinstance(usage, dict):
        return None
    champs = ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
    valeurs = []
    for c in champs:
        v = usage.get(c)
        if v is None:
            v = 0
        if type(v) is not int or v < 0:
            return None
        valeurs.append(v)
    if "input_tokens" not in usage or "output_tokens" not in usage:
        return None
    return sum(v * t for v, t in zip(valeurs, tarif)) / 1_000_000


# --- le corps (D2, A2) ---------------------------------------------------------------------------------------------------

def construire_corps_na(modele, consigne, jeu):
    corps = {"model": modele, "max_tokens": jeu["max_tokens"], "messages": [{"role": "user", "content": consigne}]}
    if jeu["reflexion"] != REFLEXION_OMISE:
        corps["thinking"] = {"type": jeu["reflexion"]}
    if jeu["effort"] is not None:
        corps["output_config"] = {"effort": jeu["effort"]}
    return corps


def verifier_corps_na(corps, consigne, modele):
    """Le corps ne porte que la liste fermée ; le seul message est la consigne, de rôle « user », chaîne identique."""
    if not isinstance(corps, dict) or any(k not in CLES_CORPS for k in corps):
        raise CorpsRefuse("champ hors de la liste fermée du corps : rien ne part (D2, A2)")
    if corps.get("model") != modele or not _entier_positif(corps.get("max_tokens")):
        raise CorpsRefuse("modèle ou plafond de sortie du corps sans sa forme")
    m = corps.get("messages")
    if not isinstance(m, list) or len(m) != 1 or not isinstance(m[0], dict) or sorted(m[0]) != ["content", "role"] \
            or m[0]["role"] != "user" or type(m[0]["content"]) is not str or m[0]["content"] != consigne:
        raise CorpsRefuse("le corps ne porte pas la consigne seule, dans un message « user »")
    return corps


def octets_consigne_du_corps(corps_octets):
    """La consigne extraite du corps reçu (égalité à l'essai à blanc : CO l. 230), encodée en UTF-8."""
    objet = json.loads(corps_octets.decode("utf-8"))
    return objet["messages"][0]["content"].encode("utf-8")


# --- lecture d'une réponse ------------------------------------------------------------------------------------------------

def _dict_de(message):
    if isinstance(message, dict):
        return message
    for nom in ("to_dict", "model_dump"):
        f = getattr(message, nom, None)
        if callable(f):
            d = f()
            if isinstance(d, dict):
                return d
    raise TypeError("réponse sans forme lisible")


def trace_repli_fournisseur(m):
    """Vrai si la réponse porte une trace de repli du fournisseur : un bloc `fallback`, ou une itération `fallback_message`
    à l'usage."""
    contenu = m.get("content")
    if isinstance(contenu, list) and any(isinstance(b, dict) and b.get("type") == "fallback" for b in contenu):
        return True
    usage = m.get("usage")
    it = usage.get("iterations") if isinstance(usage, dict) else None
    return isinstance(it, list) and any(isinstance(e, dict) and e.get("type") == "fallback_message" for e in it)


def lire_reponse(m):
    """(statut, texte, raison, catégorie, classe d'erreur, événement de refus) d'un message lu (dict)."""
    raison = m.get("stop_reason")
    contenu = m.get("content") if isinstance(m.get("content"), list) else []
    texte = "".join(b.get("text") for b in contenu if isinstance(b, dict) and b.get("type") == "text"
                    and isinstance(b.get("text"), str))
    if trace_repli_fournisseur(m):
        return "refus", "", raison, None, None, EVENEMENT_REPLI_FOURNISSEUR
    if raison == RAISON_REFUS:
        details = m.get("stop_details")
        cat = details.get("category") if isinstance(details, dict) else None
        cat = cat if isinstance(cat, str) and cat.strip() else CATEGORIE_NON_LUE
        return "refus", "", raison, cat, None, EVENEMENT_REFUS_CLASSIFIEUR
    if raison == RAISON_OK:
        return "ok", texte, raison, None, None, None
    if raison == "max_tokens":
        return "erreur", "", raison, None, ERREUR_REPONSE_COUPEE, None
    return "erreur", "", raison if isinstance(raison, str) else None, None, ERREUR_RAISON_HORS_LISTE, None


def message_de_solde(corps):
    """Vrai si le message d'erreur du corps (`error.message`) contient le fragment fixé, sans casse ; rien n'est rendu du
    message lui-même."""
    err = corps.get("error") if isinstance(corps, dict) else None
    message = err.get("message") if isinstance(err, dict) else None
    return isinstance(message, str) and FRAGMENT_CREDIT_400.casefold() in message.casefold()


def classer_erreur(exc):
    """(classe, statut HTTP, type) d'une erreur du client ; aucun texte recopié."""
    statut = getattr(exc, "status_code", None)
    corps = getattr(exc, "body", None)
    type_ = getattr(exc, "type", None)
    if type_ is None and isinstance(corps, dict) and isinstance(corps.get("error"), dict):
        type_ = corps["error"].get("type")
    if type(statut) is not int:
        return ERREUR_SANS_STATUT, None, None
    if statut == 402 and type_ == TYPE_FACTURATION:
        return ERREUR_CREDIT_AMONT, statut, type_
    if statut == 400 and type_ == TYPE_REQUETE_INVALIDE and message_de_solde(corps):
        return ERREUR_CREDIT_AMONT_400, statut, type_
    if statut == 402 and isinstance(corps, dict) and corps.get("erreur") == MESSAGE_PLAFOND_RELAIS:
        return ERREUR_PLAFOND_RELAIS, statut, None
    if statut == 403 and isinstance(corps, dict) and corps.get("erreur") == MESSAGE_MODELE_RELAIS:
        return ERREUR_MODELE_RELAIS, statut, None
    return ERREUR_STATUT, statut, type_ if isinstance(type_, str) else None


# --- le client ------------------------------------------------------------------------------------------------------------

def fabrique_client_reel(url_relais, delai_s):
    """Le client réel de l'interface des messages : relais local, jeton factice, `max_retries=0`, sans variable de
    l'environnement (aucun mandataire réseau, adresse donnée)."""
    import anthropic  # noqa: PLC0415 — importé seulement pour le client réel
    client = anthropic.Anthropic(base_url=url_relais, api_key=JETON_FACTICE, max_retries=0, timeout=delai_s,
                                 default_headers={"x-api-key": JETON_FACTICE},
                                 http_client=anthropic.DefaultHttpxClient(trust_env=False))
    return client, (anthropic.APIError,)


def _verifier_sans_relance(client):
    if getattr(client, "max_retries", None) != 0:
        raise RelanceCachee("A1 : le client doit être construit avec max_retries=0 ; rien ne part")


class AdaptateurClaudeDirectNA(Adaptateur):
    """Moteur réel du véhicule pour les clés Claude : une requête par tentative, au travers du relais de la clé."""

    nom = NOM_ADAPTATEUR

    def __init__(self, url_relais, dossier_reponses, *, modeles_admis, reglages, admis, bareme, environnement=None,
                 arme=False, delai_s=DELAI_DEFAUT_S, fabrique_client=None):
        self.url_relais = valider_url_relais(url_relais)
        if not isinstance(dossier_reponses, str) or not os.path.isabs(dossier_reponses) or not os.path.isdir(dossier_reponses):
            raise ValueError("dossier des réponses brutes : un dossier absolu existant (dans le dossier de sortie)")
        if not isinstance(modeles_admis, (list, tuple)) or not modeles_admis or len(set(modeles_admis)) != len(modeles_admis) \
                or any(not isinstance(m, str) or not m for m in modeles_admis):
            raise ValueError("modèles admis : une liste fermée de noms, sans doublon")
        if isinstance(delai_s, bool) or not isinstance(delai_s, (int, float)) or not delai_s > 0:
            raise ValueError("delai_s : nombre strictement positif (secondes)")
        self.modeles_admis = tuple(modeles_admis)
        self.reglages = lire_reglages_na(reglages, admis, self.modeles_admis)
        self.bareme = lire_bareme_na(bareme, self.modeles_admis)
        self.dossier_reponses = os.path.normpath(dossier_reponses)
        self._environnement = environnement
        self.arme = arme
        self.delai_s = float(delai_s)
        fabrique = fabrique_client if fabrique_client is not None else fabrique_client_reel
        self._client, self._erreurs_api = fabrique(self.url_relais, self.delai_s)
        self._erreurs_api = tuple(self._erreurs_api)
        _verifier_sans_relance(self._client)

    # --- conservation (A4) ---------------------------------------------------------------------------------------------

    def _conserver(self, dossier, contenu):
        session = os.path.basename(os.path.normpath(dossier))
        octets = (json.dumps(dict(contenu, format=FORMAT_REPONSE, session=session), ensure_ascii=False, sort_keys=True,
                             indent=1, default=str) + "\n").encode("utf-8")
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
                return nom
        except OSError as e:
            raise ConservationImpossible(f"réponse brute non conservée ({type(e).__name__}) : rien n'est rendu sans "
                                         "copie") from None
        raise ConservationImpossible("trop de réponses brutes pour une même session : rien n'est rendu sans copie")

    # --- l'envoi ---------------------------------------------------------------------------------------------------------

    def _envoyer(self, corps, flux, recu):
        """Rend (message lu en dict, corps brut). `recu["octets"]` passe à vrai dès qu'une réponse a commencé."""
        messages = self._client.messages
        if flux:
            evenements = []
            with messages.stream(**corps) as flot:
                recu["octets"] = True
                for ev in flot:
                    evenements.append(_dict_de(ev))
                final = _dict_de(flot.get_final_message())
            return final, {"flux": evenements, "message_final": final}
        brut = messages.with_raw_response.create(**corps)
        recu["octets"] = True
        texte = brut.http_response.text
        return _dict_de(brut.parse()), {"corps_http": texte}

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        environnement = os.environ if self._environnement is None else self._environnement
        presents = noms_de_cle_presents(environnement)
        if presents:
            raise CleDansEnvironnement("variables de clé présentes dans l'environnement de l'orchestrateur ("
                                       + ", ".join(presents) + ") : la clé doit rester dans le relais du noyau")
        if not self.arme:
            raise MoteurNonArme("moteur réel non armé : aucun appel n'est fait (essais, simulation)")
        if role not in ROLES_NA:
            raise ValueError(f"rôle du véhicule : {ROLES_NA}")
        if modele not in self.modeles_admis:
            raise ModeleNonPermis("modèle hors de la liste fermée de l'adaptateur direct")
        if max_tours != 1:
            raise ValueError("un seul tour par tentative")
        if not isinstance(consigne, str):
            raise TypeError("la consigne est une chaîne")
        if isinstance(budget_usd, bool) or not isinstance(budget_usd, (int, float)) or not budget_usd > 0:
            raise ValueError("plafond de la tentative : strictement positif")
        jeu = self.reglages[(role, modele)]
        corps = verifier_corps_na(construire_corps_na(modele, consigne, jeu), consigne, modele)
        octets_corps = json.dumps(corps, ensure_ascii=False, sort_keys=True).encode("utf-8")
        _verifier_sans_relance(self._client)
        base = {"modele_demande": modele, "role_kit": role, "corps_sha256": hashlib.sha256(octets_corps).hexdigest(),
                "corps_taille": len(octets_corps), "reglages": dict(jeu)}
        recu = {"octets": False}
        try:
            m, brut = self._envoyer(corps, jeu["flux"], recu)
        except self._erreurs_api as e:
            classe, statut_http, type_ = classer_erreur(e)
            inconnu = classe == ERREUR_SANS_STATUT or recu["octets"]
            cout = float(budget_usd) if inconnu else 0.0
            corps_erreur = getattr(e, "body", None)
            tentative = dict(base, servie=False, raison_arret=None, categorie=None, classe_erreur=classe,
                             statut_http=statut_http, type_erreur=type_, usage=None, cout_inconnu=inconnu)
            if classe == ERREUR_MODELE_RELAIS:
                refus = {"motif": "modèle refusé par le relais", "modele_demande": modele, "modele_servi": None,
                         "evenement": EVENEMENT_MODELE_NON_PERMIS, "categorie": None}
                statut = "refus"
            else:
                refus, statut = None, "erreur"
            nom = self._conserver(dossier, dict(tentative, statut=statut, corps_brut={"erreur": corps_erreur},
                                                cout_declare_usd=cout))
            tentative["reponse_brute"] = nom
            return ResultatDirectNA("", lister_fichiers(dossier), cout, statut, f"{classe} ({statut_http})",
                                    texte_brut=None, refus=refus, modele_servi=None, cout_inconnu=inconnu,
                                    tentative=tentative)
        except BaseException as e:
            self._conserver(dossier, dict(base, statut="exception", erreur=type(e).__name__, corps_brut=None,
                                          cout_declare_usd=None, cout_inconnu=True))
            raise
        statut, texte, raison, categorie, classe, evenement = lire_reponse(m)
        servi = m.get("model") if isinstance(m.get("model"), str) and m.get("model") else None
        usage = m.get("usage")
        cout = cout_par_usage(self.bareme[modele], usage)
        inconnu = cout is None
        cout = float(budget_usd) if inconnu else cout
        tentative = dict(base, servie=raison != RAISON_REFUS and evenement != EVENEMENT_REPLI_FOURNISSEUR,
                         raison_arret=raison, categorie=categorie, classe_erreur=classe, statut_http=200,
                         type_erreur=None, usage=usage if isinstance(usage, dict) else None, cout_inconnu=inconnu)
        refus = None
        if statut == "refus":
            refus = {"motif": "refus de classifieur" if evenement == EVENEMENT_REFUS_CLASSIFIEUR
                     else "trace de repli du fournisseur", "modele_demande": modele, "modele_servi": servi,
                     "evenement": evenement, "categorie": categorie}
        nom = self._conserver(dossier, dict(tentative, statut=statut, modele_servi=servi, corps_brut=brut,
                                            cout_declare_usd=cout))
        tentative["reponse_brute"] = nom
        return ResultatDirectNA(caviarder(texte)[0] if texte else "", lister_fichiers(dossier), cout, statut,
                                classe, texte_brut=texte if statut == "ok" else None, refus=refus, modele_servi=servi,
                                cout_inconnu=inconnu, tentative=tentative)


__all__ = ("AdaptateurClaudeDirectNA", "ResultatDirectNA", "CorpsRefuse", "RelanceCachee", "ReglageNonAdmisNA",
           "ConservationImpossible", "lire_reglages_na", "lire_bareme_na", "construire_corps_na", "verifier_corps_na",
           "octets_consigne_du_corps", "lire_reponse", "classer_erreur", "cout_par_usage", "fabrique_client_reel",
           "NOM_ADAPTATEUR", "EVENEMENT_REFUS_CLASSIFIEUR", "EVENEMENT_REPLI_FOURNISSEUR", "EVENEMENT_MODELE_NON_PERMIS",
           "CATEGORIE_NON_LUE", "ERREUR_CREDIT_AMONT", "ERREUR_CREDIT_AMONT_400", "ERREUR_PLAFOND_RELAIS", "ROLES_NA",
           "FRAGMENT_CREDIT_400", "message_de_solde")
