"""Aides des essais du lot 4 du véhicule NA-1 (lisent `routage_na_v1`, `appel_garde_na_v1`, `adaptateur_claude_na_v1`) :
données factices seules, noms de clés neutres (`cle_a` … `cle_d`, `cle_sans_part`, `hors_course`), aucune clé, aucun appel.

- Les tables d'essai : celle de la course (même forme de routage que la table de la conception v5, § 2.3 : la clé `cle_a`
  porte le juge et le proposeur de l'espèce 3, la clé `cle_b` l'aiguilleur et le proposeur de l'espèce 4, la clé `cle_c`
  le juge de l'espèce 1 et les proposeurs des espèces 1 et 5, sur deux adaptateurs, la clé `cle_d` le proposeur de
  l'espèce 2 ; une clé sans part, sans rôle ; `hors_course` et un lecteur d'étiquettes jamais appelé), les deux tables des
  lignes à part (épreuve des témoins, sonde de refus), et la table plantée de D11, marquée « artefact ».
- `NoyauEssai` : une classe de base qui porte **le vrai `appel` du noyau** (`OrchestreV56.appel`) et ce qu'il lit (suivi des
  rôles v54, plafonds de session, coffre de consommations, sessions dans un dossier temporaire) ; la génération d'essai est
  `GenerationEssai(AppelGardeNA, NoyauEssai)`.
- `AdaptateurEnregistreur` : garde chaque consigne reçue (la chaîne même que le noyau remet) et rend un `Resultat` réglé.
- `FauxKit` : imite l'interface du kit d'agent que lit l'adaptateur, sans aucun appel ; garde les options reçues.
- Les requêtes : celles du lot 3 (`aides_na_lot3_v3`), la garde : celle du lot 2 (`aides_na_v4.garde_essai`).
"""

import hashlib
import json
import os
import sys
import tempfile
import time

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE_ORCHESTRATEUR = os.path.dirname(ICI)
for _p in (ICI, RACINE_ORCHESTRATEUR):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import aides_na_lot3_v3 as L3  # noqa: E402
import aides_na_v4 as A  # noqa: E402
from pole import appel_garde_na_v1 as ag  # noqa: E402
from pole import journal_na_v3 as jn  # noqa: E402
from pole import noyau_v56 as nv  # noqa: E402
from pole import requete_na_v3 as rq  # noqa: E402
from pole import routage_na_v1 as rt  # noqa: E402
from pole.adaptateurs import Resultat  # noqa: E402
from pole.suivi_roles_v54 import SuiviRoles  # noqa: E402

PARTS = {"cle_a": 156.56, "cle_b": 125.63, "cle_c": 140.39, "cle_d": 17.01}
PIRE_PROPOSEUR, PIRE_AIGUILLEUR, PIRE_JUGE = 6.05, 0.25, 0.60
RELAIS_A, RELAIS_B = "http://127.0.0.1:9", "http://127.0.0.1:10"
MODELE_ESSAI = "modele-essai-inerte"
PLAFONDS_SESSION = {"proposeur": 6.05, "aiguilleur": 0.25, "juge": 0.60}
ARRETS_ESSAI = {"a3_echecs_consecutifs": 3, "a3_delai_s": {"*": 1800}, "a14_part_max": 0.34, "a11_modeles": []}
ROLES = {  # étiquette : (sorte, espèce, clé, adaptateur)
    "juge-espece-3": ("juge", 3, "cle_a", "ad_a"),
    "proposeur-espece-3": ("proposeur", 3, "cle_a", "ad_a"),
    "aiguilleur": ("portier", 4, "cle_b", "ad_b"),
    "proposeur-espece-4": ("proposeur", 4, "cle_b", "ad_b"),
    "juge-espece-1": ("juge", 1, "cle_c", "ad_c1"),
    "proposeur-espece-1": ("proposeur", 1, "cle_c", "ad_c1"),
    "proposeur-espece-5": ("proposeur", 5, "cle_c", "ad_c2"),
    "proposeur-espece-2": ("proposeur", 2, "cle_d", "ad_d"),
    "lecteur-etiquettes-1": ("juge", 1, "hors_course", "hors_course"),
}
ADAPTATEURS = ("ad_a", "ad_b", "ad_c1", "ad_c2", "ad_d", "ad_sans_part", "hors_course", "ad_x")


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def cles_course(parts=True, en_plus=()):
    p = PARTS if parts else {k: None for k in PARTS}
    return [
        {"nom": "cle_a", "type": "claude_sdk", "part_usd": p["cle_a"], "adaptateurs": ["ad_a"], "relais": RELAIS_A},
        {"nom": "cle_b", "type": "claude_sdk", "part_usd": p["cle_b"], "adaptateurs": ["ad_b"], "relais": RELAIS_B},
        {"nom": "cle_c", "type": "commande_externe", "part_usd": p["cle_c"], "adaptateurs": ["ad_c1", "ad_c2"],
         "relais": None},
        {"nom": "cle_d", "type": "kimi_protocole", "part_usd": p["cle_d"], "adaptateurs": ["ad_d"], "relais": None},
        {"nom": "cle_sans_part", "type": "aucun", "part_usd": None, "adaptateurs": ["ad_sans_part"], "relais": None},
        {"nom": "hors_course", "type": "aucun", "part_usd": None, "adaptateurs": ["hors_course"], "relais": None},
    ] + list(en_plus)


