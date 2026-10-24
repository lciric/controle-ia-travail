"""Espèces simulées : des doubles d'appelants, sans réseau, pour tester le noyau et ses gardes (R5).

Chaque double lit la consigne (reconnue par sa première phrase) et répond comme une espèce de compétence réglable :
- amorçage (« Tu écris la génération 0 d'un organisme ») : rend un organisme pris dans un dossier de fixtures
  (`organisme_amorcage`), au format FICHIER/FIN FICHIER du contrat ;
- tâche : juste avec probabilité `p_connu` si la catégorie d'indice est connue (une connaissance « catégorie x »
  visible dans la consigne), sinon `p_base` ;
- découverte : propose `k` candidats, réels (catégorie présente dans le contexte) avec probabilité `q_decouverte` ;
- vérification : juste avec probabilité `p_verif` sur chaque item (canari de la banque, ou candidat) ;
- consigne d'un organisme inconnu : lecture générique — réponse de tâche si la consigne contient les deux étiquettes
  d'une famille (JSON sur une ligne), énoncé d'induction si elle contient plusieurs exemples avec vérité ;
- tout autre texte : phrases à jetons mathématiques.

Pannes programmables (`pannes`) : erreur d'interface (404), réponse vide, modèle servi non conforme, amorçage sans
manifeste, canaris tous rejetés — pour tester chaque garde sur un cas sain et sur un artefact.
"""
from __future__ import annotations

import json
import pathlib
import re

import numpy as np

from .noyau.appels import cv
from .noyau.taches import CATEGORIES, ETIQUETTES, PHRASES_INDICE
from .outils import canaris as _canaris

VOCABULAIRE = [r"\alpha", r"\beta", r"\lambda", r"\sigma", r"\theta", r"\mu", r"\partial", r"\nabla", r"\mathbb{E}",
               r"\mathcal{L}", r"\otimes", r"\perp", r"\subseteq", "P_{do}", "S_{TD}", "h_t", "z_t", "d_z",
               "martingale", "projecteur", "résidu", "spectre", "permutation", "canari", "bandit", "entropie",
               "divergence", "idempotent", "orthogonal", "sabotage", "délégation", "collusion", "stéganographie",
               "horodatage", "gabarit", "moniteur", "alerte", "journal", "seuil", "calibration", "quantile", "bootstrap"]

MOTIF_CONNAISSANCE_CAT = re.compile(r"cat[ée]gorie ([a-z-]+)")
MOTIF_EXTRAIT = re.compile(r"EXTRAIT :\n(.*?)\n\nCONNAISSANCES", re.S)
MOTIF_CONTEXTE = re.compile(r"CONTEXTE :\n(.*?)\n\n(?:DÉJÀ FERMÉ|ITEMS)", re.S)
MOTIF_ITEMS = re.compile(r"^\[(item-\d\d)\] (.*)$", re.M)
MOTIF_CANDIDAT_CAT = re.compile(r"\(cat[ée]gorie ([a-z-]+)\)")

TOUTES_CATEGORIES = [c for fam in CATEGORIES.values() for c in fam]
VERITE_CANARIS = {e: v for e, v in _canaris.BANQUE}
FIXTURES = pathlib.Path(__file__).resolve().parent.parent / "tests" / "fixtures"


def organisme_en_texte(dossier: pathlib.Path) -> str:
    """Sérialise `dossier/organisme/` au format du contrat."""
    racine = dossier / "organisme"
    morceaux = []
    for f in sorted(racine.rglob("*")):
        if f.is_file() and "__pycache__" not in f.parts:
            morceaux.append(f"<<<FICHIER organisme/{f.relative_to(racine).as_posix()}>>>\n{f.read_text(encoding='utf-8')}\n<<<FIN FICHIER>>>")
    return "Voici l'organisme.\n\n" + "\n\n".join(morceaux)


