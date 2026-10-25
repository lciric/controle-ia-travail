"""Couche d'appel des espèces (étage commun à M3, M2, M1, M0).

Corrige, par rapport à `run_quadruple_fusee_omega_alpha_gamma_beta.py` :
- B-01 : les clés venaient de `~/.env.collider.json` (`RR_ANTHROPIC_API_KEY`, clés d'un autre projet) ; ici les
  appelants sont ceux du collisionneur v2.5 de Lazar, qui lisent `ANTHROPIC_API_KEY` et `GEMINI_API_KEY` dans
  l'environnement, ou des doubles fournis par l'appelant (tests, simulation) ;
- B-02 : la bascule silencieuse de modèle (Fable → Sonnet 3.5 → Gemini) est supprimée : une espèce = un identifiant
  de modèle ; un modèle servi non conforme est un échec consigné, jamais une réponse ;
- B-03 : une erreur n'est jamais renvoyée comme texte de réponse : chaque appel rend un `Resultat` avec un statut ;
- B-04 : chaque appel est journalisé (modèle demandé, modèle servi, raison d'arrêt, usage, coût, empreintes, heures,
  types des blocs de la réponse — R-402) ;
- B-25 : aucune clé dans une adresse ni dans un journal ;
- B-27 : plafond de dépense en dollars, vérifié avant (pire cas) et après (coût réel) chaque appel ;
- température : les appelants v2.5 n'en prennent pas (choix de Lazar) ; la valeur de Halton de Gemini devient un
  « angle d'exploration » écrit dans la consigne et consigné dans le journal (B-15).
"""
from __future__ import annotations

import dataclasses
import datetime as _dt
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import sys
import threading

ICI = pathlib.Path(__file__).resolve().parent
RACINE_OUTILS = ICI.parents[2]  # racine de la branche des outils (…/essaim-m3-refonte-v1/essaim_m3/noyau → …/)
CHEMIN_COLLISIONNEUR_DEFAUT = RACINE_OUTILS / "collisionneur-v2.5-banc-jev-travail" / "collisionneur_v2.py"

# Empreinte attendue du collisionneur v2.5 (LISEZMOI de la branche des outils) : toute différence est signalée.
EMPREINTE_COLLISIONNEUR_V25 = "213b52ef81eb4c9adfc2ac559cd68de9d706257063c7c6e137cb6264adee55fd"


def charger_collisionneur(chemin: str | os.PathLike | None = None):
    """Importe `collisionneur_v2` par son chemin (variable `ESSAIM_M3_COLLISIONNEUR`, sinon le dossier voisin)."""
    chemin = pathlib.Path(chemin or os.environ.get("ESSAIM_M3_COLLISIONNEUR") or CHEMIN_COLLISIONNEUR_DEFAUT)
    if not chemin.exists():
        raise FileNotFoundError(f"collisionneur_v2.py introuvable : {chemin}")
    if "collisionneur_v2" in sys.modules:
        return sys.modules["collisionneur_v2"]
    spec = importlib.util.spec_from_file_location("collisionneur_v2", chemin)
    module = importlib.util.module_from_spec(spec)
    sys.modules["collisionneur_v2"] = module
    spec.loader.exec_module(module)
    module.__empreinte_fichier__ = hashlib.sha256(chemin.read_bytes()).hexdigest()
    return module


cv = charger_collisionneur()

# Les trois « lignées souveraines » de Gemini, rattachées aux lettres du collisionneur (et à leur famille de
# fournisseur : Fable et Opus sont de la même famille, B-24 / constat 39 de l'essaim d'inspection).
ESPECES = {
    "CLAUDE_FABLE_5_1": {"lettre": "A", "famille": "anthropic"},
    "CLAUDE_OPUS_5_5": {"lettre": "B", "famille": "anthropic"},
    "GEMINI_ARGON": {"lettre": "C", "famille": "gemini"},
}
STATUTS_OK = ("OK",)


def modele_de(espece: str) -> dict:
    if espece not in ESPECES:
        raise KeyError(f"espèce inconnue : {espece!r} (connues : {sorted(ESPECES)})")
    return cv.MODELES[ESPECES[espece]["lettre"]]


