"""MATH500 : invite « qwen-boxed », lecture du jeu, vérificateur de réponse en boîte (exploratoire).

Invite. Le tableau 6 (p. 19) écrit `prompt_type = qwen-boxed`, nom d'un gabarit du banc d'évaluation de Qwen2.5-Math
(texte ChatML brut). Plan des étapes 0-1, § B.2 : lecture principale « gabarit_du_modele » (défaut) — gabarit de dialogue
de Llama, avec la consigne du système (« You are a helpful assistant. ») et la phrase finale de « qwen-boxed » ; variante
« litteral » : la chaîne de Qwen à la lettre. Libellé SUPPOSÉ (de mémoire, à relever sur le code public de l'outil
d'évaluation Qwen2.5-Math avant la course, plan § B.2 et condition 3 du devis).

Vérificateur. Extraction de la dernière boîte (`\\boxed{…}` ou `\\fbox{…}`, accolades appariées), normalisation à la
manière de Hendrycks et al. (fractions, `\\left`, unités en `\\text`, degrés, dollars, espaces), égalité des chaînes
normalisées, puis égalité numérique (entiers, décimaux, fractions simples, milliers à virgule). C'est une approximation du
juge du banc (qui passe par sympy) : l'écart se mesure à l'étape 0 sur les réponses de référence du jeu.
"""
from __future__ import annotations

import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path

from ..gardes import GardeArret

GABARIT_QWEN_BOXED = ("<|im_start|>system\nYou are a helpful assistant.<|im_end|>\n"
                      "<|im_start|>user\n{input}\nPlease reason step by step, and put your final answer within "
                      "\\boxed{{}}.<|im_end|>\n<|im_start|>assistant\n")
ARRETS_QWEN_BOXED = ("<|im_end|>", "<|endoftext|>")
CONSIGNE_UTILISATEUR = "{input}\nPlease reason step by step, and put your final answer within \\boxed{{}}."
CONSIGNE_SYSTEME = "You are a helpful assistant."
MODES_INVITE = ("litteral", "gabarit_du_modele")


def invite(probleme: str, mode: str = "gabarit_du_modele", gabarit_du_modele=None) -> str:
    """Texte de l'invite d'une question. `gabarit_du_modele(systeme, utilisateur) -> str` est exigé en mode
    « gabarit_du_modele » (aucun repli silencieux vers le mode littéral)."""
    if not isinstance(probleme, str) or not probleme.strip():
        raise GardeArret("énoncé vide ou non textuel")
    if mode == "litteral":
        return GABARIT_QWEN_BOXED.format(input=probleme)
    if mode == "gabarit_du_modele":
        if gabarit_du_modele is None:
            raise GardeArret("mode « gabarit_du_modele » sans gabarit fourni")
        return gabarit_du_modele(CONSIGNE_SYSTEME, CONSIGNE_UTILISATEUR.format(input=probleme))
    raise GardeArret(f"mode d'invite {mode!r} inconnu ({MODES_INVITE})")


def lire_math500(chemin: str | Path, effectif_attendu: int | None = 500) -> tuple[list[dict], str]:
    """Lit le jeu (une ligne JSON par question, champs `problem`, `answer`, `unique_id`) ; rend les questions et
    l'empreinte du fichier. Refus : champ absent, identifiant en double, effectif différent de l'attendu."""
    p = Path(chemin)
    octets = p.read_bytes()
    questions, vus = [], set()
    for n, ligne in enumerate(octets.decode("utf-8").splitlines(), 1):
        if not ligne.strip():
            continue
        q = json.loads(ligne)
        for cle in ("problem", "answer", "unique_id"):
            if not isinstance(q.get(cle), str) or not q[cle].strip():
                raise GardeArret(f"{p.name} ligne {n} : champ {cle} absent ou vide")
        if q["unique_id"] in vus:
            raise GardeArret(f"{p.name} ligne {n} : identifiant {q['unique_id']!r} en double")
        vus.add(q["unique_id"])
        questions.append({"id": q["unique_id"], "probleme": q["problem"], "reponse_attendue": q["answer"],
                          "sujet": q.get("subject"), "niveau": q.get("level")})
    if effectif_attendu is not None and len(questions) != effectif_attendu:
        raise GardeArret(f"{p.name} : {len(questions)} questions, {effectif_attendu} attendues")
    return questions, hashlib.sha256(octets).hexdigest()


# --- extraction de la boîte ------------------------------------------------------------------------------------------

def derniere_boite(texte: str) -> str | None:
    """Contenu de la dernière boîte `\\boxed{…}` / `\\fbox{…}` (accolades appariées) ou `\\boxed x` ; None sinon."""
    if not isinstance(texte, str):
        return None
    i = max(texte.rfind("\\boxed"), texte.rfind("\\fbox"))
    if i < 0:
        return None
    j = i + (len("\\boxed") if texte.startswith("\\boxed", i) else len("\\fbox"))
    if texte.startswith(" ", j) and not texte.startswith(" {", j):
        reste = texte[j + 1:]
        m = re.match(r"[^\s$]+", reste)
        return m.group(0) if m else None
    while j < len(texte) and texte[j] == " ":
        j += 1
    if j >= len(texte) or texte[j] != "{":
        return None
    profondeur, debut = 0, j + 1
    for k in range(j, len(texte)):
        if texte[k] == "{":
            profondeur += 1
        elif texte[k] == "}":
            profondeur -= 1
            if profondeur == 0:
                return texte[debut:k]
    return None                                     # boîte ouverte, jamais fermée (réponse coupée)