class EspeceSimulee:
    def __init__(self, modele_id: str, rng: np.random.Generator, p_base: float = 0.55, p_connu: float = 0.95,
                 q_decouverte: float = 0.7, k_candidats: int = 3, p_verif: float = 0.92, zipf: float = 1.1,
                 pannes: dict | None = None, organisme_amorcage: str | pathlib.Path | None = None):
        self.modele_id = modele_id
        self.rng = rng
        self.p_base, self.p_connu = p_base, p_connu
        self.q_decouverte, self.k_candidats, self.p_verif = q_decouverte, k_candidats, p_verif
        self.zipf = zipf
        self.pannes = dict(pannes or {})
        self.organisme_amorcage = pathlib.Path(organisme_amorcage) if organisme_amorcage else FIXTURES / "organisme_factice"
        self.appels: list[dict] = []
        self.compteur = 0

    def _fin(self):
        return "STOP" if self.modele_id.startswith("gemini") else "end_turn"

    def _reponse(self, texte: str, prompt: str) -> cv.Reponse:
        usage = {"entree": max(1, len(prompt) // 4), "sortie": max(1, len(texte) // 4)}
        return cv.Reponse(texte=texte, modele_servi=self.modele_id, identifiant=f"sim-{self.compteur}", fin=self._fin(), usage=usage)

    def _texte_math(self, n: int = 40) -> str:
        poids = 1.0 / np.arange(1, len(VOCABULAIRE) + 1) ** self.zipf
        poids /= poids.sum()
        mots = self.rng.choice(VOCABULAIRE, size=n, p=poids)
        return "Exploration : " + " ".join(f"${m}$" if m.startswith("\\") or "_" in m else m for m in mots) + \
               f". On pose $$\\mathcal{{L}}_{{{self.compteur}}} = \\sum_i {mots[0]} \\cdot {mots[1]}$$."

    def _panne(self, genre: str) -> bool:
        p = self.pannes.get(genre)
        if p is None:
            return False
        if isinstance(p, (set, list, tuple)):
            return self.compteur in p
        return self.rng.random() < float(p)

    def _amorcage(self) -> str:
        texte = organisme_en_texte(self.organisme_amorcage)
        if self._panne("amorcage_sans_manifeste"):
            texte = re.sub(r"<<<FICHIER organisme/manifeste.json>>>.*?<<<FIN FICHIER>>>", "", texte, flags=re.S)
        return texte

    def _tache(self, prompt: str) -> str:
        m_fam = re.search(r"famille « ([a-z-]+) »", prompt)
        fam = m_fam.group(1) if m_fam else "conscience-evaluation"
        pos, neg = ETIQUETTES[fam]
        extrait = MOTIF_EXTRAIT.search(prompt)
        texte = extrait.group(1) if extrait else ""
        cat_presente = next((c for c in CATEGORIES[fam] if PHRASES_INDICE[c] in texte), None)
        connues = set(MOTIF_CONNAISSANCE_CAT.findall(prompt.lower()))
        verite = pos if cat_presente else neg
        if cat_presente and cat_presente in connues:
            juste = self.rng.random() < self.p_connu
        elif cat_presente:
            juste = self.rng.random() < self.p_base
        else:
            juste = self.rng.random() < (self.p_connu if connues else self.p_base)
        etiquette = verite if juste else (neg if verite == pos else pos)
        ids = re.findall(r"\[(C-\d{4})\]", prompt)
        return "Analyse.\n```json\n" + json.dumps({"etiquette": etiquette, "confiance": 0.8 if juste else 0.6,
                                                   "connaissances_utilisees": ids[:2], "indice": cat_presente or ""}) + "\n```"

    def _decouverte(self, prompt: str) -> str:
        ctx = MOTIF_CONTEXTE.search(prompt)
        contexte = ctx.group(1) if ctx else ""
        presentes = [c for c in TOUTES_CATEGORIES if PHRASES_INDICE[c] in contexte]
        deja = set(MOTIF_CANDIDAT_CAT.findall(prompt))
        candidats = []
        for _ in range(self.k_candidats):
            if presentes and self.rng.random() < self.q_decouverte:
                restantes = [c for c in presentes if c not in deja] or presentes
                cat, conf = str(self.rng.choice(restantes)), 0.8
            else:
                absentes = [c for c in TOUTES_CATEGORIES if c not in presentes] or TOUTES_CATEGORIES
                cat, conf = str(self.rng.choice(absentes)), 0.6
            deja.add(cat)
            candidats.append({"enonce": f"Indice utile : « {PHRASES_INDICE[cat]} » (catégorie {cat})",
                              "mecanisme": "présence de l'indice dans les exemples positifs", "confiance": conf})
        return "Candidats.\n```json\n" + json.dumps({"candidats": candidats}, ensure_ascii=False) + "\n```"

    def _verification(self, prompt: str) -> str:
        ctx = MOTIF_CONTEXTE.search(prompt)
        contexte = ctx.group(1) if ctx else ""
        verdicts = {}
        for ident, enonce in MOTIF_ITEMS.findall(prompt):
            if enonce in VERITE_CANARIS:
                vrai = VERITE_CANARIS[enonce]
            else:
                m = MOTIF_CANDIDAT_CAT.search(enonce)
                vrai = bool(m and PHRASES_INDICE.get(m.group(1), "\u0000") in contexte)
            if self._panne("canaris_tout_invalide"):
                vrai = False
            elif self.rng.random() >= self.p_verif:
                vrai = not vrai
            verdicts[ident] = "VALIDE" if vrai else "INVALIDE"
        return "Verdicts.\n```json\n" + json.dumps({"verdicts": verdicts, "justifications": {}}) + "\n```"

    def __call__(self, modele_id: str, prompt: str, max_tokens: int) -> cv.Reponse:
        self.compteur += 1
        self.appels.append({"modele": modele_id, "n": self.compteur, "debut": prompt[:60]})
        if self._panne("404"):
            return cv.Reponse(echec="HTTP 404 : Not Found")
        if self._panne("vide"):
            return cv.Reponse(texte="", modele_servi=self.modele_id, fin=self._fin(), usage={"entree": 10, "sortie": 0})
        if self._panne("modele_non_conforme"):
            r = self._reponse("texte", prompt)
            r.modele_servi = "claude-3-5-sonnet-20241022"
            return r
        if prompt.startswith("Tu écris la génération 0 d'un organisme"):
            texte = self._amorcage()
        elif prompt.startswith("Tâche de la famille"):
            texte = self._tache(prompt)
        elif prompt.startswith("Tu es un attaquant de l'étage M1"):
            texte = self._decouverte(prompt)
        elif prompt.startswith("Tu es un vérificateur isolé"):
            texte = self._verification(prompt)
        else:
            texte = self._generique(prompt)
        return self._reponse(texte, prompt)

    # ---- consignes d'organismes inconnus : lecture générique (les espèces simulées ne sont pas écrites pour un
    # organisme ; elles doivent répondre à n'importe quelle consigne qui contient une tâche de la banque) ----
    def _generique(self, prompt: str) -> str:
        """Si la consigne contient les deux étiquettes d'une famille et au plus une phrase d'indice placée en fin de
        consigne : réponse de tâche (JSON sur une ligne) ; si elle contient plusieurs exemples avec vérité : énoncé
        d'induction qui nomme les catégories présentes ; sinon : texte mathématique."""
        bas = prompt.lower()
        familles = [f for f, (pos, neg) in ETIQUETTES.items() if pos in bas and neg in bas]
        positions = {c: prompt.rfind(PHRASES_INDICE[c]) for c in TOUTES_CATEGORIES if PHRASES_INDICE[c] in prompt}
        n_verites = len(re.findall(r"v[ée]rit[ée]\s*[:=]", bas))
        if n_verites >= 3 and positions:
            lignes = [f"Indice récurrent chez les positifs : « {PHRASES_INDICE[c]} » (catégorie {c})." for c in sorted(positions, key=positions.get)]
            return "Invariants observés :\n" + "\n".join(lignes) + "\nRègle : la présence d'un de ces indices vaut étiquette positive."
        if familles:
            # plusieurs familles nommées (règles apprises, mémoire…) : la tâche à juger est celle dont les étiquettes
            # sont citées le plus tard dans la consigne
            fam = max(familles, key=lambda f: max(bas.rfind(ETIQUETTES[f][0]), bas.rfind(ETIQUETTES[f][1])))
            pos, neg = ETIQUETTES[fam]
            # l'indice retenu est le dernier du texte : la tâche à juger vient après les règles et la mémoire
            cat_presente = max(positions, key=positions.get) if positions else None
            if cat_presente is not None and cat_presente not in CATEGORIES[fam]:
                cat_presente = None
            connues = set(MOTIF_CONNAISSANCE_CAT.findall(bas))
            verite = pos if cat_presente else neg
            if cat_presente and cat_presente in connues:
                juste = self.rng.random() < self.p_connu
            elif cat_presente:
                juste = self.rng.random() < self.p_base
            else:
                juste = self.rng.random() < (self.p_connu if connues else self.p_base)
            etiquette = verite if juste else (neg if verite == pos else pos)
            return ("Faits examinés : " + (f"indice de catégorie {cat_presente}." if cat_presente else "aucun indice net.") +
                    "\n" + json.dumps({"etiquette": etiquette, "confiance": 0.8 if juste else 0.6, "raisonnement": "lecture de la trace"}))
        return self._texte_math()


def appelants_simules(rng: np.random.Generator, **options) -> tuple[dict, dict]:
    """Un double par identifiant de modèle ; `options` : {"A": {...}, "B": {...}, "C": {...}, "commun": {...}}."""
    commun = options.get("commun", {})
    especes = {
        "claude-fable-5-1": EspeceSimulee("claude-fable-5-1", rng, **{**commun, **options.get("A", {})}),
        "claude-opus-5-5": EspeceSimulee("claude-opus-5-5", rng, **{**commun, **options.get("B", {})}),
        "gemini-4-argon": EspeceSimulee("gemini-4-argon", rng, **{**commun, **options.get("C", {})}),
    }

    def servir(modele_id, prompt, max_tokens):
        e = especes.get(modele_id)
        if e is None:
            return cv.Reponse(echec=f"HTTP 404 : modèle inconnu {modele_id}")
        return e(modele_id, prompt, max_tokens)

    return {"anthropic": servir, "gemini": servir}, especes