def famille_de(espece: str) -> str:
    return ESPECES[espece]["famille"]


def maintenant() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def empreinte(texte: str) -> str:
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


# CE3-05 étendu (R-395) : le crédit épuisé arrive en HTTP 402 (Gemini) ou, chez Anthropic, en HTTP 400 — parfois en
# erreur de flux sous HTTP 200 — avec « credit balance is too low » (constaté au pilote du 25 octobre 2026) ; une autre
# erreur 400 n'arrête rien
_MOTIF_CREDIT_EPUISE = re.compile(r"credit balance is too low", re.IGNORECASE)


def credit_epuise(echec) -> bool:
    """Vrai si l'échec d'un appel dit que le crédit du fournisseur est épuisé (la course s'arrête, CE3-05)."""
    s = str(echec or "")
    return bool(re.match(r"\s*HTTP 402\b", s) or _MOTIF_CREDIT_EPUISE.search(s))


class Arret(Exception):
    """Arrêt du run (plafond atteint, journal illisible…) : jamais un repli silencieux."""


@dataclasses.dataclass
class Resultat:
    """Ce que rend chaque appel : jamais un texte d'erreur déguisé en réponse (B-03)."""
    identifiant: str
    espece: str
    statut: str            # OK, VIDE, TRONQUE, REFUS, ANOMALIE, ECHEC_API, MODELE_NON_CONFORME
    texte: str = ""
    modele_demande: str = ""
    modele_servi: object = None
    fin: object = None
    categorie: object = None
    usage: dict = dataclasses.field(default_factory=lambda: {"entree": 0, "sortie": 0})
    cout_usd: float = 0.0
    echec: object = None
    angle: object = None

    @property
    def ok(self) -> bool:
        return self.statut in STATUTS_OK