def objet_table_course(roles=None):
    roles = ROLES if roles is None else roles
    return {"format": rt.FORMAT_TABLE, "marque": "course", "nom": "course", "plafond_ligne_usd": None,
            "cles": cles_course(), "roles": [{"role": r, "sorte": s, "espece": e, "cle": c, "adaptateur": a}
                                             for r, (s, e, c, a) in ROLES.items() if r in roles]}


def objet_table_artefact():
    """D11 : la table plantée, jamais chargée par la course ; le juge et le proposeur de l'espèce 3 sur deux clés."""
    o = objet_table_course()
    o["marque"] = "artefact"
    o["cles"].append({"nom": "cle_x", "type": "claude_sdk", "part_usd": 10.0, "adaptateurs": ["ad_x"], "relais": RELAIS_A})
    for r in o["roles"]:
        if r["role"] == "juge-espece-3":
            r["cle"], r["adaptateur"] = "cle_x", "ad_x"
    return o


def objet_table_ligne(nom, plafond, roles):
    cles = [dict(c, part_usd=None) for c in cles_course() if c["nom"] not in ("hors_course",)]
    return {"format": rt.FORMAT_TABLE, "marque": "ligne à part", "nom": nom, "plafond_ligne_usd": plafond, "cles": cles,
            "roles": [{"role": r, "sorte": s, "espece": e, "cle": c, "adaptateur": a} for r, (s, e, c, a) in roles.items()]}


def objet_table_temoins():
    """Épreuve des témoins (conception v5, § 2.10) : le portier et le juge de l'espèce 3 sur la clé de l'espèce 3 ; le juge
    de l'espèce 1 sur la clé du deuxième relais ; plafond 5 USD."""
    return objet_table_ligne("épreuve des témoins", 5.0, {
        "aiguilleur": ("portier", 4, "cle_a", "ad_a"), "juge-espece-3": ("juge", 3, "cle_a", "ad_a"),
        "juge-espece-1": ("juge", 1, "cle_c", "ad_c1")})


def objet_table_sonde():
    """Sonde de refus (§ 2.10) : espèces 3 et 4 sur la clé de l'espèce 3 ; 1 et 5 sur le deuxième relais ; 2 sur le
    troisième ; plafond 1 USD."""
    return objet_table_ligne("sonde de refus", 1.0, {
        "proposeur-espece-3": ("proposeur", 3, "cle_a", "ad_a"), "proposeur-espece-4": ("proposeur", 4, "cle_a", "ad_a"),
        "proposeur-espece-1": ("proposeur", 1, "cle_c", "ad_c1"), "proposeur-espece-5": ("proposeur", 5, "cle_c", "ad_c2"),
        "proposeur-espece-2": ("proposeur", 2, "cle_d", "ad_d")})