# --- normalisation ---------------------------------------------------------------------------------------------------

def _corriger_fractions(s: str) -> str:
    """`\\frac12` → `\\frac{1}{2}`, `\\frac1{2}` → `\\frac{1}{2}`."""
    morceaux = s.split("\\frac")
    sortie = morceaux[0]
    for m in morceaux[1:]:
        sortie += "\\frac"
        if m.startswith("{") or len(m) < 1:
            sortie += m
            continue
        a = m[0]
        if len(m) >= 2 and m[1] != "{":
            sortie += "{" + a + "}{" + m[1] + "}" + m[2:]
        elif len(m) >= 2:
            sortie += "{" + a + "}" + m[1:]
        else:
            sortie += m
    return sortie


def _corriger_racines(s: str) -> str:
    return re.sub(r"\\sqrt(\w)", r"\\sqrt{\1}", s)


def _texte_vers_contenu(s: str) -> str:
    return re.sub(r"\\(?:text|textbf|mbox|mathrm)\{([^{}]*)\}", r"\1", s)


def normaliser(reponse: str) -> str:
    s = str(reponse).strip()
    s = s.replace("\n", "").replace("\\!", "").replace("\\,", "").replace("\\;", "").replace("\\ ", "")
    s = s.replace("\\\\", "\\")
    s = s.replace("tfrac", "frac").replace("dfrac", "frac")
    s = s.replace("\\left", "").replace("\\right", "")
    s = s.replace("^{\\circ}", "").replace("^\\circ", "").replace("°", "")
    s = s.replace("\\$", "").replace("$", "")
    s = s.replace("\\%", "").replace("%", "")
    s = _texte_vers_contenu(s)
    s = re.sub(r"\s+", "", s)
    s = s.rstrip(".")
    for unite in ("degrees", "degree", "cm", "units", "unit", "inches", "inch", "meters", "dollars"):
        if s.endswith(unite) and len(s) > len(unite):
            s = s[: -len(unite)]
    if re.fullmatch(r"[a-zA-Z]=.+", s) and len(s.split("=")[0]) <= 2:
        s = s.split("=", 1)[1]
    s = _corriger_racines(_corriger_fractions(s))
    if s.startswith("."):
        s = "0" + s
    s = s.replace("{,}", ",")
    if re.fullmatch(r"-?\d+/\d+", s):
        a, b = s.split("/")
        s = f"\\frac{{{a}}}{{{b}}}"
    return s


def _nombre(s: str) -> Fraction | None:
    s = s.replace(",", "") if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", s) else s
    m = re.fullmatch(r"(-?)\\frac\{(-?\d+)\}\{(-?\d+)\}", s)
    if m:
        if int(m.group(3)) == 0:
            return None
        v = Fraction(int(m.group(2)), int(m.group(3)))
        return -v if m.group(1) else v
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        return Fraction(s)
    return None


def reponses_egales(obtenue: str | None, attendue: str) -> bool:
    if obtenue is None:
        return False
    a, b = normaliser(obtenue), normaliser(attendue)
    if a == b:
        return True
    x, y = _nombre(a), _nombre(b)
    if x is not None and y is not None:
        return abs(x - y) <= Fraction(1, 10**6) * max(1, abs(y))
    return False


def exiger_invite(texte: str, ids: list[int], decoupeur, entete: str) -> None:
    """Garde d'invite (plan, § B.3 point 2) : elle finit par l'en-tête de réponse ; décodée puis recodée, elle rend les
    mêmes jetons."""
    if not texte.endswith(entete):
        raise GardeArret(f"invite sans l'en-tête de réponse {entete!r} à la fin")
    if decoupeur.encoder(decoupeur.decoder(ids)) != list(ids):
        raise GardeArret("invite : décodée puis recodée, elle ne rend pas les mêmes jetons")


def noter(reponse: str, attendue: str, au_plafond: bool = False) -> dict:
    """Notation : boîte extraite (ou None), récompense (égalité normalisée ou numérique), récompense stricte (égalité
    des chaînes normalisées seule ; les désaccords sont comptés), drapeaux. Réponse coupée au plafond : r = 0."""
    boite = derniere_boite(reponse)
    r = int(reponses_egales(boite, attendue)) if not au_plafond else 0
    strict = int(boite is not None and not au_plafond and normaliser(boite) == normaliser(attendue))
    return {"boite": boite, "recompense": r, "recompense_stricte": strict, "sans_boite": boite is None,
            "au_plafond": bool(au_plafond)}