class Appelant:
    """Un appelant par run : journal, fichiers d'appel, plafond, doubles.

    `appelants` : {"anthropic": f, "gemini": f} avec f(modele_id, prompt, max_tokens) -> cv.Reponse.
    Sans `appelants`, ce sont ceux du collisionneur v2.5 (réseau réel) ; le mode réel n'est permis que si
    `reel=True` et qu'un identifiant de GO est donné (la vérification du GO est faite par l'orchestrateur).
    """

    def __init__(self, dossier: str | os.PathLike, plafond_usd: float, appelants: dict | None = None,
                 reel: bool = False, go_id: str | None = None):
        self.dossier = pathlib.Path(dossier)
        (self.dossier / "appels").mkdir(parents=True, exist_ok=True)
        self.journal = self.dossier / "journal-appels.jsonl"
        self.plafond_usd = float(plafond_usd)
        self.depense_usd = 0.0
        self.engage_usd = 0.0  # pire cas des appels en vol (appels parallèles) : réservé avant, libéré après
        self.credit_epuise: dict | None = None  # CE3-05 : premier crédit épuisé (HTTP 402, ou 400 de crédit, R-395) ; la course s'arrête
        self.compteur = 0
        self.reel = bool(reel)
        self.go_id = go_id
        self._verrou = threading.Lock()  # protège plafond, engagement, compteur et journal ; jamais l'appel réseau
        if appelants is None:
            if not self.reel:
                raise Arret("aucun appelant fourni et mode réel non demandé : rien n'est appelé")
            if not self.go_id:
                raise Arret("mode réel sans identifiant de GO : refusé (nœud de dépense)")
            appelants = cv.APPELANTS
        self.appelants = appelants

    # ---- plafond ----
    def _reserver(self, prix, prompt: str, max_tokens: int) -> float:
        """Sous verrou : refuse si dépense + engagé + pire cas dépasse le plafond ; sinon engage le pire cas."""
        pire = cv.cout_pire_cas(prix, len(prompt), max_tokens)
        if self.depense_usd + self.engage_usd + pire > self.plafond_usd:
            raise Arret(f"plafond {self.plafond_usd:.2f} USD : dépense {self.depense_usd:.2f} + en vol {self.engage_usd:.2f} + pire cas {pire:.2f}")
        self.engage_usd += pire
        return pire

    # ---- appel ----
    def appeler(self, espece: str, etape: str, prompt: str, max_tokens: int | None = None,
                angle: float | None = None, role: str = "") -> Resultat:
        """Sûr sous appels parallèles : le plafond est tenu au pire cas sur les appels en vol (jamais dépassé par
        la somme des pires cas), l'appel réseau se fait hors verrou, la comptabilité et le journal sous verrou."""
        m = modele_de(espece)
        max_tokens = int(max_tokens or m["max"])
        f = self.appelants.get(m["fournisseur"])
        if f is None:
            raise Arret(f"aucun appelant pour le fournisseur {m['fournisseur']!r}")
        with self._verrou:
            pire = self._reserver(m["prix"], prompt, max_tokens)
            self.compteur += 1
            ident = f"{etape}-{self.compteur:04d}"
            (self.dossier / "appels" / f"{ident}.prompt.txt").write_text(prompt, encoding="utf-8")
        debut = maintenant()
        try:
            rep = f(m["id"], prompt, max_tokens)
        except BaseException:
            with self._verrou:
                self.engage_usd = max(0.0, self.engage_usd - pire)
            raise
        fin_utc = maintenant()
        if rep.echec:
            statut = "ECHEC_API"
            if self.credit_epuise is None and credit_epuise(rep.echec):
                with self._verrou:  # CE3-05 : crédit épuisé en cours de course — consigné, la course sera arrêtée
                    if self.credit_epuise is None:
                        self.credit_epuise = {"espece": espece, "modele": m["id"], "echec": str(rep.echec)[:200]}
        elif not cv.modele_conforme(m["id"], rep.modele_servi):
            statut = "MODELE_NON_CONFORME"
        else:
            statut = cv.statut_reponse(m["fournisseur"], rep)
        texte = rep.texte if statut == "OK" else ""
        cout = cv.cout(m["prix"], rep.usage) if rep.usage else 0.0
        with self._verrou:
            self.engage_usd = max(0.0, self.engage_usd - pire)  # résidu flottant ramené à zéro
            self.depense_usd += cout
            (self.dossier / "appels" / f"{ident}.reponse.txt").write_text(rep.texte or "", encoding="utf-8")
            res = Resultat(identifiant=ident, espece=espece, statut=statut, texte=texte, modele_demande=m["id"],
                           modele_servi=rep.modele_servi, fin=rep.fin, categorie=rep.categorie, usage=dict(rep.usage),
                           cout_usd=round(cout, 6), echec=rep.echec, angle=angle)
            ligne = {
                "id": ident, "etape": etape, "role": role, "espece": espece, "famille": m["fournisseur"],
                "modele_demande": m["id"], "modele_servi": rep.modele_servi, "statut": statut, "fin": rep.fin,
                "categorie": rep.categorie, "usage": dict(rep.usage), "cout_usd": round(cout, 6),
                "cumul_usd": round(self.depense_usd, 6), "angle": angle, "max_tokens": max_tokens,
                "sha256_prompt": empreinte(prompt), "sha256_texte": empreinte(rep.texte or ""),
                "caracteres": len(rep.texte or ""), "debut_utc": debut, "fin_utc": fin_utc,
                "echec": (str(rep.echec)[:300] if rep.echec else None), "reel": self.reel, "go_id": self.go_id,
                # R-402 : types des blocs de la réponse (« thinking », « text », « thought »…), bornés ; jamais leur contenu ;
                # disent si la réflexion a eu lieu (contrat, § 3 : elle compte dans `max_tokens`)
                "types_blocs": [str(x)[:40] for x in (getattr(rep, "types_blocs", None) or [])][:20],
            }
            with self.journal.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(ligne, ensure_ascii=False, sort_keys=True) + "\n")
            depasse = self.depense_usd > self.plafond_usd
        if depasse:
            raise Arret(f"plafond {self.plafond_usd:.2f} USD dépassé après l'appel {ident} : {self.depense_usd:.2f}")
        return res

    def lire_journal(self) -> list[dict]:
        if not self.journal.exists():
            return []
        return [json.loads(l) for l in self.journal.read_text(encoding="utf-8").splitlines() if l.strip()]