def octets_table(objet):
    o = json.dumps(objet, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return o, sha(o)


def table(objet=None, marque="course"):
    o, s = octets_table(objet if objet is not None else objet_table_course())
    return rt.lire_table(o, s, marque)


PIRE_LIGNE_A_PART = 0.20  # valeur d'essai, sous le plafond de chaque ligne à part


def pires(t):
    rendu = {}
    for r, e in t.roles.items():
        if e.cle == rt.CLE_HORS_COURSE:
            continue
        if t.marque == rt.MARQUE_LIGNE_A_PART:
            rendu[r] = PIRE_LIGNE_A_PART
            continue
        rendu[r] = {"proposeur": PIRE_PROPOSEUR, "portier": PIRE_AIGUILLEUR, "juge": PIRE_JUGE}[e.sorte]
    return rendu


def parts(t):
    if t.marque == rt.MARQUE_LIGNE_A_PART:
        return {}
    return {c: PARTS[c] if c in PARTS else t.cles[c].part_micro / rt.MICRO
            for c in sorted({e.cle for e in t.roles.values() if e.cle != rt.CLE_HORS_COURSE})}


# --- requêtes factices (lot 3) -----------------------------------------------------------------------------------------

def cases():
    return L3.cases()


def requete_proposeur(generation=1, indice=0, synthese_octets=A.SYNTHESE_FACTICE):
    c = cases()[str(generation)][indice]
    if generation == 1:
        return rq.assembler_proposeur(L3.gabarit(), c, L3.synthese(synthese_octets), 1)
    return rq.assembler_proposeur(L3.gabarit(), c, L3.synthese(synthese_octets), generation, L3.registre(),
                                  L3.TITRE_REGISTRE_FACTICE)


def requete_juge(generation=1, indice=0):
    c = cases()[str(generation)][indice]
    return rq.assembler_juge(L3.consigne_juge(), L3.contenu_fiche(c), L3.identifiant_juge(), c.identifiant, generation)


def requete_portier(generation=1, indice=0):
    c = cases()[str(generation)][indice]
    return rq.assembler_portier_fiche(L3.consigne_portier(), L3.contenu_fiche(c), c.identifiant, generation)


def requete_portier_sans_fiche(generation=1, indice=0):
    c = cases()[str(generation)][indice]
    return rq.assembler_portier_reponse_sans_fiche(L3.consigne_portier(), "Réponse factice, inerte, sans fiche.",
                                                   c.identifiant, generation)


def session_de(requete, etape="proposition", role="role"):
    """Une session d'essai ; la fonction de case du contexte la rend à l'identifiant de la case de la requête."""
    return (etape, requete.identifiant_case, role)


def case_de_session(session):
    return session[1]


# --- le noyau d'essai -------------------------------------------------------------------------------------------------

class CoffreEssai:
    def __init__(self):
        self._consommations = []

    def noter_consommation(self, etape, role, cout_usd, **champs):
        self._consommations.append(dict({"etape": etape, "role": role, "cout_usd": float(cout_usd)}, **champs))

    def consommations(self):
        return [dict(c) for c in self._consommations]


class NoyauEssai:
    """Ce que lit `OrchestreV56.appel`, et rien d'autre ; `appel` est celui du noyau, inchangé."""

    appel = nv.OrchestreV56.appel
    _arreter_role_a2 = nv.OrchestreV56._arreter_role_a2

    def __init__(self, adaptateurs, dossier):
        self.ad = adaptateurs
        self.ps = dict(PLAFONDS_SESSION)
        self.suivi = SuiviRoles(ARRETS_ESSAI, horloge=time.monotonic)
        self.horloge = time.monotonic
        self.coffre = CoffreEssai()
        self.appels_sautes, self.roles_arretes_a2, self.evenements = {}, {}, []
        self.racine_sessions = os.path.join(dossier, "sessions")
        os.makedirs(self.racine_sessions, exist_ok=True)

    def ev(self, type_, **champs):
        self.evenements.append(dict(champs, type=type_))

    def session(self, *logique):
        d = os.path.join(self.racine_sessions, sha("/".join(map(str, logique)).encode("utf-8"))[:16])
        os.makedirs(d, exist_ok=True)
        return d


class GenerationEssai(ag.AppelGardeNA, NoyauEssai):
    pass


class AdaptateurEnregistreur:
    """Garde la chaîne reçue ; rend un `Resultat` réglé (`reglages` : liste consommée, puis le défaut)."""

    nom = "enregistreur"

    def __init__(self, cout=0.01, reglages=None):
        self.recus, self.cout, self.reglages = [], cout, list(reglages or [])

    def lancer(self, role, consigne, dossier, budget_usd, max_tours, modele=None):
        self.recus.append({"role_kit": role, "consigne": consigne, "budget": budget_usd, "modele": modele})
        r = dict(self.reglages.pop(0)) if self.reglages else {}
        if r.pop("lever", None):
            raise RuntimeError("panne d'adaptateur d'essai")
        r.setdefault("texte_final", "texte factice inerte")
        r.setdefault("statut", "ok")
        r.setdefault("cout_declare_usd", self.cout)
        r.setdefault("modele_servi", modele if r["statut"] == "ok" else None)
        r.setdefault("texte_brut", r["texte_final"])
        return Resultat(**r)


def adaptateurs(**reglages):
    return {n: AdaptateurEnregistreur(reglages=reglages.get(n)) for n in ADAPTATEURS}


class Montage:
    """Une génération d'essai et tout ce qu'elle lit, dans un dossier temporaire neuf."""

    def __init__(self, objet=None, marque="course", generation=1, portee_arret_1="appel", etat_relais=None, cumul=None,
                 reglages=None, journal_nom="journal-requetes-g1.jsonl"):
        self.dossier = tempfile.mkdtemp(prefix="essais-na-lot4-")
        self.sortie = os.path.join(self.dossier, "sortie")
        os.makedirs(self.sortie)
        self.table = table(objet, marque)
        self.journal = jn.JournalRequetes(self.sortie, journal_nom)
        self.garde = A.garde_essai()
        self.cumul = cumul if cumul is not None else rt.CumulParCle(self.table)
        self.lectures_relais = []
        etat = etat_relais if etat_relais is not None else etat_relais_sain()

        def lire_etat(cle):
            self.lectures_relais.append(cle)
            if isinstance(etat, Exception):
                raise etat
            return dict(etat)

        self.contexte = ag.ContexteAppelGardeNA(
            numero_generation=generation if self.table.marque == rt.MARQUE_COURSE else None, table=self.table,
            parts=parts(self.table), pires_par_role=pires(self.table), journal=self.journal, garde=self.garde,
            identifiant_case_de_session=case_de_session, cumul=self.cumul, lire_etat_relais=lire_etat,
            portee_arret_1=portee_arret_1)
        self.ad = adaptateurs(**(reglages or {}))
        self.gen = GenerationEssai(self.ad, self.dossier, contexte_na=self.contexte)

    def etat(self, reste=50.0, cout=0.0):
        return {"cout": cout, "reste": reste, "coupee": False, "etape": "proposition", "plafond_dur_usd": reste}

    def appeler(self, role, requete, fournisseur=None, etat=None, session=None, plafond_role=None, modele=MODELE_ESSAI,
                lire=None):
        e = self.table.entree(role)
        fournisseur = fournisseur if fournisseur is not None else e.adaptateur
        plafond_role = plafond_role or {"proposeur": "proposeur", "portier": "aiguilleur", "juge": "juge"}[
            e.sorte if e is not None else "juge"]
        role_kit = "proposeur_ideation" if (e is not None and e.sorte == "proposeur") else "juge_ideation"
        self.dernier_etat = etat if etat is not None else self.etat()
        return self.gen.appel(self.dernier_etat, role=role, role_kit=role_kit, fournisseur=fournisseur, modele=modele,
                              consigne=requete,
                              plafond_role=plafond_role,
                              session=session if session is not None else session_de(requete, role=role), lire=lire)

    def lignes(self):
        return jn.verifier_journal(self.journal.chemin)

    def recus(self):
        return [r for a in self.ad.values() for r in a.recus]


def etat_relais_sain():
    return {"plafond_usd": 156.56, "depense_usd": 3.0, "engage_usd": 0.0, "reserve_par_appel_usd": 0.4, "refus": 0,
            "refus_modele": 0, "appels": 5, "restant_usd": 153.56}


def etat_relais_credit():
    return {"plafond_usd": 156.56, "depense_usd": 156.40, "engage_usd": 0.0, "reserve_par_appel_usd": 0.4, "refus": 1,
            "refus_modele": 0, "appels": 300, "restant_usd": 0.16}


# --- le faux kit d'agent (adaptateur Claude neuf) -----------------------------------------------------------------------

class FauxKit:
    """L'interface du kit que lit l'adaptateur (`ClaudeAgentOptions`, `HookMatcher`, `query`, messages), sans aucun appel.
    `script` : les messages à rendre, construits par les fonctions ci-dessous."""

    class ClaudeSDKError(Exception):
        pass

    class ClaudeAgentOptions:
        def __init__(self, **reglages):
            self.__dict__.update(reglages)
            self.reglages = dict(reglages)

    class HookMatcher:
        def __init__(self, matcher=None, hooks=()):
            self.matcher, self.hooks = matcher, list(hooks)

    class TextBlock:
        def __init__(self, text):
            self.text = text

    class AssistantMessage:
        def __init__(self, content, model=None, stop_reason=None, usage=None):
            self.content, self.model, self.stop_reason, self.usage = content, model, stop_reason, usage

    class SystemMessage:
        def __init__(self, subtype, data):
            self.subtype, self.data = subtype, data

    class ResultMessage:
        def __init__(self, subtype, result, total_cost_usd, is_error=False, stop_reason=None, model_usage=None):
            self.subtype, self.result, self.total_cost_usd, self.is_error = subtype, result, total_cost_usd, is_error
            self.stop_reason, self.model_usage = stop_reason, model_usage

    def __init__(self, script=None, lever=None):
        self.script, self.lever, self.options_recues, self.consignes_recues = script, lever, [], []

    async def query(self, prompt, options):
        self.options_recues.append(options)
        self.consignes_recues.append(prompt)
        if self.lever is not None:
            raise self.lever
        for m in (self.script(self) if callable(self.script) else []):
            yield m


def script_normal(texte="Réponse factice inerte."):
    def s(kit):
        modele = kit.options_recues[-1].model
        return [kit.AssistantMessage([kit.TextBlock(texte)], model=modele, stop_reason="end_turn"),
                kit.ResultMessage("success", texte, 0.02)]
    return s


def script_refus():
    def s(kit):
        modele = kit.options_recues[-1].model
        return [kit.AssistantMessage([kit.TextBlock("")], model=modele, stop_reason="refusal")]
    return s


def script_erreur():
    def s(kit):
        return [kit.ResultMessage("error_during_execution", "erreur factice inerte", 0.0, is_error=True)]
    return s
